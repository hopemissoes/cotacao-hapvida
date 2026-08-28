# -*- coding: utf-8 -*-
"""Etapa 3: expurgo real do wpautop de dentro de <style> e <script>.
O arquivo de origem ja vinha com <br /> e <p>/</p> LITERAIS dentro dos blocos —
nao eram quebras de linha, entao colapsar linha nao resolvia. Dentro de <script>
o primeiro <br /> eh erro de sintaxe e derruba o arquivo inteiro."""
import re, io
SRC='artigos/plano-de-saude-barato_CORRIGIDO.html'
s=io.open(SRC,encoding='utf-8').read(); log=[]

def limpa(m):
    abre,corpo,fecha=m.group(1),m.group(2),m.group(3)
    corpo=re.sub(r'<br\s*/?>',' ',corpo)          # <br /> literal
    corpo=re.sub(r'</?p[^>]*>',' ',corpo)         # <p> e </p> literais
    corpo=re.sub(r'&nbsp;',' ',corpo)
    corpo=re.sub(r'\s*\n\s*',' ',corpo)
    corpo=re.sub(r'\s{2,}',' ',corpo).strip()
    return abre+corpo+fecha

for tagname in ['style','script']:
    pat=re.compile(r'(<'+tagname+r'>)(.*?)(</'+tagname+r'>)',re.S)
    n=len(pat.findall(s))
    s=pat.sub(limpa,s)
    log.append(f"OK  D1 {n} bloco(s) <{tagname}> limpo(s) de <br>/<p>")

# nenhum bloco pode conter marcacao de wpautop
for m in re.finditer(r'<(style|script)>(.*?)</\1>',s,re.S):
    assert '<br' not in m.group(2), f"<br> sobrou em <{m.group(1)}>"
    assert '<p>' not in m.group(2) and '</p>' not in m.group(2), f"<p> sobrou em <{m.group(1)}>"
    assert '\n' not in m.group(2), f"quebra de linha sobrou em <{m.group(1)}>"
log.append("OK  D2 nenhum bloco <style>/<script> contem marcacao de wpautop")

# D3: multiplicador da SulAmerica no quadro de RECIFE = 5,9997 (5,9995 e Fortaleza)
c=s.count('5,9995×'); assert c==1, f"esperava 1 '5,9995x', achei {c}"
s=s.replace('5,9995×','5,9997×')
log.append("OK  D3 SulAmerica 5,9997x (valor de Recife, nao de Fortaleza)")

# D4: a frase seguinte falava do teto; confere que segue coerente
assert 'menos de um centésimo de por cento do teto' in s
log.append("OK  D4 'menos de um centesimo de por cento do teto' segue valido (5,9997/6 = 99,995%)")

io.open(SRC,'w',encoding='utf-8').write(s)
print('\n'.join(log)); print(f"\n>> {len(s)} chars")
