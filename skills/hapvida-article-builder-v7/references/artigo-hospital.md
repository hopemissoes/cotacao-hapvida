# Artigo Individual de Hospital — Template de Produção

## Extensão do hapvida-article-builder V4.5.0

**Tipo de conteúdo:** Artigo individual de hospital (spoke do artigo de cidade)
**Keyword-alvo:** `hospital [nome] hapvida` / `hospital [nome] [cidade]`
**Hierarquia hub-spoke:**

```
Pillar temático (coparticipação, carências, rede própria...)
  └─ Artigo de cidade (hub local) ← S4 = ficha técnica do hospital
       └─ Artigo de hospital (spoke) ← ESTE TEMPLATE = guia de experiência do hospital
```

**Exemplo de URLs:**
- `/hospital-aldeota-hapvida/`
- `/hospital-ilha-do-leite-hapvida/`
- `/hospital-promed-hapvida-goiania/`
- `/hospital-rio-mar-hapvida-belem/`

---

## PRINCÍPIO ANTI-DOORWAY

O artigo de cidade (S4) já responde: **"este hospital existe, fica neste endereço, tem estas especialidades"**.
O artigo de hospital responde: **"como é ser atendido aqui, o que esperar, para quem este hospital é ideal, como chegar"**.

> **Teste:** Se a frase funciona igual na S4 do artigo de cidade, é doorway. Reescrever.

O artigo de hospital é **um guia de experiência para quem vai usar aquele hospital** — não uma ficha cadastral e não um mini-artigo de plano de saúde.

---

## TABELA "O QUE NÃO REPRODUZIR" (obrigatória antes da produção)

Antes de escrever qualquer HTML, Claude DEVE produzir esta tabela cruzando com:

### 1. Artigo de cidade (S4)

| Fonte (artigo de cidade S4) | Contém | Artigo de hospital NÃO reproduz |
|-----------------------------|--------|---------------------------------|
| Card hero deste hospital | Nome, endereço, telefone, leitos, lista de especialidades | NÃO repetir ficha técnica completa — pode mencionar endereço 1x no contexto de "como chegar" |
| Linha do tempo | Marcos históricos (aquisição, reformas) | NÃO repetir timeline — pode aprofundar 1 evento com narrativa |
| Panorama da rede | "Goiânia tem 3 hospitais próprios..." | NÃO repetir contagem da rede — foco é ESTE hospital |
| Cards de outros hospitais | Fichas dos demais hospitais da cidade | NÃO mencionar outros hospitais exceto para diferenciar ("para ortopedia, o encaminhamento vai para o Promed") |

### 2. Pillar pages temáticos

| Pillar | Contém | Artigo de hospital NÃO reproduz |
|--------|--------|---------------------------------|
| Rede Própria Hapvida | Lista nacional, modelo verticalizado | NÃO explicar modelo verticalizado |
| Coparticipação | Mecânica, tabela, simulador | NÃO explicar coparticipação — 1 frase: "internações neste hospital são isentas de coparticipação" + link |
| Carências | Prazos ANS | NÃO listar prazos — 1 frase contextual se necessário + link |
| Como Contratar | Steps, documentos, DPS | NÃO reproduzir — usar CTA |
| Tabela de Preços | Tabelas por faixa | NÃO reproduzir tabela de preços |

### 3. Outros artigos de hospital da mesma cidade

Se já existirem artigos de outros hospitais da mesma cidade, cruzar FAQ e conteúdo para evitar repetição entre os spokes.

---

## LEAD GEO (obrigatório)

O primeiro parágrafo do artigo DEVE funcionar como resposta direta para featured snippet e AI Overview. Formato obrigatório:

```
O Hospital [Nome] fica na [endereço completo], bairro [bairro], em [Cidade]-[UF], e é [posicionamento único — ex: "o primeiro hospital 100% materno-infantil da Hapvida no Norte"]. [Dados de estrutura: PA 24h, UTI, leitos, lab]. É o hospital de referência para [tipo de atendimento] dos beneficiários Hapvida em [estado/região].
```

**Elementos obrigatórios no lead GEO:**
- Endereço completo (rua, número, bairro, cidade-UF)
- Posicionamento único do hospital (o que ele é PARA a rede)
- 3-4 dados de estrutura (PA 24h, UTI, leitos, laboratório)
- Público geográfico (capital + RM ou região atendida)
- Referência de especialização (materno-infantil, ortopédico, trauma, etc.)

O lead GEO é o texto que o Google extrai. Se ele não responde "o que é, onde fica, o que faz", o artigo perde a chance de featured snippet.

---

## ARQUITETURA DO ARTIGO DE HOSPITAL

> **[V7] Regra preço-primeiro no artigo de hospital: quase nada muda.** Artigo de hospital não tem seção de preço própria — o preço aparece na HS4 como chamariz `[cidade_menorvalor]`, que é **valor pontual, não tabela**. A regra "tabela primeiro" **não se aplica**. O que se aplica: **se** o artigo passar a incluir um shortcode de tabela completa, ele sobe para antes do sumário e a regra de prioridade dos H2 de preço passa a valer. Rodar `checkpoint_preco_primeiro.py <arquivo> hospital` mesmo assim — no modo hospital ele só confere que não há H2 de preço perdido no meio do artigo.

**Total de seções: 4 + FAQ + Conclusão**
**Artigo curto e focado — não é artigo de cidade.**

```
<article>
  [IMAGEM DE ABERTURA — <figure>]             — 1º elemento, antes do lead (ver components.md)
  [INTRODUÇÃO — LEAD GEO DO HOSPITAL]         — branco (border-bottom)
  [SUMÁRIO / NAV]                              — gradiente #fafbfc → #f0f4f8
  [HS1: O QUE FAZ ESTE HOSPITAL DIFERENTE]     — #f8f9fa (CORE)
  [HS2: EXPERIÊNCIA DO PACIENTE]               — branco (CORE)
  [elementor-template — 1º formulário]         id="cotacao-1" (após HS2 — meio do artigo)
  [HS3: COMO CHEGAR E INFORMAÇÕES PRÁTICAS]    — #fff8f3 (CORE)
  [HS4: QUAIS PLANOS DÃO ACESSO]              — #f8f9fa (BRIDGE → cidade + pillars)
  [FAQ]                                        — branco
  [CTA final — elementor-template]
  [CONCLUSÃO]                                  — gradiente #f8fafc → #f1f5f9
  (sem JSON-LD aqui — V4.6.0: schema gerado em execução separada, ver SKILL.md)
  [<style>]
  [<script>]
</article>
```

**Posicionamento dos CTAs:**
- **1º CTA** (`id="cotacao-1"`): após HS2 (Experiência) — o leitor já entendeu o hospital e está engajado
- **2º CTA**: após FAQ — o leitor tirou suas dúvidas e está pronto para converter
- Os dois CTAs devem ter distância significativa entre si (mínimo 2 seções + FAQ de separação)

> **Nota sobre nomenclatura:** As seções usam HS1-HS4 (Hospital Section) para diferenciar dos artigos de cidade (S1-S7). Os H2 do HTML seguem o padrão visual do skill (mesmo estilo de header).

---

### ── HS1: O QUE FAZ O [NOME DO HOSPITAL] DIFERENTE ──
- **ID:** `#diferencial`
- **Background:** `#f8f9fa`
- **Type:** CORE
- **Extensão:** 3-4 parágrafos

**Conteúdo:**

- **Parágrafo 1 — Posicionamento:** O que este hospital é PARA a cidade. Não é lista de especialidades (S4 já faz). É o papel que ele cumpre na rede. Exemplos:
  - "O Hospital Aldeota é a porta de entrada da Hapvida para a zona leste de Fortaleza — o PS mais procurado da rede no Ceará."
  - "O Hospital Promed é o único hospital ortopédico 24h em rede própria de operadora no Centro-Oeste."
  - "O Hospital Rio Mar é o centro de alta complexidade da Hapvida no Norte — R$ 92 milhões em modernização em curso."

- **Parágrafo 2 — Diferencial técnico aprofundado:** UM aspecto que a S4 só menciona em 1 linha, desenvolvido com contexto. Exemplos:
  - S4 diz "UTI Neonatal Nível III". Artigo de hospital explica: o que significa Nível III, quantos leitos, que tipo de caso recebe, por que gestantes de alto risco da região metropolitana são encaminhadas para cá.
  - S4 diz "hemodinâmica 24h". Artigo explica: o que é o serviço de hemodinâmica, em que situações é acionado, por que ter 24h faz diferença em infarto.

- **Parágrafo 3 — Contexto local:** Quem usa este hospital e por quê. Bairros que dependem dele, perfil dos pacientes, relação com a comunidade.

- **Parágrafo 4 (opcional) — Investimento/expansão recente:** Se houve obra, inauguração, novo equipamento — aprofundar com dados (valor investido, data, impacto).

**Componentes visuais:**
- Box "Resumo Rápido" com 3-4 dados-chave do hospital (NÃO repetir a ficha da S4 — usar dados DIFERENTES: ex. "X partos realizados em 2024", "Y cirurgias ortopédicas/mês", "tempo médio triagem-atendimento: Z min")
- 1-2 destaques animados

**REGRAS ANTI-DOORWAY HS1:**
- NÃO listar especialidades (S4 faz)
- NÃO repetir ficha técnica (endereço, telefone, leitos) — pode mencionar bairro como referência
- NÃO explicar modelo verticalizado (pillar faz)
- PODE contar história do hospital com ângulo narrativo (não timeline de marcos)

---

### ── HS2: EXPERIÊNCIA DO PACIENTE ──
- **ID:** `#experiencia`
- **Background:** branco
- **Type:** CORE
- **Extensão:** 3-5 parágrafos + componentes

**Conteúdo — escolher 3-4 tópicos conforme o perfil do hospital:**

**Para hospitais com PS 24h:**
- Como funciona a chegada: triagem, classificação de risco (Manchester?), tempo médio de espera
- Diferença entre PS deste hospital e PAs da cidade (PA resolve X, hospital resolve Y)
- Horários de pico e dicas para evitar espera

**Para maternidades:**
- Como funciona o pré-natal na rede até o parto neste hospital
- Estrutura da maternidade: salas de parto, alojamento conjunto, acompanhante
- UTI neonatal: quando é acionada, capacidade
- Programa de parto humanizado (se houver)

**Para hospitais especializados (ortopédico, cardio, onco):**
- Fluxo do paciente: como chega ao especialista (encaminhamento? PS direto?)
- O que esperar de uma cirurgia eletiva neste hospital (agendamento → pré-op → internação → alta)
- Equipamentos especializados disponíveis

**Para qualquer hospital:**
- Internação: o que levar, como funciona a autorização, como é o quarto/enfermaria
- Acompanhantes: regras, horários de visita
- Alimentação durante internação
- Wi-Fi, TV, estrutura de conforto

**Componentes visuais:**
- Box "Dica DRV" com 1 dica prática sobre este hospital (ex: "Dica DRV: se você precisa de exame de imagem urgente, o laboratório dentro do Hospital X funciona até 22h — evite ir ao centro de diagnóstico externo")
- Box "Importante" para regras do PS ou internação
- 2-3 destaques animados

**REGRAS ANTI-DOORWAY HS2:**
- NÃO explicar o que é coparticipação (pillar faz)
- NÃO explicar carências (pillar faz)
- NÃO explicar como funciona teleconsulta (conteúdo nacional)
- Foco é a EXPERIÊNCIA NESTE HOSPITAL ESPECÍFICO

---

### ── HS3: COMO CHEGAR E INFORMAÇÕES PRÁTICAS ──
- **ID:** `#como-chegar`
- **Background:** `#fff8f3`
- **Type:** CORE
- **Extensão:** 2-3 parágrafos + cards

**Conteúdo:**

- **Transporte público:** Linhas de ônibus que passam na porta ou próximo, estação de metrô/BRT mais perto, tempo a pé da estação. Se a cidade tem app de transporte integrado, mencionar.
- **Carro:** Referências de acesso (avenidas principais), estacionamento (próprio? rotativo? gratuito? valor?), valet (se houver).
- **Para quem vem de fora da cidade:** De qual rodovia/entrada acessar, tempo estimado de cidades vizinhas que fazem parte da área de cobertura.

- **Card de informações práticas (borda laranja):**
  - Endereço completo (aqui SIM pode repetir — é a razão de ser desta seção)
  - Telefone
  - Horário do PS (se 24h, especificar setores com horário diferente: lab, imagem, farmácia)
  - Estacionamento (sim/não + detalhes)
  - Acessibilidade (rampa, banheiro adaptado, elevador)

**Componentes visuais:**
- Card com borda laranja contendo as informações práticas
- Referência de localização por bairro e vias de acesso
- 1 destaque animado

**REGRAS ANTI-DOORWAY HS3:**
- Esta é a ÚNICA seção onde endereço e telefone aparecem
- O ângulo é COMO CHEGAR, não ONDE FICA — a S4 diz onde fica, aqui explica como acessar
- NÃO reproduzir tabela de cobertura por bairro (S5 do artigo de cidade faz)

---

### ── HS4: QUAIS PLANOS DÃO ACESSO A ESTE HOSPITAL ──
- **ID:** `#planos-acesso`
- **Background:** `#f8f9fa`
- **Type:** BRIDGE → artigo de cidade + pillars
- **Extensão:** 2-3 parágrafos + CTA

**Conteúdo:**

- **Parágrafo 1:** Resposta direta — quais produtos dão acesso a este hospital:
  - Nosso Plano: SIM (rede própria = acesso a todos os hospitais próprios)
  - Mix: SIM (inclui rede própria + credenciados)
  - Pleno (se disponível na cidade): SIM
  - NÃO detalhar cada produto (pillars fazem isso). Apenas a relação produto → acesso a este hospital.

- **Parágrafo 2:** Internações e cirurgias neste hospital são isentas de coparticipação em qualquer modalidade. Consultas e exames seguem a tabela do plano. Link para pillar coparticipação.

- **Parágrafo 3:** CTA direto — "Para contratar um plano que dá acesso ao [Nome do Hospital], faça sua cotação gratuita. A equipe da DRV Corretora orienta a escolha da modalidade mais adequada ao seu perfil."

- **Link obrigatório para artigo de cidade:** "Para ver todos os planos disponíveis em [Cidade], preços e como contratar, consulte nosso [guia completo do plano Hapvida em Cidade]."

**Componentes visuais:**
- Link obrigatório para artigo de cidade no final desta seção

**REGRAS ANTI-DOORWAY HS4:**
- NÃO listar preços (artigo de cidade S2 faz)
- NÃO comparar produtos em detalhe (pillars fazem)
- NÃO explicar carências (pillar faz)
- NÃO listar documentos de contratação (pillar Como Contratar faz)
- NÃO reproduzir steps de contratação
- PODE fazer a ponte produto → acesso a este hospital específico (informação única)

---

### ── FAQ ──
- **ID:** `#faq`
- **Background:** branco
- **Total:** 6-8 perguntas
- **100% sobre ESTE hospital** — nenhuma pergunta genérica sobre plano ou cidade

**Exemplos de perguntas válidas (adaptar ao hospital):**
- "O [Hospital X] tem UTI neonatal?"
- "O [Hospital X] faz cirurgia bariátrica?"
- "O PS do [Hospital X] atende crianças?"
- "Tem estacionamento no [Hospital X]?"
- "Como agendar consulta no [Hospital X]?"
- "O [Hospital X] faz parto humanizado?"
- "Preciso de encaminhamento para ser atendido no [Hospital X]?"
- "O [Hospital X] tem emergência ortopédica 24h?"
- "Posso fazer exame de imagem no [Hospital X] ou só no centro de diagnóstico?"
- "Qual o horário de visita no [Hospital X]?"

**Perguntas PROIBIDAS (respondidas em outros lugares):**
- "Qual o plano mais barato em [cidade]?" → artigo de cidade S2
- "O que é coparticipação?" → pillar
- "Qual a carência?" → pillar
- "Como contratar?" → pillar + artigo de cidade S7
- "Hapvida ou Unimed?" → artigo de cidade S6
- "Quais hospitais a Hapvida tem em [cidade]?" → artigo de cidade S4
- "Hapvida cobre parto?" → pillar cobertura (a menos que a pergunta cite ESTE hospital: "O [Hospital X] faz parto?")

**REGRAS ANTI-DOORWAY FAQ:**
- Cruzar com FAQ do artigo de cidade via Supabase (`consultar_faqs_catalogo`, `consultar_artigo`) — ZERO overlap
- Cruzar com FAQ de outros artigos de hospital da mesma cidade — ZERO overlap
- Toda pergunta DEVE conter o nome do hospital
- Se a pergunta pode ser respondida sem mencionar este hospital específico, ela não pertence aqui

---

### ── CTA FINAL ──

Após o FAQ, inserir o 2º (e último) `[elementor-template id="11215"]` em div com `style="margin-bottom:4px;"`.

---

### ── CONCLUSÃO ──
- **Extensão:** 2 parágrafos curtos
- **Parágrafo 1:** O que torna este hospital valioso para quem mora na região — síntese da experiência, não da ficha técnica.
- **Parágrafo 2:** Link para artigo de cidade ("Para conhecer toda a rede Hapvida em [Cidade], incluindo preços e outros hospitais, acesse nosso guia completo") + CTA final com classe `acao-abrir-popup`.
- **Menção DRV:** 1 menção sutil (máx.) — "A equipe da DRV Corretora pode ajudar a escolher o plano que dá acesso ao [Hospital]."

---

## LINKS INTERNOS OBRIGATÓRIOS

**Regra principal (V4.5.0): cada URL aparece NO MÁXIMO 1× por artigo.**

Escolher o MELHOR ponto para cada link — não repetir em múltiplas seções. Se o artigo de cidade precisa ser linkado, posicionar na HS4 (ponto de conversão), não no lead + HS2 + HS4 + conclusão.

| De (artigo de hospital) | Para | Onde (1× apenas) |
|------------------------|------|-------------------|
| HS1 | 1 link externo contextual (Hapvida oficial, CNES, CRM, RI Hapvida) | No corpo, onde citar dados verificáveis |
| HS2 | Pillar Coparticipação (box Importante) | "Internações isentas — detalhes no guia de coparticipação" |
| HS3 | Cross-link cidade vizinha OU artigo de cidade S5 | Escolher 1 dos 2, não ambos |
| HS4 | Artigo de cidade (hub) | "Guia completo do plano Hapvida em [Cidade]" |
| FAQ | Pillar Carências | Onde mencionar carência de parto/cirurgia + link |

**Mínimo:** 4 links internos únicos + 2 links externos
**Máximo por URL:** 1× (nenhuma repetição)
**Espaçamento:** mínimo 150 palavras entre dois links consecutivos

### O que NÃO fazer (anti-padrão V4.4.0):
- ❌ Linkar artigo de cidade 3× (lead + HS4 + conclusão) → ✅ Linkar 1× na HS4
- ❌ Linkar Nosso Plano + Mix + Coparticipação na mesma HS4 → ✅ Mencionar produtos como texto, linkar só 1 pillar
- ❌ Repetir link de coparticipação no box Importante + HS4 → ✅ Linkar 1× no box Importante
- ❌ IBGE + ANS no rodapé de todo artigo → ✅ Variar: CNES, CRM regional, SBP, Hapvida oficial, RI Hapvida

### Links Externos (mínimo 2)
- **1 link contextual NO CORPO** (HS1 ou HS2): página oficial do hospital na Hapvida, RI Hapvida (investimentos), CNES/DataSUS
- **1-2 links no rodapé**: CRM regional, SBP, FEBRASGO, SBC — variar conforme perfil do hospital
- **Não usar IBGE e ANS** se os artigos de cidade da mesma localidade já os utilizam — diversificar fontes entre os conteúdos do site

---

## REGRAS VISUAIS

Segue **100% do design system** do hapvida-article-builder V4.5.0:
- Mesmos componentes, cores, fontes, espaçamentos
- Mesmo `<style>` e `<script>`
- Mesmo anti-wpautop
- Font-size 18px para parágrafos

**Limites quantitativos do artigo de hospital:**

| Elemento | Limite |
|----------|--------|
| Seções numeradas | 4 (HS1-HS4) |
| `[elementor-template]` | 2 (após HS2 + após FAQ) |
| Texto grifado animado | mínimo 6 |
| FAQ perguntas | 6-8 |
| FAQ com nome do hospital | 100% |
| Menções DRV | máx. 1 |
| Links internos únicos | 4+ |
| Cada URL interna | máx. 1× (zero repetição) |
| Links externos | 2+ (1 no corpo + 1-2 rodapé) |
| Espaçamento entre links | mín. 150 palavras |
| Parágrafos | máx. 4 linhas (mesmo do skill) |
| Blocos de produção | 1 (artigo curto — entrega única) |

---

## PROCESSO DE PRODUÇÃO

### Fase 1 — Configuração
1. Ler SKILL.md + references/
2. Consultar artigo de cidade da mesma localidade no Supabase (`consultar_artigo`)
3. Ler pillar pages relevantes (coparticipação, carências, rede própria, como contratar) — `.txt` em `references/pillars-fonte/` (ou `/mnt/project/` se dentro do projeto)
4. **Extrair o que a S4 do artigo de cidade já diz sobre ESTE hospital**
5. **Consultar Supabase** (`consultar_hospitais_cidade`, `consultar_artigo`) — verificar se já existem artigos de hospital na mesma cidade. Cruzar FAQ (`consultar_faqs_catalogo`) e overlaps (`consultar_overlaps_doorway`).
6. Produzir tabela "O QUE NÃO REPRODUZIR" (obrigatória, visível no chat)
7. Produzir outline com FAQ planejadas (cruzadas contra FAQ do artigo de cidade E de outros artigos de hospital)
8. Apresentar ao usuário para aprovação

### Fase 2 — Produção
- **Bloco único:** Introdução (Lead GEO) + Sumário + HS1 + HS2 + CTA + HS3 + HS4 + FAQ + CTA final + Conclusão + `<style>` + `<script>`. **O JSON-LD NÃO entra aqui** — é gerado em execução separada (ver SKILL.md → "Geração de Schema"), só quando o usuário pedir.
- Artigo curto — entrega em 1 bloco (não 2 ou 3)

### Fase 3 — Verificação (execuções separadas, sob comando)
A verificação é feita pelas **três auditorias pós-artigo** descritas no `SKILL.md` ("AUDITORIAS PÓS-ARTIGO — EXECUÇÕES SEPARADAS"). Cada uma roda isolada, só quando o usuário pedir, sem pressa:
- **Modo 1 — Veracidade factual** (web + `consultar_dados_canonicos`/`consultar_coparticipacao` + pillar de cidade).
- **Modo 2 — Requisitos da skill** (checklist HS1-HS4 + AUDITs 4/6/7 da `hapvida-seo-auditor`).
- **Modo 3 — Anti-doorway** (investigação ao banco + comparação com artigos de hospital irmãos e a S4 do pillar).
Não rodar as três juntas nem automaticamente — o objetivo é o melhor artigo da SERP, não a entrega rápida.

### Fase 4 — Registro no Supabase

Registrar via MCP `BD - criar`:

- **`registrar_artigo_novo`** — slug, URL, hospital, cidade, artigo de cidade vinculado, versão, status, H2s usados, campo semântico
- **`registrar_faqs_artigo`** — todas as FAQs locais do artigo
- **`registrar_hospitais_artigo`** — registrar o hospital alvo + qualquer hospital de retaguarda citado
- **`registrar_links_artigo`** — todos os links de saída (de e para)

Se houver overlap detectado com o artigo de cidade ou outros hospitais da mesma cidade, registrar via `adicionar_pendencia` para resolução futura.

O arquivo `references/database-hospitais.md` está descontinuado — não atualizar mais.

---

## TÍTULO SEO E META DESCRIPTION

**Título (máx 60 chars):**
```
Hospital [Nome] Hapvida [Cidade]: Guia Completo [ano_atual]
```

Exemplos:
- `Hospital Aldeota Hapvida Fortaleza: Guia Completo [ano_atual]`
- `Hospital Promed Hapvida Goiânia: Guia Completo [ano_atual]`
- `Hospital Rio Mar Hapvida Belém: Guia Completo [ano_atual]`

**Meta description (máx 160 chars):**
```
Tudo sobre o Hospital [Nome] da Hapvida em [Cidade]: atendimento, especialidades, como chegar e quais planos dão acesso. Guia atualizado [ano_atual].
```

---

## MANTRA DO ARTIGO DE HOSPITAL

> "O artigo de cidade diz que o hospital existe. Este artigo diz como é estar lá dentro."
> "Se o dado já está na S4, ele não entra aqui. Se ele explica o plano, pertence ao pillar. Este artigo é sobre a EXPERIÊNCIA neste hospital."
> "Toda FAQ deve conter o nome do hospital. Se a pergunta funciona sem o nome, está no lugar errado."
> "Cada artigo de hospital é um spoke que fortalece o hub da cidade. Mais spokes = mais autoridade tópica."
