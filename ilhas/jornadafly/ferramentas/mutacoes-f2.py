#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra a F2 de proposito e verifica que ferramentas/teste-f2.py reprova.

    python3 ferramentas/mutacoes-f2.py

Sai com codigo 1 se qualquer mutacao decidir errado.

Quatro tipos, os mesmos da bateria da F1:

  MUNDOS (esperam PASSAR) -- constroem o caso que o banco ainda nao tem e exigem que
  o portao o aprove. Aqui eles sao a maior parte do valor desta bateria, porque o
  banco tem ZERO faixas diarias: sem os mundos, a metade da F2 que trata faixa de
  terceiro nunca seria executada por ninguem, e o dia da primeira carga seria o dia
  de descobrir que ela estava errada. Os mundos carregam faixa em memoria -- nenhuma
  linha e gravada no banco de verdade.

  QUEBRAS DE REFERENCIA (esperam REPROVAR) -- editam o CODIGO da f2-referencia.py.
  Cada uma declara a FRASE que espera ouvir de volta, porque reprovar nao e a mesma
  coisa que reprovar PELO MOTIVO CERTO.

  QUEBRAS DE BANCO (esperam REPROVAR) -- mexem no dado, nao no codigo.

  MORTES (esperam MORRER) -- tiram do esquema uma chave de que a F2 depende e exigem
  que ela LEVANTE em vez de cair num literal.

TRAVA DE ALVO EXATO: toda quebra de referencia declara o TEXTO que vai editar, e
`_referencia_mutada` RECUSA OPERAR se o texto nao estiver mais la. Quando a regra
muda de linha, a mutacao que editava a linha antiga vira INERTE, e sem a trava ela
passa medindo nada enquanto o relatorio diz "0 sobrevivente".
"""

import copy
import importlib.util
import io
import json
import os
import sys
import types

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(AQUI)
DADOS = os.path.join(BASE, "dados")

REFERENCIA = os.path.join(AQUI, "f2-referencia.py")


def _ler(nome):
    with io.open(os.path.join(DADOS, nome), encoding="utf-8") as f:
        return json.load(f)


def _modulo(arquivo, nome):
    spec = importlib.util.spec_from_file_location(nome, os.path.join(AQUI, arquivo))
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def _portao():
    return _modulo("teste-f2.py", "teste_f2")


def _gerador():
    return _modulo("gerar-f2.py", "gerar_f2")


FONTE_DA_REFERENCIA = io.open(REFERENCIA, encoding="utf-8").read()


def _referencia_mutada(trocas=()):
    """Carrega a f2-referencia.py com o codigo editado, de um texto em memoria."""
    fonte = FONTE_DA_REFERENCIA
    for antes, depois in trocas:
        quantas = fonte.count(antes)
        if quantas != 1:
            raise SystemExit(
                "MUTACAO INERTE: o alvo %r aparece %d vezes na f2-referencia.py (tem de "
                "aparecer 1). A regra mudou de linha e esta mutacao parou de medir o que "
                "diz medir." % (antes[:70], quantas))
        fonte = fonte.replace(antes, depois)
    modulo = types.ModuleType("f2_referencia_mutada")
    modulo.__file__ = REFERENCIA
    exec(compile(fonte, REFERENCIA, "exec"), modulo.__dict__)
    return modulo


# ---------------------------------------------------------------------------
# AS FAIXAS DOS MUNDOS
#
# Nenhuma delas e dado real, e NENHUMA e gravada: sao mundos de bancada. Os numeros
# 203.87 e 396.84 sao os dois que o bloco 1 mediu na mesma pagina de resultados, em
# 14/09/2026, e estao aqui porque eles sao o caso que a regra existe para tratar --
# uma media e um minimo, que nao podem virar um intervalo.
# ---------------------------------------------------------------------------

def _faixa(**campos):
    base = {
        "id": "faixa-de-bancada",
        "cidade": "veneza",
        "categoria_de_custo": "hospedagem",
        "padrao": "economico",
        "valor_min": 100,
        "valor_max": 150,
        "moeda": "EUR",
        "base": "por_pessoa_por_dia",
        "base_transcrita_de": "valor por pessoa, por dia",
        "pessoas_por_quarto": None,
        "o_que_o_numero_e": "faixa_publicada",
        "metodo_declarado": "de 100 a 150 euros por pessoa, por dia",
        "publicado_por": "Publicador de bancada",
        "url": "https://exemplo.invalido/bancada",
        "data_leitura": "2026-09-14",
        "status": "publicavel",
    }
    base.update(campos)
    return base


def _tres_categorias(cidade="veneza", padrao="economico"):
    return [
        _faixa(id="bancada-hospedagem", cidade=cidade, padrao=padrao,
               categoria_de_custo="hospedagem"),
        _faixa(id="bancada-alimentacao", cidade=cidade, padrao=padrao,
               categoria_de_custo="alimentacao", valor_min=30, valor_max=60,
               metodo_declarado="de 30 a 60 euros por pessoa, por dia"),
        _faixa(id="bancada-transporte", cidade=cidade, padrao=padrao,
               categoria_de_custo="transporte_local", valor_min=8, valor_max=12,
               metodo_declarado="de 8 a 12 euros por pessoa, por dia"),
    ]


# ---------------------------------------------------------------------------
# OS MUNDOS
# ---------------------------------------------------------------------------

def mundo_com_as_tres_faixas_e_total(banco, esquema, constantes):
    """As quatro linhas existem: a F2 passa a ter TOTAL, e ele tem de fechar.

    E o unico mundo em que o total da F2 e exercitado. Com o banco de hoje o portao
    conta zero estados com total, e um portao que nunca viu o caminho do total nao
    mede o total.
    """
    banco["faixas_diarias"] = _tres_categorias()
    banco["resumo"]["faixas_diarias"] = 3
    banco["resumo"]["faixas_diarias_publicaveis"] = 3
    return banco, esquema, constantes


def mundo_faixa_de_quarto_com_ocupacao(banco, esquema, constantes):
    """Diaria de QUARTO duplo, com a ocupacao declarada: ela escala, e por quartos."""
    banco["faixas_diarias"] = [
        _faixa(id="bancada-quarto", base="por_quarto_por_dia", pessoas_por_quarto=2,
               base_transcrita_de="diária de quarto duplo, para 2 pessoas",
               metodo_declarado="diária de quarto duplo entre 100 e 150 euros"),
    ]
    banco["resumo"]["faixas_diarias"] = 1
    banco["resumo"]["faixas_diarias_publicaveis"] = 1
    return banco, esquema, constantes


def mundo_faixa_de_quarto_sem_ocupacao(banco, esquema, constantes):
    """Diaria de quarto SEM a ocupacao: a linha e RECUSADA, e isso e o certo.

    O portao exige a recusa nomeada em vez da linha. Dividir a diaria pelo tamanho
    do grupo seria escolher a ocupacao no lugar de quem publicou o preco.
    """
    banco["faixas_diarias"] = [
        _faixa(id="bancada-quarto-cego", base="por_quarto_por_dia",
               pessoas_por_quarto=None,
               base_transcrita_de="diária de quarto",
               metodo_declarado="diária de quarto entre 100 e 150 euros"),
    ]
    banco["resumo"]["faixas_diarias"] = 1
    banco["resumo"]["faixas_diarias_publicaveis"] = 1
    return banco, esquema, constantes


def mundo_duas_publicacoes_da_mesma_natureza(banco, esquema, constantes):
    """Dois publicadores dizendo a MESMA coisa: viram um intervalo unico."""
    banco["faixas_diarias"] = [
        _faixa(id="bancada-a", valor_min=100, valor_max=150,
               publicado_por="Primeiro publicador"),
        _faixa(id="bancada-b", valor_min=80, valor_max=200,
               publicado_por="Segundo publicador",
               metodo_declarado="de 80 a 200 euros por pessoa, por dia"),
    ]
    banco["resumo"]["faixas_diarias"] = 2
    banco["resumo"]["faixas_diarias_publicaveis"] = 2
    return banco, esquema, constantes


def mundo_naturezas_em_conflito(banco, esquema, constantes):
    """O CASO MEDIDO, com os dois numeros da mesma pagina de resultados.

    Uma media de periodo e um minimo encontrado, na mesma cidade, categoria e
    padrao. As duas vao para a tela LADO A LADO, com dono, e a F2 recusa o intervalo
    unico. Este e o mundo que a regra existe para tratar.
    """
    banco["faixas_diarias"] = [
        _faixa(id="bancada-media", valor_min=203.87, valor_max=203.87,
               o_que_o_numero_e="media_de_periodo",
               publicado_por="Publicador da media",
               metodo_declarado="média de 203,87 nos últimos 30 dias"),
        _faixa(id="bancada-minimo", valor_min=396.84, valor_max=396.84,
               o_que_o_numero_e="menor_encontrado",
               publicado_por="Publicador do minimo",
               metodo_declarado="a diária mais baixa encontrada foi 396,84"),
    ]
    banco["resumo"]["faixas_diarias"] = 2
    banco["resumo"]["faixas_diarias_publicaveis"] = 2
    return banco, esquema, constantes


def mundo_faixa_nao_publicavel(banco, esquema, constantes):
    """Faixa `pendente_de_releitura`: ela NAO vai para a tela como faixa."""
    banco["faixas_diarias"] = [_faixa(id="bancada-pendente",
                                      status="pendente_de_releitura")]
    banco["resumo"]["faixas_diarias"] = 1
    banco["resumo"]["faixas_diarias_publicaveis"] = 0
    return banco, esquema, constantes


def mundo_faixa_de_outro_padrao(banco, esquema, constantes):
    """Faixa do padrao mochileiro: ela nao aparece nas paginas dos outros dois."""
    banco["faixas_diarias"] = _tres_categorias(padrao="mochileiro")
    banco["resumo"]["faixas_diarias"] = 3
    banco["resumo"]["faixas_diarias_publicaveis"] = 3
    return banco, esquema, constantes


def mundo_empate_de_preco_entre_versoes(banco, esquema, constantes):
    """As duas versoes da gondola pelo MESMO preco: a faixa tem largura zero.

    O portao achou um defeito aqui antes do commit — as duas pontas vinham de
    versoes diferentes com o mesmo numero, e a tela publicava «de A a B» para um
    intervalo que nao e intervalo. Este mundo e a fronteira que aquele conserto
    criou, e ela nao tem como existir no banco de hoje.
    """
    for exp in banco["experiencias"]:
        if exp["id"] == "veneza-passeio-de-gondola":
            for v in exp["versoes"]:
                v["preco"] = 90
    return banco, esquema, constantes


def mundo_cidade_sem_experiencia_lida(banco, esquema, constantes):
    """Uma cidade sem nenhuma experiencia com preco: NENHUMA das quatro linhas sai."""
    banco["experiencias"] = [e for e in banco["experiencias"] if e["cidade"] != "roma"]
    banco["resumo"]["experiencias"] = len(banco["experiencias"])
    banco["resumo"]["versoes"] = sum(len(e["versoes"]) for e in banco["experiencias"])
    banco["resumo"]["faixas_etarias"] = sum(
        1 for e in banco["experiencias"] for v in e["versoes"] if "faixa_etaria" in v)
    return banco, esquema, constantes


def mundo_cidade_com_passe(banco, esquema, constantes):
    """ROMA com um PASSE DE CIDADE no banco, ao lado do ingresso do Coliseu.

    O banco de hoje tem zero passes, entao sem este mundo a regra que a F2 ganhou em
    22/10/2026 — passe nao entra na linha de experiencias — nunca seria executada. O
    defeito que ela consertou foi MEDIDO neste mundo exato: a linha de Roma publicava
    «€100 a €148» para 2 pessoas, que e o ingresso (€36 a €44) mais o passe que inclui
    o ingresso (€64 a €104). O passe e um jeito alternativo de pagar a MESMA visita.
    """
    banco["experiencias"].append({
        "id": "roma-passe-de-bancada",
        "nome": "Passe de Roma (mundo de bancada)",
        "cidade": "roma",
        "categoria": "passe_de_cidade",
        "eixo_das_versoes": "por_quantidade",
        "status": "publicavel",
        "versoes": [
            {"id": "48h", "rotulo": "2 dias", "preco": 32, "moeda": "EUR",
             "unidade_de_preco": "por_pessoa", "capacidade_maxima": None,
             "dias_de_uso": 2, "fonte": "parco-colosseo-tarifa-via-busca",
             "data_leitura": "2026-09-14"},
            {"id": "72h", "rotulo": "3 dias", "preco": 52, "moeda": "EUR",
             "unidade_de_preco": "por_pessoa", "capacidade_maxima": None,
             "dias_de_uso": 3, "fonte": "parco-colosseo-tarifa-via-busca",
             "data_leitura": "2026-09-14"},
        ],
    })
    banco["resumo"]["experiencias"] = len(banco["experiencias"])
    banco["resumo"]["versoes"] = sum(len(e.get("versoes") or [])
                                     for e in banco["experiencias"])
    return banco, esquema, constantes


def mundo_passe_excluido_do_banco(banco, esquema, constantes):
    """O mesmo passe com `excluido_do_banco`: ele nao entra na conta E nao e nomeado.

    Sao duas regras diferentes passando pelo mesmo registro, e so este mundo as separa:
    a recusa do passe existe para o passe que a ilha PUBLICA, nao para o que ela
    descartou — nomear o descartado seria contar ao visitante de um produto que esta
    pagina nao oferece.
    """
    banco, esquema, constantes = mundo_cidade_com_passe(banco, esquema, constantes)
    banco["experiencias"][-1]["status"] = "excluido_do_banco"
    return banco, esquema, constantes


# ---------------------------------------------------------------------------
# AS QUEBRAS DE REFERENCIA — (nome, trocas, frase esperada, mundo)
# ---------------------------------------------------------------------------

QUEBRAS_DE_REFERENCIA = [
    ("o passe volta para dentro da linha de experiencias (a visita paga duas vezes)",
     [('        if exp.get("categoria") == CATEGORIA_DE_PASSE:\n            continue\n        versoes = []',
       '        versoes = []')],
     "aparece no detalhe da linha de experiencias", mundo_cidade_com_passe),

    ("o passe sai da conta mas a recusa fica SEM NOME",
     [('    passes = passes_da_cidade(banco, cidade_id)\n    if passes:',
       '    passes = passes_da_cidade(banco, cidade_id)\n    if False:')],
     "nao NOMEOU a recusa", mundo_cidade_com_passe),

    ("a fonte do passe volta a prestar contas de um numero que a tela nao publica",
     [('        if exp.get("categoria") == CATEGORIA_DE_PASSE:\n            continue\n        for versao in (exp.get("versoes") or []):',
       '        for versao in (exp.get("versoes") or []):')],
     "presta contas da fonte do passe", mundo_cidade_com_passe),

    ("o passe DESCARTADO do banco volta a ser nomeado na recusa",
     [('            and exp.get("status") != "excluido_do_banco"]',
       '            ]')],
     "numa cidade que nao tem passe", mundo_passe_excluido_do_banco),

    ("diaria de quarto multiplicada por PESSOA em vez de por quarto",
     [('        return v * quartos * dias, "%d %s por %s" % (',
       '        return v * pessoas * dias, "%d %s por %s" % (')],
     "escalar_faixa", mundo_faixa_de_quarto_com_ocupacao),

    ("diaria por pessoa que nao multiplica pelo grupo",
     [('        return v * pessoas * dias, "%s por %s" % (f1.pessoas_em_palavra(pessoas),',
       '        return v * dias, "%s por %s" % (f1.pessoas_em_palavra(pessoas),')],
     "escalar_faixa", mundo_com_as_tres_faixas_e_total),

    ("diaria do grupo multiplicada pelo numero de pessoas",
     [('        return v * dias, "pelo grupo, por %s" % f1.dias_em_palavra(dias)',
       '        return v * dias * pessoas, "pelo grupo, por %s" % f1.dias_em_palavra(dias)')],
     "escalar_faixa", mundo_com_as_tres_faixas_e_total),

    ("quarto contado por ARREDONDAMENTO em vez de teto",
     [('    return f1.unidades_necessarias("por_grupo", pessoas_por_quarto, pessoas)',
       '    return max(1, int(round(float(pessoas) / pessoas_por_quarto)))')],
     "quartos_necessarios", mundo_faixa_de_quarto_com_ocupacao),

    ("naturezas DIFERENTES juntadas num grupo so",
     [('            ordem.append(natureza)',
       '            natureza = "faixa_publicada"\n            if natureza in por_natureza:\n                por_natureza[natureza].append(faixa)\n                continue\n            ordem.append(natureza)')],
     "DOIS grupos", mundo_naturezas_em_conflito),

    ("total publicado com as linhas que existem, sem as que faltam",
     [('    if publicadas == completas:',
       '    if publicadas:')],
     "faltam linhas e a F2 publicou total", None),

    ("a linha de experiencias passa a crescer com os dias",
     [('    nossa = faixa_de_experiencias(itens, pessoas)',
       '    nossa = faixa_de_experiencias(itens, pessoas)\n'
       '    if nossa is not None:\n'
       '        nossa["piso"] = nossa["piso"] * dias\n'
       '        nossa["teto"] = nossa["teto"] * dias')],
     "MUDOU com o numero de dias", None),

    ("a ponta de cima do empate volta a escolher o maior id",
     [('        maior = min((t for t in comparaveis if t[0] == maior_total), key=lambda t: t[1])',
       '        maior = max((t for t in comparaveis if t[0] == maior_total), key=lambda t: t[1])')],
     "ESTAVEL", mundo_empate_de_preco_entre_versoes),

    ("a linha nossa se declara de terceiro",
     [('            "procedencia": "nossa",',
       '            "procedencia": "de_terceiro",')],
     "declarar NOSSA", None),

    ("a linha de terceiro se declara nossa",
     [('                "procedencia": "de_terceiro",',
       '                "procedencia": "nossa",')],
     "declarar DE TERCEIRO", mundo_com_as_tres_faixas_e_total),

    ("faixa nao publicavel vai para a tela como faixa",
     [('        if faixa.get("status") != "publicavel":\n            continue\n        if faixa.get("cidade") != cidade_id:',
       '        if False:\n            continue\n        if faixa.get("cidade") != cidade_id:')],
     "nao ha faixa escalavel e a linha saiu", mundo_faixa_nao_publicavel),

    ("faixa de outro padrao aparece na pagina deste",
     [('        if faixa.get("padrao") != padrao:\n            continue',
       '        if False:\n            continue')],
     "nao ha faixa escalavel e a linha saiu", mundo_faixa_de_outro_padrao),

    ("faixa de outra cidade aparece nesta",
     [('        if faixa.get("cidade") != cidade_id:\n            continue',
       '        if False:\n            continue')],
     "nao ha faixa escalavel e a linha saiu", mundo_faixa_de_outro_padrao),

    ("diaria de quarto sem ocupacao ESTIMADA em vez de recusada",
     [('        if pessoas_por_quarto is None:\n            raise BancoIncompleto(',
       '        if pessoas_por_quarto is None:\n            pessoas_por_quarto = 2\n        if False:\n            raise BancoIncompleto(')],
     "nao ha faixa escalavel e a linha saiu", mundo_faixa_de_quarto_sem_ocupacao),

    ("teto de dias trocado de 21 para 60",
     [('DIAS_MAXIMO = 21', 'DIAS_MAXIMO = 60')],
     "a especificacao diz de 1 a 21", None),

    ("cidade que nao existe respondida em vez de recusada",
     [('    cidade = cidades.get(cidade_id)\n    if cidade is None:',
       '    cidade = cidades.get(cidade_id) or {"nome": "Cidade", "pais": "Pais", "moeda_local": "EUR"}\n    if False:')],
     "estado fora da faixa e a F2 NAO recusou", None),

    ("a recusa do total deixa de ser nomeada",
     [('        recusa("total_impossivel",', '        recusa("total_outro_codigo",')],
     "total impossivel sem a recusa nomeada", None),

    ("a recusa da categoria ausente deixa de ser nomeada",
     [('            recusa("sem_faixa_%s" % categoria,', '            recusa("sem_faixa_outro",')],
     "categoria ausente sem recusa nomeada", None),

    ("a recusa do conflito de naturezas deixa de ser nomeada",
     [('            recusa("naturezas_em_conflito_%s" % categoria,',
       '            recusa("naturezas_em_conflito_outro",')],
     "naturezas em conflito sem a recusa nomeada", mundo_naturezas_em_conflito),

    # A mutacao de acento mira uma palavra que a lista do portao da F1 COBRE. A
    # primeira versao desta linha mirava «está» -> «esta», e PASSOU: «esta» e palavra
    # legitima do portugues e nao esta na lista de proposito — regua que tentasse
    # cobrir o idioma reprovaria nome proprio e acabaria desligada por inutil. Mutacao
    # que mira fora da regra nao mede a regra, mede o engano de quem a escreveu.
    ("a frase da tela volta a publicar portugues SEM acento",
     [('                    "que foi lida. A JornadaFly não colheu este número e não o "',
       '                    "que foi lida. A JornadaFly nao colheu este numero e nao o "')],
     "sem acento", mundo_com_as_tres_faixas_e_total),

    ("a frase da tela volta a publicar nome de campo do banco",
     [('               "Esta ilha ainda não leu o preço de nenhuma experiência em %s, "',
       '               "A chave url_busca_produto ainda não leu o preço em %s, "')],
     "bastidor da fabrica", mundo_cidade_sem_experiencia_lida),

    ("a concordancia de «1 experiencia» volta a quebrar",
     [('    return "%d %s" % (n, "experiência" if n == 1 else "experiências")',
       '    return "%d %s" % (n, "experiências")')],
     "concordancia errada", None),

    ("as duas procedencias na MESMA linha",
     [('                "blocos": blocos,', '                "blocos": blocos,\n                "minimo": 1,')],
     "as duas formas ao mesmo tempo", mundo_com_as_tres_faixas_e_total),

    ("o por-pessoa-por-dia do total dividido pelo numero errado",
     [('            "por_pessoa_por_dia": f1._centavo(total_max / Decimal(pessoas) / Decimal(dias)),',
       '            "por_pessoa_por_dia": f1._centavo(total_max / Decimal(pessoas)),')],
     "por pessoa por dia nao bate", mundo_com_as_tres_faixas_e_total),

    ("o intervalo unido deixa de ir do menor piso ao maior teto",
     [('    return (min(t[0] for t in totais), max(t[1] for t in totais))',
       '    return (totais[0][0], totais[0][1])')],
     "menor piso", mundo_duas_publicacoes_da_mesma_natureza),
]


# ---------------------------------------------------------------------------
# AS QUEBRAS QUE MATAM — (nome, trocas, frase esperada, mundo)
#
# Tirar estas tres travas nao faz a F2 responder errado: faz a F2 MORRER, e morrer e
# a reacao honesta. A bateria as separou das quebras depois de medir, em 22/10/2026,
# que as tres davam `morre` onde a lista dizia `reprova` — e uma mutacao classificada
# errado e um relatorio vermelho sem defeito embaixo, que e o jeito mais rapido de uma
# bancada ser desligada.
# ---------------------------------------------------------------------------

QUEBRAS_QUE_MATAM = [
    ("a guarda da experiencia sem preco sai: min() de lista vazia",
     [('        if not comparaveis:', '        if False:')],
     "empty sequence", mundo_cidade_sem_experiencia_lida),

    ("a guarda do padrao desconhecido sai: a tela procura um rotulo que nao existe",
     [('    if padrao not in padroes(esquema):', '    if False:')],
     "padrao_que_nao_existe", None),

    ("transporte local sai da lista de tela e o vocabulario denuncia",
     [('CATEGORIAS_DE_TERCEIRO = ("hospedagem", "alimentacao", "transporte_local")',
       'CATEGORIAS_DE_TERCEIRO = ("hospedagem", "alimentacao")')],
     "nao cobre o vocabulario", None),

    ("a categoria do passe sai do vocabulario do esquema e o descarte fica cego",
     [('CATEGORIA_DE_PASSE = "passe_de_cidade"',
       'CATEGORIA_DE_PASSE = "passe_que_nao_esta_no_vocabulario"')],
     "nao esta no vocabulario", None),
]


# ---------------------------------------------------------------------------
# AS QUEBRAS DE BANCO — (nome, funcao, frase esperada)
#
# VAZIA de proposito, e a lista vazia e decisao e nao esquecimento: quebrar o DADO de
# uma faixa (teto menor que piso, categoria fora do vocabulario, ocupacao que a frase
# nao declara) nao e trabalho desta bateria, porque quem reprova isso e
# ferramentas/validar-banco.py — e sao as 24 mutacoes novas de
# ferramentas/mutacoes-banco.py que o cobram, uma por regra. Repetir aqui daria DUAS
# baterias medindo o mesmo, com a certeza de que uma das duas envelheceria sozinha.
# Esta bateria mede o que e da F2: a CONTA, a RECUSA e a FRASE.
# ---------------------------------------------------------------------------

QUEBRAS_DE_BANCO = []


# ---------------------------------------------------------------------------
# AS MORTES — a chave sai da fonte e a referencia tem de LEVANTAR
# ---------------------------------------------------------------------------

def morte_sem_vocabulario_de_padrao(banco, esquema, constantes):
    del esquema["vocabularios"]["padrao_de_viagem"]
    return banco, esquema, constantes


def morte_sem_vocabulario_de_categoria_de_custo(banco, esquema, constantes):
    del esquema["vocabularios"]["categoria_de_custo"]
    return banco, esquema, constantes


def morte_sem_vocabulario_de_base(banco, esquema, constantes):
    del esquema["vocabularios"]["base_da_faixa"]
    return banco, esquema, constantes


def morte_sem_vocabulario_de_natureza(banco, esquema, constantes):
    del esquema["vocabularios"]["o_que_o_numero_e"]
    return banco, esquema, constantes


def morte_com_padrao_novo_sem_forma_de_escrita(banco, esquema, constantes):
    """Padrao novo no vocabulario e sem rotulo na F2: a tela publicaria o codigo cru."""
    esquema["vocabularios"]["padrao_de_viagem"].append("luxo")
    return banco, esquema, constantes


def morte_com_base_nova_sem_conta(banco, esquema, constantes):
    esquema["vocabularios"]["base_da_faixa"].append("por_semana")
    return banco, esquema, constantes


def morte_sem_moeda_no_vocabulario(banco, esquema, constantes):
    esquema["vocabularios"]["moeda"] = ["USD"]
    return banco, esquema, constantes


MORTES = [
    ("sem vocabulario `padrao_de_viagem`", morte_sem_vocabulario_de_padrao),
    ("sem vocabulario `categoria_de_custo`", morte_sem_vocabulario_de_categoria_de_custo),
    ("sem vocabulario `base_da_faixa`", morte_sem_vocabulario_de_base),
    ("sem vocabulario `o_que_o_numero_e`", morte_sem_vocabulario_de_natureza),
    ("padrao novo no esquema sem forma de escrita na F2",
     morte_com_padrao_novo_sem_forma_de_escrita),
    ("base nova no esquema sem conta na F2", morte_com_base_nova_sem_conta),
    ("moeda do banco fora do vocabulario", morte_sem_moeda_no_vocabulario),
]

MUNDOS = [
    ("cidade com PASSE no banco: ele nao entra na conta e e nomeado",
     mundo_cidade_com_passe),
    ("passe excluido do banco: fora da conta e sem ser nomeado",
     mundo_passe_excluido_do_banco),
    ("as tres faixas carregadas: a F2 tem TOTAL", mundo_com_as_tres_faixas_e_total),
    ("diaria de quarto COM ocupacao declarada", mundo_faixa_de_quarto_com_ocupacao),
    ("diaria de quarto SEM ocupacao: linha recusada", mundo_faixa_de_quarto_sem_ocupacao),
    ("dois publicadores da mesma natureza", mundo_duas_publicacoes_da_mesma_natureza),
    ("media e minimo lado a lado, sem intervalo unico", mundo_naturezas_em_conflito),
    ("faixa pendente de releitura fora da tela", mundo_faixa_nao_publicavel),
    ("faixa de outro padrao", mundo_faixa_de_outro_padrao),
    ("empate de preco entre as versoes", mundo_empate_de_preco_entre_versoes),
    ("cidade sem experiencia lida", mundo_cidade_sem_experiencia_lida),
]


def _rodar(portao, gerador, f2, banco, esquema, constantes):
    """Roda o portao sobre um mundo, com o arquivo de respostas GERADO daquele mundo.

    Gerar o arquivo junto e o que impede a mutacao de reprovar pelo motivo errado:
    sem isto, toda quebra reprovaria tambem na secao 5 do portao (o arquivo gravado
    discordando do mundo mutado), e nenhuma provaria reprovar pela sua propria
    afirmacao.
    """
    try:
        doc = gerador.montar(f2, banco, esquema, constantes)
    except Exception as erro:
        return "morre", ["%s: %s" % (type(erro).__name__, erro)]
    try:
        falhas, _ = portao.conferir(f2, banco, esquema, constantes, doc)
    except Exception as erro:
        return "morre", ["%s: %s" % (type(erro).__name__, erro)]
    return ("reprova" if falhas else "passa"), falhas


def main():
    portao = _portao()
    gerador = _gerador()
    banco = _ler("experiencias.json")
    esquema = _ler("esquema-banco.json")
    constantes = _ler("constantes.json")

    f2 = _referencia_mutada()
    decidiu, falhas = _rodar(portao, gerador, f2, copy.deepcopy(banco), copy.deepcopy(esquema),
                             copy.deepcopy(constantes))
    if decidiu != "passa":
        print("O MUNDO REAL JA ESTA REPROVADO — nenhuma mutacao mede nada assim (%s):"
              % decidiu)
        for f in falhas[:10]:
            print("  - %s" % f)
        return 1

    resultados = []
    com_frase = 0

    for nome, funcao in MUNDOS:
        f2 = _referencia_mutada()
        b, e, c = funcao(copy.deepcopy(banco), copy.deepcopy(esquema),
                         copy.deepcopy(constantes))
        decidiu, falhas = _rodar(portao, gerador, f2, b, e, c)
        resultados.append((nome, "passa", decidiu, falhas, None))

    for nome, trocas, frase, mundo in QUEBRAS_DE_REFERENCIA:
        f2 = _referencia_mutada(trocas)
        b, e, c = (copy.deepcopy(banco), copy.deepcopy(esquema), copy.deepcopy(constantes))
        if mundo is not None:
            b, e, c = mundo(b, e, c)
        decidiu, falhas = _rodar(portao, gerador, f2, b, e, c)
        resultados.append((nome, "reprova", decidiu, falhas, frase or None))
        if frase:
            com_frase += 1

    for nome, trocas, frase, mundo in QUEBRAS_QUE_MATAM:
        f2 = _referencia_mutada(trocas)
        b, e, c = (copy.deepcopy(banco), copy.deepcopy(esquema), copy.deepcopy(constantes))
        if mundo is not None:
            b, e, c = mundo(b, e, c)
        decidiu, falhas = _rodar(portao, gerador, f2, b, e, c)
        resultados.append((nome, "morre", decidiu, falhas, frase or None))
        if frase:
            com_frase += 1

    for nome, funcao, frase in QUEBRAS_DE_BANCO:
        f2 = _referencia_mutada()
        b, e, c = funcao(copy.deepcopy(banco), copy.deepcopy(esquema),
                         copy.deepcopy(constantes))
        decidiu, falhas = _rodar(portao, gerador, f2, b, e, c)
        resultados.append((nome, "reprova", decidiu, falhas, frase))
        if frase:
            com_frase += 1

    for nome, funcao in MORTES:
        f2 = _referencia_mutada()
        b, e, c = funcao(copy.deepcopy(banco), copy.deepcopy(esquema),
                         copy.deepcopy(constantes))
        decidiu, falhas = _rodar(portao, gerador, f2, b, e, c)
        resultados.append((nome, "morre", decidiu, falhas, None))

    erradas = []
    for nome, espera, decidiu, falhas, frase in resultados:
        marca = "ok " if decidiu == espera else "NAO"
        if decidiu != espera:
            erradas.append((nome, espera, decidiu, falhas))
        elif frase is not None and not any(frase in f for f in falhas):
            marca = "NAO"
            erradas.append((nome + " (reprovou, mas nao pela frase %r)" % frase,
                            espera, decidiu, falhas))
        print("  %s  %-62s espera %-8s deu %s" % (marca, nome[:62], espera, decidiu))

    print("\n%d mutacoes: %d mundos que tem de PASSAR, %d quebras que tem de REPROVAR "
          "e %d mortes que tem de MATAR a referencia."
          % (len(resultados), len(MUNDOS),
             len(QUEBRAS_DE_REFERENCIA) + len(QUEBRAS_DE_BANCO),
             len(MORTES) + len(QUEBRAS_QUE_MATAM)))
    print("%d delas declaram a FRASE que esperam ouvir de volta, e foram cobradas por ela."
          % com_frase)

    if erradas:
        print("")
        for nome, espera, decidiu, falhas in erradas:
            print("  ERRADA: %s — esperava %s, deu %s" % (nome, espera, decidiu))
            for f in falhas[:3]:
                print("      %s" % f[:200])
        print("\n%d mutacao(oes) decidiram errado." % len(erradas))
        return 1
    print("Todas decidiram certo, nos TRES lados da fronteira.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
