# Camada GEO/AEO/Entidade — V2 (exclusiva do hapvida-article-builder-geo)

Este arquivo é o **diferencial da v2** sobre o `hapvida-article-builder` (v1). Ele NÃO substitui nada da v1 — estende. Tudo que a v1 faz (Fase 0, anti-doorway, S1-S7/HS/TR, E-E-A-T, schema `@graph`, Regras de Ouro, checkpoints de parágrafo/ritmo) continua valendo igual. Aqui entra só a camada de **otimização para citação em motores generativos** (Google AI Overviews/AI Mode, ChatGPT, Perplexity, Bing Copilot) e o reforço de **entidade**.

> A v1 já tem "Lead GEO" (o lead que a IA extrai). A v2 leva esse mesmo princípio para **o corpo inteiro do artigo**, formaliza o schema de entidade/voz, adiciona uma checagem de **tipo de página (SXO)** na Fase 0 e um **4º modo de auditoria**.

---

## ⚠️ RESSALVAS (ler antes de aplicar)

Estas regras vêm de skills de SEO de terceiros (claude-seo, seo-geo-optimizer) e de estudos de 2025-2026. Aplicar com cabeça:

1. **GEO ≈ SEO de sempre.** A posição oficial do Google é que otimizar para IA generativa "ainda é SEO". As táticas estruturais abaixo (resposta direta, E-E-A-T, recência, entidade) se sustentam; trate-as como **boas práticas de SEO**, não como disciplina paralela.
2. **Números percentuais são DIRECIONAIS.** Vários "+35%", "+40%", "134-167 palavras", "44% das citações nos primeiros 30%" vêm de estudos únicos, não replicados. Use como **heurística de direção** (front-load funciona, passagem auto-contida funciona), nunca como meta numérica rígida nem como afirmação dentro do artigo.
3. **`llms.txt` NÃO é alavanca comprovada** de citação (Mueller/Illyes/estudos de log). Opcional, custo zero; não prometer resultado.
4. **YMYL e faixa da corretora continuam invioláveis.** Tudo aqui respeita as travas da v1: a "entidade-autor" é a **DRV / autor do tabelaplanos** (Jessica/Victor), NUNCA conselho médico, NUNCA inventar dado. Os exemplos de "Dr. tal, MD/PhD" das skills de origem são de clínica médica dos EUA — **não** copiar esse mundo; adaptar à DRV.
5. **Nada aqui afrouxa o anti-doorway.** Uma "resposta direta" citável de cidade tem de continuar sendo **específica da cidade** — se a passagem serve para qualquer cidade trocando o nome, é doorway, mesmo que seja "citável".

---

## 1. CITABILIDADE POR PASSAGEM (a maior adição da v2)

Motores generativos extraem **passagens**, não páginas. A v1 já faz isso no lead; a v2 estende para **cada seção CORE** (S1-S7, HS1-HS4, TR2-TR4) e para o FAQ.

### 1.1 Resposta direta no topo de cada seção CORE
- Logo após o H2 (antes de contexto/narrativa), abrir com **1 frase-resposta auto-suficiente de ~40-60 palavras** que responde à intenção daquela seção, com **dado específico da cidade/hospital**.
- Padrão: definição/afirmação direta + 1 número-âncora + 1 diferencial local. Sem "Você sabia que", sem rampa de aquecimento.
- Exemplo (S4 Rede, Betim): *"A rede Hapvida em Betim é ancorada no Hospital [X], com [N] leitos e pronto-socorro 24h, complementada por [N] clínicas próprias nos bairros [A] e [B]. É a maior estrutura verticalizada da cidade, o que reduz o tempo entre consulta, exame e internação dentro da própria rede."*
- Essa frase é o que a IA tende a extrair. Ela **não dispensa** o restante da seção — é a porta de entrada.

### 1.2 Blocos auto-contidos (~130-167 palavras, direcional)
- Dentro da seção, estruturar a informação em **blocos que façam sentido isolados** (extraíveis sem o parágrafo anterior). Cada bloco = uma ideia + seu dado + sua fonte.
- Isso casa naturalmente com o checkpoint de parágrafo da v1 (≤380 chars/≈55 palavras): 2-3 parágrafos curtos formam um bloco citável. Não criar um parágrafo gigante — agrupar parágrafos curtos sob um H3 ou box.

### 1.3 Front-load (o mais citável vem cedo)
- O dado/ângulo mais forte da seção vai **no início dela**, não enterrado no fim. Vale para o artigo como um todo: o material mais citável nas primeiras seções, não só na conclusão.

### 1.4 Headings em forma de pergunta quando a SERP pede
- Quando a Fase 0 (DR1, `serp_local` + `related_keywords`/PAA) revela que a query é interrogativa ("quanto custa", "qual a rede", "como funciona"), usar **H2/H3 no formato da pergunta** (ou muito próximo). A v1 já adapta PAA no FAQ; a v2 também usa headings interrogativos nas seções correspondentes. Não forçar onde a query não é pergunta.

### 1.5 Estatística com fonte em cadência
- Distribuir **dados quantificados com fonte verificável** ao longo do corpo (não amontoados numa seção). Cada afirmação forte = número + fonte primária (IBGE/CNES/ANS/RI Hapvida) — exatamente as fontes que a v1 já manda variar. Afirmação sem dado é menos citável e menos E-E-A-T.
- Trava da v1 continua: número sem fonte vira `[VERIFICAR]` e **fica fora** do artigo.

---

## 2. SOURCING POR PLATAFORMA + SINAL OFF-PAGE (estratégia, não HTML)

Cada motor cita fontes diferentes; e **menção de marca correlaciona mais com citação em IA do que backlink** (direcional, estudo Ahrefs). Isso não muda o HTML do artigo — orienta a estratégia ao redor dele:

| Motor | Tende a citar | Implicação para a DRV |
|-------|---------------|------------------------|
| Google AI Overviews | quem já ranqueia bem | manter o SEO clássico forte (a v1 já faz) |
| Google AI Mode | pool mais amplo; recência + entidade > posição | recência real (§4) + entidade (§3) |
| ChatGPT | Wikipedia, fontes de autoridade | consistência de entidade/marca |
| Perplexity | discussão/comunidade, recência | presença e menções recentes |

**Ações fora do artigo (medir, não chutar):**
- Reforçar presença e consistência de marca onde o público BR de plano de saúde aparece: **Reclame Aqui, YouTube, perfis oficiais**, com NAP/descrição idênticos aos do schema.
- **Medir** citação real com as tools que já existem no projeto: `monitor_citacoes_ia` e `buraco_citacao_ia` (skill `dataforseo-tabelaplanos` → AI Overview / LLM Mentions). Priorizar cidades/keywords onde o site **deveria** ser citado e não é.
- Não prometer citação; tratar como programa contínuo medido pelo banco.

---

## 3. SCHEMA — REFORÇO DE ENTIDADE E VOZ (estende `references/schema-jsonld.md`)

A v1 já monta `@graph` com `@id` ligando WebPage ↔ Article ↔ Person ↔ Organization e usa `sameAs` das entidades canônicas. A v2 adiciona **dois reforços**, sem mudar o resto. Continua execução SEPARADA ("gera o schema") e continua valendo a regra anti-duplicação Rank Math.

### 3.1 `speakable` no nó WebPage (ou Article)
Diz ao motor quais trechos ler/extrair (lead + FAQ). Adicionar ao schema de City/Hospital:
```json
"speakable":{
  "@type":"SpeakableSpecification",
  "cssSelector":[".lead-geo","h1","h2",".faq-pergunta"]
}
```
> Ajustar os seletores aos que o HTML do artigo realmente usa. Se o lead não tem classe `.lead-geo`, usar o seletor real ou `h1`+primeiro parágrafo.

### 3.2 Person enriquecido (autor DRV — Jessica/Victor)
Os nós Person FIXOS da v1 continuam idênticos; a v2 **acrescenta** dois campos de entidade-autor, quando confirmados com o usuário (nunca inventar perfil):
```json
"knowsAbout":["Planos de saúde","Hapvida","Coparticipação","ANS","Portabilidade de plano"],
"sameAs":["<perfil LinkedIn do autor, se existir>","<página de autor no site>"]
```
- `knowsAbout` é seguro (descreve o tema do autor). `sameAs` só com URL **real e confirmada** — sem perfil verificável, omitir. Isso reforça a entidade-autor que o E-E-A-T YMYL valoriza.
- Manter `author.@id` → `#jessica-mendes`/`#victor-castro` e a regra de bater com o widget (igual v1).

---

## 4. RECÊNCIA COMO ALAVANCA DE CITAÇÃO (estende a Regra de Ouro 5c)

A Regra 5c da v1 já distingue recência real de cosmética. A v2 acrescenta a **leitura GEO**: conteúdo recente é desproporcionalmente mais citado em IA (direcional: ~3x para <3 meses; queda após ~6 meses parado). Logo:
- A cadência de revisão de ~90 dias da v1 deixa de ser higiene e vira **alavanca de citação** — priorizar revisão real das páginas-cidade de maior tráfego/intenção comercial.
- `dateModified` só muda com revisão **substancial** (regra 5c intacta). Registrar a revisão no banco (`atualizar_artigo`) para o banco priorizar os mais antigos.

---

## 5. MULTI-MODAL (alinha com o "ritmo visual" da v1)

Conteúdo com elemento visual relevante tende a ser mais selecionado (direcional). A v1 já força quebra visual a cada ≤3 parágrafos — a v2 só pede que, quando possível, a quebra seja **informativa e citável** (tabela comparativa real, card de métricas com dado da cidade, imagem com `alt` descritivo) em vez de decorativa. Sem inventar dado para preencher visual.

---

## 6. CHECAGEM DE TIPO DE PÁGINA — SXO (entra na Fase 0)

A v1 já lê os 10 primeiros da SERP (Regra de Ouro 2). A v2 adiciona um **veredito explícito de tipo de página** ao DR1, inspirado no SXO:
- Classificar os 10 resultados: a SERP da keyword premia **guia/pillar de cidade**, **tabela/imagem**, **página de hospital**, **home de operadora**, ou **comparador**?
- Se o tipo dominante (>60%) **diverge** do tipo que vamos publicar (ex.: a SERP é toda tabela/preço e íamos fazer guia S1-S7), **registrar isso no state file da Fase 0** e ajustar a arquitetura (talvez seja caso de TR, não de City). Isso evita o artigo tecnicamente perfeito que nunca ranqueia por ser o **tipo errado**.
- Não vira fase nova nem PAUSA extra — é um campo a mais no checkpoint do DR1.

---

## 7. TÉCNICO DE SITE (uma vez, fora do artigo)

Itens de site, não de artigo — sugerir ao usuário, não embutir no HTML:
- **`robots.txt`** liberando crawlers de IA: `GPTBot`, `OAI-SearchBot`, `ChatGPT-User`, `PerplexityBot`, `ClaudeBot`. (Bloquear treino, ex. `CCBot`, é opção do usuário.)
- **IndexNow** para indexação instantânea no Bing/Copilot ao publicar/revisar (o script `indexnow_submit.py` da skill `seo-geo-optimizer` faz isso).
- **`llms.txt`** — opcional, custo zero, **sem promessa** (ver ressalva 3).

---

## 8. CHECKLIST GEO/AEO (rodar junto do MODO 2 da v1)

Por artigo:
- [ ] Cada seção CORE abre com resposta direta de ~40-60 palavras, **específica da cidade/hospital** (não genérica — passa no teste de substituição).
- [ ] Informação em blocos auto-contidos; dado mais forte no início da seção (front-load).
- [ ] Headings interrogativos onde a SERP/PAA é pergunta.
- [ ] Dado quantificado + fonte primária distribuídos no corpo; zero número sem fonte.
- [ ] Schema (quando gerado) inclui `speakable` e Person com `knowsAbout` (+`sameAs` se confirmado).
- [ ] `dateModified` reflete revisão real; revisão registrada no banco.
- [ ] Veredito de tipo de página (SXO) no state file da Fase 0 bate com o tipo publicado.
- [ ] (Site) crawlers de IA liberados + IndexNow no publish — checado 1×.

---

## 9. MODO 4 — AUDITORIA GEO/AEO DE CITABILIDADE (4º modo, separado)

Adiciona-se aos 3 modos da v1 (veracidade / requisitos / doorway). Mesmas regras-mãe: **só sob gatilho explícito, isolado, profundidade > velocidade, classificação 🔴/🟡/🟢 + veredito.**

**Gatilhos:** "checa o GEO", "audita citabilidade", "isso é citável por IA?", "audita AEO".

**Execução:**
1. Para cada seção CORE e cada FAQ: a passagem de abertura responde a uma intenção real **sozinha**? (extrair mentalmente só ela — faz sentido?)
2. Rodar `python -X utf8 C:\Users\netop\.claude\skills\hapvida-article-builder-v5\checkpoint_citabilidade.py <arquivo.html>` e colar a saída (mede resposta-direta no topo das seções, front-load e densidade de fonte). Reprovado → corrigir e repetir.
3. Teste anti-doorway sobre as passagens citáveis: troque a cidade — se a frase-resposta continua válida, **não é citável-única**, é doorway. 🔴.
4. Cruzar com citação real medida (`monitor_citacoes_ia`/`buraco_citacao_ia`): a página é citada nas keywords-alvo? Onde falta? — **[V6] em artigo já publicado isto deixou de ser "quando disponível" e virou obrigatório**, com o estado classificado em *citado / concorrente citado, nós não / ninguém citado / não medido*. Ver "FASE 5 → MEDIÇÃO DE CITAÇÃO EM IA [V6]" no `SKILL.md`.
5. Schema: `speakable` presente? Person com `knowsAbout`? `dateModified` real?

**Saída:** tabela `seção/FAQ → passagem de abertura → citável? (🔴/🟡/🟢) → fonte presente? → correção` + veredito.
