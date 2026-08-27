# Como Contratar Hapvida — reformulação no layout V7 (versão documental, sem preço)

Arquivo: `como-contratar-hapvida-v7.html`
Arquétipo: **pillar de tema (P1-P9, sem a P3 de preço)** · slug preservado: `/como-contratar-hapvida/`
Data: 27/08/2026

## Decisão editorial: sem tabela e sem preço

A pedido do dono do site, este pillar é **documental**: descreve o rito da contratação, não o
valor. Isso desliga a camada que define a v7 (ordem preço-primeiro) e tem uma consequência
mecânica assumida: **`checkpoint_preco_primeiro.py` reprova este artigo por construção**
(sem shortcode de tabela e sem H2 de preço). Todas as outras camadas da v7/v6 continuam
valendo e aprovadas.

O artigo não exibe nenhum valor: sem shortcode de tabela, sem `[cidade_menorvalor]`, sem
valores de coparticipação. Preço aparece só como **ponteiro** — dois links, na seção de passo
a passo, para o pillar de preços e para o guia de coparticipação.

## Ordem final

Lead GEO → **sumário** → faixa navy de conversão → `[elementor-template]` `id="cotacao-1"` →
selos → P1 quem pode contratar → P2 passo a passo → documentos PF → documentos PJ/MEI →
CTA → P4 declaração de saúde (eixo) → ativação, pagamento e carências → 5 erros →
P9 veredito → FAQ → CTA → conclusão.

## Entregáveis de SEO

- **H1 (título do post):** Como Contratar Plano Hapvida: Documentos, Prazos e Ativação
- **Title SEO (48 car.):** Como Contratar Hapvida: Documentos e Prazo de 48h
- **Meta description (145 car.):** Como contratar Hapvida: documentos de PF, PJ e MEI, declaração de saúde e prazos. Pessoa física ativa em até 48h. Guia completo da DRV Corretora.
- **Keyword principal:** como contratar hapvida (H1, title, URL, meta, 1º parágrafo e 3 H2)
- **Secundárias:** documentos para contratar plano hapvida · como contratar hapvida MEI ·
  declaração de saúde hapvida · plano hapvida empresarial · contratar hapvida online ·
  prazo de ativação do plano hapvida

## Correções de conteúdo (não são mudanças de layout)

1. **Prazos de carência removidos.** A versão anterior afirmava "consultas eletivas e exames
   simples requerem 180 dias". Contradiz o dado canônico do banco (30 dias consultas,
   90 exames simples, 180 exames complexos). Virou bridge + link para o pillar de carências.
2. **"Mensalidades até 40% menores que planos individuais"** saiu: número sem fonte.
3. **Dois links quebrados corrigidos** contra o registro do banco:
   `/plano-nosso-plano-hapvida/` → `/nosso-plano-hapvida/` e
   `/portabilidade-hapvida/` → `/portabilidade-para-hapvida/`.
4. **"5 erros" tinha 4 cards.** O 5º estava escondido dentro da Dica DRV. Virou card.
5. **`<style>` e `<script>` limpos** dos `<br />` que o wpautop havia injetado.
6. **CPT, portabilidade e coparticipação** reduzidos a bridge + link (proibições consultadas
   em `consultar_pillars_proibicoes`).

## Números do artigo

10 H2 · 18 H3 · 14 FAQ · 3.343 palavras · 13 grifos animados · 15 links internos únicos
(nenhum repetido) · 2 links externos (Planalto e ANS) · 3 formulários · 3 menções à DRV.

## Checkpoints

| Trava | Resultado |
|---|---|
| `checkpoint_completude.py … pillar` | ✅ |
| `checkpoint_paragrafos.py` | ✅ nenhum `<p>` acima de 380 car. |
| `checkpoint_ritmo_visual.py` | ✅ nenhuma seção com 4+ `<p>` seguidos |
| `checkpoint_citabilidade.py` | ✅ todas as seções com abertura citável |
| `checkpoint_voz.py --rigor alto` | ✅ zero 🔴, zero 🟡 |
| `checkpoint_onpage.py` | ✅ |
| `checkpoint_doorway_final.py --tipo pillar` | ✅ sobreposição máxima de 0,3% com os pillars irmãos |
| `checkpoint_preco_primeiro.py … pillar` | ❌ **por decisão editorial** — o artigo não tem preço |

## Pendências (precisam de você)

1. **Schema JSON-LD** — execução separada, só sob pedido ("gera o schema").
2. **Registro no banco** (`registrar_atualizacao`, links e âncoras) — não gravado sem sua
   autorização expressa.
3. **Imagem** — nenhuma. O artigo não tem imagem de abertura nem imagem de tabela.
