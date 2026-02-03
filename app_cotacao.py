"""
=============================================================================
APLICACAO WEB - COTACAO HAPVIDA
=============================================================================
Aplicacao Flask para cotar planos Hapvida em multiplas cidades.

Acesse: http://localhost:5000

Autor: Claude AI
Data: 03/02/2025
=============================================================================
"""

from flask import Flask, render_template, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import threading

app = Flask(__name__)

# ============================================
# CONFIGURACOES
# ============================================
EMAIL = "jessicamendesbarbosa5@gmail.com"
SENHA = "amovoced28"
URL_LOGIN = "https://app.cotadorsimplificado.com.br/login"

# Variavel global para armazenar o driver (sessao do navegador)
driver_global = None
logado = False
primeira_cotacao = True  # Controla se e a primeira cotacao da sessao

# ============================================
# FUNCOES DE AUTOMACAO
# ============================================

def fechar_popups(driver):
    """Fecha qualquer popup/aviso que esteja bloqueando a tela."""
    popups_fechados = 0

    # Lista de seletores comuns para botoes de fechar popups
    seletores_fechar = [
        # Botoes de fechar com X
        "button[class*='close']",
        "button[class*='dismiss']",
        "button[class*='fechar']",
        "[class*='close-button']",
        "[class*='modal-close']",
        "[aria-label='Close']",
        "[aria-label='Fechar']",
        # SVGs de fechar (X)
        "svg[class*='close']",
        # Botoes com texto
        "//button[contains(text(), 'Fechar')]",
        "//button[contains(text(), 'OK')]",
        "//button[contains(text(), 'Entendi')]",
        "//button[contains(text(), 'Continuar')]",
        "//button[contains(text(), 'Pular')]",
        "//span[contains(text(), 'X')]",
        # Overlays/backdrops clicaveis
        "[class*='overlay']",
        "[class*='backdrop']",
        # Icones de fechar
        "i[class*='close']",
        "i[class*='times']",
    ]

    for seletor in seletores_fechar:
        try:
            if seletor.startswith("//"):
                # XPATH
                elementos = driver.find_elements(By.XPATH, seletor)
            else:
                # CSS
                elementos = driver.find_elements(By.CSS_SELECTOR, seletor)

            for elem in elementos:
                try:
                    if elem.is_displayed() and elem.is_enabled():
                        # Verifica se o elemento esta na frente (visivel)
                        driver.execute_script("arguments[0].click();", elem)
                        popups_fechados += 1
                        print(f"[*] Popup fechado: {seletor}")
                        time.sleep(0.5)
                except:
                    pass
        except:
            pass

    # Tenta pressionar ESC para fechar modais
    try:
        from selenium.webdriver.common.keys import Keys
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
        time.sleep(0.3)
    except:
        pass

    return popups_fechados


def clicar_elemento_seguro(driver, elemento, tentativas=3):
    """Tenta clicar em um elemento, fechando popups se necessario."""
    for tentativa in range(tentativas):
        try:
            # Primeiro tenta clicar normalmente
            elemento.click()
            return True
        except Exception as e:
            if "element click intercepted" in str(e).lower() or "not clickable" in str(e).lower():
                print(f"[*] Clique bloqueado, tentando fechar popups... (tentativa {tentativa + 1})")
                fechar_popups(driver)
                time.sleep(0.5)
                try:
                    # Tenta com JavaScript
                    driver.execute_script("arguments[0].click();", elemento)
                    return True
                except:
                    pass
            else:
                # Outro tipo de erro
                if tentativa == tentativas - 1:
                    raise e
    return False


def iniciar_navegador():
    """Inicia o navegador Chrome."""
    global driver_global

    print("[*] Iniciando navegador...")

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--headless")  # Roda sem janela (necessario para VPS)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver_global = webdriver.Chrome(service=service, options=chrome_options)

    return driver_global


def fazer_login():
    """Faz login no site."""
    global driver_global, logado

    if driver_global is None:
        iniciar_navegador()

    driver = driver_global

    print(f"[*] Acessando: {URL_LOGIN}")
    driver.get(URL_LOGIN)

    wait = WebDriverWait(driver, 20)

    try:
        print("[*] Aguardando pagina carregar...")
        time.sleep(3)

        print("[*] Preenchendo email...")
        campo_email = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email'], input[placeholder='Seu email']"))
        )
        campo_email.clear()
        campo_email.send_keys(EMAIL)
        time.sleep(0.5)

        print("[*] Clicando em 'Continuar com Email'...")
        botao_continuar = driver.find_element(By.XPATH, "//button[contains(., 'Continuar com Email')]")
        botao_continuar.click()

        print("[*] Aguardando campo de senha...")
        time.sleep(2)

        campo_senha = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
        )

        print("[*] Preenchendo senha...")
        campo_senha.clear()
        campo_senha.send_keys(SENHA)
        time.sleep(0.5)

        print("[*] Clicando em 'Entrar'...")
        botao_entrar = driver.find_element(By.XPATH, "//button[contains(., 'Entrar')]")
        botao_entrar.click()

        print("[*] Aguardando login...")
        time.sleep(4)

        if "login" not in driver.current_url.lower():
            print("[OK] Login realizado com sucesso!")
            logado = True

            # Fecha popups que aparecem apos o login
            print("[*] Verificando popups pos-login...")
            time.sleep(2)
            fechar_popups(driver)
            time.sleep(1)

            return True
        else:
            print("[ERRO] Falha no login.")
            return False

    except Exception as e:
        print(f"[ERRO] Erro durante o login: {str(e)}")
        return False


def cotar_cidade(cidade):
    """Executa a cotacao para uma cidade especifica."""
    global driver_global, logado

    if not logado or driver_global is None:
        if not fazer_login():
            return {"erro": "Falha no login"}

    driver = driver_global
    wait = WebDriverWait(driver, 15)

    try:
        # Vai para pagina inicial
        driver.get("https://app.cotadorsimplificado.com.br/")
        time.sleep(2)

        # Fecha qualquer popup que apareca
        print("[*] Verificando popups...")
        fechar_popups(driver)
        time.sleep(1)

        # ETAPA 2: Cotar Hapvida
        print(f"[*] Iniciando cotacao para {cidade}...")
        fechar_popups(driver)  # Fecha popups antes de clicar
        botao_hapvida = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Cotar Hapvida')]"))
        )
        clicar_elemento_seguro(driver, botao_hapvida)
        time.sleep(2)

        # ETAPA 3: PME ate 29 vidas
        print("[*] Selecionando PME ate 29 vidas...")
        fechar_popups(driver)  # Fecha popups antes de clicar
        opcao_pme = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'PME até 29 vidas')]"))
        )
        clicar_elemento_seguro(driver, opcao_pme)
        time.sleep(2)

        # ETAPA 4: Nome do cliente
        print("[*] Preenchendo nome do cliente...")
        campo_nome = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder*='cliente']"))
        )
        campo_nome.clear()
        campo_nome.send_keys("teste")
        time.sleep(1)

        # Fecha dropdown se aparecer
        try:
            driver.find_element(By.CSS_SELECTOR, "svg[class*='close'], button[class*='close']").click()
        except:
            pass

        # ETAPA 5: Avancar
        print("[*] Avancando...")
        clicar_avancar(driver)
        time.sleep(2)

        # ETAPA 6: Selecionar cidade
        print(f"[*] Selecionando cidade: {cidade}...")

        # Aguarda um pouco mais para a pagina carregar
        time.sleep(1)

        # O campo de cidade tem um placeholder que pode conter o nome da cidade anterior
        # Ex: "Fortaleza - CE", "Recife - PE", etc.
        # Procuramos por input que esta proximo ao texto "DIGITE o nome da CIDADE"
        campo_cidade = None

        # Metodo 1: Busca pelo texto indicativo proximo
        try:
            # Procura todos os inputs de texto
            inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='input'], input[type='text'], input:not([type])")
            for inp in inputs:
                try:
                    if inp.is_displayed() and inp.is_enabled():
                        placeholder = inp.get_attribute("placeholder") or ""
                        # O placeholder contem " - " que indica cidade/estado
                        if " - " in placeholder or "cidade" in placeholder.lower():
                            campo_cidade = inp
                            print(f"[*] Campo cidade encontrado com placeholder: {placeholder}")
                            break
                except:
                    continue
        except:
            pass

        # Metodo 2: Procura pelo XPATH relativo ao label
        if not campo_cidade:
            try:
                campo_cidade = driver.find_element(By.XPATH, "//div[contains(text(), 'CIDADE')]/ancestor::div[1]//input")
            except:
                pass

        if campo_cidade:
            # Usa JavaScript para selecionar todo o texto e substituir
            driver.execute_script("arguments[0].scrollIntoView(true);", campo_cidade)
            time.sleep(0.5)
            driver.execute_script("arguments[0].click();", campo_cidade)
            time.sleep(0.3)
            # Seleciona todo o texto existente
            driver.execute_script("arguments[0].select();", campo_cidade)
            time.sleep(0.2)
            # Digita a nova cidade (substitui o texto selecionado)
            campo_cidade.send_keys(cidade)
        else:
            raise Exception("Campo de cidade nao encontrado")

        time.sleep(2)

        # Clica na opcao do dropdown
        try:
            opcao_cidade = wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(), '{cidade} -') or contains(text(), '{cidade}/')]"))
            )
            opcao_cidade.click()
        except:
            try:
                opcao_cidade = driver.find_element(By.XPATH, f"//*[contains(text(), '{cidade}') and contains(text(), '-')]")
                opcao_cidade.click()
            except:
                opcao_cidade = driver.find_element(By.XPATH, f"//*[contains(text(), '{cidade}')]")
                driver.execute_script("arguments[0].click();", opcao_cidade)
        time.sleep(1)

        # ETAPA 7: Tipo de empresa
        print("[*] Selecionando tipo de empresa...")
        try:
            dropdown = driver.find_element(By.CSS_SELECTOR, "select")
            select = Select(dropdown)
            select.select_by_visible_text("MEI - Empresário individual")
        except:
            dropdown = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Escolha Tipo de Empresa')]"))
            )
            dropdown.click()
            time.sleep(1)
            opcao = driver.find_element(By.XPATH, "//*[contains(text(), 'MEI - Empresário individual')]")
            opcao.click()
        time.sleep(1)

        # ETAPA 8: Avancar
        clicar_avancar(driver)
        time.sleep(2)

        # ETAPA 9: Faixas etarias
        print("[*] Preenchendo faixas etarias...")
        campos_faixa = driver.find_elements(By.CSS_SELECTOR, "input[placeholder='0']")
        for campo in campos_faixa[:10]:
            try:
                campo.clear()
                campo.send_keys("1")
            except:
                pass
        time.sleep(1)

        # ETAPA 10: Avancar
        clicar_avancar(driver)
        time.sleep(2)

        # ETAPA 11: Add Produtos
        print("[*] Adicionando produtos...")
        try:
            botao_add = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add Produtos')]"))
            )
            botao_add.click()
            time.sleep(2)
        except:
            pass

        # ETAPA 12: Sequencia dentro do MODAL
        # O modal tem 4 etapas sequenciais:
        # 1. Escolher Operadora: Hapvida, Hapvida - Affix, Hapvida - CORPe
        # 2. Escolher Tabela: Hapvida [Cidade] + Odonto, Hapvida [Cidade] SEM Odonto
        # 3. Escolher Planos: Ambulatorial, Nosso Plano, Nosso Medico
        # 4. Escolha: Sem acomodacao / Com coparticipacao, Sem acomodacao / Com Coparticipacao Parcial
        print("[*] Configurando opcoes no modal...")

        # 12.1 - Clicar em "Hapvida" (operadora - primeira opcao no modal)
        print("[*] 12.1 - Clicando em Hapvida (operadora)...")
        try:
            # Aguarda o modal carregar e procura pelo texto "Hapvida" que NAO contem outros textos
            time.sleep(1)
            # Procura especificamente pelo texto "Hapvida" sem "Affix" ou "CORPe"
            operadoras = driver.find_elements(By.XPATH, "//*[text()='Hapvida']")
            for op in operadoras:
                try:
                    if op.is_displayed():
                        driver.execute_script("arguments[0].click();", op)
                        print("[*] Clicou em Hapvida (operadora)")
                        break
                except:
                    continue
            time.sleep(1.5)
        except Exception as e:
            print(f"[AVISO] Nao encontrou operadora Hapvida: {e}")

        # 12.2 - Clicar em "Hapvida [Cidade] + Odonto" (tabela com odonto)
        print(f"[*] 12.2 - Selecionando tabela + Odonto...")
        try:
            # Procura pelo texto que contem "+ Odonto" (com odonto incluso)
            tabelas = driver.find_elements(By.XPATH, "//*[contains(text(), '+ Odonto') and not(contains(text(), 'SEM'))]")
            for tab in tabelas:
                try:
                    if tab.is_displayed():
                        driver.execute_script("arguments[0].click();", tab)
                        print("[*] Clicou na tabela + Odonto")
                        break
                except:
                    continue
            time.sleep(1.5)
        except Exception as e:
            print(f"[AVISO] Nao encontrou tabela + Odonto: {e}")

        # 12.3 - Clicar em "Ambulatorial" (tipo de plano)
        print("[*] 12.3 - Selecionando Ambulatorial...")
        try:
            # Procura pelo texto "Ambulatorial"
            planos = driver.find_elements(By.XPATH, "//*[text()='Ambulatorial']")
            for plano in planos:
                try:
                    if plano.is_displayed():
                        driver.execute_script("arguments[0].click();", plano)
                        print("[*] Clicou em Ambulatorial")
                        break
                except:
                    continue
            time.sleep(1.5)
        except Exception as e:
            print(f"[AVISO] Nao encontrou Ambulatorial: {e}")

        # 12.4 - Clicar em "Sem acomodacao / Com coparticipacao" (opcao de coparticipacao)
        print("[*] 12.4 - Selecionando Sem acomodacao / Com coparticipacao...")
        try:
            # Procura pelo texto exato (sem "Parcial")
            opcoes = driver.find_elements(By.XPATH, "//*[contains(text(), 'Sem acomodação / Com coparticipação') and not(contains(text(), 'Parcial'))]")
            for opc in opcoes:
                try:
                    if opc.is_displayed():
                        driver.execute_script("arguments[0].click();", opc)
                        print("[*] Clicou em Sem acomodacao / Com coparticipacao")
                        break
                except:
                    continue
            time.sleep(1.5)
        except Exception as e:
            print(f"[AVISO] Nao encontrou opcao coparticipacao: {e}")

        time.sleep(2)

        # ETAPA 13: Fechar o modal clicando no X vermelho
        print("[*] Fechando modal...")
        try:
            # Procura o botao X vermelho do modal (geralmente tem classe close ou icone X)
            botoes_fechar = driver.find_elements(By.CSS_SELECTOR, "[class*='bubble-element'][class*='clickable-element']")
            for btn in botoes_fechar:
                try:
                    # Procura por elemento com background vermelho ou icone X
                    style = btn.get_attribute("style") or ""
                    classe = btn.get_attribute("class") or ""
                    if btn.is_displayed() and ("close" in classe.lower() or "x" in btn.text.lower()):
                        driver.execute_script("arguments[0].click();", btn)
                        print("[*] Modal fechado via botao X")
                        break
                except:
                    continue
        except:
            pass

        # Tenta fechar clicando fora do modal ou no X vermelho visivel
        try:
            # Busca pelo X vermelho especifico do site (svg ou icone)
            x_btn = driver.find_element(By.XPATH, "//div[contains(@style, 'background') and contains(@style, 'rgb(231, 76, 60)')]")
            driver.execute_script("arguments[0].click();", x_btn)
            print("[*] Modal fechado via X vermelho")
        except:
            pass

        time.sleep(1)

        # ETAPA 14: Extrair valores
        print("[*] Extraindo valores...")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        valores = extrair_valores(driver)

        print(f"[OK] Cotacao concluida para {cidade}")
        return {
            "cidade": cidade,
            "sucesso": True,
            "valores": valores
        }

    except Exception as e:
        print(f"[ERRO] Erro na cotacao de {cidade}: {str(e)}")
        return {
            "cidade": cidade,
            "sucesso": False,
            "erro": str(e)
        }


def clicar_avancar(driver):
    """Clica no botao Avancar visivel."""
    # Primeiro fecha popups
    fechar_popups(driver)

    botoes = driver.find_elements(By.XPATH, "//button[contains(., 'Avançar')]")
    for botao in botoes:
        try:
            if botao.is_displayed() and botao.is_enabled():
                if clicar_elemento_seguro(driver, botao):
                    return True
        except:
            continue
    return False


def voltar_para_cidade(driver):
    """Volta para a tela de selecao de cidade clicando em Voltar 2 vezes."""
    wait = WebDriverWait(driver, 10)

    # Fecha qualquer modal aberto primeiro
    fechar_popups(driver)
    time.sleep(1)

    # Clica em Voltar 2 vezes:
    # 1a volta: da tela de resultados para faixas etarias
    # 2a volta: da tela de faixas etarias para cidade
    for i in range(2):
        try:
            botao_voltar = driver.find_element(By.XPATH, "//button[contains(., 'Voltar')]")
            if botao_voltar.is_displayed():
                driver.execute_script("arguments[0].click();", botao_voltar)
                print(f"[*] Clicou em Voltar ({i+1}/2)")
                time.sleep(1.5)
        except:
            break

    time.sleep(1)
    print("[*] Voltou para tela de cidade")
    return True


def cotar_proxima_cidade(cidade):
    """Cota uma cidade quando ja esta na tela de selecao de cidade."""
    global driver_global

    driver = driver_global
    wait = WebDriverWait(driver, 15)

    try:
        # Fecha popups
        fechar_popups(driver)
        time.sleep(0.5)

        # Selecionar cidade
        print(f"[*] Selecionando cidade: {cidade}...")

        # Encontra o campo de cidade
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

        if campo_cidade:
            driver.execute_script("arguments[0].scrollIntoView(true);", campo_cidade)
            time.sleep(0.5)
            driver.execute_script("arguments[0].click();", campo_cidade)
            time.sleep(0.3)
            driver.execute_script("arguments[0].select();", campo_cidade)
            time.sleep(0.2)
            campo_cidade.send_keys(cidade)
        else:
            raise Exception("Campo de cidade nao encontrado")

        time.sleep(2)

        # Clica na opcao do dropdown
        try:
            opcao_cidade = wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(), '{cidade} -') or contains(text(), '{cidade}/')]"))
            )
            opcao_cidade.click()
        except:
            try:
                opcao_cidade = driver.find_element(By.XPATH, f"//*[contains(text(), '{cidade}') and contains(text(), '-')]")
                opcao_cidade.click()
            except:
                opcao_cidade = driver.find_element(By.XPATH, f"//*[contains(text(), '{cidade}')]")
                driver.execute_script("arguments[0].click();", opcao_cidade)
        time.sleep(1)

        # Avancar
        clicar_avancar(driver)
        time.sleep(2)

        # Avancar novamente (faixas etarias ja estao preenchidas)
        clicar_avancar(driver)
        time.sleep(2)

        # Add Produtos
        print("[*] Adicionando produtos...")
        try:
            botao_add = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add Produtos')]"))
            )
            botao_add.click()
            time.sleep(2)
        except:
            pass

        # Sequencia do modal
        print("[*] Configurando opcoes no modal...")

        # Hapvida
        time.sleep(1)
        operadoras = driver.find_elements(By.XPATH, "//*[text()='Hapvida']")
        for op in operadoras:
            try:
                if op.is_displayed():
                    driver.execute_script("arguments[0].click();", op)
                    break
            except:
                continue
        time.sleep(1.5)

        # Tabela - Clica na PRIMEIRA opcao que aparece apos "Escolher Tabela:"
        # (o nome varia: "Hapvida Recife + Odonto", "Hapvida Fortaleza", etc)
        print("[*] Selecionando primeira tabela disponivel...")
        clicou_tabela = False

        # Metodo 1: Procura por elemento que contem "Hapvida" e a cidade ou "2 a 29"
        tabelas = driver.find_elements(By.XPATH, "//*[contains(text(), 'Hapvida') and contains(text(), '2 a 29')]")
        for tab in tabelas:
            try:
                texto = tab.text or ""
                # Ignora se tiver "SEM" (sem odonto) - queremos a primeira opcao com odonto se houver
                if tab.is_displayed() and "SEM" not in texto.upper():
                    driver.execute_script("arguments[0].click();", tab)
                    print(f"[*] Clicou na tabela: {texto}")
                    clicou_tabela = True
                    break
            except:
                continue

        # Metodo 2: Se nao encontrou, clica na primeira opcao que tiver "2 a 29"
        if not clicou_tabela:
            tabelas2 = driver.find_elements(By.XPATH, "//*[contains(text(), '2 a 29')]")
            for tab in tabelas2:
                try:
                    if tab.is_displayed():
                        driver.execute_script("arguments[0].click();", tab)
                        print(f"[*] Clicou na tabela (metodo 2): {tab.text}")
                        clicou_tabela = True
                        break
                except:
                    continue

        # Metodo 3: Clica em qualquer elemento logo apos "Escolher Tabela:"
        if not clicou_tabela:
            try:
                primeira_tabela = driver.find_element(By.XPATH, "//div[contains(text(), 'Escolher Tabela:')]/following-sibling::div[1]")
                driver.execute_script("arguments[0].click();", primeira_tabela)
                print("[*] Clicou na primeira tabela (metodo 3)")
            except:
                pass

        time.sleep(1.5)

        # Ambulatorial
        planos = driver.find_elements(By.XPATH, "//*[text()='Ambulatorial']")
        for plano in planos:
            try:
                if plano.is_displayed():
                    driver.execute_script("arguments[0].click();", plano)
                    break
            except:
                continue
        time.sleep(1.5)

        # Sem acomodacao / Com coparticipacao
        opcoes = driver.find_elements(By.XPATH, "//*[contains(text(), 'Sem acomodação / Com coparticipação') and not(contains(text(), 'Parcial'))]")
        for opc in opcoes:
            try:
                if opc.is_displayed():
                    driver.execute_script("arguments[0].click();", opc)
                    break
            except:
                continue
        time.sleep(2)

        # Fechar modal
        try:
            x_btn = driver.find_element(By.XPATH, "//div[contains(@style, 'background') and contains(@style, 'rgb(231, 76, 60)')]")
            driver.execute_script("arguments[0].click();", x_btn)
        except:
            pass
        time.sleep(1)

        # Extrair valores
        print("[*] Extraindo valores...")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        valores = extrair_valores(driver)

        # Verifica se JSON esta vazio - se sim, tenta clicar nas opcoes novamente
        if not valores or len(valores) == 0:
            print("[AVISO] JSON vazio! Tentando selecionar opcoes novamente...")
            time.sleep(1)

            # Tenta clicar no Add Produtos novamente
            try:
                botao_add = driver.find_element(By.XPATH, "//button[contains(., 'Add Produtos')]")
                if botao_add.is_displayed():
                    driver.execute_script("arguments[0].click();", botao_add)
                    time.sleep(2)

                    # Refaz a sequencia do modal
                    # Hapvida
                    operadoras = driver.find_elements(By.XPATH, "//*[text()='Hapvida']")
                    for op in operadoras:
                        try:
                            if op.is_displayed():
                                driver.execute_script("arguments[0].click();", op)
                                break
                        except:
                            continue
                    time.sleep(1.5)

                    # Primeira tabela
                    tabelas = driver.find_elements(By.XPATH, "//*[contains(text(), '2 a 29')]")
                    for tab in tabelas:
                        try:
                            if tab.is_displayed() and "SEM" not in (tab.text or "").upper():
                                driver.execute_script("arguments[0].click();", tab)
                                break
                        except:
                            continue
                    time.sleep(1.5)

                    # Ambulatorial
                    planos = driver.find_elements(By.XPATH, "//*[text()='Ambulatorial']")
                    for plano in planos:
                        try:
                            if plano.is_displayed():
                                driver.execute_script("arguments[0].click();", plano)
                                break
                        except:
                            continue
                    time.sleep(1.5)

                    # Coparticipacao
                    opcoes = driver.find_elements(By.XPATH, "//*[contains(text(), 'Sem acomodação / Com coparticipação') and not(contains(text(), 'Parcial'))]")
                    for opc in opcoes:
                        try:
                            if opc.is_displayed():
                                driver.execute_script("arguments[0].click();", opc)
                                break
                        except:
                            continue
                    time.sleep(2)

                    # Tenta extrair novamente
                    valores = extrair_valores(driver)
            except:
                pass

        print(f"[OK] Cotacao concluida para {cidade}")
        return {
            "cidade": cidade,
            "sucesso": True if valores and len(valores) > 0 else False,
            "valores": valores,
            "erro": "Nenhum valor encontrado" if not valores or len(valores) == 0 else None
        }

    except Exception as e:
        print(f"[ERRO] Erro na cotacao de {cidade}: {str(e)}")
        return {
            "cidade": cidade,
            "sucesso": False,
            "erro": str(e)
        }


def extrair_valores(driver):
    """Extrai os valores da tabela de precos."""
    faixas = [
        "0 a 18 anos",
        "19 a 23 anos",
        "24 a 28 anos",
        "29 a 33 anos",
        "34 a 38 anos",
        "39 a 43 anos",
        "44 a 48 anos",
        "49 a 53 anos",
        "54 a 58 anos",
        "59 anos ou mais"
    ]

    valores = []

    try:
        # Rola a pagina para garantir que os valores estejam visiveis
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        # Metodo 1: Busca pela coluna "Por:" que contem os valores
        # Os valores aparecem apos o texto "Por:" na interface
        elementos = driver.find_elements(By.XPATH, "//*[contains(text(), 'Por:')]/following-sibling::*")

        valores_encontrados = []

        # Metodo 2: Busca todos elementos que contem valores no formato ###,##
        todos_elementos = driver.find_elements(By.XPATH, "//*")
        for elem in todos_elementos:
            try:
                texto = elem.text.strip()
                # Verifica se e um valor monetario (formato ###,## sem texto adicional)
                if texto and ',' in texto:
                    # Remove pontos de milhar e verifica se e numero
                    texto_limpo = texto.replace('.', '').replace(',', '.').replace('R$', '').replace(' ', '')
                    try:
                        valor_num = float(texto_limpo)
                        # Valores de plano geralmente estao entre 50 e 2000
                        if 50 < valor_num < 2000:
                            valores_encontrados.append(texto)
                    except:
                        pass
            except:
                pass

        # Remove duplicatas mantendo a ordem
        valores_unicos = []
        for v in valores_encontrados:
            if v not in valores_unicos:
                valores_unicos.append(v)

        # Pega os primeiros 10 valores (as 10 faixas etarias)
        for i, valor in enumerate(valores_unicos[:10]):
            if i < len(faixas):
                valor_formatado = valor if valor.startswith("R$") else f"R$ {valor}"
                valores.append({
                    "faixa_etaria": faixas[i],
                    "valor": valor_formatado
                })

        print(f"[*] Encontrados {len(valores)} valores de faixas etarias")

    except Exception as e:
        print(f"[ERRO] Erro ao extrair valores: {str(e)}")

    return valores


# ============================================
# ROTAS DA APLICACAO WEB
# ============================================

@app.route('/')
def index():
    """Pagina inicial."""
    return render_template('index_cotacao.html')


@app.route('/cotar', methods=['POST'])
def cotar():
    """Rota para executar cotacao."""
    global primeira_cotacao, driver_global

    try:
        dados = request.get_json()
        cidades = dados.get('cidades', [])

        if not cidades:
            return jsonify({"erro": "Nenhuma cidade informada"}), 400

        resultados = []

        for i, cidade in enumerate(cidades):
            cidade = cidade.strip()
            if cidade:
                print(f"\n{'='*50}")
                print(f"[*] Cotando cidade {i+1}/{len(cidades)}: {cidade}")
                print(f"{'='*50}")

                try:
                    if i == 0 or primeira_cotacao or driver_global is None:
                        # Primeira cidade: faz o fluxo completo
                        resultado = cotar_cidade(cidade)
                        primeira_cotacao = False
                    else:
                        # Demais cidades: volta para tela de cidade e cota
                        voltar_para_cidade(driver_global)
                        resultado = cotar_proxima_cidade(cidade)
                except Exception as e:
                    print(f"[ERRO] Excecao ao cotar {cidade}: {str(e)}")
                    resultado = {
                        "cidade": cidade,
                        "sucesso": False,
                        "erro": str(e)
                    }
                    primeira_cotacao = True

                resultados.append(resultado)

                # Se deu erro, tenta o fluxo completo na proxima
                if not resultado.get("sucesso"):
                    primeira_cotacao = True

        return jsonify(resultados)

    except Exception as e:
        print(f"[ERRO] Excecao geral na rota /cotar: {str(e)}")
        return jsonify([{"cidade": "N/A", "sucesso": False, "erro": f"Erro geral: {str(e)}"}]), 500


@app.route('/status')
def status():
    """Verifica status do sistema."""
    global driver_global, logado
    return jsonify({
        "navegador_ativo": driver_global is not None,
        "logado": logado
    })


@app.route('/login', methods=['POST'])
def login():
    """Faz login no sistema."""
    sucesso = fazer_login()
    return jsonify({"sucesso": sucesso})


@app.route('/fechar')
def fechar():
    """Fecha o navegador."""
    global driver_global, logado
    if driver_global:
        driver_global.quit()
        driver_global = None
        logado = False
    return jsonify({"mensagem": "Navegador fechado"})


# ============================================
# MAIN
# ============================================

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))

    print("\n" + "="*60)
    print("  APLICACAO WEB - COTACAO HAPVIDA")
    print("="*60)
    print(f"\n  Acesse: http://localhost:{port}")
    print("\n  Endpoints:")
    print("    GET  /         - Pagina inicial")
    print("    POST /cotar    - Executar cotacao")
    print("    POST /login    - Fazer login")
    print("    GET  /status   - Verificar status")
    print("    GET  /fechar   - Fechar navegador")
    print("\n" + "="*60 + "\n")

    app.run(debug=False, host='0.0.0.0', port=port, threaded=True)
