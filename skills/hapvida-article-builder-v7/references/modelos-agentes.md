# Multi-agentes em modelos diferentes — quem roda em quê, e por quê [V7.2]

> Esta referência é a camada **V7.2** da skill. Ela não muda o QUE cada agente
> faz (isso continua na seção "LINHA DE AGENTES ESPECIALISTAS" do `SKILL.md`) —
> ela decide **em qual modelo cada agente roda** e **quais pares de agentes não
> podem compartilhar modelo**.

**Artigo novo do zero sai automaticamente pela linha** (city, hospital, TR,
pillar). O usuário não precisa pedir "multiagente". Edição pontual, consulta e
auditoria avulsa saem em **agente único** — abrir a linha para trocar um
parágrafo custa mais do que resolve.

---

## 1. O critério de roteamento

> **O modelo se escolhe pelo custo do erro dividido pela chance de o erro ser
> pego.** Barato onde o erro é mecânico e uma trava (`checkpoint_*.py`) pega.
> Forte onde o erro é de julgamento e sai publicado sem ninguém notar.

Duas perguntas, nessa ordem, para cada agente:

1. **Se este agente errar, o erro chega ao leitor?** Se existe trava mecânica
   que pega (script, conferente com fonte na mão, `FORBIDDEN_TOKENS`), o erro é
   barato → pode rodar em modelo barato.
2. **O erro é de fato ou de julgamento?** Fato errado com fonte disponível
   qualquer modelo pega na conferência. **Julgamento errado ninguém pega** — o
   fio condutor torto, o ângulo do CI-2 que não é ângulo nenhum, a frase que
   passa no teste de substituição de cidade. Julgamento → modelo forte, sempre.

**Consequência desconfortável, dita sem rodeio:** em artigo YMYL o gasto é
concentrado na **verificação**, não na redação. Rascunho é a parte barata do
trabalho. Quem economiza no juiz e gasta no redator inverteu a conta.

**O principal (você, a sessão que orquestra) orquestra, revisa e decide — nunca
executa tarefa em lote.** Toda saída de subagente passa pela sua revisão antes
de virar insumo do próximo. Um subagente barato sem revisão do principal é um
dado não conferido entrando na linha pela porta dos fundos.

---

## 2. Os três degraus

| Degrau | Uso | Modelo em Claude Code (`Agent`/`Workflow`) |
|---|---|---|
| **forte** 🔒 | julgamento, verificação, síntese, juízo | `opus` |
| **médio** | redação com trava, coleta que exige classificar | `sonnet` |
| **barato** | leitura de arquivo grande, rodar script, coleta verificável | `haiku` |

Os nomes valem para o roteamento; a família exata é a que estiver disponível na
sessão. **O que importa não é a marca do degrau — é a distância entre dois
degraus vizinhos e a regra de modelo diferente da §4.**

🔒 = **agente travado**: não aceita rebaixamento por economia, em nenhuma
hipótese. Rebaixar um 🔒 é a falsa economia que esta camada existe para impedir.

---

## 3. A linha da v7 roteada (25 agentes — 0 a 24)

Numeração e funções idênticas às do `SKILL.md` — aqui só entra a coluna de
modelo e o porquê.

### Estágio 1 — Pesquisa (FASE 0)

| # | Agente | Modelo | Por quê |
|---|---|---|---|
| 0 | Diagnóstico do pillar (só pillar existente) | **forte** 🔒 | decide manter URL ou 301 e nomeia a causa; erro aqui joga fora meses de autoridade interna |
| 1 | Buscas e tipo de página | médio | a coleta é mecânica, mas **decidir o tipo de página que o Google premia** é julgamento |
| 2 | Rede assistencial | médio | volumoso e verificável (catálogo do banco manda), porém YMYL: **nunca barato** — foi onde Piracicaba errou |
| 3 | Contexto local (IBGE/CNES, bairros) | barato | número público, confere com a fonte |
| 4 | Keywords, PAA e query fan-out | barato → médio | coletar volume é barato; **classificar o fan-out em aqui/cluster/pendência é médio** |
| CI-1 | Desmontagem de concorrentes | **forte** 🔒 | exige julgar tipo de página, cobertura e onde o concorrente é fraco |
| CI-2 | Ganho de informação + defensibilidade | **forte** 🔒 | é a decisão que define o artigo; nível de defensibilidade errado contamina tudo |
| 5 | Síntese, fio condutor e anti-doorway | **forte** 🔒 | o fio condutor viaja da S1 à S7; torto aqui, torto no artigo inteiro |

### Estágio 2 — Conferência da pesquisa

| # | Agente | Modelo | Por quê |
|---|---|---|---|
| 6 | Conferente de fatos | **forte** 🔒 | é a trava anti-alucinação principal; **e roda em modelo diferente do Agente 2** (§4) |
| 7 | Conferente de dados DataForSeo | barato | o número confere com a fonte — erro é pego na hora |
| **23** | **Juiz P-A — suficiência e verdade [V7.2]** | **forte** 🔒 | decide se dá para escrever sem inventar |
| **24** | **Juiz P-B — originalidade e valor [V7.2]** | **forte** 🔒 | decide se o artigo merece existir; **modelo ≠ 23**, e **≥1 dos dois ≠ Agente 5** |

### Estágio 3 — Redação

| # | Agente | Modelo | Por quê |
|---|---|---|---|
| 8 | Redator do Bloco A | **forte** | o Bloco A carrega o **Lead GEO + a tabela no topo (v7)**: é a passagem que a IA extrai e a primeira tela que converte |
| 9 | Redator do Bloco B | médio | rascunho com state file aprovado na mão + editor-chefe forte atrás |
| 10 | Redator do Bloco C | médio | idem (FAQ e fechamento) |

> **Por que o Bloco A não é médio:** desde a v7 a primeira tela é o produto. O
> lead citável e a moldura da tabela são o que o AI Overview lê e o que decide
> o clique. É o único bloco em que a redação é julgamento, não redação.

### Estágio 3.5 / 3.6 — Editor-chefe, voz e imagem

| # | Agente | Modelo | Por quê |
|---|---|---|---|
| 11 | Editor-chefe | **forte** 🔒 | é a mente única; decide `[VERIFICAR]` por suavização/omissão — a decisão mais delicada da linha |
| 19 | Voz humana | médio | roda `checkpoint_voz.py` (mecânico) e decide os 🟡; **modelo diferente do 11** (§4) |
| 20 | Imagem da tabela | barato | roda `gerar_imagem_artigo.py` com os valores da mesma fonte dos shortcodes; valor faltando = falha barulhenta |

### Estágio 4 — Auditorias

| # | Agente | Modelo | Por quê |
|---|---|---|---|
| 12 | Veracidade (Modo 1) | **forte** 🔒 | pega a nuance que `checkpoint_verificar.py` não pega ("a unidade opera hoje") |
| 13 | Anti-doorway (Modo 3) | **forte** 🔒 | teste de substituição frase a frase e caça-clichê são julgamento puro |
| 14 | Requisitos da skill (Modo 2) + checkpoints | barato → médio | rodar script é barato; **interpretar 🟡 e decidir devolução é médio** |
| 15 | Citabilidade/GEO (Modo 4) | **forte** 🔒 | por plataforma, número em texto, nível de defensibilidade da passagem |

### Estágio 5 — Juízo adversarial

| # | Agente | Modelo | Por quê |
|---|---|---|---|
| 16a | Juiz A — lente factual/YMYL | **forte** 🔒 | — |
| 16b | Juiz B — lente anti-doorway/SEO | **forte** 🔒 | — |
| 16c | Juiz C — lente do leitor/voz | **forte** 🔒 | — |
| **21** | **Varredura final anti-doorway [V7.2]** | **forte** 🔒 | última chamada no HTML que vai ao ar; **modelo diferente do Agente 13** (quem auditou doorway na produção não assina a liberação) |
| 17 | Schema JSON-LD | médio | mecânico, mas o erro é silencioso; valida em ferramenta externa |
| 18 | Registro no banco | barato | chamada de MCP com campos fechados |
| **22** | **Roteador de modelos [V7.2]** | barato | escreve o `PLANO_MODELOS` antes do Estágio 1 e roda `checkpoint_modelos.py` |

> **O painel de juízes é o coração desta camada.** O `SKILL.md` já admite o
> problema: *"como os três são o mesmo modelo, erro correlacionado (mesmo ponto
> cego) é risco real"*. A resposta da v3 foi dar **lentes** diferentes. A v7.2
> acrescenta a outra metade: **modelos** diferentes. Lente distinta separa o que
> cada juiz procura; modelo distinto separa o que cada juiz **é capaz de não
> ver**. As duas juntas é que tornam o voto majoritário digno do nome.

---

## 4. As travas (o que esta camada acrescenta de inegociável)

**T1 — Nunca barateie a verificação.** Agentes 🔒 (0, CI-1, CI-2, 5, 6, 11, 12,
13, 15, 16a-c, 21, 23, 24) rodam sempre no degrau forte. Sem exceção por prazo, por lote ou
por artigo "pequeno".

**T2 — Quem confere roda em modelo diferente de quem produziu.** É a regra-mãe
da linha ("quem inventa um dado nunca é quem confere esse dado") levada um nível
acima: mesma função separada **e** modelo separado. Pares obrigatórios:

| Produz | Confere | Precisam diferir |
|---|---|---|
| 2 (rede) | 6 (fatos) | sim |
| 4 (keywords) | 7 (DataForSeo) | sim |
| 8/9/10 (redação) | 11 (editor-chefe) | sim |
| 11 (costura da voz) | 19 (voz humana) | sim |
| 5 (fio condutor/anti-doorway) | 13 (anti-doorway) | sim |
| 13 (anti-doorway na produção) | 21 (varredura final) | sim |
| 5 (síntese da pesquisa) | 23 **ou** 24 | ao menos um dos dois em modelo diferente do 5 |
| 23 (juiz P-A) | 24 (juiz P-B) | sim — as duas lentes em modelos diferentes |
| 11 + 8/9/10 | pelo menos 1 juiz | sim |

**T3b — Diversidade no portão de pesquisa [V7.2].** Os juízes 23 e 24 rodam em
modelos **diferentes entre si**, e **pelo menos um dos dois** em modelo diferente
do Agente 5 — quem sintetizou a pesquisa não pode ser o único ponto de vista que
a aprova. Mesma lógica do painel final, ajustada ao tamanho do objeto.

**T3 — Diversidade no painel.** Entre 16a, 16b e 16c tem de haver **no mínimo 2
modelos distintos**, e **pelo menos um juiz** em modelo diferente de todos os
que escreveram ou editaram o artigo. Achado de **voz** apontado só por um juiz
que roda no mesmo modelo do editor-chefe **não conta voto** — é o ponto cego
compartilhado se auto-elogiando.

**T4 — Rascunho barato só sai depois da revisão do principal.** Bloco vindo de
agente médio/barato não entra no artigo sem passar por você.

**T5 — Não delegue tarefa pequena.** Abrir subagente custa dezenas de milhares
de tokens só de carregar contexto. Delegue o **pesado e volumoso** (varredura da
rede, extração de concorrentes, auditoria do artigo inteiro). Consulta de duas
linhas se resolve na própria sessão — delegar sai mais caro que fazer.

**T6 — Subagente devolve resultado enxuto** — tabela, bloco pronto, veredito,
bastão. Nunca o passo a passo do raciocínio.

**T7 — Rebaixamento desce um degrau só, e nunca em 🔒.** Se for preciso cortar
custo, o caminho é médio→barato em agente **não travado** (3, 4, 7, 14, 17, 18,
20), com o motivo escrito no `PLANO_MODELOS`. Forte→barato é proibido: pular
degrau é onde o erro deixa de ser pego.

**T8 — Dado YMYL nunca em modelo barato sem trava que o pegue.** Rede
assistencial, carência, coparticipação, preço e regra da ANS: médio ou forte,
sempre — a não ser que um `checkpoint_*.py` reprove mecanicamente o erro
possível.

---

## 5. Como declarar — o bloco `PLANO_MODELOS`

O **Agente 22** escreve este bloco **antes** de disparar o Estágio 1 — quando
ainda não existe state file — num arquivo `PLANO_MODELOS_[slug].md`. Quando o
state file nascer (fim do Estágio 1), o bloco é **copiado para a seção 10 dele**,
para o handoff, a auditoria e a próxima sessão acharem o roteamento que foi de
fato usado. Uma linha por agente:

```
PLANO_MODELOS:
22 | roteador-modelos     | barato | haiku   |
0  | diagnostico-pillar   | forte  | opus    | pillar ja existe (canibalizacao)
1  | serp-tipo-pagina     | medio  | sonnet  |
2  | rede-assistencial    | medio  | sonnet  |
3  | contexto-local       | barato | haiku   |
4  | keywords-fanout      | medio  | sonnet  |
CI-1 | desmontagem        | forte  | opus    |
CI-2 | ganho-informacao   | forte  | opus    |
5  | sintese-fio-condutor | forte  | opus    |
6  | conferente-fatos     | forte  | opus    | T2 com o 2 (sonnet)
23 | juiz-pesquisa-a      | forte  | sonnet  | != do 5 (opus), que sintetizou
24 | juiz-pesquisa-b      | forte  | opus    | != do 23 (as duas lentes separadas)
7  | conferente-dataforseo| barato | haiku   |
8  | redator-bloco-a      | forte  | sonnet  | T2 com o 11 (opus)
9  | redator-bloco-b      | medio  | sonnet  |
10 | redator-bloco-c      | medio  | sonnet  |
11 | editor-chefe         | forte  | opus    |
19 | voz-humana           | medio  | sonnet  | T2 com o 11 (opus)
20 | imagem-tabela        | barato | haiku   |
12 | veracidade           | forte  | opus    |
13 | anti-doorway         | forte  | sonnet  | T2 com o 5 (opus)
14 | requisitos           | medio  | sonnet  |
15 | citabilidade-geo     | forte  | opus    |
16a| juiz-factual         | forte  | opus    |
16b| juiz-doorway         | forte  | sonnet  | T3 — lente B em modelo distinto
16c| juiz-leitor          | forte  | opus    |
21 | varredura-doorway    | forte  | opus    | T2 com o 13 (sonnet)
17 | schema               | medio  | sonnet  |
18 | registro-banco       | barato | haiku   |
```

Campos: `# | função | degrau | modelo | observação`. O **4º campo (modelo) é o
que a trava compara** — degrau sem modelo não prova diversidade nenhuma.

> **Degrau e modelo são eixos diferentes — leia isto antes de achar que o plano
> se contradiz.** O **degrau** diz quanto julgamento aquele assento exige (e é o
> que o T1 protege). A **coluna de modelo** diz qual cérebro senta ali (e é o que
> o T2/T3 comparam). Por isso o Agente 8, o 13 e o Juiz B aparecem como
> `forte | sonnet`: continuam sendo assentos de julgamento — rubrica inteira,
> lente completa —, só rodam em outro modelo para que o par que os confere não
> compartilhe ponto cego com eles.
>
> **Com dois modelos capazes, o critério de quem fica com o melhor é simples:
> o assento de CONFERÊNCIA fica com o mais forte.** Entre 8 e 11, o editor-chefe
> leva o topo; entre 5 e 13, o anti-doorway pode ceder porque ainda tem o painel
> de juízes atrás. Nunca o contrário: produtor forte com conferente fraco é a
> configuração que deixa o erro passar.

---

## 6. Trava mecânica — `checkpoint_modelos.py`

```bash
python -X utf8 C:\Users\netop\.claude\skills\hapvida-article-builder-v7\checkpoint_modelos.py <state_file.md|plano.md> [city|tr|pillar|hospital]
```

**Reprova (🔴, bloqueia o disparo da linha):**
1. agente obrigatório ausente do plano;
2. agente 🔒 em degrau abaixo de forte;
3. par produtor/conferente da T2 no **mesmo modelo**;
4. painel com um único modelo entre 16a/16b/16c;
5. nenhum juiz em modelo diferente do editor-chefe (11);
6. degrau inválido (fora de forte/medio/barato).

**Avisa (🟡, não bloqueia):**
- linha inteira em um só modelo (**monomodelo declarado** — ver §7);
- agente não travado rebaixado sem observação escrita;
- plano com agente que não existe na linha (provável erro de digitação).

A trava roda **antes** do Estágio 1 e é responsabilidade do Agente 22. Rodar
depois do artigo pronto não serve para nada: o plano já foi executado.

> **Por que virar script e não "o agente lembra":** esta skill já perdeu camada
> duas vezes por confiar na memória do agente (a v2 esquecida no duelo, a
> citabilidade dormente). **Camada sem trava é camada dormente.** O roteamento
> de modelo é exatamente o tipo de coisa que some sob pressa.

---

## 7. Quando só existe um modelo (o modo honesto)

Sessão com um modelo só é caso real — e a resposta certa não é fingir que a
camada rodou.

- Declare no plano: `MODO: monomodelo (<modelo>)`. O checkpoint passa com 🟡.
- **O que se mantém:** separação de função, lentes distintas dos três juízes,
  rodadas separadas (juiz nunca lê o veredito do outro antes de escrever o seu),
  todas as travas mecânicas.
- **O que se perde, dito sem enfeite:** a proteção contra erro correlacionado.
  Mesmo modelo com prompt diferente **não** é modelo diferente — o ponto cego é
  do modelo, não do prompt. Em monomodelo, o voto majoritário vale menos, e o
  **portão humano vale mais**.
- **Compensação parcial:** aumentar o esforço de raciocínio do juiz
  (`effort: high`) e separar as rodadas no tempo ajuda um pouco. Não substitui.

---

## 8. Como disparar, na prática (Claude Code)

**Subagente avulso** — a ferramenta `Agent` aceita `model`:

```
Agent(subagent_type: "general-purpose", model: "haiku",
      description: "coleta contexto local",
      prompt: "<bastão do Agente 3 + a função + o formato de retorno>")
```

**Linha inteira** — em `Workflow`, cada `agent()` aceita `model` e `effort`:

```js
const rede   = await agent(P_REDE,    {label: 'a2-rede',    model: 'sonnet', schema: REDE})
const fatos  = await agent(P_FATOS,   {label: 'a6-fatos',   model: 'opus',   schema: VEREDITO})
const juizes = await parallel([
  () => agent(P_JUIZ_A, {label: '16a', model: 'opus',   effort: 'high', schema: RUBRICA}),
  () => agent(P_JUIZ_B, {label: '16b', model: 'sonnet', effort: 'high', schema: RUBRICA}),
  () => agent(P_JUIZ_C, {label: '16c', model: 'opus',   effort: 'high', schema: RUBRICA}),
])
```

Regras de uso que valem mais que a sintaxe:

- **Estágios paralelos:** 1-4 juntos, 12-15 juntos, 16a-c juntos. Conferente
  **nunca** em paralelo com quem ele confere.
- **Cada agente recebe o bastão, não a conversa.** É o que torna o agente
  barato viável: contexto pequeno e função única.
- **Cada agente devolve no formato do bastão curto** (modelo no `SKILL.md`).
- **Delegar tem custo fixo.** Abaixo de ~3 chamadas de ferramenta ou de um
  arquivo grande para ler, faça na sessão.

---

## 9. Onde o dinheiro vai (ordem de grandeza, não promessa)

Numa linha completa de artigo de city, o peso costuma ficar assim:

| Bloco | Fatia do custo | Observação |
|---|---|---|
| Estágio 1 (pesquisa + CI) | ~25% | volumoso; é onde o barato rende |
| Estágio 3 (redação) | ~20% | Bloco A forte, B/C médio |
| Estágios 4-5 (auditorias + 3 juízes) | ~45% | **é aqui que a qualidade é comprada** |
| Resto (conferência, voz, imagem, schema, banco) | ~10% | quase tudo barato |

**A leitura correta dessa tabela:** se o seu corte de custo mirar os 45%, você
não economizou — mudou de produto. Corte nos 25% e nos 10%, que é onde a trava
mecânica pega o erro.

---

## 10. Gatilhos desta camada

`multi-agente`, `multiagente`, `modelos diferentes`, `qual modelo`, `roteamento
de modelo`, `plano de modelos`, `agente barato`, `modelo forte`, `custo da
linha`, `economizar token`, `juiz em outro modelo`, `erro correlacionado`,
`monomodelo`.

Fora disso, a linha roda como na v7.1 — com o degrau padrão da §3 aplicado
silenciosamente quando o usuário pedir a linha de agentes.
