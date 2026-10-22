#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""F3 -- O PASSE DA CIDADE VALE A PENA PARA VOCE. Implementacao de REFERENCIA.

Bloco 5 da jornadafly, terceira e ultima ferramenta das tres ancoras. Dado um
estado de entrada (cidade, atracoes pretendidas, dias, pessoas) este arquivo
devolve a resposta inteira -- a soma dos avulsos, o preco de cada passe, o valor
que cada passe entrega sobre o que esta ilha LEU que ele cobre, o ponto de
equilibrio em numero de atracoes e o veredito -- ja em frase acentuada, do jeito
que o visitante le.

    python3 ferramentas/f3-referencia.py                     # uma resposta de exemplo
    python3 ferramentas/f3-referencia.py --contar            # o tamanho do dominio
    python3 ferramentas/f3-referencia.py <cidade> <dias> <pessoas> <atracao>[,<atracao>]

POR QUE PYTHON E NAO PHP: a mesma decisao dos blocos 4 e da F2, e ela nao mudou.
Esta ilha nao tem site, nao tem WordPress, nao tem Sync e nao tem /status, e o
dominio dela nao esta na lista de dominios liberados deste ambiente -- remedido
hoje, 22/10/2026, com recusa do tunel em seis medicoes e aquametria.com.br e
robometria.com.br em 200 nas mesmas passadas. O PHP, quando nascer, e TRADUTOR
desta referencia frase a frase.

A VAGA QUE ESTA FERRAMENTA OCUPA E ESTREITA, E A ESPECIFICACAO (4) A MEDIU
----------------------------------------------------------------------------
O 1o colocado de «Roma Pass vale a pena» promete «fiz as contas pra voce» no
proprio titulo: o formato -- soma dos avulsos contra o preco do passe, com ponto
de equilibrio -- JA ESTA ENTREGUE por quem ocupa o topo. Nao ha vaga de formato.
A vaga e de ATUALIDADE e de HONESTIDADE DA BASE:

  - de atualidade, porque passe cuja regra de reserva muda e passe cujo artigo
    envelhece, e a fonte de topo do Roma Pass avisa que as regras mudaram em 2026
    (medido no bloco 1, 14/09/2026). Esta ferramenta publica a data de leitura de
    CADA preco avulso e de CADA cobertura, e diz quando a leitura venceu;
  - de honestidade da base, e esta e a maior: o ponto de equilibrio que todos
    publicam sai de uma lista de atracoes que ninguem mostra. Aqui ele sai das
    coberturas que esta ilha LEU, com o numero delas ao lado do numero que o
    proprio passe declara cobrir.

AS TRES REGRAS QUE ATRAVESSAM ESTE ARQUIVO (esquema, `regra_da_cobertura_do_passe`)

  1. NAO LIDA NAO E NAO COBERTA. Atracao pretendida sem COBERTURA_DO_PASSE fica
     fora do valor entregue E e nomeada na tela como nao lida. Trata-la como nao
     coberta publica um «nao paga» que a ilha nao mediu; trata-la como coberta
     publica o contrario. As duas sao erradas.
  2. O EQUILIBRIO E SOBRE O QUE A ILHA LEU, NUNCA SOBRE O PASSE. Os dois numeros
     vao para a tela lado a lado, e a frase do equilibrio diz sobre quantas
     atracoes ele foi calculado.
  3. DESCONTO COM TETO E FAIXA. «Ate 50%» entrega de ZERO a metade do avulso, e as
     duas pontas vao para a tela. E a mesma troca do `o_que_o_numero_e` da
     FAIXA_DIARIA: o que sai da prosa para o campo nao e o numero, e O QUE O
     NUMERO E.

O QUE ESTE ARQUIVO NAO FAZ, de proposito:

  - NAO ESCOLHE A VERSAO DA ATRACAO, como a F2 nao escolhe. Quando a fonte do
    passe diz «entrada no Coliseu» e o Coliseu tem dois bilhetes, o valor entregue
    e uma FAIXA e a tela diz quais sao as pontas.
  - NAO DA VEREDITO QUANDO A FAIXA ATRAVESSA O PRECO DO PASSE. Ali existe versao em
    que ele paga e versao em que nao paga, e as duas sao verdade. A F3 publica os
    dois numeros e diz que o veredito depende de qual bilhete.
  - NAO SOMA BENEFICIO DE FILA COMO DINHEIRO. Cobertura `sem_efeito_no_preco`
    entrega ZERO, e zero declarado e diferente de ausencia.
  - NAO RATEIA O PASSE PELOS DIAS. Passe de 2 dias numa estadia de 7 cobre 2 dias,
    e a F3 diz isso em vez de dividir: o preco do passe nao e por dia.
  - NAO INVENTA O EQUILIBRIO SEM COBERTURA. Passe sem nenhuma cobertura lida tem
    preco publicado e NAO tem equilibrio. Supor cobertura seria inventar o produto
    do passe.
  - NAO PUBLICA VALOR EM REAL, pelo mesmo motivo da F1 e da F2: as duas constantes
    de cambio estao pendentes, e constante pendente e proibida dentro de formula
    publicada.
  - NAO PUBLICA FRASE DE INEXISTENCIA SOBRE COBERTURA. O vocabulario
    `forma_de_cobertura` nasceu sem lastro (zero registros), e a
    `regra_de_crescimento_de_vocabulario` proibe a tela de afirmar que algo nao
    existe enquanto for assim. A F3 diz «esta ilha nao leu», que e outra frase.

POR QUE ELA IMPORTA A F2 E A F2 IMPORTA A F1: a faixa de preco de uma atracao
entre as versoes dela -- com o desempate das duas pontas para o mesmo lado, que
e conserto medido em 22/10/2026 -- mora em `f2.faixa_de_experiencias`, e a
normalizacao de unidade e o degrau de capacidade moram na F1. Tres copias da
mesma conta seriam tres regras que divergem no dia em que uma delas mudar.
"""

import importlib.util
import os
import sys
from decimal import Decimal

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(AQUI)
DADOS = os.path.join(BASE, "dados")


def _carregar(arquivo, nome):
    """Carrega por CAMINHO porque o nome do arquivo tem hifen."""
    caminho = os.path.join(AQUI, arquivo)
    spec = importlib.util.spec_from_file_location(nome, caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


f2 = _carregar("f2-referencia.py", "f2_referencia")
f1 = f2.f1
BancoIncompleto = f1.BancoIncompleto

ESQUEMA = os.path.join(DADOS, "esquema-banco.json")
BANCO = os.path.join(DADOS, "experiencias.json")

# A faixa de dias da F3 e a MESMA da F2, e ela e importada em vez de repetida: as
# duas respondem sobre a mesma estadia, e dois tetos para o mesmo fato divergiriam
# no dia em que um deles mudasse. Quem muda o teto muda a especificacao primeiro.
DIAS_MINIMO = f2.DIAS_MINIMO
DIAS_MAXIMO = f2.DIAS_MAXIMO

# Os dias e os grupos da TABELA PRE-RENDERIZADA. As bordas de dentro entram porque
# tabela que nao mostra a borda esconde o degrau que esta ali.
DIAS_DA_TABELA = (1, 3, 7, 21)
PESSOAS_DA_TABELA = (1, 2, 4)

# O teto de atracoes que a tela oferece de uma vez. Nao e limite de banco: e limite
# de ESCOLHA, e ele existe porque o dominio desta ferramenta cresce em 2^n -- cada
# atracao nova dobra o numero de combinacoes possiveis. Com 8 atracoes numa cidade
# sao 255 subconjuntos; com 12 seriam 4.095, e a grade do portao deixaria de caber
# numa passada. O numero esta na especificacao (4.1) e e conferido contra ela.
ATRACOES_MAXIMO = 8

# Como cada forma de cobertura se ESCREVE na tela, acentuada. A lista e conferida
# contra o vocabulario do esquema NAS DUAS DIRECOES: forma nova no esquema sem
# escrita aqui publicaria o codigo cru, e escrita aqui sem valor no esquema e tela
# para um mundo que o esquema nao permite mais.
ROTULO_DA_COBERTURA = {
    "entrada_incluida": "entrada incluída",
    "desconto_declarado": "desconto declarado",
    "sem_efeito_no_preco": "sem efeito no preço",
}

# E o que cada forma ENTREGA, em frase, para a tela dizer do que se trata em vez de
# repetir o codigo do campo.
O_QUE_A_COBERTURA_ENTREGA = {
    "entrada_incluida": "o passe paga a entrada",
    "desconto_declarado": "o passe abate um percentual da entrada",
    "sem_efeito_no_preco": "o passe dá outro benefício e não abate nada do preço",
}


# ---------------------------------------------------------------------------
# CARGA, e a conferencia das listas desta ferramenta contra o esquema
# ---------------------------------------------------------------------------

def carregar_esquema():
    return f1.carregar_esquema()


def carregar_banco():
    return f1.carregar_banco()


def carregar_constantes():
    return f1.carregar_constantes()


def conferir_vocabularios(esquema):
    """As listas desta ferramenta contra as do esquema, nas duas direcoes."""
    faltas = []
    vocabulario = f1.vocabulario(esquema, "forma_de_cobertura")
    for valor in vocabulario:
        if valor not in ROTULO_DA_COBERTURA:
            faltas.append("`%s` do vocabulario `forma_de_cobertura` sem forma de escrita "
                          "na F3" % valor)
        if valor not in O_QUE_A_COBERTURA_ENTREGA:
            faltas.append("`%s` do vocabulario `forma_de_cobertura` sem frase do que "
                          "entrega" % valor)
    for valor in ROTULO_DA_COBERTURA:
        if valor not in vocabulario:
            faltas.append("`%s` tem forma de escrita na F3 e nao esta no vocabulario "
                          "`forma_de_cobertura`" % valor)

    # A CATEGORIA DO PASSE vem da F2, nao de um segundo literal aqui: as duas
    # ferramentas falam do mesmo registro do banco, e dois nomes para ele seriam duas
    # metades que divergem na primeira troca.
    if f2.CATEGORIA_DE_PASSE not in f1.vocabulario(esquema, "categoria"):
        faltas.append(
            "a F3 procura passes pela categoria `%s` e ela nao esta no vocabulario "
            "`categoria` do esquema. Sem o valor no esquema a F3 nao acha passe nenhum "
            "e diria, em toda cidade, que a ilha nao leu passe — quando o que falta e o "
            "vocabulario." % f2.CATEGORIA_DE_PASSE)

    # E as tres regras, lidas do esquema (26.2): a regua le a lista DELE. Sem a chave,
    # a F3 publicaria as tres frases de honestidade sem nada que as sustente.
    regra = esquema.get("regra_da_cobertura_do_passe") or {}
    if len(regra.get("as_tres_regras") or []) != 3:
        faltas.append(
            "esquema: `regra_da_cobertura_do_passe.as_tres_regras` nao tem as tres. Elas "
            "sao o que esta ferramenta publica, e regra que a ferramenta carrega sem o "
            "esquema guardar e regra que a proxima execucao apaga sem saber.")

    faltas += f1.conferir_moedas_do_vocabulario(esquema)
    faltas += f1.conferir_unidades_do_vocabulario(esquema)
    return faltas


def das_atracoes(n):
    """«da única atração» / «das 3 atrações» — a forma com preposicao contraida.

    Existe porque `atracoes_em_palavra` sozinha produz «dentro das 1 atração», que e a
    MESMA familia do «as 1 experiencias» da F2 e do «por veiculo» sem acento da F1. A
    terceira vez que esta pasta paga a concordancia, e a terceira vez que quem a pegou
    foi a leitura da FRASE e nao a do codigo.
    """
    return "da \u00fanica atra\u00e7\u00e3o" if n == 1 else "das %d atra\u00e7\u00f5es" % n


def de_quantas_atracoes(n):
    """«da única que esta ilha leu» / «das 3 que esta ilha leu»."""
    return ("da \u00fanica que esta ilha leu" if n == 1
            else "das %d que esta ilha leu" % n)


def essas_atracoes(n):
    """«essa única» / «essas 3»."""
    return "essa \u00fanica" if n == 1 else "essas %d" % n


def atracoes_em_palavra(n):
    """«1 atracao» / «3 atracoes», com a concordancia certa.

    Existe pelo mesmo motivo do `experiencias_em_palavra` da F2: a primeira versao
    daquela ferramenta publicou «as 1 experiencias que esta ilha leu», e a
    concordancia nao se ve lendo o codigo — se ve lendo a FRASE, que e por isso que o
    portao desta ferramenta le a frase.
    """
    return "%d %s" % (n, "atração" if n == 1 else "atrações")


# ---------------------------------------------------------------------------
# AS CONTAS, COMO FUNCOES PURAS
#
# Nenhuma delas varre o banco. E a regra da secao 8 do ARQUIPELAGO.md: recusa que
# depende de uma RELACAO entre os dados -- ausencia, empate, faixa que atravessa o
# preco, cobertura nao lida -- mora numa funcao pura que recebe a relacao JA
# calculada, senao ela so e testavel no dia em que o banco produzir o caso, e e esse
# o dia em que ela vai estar errada. O banco de hoje tem ZERO passes e ZERO
# coberturas: sem estas funcoes puras, a ferramenta inteira seria uma frase que nada
# confere.
# ---------------------------------------------------------------------------

def valor_entregue(piso_do_avulso, teto_do_avulso, como,
                   desconto_percentual=None, desconto_e_no_maximo=None):
    """O que o passe entrega NAQUELA atracao. Funcao pura. Devolve (piso, teto).

    `piso_do_avulso` e `teto_do_avulso` sao o preco da atracao para o grupo, nas duas
    pontas das versoes dela. O que esta funcao faz e aplicar a FORMA da cobertura:

      - `entrada_incluida`: entrega o avulso inteiro, nas duas pontas;
      - `desconto_declarado` com `desconto_e_no_maximo` falso: entrega o percentual
        cheio das duas pontas;
      - `desconto_declarado` com `desconto_e_no_maximo` VERDADEIRO: entrega de ZERO ao
        percentual do teto. «Ate 50%» nao e 50%, e sem esta ponta de baixo a hedge da
        fonte entraria na conta como numero cheio -- continuando a parecer dinheiro,
        que e por que esse erro nao se ve;
      - `sem_efeito_no_preco`: entrega ZERO nas duas pontas. Zero DECLARADO, que e
        diferente de ausencia: a atracao entra na conta valendo nada, e a tela diz que
        o beneficio existe e nao e dinheiro.
    """
    if piso_do_avulso is None or teto_do_avulso is None:
        raise BancoIncompleto(
            "valor_entregue sem o preco do avulso: nao ha conta a fazer, e a F3 tem de "
            "dizer isso em vez de publicar zero.")
    piso = Decimal(str(piso_do_avulso))
    teto = Decimal(str(teto_do_avulso))
    if teto < piso:
        raise BancoIncompleto(
            "valor_entregue com teto %s menor que piso %s: faixa invertida publica um "
            "intervalo vazio com cara de intervalo." % (teto, piso))

    if como == "entrada_incluida":
        return piso, teto
    if como == "sem_efeito_no_preco":
        return Decimal(0), Decimal(0)
    if como == "desconto_declarado":
        if not isinstance(desconto_percentual, (int, float)) \
                or isinstance(desconto_percentual, bool) \
                or desconto_percentual <= 0 or desconto_percentual >= 100:
            raise BancoIncompleto(
                "cobertura por desconto com `desconto_percentual` %r: a F3 nao escolhe "
                "percentual por conta propria." % (desconto_percentual,))
        if not isinstance(desconto_e_no_maximo, bool):
            raise BancoIncompleto(
                "cobertura por desconto sem `desconto_e_no_maximo`: sem este campo a F3 "
                "nao sabe se «50%» e cinquenta por cento ou «ate cinquenta por cento», e "
                "as duas leituras dao contas diferentes.")
        fator = Decimal(str(desconto_percentual)) / Decimal(100)
        if desconto_e_no_maximo:
            return Decimal(0), teto * fator
        return piso * fator, teto * fator
    raise BancoIncompleto(
        "forma de cobertura %r sem conta definida. A F3 nao escolhe conta por conta "
        "propria: forma nova entra no vocabulario do esquema e na conta desta "
        "ferramenta na mesma passada." % (como,))


def ponto_de_equilibrio_em_atracoes(valores, preco_do_passe):
    """A CONTA DA F3. Funcao pura sobre a relacao ja calculada.

    `valores` e a lista do que o passe entrega em CADA atracao coberta e lida, numa
    das pontas da faixa; `preco_do_passe` e o que o passe custa para o grupo. Devolve
    {quantas, acumulado, ordem} ou None quando o passe nao se paga nem com TODAS as
    atracoes que esta ilha leu.

    A ORDEM E DAS MAIS CARAS PARA AS MAIS BARATAS, e isto e uma DECISAO declarada e
    nao uma otimizacao escondida: e a ordem em que o passe rende mais, e portanto a
    que da o MENOR numero de atracoes necessarias. Dizer «a partir de 3 atracoes o
    passe paga» sem dizer QUAIS 3 seria um numero sem dono -- e por isso a funcao
    devolve a `ordem` que usou, para a tela nomear as atracoes.

    Valor ZERO (cobertura sem efeito no preco) fica no fim da ordem e nunca ajuda,
    que e exatamente o que ele e.
    """
    if not isinstance(preco_do_passe, (int, float, Decimal)) or isinstance(preco_do_passe, bool):
        raise BancoIncompleto(
            "ponto_de_equilibrio_em_atracoes com preco do passe %r." % (preco_do_passe,))
    preco = Decimal(str(preco_do_passe))
    if preco <= 0:
        raise BancoIncompleto(
            "ponto_de_equilibrio_em_atracoes com preco do passe %s: passe de graca nao "
            "tem ponto de equilibrio, tem ausencia de pergunta." % preco)
    if not valores:
        return None

    # A ordem desempata pelo INDICE de entrada quando dois valores sao iguais, e esse
    # desempate e o mesmo da faixa de largura zero um andar acima: sem ele, duas
    # atracoes de preco igual trocariam de lugar entre duas cargas e a tela nomearia
    # uma atracao diferente a cada vez, sem nenhum numero mudar.
    ordem = sorted(range(len(valores)),
                   key=lambda i: (-Decimal(str(valores[i])), i))
    acumulado = Decimal(0)
    for posicao, indice in enumerate(ordem, start=1):
        acumulado += Decimal(str(valores[indice]))
        if acumulado >= preco:
            return {"quantas": posicao, "acumulado": acumulado,
                    "ordem": [ordem[i] for i in range(posicao)]}
    return None


def veredito(piso_entregue, teto_entregue, preco_do_passe):
    """TRES desfechos, nao dois. Funcao pura. Devolve (codigo, folga_no_piso).

    `paga`: o passe se paga ate na ponta de BAIXO da faixa -- qualquer bilhete que a
    pessoa comprar, ele compensa. `nao_paga`: ele nao se paga nem na ponta de CIMA.
    `depende_da_versao`: a faixa ATRAVESSA o preco do passe, e ali existe bilhete em
    que ele paga e bilhete em que nao paga. As duas sao verdade, e escolher uma seria
    a ilha escolhendo a versao no lugar de quem viaja.

    O terceiro desfecho e a licao da ohmetria de 22/10/2026 um andar acima, onde a
    tela passou a separar TRES casos onde a especificacao previa dois: quem separa as
    duas causas no codigo separa as duas no texto.
    """
    piso = Decimal(str(piso_entregue))
    teto = Decimal(str(teto_entregue))
    preco = Decimal(str(preco_do_passe))
    if teto < piso:
        raise BancoIncompleto(
            "veredito com teto %s menor que piso %s." % (teto, piso))
    if piso >= preco:
        return "paga", piso - preco
    if teto >= preco:
        return "depende_da_versao", None
    return "nao_paga", None


def cobertura_do_par(coberturas, passe_id, atracao_id):
    """A cobertura lida daquele par, ou None. Funcao pura sobre a lista.

    None quer dizer NAO LIDA, nunca NAO COBERTA -- e a diferenca entre as duas e a
    primeira das tres regras do esquema. Cobertura `excluido_do_banco` conta como nao
    lida: ela foi descartada, e descartada nao sustenta afirmacao nenhuma.
    """
    for cob in (coberturas or []):
        if cob.get("passe") != passe_id or cob.get("experiencia") != atracao_id:
            continue
        if cob.get("status") == "excluido_do_banco":
            continue
        return cob
    return None


# ---------------------------------------------------------------------------
# LEITURA DO BANCO
# ---------------------------------------------------------------------------

def atracoes_da_cidade(banco, cidade_id):
    """As atracoes (nao-passes) daquela cidade, na ordem do banco.

    `pendente_de_releitura` ENTRA com ressalva, como na F1 e na F2: preco lido e nao
    reconferido continua sendo preco lido, e some-lo faria a experiencia desaparecer
    entre uma pagina e a outra. So `excluido_do_banco` fica fora.
    """
    return [exp for exp in (banco.get("experiencias") or [])
            if exp.get("cidade") == cidade_id
            and exp.get("status") != "excluido_do_banco"
            and exp.get("categoria") != f2.CATEGORIA_DE_PASSE]


def passes_da_cidade(banco, cidade_id):
    """Os passes daquela cidade, na ordem do banco. So leitura."""
    return [exp for exp in (banco.get("experiencias") or [])
            if exp.get("cidade") == cidade_id
            and exp.get("status") != "excluido_do_banco"
            and exp.get("categoria") == f2.CATEGORIA_DE_PASSE]


def _item_para_a_faixa(exp):
    """O registro no formato que `f2.faixa_de_experiencias` recebe."""
    versoes = [(v.get("id"), v.get("rotulo"), v.get("preco"), v.get("unidade_de_preco"),
                v.get("capacidade_maxima")) for v in (exp.get("versoes") or [])]
    return (exp.get("id"), exp.get("nome"), versoes, exp.get("status"))


def faixa_do_avulso(exp, pessoas):
    """A faixa de preco de UMA atracao para o grupo, com as pontas nomeadas.

    Delega para `f2.faixa_de_experiencias` com uma lista de UM item -- de proposito:
    o desempate das duas pontas para o mesmo lado (preco empatado da ponta unica em
    vez de uma faixa de largura zero) e conserto medido em 22/10/2026, e escrever a
    segunda copia dele aqui seria garantir que uma das duas envelheceria sozinha.
    Devolve None quando a atracao nao tem preco lido.
    """
    faixa = f2.faixa_de_experiencias([_item_para_a_faixa(exp)], pessoas)
    if faixa is None:
        return None
    detalhe = faixa["detalhe"][0]
    return {"piso": faixa["piso"], "teto": faixa["teto"], "detalhe": detalhe}


def versao_de(exp, versao_id):
    return f1.versao_de(exp, versao_id)


def _total_da_versao(versao, pessoas):
    total, _por_pessoa, _unidades = f1.total_do_grupo(
        versao.get("preco"), versao.get("unidade_de_preco"),
        versao.get("capacidade_maxima"), pessoas)
    return total


# ---------------------------------------------------------------------------
# A RESPOSTA
# ---------------------------------------------------------------------------

def responder(cidade_id, atracoes, dias, pessoas, banco=None, esquema=None,
              constantes=None, hoje=None):
    banco = banco if banco is not None else carregar_banco()
    esquema = esquema if esquema is not None else carregar_esquema()
    constantes = constantes if constantes is not None else carregar_constantes()
    hoje = hoje if hoje is not None else _hoje()

    faltas = conferir_vocabularios(esquema)
    if faltas:
        raise BancoIncompleto(
            "a F3 e o vocabulario do esquema discordam: %s. Vocabulario novo entra no "
            "esquema e na ferramenta na mesma passada." % "; ".join(faltas))

    cidades, fontes, por_id = f1.indexar(banco)
    escolhidas = list(atracoes or [])

    resposta = {
        "estado": {"cidade": cidade_id, "atracoes": list(escolhidas),
                   "dias": dias, "pessoas": pessoas},
        "recusa_dura": None,
        "frase_resposta": None,
        "avulsos": None,
        "passes": [],
        "recusas": [],
        "como_sabemos": None,
    }

    def recusa(codigo, frase):
        resposta["recusas"].append({"codigo": codigo, "frase": frase})

    # ---- AS RECUSAS DURAS: elas nao publicam numero nenhum.
    if not isinstance(dias, int) or isinstance(dias, bool) \
            or dias < DIAS_MINIMO or dias > DIAS_MAXIMO:
        resposta["recusa_dura"] = {
            "codigo": "dias_fora_da_faixa",
            "frase": ("A JornadaFly responde para estadias de %d a %d dias. Acima de %d a "
                      "conta deixa de ser de viagem e passa a ser de moradia, e passe de "
                      "cidade não é o produto de quem fica um mês."
                      % (DIAS_MINIMO, DIAS_MAXIMO, DIAS_MAXIMO)),
        }
        return resposta

    if not isinstance(pessoas, int) or isinstance(pessoas, bool) \
            or pessoas < f1.PESSOAS_MINIMO or pessoas > f1.PESSOAS_MAXIMO:
        resposta["recusa_dura"] = {
            "codigo": "grupo_fora_da_faixa",
            "frase": ("A JornadaFly responde para grupos de %d a %d pessoas. Acima de %d a "
                      "compra vira negociação com quem opera, e multiplicar o preço de "
                      "tabela daria um número que ninguém vai cobrar de você."
                      % (f1.PESSOAS_MINIMO, f1.PESSOAS_MAXIMO, f1.PESSOAS_MAXIMO)),
        }
        return resposta

    cidade = cidades.get(cidade_id)
    if cidade is None:
        resposta["recusa_dura"] = {
            "codigo": "cidade_desconhecida",
            "frase": ("A JornadaFly não tem esta cidade no banco. A lista da tela é "
                      "fechada e sai do banco: ela nunca aceita texto livre."),
        }
        return resposta

    if not escolhidas:
        resposta["recusa_dura"] = {
            "codigo": "nenhuma_atracao_escolhida",
            "frase": ("Escolha ao menos uma atração: a conta do passe é a comparação "
                      "entre o que você pagaria avulso e o que o passe custa, e sem "
                      "nenhuma atração não há o primeiro lado da comparação. "
                      "Zero atrações não querem dizer que o passe não vale — querem "
                      "dizer que ainda não há pergunta."),
        }
        return resposta

    if len(escolhidas) != len(set(escolhidas)):
        # A FRASE NAO ECOA O ID DA ATRACAO, e isto e conserto de 22/10/2026: a primeira
        # versao desta recusa listava os ids repetidos na tela, e id de registro e texto
        # de BASTIDOR DA FABRICA pela 32.4 do ARQUIPELAGO.md — a mesma cicatriz que a F1
        # pagou publicando `unidade_de_preco` e a ohmetria publicando um caminho de
        # arquivo. O portao desta ferramenta nao lia as recusas duras com a regua de
        # frase, e e por isso que ninguem viu; agora le.
        quantas = len(escolhidas) - len(set(escolhidas))
        resposta["recusa_dura"] = {
            "codigo": "atracao_repetida",
            "frase": ("A mesma atração aparece mais de uma vez na sua escolha (%s %s). A "
                      "conta somaria o ingresso dela duas vezes e o passe pareceria valer "
                      "mais a pena do que vale. A lista da tela marca cada atração uma vez."
                      % (quantas, "repetição" if quantas == 1 else "repetições")),
        }
        return resposta

    if len(escolhidas) > ATRACOES_MAXIMO:
        resposta["recusa_dura"] = {
            "codigo": "atracoes_demais",
            "frase": ("A JornadaFly compara até %d atrações de uma vez. Acima disso a "
                      "conta continua certa e a tela deixa de ser legível, e o número de "
                      "combinações que esta ilha precisa ter conferido dobra a cada "
                      "atração a mais." % ATRACOES_MAXIMO),
        }
        return resposta

    conhecidas = {exp.get("id"): exp for exp in atracoes_da_cidade(banco, cidade_id)}
    for atracao_id in escolhidas:
        if atracao_id in conhecidas:
            continue
        existe = por_id.get(atracao_id)
        if existe is not None and existe.get("categoria") == f2.CATEGORIA_DE_PASSE:
            resposta["recusa_dura"] = {
                "codigo": "atracao_que_e_passe",
                "frase": ("«%s» é um passe de cidade e não uma atração: ele é o outro "
                          "lado desta conta, não um item dela. A tela oferece os passes "
                          "da cidade na comparação, nunca na lista de atrações."
                          % existe.get("nome")),
            }
        else:
            # Nem aqui o id entra na frase: ele e nome de registro, e a unica forma de um
            # id desconhecido chegar e a tela ter sido contornada — dizer qual nao ajuda
            # quem le e vaza o vocabulario de dentro da fabrica.
            resposta["recusa_dura"] = {
                "codigo": "atracao_desconhecida",
                "frase": ("Uma das atrações escolhidas não está entre as que a JornadaFly "
                          "leu em %s. A lista da tela é fechada e sai do banco: ela nunca "
                          "aceita texto livre." % cidade.get("nome")),
            }
        return resposta

    moeda = cidade.get("moeda_local")

    # ---- A SOMA DOS AVULSOS: o primeiro lado da comparacao, e ele e NOSSO.
    itens = [_item_para_a_faixa(conhecidas[a]) for a in escolhidas]
    soma = f2.faixa_de_experiencias(itens, pessoas)
    por_atracao = {}
    for atracao_id in escolhidas:
        por_atracao[atracao_id] = faixa_do_avulso(conhecidas[atracao_id], pessoas)

    sem_preco = [conhecidas[a].get("nome") for a in escolhidas if por_atracao[a] is None]
    pendentes = [conhecidas[a].get("nome") for a in escolhidas
                 if conhecidas[a].get("status") != "publicavel"]

    if soma is None:
        recusa("nenhuma_atracao_com_preco_lido",
               "Esta ilha ainda não leu o preço de nenhuma das atrações que você "
               "escolheu em %s, então não há soma de avulsos para comparar com o passe. "
               "Ela não aparece como zero: zero seria dizer que entrar nelas é de graça."
               % cidade.get("nome"))
    else:
        detalhes = []
        for atracao_id in escolhidas:
            faixa = por_atracao[atracao_id]
            nome = conhecidas[atracao_id].get("nome")
            if faixa is None:
                detalhes.append("%s: esta ilha conhece a atração e ainda não leu o preço "
                                "dela, então ela não entra na conta." % nome)
                continue
            d = faixa["detalhe"]
            if d["ponta_unica"] and d["quantas_versoes"] == 1:
                escrito = "%s, «%s», a única versão que esta ilha leu." % (
                    f1.dinheiro(faixa["piso"], moeda), d["rotulo_do_piso"])
            elif d["ponta_unica"]:
                escrito = "%s, e as %d versões custam o mesmo para este grupo." % (
                    f1.dinheiro(faixa["piso"], moeda), d["quantas_versoes"])
            else:
                escrito = "de %s («%s») a %s («%s»)." % (
                    f1.dinheiro(faixa["piso"], moeda), d["rotulo_do_piso"],
                    f1.dinheiro(faixa["teto"], moeda), d["rotulo_do_teto"])
            detalhes.append("%s: %s" % (nome, escrito))
        resposta["avulsos"] = {
            "minimo": soma["piso"],
            "maximo": soma["teto"],
            "moeda": moeda,
            "escrito": (f1.dinheiro(soma["piso"], moeda) if soma["piso"] == soma["teto"]
                        else "%s a %s" % (f1.dinheiro(soma["piso"], moeda),
                                          f1.dinheiro(soma["teto"], moeda))),
            "quantas": soma["quantas"],
            "multiplicador": "%s, uma vez cada atração" % f1.pessoas_em_palavra(pessoas),
            "detalhe": detalhes,
            "procedencia": "nossa",
            "frase_de_procedencia":
                "Todo preço desta página foi lido no site de quem opera ou de quem fixa a "
                "tarifa, com a data da leitura ao lado. Nenhum número aqui é faixa de "
                "terceiro.",
        }
        if sem_preco:
            recusa("atracao_sem_preco_lido",
                   "%s %s no banco sem preço lido, e %s fora da soma em vez de entrar "
                   "como zero: %s."
                   % (atracoes_em_palavra(len(sem_preco)),
                      "está" if len(sem_preco) == 1 else "estão",
                      "ficou" if len(sem_preco) == 1 else "ficaram",
                      ", ".join(sem_preco)))
        if pendentes:
            recusa("preco_lido_e_nao_reconferido",
                   "%s: o preço veio de uma leitura que esta ilha ainda não conferiu na "
                   "fonte de quem o fixa, e por isso ela não o chama de confirmado. Ele "
                   "está na conta com a data em que foi lido, para você decidir sabendo "
                   "disso." % ", ".join(pendentes))

    # ---- O OUTRO LADO: os passes.
    lista_de_passes = passes_da_cidade(banco, cidade_id)
    if not lista_de_passes:
        recusa("sem_passe_lido",
               "Esta ilha ainda não leu nenhum passe de %s. Isso não quer dizer que %s "
               "não tenha passe: quer dizer que esta ilha não leu o preço de nenhum na "
               "fonte de quem o vende, e ela não publica passe que não leu. A conta "
               "acima é a dos ingressos avulsos, e ela já responde à metade da sua "
               "pergunta." % (cidade.get("nome"), cidade.get("nome")))
    else:
        coberturas = banco.get("coberturas_de_passe") or []
        for passe in lista_de_passes:
            resposta["passes"].append(
                _bloco_do_passe(passe, escolhidas, conhecidas, por_atracao, coberturas,
                                pessoas, dias, moeda, esquema, fontes, cidade, recusa,
                                hoje))

    # ---- A FRASE DE RESPOSTA, e ela e a primeira coisa da tela.
    resposta["frase_resposta"] = _frase_de_resposta(resposta, cidade, dias, pessoas, moeda)

    # ---- O CAMBIO, a mesma recusa da F1 e da F2, e pelo mesmo motivo.
    if f1.constantes_pendentes(constantes):
        recusa("sem_valor_em_real",
               "Os valores desta página estão em %s, que é a moeda cobrada em %s. Esta "
               "ilha ainda não tem uma cotação datada para converter, e preço convertido "
               "sem dizer a data do câmbio envelhece sem avisar."
               % (moeda, cidade.get("nome")))

    # ---- COMO SABEMOS: tudo aqui e nosso, e sao TRES leituras diferentes.
    resposta["como_sabemos"] = _como_sabemos(resposta, banco, escolhidas, conhecidas,
                                             fontes, cidade, moeda)
    return resposta


def _bloco_do_passe(passe, escolhidas, conhecidas, por_atracao, coberturas, pessoas,
                    dias, moeda, esquema, fontes, cidade, recusa, hoje):
    """Um passe, suas versoes, o valor entregue e o veredito de cada uma."""
    passe_id = passe.get("id")
    nome_do_passe = passe.get("nome")

    # --- A COBERTURA, atracao por atracao. NAO LIDA NAO E NAO COBERTA.
    lidas = []
    nao_lidas = []
    for atracao_id in escolhidas:
        cob = cobertura_do_par(coberturas, passe_id, atracao_id)
        if cob is None:
            nao_lidas.append(atracao_id)
            continue
        lidas.append((atracao_id, cob))

    if nao_lidas:
        recusa("cobertura_nao_lida",
               "«%s»: esta ilha não leu se ele cobre %s (%s), então %s fora do valor "
               "que o passe entrega. Não é o mesmo que dizer que o passe não cobre — "
               "ninguém leu, e dizer qualquer uma das duas coisas seria afirmar sobre o "
               "que não foi medido."
               % (nome_do_passe, atracoes_em_palavra(len(nao_lidas)),
                  ", ".join(conhecidas[a].get("nome") for a in nao_lidas),
                  "ela ficou" if len(nao_lidas) == 1 else "elas ficaram"))

    declaradas = passe.get("atracoes_declaradas_pelo_passe")
    todas_as_lidas = sum(1 for c in coberturas
                         if c.get("passe") == passe_id
                         and c.get("status") != "excluido_do_banco")
    # ZERO COBERTURAS LIDAS TEM RECUSA PROPRIA, e separa-la foi conserto de leitura em
    # 22/10/2026: com zero, a frase da base do equilibrio saia «toda conta abaixo e
    # sobre essas 0», que e uma frase sobre uma conta que nao existe. Sao dois estados
    # diferentes — «leu parte» e «nao leu nada» —, e o segundo nao tem conta a
    # qualificar: ele tem a ausencia do veredito a explicar.
    if todas_as_lidas == 0:
        recusa("passe_sem_cobertura_lida",
               "«%s»: esta ilha leu o preço dele e ainda não leu a cobertura de nenhuma "
               "atração, então ela publica quanto ele custa e não publica veredito. "
               "Supor o que ele cobre seria inventar o produto do passe%s."
               % (nome_do_passe,
                  ", que declara cobrir %s" % atracoes_em_palavra(declaradas)
                  if isinstance(declaradas, int) else ""))
    elif isinstance(declaradas, int) and declaradas > todas_as_lidas:
        recusa("equilibrio_sobre_o_que_a_ilha_leu",
               "«%s» declara cobrir %s e esta ilha leu a cobertura de %s. Toda conta "
               "abaixo é sobre %s, e não sobre o passe inteiro: um ponto de equilíbrio "
               "calculado sobre parte da cobertura e apresentado como o do passe é "
               "exatamente o número que os artigos deste assunto publicam sem dizer de "
               "quantas atrações ele sai."
               % (nome_do_passe, atracoes_em_palavra(declaradas),
                  atracoes_em_palavra(todas_as_lidas), essas_atracoes(todas_as_lidas)))

    # --- O VALOR ENTREGUE em cada atracao coberta E lida.
    entregas = []
    for atracao_id, cob in lidas:
        faixa = por_atracao.get(atracao_id)
        nome = conhecidas[atracao_id].get("nome")
        if faixa is None:
            recusa("cobertura_de_atracao_sem_preco",
                   "«%s» cobre %s e esta ilha não leu o preço avulso dela, então a "
                   "cobertura não vira valor: sem o avulso não há o que o passe esteja "
                   "pagando no seu lugar." % (nome_do_passe, nome))
            continue
        versao_coberta = cob.get("versao_coberta")
        if versao_coberta is not None:
            versao = versao_de(conhecidas[atracao_id], versao_coberta)
            if versao is None:
                raise BancoIncompleto(
                    "cobertura %r aponta para a versao %r, que nao existe em %r. O "
                    "validador reprova isso; a F3 morre em vez de escolher outra."
                    % (cob.get("id"), versao_coberta, atracao_id))
            exato = _total_da_versao(versao, pessoas)
            piso_do_avulso, teto_do_avulso = exato, exato
            qual = "«%s», a versão que o passe nomeia" % versao.get("rotulo")
        else:
            piso_do_avulso, teto_do_avulso = faixa["piso"], faixa["teto"]
            qual = ("a fonte do passe não diz qual bilhete ela cobre, então o valor vai "
                    "de «%s» a «%s»" % (faixa["detalhe"]["rotulo_do_piso"],
                                        faixa["detalhe"]["rotulo_do_teto"]))
            recusa("cobertura_sem_versao_declarada",
                   "«%s» cobre %s e a fonte não diz QUAL bilhete: %s. O valor entregue "
                   "nessa atração entra como faixa, e esta ilha não escolhe o bilhete "
                   "no seu lugar."
                   % (nome_do_passe, nome,
                      (cob.get("motivo_sem_versao_coberta")
                       or "o motivo não foi registrado").rstrip(". ")))
        piso, teto = valor_entregue(piso_do_avulso, teto_do_avulso, cob.get("como"),
                                    cob.get("desconto_percentual"),
                                    cob.get("desconto_e_no_maximo"))
        if cob.get("como") == "desconto_declarado" and cob.get("desconto_e_no_maximo"):
            recusa("desconto_e_um_teto",
                   "«%s» dá «até %s%%» em %s, e «até» não é um valor: o passe pode abater "
                   "de nada a %s nessa atração. As duas pontas estão na conta, e tratar o "
                   "teto como se fosse o desconto faria o passe parecer pagar antes do "
                   "que paga."
                   % (nome_do_passe, _percentual(cob.get("desconto_percentual")), nome,
                      f1.dinheiro(teto, moeda)))
        if cob.get("como") == "sem_efeito_no_preco":
            recusa("beneficio_que_nao_e_dinheiro",
                   "«%s» dá um benefício em %s que não abate nada do preço (fila, "
                   "transporte ou desconto em outra coisa). Ele entra na conta valendo "
                   "ZERO, porque contar benefício de fila como dinheiro é o jeito mais "
                   "fácil de fazer um passe parecer que paga."
                   % (nome_do_passe, nome))
        if cob.get("reserva_obrigatoria"):
            recusa("reserva_obrigatoria",
                   "«%s» cobre %s mas a reserva é obrigatória: %s. Isso não muda o preço "
                   "e muda se a cobertura é usável no seu dia — e é a regra que envelhece "
                   "primeiro neste assunto. Lida em %s."
                   % (nome_do_passe, nome, cob.get("reserva_transcrita_de"),
                      f1.data_em_portugues(cob.get("data_leitura"))))
        entregas.append({
            "atracao": atracao_id,
            "nome": nome,
            "como": cob.get("como"),
            "rotulo_da_cobertura": ROTULO_DA_COBERTURA[cob.get("como")],
            "o_que_entrega": O_QUE_A_COBERTURA_ENTREGA[cob.get("como")],
            "qual_bilhete": qual,
            "minimo": piso,
            "maximo": teto,
            "moeda": moeda,
            "escrito": (f1.dinheiro(piso, moeda) if piso == teto
                        else "%s a %s" % (f1.dinheiro(piso, moeda),
                                          f1.dinheiro(teto, moeda))),
            "reserva_obrigatoria": bool(cob.get("reserva_obrigatoria")),
            "data_leitura": cob.get("data_leitura"),
            "declarada_por": cob.get("declarada_por"),
        })

    if lidas and not entregas:
        recusa("cobertura_lida_sem_valor_calculavel",
               "«%s» tem cobertura lida e nenhuma delas vira valor nesta escolha, então "
               "não há comparação a publicar." % nome_do_passe)

    # --- AS VERSOES DO PASSE: preco, validade, veredito e equilibrio.
    versoes = []
    for versao in (passe.get("versoes") or []):
        if versao.get("preco") is None:
            recusa("versao_do_passe_sem_preco",
                   "«%s», na versão «%s»: esta ilha conhece a versão e não leu o preço "
                   "dela, então ela não entra na comparação."
                   % (nome_do_passe, versao.get("rotulo")))
            continue
        preco_do_grupo = _total_da_versao(versao, pessoas)
        validade = versao.get("dias_de_uso")

        if validade is None:
            recusa("passe_sem_validade_declarada",
                   "«%s», na versão «%s»: esta ilha não leu por quantos dias ele vale, "
                   "então ela não diz se ele cobre a sua estadia de %s. O preço e a conta "
                   "abaixo continuam valendo; o que falta é a validade."
                   % (nome_do_passe, versao.get("rotulo"), f1.dias_em_palavra(dias)))
        elif validade < dias:
            recusa("passe_cobre_menos_dias_que_a_estadia",
                   "«%s», na versão «%s», vale %s e a sua estadia é de %s: ele cobre "
                   "parte dela. Esta ilha não divide o preço do passe pelos dias, porque "
                   "ele não é cobrado por dia — a conta abaixo é a do passe inteiro."
                   % (nome_do_passe, versao.get("rotulo"),
                      f1.dias_em_palavra(validade), f1.dias_em_palavra(dias)))

        fonte_da_versao = fontes.get(versao.get("fonte")) or {}
        vencido, passados, janela = f1.preco_vencido(
            esquema, fonte_da_versao, versao.get("data_leitura"), hoje)
        if vencido:
            recusa("preco_do_passe_vencido",
                   "«%s», na versão «%s»: o preço foi lido em %s, há %d dias, e esta ilha "
                   "considera %d dias o prazo para reler uma fonte dessas. A regra de "
                   "reserva e o preço de um passe mudam, e a conta abaixo é a do dia da "
                   "leitura — não a de hoje."
                   % (nome_do_passe, versao.get("rotulo"),
                      f1.data_em_portugues(versao.get("data_leitura")), passados, janela))

        piso_entregue = sum((e["minimo"] for e in entregas), Decimal(0))
        teto_entregue = sum((e["maximo"] for e in entregas), Decimal(0))

        if not entregas:
            versoes.append({
                "versao": versao.get("id"),
                "rotulo": versao.get("rotulo"),
                "preco_do_grupo": preco_do_grupo,
                "escrito": f1.dinheiro(preco_do_grupo, moeda),
                "moeda": moeda,
                "validade_em_dias": validade,
                "cobre_a_estadia": None if validade is None else validade >= dias,
                "data_leitura": versao.get("data_leitura"),
                "preco_vencido": vencido,
                "valor_entregue_minimo": None,
                "valor_entregue_maximo": None,
                "veredito": None,
                "frase_do_veredito": (
                    "«%s», na versão «%s», custa %s para %s. Esta ilha não publica "
                    "veredito: nenhuma das atrações que você escolheu tem cobertura lida, "
                    "e sem saber o que o passe cobre não há o que comparar com o preço "
                    "dele." % (nome_do_passe, versao.get("rotulo"),
                               f1.dinheiro(preco_do_grupo, moeda),
                               f1.pessoas_em_palavra(pessoas))),
                "equilibrio": None,
                "frase_do_equilibrio": None,
            })
            continue

        codigo, folga = veredito(piso_entregue, teto_entregue, preco_do_grupo)
        equilibrio = _equilibrio_das_duas_pontas(entregas, preco_do_grupo)
        versoes.append({
            "versao": versao.get("id"),
            "rotulo": versao.get("rotulo"),
            "preco_do_grupo": preco_do_grupo,
            "escrito": f1.dinheiro(preco_do_grupo, moeda),
            "moeda": moeda,
            "validade_em_dias": validade,
            "cobre_a_estadia": None if validade is None else validade >= dias,
            "data_leitura": versao.get("data_leitura"),
            "preco_vencido": vencido,
            "valor_entregue_minimo": piso_entregue,
            "valor_entregue_maximo": teto_entregue,
            "valor_entregue_escrito": (
                f1.dinheiro(piso_entregue, moeda) if piso_entregue == teto_entregue
                else "%s a %s" % (f1.dinheiro(piso_entregue, moeda),
                                  f1.dinheiro(teto_entregue, moeda))),
            "veredito": codigo,
            "frase_do_veredito": _frase_do_veredito(
                codigo, nome_do_passe, versao, preco_do_grupo, piso_entregue,
                teto_entregue, folga, moeda, pessoas, len(entregas)),
            "equilibrio": equilibrio,
            "frase_do_equilibrio": _frase_do_equilibrio(
                equilibrio, entregas, len(entregas), nome_do_passe, versao, moeda),
        })
        if codigo == "depende_da_versao":
            recusa("veredito_depende_da_versao",
                   "«%s», na versão «%s»: o que ele entrega vai de %s a %s e ele custa "
                   "%s. Existe bilhete em que ele paga e bilhete em que não paga, e as "
                   "duas coisas são verdade — esta ilha publica os dois números em vez de "
                   "escolher o bilhete no seu lugar."
                   % (nome_do_passe, versao.get("rotulo"),
                      f1.dinheiro(piso_entregue, moeda), f1.dinheiro(teto_entregue, moeda),
                      f1.dinheiro(preco_do_grupo, moeda)))

    return {
        "passe": passe_id,
        "nome": nome_do_passe,
        "operador": (passe.get("operador") or {}).get("nome"),
        "atracoes_declaradas": declaradas,
        "motivo_sem_atracoes_declaradas": passe.get("motivo_sem_atracoes_declaradas"),
        "coberturas_lidas_no_banco": todas_as_lidas,
        "coberturas_na_sua_escolha": len(lidas),
        "atracoes_sem_cobertura_lida": [conhecidas[a].get("nome") for a in nao_lidas],
        "entregas": entregas,
        "versoes": versoes,
        "bloco_de_compra": f1.bloco_de_compra(esquema, passe, cidade),
    }


def _percentual(valor):
    """«50» / «12,5» — o percentual como a tela o escreve, sem virar dinheiro."""
    d = Decimal(str(valor))
    if d == d.to_integral_value():
        return "{:.0f}".format(d)
    return "{:.2f}".format(d).replace(".", ",")


def _equilibrio_das_duas_pontas(entregas, preco_do_grupo):
    """O equilibrio calculado nas DUAS pontas da faixa do valor entregue.

    Duas contas e nao uma, e a diferenca entre elas e informacao: na ponta de baixo o
    passe precisa de MAIS atracoes para se pagar, na de cima de MENOS. Publicar so
    uma delas seria escolher a versao dos bilhetes no lugar de quem viaja -- a mesma
    recusa que o veredito de tres desfechos carrega.
    """
    piso = ponto_de_equilibrio_em_atracoes([e["minimo"] for e in entregas], preco_do_grupo)
    teto = ponto_de_equilibrio_em_atracoes([e["maximo"] for e in entregas], preco_do_grupo)
    return {
        "na_ponta_de_baixo": piso,
        "na_ponta_de_cima": teto,
        "sobre_quantas": len(entregas),
    }


def _frase_do_veredito(codigo, nome_do_passe, versao, preco, piso, teto, folga, moeda,
                       pessoas, quantas):
    entregue = (f1.dinheiro(piso, moeda) if piso == teto
                else "%s a %s" % (f1.dinheiro(piso, moeda), f1.dinheiro(teto, moeda)))
    if codigo == "paga":
        return ("«%s», na versão «%s», custa %s para %s e paga %s sobre %s: ele vale a "
                "pena na sua escolha, com folga de %s até no bilhete mais barato."
                % (nome_do_passe, versao.get("rotulo"), f1.dinheiro(preco, moeda),
                   f1.pessoas_em_palavra(pessoas), entregue,
                   atracoes_em_palavra(quantas), f1.dinheiro(folga, moeda)))
    if codigo == "nao_paga":
        return ("«%s», na versão «%s», custa %s para %s e paga %s sobre %s: nesta "
                "escolha ele não se paga. Comprar os ingressos avulsos sai mais barato."
                % (nome_do_passe, versao.get("rotulo"), f1.dinheiro(preco, moeda),
                   f1.pessoas_em_palavra(pessoas), entregue,
                   atracoes_em_palavra(quantas)))
    return ("«%s», na versão «%s», custa %s para %s e paga %s sobre %s: depende de qual "
            "bilhete você compraria. Nos mais caros ele se paga; nos mais baratos, não."
            % (nome_do_passe, versao.get("rotulo"), f1.dinheiro(preco, moeda),
               f1.pessoas_em_palavra(pessoas), entregue, atracoes_em_palavra(quantas)))


def _frase_do_equilibrio(equilibrio, entregas, quantas, nome_do_passe, versao, moeda):
    """A frase do ponto de equilibrio, e ela NOMEIA as atracoes que a conta usou."""
    baixo = equilibrio["na_ponta_de_baixo"]
    cima = equilibrio["na_ponta_de_cima"]

    def nomes(resultado, chave):
        return ", ".join(entregas[i]["nome"] for i in resultado["ordem"])

    if baixo is None and cima is None:
        return ("Não há ponto de equilíbrio dentro %s que esta ilha leu para este "
                "passe: nem somando %s o que ele entrega alcança o que ele custa. Com "
                "mais atrações cobertas a conta pode virar, e esta ilha não as leu."
                % (das_atracoes(quantas),
                   "ela" if quantas == 1 else "todas elas"))
    if baixo is None:
        return ("A partir de %s %s, «%s» na versão «%s» passa a se pagar — e só se você "
                "comprar os bilhetes mais caros (%s). Nos mais baratos ele não se paga "
                "nem com %s."
                % (atracoes_em_palavra(cima["quantas"]), de_quantas_atracoes(quantas),
                   nome_do_passe, versao.get("rotulo"), nomes(cima, "maximo"),
                   "ela" if quantas == 1 else "todas"))
    if baixo["quantas"] == cima["quantas"]:
        return ("A partir de %s %s, «%s» na versão «%s» se paga — contando das mais "
                "caras para as mais baratas, que é a ordem em que o passe rende mais: %s."
                % (atracoes_em_palavra(baixo["quantas"]), de_quantas_atracoes(quantas),
                   nome_do_passe, versao.get("rotulo"), nomes(baixo, "minimo")))
    return ("«%s» na versão «%s» se paga a partir de %s se você comprar os bilhetes mais "
            "caros, e a partir de %s se comprar os mais baratos — %s. A diferença entre "
            "os dois números é qual bilhete você escolheria, e esta ilha não escolhe por "
            "você."
            % (nome_do_passe, versao.get("rotulo"),
               atracoes_em_palavra(cima["quantas"]),
               atracoes_em_palavra(baixo["quantas"]), de_quantas_atracoes(quantas)))


def _frase_de_resposta(resposta, cidade, dias, pessoas, moeda):
    """A primeira frase da tela: a resposta antes da explicacao (secao 14.5)."""
    avulsos = resposta["avulsos"]
    passes = resposta["passes"]
    if avulsos is None and not passes:
        return ("Esta ilha ainda não tem nem o preço das atrações nem o de um passe de "
                "%s. A página diz isso em vez de mostrar um número que ninguém conferiu."
                % cidade.get("nome"))
    if not passes:
        # A CONCORDANCIA, e ela e a terceira vez que esta pasta a paga: a primeira
        # versao desta frase publicou «1 atração em Veneza CUSTAM €90», que e o mesmo
        # defeito do «as 1 experiencias» da F2. Nao se ve lendo o codigo; se ve lendo a
        # frase, e e por isso que o portao desta ferramenta le a frase.
        return ("%s em %s %s %s para %s, pelos ingressos avulsos. Esta ilha ainda "
                "não leu nenhum passe desta cidade, então ela não diz se um passe sairia "
                "mais barato — ela diz quanto custa o caminho que ela leu."
                % (atracoes_em_palavra(avulsos["quantas"]).capitalize(),
                   cidade.get("nome"),
                   "custa" if avulsos["quantas"] == 1 else "custam",
                   avulsos["escrito"], f1.pessoas_em_palavra(pessoas)))
    com_veredito = [(p, v) for p in passes for v in p["versoes"] if v["veredito"]]
    if not com_veredito:
        return ("Esta ilha leu %s de %s e não leu a cobertura de nenhuma das atrações "
                "que você escolheu, então ela publica o preço do passe e não publica "
                "veredito: sem saber o que ele cobre, «vale a pena» seria um palpite com "
                "cara de conta."
                % ("um passe" if len(passes) == 1 else "%d passes" % len(passes),
                   cidade.get("nome")))
    paga = [(p, v) for p, v in com_veredito if v["veredito"] == "paga"]
    if paga:
        p, v = min(paga, key=lambda pv: pv[1]["preco_do_grupo"])
        return v["frase_do_veredito"]
    depende = [(p, v) for p, v in com_veredito if v["veredito"] == "depende_da_versao"]
    if depende:
        return depende[0][1]["frase_do_veredito"]
    return com_veredito[0][1]["frase_do_veredito"]


def _como_sabemos(resposta, banco, escolhidas, conhecidas, fontes, cidade, moeda):
    """As TRES leituras desta pagina, e as tres sao nossas.

    A F2 separa o que e nosso do que e de terceiro porque ela tem as duas coisas. Aqui
    nao ha numero de terceiro NENHUM -- preco avulso, preco do passe e cobertura foram
    lidos na fonte de quem opera ou de quem fixa a tarifa. O que a tela separa sao
    TRES LEITURAS que envelhecem em velocidades diferentes, e a do meio e a que
    envelhece primeiro.
    """
    das_atracoes = []
    for atracao_id in escolhidas:
        exp = conhecidas[atracao_id]
        for versao in (exp.get("versoes") or []):
            fonte = fontes.get(versao.get("fonte")) or {}
            chave = (exp.get("nome"), fonte.get("autor"), versao.get("data_leitura"))
            if chave in [(d["atracao"], d["autor"], d["data_leitura"]) for d in das_atracoes]:
                continue
            das_atracoes.append({
                "atracao": exp.get("nome"),
                "autor": fonte.get("autor"),
                "documento": fonte.get("documento"),
                "url": fonte.get("url"),
                "motivo_sem_url": fonte.get("motivo_sem_url"),
                "data_leitura": versao.get("data_leitura"),
                "frase": "%s — %s, em %s." % (
                    exp.get("nome"), fonte.get("autor") or "fonte sem autor registrado",
                    f1.data_em_portugues(versao.get("data_leitura"))),
            })
    dos_passes = []
    das_coberturas = []
    for bloco in resposta["passes"]:
        passe = next((e for e in (banco.get("experiencias") or [])
                      if e.get("id") == bloco["passe"]), {})
        for versao in (passe.get("versoes") or []):
            fonte = fontes.get(versao.get("fonte")) or {}
            dos_passes.append({
                "passe": bloco["nome"],
                "versao": versao.get("rotulo"),
                "autor": fonte.get("autor"),
                "url": fonte.get("url"),
                "data_leitura": versao.get("data_leitura"),
                "frase": "%s, «%s» — %s, em %s." % (
                    bloco["nome"], versao.get("rotulo"),
                    fonte.get("autor") or "fonte sem autor registrado",
                    f1.data_em_portugues(versao.get("data_leitura"))),
            })
        for entrega in bloco["entregas"]:
            das_coberturas.append({
                "passe": bloco["nome"],
                "atracao": entrega["nome"],
                "data_leitura": entrega["data_leitura"],
                "frase": "%s cobre %s (%s) — cobertura lida em %s." % (
                    bloco["nome"], entrega["nome"], entrega["rotulo_da_cobertura"],
                    f1.data_em_portugues(entrega["data_leitura"])),
            })
    return {
        "cidade": cidade.get("nome"),
        "pais": cidade.get("pais"),
        "moeda": moeda,
        "preco_das_atracoes": das_atracoes,
        "preco_dos_passes": dos_passes,
        "cobertura_dos_passes": das_coberturas,
        "frase": ("Nada nesta página é faixa de terceiro: o preço de cada atração, o "
                  "preço de cada passe e a cobertura de cada passe foram lidos na fonte "
                  "de quem opera ou de quem fixa a tarifa, e cada um traz a data da sua "
                  "leitura. São três leituras diferentes, e a cobertura é a que envelhece "
                  "primeiro — é ela que muda quando um passe troca a regra de reserva."),
    }


def _hoje():
    """A data de hoje, isolada numa funcao de uma linha.

    Existe para a bancada poder passar outra sem mexer no relogio do sistema: toda
    conta de vencimento recebe `hoje`, e `responder` e o unico lugar que o le daqui.
    """
    import datetime
    return datetime.date.today()


# ---------------------------------------------------------------------------
# O DOMINIO INTEIRO, E A TABELA PRE-RENDERIZADA
# ---------------------------------------------------------------------------

def subconjuntos(atracoes):
    """Todo subconjunto NAO VAZIO da lista, em ordem estavel (tamanho, depois ordem).

    O dominio desta ferramenta cresce em 2^n - 1, e e por isso que `ATRACOES_MAXIMO`
    existe: ele nao limita o banco, limita a ESCOLHA, e com ele a grade continua
    cabendo numa passada do portao. A ordem e estavel de proposito -- grade que muda
    de ordem entre duas passadas faz o arquivo gravado diferir sem nenhuma regra ter
    mudado.
    """
    saida = []
    total = len(atracoes)
    for mascara in range(1, 1 << total):
        escolha = tuple(atracoes[i] for i in range(total) if mascara & (1 << i))
        saida.append(escolha)
    saida.sort(key=lambda e: (len(e), e))
    return saida


def estados(banco=None, esquema=None):
    """Todo (cidade, atracoes, dias, pessoas) que a F3 serve, mais as bordas.

    As bordas entram de proposito -- 0 e 22 dias, 0 e 13 pessoas, cidade que nao
    existe, escolha vazia, atracao repetida, atracao de outra cidade e o passe
    escolhido como atracao. Grade que nao pisa na borda e amostra com nome de grade, e
    as recusas duras sao justamente onde a conta NAO acontece.
    """
    banco = banco if banco is not None else carregar_banco()
    esquema = esquema if esquema is not None else carregar_esquema()
    saida = []
    dias_de_dentro = list(range(DIAS_MINIMO, DIAS_MAXIMO + 1))
    pessoas_de_dentro = list(range(f1.PESSOAS_MINIMO, f1.PESSOAS_MAXIMO + 1))
    for cidade in (banco.get("cidades") or []):
        cid = cidade.get("id")
        atracoes = [e.get("id") for e in atracoes_da_cidade(banco, cid)]
        if not atracoes:
            # Cidade sem atracao lida nao tem escolha possivel: so a borda da escolha
            # vazia, que e a recusa dura. Inventar uma escolha aqui seria grade falsa.
            saida.append((cid, (), 7, 2))
            continue
        escolhas = subconjuntos(atracoes[:ATRACOES_MAXIMO])
        for escolha in escolhas:
            for dias in dias_de_dentro:
                for pessoas in pessoas_de_dentro:
                    saida.append((cid, escolha, dias, pessoas))
        primeira = escolhas[0]
        for dias in (DIAS_MINIMO - 1, DIAS_MAXIMO + 1):
            saida.append((cid, primeira, dias, 2))
        for pessoas in (f1.PESSOAS_MINIMO - 1, f1.PESSOAS_MAXIMO + 1):
            saida.append((cid, primeira, 7, pessoas))
        saida.append((cid, (), 7, 2))
        saida.append((cid, primeira + primeira, 7, 2))
        saida.append((cid, ("atracao-que-nao-existe",), 7, 2))
        passes = [p.get("id") for p in passes_da_cidade(banco, cid)]
        if passes:
            saida.append((cid, (passes[0],), 7, 2))
        if len(atracoes) > ATRACOES_MAXIMO:
            saida.append((cid, tuple(atracoes[:ATRACOES_MAXIMO + 1]), 7, 2))
    primeira_cidade = (banco.get("cidades") or [{}])[0]
    outras = [c.get("id") for c in (banco.get("cidades") or [])
              if c.get("id") != primeira_cidade.get("id")]
    if outras:
        de_outra = [e.get("id") for e in atracoes_da_cidade(banco, outras[0])]
        if de_outra:
            saida.append((primeira_cidade.get("id"), (de_outra[0],), 7, 2))
    saida.append(("cidade-que-nao-existe", ("qualquer",), 7, 2))
    return saida


def todas_as_respostas(banco=None, esquema=None, constantes=None, hoje=None):
    banco = banco if banco is not None else carregar_banco()
    esquema = esquema if esquema is not None else carregar_esquema()
    constantes = constantes if constantes is not None else carregar_constantes()
    return [responder(c, a, d, p, banco, esquema, constantes, hoje)
            for c, a, d, p in estados(banco, esquema)]


def tabela_pre_renderizada(banco=None, esquema=None, constantes=None, hoje=None):
    """Os casos ja resolvidos, visiveis no HTML e nunca recolhidos.

    E a tabela que a secao 32.1 manda deixar aberta e que as superficies de IA citam.
    A coluna de recusa faz parte da tabela, porque a ausencia do veredito e informacao
    e nao espaco em branco.
    """
    banco = banco if banco is not None else carregar_banco()
    esquema = esquema if esquema is not None else carregar_esquema()
    constantes = constantes if constantes is not None else carregar_constantes()
    linhas = []
    for cidade in (banco.get("cidades") or []):
        atracoes = [e.get("id") for e in atracoes_da_cidade(banco, cidade.get("id"))]
        if not atracoes:
            continue
        for escolha in subconjuntos(atracoes[:ATRACOES_MAXIMO]):
            for dias in DIAS_DA_TABELA:
                for pessoas in PESSOAS_DA_TABELA:
                    r = responder(cidade.get("id"), escolha, dias, pessoas,
                                  banco, esquema, constantes, hoje)
                    if r["recusa_dura"]:
                        continue
                    vereditos = [v["veredito"] for p in r["passes"] for v in p["versoes"]]
                    linhas.append({
                        "cidade": cidade.get("nome"),
                        "atracoes": list(escolha),
                        "quantas_atracoes": len(escolha),
                        "dias": dias,
                        "pessoas": pessoas,
                        "avulsos": r["avulsos"]["escrito"] if r["avulsos"] else None,
                        "passes_lidos": len(r["passes"]),
                        "vereditos": [v for v in vereditos if v],
                        "recusas": [rec["codigo"] for rec in r["recusas"]],
                    })
    return linhas


def imprimir(r):
    saida = []
    e = r["estado"]
    saida.append("ESTADO: %s · %s · %s dias · %s pessoas"
                 % (e["cidade"], ", ".join(e["atracoes"]) or "(nenhuma)",
                    e["dias"], e["pessoas"]))
    if r["recusa_dura"]:
        saida.append("RECUSA DURA (%s): %s" % (r["recusa_dura"]["codigo"],
                                               r["recusa_dura"]["frase"]))
        return "\n".join(saida)
    saida.append("")
    saida.append("RESPOSTA: %s" % r["frase_resposta"])
    saida.append("")
    if r["avulsos"]:
        saida.append("  AVULSOS           %s   (%s)"
                     % (r["avulsos"]["escrito"], r["avulsos"]["multiplicador"]))
        for d in r["avulsos"]["detalhe"]:
            saida.append("      - %s" % d)
    for bloco in r["passes"]:
        saida.append("")
        saida.append("  PASSE: %s" % bloco["nome"])
        saida.append("      declaradas: %s · lidas no banco: %d · na sua escolha: %d"
                     % (bloco["atracoes_declaradas"], bloco["coberturas_lidas_no_banco"],
                        bloco["coberturas_na_sua_escolha"]))
        for entrega in bloco["entregas"]:
            saida.append("      entrega %s em %s (%s)"
                         % (entrega["escrito"], entrega["nome"],
                            entrega["rotulo_da_cobertura"]))
        for versao in bloco["versoes"]:
            saida.append("      [%s] %s" % (versao["veredito"] or "sem veredito",
                                            versao["frase_do_veredito"]))
            if versao["frase_do_equilibrio"]:
                saida.append("           %s" % versao["frase_do_equilibrio"])
    saida.append("")
    saida.append("RECUSAS (%d):" % len(r["recusas"]))
    for rec in r["recusas"]:
        saida.append("  [%s] %s" % (rec["codigo"], rec["frase"]))
    saida.append("")
    saida.append("COMO SABEMOS: %s" % r["como_sabemos"]["frase"])
    for f in r["como_sabemos"]["preco_das_atracoes"]:
        saida.append("  (atração)   %s" % f["frase"])
    for f in r["como_sabemos"]["preco_dos_passes"]:
        saida.append("  (passe)     %s" % f["frase"])
    for f in r["como_sabemos"]["cobertura_dos_passes"]:
        saida.append("  (cobertura) %s" % f["frase"])
    return "\n".join(saida)


def main():
    argumentos = sys.argv[1:]
    if argumentos and argumentos[0] == "--contar":
        banco = carregar_banco()
        esquema = carregar_esquema()
        todos = estados(banco, esquema)
        passes = sum(1 for e in (banco.get("experiencias") or [])
                     if e.get("categoria") == f2.CATEGORIA_DE_PASSE)
        print("cidades no banco:            %d" % len(banco.get("cidades") or []))
        print("passes no banco:             %d" % passes)
        print("coberturas no banco:         %d" % len(banco.get("coberturas_de_passe") or []))
        print("estados que a F3 serve:      %d" % len(todos))
        print("linhas da tabela:            %d"
              % len(tabela_pre_renderizada(banco, esquema)))
        return 0
    if len(argumentos) >= 4:
        cidade, dias, pessoas, lista = argumentos[0], argumentos[1], argumentos[2], argumentos[3]
        r = responder(cidade, tuple(lista.split(",")), int(dias), int(pessoas))
    else:
        banco = carregar_banco()
        primeira = (banco.get("cidades") or [{}])[0].get("id")
        atracoes = [e.get("id") for e in atracoes_da_cidade(banco, primeira)]
        r = responder(primeira, tuple(atracoes[:1]), 3, 2)
    print(imprimir(r))
    return 0


if __name__ == "__main__":
    sys.exit(main())
