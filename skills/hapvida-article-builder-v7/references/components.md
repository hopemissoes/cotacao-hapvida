# Component HTML Templates

Copy-paste reference for every visual component used in the articles.
All HTML must be compact (single line, no breaks between tags) to survive wpautop.

---

## Imagem de Abertura do Artigo (Opening / Hero Image) — OBRIGATÓRIA

**É o PRIMEIRO elemento dentro de `<article>`, ANTES da Introdução / Lead GEO.** Toda City (S1-S7) e Hospital (HS1-HS4) abre com esta `<figure>`. (Artigos TR já têm a própria estratégia image-first — ver `references/tabela-regional-subpages.md` — e não usam esta.)

**O que o redator personaliza por artigo** (os estilos inline NÃO mudam):
- `title` — frase descritiva do tema do artigo (com a keyword-alvo).
- `src` — **a URL da imagem é fornecida pelo usuário**. Enquanto não vier, deixar `[URL_DA_IMAGEM]` como placeholder e pedir ao usuário. Nunca inventar URL.
- `alt` — descrição detalhada do que a imagem mostra + o fato-âncora do artigo (com a keyword); é texto para acessibilidade e SEO de imagem, não legenda.
- `figcaption` — legenda curta que reforça o ângulo único do artigo (o "ganho de informação" da Fase 0).
- `width`/`height` — devem refletir as dimensões reais do arquivo enviado (o exemplo é 1080×1080, imagem quadrada; ajustar se a imagem for outra proporção).

```html
<figure style="margin: 0 0 24px 0; padding: 0;"><img style="max-width: 70%; height: auto; border-radius: 12px; border: 1px solid #e2e8f0; display: block; margin: 0 auto;" title="[TÍTULO DESCRITIVO — tema do artigo, com a keyword]" src="[URL_DA_IMAGEM]" alt="[ALT detalhado — o que a imagem mostra + fato-âncora do artigo, com a keyword]" width="1080" height="1080" />
<figcaption style="text-align: center; font-size: 14px; color: #718096; margin-top: 10px; font-style: italic;">[Legenda curta que reforça o ângulo único do artigo.]</figcaption></figure>
```

**Exemplo já preenchido** (tema "plano de saúde para recém-nascido"):

```html
<figure style="margin: 0 0 24px 0; padding: 0;"><img style="max-width: 70%; height: auto; border-radius: 12px; border: 1px solid #e2e8f0; display: block; margin: 0 auto;" title="Plano de saúde para recém-nascido — cobertura nos primeiros 30 dias e inclusão do bebê sem carência" src="https://tabelaplanos.com.br/wp-content/uploads/2026/06/plano-de-saude-para-recem-nascido.jpg" alt="Plano de saúde para recém-nascido: pela Lei 9.656/98, o bebê tem cobertura automática pelo plano dos pais nos primeiros 30 dias e pode ser incluído como dependente sem carência" width="1080" height="1080" />
<figcaption style="text-align: center; font-size: 14px; color: #718096; margin-top: 10px; font-style: italic;">Recém-nascido coberto desde o primeiro dia: incluindo o bebê em até 30 dias, num plano com obstetrícia, ele entra sem carência.</figcaption></figure>
```

**Regras:**
- `alt` e `figcaption` são conteúdo único do artigo — entram no teste anti-doorway (não podem servir para qualquer cidade/tema).
- Não repetir literalmente o `alt` no `figcaption` (são funções diferentes: `alt` descreve, `figcaption` comenta o ângulo).
- Manter o HTML compacto e os estilos inline exatamente como acima (sobrevive ao wpautop).

---

## Standard Section Header

Used on all sections except Introdução, CTA, and FAQ.

```html
<h2 style="font-size:clamp(24px,4vw,30px);font-weight:900;color:#1a202c;margin-bottom:8px;">Section Title</h2><p style="text-align:justify!important;font-size:18px;font-weight:500;color:#718096;margin-bottom:12px;">One-line subtitle describing the section.</p><div style="width:60px;height:4px;background:linear-gradient(90deg,#ff6b00,#ff8533);border-radius:2px;margin-bottom:28px;"></div>
```

---

## Sumário / NAV (Table of Contents)

Pure `<div>` structure. NEVER use `<ol>/<li>`. Header ≡ is first `toc-item` inside `toc-list`.
Must include a **CTA item "Faça uma Cotação"** linking to `#cotacao-1`, visually highlighted.

```html
<section style="background:linear-gradient(135deg,#fafbfc 0%,#f0f4f8 100%);padding:20px 10px;border-radius:20px;margin-bottom:4px;border:1px solid #e2e8f0;"><div class="toc-list" style="display:flex!important;flex-direction:column!important;gap:10px!important;padding:0!important;margin:0!important;"><div class="toc-item" style="display:flex!important;align-items:center!important;gap:10px!important;padding:0!important;margin:0!important;"><span style="min-width:28px;height:28px;flex-shrink:0!important;background:#ff6b00;border-radius:8px;display:flex!important;align-items:center!important;justify-content:center!important;color:#fff;font-size:14px;font-weight:700;">≡</span><span style="font-size:17px;font-weight:800;color:#1a202c;">Neste Guia Você Vai Encontrar</span></div><div class="toc-item" style="display:flex!important;align-items:center!important;gap:10px!important;padding:0!important;margin:0!important;"><span class="toc-badge" style="min-width:28px;height:28px;flex-shrink:0!important;background:#ff6b00;border-radius:8px;display:flex!important;align-items:center!important;justify-content:center!important;color:#fff;font-size:13px;font-weight:700;">1</span><a href="#id-secao" style="color:#1a202c;font-weight:600;font-size:15px;text-decoration:none;">Título da Seção</a></div><div class="toc-item" style="display:flex!important;align-items:center!important;gap:10px!important;padding:0!important;margin:0!important;"><span class="toc-badge" style="min-width:28px;height:28px;flex-shrink:0!important;background:#ff6b00;border-radius:8px;display:flex!important;align-items:center!important;justify-content:center!important;color:#fff;font-size:13px;font-weight:700;">2</span><a href="#id-secao-2" style="color:#1a202c;font-weight:600;font-size:15px;text-decoration:none;">Título da Seção 2</a></div><div class="toc-item" style="display:flex!important;align-items:center!important;gap:10px!important;padding:0!important;margin:0!important;"><span class="toc-badge" style="min-width:28px;height:28px;flex-shrink:0!important;background:#ff6b00;border-radius:8px;display:flex!important;align-items:center!important;justify-content:center!important;color:#fff;font-size:13px;font-weight:700;">$</span><a href="#cotacao-1" style="display:inline-block;color:#fff!important;font-weight:800;font-size:15px;text-decoration:none;padding:6px 14px;background:linear-gradient(135deg,#ff6b00,#e85d00);border-radius:6px;box-shadow:0 4px 14px rgba(255,107,0,0.35);">Faça uma Cotação</a></div></div></section>
```

**CTA item rules:**
- Positioned after S2 entry in the sumário (before S3)
- Same left-aligned layout as other `toc-item` entries (badge + text)
- Badge: orange `$` (same style as numbered badges)
- Text: white `#fff` on orange background (gradient `#ff6b00 → #e85d00`, `box-shadow`, `border-radius:6px`)
- Font: `font-size:15px; font-weight:800` (same as other toc links)
- Links to `#cotacao-1` (the ID on the 1st `[elementor-template]` wrapper div)
- **V4.5.0:** Background applied directly on `<a>` — NO `position:absolute`, NO `z-index:-1`, NO inner `<span>` for background. Previous approach caused invisible CTA on some WordPress themes that create stacking contexts.

```html
<div class="toc-item" style="display:flex!important;align-items:center!important;gap:10px!important;padding:0!important;margin:0!important;"><span class="toc-badge" style="min-width:28px;height:28px;flex-shrink:0!important;background:#ff6b00;border-radius:8px;display:flex!important;align-items:center!important;justify-content:center!important;color:#fff;font-size:13px;font-weight:700;">$</span><a href="#cotacao-1" style="display:inline-block;color:#fff!important;font-weight:800;font-size:15px;text-decoration:none;padding:6px 14px;background:linear-gradient(135deg,#ff6b00,#e85d00);border-radius:6px;box-shadow:0 4px 14px rgba(255,107,0,0.35);">Faça uma Cotação</a></div>
```

---

## Info Box — Resumo Rápido (badge "R")

```html
<div style="background:linear-gradient(135deg,#eff6ff 0%,#dbeafe 100%);border:1px solid #bfdbfe;border-radius:12px;padding:24px 28px;margin-bottom:24px;"><div class="box-row" style="display:flex!important;align-items:center!important;gap:10px!important;margin-bottom:12px!important;line-height:1!important;flex-wrap:nowrap!important;"><span style="width:28px!important;height:28px!important;min-width:28px!important;max-width:28px!important;flex-shrink:0!important;background:#2563eb!important;border-radius:8px!important;display:inline-flex!important;align-items:center!important;justify-content:center!important;color:#fff!important;font-size:14px!important;font-weight:800!important;line-height:1!important;font-family:Arial,Helvetica,sans-serif!important;text-align:center!important;box-sizing:border-box!important;padding:0!important;margin:0!important;vertical-align:middle!important;">R</span><span style="font-size:14px;font-weight:700;color:#1e40af;text-transform:uppercase;letter-spacing:1px;line-height:1.2;">Resumo Rápido</span></div><p style="text-align:justify!important;font-size:18px;line-height:1.7;color:#1e40af;margin:0;">Box text here.</p></div>
```

## Info Box — Importante (badge "!")

Same structure as Resumo Rápido but with badge letter `!` and label `Importante`.

## Info Box — Portabilidade (badge "P")

Same structure but with badge letter `P` and label `Portabilidade`.

## Info Box — Dica DRV (NO badge)

```html
<div style="background:linear-gradient(135deg,#eff6ff 0%,#dbeafe 100%);border:1px solid #bfdbfe;border-radius:12px;padding:24px 28px;margin-bottom:24px;"><div class="box-row" style="display:flex!important;align-items:center!important;gap:10px!important;margin-bottom:12px;"><span style="font-size:14px;font-weight:700;color:#1e40af;text-transform:uppercase;letter-spacing:1px;">DICA DRV</span></div><p style="text-align:justify!important;font-size:18px;line-height:1.7;color:#1e40af;margin:0;">Tip text here.</p></div>
```

Note: Dica DRV has NO badge icon — only the text label.

---

## Info Box Anti-Elementor / Anti-Theme Rules (apply to ALL boxes)

1. `flex-shrink:0!important` on badge — prevents compression
2. `display:flex!important` on badge container (`.box-row`)
3. Badge itself uses `<span>` with `display:inline-flex!important` (NOT `<div>` — span survives wpautop better)
4. Badge dimensions locked with `width`, `height`, `min-width` AND `max-width` (all 28px, all `!important`) — prevents theme from squeezing or stretching
5. `line-height:1!important` on badge AND on `.box-row` — prevents inherited theme line-height from offsetting the letter inside the badge (this was causing the "tilted symbol" bug)
6. `font-family:Arial,Helvetica,sans-serif!important` on badge — guarantees consistent letter baseline regardless of theme font
7. `box-sizing:border-box!important` + `padding:0!important` + `margin:0!important` + `vertical-align:middle!important` on badge — neutralizes theme resets
8. Zero blank lines between outer div → `.box-row` → badge → label → `</div>` → `<p>` → `</p>` → `</div>`
9. Compact HTML — everything on same line
10. Anti-wpautop in `<style>`: `.box-row>p{display:contents!important}` + `.box-row>br{display:none!important}`
11. NEVER `display:none` on `<p>` — wpautop wraps badge+label in `<p>`, and `none` hides entire title. Use `display:contents`.

---

## Metric Cards (grid4 example — 3 gray + 1 orange)

```html
<div class="grid4" style="display:flex!important;flex-wrap:wrap!important;gap:12px!important;margin-bottom:24px;"><div style="flex:1 1 160px!important;box-sizing:border-box!important;background:#fff;border:1px solid #e2e8f0;border-radius:20px;padding:20px 16px;text-align:center;"><div style="font-size:28px;font-weight:900;color:#1a202c;margin-bottom:4px;">1.5M+</div><div style="font-size:13px;color:#718096;">População</div></div><div style="flex:1 1 160px!important;box-sizing:border-box!important;background:#fff;border:1px solid #e2e8f0;border-radius:20px;padding:20px 16px;text-align:center;"><div style="font-size:28px;font-weight:900;color:#1a202c;margin-bottom:4px;">R$ 8.2 bi</div><div style="font-size:13px;color:#718096;">PIB Municipal</div></div><div style="flex:1 1 160px!important;box-sizing:border-box!important;background:#fff;border:1px solid #e2e8f0;border-radius:20px;padding:20px 16px;text-align:center;"><div style="font-size:28px;font-weight:900;color:#1a202c;margin-bottom:4px;">85%</div><div style="font-size:13px;color:#718096;">Cobertura SUS</div></div><div style="flex:1 1 160px!important;box-sizing:border-box!important;background:#ff6b00;border:none;border-radius:20px;padding:20px 16px;text-align:center;"><div style="font-size:28px;font-weight:900;color:#fff;margin-bottom:4px;">[cidade_menorvalor]</div><div style="font-size:13px;color:rgba(255,255,255,0.85);">A partir de</div></div></div>
```

## Metric Cards (grid5 — carências: 24h, 30d, 180d, 300d, 24m)

Same pattern using `.grid5` with `flex:1 1 120px!important` and `gap:12px`.

---

## Modality Cards (grid3)

```html
<div class="grid3" style="display:flex!important;flex-wrap:wrap!important;gap:16px!important;margin-bottom:24px;"><div style="flex:1 1 220px!important;box-sizing:border-box!important;background:#fff;border:1px solid #e2e8f0;border-radius:20px;padding:28px 22px;"><div style="width:36px;height:36px;background:#ff6b00;border-radius:10px;display:flex!important;align-items:center!important;justify-content:center!important;color:#fff;font-size:18px;font-weight:800;margin-bottom:14px;">AH</div><h3 style="font-size:17px;font-weight:800;color:#1a202c;margin-bottom:8px;">Ambulatorial + Hospitalar com Obstetrícia</h3><p style="text-align:justify!important;font-size:14px;color:#4a5568;line-height:1.6;margin-bottom:12px;">Description text.</p><div style="background:#fff8f3;border-radius:8px;padding:10px 14px;font-size:13px;color:#ff6b00;font-weight:600;">Ideal para: famílias e gestantes</div></div><div style="flex:1 1 220px!important;box-sizing:border-box!important;background:#fff;border:1px solid #e2e8f0;border-radius:20px;padding:28px 22px;"><div style="width:36px;height:36px;background:#2563eb;border-radius:10px;display:flex!important;align-items:center!important;justify-content:center!important;color:#fff;font-size:18px;font-weight:800;margin-bottom:14px;">H</div><h3 style="font-size:17px;font-weight:800;color:#1a202c;margin-bottom:8px;">Ambulatorial + Hospitalar</h3><p style="text-align:justify!important;font-size:14px;color:#4a5568;line-height:1.6;margin-bottom:12px;">Description text.</p><div style="background:#eff6ff;border-radius:8px;padding:10px 14px;font-size:13px;color:#2563eb;font-weight:600;">Ideal para: casais sem filhos</div></div><div style="flex:1 1 220px!important;box-sizing:border-box!important;background:#fff;border:1px solid #e2e8f0;border-radius:20px;padding:28px 22px;"><div style="width:36px;height:36px;background:#2563eb;border-radius:10px;display:flex!important;align-items:center!important;justify-content:center!important;color:#fff;font-size:18px;font-weight:800;margin-bottom:14px;">A</div><h3 style="font-size:17px;font-weight:800;color:#1a202c;margin-bottom:8px;">Ambulatorial</h3><p style="text-align:justify!important;font-size:14px;color:#4a5568;line-height:1.6;margin-bottom:12px;">Description text.</p><div style="background:#eff6ff;border-radius:8px;padding:10px 14px;font-size:13px;color:#2563eb;font-weight:600;">Ideal para: quem busca economia</div></div></div>
```

---

## Hospital Cards

### Hero Card (main hospital)
```html
<div style="background:#fff;border:2px solid #ff6b00;border-radius:20px;padding:28px 24px;margin-bottom:20px;box-shadow:0 2px 8px rgba(0,0,0,0.04);"><div style="display:flex!important;align-items:center!important;gap:12px!important;margin-bottom:14px;"><div style="width:40px;height:40px;background:#ff6b00;border-radius:10px;display:flex!important;align-items:center!important;justify-content:center!important;color:#fff;font-size:16px;font-weight:800;">HP</div><h3 style="font-size:18px;font-weight:800;color:#1a202c;margin:0;">Hospital Name</h3></div><p style="text-align:justify!important;font-size:14px;color:#4a5568;line-height:1.6;margin-bottom:12px;">Description.</p><div style="background:#fff8f3;border-radius:8px;padding:10px 14px;font-size:13px;color:#ff6b00;font-weight:600;">📍 Address info</div></div>
```

### Secondary Cards (grid2)
Use `.grid2` with `flex:1 1 300px!important`. Blue badges instead of orange. No `border:2px`.

---

## Timeline (Linha do Tempo)

Vertical timeline with 4-5 milestones. Each milestone has a circle connector, year, and description.

```html
<div style="position:relative;padding-left:32px;margin-bottom:28px;"><div style="position:absolute;left:10px;top:8px;bottom:8px;width:2px;background:linear-gradient(180deg,#ff6b00,#e2e8f0);"></div><div style="position:relative;margin-bottom:24px;"><div style="position:absolute;left:-27px;top:4px;width:14px;height:14px;background:#ff6b00;border-radius:50%;border:3px solid #fff;box-shadow:0 0 0 2px #ff6b00;"></div><div style="font-size:14px;font-weight:800;color:#ff6b00;margin-bottom:4px;">2010</div><p style="text-align:justify!important;font-size:14px;color:#4a5568;line-height:1.6;margin:0;">Milestone description.</p></div><div style="position:relative;margin-bottom:24px;"><div style="position:absolute;left:-27px;top:4px;width:14px;height:14px;background:#ff6b00;border-radius:50%;border:3px solid #fff;box-shadow:0 0 0 2px #ff6b00;"></div><div style="font-size:14px;font-weight:800;color:#ff6b00;margin-bottom:4px;">2015</div><p style="text-align:justify!important;font-size:14px;color:#4a5568;line-height:1.6;margin:0;">Milestone description.</p></div></div>
```

---

## Coverage X-Ray (Raio-X)

3 levels with colored circles. Uses `align-items:flex-start!important` + `margin-top:3px` on circle.

```html
<div style="margin-bottom:24px;"><div style="font-size:18px;font-weight:700;color:#1a202c;margin-bottom:16px;">Raio-X da Cobertura</div><div style="display:flex!important;align-items:flex-start!important;gap:10px!important;margin-bottom:12px;"><div style="width:14px;height:14px;flex-shrink:0!important;background:#ff6b00;border-radius:50%;margin-top:3px;"></div><div><div style="font-size:14px;font-weight:700;color:#1a202c;">Cobertura Total</div><p style="text-align:justify!important;font-size:13px;color:#718096;margin:4px 0 0;">Description of full coverage areas.</p></div></div><div style="display:flex!important;align-items:flex-start!important;gap:10px!important;margin-bottom:12px;"><div style="width:14px;height:14px;flex-shrink:0!important;background:#d45500;border-radius:50%;margin-top:3px;"></div><div><div style="font-size:14px;font-weight:700;color:#1a202c;">Atendimento de Urgência</div><p style="text-align:justify!important;font-size:13px;color:#718096;margin:4px 0 0;">Description of emergency-only areas.</p></div></div><div style="display:flex!important;align-items:flex-start!important;gap:10px!important;margin-bottom:12px;"><div style="width:14px;height:14px;flex-shrink:0!important;background:#e2e8f0;border-radius:50%;margin-top:3px;"></div><div><div style="font-size:14px;font-weight:700;color:#1a202c;">Sem Cobertura Direta</div><p style="text-align:justify!important;font-size:13px;color:#718096;margin:4px 0 0;">Description of areas without direct coverage.</p></div></div></div>
```

---

## Contraction Steps

Steps 1-3 with orange numbered badges + connector line. Step 4 with blue ✓ badge (no line).

```html
<div style="margin-bottom:24px;"><div class="step-row" style="display:flex!important;gap:16px!important;margin-bottom:0;"><div class="step-col" style="display:flex!important;flex-direction:column!important;align-items:center!important;width:40px;flex-shrink:0!important;"><div class="step-num" style="width:36px;height:36px;background:#ff6b00;border-radius:50%;display:flex!important;align-items:center!important;justify-content:center!important;color:#fff;font-size:18px;font-weight:800;">1</div><div style="width:2px;flex:1;background:#e2e8f0;margin:4px 0;"></div></div><div style="flex:1;padding-bottom:20px;"><h3 style="font-size:16px;font-weight:700;color:#1a202c;margin-bottom:6px;">Step Title</h3><p style="text-align:justify!important;font-size:14px;color:#4a5568;line-height:1.6;margin:0;">Step description.</p></div></div><div class="step-row" style="display:flex!important;gap:16px!important;margin-bottom:0;"><div class="step-col" style="display:flex!important;flex-direction:column!important;align-items:center!important;width:40px;flex-shrink:0!important;"><div class="step-num" style="width:36px;height:36px;background:#2563eb;border-radius:50%;display:flex!important;align-items:center!important;justify-content:center!important;color:#fff;font-size:18px;font-weight:800;">✓</div></div><div style="flex:1;"><h3 style="font-size:16px;font-weight:700;color:#1a202c;margin-bottom:6px;">Final Step</h3><p style="text-align:justify!important;font-size:14px;color:#4a5568;line-height:1.6;margin:0;">Final step description.</p></div></div></div>
```

---

## FAQ Structure

Uses native `<details>/<summary>` (no JS). Each question has numbered text + orange `+` icon that rotates 45° on open.

```html
<section style="background:#fff;padding:20px 10px;border-radius:20px;margin-bottom:4px;border:1px solid #e2e8f0;" id="faq"><div style="display:inline-block;background:#ff6b00;color:#fff;font-size:12px;font-weight:700;padding:4px 12px;border-radius:6px;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px;">Perguntas Frequentes</div><h2 style="font-size:clamp(24px,4vw,30px);font-weight:900;color:#1a202c;margin-bottom:8px;">FAQ Title</h2><p style="text-align:justify!important;font-size:18px;font-weight:500;color:#718096;margin-bottom:12px;">Subtitle text.</p><div style="width:60px;height:4px;background:linear-gradient(90deg,#ff6b00,#ff8533);border-radius:2px;margin-bottom:28px;"></div><details style="border:1px solid #e2e8f0;border-radius:10px;margin-bottom:12px;"><summary style="padding:16px 20px;font-size:18px;font-weight:600;color:#1a202c;cursor:pointer;display:flex!important;justify-content:space-between!important;align-items:center!important;list-style:none;"><span>1. Question text here?</span><span style="color:#ff6b00;font-size:20px;font-weight:300;transition:transform 0.3s;">+</span></summary><div style="padding:14px 20px;font-size:14px;color:#4a5568;line-height:1.7;background:#fafbfc;border-top:1px solid #e2e8f0;"><p style="text-align:justify!important;margin:0;">Answer text here (2-4 sentences).</p></div></details></section>
```

---

## CTA Shortcode (bare — no section wrapper)

**1st CTA (post-table, after S2)** — must have `id="cotacao-1"` (anchor target from sumário):
```html
<div id="cotacao-1" style="margin-bottom:4px;">[elementor-template id="11215"]</div>
```

**2nd and 3rd CTAs (intermediário + final):**
```html
<div style="margin-bottom:4px;">[elementor-template id="11215"]</div>
```

---

## Conclusion Section

```html
<section style="background:linear-gradient(135deg,#f8fafc 0%,#f1f5f9 100%);padding:20px 10px;border-radius:20px;margin-bottom:4px;border-top:1px solid #e2e8f0;" id="conclusao"><!-- Standard header --><div class="grid4" style="display:flex!important;flex-wrap:wrap!important;gap:12px!important;margin-bottom:24px;"><!-- 4 metric cards with white bg, border, shadow --></div><p style="text-align:justify!important;font-size:18px;color:#4a5568;line-height:1.7;">Concluding paragraph with CTA and <strong style="color:#ff6b00;">[cidade_menorvalor]</strong> shortcode.</p><p style="text-align:justify!important;font-size:12px;color:#94a3b8;font-style:italic;margin-top:20px;">Fontes: IBGE, ANS, Hapvida S.A. Dados atualizados em [mes_atual] de [ano_atual]. Preços sujeitos a alteração conforme faixa etária, modalidade e condições comerciais vigentes.</p></section>
```

---

## Animated Highlight Text

```html
<span class="destaque-laranja-suave" style="background-image:linear-gradient(120deg,rgba(255,107,0,0.22) 0%,rgba(255,133,51,0.22) 100%);background-repeat:no-repeat;background-position:0 50%;background-size:100% 100%;padding:2px 6px;transition:background-size 1.2s ease-out;">highlighted text</span>
```

Minimum 10 occurrences distributed across all sections (Intro through Conclusão). `background-size:100% 100%` — NEVER `0%`.

---

# [V5] COMPONENTES DE LANDING

> Camada de dinamismo/conversão da V5. **Princípio inegociável:** tudo é melhoria progressiva — sem JS, nenhum conteúdo some e nenhum botão morto aparece. Limites de uso e regras editoriais na seção "COMPONENTES DE LANDING [V5]" do SKILL.md. CSS/JS de suporte em `styles-and-scripts.md` (blocos [V5]).

## [V5] Barra Fixa de Cotação (mobile) — 1 por artigo

Colocada **imediatamente antes do `<style>`** (antepenúltimo elemento). Invisível por padrão (`display:none` via classe no `<style>`); o JS a exibe no celular após a rolagem passar do lead. Sem JS: não existe, nada quebra.

```html
<div class="v5-sticky-cta" style="position:fixed!important;bottom:0!important;left:0!important;right:0!important;z-index:99999!important;background:linear-gradient(135deg,#ff6b00,#e85d00)!important;box-shadow:0 -4px 16px rgba(0,0,0,0.18)!important;padding:10px 14px!important;align-items:center!important;justify-content:center!important;gap:10px!important;"><span style="color:#fff;font-size:14px;font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">Hapvida em [Cidade] a partir de <strong>[cidade_menorvalor]</strong></span><a class="acao-abrir-popup" href="#" style="flex-shrink:0!important;display:inline-block;background:#fff;color:#e85d00!important;font-size:14px;font-weight:800;padding:8px 16px;border-radius:8px;text-decoration:none;">Cotar agora</a></div>
```

Regras: só celular (o CSS esconde em ≥769px) · texto curto (1 linha com reticências) · CTA com `class="acao-abrir-popup" href="#"` (regra de CTA da skill) · personalizar o texto com a cidade (anti-doorway vale aqui também).

## [V5] Faixa de Conversão pós-Lead (mini-hero) — 1 por artigo

**[V7.1]** Entra **logo depois do Sumário**, abrindo a segunda metade da seção de preço (S2↑b) e colada ao `[elementor-template]` — **nunca entre a tabela e o sumário**. Resolve em 5 segundos: o que é, quanto custa, o que fazer. Fundo navy (mesma família dos headers de tabela — NÃO é bg de seção, é banda de destaque).

```html
<div class="v5-hero-conv" style="background:linear-gradient(135deg,#1a1a2e,#16213e);border-radius:20px;padding:24px 20px;margin-bottom:4px;display:flex!important;flex-wrap:wrap!important;align-items:center!important;gap:18px!important;"><div style="flex:1 1 220px!important;box-sizing:border-box!important;"><div style="font-size:12px;font-weight:700;color:#ff8533;text-transform:uppercase;letter-spacing:1px;margin-bottom:4px;">Plano Hapvida em [Cidade]</div><div style="font-size:30px;font-weight:900;color:#fff;line-height:1.1;">A partir de<br><span style="color:#ff8533;">[cidade_menorvalor]</span>/mês</div></div><div style="flex:1 1 180px!important;box-sizing:border-box!important;display:flex!important;gap:14px!important;"><div><div style="font-size:20px;font-weight:900;color:#fff;">[X]</div><div style="font-size:12px;color:#94a3b8;">unidades próprias</div></div><div><div style="font-size:20px;font-weight:900;color:#fff;">[Hospital]</div><div style="font-size:12px;color:#94a3b8;">referência na cidade</div></div></div><a class="acao-abrir-popup" href="#" style="flex-shrink:0!important;display:inline-block;background:linear-gradient(135deg,#ff6b00,#e85d00);color:#fff!important;font-size:16px;font-weight:800;padding:14px 26px;border-radius:10px;text-decoration:none;box-shadow:0 4px 14px rgba(255,107,0,0.35);">Fazer cotação</a></div>
```

Regras: as 2 mini-métricas são REAIS (rede do banco) e da cidade — nunca placeholder genérico · o preço é sempre shortcode · **quebra de linha após "A partir de"** — o preço cai para a 2ª linha (`A partir de<br>[shortcode]/mês`), preferência do usuário.

## [V5] Abas Individual × Empresarial — máx. 1 por artigo (S3 ou S7)

Os DOIS painéis vêm completos no HTML (empilhados). A barra de botões nasce escondida; o JS a exibe e ativa o modo abas. Sem JS: leitor vê os dois blocos em sequência — nada some.

```html
<div class="v5-tabs" style="margin-bottom:24px;"><div class="v5-tabbar" style="gap:8px!important;flex-wrap:wrap!important;"><button type="button" class="v5-tabbtn v5-active">Para empresas (CNPJ)</button><button type="button" class="v5-tabbtn">Individual e família</button></div><div class="v5-panel v5-active"><h3 style="font-size:19px;font-weight:800;color:#1a202c;margin:14px 0 8px 0;">[Título do bloco empresarial — ângulo local]</h3><p style="text-align:justify!important;font-size:18px;color:#4a5568;line-height:1.7;">Conteúdo empresarial da cidade.</p></div><div class="v5-panel"><h3 style="font-size:19px;font-weight:800;color:#1a202c;margin:14px 0 8px 0;">[Título do bloco individual — ângulo local]</h3><p style="text-align:justify!important;font-size:18px;color:#4a5568;line-height:1.7;">Conteúdo individual da cidade.</p></div></div>
```

Regras: nº de botões = nº de painéis (o JS confere e só ativa se bater) · conteúdo dos painéis segue anti-doorway normal · sem `<style>`/classes o conteúdo continua 100% legível e indexável (o Google lê os dois painéis).

## [V5] Contador Animado em Metric Card

Variante do Metric Card: o número ganha `class="v5-countup"` + `data-v5-num` (inteiro puro) e opcionais `data-v5-prefix`/`data-v5-suffix`. **O número final já está escrito no HTML** — sem JS, aparece parado (visível-primeiro).

```html
<div class="v5-countup" data-v5-num="127" data-v5-suffix=" mil" style="font-size:28px;font-weight:900;color:#1a202c;margin-bottom:4px;">127 mil</div>
```

Regras: SÓ para inteiros simples (população em mil, nº de unidades, leitos) · NUNCA em valores com shortcode (`[cidade_menorvalor]`) nem em R$ — shortcode renderiza no servidor e o JS não deve tocar em preço · máx. 1 grid com contadores por artigo (senão vira parque de diversões).

## [V5] Revelação Suave ao Rolar (classe utilitária)

Adicionar `v5-reveal` a cards, boxes e faixas selecionados. Elemento nasce VISÍVEL; o próprio JS o esconde e revela com deslize quando entra na tela (mesma lógica do grifo). Sem JS: tudo visível, estático.

```html
<div class="v5-reveal" style="...estilos normais do card...">...</div>
```

Regras: usar com parcimônia (6-10 elementos por artigo, os que merecem entrada) · NUNCA em parágrafos de texto corrido (só em componentes visuais) · NUNCA `opacity:0` inline no HTML.

## [V5] Sumário Compacto em Fichas (variante do TOC) — ⛔ NÃO USAR

> **Descartado pelo usuário.** Depois de revisar os artigos v5, o usuário não gostou das fichas horizontais e pediu para manter SEMPRE o sumário vertical (`toc-list`, estilo v4) — cabeçalho "Neste Guia Você Vai Encontrar", cada item numa linha com o número no quadradinho laranja. Este bloco fica só como referência histórica; **não gerar as fichas em novos artigos**.

Alternativa ao sumário vertical: uma linha de fichas roláveis na horizontal. Mantém as regras do sumário (só `<div>`/`<a>`, item de Cotação em laranja, âncoras `#id`). Usar UMA das duas variantes por artigo — nunca as duas.

```html
<section style="background:linear-gradient(135deg,#fafbfc 0%,#f0f4f8 100%);padding:14px 10px;border-radius:20px;margin-bottom:4px;border:1px solid #e2e8f0;"><div class="v5-chips" style="display:flex!important;flex-wrap:nowrap!important;overflow-x:auto;gap:8px!important;padding:2px;"><span style="flex-shrink:0!important;font-size:13px;font-weight:800;color:#718096;text-transform:uppercase;letter-spacing:1px;align-self:center;">Neste guia:</span><a href="#por-que-cidade" style="flex-shrink:0!important;font-size:14px;font-weight:700;color:#1a202c;background:#fff;border:1px solid #e2e8f0;border-radius:999px;padding:8px 14px;text-decoration:none;">Por que [Cidade]</a><a href="#precos" style="flex-shrink:0!important;font-size:14px;font-weight:700;color:#1a202c;background:#fff;border:1px solid #e2e8f0;border-radius:999px;padding:8px 14px;text-decoration:none;">Preços</a><a href="#cotacao-1" style="flex-shrink:0!important;font-size:14px;font-weight:800;color:#fff!important;background:linear-gradient(135deg,#ff6b00,#e85d00);border-radius:999px;padding:8px 14px;text-decoration:none;box-shadow:0 4px 14px rgba(255,107,0,0.35);">Faça uma Cotação</a><a href="#rede-cidade" style="flex-shrink:0!important;font-size:14px;font-weight:700;color:#1a202c;background:#fff;border:1px solid #e2e8f0;border-radius:999px;padding:8px 14px;text-decoration:none;">Rede</a><a href="#cobertura-bairros" style="flex-shrink:0!important;font-size:14px;font-weight:700;color:#1a202c;background:#fff;border:1px solid #e2e8f0;border-radius:999px;padding:8px 14px;text-decoration:none;">Bairros</a><a href="#faq" style="flex-shrink:0!important;font-size:14px;font-weight:700;color:#1a202c;background:#fff;border:1px solid #e2e8f0;border-radius:999px;padding:8px 14px;text-decoration:none;">FAQ</a></div></section>
```

Regras: 6-9 fichas (rótulos CURTOS, 1-2 palavras — não o título inteiro da seção) · a ficha de Cotação sempre presente e em laranja · rolagem horizontal é esperada no celular (`overflow-x:auto`).

## [V5] Placar Versus (S6 — alternativa à tabela comparativa)

Dois cards lado a lado: Hapvida (borda laranja) × concorrente local (navy). Cada linha = critério com VALOR ESPECÍFICO (número/fato local), nunca marcação vazia. **Exceção:** se o DR1 registrou que a caixa de destaque da SERP é *tabela*, a tabela clássica permanece e o placar não a substitui.

```html
<div class="grid2" style="display:flex!important;flex-wrap:wrap!important;gap:16px!important;margin-bottom:24px;"><div style="flex:1 1 300px!important;box-sizing:border-box!important;background:#fff;border:2px solid #ff6b00;border-radius:20px;overflow:hidden;"><div style="background:linear-gradient(135deg,#ff6b00,#e85d00);padding:14px 18px;font-size:17px;font-weight:900;color:#fff;">Hapvida em [Cidade]</div><div style="padding:6px 18px 14px 18px;"><div style="padding:10px 0;border-bottom:1px solid #f1f5f9;"><div style="font-size:12px;color:#718096;font-weight:600;">[Critério local 1]</div><div style="font-size:15px;color:#1a202c;font-weight:800;">[valor Hapvida]</div></div><div style="padding:10px 0;"><div style="font-size:12px;color:#718096;font-weight:600;">[Critério local 2]</div><div style="font-size:15px;color:#1a202c;font-weight:800;">[valor Hapvida]</div></div></div></div><div style="flex:1 1 300px!important;box-sizing:border-box!important;background:#fff;border:1px solid #e2e8f0;border-radius:20px;overflow:hidden;"><div style="background:linear-gradient(135deg,#1a1a2e,#16213e);padding:14px 18px;font-size:17px;font-weight:900;color:#fff;">[Concorrente] em [Cidade]</div><div style="padding:6px 18px 14px 18px;"><div style="padding:10px 0;border-bottom:1px solid #f1f5f9;"><div style="font-size:12px;color:#718096;font-weight:600;">[Critério local 1]</div><div style="font-size:15px;color:#4a5568;font-weight:700;">[valor concorrente]</div></div><div style="padding:10px 0;"><div style="font-size:12px;color:#718096;font-weight:600;">[Critério local 2]</div><div style="font-size:15px;color:#4a5568;font-weight:700;">[valor concorrente]</div></div></div></div></div>
```

Regras: 3-5 critérios por card, todos verificados (Modo 1 audita) e ≥2 exclusivos da cidade (regra da S6 intacta) · sem ícones de certo/errado (regra de ícones: sem emoji/dingbat) · tom consultivo: o placar informa, não desmerece o concorrente.

## [V5] Faixa de Selos de Confiança — sob cada formulário

Entra logo APÓS cada `[elementor-template]` (fora do wrapper `#cotacao-1`). Só dados REAIS (registro ANS da operadora, tempo de mercado da DRV, prêmios reais dos consultores — os mesmos do schema Person).

```html
<div class="v5-trust" style="display:flex!important;flex-wrap:wrap!important;justify-content:center!important;gap:10px!important;margin:10px 0 24px 0;"><span style="font-size:12px;color:#64748b;font-weight:600;border:1px solid #e2e8f0;border-radius:999px;padding:6px 12px;background:#fff;">Operadora registrada na ANS — nº 359017</span><span style="font-size:12px;color:#64748b;font-weight:600;border:1px solid #e2e8f0;border-radius:999px;padding:6px 12px;background:#fff;">DRV: 10+ anos especialista Hapvida</span><span style="font-size:12px;color:#64748b;font-weight:600;border:1px solid #e2e8f0;border-radius:999px;padding:6px 12px;background:#fff;">7.000+ clientes atendidos</span></div>
```

Regras: máx. 3 selos por faixa · zero superlativo vazio ("o melhor", "nº 1") · os selos NÃO contam como menção DRV para o limite E-E-A-T (são credencial factual, não narrativa), mas o texto deles não muda entre cidades — por isso ficam FORA da cota anti-doorway e não podem crescer além disso.

---

# [V6] COMPONENTES DE DADOS (visualização)

> **O buraco que isto preenche.** Até a v5 o artigo tinha **zero visualização de dado**: número virava cartão (`metric card`) ou tabela, nunca gráfico. Para "quanto sobe o preço a cada faixa etária" ou "quanto da rede é própria", cartão e tabela mostram o **valor** mas escondem a **forma** — e às vezes a forma é a informação.
>
> **Tudo aqui é HTML + CSS inline. Zero JavaScript, zero biblioteca externa.** Consequência boa: sobrevive ao `wpautop`, funciona com JS desligado por construção, e o valor está sempre visível (não existe "passe o mouse para ver").

## A paleta de série — medida, não escolhida no olho

As cores foram passadas pelo validador de daltonismo do método de dataviz. O resultado mudou a escolha:

| Par | Veredito |
|---|---|
| **`#e85d00` + `#2563eb`** | ✅ **passa nos 6 testes**, contraste incluído — **é esta que se usa** |
| `#ff6b00` + `#2563eb` | passa em daltonismo, mas o laranja fica em 2,78:1 de contraste (exigiria alívio extra) |
| `#16213e` como série | ❌ reprovado — escuro demais e sem saturação, "lê como cinza". Serve para cabeçalho de tabela, não para dado |
| `#7c3aed` (roxo) como 3ª série | ❌ reprovado feio — ΔE 0,4 contra o azul em deuteranopia: **a mesma cor** para quem tem daltonismo verde-vermelho |

**Regra:** 1ª série `#e85d00`, 2ª série `#2563eb`, sempre nessa ordem, **nunca cicladas**. Terceira série: evitar — prefira dois gráficos ou uma tabela. Se for inevitável, `#0d9488` passa, mas exige rótulo direto em cada barra (a separação contra o azul fica na faixa de piso).

**Trilho de fundo** `#f1f5f9` · **texto** sempre em tinta (`#1a202c` / `#4a5568` / `#718096`), **nunca na cor da série**.

## [V6] Barras horizontais — 1 série

Para magnitude entre categorias (unidades por região, leitos por hospital, faixa etária). Ponta arredondada só na extremidade livre; o valor fica sempre à direita.

```html
<div style="margin:22px 0;padding:20px;background:#fff;border:1px solid #e2e8f0;border-radius:12px" role="group" aria-label="Unidades Hapvida por região de Piracicaba"><p style="font-size:16px;font-weight:800;color:#1a202c;margin:0 0 3px">Unidades Hapvida por região</p><p style="font-size:13px;color:#718096;margin:0 0 16px">Piracicaba — rede própria e credenciada, [mes_atual] de [ano_atual]</p><div style="display:flex;align-items:center;gap:10px;margin-bottom:8px"><span style="flex:0 0 100px;font-size:14px;color:#4a5568">Centro</span><span style="flex:1 1 auto;height:20px;background:#f1f5f9;border-radius:4px;display:block"><span style="display:block;width:100%;height:100%;background:#e85d00;border-radius:0 4px 4px 0"></span></span><span style="flex:0 0 44px;text-align:right;font-size:15px;font-weight:800;color:#1a202c">7</span></div><div style="display:flex;align-items:center;gap:10px;margin-bottom:8px"><span style="flex:0 0 100px;font-size:14px;color:#4a5568">Zona Norte</span><span style="flex:1 1 auto;height:20px;background:#f1f5f9;border-radius:4px;display:block"><span style="display:block;width:57%;height:100%;background:#e85d00;border-radius:0 4px 4px 0"></span></span><span style="flex:0 0 44px;text-align:right;font-size:15px;font-weight:800;color:#1a202c">4</span></div><div style="display:flex;align-items:center;gap:10px"><span style="flex:0 0 100px;font-size:14px;color:#4a5568">Zona Sul</span><span style="flex:1 1 auto;height:20px;background:#f1f5f9;border-radius:4px;display:block"><span style="display:block;width:29%;height:100%;background:#e85d00;border-radius:0 4px 4px 0"></span></span><span style="flex:0 0 44px;text-align:right;font-size:15px;font-weight:800;color:#1a202c">2</span></div></div>
```

**Largura da barra:** `valor ÷ maior valor × 100`. A maior fica em `100%`. Uma série só **não leva legenda** — o título já nomeia.

## [V6] Barras agrupadas — 2 séries

Para comparar duas coisas nas mesmas categorias. Legenda obrigatória a partir de 2 séries, com o quadradinho de cor **ao lado** do texto em tinta.

```html
<div style="margin:22px 0;padding:20px;background:#fff;border:1px solid #e2e8f0;border-radius:12px" role="group" aria-label="Comparativo de mensalidade entre individual e empresarial"><p style="font-size:16px;font-weight:800;color:#1a202c;margin:0 0 3px">Individual × Empresarial na faixa de 34 a 38 anos</p><p style="font-size:13px;color:#718096;margin:0 0 12px">Valores vigentes em [mes_atual] de [ano_atual]</p><div style="display:flex;gap:16px;margin:0 0 16px"><span style="font-size:13px;color:#4a5568"><span style="display:inline-block;width:11px;height:11px;background:#e85d00;border-radius:2px;margin-right:6px"></span>Individual</span><span style="font-size:13px;color:#4a5568"><span style="display:inline-block;width:11px;height:11px;background:#2563eb;border-radius:2px;margin-right:6px"></span>Empresarial</span></div><div style="margin-bottom:14px"><p style="font-size:14px;color:#4a5568;margin:0 0 5px">Fortaleza</p><div style="display:flex;align-items:center;gap:8px;margin-bottom:2px"><span style="flex:1 1 auto;height:16px;background:#f1f5f9;border-radius:4px;display:block"><span style="display:block;width:100%;height:100%;background:#e85d00;border-radius:0 4px 4px 0"></span></span><span style="flex:0 0 86px;text-align:right;font-size:14px;font-weight:700;color:#1a202c">R$ 159,04</span></div><div style="display:flex;align-items:center;gap:8px"><span style="flex:1 1 auto;height:16px;background:#f1f5f9;border-radius:4px;display:block"><span style="display:block;width:68%;height:100%;background:#2563eb;border-radius:0 4px 4px 0"></span></span><span style="flex:0 0 86px;text-align:right;font-size:14px;font-weight:700;color:#1a202c">R$ 108,15</span></div></div></div>
```

**Vão de 2px entre as duas barras do mesmo grupo** (`margin-bottom:2px`) — é o que separa as séries sem depender só da cor.

## [V6] Barra 100% empilhada — parte-do-todo

**Use esta no lugar de pizza.** Pizza tem nota **C** de acessibilidade e exige a barra empilhada como alternativa obrigatória — então já se faz a barra direto e pula-se a pizza.

```html
<div style="margin:22px 0;padding:20px;background:#fff;border:1px solid #e2e8f0;border-radius:12px" role="group" aria-label="Composição da rede: própria e credenciada"><p style="font-size:16px;font-weight:800;color:#1a202c;margin:0 0 12px">Composição da rede em Piracicaba</p><div style="display:flex;height:26px;border-radius:6px;overflow:hidden;gap:2px;background:#fff"><span style="flex:0 0 62%;background:#e85d00;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:800;color:#1a202c">62%</span><span style="flex:1 1 auto;background:#2563eb;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:800;color:#fff">38%</span></div><div style="display:flex;gap:16px;margin-top:10px;flex-wrap:wrap"><span style="font-size:13px;color:#4a5568"><span style="display:inline-block;width:11px;height:11px;background:#e85d00;border-radius:2px;margin-right:6px"></span>Rede própria — 13 unidades</span><span style="font-size:13px;color:#4a5568"><span style="display:inline-block;width:11px;height:11px;background:#2563eb;border-radius:2px;margin-right:6px"></span>Credenciada — 8 unidades</span></div></div>
```

**Máx. 3 fatias.** Acima disso, usar as barras horizontais.

⚠️ **A cor do rótulo dentro da barra muda por segmento — não é descuido, é conta.** Medido:

| Rótulo sobre | Branco | Tinta `#1a202c` |
|---|---|---|
| laranja `#e85d00` | 3,50:1 ❌ | **4,66:1 ✅** |
| azul `#2563eb` | **5,17:1 ✅** | 3,16:1 ❌ |

Texto de 13px em negrito **não** conta como "texto grande" na WCAG, então o piso é 4,5:1 — e branco sobre o laranja reprova. Por isso: **tinta escura sobre o laranja, branco sobre o azul**. Se mudar a cor de uma fatia, refazer a conta antes de escolher a cor do rótulo.

## Regras de uso (inegociáveis)

1. **Dose: no máximo 2 gráficos por artigo.** Gráfico é destaque; três viram enfeite. Contam junto com os 3-5 componentes de landing.
2. **⚠️ Gráfico de PREÇO tem a mesma trava da imagem.** A largura da barra é um número congelado no HTML. Se o preço mudar e ninguém regerar, **a barra passa a mentir em silêncio** — exatamente o que a regra do shortcode existe para evitar, e pior que na imagem, porque não há arquivo separado para conferir. Portanto: gráfico de preço **só** com rótulo de vigência visível e **regerado no mesmo gatilho da imagem** (ver `references/imagem-automatica.md` → "Quando regerar"). Para dado estável (unidades, leitos, composição de rede), uso livre.
3. **Valor sempre visível.** Nunca só na cor, nunca só ao passar o mouse. É isso que dá alívio ao aviso de contraste do laranja.
4. **⚠️ TRAVA DE CITABILIDADE — o número TEM de existir em texto, não só na barra.**

   **LLM lê texto.** Ele não mede a largura de um `<div>`. Se o dado existir **apenas** dentro do gráfico, ele fica **invisível** para AI Overview, ChatGPT, Perplexity e Claude — e o artigo perde exatamente a citação que a camada de defensibilidade do dado existe para conquistar.

   O gráfico é, do ponto de vista da IA, **decoração**. O que a IA cita é a frase.

   | ❌ Errado | ✅ Certo |
   |---|---|
   | gráfico com as barras e o título "Unidades por região", e nada no texto | a frase no corpo — "**A rede em Piracicaba tem 13 unidades: 7 no Centro, 4 na Zona Norte e 2 na Zona Sul**" — e o gráfico ao lado mostrando a proporção |

   **Regra:** todo número que aparece num gráfico aparece **também** em passagem de texto ou em `<table>`, na mesma seção. O gráfico mostra a **forma**; o texto entrega o **dado**. Em seção de preço, os três convivem: shortcode no texto, tabela, gráfico.

   Isto vale igual para a imagem da tabela (`references/imagem-automatica.md`) — daí a regra dos shortcodes de preço nos 3 pontos obrigatórios continuar valendo, sem desconto.

   *(Como efeito colateral, isso também resolve a acessibilidade: quem usa leitor de tela recebe o mesmo dado. Mas a razão mais forte é a citação.)*
5. **Sem `@media` dentro do gráfico** — a regra da casa vale aqui também (o Elementor sobrescreve). O `flex` já degrada sozinho.
6. **`role="group"` + `aria-label`** descrevendo o que o gráfico mostra.
7. **Ordem das séries fixa:** 1ª `#e85d00`, 2ª `#2563eb`. Nunca ciclar cor por posição — **a cor segue a entidade**, não o lugar na lista.
