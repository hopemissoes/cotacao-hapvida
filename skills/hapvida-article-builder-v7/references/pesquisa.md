# FASE 0 — PESQUISA (OBRIGATÓRIA)

> Fusão da profundidade da antiga skill `hapvida-research` (DR1 + DR2) com o motor de dado real do **DataForSeo**. Esta é a **primeira fase de todo artigo** — City (S1-S7), Hospital (HS1-HS4) e Tabela Regional (TR). **Sem o state file desta fase aprovado, não se inicia o Bloco A.**

A pesquisa deixou de ser uma skill separada (de alta fricção, 2 conversas, sem DataForSeo) e virou a Fase 0 da builder. O resultado é um **state file** salvo em `/mnt/user-data/outputs/` — é ele o "arquivo de pesquisa" que as Regras de Ouro nº 1, 2 e 5 e os Blocos A/B/C consomem. Nada no artigo pode existir sem estar nesse arquivo.

---

## REGRAS ANTI-ALUCINAÇÃO (valem em TODA a Fase 0 — inegociáveis)

A pesquisa é o ponto onde a alucinação entra no artigo. Estas regras existem para fechar essa porta:

1. **Todo dado entra no state file com um campo `fonte:` preenchido.** Sem fonte verificável → registrar como `[VERIFICAR: descrição]` e **NÃO** usar no artigo. Nunca preencher um número "porque parece certo".
2. **Fontes válidas, em ordem de preferência:** (a) resultado do DataForSeo (guardar a keyword/`location_code` da chamada); (b) fonte primária via `web_fetch` (site oficial Hapvida/GNDI/Clinipam, CNES/DataSUS, IBGE, prefeitura); (c) dado canônico Hapvida via `consultar_dados_canonicos`/skill `hapvida-data`. Agregadores e blogs **não** são fonte de dado factual — no máximo pista a confirmar em fonte primária.
3. **Números corporativos da Hapvida** (hospitais próprios, clínicas, beneficiários nacionais, coparticipação) vêm **sempre** da `hapvida-data`/`consultar_dados_canonicos` — **nunca** inventados nem inferidos da web.
4. **Preços: NUNCA pesquisar nem cravar.** Vão por shortcode (ver `shortcodes.md`). A pesquisa não coleta valor de mensalidade.
5. **Marco histórico / estrutura (leitos, salas, ano de fundação):** exigir **≥2 fontes independentes**; preferir a oficial. 1 fonte só → `[VERIFICAR]`.
6. **DataForSeo só via a skill `dataforseo-tabelaplanos`.** Os formatos de entrada são traiçoeiros e o nome do conector muda entre conversas — consultá-la SEMPRE antes de qualquer chamada. Não duplicar formato aqui.
7. **Cada sub-fase termina em CHECKPOINT + PAUSA.** Apresentar o resultado da fase e **aguardar aprovação do usuário** antes de avançar. Não encadear 0.1 → 0.2 → Bloco A sem o usuário no meio.
8. **Executar, não narrar.** Não descrever os passos antes de rodar — rodar e apresentar o resultado estruturado.

**Custo típico da Fase 0 completa:** ~US$ 0,10–0,15 em DataForSeo (centavos). Não pular chamada para "economizar" — artigo escrito sem base é o gasto real.

---

## PRÉ-REQUISITOS (antes da Fase 0.1)

1. **Tipo de artigo identificado** (City / Hospital / TR) — define a profundidade (ver "Ajuste por tipo" no fim).
2. **Banco consultado** (MCP `BD - Consultar`): `consultar_artigo` (já existe? versão? status), `consultar_cluster_completo` (cluster, overlaps, FAQs usadas), `consultar_faqs_catalogo` (FAQ a evitar), `consultar_pillars_proibicoes` (o que cada pillar já cobre), `consultar_saturacao_destinos` (destinos de link saturados).
3. **`location_code` da cidade** — necessário para o DataForSeo. Se a cidade não estiver na tabela da skill `dataforseo-tabelaplanos`, descobrir o código (geo target do Google Ads) e registrar lá.
4. **`hapvida-data` lido** — números nacionais e tabela de coparticipação correta (Tabela 1 ou 2; Tabela 2 só SP e BH/RMBH).

---

## FASE 0.1 — DR1: COLETA DE DADOS

### Parte 1 — SERP real (DataForSeo)

Substitui a leitura manual de SERP (que tem viés de IP e média poluída) por dado real.

**1.1 `serp_local` na keyword principal** (`plano de saúde hapvida [cidade]`), `depth: 20`, rodar **mobile e desktop** (a posição muda entre os dois). Repetir para 2-3 keywords secundárias (`hapvida [cidade] preços`, `hapvida [cidade] hospitais`).

Para cada um dos **10 primeiros orgânicos**, documentar:
```yaml
position_organica: [rank_group]
position_absoluta: [rank_absolute]   # mostra o que empurra você pra baixo
url: "[URL]"
dominio: "[site.com.br]"
tipo_conteudo: "[guia/comparativo/institucional/blog/landing]"
h1: "[H1]"
h2s_principais: ["H2 1", "H2 2", "H2 3"]
forcas: ["o que faz bem"]
fraquezas: ["o que falta"]
tem_dado_local: "[sim/não — qual]"
e_doorway: "[sim/não — por quê]"
oportunidade: "[como superar]"
```

**1.2 Elementos da SERP que importam** (registrar presença e quem ocupa): `ai_overview` (e quais domínios são citados em `references[]` — quem alimenta a resposta do topo), `local_pack`, `people_also_ask` (guardar as perguntas — entram no DR2), `people_also_search`.

**1.2b [V5] FORMATO DE SNIPPET (registrar para a principal + 2-3 secundárias de maior volume):**
```yaml
featured_snippet:
  existe: sim/não
  formato: parágrafo / lista / tabela
  ocupante: "[domínio que ocupa hoje]"
  acao: "escrever a passagem correspondente (abertura de seção ou FAQ) NESTE formato"
```
Se a caixa responde em lista, a nossa resposta é lista (`<ul>`/steps); em tabela, tabela genuína; em parágrafo, os 40-60 palavras da geo-aeo §1. Responder no formato errado = escrever bem para o alvo errado.

**1.3 Canibalização (sinal precoce):** se **2+ URLs do próprio site** aparecem na mesma SERP → registrar 🔴 (a Fase 0 já antecipa o que o MODO 3 audita).

**1.4 `ranked_keywords` em 1-2 concorrentes locais** (os de melhor posição na 1.1) → lista de keywords pelas quais o concorrente rankeia e você não. **É a "lacuna de concorrente"** — matéria-prima de seção/subsection única no DR2.

**Síntese da SERP:**
```yaml
distribuicao: "[X guias, Y comparativos, Z institucionais, W blogs]"
com_dado_local_unico: "[__/10]"
doorways: "[__/10]"
gaps_sem_cobertura: ["5+ temas que ninguém cobre"]
oportunidades_diferenciacao: ["5+"]
keywords_dos_concorrentes: ["da 1.4 — lacunas para nós"]
```

### Parte 2 — Mapeamento completo de rede (fonte primária)

DataForSeo **não** faz isto — é `web_fetch` em fonte primária + Google Maps para validar endereço.

**Fontes obrigatórias:** `https://www2.hapvida.com.br/unidades`, Google Maps. **Complementares:** redes sociais das unidades, notícias locais (inaugurações), site da prefeitura.

**Mapear TODAS as unidades próprias.** Hospitais (meta: toda unidade da cidade):
```yaml
nome: "[nome oficial]"
tipo: "[proprio/retaguarda]"
endereco: "[rua, número, bairro, CEP]"
telefone: "[telefone]"
servicos: [PS 24h, UTI adulto, UTI neonatal, maternidade, centro cirúrgico, hemodinâmica, oncologia]
diferenciais: ["destaques"]
acreditacao: "[ONA/JCI se houver]"
ano_inauguracao: "[se encontrado]"
fonte: "[de onde veio — OBRIGATÓRIO]"
```
**PAs 24h:** `nome, endereco_completo, telefone, servicos (raio-x, medicação, sutura...), fonte`.
**Hapclínicas:** `nome, endereco_completo, telefone, especialidades[], fonte`.
**Vida & Imagem / Labs:** `nome, endereco_completo, telefone, tipos_exame (simples/complexo/imagem), fonte`.
**Rede credenciada:** mapear hospitais/clínicas credenciados-chave — crítico para cobertura do Plano Mix e cidades sem rede própria completa.

**Checklist de validação da rede:**
```yaml
hospitais_documentados: [X]
pas_24h: [X]
clinicas: [X]
labs: [X]
todos_com_endereco: [sim/não]
todos_com_telefone: [sim/não]
cobertura_por_regiao: {norte: X, sul: X, leste: X, oeste: X, centro: X}
bairros_sem_cobertura: [lista ou "nenhum"]
```

### Parte 3 — Contexto local
**Demografia (IBGE — ibge.gov.br/cidades-e-estados):**
```yaml
populacao: "[X] hab ([ano])"
populacao_metro: "[X] ([ano])"
ranking: "[Xª maior do Brasil/região/estado]"
idh: "[0,XXX] ([ano]) — [acima/abaixo] da média estadual"
pib_per_capita: "R$ [X] ([ano])"
perfil_etario: {jovens_0_14: "X%", adultos_15_59: "X%", idosos_60+: "X%"}
```
**Saúde (CNES — cnes.datasus.gov.br):**
```yaml
estabelecimentos_saude: "[X] total, [X] com internação"
leitos_hospitalares: "[X] total, [X] por 10 mil hab (média nacional: X)"
leitos_uti: "[X] total, [X] por 10 mil hab"
```
**Presença Hapvida na cidade:**
```yaml
opera_desde: "[ano]"
tipo_rede: "[propria/credenciada/mista]"
beneficiarios_estimados: "[X] (fonte)"
market_share: "[X]% (se houver)"
marcos:
  - {ano: "[ano]", evento: "[o quê]", fonte: "[fonte]"}
investimentos_recentes:
  - {descricao: "[investimento]", valor: "R$ [X] se divulgado", ano: "[ano]", fonte: "[fonte]"}
```

### Parte 4 — Acessibilidade
```yaml
concentracao_unidades:
  bairros_principais:
    - {bairro: "[nome]", unidades: X, tipos: "Hospital, Clínica, PA"}
regioes_bem_servidas: ["região — por quê"]
regioes_carentes: ["região — quantas unidades"]
transporte_publico: {perto_metro: X, perto_terminal: X}
observacoes: "[análise de cobertura]"
```

### Parte 5 — Concorrentes locais
```yaml
concorrente_1:
  nome: "[Unimed local / etc.]"
  tipo: "[cooperativa/seguradora/medicina de grupo]"
  rede: "[propria/credenciada]"
  presenca: "[forte/média/fraca]"
  diferencial: "[o que destacam]"
# mapear 2-3 concorrentes locais principais
```

### Parte 6 — [V6] Query fan-out (obrigatória)

A busca com IA **não responde só a pergunta digitada**: ela gera sub-perguntas por baixo e sintetiza. Por isso, cobrir o tema-pai com as sub-perguntas dentro rende mais do que uma página por keyword. Ver `references/geo-plataformas.md`.

Listar **5 a 10 sub-perguntas** prováveis a partir da keyword-alvo e classificar cada uma:

```yaml
fan_out:
  - pergunta: "quanto custa o plano hapvida em [cidade]"
    destino: aqui            # aqui | cluster | pendencia
    onde: "S3 — seção de preços"
  - pergunta: "quais hospitais a hapvida atende em [cidade]"
    destino: aqui
    onde: "S4 — rede"
  - pergunta: "qual a carência do plano hapvida"
    destino: cluster
    onde: "/carencia-hapvida/ — link interno"
  - pergunta: "hapvida tem plano para MEI"
    destino: pendencia       # vira pauta no banco (adicionar_pendencia)
    onde: "-"
```

**Trava:** cobrir sub-pergunta **não** autoriza inflar o artigo com conteúdo nacional genérico (regra da v4: *profundidade ≠ conteúdo nacional*). Sub-pergunta sem resposta **local** vira link, nunca seção.

### ✅ CHECKPOINT DR1 — apresentar e PAUSAR
```
SERP:        [ ] 10 concorrentes (serp_local)  [ ] gaps  [ ] oportunidades  [ ] lacunas de keyword (ranked_keywords)
Rede:        [ ] mín. 5 unidades com endereço  [ ] ≥1 hospital detalhado  [ ] cobertura por região  [ ] credenciada
Contexto:    [ ] IBGE população c/ fonte  [ ] IDH c/ fonte  [ ] CNES leitos c/ fonte
Hapvida:     [ ] opera desde [ano]  [ ] tipo de rede  [ ] beneficiários (se houver)
[V6] Fan-out:[ ] 5-10 sub-perguntas listadas  [ ] cada uma classificada (aqui/cluster/pendência)
Fontes citadas no total: [X]   |   Itens [VERIFICAR] pendentes: [X]
```
**PAUSA.** Apresentar o resumo do DR1 e aguardar o "ok" do usuário antes de ir ao DR2.

---

## FASE 0.2 — DR2: POSICIONAMENTO SEO + FAQ + ANTI-DOORWAY

**Pré-requisito:** DR1 aprovado.

### Parte 1 — SEO semântico

**1.1 Entidades principais:**
```yaml
operadora: {nome: "Hapvida", tipo: Organization, mencoes: "15-20×", variacoes: "[Hapvida NotreDame Intermédica, Grupo Hapvida]"}
cidade: {nome: "[cidade]", tipo: Place, mencoes: "20-30×", variacoes: "[capital de X, RM de...]"}
produto: {nome: "Plano de Saúde", tipo: Product/Service, mencoes: "10-15×", variacoes: "[convênio médico, plano empresarial, plano individual]"}
```
**1.2 Entidades secundárias:** hospital principal (LocalBusiness), bairros-chave (Place), ANS (Organization), Unimed local (Organization), conceitos (coparticipação, carência, rede credenciada).

**1.3 Keywords com DADO REAL (DataForSeo):**
- **Descoberta de secundárias (motor de expansão):** `keyword_suggestions` na principal → todas as queries que **contêm** a keyword (long-tail de mesma intenção); `keyword_ideas` (sementes = principal + 1-2 variações) → secundárias **da mesma categoria, não óbvias**. Filtrar por volume (`filters`) e cruzar com `serp_local`/`ranked_keywords` para **escolher no mínimo 6 secundárias reais [V5]** para H2/subseções/FAQ (formatos na skill `dataforseo-tabelaplanos`).
- **[V5] VETO DE INTENÇÃO em cada secundária (análise obrigatória — tráfego qualificado, não volume de vaidade):** para cada candidata, responder *"quem busca isso pode virar cliente da corretora?"* ✅ qualificada: intenção comercial/transacional ou informacional-de-compra local ("plano hapvida [cidade] valor", "hapvida [cidade] é bom"). ❌ descartar mesmo com volume alto: intenção de quem JÁ é cliente ou nunca será ("2ª via boleto", "telefone hapvida", "trabalhe conosco", "resultado de exame", "cancelar plano") — esse tráfego incha impressão, derruba CTR/conversão e polui o sinal de relevância da página.
- **[V5] MAPA DE CLUSTER:** para cada secundária qualificada, marcar `cluster_candidata: sim/não` — ela comporta artigo próprio no futuro (spoke desta city page)? Candidatas viram pendência de pauta no banco (`adicionar_pendencia`) no registro pós-Bloco C.
- `keyword_data` confirma volume/intenção da **principal** (e de candidatas a título/H2). Para pontuar a lista inteira de secundárias de uma vez, `bulk_keyword_difficulty` (uma chamada).
- **Regra de prioridade:** keyword de volume ~0 (`items_count: 0`) **não** vira título/H2 — é vaidade. Título/H2 puxam a keyword com volume real + intenção comercial/transacional. A oportunidade boa é **volume decente + dificuldade baixa + você fraco** (cruzar com a posição do `serp_local`).
- `related_keywords` na principal → universo semântico (variações, termos LSI) para distribuir pelas seções **e** PAA para o FAQ (Parte 3).
```yaml
principal: {kw: "plano de saúde hapvida [cidade]", volume: [X], intencao: "[...]", dificuldade: [X]}
secundarias:
  - {kw: "hapvida [cidade] preços", volume: [X], intencao: comercial}
  - {kw: "hospitais hapvida [cidade]", volume: [X], intencao: informacional}
long_tail: [...]   # com volume e intenção de cada
```
**1.4 Gap analysis vs SERP:** cruzar com os 10 concorrentes do DR1 e as lacunas do `ranked_keywords` → entidades/temas que eles cobrem e nós não (plano de ação) e os que são só nossos (alavancar).

**1.5 [V5] KIT ON-PAGE (seção obrigatória do state file — o `checkpoint_onpage.py` confere isso no HTML depois):**
```yaml
kit_onpage:
  principal: "[keyword principal]"
  posicoes_principal:   # todas obrigatórias — rascunhar aqui, conferir no HTML
    h1: "[rascunho do H1 contendo a principal]"
    title: "[rascunho do título SEO — principal à esquerda + ganho de informação do CI-2]"
    url: "[slug — conferir que contém a principal; nos padrões do site sai por arquitetura]"
    meta: "[rascunho da meta com a principal 1× — o Google negrita o termo buscado]"
    primeiro_paragrafo: "sim (lead GEO)"
    h2: "[qual H2 vai conter a principal ou variação natural]"
  secundarias:   # mínimo 6 qualificadas
    - {kw: "...", volume: X, intencao: "...", veredito: qualificada/descartada, onde_entra: "H2 da S_/H3/FAQ", cluster_candidata: sim/não}
  h2_com_secundaria: "[quais 2+ H2 contêm secundária]"
```
**Trava anti-stuffing:** o kit define ONDE, não QUANTAS vezes — vale variação natural (flexão, plural, ordem); H2 que ficar artificial se reescreve. E o teste de substituição vale nos H2 com keyword: H2 que serve para qualquer cidade continua doorway.

### Parte 2 — Diferenciais únicos (mín. 3-5)
Categorias válidas: infraestrutura, pioneirismo, atendimento, história, tecnologia.
```yaml
categoria: "[...]"
titulo: "[nome]"
descricao: "[3-5 linhas]"
dado_quantitativo: "[número específico]"
vs_outras_cidades: "[como difere de SP, BH...]"
vs_concorrentes: "[como difere da Unimed/Bradesco local]"
por_que_importa: "[benefício pro usuário]"
fonte: "[OBRIGATÓRIO]"
frase_sugerida: "[como escrever no artigo]"
defensibilidade: "[V6] 1|2|3|4|5"   # ver tabela abaixo — 4 ou 5 reprova como GANHO
```

**[V6] Defensibilidade — o critério que faltava.** Marcar o nível de cada dado:

| Nível | Tipo | Exemplo | Quem mais tem |
|---|---|---|---|
| **1** | proprietário | rede conferida cidade a cidade no banco; tabela vigente | ninguém |
| **2** | derivado de operação | dúvidas que chegam pelo WhatsApp naquela cidade; saída do cotador | ninguém |
| **3** | licenciado | SERP e volume do DataForSeo | quem paga |
| **4** | público mas trabalhoso | cruzar RN da ANS com o produto; ler o Guia Médico unidade a unidade | quem tem paciência |
| **5** | público e fácil | "a ANS exige 24h de carência para urgência" | todo mundo — a IA responde sozinha |

**Regra:** o artigo precisa de **≥3 dados de nível 1-2**, e o **ganho de informação do CI-2 tem de sair de nível 1 ou 2**. Ganho de nível 4-5 não é ganho: o concorrente copia em dez minutos e a IA já responde sem precisar de vocês.

**Trava herdada:** dado de nível 1-2 **também** passa por `[VERIFICAR]` e conferência no banco. Ser proprietário não é ser correto — o banco já se provou incompleto para hospital credenciado, e ausência no banco **não** é prova de ausência na rede.
**Diferenciais por tipo de rede:** *Própria (N/NE)* — prontuário integrado, autorização automática de emergência, padrão único de atendimento, telemedicina integrada. *Credenciada (S/SE)* — hospitais de referência, flexibilidade geográfica, parcerias com centros especializados.
**Validação:** cada diferencial passa por "outra cidade tem exatamente isto?" Se sim → não é único o bastante. Mínimo **3 de verdade**.

### Parte 3 — FAQ local (15-20 perguntas)
**Todas baseadas em dado REAL do DR1. Zero genérica.** Combinar duas fontes:
- **`related_keywords` (PAA real)** + as `people_also_ask` capturadas no DR1 Parte 1.2.
- **CRUZAR com `consultar_faqs_catalogo`** (banco) ANTES de fixar — PAA que já existe em artigo irmão é **doorway**, não FAQ nova.

Distribuição sugerida: rede (5-7), cobertura geográfica (3-5), diferenciais (3-4), contratação (3-4). Exemplos de molde (sempre com dado local concreto): "Quais hospitais Hapvida em [cidade] atendem 24h?", "Qual hospital Hapvida faz parto em [cidade]?", "Hapvida ou Unimed em [cidade]: qual escolher?", "Quanto tempo para aprovar o plano em [cidade]?".
```yaml
total: [X]   # mín. 15
com_dado_local: [X]
genericas: [X]   # tem que ser 0
teste_troca_cidade: "trocar [cidade] por outra → a pergunta perde sentido? → tem que ser SIM"
```

### Parte 4 — Validação anti-doorway
**4.1 Teste de substituição:** trocar mentalmente [cidade] por São Paulo no plano do artigo.
```
| Seção         | Perde sentido se trocar? | Por quê |
| Rede          | [sim/não] | ... |
| Contexto      | [sim/não] | ... |
| Diferenciais  | [sim/não] | ... |
| FAQ           | [sim/não] | ... |
```
**Alvo: 70%+ do conteúdo perde sentido ao trocar a cidade.**
**4.2 Contagem de dados únicos:** listar **mín. 10 (alvo 15)** dados que só existem para esta cidade.
**4.3 Frases-banidas (máx. 0):** "atendimento de qualidade", "equipe qualificada", "melhor custo-benefício", "cobertura completa", "infraestrutura moderna". Achou → trocar por dado específico.
```yaml
teste_substituicao: "[PASSOU/FALHOU] — [X]% perde sentido"
dados_unicos: "[PASSOU/FALHOU] — [X] (mín. 10)"
frases_genericas: "[PASSOU/FALHOU] — [X] (máx. 0)"
geral: "[APROVADO/REPROVADO]"
```

### ✅ CHECKPOINT DR2 + ANTI-DOORWAY — apresentar e PAUSAR
Só passa com: keywords com volume real definidas (título/H2 não-vaidade), **[V5] kit on-page completo (≥6 secundárias qualificadas + rascunhos H1/title/meta + mapa de cluster)**, ≥3 diferenciais únicos, ≥15 FAQ com dado local e 0 genérica, e anti-doorway **APROVADO** — **[V5] incluindo título e meta no teste de substituição** (trocar a cidade: se continuam válidos, o miolo é genérico). **PAUSA** para aprovação antes de gerar o state file.

---

## SAÍDA — STATE FILE (o "arquivo de pesquisa")

Gerar arquivo completo em `/mnt/user-data/outputs/PESQUISA_[slug]_COMPLETO.md` com TODO o DR1 + DR2 acima, mais o resumo:
```
═══════════════════════════════════════════
✅ PESQUISA COMPLETA — PRONTA PARA O ARTIGO
Cidade/Alvo: [...]   |   Tipo: [City S1-S7 / Hospital HS1-HS4 / TR]
SERP: 10 concorrentes (serp_local mobile+desktop)
Keywords: principal + [X] secundárias qualificadas (mín. 6, veto de intenção) + [X] long-tail (com volume real)
Kit on-page: H1/title/URL/meta/1ºP/H2 rascunhados   |   Cluster candidatas: [X]   |   Snippet: [formato ou "não há"]
Rede mapeada: [X] unidades   |   Diferenciais únicos: [X]   |   FAQ: [X]
Dados únicos (anti-doorway): [X]   |   Itens [VERIFICAR]: [X]
[V6] Fan-out: [X] sub-perguntas — [X] aqui / [X] cluster / [X] pendência
[V6] Defensibilidade: [X] dados de nível 1-2 (mín. 3)   |   Ganho do CI-2 é nível: [1|2]
Anti-doorway: APROVADO — [X]% perde sentido na troca, 0 frase genérica
Fontes citadas: [X]
[V7.2] Roteamento: PLANO_MODELOS aprovado — [X] agentes | [X] modelos distintos | modo: [multimodelo|monomodelo]
═══════════════════════════════════════════
```
Este arquivo é a fonte única que o Bloco A, B, C e as Regras de Ouro consomem. **Os itens `[VERIFICAR]` NÃO entram no artigo** — ficam listados para o usuário confirmar ou descartar.

**[V7.2] Seção 10 — `PLANO_MODELOS`.** O bloco de roteamento escrito pelo **Agente 22** em `PLANO_MODELOS_[slug].md` **antes** do Estágio 1 (e já aprovado pelo `checkpoint_modelos.py`) é **copiado para a seção 10 deste state file** assim que ele nasce. Não é decoração: é o que permite ao handoff, à auditoria e à próxima sessão saberem **em que modelo cada dado foi produzido e por qual modelo foi conferido**. Formato e travas em `references/modelos-agentes.md` §5-§6.

---

## GATE FINAL → BLOCO A (TRAVA MECÂNICA)

**Pesquisa diagnóstica NÃO é Fase 0.** Rodar `serp_local`, `keyword_data`, `keyword_suggestions` avulsos, ou olhar GSC/GA4, **não** satisfaz a Fase 0 e **não** autoriza HTML. Dizer "já temos quase tudo" / "a pesquisa já está feita" é **proibido** — ou o state file existe e está aprovado, ou a Fase 0 não foi feita. Não há meio-termo.

Antes de UMA linha de HTML, **nesta ordem**:
1. O state file `PESQUISA_<slug>_COMPLETO.md` existe em `/mnt/user-data/outputs/` com TODAS as partes do DR1 e DR2 acima.
2. Rodar **`python -X utf8 C:\Users\netop\.claude\skills\hapvida-article-builder-v5\checkpoint_fase0.py <caminho do PESQUISA_<slug>_COMPLETO.md>`** e **colar a saída na conversa**. Se não imprimir `✅ APROVADO`, **PARAR** — é proibido escrever HTML.
3. O usuário aprovou **explicitamente** o state file (o `APROVADO` do script é só "processo cumprido"; não substitui o aval humano).

Só com os três, iniciar o Bloco A. Faltando qualquer um, parar e fechar a lacuna — **nunca** "começar enquanto isso". Se o usuário pedir o HTML direto, a resposta correta é rodar/exibir o checkpoint e o que falta, não obedecer e pular a trava.

---

## AJUSTE POR TIPO DE ARTIGO

- **City (S1-S7):** Fase 0 completa, como acima.
- **Hospital (HS1-HS4):** keyword é cauda longa (volume baixo). No DR2 Parte 1.3, priorizar `related_keywords` (PAA) e **pular `ranked_keywords`** se não houver concorrente claro — não gastar chamada onde o volume é ~0. No DR1, o foco da rede é **o hospital específico** (leitos, salas, UTIs, especialidades, ONA, acessos/transporte) com ≥2 fontes — e **não repetir a S4 do pillar de cidade** (anti-doorway: ver `artigo-hospital.md`).
- **TR (TR1-TR5):** o ativo é a imagem da tabela ranqueando no image pack. No DR2, a keyword exata da imagem (`Tabela Hapvida [cidade] Empresarial [ano]`) deve passar por `keyword_data`. DR1 de rede é dispensável; manter SERP (`serp_local` para ver quem ocupa o image pack) + os 3 fatores únicos de preço da cidade (TR4). Ver `tabela-regional-subpages.md`.
