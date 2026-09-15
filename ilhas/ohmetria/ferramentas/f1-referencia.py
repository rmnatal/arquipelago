#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""F1 -- QUAL MODULO FECHA COM O SEU FALANTE. Implementacao de REFERENCIA.

Bloco 4. Este arquivo e o CEREBRO da F1: dado um estado de entrada, ele devolve a
resposta inteira -- veredito, ligacoes, prestacao de contas, bloco de compra e
"como sabemos" -- ja em frase acentuada, do jeito que o visitante le.

    python3 ferramentas/f1-referencia.py            # imprime uma resposta de exemplo
    python3 ferramentas/f1-referencia.py --contar   # so o tamanho do dominio

POR QUE A REFERENCIA E PYTHON E NAO PHP, e isto e decisao registrada do bloco 4:
esta ilha NAO TEM SITE. O passo 3b (casca do WordPress) e trabalho de navegador e
esta com o Raphael; sem casca, um snippet PHP so poderia ser medido por um render
de bancada que serve MENOS do que o site serve -- que e exatamente a cicatriz da
secao 8 do ARQUIPELAGO.md ("o render de bancada tem que servir o que o site
serve, e a metade que falta some em silencio"). Entao a regra nasce onde ela pode
ser conferida hoje, e o PHP, quando nascer, vira tradutor desta referencia frase a
frase -- o mesmo desenho que a Robometria usa entre cobertura-r1.py e
robometria-r1.php.

O QUE ESTE ARQUIVO NAO FAZ, de proposito:

  - Nao afirma nada sobre o MERCADO. Enquanto o vocabulario impedancia_de_modulo
    tiver entrada sem lastro no banco (hoje 5 de 5, porque o banco tem 0 modulos),
    a unica frase verdadeira e "nenhum modulo do NOSSO BANCO". A frase "nao existe
    modulo para isso" esta proibida e a bancada a procura em toda resposta.
  - Nao afirma teto de RMS. O criterio do fabricante
    (criterio-rms-modulo-nao-passa-do-falante) esta com status PENDENTE em
    dados/constantes.json, e constante pendente e proibida dentro de formula
    publicada (secao 10). A F1 imprime o numero do falante e diz o que ainda nao
    pode dizer, em vez de calar.
  - Nao digita numero nenhum sobre o proprio banco. Toda contagem sai de len() do
    banco carregado (secao 8: numero de tela nasce contado, nunca digitado).
"""

import io
import json
import os
import re
import sys
from urllib.parse import quote_plus

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(AQUI)
DADOS = os.path.join(BASE, "dados")

ESQUEMA = os.path.join(DADOS, "esquema-banco.json")
CASOS = os.path.join(DADOS, "impedancias-alcancaveis.json")
MODULOS = os.path.join(DADOS, "modulos.json")
CONSTANTES = os.path.join(DADOS, "constantes.json")


# ---------------------------------------------------------------------------
# CARGA. Nenhuma destas listas tem copia dentro deste arquivo: se a chave sumir
# da fonte, a referencia MORRE em vez de cair num literal (secao 26.2 e o achado
# do bloco 3, em que uma lista digitada fez a F1 quase publicar uma afirmacao
# sobre o mercado).
# ---------------------------------------------------------------------------

def _ler(caminho):
    return json.load(io.open(caminho, encoding="utf-8"))


def carregar_esquema():
    return _ler(ESQUEMA)


def carregar_casos():
    doc = _ler(CASOS)
    if not doc.get("casos"):
        raise SystemExit(
            "dados/impedancias-alcancaveis.json esta sem casos. A F1 nao tem dominio "
            "de saida sem ele -- rode ferramentas/impedancias.py.")
    return doc


def carregar_modulos():
    doc = _ler(MODULOS)
    if "itens" not in doc:
        raise SystemExit("dados/modulos.json sem a chave itens.")
    return doc


def carregar_constantes():
    return _ler(CONSTANTES)


def vocabulario(esquema, nome):
    valores = esquema.get("vocabularios", {}).get(nome, {}).get("valores")
    if not valores:
        raise SystemExit(
            "esquema-banco.json nao tem o vocabulario %s, ou ele esta vazio.\n"
            "A F1 NAO guarda copia dessa lista: uma copia envelheceria calada e a "
            "ferramenta voltaria a decidir 'fecha' contra um literal." % nome)
    return list(valores)


def molde_do_piso(esquema, programa):
    moldes = esquema.get("piso_de_compra", {}).get("moldes", {})
    if programa not in moldes:
        raise SystemExit(
            "esquema-banco.json nao publica molde de piso de compra para %r. O piso da "
            "secao 25.2 nasce do molde, nunca digitado na ferramenta." % programa)
    return moldes[programa]


# ---------------------------------------------------------------------------
# AS RECUSAS DECLARADAS. Elas aparecem em TODA resposta, nao so quando alguem
# esbarra nelas -- a especificacao 1.7 manda dizer o que a F1 nao responde, e
# recusa que so aparece quando e acionada e recusa que ninguem le.
# ---------------------------------------------------------------------------

RECUSAS = [
    {
        "id": "ligacao-assimetrica",
        "frase": ("Ligação assimétrica a gente não recomenda: ela fecha valores no meio, "
                  "mas faz bobinas iguais receberem potência diferente uma da outra."),
    },
    {
        "id": "teto-de-quatro",
        "frase": ("Acima de 4 alto-falantes a instalação vira projeto e não cabe numa "
                  "resposta de duas linhas. O teto é 4 e está dito aqui, não escondido."),
    },
    {
        "id": "falantes-iguais",
        "frase": ("A conta supõe os alto-falantes todos iguais. Falantes diferentes entre "
                  "si a F1 não responde, em vez de supor igualdade em silêncio."),
    },
    {
        "id": "qual-e-o-melhor",
        "frase": ("Qual módulo é “melhor” a gente não responde. A F1 responde qual "
                  "fecha."),
    },
    {
        "id": "quanto-aguenta-de-verdade",
        "frase": ("Quanto o falante aguenta acima do que o fabricante declara também não: "
                  "essa é a pergunta que o fórum responde e que não tem fonte."),
    },
]


# ---------------------------------------------------------------------------
# HELPERS DE LEITURA DOS CASOS
# ---------------------------------------------------------------------------

def indexar_casos(doc_casos):
    """(rotulo da bobina, quantidade) -> caso."""
    return {(c["bobina"], c["alto_falantes"]): c for c in doc_casos["casos"]}


def quantidades_que_nunca_fecham(doc_casos):
    """Quantidades de alto-falante que NAO fecham em impedancia de modulo nenhuma,
    seja qual for a bobina.

    CONTADA, nunca digitada. Hoje ela devolve [3] -- o veredito que a enumeracao do
    bloco 2 achou e que nenhuma pagina medida publica. Se um dia o vocabulario de
    impedancia de modulo mudar e tres passar a fechar, a frase da tela some sozinha,
    em vez de continuar afirmando o que era verdade no dia em que foi escrita.
    """
    por_quantidade = {}
    for c in doc_casos["casos"]:
        por_quantidade.setdefault(c["alto_falantes"], []).append(c)
    saida = []
    for n in sorted(por_quantidade):
        if all(not c["fecha_com_modulo_de"] for c in por_quantidade[n]):
            saida.append(n)
    return saida


def _palavra(n, singular, plural):
    return singular if n == 1 else plural


def _numero(token):
    """'0,5' -> 0.5. O banco escreve numero com virgula, como o leitor le."""
    return float(token.replace(",", "."))


def _ohm(valor):
    """Plural de unidade em portugues: singular ate 1, plural acima. '0,5 ohm',
    '1 ohm', '1,333 ohms', '8 ohms'."""
    return "%s ohm%s" % (valor, "" if _numero(valor) <= 1 else "s")


def _lista(itens, juncao="e"):
    itens = list(itens)
    if len(itens) <= 1:
        return "".join(itens)
    return "%s %s %s" % (", ".join(itens[:-1]), juncao, itens[-1])


# O BANCO E ASCII, A TELA E ACENTUADA (fase 4b do playbook, e o mesmo desenho da
# Robometria). A descricao da ligacao vem de dados/impedancias-alcancaveis.json,
# que e banco e nasce sem acento; quem escreve a frase que o visitante le e esta
# camada. A tabela e EXPLICITA e a guarda abaixo falha alto: palavra nova sem
# acento no banco para a referencia, em vez de ir para a tela sem acento.
ACENTOS_DA_LIGACAO = {
    "serie": "série",
}

SEM_ACENTO_PROIBIDO_NA_TELA = (
    "serie", "impedancia", "impedancias", "modulo", "modulos", "potencia",
    "minimo", "maximo", "alcanca", "voce", "criterio", "numero", "numeros",
)


def _acentuar_ligacao(texto):
    saida = texto
    for ascii_, acentuada in ACENTOS_DA_LIGACAO.items():
        saida = saida.replace(ascii_, acentuada)
    for palavra in SEM_ACENTO_PROIBIDO_NA_TELA:
        if re.search(r"\b%s\b" % palavra, saida):
            raise SystemExit(
                "a descricao de ligacao %r voltou do banco com a palavra %r sem acento e "
                "esta camada nao sabe acentua-la. Acrescente o par em ACENTOS_DA_LIGACAO: "
                "texto de tela sai acentuado, e adivinhar seria pior." % (texto, palavra))
    return saida


# ---------------------------------------------------------------------------
# O BANCO DE MODULOS, VISTO PELA F1
# ---------------------------------------------------------------------------

def modulos_que_estabilizam(banco, ohms):
    return [m for m in banco if ohms in (m.get("impedancias_estaveis") or [])]


def prestacao_de_contas(banco, impedancia_alvo):
    """Secao 7 e especificacao 1.6: TODO modulo do banco e nomeado UMA vez em cada
    resposta -- ou na frase que o recomenda, ou numa linha que diz por que ficou
    de fora. A soma dos nomeados fecha o banco, e o total e CONTADO.
    """
    dentro, fora = [], []
    for m in banco:
        nome = "%s %s" % (m.get("marca", ""), m.get("modelo", ""))
        nome = nome.strip()
        estaveis = m.get("impedancias_estaveis") or []
        if impedancia_alvo is not None and impedancia_alvo in estaveis:
            dentro.append({
                "id": m.get("id"),
                "nome": nome,
                "rms_naquela_impedancia": (m.get("rms_por_impedancia") or {}).get(impedancia_alvo),
            })
        else:
            if not estaveis:
                motivo = "não declara em que impedância estabiliza"
            elif impedancia_alvo is None:
                motivo = "estabiliza em %s" % ", ".join(_ohm(x) for x in estaveis)
            else:
                motivo = "não estabiliza em %s: só em %s" % (
                    _ohm(impedancia_alvo), ", ".join(_ohm(x) for x in estaveis))
            fora.append({"id": m.get("id"), "nome": nome, "motivo": motivo})

    total = len(banco)
    nomeados = len(dentro) + len(fora)
    if total == 0:
        # A frase NAO cita caminho de arquivo do repositorio. Ela ja citou, e a regua
        # de acento da bancada pegou -- o defeito nao era o acento: era a pagina
        # falando com o visitante em vocabulario de quem a escreveu.
        frase = ("Módulos no nosso banco: 0. Nenhum ficou de fora por escolha — a gente "
                 "ainda não conferiu nenhum módulo com a ficha do fabricante na mão, e "
                 "enquanto não conferir não recomenda nenhum.")
    elif impedancia_alvo is None:
        frase = ("Módulos no nosso banco: %d, e os %d estão nomeados aqui." % (total, nomeados))
    else:
        frase = ("Módulos no nosso banco: %d. %d %s em %s; %d %s de fora, cada um com o "
                 "motivo ao lado." % (
                     total, len(dentro), _palavra(len(dentro), "fecha", "fecham"),
                     _ohm(impedancia_alvo), len(fora),
                     _palavra(len(fora), "ficou", "ficaram")))
    return {
        "modulos_no_banco": total,
        "nomeados": nomeados,
        "dentro": dentro,
        "fora": fora,
        "frase": frase,
    }


# ---------------------------------------------------------------------------
# O BLOCO DE COMPRA
# ---------------------------------------------------------------------------

def bloco_de_compra(esquema, impedancias_para_comprar, motivo_de_nao_ter):
    """O piso da secao 25.2 quando o banco esta VAZIO.

    O piso do ARQUIPELAGO.md e por ITEM: marca + modelo viram a palavra-chave. Com
    zero itens no banco nao existe item para gerar piso, e a saida honesta nao e
    inventar produto: e derivar a busca da PROPRIA RESPOSTA -- a impedancia em que
    o modulo precisa estabilizar. E a mesma manobra que a jornadafly registrou em
    14/09/2026, quando derivou o piso da cidade porque o item nao tinha ficha.

    E quando a resposta nao tem impedancia de modulo nenhuma (as montagens que nao
    fecham), o bloco NAO lista -- e diz por que, que e o que a secao 7 manda fazer
    em vez de deixar silencio com cara de defeito. Mandar quem nao tem montagem
    valida para uma busca de modulo seria vender uma coisa no lugar de outra.
    """
    molde = molde_do_piso(esquema, "shopee")
    pisos = []
    for ohms in impedancias_para_comprar:
        palavra = "modulo amplificador %s ohm" % ohms
        pisos.append({
            "programa": "shopee",
            "para_a_impedancia": ohms,
            "palavra_chave_busca": palavra,
            "url_busca_produto": molde.format(palavra_chave=quote_plus(palavra)),
            "url_busca": None,
            "rastreavel": False,
            "rel": "nofollow noopener",
            "degrau": 4,
        })
    if pisos:
        frase = ("Onde comprar: o módulo precisa estabilizar em %s. %s abaixo %s a busca da "
                 "loja por essa impedância — não é recomendação nossa, porque nenhum módulo "
                 "do nosso banco foi conferido ainda." % (
                     _lista([_ohm(p["para_a_impedancia"]) for p in pisos], "ou"),
                     _palavra(len(pisos), "O link", "Os links"),
                     _palavra(len(pisos), "é", "são")))
    else:
        frase = "Onde comprar: %s" % motivo_de_nao_ter
    return {
        "pisos": pisos,
        "itens_do_banco": [],
        "frase": frase,
        "o_que_este_piso_e": (
            "Busca DERIVADA da resposta, nao de um item do banco. O molde vem de "
            "esquema-banco.json -> piso_de_compra.moldes.shopee e nunca e digitado aqui."),
        "rastreavel": False,
        "por_que_nao_rastreavel": (
            "As etiquetas de afiliado desta ilha ainda nao existem (PROMPT.md: ohmetriaf1, "
            "ohmetriaf2, ohmetriaf3 ainda nao criadas). Busca CRUA sai sem rel=sponsored, "
            "porque sponsored declara relacao paga e ninguem paga por este clique. E divida "
            "de comissao, nao defeito de pagina."),
    }


# ---------------------------------------------------------------------------
# A RESPOSTA
# ---------------------------------------------------------------------------

def responder(caso, pedido, rms_do_falante=None, banco=None, esquema=None,
              doc_casos=None, constantes=None):
    """A resposta inteira da F1 para um estado de entrada.

    caso   -- um item de dados/impedancias-alcancaveis.json
    pedido -- impedancia em que o modulo estabiliza, do vocabulario, ou None
    """
    esquema = esquema if esquema is not None else carregar_esquema()
    doc_casos = doc_casos if doc_casos is not None else carregar_casos()
    banco = banco if banco is not None else carregar_modulos()["itens"]
    constantes = constantes if constantes is not None else carregar_constantes()

    alcancaveis = caso["impedancias_alcancaveis"]
    fecha_em = caso["fecha_com_modulo_de"]
    nunca_fecham = quantidades_que_nunca_fecham(doc_casos)
    n = caso["alto_falantes"]
    bobina = caso["bobina"]
    k = caso["total_de_bobinas"]
    falante = _palavra(n, "alto-falante", "alto-falantes")

    pedidos = {p["impedancia_de_modulo_pedida"]: p for p in caso["pedidos_que_nao_fecham"]}

    # --- veredito -----------------------------------------------------------
    ligacao_de = {a["ohms"]: _acentuar_ligacao(a["ligacao"]) for a in alcancaveis}
    lista_alc = _lista([_ohm(a["ohms"]) for a in alcancaveis])

    if pedido is None:
        codigo = "SEM_PEDIDO"
        impedancias_para_comprar = list(fecha_em)
        motivo_sem_piso = ("essa montagem não cai em impedância de módulo nenhuma, então não "
                           "tem módulo para procurar. Veja a linha acima antes de comprar "
                           "qualquer coisa.")
        if len(alcancaveis) == 1:
            # Bobina simples e um falante so: nao ha ligacao a escolher, e dizer
            # "depende de como voce liga" seria oferecer uma escolha que nao existe.
            unico = alcancaveis[0]["ohms"]
            frase = ("Aqui não tem ligação a escolher: %s %s. E %s %s impedância de módulo." % (
                _palavra(k, "a bobina dá", "as %d bobinas dão" % k), _ohm(unico), _ohm(unico),
                "é" if fecha_em else "não é"))
        elif fecha_em:
            frase = ("Essa montagem alcança %s, e qual deles você usa depende de como liga as "
                     "%d bobinas. %s %s %s de módulo." % (
                         lista_alc, k, _lista([_ohm(x) for x in fecha_em]),
                         _palavra(len(fecha_em), "é", "são"),
                         _palavra(len(fecha_em), "impedância", "impedâncias")))
        else:
            frase = ("Essa montagem alcança %s — e nenhum desses valores é impedância de "
                     "módulo. Com %d %s iguais não existe ligação simétrica que feche." % (
                         lista_alc, n, falante))
    elif pedido in ligacao_de:
        codigo = "FECHA"
        impedancias_para_comprar = [pedido]
        motivo_sem_piso = None
        frase = ("Fecha: com %s você tem %s, que é onde o seu módulo estabiliza." % (
            ligacao_de[pedido], _ohm(pedido)))
    else:
        p = pedidos[pedido]
        perto = p["mais_perto_que_fecha"]
        if perto is None:
            codigo = "NAO_FECHA_NENHUM"
            impedancias_para_comprar = []
            motivo_sem_piso = ("essa montagem não cai em impedância de módulo nenhuma, então "
                               "não tem módulo para procurar. Resolva a ligação primeiro.")
            frase = ("Não fecha em %s, e não fecha em impedância de módulo nenhuma. Essa "
                     "montagem só dá %s, e nenhum desses valores serve." % (
                         _ohm(pedido), lista_alc))
        elif p["abaixo_do_pedido"]:
            codigo = "NAO_FECHA_SO_ABAIXO"
            impedancias_para_comprar = []
            motivo_sem_piso = ("não tem o que procurar ainda. Com essa montagem, qualquer "
                               "módulo que estabilize só até %s vai receber menos ohm do que "
                               "aguenta. Mude a montagem ou mude o módulo antes de comprar." % _ohm(pedido))
            frase = ("Não ligue assim. Essa montagem não alcança %s nem nada acima: o maior "
                     "valor que ela dá e que é impedância de módulo é %s, abaixo do mínimo "
                     "que esse módulo estabiliza — e abaixo do mínimo é o que queima. Troque "
                     "o módulo ou mude a quantidade de %s." % (
                         _ohm(pedido), _ohm(perto), falante))
        else:
            codigo = "NAO_FECHA_SOBE"
            impedancias_para_comprar = [perto]
            motivo_sem_piso = None
            frase = ("Não fecha em %s. Essa montagem não alcança %s de jeito nenhum — o mais "
                     "perto que fecha é %s, com %s. Em %s o módulo entrega menos watt e roda "
                     "frio, e esse é o lado seguro de errar." % (
                         _ohm(pedido), _ohm(pedido), _ohm(perto), ligacao_de[perto], _ohm(perto)))

    # --- a linha do achado de tres, CONTADA --------------------------------
    nota_da_quantidade = None
    if n in nunca_fecham:
        nota_da_quantidade = (
            "%d %s iguais não fecham em impedância de módulo nenhuma, seja qual for a "
            "bobina — e isso vale para as %d montagens de %d que a gente enumerou. Com %d "
            "iguais você precisa de ligação assimétrica, que a gente não recomenda, ou de "
            "dois canais." % (
                n, falante, len([c for c in doc_casos["casos"] if c["alto_falantes"] == n]),
                n, n))

    # --- as ligacoes, uma a uma --------------------------------------------
    linhas = []
    for a in alcancaveis:
        atende = modulos_que_estabilizam(banco, a["ohms"])
        linhas.append({
            "ohms": a["ohms"],
            "ligacao": _acentuar_ligacao(a["ligacao"]),
            "e_impedancia_de_modulo": a["ohms"] in vocabulario(esquema, "impedancia_de_modulo"),
            "modulos_do_banco": [m.get("id") for m in atende],
            "frase_do_banco": (
                "%d %s do nosso banco %s em %s." % (
                    len(atende), _palavra(len(atende), "módulo", "módulos"),
                    _palavra(len(atende), "estabiliza", "estabilizam"), _ohm(a["ohms"]))
                if atende else
                "Nenhum módulo do nosso banco estabiliza em %s." % _ohm(a["ohms"])),
        })

    # --- potencia -----------------------------------------------------------
    criterio = next((c for c in constantes["constantes"]
                     if c["id"] == "criterio-rms-modulo-nao-passa-do-falante"), None)
    if criterio is None:
        raise SystemExit(
            "constantes.json nao tem criterio-rms-modulo-nao-passa-do-falante. A F1 precisa "
            "dele para saber que NAO pode afirmar teto de RMS -- sem o item, ela nao sabe que "
            "esta proibida.")
    if rms_do_falante is None:
        potencia = {"rms_do_falante": None, "frase": None, "criterio_status": criterio["status"]}
    elif criterio["status"] == "publicavel":
        potencia = {
            "rms_do_falante": rms_do_falante,
            "criterio_status": criterio["status"],
            "frase": ("O seu falante é %d W RMS, e o critério do fabricante já está lido: o "
                      "módulo pode ter até %d W RMS nessa impedância." % (
                          rms_do_falante, int(rms_do_falante * criterio["valor"]))),
        }
    else:
        potencia = {
            "rms_do_falante": rms_do_falante,
            "criterio_status": criterio["status"],
            "frase": ("O seu falante é %d W RMS. Quanto de RMS o módulo pode ter nessa "
                      "impedância, a gente ainda não afirma: o critério do fabricante voltou "
                      "de busca e o documento não foi aberto, e critério nesse estado não "
                      "entra em conta publicada. Quando houver módulo no banco, a página põe "
                      "os dois números lado a lado e deixa a conta com você." % rms_do_falante),
        }

    # --- como sabemos -------------------------------------------------------
    publicaveis = [c for c in constantes["constantes"]
                   if c["status"] in ("publicavel", "publicavel_como_desacordo")
                   and "F1" in (c.get("usada_em") or [])]
    como_sabemos = []
    for c in publicaveis:
        como_sabemos.append({
            "id": c["id"],
            "descricao": c["descricao"],
            "fonte": c["fonte"],
            "url": c.get("url"),
            "verificado_em": c["verificado_em"],
            "status": c["status"],
        })

    return {
        "entrada": {
            "alto_falantes": n,
            "bobina": bobina,
            "total_de_bobinas": k,
            "rms_do_falante": rms_do_falante,
            "impedancia_do_modulo_pedida": pedido,
        },
        "veredito": {"codigo": codigo, "frase": frase},
        "nota_da_quantidade": nota_da_quantidade,
        "ligacoes": linhas,
        "potencia": potencia,
        # A prestacao de contas (secao 7) e sobre a impedancia de que a RESPOSTA
        # fala. Sem pedido, a resposta nao fala de uma so: entao o alvo e None e
        # cada modulo do banco e nomeado com a impedancia em que ele estabiliza.
        "prestacao_de_contas": prestacao_de_contas(
            banco, None if codigo == "SEM_PEDIDO" else (
                impedancias_para_comprar[0] if impedancias_para_comprar else pedido)),
        "compra": bloco_de_compra(esquema, impedancias_para_comprar, motivo_sem_piso),
        "recusas": [dict(r) for r in RECUSAS],
        "como_sabemos": como_sabemos,
    }


# ---------------------------------------------------------------------------
# O DOMINIO INTEIRO
# ---------------------------------------------------------------------------

def conferir_casos_contra_o_esquema(doc_casos, esquema):
    """As montagens que a F1 responde tem de ser EXATAMENTE as bobinas do esquema.

    Sem isto, dados/impedancias-alcancaveis.json e o vocabulario do esquema sao duas
    metades contando a mesma coisa sem nunca se falarem -- e a secao 8 do
    ARQUIPELAGO.md diz o que acontece com essas: elas ficam verdes quando as duas
    erram juntas, e a que envelhece e sempre a que ninguem regenera. Esta linha
    nasceu da bateria de mutacoes: apagando impedancia_de_bobina do esquema, a F1
    continuava respondendo, feliz, a partir do banco de casos de ontem.
    """
    do_esquema = sorted(
        "%s ohm%s" % (t, "" if t == "1" else "s")
        for t in vocabulario(esquema, "impedancia_de_bobina"))
    dos_casos = sorted({c["bobina"] for c in doc_casos["casos"]})
    if do_esquema != dos_casos:
        raise SystemExit(
            "o banco de casos responde pelas bobinas %s e o vocabulario do esquema diz %s.\n"
            "Rode ferramentas/impedancias.py para regerar os casos: a F1 nao escolhe entre "
            "as duas metades, ela para." % (dos_casos, do_esquema))


def estados(doc_casos, esquema):
    conferir_casos_contra_o_esquema(doc_casos, esquema)
    """Todo estado de entrada da F1: cada montagem x cada pedido, mais o pedido vazio.

    Varrer a ENTRADA INTEIRA, nao o caso-ancora (secao 8): ferramenta de entrada
    variavel serve uma pagina por consulta, e a pagina sem consulta e so uma delas.
    """
    for caso in doc_casos["casos"]:
        for pedido in [None] + vocabulario(esquema, "impedancia_de_modulo"):
            yield caso, pedido


def todas_as_respostas(banco=None, esquema=None, doc_casos=None, constantes=None,
                       rms_do_falante=None):
    esquema = esquema if esquema is not None else carregar_esquema()
    doc_casos = doc_casos if doc_casos is not None else carregar_casos()
    banco = banco if banco is not None else carregar_modulos()["itens"]
    constantes = constantes if constantes is not None else carregar_constantes()
    return [responder(caso, pedido, rms_do_falante=rms_do_falante, banco=banco,
                      esquema=esquema, doc_casos=doc_casos, constantes=constantes)
            for caso, pedido in estados(doc_casos, esquema)]


def tabela_de_exemplos(respostas):
    """A tabela pre-renderizada da secao 5 do ARQUIPELAGO.md: casos ja resolvidos,
    servidos no HTML, cobrindo a faixa real de uso.

    E a metade que um modelo de linguagem le sem preencher formulario, e e onde a
    F2 do Clube do Mosaico falhou em tres de nove linhas. Uma linha por MONTAGEM,
    tirada do estado sem pedido -- que e o estado que responde a pergunta inteira.
    """
    linhas = []
    for r in respostas:
        if r["entrada"]["impedancia_do_modulo_pedida"] is not None:
            continue
        linhas.append({
            "alto_falantes": r["entrada"]["alto_falantes"],
            "bobina": r["entrada"]["bobina"],
            "total_de_bobinas": r["entrada"]["total_de_bobinas"],
            "alcanca": [l["ohms"] for l in r["ligacoes"]],
            "fecha_em": [l["ohms"] for l in r["ligacoes"] if l["e_impedancia_de_modulo"]],
            "veredito": r["veredito"]["frase"],
            "modulos_do_nosso_banco": r["prestacao_de_contas"]["modulos_no_banco"],
        })
    return linhas


def main():
    doc_casos = carregar_casos()
    esquema = carregar_esquema()
    if "--contar" in sys.argv:
        print("%d estados de entrada" % len(list(estados(doc_casos, esquema))))
        return 0
    casos = indexar_casos(doc_casos)
    r = responder(casos[("2+2 ohms", 2)], "1", rms_do_falante=500)
    print(json.dumps(r, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
