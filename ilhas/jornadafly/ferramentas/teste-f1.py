#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Portao da F1 da JornadaFly. Reprova com codigo 1.

    python3 ferramentas/teste-f1.py

QUEM CONFERE ESCREVE A PROPRIA REGUA (secao 8 do ARQUIPELAGO.md). Este arquivo NAO
chama nenhuma funcao de conta da f1-referencia.py: ele refaz a aritmetica a mao, em
`Fraction`, a partir do banco -- para poder DISCORDAR do gerador. Chamar a conta de
quem produziu o numero faz as duas metades errarem juntas, e e a cicatriz que a
Robometria pagou em 10/09/2026 com tres travas verdes que nao mediam nada.

A FRONTEIRA, como a secao 8 a desenha. O que e DECISAO deste portao -- qual numero
a tela tem de publicar, o que basta para a resposta existir, o que e borda -- esta
escrito aqui, de novo, e CONFERIDO contra a referencia: divergencia aqui ensina. O
que e FATO EXTERNO -- o preco de cada versao, a capacidade, a unidade, o eixo, a
data de leitura -- e lido do BANCO, de um lugar so: ninguem redescobre fato externo
de forma independente, e a segunda escrita dele nao conferiria nada.

A GRADE PISA NA BORDA, sempre. Os estados medidos vao de 0 a 13 pessoas: 0 e 13 sao
as duas recusas duras, 1 e 12 sao os extremos que TEM de responder, e a capacidade
de cada versao com unidade de veiculo e medida exatamente nela e em capacidade + 1 --
que e onde `ceil` se separa de `floor + 1`. Grade que nao pisa na borda e amostra com
nome de grade.

E ELE MEDE ACENTO EM TODA FRASE DE TODO ESTADO, e isso nao e zelo: a PRIMEIRA versao
da f1-referencia.py, escrita em 22/10/2026, publicava "O preco e por veiculo, nao
por pessoa" -- portugues sem acento na frase-resposta, que e a cicatriz da
Robometria cometida dentro da ferramenta que existe para nao a cometer. O defeito
foi achado por leitura, e e justamente por isso que ele virou portao: leitura nao
roda na proxima passada.
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

# ---------------------------------------------------------------------------
# AS DECISOES DESTE PORTAO, escritas de novo de proposito
# ---------------------------------------------------------------------------

# A faixa de grupo. Escrita aqui, conferida contra a referencia: se as duas
# discordarem, uma das duas esta errada e a divergencia e informacao.
PESSOAS_MINIMO = 1
PESSOAS_MAXIMO = 12
IOF_ESPERADO = Fraction(35, 10)       # 3,5% -- o Decreto 12.499/2025

# As pessoas da tabela pre-renderizada. O 6 e obrigatorio: e onde o degrau de
# capacidade aparece.
PESSOAS_DA_TABELA = (1, 2, 4, 6)

# Palavra portuguesa que a tela NUNCA pode publicar sem acento. Cada uma delas e a
# forma SEM acento de uma palavra que a resposta usa; encontrar qualquer uma em
# palavra inteira e reprovacao. A lista cobre o que a F1 escreve, nao o portugues
# inteiro -- regua que tentasse cobrir o idioma reprovaria nome proprio e ficaria
# desligada por inutil.
SEM_ACENTO_PROIBIDO = (
    "nao", "preco", "precos", "versao", "versoes", "experiencia", "experiencias",
    "numero", "numeros", "voce", "comissao", "pagina", "paginas", "portugues",
    "equilibrio", "horario", "veiculo", "cambio", "cartao", "negociacao",
    "criancas", "crianca", "duracao", "razao", "proprio", "propria", "orgao",
    "e de outro", "ninguem", "alem", "apos", "ate", "tres", "seculo", "marcacao",
    "variacao", "declaracao", "informacao", "tarifa oficial de",
)

# Frase que nenhuma pagina desta fabrica pode servir. As duas primeiras vem da
# secao 7 e da 32.4 do ARQUIPELAGO.md; o resto vem da lista "Proibidas" do VOZ.md
# desta ilha. A regra da secao 8 sobre perdoar por vizinhanca vale: a conferencia e
# por FRASE inteira, nunca por palavra solta.
FRASES_PROIBIDAS = (
    "link de loja em breve",
    "egresso da nuvem", "serp classificada", "snippet", "busca restrita ao dominio",
    "lista de reconferencia",
    "imperdivel", "imperdível", "destino dos sonhos", "experiencia transformadora",
    "experiência transformadora", "lugar magico", "lugar mágico", "paraiso na terra",
    "paraíso na terra", "ultimas vagas", "últimas vagas", "quando eu fui",
    "consulta parametrica", "consulta paramétrica",
    "dado verificavel na fonte primaria", "dado verificável na fonte primária",
    "conforme publicado pelo operador",
)

# A unidade que NAO multiplica por pessoa. Escrita de novo: e decisao de qual conta
# a tela publica.
UNIDADES_COM_CAPACIDADE = ("por_veiculo", "por_cabine", "por_grupo")

# TEXTO DE BASTIDOR DA FABRICA (secao 32.4 do ARQUIPELAGO.md). Nao e uma lista de
# frases: e uma lista de FORMAS, porque o bastidor nao chega a pagina como uma frase
# conhecida -- ele chega como nome de campo dentro de um `motivo_*` do banco, como id
# de constante dentro de uma recusa, como caminho de arquivo numa prestacao de
# contas. Foi assim que a primeira versao desta ferramenta publicou
# `unidade_de_preco` e `cambio-eur-brl` na tela, e a regua de acento foi quem viu.
# A mesma cicatriz que a ohmetria pagou com `dados/modulos.json` na pagina.
FORMAS_DE_BASTIDOR = (
    ("acento grave de codigo", re.compile(r"`")),
    ("nome de campo em minusculas com sublinhado",
     re.compile(r"(?<![0-9a-zA-Z_])[a-z][a-z0-9]*_[a-z0-9_]+(?![0-9a-zA-Z_])")),
    ("caminho de arquivo do repositorio",
     re.compile(r"\b(?:dados|ferramentas|ilhas)/|\.(?:json|py|md|php)\b")),
    ("id de constante ou de registro",
     re.compile(r"(?<![0-9a-zA-Z])[a-z][a-z0-9]*(?:-[a-z0-9]+){2,}(?![0-9a-zA-Z])")),
    ("numero de secao do contrato",
     re.compile(r"\b(?:se[cç][aã]o|ARQUIPELAGO|VOZ\.md|DESIGN\.md|25\.2|32\.4)\b",
                re.IGNORECASE)),
)


def _ler(nome):
    with io.open(os.path.join(DADOS, nome), encoding="utf-8") as f:
        return json.load(f)


def _referencia():
    caminho = os.path.join(AQUI, "f1-referencia.py")
    spec = importlib.util.spec_from_file_location("f1_referencia", caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


# ---------------------------------------------------------------------------
# A ARITMETICA, REESCRITA A MAO
# ---------------------------------------------------------------------------

def _total_a_mao(preco, unidade, capacidade, pessoas):
    """O total do grupo, em Fraction, sem olhar a referencia.

    O `ceil` esta escrito como divisao inteira com arredondamento para cima
    (`-(-a // b)`), e nao com math.ceil sobre float: a forma e DIFERENTE da que a
    referencia usa, de proposito. Duas escritas da mesma conta que discordam numa
    borda e exatamente o que este portao existe para achar.
    """
    p = Fraction(str(preco))
    if unidade == "por_pessoa":
        return p * pessoas, 1
    unidades = -(-pessoas // capacidade)
    return p * unidades, unidades


def _centavo_a_mao(valor):
    """Arredonda para centavo, meio para CIMA, em aritmetica exata.

    Escrito sem Decimal de proposito: a referencia usa Decimal com
    ROUND_HALF_UP, e aqui a mesma regra sai de Fraction. Se as duas discordarem
    num centavo, uma delas esta errada.
    """
    centavos = valor * 100
    inteiro = centavos.numerator // centavos.denominator
    resto = centavos - inteiro
    if resto >= Fraction(1, 2):
        inteiro += 1
    return Fraction(inteiro, 100)


def _equilibrio_a_mao(eixo, degraus):
    """O ponto de equilibrio, reescrito a mao. Devolve {id_da_versao: dias|None}.

    Esta versao percorre os dias DE CIMA PARA BAIXO e guarda o menor que satisfaz,
    em vez de parar no primeiro de baixo para cima: mesma resposta por outro
    caminho, que e o que separa uma segunda conta de uma copia.
    """
    if eixo != "por_quantidade":
        return None
    if len(degraus) < 2:
        return None
    if any(d["preco"] is None or not isinstance(d["dias_de_uso"], int) for d in degraus):
        return None
    base = sorted(degraus, key=lambda d: (d["dias_de_uso"], Fraction(str(d["preco"]))))[0]
    saida = {}
    for d in degraus:
        if d["id"] == base["id"]:
            continue
        if d["dias_de_uso"] == base["dias_de_uso"]:
            saida[d["id"]] = None
            continue
        menor = None
        for dias in range(d["dias_de_uso"], 0, -1):
            copias = -(-dias // base["dias_de_uso"])
            if copias * Fraction(str(base["preco"])) >= Fraction(str(d["preco"])):
                menor = dias
        saida[d["id"]] = menor
    return saida


def _numero_na_frase(valor, moeda):
    """Como o numero tem de aparecer escrito na frase. Decisao deste portao."""
    simbolo = {"EUR": "€", "USD": "US$ ", "BRL_do_operador": "R$ "}[moeda]
    centavos = _centavo_a_mao(valor)
    inteiro = centavos.numerator // centavos.denominator
    sobra = centavos - inteiro
    milhar = "{:,}".format(inteiro).replace(",", ".")
    if sobra == 0:
        return simbolo + milhar
    return simbolo + milhar + "," + "%02d" % int(sobra * 100)


# ---------------------------------------------------------------------------
# A BATERIA
# ---------------------------------------------------------------------------

def _frases_de(resposta):
    """Toda frase que a resposta manda para a tela, achatada.

    Afirmacao sobre o que a pagina diz se mede no CORPO (secao 8) -- aqui, no
    conjunto das frases de tela, nunca no JSON inteiro: o JSON carrega codigo de
    recusa, id de versao e nome de campo, que nao sao texto de tela e reprovariam
    por acento sem nenhum defeito embaixo.
    """
    frases = []
    if resposta["recusa_dura"]:
        frases.append(resposta["recusa_dura"]["frase"])
        return frases
    frases.append(resposta["frase_resposta"])
    frases.append(resposta["cartao_brasileiro"])
    frases.append(resposta["inclui"]["frase"])
    frases.append(resposta["nao_inclui"]["frase"])
    if resposta["escada"]["motivo"]:
        frases.append(resposta["escada"]["motivo"])
    for l in resposta["escada"]["linhas"]:
        frases.append(l["frase"])
    frases.append(resposta["bloco_de_compra"]["aviso"])
    frases.append(resposta["bloco_de_compra"]["o_que_e"])
    for l in resposta["prestacao_de_contas"]["linhas"]:
        frases.append(l["frase"])
    frases.extend(resposta["faixa_etaria"]["frases"])
    for r in resposta["recusas"]:
        frases.append(r["frase"])
    for d in resposta["como_sabemos"]["divergentes"]:
        frases.append(d["frase"])
    return [f for f in frases if f]


def conferir(f1=None, banco=None, esquema=None, constantes=None, doc_respostas=None):
    """O portao inteiro sobre dicionarios EM MEMORIA. Devolve (falhas, resumo).

    E assim que ferramentas/mutacoes-f1.py produz os mundos que o banco ainda nao
    tem e quebra a propria referencia para ver o portao reprovar. Sem esta porta, a
    bateria de mutacoes teria de gravar arquivo em disco para medir -- e bancada que
    escreve no banco de verdade e a unica coisa que esta ilha considera imperdoavel.
    """
    f1 = f1 if f1 is not None else _referencia()
    banco = banco if banco is not None else _ler("experiencias.json")
    esquema = esquema if esquema is not None else _ler("esquema-banco.json")
    constantes = constantes if constantes is not None else _ler("constantes.json")

    falhas = []
    afirmacoes = [0]

    def afirma(ok, msg):
        afirmacoes[0] += 1
        if not ok:
            falhas.append(msg)

    # ---------------------------------------------------------------- 1. fronteiras
    afirma(f1.PESSOAS_MINIMO == PESSOAS_MINIMO and f1.PESSOAS_MAXIMO == PESSOAS_MAXIMO,
           "a faixa de grupo da referencia (%s a %s) discorda da deste portao (%s a %s)"
           % (f1.PESSOAS_MINIMO, f1.PESSOAS_MAXIMO, PESSOAS_MINIMO, PESSOAS_MAXIMO))
    afirma(tuple(f1.PESSOAS_DA_TABELA) == PESSOAS_DA_TABELA,
           "as pessoas da tabela da referencia %r discordam das deste portao %r"
           % (tuple(f1.PESSOAS_DA_TABELA), PESSOAS_DA_TABELA))
    iof = f1.iof_publicavel(constantes)
    afirma(Fraction(str(iof["valor"])) == IOF_ESPERADO,
           "o IOF do arquivo de constantes e %r e este portao espera 3,5%%" % iof["valor"])
    afirma(not f1.conferir_moedas_do_vocabulario(esquema),
           "moeda do vocabulario sem forma de escrita: %r"
           % f1.conferir_moedas_do_vocabulario(esquema))
    afirma(not f1.conferir_unidades_do_vocabulario(esquema),
           "unidade do vocabulario sem conta ou sem rotulo: %r"
           % f1.conferir_unidades_do_vocabulario(esquema))

    # -------------------------------------------- 2. VARRE A ENTRADA INTEIRA
    # "O corpo" de uma ferramenta de entrada variavel e o corpo de TODAS as
    # respostas dela (secao 8). Nenhuma amostra: todo estado, com as bordas.
    palavra_sem_acento = [(p, re.compile(r"(?<![0-9a-zà-ÿ])%s(?![0-9a-zà-ÿ])" % re.escape(p)))
                          for p in SEM_ACENTO_PROIBIDO]

    estados_medidos = 0
    for exp in banco["experiencias"]:
        eixo = exp.get("eixo_das_versoes")
        degraus = [{"id": v["id"], "rotulo": v["rotulo"], "preco": v.get("preco"),
                    "dias_de_uso": v.get("dias_de_uso")} for v in exp["versoes"]]
        equilibrio = _equilibrio_a_mao(eixo, degraus)
        ids_do_banco = [v["id"] for v in exp["versoes"]]

        for versao in exp["versoes"]:
            unidade = versao["unidade_de_preco"]
            capacidade = versao.get("capacidade_maxima")
            moeda = versao["moeda"]

            # A grade pisa na borda da CAPACIDADE, nao so na do grupo.
            pessoas_a_medir = set(range(0, PESSOAS_MAXIMO + 2))
            if unidade in UNIDADES_COM_CAPACIDADE and capacidade:
                pessoas_a_medir.add(capacidade)
                pessoas_a_medir.add(capacidade + 1)
                pessoas_a_medir.add(capacidade * 2)
            for pessoas in sorted(p for p in pessoas_a_medir if 0 <= p <= PESSOAS_MAXIMO + 1):
                estados_medidos += 1
                onde = "%s/%s/%d pessoas" % (exp["id"], versao["id"], pessoas)
                r = f1.responder(exp["id"], versao["id"], pessoas, banco, esquema, constantes)

                # --- 2a. a BORDA do grupo
                if pessoas < PESSOAS_MINIMO or pessoas > PESSOAS_MAXIMO:
                    afirma(r["recusa_dura"] is not None
                           and r["recusa_dura"]["codigo"] == "grupo_fora_da_faixa",
                           "%s: deveria recusar por grupo fora da faixa e nao recusou" % onde)
                    afirma(r["contas"] is None,
                           "%s: recusou e mesmo assim publicou conta" % onde)
                else:
                    afirma(r["recusa_dura"] is None,
                           "%s: recusou dentro da faixa que tem de responder (%r)"
                           % (onde, r["recusa_dura"]))

                for frase in _frases_de(r):
                    baixo = frase.lower()
                    for palavra, padrao in palavra_sem_acento:
                        afirma(not padrao.search(baixo),
                               "%s: a tela publica %r sem acento em: %s"
                               % (onde, palavra, frase[:110]))
                    for proibida in FRASES_PROIBIDAS:
                        afirma(proibida not in baixo,
                               "%s: frase proibida %r na tela: %s"
                               % (onde, proibida, frase[:110]))
                    for nome_da_forma, padrao in FORMAS_DE_BASTIDOR:
                        achado = padrao.search(frase)
                        afirma(achado is None,
                               "%s: texto de bastidor da fabrica na tela (%s: %r) em: %s"
                               % (onde, nome_da_forma,
                                  achado.group(0) if achado else "", frase[:110]))

                if r["recusa_dura"] is not None:
                    continue

                # --- 2b. AS QUATRO CONTAS, refeitas a mao
                total, unidades = _total_a_mao(versao["preco"], unidade, capacidade, pessoas)
                por_pessoa = _centavo_a_mao(total / pessoas)
                total_iof = total * (1 + IOF_ESPERADO / 100)
                por_pessoa_iof = _centavo_a_mao(total_iof / pessoas)

                c = r["contas"]
                afirma(Fraction(c["total"]) == total,
                       "%s: total %s e a conta a mao da %s" % (onde, c["total"], total))
                afirma(Fraction(c["por_pessoa"]) == por_pessoa,
                       "%s: por pessoa %s e a conta a mao da %s"
                       % (onde, c["por_pessoa"], por_pessoa))
                afirma(c["unidades_necessarias"] == unidades,
                       "%s: %r unidades e a conta a mao da %r"
                       % (onde, c["unidades_necessarias"], unidades))
                afirma(Fraction(c["total_com_iof"]) == _centavo_a_mao(total_iof),
                       "%s: total com IOF %s e a conta a mao da %s"
                       % (onde, c["total_com_iof"], _centavo_a_mao(total_iof)))

                # --- 2c. O NUMERO DA CONTA E O NUMERO DA FRASE sao o mesmo
                # (secao 8: afirmacao sobre o que a pagina diz se mede no corpo).
                esperado_total = _numero_na_frase(total, moeda)
                esperado_pessoa = _numero_na_frase(por_pessoa, moeda)
                afirma(esperado_total in r["frase_resposta"],
                       "%s: a frase-resposta nao publica o total %s: %s"
                       % (onde, esperado_total, r["frase_resposta"][:130]))
                afirma(esperado_pessoa in r["frase_resposta"],
                       "%s: a frase-resposta nao publica o por pessoa %s: %s"
                       % (onde, esperado_pessoa, r["frase_resposta"][:130]))
                afirma(_numero_na_frase(total_iof, moeda) in r["cartao_brasileiro"],
                       "%s: a linha do cartao nao publica %s: %s"
                       % (onde, _numero_na_frase(total_iof, moeda), r["cartao_brasileiro"]))
                afirma(_numero_na_frase(por_pessoa_iof, moeda) in r["cartao_brasileiro"],
                       "%s: a linha do cartao nao publica o por pessoa com IOF %s"
                       % (onde, _numero_na_frase(por_pessoa_iof, moeda)))

                # --- 2d. A DATA DE LEITURA e obrigatoria na tela. Preco cravado como
                # atual sem a data e, pelo VOZ.md, o defeito mais grave desta ilha.
                iso = versao["data_leitura"]
                data_br = "%s/%s/%s" % (iso[8:10], iso[5:7], iso[0:4])
                afirma(data_br in r["frase_resposta"],
                       "%s: a frase-resposta publica preco SEM a data de leitura (%s)"
                       % (onde, data_br))

                # --- 2e. PRESTACAO DE CONTAS: cada versao do banco uma vez, e a soma
                # fecha contra o tamanho CONTADO do banco (nunca um numero digitado).
                pc = r["prestacao_de_contas"]
                nomeadas = [l["versao"] for l in pc["linhas"]]
                afirma(sorted(nomeadas) == sorted(ids_do_banco),
                       "%s: a prestacao de contas nomeia %r e o banco tem %r"
                       % (onde, sorted(nomeadas), sorted(ids_do_banco)))
                afirma(len(nomeadas) == len(set(nomeadas)),
                       "%s: versao nomeada mais de uma vez: %r" % (onde, nomeadas))
                afirma(pc["versoes_nomeadas"] == len(ids_do_banco)
                       and pc["versoes_no_banco"] == len(ids_do_banco),
                       "%s: a contagem da prestacao de contas (%r/%r) nao bate com as %d "
                       "versoes contadas no banco"
                       % (onde, pc["versoes_nomeadas"], pc["versoes_no_banco"],
                          len(ids_do_banco)))
                afirma(sum(1 for l in pc["linhas"] if l["escolhida"]) == 1,
                       "%s: a prestacao de contas marca %d versoes como escolhidas"
                       % (onde, sum(1 for l in pc["linhas"] if l["escolhida"])))

                # --- 2f. A CONTA 3
                e = r["escada"]
                if equilibrio is None:
                    afirma(not e["aplicavel"],
                           "%s: a referencia calculou escada onde a conta a mao diz que "
                           "nao ha (eixo %r, %d versoes)" % (onde, eixo, len(degraus)))
                    afirma(bool(e["motivo"]),
                           "%s: escada nao aplicavel e sem motivo para a tela" % onde)
                    afirma(not e["linhas"],
                           "%s: escada nao aplicavel com linhas dentro" % onde)
                else:
                    afirma(e["aplicavel"],
                           "%s: a conta a mao acha escada e a referencia nao" % onde)
                    por_id = dict((l["para"], l["a_partir_de"]) for l in e["linhas"])
                    afirma(por_id == equilibrio,
                           "%s: a escada da referencia %r discorda da conta a mao %r"
                           % (onde, por_id, equilibrio))

                # --- 2g. O PISO DE COMPRA e DERIVADO, e link cru nao e patrocinado
                b = r["bloco_de_compra"]
                cidade = [c2 for c2 in banco["cidades"]
                          if c2["id"] == exp["cidade"]][0]
                derivado = esquema["piso_de_compra"]["molde"].replace(
                    "{slug_plataforma}", cidade["slug_plataforma"])
                esperada = (exp.get("afiliado") or {}).get("url_produto") or derivado
                afirma(b["url"] == esperada,
                       "%s: o bloco de compra aponta %r e a derivacao da %r"
                       % (onde, b["url"], esperada))
                afirma(b["url"],
                       "%s: item sem saida de compra. Pela 25.2 e erro duro." % onde)
                if not (exp.get("afiliado") or {}).get("programa"):
                    afirma("sponsored" not in b["rel"],
                           "%s: link CRU saindo com rel %r. `sponsored` declara relacao "
                           "paga e ninguem esta pagando por este clique." % (onde, b["rel"]))

                # --- 2h. NENHUM VALOR EM REAL, em nenhuma frase. As constantes de
                # cambio estao pendentes, e constante pendente nao entra em formula
                # publicada (secao 10).
                for frase in _frases_de(r):
                    afirma("R$" not in frase,
                           "%s: a tela publica valor em real com o cambio pendente: %s"
                           % (onde, frase[:110]))

                # --- 2i. recusa de resposta UNICA aparece no maximo uma vez
                unicas = ("sem_valor_em_real", "sem_temporada", "sem_faixa_etaria",
                          "registro_pendente_de_releitura", "grupo_fora_da_faixa")
                for codigo in unicas:
                    quantas = sum(1 for x in r["recusas"] if x["codigo"] == codigo)
                    afirma(quantas <= 1,
                           "%s: a recusa %r aparece %d vezes na mesma resposta"
                           % (onde, codigo, quantas))

    # ------------------------------------------------- 3. O DEGRAU DE CAPACIDADE
    # A afirmacao que separa esta ferramenta das sete paginas medidas em
    # 14/09/2026: em capacidade + 1 pessoa o total DOBRA, e nenhuma delas publica
    # esse numero.
    degraus_medidos = 0
    for exp in banco["experiencias"]:
        for versao in exp["versoes"]:
            cap = versao.get("capacidade_maxima")
            if versao["unidade_de_preco"] not in UNIDADES_COM_CAPACIDADE or not cap:
                continue
            if cap + 1 > PESSOAS_MAXIMO:
                continue
            degraus_medidos += 1
            na_capacidade = f1.responder(exp["id"], versao["id"], cap, banco, esquema,
                                         constantes)["contas"]
            depois = f1.responder(exp["id"], versao["id"], cap + 1, banco, esquema,
                                  constantes)["contas"]
            afirma(Fraction(depois["total"]) == Fraction(na_capacidade["total"]) * 2,
                   "%s/%s: com %d pessoas o total e %s e com %d e %s — o degrau de "
                   "capacidade nao dobrou"
                   % (exp["id"], versao["id"], cap, na_capacidade["total"],
                      cap + 1, depois["total"]))

    afirma(degraus_medidos > 0,
           "nenhuma versao com unidade de veiculo/cabine/grupo foi medida no degrau. A "
           "afirmacao do degrau ficaria verde sem medir nada — e e ela que separa esta "
           "ferramenta das paginas que a ilha mediu.")

    # ------------------------------------------------- 4. A TABELA PRE-RENDERIZADA
    tabela = f1.tabela_pre_renderizada(banco, esquema, constantes)
    versoes_no_banco = sum(len(e["versoes"]) for e in banco["experiencias"])
    afirma(len(tabela) == versoes_no_banco * len(PESSOAS_DA_TABELA),
           "a tabela tem %d linhas e as %d versoes contadas no banco x %d numeros de "
           "pessoas dao %d" % (len(tabela), versoes_no_banco, len(PESSOAS_DA_TABELA),
                               versoes_no_banco * len(PESSOAS_DA_TABELA)))
    afirma(sum(1 for l in tabela if l["pessoas"] == 6) == versoes_no_banco,
           "a tabela nao traz a linha de 6 pessoas para todas as %d versoes. O 6 e "
           "obrigatorio: e onde o degrau de capacidade aparece, e tabela que para em 4 "
           "esconde exatamente o que esta ferramenta tem de diferente." % versoes_no_banco)
    for linha in tabela:
        afirma(bool(linha["lido_em"]),
               "linha da tabela sem data de leitura: %r" % (linha,))
        afirma("R$" not in linha["total"] and "R$" not in linha["com_iof"],
               "linha da tabela com valor em real: %r" % (linha,))

    # A tabela e refeita a mao, linha por linha, a partir do banco.
    por_rotulo = {}
    for exp in banco["experiencias"]:
        for v in exp["versoes"]:
            por_rotulo[(exp["nome"], v["rotulo"])] = (exp, v)
    for linha in tabela:
        chave = (linha["experiencia"], linha["versao"])
        afirma(chave in por_rotulo, "linha da tabela sem versao no banco: %r" % (chave,))
        if chave not in por_rotulo:
            continue
        _exp, v = por_rotulo[chave]
        total, unidades = _total_a_mao(v["preco"], v["unidade_de_preco"],
                                       v.get("capacidade_maxima"), linha["pessoas"])
        afirma(linha["total"] == _numero_na_frase(total, v["moeda"]),
               "tabela %r: total %r e a conta a mao da %r"
               % (chave + (linha["pessoas"],), linha["total"],
                  _numero_na_frase(total, v["moeda"])))
        afirma(linha["unidades_necessarias"] == unidades,
               "tabela %r: %r unidades e a conta a mao da %r"
               % (chave, linha["unidades_necessarias"], unidades))

    # ------------------------------------------------- 5. O ARQUIVO GRAVADO
    # Para cada campo publicado, a bancada le a MESMA fonte que a pagina vai ler
    # (secao 8, Aquametria 11/09). A pagina vai ler dados/f1-respostas.json, entao e
    # ele que esta afirmacao abre — nao a referencia outra vez.
    caminho = os.path.join(DADOS, "f1-respostas.json")
    if doc_respostas is None and not os.path.exists(caminho):
        afirma(False, "dados/f1-respostas.json nao existe. Rode gerar-f1.py --gravar.")
    else:
        doc = doc_respostas if doc_respostas is not None else _ler("f1-respostas.json")
        afirma(doc.get("publicar") is False,
               "f1-respostas.json com `publicar` %r. Esta ilha nao tem site: nao existe "
               "'no ar' para onde publicar." % doc.get("publicar"))
        r = doc["resumo"]
        afirma(r["versoes"] == versoes_no_banco,
               "f1-respostas.json diz %d versoes e o banco tem %d contadas"
               % (r["versoes"], versoes_no_banco))
        afirma(r["estados"] == len(doc["respostas"]),
               "f1-respostas.json diz %d estados e traz %d respostas"
               % (r["estados"], len(doc["respostas"])))
        afirma(r["linhas_da_tabela"] == len(doc["tabela_pre_renderizada"]),
               "f1-respostas.json diz %d linhas de tabela e traz %d"
               % (r["linhas_da_tabela"], len(doc["tabela_pre_renderizada"])))
        afirma(r["estados_recusados_na_borda"] > 0,
               "f1-respostas.json nao gravou nenhum estado de borda. A metade que "
               "RECUSA ficaria sem um caso gravado.")
        duras = sum(1 for x in doc["respostas"] if x["recusa_dura"])
        afirma(duras == r["estados_recusados_na_borda"],
               "f1-respostas.json diz %d recusas de borda e tem %d"
               % (r["estados_recusados_na_borda"], duras))

    return falhas, {
        "estados_medidos": estados_medidos,
        "degraus_de_capacidade_medidos": degraus_medidos,
        "linhas_de_tabela": len(tabela),
        "afirmacoes": afirmacoes[0],
    }


def main():
    falhas, resumo = conferir()
    print("Portao da F1 da JornadaFly")
    print("  estados medidos (com as bordas):  %d" % resumo["estados_medidos"])
    print("  degraus de capacidade medidos:    %d" % resumo["degraus_de_capacidade_medidos"])
    print("  linhas de tabela refeitas a mao:  %d" % resumo["linhas_de_tabela"])
    print("  afirmacoes:                       %d" % resumo["afirmacoes"])
    if falhas:
        print("\nREPROVADO — %d falha(s):" % len(falhas))
        for f in falhas[:40]:
            print("  - %s" % f)
        if len(falhas) > 40:
            print("  ... e %d outras" % (len(falhas) - 40))
        sys.exit(1)
    print("\n0 falha(s).")


if __name__ == "__main__":
    main()
