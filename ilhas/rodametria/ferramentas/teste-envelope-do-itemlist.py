# -*- coding: utf-8 -*-
"""PORTAO DO ENVELOPE DO `ItemList` — o que a LISTA declara, fora dos itens dela.

    python3 ferramentas/teste-envelope-do-itemlist.py

POR QUE ELE NASCEU EM 12/11/2026, e a causa e uma LACUNA e nao um defeito no ar.
A passada das 16h18Z desta ilha fechou escrevendo o proximo passo com o numero
na mao: **`ItemList.description` e a `meta name="description"` da mesma pagina
sao IDENTICAS, letra por letra, nas DUAS paginas de vitrine — e NENHUM portao as
amarra.** O `conferir-produto-no-ar.py` desce fundo na `Offer` de dentro de cada
item (url vazia, `availability`, `priceValidUntil`, `priceSpecification.validFrom`
contra a data da coleta) e trata o ENVELOPE — `name`, `description`,
`numberOfItems`, `position`, o `@type` de cada degrau — como uma CONTAGEM:
`len(itens) == len(linhas)`, e nada mais.

E A 20.7 DIZ O QUE ACONTECE COM AS DUAS: *"comecam iguais e so uma sobe"*. Esta
ilha ja pagou essa cicatriz uma vez, em 11/11/2026, com o `og:title`: o valor
estava CERTO e vinha do CAMPO ERRADO (`nome`, o rotulo da trilha da 16.3, no
lugar de `titulo`), e a home desta ilha se chamava "Inicio" no cartao de
compartilhamento por tempo nenhum sabe quanto, debaixo de dez portoes verdes.
O conserto daquele dia foi uma regua que compara `<title>` e `og:title` LETRA
POR LETRA. **A `description` ficou de fora dela**, e e essa a divida que este
arquivo fecha — com a diferenca de que aqui ela e fechada ANTES do defeito, e
nao depois.

O QUE O CODIGO FAZ HOJE, lido nos snippets e nao suposto: a `<meta name=
"description">` e o `og:description` saem de `rodametria_casca_paginas()[$slug]
['description']`, que a pagina de produto registra pelo filtro `rodametria_paginas`
lendo `$pagina['declarado']['description']`; o `ItemList.description` le
`$d['description']`, que e o MESMO campo. **Uma fonte, tres leituras** — e tres
leituras sem regua e exatamente o mundo em que o `og:title` viveu errado.

O QUE E DAQUI E O QUE NAO E. Daqui: o ENVELOPE. De `conferir-produto-no-ar.py`
secao (5): a `Offer` DENTRO do item. A fronteira esta escrita para nao nascerem
duas copias da mesma regua, que e o que a 20.7 proibe aqui.

E UMA COISA QUE A REGUA NAO FAZ, de proposito: ela NAO compara `numberOfItems`
com os cartoes do carrossel. Medido no ar as 19h2xZ de 12/11/2026 — a bicicleta
serve **3** cartoes e declara **6** itens; o patinete serve **5** e declara
**15**. O `ItemList` desta ilha e a TABELA (secao 7: todo item nomeado uma vez),
nao o carrossel, que tem teto pela 32.1. Regua que confundisse os dois
reprovaria as duas paginas certas no primeiro dia.

ESTE ARQUIVO E O DONO DA REGUA. Ele fabrica os mundos que o dado de hoje nao tem
(`main()`), `conferir-produto-no-ar.py` a aplica as paginas de vitrine COM as
linhas da fonte, e `conferir-no-ar.py` a aplica a TODA URL do `wp-sitemap.xml`,
sem a fonte — porque `ItemList` servido em pagina que ninguem esperava e
justamente o caso que uma lista digitada nao alcanca (32.5-b).
"""
from __future__ import unicode_literals

import html as _html
import json
import re
import sys

# ---------------------------------------------------------------------------
# (A) LER AS DECLARACOES DAS TRES CAMADAS DO HTML SERVIDO
#
# Tudo o que sai de atributo vem pelo `esc_attr` do WordPress, entao um
# apostrofo chega como `&#039;` e um `&` como `&#038;`. Desfazer as entidades
# ANTES de comparar e o que faz a comparacao ser a do leitor e nao a do
# escapador — a mesma licao que o teto de 160 caracteres da `description` ja
# tinha aprendido em `conferir-no-ar.py`.
# ---------------------------------------------------------------------------

_RE_META_DESC = re.compile(r'<meta name="description" content="([^"]*)"')
_RE_OG_DESC = re.compile(r'<meta property="og:description" content="([^"]*)"')
_RE_H1 = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S | re.I)
_RE_LD = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)


def _texto(s):
    """Sem marcacao, sem entidade e sem espaco dobrado — os DOIS lados passam
    por aqui, nunca um so: regua que normaliza metade reprova a pagina certa."""
    s = re.sub(r"<[^>]+>", " ", s or "")
    return re.sub(r"\s+", " ", _html.unescape(s)).strip()


def declaracoes_da_pagina(html):
    """As tres declaracoes de TELA que o envelope repete. Funcao pura."""
    md = _RE_META_DESC.search(html or "")
    og = _RE_OG_DESC.search(html or "")
    h1 = _RE_H1.findall(html or "")
    return {
        "description": _texto(md.group(1)) if md else None,
        "og_description": _texto(og.group(1)) if og else None,
        "h1": _texto(h1[0]) if len(h1) == 1 else None,
        "quantos_h1": len(h1),
    }


def itemlists_do_html(html):
    """Todo `ItemList` servido, inclusive dentro de `@graph` ou de um array.

    Devolve [(ordem, dict)]. JSON-LD que nao parseia NAO e problema deste
    arquivo: `conferir-no-ar.py` ja tem a afirmacao de validade, e duplica-la
    aqui seria a segunda declaracao do mesmo fato.
    """
    achados = []
    for i, bloco in enumerate(_RE_LD.findall(html or "")):
        try:
            dado = json.loads(bloco)
        except Exception:  # noqa: BLE001 — a validade e de outro portao
            continue
        pilha = dado if isinstance(dado, list) else [dado]
        while pilha:
            no = pilha.pop(0)
            if not isinstance(no, dict):
                continue
            if isinstance(no.get("@graph"), list):
                pilha = list(no["@graph"]) + pilha
            if no.get("@type") == "ItemList":
                achados.append((i, no))
    return achados


# ---------------------------------------------------------------------------
# (B) A REGUA
# ---------------------------------------------------------------------------

def problemas_do_envelope(caminho, lista, tela, linhas=None):
    """Os problemas do ENVELOPE de UM `ItemList`. Funcao pura.

    `tela` e o dicionario de `declaracoes_da_pagina`. `linhas` e a vitrine do
    repositorio daquela pagina, quando quem chama a tem — e so com ela se pode
    afirmar o PAREAMENTO POR POSICAO de que a secao (5) de
    `conferir-produto-no-ar.py` ja depende sem nunca o ter provado.
    """
    maus = []

    def mal(msg):
        maus.append("%s: %s" % (caminho, msg))

    nome = (lista.get("name") or "").strip()
    desc = (lista.get("description") or "").strip()
    itens = lista.get("itemListElement")
    n = lista.get("numberOfItems")

    # (1) O NOME DA LISTA E O H1 DA PAGINA, letra por letra.
    #     `name` de uma lista e o nome da LISTA, e nesta ilha a lista e a
    #     resposta da pagina: o H1 e a mesma frase. Nao e o `<title>` — o
    #     `<title>` carrega a promessa de busca ("qual comprar e quanto custa
    #     hoje") e o H1 nomeia a coisa. Comparar com o `<title>` reprovaria as
    #     duas paginas certas; esta distincao esta aqui escrita para a proxima
    #     execucao nao "consertar" o que nao esta quebrado.
    if not nome:
        mal("o ItemList nao declara `name` — chave ausente nao declara nada (25.9)")
    elif tela.get("h1") is None:
        if tela.get("quantos_h1") != 1:
            mal("a pagina serve %d <h1> e o `name` do ItemList nao tem com quem "
                "ser comparado" % tela.get("quantos_h1"))
    elif nome != tela["h1"]:
        mal("o <h1> serve %r e o ItemList.name serve %r. Duas declaracoes do mesmo "
            "fato comecam iguais e so uma sobe (20.7)" % (tela["h1"][:70], nome[:70]))

    # (2) A `description` DA LISTA E A `meta name=description` DA PAGINA,
    #     letra por letra. E O DEFEITO QUE ESTE ARQUIVO EXISTE PARA IMPEDIR.
    if not desc:
        mal("o ItemList nao declara `description` — e a pagina serve uma meta "
            "description que ele repetiria (25.9)")
    elif tela.get("description") is None:
        mal("o ItemList declara `description` e a pagina NAO serve `meta "
            "name=description`: a camada da maquina diz o que a da tela nao diz")
    elif desc != tela["description"]:
        mal("a meta description serve %r e o ItemList.description serve %r. "
            "Duas declaracoes do mesmo fato comecam iguais e so uma sobe (20.7) — "
            "e esta e a cicatriz que o og:title desta ilha pagou em 11/11"
            % (tela["description"][:70], desc[:70]))

    # (3) E O PAR `og:` ENTRA NA MESMA AMARRA. Ele ja le a mesma fonte no
    #     codigo; o que faltava era alguem conferir que continua lendo.
    if tela.get("description") is not None and tela.get("og_description") is None:
        mal("a pagina serve `meta name=description` e NAO serve `og:description`: "
            "o par og: pela metade e o estado em que o og:title viveu errado")
    elif (tela.get("description") is not None
          and tela.get("og_description") != tela["description"]):
        mal("a meta description serve %r e o og:description serve %r — mesma "
            "fonte no codigo, duas leituras, e so uma subiu (20.7)"
            % (tela["description"][:70], (tela.get("og_description") or "")[:70]))

    # (4) `numberOfItems` E A CONTA DA PROPRIA LISTA, e ela se confere sozinha.
    if not isinstance(itens, list):
        mal("o ItemList nao serve `itemListElement` como lista (serve %s)"
            % type(itens).__name__)
        return maus
    if n is None:
        mal("o ItemList serve %d item(ns) e nao declara `numberOfItems` (25.9)"
            % len(itens))
    else:
        try:
            n_int = int(n)
        except (TypeError, ValueError):
            n_int = None
            mal("o `numberOfItems` do ItemList nao e numero (%r)" % (n,))
        if n_int is not None and n_int != len(itens):
            mal("o ItemList declara numberOfItems %d e serve %d item(ns): a lista "
                "se contradiz sozinha" % (n_int, len(itens)))
    if not itens:
        mal("o ItemList serve ZERO item: lista vazia nao declara nada e ocupa a "
            "camada que a visao geral de IA ingere (32.4-c)")

    # (5) AS POSICOES SAO 1..N, NA ORDEM EM QUE SAO SERVIDAS.
    #     Nao basta serem distintas: o pareamento POR INDICE de que a secao (5)
    #     do portao de ar depende so e legitimo se a posicao i+1 estiver no
    #     indice i.
    posicoes = []
    for i, el in enumerate(itens):
        if not isinstance(el, dict):
            mal("o degrau %d do ItemList nao e objeto" % (i + 1))
            continue
        if el.get("@type") != "ListItem":
            mal("o degrau %d do ItemList e %r e tinha de ser ListItem"
                % (i + 1, el.get("@type")))
        posicoes.append(el.get("position"))
        item = el.get("item")
        if not isinstance(item, dict):
            mal("o degrau %d do ItemList nao carrega `item`" % (i + 1))
            continue
        if item.get("@type") != "Product":
            mal("o item do degrau %d e %r e tinha de ser Product"
                % (i + 1, item.get("@type")))
        if not (item.get("name") or "").strip():
            mal("o item do degrau %d nao tem `name`: anuncio sem nome na camada "
                "da maquina e o que a secao 7 proibe na tela" % (i + 1))

    if posicoes and posicoes != list(range(1, len(posicoes) + 1)):
        mal("as posicoes do ItemList sao %s e tinham de ser 1..%d na ordem "
            "servida — e e o pareamento por indice que a Offer de cada linha usa "
            "para achar a data da coleta dela"
            % (posicoes[:8], len(posicoes)))

    # (6) COM A FONTE NA MAO: o item da posicao i E a linha i da vitrine.
    #     A contagem ja era afirmada; o PAREAMENTO nunca foi. E a diferenca nao
    #     e academica — a bicicleta serve DOIS anuncios com o titulo IDENTICO
    #     (posicoes 4 e 5, medido no ar em 12/11/2026), entao casar por NOME
    #     aprovaria uma lista fora de ordem. So a posicao decide.
    if linhas is not None:
        if len(itens) != len(linhas):
            mal("o ItemList serve %d item(ns) e a vitrine do repositorio tem %d "
                "linha(s)" % (len(itens), len(linhas)))
        for i, (el, linha) in enumerate(zip(itens, linhas)):
            if not isinstance(el, dict):
                continue
            item = el.get("item") or {}
            nome_ld = (item.get("name") or "").strip()
            nome_fonte = str(linha.get("nome") or "").strip()
            if nome_ld != nome_fonte:
                mal("o degrau %d do ItemList nomeia %r e a linha %d da vitrine e "
                    "%r: a lista servida nao esta na ordem da fonte"
                    % (i + 1, nome_ld[:50], i + 1, nome_fonte[:50]))
            img_fonte = str((linha.get("imagem") or {}).get("url") or "").strip()
            img_ld = str(item.get("image") or "").strip()
            if img_fonte and not img_ld:
                mal("o degrau %d tem foto na fonte e nao a declara (25.9)" % (i + 1))
            elif img_fonte and img_ld != img_fonte:
                mal("o degrau %d declara a foto %r e a fonte tem %r"
                    % (i + 1, img_ld[:60], img_fonte[:60]))

    return maus


def problemas_da_foto_na_tela(caminho, lista, html, linhas):
    """A FOTO QUE O LEITOR VE TEM DE SER A QUE A MAQUINA RECEBE — NESTA DIRECAO.

    A PRIMEIRA VERSAO DESTA AFIRMACAO ESTAVA INVERTIDA, E O AR A REPROVOU ANTES
    DE ELA ENTRAR (12/11/2026, 19h3xZ). Ela exigia que TODA foto declarada
    estivesse no HTML servido, e reprovou as DUAS paginas sas: 3 problemas na
    bicicleta e 10 no patinete. O numero explica tudo — a bicicleta declara 6
    fotos e serve 3 na tela; o patinete declara 15 e serve 5. **E exatamente o
    numero de cartoes do carrossel**, que tem TETO pela 32.1, enquanto a tabela
    da secao 7 leva todos os anuncios e nao leva foto nenhuma. A foto do anuncio
    e um fato do PRODUTO, verdadeiro esteja ele no carrossel ou na tabela; nao e
    uma segunda declaracao de algo que a pagina diz. **A regua errada aqui seria
    a pior especie: a que reprova a pagina certa**, e a 20.5 ja escreveu o que
    acontece depois — alguem passa a ignorar o portao.

    O QUE SOBRA, E ELE E A ASSIMETRIA QUE IMPORTA: a foto que o leitor ESTA
    vendo e a maquina NAO declara. A tela e o subconjunto; o que nao se admite e
    o subconjunto ser maior que o declarado.
    """
    maus = []
    corpo = _html.unescape(_RE_LD.sub(" ", html or ""))
    itens = lista.get("itemListElement") or []
    for i, linha in enumerate(linhas or []):
        foto = str((linha.get("imagem") or {}).get("url") or "").strip()
        if not foto or foto not in corpo:
            continue
        item = {}
        if i < len(itens) and isinstance(itens[i], dict):
            item = itens[i].get("item") or {}
        if str(item.get("image") or "").strip() != foto:
            maus.append("%s: a tela serve a foto do anuncio %d (%r) e o ItemList "
                        "nao a declara nesse degrau — o leitor ve o que a maquina "
                        "nao recebe" % (caminho, i + 1, foto[:60]))
    return maus


def fotos_na_tela(lista, html, linhas):
    """Quantas das fotos declaradas o leitor ve, e quantas sao. REGISTRO, nao
    veredito: o carrossel tem teto pela 32.1 e a tabela nao leva foto, entao o
    numero menor e o estado CERTO desta ilha. Ele esta aqui para a proxima
    execucao nao precisar remedir para saber que a diferenca e normal."""
    corpo = _html.unescape(_RE_LD.sub(" ", html or ""))
    declaradas = [str(((e.get("item") or {}) if isinstance(e, dict) else {}).get("image") or "")
                  for e in (lista.get("itemListElement") or [])]
    declaradas = [u for u in declaradas if u]
    return sum(1 for u in declaradas if u in corpo), len(declaradas)


# ---------------------------------------------------------------------------
# (C) OS MUNDOS FABRICADOS
#
# A regua entra verde no dado de hoje — as duas paginas de vitrine passam
# inteiras, medidas no ar as 19h2xZ de 12/11/2026 antes de uma linha deste
# arquivo entrar em portao nenhum. **Regua que so foi medida onde esta verde nao
# foi medida.** Cada afirmacao de cima tem aqui o mundo que a faz morder, e o
# mundo saudavel tem de passar com ZERO problema, senao o que esta escrito e um
# portao que reprova a pagina certa.
# ---------------------------------------------------------------------------

AFIRMACOES = [0]
FALHAS = []


def ok(cond, msg):
    AFIRMACOES[0] += 1
    if not cond:
        FALHAS.append(msg)


DESC = ("As bicicletas elétricas de adulto à venda hoje, com a faixa de preço "
        "medida na loja e o que cada anúncio declara de potência e bateria.")
H1 = "Bicicleta elétrica"
TITULO = "Bicicleta elétrica: qual comprar e quanto custa hoje"
FOTO = "https://cf.shopee.com.br/file/sg-11134201-82582-mrfxhcjpv3eodc"

LINHAS = [
    {"nome": "Bicicleta elétrica dobrável NIUDA para adultos",
     "imagem": {"url": FOTO}},
    # OS DOIS TITULOS IDENTICOS DO AR, posicoes 4 e 5 da bicicleta em
    # 12/11/2026. Sao anuncios DIFERENTES com o mesmo titulo, e e por eles que
    # o pareamento e por POSICAO.
    {"nome": "Bicicleta Elétrica Dobrável Adulto com Pneus A Vácuo", "imagem": {}},
    {"nome": "Bicicleta Elétrica Dobrável Adulto com Pneus A Vácuo", "imagem": {}},
]


def _lista(**troca):
    itens = []
    for i, l in enumerate(LINHAS):
        produto = {"@type": "Product", "name": l["nome"],
                   "offers": {"@type": "Offer", "price": "2299.99"}}
        if (l.get("imagem") or {}).get("url"):
            produto["image"] = l["imagem"]["url"]
        itens.append({"@type": "ListItem", "position": i + 1, "item": produto})
    base = {"@context": "https://schema.org", "@type": "ItemList",
            "name": H1, "description": DESC,
            "numberOfItems": len(itens), "itemListElement": itens}
    base.update(troca)
    return base


AUSENTE = object()


def _pagina_html(lista, descricao=DESC, og=None, h1=H1, quantos_h1=1):
    og = DESC if og is None else og
    og = None if og is AUSENTE else og
    cabeca = '<title>%s</title>' % TITULO
    if descricao is not None:
        cabeca += '<meta name="description" content="%s">' % descricao
    if og is not None:
        cabeca += '<meta property="og:description" content="%s">' % og
    cabeca += ('<script type="application/ld+json">%s</script>'
               % json.dumps(lista, ensure_ascii=False))
    corpo = "".join('<h1>%s</h1>' % h1 for _ in range(quantos_h1))
    corpo += '<img src="%s" alt="foto">' % FOTO
    return "<html><head>%s</head><body>%s</body></html>" % (cabeca, corpo)


def _medir(lista, **kw):
    linhas = kw.pop("linhas", LINHAS)
    html = _pagina_html(lista, **kw)
    tela = declaracoes_da_pagina(html)
    return (problemas_do_envelope("mundo", lista, tela, linhas)
            + problemas_da_foto_na_tela("mundo", lista, html, linhas))


def _regua_ingenua(lista, html):
    """A REGUA QUE ALGUEM ESCREVERIA SEM PENSAR, refeita ao lado da nova e
    obrigada a DISCORDAR dela (20.8): ela confere que os NOMES da lista sao os
    da fonte, como CONJUNTO, e que a contagem bate. Autoteste em que as duas
    concordam nao mede conserto nenhum."""
    nomes_ld = sorted((e.get("item") or {}).get("name") or ""
                      for e in (lista.get("itemListElement") or []))
    nomes_fonte = sorted(l["nome"] for l in LINHAS)
    maus = []
    if nomes_ld != nomes_fonte:
        maus.append("nomes diferentes")
    if lista.get("numberOfItems") != len(lista.get("itemListElement") or []):
        maus.append("contagem diferente")
    return maus


def mundos():
    print("MUNDOS FABRICADOS — o que cada afirmacao do envelope faz morder")

    # 0. O MUNDO SAUDAVEL PASSA. Sem isto, tudo o que vem abaixo e um portao
    #    que reprova a pagina certa.
    saudavel = _lista()
    ok(_medir(saudavel) == [],
       "0. o mundo saudavel passa com ZERO problema (deu %s)" % _medir(saudavel)[:1])

    # 1. O DEFEITO DO DIA: a description da lista e a da pagina discordam.
    m = _medir(_lista(description=DESC + " E mais uma frase."))
    ok(any("ItemList.description" in f for f in m),
       "1. description do ItemList diferente da meta description REPROVA")

    # 1-b. E o contrario tambem: a pagina muda e a lista fica para tras.
    m = _medir(saudavel, descricao=DESC.replace("hoje", "agora"), og=DESC.replace("hoje", "agora"))
    ok(any("ItemList.description" in f for f in m),
       "1-b. a meta description mudar e a lista ficar para tras REPROVA")

    # 2. O PAR og: PELA METADE — o estado em que o og:title viveu errado.
    m = _medir(saudavel, og=DESC.replace("hoje", "neste momento"))
    ok(any("og:description" in f for f in m),
       "2. og:description diferente da meta description REPROVA")
    m = _medir(saudavel, og=AUSENTE)
    ok(any("og:description" in f for f in m),
       "2-b. og:description AUSENTE com meta description presente REPROVA")

    # 3. O NOME DA LISTA E O H1.
    m = _medir(_lista(name="Bicicletas elétricas"))
    ok(any("ItemList.name" in f for f in m),
       "3. name do ItemList diferente do <h1> REPROVA")
    m = _medir(_lista(name=TITULO))
    ok(any("ItemList.name" in f for f in m),
       "3-b. name servindo o <title> no lugar do <h1> REPROVA — e e a forma "
       "exata do defeito do og:title de 11/11")
    m = _medir(saudavel, quantos_h1=2)
    ok(any("<h1>" in f for f in m),
       "3-c. pagina com dois <h1> DENUNCIA em vez de aprovar em silencio")

    # 4. A LISTA QUE SE CONTRADIZ SOZINHA.
    l = _lista()
    l.pop("numberOfItems")
    ok(any("numberOfItems" in f for f in _medir(l)),
       "4. numberOfItems ausente REPROVA (25.9)")
    ok(any("se contradiz sozinha" in f for f in _medir(_lista(numberOfItems=9))),
       "4-b. numberOfItems diferente da contagem servida REPROVA")
    ok(any("numero" in f for f in _medir(_lista(numberOfItems="seis"))),
       "4-c. numberOfItems que nao e numero REPROVA")
    ok(any("ZERO item" in f for f in _medir(_lista(itemListElement=[],
                                                   numberOfItems=0), linhas=[])),
       "4-d. ItemList vazio REPROVA")

    # 5. AS POSICOES, QUE SAO O QUE SUSTENTA O PAREAMENTO DA `Offer`.
    l = _lista()
    l["itemListElement"][0]["position"] = 3
    l["itemListElement"][2]["position"] = 1
    ok(any("posicoes" in f for f in _medir(l)),
       "5. posicoes fora de ordem REPROVAM — e com elas a data da coleta de "
       "cada Offer passaria a ser lida da linha errada")
    l = _lista()
    for e in l["itemListElement"]:
        e["position"] = 1
    ok(any("posicoes" in f for f in _medir(l)),
       "5-b. posicao repetida REPROVA")
    l = _lista()
    for i, e in enumerate(l["itemListElement"]):
        e["position"] = i
    ok(any("posicoes" in f for f in _medir(l)),
       "5-c. posicao comecando em ZERO REPROVA")

    # 6. OS TIPOS DE CADA DEGRAU.
    l = _lista()
    l["itemListElement"][1]["@type"] = "Thing"
    ok(any("tinha de ser ListItem" in f for f in _medir(l)),
       "6. degrau que nao e ListItem REPROVA")
    l = _lista()
    l["itemListElement"][1]["item"]["@type"] = "Thing"
    ok(any("tinha de ser Product" in f for f in _medir(l)),
       "6-b. item que nao e Product REPROVA")
    l = _lista()
    l["itemListElement"][1]["item"]["name"] = ""
    ok(any("nao tem `name`" in f for f in _medir(l)),
       "6-c. item sem nome REPROVA")
    l = _lista()
    l["itemListElement"][1].pop("item")
    ok(any("nao carrega `item`" in f for f in _medir(l)),
       "6-d. degrau sem item REPROVA")

    # 7. O PAREAMENTO COM A FONTE, e e aqui que mora a discordancia da 20.8.
    l = _lista()
    l["itemListElement"][0], l["itemListElement"][2] = (
        l["itemListElement"][2], l["itemListElement"][0])
    for i, e in enumerate(l["itemListElement"]):
        e["position"] = i + 1
    m = _medir(l)
    ok(any("nao esta na ordem da fonte" in f for f in m),
       "7. lista REORDENADA, com as posicoes renumeradas, REPROVA pelo nome da "
       "fonte — e e o mundo em que a Offer da linha 1 receberia a data da linha 3")
    ingenua = _regua_ingenua(l, _pagina_html(l))
    ok(ingenua == [] and m != [],
       "7-b. a regua INGENUA (nomes como conjunto, mais a contagem) APROVA essa "
       "lista reordenada e a nova a REPROVA — as duas DISCORDAM, senao este "
       "autoteste nao mede conserto nenhum (20.8)")
    ok(_medir(_lista(), linhas=LINHAS[:2]) != [],
       "7-c. vitrine com menos linhas que a lista REPROVA")

    # 8. A FOTO, NA DIRECAO QUE O AR PROVOU SER A CERTA.
    #    A foto que a tela serve e o ItemList nao declara REPROVA; a declarada
    #    que a tela nao serve NAO reprova, porque a tabela da secao 7 nao leva
    #    foto e o carrossel tem teto pela 32.1. Os dois mundos estao aqui porque
    #    a primeira versao desta regua reprovou as duas paginas sas.
    l = _lista()
    l["itemListElement"][0]["item"].pop("image")
    m = _medir(l)
    ok(any("o leitor ve o que a maquina nao recebe" in f for f in m),
       "8. foto que a TELA serve e o ItemList nao declara REPROVA")
    ok(any("foto na fonte e nao a declara" in f for f in m),
       "8-b. e a mesma ausencia REPROVA tambem contra a fonte (25.9)")
    l = _lista()
    l["itemListElement"][0]["item"]["image"] = "https://outro.site/x.jpg"
    ok(any("e a fonte tem" in f for f in _medir(l)),
       "8-c. foto declarada DIFERENTE da que a fonte tem REPROVA")
    # E O MUNDO QUE NAO PODE REPROVAR, que e o do ar de hoje: declarar foto de
    # anuncio que so aparece na TABELA, sem foto na tela.
    l = _lista()
    for e in l["itemListElement"][1:]:
        e["item"]["image"] = "https://cf.shopee.com.br/file/so-na-tabela-%d" % id(e)
    ok(_medir(l) == [],
       "8-d. foto declarada que a tela NAO serve passa — e o estado das duas "
       "paginas no ar (6 declaradas e 3 na tela; 15 e 5)")
    ok(fotos_na_tela(l, _pagina_html(l), LINHAS) == (1, 3),
       "8-e. e o registro conta quantas estao na tela, sem virar veredito")

    # 9. OS DOIS TITULOS IDENTICOS DO AR NAO SAO DEFEITO. Esta e a afirmacao
    #    que impede o portao de reprovar a pagina certa: as posicoes 4 e 5 da
    #    bicicleta sao anuncios diferentes com o MESMO titulo, e passaram.
    ok(_medir(saudavel) == [],
       "9. os DOIS anuncios de titulo identico da fonte NAO reprovam")

    # 10. A PAGINA SEM `ItemList` NAO E PROBLEMA DESTE ARQUIVO — ele mede o
    #     envelope de quem tem. Oito das dez URLs desta ilha nao servem nenhum.
    ok(itemlists_do_html("<html><head></head><body><h1>x</h1></body></html>") == [],
       "10. pagina sem ItemList devolve lista vazia, sem acusar nada")

    # 11. E ELE ACHA O `ItemList` ONDE ELE ESTIVER: solto, dentro de um array e
    #     dentro de `@graph`. Esta ilha serve o solto hoje; regua que so
    #     alcanca a forma de hoje fica cega no dia em que a forma mudar.
    solto = '<script type="application/ld+json">%s</script>' % json.dumps(_lista())
    dentro = ('<script type="application/ld+json">%s</script>'
              % json.dumps({"@context": "https://schema.org",
                            "@graph": [{"@type": "WebPage"}, _lista()]}))
    array = ('<script type="application/ld+json">%s</script>'
             % json.dumps([{"@type": "WebPage"}, _lista()]))
    ok(len(itemlists_do_html(solto)) == 1, "11. acha o ItemList solto")
    ok(len(itemlists_do_html(dentro)) == 1, "11-b. acha o ItemList dentro de @graph")
    ok(len(itemlists_do_html(array)) == 1, "11-c. acha o ItemList dentro de array")
    ok(len(itemlists_do_html(solto + dentro)) == 2,
       "11-d. acha os DOIS quando a pagina serve dois")
    ok(itemlists_do_html('<script type="application/ld+json">{quebrado</script>') == [],
       "11-e. JSON-LD quebrado nao derruba este arquivo — a validade e do "
       "conferir-no-ar.py e duplica-la aqui seria a 20.7")

    # 12. AS ENTIDADES. O atributo vem escapado do `esc_attr` e o JSON-LD nao:
    #     comparar sem desfazer reprovaria toda description com aspas ou `&`.
    com_e = "Bateria & motor: o que o anúncio declara"
    l = _lista(description=com_e)
    html = _pagina_html(l, descricao="Bateria &amp; motor: o que o anúncio declara",
                 og="Bateria &amp; motor: o que o anúncio declara")
    tela = declaracoes_da_pagina(html)
    ok(problemas_do_envelope("x", l, tela, LINHAS) == [],
       "12. `&` escapado no atributo e cru no JSON-LD NAO reprova (sao a mesma "
       "frase, e e a familia do &#038; que a secao 12 cobra)")

    print("  %d afirmacoes nos mundos fabricados" % AFIRMACOES[0])


def main():
    print("PORTAO DO ENVELOPE DO ItemList — RODAMETRIA")
    mundos()
    print()
    print("teste-envelope-do-itemlist: %d afirmacoes, %d falha(s)"
          % (AFIRMACOES[0], len(FALHAS)))
    for f in FALHAS[:40]:
        print("  FALHA", f)
    print("REPROVADO" if FALHAS else "APROVADO")
    return 1 if FALHAS else 0


if __name__ == "__main__":
    sys.exit(main())
