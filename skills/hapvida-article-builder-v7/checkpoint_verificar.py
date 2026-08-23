#!/usr/bin/env python3
"""
checkpoint_verificar.py — TRAVA MECANICA anti-[VERIFICAR] (disciplina factual YMYL).

Uso:
    python -X utf8 checkpoint_verificar.py <state_file.md> <artigo.html|.md>

Nasceu do duelo de Piracicaba: o endereco do Diagnostico Madre Cecilia e outros
itens [VERIFICAR] passavam porque a trava era so "o agente lembra". Esta trava e
mecanica: roda apos o editor-chefe e ANTES de publicar.

REPROVA o artigo se:
  1) sobrar a string literal "[VERIFICAR" no texto (bilhete interno vazou ao leitor);
  2) aparecer padrao de dado perigoso nunca confirmavel em fonte secundaria:
     telefone, contagem de leitos/salas/UTIs;
  3) aparecer qualquer token da lista FORBIDDEN_TOKENS do state file (secao 9).

LIMITE HONESTO: NAO entende nuance de frase (ex.: "a unidade X opera hoje"). Isso
continua sendo julgamento do editor-chefe / Agente 12 (veracidade). Esta trava pega
o que e mecanico: tags vazadas, numeros proibidos e tokens explicitos.

Para a trava 3 funcionar, a secao 9 do state file deve conter um bloco:
    FORBIDDEN_TOKENS:
    - Hospital Independencia
    - 2 credenciados
    - (um token exato por linha; tudo que NAO pode ser afirmado no artigo)
"""
import sys
# Blindagem UTF-8: console Windows (cp1252) quebra com emoji sem isto
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
import os
import re


def load_forbidden_tokens(state_text):
    toks = []
    m = re.search(r'FORBIDDEN_TOKENS:(.*?)(\n\s*\n|\n#|\Z)', state_text, re.I | re.S)
    if m:
        for line in m.group(1).splitlines():
            line = line.strip().lstrip('-*•').strip()
            if line:
                toks.append(line)
    return toks


DANGER = [
    ("Telefone (DDD)", r'\(\d{2}\)\s?\d{4,5}-?\d{4}'),
    ("Telefone 0800", r'0800[\s\d.\-]{6,}'),
    ("Telefone (digitos crus)", r'\b\d{10,11}\b'),
    ("Contagem de leitos", r'\d+\s*leitos?'),
    ("Contagem de salas", r'\d+\s*salas?'),
    ("Contagem de UTIs", r'\d+\s*UTIs?'),
]


def main():
    if len(sys.argv) < 3:
        print("USO: python -X utf8 checkpoint_verificar.py <state_file.md> <artigo>")
        print("❌ REPROVADO — faltam argumentos (state file e artigo).")
        sys.exit(2)

    state_path, art_path = sys.argv[1], sys.argv[2]
    for p in (state_path, art_path):
        if not os.path.isfile(p):
            print(f"❌ REPROVADO — arquivo nao existe: {p}")
            sys.exit(1)

    state = open(state_path, encoding="utf-8", errors="ignore").read()
    art = open(art_path, encoding="utf-8", errors="ignore").read()

    print(f"Checkpoint VERIFICAR — {os.path.basename(art_path)}")
    print("-" * 56)
    falhas = []

    # 1) tag vazada
    if re.search(r'\[VERIFICAR', art, re.I):
        falhas.append('Tag "[VERIFICAR" vazada no texto (bilhete interno foi ao leitor).')

    # 2) padroes perigosos
    for nome, pat in DANGER:
        for mm in re.finditer(pat, art, re.I):
            trecho = mm.group(0).strip()
            falhas.append(f'{nome}: "{trecho}" — dado nao confirmavel em fonte secundaria; remover ou usar shortcode.')

    # 3) tokens proibidos do state file
    toks = load_forbidden_tokens(state)
    for t in toks:
        if re.search(re.escape(t), art, re.I):
            falhas.append(f'Token proibido [VERIFICAR] afirmado no texto: "{t}".')

    if not toks:
        print("  [AVISO] state file sem bloco FORBIDDEN_TOKENS: — rodaram so as travas genericas (1 e 2).")

    print("-" * 56)
    if falhas:
        print(f"❌ REPROVADO — {len(falhas)} ocorrencia(s):")
        for f in falhas:
            print(f"   - {f}")
        print("   PROIBIDO publicar/seguir ate remover.")
        sys.exit(1)

    print("✅ APROVADO — nenhum dado [VERIFICAR]/perigoso afirmado no texto.")
    print("   (Lembrete: trava mecanica. Nuance de 'unidade opera hoje' continua")
    print("    sendo julgamento do editor-chefe / Agente 12 veracidade.)")
    sys.exit(0)


if __name__ == "__main__":
    main()
