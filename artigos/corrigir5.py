# -*- coding: utf-8 -*-
"""Item 2 — entrada do Sudeste na pagina, SEM misturar base.
Apurado nos artigos irmaos publicados (agosto/2026):
  /notrelife-sp-rj/  -> SP 0-18 = R$ 216,80 | RJ 0-18 = R$ 229,23 (individual, CPF)
  /plano-hapvida-rio-de-janeiro/ -> R$ 113,69 e EMPRESARIAL ambulatorial copart. total
O NotreLife tem cesta ambulatorial+hospitalar com enfermaria e tabela de copay
propria (SP = Tabela 2). Por isso entra em bloco separado, nao na tabela de piso."""
import io
SRC='artigos/plano-de-saude-barato_CORRIGIDO.html'
s=io.open(SRC,encoding='utf-8').read(); log=[]

ANCORA=('<a style="color: #ff6b00; font-weight: 600;" href="https://tabelaplanos.com.br/plano-clinipam-curitiba/">'
        'a Clinipam continua operando</a> com marca própria.</p>')
assert s.count(ANCORA)==1

BLOCO = ANCORA + '''

<h3 style="font-size: 19px; font-weight: 800; color: #1a202c; margin: 14px 0 8px 0;">São Paulo e Rio: o individual existe, mas não é o mesmo produto</h3>
<p style="text-align: justify!important; font-size: 18px; color: #4a5568; line-height: 1.7;">Nas duas maiores praças do país a pessoa física consegue contratar sem CNPJ — só que pela linha <a style="color: #ff6b00; font-weight: 600;" href="https://tabelaplanos.com.br/notrelife-sp-rj/">NotreLife</a>, e o que ela entrega não é o mesmo produto do piso do Norte e do Nordeste. Comparar os dois preços lado a lado dá um número, e o número engana.</p>

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
<td style="padding: 12px 10px; color: #4a5568;">NotreLife individual, ambulatorial <strong>+ hospitalar com enfermaria</strong></td>
</tr>
<tr style="border-bottom: 1px solid #f1f5f9;">
<td style="padding: 12px 10px; font-weight: bold; color: #1a202c;">Rio de Janeiro <span style="color: #94a3b8; font-weight: 500;">(RJ)</span></td>
<td style="padding: 12px 10px; text-align: right; font-weight: 800; color: #ff6b00;">R$ 229,23</td>
<td style="padding: 12px 10px; color: #4a5568;">NotreLife individual Smart Rio, mesma cesta</td>
</tr>
</tbody>
</table>
<p style="text-align: justify!important; font-size: 14px; color: #94a3b8; font-style: italic; margin-bottom: 20px;">Valores de referência de agosto de 2026, faixa 0 a 18 anos, publicados nas páginas de cada produto. Não são a mesma linha da tabela de piso no topo desta página: aquela é ambulatorial pura, sem internação; esta cobre cirurgia e internação em enfermaria. E a coparticipação de São Paulo segue tabela própria, mais cara por uso que a das demais capitais.</p>

<p style="text-align: justify!important; font-size: 18px; color: #4a5568; line-height: 1.7;">É por isso que a pergunta "qual o plano de saúde mais barato do Brasil" não tem resposta única: em Recife o menor valor de entrada é um plano sem internação; em São Paulo, o menor individual disponível já vem com internação embutida e custa mais por causa disso. Não é a mesma compra. No Rio, quem aceita o caminho do CNPJ encontra <a style="color: #ff6b00; font-weight: 600;" href="https://tabelaplanos.com.br/plano-hapvida-rio-de-janeiro/">o empresarial ambulatorial a partir de R$ 113,69</a> — abaixo do individual da mesma cidade, que é a inversão que este guia mede.</p>'''

s=s.replace(ANCORA,BLOCO)
log.append("OK  F1 bloco Sudeste (SP/RJ) inserido em base declarada, fora da tabela de piso")

# o sumario ganha coerencia: a secao 6 ja se chama "Onde o individual mais barato e vendido"
assert 'São Paulo e Rio: o individual existe' in s
assert s.count('notrelife-sp-rj')==2, f"links notrelife: {s.count('notrelife-sp-rj')}"
assert 'plano-hapvida-rio-de-janeiro' in s
log.append("OK  F2 links para /notrelife-sp-rj/ e /plano-hapvida-rio-de-janeiro/")

io.open(SRC,'w',encoding='utf-8').write(s)
print('\n'.join(log)); print(f"\n>> {len(s)} chars")
