# -*- coding: utf-8 -*-
"""ITEM 2 — Sudeste na pagina, em base declarada.
Ordem: (1) desduplica o link criado pelo B6; (2) insere o bloco SP/RJ.
Valores apurados nos artigos irmaos publicados (agosto/2026):
  /notrelife-sp-rj/ -> SP 0-18 R$ 216,80 | RJ 0-18 R$ 229,23 (individual por CPF,
     cesta ambulatorial + hospitalar com enfermaria; SP usa copay Tabela 2)
  /plano-hapvida-rio-de-janeiro/ -> R$ 113,69 EMPRESARIAL ambulatorial copart total
NAO entram na tabela de piso: produto e cesta diferentes."""
import io, re
SRC='artigos/plano-de-saude-barato_CORRIGIDO.html'
s=io.open(SRC,encoding='utf-8').read(); log=[]
def sub(tag,old,new,n=1):
    global s
    c=s.count(old); assert c==n, f"[{tag}] esperava {n}, achei {c}"
    s=s.replace(old,new); log.append(f"OK  {tag}")

# ---- 1. desduplicar o link do B6
sub('G1 remove link duplicado na mesma frase',
 ', vendido sob a marca do grupo naquelas praças — por isso o individual da marca Hapvida se concentra nos onze estados do Norte e do Nordeste, e em São Paulo e no Rio a porta de pessoa física é <a style="color: #ff6b00; font-weight: 600;" href="https://tabelaplanos.com.br/notrelife-sp-rj/">o NotreLife</a>.',
 ', vendido sob a marca do grupo naquelas praças. É por isso que o individual da marca Hapvida se concentra nos onze estados do Norte e do Nordeste: em São Paulo e no Rio a porta de pessoa física existe, mas atende por outro nome e com outra cesta.')

# ---- 2. inserir o bloco Sudeste
ANCORA=('<a style="color: #ff6b00; font-weight: 600;" href="https://tabelaplanos.com.br/plano-clinipam-curitiba/">'
        'a Clinipam continua operando</a> com marca própria.</p>')
P='style="text-align: justify!important; font-size: 18px; color: #4a5568; line-height: 1.7;"'
A='style="color: #ff6b00; font-weight: 600;"'
BLOCO = ANCORA + f'''

<h3 style="font-size: 19px; font-weight: 800; color: #1a202c; margin: 14px 0 8px 0;">São Paulo e Rio: o individual existe, mas não é o mesmo produto</h3>
<p {P}>Nas duas maiores praças do país a pessoa física contrata sem CNPJ — só que pela linha <a {A} href="https://tabelaplanos.com.br/notrelife-sp-rj/">NotreLife</a>, e o que ela entrega não é o produto do piso do Norte e do Nordeste. Pôr os dois preços lado a lado produz um número, e o número engana.</p>

<table style="width: 100%; border-collapse: collapse; margin-bottom: 16px; font-size: 16px;">
<thead>
<tr style="background: #16213e; color: #fff;">
<th style="padding: 12px 10px; text-align: left; font-weight: bold;">Praça</th>
<th style="padding: 12px 10px; text-align: right; font-weight: bold;">Entrada, 0 a 18 anos</th>
<th style="padding: 12px 10px; text-align: left; font-weight: bold;">O que está incluído</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid #f1f5f9;">
<td style="padding: 12px 10px; font-weight: bold; color: #1a202c;">São Paulo <span style="color: #94a3b8; font-weight: 500;">(SP)</span></td>
<td style="padding: 12px 10px; text-align: right; font-weight: 800; color: #ff6b00;">R$ 216,80</td>
<td style="padding: 12px 10px; color: #4a5568;">NotreLife individual: ambulatorial <strong>+ hospitalar com enfermaria</strong></td>
</tr>
<tr style="border-bottom: 1px solid #f1f5f9;">
<td style="padding: 12px 10px; font-weight: bold; color: #1a202c;">Rio de Janeiro <span style="color: #94a3b8; font-weight: 500;">(RJ)</span></td>
<td style="padding: 12px 10px; text-align: right; font-weight: 800; color: #ff6b00;">R$ 229,23</td>
<td style="padding: 12px 10px; color: #4a5568;">NotreLife individual Smart Rio, a mesma cesta</td>
</tr>
</tbody>
</table>
<p style="text-align: justify!important; font-size: 14px; color: #94a3b8; font-style: italic; margin-bottom: 20px;">Valores de referência de agosto de 2026, faixa 0 a 18 anos, publicados nas páginas de cada produto. <strong>Não são a mesma linha da tabela do topo desta página</strong>: aquela é ambulatorial pura, sem internação; esta cobre cirurgia e internação em enfermaria. A coparticipação de São Paulo também segue tabela própria, mais cara por uso que a das demais capitais.</p>

<p {P}>É por isso que "qual o plano de saúde mais barato do Brasil" não tem resposta única. Em Recife, o menor valor de entrada é um plano <strong>sem</strong> internação. Em São Paulo, o menor individual disponível já vem <strong>com</strong> internação embutida, e custa mais por causa disso. Não é a mesma compra, e comparar as duas mensalidades sem olhar a cesta é o erro mais comum dos rankings nacionais. No Rio, quem aceita o caminho do CNPJ encontra <a {A} href="https://tabelaplanos.com.br/plano-hapvida-rio-de-janeiro/">o empresarial ambulatorial a partir de R$ 113,69</a> — abaixo do individual da mesma cidade, que é exatamente a inversão que este guia mede.</p>'''

sub('F1 bloco Sudeste inserido', ANCORA, BLOCO)

# ---- integridade
assert s.count('notrelife-sp-rj')==2, s.count('notrelife-sp-rj')
assert 'plano-hapvida-rio-de-janeiro' in s
for m in re.finditer(r'<(style|script)>(.*?)</\1>',s,re.S):
    assert '<br' not in m.group(2) and '\n' not in m.group(2)
assert '2,38' not in s and '359017' not in s and s.count('badge-menor')==3
assert all(v in s for v in ['R$ 216,80','R$ 229,23','R$ 113,69'])
log.append("OK  G3 integridade mantida (links, style/script, numeros, badges)")

io.open(SRC,'w',encoding='utf-8').write(s)
print('\n'.join(log)); print(f"\n>> {len(s)} chars")
