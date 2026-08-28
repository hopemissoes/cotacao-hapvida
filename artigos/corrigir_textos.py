# -*- coding: utf-8 -*-
"""Alinha os textos que ainda descreviam a estrutura antiga (duas tabelas
separadas, seis capitais) a estrutura nova (uma tabela, 9 pracas, duas colunas)."""
import io, re
SRC='artigos/plano-de-saude-barato_CORRIGIDO.html'
s=io.open(SRC,encoding='utf-8').read(); log=[]
def sub(tag,old,new,n=1):
    global s
    c=s.count(old); assert c==n, f"[{tag}] esperava {n}, achei {c}"
    s=s.replace(old,new); log.append(f"OK  {tag}")

sub('K1 subtitulo da secao',
 'O piso do individual em seis capitais — e, logo abaixo, o do empresarial.',
 'O valor de entrada em nove praças, pelas duas portas de contratação.')

sub('K2 abertura descreve a tabela nova',
 'O plano de saúde mais barato não tem um preço nacional: tem um piso por praça <em>e</em> por porta de contratação. Quem procura o menor valor tem dois caminhos — contratar como pessoa física (CPF) ou por um CNPJ, inclusive MEI. A tabela abaixo traz o piso do <strong>individual</strong> nas capitais onde ele é vendido, na mesma configuração: ambulatorial, com coparticipação total. Logo depois vem o piso do <strong>empresarial</strong> nas duas praças em que cotamos as duas portas lado a lado.',
 'O plano de saúde mais barato não tem um preço nacional: tem um valor de entrada por praça <em>e</em> por porta de contratação. Quem procura o menor preço tem dois caminhos — contratar como pessoa física, pelo CPF, ou por um CNPJ, e o MEI serve. A tabela abaixo traz os dois lado a lado em nove praças, sempre na mesma configuração: faixa de 0 a 18 anos, ambulatorial, com coparticipação total. A diferença entre as duas colunas é o que quase nenhum comparativo mostra.')

sub('K3 legenda da tabela nova',
 'Valor de entrada do plano <strong>individual</strong>, faixa 0 a 18 anos, ambulatorial com coparticipação total. O individual e familiar é comercializado nos 11 estados do Norte e Nordeste; nas demais regiões, o que está à venda é o empresarial.',
 'Valor de entrada na faixa de 0 a 18 anos, ambulatorial com coparticipação total, nas duas portas de contratação. Os valores acompanham a tabela vigente de cada praça e mudam com o reajuste. A contratação por pessoa física é comercializada nos onze estados do Norte e do Nordeste; nas demais praças, a coluna do CPF traz o produto individual disponível no grupo, que tem cesta própria — a comparação direta entre as colunas vale onde as duas são do mesmo produto.')

sub('K4 caixa "A tabela de cada praça"',
 'A tabela acima traz seis capitais. O individual é comercializado em onze estados do Norte e do Nordeste, e cada capital tem tabela e rede próprias. Abaixo, o caminho para a de cada uma.',
 'A tabela acima traz nove praças. Cada uma tem tabela e rede próprias, e a contratação por pessoa física é comercializada nos onze estados do Norte e do Nordeste. Abaixo, o caminho para a tabela completa de cada praça.')

for m in re.finditer(r'<(style|script)>(.*?)</\1>',s,re.S):
    assert '<br' not in m.group(2) and '\n' not in m.group(2)
corpo=re.sub(r'<(script|style)>.*?</\1>','',s,flags=re.S)
assert not re.findall(r'R\$\s?\d+,\d{2}',corpo), "preco fixo no corpo"
assert 'seis capitais' not in s
log.append("OK  K5 travas: sem preco fixo, sem 'seis capitais'")
io.open(SRC,'w',encoding='utf-8').write(s)
print('\n'.join(log)); print(f"\n>> {len(s)} chars")
