#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BANCADA DA F1. Regua PROPRIA, escrita a mao.

    python3 ferramentas/teste-f1.py            # mede o arquivo gravado
    python3 ferramentas/teste-f1.py --gerar    # mede o que a referencia produz agora

SECAO 8 DO ARQUIPELAGO.md, e as tres linhas dela que este arquivo obedece:

  1. QUEM CONFERE ESCREVE A PROPRIA REGUA. Este arquivo nao chama uma unica funcao
     de ferramentas/f1-referencia.py para DECIDIR. A aritmetica de associacao esta
     reescrita aqui, com Fraction e divisores, e ela pode discordar do gerador --
     e o dia em que discordar, quem ganha e ela.
  2. VARRER A ENTRADA INTEIRA, NAO O CASO-ANCORA. Ferramenta de entrada variavel
     serve uma pagina por consulta; a pagina sem consulta e so uma das 144. Toda
     afirmacao abaixo e sobre a soma dos estados, nunca sobre um exemplo.
  3. AFIRMACAO SOBRE O QUE A PAGINA DIZ SE MEDE NO CORPO. texto_de_tela() junta
     exatamente o que o visitante le -- e deixa de fora id, url e palavra-chave de
     busca, que sao ASCII por desenho e nao sao frase.

A GRADE PISA NA BORDA: o dominio da F1 e pequeno e enumeravel, entao aqui nao
existe amostra. Sao as 24 montagens contra as 5 impedancias do vocabulario mais o
pedido vazio, todas elas, e o tamanho e CONTADO dos dois lados.
"""

import importlib.util
import io
import json
import os
import re
import sys
from fractions import Fraction
from urllib.parse import quote_plus

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(AQUI)
DADOS = os.path.join(BASE, "dados")


def _ler(nome):
    return json.load(io.open(os.path.join(DADOS, nome), encoding="utf-8"))


# ---------------------------------------------------------------------------
# A ARITMETICA, REESCRITA A MAO. Nao importa nada do gerador.
# ---------------------------------------------------------------------------

def _fracao(token):
    inteiro, _, decimal = token.partition(",")
    if decimal:
        return Fraction(int(inteiro + decimal), 10 ** len(decimal))
    return Fraction(int(inteiro))


def _texto(z):
    if z.denominator == 1:
        return str(z.numerator)
    return ("%.3f" % float(z)).rstrip("0").rstrip(".").replace(".", ",")


def _alcancaveis_a_mao(rotulo_da_bobina, quantidade):
    """Z * K / g^2, com g dividindo K. Escrito aqui para poder discordar."""
    token = rotulo_da_bobina.split(" ")[0]
    partes = token.split("+")
    bobinas_por_falante = len(partes)
    z = _fracao(partes[0])
    k = quantidade * bobinas_por_falante
    valores = set()
    for g in range(1, k + 1):
        if k % g:
            continue
        valores.add(z * Fraction(k, 1) / Fraction(g * g, 1))
    return sorted(valores)


# ---------------------------------------------------------------------------
# O CORPO: o que o visitante LE, e so isso.
# ---------------------------------------------------------------------------

def texto_de_tela(r):
    partes = [r["veredito"]["frase"]]
    if r.get("nota_da_quantidade"):
        partes.append(r["nota_da_quantidade"])
    for l in r["ligacoes"]:
        partes.append(l["ligacao"])
        partes.append(l["frase_do_banco"])
    if r["potencia"].get("frase"):
        partes.append(r["potencia"]["frase"])
    partes.append(r["prestacao_de_contas"]["frase"])
    for m in r["prestacao_de_contas"]["fora"]:
        partes.append(m["motivo"])
    partes.append(r["compra"]["frase"])
    for rec in r["recusas"]:
        partes.append(rec["frase"])
    return "\n".join(partes)


# O que a pagina NUNCA pode dizer enquanto o banco nao sustentar a frase. Cada
# linha e uma afirmacao sobre o MERCADO, e esta ilha nao mediu mercado nenhum.
FRASES_DE_MERCADO = [
    "nao existe modulo",
    "não existe módulo",
    "no mercado",
    "nenhum modulo existe",
    "nenhum módulo existe",
    "nao e fabricado",
    "não é fabricado",
]

# O que a pagina NUNCA pode afirmar enquanto criterio-rms-modulo-nao-passa-do-falante
# estiver pendente (secao 10: constante pendente e proibida dentro de formula publicada).
FRASES_DE_TETO_DE_RMS = [
    "pode ter até",
    "no máximo",
    "o dobro da potência",
    "até 100 por cento",
    "vezes o rms",
]

# VOZ.md, secao "Proibidas". Nenhuma delas no veredito nem no primeiro paragrafo.
FRASES_PROIBIDAS_PELA_VOZ = [
    "associação de impedâncias",
    "especificação verificável",
    "conforme a ficha técnica do fabricante",
    "consulta paramétrica",
    "procedência",
]

# Texto de tela sai ACENTUADO (fase 4b do playbook). O banco e ASCII; a tela nao.
PALAVRAS_QUE_DENUNCIAM_ASCII = [
    "serie", "impedancia", "impedancias", "modulo", "modulos", "potencia",
    "minimo", "criterio", "voce", "alcanca", "numero",
]


def conferir(doc, banco, esquema, doc_casos, constantes, especificacao=None):
    falhas = []
    afirmacoes = 0

    def afirma(cond, msg):
        nonlocal afirmacoes
        afirmacoes += 1
        if not cond:
            falhas.append(msg)

    respostas = doc["respostas"]
    vocab_modulo = esquema["vocabularios"]["impedancia_de_modulo"]["valores"]
    vocab_bobina = esquema["vocabularios"]["impedancia_de_bobina"]["valores"]
    quantidades = sorted({c["alto_falantes"] for c in doc_casos["casos"]})

    # -- A. O DOMINIO, contado dos dois lados ------------------------------
    esperado = len(vocab_bobina) * len(quantidades) * (len(vocab_modulo) + 1)
    afirma(len(respostas) == esperado,
           "o dominio da F1 tem de ser bobinas x quantidades x (pedidos + o vazio) = %d; "
           "vieram %d" % (esperado, len(respostas)))
    afirma(doc["total_de_estados"] == len(respostas),
           "total_de_estados esta digitado e nao contado: diz %s, ha %d respostas"
           % (doc["total_de_estados"], len(respostas)))

    chaves = [(r["entrada"]["bobina"], r["entrada"]["alto_falantes"],
               r["entrada"]["impedancia_do_modulo_pedida"]) for r in respostas]
    afirma(len(chaves) == len(set(chaves)), "ha estado repetido no dominio da F1")
    faltando = []
    for bob in vocab_bobina:
        rotulo = "%s ohm%s" % (bob, "" if bob == "1" else "s")
        for n in quantidades:
            for pedido in [None] + list(vocab_modulo):
                if (rotulo, n, pedido) not in set(chaves):
                    faltando.append((rotulo, n, pedido))
    afirma(not faltando, "estados ausentes do dominio: %s" % faltando[:5])

    # -- B. A ARITMETICA, contra a regua propria ----------------------------
    for r in respostas:
        e = r["entrada"]
        meu = [_texto(z) for z in _alcancaveis_a_mao(e["bobina"], e["alto_falantes"])]
        dele = [l["ohms"] for l in r["ligacoes"]]
        afirma(meu == dele,
               "%s x %d: a regua propria calcula %s e a resposta traz %s"
               % (e["bobina"], e["alto_falantes"], meu, dele))
        for l in r["ligacoes"]:
            afirma(bool(l["ligacao"].strip()),
                   "%s x %d: a impedancia %s foi servida sem dizer como ligar"
                   % (e["bobina"], e["alto_falantes"], l["ohms"]))
            afirma(l["e_impedancia_de_modulo"] == (l["ohms"] in vocab_modulo),
                   "%s: a marcacao de impedancia de modulo discorda do vocabulario do esquema"
                   % l["ohms"])
            # Quem estabiliza naquela impedancia e CONTADO do banco aqui, por um
            # caminho que nao e o da referencia. Esta linha nasceu porque a bateria
            # de mutacoes achou o buraco: com modulo no banco, a linha da ligacao
            # podia continuar dizendo que nao havia nenhum e a bancada aprovava.
            meus_modulos = sorted(m.get("id") for m in banco
                                  if l["ohms"] in (m.get("impedancias_estaveis") or []))
            afirma(sorted(l["modulos_do_banco"]) == meus_modulos,
                   "%s x %d, ligacao de %s: o banco tem %s estabilizando ai e a linha traz %s"
                   % (e["bobina"], e["alto_falantes"], l["ohms"], meus_modulos,
                      sorted(l["modulos_do_banco"])))
            esperado_na_frase = (str(len(meus_modulos)) if meus_modulos else "Nenhum")
            afirma(esperado_na_frase in l["frase_do_banco"],
                   "%s x %d, ligacao de %s: a frase nao carrega a contagem do banco (%s): %r"
                   % (e["bobina"], e["alto_falantes"], l["ohms"], esperado_na_frase,
                      l["frase_do_banco"]))

    # -- C. O VEREDITO, decidido de novo aqui -------------------------------
    for r in respostas:
        e = r["entrada"]
        pedido = e["impedancia_do_modulo_pedida"]
        alc = _alcancaveis_a_mao(e["bobina"], e["alto_falantes"])
        no_vocab = [z for z in alc if _texto(z) in vocab_modulo]
        codigo = r["veredito"]["codigo"]
        frase = r["veredito"]["frase"]
        afirma(bool(frase.strip()), "estado sem veredito: %s" % (e,))

        if pedido is None:
            afirma(codigo == "SEM_PEDIDO", "pedido vazio tem de dar SEM_PEDIDO, deu %s" % codigo)
            # Escolha que nao existe nao se oferece: com uma unica ligacao possivel,
            # "depende de como voce liga" e uma pergunta devolvida como se fosse
            # resposta. A regua conta as ligacoes e cobra os dois sentidos.
            # A implicacao e de um lado so, e isso importa: a frase PODE nao oferecer
            # escolha havendo varias ligacoes (e o que acontece quando nenhuma delas
            # cai em impedancia de modulo -- ali nao ha nada a escolher que sirva);
            # o que ela NUNCA pode e oferecer escolha onde so existe uma ligacao.
            oferece_escolha = "depende de como" in frase
            afirma(not oferece_escolha or len(alc) > 1,
                   "%s x %d: a frase oferece escolha e a montagem tem uma ligacao so: %r"
                   % (e["bobina"], e["alto_falantes"], frase))
            continue

        alvo = _fracao(pedido)
        if alvo in alc:
            afirma(codigo == "FECHA",
                   "%s x %d pedindo %s: %s esta no conjunto, o veredito tem de ser FECHA e foi %s"
                   % (e["bobina"], e["alto_falantes"], pedido, pedido, codigo))
        elif not no_vocab:
            afirma(codigo == "NAO_FECHA_NENHUM",
                   "%s x %d pedindo %s: nenhuma ligacao cai em impedancia de modulo, o veredito "
                   "tem de ser NAO_FECHA_NENHUM e foi %s"
                   % (e["bobina"], e["alto_falantes"], pedido, codigo))
        else:
            acima = [z for z in no_vocab if z >= alvo]
            if acima:
                afirma(codigo == "NAO_FECHA_SOBE",
                       "%s x %d pedindo %s: existe valor acima, o veredito tem de ser "
                       "NAO_FECHA_SOBE e foi %s" % (e["bobina"], e["alto_falantes"], pedido, codigo))
                # Substring solta casaria "1" dentro de "1,333" e dentro de "12":
                # a regua exige o NUMERO INTEIRO seguido da unidade.
                alvo_seguro = _texto(min(acima))
                afirma(re.search(r"(?<![\d,])%s ohm" % re.escape(alvo_seguro), frase),
                       "%s x %d pedindo %s: a saida segura e %s e a frase nao a nomeia: %r"
                       % (e["bobina"], e["alto_falantes"], pedido, alvo_seguro, frase))
                # A ALTERNATIVA REJEITADA, afirmada de proposito: a menor DISTANCIA
                # em ohms pode estar abaixo do pedido, e abaixo do minimo e o que
                # queima o modulo. Se alguem trocar o criterio por distancia
                # absoluta, esta linha reprova.
                por_distancia = min(no_vocab, key=lambda z: abs(z - alvo))
                if por_distancia < alvo:
                    afirma(_texto(por_distancia) != _texto(min(acima)),
                           "o criterio virou distancia absoluta em %s x %d pedindo %s"
                           % (e["bobina"], e["alto_falantes"], pedido))
            else:
                afirma(codigo == "NAO_FECHA_SO_ABAIXO",
                       "%s x %d pedindo %s: nada alcanca %s ou mais, o veredito tem de ser "
                       "NAO_FECHA_SO_ABAIXO e foi %s"
                       % (e["bobina"], e["alto_falantes"], pedido, pedido, codigo))
                afirma("queima" in frase.lower(),
                       "%s x %d pedindo %s: ficar abaixo do minimo queima o modulo e a frase "
                       "nao avisa: %r" % (e["bobina"], e["alto_falantes"], pedido, frase))
                afirma("mais perto que fecha" not in frase.lower(),
                       "%s x %d pedindo %s: o valor abaixo do minimo foi oferecido como 'mais "
                       "perto que fecha', que e a resposta que queima"
                       % (e["bobina"], e["alto_falantes"], pedido))

    # -- D. A NOTA DA QUANTIDADE, contada e nao digitada --------------------
    minhas_nunca_fecham = []
    for n in quantidades:
        fecha_alguma = False
        for bob in vocab_bobina:
            rotulo = "%s ohm%s" % (bob, "" if bob == "1" else "s")
            if any(_texto(z) in vocab_modulo for z in _alcancaveis_a_mao(rotulo, n)):
                fecha_alguma = True
        if not fecha_alguma:
            minhas_nunca_fecham.append(n)
    afirma(minhas_nunca_fecham == [3],
           "a regua propria diz que as quantidades que nunca fecham sao %s; se isso mudou, a "
           "frase da tela tem de mudar junto" % minhas_nunca_fecham)
    for r in respostas:
        n = r["entrada"]["alto_falantes"]
        tem = bool(r.get("nota_da_quantidade"))
        afirma(tem == (n in minhas_nunca_fecham),
               "a nota de quantidade apareceu em %d alto-falantes e a regua diz %s"
               % (n, minhas_nunca_fecham))
        if tem:
            afirma(str(len(vocab_bobina)) in r["nota_da_quantidade"],
                   "a nota diz sobre quantas montagens de %d ela fala, e o numero nao e o "
                   "contado (%d)" % (n, len(vocab_bobina)))
    # O contraexemplo que impede a afirmacao de virar "impar nunca fecha".
    um_de_dois = [r for r in respostas
                  if r["entrada"]["alto_falantes"] == 1 and r["entrada"]["bobina"] == "2 ohms"
                  and r["entrada"]["impedancia_do_modulo_pedida"] == "2"]
    afirma(len(um_de_dois) == 1 and um_de_dois[0]["veredito"]["codigo"] == "FECHA",
           "um falante de 2 ohms pedindo modulo de 2 ohms tem de FECHAR: a afirmacao e sobre "
           "TRES, nunca sobre impar")

    # -- E. PRESTACAO DE CONTAS (secao 7 e especificacao 1.6) ---------------
    ids_do_banco = [m.get("id") for m in banco]
    for r in respostas:
        p = r["prestacao_de_contas"]
        afirma(p["modulos_no_banco"] == len(banco),
               "a resposta diz %s modulos no banco e o banco carregado tem %d"
               % (p["modulos_no_banco"], len(banco)))
        nomeados = [m["id"] for m in p["dentro"]] + [m["id"] for m in p["fora"]]
        afirma(len(nomeados) == len(banco),
               "a soma dos nomeados (%d) nao fecha o banco contado (%d) em %s"
               % (len(nomeados), len(banco), r["entrada"]))
        afirma(len(nomeados) == len(set(nomeados)),
               "modulo nomeado duas vezes na mesma resposta: %s" % nomeados)
        afirma(sorted(nomeados) == sorted(ids_do_banco),
               "a resposta nomeia %s e o banco tem %s" % (sorted(nomeados), sorted(ids_do_banco)))
        for m in p["fora"]:
            afirma(bool(m["motivo"].strip()),
                   "modulo %s ficou de fora sem motivo escrito" % m["id"])
        afirma(str(len(banco)) in p["frase"],
               "a frase da prestacao de contas nao carrega o total contado (%d): %r"
               % (len(banco), p["frase"]))

    # -- F. O QUE A PAGINA NUNCA PODE DIZER ---------------------------------
    sem_lastro = [x for x in vocab_modulo
                  if not any(x in (m.get("impedancias_estaveis") or []) for m in banco)]
    for r in respostas:
        corpo = texto_de_tela(r).lower()
        if sem_lastro:
            for proibida in FRASES_DE_MERCADO:
                afirma(proibida not in corpo,
                       "afirmacao sobre o MERCADO no corpo (%r) com %d entrada(s) do "
                       "vocabulario sem lastro no banco, em %s"
                       % (proibida, len(sem_lastro), r["entrada"]))
        criterio = next(c for c in constantes["constantes"]
                        if c["id"] == "criterio-rms-modulo-nao-passa-do-falante")
        if criterio["status"] != "publicavel":
            for proibida in FRASES_DE_TETO_DE_RMS:
                afirma(proibida not in corpo,
                       "teto de RMS afirmado (%r) com o criterio do fabricante em status %r, "
                       "em %s" % (proibida, criterio["status"], r["entrada"]))
        for proibida in FRASES_PROIBIDAS_PELA_VOZ:
            afirma(proibida not in r["veredito"]["frase"].lower(),
                   "o veredito usa %r, que o VOZ.md proibe no titulo e no primeiro paragrafo"
                   % proibida)
        for palavra in PALAVRAS_QUE_DENUNCIAM_ASCII:
            afirma(not re.search(r"\b%s\b" % palavra, corpo),
                   "texto de tela sem acento (%r) em %s. O banco e ASCII, a tela nao e"
                   % (palavra, r["entrada"]))

    # -- G. O BLOCO DE COMPRA (secoes 7 e 25.2) -----------------------------
    molde = esquema["piso_de_compra"]["moldes"]["shopee"]
    for r in respostas:
        e = r["entrada"]
        compra = r["compra"]
        afirma("frase" in compra and bool(compra["frase"].strip()),
               "o bloco de compra veio sem uma linha para o visitante em %s" % (e,))
        pedido = e["impedancia_do_modulo_pedida"]
        alc = _alcancaveis_a_mao(e["bobina"], e["alto_falantes"])
        no_vocab = [z for z in alc if _texto(z) in vocab_modulo]
        alvo = None if pedido is None else _fracao(pedido)
        if pedido is None:
            meus = [_texto(z) for z in no_vocab]
        elif alvo in alc:
            meus = [pedido]
        else:
            acima = [z for z in no_vocab if z >= alvo]
            meus = [_texto(min(acima))] if acima else []
        dele = [p["para_a_impedancia"] for p in compra["pisos"]]
        afirma(meus == dele,
               "%s x %d pedindo %s: o piso tem de cobrir %s e cobriu %s"
               % (e["bobina"], e["alto_falantes"], pedido, meus, dele))
        for p in compra["pisos"]:
            meu_url = molde.format(palavra_chave=quote_plus(p["palavra_chave_busca"]))
            afirma(p["url_busca_produto"] == meu_url,
                   "URL de piso digitada e nao fabricada do molde: %r contra %r"
                   % (p["url_busca_produto"], meu_url))
            afirma("sponsored" not in (p["rel"] or ""),
                   "busca CRUA saiu com rel=sponsored, declarando relacao paga que nao existe")
            afirma(p["rastreavel"] is False,
                   "o piso se declarou rastreavel e esta ilha nao tem etiqueta de afiliado")
        if not compra["pisos"]:
            afirma("http" not in json.dumps(compra, ensure_ascii=False),
                   "o bloco sem piso deixou um link solto em %s" % (e,))
            afirma(len(compra["frase"]) > 60,
                   "bloco de compra vazio sem dizer POR QUE: %r. Silencio parece defeito"
                   % compra["frase"])

    # -- H. A TABELA PRE-RENDERIZADA (secao 5) ------------------------------
    tabela = doc["tabela_de_exemplos"]
    afirma(len(tabela) == len(vocab_bobina) * len(quantidades),
           "a tabela pre-renderizada tem de ter uma linha por montagem (%d) e tem %d"
           % (len(vocab_bobina) * len(quantidades), len(tabela)))
    afirma(doc["montagens"] == len(tabela),
           "o campo montagens esta digitado: diz %s e a tabela tem %d linhas"
           % (doc["montagens"], len(tabela)))
    for linha in tabela:
        meu = [_texto(z) for z in _alcancaveis_a_mao(linha["bobina"], linha["alto_falantes"])]
        afirma(linha["alcanca"] == meu,
               "linha da tabela pre-renderizada discorda da regua: %s x %d traz %s, a conta da %s"
               % (linha["bobina"], linha["alto_falantes"], linha["alcanca"], meu))
        meu_fecha = [x for x in meu if x in vocab_modulo]
        afirma(linha["fecha_em"] == meu_fecha,
               "linha da tabela: %s x %d diz que fecha em %s, a conta diz %s"
               % (linha["bobina"], linha["alto_falantes"], linha["fecha_em"], meu_fecha))
        afirma(linha["modulos_do_nosso_banco"] == len(banco),
               "a linha da tabela publica %s modulos e o banco tem %d"
               % (linha["modulos_do_nosso_banco"], len(banco)))
        afirma(bool(linha["veredito"].strip()),
               "linha da tabela sem veredito: %s x %d" % (linha["bobina"], linha["alto_falantes"]))

    # -- I. AS RECUSAS DECLARADAS (especificacao 1.7) -----------------------
    obrigatorias = {"ligacao-assimetrica", "teto-de-quatro", "falantes-iguais",
                    "qual-e-o-melhor", "quanto-aguenta-de-verdade"}
    for r in respostas:
        ids = {x["id"] for x in r["recusas"]}
        afirma(obrigatorias <= ids,
               "recusa declarada faltando em %s: %s" % (r["entrada"], obrigatorias - ids))

    # -- J. COMO SABEMOS (especificacao 1.3, saida 5) -----------------------
    esperadas = {c["id"] for c in constantes["constantes"]
                 if c["status"] in ("publicavel", "publicavel_como_desacordo")
                 and "F1" in (c.get("usada_em") or [])}
    pendentes = {c["id"] for c in constantes["constantes"]
                 if c["status"] == "pendente" and "F1" in (c.get("usada_em") or [])}
    for r in respostas:
        ids = {c["id"] for c in r["como_sabemos"]}
        afirma(ids == esperadas,
               "'como sabemos' traz %s e as constantes publicaveis da F1 sao %s"
               % (sorted(ids), sorted(esperadas)))
        afirma(not (ids & pendentes),
               "constante pendente publicada como prova: %s" % sorted(ids & pendentes))
    afirma("desacordo-multiplicador-rms-serp" in esperadas,
           "o desacordo da SERP tem de estar no 'como sabemos' da F1 (especificacao 1.3)")

    # -- K. OS NUMEROS QUE A ESPECIFICACAO PUBLICA -------------------------
    # A secao 7 de dados/especificacao-calculadoras.md publica a distribuicao dos
    # vereditos e a conta do piso de compra. Numero em prosa envelhece calado: a
    # primeira versao daquela secao dizia 47 estados sem piso e sao 53, porque a
    # soma foi feita de cabeca em vez de contada. Entao a prosa tambem passa pela
    # varredura -- e esta e a TERCEIRA conta que a secao 8 do contrato pede, lendo
    # a fonte por um caminho que nao e o do gerador.
    if especificacao is not None:
        por_codigo = {}
        for r in respostas:
            por_codigo[r["veredito"]["codigo"]] = por_codigo.get(r["veredito"]["codigo"], 0) + 1
        rotulos = {
            "FECHA": r"FECHA (\d+) ·",
            "NAO_FECHA_SOBE": r"NÃO FECHA, SOBE (\d+)",
            "NAO_FECHA_SO_ABAIXO": r"NÃO FECHA, SÓ ABAIXO (\d+)",
            "NAO_FECHA_NENHUM": r"NÃO FECHA EM NENHUMA (\d+)",
            "SEM_PEDIDO": r"SEM PEDIDO (\d+)",
        }
        for codigo, padrao in rotulos.items():
            achado = re.search(padrao, especificacao)
            afirma(achado is not None,
                   "a secao 7 da especificacao nao publica mais a contagem de %s; se a linha "
                   "mudou de forma, esta regua tem de mudar junto" % codigo)
            if achado:
                afirma(int(achado.group(1)) == por_codigo.get(codigo, 0),
                       "a especificacao publica %s para %s e a varredura conta %d"
                       % (achado.group(1), codigo, por_codigo.get(codigo, 0)))
        sem_piso = sum(1 for r in respostas if not r["compra"]["pisos"])
        com_piso = len(respostas) - sem_piso
        achado = re.search(r"São \*\*(\d+)\*\* estados, contra (\d+) com piso", especificacao)
        afirma(achado is not None,
               "a secao 7 da especificacao nao publica mais a conta do piso de compra")
        if achado:
            afirma(int(achado.group(1)) == sem_piso and int(achado.group(2)) == com_piso,
                   "a especificacao publica %s sem piso e %s com piso; a varredura conta %d e %d"
                   % (achado.group(1), achado.group(2), sem_piso, com_piso))

    return afirmacoes, falhas


def main():
    esquema = _ler("esquema-banco.json")
    doc_casos = _ler("impedancias-alcancaveis.json")
    banco = _ler("modulos.json")["itens"]
    constantes = _ler("constantes.json")

    if "--gerar" in sys.argv:
        spec = importlib.util.spec_from_file_location(
            "gerar_f1", os.path.join(AQUI, "gerar-f1.py"))
        gerar = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(gerar)
        doc = gerar.documento(gerar._referencia())
    else:
        doc = _ler("f1-respostas.json")

    especificacao = io.open(os.path.join(DADOS, "especificacao-calculadoras.md"),
                            encoding="utf-8").read()
    afirmacoes, falhas = conferir(doc, banco, esquema, doc_casos, constantes, especificacao)
    for f in falhas[:40]:
        print("FALHA: %s" % f)
    if len(falhas) > 40:
        print("... e mais %d falha(s)" % (len(falhas) - 40))
    print("%d afirmacoes, %d falha(s)" % (afirmacoes, len(falhas)))
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
