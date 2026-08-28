# -*- coding: utf-8 -*-
"""Etapa 4: publica tambem o ranking de Fortaleza (agora que a base e uniforme)
e ajusta a frase do limiar. Fortaleza, empresarial, soma das 10 faixas:
Hapvida 2.708,59 = 1,00x | Unimed 4.132,29 = 1,53x | SulAmerica 5.113,78 = 1,89x
| Amil 5.419,41 = 2,00x. Ordem identica a de Recife."""
import io
SRC='artigos/plano-de-saude-barato_CORRIGIDO.html'
s=io.open(SRC,encoding='utf-8').read(); log=[]
def sub(tag,old,new,n=1):
    global s
    c=s.count(old); assert c==n, f"[{tag}] esperava {n}, achei {c}"
    s=s.replace(old,new); log.append(f"OK  {tag}")

# E1 — a caixa dizia que Fortaleza nao tinha base uniforme. Tem: as quatro
# cotacoes de Fortaleza sao empresariais. Publicar o ranking e ganho de informacao.
sub('E1 caixa Importante: publica Fortaleza',
 'Este ranking vale para Recife. Em Fortaleza cotamos as mesmas quatro operadoras, mas as cotações não saíram todas na mesma coluna de tabela, e por isso não publicamos ranking entre operadoras daquela praça. Comparar preço fora de uma base uniforme produz número, não resposta.',
 'Rodamos a mesma conta em Fortaleza, na mesma modalidade: Hapvida 1,00×, Unimed 1,53×, SulAmérica 1,89× e Amil 2,00×. <strong>A ordem é a mesma de Recife</strong> — o que muda entre as duas praças é a distância entre elas e, sobretudo, qual porta de contratação sai na frente. Por isso o ranking entre operadoras não substitui a comparação entre individual e empresarial: é a segunda que se inverte de uma cidade para a outra.')

# E2 — legenda da tabela de modalidades dizia que Fortaleza ficou de fora
sub('E2 legenda sem a ressalva obsoleta',
 'A comparação entre operadoras de Fortaleza não entrou aqui por não ter base uniforme.',
 'O ranking entre as quatro operadoras de cada praça está na seção seguinte.')

# E3 — sobra de redacao apos remover o limiar inventado
sub('E3 frase do limiar',
 'Há um limiar prático: a conta é sua e dá para fazer antes de assinar.',
 'O ponto de virada existe, mas é seu, não do mercado — e dá para calcular antes de assinar.')

io.open(SRC,'w',encoding='utf-8').write(s)
print('\n'.join(log)); print(f"\n>> {len(s)} chars")
