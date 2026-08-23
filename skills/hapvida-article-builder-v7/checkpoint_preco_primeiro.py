# -*- coding: utf-8 -*-
"""
checkpoint_preco_primeiro.py — trava mecânica da ORDEM PREÇO-PRIMEIRO [V7]
(hapvida-article-builder-v7)

Confere as regras duras da v7 (revisão 7.1):
  1. O shortcode que RENDERIZA A TABELA de preço (ou, em TR, a <figure> da imagem
     da tabela) é o primeiro conteúdo depois do Lead GEO — e vem ANTES do sumário.
  1b. [v7.1] O SUMÁRIO vem COLADO na tabela: entre as duas não entram formulário,
     faixa de conversão, selos, análise de preço nem a imagem da tabela
     (orçamento: 600 caracteres de texto visível).
  2. Nenhum H2 de outro assunto aparece antes do primeiro H2 de preço.

Uso:
  python -X utf8 checkpoint_preco_primeiro.py artigo.html [city|tr|pillar|hospital]

Sem o tipo, assume "city". Saída: relatório + "✅ APROVADO" ou "❌ REPROVADO"
(exit code 1). Só biblioteca padrão.

O que NÃO faz: não julga conteúdo, não mede anti-doorway, não conta palavras.
Ordem é o único assunto deste script.
"""
import html as htmlmod
import re
import sys
import unicodedata

# ---------------------------------------------------------------- normalização

def normalize(text):
    text = htmlmod.unescape(text or "")
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


# ---------------------------------------------------------------- vocabulário

# Assunto "preço" no H2. Casado por palavra normalizada (sem acento).
TERMOS_PRECO = [
    "preco", "precos", "valor", "valores", "mensalidade", "mensalidades",
    "quanto custa", "custo", "custos", "tabela", "tabelas", "investimento",
    "faixa etaria", "faixas etarias", "coparticipacao", "copart",
    "promocao", "promocoes", "desconto", "descontos", "a partir de",
]

# Assuntos que NUNCA contam como preço mesmo citando a palavra.
TERMOS_NAO_PRECO = [
    "rede assistencial", "rede propria", "hospital", "hospitais", "unidades",
    "cobertura por bairro", "bairros", "como contratar", "portabilidade",
    "carencia", "carencias", "cenario de saude", "perguntas frequentes",
    "duvidas", "conclusao", "planos disponiveis", "o que e", "quem pode",
]

# Shortcodes que renderizam TABELA INTEIRA (não valor pontual).
RE_SHORTCODE_TABELA = re.compile(
    r"\[[a-z0-9\-]+_(?:menortabela|(?:ind|emp)_[a-z]+(?:total|parcial))\](?!_)",
    re.IGNORECASE,
)
# Valor pontual: mesmo pattern com sufixo _0.._9 — NÃO conta como tabela.
RE_SHORTCODE_PONTUAL = re.compile(
    r"\[[a-z0-9\-]+_(?:ind|emp)_[a-z]+(?:total|parcial)_[0-9]\]", re.IGNORECASE
)
RE_H2 = re.compile(r"<h2\b[^>]*>(.*?)</h2>", re.IGNORECASE | re.DOTALL)
RE_TOC = re.compile(r"toc-list|class\s*=\s*[\"'][^\"']*\btoc\b", re.IGNORECASE)
RE_FIGURE = re.compile(r"<figure\b.*?</figure>", re.IGNORECASE | re.DOTALL)
RE_COTACAO1 = re.compile(r"id\s*=\s*[\"']cotacao-1[\"']", re.IGNORECASE)

# Orcamento de texto visivel permitido ANTES da tabela: imagem de abertura +
# Lead GEO (3 paragrafos) + os paragrafos de contexto local da propria secao de
# preco. Medido em caracteres de texto sem tags — nao depende do tamanho do
# arquivo, entao <style>/<script> gordos no fim nao mascaram o problema.
LIMITE_TEXTO_ANTES = 1800

# [v7.1] Orcamento de texto visivel permitido ENTRE a tabela e o sumario. So cabe
# a frase de leitura da tabela. Formulario, faixa navy, selos, analise de preco e
# imagem da tabela ficam DEPOIS do sumario.
LIMITE_TEXTO_TABELA_SUMARIO = 600


def h2_e_de_preco(texto_h2):
    t = normalize(texto_h2)
    for termo in TERMOS_NAO_PRECO:
        if termo in t:
            # "tabela de preço" dentro de um H2 de rede não promove o H2.
            if not any(p in t for p in ("preco", "valor", "tabela", "quanto custa", "mensalidade")):
                return False
    return any(termo in t for termo in TERMOS_PRECO)


def pos_primeira_tabela(html, tipo):
    """Posição (char) da primeira tabela de preço renderizada."""
    m = RE_SHORTCODE_TABELA.search(html)
    pos_sc = m.start() if m else None
    if tipo != "tr":
        return pos_sc, ("shortcode " + m.group(0)) if m else None
    # Em TR a tabela é IMAGEM: procurar <figure> cujo alt/figcaption fale de tabela.
    for fig in RE_FIGURE.finditer(html):
        if "tabela" in normalize(fig.group(0)):
            if pos_sc is not None and pos_sc < fig.start():
                return pos_sc, "shortcode " + m.group(0)
            return fig.start(), "<figure> da imagem da tabela"
    return pos_sc, ("shortcode " + m.group(0)) if m else None


def main():
    if len(sys.argv) < 2:
        print("Uso: python -X utf8 checkpoint_preco_primeiro.py artigo.html [city|tr|pillar|hospital]")
        sys.exit(2)
    caminho = sys.argv[1]
    tipo = (sys.argv[2].lower() if len(sys.argv) > 2 else "city")
    if tipo not in ("city", "tr", "pillar", "hospital"):
        print("Tipo invalido. Use: city | tr | pillar | hospital")
        sys.exit(2)

    with open(caminho, "r", encoding="utf-8", errors="replace") as fh:
        html = fh.read()

    erros, avisos, notas = [], [], []
    total = max(len(html), 1)

    print("=" * 72)
    print("CHECKPOINT PRECO-PRIMEIRO [V7.1] — %s (tipo: %s)" % (caminho, tipo))
    print("=" * 72)

    # ---- H2 -------------------------------------------------------------
    h2s = [(m.start(), re.sub(r"\s+", " ", normalize(m.group(1)))) for m in RE_H2.finditer(html)]
    if not h2s:
        erros.append("Nenhum <h2> encontrado no arquivo.")
    precos = [(p, t) for p, t in h2s if h2_e_de_preco(t)]
    outros = [(p, t) for p, t in h2s if not h2_e_de_preco(t)]

    print("\n[H2 encontrados: %d | de preco: %d | de outros assuntos: %d]" % (len(h2s), len(precos), len(outros)))
    for p, t in h2s:
        marca = "PRECO" if h2_e_de_preco(t) else "     "
        print("   %s  %3.0f%%  %s" % (marca, 100.0 * p / total, t[:64]))

    # ---- Regra 1: tabela primeiro ---------------------------------------
    pos_tab, desc_tab = pos_primeira_tabela(html, tipo)
    m_toc = RE_TOC.search(html)
    pos_toc = m_toc.start() if m_toc else None

    print("\n[Regra 1 — tabela primeiro]")
    if pos_tab is None:
        if tipo == "hospital":
            notas.append("Artigo de hospital sem tabela de preco — regra 1 nao se aplica (ok).")
            print("   - sem tabela de preco; tipo hospital: regra 1 dispensada")
        else:
            erros.append("Nenhum shortcode/imagem de TABELA de preco encontrado no artigo.")
            print("   - NENHUMA tabela de preco encontrada")
    else:
        pct = 100.0 * pos_tab / total
        # Metrica robusta: texto VISIVEL (sem tags) antes da tabela.
        texto_antes = normalize(html[:pos_tab])
        n_antes = len(texto_antes)
        print("   - primeira tabela: %s" % desc_tab)
        print("   - texto visivel antes dela: %d caracteres (a %.0f%% do arquivo)" % (n_antes, pct))
        if n_antes > LIMITE_TEXTO_ANTES:
            erros.append(
                "Ha %d caracteres de texto antes da tabela (limite: %d ~= imagem + lead GEO + "
                "os paragrafos de contexto da propria secao de preco)." % (n_antes, LIMITE_TEXTO_ANTES)
            )
        if pos_toc is not None:
            print("   - sumario (toc-list) a %.0f%% do arquivo" % (100.0 * pos_toc / total))
            if pos_toc < pos_tab:
                erros.append("Sumario aparece ANTES da tabela de preco. Na v7 o sumario vem depois.")
            else:
                # ---- Regra 1b [v7.1]: sumario COLADO na tabela --------------
                miolo = html[pos_tab:pos_toc]
                n_miolo = len(normalize(miolo))
                print("\n[Regra 1b — sumario colado na tabela (v7.1)]")
                print("   - texto visivel entre a tabela e o sumario: %d caracteres (limite: %d)"
                      % (n_miolo, LIMITE_TEXTO_TABELA_SUMARIO))
                if n_miolo > LIMITE_TEXTO_TABELA_SUMARIO:
                    erros.append(
                        "Ha %d caracteres de texto entre a tabela e o sumario (limite: %d). Na v7.1 o "
                        "sumario vem colado na tabela — formulario, faixa navy, selos, analise e imagem "
                        "ficam DEPOIS dele." % (n_miolo, LIMITE_TEXTO_TABELA_SUMARIO)
                    )
                if RE_COTACAO1.search(miolo):
                    erros.append(
                        'O formulario id="cotacao-1" esta ENTRE a tabela e o sumario. Na v7.1 ele abre a '
                        "segunda metade da secao de preco, DEPOIS do sumario."
                    )
                if tipo in ("city", "pillar"):
                    for fig in RE_FIGURE.finditer(miolo):
                        if "tabela" in normalize(fig.group(0)):
                            erros.append(
                                "A <figure> da imagem da tabela esta entre a tabela e o sumario. Na v7.1 "
                                "ela e o ULTIMO elemento da secao de preco."
                            )
                            break
        else:
            avisos.append("Sumario (toc-list) nao encontrado — conferir se o artigo deveria ter um.")

    # duplicacao de tabela
    achados = [m.group(0).lower() for m in RE_SHORTCODE_TABELA.finditer(html)]
    for sc in set(achados):
        if achados.count(sc) > 1:
            erros.append("Shortcode de tabela duplicado (%dx): %s" % (achados.count(sc), sc))
    if tipo == "tr" and achados:
        avisos.append("Artigo TR com shortcode de tabela completa (%s) — a v6 proibe: em TR a tabela e IMAGEM." % achados[0])

    # ---- Regra 2: H2 de preco na frente ---------------------------------
    print("\n[Regra 2 — H2 de preco na frente]")
    if precos:
        primeiro_preco = precos[0][0]
        atrasados = [(p, t) for p, t in outros if p < primeiro_preco]
        if atrasados:
            for p, t in atrasados:
                erros.append('H2 nao-preco antes do primeiro H2 de preco: "%s"' % t[:70])
        else:
            print("   - ok: o primeiro H2 de conteudo e de preco (\"%s\")" % precos[0][1][:60])
        # H2 de preco orfao la embaixo
        if len(precos) > 1 and outros:
            primeiro_outro = outros[0][0]
            orfaos = [(p, t) for p, t in precos[1:] if p > primeiro_outro]
            for p, t in orfaos:
                avisos.append('H2 de preco fora do bloco do topo: "%s"' % t[:70])
    else:
        if tipo == "hospital":
            print("   - sem H2 de preco; tipo hospital: ok")
        else:
            erros.append("Nenhum H2 de preco encontrado — a v7 exige a secao de preco em primeiro lugar.")

    # ---- formulario pos-sumario [v7.1] -----------------------------------
    m_cot = RE_COTACAO1.search(html)
    print("\n[Formulario — v7.1: depois do sumario]")
    if m_cot and pos_toc is not None:
        if m_cot.start() < pos_toc:
            print("   - id=\"cotacao-1\" ANTES do sumario (ver erro acima)")
        else:
            print("   - ok: id=\"cotacao-1\" depois do sumario, a %.0f%% do arquivo"
                  % (100.0 * m_cot.start() / total))
    elif not m_cot:
        avisos.append('id="cotacao-1" nao encontrado — o 1o formulario abre a secao pos-sumario.')

    # ---- veredito --------------------------------------------------------
    print("\n" + "-" * 72)
    for n in notas:
        print("   NOTA: %s" % n)
    for a in avisos:
        print("   AVISO (nao bloqueia, mas explique a decisao): %s" % a)
    for e in erros:
        print("   ERRO: %s" % e)
    print("-" * 72)
    if erros:
        print("\n❌ REPROVADO — %d erro(s), %d aviso(s)." % (len(erros), len(avisos)))
        sys.exit(1)
    print("\n✅ APROVADO — ordem preco-primeiro respeitada (%d aviso(s))." % len(avisos))
    sys.exit(0)


if __name__ == "__main__":
    main()
