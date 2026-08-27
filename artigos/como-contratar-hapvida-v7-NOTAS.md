# Como Contratar Hapvida — reformulação no layout V7.1

Arquivo: `como-contratar-hapvida-v7.html`
Arquétipo: **pillar de tema (P1-P9)** · slug preservado: `/como-contratar-hapvida/`
Data: 27/08/2026

## Entregáveis de SEO

- **H1 (título do post):** Como Contratar Plano Hapvida: Documentos, Prazos e Ativação
- **Title SEO (48 car.):** Como Contratar Hapvida: Documentos e Prazo de 48h
- **Meta description (145 car.):** Como contratar Hapvida: documentos de PF, PJ e MEI, declaração de saúde e prazos. Pessoa física ativa em até 48h. Guia completo da DRV Corretora.
- **Keyword principal:** como contratar hapvida (em H1, title, URL, meta, 1º parágrafo e 3 H2)
- **Secundárias (7, com veto de intenção):** documentos para contratar plano hapvida · como contratar hapvida MEI · declaração de saúde hapvida · quanto custa o plano hapvida · plano hapvida empresarial · contratar hapvida online · prazo de ativação do plano hapvida

## Ordem V7.1 aplicada

Lead GEO → **P3↑a preço + tabela PF** (`id="precos"`) → **sumário colado** → **P3↑b**
(faixa navy + `[elementor-template]` `id="cotacao-1"` + selos + tabela PJ + pagamento +
coparticipação) → P1 quem pode → P2 passo a passo → docs PF → docs PJ/MEI → CTA →
P4 declaração de saúde (eixo) → ativação → 5 erros → P9 veredito → FAQ → CTA → conclusão.

## Correções de conteúdo (não são mudanças de layout)

1. **Prazos de carência removidos.** A versão anterior afirmava "consultas eletivas e exames
   simples requerem 180 dias". Contradiz o dado canônico do banco (30 dias consultas,
   90 exames simples, 180 exames complexos). Virou bridge + link para o pillar de carências,
   que é o dono desse conteúdo.
2. **"Mensalidades até 40% menores que planos individuais"** saiu: número sem fonte.
   O comparativo agora é feito pelas duas tabelas de shortcode, lado a lado.
3. **Dois links quebrados corrigidos** contra o registro do banco:
   `/plano-nosso-plano-hapvida/` → `/nosso-plano-hapvida/` e
   `/portabilidade-hapvida/` → `/portabilidade-para-hapvida/`.
4. **"5 erros" tinha 4 cards.** O 5º estava escondido dentro da Dica DRV. Virou card.
5. **`<style>` e `<script>` limpos** dos `<br />` que o wpautop havia injetado.
6. **CPT, portabilidade e coparticipação** reduzidos a bridge + link (proibições dos pillars
   consultadas em `consultar_pillars_proibicoes`).

## Checkpoints

| Trava | Resultado |
|---|---|
| `checkpoint_preco_primeiro.py … pillar` | ✅ 0 avisos (1.311 car. antes da tabela / 129 entre tabela e sumário) |
| `checkpoint_completude.py … pillar` | ✅ 11 H2 · 20 H3 · 14 FAQ · 3.495 palavras |
| `checkpoint_paragrafos.py` | ✅ 59 `<p>`, nenhum acima de 380 car. |
| `checkpoint_ritmo_visual.py` | ✅ 12 seções, nenhuma com 4+ `<p>` seguidos |
| `checkpoint_citabilidade.py` | ✅ 11 de 11 seções com abertura citável |
| `checkpoint_voz.py --rigor alto` | ✅ zero 🔴, zero 🟡 |
| `checkpoint_onpage.py` | ✅ principal e secundárias posicionadas |
| `checkpoint_doorway_final.py --tipo pillar` | ✅ sobreposição máxima de 0,3% com os pillars irmãos |

## Pendências (precisam de você)

1. **Imagem de abertura** — o `<figure>` está comentado no topo do arquivo. Cole a URL e
   descomente, ou apague o comentário.
2. **Imagem da tabela de preço (camada v6)** — não foi gerada: `gerar_imagem_artigo.py` exige
   os 10 valores reais por faixa, que só o shortcode renderiza no servidor.
3. **Schema JSON-LD** — execução separada, só sob pedido ("gera o schema").
4. **Registro no banco** (`registrar_atualizacao`, links e âncoras) — não gravado sem sua
   autorização expressa.
5. **Decisão sua:** a v7 obriga tabela de preço como primeiro conteúdo. Num pillar de processo
   isso foi resolvido com as tabelas de referência de Belo Horizonte (mesma convenção do pillar
   de preços) + link. Se preferir o pillar sem tabela, a seção sai e o artigo deixa de passar no
   `checkpoint_preco_primeiro.py`.
