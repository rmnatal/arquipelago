#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""F2 -- QUANTO CUSTA N DIAS EM <CIDADE>. Implementacao de REFERENCIA.

Bloco 4 da jornadafly, segunda ferramenta. Dado um estado de entrada (cidade,
dias, pessoas, padrao) este arquivo devolve a resposta inteira -- as quatro
linhas de custo, o que cada uma e, de quem ela veio, o total quando ele existe e
as recusas quando ele nao existe -- ja em frase acentuada, do jeito que o
visitante le.

    python3 ferramentas/f2-referencia.py                        # uma resposta de exemplo
    python3 ferramentas/f2-referencia.py --contar               # o tamanho do dominio
    python3 ferramentas/f2-referencia.py <cidade> <dias> <pessoas> <padrao>

POR QUE PYTHON E NAO PHP: a mesma decisao do bloco 4, e ela nao mudou. Esta ilha
nao tem site, e o dominio dela nao esta na lista de dominios liberados deste
ambiente -- remedido hoje, 22/10/2026, com recusa do tunel em seis medicoes e
aquametria.com.br e robometria.com.br em 200 nas mesmas passadas. O PHP, quando
nascer, e TRADUTOR desta referencia frase a frase.

AS DUAS PROCEDENCIAS, E ELAS SAO A FERRAMENTA INTEIRA
-----------------------------------------------------
A F2 soma QUATRO linhas, e elas nao tem a mesma origem:

  1. EXPERIENCIAS -- NOSSA. Sai da EXPERIENCIA do banco: preco colhido na fonte
     de quem opera, com data de leitura. E o unico diferencial que justifica
     entrar contra quem ja esta em primeiro lugar nesta consulta.
  2. HOSPEDAGEM, 3. ALIMENTACAO, 4. TRANSPORTE LOCAL -- DE TERCEIROS. Saem da
     FAIXA_DIARIA: faixa que alguem publicou, que a F2 republica dizendo quem
     publicou, quando foi lida e O QUE O NUMERO SIGNIFICA na frase de quem a
     escreveu.

A especificacao (3) manda a pagina dizer qual linha e qual, e proibe publicar
hospedagem e alimentacao como se fossem colhidas por nos. Aqui isso nao e uma
instrucao editorial: as duas procedencias moram em entidades diferentes do banco,
e esta referencia nunca as mistura numa linha.

O QUE ESTE ARQUIVO NAO FAZ, de proposito:

  - NAO SOMA FAIXA DE NATUREZA DIFERENTE. Duas faixas da mesma categoria cujo
    `o_que_o_numero_e` difere nao viram um intervalo unico: somar uma media com um
    minimo produz um intervalo que NINGUEM publicou. Medido no bloco 1, em
    14/09/2026: a mesma pagina de resultados trazia «media de R$ 203,87 nos
    ultimos 30 dias» e «a diaria mais baixa encontrada foi R$ 396,84».
  - NAO ESCALA DIARIA DE QUARTO SEM A OCUPACAO. Faixa com base `por_quarto_por_dia`
    e sem `pessoas_por_quarto` nao escala para o grupo, e a linha e recusada pelo
    nome. Seis pessoas numa diaria de quarto duplo sao TRES quartos.
  - NAO INVENTA O TOTAL. O total do grupo so existe quando as quatro linhas
    existem. Com o banco de hoje -- zero faixas diarias -- a F2 publica UMA linha
    de quatro e diz, categoria por categoria, o que falta.
  - NAO ESCOLHE A VERSAO DA EXPERIENCIA. Escolher entre os quatro bilhetes da
    Torre Eiffel seria decisao editorial com cara de conta, entao a linha de
    experiencias e uma FAIXA: o piso e a versao mais barata de cada experiencia,
    o teto e a mais cara, e a tela diz quais sao.
  - NAO FAZ A LINHA DE EXPERIENCIAS CRESCER COM OS DIAS, e isto e declarado em vez
    de suposto: quantas experiencias cabem em N dias nao esta no banco, e a F1
    pagou essa licao na Conta 3 (o eixo das versoes e DECLARADO, nunca lido do
    rotulo). A linha e o custo de fazer UMA VEZ cada experiencia que esta ilha ja
    leu na cidade.
  - NAO TEM SEGUNDA REGRA PARA A CONTA DO GRUPO. A normalizacao de unidade e o
    degrau de capacidade sao importados da F1: quarto e unidade de capacidade como
    a gondola, e duas funcoes para o mesmo fato e como as duas metades deste
    repositorio param de se falar.
  - NAO SOMA O PASSE DE CIDADE NA LINHA DE EXPERIENCIAS. O passe paga as MESMAS
    atracoes, por outro caminho: soma-lo com os ingressos paga a visita duas vezes. A
    F2 o descarta e NOMEIA a recusa, mandando quem pergunta para a F3 — que e a
    ferramenta cuja pergunta e exatamente essa.
  - NAO PUBLICA VALOR EM REAL, pelo mesmo motivo da F1: as duas constantes de
    cambio estao pendentes, e constante pendente e proibida dentro de formula
    publicada.
"""

import importlib.util
import os
import sys
from decimal import Decimal

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(AQUI)
DADOS = os.path.join(BASE, "dados")


def _carregar_f1():
    """A F1 e importada por caminho porque o nome do arquivo tem hifen.

    A F2 depende dela de proposito: a normalizacao de unidade, o degrau de
    capacidade, a escrita do dinheiro e a data em portugues sao as MESMAS regras, e
    duas copias delas e como as duas metades de um repositorio param de se falar.
    """
    caminho = os.path.join(AQUI, "f1-referencia.py")
    spec = importlib.util.spec_from_file_location("f1_referencia", caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


f1 = _carregar_f1()
BancoIncompleto = f1.BancoIncompleto

ESQUEMA = os.path.join(DADOS, "esquema-banco.json")
BANCO = os.path.join(DADOS, "experiencias.json")

# A faixa de dias que a F2 aceita, da especificacao (3). O teto de 21 nao e
# redondo por acaso: acima de tres semanas a estadia deixa de ser viagem e passa a
# ser permanencia, e diaria de hotel nao e o preco de quem fica um mes.
DIAS_MINIMO = 1
DIAS_MAXIMO = 21

# Os dias da TABELA PRE-RENDERIZADA. O 1 e o 21 entram porque sao as bordas de
# dentro, e tabela que nao mostra a borda esconde o degrau que esta ali.
DIAS_DA_TABELA = (1, 3, 7, 21)
PESSOAS_DA_TABELA = (1, 2, 4)

# A CATEGORIA QUE NAO ENTRA NA LINHA DE EXPERIENCIAS, e ela nao e uma delas por
# ausencia: um passe de cidade e um jeito ALTERNATIVO de pagar as atracoes que a cidade
# tem, nao um custo a mais. Somar o passe de Roma com o ingresso do Coliseu paga a mesma
# visita duas vezes. Medido em 22/10/2026, no bloco da F3: com o mundo de bancada do
# passe carregado, a linha de experiencias de Roma publicava «€100 a €148» para 2
# pessoas — o ingresso (€36 a €44) mais o passe (€64 a €104) —, e a tela nomeava os dois
# lado a lado como se fossem dois programas. Qual dos dois sai mais barato e justamente
# a pergunta da F3, e responde-la somando os dois e responder ao contrario.
CATEGORIA_DE_PASSE = "passe_de_cidade"

# As tres categorias que NAO sao nossas, na ordem em que a tela as lista. A ordem e
# de peso no bolso: hospedagem e a maior linha de toda estadia, transporte local a
# menor. A lista e CONFERIDA contra o vocabulario do esquema, nas duas direcoes.
CATEGORIAS_DE_TERCEIRO = ("hospedagem", "alimentacao", "transporte_local")

# Como cada categoria se ESCREVE na tela, acentuada. Nasceu junto com a lista acima
# porque a F1 publicou "por veiculo" sem acento ao montar rotulo com `replace`, e a
# cicatriz nao se paga duas vezes no mesmo repositorio.
ROTULO_DA_CATEGORIA = {
    "hospedagem": "Hospedagem",
    "alimentacao": "Alimentação",
    "transporte_local": "Transporte local",
}

# Como cada padrao se escreve, e o que ele promete. O texto e da especificacao (3):
# sao as tres faixas que as proprias paginas de topo publicam.
ROTULO_DO_PADRAO = {
    "mochileiro": "mochileiro",
    "economico": "econômico",
    "mediano": "mediano",
}

# O que cada natureza de numero E, em portugues, para a tela dizer de que tipo de
# numero se trata em vez de repetir o codigo do campo.
ROTULO_DA_NATUREZA = {
    "media_de_periodo": "média de um período",
    "menor_encontrado": "o menor valor encontrado",
    "faixa_publicada": "uma faixa publicada como faixa",
    "estimativa_do_autor": "estimativa de quem escreveu",
}

# Como cada base se escreve, e e ela que diz se o numero multiplica por pessoa, por
# quarto ou nem por um nem por outro.
ROTULO_DA_BASE = {
    "por_pessoa_por_dia": "por pessoa, por dia",
    "por_quarto_por_dia": "por quarto, por dia",
    "por_grupo_por_dia": "pelo grupo, por dia",
}


# ---------------------------------------------------------------------------
# CARGA, e ela confere as listas desta ferramenta contra o esquema NAS DUAS
# DIRECOES -- valor no esquema sem rotulo aqui publicaria o codigo cru no lugar da
# palavra; rotulo aqui sem valor no esquema e tela para um mundo que o esquema nao
# permite mais.
# ---------------------------------------------------------------------------

def carregar_esquema():
    return f1.carregar_esquema()


def carregar_banco():
    return f1.carregar_banco()


def carregar_constantes():
    return f1.carregar_constantes()


def _conferir(esquema, nome, rotulos, extras=()):
    vocabulario = f1.vocabulario(esquema, nome)
    faltas = []
    for valor in vocabulario:
        if valor not in rotulos:
            faltas.append("`%s` do vocabulario `%s` sem forma de escrita na F2" % (valor, nome))
    for valor in rotulos:
        if valor not in vocabulario and valor not in extras:
            faltas.append("`%s` tem forma de escrita na F2 e nao esta no vocabulario `%s`"
                          % (valor, nome))
    return faltas


def conferir_vocabularios(esquema):
    """As quatro listas desta ferramenta contra as quatro do esquema."""
    faltas = []
    faltas += _conferir(esquema, "categoria_de_custo", ROTULO_DA_CATEGORIA)
    faltas += _conferir(esquema, "padrao_de_viagem", ROTULO_DO_PADRAO)
    faltas += _conferir(esquema, "base_da_faixa", ROTULO_DA_BASE)
    faltas += _conferir(esquema, "o_que_o_numero_e", ROTULO_DA_NATUREZA)

    # A MOEDA, pelas conferencias da F1 — a F2 publica dinheiro e por isso responde
    # pelas duas listas dela tambem. Nao ter chamado isto era lacuna: a bateria de
    # mutacoes tirou EUR do vocabulario do esquema e a F2 continuou imprimindo euro,
    # porque `dinheiro()` olha o proprio dicionario de simbolos e nao o vocabulario.
    faltas += f1.conferir_moedas_do_vocabulario(esquema)
    faltas += f1.conferir_unidades_do_vocabulario(esquema)

    # A CATEGORIA DO PASSE contra o vocabulario `categoria`: se ela sair do esquema, a
    # F2 esta descartando uma categoria que nao existe mais — e nesse dia o passe
    # voltaria calado para dentro da linha de experiencias, somando duas vezes a mesma
    # visita. Regra que exclui por nome responde pelo nome que exclui.
    if CATEGORIA_DE_PASSE not in f1.vocabulario(esquema, "categoria"):
        faltas.append(
            "a F2 descarta a categoria `%s` da linha de experiencias e ela nao esta no "
            "vocabulario `categoria` do esquema. Sem o valor no esquema o descarte nao "
            "descarta nada, e o passe volta a ser somado junto com as atracoes que ele "
            "cobre." % CATEGORIA_DE_PASSE)

    # E a ORDEM da tela contra o vocabulario: categoria nova no esquema que a F2 nao
    # lista some da tela em silencio, que e pior que um erro.
    vocabulario = set(f1.vocabulario(esquema, "categoria_de_custo"))
    if set(CATEGORIAS_DE_TERCEIRO) != vocabulario:
        faltas.append(
            "a ordem de tela da F2 (%s) nao cobre o vocabulario `categoria_de_custo` (%s). "
            "Categoria que a F2 nao lista desaparece da pagina sem ninguem notar."
            % (", ".join(CATEGORIAS_DE_TERCEIRO), ", ".join(sorted(vocabulario))))
    return faltas


def experiencias_em_palavra(n):
    """«1 experiencia» / «3 experiencias», com o artigo e o verbo certos.

    Existe porque a primeira versao desta ferramenta publicou «as 1 experiencias
    que esta ilha leu»: a concordancia e a mesma familia do acento que a F1 pagou
    no dia em que nasceu, e nenhuma das duas se ve lendo o codigo — as duas se veem
    lendo a FRASE, que e por isso que o portao desta ferramenta le a frase.
    """
    return "%d %s" % (n, "experiência" if n == 1 else "experiências")


def padroes(esquema=None):
    esquema = esquema if esquema is not None else carregar_esquema()
    return list(f1.vocabulario(esquema, "padrao_de_viagem"))


# ---------------------------------------------------------------------------
# AS CONTAS, COMO FUNCOES PURAS
#
# Nenhuma delas varre o banco. E a regra da secao 8 do ARQUIPELAGO.md: recusa que
# depende de uma RELACAO entre os dados -- ausencia, empate, naturezas em conflito,
# borda -- mora numa funcao pura que recebe a relacao JA calculada, senao ela so e
# testavel no dia em que o banco produzir o caso, e e esse o dia em que ela vai
# estar errada. O banco de hoje tem ZERO faixas diarias: sem estas funcoes puras, a
# regra de nao somar naturezas diferentes seria uma frase que nada confere.
# ---------------------------------------------------------------------------

def quartos_necessarios(pessoas, pessoas_por_quarto):
    """Quantos quartos o grupo precisa. Funcao pura.

    Delega para a F1 de proposito: quarto e unidade de capacidade como a gondola, e
    a conta e literalmente a mesma (teto de pessoas / capacidade). Escrever a
    segunda aqui seria duas regras para um fato -- e o dia em que uma das duas
    mudasse, a outra ficaria certa sozinha.
    """
    return f1.unidades_necessarias("por_grupo", pessoas_por_quarto, pessoas)


def escalar_faixa(valor, base, pessoas, dias, pessoas_por_quarto=None):
    """O valor publicado, levado ao grupo e ao numero de dias. Funcao pura.

    Devolve (total, multiplicador_em_palavra). Levanta BancoIncompleto quando a
    base e de quarto e a ocupacao nao foi declarada: a F2 trata isso como linha
    recusada, nunca como numero estimado.
    """
    if not isinstance(pessoas, int) or isinstance(pessoas, bool) or pessoas < 1:
        raise BancoIncompleto("pessoas %r nao e inteiro maior ou igual a 1." % (pessoas,))
    if not isinstance(dias, int) or isinstance(dias, bool) or dias < 1:
        raise BancoIncompleto("dias %r nao e inteiro maior ou igual a 1." % (dias,))
    if valor is None:
        raise BancoIncompleto("faixa sem valor: nao ha conta a fazer.")

    v = Decimal(str(valor))
    if base == "por_pessoa_por_dia":
        return v * pessoas * dias, "%s por %s" % (f1.pessoas_em_palavra(pessoas),
                                                  f1.dias_em_palavra(dias))
    if base == "por_grupo_por_dia":
        return v * dias, "pelo grupo, por %s" % f1.dias_em_palavra(dias)
    if base == "por_quarto_por_dia":
        if pessoas_por_quarto is None:
            raise BancoIncompleto(
                "base `por_quarto_por_dia` sem `pessoas_por_quarto`: a diaria de quarto nao "
                "escala para o grupo sem a ocupacao que a propria fonte declarou.")
        quartos = quartos_necessarios(pessoas, pessoas_por_quarto)
        return v * quartos * dias, "%d %s por %s" % (
            quartos, "quarto" if quartos == 1 else "quartos", f1.dias_em_palavra(dias))
    raise BancoIncompleto(
        "base %r sem conta definida. A F2 nao escolhe conta por conta propria: base nova "
        "entra no vocabulario do esquema e na conta desta ferramenta na mesma passada."
        % (base,))


def agrupar_por_natureza(faixas):
    """Agrupa faixas da MESMA categoria pela natureza do numero. Funcao pura.

    `faixas` e uma lista de dicionarios com `o_que_o_numero_e`. Devolve a lista de
    (natureza, [faixas]) em ordem estavel de primeira aparicao -- a ordem em que o
    banco as traz, que e a ordem em que foram lidas.

    E ela que torna a regra COMPUTAVEL: enquanto a distincao entre uma media e um
    minimo morou na prosa de um aviso (de 14/09/2026 a hoje), nada a conferia.
    """
    ordem = []
    por_natureza = {}
    for faixa in faixas:
        natureza = faixa.get("o_que_o_numero_e")
        if natureza not in por_natureza:
            ordem.append(natureza)
            por_natureza[natureza] = []
        por_natureza[natureza].append(faixa)
    return [(natureza, por_natureza[natureza]) for natureza in ordem]


def unir_faixas_da_mesma_natureza(totais):
    """O intervalo de varias faixas da MESMA natureza. Funcao pura.

    `totais` e uma lista de (minimo, maximo) ja escalados. Devolve (minimo dos
    minimos, maximo dos maximos) -- porque faixas da mesma natureza, de
    publicadores diferentes, delimitam juntas o que foi publicado. Lista vazia
    devolve None: intervalo de nada e zero com cara de numero.
    """
    if not totais:
        return None
    return (min(t[0] for t in totais), max(t[1] for t in totais))


def faixa_de_experiencias(itens, pessoas):
    """A linha NOSSA: o custo de fazer uma vez cada experiencia da cidade. Pura.

    `itens` e uma lista de (experiencia_id, nome, [(versao_id, rotulo, preco,
    unidade, capacidade_maxima)], status). Devolve um dicionario com o piso, o teto,
    e QUAL versao esta em cada ponta de cada experiencia -- porque publicar um
    intervalo sem dizer de onde vem cada ponta e publicar um numero sem dono.

    O `status` entra na conta e sai na contagem: `pendente_de_releitura` e preco
    LIDO e nao reconferido, entao ele soma e a tela diz que soma com ressalva.

    Lista vazia devolve None: cidade sem experiencia lida nao tem esta linha, e
    zero seria a mentira mais barata desta ferramenta.
    """
    if not itens:
        return None
    piso = Decimal(0)
    teto = Decimal(0)
    detalhe = []
    pendentes = []
    for exp_id, nome, versoes, status in itens:
        comparaveis = []
        for versao_id, rotulo, preco, unidade, capacidade in versoes:
            if preco is None:
                continue
            total, _por_pessoa, _unidades = f1.total_do_grupo(preco, unidade, capacidade, pessoas)
            comparaveis.append((total, versao_id, rotulo))
        if not comparaveis:
            detalhe.append({
                "experiencia": exp_id, "nome": nome, "sem_preco": True,
                "frase": "%s: esta ilha conhece a experiência e ainda não leu o "
                         "preço dela, então ela não entra na conta." % nome,
            })
            continue
        # EMPATE DE TOTAL, e o desempate das DUAS pontas puxa para o MESMO lado de
        # proposito. O portao achou isto antes do commit: com `min` e `max` sobre
        # (total, id), duas versoes de preco igual davam pontas com ids DIFERENTES, e a
        # tela publicava «de A a B» para um intervalo de largura zero — uma faixa que
        # nao e faixa. Agora as duas pontas escolhem o menor id dentro do seu proprio
        # total, entao preco empatado da ponta unica, e a tela diz que as versoes custam
        # o mesmo em vez de fingir um intervalo.
        menor_total = min(t[0] for t in comparaveis)
        maior_total = max(t[0] for t in comparaveis)
        menor = min((t for t in comparaveis if t[0] == menor_total), key=lambda t: t[1])
        maior = min((t for t in comparaveis if t[0] == maior_total), key=lambda t: t[1])
        piso += menor[0]
        teto += maior[0]
        detalhe.append({
            "experiencia": exp_id,
            "nome": nome,
            "sem_preco": False,
            "versao_do_piso": menor[1],
            "rotulo_do_piso": menor[2],
            "versao_do_teto": maior[1],
            "rotulo_do_teto": maior[2],
            "ponta_unica": menor[1] == maior[1],
            "quantas_versoes": len(comparaveis),
            "status": status,
        })
        if status != "publicavel":
            pendentes.append(nome)
    com_preco = [d for d in detalhe if not d["sem_preco"]]
    if not com_preco:
        return None
    return {"piso": piso, "teto": teto, "detalhe": detalhe,
            "quantas": len(com_preco), "quantas_sem_preco": len(detalhe) - len(com_preco),
            "pendentes": pendentes}


# ---------------------------------------------------------------------------
# A RESPOSTA
# ---------------------------------------------------------------------------

def faixas_da_cidade(banco, cidade_id, categoria, padrao):
    """As faixas publicaveis daquela cidade, categoria e padrao. So leitura."""
    saida = []
    for faixa in (banco.get("faixas_diarias") or []):
        if faixa.get("status") != "publicavel":
            continue
        if faixa.get("cidade") != cidade_id:
            continue
        if faixa.get("categoria_de_custo") != categoria:
            continue
        if faixa.get("padrao") != padrao:
            continue
        saida.append(faixa)
    return saida


def experiencias_da_cidade(banco, cidade_id):
    """As experiencias daquela cidade que entram na conta, e o status de cada uma.

    O PASSE DE CIDADE NAO ENTRA, e esta e a segunda cicatriz desta funcao: ele e um jeito
    alternativo de pagar as atracoes da cidade, nao um custo a mais. Quem o quiser na
    conta esta fazendo a pergunta da F3, e a F2 diz isso numa recusa nomeada em vez de
    somar. Achado em 22/10/2026 pelo mundo de bancada do passe, que o banco nao tem.

    `pendente_de_releitura` ENTRA, com ressalva — e isto e conserto de 22/10/2026,
    achado pelo gerador antes do commit. A primeira versao desta ferramenta
    descartava quem nao fosse `publicavel`, e a consequencia era uma FRASE QUE MENTE:
    Siem Reap tem o preco do passe de Angkor lido e gravado, e a pagina dizia «esta
    ilha ainda nao leu o preco de nenhuma experiencia em Siem Reap». Pior do que a
    frase: o mesmo item aparece na F1 com ressalva e DESAPARECIA aqui, de modo que
    quem viesse da pagina do passe para a da estadia veria a experiencia sumir sem
    explicacao. Quem nao entra e `excluido_do_banco`, e esse e o unico que nao entra.
    """
    itens = []
    for exp in (banco.get("experiencias") or []):
        if exp.get("cidade") != cidade_id:
            continue
        if exp.get("status") == "excluido_do_banco":
            continue
        if exp.get("categoria") == CATEGORIA_DE_PASSE:
            continue
        versoes = []
        for versao in (exp.get("versoes") or []):
            versoes.append((versao.get("id"), versao.get("rotulo"), versao.get("preco"),
                            versao.get("unidade_de_preco"), versao.get("capacidade_maxima")))
        itens.append((exp.get("id"), exp.get("nome"), versoes, exp.get("status")))
    return itens


def passes_da_cidade(banco, cidade_id):
    """Os passes daquela cidade, pelo nome. So leitura.

    Existe para a RECUSA ter nome: dizer «o passe nao entra na conta» sem dizer qual
    passe deixaria o visitante procurando na tela um item que a propria tela esconde.
    """
    return [exp.get("nome") for exp in (banco.get("experiencias") or [])
            if exp.get("cidade") == cidade_id
            and exp.get("categoria") == CATEGORIA_DE_PASSE
            and exp.get("status") != "excluido_do_banco"]


def responder(cidade_id, dias, pessoas, padrao, banco=None, esquema=None, constantes=None):
    banco = banco if banco is not None else carregar_banco()
    esquema = esquema if esquema is not None else carregar_esquema()
    constantes = constantes if constantes is not None else carregar_constantes()

    faltas = conferir_vocabularios(esquema)
    if faltas:
        raise BancoIncompleto(
            "a F2 e o vocabulario do esquema discordam: %s. Vocabulario novo entra no "
            "esquema e na ferramenta na mesma passada." % "; ".join(faltas))

    cidades, fontes, _experiencias = f1.indexar(banco)

    resposta = {
        "estado": {"cidade": cidade_id, "dias": dias, "pessoas": pessoas, "padrao": padrao},
        "recusa_dura": None,
        "frase_resposta": None,
        "linhas": [],
        "total": None,
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
                      "conta deixa de ser de viagem e passa a ser de moradia, e diária "
                      "de hotel não é o preço de quem fica um mês."
                      % (DIAS_MINIMO, DIAS_MAXIMO, DIAS_MAXIMO)),
        }
        return resposta

    if not isinstance(pessoas, int) or isinstance(pessoas, bool) \
            or pessoas < f1.PESSOAS_MINIMO or pessoas > f1.PESSOAS_MAXIMO:
        resposta["recusa_dura"] = {
            "codigo": "grupo_fora_da_faixa",
            "frase": ("A JornadaFly responde para grupos de %d a %d pessoas. Acima de %d a "
                      "compra vira negociação com quem opera, e multiplicar o "
                      "preço de tabela daria um número que ninguém vai cobrar "
                      "de você."
                      % (f1.PESSOAS_MINIMO, f1.PESSOAS_MAXIMO, f1.PESSOAS_MAXIMO)),
        }
        return resposta

    if padrao not in padroes(esquema):
        resposta["recusa_dura"] = {
            "codigo": "padrao_desconhecido",
            "frase": ("A JornadaFly responde nos três padrões que as próprias "
                      "páginas de orçamento publicam: mochileiro, econômico e "
                      "mediano. O seletor nunca aceita texto livre."),
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

    # ---- LINHA 1: EXPERIENCIAS. A nossa.
    itens = experiencias_da_cidade(banco, cidade_id)
    nossa = faixa_de_experiencias(itens, pessoas)
    moeda = cidade.get("moeda_local")

    if nossa is None:
        recusa("sem_experiencia_lida",
               "Esta ilha ainda não leu o preço de nenhuma experiência em %s, "
               "então a linha de experiências não aparece. Ela não aparece "
               "como zero: zero seria dizer que passear em %s é de graça."
               % (cidade.get("nome"), cidade.get("nome")))
    else:
        detalhes_de_tela = []
        for d in nossa["detalhe"]:
            if d["sem_preco"]:
                detalhes_de_tela.append(d["frase"])
            elif d["ponta_unica"] and d["quantas_versoes"] == 1:
                detalhes_de_tela.append(
                    "%s: «%s», a única versão que esta ilha leu." % (d["nome"], d["rotulo_do_piso"]))
            elif d["ponta_unica"]:
                detalhes_de_tela.append(
                    "%s: as %d versões custam o mesmo para este grupo, «%s» entre elas."
                    % (d["nome"], d["quantas_versoes"], d["rotulo_do_piso"]))
            else:
                detalhes_de_tela.append(
                    "%s: de «%s» a «%s»." % (d["nome"], d["rotulo_do_piso"], d["rotulo_do_teto"]))
        resposta["linhas"].append({
            "categoria": "experiencias",
            "rotulo": "Experiências",
            "procedencia": "nossa",
            "frase_de_procedencia":
                "Preço lido no site de quem opera, com a data da leitura ao lado de cada "
                "um. Esta linha é a única da tabela que a JornadaFly colheu.",
            "minimo": nossa["piso"],
            "maximo": nossa["teto"],
            "moeda": moeda,
            "escrito": (f1.dinheiro(nossa["piso"], moeda) if nossa["piso"] == nossa["teto"]
                        else "%s a %s" % (f1.dinheiro(nossa["piso"], moeda),
                                          f1.dinheiro(nossa["teto"], moeda))),
            "multiplicador": "%s, uma vez cada experiência"
                             % f1.pessoas_em_palavra(pessoas),
            "quantas": nossa["quantas"],
            "detalhe": detalhes_de_tela,
        })
        recusa("experiencias_nao_crescem_com_os_dias",
               "A linha de experiências não cresce com os dias: ela é o custo de "
               "fazer UMA VEZ %s que esta ilha leu em %s. Quantas delas caberão nos "
               "seus %s é decisão sua, e esta ilha não tem esse número para inventar."
               % ("a única experiência" if nossa["quantas"] == 1
                  else "cada uma das %s" % experiencias_em_palavra(nossa["quantas"]),
                  cidade.get("nome"), f1.dias_em_palavra(dias)))
        if nossa["pendentes"]:
            recusa("preco_lido_e_nao_reconferido",
                   "%s: o pre\u00e7o veio de uma leitura que esta ilha ainda n\u00e3o "
                   "conferiu na fonte de quem o fixa, e por isso ela n\u00e3o o chama de "
                   "confirmado. Ele est\u00e1 na conta com a data em que foi lido, para "
                   "voc\u00ea decidir sabendo disso."
                   % ", ".join(nossa["pendentes"]))
        if nossa["quantas_sem_preco"]:
            recusa("experiencia_sem_preco_lido",
                   "%s desta cidade %s no banco sem preço lido, e %s fora da conta "
                   "em vez de entrar como zero."
                   % (experiencias_em_palavra(nossa["quantas_sem_preco"]),
                      "está" if nossa["quantas_sem_preco"] == 1 else "estão",
                      "ficou" if nossa["quantas_sem_preco"] == 1 else "ficaram"))

    passes = passes_da_cidade(banco, cidade_id)
    if passes:
        recusa("passe_fora_da_linha_de_experiencias",
               "%s %s de %s e não %s na conta acima: um passe de cidade é um jeito "
               "alternativo de pagar as atrações, não um custo a mais, e somá-lo com os "
               "ingressos pagaria a mesma visita duas vezes. Se a sua dúvida é entre o "
               "passe e os ingressos avulsos, a conta é a da outra ferramenta — "
               "«o passe da cidade vale a pena para você?»."
               % (", ".join("«%s»" % p for p in passes),
                  "é o passe" if len(passes) == 1 else "são os passes",
                  cidade.get("nome"),
                  "entra" if len(passes) == 1 else "entram"))

    # ---- LINHAS 2 A 4: AS DE TERCEIRO.
    faltando = []
    for categoria in CATEGORIAS_DE_TERCEIRO:
        disponiveis = faixas_da_cidade(banco, cidade_id, categoria, padrao)
        if not disponiveis:
            faltando.append(categoria)
            recusa("sem_faixa_%s" % categoria,
                   "%s: esta ilha não tem faixa publicada por ninguém para %s no "
                   "padrão %s, então ela não publica número nenhum aqui. "
                   "Esta ilha republica faixa com o nome de quem a publicou e a data em que "
                   "foi lida, ou não republica."
                   % (ROTULO_DA_CATEGORIA[categoria], cidade.get("nome"),
                      ROTULO_DO_PADRAO[padrao]))
            continue

        grupos = agrupar_por_natureza(disponiveis)
        blocos = []
        for natureza, faixas in grupos:
            totais = []
            recusadas = []
            for faixa in faixas:
                try:
                    menor, _m = escalar_faixa(faixa.get("valor_min"), faixa.get("base"),
                                              pessoas, dias, faixa.get("pessoas_por_quarto"))
                    maior, mult = escalar_faixa(faixa.get("valor_max"), faixa.get("base"),
                                                pessoas, dias, faixa.get("pessoas_por_quarto"))
                except BancoIncompleto:
                    recusadas.append(faixa)
                    continue
                totais.append((menor, maior))
                blocos.append({
                    "natureza": natureza,
                    "publicado_por": faixa.get("publicado_por"),
                    "metodo_declarado": faixa.get("metodo_declarado"),
                    "base": faixa.get("base"),
                    "base_transcrita_de": faixa.get("base_transcrita_de"),
                    "data_leitura": faixa.get("data_leitura"),
                    "url": faixa.get("url"),
                    "minimo": menor,
                    "maximo": maior,
                    "moeda": faixa.get("moeda"),
                    "multiplicador": mult,
                })
            for faixa in recusadas:
                recusa("faixa_de_quarto_sem_ocupacao",
                       "%s publicou uma diária de quarto para %s e não disse quantas "
                       "pessoas o quarto cobre. Sem isso o número não chega ao seu "
                       "grupo: %s em quartos duplos são mais de um quarto, e dividir a "
                       "diária pelo tamanho do grupo seria escolher a ocupação "
                       "no lugar de quem publicou o preço."
                       % (faixa.get("publicado_por"), cidade.get("nome"),
                          f1.pessoas_em_palavra(pessoas)))
            unido = unir_faixas_da_mesma_natureza(totais)
            if unido is not None and len(faixas) > 1:
                recusa("faixas_da_mesma_natureza_unidas_%s" % categoria,
                       "%s: %d publicações dizem a mesma coisa (%s) e por isso elas "
                       "aparecem como um intervalo único, do menor piso ao maior teto."
                       % (ROTULO_DA_CATEGORIA[categoria], len(faixas),
                          ROTULO_DA_NATUREZA[natureza]))

        if len(grupos) > 1:
            recusa("naturezas_em_conflito_%s" % categoria,
                   "%s: as publicações que esta ilha leu não dizem a mesma "
                   "coisa — %s —, e por isso elas aparecem lado a lado em vez de somadas num "
                   "intervalo. Somar uma média com um valor mínimo daria um "
                   "intervalo que ninguém publicou."
                   % (ROTULO_DA_CATEGORIA[categoria],
                      " e ".join(ROTULO_DA_NATUREZA[n] for n, _ in grupos)))

        if blocos:
            resposta["linhas"].append({
                "categoria": categoria,
                "rotulo": ROTULO_DA_CATEGORIA[categoria],
                "procedencia": "de_terceiro",
                "frase_de_procedencia":
                    "Faixa publicada por quem está nomeado em cada linha, com a data em "
                    "que foi lida. A JornadaFly não colheu este número e não o "
                    "apresenta como se tivesse colhido.",
                "blocos": blocos,
                "unico_intervalo": len(grupos) == 1,
            })
        else:
            faltando.append(categoria)

    # ---- O TOTAL. So existe quando as quatro linhas existem.
    publicadas = {l["categoria"] for l in resposta["linhas"]}
    completas = set(("experiencias",) + CATEGORIAS_DE_TERCEIRO)
    if publicadas == completas:
        por_linha_min = []
        por_linha_max = []
        for linha in resposta["linhas"]:
            if linha["categoria"] == "experiencias":
                por_linha_min.append(linha["minimo"])
                por_linha_max.append(linha["maximo"])
            else:
                por_linha_min.append(min(b["minimo"] for b in linha["blocos"]))
                por_linha_max.append(max(b["maximo"] for b in linha["blocos"]))
        total_min = sum(por_linha_min, Decimal(0))
        total_max = sum(por_linha_max, Decimal(0))
        resposta["total"] = {
            "minimo": total_min,
            "maximo": total_max,
            "moeda": moeda,
            "escrito": (f1.dinheiro(total_min, moeda) if total_min == total_max
                        else "%s a %s" % (f1.dinheiro(total_min, moeda),
                                          f1.dinheiro(total_max, moeda))),
            "por_pessoa_por_dia": f1._centavo(total_max / Decimal(pessoas) / Decimal(dias)),
        }
        resposta["frase_resposta"] = (
            "%s em %s, para %s, no padrão %s: %s, somando hospedagem, "
            "alimentação, transporte local e as experiências."
            % (f1.dias_em_palavra(dias).capitalize(), cidade.get("nome"),
               f1.pessoas_em_palavra(pessoas), ROTULO_DO_PADRAO[padrao],
               resposta["total"]["escrito"]))
    else:
        faltam = [ROTULO_DA_CATEGORIA[c] for c in CATEGORIAS_DE_TERCEIRO
                  if c not in publicadas]
        if "experiencias" not in publicadas:
            faltam = ["Experiências"] + faltam
        resposta["total"] = None
        recusa("total_impossivel",
               "Não há total a publicar: %d das 4 linhas da conta não existem "
               "(%s). Um total somado só com as linhas que a ilha tem seria um "
               "número menor que a sua viagem, apresentado como se fosse ela inteira — "
               "e é exatamente o que esta ilha existe para não fazer."
               % (len(faltam), ", ".join(faltam)))
        if "experiencias" in publicadas:
            linha = [l for l in resposta["linhas"] if l["categoria"] == "experiencias"][0]
            resposta["frase_resposta"] = (
                "Em %s, %s %s que esta ilha leu %s %s para %s. O que falta para "
                "fechar a conta de %s está dito abaixo, linha por linha."
                % (cidade.get("nome"), "a" if linha["quantas"] == 1 else "as",
                   experiencias_em_palavra(linha["quantas"]),
                   "custa" if linha["quantas"] == 1 else "custam",
                   linha["escrito"], f1.pessoas_em_palavra(pessoas),
                   f1.dias_em_palavra(dias)))
        else:
            resposta["frase_resposta"] = (
                "Esta ilha ainda não tem nenhuma das quatro linhas da conta de %s em %s. "
                "A página diz isso em vez de mostrar um número que ninguém "
                "conferiu." % (f1.dias_em_palavra(dias), cidade.get("nome")))

    # ---- O CAMBIO, a mesma recusa da F1 e pelo mesmo motivo.
    pendentes = f1.constantes_pendentes(constantes)
    if pendentes:
        recusa("sem_valor_em_real",
               "Os valores desta página estão em %s, que é a moeda cobrada em "
               "%s. Esta ilha ainda não tem uma cotação datada para converter, "
               "e preço convertido sem dizer a data do câmbio envelhece sem avisar."
               % (moeda, cidade.get("nome")))

    # ---- COMO SABEMOS: as duas procedencias, uma do lado da outra, nomeadas.
    nossas_fontes = []
    for exp in (banco.get("experiencias") or []):
        if exp.get("cidade") != cidade_id or exp.get("status") != "publicavel":
            continue
        # O PASSE SAI DAQUI TAMBEM, e esquecer esta metade era a parte mais traicoeira
        # do mesmo defeito: a linha dele nao aparece na tabela e a FONTE dele aparecia na
        # prestacao de contas, de modo que o «como sabemos» prestava contas de um numero
        # que a pagina nao publica. Fonte citada sem numero na tela e o inverso do numero
        # sem fonte, e as duas sao a mesma falta de correspondencia.
        if exp.get("categoria") == CATEGORIA_DE_PASSE:
            continue
        for versao in (exp.get("versoes") or []):
            fonte = fontes.get(versao.get("fonte")) or {}
            chave = (fonte.get("autor"), fonte.get("documento"), versao.get("data_leitura"))
            if chave in [(f["autor"], f["documento"], f["data_leitura"]) for f in nossas_fontes]:
                continue
            nossas_fontes.append({
                "experiencia": exp.get("nome"),
                "autor": fonte.get("autor"),
                "documento": fonte.get("documento"),
                "url": fonte.get("url"),
                "motivo_sem_url": fonte.get("motivo_sem_url"),
                "data_leitura": versao.get("data_leitura"),
                "frase": "%s, em %s." % (fonte.get("autor") or "fonte sem autor registrado",
                                         f1.data_em_portugues(versao.get("data_leitura"))),
            })
    de_terceiros = []
    for linha in resposta["linhas"]:
        for bloco in linha.get("blocos", []):
            de_terceiros.append({
                "categoria": linha["rotulo"],
                "publicado_por": bloco["publicado_por"],
                "url": bloco["url"],
                "data_leitura": bloco["data_leitura"],
                "frase": "%s — %s publicou «%s», lido em %s."
                         % (linha["rotulo"], bloco["publicado_por"],
                            bloco["metodo_declarado"],
                            f1.data_em_portugues(bloco["data_leitura"])),
            })
    resposta["como_sabemos"] = {
        "cidade": cidade.get("nome"),
        "pais": cidade.get("pais"),
        "moeda": moeda,
        "colhido_por_nos": nossas_fontes,
        "publicado_por_terceiros": de_terceiros,
        "frase": ("As experiências desta página têm preço lido no site de "
                  "quem as opera. Hospedagem, alimentação e transporte local, quando "
                  "aparecem, são faixa publicada por terceiros, com o nome de quem "
                  "publicou. As duas coisas nunca entram na mesma linha."),
    }
    return resposta


# ---------------------------------------------------------------------------
# O DOMINIO INTEIRO, E A TABELA PRE-RENDERIZADA
# ---------------------------------------------------------------------------

def estados(banco=None, esquema=None):
    """Todo (cidade, dias, pessoas, padrao) que a F2 serve, mais as bordas.

    As bordas entram de proposito: 0 e 22 dias, 0 e 13 pessoas, e um padrao que nao
    existe sao as recusas duras, e grade que nao pisa na borda e amostra com nome de
    grade.
    """
    banco = banco if banco is not None else carregar_banco()
    esquema = esquema if esquema is not None else carregar_esquema()
    lista_de_padroes = padroes(esquema)
    saida = []
    dias_de_dentro = list(range(DIAS_MINIMO, DIAS_MAXIMO + 1))
    pessoas_de_dentro = list(range(f1.PESSOAS_MINIMO, f1.PESSOAS_MAXIMO + 1))
    for cidade in (banco.get("cidades") or []):
        cid = cidade.get("id")
        for padrao in lista_de_padroes:
            for dias in dias_de_dentro:
                for pessoas in pessoas_de_dentro:
                    saida.append((cid, dias, pessoas, padrao))
            # As bordas, uma vez por cidade e padrao: elas nao dependem das outras
            # entradas, e repeti-las 21 x 12 vezes seria inflar a grade sem medir nada.
            for dias in (DIAS_MINIMO - 1, DIAS_MAXIMO + 1):
                saida.append((cid, dias, 2, padrao))
            for pessoas in (f1.PESSOAS_MINIMO - 1, f1.PESSOAS_MAXIMO + 1):
                saida.append((cid, 7, pessoas, padrao))
        saida.append((cid, 7, 2, "padrao_que_nao_existe"))
    saida.append(("cidade_que_nao_existe", 7, 2, lista_de_padroes[0]))
    return saida


def todas_as_respostas(banco=None, esquema=None, constantes=None):
    banco = banco if banco is not None else carregar_banco()
    esquema = esquema if esquema is not None else carregar_esquema()
    constantes = constantes if constantes is not None else carregar_constantes()
    return [responder(c, d, p, pa, banco, esquema, constantes)
            for c, d, p, pa in estados(banco, esquema)]


def tabela_pre_renderizada(banco=None, esquema=None, constantes=None):
    """Os casos ja resolvidos, visiveis no HTML e nunca recolhidos.

    E a tabela que a secao 32.1 manda deixar aberta e que as superficies de IA
    citam. Cada linha e um estado que a F2 responde, com o que ela PODE publicar
    hoje — e a coluna de recusa faz parte da tabela, porque a ausencia da linha e
    informacao e nao espaco em branco.
    """
    banco = banco if banco is not None else carregar_banco()
    esquema = esquema if esquema is not None else carregar_esquema()
    constantes = constantes if constantes is not None else carregar_constantes()
    linhas = []
    for cidade in (banco.get("cidades") or []):
        for padrao in padroes(esquema):
            for dias in DIAS_DA_TABELA:
                for pessoas in PESSOAS_DA_TABELA:
                    r = responder(cidade.get("id"), dias, pessoas, padrao,
                                  banco, esquema, constantes)
                    if r["recusa_dura"]:
                        continue
                    experiencias = [l for l in r["linhas"] if l["categoria"] == "experiencias"]
                    linhas.append({
                        "cidade": cidade.get("nome"),
                        "dias": dias,
                        "pessoas": pessoas,
                        "padrao": ROTULO_DO_PADRAO[padrao],
                        "experiencias": experiencias[0]["escrito"] if experiencias else None,
                        "total": r["total"]["escrito"] if r["total"] else None,
                        "linhas_publicadas": len(r["linhas"]),
                        "linhas_recusadas": 4 - len(r["linhas"]),
                    })
    return linhas


def imprimir(r):
    saida = []
    e = r["estado"]
    saida.append("ESTADO: %s · %s dias · %s pessoas · padrao %s"
                 % (e["cidade"], e["dias"], e["pessoas"], e["padrao"]))
    if r["recusa_dura"]:
        saida.append("RECUSA DURA (%s): %s" % (r["recusa_dura"]["codigo"],
                                               r["recusa_dura"]["frase"]))
        return "\n".join(saida)
    saida.append("")
    saida.append("RESPOSTA: %s" % r["frase_resposta"])
    saida.append("")
    for linha in r["linhas"]:
        if linha["categoria"] == "experiencias":
            saida.append("  %-18s %s   (%s)" % (linha["rotulo"], linha["escrito"],
                                                linha["multiplicador"]))
            for d in linha["detalhe"]:
                saida.append("      - %s" % d)
        else:
            saida.append("  %-18s" % linha["rotulo"])
            for b in linha["blocos"]:
                # «X a X» e a faixa de largura zero outra vez, um andar abaixo: o
                # publicador que deu UM numero so nao publicou intervalo nenhum, e
                # escrever dois numeros iguais com um «a» no meio e inventar largura.
                # O conserto da linha de experiencias valia aqui tambem.
                if b["minimo"] == b["maximo"]:
                    escrito = f1.dinheiro(b["minimo"], b["moeda"])
                else:
                    escrito = "%s a %s" % (f1.dinheiro(b["minimo"], b["moeda"]),
                                           f1.dinheiro(b["maximo"], b["moeda"]))
                saida.append("      - %s (%s), %s: «%s»"
                             % (escrito, b["multiplicador"], b["publicado_por"],
                                b["metodo_declarado"]))
    if r["total"]:
        saida.append("")
        saida.append("  TOTAL             %s" % r["total"]["escrito"])
    saida.append("")
    saida.append("RECUSAS (%d):" % len(r["recusas"]))
    for rec in r["recusas"]:
        saida.append("  [%s] %s" % (rec["codigo"], rec["frase"]))
    saida.append("")
    saida.append("COMO SABEMOS: %s" % r["como_sabemos"]["frase"])
    for f in r["como_sabemos"]["colhido_por_nos"]:
        saida.append("  (nosso)    %s — %s" % (f["experiencia"], f["frase"]))
    for f in r["como_sabemos"]["publicado_por_terceiros"]:
        saida.append("  (terceiro) %s" % f["frase"])
    return "\n".join(saida)


def main():
    argumentos = sys.argv[1:]
    if argumentos and argumentos[0] == "--contar":
        banco = carregar_banco()
        esquema = carregar_esquema()
        todos = estados(banco, esquema)
        print("cidades no banco:            %d" % len(banco.get("cidades") or []))
        print("faixas diarias no banco:     %d" % len(banco.get("faixas_diarias") or []))
        print("padroes:                     %d" % len(padroes(esquema)))
        print("estados que a F2 serve:      %d" % len(todos))
        print("linhas da tabela:            %d" % len(tabela_pre_renderizada(banco, esquema)))
        return 0
    if len(argumentos) == 4:
        cidade, dias, pessoas, padrao = argumentos
        r = responder(cidade, int(dias), int(pessoas), padrao)
    else:
        banco = carregar_banco()
        primeira = (banco.get("cidades") or [{}])[0].get("id")
        r = responder(primeira, 3, 2, "economico")
    print(imprimir(r))
    return 0


if __name__ == "__main__":
    sys.exit(main())
