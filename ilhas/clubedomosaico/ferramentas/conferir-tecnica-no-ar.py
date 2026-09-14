#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mede a pagina de TECNICA no HTML que o SITE SERVE.

    python3 ferramentas/conferir-tecnica-no-ar.py

O irmao de `teste-tecnicas.php`, do outro lado da distancia que a secao 4 do
ARQUIPELAGO.md paga mais caro: aquele mede o HTML que a bancada monta, este abre
a URL com curl e afirma sobre o que o leitor recebe.

DUAS COISAS QUE ESTE ARQUIVO FAZ E QUE A BANCADA NAO PODE FAZER:

  1. COMPARA O ENDERECO CANONICO COM O MESMO ENDERECO COM QUEBRA DE CACHE, sobre
     os marcadores que ESTE bloco publica. E a regra que a Robometria escreveu em
     14/09/2026 depois de o `/status` afirmar por horas que estava tudo no ar
     enquanto o canonico servia a copia anterior — sem botao de compra e com uma
     frase que o contrato tinha acabado de proibir. Sync aplicado e /status
     batendo NAO sao entrega.
     A comparacao e de MARCADOR, nunca de bytes: a chave de quebra aparece no
     canonical e nos links internos, entao comparar o arquivo inteiro daria falso
     alarme todas as vezes.

  2. RECONTA A GRADE CONTRA O BANCO COMMITADO. As 45 celulas servidas sao
     comparadas com `dados/cobertura.json`, que e a regua em Python. Sem isto,
     "verificado no ar" quereria dizer so que o site existe — que e a cicatriz da
     mesma secao 4: uma verificacao de 167 afirmacoes verdadeiras aprovando, item
     por item, a pagina de horas antes, porque nenhuma delas encostava no que o
     bloco tinha mudado.

`Accept-Encoding: identity` em toda requisicao, tambem pela secao 4: sem
cabecalho de compressao o cache pode servir uma variante de dias atras.
"""

import io
import json
import os
import re
import subprocess
import sys
import time

BASE = "https://clubedomosaico.com.br"
# O ENDERECO ESTA LITERAL AQUI, copiado a mao. Ler CDM_TECNICAS_SLUG do snippet
# seria conferir a pagina com a propria pagina: o dia em que alguem trocar o slug
# sem querer, as duas metades errariam juntas e este arquivo mediria o endereco
# novo achando que mediu o combinado.
CAMINHO = "/como-fazer/o-que-e-mosaico-picassiete/"
TESSELA = "caco_louca"

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

falhas = 0
feitos = 0


def ok(cond, rotulo, medida=""):
    global falhas, feitos
    feitos += 1
    print(("  ok   " if cond else "  FALHA ") + rotulo.ljust(64) + " " + str(medida))
    if not cond:
        falhas += 1


def buscar(url, quebra=None):
    sep = "&" if "?" in url else "?"
    alvo = url + sep + "v=" + str(int(time.time()))
    if quebra:
        alvo += "&cdm_quebra_de_cache=" + quebra
    r = subprocess.run(["curl", "-s", "--max-time", "40", "-H", "Accept-Encoding: identity",
                        "-w", "\n%{http_code}", alvo], capture_output=True, text=True)
    partes = r.stdout.rsplit("\n", 1)
    return partes[0], (partes[1] if len(partes) > 1 else "000")


def corpo(html):
    m = re.search(r"<main\b[^>]*>(.*?)</main>", html, re.S)
    return m.group(1) if m else html


def texto(html):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html))


def carregar(nome):
    with io.open(os.path.join(RAIZ, "dados", nome), encoding="utf-8") as fh:
        return json.load(fh)


print("NO AR — a pagina de tecnica do Clube do Mosaico\n")

html, codigo = buscar(BASE + CAMINHO)
ok("200" == codigo, "a pagina responde 200", codigo)
if "200" != codigo:
    print("\nSem pagina nao ha o que medir.")
    sys.exit(1)

c = corpo(html)
t = texto(c)

# ---------------------------------------------------------------- 1. a grade

print("\n1. A grade servida x o banco commitado")

cobertura = carregar("cobertura.json")
colas = carregar("materiais-colas.json")
tecnicas = carregar("tecnicas.json")

celulas = [e for e in cobertura["estados"]["cola"] if e["tessela"] == TESSELA]
ok(len(celulas) == 45, "o banco tem as 45 combinacoes desta tessela", len(celulas))

sem_nenhuma = sum(1 for e in celulas if e["quantos_elegiveis"] == 0)
com_minimo = sum(1 for e in celulas if e["quantos_elegiveis"] >= 3)
uniao = sorted({i for e in celulas for i in e["elegiveis"]})

ok(c.count("nenhum que o fabricante sustente") == sem_nenhuma,
   "a tabela servida escreve 'nao ha' nas celulas vazias do banco",
   "%d na tela, %d no banco" % (c.count("nenhum que o fabricante sustente"), sem_nenhuma))
ok(("Das %d combinações" % len(celulas)) in t,
   "a frase de resposta traz o numero de combinacoes do banco", len(celulas))
ok(("%d não têm nenhuma" % sem_nenhuma) in t,
   "e quantas ficam sem resposta", sem_nenhuma)
ok(("%d têm três ou mais" % com_minimo) in t,
   "e quantas chegam a tres opcoes", com_minimo)

linhas = len(re.findall(r"<tr\b", c))
ok(linhas >= 10, "a tabela pre-renderizada esta no HTML servido, sem JavaScript",
   "%d linhas" % linhas)

# ------------------------------------------------- 2. a prestacao de contas

print("\n2. A prestacao de contas da secao 7")

por_id = {m["id"]: m for m in colas["materiais"]}
nao_nomeados = []
for ident, m in por_id.items():
    if m["nome_comercial"] not in t:
        nao_nomeados.append(ident)
ok(not nao_nomeados, "cada cola do banco e nomeada na pagina servida",
   "%d de %d" % (len(por_id) - len(nao_nomeados), len(por_id)))

cartoes = re.findall(r'<li class="cdm-f2-cartao[^"]*">(.*?)</li>', c, re.S)
na_vitrine = []
for cartao in cartoes:
    m = re.search(r"<h3>(.*?)</h3>", cartao, re.S)
    if not m:
        continue
    nome = m.group(1).strip()
    for ident, prod in por_id.items():
        if prod["nome_comercial"] == nome:
            na_vitrine.append(ident)
ok(sorted(na_vitrine) == uniao,
   "a vitrine serve exatamente as colas elegiveis do banco",
   "%d cartoes" % len(na_vitrine))

fora = sorted(set(por_id) - set(uniao))
nomeados_fora = [i for i in fora
                 if ("<strong>" + por_id[i]["nome_comercial"]) in c
                 or ("<strong>" + (por_id[i].get("marca", "") + " " + por_id[i]["nome_comercial"]).strip()) in c]
ok(sorted(nomeados_fora) == fora,
   "quem nao entra e nomeado numa linha propria", "%d de %d" % (len(nomeados_fora), len(fora)))
ok(len(uniao) + len(fora) == len(por_id),
   "a soma dos nomeados fecha com o tamanho do banco",
   "%d + %d = %d" % (len(uniao), len(fora), len(por_id)))

ok("link de loja em breve" not in t.lower(),
   "a frase proibida pela secao 7 nao aparece")
sem_saida = [cartao for cartao in cartoes if "cdm-f2-compra" not in cartao or "cdm-f2-botao" not in cartao]
ok(not sem_saida, "nenhum cartao servido fica sem saida de compra",
   "%d cartoes com botao" % (len(cartoes) - len(sem_saida)))

cruas = re.findall(r'<a [^>]*cdm-f2-botao-busca-crua[^>]*>', c)
ok(all("nofollow" in a and "sponsored" not in a for a in cruas),
   "a busca crua servida sai nofollow e nunca sponsored", "%d links" % len(cruas))

# --------------------------------------------------- 3. a malha e o schema

print("\n3. A malha e o schema")

ld = re.search(r'<script type="application/ld\+json" id="cdm-tecnicas-jsonld">(.*?)</script>', html, re.S)
grafo = None
if ld:
    try:
        grafo = json.loads(ld.group(1))
    except ValueError:
        grafo = None
ok(grafo is not None, "o JSON-LD servido parseia")
tipos = [n.get("@type") for n in (grafo or {}).get("@graph", [])]
ok("Article" in tipos and "FAQPage" in tipos, "o grafo servido publica Article e FAQPage",
   ", ".join(t for t in tipos if t))
ok("BreadcrumbList" in html, "a pagina servida publica BreadcrumbList (16.3)")

links = 0
for pagina in ("/como-fazer/", "/"):
    h, cod = buscar(BASE + pagina)
    achou = CAMINHO in h
    ok(cod == "200" and achou, "[%s] publica o link para a pagina de tecnica" % pagina, cod)
    if achou:
        links += 1
ok(links >= 2, "a pagina recebe 2 ou mais links internos (16.4f: nenhuma orfa)", links)

mapa, cod = buscar(BASE + "/wp-sitemap-posts-page-1.xml")
ok(CAMINHO in mapa, "a pagina esta no sitemap", cod)

# ------------------------------------- 4. o cache do hospedeiro (secao 4)

print("\n4. O leitor recebe o que o bloco publicou (cache do hospedeiro)")

quebra = str(int(time.time()))
novo, cod2 = buscar(BASE + CAMINHO, quebra=quebra)
ok(cod2 == "200", "a mesma URL com quebra de cache responde 200", cod2)

# OS MARCADORES SAO OS DESTE BLOCO, nunca o arquivo inteiro: a chave de quebra
# aparece no canonical e nos links internos, e comparar bytes daria falso alarme
# em toda execucao.
MARCADORES = ("cdm-tec-tabela", "cdm-tecnicas-jsonld", "nenhum que o fabricante sustente",
              "O que é mosaico Picassiete", "cdm-f2-cartao")
divergem = [m for m in MARCADORES if c.count(m) != corpo(novo).count(m)]
ok(not divergem,
   "o endereco canonico serve o MESMO que a versao sem cache, nos marcadores deste bloco",
   "iguais em %d marcadores" % len(MARCADORES) if not divergem else "divergem: " + ", ".join(divergem))

print("")
if falhas:
    print("REPROVADO: %d falha(s) em %d afirmacoes." % (falhas, feitos))
    sys.exit(1)
print("APROVADO: %d afirmacoes, nenhuma falha." % feitos)
