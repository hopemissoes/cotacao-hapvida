# -*- coding: utf-8 -*-
"""
checkpoint_voz.py — trava mecânica da VOZ HUMANA [V6]
(hapvida-article-builder-v7)

Caça os tiques que denunciam texto de IA **em português**. A lista famosa que
circula por aí é em inglês (delve/leverage/robust); traduzir aquilo não pega o
tique nº 1 do português, que é o GERÚNDIO DE ARREMATE
("...na cidade, garantindo mais segurança para a família").

Regra-mãe: mexe em palavra e ritmo, NUNCA em fato. Ver references/voz-humana.md.

Duas severidades, de propósito:
  🔴 REPROVA — tique sem defesa razoável (arremate, tríade, "não apenas...mas
     também", abertura/fecho de piloto automático, marketing genérico)
  🟡 AVISA   — densidade que o editor julga (travessão, conectores batidos,
     palavras infladas, frases todas do mesmo tamanho)

Uso:
  python -X utf8 checkpoint_voz.py artigo.html
  python -X utf8 checkpoint_voz.py artigo.html --rigor alto    # 🟡 passa a reprovar
  python -X utf8 checkpoint_voz.py artigo.html --rigor baixo   # só relatório, nunca reprova

Ignora <style>, <script>, comentários HTML, shortcodes [...] e o miolo de
<table> (não faz sentido caçar estilo em número).

Saída: relatório + "✅ APROVADO" ou "❌ REPROVADO" (exit code 1).
"""
import argparse
import html as htmlmod
import re
import statistics
import sys

# ---------------------------------------------------------------- normalização

# Mapa que tira acento SEM mudar o comprimento da string, para os índices do
# regex continuarem valendo no texto original (NFD mudaria o tamanho).
ACENTOS = str.maketrans(
    "áàâãäéèêëíìîïóòôõöúùûüçñÁÀÂÃÄÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÛÜÇÑ",
    "aaaaaeeeeiiiiooooouuuucnAAAAAEEEEIIIIOOOOOUUUUCN",
)


def sem_acento(texto):
    return texto.translate(ACENTOS)


def extrair_texto(bruto):
    """HTML → texto visível, já sem style/script/comentário/shortcode/tabela."""
    t = bruto
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    t = re.sub(r"<style\b.*?</style>", " ", t, flags=re.S | re.I)
    t = re.sub(r"<script\b.*?</script>", " ", t, flags=re.S | re.I)
    t = re.sub(r"<table\b.*?</table>", " ", t, flags=re.S | re.I)
    t = re.sub(r"\[[^\]\n]{1,120}\]", " ", t)          # shortcodes do WordPress
    t = re.sub(r"</(p|div|li|h[1-6]|figcaption|blockquote)>", "\n\n", t, flags=re.I)
    t = re.sub(r"<br\s*/?>", "\n", t, flags=re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    t = htmlmod.unescape(t)
    t = re.sub(r"[ \t ]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


# ---------------------------------------------------------------- 🔴 detectores

GERUNDIOS_ARREMATE = (
    "garantindo|proporcionando|oferecendo|trazendo|permitindo|possibilitando|"
    "assegurando|facilitando|contribuindo|gerando|promovendo|ampliando|"
    "reduzindo|evitando|tornando|agilizando|otimizando"
)
RE_ARREMATE = re.compile(r",\s+(" + GERUNDIOS_ARREMATE + r")\b", re.I)

ADJ_VITRINE = {
    "pratico", "pratica", "rapido", "rapida", "eficiente", "completo", "completa",
    "amplo", "ampla", "seguro", "segura", "moderno", "moderna", "acessivel",
    "humanizado", "humanizada", "qualificado", "qualificada", "simples", "facil",
    "agil", "claro", "clara", "transparente", "economico", "economica",
    "personalizado", "personalizada", "exclusivo", "exclusiva", "ideal",
    "excelente", "robusto", "robusta", "diferenciado", "diferenciada",
    "fundamental", "primordial", "crucial", "imprescindivel", "essencial",
    "confiavel", "acolhedor", "acolhedora", "inovador", "inovadora",
    "abrangente", "vantajoso", "vantajosa", "tranquilo", "tranquila",
}
# tríade: "X, Y e Z" — só marca quando pelo menos 2 dos 3 são adjetivo de vitrine
# (senão pegaria lista de fato, tipo "hospitais, clínicas e laboratórios")
RE_TRIADE = re.compile(r"\b([a-zA-ZÀ-ÿ]{4,}),\s+([a-zA-ZÀ-ÿ]{4,})\s+e\s+([a-zA-ZÀ-ÿ]{4,})\b")

MOLDES_VERMELHOS = [
    (r"\bnao apenas\b[^.!?]{0,80}\bmas tambem\b", "molde \"não apenas… mas também\""),
    (r"\bseja voce\b[^.!?]{0,60}\bou\b", "molde \"seja você A, B ou C\""),
    (r"\bmais do que (um|uma)\b[^.!?]{0,40}\b(e|sao)\b", "slogan \"mais do que X, é Y\""),
    (r"\bneste artigo,? voce (vai|ira)\b", "abertura \"neste artigo você vai…\""),
    (r"\bse voce (esta|estiver) (procurando|buscando|em busca)", "abertura \"se você está procurando…\""),
    (r"\bquando o assunto e\b", "abertura \"quando o assunto é…\""),
    (r"\bcontinue a leitura\b|\bboa leitura\b|\bacompanhe a seguir\b", "chamada de enchimento"),
    (r"\bagora que voce ja sabe\b", "fecho \"agora que você já sabe…\""),
    (r"\be ai que entra\b", "ponte de anúncio \"é aí que entra…\""),
    (r"\ba resposta e simples\b", "\"a resposta é simples\""),
    (r"\bvamos entender melhor\b|\bvamos ao que interessa\b", "falso convite"),
]

MARKETING_GENERICO = [
    (r"\bexcelente custo[- ]beneficio\b", "\"excelente custo-benefício\""),
    (r"\btranquilidade para voce e sua familia\b", "\"tranquilidade para você e sua família\""),
    (r"\bo melhor plano para voce\b", "\"o melhor plano para você\""),
    (r"\bqualidade de vida\b", "\"qualidade de vida\" (vago)"),
    (r"\bcobertura total\b|\bcuidado completo\b", "promessa de cobertura total (contraria a ANS)"),
    (r"\batendimento humanizado\b", "\"atendimento humanizado\" (só com fonte citada)"),
]

# ---------------------------------------------------------------- 🟡 detectores

CONECTORES_ABERTURA = [
    "alem disso", "ademais", "outrossim", "nesse sentido", "nesse contexto",
    "diante disso", "dessa forma", "desse modo", "sendo assim", "por outro lado",
    "em suma", "em resumo", "por fim", "vale ressaltar", "vale destacar",
    "vale lembrar", "e importante ressaltar", "e importante destacar",
    "cabe destacar", "e valido lembrar", "portanto", "assim sendo",
]

PALAVRAS_INFLADAS = [
    "proporcionar", "proporciona", "possibilitar", "possibilita", "viabilizar",
    "contemplar", "contempla", "abranger", "abrange", "dispor de", "usufruir",
    "efetuar", "otimizar", "potencializar", "alavancar", "visando",
    "no que tange", "no que diz respeito", "a fim de", "bem como", "supracitado",
]


def acha(padrao, texto_norm, flags=re.I):
    return [m for m in re.finditer(padrao, texto_norm, flags)]


def trecho(original, pos, raio=52):
    ini = max(0, pos - raio)
    fim = min(len(original), pos + raio)
    s = original[ini:fim].replace("\n", " ")
    return ("…" if ini else "") + s.strip() + ("…" if fim < len(original) else "")


def main(argv=None):
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("arquivo")
    ap.add_argument("--rigor", choices=["baixo", "medio", "alto"], default="medio")
    args = ap.parse_args(argv)

    with open(args.arquivo, encoding="utf-8") as fh:
        bruto = fh.read()

    texto = extrair_texto(bruto)
    norm = sem_acento(texto).lower()
    palavras = re.findall(r"[A-Za-zÀ-ÿ0-9]+", texto)
    n_pal = len(palavras) or 1
    por_mil = lambda n: n * 1000.0 / n_pal

    paragrafos = [p.strip() for p in texto.split("\n\n") if len(p.strip()) > 40]
    frases = [f.strip() for f in re.split(r"(?<=[.!?])\s+", texto) if len(f.strip()) > 20]

    vermelhos = []   # (rótulo, [trechos])
    amarelos = []

    # ---- 🔴 gerúndio de arremate (com orçamento: 1 a cada 1500 palavras)
    ms = RE_ARREMATE.finditer(norm)
    hits = [trecho(texto, m.start()) for m in ms]
    orcamento = max(1, n_pal // 1500)
    if len(hits) > orcamento:
        vermelhos.append(
            ("gerúndio de arremate: %d ocorrência(s), orçamento %d" % (len(hits), orcamento), hits[:6])
        )
    elif hits:
        amarelos.append(("gerúndio de arremate dentro do orçamento (%d de %d)" % (len(hits), orcamento), hits[:3]))

    # ---- 🔴 tríades de adjetivo
    tri = []
    for m in RE_TRIADE.finditer(texto):
        grupo = [sem_acento(g).lower() for g in m.groups()]
        if sum(1 for g in grupo if g in ADJ_VITRINE) >= 2:
            tri.append(trecho(texto, m.start()))
    if tri:
        vermelhos.append(("tríade de adjetivos: %d" % len(tri), tri[:6]))

    # ---- 🔴 moldes
    for padrao, rotulo in MOLDES_VERMELHOS:
        hs = acha(padrao, norm)
        if hs:
            vermelhos.append(("%s: %d" % (rotulo, len(hs)), [trecho(texto, m.start()) for m in hs[:4]]))

    # ---- 🔴 marketing genérico
    for padrao, rotulo in MARKETING_GENERICO:
        hs = acha(padrao, norm)
        if hs:
            vermelhos.append(("marketing genérico %s: %d" % (rotulo, len(hs)),
                              [trecho(texto, m.start()) for m in hs[:4]]))

    # ---- 🟡 travessão
    n_trav = texto.count("—")
    # piso absoluto: em trecho curto, 1 travessão já estoura a taxa por mil sem
    # significar nada. Só avisa quando há volume real.
    if n_trav >= 4 and por_mil(n_trav) > 2.0:
        amarelos.append(("travessão: %d (%.1f por 1.000 palavras; alvo ≤ 2)" % (n_trav, por_mil(n_trav)), []))

    # ---- 🟡 conectores abrindo parágrafo
    aberturas = []
    for p in paragrafos:
        cab = sem_acento(p[:40]).lower()
        for c in CONECTORES_ABERTURA:
            if cab.startswith(c):
                aberturas.append(p[:60].replace("\n", " ") + "…")
                break
    if paragrafos and len(aberturas) > max(1, len(paragrafos) // 4):
        amarelos.append(("conector batido abrindo parágrafo: %d de %d parágrafos"
                         % (len(aberturas), len(paragrafos)), aberturas[:6]))

    # ---- 🟡 palavras infladas
    inflada_hits = []
    for w in PALAVRAS_INFLADAS:
        for m in acha(r"\b" + w + r"\b", norm):
            inflada_hits.append((w, trecho(texto, m.start())))
    if por_mil(len(inflada_hits)) > 3.0:
        amarelos.append(("palavras infladas: %d (%.1f por 1.000 palavras; alvo ≤ 3)"
                         % (len(inflada_hits), por_mil(len(inflada_hits))),
                         ["%s → %s" % (w, t) for w, t in inflada_hits[:6]]))

    # ---- 🟡 ritmo (frases todas do mesmo tamanho)
    if len(frases) >= 20:   # abaixo disso a estatística é ruído, não ritmo
        tam = [len(re.findall(r"[A-Za-zÀ-ÿ0-9]+", f)) for f in frases]
        media = statistics.mean(tam)
        desvio = statistics.pstdev(tam)
        if media and desvio / media < 0.35:
            amarelos.append(("ritmo metronômico: frases com %.0f palavras em média e "
                             "variação de só %.0f%% (alvo ≥ 35%%)" % (media, 100 * desvio / media), []))

    # ------------------------------------------------------------- relatório
    print("=" * 68)
    print("CHECKPOINT DE VOZ HUMANA [V6] — %s" % args.arquivo)
    print("%d palavras · %d parágrafos · %d frases · rigor: %s"
          % (n_pal, len(paragrafos), len(frases), args.rigor))
    print("=" * 68)

    if vermelhos:
        print("\n🔴 TIQUES QUE REPROVAM\n")
        for rotulo, exemplos in vermelhos:
            print("  • %s" % rotulo)
            for e in exemplos:
                print("      %s" % e)
    else:
        print("\n🔴 nenhum tique bloqueante.")

    if amarelos:
        print("\n🟡 DENSIDADE — o editor decide\n")
        for rotulo, exemplos in amarelos:
            print("  • %s" % rotulo)
            for e in exemplos:
                print("      %s" % e)
    else:
        print("\n🟡 nenhum aviso de densidade.")

    print("\n" + "-" * 68)
    print("Lembrete da regra-mãe: mexer em palavra e ritmo, NUNCA em fato.")
    print("Se limpar o tique custar precisão, o tique fica e o editor anota o porquê.")
    print("-" * 68)

    if args.rigor == "baixo":
        print("\n✅ APROVADO (rigor baixo: relatório apenas, nunca reprova)")
        return 0

    reprova = bool(vermelhos) or (args.rigor == "alto" and bool(amarelos))
    if reprova:
        print("\n❌ REPROVADO — corrigir os itens acima e rodar de novo.")
        return 1
    print("\n✅ APROVADO")
    return 0


if __name__ == "__main__":
    sys.exit(main())
