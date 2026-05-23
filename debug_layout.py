"""
Script de diagnostico do layout do cotadorsimplificado.com.br.

Percorre o fluxo de cotacao e em cada etapa captura:
  - screenshot PNG
  - HTML completo da pagina
  - catalogo de elementos interativos (buttons, inputs, selects, a, [role])
  - lista de textos visiveis com posicao/tamanho

Output em ./debug_output/NN_<etapa>.{png,html,json}

Uso:
    python debug_layout.py              # roda o fluxo PME completo
    python debug_layout.py --pf         # roda o fluxo PF/Coletivos
    python debug_layout.py --cidade Recife
    DEBUG_HEADED=1 python debug_layout.py   # tenta abrir janela visivel
"""

import argparse
import glob
import json
import os
import shutil
import sys
import time
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from app_cotacao import EMAIL, SENHA, URL_LOGIN


OUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "debug_output"))
STEP_COUNTER = [0]


def log(msg):
    print(f"[debug] {msg}", file=sys.stderr, flush=True)


def reset_output_dir():
    if os.path.isdir(OUT_DIR):
        shutil.rmtree(OUT_DIR)
    os.makedirs(OUT_DIR, exist_ok=True)


def encontrar_chrome_binary():
    candidatos = [
        os.environ.get("CHROME_BIN", ""),
        "/usr/bin/google-chrome",
        "/usr/bin/chromium",
        "/usr/bin/chromium-browser",
    ]
    candidatos += sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"), reverse=True)
    for p in candidatos:
        if p and os.path.exists(p):
            return p
    return None


def iniciar_navegador():
    chrome_options = Options()
    if not os.environ.get("DEBUG_HEADED"):
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-extensions")

    binary = encontrar_chrome_binary()
    if binary:
        chrome_options.binary_location = binary
        log(f"chrome binary: {binary}")

    # Selenium Manager (built-in no Selenium 4.6+) baixa driver compativel
    try:
        return webdriver.Chrome(options=chrome_options)
    except Exception as e:
        log(f"selenium manager falhou ({e}); tentando fallbacks")

    for path in (os.environ.get("CHROMEDRIVER_PATH", ""),
                 "/usr/bin/chromedriver",
                 "/usr/local/bin/chromedriver",
                 "/opt/node22/bin/chromedriver"):
        if path and os.path.exists(path):
            try:
                return webdriver.Chrome(service=Service(path), options=chrome_options)
            except Exception:
                continue
    from webdriver_manager.chrome import ChromeDriverManager
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


def catalogo_elementos(driver):
    """Lista todos elementos interativos visiveis com atributos uteis."""
    return driver.execute_script(r"""
        function rect(el){var r=el.getBoundingClientRect();return {x:Math.round(r.x),y:Math.round(r.y),w:Math.round(r.width),h:Math.round(r.height)};}
        function visivel(el){var r=el.getBoundingClientRect();return r.width>0&&r.height>0&&el.offsetParent!==null;}
        var saida = {buttons:[], inputs:[], selects:[], links:[], roles:[], textos:[]};
        var seletor = 'button, input, select, textarea, a, [role="button"], [role="textbox"], [role="combobox"], [role="listbox"], [role="option"], [role="tab"], [role="menuitem"]';
        document.querySelectorAll(seletor).forEach(function(el){
            if(!visivel(el)) return;
            var info = {
                tag: el.tagName.toLowerCase(),
                type: el.getAttribute('type') || null,
                role: el.getAttribute('role') || null,
                id: el.id || null,
                name: el.getAttribute('name') || null,
                placeholder: el.getAttribute('placeholder') || null,
                aria_label: el.getAttribute('aria-label') || null,
                text: (el.innerText || el.value || '').trim().slice(0, 120),
                rect: rect(el),
                classes: (el.className && el.className.toString) ? el.className.toString().slice(0, 200) : null
            };
            if (info.tag === 'button') saida.buttons.push(info);
            else if (info.tag === 'input' || info.tag === 'textarea') saida.inputs.push(info);
            else if (info.tag === 'select') saida.selects.push(info);
            else if (info.tag === 'a') saida.links.push(info);
            else saida.roles.push(info);
        });
        // Textos curtos visiveis (uteis pra achar headers tipo "Escolher Operadora:")
        var vistos = new Set();
        document.querySelectorAll('*').forEach(function(el){
            if (!visivel(el)) return;
            var t = (el.innerText || '').trim();
            if (!t || t.length < 2 || t.length > 80) return;
            if (vistos.has(t)) return;
            vistos.add(t);
            saida.textos.push({text: t, tag: el.tagName.toLowerCase(), rect: rect(el)});
        });
        // Limita pra nao explodir o JSON
        saida.textos = saida.textos.slice(0, 300);
        return saida;
    """)


def snapshot(driver, etapa):
    """Captura screenshot + HTML + catalogo da pagina atual."""
    STEP_COUNTER[0] += 1
    n = STEP_COUNTER[0]
    safe = etapa.replace(" ", "_").replace("/", "_")
    base = os.path.join(OUT_DIR, f"{n:02d}_{safe}")

    try:
        driver.save_screenshot(f"{base}.png")
    except Exception as e:
        log(f"  ! screenshot falhou: {e}")

    try:
        with open(f"{base}.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
    except Exception as e:
        log(f"  ! html dump falhou: {e}")

    try:
        cat = catalogo_elementos(driver)
        cat["_meta"] = {
            "url": driver.current_url,
            "title": driver.title,
            "etapa": etapa,
        }
        with open(f"{base}.json", "w", encoding="utf-8") as f:
            json.dump(cat, f, ensure_ascii=False, indent=2)
        log(f"  -> {n:02d}_{safe}: {len(cat['buttons'])}B {len(cat['inputs'])}I {len(cat['selects'])}S {len(cat['links'])}L {len(cat['roles'])}R")
    except Exception as e:
        log(f"  ! catalogo falhou: {e}")


def tentar(driver, descricao, fn, salvar_apos=True):
    """Executa uma acao, captura erros, snapshot apos."""
    log(f"== {descricao}")
    try:
        fn()
        if salvar_apos:
            time.sleep(2)
            snapshot(driver, descricao)
        return True
    except Exception as e:
        log(f"  X falhou em '{descricao}': {e}")
        snapshot(driver, f"ERRO_{descricao}")
        traceback.print_exc(file=sys.stderr)
        return False


def fazer_login(driver):
    wait = WebDriverWait(driver, 20)
    driver.get(URL_LOGIN)
    time.sleep(3)
    snapshot(driver, "login_inicial")

    campo_email = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[type='email'], input[placeholder='Seu email']")))
    campo_email.clear()
    campo_email.send_keys(EMAIL)
    time.sleep(0.5)
    snapshot(driver, "login_email_preenchido")

    try:
        botao = driver.find_element(By.XPATH, "//button[contains(., 'Continuar com Email')]")
        botao.click()
    except Exception:
        log("  ! botao 'Continuar com Email' nao encontrado - layout pode ter mudado aqui")
    time.sleep(3)
    snapshot(driver, "login_apos_email")

    try:
        campo_senha = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']")))
        campo_senha.clear()
        campo_senha.send_keys(SENHA)
        time.sleep(0.5)
        snapshot(driver, "login_senha_preenchida")

        botao_entrar = driver.find_element(By.XPATH, "//button[contains(., 'Entrar')]")
        botao_entrar.click()
        time.sleep(4)
    except Exception as e:
        log(f"  ! senha/entrar falhou: {e}")
    snapshot(driver, "login_apos_entrar")

    if "login" in driver.current_url.lower():
        log("  X login NAO concluiu - url ainda contem 'login'")
        return False
    log("  OK login concluido")
    return True


def explorar_home(driver):
    driver.get("https://app2.cotadorsimplificado.com.br/")
    time.sleep(4)
    snapshot(driver, "home")


def explorar_fluxo(driver, tipo, cidade):
    """Explora o fluxo do app2 capturando cada tela.

    app2 e SPA limpa (nao Bubble.io): botoes/links/inputs reais.
    Estrategia: clica 'Nova Cotacao', captura, espera, captura de novo
    pra ver se algo dinamico carrega. Quando souber a tela seguinte,
    adicione mais etapas aqui.
    """
    wait = WebDriverWait(driver, 15)

    tentar(driver, "home_dashboard", lambda: (
        driver.get("https://app2.cotadorsimplificado.com.br/dashboard"),
        time.sleep(4)
    ))

    def clicar_nova_cotacao():
        # tenta varios seletores possiveis pro botao "Nova Cotacao"
        candidatos = [
            (By.XPATH, "//button[.//p[normalize-space(text())='Nova Cotação']]"),
            (By.XPATH, "//button[contains(., 'Nova Cotação')]"),
            (By.XPATH, "//a[contains(., 'Nova Cotação')]"),
            (By.XPATH, "//*[contains(text(), 'Nova Cotação')]"),
        ]
        for by, sel in candidatos:
            try:
                el = wait.until(EC.element_to_be_clickable((by, sel)))
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
                time.sleep(0.5)
                el.click()
                return
            except Exception:
                continue
        raise RuntimeError("botao 'Nova Cotacao' nao encontrado")

    tentar(driver, "clicou_nova_cotacao", clicar_nova_cotacao)

    # Captura snapshots adicionais ao longo de alguns segundos pra pegar
    # qualquer transicao/modal/spinner que apareca depois do click
    for i, espera in enumerate([2, 3, 5], start=1):
        time.sleep(espera)
        snapshot(driver, f"apos_nova_cotacao_{i}")

    log("== FIM da exploracao app2 - revise debug_output/ e adicione proxima etapa")
    tentar(driver, "abriu_modal_produtos", abrir_modal)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pf", action="store_true", help="Roda o fluxo PF/Coletivos em vez de PME")
    parser.add_argument("--cidade", default="Aracaju")
    parser.add_argument("--so-login", action="store_true", help="Para apos o login (so captura login + home)")
    args = parser.parse_args()

    reset_output_dir()
    log(f"output em {OUT_DIR}")

    driver = None
    try:
        driver = iniciar_navegador()
        if not fazer_login(driver):
            log("login falhou - veja os arquivos *login* em debug_output/")
            return 1
        explorar_home(driver)
        if args.so_login:
            return 0
        tipo = "pf" if args.pf else "pme"
        explorar_fluxo(driver, tipo, args.cidade)
        return 0
    finally:
        if driver:
            try:
                driver.quit()
            except Exception:
                pass


if __name__ == "__main__":
    sys.exit(main())
