# Contrato de resposta — conciso e visual

Vale para **toda** resposta neste repositório: `/graphify`, `graphify query|path|explain`,
leitura do `GRAPH_REPORT.md` e também explicação normal de código no chat.

Regra-mãe: **o diagrama é a explicação. O texto é só o que o diagrama não consegue dizer.**

---

## 1. Orçamento de texto

| Tipo de pergunta | Prosa máxima | Visual obrigatório |
|---|---|---|
| "o que é X?" | 2 linhas | tabela do nó (arquivo:linha, tipo, grau) |
| "como funciona X?" | 4 linhas | `flowchart LR` do fluxo |
| "panorama do projeto" | 3 linhas | `mindmap` das comunidades |
| "quem chama Y / caminho A→B" | 3 linhas | `flowchart LR` do caminho |
| "por que quebrou / o que muda se eu mexer aqui" | 5 linhas | `flowchart` de impacto |

Estourou o orçamento? O excedente vira **item de tabela ou nó de diagrama**, não vira parágrafo.

## 2. Proibido

- Preâmbulo ("Ótima pergunta", "Vou analisar...", "Deixa eu explicar").
- Resumo final que repete o que já foi dito acima.
- Repetir em prosa o que o diagrama já mostra.
- Listar 20 nós quando os 5 de maior grau respondem a pergunta.
- Despejar saída bruta de `graphify query` no chat. Ela é insumo, não resposta.
- Ensinar conceito genérico ("um decorator em Python é...") sem o usuário pedir.

## 3. Qual diagrama usar

```
panorama / temas do projeto      -> mindmap
fluxo, chamada, dependência      -> flowchart LR
ordem no tempo, request/response -> sequenceDiagram
caminho entre dois nós           -> flowchart LR (só o caminho, sem vizinhos)
comparação, inventário, números  -> tabela markdown (não é diagrama, e tudo bem)
```

Mermaid sempre em bloco ```mermaid. Máximo **12 nós** por diagrama — acima disso,
quebre em dois ou suba um nível de abstração.

Exemplo do formato-alvo (uma resposta inteira):

> O upload cai no Flask e é processado em memória; nada toca disco.
>
> ```mermaid
> flowchart LR
>   U[POST /upload] --> V[valida extensão]
>   V --> P[pandas.read_excel]
>   P --> T[monta tabela De/Por]
>   T --> R[render template]
> ```
>
> | passo | arquivo:linha |
> |---|---|
> | rota | `app_cotacao.py:412` |
> | parser | `app_cotacao.py:180` |

## 4. Honestidade (herda das Honesty Rules do graphify)

Marque a origem de cada aresta afirmada:

- `✓` EXTRAÍDO — veio de AST/arquivo. Cite `arquivo:linha`.
- `~` INFERIDO — o graphify deduziu. Diga que é dedução.
- `?` AMBÍGUO — não confirme. Diga o que falta para confirmar.

Nunca invente aresta para fechar o desenho. Um diagrama com buraco declarado
vale mais que um diagrama completo e errado.

## 5. Idioma e densidade

- Responder em **português do Brasil**.
- Nome de símbolo, arquivo, flag e comando ficam no original, em `código`.
- Número sempre concreto: "23 nós", não "vários nós".
- Frase curta. Se a frase tem vírgula demais, vira item de tabela.

## 6. Ajustes de comando

- `graphify query` neste repo roda com `--budget 1200` (padrão é 2000). Subgrafo
  menor = resposta menos inchada. Use `--budget 3000` só quando 1200 vier truncado
  e faltar o essencial.
- `graphify explain "X"` — as "3-5 sentences" do SKILL.md original ficam em
  **2 linhas + tabela de conexões**.
- `graphify path A B` — desenhe só o caminho. Vizinho que não está no caminho
  não entra no diagrama.

## 7. Se o usuário pedir mais

"detalha", "explica melhor", "abre isso" = licença para passar do orçamento.
Aí sim: prosa longa, código inteiro, passo a passo. Sem isso, vale a seção 1.
