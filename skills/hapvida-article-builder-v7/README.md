# hapvida-article-builder-v7 — PREÇO PRIMEIRO + MULTI-AGENTES EM MODELOS DIFERENTES

Skill para produção de artigos HTML para tabelaplanos.com.br.

**Só dispara sob pedido explícito.** Gatilhos: `v7`, `versão 7`, `builder v7`, `preço primeiro`, `tabela primeiro`, `ordem preço-primeiro`, `sumário depois da tabela`, `H2 de preço primeiro` — e, para a camada v7.2: `multi-agente`, `modelos diferentes`, `qual modelo`, `roteamento de modelo`, `plano de modelos`, `agente barato`, `modelo forte`, `custo da linha`, `juiz em outro modelo`, `erro correlacionado`, `monomodelo`. Sem isso, use v1-v6 — as sete coexistem para comparação.

> ## ⭐ V7.2 — o que esta camada acrescenta (sobre a v7.1)
>
> A v7.1 fechou a **ordem do artigo**. A v7.2 não toca em nenhuma linha do artigo: decide **em qual modelo cada agente da linha roda**.
>
> ### 1. Roteamento por custo do erro
> Cada um dos **22 agentes** ganha um degrau — **forte 🔒 / médio / barato** — escolhido por *"se este agente errar, alguma trava pega?"*. Barato onde um `checkpoint_*.py` ou um conferente com a fonte na mão pega. **Forte onde o erro é de julgamento e sai publicado sem ninguém notar.** Doze agentes ficam travados no forte: `0`, `CI-1`, `CI-2`, `5`, `6`, `11`, `12`, `13`, `15`, `16a-c`.
>
> ### 2. Separação de modelo, além da separação de função
> A regra-mãe da linha ("quem inventa um dado nunca é quem confere esse dado") sobe um nível: **o conferente roda em modelo diferente do produtor** (2×6 · 4×7 · 8/9/10×11 · 11×19 · 5×13).
>
> ### 3. O painel de juízes deixa de ser monocultura
> O próprio SKILL.md já admitia: *"como os três são o mesmo modelo, erro correlacionado é risco real"*. A v3 respondeu com **lentes** distintas; faltava a outra metade. Agora o painel roda com **≥ 2 modelos distintos** e **≥ 1 juiz em modelo diferente do editor-chefe**. Lente separa o que cada juiz procura; **modelo separa o que cada juiz é incapaz de ver.** Achado de voz apontado só por um juiz que roda no mesmo modelo do editor-chefe **não conta voto**.
>
> ### 4. Trava mecânica nova — `checkpoint_modelos.py`
> Roda **antes** do Estágio 1 (é a única trava da skill que roda antes de existir texto), sobre o bloco `PLANO_MODELOS` escrito pelo **Agente 22**.
>
> ```
> python -X utf8 C:\Users\netop\.claude\skills\hapvida-article-builder-v7\checkpoint_modelos.py <state_file.md|PLANO_MODELOS_[slug].md> [city|tr|pillar|hospital]
> ```
>
> Reprova (🔴): agente obrigatório ausente · agente 🔒 abaixo de forte · par produtor/conferente no mesmo modelo · painel monomodelo · nenhum juiz diferente do editor-chefe · degrau inválido · linha inteira num modelo só sem `MODO: monomodelo`. Avisa (🟡): monomodelo declarado · rebaixamento sem motivo escrito · agente inexistente.
>
> ### O que a v7.2 NÃO faz
> - **Não muda uma vírgula do artigo** — nem seção, nem ordem, nem schema, nem paleta, nem limites, nem anti-doorway, nem `[VERIFICAR]`.
> - **Não mede execução.** Ela confere o **plano**; que o Agente 6 tenha mesmo rodado no modelo declarado é responsabilidade do orquestrador.
> - **Não conserta pesquisa ruim.** Três juízes em três modelos discutem com elegância sobre um artigo errado — a trava contra isso continua sendo o `consultar_rede` e o Agente 6.
> - **Não proíbe rodar com um modelo só** — exige declarar (`MODO: monomodelo`) e assumir o que se perde: mesmo modelo com prompt diferente **não** é modelo diferente; o ponto cego é do modelo, não do prompt. Aí o portão humano vale mais.
>
> **Arquivos novos:** `references/modelos-agentes.md`, `checkpoint_modelos.py`.
> **Modificados:** `SKILL.md` (bloco V7.2 + seção "MULTI-AGENTES EM MODELOS DIFERENTES [V7.2]" + Estágio 0 da linha + painel de juízes + trava de pré-voo), `references/pesquisa.md` (seção 10 do state file).
>
> **Efeito esperado, dito sem exagero:** roteamento de modelo reduz erro correlacionado e desperdício de token — **não** melhora pesquisa, nem escreve melhor. O que ganha posição continua sendo tudo o mais que a skill já fazia.

# Base v7 (continua valendo)

**Só dispara sob pedido explícito.** Gatilhos: `v7`, `versão 7`, `builder v7`, `preço primeiro`, `tabela primeiro`, `ordem preço-primeiro`, `sumário depois da tabela`, `H2 de preço primeiro`. Sem isso, use v1-v6 — as sete coexistem para comparação.

> ## ⭐ V7 — o que esta variante acrescenta (sobre a v6)
>
> Uma camada só, de **ORDEM**. Nada é cortado, nada é afrouxado.
>
> ### 1. A tabela de preço é o primeiro conteúdo
> O shortcode que renderiza a tabela (`[cidade_menortabela]`, `[cidade_emp_ambulatorialtotal]`…) — ou a imagem da tabela, em TR — entra **logo depois do Lead GEO e antes do sumário**.
> - **City:** a antiga S2 vira a 1ª seção (**S2↑**); S1 e as demais descem uma posição.
> - **Pillar:** a antiga P3 vira a 1ª seção (**P3↑**); P1 e P2 descem.
> - **TR:** já era image-first — a v7 só formaliza (TR2 antes do sumário) e trava.
> - **Hospital:** não tem tabela própria; a regra não se aplica.
>
> ### 1b. [v7.1] Depois da tabela vem o SUMÁRIO — não mais preço
> A v7.0 empilhava tabela + imagem da tabela + bloco navy + formulário antes do sumário: quatro blocos de preço na primeira tela e o índice do artigo longe demais (medido no artigo de Recife). Na **v7.1**:
> - **Tabela → SUMÁRIO** (colado, no máximo 600 caracteres de texto entre os dois).
> - Só então **faixa navy + `[elementor-template]` `id="cotacao-1"` + selos + análise de preço**.
> - A **imagem da tabela** fecha a seção de preço — nunca colada no shortcode. *(Em TR continua no topo: lá a `<figure>` **é** a tabela.)*
> - Em HTML, a seção de preço fica partida em duas `<section>` (**S2↑a** e **S2↑b**) com o sumário no meio. Continua sendo a mesma S2↑ para numeração, banco e schema.
>
> ### 2. Os H2 de preço têm prioridade de ordem
> Todo H2 sobre preço, tabela, valor, mensalidade, quanto custa ou coparticipação-em-valor fica agrupado no topo, **antes de qualquer H2 de outro assunto**. Coparticipação como *conceito* continua sendo território do pillar e não entra no artigo.
>
> ### 3. Trava mecânica nova — `checkpoint_preco_primeiro.py`
> Reprova (🔴, bloqueia entrega): sem tabela; H2 de outro assunto antes do primeiro H2 de preço; sumário antes da tabela; mais de 1.800 caracteres de texto visível antes da tabela; tabela duplicada; **[v7.1]** mais de 600 caracteres entre a tabela e o sumário; **[v7.1]** formulário `id="cotacao-1"` antes do sumário; **[v7.1]** `<figure>` da imagem da tabela entre a tabela e o sumário (city/pillar). Avisa (🟡): H2 de preço órfão no meio do artigo; `id="cotacao-1"` não encontrado.
>
> ```
> python -X utf8 C:\Users\netop\.claude\skills\hapvida-article-builder-v7\checkpoint_preco_primeiro.py <artigo.html> [city|tr|pillar|hospital]
> ```
>
> ### O que a v7 NÃO faz
> - **Não corta seção.** A S1 desce, íntegra. Os limites do `checkpoint_completude.py` fecham iguais aos da v6 — artigo que encolheu ao reordenar é artigo em que alguém cortou conteúdo.
> - **Não sobe a tabela acima do Lead GEO.** O parágrafo 1 continua sendo a passagem citável que alimenta AI Overviews, ChatGPT e Perplexity.
> - **Não dispensa o contexto local da seção de preço.** Ao contrário: por estar em 1º lugar, é a seção que mais precisa QUEBRAR no teste de substituição de cidade. Tabela solta no topo é doorway no lugar mais visível da página.
> - **Não muda schema, paleta, limites nem numeração interna.** S2 continua S2 com `id="#precos"`; P3 continua P3. Renumerar quebraria o banco e os artigos já publicados.
>
> **Arquivos novos:** `references/preco-primeiro.md`, `checkpoint_preco_primeiro.py`.
> **Modificados:** `SKILL.md` (seção "ORDEM PREÇO-PRIMEIRO [V7]" + esqueletos city/TR + Bloco A + tabela de formulários + mapa de fundos + linha de agentes e juízes), `references/sections.md` (ordem do Bloco A, sumário, S1, S2↑), `references/artigo-pillar-produto.md` (P3↑), `references/tabela-regional-subpages.md` (TR2 antes do sumário), `references/artigo-hospital.md` (nota de não-aplicação), `references/shortcodes.md` (onde o shortcode de tabela entra).
>
> **Efeito esperado, dito sem exagero:** subir a tabela resolve encontro com a intenção comercial e extração por IA — **não** resolve autoridade. Ordem é UX; o que ganha posição continua sendo tudo o mais que a skill já fazia.

# Base v6 (continua valendo)

> ## ⭐ V6 — o que esta variante acrescenta (sobre a v5)
>
> ### 1. Voz humana (anti-texto-de-IA)
> O artigo é escrito por IA. O problema não é isso — é **soar** como IA. Lista de tiques **em português**: a lista famosa que circula é em inglês (`delve`, `robust`) e nem inclui o tique nº 1 do português, que é o **gerúndio de arremate** (*"…12 hospitais na cidade, garantindo mais segurança para a família"* — o pedaço depois da vírgula pode ser apagado sem perder informação).
> - `references/voz-humana.md` + `checkpoint_voz.py` (🔴 reprova / 🟡 avisa; `--rigor alto|baixo`)
> - **Regra-mãe:** mexe em palavra e ritmo, **nunca em fato**. Correção que altera número, nome de hospital ou regra da ANS é rejeitada.
>
> ### 2. GEO por plataforma
> A camada GEO da v2 trata "IA" como uma coisa só. Não é — cada uma usa um índice e pesa sinais diferentes: **AI Overviews** (Google; schema + citação nomeada), **ChatGPT** (Bing; frescor real + formato de resposta), **Perplexity** (próprio+Google; FAQPage + parágrafo autocontido), **Copilot** (Bing; IndexNow + velocidade), **Claude** (**Brave**; densidade factual).
> Junto vêm duas coisas que mudam decisão de pauta:
> - **Escada citado → recomendado**, com a armadilha do listicle auto-promocional: uma corretora Hapvida publicando "os melhores planos de [cidade]" corre risco real de a IA extrair os concorrentes listados e recomendar **eles**.
> - **Query fan-out** obrigatório no DR1: 5-10 sub-perguntas classificadas em *aqui / cluster / pendência*.
> - `references/geo-plataformas.md`
>
> ### 3. Defensibilidade do dado
> O CI-2 da v4 mandava achar "o ângulo que ninguém tem", sem critério. Agora tem: classificar cada dado por nível (**1** proprietário → **5** público e fácil). O artigo precisa de **≥3 dados de nível 1-2** e o **ganho do CI-2 tem de sair de nível 1-2**. O banco Supabase é o ativo de SEO da operação; dado público a IA já responde sozinha, e isso deixou de valer tráfego.
>
> ### 4. Imagem automática
> A imagem da tabela deixa de ser bloco comentado e sai **junto com o artigo** — `gerar_imagem_artigo.py` devolve o `.png`, o `<figure>` pronto, o `ImageObject` e o `curl` de conferência. Duas regras duras, as duas nascidas de erro real: **(a)** nunca IA em número (embaralha dígito; faltou valor, a imagem não sai); **(b)** nome com `tabela`+`coparticipacao` em minúsculo cai num **301** do site e a imagem some do Google mesmo estando no HTML — o padrão `Tabela-Hapvida-...` passa, e o script recusa nome perigoso.
> - `references/imagem-automatica.md`
>
> ### 5. UX de conversão
> Revisão de **comportamento** dos 8 componentes de landing da v5 (toque 44px, `prefers-reduced-motion`, label visível, contraste 4,5:1, `aria-label` em botão de ícone). **Identidade visual, paleta e tipografia não mudam** — ficou de fora de propósito, porque o design já está validado e o Elementor tem armadilhas conhecidas.
>
> ### 6. Arquétipo PILLAR (P1-P9) — o artigo do plano em si
> A v5 tinha **três** arquétipos: cidade, hospital e tabela. Faltava o do **plano/produto** — e por isso os pillars refeitos em julho (Individual, Nosso Plano, Mix, Nosso Médico, Adesão) foram improvisados em cima da estrutura de cidade. A v6 formaliza:
> - **FASE P0 de diagnóstico** antes de reescrever pillar existente. Nasceu de uma descoberta cara: pillar que não ranqueia nem para a própria keyword — e a causa costuma ser **a home canibalizando**, não falta de conteúdo. Quatro coletas: GSC, `serp_local`, `consultar_links_para_destino`, `consultar_artigo`.
> - **P1-P9**, com o **eixo em P4** (o ângulo que nenhum concorrente tem, obrigatoriamente de nível 1-2 de defensibilidade) e o **veredito de dupla lista em P9** ("costuma compensar para" / "**pode não compensar para**" — o sinal de E-E-A-T mais barato e mais raro).
> - **Anti-doorway por PRODUTO**, não por cidade: troque "plano individual" por "Plano Mix" — se a seção continua válida, você está canibalizando o pillar irmão. Com 6+ pillars de produto, esse é o risco real.
> - **Pillar não desce a detalhe de cidade** — diz o âmbito nacional e linka. Isso já teve de ser corrigido à mão uma vez.
> - Limites e dosagem de componentes **calibrados no pillar Individual aprovado** (4.579 palavras, 9 H2, 26 H3, 17 FAQ, 16 links). Layout idêntico ao da v5.
> - `references/artigo-pillar-produto.md` + `checkpoint_completude.py <arquivo> pillar`
>
> **Arquivos novos:** `references/voz-humana.md`, `references/geo-plataformas.md`, `references/imagem-automatica.md`, `references/artigo-pillar-produto.md`, `checkpoint_voz.py`, `gerar_imagem_artigo.py`.
> **Modificados:** `SKILL.md` (6 seções + 4º arquétipo em TIPOS DE ARTIGO + MODO 5 de auditoria + 2 checkpoints de entrega + itens 6-9 no MODO 2), `references/pesquisa.md` (fan-out no DR1, defensibilidade no DR2, state file), `checkpoint_fase0.py` (+2 requisitos), `checkpoint_completude.py` (+tipo `pillar`).
>
> **Dependência:** `gerar_imagem_artigo.py` chama o `gerar_imagem_arte.py` de `C:\Users\netop\Downloads\claude\cotador\` (procura em 3 caminhos; se a pasta mudar, ajustar `CAMINHOS_GERADOR`). Precisa de Pillow. Os demais checkpoints são só biblioteca padrão. Sempre `python -X utf8`.

> ## ⭐ V5 — o que esta variante acrescenta (sobre a v4)
>
> 1. **Kit on-page de keywords** — principal obrigatória em H1, title, URL, meta, 1º parágrafo e ≥1 H2; **mínimo 6 secundárias** com veto de intenção (tráfego qualificado, não volume de vaidade), ≥2 H2 com secundária, e mapa de cluster (secundária → futuro spoke). Trava mecânica nova: `checkpoint_onpage.py`.
> 2. **Fase 5 — ciclo pós-publicação** — D+1 indexação (+IndexNow); D+30/60/90 colheita no Search Console dos termos "quase lá" (posição 5-15) que viram H3/FAQ; vigia de CTR (reescrever title/meta) e canibalização real; fila de revisão por decaimento (revisa quem CAI, não quem é velho).
> 3. **Anti-doorway de título/meta** — teste de substituição também no title/meta; a parte variável do título vem do ganho de informação do CI-2. Consequência: título de cidade vira "Plano Hapvida [Cidade]..." (o molde antigo sem "plano" reprova no checkpoint).
> 4. **Formato de snippet** — DR1 registra o formato da caixa de destaque (parágrafo/lista/tabela) e a passagem correspondente é escrita naquele formato.
> 5. **Governança de âncoras** — texto da âncora registrado no banco; máx. ~1/3 de repetição exata por destino.
> 6. **Piso de profundidade dinâmico** — CI-1 mede palavras/subtópicos dos concorrentes; a meta vira superar o líder em COBERTURA (nunca inflar com conteúdo nacional).
> 7. **Componentes de landing** — 8 componentes de dinamismo/conversão com melhoria progressiva (sem JS nada some): barra fixa de cotação mobile, faixa de conversão pós-lead, abas Individual×Empresarial, contador animado, revelação ao rolar, sumário em fichas, placar versus, selos de confiança. Dose: 3-5 por artigo. Templates em `references/components.md`; CSS/JS em `references/styles-and-scripts.md`; limites no SKILL.md.
>
> Nota de expectativa: FAQPage continua no schema (vale para IA), mas o Google não exibe mais o rich result de FAQ para sites como o nosso — não medir sucesso por esse visual.

> ## ⭐ V4 — o que esta variante acrescenta
>
> A **v4** é uma cópia da **v3** (que já traz orquestração — linha de 18 agentes, editor-chefe, bastão, trava mecânica `[VERIFICAR]`, painel de juízes — sobre a v2 GEO/AEO e a v1). A v4 adiciona uma **camada de Inteligência Competitiva** na FASE 0:
>
> 1. **Desmontagem de concorrentes (Agente CI-1)** — busca as 3-5 páginas que de fato ranqueiam, extrai a cobertura delas (subtópicos, dados, perguntas, estrutura) e onde são fracas. Você não vence quem não estudou.
> 2. **Ganho de informação (Agente CI-2)** — produz o que TODO concorrente cobre (must-match), as brechas a explorar, e **a coisa única que nenhum concorrente diz** (o que o Google premia). De sorte vira processo.
>
> Tudo isso entra no state file e no fio condutor; o painel de juízes ganha uma 5ª dimensão ("vantagem competitiva"). A v3 deixava o artigo impecável *contra si mesmo*; a **v4 o deixa impecável contra os concorrentes**. Vive na seção `[V4]` do `SKILL.md` e só entra sob gatilho explícito. Nada afrouxa anti-doorway, `[VERIFICAR]`, FASE 0 ou YMYL — dado de concorrente é `[VERIFICAR]` até confirmar em fonte primária.

## O que mudou desta versão

A skill agora suporta **3 tipos de artigo** (antes eram 2):

| Tipo | Sigla interna | URL pattern | Quando usar |
|------|--------------|-------------|-------------|
| **City** | S1-S7 | `/plano-hapvida-[cidade]/` | Pillar de cidade — rede assistencial, contratação local |
| **Hospital** | HS1-HS4 | `/[hospital]-hapvida/` | Artigo individual de hospital |
| **Tabela Regional** ⭐ NOVO | TR1-TR5 | `/tabela-de-preco-hapvida/[cidade]/` | Ranquear 2 imagens no image pack do Google |

A sigla **TR** (Tabela Regional) é nomenclatura interna para Claude raciocinar sobre a estrutura. Você dispara pedindo naturalmente — "crie um artigo de tabela de preço para Recife" — não precisa decorar a sigla.

## Estrutura

```
hapvida-article-builder/
├── SKILL.md                                    Documento principal
└── references/
    ├── sections.md                             City articles (S1-S7)
    ├── artigo-hospital.md                      Hospital articles (HS1-HS4)
    ├── tabela-regional-subpages.md             Tabela Regional (TR1-TR5) ⭐ NOVO
    ├── pillar-pages.md                         Registry de pillars + Critical Triangle ⭐ ATUALIZADO
    ├── database-hospitais.md                   Banco de dados de hospitais
    ├── components.md                           HTML components
    ├── shortcodes.md                           Shortcodes
    ├── preco-primeiro.md                       Ordem preço-primeiro (V7) ⭐ NOVO
    └── styles-and-scripts.md                   <style> e <script> finais
```

## Instalação

Já instalada neste ambiente (Claude Code, Windows) em:

```
C:\Users\netop\.claude\skills\hapvida-article-builder-v7\
```

A v7 coexiste com a v1-v6 — não substitui. Os checkpoints `.py` rodam com `python -X utf8` (ver o aviso de ambiente no topo do `SKILL.md`).

## Triggers para o tipo Tabela Regional (TR)

Você dispara o tipo TR pedindo de qualquer forma natural. A skill reconhece:

- "Crie um artigo de tabela de preço para [cidade]"
- "Tabela Hapvida [cidade] empresarial e individual"
- "Subpágina de tabela [cidade]"
- "Página para ranquear imagem da tabela [cidade]"
- "Image pack tabela [cidade]"
- URL pattern `/tabela-de-preco-hapvida/[cidade]/`
- Menção a "TR1-TR5" (sigla interna)

## Critical Triangle — Anti-Doorway para Artigos TR

Para artigos TR, 3 pillars formam um **triângulo crítico** de doorway. As regras estão em `references/pillar-pages.md` (seção `⚠️ CRITICAL TRIANGLE` no topo) e em `references/tabela-regional-subpages.md`. As 3 pillars são:

1. `/tabela-de-preco-hapvida/` — PILLAR PAI
2. `/plano-individual-hapvida/`
3. `/plano-empresarial-hapvida/`

Quando estes 3 arquivos `.txt` estão anexados ao projeto Claude, Claude lê para saber o que **NÃO** repetir no artigo TR. Estar no projeto não autoriza reprodução.

## Versão

- **V7 PREÇO PRIMEIRO (Agosto 2026)** — cópia da v6 + ordem preço-primeiro (tabela antes do sumário, H2 de preço na frente) + `checkpoint_preco_primeiro.py` + `references/preco-primeiro.md`
- **V7.1 SUMÁRIO COLADO NA TABELA (21/08/2026)** — correção da ordem interna da v7, validada no artigo de Recife: tabela → **sumário** → formulário/análise → **imagem da tabela por último**. Seção de preço partida em S2↑a/S2↑b (mesma S2↑ para banco e schema). Três reprovações novas no `checkpoint_preco_primeiro.py` (600 caracteres entre tabela e sumário; `cotacao-1` antes do sumário; imagem entre tabela e sumário). Modificados: `SKILL.md`, `README.md`, `references/preco-primeiro.md`, `references/sections.md`, `references/components.md` (faixa de conversão), `references/imagem-automatica.md`, `checkpoint_preco_primeiro.py`
- V6 VOZ HUMANA + GEO POR PLATAFORMA + IMAGEM + PILLAR (Agosto 2026)
- **V5 ON-PAGE + PÓS-PUBLICAÇÃO (Julho 2026)** — cópia da v4 + kit on-page de keywords (`checkpoint_onpage.py`) + Fase 5 (ciclo Search Console) + anti-doorway de título/meta + formato de snippet + governança de âncoras + piso de profundidade dinâmico
- V4 INTELIGÊNCIA COMPETITIVA (Junho 2026) — desmontagem de concorrentes (CI-1) + ganho de informação (CI-2) na FASE 0
- V3 ORQUESTRAÇÃO (Junho 2026) — cópia da v2 GEO/AEO + passagem de bastão + linha de agentes especialistas (cada agente uma função, conferindo o anterior; trava anti-alucinação)
- V2 GEO/AEO — camada de citabilidade por passagem, schema speakable/Person, checagem de tipo de página na Fase 0, MODO 4 de auditoria
- V5.0.0 (Maio 2026) — Adicionado tipo TR (Tabela Regional)
- V4.5.0 — Tipo Hospital (HS1-HS4), URL única, banco de hospitais
- V3.x — City articles S1-S7

## Mantra

> "Se o Google pode confundir meu artigo com outro — do meu site ou de concorrente — eu falhei."
> "Se uma seção inteira pode ser copiada para outra cidade sem alteração, ela não deveria existir."
> "Se a página existe sem a imagem fazer sentido, falhei. A página é wrapper da imagem, não o contrário." (TR)
