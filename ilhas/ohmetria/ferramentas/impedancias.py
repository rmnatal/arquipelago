#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enumera as impedancias alcancaveis por ligacao SIMETRICA de alto-falantes.

Parte da ESPECIFICACAO da F1 (bloco 2), nao da F1. O que este arquivo prova e
uma coisa so, e e a coisa que a especificacao nao pode afirmar em prosa: o
dominio de saida da F1 e ENUMERAVEL, e portanto a resposta "nao fecha" e
calculavel em vez de opinada.

O modelo, escrito por extenso para quem reler:

  - A entrada e (quantidade de alto-falantes N, bobinas por alto-falante C,
    impedancia de cada bobina Z). Um falante "2+2 ohms" e C=2, Z=2.
  - O total de bobinas e K = N * C. Elas sao todas iguais.
  - Uma ligacao SIMETRICA e: parta as K bobinas em g grupos IGUAIS de K/g
    bobinas, em serie dentro do grupo, e ligue os g grupos em paralelo.
    Portanto g tem de DIVIDIR K, e a impedancia final e
        Z_final = Z * (K / g) / g = Z * K / g^2
  - g = 1 e "tudo em serie". g = K e "tudo em paralelo". Os divisores do meio
    sao as serie-paralelo.

POR QUE SO SIMETRICA, e isto e recusa declarada, nao limitacao esquecida:
ligacao assimetrica (tres bobinas em paralelo mais uma, por exemplo) existe e
fecha valores intermediarios, mas as bobinas passam a receber potencia
DIFERENTE uma da outra. A ilha nao recomenda o que distribui potencia desigual
entre bobinas identicas, e a F1 diz isso na tela em vez de ficar calada.

A regra de bolso que a SERP publica -- "impedancia dividida pelo numero de
alto-falantes" -- e o caso g = K visto de longe. Ela produz UM valor e some com
os outros, e e exatamente por isso que ela responde 0,5 ohm para o par de subs
2+2 e nunca avisa que 1 ohm nao esta no conjunto.

Uso:
    python3 ferramentas/impedancias.py                # grava o JSON do banco de casos
    python3 ferramentas/impedancias.py --conferir     # regua propria, so afirma e sai
"""

import io
import json
import os
import sys
from fractions import Fraction

# ---------------------------------------------------------------------------
# AS DUAS LISTAS DESTE GERADOR MORAM NO ESQUEMA, NAO AQUI (bloco 3, 14/09/2026).
#
# Ate o bloco 3 elas eram literais deste arquivo, e a de impedancia de modulo
# vinha com um comentario dizendo que era "o conjunto de valores que o mercado de
# modulos oferece". Isso era uma afirmacao sobre o MERCADO, digitada a mao, contra
# a qual nenhum registro de banco podia falar -- e o campo que ela alimentava se
# chamava "alcancavel_mas_sem_modulo_no_mercado", quer dizer: a F1 ia publicar
# "nao existe modulo para 0,125 ohm" com base numa lista que alguem escreveu.
# E a familia da secao 8 do ARQUIPELAGO.md: numero de tela nasce CONTADO, nunca
# digitado, e regua escrita para um mundo que nunca aconteceu nasce sem poder falhar.
#
# Agora as duas saem de dados/esquema-banco.json (secao 26.2: a lista mora no
# esquema, nunca dentro da regua) e ferramentas/validar-banco.py cobra os dois
# sentidos entre a lista e o banco. Enquanto o banco estiver vazio, a unica frase
# verdadeira e "nenhum modulo do nosso banco" -- e e por isso que o campo mudou de
# nome. Se a chave sumir do esquema, este gerador MORRE em vez de cair num literal.
# ---------------------------------------------------------------------------

AQUI = os.path.dirname(os.path.abspath(__file__))
ESQUEMA = os.path.join(os.path.dirname(AQUI), "dados", "esquema-banco.json")


def _vocabulario(nome):
    esquema = json.load(io.open(ESQUEMA, encoding="utf-8"))
    valores = esquema.get("vocabularios", {}).get(nome, {}).get("valores")
    if not valores:
        raise SystemExit(
            "esquema-banco.json nao tem o vocabulario %s, ou ele esta vazio.\n"
            "Este gerador NAO tem copia dessa lista de proposito: uma copia envelheceria "
            "calada e a F1 voltaria a afirmar sobre o mercado a partir de um literal." % nome)
    return valores


def _rotulo(token):
    """'1' -> '1 ohm'; '2' -> '2 ohms'; '2+2' -> '2+2 ohms'."""
    return "%s ohm%s" % (token, "" if token == "1" else "s")


def _bobinas_do_esquema():
    """(rotulo, bobinas por falante, impedancia de cada bobina), lido do vocabulario."""
    saida = []
    for token in _vocabulario("impedancia_de_bobina"):
        partes = token.split("+")
        saida.append((_rotulo(token), len(partes), Fraction(partes[0])))
    return saida


def _impedancias_de_modulo_do_esquema():
    saida = []
    for token in _vocabulario("impedancia_de_modulo"):
        inteiro, _, decimal = token.partition(",")
        if decimal:
            saida.append(Fraction(int(inteiro + decimal), 10 ** len(decimal)))
        else:
            saida.append(Fraction(int(inteiro)))
    return sorted(saida)


# Entradas que a F1 declara aceitar, pela especificacao (dados/especificacao-calculadoras.md)
# e pelo vocabulario impedancia_de_bobina do esquema.
BOBINAS = _bobinas_do_esquema()

# Quantidade de alto-falantes que a F1 aceita. Acima de 4 a instalacao vira
# projeto e nao cabe numa resposta de duas linhas -- teto declarado, nao omissao.
# Esta continua aqui porque e recusa de PRODUTO desta ferramenta, nao vocabulario
# de banco: nenhum registro de banco pode contradize-la.
QUANTIDADES = [1, 2, 3, 4]

# O conjunto contra o qual a F1 decide "fecha" ou "nao fecha". EXPECTATIVA declarada
# no esquema, cobrada nos dois sentidos contra o banco pelo validador.
IMPEDANCIAS_DE_MODULO = _impedancias_de_modulo_do_esquema()

TOLERANCIA = Fraction(0)  # "fecha" e igualdade exata. Nao existe quase-fecha.


def divisores(n):
    return [g for g in range(1, n + 1) if n % g == 0]


def alcancaveis(n_falantes, bobinas_por_falante, z_bobina):
    """Devolve {impedancia final: descricao da ligacao}, ordenado do menor ao maior."""
    k = n_falantes * bobinas_por_falante
    saida = {}
    for g in divisores(k):
        por_grupo = k // g
        z = z_bobina * Fraction(por_grupo, 1) / Fraction(g, 1)
        if g == 1:
            como = "todas as %d bobinas em serie" % k
        elif g == k:
            como = "todas as %d bobinas em paralelo" % k
        else:
            como = "%d grupos de %d bobinas em serie, os grupos em paralelo" % (g, por_grupo)
        # Duas ligacoes diferentes podem dar a mesma impedancia; guarda a primeira
        # e registra a segunda, porque a F1 mostra o caminho e nao so o numero.
        if z in saida:
            saida[z] = saida[z] + " (ou: %s)" % como
        else:
            saida[z] = como
    return dict(sorted(saida.items()))


def fmt(z):
    if z.denominator == 1:
        return str(z.numerator)
    return ("%.3f" % float(z)).rstrip("0").rstrip(".").replace(".", ",")


def banco_de_casos():
    casos = []
    for rotulo, c, z in BOBINAS:
        for n in QUANTIDADES:
            alc = alcancaveis(n, c, z)
            valores = list(alc.keys())
            fecha_em = [fmt(v) for v in valores if v in IMPEDANCIAS_DE_MODULO]
            nao_ha_modulo = [fmt(v) for v in valores if v not in IMPEDANCIAS_DE_MODULO]
            faltantes = []
            for alvo in IMPEDANCIAS_DE_MODULO:
                if alvo not in valores:
                    # O "mais perto que fecha" NAO e a menor distancia em ohms, e a
                    # decisao vem da assimetria de custo (secao 10 do ARQUIPELAGO.md):
                    # descer abaixo da impedancia minima que o modulo estabiliza e o
                    # que QUEIMA o modulo; subir acima dela perde potencia e roda frio.
                    # Errar para baixo custa hardware, errar para cima custa volume.
                    # Portanto o mais perto e o MENOR valor alcancavel que seja >= o
                    # pedido, e a distancia absoluta e explicitamente rejeitada: para
                    # dois subs 2+2 pedindo 1 ohm, 0,5 esta mais perto em ohms e e a
                    # resposta que queima o modulo; 2 ohms e a resposta certa.
                    candidatos = [v for v in valores if v in IMPEDANCIAS_DE_MODULO]
                    acima = [v for v in candidatos if v >= alvo]
                    if acima:
                        perto = min(acima)
                        abaixo_do_pedido = False
                    elif candidatos:
                        perto = max(candidatos)
                        abaixo_do_pedido = True
                    else:
                        perto = None
                        abaixo_do_pedido = None
                    faltantes.append({
                        "impedancia_de_modulo_pedida": fmt(alvo),
                        "alcancavel": False,
                        "mais_perto_que_fecha": fmt(perto) if perto is not None else None,
                        "abaixo_do_pedido": abaixo_do_pedido,
                        "criterio": "menor alcancavel >= o pedido; nunca a menor distancia em ohms",
                    })
            casos.append({
                "bobina": rotulo,
                "alto_falantes": n,
                "total_de_bobinas": n * c,
                "impedancias_alcancaveis": [
                    {"ohms": fmt(v), "ligacao": alc[v]} for v in valores
                ],
                "fecha_com_modulo_de": fecha_em,
                "alcancavel_e_fora_do_vocabulario_de_modulo": nao_ha_modulo,
                "pedidos_que_nao_fecham": faltantes,
            })
    return casos


def conferir(casos):
    """Regua PROPRIA: nao chama nenhuma funcao do gerador acima para decidir.

    Secao 8 do ARQUIPELAGO.md -- quem confere escreve a propria regua. As contas
    abaixo estao escritas a mao, com os numeros por extenso, exatamente para
    poderem discordar do gerador.
    """
    falhas = []
    afirmacoes = 0

    def afirma(cond, msg):
        nonlocal afirmacoes
        afirmacoes += 1
        if not cond:
            falhas.append(msg)

    def caso(bobina, n):
        for c in casos:
            if c["bobina"] == bobina and c["alto_falantes"] == n:
                return c
        raise AssertionError("caso ausente: %s x %d" % (bobina, n))

    # 1. O caso do corpus, escrito a mao: DOIS subs 2+2 ohms.
    #    4 bobinas de 2 ohms. Serie: 8. Dois grupos de duas: (2+2)/2 = 2.
    #    Paralelo: 2/4 = 0,5. Nao existe outro divisor de 4.
    c = caso("2+2 ohms", 2)
    ohms = [x["ohms"] for x in c["impedancias_alcancaveis"]]
    afirma(ohms == ["0,5", "2", "8"], "dois subs 2+2 deveriam dar 0,5 / 2 / 8, deram %s" % ohms)
    afirma("1" not in ohms, "1 ohm NAO pode estar no conjunto de dois subs 2+2")
    pedidos = {p["impedancia_de_modulo_pedida"]: p for p in c["pedidos_que_nao_fecham"]}
    afirma(pedidos["1"]["mais_perto_que_fecha"] == "2",
           "para dois subs 2+2, o mais perto de 1 ohm que fecha e 2 ohms; veio %r" % pedidos["1"]["mais_perto_que_fecha"])
    # A alternativa REJEITADA, afirmada de proposito: 0,5 ohm e alcancavel e esta
    # mais perto de 1 em ohms, e e a resposta que queima o modulo de 1 ohm. Se um
    # dia alguem trocar o criterio por distancia absoluta, esta linha reprova.
    afirma(pedidos["1"]["mais_perto_que_fecha"] != "0,5",
           "distancia absoluta responderia 0,5 ohm e isso e o defeito, nao a resposta")
    afirma(pedidos["1"]["abaixo_do_pedido"] is False,
           "2 ohms esta ACIMA de 1 ohm pedido, e o campo tem de dizer isso")

    # 1b. O outro lado do mesmo criterio, e ele existe no banco: QUATRO falantes de
    #     1 ohm bobina simples dao 4 / 1 / 0,25. Quem pedir modulo de 8 ohms nao tem
    #     nada acima, entao a resposta desce para 4 e o campo declara que desceu.
    c8 = caso("1 ohm", 4)
    p8 = {p["impedancia_de_modulo_pedida"]: p for p in c8["pedidos_que_nao_fecham"]}
    afirma(p8["8"]["mais_perto_que_fecha"] == "4", "sem nada acima de 8, a resposta e o maior que fecha")
    afirma(p8["8"]["abaixo_do_pedido"] is True, "e ela tem de se declarar abaixo do pedido")
    c = caso("2+2 ohms", 2)

    # 2. UM sub 2+2 ohms: 2 bobinas de 2. Serie 4, paralelo 1. So isso.
    c = caso("2+2 ohms", 1)
    ohms = [x["ohms"] for x in c["impedancias_alcancaveis"]]
    afirma(ohms == ["1", "4"], "um sub 2+2 deveria dar 1 / 4, deu %s" % ohms)

    # 3. DOIS subs 4+4 ohms: 4 bobinas de 4. Serie 16, meio 4, paralelo 1.
    c = caso("4+4 ohms", 2)
    ohms = [x["ohms"] for x in c["impedancias_alcancaveis"]]
    afirma(ohms == ["1", "4", "16"], "dois subs 4+4 deveriam dar 1 / 4 / 16, deu %s" % ohms)
    afirma("16" in c["alcancavel_e_fora_do_vocabulario_de_modulo"], "16 ohms esta fora do vocabulario de impedancia de modulo e isso tem de estar dito")

    # 4. TRES falantes de 4 ohms bobina simples: 3 bobinas. Divisores de 3: 1 e 3.
    #    Serie 12, paralelo 4/3 = 1,333. Nenhum dos dois e impedancia de modulo.
    c = caso("4 ohms", 3)
    ohms = [x["ohms"] for x in c["impedancias_alcancaveis"]]
    afirma(ohms == ["1,333", "12"], "tres falantes de 4 ohms deveriam dar 1,333 / 12, deu %s" % ohms)
    afirma(c["fecha_com_modulo_de"] == [], "tres falantes de 4 ohms nao fecham em modulo nenhum, e o gerador disse %s" % c["fecha_com_modulo_de"])

    # 5. A BORDA de baixo: um falante de 1 ohm sozinho so tem uma ligacao.
    c = caso("1 ohm", 1)
    afirma(len(c["impedancias_alcancaveis"]) == 1, "um falante de bobina simples nao tem ligacao a escolher")
    afirma(c["impedancias_alcancaveis"][0]["ohms"] == "1", "e ele e a propria bobina")

    # 6. Caso que o ESQUEMA permite e que a prosa nunca cita (secao 8 do contrato):
    #    QUATRO falantes 1+1 ohms = 8 bobinas de 1 ohm. Divisores de 8: 1,2,4,8.
    #    8, 2, 0,5, 0,125. O ultimo e alcancavel e esta FORA do vocabulario de modulo.
    c = caso("1+1 ohms", 4)
    ohms = [x["ohms"] for x in c["impedancias_alcancaveis"]]
    afirma(ohms == ["0,125", "0,5", "2", "8"], "quatro 1+1 deveriam dar 0,125 / 0,5 / 2 / 8, deu %s" % ohms)
    afirma("0,125" in c["alcancavel_e_fora_do_vocabulario_de_modulo"],
           "0,125 ohm e alcancavel e esta fora do vocabulario; a F1 recusa em vez de recomendar")

    # 6b. O VEREDITO QUE SAIU DA ENUMERACAO e que nenhuma pagina medida publica:
    #     TRES alto-falantes iguais nao fecham em impedancia de modulo NENHUMA, seja
    #     qual for a bobina. Conta a mao para 3 falantes 2+2 (K=6 bobinas de 2 ohms):
    #     divisores de 6 sao 1, 2, 3 e 6, dando 12 / 3 / 1,333 / 0,333 -- e nenhum dos
    #     quatro e 0,5, 1, 2, 4 ou 8. O mesmo acontece com as outras cinco bobinas.
    #     Afirmado sobre as SEIS montagens de tres, nao sobre uma amostra.
    tres = [c for c in casos if c["alto_falantes"] == 3]
    afirma(len(tres) == len(BOBINAS), "tem de haver uma montagem de tres por tipo de bobina")
    for c in tres:
        afirma(c["fecha_com_modulo_de"] == [],
               "tres falantes de %s nao fecham em modulo nenhum, e o gerador disse %s"
               % (c["bobina"], c["fecha_com_modulo_de"]))
    # E o contraexemplo que impede a afirmacao de virar "impar nunca fecha": UM falante
    # sozinho e impar e fecha, quando a bobina ja e impedancia de modulo.
    afirma(caso("2 ohms", 1)["fecha_com_modulo_de"] == ["2"],
           "um falante de 2 ohms fecha em modulo de 2 ohms: a regra e sobre TRES, nao sobre impar")

    # 7. Cobertura: todo caso tem pelo menos uma ligacao, e nenhuma impedancia
    #    aparece duas vezes na lista de um caso.
    for c in casos:
        afirma(len(c["impedancias_alcancaveis"]) >= 1, "caso sem ligacao: %s x %s" % (c["bobina"], c["alto_falantes"]))
        vistos = [x["ohms"] for x in c["impedancias_alcancaveis"]]
        afirma(len(vistos) == len(set(vistos)), "impedancia repetida em %s x %s" % (c["bobina"], c["alto_falantes"]))

    # 8. O tamanho do banco de casos e CONTADO, nunca digitado (secao 8).
    afirma(len(casos) == len(BOBINAS) * len(QUANTIDADES),
           "o banco de casos tem de ser bobinas x quantidades")

    return afirmacoes, falhas


def main():
    casos = banco_de_casos()
    if "--conferir" in sys.argv:
        afirmacoes, falhas = conferir(casos)
        for f in falhas:
            print("FALHA: %s" % f)
        print("%d afirmacoes, %d falha(s)" % (afirmacoes, len(falhas)))
        return 1 if falhas else 0

    doc = {
        "ilha": "ohmetria",
        "bloco": "2",
        "corrigido_no_bloco": 3,
        "titulo": "Impedancias alcancaveis por ligacao simetrica",
        "gerado_por": "ferramentas/impedancias.py",
        "gerado_em": "2026-09-14",
        "publicar": False,
        "o_que_este_arquivo_e": (
            "Dominio de saida da F1, enumerado. Nao e banco de produto e nao tem fonte de "
            "fabricante: e aritmetica de associacao em serie e paralelo, derivada no proprio "
            "arquivo do gerador. Serve a especificacao para que a resposta 'nao fecha' seja "
            "calculada, nunca opinada."
        ),
        "modelo": (
            "K bobinas iguais de Z ohms, partidas em g grupos iguais de K/g em serie, os g "
            "grupos em paralelo: Z_final = Z * K / g^2, com g dividindo K. g=1 e tudo em serie, "
            "g=K e tudo em paralelo."
        ),
        "recusa_declarada": (
            "Ligacao assimetrica nao entra. Ela fecha valores intermediarios e faz bobinas "
            "identicas receberem potencia diferente; a F1 diz isso na tela em vez de omitir."
        ),
        "impedancias_de_modulo_do_esquema": [fmt(z) for z in IMPEDANCIAS_DE_MODULO],
        "o_que_esta_lista_e_e_o_que_ela_NAO_e": (
            "Vocabulario impedancia_de_modulo de dados/esquema-banco.json, lido dali e nunca "
            "copiado para dentro deste gerador. E EXPECTATIVA DECLARADA, nao medicao de mercado: "
            "ela veio da leitura de SERP do bloco 1 e nenhum registro de banco a sustenta ainda. "
            "Portanto o campo alcancavel_e_fora_do_vocabulario_de_modulo autoriza a F1 a dizer "
            "'nenhum modulo do nosso banco atende essa impedancia' e NUNCA "
            "'nao existe modulo para isso' -- a segunda e afirmacao sobre o mercado e esta ilha "
            "nao a mediu. Ate o bloco 3 este campo se chamava "
            "'alcancavel_mas_sem_modulo_no_mercado' e afirmava exatamente o que nao podia."
        ),
        "total_de_casos": len(casos),
        "casos": casos,
    }
    with open("dados/impedancias-alcancaveis.json", "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("gravado dados/impedancias-alcancaveis.json com %d casos" % len(casos))
    return 0


if __name__ == "__main__":
    sys.exit(main())
