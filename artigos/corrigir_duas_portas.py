# -*- coding: utf-8 -*-
"""ITEM 3 — a busca "plano de saude barato" abrange EMPRESARIAL/CNPJ, nao so
individual. Os concorrentes que ranqueiam vendem CNPJ como a resposta.
O topo do artigo estava enquadrado so no individual.

Valores empresariais VERIFICADOS na fila do cotador (coluna De, junho/2026):
  Fortaleza Hapvida PME 0-18 = R$ 107,83  (soma 10 faixas 2.708,59)
  Recife    Hapvida PME 0-18 = R$ 139,00  (soma 10 faixas 3.491,52)
Individual (shortcode do site): Fortaleza 159,53 | Recife 131,32."""
import io, re
SRC='artigos/plano-de-saude-barato_CORRIGIDO.html'
s=io.open(SRC,encoding='utf-8').read(); log=[]
def sub(tag,old,new,n=1):
    global s
    c=s.count(old); assert c==n, f"[{tag}] esperava {n}, achei {c}"
    s=s.replace(old,new); log.append(f"OK  {tag}")

P='style="text-align: justify!important; font-size: 18px; color: #4a5568; line-height: 1.7;"'

# H1 — etiqueta do heroi nomeia as duas portas
sub('H1 etiqueta do heroi',
 'Plano de Saúde Barato · piso medido em junho de 2026',
 'Plano de Saúde Barato · as duas portas, medidas em junho de 2026')

# H2 — o lead citavel passa a responder pelas DUAS modalidades
sub('H2 lead cobre individual e empresarial',
 'Não existe preço nacional: o piso muda de cidade e de idade. Das seis capitais que medimos, o menor valor de entrada é o de <strong style="color: #ff8533;">Recife</strong>, [recife_ind_ambulatorialtotal_0] por mês na faixa de 0 a 18 anos.',
 'Não existe preço nacional: o piso muda de cidade, de idade e da <strong style="color: #ff8533;">porta de contratação</strong>. Há duas: o individual, por CPF, e o empresarial, por CNPJ — e nem sempre a segunda é a mais barata. Cotando as duas na mesma semana, em Fortaleza o empresarial saiu na frente nas dez faixas etárias, a partir de <strong style="color: #ff8533;">R$ 107,83</strong>; em Recife venceu em apenas três, e o individual entra a [recife_ind_ambulatorialtotal_0].')

# H3 — subtitulo da secao de preco
sub('H3 subtitulo da secao de preco',
 'O piso de entrada em seis capitais, na mesma configuração.',
 'O piso do individual em seis capitais — e, logo abaixo, o do empresarial.')

# H4 — paragrafo de abertura da tabela declara que ha duas tabelas
sub('H4 abertura declara as duas portas',
 'O plano de saúde mais barato não tem um preço nacional: tem um piso por praça. Nas capitais onde a Hapvida vende o plano individual, o valor de entrada da primeira faixa etária muda de cidade para cidade, na mesma configuração: ambulatorial, com coparticipação total. A tabela abaixo mostra o piso de cada uma.',
 'O plano de saúde mais barato não tem um preço nacional: tem um piso por praça <em>e</em> por porta de contratação. Quem procura o menor valor tem dois caminhos — contratar como pessoa física (CPF) ou por um CNPJ, inclusive MEI. A tabela abaixo traz o piso do <strong>individual</strong> nas capitais onde ele é vendido, na mesma configuração: ambulatorial, com coparticipação total. Logo depois vem o piso do <strong>empresarial</strong> nas duas praças em que cotamos as duas portas lado a lado.')

# H5 — legenda da tabela de capitais + nova tabela do empresarial
ANTIGA=('Valor de entrada do plano individual, faixa 0 a 18 anos, ambulatorial com coparticipação total. '
        'O individual e familiar é comercializado nos 11 estados do Norte e Nordeste; nas demais regiões, '
        'o que está à venda é o empresarial.</p>')
NOVA=('Valor de entrada do plano <strong>individual</strong>, faixa 0 a 18 anos, ambulatorial com coparticipação total. '
 'O individual e familiar é comercializado nos 11 estados do Norte e Nordeste; nas demais regiões, o que está à venda é o empresarial.</p>\n\n'
 f'<h3 style="font-size: 19px; font-weight: 800; color: #1a202c; margin: 22px 0 8px 0;">O mesmo piso, pela porta do CNPJ</h3>\n'
 f'<p {P}>Boa parte de quem procura plano barato acaba no empresarial, e com razão: com um CNPJ — MEI serve — a tabela costuma começar mais baixo. Costuma, não sempre. Cotamos as duas portas da mesma operadora, na mesma semana e na mesma configuração, em duas capitais:</p>\n\n'
 '<table style="width: 100%; border-collapse: collapse; margin-bottom: 16px; font-size: 16px;">\n<thead>\n'
 '<tr style="background: #16213e; color: #fff;">\n'
 '<th style="padding: 12px 10px; text-align: left; font-weight: bold;">Capital</th>\n'
 '<th style="padding: 12px 10px; text-align: right; font-weight: bold;">Individual (CPF)</th>\n'
 '<th style="padding: 12px 10px; text-align: right; font-weight: bold;">Empresarial (CNPJ)</th>\n'
 '<th style="padding: 12px 10px; text-align: left; font-weight: bold;">Quem entra mais barato</th>\n</tr>\n</thead>\n<tbody>\n'
 '<tr style="border-bottom: 1px solid #f1f5f9; background: #fff8f3;">\n'
 '<td style="padding: 12px 10px; font-weight: 800; color: #1a202c;">Fortaleza <span style="color: #94a3b8; font-weight: 500;">(CE)</span></td>\n'
 '<td style="padding: 12px 10px; text-align: right; color: #4a5568;">[fortaleza_ind_ambulatorialtotal_0]</td>\n'
 '<td style="padding: 12px 10px; text-align: right; font-weight: 800; color: #ff6b00;">R$ 107,83<span class="badge-menor">menor</span></td>\n'
 '<td style="padding: 12px 10px; color: #4a5568;">O CNPJ, nas <strong>dez</strong> faixas etárias</td>\n</tr>\n'
 '<tr style="border-bottom: 1px solid #f1f5f9;">\n'
 '<td style="padding: 12px 10px; font-weight: bold; color: #1a202c;">Recife <span style="color: #94a3b8; font-weight: 500;">(PE)</span></td>\n'
 '<td style="padding: 12px 10px; text-align: right; font-weight: 800; color: #ff6b00;">[recife_ind_ambulatorialtotal_0]</td>\n'
 '<td style="padding: 12px 10px; text-align: right; color: #4a5568;">R$ 139,00</td>\n'
 '<td style="padding: 12px 10px; color: #4a5568;">O CPF, em <strong>sete</strong> das dez faixas</td>\n</tr>\n'
 '</tbody>\n</table>\n'
 '<p style="text-align: justify!important; font-size: 14px; color: #94a3b8; font-style: italic; margin-bottom: 0;">'
 'Cotação própria da Hapvida, junho de 2026, coluna De, faixa 0 a 18 anos, ambulatorial com coparticipação total nas duas portas. '
 'O empresarial cotado é o de menor porte (Super Simples/MEI). A coluna do individual vem da tabela vigente de cada praça. '
 'Em Recife o individual entra mais barato na primeira faixa; o empresarial só vence dos 19 aos 33 anos.</p>')
sub('H5 tabela das duas portas (Fortaleza e Recife)', ANTIGA, NOVA)

# integridade
assert s.count('badge-menor')==4, s.count('badge-menor')
for m in re.finditer(r'<(style|script)>(.*?)</\1>',s,re.S):
    assert '<br' not in m.group(2) and '\n' not in m.group(2)
assert 'R$ 107,83' in s and 'R$ 139,00' in s
log.append("OK  H6 integridade mantida")
io.open(SRC,'w',encoding='utf-8').write(s)
print('\n'.join(log)); print(f"\n>> {len(s)} chars")
