"""
Script de cotacao rapida Hapvida via Selenium.
Compara PME (empresarial) vs PF/Coletivos (individual) e retorna o mais barato.

Uso: python cotar_rapido.py "Aracaju"
     python cotar_rapido.py "Recife" "Teresina" "Aracaju"

Retorna JSON com a opcao mais barata por faixa etaria.
"""

import sys
import json
import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# ============================================
# CONFIGURACOES
# ============================================
EMAIL = "jessicamendesbarbosa5@gmail.com"
SENHA = "amovoced28"
URL_LOGIN = "https://app.cotadorsimplificado.com.br/login"

FAIXAS = [
    "0 a 18 anos", "19 a 23 anos", "24 a 28 anos",
    "29 a 33 anos", "34 a 38 anos", "39 a 43 anos",
    "44 a 48 anos", "49 a 53 anos", "54 a 58 anos",
    "59 anos ou mais"
]


# ============================================
# HELPERS
# ============================================
def clique_real(driver, el):
    """Clica via ActionChains na posicao central do elemento (Bubble.io ignora .click() sintetico)."""
    rect = driver.execute_script("""
        var r = arguments[0].getBoundingClientRect();
        return {x: Math.round(r.x + r.width/2), y: Math.round(r.y + r.height/2)};
    """, el)
    actions = ActionChains(driver)
    actions.move_by_offset(rect['x'], rect['y']).click().perform()
    actions.reset_actions()


def clique_coords(driver, x, y):
    """Clica via ActionChains em coordenadas absolutas."""
    actions = ActionChains(driver)
    actions.move_by_offset(x, y).click().perform()
    actions.reset_actions()


def iniciar_navegador():
    """Inicia o Chrome em modo headless."""
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-extensions")

    chromedriver_paths = [
        os.environ.get("CHROMEDRIVER_PATH", ""),
        "/usr/bin/chromedriver",
        "/usr/local/bin/chromedriver",
    ]
    for path in chromedriver_paths:
        if path and os.path.exists(path):
            try:
                service = Service(path)
                return webdriver.Chrome(service=service, options=chrome_options)
            except:
                continue

    from webdriver_manager.chrome import ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)


def fazer_login(driver):
    """Faz login no site."""
    print("[*] Acessando login...", file=sys.stderr)
    driver.get(URL_LOGIN)
    wait = WebDriverWait(driver, 20)
    time.sleep(3)

    campo_email = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email'], input[placeholder='Seu email']"))
    )
    campo_email.clear()
    campo_email.send_keys(EMAIL)
    time.sleep(0.5)

    botao_continuar = driver.find_element(By.XPATH, "//button[contains(., 'Continuar com Email')]")
    botao_continuar.click()
    time.sleep(3)

    campo_senha = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
    )
    campo_senha.clear()
    campo_senha.send_keys(SENHA)
    time.sleep(0.5)

    botao_entrar = driver.find_element(By.XPATH, "//button[contains(., 'Entrar')]")
    botao_entrar.click()
    time.sleep(4)

    if "login" not in driver.current_url.lower():
        print("[OK] Login realizado", file=sys.stderr)
        return True
    else:
        print("[ERRO] Falha no login", file=sys.stderr)
        return False


def fechar_popups(driver):
    """Fecha popups que bloqueiam a tela."""
    seletores = [
        "button[class*='close']", "button[class*='dismiss']",
        "[aria-label='Close']", "[aria-label='Fechar']",
    ]
    for sel in seletores:
        try:
            for elem in driver.find_elements(By.CSS_SELECTOR, sel):
                if elem.is_displayed():
                    driver.execute_script("arguments[0].click();", elem)
                    time.sleep(0.3)
        except:
            pass
    try:
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
    except:
        pass


def clicar_avancar(driver):
    """Clica no botao Avancar visivel."""
    fechar_popups(driver)
    botoes = driver.find_elements(By.XPATH, "//button[contains(., 'Avançar')]")
    for botao in botoes:
        try:
            if botao.is_displayed() and botao.is_enabled():
                driver.execute_script("arguments[0].click();", botao)
                return True
        except:
            continue
    return False


def extrair_valores(driver):
    """Extrai valores da tabela de cotacao via posicionamento DOM."""
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 300);")
    time.sleep(1)

    resultado = []
    try:
        items = driver.execute_script("""
            var all = document.querySelectorAll('*');
            var faixas = [];
            var valores_de = [];

            for (var el of all) {
                var t = (el.innerText || '').trim();
                if (!t || t.length > 20) continue;
                var rect = el.getBoundingClientRect();
                if (rect.width === 0 || rect.height === 0) continue;
                if (rect.y < 0 || rect.y > 2000) continue;

                if (/^\\d+ a \\d+ anos$|^59 anos ou mais$|^59 ou \\+$/.test(t)) {
                    faixas.push({text: t, y: Math.round(rect.y), x: Math.round(rect.x), w: Math.round(rect.width)});
                }
                if (/^\\d{2,3},\\d{2}$/.test(t)) {
                    valores_de.push({text: t, y: Math.round(rect.y), x: Math.round(rect.x)});
                }
            }

            var faixas_by_y = {};
            for (var f of faixas) {
                if (!faixas_by_y[f.y] || f.w < faixas_by_y[f.y].w) {
                    faixas_by_y[f.y] = f;
                }
            }

            var valores_by_y = {};
            for (var v of valores_de) {
                if (!valores_by_y[v.y] || v.x < valores_by_y[v.y].x) {
                    valores_by_y[v.y] = v;
                }
            }

            var resultado = [];
            var faixas_keys = Object.keys(faixas_by_y).map(Number).sort((a,b) => a-b);
            for (var fy of faixas_keys) {
                var faixa = faixas_by_y[fy];
                var melhor_v = null;
                var melhor_dist = 999;
                for (var vy in valores_by_y) {
                    var dist = Math.abs(fy - parseInt(vy));
                    if (dist <= 8 && dist < melhor_dist) {
                        melhor_dist = dist;
                        melhor_v = valores_by_y[vy];
                    }
                }
                if (melhor_v) {
                    resultado.push({faixa: faixa.text, valor: melhor_v.text});
                }
            }
            return resultado;
        """)

        if items and len(items) > 0:
            faixa_nomes = {
                "59 anos ou...": "59 anos ou mais",
                "59 anos ou mais": "59 anos ou mais",
                "59 ou +": "59 anos ou mais",
            }
            vistos = set()
            for item in items:
                nome = faixa_nomes.get(item["faixa"], item["faixa"])
                if nome not in vistos:
                    vistos.add(nome)
                    resultado.append({
                        "faixa_etaria": nome,
                        "valor": f"R$ {item['valor']}"
                    })
    except Exception as e:
        print(f"[AVISO] Extracao DOM falhou: {e}", file=sys.stderr)

    return resultado


# ============================================
# SELECAO DE PRODUTOS NO MODAL (compartilhado)
# ============================================
def selecionar_produtos_modal(driver, wait, tipo="pme"):
    """Seleciona produtos no modal do Bubble.io. Funciona para PME e PF."""
    # Add Produtos
    try:
        botao_add = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add Produtos')]")))
        botao_add.click()
        time.sleep(2)
    except:
        pass

    print("[*] Selecionando produtos no modal...", file=sys.stderr)
    time.sleep(1)
    driver.save_screenshot("debug_modal_aberto.png")

    # Debug: listar todos textos visiveis no modal
    textos_modal = driver.execute_script("""
        var all = document.querySelectorAll('*');
        var textos = [];
        for (var el of all) {
            var t = (el.innerText || '').trim();
            var rect = el.getBoundingClientRect();
            if (t.length > 2 && t.length < 100 && rect.width > 30 && rect.height > 10
                && rect.y > 50 && rect.y < 600 && rect.x < 500 && el.offsetParent) {
                var key = t.substring(0, 60);
                if (textos.indexOf(key) === -1) textos.push(key);
            }
        }
        return textos.slice(0, 30);
    """)
    print(f"[DEBUG] Textos no modal: {textos_modal}", file=sys.stderr)

    # Etapa 1: Escolher Operadora - primeira opcao visivel
    operadora_info = driver.execute_script("""
        var header = null;
        var all = document.querySelectorAll('*');
        // Acha o header "Escolher Operadora:" pra saber onde começa a lista
        for (var el of all) {
            var t = (el.innerText || '').trim();
            if (t === 'Escolher Operadora:' || t === 'Escolher Operadora') {
                header = el.getBoundingClientRect();
                break;
            }
        }
        // Procura o primeiro item clicavel abaixo do header (ou no modal)
        var minY = header ? header.y + header.height : 80;
        var items = [];
        for (var el of all) {
            var t = (el.innerText || '').trim();
            var rect = el.getBoundingClientRect();
            if (t.length > 2 && t.length < 60
                && rect.width > 50 && rect.width < 400
                && rect.height > 15 && rect.height < 60
                && rect.y > minY && rect.y < minY + 300
                && rect.x < 400 && el.offsetParent
                && !t.includes('Escolher') && !t.includes('Add')
                && !t.includes('Fechar') && !t.includes('Cancelar')) {
                items.push({x: Math.round(rect.x + rect.width/2), y: Math.round(rect.y + rect.height/2), text: t});
            }
        }
        items.sort(function(a,b) { return a.y - b.y; });
        return items.length > 0 ? items[0] : null;
    """)
    if operadora_info:
        clique_coords(driver, operadora_info['x'], operadora_info['y'])
        print(f"[*] Operadora: {operadora_info['text']}", file=sys.stderr)
    else:
        print("[AVISO] Nenhuma operadora encontrada no modal!", file=sys.stderr)
    driver.save_screenshot("debug_apos_operadora.png")
    time.sleep(3)

    # Etapa 2: Escolher Tabela - primeira opcao visivel
    tabela_info = driver.execute_script("""
        var header = null;
        var all = document.querySelectorAll('*');
        for (var el of all) {
            var t = (el.innerText || '').trim();
            if (t === 'Escolher Tabela:' || t === 'Escolher Tabela'
                || t === 'Qual Tabela?' || t === 'Qual Tabela') {
                header = el.getBoundingClientRect();
                break;
            }
        }
        var minY = header ? header.y + header.height : 80;
        var items = [];
        for (var el of all) {
            var t = (el.innerText || '').trim();
            var rect = el.getBoundingClientRect();
            if (t.length > 3 && t.length < 100
                && rect.width > 60 && rect.width < 500
                && rect.height > 15 && rect.height < 80
                && rect.y > minY && rect.y < minY + 400
                && rect.x < 450 && el.offsetParent
                && !t.includes('Escolher') && !t.includes('Operadora')
                && !t.includes('Add') && !t.includes('Fechar')
                && !t.includes('Qual')) {
                items.push({x: Math.round(rect.x + rect.width/2), y: Math.round(rect.y + rect.height/2), text: t});
            }
        }
        items.sort(function(a,b) { return a.y - b.y; });
        return items.length > 0 ? items[0] : null;
    """)
    if tabela_info:
        clique_coords(driver, tabela_info['x'], tabela_info['y'])
        print(f"[*] Tabela: {tabela_info['text'].strip()[:50]}", file=sys.stderr)
    else:
        print("[AVISO] Nenhuma tabela encontrada!", file=sys.stderr)
    driver.save_screenshot("debug_apos_tabela.png")
    time.sleep(3)

    # Etapa 3: Escolher Plano - primeiro disponivel (Ambulatorial, Nosso Plano, etc.)
    driver.save_screenshot("debug_antes_plano.png")
    plano_ok = False
    for tentativa in range(5):
        plano_info = driver.execute_script("""
            var header = null;
            var all = document.querySelectorAll('*');
            // Header pode ser "Escolher Plano(s):" (layout antigo) ou "Qual Plano?" (layout novo)
            for (var el of all) {
                var t = (el.innerText || '').trim();
                if (t.match(/^(Escolher Plano[s]?|Qual Plano)[?:]?$/)) {
                    header = el.getBoundingClientRect();
                    break;
                }
            }
            var minY = header ? header.y + header.height : 100;
            var items = [];
            // Nomes conhecidos de planos
            var nomes_plano = ['Ambulatorial', 'Nosso Plano', 'Nosso Médico', 'Pleno',
                               'Nosso Plano A+H', 'Nosso Plano A+H+O'];
            for (var el of all) {
                var t = (el.innerText || '').trim();
                var rect = el.getBoundingClientRect();
                if (rect.width > 40 && rect.height > 10 && rect.height < 50
                    && rect.y >= minY && rect.y < minY + 300
                    && rect.x < 350 && el.offsetParent) {
                    for (var np of nomes_plano) {
                        if (t === np) {
                            items.push({x: Math.round(rect.x + rect.width/2), y: Math.round(rect.y + rect.height/2), text: t});
                            break;
                        }
                    }
                }
            }
            items.sort(function(a,b) { return a.y - b.y; });
            return items.length > 0 ? items[0] : null;
        """)
        if plano_info:
            clique_coords(driver, plano_info['x'], plano_info['y'])
            print(f"[*] Plano: {plano_info['text']}", file=sys.stderr)
            plano_ok = True
            break
        time.sleep(1)
    if not plano_ok:
        print("[AVISO] Nenhum plano encontrado!", file=sys.stderr)
    driver.save_screenshot("debug_apos_plano.png")
    time.sleep(3)

    # Etapa 4: Escolher modalidade - primeira opcao (mais barata)
    for tentativa in range(5):
        modal_info = driver.execute_script("""
            var all = document.querySelectorAll('*');
            var found = [];
            for (var el of all) {
                var t = (el.innerText || '').trim();
                var rect = el.getBoundingClientRect();
                if (t.includes('Total:') && t.includes('por:')
                    && rect.height > 30 && rect.width > 80
                    && el.offsetParent && rect.x < 400 && rect.y > 100) {
                    found.push({x: Math.round(rect.x + rect.width/2), y: Math.round(rect.y + rect.height/2)});
                }
            }
            found.sort(function(a,b) { return a.y - b.y; });
            return found.length > 0 ? found[0] : null;
        """)
        if modal_info:
            clique_coords(driver, modal_info['x'], modal_info['y'])
            print("[*] Modalidade selecionada (primeira opcao)", file=sys.stderr)
            break
        time.sleep(1)
    time.sleep(3)

    # Fechar modal
    print("[*] Fechando modal...", file=sys.stderr)
    try:
        clique_coords(driver, 283, 22)
        time.sleep(1)
    except:
        pass
    try:
        clique_coords(driver, 800, 400)
    except:
        pass
    time.sleep(2)

    # Ver mais Detalhes da Cotacao
    print("[*] Abrindo detalhes da cotacao...", file=sys.stderr)
    try:
        btn_detalhes = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[contains(text(), 'Ver mais Detalhes')]")
        ))
        driver.execute_script("arguments[0].click();", btn_detalhes)
        time.sleep(4)
    except Exception as e:
        print(f"[AVISO] Nao achou botao detalhes: {e}", file=sys.stderr)

    return extrair_valores(driver)


# ============================================
# COTACAO PME (EMPRESARIAL)
# ============================================
def cotar_cidade_pme(driver, cidade):
    """Cotacao PME ate 29 vidas (empresarial com MEI)."""
    wait = WebDriverWait(driver, 15)

    driver.get("https://app.cotadorsimplificado.com.br/")
    time.sleep(2)
    fechar_popups(driver)
    time.sleep(1)

    print(f"[*] Cotando {cidade} (PME)...", file=sys.stderr)
    botao = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Cotar Hapvida')]")))
    driver.execute_script("arguments[0].click();", botao)
    time.sleep(2)

    # PME ate 29 vidas - layout novo usa card div clicavel (Bubble ignora .click() sintetico)
    opcao = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[normalize-space(text())='PME até 29 vidas']")))
    clique_real(driver, opcao)
    time.sleep(2)

    # Nome do cliente
    campo_nome = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder*='cliente']")))
    campo_nome.clear()
    campo_nome.send_keys("teste")
    time.sleep(1)

    # Fecha dropdown de clientes
    try:
        fechar_btn = driver.find_elements(By.CSS_SELECTOR, "svg[class*='close'], button[class*='close']")
        for btn in fechar_btn:
            if btn.is_displayed():
                driver.execute_script("arguments[0].click();", btn)
                break
    except:
        pass
    time.sleep(0.5)

    clicar_avancar(driver)
    time.sleep(2)

    # Selecionar cidade
    campo_cidade = None
    inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='input'], input[type='text'], input:not([type])")
    for inp in inputs:
        try:
            if inp.is_displayed() and inp.is_enabled():
                placeholder = inp.get_attribute("placeholder") or ""
                if " - " in placeholder or "cidade" in placeholder.lower():
                    campo_cidade = inp
                    break
        except:
            continue

    if not campo_cidade:
        raise Exception("Campo de cidade nao encontrado")

    driver.execute_script("arguments[0].click();", campo_cidade)
    time.sleep(0.3)
    driver.execute_script("arguments[0].select();", campo_cidade)
    time.sleep(0.2)
    campo_cidade.send_keys(cidade)
    time.sleep(2)

    try:
        opcao_cidade = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(), '{cidade} -') or contains(text(), '{cidade}/')]"))
        )
        opcao_cidade.click()
    except:
        opcao_cidade = driver.find_element(By.XPATH, f"//*[contains(text(), '{cidade}') and contains(text(), '-')]")
        driver.execute_script("arguments[0].click();", opcao_cidade)
    time.sleep(1)

    # MEI
    mei_selecionado = False
    try:
        selects = driver.find_elements(By.CSS_SELECTOR, "select")
        for sel in selects:
            if sel.is_displayed():
                select = Select(sel)
                for option in select.options:
                    if "MEI" in option.text:
                        select.select_by_visible_text(option.text)
                        mei_selecionado = True
                        break
            if mei_selecionado:
                break
    except:
        pass
    if not mei_selecionado:
        try:
            driver.execute_script("""
                var selects = document.querySelectorAll('select');
                for (var s of selects) {
                    for (var o of s.options) {
                        if (o.text.includes('MEI')) {
                            s.value = o.value;
                            s.dispatchEvent(new Event('change', {bubbles: true}));
                            return true;
                        }
                    }
                }
                return false;
            """)
        except:
            pass
    time.sleep(1)

    clicar_avancar(driver)
    time.sleep(2)

    # Faixas etarias: 1 em cada
    campos_faixa = driver.find_elements(By.CSS_SELECTOR, "input[placeholder='0']")
    for campo in campos_faixa[:10]:
        try:
            campo.clear()
            campo.send_keys("1")
        except:
            pass
    time.sleep(1)

    clicar_avancar(driver)
    time.sleep(2)

    return selecionar_produtos_modal(driver, wait, tipo="pme")


# ============================================
# COTACAO PF / COLETIVOS (INDIVIDUAL)
# ============================================
def cotar_cidade_pf(driver, cidade):
    """Cotacao PF/Coletivos (individual - sem tipo empresa)."""
    wait = WebDriverWait(driver, 15)

    driver.get("https://app.cotadorsimplificado.com.br/")
    time.sleep(2)
    fechar_popups(driver)
    time.sleep(1)

    print(f"[*] Cotando {cidade} (PF/Coletivos)...", file=sys.stderr)
    botao = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Cotar Hapvida')]")))
    driver.execute_script("arguments[0].click();", botao)
    time.sleep(2)

    # PF / Coletivos - layout novo usa card div clicavel (Bubble ignora .click() sintetico)
    opcao = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[normalize-space(text())='PF / Coletivos']")))
    clique_real(driver, opcao)
    time.sleep(2)

    # Nome do cliente
    campo_nome = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder*='cliente']")))
    campo_nome.clear()
    campo_nome.send_keys("teste")
    time.sleep(1)

    # Fecha dropdown de clientes
    try:
        fechar_btn = driver.find_elements(By.CSS_SELECTOR, "svg[class*='close'], button[class*='close']")
        for btn in fechar_btn:
            if btn.is_displayed():
                driver.execute_script("arguments[0].click();", btn)
                break
    except:
        pass
    time.sleep(0.5)

    clicar_avancar(driver)
    time.sleep(2)

    # Selecionar cidade (sem tipo empresa - vai direto)
    campo_cidade = None
    inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='input'], input[type='text'], input:not([type])")
    for inp in inputs:
        try:
            if inp.is_displayed() and inp.is_enabled():
                placeholder = inp.get_attribute("placeholder") or ""
                if " - " in placeholder or "cidade" in placeholder.lower():
                    campo_cidade = inp
                    break
        except:
            continue

    if not campo_cidade:
        raise Exception("Campo de cidade nao encontrado")

    driver.execute_script("arguments[0].click();", campo_cidade)
    time.sleep(0.3)
    driver.execute_script("arguments[0].select();", campo_cidade)
    time.sleep(0.2)
    campo_cidade.send_keys(cidade)
    time.sleep(2)

    try:
        opcao_cidade = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(), '{cidade} -') or contains(text(), '{cidade}/')]"))
        )
        opcao_cidade.click()
    except:
        opcao_cidade = driver.find_element(By.XPATH, f"//*[contains(text(), '{cidade}') and contains(text(), '-')]")
        driver.execute_script("arguments[0].click();", opcao_cidade)
    time.sleep(1)

    # PF nao tem tipo empresa - clica direto em Avancar
    clicar_avancar(driver)
    time.sleep(2)

    # Faixas etarias: 1 em cada
    campos_faixa = driver.find_elements(By.CSS_SELECTOR, "input[placeholder='0']")
    for campo in campos_faixa[:10]:
        try:
            campo.clear()
            campo.send_keys("1")
        except:
            pass
    time.sleep(1)

    clicar_avancar(driver)
    time.sleep(2)

    return selecionar_produtos_modal(driver, wait, tipo="pf")


# ============================================
# COMPARACAO PME vs PF
# ============================================
def valor_para_float(valor_str):
    """Converte 'R$ 123,45' para 123.45"""
    return float(valor_str.replace("R$ ", "").replace(".", "").replace(",", "."))


def comparar_e_melhor(pme_valores, pf_valores):
    """Compara PME vs PF e retorna lista simples com o valor mais barato por faixa."""
    pme_dict = {v["faixa_etaria"]: v["valor"] for v in pme_valores}
    pf_dict = {v["faixa_etaria"]: v["valor"] for v in pf_valores}

    resultado = []
    total_pme = 0
    total_pf = 0

    for faixa in FAIXAS:
        val_pme = pme_dict.get(faixa)
        val_pf = pf_dict.get(faixa)

        if val_pme and val_pf:
            num_pme = valor_para_float(val_pme)
            num_pf = valor_para_float(val_pf)
            total_pme += num_pme
            total_pf += num_pf
            melhor_valor = val_pf if num_pf < num_pme else val_pme
            resultado.append({"faixa_etaria": faixa, "valor": melhor_valor})
        elif val_pme:
            resultado.append({"faixa_etaria": faixa, "valor": val_pme})
        elif val_pf:
            resultado.append({"faixa_etaria": faixa, "valor": val_pf})

    melhor_tipo = "PF/Coletivos" if total_pf < total_pme else "PME"
    print(f"\n[RESULTADO] Melhor opcao global: {melhor_tipo}", file=sys.stderr)
    print(f"  PME total: R$ {total_pme:,.2f} | PF total: R$ {total_pf:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."), file=sys.stderr)

    return resultado


# ============================================
# MAIN
# ============================================
def main():
    if len(sys.argv) < 2:
        print('Uso: python cotar_rapido.py "Aracaju" ["Recife" ...]', file=sys.stderr)
        sys.exit(1)

    cidades = sys.argv[1:]
    driver = None

    try:
        driver = iniciar_navegador()
        if not fazer_login(driver):
            print(json.dumps({"erro": "Falha no login"}))
            sys.exit(1)

        todos_resultados = {}
        for cidade in cidades:
            print(f"\n{'='*50}", file=sys.stderr)
            print(f"  COTANDO: {cidade}", file=sys.stderr)
            print(f"{'='*50}", file=sys.stderr)

            try:
                # Cota PME
                pme = cotar_cidade_pme(driver, cidade)
                print(f"[OK] {cidade} PME: {len(pme)} faixas", file=sys.stderr)

                # Cota PF
                pf = cotar_cidade_pf(driver, cidade)
                print(f"[OK] {cidade} PF: {len(pf)} faixas", file=sys.stderr)

                # Compara e pega o melhor (retorna lista simples)
                if pme and pf:
                    todos_resultados[cidade] = comparar_e_melhor(pme, pf)
                elif pme:
                    todos_resultados[cidade] = pme
                elif pf:
                    todos_resultados[cidade] = pf
                else:
                    todos_resultados[cidade] = []

            except Exception as e:
                print(f"[ERRO] {cidade}: {str(e)}", file=sys.stderr)
                todos_resultados[cidade] = []

        # Output JSON - sempre formato [{faixa_etaria, valor}]
        if len(cidades) == 1:
            print(json.dumps(todos_resultados[cidades[0]], indent=2, ensure_ascii=False))
        else:
            print(json.dumps(todos_resultados, indent=2, ensure_ascii=False))

    finally:
        if driver:
            driver.quit()


if __name__ == "__main__":
    main()
