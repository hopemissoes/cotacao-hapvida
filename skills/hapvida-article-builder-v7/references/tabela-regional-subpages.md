# Tabela Regional Subpages — Article Type TR

Subpáginas-filha de `/tabela-de-preco-hapvida/` que existem para **ranquear duas imagens no image pack do Google**.

**URL pattern:** `https://tabelaplanos.com.br/tabela-de-preco-hapvida/[cidade-slug]/`

**Estrutura:** TR1 → TR5 + FAQ + Conclusão. Cinco seções, não sete. Mais enxuto que artigo de cidade (S1-S7) e mais focado que artigo de hospital (HS1-HS4).

---

## When to Use

Triggers que disparam este article type:

- "Artigo de tabela de preço para [cidade]"
- "Subpágina de tabela [cidade]"
- "Tabela Hapvida [cidade] empresarial e individual"
- "Página para ranquear imagem da tabela Hapvida [cidade]"
- "TR1", "TR5", "artigo TR", "subpágina de tabela"
- Menção a "image pack", "ranquear imagem", "image search Hapvida"
- URL pattern `/tabela-de-preco-hapvida/[cidade]/`

**NÃO usar quando:**

- Usuário pede artigo geral de cidade → usar arquitetura S1-S7 (este SKILL.md principal)
- Usuário pede artigo de hospital → usar `references/artigo-hospital.md` (HS1-HS4)
- Usuário pede artigo de cobertura → usar skill `hapvida-coverage-builder` (C1-C7)

---

## Core Principle — Image-First, Not Article-First

Estes artigos existem por **uma única razão estratégica**: ranquear 2 imagens (Empresarial Coparticipação Total + Individual Coparticipação Total) no image pack do Google para queries `tabela hapvida [cidade]`.

O texto que envolve as imagens não é o produto. É **wrapper SEO** que precisa cumprir 4 funções:

1. **Substantivo o bastante** para não ser thin content (penalidade que tira a página E as imagens do índice)
2. **Rico em contexto ao redor de cada imagem** (Google ranqueia imagem por proximidade textual, ~300-400 palavras de contexto por imagem é o mínimo)
3. **H2 com keyword exata** acima de cada imagem (sinal semântico forte)
4. **Não doorway** com as 3 pillars do projeto (Tabela de Preços, Individual, Empresarial) — sob risco de a URL ser desindexada e as imagens irem junto

Diferente do artigo de cidade (S1-S7), aqui a duplicação de dados com as pillars **não é problema canibalístico** — pelo contrário, reforça sinal semântico para as imagens. O risco é apenas a URL ser flagada como doorway.

---

## Architecture TR1-TR5

> **[V7] A TR2 subiu para antes do sumário.** A TR já era image-first; a v7 formaliza e trava: a IMAGEM 1 é o primeiro conteúdo depois da TR1. **[V7.1] O sumário vem colado na IMAGEM 1** (só a leitura da imagem entre as duas) e o **1º formulário desceu para depois do sumário**. TR2 e TR3 continuam sendo os dois primeiros H2 de conteúdo — nenhum H2 de TR4/TR5 pode passar na frente. Trava: `checkpoint_preco_primeiro.py <arquivo> tr`.

```
<article>
  [TR1: INTRODUÇÃO]                          — branco (border-bottom)
                                              lead com posicionamento tarifário local
                                              + links 3 pillars (tabelas, individual, empresarial)
                                              + link pillar de cidade
  [TR2: TABELA EMPRESARIAL]  ⭐ [V7]         — branco — 1º conteúdo, ANTES do sumário
                                              H2 keyword-rico
                                              ~400 palavras de contexto local
                                              IMAGEM 1 (empresarial)
                                              ~200 palavras de "leitura" da imagem
  [SUMÁRIO]  ⭐ [V7.1]                        — gradiente #fafbfc → #f0f4f8 — colado na IMAGEM 1
                                              apenas 5 itens + CTA "Faça uma Cotação"
                                              1º item aponta para a âncora da TR2, acima dele
  [elementor-template — 1º formulário]       id="cotacao-1" — [V7.1] agora DEPOIS do sumário
                                              + bridge curta + link pillar empresarial
  [TR3: TABELA INDIVIDUAL]                   — #f8f9fa (cinza)
                                              H2 keyword-rico
                                              ~400 palavras de contexto local
                                              IMAGEM 2 (individual)
                                              ~200 palavras de "leitura" da imagem
                                              bridge curta + link pillar individual
  [TR4: POR QUE [CIDADE] TEM ESSE PREÇO]     — branco (CORE único)
                                              3 fatores específicos da cidade
                                              tabela comparativa com 3 outras capitais
                                              ESTA SEÇÃO JUSTIFICA A EXISTÊNCIA DA URL
  [TR5: PROMOÇÕES VIGENTES NA CIDADE]        — #f8f9fa (cinza)
                                              gatilho regional específico
                                              + 15% padrão (já nas imagens)
  [FAQ]                                       — branco
                                              6-8 perguntas focadas em interpretar tabelas
                                              zero overlap com pillars
  [elementor-template — 2º formulário]       div sem id
  [CONCLUSÃO]                                 — gradiente #f8fafc → #f1f5f9
                                              resumo dos 2 valores + assinatura DRV
  [JSON-LD ImageObject schema]               — script type="application/ld+json"
                                              2 schemas (1 por imagem)
  [<style>]                                   — penúltimo
  [<script>]                                  — último
</article>
```

### Não inclui (cortes mandatórios — caem em doorway)

| Seção que NÃO existe | Por quê |
|---|---|
| Visão Geral por Modalidade | Conteúdo genérico — pillars já cobrem |
| Decisão entre modalidades (Perfil A/B, MEI/CLT/PJ) | Educacional puro — pillars empresarial e individual cobrem |
| Faixa Etária e Reajuste educacional | Conteúdo nacional ANS — pillar empresarial cobre |
| Atualizações detalhadas / histórico reajustes | Território pillar empresarial |
| Bloco Adesão extenso | Sem imagem associada — só mencionar 1× na TR1 |
| Coparticipação completa (cards/tabela) | Pillar coparticipação cobre |
| Tipos de plano (Ambulatorial/Enfermaria/etc.) | Pillar individual cobre |
| Comparativo com Amil/SulAmérica/Bradesco | Pillar individual cobre |
| Direitos Art. 30/31 | Pillar empresarial cobre |
| Tecnologia/Telemedicina | Pillars individual e empresarial cobrem |

---

## Anti-Doorway — As 3 Pillars Concorrentes

⚠️ **CRÍTICO:** Estas 3 pillars **estão no projeto Claude do usuário** (arquivos `.txt` anexados). Mesmo assim, NUNCA reproduzir conteúdo delas no artigo TR. A presença no projeto serve para Claude saber o que existe e o que NÃO repetir.

### 1. Pillar `/tabela-de-preco-hapvida/` (PILLAR PAI)

Esta é a pillar pai. A subpágina TR é filha dela.

**NUNCA reproduzir:**

- Tabelas regionais em HTML (BH, Belém, e demais cidades que a pillar exibe)
- Imagem-hero genérica da pillar
- Comparação total entre todas as cidades brasileiras
- Mecânica de coparticipação completa (Total vs Parcial com valores nacionais)
- Tabela "Valores de Coparticipação por Procedimento" (consultas, exames, terapias)
- Lista de cidades onde Hapvida opera

**TR pode (BRIDGE leve):**

- Mencionar 1× na TR1 que faz parte da família de tabelas de preço
- Linkar à pillar como "visão nacional"
- Adaptar a tabela comparativa de TR4 com apenas 3-4 cidades (não todas)

### 2. Pillar `/plano-individual-hapvida/`

**NUNCA reproduzir:**

- Narrativa "Hapvida é uma das poucas operadoras que ainda comercializa individual — Amil, Golden Cross e Bradesco encerraram comercialização entre 2017-2020"
- Tabela comparativa de concorrentes (Amil suspensa / SulAmérica restrita / Bradesco não oferece / Golden Cross descontinuado)
- Tipos de plano individuais (Ambulatorial / Enfermaria / Apartamento / Obstétrico / NotreLife / NotreLife 50+ / Nosso Médico / Mix)
- Tabela resumo comparativo das modalidades
- Sistema de Coparticipação detalhado (CT vs CP cards, valores Tabela 1 vs Tabela 2)
- Coberturas e Carências (cards 24h/30d/180d/300d/24m)
- Rede Hospitalar Nacional (lista regional Norte/NE/SE/Sul-CO)
- Histórico de Reajustes ANS (2023: 9,63% / 2024: 6,91% / 2025: 6,06%)
- Inovações Tecnológicas (Telemedicina 30M/ano, App, Programas Preventivos)
- Aspectos Regulatórios (RN 623/2024, Lei 14.454/2022)
- Direitos do Beneficiário (portabilidade, proteção cancelamento, reativação)
- Processo de Contratação (documentos, formas de pagamento)
- Quando Vale a Pena (recomendado/não compensa/considerar alternativas)
- Tendências e Perspectivas (R$ 2bi expansão, IA diagnóstico, home care digital)

**TR pode (BRIDGE leve em TR3):**

- 1 parágrafo: "modalidade individual contratada por CPF, sem necessidade de CNPJ ou vínculo com entidade"
- 1 menção: "alternativa para autônomos, profissionais liberais e famílias sem acesso a contrato empresarial"
- 1 frase: "valores em média 15-25% superiores ao empresarial pela mesma faixa etária"
- 1 frase sobre coparticipação: "internações e cirurgias permanecem 100% isentas"
- Link à pillar individual no final do bloco TR3 para "tipos de plano, regras de cobertura, comparativo de concorrentes e histórico de reajustes"

### 3. Pillar `/plano-empresarial-hapvida/`

**NUNCA reproduzir:**

- "Mais de 70% dos beneficiários brasileiros estão em contratos empresariais"
- Modalidades Super Simples (2-29 vidas) / PME (30-99) / Corporativo (100+) — gatekeeping ANS por número de vidas
- "MEI com CNPJ ativo há no mínimo 6 meses, conforme RN 432/2017"
- "Na marca Hapvida, mínimo de 2 vidas"
- Reajuste 11,5% PME 2025-2026 + tabela comparativa de operadoras (Hapvida vs NDI vs Bradesco vs SulAmérica vs Amil vs Unimed)
- Pool de risco RN 565/2022
- Sinistralidade 68% 1T24
- Produtos Hapvida (Nosso Plano / Plano Mix / Plano Pleno / Infinity 1000)
- Acesso a hospitais premium (Einstein, Sírio-Libanês, Fleury via Infinity)
- Programa Qualivida (11 programas com certificação QMentum)
- Coparticipação Total vs Parcial (até 35% redução / até 20% redução)
- Tabela "Valores de Coparticipação por Procedimento" (SP/BH vs Demais Capitais)
- Reajuste por faixa etária (10 faixas, trava 6x ANS)
- Direitos pós-vínculo Art. 30 / Art. 31 (Lei 9.656/98)
- Portabilidade RN 438/2018
- Tecnologia (Telemedicina 24h 25+ especialidades / Portal Empresa / App Hapvida)
- Processo de Contratação (4 etapas / 10 dias úteis)
- Benefícios Fiscais (dedução IRPJ/CSLL, CLT Art. 458 §2° IV)
- Comparação com cooperativas médicas e seguradoras

**TR pode (BRIDGE leve em TR2):**

- 1 parágrafo: "modalidade mais procurada na capital cearense" (sem cravar "70%")
- 1 frase: "exige CNPJ ativo, incluindo MEI" (sem detalhar 6 meses ou RN 432)
- 1 frase: "valores em média 15-25% inferiores ao individual"
- 1 frase sobre coparticipação por procedimento: citar 2-3 valores específicos da cidade (R$ 25,42 consulta eletiva Tabela 1, etc.)
- 1 frase: "internações e cirurgias totalmente isentas"
- Link à pillar empresarial no final do bloco TR2 para "documentação, modalidades Super Simples/PME, Qualivida, reajuste e direitos pós-demissão"

---

## Substitution Test (Audit 5 do hapvida-seo-auditor)

Para cada parágrafo, H2, e FAQ, fazer mentalmente: "Se eu trocar [cidade] por [outra cidade do mesmo grupo tarifário], este texto continua fazendo 100% sentido?"

**SE SIM em uma seção inteira → essa seção é doorway. Reescrever ou cortar.**

### Pontos onde substitution test DEVE FALHAR (conteúdo único exigido)

| Localização | O que precisa ser único |
|---|---|
| TR1 introdução | Pelo menos 1 frase só faz sentido naquela cidade (sede nacional / referência Tabela 1 / valor inicial específico) |
| TR4 inteira | 3 fatores únicos da cidade (ano de fundação, número de beneficiários no estado, % rede própria, modelo operacional local) |
| TR4 tabela comparativa | Ordem das cidades comparadas varia conforme a cidade do artigo. Para Recife, comparar com Fortaleza primeiro (ambas Tabela 1). Para BH, comparar com SP primeiro (ambas Tabela 2). |
| TR5 promoções | Pelo menos 1 gatilho regional específico (migração Amil Nordeste para cidades NE; entrada NotreDame para cidades Sudeste; etc.) |
| 2-3 FAQs | Pergunta exclusiva sobre região metropolitana ou bairros da cidade ("Vale para Caucaia/Maracanaú/Aquiraz?" em Fortaleza; "Vale para Olinda/Jaboatão/Camaragibe?" em Recife) |

### Pontos onde substitution test PODE PASSAR (bridge legítimo)

| Localização | Conteúdo aceito |
|---|---|
| TR2/TR3 parágrafos descritivos | Definição enxuta de empresarial/individual (50-80 palavras cada). Tudo além disso vira doorway. |
| 1-2 FAQs estruturais | Perguntas sobre interpretação geral de tabela (dependentes por pessoa, desconto promocional já aplicado, etc.) |
| TR1 último parágrafo (atualização) | Frase com `[mes_atual] de [ano_atual]` e assinatura DRV |

---

## Image-First Optimization

### Filename Pattern

```
tabela-hapvida-[cidade-slug]-[modalidade]-coparticipacao-total-[ano].webp
```

**Modalidade:** `empresarial` ou `individual` (sempre lowercase, sem acento).

**Cidade slug:** mesmo slug do artigo de cidade registrado no Supabase (consultar via `consultar_artigo`).

**Ano no filename:** atualizar conforme ciclo de release anual da tabela (`2026` em 2026, `2027` quando a tabela for revisada para 2027 e a imagem regerada).

Exemplos:
- `tabela-hapvida-fortaleza-empresarial-coparticipacao-total-2026.webp`
- `tabela-hapvida-fortaleza-individual-coparticipacao-total-2026.webp`
- `tabela-hapvida-recife-empresarial-coparticipacao-total-2026.webp`
- `tabela-hapvida-belo-horizonte-empresarial-coparticipacao-total-2026.webp` (hífen, não acento)
- `tabela-hapvida-ribeirao-preto-individual-coparticipacao-total-2026.webp`

A presença de `coparticipacao-total` no nome:
- Sinaliza explicitamente para o Google qual é o tipo de coparticipação retratado na imagem (importante porque há também a versão parcial nas pillars)
- Permite produzir variações futuras (`-coparticipacao-parcial-2026.webp`) sem ambiguidade
- Mais riqueza semântica no filename — sinal forte para image search ranking

**NUNCA:**
- `tabela-precos-hapvida-2026.webp` (genérico — esse fica na pillar pai)
- `tabela_hapvida_fortaleza_2026.webp` (underscores não otimizam image search)
- `IMG_5234.webp` (sem semântica)
- `tabela-hapvida-fortaleza-2026.webp` sem modalidade nem tipo de copart (ambíguo)

### Alt Text (mínimo 150 caracteres, máximo 250)

Pattern:

```
Tabela Hapvida [Cidade] [modalidade] [ano] — referência por faixa etária ANS, valores oficiais com coparticipação total [característica regional opcional]. Valores entre [valor inicial] e [valor final]
```

Estrutura: o "Valores entre X e Y" no final ajuda image search a indexar a imagem para queries com filtros de preço aproximado, além de descrever o que está visualmente impresso.

Exemplos:

- Empresarial Fortaleza: "Tabela Hapvida Fortaleza empresarial 2026 — referência por faixa etária ANS, valores oficiais com coparticipação total na capital cearense. Valores entre 87,35 e 513,03"
- Individual Recife: "Tabela Hapvida Recife individual 2026 — referência por faixa etária ANS, valores oficiais com coparticipação total. Valores entre 101,77 e 591,19"

Os valores no alt text **descrevem o que está burned-in na imagem** — mantidos hardcoded (sem shortcode). Quando regenerar a imagem com novos valores, atualizar alt junto.

### Title Attribute

Pattern: `Tabela Hapvida [Cidade] [modalidade] [ano_atual] — Preços por Faixa Etária`

Modalidade em **lowercase** (`empresarial`, `individual`) por consistência com o pattern oficial. Title é mais curto que alt, serve como tooltip e reforço semântico secundário.

Exemplos:
- "Tabela Hapvida Fortaleza empresarial 2026 — Preços por Faixa Etária"
- "Tabela Hapvida Recife individual 2026 — Preços por Faixa Etária"

### Figcaption (visível abaixo da imagem)

Pattern:

```
Tabela referência Plano Hapvida [modalidade] (coparticipação total) [Cidade] — valores por faixa etária ANS (Resolução Normativa nº 63/2003). Atualizada em [mes_atual] de [ano_atual].
```

Modalidade em **lowercase** (consistência com title/alt). "Tabela referência" sinaliza ao Google e ao usuário que essa é uma das tabelas existentes (não a única) — preserva o flow para outras subpáginas TR de outras cidades.

CSS do `<figcaption>`:
```
style="text-align: center; font-size: 14px; color: #718096; margin-top: 10px; font-style: italic;"
```

Exemplos:
- "Tabela referência Plano Hapvida empresarial (coparticipação total) Fortaleza — valores por faixa etária ANS (Resolução Normativa nº 63/2003). Atualizada em [mes_atual] de [ano_atual]."
- "Tabela referência Plano Hapvida individual (coparticipação total) Recife — valores por faixa etária ANS (Resolução Normativa nº 63/2003). Atualizada em [mes_atual] de [ano_atual]."

### Tag `<figure>` Completa — Template Mandatório

Estrutura HTML exata a usar em TODOS os artigos TR. A ordem dos atributos e a configuração CSS são **prescritivas**:

```html
<figure style="margin: 0 0 24px 0; padding: 0;"><img style="max-width: 70%; height: auto; border-radius: 12px; border: 1px solid #e2e8f0; display: block; margin: 0 auto;" title="Tabela Hapvida [Cidade] [modalidade] [ano] — Preços por Faixa Etária" src="https://tabelaplanos.com.br/wp-content/uploads/[ANO]/[MES]/tabela-hapvida-[cidade]-[modalidade]-coparticipacao-total-[ano].webp" alt="Tabela Hapvida [Cidade] [modalidade] [ano] — referência por faixa etária ANS, valores oficiais com coparticipação total [característica regional]. Valores entre [valor inicial] e [valor final]" width="1080" height="1080" />
<figcaption style="text-align: center; font-size: 14px; color: #718096; margin-top: 10px; font-style: italic;">Tabela referência Plano Hapvida [modalidade] (coparticipação total) [Cidade] — valores por faixa etária ANS (Resolução Normativa nº 63/2003). Atualizada em [mes_atual] de [ano_atual].</figcaption></figure>
```

**Especificações fixas (NÃO ajustar):**

| Atributo | Valor | Por quê |
|---|---|---|
| `<figure>` style margin | `margin: 0 0 24px 0` | Espaço inferior padronizado entre figure e próximo bloco |
| `<img>` style `max-width` | `70%` | Centraliza a imagem com respiro lateral em desktop; mobile fica ~100% por causa do height auto |
| `<img>` style `display` | `block` + `margin: 0 auto` | Centraliza horizontalmente |
| `<img>` `width` × `height` | `1080` × `1080` | Imagem **quadrada** Instagram-friendly. Produzir as imagens nessa proporção 1:1 |
| `<img>` `border-radius` | `12px` | Identidade visual do site |
| `<img>` `border` | `1px solid #e2e8f0` | Idem |
| `<figcaption>` style | `text-align: center; font-size: 14px; color: #718096; margin-top: 10px; font-style: italic` | Estilo de legenda em todo o site |

**Ordem dos atributos da `<img>` (prescritiva):**

```
style → title → src → alt → width → height
```

Manter exatamente essa ordem por consistência editorial e para facilitar busca/manutenção via grep no banco de artigos.

**Atributos NÃO incluídos no template:**

- `loading="lazy"` — omitido por padrão. Se o site não tiver plugin de lazy loading (WP Rocket, Optimole, ou tema com lazy nativo), adicionar manualmente após o `border` no style.
- `decoding="async"` — opcional, omitido por padrão.

**Imagem em produção:** as imagens devem ser geradas em **1080×1080 pixels** (formato quadrado). Isso é diferente do template anterior (que tinha 800×900 retangular). Confirmar com o pipeline de geração (Puppeteer no VPS, ou processo manual) antes de produzir o lote das 10 cidades.

### JSON-LD ImageObject Schema (FINAL DO ARTIGO, ANTES DO `<style>`)

```html
<script type="application/ld+json">{
  "@context":"https://schema.org",
  "@graph":[
    {
      "@type":"ImageObject",
      "contentUrl":"https://tabelaplanos.com.br/wp-content/uploads/2026/05/tabela-hapvida-[cidade]-empresarial-coparticipacao-total-2026.webp",
      "name":"Tabela Hapvida [Cidade] Empresarial 2026",
      "description":"Tabela oficial de preços do plano Hapvida empresarial em [Cidade] com coparticipação total, valores por faixa etária ANS (0-18 a 59+), de [valor inicial] a [valor final]",
      "caption":"Tabela oficial Hapvida [Cidade] — plano empresarial coparticipação total por faixa etária ANS",
      "representativeOfPage":true,
      "creator":{
        "@type":"Organization",
        "name":"DRV Corretora"
      }
    },
    {
      "@type":"ImageObject",
      "contentUrl":"https://tabelaplanos.com.br/wp-content/uploads/2026/05/tabela-hapvida-[cidade]-individual-coparticipacao-total-2026.webp",
      "name":"Tabela Hapvida [Cidade] Individual 2026",
      "description":"Tabela oficial de preços do plano Hapvida individual em [Cidade] com coparticipação total, valores por faixa etária ANS (0-18 a 59+), de [valor inicial] a [valor final]",
      "caption":"Tabela oficial Hapvida [Cidade] — plano individual coparticipação total por faixa etária ANS",
      "representativeOfPage":true,
      "creator":{
        "@type":"Organization",
        "name":"DRV Corretora"
      }
    }
  ]
}</script>
```

### Image Production Notes (visual design)

A imagem visual produzida NÃO pode ser parecida com as tabelas HTML simples que estão nas pillars Empresarial e Individual (que mostram valor por faixa em formato tabular puro). Para diferenciar visualmente:

- Header com logo Hapvida + identidade DRV
- Paleta laranja `#ff6b00` + branco do site
- Espaçamento generoso entre faixas
- Tipografia grande para os valores
- Marca d'água "DRV" discreta no canto
- Idealmente: pequeno elemento gráfico (chart, ícone, gradient) que diferencie de imagem de tabela genérica

Isso evita fingerprinting de duplicata pelo Google. Imagens visualmente únicas ranqueiam melhor que cópias de tabelas tabulares.

---

## Shortcode Strategy — Preços e Promoções em Artigos TR

### Preços — sempre shortcode, nunca hardcode

Vale a regra geral do site: zero valores fixos em conteúdo evergreen. Em artigos TR, isso é especialmente importante porque:

1. **Disciplina operacional:** se o admin atualizar preços no plugin e esquecer de regenerar a imagem, a discrepância entre texto (com shortcode atualizado) e imagem (com valor antigo) fica visível, forçando a regeneração.
2. **Hardcode mascara desatualização:** se o texto repete os valores da imagem em hardcode, ambos envelhecem juntos sem aviso. O artigo fica obsoleto silenciosamente.

#### Shortcodes que já existem (usar primeiro)

| Shortcode | Output | Onde usar no artigo TR |
|---|---|---|
| `[cidade_menorvalor]` | Menor valor empresarial copart total (chamariz) | TR1 lead, TR2 abertura, TR4 tabela comparativa, Conclusão (cards-resumo) |
| `[demais_capitais_consultas_eletivas]` | Coparticipação consulta eletiva Tabela 1 | TR2/TR3 bloco coparticipação, FAQ #3 |
| `[demais_capitais_exames_simples]` | Coparticipação exame simples Tabela 1 | Idem |
| `[demais_capitais_exames_complexos]` | Coparticipação exame complexo Tabela 1 | Idem |
| `[sp_bh_consultas_eletivas]` | Mesmo, para SP/BH (Tabela 2) | Subpáginas TR de SP ou BH |
| `[sp_bh_exames_simples]` | Idem | Idem |
| `[sp_bh_exames_complexos]` | Idem | Idem |

#### Shortcodes de valor pontual por faixa etária (uso em TR)

Para citar valores nas leituras de imagem ("começa em X e progride até Y"), usar o pattern do plugin de preços com sufixo de faixa etária. Não duplicar a tabela inteira em HTML — o artigo TR depende da imagem para ranquear.

| Shortcode | Output | Onde usar |
|---|---|---|
| `[cidade_emp_ambulatorialtotal_0]` | Empresarial faixa 0-18 (menor valor) | TR2 leitura da imagem, Conclusão card-resumo |
| `[cidade_emp_ambulatorialtotal_9]` | Empresarial faixa 59+ (maior valor) | TR2 leitura da imagem |
| `[cidade_ind_ambulatorialtotal_0]` | Individual faixa 0-18 (menor valor) | TR3 abertura, Conclusão card-resumo |
| `[cidade_ind_ambulatorialtotal_9]` | Individual faixa 59+ (maior valor) | TR3 leitura da imagem |

Substituir `cidade` pelo slug (`fortaleza`, `recife`, `salvador`, `belo-horizonte` com hífen, etc.).

**Confirmar com o admin do site:** o pattern com sufixo `_0` a `_9` deve estar habilitado no plugin de shortcodes. Se não estiver, cadastrar essas 4 combinações por cidade (40 shortcodes para 10 cidades — ou criar shortcode genérico que aceite cidade + modalidade + faixa como parâmetros).

#### Shortcodes que NÃO entram no artigo TR

| Shortcode | Por quê |
|---|---|
| `[cidade_menortabela]` | Renderiza tabela HTML completa — duplica a imagem-target |
| `[cidade_emp_ambulatorialtotal]` (sem `_faixa`) | Idem |
| `[cidade_ind_ambulatorialtotal]` (sem `_faixa`) | Idem |

Esses shortcodes de tabela completa são apropriados para artigos S1-S7 (city pillars), não para TR.

#### Onde MANTER hardcoded em artigos TR

Apenas dentro destes 4 pontos da `<img>` — porque descrevem a imagem visualmente:

1. Atributo `alt` (ex: "...de R$ 87,35 (0 a 18 anos) até R$ 513,03...")
2. Atributo `title`
3. Conteúdo do `<figcaption>`
4. Campo `description` no JSON-LD ImageObject schema

Quando regenerar a imagem com novos valores, atualizar esses 4 pontos juntos. São descrições do que está burned-in na imagem, não conteúdo dinâmico.

### Promoções — Estratégia híbrida em 3 camadas

Promoções são variáveis (desconto pode ser 10%, 15%, 20%; pode ter 3 ou 4 parcelas; pode encerrar). A estratégia recomendada combina 3 mecanismos para minimizar manutenção e preservar diferenciação por cidade.

#### Camada 1 — Elementor Template para card visual padrão

Criar **um** template no Elementor (ex: ID 11220) chamado "Card Promoção Padrão Hapvida". O template renderiza o card visual "[promocao_desconto] em [promocao_parcelas] parcelas" usando estilo grid2 + cor laranja `#ff6b00`.

Inserir em todas as subpáginas TR via:

```html
<div class="grid2" style="display:flex!important;flex-wrap:wrap!important;gap:16px!important;margin-bottom:24px;">
  [elementor-template id="11220"]
  
  <!-- segundo card: gatilho regional específico da cidade (texto manual) -->
  <div style="flex:1 1 300px!important;box-sizing:border-box!important;background:#fff;border:1px solid #e2e8f0;border-radius:20px;padding:28px 24px;">
    <!-- conteúdo local manual: "Por ser sede nacional..." etc. -->
  </div>
</div>
```

Quando a promoção mudar visualmente (cor, formato, layout), edita o template Elementor 1 vez e propaga para todas as subpáginas.

#### Camada 2 — Shortcodes simples para números variáveis

Criar 2-3 shortcodes no plugin de shortcodes (mesmo padrão de `[ano_atual]` e `[mes_atual]`):

| Shortcode | Output exemplo | Onde usar |
|---|---|---|
| `[promocao_desconto]` | `15%` | Dentro do template Elementor + em menções no texto da TR1, TR5 e FAQ |
| `[promocao_parcelas]` | `3` | Idem |
| `[promocao_validade]` | `até [mes_atual] de [ano_atual]` ou data específica | Disclaimer da nota |

Esses shortcodes leem de uma única opção/setting do admin WP. Quando a promoção mudar de 15% para 12%, edita 1 opção → texto e card atualizam em todas as subpáginas TR simultaneamente.

#### Camada 3 — Texto local sobre gatilho regional permanece manual

A parte que diferencia cada cidade — "Por ser sede nacional, Fortaleza concentra políticas comerciais específicas" / "Migração Amil Nordeste em Recife" / "Servidores públicos em Brasília" — **permanece como texto manual** na TR5 de cada artigo.

Por quê:
- Esses contextos são **estruturais e estáveis** (Fortaleza não vai deixar de ser sede; o servidor público não vai sumir de Brasília)
- Atualização é eventual, não mensal
- **Cada cidade tem seu gatilho único — que é exatamente o que protege contra doorway de cluster**

Manter manual também garante que se Claude refaz a TR5 de uma cidade, não há risco de quebrar a diferenciação entre as 10 subpáginas.

#### Resumo operacional

| O que muda | Onde editar | Frequência |
|---|---|---|
| % de desconto (15→12, etc.) | Opção do admin (`[promocao_desconto]`) | Mensal/trimestral |
| Nº de parcelas (3→4, etc.) | Opção do admin (`[promocao_parcelas]`) | Raramente |
| Validade da promoção | Opção do admin (`[promocao_validade]`) | Mensal |
| Visual do card | Template Elementor (ID 11220) | Esporádico |
| Gatilho regional Fortaleza/Recife/etc | Texto manual na TR5 de cada artigo | Apenas se mudar contexto comercial |
| Lista de situações específicas (30+ vidas, migração Amil, reativação) | Texto manual na TR5 de cada artigo | Apenas se mudar realidade |
| Data da última atualização | `[mes_atual] de [ano_atual]` (já existe) | Automático |

---

## Image Naming Strategy — Pillar vs Subpages

A pillar pai e as subpáginas filhas **NÃO competem entre si** porque miram queries diferentes.

### Pillar `/tabela-de-preco-hapvida/`

- **Imagem hero:** nome GENÉRICO, sem cidade. Ex: `tabela-hapvida-empresarial-2026.webp`, `tabela-hapvida-individual-2026.webp`, ou `tabela-hapvida-2026.webp` (mais amplo)
- **Cidade-referência visual:** BH (status quo atual) OU Fortaleza (alternativa de migração). Mostrar uma cidade só para evitar imagem-poluição.
- **Alt text:** descreve a tabela sem prender à cidade. Ex: "Tabela Hapvida 2026 — referência por faixa etária, valores oficiais com coparticipação total na principal capital"
- **Alvo de query:** `tabela hapvida`, `tabela hapvida 2026`, `preço plano hapvida` (queries amplas, alto volume)

### Subpages `/tabela-de-preco-hapvida/[cidade]/`

- **2 imagens com nome ESPECÍFICO** (city-named conforme pattern acima)
- **Alvo de query:** `tabela hapvida [cidade]`, `preço plano hapvida [cidade]`, `tabela hapvida [cidade] empresarial`, `tabela hapvida [cidade] individual` (queries long-tail, alta intenção comercial)

### Por que não compete

Filename específico **não exclui** imagem do image-pack da query ampla — Google pondera múltiplos sinais (alt, contexto textual, autoridade da URL). Mas filename específico **prioriza fortemente** a imagem para long-tail. A pillar mantém vantagem na ampla por filename genérico + autoridade superior da URL pai.

Cada uma das 20 imagens (10 cidades × 2 modalidades) compete por sua long-tail; a pillar compete pela ampla. Sem canibalização interna.

---

## Quantitative Limits — TR Articles

| Elemento | Limite |
|---|---|
| Seções numeradas | 5 (TR1-TR5) |
| Imagens-target | exatamente 2 (Empresarial Coparticipação Total + Individual Coparticipação Total) |
| Tabelas HTML | máximo 1 (somente comparativo de cidades em TR4 — opcional) |
| Formulários `[elementor-template]` | 2 (após TR2 + antes da Conclusão) |
| Texto grifado animado `.destaque-laranja-suave` | mínimo 8 |
| FAQ perguntas | 6-8 |
| FAQ com overlap das 3 pillars críticas | ZERO |
| FAQs estruturalmente locais | mínimo 50% (4 de 8) |
| Link à pillar `/tabela-de-preco-hapvida/` | 1 (na TR1 ou conclusão) |
| Link à pillar `/plano-empresarial-hapvida/` | 1 (no final da TR2) |
| Link à pillar `/plano-individual-hapvida/` | 1 (no final da TR3) |
| Link à pillar de cidade `/plano-hapvida-[cidade]/` | 1 (na TR1) |
| Outros links pillars (coparticipação, portabilidade, carências) | 1-2 opcionais |
| Cross-links a outras cidades | 1-2 (na tabela comparativa de TR4) |
| Links externos | opcional (ANS pode ser citado em TR4 sem link, ou linkado) |
| JSON-LD schemas | 1 bloco `<script type="application/ld+json">` com 2 ImageObjects |
| Menções DRV (E-E-A-T) | máximo 2 (TR1 + conclusão) |
| Tamanho do arquivo HTML | 35-50 KB |
| Sumário itens | 5 + 1 CTA "Faça uma Cotação" |

---

## Template Skeleton

Use os componentes do `references/components.md` (boxes, grids, FAQ details, animated highlight). Estrutura abreviada:

```html
<article>
  <!-- TR1: Introdução -->
  <section style="padding:20px 10px;border-bottom:1px solid #e2e8f0;margin-bottom:4px;">
    <h1>Tabela Hapvida [Cidade] [ano_atual]: Preços por Faixa Etária — Empresarial e Individual</h1>
    <p>Lead com posicionamento tarifário local + valor inicial + valor final empresarial</p>
    <p>Contextualização Tabela 1 ou Tabela 2 + razão estrutural</p>
    <p>Links pillars: cidade + tabela nacional</p>
    <p>Assinatura DRV + data atualização</p>
  </section>

  <!-- Sumário (5 itens + CTA) -->
  <section>...</section>

  <!-- TR2: Tabela Empresarial -->
  <section id="empresarial" style="padding:24px 14px;border-radius:20px;">
    <h2>Tabela Hapvida [Cidade] Empresarial [ano_atual]</h2>
    <p>Subtítulo descritivo</p>
    <div style="orange-bar"></div>
    
    <!-- ~400 palavras de contexto local -->
    <p>Por que empresarial é a mais procurada na cidade</p>
    <p>Introdução da tabela: o que ela mostra</p>
    
    <!-- IMAGEM 1 com figure + figcaption -->
    <figure>
      <img style="max-width: 70%; ..." title="..." src="..." alt="..." width="1080" height="1080" />
      <figcaption>...</figcaption>
    </figure>
    
    <!-- ~200 palavras de leitura da imagem -->
    <p>Análise dos valores: faixa inicial, faixa final, salto 49-53/54-58, desconto 15% já aplicado</p>
    <p>Quem contrata: CNPJ ativo, mínimo 2 vidas, coparticipação por procedimento Tabela 1 (R$ 25,42 etc.)</p>
    
    <!-- Bridge curta + link pillar -->
    <p>Para regras de modalidades Super Simples/PME, documentação, Qualivida, direitos pós-demissão → <a href="/plano-empresarial-hapvida/">guia completo do plano empresarial Hapvida</a></p>
  </section>

  <!-- Formulário 1 -->
  <div id="cotacao-1">[elementor-template id="11215"]</div>

  <!-- TR3: Tabela Individual -->
  <section id="individual" style="background:#f8f9fa;padding:24px 14px;border-radius:20px;">
    <h2>Tabela Hapvida [Cidade] Individual [ano_atual]</h2>
    <p>Subtítulo descritivo</p>
    <div style="orange-bar"></div>
    
    <!-- ~400 palavras de contexto -->
    <p>Por que individual é alternativa para quem não tem CNPJ</p>
    <p>Introdução da tabela: o que mostra</p>
    
    <!-- IMAGEM 2 -->
    <figure>
      <img style="max-width: 70%; ..." title="..." src="..." alt="..." width="1080" height="1080" />
      <figcaption>...</figcaption>
    </figure>
    
    <!-- ~200 palavras de leitura -->
    <p>Análise valores: 15-25% acima do empresarial, internações isentas, portabilidade RN 438</p>
    
    <!-- Bridge curta + link pillar -->
    <p>Para tipos de plano (Ambulatorial, Apartamento, NotreLife), comparativo com Amil/SulAmérica/Bradesco, histórico de reajustes → <a href="/plano-individual-hapvida/">guia completo do plano individual Hapvida</a></p>
  </section>

  <!-- TR4: Por Que [Cidade] Tem Esse Preço (CORE ÚNICO) -->
  <section id="posicionamento" style="padding:24px 14px;border-radius:20px;">
    <h2>Por Que [Cidade] Tem Esse Preço — e Não Outro</h2>
    <p>Subtítulo: posicionamento tarifário reflete contexto local</p>
    <div style="orange-bar"></div>
    
    <p>Contextualização Tabela 1 vs Tabela 2 (1 parágrafo)</p>
    <p>"Três fatores específicos da [cidade] explicam o posicionamento tarifário inferior nas tabelas apresentadas:"</p>
    
    <!-- 3 CARDS com 3 fatores ÚNICOS DA CIDADE -->
    <div class="grid3">
      <div>FATOR 1 — específico (ex: 45 anos sede, 2010 expansão pré-NDI)</div>
      <div>FATOR 2 — específico (ex: 1.3M beneficiários estado, market share)</div>
      <div>FATOR 3 — específico (ex: 80% rede própria, modelo verticalizado puro)</div>
    </div>
    
    <h3>Comparativo Tarifário: [Cidade] vs Outras Capitais</h3>
    <p>Introdução à tabela comparativa</p>
    
    <!-- Tabela HTML opcional com 4 cidades (Cidade-foco + 3 outras) -->
    <table>...</table>
    
    <p>Nota explicativa final: qualidade assistencial uniforme nacional</p>
  </section>

  <!-- TR5: Promoções na Cidade -->
  <section id="promocoes" style="background:#f8f9fa;padding:24px 14px;border-radius:20px;">
    <h2>Promoções Vigentes em [Cidade] — [mes_atual] de [ano_atual]</h2>
    <p>Subtítulo: tabelas já incorporam desconto</p>
    <div style="orange-bar"></div>
    
    <p>Contexto: tabelas exibidas já consideram desconto vigente</p>
    
    <!-- 2 cards: 15% padrão + Condição Regional -->
    <div class="grid2">
      <div>15% em 3 parcelas (padrão site)</div>
      <div>Condição regional específica da cidade (sede / migração concorrente / etc.)</div>
    </div>
    
    <!-- Lista de situações específicas de Fortaleza -->
    <ul>
      <li>Empresarial 30+ vidas (negociação direta)</li>
      <li>Migração de operadora que se retirou da região (caso Amil no NE)</li>
      <li>Reativação de contratos cancelados (diretoria regional)</li>
    </ul>
    
    <p>CTA para cotação personalizada</p>
  </section>

  <!-- FAQ -->
  <section id="faq" style="padding:24px 14px;border-radius:20px;">
    <h2>Como Interpretar as Tabelas Hapvida [Cidade] — Perguntas Frequentes</h2>
    <p>Subtítulo</p>
    <div style="orange-bar"></div>
    
    <!-- 6-8 FAQs em <details> — TODAS focadas em interpretar as tabelas -->
    <details><summary>Por que tabela de [cidade] é diferente da tabela de SP?</summary>...</details>
    <details><summary>Os valores das tabelas já incluem o desconto promocional?</summary>...</details>
    <details><summary>É o que vou pagar mensal ou tem coparticipação extra?</summary>...</details>
    <details><summary>Valores são por pessoa ou pela família inteira?</summary>...</details>
    <details><summary>Por que diferença entre Empresarial e Individual mesma idade?</summary>...</details>
    <details><summary>Quanto a tabela muda quando eu envelhecer?</summary>...</details>
    <details><summary>Vale para [cidade vizinha 1], [cidade vizinha 2], [cidade vizinha 3]?</summary>...</details>
    <details><summary>Posso travar o valor atual?</summary>...</details>
  </section>

  <!-- Formulário 2 -->
  <div>[elementor-template id="11215"]</div>

  <!-- Conclusão -->
  <section id="conclusao" style="background:gradient;padding:24px 14px;border-radius:20px;">
    <h2>As Tabelas Mais Acessíveis Entre as Cidades Hapvida [ou variação]</h2>
    <p>Subtítulo</p>
    <div style="orange-bar"></div>
    
    <!-- 4 cards-resumo -->
    <div class="grid4">
      <div>R$ X,XX — Empresarial 0-18</div>
      <div>R$ Y,YY — Individual 0-18</div>
      <div>10 — Faixas ANS</div>
      <div>15% — Desconto</div>
    </div>
    
    <p>Resumo posicionamento tarifário</p>
    <p>Decisão entre Empresarial e Individual</p>
    <p>Assinatura DRV + data</p>
  </section>

  <!-- JSON-LD ImageObject (2 schemas) -->
  <script type="application/ld+json">...</script>

  <!-- Style -->
  <style>...</style>

  <!-- Script -->
  <script>...</script>
</article>
```

---

## FAQ — Perguntas Modelo (Adaptar por Cidade)

8 perguntas-template. **Substituir placeholders e validar substitution test cidade a cidade.**

| # | Pergunta-Template | Substitution test deve... |
|---|---|---|
| 1 | Por que a tabela de [cidade] é muito mais barata que a tabela de São Paulo? | Falhar — resposta cita hospital específico local (ex: Hospital Antônio Prudente Fortaleza vs Hospital BP SP) |
| 2 | Os valores das tabelas já incluem o desconto promocional? | Passar — pergunta estrutural (1 das 2 permitidas) |
| 3 | O valor da tabela é o que vou pagar todo mês, ou tem coparticipação extra? | Falhar — resposta cita valores Tabela 1/Tabela 2 conforme a cidade |
| 4 | Os valores são por pessoa ou pela família inteira? | Passar — pergunta estrutural (2 das 2 permitidas) |
| 5 | Por que existe diferença entre Empresarial e Individual para a mesma idade? | Aceitável — resposta pode ter exemplo numérico específico da cidade |
| 6 | Quanto a tabela vai mudar quando eu envelhecer? | Aceitável — resposta com cálculo local (ex: "em Fortaleza, sai de R$ 87 e chega a R$ 513") |
| 7 | Esses valores valem para [bairros/cidades vizinhas]? | DEVE FALHAR — pergunta hiperlocal exclusiva (Caucaia/Maracanaú em Fortaleza; Olinda/Jaboatão em Recife; Iranduba em Manaus) |
| 8 | A tabela vai subir muito em [ano_atual]? Posso travar o valor atual? | Aceitável — resposta cita "em [cidade]" o que pode fazer |

**Pelo menos 4 das 8 FAQs devem falhar no substitution test.** Caso contrário, é doorway de cluster.

---

## Pre-Publication Checklist (GO/NO-GO)

Antes de entregar o artigo final, verificar todos os itens:

### Estrutura

- [ ] Apenas 5 seções numeradas (TR1-TR5) + FAQ + Conclusão
- [ ] TR4 (Por Que [Cidade]) presente e com 3 fatores ÚNICOS da cidade
- [ ] TR4 tabela comparativa cita 3 cidades específicas (não todas)
- [ ] TR5 tem pelo menos 1 gatilho regional específico (não só "15% padrão")
- [ ] Cortes confirmados: zero "Visão Geral por Modalidade", "Decisão entre Modalidades", "Faixa Etária Educacional", "Atualizações Detalhadas", "Bloco Adesão extenso"

### Imagens

- [ ] Exatamente 2 imagens (Empresarial + Individual, modalidade Coparticipação Total)
- [ ] Imagens produzidas em **1080×1080 pixels** (quadradas)
- [ ] Filename city-specific (`tabela-hapvida-[cidade]-[modalidade]-coparticipacao-total-2026.webp`)
- [ ] Estrutura `<figure>` exata conforme template: margin `0 0 24px 0`, padding `0`
- [ ] `<img>` segue a ordem prescrita de atributos: `style → title → src → alt → width → height`
- [ ] `<img>` style começa com `max-width: 70%; height: auto;`
- [ ] `<img>` style inclui `border-radius: 12px; border: 1px solid #e2e8f0; display: block; margin: 0 auto;`
- [ ] `<img>` `width="1080" height="1080"` explícito
- [ ] Title attribute: `Tabela Hapvida [Cidade] [modalidade] [ano] — Preços por Faixa Etária` (modalidade lowercase)
- [ ] Alt text: padrão "Tabela Hapvida [Cidade] [modalidade] [ano] — referência por faixa etária ANS... Valores entre X e Y"
- [ ] `<figcaption>` com pattern correto: "Tabela referência Plano Hapvida [modalidade] (coparticipação total) [Cidade] — valores por faixa etária ANS (Resolução Normativa nº 63/2003). Atualizada em [mes_atual] de [ano_atual]."
- [ ] `<figcaption>` style: `text-align: center; font-size: 14px; color: #718096; margin-top: 10px; font-style: italic`
- [ ] `loading="lazy"` adicionado apenas se o site não tem plugin de lazy loading
- [ ] H2 acima de cada imagem contém keyword exata da imagem
- [ ] ~400 palavras de contexto antes da imagem + ~200 palavras depois

### Anti-Doorway

- [ ] Substitution test trocando [cidade] por outra do mesmo grupo: deve falhar em TR1, TR4, TR5, e em pelo menos 4 das FAQs
- [ ] TR2 bloco empresarial tem MÁXIMO 6 parágrafos (incluindo o sobre coparticipação parcial)
- [ ] TR3 bloco individual tem MÁXIMO 5 parágrafos
- [ ] Zero menção a "70% dos beneficiários empresariais" (território pillar empresarial)
- [ ] Zero menção a "RN 432/2017" + "6 meses MEI" (território pillar empresarial)
- [ ] Zero menção a "Amil/Golden Cross/Bradesco encerraram individual entre 2017-2020" (território pillar individual)
- [ ] Zero tabela comparativa de concorrentes (Amil suspensa / Bradesco não oferece / etc.)
- [ ] Zero tabela "Valores de Coparticipação por Procedimento" (território pillar empresarial)
- [ ] Zero seção sobre faixas etárias ANS / RN 63/2003 / trava 6x (genérico)
- [ ] Zero seção sobre reajustes 11,5% / pool RN 565/2022 / sinistralidade (território pillar empresarial)
- [ ] Zero seção sobre Tipos de Plano (Ambulatorial/Enfermaria/NotreLife) (território pillar individual)

### Links

- [ ] 1 link exato à pillar `/tabela-de-preco-hapvida/`
- [ ] 1 link exato à pillar `/plano-empresarial-hapvida/` (no final da TR2)
- [ ] 1 link exato à pillar `/plano-individual-hapvida/` (no final da TR3)
- [ ] 1 link à pillar de cidade `/plano-hapvida-[cidade]/` (na TR1)
- [ ] 1-2 cross-links a outras cidades (na tabela comparativa de TR4)
- [ ] Nenhuma URL repetida no artigo
- [ ] Mínimo 150 palavras entre quaisquer 2 links internos

### Schema e Técnico

- [ ] JSON-LD `<script type="application/ld+json">` presente
- [ ] JSON-LD contém 2 ImageObject (um por imagem)
- [ ] JSON-LD posicionado ANTES do `<style>` final
- [ ] `[ano_atual]` usado em vez de ano fixo (mín. 4 ocorrências)
- [ ] `[mes_atual]` usado em vez de mês fixo (mín. 1 ocorrência)
- [ ] `[cidade_menorvalor]` usado para valor de chamariz (não R$ fixo)
- [ ] Style block penúltimo
- [ ] Script block último
- [ ] Tamanho final entre 35 KB e 50 KB

### Conteúdo Quality

- [ ] Mínimo 8 destaques `.destaque-laranja-suave` distribuídos
- [ ] Mínimo 6 FAQs (máximo 8)
- [ ] Mínimo 4 FAQs falham no substitution test
- [ ] Pelo menos 1 FAQ hiperlocal (sobre RM/bairros/cidades vizinhas)
- [ ] Conclusão tem grid4 com 4 cards-resumo
- [ ] Menção DRV: máximo 2 (TR1 + conclusão), 1 boxes "Dica DRV" opcional na TR5
- [ ] Sumário tem 5 itens + CTA "Faça uma Cotação" com `#cotacao-1`

### Pós-Publicação

- [ ] Registrar no Supabase via MCP `BD - criar` (`registrar_artigo_novo`, `registrar_faqs_artigo`, `registrar_links_artigo`)
- [ ] Sugerir links recíprocos: identificar onde o artigo de cidade `/plano-hapvida-[cidade]/` pode linkar para esta nova subpágina
- [ ] Sugerir link na pillar `/tabela-de-preco-hapvida/` apontando para a nova subpágina
- [ ] Verificar se as 2 imagens foram subidas na biblioteca WP com filenames exatos
- [ ] Verificar se as imagens estão acessíveis na URL especificada no schema

---

## Cluster Anti-Doorway — Quando Produzir 10 Cidades

Se for produzir múltiplas subpáginas em sequência (Fortaleza, Recife, Salvador, Manaus, etc.), o risco passa de "doorway de URL" para **"doorway de cluster"** — Google detecta padrões de template e penaliza o conjunto.

Regras adicionais para o cluster:

### TR4 (3 fatores) — Reescrever do zero por cidade

NÃO é "trocar Fortaleza por Recife nos mesmos parágrafos". Cada cidade precisa do próprio motivo estrutural:

| Cidade | Fator 1 (Maturidade) | Fator 2 (Escala) | Fator 3 (Modelo) |
|---|---|---|---|
| Fortaleza | 1979, sede nacional, 45 anos | 1,33M beneficiários CE | 80% rede própria, verticalizado puro |
| Recife | Expansão pré-2010, rede consolidada | Beneficiários PE específicos | Rede própria forte, Hapclínicas distribuídas |
| Salvador | Expansão Hapvida BA | Beneficiários BA | Rede mista, Hospital Teresa de Lisieux |
| Manaus | Expansão amazônica | Beneficiários AM, Iranduba | Hospital Nilton Lins, Hospital Rio Amazonas |
| Belém | Programa Barco-Saúde, ribeirinhos | Beneficiários PA | 2 hospitais, novo Layr Maia 2025 |
| Brasília | Mercado DF, perfil servidor público | Beneficiários DF | Hospital Brasiliense (trauma, ortopedia) |
| Goiânia | Expansão centro-oeste | Beneficiários GO | Hospital América |
| Natal | Mercado RN | Beneficiários RN | Rede própria potiguar |
| João Pessoa | Mercado PB | Beneficiários PB | Rede própria PB |
| Maceió | Mercado AL | Beneficiários AL | Rede própria AL |

### FAQ #7 (hiperlocal) — Trocar bairros/cidades vizinhas

| Cidade | Cidades RM para citar |
|---|---|
| Fortaleza | Caucaia, Maracanaú, Aquiraz, Eusébio |
| Recife | Olinda, Jaboatão dos Guararapes, Paulista, Camaragibe |
| Salvador | Lauro de Freitas, Camaçari, Simões Filho |
| Manaus | Iranduba, Careiro da Várzea |
| Belém | Ananindeua, Marituba, Benevides |
| Brasília | Águas Claras, Taguatinga, Ceilândia (regiões administrativas) |
| Goiânia | Aparecida de Goiânia, Anápolis (proximidade) |
| Natal | Parnamirim, Macaíba, São Gonçalo do Amarante |
| João Pessoa | Cabedelo, Bayeux, Santa Rita |
| Maceió | Rio Largo, Atalaia, Murici |

### TR5 (Promoções) — Gatilhos regionais por cidade

| Cidade | Gatilho regional possível |
|---|---|
| Fortaleza | "Sede nacional concentra políticas comerciais" + "migração Amil Nordeste" |
| Recife | "Migração Amil Nordeste" + "Polo médico do NE" |
| Salvador | "Migração Amil Nordeste" + "Polo de medicina diagnóstica" |
| Manaus | "Mercado regional Amazônia" + "rede pioneira" |
| Belém | "Programa Barco-Saúde exclusivo" + "novo Hospital Layr Maia" |
| Brasília | "Servidores públicos" + "concentração corporativa" |
| Goiânia | "Crescimento Centro-Oeste" + "Hospital América referência" |
| Natal/João Pessoa/Maceió | "Migração Amil Nordeste" + "rede em expansão" |

### Comparativo da TR4 — Ordem varia por cidade

A tabela "Comparativo Tarifário [Cidade] vs Outras Capitais" não deve ter as mesmas 4 cidades em todas as subpáginas. Varia conforme o foco:

| Cidade-foco | Comparar com (ordem) |
|---|---|
| Fortaleza | Recife, BH, SP |
| Recife | Fortaleza, BH, SP |
| Salvador | Recife, BH, SP |
| Manaus | Belém, BH, SP |
| Belém | Manaus, BH, SP |
| Brasília | Goiânia, BH, SP |
| Goiânia | Brasília, BH, SP |
| Natal | Fortaleza, Recife, SP |
| João Pessoa | Recife, Natal, SP |
| Maceió | Recife, Salvador, SP |

Sempre incluir SP como referência alta (para mostrar diferença +100%) e BH como referência intermediária. As outras 1-2 cidades variam.

---

## Mantra Específico TR

> "Se eu posso usar o mesmo artigo para Fortaleza e Recife trocando só nome de cidade, falhei."
> "Se o texto ao redor da imagem é mais sobre o produto que sobre a CIDADE específica, falhei."
> "Se a página existe sem a imagem fazer sentido, falhei. A página é wrapper da imagem, não o contrário."
