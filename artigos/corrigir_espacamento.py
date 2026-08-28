# -*- coding: utf-8 -*-
"""Zera as 5 violacoes de espacamento restantes (min 150 palavras entre links).
Estrategia: reposicionar, nao so apagar — cada link removido de um aglomerado
volta num ponto onde o tema o pede e a distancia permite."""
import io, re, html
SRC='artigos/plano-de-saude-barato_FINAL.html'
s=io.open(SRC,encoding='utf-8').read(); log=[]
A='style="color: #ff6b00; font-weight: 600;"'
def sub(tag,old,new,n=1):
    global s
    c=s.count(old); assert c==n, f"[{tag}] esperava {n}, achei {c}"
    s=s.replace(old,new); log.append(f"OK  {tag}")

# C1 — BH ganha link onde a tabela dele esta (palavra ~200), longe do proximo
sub('C1 link de BH junto da tabela de BH',
 'A tabela abaixo é a de Belo Horizonte, a praça com o menor valor de entrada entre as que acompanhamos,',
 f'A tabela abaixo é a de <a {A} href="https://tabelaplanos.com.br/plano-de-saude-bh/">Belo Horizonte</a>, a praça com o menor valor de entrada entre as que acompanhamos,')

# C2 — e sai do aglomerado de "Como achar o piso"
sub('C2 remove BH do aglomerado',
 f'Vale começar por <a {A} href="https://tabelaplanos.com.br/plano-de-saude-bh/">o que muda em Belo Horizonte, que tem tabela própria</a>, porque é a praça de menor entrada nesta página.',
 'Vale começar pela praça de menor entrada desta página, cuja tabela está logo no topo.')

# C3 — NotreLife: o link vale mais no bloco do Sudeste, onde ha SP e RJ na mesa
sub('C3 desfaz o link de NotreLife na secao de produto',
 f'<a {A} href="https://tabelaplanos.com.br/notrelife-sp-rj/">NotreLife</a>, vendido sob a marca do grupo',
 'NotreLife, vendido sob a marca do grupo')
sub('C4 e devolve o link no bloco do Sudeste',
 'só que pela linha NotreLife, e o que ela entrega',
 f'só que pela linha <a {A} href="https://tabelaplanos.com.br/notrelife-sp-rj/">NotreLife</a>, e o que ela entrega')

# C5 — ancora fraca colada em outro link
sub('C5 rede credenciada vira texto',
 f'<a {A} href="https://tabelaplanos.com.br/rede-credenciada-hapvida/">somados aos hospitais credenciados de cada praça</a>',
 'somados aos hospitais credenciados de cada praça')

# C6 — portabilidade estava a 46 palavras do link de coparticipacao
sub('C6 portabilidade vira texto',
 f'<a {A} href="https://tabelaplanos.com.br/portabilidade-para-hapvida/">portabilidade de carências</a>',
 'portabilidade de carências')

io.open(SRC,'w',encoding='utf-8').write(s)
print('\n'.join(log))
