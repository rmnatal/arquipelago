#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PORTAO DA F3 -- varre o dominio inteiro e refaz a aritmetica a mao.

    python3 ferramentas/teste-f3.py

Reprova com codigo de saida 1. Nao abre a rede e nao escreve nada em disco.

O QUE ESTE PORTAO MEDE, e por que ele e assim:

  1. A ARITMETICA, REFEITA EM Fraction. Todo numero que a F3 publica e recalculado
     aqui por um caminho diferente -- Fraction em vez de Decimal, com o
     arredondamento meio-para-cima escrito a mao -- porque regua que chama a mesma
     funcao da ferramenta nao mede a conta, mede a si mesma.
  2. O DOMINIO INTEIRO, NAO UMA AMOSTRA. Os estados de dentro e as bordas de fora,
     incluindo as SETE recusas duras desta ferramenta (dias, grupo, cidade, escolha
     vazia, atracao repetida, atracao desconhecida e o passe escolhido como atracao).
  3. AS FUNCOES PURAS COM MUNDOS QUE O BANCO NAO TEM, e aqui isto e a ferramenta
     INTEIRA: o banco tem ZERO passes e ZERO coberturas, entao o valor entregue, o
     ponto de equilibrio, os tres desfechos do veredito e a leitura da hedge do
     desconto SO sao mediveis assim. Sem esta metade, a F3 seria uma frase que nada
     confere, e o dia em que o primeiro passe for carregado seria o dia de descobrir
     que ela estava errada.
  4. A FRASE, e nao so o numero. Acento, concordancia, frase proibida do VOZ.md e
     texto de bastidor da fabrica (secao 32.4 do ARQUIPELAGO.md). As listas vem do
     portao da F1 por IMPORTACAO, nunca copiadas.
  5. AS TRES REGRAS DA COBERTURA, uma por uma: que «nao lida» nunca seja publicada
     como «nao coberta», que o equilibrio diga sobre quantas atracoes foi calculado,
     e que desconto com teto entre como faixa de ZERO ao teto.
  6. QUE O VENCIMENTO DA F3 CONCORDE COM O DO VALIDADOR. A regra de validade do
     preco mora em `f1.preco_vencido` desde 22/10/2026 e o validador tem a dele
     escrita por dentro; este portao compara os dois vereditos VERSAO POR VERSAO do
     banco. Duas metades da mesma regra que nunca se falam e o defeito que esta
     pasta mais paga.
"""

import datetime
import importlib.util
import io
import json
import math
import os
import sys
from fractions import Fraction

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(AQUI)
DADOS = os.path.join(BASE, "dados")

# OS LIMITES, ESCRITOS AQUI E NAO LIDOS DA FERRAMENTA. Eles vem da especificacao
# (dados/especificacao-calculadoras.md, secoes 3 e 4.1), e a razao esta medida: em
# 22/10/2026 a bateria da F2 trocou o teto de dias de 21 para 60 e o portao PASSOU,
# porque grade, bordas e a conta do que esta «fora» saiam todas de `f2.DIAS_MAXIMO`.
# Regua que toma o limite da coisa que ela mede nao mede o limite.
DIAS_DA_ESPECIFICACAO = (1, 21)
PESSOAS_DA_ESPECIFICACAO = (1, 12)
ATRACOES_DA_ESPECIFICACAO = 8


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
    return _modulo("f3-referencia.py", "f3_referencia")


def _portao_da_f1():
    """As listas de frase e de bastidor vem DAQUI, nunca de uma copia local."""
    return _modulo("teste-f1.py", "teste_f1")


def _validador():
    return _modulo("validar-banco.py", "validar_banco")


# ---------------------------------------------------------------------------
# A ARITMETICA, REFEITA POR OUTRO CAMINHO
# ---------------------------------------------------------------------------

def _centavo_a_mao(valor):
    """Arredonda ao centavo, meio-para-CIMA, escrito a mao em Fraction."""
    v = Fraction(valor) * 100
    piso = v.numerator // v.denominator
    resto = v - piso
    if resto >= Fraction(1, 2):
        piso += 1
    return Fraction(piso, 100)


def _total_a_mao(preco, unidade, capacidade, pessoas):
    """A Conta 1 da F1, refeita: por pessoa multiplica; as outras tomam o teto."""
    p = Fraction(str(preco))
    if unidade == "por_pessoa":
        return p * pessoas
    if capacidade is None or capacidade < 1:
        raise AssertionError("capacidade %r invalida para unidade %r" % (capacidade, unidade))
    return p * int(math.ceil(float(pessoas) / capacidade))


def _valor_entregue_a_mao(piso, teto, como, pct, teto_declarado):
    """O que o passe entrega, refeito a mao."""
    pi, te = Fraction(str(piso)), Fraction(str(teto))
    if como == "entrada_incluida":
        return pi, te
    if como == "sem_efeito_no_preco":
        return Fraction(0), Fraction(0)
    if como == "desconto_declarado":
        fator = Fraction(str(pct)) / 100
        if teto_declarado:
            return Fraction(0), te * fator
        return pi * fator, te * fator
    raise AssertionError("forma %r sem conta a mao" % (como,))


def _equilibrio_a_mao(valores, preco):
    """O ponto de equilibrio refeito a mao, por um caminho diferente: em vez de
    ordenar indices, ordena os PROPRIOS valores e acumula. Devolve o numero de
    atracoes ou None."""
    acumulado = Fraction(0)
    alvo = Fraction(str(preco))
    for posicao, valor in enumerate(sorted((Fraction(str(v)) for v in valores),
                                           reverse=True), start=1):
        acumulado += valor
        if acumulado >= alvo:
            return posicao
    return None


def _frases_de(resposta):
    """Toda frase que a resposta manda para a tela, achatada.

    Mede o CORPO e nao o JSON inteiro: o JSON carrega codigo de recusa, id de cidade
    e id de atracao, que nao sao texto de tela e reprovariam por acento sem nenhum
    defeito embaixo.
    """
    frases = []
    if resposta["recusa_dura"]:
        return [resposta["recusa_dura"]["frase"]]
    frases.append(resposta["frase_resposta"])
    if resposta["avulsos"]:
        frases.append(resposta["avulsos"]["frase_de_procedencia"])
        frases.append(resposta["avulsos"]["multiplicador"])
        frases.extend(resposta["avulsos"]["detalhe"])
    for bloco in resposta["passes"]:
        for entrega in bloco["entregas"]:
            frases.append(entrega["rotulo_da_cobertura"])
            frases.append(entrega["o_que_entrega"])
            frases.append(entrega["qual_bilhete"])
        for versao in bloco["versoes"]:
            frases.append(versao["frase_do_veredito"])
            if versao["frase_do_equilibrio"]:
                frases.append(versao["frase_do_equilibrio"])
    for rec in resposta["recusas"]:
        frases.append(rec["frase"])
    frases.append(resposta["como_sabemos"]["frase"])
    for grupo in ("preco_das_atracoes", "preco_dos_passes", "cobertura_dos_passes"):
        for f in resposta["como_sabemos"][grupo]:
            frases.append(f["frase"])
    return [f for f in frases if f]


# ---------------------------------------------------------------------------
# OS MUNDOS DE BANCADA DESTE PORTAO
#
# Nenhum deles e gravado: sao dicionarios que vivem dentro deste processo. Eles
# existem porque o banco de hoje tem ZERO passes, e sem eles a metade da F3 que
# compara passe com avulso nunca seria executada por ninguem.
# ---------------------------------------------------------------------------

def _atracao(aid, nome, versoes, status="publicavel", cidade="roma"):
    return {
        "id": aid, "nome": nome, "cidade": cidade,
        "categoria": "ingresso_de_sitio_publico", "status": status,
        "versoes": [{"id": v[0], "rotulo": v[1], "preco": v[2],
                     "unidade_de_preco": v[3] if len(v) > 3 else "por_pessoa",
                     "capacidade_maxima": v[4] if len(v) > 4 else None,
                     "moeda": "EUR", "fonte": "fonte-de-bancada",
                     "data_leitura": "2026-10-20"} for v in versoes],
        "operador": {"nome": "operador de bancada", "tipo": "operador_privado"},
        "afiliado": {"programa": None, "url": "", "url_produto": None,
                     "url_busca_produto": "https://civitatis.com/br/roma/"},
    }


def _passe(preco_por_versao, declaradas=2, cidade="roma", status="publicavel"):
    return {
        "id": "passe-de-bancada", "nome": "Passe de bancada", "cidade": cidade,
        "categoria": "passe_de_cidade", "status": status,
        "atracoes_declaradas_pelo_passe": declaradas,
        "versoes": [{"id": v[0], "rotulo": v[1], "preco": v[2],
                     "unidade_de_preco": "por_pessoa", "capacidade_maxima": None,
                     "dias_de_uso": v[3], "moeda": "EUR",
                     "fonte": "fonte-de-bancada", "data_leitura": "2026-10-20"}
                    for v in preco_por_versao],
        "operador": {"nome": "operador de bancada", "tipo": "operador_privado"},
        "afiliado": {"programa": None, "url": "", "url_produto": None,
                     "url_busca_produto": "https://civitatis.com/br/roma/"},
    }


def _cob(atracao, como="entrada_incluida", versao=None, pct=None, teto=None,
         reserva=False, status="publicavel"):
    return {
        "id": "cob-" + atracao, "passe": "passe-de-bancada", "experiencia": atracao,
        "versao_coberta": versao,
        "motivo_sem_versao_coberta": None if versao else "a fonte não diz qual bilhete",
        "como": como, "desconto_percentual": pct, "desconto_e_no_maximo": teto,
        "desconto_transcrito_de": None if pct is None else "desconto de bancada",
        "reserva_obrigatoria": reserva,
        "reserva_transcrita_de": "a reserva é obrigatória" if reserva else None,
        "declarada_por": "no_texto_da_fonte", "fonte": "fonte-de-bancada",
        "data_leitura": "2026-10-20", "status": status,
    }


def _banco_de_bancada(atracoes, passes=(), coberturas=()):
    return {
        "cidades": [{"id": "roma", "nome": "Roma", "pais": "Itália",
                     "moeda_local": "EUR", "slug_plataforma": "roma"}],
        "fontes": [{"id": "fonte-de-bancada", "nivel": 4,
                    "origem": "operador-via-busca", "leitura": "busca_web",
                    "autor": "operador de bancada", "documento": "página de bancada",
                    "url": None, "motivo_sem_url": "mundo de bancada"}],
        "experiencias": list(atracoes) + list(passes),
        "coberturas_de_passe": list(coberturas),
        "faixas_diarias": [],
        "resumo": {},
    }


# ---------------------------------------------------------------------------
# O PORTAO
# ---------------------------------------------------------------------------

def conferir(f3=None, banco=None, esquema=None, constantes=None, doc_respostas=None,
             hoje=None):
    """O portao inteiro sobre dicionarios EM MEMORIA. Devolve (falhas, resumo).

    E assim que ferramentas/mutacoes-f3.py produz os mundos que o banco ainda nao
    tem -- passe, cobertura, desconto com teto, veredito que atravessa o preco -- e
    quebra a propria referencia para ver o portao reprovar, sem gravar uma linha no
    banco de verdade.
    """
    f3 = f3 if f3 is not None else _referencia()
    banco = banco if banco is not None else _ler("experiencias.json")
    esquema = esquema if esquema is not None else _ler("esquema-banco.json")
    constantes = constantes if constantes is not None else _ler("constantes.json")
    hoje = hoje if hoje is not None else datetime.date.today()
    p1 = _portao_da_f1()

    falhas = []
    afirmacoes = 0

    def afirmar(condicao, mensagem):
        nonlocal afirmacoes
        afirmacoes += 1
        if not condicao:
            falhas.append(mensagem)

    cidades = {c.get("id"): c for c in (banco.get("cidades") or [])}

    # ---- 1. AS LISTAS DA F3 CONTRA O VOCABULARIO DO ESQUEMA
    faltas = f3.conferir_vocabularios(esquema)
    afirmar(faltas == [],
            "a F3 e o vocabulario do esquema discordam: %s" % "; ".join(faltas))

    # ---- 1b. OS LIMITES, CONTRA A ESPECIFICACAO E NAO CONTRA A FERRAMENTA
    afirmar((f3.DIAS_MINIMO, f3.DIAS_MAXIMO) == DIAS_DA_ESPECIFICACAO,
            "a F3 aceita de %d a %d dias e a especificacao diz de %d a %d. Teto novo e "
            "decisao de produto: ele muda na especificacao primeiro, e aqui depois"
            % ((f3.DIAS_MINIMO, f3.DIAS_MAXIMO) + DIAS_DA_ESPECIFICACAO))
    afirmar((f3.f1.PESSOAS_MINIMO, f3.f1.PESSOAS_MAXIMO) == PESSOAS_DA_ESPECIFICACAO,
            "a F3 aceita de %d a %d pessoas e a especificacao diz de %d a %d"
            % ((f3.f1.PESSOAS_MINIMO, f3.f1.PESSOAS_MAXIMO) + PESSOAS_DA_ESPECIFICACAO))
    afirmar(f3.ATRACOES_MAXIMO == ATRACOES_DA_ESPECIFICACAO,
            "a F3 compara ate %d atracoes e a especificacao diz %d. O dominio desta "
            "ferramenta cresce em 2^n: mudar este teto muda o tamanho da grade que "
            "alguem tem de ter conferido"
            % (f3.ATRACOES_MAXIMO, ATRACOES_DA_ESPECIFICACAO))
    afirmar(f3.DIAS_MAXIMO in f3.DIAS_DA_TABELA and f3.DIAS_MINIMO in f3.DIAS_DA_TABELA,
            "a tabela pre-renderizada nao mostra as bordas de dentro (%r): tabela que "
            "para antes da borda esconde o degrau que esta ali" % (f3.DIAS_DA_TABELA,))

    # ---- 2. AS FUNCOES PURAS, COM MUNDOS QUE O BANCO NAO TEM

    # 2a. valor_entregue nas quatro formas, com a conta refeita a mao
    for como, pct, teto_declarado in (("entrada_incluida", None, None),
                                      ("sem_efeito_no_preco", None, None),
                                      ("desconto_declarado", 50, False),
                                      ("desconto_declarado", 50, True),
                                      ("desconto_declarado", 12.5, False),
                                      ("desconto_declarado", 12.5, True),
                                      ("desconto_declarado", 99, True)):
        for piso, teto in ((36, 44), (18, 18), (0.01, 1000), (14.8, 36.7)):
            dado = f3.valor_entregue(piso, teto, como, pct, teto_declarado)
            mao = _valor_entregue_a_mao(piso, teto, como, pct, teto_declarado)
            afirmar((Fraction(str(dado[0])), Fraction(str(dado[1]))) == mao,
                    "valor_entregue(%r, %r, %s, %r, %r) deu %r e a conta a mao da %r"
                    % (piso, teto, como, pct, teto_declarado, dado, mao))

    # 2b. A TERCEIRA REGRA DA COBERTURA, medida no numero: «ate 50%» entrega de ZERO
    #     ao teto, e nao o percentual cheio nas duas pontas.
    cheio = f3.valor_entregue(36, 44, "desconto_declarado", 50, False)
    com_teto = f3.valor_entregue(36, 44, "desconto_declarado", 50, True)
    afirmar(Fraction(str(cheio[0])) == 18 and Fraction(str(cheio[1])) == 22,
            "desconto cheio de 50%% sobre 36 a 44 tem de dar 18 a 22: deu %r" % (cheio,))
    afirmar(Fraction(str(com_teto[0])) == 0 and Fraction(str(com_teto[1])) == 22,
            "desconto que e TETO tem de comecar em ZERO: «ate 50%%» nao e 50%%, e a ponta "
            "de baixo e o que impede a hedge da fonte de entrar como numero cheio. "
            "Deu %r" % (com_teto,))
    afirmar(f3.valor_entregue(36, 44, "sem_efeito_no_preco")[1] == 0,
            "cobertura sem efeito no preco tem de entregar ZERO nas duas pontas: contar "
            "beneficio de fila como dinheiro faz um passe parecer que paga")

    # 2c. valor_entregue nas bordas: MORRE em vez de escolher
    for argumentos in ((None, 44, "entrada_incluida", None, None),
                       (36, None, "entrada_incluida", None, None),
                       (44, 36, "entrada_incluida", None, None),
                       (36, 44, "forma_que_nao_existe", None, None),
                       (36, 44, "desconto_declarado", None, False),
                       (36, 44, "desconto_declarado", 0, False),
                       (36, 44, "desconto_declarado", 100, False),
                       (36, 44, "desconto_declarado", 50, None)):
        try:
            f3.valor_entregue(*argumentos)
            afirmar(False, "valor_entregue aceitou %r e devolveu numero" % (argumentos,))
        except f3.BancoIncompleto:
            afirmar(True, "")

    # 2d. ponto_de_equilibrio_em_atracoes: vazio, exato, nunca alcanca, empate, zeros
    afirmar(f3.ponto_de_equilibrio_em_atracoes([], 10) is None,
            "equilibrio de lista vazia tem de dar None — zero atracoes nao se pagam")
    for valores, preco in (([20, 20, 20], 50), ([20, 20, 20], 60), ([20, 20, 20], 61),
                           ([5, 50, 10], 50), ([5, 50, 10], 55), ([0, 0, 30], 30),
                           ([0, 0, 30], 31), ([18], 18), ([18], 19),
                           ([36, 22, 0, 14.8], 60), ([1, 1, 1, 1, 1, 1, 1, 1], 8)):
        dado = f3.ponto_de_equilibrio_em_atracoes(valores, preco)
        mao = _equilibrio_a_mao(valores, preco)
        afirmar((dado["quantas"] if dado else None) == mao,
                "ponto_de_equilibrio_em_atracoes(%r, %r) deu %r e a conta a mao da %r"
                % (valores, preco, dado["quantas"] if dado else None, mao))
        if dado:
            soma = sum(Fraction(str(valores[i])) for i in dado["ordem"])
            afirmar(soma >= Fraction(str(preco)),
                    "a ordem devolvida por ponto_de_equilibrio_em_atracoes(%r, %r) soma "
                    "%s e nao alcanca o preco" % (valores, preco, soma))
            afirmar(len(dado["ordem"]) == dado["quantas"],
                    "a ordem tem %d atracoes e `quantas` diz %d: a tela nomearia um "
                    "numero de atracoes diferente do que a frase anuncia"
                    % (len(dado["ordem"]), dado["quantas"]))
            valores_na_ordem = [Fraction(str(valores[i])) for i in dado["ordem"]]
            afirmar(valores_na_ordem == sorted(valores_na_ordem, reverse=True),
                    "a ordem nao esta das mais caras para as mais baratas (%r): e ela "
                    "que da o MENOR numero de atracoes, e a tela declara essa ordem"
                    % (valores_na_ordem,))
    # O desempate da ordem e ESTAVEL: dois valores iguais saem na ordem de entrada.
    empate = f3.ponto_de_equilibrio_em_atracoes([10, 10, 10], 20)
    afirmar(empate["ordem"] == [0, 1],
            "no empate a ordem tem de ser ESTAVEL (indice de entrada), para a tela nao "
            "nomear uma atracao diferente a cada carga: deu %r" % (empate["ordem"],))
    for preco in (0, -1, None, True, "18"):
        try:
            f3.ponto_de_equilibrio_em_atracoes([10], preco)
            afirmar(False, "equilibrio aceitou preco de passe %r" % (preco,))
        except f3.BancoIncompleto:
            afirmar(True, "")

    # 2e. veredito: TRES desfechos, e as bordas exatas de cada fronteira
    for piso, teto, preco, esperado in ((36, 44, 30, "paga"), (36, 44, 36, "paga"),
                                        (36, 44, 37, "depende_da_versao"),
                                        (36, 44, 44, "depende_da_versao"),
                                        (36, 44, 45, "nao_paga"),
                                        (0, 22, 10, "depende_da_versao"),
                                        (0, 0, 10, "nao_paga"),
                                        (50, 50, 50, "paga"),
                                        (50, 50, 51, "nao_paga")):
        codigo, folga = f3.veredito(piso, teto, preco)
        afirmar(codigo == esperado,
                "veredito(%r, %r, %r) deu %r e tem de dar %r"
                % (piso, teto, preco, codigo, esperado))
        if codigo == "paga":
            afirmar(Fraction(str(folga)) == Fraction(str(piso)) - Fraction(str(preco)),
                    "a folga do veredito `paga` nao e piso menos preco")
        else:
            afirmar(folga is None, "veredito %r devolveu folga %r" % (codigo, folga))
    try:
        f3.veredito(44, 36, 40)
        afirmar(False, "veredito aceitou faixa invertida")
    except f3.BancoIncompleto:
        afirmar(True, "")

    # 2f. cobertura_do_par: NAO LIDA e None, e `excluido_do_banco` conta como nao lida
    lista = [_cob("a"), _cob("b", status="excluido_do_banco")]
    afirmar(f3.cobertura_do_par(lista, "passe-de-bancada", "a") is not None,
            "cobertura_do_par nao achou a cobertura que existe")
    afirmar(f3.cobertura_do_par(lista, "passe-de-bancada", "b") is None,
            "cobertura `excluido_do_banco` tem de contar como NAO LIDA: descartada nao "
            "sustenta afirmacao nenhuma")
    afirmar(f3.cobertura_do_par(lista, "outro-passe", "a") is None,
            "cobertura_do_par casou o passe errado")
    afirmar(f3.cobertura_do_par([], "passe-de-bancada", "a") is None,
            "cobertura_do_par de lista vazia tem de dar None")

    # 2g. subconjuntos: 2^n - 1, nao vazios, ordem estavel, sem repetido
    for n in (1, 2, 3, 5, 8):
        atracoes = ["a%d" % i for i in range(n)]
        conjuntos = f3.subconjuntos(atracoes)
        afirmar(len(conjuntos) == (1 << n) - 1,
                "subconjuntos de %d atracoes deu %d e tem de dar %d (2^n - 1)"
                % (n, len(conjuntos), (1 << n) - 1))
        afirmar(len(set(conjuntos)) == len(conjuntos),
                "subconjuntos devolveu combinacao repetida com %d atracoes" % n)
        afirmar(all(c for c in conjuntos),
                "subconjuntos devolveu a escolha VAZIA, que e recusa dura e nao estado")
        afirmar(conjuntos == f3.subconjuntos(atracoes),
                "subconjuntos nao e estavel entre duas chamadas: o arquivo gravado "
                "diferiria sem nenhuma regra ter mudado")
        afirmar([len(c) for c in conjuntos] == sorted(len(c) for c in conjuntos),
                "subconjuntos nao esta em ordem de tamanho")

    # 2h. preco_vencido: a BORDA EXATA do dia em que o preco vence
    fonte_publica = {"origem": "poder-publico-via-busca"}
    fonte_privada = {"origem": "operador-via-busca"}
    afirmar(f3.f1.dias_de_validade(esquema, fonte_publica) == 180,
            "tarifa de poder publico tem de valer 180 dias pelo esquema")
    afirmar(f3.f1.dias_de_validade(esquema, fonte_privada) == 60,
            "preco de operador privado tem de valer 60 dias pelo esquema")
    base = datetime.date(2026, 1, 1)
    for dias_passados, esperado in ((0, False), (59, False), (60, False), (61, True),
                                    (365, True)):
        vencido, passados, janela = f3.f1.preco_vencido(
            esquema, fonte_privada, base.isoformat(),
            base + datetime.timedelta(days=dias_passados))
        afirmar((vencido, passados, janela) == (esperado, dias_passados, 60),
                "preco_vencido com %d dias passados deu %r e tem de dar %r"
                % (dias_passados, (vencido, passados, janela),
                   (esperado, dias_passados, 60)))

    # ---- 3. O MUNDO COM PASSE: a ferramenta inteira, que o banco nao alcanca
    #
    # Tres atracoes em Roma e um passe de duas versoes. O banco de hoje tem UMA
    # atracao por cidade e ZERO passes, entao nenhum destes caminhos e executado pela
    # varredura do dominio real.
    atracoes = [
        _atracao("coliseu", "Coliseu", [("comum", "comum", 18), ("completa", "completa", 22)]),
        _atracao("forum", "Fórum", [("unico", "único", 16)]),
        _atracao("castelo", "Castelo", [("unico", "único", 14)]),
    ]
    # TRES versoes de preco e nao duas, e a terceira existe para que os TRES
    # desfechos do veredito aparecam na MESMA passada: 64 no grupo (abaixo do piso de
    # 68, PAGA), 76 (dentro da faixa 68 a 82, DEPENDE DA VERSAO) e 104 (acima do teto,
    # NAO PAGA). Com duas versoes o desfecho do meio so era exercitado nas chamadas
    # puras, e e justamente ele o que esta ferramenta tem de diferente.
    passe = _passe([("48h", "2 dias", 32, 2), ("96h", "4 dias", 38, 4),
                    ("72h", "3 dias", 52, 3)], declaradas=5)
    coberturas = [_cob("coliseu", versao="comum", reserva=True),
                  _cob("forum"),
                  _cob("castelo", como="desconto_declarado", pct=50, teto=True)]
    mundo = _banco_de_bancada(atracoes, [passe], coberturas)

    r = f3.responder("roma", ("coliseu", "forum", "castelo"), 3, 2, mundo, esquema,
                     constantes, hoje)
    afirmar(r["recusa_dura"] is None, "o mundo com passe caiu em recusa dura")
    bloco = r["passes"][0]
    # Avulsos para 2 pessoas: coliseu 36 a 44, forum 32, castelo 28 -> 96 a 104
    afirmar(Fraction(str(r["avulsos"]["minimo"])) == 96
            and Fraction(str(r["avulsos"]["maximo"])) == 104,
            "a soma dos avulsos do mundo com passe deu %s a %s e a conta a mao da 96 a 104"
            % (r["avulsos"]["minimo"], r["avulsos"]["maximo"]))
    # O que o passe entrega: coliseu na versao NOMEADA (36), forum inteiro (32),
    # castelo com «ate 50%» (0 a 14) -> 68 a 82
    entregue_min = sum(Fraction(str(e["minimo"])) for e in bloco["entregas"])
    entregue_max = sum(Fraction(str(e["maximo"])) for e in bloco["entregas"])
    afirmar(entregue_min == 68 and entregue_max == 82,
            "o valor entregue deu %s a %s e a conta a mao da 68 a 82 (coliseu na versao "
            "nomeada, forum inteiro, castelo so ate a metade)" % (entregue_min, entregue_max))
    v48 = [v for v in bloco["versoes"] if v["versao"] == "48h"][0]
    v96 = [v for v in bloco["versoes"] if v["versao"] == "96h"][0]
    v72 = [v for v in bloco["versoes"] if v["versao"] == "72h"][0]
    afirmar(v48["veredito"] == "paga",
            "o passe de 32 por pessoa (64 no grupo) entrega 68 a 82: ele se paga ate na "
            "ponta de BAIXO, entao tem de dar `paga`. Deu %r" % v48["veredito"])
    afirmar(v96["veredito"] == "depende_da_versao",
            "o passe de 38 por pessoa (76 no grupo) entrega 68 a 82: a faixa ATRAVESSA o "
            "preco, e ali existe bilhete em que ele paga e bilhete em que nao paga. Tem "
            "de dar `depende_da_versao`, e dar qualquer um dos outros dois seria a ilha "
            "escolhendo a versao no lugar de quem viaja. Deu %r" % v96["veredito"])
    afirmar(v72["veredito"] == "nao_paga",
            "o passe de 52 por pessoa (104 no grupo) entrega 68 a 82: nem na ponta de "
            "CIMA ele se paga, entao tem de dar `nao_paga`. Deu %r" % v72["veredito"])
    afirmar({v["veredito"] for v in bloco["versoes"]}
            == {"paga", "depende_da_versao", "nao_paga"},
            "o mundo com passe tem de exercitar os TRES desfechos numa passada: deu %r"
            % ({v["veredito"] for v in bloco["versoes"]},))
    baixo_de_48 = (v48["equilibrio"] or {}).get("na_ponta_de_baixo")
    afirmar(baixo_de_48 is not None and baixo_de_48["quantas"] == 2,
            "o equilibrio do passe de 64 sobre entregas de 36, 32 e 0 tem de ser 2 "
            "atracoes na ponta de baixo: deu %r" % (baixo_de_48,))
    afirmar(bloco["atracoes_declaradas"] == 5 and bloco["coberturas_lidas_no_banco"] == 3,
            "o bloco do passe tem de publicar os DOIS numeros — 5 declaradas e 3 lidas")
    codigos = {rec["codigo"] for rec in r["recusas"]}
    afirmar("equilibrio_sobre_o_que_a_ilha_leu" in codigos,
            "o passe declara 5 atracoes e a ilha leu 3, e a F3 nao disse sobre quantas o "
            "equilibrio foi calculado. E a SEGUNDA regra da cobertura, e sem ela esta "
            "ferramenta publica o mesmo numero sem dono que o 1o colocado publica")
    afirmar("desconto_e_um_teto" in codigos,
            "o castelo tem «ate 50%» e a F3 nao disse que o desconto e um TETO")
    afirmar("reserva_obrigatoria" in codigos,
            "o coliseu tem reserva obrigatoria e a F3 nao a levou para a tela")
    afirmar("cobertura_nao_lida" not in codigos,
            "todas as tres atracoes tem cobertura lida e a F3 recusou por nao lida")

    # 3b. A PRIMEIRA REGRA: atracao sem cobertura fica fora E e NOMEADA.
    sem_uma = f3.responder("roma", ("coliseu", "forum", "castelo"), 3, 2,
                           _banco_de_bancada(atracoes, [passe], coberturas[:2]),
                           esquema, constantes, hoje)
    codigos = {rec["codigo"] for rec in sem_uma["recusas"]}
    afirmar("cobertura_nao_lida" in codigos,
            "o castelo nao tem cobertura lida e a F3 nao NOMEOU isso. «Nao lida» e "
            "«nao coberta» sao coisas diferentes, e a tela que cala sobre a primeira "
            "publica a segunda sem a ter medido")
    frase = _frase_da_recusa(sem_uma, "cobertura_nao_lida")
    if frase is not None:
        afirmar("Castelo" in frase,
                "a recusa da cobertura nao lida nao nomeia a atracao: %r" % frase[:120])
        afirmar("não leu" in frase and "não cobre" in frase,
                "a recusa da cobertura nao lida tem de dizer as duas coisas — que ninguem "
                "leu e que isso NAO e o mesmo que nao cobrir: %r" % frase[:160])
    entregue = sum(Fraction(str(e["minimo"]))
                   for b in sem_uma["passes"] for e in b["entregas"])
    afirmar(entregue == 68,
            "a atracao sem cobertura lida entrou no valor entregue: deu %s e tem de dar "
            "68 (so coliseu e forum)" % entregue)

    # 3c. PASSE SEM NENHUMA COBERTURA: preco publicado e veredito NEGADO.
    nenhuma = f3.responder("roma", ("coliseu",), 3, 2,
                           _banco_de_bancada(atracoes, [passe], []), esquema,
                           constantes, hoje)
    codigos = {rec["codigo"] for rec in nenhuma["recusas"]}
    afirmar("passe_sem_cobertura_lida" in codigos,
            "passe sem nenhuma cobertura lida e a F3 nao disse por que nao ha veredito")
    afirmar("equilibrio_sobre_o_que_a_ilha_leu" not in codigos,
            "com ZERO coberturas a F3 publicou a recusa da BASE do equilibrio, que fala "
            "de uma conta que nao existe. Sao dois estados diferentes")
    versoes_sem_cobertura = [v for b in nenhuma["passes"] for v in b["versoes"]]
    afirmar(all(v["veredito"] is None for v in versoes_sem_cobertura),
            "a F3 publicou veredito sobre um passe cuja cobertura ninguem leu")
    afirmar(all(v["equilibrio"] is None for v in versoes_sem_cobertura),
            "a F3 publicou ponto de equilibrio sem nenhuma cobertura lida")
    afirmar(versoes_sem_cobertura
            and all(v["preco_do_grupo"] is not None for v in versoes_sem_cobertura),
            "a F3 escondeu o PRECO do passe: o preco foi lido e vai para a tela mesmo "
            "sem veredito")

    # 3d. O PASSE NAO E ATRACAO, e escolhe-lo como atracao e recusa dura.
    como_atracao = f3.responder("roma", ("passe-de-bancada",), 3, 2,
                                _banco_de_bancada(atracoes, [passe], coberturas),
                                esquema, constantes, hoje)
    afirmar(como_atracao["recusa_dura"]
            and como_atracao["recusa_dura"]["codigo"] == "atracao_que_e_passe",
            "o passe escolhido como atracao nao deu a recusa dura certa: %r"
            % (como_atracao["recusa_dura"],))

    # 3e. ADITIVIDADE: a soma das faixas por atracao e a faixa do conjunto.
    #     Duas contas pelo mesmo caminho nao provariam nada; esta e por outro caminho,
    #     e e ela que garante que a tela possa publicar o detalhe POR ATRACAO ao lado
    #     do total sem que os dois discordem.
    for escolha in f3.subconjuntos(["coliseu", "forum", "castelo"]):
        inteiro = f3.responder("roma", escolha, 3, 2,
                               _banco_de_bancada(atracoes, [passe], coberturas),
                               esquema, constantes, hoje)
        if inteiro["avulsos"] is None:
            # Escolha que a F3 recusa na borda nao tem soma a conferir. A guarda existe
            # para o portao RELATAR em vez de estourar: a afirmacao de 2g ja reprovou a
            # lista de subconjuntos que inclui a escolha vazia, e perder a mensagem dela
            # num traceback foi o que a bateria mediu em 22/10/2026.
            afirmar(False,
                    "a escolha %r nao produziu soma de avulsos: subconjunto que a F3 "
                    "recusa na borda nao devia estar na lista de subconjuntos" % (escolha,))
            continue
        soma_piso = Fraction(0)
        soma_teto = Fraction(0)
        for atracao_id in escolha:
            uma = f3.responder("roma", (atracao_id,), 3, 2,
                               _banco_de_bancada(atracoes, [passe], coberturas),
                               esquema, constantes, hoje)
            soma_piso += Fraction(str(uma["avulsos"]["minimo"]))
            soma_teto += Fraction(str(uma["avulsos"]["maximo"]))
        afirmar(Fraction(str(inteiro["avulsos"]["minimo"])) == soma_piso
                and Fraction(str(inteiro["avulsos"]["maximo"])) == soma_teto,
                "a soma dos avulsos de %r (%s a %s) nao e a soma das atracoes uma a uma "
                "(%s a %s)" % (escolha, inteiro["avulsos"]["minimo"],
                               inteiro["avulsos"]["maximo"], soma_piso, soma_teto))

    # 3f. A FRASE DE TODO ESTADO DO MUNDO COM PASSE passa pela regua de frase.
    for escolha in f3.subconjuntos(["coliseu", "forum", "castelo"]):
        for pessoas in (1, 2, 6):
            r2 = f3.responder("roma", escolha, 3, pessoas,
                              _banco_de_bancada(atracoes, [passe], coberturas),
                              esquema, constantes, hoje)
            for frase in _frases_de(r2):
                baixo = frase.lower()
                for palavra in p1.SEM_ACENTO_PROIBIDO:
                    afirmar(not _palavra_inteira(baixo, palavra),
                            "mundo com passe %r/%d pessoas: a frase publica %r sem "
                            "acento: %r" % (escolha, pessoas, palavra, frase[:130]))
                for proibida in p1.FRASES_PROIBIDAS:
                    afirmar(proibida not in baixo,
                            "mundo com passe: a frase traz a proibida %r: %r"
                            % (proibida, frase[:130]))
                for nome, forma in p1.FORMAS_DE_BASTIDOR:
                    achado = forma.search(frase)
                    afirmar(achado is None,
                            "mundo com passe: a frase traz bastidor da fabrica (%s: %r): "
                            "%r" % (nome, achado.group(0) if achado else "", frase[:130]))
                afirmar(" 1 atrações" not in frase and " 1 atrações" not in frase,
                        "concordancia: %r" % frase[:130])
                afirmar("das 1 " not in frase and "essas 1 " not in frase,
                        "concordancia de artigo: %r" % frase[:130])

    # ---- 4. O DOMINIO INTEIRO DO BANCO DE VERDADE
    todos = f3.estados(banco, esquema)
    afirmar(len(todos) == len(set(todos)),
            "a grade tem estado repetido: %d estados e %d distintos"
            % (len(todos), len(set(todos))))

    duras = 0
    com_avulsos = 0
    com_passe = 0
    for cidade_id, escolha, dias, pessoas in todos:
        r = f3.responder(cidade_id, escolha, dias, pessoas, banco, esquema, constantes,
                         hoje)
        onde = "%s/%s/%s dias/%s pessoas" % (cidade_id, ",".join(escolha) or "(vazia)",
                                             dias, pessoas)
        cidade = cidades.get(cidade_id)
        conhecidas = ({e.get("id"): e for e in f3.atracoes_da_cidade(banco, cidade_id)}
                      if cidade else {})
        passes_da_cidade = ({p.get("id") for p in f3.passes_da_cidade(banco, cidade_id)}
                            if cidade else set())

        fora = (not isinstance(dias, int) or dias < DIAS_DA_ESPECIFICACAO[0]
                or dias > DIAS_DA_ESPECIFICACAO[1]
                or not isinstance(pessoas, int) or pessoas < PESSOAS_DA_ESPECIFICACAO[0]
                or pessoas > PESSOAS_DA_ESPECIFICACAO[1]
                or cidade is None
                or not escolha
                or len(escolha) != len(set(escolha))
                or len(escolha) > ATRACOES_DA_ESPECIFICACAO
                or any(a not in conhecidas for a in escolha))
        if fora:
            duras += 1
            afirmar(r["recusa_dura"] is not None,
                    "%s: estado fora da faixa e a F3 NAO recusou" % onde)
            afirmar(r["avulsos"] is None and r["passes"] == [],
                    "%s: recusa dura publicou avulsos ou passe" % onde)
            afirmar(r["frase_resposta"] is None,
                    "%s: recusa dura publicou frase de resposta" % onde)
            afirmar(r["recusas"] == [],
                    "%s: recusa dura publicou recusa macia junto" % onde)
            if any(a in passes_da_cidade for a in escolha):
                afirmar(r["recusa_dura"]["codigo"] == "atracao_que_e_passe",
                        "%s: passe escolhido como atracao recusou por %r"
                        % (onde, r["recusa_dura"]["codigo"]))
            # A REGUA DE FRASE LE A RECUSA DURA TAMBEM, e nao lia ate 22/10/2026: a
            # varredura dava `continue` aqui e as sete frases de borda nunca passavam por
            # acento, frase proibida nem bastidor da fabrica. O custo era real e estava na
            # tela — duas delas ECOAVAM o id do registro («atracao-que-nao-existe» entre
            # aspas na pagina), que e bastidor pela 32.4. Recusa e texto de tela como
            # qualquer outro; a unica coisa que a borda tem de diferente e nao ter numero.
            for frase in _frases_de(r):
                baixo = frase.lower()
                for palavra in p1.SEM_ACENTO_PROIBIDO:
                    afirmar(not _palavra_inteira(baixo, palavra),
                            "%s: a recusa dura publica %r sem acento: %r"
                            % (onde, palavra, frase[:130]))
                for proibida in p1.FRASES_PROIBIDAS:
                    afirmar(proibida not in baixo,
                            "%s: a recusa dura traz a proibida %r: %r"
                            % (onde, proibida, frase[:130]))
                for nome, forma in p1.FORMAS_DE_BASTIDOR:
                    achado = forma.search(frase)
                    afirmar(achado is None,
                            "%s: a recusa dura traz bastidor da fabrica (%s: %r): %r"
                            % (onde, nome, achado.group(0) if achado else "", frase[:130]))
            continue

        afirmar(r["recusa_dura"] is None, "%s: a F3 recusou um estado valido" % onde)
        afirmar(r["frase_resposta"], "%s: estado valido sem frase de resposta" % onde)

        # 4a. A SOMA DOS AVULSOS, refeita a mao
        com_versoes = [conhecidas[a] for a in escolha
                       if any(v.get("preco") is not None
                              for v in (conhecidas[a].get("versoes") or []))]
        if com_versoes:
            com_avulsos += 1
            afirmar(r["avulsos"] is not None,
                    "%s: atracao com preco lido e sem a soma dos avulsos" % onde)
            piso = Fraction(0)
            teto = Fraction(0)
            for exp in com_versoes:
                totais = []
                for v in (exp.get("versoes") or []):
                    if v.get("preco") is None:
                        continue
                    totais.append((_total_a_mao(v.get("preco"), v.get("unidade_de_preco"),
                                                v.get("capacidade_maxima"), pessoas),
                                   v.get("id")))
                piso += min(totais)[0]
                teto += max(totais)[0]
            afirmar(Fraction(str(r["avulsos"]["minimo"])) == piso,
                    "%s: piso dos avulsos e %s e a conta a mao da %s"
                    % (onde, r["avulsos"]["minimo"], piso))
            afirmar(Fraction(str(r["avulsos"]["maximo"])) == teto,
                    "%s: teto dos avulsos e %s e a conta a mao da %s"
                    % (onde, r["avulsos"]["maximo"], teto))
            afirmar(r["avulsos"]["quantas"] == len(com_versoes),
                    "%s: a soma diz %d atracoes e a conta a mao acha %d"
                    % (onde, r["avulsos"]["quantas"], len(com_versoes)))
            afirmar(len(r["avulsos"]["detalhe"]) == len(escolha),
                    "%s: o detalhe tem %d linhas e a escolha tem %d atracoes: atracao "
                    "escolhida que nao aparece no detalhe desaparece da tela"
                    % (onde, len(r["avulsos"]["detalhe"]), len(escolha)))
        else:
            afirmar(r["avulsos"] is None,
                    "%s: nenhuma atracao com preco lido e a F3 publicou soma" % onde)

        # 4b. OS PASSES, e hoje a ausencia deles e NOMEADA
        codigos = {rec["codigo"] for rec in r["recusas"]}
        if passes_da_cidade:
            com_passe += 1
            afirmar(len(r["passes"]) == len(passes_da_cidade),
                    "%s: a cidade tem %d passes e a F3 publicou %d"
                    % (onde, len(passes_da_cidade), len(r["passes"])))
            afirmar("sem_passe_lido" not in codigos,
                    "%s: a cidade tem passe e a F3 disse que nao leu nenhum" % onde)
        else:
            afirmar(r["passes"] == [],
                    "%s: a cidade nao tem passe e a F3 publicou %d"
                    % (onde, len(r["passes"])))
            afirmar("sem_passe_lido" in codigos,
                    "%s: a cidade nao tem passe lido e a F3 NAO disse isso. Calar aqui "
                    "deixaria a pagina parecendo uma conta completa" % onde)
            # A PRIMEIRA REGRA, na direcao que ninguem procura: sem passe lido a F3 nao
            # pode dizer que a cidade NAO TEM passe. O vocabulario `forma_de_cobertura`
            # nasceu sem lastro, e a regra de crescimento de vocabulario do esquema
            # proibe frase de inexistencia enquanto for assim.
            frase = _frase_da_recusa(r, "sem_passe_lido")
            if frase is not None:
                afirmar("não leu" in frase,
                        "%s: a recusa do passe nao diz que a ILHA nao leu: %r"
                        % (onde, frase[:120]))
                for inexistencia in ("não tem passe", "nao tem passe", "não existe passe",
                                     "sem passe nenhum", "nenhum passe existe"):
                    afirmar(inexistencia not in frase.lower(),
                            "%s: a recusa do passe afirma INEXISTENCIA (%r) e o "
                            "vocabulario da cobertura nasceu sem lastro: a ilha nao pode "
                            "dizer que a cidade nao tem passe, so que nao leu nenhum"
                            % (onde, inexistencia))

        # 4c. A FRASE
        for frase in _frases_de(r):
            baixo = frase.lower()
            for palavra in p1.SEM_ACENTO_PROIBIDO:
                afirmar(not _palavra_inteira(baixo, palavra),
                        "%s: a frase publica %r sem acento: %r"
                        % (onde, palavra, frase[:130]))
            for proibida in p1.FRASES_PROIBIDAS:
                afirmar(proibida not in baixo,
                        "%s: a frase traz a proibida %r: %r" % (onde, proibida, frase[:130]))
            for nome, forma in p1.FORMAS_DE_BASTIDOR:
                achado = forma.search(frase)
                afirmar(achado is None,
                        "%s: a frase traz bastidor da fabrica (%s: %r): %r"
                        % (onde, nome, achado.group(0) if achado else "", frase[:130]))

    afirmar(duras > 0, "a grade nao tem nenhuma borda: ela e amostra com nome de grade")
    afirmar(com_avulsos > 0, "nenhum estado da grade publicou soma de avulsos")

    # ---- 5. AS SETE RECUSAS DURAS, cada uma com pelo menos um estado na grade
    duras_vistas = set()
    for cidade_id, escolha, dias, pessoas in todos:
        r = f3.responder(cidade_id, escolha, dias, pessoas, banco, esquema, constantes,
                         hoje)
        if r["recusa_dura"]:
            duras_vistas.add(r["recusa_dura"]["codigo"])
    for esperada in ("dias_fora_da_faixa", "grupo_fora_da_faixa", "cidade_desconhecida",
                     "nenhuma_atracao_escolhida", "atracao_repetida",
                     "atracao_desconhecida"):
        afirmar(esperada in duras_vistas,
                "a grade nao produz a recusa dura %r: recusa que nenhum estado alcanca "
                "e codigo que ninguem mediu" % esperada)

    # ---- 6. O VENCIMENTO DA F3 CONTRA O DO VALIDADOR, versao por versao
    validador = _validador()
    _erros, avisos, _calc = validador.validar(esquema, json.loads(json.dumps(banco)),
                                              constantes, hoje)
    vencidos_do_validador = set()
    for aviso in avisos:
        if aviso.startswith("preco vencido:"):
            vencidos_do_validador.add(aviso.split("(lido em")[0].split(":", 1)[1].strip())
    fontes = {f.get("id"): f for f in (banco.get("fontes") or [])}
    vencidos_da_f3 = set()
    for exp in (banco.get("experiencias") or []):
        for versao in (exp.get("versoes") or []):
            if not versao.get("data_leitura"):
                continue
            vencido, _p, _j = f3.f1.preco_vencido(
                esquema, fontes.get(versao.get("fonte")) or {},
                versao.get("data_leitura"), hoje)
            if vencido:
                vencidos_da_f3.add("experiencias/%s/versoes/%s"
                                   % (exp.get("id"), versao.get("id")))
    afirmar(vencidos_da_f3 == vencidos_do_validador,
            "a F3 acha %d precos vencidos e o validador acha %d, e as listas diferem em "
            "%r. Sao DUAS metades da mesma regra: a da F3 mora em `f1.preco_vencido` e "
            "vai para a TELA, a do validador e aviso de bancada. Elas discordarem quer "
            "dizer que uma das duas esta errada e nenhuma das duas sabe"
            % (len(vencidos_da_f3), len(vencidos_do_validador),
               sorted(vencidos_da_f3 ^ vencidos_do_validador)))

    # ---- 7. A TABELA PRE-RENDERIZADA
    tabela = f3.tabela_pre_renderizada(banco, esquema, constantes, hoje)
    for linha in tabela:
        afirmar(1 <= linha["quantas_atracoes"] <= ATRACOES_DA_ESPECIFICACAO,
                "linha da tabela com %d atracoes" % linha["quantas_atracoes"])
        afirmar(linha["quantas_atracoes"] == len(linha["atracoes"]),
                "linha da tabela diz %d atracoes e lista %d"
                % (linha["quantas_atracoes"], len(linha["atracoes"])))
        afirmar(linha["dias"] in f3.DIAS_DA_TABELA,
                "linha da tabela com dias fora da grade da tabela")
        afirmar(linha["pessoas"] in f3.PESSOAS_DA_TABELA,
                "linha da tabela com pessoas fora da grade da tabela")
        afirmar(linha["recusas"] or linha["vereditos"],
                "linha da tabela sem veredito E sem recusa: a ausencia do veredito e "
                "informacao, nao espaco em branco")

    # ---- 8. O ARQUIVO GRAVADO
    # A pagina vai ler dados/f3-respostas.json, entao e ele que esta afirmacao abre, e
    # nao a referencia outra vez. Sem isto o arquivo pode envelhecer em silencio
    # enquanto a referencia muda, e o portao continuaria verde.
    caminho = os.path.join(DADOS, "f3-respostas.json")
    if doc_respostas is None and not os.path.exists(caminho):
        afirmar(False, "dados/f3-respostas.json nao existe. Rode gerar-f3.py --gravar.")
    else:
        doc = doc_respostas if doc_respostas is not None else _ler("f3-respostas.json")
        afirmar(doc.get("publicar") is False,
                "f3-respostas.json com `publicar` %r. Esta ilha nao tem site: nao existe "
                "'no ar' para onde publicar." % doc.get("publicar"))
        rg = doc["resumo"]
        afirmar(rg["estados"] == len(todos),
                "f3-respostas.json diz %d estados servidos e a grade de hoje tem %d: o "
                "arquivo envelheceu e a pagina leria um dominio que nao e mais o do banco"
                % (rg["estados"], len(todos)))
        afirmar(rg["estados_gravados"] == len(doc["respostas"]),
                "f3-respostas.json diz %d estados gravados e traz %d respostas"
                % (rg["estados_gravados"], len(doc["respostas"])))
        afirmar(rg["linhas_da_tabela"] == len(doc["tabela_pre_renderizada"]),
                "f3-respostas.json diz %d linhas de tabela e traz %d"
                % (rg["linhas_da_tabela"], len(doc["tabela_pre_renderizada"])))
        afirmar(rg["linhas_da_tabela"] == len(tabela),
                "f3-respostas.json tem %d linhas de tabela e a tabela de hoje tem %d"
                % (rg["linhas_da_tabela"], len(tabela)))
        gravadas_duras = sum(1 for x in doc["respostas"] if x["recusa_dura"])
        afirmar(gravadas_duras == rg["estados_recusados_na_borda"],
                "f3-respostas.json diz %d recusas de borda e tem %d"
                % (rg["estados_recusados_na_borda"], gravadas_duras))
        afirmar(gravadas_duras == duras,
                "f3-respostas.json gravou %d bordas e a grade tem %d: borda que nao foi "
                "gravada e a metade que RECUSA sem nenhum caso no arquivo"
                % (gravadas_duras, duras))
        afirmar(rg["cidades"] == len(cidades),
                "f3-respostas.json diz %d cidades e o banco tem %d contadas"
                % (rg["cidades"], len(cidades)))
        afirmar(rg["coberturas_no_banco"] == len(banco.get("coberturas_de_passe") or []),
                "f3-respostas.json diz %d coberturas e o banco tem %d contadas"
                % (rg["coberturas_no_banco"],
                   len(banco.get("coberturas_de_passe") or [])))
        afirmar(rg["estados_com_passe_lido"] == com_passe,
                "f3-respostas.json diz %d estados com passe lido e a varredura achou %d"
                % (rg["estados_com_passe_lido"], com_passe))
        afirmar(rg["estados_com_soma_de_avulsos"] == com_avulsos,
                "f3-respostas.json diz %d estados com soma de avulsos e a varredura "
                "achou %d" % (rg["estados_com_soma_de_avulsos"], com_avulsos))
        afirmar(len(doc.get("as_tres_regras_da_cobertura") or []) == 3,
                "f3-respostas.json nao carrega as tres regras da cobertura: elas vem do "
                "esquema e sao o que esta ferramenta publica")

    resumo = {
        "estados que a F3 serve": len(todos),
        "bordas de recusa dura": duras,
        "estados com soma de avulsos": com_avulsos,
        "estados com passe lido": com_passe,
        "passes no banco": sum(1 for e in (banco.get("experiencias") or [])
                               if e.get("categoria") == "passe_de_cidade"),
        "coberturas no banco": len(banco.get("coberturas_de_passe") or []),
        "linhas da tabela": len(tabela),
        "afirmacoes": afirmacoes,
    }
    return falhas, resumo


def _frase_da_recusa(resposta, codigo):
    """A frase daquela recusa, ou None se ela nao foi publicada.

    PARECE DETALHE E NAO E. Ate 22/10/2026 este portao indexava a lista direto —
    `[rec["frase"] for rec in ... if codigo == X][0]` — e a bateria de mutacoes mediu o
    custo: CINCO quebras foram classificadas `morre` em vez de `reprova`, porque o
    portao PEGAVA o defeito na afirmacao anterior e depois estourava um IndexError antes
    de relatar. Portao que morre em vez de reprovar perde a mensagem que ele existe para
    escrever, e quem le o relatorio ve um traceback onde devia ver a frase. A regra, e
    ela vale para toda regua desta pasta: afirmar primeiro, e so entao ler o que a
    afirmacao garantiu.
    """
    for rec in resposta["recusas"]:
        if rec["codigo"] == codigo:
            return rec["frase"]
    return None


def _palavra_inteira(texto, palavra):
    """A palavra aparece INTEIRA no texto? A vizinhanca nao perdoa nem condena.

    `nao` dentro de «nação» nao e defeito, e `ate` dentro de «atenção» tambem nao:
    a secao 8 do contrato chama de errada a regua que decide por vizinhanca, e esta
    aqui decide por fronteira de palavra.
    """
    import re
    return re.search(r"(?<![0-9a-zà-ÿ])%s(?![0-9a-zà-ÿ])" % re.escape(palavra),
                     texto) is not None


def main():
    falhas, resumo = conferir()
    print("Portao da F3 — o passe da cidade")
    for chave, valor in resumo.items():
        print("  %-32s %s" % (chave + ":", valor))
    print("")
    if falhas:
        print("%d falha(s):" % len(falhas))
        for f in falhas[:40]:
            print("  - %s" % f)
        if len(falhas) > 40:
            print("  ... e %d outras" % (len(falhas) - 40))
        return 1
    print("0 falha(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
