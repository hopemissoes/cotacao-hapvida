## Como responder neste projeto

Leia e obedeça `.claude/graphify-estilo.md` antes de escrever qualquer resposta — vale para
o `/graphify` e para explicação normal de código. Resumo do contrato:

- **O diagrama é a explicação.** Mermaid `mindmap` (panorama), `flowchart LR` (fluxo /
  quem chama quem), `sequenceDiagram` (ordem no tempo), tabela markdown (inventário,
  comparação). Máximo 12 nós por diagrama.
- **Orçamento de prosa: 2 a 5 linhas**, conforme o tipo de pergunta. O que passar disso
  vira linha de tabela ou nó de diagrama — nunca outro parágrafo.
- **Sem preâmbulo e sem resumo final.** Não repetir em texto o que o diagrama já mostra.
- **Português do Brasil**; símbolo, caminho, flag e comando ficam no original, em `código`.
- Toda aresta afirmada vem marcada: `✓` extraída (com `arquivo:linha`), `~` inferida,
  `?` ambígua. Nunca inventar aresta para fechar o desenho.
- "detalha" / "explica melhor" é a licença para passar do orçamento. Sem isso, vale o teto.

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- For codebase questions, first run `graphify query "<question>" --budget 1200` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
