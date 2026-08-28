# -*- coding: utf-8 -*-
"""ORDEM P3^ da v7 (references/preco-primeiro.md, secao 'Pillar (P1-P9)'):
   1 = P3^a: H2 de preco + contexto + SHORTCODE DA TABELA
   2 = Sumario (colado na tabela; entre as duas so cabe a frase de leitura)
   3 = P3^b: formulario + analise de preco + imagem por ultimo

Estava errado: eu tinha a tabela comparativa de 9 pracas (feita de valores
pontuais _0, que a trava explicitamente NAO conta como tabela) na posicao 1,
e o shortcode de tabela completa la embaixo. Move a comparativa para o P3^b
e poe [fortaleza_emp_ambulatorialtotal] na posicao 1."""
import io, re
SRC='artigos/plano-de-saude-barato_CORRIGIDO.html'
s=io.open(SRC,encoding='utf-8').read(); log=[]
P='style="text-align: justify!important; font-size: 18px; color: #4a5568; line-height: 1.7;"'
CAP='style="text-align: justify!important; font-size: 14px; color: #94a3b8; font-style: italic; margin-bottom: 20px;"'

# ---- 1. recortar o bloco comparativo (tabela 9 pracas + legenda + paragrafo)
ini=s.find('<table style="width: 100%; border-collapse: collapse; margin-bottom: 16px; font-size: 16px;">')
fim=s.find('a comparação direta entre as colunas vale onde as duas são do mesmo produto.</p>')
assert 0 < ini < fim
fim=s.find('</p>',fim)+4
# inclui o paragrafo "Os dois caminhos..." que vem logo depois
f2=s.find('Onde as duas colunas existem no mesmo produto, a comparação vale, e foi ela que cotamos.</p>')
if f2>0: fim=max(fim, s.find('</p>',f2)+4)
BLOCO=s[ini:fim]
assert '[fortaleza_emp_ambulatorialtotal_0]' in BLOCO and '[sao-paulo_emp_ambulatorialtotal_0]' in BLOCO
s=s[:ini]+s[fim:]
log.append(f"OK  M1 bloco comparativo recortado ({len(BLOCO)} chars)")

# ---- 2. na posicao 1: contexto curto + shortcode de tabela completa + frase de leitura
sub_old='O plano de saúde mais barato não tem preço nacional: tem valor de entrada por praça e por porta de contratação. A tabela traz as duas lado a lado em nove praças, na mesma configuração: faixa de 0 a 18 anos, ambulatorial, com coparticipação total.</p>'
assert s.count(sub_old)==1
sub_new=('O plano de saúde mais barato não tem preço nacional: tem valor de entrada por praça, por faixa etária e por porta de contratação. A tabela abaixo é a de Fortaleza, a praça mais barata entre as que cotamos, na configuração de menor mensalidade: ambulatorial, com coparticipação total.</p>\n'
 '[fortaleza_emp_ambulatorialtotal]\n'
 f'<p {CAP}>Cada faixa etária tem seu próprio valor: a ANS divide o preço em dez faixas e permite que a última custe até seis vezes a primeira. Confira em qual faixa você entra antes de comparar praças.</p>')
s=s.replace(sub_old,sub_new)
log.append("OK  M2 [fortaleza_emp_ambulatorialtotal] na posicao 1, antes do sumario")

# ---- 3. reinserir o comparativo no P3^b, depois dos selos de confianca
anc='Três coisas explicam'
i=s.find(anc); assert i>0
ini_p=s.rfind('<p ',0,i)
NOVO=(f'<h3 style="font-size: 19px; font-weight: 800; color: #1a202c; margin: 14px 0 8px 0;">As duas portas, praça por praça</h3>\n'
 f'<p {P}>Quem procura o menor preço tem dois caminhos: contratar como pessoa física, pelo CPF, ou por um CNPJ, e o MEI serve. Raramente os dois aparecem lado a lado. Abaixo estão, em nove praças, sempre na faixa de 0 a 18 anos e na mesma configuração.</p>\n'
 + BLOCO + '\n')
s=s[:ini_p]+NOVO+s[ini_p:]
log.append("OK  M3 comparativo reinserido no P3^b (depois do formulario e dos selos)")

for m in re.finditer(r'<(style|script)>(.*?)</\1>',s,re.S):
    assert '<br' not in m.group(2) and '\n' not in m.group(2)
corpo=re.sub(r'<(script|style)>.*?</\1>','',s,flags=re.S)
assert not re.findall(r'R\$\s?\d+,\d{2}',corpo)
io.open(SRC,'w',encoding='utf-8').write(s)
print('\n'.join(log)); print(f"\n>> {len(s)} chars")
