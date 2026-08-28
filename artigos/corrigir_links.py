# -*- coding: utf-8 -*-
"""Correcoes sobre a versao editada pelo usuario.

A) Bugs da edicao do usuario:
   A1 heroi recebeu [belo-horizonte_emp_ambulatorialtotal], que pelo
      shortcodes.md renderiza a TABELA INTEIRA dentro da linha de 34px.
      O correto para valor unico e [belo-horizonte_menorvalor].
   A2 a linha de apoio do heroi continuou dizendo "em Fortaleza".
   A3 "a praca mais barata entre as que cotamos" nao vale para BH: BH esta
      'pendente' na fila do cotador. Cotamos Fortaleza e Recife.

B) Links internos (SKILL.md 'Espacamento e Limites' + artigo-pillar-produto.md):
   - min 150 palavras entre dois links internos, nunca em paragrafos seguidos
   - cada URL no maximo 1x
   - pillar: 8 min / 12-16 alvo / 16 referencia  -> estava com 31 (29 unicos)
"""
import io, re
SRC='artigos/plano-de-saude-barato_USUARIO.html'
DST='artigos/plano-de-saude-barato_FINAL.html'
s=io.open(SRC,encoding='utf-8').read(); log=[]
def sub(tag,old,new,n=1):
    global s
    c=s.count(old); assert c==n, f"[{tag}] esperava {n}, achei {c}"
    s=s.replace(old,new); log.append(f"OK  {tag}")

# ---------------- A. bugs da edicao
sub('A1 heroi: valor unico, nao tabela inteira',
 'A partir de <span style="color: #ff8533;">[belo-horizonte_emp_ambulatorialtotal]</span>/mês',
 'A partir de <span style="color: #ff8533;">[belo-horizonte_menorvalor]</span>/mês')
sub('A2 linha de apoio do heroi bate com BH',
 'em Fortaleza, a praça mais barata entre as que cotamos — e pela porta do CNPJ',
 'em Belo Horizonte, a praça de menor valor de entrada da nossa tabela, pela porta do CNPJ')
sub('A3 BH nao foi cotada: ajusta a afirmacao',
 'A tabela abaixo é a de Belo Horizonte, a praça mais barata entre as que cotamos, na configuração de menor mensalidade: ambulatorial, com coparticipação total.',
 'A tabela abaixo é a de Belo Horizonte, a praça com o menor valor de entrada entre as que acompanhamos, na configuração de menor mensalidade: ambulatorial, com coparticipação total.')

# ---------------- B. links
# B1 grade de 11 cidades: 11 links a 8 palavras de distancia. Vira texto,
# com a rota unica para o hub de cidades (que ja existia mais abaixo).
i=s.find('<div class="grid3"')
j=s.find('</div>', s.find('Aracaju', i))+len('</div>')
assert 0 < i < j and s[i:j].count('<a ')==11, s[i:j].count('<a ')
s=s[:i]+('<p style="text-align: justify!important; font-size: 18px; color: #4a5568; line-height: 1.7;">'
 'Cada praça tem tabela e rede próprias, e a página de cada cidade traz a tabela completa por faixa etária, '
 'com a lista de unidades daquela praça. A rota para todas elas está em '
 '<a style="color: #ff6b00; font-weight: 600;" href="https://tabelaplanos.com.br/hapvida-cidades/">'
 'nossa lista de cidades atendidas, estado por estado</a>.</p>')+s[j:]
log.append("OK  B1 grade de 11 links vira texto + 1 rota para o hub")

# B2 paragrafo "Como achar o piso": 7 links em ~100 palavras -> 2, espacados
sub('B2 paragrafo de rotas enxugado',
 'O preço de entrada de cada praça está nas páginas de cidade, com a tabela local. Vale conferir <a style="color: #ff6b00; font-weight: 600;" href="https://tabelaplanos.com.br/plano-hapvida-rio-de-janeiro/">como o piso se comporta no Rio de Janeiro</a>, <a style="color: #ff6b00; font-weight: 600;" href="https://tabelaplanos.com.br/plano-hapvida-goiania/">quem contrata em Goiânia</a>, o Norte, onde a rede própria é mais densa, <a style="color: #ff6b00; font-weight: 600;" href="https://tabelaplanos.com.br/plano-de-saude-bh/">o que muda em Belo Horizonte, que tem tabela própria</a> ou <a style="color: #ff6b00; font-weight: 600;" href="https://tabelaplanos.com.br/plano-de-saude-em-recife/">o comparativo de operadoras em Recife</a>, a praça que cotamos aqui.</p>\n<p style="text-align: justify!important; font-size: 18px; color: #4a5568; line-height: 1.7;">Para ver todas as praças de uma vez, temos <a style="color: #ff6b00; font-weight: 600;" href="https://tabelaplanos.com.br/hapvida-cidades/">a lista de cidades atendidas, estado por estado</a>. E se você quer a tabela por faixa etária de uma praça específica, <a style="color: #ff6b00; font-weight: 600;" href="https://tabelaplanos.com.br/tabela-hapvida-fortaleza/">a de Fortaleza está publicada na íntegra</a>.</p>',
 'O preço de entrada de cada praça está na página da própria cidade, com a tabela local e a rede daquela praça. Onde a rede própria é mais densa, o desconto do modelo aparece inteiro; onde ela é rarefeita, o preço se aproxima do das operadoras tradicionais. Vale começar por <a style="color: #ff6b00; font-weight: 600;" href="https://tabelaplanos.com.br/plano-de-saude-bh/">o que muda em Belo Horizonte, que tem tabela própria</a>, porque é a praça de menor entrada nesta página.</p>\n'
 '<p style="text-align: justify!important; font-size: 18px; color: #4a5568; line-height: 1.7;">Depois, compare com uma praça onde a medição foi feita operadora por operadora. Foi o caso de <a style="color: #ff6b00; font-weight: 600;" href="https://tabelaplanos.com.br/plano-de-saude-em-recife/">Recife, que cotamos aqui</a>, e é lá que a inversão entre as duas portas de contratação aparece com mais clareza.</p>')

# B3 URLs repetidas (regra: cada URL 1x)
n=s.count('href="https://tabelaplanos.com.br/notrelife-sp-rj/"')
assert n==2, n
i2=s.rfind('<a style="color: #ff6b00; font-weight: 600;" href="https://tabelaplanos.com.br/notrelife-sp-rj/">NotreLife</a>')
s=s[:i2]+'NotreLife'+s[i2+len('<a style="color: #ff6b00; font-weight: 600;" href="https://tabelaplanos.com.br/notrelife-sp-rj/">NotreLife</a>'):]
log.append("OK  B3 /notrelife-sp-rj/ agora 1x (2a ocorrencia vira texto)")

n=s.count('href="https://tabelaplanos.com.br/plano-hapvida-rio-de-janeiro/"')
assert n==1, f"rio: {n}"
log.append("OK  B4 /plano-hapvida-rio-de-janeiro/ ja esta 1x")

io.open(DST,'w',encoding='utf-8').write(s)
print('\n'.join(log)); print(f"\n>> {len(s)} chars -> {DST}")
