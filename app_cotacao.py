"""
=============================================================================
APLICACAO WEB - COTACAO HAPVIDA (AI-DRIVEN)
=============================================================================
Aplicacao Flask com agente de IA (Claude Vision) para cotar planos Hapvida.
O agente usa screenshots para "ver" a pagina e decidir acoes,
adaptando-se a mudancas no layout e opcoes disponiveis.

Acesse: http://localhost:5000

Requer: ANTHROPIC_API_KEY no ambiente
=============================================================================
"""

import os
import re
import time
import json
import base64
import threading

from flask import Flask, render_template, request, jsonify

# Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

# Anthropic
import anthropic

app = Flask(__name__)

# ============================================
# CONFIGURACOES
# ============================================
EMAIL = os.environ.get("COTADOR_EMAIL", "jessicamendesbarbosa5@gmail.com")
SENHA = os.environ.get("COTADOR_SENHA", "amovoced28")
URL_LOGIN = "https://app.cotadorsimplificado.com.br/login"
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
AI_MODEL = os.environ.get("AI_MODEL", "claude-sonnet-4-20250514")

# Estado global
driver_global = None
logado = False
primeira_cotacao = True

FAIXAS_ETARIAS = [
    "0 a 18 anos",
    "19 a 23 anos",
    "24 a 28 anos",
    "29 a 33 anos",
    "34 a 38 anos",
    "39 a 43 anos",
    "44 a 48 anos",
    "49 a 53 anos",
    "54 a 58 anos",
    "59 anos ou mais",
]


# ============================================
# AGENTE DE IA PARA NAVEGACAO
# ============================================

class AIBrowserAgent:
    """
    Agente que combina Selenium + Claude Vision.
    Tira screenshots, envia para Claude, recebe acoes e executa no navegador.
    Adapta-se a mudancas de layout porque "ve" a pagina como um humano.
    """

    SYSTEM_PROMPT = """Voce e um agente de automacao web especializado em cotar planos de saude no site "Cotador Simplificado" (app.cotadorsimplificado.com.br).

Voce recebe uma screenshot da pagina atual e um objetivo. Decida a PROXIMA acao usando uma das ferramentas.

REGRAS:
1. Analise a screenshot com cuidado - identifique botoes, campos, dropdowns, modais
2. Use o texto EXATO visivel na tela ao clicar em elementos
3. Se um popup/modal estiver bloqueando, feche-o primeiro
4. Se a acao anterior falhou, tente uma abordagem alternativa
5. Quando o objetivo for alcancado, use "done"
6. Seja conciso nas mensagens - nao explique demais

DICAS DO SITE:
- Botoes principais: "Cotar Hapvida", "Avancar", "Voltar", "Add Produtos"
- O site usa modais para selecao de produtos (operadora > tabela > plano > acomodacao)
- Campos de faixa etaria tem placeholder "0"
- O campo de cidade e autocomplete - digite e selecione do dropdown
- O X vermelho fecha modais de produtos"""

    TOOLS = [
        {
            "name": "click_element",
            "description": "Clica em um elemento pelo texto visivel. Use para botoes, links, opcoes.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "Texto visivel do elemento (exato ou parcial)"
                    },
                    "match_type": {
                        "type": "string",
                        "enum": ["exact", "contains"],
                        "description": "Tipo de match. Default: contains"
                    },
                    "index": {
                        "type": "integer",
                        "description": "Indice se houver multiplos (0=primeiro). Default: 0"
                    }
                },
                "required": ["text"]
            }
        },
        {
            "name": "type_in_field",
            "description": "Digita texto em um campo de input. Limpa o campo antes.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "field_hint": {
                        "type": "string",
                        "description": "Placeholder, label ou descricao do campo (ex: 'email', 'senha', 'cliente', 'cidade')"
                    },
                    "text": {
                        "type": "string",
                        "description": "Texto para digitar"
                    },
                    "press_enter": {
                        "type": "boolean",
                        "description": "Pressionar Enter apos digitar. Default: false"
                    }
                },
                "required": ["field_hint", "text"]
            }
        },
        {
            "name": "select_dropdown",
            "description": "Seleciona opcao de um dropdown/select nativo.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "option_text": {
                        "type": "string",
                        "description": "Texto da opcao para selecionar"
                    }
                },
                "required": ["option_text"]
            }
        },
        {
            "name": "fill_age_brackets",
            "description": "Preenche todos os campos de faixa etaria (placeholder='0') com um valor.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "value": {
                        "type": "string",
                        "description": "Valor para cada campo. Default: '1'"
                    }
                },
                "required": ["value"]
            }
        },
        {
            "name": "scroll",
            "description": "Rola a pagina.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "direction": {
                        "type": "string",
                        "enum": ["down", "up"],
                        "description": "Direcao"
                    },
                    "pixels": {
                        "type": "integer",
                        "description": "Quantidade em pixels. Default: 500"
                    }
                },
                "required": ["direction"]
            }
        },
        {
            "name": "wait_for_page",
            "description": "Espera a pagina carregar/atualizar.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "seconds": {
                        "type": "number",
                        "description": "Segundos. Default: 2"
                    }
                },
                "required": []
            }
        },
        {
            "name": "press_escape",
            "description": "Pressiona ESC para fechar modais/popups.",
            "input_schema": {
                "type": "object",
                "properties": {},
                "required": []
            }
        },
        {
            "name": "done",
            "description": "O objetivo foi alcancado. Use quando terminar a tarefa.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "success": {
                        "type": "boolean",
                        "description": "Se teve sucesso"
                    },
                    "message": {
                        "type": "string",
                        "description": "Descricao breve do resultado"
                    }
                },
                "required": ["success"]
            }
        }
    ]

    def __init__(self, driver, api_key, model=None):
        self.driver = driver
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = model or AI_MODEL
        self.action_log = []

    def screenshot_b64(self):
        """Tira screenshot e retorna como base64 PNG."""
        return self.driver.get_screenshot_as_base64()

    def page_info(self):
        """Info basica da pagina atual."""
        return f"URL: {self.driver.current_url} | Titulo: {self.driver.title}"

    # ------------------------------------------
    # EXECUCAO DE OBJETIVOS
    # ------------------------------------------

    def execute_goal(self, goal, max_steps=15):
        """
        Executa um objetivo de alto nivel usando IA.
        A cada passo: screenshot -> pergunta ao Claude -> executa acao.
        Repete ate Claude chamar 'done' ou atingir max_steps.
        """
        self.action_log = []

        for step in range(1, max_steps + 1):
            print(f"  [AI passo {step}/{max_steps}] Analisando...")

            img = self.screenshot_b64()
            info = self.page_info()
            history = "\n".join(self.action_log[-6:]) or "(nenhuma)"

            # Monta mensagem para Claude
            user_content = [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/png",
                        "data": img,
                    },
                },
                {
                    "type": "text",
                    "text": (
                        f"OBJETIVO: {goal}\n\n"
                        f"PAGINA: {info}\n\n"
                        f"HISTORICO DE ACOES:\n{history}\n\n"
                        "Qual a proxima acao?"
                    ),
                },
            ]

            try:
                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=512,
                    system=self.SYSTEM_PROMPT,
                    messages=[{"role": "user", "content": user_content}],
                    tools=self.TOOLS,
                    tool_choice={"type": "any"},
                )
            except Exception as e:
                print(f"  [AI] Erro na API: {e}")
                return {"sucesso": False, "erro": f"Erro na API Claude: {e}"}

            # Processa resposta
            result = self._handle_response(response)

            if result.get("done"):
                success = result.get("success", True)
                msg = result.get("message", "")
                print(f"  [AI] {'Concluido' if success else 'Falhou'}: {msg}")
                return {"sucesso": success, "mensagem": msg}

            time.sleep(0.3)

        print(f"  [AI] Maximo de {max_steps} passos atingido")
        return {"sucesso": False, "erro": f"Nao concluiu em {max_steps} passos"}

    def _handle_response(self, response):
        """Processa a resposta do Claude e executa a acao."""
        for block in response.content:
            if block.type == "tool_use":
                name = block.name
                inp = block.input
                log_line = f"{name}({json.dumps(inp, ensure_ascii=False)[:120]})"
                self.action_log.append(log_line)
                print(f"  [AI] -> {log_line}")
                return self._run_action(name, inp)
        return {}

    # ------------------------------------------
    # ACOES DO NAVEGADOR
    # ------------------------------------------

    def _run_action(self, name, params):
        """Dispatch da acao para o metodo correto."""
        try:
            if name == "click_element":
                return self._click(params)
            elif name == "type_in_field":
                return self._type(params)
            elif name == "select_dropdown":
                return self._select(params)
            elif name == "fill_age_brackets":
                return self._fill_brackets(params)
            elif name == "scroll":
                return self._scroll(params)
            elif name == "wait_for_page":
                time.sleep(params.get("seconds", 2))
                return {}
            elif name == "press_escape":
                self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
                time.sleep(0.5)
                return {}
            elif name == "done":
                return {
                    "done": True,
                    "success": params.get("success", True),
                    "message": params.get("message", ""),
                }
            return {}
        except Exception as e:
            err = f"Erro em {name}: {e}"
            print(f"  [AI] {err}")
            self.action_log.append(f"ERRO: {err}")
            return {}

    def _click(self, params):
        """Clica em elemento pelo texto visivel."""
        text = params["text"]
        match = params.get("match_type", "contains")
        idx = params.get("index", 0)

        if match == "exact":
            xpath = f"//*[normalize-space(text())='{text}']"
        else:
            xpath = f"//*[contains(text(), '{text}')]"

        elements = self.driver.find_elements(By.XPATH, xpath)
        visible = [e for e in elements if self._is_visible(e)]

        if not visible:
            # Fallback: tenta em botoes, spans, divs, labels
            for tag in ["button", "a", "span", "div", "label", "li"]:
                elems = self.driver.find_elements(
                    By.XPATH, f"//{tag}[contains(., '{text}')]"
                )
                vis = [e for e in elems if self._is_visible(e)]
                if vis:
                    visible = vis
                    break

        if visible and idx < len(visible):
            el = visible[idx]
            try:
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", el
                )
                time.sleep(0.3)
                self.driver.execute_script("arguments[0].click();", el)
            except Exception:
                ActionChains(self.driver).move_to_element(el).click().perform()
            time.sleep(1)
        else:
            self.action_log.append(f"AVISO: '{text}' nao encontrado")

        return {}

    def _type(self, params):
        """Digita texto em um campo."""
        hint = params["field_hint"].lower()
        text = params["text"]
        press_enter = params.get("press_enter", False)

        el = self._find_input(hint)

        if el:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", el
            )
            time.sleep(0.2)
            self.driver.execute_script("arguments[0].click();", el)
            time.sleep(0.2)
            # Seleciona tudo e sobrescreve
            self.driver.execute_script("arguments[0].select();", el)
            time.sleep(0.1)
            el.send_keys(text)
            if press_enter:
                time.sleep(0.3)
                el.send_keys(Keys.ENTER)
            time.sleep(0.5)
        else:
            self.action_log.append(f"AVISO: Campo '{hint}' nao encontrado")

        return {}

    def _find_input(self, hint):
        """Encontra input por hint (placeholder, type, label proximo)."""
        inputs = self.driver.find_elements(
            By.CSS_SELECTOR, "input:not([type='hidden']), textarea"
        )

        # Por placeholder
        for inp in inputs:
            if self._is_visible(inp) and inp.is_enabled():
                ph = (inp.get_attribute("placeholder") or "").lower()
                if hint in ph:
                    return inp

        # Por type (email, password)
        type_map = {
            "email": "email",
            "e-mail": "email",
            "senha": "password",
            "password": "password",
        }
        for key, input_type in type_map.items():
            if key in hint:
                for inp in inputs:
                    if (
                        self._is_visible(inp)
                        and inp.get_attribute("type") == input_type
                    ):
                        return inp

        # Por label proximo
        try:
            label = self.driver.find_element(
                By.XPATH, f"//*[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'), '{hint}')]"
            )
            parent = label
            for _ in range(3):
                parent = parent.find_element(By.XPATH, "..")
                found = parent.find_elements(By.CSS_SELECTOR, "input, textarea")
                for f in found:
                    if self._is_visible(f) and f.is_enabled():
                        return f
        except Exception:
            pass

        # Por placeholder com " - " (campo de cidade)
        if "cidade" in hint or "city" in hint:
            for inp in inputs:
                if self._is_visible(inp) and inp.is_enabled():
                    ph = inp.get_attribute("placeholder") or ""
                    if " - " in ph:
                        return inp

        return None

    def _select(self, params):
        """Seleciona opcao de dropdown nativo."""
        option_text = params["option_text"]
        selects = self.driver.find_elements(By.CSS_SELECTOR, "select")
        for sel in selects:
            if self._is_visible(sel):
                try:
                    s = Select(sel)
                    for opt in s.options:
                        if option_text.lower() in opt.text.lower():
                            s.select_by_visible_text(opt.text)
                            time.sleep(0.5)
                            return {}
                except Exception:
                    continue
        # Fallback: clica no texto como elemento normal
        return self._click({"text": option_text, "match_type": "contains"})

    def _fill_brackets(self, params):
        """Preenche campos de faixa etaria."""
        value = params.get("value", "1")
        inputs = self.driver.find_elements(
            By.CSS_SELECTOR, "input[placeholder='0']"
        )
        count = 0
        for inp in inputs[:10]:
            try:
                if self._is_visible(inp) and inp.is_enabled():
                    inp.clear()
                    inp.send_keys(value)
                    count += 1
            except Exception:
                pass
        print(f"  [AI] Preencheu {count} campos de faixa etaria com '{value}'")
        time.sleep(0.5)
        return {}

    def _scroll(self, params):
        """Rola pagina."""
        d = params["direction"]
        px = params.get("pixels", 500)
        self.driver.execute_script(
            f"window.scrollBy(0, {px if d == 'down' else -px});"
        )
        time.sleep(0.5)
        return {}

    def _is_visible(self, el):
        """Verifica se elemento esta visivel."""
        try:
            return el.is_displayed()
        except Exception:
            return False

    # ------------------------------------------
    # EXTRACAO DE VALORES COM IA
    # ------------------------------------------

    def extract_price_values(self):
        """
        Usa Claude Vision para ler os valores de cotacao da tela.
        Retorna lista de {faixa_etaria, valor}.
        """
        # Rola para baixo para garantir que valores estejam visiveis
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
        time.sleep(1.5)

        img = self.screenshot_b64()

        prompt = """Analise esta screenshot de uma cotacao de plano de saude.
Extraia TODOS os valores monetarios visiveis, associando cada valor a sua faixa etaria.

As faixas etarias sao (nesta ordem):
1. 0 a 18 anos
2. 19 a 23 anos
3. 24 a 28 anos
4. 29 a 33 anos
5. 34 a 38 anos
6. 39 a 43 anos
7. 44 a 48 anos
8. 49 a 53 anos
9. 54 a 58 anos
10. 59 anos ou mais

IMPORTANTE: Retorne APENAS um JSON valido, sem markdown, neste formato:
[{"faixa_etaria": "0 a 18 anos", "valor": "R$ 123,45"}, ...]

Se nao conseguir ver valores, retorne: []"""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image",
                                "source": {
                                    "type": "base64",
                                    "media_type": "image/png",
                                    "data": img,
                                },
                            },
                            {"type": "text", "text": prompt},
                        ],
                    }
                ],
            )

            text = response.content[0].text.strip()
            # Extrai JSON da resposta
            json_match = re.search(r"\[.*\]", text, re.DOTALL)
            if json_match:
                valores = json.loads(json_match.group())
                print(f"  [AI] Extraidos {len(valores)} valores")
                return valores

        except Exception as e:
            print(f"  [AI] Erro ao extrair valores: {e}")

        # Fallback: tenta extrair do DOM
        return self._extract_values_dom()

    def _extract_values_dom(self):
        """Fallback: extrai valores direto do DOM."""
        valores = []
        try:
            all_elements = self.driver.find_elements(By.XPATH, "//*")
            found = []
            for el in all_elements:
                try:
                    txt = el.text.strip()
                    if txt and "," in txt and len(txt) < 15:
                        clean = (
                            txt.replace(".", "")
                            .replace(",", ".")
                            .replace("R$", "")
                            .replace(" ", "")
                        )
                        val = float(clean)
                        if 30 < val < 3000:
                            found.append(txt)
                except Exception:
                    pass

            # Remove duplicatas mantendo ordem
            seen = set()
            unique = []
            for v in found:
                if v not in seen:
                    seen.add(v)
                    unique.append(v)

            for i, val in enumerate(unique[:10]):
                if i < len(FAIXAS_ETARIAS):
                    formatted = val if val.startswith("R$") else f"R$ {val}"
                    valores.append(
                        {"faixa_etaria": FAIXAS_ETARIAS[i], "valor": formatted}
                    )

        except Exception as e:
            print(f"  [AI] Fallback DOM tambem falhou: {e}")

        return valores


# ============================================
# NAVEGADOR
# ============================================

def iniciar_navegador():
    """Inicia o navegador Chrome/Chromium em modo headless."""
    global driver_global

    print("[*] Iniciando navegador...")

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-setuid-sandbox")
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("--no-zygote")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--disable-background-networking")
    chrome_options.add_argument("--disable-default-apps")
    chrome_options.add_argument("--remote-debugging-port=9222")

    chromium_bin = os.environ.get("CHROME_BIN", "/usr/bin/chromium")
    if os.path.exists(chromium_bin):
        chrome_options.binary_location = chromium_bin

    chromedriver_paths = [
        os.environ.get("CHROMEDRIVER_PATH", ""),
        "/usr/bin/chromedriver",
        "/usr/local/bin/chromedriver",
    ]

    for path in chromedriver_paths:
        if path and os.path.exists(path):
            try:
                service = Service(path)
                driver_global = webdriver.Chrome(
                    service=service, options=chrome_options
                )
                print(f"[OK] Navegador iniciado com {path}")
                return driver_global
            except Exception as e:
                print(f"[AVISO] Falhou com {path}: {e}")

    print("[*] Usando webdriver-manager...")
    service = Service(ChromeDriverManager().install())
    driver_global = webdriver.Chrome(service=service, options=chrome_options)
    return driver_global


# ============================================
# FLUXO DE COTACAO AI-DRIVEN
# ============================================

def fazer_login_ai(agent):
    """Faz login usando o agente de IA."""
    global logado

    driver = agent.driver
    print("[*] Acessando pagina de login...")
    driver.get(URL_LOGIN)
    time.sleep(3)

    result = agent.execute_goal(
        f"Faca login no site. "
        f"1) Digite o email '{EMAIL}' no campo de email. "
        f"2) Clique no botao 'Continuar com Email'. "
        f"3) Aguarde o campo de senha aparecer. "
        f"4) Digite a senha '{SENHA}' no campo de senha. "
        f"5) Clique no botao 'Entrar'. "
        f"6) Se aparecer algum popup/aviso apos o login, feche-o. "
        f"7) Quando estiver na pagina inicial (nao mais na pagina de login), sinalize done.",
        max_steps=12,
    )

    if "login" not in driver.current_url.lower():
        logado = True
        print("[OK] Login realizado com sucesso!")
        return True

    print("[ERRO] Login falhou")
    return False


def cotar_cidade_ai(agent, cidade, config):
    """
    Executa cotacao completa para uma cidade (fluxo inicial).
    Usa IA para navegar cada etapa com parametros configuraveis.
    """
    driver = agent.driver
    operadora = config.get("operadora", "Hapvida")
    tabela = config.get("tabela", "+ Odonto")
    plano = config.get("plano", "Ambulatorial")
    acomodacao = config.get("acomodacao", "Sem acomodacao / Com coparticipacao")
    tipo_empresa = config.get("tipo_empresa", "MEI - Empresario individual")
    vidas = config.get("vidas_por_faixa", "1")

    try:
        # ---- FASE 1: Pagina inicial -> Cotar Hapvida -> PME -> Nome -> Avancar ----
        print(f"[*] Fase 1: Setup inicial para {cidade}...")
        driver.get("https://app.cotadorsimplificado.com.br/")
        time.sleep(2)

        result = agent.execute_goal(
            "Na pagina inicial do Cotador Simplificado: "
            "1) Feche qualquer popup/aviso que esteja aparecendo. "
            "2) Clique em 'Cotar Hapvida'. "
            "3) Selecione 'PME ate 29 vidas'. "
            "4) Preencha o nome do cliente com 'teste'. "
            "5) Clique em 'Avancar'. "
            "Sinalize done quando estiver na tela de selecao de cidade.",
            max_steps=10,
        )

        if not result.get("sucesso", True):
            return _erro(cidade, result.get("erro", "Falha no setup inicial"))

        # ---- FASE 2: Cidade + Tipo empresa ----
        print(f"[*] Fase 2: Selecionando cidade {cidade}...")
        result = agent.execute_goal(
            f"Nesta tela de selecao: "
            f"1) No campo de cidade (que pode ter um placeholder com nome de cidade e estado), "
            f"   limpe o campo e digite '{cidade}'. "
            f"2) Espere o dropdown aparecer e clique na opcao que contem '{cidade}'. "
            f"3) No dropdown de tipo de empresa, selecione '{tipo_empresa}'. "
            f"4) Clique em 'Avancar'. "
            f"Sinalize done quando estiver na tela de faixas etarias.",
            max_steps=10,
        )

        if not result.get("sucesso", True):
            return _erro(cidade, result.get("erro", "Falha na selecao de cidade"))

        # ---- FASE 3: Faixas etarias ----
        print(f"[*] Fase 3: Preenchendo faixas etarias...")
        result = agent.execute_goal(
            f"Preencha todos os campos de faixa etaria com '{vidas}'. "
            f"Os campos tem placeholder '0'. Existem 10 campos. "
            f"Apos preencher, clique em 'Avancar'. "
            f"Sinalize done quando avancar para a proxima tela.",
            max_steps=6,
        )

        if not result.get("sucesso", True):
            return _erro(cidade, result.get("erro", "Falha nas faixas etarias"))

        # ---- FASE 4: Configuracao de produtos (modal) ----
        print(f"[*] Fase 4: Configurando produtos...")
        result = agent.execute_goal(
            f"Configure os produtos da cotacao: "
            f"1) Clique em 'Add Produtos' (botao). "
            f"2) No modal que abrir, siga esta sequencia: "
            f"   a) Clique na operadora '{operadora}' (cuidado para nao clicar em variantes como 'Hapvida - Affix'). "
            f"   b) Clique na tabela que contem '{tabela}' (a opcao com odonto se '{tabela}' for '+ Odonto'). "
            f"   c) Clique no plano '{plano}'. "
            f"   d) Clique na opcao '{acomodacao}' (evite opcoes com 'Parcial' a menos que solicitado). "
            f"3) Apos selecionar tudo, feche o modal clicando no X vermelho. "
            f"Sinalize done quando o modal fechar e os valores aparecerem na pagina.",
            max_steps=12,
        )

        if not result.get("sucesso", True):
            return _erro(cidade, result.get("erro", "Falha na configuracao de produtos"))

        # ---- FASE 5: Extracao de valores ----
        print(f"[*] Fase 5: Extraindo valores...")
        time.sleep(1)
        valores = agent.extract_price_values()

        if not valores:
            # Tenta mais uma vez rolando e extraindo
            print("[*] Tentando novamente...")
            agent._scroll({"direction": "down", "pixels": 800})
            time.sleep(2)
            valores = agent.extract_price_values()

        print(f"[OK] Cotacao concluida para {cidade}: {len(valores)} valores")
        return {
            "cidade": cidade,
            "sucesso": len(valores) > 0,
            "valores": valores,
            "erro": None if valores else "Nenhum valor encontrado",
        }

    except Exception as e:
        print(f"[ERRO] Excecao na cotacao de {cidade}: {e}")
        return _erro(cidade, str(e))


def cotar_proxima_cidade_ai(agent, cidade, config):
    """
    Cota proxima cidade voltando 2 telas (reusa sessao).
    """
    driver = agent.driver
    operadora = config.get("operadora", "Hapvida")
    tabela = config.get("tabela", "+ Odonto")
    plano = config.get("plano", "Ambulatorial")
    acomodacao = config.get("acomodacao", "Sem acomodacao / Com coparticipacao")
    tipo_empresa = config.get("tipo_empresa", "MEI - Empresario individual")
    vidas = config.get("vidas_por_faixa", "1")

    try:
        # ---- Voltar para tela de cidade ----
        print(f"[*] Voltando para selecao de cidade...")
        result = agent.execute_goal(
            "Clique no botao 'Voltar' duas vezes para voltar a tela de selecao de cidade. "
            "Feche quaisquer popups/modais antes. "
            "Sinalize done quando estiver na tela de selecao de cidade.",
            max_steps=6,
        )

        # ---- Cidade ----
        print(f"[*] Selecionando cidade: {cidade}...")
        result = agent.execute_goal(
            f"1) No campo de cidade, limpe e digite '{cidade}'. "
            f"2) Selecione '{cidade}' no dropdown. "
            f"3) Clique em 'Avancar'. "
            f"Sinalize done apos avancar.",
            max_steps=8,
        )

        if not result.get("sucesso", True):
            return _erro(cidade, "Falha na selecao de cidade")

        # ---- Faixas etarias (ja preenchidas, so avancar) ----
        print(f"[*] Avancando faixas etarias...")
        result = agent.execute_goal(
            "Os campos de faixa etaria ja devem estar preenchidos. "
            "Clique em 'Avancar'. "
            "Sinalize done apos avancar.",
            max_steps=4,
        )

        # ---- Produtos ----
        print(f"[*] Configurando produtos para {cidade}...")
        result = agent.execute_goal(
            f"1) Clique em 'Add Produtos'. "
            f"2) No modal: selecione '{operadora}', depois a tabela com '{tabela}', "
            f"   depois '{plano}', depois '{acomodacao}'. "
            f"3) Feche o modal (X vermelho). "
            f"Sinalize done quando os valores aparecerem.",
            max_steps=12,
        )

        # ---- Extracao ----
        print(f"[*] Extraindo valores...")
        time.sleep(1)
        valores = agent.extract_price_values()

        if not valores:
            agent._scroll({"direction": "down", "pixels": 800})
            time.sleep(2)
            valores = agent.extract_price_values()

        print(f"[OK] Cotacao concluida para {cidade}: {len(valores)} valores")
        return {
            "cidade": cidade,
            "sucesso": len(valores) > 0,
            "valores": valores,
            "erro": None if valores else "Nenhum valor encontrado",
        }

    except Exception as e:
        print(f"[ERRO] Excecao na cotacao de {cidade}: {e}")
        return _erro(cidade, str(e))


def _erro(cidade, msg):
    """Helper para retornar erro."""
    return {"cidade": cidade, "sucesso": False, "valores": [], "erro": msg}


# ============================================
# ROTAS FLASK
# ============================================

@app.route("/")
def index():
    """Pagina inicial."""
    has_key = bool(ANTHROPIC_API_KEY)
    return render_template("index_cotacao.html", has_api_key=has_key)


@app.route("/cotar", methods=["POST"])
def cotar():
    """Rota principal de cotacao - AI-driven."""
    global primeira_cotacao, driver_global, logado

    if not ANTHROPIC_API_KEY:
        return jsonify(
            [_erro("N/A", "ANTHROPIC_API_KEY nao configurada. Defina a variavel de ambiente.")]
        ), 500

    try:
        dados = request.get_json()
        cidades = dados.get("cidades", [])
        config = dados.get("config", {})

        if not cidades:
            return jsonify({"erro": "Nenhuma cidade informada"}), 400

        # Garante navegador e login
        if driver_global is None:
            iniciar_navegador()

        agent = AIBrowserAgent(driver_global, ANTHROPIC_API_KEY)

        if not logado:
            if not fazer_login_ai(agent):
                return jsonify([_erro("N/A", "Falha no login")]), 500

        resultados = []

        for i, cidade in enumerate(cidades):
            cidade = cidade.strip()
            if not cidade:
                continue

            print(f"\n{'='*50}")
            print(f"[*] Cotando {i+1}/{len(cidades)}: {cidade}")
            print(f"{'='*50}")

            try:
                if i == 0 or primeira_cotacao or driver_global is None:
                    resultado = cotar_cidade_ai(agent, cidade, config)
                    primeira_cotacao = False
                else:
                    resultado = cotar_proxima_cidade_ai(agent, cidade, config)
            except Exception as e:
                print(f"[ERRO] Excecao ao cotar {cidade}: {e}")
                resultado = _erro(cidade, str(e))
                primeira_cotacao = True

            resultados.append(resultado)

            if not resultado.get("sucesso"):
                primeira_cotacao = True

        return jsonify(resultados)

    except Exception as e:
        print(f"[ERRO] Excecao geral: {e}")
        return jsonify([_erro("N/A", f"Erro geral: {e}")]), 500


@app.route("/status")
def status():
    """Status do sistema."""
    return jsonify(
        {
            "navegador_ativo": driver_global is not None,
            "logado": logado,
            "ai_configurada": bool(ANTHROPIC_API_KEY),
        }
    )


@app.route("/login", methods=["POST"])
def login():
    """Faz login."""
    global driver_global

    if not ANTHROPIC_API_KEY:
        return jsonify({"sucesso": False, "erro": "ANTHROPIC_API_KEY nao configurada"})

    if driver_global is None:
        iniciar_navegador()

    agent = AIBrowserAgent(driver_global, ANTHROPIC_API_KEY)
    sucesso = fazer_login_ai(agent)
    return jsonify({"sucesso": sucesso})


@app.route("/fechar")
def fechar():
    """Fecha navegador."""
    global driver_global, logado, primeira_cotacao
    if driver_global:
        driver_global.quit()
        driver_global = None
        logado = False
        primeira_cotacao = True
    return jsonify({"mensagem": "Navegador fechado"})


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    print("\n" + "=" * 60)
    print("  COTACAO HAPVIDA - AI-DRIVEN")
    print("=" * 60)
    print(f"\n  Acesse: http://localhost:{port}")
    print(f"  AI: {'Configurada' if ANTHROPIC_API_KEY else 'FALTA ANTHROPIC_API_KEY!'}")
    print(f"  Modelo: {AI_MODEL}")
    print("\n  Endpoints:")
    print("    GET  /         - Pagina inicial")
    print("    POST /cotar    - Executar cotacao (AI)")
    print("    POST /login    - Fazer login")
    print("    GET  /status   - Status do sistema")
    print("    GET  /fechar   - Fechar navegador")
    print("\n" + "=" * 60 + "\n")

    app.run(debug=False, host="0.0.0.0", port=port, threaded=True)
