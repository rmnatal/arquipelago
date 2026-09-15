#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica se o banco da Ohmetria cumpre o contrato de dados/esquema-banco.json.

Roda sem dependencia e sem rede, a partir de ilhas/ohmetria/:

    python3 ferramentas/validar-banco.py

Sai com codigo 1 se qualquer invariante for violada. Ferramenta de bancada: nunca
e publicada no site.

POR QUE ELE EXISTE, e o que ele mede que as irmas nao medem.
O produto desta ilha e o RMS DECLARADO NAQUELA IMPEDANCIA. Os dois defeitos que o
bloco 1 mediu na SERP sao: um numero de potencia solto, sem dizer em que impedancia
vale, e a unidade nao declarada -- e o achado 0.1 do bloco 2 mostrou que o desacordo
de 2,7 vezes entre as paginas de topo era UMA confusao de unidade, nao tres opinioes.
Um banco que deixe entrar um campo rms escalar, ou um watt sem unidade declarada,
publica a ilha inteira cometendo o defeito que ela existe para corrigir.

AS CINCO COISAS QUE ELE FAZ E QUE NAO SAO "CONFERIR CAMPO OBRIGATORIO":

  1. COMPARA impedancias_estaveis COM AS CHAVES DE rms_por_impedancia NOS DOIS
     SENTIDOS. As duas metades contam a mesma coisa; a cicatriz da secao 8 e que
     duas metades assim ficam verdes quando erram juntas, entao a comparacao e
     obrigatoria e sabidamente nao basta -- por isso a monotonia abaixo, que le a
     mesma tabela por outro criterio.

  2. RECOMPUTA A MONOTONIA DA POTENCIA. Modulo entrega mais watt quando a impedancia
     CAI. rms_por_impedancia nao-crescente da menor impedancia para a maior e fisica,
     nao convencao -- e quando a leitura devolve o contrario, ou o numero foi
     transcrito errado ou dois numeros de UNIDADES diferentes foram postos na mesma
     tabela. E o defeito da ilha aparecendo dentro de um unico registro.

  3. COBRA O VOCABULARIO DE IMPEDANCIA DE MODULO NOS DOIS SENTIDOS, e essa e a
     correcao que este bloco trouxe. Modulo do banco fora do vocabulario e ERRO DURO
     DO ESQUEMA (a lista cresce numa linha; somer o modulo seria o banco escondendo o
     que mediu). E entrada do vocabulario sem modulo no banco e DIVIDA CONTADA, em
     vocabulario_sem_lastro: enquanto ela nao for zero, nenhuma frase desta ilha pode
     dizer que uma impedancia "nao existe no mercado" -- a frase verdadeira e
     "nenhum modulo do nosso banco".

  4. DERIVA O PISO DE BUSCA do molde do esquema com a palavra-chave e compara com o
     que esta gravado. URL de piso digitada a mao envelhece calada no dia em que o
     molde mudar (secao 8: numero de tela nasce contado, nunca digitado).

  5. LE AS LISTAS DE FORA DE SI. A lista de campos que exigem declaracao de origem
     vem do ESQUEMA (secao 26.2) e a faixa de Thiele-Small vem de constantes.json --
     e ele REPROVA SE QUALQUER UMA DAS DUAS CHAVES SUMIR. Regua que le a propria
     lista de um arquivo de dados aprova tudo, em silencio, no dia em que o arquivo
     perder a chave.

E ele e importavel: `validar(esquema, bancos, constantes)` devolve
(erros, avisos, resumo_calculado) sobre dicionarios em memoria. E assim que
ferramentas/mutacoes-banco.py PRODUZ os mundos que o banco ainda nao tem -- porque
verde sobre um banco de zero registros nao e medicao, e ausencia de contraexemplo
confundida com prova.
"""

import io
import json
import os
import re
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)

ESQUEMA = os.path.join(RAIZ, "dados", "esquema-banco.json")
CONSTANTES = os.path.join(RAIZ, "dados", "constantes.json")
PASTA_DADOS = os.path.join(RAIZ, "dados")

# Arquivos da pasta dados/ que NAO sao banco de produto. Qualquer outro .json de la
# tem de estar declarado por alguma entidade do esquema -- e o contrario tambem.
NAO_SAO_BANCO = ("esquema-banco.json", "constantes.json", "impedancias-alcancaveis.json",
                 # Saida derivada da F1 (bloco 4): e o dominio de resposta da
                 # ferramenta, gerado de ferramentas/f1-referencia.py e medido por
                 # ferramentas/teste-f1.py. Nao tem item, nao tem fabricante e nao
                 # tem procedencia propria -- cobra-lo como banco de produto seria
                 # medir a coisa errada com a regua certa.
                 "f1-respostas.json")


# ----------------------------------------------------------------------------
# leitura
# ----------------------------------------------------------------------------

def ler_json(caminho):
    return json.load(io.open(caminho, encoding="utf-8"))


def ohms(texto):
    """'0,5' -> 0.5. O banco escreve impedancia com virgula, como a tela mostra."""
    return float(str(texto).replace(",", "."))


def slugificar(texto):
    sem_acento = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", sem_acento.lower()).strip("-")


# ----------------------------------------------------------------------------
# a regua
# ----------------------------------------------------------------------------

def validar(esquema, bancos, constantes):
    """Devolve (erros, avisos, resumo). Nenhum acesso a disco: tudo em memoria."""
    erros = []
    avisos = []

    def erro(onde, msg):
        erros.append("%s: %s" % (onde, msg))

    # -- 5. as listas que moram FORA desta regua, e a reprovacao quando elas somem --

    exige_origem = esquema.get("campos_que_exigem_declaracao_de_origem")
    if not isinstance(exige_origem, dict) or not exige_origem.get("campos"):
        erro("esquema", "a chave campos_que_exigem_declaracao_de_origem sumiu ou esta vazia. "
                        "Sem ela esta regua aprovaria todo registro sem origem, em silencio (secao 26.2).")
        exige_origem = {"campos": [], "origens_legitimas": {}}

    origens_ok = set(exige_origem.get("origens_legitimas", {}).keys())
    if not origens_ok:
        erro("esquema", "campos_que_exigem_declaracao_de_origem.origens_legitimas esta vazia: "
                        "qualquer string passaria a valer como origem declarada.")

    faixa_ts = None
    for c in constantes.get("constantes", []):
        if c.get("id") == "faixa-de-validacao-thiele-small":
            faixa_ts = c.get("valor")
    if not isinstance(faixa_ts, dict) or not faixa_ts:
        erro("constantes", "a constante faixa-de-validacao-thiele-small sumiu de constantes.json. "
                           "Sem ela o portao de entrada de Thiele-Small aprova qualquer numero, "
                           "inclusive os Fs de 4 Hz e os Vas em cm3 que o PROMPT.md registra.")
        faixa_ts = {}

    vocabs = esquema.get("vocabularios", {})

    def vocab(nome):
        v = vocabs.get(nome, {}).get("valores")
        if not v:
            erro("esquema", "o vocabulario %s sumiu ou esta vazio." % nome)
            return []
        return v

    voc_imp_modulo = vocab("impedancia_de_modulo")
    voc_imp_bobina = vocab("impedancia_de_bobina")
    voc_unidade = vocab("unidade_de_potencia")
    voc_fonte_tipo = vocab("fonte_tipo")
    voc_leitura = vocab("canal_de_leitura")
    voc_programa = vocab("programa_afiliado")

    # nivel de cada fonte_tipo, lido da escada -- nunca digitado aqui
    nivel_de = {}
    for degrau in esquema.get("escada_de_fontes", {}).get("niveis", []):
        nivel_de[degrau["fonte_tipo"]] = degrau["nivel"]
    if not nivel_de:
        erro("esquema", "escada_de_fontes.niveis sumiu: o campo nivel de toda fonte ficaria sem com o que ser comparado.")

    leituras_que_publicam = set()
    for canal, texto in esquema.get("escada_de_fontes", {}).get("canais_de_leitura", {}).items():
        if "Sustenta publicavel true" in texto or "Unico canal que sustenta publicavel true" in texto:
            leituras_que_publicam.add(canal)
    if not leituras_que_publicam:
        erro("esquema", "nenhum canal de leitura declara sustentar publicavel true: "
                        "a regra do elo mais fraco ficaria sem lado forte.")

    moldes = esquema.get("piso_de_compra", {}).get("moldes", {})
    if not moldes:
        erro("esquema", "piso_de_compra.moldes sumiu: o piso de busca deixaria de ser derivado e passaria a ser digitado.")

    # -- os dois sentidos entre esquema e arquivos de banco --

    entidades = esquema.get("entidades", {})
    declarados = {}
    for nome, ent in entidades.items():
        arq = ent.get("arquivo_de_banco")
        if arq:
            declarados[arq] = nome
        elif not ent.get("embutida") and not ent.get("motivo_de_nao_ter_banco_ainda"):
            erro("esquema/%s" % nome, "entidade sem arquivo_de_banco, sem embutida e sem "
                                      "motivo_de_nao_ter_banco_ainda. Lacuna sem causa nomeada nao e dado.")

    for arq, nome in sorted(declarados.items()):
        if arq not in bancos:
            erro("esquema/%s" % nome, "declara o banco %s e o arquivo nao existe. "
                                      "Entidade mostrada sem arquivo de banco e promessa." % arq)
    for arq in sorted(bancos):
        if arq not in declarados:
            erro("dados", "%s existe e nenhuma entidade do esquema o declara. "
                          "Arquivo de banco sem entidade que o mostre e dado colhido que a tela nunca usa." % arq)

    # -- registro a registro --

    resumo = {
        "registros": 0,
        "publicaveis": 0,
        "nao_publicaveis": 0,
        "esperando_link_de_afiliado": 0,
        "intestaveis": 0,
        "sem_saida_de_compra": 0,
        "por_entidade": {},
        "impedancias_com_lastro": {},
        "vocabulario_sem_lastro": [],
    }

    lastro = dict((z, 0) for z in voc_imp_modulo)
    pares_de_bobina_usados = set()

    for arq in sorted(bancos):
        banco = bancos[arq]
        nome_ent = declarados.get(arq, "?")
        itens = banco.get("itens")
        if itens is None:
            erro(arq, "nao tem a chave itens. Banco sem lista de itens nao e banco.")
            continue
        if not itens and not banco.get("motivo_de_estar_vazio"):
            erro(arq, "esta vazio e nao diz por que. Banco vazio com causa nomeada e dado; "
                      "banco vazio calado e trabalho que ninguem sabe se foi feito.")
        resumo["por_entidade"][nome_ent] = len(itens)
        resumo["registros"] += len(itens)

        for item in itens:
            ident = item.get("id") or "<sem id>"
            onde = "%s/%s" % (nome_ent, ident)

            if not item.get("id"):
                erro(onde, "sem id.")
            elif item.get("marca") and item.get("modelo"):
                esperado = slugificar("%s %s" % (item["marca"], item["modelo"]))
                if item["id"] != esperado:
                    erro(onde, "o id nao e o slug de marca + modelo (esperado %s)." % esperado)
            for obrig in ("marca", "modelo"):
                if not item.get(obrig):
                    erro(onde, "sem %s." % obrig)

            # ---- declaracao de origem, lida do esquema ----
            for regra in exige_origem["campos"]:
                if nome_ent not in regra.get("vale_para", []):
                    continue
                caminho = regra["campo"].split(".")
                origem_caminho = regra["campo_da_origem"].split(".")
                alvo = item
                for p in caminho[:-1]:
                    alvo = alvo.get(p, {}) if isinstance(alvo, dict) else {}
                valor = alvo.get(caminho[-1]) if isinstance(alvo, dict) else None
                orig = item
                for p in origem_caminho[:-1]:
                    orig = orig.get(p, {}) if isinstance(orig, dict) else {}
                origem = orig.get(origem_caminho[-1]) if isinstance(orig, dict) else None
                if valor in (None, "", []):
                    erro(onde, "%s e obrigatorio e esta vazio." % regra["campo"])
                if origem in (None, "", []):
                    erro(onde, "%s exige %s e ele esta vazio. Sem origem declarada o registro nao nasce (secao 26)."
                         % (regra["campo"], regra["campo_da_origem"]))
                elif origem not in origens_ok:
                    erro(onde, "%s = %r nao e origem legitima. As tres sao: %s."
                         % (regra["campo_da_origem"], origem, ", ".join(sorted(origens_ok))))

            # ---- fonte ----
            fonte = item.get("fonte") or {}
            nivel = None
            if not fonte:
                erro(onde, "sem fonte. Um registro so tem um numero porque alguem publicou aquele numero.")
            else:
                if fonte.get("tipo") not in voc_fonte_tipo:
                    erro(onde, "fonte.tipo = %r fora do vocabulario." % fonte.get("tipo"))
                if fonte.get("leitura") not in voc_leitura:
                    erro(onde, "fonte.leitura = %r fora do vocabulario." % fonte.get("leitura"))
                for obrig in ("url", "titulo_ou_codigo", "data_leitura"):
                    if not fonte.get(obrig):
                        erro(onde, "fonte.%s vazio." % obrig)
                if fonte.get("data_leitura") and not re.match(r"^\d{4}-\d{2}-\d{2}$", str(fonte["data_leitura"])):
                    erro(onde, "fonte.data_leitura = %r nao esta em AAAA-MM-DD." % fonte["data_leitura"])
                nivel_esperado = nivel_de.get(fonte.get("tipo"))
                nivel = fonte.get("nivel")
                if nivel_esperado is not None and nivel != nivel_esperado:
                    erro(onde, "fonte.nivel = %r e a escada diz %r para o tipo %s. "
                               "O nivel e derivado do tipo, nunca digitado."
                         % (nivel, nivel_esperado, fonte.get("tipo")))
                    nivel = nivel_esperado

            # ---- elo mais fraco: quem pode ser publicavel ----
            publicavel = item.get("publicavel")
            if publicavel is None:
                erro(onde, "sem o campo publicavel.")
            pode = (nivel in (1, 2)) and (fonte.get("leitura") in leituras_que_publicam)
            if publicavel and not pode:
                erro(onde, "publicavel true com fonte de nivel %r lida por %r. "
                           "O nivel de um dado e o do elo mais fraco, e a LEITURA e um elo: "
                           "documento oficial colhido por busca continua sendo busca."
                     % (nivel, fonte.get("leitura")))
            if publicavel is False and not item.get("motivo_nao_publicavel"):
                erro(onde, "publicavel false sem motivo_nao_publicavel. Prosa nao se conta, e silencio menos ainda.")
            if publicavel:
                resumo["publicaveis"] += 1
            else:
                resumo["nao_publicaveis"] += 1

            # ---- potencia e unidade ----
            pot = item.get("potencia") or {}
            unidade = pot.get("unidade_declarada")
            if unidade is not None and unidade not in voc_unidade:
                erro(onde, "potencia.unidade_declarada = %r fora do vocabulario." % unidade)
            if publicavel and unidade != "rms":
                erro(onde, "publicavel true com unidade_declarada = %r. A ilha so publica RMS; "
                           "musical e pico entram no banco para o registro poder dizer que o numero que tem nao serve."
                     % unidade)

            # ---- o que so o MODULO tem ----
            if nome_ent == "MODULO":
                estaveis = item.get("impedancias_estaveis")
                tabela = item.get("rms_por_impedancia")
                if not estaveis:
                    erro(onde, "sem impedancias_estaveis.")
                if not isinstance(tabela, dict) or not tabela:
                    erro(onde, "sem rms_por_impedancia. Modulo com um RMS solto e o defeito que a ilha corrige, "
                               "nao um registro incompleto.")
                if estaveis and isinstance(tabela, dict) and tabela:
                    faltam_na_tabela = [z for z in estaveis if z not in tabela]
                    sobram_na_tabela = [z for z in tabela if z not in estaveis]
                    if faltam_na_tabela:
                        erro(onde, "impedancias_estaveis tem %s e rms_por_impedancia nao: as duas metades contam "
                                   "a mesma coisa e discordam." % ", ".join(faltam_na_tabela))
                    if sobram_na_tabela:
                        erro(onde, "rms_por_impedancia tem %s e impedancias_estaveis nao: as duas metades contam "
                                   "a mesma coisa e discordam." % ", ".join(sobram_na_tabela))

                    # monotonia: menos ohm, mais watt
                    ordenadas = sorted(tabela.keys(), key=ohms)
                    for a, b in zip(ordenadas, ordenadas[1:]):
                        if tabela[b] > tabela[a]:
                            erro(onde, "rms_por_impedancia cresce de %s ohm (%s W) para %s ohm (%s W). "
                                       "Modulo entrega MAIS potencia quando a impedancia CAI: ou o numero foi "
                                       "transcrito errado, ou dois numeros de unidades diferentes estao na mesma tabela."
                                 % (a, tabela[a], b, tabela[b]))

                    for z in estaveis:
                        if z not in voc_imp_modulo:
                            erro("esquema", "%s estabiliza em %s ohm e o vocabulario impedancia_de_modulo nao tem esse "
                                            "valor. O erro e do ESQUEMA, nao do modulo: a lista cresce numa linha e o "
                                            "modulo entra. Somer o modulo seria o banco escondendo o que mediu."
                                 % (onde, z))
                        else:
                            lastro[z] += 1

                for z, w in (tabela or {}).items():
                    if not isinstance(w, int) or w <= 0:
                        erro(onde, "rms_por_impedancia[%s] = %r nao e watt inteiro positivo." % (z, w))

            # ---- o que so o ALTO_FALANTE tem ----
            if nome_ent == "ALTO_FALANTE":
                imp = item.get("impedancia_bobinas")
                if imp not in voc_imp_bobina:
                    erro(onde, "impedancia_bobinas = %r fora do vocabulario." % imp)
                else:
                    esperado_bobinas = 2 if "+" in imp else 1
                    esperado_ohms = ohms(imp.split("+")[0])
                    if item.get("bobinas") != esperado_bobinas:
                        erro(onde, "bobinas = %r e a string %r diz %d. O campo derivado e gravado justamente para "
                                   "que esta comparacao exista." % (item.get("bobinas"), imp, esperado_bobinas))
                    if item.get("ohms_por_bobina") != esperado_ohms:
                        erro(onde, "ohms_por_bobina = %r e a string %r diz %s."
                             % (item.get("ohms_por_bobina"), imp, esperado_ohms))
                    pares_de_bobina_usados.add((esperado_bobinas, esperado_ohms))

                ts = item.get("thiele_small")
                if ts:
                    for campo, faixa in faixa_ts.items():
                        if campo not in ts:
                            erro(onde, "thiele_small sem %s, e a faixa de validacao o cobra." % campo)
                            continue
                        v = ts[campo]
                        if not isinstance(v, (int, float)) or not (faixa[0] <= v <= faixa[1]):
                            erro(onde, "thiele_small.%s = %r fora da faixa %s a %s. Valor fora da faixa e RECUSADO "
                                       "na entrada, nunca corrigido." % (campo, v, faixa[0], faixa[1]))

            # ---- piso de compra (25.2) ----
            afl = item.get("afiliado")
            if afl is None:
                erro(onde, "sem o bloco afiliado. Ele nasce PRESENTE em todo item, mesmo vazio.")
            else:
                programa = afl.get("programa")
                if programa not in voc_programa:
                    erro(onde, "afiliado.programa = %r fora do vocabulario." % programa)
                chave = afl.get("palavra_chave_busca")
                if not chave:
                    erro(onde, "afiliado.palavra_chave_busca vazia: o piso nao tem de onde nascer.")
                gravada = afl.get("url_busca_produto")
                if not gravada:
                    resumo["sem_saida_de_compra"] += 1
                    erro(onde, "sem afiliado.url_busca_produto. Item sem piso de busca nao e publicavel em "
                               "degrau nenhum (secao 25.2), e a frase 'link de loja em breve' e proibida.")
                elif chave and programa in moldes:
                    fabricada = (moldes[programa]
                                 .replace("{palavra_chave}", chave.replace(" ", "%20"))
                                 .replace("{palavra_chave_hifen}", chave.replace(" ", "-")))
                    if fabricada != gravada:
                        erro(onde, "afiliado.url_busca_produto gravada nao bate com a fabricada do molde.\n"
                                   "      gravada:   %s\n      do molde:  %s" % (gravada, fabricada))
                if not afl.get("url_busca"):
                    resumo["esperando_link_de_afiliado"] += 1
                intestavel = bool(afl.get("url")) and not afl.get("url_produto")
                if afl.get("intestavel") != intestavel:
                    erro(onde, "afiliado.intestavel = %r e o derivado diz %r (tem url: %r, tem url_produto: %r). "
                               "A divida sai de dentro da prosa e vira contagem."
                         % (afl.get("intestavel"), intestavel, bool(afl.get("url")), bool(afl.get("url_produto"))))
                if intestavel:
                    resumo["intestaveis"] += 1
                degrau = afl.get("degrau")
                if degrau not in (1, 2, 3, 4):
                    erro(onde, "afiliado.degrau = %r fora da escada 25.1." % degrau)
                if intestavel:
                    erro(onde, "tem afiliado.url (ficha) e nao tem afiliado.url_produto. "
                               "Sem a URL crua da ficha o teste de vida e IMPOSSIVEL, porque a 25.4 proibe "
                               "clicar no proprio link de afiliado para chegar la. Esta ilha nasceu depois "
                               "da 25.4-b e nao tem divida herdada: aqui isso e erro, nao divida.")

    # -- vocabulario sem lastro: divida contada, nunca silencio --
    resumo["impedancias_com_lastro"] = lastro
    resumo["vocabulario_sem_lastro"] = [z for z in voc_imp_modulo if lastro.get(z, 0) == 0]
    if resumo["vocabulario_sem_lastro"]:
        avisos.append(
            "vocabulario_sem_lastro: %s. Enquanto esta lista nao for vazia, NENHUMA frase da ilha pode dizer que "
            "uma impedancia 'nao existe no mercado' -- a unica frase verdadeira e 'nenhum modulo do nosso banco'."
            % ", ".join(resumo["vocabulario_sem_lastro"]))

    if resumo["esperando_link_de_afiliado"]:
        avisos.append("%d itens esperam link de afiliado (divida de comissao, nunca defeito de pagina)."
                      % resumo["esperando_link_de_afiliado"])
    if resumo["intestaveis"]:
        avisos.append("%d itens intestaveis: tem ficha de afiliado e nao tem url_produto, entao a ronda nao "
                      "consegue abrir a pagina para o teste de vida (25.4-b)." % resumo["intestaveis"])

    return erros, avisos, resumo


# ----------------------------------------------------------------------------
# a terceira conta: o banco contra a aritmetica ja entregue
# ----------------------------------------------------------------------------

def conferir_contra_o_gerador(bancos, casos_da_f1):
    """Todo alto-falante do banco tem de ser respondivel pela F1.

    Duas metades que nunca se falam sao o defeito mais caro deste repositorio. O
    banco grava (bobinas, ohms_por_bobina) e ferramentas/impedancias.py enumera o
    dominio de saida a partir das MESMAS duas coisas. Se o banco puder ter um falante
    que o gerador nao enumera, a F1 serve uma pagina sem resposta e nenhum dos dois
    lados reprova sozinho.
    """
    erros = []
    if casos_da_f1 is None:
        return erros
    enumerados = set()
    for caso in casos_da_f1.get("casos", []):
        token = caso["bobina"].split(" ohm")[0]          # '2+2 ohms' -> '2+2'
        z = ohms(token.split("+")[0])
        bobinas_por_falante = caso["total_de_bobinas"] // caso["alto_falantes"]
        enumerados.add((bobinas_por_falante, z))
    for arq, banco in bancos.items():
        for item in banco.get("itens", []):
            if "impedancia_bobinas" not in item:
                continue
            imp = item["impedancia_bobinas"]
            par = (2 if "+" in imp else 1, ohms(str(imp).split("+")[0]))
            if par not in enumerados:
                erros.append("ALTO_FALANTE/%s: bobina %s nao aparece em nenhum dos %d casos de "
                             "impedancias-alcancaveis.json. O banco nao pode ter falante que a F1 nao sabe responder."
                             % (item.get("id"), imp, len(casos_da_f1.get("casos", []))))
    return erros


# ----------------------------------------------------------------------------

def carregar_bancos():
    bancos = {}
    for nome in sorted(os.listdir(PASTA_DADOS)):
        if nome.endswith(".json") and nome not in NAO_SAO_BANCO:
            bancos["dados/" + nome] = ler_json(os.path.join(PASTA_DADOS, nome))
    return bancos


def main():
    esquema = ler_json(ESQUEMA)
    constantes = ler_json(CONSTANTES)
    bancos = carregar_bancos()

    erros, avisos, resumo = validar(esquema, bancos, constantes)

    caminho_casos = os.path.join(PASTA_DADOS, "impedancias-alcancaveis.json")
    casos = ler_json(caminho_casos) if os.path.exists(caminho_casos) else None
    erros += conferir_contra_o_gerador(bancos, casos)

    print("VALIDADOR DO BANCO - OHMETRIA")
    print("Esquema versao %s, %d entidades, %d arquivos de banco."
          % (esquema.get("versao_esquema"), len(esquema.get("entidades", {})), len(bancos)))
    print("")
    print("Registros: %d (%d publicaveis, %d nao publicaveis)"
          % (resumo["registros"], resumo["publicaveis"], resumo["nao_publicaveis"]))
    for ent, n in sorted(resumo["por_entidade"].items()):
        print("  %-14s %d" % (ent, n))
    print("Itens sem saida de compra (erro duro): %d" % resumo["sem_saida_de_compra"])
    print("Itens esperando link de afiliado:      %d" % resumo["esperando_link_de_afiliado"])
    print("Itens intestaveis:                     %d" % resumo["intestaveis"])
    print("Lastro por impedancia de modulo:       %s"
          % ", ".join("%s ohm: %d" % (z, n) for z, n in sorted(resumo["impedancias_com_lastro"].items(), key=lambda p: ohms(p[0]))))

    if avisos:
        print("\nAVISOS (%d) - divida contada, nao defeito:" % len(avisos))
        for a in avisos:
            print("  - %s" % a)

    if erros:
        print("\n%d ERRO(S):" % len(erros))
        for e in erros:
            print("  - %s" % e)
        sys.exit(1)

    print("\nSem erro. O banco cumpre o contrato do esquema.")


if __name__ == "__main__":
    main()
