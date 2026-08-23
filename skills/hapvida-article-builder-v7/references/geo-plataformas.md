# GEO POR PLATAFORMA — cada IA escolhe fonte de um jeito [V6]

> **Por que esta referência existe.** A `geo-aeo.md` (camada v2) trata "IA" como uma coisa só: passagem citável, schema, freshness. Está certo, mas é o denominador comum. Na prática **AI Overviews, ChatGPT, Perplexity, Copilot e Claude usam índices diferentes e pesam sinais diferentes** — dá para estar ótimo num e invisível no outro. Esta referência diz o que muda em cada um.
>
> **Como tratar os números daqui.** Vieram de estudos de terceiros de 2025-2026 (Amsive/Lily Ray, SE Ranking, ZipTie, Scrunch, SimilarWeb, Princeton/KDD 2024). São **direcionais**, não lei — a mesma ressalva que já vale na `geo-aeo.md`. Use a estrutura, não decore a porcentagem. E nenhum deles foi medido em português nem em plano de saúde.

---

## O piso comum (vale para todas)

1. **Estar no índice que aquela IA usa.** Cada uma puxa de um buscador diferente. Fora do índice, não existe citação.
2. **Ser rastreável.** Robô bloqueado no `robots.txt` = citação perdida. Ver a seção de robôs no fim.
3. **Ser extraível.** Todas puxam **passagem**, não página. Parágrafo autocontido ganha; parágrafo que depende do anterior, não.

Isso a v2 já cobria. O que vem abaixo é o que **não** é comum.

---

## Google AI Overviews

**Índice:** o do próprio Google. **Aparece em algo perto de metade das buscas.**

**O que mais muda aqui:** o Google já tem os seus sinais clássicos (links, autoridade, relevância). A camada de IA acrescenta preferência por **conteúdo com fonte citada** e por **dado estruturado**. E o detalhe que mais importa para vocês: **as fontes da AI Overview coincidem pouco com o top 10 orgânico** (estimativas na casa de 15%). Ou seja — **uma página que não chega à primeira página pode ser citada assim mesmo**, se o schema for bom e a resposta for extraível.

**O que fazer:**
- **Schema é a maior alavanca aqui.** Article, FAQPage, o `@graph` ligando Organization ↔ Person(autor) ↔ Article. Isso vocês já geram — ver `references/schema-jsonld.md`.
- Autoridade temática por **cluster com linkagem interna forte** (o modelo hub-spoke da v1 serve exatamente a isso).
- **Citação nomeada dentro do texto**: "segundo a Resolução Normativa 465/2021 da ANS" vale mais que "segundo a ANS".
- Bio de autor com credencial real (E-E-A-T pesa muito num tema YMYL).
- Os padrões de consulta que mais disparam AI Overview são **"o que é"** e **"como"** — que na prática de vocês viram FAQ e H3.

---

## ChatGPT

**Índice:** baseado no Bing. Combina busca com o que já sabe e cita as fontes que usou.

**O que mais muda aqui:**
- **Frescor pesa muito.** Conteúdo atualizado nos últimos ~30 dias é citado com folga mais frequência do que conteúdo velho. Isso conversa direto com a **Regra de Ouro nº 5c (recência real, não cosmética)**: mexer no `dateModified` sem mexer no conteúdo não engana e não adianta.
- **O sinal mais forte é o encaixe formato-resposta**: quanto mais o seu texto se parece com o jeito que o ChatGPT responderia àquela pergunta, mais ele cita. Mais forte que autoridade de domínio. Na prática: **resposta direta primeiro, organizada, conversacional, sem rodeio.**
- **Autoridade de domínio pesa mais aqui do que nas outras.**
- Fora do seu site, ele puxa muito de **Wikipédia** e **Reddit**.

**O que fazer:** manter as páginas competitivas revisadas de verdade; escrever a passagem de abertura no formato de uma resposta; estatística sempre com fonte nomeada; hierarquia limpa de H1 > H2 > H3.

---

## Perplexity

**Índice:** o próprio + Google, com várias passadas de reordenação.

**O que mais muda aqui:**
- **FAQPage em JSON-LD** tem efeito visível — e é o argumento que faltava para continuar gerando FAQ schema mesmo depois de o Google ter parado de exibir o rich result de FAQ para sites comuns (a ressalva que já está na v5). **O schema continua valendo; só mudou quem consome.**
- **PDF público é priorizado.** Vocês têm tabela de preço em PDF na origem — vale considerar publicar uma versão pública.
- **Velocidade de publicação** conta mais que mira em keyword.
- **Parágrafo autocontido** é a moeda: ele extrai o parágrafo inteiro.
- Usa decaimento por tempo, o que dá chance real a publicador novo.

**O que fazer:** liberar `PerplexityBot`; manter FAQPage em toda página com pergunta e resposta; `Article` com `datePublished` e `dateModified`; escrever parágrafo que funcione sozinho.

---

## Microsoft Copilot

**Índice:** inteiramente o do Bing. **Se o Bing não indexou, o Copilot não cita.**

**O que mais muda aqui:** velocidade de página pesa mais (limiar prático perto de 2 segundos), e o ecossistema Microsoft dá impulso — presença no **LinkedIn** ajuda aqui e não ajuda nas outras.

**O que fazer:** cadastrar o site no **Bing Webmaster Tools** (quase todo mundo só cadastra no Google Search Console); usar **IndexNow** ao publicar e ao revisar — isso já está na Fase 5 da v5, e aqui ganha um segundo motivo; cuidar do tempo de carregamento; definição de termo explícita e extraível ("Coparticipação é…").

---

## Claude

**Índice:** **Brave Search** — nem Google nem Bing. Se você não aparece no Brave, o Claude não te acha.

**O que mais muda aqui:** ele é **muito seletivo**. Cita pouco, e o que cita tende a ser o material mais preciso e melhor fundamentado do assunto. **Densidade factual** — número específico, fonte nomeada, data — rende muito mais aqui do que texto bem escrito e vago.

**O que fazer:** conferir se o site aparece em `search.brave.com`; liberar `ClaudeBot` e `anthropic-ai`; e — a parte fácil para vocês — **encher o artigo de dado do banco**: "7 hospitais e 12 clínicas", "R$ 107,83 na tabela de julho", "RN 465/2021". É exatamente o que a camada de **DEFENSIBILIDADE DO DADO [V6]** manda fazer.

---

## Resumo de bolso

| Plataforma | Índice | A alavanca nº 1 | O erro que mata |
|---|---|---|---|
| AI Overviews | Google | schema + citação nomeada | achar que só o top 10 é citado |
| ChatGPT | Bing | frescor real + formato de resposta | atualizar a data sem atualizar o texto |
| Perplexity | próprio + Google | FAQPage + parágrafo autocontido | parágrafo que depende do anterior |
| Copilot | Bing | estar no Bing + IndexNow + velocidade | só cadastrar no Google |
| Claude | Brave | densidade factual (número + fonte + data) | texto bonito e vago |

---

## Robôs a liberar no `robots.txt`

Verificação de site (uma vez, não por artigo — registrar como pendência se faltar):

```
User-agent: GPTBot            # OpenAI — alimenta a busca do ChatGPT
User-agent: ChatGPT-User      # ChatGPT navegando
User-agent: PerplexityBot     # Perplexity
User-agent: ClaudeBot         # Claude
User-agent: anthropic-ai      # Claude (alternativo)
User-agent: Google-Extended   # Gemini e AI Overviews
User-agent: Bingbot           # Copilot, via Bing
Allow: /
```

`CCBot` (Common Crawl) pode ser bloqueado sem perder citação — ele serve a treino, não a busca.

---

## A escada: citado ≠ recomendado

Esta é a parte desconfortável, e é a mais importante para uma corretora.

| Degrau | O que significa | O que decide |
|---|---|---|
| 1. **Lido** | a IA leu para montar a resposta, sem citar | rastreabilidade, estrutura |
| 2. **Citado** | seu link aparece como fonte | utilidade do conteúdo: estrutura, dado, clareza, frescor |
| 3. **Mencionado** | a marca é nomeada no texto da resposta | como a web fala de vocês |
| 4. **Recomendado** | a IA coloca vocês na lista de quem considerar | **consenso da web inteira** — avaliação, fórum, imprensa, vídeo. Quase independente do seu site |

Os degraus 1-3 são o que o artigo conquista. **O degrau 4 é decidido majoritariamente fora do site** — e é o degrau que vende. Nenhum artigo, por melhor que seja, resolve isso sozinho. Dizer o contrário seria mentira.

Existe ainda um degrau-sombra: **recomendado contra**. Em pergunta detalhada, os modelos já apontam o que **evitar**, com fonte. Reputação fraca em fonte terceira deixou de ser só ausência — pode virar contraindicação explícita.

### A armadilha do listicle auto-promocional (leia antes de pautar "melhores planos")

Um estudo de 2026 (Amsive) mediu 100 buscas do tipo "melhor software de [categoria]": os artigos auto-promocionais foram citados 323 vezes nas AI Overviews e, **em 69% dessas citações, a resposta recomendou os concorrentes e deixou de fora quem publicou o artigo**.

O mecanismo: o modelo trata o seu guia como **fonte sobre a categoria**. Ele extrai os nomes dos concorrentes que você compilou — e monta a recomendação pelo consenso da web, onde manda quem é maior.

**Traduzindo para vocês:** a DRV é corretora **Hapvida**. Um artigo tipo *"os melhores planos de saúde de [cidade]"* com a Hapvida em primeiro é auto-promocional por definição — e há risco real de o modelo extrair dali "Unimed, Amil, SulAmérica" e recomendar **esses**. Vocês fariam a pesquisa que ajuda o modelo a descrever a concorrência.

**O que fazer em vez disso:**
- Ser a fonte **do dado**, não do ranking. "Quanto custa o plano Hapvida em [cidade]" com a tabela real é território de vocês e ninguém disputa. Comparação entre operadoras não é.
- Quando a comparação for inevitável (e às vezes é, porque o leitor busca isso), **comparar com honestidade e escopo declarado** — "comparativo de carências entre operadoras segundo a ANS" — em vez de premiar a si mesmo. Isso ainda alimenta a IA, mas sem entregar a recomendação de bandeja.
- **A pergunta-teste, antes de pautar qualquer comparativo:** *se a IA ignorasse tudo do nosso domínio, o resto da web ainda colocaria a DRV na lista?* Se a resposta for não, o comparativo não é a prioridade — a reputação em fonte terceira é.

### O que move o degrau 4 (fora do artigo — registrar como pendência, não fingir que o artigo resolve)

Reclame Aqui e avaliações do Google Business Profile · discussão espontânea em fórum e grupo · imprensa local e regional · vídeo e podcast (transcrição é bastante recuperada) · perfis atualizados em diretório de corretora.

**A honestidade que a v6 exige:** ao entregar um artigo, **não prometer "vai ser recomendado pela IA"**. O artigo trabalha os degraus 1-3. O degrau 4 é outro projeto — e é justo dizer isso ao usuário.

---

## Query fan-out — o que muda na FASE 0

A busca com IA do Google **não responde só a pergunta digitada**: ela gera perguntas relacionadas por baixo e sintetiza tudo. Exemplo do próprio Google: "como cuidar do gramado" dispara consultas sobre herbicida, remoção sem química, prevenção de erva daninha.

**Consequência prática:** mirar uma página por keyword rende menos. **Ganha a página que cobre o tema-pai com as sub-perguntas dentro.**

**O que passa a ser obrigatório na FASE 0 (DR1):** listar de **5 a 10 sub-perguntas** que a IA provavelmente vai gerar a partir da keyword-alvo, e marcar cada uma como:
- **coberta neste artigo** (vira H3 ou FAQ), ou
- **coberta por outro artigo do cluster** (vira link interno), ou
- **descoberta** → vira **pendência de pauta** no banco.

Exemplo, para "plano hapvida piracicaba":
1. quanto custa o plano hapvida em piracicaba
2. quais hospitais a hapvida atende em piracicaba
3. qual a carência do plano hapvida
4. hapvida piracicaba é bom? (reputação — cuidado YMYL)
5. hapvida tem plano individual em piracicaba
6. como funciona a coparticipação
7. hapvida cobre parto em piracicaba
8. plano hapvida empresarial piracicaba (2 vidas)
9. qual a diferença entre Nosso Plano e Nosso Médico
10. como cancelar / trocar de plano

Note que várias já são artigos do cluster — **é exatamente esse o ponto**: o fan-out é o mapa de link interno que o Google já está montando sozinho.

**Trava:** cobrir sub-pergunta **não** autoriza inflar o artigo com conteúdo nacional genérico. Vale a regra da v4: *profundidade ≠ conteúdo nacional*. Sub-pergunta que não tem resposta local vira link, não seção.

---

## O que NÃO fazer (expectativas honestas)

- **Não medir sucesso por rich result de FAQ.** Desde 2023 o Google só exibe para site de alta autoridade em saúde/governo. O schema continua valendo — para Perplexity e para extração —, mas o visual não vem.
- **Não tratar `llms.txt` como alavanca comprovada.** O próprio Google diz que não é necessário para AI Overviews. Se fizer, faça como aposta barata de protocolo, não como tática de ranqueamento — a mesma ressalva já registrada na `geo-aeo.md`.
- **Não inventar métrica de citação.** Só reportar com dado real (`monitor_citacoes_ia` / `buraco_citacao_ia` do DataForSeo). Sem dado, dizer que não foi medido.
- **Não confundir citação com tráfego.** Boa parte do efeito de uma recomendação chega como **busca por marca** e tráfego direto, não como referência visível de IA — a atribuição padrão subnotifica. Vigiar volume de busca por marca no GSC é um proxy melhor do que caçar referral de IA.

Ver também: `references/geo-aeo.md` (a base v2), `references/voz-humana.md` (tom autoritativo e densidade factual são o que faz citar) e **DEFENSIBILIDADE DO DADO [V6]** no `SKILL.md`.
