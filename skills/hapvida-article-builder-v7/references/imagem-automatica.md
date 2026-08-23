# IMAGEM AUTOMÁTICA DA TABELA DE PREÇO [V6]

> **O que muda.** Até a v5, a imagem da tabela era um **bloco comentado** que a pós-produção deixava para alguém preencher depois — e que muitas vezes nunca era preenchido. Na v6, a imagem é **entregue junto com o artigo**, com `<figure>` e `ImageObject` prontos.
>
> **O que NÃO muda.** Nada de gerador de imagem por IA. A imagem sai da **arte que já está em uso**, trocando apenas a coluna de valores.

---

## As duas regras duras (as duas nasceram de erro real)

### 1. Nunca IA em número

Modelo de imagem **embaralha dígito**. Num artigo de preço, um dígito trocado é dano ao leitor e risco para a corretora.

- O valor vai para a arte **exatamente como saiu da cotação**.
- Faltando qualquer um dos 10 valores, **a imagem não sai**. Falha barulhenta, nunca silenciosa — o `gerar_imagem_artigo.py` recusa e explica.
- Valor fora do formato brasileiro (`1.234,56`) também é recusado. **Nunca "arredondar para funcionar".**

### 2. O nome do arquivo pode matar a imagem

Existe no tabelaplanos.com.br um **301** que captura qualquer URL contendo `tabela` **e** `coparticipacao` **em minúsculo** — inclusive dentro de `/wp-content/uploads/` — e joga para o guia de coparticipação. A imagem fica **invisível para o Google mesmo estando no HTML**. Foi isso que matou a geração anterior de tabelas.

A regra é **sensível a maiúscula**. O padrão que funciona (e que fez as 6 imagens de julho/2026 sobreviverem):

```
Tabela-Hapvida-<Cidade>-<modalidade>-coparticipacao-<total|parcial>.png
```

Com `T` e `H` maiúsculos, a regra não dispara. O script já nomeia assim e **recusa** nome perigoso.

⚠️ **Plugin de otimização que "normaliza" nome de arquivo para minúsculo derruba tudo de novo.** Se alguém instalar um, as imagens somem sem aviso.

---

## Como rodar

```
python -X utf8 C:\Users\netop\.claude\skills\hapvida-article-builder-v7\gerar_imagem_artigo.py ^
    --cidade "Piracicaba" --modalidade individual --coparticipacao parcial ^
    --valores "107,83;120,77;135,26;146,25;159,04;180,63;216,75;259,20;349,53;541,88" ^
    --saida-dir "C:\Users\netop\Downloads\imagens-artigo" ^
    --vigencia "julho de 2026"
```

**Combinações disponíveis** (6 artes): `individual` / `empresarial` / `adesao` × `total` / `parcial`.

**Ordem dos 10 valores** — as faixas etárias da ANS, de cima para baixo na arte:
`0-18 · 19-23 · 24-28 · 29-33 · 34-38 · 39-43 · 44-48 · 49-53 · 54-58 · 59+`

**Saída:** o arquivo `.png`, o bloco `<figure>` pronto, o `ImageObject` para o `@graph` e o comando `curl` de conferência.

---

## De onde vêm os valores

**Da mesma fonte dos shortcodes do artigo.** Não de outra consulta, não de memória, não de artigo anterior.

Isso não é preciosismo — é a proteção que já está na Regra de Shortcodes: se o admin atualizar o preço sem regerar a imagem, o texto (com shortcode) fica atualizado e a imagem fica velha, e a **discrepância aparece** e força a correção. Se a imagem tiver vindo de outra fonte, a discrepância pode existir desde o dia zero e ninguém percebe.

> **Nota de produto:** em PF (individual e adesão), o padrão da casa é **sempre "+ Odonto"** — decisão de 28/07/2026. Em Fortaleza, inclusive, a com odonto é a mais barata. Cotar e gerar a imagem sobre esse padrão.

---

## Onde a imagem entra no artigo

| Tipo | Onde | Quantas |
|---|---|---|
| **TR1-TR5** (tabela regional) | logo abaixo do H2 da tabela de preço | 1 por modalidade presente na página |
| **City S1-S7** | **[V7.1]** no **fim** da seção de preço (último elemento da S2↑b), depois da análise e do H3 de coparticipação — **nunca colada no shortcode da tabela** | 1, a modalidade principal da cidade |
| **Pillar P1-P9** | **[V7.1]** idem city: fecha a P3↑b, não abre | 1 |
| **Hospital HS1-HS4** | normalmente nenhuma | só se a página tiver seção de preço própria |

> **[V7.1] Por que a imagem desceu na city/pillar:** com a tabela em primeiro lugar (v7), colar a imagem embaixo dela entrega a mesma informação duas vezes na primeira tela e empurra o sumário para longe. Medido no artigo de Recife. Em **TR a regra é a oposta e continua valendo**: lá a `<figure>` **é** a tabela, e por isso fica no topo.

**Regra de ouro que não muda:** a imagem **acompanha** o shortcode de preço, nunca o substitui. O texto continua com shortcode; a imagem é reforço visual e ativo de busca por imagem.

---

## Depois de subir — conferência obrigatória

```bash
curl -sSI "https://tabelaplanos.com.br/wp-content/uploads/Tabela-Hapvida-Piracicaba-individual-coparticipacao-parcial.png"
```

Tem que voltar **200** e `content-type: image/*`.

- **301** → o nome caiu na regra de redirecionamento. Renomear mantendo as maiúsculas e subir de novo.
- Conferir **também** as variações que o WordPress gera sozinho: `-1024x1024`, `-scaled`. Elas caem na mesma regra.
- **Nunca assumir que o arquivo existe só porque o upload não deu erro.**

---

## Quando regerar

- Reajuste anual (maio) ou qualquer mudança na tabela.
- Mudança de modalidade padrão da cidade.
- **Sempre que o shortcode de preço mudar de valor** — imagem velha ao lado de texto novo é pior que não ter imagem.

Registrar a regeração no banco junto com a atualização do artigo (`registrar_atualizacao`).

---

## Ressalva honesta sobre a arte

O `gerar_imagem_arte.py` apaga o valor antigo copiando uma fatia limpa de cima e de baixo da própria linha. É um bom truque — mantém a listra e o degradê —, mas **não é perfeito**: em algumas linhas fica uma sombra fina do número anterior, visível se você aproximar. Não atrapalha a leitura nem o SEO, mas **não diga que a imagem está impecável**. Se for para uso em anúncio pago ou peça impressa, vale abrir e revisar antes.

---

## Ponto de extensão pronto (ainda não implementado)

**Cartão de capa / OG por cidade.** Já existem no mesmo diretório o `imagem-tabela.html` + `gerar_imagem.py`, que renderizam um cartão limpo via Chrome headless — determinístico, sem IA. Dá para transformar num cartão de compartilhamento (nome da cidade, "a partir de R$", selo) com pouco trabalho. Ficou **fora** da v6 por escolha de escopo: a imagem da tabela tem infraestrutura pronta e valor imediato; a capa exige desenhar um molde novo.

Quando for fazer: as mesmas duas regras duras valem — nada de IA no número, e testar a URL com `curl` antes de confiar.

Ver também: `references/tabela-regional-subpages.md` (seção "Image-First Optimization"), `references/shortcodes.md` e a seção **Image Optimization Rules** do `SKILL.md`.
