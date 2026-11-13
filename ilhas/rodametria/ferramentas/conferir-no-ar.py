#!/usr/bin/env python3
"""
CONFERE A ILHA NO AR — o portao que a secao 8 do ARQUIPELAGO.md exige por escrito.

    "Depois de publicar, busque a URL no ar e confira com numero medido:
     (1) HTTP 200; (2) zero entidades &#038; DENTRO de <script>; (3) o corpo
     comeca pelo texto e nao por metadado; (4) o script vem do rodape e a tabela
     de exemplos aparece no HTML servido; (5) a revisao aplicada bate com a do
     manifest."

Mais o que as outras secoes cobram e que esta ilha tinha de herdar pronto:
  - a PORTA DE ENTRADA da 29.2 (robots.txt em text/plain, wp-sitemap.xml em
    application/xml, wp-json em application/json, e caminho virgem em 404);
  - a ROTA QUE MEDE A PORTA POR DENTRO, da 29.3, lida SEM o token: ela existe
    no indice de rotas, nega quem nao tem token, e o CODIGO da negativa prova
    que a parede achou a fonte do token e comparou. Nasceu em 03/11/2026, com
    a rota, e reprovou contra o ar ANTES do desembarque — quatro falhas, as
    quatro certas;
  - o PORTAO DO DESEMBARQUE da 20.4: o log do /status e lido LINHA POR LINHA e
    nenhuma linha da revisao corrente pode deixar de dizer `ok`. Resumo verde
    nao e entrega;
  - a 20.5: revisao atrasada com log de AGORA e cache do GitHub, nao defeito —
    e o portao diz qual dos dois e, em vez de reprovar os dois igual;
  - a 20.4 OUTRA VEZ, por outro caminho (02/11/2026): a VERSAO que o WordPress
    carregou de cada snippet, lida em `/casca` -> `versoes`, contra o campo
    `versao` do manifest. O sha256 e sobre o byte do repositorio e NAO alcanca
    snippet `gravado mas NAO ativado`; o `id` que falta no /casca e esse defeito,
    e o portao diz "nao ativado" e "versao diferente" separados, porque o
    conserto das duas nao e o mesmo;
  - a 32.4: zero palavra de bastidor da fabrica no texto servido;
  - a 32.5 pede medicao a 390 px num navegador de verdade, e ISSO NAO E AQUI:
    quem faz e `conferir-32-5-no-navegador.mjs` (a copiar do modelo da
    clubedomosaico quando esta ilha tiver molde em mais de uma pagina). Este
    portao mede o que se mede no HTML servido, e DIZ que nao mediu pixel —
    aprovar em silencio o que nao se mediu e o defeito que a 32.5-b nomeou.

TODA URL E PEDIDA COM QUEBRA DE CACHE: as afirmacoes aqui sao sobre a ORIGEM.
Quem le como o Google le, sem quebra de cache, e outro portao.
"""

# A FUNCAO VEM COM NOME PROPRIO, E NAO O MODULO: `import html` seria SOMBREADO
# dentro do laco, porque a variavel que guarda o corpo da pagina tambem se chama
# `html` (a linha do `cod, ct, html = buscar(...)`) — e a chamada ao modulo
# morreria com AttributeError na PRIMEIRA description medida. Nenhuma LEITURA
# pega isso: o nome existe, certinho, nos dois lugares. Quem pegou foi perguntar
# ao arquivo quem MAIS usa o nome, antes de empurrar.
from datetime import datetime, timedelta
from html import unescape as desescapar_entidades
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)
DOMINIO = "https://rodametria.com.br"


# ---------------------------------------------------------------------------
# A REGUA DAS DUAS AFIRMACOES QUE ESTA ILHA NAO PODE FAZER MORA EM OUTRO PORTAO,
# E E IMPORTADA DAQUI EM VEZ DE REESCRITA (06/11/2026)
#
# `ferramentas/teste-afirmacao-de-tela.py` e dono da regra: a de HABILITACAO
# (itens 3 e 4 do despacho de 06/11) e a do PESO DE QUEM PILOTA NA AUTONOMIA
# (item 2). Ele a aplica ao REPOSITORIO, sem rede; este portao a aplica ao HTML
# SERVIDO de toda URL do `wp-sitemap.xml` e aos blocos `application/ld+json`,
# que e onde o item 3 do despacho manda a regua chegar — *"o portao que cobra
# isso roda sobre TODAS as URLs do wp-sitemap.xml, e nao so sobre as telas da
# F1"*.
#
# POR QUE IMPORTAR E NAO COPIAR: duas copias da mesma regra sao a "segunda
# declaracao do mesmo fato" que a 20.7 proibe nesta ilha — *"duas declaracoes do
# mesmo fato comecam iguais e so uma sobe"*. E isto NAO fere a regra da secao 8
# ("quem confere escreve a propria regua, nunca chama a de quem produziu o
# dado"): a regua de afirmacao nao PRODUZ texto nenhum, ela so o reprova.
#
# Se o irmao nao estiver no disco, este portao DIZ e segue — mas as duas
# afirmacoes ficam sem medir, e isso vai para o relatorio em vez de passar calado.
_REGUA_DE_AFIRMACAO = None
try:
    import importlib.util as _ilu

    _spec = _ilu.spec_from_file_location(
        "rodametria_afirmacao_de_tela",
        os.path.join(AQUI, "teste-afirmacao-de-tela.py"))
    _REGUA_DE_AFIRMACAO = _ilu.module_from_spec(_spec)
    _spec.loader.exec_module(_REGUA_DE_AFIRMACAO)
except Exception as _e:  # noqa: BLE001 — qualquer falha aqui e "nao medi"
    _POR_QUE_SEM_REGUA = str(_e)


# A REGUA DA REMISSAO DE CAMADA, pelo MESMO desenho e pela mesma razao
# (09/11/2026). Dona: `ferramentas/teste-remissao-de-camada.py`, que a aplica ao
# repositorio e aos mundos fabricados; aqui ela chega ao JSON-LD SERVIDO de toda
# URL do sitemap, que e onde os dois defeitos que a fizeram nascer foram
# medidos: a seta `logo abaixo` na resposta do `FAQPage` da F3 e a oracao
# declarada duas vezes na resposta do pico, na home.
_REGUA_DE_REMISSAO = None
_POR_QUE_SEM_REMISSAO = ""
try:
    import importlib.util as _ilu2

    _spec2 = _ilu2.spec_from_file_location(
        "rodametria_remissao_de_camada",
        os.path.join(AQUI, "teste-remissao-de-camada.py"))
    _REGUA_DE_REMISSAO = _ilu2.module_from_spec(_spec2)
    _spec2.loader.exec_module(_REGUA_DE_REMISSAO)
except Exception as _e2:  # noqa: BLE001
    _POR_QUE_SEM_REMISSAO = str(_e2)


# A REGUA DO ENVELOPE DO `ItemList`, pelo MESMO desenho e pela mesma razao
# (12/11/2026). Dona: `ferramentas/teste-envelope-do-itemlist.py`, que a aplica
# aos mundos fabricados; `conferir-produto-no-ar.py` a aplica as duas paginas de
# vitrine COM as linhas da fonte na mao. **Aqui ela alcanca TODA URL do
# `wp-sitemap.xml`**, sem a fonte — porque `ItemList` servido em pagina que
# ninguem esperava e justamente o caso que uma lista digitada nao alcanca
# (32.5-b), e porque hoje 8 das 10 URLs desta ilha nao servem nenhum.
_REGUA_DO_ENVELOPE = None
_POR_QUE_SEM_ENVELOPE = ""
try:
    import importlib.util as _ilu3

    _spec3 = _ilu3.spec_from_file_location(
        "rodametria_envelope_do_itemlist",
        os.path.join(AQUI, "teste-envelope-do-itemlist.py"))
    _REGUA_DO_ENVELOPE = _ilu3.module_from_spec(_spec3)
    _spec3.loader.exec_module(_REGUA_DO_ENVELOPE)
except Exception as _e3:  # noqa: BLE001
    _POR_QUE_SEM_ENVELOPE = str(_e3)


# As marcacoes que carregam PROSA nesta ilha. `label` e `option` ficam FORA de
# proposito: o campo "Seu peso" da F2 e um ROTULO de formulario, e medi-lo como
# afirmacao reprovaria o formulario que a propria ferramenta precisa ter.
TAGS_DE_PROSA = ("p", "li", "h1", "h2", "h3", "h4", "summary", "dt", "dd",
                 "td", "th", "caption", "figcaption", "blockquote")
_RE_ELEMENTOS = re.compile(
    r"<(%s)\b[^>]*>(.*?)</\1>" % "|".join(TAGS_DE_PROSA), re.S | re.I)


# ---------------------------------------------------------------------------
# AS CINCO REGUAS DE TELA SOBRE O TEXTO SERVIDO, E A CITACAO E DESCONTADA ANTES
# (10/11/2026)
# ---------------------------------------------------------------------------
#
# O QUE FEZ ISTO NASCER: o fecho de 10/11 as 10h45Z deixou escrito, como o que
# sobrou para quem viesse, que *"as reguas de tela desta ilha agora moram num
# lugar so e cobrem quatro classes, mas alcancam A FRASE DE PROCEDENCIA das
# constantes — nao todo texto que um snippet imprime"*, e que o caminho era
# *"LER A PAGINA SERVIDA COM OS OLHOS e perguntar em que vocabulario ela esta
# falando"*. Esta e aquela leitura virada mecanismo, e ela achou DOIS defeitos
# na mesma passada:
#
#   - a F2 servindo `Tipo: observacao_de_mercado`, a chave de maquina como frase;
#   - a `/privacidade/` servindo "as fontes da letra desta pagina em toda
#     pagina" e "a foto do produto, quando a pagina tem uma nas paginas com foto
#     de produto" — CINCO `pagina`/`paginas` sem acento na voz da propria ilha,
#     e a mesma coisa dita DUAS VEZES na mesma oracao.
#
# POR QUE O PORTAO MORA NO AR E NAO NO REPOSITORIO, E ISTO FOI MEDIDO ANTES DE
# ESCOLHER: rodar as cinco reguas sobre TODO texto de tela dos arquivos de dado
# devolve 188 falhas, e a esmagadora maioria NAO e tela — e prosa de bastidor
# (`especificacao`, `a_caixa_da_mae`, `por_que_ancora`,
# `vendas_ordenam_e_nao_vao_para_a_tela`) e CITACAO (titulo de anuncio colhido,
# chave da loja). Um portao assim reprovaria a pagina certa em massa, que e o
# caminho mais curto para alguem passar a ignora-lo (20.5) — e contorcer a copia
# para agradar regua errada e pior que a regua errada, que e a licao escrita
# nesta ilha em 06/11. No ar a pergunta e outra e e a certa: o que o VISITANTE
# le esta no vocabulario dele?
#
# E A CITACAO E DESCONTADA POR LITERAL, NUNCA POR ELEMENTO. Esta ilha cita o
# titulo do anuncio letra por letra de proposito — e a tese dela, *"o numero do
# anuncio nao e o que a regra le"* —, e cita a CHAVE DA LOJA entre aspas porque
# *"a consulta e a palavra da PESSOA; a chave e a palavra da LOJA"*. As duas
# chegam a tela sem acento e estao CERTAS. O desconto remove a cadeia exata e
# mede o que sobra: defeito DENTRO da citacao fica invisivel (e deve), e defeito
# ao lado dela continua sendo pego. Pular o elemento inteiro perdoaria a frase
# da ilha que convive com um titulo colhido na mesma linha.
#
# MEDIDO EM 10/11/2026 as 13h2xZ, nas 10 URLs: 17 achados, dos quais 16 eram
# citacao (titulo de anuncio e chave da loja) e 1 era a ilha falando.

# Os nomes de campo que carregam CITACAO nos arquivos de dado desta ilha. Cada
# um esta aqui com a razao, porque lista sem razao envelhece calada:
#   titulo_colhido/titulo_do_anuncio/titulo_da_oferta — o anuncio, letra por letra
#   nome/rotulo/alt — a copia que o gerador promove daquele titulo (`regras/nomes.py`)
#   chave/chave_da_loja/chave_escolhida/chave_que_achou — a palavra da LOJA
#   consulta — a palavra da PESSOA, servida entre aspas
CHAVES_DE_CITACAO_NO_DADO = (
    "titulo_colhido", "titulo_do_anuncio", "titulo_da_oferta",
    "nome", "rotulo", "alt",
    "chave", "chave_da_loja", "chave_escolhida", "chave_que_achou",
    "consulta",
)


def citacoes_do_dado(pasta=None):
    """Toda cadeia que esta ilha CITA, colhida dos arquivos de `dados/`.

    Devolve a lista ordenada da mais longa para a mais curta, porque o desconto
    e por substring: descontar a curta primeiro picaria a longa e deixaria
    pedacos soltos que a regua leria como texto da ilha.
    """
    pasta = pasta or os.path.join(ILHA, "dados")
    achadas = set()

    def anda(x, chave=None):
        if isinstance(x, dict):
            for k, v in x.items():
                anda(v, k)
        elif isinstance(x, list):
            for v in x:
                anda(v, chave)
        elif isinstance(x, str) and chave in CHAVES_DE_CITACAO_NO_DADO:
            if len(x.strip()) >= 4:
                achadas.add(x.strip())

    if os.path.isdir(pasta):
        for nome in sorted(os.listdir(pasta)):
            if not nome.endswith(".json"):
                continue
            try:
                with open(os.path.join(pasta, nome), encoding="utf-8") as f:
                    anda(json.load(f))
            except Exception:  # noqa: BLE001 — arquivo ilegivel nao e desta regua
                continue

    return sorted(achadas, key=lambda t: (-len(t), t))


def _um_espaco(t):
    """Espaco normalizado — e esta funcao e o conserto de um falso positivo MEDIDO.

    O HTML colapsa espaco e o extrator normaliza; o arquivo de dado guarda o que
    a loja serviu. O titulo colhido do anuncio `Bicicleta Eletrica Ebike M2 (...)
    bike eletrica  E` tem DOIS espacos antes do `E` no dado e UM no ar, e por
    isso o desconto por literal cru nao o removia: a citacao sobrevivia ao
    desconto e a regua de acento a reprovava por `eletric`, que esta CERTO
    porque e o anuncio falando. Portao que reprova a citacao que a ilha faz de
    proposito e o caminho mais curto para alguem ignora-lo (20.5).
    """
    return re.sub(r"\s+", " ", t).strip()


def descontar_citacoes(texto, citacoes):
    """O texto sem as cadeias que a ilha cita — e o que sobra e a voz dela."""
    texto = _um_espaco(texto)
    for c in citacoes:
        c = _um_espaco(c)
        if c and c in texto:
            texto = texto.replace(c, " ")

    return texto


def problemas_de_vocabulario_servido(onde, textos, citacoes):
    """As cinco reguas de tela sobre o texto SERVIDO, citacao descontada.

    A regua e de `teste-afirmacao-de-tela.py` e esta importada no topo; o que e
    DAQUI e a superficie (o HTML servido) e o desconto da citacao.
    """
    if _REGUA_DE_AFIRMACAO is None:
        return []
    falhas = []
    for i, t in enumerate(textos):
        limpo = descontar_citacoes(t, citacoes)
        if not limpo.strip():
            continue
        falhas += _REGUA_DE_AFIRMACAO.problemas_de_procedencia(
            "%s elemento %d" % (onde, i + 1), limpo)

    return falhas


def elementos_de_prosa(corpo):
    """Cada elemento de prosa da pagina, como texto, na ordem em que e servido."""
    out = []
    sem_rotulo = re.sub(r"<label\b.*?</label>", " ", corpo, flags=re.S | re.I)
    for m in _RE_ELEMENTOS.finditer(sem_rotulo):
        t = desescapar_entidades(re.sub(r"<[^>]+>", " ", m.group(2)))
        t = re.sub(r"\s+", " ", t).strip()
        if t:
            out.append(t)

    return out


# ---------------------------------------------------------------------------
# O ARTIGO CONCORDA COM A LOJA QUE A FRASE NOMEIA (11/11/2026)
# ---------------------------------------------------------------------------
#
# MEDIDO NO AR as 13h2xZ de 11/11/2026, nos dois cartoes de Mercado Livre da
# pagina da F2: *"R$ 8.244,00 lido na Mercado Livre em 27/10/2026"*. `Mercado
# Livre` e masculino e a frase o tratava como feminino, porque a PREPOSICAO
# era literal no PHP (`'lido na ' . $loja`) e so o NOME vinha da funcao.
#
# POR QUE A REGUA MORA TAMBEM NO AR, e nao so no portao do chao que conserta a
# frase: o chao mede UMA funcao, e o nome da loja chega a tela por mais de um
# caminho — o rotulo do botao, a nota do preco, a linha do piso, a prosa do
# escopo da vitrine e a dobra "Como sabemos". Regua no ar nao pergunta por
# onde a frase veio.
#
# MEDIDO ANTES DE ENTRAR, nas 10 URLs: 43 pares de artigo com nome de loja no
# texto de prosa — 38 `na Shopee`, 3 `a Shopee` e os 2 `na Mercado Livre` do
# defeito. ZERO falso positivo, inclusive nos titulos de anuncio colhidos, que
# e onde uma regua de vocabulario costuma tropecar nesta ilha.
#
# A TABELA DE GENERO E ESCRITA AQUI, nao importada de quem produz a frase —
# secao 8: *"quem confere escreve a propria regua, nunca chama a de quem
# produziu o dado"*.
GENERO_DA_LOJA = {"Shopee": "f", "Mercado Livre": "m"}
_RE_ARTIGO_DA_LOJA = re.compile(
    r"\b(n?[ao]s?)\s+(%s)\b" % "|".join(re.escape(k) for k in GENERO_DA_LOJA))


def problemas_de_artigo_da_loja(textos):
    """Artigo de um genero colado ao nome de loja do outro. Funcao pura."""
    ruim = []
    for t in textos:
        for m in _RE_ARTIGO_DA_LOJA.finditer(t):
            artigo, loja = m.group(1), m.group(2)
            masculino = "o" in artigo
            if (GENERO_DA_LOJA[loja] == "m") != masculino:
                ruim.append("o artigo discorda da loja: %r em %r — o genero e propriedade "
                            "do NOME e nao da frase" % (m.group(0), t[:120]))

    return ruim


# ---------------------------------------------------------------------------
# A TERCEIRA SUPERFICIE: O TEXTO QUE VIVE EM ATRIBUTO (10/11/2026, 16h3xZ)
# ---------------------------------------------------------------------------
#
# O FECHO DAS 14h13Z DE HOJE DEIXOU ESTA FAMILIA ESCRITA, letra por letra, como
# o que sobrava para quem viesse: *"as cinco reguas de tela agora correm sobre o
# AR (...) e o alcance delas e o TEXTO DE PROSA (`<p>`, `<li>`, `<h1>`...,
# `<td>`). O que elas NAO alcancam e o texto que vive em ATRIBUTO — `alt`,
# `title`, `aria-label`"*. Esta e aquela ponta, e ela achou defeito no ar na
# primeira passada: `/veiculos/patinete-eletrico/` servia, no `title` do `<td>`
# da coluna de carga, `o titulo nao declara nenhum kg` NOVE vezes e
# `/veiculos/bicicleta-eletrica/` SEIS — frase da ilha, em portugues sem acento,
# dentro do atributo que o visitante le ao parar o ponteiro na celula e que o
# leitor de tela anuncia.
#
# `elementos_de_prosa` NAO podia ver isso: ela recorta o MIOLO das marcacoes de
# prosa e joga as marcacoes fora com `re.sub(r"<[^>]+>", " ", ...)`. O atributo
# mora justamente no que ela descarta.
#
# AS QUATRO MARCACOES DE FORA, cada uma com a razao, porque lista sem razao
# envelhece calada:
#   script/style — ali mora codigo, nao texto de leitor (a 20.8 ja separa isso)
#   link         — `title="Feed para Rodametria »"`, `title="RSD"` e
#                  `title="oEmbed (JSON)"` sao do WordPress e nao desta ilha:
#                  nenhum visitante os le, e cobra-los seria reprovar a pagina
#                  certa por texto que a fabrica nao escreve (20.5)
#
# E O `<meta>` ENTRA SO POR TRES NOMES. `content` carrega
# `width=device-width`, `#13212B`, `website`, `pt_BR` e `WordPress 7.1.4` —
# valor de maquina que a ilha nao escolhe. O que ela escreve e a `description` e
# o par `og:`, que e texto de leitor servido no resultado de busca e no cartao
# de compartilhamento. Medido antes de escolher: com os tres, 16 achados e ZERO
# falso positivo nas outras oito URLs; sem o recorte, a tupla inteira de
# `content` reprovaria as dez.
ATRIBUTOS_DE_LEITOR = ("title", "alt", "aria-label", "placeholder")
TAGS_SEM_TEXTO_DE_LEITOR = ("script", "style", "link")
META_DE_LEITOR = ("description", "og:description", "og:title")

_RE_MARCACAO = re.compile(r"""<([a-zA-Z][\w:-]*)((?:[^<>"]|"[^"]*")*)>""")
_RE_NOME_DO_META = re.compile(r"""\b(?:name|property)\s*=\s*"([^"]*)\"""", re.I)


def textos_de_atributo(corpo):
    """Cada texto de ATRIBUTO que o visitante le, com onde ele mora.

    Devolve pares `(onde, texto)`. `onde` diz o atributo e a marcacao — `title@td`,
    `alt@img` — porque o conserto de cada um e em lugar diferente e mensagem que
    nao diz onde manda alguem procurar.
    """
    out = []
    for m in _RE_MARCACAO.finditer(corpo):
        tag = m.group(1).lower()
        atributos = m.group(2)
        if tag in TAGS_SEM_TEXTO_DE_LEITOR:
            continue
        if tag == "meta":
            nome = _RE_NOME_DO_META.search(atributos)
            if not nome or nome.group(1).lower() not in META_DE_LEITOR:
                continue
            for valor in re.finditer(r'\bcontent\s*=\s*"([^"]*)"', atributos, re.I):
                texto = desescapar_entidades(valor.group(1)).strip()
                if texto:
                    out.append(("meta[%s]" % nome.group(1).lower(), texto))
            continue
        for atributo in ATRIBUTOS_DE_LEITOR:
            padrao = r'\b%s\s*=\s*"([^"]*)"' % re.escape(atributo)
            for valor in re.finditer(padrao, atributos, re.I):
                texto = desescapar_entidades(valor.group(1)).strip()
                if texto:
                    out.append(("%s@%s" % (atributo, tag), texto))

    return out


def frases_e_pares_do_jsonld(blocos):
    """As strings de todo JSON-LD e os pares (pergunta, resposta) de FAQPage.

    O item 4 do despacho de 06/11/2026 e literal sobre por que isto existe: a
    `FAQPage` da bicicleta respondia "precisa de CNH?" com **nao** na camada
    estruturada, e *"a que vai para o Google e a do JSON-LD"*. Nenhuma regua
    desta ilha olhava para dentro dele procurando afirmacao de habilitacao.
    """
    textos = []
    pares = []
    for b in blocos:
        try:
            d = json.loads(b)
        except Exception:
            continue
        pilha = [d]
        while pilha:
            x = pilha.pop()
            if isinstance(x, dict):
                if x.get("@type") == "Question":
                    nome = x.get("name")
                    resp = x.get("acceptedAnswer") or {}
                    texto = resp.get("text") if isinstance(resp, dict) else None
                    if isinstance(nome, str) and isinstance(texto, str):
                        pares.append((nome, texto))
                for v in x.values():
                    if isinstance(v, str):
                        textos.append(v)
                    else:
                        pilha.append(v)
            elif isinstance(x, list):
                pilha += x

    return textos, pares


# ---------------------------------------------------------------------------
# AS DUAS SUPERFICIES QUE AS DUAS LISTAS DA 32.4 NUNCA TINHAM LIDO (11/11/2026,
# a tarde)
#
# O `bloco_atual` desta ilha deixou esta ponta escrita de manha: *"o TEXTO DE
# ATRIBUTO (`alt`, `aria-label`, `title`) e o JSON-LD contra a regua de bastidor
# nas 10 URLs de uma vez, agora que a regua de FRONTEIRA existe e pode ser
# apontada para eles"*. As duas superficies JA tinham extrator aqui —
# `textos_de_atributo()` nasceu em 10/11 e `frases_e_pares_do_jsonld()` em
# 06/11 —, e as DUAS listas da 32.4 nunca foram apontadas para nenhum dos dois:
# elas correm sobre o TEXTO VISIVEL e sobre o BYTE SERVIDO INTEIRO.
#
# O BYTE SERVIDO PARECE COBRIR OS DOIS, E E ESSE "PARECE" QUE ESTA MEDIDO AQUI.
# Ele cobre enquanto o byte e igual ao texto que a pessoa le, e as duas
# superficies sao exatamente as duas em que ele NAO e:
#
#   (a) ENTIDADE DE HTML. Atributo nasce de `esc_attr()`, que escreve `&amp;`,
#       `&#039;` e, em servidor com `htmlentities`, tambem o acento. A regua de
#       fronteira DOBRA o acento (`publicável` -> `publicavel`) e nao desdobra
#       entidade: `title="public&aacute;vel"` passa pela regua do byte sem ser
#       vista, e `textos_de_atributo()` ja a entrega desescapada. A mesma coisa
#       vale para `&#105;lha`, que e `ilha` escrito em numero.
#   (b) ESCAPE DE JSON. `wp_json_encode` escreve `á` e `dados\/` quando
#       `JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES` nao vao na chamada.
#       Esta ilha passa as duas bandeiras hoje, nas seis chamadas que servem
#       JSON-LD — contado, nao suposto — e por isso o byte serve `publicável` e
#       `dados/` legiveis. TRES TERMOS DA LISTA DE CIMA TERMINAM EM `/`
#       (`dados/`, `ferramentas/`, `regras/`): no dia em que uma chamada nova
#       nascer sem a bandeira, os tres ficam cegos de uma vez, e NENHUM portao
#       acusaria. `json.loads` desfaz os dois escapes, e e por isso que a regua
#       le o VALOR e nao a linha.
#
# E A TERCEIRA RAZAO NAO E DE CODIFICACAO, E DE ENDERECO (20.5): o byte inteiro
# nao sabe dizer se o termo esta num `alt` que o leitor de tela anuncia, numa
# resposta de `FAQPage` que o Google cita, ou dentro de um comentario nosso —
# e o conserto de cada um fica em arquivo diferente. Afirmacao que nao diz onde
# manda procurar.
# ---------------------------------------------------------------------------

def valores_do_jsonld(blocos):
    """Toda string de todo `application/ld+json`, com o CAMINHO dela dentro do bloco.

    Diferente de `frases_e_pares_do_jsonld()`, que devolve texto solto para as
    reguas de afirmacao: aqui o endereco vem junto (`ld[2]/mainEntity/0/name`),
    porque o conserto de uma string de JSON-LD mora em lugar diferente conforme
    a chave, e mensagem sem endereco manda alguem procurar.

    NENHUMA CHAVE E EXCLUIDA, de proposito. `@context` e `@type` sao vocabulario
    da schema.org e nao prosa desta ilha, e excluir os dois seria barato — mas
    lista de excecao envelhece calada, e as duas foram MEDIDAS em zero achado
    nas 10 URLs antes desta decisao. No dia em que uma palavra da schema.org
    colidir com a lista, o portao diz qual chave e, e a excecao nasce com
    medicao em vez de nascer por precaucao.
    """
    out = []
    for i, bloco in enumerate(blocos):
        try:
            dado = json.loads(bloco)
        except Exception:
            continue

        pilha = [("ld[%d]" % i, dado)]
        while pilha:
            onde, x = pilha.pop()
            if isinstance(x, dict):
                for k, v in x.items():
                    pilha.append(("%s/%s" % (onde, k), v))
            elif isinstance(x, list):
                for j, v in enumerate(x):
                    pilha.append(("%s/%d" % (onde, j), v))
            elif isinstance(x, str) and x.strip():
                out.append((onde, x))

    return out


def problemas_de_bastidor_em_pares(pares, superficie):
    """AS DUAS listas da 32.4 sobre pares `(onde, texto)` JA DESESCAPADOS.

    A de substring e a de fronteira, nesta ordem, com o endereco de dentro da
    pagina em cada linha. O texto chega desescapado de quem chama — e isso e a
    metade que o byte servido nao tem.
    """
    ruim = []
    for onde, texto in pares:
        baixo = texto.lower()
        for termo in BASTIDOR:
            if termo.lower() in baixo:
                ruim.append("32.4 em %s %s: a palavra de bastidor %r — %r"
                            % (superficie, onde, termo, texto[:140]))
        for problema in problemas_de_bastidor_com_fronteira(
                texto, "%s %s" % (superficie, onde)):
            ruim.append("%s — %r" % (problema, texto[:140]))

    return ruim


# ---------------------------------------------------------------------------
# O `alt` QUE DIZ, LETRA POR LETRA, O QUE A PAGINA JA IMPRIME AO LADO
# (11/11/2026, achado na primeira leitura do texto de atributo com os olhos)
#
# MEDIDO NO AR as 19h2xZ de 11/11/2026, em `/veiculos/patinete-eletrico/` e
# `/veiculos/bicicleta-eletrica/`: os 8 cartoes com foto serviam
#
#     <img class="rdm-molde-cartao-foto" ... alt="TITULO DO ANUNCIO">
#     <p class="rdm-molde-cartao-nome">TITULO DO ANUNCIO</p>
#
# com a MESMA cadeia nos dois, encostadas. Para quem usa leitor de tela isso e
# o titulo do anuncio anunciado DUAS vezes por cartao — e o titulo do anuncio
# desta ilha tem 60 a 120 caracteres. E tem a outra metade, que e de voz: o
# `alt` e a ilha descrevendo a imagem com as PALAVRAS DELA, e a cadeia copiada
# diz `Suporta Ate 150kg` e `Ate 30Km/h` sem o verbo que nomeia quem declarou —
# numa ilha cuja tese e que o numero do anuncio engana (26, e o item 4 do
# despacho de 09/11, que ancorou a regua no VERBO). Na tela a cadeia tem a
# frase de escopo do carrossel acima dela dizendo de onde ela vem; no atributo
# nao tem vizinho nenhum.
#
# POR QUE A REGUA MEDE IGUALDADE E NAO A FRASE: igualdade e conferivel sem
# escolher redacao, e e ela que prova a repeticao. Um `alt` que descreva a FOTO
# (o que ela mostra) passa, porque nao e igual ao texto ao lado; um `alt` vazio
# passa, porque atributo vazio e a declaracao de que a imagem e redundante — que
# e a verdade aqui — e `textos_de_atributo()` ja nao o conta. O que ela reprova
# e a copia.
# ---------------------------------------------------------------------------

_RE_IMG_COM_ALT = re.compile(r'<img\b[^>]*\balt\s*=\s*"([^"]*)"[^>]*>', re.I)
_RE_PROSA_VIZINHA = re.compile(
    r'<(p|h1|h2|h3|h4|li|td|figcaption|span)\b[^>]*>(.*?)</\1>', re.I | re.S)


def _texto_cru(fragmento):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ",
                                      desescapar_entidades(fragmento))).strip()


def alts_que_repetem_a_prosa_vizinha(corpo, vizinhanca=600):
    """`alt` identico ao texto do primeiro elemento de prosa que vem depois dele.

    Devolve uma linha por ocorrencia. A janela e de `vizinhanca` caracteres de
    HTML depois da tag: o cartao desta ilha imprime o nome na marcacao
    IMEDIATAMENTE seguinte, e janela maior passaria a casar com prosa que a
    pessoa nao le junto com a imagem.
    """
    ruim = []
    for m in _RE_IMG_COM_ALT.finditer(corpo):
        alt = _texto_cru(m.group(1))
        if not alt:
            continue
        depois = corpo[m.end():m.end() + vizinhanca]
        vizinho = _RE_PROSA_VIZINHA.search(depois)
        if not vizinho:
            continue
        if _texto_cru(vizinho.group(2)) == alt:
            ruim.append("o `alt` da imagem repete, letra por letra, o <%s> que a "
                        "pagina imprime logo depois dela — leitor de tela diz a "
                        "mesma cadeia duas vezes: %r"
                        % (vizinho.group(1).lower(), alt[:120]))

    return ruim


# ---------------------------------------------------------------------------
# A CELULA DA TABELA VIRA ORACAO DENTRO DE UMA FRASE, E A CONCORDANCIA E DE QUEM
# ESCREVEU PRIMEIRO (11/11/2026, achado na primeira leitura do JSON-LD com os
# olhos)
#
# MEDIDO NO AR as 19h2xZ de 11/11/2026, na home, nas DUAS camadas: a `FAQPage`
# servia *"o art. 12 diz que o veiculo nao e **sujeita** a registro,
# licenciamento nem placa"* e a tabela visivel, tres dobras acima, servia a
# MESMA cadeia na linha `bicicleta eletrica`. Na mesma pagina, a resposta
# seguinte dizia *"ele nao e **sujeito**"*. Duas concordancias para a mesma
# afirmacao, e uma delas errada.
#
# A CAUSA NAO E ERRO DE DIGITACAO, E E POR ISSO QUE ISTO E PORTAO E NAO CONSERTO
# DE UMA PALAVRA. O campo `placa` da tabela da regra e UM dado servido em DOIS
# lugares, de proposito — o comentario de `rodametria-f1.php` o diz com todas as
# letras: *"as respostas sao montadas dos campos da tabela, nunca digitadas (...)
# a camada que a IA le e a camada que a pessoa le nao podem divergir"*, e essa
# regra esta CERTA. O que ninguem havia medido e que o campo e um PEDACO DE
# ORACAO que concorda com o sujeito de quem o usa: na tabela o sujeito e a
# linha (`bicicleta eletrica`, feminino) e na frase era `o veiculo` (masculino).
# A celula estava certa no lugar onde nasceu e errada no lugar onde foi colada.
#
# O CONSERTO E DA FRASE, NAO DO DADO: a frase passa a nomear a categoria de que
# ela fala, e com isso os dois sujeitos passam a ser o mesmo. Trocar o dado
# consertaria a frase e quebraria a tabela — que e o jeito de este defeito voltar
# pela outra ponta.
#
# O QUE A REGUA NAO ALCANCA, DITO AQUI PARA NAO APROVAR EM SILENCIO: ela conhece
# UMA familia de oracao (a de registro e placa, que e a afirmacao mais perigosa
# que esta ilha faz) e uma lista de sujeitos. Sujeito fora da lista nao reprova:
# vira linha de REGISTRO, porque regua que aprova o que nao reconheceu e pior
# que regua que nao roda.
# ---------------------------------------------------------------------------

# O SUJEITO E MEDIDO COM FRONTEIRA DE PALAVRA, e isto nao e zelo: escrito com
# `str.rfind`, este dicionario achou `ele` dentro de `acELErador` e dentro de
# `ELEtrica`, nas DUAS frases do mundo 20 — e, por achar o masculino mais perto
# do participio, APROVOU a frase doente e a consertada do mesmo jeito. E a
# 32.4-e, escrita nesta ilha nesta manha (*"palavra que vive dentro de outra nao
# pode ser medida por pedaco"*), repetida a tarde por quem a leu. A ordem da
# tupla continua importando: `a bicicleta eletrica` vem antes de `a bicicleta`
# porque as duas comecam no mesmo lugar e a mais longa e a que a frase diz.
SUJEITOS_COM_GENERO = (
    (r"\ba bicicleta eletrica\b", "a bicicleta eletrica", "f"),
    (r"\ba bicicleta\b", "a bicicleta", "f"),
    (r"\bo autopropelido\b", "o autopropelido", "m"),
    (r"\bo ciclomotor\b", "o ciclomotor", "m"),
    (r"\bo equipamento\b", "o equipamento", "m"),
    (r"\bo veiculo\b", "o veiculo", "m"),
    (r"\bela\b", "ela", "f"),
    (r"\bele\b", "ele", "m"),
)

_RE_PARTICIPIO_DE_SUJEICAO = re.compile(r"\bnao e (sujeit[oa])\b")


def problemas_de_concordancia_da_sujeicao(textos, onde):
    """`nao e sujeito/sujeita` concordando com o sujeito que a frase traz.

    Devolve `(problemas, sem_sujeito)`. O texto e lido DOBRADO, pela mesma razao
    da regua de fronteira da 32.4: `veículo` e `veiculo` sao a mesma palavra e
    nenhuma regua desta ilha deve depender de qual das duas chegou.
    """
    ruim = []
    sem_sujeito = []
    for texto in textos:
        dobrado = re.sub(r"\s+", " ", _sem_acento(texto).lower())
        for m in _RE_PARTICIPIO_DE_SUJEICAO.finditer(dobrado):
            participio = m.group(1)
            genero_dito = "f" if participio.endswith("a") else "m"
            antes = dobrado[max(0, m.start() - 70):m.start()]
            achado = None
            for padrao, sujeito, genero in SUJEITOS_COM_GENERO:
                encontrados = list(re.finditer(padrao, antes))
                if not encontrados:
                    continue
                pos = encontrados[-1].start()
                if achado is None or pos > achado[0]:
                    achado = (pos, sujeito, genero)
            if achado is None:
                sem_sujeito.append("%s: %r sem sujeito reconhecido em %r"
                                   % (onde, participio, texto[:120]))
                continue
            if achado[2] != genero_dito:
                ruim.append("%s: %r depois de %r — a celula da tabela da regra foi "
                            "colada numa frase cujo sujeito e de outro genero, e a "
                            "frase tem de nomear a categoria de que fala: %r"
                            % (onde, participio, achado[1], texto[:160]))

    return ruim, sem_sujeito


falhas = []
registros = []
afirmacoes = 0


def afirma(cond, msg):
    global afirmacoes
    afirmacoes += 1
    if not cond:
        falhas.append(msg)


def registro(msg):
    registros.append(msg)


class _SemSeguir(urllib.request.HTTPRedirectHandler):
    """NAO segue redirecionamento: devolve a resposta do 3xx como ela veio.

    NASCEU EM 09/11/2026, PELO ITEM 5 DO DESPACHO. `urllib.request.urlopen`
    segue 301 e 302 por padrao, e `buscar()` devolvia o codigo do FIM DA CADEIA.
    Com isso a afirmacao da 32.1-b — que manda *"montar a query com os valores
    que o navegador enviaria e exigir 200"* — media "chega em 200" onde a regra
    pede "responde 200", e aprovava 486 afirmacoes com o botao da ferramenta
    principal respondendo 301. Portao que relata o estado do fim da cadeia nao ve
    o que acontece no meio dela.
    """

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


_ABRIDOR_SEM_SEGUIR = urllib.request.build_opener(_SemSeguir)


def buscar(caminho, v=True, seguir=True):
    url = DOMINIO + caminho
    if v:
        url += ("&" if "?" in caminho else "?") + "v=" + str(int(__import__("time").time()))
    req = urllib.request.Request(url, headers={
        "User-Agent": "rodametria-conferir/1.0",
        "Accept-Encoding": "identity",
    })
    abrir = urllib.request.urlopen if seguir else _ABRIDOR_SEM_SEGUIR.open
    try:
        with abrir(req, timeout=40) as r:
            return r.status, r.headers.get("Content-Type", ""), r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        # COM `seguir=False` O 3xx CHEGA AQUI, e o `Location` entra no
        # `Content-Type` nao — entao ele vai no corpo, que e onde quem chama o
        # le. Sem isso o portao diria "301" e nao diria PARA ONDE.
        corpo = e.read().decode("utf-8", "replace")
        if not seguir and 300 <= e.code < 400:
            corpo = "LOCATION: %s\n%s" % (e.headers.get("Location", ""), corpo)
        return e.code, e.headers.get("Content-Type", ""), corpo
    except Exception as e:
        return 0, "", "ERRO: %s" % e


def normalizar_par_vazio(url):
    """A URL com todo `chave=` vazio reescrito como `chave`, que e o que o
    WordPress faz no `redirect_canonical`.

    MEDIDO DE FORA EM 09/11/2026, e a causa NAO e desta ilha: `?foo=` tambem
    devolve 301 para `?foo`, e `?rdm_mun=sao-paulo` devolve 200. Nao e colisao
    com query var do WordPress (a familia do `w=500` em 404, de 06/11) e nao e
    nome de campo: e canonicalizacao, e vale para QUALQUER parametro vazio, em
    qualquer pagina, em qualquer ilha com WordPress.

    E ELA NAO TEM CONSERTO DO LADO DO HTML: formulario `method="get"` com campo
    de texto opcional vazio faz o navegador enviar `chave=`, e nenhum atributo de
    HTML impede isso. Entao o conserto escolhido foi NOMEAR o salto — e nomear
    com precisao, nao com complacencia: o unico salto aceito e este, de uma perna
    so, e qualquer outro REPROVA.
    """
    partes = urllib.parse.urlsplit(url)
    if not partes.query:
        return url
    pares = []
    for pedaco in partes.query.split("&"):
        pares.append(pedaco[:-1] if pedaco.endswith("=") else pedaco)
    return urllib.parse.urlunsplit(
        (partes.scheme, partes.netloc, partes.path, "&".join(pares), partes.fragment))


def veredito_do_botao(url, codigo, destino):
    """O veredito do botao de um formulario: `ok`, ou a frase do que esta errado.

    FUNCAO PURA, para o `--autoteste` FABRICAR o mundo em vez de esperar que ele
    aconteca — a mesma razao escrita na `veredito_da_revisao_atrasada` desta
    ferramenta, pela 20.9.

    OS QUATRO VEREDITOS, E ELES NAO SAO O MESMO CONSERTO:
      - 200                                  -> `ok`
      - 3xx cujo destino e a MESMA URL com o par vazio normalizado -> `ok`,
        porque e a canonicalizacao do WordPress e nao ha HTML que a evite
      - 3xx para QUALQUER outro lugar         -> REPROVA, e e o caso perigoso:
        botao que leva a outra pagina, ou cadeia de dois saltos, ou destino em
        404 depois do salto
      - qualquer outro codigo                 -> REPROVA
    """
    if codigo == 200:
        return "ok"
    if 300 <= codigo < 400:
        esperado = normalizar_par_vazio(url)
        if destino and urllib.parse.urlsplit(destino).geturl() == urllib.parse.urlsplit(esperado).geturl():
            return "ok"
        return ("responde %s e o destino e `%s`, que NAO e a propria URL com o par vazio "
                "normalizado (esperava `%s`). Salto de botao para outro lugar nao e "
                "canonicalizacao: e botao que leva a pessoa a uma pagina que ela nao pediu"
                % (codigo, destino or "(sem Location)", esperado))
    return ("responde %s. O formulario e method=get e o JS e quem faz preventDefault, entao "
            "quem estiver sem JavaScript cai nisso. Nome de campo curto colide com query var "
            "do WordPress" % codigo)


def formularios_da_pagina(html):
    """Os formularios da pagina, como (acao, [(nome, valor), ...]).

    O valor de cada campo sai do HTML SERVIDO — a opcao `selected`, o radio
    `checked`, o `value` do input —, que e exatamente o que o navegador
    enviaria se alguem apertasse o botao sem tocar em nada. Campo sem valor
    legivel entra vazio, que tambem e o que o navegador manda.

    A funcao NAO tem lista de nomes de campo e nao pode ter: e justamente a
    lista escrita a mao que deixaria a afirmacao verde depois de uma troca de
    nome. Ela le o que a pagina serve.
    """
    saida = []
    for m in re.finditer(r"<form\b([^>]*)>(.*?)</form>", html, re.S | re.I):
        atributos, dentro = m.group(1), m.group(2)
        acao = re.search(r'action="([^"]*)"', atributos)
        campos = []
        # <select name=...> ... <option value=X selected>
        for sm in re.finditer(r"<select\b([^>]*)>(.*?)</select>", dentro, re.S | re.I):
            nome = re.search(r'name="([^"]+)"', sm.group(1))
            if not nome:
                continue
            sel = re.search(r'<option value="([^"]*)"[^>]*\bselected\b', sm.group(2), re.I)
            primeira = re.search(r'<option value="([^"]*)"', sm.group(2), re.I)
            valor = (sel or primeira)
            campos.append((nome.group(1), valor.group(1) if valor else ""))
        # <input>: radio/checkbox so entram quando marcados; os outros sempre
        vistos_radio = set()
        for im in re.finditer(r"<input\b([^>]*)>", dentro, re.I):
            at = im.group(1)
            nome = re.search(r'name="([^"]+)"', at)
            if not nome:
                continue
            tipo = (re.search(r'type="([^"]+)"', at) or [None, "text"])[1].lower()
            valor = re.search(r'value="([^"]*)"', at)
            if tipo in ("radio", "checkbox"):
                if re.search(r"\bchecked\b", at, re.I) and nome.group(1) not in vistos_radio:
                    vistos_radio.add(nome.group(1))
                    campos.append((nome.group(1), valor.group(1) if valor else "on"))
                continue
            if tipo in ("submit", "button", "image", "reset", "file"):
                continue
            campos.append((nome.group(1), valor.group(1) if valor else ""))
        saida.append((acao.group(1) if acao else "", campos))
    return saida


def corpo_da_pagina(html):
    """So o CORPO, nunca o HTML completo.

    A secao 8: "afirmacao sobre o que a pagina diz se mede no CORPO, nunca no
    HTML completo" — a trava que achava o texto dentro do proprio JSON-LD e
    passava ate com resposta inventada.
    """
    m = re.search(r"<body[^>]*>(.*)</body>", html, re.S | re.I)
    corpo = m.group(1) if m else html
    corpo = re.sub(r"<script.*?</script>", " ", corpo, flags=re.S | re.I)
    corpo = re.sub(r"<style.*?</style>", " ", corpo, flags=re.S | re.I)

    return corpo


# ---------------------------------------------------------------------------
# A 32.4 NO QUE A PAGINA SERVE, E NAO SO NO QUE O LEITOR VE (bloco 7, 04/11/2026)
#
# `corpo_da_pagina()` acima tira `<script>` e `<style>` antes de medir, e esta
# CERTO: ali mora CSS e JS, nao prosa, e a afirmacao sobre o que a pagina DIZ se
# mede no corpo. So que a 32.4 nao e sobre o que o leitor VE — e sobre o que a
# pagina SERVE, e e o fonte que a visao geral de IA ingere. Entre as duas
# leituras cabia o defeito medido no ar as 19h2xZ de 04/11/2026: as folhas desta
# ilha serviam 23 comentarios de CSS e 7.486 bytes na home e na F2, com tres
# mencoes a `conferir-32-5-no-navegador.mjs`, uma a `bancada` e varias a numero
# de secao do contrato.
#
# AS DUAS AFIRMACOES SAO SEPARADAS de proposito, porque o conserto de cada uma e
# diferente (20.5): uma diz que a FOLHA servida tem comentario; a outra diz que
# ha PALAVRA de bastidor no HTML servido. A primeira se conserta na casca, a
# segunda no texto que a produziu.
# ---------------------------------------------------------------------------

BASTIDOR = ["egresso", "SERP classificada", "snippet", "wp-sitemap", "manifest.json",
            "ARQUIPELAGO", "Rodametria Sync", "bancada", "dados/", "ferramentas/",
            "regras/", "sha256", "revisao",
            # O NOME DAS IRMAS, acrescentado em 11/11/2026: um comentario do
            # roteiro da home servia "a cicatriz que a clubedomosaico pagou em
            # 12/10/2026" em toda leitura. Nome de outra ilha do arquipelago na
            # pagina e bastidor da fabrica no sentido mais literal que existe —
            # e o visitante nao tem nem como saber do que se trata. MEDIDO em
            # zero fora dos nossos proprios comentarios, nas 10 URLs, antes de
            # entrar: `rodametria` ficaria de fora de qualquer jeito, porque e o
            # dominio e o prefixo de toda classe desta casca.
            "clubedomosaico", "aquametria", "robometria", "jornadafly", "ohmetria",
            # E as duas palavras do vocabulario da fabrica que estavam nos
            # mesmos comentarios: a ordem de servico e o nome que esta ilha da
            # ao modulo de regra.
            "despacho", "cerebro"]

# ---------------------------------------------------------------------------
# A MESMA 32.4, PARA O QUE SUBSTRING CRUA NAO CONSEGUE DIZER (itens 2 e 3 do
# despacho de 11/11/2026)
# ---------------------------------------------------------------------------
# A lista de cima casa pedaco de texto, em minuscula, e isso basta para
# `snippet` ou `manifest.json`. Duas classes de termo ela NAO alcanca, e as duas
# chegaram ao ar:
#
# (a) PALAVRA QUE VIVE DENTRO DE OUTRA. `ilha` esta dentro de `trilha`, e a
#     trilha de migalhas e exigida pela 16.3 em toda pagina desta ilha — 5 a 7
#     ocorrencias por URL, medidas. Um termo `ilha` de substring reprovaria as 10
#     paginas pelo que elas tem de CERTO, que e o caminho mais curto para alguem
#     passar a ignorar o portao (20.5). Entao a regua e de FRONTEIRA DE PALAVRA.
#
# (b) PALAVRA ACENTUADA NA TELA E SEM ACENTO NA LISTA. `publicavel` ESTAVA na
#     lista de cima desde que ela nasceu, e o que a F2 servia era `publicável`
#     — com acento. A lista nao pegou, a ronda de 11/11 pegou com os olhos. A
#     regua aqui DOBRA o acento dos dois lados antes de comparar, entao
#     `publicável`, `publicaveis` e `publicáveis` caem no mesmo termo.
#
# `ilha` E `ilhas` SAO O NOME QUE O CONTRATO DA A UM SITE DESTA FABRICA (a
# secao de vocabulario: "cada site de nicho e uma ilha"). A 32.4-d de 11/11 pos
# na lista o nome PROPRIO das irmas e deixou de pe o nome COMUM da coisa — e era
# o nome comum que aparecia 10 vezes, em prosa de leitor, em 5 das 10 paginas,
# dizendo ao visitante que ele esta dentro de uma peca de uma fabrica cujo nome
# o site nunca explica.
#
# `Tipo:` e ROTULO DE CAMPO DE BANCO impresso como texto de leitor. Medido em
# 11/11/2026: UMA ocorrencia nas 10 URLs, a nossa, na lista de reguas da F2 —
# `Tipo: pendente, sem valor publicado`, onde `pendente` e valor do enum de
# `status` do esquema. Nenhuma pagina do WordPress serve `tipo:`, e isso foi
# contado antes de o termo entrar, nao suposto.
BASTIDOR_COM_FRONTEIRA = [
    (r"\bilhas?\b",
     "`ilha`/`ilhas` — e o nome que esta fabrica da a um site dela, e o visitante "
     "nao tem como saber do que se trata; na tela ele se diz `este site`"),
    (r"publicav\w*",
     "`publicavel` e familia — e valor do enum de `status` do banco, nao palavra "
     "de leitor"),
    (r"tipo:",
     "`Tipo:` — rotulo de campo de banco impresso como se fosse frase de leitor"),
]


def _sem_acento(texto):
    return "".join(c for c in unicodedata.normalize("NFKD", texto)
                   if not unicodedata.combining(c))


def problemas_de_bastidor_com_fronteira(texto, onde):
    """Os termos da 32.4 que pedem fronteira de palavra ou acento dobrado.

    `texto` e lido DOBRADO (sem acento, em minuscula) e os padroes sao escritos
    sem acento, entao `publicável` e `publicavel` sao o mesmo termo. Devolve uma
    linha por termo, com a contagem e o motivo — a linha diz o CONSERTO, nunca so
    o veredito.
    """
    ruim = []
    dobrado = _sem_acento(texto).lower()
    for padrao, motivo in BASTIDOR_COM_FRONTEIRA:
        achados = re.findall(padrao, dobrado)
        if achados:
            ruim.append("32.4 em %s: %s — %d ocorrencia(s)" % (onde, motivo, len(achados)))

    return ruim


# Extensao de rotina desta fabrica. `.php` NAO entra, e a causa foi MEDIDA em
# 04/11/2026: o WordPress serve `/wp-*.php` e `xmlrpc.php` no proprio `<head>`,
# em duas ocorrencias por pagina, e um termo `.php` reprovaria a pagina certa —
# que e o caminho mais curto para alguem passar a ignorar o portao (20.5).
# `.py` e `.mjs` foram medidos em ZERO fora das nossas folhas nas mesmas 9 URLs.
EXTENSOES_DE_ROTINA = [".py", ".mjs"]


def folhas_da_ilha(html):
    """So as folhas que ESTA ilha escreve, nunca as do WordPress.

    Medido em 04/11/2026 na pagina da F2: 18 blocos `<style>`, dos quais 17 sao
    do proprio WordPress — one-liners de 41 a 103 bytes, 1.254 bytes de
    comentario no total, que nao sao desta ilha e nao saem daqui. O nosso e 1
    bloco com 23 comentarios e 7.486 bytes: 85,6% dos bytes de comentario da
    pagina. Reprovar pelos 17 do WordPress seria reprovar o que esta ilha nao
    pode consertar.
    """
    nossas = []
    for atrib, css in re.findall(r"<style([^>]*)>(.*?)</style>", html, re.S | re.I):
        if "rodametria" in atrib or "rdm-" in atrib:
            m = re.search(r'id="([^"]+)"', atrib)
            nossas.append((m.group(1) if m else "(sem id)", css))

    return nossas


def problemas_da_folha_servida(html):
    """Comentario de CSS dentro de folha DESTA ilha. Funcao pura, sem rede."""
    ruim = []
    for ident, css in folhas_da_ilha(html):
        quantos = len(re.findall(r"/\*", css))
        if quantos:
            bytes_ = sum(len(m) for m in re.findall(r"/\*.*?\*/", css, re.S))
            ruim.append("a folha %s serve %d comentario(s) de CSS (%d bytes) — o comentario "
                        "mora no repositorio (secao 3), nunca na folha impressa"
                        % (ident, quantos, bytes_))

    return ruim


def roteiros_da_ilha(html):
    """So os roteiros que ESTA ilha escreve, nunca os do WordPress.

    Medido em 11/11/2026 nas 10 URLs: os quatro blocos desta ilha sao os de
    `id="rodametria-*-js"`; o WordPress serve mais dois (`wp-importmap` e o
    modulo de navegacao do tema) e um sem `id`, e nenhum deles e nosso nem sai
    daqui. O `application/ld+json` fica FORA de proposito: ele serve dado
    estruturado, nao codigo, e nao tem comentario para esconder.
    """
    nossos = []
    for atrib, js in re.findall(r"<script([^>]*)>(.*?)</script>", html, re.S | re.I):
        if "ld+json" in atrib.lower():
            continue
        m = re.search(r'id="(rodametria-[^"]+)"', atrib)
        if m:
            nossos.append((m.group(1), js))

    return nossos


# A REGUA QUE CONTA — A DE DENTRO DA CASCA DECIDE O QUE APAGAR (secao 8)
#
# Ela tira os literais (aspa simples, dupla e template) e conta o comentario no
# que sobra. NAO e a funcao da casca reescrita em Python: aquela decide o que
# REMOVER e esta decide o que CONTAR, e e por as duas serem independentes que
# uma pode reprovar a outra. O que ela nao enxerga e expressao regular com `//`
# ou `/*` dentro — medido em ZERO nos quatro roteiros, e o portao do chao
# (`teste-roteiro-sem-comentario.php`) tem a afirmacao que fica vermelha no dia
# em que deixar de ser zero.
_SEM_LITERAL = (
    re.compile(r'"(?:\\.|[^"\\])*"', re.S),
    re.compile(r"'(?:\\.|[^'\\])*'", re.S),
    re.compile(r"`(?:\\.|[^`\\])*`", re.S),
)


def problemas_do_roteiro_servido(html):
    """Comentario de JavaScript dentro de roteiro DESTA ilha. Sem rede.

    O DEFEITO, medido no ar as 13h2xZ de 11/11/2026 nas 10 URLs: os quatro
    roteiros desta ilha serviam 14 comentarios e 3.489 bytes, seis deles com o
    vocabulario que a 32.4 proibe. A 32.4-b de 04/11 tirou o comentario da
    FOLHA e deixou o do ROTEIRO — mesma pagina, metade do lado.
    """
    ruim = []
    for ident, js in roteiros_da_ilha(html):
        cru = js
        for padrao in _SEM_LITERAL:
            cru = padrao.sub('""', cru)
        blocos = len(re.findall(r"/\*", cru))
        linhas = len(re.findall(r"//", cru))
        if blocos or linhas:
            bytes_ = sum(len(m) for m in re.findall(r"/\*.*?\*/", js, re.S))
            ruim.append("o roteiro %s serve %d comentario(s) de bloco (%d bytes) e %d de "
                        "linha — o comentario mora no repositorio (secao 3), nunca no "
                        "roteiro impresso" % (ident, blocos, bytes_, linhas))

    return ruim


def problemas_de_bastidor_no_servido(html, nomes_de_arquivo=()):
    """A 32.4 sobre o HTML SERVIDO INTEIRO, e a afirmacao e POSITIVA.

    Nao procura "a falha que alguem ja imaginou" num pedaco escolhido: varre o
    byte servido. Medido em 04/11/2026 nas 9 URLs, a UNICA palavra da lista que
    aparecia no HTML inteiro era `bancada`, uma vez, DENTRO da nossa folha —
    entao esta regua nao reprova o WordPress por acidente, e isso foi medido
    antes de ela nascer, nao suposto.
    """
    ruim = []
    baixo = html.lower()
    for termo in BASTIDOR:
        if termo.lower() in baixo:
            ruim.append("32.4 no HTML servido: a palavra de bastidor %r aparece %d vez(es) — "
                        "invisivel para o visitante e legivel para quem le o fonte, que e o "
                        "que a visao geral de IA ingere" % (termo, baixo.count(termo.lower())))
    for ext in EXTENSOES_DE_ROTINA:
        if ext in baixo:
            ruim.append("32.4 no HTML servido: a extensao de rotina %r aparece %d vez(es) — "
                        "nome de arquivo desta fabrica nao e coisa que a pagina sirva"
                        % (ext, baixo.count(ext)))
    for nome in nomes_de_arquivo:
        if nome.lower() in baixo:
            ruim.append("32.4 no HTML servido: o nome de arquivo %r desta pasta aparece na "
                        "pagina" % nome)

    return ruim

REV_RE = re.compile(r"revis\w*\s+(\d+)\s*:")

# A LINHA DA CURA DA PORTA (29.4), que mora no MESMO log do desembarque e NAO e
# item dele. O nome e escrito pela casca em `rodametria_casca_cura_registrar()`;
# a forma e a que a 29.4 exige — o antes e o depois em bytes E em blocos.
CURA_RE = re.compile(r"cura da porta\s*:")
CURA_FORMA_RE = re.compile(
    r"cura da porta:.*?(\d+)\s*bytes\s*\[([^\]]*)\]\s*->\s*(\d+)\s*bytes\s*\[([^\]]*)\]")



# O EVENTO DO CRON DO SYNC E RECORRENTE DE 1.800 SEGUNDOS, e isto nao e palpite:
# esta na fonte do Sync, que mora no repositorio — `$s['<ilha>_30min'] = array(
# 'interval' => 1800, ... )`, agendado por `wp_schedule_event( time() + 120, ... )`
# (linhas 530 e 536 de ilhas/robometria/snippets/robometria-sync.php; o mesmo
# codigo nas quatro ilhas). O WP-Cron so dispara evento DEVIDO.
INTERVALO_DO_CRON_S = 1800


def veredito_da_revisao_atrasada(ultimo, agora, commit_do_manifest, raw_ja_serve,
                                 intervalo=INTERVALO_DO_CRON_S):
    """Por que a revisao do /status esta atras da do manifest — em QUATRO casos.

    E FUNCAO PURA DE PROPOSITO, como `rotas_do_indice` e `diagnostico_da_porta`,
    e e isso que faz o `--autoteste` fabricar o mundo em vez de esperar que ele
    aconteca.

    MEDIDO EM 05/11/2026 as 19h1xZ–19h3xZ, e o custo foi OITO MINUTOS e TRES
    rodadas de uma execucao da ilha em FOCO TOTAL, gastos reacionando um Sync que
    estava saudavel. A regua que existia aqui era de DUAS pontas e vinha da 20.5:
    "log recente significa CACHE do GitHub (reacione de dois em dois) e log antigo
    significa que o Sync NAO RODOU". Ela erra por DOIS motivos, e os dois estao
    conferidos na fonte do Sync:

      (a) ELA CHAMA `ultimo` DE "LOG", E OS DOIS NAO SAO A MESMA COISA. Na rodada
          em que nao ha nada a aplicar, o Sync grava `ultimo` e RETORNA ANTES de
          escrever linha de log — `if ( ! $forcar && (int) $m['revisao'] === (int)
          $estado['revisao'] ) { $estado['ultimo'] = current_time( 'mysql' ); ...
          return $estado; // nada novo }`, linhas 473 a 477. A linha de log nasce
          na 518, DEPOIS de aplicar. Logo: `ultimo` diz se o Sync RODOU; o log diz
          quando ele APLICOU. Log parado com `ultimo` de agora e um Sync saudavel
          que nao tinha trabalho — nao e canal morto.

      (b) ELA NAO TEM O CASO DO EVENTO NAO VENCIDO, QUE E O CASO COMUM. Push feito
          logo DEPOIS de uma rodada espera o proximo vencimento, e reacionar NAO
          antecipa vencimento — o WP-Cron dispara evento devido, e o evento e de
          30 minutos. A 20.6 diz "roda por visita, nao por relogio", o que esta
          certo contra a leitura de que haveria um relogio no servidor, mas lido
          sozinho sugere que VISITAR BASTA. Nao basta. A receita inteira e "roda
          por visita E quando devido".

    OS QUATRO VEREDITOS, e cada um tem conserto DIFERENTE (e por isso a 20.5 manda
    separa-los: portao que reprova a coisa certa pelo motivo errado e o caminho
    mais curto para alguem ignora-lo):

      `relogio-divergente` — `ultimo` NO FUTURO em relacao a quem mede. So o futuro
          e inequivoco: Sync que nao roda nao grava hora que ainda nao chegou, entao
          isto e relogio e nao canal morto. `ultimo` ATRASADO e ambiguo POR DESENHO
          — um Sync morto e um site em UTC-3 dao a MESMA leitura numa amostra so —, e
          esta funcao nao adivinha: devolve `sync-morto` e DIZ a ambiguidade na frase.
          (Medido em 05/11: o relogio deste site bate com UTC — `ultimo` 19:16:46
          contra 19:16Z de quem mediu.)
      `sync-morto` — `ultimo` ausente, ou mais velho que o intervalo com folga: o
          evento nao esta disparando. E defeito de verdade, e e o unico dos quatro
          que e.
      `raw-atrasado` — o Sync esta vivo e o `raw.githubusercontent.com` ainda nao
          serve a revisao nova. Nao e do site: nao ha o que reacionar.
      `evento-nao-vencido` — o Sync esta vivo e a ultima rodada dele e ANTERIOR ao
          commit do manifest: naquela rodada nao havia nada a aplicar. REACIONAR NAO
          ANTECIPA. E `ultimo + intervalo` e TETO e nao hora exata: o WordPress
          reagenda evento recorrente a partir do horario AGENDADO, nao do horario em
          que ele rodou, entao uma rodada ATRASADA e seguida por um vencimento mais
          CEDO do que a conta ingenua diz. MEDIDO em 05/11/2026 nesta ilha, e a
          medicao FALSIFICOU a primeira versao desta propria frase, escrita minutos
          antes: rodada as 19:16:46, teto 19:46:46, revisao entrando as 19:40:09 —
          porque o agendamento era de 19:10:09. O horario exato nao sai do `/status`.
      `cache` — o Sync rodou DEPOIS do commit e ainda nao pegou a revisao: e o
          cache do GitHub da 20.5. Reacione de dois em dois.

    Devolve `(codigo, frase)`. Nenhum dos quatro e aprovacao: a revisao atrasada
    continua sendo falha. O que muda e O QUE A PROXIMA PESSOA FAZ.
    """
    if ultimo is None:
        return ("sync-morto", "o /status nao traz `ultimo`: o Sync nunca rodou neste site, "
                              "ou a rodada nao chegou a gravar estado. E defeito de verdade.")

    # SO O FUTURO E INEQUIVOCO. `ultimo` ADIANTADO nao pode ser Sync morto — Sync
    # que nao roda nao grava hora que ainda nao chegou —, entao e relogio. Ja
    # `ultimo` ATRASADO e ambiguo por desenho: um Sync morto e um site em UTC-3
    # produzem a MESMA leitura numa amostra so, e nao ha como separa-los daqui.
    # Esta funcao NAO adivinha: chama de `sync-morto` e DIZ a ambiguidade na
    # frase, para quem ler conferir o fuso em vez de confiar no veredito.
    deriva = (ultimo - agora).total_seconds()
    if deriva > 600:
        return ("relogio-divergente",
                "`ultimo` (%s) esta %d minuto(s) NO FUTURO em relacao a hora de quem mediu (%s). "
                "Sync que nao roda nao grava hora que ainda nao chegou, entao isto nao e Sync "
                "morto: e relogio. `ultimo` vem de `current_time('mysql')`, a hora LOCAL do site. "
                "Este portao DENUNCIA em vez de escolher veredito."
                % (ultimo.strftime("%Y-%m-%d %H:%M:%S"), round(deriva / 60.0),
                   agora.strftime("%Y-%m-%d %H:%M:%S")))

    idade = -deriva
    if idade > intervalo + 600:
        return ("sync-morto",
                "a ultima rodada do Sync (`ultimo` = %s) foi ha %d minuto(s), e o evento e de %d "
                "minuto(s). Passou do vencimento com folga e nao rodou: o evento nao esta "
                "disparando. E defeito de verdade, e o unico dos vereditos que e. E A RESSALVA, "
                "porque ela nao cabe em palpite: `ultimo` e hora LOCAL do site, e um site atrasado "
                "em relacao a quem mede produz esta MESMA leitura. Antes de abrir chamado, confira "
                "o fuso do site — neste site ele foi MEDIDO batendo com UTC em 05/11/2026 "
                "(`ultimo` 19:16:46 contra 19:16Z de quem mediu)."
                % (ultimo.strftime("%Y-%m-%d %H:%M:%S"), round(idade / 60.0), intervalo // 60))

    if not raw_ja_serve:
        return ("raw-atrasado",
                "o Sync esta VIVO (rodou ha %d minuto(s)) e o `raw.githubusercontent.com` ainda nao "
                "serve a revisao nova. Nao e defeito do site e nao ha o que reacionar: espere o raw."
                % round(idade / 60.0))

    if commit_do_manifest is not None and ultimo < commit_do_manifest:
        teto = (ultimo + timedelta(seconds=intervalo))
        return ("evento-nao-vencido",
                "o Sync esta VIVO e a ultima rodada dele (%s) e ANTERIOR ao commit do manifest "
                "(%s): naquela rodada nao havia nada a aplicar, e por isso o log tambem nao ganhou "
                "linha. REACIONAR NAO ANTECIPA VENCIMENTO — o WP-Cron dispara evento DEVIDO (20.6: "
                "roda por visita E quando devido). O proximo vencimento cai em %s NO MAIS TARDE, e "
                "PODE CAIR ANTES: o WordPress reagenda evento recorrente a partir do horario "
                "AGENDADO e nao do horario em que ele rodou, entao `ultimo` + %d min e TETO e nunca "
                "a hora exata. (Medido nesta ilha em 05/11/2026: rodada atrasada as 19:16:46, teto "
                "calculado 19:46:46, e a revisao entrou as 19:40:09 — 6m37s ANTES do teto, porque o "
                "agendamento era de 19:10:09. O horario exato nao sai do `/status`: sairia de "
                "`wp_next_scheduled`, que nenhuma rota publica serve.)"
                % (ultimo.strftime("%H:%M:%S"), commit_do_manifest.strftime("%H:%M:%S"),
                   teto.strftime("%H:%M:%S"), intervalo // 60))

    return ("cache",
            "o Sync rodou %s, DEPOIS do commit do manifest (%s), e ainda nao pegou a revisao nova: "
            "e o cache do GitHub da 20.5. Reacione de dois em dois, com alguns minutos entre as "
            "rodadas; se nao subir em ~10 minutos, ai sim e defeito."
            % (ultimo.strftime("%H:%M:%S"),
               commit_do_manifest.strftime("%H:%M:%S") if commit_do_manifest else "desconhecido"))


def linhas_da_revisao(log, n):
    """Devolve (linha de FECHO da revisao n, [linhas de ITEM dela]).

    O LOG VEM DO MAIS NOVO PARA O MAIS VELHO, E A LINHA DE FECHO E ESCRITA POR
    ULTIMO — entao ela aparece ANTES dos itens que resume. A primeira versao
    desta regua supunha o contrario, com estas palavras no comentario: "cada
    revisao COMECA com a linha `revisao N:`. As linhas desta entrega sao as que
    vao do topo ate essa linha, inclusive." Com o fecho no topo, esse corte
    devolvia UMA linha — a de fecho — e o portao imprimia "1 da revisao 29, 0
    linha de falha nesta entrega".

    MEDIDO EM 02/11/2026 as 17h4xZ, no desembarque da revisao 29: o log tinha 15
    linhas, a revisao 29 tinha 1 linha de fecho e 8 de item, e o portao leu 1.
    As 8 linhas de item NUNCA foram lidas por ele — e linha de item e justamente
    onde mora `gravado (#13) mas NAO ativado`, o defeito que a 20.4 existe para
    pegar e que custou SETE paginas na clubedomosaico duas vezes em tres dias.

    E A IRONIA E EXATA: a 20.4 diz "a revisao do /status E O RESUMO, E RESUMO
    VERDE NAO E ENTREGA". O portao escrito para cobrar isso estava lendo SO O
    RESUMO, e dizia "lido linha por linha" ao fazer isso. As execucoes de 30/10
    e das 14h14Z de hoje escreveram "as 7 linhas" e "as 5 linhas da revisao
    corrente dizendo ok" — numeros que saiam de leitura A MAO, nao deste portao,
    que nas duas vezes tinha lido 1.
    """
    inicio = None
    for k, l in enumerate(log):
        m = REV_RE.search(l)
        if m and int(m.group(1)) == n:
            inicio = k
            break
    if inicio is None:
        return None, []
    itens = []
    for l in log[inicio + 1:]:
        if REV_RE.search(l):
            break
        itens.append(l)
    return log[inicio], itens


def aplicados_declarados(fecho):
    """Quantos itens a LINHA DE FECHO diz ter aplicado, ou None.

    E a regua que fecha o buraco de verdade: o fecho declara um numero, e o
    portao conta as linhas que leu. Se a janela do log rolou e levou itens, a
    conta nao fecha e o portao DIZ isso, em vez de aprovar com cara de completo
    sobre as linhas que sobraram.
    """
    m = re.search(r"(\d+)\s+aplicado", fecho or "")
    return int(m.group(1)) if m else None


ROTA_DA_293 = "/rodametria/v1/rotas"

# A LISTA DA 29.2 MORA NUMA CONSTANTE porque o diagnostico da porta a conta.
PORTAS_DA_292 = (
    ("/robots.txt", "text/plain"),
    ("/wp-sitemap.xml", "xml"),
    ("/wp-json/", "application/json"),
)


def rest(rota):
    """A rota REST pela porta QUE NAO CAI, e nunca pelo caminho bonito.

    MEDIDO NESTA ILHA EM 05/11/2026, as 10h2xZ, e o defeito era DESTE ARQUIVO.
    A porta de entrada caiu (o bloco `# BEGIN WordPress` fora do `.htaccess` da
    raiz, a assinatura da 29 pela QUINTA vez no Arquipelago) e este portao, que
    existe para medir isso, fez duas coisas erradas por ler o REST pelo caminho
    bonito:

      (1) ACUSOU A CASCA DE UM DEFEITO QUE ELA NAO TEM. O indice de rotas era
          lido em `/wp-json/rodametria/v1` — que e caminho bonito, portanto
          morto junto com a porta. O `json.loads` falhava sobre a pagina 404 do
          hospedeiro, `rotas_no_indice` vinha VAZIA, e a saida dizia "esta casca
          nao registra a rota que mede a porta de entrada por dentro". A rota
          ESTAVA registrada: `?rest_route=/rodametria/v1/rotas` respondia 200 na
          mesma passada, e a casca a servia desde 03/11. Quem lesse aquela linha
          iria procurar registro de rota na casca — o conserto errado, no arquivo
          errado, com a porta de entrada do site no chao.

      (2) PAROU DE MEDIR O RESTO. O `/status` era lido pelo caminho bonito, e
          `main()` devolve `encerrar()` quando ele nao da 200: a leitura inteira
          encolheu de 481 afirmacoes (04/11, de tarde) para NOVE. Tudo o que este
          portao sabe sobre conteudo, voz, 32.4 e 32.5 deixou de ser medido
          exatamente no dia em que a ilha mais precisava ser medida.

    E A 29.1 COM UM ANDAR A MAIS, e por isso esta aqui e nao so no registro do
    dia: a 29.1 diz que nenhum portao viu a porta cair porque todos entravam
    pela porta que continuou aberta. Este portao, escrito para ver, entrava pela
    porta que CAI — e por isso ele viu, e culpou a casca.

    O QUE ESTA TROCA NAO AFROUXA, porque afrouxar portao por conveniencia seria
    o conserto virar o defeito seguinte: `/wp-json/` em 200 com
    `application/json` continua sendo afirmacao da 29.2, inteira, logo acima.
    A porta segue cobrada pela afirmacao que existe para cobra-la; o que muda e
    que as OUTRAS afirmacoes param de depender dela. E a 20.5 ao pe da letra —
    portao que reprova pelo motivo errado e o caminho mais curto para alguem
    passar a ignora-lo.
    """
    return "?rest_route=" + rota


def rotas_do_indice(bruto):
    """As rotas que o indice REST declara, ou LISTA VAZIA se nao for JSON.

    Separada de `main()` de proposito, para o `--autoteste` poder dar a ela a
    pagina 404 do hospedeiro e medir o que a regua velha concluia dela.
    """
    try:
        d = json.loads(bruto)
    except Exception:
        return []
    if not isinstance(d, dict):
        return []

    return sorted((d.get("routes") or {}).keys())


def diagnostico_da_porta(cod_home, cods_das_portas, rest_vivo):
    """A ASSINATURA DA 29, NOMEADA — ou None quando ela nao esta na mesa.

    Cinco vezes no Arquipelago com a mesma cara: clubedomosaico em 24/09, 05/10
    e 08/10, robometria em 30/10 e esta ilha em 05/11. Sempre as mesmas quatro
    grandezas juntas: a HOME em 200, as TRES portas da 29.2 em 404, o REST VIVO
    por `?rest_route=` e o caminho bonito morto. O que isso quer dizer tem nome
    e tem conserto, e os dois estao na 29: o bloco `# BEGIN WordPress` saiu do
    `.htaccess` da raiz, e o conserto e o `flush_rewrite_rules( true )` da 29.3.

    POR QUE O PORTAO DIZ A CAUSA E NAO SO OS SINTOMAS: sem esta linha a leitura
    sai como seis ou oito reprovacoes espalhadas, cada uma verdadeira e nenhuma
    dizendo o que fazer, e a de 05/11 ainda saia com uma SETIMA acusando a
    casca. Causa medida cinco vezes e com conserto escrito nao e palpite: e o
    que separa "a ilha esta vermelha" de "a porta caiu, e o conserto e este".

    O QUE ELA NAO AFIRMA, e e por isso que ela cobra as quatro grandezas
    juntas: se a home TAMBEM estiver morta, ou se o REST estiver morto nas duas
    formas, nao e esta a causa — e esta funcao devolve None em vez de nomear a
    errada. Causa inventada e a proxima execucao consertando a coisa errada
    (29.5).
    """
    if cod_home != 200 or not rest_vivo:
        return None
    if not cods_das_portas or any(c == 200 for c in cods_das_portas):
        return None

    return ("29: A PORTA DE ENTRADA CAIU, e a assinatura e a conhecida — home em 200, "
            "as %d portas da 29.2 em %s, e o REST VIVO por `?rest_route=`. O WordPress "
            "esta de pe e o Apache parou de lhe mandar caminho bonito: e o bloco "
            "`# BEGIN WordPress` fora do `.htaccess` da raiz. CONSERTO: o "
            "`flush_rewrite_rules( true )` da 29.3 — `?rest_route=/rodametria/v1/rotas"
            "&token=<token do Sync>&reparar=1`, ou Salvar em Configuracoes > Links "
            "permanentes no wp-admin. O token desta ilha nao esta no REPOSITORIO; "
            "pela 29.3-a isso NAO significa que o reparo nao e exercitavel daqui — "
            "esta linha afirmava o contrario e foi corrigida em 12/11/2026, depois "
            "de a Sentinela reparar duas ilhas desta nuvem em 11/11 as 17h54Z e de "
            "a Fundacao reparar a clubedomosaico em 12/11 as 10h18Z. TENTE antes de "
            "escrever que nao da: causa de impossibilidade envelhece. E pela "
            "excecao da 29.4 (a cura da porta) a casca da ilha que a tiver repoe o "
            "bloco sozinha na primeira requisicao, sem token nenhum — esta ilha "
            "ainda NAO a tem (nona ocorrencia no Arquipelago: clubedomosaico 24/09, "
            "05/10, 08/10, 11/11 manha, 11/11 noite e 12/11; robometria 30/10 e "
            "11/11; rodametria 05/11)"
            % (len(cods_das_portas), "/".join(str(c) for c in cods_das_portas)))


def codigo_do_erro(bruto):
    """O campo `code` do JSON de erro do WordPress, ou None se nao for um."""
    try:
        d = json.loads(bruto)
    except Exception:
        return None

    return d.get("code") if isinstance(d, dict) else None


def problemas_da_parede(rotas_no_indice, cod_sem_token, cod_token_errado, code_errado):
    """A rota da 29.3 lida DE FORA, sem nunca ter o token.

    E FUNCAO PURA DE PROPOSITO, e e isso que faz o `--autoteste` poder fabricar
    os tres mundos que esta nuvem nao consegue produzir de verdade: a rota
    AUSENTE, a parede ABERTA e o PORTAO MORTO. Portao de rede cujo autoteste
    precisa de rede nao roda (20.8).

    A AFIRMACAO FORTE E A DO `code`, e ela e POSITIVA. Procurar "nao deu 200" e
    a leitura pelo avesso que a 20.8 nomeia: ela aprova um 404 e aprova uma
    casca que nega TODO pedido porque nao acha o token. O que prova que a
    parede esta VIVA e `rodametria_rotas_token_invalido` — esse codigo so sai
    depois de a casca achar a fonte do token E rodar o `hash_equals`. Ele e
    legivel sem o token, e e por isso que esta ilha o tem (ver a divergencia
    (b) da secao 12 da casca: o Sync dela nao esta no repositorio, entao o nome
    da fonte do token foi herdado e nao conferido no chao).
    """
    p = []

    if ROTA_DA_293 not in rotas_no_indice:
        p.append("29.3: %s NAO aparece no indice de rotas do WordPress — esta casca nao registra a rota que mede a porta de entrada por dentro"
                 % ROTA_DA_293)

    if 404 in (cod_sem_token, cod_token_errado):
        p.append("29.3: a rota respondeu 404 — ela nao existe neste site, e a porta de entrada segue sem instrumento (foi essa falta que custou QUATRO DIAS de ar na robometria)")

    if 200 in (cod_sem_token, cod_token_errado):
        p.append("29.3: A PAREDE ESTA ABERTA — a rota devolveu 200 SEM o token do Sync, e ela mostra o retrato do roteamento do servidor")

    if code_errado == "rodametria_rotas_sem_fonte_de_token":
        p.append("29.3: PORTAO MORTO — a casca nao achou de onde ler o token do Sync, entao a rota nega TODO pedido, inclusive o certo. O nome da funcao ou da option do token esta errado nesta ilha")
    elif code_errado != "rodametria_rotas_token_invalido":
        p.append("29.3: com token ERRADO a rota devia dizer `rodametria_rotas_token_invalido` e disse %r — sem esse codigo nao existe prova, desta nuvem, de que a parede achou a fonte do token e comparou"
                 % (code_errado,))

    if cod_token_errado != 401:
        p.append("29.3: com token errado a rota respondeu %s e tinha de responder 401 — o `status` vai EXPLICITO no WP_Error porque sem ele o WordPress devolve 500"
                 % (cod_token_errado,))

    return p


# ---------------------------------------------------------------------------
# A CLASSE DO QUANTIFICADOR E DO SUPERLATIVO, VARRIDA NO SITE INTEIRO — 04/11/2026
#
# POR QUE ELA ESTA NESTE PORTAO E NAO NOS OUTROS DOIS. A classe nasceu em
# 03/11/2026 nomeando UMA FRASE dentro do laco das paginas FILHAS de produto; na
# manha de 04/11 ela virou CLASSE, e entrou nas DUAS camadas declaradas que
# tinham portao (produto e institucional), cada uma com a propria lista de termos
# e a propria lista de liberacao. Na mesma tarde a varredura do site inteiro
# achou a MESMA classe numa TERCEIRA pagina, que nenhuma das duas podia ver:
#
#   /autonomia-patinete-eletrico/  ->  "E a lacuna MAIS COMUM do varejo"
#
# A prosa da F2 vive dentro de `snippets/rodametria-f2.php`. O cabecalho do
# portao de produto JA DIZIA, escrito antes deste dia, que existe *"um mundo
# entre os dois — prosa escrita direto no PHP, que a camada declarada nao ve"* —
# e a frase estava no ar desde 29/10 afirmando um ranqueamento que esta ilha
# nunca mediu.
#
# ENTAO O CONSERTO NAO E UM PORTAO POR CAMADA: E UM PORTAO POR SITE. Este laco
# varre TODA URL do sitemap e nao sabe de camada nenhuma — camada nova de pagina
# nasce JA coberta, que e o contrario do que aconteceu tres vezes em tres dias.
# As liberacoes continuam sendo por escrito, e ele le as TRES listas declaradas,
# porque a liberacao e da frase e nao do portao que a encontrou.
QUANTIFICADORES = (
    "quase nunca", "quase sempre", "quase todo", "quase toda", "quase todos",
    "quase todas", "quase ninguem", "quase nenhum", "quase nenhuma", "a maioria",
    "maioria", "a minoria", "minoria", "raramente", "costuma", "costumam",
    "na maior parte", "a maior parte", "maior parte", "boa parte", "grande parte",
    "geralmente", "normalmente", "em geral", "de modo geral", "via de regra",
    "tipicamente", "frequentemente", "na pratica", "poucos", "poucas", "muitos",
    "muitas",
    # O SUPERLATIVO DE FREQUENCIA E DE VENDA: nao e quantificador, e foi por isso
    # que as duas travas de ontem e de hoje de manha aprovaram as tres frases.
    "mais comum", "mais comuns", "mais vendido", "mais vendida",
    "mais vendidos", "mais vendidas", "vende mais", "vendem mais",
    "mais popular", "mais populares", "a media", "na media", "da media",
)

AS_TRES_CAMADAS_DECLARADAS = (
    "paginas-de-produto.json",
    "paginas-institucionais.json",
    # A TERCEIRA nasceu com este laco, para a camada cuja prosa vive no PHP e
    # que por isso nao tem camada declarada onde liberar.
    "liberacoes-de-quantificador.json",
)


def _sem_acento_q(t):
    import unicodedata
    t = unicodedata.normalize("NFD", str(t or "").lower())
    return "".join(c for c in t if unicodedata.category(c) != "Mn")


def ancoras_liberadas_do_site():
    """As ancoras LITERAIS das tres camadas declaradas, juntas.

    A liberacao e da FRASE, nao do portao que a encontrou: frase liberada na
    camada de produto nao pode ser denunciada aqui so porque este laco a achou
    por outro caminho. E ancora ausente no ar e cobrada pelo portao DAQUELA
    camada, que e quem sabe em que pagina ela devia estar.
    """
    ancoras = set()
    for nome in AS_TRES_CAMADAS_DECLARADAS:
        caminho = os.path.join(ILHA, "dados", nome)
        if not os.path.exists(caminho):
            continue
        with open(caminho, encoding="utf-8") as f:
            d = json.load(f)
        for q in d.get("quantificadores_declarados_permitidos") or []:
            a = (q.get("ancora_no_ar") or "").strip()
            if a:
                ancoras.add(_sem_acento_q(a))

    return tuple(sorted(ancoras))


def conferir_classe_no_site(caminho, texto, ancoras):
    """Denuncia a ocorrencia; nunca julga a prosa (20.5)."""
    t = _sem_acento_q(texto)
    for anc in ancoras:
        t = t.replace(anc, " ")
    for q in QUANTIFICADORES:
        i = t.find(q)
        while i >= 0:
            antes = t[i - 1] if i else " "
            depois = t[i + len(q):i + len(q) + 1] or " "
            if not (antes.isalpha() or depois.isalpha()):
                afirma(False,
                       "%s serve uma PROPORCAO ou um SUPERLATIVO por extenso (%r) que nao "
                       "esta liberado em camada declarada nenhuma: %r — e a classe que "
                       "chegou ao ar por TRES camadas em TRES dias, e este laco e o unico "
                       "que varre o site inteiro"
                       % (caminho, q, texto[max(0, i - 60):i + 80]))
                return
            i = t.find(q, i + 1)
    afirma(True, "")


def main():
    manifest = json.load(open(os.path.join(ILHA, "manifest.json"), encoding="utf-8"))
    revisao_esperada = int(manifest["revisao"])

    # -------------------------------------------------------------------
    # 1. A PORTA DE ENTRADA (29.2). Ela cai sozinha, sem nenhum portao
    #    acusar, e foi assim que o Clube do Mosaico passou nove dias fora.
    # -------------------------------------------------------------------
    cods_das_portas = []
    for caminho, tipo in PORTAS_DA_292:
        cod, ct, _ = buscar(caminho)
        cods_das_portas.append(cod)
        afirma(cod == 200, "29.2: %s respondeu %s, nao 200" % (caminho, cod))
        afirma(tipo in ct, "29.2: %s veio como %r e tinha de ser %r" % (caminho, ct, tipo))

    cod_home, _, _ = buscar("/")
    afirma(cod_home == 200, "29.2: a home respondeu %s, nao 200" % cod_home)

    virgem = "/caminho-que-nunca-existiu-%d/" % int(__import__("time").time())
    cod, _, _ = buscar(virgem, v=False)
    afirma(cod == 404, "29.2: caminho virgem respondeu %s e tinha de ser 404" % cod)

    # -------------------------------------------------------------------
    # 1-a. O BOTAO DE CADA FORMULARIO TEM DE LEVAR A UMA PAGINA, E ISSO
    #      NASCEU DE UM 404 MEDIDO EM 06/11/2026.
    #
    # Os formularios desta ilha sao `method="get"` para a propria pagina, e
    # o JS e quem chama `preventDefault()`. Entao a URL que o botao monta e
    # uma pagina de verdade, servida a quem estiver SEM JavaScript — e no dia
    # em que a F1 foi ao ar o primeiro campo dela se chamava `w`, que e QUERY
    # VAR RESERVADA do WordPress (a SEMANA do arquivo de data):
    # `/?w=500` devolvia **404**, a pagina "Pagina nao encontrada" da propria
    # ilha. Medido campo por campo, com controle: `w=500` em 404 e `kmh`,
    # `acel` e `mun` em 200 nas mesmas passadas.
    #
    # ESTE DEFEITO E DA FAMILIA MAIS PACIENTE QUE EXISTE: a pagina responde
    # 200, este portao ficava verde, o portao de pixel ficava verde, e o
    # defeito so aparecia para quem APERTASSE O BOTAO sem JavaScript.
    #
    # A AFIRMACAO SE CONSTROI DO HTML SERVIDO, nunca de uma lista escrita
    # aqui: o portao le os `name=` de cada formulario da pagina e monta a
    # query com eles. Formulario novo entra na conta no dia em que nasce, e
    # nome de campo trocado nao deixa a afirmacao velha passando verde.
    # -------------------------------------------------------------------
    # (A afirmacao vive no laco de TODA URL do sitemap, mais abaixo: o contrato que
    #  nasceu deste defeito, a 32.1-b, diz "cada formulario do HTML servido", e a
    #  primeira versao desta regua media so a home — ou seja, media a pagina em que
    #  o defeito foi achado e nao a classe dele. E a licao da 32.5-b: "regua que
    #  nao varre todas certifica a pagina que o autor abriu".)

    # -------------------------------------------------------------------
    # 1-b. A ROTA QUE MEDE A PORTA POR DENTRO (29.3). Ela nasceu nesta ilha
    #      em 03/11/2026, e a divida era de nascimento: a varredura do
    #      despacho de 02/11 listou esta ilha com `NAO` nesta coluna, ao lado
    #      da aquametria. A robometria pagou QUATRO DIAS fora do ar por nao
    #      te-la — em 30/10 o despacho escreveu "nao e consertavel pelo
    #      repositorio", e era verdade sobre aquela ilha e falso sobre o
    #      Arquipelago.
    #
    #      O QUE ESTE PORTAO CONSEGUE PROVAR SEM O TOKEN, que nao esta no
    #      repositorio e nao deve estar: que a rota EXISTE, que a parede
    #      NEGA, e — pelo codigo de erro — que a parede negou depois de achar
    #      a fonte do token e comparar. O reparo em si nao e exercitavel
    #      daqui, e isso esta dito em vez de maquiado.
    # -------------------------------------------------------------------
    _, _, indice = buscar(rest("/rodametria/v1"))
    rotas_no_indice = rotas_do_indice(indice)

    cod_sem, _, _ = buscar(rest(ROTA_DA_293))
    cod_err, _, corpo_err = buscar(rest(ROTA_DA_293) + "&token=token-de-proposito-errado")
    code_err = codigo_do_erro(corpo_err)

    for problema in problemas_da_parede(rotas_no_indice, cod_sem, cod_err, code_err):
        afirma(False, problema)

    # A LINHA DE REGISTRO DIZ O QUE FOI MEDIDO, NUNCA O VEREDITO. A primeira
    # versao dela dizia "a rota esta registrada" — e imprimia isso tambem no
    # mundo em que a rota devolvia 404 e NAO estava registrada. Registro que
    # afirma o que nao mediu e a familia do comentario que declara um
    # mecanismo: parece conferido e nao mede nada (32.5-d). Quem decide aqui
    # sao as afirmacoes acima.
    porta_caida = diagnostico_da_porta(cod_home, cods_das_portas, cod_sem in (200, 401))
    if porta_caida:
        afirma(False, porta_caida)

    registro("29.3: %s %s no indice; sem token -> %s; token errado -> %s com `%s` (a parede medida de fora, sem o token, e o indice lido por ?rest_route= — a porta que nao cai)"
             % (ROTA_DA_293,
                "PRESENTE" if ROTA_DA_293 in rotas_no_indice else "AUSENTE",
                cod_sem, cod_err, code_err))

    # -------------------------------------------------------------------
    # 2. O /status E O PORTAO DO DESEMBARQUE (20.4 e 20.5)
    # -------------------------------------------------------------------
    cod, _, bruto = buscar(rest("/rodametria/v1/status"))
    afirma(cod == 200, "/status respondeu %s" % cod)
    if cod != 200:
        return encerrar()

    st = json.loads(bruto)
    revisao_no_ar = int(st.get("revisao", -1))
    log = st.get("log", [])
    ultimo = str(st.get("ultimo", ""))

    if revisao_no_ar < revisao_esperada:
        # QUATRO CAUSAS, NAO DUAS, e cada uma tem conserto diferente. A regua que
        # morava aqui chamava `ultimo` de "log" e dava veredito de duas pontas; o
        # que isso custou esta medido no docstring de
        # `veredito_da_revisao_atrasada` — OITO minutos de uma execucao da ilha em
        # foco total, reacionando um Sync saudavel.
        ultimo_dt = None
        if ultimo:
            try:
                ultimo_dt = datetime.strptime(ultimo.strip(), "%Y-%m-%d %H:%M:%S")
            except ValueError:
                ultimo_dt = None

        commit_dt = None
        bruto_commit = os.popen(
            "git log -1 --format=%%cd --date=format-local:'%%Y-%%m-%%d %%H:%%M:%%S' -- "
            "'%s' 2>/dev/null" % os.path.join(ILHA, "manifest.json")).read().strip().strip("'")
        if bruto_commit:
            try:
                commit_dt = datetime.strptime(bruto_commit, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                commit_dt = None

        # O raw e OUTRO host, entao nao passa por `buscar()` (que prefixa DOMINIO).
        raw_ja_serve = False
        try:
            url_raw = ("https://raw.githubusercontent.com/rmnatal/arquipelago/main/"
                       "ilhas/rodametria/manifest.json?v=%d"
                       % int(datetime.utcnow().timestamp()))
            with urllib.request.urlopen(urllib.request.Request(
                    url_raw, headers={"User-Agent": "rodametria-conferir/1.0"}),
                    timeout=40) as r:
                raw_ja_serve = int(json.load(r).get("revisao", -1)) >= revisao_esperada
        except Exception:
            raw_ja_serve = False

        codigo, frase = veredito_da_revisao_atrasada(
            ultimo_dt, datetime.utcnow(), commit_dt, raw_ja_serve)

        afirma(False,
               "o manifest esta na revisao %d e o /status esta na %d. CAUSA: `%s` — %s "
               "(`ultimo` = %s; commit do manifest = %s; o raw %s serve a revisao %d)"
               % (revisao_esperada, revisao_no_ar, codigo, frase, ultimo or "ausente",
                  bruto_commit or "desconhecido",
                  "JA" if raw_ja_serve else "AINDA NAO", revisao_esperada))
        return encerrar()

    afirma(revisao_no_ar == revisao_esperada,
           "o /status esta na revisao %d e o manifest na %d" % (revisao_no_ar, revisao_esperada))

    # O LOG LINHA POR LINHA, E SO AS LINHAS DA REVISAO CORRENTE.
    #
    # A 20.4 e literal: "a execucao le as linhas da REVISAO CORRENTE no log do
    # /status, e nenhuma pode deixar de dizer `ok`". Duas versoes anteriores
    # desta regua erraram, cada uma para um lado, e as duas estao registradas
    # porque as duas sao licao:
    #
    #   (1) a primeira lia a JANELA INTEIRA e reprovou a entrega de 29/10 por
    #       causa de quatro linhas `FALHA manifest: HTTP 404` de 28/10 — de
    #       antes de o manifest existir, ou seja a historia de um defeito ja
    #       consertado. Regua que reprova entrega certa e o caminho mais curto
    #       para alguem passar a ignora-la (20.5), e a janela e append-only:
    #       ela SEMPRE vai carregar o passado.
    #   (2) a segunda cortou do topo ate a linha de fecho, supondo que a
    #       revisao COMECA por ela. O log vem do mais novo para o mais velho e
    #       o fecho e escrito por ULTIMO: ele esta no TOPO do grupo. O corte
    #       devolvia 1 linha — o RESUMO — e o portao chamava isso de "lido
    #       linha por linha". Medido no desembarque da revisao 29, em 02/11.
    #
    # AGORA O PORTAO NAO ACREDITA NA PROPRIA CONTAGEM: a linha de fecho DECLARA
    # quantos itens foram aplicados, e as linhas lidas tem de ser esse numero.
    # Janela que rolou e levou item deixa a conta aberta, e aberta ela e dita.
    fecho, itens_da_revisao = linhas_da_revisao(log, revisao_no_ar)

    # A LINHA DA CURA DA PORTA NAO E ITEM DE DESEMBARQUE, E ELA MORA NO MESMO
    # LOG — ACHADO AS 16h4xZ DE 12/11/2026, QUANDO A CURA DISPAROU DE VERDADE
    # PELA PRIMEIRA VEZ, 2h43 DEPOIS DE IR AO AR.
    #
    # O log vem do mais novo para o mais velho e o agrupamento desta regua e
    # POSICIONAL: o fecho da revisao corrente no topo, e tudo abaixo dele ate o
    # fecho anterior. A cura escreveu `2026-11-12 16:25 cura da porta: ...`
    # entre a revisao 89 (16:39) e a 87 (13:39) — e caiu DENTRO do grupo da 89.
    # Resultado: a conta da 20.10 acusou 8 declarados contra 9 lidos, e a
    # afirmacao positiva do `ok` reprovou uma linha que NUNCA vai dizer `ok`
    # porque nao e um item sendo aplicado. **O portao reprovava a ilha sa, e o
    # defeito era da regua.**
    #
    # POR QUE ELA NAO E SIMPLESMENTE DESCARTADA: a 29.4 nomeia esta linha como a
    # EXCECAO que sustenta o chamado — "a serie e o que sustenta o chamado". Ela
    # sai da conta de ITENS e ganha afirmacoes PROPRIAS, sobre a forma que a
    # 29.4 exige: o antes e o depois em bytes e em blocos, e NUNCA o conteudo do
    # arquivo. Linha de classe nova silenciosamente descartada e como item que
    # rolou para fora da janela: aprovar sobre o que sobrou.
    curas = [l for l in itens_da_revisao if CURA_RE.search(l)]
    itens_da_revisao = [l for l in itens_da_revisao if not CURA_RE.search(l)]
    for l in curas:
        m = CURA_FORMA_RE.search(l)
        afirma(m is not None,
               "29.4: a linha da cura da porta esta fora da forma que a 29.4 exige (antes e "
               "depois em bytes e em blocos): %r" % l)
        afirma(not re.search(r"Rewrite(Rule|Cond|Base|Engine)|<IfModule", l),
               "29.4: a linha da cura da porta carrega CONTEUDO do .htaccess, e a trava diz "
               "bytes e blocos e nunca o conteudo: %r" % l)
        if m:
            antes, depois = int(m.group(1)), int(m.group(3))
            afirma(depois > antes,
                   "29.4: a cura da porta registrou %d bytes ANTES e %d DEPOIS — repor bloco "
                   "nao encolhe o arquivo, e a linha e a unica prova do que aconteceu"
                   % (antes, depois))
            afirma("WordPress" in m.group(4),
                   "29.4: a cura da porta diz ter reposto o bloco e o `depois` nao lista "
                   "`WordPress` nos blocos: %r" % l)
    if curas:
        registro("29.4: a cura da porta DISPAROU nesta janela, %d linha(s), e ela nao e item de "
                 "desembarque: %s" % (len(curas), curas))

    afirma(fecho is not None,
           "20.4: o log do /status nao tem a linha de fecho da revisao %d — a janela pode "
           "ter rolado, e entrega sem linha de fecho nao foi conferida" % revisao_no_ar)

    declarados = aplicados_declarados(fecho)
    afirma(declarados is not None,
           "20.4: a linha de fecho da revisao %d nao declara quantos itens aplicou (%r) — sem "
           "esse numero o portao nao tem contra o que conferir o que leu" % (revisao_no_ar, fecho))
    afirma(declarados is None or len(itens_da_revisao) == declarados,
           "20.4: a linha de fecho da revisao %d declara %s item(ns) aplicado(s) e o log traz %d "
           "linha(s) de item. A janela e append-only e tem teto: item que rolou para fora dela "
           "NAO foi conferido, e aprovar sobre o que sobrou e aprovar com cara de completo"
           % (revisao_no_ar, declarados, len(itens_da_revisao)))

    # A AFIRMACAO E POSITIVA DE PROPOSITO: "nenhuma pode deixar de dizer `ok`".
    # Procurar palavra de falha (FALHA, erro, NAO) e a leitura pelo avesso, e ela
    # so pega as falhas que alguem ja imaginou. Linha de item com redacao nova
    # que nao diz `ok` passaria calada — e e exatamente assim que
    # `gravado (#13) mas NAO ativado` chegou ao ar duas vezes.
    muda = [l for l in itens_da_revisao if not re.search(r"\bok\b", l)]
    afirma(not muda,
           "20.4: a revisao %d tem %d linha(s) de item que NAO dizem `ok`: %s"
           % (revisao_no_ar, len(muda), muda))
    registro("20.4: log lido linha por linha — janela de %d linha(s); a revisao %d declara %s "
             "item(ns) aplicado(s) e as %d linha(s) de item dela foram lidas uma por uma, "
             "todas dizendo `ok`"
             % (len(log), revisao_no_ar, declarados, len(itens_da_revisao)))

    antigas = [l for l in log if l not in itens_da_revisao and l != fecho
               and ("FALHA" in l or "erro" in l.lower())]
    if antigas:
        registro("20.4: a janela do log carrega %d linha(s) de FALHA de revisoes ANTERIORES, e "
                 "elas nao sao desta entrega: %s" % (len(antigas), antigas[:2]))
    if len(log) >= 15:
        registro("20.4: a janela do log tem %d linhas e esta CHEIA — item de revisao ANTERIOR "
                 "que rolou para fora dela nao foi conferido por ninguem. Registro, nao "
                 "aprovacao. (Os itens DESTA entrega estao conferidos pela conta do fecho.)"
                 % len(log))

    # -------------------------------------------------------------------
    # 3. A CASCA INSTALOU AS PAGINAS QUE DIZ TER INSTALADO
    # -------------------------------------------------------------------
    cod, _, bruto = buscar(rest("/rodametria/v1/casca"))
    afirma(cod == 200, "/casca respondeu %s — a casca nao esta ativa no ar" % cod)
    urls = {}
    if cod == 200:
        c = json.loads(bruto)
        registro("casca %s instalada em %s"
                 % (c.get("versao_casca"), (c.get("instalado") or {}).get("em")))

        # ---------------------------------------------------------------
        # 3a. A PURGA DE CACHE DO HOSPEDEIRO ESTA CARREGADA (03/11/2026)
        #
        # O "pronto quando" do despacho da purga pedia `tem_purga_de_cache`
        # saindo `true` no ar. Ele sai no retrato da rota da 29.3 desde que
        # a rota nasceu — e aquele retrato exige o TOKEN DO SYNC, que nao
        # esta no repositorio e nao deve estar. Ou seja: o criterio de
        # pronto do despacho nao era conferivel desta nuvem, e portao que
        # nao roda nao e portao. A casca 1.8.0 passou a servir o mesmo
        # booleano no /casca, que e publico.
        #
        # E ELE NAO E REDUNDANTE COM A VERSAO DO SNIPPET (3b abaixo): a
        # versao diz QUAL BYTE o WordPress carregou; este campo diz que a
        # FUNCAO existe no processo. A chamada dentro do reparo da 29.3 e
        # guardada por `function_exists`, entao e esta pergunta — e nao a
        # versao — que decide se o reparo vai purgar ou nao. E a 20.7 ao
        # contrario: la a ausencia do `id` acusa snippet morto; aqui a
        # presenca do booleano prova a funcao viva.
        # ---------------------------------------------------------------
        afirma(c.get("tem_purga_de_cache") is True,
               "/casca diz tem_purga_de_cache=%r — a purga do hospedeiro NAO esta "
               "carregada, e o reparo da 29.3 vai medir a copia velha depois de "
               "consertar" % (c.get("tem_purga_de_cache"),))

        # ---------------------------------------------------------------
        # 3a-b. A CURA DA PORTA ESTA CARREGADA, E TEM ONDE ESCREVER
        #       (12/11/2026, excecao nomeada da 29.4)
        #
        # POR QUE ISTO E AFIRMACAO DE AR E NAO DE BANCADA. A bancada
        # (`teste-cura-da-porta.php`, 174 afirmacoes) prova que a REGRA
        # decide certo; ela nao prova que o codigo esta CARREGADO no
        # WordPress — e snippet gravado e nao ativado e a cicatriz da 20.4,
        # medida tres vezes em quatro dias nesta fabrica, nesta ilha
        # inclusive (revisao 82, em 11/11). Cura que nao esta no processo e
        # cura que nao acontece, e o jeito de descobrir isso NAO pode ser
        # a proxima queda da porta.
        #
        # E O SEGUNDO CAMPO E O QUE SEPARA DOIS SILENCIOS IDENTICOS. A cura
        # e calada por desenho com a porta de pe (trava 4), entao "o log
        # nunca ganhou linha da cura" e o desfecho SADIO de quase todo dia.
        # Ele e tambem o que se veria se a cura nao tivesse onde escrever —
        # e nesse mundo ela, pela trava 3, se recusa a agir. Os dois
        # silencios sao o mesmo byte; `fonte_do_log_da_cura` e o que os
        # distingue, e por isso ele e campo e nao comentario.
        #
        # O NOME DA FONTE E CONFERIDO, nao so a presenca: o Sync desta ilha
        # nao esta no repositorio (nasceu no site, passo 8 da secao 11),
        # entao `funcao:` prova que o nome herdado das irmas esta certo no
        # ar. `option:` nao reprova — e o caminho de reserva, e a linha sai
        # com a mesma forma —, mas ele e DITO, porque e a prova de que a
        # funcao de log do Sync nao esta carregada, e isso e informacao
        # sobre o Sync e nao sobre a cura.
        # ---------------------------------------------------------------
        afirma(c.get("tem_cura_da_porta") is True,
               "/casca diz tem_cura_da_porta=%r — a excecao da 29.4 NAO esta carregada "
               "no ar, e a proxima queda desta porta volta a durar ate alguem rodar um "
               "comando (05/11: ~16 horas)" % (c.get("tem_cura_da_porta"),))

        fonte_cura = c.get("fonte_do_log_da_cura")
        afirma(isinstance(fonte_cura, str) and fonte_cura != "",
               "/casca diz fonte_do_log_da_cura=%r — a cura nao tem onde escrever a "
               "linha da tentativa e, pela trava 3 da 29.4, ela se RECUSA a agir. "
               "Porta sem cura com cara de porta com cura" % (fonte_cura,))
        if isinstance(fonte_cura, str) and fonte_cura.startswith("option:"):
            registro("a cura da porta escreveria pelo caminho de RESERVA (%s), nao pela "
                     "funcao de log do Sync — a linha sai com a mesma forma, e o que isto "
                     "diz e que `rodametria_sync_log` nao esta carregada no ar" % fonte_cura)
        elif fonte_cura == "funcao:rodametria_sync_log":
            registro("a cura da porta escreve pela funcao de log do Sync "
                     "(`rodametria_sync_log`), que e o caminho preferido: um escritor so")

        # ---------------------------------------------------------------
        # 3b. A VERSAO QUE O WORDPRESS CARREGOU, E A AUSENCIA E O SINAL
        #     (02/11/2026)
        #
        # O `sha256` do manifest e sobre o BYTE do repositorio. Ele nao
        # alcanca a cicatriz da 20.4, que custou SETE paginas servindo o
        # tema cru na clubedomosaico DUAS VEZES em tres dias: o Sync grava
        # o snippet INATIVO de proposito e ATIVA depois, e quando a
        # ativacao falha ele escreve `gravado (#13) mas NAO ativado` numa
        # linha do log, SEGUE EM FRENTE e sobe a revisao. O byte estava
        # certo no repositorio nas duas vezes.
        #
        # A partir da casca 1.6.0 o /casca serve `versoes`, que o coletor
        # monta por filtro. Snippet que nao esta ATIVO nao roda, nao
        # pendura o filtro, e o `id` dele NAO APARECE — entao `id` que
        # falta aqui e snippet que nao carregou, nao snippet com versao
        # errada. As duas coisas tem conserto diferente, e por isso o
        # portao as diz separadas em vez de reprovar as duas igual (20.5).
        #
        # E a leitura so e honesta porque `teste-versao-dos-snippets.php`
        # garante, no chao e antes de o ar ser consultado, que todo
        # snippet `publicar: true` SE REGISTRA com o proprio `id`: sem
        # isso, `id` ausente poderia ser descuido do repositorio, e o
        # portao estaria acusando o ar de um defeito da bancada.
        # ---------------------------------------------------------------
        esperadas = dict((it["id"], it.get("versao"))
                         for it in manifest["snippets"] if it.get("publicar"))
        no_ar = c.get("versoes")
        afirma(isinstance(no_ar, dict),
               "o /casca nao serve `versoes` — a casca no ar e anterior a 1.6.0, ou o campo "
               "sumiu. Sem ele o espelho de versao para no repositorio e o ar segue sem regua")
        if isinstance(no_ar, dict):
            faltando = [i for i in esperadas if i not in no_ar]
            afirma(not faltando,
                   "20.4: o /casca nao traz a versao de %s. Snippet que nao esta ATIVO nao "
                   "pendura o filtro, entao `id` ausente aqui significa GRAVADO E NAO ATIVADO "
                   "— o defeito que a 20.4 nomeia, e o conserto e acionar o Sync outra vez"
                   % ", ".join(sorted(faltando)))
            for ident, declarada in sorted(esperadas.items()):
                if ident in no_ar:
                    afirma(no_ar[ident] == declarada,
                           "%s: o manifest declara `versao` %r e o WordPress carregou %r. O "
                           "sha256 bate com o byte do repositorio e o codigo no ar e OUTRO: "
                           "e snippet gravado sem ativar, ou ativacao que pegou a passada "
                           "anterior" % (ident, declarada, no_ar[ident]))
            sobrando = [i for i in no_ar if i not in esperadas]
            if sobrando:
                registro("o /casca traz %d versao(oes) que o manifest nao publica: %s"
                         % (len(sobrando), ", ".join(sorted(sobrando))))
            registro("versao no ar conferida contra o manifest em %d de %d snippet(s) "
                     "publicaveis: %s"
                     % (len([i for i in esperadas if i in no_ar]), len(esperadas),
                        ", ".join("%s %s" % (i, no_ar[i])
                                  for i in sorted(esperadas) if i in no_ar)))
        for linha in ((c.get("instalado") or {}).get("relato") or []):
            afirma("ERRO" not in linha and "ATENCAO" not in linha,
                   "a instalacao da casca relatou: %s" % linha)
            registro("instalacao: %s" % linha)
        for slug, p in (c.get("paginas") or {}).items():
            afirma(bool(p.get("url")),
                   "a pagina %r esta no mapa da casca e nao tem URL no ar — link interno "
                   "para 404 e o defeito de 08/09/2026" % slug)
            if p.get("url"):
                urls[slug] = p["url"]

    # -------------------------------------------------------------------
    # 4. O SITEMAP, E TODA URL DELE EM 200
    # -------------------------------------------------------------------
    cod, _, mapa = buscar("/wp-sitemap.xml")
    sub = re.findall(r"<loc>([^<]+)</loc>", mapa)
    todas = []
    for s in sub:
        c2, _, x = buscar(s.replace(DOMINIO, ""), v=True)
        afirma(c2 == 200, "sub-sitemap %s respondeu %s" % (s, c2))
        todas.extend(re.findall(r"<loc>([^<]+)</loc>", x))
    todas = sorted(set(todas))
    registro("sitemap: %d URL(s) publicada(s)" % len(todas))
    afirma(len(todas) >= 1, "o sitemap nao publica nenhuma URL")

    # O SITEMAP E CURADORIA, NAO INVENTARIO (14.1). Medido em 29/10/2026: quatro
    # das seis URLs eram lixo de fabrica do WordPress, num dominio de dois dias.
    lixo = ("hello-world", "sample-page", "/author/", "/category/", "ola-mundo",
            "pagina-exemplo", "/tag/", "?p=")
    for u in todas:
        for termo in lixo:
            afirma(termo not in u,
                   "14.1: o sitemap publica %s, que e URL fraca de dominio novo — sitemap e "
                   "curadoria, nao inventario" % u)
    for s in sub:
        afirma("users" not in s and "taxonomies" not in s,
               "14.1: o sitemap ainda tem o sub-sitemap %s — arquivo de autor e de "
               "categoria nao e pagina de verdade nesta ilha" % s)

    # -------------------------------------------------------------------
    # 5. CADA PAGINA, UMA POR UMA
    # -------------------------------------------------------------------
    bastidor = BASTIDOR

    # OS NOMES DE ARQUIVO DESTA PASTA, lidos do disco e nunca enumerados: nome
    # de rotina e exatamente o que a 32.4 proibe, e tres comentarios da folha
    # traziam `conferir-32-5-no-navegador.mjs` quando isto foi medido.
    nomes_de_arquivo = []
    for pasta in ("ferramentas", "regras", "dados", "snippets"):
        caminho = os.path.join(ILHA, pasta)
        if os.path.isdir(caminho):
            nomes_de_arquivo += [f for f in os.listdir(caminho)
                                 if os.path.isfile(os.path.join(caminho, f))]
    nomes_de_arquivo += ["manifest.json", "PROMPT.md", "ESTADO.md", "REGISTRO.md",
                         "VOZ.md", "DESIGN.md"]
    registro("nomes de arquivo desta pasta na regua da 32.4: %d" % len(nomes_de_arquivo))

    ancoras_do_site = ancoras_liberadas_do_site()
    registro("liberacoes de quantificador lidas das tres camadas declaradas: %d ancora(s)"
             % len(ancoras_do_site))

    for u in todas:
        caminho = u.replace(DOMINIO, "")
        cod, ct, html = buscar(caminho)
        afirma(cod == 200, "%s respondeu %s" % (caminho, cod))
        if cod != 200:
            continue

        # (2) zero &#038; DENTRO de <script> — contado SO nos blocos script.
        scripts = re.findall(r"<script[^>]*>(.*?)</script>", html, re.S | re.I)
        dentro = sum(s.count("&#038;") for s in scripts)
        afirma(dentro == 0,
               "%s: ha %d entidade(s) &#038; dentro de <script> — e o defeito que derrubou "
               "cinco calculadoras da Aquametria" % (caminho, dentro))

        corpo = corpo_da_pagina(html)
        texto = re.sub(r"<[^>]+>", " ", corpo)
        texto = re.sub(r"\s+", " ", texto).strip()

        # (3) o corpo comeca pelo texto, e nao por metadado YAML.
        afirma(not texto.startswith("---"),
               "%s: o corpo comeca por metadado e nao por texto" % caminho)

        # Pagina fina nao entra no indice de dominio novo (secao 8).
        afirma(len(texto) >= 1500,
               "%s: o corpo tem %d caracteres e o piso e 1.500 — pagina fina gasta orcamento "
               "de rastreamento de dominio novo" % (caminho, len(texto)))
        registro("%s: %d caracteres de corpo" % (caminho, len(texto)))

        # O BOTAO DE CADA FORMULARIO TEM DE LEVAR A UMA PAGINA (32.1-b), E ISSO
        # NASCEU DE UM 404 MEDIDO EM 06/11/2026.
        #
        # Os formularios de ferramenta desta ilha sao `method="get"` para a
        # PROPRIA pagina, e o JS e quem chama `preventDefault()`. Entao a URL que
        # o botao monta e uma pagina de verdade, servida a quem estiver SEM
        # JavaScript — e no dia em que a F1 foi ao ar o primeiro campo dela se
        # chamava `w`, que e QUERY VAR RESERVADA do WordPress (a SEMANA do
        # arquivo de data): `/?w=500` devolvia 404, a pagina "Pagina nao
        # encontrada" da propria ilha. Medido campo por campo, com controle:
        # `w=500` em 404 e `kmh`, `acel` e `mun` em 200 nas mesmas passadas.
        #
        # ESTE DEFEITO E DA FAMILIA MAIS PACIENTE QUE EXISTE: a pagina responde
        # 200, este portao ficava verde em 484 afirmacoes, o portao de pixel
        # ficava verde em 9 de 9, e o defeito so aparecia para quem APERTASSE O
        # BOTAO sem JavaScript. Sete reguas mediram aquela pagina naquele dia e
        # nenhuma tinha como ve-lo, porque nenhuma apertava o botao.
        #
        # A AFIRMACAO SE CONSTROI DO HTML SERVIDO, nunca de uma lista escrita
        # aqui: o portao le os `name=` de cada formulario da pagina e monta a
        # query com os valores que o navegador enviaria. Formulario novo entra na
        # conta no dia em que nasce, e nome de campo trocado nao deixa a
        # afirmacao velha passando verde.
        for _acao, _campos in formularios_da_pagina(html):
            if not _campos:
                continue
            _query = "&".join("%s=%s" % (urllib.parse.quote(n), urllib.parse.quote(str(v)))
                              for n, v in _campos)
            _destino = (_acao.replace(DOMINIO, "") or caminho) or "/"
            _url = _destino + ("&" if "?" in _destino else "?") + _query
            # SEM SEGUIR REDIRECIONAMENTO (item 5 do despacho de 09/11/2026). A
            # 32.1-b e literal: *"monta a query com os valores que o navegador
            # enviaria e exige 200"*. `urlopen` segue 301 por padrao, entao esta
            # linha media "chega em 200" — e aprovava 486 afirmacoes com o botao
            # da ferramenta PRINCIPAL respondendo 301, por causa do `=` vazio do
            # campo opcional de cidade. O visitante nao ve nada quebrado, e e por
            # isso que o defeito e deste tipo: so aparece para quem monta a query
            # a mao e PROIBE o cliente de seguir o salto.
            #
            # A URL E MONTADA AQUI, COM O QUEBRA-CACHE DENTRO, e `buscar` a
            # recebe com `v=False`. MEDIDO: deixando o quebra-cache para o
            # `buscar` acrescentar, a URL comparada NAO era a URL enviada — o
            # `Location` voltava com `&v=1794242521` e o veredito o chamava de
            # "destino diferente", reprovando a canonicalizacao por um parametro
            # que o proprio portao tinha posto. Regua que nao sabe o que mandou
            # nao pode julgar o que voltou.
            _url_v = _url + ("&" if "?" in _url else "?") + "v=" + str(int(time.time()))
            _cod, _, _corpo = buscar(_url_v, v=False, seguir=False)
            _loc = ""
            if _corpo.startswith("LOCATION: "):
                _loc = _corpo.split("\n", 1)[0][len("LOCATION: "):].strip()
            _veredito = veredito_do_botao(DOMINIO + _url_v, _cod, _loc)
            afirma(_veredito == "ok",
                   "32.1-b: o botao de um formulario de %s monta `%s` e essa URL %s"
                   % (caminho, _url, _veredito))
            registro("32.1-b: o formulario de %s monta `%s` e ela responde %s%s"
                     % (caminho, _url, _cod,
                        "" if _cod == 200 else " -> %s (par vazio canonicalizado)" % _loc))

        # A OUTRA METADE DA 32.1-b, E ELA E O VEREDITO DO QUE A PAGINA SERVE
        # (acrescentada em 06/11/2026, na tarde do dia em que a regra nasceu).
        #
        # A afirmacao de cima exige 200 da URL que o botao monta. CONSEGUIDO O
        # 200, nasce o defeito que o 404 escondia: a pagina recarrega e a caixa
        # volta a servir o CASO DE EXEMPLO — ela responde outra pergunta e
        # parece responder a da pessoa. Do lado de fora as duas paginas sao
        # IDENTICAS, entao nem a 22.8 nem a 32.5 cobrem isso: as duas exigem que
        # a resposta pre-renderizada ESTEJA no HTML servido, e ela esta.
        #
        # POR QUE AQUI E NAO SO NA BANCADA: o portao sem rede
        # (`teste-formulario-da-ilha.py`) le o REPOSITORIO, e desde que o aviso
        # virou componente da casca ele aceita a CHAMADA do componente como
        # prova. Chamada no codigo nao e tag na pagina — snippet gravado e NAO
        # ATIVADO (a 20.4) tem a chamada no repositorio e nao escreve byte
        # nenhum. **Quem prova que o aviso chegou ao visitante e esta linha.**
        if formularios_da_pagina(html):
            _tem_aviso = bool(re.search(r"<\s*noscript\b", html, re.I))
            afirma(_tem_aviso,
                   "32.1-b: %s serve <form> e NAO serve <noscript>. Com o JavaScript "
                   "desligado o botao recarrega a pagina e a caixa volta a servir o caso "
                   "de exemplo, sem dizer que e o exemplo" % caminho)
            # O REGISTRO NAO PODE CONTRADIZER A FALHA, e a primeira versao desta
            # afirmacao contradizia: ela imprimia "serve <noscript>" como
            # registro ao lado da propria falha que dizia que NAO servia. E a
            # pagina se desdizendo, um andar abaixo — a mesma familia do bloco
            # de compra da F2 que negava em palavras os botoes que mostrava.
            registro("32.1-b: %s serve <form> e %s <noscript>"
                     % (caminho, "serve" if _tem_aviso else "NAO serve"))

        # O BLOCO DE COMPRA NAO DIZ A MESMA COISA DUAS VEZES (06/11/2026).
        #
        # Com a vitrine vazia, o componente da casca imprimia o paragrafo de
        # ESCOPO e o paragrafo da CAUSA — e quando a ferramenta nao tem o que
        # vender os dois sao a mesma frase. A HOME foi ao ar hoje de manha com o
        # paragrafo inteiro DUPLICADO, as mesmas 14 contagens dentro dos dois, e
        # nenhum portao viu: cada paragrafo, sozinho, e a frase certa, e nenhuma
        # regua comparava os dois ENTRE SI.
        #
        # E a familia do bloco de compra da F2 em 29/10/2026, que "dizia a mesma
        # coisa tres vezes" — e a licao de la media o texto de UMA pagina, por
        # isso nao alcancou este componente. Esta afirmacao mede o COMPONENTE, em
        # toda URL do sitemap, entao ferramenta nova entra na conta no dia em que
        # nasce.
        _escopo = re.findall(r'class="rdm-molde-compra-escopo">(.*?)</p>', html, re.S)
        _vazio = re.findall(r'class="rdm-molde-compra-vazio">(.*?)</p>', html, re.S)
        if _escopo and _vazio:
            _a = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", _escopo[0])).strip()
            _b = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", _vazio[0])).strip()
            afirma(_a != _b,
                   "%s: o bloco de compra serve o MESMO paragrafo duas vezes — o de "
                   "escopo e o da causa de estar vazio sao identicos (%d caracteres "
                   "cada): %r" % (caminho, len(_a), _a[:90]))
            registro("%s: os dois paragrafos do bloco de compra vazio sao diferentes"
                     % caminho)

        # A PAGINA NAO SERVE O MESMO PARAGRAFO LONGO DUAS VEZES (06/11/2026).
        #
        # A afirmacao acima compara os dois paragrafos DENTRO do bloco de compra.
        # Esta e a geral, e ela nasceu porque a de cima nao bastou: no mesmo dia,
        # na mesma ilha, a duplicata apareceu ATRAVESSANDO blocos — e uma delas
        # foi cometida por quem acabara de consertar a outra.
        #
        # AS TRES QUE ELA ACHOU, medidas nas 10 URLs servidas ANTES de esta regua
        # entrar no portao (a licao de metodo desta passada: regua se mede contra
        # o repositorio antes de entrar, e as quatro que nao foram medidas antes
        # reprovaram o texto certo):
        #   /                                 290 caracteres — a recusa sobre
        #       habilitacao saia na CAIXA e outra vez numa DOBRA, desde que a F1
        #       foi ao ar nesta manha;
        #   /peso-maximo-patinete-eletrico/   306 caracteres — a causa de lista
        #       vazia saia no BLOCO DE COMPRA e outra vez no bloco de resposta;
        #   /peso-maximo-patinete-eletrico/   200 caracteres — a frase da margem
        #       saia na CAIXA e outra vez numa DOBRA.
        # **Zero falso positivo nas outras OITO paginas**, com 13 a 32 paragrafos
        # longos cada. E por isso o piso e 120 caracteres: abaixo disso, repetir
        # rotulo e linha de procedencia e normal e a regua reprovaria a pagina
        # certa.
        #
        # POR QUE NENHUM OUTRO PORTAO VE: cada paragrafo, SOZINHO, e a frase
        # certa. Nenhuma regua desta ilha comparava os paragrafos ENTRE SI.
        _longos = []
        for _t in re.findall(r"<(?:p|li)\b[^>]*>(.*?)</(?:p|li)>", html, re.S | re.I):
            _t = desescapar_entidades(re.sub(r"<[^>]+>", " ", _t))
            _t = re.sub(r"\s+", " ", _t).strip()
            if len(_t) >= 120:
                _longos.append(_t)
        _dup = sorted({t for t in _longos if _longos.count(t) > 1})
        afirma(not _dup,
               "%s: serve o MESMO paragrafo mais de uma vez — %d duplicata(s), a "
               "primeira com %d caracteres: %r. Cada paragrafo sozinho e a frase "
               "certa; o que esta errado e a pagina dizer a mesma coisa duas vezes"
               % (caminho, len(_dup), len(_dup[0]) if _dup else 0,
                  _dup[0][:90] if _dup else ""))
        registro("%s: %d paragrafo(s) longo(s), %d duplicado(s)"
                 % (caminho, len(_longos), len(_dup)))

        # A CLASSE DO QUANTIFICADOR E DO SUPERLATIVO, EM TODA URL DO SITEMAP.
        conferir_classe_no_site(caminho, texto, ancoras_do_site)

        # <title>, H1, description e JSON-LD (32.3: nenhum deles muda com o molde).
        afirma(bool(re.search(r"<title>[^<]{10,}</title>", html)),
               "%s: sem <title>" % caminho)

        # O og:title E O <title>, LETRA POR LETRA (11/11/2026).
        #
        # MEDIDO NO AR as 10h3xZ de 11/11/2026, revisao 78, em 10 de 10 URLs: o
        # `<title>` servia o `titulo` do mapa de paginas e o `og:title` servia o
        # `nome`, que e o rotulo da TRILHA da 16.3. A home se chamava "Inicio" no
        # cartao de compartilhamento; a F3, "Carga maxima". O `og:description` ao
        # lado ja lia a MESMA `description` da meta de cima — o par `og:` estava
        # metade certo, e e por isso que isto e defeito e nao escolha.
        #
        # O og:title JA ESTAVA NA REGUA DESTA ILHA — `META_DE_LEITOR` o nomeia,
        # e as cinco reguas de vocabulario o leem desde 09/11. O que nenhuma
        # delas podia ver e que o VALOR estava certo e vinha do CAMPO ERRADO:
        # "Inicio" e acentuado, nao e chave de maquina e nao e vocabulario de
        # bastidor. A regua que pega isto nao e de vocabulario, e de CONTAGEM DE
        # DECLARACOES — a mesma familia do `Mediano` da barra fixa, de 10/11.
        _t_doc = re.search(r"<title>([^<]*)</title>", html)
        _t_og = re.search(r'<meta property="og:title" content="([^"]*)"', html)
        afirma(bool(_t_og), "%s: sem og:title" % caminho)
        if _t_doc and _t_og:
            _d = desescapar_entidades(_t_doc.group(1)).strip()
            _o = desescapar_entidades(_t_og.group(1)).strip()
            afirma(_d == _o,
                   "%s: o <title> serve %r e o og:title serve %r. Duas declaracoes "
                   "do mesmo fato comecam iguais e so uma sobe (20.7) — e o "
                   "og:title e o nome que o WhatsApp, o Facebook e o Slack mostram "
                   "do link" % (caminho, _d[:70], _o[:70]))

        h1 = re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.S | re.I)
        afirma(len(h1) == 1, "%s: tem %d <h1> e tinha de ter 1" % (caminho, len(h1)))
        desc = re.search(r'<meta name="description" content="([^"]{20,})"', html)
        afirma(bool(desc), "%s: sem meta description" % caminho)
        if desc:
            # ITEM 5 DO DESPACHO DE 30/10/2026. O teto era 200 e por isso ele
            # APROVOU uma description de 193 e uma de 161: a ronda achou as duas
            # a olho, com o portao verde. 160 e o numero que o despacho declara.
            # E O QUE SE CONTA E O TEXTO, NAO A MARCACAO: o atributo vem
            # escapado do `esc_attr` do WordPress, entao um apostrofo chega como
            # `&#039;` e contaria 6 caracteres no lugar de 1 — a familia do
            # `&#038;` que a propria 12 cobra dentro de <script>. Desfazer as
            # entidades antes de medir e o que faz o numero ser o do leitor.
            texto_desc = desescapar_entidades(desc.group(1))
            afirma(len(texto_desc) <= 160,
                   "%s: description com %d caracteres e o teto e 160"
                   % (caminho, len(texto_desc)))
            registro("%s: description com %d caracteres" % (caminho, len(texto_desc)))
        jsonld = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
        afirma(len(jsonld) >= 1, "%s: sem JSON-LD" % caminho)
        for j in jsonld:
            try:
                json.loads(j)
            except Exception as e:
                afirma(False, "%s: JSON-LD invalido (%s)" % (caminho, e))
        # ITEM 2 DO DESPACHO DE 04/11/2026 — `dateModified` EM TODA URL DO SITEMAP.
        # O defeito medido: ZERO ocorrencia de `dateModified` e ZERO de
        # `datePublished` em todo o JSON-LD das 9 URLs, numa ilha cujo produto E
        # "o preco de hoje". As paginas diziam a data em PROSA e a camada que o
        # Google e as IAs leem nao dizia nada — a familia da 25.9: chave ausente
        # nao declara nada.
        #
        # E A AFIRMACAO NAO PARA NA PRESENCA DA CHAVE: a data servida tem de
        # APARECER NA PROSA da propria pagina, no formato brasileiro, quando a
        # pagina publicar alguma data. Sem isso o campo poderia dizer "hoje" em
        # pagina que nao muda desde 30/10, que e precisamente a mentira que um
        # sinal de frescor pode contar — e seria uma SEGUNDA declaracao do mesmo
        # fato, que e o que a 20.7 proibe.
        datas_ld = []
        for j in jsonld:
            try:
                datas_ld += re.findall(r'"dateModified"\s*:\s*"(\d{4}-\d{2}-\d{2})', j)
            except Exception:
                pass
        afirma(len(datas_ld) >= 1,
               "%s: nenhum JSON-LD declara `dateModified`. A ilha que recoleta preco e a que mais "
               "precisa do sinal de frescor, e chave ausente nao declara nada (25.9)" % caminho)
        for d in set(datas_ld):
            br = "%s/%s/%s" % (d[8:10], d[5:7], d[:4])
            datas_na_prosa = set(re.findall(r"\d{2}/\d{2}/\d{4}", texto))
            if datas_na_prosa:
                afirma(br in datas_na_prosa,
                       "%s: o JSON-LD diz dateModified %s (%s) e a prosa da pagina nao traz essa data "
                       "em lugar nenhum (traz %s). Duas declaracoes do mesmo fato comecam iguais e so "
                       "uma sobe (20.7)"
                       % (caminho, d, br, ", ".join(sorted(datas_na_prosa)) or "nenhuma"))
            else:
                registro("%s: dateModified %s, e a pagina nao publica data em prosa para cruzar"
                         % (caminho, d))
        if datas_ld:
            registro("%s: dateModified %s" % (caminho, ", ".join(sorted(set(datas_ld)))))

        # O ENVELOPE DE TODO `ItemList` SERVIDO (12/11/2026), e a razao de ele
        # ser medido AQUI e nao so no portao de vitrine: `conferir-produto-no-ar`
        # descobre as paginas CASANDO o sitemap com os slugs da vitrine, entao
        # `ItemList` servido em qualquer OUTRA pagina desta ilha nao teria
        # portao nenhum. Sem a fonte do repositorio na mao, o que se afirma aqui
        # e a metade das CAMADAS — `name` x `<h1>`, `description` x `meta` x
        # `og:`, `numberOfItems` x contagem, posicoes 1..N e os dois `@type`.
        # A regra inteira e o motivo estao em `teste-envelope-do-itemlist.py`.
        if _REGUA_DO_ENVELOPE is None:
            registro("%s: o envelope do ItemList NAO foi medido (%s)"
                     % (caminho, _POR_QUE_SEM_ENVELOPE))
        else:
            _listas_env = _REGUA_DO_ENVELOPE.itemlists_do_html(html)
            if _listas_env:
                _tela_env = _REGUA_DO_ENVELOPE.declaracoes_da_pagina(html)
                for _ie, _lista_env in _listas_env:
                    _maus_env = _REGUA_DO_ENVELOPE.problemas_do_envelope(
                        caminho, _lista_env, _tela_env)
                    afirma(not _maus_env,
                           "%s: %d problema(s) no ENVELOPE do ItemList. O primeiro: %s"
                           % (caminho, len(_maus_env),
                              _maus_env[0] if _maus_env else ""))
                registro("%s: %d ItemList servido(s), envelope medido nas camadas"
                         % (caminho, len(_listas_env)))
            # E A OUTRA METADE, QUE E REGISTRO E NAO VEREDITO: a pagina que
            # serve bloco de compra COM cartao e nao declara `ItemList` nenhum.
            # Medido no ar as 19h2xZ de 12/11/2026 nas 10 URLs: TRES paginas
            # servem `id="comprar"` e so DUAS declaram lista — a terceira e
            # `/autonomia-patinete-eletrico/`, com 4 cartoes de preco datado e
            # ZERO `Product`. As outras duas com bloco de compra (`/` e
            # `/peso-maximo-patinete-eletrico/`) o servem VAZIO, e nelas a
            # ausencia e legitima. Nao e afirmacao porque a escolha entre
            # declarar a lista ou nao e da Fundacao (19.2) e esta escrita no
            # REGISTRO.md desta data; o numero fica aqui para ela nao precisar
            # ser remedida.
            _cartoes_de_compra = len(re.findall(
                r'<li[^>]*class="[^"]*rdm-molde-cartao', corpo))
            if 'id="comprar"' in corpo and _cartoes_de_compra and not _listas_env:
                registro("%s: serve bloco de compra com %d cartao(oes) e NENHUM "
                         "ItemList — a tela declara o preco e a camada da maquina "
                         "nao declara nada (32.4-c)"
                         % (caminho, _cartoes_de_compra))

        # =================================================================
        # AS DUAS AFIRMACOES QUE ESTA ILHA NAO PODE FAZER, NA TELA E NO JSON-LD
        # (itens 2, 3 e 4 do despacho de 06/11/2026)
        #
        # A regua e de `teste-afirmacao-de-tela.py` e esta importada no topo; o
        # que e DAQUI e a superficie: o HTML servido, elemento por elemento, mais
        # as strings e os pares de pergunta/resposta de todo `application/ld+json`
        # — em TODA URL do `wp-sitemap.xml`, que e o alcance que o item 3 exige.
        #
        # MEDIDO CONTRA A REVISAO 60 ANTES DE QUALQUER CONSERTO, como o proprio
        # despacho manda (*"portao que nao reprova o defeito conhecido nao esta
        # medindo nada"*): 6 afirmacoes de habilitacao, 9 promessas de peso e 2
        # pares de FAQ, em 5 das 10 URLs — e ZERO falso positivo nas outras
        # cinco, inclusive na HOME, que e onde moram as sete mencoes CERTAS a
        # habilitacao desta ilha, e na F2, que e dona da unica oracao de recusa
        # de peso.
        # =================================================================
        if _REGUA_DE_AFIRMACAO is None:
            registro("%s: as duas afirmacoes NAO foram medidas (%s)"
                     % (caminho, _POR_QUE_SEM_REGUA))
        else:
            _elem = elementos_de_prosa(corpo)
            _ld_textos, _ld_pares = frases_e_pares_do_jsonld(jsonld)
            _maus_hab = (_REGUA_DE_AFIRMACAO.problemas_de_habilitacao(
                             "%s (tela)" % caminho, _elem)
                         + _REGUA_DE_AFIRMACAO.problemas_de_habilitacao(
                             "%s (JSON-LD)" % caminho, _ld_textos))
            _maus_peso = (_REGUA_DE_AFIRMACAO.problemas_de_peso(
                              "%s (tela)" % caminho, _elem)
                          + _REGUA_DE_AFIRMACAO.problemas_de_peso(
                              "%s (JSON-LD)" % caminho, _ld_textos))
            _maus_faq = _REGUA_DE_AFIRMACAO.problemas_do_faq_de_habilitacao(
                "%s (FAQPage)" % caminho, _ld_pares)
            afirma(not _maus_hab,
                   "%s: %d afirmacao(oes) sobre HABILITACAO sem nenhuma das oracoes "
                   "de recusa desta ilha. A 996/2023 decide a categoria e nao tem "
                   "artigo sobre CNH; o CTB nao foi lido na fonte. A primeira: %s"
                   % (caminho, len(_maus_hab), _maus_hab[0] if _maus_hab else ""))
            afirma(not _maus_peso,
                   "%s: %d texto(s) prometendo o peso de quem pilota na conta de "
                   "autonomia, que a F2 NAO faz (a constante de consumo por quilo "
                   "esta pendente). O primeiro: %s"
                   % (caminho, len(_maus_peso), _maus_peso[0] if _maus_peso else ""))
            afirma(not _maus_faq,
                   "%s: %d pergunta(s) de FAQPage sobre habilitacao cuja resposta "
                   "nao recusa responder. E a metade que o Google e as ferramentas "
                   "de IA citam sem abrir formulario nenhum. A primeira: %s"
                   % (caminho, len(_maus_faq), _maus_faq[0] if _maus_faq else ""))
            registro("%s: %d elemento(s) de prosa e %d string(s) de JSON-LD na regua "
                     "das duas afirmacoes, %d par(es) de FAQ"
                     % (caminho, len(_elem), len(_ld_textos), len(_ld_pares)))

            # -------------------------------------------------------------
            # O VOCABULARIO DA TELA, NAS CINCO REGUAS, COM A CITACAO DESCONTADA
            # (10/11/2026). Ver o comentario de `citacoes_do_dado` acima: as
            # duas medicoes que a fizeram nascer sao a chave `observacao_de_mercado`
            # servida pela F2 como frase e os cinco `pagina` sem acento da
            # `/privacidade/`.
            _cit = citacoes_do_dado()
            _attr = textos_de_atributo(corpo)
            _maus_voc = (problemas_de_vocabulario_servido(
                             "%s (tela)" % caminho, _elem, _cit)
                         + problemas_de_vocabulario_servido(
                             "%s (atributo)" % caminho,
                             [t for _onde, t in _attr], _cit))
            afirma(not _maus_voc,
                   "%s: %d texto(s) servido(s) no vocabulario da FABRICA e nao no "
                   "de quem le — palavra portuguesa sem acento, bastidor, nome do "
                   "dono, formato de maquina ou chave de maquina —, ja descontadas "
                   "as %d citacoes que esta ilha faz de proposito. O primeiro: %s"
                   % (caminho, len(_maus_voc), len(_cit),
                      _maus_voc[0] if _maus_voc else ""))
            # A CONTA DAS TRES SUPERFICIES VAI DITA, pela 20.8: portao que nao
            # diz sobre quanto mediu aprova sobre o que sobrou com cara de
            # completo. A de atributo e a mais nova e a que precisa mais disso —
            # ela nasceu com zero afirmacao nas oito URLs que passam, e zero
            # afirmacao e indistinguivel de regua que nao rodou.
            registro("%s: %d texto(s) de ATRIBUTO na regua do vocabulario (%s)"
                     % (caminho, len(_attr),
                        ", ".join(sorted({onde for onde, _t in _attr})) or "nenhum"))

            # -------------------------------------------------------------
            # A TERCEIRA AFIRMACAO: O MESMO ATO DE COLHER CONTADO DUAS VEZES
            # NA MESMA PAGINA (item 4 do despacho de 09/11/2026).
            #
            # AQUI E QUE ELA VALE, e nao no repositorio: a unidade desta classe
            # e a PAGINA, porque cada frase, sozinha, esta certa. A home servia
            # "17 veiculos colhidos" numa dobra e "14 anuncios que a gente
            # colheu" em duas outras, com os tres numeros CERTOS — e nenhum
            # portao via, porque nenhum lia a pagina como um texto so.
            #
            # A TELA E O JSON-LD JUNTOS, de proposito: a camada que a IA ingere
            # cita as mesmas contagens, e foi la que os defeitos de 09/11 de
            # manha moravam. Contradicao que a tela nao tem e o JSON-LD tem
            # continua sendo contradicao da pagina.
            _maus_colheita = _REGUA_DE_AFIRMACAO.problemas_de_colheita(
                "%s (tela + JSON-LD)" % caminho, list(_elem) + list(_ld_textos))
            afirma(not _maus_colheita,
                   "%s: %s" % (caminho, _maus_colheita[0] if _maus_colheita else ""))
            _contagens = sorted({n for t in (list(_elem) + list(_ld_textos))
                                 for n, _tr in _REGUA_DE_AFIRMACAO.contagens_de_colheita(t)})
            registro("%s: %d contagem(ns) distinta(s) de colheita na pagina (%s)"
                     % (caminho, len(_contagens),
                        ", ".join(str(n) for n in _contagens) or "nenhuma"))

        # =================================================================
        # A CAMADA QUE NAO TEM VIZINHO — REMISSAO LOCATIVA E ORACAO REPETIDA
        # (09/11/2026, os dois medidos no ar nesta mesma passada)
        #
        # Isto NAO e a regua de cima com outra lista: aquela mede AFIRMACAO (a
        # pagina diz algo que nao pode dizer) e esta mede o que a CAMADA pode
        # cumprir. `Os nomes estao logo abaixo` e verdade na tela e mentira no
        # JSON-LD, sem que uma palavra da frase mude — por isso ela roda SO
        # sobre o JSON-LD, e nao sobre a prosa.
        # =================================================================
        if _REGUA_DE_REMISSAO is None:
            registro("%s: a remissao de camada NAO foi medida (%s)"
                     % (caminho, _POR_QUE_SEM_REMISSAO))
        else:
            _ld_textos2, _ld_pares2 = frases_e_pares_do_jsonld(jsonld)
            _maus_rem = _REGUA_DE_REMISSAO.problemas_de_remissao(
                "%s (JSON-LD)" % caminho, _ld_textos2)
            _maus_rep = _REGUA_DE_REMISSAO.problemas_de_oracao_repetida(
                "%s (FAQPage)" % caminho, _ld_pares2)
            afirma(not _maus_rem,
                   "%s: %d remissao(oes) locativa(s) no JSON-LD — prosa que aponta "
                   "para um lugar da pagina numa camada que nao tem vizinho nem "
                   "ordem. A primeira: %s"
                   % (caminho, len(_maus_rem), _maus_rem[0] if _maus_rem else ""))
            afirma(not _maus_rep,
                   "%s: %d resposta(s) de FAQPage declarando o mesmo fato duas "
                   "vezes dentro de si. A primeira: %s"
                   % (caminho, len(_maus_rep), _maus_rep[0] if _maus_rep else ""))

        if caminho not in ("/", ""):
            afirma(any("BreadcrumbList" in j for j in jsonld),
                   "%s: sem BreadcrumbList, e a 16.4 o exige em toda pagina que nao e a home"
                   % caminho)
            afirma("rdm-trilha" in html, "%s: sem trilha na tela" % caminho)

        # Menu acessivel (secao 6), favicon proprio e marca.
        afirma('aria-expanded' in html and 'aria-controls' in html,
               "%s: o botao do menu esta sem aria-expanded/aria-controls" % caminho)
        afirma('rel="icon"' in html and "image/svg+xml" in html,
               "%s: sem favicon proprio — icone padrao do WordPress na aba e bloco reprovado"
               % caminho)
        afirma("rdm-marca" in html, "%s: a casca nao pintou a marca" % caminho)
        afirma(html.count("rdm-rodape") >= 1, "%s: sem rodape da casca" % caminho)
        afirma(len(re.findall(r'class="rdm-rodape"', html)) <= 1,
               "%s: DOIS rodapes empilhados" % caminho)

        # Imagem com width/height e alt (secao 6 e 32.3).
        for img in re.findall(r"<img[^>]*>", corpo):
            afirma("alt=" in img, "%s: <img> sem alt: %s" % (caminho, img[:80]))
            afirma("width=" in img and "height=" in img,
                   "%s: <img> sem width/height: %s" % (caminho, img[:80]))

        # 32.4: zero palavra de bastidor no texto SERVIDO.
        for termo in bastidor:
            afirma(termo.lower() not in texto.lower(),
                   "32.4: a palavra de bastidor %r aparece no texto servido de %s"
                   % (termo, caminho))
        # E OS TERMOS DE FRONTEIRA DE PALAVRA, no texto visivel (itens 2 e 3 do
        # despacho de 11/11/2026). Afirmacao separada da de cima porque a regua
        # e outra, nao porque o conserto seja outro.
        for problema in problemas_de_bastidor_com_fronteira(texto, "texto visivel de %s" % caminho):
            afirma(False, problema)

        # A FOLHA DESTA ILHA NAO SERVE OS PROPRIOS COMENTARIOS (bloco 7).
        nossas = folhas_da_ilha(html)
        afirma(len(nossas) >= 1,
               "%s: nao serve nenhuma folha desta ilha — ou o snippet esta gravado e NAO "
               "ativado (20.7), ou a tag <style> deixou de sair da casca" % caminho)
        for problema in problemas_da_folha_servida(html):
            afirma(False, "%s: %s" % (caminho, problema))

        # E O ROTEIRO DESTA ILHA, PELA MESMA RAZAO E NUMA AFIRMACAO SEPARADA
        # (11/11/2026). Separada da folha porque o conserto e outro (20.5):
        # um sai de `rodametria_casca_fechar_folha()`, o outro de
        # `rodametria_casca_fechar_roteiro()`. Pagina sem roteiro nosso e
        # legitima — as quatro institucionais e as tres de produto nao tem
        # formulario —, entao aqui nao ha piso de contagem como o da folha.
        for problema in problemas_do_roteiro_servido(html):
            afirma(False, "%s: %s" % (caminho, problema))

        # O ARTIGO CONCORDA COM A LOJA (11/11/2026). Sobre a prosa e sobre o
        # texto de atributo, porque o nome da loja aparece nos dois.
        for problema in problemas_de_artigo_da_loja(
                elementos_de_prosa(corpo) + [v for _, v in textos_de_atributo(corpo)]):
            afirma(False, "%s: %s" % (caminho, problema))

        # E A 32.4 SOBRE O HTML SERVIDO INTEIRO, separada da de cima porque o
        # conserto de cada uma e diferente (20.5).
        for problema in problemas_de_bastidor_no_servido(html, nomes_de_arquivo):
            afirma(False, "%s: %s" % (caminho, problema))
        # ... e os de fronteira, sobre o BYTE SERVIDO INTEIRO, que e onde mora o
        # JSON-LD. O item 2 do despacho pede as duas leituras com todas as
        # letras: "zero ocorrencia em texto visivel E em JSON-LD".
        for problema in problemas_de_bastidor_com_fronteira(html, "HTML servido de %s" % caminho):
            afirma(False, problema)


        # E AS DUAS LISTAS DA 32.4 SOBRE AS DUAS SUPERFICIES DESESCAPADAS: o
        # texto de ATRIBUTO e o VALOR do JSON-LD (11/11/2026, a tarde). Ver o
        # comentario de `valores_do_jsonld()` acima para as tres razoes de nao
        # bastar o byte servido — entidade de HTML, escape de JSON e endereco.
        # Duas afirmacoes SEPARADAS porque o conserto de cada uma mora em
        # arquivo diferente (20.5): atributo sai da casca e do gerador da
        # vitrine; valor de JSON-LD sai do snippet que monta o bloco.
        _attr_324 = textos_de_atributo(corpo)
        _ld_324 = valores_do_jsonld(jsonld)
        _maus_attr = problemas_de_bastidor_em_pares(_attr_324, "atributo de %s" % caminho)
        _maus_ld = problemas_de_bastidor_em_pares(_ld_324, "JSON-LD de %s" % caminho)
        afirma(not _maus_attr,
               "%s: %d texto(s) de ATRIBUTO com palavra de bastidor da 32.4 — e e "
               "o atributo que o leitor de tela anuncia e que o ponteiro mostra. "
               "O primeiro: %s"
               % (caminho, len(_maus_attr), _maus_attr[0] if _maus_attr else ""))
        afirma(not _maus_ld,
               "%s: %d valor(es) de JSON-LD com palavra de bastidor da 32.4 — e e "
               "a camada que o Google e as ferramentas de IA citam sem abrir a "
               "pagina. O primeiro: %s"
               % (caminho, len(_maus_ld), _maus_ld[0] if _maus_ld else ""))
        # A CONTA DAS DUAS VAI DITA (20.8): zero achado e indistinguivel de regua
        # que nao rodou, e as duas nasceram com zero achado nas 10 URLs.
        registro("%s: a 32.4 leu %d texto(s) de atributo e %d valor(es) de JSON-LD"
                 % (caminho, len(_attr_324), len(_ld_324)))

        # O `alt` NAO REPETE A PROSA QUE VEM LOGO DEPOIS DELE (11/11/2026).
        for problema in alts_que_repetem_a_prosa_vizinha(corpo):
            afirma(False, "%s: %s" % (caminho, problema))

        # A CONCORDANCIA DA ORACAO DE SUJEICAO, nas DUAS camadas (11/11/2026).
        # Sobre a prosa visivel e sobre o valor do JSON-LD, porque a celula da
        # tabela da regra e colada nas duas e o defeito medido estava na segunda.
        _textos_da_sujeicao = (elementos_de_prosa(corpo)
                               + [v for _onde, v in _ld_324])
        _maus_conc, _sem_suj = problemas_de_concordancia_da_sujeicao(
            _textos_da_sujeicao, caminho)
        afirma(not _maus_conc,
               "%s: %d oracao(oes) de sujeicao concordando com outro sujeito. A "
               "primeira: %s"
               % (caminho, len(_maus_conc), _maus_conc[0] if _maus_conc else ""))
        for linha in _sem_suj:
            registro(linha)

        # Shortcode cru na tela e desembarque que nao aconteceu.
        afirma("[rodametria_" not in texto,
               "%s: shortcode cru servido na tela — o snippet nao esta ativo" % caminho)

    # -------------------------------------------------------------------
    # 6. A F2, AFIRMACAO POR AFIRMACAO CONTRA O BANCO
    # -------------------------------------------------------------------
    d = json.load(open(os.path.join(ILHA, "dados", "f2-respostas.json"), encoding="utf-8"))
    alvo = None
    for u in todas:
        if "autonomia" in u:
            alvo = u.replace(DOMINIO, "")
    afirma(alvo is not None, "a F2 nao esta no sitemap")
    if alvo:
        cod, _, html = buscar(alvo)
        corpo = corpo_da_pagina(html)
        texto = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", corpo))

        # (4) o script vem do RODAPE e a tabela aparece no HTML servido.
        pos_script = html.find('id="rodametria-f2-js"')
        pos_corpo = html.find("rdm-tabela")
        afirma(pos_script > pos_corpo > 0,
               "a F2 serve o script antes da tabela — o JS tinha de vir do rodape")
        afirma("rdm-tabela" in html, "a F2 nao serve a tabela pre-renderizada")

        # A CAIXA DE RESULTADO ESTA PRE-RENDERIZADA: o numero do exemplo tem de
        # estar no HTML servido, sem ninguem clicar em nada. E a 32.1 item 4 e a
        # secao 5 (visibilidade em IA) na mesma afirmacao.
        r = d["resposta_exemplo"]
        # O NUMERO PRE-RENDERIZADO DEPENDE DO MUNDO DO EXEMPLO, e desde
        # 13/11/2026 (item 2 do despacho da ronda) o exemplo entregue NAO tem
        # autonomia declarada: os dois campos opcionais chegam vazios, e o que a
        # caixa publica e a ENERGIA. A regua anterior procurava `piso_km_tela`
        # cru e estourava com `None` — portao que estoura nao reprova, so some,
        # e a bancada o chamou de INERTE na mesma passada.
        if r["piso_km_tela"] is None:
            afirma(r["wh_tela"] in corpo,
                   "a F2 nao serve o Wh do exemplo (%s) no HTML" % r["wh_tela"])
            # A CAUSA DA RECUSA ESTA NO AR, e FORA da caixa: dentro dela o
            # primeiro botao de compra sai dos 1.400 px da 32.5.
            porque = re.sub(r"\s+", " ", r["frase_porque_da_recusa"] or "")
            afirma(bool(porque) and porque[:60] in texto,
                   "a F2 recusa o km e nao serve a causa: a 2.4 da especificacao exige "
                   "que a recusa NOMEIE o que falta")
            pos_caixa = corpo.find("data-rdm-f2-caixa")
            pos_porque = corpo.find("rdm-f2-porque")
            pos_compra_da_causa = corpo.find("rdm-molde-compra")
            afirma(0 < pos_caixa < pos_compra_da_causa < pos_porque,
                   "a causa da recusa voltou para dentro da caixa (caixa em %d, compra "
                   "em %d, causa em %d)"
                   % (pos_caixa, pos_compra_da_causa, pos_porque))
            # E NENHUM KG NA RESPOSTA ENTREGUE: o campo do peso chega vazio, e
            # a pagina nao devolve ao leitor um numero que ela mesma escreveu.
            for f in r["frases_km"] + r["frases_peso"]:
                afirma(" kg" not in f,
                       "a F2 serve um peso em kg sem que o leitor tenha informado "
                       "nenhum: %r" % f[:80])
        else:
            afirma(r["piso_km_tela"] in corpo,
                   "a F2 nao serve o piso de km do exemplo (%s) no HTML" % r["piso_km_tela"])
            afirma(r["teto_km_tela"] in corpo,
                   "a F2 nao serve o teto de km do exemplo (%s) no HTML" % r["teto_km_tela"])
        for f in r["frases_km"] + r["frases_peso"]:
            limpo = re.sub(r"\s+", " ", f)
            afirma(limpo[:60] in texto,
                   "a F2 nao serve a frase do banco: %r" % limpo[:70])

        # A RESSALVA DO PESO ESTA DEPOIS DO BLOCO DE COMPRA, e nao dentro da
        # caixa: e o que mantem o primeiro botao de compra acima do teto de
        # 1.400 px da 32.5 no telefone de 390 px.
        pos_compra = corpo.find("rdm-molde-compra")
        pos_ressalva = corpo.find("rdm-f2-ressalva")
        afirma(0 < pos_compra < pos_ressalva,
               "a ressalva do peso nao esta depois do bloco de compra (compra em %d, "
               "ressalva em %d)" % (pos_compra, pos_ressalva))

        # TODA linha da tabela do banco esta no ar, com o Wh que o banco diz.
        for l in d["tabela"]["do_banco"] + d["tabela"]["externas"]:
            afirma(l["rotulo"] in corpo,
                   "a linha %r da tabela nao esta no ar" % l["rotulo"])
            afirma(l["wh"] in corpo,
                   "o Wh %r da linha %r nao esta no ar" % (l["wh"], l["rotulo"]))

        # O BLOCO DE COMPRA: conta CARTAO contra BLOCO, nunca a classe de um
        # degrau (secao 8 — sete reguas quebraram por procurar o rotulo do
        # degrau). O degrau viaja como registro, nunca como criterio.
        cartoes = re.findall(r'class="rdm-molde-cartao"', corpo)
        afirma(len(cartoes) == len(d["compra"]["vitrine"]),
               "o bloco de compra serve %d cartao(oes) e a vitrine do banco tem %d"
               % (len(cartoes), len(d["compra"]["vitrine"])))
        afirma(len(cartoes) >= 1,
               "o bloco de compra esta VAZIO, e a secao 7 proibe: o piso e o link de busca")
        for f in d["compra"]["vitrine"]:
            afirma(f["url_busca"] in corpo,
                   "a saida de compra de %s nao esta no ar" % f["id"])
            afirma(f["nome"] in corpo, "o nome de %s nao esta no ar" % f["id"])
        for a in re.findall(r"<a[^>]*s\.shopee\.com\.br[^>]*>", corpo):
            afirma('rel="sponsored noopener"' in a,
                   "link de afiliado sem rel sponsored: %s" % a[:90])
            afirma('target="_blank"' in a,
                   "link de afiliado sem target _blank: %s" % a[:90])
        registro("bloco de compra: %d cartao(oes), degrau(s) %s"
                 % (len(cartoes), sorted({f["degrau"] for f in d["compra"]["vitrine"]})))

        # A PRESTACAO DE CONTAS FECHA NO AR, e o numero e lido da TELA.
        total = d["compra"]["total_registros_veiculos"]
        soma = sum(len(v) for v in d["compra"]["grupos"].values())
        afirma(soma == total, "a prestacao de contas do banco nao fecha: %d de %d" % (soma, total))
        m = re.search(r"São (\d+) veículos nomeados de (\d+) no banco", texto)
        afirma(bool(m), "a F2 nao serve a frase que fecha a prestacao de contas")
        if m:
            afirma(int(m.group(1)) == int(m.group(2)) == total,
                   "a tela diz %s nomeados de %s e o banco tem %d"
                   % (m.group(1), m.group(2), total))

        # Toda dobra e <details> de verdade: o texto continua no HTML servido.
        dobras = re.findall(r"<details[^>]*class=\"rdm-molde-dobra\"", corpo)
        afirma(len(dobras) >= 3,
               "a F2 tem %d dobra(s) e a 32.1 item 7 pede o texto recolhivel em secoes" % len(dobras))

        # O aviso de comissao existe e esta visivel (secao 7).
        afirma("comiss" in texto.lower(), "a F2 nao serve o aviso de comissao")

    # -------------------------------------------------------------------
    # 7. O QUE ESTE PORTAO NAO MEDIU — dito, nunca aprovado em silencio
    # -------------------------------------------------------------------
    # Esta linha dizia "que esta ilha ainda nao tem", e envelheceu em UMA HORA:
    # o portao nasceu na mesma execucao. Frase sobre o estado da fabrica dentro
    # de um portao e a mesma divida do numero de tela digitado — ela nao fala
    # com o que descreve. Agora ela CONFERE que o arquivo existe.
    tem_portao_de_pixel = os.path.exists(
        os.path.join(AQUI, "conferir-32-5-no-navegador.mjs"))
    registro("NAO MEDIDO AQUI: a 32.5 (formulario antes de 700 px, primeiro botao de compra "
             "antes de 1.400 px) se mede a 390 px num navegador de verdade. O portao de "
             "pixel %s — rode `node ferramentas/conferir-32-5-no-navegador.mjs`."
             % ("EXISTE nesta ilha e NAO foi rodado por este portao"
                if tem_portao_de_pixel else
                "NAO EXISTE nesta ilha, e a 32.5 segue sem ser medida em pixel"))
    registro("NAO MEDIDO AQUI: a leitura SEM quebra de cache (como o Google le). Toda URL acima "
             "foi pedida com ?v=<agora>, entao estas afirmacoes sao sobre a ORIGEM.")

    return encerrar()


def encerrar():
    print("conferir-no-ar: %d afirmacoes, %d falha(s)" % (afirmacoes, len(falhas)))
    for r in registros:
        print("  registro: %s" % r)
    for f in falhas:
        print("  REPROVADO: %s" % f)
    print("APROVADO" if not falhas else "REPROVADO")

    return 1 if falhas else 0


def autoteste():
    """O CORTE DO LOG, MEDIDO SEM REDE — e o primeiro mundo e o mundo de verdade.

        python3 ferramentas/conferir-no-ar.py --autoteste

    Nasceu em 02/11/2026 junto com o conserto do corte, porque a regua que
    estava errada estava VERDE: ela imprimia "0 linha de falha nesta entrega"
    sobre uma unica linha, a de resumo. Conserto sem mundo fabricado e conserto
    que a proxima mudanca desfaz calada — e a 32.5-d e literal sobre isso: "a
    regra do molde que nunca rodou contra o dado de verdade esta quebrada e
    parece sa".
    """
    ok = []
    mal = []

    def diz(cond, msg):
        (ok if cond else mal).append(msg)

    # MUNDO 1 — O LOG DE VERDADE, lido no /status as 17h40Z de 02/11/2026, no
    # desembarque da revisao 29. E o mundo em que a regua velha devolvia 1.
    real = [
        "2026-11-02 17:40 revisão 29: 8 aplicado(s), 6 aguardando desembarque",
        "2026-11-02 17:40 dados/paginas-institucionais: ok (option rodametria_dados_paginas-institucionais)",
        "2026-11-02 17:40 dados/vitrine-de-produto: ok (option rodametria_dados_vitrine-de-produto)",
        "2026-11-02 17:40 dados/paginas-de-produto: ok (option rodametria_dados_paginas-de-produto)",
        "2026-11-02 17:40 dados/f2-respostas: ok (option rodametria_dados_f2-respostas)",
        "2026-11-02 17:40 snippets/rodametria-institucional: ok (snippet #9 atualizado)",
        "2026-11-02 17:40 snippets/rodametria-produto: ok (snippet #8 atualizado)",
        "2026-11-02 17:40 snippets/rodametria-f2: ok (snippet #7 atualizado)",
        "2026-11-02 17:40 snippets/rodametria-casca: ok (snippet #6 atualizado)",
        "2026-11-02 14:10 revisão 28: 5 aplicado(s), 6 aguardando desembarque",
        "2026-11-02 14:10 dados/paginas-institucionais: ok (option rodametria_dados_paginas-institucionais)",
        "2026-11-02 14:10 dados/vitrine-de-produto: ok (option rodametria_dados_vitrine-de-produto)",
        "2026-11-02 14:10 dados/paginas-de-produto: ok (option rodametria_dados_paginas-de-produto)",
        "2026-11-02 14:10 dados/f2-respostas: ok (option rodametria_dados_f2-respostas)",
        "2026-11-02 14:10 snippets/rodametria-produto: ok (snippet #8 atualizado)",
    ]
    fecho, itens = linhas_da_revisao(real, 29)
    diz(fecho is not None and "revisão 29" in fecho, "1. acha a linha de fecho da revisao 29")
    diz(len(itens) == 8, "1. le 8 linhas de item da revisao 29 (a regua velha lia 1)")
    diz(aplicados_declarados(fecho) == 8, "1. le `8 aplicado(s)` da linha de fecho")
    diz(all(re.search(r"\bok\b", l) for l in itens), "1. as 8 linhas dizem `ok`")

    # MUNDO 2 — A REVISAO ANTERIOR, no meio da janela: o corte nao pode
    # atravessar para a de cima nem para a de baixo.
    fecho28, itens28 = linhas_da_revisao(real, 28)
    diz(len(itens28) == 5, "2. le 5 linhas de item da revisao 28, sem invadir a 29")
    diz(aplicados_declarados(fecho28) == 5, "2. a conta da 28 fecha em 5")
    diz(not any("17:40" in l for l in itens28), "2. nenhuma linha da 29 vazou para a 28")

    # MUNDO 3 — UMA LINHA DE ITEM QUE NAO DIZ `ok`. E a cicatriz com nome: o
    # Sync grava inativo e ativa depois, e na falha escreve esta linha e SEGUE.
    quebrado = list(real)
    quebrado[5] = "2026-11-02 17:40 snippets/rodametria-institucional: gravado (#9) mas NÃO ativado"
    _, itens_q = linhas_da_revisao(quebrado, 29)
    muda = [l for l in itens_q if not re.search(r"\bok\b", l)]
    diz(len(muda) == 1 and "ativado" in muda[0],
        "3. a linha `gravado mas NAO ativado` e PEGA (a regua velha nao a lia)")

    # MUNDO 4 — A JANELA ROLOU E LEVOU ITEM: o fecho declara 8, sobraram 3. A
    # conta nao fecha, e e isso que o portao tem de dizer.
    rolado = real[:4]
    fecho_r, itens_r = linhas_da_revisao(rolado, 29)
    diz(aplicados_declarados(fecho_r) == 8 and len(itens_r) == 3,
        "4. janela rolada: o fecho declara 8 e so 3 itens sobraram — a conta abre")

    # MUNDO 4-b — A LINHA DA CURA DA PORTA DENTRO DO GRUPO DA REVISAO, E ESTE
    # E O MUNDO DE VERDADE, LIDO NO /status AS 16h4xZ DE 12/11/2026. A cura
    # disparou as 16:25 e o desembarque da revisao 89 foi as 16:39: o log vem do
    # mais novo para o mais velho, entao a linha da cura caiu ENTRE o grupo da 89
    # e o fecho da 87 — isto e, DENTRO do grupo da 89 pelo corte posicional.
    #
    # A REGUA INGENUA (a de antes, refeita aqui ao lado) CONTAVA 9 ITENS CONTRA 8
    # DECLARADOS e reprovava a linha da cura por nao dizer `ok`. Ela nunca vai
    # dizer `ok`: nao e um item sendo aplicado, e a 29.4 a nomeia como excecao.
    # **O portao reprovava a ilha sa, e as duas reguas tem de DISCORDAR aqui,
    # senao este mundo nao mede o conserto (20.8).**
    com_cura = [
        "2026-11-12 16:39 revisão 89: 8 aplicado(s), 6 aguardando desembarque",
        "2026-11-12 16:39 dados/municipios: ok (option rodametria_dados_municipios)",
        "2026-11-12 16:39 dados/f3-respostas: ok (option rodametria_dados_f3-respostas)",
        "2026-11-12 16:39 dados/f1-respostas: ok (option rodametria_dados_f1-respostas)",
        "2026-11-12 16:39 dados/paginas-institucionais: ok (option rodametria_dados_paginas-institucionais)",
        "2026-11-12 16:39 dados/vitrine-de-produto: ok (option rodametria_dados_vitrine-de-produto)",
        "2026-11-12 16:39 dados/paginas-de-produto: ok (option rodametria_dados_paginas-de-produto)",
        "2026-11-12 16:39 dados/f2-respostas: ok (option rodametria_dados_f2-respostas)",
        "2026-11-12 16:39 snippets/rodametria-produto: ok (snippet #8 atualizado)",
        "2026-11-12 16:25 cura da porta: bloco WordPress reposto — 0 bytes [] -> 1579 bytes [NFD EPC, WordPress]",
        "2026-11-12 13:39 revisão 87: 8 aplicado(s), 6 aguardando desembarque",
    ]
    fecho_c, itens_c = linhas_da_revisao(com_cura, 89)
    ingenua = list(itens_c)                      # a regua de antes: nao separava nada
    curas_c = [l for l in itens_c if CURA_RE.search(l)]
    itens_c = [l for l in itens_c if not CURA_RE.search(l)]
    diz(len(ingenua) == 9 and aplicados_declarados(fecho_c) == 8,
        "4-b. a regua INGENUA conta 9 itens contra 8 declarados — a conta da 20.10 abre sem defeito embaixo")
    diz(any(not re.search(r"\bok\b", l) for l in ingenua),
        "4-b. a regua INGENUA reprova a linha da cura por nao dizer `ok`, e ela nunca vai dizer")
    diz(len(curas_c) == 1 and len(itens_c) == 8,
        "4-b. a regua NOVA separa 1 linha de cura e 8 de item — a conta da 20.10 fecha 8 contra 8")
    diz(len(ingenua) != len(itens_c),
        "4-b. AS DUAS REGUAS DISCORDAM (9 contra 8), senao este mundo nao mede o conserto (20.8)")
    diz(all(re.search(r"\bok\b", l) for l in itens_c),
        "4-b. as 8 linhas de item que sobraram dizem `ok`, uma por uma")
    m_c = CURA_FORMA_RE.search(curas_c[0]) if curas_c else None
    diz(m_c is not None and int(m_c.group(1)) == 0 and int(m_c.group(3)) == 1579,
        "4-b. a forma da 29.4 e lida da linha: 0 bytes antes, 1.579 depois")
    diz(m_c is not None and m_c.group(2) == "" and "WordPress" in m_c.group(4),
        "4-b. os BLOCOS sao lidos dos dois lados: nenhum antes, `NFD EPC, WordPress` depois")
    diz(not re.search(r"Rewrite(Rule|Cond|Base|Engine)|<IfModule", curas_c[0]) if curas_c else False,
        "4-b. a linha da cura NAO carrega conteudo do .htaccess (a trava da 29.4)")

    # MUNDO 4-c — A CURA QUE ENCOLHE O ARQUIVO, que nao se encena no disco e
    # portanto so existe fabricado: repor um bloco nao pode deixar o arquivo
    # MENOR, e uma linha que diga isso e sinal de que a cura cortou em vez de
    # repor. O mundo 4-b prova que a afirmacao passa; este prova que ela morde.
    encolheu = "2026-11-12 16:25 cura da porta: bloco WordPress reposto — 1579 bytes [NFD EPC, WordPress] -> 0 bytes []"
    m_e = CURA_FORMA_RE.search(encolheu)
    diz(m_e is not None and int(m_e.group(1)) > int(m_e.group(3)),
        "4-c. a regua LE o encolhimento (1.579 -> 0) em vez de aprovar a linha por ela existir")

    # MUNDO 4-d — A LINHA DE ITEM QUE FALA DE CURA SEM SER DA CURA. `CURA_RE`
    # casa `cura da porta:` e nada mais: um snippet chamado `cura-da-porta.php`
    # sendo aplicado e ITEM, e tira-lo da conta seria aprovar sobre o que sobrou.
    quase = "2026-11-12 16:39 snippets/rodametria-cura-da-porta: ok (snippet #11 atualizado)"
    diz(CURA_RE.search(quase) is None,
        "4-d. linha de ITEM com `cura-da-porta` no NOME do arquivo nao e confundida com a linha da cura")

    # MUNDO 5 — REVISAO QUE NAO ESTA NA JANELA.
    fecho_x, itens_x = linhas_da_revisao(real, 99)
    diz(fecho_x is None and itens_x == [],
        "5. revisao fora da janela devolve nada, em vez de devolver a janela toda")

    # MUNDO 6 — FECHO SEM NUMERO DE APLICADOS.
    diz(aplicados_declarados("2026-11-02 17:40 revisão 29: nada a fazer") is None,
        "6. fecho sem `N aplicado(s)` devolve None, e nao um numero inventado")

    # MUNDO 7 — A REGUA VELHA, REFEITA AQUI, TEM DE DISCORDAR DESTA. Se as duas
    # concordarem, este autoteste nao esta medindo o conserto.
    velhas = []
    for l in real:
        velhas.append(l)
        if REV_RE.search(l) and int(REV_RE.search(l).group(1)) == 29:
            break
    diz(len(velhas) == 1 and len(itens) == 8,
        "7. a regua VELHA devolve 1 linha e a nova devolve 8 — o conserto move algo")

    # MUNDO 8 — A ROTA DA 29.3, OS QUATRO MUNDOS QUE ESTA NUVEM NAO PRODUZ.
    # O site de verdade (se tudo estiver sao) devolve SEMPRE o mundo sadio, e
    # portao que so viu o mundo sadio nao mediu nada.
    indice_com = ["/rodametria/v1", "/rodametria/v1/casca", "/rodametria/v1/rotas",
                  "/rodametria/v1/status", "/rodametria/v1/sync", "/rodametria/v1/token"]
    indice_sem = [r for r in indice_com if r != "/rodametria/v1/rotas"]

    diz(problemas_da_parede(indice_com, 401, 401, "rodametria_rotas_token_invalido") == [],
        "8. o mundo SADIO passa (rota no indice, 401 nas duas, codigo de token invalido)")

    sem_rota = problemas_da_parede(indice_sem, 404, 404, None)
    diz(len(sem_rota) >= 2 and any("NAO aparece no indice" in m for m in sem_rota)
        and any("404" in m for m in sem_rota),
        "8. a rota AUSENTE e pega pelo indice E pelo 404 — foi este o mundo da robometria por quatro dias")

    aberta = problemas_da_parede(indice_com, 200, 200, None)
    diz(any("PAREDE ESTA ABERTA" in m for m in aberta),
        "8. a parede ABERTA e pega: 200 sem token entrega o retrato do servidor")

    morto = problemas_da_parede(indice_com, 401, 401, "rodametria_rotas_sem_fonte_de_token")
    diz(any("PORTAO MORTO" in m for m in morto),
        "8. o PORTAO MORTO e pego: 401 nas duas, rota no indice, e a casca negando TODO pedido")

    quinhentos = problemas_da_parede(indice_com, 500, 500, None)
    diz(any("401" in m for m in quinhentos),
        "8. 500 na parede e pego — e o que sai quando o WP_Error nao traz `status`")

    # MUNDO 9 — A REGUA VELHA DESTA LEITURA, refeita ao lado da nova: a que
    # so pergunta "nao deu 200?". Ela APROVA o portao morto e APROVA o 404 —
    # e e por isso que a afirmacao do codigo e positiva (20.8).
    regua_velha = lambda cod: [] if cod != 200 else ["deu 200"]
    diz(regua_velha(401) == [] and morto != [],
        "9. a regua velha APROVA o portao morto e a nova o REPROVA — as duas discordam, senao este autoteste nao mede o conserto")
    diz(regua_velha(404) == [] and sem_rota != [],
        "9. a regua velha APROVA a rota AUSENTE e a nova a REPROVA")

    # MUNDO 10 — A CLASSE DO QUANTIFICADOR E DO SUPERLATIVO, com as TRES frases
    # REAIS que chegaram ao ar por TRES camadas diferentes em TRES dias. A
    # funcao e pura e nao precisa de rede, entao ela roda sempre.
    pegos = []

    def espiao(cond, msg):
        if not cond:
            pegos.append(msg)

    global afirma
    afirma_de_verdade = afirma
    try:
        afirma = espiao
        AS_TRES = (
            "/veiculos/bicicleta-eletrica/ é a reclamação mais comum de quem compra sem fazer essa conta",
            "/divulgacao-de-afiliados/ os dois são a maneira mais comum de prometer um aparelho",
            "/autonomia-patinete-eletrico/ É a lacuna mais comum do varejo: o anúncio grita o watt",
        )
        for i, frase in enumerate(AS_TRES):
            pegos = []
            conferir_classe_no_site("/x/", frase, ())
            diz(len(pegos) == 1,
                "10.%d a frase REAL que foi ao ar e pega pela classe: %r" % (i + 1, frase[:48]))

        # A LIBERACAO FUNCIONA, E SO PARA A ANCORA: a mesma frase com a ancora
        # declarada passa, e uma ancora de OUTRA frase nao a salva.
        pegos = []
        conferir_classe_no_site(
            "/x/", "a media simples porque a grandeza e um multiplicador",
            ("a media simples porque a grandeza e um multiplicador",))
        diz(not pegos, "10.4 ancora declarada libera a frase dela")
        pegos = []
        conferir_classe_no_site(
            "/x/", "a media simples porque a grandeza e um multiplicador",
            ("selo de mais vendido nem nota de estrela",))
        diz(len(pegos) == 1, "10.5 ancora de OUTRA frase nao libera esta")

        # A BORDA DA PALAVRA, pela licao do `Capacete1`: `na media` dentro de
        # `permeado` nao e ocorrencia.
        pegos = []
        conferir_classe_no_site("/x/", "o texto diz amaioria e nada mais", ())
        diz(not pegos, "10.6 termo colado dentro de outra palavra nao conta")

        # E A REGUA VELHA REFEITA AO LADO DA NOVA: a lista SEM o superlativo
        # APROVA as tres frases que foram ao ar, e a nova as REPROVA. Autoteste
        # em que as duas concordam nao mede conserto nenhum (20.8).
        velha = tuple(q for q in QUANTIFICADORES
                      if q not in ("mais comum", "mais comuns", "mais vendido",
                                   "mais vendida", "mais vendidos", "mais vendidas",
                                   "vende mais", "vendem mais", "mais popular",
                                   "mais populares", "a media", "na media", "da media"))

        def com_a_lista_velha(texto):
            t = _sem_acento_q(texto)
            return [q for q in velha
                    if q in t]

        for i, frase in enumerate(AS_TRES):
            pegos = []
            conferir_classe_no_site("/x/", frase, ())
            diz(not com_a_lista_velha(frase) and len(pegos) == 1,
                "10.7.%d a lista VELHA aprova a frase %r e a nova a reprova — as duas "
                "discordam" % (i + 1, frase[:40]))
    finally:
        afirma = afirma_de_verdade

    # MUNDO 11 — A FOLHA SERVIDA E A 32.4 NO BYTE SERVIDO (bloco 7, 04/11/2026).
    # As duas funcoes sao puras, entao esta metade roda SEMPRE, sem rede.
    #
    # O MUNDO 1 DESTA PARTE E O MUNDO DE VERDADE: a folha da casca como ela
    # estava no ar as 19h2xZ de 04/11/2026 — um comentario que nomeia a rotina
    # `conferir-32-5-no-navegador.mjs`, outro que diz `bancada`, e numero de
    # secao do contrato. A pagina tinha 17 blocos `<style>` do proprio
    # WordPress ao lado, e NENHUM deles pode fazer este portao reprovar.
    wp = ('<style id="wp-block-library-inline-css">/*! normalize */.wp-x{color:red}</style>'
          '<style id="global-styles-inline-css">/* auto-generated */body{margin:0}</style>')
    doente = ('<html><head>' + wp + '<style id="rodametria-casca">\n'
              '/* MEDIDO NO AR a 390 px pelo conferir-32-5-no-navegador.mjs, e a bancada\n'
              '   desta ilha roda o portao da secao 32.5 depois. */\n'
              'body.rdm{margin:0}\n</style></head><body><p>Faz uns 35 km.</p></body></html>')
    sao = ('<html><head>' + wp + '<style id="rodametria-casca">\n'
           'body.rdm{margin:0}\n</style></head><body><p>Faz uns 35 km.</p></body></html>')

    diz(len(folhas_da_ilha(doente)) == 1,
        "11.1 das 3 folhas servidas so 1 e desta ilha — as 2 do WordPress ficam de fora, "
        "porque esta ilha nao pode consertar o que nao escreve")
    diz(len(problemas_da_folha_servida(doente)) == 1,
        "11.2 a folha DOENTE e pega: comentario de CSS dentro da folha desta ilha")
    diz(problemas_da_folha_servida(sao) == [],
        "11.3 a folha SA passa, com os comentarios do WordPress intactos ao lado — portao "
        "que reprova a pagina certa e o caminho mais curto para alguem ignora-lo (20.5)")
    bast = problemas_de_bastidor_no_servido(doente, ("conferir-32-5-no-navegador.mjs",))
    diz(any("bancada" in m for m in bast),
        "11.4 a palavra de bastidor dentro do COMENTARIO da folha e pega pela 32.4 no servido")
    diz(any(".mjs" in m for m in bast),
        "11.5 a extensao de rotina dentro da folha e pega")
    diz(any("conferir-32-5-no-navegador.mjs" in m for m in bast),
        "11.6 o NOME do arquivo desta pasta dentro da folha e pego")
    diz(problemas_de_bastidor_no_servido(sao, ("conferir-32-5-no-navegador.mjs",)) == [],
        "11.7 a pagina SA passa na 32.4 do servido")

    # E A REGUA VELHA REFEITA AO LADO DA NOVA: a velha le o TEXTO VISIVEL, e
    # `corpo_da_pagina()` tira `<style>` antes de medir — entao ela APROVA a
    # pagina doente. As duas tem de discordar, senao este mundo nao mede o
    # conserto (20.8).
    def regua_velha_do_bastidor(html):
        corpo = corpo_da_pagina(html)
        texto = re.sub(r"<[^>]+>", " ", corpo)
        return [t for t in BASTIDOR if t.lower() in texto.lower()]

    diz(regua_velha_do_bastidor(doente) == [] and bast != [],
        "11.8 a regua VELHA (texto visivel) APROVA a pagina doente e a NOVA (byte servido) a "
        "REPROVA — as duas discordam, senao este autoteste nao mede o conserto")

    # MUNDO 11-b — O ROTEIRO SERVIDO, E ELE E O MUNDO DE VERDADE DE 11/11/2026.
    #
    # O comentario abaixo e o que a home servia as 13h2xZ, letra por letra: ele
    # nomeia OUTRA ILHA do arquipelago. Ao lado vao os roteiros do proprio
    # WordPress, com comentario dentro, e NENHUM deles pode fazer este portao
    # reprovar — e a licao da folha de 04/11 aplicada ao roteiro.
    wpjs = ('<script id="wp-importmap" type="importmap">/* gerado */{"imports":{}}</script>'
            '<script id="@wordpress/block-library/navigation/view-js-module">'
            '// modulo do tema\nvar a=1;</script>')
    rot_doente = ('<html><head>' + wpjs
                  + '<script type="application/ld+json">{"@type":"WebPage"}</script>'
                  + '<script id="rodametria-f1-js">\n(function(){\n'
                  + '  /* A RESSALVA DO PICO. O molde do zero existe porque o mundo de hoje\n'
                  + '     e o do zero, e "e 0 declaram o nominal" e o plural que mente — a\n'
                  + '     cicatriz que a clubedomosaico pagou em 12/10/2026. */\n'
                  + '  var u = "https://s.shopee.com.br/a";\n})();\n</script>'
                  + '</head><body><p>Faz uns 35 km.</p></body></html>')
    rot_sao = ('<html><head>' + wpjs
               + '<script type="application/ld+json">{"@type":"WebPage"}</script>'
               + '<script id="rodametria-f1-js">\n(function(){\n'
               + '  var u = "https://s.shopee.com.br/a";\n})();\n</script>'
               + '</head><body><p>Faz uns 35 km.</p></body></html>')

    diz(len(roteiros_da_ilha(rot_doente)) == 1,
        "11.9 dos 4 roteiros servidos so 1 e desta ilha — os 2 do WordPress e o JSON-LD "
        "ficam de fora, porque esta ilha nao escreve os dois primeiros e o terceiro nao e "
        "codigo")
    diz(len(problemas_do_roteiro_servido(rot_doente)) == 1,
        "11.10 o roteiro DOENTE e pego: comentario de JavaScript dentro do roteiro desta ilha")
    diz(problemas_do_roteiro_servido(rot_sao) == [],
        "11.11 o roteiro SAO passa, com os comentarios do WordPress intactos ao lado — e a "
        "URL com `//` DENTRO DE STRING nao e lida como comentario de linha (20.5)")
    bast_rot = problemas_de_bastidor_no_servido(rot_doente)
    diz(any("clubedomosaico" in m for m in bast_rot),
        "11.12 o nome de OUTRA ILHA dentro do comentario do roteiro e pego pela 32.4 no servido")
    diz(problemas_de_bastidor_no_servido(rot_sao) == [],
        "11.13 a pagina de roteiro SAO passa na 32.4 do servido")
    diz(regua_velha_do_bastidor(rot_doente) == [] and bast_rot != [],
        "11.14 a regua VELHA (texto visivel) APROVA a pagina de roteiro doente e a NOVA a "
        "REPROVA — foi exatamente esta fenda que guardou o defeito por sete dias")

    # MUNDO 11-b-ii — A PALAVRA `ilha` E A PALAVRA `publicavel` NA PROSA DE
    # LEITOR (itens 2 e 3 do despacho de 11/11/2026), E OS MUNDOS 1 SAO O QUE
    # ESTAVA NO AR, letra por letra.
    #
    # A trilha de migalhas VAI em todos eles, porque e ela que a regua velha nao
    # saberia poupar: `ilha` esta dentro de `trilha`, e a 16.3 exige a trilha nas
    # 10 paginas. Portao que reprovasse a trilha reprovaria o CERTO (20.5).
    trilha = ('<nav aria-label="Trilha"><a href="/">Rodametria</a> › '
              '<a href="/veiculos/">Veiculos</a> › <span>Patinete</span></nav>')
    texto_doente_ilha = (trilha + '<p>Se um numero desta ilha esta errado, ele vale menos '
                         'que a fonte que o contradiz.</p>')
    texto_sao_ilha = (trilha + '<p>Se um numero deste site esta errado, ele vale menos '
                      'que a fonte que o contradiz.</p>')
    # E O MUNDO DA F2, COM ACENTO — que e o detalhe que fez a lista de cima
    # falhar: ela tinha `publicavel` e o ar servia `publicável`.
    texto_doente_publicavel = (trilha + '<p>Consumo de um patinete por km — sem valor '
                               'publicável. Tipo: pendente, sem valor publicado.</p>')
    texto_sao_publicavel = (trilha + '<p>Consumo de um patinete por km — não publicamos '
                            'nenhum valor, e o motivo está nesta lista.</p>')

    p_ilha = problemas_de_bastidor_com_fronteira(texto_doente_ilha, "/contato/")
    diz(len(p_ilha) == 1 and "/contato/" in p_ilha[0],
        "11.14-b a palavra `ilha` na prosa de leitor e pega, UMA vez, e a linha NOMEIA a "
        "pagina — plantar `desta ilha` numa das cinco paginas reprova, que e o que o item "
        "2 do despacho pede")
    diz(problemas_de_bastidor_com_fronteira(texto_sao_ilha, "/contato/") == [],
        "11.15-b a mesma pagina com `deste site` passa — e a TRILHA de migalhas, com cinco "
        "`trilha` dentro, NAO reprova nenhuma das duas: `ilha` dentro de `trilha` nao e "
        "ocorrencia, e e por isso que esta regua e de fronteira de palavra")
    p_pub = problemas_de_bastidor_com_fronteira(texto_doente_publicavel, "/autonomia/")
    diz(len(p_pub) == 2,
        "11.16-b a linha da F2 que estava no ar e pega DUAS vezes — `publicável` (com "
        "acento, que a lista sem acento nao pegava) e o rotulo `Tipo:`")
    diz(problemas_de_bastidor_com_fronteira(texto_sao_publicavel, "/autonomia/") == [],
        "11.17-b a mesma prestacao de contas em portugues de leitor passa")
    # E A REGUA VELHA AO LADO DA NOVA, nos dois mundos: ela e a lista de
    # substring crua, e nos DOIS ela APROVA o que a nova reprova. Sem esta
    # discordancia o autoteste nao mede conserto nenhum (20.8).
    diz(regua_velha_do_bastidor('<body>' + texto_doente_ilha + '</body>') == [] and p_ilha != [],
        "11.18-b a regua VELHA APROVA a pagina com `desta ilha` (a palavra nao estava na "
        "lista) e a NOVA a reprova — as duas discordam")
    diz(regua_velha_do_bastidor('<body>' + texto_doente_publicavel + '</body>') == []
        and p_pub != [],
        "11.19-b a regua VELHA APROVA `publicável` com acento MESMO TENDO `publicavel` na "
        "lista desde que ela nasceu — e a NOVA reprova. Esta e a fenda exata do item 3: o "
        "termo estava na lista e o acento o atravessava")

    # MUNDO 11-c — O ARTIGO DA LOJA, e o mundo 1 e a frase que estava no ar.
    diz(len(problemas_de_artigo_da_loja(
            ["R$ 8.244,00 lido na Mercado Livre em 27/10/2026 — o botao abre a Shopee"])) == 1,
        "11.15 a frase que estava no ar as 13h2xZ de 11/11/2026 e pega — e so uma vez, "
        "porque `a Shopee` na mesma frase esta CERTO")
    diz(problemas_de_artigo_da_loja(
            ["R$ 8.244,00 lido no Mercado Livre em 27/10/2026 — o botao abre a Shopee"]) == [],
        "11.16 a frase CERTA das duas lojas passa")
    diz(len(problemas_de_artigo_da_loja(["lido no Shopee em 27/10/2026"])) == 1,
        "11.17 o espelho do defeito (masculino na Shopee) tambem e pego — regua que so "
        "conhece o erro de hoje nao pega o de amanha")
    diz(problemas_de_artigo_da_loja(
            ["na Shopee, lido em 27/10/2026", "o botao abre o Mercado Livre",
             "Os anuncios saem da busca \"patinete eletrico adulto\" na Shopee"]) == [],
        "11.18 as tres formas sadias que a ilha de fato serve passam")

    # MUNDO 12 — A PORTA CAIDA, FABRICADA, E AS DUAS REGUAS LADO A LADO.
    # Este mundo e o de 05/11/2026 as 10h2xZ nesta ilha, e ele existe porque o
    # portao que devia medir a queda entrava pela porta que cai. Os bytes
    # abaixo sao os que o hospedeiro serviu naquela leitura.
    pagina_do_hospedeiro = (
        '<!DOCTYPE html>\n<html lang="pt-BR">\n  <head>\n'
        '    <meta name="robots" content="noindex">\n'
        '    <title>Hospedagem de Site com Dominio Gratis - HostGator</title>\n'
        '  </head>\n  <body>\n    <h3>Erro 404</h3>\n  </body>\n</html>'
    )
    indice_de_verdade = json.dumps({"namespace": "rodametria/v1", "routes": {
        "/rodametria/v1": {}, "/rodametria/v1/casca": {},
        "/rodametria/v1/rotas": {}, "/rodametria/v1/status": {},
        "/rodametria/v1/sync": {}, "/rodametria/v1/token": {}}})

    # (a) A REGUA VELHA lia o indice pelo caminho bonito, entao com a porta no
    #     chao ela recebia a pagina do hospedeiro e concluia LISTA VAZIA.
    velha = rotas_do_indice(pagina_do_hospedeiro)
    nova = rotas_do_indice(indice_de_verdade)
    diz(velha == [] and ROTA_DA_293 in nova,
        "12. a regua VELHA (indice pelo caminho bonito) le a pagina do hospedeiro como "
        "ZERO rota, e a NOVA (?rest_route=) acha a rota — as duas DISCORDAM, senao este "
        "autoteste nao mede o conserto")

    # (b) E a discordancia nao e academica: ela trocava o DONO do defeito.
    acusacao_velha = problemas_da_parede(velha, 401, 401, "rodametria_rotas_token_invalido")
    acusacao_nova = problemas_da_parede(nova, 401, 401, "rodametria_rotas_token_invalido")
    diz(any("NAO aparece no indice" in m for m in acusacao_velha) and acusacao_nova == [],
        "12. com a porta caida a regua VELHA acusa a casca de nao registrar a rota (o "
        "conserto errado, no arquivo errado) e a NOVA nao acusa nada — a rota responde")

    # (c) O CONSERTO NAO AFROUXA O PORTAO: rota de verdade ausente continua pega.
    indice_sem_a_rota = json.dumps({"routes": {
        "/rodametria/v1": {}, "/rodametria/v1/casca": {}, "/rodametria/v1/status": {}}})
    ausente = problemas_da_parede(rotas_do_indice(indice_sem_a_rota), 404, 404, None)
    diz(any("NAO aparece no indice" in m for m in ausente),
        "12. rota DE VERDADE ausente segue sendo pega pela regua nova — o conserto nao "
        "afrouxou a afirmacao, so trocou a porta por onde ela entra")

    # (d) O JSON QUE NAO E DICIONARIO nao pode virar excecao nem rota inventada.
    diz(rotas_do_indice("[]") == [] and rotas_do_indice('{"routes": null}') == [],
        "12. indice que nao e dicionario, e `routes` nulo, devolvem lista vazia sem "
        "estourar — a pagina do hospedeiro nao e o unico corpo que nao e indice")

    # MUNDO 13 — O DIAGNOSTICO NOMEADO, E AS QUATRO GRANDEZAS QUE ELE EXIGE.
    # A causa so e nomeada quando as quatro estao na mesa; fora disso o portao
    # prefere nao dizer causa nenhuma (29.5: causa inventada e a proxima
    # execucao consertando a coisa errada).
    caiu = diagnostico_da_porta(200, [404, 404, 404], True)
    diz(caiu is not None and "PORTA DE ENTRADA CAIU" in caiu and "flush_rewrite_rules" in caiu,
        "13. o mundo de 05/11 e NOMEADO: home 200, as tres portas em 404, REST vivo — e a "
        "linha traz o conserto, nao so o sintoma")

    diz(diagnostico_da_porta(200, [200, 200, 200], True) is None,
        "13. o mundo SADIO nao nomeia causa nenhuma")

    diz(diagnostico_da_porta(404, [404, 404, 404], True) is None,
        "13. home TAMBEM morta nao e esta causa — o site inteiro fora do ar e outro "
        "mundo, e o portao devolve None em vez de nomear a errada")

    diz(diagnostico_da_porta(200, [404, 404, 404], False) is None,
        "13. REST morto nas DUAS formas nao e esta causa: o que esta assinatura exige e o "
        "WordPress de pe atras de uma porta fechada")

    diz(diagnostico_da_porta(200, [404, 200, 404], True) is None,
        "13. UMA das portas viva ja nao e esta assinatura — ela cobra as tres juntas, "
        "porque as tres sao rota virtual e caem juntas")

    diz(diagnostico_da_porta(200, [], True) is None,
        "13. sem porta medida nenhuma nao se nomeia causa — lista vazia nao e prova de "
        "que as portas estao mortas, e `all()` sobre vazio diria que sim")


    # MUNDO 14 — A REVISAO ATRASADA TEM QUATRO CAUSAS, NAO DUAS, E O MUNDO (c) E
    # O QUE ACONTECEU AS 19h1xZ DE 05/11/2026 NESTA ILHA.
    #
    # A regua que morava em `main()` chamava `ultimo` de "log" e dava veredito de
    # duas pontas (cache ou Sync morto). Custou OITO MINUTOS e TRES rodadas de uma
    # execucao da ilha em FOCO TOTAL, reacionando um Sync que estava saudavel.
    # Os dois motivos estao conferidos na FONTE do Sync, que esta no repositorio
    # (ilhas/robometria/snippets/robometria-sync.php, o mesmo codigo nas quatro):
    # `interval => 1800` na 530, e o retorno antecipado das 473 a 477 que grava
    # `ultimo` e NAO escreve linha de log quando nao ha nada a aplicar.
    def t(hh, mm, ss=0):
        return datetime(2026, 11, 5, hh, mm, ss)

    # (a) `ultimo` AUSENTE — o Sync nunca gravou estado.
    cod, _ = veredito_da_revisao_atrasada(None, t(19, 31), t(19, 30), True)
    diz(cod == "sync-morto",
        "14.a `ultimo` ausente e `sync-morto` — o Sync nunca rodou neste site")

    # (b) `ultimo` VELHO — passou do vencimento com folga e nao rodou.
    cod, frase = veredito_da_revisao_atrasada(t(17, 0), t(19, 31), t(19, 30), True)
    diz(cod == "sync-morto" and "nao esta disparando" in frase,
        "14.b `ultimo` de 2h31 atras, com evento de 30 min, e `sync-morto` — e o unico "
        "dos quatro vereditos que e defeito de verdade")

    # (c) O MUNDO MEDIDO: Sync VIVO, rodada ANTERIOR ao commit, raw JA servindo.
    #     `ultimo` 19:16:46, commit do manifest 19:30, medicao 19:31.
    cod, frase = veredito_da_revisao_atrasada(t(19, 16, 46), t(19, 31), t(19, 30), True)
    diz(cod == "evento-nao-vencido",
        "14.c o mundo MEDIDO as 19h3xZ de 05/11 (Sync vivo, ultima rodada ANTERIOR ao "
        "commit, raw ja servindo) e `evento-nao-vencido`, nao `cache`")
    diz("19:46:46" in frase and "NO MAIS TARDE" in frase and "PODE CAIR ANTES" in frase,
        "14.c o veredito da o TETO do proximo vencimento (`ultimo` + 1.800 s = 19:46:46) e diz, "
        "com todas as letras, que PODE CAIR ANTES — o WordPress reagenda a partir do horario "
        "AGENDADO e nao do horario em que rodou. ESTA AFIRMACAO EXISTE PORQUE A MEDICAO "
        "FALSIFICOU A PRIMEIRA VERSAO DELA: ela exigia a hora exata `19:46:46`, e a revisao "
        "entrou as 19:40:09, 6m37s antes, porque o agendamento era de 19:10:09")
    diz("REACIONAR NAO ANTECIPA" in frase,
        "14.c e diz, com todas as letras, que reacionar nao antecipa vencimento — a "
        "metade que faltava na 20.6")

    # (d) CACHE DE VERDADE: o Sync rodou DEPOIS do commit e nao pegou a revisao.
    cod, _ = veredito_da_revisao_atrasada(t(19, 31), t(19, 32), t(19, 30), True)
    diz(cod == "cache",
        "14.d Sync que rodou DEPOIS do commit e ainda nao pegou a revisao e `cache` "
        "do GitHub (20.5) — e so aqui reacionar de dois em dois e a acao certa")

    # (e) O RAW AINDA NAO SERVE: nao e do site, e nao ha o que reacionar.
    cod, _ = veredito_da_revisao_atrasada(t(19, 31), t(19, 32), t(19, 30), False)
    diz(cod == "raw-atrasado",
        "14.e com o raw ainda sem a revisao nova o veredito e `raw-atrasado` — o "
        "defeito nao e do site e reacionar o Sync nao resolve")

    # (f) O RELOGIO DIVERGENTE DENUNCIA EM VEZ DE ESCOLHER. `ultimo` vem de
    #     `current_time('mysql')`, que e hora LOCAL do site. Um site em UTC-3
    #     devolveria 16:16:46 onde este devolveu 19:16:46 — e, com a regua cega a
    #     fuso, isso viraria "Sync morto" num Sync saudavel.
    cod, frase = veredito_da_revisao_atrasada(t(16, 16, 46), t(19, 31), t(19, 30), True)
    diz(cod in ("sync-morto", "relogio-divergente"),
        "14.f `ultimo` com 3h de deriva cai num veredito nomeado e nao passa calado")
    cod, frase = veredito_da_revisao_atrasada(t(21, 0), t(19, 31), t(19, 30), True)
    diz(cod == "relogio-divergente" and "DENUNCIA" in frase,
        "14.f `ultimo` NO FUTURO e `relogio-divergente` e DENUNCIA — adivinhar fuso "
        "aqui trocaria `Sync morto` por `Sync vivo` nos dois sentidos")

    # (g) A DISCORDANCIA QUE A 20.8 EXIGE: no mundo medido, a regua VELHA manda
    #     reacionar e a NOVA manda esperar. Se as duas concordassem, este mundo
    #     nao estaria medindo o conserto.
    def regua_velha(ultimo, agora):
        """A de duas pontas, como estava em main(): `ultimo` recente = cache."""
        return "cache" if (agora - ultimo).total_seconds() < 1800 else "sync-morto"

    velha = regua_velha(t(19, 16, 46), t(19, 31))
    nova, _ = veredito_da_revisao_atrasada(t(19, 16, 46), t(19, 31), t(19, 30), True)
    diz(velha == "cache" and nova == "evento-nao-vencido",
        "14.g a regua VELHA diz `cache` (e manda reacionar de dois em dois) e a NOVA diz "
        "`evento-nao-vencido` (e manda esperar o vencimento) no MESMO mundo — as duas "
        "DISCORDAM, senao este autoteste nao mede o conserto. A discordancia vale os "
        "oito minutos que a execucao de 05/11 gastou reacionando")

    # (h) E O CONSERTO NAO AFROUXA O PORTAO: revisao atrasada continua FALHA nos
    #     quatro vereditos. Nenhum deles e aprovacao.
    diz(all(veredito_da_revisao_atrasada(u, t(19, 31), c, r)[0] in (
            "sync-morto", "relogio-divergente", "raw-atrasado", "evento-nao-vencido", "cache")
            for u, c, r in ((None, t(19, 30), True), (t(17, 0), t(19, 30), True),
                            (t(19, 16, 46), t(19, 30), True), (t(19, 31), t(19, 30), True),
                            (t(19, 31), t(19, 30), False))),
        "14.h os quatro vereditos sao CAUSAS e nenhum e aprovacao — revisao atrasada "
        "segue sendo falha, e o que muda e o que a proxima pessoa faz")

    # ======================================================================
    # MUNDO 15 — O BOTAO DO FORMULARIO RESPONDE 200, E NAO "CHEGA EM 200"
    # (item 5 do despacho de 09/11/2026).
    #
    # FUNCAO PURA, mundos FABRICADOS, pela mesma razao da 20.9 nesta mesma
    # ferramenta: esperar que o salto aconteca para medi-lo e esperar que o
    # defeito volte ao ar.
    # ======================================================================
    HOME = "https://rodametria.com.br/?rdm_w=500&rdm_kmh=32&rdm_acel=manual&rdm_mun=&v=1"
    CANON = "https://rodametria.com.br/?rdm_w=500&rdm_kmh=32&rdm_acel=manual&rdm_mun&v=1"

    # (a) O MUNDO MEDIDO: a home de hoje, 301 para a propria URL canonicalizada.
    diz(veredito_do_botao(HOME, 301, CANON) == "ok",
        "15.a o 301 do par vazio para a PROPRIA URL canonicalizada e `ok` — e o "
        "`redirect_canonical` do WordPress, medido tambem com `?foo=`, e nenhum atributo "
        "de HTML impede o navegador de enviar `chave=` num campo de texto vazio")

    # (b) 200 e `ok`, e e o caso da F2, da F3 e da home sem o campo vazio.
    diz(veredito_do_botao(HOME.replace("&rdm_mun=", ""), 200, "") == "ok",
        "15.b 200 e `ok`")

    # (c) O CASO PERIGOSO: salto para OUTRO lugar. E aqui que o conserto nao
    #     afrouxa nada — era exatamente isto que o portao, seguindo o 301, nao
    #     podia distinguir do caso (a).
    for destino, oquee in (
            ("https://rodametria.com.br/autonomia-patinete-eletrico/", "outra PAGINA"),
            ("https://rodametria.com.br/?rdm_w=500&v=1", "a URL com CAMPOS A MENOS"),
            ("https://rodametria.com.br/?rdm_w=500&rdm_kmh=32&rdm_acel=manual&rdm_mun=&v=1",
             "a MESMA URL (cadeia que nao termina)"),
            ("", "nenhum Location")):
        diz(veredito_do_botao(HOME, 301, destino) != "ok",
            "15.c 301 para %s REPROVA" % oquee)

    # (d) 404 e 0 continuam reprovando, e e o defeito de 06/11 (o campo `w`
    #     colidindo com query var do WordPress) que nasceu esta afirmacao.
    diz(veredito_do_botao(HOME, 404, "") != "ok", "15.d 404 REPROVA (o `w=500` de 06/11)")
    diz(veredito_do_botao(HOME, 0, "") != "ok", "15.d codigo 0 (rede) REPROVA")

    # (e) A NORMALIZACAO: `chave=` vira `chave`, e `chave=valor` nao se toca.
    diz(normalizar_par_vazio(HOME) == CANON, "15.e o par vazio e normalizado")
    diz(normalizar_par_vazio("https://x/?a=1&b=2") == "https://x/?a=1&b=2",
        "15.e par com valor nao e tocado")
    diz(normalizar_par_vazio("https://x/sem-query") == "https://x/sem-query",
        "15.e URL sem query nao e tocada")
    diz(normalizar_par_vazio("https://x/?a=&b=&c=3") == "https://x/?a&b&c=3",
        "15.e DOIS pares vazios sao normalizados, e o terceiro fica")

    # (f) A DISCORDANCIA QUE TORNA ISTO MEDICAO (20.8). A regua VELHA era "o
    #     codigo do FIM DA CADEIA": ela recebia 200 e aprovava. A nova ve o 301.
    #     No caso (a) as duas concordam no veredito final e DISCORDAM no que
    #     mediram; no caso (c) elas discordam no VEREDITO, e e esse que importa.
    def regua_velha_segue(codigo_do_fim):
        return "ok" if codigo_do_fim == 200 else "reprova"

    diz(regua_velha_segue(200) == "ok" and veredito_do_botao(HOME, 301, CANON) == "ok",
        "15.f no caso canonico as duas chegam a `ok` — mas a velha o fez sem NUNCA ter "
        "visto o 301, e e por isso que ela nao podia distinguir o caso de baixo")
    diz(regua_velha_segue(200) == "ok"
        and veredito_do_botao(HOME, 301, "https://rodametria.com.br/outra/") != "ok",
        "15.f e no salto para OUTRA pagina a velha APROVA (o fim da cadeia e 200) e a nova "
        "REPROVA — as duas DISCORDAM, e essa discordancia e todo o valor do item 5")

    # (g) E A EXIGENCIA CRUA DE 200 REPROVA A HOME COMO ELA ESTA HOJE, que e o
    #     que o despacho manda provar antes de qualquer escolha: *"portao que nao
    #     reprova o defeito conhecido nao esta medindo nada"*.
    # O MECANISMO, e nao a aritmetica: `301 != 200` seria afirmacao que passa
    # sempre, e portao inerte e o que o proprio `bancada.py` desta ilha denuncia
    # por nome. O que da para medir sem rede e se o abridor REALMENTE nao segue.
    diz(_SemSeguir().redirect_request(None, None, 301, "", {}, "https://x/") is None,
        "15.g o abridor sem-seguir devolve None em `redirect_request`, que e como o urllib "
        "para de seguir. Sem isto a afirmacao da 32.1-b voltaria a medir `chega em 200`")
    diz(_ABRIDOR_SEM_SEGUIR is not urllib.request.urlopen
        and any(isinstance(h, _SemSeguir) for h in _ABRIDOR_SEM_SEGUIR.handlers),
        "15.g e o abridor usado por `buscar(seguir=False)` e o que carrega esse tratador")

    # E A MEDICAO NO AR, que nao cabe em autoteste e esta aqui escrita porque e
    # ela que justifica a escolha: as 16h2xZ de 09/11/2026 a URL do botao da home
    # respondeu 301 em tres passadas iguais (`x-redirect-by: WordPress`), e o
    # controle sem o campo vazio respondeu 200 nas mesmas tres; `?foo=` tambem
    # respondeu 301, o que prova que a causa e canonicalizacao e NAO colisao com
    # query var. A exigencia crua de 200 REPROVA a home como ela esta hoje — foi
    # medida antes de qualquer conserto, como o despacho manda —, e a escolha da
    # Fundacao foi NOMEAR esse unico salto em vez de exigir do HTML uma coisa que
    # o HTML nao pode dar.

    # =====================================================================
    # MUNDO 16 — O VOCABULARIO DA TELA, E O PRIMEIRO MUNDO E O AR DE VERDADE
    # (10/11/2026)
    # =====================================================================
    #
    # Os dois elementos abaixo sao copiados LETRA POR LETRA do HTML servido as
    # 13h2xZ de 10/11/2026, revisao 74, pela execucao que escreveu esta regua.
    AR_74_TIPO_CRU = (
        "Maior carga maxima que vimos no varejo — 120 . Tipo: "
        "observacao_de_mercado. Fichas de varejo lidas em extra.com.br, "
        "casasbahia.com.br e magazineluiza.com.br, mais o painel de afiliado da "
        "Shopee, em 27 e 28/10/2026. Lido em 28/10/2026.")
    AR_74_PRIVACIDADE_CRUA = (
        "Google, que serve as fontes da letra desta pagina em toda pagina, por "
        "fonts.googleapis.com e fonts.gstatic.com. Shopee, que serve a foto do "
        "produto, quando a pagina tem uma nas paginas com foto de produto, por "
        "cf.shopee.com.br.")

    if _REGUA_DE_AFIRMACAO is None:
        diz(False, "16. a regua de vocabulario de tela NAO pode ser medida: o irmao "
                   "`teste-afirmacao-de-tela.py` nao carregou")
    else:
        m16 = problemas_de_vocabulario_servido("ar74", [AR_74_TIPO_CRU], [])
        diz(any("sublinhado" in f for f in m16),
            "16. a chave `observacao_de_mercado` DENTRO da frase de procedencia "
            "reprova pela regua de sublinhado")
        m16b = problemas_de_vocabulario_servido("ar74", [AR_74_PRIVACIDADE_CRUA], [])
        diz(any("pagina" in f and "sem acento" in f for f in m16b),
            "16. os `pagina` sem acento da /privacidade/ reprovam pela regua de acento")

        # AS DUAS SUPERFICIES DISCORDAM, e e isso que prova o conserto (20.8).
        # A regua que ja existia neste portao media HABILITACAO e PESO, e as
        # duas frases acima nao falam de nenhum dos dois: ela reprovava em ZERO.
        velha16 = (_REGUA_DE_AFIRMACAO.problemas_de_habilitacao("x", [AR_74_TIPO_CRU])
                   + _REGUA_DE_AFIRMACAO.problemas_de_peso("x", [AR_74_TIPO_CRU])
                   + _REGUA_DE_AFIRMACAO.problemas_de_habilitacao(
                       "x", [AR_74_PRIVACIDADE_CRUA])
                   + _REGUA_DE_AFIRMACAO.problemas_de_peso("x", [AR_74_PRIVACIDADE_CRUA]))
        diz(not velha16,
            "16. e as reguas que este portao JA TINHA reprovam os dois mundos em "
            "ZERO — as duas discordam, senao o conserto nao existiria (20.8)")

        # MUNDO 16b — A CITACAO PASSA, E ELA E O TESTE QUE IMPORTA. Contorcer a
        # copia para agradar regua errada e pior que a regua errada; aqui o que
        # nao pode ser contorcido e o ANUNCIO, citado letra por letra.
        titulo = ("Bicicleta Elétrica Ebike M2 800w Litio 48v 43kmh Scooter eletrica "
                  "Trabalho adulto bike eletrica  E")
        elemento = titulo.replace("  E", " E") + " E declara watt, sem dizer se é nominal"
        diz(problemas_de_vocabulario_servido("x", [elemento], []),
            "16b. sem desconto, o titulo do anuncio REPROVA por `eletric` — e e por "
            "isso que o desconto existe")
        diz(not problemas_de_vocabulario_servido("x", [elemento], [titulo]),
            "16b. com a citacao descontada, o MESMO elemento passa — e o espaco "
            "DOBRADO do dado contra o espaco unico do ar nao impede o desconto")

        # MUNDO 16c — O DESCONTO E POR LITERAL E NAO POR ELEMENTO. Defeito ao
        # LADO da citacao continua sendo pego; se o desconto pulasse o elemento
        # inteiro, a frase da ilha pegaria carona no titulo do anuncio.
        vizinho = titulo.replace("  E", " E") + " e esta pagina nao tem acento"
        falhas16c = problemas_de_vocabulario_servido("x", [vizinho], [titulo])
        diz(any("pagina" in f for f in falhas16c),
            "16c. defeito AO LADO da citacao e pego: o desconto remove a cadeia, "
            "nunca o elemento")

        # MUNDO 16d — O SUBLINHADO NAO TEM FALSO POSITIVO MEDIDO, e a frase certa
        # da tela passa.
        diz(not problemas_de_vocabulario_servido(
                "x", ["A faixa que a gente observou no varejo, numa data."], []),
            "16d. a frase de leitor que substituiu a chave passa limpa")

        # =================================================================
        # MUNDO 17 — O TEXTO QUE VIVE EM ATRIBUTO, E O PRIMEIRO MUNDO E O AR
        # DE VERDADE (10/11/2026, 16h3xZ)
        # =================================================================
        #
        # As duas celulas abaixo sao copiadas LETRA POR LETRA do HTML servido
        # as 16h2xZ de 10/11/2026 por `/veiculos/patinete-eletrico/`, revisao
        # 76 — a pagina servia a de cima NOVE vezes e a de baixo UMA.
        AR_76_CELULA_FRASE_NOSSA = (
            '<td class="rdm-tabela-carga" title="o titulo nao declara nenhum kg">'
            'o título não declara</td>')
        AR_76_CELULA_NORMALIZADA = (
            '<td class="rdm-tabela-carga" title="suporta ate 150kg">até 150 kg</td>')
        # E O QUE A PAGINA SERVE AO LADO, que NAO pode fazer o portao reprovar:
        # o `<link>` do WordPress, o `<meta>` de maquina, e o `alt` que e o
        # titulo do anuncio citado letra por letra.
        TITULO_DO_ANUNCIO = ("Patinete Elétrico Adulto 350W – Alta Velocidade, "
                             "Bateria Longa e Suporta Até 150kg")
        AO_LADO = (
            '<link rel="alternate" title="Feed para Rodametria &#187;" href="/feed/">'
            '<link rel="EditURI" title="RSD" href="/xmlrpc.php?rsd">'
            '<link rel="alternate" title="oEmbed (JSON)" href="/x">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            '<meta name="generator" content="WordPress 7.1.4">'
            '<meta name="theme-color" content="#13212B">'
            '<meta property="og:locale" content="pt_BR">'
            '<img src="/x.jpg" alt="' + TITULO_DO_ANUNCIO + '">')

        _attr_doente = textos_de_atributo(
            AR_76_CELULA_FRASE_NOSSA + AR_76_CELULA_NORMALIZADA + AO_LADO)
        _attr_doente_textos = [t for _o, t in _attr_doente]
        m17 = problemas_de_vocabulario_servido(
            "ar76", _attr_doente_textos, [TITULO_DO_ANUNCIO])
        diz(any("titulo" in f and "sem acento" in f for f in m17),
            "17.1 o `title` da celula de carga com a FRASE NOSSA sem acento reprova — "
            "e o defeito que estava no ar em 2 das 10 URLs")
        diz(any("ate" in f for f in m17),
            "17.2 o `title` com a NORMALIZACAO do pedaco (`suporta ate 150kg`, onde o "
            "anuncio escreve `Suporta Até 150kg`) reprova pelo `ate` por palavra inteira")

        # A SUPERFICIE NAO ALCANCA O QUE NAO E DESTA ILHA, e isto e medido e nao
        # declarado: `<link title>` e `<meta>` de maquina ficam FORA, senao o
        # portao reprovaria as dez URLs por texto que a fabrica nao escreve.
        diz(not any("Feed para Rodametria" in t or "RSD" in t or "oEmbed" in t
                    for t in _attr_doente_textos),
            "17.3 o `title` dos `<link>` do WordPress NAO entra na superficie")
        diz(not any(t.startswith("width=device-width") or t == "WordPress 7.1.4"
                    or t == "#13212B" or t == "pt_BR" for t in _attr_doente_textos),
            "17.4 o `content` de `<meta>` de maquina NAO entra: so description e og:")
        diz(TITULO_DO_ANUNCIO in _attr_doente_textos,
            "17.5 o `alt` da foto ENTRA na superficie (e texto que o leitor de tela le)")
        diz(not problemas_de_vocabulario_servido(
                "x", [TITULO_DO_ANUNCIO], [TITULO_DO_ANUNCIO]),
            "17.6 e ele passa com a citacao descontada, apesar do `Elétrico`/`eletric`")

        # A `description` E MEDIDA, porque e texto de leitor servido no resultado
        # de busca — e so ela e o par `og:` entre os `<meta>`.
        _desc = textos_de_atributo(
            '<meta name="description" content="o titulo nao declara nada">'
            '<meta property="og:title" content="Patinete elétrico">')
        diz([o for o, _t in _desc] == ["meta[description]", "meta[og:title]"],
            "17.7 `description` e `og:title` entram, e so eles")
        diz(problemas_de_vocabulario_servido("x", [t for _o, t in _desc], []),
            "17.8 e a `description` sem acento REPROVA, como qualquer texto de tela")

        # E A REGUA VELHA REFEITA AO LADO DA NOVA: a de PROSA recorta o miolo das
        # marcacoes e joga as marcacoes fora — ela APROVA as duas celulas doentes,
        # porque o texto visivel delas (`o título não declara`, `até 150 kg`) esta
        # CERTO. Autoteste em que as duas concordam nao mede conserto nenhum (20.8).
        _prosa_doente = elementos_de_prosa(
            AR_76_CELULA_FRASE_NOSSA + AR_76_CELULA_NORMALIZADA + AO_LADO)
        diz(not problemas_de_vocabulario_servido(
                "x", _prosa_doente, [TITULO_DO_ANUNCIO]) and m17 != [],
            "17.9 a regua de PROSA APROVA as duas celulas doentes e a de ATRIBUTO as "
            "REPROVA — as duas discordam, e e esta discordancia que explica por que o "
            "defeito ficou dez dias no ar debaixo de um portao verde")

        # E A CELULA CONSERTADA PASSA NAS DUAS, que e a outra metade do conserto.
        _attr_sa = textos_de_atributo(
            '<td class="rdm-tabela-carga" title="o título não declara nenhum kg">'
            'o título não declara</td>'
            '<td class="rdm-tabela-carga" title="Suporta Até 150kg">até 150 kg</td>')
        diz(not problemas_de_vocabulario_servido(
                "x", [t for _o, t in _attr_sa], [TITULO_DO_ANUNCIO]),
            "17.10 as duas celulas CONSERTADAS passam — portao que reprova a pagina "
            "certa e o caminho mais curto para alguem ignora-lo (20.5)")

        # =================================================================
        # MUNDO 18 — AS DUAS LISTAS DA 32.4 NAS DUAS SUPERFICIES DESESCAPADAS,
        # E O BYTE SERVIDO TEM DE DISCORDAR (11/11/2026, a tarde)
        # =================================================================
        #
        # O PRIMEIRO MUNDO E O AR DE VERDADE: as 10 URLs servidas as 19h2xZ de
        # 11/11/2026 deram ZERO achado nas duas superficies, e e por isso que
        # estes mundos sao FABRICADOS. Zero no ar com regua que nunca mordeu nao
        # distingue pagina sa de regua que nao roda.
        _ATTR_COM_ENTIDADE = (
            '<td class="rdm-tabela-carga" title="Tipo: public&aacute;vel">até 150 kg</td>'
            '<img src="/x.jpg" alt="foto desta &#105;lha">')
        _m18_attr = problemas_de_bastidor_em_pares(
            textos_de_atributo(_ATTR_COM_ENTIDADE), "atributo")
        diz(any("publicavel" in p for p in _m18_attr),
            "18.1 `public&aacute;vel` dentro de um `title` REPROVA — o acento escrito "
            "em entidade e a mesma palavra do enum de `status`")
        diz(any("Tipo:" in p or "rotulo de campo de banco" in p for p in _m18_attr),
            "18.2 o rotulo `Tipo:` dentro do mesmo `title` REPROVA pela lista de fronteira")
        diz(any("este site" in p for p in _m18_attr),
            "18.3 `&#105;lha` dentro de um `alt` REPROVA — o acento nao e a unica "
            "entidade que esconde palavra; o numero tambem esconde")

        # E A REGUA DO BYTE SERVIDO, QUE JA EXISTIA, APROVA OS TRES. E a
        # discordancia que a 20.8 exige: ela dobra o ACENTO e nao desfaz a
        # ENTIDADE, e `publicavel` so existe depois de desescapar.
        # E A REGUA DO BYTE SERVIDO, QUE JA EXISTIA, PERDE EXATAMENTE AS DUAS
        # PALAVRAS ESCONDIDAS EM ENTIDADE — e acha a terceira, que nao esta
        # escondida. A discordancia nao e "ela nao ve nada": e "ela ve o que esta
        # em texto cru e e cega para o que `esc_attr` escreveu", e e por isso que
        # a afirmacao e contada termo por termo em vez de no bloco todo.
        _m18_byte = problemas_de_bastidor_com_fronteira(_ATTR_COM_ENTIDADE, "byte")
        diz(any("rotulo de campo de banco" in p for p in _m18_byte),
            "18.4 o byte servido ACHA o `Tipo:`, que esta em texto cru")
        diz(not any("publicavel" in p or "este site" in p for p in _m18_byte)
                and any("publicavel" in p for p in _m18_attr)
                and any("este site" in p for p in _m18_attr),
            "18.4-b e e CEGO para `public&aacute;vel` e `&#105;lha`, que a regua de "
            "atributo reprova — a discordancia e o motivo de esta afirmacao existir")

        # O JSON-LD, com os DOIS escapes que `wp_json_encode` escreve quando as
        # bandeiras nao vao na chamada: `á` no acento e `\/` na barra. Os
        # tres termos da lista que terminam em `/` ficam cegos de uma vez.
        _LD_COM_ESCAPE = ['{"@type":"WebPage","name":"public\\u00e1vel",'
                          '"description":"lido de dados\\/veiculos.json"}']
        _m18_ld = problemas_de_bastidor_em_pares(
            valores_do_jsonld(_LD_COM_ESCAPE), "JSON-LD")
        diz(any("publicavel" in p for p in _m18_ld),
            "18.5 `\\u00e1` dentro de um valor de JSON-LD REPROVA depois do `json.loads`")
        diz(any("'dados/'" in p for p in _m18_ld),
            "18.6 `dados\\/` REPROVA pelo mesmo caminho — e e o escape que cegaria "
            "`dados/`, `ferramentas/` e `regras/` juntos")
        diz(problemas_de_bastidor_com_fronteira(_LD_COM_ESCAPE[0], "byte") == []
                and [t for t in BASTIDOR if t.lower() in _LD_COM_ESCAPE[0].lower()] == []
                and _m18_ld != [],
            "18.7 e a regua do byte aprova os dois — a mesma discordancia, do outro lado")

        # O ENDERECO VAI NA MENSAGEM, porque o conserto de cada chave mora em
        # lugar diferente e mensagem sem endereco manda alguem procurar.
        diz(any("/description" in p for p in _m18_ld),
            "18.8 a linha diz a CHAVE de dentro do bloco (`ld[0]/description`)")

        # E O AR DE VERDADE PASSA NAS DUAS, com o JSON-LD da home como ele foi
        # servido: nenhuma das duas listas pode reprovar a pagina certa (20.5).
        _LD_SAO = ['{"@context":"https://schema.org","@type":"WebSite",'
                   '"name":"Rodametria","inLanguage":"pt-BR",'
                   '"description":"Potência, velocidade e acelerador decidem se o '
                   'seu elétrico é bicicleta, autopropelido ou ciclomotor."}']
        diz(problemas_de_bastidor_em_pares(valores_do_jsonld(_LD_SAO), "JSON-LD") == [],
            "18.9 o JSON-LD da home como ele esta no ar PASSA, `@context` e `@type` "
            "inclusive — nenhuma chave e excluida da leitura")
        diz(len(valores_do_jsonld(_LD_SAO)) == 5,
            "18.10 e ela diz quantos valores leu: 5 do bloco da home, contados")
        diz(valores_do_jsonld(['{"isto nao e json']) == [],
            "18.11 bloco ilegivel nao derruba a leitura dos outros")

        # =================================================================
        # MUNDO 19 — O `alt` QUE REPETE A PROSA VIZINHA, E O MUNDO 1 E O AR
        # (11/11/2026, 19h2xZ, `/veiculos/patinete-eletrico/`)
        # =================================================================
        _AR_CARTAO_DOENTE = (
            '<li class="rdm-molde-cartao">'
            '<img class="rdm-molde-cartao-foto" src="https://cf.shopee.com.br/file/x"'
            ' width="1024" height="1024" loading="lazy" decoding="async"'
            ' alt="' + TITULO_DO_ANUNCIO + '">'
            '<p class="rdm-molde-cartao-nome">' + TITULO_DO_ANUNCIO + '</p>'
            '<p class="rdm-molde-cartao-spec">declara watt, sem dizer se é nominal '
            'ou de pico</p></li>')
        _m19 = alts_que_repetem_a_prosa_vizinha(_AR_CARTAO_DOENTE)
        diz(len(_m19) == 1 and "<p>" in _m19[0].replace("`", ""),
            "19.1 o cartao como ele estava no ar REPROVA: o `alt` e o <p> seguinte "
            "sao a mesma cadeia, e o leitor de tela diz o titulo do anuncio duas vezes")

        # O CONSERTO: `alt` vazio. A imagem e redundante porque a pagina imprime
        # o nome ao lado dela, e atributo vazio e a declaracao disso.
        _AR_CARTAO_SAO = _AR_CARTAO_DOENTE.replace(
            'alt="' + TITULO_DO_ANUNCIO + '"', 'alt=""')
        diz(alts_que_repetem_a_prosa_vizinha(_AR_CARTAO_SAO) == [],
            "19.2 com `alt=\"\"` o cartao PASSA — e `textos_de_atributo()` deixa de "
            "contar o atributo vazio, que e a verdade daquele atributo")

        # E UM `alt` QUE DESCREVE A FOTO TAMBEM PASSA: a regua mede IGUALDADE e nao
        # redacao, entao ela nao obriga o atributo a ser vazio.
        diz(alts_que_repetem_a_prosa_vizinha(_AR_CARTAO_DOENTE.replace(
                'alt="' + TITULO_DO_ANUNCIO + '"',
                'alt="patinete branco dobrado, de perfil"')) == [],
            "19.3 um `alt` que descreve a FOTO passa — a regua reprova a copia, "
            "nao o atributo")

        # E A FOTO LONGE DA PROSA PASSA: a janela e curta de proposito, porque
        # prosa distante nao e lida junto com a imagem.
        diz(alts_que_repetem_a_prosa_vizinha(
                '<img src="/x.jpg" alt="' + TITULO_DO_ANUNCIO + '">'
                + ("<div>" * 200)
                + '<p>' + TITULO_DO_ANUNCIO + '</p>') == [],
            "19.4 prosa igual a 600 caracteres de distancia NAO reprova — a janela "
            "mede vizinhanca, nao a pagina")

        # A REGUA VELHA REFEITA AO LADO: a afirmacao que esta ilha ja tinha sobre
        # `<img>` e `"alt=" in img`, e ela APROVA o cartao doente, porque o
        # atributo existe. Ela tambem aprova o consertado. Nunca mediu repeticao.
        diz(all("alt=" in i for i in re.findall(r"<img[^>]*>", _AR_CARTAO_DOENTE))
                and _m19 != [],
            "19.5 a afirmacao velha (`<img> sem alt`) APROVA o cartao doente e a nova "
            "o REPROVA — a discordancia que a 20.8 exige")

        # =================================================================
        # MUNDO 20 — A CONCORDANCIA DA ORACAO DE SUJEICAO, E O MUNDO 1 E O AR
        # (11/11/2026, 19h2xZ, home, nas DUAS camadas)
        # =================================================================
        #
        # A frase abaixo e copiada LETRA POR LETRA da resposta de `FAQPage`
        # servida pela home as 19h2xZ de 11/11/2026, e a mesma celula aparecia
        # na tabela visivel tres dobras acima.
        AR_FAQ_DOENTE = ("Pela Resolução Contran nº 996/2023, quando o motor auxiliar "
                         "tem até 1.000 W de potência nominal, a velocidade do motor "
                         "não passa de 32 km/h, o veículo só funciona quando a pessoa "
                         "pedala e ele não tem acelerador. Nessa categoria, o art. 12 "
                         "diz que o veículo não é sujeita a registro, licenciamento "
                         "nem placa.")
        _m20, _s20 = problemas_de_concordancia_da_sujeicao([AR_FAQ_DOENTE], "/")
        diz(len(_m20) == 1 and "sujeita" in _m20[0],
            "20.1 a resposta de `FAQPage` como ela estava no ar REPROVA: `o veículo` "
            "e masculino e a celula da tabela diz `sujeita`")

        # O CONSERTO E DA FRASE: ela passa a nomear a categoria de que fala, e os
        # dois sujeitos passam a ser o mesmo. O DADO nao muda.
        AR_FAQ_SAO = AR_FAQ_DOENTE.replace("que o veículo não é sujeita",
                                           "que a bicicleta elétrica não é sujeita")
        diz(problemas_de_concordancia_da_sujeicao([AR_FAQ_SAO], "/")[0] == [],
            "20.2 com a categoria nomeada a mesma celula PASSA — o conserto nao "
            "toca o campo `placa` da tabela")

        # E A OUTRA PONTA, QUE E COMO ESTE DEFEITO VOLTARIA: trocar o DADO para
        # `sujeito` consertaria a frase antiga e quebraria a linha da tabela.
        diz(problemas_de_concordancia_da_sujeicao(
                ["a bicicleta elétrica não é sujeito a registro, licenciamento nem placa"],
                "/")[0] != [],
            "20.3 `a bicicleta elétrica não é sujeito` tambem REPROVA — a regua nao "
            "decidiu que `sujeita` e sempre errado, ela mede concordancia")

        # AS DUAS FRASES CERTAS QUE A HOME JA SERVIA passam, e e isso que separa
        # esta regua de um termo proibido.
        diz(problemas_de_concordancia_da_sujeicao(
                ["Pelo art. 12, ele não é sujeito a registro, licenciamento nem placa.",
                 "A resolução diz, no art. 12, que não é sujeito a registro, a "
                 "licenciamento nem a emplacamento para circular nas vias."],
                "/")[0] == [],
            "20.4 as duas oracoes CERTAS que a home ja servia passam")

        # E A CELULA SOZINHA — como a TABELA a serve, sem sujeito na frase — nao
        # reprova: vira linha de REGISTRO. Regua que aprova o que nao reconheceu
        # e pior que regua que nao roda.
        _m20c, _s20c = problemas_de_concordancia_da_sujeicao(
            ["não é sujeita a registro, licenciamento nem placa"], "/")
        diz(_m20c == [] and len(_s20c) == 1,
            "20.5 a celula sozinha, como a tabela a serve, nao reprova e e RELATADA — "
            "ali o sujeito e a linha da tabela, que nao esta na frase")

        print("conferir-no-ar --autoteste: %d de %d afirmacoes, %d falha(s)"
          % (len(ok), len(ok) + len(mal), len(mal)))
    for m in mal:
        print("  REPROVADO: %s" % m)
    print("APROVADO" if not mal else "REPROVADO")

    return 1 if mal else 0


if __name__ == "__main__":
    sys.exit(autoteste() if "--autoteste" in sys.argv else main())
