# -*- coding: utf-8 -*-
"""Troca os shortcodes de PRECO/COPARTICIPACAO por XXXX, para o dono preencher
manualmente. Mantem os que quebrariam a pagina ou violariam regra da v7:
  [elementor-template id="11215"] -> e o formulario de cotacao (3x)
  [ano_atual] / [mes_atual]       -> shortcodes.md regras 1 e 2: NUNCA escrever
                                     ano/mes fixo em conteudo evergreen
Gera um mapa numerado XXXX-01..N dizendo o que vai em cada slot."""
import io, re
SRC='artigos/plano-de-saude-barato_FINAL.html'
DST='artigos/plano-de-saude-barato_XXXX.html'
s=io.open(SRC,encoding='utf-8').read()

MANTER={'[ano_atual]','[mes_atual]'}
alvo=re.compile(r'\[[a-z0-9_\-]+\]')
def contexto(txt,pos,n=95):
    a=re.sub(r'<[^>]+>',' ',txt[max(0,pos-260):pos])
    a=re.sub(r'\s+',' ',a).strip()
    return a[-n:]

mapa=[]; out=[]; last=0; i=0
for m in alvo.finditer(s):
    sc=m.group(0)
    if sc in MANTER or 'elementor' in sc: continue
    i+=1
    tag=f"XXXX-{i:02d}"
    mapa.append((tag,sc,contexto(s,m.start())))
    out.append(s[last:m.start()]); out.append(tag); last=m.end()
out.append(s[last:])
novo=''.join(out)

assert '[elementor-template id="11215"]' in novo and novo.count('[elementor-template id="11215"]')==3
assert '[ano_atual]' in novo and '[mes_atual]' in novo
io.open(DST,'w',encoding='utf-8').write(novo)

linhas=["# Mapa dos XXXX — plano-de-saude-barato","",
 f"{len(mapa)} slots. Substitua cada `XXXX-NN` pelo shortcode correto.",
 "Mantidos de propósito (não vire XXXX): `[elementor-template id=\"11215\"]` (o formulário, 3×),",
 "`[ano_atual]` e `[mes_atual]` — o shortcodes.md proíbe ano/mês fixo em conteúdo evergreen.","",
 "| Slot | Shortcode que eu havia usado | Onde fica (texto imediatamente antes) |","|---|---|---|"]
for t,sc,ctx in mapa:
    linhas.append(f"| `{t}` | `{sc}` | …{ctx.replace('|','/')} |")
io.open('artigos/MAPA_XXXX.md','w',encoding='utf-8').write('\n'.join(linhas)+'\n')
print(f"{len(mapa)} shortcodes -> XXXX")
print(f"mantidos: elementor-template x{novo.count('[elementor-template id=\"11215\"]')}, [ano_atual], [mes_atual]")
