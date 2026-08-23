# Varredura final anti-doorway — a última chamada antes de publicar [V7.2]

> **Por que existe uma varredura FINAL, se o Agente 13 já audita doorway.**
> O 13 audita **enquanto** o artigo se forma, seção por seção, e olha para o
> texto que tem na mão. Doorway não mora no parágrafo: mora no **conjunto** — e
> o conjunto só existe depois do editor-chefe, do refino dos juízes e das
> correções do portão humano. É exatamente nesse intervalo que o dano entra:
> uma frase "resolvida" que virou genérica, um parágrafo colado de um artigo
> irmão para tapar buraco, uma seção que perdeu a âncora local na reescrita.
> A varredura final é a única checagem que roda **no artigo que vai ser
> publicado**, e não numa versão anterior dele.

**Quem roda:** **Agente 21 — Varredura final anti-doorway.** Modelo **forte 🔒**,
e obrigatoriamente **diferente do modelo do Agente 13** (trava T2 de
`references/modelos-agentes.md`): quem auditou doorway durante a produção não
pode ser o mesmo ponto de vista que assina a liberação.

**Quando roda:** depois do portão humano, **antes** do Agente 17 (schema) e do
Agente 18 (registro no banco). Reprovou, não publica — nota de juiz não compra
seção sem âncora.

---

## Parte 1 — A trava mecânica

```bash
python -X utf8 C:\Users\netop\.claude\skills\hapvida-article-builder-v7\checkpoint_doorway_final.py <artigo.html> --cidade "Piracicaba" --ancoras <ancoras.txt> --outros <irmao1.html> <irmao2.html> --tipo city
```

O arquivo `--ancoras` tem **uma âncora local por linha** — bairros, unidades,
hospitais, avenidas, entidades da praça. Sai pronto da seção de rede do state
file. **Em artigo de city, rodar sem ele é rodar cego pela metade:** o script
ainda acha entidade por padrão textual ("Hospital X", "bairro Y"), mas perde o
que é local sem marcador.

**Em artigo PILLAR o eixo de substituição não é a praça — é o produto.** Passe o
nome do produto em `--cidade` (`--cidade "Nosso Plano"`) para que D1 e D2 valham
como bloqueio. Sem isso, o script roda os dois como **aviso**: reprovar um artigo
nacional por falta de âncora geográfica seria falso positivo, e falso positivo
ensina o time a ignorar a trava.

O `--outros` recebe os **artigos irmãos** do mesmo cluster (as cidades vizinhas,
os outros hospitais, os spokes do mesmo pillar). Sem eles, o D4 não roda e o
script avisa — comparação com irmão é onde a repetição real aparece.

### As cinco medidas

| # | Mede | 🟡 | 🔴 |
|---|---|---|---|
| **D1** | % do texto visível em parágrafos **sem nenhuma âncora local** (teste de substituição mecanizado) | ≥ 30% | ≥ 45% |
| **D2** | seção/H2 inteira sem uma única âncora local | — | qualquer uma |
| **D3** | clichê de operadora e clichê regulatório (verticalização, custo competitivo, "como qualquer plano regulado pela ANS"…) | 1-5 inline | clichê ocupando parágrafo inteiro, ou > 5 ocorrências |
| **D4** | sobreposição de shingles de 8 palavras com cada artigo irmão | ≥ 8% | ≥ 15%, ou trecho literal ≥ 40 palavras |
| **D5** | title e meta description citam a praça (regra da v5) | ausentes | servem para qualquer praça |

**Por que shingle de 8 palavras e não "parece parecido":** oito palavras
seguidas idênticas não acontecem por acaso em texto original. É a diferença
entre *"os dois artigos falam de carência"* (legítimo) e *"os dois artigos têm o
mesmo parágrafo sobre carência"* (doorway). O script ignora o nome da cidade
antes de comparar — trocar "Piracicaba" por "Sorocaba" não engana a medida.

---

## Parte 2 — A consulta ao banco (o script não faz, o Agente 21 faz)

A trava mede o **texto**. O banco sabe do **site**. As duas metades juntas é que
fecham o veredito:

1. `consultar_overlaps_doorway` — overlaps de risco alto e médio já catalogados.
2. `consultar_cluster_completo` — artigos do cluster, FAQs já usadas, overlaps.
3. `consultar_faqs_catalogo` — **cada FAQ do artigo** contra o catálogo: pergunta
   repetida com resposta parecida é doorway de FAQ, o mais comum e o menos visto.
4. `consultar_pillars_proibicoes` — o que cada pillar já contém e este artigo
   não pode reproduzir (bridge de 1-2 frases + link, nunca a seção inteira).
5. `consultar_saturacao_destinos` — se o artigo empurra link para um destino já
   saturado, a âncora vira ruído.
6. **Opcional, recomendado quando há pillar + spoke na mesma praça:**
   `serp_local` na keyword-alvo (skill `dataforseo-tabelaplanos`) — mais de uma
   URL sua na mesma SERP é canibalização, que é o doorway visto de fora.

---

## Parte 3 — O que fazer com cada achado

| Achado | Correção certa | Correção errada (não faça) |
|---|---|---|
| Parágrafo sem âncora (D1) | reancorar no dado local que a Fase 0 já tem, ou **cortar** | trocar palavras para "soar" local |
| Seção inteira sem âncora (D2) | devolver ao redator da seção com o dado local na mão | espalhar o nome da cidade pelo texto — âncora é **fato** local, não menção |
| Clichê (D3) | apagar; se sustentava a seção, a seção estava vazia | reescrever o clichê com sinônimos |
| Sobreposição com irmão (D4) | decidir **de quem é o território** e transformar o lado perdedor em bridge + link | reescrever os dois para ficarem "diferentes o suficiente" |
| Title/meta genéricos (D5) | reescrever a partir do **ganho de informação do CI-2**, não de um diferencial genérico | acrescentar o nome da cidade no fim |

> **A regra que evita a correção cosmética:** âncora local é **fato que só vale
> naquela praça** — uma unidade, um bairro, um deslocamento, uma comparação com
> a cidade vizinha, um preço com contexto local. Repetir o nome da cidade não
> ancora nada; é o mesmo doorway com etiqueta nova, e o D1 continua reprovando
> porque a medida olha âncora, não menção. (O script vê o nome da cidade como
> âncora — por isso o **julgamento do Agente 21 vem depois do script**, nunca no
> lugar dele: se o parágrafo só passou porque cita a cidade duas vezes, o
> agente reprova mesmo com o script aprovando.)

---

## Parte 4 — Saída do Agente 21

```markdown
# VARREDURA FINAL ANTI-DOORWAY — [cidade/artigo]
Veredito: LIBERADO / BLOQUEADO

## Trava mecânica
[colar a saída do checkpoint_doorway_final.py — inteira, não resumida]

## Banco
- overlaps de risco alto/médio: [...]
- FAQ repetida do catálogo: [...]
- pillar reproduzido: [...]
- saturação de destino: [...]

## Achados que bloqueiam
- [achado] → [correção] → [agente responsável]

## Achados que não bloqueiam (registrar como pendência)
- [...]
```

Bloqueado → volta ao agente da função (D1/D2 → redator do bloco; D3 → Agente 13;
D4 → Agente 5, que decide território; D5 → CI-2 + editor-chefe) e **roda de
novo**. Liberado → só então schema (17) e registro no banco (18).

> **Limite honesto desta varredura:** ela pega repetição, ausência de âncora e
> clichê catalogado. Ela **não** pega texto original, bem ancorado e mesmo assim
> inútil — artigo que responde uma pergunta que ninguém faz. Contra isso, o que
> vale é o CI-2 e o painel de juízes, lá atrás. Doorway é um teste de
> originalidade, não de utilidade.
