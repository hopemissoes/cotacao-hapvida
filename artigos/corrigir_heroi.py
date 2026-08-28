# -*- coding: utf-8 -*-
"""O numero grande do heroi e o INDIVIDUAL (shortcode). O piso medido pela porta
do CNPJ e menor (R$ 107,83, Fortaleza, jun/2026). Declarar as duas no heroi para
o numero grande nao ser lido como piso absoluto."""
import io, re
SRC='artigos/plano-de-saude-barato_CORRIGIDO.html'
s=io.open(SRC,encoding='utf-8').read()
old=('<div style="font-size: 34px; font-weight: 900; color: #fff; line-height: 1.1; margin-bottom: 18px;">'
     'A partir de <span style="color: #ff8533;">[recife_ind_ambulatorialtotal_0]</span>/mês</div>')
new=('<div style="font-size: 34px; font-weight: 900; color: #fff; line-height: 1.1; margin-bottom: 6px;">'
     'A partir de <span style="color: #ff8533;">[recife_ind_ambulatorialtotal_0]</span>/mês</div>\n'
     '<div style="font-size: 15px; font-weight: 600; color: #94a3b8; margin-bottom: 18px;">'
     'no individual, por CPF — pela porta do CNPJ, medimos a partir de '
     '<span style="color: #e2e8f0; font-weight: 800;">R$ 107,83</span></div>')
assert s.count(old)==1
s=s.replace(old,new)
for m in re.finditer(r'<(style|script)>(.*?)</\1>',s,re.S):
    assert '<br' not in m.group(2) and '\n' not in m.group(2)
io.open(SRC,'w',encoding='utf-8').write(s)
print("OK  I1 heroi declara as duas portas |",len(s),"chars")
