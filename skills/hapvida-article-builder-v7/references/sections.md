# Sections Map — V3 Content Architecture (Fusão Definitiva)

> ## ⚠️ [V7] A ORDEM DESTE ARQUIVO FOI ALTERADA
>
> Na v7, **a S2 (Preços) é a PRIMEIRA seção do artigo** — vem logo depois do Lead GEO e **antes do sumário**. A S1 e todas as demais descem uma posição. **Nenhuma seção foi cortada e a numeração interna (S1…S7) e os `id` não mudaram** — muda só a ordem em que são escritas e renderizadas.
>
> Ordem v7.1: `<figure>` de abertura → Lead GEO → **S2↑a PREÇOS (H2 + contexto + tabela)** → **SUMÁRIO** → **S2↑b (faixa navy + `[elementor-template]` `id="cotacao-1"` + selos + análise de preço + H3 copart + imagem da tabela)** → S1 → S3 → S4 → S5 → S6 → CTA inter → S7 → FAQ → CTA final → Conclusão.
>
> As descrições de conteúdo de cada seção abaixo continuam valendo integralmente. **Para a ordem, `references/preco-primeiro.md` é a fonte da verdade.**

This file describes what each section contains, its ID, background, content type (CORE/BRIDGE),
expected content, and editorial guidelines. For HTML component templates, see `components.md`.

---

## FASES DE EXECUÇÃO

### FASE 1: CONFIGURAÇÃO INICIAL
1. Receber keyword alvo e cidade
2. Ler arquivo de pesquisa (DR1/DR2 da skill de pesquisa, se fornecido)
   - Extrair: dados da cidade, hospitais, concorrentes, produtos disponíveis, PAA, termos LSI
   - Identificar gaps — sinalizar com `[VERIFICAR]`
3. **Consultar Banco de Dados Supabase** (OBRIGATÓRIO):
   - Identificar cluster (RMBH, Grande SP, Triângulo MG, etc.)
   - `consultar_cluster_completo` — puxar todos os artigos, hospitais, pendências e overlaps do cluster
   - `consultar_artigo` — verificar se já existe artigo na cidade alvo
   - `consultar_faqs_catalogo` — listar FAQs já usadas (máx. 1 pergunta estrutural compartilhada com cidades do cluster)
   - `consultar_hospitais_cidade` — listar hospitais cadastrados
   - `consultar_overlaps_doorway` — checar overlaps já catalogados (evitar repetir o mesmo padrão)
   - `consultar_dados_canonicos` + `consultar_coparticipacao` — números oficiais e valores
   - `consultar_saturacao_destinos` — priorizar pillars subutilizadas como destino de link
   - Mapear oportunidades de cross-link para cidades vizinhas/relacionadas
3b. **Ler TODOS os arquivos de pillar pages do projeto** (OBRIGATÓRIO ANTI-DOORWAY):
   - Abrir cada arquivo `.txt` do projeto que corresponda a um pillar que será linkado no artigo (ex: `como_contratar.txt`, `coparticipacao_guia_completo.txt`, `carencias.txt`, `plano_individual_hapvida.txt`, `plano_empresarial_hapvida.txt`, `tabela_de_precos.txt`, `plano_mix.txt`, `nosso_plano.txt`, etc.)
   - Para cada seção BRIDGE planejada, identificar no arquivo do pillar: quais listas, steps, tabelas, checklists, cards e explicações detalhadas ele contém
   - Registrar o que o artigo de cidade NÃO deve reproduzir — nem de forma condensada ou resumida
   - **Regra:** Se o pillar tem checklist de documentos → artigo de cidade NÃO lista documentos. Se o pillar tem steps de contratação → artigo de cidade NÃO repete os mesmos steps com ângulo genérico. Se o pillar tem tabela de prazos → artigo de cidade NÃO reproduz a tabela.
   - **Teste:** "Este parágrafo é basicamente a versão resumida de uma seção do pillar?" → Se sim, é doorway. Reescrever com dado que só faz sentido naquela cidade + link para o pillar.
4. Consultar `references/pillar-pages.md` para saber quais pillars linkar em cada seção
5. Verificar dados coletados e identificar gaps
6. Consultar esqueleto skill para componentes necessários

### FASE 1b: OUTLINE
1. Criar outline ÚNICO — nunca usar template fixo cegamente
2. Incluir no outline:
   - H2 de cada seção (verificados como únicos vs Supabase)
   - Quais PAA serão respondidos no FAQ (com ângulo local)
   - Quais termos semânticos priorizar por seção
   - Quais pillar pages serão linkados (e em qual seção, com URL real)
   - Quais artigos de cidade serão cross-linkados (e em qual seção)
   - O parágrafo 1 do lead (resposta direta à intenção de busca)
   - Lista de FAQ planejadas (verificadas contra banco)
3. Apresentar outline ao usuário para aprovação

**Entregável da Fase 1:** Outline + campo semântico + lista de PAA + produtos locais confirmados + cross-links planejados + lista de pillars lidos com "o que NÃO reproduzir" por seção BRIDGE

**⏸️ PAUSA — Aguardar aprovação do outline**

---

### FASE 2: PRODUÇÃO — BLOCO A (Introdução → Seção 3) — **[V7.1] ordem nova**
Produzir, **nesta ordem**: **Imagem de abertura (`<figure>`)** + Introdução / Lead GEO + **S2↑a PREÇOS (H2 de preço + 1 parágrafo de contexto + shortcode de tabela)** + **Sumário** + **S2↑b (faixa navy + `[elementor-template]` `id="cotacao-1"` + selos + análise local de preço + H3 bridge copart + `<figure>` da imagem da tabela)** + S1 + S3

> **[V7.1] O que mudou no Bloco A:** a S2 saiu do 4º lugar e virou o 1º conteúdo depois do lead; o **sumário vem colado na tabela** (não depois do formulário, como na v7.0), e o formulário abre a segunda metade da seção de preço. A imagem da tabela fecha essa segunda metade. O conteúdo de cada peça é o mesmo — ver a descrição de cada seção mais abaixo. Regra e trava em `references/preco-primeiro.md`.

> **Imagem de abertura — PRIMEIRO elemento do `<article>`, antes do Lead GEO.** Usar o template de `components.md` ("Imagem de Abertura do Artigo"). Personalizar `title`/`alt`/`figcaption` para o tema (são conteúdo único, contam no anti-doorway). A **URL (`src`) é fornecida pelo usuário**; sem ela, deixar `[URL_DA_IMAGEM]` e pedir — nunca inventar URL.

**Aplicar durante redação:**
- Campo semântico do arquivo de pesquisa — distribuir termos LSI e variações da keyword
- Parágrafos com máx. 4 linhas
- Checklist anti-doorway por parágrafo (1 dado específico mínimo)
- Sinais E-E-A-T (credencial DRV no lead, legislação citada)

**⏸️ CHECKPOINT A** (ver abaixo) → **PAUSA — Aguardar aprovação**

### FASE 3: PRODUÇÃO — BLOCO B (Seção 4 → CTA intermediário)
Produzir: S4 + S5 + S6 + CTA intermediário

**Aplicar durante redação:**
- Campo semântico — continuar distribuindo termos
- Dados específicos anti-doorway em cada parágrafo
- Comparativo com critérios locais (não genéricos)
- Cross-links para cidades vizinhas nos pontos naturais

**⏸️ CHECKPOINT B** (ver abaixo) → **PAUSA — Aguardar aprovação**

### FASE 4: PRODUÇÃO — BLOCO C (Seção 7 → Conclusão)
Produzir: S7 + FAQ + CTA final + Conclusão + `<style>` + `<script>`

**Aplicar durante redação:**
- FAQ com 90%+ perguntas locais, mín. 3 derivadas de PAA
- Consultar Supabase (`consultar_faqs_catalogo`) para anti-repetição de FAQ
- Sinais E-E-A-T na conclusão (DRV + fontes)
- Cross-links restantes

**⏸️ CHECKPOINT C FINAL** (ver abaixo) → **PAUSA — Aguardar aprovação**

### FASE 5: PÓS-PRODUÇÃO
Após aprovação de todos os blocos:
1. Teste de substituição de operadora (trocar Hapvida por Unimed — deve quebrar)
2. Teste de substituição de cidade (trocar cidade — deve quebrar)
3. Teste de duplicação (nenhum parágrafo copiável para outro artigo)
4. Gerar Título SEO (máx 60 caracteres)
5. Gerar Meta Description (máx 160 caracteres)
6. Entregar arquivo HTML completo
7. **Registrar no Supabase** via MCP `BD - criar` — `registrar_artigo_novo`, `registrar_faqs_artigo`, `registrar_hospitais_artigo`, `registrar_links_artigo`
8. **Sugerir links recíprocos** — identificar artigos já publicados onde inserir link para o novo, e quais artigos publicados o novo deveria linkar

---

## SEÇÕES DETALHADAS

---

### ── IMAGEM DE ABERTURA ──
- **ID:** none
- **Posição:** PRIMEIRO elemento dentro de `<article>`, imediatamente ANTES da Introdução / Lead GEO
- **Type:** `<figure>` + `<figcaption>` (template em `components.md` → "Imagem de Abertura do Artigo")
- **Personalizar:** `title`, `alt`, `figcaption` para o tema do artigo (conteúdo único — entra no teste anti-doorway). A **URL (`src`) vem do usuário**; sem ela, deixar `[URL_DA_IMAGEM]` e pedir. Manter os estilos inline e a estrutura exatamente como no template.

---

### ── INTRODUÇÃO — LEAD GEO ──
- **ID:** none
- **Background:** white with `border-bottom: 1px solid #e2e8f0`
- **Type:** Special (no H2)

A introdução é o elemento mais importante para **GEO (Generative Engine Optimization)**. Motores de busca e IAs generativas (Google SGE, Bing Copilot, etc.) extraem trechos do lead para gerar respostas diretas. O lead DEVE responder à intenção de busca da keyword alvo de forma objetiva nos primeiros parágrafos.

**Parágrafo 1 — Resposta direta à intenção de busca (GEO snippet):**
- Responder a keyword em 2-3 frases diretas, como se fosse um featured snippet
- Incluir: o que é (Hapvida em [cidade]), quanto custa (shortcode `[cidade_menorvalor]`), e o diferencial principal
- Ex: "A Hapvida em [cidade] oferece planos de saúde a partir de [cidade_menorvalor] por mês, com rede própria que inclui [hospital principal] e [X] unidades na região. A operadora é líder em [região/estado] e opera um modelo verticalizado que combina menor custo com atendimento em estrutura própria."
- Este parágrafo deve funcionar como resposta autossuficiente — se a IA extrair apenas ele, o leitor já terá a informação essencial
- Deve ser CONCISO e FACTUAL — sem adjetivos vazios, sem "Você sabia que..."

**Parágrafo 2 — Contexto local:**
- Dados âncora da cidade: população, economia, perfil de demanda por saúde
- Link externo (IBGE, fonte institucional)
- Texto grifado animado (1-2 ocorrências)

**Parágrafo 3 — Promessa do artigo:**
- O que o leitor vai encontrar no guia (preços, rede, comparativo, como contratar)
- Credencial DRV (1ª menção E-E-A-T, sutil): "Este guia foi preparado pela equipe da DRV Corretora, especialista Hapvida..."

**Regras do lead:**
- Shortcode valor inicial: `[cidade_menorvalor]` em `<strong style="color: #ff6b00;">`
- Parágrafos com máx. 4 linhas cada
- Sem badge, sem emoji
- Sem H2 — funciona como lead

---

### ── SUMÁRIO / NAV ──
- **[V7] Posição:** DEPOIS da S2↑ (Preços) e do 1º `[elementor-template]`. Não é mais o 3º elemento do artigo — é o 5º. Tudo o mais (estrutura, classes, anti-Elementor, contagem de itens) é idêntico.
- **[V7] Primeiro item:** "Preços e Investimento" → `#precos`, que fica **acima** do sumário. Âncora que sobe funciona igual à que desce — não "corrigir" isso movendo a seção de volta.
- **Background:** gradient `#fafbfc → #f0f4f8`
- **Content:**
  - Icon `≡` in orange badge (28×28px) + Title "Neste Guia Você Vai Encontrar"
  - Numbered badges (`toc-badge`) + anchor links
  - **10-11 items** (7 sections + CTA destacado + FAQ + Conclusão)
  - **Item CTA obrigatório:** "Faça uma Cotação" — posicionado após S2 (badge sem número, fundo laranja `#ff6b00`, texto branco, font-weight 800). Link para `#cotacao-1`. Destaca-se visualmente dos demais itens.
  - Uses classes `toc-list`, `toc-item`, `toc-badge`
- **Anti-Elementor rules:**
  1. Pure `<div>` — NEVER `<ol>/<li>`
  2. Header ≡ INSIDE `toc-list` as 1st `toc-item`
  3. Zero blank lines between tags
  4. `!important` inline on all flex properties
  5. `flex-shrink:0!important` on badges
  6. `padding:0!important;margin:0!important` on each `toc-item`
  7. Anti-wpautop in `<style>`: `.toc-list>p,.toc-list>br,.toc-item>p,.toc-item>br{display:none!important}`

---

### ── S1: POR QUE [CIDADE] É DIFERENTE ──
- **[V7] Posição:** 2ª seção (depois da S2↑ e do sumário). Continua se chamando S1 e continua com o mesmo `id` — só desceu. **Nada aqui é cortado ou encolhido por causa da reordenação.**
- **ID:** `#por-que-[cidade]`
- **Background:** `#f8f9fa`
- **Type:** CORE
- **Content:**
  - Standard header (H2 — verificar redação única vs Supabase via `consultar_cluster_completo`)
  - Box "RESUMO RÁPIDO" (badge "R", dados-chave da cidade)
  - 3-4 parágrafos anti-doorway com dados específicos da cidade (4 linhas cada)
  - Cards métricas grid4 (3 cinza + 1 laranja destaque)
  - 1-2 parágrafos finais
  - Box "DICA DRV" (sem badge, apenas label)
  - Texto grifado animado (1-2 ocorrências)
- **Teste de substituição:** Se trocar a cidade e a seção ainda fizer sentido → reescrever.
- **Components:** `box_resposta_rapida`, `cards_estatisticas`, `box_dica_drv`

---

### ── S2↑: PREÇOS E INVESTIMENTO EM SAÚDE ── **[V7] PRIMEIRA SEÇÃO DO ARTIGO**
- **[V7] Posição:** 1ª seção — imediatamente após o Lead GEO, **antes do sumário**. O H2 desta seção é o primeiro H2 do artigo e deve conter a keyword de preço do kit on-page.
- **[V7] Trava extra:** por estar em primeiro lugar, esta é a seção que mais precisa QUEBRAR no teste de substituição — trocar a cidade tem de invalidar a seção. Tabela no topo com contexto genérico é doorway na posição mais visível da página. Os 2 parágrafos de contexto local **não** são opcionais.
- **ID:** `#precos`
- **Background:** white
- **Type:** CORE
- **Content:**
  - Standard header
  - 2 parágrafos contextuais sobre o mercado de preços local (4 linhas cada)
  - **Link para pillar Tabela de Preços** no 1º parágrafo (contextual, anchor descritivo — URL em `pillar-pages.md`)
  - **Shortcode tabela:** `[cidade_menortabela]`
  - Nota rodapé (italic, `#94a3b8`)
  - Box "IMPORTANTE" (badge "!", no emoji)
  - 1 parágrafo final (faixa 59+, copart parcial)

**Subsection: Coparticipação na prática em [Cidade] (H3) — BRIDGE**
- 2 parágrafos com **ÂNGULO LOCAL OBRIGATÓRIO:**
  - Como a copart afeta o custo-benefício nesta cidade (comparar com alternativas locais)
  - Perfil de uso local (rede verticalizada, concentração de consultas na rede própria, etc.)
  - Shortcodes de coparticipação (grupo correto: `sp_bh` ou `demais_capitais`)
- Link interno para pillar page de coparticipação (URL em `pillar-pages.md`)
- Texto grifado animado (1 ocorrência na subsection bridge)
- **PROIBIDO:** Repetir "o que é coparticipação" (está no pillar)
- **PROIBIDO:** Tabela comparativa Total vs Parcial completa (está no pillar)

**Após (FORA da section):**
- **[V7.1] Primeiro o SUMÁRIO**, colado na tabela — fechar a `<section>` logo depois do shortcode de tabela e abrir a do `toc-list`.
- Depois o **S2↑b**: faixa navy de conversão + `[elementor-template id="11215"]` (1º formulário) em `<div id="cotacao-1" style="margin-bottom:4px;">` + selos + a análise local de preço + o H3 bridge de coparticipação + a `<figure>` da imagem da tabela (último elemento).
- A ordem é: H2 de preço + contexto + tabela → **sumário** → conversão/formulário → análise → imagem → S1.
- **Components:** `tabelas`, `box_destaque_azul`

---

### ── S3: PLANOS DISPONÍVEIS EM [CIDADE] ──
- **ID:** `#planos-disponiveis`
- **Background:** `#fff8f3`
- **Type:** CORE

**Dados obrigatórios do arquivo de pesquisa (verificar ANTES de escrever):**
1. Quais produtos Hapvida estão disponíveis na cidade (Nosso Plano, Mix, Pleno, Nosso Médico, etc.)
2. Quais modalidades cada produto oferece (enfermaria, apartamento, ambulatorial)
3. Se há produtos exclusivos da região ou restrições de disponibilidade
4. Se a cidade tem individual/familiar ou apenas empresarial/adesão

**Conteúdo:**
- 1 parágrafo sobre a oferta específica da cidade (4 linhas)
- Cards grid2 ou grid3: **produtos comerciais reais** (NÃO modalidades ANS)
  - Cada card: nome comercial + cobertura + diferencial + "Disponível em [cidade]"
  - Se 2 produtos → grid2. Se 3+ → grid3
  - Badge: sigla do produto (NP, MX, PL, etc.)
- 1 parágrafo sobre tipos de contratação disponíveis nesta cidade
- Box "DICA DRV" — recomendação por perfil considerando o mercado local
- Link para pillar de produto relevante (Nosso Plano, Mix, Individual, Empresarial — URL em `pillar-pages.md`)

**TESTE DE SUBSTITUIÇÃO:** Se trocar o nome da cidade e os cards ainda fizerem sentido → seção falhou.
- **Components:** `cards_modalidades` (adapted for commercial products)

---

### ── S4: REDE ASSISTENCIAL EM [CIDADE] ──
- **ID:** `#rede-[cidade]`
- **Background:** white
- **Type:** CORE

**Conteúdo:**
- 1 parágrafo panorama da rede na cidade (4 linhas)

**Subsection: [Nome do Hospital Principal] (H3)**
- Card hero hospital (borda laranja 2px)
- Linha do tempo (4-5 marcos — aquisição, reformas, expansões)
- 2-3 parágrafos detalhamento (leitos, capacidade, especialidades) (4 linhas cada)
- Texto grifado animado (1-2 ocorrências)

**Subsection: Demais Unidades (H3)**
- Cards grid2: clínicas, laboratórios, centros de diagnóstico
  - Cada card: badge sigla + H3 + endereço real + faixa info
- 1-2 parágrafos finais + link interno para pillar rede própria (URL em `pillar-pages.md`)
- Texto grifado animado (1-2 ocorrências)
- **Ponto de cross-link para cidades vizinhas:**
  - "Pacientes de [cidade vizinha] também utilizam o [hospital] — veja nosso guia de [cidade vizinha]"
  - Verificar quais artigos de cidade vizinha estão publicados via Supabase (`consultar_cluster_completo`)

**REGRAS:**
- Todos os dados (endereços, nomes, capacidade) devem ser verificados. Nenhum dado inventado.
- Se o mesmo hospital aparece em artigo de outra cidade (verificar via `consultar_hospitais_cidade` e `consultar_artigo` no Supabase), usar ÂNGULO DIFERENTE (história vs capacidade vs especialidades vs acesso)
- **Components:** `cards_hospitais`, `linha_do_tempo`

---

### ── S5: COBERTURA POR BAIRRO EM [CIDADE] ──
- **ID:** `#cobertura-bairros`
- **Background:** `#f8f9fa`
- **Type:** CORE
- **Content:**
  - Standard header
  - 1 parágrafo introdutório (4 linhas)
  - Tabela (bairro/regional × unidade mais próxima × tempo estimado)
    - 1ª linha: destaque laranja (bairro principal)
    - Dark gradient header
  - Nota rodapé
  - **Raio-X da Cobertura** (3 níveis: total, urgência, sem cobertura direta)
  - 1-2 parágrafos finais (4 linhas cada)
  - Texto grifado animado (1 ocorrência)
  - **Ponto de cross-link:** "Moradores de [bairro limítrofe] podem considerar as unidades de [cidade vizinha]"
- **Components:** `tabelas`, `raio_x_cobertura`

---

### ── S6: CENÁRIO DE SAÚDE EM [CIDADE] ──
- **ID:** `#cenario-saude`
- **Background:** `#fff8f3`
- **Type:** CORE
- **Content:**
  - Standard header
  - 1-2 parágrafos sobre panorama de saúde da cidade (operadoras atuantes, perfil de demanda, desafios locais) (4 linhas cada)
  - Tabela comparativa (Hapvida vs Concorrente A vs Concorrente B)
    - Coluna Hapvida com header laranja, demais com header escuro
    - Valores Hapvida em laranja + bold
    - **Mínimo 2 critérios relevantes APENAS para esta cidade**
  - 1 parágrafo de análise: o que o comparativo revela sobre o mercado LOCAL
  - Texto grifado animado (1-2 ocorrências)
  - Box "DICA DRV" — orientação baseada no cenário local
  - **Ponto de cross-link para pillar comparativo:** se o concorrente é Unimed ou Amil, linkar para pillar vs Unimed / vs Amil (URL em `pillar-pages.md`)
  - **Ponto de cross-link para cidade vizinha:** "O mercado de [cidade] tem dinâmica semelhante ao de [cidade vizinha]"

**REGRA ANTI-DOORWAY:** Se os critérios de comparação podem ser usados em qualquer cidade → reescrever com ângulo local. Verificar banco: se o mesmo concorrente foi comparado em cidade do cluster, usar CRITÉRIOS DIFERENTES.

- **Components:** `tabelas`

---

### ── CTA INTERMEDIÁRIO ──
- **Background:** none — bare shortcode only
- `[elementor-template id="11215"]` em div simples (`margin-bottom: 4px`)
- Sem H2, sem subtítulo, sem section — o Elementor renderiza o visual
- **Posição:** entre S6 e S7

---

### ── S7: COMO CONTRATAR HAPVIDA EM [CIDADE] ──
- **ID:** `#como-contratar`
- **Background:** `#f8f9fa`
- **Type:** BRIDGE

**Subsection: Portabilidade e Carências em [Cidade] (H3) — BRIDGE**
- 1-2 parágrafos com **ÂNGULO LOCAL OBRIGATÓRIO** (4 linhas cada):
  - Oportunidades de portabilidade na cidade: "Quem tem [concorrente local] em [cidade] pode migrar para a Hapvida aproveitando carências já cumpridas"
  - Contexto local de mercado (concorrentes com reajustes altos, operadoras saindo da cidade, etc.)
  - Link externo ANS + link interno para pillar de carências (URL em `pillar-pages.md`)
  - Link interno para pillar de portabilidade (URL em `pillar-pages.md`)
- **PROIBIDO:** Cards com prazos ANS (24h/30d/180d/300d/24m) — estão no pillar
- **PROIBIDO:** Explicação genérica de "o que é carência" — está no pillar
- Box "PORTABILIDADE" (badge "P") — com dado local
- Texto grifado animado (1 ocorrência na subsection portabilidade)

**Subsection: Passos para Contratar em [Cidade] (H3) — BRIDGE**
- 1 parágrafo com contexto local (documentação, prazos, particularidades) (4 linhas)
- Steps: 3-4 passos com **pelo menos 1 referência local por step:**
  - Ex: "Agende uma consultoria com a DRV Corretora — atendemos [cidade] e região desde [ano]"
  - Ex: "Escolha a unidade mais próxima em [bairro] para a perícia médica, se aplicável"
- Link interno para pillar Como Contratar (URL em `pillar-pages.md`)
- Menção ao app Hapvida em máx. 1 frase (substitui antiga seção de Tecnologia)
- Box "DICA DRV" — dica prática de quem atua no mercado local
- **Ponto de cross-link:** "Quem reside na região metropolitana pode contratar em [cidade vizinha] — confira as opções"
- **PROIBIDO:** Lista de documentos (RG, CPF, CNPJ, comprovante, DPS) — pertence ao pillar Como Contratar
- **PROIBIDO:** Explicação detalhada da Declaração Pessoal de Saúde — pertence ao pillar
- **PROIBIDO:** Prazos genéricos de ativação (48h individual, 10 dias empresarial) como lista — 1 frase contextual no máximo
- **PROIBIDO:** Reproduzir steps genéricos condensados do pillar — cada step DEVE ter dado local exclusivo

**TESTE DE SUBSTITUIÇÃO:** Se trocar a cidade nos steps e no bloco de portabilidade e nada quebrar → seção falhou.

- **Components:** `contadores_steps`, `box_portabilidade`, `box_dica_drv`

---

### ── FAQ ──
- **ID:** `#faq`
- **Background:** white
- **Content:**
  - Orange label "PERGUNTAS FREQUENTES" + H2 + subtitle + bar
  - **12-15 perguntas** em `<details>/<summary>`
  - **90%+ específicas da cidade**
  - Pergunta obrigatória sobre valor com shortcode `[cidade_menorvalor]`
  - **Mínimo 3 perguntas derivadas dos PAA** ("Pessoas Também Perguntam" do Google), adaptadas com ângulo local

**Regras anti-repetição (Supabase):**
1. **Antes de escrever:** consultar Supabase (`consultar_faqs_catalogo`, `consultar_cluster_completo`) para ver quais perguntas já foram usadas em cidades do cluster
2. Máximo 2 perguntas estruturais (valor, como contratar) — o resto deve ser local
3. Cada pergunta deve passar no teste: "Um morador de outra cidade faria essa mesma pergunta?" → Se sim, reescrever com ângulo local ou remover
4. Perguntas sobre coparticipação, carências, tecnologia → resposta breve (2-3 frases) + link para pillar

**Exemplos bons (locais):**
- "A Hapvida atende no bairro [X] em [cidade]?"
- "Qual hospital Hapvida é referência em maternidade em [cidade]?"
- "Quanto tempo leva para ser atendido no pronto-socorro Hapvida de [bairro]?"
- "A Hapvida [cidade] tem plano individual ou só empresarial?"
- PAA adaptado: "Qual o melhor plano de saúde em [cidade]?" → responder com comparativo local, não genérico

**Exemplos ruins (genéricos — PROIBIDOS como pergunta isolada):**
- "O que é coparticipação?" → pillar page
- "Quais são os prazos de carência?" → pillar page
- "O que o app Hapvida oferece?" → irrelevante para decisão local
- "Qual a diferença entre enfermaria e apartamento?" → pillar page

**Ponto de cross-link no FAQ:**
- "A Hapvida [cidade] atende moradores de [cidade vizinha]?" → link para artigo daquela cidade
- "Como se compara a Hapvida com a [operadora] em [cidade]?" → link para pillar vs Unimed/Amil se aplicável

- **Components:** `faq`

---

### ── CTA FINAL ──
- **Background:** none — bare shortcode only
- `[elementor-template id="11215"]` em div simples (`margin-bottom: 4px`)
- Sem H2, sem subtítulo, sem section
- **Posição:** entre FAQ e Conclusão

---

### ── CONCLUSÃO ──
- **ID:** `#conclusao`
- **Background:** gradient `#f8fafc → #f1f5f9` with `border-top: 1px solid #e2e8f0`
- **Content:**
  - Standard header (H2 com frase-resumo impactante)
  - Cards métricas conclusão grid4: 4 dados-chave finais (white bg, border, shadow)
  - 2 parágrafos conclusivos (4 linhas cada): recapitulação + CTA textual com shortcode valor
  - CTA textual enfatizando DRV Corretora (especialista Hapvida) — 2ª menção E-E-A-T
  - Nota rodapé: fontes, data atualização usando `[mes_atual] de [ano_atual]` — itálico, `#94a3b8`
  - Disclosure: "Preços sujeitos a alteração. Consulte condições atualizadas."
- **Components:** `conclusao_gradiente_cinza`

---

## CHECKLISTS DE ENTREGA

### ⏸️ CHECKPOINT A (Intro → Seção 3):
```
[ ] Lead GEO: parágrafo 1 responde diretamente à intenção de busca?
[ ] Lead GEO: parágrafo 1 inclui [cidade_menorvalor] + hospital principal + diferencial?
[ ] Lead GEO: parágrafo 1 funciona como resposta autossuficiente para IA generativa?
[ ] Backgrounds alternados corretos? (cinza → branco → laranja)
[ ] Coparticipação é subsection da S2 (NÃO seção própria)?
[ ] Coparticipação tem ângulo local (NÃO explicação genérica)?
[ ] Coparticipação NÃO reproduz conteúdo condensado do pillar coparticipação (verificado contra arquivo do projeto)?
[ ] Link para pillar de coparticipação presente (URL correta)?
[ ] Link para pillar tabela de preços presente na S2 (URL correta)?
[ ] S3 lista produtos comerciais reais (NÃO modalidades ANS)?
[ ] Produtos da S3 verificados como disponíveis na cidade?
[ ] Link para pillar de produto na S3?
[ ] [elementor-template] FORA da section após S2?
[ ] Shortcodes corretos ([cidade_menorvalor] para valor, [cidade_menortabela] para tabela)?
[ ] Texto grifado: __/10 (mínimo 10 no artigo todo)
[ ] Links internos: __ (mín. 2 para pillar, 150+ palavras entre links)
[ ] Cross-links para cidades: __ planejados
[ ] Sumário com IDs corretos (7 seções + FAQ + Conclusão)?
[ ] Parágrafos 4 linhas max?
[ ] Nenhum emoji em nenhum componente?
[ ] Campo semântico aplicado? (variações da keyword, termos LSI presentes)
[ ] E-E-A-T: credencial DRV no lead (1ª de máx. 3)?
[ ] E-E-A-T: legislação/fonte citada?
[ ] H2s verificados como únicos vs Supabase (`consultar_cluster_completo`)?
```

### ⏸️ CHECKPOINT B (Seção 4 → CTA intermediário):
```
[ ] S4 tem linha do tempo do hospital principal?
[ ] S4 tem cards com endereços reais verificados?
[ ] S4 hospital com ângulo diferente de artigo de outra cidade (verificar Supabase via `consultar_hospitais_cidade` + `consultar_artigo`)?
[ ] S4 cross-link para cidade vizinha (se infraestrutura compartilhada)?
[ ] S5 tem tabela bairro × unidade × tempo?
[ ] S5 tem Raio-X da cobertura?
[ ] S5 cross-link para cidade vizinha (se bairro limítrofe)?
[ ] S6 tem comparativo com pelo menos 2 critérios exclusivos da cidade?
[ ] S6 critérios diferentes dos usados em cidades do cluster (verificar Supabase)?
[ ] S6 tem parágrafo de análise do mercado local (não só tabela)?
[ ] S6 link para pillar comparativo (vs Unimed / vs Amil) se aplicável?
[ ] [elementor-template] em div simples entre S6 e S7?
[ ] Texto grifado: __/10 total
[ ] Parágrafos 4 linhas max?
[ ] Nenhum emoji?
[ ] Campo semântico: termos LSI distribuídos neste bloco?
```

### ⏸️ CHECKPOINT C — FINAL (Seção 7 → end):
```
[ ] S7 tem ângulo local de portabilidade (NÃO explicação genérica)?
[ ] S7 NÃO tem cards de prazos ANS (24h/30d/180d/300d/24m)?
[ ] S7 tem pelo menos 1 referência local em cada step de contratação?
[ ] S7 NÃO lista documentos (RG/CPF/CNPJ/comprovante/DPS) — pertence ao pillar Como Contratar?
[ ] S7 NÃO reproduz steps genéricos condensados de nenhum pillar (Como Contratar, Carências, etc.)?
[ ] S7 link para pillar Como Contratar presente (URL correta)?
[ ] S7 menciona app Hapvida em máx. 1 frase?
[ ] Links para pillar de carências + portabilidade presentes (URLs corretas)?
[ ] S7 cross-link para cidade vizinha (região metropolitana)?
[ ] ANTI-DOORWAY PILLAR: cada seção BRIDGE cruzada contra arquivo do pillar no projeto — nenhum conteúdo condensado?
[ ] FAQ 12-15 perguntas, 90%+ específicas da cidade?
[ ] FAQ inclui mín. 3 perguntas derivadas dos PAA (com ângulo local)?
[ ] FAQ cruzado com Supabase via `consultar_faqs_catalogo` (sem repetição de cidades do cluster)?
[ ] FAQ cross-link para cidade vizinha em pelo menos 1 pergunta?
[ ] Pergunta de valor com [cidade_menorvalor]?
[ ] CTA final em div simples + [elementor-template]?
[ ] Conclusão com métricas (fundo gradiente cinza, NÃO azul)?
[ ] CTA textual com DRV Corretora (2ª menção E-E-A-T)?
[ ] Nota rodapé com fontes e data?
[ ] Disclosure presente ("Preços sujeitos a alteração")?
[ ] <style> é penúltimo, <script> é último?
[ ] TOTAL texto grifado: __/10 (mínimo 10)
[ ] TOTAL [elementor-template]: 3 (pós-tabela + CTA inter + CTA final)
[ ] Nenhum emoji em nenhum componente?
[ ] Parágrafos 4 linhas max?
[ ] E-E-A-T: máx. 3 menções DRV no artigo todo? (lead + conclusão + 1 Dica DRV)
[ ] E-E-A-T: legislação/resolução ANS citada pelo menos 1x?
[ ] Links internos: __/5+ total (pillars mín. 3 + cidades mín. 2, mín. 150 palavras entre links)?
[ ] Cross-links para artigos de cidade: __/2+ total?
[ ] Links externos: __/2+ (fontes diversificadas, rel="nofollow noopener", máx. 3/domínio)?
[ ] Campo semântico: variações da keyword distribuídas por todo o artigo?
[ ] H2s todos únicos vs Supabase?
```

### PÓS-PRODUÇÃO (após todos os blocos aprovados):
```
1. Teste substituição operadora (Hapvida → Unimed) — deve quebrar
2. Teste substituição cidade — deve quebrar
3. Teste duplicação — nenhum parágrafo copiável para outro artigo
4. Título SEO (máx. 60 caracteres)
5. Meta Description (máx. 160 caracteres)
6. Entregar HTML completo
7. Registrar no Supabase (`registrar_artigo_novo`, `registrar_faqs_artigo`, `registrar_hospitais_artigo`, `registrar_links_artigo`)
8. Sugerir links recíprocos (em artigos já publicados + no novo artigo)
```
