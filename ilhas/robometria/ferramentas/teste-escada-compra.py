#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A escada de compra da secao 25, medida com REGUA PROPRIA.

    python3 ferramentas/teste-escada-compra.py

Sai com codigo 1 na primeira reprovacao contada.

POR QUE ELE EXISTE, SE JA HA validar-banco.py
---------------------------------------------
O validador cobra o CONTRATO DO ESQUEMA: a forma do campo, a coerencia entre
degrau e ficha, as contagens do cabecalho. Este arquivo cobra outra coisa — o que
a secao 25 do ARQUIPELAGO.md DECIDIU, que e anterior ao esquema e nao muda quando
alguem edita o esquema. Se as duas travas lessem a mesma fonte, editar o esquema
apagaria as duas de uma vez, e o portao ficaria verde sobre a decisao revogada em
silencio. E a terceira conta que a secao 8 exige quando duas metades contam a mesma
coisa.

AS TRES CICATRIZES DO ARQUIPELAGO QUE ESTE ARQUIVO CARREGA
-----------------------------------------------------------
1. QUEM CONFERE ESCREVE A PROPRIA REGUA. Os tokens de marca e as chaves-ancora
   abaixo estao escritos AQUI, a mao, e este arquivo NAO importa
   gerar-busca-de-produto.py nem validar-banco.py. Se importasse, trocar a
   composicao faria as duas metades errarem juntas — foi assim que a frase da R1
   atribuiu ao fabricante uma classificacao que era da ilha, com o PHP e a
   referencia dizendo a MESMA coisa errada e todo portao verde.

2. LISTA DENTRO DA REGUA ENVELHECE CALADA — entao a regua declara o UNIVERSO que
   conhece e reprova quando ele cresce. Marca nova em marcas.json ou entidade nova
   no esquema fazem este arquivo FALHAR, em vez de passar por cima delas. E a outra
   metade da cicatriz de 13/09/2026: a lista de tipos saiu de dentro da regua da
   funcao porque tipo novo entraria sem trava nenhuma com o banco verde. Aqui a
   lista de VALORES ESPERADOS fica a mao (senao nao ha regua) e a lista de QUEM
   EXISTE vem do banco (senao ha buraco).

3. A GRADE TEM QUE PISAR NA BORDA. As ancoras nao sao uma amostra bonita: sao a
   marca cujo `nome` de tela tem parenteses, a marca cujo id e palavra comum do
   portugues, o modelo cujo codigo sozinho e um celular de outra marca, a peca sem
   codigo_fabricante, a peca cujo fabricante batiza pela POSICAO e nao pela funcao,
   e um registro NAO publicavel, que tem de sair vazio.
"""
import json
import os
import sys
from urllib.parse import unquote, urlparse, parse_qs

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

falhas = []
contadas = 0


def ok(condicao, mensagem):
    global contadas
    contadas += 1
    if not condicao:
        falhas.append(mensagem)


def carregar(rel):
    with open(os.path.join(RAIZ, rel), encoding="utf-8") as fh:
        return json.load(fh)


# --------------------------------------------------------------- A REGUA, A MAO
# O que a secao 25.1 decidiu, escrito aqui e nao lido do esquema.
DEGRAUS_DA_25_1 = {
    1: "loja-oficial-shopee",
    2: "catalogo-mercadolivre",
    3: "anuncio-vendedor-shopee",
    4: "busca",
}

# O token de marca que a busca tem de carregar. Escrito a mao: se o marcas.json
# passar a dizer outra coisa, e ESTA lista que decide quem esta errado.
TOKEN_DA_MARCA = {
    "multi": "Multilaser",
    "electrolux": "Electrolux",
    "xiaomi": "Xiaomi",
    "positivo": "Positivo",
    "wap": "WAP",
}

ENTIDADES = {"modelos-robo.json": "modelo_robo", "pecas.json": "peca"}
CONTEXTO = "robo aspirador"
BASE = "https://shopee.com.br/search?keyword="

# As ancoras, chave por chave. Cada uma esta aqui por um motivo escrito.
ANCORAS = {
    # marca cujo `nome` de tela e "Multi (ex-Multilaser)": a chave NAO pode levar
    # parenteses, e o id "multi" sozinho e prefixo do portugues.
    "multi-ho041": "Multilaser HO041 robo aspirador",
    # o codigo sozinho e um celular de outra marca. E a armadilha da 25.3 na forma
    # que so esta ilha tem, e o contexto e o que a desarma.
    "xiaomi-s20": "Xiaomi S20 robo aspirador",
    # sigla que em ingles e outra coisa; so sobrevive com o contexto do lado.
    "wap-w300": "WAP W300 robo aspirador",
    # marca cujo id e palavra comum e cujo nome de tela gasta tres tokens.
    "positivo-pra800": "Positivo PRA800 robo aspirador",
    "electrolux-erb60": "Electrolux ERB60 robo aspirador",
    # PECA QUE MUDOU DE CHAVE EM 16/09/2026, E ELA E A BORDA MAIS CARA DESTA
    # LISTA. Ate hoje a ancora era "WAP escova lateral robo aspirador", com o
    # comentario *"quem busca digita a funcao, nao a posicao"* — e a frase estava
    # ERRADA, escrita sem medicao porque nao havia como medir. A ronda de 16/09
    # abriu essa busca no navegador e ela devolveu ZERO resultado; a Open API da
    # 25.6 confirmou que quem devolve e a POSICAO, o batismo da WAP. A ilha
    # continua classificando pela funcao no banco e na tela (secao 26); o que
    # mudou e a palavra que vai a loja, e so ela.
    "wap-escova-direita-w300": "WAP Escova Direita robo aspirador",
    # peca com codigo_fabricante null: a chave sai igual, porque o codigo nunca
    # entrou nela.
    "electrolux-filtro-hepa-espuma-erb44-erb60-erb61-erb62":
        "Electrolux filtro robo aspirador",
    "xiaomi-b112-tb": "Xiaomi mop robo aspirador",
    "multi-pr10127": "Multilaser bateria robo aspirador",
    "electrolux-kpcel01": "Electrolux kit robo aspirador",
}


def chave_legivel(url):
    """A palavra-chave como uma pessoa a digitaria, tirada da URL pelo parametro —
    nunca por corte de string. Cortar pelo tamanho da base e a mesma familia de
    erro que contar `&#038;` na pagina inteira: mede o lugar errado e passa."""
    q = parse_qs(urlparse(url).query)
    return unquote(q.get("keyword", [""])[0])


esquema = carregar("dados/esquema-banco.json")
marcas = carregar("dados/marcas.json")
bancos = {rel: carregar("dados/" + rel) for rel in ENTIDADES}

escada = esquema["tipos_compostos"]["afiliado"].get("escada_de_compra") or {}

# A MEDICAO DE PALAVRA-CHAVE (16/09/2026). Este arquivo continua sem importar o
# gerador e sem importar o validador — le o ARQUIVO DE DADOS, que e o resultado
# publicado da medicao, do mesmo jeito que le o banco. Arquivo ausente nao e
# erro: a regra antiga volta a valer inteira para todo mundo, que e o
# comportamento certo quando ninguem mediu nada.
try:
    _medicao = carregar("dados/palavras-chave-medidas.json")
except FileNotFoundError:
    _medicao = {"registros": [], "gerado_em": None}
MEDIDO_EM = _medicao.get("gerado_em")
MEDIDAS = {r["id"]: (r.get("escolhido") or {}) for r in _medicao.get("registros", [])}

# ------------------------------------------- 1. O UNIVERSO NAO CRESCEU AS ESCURAS
ok(set(TOKEN_DA_MARCA) == {m["id"] for m in marcas["registros"]},
   "a regua conhece as marcas %s e marcas.json tem %s. Marca nova entra com token de "
   "busca conferido a mao, ou nao entra"
   % (sorted(TOKEN_DA_MARCA), sorted(m["id"] for m in marcas["registros"])))

ok(set(ENTIDADES.values()) == set(escada.get("termo_de_contexto_por_entidade") or {}),
   "a regua conhece as entidades %s e o esquema declara termo para %s"
   % (sorted(set(ENTIDADES.values())),
      sorted(escada.get("termo_de_contexto_por_entidade") or {})))

# ---------------------------------------------------- 2. A ESCADA E A DA SECAO 25
declarados = {d.get("degrau"): d.get("nome") for d in escada.get("degraus", [])}
ok(declarados == DEGRAUS_DA_25_1,
   "os degraus do esquema sao %r e a secao 25.1 tem %r" % (declarados, DEGRAUS_DA_25_1))
ok(escada.get("base_da_busca") == BASE,
   "base_da_busca e %r e a 25.1 usa %r" % (escada.get("base_da_busca"), BASE))
for ent in set(ENTIDADES.values()):
    ok((escada.get("termo_de_contexto_por_entidade") or {}).get(ent) == CONTEXTO,
       "termo de contexto de %r e %r e a regua espera %r"
       % (ent, (escada.get("termo_de_contexto_por_entidade") or {}).get(ent), CONTEXTO))

# ------------------------------------------------- 3. AS ANCORAS, CHAVE POR CHAVE
por_id = {}
for rel, doc in bancos.items():
    for r in doc["registros"]:
        por_id[r["id"]] = (rel, r)

for ident, esperada in ANCORAS.items():
    if ident not in por_id:
        ok(False, "ancora %r sumiu do banco. Ancora que some leva a trava junto: "
                  "escolha outra borda e escreva por que ela e borda" % ident)
        continue
    _rel, reg = por_id[ident]
    ok(chave_legivel(reg["afiliado"]["url_busca_produto"]) == esperada,
       "%s: a busca e %r e a regua escreveu %r"
       % (ident, chave_legivel(reg["afiliado"]["url_busca_produto"]), esperada))

# -------------------------------- 4. A VARREDURA INTEIRA, NAO O CASO-ANCORA
# "O corpo" de uma regra e o corpo de TODOS os registros. Amostra com nome de
# varredura e o mesmo defeito da grade que nao pisa na borda.
publicaveis = chaves = 0
distintas = set()
for rel, doc in bancos.items():
    entidade = ENTIDADES[rel]
    for reg in doc["registros"]:
        onde = "%s/%s" % (rel, reg["id"])
        a = reg.get("afiliado") or {}
        busca = a.get("url_busca_produto") or ""

        if reg["status"] != "publicavel":
            ok(busca == "",
               "%s: registro %r com busca escrita. O portao da categoria ja recusou "
               "este aparelho, e a chave diria 'robo aspirador' sobre ele"
               % (onde, reg["status"]))
            continue

        publicaveis += 1
        ok(busca.startswith(BASE), "%s: a busca nao sai da base da 25.1" % onde)
        chave = chave_legivel(busca)
        distintas.add(chave)
        if not chave:
            ok(False, "%s: publicavel sem palavra-chave. A 25.2 chama isto de defeito "
                      "da 19.1, em qualquer degrau" % onde)
            continue
        chaves += 1

        token = TOKEN_DA_MARCA.get(reg["marca"], "")
        ok(token and chave.startswith(token + " "),
           "%s: a busca %r nao ABRE pelo token da marca %r. A marca e o filtro mais "
           "forte e vem primeiro, como digita quem compra" % (onde, chave, token))
        ok(chave.endswith(" " + CONTEXTO),
           "%s: a busca %r nao termina no termo de contexto %r. Sem ele, 'S20' e um "
           "celular e 'Positivo' e um adjetivo (25.3)" % (onde, chave, CONTEXTO))
        ok(len(chave.split()) >= 3,
           "%s: a busca %r tem menos de tres palavras, entao nao tem o que distingue "
           "este item dos irmaos da mesma marca" % (onde, chave))
        ok("(" not in chave and ")" not in chave,
           "%s: a busca %r leva parentese. E o `nome` de tela vazando para dentro da "
           "consulta — 'Multi (ex-Multilaser)' e o caso que criou o nome_de_busca"
           % (onde, chave))

        # A ASSIMETRIA ENTRE AS DUAS ENTIDADES E DECISAO, ENTAO E MEDIDA. Sem estas
        # duas, alguem inverte a composicao um dia e nada reprova.
        codigo = (reg.get("codigo_fabricante") or "").strip()
        if entidade == "modelo_robo":
            ok(codigo and (" %s " % codigo) in (" %s " % chave),
               "%s: modelo sem o codigo %r dentro da busca %r. O codigo do modelo E o "
               "nome comercial: ninguem vende 'Electrolux robo aspirador'"
               % (onde, codigo, chave))
        else:
            # ESTA TRAVA MUDOU EM 16/09/2026, E O AVISO QUE ELA CARREGAVA E QUEM
            # MANDOU MUDA-LA: *"Se isto mudar de proposito, mude tambem esta trava
            # e escreva a medicao que sustenta a mudanca."* A medicao existe e mora
            # em `dados/palavras-chave-medidas.json`.
            #
            # Ate hoje a lei era "a chave de peca leva o TIPO e nunca o codigo",
            # escrita sem medicao porque a busca do site nao era mensuravel da
            # nuvem. A Open API da 25.6 mediu, e ela derrubou as duas metades: o
            # TIPO e vocabulario da ILHA (secao 26) e devolve zero em tres marcas,
            # e o CODIGO DA PECA, que a trava jurava que ninguem digita, devolve
            # resultado em loja de reposicao.
            #
            # A lei nova e mais dura, nao mais frouxa. Chave que foge da
            # composicao de sempre so passa se for EXATAMENTE a que a medicao
            # escolheu e se a medicao tiver registrado resultado para ela. Chave
            # sem medicao continua obrigada ao tipo e proibida de levar o codigo —
            # ou seja, ninguem mais estreita uma chave "no olho".
            tipo = (reg.get("tipo") or "").strip()
            medida = MEDIDAS.get(reg["id"]) or {}
            if medida.get("chave") == chave:
                ok((medida.get("resultados") or 0) > 0,
                   "%s: a busca %r e a chave MEDIDA, e a medicao de %s registrou "
                   "%r resultado(s). Chave medida em zero e beco sem saida com "
                   "procedencia — pior que chave nao medida, porque parece conferida"
                   % (onde, chave, MEDIDO_EM, medida.get("resultados")))
            else:
                ok(tipo and tipo in chave,
                   "%s: peca sem o tipo %r dentro da busca %r, e esta chave NAO e a "
                   "que a medicao de %s escolheu (%r). Chave estreitada fora da "
                   "medicao e palpite com cara de dado"
                   % (onde, tipo, chave, MEDIDO_EM, medida.get("chave")))
                ok(not codigo or codigo.lower() not in chave.lower(),
                   "%s: a busca %r carrega o codigo de peca %r sem medicao que o "
                   "sustente. Com medicao o codigo e legitimo (degrau 3); sem ela e "
                   "o SKU interno de sempre, que o vendedor nao digita"
                   % (onde, chave, codigo))

        # O QUE FALTA SE DECLARA. Piso sem o link encurtado exige motivo escrito.
        if not a.get("url_busca"):
            ok((a.get("motivo_sem_url_busca") or "").strip(),
               "%s: sem o link encurtado da busca e sem motivo. Divida sem motivo "
               "escrito e divida que a proxima execucao nao sabe medir" % onde)

        # O DEGRAU, MEDIDO POR REGUA PROPRIA (14/09/2026, item 2 do despacho do
        # Raphael). O numero 4 esta escrito AQUI a mao, e este arquivo nao le o
        # esquema nem chama o gerador: se lesse, trocar o degrau do piso num lugar
        # so faria as duas metades errarem juntas — a terceira conta que a secao 8
        # exige. A 25.1 diz que a escada para no PRIMEIRO degrau que servir, e quem
        # nao tem ficha parou na busca.
        degrau = a.get("degrau")
        if (a.get("url") or "").strip():
            ok(degrau in (1, 2, 3),
               "%s: tem ficha de produto e degrau %r. Ficha nao para no degrau da "
               "busca" % (onde, degrau))
        else:
            ok(degrau == 4,
               "%s: publicavel sem ficha e degrau %r. A escada parou na busca, que e "
               "o degrau 4 — e degrau null quer dizer 'ninguem decidiu', que era o "
               "estado desta ilha ate 14/09/2026" % (onde, degrau))
        ok((a.get("conferido_em") or "").strip(),
           "%s: degrau sem conferido_em, a data em que ele foi decidido. Decisao sem "
           "data nao da para reconferir" % onde)

        # INTESTAVEL E DERIVADO (item 3 do despacho). A regua reescreve a derivacao
        # a mao, em vez de comparar o campo com ele mesmo.
        sem_url_crua = not (a.get("url_produto") or "").strip()
        deveria = bool((a.get("url") or "").strip() and sem_url_crua)
        ok(a.get("intestavel") is deveria,
           "%s: intestavel diz %r e o item %s. Pela 25.4-b, item com link encurtado e "
           "sem a URL crua do produto NAO da para conferir, e isso tem de ficar "
           "visivel em vez de escondido"
           % (onde, a.get("intestavel"),
              "e intestavel" if deveria else "da para conferir"))

print("Robometria — escada de compra da secao 25")
print("  degraus conferidos ... 4, com os nomes da 25.1")
print("  publicaveis .......... %d, todos com palavra-chave (%d distintas)"
      % (publicaveis, len(distintas)))
print("  ancoras a mao ........ %d" % len(ANCORAS))
print("  afirmacoes ........... %d" % contadas)

if falhas:
    print("\nREPROVADO — %d de %d:" % (len(falhas), contadas))
    for f in falhas:
        print("  x " + f)
    sys.exit(1)

print("\nAPROVADO: %d afirmacoes, 0 falha." % contadas)
