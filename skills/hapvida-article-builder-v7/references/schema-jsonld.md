# JSON-LD Schema — Hapvida (CONVERSÃO + INFORMATIVA + HOSPITAL)

Este arquivo rege o schema **obrigatório** de todos os artigos do tabelaplanos.com.br. Substitui a versão anterior (que só cobria Article+WebPage editorial) e incorpora a estrutura de **páginas de conversão** (WebPage + Service com preços), **BreadcrumbList separado**, **shortcodes de coparticipação** e os **Person fixos**.

> Artigos TR (tabela regional) têm schema próprio (`ImageObject`) em `tabela-regional-subpages.md` — não usar este.

---

## ⚠️ PASSO 0 — IDENTIFICAR O TIPO DE PÁGINA (SEMPRE PRIMEIRO)

O tipo de página decide qual conjunto de schema gerar. Declarar explicitamente antes de montar qualquer coisa.

### Por que a classificação mudou (base da decisão)

Plano de saúde é tema **YMYL** ("Your Money or Your Life" — saúde e dinheiro), onde o **E-E-A-T** (Experiência, Expertise, Autoridade, Confiança) é o principal fator de ranking. O nó **Article + Person (autor) + Organization (publisher)** é o que carrega esse sinal. Diretrizes do Google e prática atual confirmam:
- Article **não tem propriedade obrigatória** e **pode coexistir** com outros tipos na mesma página — o que importa é o schema bater com o conteúdo visível. Não existe regra do Google proibindo Article em página com função comercial.
- O **rich result de preço** (Offer/AggregateOffer) exige **oferta única** e preço que **não muda dinamicamente** por usuário. Nossos preços variam por faixa etária e vêm de shortcode dinâmico → o snippet de preço é frágil, geralmente não exibe, e ainda nos expõe à regra "schema tem que bater com o visível". Logo, **não vale sacrificar o Article/Person para perseguir snippet de preço**.

Conclusão: a maioria das nossas páginas de cidade é **editorial-comercial**, não conversão pura. O Article/Person é a espinha dorsal; o Service entra como entidade secundária, **sem** AggregateOffer de preço.

### TIPO A — Página de cidade EDITORIAL-COMERCIAL (PADRÃO para S1-S7)
Indicadores: autor visível (widget), corpo de guia (1000+ palavras), FAQ — **mesmo tendo** tabela de preço e formulário.
→ Gera: **WebPage + Article + Person + BreadcrumbList + FAQPage** (Bloco C). Opcionalmente um nó **Service** como entidade secundária, **sem** `offers`/`AggregateOffer` de preço (Bloco C-Service).

### TIPO B — Landing de CONVERSÃO PURA (raro)
Indicadores: página fina, **só** formulário/cotação, **sem** autor e **sem** corpo editorial de guia.
→ Gera: **WebPage + Service** (Bloco A) · **BreadcrumbList** · **FAQPage**. Aqui o Service é o foco porque não há Article a preservar.

### TIPO C — Página INFORMATIVA pura (blog/guia, sem preço)
Indicadores: artigo educacional, foco em informar, URL `/blog/` ou similar.
→ Gera: **WebPage + Article + Person + BreadcrumbList + FAQPage** (Bloco C).

### TIPO D — Página HOSPITAL (HS1-HS4 — editorial)
Artigo sobre uma unidade hospitalar → Article+WebPage editorial (Bloco D).

> **Regras:** O nó Article só é legítimo se houver conteúdo editorial real e visível na página. NUNCA usar AggregateOffer de preço com valores dinâmicos por faixa etária. NUNCA marcar dado que não esteja visível ao usuário.

---

## ⚠️ REGRA CRÍTICA — PREÇOS (NUNCA INVENTAR)

Antes de montar schema de **landing pura (Bloco A)** com preço, **PERGUNTAR ao usuário o menor e o maior valor** (ou confirmar o prefixo de cidade do shortcode). Jamais inventar, assumir ou estimar valores. Nas páginas editorial-comerciais (padrão), o schema não leva preço — então essa pergunta só vale para o Bloco A.

- **Preferir shortcode** ao valor fixo: `lowPrice` = `[cidade_emp_ambulatorialtotal_0]`, `highPrice` = `[cidade_emp_ambulatorialtotal_9]` (ver `shortcodes.md`). Valor numérico só se o usuário confirmar e não houver shortcode.
- Se usar número: extrair do HTML, converter `R$ 52,32` → `"52.32"` (ponto decimal, sem moeda). `lowPrice` < `highPrice`. `offerCount` = nº de faixas etárias.
- Se não houver shortcode nem valor confirmado → marcar `❓ NÃO ENCONTRADO` e **perguntar**. Não gerar sem confirmação.

---

## ⚠️ REGRA CRÍTICA — SHORTCODES (fonte da verdade: `shortcodes.md`)

**Fonte única da verdade dos shortcodes é `references/shortcodes.md`.** Usar os padrões EXATOS de lá — nunca inventar nome de shortcode. Nenhum valor de preço ou coparticipação entra como número fixo no schema.

**Preço (menor/maior valor):** usar os shortcodes registrados no plugin, no padrão da skill:
- `[cidade_menorvalor]` → menor valor / chamariz "a partir de R$ X" (`cidade` = prefixo real: `belem`, `fortaleza`, `belo-horizonte`, `sao-paulo`…).
- Valor pontual por faixa etária: `[cidade_emp_ambulatorialtotal_0]` (faixa 0-18) … `[cidade_emp_ambulatorialtotal_9]` (faixa 59+). Padrão completo: `[cidade_ind/emp_modalidade_acomodacaotipo_faixaetaria]`.
- **NÃO existe** `[cidade_maiorvalor]` — para o maior valor usar o pontual `_9`.
- Em landing pura (Bloco A): `lowPrice` = `[cidade_emp_ambulatorialtotal_0]`, `highPrice` = `[cidade_emp_ambulatorialtotal_9]`. Nas páginas editorial-comerciais (padrão), o C2-Service **não tem preço** — os shortcodes de preço ficam no corpo do artigo (seção S2), não no schema.

**Coparticipação — dois grupos, nunca misturar (idêntico ao `shortcodes.md`):**

Grupo 1 — São Paulo e Belo Horizonte (prefixo `sp_bh_`):
`[sp_bh_consultas_eletivas]` · `[sp_bh_consultas_urgencia]` · `[sp_bh_exames_simples]` · `[sp_bh_exames_complexos]` · `[sp_bh_terapias_neurologicas]` · `[sp_bh_demais_terapias]`

Grupo 2 — demais cidades (prefixo `demais_capitais_`):
`[demais_capitais_consultas_eletivas]` · `[demais_capitais_consultas_urgencia]` · `[demais_capitais_exames_simples]` · `[demais_capitais_exames_complexos]` · `[demais_capitais_terapias_neurologicas]` · `[demais_capitais_demais_terapias]`

**Datas no corpo** (não no schema): `[ano_atual]` e `[mes_atual]` conforme `shortcodes.md`. No schema, `datePublished`/`dateModified` são datas fixas reais (ver seção Datas) — ali NÃO usar `[ano_atual]`.

---

## ⚠️ MÉTODO DE IMPLEMENTAÇÃO — ARQUIVO SEPARADO (padrão V4.6.0)

**Mudança V4.6.0:** o schema NÃO é mais embutido no HTML do artigo. É gerado em **execução separada** (ver `SKILL.md` → "Geração de schema (execução separada)") e entregue como **arquivo próprio**.

**Formato único do arquivo:** um bloco `<script type="application/ld+json">…</script>` completo, **com `@context` e `@graph`**. Esse formato funciona nos dois pontos de colagem do Rank Math:

1. **Rank Math → editor do post → aba "Schema" → "Schema Generator" → "Import" → "JSON-LD/Custom Code" → Process Code.** O Rank Math lê o `@graph` completo e separa cada `@type` sozinho. É o método recomendado.
2. **Bloco "HTML Personalizado" (Custom HTML)** dentro do conteúdo do post: cola-se o `<script type="application/ld+json">…</script>` inteiro.

> ❌ **Não fazer mais (orientação revogada):** colar "cada nó separado sem `@context`/`@graph`". Os dois caminhos do Rank Math aceitam — e preferem — o bloco completo com `@graph`. Quebrar em nós soltos é trabalhoso e propenso a erro.
> ⚠️ Se o usuário usar o **Import → JSON-LD/Custom Code**, ele cola o bloco completo; o `@context`/`@graph` é obrigatório ali. Se usar o **Custom HTML block**, idem. Em nenhum dos dois casos remover o invólucro.

Os blocos-modelo abaixo já estão no formato correto (com `@graph`) — é exatamente o que vai no arquivo separado.

**Nome do arquivo entregue:** `schema-[slug-do-artigo].html` (ex.: `schema-hospital-renascenca-campinas-hapvida.html`). Conteúdo: apenas o bloco `<script type="application/ld+json">…</script>`, nada mais.

> **NÃO gerar** Organization nem WebSite: já existem globais no RankMath. Apenas referenciar por `@id`:
> Organization → `https://tabelaplanos.com.br/#organization` · WebSite → `https://tabelaplanos.com.br/#website`

---

## BLOCO A — LANDING DE CONVERSÃO PURA (TIPO B — raro)

⚠️ **Usar APENAS em landing fina, sem autor e sem corpo editorial.** Para páginas de cidade S1-S7 (que têm guia + autor), NÃO usar este bloco — usar o Bloco C + C-Service. Aqui o Service é o foco porque não há Article a preservar.

São **3 schemas**: WebPage+Service (1 bloco), BreadcrumbList (separado), FAQPage (separado).

### A1. WebPage + Service

```html
<script type="application/ld+json">{
  "@context":"https://schema.org",
  "@graph":[
    {
      "@type":"WebPage",
      "@id":"https://tabelaplanos.com.br/plano-hapvida-[cidade]/#webpage",
      "name":"[Título SEO da página]",
      "description":"[Meta description]",
      "url":"https://tabelaplanos.com.br/plano-hapvida-[cidade]/",
      "inLanguage":"pt-BR",
      "datePublished":"[AAAA-MM-DD da 1ª publicação]",
      "dateModified":"[AAAA-MM-DD da última revisão real]",
      "specialty":{"@type":"Specialty","name":"Health"},
      "isPartOf":{"@type":"WebSite","@id":"https://tabelaplanos.com.br/#website"},
      "primaryImageOfPage":{"@id":"https://tabelaplanos.com.br/plano-hapvida-[cidade]/#primaryimage"},
      "image":{
        "@type":"ImageObject",
        "@id":"https://tabelaplanos.com.br/plano-hapvida-[cidade]/#primaryimage",
        "url":"[URL da imagem principal — mín. 1200px de largura]",
        "width":1200,
        "height":630
      },
      "mainEntity":{
        "@type":"Service",
        "@id":"https://tabelaplanos.com.br/plano-hapvida-[cidade]/#service",
        "additionalType":"https://schema.org/HealthInsurancePlan",
        "name":"Plano de Saúde Hapvida [Cidade]",
        "description":"[Descrição do serviço — rede, cobertura regional, sem preço fixo]",
        "serviceType":"Health Insurance - Regional",
        "provider":{
          "@type":"Organization",
          "@id":"https://www.hapvida.com.br/#organization",
          "name":"Hapvida Assistência Médica",
          "identifier":{"@type":"PropertyValue","name":"Registro ANS","value":"359017"}
        },
        "broker":{"@type":"InsuranceAgency","@id":"https://tabelaplanos.com.br/#organization"},
        "areaServed":{
          "@type":"City",
          "name":"[Cidade]",
          "containedInPlace":{"@type":"State","name":"[Estado]"}
        },
        "availableChannel":{
          "@type":"ServiceChannel",
          "serviceUrl":"https://tabelaplanos.com.br/plano-hapvida-[cidade]/"
        },
        "hasOfferCatalog":{
          "@type":"OfferCatalog",
          "name":"Planos Hapvida [Cidade]",
          "itemListElement":[
            {
              "@type":"Offer",
              "itemOffered":{
                "@type":"Service",
                "name":"Hapvida Empresarial [Cidade] - Coparticipação Total",
                "description":"Plano com coparticipação em consultas eletivas ([demais_capitais_consultas_eletivas]), consultas de urgência ([demais_capitais_consultas_urgencia]), exames simples ([demais_capitais_exames_simples]), exames complexos ([demais_capitais_exames_complexos]), terapias neurológicas ([demais_capitais_terapias_neurologicas]) e demais terapias ([demais_capitais_demais_terapias])."
              },
              "priceCurrency":"BRL",
              "price":"[cidade_menorvalor]",
              "priceValidUntil":"2026-12-31",
              "availability":"https://schema.org/InStock",
              "eligibleRegion":{"@type":"City","name":"[Cidade]"}
            }
          ]
        },
        "offers":{
          "@type":"AggregateOffer",
          "priceCurrency":"BRL",
          "lowPrice":"[cidade_emp_ambulatorialtotal_0]",
          "highPrice":"[cidade_emp_ambulatorialtotal_9]",
          "offerCount":"10",
          "priceValidUntil":"2026-12-31",
          "availability":"https://schema.org/InStock",
          "description":"Valores variam conforme idade, acomodação e modelo de coparticipação.",
          "eligibleRegion":{"@type":"City","name":"[Cidade]"}
        }
      }
    }
  ]
}</script>
```

**Regras do bloco A1:**
- `provider` = SEMPRE Hapvida (operadora, ANS 359017 fixo). `broker` = SEMPRE DRV/Tabela Planos (corretora). Nunca inverter.
- `additionalType: HealthInsurancePlan` é obrigatório no Service.
- `areaServed`: cidade → `City` com `containedInPlace` State; página de estado → `State` com `containedInPlace` Country.
- Imagem vive no WebPage (`primaryImageOfPage` + `image`), nunca no Service — plano de saúde não tem "foto de produto".
- Preços usam shortcode (`[cidade_menorvalor]`, `[cidade_emp_ambulatorialtotal_0/_9]`) — ver `shortcodes.md`. Valor numérico só se confirmado pelo usuário. Nunca inventar nem usar `[cidade_maiorvalor]` (não existe).

### A2. BreadcrumbList (SEPARADO — padrão fixo 3 posições)

```html
<script type="application/ld+json">{
  "@context":"https://schema.org",
  "@type":"BreadcrumbList",
  "@id":"https://tabelaplanos.com.br/plano-hapvida-[cidade]/#breadcrumb",
  "itemListElement":[
    {"@type":"ListItem","position":1,"name":"Home","item":"https://tabelaplanos.com.br/"},
    {"@type":"ListItem","position":2,"name":"Hapvida Cidades","item":"https://tabelaplanos.com.br/hapvida-cidades/"},
    {"@type":"ListItem","position":3,"name":"Hapvida [Cidade]","item":"https://tabelaplanos.com.br/plano-hapvida-[cidade]/"}
  ]
}</script>
```

Position 1 sempre "Home"; position 2 sempre "Hapvida Cidades"; position 3 "Hapvida [Cidade]". Todas as URLs terminam com `/`. Nunca pular positions.

### A3. FAQPage (SEPARADO)

```html
<script type="application/ld+json">{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "@id":"https://tabelaplanos.com.br/plano-hapvida-[cidade]/#faq",
  "mainEntity":[
    {"@type":"Question","name":"[Pergunta 1 — idêntica ao FAQ visível]","acceptedAnswer":{"@type":"Answer","text":"[Resposta sem R$ fixo]"}},
    {"@type":"Question","name":"[Pergunta 2]","acceptedAnswer":{"@type":"Answer","text":"[Resposta 2]"}}
  ]
}</script>
```

Mínimo 3 perguntas (se houver menos, não gerar). Uma entrada por pergunta do FAQ visível (12-15). `name` idêntico ao texto visível. `Answer.text` sem valor de preço fixo — descrever de forma evergreen. Extrair das `<details>`/`<summary>` visíveis, nunca de schema RankMath pré-existente (costumam divergir).

---

## BLOCO B — CONVERSÃO, MÚLTIPLAS CIDADES

URL genérica que cobre várias cidades. NÃO criar um Service que agrega tudo, e NÃO usar ItemList (gera carrossel indesejado). Usar WebPage com `mentions` apontando para cada página de cidade.

```html
<script type="application/ld+json">{
  "@context":"https://schema.org",
  "@graph":[
    {
      "@type":"WebPage",
      "@id":"[URL]#webpage",
      "name":"[Título]",
      "description":"[Meta]",
      "url":"[URL]",
      "inLanguage":"pt-BR",
      "datePublished":"[AAAA-MM-DD]",
      "dateModified":"[AAAA-MM-DD]",
      "isPartOf":{"@type":"WebSite","@id":"https://tabelaplanos.com.br/#website"},
      "mentions":[
        {"@type":"WebPage","@id":"https://tabelaplanos.com.br/plano-hapvida-fortaleza/#webpage"},
        {"@type":"WebPage","@id":"https://tabelaplanos.com.br/plano-hapvida-recife/#webpage"}
      ]
    }
  ]
}</script>
```

Acompanha BreadcrumbList e FAQPage separados (mesmos moldes de A2/A3).

---

## BLOCO C — EDITORIAL (TIPO A cidade S1-S7 + TIPO C informativa)

Este é o **PADRÃO** para páginas de cidade S1-S7 (editorial-comercial) e para artigos informativos puros. São **5 schemas**: WebPage, Article (separado), Person (separado), BreadcrumbList (separado), FAQPage (separado).

Para páginas de cidade S1-S7 que tenham tabela de preço/formulário, adicionar também o nó **C-Service** (entidade comercial secundária, **sem** preço de oferta) — ver abaixo.

### C1. WebPage

```html
<script type="application/ld+json">{
  "@context":"https://schema.org",
  "@graph":[
    {
      "@type":"WebPage",
      "@id":"[URL]#webpage",
      "name":"[Título do artigo]",
      "description":"[Meta description]",
      "url":"[URL]",
      "inLanguage":"pt-BR",
      "datePublished":"[AAAA-MM-DD]",
      "dateModified":"[AAAA-MM-DD]",
      "specialty":{"@type":"Specialty","name":"Health"},
      "isPartOf":{"@type":"WebSite","@id":"https://tabelaplanos.com.br/#website"},
      "mainEntity":{"@id":"[URL]#article"}
    }
  ]
}</script>
```

### C2. Article (SEPARADO)

```html
<script type="application/ld+json">{
  "@context":"https://schema.org",
  "@type":"Article",
  "@id":"[URL]#article",
  "headline":"[H1 — máx. 110 caracteres]",
  "description":"[Meta description]",
  "image":{"@type":"ImageObject","url":"[URL imagem]","width":1200,"height":630},
  "author":{"@id":"https://tabelaplanos.com.br/#jessica-mendes"},
  "publisher":{"@id":"https://tabelaplanos.com.br/#organization"},
  "datePublished":"[AAAA-MM-DD]",
  "dateModified":"[AAAA-MM-DD]",
  "mainEntityOfPage":{"@type":"WebPage","@id":"[URL]"},
  "articleSection":"[Categoria]",
  "wordCount":[número calculado],
  "inLanguage":"pt-BR"
}</script>
```

- `author.@id` → `#jessica-mendes` ou `#victor-castro`. Se o autor não estiver no HTML, marcar `❓` e **perguntar** — nunca assumir.
- `mainEntityOfPage.@id` = a URL pura (não `#webpage`).
- `wordCount` calculado do corpo (sem nav/sidebar/footer).

### C2-Service. Service secundário (SÓ para cidade S1-S7 com preço/formulário)

Adicionar este nó **apenas** em páginas de cidade que tenham tabela de preço/formulário. Ele descreve a intenção comercial como **entidade** (ajuda o Google a entender que a página é sobre o plano Hapvida na cidade), **sem** `offers`/`AggregateOffer` de preço — porque preço dinâmico por faixa etária não é elegível a rich result de preço e ainda violaria a regra de "schema = conteúdo visível". O Article/Person continua sendo a espinha dorsal (E-E-A-T).

No C1 (WebPage), além de `mainEntity` apontar para o Article, adicionar `about` referenciando este Service:
```json
"about":{"@id":"[URL]#service"}
```

```html
<script type="application/ld+json">{
  "@context":"https://schema.org",
  "@type":"Service",
  "@id":"[URL]#service",
  "additionalType":"https://schema.org/HealthInsurancePlan",
  "name":"Plano de Saúde Hapvida [Cidade]",
  "description":"[Descrição da rede e cobertura regional — sem preço fixo]",
  "serviceType":"Health Insurance - Regional",
  "provider":{
    "@type":"Organization",
    "@id":"https://www.hapvida.com.br/#organization",
    "name":"Hapvida Assistência Médica",
    "identifier":{"@type":"PropertyValue","name":"Registro ANS","value":"359017"}
  },
  "broker":{"@type":"InsuranceAgency","@id":"https://tabelaplanos.com.br/#organization"},
  "areaServed":{"@type":"City","name":"[Cidade]","containedInPlace":{"@type":"State","name":"[Estado]"}}
}</script>
```

**Regras do C2-Service:**
- **NÃO** incluir `offers`, `AggregateOffer`, `hasOfferCatalog` com preço, nem `price`. Sem preço de oferta neste nó.
- `provider` = Hapvida (ANS 359017) · `broker` = DRV/Tabela Planos. Nunca inverter.
- Se quiser mencionar coparticipação em alguma descrição, usar shortcode do grupo correto (ver regra de shortcodes) — nunca número fixo.

### C3. BreadcrumbList (informativa — 3-4 níveis)

```html
<script type="application/ld+json">{
  "@context":"https://schema.org",
  "@type":"BreadcrumbList",
  "@id":"[URL]#breadcrumb",
  "itemListElement":[
    {"@type":"ListItem","position":1,"name":"Home","item":"https://tabelaplanos.com.br/"},
    {"@type":"ListItem","position":2,"name":"Blog","item":"https://tabelaplanos.com.br/blog/"},
    {"@type":"ListItem","position":3,"name":"[Categoria]","item":"https://tabelaplanos.com.br/blog/[categoria]/"},
    {"@type":"ListItem","position":4,"name":"[Título curto]","item":"[URL]"}
  ]
}</script>
```

### C4. FAQPage — igual ao A3 (se houver ≥ 3 FAQs).

### C5. Person (FIXOS — copiar EXATAMENTE, não modificar)

**Jessica Mendes:**
```html
<script type="application/ld+json">{
  "@context":"https://schema.org",
  "@type":"Person",
  "@id":"https://tabelaplanos.com.br/#jessica-mendes",
  "name":"Jessica Mendes",
  "alternateName":"Jéssica Mendes",
  "jobTitle":"Consultora Especialista em Planos de Saúde",
  "description":"Consultora especializada em planos de saúde desde 2020, com foco em soluções Hapvida para pessoas físicas e famílias. Possui 10 premiações como Consultora Estrela pela operadora Hapvida e uma carteira ativa de mais de 7.000 clientes atendidos.",
  "url":"https://tabelaplanos.com.br/sobre_nos/jessica_mendes/",
  "image":{"@type":"ImageObject","url":"https://tabelaplanos.com.br/imagens/jessica-mendes.jpg","width":400,"height":400},
  "sameAs":["https://www.instagram.com/consultorajessicamendes/"],
  "worksFor":{"@id":"https://tabelaplanos.com.br/#organization"},
  "knowsAbout":["Planos de Saúde Hapvida","Consultoria em Seguros de Saúde","Planos Individuais e Familiares","Portabilidade de Planos de Saúde"],
  "award":["Consultora Estrela Hapvida (10x)"],
  "hasOccupation":{"@type":"Occupation","name":"Consultora de Seguros de Saúde","experienceRequirements":"5 anos de experiência"}
}</script>
```

**Victor Castro:**
```html
<script type="application/ld+json">{
  "@context":"https://schema.org",
  "@type":"Person",
  "@id":"https://tabelaplanos.com.br/#victor-castro",
  "name":"Victor Castro",
  "jobTitle":"Consultor Especialista em Planos de Saúde",
  "description":"Consultor especialista em planos de saúde desde 2017, com mais de 10 premiações e reconhecimento na categoria 5 estrelas, o mais alto nível de excelência no mercado de planos de saúde.",
  "url":"https://tabelaplanos.com.br/sobre_nos/victor_castro/",
  "image":{"@type":"ImageObject","url":"https://tabelaplanos.com.br/imagens/victor-castro.jpg","width":400,"height":400},
  "sameAs":["https://www.instagram.com/planosdesaude.victorcastro"],
  "worksFor":{"@id":"https://tabelaplanos.com.br/#organization"},
  "knowsAbout":["Planos de Saúde Hapvida","Consultoria em Seguros de Saúde","Planos Individuais","Hapvida NotreDame Intermédica"],
  "award":["Consultor 5 Estrelas Hapvida","Mais de 10 Premiações por Desempenho e Profissionalismo"],
  "hasOccupation":{"@type":"Occupation","name":"Consultor de Seguros de Saúde","experienceRequirements":"8 anos de experiência"},
  "telephone":"+5585981848298",
  "contactPoint":{"@type":"ContactPoint","telephone":"+5585981848298","contactType":"customer service","availableLanguage":"Portuguese"}
}</script>
```

> Se o widget de autor do tema já emite um `Person` próprio, NÃO incluir este nó — apenas referenciar `"author":{"@id":"…#person"}` apontando para o `@id` do widget, para evitar duplicação.

---

## BLOCO D — HOSPITAL (HS1-HS4, editorial)

Mesma lógica editorial do bloco C, com a entidade-hospital em `about` e `sameAs` para CNES/DataSUS. Mantém Article+WebPage, Person (ou ref `@id`), FAQPage.

```html
<script type="application/ld+json">{
  "@context":"https://schema.org",
  "@graph":[
    {
      "@type":["Article","WebPage"],
      "@id":"https://tabelaplanos.com.br/[hospital]-hapvida/#article",
      "headline":"[H1 — máx. 110 caracteres]",
      "description":"[meta description]",
      "inLanguage":"pt-BR",
      "datePublished":"[AAAA-MM-DD]",
      "dateModified":"[AAAA-MM-DD]",
      "author":{"@id":"https://tabelaplanos.com.br/#victor-castro"},
      "publisher":{"@id":"https://tabelaplanos.com.br/#organization"},
      "about":[
        {"@type":"Hospital","name":"[Nome oficial]","sameAs":"[URL CNES/DataSUS ou página oficial Hapvida]"},
        {"@type":"Thing","name":"Hapvida","sameAs":"https://www.hapvida.com.br/"}
      ]
    },
    {
      "@type":"FAQPage",
      "@id":"https://tabelaplanos.com.br/[hospital]-hapvida/#faq",
      "mainEntity":[
        {"@type":"Question","name":"[Pergunta 1]","acceptedAnswer":{"@type":"Answer","text":"[Resposta]"}}
      ]
    }
  ]
}</script>
```

O nó `Hospital` fica mínimo e verdadeiro (`name` + `sameAs`) — não transformar em `MedicalBusiness` com horários/avaliações não confirmados. FAQ do hospital: 6-8 perguntas.

---

## TABELA DE ENTIDADES CANÔNICAS (sameAs)

| Entidade | sameAs canônico |
|----------|-----------------|
| Hapvida | `https://www.hapvida.com.br/` |
| ANS | `https://www.gov.br/ans/` |
| Hospital (próprio) | URL da unidade no site Hapvida ou ficha CNES (`cnes.datasus.gov.br`) |
| Cidade | URL da Wikipedia pt da cidade (omitir se não houver — não inventar) |
| DRV Corretora | `https://tabelaplanos.com.br/#organization` (sempre por `@id`) |

---

## DATAS

`datePublished`/`dateModified` são timestamps factuais — exceção à regra evergreen, NÃO usam `[ano_atual]`. `datePublished` é fixo (1ª publicação). `dateModified` atualiza a cada revisão real do conteúdo — é o sinal de recência que a IA lê (trocar o ano no título não conta).

---

## ⚠️ ANTI-DUPLICAÇÃO (LER ANTES DE PUBLICAR)

Este JSON-LD é a **fonte única da verdade** para os `@type` que declara. Nunca ter o mesmo `@type` saindo de dois lugares (ex.: dois `FAQPage` na mesma página).

- Como o schema é colado via Rank Math (Import ou Custom HTML), **desligar** os campos nativos de schema do Rank Math para os mesmos `@type` nesse post, para não duplicar.
- Se o widget de autor já emite `Person`, não duplicar o nó — referenciar por `@id`.
- Nunca gerar Organization/WebSite (globais no RankMath) — só referenciar.
- Validar no [Rich Results Test](https://search.google.com/test/rich-results): exatamente **um** de cada `@type`.

---

## CHECKLIST FINAL

**Identificação**
- [ ] Tipo declarado: A (cidade editorial-comercial) / B (landing pura) / C (informativa) / D (hospital), com razões
- [ ] Conjunto de schemas correto selecionado

**Cidade S1-S7 (TIPO A — padrão) e Informativa (TIPO C)**
- [ ] WebPage + Article + Person + BreadcrumbList + FAQPage (espinha dorsal E-E-A-T preservada)
- [ ] Autor confirmado (Jessica ou Victor) — Person fixo copiado exato
- [ ] `mainEntityOfPage.@id` = URL pura · `wordCount` calculado
- [ ] Se a cidade tem preço/formulário: adicionou C2-Service **sem** `offers`/`price`; WebPage com `about` → `#service`
- [ ] NÃO usou AggregateOffer/preço de oferta numa página editorial

**Landing de conversão pura (TIPO B — só se sem autor e sem guia)**
- [ ] Menor e maior valor CONFIRMADOS pelo usuário (nunca inventados)
- [ ] WebPage + Service em um bloco; BreadcrumbList e FAQPage separados
- [ ] `provider` = Hapvida (ANS 359017) · `broker` = Tabela Planos · não invertidos
- [ ] `additionalType: HealthInsurancePlan` presente · `lowPrice` < `highPrice`
- [ ] Imagem no WebPage (`primaryImageOfPage` + `image`, ≥ 1200px), não no Service

**Geral**
- [ ] Article só existe se há conteúdo editorial real e visível na página
- [ ] Shortcodes de coparticipação do grupo certo (SP/BH vs. demais), sem misturar; nenhum valor fixo
- [ ] BreadcrumbList: positions sequenciais, URLs com `/` no fim
- [ ] FAQPage só se ≥ 3 perguntas; texto idêntico ao visível; sem R$ fixo nas respostas
- [ ] `dateModified` = última revisão real
- [ ] Invólucro correto p/ método: script embutido = com `@context`/`@graph`; RankMath = sem
- [ ] Não gerou Organization/WebSite; sem `@type` duplicado
- [ ] Validado no Rich Results Test: 1 de cada tipo
