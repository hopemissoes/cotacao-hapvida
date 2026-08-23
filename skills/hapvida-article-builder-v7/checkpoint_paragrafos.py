#!/usr/bin/env python3
"""
Checkpoint OBRIGATÓRIO de tamanho de parágrafo para artigos
hapvida-article-builder.

Uso:
    python -X utf8 checkpoint_paragrafos.py <arquivo.html>

Regra:
    - ≤380 chars      → aprovado
    - 381-480 chars   → no limite (justificar)
    - >480 chars      → REPROVADO. Quebrar antes de prosseguir.

Mede apenas os <p> de CORPO (font-size:18px no padrão V4.5.0).
Cards, subtítulos e footer notes não entram na medida.

Retorna exit code 0 se aprovado, 1 se houver qualquer reprovado.
"""

import re
import sys
# Blindagem UTF-8: console Windows (cp1252) quebra com emoji sem isto
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
from pathlib import Path

LIMITE_ALVO = 380        # ~55 palavras / 4 linhas no layout 820px
LIMITE_ABSOLUTO = 480    # 5 linhas — só aceitar se justificado


def limpar(texto: str) -> str:
    """Remove HTML interno e shortcodes para contar só o texto visível."""
    texto = re.sub(r"<[^>]+>", "", texto)
    texto = re.sub(r"\[[^\]]+\]", "XXX", texto)  # shortcode = placeholder curto
    texto = re.sub(r"&[a-z]+;", " ", texto)
    return texto.strip()


def extrair_paragrafos_corpo(html: str) -> list:
    """
    Pega só os <p> de corpo (font-size:18px no padrão V4.5.0).
    Ignora cards (14px), subtítulos (15px), footer notes (12px).
    """
    padrao = r'<p[^>]*style="[^"]*font-size:\s*18px[^"]*"[^>]*>(.*?)</p>'
    return re.findall(padrao, html, flags=re.DOTALL)


def checkpoint(caminho_html: str) -> int:
    arquivo = Path(caminho_html)
    if not arquivo.exists():
        print(f"❌ Arquivo não encontrado: {caminho_html}")
        return 2

    html = arquivo.read_text(encoding="utf-8")
    paragrafos = extrair_paragrafos_corpo(html)

    if not paragrafos:
        print("⚠️  Nenhum <p> de corpo encontrado (font-size:18px).")
        print("    Conferir se o bloco foi salvo no formato V4.5.0.")
        return 2

    aprovados, no_limite, reprovados = [], [], []

    for i, bruto in enumerate(paragrafos, 1):
        texto = limpar(bruto)
        if not texto:
            continue
        n = len(texto)
        preview = texto[:100] + ("..." if len(texto) > 100 else "")
        if n <= LIMITE_ALVO:
            aprovados.append((i, n, preview))
        elif n <= LIMITE_ABSOLUTO:
            no_limite.append((i, n, preview))
        else:
            reprovados.append((i, n, preview))

    total = len(aprovados) + len(no_limite) + len(reprovados)
    print(f"\n{'=' * 75}")
    print(f"CHECKPOINT — TAMANHO DE PARÁGRAFO ({arquivo.name})")
    print(f"{'=' * 75}")
    print(f"Total <p> de corpo: {total}")
    print(f"  ✅ Aprovados (≤{LIMITE_ALVO} chars):     {len(aprovados)}")
    print(f"  ⚠️  No limite ({LIMITE_ALVO+1}-{LIMITE_ABSOLUTO} chars): {len(no_limite)}")
    print(f"  ❌ Reprovados (>{LIMITE_ABSOLUTO} chars):     {len(reprovados)}")
    print()

    if no_limite:
        print(f"⚠️  PARÁGRAFOS NO LIMITE ({len(no_limite)}) — aceitar só se a divisão prejudicar o sentido:")
        for idx, n, preview in no_limite:
            linhas = round(n / 75, 1)
            print(f"   P{idx}: {n} chars (~{linhas} linhas)")
            print(f"        {preview}")
        print()

    if reprovados:
        print(f"❌ PARÁGRAFOS REPROVADOS ({len(reprovados)}) — REESCREVER antes de prosseguir:")
        for idx, n, preview in reprovados:
            linhas = round(n / 75, 1)
            print(f"   P{idx}: {n} chars (~{linhas} linhas)")
            print(f"        {preview}")
        print()
        print("AÇÃO OBRIGATÓRIA: dividir cada parágrafo reprovado em dois,")
        print("redistribuindo o conteúdo. Rodar o checkpoint de novo até passar.")
        return 1

    print("✅ CHECKPOINT APROVADO — bloco pode ser apresentado ao usuário.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python -X utf8 checkpoint_paragrafos.py <arquivo.html>")
        sys.exit(2)
    sys.exit(checkpoint(sys.argv[1]))
