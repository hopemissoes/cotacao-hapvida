# -*- coding: utf-8 -*-
"""Corrige o que as travas da v7 apontaram NA MINHA versao:
  - checkpoint_paragrafos: P1 (524) e P38 (553) acima do limite de 480
  - checkpoint_voz: densidade de travessao 4,1/1.000 (alvo <= 2)
  - checkpoint_preco_primeiro: reduzir texto antes da tabela
Regra-mae respeitada: mexe em palavra e ritmo, nunca em fato."""
import io, re
SRC='artigos/plano-de-saude-barato_CORRIGIDO.html'
s=io.open(SRC,encoding='utf-8').read(); log=[]
def sub(tag,old,new,n=1):
    global s
    c=s.count(old); assert c==n, f"[{tag}] esperava {n}, achei {c}"
    s=s.replace(old,new); log.append(f"OK  {tag}")

PL='style="text-align: justify!important; font-size: 18px; line-height: 1.7; color: #e2e8f0; margin-bottom: 16px;"'
O='color: #ff8533;'

# L1 — lead do heroi: 524 -> dois paragrafos, sem travessao
sub('L1 divide o lead do heroi',
 'Plano de saúde barato</strong> é o plano de entrada: cobre o Rol obrigatório da ANS, mas chega a esse preço cortando internação, abrangência ou livre escolha de médico. Não existe preço nacional: o piso muda de cidade, de idade e da <strong style="color: #ff8533;">porta de contratação</strong>. Há duas: o individual, por CPF, e o empresarial, por CNPJ — e nem sempre a segunda é a mais barata. Cotando as duas na mesma semana, em Fortaleza o caminho do CNPJ saiu na frente nas <strong style="color: #ff8533;">dez</strong> faixas etárias; em Recife, em apenas <strong style="color: #ff8533;">três</strong>. Mesma operadora, mesmo mês, resultado invertido.</p>',
 'Plano de saúde barato</strong> é o plano de entrada: cobre o Rol obrigatório da ANS, mas chega a esse preço cortando internação, abrangência ou livre escolha de médico. Não existe preço nacional: o valor de entrada muda de cidade, de idade e da <strong style="'+O+'">porta de contratação</strong>.</p>\n'
 f'<p {PL}>São duas portas: o individual, pelo CPF, e o empresarial, por um CNPJ. Nem sempre a segunda é a mais barata. Cotamos as duas na mesma semana e, em Fortaleza, o caminho do CNPJ saiu na frente nas <strong style="{O}">dez</strong> faixas etárias; em Recife, em apenas <strong style="{O}">três</strong>.</p>')

# L2 — paragrafo do bloco Sudeste: 553 -> dois, sem travessao
sub('L2 divide o paragrafo do Sudeste',
 'É por isso que "qual o plano de saúde mais barato do Brasil" não tem resposta única. Em Recife, o menor valor de entrada é um plano <strong>sem</strong> internação. Em São Paulo, o menor individual disponível já vem <strong>com</strong> internação embutida, e custa mais por causa disso. Não é a mesma compra, e comparar as duas mensalidades sem olhar a cesta é o erro mais comum dos rankings nacionais. No Rio, quem aceita o caminho do CNPJ encontra <a style="color: #ff6b00; font-weight: 600;" href="https://tabelaplanos.com.br/plano-hapvida-rio-de-janeiro/">o mesmo plano pela porta do CNPJ a partir de [rio-de-janeiro_menorvalor]</a> — abaixo do individual da mesma cidade, que é exatamente a inversão que este guia mede.</p>',
 'É por isso que "qual o plano de saúde mais barato do Brasil" não tem resposta única. Em Recife, o menor valor de entrada é um plano <strong>sem</strong> internação. Em São Paulo, o menor individual disponível já vem <strong>com</strong> internação embutida, e custa mais por causa disso. Não é a mesma compra.</p>\n'
 '<p style="text-align: justify!important; font-size: 18px; color: #4a5568; line-height: 1.7;">Comparar as duas mensalidades sem olhar a cesta é o erro mais comum dos rankings nacionais. No Rio, quem aceita o caminho do CNPJ encontra <a style="color: #ff6b00; font-weight: 600;" href="https://tabelaplanos.com.br/plano-hapvida-rio-de-janeiro/">o mesmo plano a partir de [rio-de-janeiro_menorvalor]</a>, abaixo do individual da mesma cidade. É exatamente a inversão que este guia mede.</p>')

# L3 — enxugar o texto antes da tabela (checkpoint_preco_primeiro)
sub('L3 abertura da secao mais curta',
 'O plano de saúde mais barato não tem um preço nacional: tem um valor de entrada por praça <em>e</em> por porta de contratação. Quem procura o menor preço tem dois caminhos — contratar como pessoa física, pelo CPF, ou por um CNPJ, e o MEI serve. A tabela abaixo traz os dois lado a lado em nove praças, sempre na mesma configuração: faixa de 0 a 18 anos, ambulatorial, com coparticipação total. A diferença entre as duas colunas é o que quase nenhum comparativo mostra.',
 'O plano de saúde mais barato não tem preço nacional: tem valor de entrada por praça e por porta de contratação. A tabela traz as duas lado a lado em nove praças, na mesma configuração: faixa de 0 a 18 anos, ambulatorial, com coparticipação total.')

# L4 — travessoes: trocar por virgula/dois-pontos onde nao muda o sentido
antes=s.count('—')
for a,b in [(' — e o MEI serve',', e o MEI serve'),
            (' — as quatro na mesma modalidade',', as quatro na mesma modalidade'),
            (' — o que muda entre as duas praças',': o que muda entre as duas praças'),
            (' — empresarial com coparticipação, o menor plano de cada uma —',', empresarial com coparticipação, o menor plano de cada uma,'),
            (' — a comparação direta entre as colunas vale',': a comparação direta entre as colunas vale'),
            (' — MEI serve — a tabela costuma começar mais baixo',', e o MEI serve, a tabela costuma começar mais baixo')]:
    if a in s: s=s.replace(a,b)
log.append(f"OK  L4 travessoes: {antes} -> {s.count('—')}")

for m in re.finditer(r'<(style|script)>(.*?)</\1>',s,re.S):
    assert '<br' not in m.group(2) and '\n' not in m.group(2)
corpo=re.sub(r'<(script|style)>.*?</\1>','',s,flags=re.S)
assert not re.findall(r'R\$\s?\d+,\d{2}',corpo)
io.open(SRC,'w',encoding='utf-8').write(s)
print('\n'.join(log)); print(f"\n>> {len(s)} chars")
