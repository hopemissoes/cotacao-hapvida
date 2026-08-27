# Patch da skill v7 — Cartão de Checklist em Duas Colunas

Aplicado em `/root/.claude/skills/synced/hapvida-article-builder-v7/` nesta sessão.
**Essa pasta é sincronizada**, então a mudança precisa ser espelhada na instalação de origem
(`C:\Users\netop\.claude\skills\hapvida-article-builder-v7\`) para valer nas próximas rodadas.

## O problema que o patch corrige

A skill **não tinha componente para duas listas paralelas**. Sem template, cada artigo improvisava
dois `<div>` de `grid2` com `<p>` soltos e sem título de coluna. No desktop passa; no celular as
colunas empilham e as duas listas viram uma só — o título "Documentos dos beneficiários" fica
indistinguível de mais um item em negrito. E o `<p>` herda `text-align:justify` da regra global,
que em linha curta abre buracos entre as palavras.

## Mudança 1 — `references/components.md`

Nova seção **"Cartão de Checklist em Duas Colunas"**, inserida imediatamente antes de
`## Metric Cards (grid4 example — 3 gray + 1 orange)`. Traz o template HTML completo, as três
decisões de design e os limites de uso.

As três decisões:

1. **Cada coluna é um cartão fechado** (borda + `border-top` de 3px colorido). A divisória é a
   borda do próprio cartão. **Não usar `border-right` na coluna A** — quando o flex quebra no
   celular, aquela borda vira um risco vertical solto no meio do texto, e `@media` para corrigir
   grid é proibido pela regra da casa (o Elementor sobrescreve).
2. **Cada coluna se anuncia**: `card-head` com badge de 30px (letras, nunca emoji) + título.
   Laranja `#ff6b00` na coluna A, azul `#2563eb` na coluna B.
3. **Item é `<div class="doc-row">`, não `<p>`**: marcador `&#9656;`, `text-align:left` explícito
   (foge do justify global) e `border-top:1px solid #f1f5f9` a partir do 2º item.

Limites: 3 a 5 itens por coluna, item de 1 a 3 linhas, exatamente 2 colunas.

## Mudança 2 — `references/styles-and-scripts.md`

No bloco `<style>` obrigatório, logo depois de `/* === ANTI-WPAUTOP (STEPS) === */`:

```css
/* === ANTI-WPAUTOP (CHECKLIST DE DOCUMENTOS) === */
.doc-col>p,.doc-col>br{display:none!important}
.doc-row>p{display:contents!important}
.doc-row>br{display:none!important}
```

E uma linha nova em **Rules**: `.doc-row>p` usa `display:contents`, **nunca `display:none`** — o
`<p>` que o wpautop injeta ali embrulha o conteúdo do item, e escondê-lo apagaria a linha inteira.
É a mesma razão da regra do `.box-row`.

## Mudança 3 — `SKILL.md`

- Na tabela **"Elementos visuais que valem como quebra"** (ritmo visual), linha nova:
  `Cartão de checklist em duas colunas (doc-col/doc-row)` — quando o conteúdo são duas listas
  paralelas.
- Em **WordPress Survival Rules (Critical)**, regra `8b`: duas listas paralelas usam o componente,
  nunca dois `<div>` de `grid2` com `<p>` soltos e sem título de coluna.

## O que não precisou mudar

`checkpoint_ritmo_visual.py` já reconhece `<div class="grid2">` como quebra visual e pula o
conteúdo interno — o componente entra na contagem sozinho, sem alteração no script.
