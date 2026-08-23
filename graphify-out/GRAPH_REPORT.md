# Graph Report - cotacao-hapvida  (2026-08-23)

## Corpus Check
- 16 files · ~17,278 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 121 nodes · 121 edges · 17 communities (12 shown, 5 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `2fba4644`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- app_cotacao.py
- What You Must Do When Invoked
- /graphify
- Deploy no Easypanel (Hostinger VPS)
- Contrato de resposta — conciso e visual
- graphify reference: extra exports and benchmark
- Passo a Passo
- graphify reference: query, path, explain
- graphify reference: add a URL and watch a folder
- graphify reference: commit hook and native CLAUDE.md integration
- graphify reference: incremental update and cluster-only
- CLAUDE.md
- graphify reference: GitHub clone and cross-repo merge
- graphify reference: transcribe video and audio
- .claude/CLAUDE.md
- extraction-spec.md

## God Nodes (most connected - your core abstractions)
1. `What You Must Do When Invoked` - 12 edges
2. `/graphify` - 11 edges
3. `Contrato de resposta — conciso e visual` - 8 edges
4. `graphify reference: extra exports and benchmark` - 8 edges
5. `Passo a Passo` - 8 edges
6. `Deploy no Easypanel (Hostinger VPS)` - 7 edges
7. `selecionar_produtos_modal()` - 6 edges
8. `cotar_cidade_pme()` - 6 edges
9. `cotar_cidade_pf()` - 6 edges
10. `main()` - 6 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (17 total, 5 thin omitted)

### Community 0 - "app_cotacao.py"
Cohesion: 0.12
Nodes (25): clicar_avancar(), clique_coords(), clique_real(), comparar_e_melhor(), cotar_cidade_pf(), cotar_cidade_pme(), extrair_valores(), fazer_login() (+17 more)

### Community 1 - "What You Must Do When Invoked"
Cohesion: 0.13
Nodes (15): Part A - Structural extraction for code files, Part B - Semantic extraction (parallel subagents), Part C - Merge AST + semantic into final extraction, Step 0 - GitHub repos and multi-path merge (only if a URL or several paths), Step 1 - Ensure graphify is installed, Step 2.5 - Video and audio (only if video files detected), Step 2 - Detect files, Step 3 - Extract entities and relationships (+7 more)

### Community 2 - "/graphify"
Cohesion: 0.18
Nodes (10): Answer style — MANDATORY, project override, For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands (+2 more)

### Community 3 - "Deploy no Easypanel (Hostinger VPS)"
Cohesion: 0.20
Nodes (9): Acesso, Arquivos Necessarios, Chrome nao inicia, Deploy no Easypanel (Hostinger VPS), Erro de memoria, Estrutura do Projeto para Upload, Notas Importantes, Timeout (+1 more)

### Community 4 - "Contrato de resposta — conciso e visual"
Cohesion: 0.22
Nodes (8): 1. Orçamento de texto, 2. Proibido, 3. Qual diagrama usar, 4. Honestidade (herda das Honesty Rules do graphify), 5. Idioma e densidade, 6. Ajustes de comando, 7. Se o usuário pedir mais, Contrato de resposta — conciso e visual

### Community 5 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 6 - "Passo a Passo"
Cohesion: 0.25
Nodes (8): 1. Acesse o Easypanel, 2. Crie um novo servico, 3. Opcao A: Via GitHub, 3. Opcao B: Via Upload/Docker Image, 4. Configuracoes no Easypanel, 5. Dominio, 6. Deploy, Passo a Passo

### Community 7 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 8 - "graphify reference: add a URL and watch a folder"
Cohesion: 0.50
Nodes (3): For /graphify add, For --watch, graphify reference: add a URL and watch a folder

### Community 9 - "graphify reference: commit hook and native CLAUDE.md integration"
Cohesion: 0.50
Nodes (3): For git commit hook, For native CLAUDE.md integration, graphify reference: commit hook and native CLAUDE.md integration

### Community 10 - "graphify reference: incremental update and cluster-only"
Cohesion: 0.50
Nodes (3): For --cluster-only, For --update (incremental re-extraction), graphify reference: incremental update and cluster-only

## Knowledge Gaps
- **66 isolated node(s):** `graphify`, `1. Orçamento de texto`, `2. Proibido`, `3. Qual diagrama usar`, `4. Honestidade (herda das Honesty Rules do graphify)` (+61 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `What You Must Do When Invoked` connect `What You Must Do When Invoked` to `/graphify`?**
  _High betweenness centrality (0.033) - this node is a cross-community bridge._
- **Why does `/graphify` connect `/graphify` to `What You Must Do When Invoked`?**
  _High betweenness centrality (0.027) - this node is a cross-community bridge._
- **Why does `Deploy no Easypanel (Hostinger VPS)` connect `Deploy no Easypanel (Hostinger VPS)` to `Passo a Passo`?**
  _High betweenness centrality (0.014) - this node is a cross-community bridge._
- **What connects `graphify`, `1. Orçamento de texto`, `2. Proibido` to the rest of the system?**
  _66 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `app_cotacao.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12307692307692308 - nodes in this community are weakly interconnected._
- **Should `What You Must Do When Invoked` be split into smaller, more focused modules?**
  _Cohesion score 0.13333333333333333 - nodes in this community are weakly interconnected._