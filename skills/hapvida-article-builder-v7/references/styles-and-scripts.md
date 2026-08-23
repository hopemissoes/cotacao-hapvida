# Mandatory Style and Script Blocks

These blocks are placed at the END of the `<article>`, in this exact order:
1. `<style>` block — penultimate element
2. `<script>` block — last element

NEVER place `<style>` in the middle of the article.

**WPAUTOP WARNING:** WordPress can inject `<br />` inside `<style>` and `<script>` blocks
when saved in the visual editor, breaking ALL CSS and JS. Always paste in the code/HTML
editor, never the visual editor.

---

## `<style>` Block

```html
<style>
/* === UTILITY CLASSES === */
.fx{display:flex!important}
.fx-col{display:flex!important;flex-direction:column!important}
.fx-center{display:flex!important;align-items:center!important;justify-content:center!important}

/* === GRIDS (FLEXBOX) === */
.grid2{display:flex!important;flex-wrap:wrap!important;gap:16px!important}
.grid3{display:flex!important;flex-wrap:wrap!important;gap:16px!important}
.grid4{display:flex!important;flex-wrap:wrap!important;gap:12px!important}
.grid5{display:flex!important;flex-wrap:wrap!important;gap:12px!important}

/* === ANTI-WPAUTOP (GRIDS) === */
.grid2>p,.grid2>br,.grid3>p,.grid3>br,.grid4>p,.grid4>br,.grid5>p,.grid5>br{display:none!important;margin:0!important;padding:0!important;height:0!important;line-height:0!important}

/* === ANTI-WPAUTOP (SUMÁRIO) === */
.toc-list>p,.toc-list>br,.toc-item>p,.toc-item>br{display:none!important}

/* === ANTI-WPAUTOP (BOXES) === */
.box-row>p{display:contents!important}
.box-row>br{display:none!important}

/* === ANTI-WPAUTOP (STEPS) === */
.step-row>p,.step-row>br,.step-col>p,.step-col>br{display:none!important}

/* === PARÁGRAFOS === */
article p{text-align:justify!important}

/* === EXCEÇÃO COTAÇÃO === */
.titulo-cotacao,.subtitulo-cotacao,.titulo-cotacao .elementor-heading-title,.subtitulo-cotacao .elementor-heading-title{text-align:center!important}

/* === CARDS === */
.card-head{display:flex!important;align-items:center!important;gap:12px!important;margin-bottom:14px}
.card-icon{flex-shrink:0!important}

/* === ANIMATED HIGHLIGHT (REFORÇO) === */
.destaque-laranja-suave{
background-image:linear-gradient(120deg,rgba(255,107,0,0.22) 0%,rgba(255,133,51,0.22) 100%);
background-repeat:no-repeat;
background-position:0 50%;
background-size:100% 100%;
padding:2px 6px;
transition:background-size 1.2s ease-out;
}

/* === FAQ === */
details summary{list-style:none}
details summary::-webkit-details-marker{display:none}
details[open] summary span:last-child{transform:rotate(45deg)}

/* === SCROLL SUAVE === */
html{scroll-behavior:smooth}

/* === RESPONSIVO (apenas padding/font — NÃO grids) === */
@media(max-width:768px){
section{padding:10px 5px!important}
table{font-size:13px!important}
.toc-item a{font-size:14px!important}
}

/* === [V5] LANDING === */
.v5-sticky-cta{display:none!important}
.v5-sticky-cta.v5-on{display:flex!important}
@media(min-width:769px){.v5-sticky-cta{display:none!important}}
.v5-tabbar{display:none!important}
.v5-tabs.v5-on .v5-tabbar{display:flex!important}
.v5-tabs.v5-on .v5-panel{display:none!important}
.v5-tabs.v5-on .v5-panel.v5-active{display:block!important}
.v5-tabbtn{background:#fff;border:1px solid #e2e8f0;color:#4a5568;font-size:14px;font-weight:700;padding:8px 16px;border-radius:999px;cursor:pointer;font-family:inherit}
.v5-tabbtn.v5-active{background:#ff6b00!important;border-color:#ff6b00!important;color:#fff!important}
.v5-reveal{transition:opacity .6s ease-out,transform .6s ease-out}
.v5-chips>p,.v5-chips>br,.v5-tabbar>p,.v5-tabbar>br,.v5-tabs>p,.v5-tabs>br,.v5-trust>p,.v5-trust>br,.v5-sticky-cta>p,.v5-sticky-cta>br,.v5-hero-conv>p,.v5-hero-conv>br{display:none!important}
</style>
```

**Rules:**
- Grid child sizing is NEVER in `<style>` — always inline `flex:1 1 Xpx!important`
- No media queries for grids — Elementor JS overrides them
- The `.destaque-laranja-suave` class reinforces the inline styles (backup if Elementor strips inline)
- NO `@keyframes` and NO `animation` properties — not needed since V4.3

---

## `<script>` Block

Contains two functions:
1. **Intersection Observer** — triggers animated highlight on scroll
2. **Fix Cotação** — forces `text-align:center` on form titles that Elementor JS realigns to `left`

### Visible-First Strategy (V4.3)

- `<span>` starts with `background-size:100% 100%` (VISIBLE)
- JS resets to `0%` and animates on scroll (progressive enhancement)
- If JS is stripped by WordPress, highlight remains visible (static)

| Scenario | Behavior |
|----------|----------|
| JS works (best experience) | Resets to 0% → animates on scroll via IO |
| JS stripped | Inline 100% → highlight always visible, static |
| JS AND CSS stripped | Inline 100% → highlight always visible, static |

### Script (copy exactly)

```html
<script>
document.addEventListener('DOMContentLoaded',function(){
var els=document.querySelectorAll('.destaque-laranja-suave');
if(!els.length)return;
els.forEach(function(el){el.style.backgroundSize='0% 100%';});
var ob=new IntersectionObserver(function(entries){
entries.forEach(function(e){
if(e.isIntersecting){
e.target.style.backgroundSize='100% 100%';
ob.unobserve(e.target);
}
});
},{threshold:0.5});
els.forEach(function(el){ob.observe(el);});
function fixCotacao(){
document.querySelectorAll('.titulo-cotacao,.subtitulo-cotacao,.titulo-cotacao .elementor-heading-title,.subtitulo-cotacao .elementor-heading-title').forEach(function(el){el.style.setProperty('text-align','center','important');});
}
fixCotacao();
setTimeout(fixCotacao,500);
setTimeout(fixCotacao,1500);
setTimeout(fixCotacao,3000);
var mo=new MutationObserver(fixCotacao);
mo.observe(document.body,{childList:true,subtree:true});
setTimeout(function(){mo.disconnect();},10000);
});
</script>
```

### Script Rules:
1. Minimum **10 occurrences** of highlighted text per article, distributed across all sections
2. Span styles are **100% inline** (Elementor overrides `<style>` classes)
3. `background-size` starts at `100% 100%` (VISIBLE) — JS resets to `0%` and animates
4. `threshold: 0.5` = triggers when 50% of element is visible
5. `ob.unobserve` = animates only once (no reactivation on scroll up)
6. **fixCotacao** runs 4× (immediate + 500ms + 1.5s + 3s) + MutationObserver for 10s
7. MutationObserver disconnects after 10s to avoid performance impact
8. **NEVER** use `background-size:0%` in inline `<span>` — if JS is stripped, text becomes invisible
9. The script does NOT use `el.style.animation='none'` — there is no CSS animation to disable

---

## [V5] Script Aditivo de Landing (segundo `<script>`, colado imediatamente APÓS o principal — o fim do `<article>` passa a ser: `<style>` → `<script>` principal → `<script>` [V5])

Ativa os componentes de landing (barra fixa, abas, contadores, revelação). Cada recurso está em `try/catch` próprio — se um falhar, os outros e o script principal continuam. **Só incluir este bloco se o artigo usa pelo menos um componente [V5]** (não carregar JS morto).

### Script (copy exactly)

```html
<script>
document.addEventListener('DOMContentLoaded',function(){
/* [V5-1] Barra fixa de cotação (mobile) — aparece após rolar além do lead */
try{var sb=document.querySelector('.v5-sticky-cta');if(sb){var v5s=function(){var y=window.scrollY||window.pageYOffset;if(y>700){sb.classList.add('v5-on');}else{sb.classList.remove('v5-on');}};window.addEventListener('scroll',v5s,{passive:true});v5s();}}catch(e){}
/* [V5-2] Abas — só ativa se nº de botões = nº de painéis */
try{document.querySelectorAll('.v5-tabs').forEach(function(t){var btns=t.querySelectorAll('.v5-tabbtn'),panels=t.querySelectorAll('.v5-panel');if(btns.length&&btns.length===panels.length){t.classList.add('v5-on');if(!t.querySelector('.v5-panel.v5-active')){panels[0].classList.add('v5-active');}if(!t.querySelector('.v5-tabbtn.v5-active')){btns[0].classList.add('v5-active');}btns.forEach(function(b,i){b.addEventListener('click',function(){btns.forEach(function(x){x.classList.remove('v5-active');});panels.forEach(function(x){x.classList.remove('v5-active');});b.classList.add('v5-active');panels[i].classList.add('v5-active');});});}});}catch(e){}
/* [V5-3] Contadores — número final já está no HTML; JS só anima */
try{var cu=document.querySelectorAll('.v5-countup');if(cu.length&&'IntersectionObserver' in window){var cio=new IntersectionObserver(function(es){es.forEach(function(en){if(!en.isIntersecting)return;cio.unobserve(en.target);var el=en.target,n=parseInt(el.getAttribute('data-v5-num'),10);if(isNaN(n))return;var pre=el.getAttribute('data-v5-prefix')||'',suf=el.getAttribute('data-v5-suffix')||'',t0=null;function stp(ts){if(!t0)t0=ts;var p=Math.min((ts-t0)/900,1);el.textContent=pre+Math.round(n*p).toLocaleString('pt-BR')+suf;if(p<1)requestAnimationFrame(stp);}requestAnimationFrame(stp);});},{threshold:0.6});cu.forEach(function(el){cio.observe(el);});}}catch(e){}
/* [V5-4] Revelação suave — o JS esconde e revela (visível-primeiro) */
try{var rv=document.querySelectorAll('.v5-reveal');if(rv.length&&'IntersectionObserver' in window){rv.forEach(function(el){el.style.opacity='0';el.style.transform='translateY(14px)';});var rio=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){en.target.style.opacity='1';en.target.style.transform='translateY(0)';rio.unobserve(en.target);}});},{threshold:0.15});rv.forEach(function(el){rio.observe(el);});}}catch(e){}
});
</script>
```

### [V5] Script Rules:
1. **Visível-primeiro em tudo:** contador tem o número final escrito no HTML; `.v5-reveal` nasce visível (o JS é quem esconde); painéis de abas nascem empilhados e legíveis; a barra fixa nasce inexistente (é EXTRA, não conteúdo).
2. Barra fixa: gatilho `scrollY > 700` (além do lead) e SÓ celular (o CSS bloqueia em ≥769px).
3. Contador NUNCA em valor com shortcode ou R$ — o shortcode renderiza no servidor e o JS não toca em preço.
4. Abas: se o HTML vier com nº de botões ≠ nº de painéis, o JS NÃO ativa (fica empilhado — seguro).
5. Este bloco é um SEGUNDO `<script>` colado imediatamente após o principal, no fim do `<article>` — nunca um `<script>` no meio do artigo. (Como é um listener próprio de `DOMContentLoaded`, os dois blocos não interferem um no outro.)
6. Sem componente [V5] no artigo → não incluir este bloco.
