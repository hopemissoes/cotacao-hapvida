# BRIEFING COMUM — todos os redatores do artigo "Como Contratar Hapvida"

Skill: hapvida-article-builder-v7 · arquétipo PILLAR de tema (P1-P9) · ordem preço-primeiro v7.1
URL (mantida, sem 301): https://tabelaplanos.com.br/como-contratar-hapvida/
Site: tabelaplanos.com.br — DRV Corretora, especialista Hapvida há mais de 10 anos.

## ARQUIVOS QUE VOCÊ DEVE LER ANTES DE ESCREVER (obrigatório)
1. `PESQUISA_como-contratar-hapvida_COMPLETO.md` (mesma pasta) — o state file APROVADO da FASE 0. **Se um dado não está lá, você NÃO escreve.**
2. `artigo-atual-limpo.html` (mesma pasta) — o artigo publicado hoje. Você REAPROVEITA o conteúdo dele; nada é jogado fora.
3. `/root/.claude/skills/synced/hapvida-article-builder-v7/references/components.md` — templates HTML exatos.
4. `/root/.claude/skills/synced/hapvida-article-builder-v7/references/voz-humana.md` — os tiques a evitar.

## FIO CONDUTOR (a voz e o ângulo — vale do 1º ao último parágrafo)
> **A porta pela qual você entra decide o preço. Juntar documento é a parte fácil; escolher a modalidade errada é o que custa caro — e é a única etapa que não dá para desfazer sem cumprir carência de novo.**

Tom: consultivo, direto, adulto. Número antes de adjetivo. Frases de tamanhos diferentes.
O artigo NÃO é um checklist burocrático — é a explicação de uma decisão que envolve dinheiro.

## REGRAS DURAS (violar = bloco devolvido)

### Fato
- **Jamais inventar.** Todo número, prazo, nome de produto ou regra vem do state file ou do artigo atual. Faltou? Não escreve.
- **Zero tag `[VERIFICAR]` no HTML.** Se um dado é incerto: omita ou suavize. Nunca apague a tag mantendo a afirmação.
- **Preço só por shortcode.** Nunca "R$ 120,00" escrito à mão, em lugar nenhum.
- Dados canônicos permitidos (Supabase): 86 hospitais próprios · 168 credenciados · 15,9 milhões de beneficiários · 80 PAs 24h · 16 estados · 11 programas Qualivida. Use com parcimônia — este é pillar de processo, não de rede.
- Legislação permitida: Lei 9.656/98 (art. 11) · RN 432/2017 da ANS (CNPJ ativo há 6 meses para MEI).

### Datas
- **PROIBIDO escrever "2026" ou "2025" literalmente.** Use `[ano_atual]` e `[mes_atual]`.
- Exceção: legislação com ano no nome (Lei 9.656/98, RN 432/2017) — mantém.

### Anti-doorway POR PRODUTO (é pillar, não cidade)
Teste: troque "contratar Hapvida" por "contratar Plano Mix". Se a frase continua válida, é genérica → reescreva ou corte.
**Conteúdo que NÃO pode ser desenvolvido aqui** (é de outro pillar — no máximo 1-2 frases + link):
- Mecânica da coparticipação, tabela Total × Parcial, simulador de economia
- Tabela de prazos de carência, os cards 24h/30d/180d/300d, CPT explicada em detalhe
- Tabela de preços por FAIXA ETÁRIA (10 faixas) — pertence a /tabela-de-preco-hapvida/ e /plano-individual-hapvida/
- Reajuste ANS, histórico de reajustes, "os 5 fatores que definem o preço"
- Lista dos 11 programas Qualivida, direitos do beneficiário, portal RH
- Detalhe de cidade (rede, endereço, hospital por bairro) — pillar cita âmbito nacional e LINKA

### Voz humana (checkpoint_voz.py roda com --rigor alto)
PROIBIDO:
- Gerúndio de arremate: "…12 hospitais, **garantindo** mais segurança". Corte tudo depois da vírgula.
- Tríade de adjetivos: "prático, rápido e eficiente" → troque por um número.
- Moldes: "não apenas X, mas também Y" · "seja você A, B ou C" · "quando o assunto é" · "neste artigo você vai" · "continue a leitura" · "é importante ressaltar que" · "vale lembrar que".
- Marketing vazio: "excelente custo-benefício" · "tranquilidade para você e sua família" · "cobertura total" · "atendimento de qualidade" · "solução completa".
- Frases todas do mesmo tamanho.
Toda vez que couber um adjetivo de vitrine, troque por dado.

### Layout (WordPress + Elementor)
- HTML **compacto**: zero linha em branco entre tags, tudo grudado. O `wpautop` injeta `<p>&nbsp;</p>` em qualquer respiro.
- CSS 100% inline, copiado dos templates de `components.md`. Não invente estilo.
- **ZERO emoji e zero dingbat** em qualquer lugar (o template de Hero Card em components.md tem um `📍` — **remova**). Badges só com letra.
- Todo `<p>` de corpo: `style="text-align:justify!important;font-size:18px;line-height:1.8;color:#4a5568;margin-bottom:18px;"`
- **Parágrafo: máximo 380 caracteres.** Passou disso, quebre em dois. É medido por script.
- **Ritmo: no máximo 3 `<p>` seguidos** sem quebra visual (H3, box, grid de cards, bullet list curta, callout, tabela, steps, timeline). É medido por script.
- Cabeçalho de seção padrão (H2 + subtítulo + barra laranja) em toda seção, exceto FAQ (que tem o seu próprio) e o sumário.
- Bullet list: máximo 1 `<ul>` por seção, 3-5 itens curtos, no padrão inline de bullets da skill (marcador `▸` laranja).

### Grifo animado
Use o `<span class="destaque-laranja-suave" ...>` exatamente como no template, sempre com `background-size:100% 100%` (NUNCA 0%). Grife trechos que carregam FATO, não adjetivo.

### Links
- Âncora descritiva, nunca "clique aqui" / "saiba mais".
- **Cada URL no máximo 1× no artigo inteiro.** Mínimo ~150 palavras entre dois links.
- Links externos: `target="_blank" rel="nofollow noopener"`.
- Nunca linkar concorrente (outra corretora ou comparador).

### Menções à DRV
Máximo 3 no artigo INTEIRO. Bloco A tem 1 (lead). Bloco B tem 1 (Dica DRV). Bloco C tem 1 (fechamento). Não estoure.

## MAPA DE FUNDOS (não invente cor)
| Seção | Fundo |
|---|---|
| Lead | `background:#fff;` + `border-bottom:1px solid #e2e8f0;` |
| P3↑a Preço (id="precos") | `#fff` |
| Sumário | `linear-gradient(135deg,#fafbfc 0%,#f0f4f8 100%)` + `border:1px solid #e2e8f0` |
| P3↑b | `#fff` |
| P1 | `#f8f9fa` |
| P2 | `#fff8f3` |
| P4 (eixo) | `#fff` |
| P5 | `#f8f9fa` |
| P6 | `#fff8f3` |
| P7 | `#fff` |
| P8 | `#f8f9fa` |
| FAQ | `#fff` + `border:1px solid #e2e8f0` |
| P9 / Conclusão | `linear-gradient(135deg,#f8fafc 0%,#f1f5f9 100%)` + `border-top:1px solid #e2e8f0` |

Padrão da tag `<section>`: `style="background:[COR];padding:20px 10px;border-radius:20px;margin-bottom:4px;" id="[ID]"` (o lead usa `border-bottom` no lugar de `border-radius`).
Dentro de cada `<section>`, envolver o conteúdo em `<div style="max-width:820px;margin:0 auto;">`.

## ORDEM FINAL DO ARTIGO (v7.1 — não altere)
1. `<figure>` de abertura
2. Lead GEO
3. **P3↑a** — H2 "Quanto Custa Contratar o Plano Hapvida" (`id="precos"`) + contexto + **TABELA**
4. **SUMÁRIO** (colado na tabela)
5. **P3↑b** — faixa navy + `[elementor-template]` `id="cotacao-1"` + selos + leitura da tabela + H3 copart em valor
6. **P1** (`id="modalidades"`) · 7. **P2** (`id="portas-de-entrada"`) · 8. **P4 eixo** (`id="qual-porta"`)
9. **P5** (`id="documentos-pf"`) · 10. **P6** (`id="documentos-pj-mei"`) · 11. **P7** (`id="passo-a-passo"`)
12. CTA intermediário · 13. **P8** (`id="declaracao-de-saude"`) · 14. **FAQ** (`id="faq"`)
15. CTA final · 16. **P9 / Conclusão** (`id="conclusao"`) · 17. `<style>` · 18. `<script>` · 19. `<script>` [V5]

## O QUE VOCÊ ENTREGA
Apenas o HTML do SEU bloco — sem `<article>` de abertura/fechamento (o editor-chefe costura), sem comentários de explicação fora do HTML, sem markdown ao redor. Grave num arquivo e devolva o caminho + um relatório curto do que fez e das decisões que tomou.
