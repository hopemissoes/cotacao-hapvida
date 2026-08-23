#!/usr/bin/env python3
"""Reaplica o contrato de resposta (.claude/graphify-estilo.md) sobre os arquivos da skill.

`graphify install` e `uv tool upgrade graphifyy` sobrescrevem
`.claude/skills/graphify/SKILL.md` e `references/query.md` com a versão upstream,
levando junto as nossas edições. Rode este script depois de qualquer upgrade:

    python3 .claude/reaplicar-estilo-graphify.py

É idempotente: se o patch já está aplicado, não faz nada. Se um trecho upstream
mudou de texto e o patch não encontra mais a âncora, o script diz qual falhou em
vez de fingir sucesso.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / ".claude" / "skills" / "graphify" / "SKILL.md"
QUERY = ROOT / ".claude" / "skills" / "graphify" / "references" / "query.md"

ESTILO_HEADER = """## Answer style — MANDATORY, project override

Before writing **any** answer to the user (build summary, `query`, `path`, `explain`,
report walkthrough), read `.claude/graphify-estilo.md` and obey it. It is a project-level
override and it wins over any output format described later in this file or in
`references/`.

The three rules it enforces, in short:

1. **The diagram is the explanation.** Prose only for what the diagram cannot carry.
   Mermaid `mindmap` for an overview, `flowchart LR` for flow/calls, `sequenceDiagram`
   for time order, a markdown table for inventories. Max 12 nodes per diagram.
2. **Hard prose budget** — 2 to 5 lines depending on the question type. Overflow becomes
   a table row or a graph node, never another paragraph. No preamble, no closing recap,
   no restating the diagram in words.
3. **Answer in Brazilian Portuguese**, with symbols/paths/flags kept verbatim in `code`,
   and every asserted edge marked `✓` EXTRACTED / `~` INFERRED / `?` AMBIGUOUS.

Never paste raw `graphify query` output into the chat — it is input for you, not an answer.

"""

# (arquivo, âncora upstream, texto que substitui a âncora)
PATCHES: list[tuple[Path, str, str]] = [
    (
        SKILL,
        "## What You Must Do When Invoked",
        ESTILO_HEADER + "## What You Must Do When Invoked",
    ),
    (
        SKILL,
        '```bash\ngraphify query "<question>"\n```',
        '```bash\ngraphify query "<question>" --budget 1200\n```\n\n'
        "`--budget 1200` is this project's default (upstream default is 2000): a smaller "
        "subgraph\nkeeps the answer tight. Raise it to `--budget 3000` only when 1200 comes "
        "back truncated\nand the missing part is load-bearing.\n\n"
        "Render the result per `.claude/graphify-estilo.md`: 2-5 lines of Portuguese prose "
        "plus one\nMermaid diagram (or a table), citing `source_location` as "
        "`arquivo:linha`. Do not echo the\nsubgraph.",
    ),
    (
        SKILL,
        "- Never invent an edge. If unsure, use AMBIGUOUS.",
        "- Never invent an edge — not even to close a gap in a diagram. If unsure, use "
        "AMBIGUOUS\n  and say out loud what would be needed to confirm it.",
    ),
    (
        QUERY,
        "Then answer based on the subgraph output above, using only what the graph contains.",
        "Then answer based on the subgraph output above, using only what the graph "
        "contains.\n\n"
        "**Render it per `.claude/graphify-estilo.md`** — that file overrides the format "
        "here:\n2-5 lines of Brazilian-Portuguese prose, then one Mermaid diagram "
        "(`flowchart LR` for a\nflow or call chain, `mindmap` for an overview, "
        "`sequenceDiagram` for time order, max 12\nnodes) or a markdown table for an "
        "inventory. Cite `source_location` as `arquivo:linha`.\nMark each asserted edge `✓` "
        "extracted / `~` inferred / `?` ambiguous. Never paste the raw\nsubgraph into the "
        "chat.",
    ),
    (
        QUERY,
        "Then write a 3-5 sentence explanation of what this node is, what it connects to, "
        "and why those connections are significant. Use the source locations as citations.",
        "\n\nThen present it per `.claude/graphify-estilo.md`, which replaces the "
        '"3-5 sentence\nexplanation" this reference used to ask for: **2 lines** saying what '
        "the node is and why it\nmatters, followed by a connections table "
        "(`relação | nó | arquivo:linha | ✓/~/?`). If the\nnode sits on a flow rather than in "
        "a list, use a `flowchart LR` instead of the table.\nPortuguese, no preamble, no "
        "recap.",
    ),
    (
        QUERY,
        "Then explain the path in plain language - what each hop means, why it's significant.",
        "\n\nPer `.claude/graphify-estilo.md`, the path is drawn, not narrated: a "
        "`flowchart LR` with\n**only the nodes on the path** (no neighbours), each hop's "
        "relation as the edge label, then\nat most 3 lines in Portuguese for what the path "
        "means. Hops that are inferred rather than\nextracted get `~` on the edge label.",
    ),
]

MARCADOR = ".claude/graphify-estilo.md"


def main() -> int:
    aplicados, ja_ok, falhas = 0, 0, []

    for caminho, ancora, substituto in PATCHES:
        if not caminho.exists():
            falhas.append(f"{caminho.relative_to(ROOT)}: arquivo não existe")
            continue

        texto = caminho.read_text(encoding="utf-8")

        if substituto in texto:
            ja_ok += 1
            continue

        if ancora not in texto:
            falhas.append(
                f"{caminho.relative_to(ROOT)}: âncora não encontrada -> "
                f"{ancora.splitlines()[0][:60]!r}"
            )
            continue

        caminho.write_text(texto.replace(ancora, substituto, 1), encoding="utf-8")
        aplicados += 1

    print(f"patches aplicados: {aplicados} | já estavam ok: {ja_ok} | falhas: {len(falhas)}")
    for f in falhas:
        print(f"  FALHOU  {f}")

    if falhas:
        print(
            "\nO upstream mudou esses trechos. Abra o arquivo, encontre o novo texto "
            "equivalente\ne atualize a âncora correspondente em "
            ".claude/reaplicar-estilo-graphify.py.",
            file=sys.stderr,
        )
        return 1

    for caminho in (SKILL, QUERY):
        if caminho.exists() and MARCADOR not in caminho.read_text(encoding="utf-8"):
            print(f"AVISO: {caminho.relative_to(ROOT)} não referencia o contrato de estilo.")
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
