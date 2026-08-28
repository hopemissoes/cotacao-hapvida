# -*- coding: utf-8 -*-
"""Gera schema-plano-de-saude-barato.html conforme references/schema-jsonld.md.

PASSO 0 — TIPO: editorial-comercial (equivalente ao TIPO A), nao landing pura:
  ha corpo de guia de 5.414 palavras, 18 FAQs e autor. Tem tabela de preco e
  formulario, entao entra tambem o no Service secundario SEM offers/price.
  Como o pillar cobre varias pracas, o WebPage usa 'mentions' (padrao do Bloco B).
Formato: UM bloco <script type="application/ld+json"> com @context + @graph
  (metodo V4.6.0 — a orientacao de nos soltos foi revogada).
Nao gera Organization nem WebSite: sao globais no RankMath, so referencia por @id.
"""
import io, re, html, json

URL='https://tabelaplanos.com.br/plano-de-saude-barato/'
ART='artigos/plano-de-saude-barato_FINAL.html'
s=io.open(ART,encoding='utf-8').read()
corpo=re.sub(r'<(script|style)>.*?</\1>','',s,flags=re.S)
wc=len(html.unescape(re.sub(r'<[^>]+>',' ',corpo)).split())

# --- FAQ: extraidas do visivel, texto identico
faqs=[]
for d in re.finditer(r'<details\b.*?</details>',corpo,re.S):
    b=d.group(0)
    q=re.search(r'<summary[^>]*>(.*?)</summary>',b,re.S)
    if not q: continue
    perg=html.unescape(re.sub(r'<[^>]+>','',q.group(1))).strip()
    perg=re.sub(r'^\d+\.\s*','',re.sub(r'\s*\+\s*$','',perg)).strip()
    resp=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',b[q.end():]))).strip()
    faqs.append({"@type":"Question","name":perg,
                 "acceptedAnswer":{"@type":"Answer","text":resp}})
assert len(faqs)>=3, len(faqs)

MENTIONS=["https://tabelaplanos.com.br/plano-de-saude-bh/",
 "https://tabelaplanos.com.br/plano-hapvida-rio-de-janeiro/",
 "https://tabelaplanos.com.br/plano-de-saude-em-recife/",
 "https://tabelaplanos.com.br/notrelife-sp-rj/",
 "https://tabelaplanos.com.br/hapvida-cidades/"]

grafo=[
{"@type":"WebPage","@id":URL+"#webpage",
 "name":"Plano de Saúde Barato 2026: CPF ou CNPJ, Qual Custa Menos",
 "description":"Quanto custa o plano de saúde mais barato em 2026: cotamos as duas portas, individual (CPF) e empresarial (MEI/CNPJ), em Fortaleza e Recife. Veja qual sai na frente na sua idade.",
 "url":URL,"inLanguage":"pt-BR",
 "datePublished":"2026-01-14","dateModified":"2026-08-28",
 "specialty":{"@type":"Specialty","name":"Health"},
 "isPartOf":{"@type":"WebSite","@id":"https://tabelaplanos.com.br/#website"},
 "primaryImageOfPage":{"@id":URL+"#primaryimage"},
 "image":{"@type":"ImageObject","@id":URL+"#primaryimage",
          "url":"https://tabelaplanos.com.br/wp-content/uploads/2026/08/Plano-de-Saude-Barato-2026-CPF-ou-CNPJ.png","width":1200,"height":630},
 "mainEntity":{"@id":URL+"#article"},
 "about":{"@id":URL+"#service"},
 "mentions":[{"@type":"WebPage","@id":u+"#webpage"} for u in MENTIONS]},

{"@type":"Article","@id":URL+"#article",
 "headline":"Plano de Saúde Barato: Quanto Custa o Piso do Mercado em 2026",
 "description":"Quanto custa o plano de saúde mais barato em 2026: cotamos as duas portas, individual (CPF) e empresarial (MEI/CNPJ), em Fortaleza e Recife. Veja qual sai na frente na sua idade.",
 "image":{"@type":"ImageObject","url":"https://tabelaplanos.com.br/wp-content/uploads/2026/08/Plano-de-Saude-Barato-2026-CPF-ou-CNPJ.png","width":1200,"height":630},
 "author":{"@id":"https://tabelaplanos.com.br/#jessica-mendes"},
 "publisher":{"@id":"https://tabelaplanos.com.br/#organization"},
 "datePublished":"2026-01-14","dateModified":"2026-08-28",
 "mainEntityOfPage":{"@type":"WebPage","@id":URL},
 "articleSection":"Planos de Saúde","wordCount":wc,"inLanguage":"pt-BR"},

{"@type":"Service","@id":URL+"#service",
 "additionalType":"https://schema.org/HealthInsurancePlan",
 "name":"Plano de saúde de entrada — individual e empresarial",
 "description":"Plano de entrada com cobertura do Rol obrigatório da ANS, em segmentação ambulatorial com coparticipação total, contratável por pessoa física (CPF) onde o individual é comercializado ou por CNPJ, inclusive MEI. Coparticipação por consulta eletiva em [demais_capitais_consultas_eletivas] e por exame simples em [demais_capitais_exames_simples] nas capitais fora de São Paulo e Belo Horizonte; internação, cirurgia e UTI são isentas de coparticipação.",
 "serviceType":"Health Insurance",
 "provider":{"@type":"Organization","@id":"https://www.hapvida.com.br/#organization",
   "name":"Hapvida Assistência Médica",
   "identifier":{"@type":"PropertyValue","name":"Registro ANS","value":"359017"}},
 "broker":{"@type":"InsuranceAgency","@id":"https://tabelaplanos.com.br/#organization"},
 "areaServed":{"@type":"Country","name":"Brasil"}},

{"@type":"BreadcrumbList","@id":URL+"#breadcrumb","itemListElement":[
 {"@type":"ListItem","position":1,"name":"Home","item":"https://tabelaplanos.com.br/"},
 {"@type":"ListItem","position":2,"name":"Plano de Saúde Barato","item":URL}]},

{"@type":"FAQPage","@id":URL+"#faq","mainEntity":faqs},

{"@type":"Person","@id":"https://tabelaplanos.com.br/#jessica-mendes",
 "name":"Jessica Mendes","alternateName":"Jéssica Mendes",
 "jobTitle":"Consultora Especialista em Planos de Saúde",
 "description":"Consultora especializada em planos de saúde desde 2020, com foco em soluções Hapvida para pessoas físicas e famílias. Possui 10 premiações como Consultora Estrela pela operadora Hapvida e uma carteira ativa de mais de 7.000 clientes atendidos.",
 "url":"https://tabelaplanos.com.br/sobre_nos/jessica_mendes/",
 "image":{"@type":"ImageObject","url":"https://tabelaplanos.com.br/imagens/jessica-mendes.jpg","width":400,"height":400},
 "sameAs":["https://www.instagram.com/consultorajessicamendes/"],
 "worksFor":{"@id":"https://tabelaplanos.com.br/#organization"},
 "knowsAbout":["Planos de Saúde Hapvida","Consultoria em Seguros de Saúde","Planos Individuais e Familiares","Portabilidade de Planos de Saúde"],
 "award":["Consultora Estrela Hapvida (10x)"],
 "hasOccupation":{"@type":"Occupation","name":"Consultora de Seguros de Saúde","experienceRequirements":"5 anos de experiência"}},
]

doc={"@context":"https://schema.org","@graph":grafo}
saida='<script type="application/ld+json">'+json.dumps(doc,ensure_ascii=False,indent=2)+'</script>'
io.open('artigos/schema-plano-de-saude-barato.html','w',encoding='utf-8').write(saida)

# --- travas do checklist final
tipos=[n["@type"] for n in grafo]
assert len(tipos)==len(set(tipos)), f"@type duplicado: {tipos}"
assert not any(t in ("Organization","WebSite") for t in tipos), "nao gerar Organization/WebSite"
for proibido in ("offers","AggregateOffer","hasOfferCatalog","price","lowPrice","highPrice"):
    assert proibido not in json.dumps(grafo[2]), f"Service com {proibido}"
assert not re.search(r'R\$\s?\d', json.dumps(doc,ensure_ascii=False)), "valor em reais fixo no schema"
bc=[i["position"] for i in grafo[3]["itemListElement"]]
assert bc==list(range(1,len(bc)+1)), "positions nao sequenciais"
assert all(i["item"].endswith("/") for i in grafo[3]["itemListElement"]), "URL sem / final"
assert len(grafo[1]["headline"])<=110, len(grafo[1]["headline"])
json.loads(saida[len('<script type="application/ld+json">'):-len('</script>')])
print(f"OK — {len(grafo)} nos | {len(faqs)} FAQs | wordCount {wc} | {len(saida)} chars")
print("tipos:", ", ".join(tipos))
