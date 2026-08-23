#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
checkpoint_fase0.py — TRAVA MECÂNICA da FASE 0 (pesquisa) [reescrito na V7.2]

Uso:
    python -X utf8 checkpoint_fase0.py <PESQUISA_<slug>_COMPLETO.md> [city|tr|pillar|hospital]

REGRA INEGOCIÁVEL:
    É PROIBIDO escrever QUALQUER HTML de artigo se este script não imprimir 'APROVADO'.
    Pesquisa diagnóstica (serp_local/keyword_data avulsos, GSC, GA4) NÃO é a Fase 0.

O QUE MUDOU NA V7.2 (e por que):
    A versão anterior procurava PALAVRAS no arquivo — "volume", "rede", "diferenci".
    Um state file com o gabarito vazio (516 bytes, tudo em [X]) passava com APROVADO
    em todos os itens. A trava media vocabulário, não pesquisa.

    Esta versão CONTA DADO PREENCHIDO: unidades com endereço e fonte, FAQ, keywords
    secundárias com veto, fontes primárias distintas, dados de nível 1-2, e reprova
    gabarito não preenchido, `fonte:` vazia, coleta velha e ausência do bloco
    FORBIDDEN_TOKENS (sem o qual o checkpoint_verificar.py roda desarmado).

O QUE ELE CONTINUA NÃO FAZENDO:
    Não julga a QUALIDADE da pesquisa. Contar 15 FAQ não prova que são boas.
    O 'ok' explícito do usuário sobre o state file continua obrigatório.
"""
import os
import re
import sys
import unicodedata
from datetime import date, datetime

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ------------------------------------------------------------------ limiares

MIN_UNIDADES = {"city": 5, "hospital": 1, "tr": 0, "pillar": 0}
MIN_FAQ = {"city": 15, "hospital": 10, "tr": 8, "pillar": 15}
MIN_SECUNDARIAS = 6          # [V5] veto de intenção
MIN_FONTES_URL = 8           # URLs distintas no state file
MIN_DOMINIOS_PRIMARIOS = 3   # gov.br, ibge, datasus/cnes, hapvida, ans...
MIN_NIVEL_12 = 3             # [V6] defensibilidade
MIN_DADOS_UNICOS = 10        # anti-doorway 4.2
MIN_FANOUT = 5               # [V6]
MAX_PLACEHOLDERS = 3         # tolerância para molde citado em texto explicativo
IDADE_AMARELA_SERP = 90      # dias
IDADE_VERMELHA_SERP = 180
IDADE_VERMELHA_REDE = 180

DOMINIOS_PRIMARIOS = (
    "hapvida.com.br", "gndi.com.br", "clinipam.com.br", "ans.gov.br",
    "ibge.gov.br", "datasus.gov.br", "cnes.datasus.gov.br", "saude.gov.br",
    ".gov.br", "gov.br",
)
DOMINIOS_NAO_FONTE = (
    "reclameaqui", "consumidor.gov", "quora", "yahoo", "wikipedia",
    "blogspot", "medium.com", "pinterest", "facebook.com", "instagram.com",
)

MOLDES = [
    r"\[X\]", r"\[x\]", r"\[\.\.\.\]", r"\[fonte\]", r"\[OBRIGAT[ÓO]RIO\]",
    r"\[nome[^\]]*\]", r"\[ano\]", r"\[cidade\]", r"\[sim/n[ãa]o\]",
    r"\[PASSOU/FALHOU\]", r"\[APROVADO/REPROVADO\]", r"\[URL\]", r"\[H1\]",
    r"\[telefone\]", r"\[endere[çc]o[^\]]*\]", r"\[rua[^\]]*\]", r"\[keyword[^\]]*\]",
    r"\[quanto[^\]]*\]", r"\[o qu[êe][^\]]*\]", r"\[rascunho[^\]]*\]",
]

# Camada 0 — SEÇÕES que precisam existir (herdada da v7.1). Presença sozinha
# não prova nada (foi o buraco antigo), mas ausência prova que falta seção.
SECOES = [
    ("SERP real (serp_local)", [r"serp_local", r"\bSERP\b"]),
    ("Contexto local (IBGE/CNES)", [r"IBGE", r"CNES", r"popula[çc]", r"leitos", r"\bIDH\b"]),
    ("[V4] Desmontagem de concorrentes", [r"desmontagem", r"concorrente", r"matriz de cobertura"]),
    ("[V4] Ganho de informação / brechas", [r"ganho de informa", r"must-?match", r"brecha"]),
    ("[V5] Kit on-page (matriz de posicionamento)", [r"kit[_ ]on-?page", r"posicoes_principal", r"matriz de posicionamento"]),
    ("[V5] Formato de snippet registrado", [r"featured_snippet", r"formato de snippet", r"snippet"]),
    ("[V6] Defensibilidade do dado", [r"defensibilidade", r"dado propriet"]),
    ("[V7.2] Dado proprietário (Parte 7)", [r"dado_propriet", r"consultar_rede", r"cotador_fila"]),
    ("[V7.2] Não encontrado (Parte 8)", [r"nao_encontrado", r"n[ãa]o encontrado"]),
]

RE_URL = re.compile(r"https?://[^\s,)\"'\]]+", re.I)
RE_DATA = re.compile(r"coletado_em\s*:\s*(\d{4})-(\d{2})-(\d{2})", re.I)
RE_DATA_ROTULADA = re.compile(
    r"coletado_em\s*:\s*(\d{4}-\d{2}-\d{2})\s*(?:#\s*([a-zA-Zçãéí_\- ]+))?", re.I)


def sem_acento(t):
    t = unicodedata.normalize("NFD", t or "")
    return "".join(c for c in t if unicodedata.category(c) != "Mn")


def norm(t):
    return sem_acento(t or "").lower()


# ------------------------------------------------------------------ medidas

def contar_placeholders(txt):
    achados = []
    for molde in MOLDES:
        for m in re.finditer(molde, txt):
            trecho = txt[max(0, m.start() - 40):m.end() + 10].replace("\n", " ")
            if "[VERIFICAR" in trecho.upper():
                continue
            achados.append((m.group(0), trecho.strip()))
    return achados


def contar_fontes_vazias(txt):
    vazias = 0
    for m in re.finditer(r"^[ \t]*fonte[ \t]*:[ \t]*(.*)$", txt, re.I | re.M):
        valor = m.group(1).strip().strip('"').strip("'")
        if (not valor) or re.match(r"^\[.*\]$", valor) or norm(valor) in (
                "", "-", "n/a", "na", "tbd", "a definir", "obrigatorio"):
            vazias += 1
    return vazias


def contar_unidades(txt):
    """Unidade = bloco com endereço preenchido (rua/av/nº ou CEP)."""
    total = 0
    for m in re.finditer(r"^[ \t]*endere[çc]o[^:\n]*:[ \t]*(.*)$", txt, re.I | re.M):
        valor = m.group(1).strip().strip('"')
        if re.match(r"^\[", valor) or len(valor) < 8:
            continue
        total += 1
    return total


def contar_faq(txt):
    """Perguntas de FAQ = linhas terminadas em '?' com >= 5 palavras."""
    perguntas = set()
    for linha in txt.splitlines():
        l = linha.strip().strip('"').strip("'").strip("-").strip()
        if l.endswith("?") and len(l.split()) >= 5 and not l.startswith("#"):
            perguntas.add(norm(l))
    return len(perguntas)


def contar_secundarias(txt):
    qualificadas = len(re.findall(r"veredito\s*:\s*qualificada", txt, re.I))
    if qualificadas:
        return qualificadas
    bloco = re.search(r"secundarias\s*:(.*?)(\n\S|\Z)", txt, re.I | re.S)
    if not bloco:
        return 0
    return len([l for l in re.findall(r"kw\s*:\s*[\"']?([^\"'\n,}]+)", bloco.group(1))
                if not l.strip().startswith("[")])


def analisar_urls(txt):
    urls, dominios = set(), set()
    for m in RE_URL.finditer(txt):
        url = m.group(0).rstrip(".,;")
        urls.add(url.lower())
        host = url.split("//", 1)[-1].split("/", 1)[0].lower()
        dominios.add(host[4:] if host.startswith("www.") else host)
    primarios = {d for d in dominios if any(p in d for p in DOMINIOS_PRIMARIOS)}
    suspeitos = {d for d in dominios if any(p in d for p in DOMINIOS_NAO_FONTE)}
    return urls, dominios, primarios, suspeitos


def contar_nivel_12(txt):
    return len(re.findall(r"defensibilidade\s*:\s*\"?\s*[12]\b", txt, re.I))


def numero_de(txt, campo):
    m = re.search(campo + r"[^\n]*?(\d+)", txt, re.I)
    return int(m.group(1)) if m else None


def datas_de_coleta(txt):
    """Devolve [(data, rotulo)] — rótulo é o comentário após a data, se houver."""
    saida = []
    for m in RE_DATA_ROTULADA.finditer(txt):
        try:
            d = datetime.strptime(m.group(1), "%Y-%m-%d").date()
        except ValueError:
            continue
        saida.append((d, norm(m.group(2) or "")))
    return saida


def anti_doorway_ok(txt):
    """Aprovação tem de estar NA MESMA LINHA do rótulo — não em qualquer lugar."""
    aprovado = False
    reprovado = []
    for linha in txt.splitlines():
        n = norm(linha)
        if re.search(r"(anti-?doorway|geral)\s*:", n) or n.startswith("anti-doorway"):
            if "aprovad" in n and "reprovad" not in n:
                aprovado = True
            if "reprovad" in n:
                reprovado.append(linha.strip()[:80])
        elif re.search(r"(teste_substituicao|dados_unicos|frases_genericas)\s*:", n):
            if "reprovad" in n or "falhou" in n:
                reprovado.append(linha.strip()[:80])
    return aprovado, reprovado


def forbidden_tokens(txt):
    m = re.search(r"FORBIDDEN_TOKENS\s*:(.*?)(\n\s*\n|\n#|\Z)", txt, re.I | re.S)
    if not m:
        return None
    linhas = [l.strip("- ").strip() for l in m.group(1).splitlines() if l.strip()]
    return [l for l in linhas if l and not l.startswith("#")]


# ------------------------------------------------------------------ main

def main():
    if len(sys.argv) < 2:
        print("USO: python -X utf8 checkpoint_fase0.py <PESQUISA_<slug>_COMPLETO.md> [city|tr|pillar|hospital]")
        print("❌ REPROVADO — nenhum state file informado. PROIBIDO escrever HTML.")
        return 2

    path = sys.argv[1]
    tipo = (sys.argv[2].lower() if len(sys.argv) > 2 else "city")
    if tipo not in MIN_UNIDADES:
        print("tipo desconhecido '%s' — usando 'city'" % tipo)
        tipo = "city"

    if not os.path.isfile(path):
        print("❌ REPROVADO — o state file NÃO existe: %s" % path)
        print("   A FASE 0 não foi concluída. Pesquisa diagnóstica NÃO conta.")
        return 1

    txt = open(path, encoding="utf-8", errors="ignore").read()

    print("=" * 68)
    print("CHECKPOINT FASE 0 [V7.2] — %s (tipo: %s)" % (os.path.basename(path), tipo))
    print("=" * 68)

    erros, avisos = [], []

    # 0) seções presentes ---------------------------------------------------
    print("\n0 · SEÇÕES DO ROTEIRO")
    for nome, padroes in SECOES:
        ok = any(re.search(pat, txt, re.I) for pat in padroes)
        print("   [%s] %s" % ("OK   " if ok else "FALTA", nome))
        if not ok:
            erros.append("seção ausente no state file: %s" % nome)

    # 1) gabarito não preenchido -------------------------------------------
    placeholders = contar_placeholders(txt)
    print("\n1 · GABARITO PREENCHIDO")
    print("   marcadores de molde ainda no arquivo: %d (limite %d)"
          % (len(placeholders), MAX_PLACEHOLDERS))
    for marca, trecho in placeholders[:6]:
        print("   - %-14s … %s" % (marca, trecho[-60:]))
    if len(placeholders) > MAX_PLACEHOLDERS:
        erros.append("gabarito não preenchido: %d marcadores de molde (ex.: %s). "
                     "State file colado do template NÃO é pesquisa"
                     % (len(placeholders), ", ".join(sorted({p[0] for p in placeholders})[:5])))

    # 2) fonte por dado -----------------------------------------------------
    fontes_vazias = contar_fontes_vazias(txt)
    urls, dominios, primarios, suspeitos = analisar_urls(txt)
    print("\n2 · FONTE POR DADO")
    print("   campos 'fonte:' vazios ou em molde: %d" % fontes_vazias)
    print("   URLs distintas: %d | domínios: %d | primários: %d (%s)"
          % (len(urls), len(dominios), len(primarios),
             ", ".join(sorted(primarios)[:4]) or "-"))
    if fontes_vazias:
        erros.append("%d campo(s) 'fonte:' vazio(s) — regra 1 da Fase 0: dado sem "
                     "fonte vira [VERIFICAR] e não entra" % fontes_vazias)
    if len(urls) < MIN_FONTES_URL:
        erros.append("só %d URL(s) distinta(s) de fonte no state file (mín. %d) — "
                     "DR1 completo cita SERP, guia oficial, IBGE, CNES, ANS e "
                     "prefeitura, no mínimo" % (len(urls), MIN_FONTES_URL))
    if len(primarios) < MIN_DOMINIOS_PRIMARIOS:
        erros.append("só %d domínio(s) primário(s) (mín. %d: oficial Hapvida, "
                     "IBGE, CNES/DataSUS, ANS, prefeitura)"
                     % (len(primarios), MIN_DOMINIOS_PRIMARIOS))
    if suspeitos:
        avisos.append("fonte de agregador/rede social citada (%s) — regra 2: "
                      "no máximo pista, nunca fonte factual" % ", ".join(sorted(suspeitos)[:3]))

    # 3) volume de coleta ---------------------------------------------------
    unidades = contar_unidades(txt)
    faq = contar_faq(txt)
    secundarias = contar_secundarias(txt)
    nivel12 = contar_nivel_12(txt)
    fanout = len(re.findall(r"^[ \t]*-?[ \t]*pergunta[ \t]*:", txt, re.I | re.M))
    unicos = numero_de(txt, r"dados_unicos")
    print("\n3 · VOLUME DE COLETA (contado, não procurado)")
    print("   unidades com endereço preenchido: %d (mín. %d)"
          % (unidades, MIN_UNIDADES[tipo]))
    print("   perguntas de FAQ: %d (mín. %d)" % (faq, MIN_FAQ[tipo]))
    print("   secundárias qualificadas: %d (mín. %d)" % (secundarias, MIN_SECUNDARIAS))
    print("   dados de defensibilidade nível 1-2: %d (mín. %d)" % (nivel12, MIN_NIVEL_12))
    print("   sub-perguntas de fan-out: %d (mín. %d)" % (fanout, MIN_FANOUT))
    print("   dados únicos declarados: %s (mín. %d)"
          % (unicos if unicos is not None else "não declarado", MIN_DADOS_UNICOS))

    if unidades < MIN_UNIDADES[tipo]:
        erros.append("rede rasa: %d unidade(s) com endereço (mín. %d para %s)"
                     % (unidades, MIN_UNIDADES[tipo], tipo))
    if faq < MIN_FAQ[tipo]:
        erros.append("%d pergunta(s) de FAQ (mín. %d para %s)" % (faq, MIN_FAQ[tipo], tipo))
    if secundarias < MIN_SECUNDARIAS:
        erros.append("%d secundária(s) qualificada(s) (mín. %d, com veto de intenção)"
                     % (secundarias, MIN_SECUNDARIAS))
    if nivel12 < MIN_NIVEL_12:
        erros.append("%d dado(s) de nível 1-2 (mín. %d) — sem dado proprietário o "
                     "ganho do CI-2 não se sustenta" % (nivel12, MIN_NIVEL_12))
    if fanout < MIN_FANOUT:
        erros.append("%d sub-pergunta(s) de fan-out (mín. %d)" % (fanout, MIN_FANOUT))
    if unicos is None:
        erros.append("dados_unicos não declarado (anti-doorway 4.2)")
    elif unicos < MIN_DADOS_UNICOS:
        erros.append("%d dado(s) único(s) da praça (mín. %d)" % (unicos, MIN_DADOS_UNICOS))

    # 4) recência -----------------------------------------------------------
    print("\n4 · RECÊNCIA DA COLETA")
    datas = datas_de_coleta(txt)
    if not datas:
        erros.append("nenhum 'coletado_em: AAAA-MM-DD' no state file — sem data não "
                     "se sabe se a pesquisa é de hoje ou do ano passado (seção 11)")
        print("   nenhuma data de coleta declarada")
    else:
        hoje = date.today()
        for d, rotulo in sorted(datas):
            idade = (hoje - d).days
            marca = ""
            rede = "rede" in rotulo or "unidade" in rotulo
            if rede and idade > IDADE_VERMELHA_REDE:
                erros.append("coleta de REDE com %d dias (limite %d) — rede muda; "
                             "recoletar antes de escrever" % (idade, IDADE_VERMELHA_REDE))
                marca = " 🔴"
            elif idade > IDADE_VERMELHA_SERP:
                erros.append("coleta '%s' com %d dias (limite %d)"
                             % (rotulo or "sem rótulo", idade, IDADE_VERMELHA_SERP))
                marca = " 🔴"
            elif idade > IDADE_AMARELA_SERP:
                avisos.append("coleta '%s' com %d dias — SERP e volume envelhecem"
                              % (rotulo or "sem rótulo", idade))
                marca = " 🟡"
            print("   %s  %-22s %4d dias%s" % (d.isoformat(), rotulo or "-", idade, marca))

    # 5) anti-doorway -------------------------------------------------------
    aprovado, reprovado = anti_doorway_ok(txt)
    print("\n5 · ANTI-DOORWAY")
    print("   aprovação explícita na linha do rótulo: %s" % ("sim" if aprovado else "NÃO"))
    for r in reprovado[:4]:
        print("   - reprovação encontrada: %s" % r)
    if not aprovado:
        erros.append("anti-doorway não está APROVADO na própria linha do rótulo "
                     "(seção 4 do DR2)")
    if reprovado:
        erros.append("%d linha(s) do anti-doorway marcada(s) REPROVADO/FALHOU"
                     % len(reprovado))

    # 6) FORBIDDEN_TOKENS ---------------------------------------------------
    tokens = forbidden_tokens(txt)
    print("\n6 · SEÇÃO 9 — FORBIDDEN_TOKENS")
    if tokens is None:
        erros.append("sem bloco 'FORBIDDEN_TOKENS:' (seção 9) — sem ele o "
                     "checkpoint_verificar.py roda com a trava 3 DESARMADA")
        print("   ausente")
    elif not tokens:
        avisos.append("bloco FORBIDDEN_TOKENS presente mas vazio — se não há token "
                      "proibido, escreva 'nenhum' e diga por quê")
        print("   presente, vazio")
    else:
        print("   %d token(s) proibido(s): %s" % (len(tokens), ", ".join(tokens[:5])))

    # 7) itens [VERIFICAR] --------------------------------------------------
    n_verif = len(re.findall(r"\[VERIFICAR", txt, re.I))
    if n_verif:
        avisos.append("%d item(ns) [VERIFICAR] — NÃO podem entrar no artigo" % n_verif)

    # ------------------------------------------------------------ veredito
    print("\n" + "-" * 68)
    if avisos:
        print("🟡 AVISOS (%d)" % len(avisos))
        for a in avisos:
            print("   - %s" % a)
    if erros:
        print("\n🔴 BLOQUEIOS (%d)" % len(erros))
        for e in erros:
            print("   - %s" % e)
        print("\n❌ REPROVADO — PROIBIDO escrever HTML até o state file estar completo.")
        return 1

    print("\n✅ APROVADO — state file completo e preenchido.")
    print("   Atenção: APROVADO aqui = dado coletado e com fonte. NÃO é juízo de")
    print("   qualidade. O HTML ainda exige o 'ok' EXPLÍCITO do usuário.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
