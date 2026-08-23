# Pillars — Conteúdo Bruto (fonte para teste de substituição anti-doorway)

**Sincronizado do projeto `tabelaplanos` em: 2026-06-08**
**Convertido para markdown limpo (HTML removido) em: 2026-06-08**

**Nota de nome:** dois arquivos foram renomeados para ASCII (o instalador de skill rejeita
acento em nome de arquivo). O mapa para os originais do projeto:
- `coparticipacao_guia_completo.md` ← projeto: `coparticipação_guia_completo.txt`
- `tabela_de_precos.md` ← projeto: `tabela_de_preços.txt`
Ao reconciliar com `/mnt/project/`, considere esse mapeamento.

Os pillars são **cópias do conteúdo** dos pillars do projeto, embutidas na skill para que o
protocolo anti-skip funcione em **qualquer conversa do Claude** — dentro ou fora do projeto.

**Formato:** os pillars que vinham como dump de HTML foram convertidos para **markdown de texto
(`.md`), com o HTML inline removido** — propósito destes arquivos é o teste de substituição
anti-doorway (estrutura + tópicos + frases), não renderização. O HTML cru inflava os arquivos
em ~2,5x e não agregava nada ao teste. As 3 capturas OCR seguem como `.txt` (já eram texto puro).

## ⚠️ Regra de reconciliação (leia antes de usar)

- A **fonte da verdade** é o conteúdo original no projeto (`/mnt/project/`) e a página publicada.
- Se você está **dentro do projeto** e os arquivos aparecem em `/mnt/project/`, leia de lá —
  pode estar mais novo que esta cópia. Ao ressincronizar, **reaplique a conversão HTML→markdown**
  (script no histórico de conversa) para não reintroduzir HTML cru.
- Se houver divergência, **o `/mnt/project/` vence** e esta cópia deve ser ressincronizada
  (atualizar os arquivos + a data no topo deste índice).
- Esta cópia é para **portabilidade**, não para substituir a fonte viva.

## Para que servem

NÃO são conteúdo a reproduzir. São o material contra o qual rodar o teste de substituição:
> "Esta frase do meu artigo de cidade é a versão resumida de algo que está aqui no pillar?"
> Se sim → reescrever com dado exclusivamente local + link. Se não → manter.

O mapa de "O QUE NÃO REPRODUZIR" por pillar (URLs, estruturas, listas) está em
`references/pillar-pages.md`. Estes `.txt` são o texto bruto que aquele mapa resume.

## Arquivos

| Arquivo | Tipo | Pillar / URL | Usado em (BRIDGE) |
|---|---|---|---|
| `coparticipacao_guia_completo.md` | Pillar nacional | `/tabela-precos-hapvida-coparticipacao-guia-completo/` | S2 |
| `carencias.md` | Pillar HUB | `/plano-de-saude-hapvida-carencia/` | S7 |
| `como_contratar.md` | Pillar nacional | `/como-contratar-plano-hapvida/` | S7 |
| `tabela_de_precos.md` | Pillar PAI (TR) | `/tabela-de-preco-hapvida/` | S2 / Critical Triangle TR |
| `plano_individual_hapvida.md` | Pillar produto | `/plano-individual-hapvida/` | S3/S7 / Critical Triangle TR |
| `plano_empresarial_hapvida.md` | Pillar produto | `/plano-empresarial-hapvida/` | S3/S7 / Critical Triangle TR |
| `nosso_plano.md` | Pillar produto | (produto Nosso Plano) | S3 |
| `plano_mix.md` | Pillar produto | (produto Plano Mix) | S3 |
| `nosso_medico.md` | Pillar produto | (produto Nosso Médico) | S3 |
| `notrelife.md` | Pillar produto | (produto NotreLife / 50+) | S3 |
| `o_que_o_plano_de_saude_cobre.md` | Pillar cobertura | `/cobertura/` (o que o plano cobre) | S5 / cobertura |
| `plano_hapvida_fortaleza.md` | **Artigo de cidade** (não é pillar) | `/plano-hapvida-fortaleza/` | Referência de cross-link e anti-doorway entre cidades |
| `captura-artigo-belo-horizonte-ocr.txt` | **Artigo de cidade** (captura OCR) | `/plano-hapvida-belo-horizonte/` | Anti-doorway + cross-link RMBH (Contagem, Betim, etc.) |
| `captura-artigo-recife-ocr.txt` | **Artigo de cidade** (captura OCR) | `/plano-hapvida-recife/` | Anti-doorway entre cidades NE |
| `captura-plano-individual-ocr.txt` | **Página de produto** (captura OCR) | `/plano-individual-hapvida/` | Anti-doorway (complementa `plano_individual_hapvida.md`) |

## Sobre as 3 capturas OCR (ex-"PDFs")

Os 3 arquivos `.pdf`/`.PDF` do projeto eram, na verdade, ZIPs com 12 imagens JPEG cada —
capturas das páginas publicadas (BH, Recife, Plano Individual). Foram convertidos por OCR
(tesseract pt-BR) em `.txt` e embutidos como referência anti-doorway.
- **Os preços/valores nessas capturas são IGNORADOS** — preço só via shortcode do WordPress.
- O OCR pode ter pequenos erros; o que vale é a **estrutura e os tópicos** da página.

## Itens do projeto que NÃO foram embutidos (e por quê)

- **`SKILL_database.md`**: é o `SKILL.md` de OUTRA skill (`hapvida-article-database`), não um pillar.
- **`database.md`**: arquivo vazio (0 bytes).
- **`sobre_a_coparticipação`**: regra de escrita de 1 linha — absorvida como nota no `SKILL.md`
  (item 8 do "O QUE LER"), não vira referência.
