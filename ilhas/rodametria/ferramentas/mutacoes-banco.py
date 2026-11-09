#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bateria de mutacao do validador do banco da Rodametria.

    python3 ferramentas/mutacoes-banco.py
    python3 ferramentas/mutacoes-banco.py --lista

Portao escrito sem bateria que prove que ele MORDE e portao que ninguem sabe se funciona — a
licao mais cara da Robometria nao foi uma regua errada, foi uma regua certa que nunca rodou.
Esta bateria tem quatro familias:

  MUNDOS QUE TEM DE PASSAR — o banco de hoje, o banco VAZIO, um registro publicavel completo e
  um registro no degrau 4. Portao que so reprova nao e portao: e um NAO constante.
  QUEBRAS — cada uma estraga UMA coisa e DECLARA, no proprio caso, o pedaco da frase que espera
  ouvir de volta. Mutacao que aceita qualquer reprovacao passa quando o portao reprova pelo
  motivo errado.
  MORTES DO ESQUEMA — a 26.2: chave que some do esquema tem de MATAR o portao, nunca faze-lo
  aprovar em silencio. Estas mutacoes nao estragam registro nenhum.
  AUTOTESTE DA BATERIA — um validador de mentira, que aprova tudo, tem de fazer esta bateria
  reprovar. Sem isto, uma bateria quebrada diz 0 falha(s) e ninguem sabe.
"""
import copy
import json
import sys
import importlib.util
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("vb", RAIZ / "ferramentas/validar-banco.py")
VB = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(VB)

# O GERADOR DO `nota`, IMPORTADO PORQUE MUNDO FABRICADO TEM DE SER MUNDO
# CONSISTENTE (06/11/2026, com o item 5 do despacho da ronda daquele dia).
#
# Desde 06/11 o validador RECONTA, no proprio arquivo, quantos registros tem saida
# de compra e quantos estao `publicavel`, e reprova divergencia com a frase do
# `nota` — porque aquela frase afirmava *"nenhum tem saida de compra"* com QUATRO
# tendo. A consequencia aqui e direta: um mundo que MEXE NA LISTA de registros e
# deixa o `nota` do arquivo de verdade NAO e um mundo valido, e os tres "mundos
# que tem de passar" desta bateria reprovaram por isso no minuto em que o portao
# nasceu.
#
# A BATERIA IMPORTA O PRODUTOR, E ISSO NAO FERE A REGRA DA SECAO 8 ("quem confere
# escreve a propria regua, nunca chama a de quem produziu o dado"): quem confere
# aqui e `validar-banco.py`, com a propria contagem. Esta bateria nao confere o
# `nota` — ela CONSTROI o mundo, e construir um mundo coerente e trabalho de quem
# o fabrica.
_spec_db = importlib.util.spec_from_file_location("db", RAIZ / "ferramentas/derivar-banco.py")
DB = importlib.util.module_from_spec(_spec_db)
_spec_db.loader.exec_module(DB)

CASOS = []


def caso(nome, espera=None, passa=False):
    """espera = pedaco da frase que o portao tem de devolver. passa=True: mundo que nao reprova."""
    def deco(fn):
        CASOS.append((nome, espera, passa, fn))
        return fn
    return deco


def base():
    return VB.carregar(RAIZ)


def v(d, id_):
    for r in d["veiculos"]["registros"]:
        if r["id"] == id_:
            return r
    raise KeyError(id_)


def primeiro(d):
    return d["veiculos"]["registros"][0]


def nota_consistente(d):
    """Reescreve o `nota` de veiculos.json a partir dos registros DESTE mundo."""
    d["veiculos"]["nota"] = DB.nota_com_a_frase(d["veiculos"].get("nota") or "",
                                                d["veiculos"].get("registros", []))
    return d


def registro_publicavel(d):
    """Um veiculo minimo, completo e publicavel. Serve de base as quebras de compra."""
    r = copy.deepcopy(v(d, "maxshot-v1"))
    r["id"] = "caso-publicavel"
    r["afiliado"] = {
        "programa": "shopee", "degrau": 3,
        "url": "https://s.shopee.com.br/AAAAAAAAAA",
        "url_produto": "https://shopee.com.br/product/111/222",
        "par_colhido_em": "2026-10-28",
        "url_busca": "https://s.shopee.com.br/BBBBBBBBBB",
        "url_busca_produto": "https://shopee.com.br/search?keyword=patinete+eletrico+adulto",
        "encurtamento_tentado_em": "2026-10-28",
        "sub_id_1": "rodametria", "sub_id_2": "f3",
        "motivo_sem_url_produto": None, "motivo_sem_url_busca": None,
        # DECLARADO, como em todo registro desde 04/11/2026: a chave e escrita por
        # `derivar-banco.py` e recalculada pelo validador. Este caso tem o par
        # (url + url_produto), logo `false`.
        "intestavel": False,
    }
    r["status"] = "publicavel"
    r["motivo_do_status"] = "caso de teste"
    d["veiculos"]["registros"].append(r)
    return r


# ----------------------------------------------------- mundos que tem de passar
@caso("o banco de hoje, como esta no repositorio", passa=True)
def _(d):
    return d


@caso("banco VAZIO nas tres entidades", passa=True)
def _(d):
    for k in ("veiculos", "pecas", "municipios"):
        d[k]["registros"] = []
    return nota_consistente(d)


@caso("um registro publicavel completo, degrau 3 com par colhido", passa=True)
def _(d):
    registro_publicavel(d)
    return nota_consistente(d)


@caso("um registro publicavel no degrau 4, com `url` vazia", passa=True)
def _(d):
    r = registro_publicavel(d)
    r["afiliado"]["degrau"] = 4
    r["afiliado"]["url"] = None
    r["afiliado"]["url_produto"] = None
    r["afiliado"]["par_colhido_em"] = None
    return nota_consistente(d)


# --------------------------------------- o `intestavel` DECLARADO (04/11/2026)
# Tres quebras, e a segunda e a que importa: ela e o mundo em que o espelho
# envelheceu calado — o campo diz uma coisa e o par de URLs diz outra.
@caso("`afiliado.intestavel` AUSENTE num registro", "`afiliado.intestavel` AUSENTE")
def _(d):
    del primeiro(d)["afiliado"]["intestavel"]
    return d


@caso("`intestavel: false` num item que PERDEU o `url_produto`",
      "declarado False and a regra da 25.4-b diz True".replace(" and ", " e "))
def _(d):
    r = registro_publicavel(d)
    r["afiliado"]["url_produto"] = None
    r["afiliado"]["par_colhido_em"] = None
    r["afiliado"]["intestavel"] = False
    r["afiliado"]["degrau"] = 4          # para a quebra ser SO a do espelho
    r["afiliado"]["motivo_sem_url_produto"] = "CAUSA: teste. || ULTIMA TENTATIVA: teste."
    return d


@caso("`intestavel: true` sem motivo escrito", "sem `motivo_sem_url_produto`")
def _(d):
    r = registro_publicavel(d)
    r["afiliado"]["url_produto"] = None
    r["afiliado"]["par_colhido_em"] = None
    r["afiliado"]["intestavel"] = True
    r["afiliado"]["degrau"] = 4
    r["afiliado"]["motivo_sem_url_produto"] = None
    return d


# ------------------------------------------------------------- o pivo da F1
@caso("acelerador com valor null", "E o PIVO da F1 e nao aceita nulo")
def _(d):
    primeiro(d)["acelerador"] = {"valor": None, "motivo": "x"}
    return d


@caso("acelerador fora do enum", "fora do enum")
def _(d):
    primeiro(d)["acelerador"] = {"valor": "tem_acelerador", "fonte": "painel-shopee", "motivo": "x"}
    return d


@caso("acelerador na sentinela, sem motivo", "sentinela de ausencia) sem `motivo`")
def _(d):
    r = v(d, "siena-1000w-sem-cnh")
    r["acelerador"] = {"valor": "nao_declarado", "fonte": "ficha-extra"}
    return d


@caso("acelerador na sentinela, sem dizer ONDE se olhou", "dispensa o literal, nunca o registro de ONDE")
def _(d):
    r = v(d, "siena-1000w-sem-cnh")
    r["acelerador"] = {"valor": "nao_declarado", "motivo": "x", "fonte": None}
    return d


@caso("acelerador declarado sem `declarada_por` (26.1)", "nao e uma das origens legitimas de leitura")
def _(d):
    r = v(d, "maxshot-v1")
    r["acelerador"].pop("declarada_por")
    return d


@caso("acelerador declarado com `declarada_por` inventado", "nao e uma das origens legitimas de leitura")
def _(d):
    v(d, "maxshot-v1")["acelerador"]["declarada_por"] = "parece_que_tem"
    return d


# ------------------------------------------------- nominal, pico e o piso de nivel
@caso("potencia nominal com valor e sem procedencia de leitura", "nao e uma das origens legitimas")
def _(d):
    r = v(d, "maxshot-v1")
    r["potencia_nominal_w"] = {"valor": 350, "unidade": "W", "fonte": "ficha-extra",
                               "declarado_como": "350 W"}
    return d


@caso("potencia nominal vinda de DECLARACAO DE VENDEDOR (nivel 6)", "o pior nivel aceito neste campo e 5")
def _(d):
    r = v(d, "honeywhale-m2-max")
    r["potencia_nominal_w"] = {"valor": 500, "unidade": "W", "fonte": "painel-shopee",
                               "declarado_como": "500 W",
                               "declarada_por": "titulo_ou_ficha_declara_literalmente"}
    return d


@caso("velocidade de fabrica vinda de anuncio (nivel 6)", "o pior nivel aceito neste campo e 5")
def _(d):
    r = v(d, "honeywhale-h3")
    r["velocidade_max_kmh"] = {"valor": 55, "unidade": "km/h", "fonte": "painel-ml",
                               "declarado_como": "55 km/h"}
    return d


@caso("carga maxima vinda de anuncio (nivel 6)", "o pior nivel aceito neste campo e 5")
def _(d):
    r = v(d, "haixia-scooter-1000w-60v-20ah")
    r["carga_max_kg"] = {"valor": 150, "unidade": "kg", "fonte": "painel-ml",
                         "declarado_como": "150 kg"}
    return d


@caso("tensao vinda de FAZENDA (nivel 8)", "nivel 8")
def _(d):
    r = v(d, "guia-melhor-de-2026")
    r["tensao_v"] = {"valor": 60, "unidade": "V", "fonte": "guia-dos-perifericos",
                     "declarado_como": "60 V"}
    return d


# ------------------------------------------------------------- o derivado
@caso("energia_wh DIGITADA, sem tensao nem amperagem", "Wh copiado de anuncio")
def _(d):
    r = v(d, "l40-plus")
    r["energia_wh"] = {"valor": 1500, "unidade": "Wh", "derivado_de": "x"}
    return d


@caso("energia_wh discordando de V x Ah", "nao e V x Ah")
def _(d):
    r = v(d, "haixia-scooter-1000w-60v-20ah")
    r["energia_wh"]["valor"] = 1100
    return d


@caso("energia_wh certa e sem `derivado_de`", "sem `derivado_de`")
def _(d):
    r = v(d, "haixia-scooter-1000w-60v-20ah")
    r["energia_wh"].pop("derivado_de")
    return d


@caso("energia_wh null com os dois lados da conta preenchidos", "o derivado existe")
def _(d):
    r = v(d, "haixia-scooter-1000w-60v-20ah")
    r["energia_wh"] = {"valor": None, "motivo": "x"}
    return d


# ---------------------------------------------------------- categoria e a constante
#
# OS DOIS PRIMEIROS CASOS FABRICAM O MUNDO EM QUE O LIMIAR E `pendente`, E ISSO
# NAO E DETALHE: ate 06/11/2026 eles NAO fabricavam nada — liam o
# dados/constantes.json de verdade, que estava pendente, e passavam por sorte.
# No dia em que a Resolucao 996/2023 foi lida no texto oficial e a constante
# virou `publicavel`, os dois viraram VERMELHO sem que uma linha deles mudasse:
# a premissa deles tinha deixado de ser verdade. E a regra desta propria bateria
# aplicada a ela mesma — *"o mundo que o esquema permite e o banco ainda nao
# tem, e so a mutacao que PRODUZ o mundo o enxerga"*.
def _com_limiar(d, status):
    for c in d["constantes"]["constantes"]:
        if c["id"] == "limiares-categoria-contran-996-2023":
            c["status"] = status
    return d


@caso("categoria PREENCHIDA com o limiar legal pendente", "o anuncio escrevendo a regra")
def _(d):
    _com_limiar(d, "pendente")
    primeiro(d)["categoria"] = "autopropelido"
    return d


@caso("categoria null sem `motivo_categoria_null`", "sem `motivo_categoria_null`")
def _(d):
    _com_limiar(d, "pendente")
    primeiro(d).pop("motivo_categoria_null")
    return d


# ---- E OS TRES CASOS DO MUNDO DE HOJE, em que o limiar JA esta publicavel.
#
# Com a constante publicavel a trava antiga ("categoria tem de ser null")
# DESLIGA SOZINHA, e sem estes casos o campo mais perigoso do banco ficaria sem
# portao nenhum. O perigo e a tese da ilha: o numero do anuncio nao e o que a
# regra le, entao categoria escrita a mao a partir de um watt sem rotulo e o
# ANUNCIO ESCREVENDO A REGRA — e o erro e para o lado permissivo.
@caso("categoria preenchida com o limiar publicavel e SEM o watt nominal",
      "NAO classifica este registro")
def _(d):
    primeiro(d)["categoria"] = "autopropelido"
    return d


def _declara_os_tres(d, w, kmh, acel):
    """Fabrica o registro que o banco de hoje NAO TEM: um que declara os tres
    campos de entrada da F1 e portanto CLASSIFICA. Sem este mundo, a trava
    reapontada de 06/11 passaria sobre um banco em que nenhuma categoria e
    derivavel — o teste que mede a si mesmo.

    A fonte e `declarada_por` saem do proprio registro base (maxshot-v1, a unica
    fonte dele e `ficha-extra`): mutacao que inventa fonte reprova pelas OUTRAS
    reguas do portao e nao pela que ela quer medir.
    """
    r = v(d, "maxshot-v1")
    r["potencia_nominal_w"] = {"valor": w, "unidade": "W", "fonte": "ficha-extra",
                               "declarado_como": "%s W nominais" % w,
                               "declarada_por": "titulo_ou_ficha_declara_literalmente"}
    r["velocidade_max_kmh"] = {"valor": kmh, "unidade": "km/h", "fonte": "ficha-extra",
                               "declarado_como": "%s km/h" % kmh,
                               "declarada_por": "titulo_ou_ficha_declara_literalmente"}
    r["acelerador"] = {"valor": acel, "fonte": "ficha-extra", "declarado_como": acel,
                       "declarada_por": "titulo_ou_ficha_declara_literalmente"}
    return r


@caso("categoria preenchida com os tres campos e o valor ERRADO para eles",
      "O campo e DERIVADO: ele nao escolhe")
def _(d):
    # Com acelerador MANUAL nao e bicicleta eletrica, por mais baixos que sejam
    # os numeros — e o pivo da 1.1, e e justamente o erro permissivo.
    r = _declara_os_tres(d, 500, 25, "manual")
    r["categoria"] = "bicicleta_eletrica"
    return d


@caso("MUNDO QUE PASSA: categoria DERIVADA certa, com os tres campos declarados",
      passa=True)
def _(d):
    r = _declara_os_tres(d, 500, 25, "manual")
    r["categoria"] = "autopropelido"
    return d


@caso("categoria com valor fora do enum, com o limiar JA publicavel", "fora do enum")
def _(d):
    for c in d["constantes"]["constantes"]:
        if c["id"] == "limiares-categoria-contran-996-2023":
            c["status"] = "publicavel"
    primeiro(d)["categoria"] = "scooter"
    return d


# -------------------------------------------------------------- a escada de fontes
@caso("fonte cuja `origem` nao e a do `nivel` dela", "nao e a que a escada da ao nivel")
def _(d):
    primeiro(d)["fontes"]["painel-shopee"]["origem"] = "ficha-do-fabricante-lida"
    return d


@caso("fonte de nivel 2 sem `leitura` declarada", "exige `leitura` declarada")
def _(d):
    primeiro(d)["fontes"]["painel-shopee"].update(
        {"nivel": 2, "origem": "norma-lida-no-orgao", "leitura": None})
    return d


@caso("fonte com nivel que nao existe na escada", "nao existe na escada")
def _(d):
    primeiro(d)["fontes"]["painel-shopee"]["nivel"] = 99
    return d


@caso("fonte sem `data_leitura`", "falta `data_leitura`")
def _(d):
    primeiro(d)["fontes"]["painel-shopee"].pop("data_leitura")
    return d


# ------------------------------------------------------- forma dos campos e da identidade
@caso("chave de campo tecnico AUSENTE (nao null)", "esta ausente")
def _(d):
    primeiro(d).pop("carga_max_kg")
    return d


@caso("campo null sem `motivo`", "e null e nao ha `motivo`")
def _(d):
    primeiro(d)["peso_kg"] = {"valor": None}
    return d


@caso("campo com valor e sem `declarado_como` literal", "nao tem `declarado_como`")
def _(d):
    v(d, "maxshot-v1")["carga_max_kg"].pop("declarado_como")
    return d


@caso("campo apontando fonte que nao existe", "que nao esta em fontes{}")
def _(d):
    v(d, "maxshot-v1")["carga_max_kg"]["fonte"] = "inventada"
    return d


@caso("marca null sem `motivo_sem_marca`", "Null e resposta, e resposta tem motivo")
def _(d):
    v(d, "x13-chopper-1000w").pop("motivo_sem_marca")
    return d


@caso("modelo null sem `motivo_sem_modelo`", "Null e resposta, e resposta tem motivo")
def _(d):
    v(d, "playbik").pop("motivo_sem_modelo")
    return d


@caso("tipo_comercial fora do enum", "`tipo_comercial` 'ciclomotor' fora do enum")
def _(d):
    primeiro(d)["tipo_comercial"] = "ciclomotor"
    return d


@caso("id repetido", "`id` repetido")
def _(d):
    d["veiculos"]["registros"].append(copy.deepcopy(primeiro(d)))
    return d


@caso("id que nao e slug", "`id` nao e slug")
def _(d):
    primeiro(d)["id"] = "Honeywhale M2"
    return d


@caso("titulo colhido vazio", "`titulo_colhido` vazio")
def _(d):
    primeiro(d)["titulo_colhido"] = ""
    return d


@caso("chave `imagem` ausente", "a chave `imagem` esta ausente")
def _(d):
    primeiro(d).pop("imagem")
    return d


@caso("`divergencias` deixando de ser lista", "Lista vazia e AFIRMACAO")
def _(d):
    primeiro(d)["divergencias"] = None
    return d


@caso("divergencia sem `resolucao`", "sem `resolucao` escrita")
def _(d):
    primeiro(d)["divergencias"] = [{"campo": "carga_max_kg", "declaracoes": []}]
    return d


@caso("versao_esquema do arquivo divergindo do esquema", "nao bate com a do esquema")
def _(d):
    d["veiculos"]["versao_esquema"] = 99
    return d


# AS QUEBRAS DO `nota` RECONTADO (item 5 do despacho de 06/11/2026). Elas sao
# TRES porque o portao tem tres pontas, e cada uma e um jeito diferente de o campo
# voltar a mentir: a contagem errada, o nome que falta e o bloco inteiro apagado.
@caso("o `nota` afirma que NENHUM registro tem saida de compra, e quatro tem",
      "o `nota` recontado nao diz '4 deles JA tem saida de compra'")
def _(d):
    d["veiculos"]["nota"] = d["veiculos"]["nota"].replace(
        "4 deles JA tem saida de compra", "nenhum deles tem saida de compra")
    return d


@caso("o `nota` recontado deixa de NOMEAR um registro que tem saida de compra",
      "nao nomeia `ls-sport-scooter-1000w`")
def _(d):
    d["veiculos"]["nota"] = d["veiculos"]["nota"].replace(", ls-sport-scooter-1000w", "")
    return d


@caso("o bloco recontado do `nota` foi apagado e o campo voltou a ser prosa a mao",
      "o `nota` nao traz o bloco recontado da saida de compra")
def _(d):
    d["veiculos"]["nota"] = d["veiculos"]["nota"].split(
        "SAIDA DE COMPRA E PUBLICAVEIS, RECONTADOS POR")[0]
    return d


# AS QUEBRAS DA METADE *PUBLICAVEL* DO MESMO CAMPO (09/11/2026, item 2 do
# despacho de hoje). As tres de cima, de 06/11, mordiam a clausula da SAIDA DE
# COMPRA — e a frase tem DUAS clausulas. A de publicaveis ficou tres dias sem
# nenhuma quebra, derivada de uma chave booleana `publicavel` que 0 dos 17
# registros carrega: espelho e portao liam a MESMA chave ausente, os dois
# contavam zero e os dois CONCORDAVAM. O despacho pediu, com todas as letras,
# "uma quebra nova provando que a afirmacao morde ESTA clausula, nao so a
# vizinha" — e e por isso que a primeira delas e a chave que nao pode voltar a
# nascer, nao o numero.
@caso("ALGUEM INVENTA O CAMPO BOOLEANO `publicavel` num registro",
      "carrega a chave `publicavel`")
def _(d):
    # A mutacao do defeito de 06-09/11 pela RAIZ dele: com a chave existindo, a
    # pergunta "quem e publicavel" passa a ter duas respostas no mesmo arquivo.
    r = v(d, "maxshot-v1")
    r["publicavel"] = True
    return nota_consistente(d)


@caso("o `nota` afirma que NENHUM registro esta publicavel, e quatro estao",
      "a clausula de publicaveis do `nota` recontado nao e '4 dos 17 registros estao")
def _(d):
    # A FRASE EXATA que esteve no ar de 06/11 a 09/11, letra por letra.
    d["veiculos"]["nota"] = d["veiculos"]["nota"].replace(
        "4 dos 17 registros estao `publicavel` (honeywhale-m2-max, sousa-bike-aro-24, "
        "x13-chopper-1000w, ls-sport-scooter-1000w)",
        "NENHUM dos 17 registros esta `publicavel`")
    return d


@caso("o `nota` recontado deixa de NOMEAR um registro que esta publicavel",
      "a clausula de publicaveis do `nota` recontado nao e '4 dos 17 registros estao")
def _(d):
    # So a PRIMEIRA ocorrencia: a clausula de publicaveis. A segunda, da saida de
    # compra, fica intacta de proposito — se o portao cobrasse as duas de uma vez,
    # esta quebra nao provaria QUAL clausula morde.
    d["veiculos"]["nota"] = d["veiculos"]["nota"].replace(
        ", x13-chopper-1000w", "", 1)
    return d


@caso("um registro SAI de `publicavel` e o `nota` nao foi reespelhado",
      "a clausula de publicaveis do `nota` recontado nao e '3 dos 17 registros estao")
def _(d):
    # O envelhecimento de verdade: o banco anda e a frase fica. Sem nota_consistente
    # de proposito — e exatamente o mundo que o espelho conserta e o portao acusa.
    r = v(d, "sousa-bike-aro-24")
    r["status"] = "rascunho"
    r["motivo_do_status"] = "mundo fabricado pela bateria de mutacao"
    return d


@caso("status fora do enum", "`status` 'quase' fora do enum")
def _(d):
    primeiro(d)["status"] = "quase"
    return d


@caso("excluido_do_banco sem a causa escrita", "recusa que a proxima coleta repete")
def _(d):
    v(d, "guia-melhor-de-2026").pop("excluido_do_banco_por_que")
    return d


# ------------------------------------------------------------------- cotacoes
@caso("cotacao sem `data_leitura`", "Preco sem a data da leitura e proibido")
def _(d):
    primeiro(d)["cotacoes"][0].pop("data_leitura")
    return d


@caso("cotacao apontando fonte que nao existe", "cotacao aponta a fonte")
def _(d):
    primeiro(d)["cotacoes"][0]["fonte"] = "inventada"
    return d


# ----------------------------------------------------------- a escada do link de compra
@caso("publicavel SEM piso de compra", "Nao existe item publicavel sem piso")
def _(d):
    r = registro_publicavel(d)
    r["afiliado"]["url_busca"] = None
    return d


@caso("publicavel sem `encurtamento_tentado_em`", "AUSENTE e diferente de tentado-e-falhou")
def _(d):
    r = registro_publicavel(d)
    r["afiliado"]["encurtamento_tentado_em"] = None
    return d


@caso("par de link GRAMPEADO: url e url_produto sem `par_colhido_em`", "ou nenhum entra")
def _(d):
    r = registro_publicavel(d)
    r["afiliado"]["par_colhido_em"] = None
    return d


@caso("degrau 4 com `url` preenchida", "degrau 4 com `url` preenchida")
def _(d):
    r = registro_publicavel(d)
    r["afiliado"]["degrau"] = 4
    return d


@caso("degrau 2 com `url` e sem `url_produto`", "permanecera desconhecida")
def _(d):
    r = registro_publicavel(d)
    r["afiliado"]["degrau"] = 2
    r["afiliado"]["url_produto"] = None
    r["afiliado"]["par_colhido_em"] = None
    return d


@caso("motivo de link que nao separa CAUSA de ULTIMA TENTATIVA", "marcador `||`")
def _(d):
    primeiro(d)["afiliado"]["motivo_sem_url_busca"] = "nao deu"
    return d


@caso("chave de `afiliado` ausente", "`afiliado.url_busca` ausente")
def _(d):
    primeiro(d)["afiliado"].pop("url_busca")
    return d


# ------------------------------------------------------------------------ PECA
@caso("peca com tipo fora do vocabulario da ilha", "fora do vocabulario da ilha")
def _(d):
    d["pecas"]["registros"][0]["tipo"] = "escova lateral"
    return d


@caso("peca com chave de encaixe e sem valor", "e `valor` vazio")
def _(d):
    d["pecas"]["registros"][0]["compatibilidade"]["valor"] = None
    return d


@caso("peca com compatibilidade DEDUZIDA", "fora das origens legitimas de leitura")
def _(d):
    d["pecas"]["registros"][0]["compatibilidade"]["declarada_por"] = "parece_dessa_medida"
    return d


@caso("peca com chave null e sem motivo", "Compatibilidade nao se deduz")
def _(d):
    for p in d["pecas"]["registros"]:
        if p["id"] == "chicote-shopee":
            p["compatibilidade"]["motivo"] = None
    return d


@caso("peca de medida marcada como `chave: nenhuma`", "num tipo cuja chave de encaixe no esquema e")
def _(d):
    d["pecas"]["registros"][0]["compatibilidade"]["chave"] = "nenhuma"
    return d


# ------------------------------------------------------------------- MUNICIPIO
@caso("municipio publicavel com fonte de MATERIA", "Materia sobre o ato nao e o ato")
def _(d):
    d["municipios"]["registros"][0]["status"] = "publicavel"
    return d


@caso("municipio publicavel sem nenhum limite", "Municipio sem limite nao e camada 2")
def _(d):
    m = d["municipios"]["registros"][2]
    m["status"] = "publicavel"
    m["fontes"]["corpus-bloco-1"].update(
        {"nivel": 3, "origem": "ato-municipal-lido-no-municipio", "leitura": "lido no .gov.br"})
    return d


@caso("municipio com status fora do enum", "`status` 'talvez' fora do enum")
def _(d):
    d["municipios"]["registros"][0]["status"] = "talvez"
    return d


# ------------------------------------------- MORTES DO ESQUEMA (26.2): chave que some MATA
@caso("MORTE: a lista de campos que exigem procedencia de leitura SOME do esquema",
      "`campos_que_exigem_procedencia_de_leitura.campos` desapareceu do esquema")
def _(d):
    d["esquema"]["campos_que_exigem_procedencia_de_leitura"].pop("campos")
    return d


@caso("MORTE: `niveis_minimos_por_campo` SOME do esquema", "desapareceu do esquema")
def _(d):
    d["esquema"]["escada_de_fontes"].pop("niveis_minimos_por_campo")
    return d


@caso("MORTE: os grupos de prestacao de contas da F1 SOMEM do esquema", "desapareceu do esquema")
def _(d):
    d["esquema"]["grupos_de_prestacao_de_contas"].pop("F1")
    return d


@caso("MORTE: a entidade MUNICIPIO SOME do esquema", "desapareceu do esquema")
def _(d):
    d["esquema"]["entidades"].pop("MUNICIPIO")
    return d


@caso("MORTE: a constante do limiar legal SOME de constantes.json", "nao existe mais em dados/constantes.json")
def _(d):
    d["constantes"]["constantes"] = [c for c in d["constantes"]["constantes"]
                                     if c["id"] != "limiares-categoria-contran-996-2023"]
    return d


@caso("MORTE: a sentinela de ausencia SOME do esquema, e o banco de HOJE passa a reprovar",
      "nao tem `declarado_como`")
def _(d):
    d["esquema"]["entidades"]["VEICULO"]["campos_tecnicos"]["acelerador"].pop("valor_sentinela_de_ausencia")
    return d


@caso("MORTE: `tipo_comercial` e `categoria` passam a compartilhar um valor",
      "nao pode ser gravavel como categoria da resolucao")
def _(d):
    d["esquema"]["entidades"]["VEICULO"]["campos_de_identidade"]["tipo_comercial"]["valores"].append(
        "autopropelido")
    return d


# --------------------------------------------------------------------- execucao
def rodar():
    falhas_da_bateria = []
    dados0 = base()
    for nome, espera, passa, fn in CASOS:
        d = copy.deepcopy(dados0)
        d = fn(d) or d
        try:
            falhas, _avisos, _c = VB.validar(d)
        except Exception as e:  # portao que explode nao e portao que reprova
            falhas_da_bateria.append("%s: o validador LEVANTOU %s: %s" % (nome, type(e).__name__, e))
            continue
        if passa:
            if falhas:
                falhas_da_bateria.append("%s: mundo que tinha de PASSAR reprovou com %r"
                                         % (nome, falhas[:3]))
        else:
            if not falhas:
                falhas_da_bateria.append("%s: o validador APROVOU o banco estragado" % nome)
            elif espera and not any(espera in f for f in falhas):
                falhas_da_bateria.append(
                    "%s: reprovou pelo motivo ERRADO. Esperava ouvir %r e ouviu %r"
                    % (nome, espera, falhas[:3]))
    return falhas_da_bateria


def autoteste():
    """Um validador de mentira, que aprova tudo, tem de fazer esta bateria reprovar."""
    original = VB.validar
    try:
        VB.validar = lambda d: ([], [], {})
        if not rodar():
            return ["AUTOTESTE: um validador que aprova TUDO passou nesta bateria. A bateria esta "
                    "quebrada e dizia 0 falha(s)."]
    finally:
        VB.validar = original
    return []


def main():
    if "--lista" in sys.argv:
        for nome, espera, passa, _ in CASOS:
            print("%-8s %s" % ("[passa]" if passa else "[quebra]", nome))
        print("")
        print("%d caso(s) + 1 autoteste." % len(CASOS))
        return 0
    falhas = autoteste() + rodar()
    for f in falhas:
        print("FALHA %s" % f)
    print("")
    print("%d caso(s) rodado(s) (%d mundos que passam, %d quebras) + 1 autoteste da bateria."
          % (len(CASOS), sum(1 for c in CASOS if c[2]), sum(1 for c in CASOS if not c[2])))
    print("%d falha(s)." % len(falhas))
    print("APROVADO" if not falhas else "REPROVADO")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
