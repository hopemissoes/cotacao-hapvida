# -*- coding: utf-8 -*-
"""
checkpoint_onpage.py — trava mecânica do KIT ON-PAGE DE KEYWORDS [V5]
(hapvida-article-builder-v5)

Confere a matriz de posicionamento:
  KEYWORD PRINCIPAL → 1º parágrafo do corpo, ≥1 H2 (no HTML)
                      e, quando informados via flags: H1, title SEO, URL/slug, meta description.
  SECUNDÁRIAS       → ≥2 H2 distintos do artigo contêm alguma secundária.

O matching é por PALAVRAS (ignora acento, maiúscula/minúscula, ordem e plural
simples) — variação natural passa; ausência real não passa. Não mede densidade:
stuffing continua sendo julgamento (Regra de Ouro nº 1).

Uso:
  python -X utf8 checkpoint_onpage.py artigo.html --kw "plano hapvida piracicaba" ^
      --sec "hapvida piracicaba preço;plano de saúde piracicaba" ^
      --h1 "..." --title "..." --url "plano-hapvida-piracicaba" --meta "..."

Saída: relatório + "✅ APROVADO" ou "❌ REPROVADO" (exit code 1).
Flags --h1/--title/--url/--meta são opcionais: sem elas, esses itens saem como
⚠️ NÃO CONFERIDO (lembrete), sem reprovar.
"""
import argparse
import html as htmlmod
import re
import sys
import unicodedata

STOPWORDS = {
    "de", "da", "do", "das", "dos", "em", "no", "na", "nos", "nas",
    "o", "a", "os", "as", "e", "ou", "um", "uma", "para", "pra",
    "com", "por", "que", "ao", "aos", "à", "às",
}


def normalize(text: str) -> str:
    text = htmlmod.unescape(text or "")
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return text.lower()


def tokens(text: str) -> set:
    words = re.findall(r"[a-z0-9]+", normalize(text))
    out = set()
    for w in words:
        if w in STOPWORDS:
            continue
        # stem tosco: singular/plural simples (planos→plano, hospitais→hospitai é
        # tratado abaixo; preços→preco já veio sem acento)
        if len(w) > 3 and w.endswith("s"):
            w = w[:-1]
        out.add(w)
    return out


def kw_in(keyword: str, text: str) -> bool:
    """Todos os tokens significativos da keyword aparecem no texto."""
    kt = tokens(keyword)
    if not kt:
        return False
    tt = tokens(text)
    return kt.issubset(tt)


def strip_tags(fragment: str) -> str:
    return re.sub(r"<[^>]+>", " ", fragment)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html_file")
    ap.add_argument("--kw", required=True, help="keyword principal")
    ap.add_argument("--sec", default="", help="secundárias separadas por ';'")
    ap.add_argument("--h1", default=None)
    ap.add_argument("--title", default=None)
    ap.add_argument("--url", default=None)
    ap.add_argument("--meta", default=None)
    args = ap.parse_args()

    with open(args.html_file, "r", encoding="utf-8") as f:
        raw = f.read()

    # remover <style>/<script> para não poluir a análise
    body = re.sub(r"<style\b.*?</style>", " ", raw, flags=re.S | re.I)
    body = re.sub(r"<script\b.*?</script>", " ", body, flags=re.S | re.I)

    principal = args.kw
    secundarias = [s.strip() for s in args.sec.split(";") if s.strip()]

    falhas, avisos, oks = [], [], []

    # ---------- 1º parágrafo do corpo ----------
    paragrafos = re.findall(r"<p\b[^>]*>(.*?)</p>", body, flags=re.S | re.I)
    primeiro = ""
    for p in paragrafos:
        texto = strip_tags(p).strip()
        if len(texto) >= 60:  # pula <p> de figcaption/nota curtos
            primeiro = texto
            break
    if not primeiro:
        falhas.append("Nenhum parágrafo de corpo encontrado no HTML.")
    elif kw_in(principal, primeiro):
        oks.append("Principal no 1º parágrafo do corpo ✔")
    else:
        falhas.append(
            f"Principal AUSENTE do 1º parágrafo do corpo.\n    1º parágrafo: \"{primeiro[:140]}...\""
        )

    # ---------- H2 ----------
    h2s = [strip_tags(h).strip() for h in re.findall(r"<h2\b[^>]*>(.*?)</h2>", body, flags=re.S | re.I)]
    if not h2s:
        falhas.append("Nenhum <h2> encontrado no HTML.")
    else:
        h2_com_principal = [h for h in h2s if kw_in(principal, h)]
        if h2_com_principal:
            oks.append(f"Principal em {len(h2_com_principal)} H2 ✔ (ex.: \"{h2_com_principal[0][:70]}\")")
        else:
            falhas.append("Principal AUSENTE de todos os H2 (precisa de ≥1, vale variação natural).")

        if secundarias:
            h2_com_sec = []
            for h in h2s:
                for s in secundarias:
                    if kw_in(s, h):
                        h2_com_sec.append((h, s))
                        break
            if len(h2_com_sec) >= 2:
                oks.append(f"Secundárias em {len(h2_com_sec)} H2 ✔ (mín. 2)")
            else:
                falhas.append(
                    f"Apenas {len(h2_com_sec)} H2 contém secundária (mín. 2). Secundárias: {secundarias}"
                )
            if len(secundarias) < 6:
                avisos.append(
                    f"Só {len(secundarias)} secundárias informadas — o kit exige mín. 6 no state file "
                    "(as que não couberem em H2 vão para H3/corpo/FAQ)."
                )
        else:
            avisos.append("Nenhuma secundária informada via --sec — item ≥2 H2 com secundária NÃO conferido.")

    # ---------- flags opcionais ----------
    for nome, valor in (("H1", args.h1), ("Title SEO", args.title), ("URL/slug", args.url), ("Meta description", args.meta)):
        if valor is None:
            avisos.append(f"{nome}: não informado (--{nome.split()[0].lower().replace('/slug','').replace('description','meta').replace('seo','title').strip()}) — conferir manualmente.")
        elif kw_in(principal, valor.replace("-", " ")):
            oks.append(f"Principal no {nome} ✔")
        else:
            falhas.append(f"Principal AUSENTE do {nome}: \"{valor[:90]}\"")

    # ---------- relatório ----------
    print("=" * 62)
    print("CHECKPOINT ON-PAGE [V5] — matriz de posicionamento de keywords")
    print("=" * 62)
    print(f"Principal: {principal}")
    if secundarias:
        print(f"Secundárias ({len(secundarias)}): {'; '.join(secundarias)}")
    print("-" * 62)
    for m in oks:
        print(f"  ✅ {m}")
    for m in avisos:
        print(f"  ⚠️  {m}")
    for m in falhas:
        print(f"  ❌ {m}")
    print("-" * 62)
    if falhas:
        print("❌ REPROVADO — corrigir os itens acima e rodar de novo.")
        sys.exit(1)
    print("✅ APROVADO" + (" (com avisos — resolver os ⚠️ antes de publicar)" if avisos else ""))


if __name__ == "__main__":
    main()
