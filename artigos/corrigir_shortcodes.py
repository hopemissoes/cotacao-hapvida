# -*- coding: utf-8 -*-
"""Alinha o artigo ao references/shortcodes.md da v7:
  - REGRA DURA: nenhum preco fixo no artigo. Tudo por shortcode.
  - [cidade_menorvalor] = chamariz (empresarial copart total) -> heroi
  - [cidade_emp_ambulatorialtotal_0] / [cidade_ind_ambulatorialtotal_0] = valor
    pontual da faixa 0-18
Substitui a tabela de 2 pracas por uma tabela unica de 9 pracas com as duas
portas, incluindo Belo Horizonte, Sao Paulo e Rio (as que a SERP premia).
Remove os badges 'menor' fixos: com valor dinamico, rotulo fixo envelhece."""
import io, re
SRC='artigos/plano-de-saude-barato_CORRIGIDO.html'
s=io.open(SRC,encoding='utf-8').read(); log=[]
def sub(tag,old,new,n=1):
    global s
    c=s.count(old); assert c==n, f"[{tag}] esperava {n}, achei {c}"
    s=s.replace(old,new); log.append(f"OK  {tag}")

P='style="text-align: justify!important; font-size: 18px; color: #4a5568; line-height: 1.7;"'
TD='style="padding: 12px 10px;'

# ---------- 1. HEROI: chamariz canonico, sem preco fixo
sub('J1 heroi usa [fortaleza_menorvalor]',
 'A partir de <span style="color: #ff8533;">[recife_ind_ambulatorialtotal_0]</span>/mês</div>\n'
 '<div style="font-size: 15px; font-weight: 600; color: #94a3b8; margin-bottom: 18px;">'
 'no individual, por CPF — pela porta do CNPJ, medimos a partir de '
 '<span style="color: #e2e8f0; font-weight: 800;">R$ 107,83</span></div>',
 'A partir de <span style="color: #ff8533;">[fortaleza_menorvalor]</span>/mês</div>\n'
 '<div style="font-size: 15px; font-weight: 600; color: #94a3b8; margin-bottom: 18px;">'
 'em Fortaleza, a praça mais barata entre as que cotamos — e pela porta do CNPJ</div>')

sub('J2 lead sem preco fixo',
 'em Fortaleza o empresarial saiu na frente nas dez faixas etárias, a partir de <strong style="color: #ff8533;">R$ 107,83</strong>; em Recife venceu em apenas três, e o individual entra a [recife_ind_ambulatorialtotal_0].',
 'em Fortaleza o caminho do CNPJ saiu na frente nas <strong style="color: #ff8533;">dez</strong> faixas etárias; em Recife, em apenas <strong style="color: #ff8533;">três</strong>. Mesma operadora, mesmo mês, resultado invertido.')

# ---------- 2. TABELA UNICA: 9 pracas x 2 portas, tudo em shortcode
CIDADES=[('Fortaleza','CE','fortaleza'),('Recife','PE','recife'),('Salvador','BA','salvador'),
         ('Belém','PA','belem'),('Manaus','AM','manaus'),('São Luís','MA','sao-luis'),
         ('Belo Horizonte','MG','belo-horizonte'),('São Paulo','SP','sao-paulo'),
         ('Rio de Janeiro','RJ','rio-de-janeiro')]
linhas=[]
for i,(nome,uf,slug) in enumerate(CIDADES):
    bg=' background: #fff8f3;' if i==0 else ''
    linhas.append(
     f'<tr style="border-bottom: 1px solid #f1f5f9;{bg}">\n'
     f'<td {TD} font-weight: bold; color: #1a202c;">{nome} <span style="color: #94a3b8; font-weight: 500;">({uf})</span></td>\n'
     f'<td class="cel-preco" {TD} text-align: right; color: #4a5568;" data-grupo="individual">[{slug}_ind_ambulatorialtotal_0]</td>\n'
     f'<td class="cel-preco" {TD} text-align: right; font-weight: 800; color: #ff6b00;" data-grupo="empresarial">[{slug}_emp_ambulatorialtotal_0]</td>\n</tr>')
TABELA=('<table style="width: 100%; border-collapse: collapse; margin-bottom: 16px; font-size: 16px;">\n<thead>\n'
 '<tr style="background: #16213e; color: #fff;">\n'
 '<th style="padding: 12px 10px; text-align: left; font-weight: bold;">Praça</th>\n'
 '<th style="padding: 12px 10px; text-align: right; font-weight: bold;">Por CPF</th>\n'
 '<th style="padding: 12px 10px; text-align: right; font-weight: bold;">Por CNPJ</th>\n</tr>\n</thead>\n<tbody>\n'
 + '\n'.join(linhas) + '\n</tbody>\n</table>\n')

# troca a tabela antiga de 6 capitais (so individual) pela nova de 9 x 2 portas
ini=s.find('<table style="width: 100%; border-collapse: collapse; margin-bottom: 16px; font-size: 16px;">')
fim=s.find('</table>',ini)+len('</table>\n')
antiga=s[ini:fim]
assert '[fortaleza_ind_ambulatorialtotal_0]' in antiga and 'sao-luis' in antiga, "tabela alvo errada"
s=s[:ini]+TABELA+s[fim:]
log.append("OK  J3 tabela unica: 9 pracas x CPF/CNPJ, 100% shortcode")

# ---------- 3. remove a tabela de 2 pracas com valores fixos
i2=s.find('<h3 style="font-size: 19px; font-weight: 800; color: #1a202c; margin: 22px 0 8px 0;">O mesmo piso, pela porta do CNPJ</h3>')
assert i2>0
f2=s.find('Em Recife o individual entra mais barato na primeira faixa; o empresarial só vence dos 19 aos 33 anos.</p>')
assert f2>i2
f2+=len('Em Recife o individual entra mais barato na primeira faixa; o empresarial só vence dos 19 aos 33 anos.</p>')
s=s[:i2]+(
 f'<p {P}>Os dois caminhos aparecem lado a lado de propósito. Em Fortaleza, Belo Horizonte, São Paulo '
 'e Rio o individual da marca não é vendido a pessoa física do jeito tradicional — nessas praças a coluna '
 'do CPF traz o produto individual disponível no grupo, que não é a mesma cesta. Onde as duas colunas '
 'existem no mesmo produto, a comparação vale, e foi ela que cotamos.</p>')+s[f2:]
log.append("OK  J4 tabela de valores fixos removida")

# ---------- 4. bloco Sudeste: trocar precos fixos por shortcode
sub('J5 SP NotreLife por shortcode','R$ 216,80','[sao-paulo_ind_ambulatorialtotal_0]')
sub('J6 RJ NotreLife por shortcode','R$ 229,23','[rio-de-janeiro_ind_ambulatorialtotal_0]')
sub('J7 Rio empresarial por shortcode',
 'o empresarial ambulatorial a partir de R$ 113,69','o mesmo plano pela porta do CNPJ a partir de [rio-de-janeiro_menorvalor]')

# ---------- 5. badges fixos saem (valor dinamico + rotulo fixo = erro futuro)
s=re.sub(r'<span class="badge-menor">menor</span>','',s)
log.append("OK  J8 badges 'menor' fixos removidos (eram o bug original)")

# ---------- 6. TRAVA: nenhum preco fixo no corpo
corpo=re.sub(r'<(script|style)>.*?</\1>','',s,flags=re.S)
fixos=re.findall(r'R\$\s?\d{1,3}(?:\.\d{3})*,\d{2}',corpo)
assert not fixos, f"ainda ha preco fixo no corpo: {sorted(set(fixos))}"
log.append("OK  J9 TRAVA: zero preco fixo no corpo (regra dura do shortcodes.md)")

for m in re.finditer(r'<(style|script)>(.*?)</\1>',s,re.S):
    assert '<br' not in m.group(2) and '\n' not in m.group(2)
io.open(SRC,'w',encoding='utf-8').write(s)
print('\n'.join(log)); print(f"\n>> {len(s)} chars")
