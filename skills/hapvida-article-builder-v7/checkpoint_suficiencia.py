# -*- coding: utf-8 -*-
"""
checkpoint_suficiencia.py — A PESQUISA DÁ PARA ESCREVER O ARTIGO? [V7.2]
(hapvida-article-builder-v7)

Roda no fim do Estágio 2, ANTES de qualquer redação, junto com o painel de
juízes da pesquisa (Agentes 23 e 24 — ver references/juiz-pesquisa.md).

O checkpoint_fase0.py responde "a pesquisa foi FEITA?" (volume, fonte, data).
Este responde outra pergunta, que é onde o artigo realmente morre:
"a pesquisa SUSTENTA o artigo que vamos escrever?"

Cinco medidas:

  A. SEÇÃO ÓRFÃ — para cada seção prevista do tipo de artigo, quantos itens da
     pesquisa a sustentam. Seção com zero é seção que vai ser preenchida com
     texto genérico — o doorway nasce aqui, não na redação.
  B. FAQ LOCAL — quantas perguntas sobrevivem à troca da cidade (paráfrase de
     PAA nacional), e quantas são duplicatas entre si.
  C. VETO DE INTENÇÃO — secundária marcada "qualificada" que na verdade é
     tráfego de quem JÁ é cliente (2ª via, boleto, telefone, cancelar).
  D. GANHO DO CI-2 — o ganho de informação está em defensibilidade 4-5?
     Nível 4-5 não é ganho: o concorrente copia e a IA responde sozinha.
  E. DIFERENCIAL SEM ÂNCORA — "diferencial" que serve para qualquer praça.

Uso:
  python -X utf8 checkpoint_suficiencia.py <state_file.md> --cidade "Piracicaba"
         [--tipo city|tr|pillar|hospital] [--ancoras ancoras.txt]

Saída: matriz + "✅ APROVADO" ou "❌ REPROVADO" (exit 1). Só biblioteca padrão.

O que NÃO faz: não julga se o dado é interessante, nem se o ângulo vende. Isso
é dos juízes 23/24 — este script só entrega a eles o mapa do que está vazio.
"""
import argparse
import os
import re
import sys
import unicodedata

# ------------------------------------------------------------------ limiares

MIN_ITENS_POR_SECAO = 2
MAX_FAQ_GENERICA_PCT = 20.0
MAX_DIFERENCIAL_SEM_ANCORA_PCT = 34.0
JACCARD_DUPLICATA = 0.6

# Seções por tipo: rótulo -> vocabulário que indica que um item a sustenta
SECOES = {
    "city": [
        ("S1 por que a cidade é diferente", ["perfil", "industrial", "economia", "populacao",
                                             "renda", "idh", "cresc", "regiao metropolitana",
                                             "diferente", "fio condutor"]),
        ("S2 preços e coparticipação", ["preco", "valor", "mensalidade", "tabela",
                                        "coparticipacao", "faixa etaria", "reajuste"]),
        ("S3 planos disponíveis", ["nosso plano", "mix", "pleno", "smart", "advance",
                                   "premium", "infinity", "notrelife", "produto",
                                   "individual", "empresarial", "adesao"]),
        ("S4 rede assistencial", ["hospital", "clinica", "unidade", "pronto", "upa",
                                  "laborat", "rede", "leito", "credenciad"]),
        ("S5 cobertura por bairro", ["bairro", "zona ", "regiao", "distrito", "avenida",
                                     "deslocamento", "transporte", "cobertura"]),
        ("S6 cenário de saúde local", ["cnes", "datasus", "leitos", "sus", "ibge",
                                       "estabelecimento", "saude publica", "concorrente",
                                       "unimed", "santa casa"]),
        ("S7 como contratar", ["contrat", "carencia", "portabilidade", "documento",
                               "corretora", "prazo", "adesao", "vidas"]),
    ],
    "hospital": [
        ("HS1 o hospital", ["hospital", "endereco", "fundac", "acredita", "ona"]),
        ("HS2 estrutura e serviços", ["uti", "centro cirurgico", "maternidade", "pronto",
                                      "especialidade", "exame", "servico"]),
        ("HS3 como usar", ["autorizac", "agendamento", "guia medico", "encaminhamento",
                           "carteirinha", "coparticipacao"]),
        ("HS4 rede em volta", ["cidade", "bairro", "clinica", "unidade", "rede"]),
    ],
    "tr": [
        ("TR1 introdução local", ["cidade", "sede", "referencia", "tabela 1", "tabela 2"]),
        ("TR2 tabela empresarial", ["empresarial", "vidas", "cnpj", "tabela", "valor"]),
        ("TR3 tabela individual", ["individual", "familiar", "tabela", "valor", "faixa"]),
        ("TR4 fatores únicos da praça", ["beneficiario", "rede propria", "fundac",
                                         "modelo", "comparac", "cidade"]),
        ("TR5 promoções e gatilhos", ["promoc", "migrac", "desconto", "campanha", "amil",
                                      "notredame"]),
    ],
    "pillar": [
        ("P1-P2 o que é / para quem", ["definic", "o que e", "publico", "perfil", "quem"]),
        ("P3 preços", ["preco", "valor", "tabela", "mensalidade", "faixa etaria"]),
        ("P4-P5 cobertura e regras", ["cobertura", "carencia", "rol", "ans", "regra",
                                      "coparticipacao"]),
        ("P6 comparação", ["compara", "versus", "diferenca", "mix", "nosso plano",
                           "individual", "empresarial"]),
        ("P7-P8 como contratar", ["contrat", "documento", "corretora", "prazo", "adesao"]),
        ("P9 compensa / não compensa", ["compensa", "vantagem", "desvantagem", "limitac",
                                        "nao serve", "perfil"]),
    ],
}

INTENCAO_JA_CLIENTE = [
    "2 via", "2a via", "segunda via", "boleto", "fatura", "telefone", "0800",
    "trabalhe conosco", "resultado de exame", "resultado exame", "cancelar",
    "cancelamento", "login", "entrar no app", "aplicativo", "ouvidoria",
    "reclamac", "carteirinha digital", "sac", "central de atendimento",
]

MARCADORES_ENTIDADE = [
    "hospital", "clinica", "policlinica", "upa", "pronto", "unidade", "bairro",
    "avenida", "rua", "distrito", "jardim", "vila", "laborat", "maternidade",
]


def sem_acento(t):
    t = unicodedata.normalize("NFD", t or "")
    return "".join(c for c in t if unicodedata.category(c) != "Mn")


def norm(t):
    t = sem_acento(t or "").lower()
    return re.sub(r"\s+", " ", t).strip()


def variantes_cidade(cidade):
    base = norm(cidade)
    out = {base} if base else set()
    for p in base.split():
        if len(p) > 2 and p not in ("de", "do", "da", "dos", "das"):
            out.add(p)
    return {o for o in out if o}


def carregar_ancoras(caminho):
    if not caminho or not os.path.isfile(caminho):
        return []
    with open(caminho, encoding="utf-8", errors="replace") as fh:
        return [norm(l) for l in fh if l.strip() and not l.startswith("#") and len(l) > 3]


def tem_ancora_local(texto, variantes, ancoras):
    n = norm(texto)
    if any(v in n for v in variantes):
        return True
    if any(a in n for a in ancoras):
        return True
    for marcador in MARCADORES_ENTIDADE:
        if re.search(r"\b%s\b\s+[a-z0-9]" % marcador, n):
            return True
    return False


def itens_do_state(txt):
    """Um 'item' é uma linha com conteúdo real (bullet, campo yaml, frase)."""
    itens = []
    for linha in txt.splitlines():
        l = linha.strip()
        if not l or l.startswith("#") or l.startswith("|") or l.startswith("```"):
            continue
        if len(l.split()) < 4:
            continue
        itens.append(l)
    return itens


def perguntas(txt):
    out = []
    for linha in txt.splitlines():
        l = linha.strip().strip('"').strip("'").lstrip("-").strip()
        if l.endswith("?") and len(l.split()) >= 5 and not l.startswith("#"):
            out.append(l)
    return out


def jaccard(a, b):
    sa, sb = set(norm(a).split()), set(norm(b).split())
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / float(len(sa | sb))


# ------------------------------------------------------------------ main

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("state_file")
    ap.add_argument("--cidade", default="")
    ap.add_argument("--tipo", default="city", choices=list(SECOES))
    ap.add_argument("--ancoras", default="")
    args = ap.parse_args()

    try:
        with open(args.state_file, encoding="utf-8", errors="replace") as fh:
            txt = fh.read()
    except OSError as exc:
        print("nao consegui ler o state file: %s" % exc)
        return 2

    if args.tipo in ("city", "tr", "hospital") and not args.cidade:
        print("❌ REPROVADO — --cidade e' obrigatorio em artigo %s." % args.tipo)
        return 1

    variantes = variantes_cidade(args.cidade)
    ancoras = carregar_ancoras(args.ancoras)
    erros, avisos = [], []

    print("=" * 70)
    print("SUFICIÊNCIA DA PESQUISA [V7.2] — %s" % os.path.basename(args.state_file))
    print("tipo: %s | cidade/eixo: %s | âncoras: %d"
          % (args.tipo, args.cidade or "-", len(ancoras)))
    print("=" * 70)

    itens = itens_do_state(txt)
    itens_norm = [norm(i) for i in itens]

    # A) seção órfã --------------------------------------------------------
    print("\nA · MATRIZ DE SUFICIÊNCIA POR SEÇÃO (itens da pesquisa que a sustentam)")
    orfas, magras = [], []
    for rotulo, vocab in SECOES[args.tipo]:
        n = sum(1 for i in itens_norm if any(v in i for v in vocab))
        marca = ""
        if n == 0:
            orfas.append(rotulo)
            marca = " 🔴 ÓRFÃ"
        elif n < MIN_ITENS_POR_SECAO:
            magras.append(rotulo)
            marca = " 🟡 magra"
        print("   %-38s %3d item(ns)%s" % (rotulo, n, marca))
    if orfas:
        erros.append("A %d seção(ões) órfã(s) — nada na pesquisa as sustenta: %s. "
                     "Seção sem dado vira texto genérico na redação"
                     % (len(orfas), "; ".join(orfas)))
    if magras:
        avisos.append("A seção(ões) com menos de %d itens: %s"
                      % (MIN_ITENS_POR_SECAO, "; ".join(magras)))

    # B) FAQ ---------------------------------------------------------------
    qs = perguntas(txt)
    print("\nB · FAQ — LOCAL DE VERDADE?")
    genericas = [q for q in qs if not tem_ancora_local(q, variantes, ancoras)]
    pct = (100.0 * len(genericas) / len(qs)) if qs else 0.0
    print("   perguntas: %d | sem âncora local: %d (%.1f%%, limite %.0f%%)"
          % (len(qs), len(genericas), pct, MAX_FAQ_GENERICA_PCT))
    for q in genericas[:5]:
        print("   - %s" % q[:88])
    if qs and pct > MAX_FAQ_GENERICA_PCT:
        erros.append("B %.1f%% das FAQ sobrevivem à troca da cidade (limite %.0f%%) — "
                     "é paráfrase de PAA nacional, não FAQ local"
                     % (pct, MAX_FAQ_GENERICA_PCT))
    duplicatas = []
    for i in range(len(qs)):
        for j in range(i + 1, len(qs)):
            if jaccard(qs[i], qs[j]) >= JACCARD_DUPLICATA:
                duplicatas.append((qs[i], qs[j]))
    if duplicatas:
        print("   duplicatas entre si: %d par(es)" % len(duplicatas))
        for a, b in duplicatas[:3]:
            print("     · %s\n       %s" % (a[:70], b[:70]))
        erros.append("B %d par(es) de FAQ quase idênticas entre si" % len(duplicatas))

    # C) veto de intenção ---------------------------------------------------
    print("\nC · VETO DE INTENÇÃO NAS SECUNDÁRIAS")
    ruins = []
    ocorrencias = list(re.finditer(r"kw\s*:\s*[\"']?([^\"'\n]+)", txt, re.I))
    for idx, m in enumerate(ocorrencias):
        kw = m.group(1).strip()
        # contexto = só até o próximo 'kw:' — senão o veredito do item seguinte
        # é lido como se fosse deste (falso positivo real, pego em teste)
        fim = ocorrencias[idx + 1].start() if idx + 1 < len(ocorrencias) else len(txt)
        contexto = txt[m.end():min(fim, m.end() + 220)]
        if not re.search(r"veredito\s*:\s*qualificada", contexto, re.I):
            continue
        if any(t in norm(kw) for t in INTENCAO_JA_CLIENTE):
            ruins.append(kw)
    print("   secundárias qualificadas com intenção de quem JÁ é cliente: %d" % len(ruins))
    for k in ruins[:5]:
        print("   - %s" % k)
    if ruins:
        erros.append("C %d secundária(s) qualificada(s) são tráfego de quem já é "
                     "cliente (%s) — incham impressão e derrubam conversão"
                     % (len(ruins), ", ".join(ruins[:3])))

    # D) ganho do CI-2 ------------------------------------------------------
    print("\nD · GANHO DE INFORMAÇÃO (CI-2) — nível de defensibilidade")
    nivel_ganho = None
    for m in re.finditer(r"ganho[^\n]*informa[^\n]*", txt, re.I):
        janela = txt[m.start():m.start() + 400]
        d = re.search(r"defensibilidade\s*:\s*\"?\s*([1-5])", janela, re.I)
        if d:
            nivel_ganho = int(d.group(1))
            break
    if nivel_ganho is None:
        print("   nível não declarado junto ao ganho")
        erros.append("D o ganho de informação do CI-2 não declara defensibilidade — "
                     "sem nível não se sabe se é vantagem ou lugar-comum")
    else:
        print("   nível declarado: %d" % nivel_ganho)
        if nivel_ganho >= 4:
            erros.append("D ganho de informação em nível %d — nível 4-5 não é ganho: "
                         "o concorrente copia em dez minutos e a IA responde sozinha"
                         % nivel_ganho)

    # E) diferenciais -------------------------------------------------------
    print("\nE · DIFERENCIAIS COM ÂNCORA LOCAL")
    difs = []
    for m in re.finditer(r"^[ \t]*-?[ \t]*(?:titulo|diferencial)[ \t]*:[ \t]*(.+)$",
                         txt, re.I | re.M):
        difs.append(m.group(1).strip())
    sem_ancora = [d for d in difs if not tem_ancora_local(d, variantes, ancoras)]
    if difs:
        pct_d = 100.0 * len(sem_ancora) / len(difs)
        print("   diferenciais: %d | sem âncora local: %d (%.0f%%)"
              % (len(difs), len(sem_ancora), pct_d))
        for d in sem_ancora[:4]:
            print("   - %s" % d[:88])
        if pct_d > MAX_DIFERENCIAL_SEM_ANCORA_PCT:
            erros.append("E %.0f%% dos diferenciais servem para qualquer praça "
                         "(limite %.0f%%)" % (pct_d, MAX_DIFERENCIAL_SEM_ANCORA_PCT))
    else:
        print("   nenhum diferencial com rótulo 'titulo:'/'diferencial:' encontrado")
        avisos.append("E diferenciais não rotulados — use 'titulo:' para que a trava veja")

    # ------------------------------------------------------------ veredito
    print("\n" + "-" * 70)
    if avisos:
        print("🟡 AVISOS (%d)" % len(avisos))
        for a in avisos:
            print("   - %s" % a)
    if erros:
        print("\n🔴 BLOQUEIOS (%d)" % len(erros))
        for e in erros:
            print("   - %s" % e)
        print("\n❌ REPROVADO — a pesquisa não sustenta o artigo. Volte ao Estágio 1")
        print("   (agente da função), não à redação. Escrever com isto produz doorway.")
        return 1

    print("\n✅ APROVADO — a pesquisa cobre todas as seções previstas.")
    print("   Isto NÃO é juízo de qualidade: os juízes 23 e 24 ainda decidem se o")
    print("   que foi coletado presta (references/juiz-pesquisa.md).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
