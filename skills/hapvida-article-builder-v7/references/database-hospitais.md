# BANCO DE DADOS — ARTIGOS INDIVIDUAIS DE HOSPITAL

> ⚠️ **ARQUIVO DESCONTINUADO** — Este `.md` não é mais a fonte da verdade.
>
> O banco de hospitais migrou para o **Supabase**, consultado via MCP `BD - Consultar 3`. Para consultar hospitais, use:
> - `consultar_hospitais_cidade` — listar hospitais por cidade
> - `consultar_artigo` — buscar artigo de hospital específico
> - `consultar_overlaps_doorway` — overlaps com artigo de cidade
> - `consultar_faqs_catalogo` — FAQs já usadas
>
> Para registrar um novo artigo de hospital, use MCP `BD - criar`:
> - `registrar_artigo_novo`, `registrar_faqs_artigo`, `registrar_hospitais_artigo`, `registrar_links_artigo`
>
> O conteúdo abaixo é mantido como referência histórica (snapshot 2026-05-11). Não atualizar mais.

---

> Última atualização: 2026-05-11
> Total de artigos de hospital com registro completo neste arquivo: 6 (Vera Cruz BH adicionado em 2026-05-11 — V4.5.0 hospital)
> Hospitais produzidos NÃO registrados aqui (pendente sincronização): Hospital Antônio Prudente (Fortaleza), Hospital Octaviano Neves (BH), Hospital Lifecenter (BH) — total geral de sub-spokes hospitalares produzidos: 9
> Template: `references/artigo-hospital.md` (HS1-HS4 + FAQ + Conclusão)

---

## ÍNDICE

| Hospital | Cidade | UF | Slug | Artigo de Cidade Vinculado | Status |
|----------|--------|----|------|---------------------------|--------|
| Hospital Layr Maia | Belém | PA | `hospital-layr-maia-hapvida` | `/plano-hapvida-belem/` | Produzido |
| Hospital Aldeota | Fortaleza | CE | `hospital-aldeota-hapvida` | `/plano-hapvida-fortaleza/` | Produzido |
| Hospital Ilha do Leite | Recife | PE | `hospital-ilha-do-leite-hapvida` | `/plano-hapvida-recife/` | Produzido |
| Hospital Mandacaru | Recife | PE | `hospital-mandacaru-hapvida` | `/plano-hapvida-recife/` | Produzido |
| Hospital Jardim América | Goiânia | GO | `hospital-jardim-america-hapvida` | `/plano-hapvida-goiania/` | Produzido |
| **Hospital Vera Cruz** | **Belo Horizonte** | **MG** | **`hospital-vera-cruz-hapvida`** | **`/plano-hapvida-belo-horizonte/`** | **Produzido (V4.5.0 — auditoria rigorosa)** |

---

## HOSPITAIS CANDIDATOS (pendentes de produção)

| Hospital | Cidade | UF | Artigo Cidade V4? | Prioridade | Observação |
|----------|--------|----|-------------------|------------|------------|
| Hospital e Maternidade Rio Amazonas | Manaus | AM | Não (pré-V3) | Aguarda reformulação | 5 hospitais em Manaus — boa densidade para spokes |
| Hospital Santa Paula SP | São Paulo | SP | Sim (V4) | Verificar se é Hapvida | Não consta no banco como hospital próprio |
| Hospital Jardim América | Goiânia | GO | Sim (V4) | **Produzido** | PS 24h geral, 20+ espec., polo referência |
| Hospital Heliópolis | São Paulo | SP | Sim (V4) | Verificar se é Hapvida | Não consta no banco como hospital próprio |
| Hospital Aldeota | Fortaleza | CE | Sim (V4) | Alta | Zona leste, referência Fortaleza |
| Hospital Hapvida Ilha do Leite | Recife | PE | Sim (V4) | Alta | Referência Recife |
| Hospital Mandacaru | Recife | PE | Sim (V4) | Alta | 2º hospital Recife |
| Hospital Vila Penteado | São Paulo | SP | Sim (V4) | Verificar se é Hapvida | Não consta no banco como hospital próprio |
| Hospital Rio Mar | Belém | PA | Sim (V4) | Alta | R$ 92M modernização, trauma 24h |
| Hospital Promed | Goiânia | GO | Sim (V4) | Alta | Ortopédico 24h exclusivo |

---

## REGISTROS COMPLETOS

---

### HOSPITAL LAYR MAIA — BELÉM/PA
- **Slug:** `hospital-layr-maia-hapvida`
- **URL sugerida:** https://tabelaplanos.com.br/hospital-layr-maia-hapvida/
- **Status:** Produzido (abr/2026)
- **Artigo de cidade vinculado:** Belém (`/plano-hapvida-belem/`)
- **Tipo:** Materno-infantil exclusivo
- **Keyword-alvo:** `hospital layr maia hapvida`, `hospital layr maia belém`
- **Título SEO:** Hospital Layr Maia Hapvida Belém: Guia Completo [ano_atual]
- **Meta Description:** Tudo sobre o Hospital Layr Maia da Hapvida em Belém: maternidade, UTI neonatal, parto humanizado, como chegar e quais planos dão acesso. Guia [ano_atual].
- **H2 usados (6):**
  1. O Primeiro Hospital 100% Materno-Infantil da Hapvida no Norte (`#diferencial`) — HS1
  2. Experiência da Gestante e da Mãe no Layr Maia (`#experiencia`) — HS2
  3. Como Chegar ao Hospital Layr Maia (`#como-chegar`) — HS3
  4. Quais Planos Hapvida Dão Acesso ao Layr Maia (`#planos-acesso`) — HS4
  5. Dúvidas Sobre o Hospital Layr Maia (`#faq`) — FAQ
  6. Hospital Layr Maia: Atendimento Materno-Infantil Dedicado em Belém (`#conclusao`) — Conclusão
- **FAQ perguntas (7):**
  1. O Hospital Layr Maia tem PA pediátrico 24 horas?
  2. Como funciona o parto humanizado no Hospital Layr Maia?
  3. A UTI Neonatal do Hospital Layr Maia atende prematuros?
  4. Preciso de encaminhamento para ser atendida no Hospital Layr Maia?
  5. O Hospital Layr Maia faz exames de imagem e laboratório internamente?
  6. Tem estacionamento no Hospital Layr Maia?
  7. Posso fazer o pré-natal direto no Hospital Layr Maia?
- **Destaques animados:** 7
- **Menções DRV:** 1 (Dica DRV no HS2)
- **`[elementor-template]`:** 2 (após HS2 + após FAQ)
- **Shortcodes:** `[ano_atual]` × 3, `[mes_atual]` × 2
- **Links internos DE este artigo PARA:**

| Destino | Tipo | Onde no artigo | Âncora |
|---------|------|----------------|--------|
| `/plano-hapvida-belem/` | Artigo de cidade (hub) | Lead, HS4, Conclusão | — |
| `/plano-hapvida-belem/#rede-belem` | Artigo de cidade S4 | HS2 (encaminhamento Rio Mar) | `#rede-belem` |
| `/plano-hapvida-belem/#cobertura-bairros` | Artigo de cidade S5 | HS3 (cobertura bairros) | `#cobertura-bairros` |
| `/plano-hapvida-ananindeua/` | Cross-link cidade | HS1 (RMB) | — |
| `/tabela-precos-hapvida-coparticipacao-guia-completo/` | Pillar coparticipação | HS2 (box Importante) + HS4 | — |
| `/plano-de-saude-hapvida-carencia/` | Pillar carências | FAQ #3 (300 dias parto) | — |
| `/nosso-plano-hapvida/` | Pillar produto | HS4 | — |
| `/plano-mix-hapvida/` | Pillar produto | HS4 | — |

- **Links internos QUE DEVEM APONTAR PARA este artigo (pendentes de inserção):**

| Origem | Onde inserir | Texto-âncora sugerido |
|--------|-------------|----------------------|
| `/plano-hapvida-belem/` (S4) | Card ou parágrafo sobre Layr Maia | "Veja o guia completo do Hospital Layr Maia" |
| `/plano-hapvida-ananindeua/` (seção hospital) | Menção ao Layr Maia | "Conheça o Hospital Layr Maia em detalhes" |
| `/rede-propria-hapvida/` (Região Norte) | Lista hospitais Belém | "Guia do Hospital Layr Maia" |

- **Links externos:**
  - https://cidades.ibge.gov.br/brasil/pa/belem/panorama (nofollow)
  - https://www.gov.br/ans/pt-br (nofollow)
- **Anti-doorway verificado:**
  - Zero explicação de coparticipação (1 frase + link) ✅
  - Zero tabela de carências (1 menção 300 dias + link) ✅
  - Zero lista de documentos ✅
  - Zero steps de contratação ✅
  - Zero modelo verticalizado ✅
  - Endereço apenas na HS3 (Como Chegar) ✅
- **Overlap com artigo de Belém:**
  - FAQ #2 Belém ("diferença Rio Mar e Layr Maia") → NÃO repetida ✅
  - FAQ #7 Belém ("gestante pode usar Layr Maia para parto?") → NÃO repetida ✅
- **Overlap com artigo de Ananindeua:**
  - FAQ #8 Ananindeua ("Layr Maia atende gestantes de Ananindeua?") → NÃO repetida ✅
- **Campo semântico:** hospital layr maia, layr maia hapvida, maternidade hapvida belém, hospital materno-infantil belém, parto humanizado hapvida, UTI neonatal belém, pediatria hapvida belém, hospital nazaré belém, gestante hapvida, pronto atendimento pediátrico belém

---

### HOSPITAL ALDEOTA — FORTALEZA/CE
- **Slug:** `hospital-aldeota-hapvida`
- **URL sugerida:** https://tabelaplanos.com.br/hospital-aldeota-hapvida/
- **Status:** Produzido (abr/2026)
- **Artigo de cidade vinculado:** Fortaleza (`/plano-hapvida-fortaleza/`)
- **Tipo:** Hospital geral com emergência pediátrica dedicada + maternidade
- **Keyword-alvo:** `hospital aldeota hapvida`, `hospital aldeota fortaleza`
- **Título SEO:** Hospital Aldeota Hapvida Fortaleza: Guia Completo [ano_atual]
- **Meta Description:** Hospital Aldeota da Hapvida em Fortaleza: emergência pediátrica 24h, maternidade com 1.500+ partos/ano, banco de sangue e como chegar. Guia [ano_atual].
- **H2 usados (6):**
  1. A Única Emergência Pediátrica Dedicada 24h da Hapvida em Fortaleza (`#diferencial`) — HS1
  2. Experiência do Paciente no Hospital Aldeota (`#experiencia`) — HS2
  3. Como Chegar ao Hospital Aldeota (`#como-chegar`) — HS3
  4. Quais Planos Hapvida Dão Acesso ao Hospital Aldeota (`#planos-acesso`) — HS4
  5. Dúvidas Sobre o Hospital Aldeota (`#faq`) — FAQ
  6. Hospital Aldeota: Emergência Pediátrica, Maternidade e Banco de Sangue na Zona Leste de Fortaleza (`#conclusao`) — Conclusão
- **FAQ perguntas (7):**
  1. O Hospital Aldeota tem emergência pediátrica 24 horas?
  2. A maternidade do Hospital Aldeota faz parto humanizado?
  3. O Hospital Aldeota tem banco de sangue próprio?
  4. Preciso de encaminhamento para levar meu filho ao PS do Hospital Aldeota?
  5. O Hospital Aldeota faz cirurgias de alta complexidade?
  6. Tem estacionamento no Hospital Aldeota?
  7. O Hospital Aldeota atende pacientes adultos ou é só pediátrico?
- **Destaques animados:** 7
- **Menções DRV:** 1 (Dica DRV no HS2)
- **`[elementor-template]`:** 2 (após HS2 + após FAQ)
- **Shortcodes:** `[ano_atual]` × 3, `[mes_atual]` × 2
- **Links internos DE este artigo PARA:**

| Destino | Tipo | Onde no artigo |
|---------|------|----------------|
| `/plano-hapvida-fortaleza/` | Artigo de cidade (hub) | Lead, HS2, HS4, Conclusão |
| `/plano-hapvida-fortaleza/#rede-fortaleza` | S4 cidade | HS1 (encaminhamento Antônio Prudente) |
| `/plano-hapvida-fortaleza/#cobertura-bairros` | S5 cidade | HS3 (cobertura bairros) |
| `/tabela-precos-hapvida-coparticipacao-guia-completo/` | Pillar coparticipação | HS2 (box Importante) + HS4 |
| `/nosso-plano-hapvida/` | Pillar produto | HS4 |
| `/plano-mix-hapvida/` | Pillar produto | HS4 |
| `/rede-propria-hapvida/` | Pillar rede | HS1 |

- **Links internos QUE DEVEM APONTAR PARA este artigo (pendentes de inserção):**

| Origem | Onde inserir | Texto-âncora sugerido |
|--------|-------------|----------------------|
| `/plano-hapvida-fortaleza/` (S4) | Card ou parágrafo sobre Aldeota | "Veja o guia completo do Hospital Aldeota" |
| `/rede-propria-hapvida/` (Região Nordeste) | Lista hospitais Fortaleza | "Guia do Hospital Aldeota" |
| `/cobertura-completa-hapvida-fortaleza/` | Menção ao hospital | "Conheça o Hospital Aldeota em detalhes" |

- **Links externos:**
  - https://cidades.ibge.gov.br/brasil/ce/fortaleza/panorama (nofollow)
  - https://www.gov.br/ans/pt-br (nofollow)
- **Anti-doorway verificado:** ✅ (zero copart/carência/docs/verticalizado)
- **Overlap com artigo de Fortaleza:** FAQ #8 ("Aldeota, Meireles e Cocó") e #10 ("parto humanizado") → NÃO repetidas ✅
- **Overlap com Hospital Layr Maia (Belém):** Nenhum (cidade diferente) ✅
- **Campo semântico:** hospital aldeota, hospital aldeota hapvida, hospital aldeota fortaleza, emergência pediátrica fortaleza, maternidade hapvida fortaleza, UTI pediátrica fortaleza, banco de sangue hapvida, parto aldeota, PS pediátrico 24h fortaleza, zona leste fortaleza, av padre antônio tomás

---

### HOSPITAL ILHA DO LEITE — RECIFE/PE
- **Slug:** `hospital-ilha-do-leite-hapvida`
- **URL sugerida:** https://tabelaplanos.com.br/hospital-ilha-do-leite-hapvida/
- **Status:** Produzido (abr/2026)
- **Artigo de cidade vinculado:** Recife (`/plano-hapvida-recife/`)
- **Tipo:** Hospital geral com hemodinâmica 24h + maternidade + pediatria
- **Keyword-alvo:** `hospital ilha do leite hapvida`, `hospital hapvida ilha do leite`
- **Título SEO:** Hospital Ilha do Leite Hapvida Recife: Guia Completo [ano_atual]
- **Meta Description:** Hospital Ilha do Leite da Hapvida em Recife: urgência 24h, maternidade, hemodinâmica, 200+ leitos e UTI neonatal. Como funciona, como chegar e planos com acesso.
- **H2 usados (6):**
  1. O Hospital-Âncora da Hapvida em Pernambuco Desde 2008 (`#diferencial`) — HS1
  2. Experiência do Paciente no Hospital Ilha do Leite (`#experiencia`) — HS2
  3. Como Chegar ao Hospital Ilha do Leite (`#como-chegar`) — HS3
  4. Quais Planos Hapvida Dão Acesso ao Ilha do Leite (`#planos-acesso`) — HS4
  5. Dúvidas Sobre o Hospital Ilha do Leite (`#faq`) — FAQ
  6. Hospital Ilha do Leite: Hemodinâmica, Maternidade e 17 Anos de Operação no Recife (`#conclusao`) — Conclusão
- **FAQ perguntas (7):**
  1. O Hospital Ilha do Leite tem hemodinâmica 24 horas?
  2. A maternidade do Hospital Ilha do Leite faz partos de alto risco?
  3. Qual a diferença entre o Hospital Ilha do Leite e o Ariano Suassuna?
  4. O PS do Hospital Ilha do Leite atende crianças?
  5. Preciso de encaminhamento para ser atendido no Hospital Ilha do Leite?
  6. Tem estacionamento no Hospital Ilha do Leite?
  7. O Hospital Ilha do Leite faz cirurgia cardíaca?
- **Destaques animados:** 7
- **Menções DRV:** 1 (Dica DRV no HS2)
- **`[elementor-template]`:** 2 (após HS2 + após FAQ)
- **Links internos DE este artigo PARA:**

| Destino | Tipo | Onde (1×) |
|---------|------|-----------|
| `/plano-hapvida-recife/` | Hub cidade | HS4 |
| `/tabela-precos-hapvida-coparticipacao-guia-completo/` | Pillar copart | HS2 (box Importante) |
| `/plano-de-saude-hapvida-carencia/` | Pillar carências | FAQ #2 |
| `/cobertura-completa-hapvida-recife/` | Cross-link cobertura | HS3 |

- **Links internos QUE DEVEM APONTAR PARA este artigo (pendentes):**

| Origem | Onde inserir | Texto sugerido |
|--------|-------------|----------------|
| `/plano-hapvida-recife/` (seção rede) | Ficha Ilha do Leite | "Veja o guia completo do Hospital Ilha do Leite" |
| `/rede-propria-hapvida/` (Nordeste) | Lista hospitais Recife | "Guia do Hospital Ilha do Leite" |
| `/cobertura-completa-hapvida-recife/` | Menção ao hospital | "Conheça o Hospital Ilha do Leite em detalhes" |
| `/hospital-mandacaru-hapvida/` | FAQ #5 (UTI Pediátrica) | Mandacaru referencia Ilha do Leite — link bidirecional |

- **Links externos:**
  - https://www2.hapvida.com.br/unidades/hospital-ilha-do-leite (corpo HS1)
  - https://cnes.datasus.gov.br/ (rodapé)
  - https://www.cremepe.org.br/ (rodapé)
- **Anti-doorway verificado:** ✅
- **Overlap com artigo de Recife:** FAQ #2 ("Quais hospitais atendem 24h") e #3 ("Quais fazem parto") e #17 ("O que é o Ariano Suassuna") → NÃO repetidas ✅
- **Overlap com Layr Maia e Aldeota:** Nenhum (cidades diferentes) ✅
- **Campo semântico:** hospital ilha do leite, hospital ilha do leite hapvida, hapvida ilha do leite recife, hemodinâmica hapvida, maternidade hapvida recife, UTI neonatal recife, urgência 24h recife, cateterismo hapvida, hospital ariano suassuna, estação joana bezerra

---

### HOSPITAL MANDACARU — RECIFE/PE
- **Slug:** `hospital-mandacaru-hapvida`
- **URL sugerida:** https://tabelaplanos.com.br/hospital-mandacaru-hapvida/
- **Status:** Produzido (abr/2026)
- **Artigo de cidade vinculado:** Recife (`/plano-hapvida-recife/`)
- **Tipo:** 100% pediátrico exclusivo
- **Keyword-alvo:** `hospital mandacaru hapvida`, `hospital mandacaru recife`
- **Título SEO:** Hospital Mandacaru Hapvida Recife: Guia Completo [ano_atual]
- **Meta Description:** Hospital Mandacaru da Hapvida em Recife: primeiro hospital 100% pediátrico da rede em PE. Urgência infantil, internação, como chegar e planos com acesso.
- **H2 usados (6):**
  1. O Único Hospital 100% Pediátrico da Hapvida em Pernambuco (`#diferencial`) — HS1
  2. Experiência do Paciente no Hospital Mandacaru (`#experiencia`) — HS2
  3. Como Chegar ao Hospital Mandacaru (`#como-chegar`) — HS3
  4. Quais Planos Hapvida Dão Acesso ao Mandacaru (`#planos-acesso`) — HS4
  5. Dúvidas Sobre o Hospital Mandacaru (`#faq`) — FAQ
  6. Hospital Mandacaru: Pediatria Exclusiva no Polo Médico do Recife (`#conclusao`) — Conclusão
- **FAQ perguntas (7):**
  1. O Hospital Mandacaru atende apenas crianças?
  2. Até que idade o Hospital Mandacaru atende?
  3. O Hospital Mandacaru tem centro cirúrgico pediátrico?
  4. Preciso de encaminhamento para levar meu filho ao Hospital Mandacaru?
  5. O Hospital Mandacaru tem UTI Pediátrica?
  6. Qual a diferença entre o Hospital Mandacaru e a pediatria do Ilha do Leite?
  7. Tem estacionamento no Hospital Mandacaru?
- **Destaques animados:** 6
- **Menções DRV:** 1 (Dica DRV no HS2)
- **`[elementor-template]`:** 2 (após HS2 + após FAQ)
- **Links internos DE este artigo PARA:**

| Destino | Tipo | Onde (1×) |
|---------|------|-----------|
| `/plano-hapvida-recife/` | Hub cidade | HS4 |
| `/tabela-precos-hapvida-coparticipacao-guia-completo/` | Pillar copart | HS2 (box Importante) |
| `/plano-de-saude-hapvida-carencia/` | Pillar carências | FAQ #3 |
| `/plano-de-saude-barato/` | Pillar temático | HS4 (contexto acessibilidade) |
| `/hospital-ilha-do-leite-hapvida/` | Cross-link hospital mesma cidade | FAQ #6 |

- **Links internos QUE DEVEM APONTAR PARA este artigo (pendentes):**

| Origem | Onde inserir | Texto sugerido |
|--------|-------------|----------------|
| `/plano-hapvida-recife/` (seção rede) | Ficha Mandacaru | "Veja o guia completo do Hospital Mandacaru" |
| `/hospital-ilha-do-leite-hapvida/` | FAQ #4 (pediatria) | "Para atendimento 100% pediátrico, veja o Hospital Mandacaru" |
| `/rede-propria-hapvida/` (Nordeste) | Lista hospitais Recife | "Guia do Hospital Mandacaru" |
| `/plano-de-saude-hapvida-infantil/` | Seção rede | "Hospital pediátrico exclusivo em Recife" |

- **Links externos:**
  - https://www2.hapvida.com.br/unidades/hospital-mandacaru (corpo HS1)
  - https://cnes.datasus.gov.br/ (rodapé)
  - https://www.cremepe.org.br/ (rodapé)
- **Anti-doorway verificado:** ✅
- **Overlap com artigo de Recife:** FAQ #2 ("Quais hospitais atendem 24h") → NÃO repetida ✅
- **Overlap com Ilha do Leite (mesma cidade):** FAQ #4 ("PS atende crianças") — ângulos diferentes: Ilha do Leite = "sim, tem setor pediátrico" / Mandacaru = "é 100% pediátrico" ✅ FAQ #6 Mandacaru referencia Ilha do Leite com link cruzado ✅
- **Campo semântico:** hospital mandacaru, hospital mandacaru hapvida, hospital pediátrico recife, pediatria hapvida recife, urgência infantil recife, cirurgia pediátrica hapvida, hospital infantil recife, torreão recife, av agamenon magalhães

---

### HOSPITAL JARDIM AMÉRICA — GOIÂNIA/GO
- **Slug:** `hospital-jardim-america-hapvida`
- **URL sugerida:** https://tabelaplanos.com.br/hospital-jardim-america-hapvida/
- **Status:** Produzido (abr/2026)
- **Artigo de cidade vinculado:** Goiânia (`/plano-hapvida-goiania/`)
- **Tipo:** Hospital geral de alta complexidade (maior unidade Hapvida no Centro-Oeste)
- **Keyword-alvo:** `hospital jardim américa hapvida`, `hospital jardim américa goiânia`
- **Título SEO:** Hospital Jardim América Hapvida Goiânia: Guia Completo [ano_atual]
- **Meta Description:** Tudo sobre o Hospital Jardim América da Hapvida em Goiânia: PS 24h, 1.000+ cirurgias/mês, alta complexidade, como chegar e quais planos dão acesso. Guia [ano_atual].
- **H2 usados (6):**
  1. O Maior Hospital Hapvida do Centro-Oeste: 43 Anos de Operação em Goiânia (`#diferencial`) — HS1
  2. Experiência do Paciente no Hospital Jardim América (`#experiencia`) — HS2
  3. Como Chegar ao Hospital Jardim América (`#como-chegar`) — HS3
  4. Quais Planos Hapvida Dão Acesso ao Hospital Jardim América (`#planos-acesso`) — HS4
  5. Dúvidas Sobre o Hospital Jardim América (`#faq`) — FAQ
  6. Hospital Jardim América: Alta Complexidade com 43 Anos de Presença em Goiânia (`#conclusao`) — Conclusão
- **FAQ perguntas (7):**
  1. O Hospital Jardim América tem pronto-socorro 24 horas para adultos e crianças?
  2. Quantas cirurgias o Hospital Jardim América realiza por mês?
  3. O Hospital Jardim América faz cirurgia cardíaca e neurológica?
  4. O Hospital Jardim América faz exames de ressonância e tomografia?
  5. Preciso de encaminhamento para ser atendido no Hospital Jardim América?
  6. Tem estacionamento no Hospital Jardim América?
  7. O Hospital Jardim América atende pacientes de Anápolis e do interior de Goiás?
- **Destaques animados:** 6
- **Menções DRV:** 1 (conclusão)
- **`[elementor-template]`:** 2 (após HS2 + após FAQ)
- **Shortcodes:** `[ano_atual]` × 1, `[mes_atual]` × 1
- **Links internos DE este artigo PARA:**

| Destino | Tipo | Onde (1×) |
|---------|------|-----------|
| `/promed-plano-de-saude/` | Pillar/temático Promed | HS1 (diferenciação ortopedia) |
| `/endoscopia-preco-popular-2/` | Pillar/temático endoscopia | HS2 (exames integrados) |
| `/plano-hapvida-anapolis/` | Cross-link cidade vizinha | HS3 (pacientes do interior) |
| `/plano-hapvida-goiania/` | Hub cidade | HS4 (guia completo) |
| `/urgencia-e-emergencia-hapvida/` | Pillar urgência/emergência | FAQ #3 (hemodinâmica + PS) |

- **Links internos QUE DEVEM APONTAR PARA este artigo (pendentes de inserção):**

| Origem | Onde inserir | Texto-âncora sugerido |
|--------|-------------|----------------------|
| `/plano-hapvida-goiania/` (S4) | Card hero Hospital Jardim América | "Veja o guia completo do Hospital Jardim América" |
| `/plano-hapvida-anapolis/` (seção hospital) | Menção internações em Goiânia | "Conheça o Hospital Jardim América em detalhes" |
| `/rede-propria-hapvida/` (Centro-Oeste) | Lista hospitais Goiânia | "Guia do Hospital Jardim América" |

- **Links externos:**
  - https://www2.hapvida.com.br/unidades/hospital-jardim-america (corpo HS1 — página oficial)
  - https://cremego.org.br/ (rodapé — CRM-GO)
- **Anti-doorway verificado:**
  - Zero explicação de coparticipação (1 frase "internações isentas" no box Importante) ✅
  - Zero tabela de carências ✅
  - Zero lista de documentos ✅
  - Zero steps de contratação ✅
  - Zero modelo verticalizado explicado ✅
  - Endereço: lead (1×) + HS3 (1×) ✅
- **Overlap com artigo de Goiânia:**
  - FAQ #1 GO ("tem hospital próprio?") → NÃO repetida (ângulo diferente: GO pergunta se existe, hospital pergunta se tem PS 24h para adultos e crianças) ✅
  - FAQ #3 GO ("Promed atende ortopédica?") → NÃO repetida (hospital diferente) ✅
  - FAQ #4 GO ("cobre Aparecida e Anápolis?") → NÃO repetida (FAQ#7 hospital = ângulo paciente encaminhado, não cobertura do plano) ✅
  - FAQ #6 GO ("cobre parto?") → NÃO repetida ✅
- **Overlap com outros artigos de hospital (mesma cidade):** Nenhum artigo de hospital produzido em Goiânia anteriormente. Próximo candidato: Hospital Promed (ortopédico) — FAQ e conteúdo devem ser cruzados.
- **Campo semântico:** hospital jardim américa, hospital jardim américa hapvida, hapvida jardim américa goiânia, hospital hapvida goiânia, grupo américa hapvida, pronto socorro jardim américa, UTI jardim américa, cirurgia cardíaca hapvida goiânia, hemodinâmica hapvida goiânia, maternidade hapvida goiânia, av t-63 goiânia, centro-oeste hapvida

---

### HOSPITAL VERA CRUZ — BELO HORIZONTE/MG
- **Slug:** `hospital-vera-cruz-hapvida`
- **URL:** https://tabelaplanos.com.br/hospital-vera-cruz-hapvida/
- **Status:** Produzido (2026-05-11) — auditado com rigor factual. Pendente publicação.
- **Versão:** V4.5.0 hospital
- **Artigo de cidade vinculado:** Belo Horizonte (`/plano-hapvida-belo-horizonte/` — V4.3.2, pendente inserção de link recíproco no S4 Card Vera Cruz)
- **Tipo:** Hospital geral de tradição (PS 24h + cardiologia histórica)
- **Anchor central:** Hospital de maior tradição entre os 3 próprios BH (inaugurado em 9/abril/1949) + pioneiro em cirurgia cardiovascular em Minas Gerais + porta de entrada de urgência da rede vertical Hapvida na capital
- **Keyword-alvo:** `hospital vera cruz hapvida`, `hospital vera cruz bh`, `vera cruz belo horizonte`, `vera cruz convênio hapvida`, `vera cruz barbacena`
- **Título SEO:** Hospital Vera Cruz Hapvida BH: Guia Completo [ano_atual] (~52 chars)
- **Meta Description:** Hospital Vera Cruz Hapvida BH: tradição em cardiologia, PS 24h, UTI adulto e UCO na Av. Barbacena. Como funciona e quais planos dão acesso. Guia [ano_atual]. (~158 chars)
- **H2 usados (6):**
  1. Por Que o Vera Cruz é o Hospital de Tradição da Rede Hapvida em BH (`#diferencial`) — HS1
  2. Atendimento de Urgência no Vera Cruz: Da Triagem à Internação (`#experiencia`) — HS2
  3. Como Chegar ao Vera Cruz na Av. Barbacena (`#como-chegar`) — HS3
  4. Quais Planos Hapvida Dão Acesso ao Vera Cruz (`#planos-acesso`) — HS4
  5. Dúvidas Sobre o Hospital Vera Cruz (`#faq`) — FAQ
  6. Hospital Vera Cruz: Tradição Cardiovascular de MG na Rede Verticalizada Hapvida (`#conclusao`) — Conclusão

- **FAQ perguntas (8 — 100% nominam o hospital):**
  1. Por que o Hospital Vera Cruz é o hospital de maior tradição da rede própria Hapvida em BH?
  2. Qual a diferença entre o Hospital Vera Cruz (Av. Barbacena) e o Pronto Atendimento do Hospital Vera Cruz (Rua Paracatu)?
  3. Como o Hospital Vera Cruz se tornou referência em cardiologia em Minas Gerais?
  4. Em quais casos o Vera Cruz transfere o paciente para o Hospital Lifecenter ou para o Octaviano Neves?
  5. O Hospital Vera Cruz tem centro cirúrgico para urgências ortopédicas e cirurgia geral?
  6. O Hospital Vera Cruz tem setor de diagnóstico por imagem para apoiar o atendimento de urgência?
  7. O Hospital Vera Cruz tem UCO (Unidade Coronariana) e UTI adulto pelo plano Hapvida?
  8. Como chegar ao Hospital Vera Cruz (Av. Barbacena, 653) vindo da Pampulha, Savassi e Contagem?

- **Métricas pós-auditoria rigorosa:**
  - Tamanho: 33.824 caracteres / 2.055 palavras
  - Densidade Hapvida: 1.17% (≤1.6%) | Vera Cruz: 2.14% | BH/Belo Horizonte: 1.22% (≤1.4%)
  - Destaques animados: 11 (mín. 6)
  - Parágrafos >56 palavras: 0
  - Emojis: 0 | DRV menções: 1 (badge Dica DRV)
  - Elementor templates: 2 | id="cotacao-1": 1
  - Links internos únicos: 5 | Links externos únicos: 2

- **Dados únicos (TODOS verificados em fonte primária — auditoria rigorosa aplicada):**
  - **Inaugurado em 9 de abril de 1949** (IBGE citando hvc.com.br/pagina/historia)
  - **3 fundadores:** Dr. Sylvio Miraglia, Dr. Antônio Figueiredo Starling, engenheiro Dr. Ajax Rabello
  - **Dr. Sebastião Rabello (filho do fundador Dr. Ajax)** — responsável pelo pioneirismo em cirurgia cardiovascular em MG
  - **Apoio histórico das Irmãs Franciscanas Hospitaleiras do Imaculado Conceição** (indicação do Arcebispo Dom Antônio dos Santos Cabral)
  - **Hospital de maior tradição entre os 3 próprios BH:** Octaviano Neves 1964 / Lifecenter 2002 / Vera Cruz **1949**
  - **Estrutura confirmada (sem números específicos no artigo):** UTI adulto + UCO (Unidade Coronariana) + centro cirúrgico para procedimentos de pequeno, médio e grande porte com foco em alta complexidade + hemodinâmica + diagnóstico por imagem + PS 24h com classificação de risco
  - **30+ especialidades médicas** atendidas (hvc.com.br/quem-somos)
  - **Aquisição via Grupo Promed:** anúncio 8/set/2020, conclusão 20/mai/2021, R$ 1,5 bi (3 hospitais + 7 clínicas + 3 operadoras absorvidas)
  - **Endereço:** Av. Barbacena, 653 — Barro Preto, Belo Horizonte/MG (CEP NÃO incluído no artigo — fontes secundárias divergem)
  - **Unidade satélite distinta:** Pronto Atendimento do Hospital Vera Cruz — Rua Paracatu, 724, Santo Agostinho (confirmado em portal oficial Hapvida)
  - **DADOS REMOVIDOS DO ARTIGO POR FALTA DE FONTE PRIMÁRIA:** telefone (31) 3337-1000 | CEP 30190-130 | números 24 UTI + 10 UCO | ano 2009 da implantação da classificação de risco | "década de 1950" para o pioneirismo cardiovascular | "hospital-âncora da transação" | "um dos primeiros da saúde privada em BH" | listas específicas de tipos de cirurgia/exames

- **Links internos (5 únicos, cada 1×):**
  - `/rede-propria-hapvida/` — HS1 P2 (registro na rede própria nacional)
  - `/plano-de-saude-hapvida-carencia/` — HS2 Box Importante (regra urgência 24h ANS)
  - `/plano-hapvida-contagem/` — HS3 P último (rota Eldorado)
  - `/plano-hapvida-belo-horizonte/` — HS4 P último (hub cidade obrigatório)
  - `/hospital-lifecenter-hapvida-bh/` — FAQ #4 (transferência intra-rede cirurgia eletiva)

- **Links externos (2 únicos):**
  - `https://www2.hapvida.com.br/unidades/hospital-vera-cruz` — corpo HS1 (página oficial)
  - `https://www.crmmg.org.br/` — rodapé Conclusão (CRM-MG)

- **Links QUE DEVEM APONTAR PARA este artigo (reciprocidade pendente):**
  - `/plano-hapvida-belo-horizonte/` S4 Card Vera Cruz (linha 3779 do HTML atual) — texto-âncora: "Veja o guia completo do Hospital Vera Cruz"
  - `/plano-hapvida-contagem/` (encaminhamento urgência) — texto-âncora: "Hospital Vera Cruz (BH, PS 24h)"
  - `/plano-hapvida-betim/` (encaminhamento urgência) — texto-âncora: "Hospital Vera Cruz em BH"
  - `/plano-hapvida-santa-luzia/` (encaminhamento urgência)
  - `/plano-hapvida-ribeirao-das-neves/` (encaminhamento urgência)
  - `/rede-propria-hapvida/` (seção Sudeste/MG)
  - `/promed-plano-de-saude/` (quando reformulada — Vera Cruz como hospital-âncora da aquisição set/2020)
  - `/hospital-octaviano-neves-hapvida/` (diferenciação interna BH — texto-âncora: "Hospital Vera Cruz (PS 24h e UCO)")
  - `/hospital-lifecenter-hapvida-bh/` (reciprocidade — atualmente só Vera Cruz linka Lifecenter; falta inverso)
  - `/plano-de-saude-hapvida-carencia/` (porta de urgência 24h em BH)

- **Overlap com artigo de cidade (BH city V4.3.2):**
  - FAQ #1 BH (3 hospitais próprios) → NÃO repetida no sub-spoke (anchor BH é "Vera Cruz no contexto dos 3"; anchor sub-spoke é "Vera Cruz especificamente") ✅
  - S4 BH city descreve Vera Cruz em 1 bullet + endereço; sub-spoke aprofunda em HS1-HS4 (autorizado pelo skill) ✅
  - Endereço Av. Barbacena, 653: BH city S4 bullet + sub-spoke Lead/HS3 (≤2 menções no sub-spoke, autorizado) ✅

- **Overlap com sub-spokes BH irmãos (Octaviano + Lifecenter):**
  - Octaviano: materno-infantil + UTI Neonatal Nível III (zero overlap com Vera Cruz)
  - Lifecenter: cirurgia eletiva alta complexidade + ONA III (zero overlap com Vera Cruz)
  - Vera Cruz: tradição cardiovascular + PS 24h + UCO (anchor único)
  - ⚠️ Hemodinâmica: ambos Vera Cruz e Lifecenter têm. Vera Cruz usa ângulo histórico/UCO; Lifecenter usa ângulo moderno/eletivo (pode precisar de refinamento na FAQ #3 do Lifecenter — pendente).

- **Campo semântico:** hospital vera cruz, hospital vera cruz hapvida, vera cruz bh, vera cruz belo horizonte, vera cruz barbacena, vera cruz barro preto, PS 24h hapvida bh, UCO hapvida bh, hemodinâmica hapvida bh, cirurgia cardiovascular bh, sebastião rabello, ajax rabello, hospital de tradição bh, hospital antigo bh



### Entre artigos de hospital da mesma cidade
- **FAQ:** ZERO overlap — nenhuma pergunta pode aparecer em dois artigos de hospital da mesma cidade
- **Conteúdo HS1:** Cada hospital deve ter posicionamento DIFERENTE (materno-infantil vs trauma vs ortopédico)
- **Conteúdo HS2:** Experiências são naturalmente únicas por hospital
- **Links cruzados:** Artigos de hospital da mesma cidade DEVEM se referenciar mutuamente ("para emergência ortopédica, veja o Hospital Promed")

### Entre artigo de hospital e artigo de cidade
- **FAQ:** ZERO overlap — cruzar antes de produzir
- **S4 do artigo de cidade:** Artigo de hospital DEVE linkar para a S4 como referência e a S4 DEVE linkar para o artigo de hospital quando existir
- **Endereço/telefone:** Artigo de hospital usa APENAS na HS3 (como chegar), com ângulo de acesso

### Linkagem bidirecional obrigatória
Quando um artigo de hospital é publicado:
1. **Inserir link no artigo de cidade (S4)** → apontando para o artigo de hospital
2. **Inserir link no pillar Rede Própria** → na listagem regional do hospital
3. **Inserir link em artigos de cidade vizinha** (se o hospital atende beneficiários da RM) → ex: Ananindeua linka para Layr Maia
4. **Registrar todos os links neste banco** na tabela "Links que DEVEM APONTAR PARA este artigo"

---

## REGRAS DE CRUZAMENTO

### Entre artigos de hospital da mesma cidade
- **FAQ:** ZERO overlap — nenhuma pergunta pode aparecer em dois artigos de hospital da mesma cidade
- **Conteúdo HS1:** Cada hospital deve ter posicionamento DIFERENTE (materno-infantil vs trauma vs ortopédico)
- **Conteúdo HS2:** Experiências são naturalmente únicas por hospital
- **Links cruzados:** Artigos de hospital da mesma cidade DEVEM se referenciar mutuamente ("para emergência ortopédica, veja o Hospital Promed")

### Entre artigo de hospital e artigo de cidade
- **FAQ:** ZERO overlap — cruzar antes de produzir
- **S4 do artigo de cidade:** Artigo de hospital DEVE linkar para a S4 como referência e a S4 DEVE linkar para o artigo de hospital quando existir
- **Endereço/telefone:** Artigo de hospital usa APENAS na HS3 (como chegar), com ângulo de acesso

### Linkagem bidirecional obrigatória
Quando um artigo de hospital é publicado:
1. **Inserir link no artigo de cidade (S4)** → apontando para o artigo de hospital
2. **Inserir link no pillar Rede Própria** → na listagem regional do hospital
3. **Inserir link em artigos de cidade vizinha** (se o hospital atende beneficiários da RM) → ex: Ananindeua linka para Layr Maia
4. **Registrar todos os links neste banco** na tabela "Links que DEVEM APONTAR PARA este artigo"
