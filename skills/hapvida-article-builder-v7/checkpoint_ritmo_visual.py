#!/usr/bin/env python3
"""
Checkpoint OBRIGATÓRIO de ritmo visual para artigos hapvida-article-builder.

Detecta sequências longas de <p> de corpo (font-size:18px) sem elemento
visual de quebra entre eles — problema que cansa a leitura quando vários
parágrafos curtos vêm seguidos.

Uso:
    python -X utf8 checkpoint_ritmo_visual.py <arquivo.html>

Regra:
    - ≤3 parágrafos consecutivos     → aprovado
    - 4 parágrafos                    → aviso
    - ≥5 parágrafos                   → REPROVADO

Elementos visuais que valem como quebra:
    - <h3> (subseção)
    - <div class="grid2|grid3|grid4|grid5"> (cards)
    - <div ... border:2px solid #ff6b00> (hero card)
    - <div ... linear-gradient(135deg,#eff6ff> (box: Resumo/Importante/Dica DRV)
    - <div ... linear-gradient(135deg,#fff8f3> (box Portabilidade) — quando existir
    - <div ... padding-left:32px> (linha do tempo)
    - <ul> ou <ol> (listas bullet)
    - <table> (tabela)
    - <blockquote> (quote)
    - <div ... border-left:4px solid #ff6b00> (callout/quote novo)

NÃO contam como quebra:
    - Outros <p>
    - <br>
    - <span class="destaque-laranja-suave"> (vai DENTRO do parágrafo)
    - [elementor-template] (form não é break de conteúdo)

Retorna exit code 0 se aprovado, 1 se houver qualquer sequência reprovada.
"""

import re
import sys
# Blindagem UTF-8: console Windows (cp1252) quebra com emoji sem isto
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
from pathlib import Path

LIMITE_OK = 3        # até 3 P consecutivos = aprovado
LIMITE_AVISO = 4     # 4 P = aviso (aceitar só se forçado)
# ≥5 P = reprovado


def encontrar_fim_elemento(html: str, pos_inicio: int, tag: str) -> int:
    """
    Dado o início de uma tag <tag>, encontra a posição do </tag> correspondente
    usando contagem de balanço. Retorna posição após o </tag>.
    """
    balance = 0
    i = pos_inicio
    abertura_re = re.compile(rf"<{tag}[^>]*>", re.IGNORECASE)
    fechamento_re = re.compile(rf"</{tag}>", re.IGNORECASE)
    while i < len(html):
        m_open = abertura_re.match(html[i:])
        if m_open:
            balance += 1
            i += m_open.end()
            continue
        m_close = fechamento_re.match(html[i:])
        if m_close:
            balance -= 1
            i += m_close.end()
            if balance == 0:
                return i
            continue
        i += 1
    return len(html)  # se não achar fechamento, vai até o fim


def tokenizar(html: str) -> list:
    """
    Percorre o HTML e gera uma lista ordenada de tokens relevantes.
    IMPORTANTE: quando encontra um break visual com conteúdo, PULA o conteúdo
    interno (não conta <p> internos como p_corpo).
    """
    tokens = []
    i = 0
    while i < len(html):
        # H2 — início de nova seção (reseta contador)
        m = re.match(r"<h2[^>]*>", html[i:])
        if m:
            tokens.append(("h2_start", i))
            i += m.end()
            continue

        # H3 — break visual (subseção). Não tem conteúdo interno pra pular.
        m = re.match(r"<h3[^>]*>", html[i:])
        if m:
            tokens.append(("h3", i))
            i += m.end()
            continue

        # P corpo (font-size:18px) — exclui o subtítulo da seção (font-weight:500)
        m = re.match(r"<p\s+([^>]*)>", html[i:])
        if m:
            attrs = m.group(1).replace(" ", "")
            if (
                "font-size:18px" in attrs
                and "font-weight:500" not in attrs
                and "color:#718096" not in attrs
            ):
                tokens.append(("p_corpo", i))
                i += m.end()
                continue
            # Se for outro tipo de <p> (subtítulo, cards, footer), só avança
            i += m.end()
            continue

        # Grid de cards — PULAR conteúdo interno
        m = re.match(r'<div\s+class="grid[2345]"', html[i:])
        if m:
            tokens.append(("cards_grid", i))
            i = encontrar_fim_elemento(html, i, "div")
            continue

        # Hero card — PULAR conteúdo interno
        m = re.match(r"<div[^>]*border:2px solid #ff6b00", html[i:])
        if m:
            tokens.append(("hero_card", i))
            i = encontrar_fim_elemento(html, i, "div")
            continue

        # Box (Resumo/Importante/Dica DRV) — PULAR conteúdo interno
        m = re.match(r"<div[^>]*linear-gradient\(135deg,#eff6ff", html[i:])
        if m:
            tokens.append(("box", i))
            i = encontrar_fim_elemento(html, i, "div")
            continue

        # Box variação fff8f3 — PULAR conteúdo interno
        m = re.match(r"<div[^>]*linear-gradient\(135deg,#fff8f3", html[i:])
        if m:
            tokens.append(("box", i))
            i = encontrar_fim_elemento(html, i, "div")
            continue

        # Linha do tempo — PULAR conteúdo interno
        m = re.match(r"<div[^>]*padding-left:32px", html[i:])
        if m:
            tokens.append(("timeline", i))
            i = encontrar_fim_elemento(html, i, "div")
            continue

        # Callout/quote — PULAR conteúdo interno
        m = re.match(r"<div[^>]*border-left:4px solid #ff6b00", html[i:])
        if m:
            tokens.append(("callout", i))
            i = encontrar_fim_elemento(html, i, "div")
            continue

        # Bullet list — PULAR conteúdo interno
        m = re.match(r"<(ul|ol)[^>]*>", html[i:])
        if m:
            tag = m.group(1)
            tokens.append(("bullet_list", i))
            i = encontrar_fim_elemento(html, i, tag)
            continue

        # Tabela — PULAR conteúdo interno
        m = re.match(r"<table[^>]*>", html[i:])
        if m:
            tokens.append(("table", i))
            i = encontrar_fim_elemento(html, i, "table")
            continue

        # Blockquote — PULAR conteúdo interno
        m = re.match(r"<blockquote[^>]*>", html[i:])
        if m:
            tokens.append(("quote", i))
            i = encontrar_fim_elemento(html, i, "blockquote")
            continue

        i += 1
    return tokens


def pegar_titulo_secao(html: str, pos_h2: int) -> str:
    """Extrai texto do <h2> a partir da posição."""
    m = re.search(r"<h2[^>]*>([^<]+)</h2>", html[pos_h2 : pos_h2 + 500])
    return m.group(1)[:60] if m else "(sem h2)"


def checkpoint(caminho_html: str) -> int:
    arquivo = Path(caminho_html)
    if not arquivo.exists():
        print(f"❌ Arquivo não encontrado: {caminho_html}")
        return 2

    html = arquivo.read_text(encoding="utf-8")
    tokens = tokenizar(html)

    if not tokens:
        print("⚠️  Nenhum token encontrado.")
        return 2

    # Agrupar tokens por seção (entre h2_start)
    secoes = []
    secao_atual = []
    for kind, pos in tokens:
        if kind == "h2_start":
            if secao_atual:
                secoes.append(secao_atual)
            secao_atual = []
        secao_atual.append((kind, pos))
    if secao_atual:
        secoes.append(secao_atual)

    # Analisar cada seção: maior sequência de p_corpo consecutivos
    aprovadas, em_aviso, reprovadas = [], [], []

    for s_idx, secao in enumerate(secoes, 1):
        sequencias = []
        sequencia_atual = 0
        for kind, _pos in secao:
            if kind == "p_corpo":
                sequencia_atual += 1
            else:
                if sequencia_atual >= 1:
                    sequencias.append(sequencia_atual)
                sequencia_atual = 0
        if sequencia_atual >= 1:
            sequencias.append(sequencia_atual)

        pior = max(sequencias) if sequencias else 0

        h2_pos = next((p for k, p in secao if k == "h2_start"), 0)
        titulo = pegar_titulo_secao(html, h2_pos) if h2_pos else "(lead/sumário)"

        info = {
            "idx": s_idx,
            "titulo": titulo,
            "sequencias": sequencias,
            "pior": pior,
        }

        if pior >= 5:
            reprovadas.append(info)
        elif pior == LIMITE_AVISO:
            em_aviso.append(info)
        else:
            aprovadas.append(info)

    total = len(secoes)
    print(f"\n{'=' * 75}")
    print(f"CHECKPOINT — RITMO VISUAL ({arquivo.name})")
    print(f"{'=' * 75}")
    print(f"Total de seções analisadas: {total}")
    print(f"  ✅ Aprovadas (≤3 P consecutivos):       {len(aprovadas)}")
    print(f"  ⚠️  Em aviso (4 P consecutivos):         {len(em_aviso)}")
    print(f"  ❌ Reprovadas (≥5 P consecutivos):      {len(reprovadas)}")
    print()

    if em_aviso:
        print(f"⚠️  SEÇÕES NO LIMITE ({len(em_aviso)}) — considerar inserir break:")
        for s in em_aviso:
            print(f"   S{s['idx']}: {s['titulo']}")
            print(f"        Sequências: {s['sequencias']} | Pior bloco: {s['pior']} P")
        print()

    if reprovadas:
        print(f"❌ SEÇÕES REPROVADAS ({len(reprovadas)}) — INSERIR BREAK VISUAL:")
        for s in reprovadas:
            print(f"   S{s['idx']}: {s['titulo']}")
            print(f"        Sequências: {s['sequencias']} | Pior bloco: {s['pior']} P")
        print()
        print("AÇÃO OBRIGATÓRIA: inserir um dos elementos de quebra")
        print("(H3, box, cards, hero card, timeline, bullet list, callout, tabela)")
        print("dentro de cada bloco com 5+ parágrafos consecutivos.")
        return 1

    print("✅ CHECKPOINT APROVADO — ritmo visual OK em todas as seções.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python -X utf8 checkpoint_ritmo_visual.py <arquivo.html>")
        sys.exit(2)
    sys.exit(checkpoint(sys.argv[1]))
