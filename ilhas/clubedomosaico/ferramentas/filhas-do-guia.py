#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O PORTAO DE DADO DAS FILHAS DE NIVEL 3 DO GUIA — quais podem nascer HOJE, e com que numero.

    python3 ferramentas/filhas-do-guia.py              # escreve dados/filhas-do-guia.json e o .md
    python3 ferramentas/filhas-do-guia.py --conferir   # nao escreve; falha se o arquivo estiver velho
    python3 ferramentas/filhas-do-guia.py --autoteste  # bancos fabricados, para a regua poder morder

POR QUE ESTE ARQUIVO EXISTE. A secao 7b do ARVORE.md desta ilha escreveu a ordem em
12/09/2026 e ela nao mudou: "Banco. (...) So entao as filhas de nivel 3, por cluster,
comecando pelo cluster cuja resposta termina em produto do banco. So entao a mae de nivel
2, que e o 4c." O primeiro degrau andou duas vezes (a `alicate` em 25/09, a `acabamento`
no mesmo dia) e o segundo nunca foi MEDIDO — o que existia era a frase "nenhuma filha de
alicate existe", que diz o que falta e nao diz o que ja da. Entre "o 4c esta fechado" e
"quais paginas podem nascer amanha" ha uma contagem, e ela nunca tinha sido feita.

A PERGUNTA, palavra por palavra da secao 9 do ARQUIPELAGO.md: "Portao inegociavel: pelo
menos 3 itens de banco reais E um numero calculado proprio por pagina." Sao DUAS
condicoes, e a segunda nunca foi contada nesta ilha. Contar itens e facil e ja foi feito
pelo `cobertura.py` para as FAIXAS das ferramentas; contar se existe um numero que a
pagina consegue CALCULAR sobre 3 itens do mesmo recorte e outra coisa — e e ela que decide
se a pagina compara tres produtos ou mostra um numero e duas lacunas.

OS DOIS VEREDITOS SAEM JUNTOS OU NENHUM DOS DOIS SERVE. Esta e a licao que o
`medir-egresso.py` desta mesma ilha pagou em 30/09/2026, e ela e geral: um portao que
olhasse so a CONTAGEM diria hoje que `torques` passa (tres registros) e mandaria escrever
uma pagina que compara um produto com dois silencios; um que olhasse so a DECLARACAO
esconderia que falta UMA frase de fabricante, nao um produto. Por isso cada recorte sai
com tres vereditos possiveis e nunca com um booleano:

  passa                         — 3+ itens E 3+ sustentaveis E ao menos um numero comum
  passa_na_contagem_sem_lastro  — 3+ itens, e menos de 3 deles sustentam recomendacao
  nao_passa                     — menos de 3 itens no banco

NADA AQUI E DIGITADO. Os recortes saem de `vocabularios.tipo_por_categoria` do
`dados/esquema-banco.json` — categoria inteira mais cada tipo que o vocabulario admite —,
o teto de nivel de fonte sai de `escada_de_fontes.nivel_minimo_para_recomendacao_primaria`
do mesmo arquivo, e os itens saem dos `dados/materiais-*.json`. Recorte digitado mediria
os recortes que alguem lembrou, e ficaria verde no dia em que o vocabulario crescesse —
que e exatamente o que acontece nesta ilha, onde a regra de crescimento de vocabulario faz
valor novo nascer junto com o primeiro registro que o usa.

O QUE ESTE ARQUIVO NAO FAZ: ele nao escreve pagina, nao escolhe endereco e nao classifica
SERP. A classificacao da 14.9 e trabalho de busca, mora em `dados/filhas-do-guia.md` na
secao que este gerador NAO toca, e existe porque contagem de banco e chance de primeira
pagina sao duas perguntas diferentes — a 14.9 manda cruzar as duas, nunca uma so.
"""

import io
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = os.path.join(BASE, "dados")

# A secao 9 do ARQUIPELAGO.md: "pelo menos 3 itens de banco reais e um numero calculado
# proprio por pagina". O 3 e do contrato, nao desta ilha, e por isso tem o nome da secao.
MINIMO_DA_SECAO_9 = 3

SAIDA_JSON = os.path.join(DADOS, "filhas-do-guia.json")
SAIDA_MD = os.path.join(DADOS, "filhas-do-guia.md")

# A marca que separa o que o gerador escreve do que a BUSCA escreve. Tudo acima dela e
# derivado e se regenera; tudo abaixo e a classificacao de SERP da 14.9, escrita a mao com
# data e consulta, e o gerador a PRESERVA. Sem esta fronteira, regenerar o arquivo apagaria
# a medicao que custou busca — que e a forma mais barata de perder dado que ninguem refaz.
FRONTEIRA = "<!-- DAQUI PARA BAIXO E BUSCA, NAO DERIVACAO: o gerador preserva. -->"


def carregar_esquema(dados=DADOS):
    with io.open(os.path.join(dados, "esquema-banco.json"), encoding="utf-8") as f:
        return json.load(f)


def carregar_banco(dados=DADOS):
    """Todos os materiais dos dados/materiais-*.json, na ordem dos arquivos."""
    itens = []
    for nome in sorted(os.listdir(dados)):
        if not (nome.startswith("materiais-") and nome.endswith(".json")):
            continue
        with io.open(os.path.join(dados, nome), encoding="utf-8") as f:
            d = json.load(f)
        for m in d.get("materiais", []):
            m = dict(m)
            m["_arquivo"] = nome
            itens.append(m)
    return itens


def teto_de_nivel(esquema):
    """O nivel maximo de fonte que sustenta recomendacao primaria, LIDO do esquema."""
    escada = esquema["escada_de_fontes"]
    return escada["nivel_minimo_para_recomendacao_primaria"]


def recortes_do_vocabulario(esquema):
    """Categoria inteira + cada tipo que o vocabulario admite. Derivado, nunca digitado."""
    por_categoria = esquema["vocabularios"]["tipo_por_categoria"]
    recortes = []
    for categoria in sorted(por_categoria):
        recortes.append({"recorte": categoria, "categoria": categoria, "tipo": None})
        for tipo in por_categoria[categoria]:
            recortes.append({"recorte": "%s/%s" % (categoria, tipo),
                             "categoria": categoria, "tipo": tipo})
    return recortes


def propriedades_com_lastro(material, teto):
    """Nomes das propriedades com valor nao nulo cuja fonte tem nivel <= teto.

    E aqui que a regra 5 do esquema ("recomendacao primaria exige fonte de nivel <= 3")
    deixa de ser prosa. Propriedade sem `fonte_id`, com fonte que o registro nao declara,
    ou com fonte de nivel pior que o teto, NAO conta: ela pode aparecer na tela como
    mencao com ressalva, e mencao com ressalva nao sustenta uma pagina.
    """
    fontes = material.get("fontes") or {}
    saida = []
    for nome, prop in (material.get("propriedades") or {}).items():
        if not isinstance(prop, dict):
            continue
        if prop.get("valor") is None:
            continue
        fonte_id = prop.get("fonte_id")
        if not fonte_id:
            continue
        fonte = fontes.get(fonte_id)
        if not isinstance(fonte, dict):
            continue
        nivel = fonte.get("nivel")
        if not isinstance(nivel, int) or nivel > teto:
            continue
        saida.append(nome)
    return sorted(saida)


def medir(esquema, banco):
    teto = teto_de_nivel(esquema)
    linhas = []
    for r in recortes_do_vocabulario(esquema):
        dentro = [m for m in banco
                  if m.get("categoria") == r["categoria"]
                  and m.get("status") == "ativo"
                  and (r["tipo"] is None or m.get("tipo") == r["tipo"])]

        com_lastro = []
        contagem_por_propriedade = {}
        for m in dentro:
            props = propriedades_com_lastro(m, teto)
            if props:
                com_lastro.append(m["id"])
            for p in props:
                contagem_por_propriedade.setdefault(p, []).append(m["id"])

        numeros = sorted(
            [{"propriedade": p, "em_quantos_itens": len(ids), "itens": sorted(ids)}
             for p, ids in contagem_por_propriedade.items()
             if len(ids) >= MINIMO_DA_SECAO_9],
            key=lambda x: (-x["em_quantos_itens"], x["propriedade"]),
        )

        if len(dentro) < MINIMO_DA_SECAO_9:
            veredito = "nao_passa"
        elif len(com_lastro) < MINIMO_DA_SECAO_9 or not numeros:
            veredito = "passa_na_contagem_sem_lastro"
        else:
            veredito = "passa"

        motivo = None
        if veredito == "nao_passa":
            motivo = ("o banco tem %d item(ns) ativo(s) neste recorte e a secao 9 exige %d"
                      % (len(dentro), MINIMO_DA_SECAO_9))
        elif veredito == "passa_na_contagem_sem_lastro":
            if len(com_lastro) < MINIMO_DA_SECAO_9:
                motivo = ("%d dos %d itens sustentam recomendacao primaria (fonte de nivel <= %d);"
                          " a secao 9 exige %d"
                          % (len(com_lastro), len(dentro), teto, MINIMO_DA_SECAO_9))
            else:
                motivo = ("%d dos %d itens sustentam recomendacao, e NENHUMA propriedade e declarada"
                          " por %d deles ao mesmo tempo — nao ha numero que a pagina calcule sobre o"
                          " recorte inteiro"
                          % (len(com_lastro), len(dentro), MINIMO_DA_SECAO_9))

        # A LISTA DE COMPRAS, e ela e o que separa "nao passa" de "nao se sabe o que falta".
        # A licao e do cobertura.py desta mesma ilha: "O que falta nessa varredura e a lista de
        # compras do banco — e o numero final aparece sozinho." Sem estes tres numeros, a proxima
        # execucao le "nao_passa" e recomeca a contagem do zero, que foi o que aconteceu quatro
        # vezes com o egresso entre 26/09 e 29/09.
        melhor = numeros[0]["em_quantos_itens"] if numeros else (
            max((len(ids) for ids in contagem_por_propriedade.values()), default=0))
        distancia = {
            "itens_que_faltam_para_3": max(0, MINIMO_DA_SECAO_9 - len(dentro)),
            "itens_com_lastro_que_faltam_para_3": max(0, MINIMO_DA_SECAO_9 - len(com_lastro)),
            "itens_que_faltam_para_o_numero_mais_perto": max(0, MINIMO_DA_SECAO_9 - melhor),
            "propriedade_mais_perto_de_ser_numero": (
                numeros[0]["propriedade"] if numeros else
                (max(contagem_por_propriedade.items(), key=lambda kv: (len(kv[1]), kv[0]))[0]
                 if contagem_por_propriedade else None)),
            "itens_sem_nenhum_numero_com_lastro": sorted(
                m["id"] for m in dentro if m["id"] not in com_lastro),
        }

        # SKU NOVO E CAMPO VAZIO NAO CUSTAM A MESMA COISA, e a distancia em ITENS esconde a
        # diferenca. Quando o recorte ja tem 3 itens com lastro e o que falta e o NUMERO comum, o
        # buraco pode estar num registro que ja mora no banco e so nao declara aquela propriedade —
        # e completar um campo de registro existente e coleta de um valor, nao de um produto. Sem
        # esta lista, "falta 1 item" manda procurar um SKU que talvez nem precise existir.
        # E a promessa so vale quando o recorte esta a UM registro. Medido em 30/09/2026 no banco
        # de verdade: a `cola` tem 7 itens e a propriedade "mais perto" e declarada por UM so, o que
        # fazia esta lista dizer "falta em 6 registros que ja estao no banco" — verdade literal que
        # se le como uma coleta e sao seis. Numero que existe num registro so nao esta perto de ser
        # numero da pagina: ele ainda tem de ser construido, e construir nao e completar.
        quem_falta = []
        prop_perto = distancia["propriedade_mais_perto_de_ser_numero"]
        if (prop_perto
                and melhor >= MINIMO_DA_SECAO_9 - 1
                and distancia["itens_que_faltam_para_3"] == 0
                and distancia["itens_com_lastro_que_faltam_para_3"] == 0
                and distancia["itens_que_faltam_para_o_numero_mais_perto"] > 0):
            tem = set(contagem_por_propriedade.get(prop_perto, []))
            quem_falta = sorted(m["id"] for m in dentro if m["id"] not in tem)
        distancia["pode_fechar_completando_registro_existente"] = {
            "propriedade": prop_perto if quem_falta else None,
            "registros_que_nao_a_declaram": quem_falta,
            "leitura": ("a propriedade `%s` falta em %d registro(s) que JA estao no banco: o recorte"
                        " fecha coletando esse valor, nao um produto novo"
                        % (prop_perto, len(quem_falta))) if quem_falta else None,
        }

        linhas.append({
            "recorte": r["recorte"],
            "a_que_distancia_esta": distancia,
            "categoria": r["categoria"],
            "tipo": r["tipo"],
            "itens_no_banco": len(dentro),
            "itens": sorted(m["id"] for m in dentro),
            "itens_que_sustentam_recomendacao": len(com_lastro),
            "quais_sustentam": sorted(com_lastro),
            "numeros_calculaveis_sobre_o_recorte": numeros,
            "veredito": veredito,
            "motivo": motivo,
        })
    return teto, linhas


def custo_para_passar(l):
    """Quantos itens de banco faltam para este recorte virar filha publicavel.

    E o MAIOR dos tres buracos, nunca a soma: um item novo com numero declarado fecha os
    tres de uma vez, e somar faria a lista de compras pedir o triplo do que ela precisa.
    """
    d = l["a_que_distancia_esta"]
    return max(d["itens_que_faltam_para_3"],
               d["itens_com_lastro_que_faltam_para_3"],
               d["itens_que_faltam_para_o_numero_mais_perto"])


def resumo(linhas):
    conta = {"passa": 0, "passa_na_contagem_sem_lastro": 0, "nao_passa": 0}
    for l in linhas:
        conta[l["veredito"]] += 1
    por_categoria = {}
    for l in linhas:
        if l["tipo"] is None:
            continue
        c = por_categoria.setdefault(l["categoria"], {
            "tipos_que_passam": 0, "tipos_no_vocabulario": 0,
            "tipos_que_passam_quais": [], "caminho_mais_barato_para_as_3_filhas": None})
        c["tipos_no_vocabulario"] += 1
        if l["veredito"] == "passa":
            c["tipos_que_passam"] += 1
            c["tipos_que_passam_quais"].append(l["recorte"])

    # O caminho mais barato: entre os tipos que AINDA nao passam, os que faltam para chegar a 3,
    # ordenados pelo que custa menos item novo. Se a categoria nao tem 3 tipos no vocabulario, a
    # 16.5 nao se fecha por coleta nenhuma — e isso tem de sair escrito, nao deduzido.
    for cat, c in por_categoria.items():
        faltam = MINIMO_DA_SECAO_9 - c["tipos_que_passam"]
        if faltam <= 0:
            c["caminho_mais_barato_para_as_3_filhas"] = "ja alcancada"
            continue
        if c["tipos_no_vocabulario"] < MINIMO_DA_SECAO_9:
            c["caminho_mais_barato_para_as_3_filhas"] = (
                "IMPOSSIVEL por tipo: o vocabulario admite %d tipo(s) nesta categoria e a 16.5 exige"
                " %d filhas. So filha em forma de PERGUNTA (como a F2 e a F1 sao) fecha esta"
                " categoria." % (c["tipos_no_vocabulario"], MINIMO_DA_SECAO_9))
            continue
        candidatos = sorted(
            (l for l in linhas
             if l["categoria"] == cat and l["tipo"] is not None and l["veredito"] != "passa"),
            key=lambda l: (custo_para_passar(l), l["recorte"]))[:faltam]
        c["caminho_mais_barato_para_as_3_filhas"] = {
            "faltam_filhas": faltam,
            "itens_de_banco_a_coletar": sum(custo_para_passar(l) for l in candidatos),
            "em_quais_tipos": [{"tipo": l["recorte"], "itens_a_coletar": custo_para_passar(l)}
                               for l in candidatos],
        }
    return {
        "vereditos": conta,
        "filhas_que_podem_nascer_hoje": sorted(l["recorte"] for l in linhas if l["veredito"] == "passa"),
        "por_categoria_do_guia": por_categoria,
        "categorias_que_alcancam_as_3_filhas_da_16_5": sorted(
            c for c, v in por_categoria.items() if v["tipos_que_passam"] >= MINIMO_DA_SECAO_9),
    }


def montar(esquema, banco, perguntas=None):
    teto, linhas = medir(esquema, banco)
    perguntas = carregar_perguntas() if perguntas is None else perguntas
    linhas_de_pergunta = medir_perguntas(esquema, banco, perguntas)
    return {
        "id": "filhas-do-guia",
        "ilha": "clubedomosaico",
        "gerado_por": "ferramentas/filhas-do-guia.py",
        "derivado_de": ["dados/esquema-banco.json", "dados/materiais-*.json"],
        "o_que_este_arquivo_e": (
            "O portao de dado da secao 9 do ARQUIPELAGO.md aplicado, um por um, a TODOS os"
            " recortes que o vocabulario do esquema admite no Guia. Fotografia do banco de"
            " hoje, nao serie: se regenera a cada mudanca de banco ou de vocabulario."),
        "a_pergunta": ("quais filhas de nivel 3 do Guia passam HOJE o portao da secao 9 — 3 itens"
                       " de banco reais E um numero calculado proprio — e, para as que nao passam,"
                       " qual das duas metades falta"),
        "minimo_exigido_pela_secao_9": MINIMO_DA_SECAO_9,
        "nivel_maximo_de_fonte_lido_do_esquema": teto,
        "versao_do_esquema_lida": esquema.get("versao_esquema"),
        "o_que_conta_como_numero_calculavel": (
            "propriedade com valor nao nulo e fonte de nivel <= %d declarada por pelo menos %d"
            " itens DO MESMO recorte. Propriedade que so um item declara nao e numero da pagina:"
            " e numero de um produto, e a pagina que a publicasse compararia um item com dois"
            " silencios." % (teto, MINIMO_DA_SECAO_9)),
        "o_que_este_arquivo_mede_e_o_que_ele_NAO_alcanca": (
            "Ele mede os recortes que o VOCABULARIO nomeia — categoria inteira e cada tipo de"
            " `tipo_por_categoria` — e, desde 07/10/2026, tambem as filhas em forma de PERGUNTA"
            " declaradas em `dados/perguntas-do-guia.json`, pela MESMA regua e com o mesmo minimo."
            " De 30/09 a 07/10 esta frase dizia que a pergunta ficava fora e que o arquivo era um"
            " PISO; a pergunta entrou, e o piso de hoje e outro: o que continua fora e a pergunta"
            " que ninguem declarou. Uma pergunta atravessa tipos e pode reunir 3 itens onde nenhum"
            " tipo sozinho reune, e e por isso que `nao_passa` num tipo nao proibe a pergunta —"
            " proibe o tipo. O que esta regua NAO faz pela pergunta e dizer se ela ACRESCENTA uma"
            " filha a categoria: isso e do `cruzamento-14-9.py`, porque a 16.5 se fecha por"
            " CONSULTA, e pergunta que mira a consulta aberta de um tipo e o tipo com outro titulo."),
        "o_que_este_arquivo_NAO_decide": [
            "o endereco da pagina — quem publica escolhe, e a 16.5 manda a mae esperar 3 filhas",
            "a chance de primeira pagina — e a 14.9, e ela se mede na SERP, nao no banco",
            "a ordem das levas — e a secao 9, por intencao de compra, e ela olha a SERP tambem",
        ],
        "recortes": linhas,
        "resumo": resumo(linhas),
        "perguntas": linhas_de_pergunta,
        "resumo_das_perguntas": resumo_das_perguntas(linhas_de_pergunta),
    }


# ------------------------------------------------- as filhas em forma de PERGUNTA (07/10/2026)
#
# O cabecalho deste arquivo diz, desde 30/09/2026, que ele e um PISO e nunca um teto, porque
# filha de nivel 3 tambem pode ter forma de PERGUNTA — e que "quem escrever a pergunta conta os
# 3 itens dela pela mesma regua, e a regua esta nesta ferramenta para ser chamada em vez de
# reescrita". Por sete dias ninguem a chamou: a fila inteira da ilha foi escrita contando TIPOS,
# e as duas filhas vivas (a F1 e a F2) sao perguntas. Esta secao e a frase deixando de ser prosa.
#
# A PERGUNTA NAO AFROUXA O PORTAO, E ISTO TEM DE SER LIDO ANTES DE QUALQUER NUMERO. No recorte de
# tipo a secao 9 cobra TRES coisas separadas: 3 itens no recorte, 3 deles com lastro, e uma
# propriedade declarada por 3 ao mesmo tempo. Na pergunta as tres COINCIDEM, porque o recorte dela
# nao e um tipo do vocabulario: e o conjunto dos itens que declaram o numero com lastro. Contar
# "itens no recorte" ali seria contar a mesma coisa duas vezes e dizer que o portao e mais largo.
# O minimo e o mesmo, lido da mesma constante, e o teto de nivel de fonte e o mesmo do esquema.
#
# E A PERGUNTA NAO DECIDE SOZINHA SE A CATEGORIA GANHOU UMA FILHA. Isso e do `cruzamento-14-9.py`,
# porque a 16.5 se fecha por CONSULTA e nao por recorte: pergunta que mira a consulta aberta que
# ja esta creditada a um tipo nao e uma segunda filha — e o mesmo tipo com outro titulo, e publicar
# as duas seria disputar a propria consulta. Aqui mede-se so o lado do BANCO, igual aos recortes.

def carregar_perguntas(dados=DADOS):
    """As perguntas declaradas. Arquivo ausente = nenhuma pergunta, e isso nao e falha."""
    caminho = os.path.join(dados, "perguntas-do-guia.json")
    if not os.path.exists(caminho):
        return []
    with io.open(caminho, encoding="utf-8") as f:
        return json.load(f).get("perguntas", [])


def medir_perguntas(esquema, banco, perguntas):
    """Cada pergunta medida pela MESMA regua dos recortes de tipo.

    O recorte de uma pergunta e derivado: os itens ATIVOS da categoria dela que declaram a
    propriedade apontada com fonte de nivel <= teto. Nada aqui e digitado alem do nome da
    categoria, do nome da propriedade e da consulta — e os tres sao decisao de nome.
    """
    teto = teto_de_nivel(esquema)
    por_categoria = esquema["vocabularios"]["tipo_por_categoria"]
    linhas = []
    for p in perguntas:
        categoria = p["categoria"]
        propriedade = p["propriedade_que_carrega_o_numero"]

        dentro = [m for m in banco
                  if m.get("categoria") == categoria
                  and m.get("status") == "ativo"
                  and propriedade in propriedades_com_lastro(m, teto)]
        tipos = sorted(set(m.get("tipo") for m in dentro if m.get("tipo")))

        veredito = "passa" if len(dentro) >= MINIMO_DA_SECAO_9 else "nao_passa"
        motivo = None
        if veredito == "nao_passa":
            motivo = ("%d item(ns) ativo(s) de `%s` declaram `%s` com fonte de nivel <= %d, e a"
                      " secao 9 exige %d"
                      % (len(dentro), categoria, propriedade, teto, MINIMO_DA_SECAO_9))

        # A PERGUNTA QUE NAO ATRAVESSA TIPO NAO E UM TETO: E O PISO COM OUTRO TITULO. O proprio
        # cabecalho deste arquivo justifica a pergunta por ela "reunir 3 itens onde nenhum tipo
        # sozinho reune". Quando o conjunto de itens da pergunta e exatamente o de um recorte de
        # tipo, ela nao reuniu nada — e publicar as duas seria a mesma pagina duas vezes. Sai
        # escrito, com o nome do tipo, em vez de deduzido por quem ler a lista de tipos.
        # E A COINCIDENCIA COM A CATEGORIA INTEIRA NAO E O MESMO DEFEITO — foi a propria regua que
        # mostrou isso, na primeira passada, apontando `rejunte` para a pergunta da junta. A mae de
        # nivel 2 e INDICE de categoria e a pergunta e a pagina de nivel 3 que responde; os dois
        # lerem os mesmos 5 itens e o que "atravessa os tres tipos" significa no limite, e e assim
        # que a F1 e a F2 desta ilha vivem desde 11/09/2026. O que nao pode e coincidir com um TIPO.
        ids = set(m["id"] for m in dentro)
        coincide = None
        for tipo in por_categoria.get(categoria, []):
            do_tipo = set(m["id"] for m in banco
                          if m.get("categoria") == categoria
                          and m.get("status") == "ativo"
                          and m.get("tipo") == tipo)
            if ids and do_tipo == ids:
                coincide = "%s/%s" % (categoria, tipo)
                break
        da_categoria_inteira = set(m["id"] for m in banco
                                   if m.get("categoria") == categoria and m.get("status") == "ativo")
        cobre_a_categoria = bool(ids) and ids == da_categoria_inteira

        # A ANCORA A MAO, e ela e o unico lugar deste arquivo onde um numero escrito por uma
        # pessoa encosta na derivacao. Ela existe para CAIR: banco que cresce derruba a ancora e o
        # portao reprova, e a lida e reescrever dois numeros, nao procurar defeito.
        ancora = p.get("ancora_a_mao") or {}
        divergencias = []
        if "itens_que_declaram_o_numero" in ancora and ancora["itens_que_declaram_o_numero"] != len(dentro):
            divergencias.append("a ancora diz %s item(ns) e a derivacao conta %d"
                                % (ancora["itens_que_declaram_o_numero"], len(dentro)))
        if "tipos_atravessados" in ancora and sorted(ancora["tipos_atravessados"]) != tipos:
            divergencias.append("a ancora diz os tipos %s e a derivacao acha %s"
                                % (sorted(ancora["tipos_atravessados"]), tipos))

        linhas.append({
            "pergunta": p["id"],
            "categoria": categoria,
            "propriedade_que_carrega_o_numero": propriedade,
            "consulta_alvo": p["consulta_alvo"],
            "titulo_candidato": p.get("titulo_candidato"),
            "itens_que_declaram_o_numero": len(dentro),
            "itens": sorted(ids),
            "tipos_atravessados": tipos,
            "atravessa_mais_de_um_tipo": len(tipos) > 1,
            "coincide_com_o_recorte_de_tipo": coincide,
            "cobre_a_categoria_inteira": cobre_a_categoria,
            "veredito": veredito,
            "motivo": motivo,
            "divergencias_com_a_ancora_a_mao": divergencias,
        })
    return linhas


def resumo_das_perguntas(linhas):
    return {
        "perguntas_medidas": len(linhas),
        "passam_o_portao_de_dado": sorted(l["pergunta"] for l in linhas if l["veredito"] == "passa"),
        "atravessam_mais_de_um_tipo": sorted(l["pergunta"] for l in linhas
                                             if l["atravessa_mais_de_um_tipo"]),
        "coincidem_com_um_recorte_de_tipo": sorted(
            "%s = %s" % (l["pergunta"], l["coincide_com_o_recorte_de_tipo"])
            for l in linhas if l["coincide_com_o_recorte_de_tipo"]),
        "cobrem_a_categoria_inteira": sorted(l["pergunta"] for l in linhas
                                             if l["cobre_a_categoria_inteira"]),
        "ancoras_a_mao_que_cairam": sorted(l["pergunta"] for l in linhas
                                           if l["divergencias_com_a_ancora_a_mao"]),
    }


# ------------------------------------------------- o portao da tabela do ARVORE.md (secao 2)

# A UNICA COISA DIGITADA NESTE ARQUIVO, e ela tem de ser: o slug de nivel 2 e uma decisao de NOME,
# escrita no VOZ.md desta ilha ("colas-e-adesivos", nao "cola"), e nao se deriva do vocabulario do
# esquema. O que NAO e digitado e nenhum numero: a ponte diz qual linha da tabela fala de qual
# categoria, e os numeros da linha sao conferidos contra a derivacao.
PONTE_SLUG_CATEGORIA = {
    "/materiais/colas-e-adesivos/": "cola",
    "/materiais/rejuntes/": "rejunte",
    "/materiais/pastilhas/": "pastilha",
    "/materiais/alicates-e-corte/": "alicate",
    "/materiais/bases/": "base",
    "/materiais/acabamento/": "acabamento",
}

# `apoio` existe no vocabulario e NAO tem linha na tabela do Guia, de proposito: o ARVORE.md nao lhe
# da pagina de nivel 2, e criar uma e decisao de quem publicar, nao deste portao. Fica nomeada aqui
# para a ausencia ser declarada em vez de parecer esquecimento — se alguem lhe der nivel 2, o portao
# abaixo reprova por falta de linha, que e o alarme certo.
CATEGORIAS_SEM_NIVEL_2_NO_GUIA = {"apoio"}

LINHA_DA_TABELA = re.compile(
    r"^\|[^|]*\|\s*`(/materiais/[^`]+)`\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$")


def conferir_tabela_da_arvore(d, caminho=None):
    """A tabela da secao 2 do ARVORE.md tem de fechar com esta derivacao, nas DUAS direcoes.

    Cicatriz medida em 30/09/2026, nesta mesma tabela: ela dizia `0` em `Alicates e corte` e em
    `Acabamento` cinco dias depois de as duas sairem de zero, e o proprio arquivo registrava a
    correcao em prosa tres telas abaixo. Numero de documento sem portao envelhece calado, e a prosa
    que o corrige nao e lida por quem le a tabela primeiro.
    """
    caminho = caminho or os.path.join(BASE, "ARVORE.md")
    falhas = []
    if not os.path.exists(caminho):
        return ["ARVORE.md nao existe"]
    with io.open(caminho, encoding="utf-8") as f:
        linhas = f.read().splitlines()

    por_cat = d["resumo"]["por_categoria_do_guia"]
    itens_da_categoria = {l["categoria"]: l["itens_no_banco"]
                          for l in d["recortes"] if l["tipo"] is None}

    vistos = {}
    for linha in linhas:
        m = LINHA_DA_TABELA.match(linha)
        if not m:
            continue
        slug, banco, passam, _existe = m.groups()
        if slug not in PONTE_SLUG_CATEGORIA:
            continue
        cat = PONTE_SLUG_CATEGORIA[slug]
        vistos[cat] = True

        # coluna "banco hoje": "7 itens" ou "0"
        n = re.search(r"\d+", banco)
        if not n:
            falhas.append("a linha de `%s` nao traz numero na coluna de banco" % slug)
        elif int(n.group()) != itens_da_categoria.get(cat, 0):
            falhas.append("a linha de `%s` diz banco %s e a derivacao diz %d"
                          % (slug, n.group(), itens_da_categoria.get(cat, 0)))

        # coluna "tipos que passam": "1 de 6"
        mm = re.match(r"^(\d+)\s+de\s+(\d+)$", passam.strip())
        if not mm:
            falhas.append("a linha de `%s` nao traz a coluna de tipos na forma 'N de M'" % slug)
        else:
            q, tot = int(mm.group(1)), int(mm.group(2))
            c = por_cat.get(cat, {})
            if q != c.get("tipos_que_passam") or tot != c.get("tipos_no_vocabulario"):
                falhas.append("a linha de `%s` diz %d de %d e a derivacao diz %s de %s"
                              % (slug, q, tot, c.get("tipos_que_passam"),
                                 c.get("tipos_no_vocabulario")))

    # a outra direcao: categoria do vocabulario que deveria ter linha e nao tem
    for cat in por_cat:
        if cat in CATEGORIAS_SEM_NIVEL_2_NO_GUIA:
            continue
        if cat not in vistos:
            falhas.append("a categoria `%s` do vocabulario nao tem linha na tabela do ARVORE.md" % cat)
    for cat in vistos:
        if cat not in por_cat:
            falhas.append("a tabela do ARVORE.md tem linha de `%s`, que nao existe no vocabulario" % cat)
    return falhas


# ---------------------------------------------------------------- o .md, GERADO do json

def gerar_md(d, preservado=""):
    L = []
    A = L.append
    A("# As filhas de nivel 3 do Guia — o portao de dado da secao 9, medido recorte por recorte")
    A("")
    A("**GERADO por `ferramentas/filhas-do-guia.py` a partir de `dados/filhas-do-guia.json`.**")
    A("Nao edite este trecho a mao: `--conferir` regera e compara, e uma edicao manual reprova o")
    A("portao. O que se escreve a mao esta depois da fronteira, no fim do arquivo.")
    A("")
    A("Minimo da secao 9: **%d** itens. Nivel maximo de fonte para recomendacao primaria, lido do"
      % d["minimo_exigido_pela_secao_9"])
    A("esquema (versao %s): **%d**." % (d["versao_do_esquema_lida"], d["nivel_maximo_de_fonte_lido_do_esquema"]))
    A("")
    r = d["resumo"]
    A("## O numero que manda")
    A("")
    A("| veredito | recortes |")
    A("|---|---|")
    for k in ("passa", "passa_na_contagem_sem_lastro", "nao_passa"):
        A("| `%s` | %d |" % (k, r["vereditos"][k]))
    A("")
    if r["filhas_que_podem_nascer_hoje"]:
        A("**Podem nascer hoje:** " + ", ".join("`%s`" % x for x in r["filhas_que_podem_nascer_hoje"]) + ".")
    else:
        A("**Nenhum recorte passa hoje.**")
    A("")
    if r["categorias_que_alcancam_as_3_filhas_da_16_5"]:
        A("**Categorias que alcancam as 3 filhas da 16.5:** "
          + ", ".join("`%s`" % x for x in r["categorias_que_alcancam_as_3_filhas_da_16_5"]) + ".")
    else:
        A("**Nenhuma categoria do Guia alcanca as 3 filhas que a 16.5 exige** — nem somando todos os")
        A("tipos que o vocabulario admite. A mae de nivel 2 continua fechada, e agora por um numero.")
    A("")
    A("## Recorte por recorte")
    A("")
    A("| recorte | itens | com lastro | numeros calculaveis | veredito |")
    A("|---|---|---|---|---|")
    for l in d["recortes"]:
        nums = l["numeros_calculaveis_sobre_o_recorte"]
        cel = ", ".join("`%s` (%d)" % (n["propriedade"], n["em_quantos_itens"]) for n in nums[:3])
        if len(nums) > 3:
            cel += ", e mais %d" % (len(nums) - 3)
        A("| `%s` | %d | %d | %s | `%s` |"
          % (l["recorte"], l["itens_no_banco"], l["itens_que_sustentam_recomendacao"],
             cel or "—", l["veredito"]))
    A("")
    A("## As filhas em forma de PERGUNTA — a mesma regua, declaradas em `dados/perguntas-do-guia.json`")
    A("")
    A("A pergunta **nao afrouxa o portao**: no recorte de tipo a secao 9 cobra tres coisas separadas")
    A("(3 itens, 3 com lastro, um numero sobre 3); na pergunta as tres COINCIDEM, porque o recorte")
    A("dela e o conjunto dos itens que declaram o numero com lastro. Minimo e teto de nivel sao os")
    A("mesmos, lidos dos mesmos lugares. **E ela nao decide se a categoria ganhou filha** — a 16.5 se")
    A("fecha por CONSULTA, e isso e do `cruzamento-14-9.py`.")
    A("")
    if not d["perguntas"]:
        A("**Nenhuma pergunta declarada.** O arquivo de perguntas esta ausente ou vazio, e o portao")
        A("acima volta a ser o piso que ele era antes de 07/10/2026.")
    else:
        A("| pergunta | categoria | numero | itens | tipos que atravessa | veredito |")
        A("|---|---|---|---|---|---|")
        for l in d["perguntas"]:
            A("| `%s` | `%s` | `%s` | %d | %s | `%s` |"
              % (l["pergunta"], l["categoria"], l["propriedade_que_carrega_o_numero"],
                 l["itens_que_declaram_o_numero"],
                 ", ".join("`%s`" % t for t in l["tipos_atravessados"]) or "—",
                 l["veredito"]))
        A("")
        for l in d["perguntas"]:
            A("- **`%s`** — consulta-alvo: *%s*" % (l["pergunta"], l["consulta_alvo"]))
            if l["motivo"]:
                A("  - nao passa: %s" % l["motivo"])
            if l["coincide_com_o_recorte_de_tipo"]:
                A("  - **o conjunto de itens dela e exatamente o do TIPO `%s`**: ela nao reuniu o"
                  % l["coincide_com_o_recorte_de_tipo"])
                A("    que nenhum tipo reune, e publicar as duas seria a mesma pagina duas vezes.")
            elif l["cobre_a_categoria_inteira"]:
                A("  - cobre a categoria inteira (%d de %d itens ativos), e isso e o esperado: a mae"
                  % (l["itens_que_declaram_o_numero"], l["itens_que_declaram_o_numero"]))
                A("    de nivel 2 e indice e esta pergunta e a pagina de nivel 3 que responde.")
            elif not l["atravessa_mais_de_um_tipo"]:
                A("  - atravessa um tipo so, e ainda assim nao coincide com ele: o recorte da")
                A("    pergunta e menor que o do tipo, porque parte dos itens nao declara o numero.")
            for div in l["divergencias_com_a_ancora_a_mao"]:
                A("  - **ANCORA A MAO CAIDA:** %s" % div)
    A("")
    A("## O motivo, nos recortes que nao passam inteiros")
    A("")
    for l in d["recortes"]:
        if l["veredito"] == "passa":
            continue
        A("- **`%s`** — %s" % (l["recorte"], l["motivo"]))
    A("")
    A(FRONTEIRA)
    A("")
    if preservado.strip():
        # .strip() e nao .rstrip(): o trecho preservado chega com a quebra de linha que o separava da
        # fronteira, e A("") ja pos uma. Com .rstrip() o arquivo ganhava uma linha vazia por passada e
        # --conferir reprovava o proprio arquivo que a passada anterior escreveu. Gerador que nao e
        # idempotente e gerador que nao fecha com a propria derivacao — o caso 19 do autoteste morde
        # exatamente isto, porque um defeito assim passa por qualquer leitura no olho.
        A(preservado.strip())
    else:
        A("## A classificacao de SERP da 14.9 — ainda nao feita")
        A("")
        A("A 14.9 manda olhar a SERP da consulta-alvo ANTES de criar a pagina, e classificar quem")
        A("ocupa o top 10. Contagem de banco nao responde isso. Enquanto esta secao estiver assim,")
        A("nenhuma filha nasce, por mais que o portao de dado acima a autorize.")
    A("")
    return "\n".join(L)


def separar_preservado(caminho):
    if not os.path.exists(caminho):
        return ""
    with io.open(caminho, encoding="utf-8") as f:
        texto = f.read()
    if FRONTEIRA not in texto:
        return ""
    return texto.split(FRONTEIRA, 1)[1]


# ---------------------------------------------------------------------------- autoteste

def _material(id_, categoria, tipo, props=None, nivel=2, status="ativo"):
    props = props if props is not None else {"p": 1}
    return {
        "id": id_, "categoria": categoria, "tipo": tipo, "status": status,
        "propriedades": {n: {"valor": v, "unidade": "x", "fonte_id": "f1"} for n, v in props.items()},
        "fontes": {"f1": {"url": "x", "tipo": "x", "nivel": nivel}},
    }


def _esquema(tipos, teto=3, versao=99):
    return {
        "versao_esquema": versao,
        "escada_de_fontes": {"nivel_minimo_para_recomendacao_primaria": teto},
        "vocabularios": {"tipo_por_categoria": tipos},
    }


def autoteste():
    casos = []

    def caso(nome, esquema, banco, confere):
        casos.append((nome, esquema, banco, confere))

    def v(linhas, recorte):
        for l in linhas:
            if l["recorte"] == recorte:
                return l
        raise AssertionError("recorte %s nao saiu da medicao" % recorte)

    # 1. tres itens com numero comum passam
    caso("tres itens com a mesma propriedade PASSAM",
         _esquema({"cola": ["pva"]}),
         [_material("a", "cola", "pva"), _material("b", "cola", "pva"), _material("c", "cola", "pva")],
         lambda t, l: v(l, "cola/pva")["veredito"] == "passa")

    # 2. dois itens nao passam
    caso("dois itens NAO passam",
         _esquema({"cola": ["pva"]}),
         [_material("a", "cola", "pva"), _material("b", "cola", "pva")],
         lambda t, l: v(l, "cola/pva")["veredito"] == "nao_passa")

    # 3. tres itens, um so com lastro -> passa_na_contagem_sem_lastro (o caso torques)
    caso("tres itens e um so com lastro cai em passa_na_contagem_sem_lastro",
         _esquema({"alicate": ["torques"]}),
         [_material("a", "alicate", "torques"),
          _material("b", "alicate", "torques", props={}),
          _material("c", "alicate", "torques", props={})],
         lambda t, l: v(l, "alicate/torques")["veredito"] == "passa_na_contagem_sem_lastro")

    # 4. tres itens com lastro mas NENHUMA propriedade comum aos tres -> sem numero
    caso("tres itens com lastro e nenhum numero comum NAO passam",
         _esquema({"cola": ["pva"]}),
         [_material("a", "cola", "pva", props={"x": 1}),
          _material("b", "cola", "pva", props={"y": 1}),
          _material("c", "cola", "pva", props={"z": 1})],
         lambda t, l: v(l, "cola/pva")["veredito"] == "passa_na_contagem_sem_lastro"
                      and not v(l, "cola/pva")["numeros_calculaveis_sobre_o_recorte"])

    # 5. fonte de nivel pior que o teto nao sustenta
    caso("fonte de nivel 4 com teto 3 nao sustenta recomendacao",
         _esquema({"cola": ["pva"]}, teto=3),
         [_material("a", "cola", "pva", nivel=4), _material("b", "cola", "pva", nivel=4),
          _material("c", "cola", "pva", nivel=4)],
         lambda t, l: v(l, "cola/pva")["itens_que_sustentam_recomendacao"] == 0)

    # 6. o teto vem do esquema, nao do codigo: subindo o teto, os mesmos itens sustentam
    caso("o teto e LIDO do esquema — com teto 4 os mesmos itens sustentam",
         _esquema({"cola": ["pva"]}, teto=4),
         [_material("a", "cola", "pva", nivel=4), _material("b", "cola", "pva", nivel=4),
          _material("c", "cola", "pva", nivel=4)],
         lambda t, l: t == 4 and v(l, "cola/pva")["veredito"] == "passa")

    # 7. valor nulo nao conta como numero
    caso("propriedade com valor nulo nao conta",
         _esquema({"cola": ["pva"]}),
         [{"id": "a", "categoria": "cola", "tipo": "pva", "status": "ativo",
           "propriedades": {"p": {"valor": None, "fonte_id": "f1"}},
           "fontes": {"f1": {"nivel": 2}}}] * 3,
         lambda t, l: v(l, "cola/pva")["itens_que_sustentam_recomendacao"] == 0)

    # 8. item inativo nao entra
    caso("registro com status diferente de ativo nao entra na contagem",
         _esquema({"cola": ["pva"]}),
         [_material("a", "cola", "pva"), _material("b", "cola", "pva"),
          _material("c", "cola", "pva", status="descartado")],
         lambda t, l: v(l, "cola/pva")["itens_no_banco"] == 2)

    # 9. a categoria inteira agrega os tipos
    caso("a categoria inteira agrega os tipos",
         _esquema({"cola": ["pva", "epoxi"]}),
         [_material("a", "cola", "pva"), _material("b", "cola", "epoxi"), _material("c", "cola", "epoxi")],
         lambda t, l: v(l, "cola")["itens_no_banco"] == 3 and v(l, "cola/pva")["itens_no_banco"] == 1)

    # 10. tipo do vocabulario sem nenhum item aparece na medicao, com veredito
    caso("tipo do vocabulario sem item NENHUM ainda sai na medicao",
         _esquema({"cola": ["pva", "adesivo_para_espelho"]}),
         [_material("a", "cola", "pva")],
         lambda t, l: v(l, "cola/adesivo_para_espelho")["itens_no_banco"] == 0
                      and v(l, "cola/adesivo_para_espelho")["veredito"] == "nao_passa")

    # 11. a 16.5: categoria com 3 tipos que passam e nomeada; com 2, nao
    tres = []
    for tp in ("pva", "epoxi", "silicone_acetico"):
        tres += [_material("%s%d" % (tp, i), "cola", tp) for i in range(3)]
    caso("categoria com 3 tipos que passam alcanca a 16.5",
         _esquema({"cola": ["pva", "epoxi", "silicone_acetico"]}), tres,
         lambda t, l: "cola" in resumo(l)["categorias_que_alcancam_as_3_filhas_da_16_5"])
    caso("categoria com 2 tipos que passam NAO alcanca a 16.5",
         _esquema({"cola": ["pva", "epoxi", "silicone_acetico"]}), tres[:6],
         lambda t, l: not resumo(l)["categorias_que_alcancam_as_3_filhas_da_16_5"])

    # 12. propriedade sem fonte_id nao sustenta
    caso("propriedade sem fonte_id nao sustenta",
         _esquema({"cola": ["pva"]}),
         [{"id": "a%d" % i, "categoria": "cola", "tipo": "pva", "status": "ativo",
           "propriedades": {"p": {"valor": 1}}, "fontes": {}} for i in range(3)],
         lambda t, l: v(l, "cola/pva")["itens_que_sustentam_recomendacao"] == 0)

    # 13. fonte_id que o registro nao declara nao sustenta
    caso("fonte_id orfa nao sustenta",
         _esquema({"cola": ["pva"]}),
         [{"id": "a%d" % i, "categoria": "cola", "tipo": "pva", "status": "ativo",
           "propriedades": {"p": {"valor": 1, "fonte_id": "nao-existe"}},
           "fontes": {"f1": {"nivel": 1}}} for i in range(3)],
         lambda t, l: v(l, "cola/pva")["itens_que_sustentam_recomendacao"] == 0)

    # 14. distancia: um recorte a um item de passar diz que falta UM, nao tres
    caso("a distancia conta o MAIOR buraco, nunca a soma",
         _esquema({"cola": ["pva"]}),
         [_material("a", "cola", "pva"), _material("b", "cola", "pva")],
         lambda t, l: custo_para_passar(v(l, "cola/pva")) == 1)

    # 15. o buraco que se fecha completando registro existente e NOMEADO, com o registro
    def confere_completa(t, l):
        d = v(l, "rejunte/cimenticio")["a_que_distancia_esta"]
        f = d["pode_fechar_completando_registro_existente"]
        return (d["itens_que_faltam_para_o_numero_mais_perto"] == 1
                and f["propriedade"] == "junta"
                and f["registros_que_nao_a_declaram"] == ["c"])
    caso("o recorte que fecha completando registro existente nomeia o registro",
         _esquema({"rejunte": ["cimenticio"]}),
         [_material("a", "rejunte", "cimenticio", props={"junta": 2}),
          _material("b", "rejunte", "cimenticio", props={"junta": 3}),
          _material("c", "rejunte", "cimenticio", props={"outra": 1})],
         confere_completa)

    # 16. e quando o buraco E de produto novo, esse campo fica vazio em vez de apontar registro
    caso("com menos de 3 itens NAO se promete fechar por registro existente",
         _esquema({"rejunte": ["cimenticio"]}),
         [_material("a", "rejunte", "cimenticio"), _material("b", "rejunte", "cimenticio")],
         lambda t, l: v(l, "rejunte/cimenticio")["a_que_distancia_esta"][
             "pode_fechar_completando_registro_existente"]["registros_que_nao_a_declaram"] == [])

    # 17. o buraco LARGO nao se disfarca de "completar registro": o caso medido da cola
    caso("numero declarado por UM item so nao vira promessa de completar registro",
         _esquema({"cola": ["pva"]}),
         [_material("a", "cola", "pva", props={"x": 1}),
          _material("b", "cola", "pva", props={"y": 1}),
          _material("c", "cola", "pva", props={"z": 1})],
         lambda t, l: v(l, "cola/pva")["a_que_distancia_esta"][
             "pode_fechar_completando_registro_existente"]["registros_que_nao_a_declaram"] == [])

    # 18. o gerador e IDEMPOTENTE: gerar do proprio texto gerado devolve o mesmo texto
    def confere_idempotente(t, l):
        d = {"id": "x", "minimo_exigido_pela_secao_9": 3, "nivel_maximo_de_fonte_lido_do_esquema": 3,
             "versao_do_esquema_lida": 9, "recortes": l, "resumo": resumo(l),
             "perguntas": [], "resumo_das_perguntas": resumo_das_perguntas([])}
        um = gerar_md(d, preservado="\n## MINHA SERP\n\nmedido a mao\n")
        dois = gerar_md(d, preservado=um.split(FRONTEIRA, 1)[1])
        tres = gerar_md(d, preservado=dois.split(FRONTEIRA, 1)[1])
        return um == dois == tres
    caso("o gerador e idempotente — tres passadas dao o mesmo texto",
         _esquema({"cola": ["pva"]}), [_material("a", "cola", "pva")], confere_idempotente)

    # 19. o .md gerado PRESERVA o que esta depois da fronteira
    def confere_preserva(t, l):
        d = {"id": "x", "minimo_exigido_pela_secao_9": 3, "nivel_maximo_de_fonte_lido_do_esquema": 3,
             "versao_do_esquema_lida": 9, "recortes": l, "resumo": resumo(l),
             "perguntas": [], "resumo_das_perguntas": resumo_das_perguntas([])}
        md = gerar_md(d, preservado="\n## MINHA SERP\n\nmedido a mao\n")
        return "MINHA SERP" in md and "medido a mao" in md
    caso("o .md gerado preserva o trecho de busca",
         _esquema({"cola": ["pva"]}), [_material("a", "cola", "pva")], confere_preserva)

    # 19-b. o .md com PERGUNTA dentro: a secao sai, a consulta-alvo sai, e o gerador continua
    # idempotente. Sem este caso os dois fixtures acima renderizavam a secao nova VAZIA e a
    # bancada ficava verde sobre um trecho de documento que ninguem nunca viu escrito.
    def confere_md_com_pergunta(t, l):
        perg = medir_perguntas(
            _esquema({"cola": ["pva", "epoxi"]}),
            [_material("a", "cola", "pva", {"esp": 1}), _material("b", "cola", "pva", {"esp": 1}),
             _material("c", "cola", "epoxi", {"esp": 2})],
            [{"id": "pergunta:esp", "categoria": "cola",
              "propriedade_que_carrega_o_numero": "esp",
              "consulta_alvo": "minha consulta de teste", "titulo_candidato": "t"}])
        d = {"id": "x", "minimo_exigido_pela_secao_9": 3, "nivel_maximo_de_fonte_lido_do_esquema": 3,
             "versao_do_esquema_lida": 9, "recortes": l, "resumo": resumo(l),
             "perguntas": perg, "resumo_das_perguntas": resumo_das_perguntas(perg)}
        um = gerar_md(d, preservado="\n## MINHA SERP\n\nmedido a mao\n")
        dois = gerar_md(d, preservado=um.split(FRONTEIRA, 1)[1])
        return ("pergunta:esp" in um and "minha consulta de teste" in um
                and "forma de PERGUNTA" in um and um == dois)
    caso("o .md publica a secao das perguntas e segue idempotente com ela",
         _esquema({"cola": ["pva"]}), [_material("a", "cola", "pva")], confere_md_com_pergunta)

    # ---- o portao da tabela do ARVORE.md, com documentos FABRICADOS. Portao que so viu tabela
    # certa nao provou nada: cada caso abaixo escreve uma tabela ERRADA de um jeito diferente e
    # exige que o portao a reprove, e o ultimo exige que ele APROVE a certa.
    import tempfile

    def tabela(banco_cola="7 itens", passam_cola="0 de 7", faltando=None, extra=""):
        faltando = faltando or set()
        linhas = ["| nivel 2 | slug | banco hoje | tipos que passam o portao da 9 | existe |",
                  "|---|---|---|---|---|"]
        alvo = {"/materiais/colas-e-adesivos/": ("cola", banco_cola, passam_cola),
                # `rejunte` foi de "0 de 4" para "1 de 4" em 05/10/2026, quando a faixa de junta do
                # rejunte piscinas chegou pelo boletim tecnico, e ESTE FIXTURE NAO FOI ACERTADO JUNTO:
                # a autoteste ficou vermelha no main por dois dias em DOIS casos (o que exige APROVAR a
                # tabela certa e o do slug fora da ponte, que monta a mesma tabela), com uma causa so.
                # Ninguem viu porque `filhas-do-guia.py --autoteste` nao esta na lista de bancadas que
                # a ronda diaria roda — a mesma tabela do ARVORE.md tinha sido corrigida no dia, pelo
                # `--conferir`, e esta copia a mao nao tem quem a confira. Corrigido em 07/10/2026.
                "/materiais/rejuntes/": ("rejunte", "5 itens", "1 de 4"),
                "/materiais/pastilhas/": ("pastilha", "13 itens", "1 de 6"),
                # `alicate` foi de "1 de 4" para "2 de 4" em 07/10/2026: `alicate/torques` passou o
                # portao quando os dois torqueses que faltavam ganharam `tamanho_polegadas` de nivel 3.
                "/materiais/alicates-e-corte/": ("alicate", "6 itens", "2 de 4"),
                "/materiais/bases/": ("base", "0", "0 de 5"),
                # 10 itens e 3 de 3 desde 02/10/2026: a coleta de um
                # impermeabilizante e dois seladores fez `acabamento` ser a
                # primeira categoria do Guia a alcancar as 3 filhas da 16.5.
                # A regua desta bancada e ESCRITA A MAO de proposito, para nao
                # chamar a funcao que ela mede — e o preco disso e que ela se
                # atualiza quando o banco muda. Quem mudar o banco e vir este
                # caso falhar nao tem defeito para procurar: tem dois numeros
                # para reescrever, aqui e na tabela do ARVORE.md.
                "/materiais/acabamento/": ("acabamento", "10 itens", "3 de 3")}
        for slug, (cat, b, q) in alvo.items():
            if cat in faltando:
                continue
            linhas.append("| %s | `%s` | %s | %s | nao |" % (cat, slug, b, q))
        if extra:
            linhas.append(extra)
        return "\n".join(linhas) + "\n"

    def com_tabela(texto, d):
        f = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8")
        f.write(texto)
        f.close()
        try:
            return conferir_tabela_da_arvore(d, caminho=f.name)
        finally:
            os.unlink(f.name)

    # ----------------------------------------------------------------- as filhas em PERGUNTA
    #
    # A regua da pergunta nasceu em 07/10/2026 e estes casos existem para ela poder morder. O
    # primeiro deles e o que mais importa e e o unico que justifica a pergunta existir: dois tipos
    # com 2 itens cada, nenhum passando sozinho, e a pergunta reunindo os 4.

    def p(id_, categoria, propriedade, ancora=None):
        d = {"id": id_, "categoria": categoria,
             "propriedade_que_carrega_o_numero": propriedade,
             "consulta_alvo": "c", "titulo_candidato": "t"}
        if ancora:
            d["ancora_a_mao"] = ancora
        return d

    def pcaso(nome, esquema, banco, perguntas, confere):
        casos.append((nome, esquema, banco, ("PERGUNTA", perguntas, confere)))

    def q(linhas, pergunta):
        for l in linhas:
            if l["pergunta"] == pergunta:
                return l
        raise AssertionError("pergunta %s nao saiu da medicao" % pergunta)

    pcaso("a PERGUNTA reune 4 itens onde nenhum dos dois tipos reune 3",
          _esquema({"alicate": ["torques", "cortador"]}),
          [_material("a", "alicate", "torques", {"esp": 5}),
           _material("b", "alicate", "torques", {"esp": 5}),
           _material("c", "alicate", "cortador", {"esp": 10}),
           _material("d", "alicate", "cortador", {"esp": 10})],
          [p("pergunta:esp", "alicate", "esp")],
          lambda l: (q(l, "pergunta:esp")["veredito"] == "passa"
                     and q(l, "pergunta:esp")["itens_que_declaram_o_numero"] == 4
                     and q(l, "pergunta:esp")["atravessa_mais_de_um_tipo"]))

    pcaso("DOIS itens declarando o numero NAO passam, e o minimo e o mesmo da secao 9",
          _esquema({"alicate": ["torques"]}),
          [_material("a", "alicate", "torques", {"esp": 5}),
           _material("b", "alicate", "torques", {"esp": 5}),
           _material("c", "alicate", "torques", {"outra": 1})],
          [p("pergunta:esp", "alicate", "esp")],
          lambda l: (q(l, "pergunta:esp")["veredito"] == "nao_passa"
                     and "2 item" in q(l, "pergunta:esp")["motivo"]))

    pcaso("item cuja fonte e PIOR que o teto do esquema nao conta para a pergunta",
          _esquema({"alicate": ["torques"]}, teto=3),
          [_material("a", "alicate", "torques", {"esp": 5}),
           _material("b", "alicate", "torques", {"esp": 5}),
           _material("c", "alicate", "torques", {"esp": 5}, nivel=5)],
          [p("pergunta:esp", "alicate", "esp")],
          lambda l: q(l, "pergunta:esp")["veredito"] == "nao_passa")

    pcaso("item DESCARTADO nao conta para a pergunta",
          _esquema({"alicate": ["torques"]}),
          [_material("a", "alicate", "torques", {"esp": 5}),
           _material("b", "alicate", "torques", {"esp": 5}),
           _material("c", "alicate", "torques", {"esp": 5}, status="descartado")],
          [p("pergunta:esp", "alicate", "esp")],
          lambda l: q(l, "pergunta:esp")["veredito"] == "nao_passa")

    pcaso("pergunta cujo conjunto de itens e o de UM TIPO sai marcada: e o tipo com outro titulo",
          _esquema({"alicate": ["torques", "cortador"]}),
          [_material("a", "alicate", "torques", {"esp": 5}),
           _material("b", "alicate", "torques", {"esp": 5}),
           _material("c", "alicate", "torques", {"esp": 5}),
           _material("d", "alicate", "cortador", {"outra": 1})],
          [p("pergunta:esp", "alicate", "esp")],
          lambda l: q(l, "pergunta:esp")["coincide_com_o_recorte_de_tipo"] == "alicate/torques")

    # ESTE CASO E A CORRECAO QUE A PROPRIA REGUA PEDIU NA PRIMEIRA PASSADA. A versao de 15 minutos
    # antes marcava a pergunta da junta como "coincide com o recorte `rejunte`" — a CATEGORIA — e
    # lida ao pe da letra ela proibiria justamente a pergunta que atravessa os tres tipos. Mae de
    # nivel 2 e indice; pergunta e a pagina de nivel 3 que responde. Os dois lendo os mesmos itens
    # e o esperado, e e assim que a F1 e a F2 desta ilha vivem.
    pcaso("pergunta que cobre a CATEGORIA inteira nao e coincidencia de tipo",
          _esquema({"rejunte": ["acrilico", "cimenticio", "epoxi"]}),
          [_material("a", "rejunte", "acrilico", {"junta": 1}),
           _material("b", "rejunte", "cimenticio", {"junta": 2}),
           _material("c", "rejunte", "epoxi", {"junta": 1})],
          [p("pergunta:junta", "rejunte", "junta")],
          lambda l: (q(l, "pergunta:junta")["cobre_a_categoria_inteira"]
                     and q(l, "pergunta:junta")["coincide_com_o_recorte_de_tipo"] is None
                     and q(l, "pergunta:junta")["veredito"] == "passa"))

    pcaso("ancora a mao com CONTAGEM errada derruba a pergunta",
          _esquema({"alicate": ["torques"]}),
          [_material("a", "alicate", "torques", {"esp": 5}),
           _material("b", "alicate", "torques", {"esp": 5}),
           _material("c", "alicate", "torques", {"esp": 5})],
          [p("pergunta:esp", "alicate", "esp", {"itens_que_declaram_o_numero": 9})],
          lambda l: any("a ancora diz 9" in x
                        for x in q(l, "pergunta:esp")["divergencias_com_a_ancora_a_mao"]))

    pcaso("ancora a mao com TIPOS errados derruba a pergunta",
          _esquema({"alicate": ["torques", "cortador"]}),
          [_material("a", "alicate", "torques", {"esp": 5}),
           _material("b", "alicate", "torques", {"esp": 5}),
           _material("c", "alicate", "torques", {"esp": 5})],
          [p("pergunta:esp", "alicate", "esp", {"tipos_atravessados": ["torques", "cortador"]})],
          lambda l: any("os tipos" in x
                        for x in q(l, "pergunta:esp")["divergencias_com_a_ancora_a_mao"]))

    pcaso("ancora a mao CERTA nao derruba nada — a regua tem de aprovar o certo",
          _esquema({"alicate": ["torques", "cortador"]}),
          [_material("a", "alicate", "torques", {"esp": 5}),
           _material("b", "alicate", "cortador", {"esp": 10}),
           _material("c", "alicate", "cortador", {"esp": 10})],
          [p("pergunta:esp", "alicate", "esp",
             {"itens_que_declaram_o_numero": 3, "tipos_atravessados": ["cortador", "torques"]})],
          lambda l: (not q(l, "pergunta:esp")["divergencias_com_a_ancora_a_mao"]
                     and q(l, "pergunta:esp")["veredito"] == "passa"))

    pcaso("propriedade que NINGUEM declara nao passa, e o motivo diz qual propriedade era",
          _esquema({"alicate": ["torques"]}),
          [_material("a", "alicate", "torques", {"outra": 1}),
           _material("b", "alicate", "torques", {"outra": 1}),
           _material("c", "alicate", "torques", {"outra": 1})],
          [p("pergunta:esp", "alicate", "esp")],
          lambda l: (q(l, "pergunta:esp")["veredito"] == "nao_passa"
                     and "`esp`" in q(l, "pergunta:esp")["motivo"]))

    pcaso("pergunta de CATEGORIA que nao existe no banco nao explode: sai nao_passa com zero",
          _esquema({"alicate": ["torques"]}),
          [_material("a", "alicate", "torques", {"esp": 5})],
          [p("pergunta:x", "base", "esp")],
          lambda l: (q(l, "pergunta:x")["veredito"] == "nao_passa"
                     and q(l, "pergunta:x")["itens_que_declaram_o_numero"] == 0
                     and q(l, "pergunta:x")["coincide_com_o_recorte_de_tipo"] is None
                     and not q(l, "pergunta:x")["cobre_a_categoria_inteira"]))

    pcaso("arquivo de perguntas VAZIO deixa a medicao vazia, e isso nao e falha",
          _esquema({"alicate": ["torques"]}),
          [_material("a", "alicate", "torques", {"esp": 5})],
          [],
          lambda l: l == [])

    esquema_real = carregar_esquema()
    banco_real = carregar_banco()
    d_real = montar(esquema_real, banco_real)

    casos_tabela = [
        ("o portao APROVA a tabela certa", tabela(), True),
        ("reprova numero de banco errado", tabela(banco_cola="99 itens"), False),
        ("reprova contagem de tipos errada", tabela(passam_cola="3 de 7"), False),
        ("reprova total de tipos errado", tabela(passam_cola="0 de 99"), False),
        ("reprova coluna de tipos fora da forma 'N de M'", tabela(passam_cola="nenhum"), False),
        ("reprova linha que FALTA", tabela(faltando={"acabamento"}), False),
        # Slug que a ponte nao conhece e IGNORADO de proposito: a tabela do ARVORE.md tem outras
        # linhas (`/materiais/como-sabemos/`) que nao sao categoria de banco, e reprovar por elas
        # faria o portao brigar com o documento certo. O que ele cobra e a outra direcao — toda
        # categoria do vocabulario com nivel 2 tem de ter linha —, e isso o caso acima mede.
        ("linha de slug fora da ponte e ignorada, nao reprovada",
         tabela(extra="| Como sabemos | `/materiais/como-sabemos/` | — | — | **sim** |"), True),
    ]
    for nome, texto, deve_aprovar in casos_tabela:
        falhas_t = com_tabela(texto, d_real)
        casos.append((nome, None, None, ("TABELA", falhas_t, deve_aprovar)))

    falhas = 0
    for nome, esquema, banco, confere in casos:
        try:
            if isinstance(confere, tuple) and confere and confere[0] == "TABELA":
                _, falhas_t, deve_aprovar = confere
                ok = (not falhas_t) if deve_aprovar else bool(falhas_t)
            elif isinstance(confere, tuple) and confere and confere[0] == "PERGUNTA":
                _, perguntas_fab, confere_p = confere
                ok = bool(confere_p(medir_perguntas(esquema, banco, perguntas_fab)))
            else:
                teto, linhas = medir(esquema, banco)
                ok = bool(confere(teto, linhas))
        except Exception as e:  # noqa: BLE001 — a bancada tem de dizer QUAL caso explodiu
            ok = False
            nome = "%s  [explodiu: %s]" % (nome, e)
        print("  %-4s %s" % ("ok" if ok else "FALHA", nome))
        if not ok:
            falhas += 1
    print("")
    print("%s: %d caso(s) fabricado(s), %d falha(s)."
          % ("APROVADO" if not falhas else "REPROVADO", len(casos), falhas))
    return 1 if falhas else 0


# -------------------------------------------------------------------------------- main

def main(argv):
    if "--autoteste" in argv:
        return autoteste()

    esquema = carregar_esquema()
    banco = carregar_banco()
    d = montar(esquema, banco)
    md = gerar_md(d, preservado=separar_preservado(SAIDA_MD))

    if "--conferir" in argv:
        falhas = []
        if not os.path.exists(SAIDA_JSON):
            falhas.append("dados/filhas-do-guia.json nao existe")
        else:
            with io.open(SAIDA_JSON, encoding="utf-8") as f:
                gravado = json.load(f)
            if gravado.get("recortes") != d["recortes"] or gravado.get("resumo") != d["resumo"]:
                falhas.append("dados/filhas-do-guia.json esta velho: o banco ou o vocabulario mudou")
            if (gravado.get("perguntas") != d["perguntas"]
                    or gravado.get("resumo_das_perguntas") != d["resumo_das_perguntas"]):
                falhas.append("dados/filhas-do-guia.json esta velho na secao das PERGUNTAS: o banco"
                              " ou o dados/perguntas-do-guia.json mudou")
        for l in d["perguntas"]:
            for div in l["divergencias_com_a_ancora_a_mao"]:
                falhas.append("a ancora a mao de `%s` caiu: %s" % (l["pergunta"], div))
        if not os.path.exists(SAIDA_MD):
            falhas.append("dados/filhas-do-guia.md nao existe")
        else:
            with io.open(SAIDA_MD, encoding="utf-8") as f:
                if f.read() != md:
                    falhas.append("dados/filhas-do-guia.md nao fecha com a propria derivacao")
        falhas += conferir_tabela_da_arvore(d)
        for f_ in falhas:
            print("  FALHA %s" % f_)
        if falhas:
            print("")
            print("REPROVADO: %d falha(s). Rode sem --conferir para regerar." % len(falhas))
            return 1
        print("  ok   dados/filhas-do-guia.json fecha com o banco de hoje")
        print("  ok   as %d pergunta(s) declarada(s) fecham com o banco e com a propria ancora a mao"
              % len(d["perguntas"]))
        print("  ok   dados/filhas-do-guia.md fecha com a propria derivacao")
        print("  ok   a tabela da secao 2 do ARVORE.md fecha com a derivacao, nas duas direcoes")
        print("")
        print("APROVADO: o arquivo gerado fecha com a derivacao.")
        return 0

    with io.open(SAIDA_JSON, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
        f.write("\n")
    with io.open(SAIDA_MD, "w", encoding="utf-8") as f:
        f.write(md)

    r = d["resumo"]
    print("Recortes medidos: %d" % len(d["recortes"]))
    for k in ("passa", "passa_na_contagem_sem_lastro", "nao_passa"):
        print("  %-30s %d" % (k, r["vereditos"][k]))
    print("")
    print("Podem nascer hoje: %s" % (", ".join(r["filhas_que_podem_nascer_hoje"]) or "nenhum"))
    print("Categorias com as 3 filhas da 16.5: %s"
          % (", ".join(r["categorias_que_alcancam_as_3_filhas_da_16_5"]) or "nenhuma"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
