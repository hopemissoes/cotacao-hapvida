# -*- coding: utf-8 -*-
"""
gerar_imagem_artigo.py — IMAGEM AUTOMÁTICA DO ARTIGO [V6]
(hapvida-article-builder-v7)

Gera a imagem da tabela de preço JUNTO com o artigo e devolve, prontos para colar:
  1. o arquivo de imagem (com nome que sobrevive ao redirect do site)
  2. o bloco <figure> completo (lazy, width/height, alt, figcaption)
  3. o JSON-LD ImageObject
  4. o comando curl de conferência

NÃO desenha nada: é um embrulho sobre o `gerar_imagem_arte.py` que já existe em
C:\\Users\\netop\\Downloads\\claude\\cotador\\, que reaproveita as 6 artes e troca
apenas a coluna de valores.

REGRAS DURAS (as duas nasceram de erro real, não de teoria):

  1. NUNCA usar modelo de imagem (IA) para tabela de preço — embaralha dígito.
     O valor vai para a arte exatamente como saiu da cotação. Faltando qualquer
     um dos 10 valores, a imagem NÃO SAI (falha barulhenta, nunca silenciosa).

  2. O nome do arquivo NÃO pode ter "tabela" e "coparticipacao" juntos em
     MINÚSCULO. Existe no tabelaplanos.com.br um 301 que captura qualquer URL
     com essas duas palavras em minúsculo — inclusive dentro de
     /wp-content/uploads/ — e joga para o guia de coparticipação. A imagem some
     do Google mesmo estando no HTML. A regra é sensível a maiúscula: o padrão
     "Tabela-Hapvida-..." (T e H maiúsculos) passa. Foi assim que as 6 imagens
     de julho/2026 funcionaram. Este script já nomeia assim e RECUSA nome
     perigoso.

Uso:
  python -X utf8 gerar_imagem_artigo.py \\
      --cidade "Piracicaba" --modalidade individual --coparticipacao parcial \\
      --valores "107,83;120,77;135,26;146,25;159,04;180,63;216,75;259,20;349,53;541,88" \\
      --saida-dir "C:\\Users\\netop\\Downloads\\imagens-artigo"

Opcionais:
  --alt "..."        alt próprio (senão é montado a partir de cidade/modalidade)
  --base-url "..."   base pública para montar a URL final e o ImageObject
                     (padrão: https://tabelaplanos.com.br/wp-content/uploads/)
  --vigencia "julho de 2026"   entra no figcaption e na descrição
"""
import argparse
import importlib.util
import os
import re
import sys
import unicodedata

# Onde procurar o gerador de arte, nesta ordem (a pasta pode ter sido movida).
CAMINHOS_GERADOR = [
    r"C:\Users\netop\Downloads\claude\cotador\gerar_imagem_arte.py",
    r"C:\Users\netop\Downloads\gerar_imagem_arte.py",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "gerar_imagem_arte.py"),
]

MODALIDADES = {"individual", "empresarial", "adesao"}
COPARTICIPACOES = {"total", "parcial"}

# Faixas etárias da ANS, na ordem em que aparecem na arte.
FAIXAS = ["0-18", "19-23", "24-28", "29-33", "34-38",
          "39-43", "44-48", "49-53", "54-58", "59+"]

BASE_URL_PADRAO = "https://tabelaplanos.com.br/wp-content/uploads/"

RE_VALOR = re.compile(r"^\d{1,3}(\.\d{3})*,\d{2}$")


def morde(msg):
    print("\n❌ " + msg, file=sys.stderr)
    raise SystemExit(1)


def slug_titulado(texto):
    """'São José do Rio Preto' -> 'Sao-Jose-do-Rio-Preto' (mantém maiúsculas)."""
    t = unicodedata.normalize("NFD", texto)
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    t = re.sub(r"[^A-Za-z0-9]+", "-", t).strip("-")
    return t


def nome_seguro(cidade, modalidade, coparticipacao):
    """Nome de arquivo que NÃO cai no 301 do site.

    O 301 exige 'tabela' E 'coparticipacao' ambos em minúsculo. Mantendo
    'Tabela' e 'Hapvida' capitalizados, a regra não dispara.
    """
    nome = "Tabela-Hapvida-%s-%s-coparticipacao-%s.png" % (
        slug_titulado(cidade), modalidade, coparticipacao
    )
    checa_nome(nome)
    return nome


def checa_nome(nome):
    baixo = nome.lower()
    if "tabela" in nome and "coparticipacao" in baixo and "Tabela" not in nome:
        morde("Nome de arquivo perigoso: '%s'.\n"
              "   Ele tem 'tabela' e 'coparticipacao' em minúsculo — o 301 do site captura\n"
              "   esse padrão e a imagem fica invisível para o Google. Use 'Tabela-Hapvida-...'."
              % nome)


def valida_valores(bruto):
    valores = [v.strip() for v in bruto.split(";")]
    valores = [v for v in valores if v != ""]
    if len(valores) != 10:
        morde("Esperava exatamente 10 valores (uma por faixa etária da ANS), recebi %d.\n"
              "   Valor faltando = imagem NÃO SAI. Complete a cotação e rode de novo." % len(valores))
    ruins = [v for v in valores if not RE_VALOR.match(v.replace("R$", "").strip())]
    if ruins:
        morde("Valor fora do formato brasileiro (1.234,56): %s\n"
              "   Nunca 'arredondar para funcionar' — o número tem que sair da cotação como está."
              % ", ".join(ruins))
    return valores


def carrega_gerador():
    for caminho in CAMINHOS_GERADOR:
        if os.path.isfile(caminho):
            spec = importlib.util.spec_from_file_location("gerar_imagem_arte", caminho)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod, caminho
    morde("Não achei o gerar_imagem_arte.py. Procurei em:\n   " +
          "\n   ".join(CAMINHOS_GERADOR) +
          "\n   Ele é quem reaproveita as 6 artes. Sem ele a v6 não gera imagem —\n"
          "   e a alternativa NÃO é desenhar layout novo nem usar gerador de imagem.")


def monta_alt(cidade, modalidade, coparticipacao, valores, vigencia):
    rotulo = {"individual": "individual", "empresarial": "empresarial (PME)",
              "adesao": "por adesão"}[modalidade]
    alt = ("Tabela de preços do plano Hapvida %s em %s com coparticipação %s, "
           "por faixa etária da ANS: de R$ %s na faixa até 18 anos a R$ %s na faixa "
           "de 59 anos ou mais. Valores vigentes em %s."
           % (rotulo, cidade, coparticipacao, valores[0], valores[-1], vigencia))
    return alt


def main(argv=None):
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--cidade", required=True)
    ap.add_argument("--modalidade", required=True, choices=sorted(MODALIDADES))
    ap.add_argument("--coparticipacao", required=True, choices=sorted(COPARTICIPACOES))
    ap.add_argument("--valores", required=True,
                    help="10 valores separados por ';', na ordem das faixas da ANS")
    ap.add_argument("--saida-dir", default=os.path.join(os.path.expanduser("~"), "Downloads"))
    ap.add_argument("--alt", default=None)
    ap.add_argument("--vigencia", default="[mes_atual] de [ano_atual]")
    ap.add_argument("--base-url", default=BASE_URL_PADRAO)
    args = ap.parse_args(argv)

    valores = valida_valores(args.valores)
    nome = nome_seguro(args.cidade, args.modalidade, args.coparticipacao)
    destino = os.path.join(args.saida_dir, nome)

    gerador, caminho_gerador = carrega_gerador()
    chave_arte = "%s_%s" % (args.modalidade, args.coparticipacao)
    if chave_arte not in gerador.ARTES:
        morde("Não existe arte para '%s'. Artes disponíveis: %s"
              % (chave_arte, ", ".join(sorted(gerador.ARTES))))

    print("Gerador de arte: %s" % caminho_gerador)
    print("Arte: %s  (%s)" % (chave_arte, gerador.ARTES[chave_arte]))
    gerador.gerar({"arte": chave_arte, "valores": valores}, destino)

    from PIL import Image
    with Image.open(destino) as im:
        larg, alt_px = im.size

    alt = args.alt or monta_alt(args.cidade, args.modalidade,
                                args.coparticipacao, valores, args.vigencia)
    if not (120 <= len(alt) <= 260):
        print("\n⚠️  alt com %d caracteres (alvo 150-250). Reveja antes de publicar." % len(alt))

    url = args.base_url.rstrip("/") + "/" + nome
    rotulo = {"individual": "Individual/Familiar", "empresarial": "Empresarial (PME)",
              "adesao": "Por Adesão"}[args.modalidade]

    figura = (
        '<figure style="margin:24px 0;text-align:center">\n'
        '  <img src="%s" alt="%s"\n'
        '       width="%d" height="%d" loading="lazy" decoding="async"\n'
        '       style="max-width:100%%;height:auto;border-radius:12px" />\n'
        '  <figcaption style="font-size:14px;color:#5a6b7a;margin-top:10px">\n'
        '    Tabela de preços Hapvida %s com coparticipação %s em %s — '
        'valores vigentes em %s. Consulte a cotação para o valor do seu caso.\n'
        '  </figcaption>\n'
        '</figure>'
        % (url, alt.replace('"', "&quot;"), larg, alt_px,
           rotulo, args.coparticipacao, args.cidade, args.vigencia)
    )

    jsonld = (
        '{\n'
        '  "@type": "ImageObject",\n'
        '  "contentUrl": "%s",\n'
        '  "url": "%s",\n'
        '  "width": %d,\n'
        '  "height": %d,\n'
        '  "caption": "%s",\n'
        '  "description": "%s"\n'
        '}' % (url, url, larg, alt_px,
               "Tabela de preços Hapvida %s — %s" % (rotulo, args.cidade),
               alt.replace('"', '\\"'))
    )

    print("\n" + "=" * 68)
    print("IMAGEM GERADA — %s (%dx%d)" % (destino, larg, alt_px))
    print("=" * 68)
    print("\n--- BLOCO <figure> (colar no artigo, editor de CÓDIGO) ---\n")
    print(figura)
    print("\n--- ImageObject (entra no @graph do schema) ---\n")
    print(jsonld)
    print("\n--- CONFERÊNCIA OBRIGATÓRIA depois do upload ---\n")
    print('curl -sSI "%s"' % url)
    print("\nTem que voltar 200 + content-type: image/*.")
    print("Se voltar 301, o nome caiu na regra de redirecionamento do site —")
    print("renomeie mantendo 'Tabela-Hapvida-' com maiúsculas e suba de novo.")
    print("Conferir TAMBÉM as variações que o WordPress gera (-1024x1024, -scaled).")
    print("\n⚠️  Plugin que 'normaliza' nome de arquivo para minúsculo derruba tudo de novo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
