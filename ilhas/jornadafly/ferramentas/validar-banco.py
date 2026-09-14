#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica se o banco da JornadaFly cumpre o contrato de dados/esquema-banco.json.

Roda sem dependencia e sem rede:

    python3 ferramentas/validar-banco.py

Sai com codigo 1 se qualquer invariante for violada. Ferramenta de bancada: nunca
e publicada no site.

POR QUE ELE EXISTE, e por que nesta ilha ele mede outra coisa que nas irmas.
O produto desta ilha e o preco DATADO, com a unidade declarada e a conta fechada
para o grupo. Os dois defeitos que os blocos 1 e 2 mediram em oito consultas e tres
continentes sao: ninguem data o preco, e a unidade do preco troca dentro da mesma
resposta sem aviso. Um banco que deixe entrar preco sem data, ou unidade sem dizer
de onde ela foi lida, publica a ilha inteira cometendo o defeito que ela existe
para corrigir.

AS QUATRO COISAS QUE ELE FAZ E QUE NAO SAO "CONFERIR CAMPO OBRIGATORIO":

  1. RECOMPUTA A RESOLUCAO DE DIVERGENCIA a partir das declaracoes e da escada de
     fontes, e reprova o valor resolvido que nao seja o da autoridade (quando ha) ou
     o MAXIMO das declaracoes (quando nao ha). E a proibicao de media virada em
     codigo: media nao se reconhece pelo nome, se reconhece por cair entre o minimo
     e o maximo sem ser nenhum dos dois.
  2. DERIVA O PISO DE COMPRA do molde do esquema com o slug da cidade e compara com
     o que esta gravado. URL de piso digitada a mao envelhece calada no dia em que o
     molde mudar (secao 8: numero de tela nasce contado, nunca digitado).
  3. LE A LISTA DE CAMPOS QUE EXIGEM declarada_por DO ESQUEMA, nunca de dentro de si
     (secao 26.2) — e REPROVA SE A CHAVE SUMIR. Regua que le a propria lista de um
     arquivo de dados aprova tudo, em silencio, no dia em que o arquivo perder a
     chave.
  4. COBRA A REGRA DO DOCUMENTO NOMEADO (nascida na carga de 14/09/2026, e tambem
     lida do esquema): fonte de nivel de autoridade que nao nomeia o documento que
     a sustenta nao deixa o registro `publicavel` — ele entra como
     `pendente_de_releitura`. A escada ja cobrava o elo mais fraco entre autoria,
     custodia e leitura, e faltava o quarto elo. A tarifa da gondola e nivel 3 e
     cita a Delibera 89/2023; a do Angkor e nivel 3 e voltou em duas passadas sem
     nenhum ato, tabela ou pagina de tarifa junto. Sao coisas diferentes, e ate
     esta regra o esquema nao tinha como dizer isso.

E ele e importavel: `validar(esquema, banco, constantes, hoje)` devolve
(erros, avisos, resumo_calculado) sobre dicionarios em memoria. E assim que
ferramentas/mutacoes-banco.py produz os mundos que o banco ainda nao tem.
"""

import copy
import datetime
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = os.path.join(BASE, "dados")

HEDGES = ("cerca de", "aproximadamente", "em torno de", "a partir de", "por volta de")
FRASE_PROIBIDA = "link de loja em breve"


def _carregar(nome):
    caminho = os.path.join(DADOS, nome)
    with open(caminho, encoding="utf-8") as fh:
        return json.load(fh)


def _e_data(valor):
    if not isinstance(valor, str):
        return False
    try:
        datetime.date.fromisoformat(valor)
        return True
    except ValueError:
        return False


def _textos(no):
    """Todo texto dentro de uma estrutura, para varredura de frase proibida."""
    if isinstance(no, str):
        yield no
    elif isinstance(no, dict):
        for k, v in no.items():
            yield k
            for t in _textos(v):
                yield t
    elif isinstance(no, list):
        for v in no:
            for t in _textos(v):
                yield t


def _maximo(valor):
    """Valor comparavel de uma declaracao: numero, ou o topo da faixa."""
    if isinstance(valor, (int, float)):
        return float(valor)
    if isinstance(valor, dict) and isinstance(valor.get("maximo"), (int, float)):
        return float(valor["maximo"])
    return None


def _minimo(valor):
    if isinstance(valor, (int, float)):
        return float(valor)
    if isinstance(valor, dict) and isinstance(valor.get("minimo"), (int, float)):
        return float(valor["minimo"])
    return None


def validar(esquema, banco, constantes=None, hoje=None):
    erros = []
    avisos = []
    hoje = hoje or datetime.date.today()

    def erro(msg):
        erros.append(msg)

    def aviso(msg):
        if msg not in avisos:
            avisos.append(msg)

    # ------------------------------------------------------------------
    # 1. O ESQUEMA ESTA INTEIRO?
    # A regua le a lista DELE (26.2). Se a chave sumir, tudo passa em silencio —
    # entao a ausencia da chave e erro duro, e e a primeira coisa conferida.
    # ------------------------------------------------------------------
    vocab = esquema.get("vocabularios")
    if not isinstance(vocab, dict) or not vocab:
        erro("esquema: `vocabularios` ausente ou vazio. Sem ele nenhum valor de "
             "vocabulario controlado pode ser conferido, e a regua aprovaria "
             "qualquer coisa em silencio.")
        vocab = {}

    for chave in ("unidade_de_preco", "declarada_por", "categoria", "tipo_de_operador",
                  "momento_do_dia", "canal_de_leitura", "moeda", "status_do_registro"):
        if not isinstance(vocab.get(chave), list) or not vocab.get(chave):
            erro("esquema: vocabularios.%s ausente ou vazio." % chave)

    exige = esquema.get("campos_que_exigem_declaracao_de_origem")
    campos_declarada_por = None
    if not isinstance(exige, dict) or not isinstance(exige.get("campos"), list) or not exige.get("campos"):
        erro("esquema: `campos_que_exigem_declaracao_de_origem.campos` ausente ou vazia. "
             "Esta e a lista da secao 26.2: sem ela a trava de origem do dado aprova "
             "todo registro, inclusive o proximo, e fica verde.")
    else:
        campos_declarada_por = exige["campos"]

    escada = esquema.get("escada_de_fontes", {}).get("niveis")
    niveis = {}
    if not isinstance(escada, list) or not escada:
        erro("esquema: `escada_de_fontes.niveis` ausente ou vazia. Sem escada, o nivel "
             "de uma fonte vira um numero que nao responde a ninguem — que e exatamente "
             "por onde o defeito do elo mais fraco entrou na Robometria.")
    else:
        for degrau in escada:
            niveis[degrau.get("nivel")] = degrau

    molde_piso = esquema.get("piso_de_compra", {}).get("molde")
    if not isinstance(molde_piso, str) or "{slug_plataforma}" not in molde_piso:
        erro("esquema: `piso_de_compra.molde` ausente ou sem {slug_plataforma}. O piso "
             "da 25.2 tem de ser DERIVADO da cidade; sem molde ele vira URL digitada.")
        molde_piso = None

    regra_div = esquema.get("regra_de_divergencia")
    if not isinstance(regra_div, dict) or not regra_div.get("media"):
        erro("esquema: `regra_de_divergencia` ausente ou sem a linha da media. A "
             "proibicao de media (secao 10) mora no esquema e e daqui que ela e cobrada.")

    # A regra do documento nomeado (nascida na carga de 14/09/2026). Ela tambem
    # mora no ESQUEMA e nao aqui dentro (26.2): se a chave sumir, autoridade de
    # ouvir falar volta a valer o mesmo que autoridade com ato nomeado, e a regua
    # fica verde sem medir nada.
    regra_doc = esquema.get("regra_do_documento_nomeado")
    niveis_de_autoridade = []
    status_sem_documento = None
    if not isinstance(regra_doc, dict) \
            or not isinstance(regra_doc.get("niveis_de_autoridade"), list) \
            or not regra_doc.get("niveis_de_autoridade") \
            or not regra_doc.get("status_quando_falta_documento"):
        erro("esquema: `regra_do_documento_nomeado` ausente ou incompleta. Sem ela, "
             "fonte de autoridade que nao nomeia o documento que a sustenta volta a "
             "sustentar registro `publicavel` — que e a distancia entre a tarifa da "
             "gondola, com ato citado, e a do Angkor, que duas passadas atribuiram ao "
             "vendedor oficial sem nenhuma delas trazer o ato.")
    else:
        niveis_de_autoridade = regra_doc["niveis_de_autoridade"]
        status_sem_documento = regra_doc["status_quando_falta_documento"]

    validade = esquema.get("validade_do_preco", {})

    if erros and campos_declarada_por is None:
        # Sem a lista, nao da para afirmar nada sobre os registros; o relatorio ja
        # nomeou a causa e insistir produziria cem erros derivados de um so.
        return erros, avisos, {}

    def em_vocab(chave, valor):
        return valor in vocab.get(chave, [])

    # ------------------------------------------------------------------
    # 2. CIDADES
    # ------------------------------------------------------------------
    cidades = {}
    for cidade in banco.get("cidades", []):
        cid = cidade.get("id")
        onde = "cidades/%s" % (cid or "?")
        if not cid:
            erro("%s: sem `id`." % onde)
            continue
        if cid in cidades:
            erro("%s: `id` repetido." % onde)
        cidades[cid] = cidade
        for campo in ("nome", "pais", "moeda_local", "slug_plataforma"):
            if not cidade.get(campo):
                erro("%s: sem `%s`." % (onde, campo))
        if not em_vocab("moeda", cidade.get("moeda_local")):
            erro("%s: `moeda_local` %r fora do vocabulario." % (onde, cidade.get("moeda_local")))
        if not _e_data(cidade.get("slug_plataforma_conferido_em")):
            erro("%s: `slug_plataforma_conferido_em` ausente ou nao e data. Sem a data, "
                 "o piso de compra e uma URL SUPOSTA, e piso suposto e pior que piso "
                 "ausente: ele parece conferido." % onde)

    # ------------------------------------------------------------------
    # 3. FONTES — o elo mais fraco (secao 10)
    # ------------------------------------------------------------------
    fontes = {}
    for fonte in banco.get("fontes", []):
        fid = fonte.get("id")
        onde = "fontes/%s" % (fid or "?")
        if not fid:
            erro("%s: sem `id`." % onde)
            continue
        if fid in fontes:
            erro("%s: `id` repetido." % onde)
        fontes[fid] = fonte

        nivel = fonte.get("nivel")
        degrau = niveis.get(nivel)
        if degrau is None:
            erro("%s: nivel %r nao existe na escada do esquema." % (onde, nivel))
            continue
        if fonte.get("origem") != degrau.get("origem"):
            erro("%s: `origem` %r nao bate com a origem que a escada da ao nivel %s (%r). "
                 "Conferir so o numero e por onde o defeito do elo mais fraco entra."
                 % (onde, fonte.get("origem"), nivel, degrau.get("origem")))
        if not em_vocab("canal_de_leitura", fonte.get("leitura")):
            erro("%s: `leitura` %r fora do vocabulario. Silencio nunca promove."
                 % (onde, fonte.get("leitura")))
        if degrau.get("exige_leitura_direta") and fonte.get("leitura") != "leitura_direta":
            erro("%s: o nivel %s exige leitura direta e a fonte declara `leitura` %r. "
                 "Autoria forte nao promove custodia nem leitura fracas."
                 % (onde, nivel, fonte.get("leitura")))
        if not fonte.get("autor"):
            erro("%s: sem `autor`." % onde)
        if fonte.get("documento") is None and not fonte.get("motivo_sem_documento"):
            erro("%s: `documento` null sem `motivo_sem_documento`. Resposta que nao cita "
                 "o documento que a sustenta nao e fonte, e parafrase (secao 8)." % onde)
        if fonte.get("url") is None and not fonte.get("motivo_sem_url"):
            erro("%s: `url` null sem `motivo_sem_url`." % onde)
        if not _e_data(fonte.get("data_leitura")):
            erro("%s: `data_leitura` ausente ou nao e data." % onde)

    fontes_usadas = set()

    # ------------------------------------------------------------------
    # 4. EXPERIENCIAS
    # ------------------------------------------------------------------
    ids = set()
    n_versoes = 0
    n_declaracoes = 0
    n_publicaveis = 0
    sem_saida = 0
    piso_nao_rastreavel = 0
    intestaveis = 0
    com_brl_convertido = 0
    sem_versao = 0
    vencidos = []

    for exp in banco.get("experiencias", []):
        eid = exp.get("id")
        onde = "experiencias/%s" % (eid or "?")
        if not eid:
            erro("%s: sem `id`." % onde)
            continue
        if eid in ids:
            erro("%s: `id` repetido." % onde)
        ids.add(eid)

        if not exp.get("nome"):
            erro("%s: sem `nome`." % onde)
        if not exp.get("entra_por"):
            erro("%s: sem `entra_por`. Todo registro diz por que esta no banco — o "
                 "criterio de entrada prefere operador privado sem tabela publica, e "
                 "quem entra por outro motivo nomeia o motivo." % onde)
        if not em_vocab("categoria", exp.get("categoria")):
            erro("%s: `categoria` %r fora do vocabulario." % (onde, exp.get("categoria")))
        if not em_vocab("status_do_registro", exp.get("status")):
            erro("%s: `status` %r fora do vocabulario." % (onde, exp.get("status")))

        cidade = cidades.get(exp.get("cidade"))
        if cidade is None:
            erro("%s: `cidade` %r nao existe em cidades[]. Sem cidade nao ha piso de "
                 "compra, porque o piso e DERIVADO dela." % (onde, exp.get("cidade")))

        operador = exp.get("operador") or {}
        if not operador.get("nome"):
            erro("%s: operador sem `nome`." % onde)
        if not em_vocab("tipo_de_operador", operador.get("tipo")):
            erro("%s: operador com `tipo` %r fora do vocabulario." % (onde, operador.get("tipo")))
        if operador.get("url") is None and not operador.get("motivo_sem_url"):
            erro("%s: operador com `url` null sem `motivo_sem_url`." % onde)

        for campo, motivo in (("temporada", "motivo_sem_temporada"),
                              ("faixa_etaria", "motivo_sem_faixa_etaria"),
                              ("imagem", "motivo_sem_imagem")):
            if campo not in exp:
                erro("%s: falta o campo `%s`. Ausencia de chave e esquecimento; null "
                     "com motivo e resposta." % (onde, campo))
            elif exp.get(campo) is None and not exp.get(motivo):
                erro("%s: `%s` null sem `%s`. Lacuna com causa nomeada e dado; lacuna "
                     "muda e defeito que ninguem ve." % (onde, campo, motivo))

        # ---------------- versoes
        versoes = exp.get("versoes") or []
        if not versoes:
            erro("%s: sem `versoes`. A F1 so oferece o que o banco conhece; "
                 "experiencia sem versao nao tem o que oferecer." % onde)
        vistos = set()
        precos_por_id = {}
        for versao in versoes:
            n_versoes += 1
            vid = versao.get("id")
            ondev = "%s/versoes/%s" % (onde, vid or "?")
            if not vid:
                erro("%s: sem `id`." % ondev)
            elif vid in vistos:
                erro("%s: `id` de versao repetido dentro da experiencia." % ondev)
            vistos.add(vid)

            if not versao.get("rotulo"):
                erro("%s: sem `rotulo`." % ondev)

            preco = versao.get("preco")
            if preco is None:
                if not versao.get("motivo_sem_preco"):
                    erro("%s: `preco` null sem `motivo_sem_preco`." % ondev)
            elif not isinstance(preco, (int, float)) or preco <= 0:
                erro("%s: `preco` %r nao e numero positivo." % (ondev, preco))
            precos_por_id[vid] = preco

            if not em_vocab("moeda", versao.get("moeda")):
                erro("%s: `moeda` %r fora do vocabulario." % (ondev, versao.get("moeda")))
            elif cidade is not None and versao.get("moeda") != cidade.get("moeda_local"):
                erro("%s: `moeda` %r nao e a moeda em que o operador desta cidade cobra "
                     "(%r). O banco guarda a moeda do operador, nunca uma convertida por "
                     "esta ilha — as constantes de cambio estao PENDENTES e constante "
                     "pendente e proibida em formula publicada (secao 10)."
                     % (ondev, versao.get("moeda"), cidade.get("moeda_local")))
                com_brl_convertido += 1

            unidade = versao.get("unidade_de_preco")
            if not em_vocab("unidade_de_preco", unidade):
                erro("%s: `unidade_de_preco` %r fora do vocabulario." % (ondev, unidade))

            # A trava da secao 26 aplicada ao campo que doi nesta ilha.
            for campo in campos_declarada_por:
                if campo not in versao:
                    erro("%s: falta o campo `%s`, que o esquema declara obrigatorio."
                         % (ondev, campo))
                    continue
                chave = "%s_declarada_por" % campo
                if versao.get(campo) is None:
                    if versao.get(chave) is not None:
                        erro("%s: `%s` e null e mesmo assim declara `%s`. Origem de um "
                             "valor que nao existe e afirmacao sobre nada."
                             % (ondev, campo, chave))
                    continue
                if not em_vocab("declarada_por", versao.get(chave)):
                    erro("%s: `%s` ausente ou fora do vocabulario (%r). O esquema exige "
                         "declaracao de origem para `%s`: sem uma das tres origens "
                         "legitimas o registro NAO nasce (secao 26.1)."
                         % (ondev, chave, versao.get(chave), campo))

            cap = versao.get("capacidade_maxima")
            if cap is None:
                if unidade != "por_pessoa":
                    erro("%s: `capacidade_maxima` null com unidade %r. Quando a unidade "
                         "nao e por pessoa, e a capacidade que produz o degrau: 6 pessoas "
                         "na gondola sao DUAS gondolas, e sem ela a conta do grupo nao "
                         "fecha." % (ondev, unidade))
            elif not isinstance(cap, int) or cap < 1:
                erro("%s: `capacidade_maxima` %r nao e inteiro maior que zero." % (ondev, cap))

            if "duracao_minutos" not in versao:
                erro("%s: falta `duracao_minutos`." % ondev)
            elif versao.get("duracao_minutos") is None and not versao.get("motivo_sem_duracao"):
                erro("%s: `duracao_minutos` null sem `motivo_sem_duracao`." % ondev)

            if not em_vocab("momento_do_dia", versao.get("momento_do_dia")):
                erro("%s: `momento_do_dia` %r fora do vocabulario."
                     % (ondev, versao.get("momento_do_dia")))

            for lista, motivo in (("inclui", "inclui_motivo_lista_vazia"),
                                  ("nao_inclui", "nao_inclui_motivo_lista_vazia")):
                if not isinstance(versao.get(lista), list):
                    erro("%s: `%s` ausente ou nao e lista." % (ondev, lista))
                elif not versao.get(lista) and not versao.get(motivo):
                    erro("%s: `%s` vazia sem `%s`. Lista vazia nao some da tela: ela diz "
                         "que o operador nao declara o que esta incluso, e isso e "
                         "informacao sobre o operador." % (ondev, lista, motivo))

            for acrescimo in versao.get("acrescimos") or []:
                ondea = "%s/acrescimos" % ondev
                if not acrescimo.get("o_que_e") or not acrescimo.get("declarado_como"):
                    erro("%s: acrescimo sem `o_que_e` ou sem `declarado_como`." % ondea)
                    continue
                frase = acrescimo["declarado_como"].lower()
                hedge = next((h for h in HEDGES if h in frase), None)
                if hedge and acrescimo.get("aproximado") is not True:
                    erro("%s: `declarado_como` diz %r e `aproximado` nao e true. O 'mais "
                         "ou menos' e da fonte e nao pode virar numero seco na tela."
                         % (ondea, hedge))
                if not hedge and acrescimo.get("aproximado") is True:
                    erro("%s: `aproximado` true mas a frase da fonte nao tem ressalva "
                         "nenhuma. Ressalva inventada tambem e invencao." % ondea)

            fid = versao.get("fonte")
            if fid not in fontes:
                erro("%s: `fonte` %r nao existe em fontes[]." % (ondev, fid))
            else:
                fontes_usadas.add(fid)
                if not _e_data(versao.get("data_leitura")):
                    erro("%s: `data_leitura` ausente ou nao e data. Preco sem data de "
                         "leitura nao existe nesta ilha — e o defeito mais grave que o "
                         "VOZ.md nomeia." % ondev)
                else:
                    origem = fontes[fid].get("origem") or ""
                    dias = int(validade.get("tarifa_de_poder_publico_dias", 180)) \
                        if "poder-publico" in origem \
                        else int(validade.get("operador_privado_dias", 60))
                    lido = datetime.date.fromisoformat(versao["data_leitura"])
                    if (hoje - lido).days > dias:
                        vencidos.append("%s (lido em %s, validade de %d dias)"
                                        % (ondev, versao["data_leitura"], dias))

            if not versao.get("declarado_como"):
                erro("%s: sem `declarado_como`. Sem a frase da fonte, a tela parafraseia "
                     "em vez de citar." % ondev)

        # ---------------- a regra do documento nomeado (esquema, 26.2)
        # O que sustenta o PRECO de um registro sao as fontes das versoes dele. Se
        # alguma delas e de nivel de autoridade e nao nomeia documento, o registro
        # entra como pendente_de_releitura e nunca como publicavel.
        if status_sem_documento:
            mudas = [v.get("fonte") for v in versoes
                     if fontes.get(v.get("fonte"), {}).get("nivel") in niveis_de_autoridade
                     and fontes.get(v.get("fonte"), {}).get("documento") is None]
            if mudas and exp.get("status") != status_sem_documento:
                erro("%s: `status` %r com preco sustentado por fonte de autoridade que "
                     "NAO nomeia documento (%s). O esquema manda %r nesse caso: o "
                     "registro entra, e entra a reconferir. Autoridade de que so se "
                     "ouviu falar nao vale o mesmo que autoridade com ato citado, e "
                     "antes desta regra as duas tinham o mesmo nivel."
                     % (onde, exp.get("status"), ", ".join(sorted(set(mudas))),
                        status_sem_documento))

        # ---------------- declaracoes divergentes
        declaracoes = exp.get("declaracoes")
        if not isinstance(declaracoes, list):
            erro("%s: `declaracoes` ausente ou nao e lista. Lista vazia e afirmacao "
                 "(ninguem mais publicou numero); chave ausente e esquecimento." % onde)
            declaracoes = []
        for i, dec in enumerate(declaracoes):
            n_declaracoes += 1
            onded = "%s/declaracoes[%d]" % (onde, i)
            if "versao" not in dec:
                erro("%s: falta o campo `versao`. Divergencia e sobre a VERSAO, nunca "
                     "sobre a experiencia: numa escada de dias, comparar o preco de 1 dia "
                     "com o de 3 e comparar dois produtos." % onded)
            elif dec.get("versao") is None:
                if not dec.get("motivo_sem_versao"):
                    erro("%s: `versao` null sem `motivo_sem_versao`." % onded)
                sem_versao += 1
            elif dec.get("versao") not in precos_por_id:
                erro("%s: `versao` %r nao e uma versao desta experiencia."
                     % (onded, dec.get("versao")))
            if dec.get("publicador") is None and not dec.get("motivo_sem_publicador"):
                erro("%s: `publicador` null sem `motivo_sem_publicador`." % onded)
            esperado = dec.get("publicador") is not None
            if dec.get("publicavel_na_tela") is not esperado:
                erro("%s: `publicavel_na_tela` gravado como %r e a derivacao da %r. "
                     "Declaracao so vai para a tela com nome: 'algumas paginas dizem X' "
                     "e a frase sem dono que esta ilha existe para nao escrever."
                     % (onded, dec.get("publicavel_na_tela"), esperado))
            if esperado:
                n_publicaveis += 1
            if dec.get("url") is None and not dec.get("motivo_sem_url"):
                erro("%s: `url` null sem `motivo_sem_url`." % onded)
            if not dec.get("diz"):
                erro("%s: sem `diz`." % onded)
            if not em_vocab("unidade_de_preco", dec.get("unidade_de_preco")):
                erro("%s: `unidade_de_preco` %r fora do vocabulario."
                     % (onded, dec.get("unidade_de_preco")))
            if not em_vocab("moeda", dec.get("moeda")):
                erro("%s: `moeda` %r fora do vocabulario." % (onded, dec.get("moeda")))
            if not _e_data(dec.get("data_leitura")):
                erro("%s: `data_leitura` ausente ou nao e data." % onded)
            if _maximo(dec.get("valor")) is None:
                erro("%s: `valor` %r nao e numero nem faixa {minimo, maximo}."
                     % (onded, dec.get("valor")))
            if dec.get("fonte") not in fontes:
                erro("%s: `fonte` %r nao existe em fontes[]." % (onded, dec.get("fonte")))
            else:
                fontes_usadas.add(dec["fonte"])

        # ---------------- resolucao: a proibicao de media, em codigo
        resolucao = exp.get("resolucao")
        if declaracoes and not resolucao:
            erro("%s: ha declaracoes divergentes e nao ha `resolucao`. Divergencia sem "
                 "resolucao escrita e a ilha empurrando a duvida para quem le." % onde)
        if not declaracoes and resolucao:
            erro("%s: ha `resolucao` e nenhuma declaracao divergente para resolver." % onde)
        if declaracoes and resolucao:
            onder = "%s/resolucao" % onde
            if not resolucao.get("erro_caro"):
                erro("%s: sem `erro_caro`. Antes de resolver qualquer divergencia se "
                     "escreve qual e o erro caro — a direcao sai sozinha depois disso "
                     "(secao 10)." % onder)
            if not resolucao.get("texto"):
                erro("%s: sem `texto`." % onder)

            vid = resolucao.get("versao_resolvida")
            if vid not in precos_por_id:
                erro("%s: `versao_resolvida` %r nao e uma versao desta experiencia."
                     % (onder, vid))
            else:
                versao = next(v for v in versoes if v.get("id") == vid)
                if resolucao.get("valor") != versao.get("preco"):
                    erro("%s: `valor` %r nao e o preco da versao resolvida (%r). O valor "
                         "resolvido E o que vai para a tela; dois numeros para a mesma "
                         "coisa no mesmo registro e armadilha, nao historia."
                         % (onder, resolucao.get("valor"), versao.get("preco")))
                if resolucao.get("unidade_de_preco") != versao.get("unidade_de_preco"):
                    erro("%s: `unidade_de_preco` %r difere da versao resolvida (%r)."
                         % (onder, resolucao.get("unidade_de_preco"),
                            versao.get("unidade_de_preco")))
                if resolucao.get("moeda") != versao.get("moeda"):
                    erro("%s: `moeda` %r difere da versao resolvida (%r)."
                         % (onder, resolucao.get("moeda"), versao.get("moeda")))

            fid = resolucao.get("fonte")
            if fid not in fontes:
                erro("%s: `fonte` %r nao existe em fontes[]." % (onder, fid))
            else:
                fontes_usadas.add(fid)
                origem = fontes[fid].get("origem") or ""
                tem_autoridade = "poder-publico" in origem
                if resolucao.get("por_autoridade") is not tem_autoridade:
                    erro("%s: `por_autoridade` gravado como %r e a escada diz %r para a "
                         "origem %r. Autoridade nao se declara, se le da escada."
                         % (onder, resolucao.get("por_autoridade"), tem_autoridade, origem))

                if not tem_autoridade:
                    # Sem autoridade resolve para o MAIOR. Media nao se reconhece pelo
                    # nome: ela se reconhece por cair entre o minimo e o maximo sem ser
                    # nenhum dos dois.
                    #
                    # E os candidatos sao os da VERSAO RESOLVIDA, nunca os da
                    # experiencia inteira: numa escada de dias, o preco de 3 dias e
                    # outro produto. Declaracao sem versao atribuida e conteudo na
                    # tela e nao e voto na conta.
                    unidade = resolucao.get("unidade_de_preco")
                    candidatos = []
                    comparaveis = []
                    versao_alvo = next((v for v in versoes if v.get("id") == vid), None)
                    if versao_alvo and isinstance(versao_alvo.get("preco"), (int, float)):
                        candidatos.append(float(versao_alvo["preco"]))
                    for dec in declaracoes:
                        if dec.get("versao") == vid and dec.get("unidade_de_preco") == unidade:
                            topo = _maximo(dec.get("valor"))
                            if topo is not None:
                                candidatos.append(topo)
                                comparaveis.append(dec)
                    if candidatos:
                        alvo = max(candidatos)
                        valor = resolucao.get("valor")
                        if isinstance(valor, (int, float)) and float(valor) != alvo:
                            piso = min(candidatos + [_minimo(d.get("valor")) or alvo
                                                     for d in comparaveis])
                            if piso < float(valor) < alvo:
                                erro("%s: sem autoridade, o valor resolvido %r cai ENTRE "
                                     "%r e %r sem ser nenhum dos dois. Isso e media com "
                                     "outro nome, e media e a unica saida proibida: ela "
                                     "esconde exatamente o desacordo que faz a pagina "
                                     "valer." % (onder, valor, piso, alvo))
                            else:
                                erro("%s: sem autoridade a regra resolve para o MAIOR "
                                     "(%r) e o gravado e %r. O erro caro desta ilha e "
                                     "subestimar." % (onder, alvo, valor))

        # ---------------- afiliado: o piso da 25.2
        afiliado = exp.get("afiliado")
        if not isinstance(afiliado, dict):
            erro("%s: sem `afiliado`. O piso de compra nasce com o item." % onde)
            sem_saida += 1
        else:
            ondea = "%s/afiliado" % onde
            if "url" not in afiliado or not isinstance(afiliado.get("url"), str):
                erro("%s: `url` ausente. Ela nasce PRESENTE E VAZIA — string vazia "
                     "declara que o campo existe e nao tem link rastreado; chave ausente "
                     "e esquecimento." % ondea)
            if afiliado.get("url_produto") is None and not afiliado.get("motivo_sem_url_produto"):
                erro("%s: `url_produto` null sem `motivo_sem_url_produto` (25.4-b: sem "
                     "URL crua o teste de vida e impossivel)." % ondea)

            piso = afiliado.get("url_busca_produto")
            if not piso:
                erro("%s: SEM PISO DE COMPRA. Item sem saida de compra e defeito da 19.1, "
                     "sempre — e 'link de loja em breve' esta proibido (secao 7)." % ondea)
                sem_saida += 1
            elif molde_piso and cidade is not None:
                derivado = molde_piso.replace("{slug_plataforma}", cidade.get("slug_plataforma") or "")
                if piso != derivado:
                    erro("%s: `url_busca_produto` gravada como %r e a derivacao do molde "
                         "com o slug da cidade da %r. O piso e fabricado a partir da "
                         "cidade, nunca digitado: URL digitada envelhece calada no dia em "
                         "que o molde mudar." % (ondea, piso, derivado))

            if not afiliado.get("url"):
                piso_nao_rastreavel += 1

            rel = afiliado.get("rel") or ""
            if afiliado.get("programa") is None:
                esperado_rel = esquema.get("piso_de_compra", {}).get("rel_enquanto_nao_ha_programa")
                if esperado_rel and rel != esperado_rel:
                    erro("%s: sem programa cadastrado, `rel` tem de ser %r e esta %r."
                         % (ondea, esperado_rel, rel))
                if "sponsored" in rel:
                    erro("%s: `rel` tem `sponsored` e nao ha programa de afiliado. "
                         "sponsored declara relacao PAGA, e ninguem esta pagando por este "
                         "clique." % ondea)

            esperado_int = bool(afiliado.get("url")) and afiliado.get("url_produto") is None
            if afiliado.get("intestavel") is not esperado_int:
                erro("%s: `intestavel` gravado como %r e a derivacao da %r."
                     % (ondea, afiliado.get("intestavel"), esperado_int))
            if esperado_int:
                intestaveis += 1

    # ------------------------------------------------------------------
    # 5. AS DUAS DIRECOES (secao 8): dado colhido que a tela nunca usa tambem conta
    # ------------------------------------------------------------------
    for fid in fontes:
        if fid not in fontes_usadas:
            erro("fontes/%s: nenhuma versao e nenhuma declaracao aponta para esta fonte. "
                 "Fonte colhida que o banco nunca usa e a outra direcao do numero "
                 "digitado: ela envelhece sem ninguem notar." % fid)
    usadas_por_exp = {e.get("cidade") for e in banco.get("experiencias", [])}
    for cid in cidades:
        if cid not in usadas_por_exp:
            aviso("cidades/%s: nenhuma experiencia nesta cidade ainda. Cidade pode "
                  "preceder experiencia; se persistir, e malha prometida e nao construida."
                  % cid)

    # ------------------------------------------------------------------
    # 6. FRASE PROIBIDA E CONSTANTE PENDENTE
    # ------------------------------------------------------------------
    for texto in _textos(banco):
        if FRASE_PROIBIDA in texto.lower():
            erro("banco: a frase %r aparece no banco. Proibida pela secao 7 desde "
                 "14/09/2026." % FRASE_PROIBIDA)
            break

    if constantes:
        pendentes = [c.get("id") for c in constantes.get("constantes", [])
                     if c.get("status") == "pendente"]
        textos = list(_textos(banco))
        for cid in pendentes:
            if any(cid and cid in t for t in textos):
                erro("banco: usa a constante %r, que esta com status `pendente`. "
                     "Constante pendente e proibida dentro de formula publicada "
                     "(secao 10)." % cid)

    # ------------------------------------------------------------------
    # 7. O RESUMO NASCE CONTADO, NUNCA DIGITADO (secao 8)
    # ------------------------------------------------------------------
    calculado = {
        "cidades": len(banco.get("cidades", [])),
        "experiencias": len(banco.get("experiencias", [])),
        "versoes": n_versoes,
        "fontes": len(banco.get("fontes", [])),
        "declaracoes": n_declaracoes,
        "declaracoes_publicaveis": n_publicaveis,
        "declaracoes_sem_versao": sem_versao,
        "itens_sem_saida_de_compra": sem_saida,
        "itens_com_piso_nao_rastreavel": piso_nao_rastreavel,
        "itens_intestaveis": intestaveis,
        "experiencias_com_preco_em_brl": com_brl_convertido,
        "fontes_de_leitura_direta": sum(1 for f in banco.get("fontes", [])
                                        if f.get("leitura") == "leitura_direta"),
    }
    gravado = banco.get("resumo") or {}
    for chave, valor in calculado.items():
        if chave not in gravado:
            erro("resumo: falta a chave `%s` (contada: %r)." % (chave, valor))
        elif gravado[chave] != valor:
            erro("resumo: `%s` gravado como %r e a contagem da %r. Numero que a ilha "
                 "publica sobre si mesma nasce contado, nunca digitado (secao 8)."
                 % (chave, gravado[chave], valor))
    for chave in gravado:
        if chave not in calculado:
            erro("resumo: `%s` nao e uma contagem que esta regua saiba refazer. Numero "
                 "no resumo que ninguem recomputa e digitado com cara de medido." % chave)

    if sem_saida:
        erro("banco: %d item(ns) SEM saida de compra. Pela 25.2 isso e erro duro, nunca "
             "divida." % sem_saida)

    for v in vencidos:
        aviso("preco vencido: %s. Item vencido e defeito de ronda, nunca item escondido — "
              "a data de leitura vai para a tela vencida ou nao." % v)

    return erros, avisos, calculado


def main():
    esquema = _carregar("esquema-banco.json")
    banco = _carregar("experiencias.json")
    try:
        constantes = _carregar("constantes.json")
    except FileNotFoundError:
        constantes = None

    erros, avisos, calculado = validar(esquema, banco, constantes)

    print("Banco da JornadaFly — verificacao do esquema do bloco 3")
    for chave in ("cidades", "experiencias", "versoes", "fontes", "declaracoes",
                  "declaracoes_publicaveis", "declaracoes_sem_versao", "itens_sem_saida_de_compra",
                  "itens_com_piso_nao_rastreavel", "itens_intestaveis",
                  "experiencias_com_preco_em_brl", "fontes_de_leitura_direta"):
        if chave in calculado:
            print("  %-32s %s" % (chave.replace("_", " ") + " ", calculado[chave]))
    for a in avisos:
        print("  AVISO: %s" % a)
    if erros:
        print("\n%d ERRO(S):" % len(erros))
        for e in erros:
            print("  - %s" % e)
        sys.exit(1)
    print("\nOK: o banco cumpre o esquema, o piso de compra bate com a derivacao da "
          "cidade e a resolucao de divergencia bate com a escada de fontes.")


if __name__ == "__main__":
    main()
