#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Valida o banco de especies da ilha Aquametria contra dados/esquema-especies.json.

Uso (a partir de ilhas/aquametria/):  python3 ferramentas/validar-especies.py [arquivo]

As regras E1 a E28 estao descritas em dados/esquema-especies.json. Este arquivo e a
versao executavel delas, pelo mesmo motivo do validador de produtos: regra que nao
roda vira decoracao. Imprime tambem quem passa no minimo_para_sugerir de cada
consumidor, que e a resposta pratica para "esta especie ja pode virar pagina?".

Codigo de saida: 0 se nao houver erro (avisos nao reprovam), 1 se houver.
"""

import importlib.util
import json
import os
import re
import sys
import unicodedata
from datetime import date, datetime
from urllib.parse import urlparse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ESQUEMA = os.path.join(RAIZ, "dados", "esquema-especies.json")
# Aceita um caminho no argv para que ferramentas/testar-validador-especies.py possa
# rodar as regras contra bancos deliberadamente corrompidos sem tocar no arquivo real.
ARQUIVO = sys.argv[1] if len(sys.argv) > 1 else "dados/especies-agua-doce.json"

def carregar_regua(nome):
    """Carrega uma regua compartilhada de ferramentas/ pelo nome do arquivo.

    Regua com travessao no nome nao e importavel por `import`, e renomea-la tiraria o
    arquivo da convencao que a bancada varre — entao o caminho e este, o mesmo que
    `teste-robots.py` e `conferir-robots-no-ar.py` usam desde 24/09/2026.
    """
    caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)), nome)
    spec = importlib.util.spec_from_file_location(nome.replace("-", "_")[:-3], caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


ID_VALIDO = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LIMITE_DIAS_REVALIDAR = 365
AMPLITUDE_QUE_E_TOLERANCIA = 20.0

erros = []
avisos = []


def erro(regra, alvo, texto):
    erros.append((regra, alvo, texto))


def aviso(regra, alvo, texto):
    avisos.append((regra, alvo, texto))


def carregar(caminho):
    with open(os.path.join(RAIZ, caminho), encoding="utf-8") as fp:
        return json.load(fp)


def preenchido(valor):
    if valor is None:
        return False
    if isinstance(valor, (list, dict)) and not valor:
        return False
    if isinstance(valor, dict):
        return any(v is not None for v in valor.values())
    return True


def intervalo(valor):
    return isinstance(valor, dict) and "min" in valor and "max" in valor


# A CONTAGEM DE CORPOS DE FONTE MORA EM `ferramentas/regua-corpos-de-fonte.py`,
# NUNCA AQUI (regra E26; a regua virou arquivo proprio em 16/10/2026).
#
# Em 15/10/2026 esta tabela saiu do hostname e passou a ser lida de `corpos_de_fonte`
# do esquema, e o cabecalho daquela mudanca diz "agora a regua e uma so". NAO ERA: ela
# era QUATRO, e so as DUAS QUE MEDEM foram consertadas. As duas que DECIDEM O QUE VAI A
# TELA — `gerar-catalogo-especies.py` e `teste-peixes.py` — continuaram contando corpo
# pelo prefixo da referencia, cegas a procedencia. Medido em 16/10/2026 no banco real:
# com uma fonte `indeterminada` (o usgs-nas, recusado em 15/10 para este mesmo
# registro) acrescentada ao `poecilia-reticulata`, ESTE validador contava 1 corpo e
# BARRAVA, e os outros dois contavam 2 e PUBLICAVAM. O cabecalho da regua traz a
# medicao inteira.
regua_corpos = carregar_regua("regua-corpos-de-fonte.py")
PROCEDENCIAS = regua_corpos.PROCEDENCIAS
carregar_corpos = regua_corpos.carregar
corpo_declarado = regua_corpos.corpo_declarado
corpos_de = regua_corpos.corpos_de
corpos_por_campo = regua_corpos.corpos_por_campo
# O `host_da_fonte` entra nesta lista porque a MENSAGEM do E26 o usa para nomear o host
# que nao esta declarado — e essa linha e o UNICO lugar do validador que o chama. Em
# banco limpo ela nunca roda, entao esquece-lo nao reprovava nada aqui: quem o pegou foi
# o `testar-validador-especies.py`, que corrompe o banco de proposito e exige que a regra
# reprove. Ele acusou NameError no caminho do E26, e nenhuma passada sobre o banco real
# teria acusado.
host_da_fonte = regua_corpos.host_da_fonte


# Numero por extenso conta como numero (regra E16). A fonte costuma escrever
# "grupo de pelo menos SEIS", e cobrar algarismo ali reprovaria transcricao fiel.
# As referencias do banco sao ASCII sem acento, por isso "tres" e nao "tres".
POR_EXTENSO = {
    "um": 1, "uma": 1, "dois": 2, "duas": 2, "tres": 3, "quatro": 4, "cinco": 5,
    "seis": 6, "sete": 7, "oito": 8, "nove": 9, "dez": 10, "onze": 11, "doze": 12,
    "treze": 13, "quatorze": 14, "catorze": 14, "quinze": 15, "dezesseis": 16,
    "dezessete": 17, "dezoito": 18, "dezenove": 19, "vinte": 20,
}
NUMERO_NO_TEXTO = re.compile(r"\d+(?:[.,]\d+)?")
PALAVRA_NO_TEXTO = re.compile(r"[a-z]+")


def numeros_no_texto(texto):
    """Todo numero que a fonte escreveu, em algarismo ou por extenso."""
    achados = set()
    for bruto in NUMERO_NO_TEXTO.findall(texto or ""):
        try:
            achados.add(round(float(bruto.replace(",", ".")), 4))
        except ValueError:
            pass
    for palavra in PALAVRA_NO_TEXTO.findall((texto or "").lower()):
        if palavra in POR_EXTENSO:
            achados.add(float(POR_EXTENSO[palavra]))
    return achados


def valores_numericos(campo, valor):
    """Os numeros que um campo publica: ele mesmo, ou cada lado do intervalo/base.

    DESCE EM OBJETO DENTRO DE OBJETO desde 15/10/2026, e o motivo e um mundo que
    o esquema passou a permitir na versao 7: o `comum` de porte_e_maximo_registrado
    e um objeto com dois numeros DENTRO de um campo que e objeto. Enquanto esta
    funcao olhava um nivel so, o E16 — que e quem confere que o numero do campo
    esta escrito no texto da fonte — passava por cima deles em silencio, dando
    por conferido o unico par de numeros do banco que ninguem tinha conferido.
    E a familia da regua que nao alcanca o mundo novo: ela nao errava, ela nao
    chegava — e portao que nao chega aprova por falta de evidencia.
    """
    if isinstance(valor, bool) or valor is None:
        return []
    if isinstance(valor, (int, float)):
        return [(campo, valor)]
    if isinstance(valor, dict):
        achados = []
        for chave, v in valor.items():
            achados.extend(valores_numericos("%s.%s" % (campo, chave), v))
        return achados
    return []


# O CHAO DECLARADO E UMA AFIRMACAO SOBRE UMA POPULACAO (esquema versao 5, 22/09/2026).
# Os termos sao ordenados: um aquario declarado para um grupo abriga um casal, e o
# contrario nao vale. `nao-declarado` fica FORA da ordem de proposito — ele nao e um
# nivel, e a ausencia de nivel: a fonte publicou a base como o minimo da especie sem
# nomear populacao nenhuma, e ai ela vale para o arranjo que o registro publica.
# O DESFECHO DE UM SEGUNDO CORPO QUE NAO ENTROU (E28, esquema versao 10). Fechado
# de proposito: "nao deu certo" nao se conta e nao se agrupa, e as quatro causas
# pedem coisas diferentes — `divergiu` pede DECISAO com data, `regua-diferente`
# pede outra LEITURA, `escopo` pede fonte que fale da MESMA populacao e
# `nao-cobre` pede OUTRO CORPO. A lista mora aqui e no esquema, e o validador
# confere as duas contra o banco.
# OS DOIS DESFECHOS QUE SAO DECISAO ADIADA, e por isso exigem data: `divergiu`
# (a fonte diz outro numero e alguem tem de escolher) e `confirmou-espera-data`
# (a fonte diz o mesmo numero e o que impede e o calendario). Os outros tres
# nao tem data para esperar: pedem outra leitura, outro escopo ou outro corpo.
PEDEM_DATA = ("divergiu", "confirmou-espera-data")

DESFECHOS_SEGUNDO_CORPO = ("divergiu", "regua-diferente", "escopo", "nao-cobre",
                           "confirmou-espera-data")

NIVEL_DO_CHAO = {"juvenis": 0, "um-exemplar": 1, "casal": 2, "grupo": 3}
ARRANJOS_DO_CHAO = tuple(NIVEL_DO_CHAO) + ("nao-declarado",)

# Como o arranjo que o registro PUBLICA vira populacao. Harem e cardume caem os dois
# em `grupo` porque os dois sao varios peixes no mesmo aquario — e e por isso que a
# base declarada para um casal nao serve nenhum dos dois.
POPULACAO_PUBLICADA = {
    "solitario": "um-exemplar",
    "casal": "casal",
    "cardume": "grupo",
    "grupo": "grupo",
    "harem": "grupo",
}

# As palavras que sustentam cada termo na clausula da fonte (regra E22). Sao as
# formas que os dois corpos deste banco usam de fato, nao um dicionario geral.
PALAVRAS_DO_ARRANJO = {
    "juvenis": ("juven",),
    "um-exemplar": ("sozinho", "um exemplar", "um adulto", "um macho", "um individuo"),
    "casal": ("casal",),
    "grupo": ("grupo", "cardume", "mantida em numero", "mantido em numero"),
}

# QUEM A FONTE MANDA NAO POR NA MESMA AGUA (regra E23, esquema versao 6,
# 23/09/2026). O vocabulario e fechado porque a traducao para a lingua do leitor
# mora num mapa so do PHP; e a palavra ao lado e o que a clausula transcrita tem
# de trazer para sustentar o termo, pelo mesmo desenho do PALAVRAS_DO_ARRANJO
# acima. Duas entradas, e as duas nasceram de registro real: o barbo sumatra
# (nadadeira longa, FishBase) e o papilocromis (aquario comunitario geral,
# Seriously Fish), este ultimo com a ficha NO AR ha nove dias servindo treze
# companheiros contra a propria frase que ela cita.
PALAVRAS_DA_RESTRICAO = {
    "nadadeiras-longas": ("nadadeira",),
    "comunitario-geral": ("comunitario",),
}

# O PORTE QUE AS TABELAS USAM E O MAXIMO REGISTRADO (regra E24, esquema versao 7,
# 15/10/2026). A palavra que a clausula tem de trazer para sustentar o campo — a
# base cientifica escreve "max length" e "max", o compendio escreve "maximo", e
# "max" cobre os tres sem casar com mais nada neste banco. Ela NAO basta sozinha:
# o E24 exige tambem o proprio numero de porte_adulto_cm na clausula, porque a
# transcricao do danio_margaritatus traz "lagoas rasas de no maximo 30 cm de
# profundidade" — clausula de maximo que fala da agua e nao do peixe.
PALAVRAS_DE_MAXIMO = ("max",)

# A unidade do tamanho COMUM e a da clausula, nunca convertida na digitacao: o
# compendio do barbo rosado escreve milimetro, e converter ao digitar tiraria o
# numero do campo do texto da fonte, que e justamente o que o E16 confere. A
# conversao mora aqui, num lugar so.
EM_CENTIMETRO = {"cm": 1.0, "mm": 0.1}


def sem_acento(texto):
    return "".join(c for c in unicodedata.normalize("NFD", str(texto or ""))
                   if unicodedata.category(c) != "Mn").lower()


def chao_serve(arranjos, convivencia):
    """O chao declarado cobre a populacao que o registro publica?

    `nao-declarado` cobre tudo por decisao escrita no esquema. Fora dele, o chao
    serve ate o MAIOR nivel que a fonte nomeou.
    """
    if "nao-declarado" in arranjos:
        return True
    populacao = POPULACAO_PUBLICADA.get(convivencia)
    if populacao is None:
        return True
    niveis = [NIVEL_DO_CHAO[a] for a in arranjos if a in NIVEL_DO_CHAO]
    if not niveis:
        return True
    return NIVEL_DO_CHAO[populacao] <= max(niveis)



def main():
    esquema = json.load(open(ESQUEMA, encoding="utf-8"))
    campos_esq = {c["campo"]: c for c in esquema["campos"]}
    obrigatorios = [c["campo"] for c in esquema["campos"] if c.get("obrigatorio")]
    isentos = set(esquema["campos_sem_fonte_exigida"]["lista"])
    carregar_corpos(esquema)
    origens = {n["origem"] for n in esquema["escada_de_fontes"]["niveis"]}
    status_por_origem = {n["origem"]: n["status"] for n in esquema["escada_de_fontes"]["niveis"]}
    dominio = esquema["dominio_por_campo"]
    campos_manutencao = set(dominio["manutencao"]["campos"])
    # A LISTA DE BEM-ESTAR SAI DO ESQUEMA desde 21/10/2026, e nao mais daqui. Ela
    # estava digitada nesta linha desde que a E9 nasceu, a UM arquivo de distancia
    # da tabela dominio_por_campo com que ela briga — e as duas brigaram pela
    # primeira vez em 21/10/2026, nos conflitos de frente minima do guppy (60 da
    # base cientifica contra 45 do compendio) e do gurami perola (120 contra 90).
    # A precedencia esta escrita ao lado da lista, em
    # dominio_por_campo.campos_de_bem_estar, com os tres numeros que a medem.
    campos_bem_estar = set(dominio["campos_de_bem_estar"]["lista"])
    global ACENTUACAO, ACENTUACAO_CAMPOS
    ACENTUACAO = dict(esquema["acentuacao_de_texto_de_tela"]["tabela"])
    # A LISTA DE CAMPOS DE TELA MORA NO ESQUEMA, ao lado da tabela, desde
    # 14/09/2026. Ate ali ela estava DIGITADA aqui num campo so, e o campo
    # vizinho — origem_geografica, que vai para a linha "De onde vem" de toda
    # ficha — ficou tres dias no ar sem UM acento em 15 de 15 registros, porque
    # a correcao de 12/09 acentuou o que a regra nomeava e mais nada.
    ACENTUACAO_CAMPOS = list(esquema["acentuacao_de_texto_de_tela"]["campos"])

    # AS DUAS COPIAS DO VOCABULARIO DO DESFECHO SE CONFEREM (E28, 16/10/2026).
    # A lista esta escrita no topo deste arquivo e no esquema, e e por isso que
    # ela pode ser conferida: regua que IMPORTA a lista do arquivo que ela mede
    # aprova qualquer palavra que alguem acrescentar la, que e o defeito que a
    # secao 8 do ARQUIPELAGO.md nomeia.
    voc_esq = tuple(sorted(esquema["desfechos_de_segundo_corpo"]["vocabulario"]))
    if voc_esq != tuple(sorted(DESFECHOS_SEGUNDO_CORPO)):
        erro("E28", "(esquema)", "o vocabulario de desfecho do esquema (%s) nao e o do "
                                 "validador (%s)" % (", ".join(voc_esq),
                                                     ", ".join(sorted(DESFECHOS_SEGUNDO_CORPO))))

    banco = carregar(ARQUIVO)
    registros = banco["especies"]
    hoje = date.today()
    vistos = set()

    for r in registros:
        rid = r.get("id", "<sem id>")

        # E1 - id
        if not ID_VALIDO.match(rid):
            erro("E1", rid, "id fora do kebab-case")
        if rid in vistos:
            erro("E1", rid, "id repetido no arquivo")
        vistos.add(rid)
        esperado = r.get("nome_cientifico", "").lower().replace(" ", "-")
        if esperado and esperado != rid:
            erro("E1", rid, "id nao corresponde ao nome cientifico (%s)" % esperado)

        # E2 - obrigatorios
        faltando = [c for c in obrigatorios if not preenchido(r.get(c))]
        if faltando:
            if r.get("status_registro") != "parcial":
                erro("E2", rid, "falta campo obrigatorio (%s) e o status nao e parcial"
                     % ", ".join(faltando))
            elif not r.get("observacao"):
                erro("E2", rid, "registro parcial sem observacao dizendo o que falta")

        # E26 - corpo de fonte nao declarado no esquema REPROVA, em vez de a contagem
        # herdar o palpite de que host diferente e corpo diferente. Vem ANTES do E14 e do
        # E15 de proposito: sem ele os dois contam um corpo que ninguem decidiu o que e.
        for f in r.get("fontes", []):
            if not f.get("url"):
                continue        # fonte sem url ja e erro E4; nao se cobra o corpo dela
            corpo = corpo_declarado(f["url"])
            ref = f.get("referencia", "<sem referencia>")[:40]
            if corpo is None:
                erro("E26", rid, "fonte '%s' tem corpo nao declarado em corpos_de_fonte do "
                                 "esquema (host %s)" % (ref, host_da_fonte(f["url"]) or "?"))
            elif corpo.get("procedencia") not in PROCEDENCIAS:
                erro("E26", rid, "corpo '%s' com procedencia fora do vocabulario: %s"
                     % (corpo.get("nome"), corpo.get("procedencia")))
            elif corpo["procedencia"] == "reproduz" and not corpo.get("reproduz"):
                erro("E26", rid, "corpo '%s' declarado como reprodutor sem dizer o que reproduz"
                     % corpo.get("nome"))

        # E14 / E15 - completo exige duas fontes de CORPOS distintos, nao so de urls distintas
        urls_fonte = {f.get("url") for f in r.get("fontes", []) if f.get("url")}
        corpos = corpos_de(r)
        if r.get("status_registro") == "completo" and len(corpos) < 2:
            erro("E14", rid, "status completo com %d corpo(s) de fonte distinto(s)" % len(corpos))
        if len(urls_fonte) >= 2 and len(corpos) < 2:
            aviso("E15", rid, "tem %d urls mas um corpo de fonte so (%s): espelho nao confere "
                              "espelho" % (len(urls_fonte), ", ".join(sorted(corpos)) or "nenhum"))

        # E4 - fontes bem formadas, e o indice campo -> origens
        sustentado = {}
        referencias_por_campo = {}
        for f in r.get("fontes", []):
            ref = f.get("referencia", "<sem referencia>")[:40]
            if f.get("origem") not in origens:
                erro("E4", rid, "fonte com origem fora da escada: %s" % f.get("origem"))
            elif f.get("status") != status_por_origem[f["origem"]]:
                erro("E4", rid, "fonte '%s' com status incoerente com a origem" % ref)
            if not f.get("url"):
                erro("E4", rid, "fonte '%s' sem url" % ref)
            if not f.get("verificado_em"):
                erro("E4", rid, "fonte '%s' sem verificado_em" % ref)
            for campo in f.get("campos", []):
                sustentado.setdefault(campo, []).append(f.get("origem"))
                referencias_por_campo.setdefault(campo, []).append(f.get("referencia") or "")

        # E3 - todo campo preenchido tem fonte
        for campo, spec in campos_esq.items():
            if campo in isentos:
                continue
            if preenchido(r.get(campo)) and campo not in sustentado:
                erro("E3", rid, "campo '%s' preenchido sem nenhuma fonte que o sustente" % campo)

        # E27 - QUANTOS CORPOS SUSTENTAM CADA CAMPO OBRIGATORIO (16/10/2026).
        # O E14 e o E15 contam os corpos que o REGISTRO cita. Essa pergunta e sobre o
        # sintoma — duas urls fingindo dois corpos — e aprova em silencio o mundo em que
        # o sintoma nao aparece: o registro cita dois corpos, o segundo sustenta so
        # campo OPCIONAL, e o nucleo obrigatorio inteiro continua apoiado num corpo so.
        # Medido no banco em 16/10/2026: seis registros estao nesse estado, e DOIS deles
        # sao `completo` — o E14 os aprovou por um corpo que nao sustenta campo
        # obrigatorio nenhum. Os outros dois nomeados (danio-margaritatus e
        # poecilia-reticulata) ja eram visiveis um andar acima, e e por isso que esta
        # regua nao substitui aquela: ela mede a CONDICAO onde as duas sao a mesma e
        # continua medindo onde elas se separam.
        nucleo = [c for c in obrigatorios if c not in isentos and c in sustentado]
        corpos_do_campo = corpos_por_campo(r)
        for campo in nucleo:
            if not corpos_do_campo.get(campo):
                # E3 ja cobra que o campo tenha FONTE; aqui se cobra que ele tenha
                # CORPO. Fonte de procedencia `indeterminada` e leitura e nao corpo
                # (E26), entao um campo obrigatorio sustentado so por ela passa no E3 e
                # nao tem quem o sustente. Hoje nenhum registro cai aqui, e o valor da
                # regra e justamente esse: ela fecha a porta antes de alguem entrar.
                erro("E27", rid, "campo obrigatorio '%s' tem fonte mas nenhum corpo "
                                 "contavel o sustenta (procedencia indeterminada nao e "
                                 "corpo)" % campo)
        if nucleo:
            corpos_do_nucleo = set()
            for campo in nucleo:
                corpos_do_nucleo |= corpos_do_campo.get(campo, set())
            if len(corpos_do_nucleo) < 2:
                detalhe = ", ".join("%s=%d" % (c, len(corpos_do_campo.get(c, ())))
                                    for c in nucleo)
                ociosos = sorted(corpos_de(r) - corpos_do_nucleo)
                cauda = ""
                if ociosos:
                    cauda = ("; o corpo %s e citado pelo registro e nao sustenta campo "
                             "obrigatorio nenhum" % ", ".join(ociosos))
                    if r.get("status_registro") == "completo":
                        cauda += (", entao o E14 aprovou 'completo' por um corpo que nao "
                                  "sustenta o nucleo")
                aviso("E27", rid, "os %d campo(s) obrigatorio(s) com fonte se apoiam em %d "
                                  "corpo(s) (%s) — %s%s"
                      % (len(nucleo), len(corpos_do_nucleo),
                         ", ".join(sorted(corpos_do_nucleo)) or "nenhum", detalhe, cauda))

        # E5 - varejo nao sustenta manutencao
        for campo, ors in sustentado.items():
            if campo in campos_manutencao and set(ors) == {"varejo"}:
                erro("E5", rid, "campo de manutencao '%s' sustentado so por varejo" % campo)

        # E6 - porte exige medida
        if preenchido(r.get("porte_adulto_cm")) and not r.get("porte_medida"):
            erro("E6", rid, "porte_adulto_cm sem porte_medida (SL ou TL)")

        # E7 - litro derivado gravado a mao
        vol = r.get("volume_minimo_declarado_L")
        if preenchido(vol):
            if "volume_minimo_declarado_L" not in sustentado:
                erro("E7", rid, "volume_minimo_declarado_L sem fonte que declare litro")
            base = r.get("base_minima_cm") or {}
            comp, larg = base.get("comprimento"), base.get("largura")
            if comp and larg:
                for altura in range(25, 61, 5):
                    if abs(comp * larg * altura / 1000.0 - vol) < 0.5:
                        erro("E7", rid, "volume_minimo_declarado_L bate com a base x %d cm: "
                                        "e derivado gravado a mao" % altura)
                        break

        # E8 - intervalos
        for campo in ("temperatura_C", "ph", "dureza_dgh"):
            v = r.get(campo)
            if intervalo(v) and v["min"] is not None and v["max"] is not None:
                if v["min"] > v["max"]:
                    erro("E8", rid, "%s com min maior que max" % campo)
                elif v["min"] == v["max"]:
                    aviso("E8", rid, "%s com min igual a max" % campo)

        # E16 - o numero do campo tem de estar no texto da fonte que declara o campo.
        # Campo e referencia sao duas escritas independentes do mesmo fato: a maquina usa
        # uma, o leitor le a outra. Quando divergem, alguem transcreveu, digitou ou editou
        # um lado so — e e o unico jeito de pegar isso sem abrir a pagina da fonte.
        for campo, textos in referencias_por_campo.items():
            if campo in isentos:
                continue
            numeros_da_fonte = set()
            for t in textos:
                numeros_da_fonte |= numeros_no_texto(t)
            for rotulo, valor in valores_numericos(campo, r.get(campo)):
                if round(float(valor), 4) not in numeros_da_fonte:
                    erro("E16", rid, "%s = %s nao aparece no texto de nenhuma fonte que declara "
                                     "'%s'" % (rotulo, valor, campo))

        # E9 / E10 - conflitos
        confs = r.get("conflitos") or []
        for c in confs:
            if c.get("tratamento") not in ("publicar-os-dois", "nivel-mais-alto-vence",
                                           "campo-vira-null", "intersecao-conservadora"):
                erro("E9", rid, "conflito em '%s' com tratamento invalido" % c.get("campo"))
            if c.get("campo") in campos_bem_estar:
                brutos = [v.get("valor") for v in c.get("valores", [])]
                numeros = [v for v in brutos if isinstance(v, (int, float))]
                if numeros and c.get("valor_conservador") != max(numeros):
                    erro("E9", rid, "conflito de bem-estar em '%s': o conservador tem de ser o maior (%s)"
                         % (c["campo"], max(numeros)))
        # E10: 'parcial' tambem vale quando o registro tem campo obrigatorio faltando.
        # Completude e divergencia sao fatos ortogonais e status_registro carrega um campo so:
        # nesse caso vale o mais restritivo, e 'parcial' e mais restritivo que 'conflito'
        # porque barra a pagina.
        aceitos_com_conflito = ["conflito", "revalidar"] + (["parcial"] if faltando else [])
        if confs and r.get("status_registro") not in aceitos_com_conflito:
            erro("E10", rid, "tem conflitos mas o status nao e conflito, revalidar nem parcial "
                             "com campo obrigatorio faltando")
        if r.get("status_registro") == "conflito" and not confs:
            erro("E10", rid, "status conflito sem nenhum conflito declarado")

        # E11 - idade do registro
        try:
            visto = datetime.strptime(r["verificado_em"], "%Y-%m-%d").date()
            if (hoje - visto).days > LIMITE_DIAS_REVALIDAR:
                aviso("E11", rid, "verificado ha mais de %d dias" % LIMITE_DIAS_REVALIDAR)
        except (KeyError, ValueError):
            erro("E11", rid, "verificado_em ausente ou fora do formato ISO")

        # E12 - cardume x convivencia
        card, conv = r.get("cardume_minimo"), r.get("convivencia")
        if preenchido(card) and card > 1 and conv not in ("cardume", "grupo"):
            erro("E12", rid, "cardume_minimo %s com convivencia '%s'" % (card, conv))
        if conv == "solitario" and preenchido(card):
            erro("E12", rid, "convivencia solitario com cardume_minimo preenchido")

        # E19 - a coleta que foi feita e NAO entrou (esquema de 22/09/2026).
        # Ate aqui a recusa vivia em prosa, e prosa nao se conta: a execucao
        # seguinte repete a busca, gasta a passada e chega a mesma recusa — ou,
        # pior, acha o numero sem achar o motivo pelo qual ele foi recusado e
        # grava. A regra com dentes e a ultima: campo recusado que hoje esta
        # PREENCHIDO obriga a entrada a dizer quem o superou e quando.
        for i, c in enumerate(r.get("coletas_recusadas", []) or []):
            onde = "coletas_recusadas[%d]" % i
            for obrig in ("em", "corpo", "metodo", "motivo"):
                if not str(c.get(obrig) or "").strip():
                    erro("E19", rid, "%s sem %s" % (onde, obrig))
            data = str(c.get("em") or "")
            if data:
                try:
                    if date.fromisoformat(data) > hoje:
                        erro("E19", rid, "%s com data no futuro (%s)" % (onde, data))
                except ValueError:
                    erro("E19", rid, "%s com data fora do formato ISO (%s)" % (onde, data))
            pretendidos = list(c.get("campos_pretendidos") or [])
            if not pretendidos:
                erro("E19", rid, "%s sem campos_pretendidos: recusa que nao diz o que "
                                 "deixou de preencher nao ensina nada" % onde)
            for campo in pretendidos:
                if campo not in campos_esq:
                    erro("E19", rid, "%s pretende '%s', que nao e campo deste esquema"
                         % (onde, campo))
                elif preenchido(r.get(campo)) and not (
                        str(c.get("superada_em") or "").strip()
                        and str(c.get("superada_por") or "").strip()):
                    erro("E19", rid, "%s recusou '%s' e o campo esta preenchido, sem "
                                     "superada_em e superada_por: a recusa e o dado "
                                     "dizem coisas contrarias" % (onde, campo))

        # E28 - O SEGUNDO CORPO QUE FOI BUSCADO E NAO ENTROU (esquema versao 10,
        # 16/10/2026).
        #
        # A E19 cuida da coleta que nao entrou em campo VAZIO e tem dentes nisso:
        # recusa de campo preenchido e erro, porque a recusa e o dado diriam
        # coisas contrarias. O terceiro caso apareceu inteiro no dia em que a E27
        # passou a contar corpo POR CAMPO: o campo esta preenchido por UM corpo, a
        # execucao vai buscar o SEGUNDO e o segundo nao entra. Sem lugar para
        # isso, o achado vira prosa no REGISTRO.md e a execucao seguinte refaz a
        # mesma busca e bate na mesma parede.
        #
        # A FRONTEIRA ENTRE AS DUAS LISTAS E ESCRITA AQUI, NAS DUAS DIRECOES: a
        # E19 reprova recusa de campo preenchido e a E28 reprova segundo corpo de
        # campo vazio. Uma so das duas metades deixaria a execucao escolher a
        # lista pelo gosto, e duas listas que aceitam o mesmo registro nao contam
        # duas coisas diferentes — contam a mesma coisa duas vezes.
        #
        # E a regra com dentes e a ultima: `divergiu` sem `decidir_em` e decisao
        # adiada sem data, que e decisao perdida; e `decidir_em` vencido sem
        # superada_* vira AVISO, porque a divergencia envelhece calada enquanto a
        # tela continua publicando um numero so. E a mesma licao da 25.4-b.3 do
        # contrato, do lado do banco de especies.
        for i, c in enumerate(r.get("segundo_corpo_nao_entrou", []) or []):
            onde = "segundo_corpo_nao_entrou[%d]" % i
            for obrig in ("em", "corpo", "url", "metodo", "o_que_a_fonte_declara",
                          "motivo", "o_que_destravaria"):
                if not str(c.get(obrig) or "").strip():
                    erro("E28", rid, "%s sem %s" % (onde, obrig))
            data = str(c.get("em") or "")
            if data:
                try:
                    if date.fromisoformat(data) > hoje:
                        erro("E28", rid, "%s com data no futuro (%s)" % (onde, data))
                except ValueError:
                    erro("E28", rid, "%s com data fora do formato ISO (%s)" % (onde, data))
            desfecho = str(c.get("desfecho") or "")
            if desfecho not in DESFECHOS_SEGUNDO_CORPO:
                erro("E28", rid, "%s com desfecho '%s' fora do vocabulario (%s)"
                     % (onde, desfecho, ", ".join(sorted(DESFECHOS_SEGUNDO_CORPO))))
            alvos = list(c.get("campos") or [])
            if not alvos:
                erro("E28", rid, "%s sem campos: segundo corpo que nao diz de qual campo "
                                 "ele seria nao ensina nada" % onde)
            for campo in alvos:
                if campo not in campos_esq:
                    erro("E28", rid, "%s cita '%s', que nao e campo deste esquema"
                         % (onde, campo))
                elif not preenchido(r.get(campo)):
                    erro("E28", rid, "%s cita '%s' e o campo esta VAZIO: segundo corpo e de "
                                     "campo que ja tem o primeiro — campo vazio e coleta "
                                     "recusada, e o lugar dela e coletas_recusadas (E19)"
                         % (onde, campo))
            decidir = str(c.get("decidir_em") or "").strip()
            superada = (str(c.get("superada_em") or "").strip()
                        and str(c.get("superada_por") or "").strip())
            if desfecho in PEDEM_DATA and not decidir and not superada:
                erro("E28", rid, "%s tem desfecho '%s' e nao declara decidir_em: o que nao "
                                 "entrou hoje por decisao adiada precisa da data da decisao, "
                                 "senao a decisao se perde" % (onde, desfecho))
            if decidir:
                try:
                    prazo = date.fromisoformat(decidir)
                except ValueError:
                    erro("E28", rid, "%s com decidir_em fora do formato ISO (%s)"
                         % (onde, decidir))
                else:
                    if prazo <= hoje and not superada:
                        aviso("E28", rid, "%s tem decidir_em %s, que ja chegou, e a divergencia "
                                          "continua nao declarada: a tela segue publicando um "
                                          "numero so" % (onde, decidir))

        # E18 - o teto da faixa de grupo (esquema versao 4, 14/09/2026)
        #
        # A fonte do gurami mel escreve "nao menos que 4 a 6 exemplares": o piso
        # mora em cardume_minimo e o teto neste campo. Teto SEM piso nao e faixa
        # e teto <= piso e faixa invertida — as duas fariam a ficha publicar uma
        # recomendacao que a fonte nao fez, que e o mesmo defeito do numero de
        # tela digitado, so que gravado no banco.
        teto = r.get("cardume_recomendado_ate")
        if preenchido(teto):
            if not preenchido(card):
                erro("E18", rid, "cardume_recomendado_ate sem cardume_minimo: teto sem piso nao e faixa")
            elif teto <= card:
                erro("E18", rid, "cardume_recomendado_ate %s nao e maior que o cardume_minimo %s"
                     % (teto, card))

        # E17 - acentuacao de texto de tela
        #
        # nomes_populares_br e o unico campo deste banco que vai INTEIRO para a
        # tela: e o nome que a ficha imprime dezenas de vezes, o que a tabela da
        # categoria mostra e o que o leitor de tela le. O resto do arquivo e nota
        # interna e por isso e escrito sem acento — e foi por arrasto que este
        # campo nasceu sem acento tambem, e assim ficou tres levas, invisivel
        # porque as tres primeiras fichas eram nomes que o portugues nao acentua.
        #
        # A tabela mora no esquema e e DECLARADA, nao adivinhada: "parece que
        # falta acento" seria a heuristica por vizinhanca que a secao 8 do
        # contrato proibe. O que esta regra pega e o erro que ja foi achado uma
        # vez; o que ela nao pega esta escrito no proprio esquema.
        #
        # OS CAMPOS DE TELA SAO DOIS DESDE 14/09/2026, e ate ali esta regra
        # nomeava um so. `origem_geografica` vai para a linha "De onde vem" da
        # tabela de fontes de toda ficha, e estava sem UM acento em 15 de 15
        # registros que a declaram — no ar desde 12/09, em onze paginas. Regra
        # que nomeia um campo nao protege o campo vizinho, e o vizinho aqui
        # nasceu do mesmo arrasto: o resto do arquivo e nota interna e por isso
        # e escrito sem acento. A lista de campos mora no ESQUEMA, ao lado da
        # tabela, para as duas crescerem juntas.
        for campo in ACENTUACAO_CAMPOS:
            valores = r.get(campo)
            if valores is None:
                continue
            if not isinstance(valores, list):
                valores = [valores]
            for valor in valores:
                for token in str(valor).replace(",", " ").split(" "):
                    for pedaco in sorted(set([token] + token.split("-"))):
                        if pedaco in ACENTUACAO:
                            erro("E17", rid, "%s '%s' com '%s' sem acento; na tela e '%s'"
                                 % (campo, valor, pedaco, ACENTUACAO[pedaco]))


        # E20 / E21 / E22 - o chao declarado e a populacao para quem ele foi declarado
        #
        # O DEFEITO QUE FEZ ESTA REGRA NASCER ESTEVE OITO DIAS NO AR: a ficha do
        # apistogramma agassizi abria com "para um harem ... o seu aquario precisa
        # de 60 cm de frente por 30 cm de fundo", e os 30 cm de fundo vem do
        # compendio, que os declarou para UM CASAL. A proibicao ja estava escrita,
        # em maiusculas, no `observacao` daquele mesmo registro. Prosa nao barra
        # pagina; regra barra.
        chao = r.get("chao_declarado_para")
        base = r.get("base_minima_cm") or {}
        tem_base_dos_dois_lados = bool(base.get("comprimento") and base.get("largura"))
        if tem_base_dos_dois_lados and not chao:
            erro("E20", rid, "base_minima_cm com os dois lados e sem chao_declarado_para: "
                             "chao sem populacao e numero que a ficha promete a quem quiser")
        elif chao and not tem_base_dos_dois_lados:
            erro("E20", rid, "chao_declarado_para sem base_minima_cm dos dois lados: "
                             "escopo de um chao que nao existe")
        elif chao:
            arranjos = list(chao.get("arranjos") or [])
            frase = str(chao.get("frase") or "").strip()
            if not arranjos:
                erro("E20", rid, "chao_declarado_para com arranjos vazio")
            for a in arranjos:
                if a not in ARRANJOS_DO_CHAO:
                    erro("E20", rid, "chao_declarado_para com arranjo '%s' fora do vocabulario" % a)
            if "nao-declarado" in arranjos and len(arranjos) > 1:
                erro("E20", rid, "chao_declarado_para mistura 'nao-declarado' com outro termo: "
                                 "ou a fonte nomeou a populacao, ou nao nomeou")
            if not frase:
                erro("E20", rid, "chao_declarado_para sem frase: termo sem a clausula da fonte "
                                 "e palpite de quem digitou")
            else:
                # E22 - a clausula e trecho LITERAL da fonte que sustenta a base
                refs = [f.get("referencia") or "" for f in r.get("fontes", [])
                        if "base_minima_cm" in (f.get("campos") or [])]
                if not any(frase in ref for ref in refs):
                    erro("E22", rid, "a frase de chao_declarado_para nao e trecho literal de "
                                     "nenhuma fonte que sustente base_minima_cm")
                else:
                    texto = sem_acento(frase)
                    nomeados = [a for a, palavras in PALAVRAS_DO_ARRANJO.items()
                                if any(w in texto for w in palavras)]
                    if "nao-declarado" in arranjos:
                        if nomeados:
                            erro("E22", rid, "chao_declarado_para diz 'nao-declarado' e a clausula "
                                             "nomeia %s" % ", ".join(sorted(nomeados)))
                    else:
                        for a in arranjos:
                            if a in PALAVRAS_DO_ARRANJO and a not in nomeados:
                                erro("E22", rid, "chao_declarado_para diz '%s' e a clausula da fonte "
                                                 "nao traz nenhuma palavra que sustente isso" % a)
            # E21 - aviso: o arranjo publicado esta acima do chao declarado
            if arranjos and not chao_serve(arranjos, r.get("convivencia")):
                aviso("E21", rid, "o registro publica convivencia '%s' e o chao foi declarado para "
                                  "%s: a ficha NAO pode servir o fundo a essa populacao (quem executa "
                                  "essa metade e ferramentas/teste-peixes.py, contra o HTML servido)"
                      % (r.get("convivencia"), ", ".join(arranjos)))

        # E23 - a restricao de companhia que a fonte declarou EM PALAVRAS
        #
        # O DEFEITO QUE FEZ ESTA REGRA NASCER ESTAVA NO AR HA NOVE DIAS, e e pior
        # que o do chao declarado: la a proibicao morava na `observacao` do
        # registro, aqui ela mora na TRANSCRICAO DA FONTE QUE A PAGINA CITA. A
        # ficha do papilocromis servia treze companheiros de aquario enquanto a
        # frase do compendio, copiada tres linhas acima no mesmo registro, diz que
        # a especie nao e recomendada para o aquario comunitario geral.
        restr = r.get("restricoes_de_companhia")
        if restr is not None:
            if not isinstance(restr, list) or not restr:
                erro("E23", rid, "restricoes_de_companhia presente e vazia: lista vazia afirma que a "
                                 "fonte foi lida e nao declarou nada, e isso se escreve deixando o campo fora")
            else:
                refs = [f.get("referencia") or "" for f in r.get("fontes", [])
                        if "restricoes_de_companhia" in (f.get("campos") or [])]
                for item in restr:
                    tipo = str((item or {}).get("tipo") or "")
                    frase = str((item or {}).get("frase") or "").strip()
                    if tipo not in PALAVRAS_DA_RESTRICAO:
                        erro("E23", rid, "restricoes_de_companhia com tipo '%s' fora do vocabulario" % tipo)
                    if not frase:
                        erro("E23", rid, "restricoes_de_companhia sem frase: tipo sem a clausula da "
                                         "fonte e palpite de quem digitou")
                        continue
                    if not any(frase in ref for ref in refs):
                        erro("E23", rid, "a frase de restricoes_de_companhia nao e trecho literal de "
                                         "nenhuma fonte que declare restricoes_de_companhia em campos")
                    elif tipo in PALAVRAS_DA_RESTRICAO:
                        texto = sem_acento(frase)
                        if not any(w in texto for w in PALAVRAS_DA_RESTRICAO[tipo]):
                            erro("E23", rid, "restricoes_de_companhia diz '%s' e a clausula da fonte "
                                             "nao traz nenhuma palavra que sustente isso" % tipo)

        # E24 / E25 - O ESCOPO DO PORTE: o numero que as tabelas usam e o maximo
        # registrado, e ate a versao 7 do esquema a pagina nao tinha onde dizer isso.
        #
        # E A TERCEIRA VEZ NESTE EIXO que a proibicao morava em prosa: o
        # chao_declarado_para (versao 5) nasceu de uma proibicao escrita na
        # `observacao` do apistogramma, as restricoes_de_companhia (versao 6) de
        # uma escrita na transcricao que a propria pagina cita, e esta de uma
        # escrita na `observacao` do barbo rosado em 23/09/2026 — "a ficha tem de
        # publicar o numero da fonte COM a medida dele E dizer que porte maximo
        # registrado nao e porte esperado em cativeiro, senao a C8 dimensiona para
        # um peixe que ninguem tem". PROSA NAO BARRA PAGINA.
        pmr = r.get("porte_e_maximo_registrado")
        if pmr is not None:
            if not isinstance(pmr, dict):
                erro("E24", rid, "porte_e_maximo_registrado tem de ser objeto {frase, comum?}")
            else:
                porte = r.get("porte_adulto_cm")
                refs = [f.get("referencia") or "" for f in r.get("fontes", [])
                        if "porte_e_maximo_registrado" in (f.get("campos") or [])]
                frase = str(pmr.get("frase") or "").strip()
                if not preenchido(porte):
                    erro("E24", rid, "porte_e_maximo_registrado sem porte_adulto_cm: o escopo sem "
                                     "o numero nao qualifica nada")
                if not frase:
                    erro("E24", rid, "porte_e_maximo_registrado sem frase: o escopo sem a clausula "
                                     "da fonte e palpite de quem digitou")
                else:
                    if not any(frase in ref for ref in refs):
                        erro("E24", rid, "a frase de porte_e_maximo_registrado nao e trecho literal "
                                         "de nenhuma fonte que declare porte_e_maximo_registrado em campos")
                    texto = sem_acento(frase)
                    if not any(w in texto for w in PALAVRAS_DE_MAXIMO):
                        erro("E24", rid, "a clausula de porte_e_maximo_registrado nao traz nenhuma "
                                         "palavra de maximo: sem ela o campo afirma o que a fonte nao disse")
                    # O NUMERO, e ele e a metade que pega a clausula de maximo que
                    # fala de outra coisa. So a palavra deixaria passar a lagoa de
                    # "no maximo 30 cm de profundidade" do danio_margaritatus.
                    if preenchido(porte) and round(float(porte), 4) not in numeros_no_texto(frase):
                        erro("E24", rid, "a clausula de porte_e_maximo_registrado nao traz o proprio "
                                         "porte_adulto_cm (%s): clausula de maximo que nao fala deste "
                                         "numero nao o qualifica" % porte)

                comum = pmr.get("comum")
                if comum is not None:
                    if not isinstance(comum, dict):
                        erro("E24", rid, "porte_e_maximo_registrado.comum tem de ser objeto "
                                         "{de, ate, unidade, medida, frase}")
                    else:
                        de, ate = comum.get("de"), comum.get("ate")
                        unidade = comum.get("unidade")
                        medida = comum.get("medida")
                        fr_comum = str(comum.get("frase") or "").strip()
                        if not isinstance(de, (int, float)) or isinstance(de, bool) or de <= 0:
                            erro("E24", rid, "comum.de tem de ser numero maior que zero")
                        if ate is not None:
                            if not isinstance(ate, (int, float)) or isinstance(ate, bool):
                                erro("E24", rid, "comum.ate tem de ser numero ou null")
                            elif isinstance(de, (int, float)) and ate <= de:
                                erro("E24", rid, "comum.ate (%s) nao e maior que comum.de (%s): "
                                                 "teto que nao passa do piso nao e faixa" % (ate, de))
                        if unidade not in EM_CENTIMETRO:
                            erro("E24", rid, "comum.unidade '%s' fora de (cm, mm)" % unidade)
                        elif fr_comum and unidade not in sem_acento(fr_comum):
                            erro("E24", rid, "comum.unidade e '%s' e a clausula nao usa essa unidade: "
                                             "a unidade e a DA FONTE, nunca convertida na digitacao"
                                 % unidade)
                        if medida is not None and medida not in ("SL", "TL"):
                            erro("E24", rid, "comum.medida '%s' fora de (SL, TL, null)" % medida)
                        if not fr_comum:
                            erro("E24", rid, "comum sem frase: o numero do tamanho comum sem a "
                                             "clausula da fonte e palpite de quem digitou")
                        elif not any(fr_comum in ref for ref in refs):
                            erro("E24", rid, "a frase de comum nao e trecho literal de nenhuma fonte "
                                             "que declare porte_e_maximo_registrado em campos")
                        # TAMANHO COMUM QUE ALCANCA O MAXIMO NAO E TAMANHO COMUM.
                        # Mesma aritmetica do E18, e ela so fecha depois de
                        # converter — por isso a conversao mora numa funcao so.
                        if (isinstance(de, (int, float)) and not isinstance(de, bool)
                                and unidade in EM_CENTIMETRO and preenchido(porte)):
                            if de * EM_CENTIMETRO[unidade] >= float(porte):
                                erro("E24", rid, "o tamanho comum (%s %s) alcanca ou passa o porte "
                                                 "maximo (%s cm): nao e tamanho comum"
                                     % (de, unidade, porte))
                        # E25 - AS DUAS REGUAS, e ela e AVISO pelo mesmo desenho do
                        # E21: o dado esta certo e quem tem de obedecer e a PAGINA.
                        if medida is None or medida != r.get("porte_medida"):
                            aviso("E25", rid, "o maximo esta em %s e o tamanho comum em %s: os dois "
                                              "numeros estao em reguas diferentes e a ficha NAO pode "
                                              "servi-los como comparacao — ela publica os dois com o "
                                              "dono de cada um e diz que a regua do comum nao foi "
                                              "declarada (quem executa essa metade e "
                                              "ferramentas/teste-peixes.py, contra o HTML servido)"
                                  % (r.get("porte_medida"), medida if medida else "regua nao declarada"))

        # E13 - tolerancia disfarcada de recomendacao
        t = r.get("temperatura_C")
        if intervalo(t) and t["min"] is not None and t["max"] is not None:
            if (t["max"] - t["min"]) > AMPLITUDE_QUE_E_TOLERANCIA and not r.get("temperatura_e_tolerancia"):
                erro("E13", rid, "temperatura com amplitude de %.0f C sem temperatura_e_tolerancia"
                     % (t["max"] - t["min"]))

    # quem ja pode virar pagina, e quem alimenta cada calculadora
    print("== quem passa no minimo_para_sugerir ==")
    for consumidor, requisitos in esquema["minimo_para_sugerir"].items():
        if consumidor == "regra":
            continue
        aptos, barrados = [], []
        for r in registros:
            falta = []
            for req in requisitos:
                if req == "duas fontes distintas":
                    if len(corpos_de(r)) < 2:
                        falta.append("duas fontes de corpos distintos")
                elif req.startswith("cardume_minimo OU"):
                    if not preenchido(r.get("cardume_minimo")) and \
                       r.get("convivencia") not in ("solitario", "casal", "harem"):
                        falta.append("cardume_minimo ou convivencia solitario/casal/harem")
                elif req.startswith("temperatura_C com"):
                    if not preenchido(r.get("temperatura_C")) or r.get("temperatura_e_tolerancia"):
                        falta.append("temperatura de manutencao (a faixa e de tolerancia)")
                elif not preenchido(r.get(req)):
                    falta.append(req)
            if r.get("status_registro") in ("rascunho", "revalidar"):
                falta.append("status " + r["status_registro"])
            (barrados if falta else aptos).append((r["id"], ", ".join(falta)))
        print("  %-16s %d apto(s), %d barrado(s)" % (consumidor, len(aptos), len(barrados)))
        for rid, motivo in barrados:
            print("      - %-28s falta: %s" % (rid, motivo))

    print("\n== faixa de porte coberta ==")
    portes = sorted((r["porte_adulto_cm"], r["id"]) for r in registros
                    if preenchido(r.get("porte_adulto_cm")))
    if portes:
        print("  de %.1f cm (%s) a %.1f cm (%s)"
              % (portes[0][0], portes[0][1], portes[-1][0], portes[-1][1]))
    frentes = sorted({r["comprimento_minimo_aquario_cm"] for r in registros
                      if preenchido(r.get("comprimento_minimo_aquario_cm"))})
    print("  frentes minimas declaradas: %s cm" % ", ".join(str(f) for f in frentes))

    print("\n== resultado ==")
    print("  %d especies, %d erro(s), %d aviso(s)" % (len(registros), len(erros), len(avisos)))
    for regra, rid, texto in erros:
        print("  ERRO  [%s] %s: %s" % (regra, rid, texto))
    for regra, rid, texto in avisos:
        print("  aviso [%s] %s: %s" % (regra, rid, texto))
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
