# -*- coding: utf-8 -*-
"""Etapa 2: refaz o ranking entre operadoras em BASE UNIFORME.
Problema: o indice 1,84 / 2,07 / 2,38 punha a Hapvida como INDIVIDUAL AMBULATORIAL
(soma 3.103,33) contra concorrentes em EMPRESARIAL COM INTERNACAO (Amil Prata
Enfermaria, SulAmerica Hospitalar Especial 100 RC Apartamento, Unimed UniFlex
Enfermaria). Na base uniforme — todas empresariais, soma das 10 faixas — o indice
real e: Hapvida 3.491,52 = 1,00x | Unimed 5.719,51 = 1,64x | SulAmerica 6.433,59
= 1,84x | Amil 7.378,19 = 2,11x."""
import re, io
SRC='artigos/plano-de-saude-barato_CORRIGIDO.html'
s=io.open(SRC,encoding='utf-8').read(); log=[]
def sub(tag,old,new,n=1):
    global s
    c=s.count(old); assert c==n, f"[{tag}] esperava {n}, achei {c}"
    s=s.replace(old,new); log.append(f"OK  {tag}")

# C1 — paragrafo de abertura do ranking
sub('C1 abertura do ranking em base uniforme',
 'Em Recife, cotamos as quatro maiores operadoras na mesma semana de junho de 2026 e somamos as dez faixas etárias de cada uma. A distância entre a primeira e a última é maior do que os comparativos de mercado costumam sugerir: a mais cara pediu 2,38 vezes o que a mais barata pediu, pelo mesmo perfil e no mesmo mês.',
 'Em Recife, cotamos as quatro maiores operadoras na mesma semana de junho de 2026 e somamos as dez faixas etárias de cada uma. Para o ranking abaixo colocamos as quatro na mesma modalidade — empresarial com coparticipação, o menor plano de cada uma —, porque é a única base que as quatro têm em comum. Nela, a mais cara pediu <strong>2,11 vezes</strong> o que a mais barata pediu, no mesmo mês e na mesma praça.')

# C2 — indices da tabela
sub('C2 indice Unimed','>1,84×</td>','>1,64×</td>')
sub('C2 indice SulAmerica','>2,07×</td>','>1,84×</td>')
sub('C2 indice Amil','>2,38×</td>','>2,11×</td>')

# C3 — legenda da tabela: declarar a base e o que ela NAO diz
sub('C3 legenda honesta do ranking',
 'Cotação própria em Recife, junho de 2026, menor plano de cada operadora, as quatro na mesma coluna de tabela. O índice é sobre a soma das dez faixas etárias, não sobre uma faixa isolada. Os valores em reais de cada praça ficam nas tabelas locais.',
 'Cotação própria em Recife, junho de 2026, coluna De, menor plano <strong>empresarial com coparticipação</strong> de cada operadora — as quatro na mesma modalidade. O índice é sobre a soma das dez faixas etárias, não sobre uma faixa isolada. Não é o mesmo recorte da tabela de entrada mais acima, em que a linha da Hapvida é o plano individual ambulatorial: comparar aquela linha com estas produziria uma distância maior e falsa, porque os planos das outras três incluem internação.')

# C4/C5 — FAQs que repetiam o numero antigo
sub('C4 FAQ2 em base uniforme',
 'Em Recife, a faixa de 0 a 18 anos entra em [recife_ind_ambulatorialtotal_0] na operadora mais barata. Somadas as dez faixas, a mais cara da mesma praça pediu 2,38 vezes isso, no mesmo mês e no mesmo perfil. A tabela completa está no topo desta página.',
 'Em Recife, a faixa de 0 a 18 anos entra em [recife_ind_ambulatorialtotal_0] no plano individual ambulatorial com coparticipação total. Colocando as quatro operadoras na mesma modalidade — empresarial com coparticipação — e somando as dez faixas, a mais cara da praça pediu 2,11 vezes o que a mais barata pediu. A tabela completa está no topo desta página.')
sub('C5 FAQ3 em base uniforme',
 'Em Recife a mesma configuração de entrada custou 2,38 vezes mais na operadora mais cara que na mais barata, com o mesmo Rol nas duas.',
 'Em Recife, com as quatro operadoras na mesma modalidade, a mais cara custou 2,11 vezes a mais barata, com o mesmo Rol nas duas.')

# C6 — subtitulo da secao mentia "uma coluna de tabela so"
sub('C6 subtitulo do ranking',
 'Quatro operadoras, uma praça, um mês, uma coluna de tabela só.',
 'Quatro operadoras, uma praça, um mês, todas na mesma modalidade.')

# C7 — tabela de entrada: declarar a segmentacao real de cada linha, que difere
for op,antigo,novo in [
 ('Unimed','Menor plano empresarial com coparticipação','Empresarial, hospitalar com enfermaria, coparticipação'),
 ('SulAmérica','Menor plano empresarial com coparticipação','Empresarial, hospitalar com apartamento, coparticipação'),
 ('Amil','Menor plano empresarial com coparticipação','Empresarial, hospitalar com enfermaria, coparticipação')]:
    pass
assert s.count('Menor plano empresarial com coparticipação')==3
s=s.replace('>Unimed</td>\n<td class="cel-preco" style="padding: 12px 10px; text-align: right; font-weight: bold; color: #4a5568;" data-grupo="operadoras">[unimed_recife_menorvalor]</td>\n<td style="padding: 12px 10px; color: #4a5568;">Menor plano empresarial com coparticipação</td>',
            '>Unimed</td>\n<td class="cel-preco" style="padding: 12px 10px; text-align: right; font-weight: bold; color: #4a5568;" data-grupo="operadoras">[unimed_recife_menorvalor]</td>\n<td style="padding: 12px 10px; color: #4a5568;">Empresarial, hospitalar com enfermaria, coparticipação</td>')
s=s.replace('>SulAmérica</td>\n<td class="cel-preco" style="padding: 12px 10px; text-align: right; font-weight: bold; color: #4a5568;" data-grupo="operadoras">[sulamerica_recife_menorvalor]</td>\n<td style="padding: 12px 10px; color: #4a5568;">Menor plano empresarial com coparticipação</td>',
            '>SulAmérica</td>\n<td class="cel-preco" style="padding: 12px 10px; text-align: right; font-weight: bold; color: #4a5568;" data-grupo="operadoras">[sulamerica_recife_menorvalor]</td>\n<td style="padding: 12px 10px; color: #4a5568;">Empresarial, hospitalar com apartamento, coparticipação</td>')
s=s.replace('>Amil</td>\n<td class="cel-preco" style="padding: 12px 10px; text-align: right; font-weight: bold; color: #4a5568;" data-grupo="operadoras">[amil_recife_menorvalor]</td>\n<td style="padding: 12px 10px; color: #4a5568;">Menor plano empresarial com coparticipação</td>',
            '>Amil</td>\n<td class="cel-preco" style="padding: 12px 10px; text-align: right; font-weight: bold; color: #4a5568;" data-grupo="operadoras">[amil_recife_menorvalor]</td>\n<td style="padding: 12px 10px; color: #4a5568;">Empresarial, hospitalar com enfermaria, coparticipação</td>')
assert s.count('Menor plano empresarial com coparticipação')==0, "as 3 linhas nao foram rotuladas"
log.append("OK  C7 segmentacao real declarada nas 3 linhas de concorrente")

assert '2,38' not in s, "sobrou 2,38 no artigo"
assert '2,07×' not in s and '1,84×' in s
io.open(SRC,'w',encoding='utf-8').write(s)
print('\n'.join(log)); print(f"\n>> {len(log)} correcoes | {len(s)} chars")
