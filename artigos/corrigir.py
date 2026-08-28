# -*- coding: utf-8 -*-
"""Correcoes auditadas do artigo 'plano de saude barato' (tabelaplanos.com.br).
Toda troca eh asseverada: se o alvo nao existir, o script para em vez de
silenciosamente nao corrigir. Fonte dos numeros: fila do cotador no Supabase
(Fortaleza 23-24/jun/2026, Recife 25/jun/2026) e dados canonicos do banco."""
import re, io

SRC='artigos/plano-de-saude-barato_ORIGINAL.html'
DST='artigos/plano-de-saude-barato_CORRIGIDO.html'
s=io.open(SRC,encoding='utf-8').read(); log=[]

def sub(tag,old,new,n=1):
    global s
    c=s.count(old); assert c==n, f"[{tag}] esperava {n}, achei {c}"
    s=s.replace(old,new); log.append(f"OK  {tag}")

# ============================================================ A. QUEBRA NO AR
# O wpautop injeta <br /> e <p> a cada quebra de linha. Dentro de <style> isso
# matou 48 regras; dentro de <script> o primeiro <br /> eh erro de sintaxe e
# derrubou o JS INTEIRO (por isso as 6 capitais apareciam todas como "menor").
def colapsa(m):
    corpo=re.sub(r'/\*.*?\*/','',m.group(2),flags=re.S)
    corpo=re.sub(r'//[^\n]*','',corpo)
    corpo=re.sub(r'\s*\n\s*',' ',corpo)
    return m.group(1)+re.sub(r'\s{2,}',' ',corpo).strip()+m.group(3)
s=re.sub(r'(<style>)(.*?)(</style>)',colapsa,s,flags=re.S)
s=re.sub(r'(<script>)(.*?)(</script>)',colapsa,s,flags=re.S)
assert '\n' not in re.search(r'<style>(.*?)</style>',s,re.S).group(1)
assert '\n' not in re.search(r'<script>(.*?)</script>',s,re.S).group(1)
log.append("OK  A1 <style> em linha unica — imune ao wpautop")
log.append("OK  A2 <script> em linha unica — JS volta a rodar")

# A3: badge "menor" so no menor de verdade (Recife, R$ 131,32)
for c in ['fortaleza','salvador','belem','manaus','sao-luis']:
    sub(f'A3 badge fora de {c}',
        f'data-grupo="capitais">[{c}_ind_ambulatorialtotal_0]<span class="badge-menor">menor</span>',
        f'data-grupo="capitais">[{c}_ind_ambulatorialtotal_0]')

# ============================================================ B. FATOS
# B1 heroi anunciava Belem (161,35); o menor da propria tabela eh Recife (131,32)
sub('B1 heroi passa a mostrar o menor real',
 'A partir de <span style="color: #ff8533;">[belem_ind_ambulatorialtotal_0]</span>/mês',
 'A partir de <span style="color: #ff8533;">[recife_ind_ambulatorialtotal_0]</span>/mês')

# B2 lead vendia 2,38x apurado fora de base uniforme
sub('B2 lead citavel sem o 2,38x falso',
 '<strong style="color: #ff8533;">Plano de saúde barato</strong> é o plano de entrada: cobre o Rol obrigatório da ANS, mas chega a esse preço cortando internação, abrangência ou livre escolha de médico. Cotamos as quatro maiores operadoras em Recife em junho de 2026 e, somando as dez faixas, a mais cara pediu <strong style="color: #ff8533;">2,38 vezes</strong> o que a mais barata pediu.',
 '<strong style="color: #ff8533;">Plano de saúde barato</strong> é o plano de entrada: cobre o Rol obrigatório da ANS, mas chega a esse preço cortando internação, abrangência ou livre escolha de médico. Não existe preço nacional: o piso muda de cidade e de idade. Das seis capitais que medimos, o menor valor de entrada é o de <strong style="color: #ff8533;">Recife</strong>, [recife_ind_ambulatorialtotal_0] por mês na faixa de 0 a 18 anos.')

# B3 quadro de Recife trazia o multiplicador da Unimed de FORTALEZA (5,999)
sub('B3 multiplicador Unimed = 5,983 (Recife)',
 '<div style="font-size: 28px; font-weight: 900; color: #1a202c; margin-bottom: 4px;">5,999×</div>\n<div style="font-size: 13px; color: #718096;">Unimed</div>',
 '<div style="font-size: 28px; font-weight: 900; color: #1a202c; margin-bottom: 4px;">5,983×</div>\n<div style="font-size: 13px; color: #718096;">Unimed</div>')
sub('B3b faixa correta dos multiplicadores',
 'As quatro operam entre 5,873 e 5,9995,',
 'Em Recife, as quatro operam entre 5,873 e 5,9997,')

# B4 "multiplicador exato" nao vale para a SulAmerica (5,9995 F x 5,9997 R)
sub('B4 precisao do cruzamento entre pracas',
 'Cruzando as duas praças, Hapvida, Amil e SulAmérica repetiram o multiplicador exato de faixa nas duas capitais. Só a Unimed não repetiu: 5,999× em Fortaleza contra 5,983× em Recife.',
 'Cruzando as duas praças, Hapvida e Amil repetiram o multiplicador exato nas duas capitais (5,873× e 5,951×) e a SulAmérica variou só na quarta casa. Só a Unimed mudou de forma visível: 5,999× em Fortaleza contra 5,983× em Recife.')
sub('B4b resumo rapido coerente',
 'das quatro, três repetiram o mesmo multiplicador nas duas capitais. Uma variou.',
 'das quatro, três mantiveram na prática o mesmo multiplicador nas duas capitais. Só a Unimed mudou de forma visível.')

# B5 FAQ 1 afirmava que a ordem nao se repetiu. Ela SE REPETE nas duas pracas.
sub('B5 FAQ1 — a ordem se repete; o que inverte eh a porta',
 'Cotamos as quatro maiores operadoras em Fortaleza e em Recife na mesma semana de junho de 2026 e a ordem não se repetiu. Um ranking nacional único não descreve o que acontece na sua cidade.',
 'Cotamos as quatro maiores operadoras em Fortaleza e em Recife em junho de 2026. A ordem entre elas se repetiu nas duas praças, mas o valor de entrada e — principalmente — qual porta de contratação sai mais barata mudaram: em Fortaleza o empresarial venceu nas dez faixas etárias; em Recife, em apenas três. Um ranking nacional único não descreve o que acontece na sua cidade.')

# B6 contradicao: individual so no N/NE x NotreLife individual em SP e RJ
sub('B6 geografia do individual sem contradicao',
 'o único individual ainda aberto a pessoa física nas duas capitais.',
 'vendido sob a marca do grupo naquelas praças — por isso o individual da marca Hapvida se concentra nos onze estados do Norte e do Nordeste, e em São Paulo e no Rio a porta de pessoa física é <a style="color: #ff6b00; font-weight: 600;" href="https://tabelaplanos.com.br/notrelife-sp-rj/">o NotreLife</a>.')

# B7 selo com ANS de outra operadora (359017 = Notre Dame Intermedica) e DRV velha
sub('B7 selos: ANS incorreta fora, DRV atualizada',
 'Operadora registrada na ANS — nº 359017</span><span style="font-size: 12px; color: #64748b; font-weight: 600; border: 1px solid #e2e8f0; border-radius: 999px; padding: 6px 12px; background: #fff;">DRV: 10+ anos especialista Hapvida</span>',
 'Cotação própria — junho de 2026</span><span style="font-size: 12px; color: #64748b; font-weight: 600; border: 1px solid #e2e8f0; border-radius: 999px; padding: 6px 12px; background: #fff;">DRV: 11 anos especialista Hapvida, certificação Safira</span>')

# B8 ANS: os 53,1 mi sao de JUNHO/2026 (53.145.666), nao de maio
sub('B8 mes correto do dado da ANS',
 '53,1 milhões de beneficiários em assistência médica em maio de 2026, segundo a ANS.',
 '53,1 milhões de beneficiários em assistência médica em junho de 2026, segundo a ANS.')

# B9/B10 dados proprios nao verificaveis — removidos a pedido do dono
sub('B9 remove "sete em cada dez contratacoes"',
 'Sete em cada dez contratações que fechamos são com coparticipação total, e a maioria está na faixa de 19 a 38 anos. Faz sentido para quem usa pouco, e é a primeira coisa que revemos quando o cliente começa a usar mais.',
 'A coparticipação total é a escolha mais comum de quem chega buscando o menor valor de entrada, e é reversível: dá para rever a modalidade sem refazer o contrato quando o padrão de uso muda.')
sub('B10 remove limiar inventado de exames',
 'acima de dez exames por ano, a modalidade parcial costuma compensar mais que a total. Abaixo de cinco, a total ganha com folga. Entre os dois, depende do resto.',
 'a conta é sua e dá para fazer antes de assinar. Multiplique quantas consultas e exames você usou no último ano pelos valores acima e compare com a diferença de mensalidade entre a modalidade total e a parcial.')
sub('B10b remove o mesmo limiar na lista',
 'abaixo de cinco exames por ano, a coparticipação total ganha com folga.',
 'quanto menor o número de consultas e exames no ano, mais a coparticipação total compensa.')

io.open(DST,'w',encoding='utf-8').write(s)
print('\n'.join(log)); print(f"\n>> {len(log)} correcoes | {len(s)} chars -> {DST}")
