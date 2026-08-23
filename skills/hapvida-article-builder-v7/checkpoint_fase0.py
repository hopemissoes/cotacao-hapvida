#!/usr/bin/env python3
"""
checkpoint_fase0.py — TRAVA MECÂNICA da FASE 0 (pesquisa) da hapvida-article-builder.

Uso:
    python -X utf8 checkpoint_fase0.py <caminho do PESQUISA_<slug>_COMPLETO.md>

REGRA INEGOCIÁVEL:
    É PROIBIDO escrever QUALQUER HTML de artigo se este script não imprimir 'APROVADO'.
    Pesquisa diagnóstica (serp_local/keyword_data/keyword_suggestions avulsos, GSC, GA4)
    NÃO é a Fase 0 e NÃO satisfaz esta trava. Só o state file completo conta.

O script verifica PROCESSO (o state file existe e tem todas as partes do DR1+DR2 e o
anti-doorway marcado APROVADO). Ele NÃO julga a qualidade da pesquisa — isso continua
exigindo o aval explícito do usuário. Mas ele torna impossível fingir que a Fase 0
aconteceu quando o artefato dela não existe.
"""
import sys
# Blindagem UTF-8: console Windows (cp1252) quebra com emoji sem isto
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
import os
import re

# (nome legível, lista de padrões — basta um casar)
REQUISITOS = [
    ("SERP real (serp_local, mobile+desktop)", [r"serp_local", r"\bSERP\b"]),
    ("Mapeamento de rede (unidades/hospitais)", [r"\brede\b", r"hospita", r"unidade", r"PA 24", r"clínica"]),
    ("Contexto local (IBGE/CNES)", [r"IBGE", r"CNES", r"popula[çc]", r"leitos", r"\bIDH\b"]),
    ("Keywords com volume real (DataForSeo)", [r"volume", r"keyword_data", r"keyword_suggestions", r"keyword_ideas"]),
    ("Diferenciais únicos", [r"diferenci"]),
    ("FAQ local", [r"\bFAQ\b", r"perguntas?"]),
    ("Validação anti-doorway (teste de substituição)", [r"anti-?doorway", r"substitui[çc]"]),
    ("[V4] Desmontagem de concorrentes", [r"desmontagem", r"concorrente", r"matriz de cobertura"]),
    ("[V4] Ganho de informação / brechas", [r"ganho de informa", r"must-?match", r"brecha"]),
    ("[V5] Kit on-page (matriz de posicionamento)", [r"kit[_ ]on-?page", r"posicoes_principal", r"matriz de posicionamento"]),
    ("[V5] Secundárias com veto de intenção (mín. 6)", [r"veto de inten", r"cluster_candidata", r"qualificada"]),
    ("[V5] Formato de snippet registrado", [r"featured_snippet", r"formato de snippet", r"snippet"]),
    ("[V6] Query fan-out (5-10 sub-perguntas classificadas)", [r"fan-?out", r"sub-?pergunta"]),
    ("[V6] Defensibilidade do dado (nível de cada dado do ganho)", [r"defensibilidade", r"n[ií]vel 1", r"dado propriet"]),
]


def main():
    if len(sys.argv) < 2:
        print("USO: python -X utf8 checkpoint_fase0.py <caminho do PESQUISA_<slug>_COMPLETO.md>")
        print("❌ REPROVADO — nenhum state file informado. PROIBIDO escrever HTML.")
        sys.exit(2)

    path = sys.argv[1]

    if not os.path.isfile(path):
        print(f"❌ REPROVADO — o state file NÃO existe: {path}")
        print("   A FASE 0 não foi concluída. Pesquisa diagnóstica (SERP/keyword/GSC) NÃO conta.")
        print("   PROIBIDO escrever qualquer HTML de artigo. Rode a Fase 0 (references/pesquisa.md) primeiro.")
        sys.exit(1)

    txt = open(path, encoding="utf-8", errors="ignore").read()
    low = txt.lower()

    print(f"Checkpoint FASE 0 — {os.path.basename(path)}")
    print("-" * 56)

    falhas = []
    for nome, padroes in REQUISITOS:
        ok = any(re.search(p, txt, re.I) for p in padroes)
        print(f"  [{'OK   ' if ok else 'FALTA'}] {nome}")
        if not ok:
            falhas.append(nome)

    # Anti-doorway PRECISA estar marcado APROVADO e não pode haver REPROVADO
    ad_aprovado = bool(re.search(r"anti-?doorway[^\n]*aprovad", low) or re.search(r"geral[^\n]*aprovad", low))
    ad_reprovado = bool(re.search(r"reprovad", low))
    ad_ok = ad_aprovado and not ad_reprovado
    print(f"  [{'OK   ' if ad_ok else 'FALTA'}] Anti-doorway explicitamente APROVADO")
    if not ad_ok:
        falhas.append("Anti-doorway APROVADO (encontrado REPROVADO ou ausência de aprovação)")

    # Itens [VERIFICAR]: não reprovam o state file, mas NÃO podem entrar no artigo
    n_verif = len(re.findall(r"\[VERIFICAR", txt, re.I))
    if n_verif:
        print(f"  [AVISO] {n_verif} item(ns) [VERIFICAR] no state file — NÃO podem entrar no artigo.")

    print("-" * 56)

    if falhas:
        print("❌ REPROVADO — faltando no state file:")
        for f in falhas:
            print(f"     - {f}")
        print("   PROIBIDO escrever HTML até o state file estar completo E aprovado pelo usuário.")
        sys.exit(1)

    print("✅ APROVADO — state file completo.")
    print("   Atenção: APROVADO aqui = processo cumprido. O HTML ainda exige o 'ok' EXPLÍCITO")
    print("   do usuário sobre o state file. Sem esse 'ok', continua proibido escrever HTML.")
    sys.exit(0)


if __name__ == "__main__":
    main()
