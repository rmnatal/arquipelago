#!/usr/bin/env python3
"""
F2 — "QUANTOS KM ELE FAZ DE VERDADE?" — A REFERENCIA.

Este arquivo e o CEREBRO da F2: entrada -> resposta inteira, ja em frase
acentuada. O snippet PHP que vai ao ar e TRADUTOR dele, frase a frase, como a
Robometria faz entre cobertura-r1.py e robometria-r1.php e como a Ohmetria fez
na F1 dela. O motivo esta na secao 8 do ARQUIPELAGO.md: quem confere escreve a
propria regua, e a regua da DECISAO se escreve duas vezes de proposito — e o
que e FATO EXTERNO (os valores das constantes) mora num lugar so, que aqui e
dados/constantes.json, lido e nunca digitado.

O QUE ESTA REFERENCIA NAO FAZ, e esta e a metade que o leitor da pagina recebe:
ela NAO devolve km absoluto a partir de V e Ah. O degrau 3 da conta da
especificacao (consumo absoluto em Wh/km de patinete) esta `pendente` em
dados/constantes.json, e o status e LIDO daqui — nunca ha uma lista escrita
dentro deste arquivo dizendo o que esta pendente. Se a constante virar
publicavel um dia, este arquivo passa a oferecer o degrau 3 sem que uma linha de
logica mude; enquanto ela for pendente, a recusa da 2.4 e impressa nomeando a
causa, que e a secao 7 do contrato ("a recusa nomeia a causa que a pagina
mediu").

E A RECUSA MORA EM FUNCAO PURA, nao dentro do laco que a calcula: e a regra do
"produza o mundo" da secao 8 (Clube do Mosaico, 08/10/2026). `faixa_de_km()`
recebe a autonomia declarada e o fator ja resolvido e devolve a faixa ou a
recusa; a bancada a chama direto, com declarada ausente, com fator 1,0, com
declarada no limite inferior e com o mundo em que o degrau 3 existe — nenhum
desses mundos depende do banco nem do arquivo de constantes de hoje.
"""

import json
import os
from fractions import Fraction

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)   # regras/ fica na raiz da ilha; ver regras/LEIA.md

RELEVOS = ("plano", "misto", "ladeira")

# Nome da constante por relevo. O numero NUNCA aparece neste arquivo: ele e
# fato externo e mora em dados/constantes.json. `plano` e o denominador da
# medicao, logo 1,0 por definicao da propria razao — e isso e identidade, nao
# constante colhida, entao esta declarado aqui com o motivo ao lado.
CONSTANTE_DO_RELEVO = {
    "plano": None,  # 1,0 por definicao: o trecho plano e o denominador da razao
    "misto": "fator-relevo-misto",
    "ladeira": "fator-relevo-ladeira-contra-plano",
}


# --------------------------------------------------------------------------
# OS MOLDES DE FRASE, NUM LUGAR SO.
#
# A pagina responde em DOIS lugares: o HTML pre-renderizado (que o PHP serve e
# que a IA le sem preencher formulario) e a recomputacao no navegador quando a
# pessoa troca um campo. Se cada um escrevesse a propria frase, a pagina diria
# duas coisas diferentes para a mesma entrada, e nenhum portao veria — e a
# cicatriz da secao 8 e exatamente essa ("as duas metades nunca se falavam").
#
# Entao o molde e FATO EXTERNO as duas metades: mora aqui, viaja inteiro para
# dados/f2-respostas.json, e o navegador o preenche. O que continua escrito
# duas vezes de proposito e a DECISAO — qual molde vale em cada mundo —, porque
# e ali que a divergencia ensina algo (secao 8, "a fronteira em duas
# perguntas").
# --------------------------------------------------------------------------

MOLDES = {
    "wh": "{v} V \u00d7 {ah} Ah s\u00e3o {wh} Wh de bateria.",
    "km_plano": (
        "No plano a r\u00e9gua de relevo n\u00e3o desconta nada \u2014 ela \u00e9 1,0 por "
        "defini\u00e7\u00e3o, porque o trecho plano \u00e9 justamente o denominador da "
        "medi\u00e7\u00e3o. Ent\u00e3o aqui o n\u00famero do an\u00fancio fica como TETO, n\u00e3o "
        "como promessa: {teto} km \u00e9 o melhor caso."
    ),
    # ITEM 1 DO DESPACHO DE 30/10/2026. Este molde dizia "conte com {piso} a
    # {teto} km, e nao os {teto} km do anuncio" — e {teto} E a autonomia
    # declarada, ou seja a frase negava o topo da faixa que ela mesma acabou de
    # publicar. A ronda ofereceu duas saidas defensaveis; a escolhida foi a
    # SEGUNDA (a frase para de prometer que nao e a declarada), porque a
    # primeira — mexer no topo da faixa — exigiria um numero que NINGUEM mediu:
    # `faixa_de_km` deriva o piso de `declarada / fator`, e nao ha fonte para um
    # teto que nao seja a propria declarada. Inventar o topo para salvar a frase
    # seria a secao 10 ao contrario. Agora o molde diz o MESMO que o `km_plano`
    # ja dizia do numero do anuncio — que ele e TETO, o melhor caso — e aponta a
    # ponta da faixa que a pessoa deve esperar.
    #
    # E O TAMANHO DELA E MEDIDO, NAO ESCOLHIDO. A primeira versao deste conserto
    # tinha "e valem no plano" no fim, foi ao ar na revisao 22 e o portao da 32.5
    # REPROVOU: a frase virou 3 linhas e empurrou o primeiro botao de compra de
    # 1.380 px para 1.407, contra o teto de 1.400. Eu havia INFERIDO que ela
    # custava zero, subtraindo medicoes de outras variantes em vez de medir esta
    # — e a inferencia errou por uma linha. Esta versao foi MEDIDA na pagina
    # viva, a 390 px: 2 linhas, botao de volta a 1.380 px. A folga desta pagina
    # e de 20 px; frase que nasce aqui se mede antes de ser empurrada.
    "km_degradado": (
        "Com {relevo_frase}, conte com {piso} a {teto} km \u2014 os {teto} do an\u00fancio s\u00e3o o teto."
    ),
    "km_absoluto": "Com {wh} Wh e o consumo medido, conte com uns {piso} km.",
    "km_recusa": (
        "Sem a autonomia que o an\u00fancio declara, n\u00e3o d\u00e1 para dizer quantos km "
        "esta bateria faz \u2014 e a gente n\u00e3o inventa o n\u00famero. Falta a r\u00e9gua de "
        "quantos Wh um patinete gasta por km: a \u00fanica medi\u00e7\u00e3o de patinete que "
        "achamos est\u00e1 em peri\u00f3dico que n\u00e3o abre por aqui, e medi\u00e7\u00e3o de moto "
        "n\u00e3o serve para patinete. Informe os km do an\u00fancio no campo acima e a "
        "conta sai."
    ),
    "peso": (
        "Os seus {peso} kg n\u00e3o entram na conta: n\u00e3o achamos, em fonte que alcance, "
        "nenhuma r\u00e9gua de quanto cada quilo de quem pilota custa em Wh por km. "
        "Eles entram aqui, no que esperar da faixa."
    ),
    "peso_ladeira": "Com {peso} kg e ladeira, espere o PISO da faixa, n\u00e3o o meio dela.",
    "peso_acima_do_teto": (
        "E antes da autonomia tem uma pergunta mais dura: {peso} kg passam do maior "
        "limite de carga que a gente viu no varejo brasileiro ({teto_carga} kg). Veja se o "
        "modelo aguenta o seu peso antes de olhar km."
    ),
    "rotulo_km": "O que esperar no seu trajeto",
    "rotulo_wh": "A energia da bateria",
    "calibracao": (
        "Para calibrar a expectativa: numa medi\u00e7\u00e3o de 2025 de Rodrigo David "
        "Limaico Quinteros, na Universidade Polit\u00e9cnica Salesiana de Quito, o "
        "ve\u00edculo entregou {pct}% da autonomia que a ficha declarava (29,8 km "
        "medidos contra 60 km de ficha). N\u00e3o multiplicamos nada por esse "
        "n\u00famero \u2014 ele \u00e9 uma medi\u00e7\u00e3o, de um ve\u00edculo, numa rota, e de moto, n\u00e3o "
        "de patinete."
    ),
}

RELEVO_FRASE = {"misto": "um pouco de subida", "ladeira": "ladeira de verdade"}


def carregar_constantes(caminho=None):
    """Le dados/constantes.json e devolve {id: registro}."""
    caminho = caminho or os.path.join(ILHA, "dados", "constantes.json")
    with open(caminho, encoding="utf-8") as f:
        bruto = json.load(f)
    return {c["id"]: c for c in bruto["constantes"]}


def constante_publicavel(constantes, cid):
    """Devolve o valor SO se a constante estiver publicavel; senao None.

    O status e lido do arquivo. E a decisao de engenharia do bloco 2: nenhuma
    lista de pendencias e escrita dentro do codigo, porque lista escrita a mao
    envelhece calada no dia em que a constante destrava.
    """
    c = constantes.get(cid)
    if not c or c.get("status") != "publicavel":
        return None
    return c.get("valor")


def fator_do_relevo(constantes, relevo):
    """Multiplicador de consumo do relevo. Devolve (fator, id_da_constante).

    `plano` devolve Fraction(1) e id None: e identidade da propria razao.
    """
    if relevo not in RELEVOS:
        raise ValueError("relevo desconhecido: %r" % (relevo,))
    cid = CONSTANTE_DO_RELEVO[relevo]
    if cid is None:
        return Fraction(1), None
    valor = constante_publicavel(constantes, cid)
    if valor is None:
        return None, cid
    return Fraction(str(valor)), cid


def energia_wh(tensao_v, amperagem_ah):
    """Wh = V x Ah. Identidade de unidades, nao fonte.

    Devolve Fraction para a bancada poder discordar sem erro de ponto
    flutuante. Quem arredonda e a tela, uma vez, no fim.
    """
    return Fraction(str(tensao_v)) * Fraction(str(amperagem_ah))


def faixa_de_km(autonomia_declarada_km, fator, consumo_wh_por_km=None, wh=None):
    """A FUNCAO PURA ONDE A RECUSA MORA.

    Entra: a autonomia declarada (ou None), o fator de relevo ja resolvido, e —
    para o mundo em que o degrau 3 existir — o consumo absoluto e o Wh.
    Sai: um dicionario com `tem_km` e, quando tem, `piso_km` e `teto_km`; quando
    nao tem, `causa`, que e o nome da causa e nunca uma hipotese.

    Tres mundos, e os tres sao fabricaveis sem tocar no banco:
      - declarada informada            -> faixa degradada (degrau 2)
      - declarada ausente, degrau 3 ON -> faixa absoluta (degrau 3)
      - declarada ausente, degrau 3 OFF-> recusa com causa nomeada (2.4)
    """
    if fator is None:
        return {"tem_km": False, "causa": "fator_de_relevo_indisponivel", "degrau": None}

    if autonomia_declarada_km is not None:
        declarada = Fraction(str(autonomia_declarada_km))
        if declarada <= 0:
            return {"tem_km": False, "causa": "autonomia_declarada_nao_positiva", "degrau": None}
        piso = declarada / fator
        return {
            "tem_km": True,
            "degrau": 2,
            "piso_km": piso,
            "teto_km": declarada,
            "faixa_degenerada": piso == declarada,
            "base": "autonomia_declarada",
        }

    if consumo_wh_por_km is not None and wh is not None:
        consumo = Fraction(str(consumo_wh_por_km)) * fator
        if consumo <= 0:
            return {"tem_km": False, "causa": "consumo_nao_positivo", "degrau": None}
        km = Fraction(str(wh)) / consumo
        return {
            "tem_km": True,
            "degrau": 3,
            "piso_km": km,
            "teto_km": km,
            "faixa_degenerada": True,
            "base": "consumo_absoluto",
        }

    return {
        "tem_km": False,
        "causa": "sem_autonomia_declarada_e_degrau_3_pendente",
        "degrau": None,
    }


def _n(fr, casas=0):
    """Numero em portugues: milhar com ponto, decimal com virgula."""
    if casas == 0:
        inteiro = int(fr + Fraction(1, 2)) if fr >= 0 else -int(-fr + Fraction(1, 2))
        s = "{:,}".format(inteiro).replace(",", ".")
        return s
    q = Fraction(10) ** casas
    arred = int(fr * q + Fraction(1, 2)) / float(q)
    s = ("{:,.%df}" % casas).format(arred)
    return s.replace(",", "\x00").replace(".", ",").replace("\x00", ".")


def responder(tensao_v, amperagem_ah, peso_piloto_kg, relevo,
              autonomia_declarada_km=None, constantes=None):
    """A resposta inteira da F2, ja em frases acentuadas.

    O peso do piloto NAO entra em conta nenhuma, e isso esta declarado na
    resposta em vez de disfarcado: a 2.4 da especificacao diz que nenhuma regua
    de Wh/km por kg de condutor foi achada em fonte alcancavel. Ele escolhe a
    frase de ressalva e o convite para a F3.
    """
    constantes = constantes if constantes is not None else carregar_constantes()

    if relevo not in RELEVOS:
        raise ValueError("relevo desconhecido: %r" % (relevo,))
    for nome, v in (("tensao_v", tensao_v), ("amperagem_ah", amperagem_ah),
                    ("peso_piloto_kg", peso_piloto_kg)):
        if v is None or Fraction(str(v)) <= 0:
            raise ValueError("%s tem de ser positivo" % nome)

    wh = energia_wh(tensao_v, amperagem_ah)
    fator, cid_fator = fator_do_relevo(constantes, relevo)
    consumo = constante_publicavel(constantes, "consumo-absoluto-wh-por-km-patinete")
    faixa = faixa_de_km(autonomia_declarada_km, fator, consumo, wh)

    teto_carga = constante_publicavel(constantes, "teto-de-carga-do-mercado-brasileiro")
    calibracao = constante_publicavel(constantes, "calibracao-autonomia-declarada-contra-medida")

    # ---- camada 1: a energia. Sempre existe, e e a ferramenta funcionando. ----
    frase_wh = MOLDES["wh"].format(
        v=_n(Fraction(str(tensao_v))), ah=_n(Fraction(str(amperagem_ah)), 1), wh=_n(wh))

    # ---- camada 2: o km, ou a recusa que nomeia a causa ----
    frases_km = []
    if faixa["tem_km"] and faixa["degrau"] == 2:
        if faixa["faixa_degenerada"]:
            frases_km.append(MOLDES["km_plano"].format(teto=_n(faixa["teto_km"])))
        else:
            frases_km.append(MOLDES["km_degradado"].format(
                relevo_frase=RELEVO_FRASE[relevo],
                piso=_n(faixa["piso_km"]), teto=_n(faixa["teto_km"])))
    elif faixa["tem_km"] and faixa["degrau"] == 3:
        frases_km.append(MOLDES["km_absoluto"].format(
            wh=_n(wh), piso=_n(faixa["piso_km"])))
    else:
        frases_km.append(MOLDES["km_recusa"])

    # ---- a ressalva do peso: declarada como ressalva, nunca como conta ----
    peso = Fraction(str(peso_piloto_kg))

    # `peso_ladeira` fala do PISO DA FAIXA, entao ela so pode nascer onde existe
    # faixa com DUAS PONTAS. Sem esta guarda ela contradizia a recusa: com
    # ladeira e sem autonomia declarada, a caixa dizia "nao da para dizer
    # quantos km esta bateria faz" e a ressalva, logo abaixo, mandava "esperar o
    # PISO da faixa" — o piso de uma faixa que a pagina acabou de se recusar a
    # dar. E a MESMA FAMILIA do item 1 deste despacho (a pagina se desdizendo),
    # um andar abaixo, e nao estava no despacho: foi achada ao escrever o item 2.
    faixa_com_duas_pontas = bool(faixa["tem_km"]) and not faixa.get("faixa_degenerada")

    # A RESSALVA DO PESO MORA ABAIXO DO BLOCO DE COMPRA, E ELA DIFERENCIA.
    # O item 2 do despacho de 30/10/2026 deu duas saidas e a escolhida foi a
    # SEGUNDA — o peso sai da PROMESSA —, porque a primeira (a caixa dizer algo
    # sobre o peso informado) foi MEDIDA e NAO CABE: o primeiro botao de compra
    # da F2 estava a 1.380 px dos 1.400 que a 32.5 permite, e qualquer frase
    # nova na caixa custa 97 px fixos (custo de BLOCO, nao de linha — medido em
    # navegador a 390 px, com a frase curta e a longa dando o mesmo numero).
    # Nenhuma combinacao coube: a melhor, com a promessa encurtada e a frase
    # dentro do paragrafo do km, deu 1.411 px. Entao a pagina deixa de prometer
    # o que nao entrega, em vez de entregar mal o que prometia.
    frases_peso = [MOLDES["peso"].format(peso=_n(peso))]
    if relevo == "ladeira" and faixa_com_duas_pontas:
        frases_peso.append(MOLDES["peso_ladeira"].format(peso=_n(peso)))
    if teto_carga is not None and peso > Fraction(str(teto_carga)):
        frases_peso.append(MOLDES["peso_acima_do_teto"].format(
            peso=_n(peso), teto_carga=_n(Fraction(str(teto_carga)))))

    # ---- a calibracao: medicao de terceiro, nomeada, e nunca fator de calculo ----
    frases_calibracao = []
    if calibracao is not None:
        c = constantes["calibracao-autonomia-declarada-contra-medida"]
        frases_calibracao.append(MOLDES["calibracao"].format(
            pct=_n(Fraction(str(calibracao)), 1)))
        assert c["status"] == "publicavel"

    return {
        "entrada": {
            "tensao_v": float(tensao_v),
            "amperagem_ah": float(amperagem_ah),
            "peso_piloto_kg": float(peso_piloto_kg),
            "relevo": relevo,
            "autonomia_declarada_km": (None if autonomia_declarada_km is None
                                       else float(autonomia_declarada_km)),
        },
        "wh": wh,
        "wh_tela": _n(wh),
        "fator_relevo": fator,
        "fator_relevo_tela": _n(fator, 2) if fator is not None else None,
        "constante_do_fator": cid_fator,
        "faixa": faixa,
        "piso_km_tela": _n(faixa["piso_km"]) if faixa["tem_km"] else None,
        "teto_km_tela": _n(faixa["teto_km"]) if faixa["tem_km"] else None,
        "degrau_da_conta": faixa["degrau"],
        "frase_wh": frase_wh,
        "frases_km": frases_km,
        "frases_peso": frases_peso,
        "frases_calibracao": frases_calibracao,
    }


# --------------------------------------------------------------------------
# A PRESTACAO DE CONTAS DA SECAO 7, EM FUNCAO PURA SOBRE O BANCO JA LIDO.
#
# A regra: todo registro da categoria consultada aparece EXATAMENTE UMA VEZ,
# num grupo com nome proprio. Os grupos da 2.6 da especificacao sao quatro, por
# CAUSA, e nunca se fundem. A funcao recebe a lista de registros ja lida (fato
# externo num lugar so) e devolve os grupos — entao a bancada fabrica o mundo
# que o banco de hoje nao tem, inclusive o mundo em que um veiculo DECLARA V e
# Ah, que hoje nao existe em nenhum dos 17 registros.
# --------------------------------------------------------------------------

def _valor(campo):
    """Campo do banco: ou {'valor': x, ...} ou o valor cru."""
    if isinstance(campo, dict):
        return campo.get("valor")
    return campo


def grupos_de_compra(registros, wh_pedido, tolerancia=Fraction(20, 100)):
    """Agrupa os registros por CAUSA, para a prosa e para a vitrine.

    Devolve dict com as quatro chaves da 2.6, cada uma com uma lista. A soma das
    quatro mais `fora_do_banco` fecha o total de registros recebidos, e isso e
    afirmado aqui dentro — numero de tela nasce contado, nunca digitado.
    """
    g = {
        "cabem_no_wh": [],
        "de_outro_wh": [],
        "nao_declaram_v_ou_ah": [],
        "sem_saida_de_compra": [],
        "fora_do_banco": [],
    }
    for r in registros:
        if r.get("status") == "excluido_do_banco":
            g["fora_do_banco"].append(r)
            continue
        v = _valor(r.get("tensao_v"))
        a = _valor(r.get("amperagem_ah"))
        tem_saida = bool(((r.get("afiliado") or {}).get("url_busca")
                          or (r.get("afiliado") or {}).get("url_produto")))
        if v is None or a is None:
            # A causa mais comum nas fichas colhidas, e ela vem ANTES da causa
            # "sem link": o registro pode ter link e continuar sem declarar V/Ah.
            g["nao_declaram_v_ou_ah"].append(r)
            continue
        if not tem_saida:
            g["sem_saida_de_compra"].append(r)
            continue
        wh = energia_wh(v, a)
        alvo = Fraction(str(wh_pedido))
        if alvo <= 0:
            g["de_outro_wh"].append(r)
            continue
        if abs(wh - alvo) <= alvo * tolerancia:
            g["cabem_no_wh"].append(r)
        else:
            g["de_outro_wh"].append(r)

    soma = sum(len(v) for v in g.values())
    assert soma == len(registros), (
        "prestacao de contas furada: %d agrupados de %d recebidos" % (soma, len(registros)))
    return g


if __name__ == "__main__":
    import sys
    cs = carregar_constantes()
    casos = [
        (48, 20, 90, "misto", 60),
        (60, 20, 90, "ladeira", 70),
        (36, 10.4, 70, "plano", 25),
        (48, 20, 90, "misto", None),
    ]
    for c in casos:
        r = responder(*c, constantes=cs)
        print("--", c)
        print("  ", r["frase_wh"])
        for f in r["frases_km"]:
            print("  ", f)
    sys.exit(0)
