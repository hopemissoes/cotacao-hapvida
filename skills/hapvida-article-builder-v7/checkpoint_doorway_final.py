# -*- coding: utf-8 -*-
"""
checkpoint_doorway_final.py — VARREDURA FINAL ANTI-DOORWAY [V7.2]
(hapvida-article-builder-v7)

E' a ULTIMA chamada antes de publicar. Roda depois do editor-chefe, das
auditorias, do painel de juizes e do portao humano — quando o artigo ja esta
"pronto". Existe porque doorway nao aparece no paragrafo: aparece no CONJUNTO,
e o conjunto so existe no fim.

Quatro medidas, todas mecanicas:

  D1. TESTE DE SUBSTITUICAO — quanto do texto visivel continua valido depois de
      apagar a cidade e as ancoras locais. Paragrafo sem NENHUMA ancora local e'
      paragrafo que serve para qualquer cidade.
  D2. SECAO SEM ANCORA — qualquer <section>/H2 do corpo sem uma unica ancora
      local e' uma secao inteira reaproveitavel: doorway estrutural.
  D3. CLICHE DE OPERADORA E CLICHE REGULATORIO — o "cacador de cliche" do
      Agente 13, mecanizado (verticalizacao, rede propria, custo competitivo,
      atendimento de qualidade, "como qualquer plano regulado pela ANS"...).
  D4. SOBREPOSICAO COM OS ARTIGOS IRMAOS — shingles de 8 palavras contra os
      outros artigos do site que forem passados em --outros. Mede repeticao
      real, nao impressao.

  + TITULO E META no teste de substituicao (regra da v5).

Uso:
  python -X utf8 checkpoint_doorway_final.py <artigo.html> --cidade "Piracicaba"
         [--ancoras ancoras.txt] [--outros a.html b.html pasta/]
         [--tipo city|pillar|tr|hospital] [--titulo "..."] [--meta "..."]

O arquivo --ancoras tem uma ancora por linha (bairros, hospitais, unidades,
avenidas, entidades locais) — normalmente sai da secao de rede do state file.
Sem ele, o script ainda acha ancoras por padrao textual (Hospital X, Bairro Y),
mas com menos precisao: PASSE O ARQUIVO em artigo de city.

Saida: relatorio + "✅ APROVADO" ou "❌ REPROVADO" (exit code 1).
Só biblioteca padrão.

O que NAO faz: nao consulta o banco (isso e' do Agente 21, via MCP), nao julga
qualidade, nao reescreve. Ele mede repeticao e ausencia de ancora — o resto e'
julgamento humano/agente.
"""
import argparse
import html as htmlmod
import os
import re
import sys
import unicodedata

# --------------------------------------------------------------- limiares

LIM_GENERICO_AMARELO = 30.0   # % do texto visivel em paragrafos sem ancora
LIM_GENERICO_VERMELHO = 45.0
LIM_OVERLAP_AMARELO = 8.0     # % de shingles compartilhados com um irmao
LIM_OVERLAP_VERMELHO = 15.0
LIM_TRECHO_LITERAL = 40       # palavras seguidas identicas = colagem
SHINGLE = 8
MIN_PALAVRAS_PARAGRAFO = 12   # abaixo disso nao julga (legenda, rotulo)

# --------------------------------------------------------------- vocabulario

CLICHES = [
    ("modelo verticalizado", "discurso institucional da operadora"),
    ("rede propria sempre que possivel", "discurso institucional"),
    ("atendimento de qualidade", "promessa generica"),
    ("qualidade no atendimento", "promessa generica"),
    ("custo competitivo", "promessa generica"),
    ("mensalidades mais baixas do mercado", "promessa generica"),
    ("melhor custo-beneficio", "promessa generica"),
    ("pensando em voce", "marketing vazio"),
    ("cuidar de quem voce ama", "marketing vazio"),
    ("como qualquer plano regulado pela ans", "cliche regulatorio"),
    ("de acordo com as normas da ans", "cliche regulatorio"),
    ("a coparticipacao e um valor cobrado por uso", "cliche regulatorio"),
    ("os reajustes seguem as regras da ans", "cliche regulatorio"),
    ("um dos maiores planos de saude do brasil", "cliche institucional"),
    ("presente em todo o territorio nacional", "cliche institucional"),
    ("solucoes completas em saude", "cliche institucional"),
]

# Marcadores que denunciam entidade local nomeada (mesmo sem lista de ancoras)
MARCADORES_ENTIDADE = [
    "hospital", "hospitais", "clinica", "clinicas", "policlinica", "policlinicas",
    "pronto atendimento", "pronto-socorro", "upa", "unidade", "unidades",
    "bairro", "bairros", "avenida", "avenidas", "rua", "rodovia", "distrito",
    "jardim", "vila", "centro medico", "laboratorio", "maternidade",
    "regiao metropolitana", "zona norte", "zona sul", "zona leste", "zona oeste",
]

RE_TAG = re.compile(r"<[^>]+>")
RE_SHORTCODE = re.compile(r"\[[^\]\n]{1,120}\]")
RE_BLOCOS_FORA = re.compile(
    r"<(script|style|noscript)\b.*?</\1>|<!--.*?-->", re.IGNORECASE | re.DOTALL)
RE_PARAGRAFO = re.compile(r"<(p|li|h[23]|figcaption)\b[^>]*>(.*?)</\1>",
                          re.IGNORECASE | re.DOTALL)
RE_SECTION = re.compile(r"<section\b[^>]*>(.*?)</section>", re.IGNORECASE | re.DOTALL)
RE_H2 = re.compile(r"<h2\b[^>]*>(.*?)</h2>", re.IGNORECASE | re.DOTALL)
RE_TITLE = re.compile(r"<title\b[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)
RE_META = re.compile(
    r"<meta\b[^>]*name=[\"']description[\"'][^>]*content=[\"'](.*?)[\"']",
    re.IGNORECASE | re.DOTALL)


# --------------------------------------------------------------- utilidades

def sem_acento(txt):
    txt = unicodedata.normalize("NFD", txt or "")
    return "".join(c for c in txt if unicodedata.category(c) != "Mn")


def limpar(txt):
    """HTML -> texto visivel normalizado (minusculo, sem acento, sem shortcode)."""
    txt = RE_BLOCOS_FORA.sub(" ", txt or "")
    txt = RE_TAG.sub(" ", txt)
    txt = htmlmod.unescape(txt)
    txt = RE_SHORTCODE.sub(" ", txt)
    txt = sem_acento(txt).lower()
    txt = re.sub(r"[^a-z0-9%\s-]", " ", txt)
    return re.sub(r"\s+", " ", txt).strip()


def palavras(txt):
    return [p for p in limpar(txt).split() if p]


def shingles(lista, k=SHINGLE):
    return {" ".join(lista[i:i + k]) for i in range(len(lista) - k + 1)}


def variantes_cidade(cidade):
    """Piracicaba -> {piracicaba}; Belo Horizonte -> {belo horizonte, bh}."""
    base = sem_acento(cidade or "").lower().strip()
    out = {base} if base else set()
    partes = [p for p in base.split() if len(p) > 2 and p not in ("de", "do", "da", "dos", "das")]
    for p in partes:
        out.add(p)
    if len(partes) > 1:
        out.add("".join(p[0] for p in partes))
    return {o for o in out if o}


# --------------------------------------------------------------- ancoras

def carregar_ancoras(caminho):
    if not caminho:
        return []
    with open(caminho, "r", encoding="utf-8", errors="replace") as fh:
        linhas = [sem_acento(l).lower().strip() for l in fh]
    return [l for l in linhas if l and not l.startswith("#") and len(l) > 3]


def ancoras_no_texto(texto_norm, variantes, ancoras, texto_cru):
    """Devolve a lista de ancoras locais encontradas no trecho."""
    achadas = []
    for v in variantes:
        if v and v in texto_norm:
            achadas.append("cidade:%s" % v)
    for a in ancoras:
        if a in texto_norm:
            achadas.append("ancora:%s" % a)
    # entidade nomeada: marcador seguido de nome proprio no texto CRU
    for marcador in MARCADORES_ENTIDADE:
        padrao = re.compile(
            r"\b%s\b\s+(?:de\s+|do\s+|da\s+)?([A-ZÁÂÃÉÊÍÓÔÕÚÜÇ][\wÁÂÃÉÊÍÓÔÕÚÜÇáâãéêíóôõúüç]{2,})"
            % re.escape(marcador.split()[0]))
        m = padrao.search(texto_cru)
        if m:
            achadas.append("entidade:%s %s" % (marcador.split()[0], m.group(1)))
    return achadas


# --------------------------------------------------------------- medidas

def extrair_paragrafos(html):
    corpo = RE_BLOCOS_FORA.sub(" ", html)
    for m in RE_PARAGRAFO.finditer(corpo):
        cru = m.group(2)
        yield m.group(1).lower(), cru


def medir_genericos(html, variantes, ancoras):
    total_palavras = 0
    genericos = []
    gen_palavras = 0
    for tag, cru in extrair_paragrafos(html):
        pals = palavras(cru)
        if len(pals) < MIN_PALAVRAS_PARAGRAFO:
            continue
        total_palavras += len(pals)
        norm = " ".join(pals)
        if not ancoras_no_texto(norm, variantes, ancoras, cru):
            gen_palavras += len(pals)
            genericos.append((tag, " ".join(pals[:18])))
    pct = (100.0 * gen_palavras / total_palavras) if total_palavras else 0.0
    return pct, genericos, total_palavras


def medir_secoes(html, variantes, ancoras):
    """Secao (ou bloco de H2) sem nenhuma ancora local."""
    secoes = []
    blocos = RE_SECTION.findall(html)
    if not blocos:
        partes = re.split(r"(?=<h2\b)", html, flags=re.IGNORECASE)
        blocos = [p for p in partes if re.search(r"<h2\b", p, re.IGNORECASE)]
    for bloco in blocos:
        h2 = RE_H2.search(bloco)
        titulo = limpar(h2.group(1))[:70] if h2 else "(sem h2)"
        pals = palavras(bloco)
        if len(pals) < 40:
            continue
        norm = " ".join(pals)
        if not ancoras_no_texto(norm, variantes, ancoras, bloco):
            secoes.append(titulo)
    return secoes


def medir_cliches(html):
    achados = []
    for tag, cru in extrair_paragrafos(html):
        norm = " ".join(palavras(cru))
        for frase, motivo in CLICHES:
            if frase in norm:
                paragrafo_inteiro = len(norm.split()) <= 45
                achados.append((frase, motivo, paragrafo_inteiro,
                                " ".join(norm.split()[:16])))
    return achados


def medir_overlap(html, outros, variantes):
    """Shingles compartilhados com cada artigo irmao, ignorando a cidade."""
    pals = [p for p in palavras(html) if p not in variantes]
    base = shingles(pals)
    resultados = []
    if not base:
        return resultados
    for caminho in outros:
        try:
            with open(caminho, "r", encoding="utf-8", errors="replace") as fh:
                outro_html = fh.read()
        except OSError as exc:
            resultados.append((caminho, None, 0, "nao consegui ler: %s" % exc))
            continue
        pals_outro = [p for p in palavras(outro_html) if p not in variantes]
        comuns = base & shingles(pals_outro)
        pct = 100.0 * len(comuns) / len(base)
        maior = maior_trecho_comum(pals, pals_outro)
        resultados.append((caminho, pct, maior, None))
    return resultados


def maior_trecho_comum(a, b):
    """Maior sequencia identica de palavras (limitada, para nao explodir)."""
    if not a or not b:
        return 0
    setb = shingles(b, SHINGLE)
    melhor = 0
    i = 0
    while i <= len(a) - SHINGLE:
        if " ".join(a[i:i + SHINGLE]) in setb:
            j = i + SHINGLE
            while j < len(a) and " ".join(a[j - SHINGLE + 1:j + 1]) in setb:
                j += 1
            melhor = max(melhor, j - i)
            i = j
        else:
            i += 1
    return melhor


def medir_titulo_meta(html, variantes, titulo_arg, meta_arg):
    problemas = []
    titulo = titulo_arg
    if not titulo:
        m = RE_TITLE.search(html)
        titulo = m.group(1) if m else ""
    meta = meta_arg
    if not meta:
        m = RE_META.search(html)
        meta = m.group(1) if m else ""
    for rotulo, texto in (("title", titulo), ("meta description", meta)):
        if not texto:
            problemas.append((rotulo, "ausente", None))
            continue
        norm = " ".join(palavras(texto))
        if not any(v in norm for v in variantes):
            problemas.append((rotulo, "nao cita a cidade — serve para qualquer praca",
                              texto.strip()[:110]))
    return problemas


# --------------------------------------------------------------- main

def expandir_outros(itens):
    saida = []
    for item in itens or []:
        if os.path.isdir(item):
            for nome in sorted(os.listdir(item)):
                if nome.lower().endswith((".html", ".htm")):
                    saida.append(os.path.join(item, nome))
        else:
            saida.append(item)
    return saida


def main():
    ap = argparse.ArgumentParser(add_help=True, description=__doc__)
    ap.add_argument("artigo")
    ap.add_argument("--cidade", default="")
    ap.add_argument("--ancoras", default="")
    ap.add_argument("--outros", nargs="*", default=[])
    ap.add_argument("--tipo", default="city",
                    choices=["city", "pillar", "tr", "hospital"])
    ap.add_argument("--titulo", default="")
    ap.add_argument("--meta", default="")
    args = ap.parse_args()

    try:
        with open(args.artigo, "r", encoding="utf-8", errors="replace") as fh:
            html = fh.read()
    except OSError as exc:
        print("nao consegui ler o artigo: %s" % exc)
        return 2

    geo = args.tipo in ("city", "tr", "hospital")
    # Em pillar o eixo de substituicao nao e' a praca, e' o PRODUTO (Nosso Plano,
    # Mix, Individual...). Passe-o em --cidade para o teste valer como bloqueio;
    # sem ele, D1/D2 viram aviso — reprovar por falta de ancora geografica num
    # artigo nacional seria falso positivo.
    pillar_sem_eixo = (args.tipo == "pillar" and not args.cidade)
    if geo and not args.cidade:
        print("❌ REPROVADO — em artigo %s o parametro --cidade e' obrigatorio "
              "(o teste de substituicao depende dele)." % args.tipo)
        return 1

    variantes = variantes_cidade(args.cidade)
    ancoras = carregar_ancoras(args.ancoras)
    outros = expandir_outros(args.outros)

    erros, avisos = [], []

    print("=" * 70)
    print("VARREDURA FINAL ANTI-DOORWAY [V7.2] — %s" % args.artigo)
    print("tipo: %s | cidade: %s | ancoras carregadas: %d | irmaos: %d"
          % (args.tipo, args.cidade or "-", len(ancoras), len(outros)))
    print("=" * 70)

    # D1 — teste de substituicao
    pct, genericos, total = medir_genericos(html, variantes, ancoras)
    print("\nD1 · TESTE DE SUBSTITUICAO")
    print("   texto visivel julgado: %d palavras" % total)
    print("   em paragrafos SEM ancora local: %.1f%%" % pct)
    if pillar_sem_eixo:
        print("   (pillar sem --cidade/eixo: D1 e D2 rodam como AVISO — passe o nome")
        print("    do produto em --cidade para que valham como bloqueio)")
    if pct >= LIM_GENERICO_VERMELHO and not pillar_sem_eixo:
        erros.append("D1 %.1f%% do texto sobrevive a troca de cidade/eixo (limite %.0f%%)"
                     % (pct, LIM_GENERICO_VERMELHO))
    elif pct >= LIM_GENERICO_AMARELO or (pillar_sem_eixo and pct >= LIM_GENERICO_VERMELHO):
        avisos.append("D1 %.1f%% do texto sem ancora local (alerta a partir de %.0f%%)"
                      % (pct, LIM_GENERICO_AMARELO))
    for tag, trecho in genericos[:8]:
        print("   - <%s> %s..." % (tag, trecho))
    if len(genericos) > 8:
        print("   (+%d paragrafos genericos)" % (len(genericos) - 8))

    # D2 — secao sem ancora
    secoes = medir_secoes(html, variantes, ancoras)
    print("\nD2 · SECAO SEM ANCORA LOCAL")
    if secoes:
        for s in secoes:
            print("   - %s" % s)
        destino = avisos if pillar_sem_eixo else erros
        destino.append("D2 %d secao(oes) inteira(s) sem uma unica ancora local: %s"
                       % (len(secoes), "; ".join(secoes[:3])))
    else:
        print("   nenhuma — toda secao tem ancora local")

    # D3 — cliche
    cliches = medir_cliches(html)
    print("\nD3 · CLICHE DE OPERADORA / REGULATORIO")
    if cliches:
        for frase, motivo, inteiro, trecho in cliches[:10]:
            print("   - \"%s\" (%s)%s" % (frase, motivo,
                                          " [paragrafo inteiro]" if inteiro else ""))
        inteiros = [c for c in cliches if c[2]]
        if inteiros:
            erros.append("D3 %d cliche(s) ocupando paragrafo inteiro" % len(inteiros))
        elif len(cliches) > 5:
            erros.append("D3 %d ocorrencias de cliche institucional (limite 5)"
                         % len(cliches))
        else:
            avisos.append("D3 %d ocorrencia(s) de cliche institucional" % len(cliches))
    else:
        print("   nenhum da lista")

    # D4 — sobreposicao com irmaos
    print("\nD4 · SOBREPOSICAO COM ARTIGOS IRMAOS")
    if not outros:
        print("   nenhum irmao passado em --outros")
        avisos.append("D4 varredura rodou SEM comparar com artigos irmaos — "
                      "passe --outros com os artigos do mesmo cluster")
    for caminho, pct_o, maior, erro in medir_overlap(html, outros, variantes):
        nome = os.path.basename(caminho)
        if erro:
            print("   - %s: %s" % (nome, erro))
            avisos.append("D4 %s" % erro)
            continue
        print("   - %-38s %5.1f%% de shingles | maior trecho identico: %d palavras"
              % (nome[:38], pct_o, maior))
        if pct_o >= LIM_OVERLAP_VERMELHO:
            erros.append("D4 %.1f%% de sobreposicao com %s (limite %.0f%%)"
                         % (pct_o, nome, LIM_OVERLAP_VERMELHO))
        elif pct_o >= LIM_OVERLAP_AMARELO:
            avisos.append("D4 %.1f%% de sobreposicao com %s" % (pct_o, nome))
        if maior >= LIM_TRECHO_LITERAL:
            erros.append("D4 trecho literal de %d palavras identico a %s"
                         % (maior, nome))

    # Titulo e meta
    print("\nD5 · TITULO E META NO TESTE DE SUBSTITUICAO")
    if geo:
        problemas = medir_titulo_meta(html, variantes, args.titulo, args.meta)
        if problemas:
            for rotulo, motivo, amostra in problemas:
                print("   - %s: %s%s" % (rotulo, motivo,
                                         (" — \"%s\"" % amostra) if amostra else ""))
                if motivo == "ausente":
                    avisos.append("D5 %s ausente no HTML (passe --%s se ele vive fora)"
                                  % (rotulo, "titulo" if rotulo == "title" else "meta"))
                else:
                    erros.append("D5 %s serve para qualquer praca" % rotulo)
        else:
            print("   title e meta citam a cidade")
    else:
        print("   pulado (artigo nao-geografico)")

    # ------------------------------------------------------------ veredito
    print("\n" + "-" * 70)
    if avisos:
        print("🟡 AVISOS (%d)" % len(avisos))
        for a in avisos:
            print("   - %s" % a)
    if erros:
        print("\n🔴 BLOQUEIOS (%d)" % len(erros))
        for e in erros:
            print("   - %s" % e)
        print("\n❌ REPROVADO — o artigo nao passa na varredura final anti-doorway.")
        print("   Corrija e rode de novo. Nota de juiz nao compra secao sem ancora.")
        return 1

    print("\n✅ APROVADO — nenhuma medida de doorway estourou o limite.")
    print("   Lembrete: o script mede repeticao e ausencia de ancora. A consulta")
    print("   ao banco (overlaps, FAQs, saturacao) continua sendo do Agente 21.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
