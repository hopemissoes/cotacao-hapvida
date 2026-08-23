# Shortcode Reference

All prices (monthly fees and copay values) are dynamic and controlled via shortcodes.
**NEVER insert fixed price values in the article.**
**NEVER mention the pricing table is for "plano empresarial"** — say only "plano Hapvida".

---

## Price Shortcodes (monthly fee)

### Shortcodes utilitários (sempre disponíveis)

| Shortcode | Output | Use |
|-----------|--------|-----|
| `[cidade_menorvalor]` | Menor valor empresarial copart total (chamariz) | CTA, lead, FAQ, conclusion — chamariz "a partir de R$ X" |
| `[cidade_menortabela]` | Tabela completa de preços por faixa etária (HTML) | Quando precisa renderizar tabela inteira |

`cidade` = city prefix (e.g., `belem`, `contagem`, `fortaleza`, `belo-horizonte`). Use the correct prefix
as registered in the WordPress pricing plugin.

### Shortcodes de tabela completa por modalidade (existem para todas as cidades)

Renderizam a tabela inteira em HTML com as 10 faixas etárias. Pattern:

```
[cidade_emp_ambulatorialtotal]   → tabela empresarial coparticipação total
[cidade_ind_ambulatorialtotal]   → tabela individual coparticipação total
```

Exemplos confirmados:

```
[belo-horizonte_emp_ambulatorialtotal]
[belo-horizonte_ind_ambulatorialtotal]
[fortaleza_emp_ambulatorialtotal]
[fortaleza_ind_ambulatorialtotal]
[recife_emp_ambulatorialtotal]
[recife_ind_ambulatorialtotal]
[sao-paulo_emp_ambulatorialtotal]
[sao-paulo_ind_ambulatorialtotal]
```

**Onde usar:** artigos S1-S7 (city pillar) em seção S2 (Preços). Cobre todas as cidades onde a Hapvida opera.

> **[V7.1] ONDE, exatamente:** a S2 é a **primeira seção do artigo** — o shortcode de tabela entra logo depois do Lead GEO e **antes do sumário**, com o **sumário colado nele** (nada de formulário, faixa navy ou imagem no meio). Ver `references/preco-primeiro.md`. Em pillar, o mesmo vale para a P3↑.

**Onde NÃO usar:** artigos TR (Tabela Regional). O artigo TR usa a tabela como **imagem** para ranquear no image pack — duplicar como tabela HTML é redundante e prejudica o objetivo da imagem. Em vez disso, usar shortcodes de valor pontual (ver abaixo).

### Shortcodes de valor pontual por faixa etária (uso em artigos TR)

Para citar valores específicos no texto (ex: "começa em R$ X e progride até R$ Y"), usar o pattern com sufixo de faixa etária:

```
[cidade_emp_ambulatorialtotal_0]   → faixa 0-18 empresarial
[cidade_emp_ambulatorialtotal_9]   → faixa 59+ empresarial
[cidade_ind_ambulatorialtotal_0]   → faixa 0-18 individual
[cidade_ind_ambulatorialtotal_9]   → faixa 59+ individual
```

Onde `faixaetaria`:
- `0` = 0 a 18 anos
- `1` = 19 a 23 anos
- `2` = 24 a 28 anos
- `3` = 29 a 33 anos
- `4` = 34 a 38 anos
- `5` = 39 a 43 anos
- `6` = 44 a 48 anos
- `7` = 49 a 53 anos
- `8` = 54 a 58 anos
- `9` = 59 anos ou mais

**Onde usar:** artigos TR (Tabela Regional). Permite citar valores extremos da imagem sem hardcode, garantindo que se a tabela for atualizada, o texto reflete automaticamente — e a discrepância com a imagem antiga vira visível, forçando regeneração.

**Confirmar com admin:** verificar se o plugin de shortcodes do site aceita o sufixo `_faixaetaria` (0-9) ou se cada combinação `cidade × modalidade × faixa` precisa ser cadastrada como shortcode separado.

---

## Date Shortcodes (automatic update)

WordPress shortcodes that update automatically. Registered via snippet PHP no WPCode.

| Shortcode | Output | Use |
|-----------|--------|-----|
| `[ano_atual]` | Ano vigente (ex: 2026, 2027…) | Títulos H3 com ano, meta description, notas de rodapé, qualquer menção ao ano corrente |
| `[mes_atual]` | Mês vigente por extenso em PT-BR (ex: Janeiro, Fevereiro…) | Notas de atualização ("Dados atualizados em [mes_atual] de [ano_atual]") |

**Regras de uso:**
1. **NUNCA** escrever ano fixo (2025, 2026, 2027) em conteúdo evergreen — usar `[ano_atual]`
2. **NUNCA** escrever mês fixo em notas de atualização — usar `[mes_atual]`
3. **Exceção:** Datas históricas factuais (ex: "fundado em 1979", "inaugurado em jan/2025") permanecem fixas — são fatos, não referências ao ano corrente
4. **Exceção:** Legislação com ano fixo (ex: "Lei 9.656/98", "RN 438/2018") permanece fixa
5. Shortcodes funcionam dentro de blocos HTML Personalizado no WordPress — NÃO funcionam dentro de tags `<h2>` no editor Gutenberg nativo (apenas em Custom HTML, que é o nosso caso)
6. Para título SEO (meta title): usar variável do plugin SEO em vez de shortcode (`%currentyear%` no RankMath, `%%currentyear%%` no Yoast)

**Onde usar `[ano_atual]` nos artigos:**
- H3 com ano: `Tabela de Preços Hapvida [Cidade] [ano_atual]`
- Nota rodapé: `Dados atualizados em [mes_atual] de [ano_atual]`
- Meta description: `Hapvida [Cidade] [ano_atual]: ...`
- FAQ com ano: `Quanto custa o plano Hapvida em [Cidade] em [ano_atual]?`

**Onde NÃO usar (manter ano fixo):**
- Datas históricas: "fundado em 1979", "inaugurado jan/2025"
- Legislação: "Lei 9.656/98", "RN 63/2003"
- Dados de pesquisa com data específica: "segundo censo IBGE 2022"

---

## Copay Shortcodes

Two groups depending on the city. Use instead of ANY fixed copay value.

### Group 1 — São Paulo and Belo Horizonte

| Shortcode | Procedure |
|-----------|----------|
| `[sp_bh_consultas_eletivas]` | Elective consultations |
| `[sp_bh_consultas_urgencia]` | Urgent/emergency consultations |
| `[sp_bh_exames_simples]` | Simple exams (blood, urine, etc.) |
| `[sp_bh_exames_complexos]` | Complex exams (MRI, CT scan) |
| `[sp_bh_terapias_neurologicas]` | Neurological therapies (speech, neurological physio) |
| `[sp_bh_demais_terapias]` | Other therapies (conventional physio, psychology, nutrition) |

### Group 2 — All other cities

| Shortcode | Procedure |
|-----------|----------|
| `[demais_capitais_consultas_eletivas]` | Elective consultations |
| `[demais_capitais_consultas_urgencia]` | Urgent/emergency consultations |
| `[demais_capitais_exames_simples]` | Simple exams |
| `[demais_capitais_exames_complexos]` | Complex exams |
| `[demais_capitais_terapias_neurologicas]` | Neurological therapies |
| `[demais_capitais_demais_terapias]` | Other therapies |

---

## Form Shortcode

| Shortcode | Use | Quantity |
|-----------|-----|---------|
| `[elementor-template id="11215"]` | Quotation form | **3×** (post-table + CTA mid + CTA final) |

### Placement Rules:
1. **Post-sumário [V7.1]** — a ordem é tabela → **sumário** → formulário. O `id="cotacao-1"` abre a segunda metade da seção de preço (S2↑b), colado na faixa navy de conversão. É o 1º formulário do artigo e o mais alto da página — mas **nunca** entre a tabela e o sumário
2. **CTA intermediário** — between S6 (Cenário de Saúde) and S7 (Como Contratar), in a bare `<div style="margin-bottom:4px;">`
3. **CTA final** — between FAQ and Conclusão, in a bare `<div style="margin-bottom:4px;">`

No section wrapper, no H2, no subtitle — the Elementor template renders its own visual.

---

## Shortcode Pattern Reference

The general shortcode pattern for the pricing plugin is:
```
[cidade_ind/emp_modalidade_acomodacaotipo_faixaetaria]
```

Where:
- `cidade` = city prefix (e.g., `belo-horizonte`, `sao-paulo`, `belem`, `fortaleza`)
- `ind/emp` = individual or empresarial
- `modalidade` = `ambulatorial`, `hospitalar`, etc. (most common in articles: `ambulatorial`)
- `acomodacao` = `enfermaria`, `apartamento` (concatenated with `tipo` without separator)
- `tipo` = `total`, `parcial` (copay type — `total` is the most cited in articles)
- `faixaetaria` = `0` (0-18) through `9` (59+) — OPTIONAL; omitting renders full table
- `_sd` suffix = removes buttons/CTAs from displayed tables

**Common usage patterns:**

| Pattern | Output | Used in |
|---------|--------|---------|
| `[cidade_menorvalor]` | Single value (starting price) | All article types — chamariz |
| `[cidade_menortabela]` | Full HTML table | S1-S7 (city articles) |
| `[cidade_emp_ambulatorialtotal]` | Full HTML table (empresarial copart total) | S1-S7 |
| `[cidade_ind_ambulatorialtotal]` | Full HTML table (individual copart total) | S1-S7 |
| `[cidade_emp_ambulatorialtotal_0]` | Single value (faixa 0-18 empresarial) | **TR articles** — leitura da imagem |
| `[cidade_emp_ambulatorialtotal_9]` | Single value (faixa 59+ empresarial) | **TR articles** |
| `[cidade_ind_ambulatorialtotal_0]` | Single value (faixa 0-18 individual) | **TR articles** |
| `[cidade_ind_ambulatorialtotal_9]` | Single value (faixa 59+ individual) | **TR articles** |

**Important rule for TR articles:** the article hosts the price table as an **image** for image-pack ranking. Do NOT use full-table shortcodes (`[cidade_emp_ambulatorialtotal]`) inside the TR article body — they would duplicate the image as HTML, which is redundant and prejudices the image-first strategy. Use only point-value shortcodes (with `_faixaetaria` suffix) when citing values in surrounding text.
