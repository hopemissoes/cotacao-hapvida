# Painel de juízes da PESQUISA — o julgamento que faltava no começo [V7.2]

> **O problema que isto resolve.** A skill tinha juízo adversarial de sobra — no
> **fim**. Três juízes com lentes distintas liam o artigo pronto e apontavam o
> que estava errado. Só que **erro de pesquisa não se conserta na redação**: se a
> S7 não tem dado local, nenhum juiz de texto vai fazer aparecer; o redator vai
> preencher com genérico, o editor vai costurar bonito, e o juiz vai reprovar
> "doorway na S7" — três estágios depois de o problema ter nascido.
>
> **A regra:** julgar cedo custa uma rodada; julgar tarde custa o artigo inteiro.

**Quando roda:** fim do **Estágio 2** (depois da conferência de fatos do Agente 6
e antes de UMA linha de HTML). É o segundo portão da linha, e é bloqueante.

**Quem roda:** **Agente 23 — Juiz P-A (suficiência e verdade)** e **Agente 24 —
Juiz P-B (originalidade e valor)**. Ambos **forte 🔒**, em **modelos distintos
entre si**, e **pelo menos um dos dois** em modelo diferente do **Agente 5**
(quem sintetizou a pesquisa) — quem montou não pode ser o único ponto de vista
que aprova o que montou. É a trava **T3b** de `references/modelos-agentes.md`.

---

## Antes dos juízes: a trava mecânica

```bash
python -X utf8 C:\Users\netop\.claude\skills\hapvida-article-builder-v7\checkpoint_suficiencia.py <state_file.md> --cidade "Piracicaba" --tipo city --ancoras <ancoras.txt>
```

Ela entrega aos juízes o **mapa do que está vazio**, para eles não gastarem
atenção com o que é contável:

| | Mede | 🔴 |
|---|---|---|
| **A** | itens da pesquisa que sustentam cada seção prevista | qualquer **seção órfã** (zero itens) |
| **B** | FAQ que sobrevivem à troca da cidade; FAQ duplicadas entre si | > 20% genéricas, ou qualquer par duplicado |
| **C** | secundária "qualificada" que é tráfego de quem **já é cliente** | qualquer uma |
| **D** | defensibilidade do ganho de informação do CI-2 | nível 4-5, ou não declarado |
| **E** | diferenciais sem âncora local | > 34% |

Reprovou → **volta ao Estágio 1**, ao agente da função — não à redação.

---

## As duas lentes

### Agente 23 — Juiz P-A: suficiência e verdade

Pergunta-mãe: **"dá para escrever este artigo inteiro só com isto, sem inventar
nada?"**

1. **Percorrer o esqueleto seção a seção** (S1-S7 / P1-P9 / HS1-HS4 / TR1-TR5) e,
   para cada uma, nomear **o dado do state file que a sustenta**. Seção que só
   tem "contexto geral" está órfã, mesmo que o script tenha achado palavras.
2. **Cada afirmação estrutural tem fonte forte?** Fonte de nível 1-2 ou primária
   para o que sustenta seção; nada estrutural apoiado só em agregador ou em
   uma fonte só (regra das 2 fontes para estrutura/marco histórico).
3. **A regra das duas listas foi aplicada?** Toda unidade com `no_catalogo` e
   `no_guia_oficial` preenchidos, e as divergências viraram `[VERIFICAR]` de
   operação — não sumiram nem foram promovidas a fato.
4. **Os `[VERIFICAR]` e o `nao_encontrado` estão coerentes?** Item em
   `nao_encontrado` não pode reaparecer como dado em outra parte da pesquisa.
5. **O `FORBIDDEN_TOKENS` cobre o que a pesquisa descartou?** Nome de unidade
   refutado que não está lá é um erro esperando para acontecer.

### Agente 24 — Juiz P-B: originalidade e valor

Pergunta-mãe: **"se este artigo for publicado exatamente com esta pesquisa, ele
merece existir na SERP?"**

1. **Teste de substituição aplicado à PESQUISA** (não ao texto): trocar a cidade
   e contar quantos itens continuam verdadeiros. Item que sobrevive é item que
   vai virar parágrafo genérico.
2. **O ganho de informação do CI-2 é ganho mesmo?** Nível 1-2, e responde a algo
   que os 10 da SERP não respondem. "Somos especialistas há 11 anos" não é ganho.
3. **As FAQ nasceram de dado local ou de paráfrase de PAA?** Cada pergunta tem um
   dado do DR1 atrás dela?
4. **As secundárias trazem quem compra?** Veto de intenção aplicado de verdade —
   volume alto de quem já é cliente é prejuízo, não ganho.
5. **O fio condutor é uma tese ou uma frase bonita?** "Cidade industrial, rede
   que aguenta demanda de trabalhador" é tese (dá para checar na S4 e na S5).
   "Cidade que merece saúde de qualidade" não é nada.
6. **O que os MUST-MATCH dos concorrentes cobrem e nós não?** Falta de must-match
   é buraco garantido; e a lacuna que ninguém cobre é a nossa chance.

---

## Rubrica (as duas notas, 0-10, sem suavizar)

| Dimensão | Juiz | O que 10 significa |
|---|---|---|
| Suficiência por seção | P-A | toda seção tem dado próprio nomeado |
| Verdade e fonte | P-A | nada estrutural sem fonte forte; divergências marcadas |
| Originalidade (substituição) | P-B | ≥ 70% dos itens morrem ao trocar a praça |
| Valor comercial | P-B | ganho nível 1-2 + secundárias de quem compra |

**Regra de parada:** libera para o Estágio 3 com **as 4 dimensões ≥ 8** e **zero
🔴**. Senão, refino dirigido — **no máximo 2 rodadas**, e então portão humano com
o que travou dito em uma linha.

**Para onde volta cada achado:** seção órfã → Agente 2/3 (recoletar) · fonte
fraca → Agente 6 · FAQ genérica → Agente 4 + 5 · ganho fraco → CI-2 · fio
condutor vago → Agente 5 · secundária ruim → Agente 4.

---

## Prompt-molde (os dois juízes usam a mesma abertura)

> Você é juiz adversarial de PESQUISA, não de texto. Seu objetivo é **achar o
> buraco**, não aprovar. State file: `<caminho>`. Tipo: `<city|hospital|tr|pillar>`.
> Saída do `checkpoint_suficiencia.py` em anexo — não repita o que ela já mediu.
>
> Sua lente é **<A: suficiência e verdade | B: originalidade e valor>**. Percorra
> os pontos da sua lente, um a um, e para cada um: veredito (🟢/🟡/🔴), a
> **evidência citada do state file** (linha ou trecho) e a correção em uma frase.
> Feche com as suas 2 notas da rubrica e o veredito: LIBERA / REFINA / PARA.
>
> Proibido: elogiar, resumir a pesquisa, sugerir estrutura de artigo, opinar
> sobre redação. Se não houver buraco na sua lente, diga isso em uma linha — mas
> só depois de ter percorrido todos os pontos.

---

## Por que dois juízes e não três

No fim da linha são três porque o objeto é grande (artigo inteiro, cinco
dimensões) e o custo do erro é máximo — já é a última chance. Na pesquisa, o
objeto é menor e **estruturado**: a trava mecânica já cobre o que é contável, e
sobram duas perguntas de julgamento — *dá para escrever?* e *merece existir?*.
Um terceiro juiz aqui repetiria lente sem cobrir risco novo, e o custo apareceria
em todo artigo, não só nos difíceis.

> **Honestidade sobre o limite:** julgar pesquisa cedo reduz retrabalho, **não
> garante artigo bom**. Pesquisa excelente ainda pode virar texto ruim — para
> isso continuam existindo o editor-chefe, o painel do Estágio 5 e a varredura
> final. O que este portão elimina é a categoria de erro que os outros três não
> conseguem consertar.
