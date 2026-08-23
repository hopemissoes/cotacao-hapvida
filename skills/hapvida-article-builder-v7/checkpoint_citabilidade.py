#!/usr/bin/env python3
"""
Checkpoint de CITABILIDADE GEO/AEO para artigos hapvida-article-builder-geo (v2).

Uso:
    python -X utf8 checkpoint_citabilidade.py <arquivo.html>

Mede heurísticas de "passagem citável" por seção (ver references/geo-aeo.md §1):
  - cada seção (<h2>) abre com um <p> de corpo (font-size:18px) curto e direto?
  - a frase de abertura tem ~40-60 palavras (banda aceitável 25-75)?
  - a abertura traz um número-âncora (dígito) — sinal de resposta factual?
  - densidade de fonte: o artigo tem links externos de fonte (rel="nofollow")?

⚠️ DIRECIONAL, não nota rígida. As faixas vêm de estudos não replicados
(ver ressalva 2 em references/geo-aeo.md). O objetivo é flagrar seções que
abrem com rampa de aquecimento em vez de resposta — não premiar contagem exata.

Exit code: 0 se nenhuma seção reprovada; 1 se houver seção sem abertura citável.
"""

import re
import sys
from pathlib import Path

# Garante UTF-8 no stdout (Windows usa cp1252 por padrão e quebra nos emojis).
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

MIN_PALAVRAS = 25       # abaixo: abertura curta demais p/ responder
MAX_PALAVRAS = 75       # acima: não é resposta direta, é rampa/narrativa
IDEAL_MIN, IDEAL_MAX = 40, 60


def limpar(texto: str) -> str:
    texto = re.sub(r"<[^>]+>", "", texto)
    texto = re.sub(r"\[[^\]]+\]", "XXX", texto)  # shortcode -> placeholder
    texto = re.sub(r"&[a-z]+;", " ", texto)
    return re.sub(r"\s+", " ", texto).strip()


def primeiro_p_corpo(trecho: str):
    """Primeiro <p> de corpo (font-size:18px) dentro do trecho da seção."""
    m = re.search(r'<p[^>]*style="[^"]*font-size:\s*18px[^"]*"[^>]*>(.*?)</p>',
                  trecho, flags=re.DOTALL)
    return limpar(m.group(1)) if m else ""


def titulo_h2(tag: str) -> str:
    return (limpar(tag) or "(sem texto)")[:60]


def checkpoint(caminho_html: str) -> int:
    arquivo = Path(caminho_html)
    if not arquivo.exists():
        print(f"❌ Arquivo não encontrado: {caminho_html}")
        return 2

    html = arquivo.read_text(encoding="utf-8")

    # Divide o documento por <h2 ...>...</h2>, guardando o conteúdo seguinte.
    h2s = list(re.finditer(r"<h2[^>]*>.*?</h2>", html, flags=re.DOTALL))
    if not h2s:
        print("⚠️  Nenhum <h2> encontrado. Rode no HTML completo do artigo/bloco.")
        return 2

    ok, atencao, reprovadas = [], [], []
    for i, h in enumerate(h2s):
        ini = h.end()
        fim = h2s[i + 1].start() if i + 1 < len(h2s) else len(html)
        secao = html[ini:fim]
        titulo = titulo_h2(h.group(0))
        abertura = primeiro_p_corpo(secao)

        if not abertura:
            reprovadas.append((titulo, 0, False, "sem <p> de corpo logo após o H2"))
            continue

        n = len(abertura.split())
        tem_numero = bool(re.search(r"\d", abertura))
        if n < MIN_PALAVRAS:
            reprovadas.append((titulo, n, tem_numero, "abertura curta demais p/ responder"))
        elif n > MAX_PALAVRAS:
            atencao.append((titulo, n, tem_numero, "abertura longa — não é resposta direta"))
        elif not (IDEAL_MIN <= n <= IDEAL_MAX):
            atencao.append((titulo, n, tem_numero, "fora da faixa ideal 40-60 (aceitável)"))
        else:
            ok.append((titulo, n, tem_numero, ""))

    # Densidade de fonte (links externos com rel nofollow = fontes citadas)
    fontes = len(re.findall(r'rel="[^"]*nofollow', html))

    print(f"\n{'=' * 75}")
    print(f"CHECKPOINT — CITABILIDADE GEO/AEO ({arquivo.name})")
    print(f"{'=' * 75}")
    print(f"Seções (<h2>) analisadas: {len(h2s)}")
    print(f"  ✅ Abertura citável (faixa ideal):  {len(ok)}")
    print(f"  ⚠️  Aceitável / atenção:            {len(atencao)}")
    print(f"  ❌ Reprovadas:                      {len(reprovadas)}")
    print(f"Links externos de fonte (rel=nofollow): {fontes}")
    sem_numero = [t for grupo in (ok, atencao) for (t, n, num, _) in [(g[0], g[1], g[2], g[3]) for g in grupo] if not num]
    if sem_numero:
        print(f"Seções com abertura SEM número-âncora: {len(sem_numero)} "
              f"(considere ancorar com um dado da cidade/hospital)")
    print()

    if atencao:
        print(f"⚠️  ATENÇÃO ({len(atencao)}):")
        for titulo, n, num, motivo in atencao:
            print(f"   • {titulo} — {n} palavras na abertura — {motivo}")
        print()

    if reprovadas:
        print(f"❌ REPROVADAS ({len(reprovadas)}) — abrir a seção com resposta direta:")
        for titulo, n, num, motivo in reprovadas:
            print(f"   • {titulo} — {motivo}")
        print()
        print("AÇÃO: logo após o H2, escrever 1 frase-resposta de ~40-60 palavras,")
        print("específica da cidade/hospital, com 1 número-âncora (ver geo-aeo.md §1.1).")
        print("Lembre: a resposta tem de ser ÚNICA da cidade (não passar no teste de substituição).")
        return 1

    print("✅ CHECKPOINT DE CITABILIDADE APROVADO (heurístico/direcional).")
    print("   Confirme manualmente que cada abertura é específica da cidade — o script")
    print("   mede forma, não unicidade. Anti-doorway continua sendo julgamento humano.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python -X utf8 checkpoint_citabilidade.py <arquivo.html>")
        sys.exit(2)
    sys.exit(checkpoint(sys.argv[1]))
