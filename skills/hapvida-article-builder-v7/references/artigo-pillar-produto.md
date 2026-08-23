# ARTIGO PILLAR DE PRODUTO / TEMA (P1-P9) [V6 — quarto arquétipo]

> **Por que este arquivo existe.** Até a v5 a skill tinha três arquétipos — cidade (S1-S7), hospital (HS1-HS4) e tabela regional (TR1-TR5). O `pillar-pages.md` é um **registro de links** ("estes pillars existem, não duplique"), não uma arquitetura para construir. Resultado: os pillars refeitos em julho/2026 (Individual, Nosso Plano, Plano Mix, Nosso Médico, Adesão, Empresarial) foram produzidos **improvisando em cima da estrutura de cidade**. Este arquivo formaliza o que deu certo.
>
> **Base:** o pillar `/plano-individual-hapvida/` reformulado em 26-27/07/2026 — 4.579 palavras, 9 H2, 26 H3, 17 FAQ, 16 links internos, aprovado pelo usuário. A estrutura abaixo é a dele, generalizada.

---

## Quando usar este arquétipo

| Família | Exemplos | Usa P1-P9? |
|---|---|---|
| **Produto** | Plano Individual, Nosso Plano, Plano Mix, Nosso Médico, NotreLife, Adesão, Empresarial | ✅ completo |
| **Tema/conceito** | Coparticipação, Carências, Portabilidade, Como Contratar, O Que Cobre | ✅ com P2 e P5 encolhidos |
| **Avaliação** | "Hapvida é boa?", "Plano de saúde barato" | ✅ com P4 e P9 ampliados |
| **Comparação entre operadoras** | "Hapvida vs Unimed" | ⚠️ **ler antes a armadilha do listicle** (`geo-plataformas.md`) |

**Não** use aqui: artigo de cidade (S1-S7), de hospital (HS1-HS4), de tabela regional (TR1-TR5) ou de cobertura (skill `hapvida-coverage-builder`).

---

## FASE P0 — diagnóstico (obrigatória antes de reescrever pillar que já existe)

Isto **não** substitui a FASE 0 normal; roda antes dela. Nasceu de uma descoberta cara: **um pillar pode não ranquear nem para a própria keyword** — e a causa costuma ser a home do site canibalizando, não falta de conteúdo.

Quatro coletas, quatro ferramentas, nenhuma opinião:

| Pergunta | Como responder | O que fazer com a resposta |
|---|---|---|
| A página rende? | GSC `gsc_queries_for_page` — impressões, cliques, CTR, posição em 28 dias | CTR 0% com impressão alta = problema de title/meta, não de conteúdo |
| **Quem ranqueia pela keyword-alvo?** | DataForSeo `serp_local` na keyword do pillar | **Se for a home ou outro artigo seu, é canibalização** — reescrever o pillar sem resolver isso não adianta |
| Quanta autoridade interna ela tem? | Supabase `consultar_links_para_destino` | Muitos links → **preservar a URL**. Trocar slug joga fora autoridade acumulada |
| O que o banco já diz dela? | Supabase `consultar_artigo` + `consultar_pillars_proibicoes` | "saturado", proibições de conteúdo, overlaps já mapeados |

**Saída da P0:** um parágrafo dizendo se o problema é **conteúdo**, **ângulo**, **title/meta** ou **canibalização** — e a decisão de URL (manter ou 301, com o contraponto registrado).

---

## A arquitetura P1-P9

> **[V7] A ORDEM MUDOU: a P3 (Quanto custa) é a PRIMEIRA seção.** Ordem de renderização na **v7.1**: **P3↑a (H2 + contexto + tabela) → SUMÁRIO → P3↑b (formulário + análise + imagem da tabela por último) → P1 → P2 → P4 → P5 → P6 → P7 → P8 → P9**. A numeração não muda (continua P1, P2, P3…) — muda a ordem em que aparecem no HTML. Nenhuma seção é cortada. Fonte da verdade da ordem: `references/preco-primeiro.md`.
>
> **Cuidado do pillar:** a definição citável de 40-60 palavras continua na **P1**, agora em 2º lugar — ela **não** sobe para dentro da P3↑ e **não** é duplicada no topo. O que sobe é a tabela, não a definição.
>
> **E o eixo continua na P4.** Preço em primeiro lugar é ordem de leitura; o eixo é o que faz o artigo vencer. Prioridade de posição ≠ prioridade de importância.

| Seção | O que é | Obrigatória |
|---|---|---|
| **P3↑ [V7.1]** | **Quanto custa** — shortcode obrigatório, nunca valor fixo. **1ª seção do artigo, logo após o lead**: H2 + contexto + tabela, **sumário colado**, e só então formulário, análise e (por último) a imagem da tabela | ✅ |
| **P1** | **O que é + quem pode contratar** — definição citável em 40-60 palavras, depois o público real | ✅ |
| **P2** | **O que a Hapvida vende nessa modalidade** — tipos de cobertura + produtos nomeados, cada um com H3 | ✅ (encolhe em pillar de tema) |
| **P4** | **O EIXO — o ângulo que nenhum concorrente tem** | ✅ **é o coração do artigo** |
| **P5** | **Onde tem rede / onde é vendido** — âmbito nacional, ligando aos artigos de cidade | ✅ (encolhe em pillar de tema) |
| **P6** | **Comparação interna** — esta modalidade × a alternativa **da casa** | ✅ |
| **P7** | **Segmento específico** — aposentado, 50+, MEI, família, quem sai de plano empresarial | ✅ |
| **P8** | **Dúvidas (FAQ)** — mín. 12, alvo 15-17 | ✅ |
| **P9** | **Vale a pena?** — veredito consultivo, com "pode NÃO compensar para" | ✅ |

### P4 — o eixo (a seção que decide se o artigo vence)

Todo concorrente cobre o mesmo: o que é, quem pode contratar, cobertura, carências, coparticipação, faixa etária. **O artigo só ganha no que eles não cobrem.**

O eixo sai do **CI-2** e tem de ser de **nível 1-2 de defensibilidade** (ver `SKILL.md` → DEFENSIBILIDADE DO DADO). Exemplo real, do pillar Individual:

> O plano individual é o único com reajuste sob teto anual da ANS. O que torna a modalidade ruim para a operadora é exatamente o que a torna boa para o consumidor — e foi por isso que quase todas as grandes fugiram do segmento.

Onze concorrentes desmontados, **nenhum** explicava por que a modalidade quase sumiu. Esse é o formato do eixo: uma tensão real, verificável, que o leitor não acha em outro lugar.

**Teste do eixo:** se o concorrente pudesse escrever a mesma frase depois de 20 minutos de Google, não é eixo — é dado nível 5.

### P9 — o veredito (o mais barato e o mais raro)

Duas listas, sempre as duas: **"costuma compensar para"** e **"pode não compensar para"**. Admitir para quem o produto **não** serve é o sinal de E-E-A-T mais forte e mais barato que existe — e praticamente nenhum concorrente faz, porque todos estão vendendo.

Trava YMYL: dizer para quem não compensa é orientação **comercial**, nunca clínica. Nada de "quem tem a doença X deve escolher Y".

---

## Anti-doorway de pillar — o teste é OUTRO

No artigo de cidade, o teste de substituição troca **a cidade**. Aqui isso não serve: pillar é nacional.

**No pillar, o teste troca o PRODUTO.** Pegue a seção e substitua "plano individual" por "Plano Mix". Se continuar válida, a seção é genérica — e o risco não é doorway contra um concorrente, é **doorway contra o seu próprio pillar irmão**. Vocês têm 6+ pillars de produto: eles se canibalizam com facilidade.

**Três travas obrigatórias:**
1. **Rodar `consultar_pillars_proibicoes` antes de escrever.** O banco registra o que cada pillar não pode repetir.
2. **Rodar `consultar_overlaps_doorway`** para os pillars da mesma família.
3. **Pillar não desce a detalhe de cidade.** Rede por cidade, tabela por cidade e endereço são território do artigo de cidade e da TR. O pillar diz o âmbito nacional e **linka**. Isso já foi corrigido à mão uma vez (parágrafos e tabelas de cidade foram removidos do pillar empresarial) — não recriar o problema.

**E a armadilha do listicle:** P6 compara **produtos da casa** (Individual × Empresarial, Nosso Plano × Nosso Médico). Comparar com outras operadoras só com escopo declarado e critério verificável (ex.: carências segundo a ANS), **nunca premiando a si mesmo** — ver `references/geo-plataformas.md`.

---

## Limites quantitativos

| Item | Mínimo | Alvo | Referência real |
|---|---|---|---|
| Palavras de corpo | 2.500 | 3.500-4.500 | 4.579 |
| `<h2>` | 8 | 9 | 9 |
| `<h3>` | 15 | 22-28 | 26 |
| FAQ (`<details>`) | 12 | 15-17 | 17 |
| Links internos únicos | 8 | 12-16 | 16 |
| Links externos | 2 | 3-4 | — |
| Shortcodes de preço | 3 | conforme as praças citadas | 22 |
| `[elementor-template]` | 2 | 3 | 3 |
| Dados de nível 1-2 | 3 | 5+ | — |

Trava mecânica:
```
python -X utf8 C:\Users\netop\.claude\skills\hapvida-article-builder-v7\checkpoint_completude.py <artigo.html> pillar
python -X utf8 C:\Users\netop\.claude\skills\hapvida-article-builder-v7\checkpoint_preco_primeiro.py <artigo.html> pillar
```

**[V7]** Os limites acima **não mudam** com a reordenação — mesma contagem de palavras, H2, H3, FAQ e links. Se o artigo encolheu ao subir a P3, alguém cortou conteúdo: reprova.

---

## Layout — o mesmo sistema da v5, nesta dosagem

O pillar aprovado usa **exatamente** os componentes da v5. Nada novo, nada removido:

| Componente | Dose no pillar real |
|---|---|
| `toc-list` (sumário **vertical**) | 1 — com 10 itens. **Nunca `v5-chips`** |
| `destaque-laranja-suave` | 19 |
| `box-row` + `card-head`/`card-icon` | 12 / 8 |
| `grid2` / `grid3` / `grid4` | 3 / 2 / 2 |
| `v5-countup` (contador animado) | 2 |
| `v5-trust` (selos) | 1 |
| `v5-sticky-cta` (barra fixa mobile) | 1 |
| `v5-reveal` | 1 |
| `[elementor-template]` | 3 |
| `<table>` | 1 (comparativo de praças) |
| `<figure>`/`<img>` | 1 |
| `<ul>` / `<blockquote>` | 0 / 0 |

**Leitura:** o pillar é **denso em componente de bloco** (box-row, card, grid) e **pobre em lista solta** — a informação vira cartão, não bullet. O ritmo visual vem do `destaque-laranja-suave`, que aparece a cada ~240 palavras.

As regras de layout da v5 continuam valendo integralmente: melhoria progressiva (sem JS nada some), preço nunca no JS, `<style>` penúltimo e `<script>` último, nada de Gutenberg, e as travas de `wpautop`. Ver `references/components.md` e `references/styles-and-scripts.md`.

---

## Checklist de entrega (além dos checkpoints comuns)

- [ ] FASE P0 rodada e a causa nomeada (conteúdo / ângulo / title-meta / canibalização)
- [ ] Decisão de URL registrada (manter × 301) com o contraponto anotado
- [ ] Eixo (P4) é de nível 1-2 de defensibilidade e passa no teste do eixo
- [ ] Teste de substituição **por produto** rodado seção a seção
- [ ] `consultar_pillars_proibicoes` e `consultar_overlaps_doorway` consultados
- [ ] Nenhum detalhe de cidade no pillar — só âmbito nacional + link
- [ ] P9 tem as **duas** listas (compensa / não compensa)
- [ ] `checkpoint_completude.py <arquivo> pillar` ✅
- [ ] `checkpoint_voz.py` ✅ (em pillar, rodar com `--rigor alto`)
- [ ] `checkpoint_onpage.py` ✅ e `checkpoint_citabilidade.py` ✅
- [ ] Registro no banco: `registrar_artigo_novo`/`registrar_atualizacao`, links, FAQs, âncoras
