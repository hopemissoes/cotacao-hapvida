# -*- coding: utf-8 -*-
"""Etapa 6: limpa a redundancia criada pelo proprio B6 (dois links para o mesmo
destino na mesma frase) e fecha o item 2."""
import io
SRC='artigos/plano-de-saude-barato_CORRIGIDO.html'
s=io.open(SRC,encoding='utf-8').read(); log=[]
def sub(tag,old,new,n=1):
    global s
    c=s.count(old); assert c==n, f"[{tag}] esperava {n}, achei {c}"
    s=s.replace(old,new); log.append(f"OK  {tag}")

sub('G1 remove link duplicado na mesma frase',
 ', vendido sob a marca do grupo naquelas praças — por isso o individual da marca Hapvida se concentra nos onze estados do Norte e do Nordeste, e em São Paulo e no Rio a porta de pessoa física é <a style="color: #ff6b00; font-weight: 600;" href="https://tabelaplanos.com.br/notrelife-sp-rj/">o NotreLife</a>.',
 ', vendido sob a marca do grupo naquelas praças. É por isso que o individual da marca Hapvida se concentra nos onze estados do Norte e do Nordeste: em São Paulo e no Rio, a porta de pessoa física existe, mas atende por outro nome e com outra cesta.')

assert s.count('notrelife-sp-rj')==2, s.count('notrelife-sp-rj')
log.append("OK  G2 2 links para /notrelife-sp-rj/ (um no contexto do produto, um no bloco Sudeste)")

# integridade final
import re
for m in re.finditer(r'<(style|script)>(.*?)</\1>',s,re.S):
    assert '<br' not in m.group(2) and '\n' not in m.group(2)
assert '2,38' not in s and '359017' not in s
assert s.count('badge-menor')==3
assert 'R$ 216,80' in s and 'R$ 229,23' in s and 'R$ 113,69' in s
log.append("OK  G3 integridade mantida (style/script, numeros, badges)")

io.open(SRC,'w',encoding='utf-8').write(s)
print('\n'.join(log)); print(f"\n>> {len(s)} chars")
