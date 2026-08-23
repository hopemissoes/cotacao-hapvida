#!/usr/bin/env python3
"""
checkpoint_completude.py — TRAVA de COMPLETUDE / PROFUNDIDADE (v4).
A v4 NAO aceita artigo curto e fraco. Roda no HTML final, antes de publicar.

Uso:
    python -X utf8 checkpoint_completude.py <artigo.html> [city|hospital|tr]

Reprova (city, padrao) se:
  - menos de 8 <h2> (7 secoes S1-S7 + FAQ; conclusao tambem conta)
  - menos de 12 perguntas de FAQ (<details>)
  - menos de 1200 palavras de corpo
  - nenhuma "DICA DRV" (sinal E-E-A-T)
  - nenhuma secao de rede assistencial

LIMITE HONESTO: NAO verifica se a REDE esta COMPLETA vs o catalogo do banco
(`consultar_rede`) — isso e regra do Agente 2 (puxar a rede do banco) + do
editor-chefe (reprovar rede incompleta). Aqui e so o piso de TAMANHO/ESTRUTURA.
"""
import sys
# Blindagem UTF-8: console Windows (cp1252) quebra com emoji sem isto
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
import os
import re

THRESH = {
    "city":     {"h2": 8, "faq": 12, "palavras": 1200},
    "hospital": {"h2": 5, "faq": 6,  "palavras": 800},
    "tr":       {"h2": 6, "faq": 6,  "palavras": 600},
    # [V6] pillar de produto/tema (P1-P9). Piso calibrado no pillar
    # /plano-individual-hapvida/ aprovado em 27/07/2026: 4.579 palavras,
    # 9 h2, 26 h3, 17 FAQ. O piso fica abaixo do real de proposito —
    # e minimo absoluto, nao meta. Ver references/artigo-pillar-produto.md.
    "pillar":   {"h2": 8, "faq": 12, "palavras": 2500},
}

# Tipos em que a secao de rede assistencial NAO e exigida: um pillar de tema
# ("Coparticipacao", "Carencias") fala de regra, nao de rede.
SEM_REDE_OBRIGATORIA = {"pillar"}


def main():
    if len(sys.argv) < 2:
        print("USO: python -X utf8 checkpoint_completude.py <artigo.html> [city|hospital|tr]")
        print("❌ REPROVADO — nenhum arquivo informado.")
        sys.exit(2)

    path = sys.argv[1]
    tipo = (sys.argv[2].lower() if len(sys.argv) > 2 else "city")
    th = THRESH.get(tipo, THRESH["city"])

    if not os.path.isfile(path):
        print(f"❌ REPROVADO — arquivo nao existe: {path}")
        sys.exit(1)

    html = open(path, encoding="utf-8", errors="ignore").read()

    # remove style/script antes de contar palavras
    corpo = re.sub(r"<style[\s\S]*?</style>", " ", html, flags=re.I)
    corpo = re.sub(r"<script[\s\S]*?</script>", " ", corpo, flags=re.I)
    texto = re.sub(r"<[^>]+>", " ", corpo)
    texto = re.sub(r"\[[^\]]+\]", " ", texto)  # remove shortcodes
    palavras = len(re.findall(r"\w+", texto))

    n_h2 = len(re.findall(r"<h2[\s>]", html, re.I))
    n_faq = len(re.findall(r"<details", html, re.I))
    tem_dica = bool(re.search(r"DICA DRV", html, re.I))
    tem_rede = bool(re.search(r"rede assistencial|rede pr[oó]pria", html, re.I))

    print(f"Checkpoint COMPLETUDE ({tipo}) — {os.path.basename(path)}")
    print("-" * 56)
    falhas = []

    def linha(ok, label, val, alvo):
        print(f"  [{'OK   ' if ok else 'FALTA'}] {label}: {val} (min. {alvo})")
        if not ok:
            falhas.append(f"{label}: {val} < {alvo}")

    linha(n_h2 >= th["h2"], "Secoes (<h2>)", n_h2, th["h2"])
    linha(n_faq >= th["faq"], "Perguntas de FAQ", n_faq, th["faq"])
    linha(palavras >= th["palavras"], "Palavras de corpo", palavras, th["palavras"])
    print(f"  [{'OK   ' if tem_dica else 'FALTA'}] Dica DRV (E-E-A-T): {'sim' if tem_dica else 'nao'}")
    if not tem_dica:
        falhas.append("Sem 'DICA DRV' (sinal E-E-A-T)")
    if tipo in SEM_REDE_OBRIGATORIA:
        # pillar de PRODUTO tem P5 (onde tem rede); pillar de TEMA (coparticipacao,
        # carencias) fala de regra e nao de rede — por isso aqui e aviso, nao falha.
        print(f"  [{'OK   ' if tem_rede else 'AVISO'}] Secao de rede: "
              f"{'sim' if tem_rede else 'nao — ok em pillar de TEMA, falta em pillar de PRODUTO (P5)'}")
    else:
        print(f"  [{'OK   ' if tem_rede else 'FALTA'}] Secao de rede: {'sim' if tem_rede else 'nao'}")
        if not tem_rede:
            falhas.append("Sem secao de rede assistencial")

    if tipo == "pillar":
        n_h3 = len(re.findall(r"<h3[\s>]", html, re.I))
        linha(n_h3 >= 15, "Subsecoes (<h3>)", n_h3, 15)

    print("-" * 56)
    if falhas:
        print("❌ REPROVADO — a v4 NAO aceita artigo curto/fraco. Faltando:")
        for f in falhas:
            print(f"   - {f}")
        print("   Aprofundar (ver REQUISITOS DE PROFUNDIDADE [V4]) antes de publicar.")
        sys.exit(1)

    print("✅ APROVADO — piso de completude/profundidade atingido.")
    print("   (Lembrete: piso de TAMANHO/ESTRUTURA. Rede COMPLETA vs catalogo do banco")
    print("    e qualidade do conteudo continuam sendo Agente 2 / editor-chefe / juizes.)")
    sys.exit(0)


if __name__ == "__main__":
    main()
