# -*- coding: utf-8 -*-
"""
checkpoint_modelos.py — trava mecânica do ROTEAMENTO DE MODELOS [V7.2]
(hapvida-article-builder-v7)

Confere o bloco PLANO_MODELOS antes de a linha de agentes ser disparada:

  T1  agente travado (🔒) roda em degrau "forte";
  T2  par produtor/conferente NÃO compartilha modelo;
  T3  painel de juízes tem >= 2 modelos distintos e >= 1 juiz em modelo
      diferente de todos os que escreveram/editaram;
  T7  rebaixamento de agente não travado vem com observação escrita;
      agente obrigatório presente; degrau válido.

Uso:
  python -X utf8 checkpoint_modelos.py <state_file.md|plano.md> [city|tr|pillar|hospital]

Sem o tipo, assume "city". Saída: relatório + "✅ APROVADO" ou "❌ REPROVADO"
(exit code 1). Só biblioteca padrão.

O que NÃO faz: não julga o artigo, não mede custo real, não verifica se o
modelo declarado foi mesmo o usado. Ele confere o PLANO — a honestidade da
execução continua sendo do orquestrador.
"""
import re
import sys
import unicodedata

# ------------------------------------------------------------------ constantes

DEGRAUS = ("forte", "medio", "barato")

# Degrau padrão da §3 da references/modelos-agentes.md
PADRAO = {
    "0": "forte", "1": "medio", "2": "medio", "3": "barato", "4": "medio",
    "ci-1": "forte", "ci-2": "forte", "5": "forte",
    "6": "forte", "7": "barato",
    "8": "forte", "9": "medio", "10": "medio",
    "11": "forte", "19": "medio", "20": "barato",
    "12": "forte", "13": "forte", "14": "medio", "15": "forte",
    "16a": "forte", "16b": "forte", "16c": "forte",
    "17": "medio", "18": "barato", "22": "barato",
}

# 🔒 não aceitam rebaixamento (T1)
TRAVADOS = {"0", "ci-1", "ci-2", "5", "6", "11", "12", "13", "15",
            "16a", "16b", "16c"}

# Pares (produtor, conferente) que precisam diferir de MODELO (T2)
PARES = [
    ("2", "6", "rede assistencial x conferente de fatos"),
    ("4", "7", "keywords x conferente DataForSeo"),
    ("8", "11", "redator Bloco A x editor-chefe"),
    ("9", "11", "redator Bloco B x editor-chefe"),
    ("10", "11", "redator Bloco C x editor-chefe"),
    ("11", "19", "editor-chefe x voz humana"),
    ("5", "13", "fio condutor x anti-doorway"),
]

JUIZES = ("16a", "16b", "16c")
EDITOR_FINAL = "11"   # quem assina o texto inteiro (T3)

OBRIGATORIOS_BASE = [
    "1", "2", "3", "4", "ci-1", "ci-2", "5", "6", "7",
    "8", "9", "10", "11", "12", "13", "14", "15",
    "16a", "16b", "16c", "18",
]
# Por tipo de artigo
OBRIGATORIOS_EXTRA = {
    "city": ["19", "20"],
    "pillar": ["19", "20"],
    "tr": ["20"],
    "hospital": ["19"],
}
OPCIONAIS_AVISO = ["17", "22"]

RE_LINHA = re.compile(r"^\s*([0-9]{1,2}[abc]?|ci-?[12])\s*\|(.+)$", re.IGNORECASE)
RE_MONOMODELO = re.compile(r"^\s*MODO\s*:\s*monomodelo", re.IGNORECASE)


# ------------------------------------------------------------------ utilidades

def norm(text):
    text = unicodedata.normalize("NFD", text or "")
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return text.strip().lower()


def norm_id(raw):
    ident = norm(raw).replace(" ", "")
    ident = re.sub(r"^ci-?([12])$", r"ci-\1", ident)
    return ident


# ------------------------------------------------------------------ parsing

def parse(caminho):
    """Devolve (plano, monomodelo, achou_bloco)."""
    with open(caminho, "r", encoding="utf-8", errors="replace") as fh:
        linhas = fh.read().splitlines()

    plano = {}
    monomodelo = False
    dentro = False
    achou = False

    for linha in linhas:
        if RE_MONOMODELO.match(linha):
            monomodelo = True
            continue
        if norm(linha).startswith("plano_modelos"):
            dentro = True
            achou = True
            continue
        if not dentro:
            continue

        crua = linha.strip()
        if crua.startswith("```"):
            continue
        if not crua:
            # uma linha em branco não encerra; duas seguidas sim
            continue

        m = RE_LINHA.match(crua)
        if not m:
            # linha que não é do plano encerra o bloco
            if plano:
                dentro = False
            continue

        ident = norm_id(m.group(1))
        campos = [c.strip() for c in m.group(2).split("|")]
        funcao = campos[0] if campos else ""
        degrau = norm(campos[1]) if len(campos) > 1 else ""
        modelo = norm(campos[2]) if len(campos) > 2 else ""
        obs = campos[3].strip() if len(campos) > 3 else ""
        degrau = "medio" if degrau in ("medio", "médio") else degrau
        plano[ident] = {"funcao": funcao, "degrau": degrau,
                        "modelo": modelo, "obs": obs}

    return plano, monomodelo, achou


# ------------------------------------------------------------------ conferência

def conferir(plano, monomodelo, tipo):
    erros, avisos = [], []

    obrigatorios = OBRIGATORIOS_BASE + OBRIGATORIOS_EXTRA.get(tipo, [])
    for ident in obrigatorios:
        if ident not in plano:
            erros.append("agente obrigatorio ausente do plano: %s (%s)"
                         % (ident, tipo))
    for ident in OPCIONAIS_AVISO:
        if ident not in plano:
            avisos.append("agente %s ausente (opcional, mas confira se e' proposital)"
                          % ident)

    for ident, dados in sorted(plano.items()):
        if ident not in PADRAO:
            avisos.append("agente '%s' nao existe na linha da v7 (erro de digitacao?)"
                          % ident)
        if dados["degrau"] not in DEGRAUS:
            erros.append("agente %s: degrau invalido '%s' (use forte/medio/barato)"
                         % (ident, dados["degrau"] or "vazio"))
            continue
        if not dados["modelo"]:
            erros.append("agente %s: modelo nao declarado (4o campo) — sem ele "
                         "a diversidade nao e' verificavel" % ident)

        # T1 — travados
        if ident in TRAVADOS and dados["degrau"] != "forte":
            erros.append("T1 agente %s e' TRAVADO (nao aceita rebaixamento) e "
                         "esta em '%s'" % (ident, dados["degrau"]))

        # T7 — rebaixamento com motivo escrito
        padrao = PADRAO.get(ident)
        if padrao and dados["degrau"] in DEGRAUS and padrao in DEGRAUS:
            if DEGRAUS.index(dados["degrau"]) > DEGRAUS.index(padrao):
                salto = DEGRAUS.index(dados["degrau"]) - DEGRAUS.index(padrao)
                if salto > 1:
                    erros.append("T7 agente %s pulou degrau (%s -> %s); "
                                 "rebaixamento desce um degrau por vez"
                                 % (ident, padrao, dados["degrau"]))
                elif not dados["obs"]:
                    avisos.append("T7 agente %s rebaixado (%s -> %s) sem "
                                  "observacao escrita"
                                  % (ident, padrao, dados["degrau"]))

    modelos = {i: d["modelo"] for i, d in plano.items() if d["modelo"]}
    distintos = set(modelos.values())

    if len(distintos) <= 1 and modelos:
        if monomodelo:
            avisos.append("MODO monomodelo declarado: a linha inteira roda em "
                          "'%s'. A protecao contra erro correlacionado NAO "
                          "existe nessa configuracao — o portao humano vale "
                          "mais (ver §7 da modelos-agentes.md)"
                          % list(distintos)[0])
        else:
            erros.append("linha inteira em um unico modelo sem declarar "
                         "'MODO: monomodelo'. Ou roteie os agentes, ou declare "
                         "o modo e assuma a perda")

    grave = erros.append if not monomodelo else avisos.append

    # T2 — produtor x conferente
    for produtor, conferente, rotulo in PARES:
        mp = modelos.get(produtor)
        mc = modelos.get(conferente)
        if mp and mc and mp == mc:
            grave("T2 %s: produtor (%s) e conferente (%s) no MESMO modelo '%s' "
                  "— quem produz nao pode conferir, nem por modelo"
                  % (rotulo, produtor, conferente, mp))

    # T3 — painel de juizes
    modelos_juizes = [modelos[j] for j in JUIZES if j in modelos]
    if len(modelos_juizes) == 3:
        if len(set(modelos_juizes)) < 2:
            grave("T3 painel de juizes com um unico modelo (%s): erro "
                  "correlacionado nao e' quebrado por lente, so por modelo"
                  % modelos_juizes[0])
        modelo_editor = modelos.get(EDITOR_FINAL)
        if modelo_editor and all(m == modelo_editor for m in modelos_juizes):
            grave("T3 nenhum juiz roda em modelo diferente do editor-chefe "
                  "(%s) — quem assina o texto final nao pode ser o unico "
                  "ponto de vista do painel" % modelo_editor)

    return erros, avisos


# ------------------------------------------------------------------ main

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2

    caminho = sys.argv[1]
    tipo = (sys.argv[2].lower() if len(sys.argv) > 2 else "city")
    if tipo not in OBRIGATORIOS_EXTRA:
        print("tipo desconhecido '%s' — usando 'city'" % tipo)
        tipo = "city"

    try:
        plano, monomodelo, achou = parse(caminho)
    except OSError as exc:
        print("nao consegui ler o arquivo: %s" % exc)
        return 2

    print("=" * 68)
    print("CHECKPOINT DE MODELOS [V7.2] — %s (tipo: %s)" % (caminho, tipo))
    print("=" * 68)

    if not achou:
        print("\n❌ REPROVADO — nenhum bloco 'PLANO_MODELOS:' encontrado.")
        print("   O Agente 22 escreve o plano ANTES do Estagio 1.")
        print("   Formato: '# | funcao | degrau | modelo | observacao'")
        return 1

    print("\nAgentes no plano: %d" % len(plano))
    for ident in sorted(plano, key=lambda k: (len(k), k)):
        d = plano[ident]
        trava = " 🔒" if ident in TRAVADOS else ""
        print("  %-5s %-22s %-7s %-10s%s"
              % (ident, d["funcao"][:22], d["degrau"], d["modelo"], trava))

    erros, avisos = conferir(plano, monomodelo, tipo)

    if avisos:
        print("\n🟡 AVISOS (%d)" % len(avisos))
        for a in avisos:
            print("   - %s" % a)

    if erros:
        print("\n🔴 BLOQUEIOS (%d)" % len(erros))
        for e in erros:
            print("   - %s" % e)
        print("\n❌ REPROVADO — corrija o PLANO_MODELOS antes de disparar a linha.")
        return 1

    print("\n✅ APROVADO — roteamento coerente com as travas T1/T2/T3/T7.")
    if monomodelo:
        print("   (em modo monomodelo: o portao humano final nao e' opcional)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
