# Auditoria — "plano de saúde barato" (tabelaplanos.com.br, post 34416)

Data: 28/08/2026. Fontes de verificação: fila do cotador no Supabase
(`cotador_fila`), dados canônicos (`consultar_dados_canonicos`), conteúdo
publicado via WordPress REST, DataForSeo (SERP + keyword), IBGE PNS 2019, ANS.

## Confirmado como correto (não mexer)
- Fortaleza: empresarial vence 10/10 faixas. Recife: 3/10, faixas 19–33. ✓
- Multiplicadores de faixa etária Hapvida 5,873× e Amil 5,951×. ✓
- 86 hospitais próprios, 80 PAs 24h, 16 estados. ✓ (dados canônicos)
- IBGE PNS 2019: 2,2% (até ¼ SM) e 86,8% (>5 SM). ✓
- "8 cotações próprias": batem 4 em Fortaleza + 4 em Recife. ✓

## Corrigido
| # | Problema | Correção |
|---|---|---|
| A1 | `<style>` com 48 `<br />`/`<p>` do wpautop — CSS morto | bloco em linha única |
| A2 | `<script>` idem — JS inteiro morto (erro de sintaxe) | bloco em linha única; valida em `node --check` |
| A3 | Badge "menor" nas 6 capitais ao mesmo tempo (escrito à mão) | só em Recife, o menor real |
| B1 | Herói anunciava Belém R$ 161,35; menor da tabela é Recife R$ 131,32 | herói passa a Recife |
| B2 | Lead vendia "2,38×" apurado fora de base uniforme | lead reescrito sem o número falso |
| B3 | Quadro de Recife trazia multiplicador da Unimed de Fortaleza (5,999) | 5,983× (Recife) |
| D3 | SulAmérica 5,9995 (Fortaleza) no quadro de Recife | 5,9997× |
| B4 | "três repetiram o multiplicador exato" — falso p/ SulAmérica | redação precisa |
| B5 | FAQ 1: "a ordem não se repetiu" — **a ordem se repete nas duas praças** | reescrita |
| B6 | Contradição: individual só no N/NE × NotreLife individual em SP/RJ | reconciliado + link |
| B7 | Selo com ANS 359017 (= Notre Dame Intermédica, não Hapvida) e "DRV 10+ anos" | selo trocado; DRV 11 anos + Safira |
| B8 | "53,1 mi em maio/2026" | junho/2026 (53.145.666) |
| B9/B10 | Dados próprios não verificáveis ("7 em cada 10", limiar de 10 exames) | removidos a pedido do dono |
| C1–C7 | Ranking 1,84/2,07/2,38 misturava Hapvida **individual ambulatorial** com concorrentes **empresarial com internação** | refeito em base uniforme: 1,00 / 1,64 / 1,84 / 2,11; segmentação real declarada em cada linha |
| E1 | Caixa dizia que Fortaleza não tinha base uniforme (tinha) | publica Fortaleza: 1,00 / 1,53 / 1,89 / 2,00 |

## Pendente de decisão do dono
1. **Meta title e description estão com shortcode cru no ar** — o Rank Math não
   executa shortcode. Google vê `Plano de Saúde Barato [ano_atual]: PROMOÇÃO por
   [belem_ind_ambulatorialtotal_0]`. Precisa de texto fixo.
2. **Geografia × SERP.** A SERP nacional de "plano de saúde barato" (2.400/mês,
   intenção comercial, AI Overview em #1) é resolvida com SP, RJ, BH, Brasília,
   Campinas e Porto Alegre. O artigo cobre seis capitais do N/NE. Barreira de
   link é baixa (~7 domínios referentes na média dos que rankeiam).
3. **Preço de entrada divergente no próprio site**: as páginas de cidade anunciam
   Natal R$ 91,37 e Uberlândia R$ 91,48 — abaixo das seis capitais desta página,
   que usam outra coluna (individual ambulatorial). Vale unificar o discurso de
   "piso" ou explicitar a diferença de produto.
