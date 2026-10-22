#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PORTAO DA F2 -- varre o dominio inteiro e refaz a aritmetica a mao.

    python3 ferramentas/teste-f2.py

Reprova com codigo de saida 1. Nao abre a rede e nao escreve nada em disco.

O QUE ESTE PORTAO MEDE, e por que ele e assim:

  1. A ARITMETICA, REFEITA EM Fraction. Todo numero que a F2 publica e recalculado
     aqui por um caminho diferente -- Fraction em vez de Decimal, com o
     arredondamento meio-para-cima escrito a mao -- porque regua que chama a mesma
     funcao da ferramenta nao mede a conta, mede a si mesma.
  2. O DOMINIO INTEIRO, NAO UMA AMOSTRA. Os 3.077 estados, as bordas de dentro e as
     de fora. A F1 pagou esta licao com um numero: existe EXATAMENTE UM estado no
     banco dela em que o arredondamento muda o resultado, e uma grade por amostragem
     teria uma chance em 154 de o achar.
  3. AS FUNCOES PURAS COM MUNDOS QUE O BANCO NAO TEM. O banco tem ZERO faixas
     diarias hoje, entao a regra «faixa de natureza diferente nao se soma», a recusa
     da diaria de quarto sem ocupacao e a uniao de faixas da mesma natureza SO sao
     mediveis assim. Sem esta metade, as tres seriam frases que nada confere, e o
     dia em que a primeira faixa for carregada seria o dia de descobrir que estavam
     erradas.
  4. A FRASE, e nao so o numero. Acento, concordancia, frase proibida do VOZ.md e
     texto de bastidor da fabrica (secao 32.4 do ARQUIPELAGO.md). As listas vem do
     portao da F1 por IMPORTACAO, nunca copiadas: lista de palavra proibida que
     existe em duas copias e uma lista que diverge no dia em que alguem acrescenta a
     palavra em uma delas.
  5. QUE A F2 NAO ESCOLHE VERSAO NEM INVENTA TOTAL. Com tres das quatro linhas
     ausentes, `total` tem de ser None e a recusa tem de estar nomeada -- publicar o
     total do que existe seria publicar um numero menor que a viagem com cara de
     viagem inteira.
"""

import importlib.util
import io
import json
import math
import os
import re
import sys
from fractions import Fraction

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(AQUI)
DADOS = os.path.join(BASE, "dados")


def _modulo(nome_do_arquivo, nome):
    caminho = os.path.join(AQUI, nome_do_arquivo)
    spec = importlib.util.spec_from_file_location(nome, caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def _ler(nome):
    with io.open(os.path.join(DADOS, nome), encoding="utf-8") as f:
        return json.load(f)


def _referencia():
    return _modulo("f2-referencia.py", "f2_referencia")


def _portao_da_f1():
    """As listas de frase e de bastidor vem DAQUI, nunca de uma copia local."""
    return _modulo("teste-f1.py", "teste_f1")


# ---------------------------------------------------------------------------
# A ARITMETICA, REFEITA POR OUTRO CAMINHO
# ---------------------------------------------------------------------------

def _centavo_a_mao(valor):
    """Arredonda ao centavo, meio-para-CIMA, escrito a mao em Fraction.

    O `quantize` do Decimal nao aparece aqui de proposito: se a regua usasse a mesma
    ferramenta da ferramenta, ela aprovaria o arredondamento do banqueiro no dia em
    que alguem trocasse o modo -- e esse e o defeito de um centavo que ninguem
    procura.
    """
    v = Fraction(valor) * 100
    piso = v.numerator // v.denominator
    resto = v - piso
    if resto > Fraction(1, 2):
        piso += 1
    elif resto == Fraction(1, 2):
        piso += 1
    return Fraction(piso, 100)


def _total_da_experiencia_a_mao(preco, unidade, capacidade, pessoas):
    """A Conta 1 da F1, refeita: unidade por pessoa multiplica; as outras tomam o
    teto de pessoas / capacidade."""
    p = Fraction(str(preco))
    if unidade == "por_pessoa":
        return p * pessoas
    if capacidade is None or capacidade < 1:
        raise AssertionError("capacidade %r invalida para unidade %r" % (capacidade, unidade))
    return p * int(math.ceil(float(pessoas) / capacidade))


def _escalar_a_mao(valor, base, pessoas, dias, pessoas_por_quarto):
    v = Fraction(str(valor))
    if base == "por_pessoa_por_dia":
        return v * pessoas * dias
    if base == "por_grupo_por_dia":
        return v * dias
    if base == "por_quarto_por_dia":
        quartos = int(math.ceil(float(pessoas) / pessoas_por_quarto))
        return v * quartos * dias
    raise AssertionError("base %r sem conta a mao" % (base,))


def _numero_na_frase(valor, moeda):
    """O numero como a tela o escreve, para procurar na frase."""
    d = _centavo_a_mao(valor)
    inteiro = d.denominator == 1 or (d * 100) % 100 == 0
    if inteiro:
        corpo = "{:,.0f}".format(float(d)).replace(",", ".")
    else:
        corpo = "{:,.2f}".format(float(d))
        corpo = corpo.replace(",", "\x00").replace(".", ",").replace("\x00", ".")
    simbolo = {"EUR": "€", "USD": "US$ ", "BRL_do_operador": "R$ "}[moeda]
    return simbolo + corpo


def _frases_de(resposta):
    """Toda frase que a resposta manda para a tela, achatada.

    Mede o CORPO e nao o JSON inteiro: o JSON carrega codigo de recusa, id de cidade
    e nome de base, que nao sao texto de tela e reprovariam por acento sem nenhum
    defeito embaixo.
    """
    frases = []
    if resposta["recusa_dura"]:
        return [resposta["recusa_dura"]["frase"]]
    frases.append(resposta["frase_resposta"])
    for linha in resposta["linhas"]:
        frases.append(linha["rotulo"])
        frases.append(linha["frase_de_procedencia"])
        for d in linha.get("detalhe", []):
            frases.append(d)
        for b in linha.get("blocos", []):
            frases.append(b["metodo_declarado"])
            frases.append(b["multiplicador"])
        if linha.get("multiplicador"):
            frases.append(linha["multiplicador"])
    for r in resposta["recusas"]:
        frases.append(r["frase"])
    frases.append(resposta["como_sabemos"]["frase"])
    for f in resposta["como_sabemos"]["colhido_por_nos"]:
        frases.append(f["frase"])
    for f in resposta["como_sabemos"]["publicado_por_terceiros"]:
        frases.append(f["frase"])
    return [f for f in frases if f]


# ---------------------------------------------------------------------------
# O PORTAO
# ---------------------------------------------------------------------------

def conferir(f2=None, banco=None, esquema=None, constantes=None, doc_respostas=None):
    """O portao inteiro sobre dicionarios EM MEMORIA. Devolve (falhas, resumo).

    E assim que ferramentas/mutacoes-f2.py produz os mundos que o banco ainda nao
    tem -- faixas diarias, naturezas em conflito, diaria de quarto sem ocupacao --
    e quebra a propria referencia para ver o portao reprovar, sem gravar uma linha
    no banco de verdade.
    """
    f2 = f2 if f2 is not None else _referencia()
    banco = banco if banco is not None else _ler("experiencias.json")
    esquema = esquema if esquema is not None else _ler("esquema-banco.json")
    constantes = constantes if constantes is not None else _ler("constantes.json")
    p1 = _portao_da_f1()

    falhas = []
    afirmacoes = 0

    def afirmar(condicao, mensagem):
        nonlocal afirmacoes
        afirmacoes += 1
        if not condicao:
            falhas.append(mensagem)

    cidades = {c.get("id"): c for c in (banco.get("cidades") or [])}
    vocabulario_de_padroes = (esquema.get("vocabularios") or {}).get("padrao_de_viagem") or []

    # ---- 1. AS LISTAS DA F2 CONTRA O VOCABULARIO DO ESQUEMA
    afirmar(f2.conferir_vocabularios(esquema) == [],
            "a F2 e o vocabulario do esquema discordam: %s"
            % "; ".join(f2.conferir_vocabularios(esquema)))

    # ---- 1b. OS LIMITES DE ENTRADA, CONTRA A ESPECIFICACAO E NAO CONTRA A FERRAMENTA
    #
    # Achado pela bateria de mutacoes em 22/10/2026: a mutacao que trocou o teto de
    # dias de 21 para 60 PASSOU, porque todo o resto deste portao lia o teto da
    # propria referencia — grade, bordas e a conta do que esta «fora» saiam de
    # `f2.DIAS_MAXIMO`, entao os dois concordavam sempre. Regua que toma o limite da
    # coisa que ela mede nao mede o limite. Os numeros abaixo vem da especificacao
    # (dados/especificacao-calculadoras.md, secao 3: «dias (1 a 21), pessoas (1 a
    # 12)») e por isso estao escritos aqui, nao lidos.
    afirmar(f2.DIAS_MINIMO == 1 and f2.DIAS_MAXIMO == 21,
            "a F2 aceita de %d a %d dias e a especificacao diz de 1 a 21. Teto novo e "
            "decisao de produto: ele muda na especificacao primeiro, e aqui depois"
            % (f2.DIAS_MINIMO, f2.DIAS_MAXIMO))
    afirmar(f2.f1.PESSOAS_MINIMO == 1 and f2.f1.PESSOAS_MAXIMO == 12,
            "a F2 aceita de %d a %d pessoas e a especificacao diz de 1 a 12"
            % (f2.f1.PESSOAS_MINIMO, f2.f1.PESSOAS_MAXIMO))
    afirmar(f2.DIAS_MAXIMO in f2.DIAS_DA_TABELA and f2.DIAS_MINIMO in f2.DIAS_DA_TABELA,
            "a tabela pre-renderizada nao mostra as bordas de dentro (%r): tabela que "
            "para antes da borda esconde o degrau que esta ali"
            % (f2.DIAS_DA_TABELA,))

    # ---- 2. AS FUNCOES PURAS, COM MUNDOS QUE O BANCO NAO TEM
    #
    # Esta e a metade do portao que o banco de hoje nao alcanca: zero faixas
    # diarias. Sem ela, tres regras da F2 seriam prosa.

    # 2a. quartos: o degrau, a borda exata e o um-a-um
    for pessoas, ppq, esperado in ((1, 2, 1), (2, 2, 1), (3, 2, 2), (4, 2, 2), (5, 2, 3),
                                   (1, 1, 1), (12, 1, 12), (12, 4, 3), (13, 4, 4),
                                   (6, 2, 3), (7, 3, 3), (8, 3, 3), (9, 3, 3), (10, 3, 4)):
        afirmar(f2.quartos_necessarios(pessoas, ppq) == esperado,
                "quartos_necessarios(%d, %d) deu %r e tem de dar %d — e o degrau de "
                "capacidade, o mesmo da gondola"
                % (pessoas, ppq, f2.quartos_necessarios(pessoas, ppq), esperado))

    # 2b. escalar_faixa nas tres bases, com a conta refeita a mao
    for base, ppq in (("por_pessoa_por_dia", None), ("por_grupo_por_dia", None),
                      ("por_quarto_por_dia", 2), ("por_quarto_por_dia", 1),
                      ("por_quarto_por_dia", 4)):
        for valor in (10, 37.5, 203.87, 396.84, 1):
            for pessoas in (1, 2, 3, 5, 12):
                for dias in (1, 2, 7, 21):
                    total, _mult = f2.escalar_faixa(valor, base, pessoas, dias, ppq)
                    mao = _escalar_a_mao(valor, base, pessoas, dias, ppq)
                    afirmar(Fraction(str(total)) == mao,
                            "escalar_faixa(%r, %s, %d, %d, %r) deu %s e a conta a mao da %s"
                            % (valor, base, pessoas, dias, ppq, total, mao))

    # 2c. a diaria de quarto SEM ocupacao nao escala: ela levanta, nunca estima
    try:
        f2.escalar_faixa(100, "por_quarto_por_dia", 4, 3, None)
        afirmar(False, "escalar_faixa aceitou base de quarto SEM `pessoas_por_quarto` e "
                       "devolveu numero. Sem a ocupacao a diaria nao chega ao grupo, e "
                       "estimar aqui seria escolher a ocupacao no lugar de quem publicou.")
    except f2.BancoIncompleto:
        afirmar(True, "")

    # 2d. base que o vocabulario nao conhece MATA, nunca escolhe conta
    try:
        f2.escalar_faixa(100, "por_semana_por_pessoa", 2, 3, None)
        afirmar(False, "escalar_faixa aceitou uma base que nao esta no vocabulario e "
                       "escolheu uma conta por conta propria.")
    except f2.BancoIncompleto:
        afirmar(True, "")

    # 2e. as bordas de pessoas e dias nas funcoes puras
    for pessoas, dias in ((0, 3), (-1, 3), (2, 0), (2, -1), (True, 3), (2, True)):
        try:
            f2.escalar_faixa(100, "por_pessoa_por_dia", pessoas, dias, None)
            afirmar(False, "escalar_faixa aceitou pessoas=%r dias=%r" % (pessoas, dias))
        except f2.BancoIncompleto:
            afirmar(True, "")

    # 2f. agrupar_por_natureza: vazio, uma, duas iguais, duas diferentes, ordem estavel
    afirmar(f2.agrupar_por_natureza([]) == [],
            "agrupar_por_natureza([]) tem de dar lista vazia")
    media = {"o_que_o_numero_e": "media_de_periodo"}
    minimo = {"o_que_o_numero_e": "menor_encontrado"}
    grupos = f2.agrupar_por_natureza([media, minimo, media])
    afirmar([n for n, _ in grupos] == ["media_de_periodo", "menor_encontrado"],
            "agrupar_por_natureza nao preservou a ordem de primeira aparicao: %r"
            % ([n for n, _ in grupos],))
    afirmar(len(grupos[0][1]) == 2 and len(grupos[1][1]) == 1,
            "agrupar_por_natureza nao juntou as duas da mesma natureza")
    afirmar(len(f2.agrupar_por_natureza([media, media])) == 1,
            "duas faixas da MESMA natureza tem de dar UM grupo")
    afirmar(len(f2.agrupar_por_natureza([media, minimo])) == 2,
            "uma media e um minimo tem de dar DOIS grupos: somar os dois daria um "
            "intervalo que ninguem publicou")

    # 2g. unir_faixas_da_mesma_natureza: vazio devolve None, nunca zero
    afirmar(f2.unir_faixas_da_mesma_natureza([]) is None,
            "unir_faixas_da_mesma_natureza([]) tem de dar None — intervalo de nada e "
            "zero com cara de numero")
    unido = f2.unir_faixas_da_mesma_natureza([(10, 20), (5, 15), (12, 40)])
    afirmar(unido == (5, 40),
            "unir_faixas_da_mesma_natureza deu %r e tem de dar (5, 40): do menor piso "
            "ao maior teto" % (unido,))
    afirmar(f2.unir_faixas_da_mesma_natureza([(7, 7)]) == (7, 7),
            "uma faixa so tem de devolver a propria faixa")

    # 2h. faixa_de_experiencias: vazia devolve None; empate; uma versao so; sem preco
    afirmar(f2.faixa_de_experiencias([], 2) is None,
            "faixa_de_experiencias([]) tem de dar None — zero seria dizer que passear "
            "e de graca")
    uma = f2.faixa_de_experiencias(
        [("x", "X", [("v", "V", 50, "por_pessoa", None)], "publicavel")], 3)
    afirmar(uma["piso"] == uma["teto"] == 150 and uma["detalhe"][0]["ponta_unica"],
            "uma versao so tem de dar piso igual ao teto e ponta unica: %r" % (uma,))
    empate = f2.faixa_de_experiencias(
        [("x", "X", [("a", "A", 50, "por_pessoa", None),
                     ("b", "B", 50, "por_pessoa", None)], "publicavel")], 1)
    afirmar(empate["piso"] == empate["teto"] == 50,
            "empate de preco tem de dar piso igual ao teto")
    afirmar(empate["detalhe"][0]["versao_do_piso"] == "a"
            and empate["detalhe"][0]["versao_do_teto"] == "a",
            "no empate a ponta tem de ser ESTAVEL (o menor id), para a tela nao trocar "
            "de versao a cada carga: %r" % (empate["detalhe"][0],))
    sem_preco = f2.faixa_de_experiencias(
        [("x", "X", [("v", "V", None, "por_pessoa", None)], "publicavel")], 2)
    afirmar(sem_preco is None,
            "experiencia unica SEM preco lido tem de dar None, nunca zero")
    mista = f2.faixa_de_experiencias(
        [("x", "X", [("v", "V", None, "por_pessoa", None)], "publicavel"),
         ("y", "Y", [("w", "W", 20, "por_pessoa", None)], "publicavel")], 2)
    afirmar(mista["quantas"] == 1 and mista["quantas_sem_preco"] == 1 and mista["piso"] == 40,
            "experiencia sem preco tem de ficar FORA da conta e CONTADA: %r" % (mista,))
    capacidade = f2.faixa_de_experiencias(
        [("g", "G", [("d", "D", 90, "por_veiculo", 5)], "publicavel")], 6)
    afirmar(capacidade["piso"] == 180,
            "6 pessoas numa unidade de capacidade 5 sao DUAS unidades: deu %r"
            % (capacidade["piso"],))
    afirmar(uma["pendentes"] == [],
            "experiencia `publicavel` nao pode entrar na lista de pendentes")
    pendente = f2.faixa_de_experiencias(
        [("x", "X", [("v", "V", 50, "por_pessoa", None)], "pendente_de_releitura")], 2)
    afirmar(pendente is not None and pendente["piso"] == 100,
            "preco lido e nao reconferido tem de ENTRAR na conta: o mesmo item aparece "
            "na F1 com ressalva, e some-lo aqui faria a experiencia desaparecer entre "
            "uma pagina e a outra")
    afirmar(pendente["pendentes"] == ["X"],
            "a experiencia pendente tem de ser NOMEADA para a tela dizer a ressalva: %r"
            % (pendente["pendentes"],))

    # ---- 3. O DOMINIO INTEIRO
    todos = f2.estados(banco, esquema)
    afirmar(len(todos) == len(set(todos)),
            "a grade tem estado repetido: %d estados e %d distintos"
            % (len(todos), len(set(todos))))

    duras = 0
    com_total = 0
    com_linha_nossa = 0
    for cidade_id, dias, pessoas, padrao in todos:
        r = f2.responder(cidade_id, dias, pessoas, padrao, banco, esquema, constantes)
        onde = "%s/%s dias/%s pessoas/%s" % (cidade_id, dias, pessoas, padrao)

        fora = (not isinstance(dias, int) or dias < f2.DIAS_MINIMO or dias > f2.DIAS_MAXIMO
                or not isinstance(pessoas, int) or pessoas < f2.f1.PESSOAS_MINIMO
                or pessoas > f2.f1.PESSOAS_MAXIMO
                or padrao not in vocabulario_de_padroes
                or cidade_id not in cidades)
        if fora:
            duras += 1
            afirmar(r["recusa_dura"] is not None,
                    "%s: estado fora da faixa e a F2 NAO recusou" % onde)
            afirmar(r["linhas"] == [] and r["total"] is None,
                    "%s: recusa dura publicou linha ou total" % onde)
            afirmar(r["frase_resposta"] is None,
                    "%s: recusa dura publicou frase de resposta" % onde)
            continue

        afirmar(r["recusa_dura"] is None, "%s: a F2 recusou um estado valido" % onde)
        afirmar(r["frase_resposta"],
                "%s: estado valido sem frase de resposta" % onde)

        # 3a. a linha NOSSA, com a aritmetica refeita
        nossas = [l for l in r["linhas"] if l["categoria"] == "experiencias"]
        # `pendente_de_releitura` ENTRA: preco lido e nao reconferido continua sendo
        # preco lido, e o mesmo item aparece na F1 com ressalva. So `excluido_do_banco`
        # fica fora. A primeira versao desta ferramenta so aceitava `publicavel`, e a
        # consequencia era a pagina de Siem Reap dizendo que esta ilha nao leu um preco
        # que ela leu — o gerador achou isso antes do commit.
        esperadas = [e for e in (banco.get("experiencias") or [])
                     if e.get("cidade") == cidade_id
                     and e.get("status") != "excluido_do_banco"
                     and any(v.get("preco") is not None for v in (e.get("versoes") or []))]
        if esperadas:
            afirmar(len(nossas) == 1, "%s: cidade com experiencia lida e sem a linha" % onde)
            linha = nossas[0]
            com_linha_nossa += 1
            piso = Fraction(0)
            teto = Fraction(0)
            for exp in esperadas:
                totais = []
                for v in (exp.get("versoes") or []):
                    if v.get("preco") is None:
                        continue
                    totais.append((
                        _total_da_experiencia_a_mao(v.get("preco"), v.get("unidade_de_preco"),
                                                    v.get("capacidade_maxima"), pessoas),
                        v.get("id")))
                piso += min(totais)[0]
                teto += max(totais)[0]
            afirmar(Fraction(str(linha["minimo"])) == piso,
                    "%s: piso da linha de experiencias e %s e a conta a mao da %s"
                    % (onde, linha["minimo"], piso))
            afirmar(Fraction(str(linha["maximo"])) == teto,
                    "%s: teto da linha de experiencias e %s e a conta a mao da %s"
                    % (onde, linha["maximo"], teto))
            afirmar(linha["procedencia"] == "nossa",
                    "%s: a linha de experiencias tem de se declarar NOSSA" % onde)
            # o numero escrito na frase tem de ser o numero calculado
            esperado_escrito = (_numero_na_frase(piso, linha["moeda"]) if piso == teto
                                else "%s a %s" % (_numero_na_frase(piso, linha["moeda"]),
                                                  _numero_na_frase(teto, linha["moeda"])))
            afirmar(linha["escrito"] == esperado_escrito,
                    "%s: a linha escreve %r e a conta a mao escreve %r"
                    % (onde, linha["escrito"], esperado_escrito))
            # A LINHA NAO CRESCE COM OS DIAS, e isto e medido e nao prometido
            outro = f2.responder(cidade_id, f2.DIAS_MAXIMO if dias != f2.DIAS_MAXIMO else 1,
                                 pessoas, padrao, banco, esquema, constantes)
            nossa_outro = [l for l in outro["linhas"] if l["categoria"] == "experiencias"][0]
            afirmar(nossa_outro["minimo"] == linha["minimo"]
                    and nossa_outro["maximo"] == linha["maximo"],
                    "%s: a linha de experiencias MUDOU com o numero de dias, e ela nao "
                    "pode: quantas experiencias cabem em N dias nao esta no banco" % onde)
            afirmar(any(rc["codigo"] == "experiencias_nao_crescem_com_os_dias"
                        for rc in r["recusas"]),
                    "%s: a linha de experiencias nao cresce com os dias e a pagina nao "
                    "diz isso ao leitor" % onde)
            pendentes_na_cidade = [e for e in esperadas if e.get("status") != "publicavel"]
            if pendentes_na_cidade:
                afirmar(any(rc["codigo"] == "preco_lido_e_nao_reconferido"
                            for rc in r["recusas"]),
                        "%s: ha preco lido e NAO reconferido na conta e a pagina nao diz "
                        "a ressalva. Somar sem ressalvar e pior que nao somar" % onde)
        else:
            afirmar(nossas == [],
                    "%s: cidade SEM experiencia lida publicou a linha nossa" % onde)
            afirmar(any(rc["codigo"] == "sem_experiencia_lida" for rc in r["recusas"]),
                    "%s: cidade sem experiencia lida e sem a recusa nomeada" % onde)

        # 3b. as linhas de terceiro: cada categoria aparece OU e recusada pelo nome
        for categoria in f2.CATEGORIAS_DE_TERCEIRO:
            tem = [l for l in r["linhas"] if l["categoria"] == categoria]
            publicaveis = [fx for fx in (banco.get("faixas_diarias") or [])
                           if fx.get("status") == "publicavel"
                           and fx.get("cidade") == cidade_id
                           and fx.get("categoria_de_custo") == categoria
                           and fx.get("padrao") == padrao]
            escalaveis = [fx for fx in publicaveis
                          if fx.get("base") != "por_quarto_por_dia"
                          or fx.get("pessoas_por_quarto") is not None]
            if escalaveis:
                afirmar(len(tem) == 1,
                        "%s/%s: ha faixa publicavel e a linha nao saiu" % (onde, categoria))
                afirmar(tem[0]["procedencia"] == "de_terceiro",
                        "%s/%s: a linha tem de se declarar DE TERCEIRO" % (onde, categoria))
                for bloco in tem[0]["blocos"]:
                    afirmar(bloco["publicado_por"],
                            "%s/%s: bloco sem o nome de quem publicou" % (onde, categoria))
                    afirmar(bloco["metodo_declarado"],
                            "%s/%s: bloco sem a frase de quem publicou" % (onde, categoria))
                naturezas = {b["natureza"] for b in tem[0]["blocos"]}
                afirmar(tem[0]["unico_intervalo"] == (len(naturezas) == 1),
                        "%s/%s: `unico_intervalo` discorda do numero de naturezas"
                        % (onde, categoria))
                if len(naturezas) > 1:
                    afirmar(any(rc["codigo"] == "naturezas_em_conflito_%s" % categoria
                                for rc in r["recusas"]),
                            "%s/%s: naturezas em conflito sem a recusa nomeada. Somar "
                            "media com minimo daria um intervalo que ninguem publicou"
                            % (onde, categoria))
            else:
                afirmar(tem == [],
                        "%s/%s: nao ha faixa escalavel e a linha saiu" % (onde, categoria))
                afirmar(any(rc["codigo"] in ("sem_faixa_%s" % categoria,
                                             "faixa_de_quarto_sem_ocupacao")
                            for rc in r["recusas"]),
                        "%s/%s: categoria ausente sem recusa nomeada. Linha que nao sai e "
                        "nao e explicada e espaco em branco com cara de zero"
                        % (onde, categoria))

        # 3c. O TOTAL so existe com as quatro linhas
        publicadas = {l["categoria"] for l in r["linhas"]}
        completo = publicadas == set(("experiencias",) + f2.CATEGORIAS_DE_TERCEIRO)
        if completo:
            com_total += 1
            afirmar(r["total"] is not None,
                    "%s: as quatro linhas existem e nao ha total" % onde)
            soma_min = Fraction(0)
            soma_max = Fraction(0)
            for linha in r["linhas"]:
                if linha["categoria"] == "experiencias":
                    soma_min += Fraction(str(linha["minimo"]))
                    soma_max += Fraction(str(linha["maximo"]))
                else:
                    soma_min += min(Fraction(str(b["minimo"])) for b in linha["blocos"])
                    soma_max += max(Fraction(str(b["maximo"])) for b in linha["blocos"])
            afirmar(Fraction(str(r["total"]["minimo"])) == soma_min,
                    "%s: total minimo %s e a soma a mao %s"
                    % (onde, r["total"]["minimo"], soma_min))
            afirmar(Fraction(str(r["total"]["maximo"])) == soma_max,
                    "%s: total maximo %s e a soma a mao %s"
                    % (onde, r["total"]["maximo"], soma_max))
            afirmar(Fraction(str(r["total"]["por_pessoa_por_dia"]))
                    == _centavo_a_mao(soma_max / pessoas / dias),
                    "%s: o por pessoa por dia nao bate com a conta a mao" % onde)
        else:
            afirmar(r["total"] is None,
                    "%s: faltam linhas e a F2 publicou total. Total somado so com o que a "
                    "ilha tem e um numero menor que a viagem com cara de viagem inteira"
                    % onde)
            afirmar(any(rc["codigo"] == "total_impossivel" for rc in r["recusas"]),
                    "%s: total impossivel sem a recusa nomeada" % onde)

        # 3d. AS DUAS PROCEDENCIAS NUNCA NA MESMA LINHA
        for linha in r["linhas"]:
            afirmar(("blocos" in linha) != ("minimo" in linha),
                    "%s: a linha %r tem as duas formas ao mesmo tempo — a nossa (um "
                    "intervalo) e a de terceiro (blocos com dono). Misturar as duas "
                    "procedencias numa linha e o defeito que esta ilha existe para nao "
                    "cometer" % (onde, linha["categoria"]))

        # 3e. A FRASE: acento, bastidor, frase proibida, buraco de formatacao
        for frase in _frases_de(r):
            baixo = frase.lower()
            for palavra in p1.SEM_ACENTO_PROIBIDO:
                if re.search(r"(?<![0-9a-zà-ÿ])%s(?![0-9a-zà-ÿ])" % re.escape(palavra), baixo):
                    afirmar(False, "%s: a tela publica %r sem acento em «%s»"
                            % (onde, palavra, frase[:90]))
            for proibida in p1.FRASES_PROIBIDAS:
                if proibida in baixo:
                    afirmar(False, "%s: frase proibida %r em «%s»"
                            % (onde, proibida, frase[:90]))
            for nome, forma in p1.FORMAS_DE_BASTIDOR:
                achado = forma.search(frase)
                if achado:
                    afirmar(False, "%s: texto de bastidor da fabrica (%s: %r) em «%s»"
                            % (onde, nome, achado.group(0), frase[:90]))
            afirmar("%s" not in frase and "%d" not in frase,
                    "%s: buraco de formatacao na tela: «%s»" % (onde, frase[:90]))
            afirmar("  " not in frase,
                    "%s: espaco dobrado na tela: «%s»" % (onde, frase[:90]))
            afirmar("None" not in frase,
                    "%s: a palavra None foi para a tela: «%s»" % (onde, frase[:90]))
            afirmar(" 1 experiências" not in frase and " 1 dias" not in frase
                    and " 1 pessoas" not in frase,
                    "%s: concordancia errada na tela: «%s»" % (onde, frase[:90]))

    # ---- 4. A TABELA PRE-RENDERIZADA
    tabela = f2.tabela_pre_renderizada(banco, esquema, constantes)
    afirmar(len(tabela) == len(cidades) * len(vocabulario_de_padroes)
            * len(f2.DIAS_DA_TABELA) * len(f2.PESSOAS_DA_TABELA),
            "a tabela tem %d linhas e a grade dela pede %d"
            % (len(tabela), len(cidades) * len(vocabulario_de_padroes)
               * len(f2.DIAS_DA_TABELA) * len(f2.PESSOAS_DA_TABELA)))
    for linha in tabela:
        afirmar(linha["linhas_publicadas"] + linha["linhas_recusadas"] == 4,
                "linha da tabela com %d publicadas e %d recusadas: as duas somam 4"
                % (linha["linhas_publicadas"], linha["linhas_recusadas"]))
        afirmar(f2.DIAS_MINIMO <= linha["dias"] <= f2.DIAS_MAXIMO,
                "linha da tabela com dias fora da faixa")

    # ---- 5. O ARQUIVO GRAVADO
    # Para cada campo publicado, a bancada le a MESMA fonte que a pagina vai ler: a
    # pagina vai ler dados/f2-respostas.json, entao e ele que esta afirmacao abre, e
    # nao a referencia outra vez. Sem isto o arquivo pode envelhecer em silencio
    # enquanto a referencia muda, e o portao continuaria verde.
    caminho = os.path.join(DADOS, "f2-respostas.json")
    if doc_respostas is None and not os.path.exists(caminho):
        afirmar(False, "dados/f2-respostas.json nao existe. Rode gerar-f2.py --gravar.")
    else:
        doc = doc_respostas if doc_respostas is not None else _ler("f2-respostas.json")
        afirmar(doc.get("publicar") is False,
                "f2-respostas.json com `publicar` %r. Esta ilha nao tem site: nao existe "
                "'no ar' para onde publicar." % doc.get("publicar"))
        rg = doc["resumo"]
        afirmar(rg["estados_gravados"] == len(doc["respostas"]),
                "f2-respostas.json diz %d estados gravados e traz %d respostas"
                % (rg["estados_gravados"], len(doc["respostas"])))
        afirmar(rg["estados"] == len(todos),
                "f2-respostas.json diz %d estados servidos e a grade de hoje tem %d: o "
                "arquivo envelheceu e a pagina leria um dominio que nao e mais o do banco"
                % (rg["estados"], len(todos)))
        # O arquivo grava MENOS do que a F2 serve, e isso e decisao escrita nele. O que
        # o portao cobra e que ele grave a grade da tabela INTEIRA mais TODAS as bordas:
        # arquivo que perdesse uma borda ficaria sem nenhum caso gravado da metade que
        # recusa, e e essa metade que esta ilha tem de diferente.
        afirmar(rg["estados_gravados"] >= len(doc["tabela_pre_renderizada"]),
                "f2-respostas.json grava %d estados e a tabela tem %d linhas: a grade da "
                "tabela nao cabe no que foi gravado"
                % (rg["estados_gravados"], len(doc["tabela_pre_renderizada"])))
        duras_servidas = sum(1 for c, d, p, pa in todos
                             if not (f2.DIAS_MINIMO <= d <= f2.DIAS_MAXIMO)
                             or not (f2.f1.PESSOAS_MINIMO <= p <= f2.f1.PESSOAS_MAXIMO)
                             or pa not in vocabulario_de_padroes or c not in cidades)
        afirmar(rg["estados_recusados_na_borda"] == duras_servidas,
                "f2-respostas.json gravou %d bordas e a grade tem %d: borda que nao foi "
                "gravada e a metade que RECUSA sem nenhum caso no arquivo"
                % (rg["estados_recusados_na_borda"], duras_servidas))
        afirmar(rg["cidades"] == len(cidades),
                "f2-respostas.json diz %d cidades e o banco tem %d contadas"
                % (rg["cidades"], len(cidades)))
        afirmar(rg["faixas_diarias"] == len(banco.get("faixas_diarias") or []),
                "f2-respostas.json diz %d faixas diarias e o banco tem %d contadas"
                % (rg["faixas_diarias"], len(banco.get("faixas_diarias") or [])))
        afirmar(rg["linhas_da_tabela"] == len(doc["tabela_pre_renderizada"]),
                "f2-respostas.json diz %d linhas de tabela e traz %d"
                % (rg["linhas_da_tabela"], len(doc["tabela_pre_renderizada"])))
        afirmar(rg["estados_recusados_na_borda"] > 0,
                "f2-respostas.json nao gravou nenhum estado de borda. A metade que "
                "RECUSA ficaria sem um caso gravado.")
        gravadas_duras = sum(1 for x in doc["respostas"] if x["recusa_dura"])
        afirmar(gravadas_duras == rg["estados_recusados_na_borda"],
                "f2-respostas.json diz %d recusas de borda e tem %d"
                % (rg["estados_recusados_na_borda"], gravadas_duras))
        # DOIS numeros, e cada um responde a uma pergunta diferente: o gravado tem de
        # bater com o CONTEUDO do arquivo, e o do dominio com a VARREDURA deste portao.
        # Comparar o do dominio com o conteudo do arquivo recortado foi o defeito que a
        # bateria de mutacoes achou em 22/10/2026 — invisivel com zero faixas no banco,
        # porque ali os dois numeros valem 0.
        afirmar(rg["estados_gravados_com_total"]
                == sum(1 for x in doc["respostas"] if x["total"]),
                "f2-respostas.json diz %d estados gravados com total e tem %d"
                % (rg["estados_gravados_com_total"],
                   sum(1 for x in doc["respostas"] if x["total"])))
        afirmar(rg["estados_com_total"] == com_total,
                "f2-respostas.json diz %d estados com total no dominio e esta varredura "
                "contou %d" % (rg["estados_com_total"], com_total))
        afirmar(rg["estados_gravados_com_total"] <= rg["estados_com_total"],
                "f2-respostas.json grava %d estados com total e o dominio tem %d: o "
                "arquivo nao pode ter mais do que existe"
                % (rg["estados_gravados_com_total"], rg["estados_com_total"]))
        # O arquivo guarda dinheiro como TEXTO, nunca como float: float de dinheiro
        # quase sempre imprime igual, e e por isso que a perda do centavo passaria.
        for x in doc["respostas"][:200]:
            for linha in x.get("linhas") or []:
                if "minimo" in linha:
                    afirmar(isinstance(linha["minimo"], str),
                            "f2-respostas.json gravou o piso como %s em vez de texto: "
                            "float de dinheiro perde o centavo sem ninguem ver"
                            % type(linha["minimo"]).__name__)

    resumo = {
        "estados varridos": len(todos),
        "recusas duras": duras,
        "estados com a linha nossa": com_linha_nossa,
        "estados com total": com_total,
        "linhas da tabela": len(tabela),
        "faixas diarias no banco": len(banco.get("faixas_diarias") or []),
        "afirmacoes": afirmacoes,
    }
    return falhas, resumo


def main():
    falhas, resumo = conferir()
    print("PORTAO DA F2 — jornadafly")
    print("")
    for chave, valor in resumo.items():
        print("  %-28s %s" % (chave + ":", valor))
    print("")
    if falhas:
        for f in falhas[:40]:
            print("  FALHA: %s" % f)
        if len(falhas) > 40:
            print("  ... e mais %d" % (len(falhas) - 40))
        print("")
        print("%d falha(s)." % len(falhas))
        return 1
    print("0 falha(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
