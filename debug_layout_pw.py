"""
Versao Playwright do diagnostico de layout (para uso em ambientes onde
o Selenium nao consegue casar Chrome/ChromeDriver). Mesmas capturas:
  - screenshot PNG
  - HTML completo
  - catalogo JSON de elementos interativos + textos

Uso:
    python debug_layout_pw.py              # PME
    python debug_layout_pw.py --pf
    python debug_layout_pw.py --so-login
"""

import argparse
import glob
import json
import os
import shutil
import sys
import traceback

from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

from app_cotacao import EMAIL, SENHA, URL_LOGIN

OUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "debug_output"))
STEP = [0]

CATALOGO_JS = r"""
() => {
  const rect = (el) => { const r = el.getBoundingClientRect(); return {x:Math.round(r.x), y:Math.round(r.y), w:Math.round(r.width), h:Math.round(r.height)}; };
  const visivel = (el) => { const r = el.getBoundingClientRect(); return r.width>0 && r.height>0 && el.offsetParent !== null; };
  const saida = {buttons:[], inputs:[], selects:[], links:[], roles:[], textos:[]};
  const sel = 'button, input, select, textarea, a, [role="button"], [role="textbox"], [role="combobox"], [role="listbox"], [role="option"], [role="tab"], [role="menuitem"]';
  document.querySelectorAll(sel).forEach((el) => {
    if (!visivel(el)) return;
    const info = {
      tag: el.tagName.toLowerCase(),
      type: el.getAttribute('type') || null,
      role: el.getAttribute('role') || null,
      id: el.id || null,
      name: el.getAttribute('name') || null,
      placeholder: el.getAttribute('placeholder') || null,
      aria_label: el.getAttribute('aria-label') || null,
      text: ((el.innerText || el.value || '') + '').trim().slice(0, 120),
      rect: rect(el),
      classes: (el.className && el.className.toString) ? el.className.toString().slice(0, 200) : null
    };
    if (info.tag === 'button') saida.buttons.push(info);
    else if (info.tag === 'input' || info.tag === 'textarea') saida.inputs.push(info);
    else if (info.tag === 'select') saida.selects.push(info);
    else if (info.tag === 'a') saida.links.push(info);
    else saida.roles.push(info);
  });
  const vistos = new Set();
  document.querySelectorAll('*').forEach((el) => {
    if (!visivel(el)) return;
    const t = (el.innerText || '').trim();
    if (!t || t.length < 2 || t.length > 80) return;
    if (vistos.has(t)) return;
    vistos.add(t);
    saida.textos.push({text: t, tag: el.tagName.toLowerCase(), rect: rect(el)});
  });
  saida.textos = saida.textos.slice(0, 300);
  return saida;
}
"""


def log(m):
    print(f"[debug] {m}", file=sys.stderr, flush=True)


def reset_output_dir():
    if os.path.isdir(OUT_DIR):
        shutil.rmtree(OUT_DIR)
    os.makedirs(OUT_DIR, exist_ok=True)


def encontrar_chrome():
    candidatos = [os.environ.get("CHROME_BIN", "")]
    candidatos += sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"), reverse=True)
    candidatos += ["/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser"]
    for p in candidatos:
        if p and os.path.exists(p):
            return p
    return None


def snapshot(page, etapa):
    STEP[0] += 1
    n = STEP[0]
    safe = etapa.replace(" ", "_").replace("/", "_")
    base = os.path.join(OUT_DIR, f"{n:02d}_{safe}")
    try:
        page.screenshot(path=f"{base}.png", full_page=False)
    except Exception as e:
        log(f"  ! screenshot: {e}")
    try:
        with open(f"{base}.html", "w", encoding="utf-8") as f:
            f.write(page.content())
    except Exception as e:
        log(f"  ! html: {e}")
    try:
        cat = page.evaluate(CATALOGO_JS)
        cat["_meta"] = {"url": page.url, "title": page.title(), "etapa": etapa}
        with open(f"{base}.json", "w", encoding="utf-8") as f:
            json.dump(cat, f, ensure_ascii=False, indent=2)
        log(f"  -> {n:02d}_{safe}: {len(cat['buttons'])}B {len(cat['inputs'])}I "
            f"{len(cat['selects'])}S {len(cat['links'])}L {len(cat['roles'])}R "
            f"{len(cat['textos'])}T")
    except Exception as e:
        log(f"  ! catalogo: {e}")


def tentar(page, descricao, fn):
    log(f"== {descricao}")
    try:
        fn()
        page.wait_for_timeout(1500)
        snapshot(page, descricao)
        return True
    except Exception as e:
        log(f"  X erro em '{descricao}': {e}")
        snapshot(page, f"ERRO_{descricao}")
        traceback.print_exc(file=sys.stderr)
        return False


def fazer_login(page):
    page.goto(URL_LOGIN, wait_until="domcontentloaded", timeout=30000)
    page.wait_for_timeout(3000)
    snapshot(page, "login_inicial")

    try:
        page.locator("input[type='email'], input[placeholder='Seu email']").first.fill(EMAIL)
        page.wait_for_timeout(500)
        snapshot(page, "login_email_preenchido")
    except Exception as e:
        log(f"  ! preencher email falhou: {e}")
        snapshot(page, "ERRO_login_email")
        return False

    try:
        page.get_by_role("button", name=lambda n: n and "Continuar com Email" in n).first.click()
    except Exception:
        try:
            page.locator("button:has-text('Continuar com Email')").first.click()
        except Exception as e:
            log(f"  ! botao 'Continuar com Email' nao achado: {e}")
    page.wait_for_timeout(3000)
    snapshot(page, "login_apos_email")

    try:
        page.locator("input[type='password']").first.fill(SENHA)
        page.wait_for_timeout(500)
        snapshot(page, "login_senha_preenchida")
        try:
            page.locator("button:has-text('Entrar')").first.click()
        except Exception:
            page.locator("button:has-text('Acessar')").first.click()
        page.wait_for_timeout(4000)
    except Exception as e:
        log(f"  ! senha/entrar: {e}")
    snapshot(page, "login_apos_entrar")

    if "login" in page.url.lower():
        log("  X login NAO concluiu - URL ainda em /login")
        return False
    log("  OK login concluido")
    return True


def explorar_home(page):
    page.goto("https://app.cotadorsimplificado.com.br/", wait_until="domcontentloaded", timeout=30000)
    page.wait_for_timeout(4000)
    snapshot(page, "home")


def explorar_fluxo(page, tipo, cidade):
    label_tipo = "PME até 29 vidas" if tipo == "pme" else "PF / Coletivos"

    def avancar():
        page.locator("button:has-text('Avançar'):visible").first.click()

    tentar(page, "home_carregada", lambda: (
        page.goto("https://app.cotadorsimplificado.com.br/", wait_until="domcontentloaded", timeout=30000),
        page.wait_for_timeout(4000)
    ))
    tentar(page, "clicou_cotar_hapvida", lambda: page.locator("text=Cotar Hapvida").first.click())
    tentar(page, f"clicou_{tipo}", lambda: page.locator(f"text={label_tipo}").first.click())

    def preencher_nome():
        page.locator("input[placeholder*='cliente']").first.fill("teste")
        page.wait_for_timeout(1000)
    tentar(page, "preencheu_nome_cliente", preencher_nome)

    tentar(page, "avancou_pos_nome", avancar)

    def selecionar_cidade():
        # acha o input cuja placeholder contem " - " ou "cidade"
        encontrados = page.evaluate("""
            () => {
              const arr = [];
              document.querySelectorAll('input').forEach((el, i) => {
                const ph = (el.placeholder || '').toLowerCase();
                const r = el.getBoundingClientRect();
                if (r.width > 0 && r.height > 0 && el.offsetParent && (ph.includes(' - ') || ph.includes('cidade'))) {
                  arr.push(i);
                }
              });
              return arr;
            }
        """)
        if not encontrados:
            raise RuntimeError("nenhum input de cidade visivel")
        page.locator("input").nth(encontrados[0]).click()
        page.locator("input").nth(encontrados[0]).fill(cidade)
        page.wait_for_timeout(2000)
        page.locator(f"text=/^{cidade}\\s*[-/]/").first.click()
        page.wait_for_timeout(1000)
    tentar(page, f"selecionou_cidade_{cidade}", selecionar_cidade)

    if tipo == "pme":
        def selecionar_mei():
            sel = page.locator("select:visible").first
            sel.select_option(label="MEI")
        tentar(page, "selecionou_mei", selecionar_mei)

    tentar(page, "avancou_pos_cidade", avancar)

    def preencher_faixas():
        campos = page.locator("input[placeholder='0']")
        n = campos.count()
        if n == 0:
            raise RuntimeError("nenhum input de faixa visivel")
        for i in range(min(n, 10)):
            try:
                campos.nth(i).fill("1")
            except Exception:
                pass
    tentar(page, "preencheu_faixas_etarias", preencher_faixas)

    tentar(page, "avancou_pos_faixas", avancar)

    tentar(page, "abriu_modal_produtos",
           lambda: page.locator("button:has-text('Add Produtos')").first.click())

    log("== FIM do fluxo explorado")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pf", action="store_true")
    parser.add_argument("--cidade", default="Aracaju")
    parser.add_argument("--so-login", action="store_true")
    args = parser.parse_args()

    reset_output_dir()
    log(f"output em {OUT_DIR}")
    chrome = encontrar_chrome()
    log(f"chrome binary: {chrome}")

    with sync_playwright() as pw:
        browser = pw.chromium.launch(
            headless=True,
            executable_path=chrome,
            args=["--no-sandbox", "--disable-dev-shm-usage", "--ignore-certificate-errors",
                  "--disable-notifications", "--disable-popup-blocking"],
        )
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True,
        )
        page = context.new_page()
        page.set_default_timeout(15000)

        try:
            if not fazer_login(page):
                log("login falhou - veja arquivos *login* em debug_output/")
                return 1
            explorar_home(page)
            if args.so_login:
                return 0
            explorar_fluxo(page, "pf" if args.pf else "pme", args.cidade)
            return 0
        finally:
            browser.close()


if __name__ == "__main__":
    sys.exit(main())
