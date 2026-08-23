# PESQUISA FASE 0 — COMO CONTRATAR HAPVIDA (pillar de tema, P1-P9)

- **Alvo:** https://tabelaplanos.com.br/como-contratar-hapvida/ (WP ID 37416 · Supabase artigo id 64)
- **Arquétipo:** Pillar de TEMA/PROCESSO (P1-P9, com P2 e P5 encolhidos) — nacional, não geográfico
- **Skill:** hapvida-article-builder-v7 (ordem preço-primeiro v7.1)
- **Coleta:** 23/08/2026
- **Natureza do trabalho:** OTIMIZAÇÃO de pillar existente — a FASE P0 (diagnóstico) é obrigatória e vem antes.

---

## 0. FASE P0 — DIAGNÓSTICO DO PILLAR EXISTENTE

Quatro coletas, nenhuma opinião (`artigo-pillar-produto.md` → FASE P0).

### 0.1 A página rende? (GSC, 28 dias: 26/07 a 22/08/2026)

Fonte: `gsc_queries_for_page` + `gsc_custom_query`, propriedade `sc-domain:tabelaplanos.com.br`.

| Métrica | Valor |
|---|---|
| Consultas distintas | 93 |
| Impressões somadas | ~251 |
| **Cliques** | **0** |
| **CTR** | **0,00%** |
| Posição média das consultas de cabeça | 8,5 a 12 |

**Zero clique em 93 consultas.** Não é ruído de amostra pequena numa consulta — é o comportamento de todas.

Consultas de cabeça (posição 5-15 + impressão — as "quase lá" da Fase 5):

| Consulta | Impr. | Posição |
|---|---|---|
| contrate online hapvida + hapvida contrate online | 26 | 9,8 / 10,5 |
| contratar hapvida | 18 | 11,9 |
| **hapvida joinville documentos mei** | **12** | **5,1** |
| documentos hapvida + hapvida documentos | 16 | 8,5 / 10,5 |
| hapvida contratação | 10 | 10,8 |
| hapvida contratar | 9 | 11,1 |
| como fazer um plano de saúde hapvida | 6 | 12,2 |
| como fazer plano hapvida | 6 | 11,8 |
| contratar plano hapvida | 7 | 24,1 |
| fazer plano hapvida | 5 | 30,2 |

### 0.2 Quem ranqueia pela keyword-alvo? (canibalização)

Fonte: `serp_local` — keyword "como contratar hapvida", location_code 2076, pt, mobile, depth 20, coletado 23/08/2026 00:31 UTC.

| Pos. abs. | Domínio | Observação |
|---|---|---|
| 1 | **AI Overview** | a SERP tem resumo de IA |
| 2 | contrate-online.hapvida.com.br | portal oficial |
| 3 | planos-saude.hapvida.com.br | oficial |
| 4 | www2.hapvida.com.br/seja-cliente | oficial |
| 5 | People Also Ask | 4 perguntas |
| 6 | saudedigital.hapvida.com.br | oficial |
| 8 | carmelseguros.com.br | corretora |
| 9-10 | www2.hapvida.com.br (individuais / home) | oficial |
| **11** | **tabelaplanos.com.br/como-contratar-hapvida/** | **nosso — página 2** |
| 12 | www2.hapvida.com.br/vendas | oficial |
| 13 | gndi.com.br | oficial |
| 15 | planosdesaude.org | corretora |
| 16 | youtube.com | vídeo (2020) |
| 17 | valcorretora.com.br | corretora — atualizada **há 3 dias** |
| 18 | amigaosaude.com.br | corretora (adesão) |

**Canibalização: NÃO.** Só uma URL do site na SERP. A home não disputa esta keyword.

**O que a SERP diz:** 7 das 14 URLs orgânicas são domínios da própria Hapvida. A intenção "como contratar hapvida" é, em boa parte, **navegacional para o portal oficial** — existe um teto real para uma corretora nas 4 primeiras posições. A disputa viável é a faixa 8-15, hoje ocupada por corretoras.

**Snippet:** não há featured snippet nesta SERP (`is_featured_snippet: false` em todos). Há **AI Overview** — o formato que importa aqui é passagem citável autocontida, não caixa de destaque.

### 0.3 Quanta autoridade interna a página tem?

Fonte: `consultar_saturacao_destinos`.

- `como-contratar-hapvida` → **26 backlinks internos · classificação SATURADO**. É o 6º destino mais linkado do site.
- **Decisão de URL: MANTER `/como-contratar-hapvida/`. Não fazer 301.** Trocar slug jogaria fora 26 links internos acumulados. Contraponto registrado: o slug não contém "plano", que aparece em várias consultas ("como fazer o **plano** hapvida"); ainda assim o custo do 301 supera o ganho marginal do slug.
- Achado colateral: existe um destino `como-contratar-plano-hapvida` com 1 backlink — slug diferente do real. Provável link interno apontando para URL inexistente. **Pendência a propor** (não é escopo deste artigo).

### 0.4 O que o banco já diz dela?

Fonte: `consultar_artigo` (slug como-contratar-hapvida) e `consultar_pillars_proibicoes`.

- Registro Supabase: `tipo: pillar_processo`, status publicado, `observacoes: "S7 linka; SATURADO — não duplicar docs/steps"`.
- Campos vazios no banco: `h2s`, `faqs`, `produtos`, `versao`, `data_atualizacao`, `titulo_seo`. **O banco não tem o conteúdo desta página mapeado** — precisa ser preenchido no registro pós-aprovação.
- `links_saida` registrados: 5 (notrelife-sp-rj, plano-empresarial-hapvida, plano-mix-hapvida, tabela-de-preco-hapvida, portabilidade-para-hapvida) — mas o HTML tem 10 destinos. Banco desatualizado.

### 0.5 Medição do artigo atual (HTML real, obtido via MCP WordPress, id 37416)

| Item | Piso pillar | Alvo | **Atual** | Situação |
|---|---|---|---|---|
| Palavras de corpo | 2.500 | 3.500-4.500 | **2.265** | abaixo do piso |
| `<h2>` | 8 | 9 | 9 | ok |
| `<h3>` | 15 | 22-28 | **2** | muito abaixo |
| FAQ (`<details>`) | 12 | 15-17 | **10** | abaixo |
| Links internos únicos | 8 | 12-16 | 10 | limítrofe |
| Links externos | 2 | 3-4 | **0** | ausente |
| **Shortcodes de preço** | 3 | conforme praças | **0** | **ausente** |
| `[elementor-template]` | 2 | 3 | 3 | ok |
| `destaque-laranja-suave` | — | ~19 | 9 | abaixo |
| `<figure>` / imagem | 1 | 1 | **0** | ausente |
| Dados de nível 1-2 | 3 | 5+ | **0** | ausente |
| `[ano_atual]` | — | — | 0 (usa "2026" fixo no title) | fere a Regra 5b |
| Meta title Rank Math | — | — | **vazio** | ausente |
| Meta description Rank Math | — | — | **vazio** | ausente |

Saída do `checkpoint_completude.py como-contratar-hapvida pillar`: falha em FAQ (10<12), palavras (2265<2500) e H3 (2<15).
Saída do `checkpoint_preco_primeiro.py ... pillar`: 6 erros — nenhuma tabela de preço no artigo e 5 H2 de outro assunto antes do único H2 de preço.

### 0.6 VEREDITO DA P0 — a causa, nomeada

A causa é **conteúdo + ângulo**, com um agravante de **title/meta**, e **não** é canibalização.

1. **Conteúdo:** o artigo está abaixo do piso do arquétipo pillar em palavras, H3 e FAQ, e não tem uma única linha de preço — numa SERP cujas buscas relacionadas são todas de preço (§2.2). Ele responde "quais documentos levar" e não responde "quanto vai custar e por qual porta entrar".
2. **Ângulo:** o texto trata contratação como um processo burocrático linear. A decisão que muda dinheiro — **por qual modalidade contratar** — aparece só como observação solta na Dica DRV.
3. **Title/meta (agravante, não causa raiz):** os campos Rank Math estão **vazios**; o Google está montando o snippet a partir do meio do corpo ("O plano empresarial Hapvida aceita contratação a partir de 2 vidas..."). O title tem **"2026" fixo**, contra a Regra 5b. Mas em posição 11 (página 2) o CTR seria próximo de zero de qualquer forma — corrigir meta sem corrigir posição não resolve.

---

## 1. DR1 — COLETA

### 1.1 SERP real
Ver §0.2. Coletada com `serp_local` (mobile, Brasil, 23/08/2026). Formato de snippet: **sem featured snippet; com AI Overview**.

### 1.2 Rede / âmbito nacional (dado canônico)
Fonte: `consultar_dados_canonicos` (Supabase).

| Chave | Valor | Fonte registrada |
|---|---|---|
| hospitais_proprios | 86 | Confirmado fev/2026 |
| hospitais_credenciados | 168 | Refeito 2026-05-15 |
| beneficiarios | 15,9 milhões | Dados oficiais 2026 |
| pas_24h | 80 | Base validada + decisão do dono 22/07/2026 |
| estados | 16 | idem |
| programas_qualivida | 11 | Pillar Qualivida |

**Uso neste artigo:** mínimo. Pillar de processo não descreve rede — no máximo 1 menção de âmbito ("16 estados") para situar onde a contratação é possível, com link. Rede é território dos artigos de cidade.

### 1.3 Contexto — onde a contratação é possível
A Hapvida opera em **16 estados** (dado canônico). O artigo NÃO desce a detalhe de cidade (trava do arquétipo pillar) — cita o âmbito e linka para o hub de cidades (`/hapvida-cidades/`) e para 2-3 artigos de cidade.

### 1.4 Keywords com volume real

`keyword_data` e `related_keywords` do DataForSeo retornaram **items_count: 0** para "como contratar hapvida" (a base Labs não tem volume para essa cauda em pt-BR). Registro honesto: **não há volume DataForSeo para a keyword principal.**

**Substituto usado — e melhor:** dado real de impressão do próprio Search Console (§0.1), que mede a demanda que já chega nesta URL. Volume estimado é previsão; impressão é o que aconteceu.

### 1.5 PAA e buscas relacionadas (da SERP coletada)

**People Also Ask (4):**
1. Como contratar o convênio Hapvida?
2. **Qual é o valor do plano Hapvida particular?**
3. O plano Hapvida cobre cirurgia de hérnia?
4. Como conseguir o contrato da Hapvida?

**"Outras pessoas pesquisaram" (12, deduplicadas):**
Hapvida plano individual preço · Contratar Hapvida online · Plano de saúde Hapvida preço · Hapvida plano familiar preços · Valor do plano da Hapvida Infantil · Plano Hapvida Belém preços · Hapvida simulação · Tabela de preços Hapvida 2026 · Plano de saúde Hapvida NotreDame · Hapvida plano individual preço 2026 · Plano individual Hapvida · Hapvida tabela de preços por idade.

**Leitura:** 10 das 12 buscas relacionadas e 1 das 4 PAA são de **preço**. O Google associa "como contratar hapvida" a "quanto custa hapvida" — e o artigo atual não tem preço.

### 1.6 QUERY FAN-OUT [V6] — 5-10 sub-perguntas classificadas

Sub-consultas que uma busca com IA provavelmente gera a partir de "como contratar hapvida". **Não são as PAA** (essas estão em §1.5).

| # | Sub-pergunta | Classificação | Onde resolve |
|---|---|---|---|
| 1 | Quanto custa contratar o Hapvida? | **aqui** | P3↑ — tabela por modalidade |
| 2 | Qual a diferença de preço entre individual e empresarial? | **aqui** | P3↑ + P4 (o eixo) |
| 3 | Quais documentos preciso? | **aqui** | P5 (PF) e P6 (PJ/MEI) |
| 4 | Dá para contratar sozinho pelo site da Hapvida? | **aqui** | P2 — as 3 portas de entrada |
| 5 | MEI pode contratar? Precisa de quanto tempo de CNPJ? | **aqui** | P6 + FAQ |
| 6 | Quanto tempo até o plano ficar ativo? | **aqui** | P7 |
| 7 | Preciso declarar doença preexistente? | **aqui (resumido)** + link | bridge → `/doenca-preexistente-plano-de-saude/` |
| 8 | Quais as carências depois de contratar? | **cluster** | bridge 1-2 frases → pillar Carências |
| 9 | Quanto custa na minha cidade? | **cluster** | link → `/hapvida-cidades/` e artigos de cidade |
| 10 | Como contratar por adesão (sindicato/conselho)? | **aqui (curto)** + **pendência** | P2 + FAQ; artigo próprio de adesão é pauta |

Trava respeitada: sub-pergunta sem resposta própria vira link, não seção inflada com conteúdo nacional de outro pillar.

---

## 2. CI-1 — DESMONTAGEM DE CONCORRENTES

> ⚠️ **LIMITAÇÃO DECLARADA.** O `web_fetch` das páginas concorrentes **não pôde ser executado**: o proxy de egresso deste ambiente bloqueia todos os domínios externos (testado em `valcorretora.com.br`, `planosdesaude.org` e no próprio `tabelaplanos.com.br`). A desmontagem página a página da v4 **não foi feita**. O que segue é reconstruído de (a) metadados da SERP — título, descrição, trecho destacado, data — e (b) `ranked_keywords` do concorrente, que é ferramenta da própria skill. **Isto é um CI-1 parcial e está registrado como tal.**

### 2.1 Matriz de cobertura (a partir dos metadados de SERP)

| Concorrente | Pos. | O que o snippet revela que cobre | Data | Fraqueza aparente |
|---|---|---|---|---|
| carmelseguros.com.br | 8 | "entrar em contato com um consultor via WhatsApp, Formulário ou Telefone" | — | é uma página de **dúvida avulsa**, não guia; resposta é "fale conosco" |
| planosdesaude.org | 15 | lista de documentos: RG/CPF, certidão, comprovante | — | cobre só documentos; recorte de SP |
| valcorretora.com.br | 17 | "definir a modalidade (Individual, Adesão ou Empresarial)" | **há 3 dias** | recência alta; **é o único que abre pela modalidade** |
| amigaosaude.com.br | 18 | adesão via administradora de benefícios | 27/11/2025 | cobre só adesão; desatualizado |
| YouTube (Compare) | 16 | vídeo de contratação | 2020 | 6 anos; 1,7 mil views |

### 2.2 Portfólio do concorrente mais forte (`ranked_keywords`, valcorretora.com.br, Brasil, top 40 por volume)

Das 40 keywords de maior volume do domínio, **26 são de preço/tabela** e apontam para `/tabelas-planos-de-saude` e `/tabelas-comparativas-de-precos-planos-de-saude`:

- "tabela de preços dos planos de saúde" (6.600) · "valores plano de saude" (3.600) · "preço de planos de saúde" (2.900) · "plano de saude tabela de preço" (6.600) · "cotação plano de saúde" (2.900, pos 17) · "plano de saúde hapvida valores" (2.400) · "hapvida plano individual preço" (1.900)…
- A página deles de **"como contratar hapvida" não aparece no top 40** — é página de cauda, sem autoridade própria.

**Conclusão do CI-1:** o concorrente que mais cresce nesta vertical **não vive de "como contratar" — vive de tabela de preço**. Ele ranqueia em "como contratar" por tabela, não o contrário.

---

## 3. CI-2 — MUST-MATCH, BRECHAS E GANHO DE INFORMAÇÃO

### 3.1 MUST-MATCH (o que todo concorrente cobre — não podemos faltar)
1. Passo a passo da contratação (cotação → documentos → declaração → ativação)
2. Lista de documentos PF (titular e dependentes)
3. Lista de documentos PJ/MEI
4. Declaração de saúde e o que acontece ao declarar doença preexistente
5. Prazo de ativação
6. As modalidades de contratação (Individual, Empresarial, Adesão)
7. Formas de pagamento

*(1 a 5 e 7 o artigo atual já cobre. O item 6 está fraco — é exatamente onde o valcorretora abre.)*

### 3.2 BRECHAS (o que todos cobrem mal ou ninguém cobre)
| # | Brecha | Evidência |
|---|---|---|
| B1 | **Ninguém dá preço na página de "como contratar"** | nenhum snippet da SERP traz valor; 10 das 12 buscas relacionadas são de preço |
| B2 | **Ninguém quantifica a diferença entre as modalidades** | valcorretora só *nomeia* as três (snippet) |
| B3 | **Ninguém explica o que o portal oficial NÃO resolve** | 26 impressões nossas em "contrate online hapvida", pos ~10, e a resposta hoje é 1 frase de FAQ |
| B4 | **MEI é tratado como nota de rodapé** | 17 impressões no cluster MEI, com "hapvida joinville documentos mei" em **posição 5,1** — a melhor posição da página inteira |
| B5 | Adesão praticamente ausente | "o que é plano por adesão" pos 18; "plano coletivo por adesão" pos 3 |

### 3.3 GANHO DE INFORMAÇÃO — a UMA coisa que nenhum concorrente diz

> **A porta pela qual você entra vale mais do que qualquer documento que você junte.**
> A mesma pessoa, na mesma idade e na mesma cidade, paga valores diferentes conforme contrate como pessoa física, por CNPJ (inclusive MEI, a partir de 2 vidas) ou por adesão. Essa escolha é feita no primeiro minuto — antes de qualquer papel — e é a única etapa da contratação que não dá para desfazer depois sem cumprir carência de novo.

**Por que é ganho e não lugar-comum:** os concorrentes *nomeiam* as três modalidades; nenhum coloca o número de cada uma lado a lado. Nós temos os três números por praça no plugin de preços do site.

### 3.4 DEFENSIBILIDADE DO DADO [V6] — nível de cada dado do ganho

| Dado | Nível | Por quê | Quem mais tem |
|---|---|---|---|
| Valor de entrada Individual × Empresarial × Adesão, por praça (shortcodes do plugin) | **1 — proprietário** | é a tabela vigente da corretora, renderizada pelo site | ninguém |
| O que trava a contratação na prática (CNPJ < 6 meses, comprovante vencido, inclusão fora dos 30 dias) | **2 — derivado de operação** | vem de contratos implantados pela DRV | ninguém |
| Quais dúvidas de contratação mais chegam (cluster MEI, "contrate online") | **2 — derivado de operação** | GSC próprio + atendimento | ninguém |
| Dados canônicos Hapvida (86 hospitais, 16 estados) | 4 — público trabalhoso | consolidado no banco | quem tem paciência |
| RN 432/2017, Lei 9.656/98, prazos ANS | 5 — público e fácil | a IA responde sozinha | todo mundo |

**Contagem de nível 1-2 planejada para o artigo: 5** (piso é 3). ✅
**O ganho de informação sai de nível 1-2.** ✅ (não de nível 4-5 — a trava do CI-2 está satisfeita)

---

## 4. DR2 — POSICIONAMENTO

### 4.1 KIT ON-PAGE [V5] — matriz de posicionamento

**Keyword principal:** `como contratar hapvida`

| Posição | Conteúdo planejado |
|---|---|
| URL (slug) | `/como-contratar-hapvida/` — **mantida** (contém a principal) |
| H1 | Como Contratar Hapvida: as 3 Portas de Entrada, o Preço de Cada Uma e os Documentos |
| Title SEO | `Como Contratar Hapvida [ano]: 3 Modalidades, Preço e Documentos` (`%currentyear%` no Rank Math) |
| Meta description | contém a principal 1× + o ganho de informação |
| 1º parágrafo (Lead GEO) | contém a principal |
| ≥1 H2 | "Quanto custa contratar o plano Hapvida" (principal por variação) + "Como contratar sendo MEI ou empresa" |

### 4.2 Secundárias — com VETO DE INTENÇÃO (mín. 6; 8 qualificadas)

| # | Keyword secundária | Impressões GSC (28d) | Posição | Intenção | Veredito | Onde entra | cluster_candidata |
|---|---|---|---|---|---|---|---|
| 1 | contrate online hapvida / hapvida contrate online | 26 | 9,8 / 10,5 | comercial-navegacional | **qualificada** | H2 das portas de entrada (P2) + FAQ | não |
| 2 | documentos hapvida / hapvida documentos | 16 | 8,5 / 10,5 | informacional de compra | **qualificada** | H2 de documentos PF (P5) | não |
| 3 | documentos mei plano de saúde hapvida (+ joinville, goiânia) | 17 | 5,1 a 8 | comercial | **qualificada** | H2 de PJ/MEI (P6) | **sim — spoke "plano de saúde MEI Hapvida: documentos"** |
| 4 | contratar hapvida / hapvida contratar | 27 | 11,9 / 11,1 | transacional | **qualificada** | H1, lead, conclusão | não |
| 5 | como fazer plano hapvida / como fazer um plano de saúde hapvida | 19 | 11,8 / 12,2 | transacional | **qualificada** | H2 do passo a passo (P7) | não |
| 6 | valor plano de saúde hapvida / valor do plano por idade | 3 | 1,0 | comercial | **qualificada** | H2 de preço (P3↑) | não (já é o pillar Tabela) |
| 7 | declaração de saúde hapvida | 1 | 1,0 | informacional de compra | **qualificada** | H2 da declaração (P8) | **sim — já existe `/doenca-preexistente-plano-de-saude/`: linkar, não criar** |
| 8 | plano coletivo por adesão / o que é plano por adesão | 2 | 3 / 18 | informacional de compra | **qualificada** | P2 + FAQ | **sim — spoke "Hapvida por adesão"** |

**Descartadas pelo veto de intenção** (volume sem cliente — quem já é cliente, ou navegacional puro):
`central de vendas hapvida` (pos 1) · `hapvida vendas telefone` (pos 1) · `contato hapvida` · `email sac hapvida` · `adicionar dependente hapvida` · `incluir beneficiario hapvida` · `hapvida contrato` · `exame de sangue no hapvida` · `hapvida araquari / garuva / guapo / onça de pitangui / itirapina` (geo sem rede, pos 19-86).
Atrair esse tráfego incha impressão e mantém o CTR no chão — que é exatamente o problema medido em §0.1.

### 4.3 Formato de snippet [V5]
Não há featured snippet nesta SERP. Há **AI Overview**. Consequência: as passagens de abertura são escritas como **parágrafo autocontido de 40-60 palavras** (formato que AI Overview e Perplexity extraem), e não como lista otimizada para caixa de destaque.

### 4.4 GEO por plataforma [V6]
- **AI Overviews:** presente na SERP-alvo → passagem citável no topo de cada seção CORE + schema.
- **Perplexity:** manter FAQPage no schema (ele usa, mesmo o Google não exibindo) e parágrafos que não dependem do anterior.
- **ChatGPT/Copilot (Bing):** frescor **real** — `dateModified` só muda porque o conteúdo mudou de verdade, e aqui muda.
- **Claude (Brave):** densidade factual — número + fonte + data. É o que os 5 dados de nível 1-2 entregam.
- Medição de citação (`monitor_citacoes_ia`): **não medida** nesta fase. Fica para a Fase 5, D+30. Não estimar.

### 4.5 Diferenciais únicos (mín. 3)
1. **A tabela por modalidade no topo** — individual × empresarial/MEI × adesão, com valor de entrada por praça, saindo do plugin de preços do site. Nenhum concorrente da SERP tem.
2. **O que o Contrate Online resolve e o que não resolve** — responde a 26 impressões que hoje não convertem.
3. **MEI tratado como caminho de primeira classe**, não nota de rodapé — sustentado pela melhor posição da página (5,1 em "hapvida joinville documentos mei").
4. **O veredito de dupla lista (P9)** — para quem cada porta compensa e **para quem não compensa**.

---

## 5. ARQUITETURA PLANEJADA — P1-P9 na ordem v7.1

| Ordem | Seção | H2 | Tipo |
|---|---|---|---|
| 1 | `<figure>` de abertura + **Lead GEO** | — | passagem citável, contém a principal |
| 2 | **P3↑a** | **Quanto custa contratar o plano Hapvida** (`id="precos"`) | H2 de PREÇO + contexto + **TABELA por modalidade** |
| 3 | **SUMÁRIO** (`toc-list` vertical, colado na tabela) | — | 10-11 itens |
| 4 | **P3↑b** | *(sem H2 novo)* | faixa navy + `[elementor-template]` `id="cotacao-1"` + selos + leitura da tabela + H3 coparticipação em valor + **`<figure>` da imagem da tabela por último** |
| 5 | P1 | O que é contratar direto, por CNPJ e por adesão | definição citável 40-60 palavras |
| 6 | P2 | As 3 portas de entrada — e o que o Contrate Online não resolve | brecha B3 |
| 7 | **P4 — EIXO** | Por que a modalidade decide mais que o documento | **o coração** |
| 8 | P5 | Documentos para pessoa física | must-match + secundária 2 |
| 9 | P6 | Como contratar sendo MEI ou empresa | must-match + secundária 3 (brecha B4) |
| 10 | P7 | Passo a passo, prazos e ativação | must-match + secundária 5 |
| 11 | CTA intermediário | — | `[elementor-template]` |
| 12 | P8 | Declaração de saúde e os erros que travam a contratação | must-match + dado nível 2 |
| 13 | FAQ | Perguntas frequentes | 15-17 perguntas |
| 14 | CTA final | — | `[elementor-template]` |
| 15 | P9 | Vale a pena contratar por qual porta? | **duas listas: compensa / não compensa** |

**Nada foi cortado.** Todas as 7 seções do artigo atual permanecem, redistribuídas em P1-P9; o que entra é preço, eixo, portas de entrada e veredito.

### 5.1 A tabela do topo — desenho e trava anti-doorway

⚠️ `consultar_pillars_proibicoes` marca, para `tabela-de-preco-hapvida`: *"Tabela completa de preços por faixa etária empresarial (10 faixas) — NÃO REPRODUZIR"*, e para `plano-individual-hapvida`: *"Tabela completa por faixa etária individual — usar shortcode + link"*.

**Resolução:** a tabela do topo **não é** a tabela de 10 faixas etárias. É um **recorte diferente — por modalidade de contratação**, que é o assunto deste pillar e de nenhum outro:

| Como você contrata | Quem pode | A partir de (BH) | A partir de (Fortaleza) | A partir de (São Paulo) |
|---|---|---|---|---|
| Pessoa física (individual/familiar) | qualquer pessoa | `[belo-horizonte_ind_ambulatorialtotal_0]` | `[fortaleza_ind_ambulatorialtotal_0]` | `[sao-paulo_ind_ambulatorialtotal_0]` |
| CNPJ, a partir de 2 vidas (inclui MEI) | empresa com CNPJ ativo | `[belo-horizonte_emp_ambulatorialtotal_0]` | `[fortaleza_emp_ambulatorialtotal_0]` | `[sao-paulo_emp_ambulatorialtotal_0]` |
| Coletivo por adesão | filiado a entidade de classe | `[belo-horizonte_ade_ambulatorialtotal_0]` | — | `[sao-paulo_ade_ambulatorialtotal_0]` |

Isso satisfaz as três coisas ao mesmo tempo: é tabela de preço real no topo (v7 regra 1), não é o recorte por faixa etária que pertence aos outros pillars (anti-doorway por produto), e **é** o eixo do artigo.

**[VERIFICAR]** — confirmar com o admin que cada um dos shortcodes acima renderiza. Confirmados no corpus dos pillars publicados: `belo-horizonte_ind_ambulatorialtotal_0`, `belo-horizonte_emp_ambulatorialtotal_0`, `belo-horizonte_ade_ambulatorialtotal_0`, `sao-paulo_ind_ambulatorialtotal_0`, `sao-paulo_ade_ambulatorialtotal`. **Não confirmados:** `fortaleza_ind_ambulatorialtotal_0`, `fortaleza_emp_ambulatorialtotal_0`, `sao-paulo_emp_ambulatorialtotal_0`. Qualquer shortcode que não renderize sai da tabela — **coluna vazia não entra no ar**.

### 5.2 Bridges e links (anti-saturação)

Destinos SATURADOS a usar no máximo 1× e só onde a bridge for obrigatória: `tabela-precos-hapvida-coparticipacao-guia-completo` (56), `plano-de-saude-hapvida-carencia` (52), `tabela-de-preco-hapvida` (44), `plano-empresarial-hapvida` (17), `plano-individual-hapvida` (19).

Destinos SUBUTILIZADOS a priorizar: `convenio-medico-para-mei` (4) · `plano-hapvida-adesao` (12, NORMAL) · `doenca-preexistente-plano-de-saude` · `aplicativo-hapvida` (1) · `hapvida-agora-aceita-caepf` (2) · `cancelamento-plano-hapvida` (1) · `plano-hapvida-joinville` (4) · `plano-hapvida-goiania` (5).

Links externos (hoje 0, mínimo 2): ANS (RN 432/2017 e portabilidade) e Planalto (Lei 9.656/98) — `rel="nofollow noopener"`, `target="_blank"`. Ambos são fonte primária citada no corpo.

---

## 6. FAQ PLANEJADA (15-17) — cruzada contra o catálogo

As 10 perguntas atuais são mantidas (nenhuma some) e revisadas. **Novas, vindas das brechas e do fan-out:**

11. Quanto custa contratar o plano Hapvida? *(PAA #2 — hoje sem resposta na página)*
12. É mais barato contratar como MEI do que como pessoa física? *(brecha B2, eixo)*
13. Consigo contratar sozinho pelo Contrate Online da Hapvida? *(brecha B3, 26 impressões)*
14. Quais documentos o MEI precisa para contratar? *(brecha B4, posição 5,1)*
15. Como funciona a contratação por adesão? *(brecha B5)*
16. Contratei e mudei de ideia — dá para desistir? *(prazo de arrependimento; link cancelamento)*
17. Posso contratar em uma cidade e usar em outra? *(área de abrangência; link)*

Anti-repetição: cruzar com `consultar_faqs_catalogo` antes de fechar o Bloco C. Nenhuma FAQ reproduz o pillar de Carências (máx. 1 menção + link) nem o de Coparticipação.

---

## 7. VALIDAÇÃO ANTI-DOORWAY (teste de substituição POR PRODUTO)

No pillar o teste não troca a cidade — **troca o produto**. Substituí "contratar Hapvida" por "contratar Plano Mix" em cada seção planejada:

| Seção | Continua válida trocando o produto? | Veredito |
|---|---|---|
| P3↑ tabela por modalidade | Não — as três portas e seus preços são da contratação Hapvida | único |
| P1 definição | Não — define as modalidades de contratação, não um produto | único |
| P2 portas de entrada / Contrate Online | Não — o Contrate Online é canal Hapvida | único |
| P4 eixo | Não — o eixo é a comparação de preço entre modalidades, com número | único |
| P5 documentos PF | Parcialmente — mitigado com o que trava na prática (nível 2) | reancorado |
| P6 MEI/PJ | Não — RN 432/2017 + documentos + preço MEI | único |
| P7 prazos | Parcialmente — prazos Hapvida são específicos (48h / 10 dias úteis) | reancorado |
| P8 declaração de saúde | Parcialmente — bridge curto + link, não seção completa | bridge |
| P9 veredito duplo | Não — nenhum concorrente publica para quem não compensa | único |

**Dados únicos contados: 11** (5 de nível 1-2 + 6 de contexto medido). Frases genéricas de operadora ("modelo verticalizado", "atendimento de qualidade", "custo-benefício"): **0 planejadas** — caça-clichê aplicada na redação.

**ANTI-DOORWAY: APROVADO.**

---

## 8. VOZ, IMAGEM E COMPONENTES

- **Voz humana [V6]:** `checkpoint_voz.py --rigor alto` (é pillar). Alvo: zero gerúndio de arremate, zero tríade de adjetivos, zero molde. Regra-mãe: mexer em palavra e ritmo, nunca em fato.
- **Imagem [V6]:** o artigo passa a ter seção de preço → precisa de `<figure>`. **Mas a imagem de `gerar_imagem_artigo.py` é de tabela por faixa etária de UMA praça**, que não é a tabela deste artigo. **Proposta:** usar `<figure>` de abertura (imagem editorial, URL fornecida pelo usuário) e **não** gerar imagem de tabela aqui — a imagem de tabela pertence aos artigos TR e de cidade. Registrar a decisão e o contraponto. **Decisão pendente do usuário.**
- **Componentes (dose 3-5):** `toc-list` vertical (nunca `v5-chips`), `box-row`/cards, `grid2`/`grid3`, faixa navy de conversão, `v5-trust` (selos), `v5-sticky-cta`. Contador animado **proibido em valor de preço**.
- **Número em TEXTO:** todo valor que sustenta passagem citável aparece em `<p>` ou `<table>` — nunca só em gráfico/imagem.

---

## 9. FORBIDDEN_TOKENS

Tokens que **não podem** aparecer no HTML final (rodar `checkpoint_verificar.py`):

FORBIDDEN_TOKENS:
2026:
2025:
telefone
0800
leitos
Contrate Online resolve tudo
cobertura total
melhor plano de saúde do Brasil
sem custo nenhum
garantido
100% de aprovação

*(o ano corrente só entra via `[ano_atual]`; "2026" literal é proibido no corpo. Datas históricas e legislação — Lei 9.656/98, RN 432/2017 — são exceção e não usam o token nu.)*

---

## 10. O QUE FICA FORA E POR QUÊ

- **Detalhe de cidade** (rede, endereço, tabela por bairro): território dos artigos de cidade. Aqui só âmbito + link.
- **Mecânica de coparticipação, carências, reajuste ANS:** bridge de 1-2 frases + link. Proibições confirmadas no banco.
- **Tabela de 10 faixas etárias:** pertence a `/tabela-de-preco-hapvida/` e `/plano-individual-hapvida/`.
- **Comparativo entre operadoras:** armadilha do listicle — não fazer aqui.
- **Métrica de citação em IA:** não medida; fica para a Fase 5.

---

## 11. PENDÊNCIAS A PROPOR AO USUÁRIO (não gravar sem autorização)

1. Link interno apontando para `como-contratar-plano-hapvida` (slug inexistente) — corrigir para `como-contratar-hapvida`.
2. Registro do artigo 64 no Supabase está incompleto (`h2s`, `faqs`, `links_saida` desatualizados).
3. Spoke candidato: "Plano de saúde para MEI Hapvida — documentos e prazo de CNPJ".
4. Spoke candidato: "Hapvida por adesão — como funciona".
5. Preencher `rank_math_title` e `rank_math_description` (hoje vazios).
