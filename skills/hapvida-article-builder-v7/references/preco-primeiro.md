# Ordem Preço-Primeiro — V7 (revisão 7.1)

> Este arquivo **redefine a ordem** que `sections.md`, `tabela-regional-subpages.md`,
> `artigo-pillar-produto.md` e `artigo-hospital.md` descrevem. O conteúdo de cada seção
> continua sendo o que aqueles arquivos dizem — muda **onde** a seção aparece.
> Em caso de conflito de ordem, **este arquivo vence**.

---

## A regra, em uma frase

O primeiro conteúdo depois do Lead GEO é a tabela de preço, **o sumário vem colado nela**, e nenhum H2 de outro assunto aparece antes de um H2 de preço.

---

## [v7.1] O que mudou em relação à v7.0 — e por quê

A v7.0 mandava: tabela → formulário → sumário. Na prática, o que ficava antes do sumário era **quatro blocos de preço seguidos**: a tabela, a imagem da tabela, o bloco navy "A partir de R$…" e o formulário. Medido no artigo de Recife, o efeito foi o oposto do pretendido — *"muito preço logo de cara"* e o índice do artigo empurrado para longe.

**A correção (v7.1), em três linhas:**

1. A **tabela continua em primeiro** — isso não mudou e não está em discussão.
2. O que vem **logo depois dela é o SUMÁRIO**, não mais preço. O leitor recebe o número e, em seguida, o mapa do artigo.
3. O **formulário, o bloco navy, os selos e a análise de preço** vêm depois do sumário; a **imagem da tabela** desce para o **fim** da seção de preço.

**Consequência de HTML:** a seção de preço fica partida em duas `<section>` — `S2↑a` (H2 + contexto + tabela, com `id="precos"`) e `S2↑b` (conversão + análise + imagem) —, com o sumário entre elas. **As duas continuam sendo a mesma S2↑** para numeração, banco e schema. Não renumerar, não criar H2 novo para a segunda metade.

---

## Por que subir a tabela

A intenção de quem chega nas keywords deste site é **comercial-transacional**: "tabela de preço hapvida [cidade]", "plano hapvida [cidade] valor", "quanto custa hapvida". A v6 entregava esse número na 2ª ou 3ª tela, depois de contexto de cidade que o leitor não pediu ainda. Três consequências medidas na prática:

1. **Pogo-sticking** — o usuário volta para a SERP e abre o concorrente que mostrou o número primeiro. O Google lê isso.
2. **Extração por IA** — AI Overviews e Perplexity puxam o que está mais alto e mais estruturado. Tabela abaixo de 1.200 palavras de contexto é tabela que a IA não cita.
3. **Fricção até o formulário** — o `[elementor-template]` mora colado na tabela. Tabela lá embaixo = formulário lá embaixo.

**O que a v7 NÃO afirma:** que subir a tabela sozinho faz ranquear. Ordem é UX e extração, não autoridade. Todo o resto da skill continua sendo o que ganha posição.

---

## O que é "H2 de preço"

| É H2 de preço | Não é |
|---|---|
| Preços, valores, mensalidade, quanto custa | Rede assistencial, hospitais, unidades |
| Tabela de preços, tabela empresarial, tabela individual | Cobertura por bairro |
| Faixa etária (quando o assunto é valor por faixa) | Como contratar, portabilidade, carências |
| Coparticipação **em valor** (quanto se paga por consulta/exame) | Coparticipação **como conceito** — é do pillar, não entra |
| Promoção / desconto vigente | Cenário de saúde, comparativo de operadoras |
| Investimento em saúde (quando abre com a tabela) | Planos disponíveis (produtos), FAQ, conclusão |

**Teste rápido:** se o leitor consegue tirar um número em reais lendo só aquela seção, é H2 de preço.

---

## Ordem por arquétipo

### City (S1-S7) — a mudança maior

| # | V6 | V7.0 | **V7.1 (vigente)** |
|---|---|---|---|
| 1 | Imagem de abertura | Imagem de abertura | Imagem de abertura |
| 2 | Lead GEO | Lead GEO | Lead GEO |
| 3 | Sumário | S2↑ preços + tabela + form | **S2↑a PREÇOS** — H2 de preço + 1 parágrafo de contexto + `[cidade_menortabela]` (`id="precos"`, fecha a `<section>` aqui) |
| 4 | S1 Por que a cidade é diferente | `[elementor-template]` | **Sumário** (`toc-list` vertical) — colado na tabela |
| 5 | S2 Preços + form | Sumário | **S2↑b** — faixa navy de conversão + `[elementor-template id="11215"]` (`id="cotacao-1"`) + selos + análise local de preço + box Importante + H3 bridge coparticipação em valor + **`<figure>` da imagem da tabela (último elemento da seção)** |
| 6 | S3 Planos disponíveis | S1 | **S1** Por que a cidade é diferente |
| 7 | S4 Rede assistencial | S3 | S3 Planos disponíveis |
| 8 | S5 Cobertura por bairro | S4 | S4 Rede assistencial |
| 9 | S6 Cenário de saúde | S5 | S5 Cobertura por bairro |
| 10 | CTA intermediário | S6 | S6 Cenário de saúde |
| 11 | S7 Como contratar | CTA inter | CTA intermediário |
| 12 | FAQ → CTA final → Conclusão | S7 → FAQ → … | S7 → FAQ → CTA final → Conclusão |

**A numeração interna não muda.** A seção de preço continua se chamando S2 (anotada **S2↑**, agora em duas metades `a` e `b`) e mantendo `id="precos"` na primeira; a S1 continua S1 com `id="#por-que-[cidade]"`. Renumerar quebraria o banco, os checkpoints e todos os artigos já publicados. **Muda a ordem de escrita, não o nome.**

**O sumário colado na tabela.** Entre o shortcode da tabela e o `toc-list` não entra nada além da frase de leitura da tabela — **máximo 600 caracteres de texto visível**, medidos pelo checkpoint. O 1º item é "Preços e Investimento" apontando para `#precos`, que fica **acima** dele; o item destacado "Faça uma Cotação" aponta para `#cotacao-1`, que agora fica logo **abaixo**. Âncora que sobe funciona igual à que desce. Contagem de itens: continua 10-11.

**A imagem da tabela é o último elemento da seção de preço.** Não colar a `<figure>` embaixo do shortcode: é a mesma informação duas vezes na primeira tela, e empurra o sumário e o artigo inteiro para baixo. Ela fecha a S2↑b, depois da análise e da coparticipação (ver `imagem-automatica.md`).

**Blocos de entrega (novos):**

- **Bloco A:** Imagem → Lead GEO → **S2↑a (H2 preço + contexto + tabela)** → **Sumário** → **S2↑b (navy + `[elementor-template]` + selos + análise + copart + imagem da tabela)** → S1 → S3
- **Bloco B:** S4 → S5 → S6 → CTA intermediário *(inalterado)*
- **Bloco C:** S7 → FAQ → CTA final → Conclusão → `<style>` → `<script>` *(inalterado)*

### TR (TR1-TR5) — só formaliza

A TR já era image-first. A v7 trava duas coisas:

- **A IMAGEM 1 (empresarial) sobe para antes do sumário.** Ordem **[v7.1]**: TR1 introdução → **TR2 tabela empresarial (H2 + contexto + IMAGEM 1 + leitura)** → **Sumário (5 itens + CTA)** → `[elementor-template]` `id="cotacao-1"` + bridge do pillar empresarial → TR3 tabela individual → TR4 → TR5 → FAQ → form → Conclusão. *(Na TR a `<figure>` **é** a tabela — a regra "imagem por último" da city não se aplica aqui.)*
- **TR2 e TR3 continuam sendo os dois primeiros H2 de conteúdo** — nenhum H2 de "por que a cidade tem esse preço" ou "promoções" pode passar na frente.

Continua valendo a regra da v6: em TR **não** usar shortcode de tabela completa (duplicaria a imagem). O que conta como "tabela no topo" na TR é a `<figure>` com a IMAGEM 1 + os shortcodes de valor pontual (`_0`, `_9`) na leitura da imagem.

### Pillar (P1-P9) — P3 sobe para 1

| # | V6 | **V7.1** |
|---|---|---|
| 1 | P1 O que é + quem pode contratar | **P3↑a Quanto custa** — H2 de preço + contexto + shortcode da tabela |
| 2 | P2 O que a Hapvida vende | **Sumário** (colado na tabela) |
| 3 | P3 Quanto custa | **P3↑b** — formulário + análise de preço + **imagem da tabela por último** |
| 4 | — | P1 O que é + quem pode contratar |
| 5 | — | P2 O que a Hapvida vende |
| 6-11 | P4 eixo → P9 veredito | P4 eixo → P9 veredito *(inalterado)* |

**Cuidado específico do pillar:** a definição citável de 40-60 palavras da P1 é o que alimenta a extração por IA. Ela **não** sobe para dentro da P3↑ — continua na P1, agora em 2º lugar. O que sobe é a tabela, não a definição. Duplicar a definição no topo para "compensar" é repetição e reprova na voz humana.

O **eixo continua em P4** e continua sendo o coração do artigo. Preço em primeiro lugar é ordem de leitura; eixo é o que faz o artigo vencer. Não confundir prioridade de posição com prioridade de importância.

### Hospital (HS1-HS4) — quase nada muda

Artigo de hospital não tem seção de preço própria: preço aparece na **HS4** ("quais planos dão acesso a este hospital"), como chamariz `[cidade_menorvalor]`, e isso é **valor pontual, não tabela**. A regra 1 (tabela primeiro) **não se aplica**.

O que se aplica: **se** o artigo de hospital passar a incluir um shortcode de tabela completa, ele vai para antes do sumário e a regra 2 (H2 de preço na frente) passa a valer. Sem tabela, o `checkpoint_preco_primeiro.py` roda em modo `hospital` e só confere que não há H2 de preço perdido no meio.

---

## Checklist de entrega da v7.1 (soma-se ao da v6)

- [ ] O primeiro shortcode de tabela (ou `<figure>` de tabela, em TR) aparece antes do `toc-list`
- [ ] O primeiro H2 de conteúdo é H2 de preço
- [ ] Nenhum H2 não-preço antes do primeiro H2 de preço
- [ ] **Entre a tabela e o sumário não há formulário, faixa navy, selos, análise nem imagem** (≤600 caracteres de texto visível)
- [ ] `[elementor-template]` `id="cotacao-1"` **depois** do sumário, abrindo a S2↑b
- [ ] **A `<figure>` da imagem da tabela é o último elemento da seção de preço** (não vale para TR, onde a figure é a tabela)
- [ ] Sumário íntegro, vertical, com 1º item apontando para a âncora de preço
- [ ] A seção de preço tem os parágrafos de contexto local — e **falha** no teste de substituição de cidade
- [ ] Nenhuma seção foi cortada; a contagem do `checkpoint_completude.py` fecha igual à da v6
- [ ] `checkpoint_preco_primeiro.py` retorna ✅ APROVADO
