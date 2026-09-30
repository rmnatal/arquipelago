#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica se o banco do Clube do Mosaico cumpre o contrato de dados/esquema-banco.json.

Roda sem dependencia e sem rede:

    python3 ferramentas/validar-banco.py

Sai com codigo 1 se qualquer invariante for violada. Este arquivo NUNCA e publicado no
site: e ferramenta de bancada.

Por que ele existe, e por que nesta ilha ele importa mais do que a media: o produto
desta ilha e a compatibilidade cola x base x ambiente. Errar ali faz a peca descolar
meses depois, na casa de quem comprou. E defeito de banco nao aparece lendo o arquivo —
aparece quando alguem passa o fim de semana montando um vaso que vai soltar.

O que ele faz, alem de conferir campo obrigatorio:

  RECOMPUTA A MATRIZ DA F2 a partir das declaracoes dos fabricantes, aplicando as cinco
  regras_de_elegibilidade do esquema, e compara celula a celula com a matriz publicada em
  esquema-banco.json -> matriz_esperada_da_F2. Se o banco e a pagina se separarem, isto
  falha alto. E a mesma logica que o snippet PHP do bloco 4 tem que repetir: as duas
  implementacoes precisam dar o mesmo resultado, e esta aqui e a de referencia.
"""

import json
import os
import re
import sys
import unicodedata

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = os.path.join(BASE, "dados")

erros = []
avisos = []
notas = []


def erro(msg):
    erros.append(msg)


def aviso(msg):
    # deduplicado: `perfil()` roda uma vez por celula da matriz, e o mesmo termo sem
    # traducao apareceria 18 vezes no relatorio.
    if msg not in avisos:
        avisos.append(msg)


def nota(msg):
    notas.append(msg)


def carregar(nome):
    caminho = os.path.join(DADOS, nome)
    if not os.path.exists(caminho):
        return None
    with open(caminho, encoding="utf-8") as fh:
        return json.load(fh)


def normalizar(texto):
    """Minusculas, sem acento, espacos colapsados. A comparacao com o mapa de termos e
    EXATA depois disso: 'ceramica' (substrato, no produto de colagem) e 'ceramicas' (a
    peca assentada, no produto de assentamento) sao termos diferentes de proposito."""
    t = unicodedata.normalize("NFKD", texto.strip().lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return " ".join(t.split())


# ---------------------------------------------------------------- carregar

esquema = carregar("esquema-banco.json")
if esquema is None:
    print("ERRO: dados/esquema-banco.json nao existe.")
    sys.exit(1)

VOC = esquema["vocabularios"]

# INTERRUPTOR DE MEDICAO, e ele existe por um motivo so: `mutacoes-acabamento.py`
# precisa separar o que o portao NOVO viu do que o esquema ja pegava, e a bateria
# das pastilhas fazia isso rodando dois scripts diferentes — aqui os dois moram no
# mesmo. Nao e jeito de aprovar banco: quando ele esta ligado, a saida diz isso em
# voz alta na primeira linha, entao passada verde com ele ligado nunca e silenciosa.
SEM_PORTAO_ACABAMENTO = os.environ.get("CDM_SEM_PORTAO_ACABAMENTO") == "1"
if SEM_PORTAO_ACABAMENTO:
    print("  ATENCAO: CDM_SEM_PORTAO_ACABAMENTO=1 — o bloco da categoria acabamento "
          "NAO foi medido nesta passada. So a bateria de mutacao usa isto.")
SEM_PORTAO_BASE = os.environ.get("CDM_SEM_PORTAO_BASE") == "1"
if SEM_PORTAO_BASE:
    print("  ATENCAO: CDM_SEM_PORTAO_BASE=1 — o bloco da categoria base NAO foi medido nesta "
          "passada. So a bateria de mutacao usa isto.")
SEM_PORTAO_APOIO = os.environ.get("CDM_SEM_PORTAO_APOIO") == "1"
if SEM_PORTAO_APOIO:
    print("  ATENCAO: CDM_SEM_PORTAO_APOIO=1 — o bloco da categoria apoio, a ponte do ramo e a "
          "varredura de apoio declarado NAO foram medidos nesta passada. So a bateria de mutacao "
          "usa isto.")
SEM_PORTAO_DEGRAU = os.environ.get("CDM_SEM_PORTAO_DEGRAU") == "1"
if SEM_PORTAO_DEGRAU:
    print("  ATENCAO: CDM_SEM_PORTAO_DEGRAU=1 — o degrau da escada da 25.1 volta a ser cobrado "
          "so de quem tem `url`, que e a regra ANTIGA, a que deixou 13 itens em null. So a "
          "bateria de mutacao usa isto.")
SEM_PORTAO_MOTIVO_DEGRAU_4 = os.environ.get("CDM_SEM_PORTAO_MOTIVO_DEGRAU_4") == "1"
if SEM_PORTAO_MOTIVO_DEGRAU_4:
    print("  ATENCAO: CDM_SEM_PORTAO_MOTIVO_DEGRAU_4=1 — o motivo do degrau 4 NAO foi cobrado "
          "nesta passada, que e a regra ANTIGA, a que deixou 12 dos 17 itens sem dizer por que "
          "pararam. So a bateria de mutacao usa isto.")
BASES = set(VOC["base"])
AMBIENTES = set(VOC["ambiente"])
REGRAS = esquema["regras_de_elegibilidade"]
CRITICOS = set(REGRAS["4_ambiente_critico_exige_declaracao_EXPLICITA"]["ambientes"])
NIVEL_MAX = esquema["escada_de_fontes"]["nivel_minimo_para_recomendacao_primaria"]
CATEGORIA_DA_MATRIZ_F2 = esquema["matriz_esperada_da_F2"].get("categoria_considerada", "cola")
if CATEGORIA_DA_MATRIZ_F2 not in VOC["categoria_material"]:
    erro("matriz da F2: categoria_considerada '%s' fora do vocabulario" % CATEGORIA_DA_MATRIZ_F2)

MAPA = {}
VAGOS = set()
for termo in esquema["mapa_de_termos_do_fabricante"]["termos"]:
    chave = normalizar(termo["literal"])
    MAPA[chave] = {"base": termo.get("base", []), "ambiente": termo.get("ambiente", [])}
    if termo.get("vago"):
        VAGOS.add(chave)

NAO_TRADUZ = {normalizar(t["literal"]) for t in esquema["mapa_de_termos_do_fabricante"]["termos_que_nao_traduzem"]}

# vocabulario do mapa tem que existir no vocabulario da ilha
for chave, alvo in MAPA.items():
    for b in alvo["base"]:
        if b not in BASES:
            erro("mapa de termos: '%s' aponta para base inexistente '%s'" % (chave, b))
    for a in alvo["ambiente"]:
        if a not in AMBIENTES:
            erro("mapa de termos: '%s' aponta para ambiente inexistente '%s'" % (chave, a))
for chave in NAO_TRADUZ:
    if chave in MAPA:
        erro("termo '%s' esta ao mesmo tempo no mapa e na lista dos que nao traduzem" % chave)


# ---------------------------------------------- A PONTE DO TIPO PARA O EIXO
# 28/09/2026, com a categoria `base`. Este bloco NAO olha registro nenhum: ele
# mede o esquema contra si mesmo, e foi preciso porque a categoria `base` e a
# unica cujo PRODUTO E o eixo pelo qual a F2 decide. Antes dele, tres dos cinco
# tipos de `tipo_por_categoria.base` nao tinham onde pousar em `vocabularios.base`
# e nada dizia isso em lugar nenhum — e o preco ja estava pago no banco: dois
# vernizes da Acrilex carregam `isopor` e `gesso` DENTRO da frase literal do
# fabricante, e as duas palavras nao existem no vocabulario, entao a declaracao
# foi lida, classificada e descartada em silencio.
#
# A ilha ja sabia ler SILENCIO de fabricante (e o terceiro estado do esquema).
# O que ela nao sabia ler era declaracao de fabricante JOGADA FORA por falta de
# vocabulario nosso — que e a mesma familia, do nosso lado do balcao.
PONTE = esquema.get("ponte_do_tipo_para_o_vocabulario_base")
SEM_PORTAO_PONTE = os.environ.get("CDM_SEM_PORTAO_PONTE") == "1"
if SEM_PORTAO_PONTE:
    print("  ATENCAO: CDM_SEM_PORTAO_PONTE=1 — a ponte do tipo para o eixo NAO foi medida "
          "nesta passada. So a bateria de mutacao usa isto.")
if PONTE is None and not SEM_PORTAO_PONTE:
    erro("esquema sem `ponte_do_tipo_para_o_vocabulario_base`. A categoria `base` e a unica cujo "
         "produto E o eixo da F2; sem a ponte, tipo sem valor no vocabulario fica invisivel")
elif PONTE is not None and not SEM_PORTAO_PONTE:
    ESTADOS_DA_PONTE = ("pousa", "sem_valor_no_vocabulario", "nao_e_material")
    tipos_declarados = PONTE.get("tipos")
    if not isinstance(tipos_declarados, dict):
        erro("ponte: `tipos` tem de ser um objeto")
        tipos_declarados = {}
    do_vocabulario = list(VOC["tipo_por_categoria"]["base"])

    faltando = [t for t in do_vocabulario if t not in tipos_declarados]
    sobrando = [t for t in tipos_declarados if t not in do_vocabulario]
    if faltando:
        erro("ponte: tipo de base sem declaracao de onde pousa: %s. Tipo calado aqui e declaracao "
             "de fabricante que a ilha le e joga fora sem ninguem ver" % ", ".join(sorted(faltando)))
    if sobrando:
        erro("ponte: tipo declarado que nao existe em `tipo_por_categoria.base`: %s"
             % ", ".join(sorted(sobrando)))

    for tipo in sorted(set(do_vocabulario) & set(tipos_declarados)):
        d = tipos_declarados[tipo] or {}
        est = d.get("estado")
        if est not in ESTADOS_DA_PONTE:
            erro("ponte / %s: estado '%s' fora da lista (%s)" % (tipo, est, ", ".join(ESTADOS_DA_PONTE)))
            continue
        if not d.get("motivo"):
            erro("ponte / %s: estado '%s' sem `motivo`" % (tipo, est))
        if est == "pousa":
            alvos = d.get("pousa_em")
            if not isinstance(alvos, list) or not alvos:
                erro("ponte / %s: estado `pousa` com `pousa_em` vazio" % tipo)
            else:
                for b in alvos:
                    if b not in BASES:
                        erro("ponte / %s: pousa em '%s', que nao existe em `vocabularios.base`"
                             % (tipo, b))
        elif est == "sem_valor_no_vocabulario":
            proposto = d.get("valor_proposto")
            if not proposto:
                erro("ponte / %s: `sem_valor_no_vocabulario` sem `valor_proposto`. Buraco sem nome "
                     "e buraco que a proxima execucao redescobre do zero" % tipo)
            elif proposto in BASES:
                erro("ponte / %s: `valor_proposto` '%s' JA existe em `vocabularios.base` — entao o "
                     "tipo pousa e o estado esta errado" % (tipo, proposto))
            if not d.get("o_que_falta"):
                erro("ponte / %s: `sem_valor_no_vocabulario` sem `o_que_falta`" % tipo)
        elif est == "nao_e_material":
            if not d.get("onde_ele_e"):
                erro("ponte / %s: `nao_e_material` sem `onde_ele_e`. Tipo que nao e material tem "
                     "de dizer em que eixo ele mora, senao ele so desaparece" % tipo)

    # AS CONDICIONAIS DO MAPA DE TERMOS. Duas linhas de `termos_que_nao_traduzem`
    # nao recusam o termo para sempre: recusam SOB CONDICAO, com a frase "entra no
    # vocabulario primeiro". Uma delas — `poliestireno expandido` — ja estava
    # cumprida no dia em que foi escrita, porque `isopor_estrutural` ja era um dos
    # cinco tipos de `tipo_por_categoria.base` no MESMO arquivo. Nada conferia as
    # duas linhas juntas. Agora confere.
    FRASE_CONDICIONAL = "entra no vocabulario primeiro"
    cond = (PONTE.get("condicionais_do_mapa_de_termos") or {}).get("linhas") or []
    cobertas = {normalizar(l.get("literal", "")) for l in cond if isinstance(l, dict)}
    for termo in esquema["mapa_de_termos_do_fabricante"]["termos_que_nao_traduzem"]:
        if FRASE_CONDICIONAL in normalizar(termo.get("por_que", "")):
            if normalizar(termo["literal"]) not in cobertas:
                erro("ponte: o termo '%s' recusa a traducao SOB CONDICAO ('%s') e a condicao nao "
                     "aparece em `condicionais_do_mapa_de_termos`. Condicao escrita e nunca "
                     "conferida e promessa — foi assim que `poliestireno expandido` ficou com a "
                     "condicao cumprida no proprio arquivo sem ninguem ver" % (termo["literal"], FRASE_CONDICIONAL))
    for l in cond:
        if not isinstance(l, dict):
            erro("ponte / condicionais: linha que nao e objeto")
            continue
        if not isinstance(l.get("condicao_cumprida"), bool):
            erro("ponte / condicionais / %s: `condicao_cumprida` tem de ser true ou false"
                 % l.get("literal"))
        if not l.get("por_onde"):
            erro("ponte / condicionais / %s: sem `por_onde` — a medicao tem de dizer por onde foi "
                 "feita, senao ela e opiniao" % l.get("literal"))
        if l.get("condicao_cumprida") and normalizar(l.get("literal", "")) not in NAO_TRADUZ:
            erro("ponte / condicionais / %s: condicao cumprida e o termo ja saiu de "
                 "`termos_que_nao_traduzem` — a linha virou historia e nao portao" % l.get("literal"))


# ------------------------------------------ A PONTE DO TIPO DE APOIO PARA O RAMO
# 28/09/2026, com a categoria `apoio`, a ultima das sete a receber decisao de
# campo. Irma da ponte acima e escrita pelo mesmo motivo — conferir, ANTES do
# primeiro SKU, se o vocabulario de tipos tem onde pousar —, mas o eixo aqui nao
# e material: e RAMO. Espatula, desempenadeira, pinca e marcador agem sobre o
# MATERIAL e o erro deles estraga a PECA; oculos e luva agem sobre a PESSOA e o
# erro deles machuca quem monta. Uma lista so poria luva ao lado de
# desempenadeira como se a escolha fosse do mesmo tipo, e nao e.
PONTE_APOIO = esquema.get("ponte_do_tipo_de_apoio_para_o_ramo")
if PONTE_APOIO is None and not SEM_PORTAO_APOIO:
    erro("esquema sem `ponte_do_tipo_de_apoio_para_o_ramo`. Sem ela, luva e desempenadeira viram "
         "a mesma lista, e as duas nao se escolhem pelo mesmo criterio")
elif PONTE_APOIO is not None and not SEM_PORTAO_APOIO:
    RAMOS = set(VOC.get("ramo_do_apoio") or [])
    if not RAMOS:
        erro("esquema sem `vocabularios.ramo_do_apoio`")
    tipos_apoio = PONTE_APOIO.get("tipos")
    if not isinstance(tipos_apoio, dict):
        erro("ponte do apoio: `tipos` tem de ser um objeto")
        tipos_apoio = {}
    do_voc_apoio = list(VOC["tipo_por_categoria"]["apoio"])
    faltando = [t for t in do_voc_apoio if t not in tipos_apoio]
    sobrando = [t for t in tipos_apoio if t not in do_voc_apoio]
    if faltando:
        erro("ponte do apoio: tipo sem ramo declarado: %s. Tipo calado aqui e um item que a "
             "vitrine nao sabe se protege a peca ou a pessoa" % ", ".join(sorted(faltando)))
    if sobrando:
        erro("ponte do apoio: tipo declarado que nao existe em `tipo_por_categoria.apoio`: %s"
             % ", ".join(sorted(sobrando)))
    for tipo in sorted(set(do_voc_apoio) & set(tipos_apoio)):
        linha = tipos_apoio[tipo] or {}
        if linha.get("ramo") not in RAMOS:
            erro("ponte do apoio / %s: ramo '%s' fora de `vocabularios.ramo_do_apoio`"
                 % (tipo, linha.get("ramo")))
        if not linha.get("motivo"):
            erro("ponte do apoio / %s: ramo sem `motivo`" % tipo)


def traduzir(lista, onde):
    """Devolve (bases, ambientes, vagos) de uma lista de termos literais do fabricante."""
    bases, ambientes, vagos = set(), set(), set()
    for literal in lista or []:
        chave = normalizar(literal)
        if chave in MAPA:
            if chave in VAGOS:
                vagos.update(MAPA[chave]["base"])
            else:
                bases.update(MAPA[chave]["base"])
            ambientes.update(MAPA[chave]["ambiente"])
        elif chave in NAO_TRADUZ:
            continue
        else:
            aviso("%s: termo do fabricante sem traducao no mapa, ficou so na citacao literal: '%s'" % (onde, literal))
    return bases, ambientes, vagos


# ---------------------------------------------------------------- MATERIAL

CAMPOS_OBRIGATORIOS = [
    "id", "categoria", "tipo", "marca", "fabricante", "nome_comercial",
    "codigo_fabricante", "declaracoes", "venda", "afiliado", "imagem",
    "fontes", "divergencias", "status",
]

arquivos_material = sorted(
    n for n in os.listdir(DADOS) if n.startswith("materiais-") and n.endswith(".json")
)
if not arquivos_material:
    nota("nenhum arquivo materiais-*.json ainda: banco de MATERIAL vazio.")

materiais = {}
esperando_link = 0
sem_imagem = 0
sem_saida = 0            # secao 7 e 25.2: item sem NENHUMA saida de compra — erro duro
piso_nao_rastreavel = 0  # 25.6: tem busca CRUA e nao tem a encurtada — divida de comissao
sem_busca_crua = 0    # secao 25.4-b: tem busca e nao guarda o endereco cru dela
# A ESCADA CONTADA, degrau a degrau (28/09/2026). A 25.1 manda GRAVAR o degrau;
# esta contagem e o que torna o campo util depois de gravado, porque e por ela
# que a leitura semanal acha o que pode subir. O 4 e o degrau que nao esgota e
# nao some, e tambem o que converte pior: banco inteiro no 4 cumpre o esquema e
# rende o minimo.
por_degrau = {1: 0, 2: 0, 3: 0, 4: 0}
# O MOTIVO DO DEGRAU 4, CONTADO POR CLASSE DE CAUSA (30/09/2026). A 25.4-b.4 diz
# que "nao casou" tem causas que parecem uma e que, contadas juntas, "viram um
# numero que nao diz o que fazer". Entao o portao nao conta quantos tem o campo:
# conta quantos estao em CADA causa, porque e essa reparticao que diz o que fazer
# — item cuja marca nem e anunciada espera decisao do Raphael, e item com
# candidato barrado espera trava melhor ou registro de variante. Um numero so
# mistura um pedido a ele com uma divida nossa.
degrau_4_sem_ficha = 0
degrau_4_com_motivo = 0
por_causa_do_degrau_4 = {}
casamentos_a_reconferir = []   # (onde, registro, titulo gravado) — reconferidos abaixo
reconferidos = 0

# ---------------------------------------------- A TRAVA DO BATISMO (esquema v8)
#
# `nome_comercial` e campo do FABRICANTE. A regra mora sozinha em
# batismo-do-fabricante.py porque mutacoes-batismo.py ataca a MESMA funcao que
# este validador usa. Quais fontes batizam e decisao do esquema (26.2), e a
# regra levanta EsquemaSemBatismo quando a chave some — trava que le a propria
# lista de um arquivo de dados aprova tudo em silencio no dia em que a lista
# sumir, e esse dia nao pode passar despercebido.
import importlib.util as _iu_bat
_s_bat = _iu_bat.spec_from_file_location(
    "batismo_do_fabricante",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "batismo-do-fabricante.py"))
_batismo = _iu_bat.module_from_spec(_s_bat)
_s_bat.loader.exec_module(_batismo)
batismos_conferidos = 0

for nome in arquivos_material:
    arq = carregar(nome)
    categoria_arquivo = arq.get("categoria")
    if categoria_arquivo not in VOC["categoria_material"]:
        erro("%s: categoria '%s' fora do vocabulario" % (nome, categoria_arquivo))

    for m in arq.get("materiais", []):
        ident = m.get("id", "<sem id>")
        onde = "%s / %s" % (nome, ident)

        for campo in CAMPOS_OBRIGATORIOS:
            if campo not in m:
                erro("%s: campo obrigatorio ausente: %s" % (onde, campo))

        if ident in materiais:
            erro("%s: id repetido no banco" % onde)
        materiais[ident] = m

        if m.get("categoria") != categoria_arquivo:
            erro("%s: categoria do registro difere da do arquivo" % onde)
        tipos = VOC["tipo_por_categoria"].get(m.get("categoria"), [])
        if m.get("tipo") not in tipos:
            erro("%s: tipo '%s' fora do vocabulario da categoria" % (onde, m.get("tipo")))
        if m.get("status") not in VOC["status_do_registro"]:
            erro("%s: status invalido" % onde)
        if m.get("status") == "descartado" and not m.get("motivo_do_descarte"):
            erro("%s: descartado sem motivo_do_descarte" % onde)
        if m.get("codigo_fabricante") is None and not m.get("motivo_sem_codigo"):
            erro("%s: codigo_fabricante null exige motivo_sem_codigo" % onde)
        if m.get("divergencias") and not m.get("resolucao"):
            erro("%s: divergencias sem resolucao escrita" % onde)

        # O BATISMO E DO FABRICANTE (esquema v8, secao 26 ao contrario). Nasceu de
        # `quartzolit-borracha-liquida-elastica`, que se chamava "impermeabilizante
        # borracha liquida elastica quartzolit" — e `impermeabilizante` veio do
        # CAMINHO da pagina de produto, a prateleira do fabricante, enquanto o
        # boletim tecnico do mesmo produto (nivel 2) nao a escreve. O registro
        # citava as duas fontes e tinha tomado a mais fraca.
        try:
            ok_batismo, laudo_batismo = _batismo.conferir(m, esquema)
        except _batismo.EsquemaSemBatismo as falha:
            erro("%s: %s" % (onde, falha))
        else:
            if laudo_batismo.get("em_escopo"):
                batismos_conferidos += 1
                if not ok_batismo:
                    erro("%s / nome_comercial: %s" % (onde, laudo_batismo["motivo"]))

        # fontes
        fontes = m.get("fontes") or {}
        if not fontes:
            erro("%s: sem nenhuma fonte" % onde)
        for fid, f in fontes.items():
            for campo in ("url", "tipo", "nivel", "coletado_em", "conferir_no_pdf"):
                if campo not in f:
                    erro("%s / fonte %s: falta %s" % (onde, fid, campo))
            if not isinstance(f.get("nivel"), int) or not (1 <= f["nivel"] <= 7):
                erro("%s / fonte %s: nivel fora de 1-7" % (onde, fid))
            if f.get("nivel") == 7:
                erro("%s / fonte %s: nivel 7 (blog/SERP) e PROIBIDO como fonte tecnica nesta ilha" % (onde, fid))
            # `fontes` E O QUE SUSTENTA O REGISTRO, e nada mais. Achado em 13/09/2026,
            # pelo portao da F2, antes do commit: uma ficha tecnica LOCALIZADA e nao lida
            # tinha sido gravada aqui "para a proxima execucao saber onde ir", com nivel 2.
            # O nivel de um material e o MELHOR dos niveis das fontes dele, entao aquela
            # linha promoveu o produto inteiro de 3 para 2 sem que uma declaracao dele
            # viesse da ficha — e a linha de prova da tela passou a atribuir a declaracao a
            # um documento que ninguem abriu. Secao 10 do ARQUIPELAGO.md: o nivel e o do elo
            # MAIS FRACO, e inflar o proprio nivel de fonte e o defeito mais caro desta
            # fabrica. Endereco de documento que ainda nao foi lido mora em
            # `fonte_localizada_nao_lida`, fora de `fontes`.
            if f.get("sustenta_algum_campo") is False:
                erro("%s / fonte %s: esta em `fontes` declarando que nao sustenta campo "
                     "nenhum. Fonte que nao sustenta nada nao e fonte: ela empresta o nivel "
                     "dela ao produto inteiro. Mova para `fonte_localizada_nao_lida`."
                     % (onde, fid))

        # toda propriedade com valor precisa apontar fonte; toda propriedade nula, motivo
        for pnome, prop in (m.get("propriedades") or {}).items():
            if prop.get("valor") is None:
                if not prop.get("motivo"):
                    erro("%s / %s: valor null sem motivo escrito" % (onde, pnome))
            else:
                fid = prop.get("fonte_id")
                if not fid:
                    erro("%s / %s: valor sem fonte_id" % (onde, pnome))
                elif fid not in fontes:
                    erro("%s / %s: fonte_id '%s' nao existe em fontes{}" % (onde, pnome, fid))

        # ofertas
        for oferta in m.get("venda") or []:
            if oferta.get("unidade") not in VOC["unidade_de_venda"]:
                erro("%s: unidade de venda '%s' fora do vocabulario" % (onde, oferta.get("unidade")))
            if oferta.get("fonte_id") not in fontes:
                erro("%s: oferta sem fonte_id valido" % onde)
            if not oferta.get("coletado_em"):
                erro("%s: oferta sem coletado_em" % onde)

        # afiliado presente mesmo vazio (secao 7 do ARQUIPELAGO.md)
        af = m.get("afiliado") or {}
        if "url" not in af:
            erro("%s: afiliado.url tem que existir mesmo vazio" % onde)
        elif af["url"] == "":
            esperando_link += 1
        if af.get("programa") not in (None,) + tuple(VOC["programa_de_afiliado"]):
            erro("%s: programa de afiliado invalido" % onde)
        if af.get("sub_id_1") != "clubedomosaico":
            erro("%s: sub_id_1 tem que ser o nome da ilha" % onde)
        # A ETIQUETA DO MERCADO LIVRE, com a regra que o PAINEL aceita — e ela nao e a
        # que estava escrita aqui. A secao 7 do ARQUIPELAGO.md foi corrigida em 13/09/2026
        # MEDINDO o painel: so letras minusculas e numeros, sem hifen, sem espaco, sem
        # maiuscula, no maximo 30 caracteres, no formato <ilha><ferramenta>. A regua daqui
        # cobrava `clubedomosaico-<codigo>`, que e uma etiqueta IMPOSSIVEL de criar, e
        # aprovava os 23 registros do banco que a carregavam. Portao verde sobre um valor
        # que nao existe do outro lado: o mesmo defeito do numero de tela digitado, agora
        # numa regra de formato. Corrigido no mesmo commit que corrige os 23 registros.
        etiqueta = af.get("etiqueta_ml")
        if etiqueta:
            if not re.match(r"^[a-z0-9]{1,30}$", etiqueta):
                erro("%s: etiqueta '%s' fora do que o painel do Mercado Livre aceita "
                     "(so minuscula e numero, sem hifen, ate 30 caracteres — secao 7)"
                     % (onde, etiqueta))
            elif not etiqueta.startswith("clubedomosaico"):
                erro("%s: etiqueta '%s' nao comeca pelo nome da ilha" % (onde, etiqueta))

        # A ESCADA DA SECAO 25, medida no dado.
        #
        # 25.2 (decisao do Raphael, 13/09/2026): "todo item ganha `url_busca`
        # ANTES de qualquer outra coisa. Item sem `url_busca` e defeito da 19.1,
        # sempre, em qualquer degrau." Aqui ele e CONTADO, nao ignorado nem
        # transformado em erro duro, e a diferenca e deliberada:
        #
        #  - erro duro deixaria o `validar-banco.py` vermelho hoje pelas dez
        #    pastilhas, e portao vermelho que ninguem consegue fechar e portao
        #    que se aprende a ignorar;
        #  - silencio deixaria a divida invisivel, que e como ela chegou ate aqui.
        #
        # Contado e declarado no cabecalho do proprio arquivo, ele vira numero que
        # a ilha reporta em todo bloco — o mesmo desenho de `itens_esperando_link`,
        # que foi o que fez os dez links serem gerados em 13/09. No dia em que o
        # numero chegar a zero em todos os bancos, esta linha vira `erro()` e o
        # portao passa a impedir a divida de voltar.
        # A CONTAGEM MUDOU EM 14/09/2026, E ELA ESTAVA MEDINDO A COISA ERRADA.
        #
        # Ate aqui `sem_piso` contava quem nao tinha `url_busca` — o piso
        # ENCURTADO, o que rende comissao — e chamava isso de "sem piso". Sao duas
        # perguntas diferentes coladas numa so, e elas so davam o mesmo numero
        # enquanto nenhum item tinha saida CRUA:
        #
        #   1. O leitor tem para onde ir? (secao 7: nenhum item fica sem saida de
        #      compra, e a frase "link de loja em breve" esta proibida)
        #   2. Esse clique rende comissao? (25.6: o encurtamento depende de uma
        #      sessao do painel da Shopee, que nenhuma rotina alcanca)
        #
        # A primeira e defeito no ar e agora e ERRO DURO: com `url_busca_produto`
        # escrito, ela e fechavel sem depender de ninguem, e portao fechavel que
        # fica sendo aviso e portao que se aprende a ignorar. A segunda e divida
        # de receita, continua CONTADA, e nao e defeito de pagina: o leitor
        # chegou na loja.
        if not af.get("url") and not af.get("url_busca") and not af.get("url_busca_produto"):
            sem_saida += 1
            erro("%s: sem NENHUMA saida de compra — sem ficha, sem busca encurtada e sem busca "
                 "crua. E o item que chegaria a frase 'link de loja em breve', proibida pela "
                 "secao 7 desde 14/09/2026, e defeito da 19.1 pela 25.2" % onde)
        # DE AVISO PARA ERRO DURO EM 25/09/2026, e o comentario acima explica a
        # condicao: "no dia em que o numero chegar a zero em todos os bancos,
        # esta linha vira erro()". Chegou. Os quinze que faltavam foram gerados
        # pela Open API (25.6), que nao depende de sessao de ninguem, e o motivo
        # que mandava esperar o painel era de 13/09 — a 25.4-b.3 em acao.
        #
        # `ausente` continua diferente de `tentado-e-falhou` (25.2-b): registro
        # com `motivo_sem_url_busca` escrito passa, porque ali a tentativa esta
        # declarada. O que nao passa e o silencio.
        if af.get("url_busca_produto") and not af.get("url_busca"):
            piso_nao_rastreavel += 1
            if not af.get("motivo_sem_url_busca"):
                erro("%s: tem busca crua e nao tem busca ENCURTADA, e nao diz por que. "
                     "Desde 16/09/2026 o encurtamento e uma chamada de API (25.6) e nao "
                     "depende de sessao de ninguem; 25.2-b manda que a tentativa seja passo "
                     "do nascimento do registro. Rode "
                     "ferramentas/gerar-links-afiliado.py --escrever, ou escreva "
                     "`motivo_sem_url_busca` com o que a API respondeu" % onde)
        # 25.4-b: o endereco CRU da busca, que e o que a ronda abre para conferir
        # se a palavra-chave ainda traz resultado. Do link encurtado nao se chega
        # la sem clicar, e clicar o proprio link de afiliado e o que a 25.4 proibe.
        # TAMBEM VIROU ERRO DURO EM 25/09/2026, pelo mesmo motivo: os dez que
        # faltavam tiveram o par REESCOLHIDO inteiro (25.4-b.1) e o numero foi a
        # zero. Sem o endereco cru ninguem confere se a palavra-chave ainda traz
        # resultado — e as treze chaves das pastilhas provaram, no mesmo dia, que
        # chave escrita uma vez envelhece calada: devolviam zero oferta desde
        # 13/09 e nada acusava.
        if af.get("url_busca") and not af.get("url_busca_produto"):
            sem_busca_crua += 1
            erro("%s: tem busca ENCURTADA e nao tem o endereco CRU dela — 25.4-b. Do link "
                 "encurtado nao se chega a busca sem clicar, e clicar o proprio link de "
                 "afiliado e o que a 25.4 proibe: a palavra-chave fica sem quem a confira" % onde)
        if af.get("url") and not af.get("url_produto"):
            erro("%s: tem link de afiliado e nao tem url_produto — 25.4-b, link cuja saude "
                 "ninguem consegue conferir" % onde)
        if af.get("degrau") is not None and af["degrau"] not in (1, 2, 3, 4):
            erro("%s: degrau %r fora da escada da secao 25 (1 a 4)" % (onde, af["degrau"]))
        # O DEGRAU E COBRADO DE QUEM SERVE LINK, NAO DE QUEM TEM `url` (28/09/2026).
        #
        # Ate aqui esta linha cobrava `degrau` so de quem tinha `af["url"]` — a
        # ficha de produto —, e o esquema dizia o mesmo em
        # `obrigatorio_quando: "url estiver preenchida"`. Quem serve BUSCA nao
        # tem `url`, entao os treze itens de acabamento e alicate passavam com
        # `degrau: null` servindo degrau 4 na tela. Medido pela ronda da
        # Sentinela em 28/09/2026: 13 dos 38 itens do banco.
        #
        # Nao e cosmetico, e o motivo esta na 25.1: `degrau` e o campo pelo qual
        # a leitura semanal acha o que pode SUBIR de degrau. Item no 4 e item
        # com degrau em branco sao a mesma tela e leituras opostas — o primeiro
        # e uma oportunidade na fila, o segundo e invisivel. Treze itens em
        # `null` eram treze oportunidades que ninguem conseguia contar.
        #
        # A regra, na formulacao da 25.1: "o degrau usado fica gravado em
        # `afiliado.degrau`". Quem SERVE alguma saida de compra usou um degrau —
        # qualquer uma das quatro saidas, nao so a ficha. Quem nao serve
        # nenhuma ja e reprovado acima por `sem_saida`, entao esta linha nunca
        # cobra degrau de registro que nao tem o que declarar.
        _serve_compra = bool(af.get("url") or af.get("url_produto")
                             or af.get("url_busca") or af.get("url_busca_produto"))
        if SEM_PORTAO_DEGRAU:
            _serve_compra = bool(af.get("url"))
        if _serve_compra and af.get("degrau") is None:
            erro("%s: serve link de compra e nao diz de que degrau da escada ele veio — 25.1. "
                 "Item que serve so busca e degrau 4; a busca nao dispensa a declaracao, "
                 "ela E a declaracao" % onde)
        # A CONTAGEM POR DEGRAU, que e o que a leitura semanal le para achar o
        # que pode subir. Sem ela o portao diria "o campo esta preenchido" e
        # ninguem saberia preenchido COM O QUE — e 38 itens todos no 4 e um
        # banco que cumpre o esquema e nao rende nada.
        if af.get("degrau") in (1, 2, 3, 4):
            por_degrau[int(af["degrau"])] += 1

        # POR QUE ESTE ITEM PAROU NO DEGRAU 4 (30/09/2026) — despacho da ronda
        # diaria tecnica daquele dia, item 1.
        #
        # O portao do degrau, de 28/09, cobra que o degrau esteja ESCRITO. Ele
        # nao ve o degrau 4 que nao diz por que. Medido no `main` de 30/09: dos
        # 17 registros no 4, **12 traziam so `motivo_da_chave`** — texto como
        # `"familia: medida"`, que conta como a chave foi MONTADA e nao o que a
        # escada devolveu. Cinco escreviam o motivo de verdade e doze calavam, e
        # nada distinguia os dois estados.
        #
        # Nao e zelo de arquivo. A 25.4-b.4 diz que "nao casou" tem causas que
        # parecem uma — produto nao anunciado (so o mercado resolve) ou candidato
        # barrado por trava (resolve-se com trava melhor ou com um registro de
        # variante que falta) — e a 25.4-b.3 manda o campo separar a CAUSA, que
        # nao muda, da ULTIMA TENTATIVA, que muda a cada passada. Sem a segunda
        # escrita, a passada seguinte nao sabe se deve tentar de novo; e foi
        # exatamente assim que os 39 links da Aquametria passaram dez dias
        # carregando um motivo que mandava "nem tentar" e havia deixado de ser
        # verdade no quarto dia (25.4-b.3).
        #
        # O portao cobra a FORMA, nunca o texto: o marcador ` || `, a palavra
        # CAUSA com a classe entre parenteses e uma ULTIMA TENTATIVA com data
        # ISO. Quem escreve e `ferramentas/medir-degrau-4.py`, que mede a escada
        # pela Open API e classifica pelo laudo da regra de casamento.
        if af.get("degrau") == 4 and not af.get("url"):
            degrau_4_sem_ficha += 1
            motivo = af.get("motivo_sem_ficha") or ""
            partes = motivo.split(" || ")
            causa = partes[0].strip() if partes else ""
            tentativa = partes[1].strip() if len(partes) > 1 else ""
            casado = re.match(r"^CAUSA \(([a-z0-9-]+)\):\s*\S", causa)
            datada = re.match(r"^ULTIMA TENTATIVA (\d{4}-\d{2}-\d{2}):\s*\S", tentativa)
            if SEM_PORTAO_MOTIVO_DEGRAU_4:
                pass
            elif not motivo.strip():
                erro("%s: esta no degrau 4 e nao diz POR QUE — 25.4-b.4. `motivo_da_chave` "
                     "conta como a chave foi montada, nao o que a escada devolveu. Rode "
                     "ferramentas/medir-degrau-4.py --gravar" % onde)
            elif not casado or not datada:
                erro("%s: tem motivo do degrau 4 fora da forma da 25.4-b.3 — a causa (que nao "
                     "muda) e a ultima tentativa (que muda a cada passada) se separam por ' || ', "
                     "e a tentativa leva data ISO: `CAUSA (<classe>): ... || ULTIMA TENTATIVA "
                     "<AAAA-MM-DD>: ...`. Sem as duas metades, ou a prosa cresce sem fim ou a "
                     "causa e apagada pela tentativa de hoje" % onde)
            else:
                degrau_4_com_motivo += 1
                classe = casado.group(1)
                por_causa_do_degrau_4[classe] = por_causa_do_degrau_4.get(classe, 0) + 1

        # O CASAMENTO SE RECONFERE, NAO SE ACREDITA (29/09/2026).
        #
        # Dez registros ganharam ficha de produto em 29/09/2026 porque um anuncio
        # da Shopee foi provadamente daquele SKU, pela regra de
        # `ferramentas/casar-anuncio.py`. A prova ficou gravada em
        # `afiliado.casamento`, com o titulo do anuncio que a produziu.
        #
        # Titulo gravado e procedencia; procedencia que ninguem reconfere e
        # decoracao. Entao este portao NAO le o campo: ele passa o titulo
        # gravado pela regra VIVA e exige que ela continue identificando ESTE
        # registro e mais nenhum. No dia em que alguem afrouxar a regra, renomear
        # um registro ou acrescentar um irmao que o titulo tambem descreve, o
        # casamento para de valer e isto reprova — que e exatamente o que a
        # secao 4 do contrato pede: o resumo nao pode sobreviver ao fato.
        cas = af.get("casamento")
        if cas:
            for campo in ("casado_em", "regra", "degrau_da_palavra_chave",
                          "palavra_chave", "titulo_do_anuncio", "loja",
                          "item_id", "shop_id", "por_que_este_degrau_da_25_1",
                          "prova_de_vida"):
                if campo not in cas:
                    erro("%s / casamento: falta %s" % (onde, campo))
            if not af.get("url") or not af.get("url_produto"):
                erro("%s: tem casamento gravado e nao tem ficha — casamento sem `url` "
                     "e prova de uma coisa que nao esta no ar" % onde)
            casamentos_a_reconferir.append((onde, m, cas.get("titulo_do_anuncio") or ""))

        if m.get("imagem") is None:
            sem_imagem += 1
        else:
            for campo in ("url", "largura", "altura", "fonte", "coletado_em", "alt"):
                if campo not in m["imagem"]:
                    erro("%s / imagem: falta %s" % (onde, campo))

        # geometria obrigatoria em pastilha
        if m.get("categoria") == "pastilha":
            g = m.get("geometria")
            if not g:
                erro("%s: pastilha sem geometria" % onde)
            else:
                if g.get("espessura_mm") is None and not g.get("motivo"):
                    erro("%s / geometria: espessura null sem motivo" % onde)
                # CORRIGIDO no bloco 3d (12/09/2026). O L da formula L/raiz(N) e o lado da
                # PLACA, nao o da pastilha: com o exemplo do proprio `especificacao-calculadoras.md`
                # (placa 30x30 com 225 pastilhas -> passo 2,00 cm) a conta certa e 30/raiz(225);
                # a que estava escrita aqui usava `lado_anunciado_cm` e daria 1/15 = 0,07 cm.
                # Nunca disparou porque a categoria pastilha tinha zero itens ate este bloco.
                lado_placa = g.get("placa_lado_a_cm")
                lado_b = g.get("placa_lado_b_cm")
                n = g.get("pastilhas_por_placa")
                passo_declarado = g.get("passo_de_fabrica_cm")
                if n is None and not g.get("motivo_pastilhas_por_placa"):
                    erro("%s / geometria: pastilhas_por_placa null sem motivo escrito" % onde)
                if passo_declarado is None and not g.get("motivo_passo"):
                    erro("%s / geometria: passo_de_fabrica_cm null sem motivo escrito" % onde)
                if passo_declarado is not None and n is None:
                    erro("%s / geometria: passo de fabrica declarado sem pastilhas_por_placa que o sustente" % onde)
                if passo_declarado is not None and lado_b is not None and lado_placa is not None \
                        and abs(lado_b - lado_placa) > 0.001:
                    erro("%s / geometria: placa nao e quadrada (%s x %s), e L/raiz(N) nao se aplica"
                         % (onde, lado_placa, lado_b))
                if n and lado_placa and passo_declarado:
                    passo = round(lado_placa / (n ** 0.5), 2)
                    if abs(passo - passo_declarado) > 0.01:
                        erro("%s / geometria: passo de fabrica deveria ser %.2f cm (lado da PLACA / raiz(N))"
                             % (onde, passo))
                lado_past = g.get("lado_anunciado_cm")
                if passo_declarado is not None and lado_past is not None and passo_declarado < lado_past - 0.001:
                    erro("%s / geometria: passo (%s cm) menor que a propria pastilha (%s cm) — junta negativa"
                         % (onde, passo_declarado, lado_past))

        # ------------------------------------------------- categoria ACABAMENTO
        # A REGRA ESTA EM `regras_da_categoria_acabamento` DO ESQUEMA e nasceu em
        # 25/09/2026, junto com os sete primeiros registros. Ela esta aqui porque
        # regra escrita sem regua que a meca e promessa, e esta ilha ja pagou por
        # isso: o `no_banco` do cartao do Guia ficou zero com o banco cheio porque
        # ninguem media as duas listas juntas.
        #
        # O QUE ESTE PORTAO MEDE, e por que cada pedaco:
        #  - `protecao` existe e a frase do fabricante esta la, com fonte. Sem a
        #    frase literal nao ha como conferir o que foi lido dela.
        #  - as duas listas de vocabulario COBREM o vocabulario inteiro, sem
        #    sobreposicao. E a parte que mais importa: o que nao entra em nenhuma
        #    das duas e silencio NAO LIDO, e silencio nao lido e como faixa
        #    descoberta fica invisivel — foi assim que a espessura de 5 mm do
        #    alicate quase passou batida.
        #  - `momento_de_uso` sai do vocabulario e, quando e `nao_declarado`,
        #    escreve o motivo. Deduzir o momento pelo mecanismo do produto e
        #    afirmar pelo fabricante.
        #  - as propriedades tem NOME FIXO. Nome livre e o que faz a proxima
        #    execucao gravar `secagem_horas` onde esta gravou `tempo_de_secagem_h`.
        #  - `contato_com_alimento` e OBRIGATORIO mesmo (e principalmente) null:
        #    centro de mesa e tampo sao duas colecoes desta loja, e campo ausente
        #    e pergunta que ninguem faz.
        if m.get("categoria") == "acabamento" and not SEM_PORTAO_ACABAMENTO:
            pr = m.get("protecao")
            if not pr:
                erro("%s: acabamento sem o objeto `protecao`" % onde)
            else:
                if not pr.get("literal_do_fabricante"):
                    erro("%s / protecao: sem `literal_do_fabricante`" % onde)
                if pr.get("fonte_id") not in fontes:
                    erro("%s / protecao: `fonte_id` nao existe em fontes{}" % onde)
                mom = pr.get("momento_de_uso")
                if mom not in VOC["momento_de_uso"]:
                    erro("%s / protecao: momento_de_uso '%s' fora do vocabulario" % (onde, mom))
                if mom == "nao_declarado" and not pr.get("motivo_do_momento"):
                    erro("%s / protecao: momento_de_uso `nao_declarado` sem `motivo_do_momento`" % onde)
                # ACHADO PELA MUTACAO 05, ANTES DO COMMIT. Ate aqui o portao so
                # cobrava motivo no `nao_declarado` — e o defeito caro e o CONTRARIO:
                # gravar um momento que o fabricante nao declarou, deduzido do
                # mecanismo do produto (hidrofugante "obviamente" se passa depois de
                # rejuntar). Deducao com cara de declaracao e afirmar pelo fabricante,
                # que a secao 8 do ARQUIPELAGO.md proibe. Entao momento declarado
                # exige o TRECHO, e o trecho tem de ser pedaco da frase literal —
                # nao uma segunda frase escrita aqui, que seria a parafrase de novo.
                if mom and mom != "nao_declarado":
                    trecho = pr.get("trecho_que_declara_o_momento")
                    literal = pr.get("literal_do_fabricante") or ""
                    if not trecho:
                        erro("%s / protecao: momento_de_uso '%s' sem `trecho_que_declara_o_momento`. "
                             "Momento que o fabricante nao declarou e deducao, e deducao com cara de "
                             "declaracao e o defeito que a escada de fontes existe para impedir"
                             % (onde, mom))
                    elif trecho not in literal:
                        erro("%s / protecao: `trecho_que_declara_o_momento` nao e pedaco de "
                             "`literal_do_fabricante` — o trecho tem de sair da frase, nao ser "
                             "uma segunda frase escrita por quem preencheu" % onde)
                for voc, a, b in (
                        ("base", "bases_do_vocabulario_que_a_frase_nomeia",
                         "bases_do_vocabulario_que_a_frase_NAO_nomeia"),
                        ("material_tessela", "tesselas_do_vocabulario_que_a_frase_nomeia",
                         "tesselas_do_vocabulario_que_a_frase_NAO_nomeia")):
                    nomeia = pr.get(a)
                    nao = pr.get(b)
                    if not isinstance(nomeia, list) or not isinstance(nao, list):
                        erro("%s / protecao: `%s` e `%s` tem de ser listas" % (onde, a, b))
                        continue
                    inteiro = set(VOC[voc])
                    juntos = list(nomeia) + list(nao)
                    if len(juntos) != len(set(juntos)):
                        erro("%s / protecao: valor repetido entre `%s` e `%s`" % (onde, a, b))
                    faltando = sorted(inteiro - set(juntos))
                    sobrando = sorted(set(juntos) - inteiro)
                    if faltando:
                        erro("%s / protecao: as duas listas de `%s` nao cobrem o vocabulario — "
                             "ficou de fora: %s. O que nao entra em nenhuma das duas e silencio "
                             "NAO LIDO, e e assim que faixa descoberta fica invisivel"
                             % (onde, voc, ", ".join(faltando)))
                    if sobrando:
                        erro("%s / protecao: valor fora do vocabulario `%s`: %s"
                             % (onde, voc, ", ".join(sobrando)))
                if not isinstance(pr.get("nomeia_rejunte"), bool):
                    erro("%s / protecao: `nomeia_rejunte` tem de ser true ou false. REJUNTE nao e "
                         "valor de `base` nem de `material_tessela` e mesmo assim e metade da "
                         "superficie exposta de uma peca de mosaico" % onde)

            # ACHADO PELA MUTACAO 13, ANTES DO COMMIT. A regra dizia, desde que
            # nasceu, que a matriz base x ambiente fica VAZIA em acabamento — e
            # nenhuma regua media isso. Um verniz com `indicado_para` preenchido
            # entraria na traducao do mapa de termos e a F2 passaria a considerar
            # verniz onde ela decide COLA. A regra era prosa; agora e portao.
            decl = m.get("declaracoes") or {}
            preenchidas = sorted(k for k, v in decl.items() if v)
            if preenchidas:
                erro("%s / declaracoes: acabamento tem de nascer com as listas VAZIAS e "
                     "preencheu %s. A matriz base x ambiente e o eixo pelo qual a F2 escolhe "
                     "COLA; verniz dentro dela vira candidato a colar peca"
                     % (onde, ", ".join(preenchidas)))
            elif not m.get("motivo_declaracoes_vazias"):
                erro("%s: acabamento com `declaracoes` vazias e sem `motivo_declaracoes_vazias`. "
                     "Lista vazia sem motivo e indistinguivel de coleta que ninguem fez" % onde)

            props = m.get("propriedades") or {}
            nomes_fixos = set(esquema["regras_da_categoria_acabamento"]
                              ["as_propriedades_tem_NOME_FIXO_e_esta_e_a_lista"]["nomes"].keys())
            for pnome in props:
                if pnome not in nomes_fixos:
                    erro("%s / %s: propriedade de acabamento com nome fora da lista fixa do esquema. "
                         "Nome livre e o que faz a proxima execucao gravar o mesmo dado com outro "
                         "nome, e ai nenhuma regua compara dois registros" % (onde, pnome))
            if "contato_com_alimento" not in props:
                erro("%s: acabamento sem `contato_com_alimento`. O campo e obrigatorio mesmo quando "
                     "o fabricante nao declara nada — centro de mesa e tampo sao duas colecoes desta "
                     "loja, e campo ausente e pergunta que ninguem faz" % onde)
            av = (props.get("acabamento_visual") or {}).get("valor")
            if av is not None and av not in VOC["acabamento_visual"]:
                erro("%s / acabamento_visual: '%s' fora do vocabulario" % (onde, av))

        # ----------------------------------------------------- categoria BASE
        # A REGRA ESTA EM `regras_da_categoria_base` DO ESQUEMA e nasceu em
        # 28/09/2026, ANTES do primeiro SKU — de proposito, e e a primeira vez
        # nesta ilha que a ordem e essa. O motivo esta escrito no proprio esquema:
        # o canal de busca desta execucao devolveu resumo e traducao das paginas
        # de fabricante, e `literal_do_fabricante` e a viga do banco inteiro.
        # Portao que nasce antes do dado so vale se alguem provar que ele reprova,
        # e quem prova e `ferramentas/mutacoes-base.py`, que fabrica os registros.
        #
        # O QUE ESTE PORTAO MEDE que os outros nao mediam:
        #  - `valor_do_vocabulario_base` e UM valor, nao lista: uma base e feita de
        #    um material so.
        #  - quando ele e `sem_valor_no_vocabulario`, a PONTE tem de concordar. E a
        #    trava que impede um registro de inventar um buraco que a ponte nao
        #    reconhece — ou, pior, de esconder um que ela reconhece gravando o
        #    valor vizinho (barro cru entrando como ceramica esmaltada, que
        #    absorvem de maneira oposta).
        #  - `trecho_que_declara_o_material` e pedaco LITERAL da frase, herdado da
        #    mutacao 05 do acabamento: 'disco MDF 20 cm' e nome comercial, e nome
        #    comercial nao e declaracao tecnica.
        #  - `absorcao_declarada` e obrigatorio mesmo null, pelo mesmo motivo que
        #    `contato_com_alimento` e no acabamento: e a pergunta que decide a
        #    regra 6 da F2 e a que separa barro cru de ceramica esmaltada.
        if m.get("categoria") == "base" and not SEM_PORTAO_BASE:
            sub = m.get("substrato")
            if not sub:
                erro("%s: base sem o objeto `substrato`" % onde)
            else:
                if not sub.get("literal_do_fabricante"):
                    erro("%s / substrato: sem `literal_do_fabricante`" % onde)
                if sub.get("fonte_id") not in fontes:
                    erro("%s / substrato: `fonte_id` nao existe em fontes{}" % onde)
                val = sub.get("valor_do_vocabulario_base")
                if isinstance(val, list):
                    erro("%s / substrato: `valor_do_vocabulario_base` e UM valor, nao lista. Uma "
                         "base e feita de um material so; produto que o fabricante descreve com "
                         "dois materiais sao dois registros" % onde)
                elif val == "sem_valor_no_vocabulario":
                    if not sub.get("motivo_sem_valor"):
                        erro("%s / substrato: `sem_valor_no_vocabulario` sem `motivo_sem_valor`" % onde)
                    tipo_do_registro = m.get("tipo")
                    na_ponte = ((PONTE or {}).get("tipos") or {}).get(tipo_do_registro) or {}
                    if na_ponte.get("estado") != "sem_valor_no_vocabulario":
                        erro("%s / substrato: o registro diz `sem_valor_no_vocabulario` e a ponte "
                             "diz '%s' para o tipo '%s'. Buraco que so o registro enxerga e buraco "
                             "que some quando o registro sair"
                             % (onde, na_ponte.get("estado"), tipo_do_registro))
                elif val not in BASES:
                    erro("%s / substrato: `valor_do_vocabulario_base` '%s' fora de "
                         "`vocabularios.base`" % (onde, val))
                else:
                    trecho = sub.get("trecho_que_declara_o_material")
                    literal = sub.get("literal_do_fabricante") or ""
                    if not trecho:
                        erro("%s / substrato: `valor_do_vocabulario_base` '%s' sem "
                             "`trecho_que_declara_o_material`. Material deduzido do nome comercial "
                             "passa com cara de declaracao do fabricante, e nome comercial nao e "
                             "declaracao tecnica" % (onde, val))
                    elif trecho not in literal:
                        erro("%s / substrato: `trecho_que_declara_o_material` nao e pedaco de "
                             "`literal_do_fabricante`" % onde)
                    # A PONTE MANDA TAMBEM DO LADO DE CA: registro cujo tipo a ponte
                    # diz que POUSA tem de pousar onde ela diz. Senao a ponte vira
                    # documento e o registro vira a verdade, que e a divergencia que
                    # a secao 4 do contrato chama de resumo velho lido como fato.
                    na_ponte = ((PONTE or {}).get("tipos") or {}).get(m.get("tipo")) or {}
                    # ACHADO PELA MUTACAO 05, ANTES DO COMMIT, e e o defeito mais
                    # caro desta categoria. Ate aqui a ponte so era consultada
                    # quando o REGISTRO dizia `sem_valor_no_vocabulario` — e o
                    # caminho caro e o contrario: o registro grava um valor de
                    # verdade num tipo que a ponte diz que NAO POUSA. Vaso de barro
                    # cru entrando como `ceramica_esmaltada_porcelana` nao deixa
                    # rastro nenhum: some um buraco declarado e nasce, no lugar
                    # dele, uma recomendacao de cola para uma superficie que
                    # absorve ao contrario da que foi respondida. O registro ficaria
                    # verde, a ponte continuaria dizendo a verdade, e as duas nunca
                    # se encontrariam.
                    if na_ponte.get("estado") == "sem_valor_no_vocabulario":
                        erro("%s / substrato: a ponte diz que o tipo '%s' NAO tem valor no "
                             "vocabulario e o registro gravou '%s'. Buraco escondido atras do "
                             "valor vizinho e o unico defeito desta categoria que nao deixa "
                             "rastro: some a faixa descoberta e nasce uma recomendacao sobre "
                             "uma superficie que ninguem perguntou. Enquanto a ponte nao for "
                             "executada, o registro diz `sem_valor_no_vocabulario` com o "
                             "motivo — e e isso que a tela mostra"
                             % (onde, m.get("tipo"), val))
                    if na_ponte.get("estado") == "pousa" and val not in (na_ponte.get("pousa_em") or []):
                        erro("%s / substrato: a ponte diz que o tipo '%s' pousa em %s e o registro "
                             "gravou '%s'" % (onde, m.get("tipo"),
                                              ", ".join(na_ponte.get("pousa_em") or []), val))
                    if na_ponte.get("estado") == "nao_e_material":
                        # moldura: o registro aponta para o material DELA, e isso e
                        # certo — mas tem de ser um valor do eixo, nunca o proprio
                        # nome do tipo.
                        if val == m.get("tipo"):
                            erro("%s / substrato: o tipo '%s' nao e material (ponte) e o registro "
                                 "gravou o proprio nome do tipo como base" % (onde, m.get("tipo")))
                nomeia = sub.get("ambientes_do_vocabulario_que_a_frase_nomeia")
                nao = sub.get("ambientes_do_vocabulario_que_a_frase_NAO_nomeia")
                if not isinstance(nomeia, list) or not isinstance(nao, list):
                    erro("%s / substrato: as duas listas de ambiente tem de existir e ser listas" % onde)
                else:
                    juntos = list(nomeia) + list(nao)
                    if len(juntos) != len(set(juntos)):
                        erro("%s / substrato: ambiente repetido entre as duas listas" % onde)
                    faltam = sorted(AMBIENTES - set(juntos))
                    sobram = sorted(set(juntos) - AMBIENTES)
                    if faltam:
                        erro("%s / substrato: as duas listas de ambiente nao cobrem o vocabulario — "
                             "ficou de fora: %s. O que nao entra em nenhuma das duas e silencio NAO "
                             "LIDO" % (onde, ", ".join(faltam)))
                    if sobram:
                        erro("%s / substrato: ambiente fora do vocabulario: %s"
                             % (onde, ", ".join(sobram)))
                if "preparo_declarado" not in sub:
                    erro("%s / substrato: sem `preparo_declarado`. O campo e obrigatorio mesmo "
                         "quando o fabricante nao manda preparar nada — e o mesmo preparo que o "
                         "selador do banco declara em `momento_de_uso: antes_de_colar`, visto do "
                         "outro lado" % onde)

            decl = m.get("declaracoes") or {}
            preenchidas = sorted(k for k, v in decl.items() if v)
            if preenchidas:
                erro("%s / declaracoes: base tem de nascer com as listas VAZIAS e preencheu %s. "
                     "`indicado_para` quer dizer 'este produto adere sobre estas superficies', e "
                     "uma base nao adere sobre nada — ela E a superficie. Um disco de MDF ali "
                     "dentro faz a F2 oferecer madeira como candidata a COLAR madeira"
                     % (onde, ", ".join(preenchidas)))
            elif not m.get("motivo_declaracoes_vazias"):
                erro("%s: base com `declaracoes` vazias e sem `motivo_declaracoes_vazias`" % onde)

            props = m.get("propriedades") or {}
            nomes_fixos = set(esquema["regras_da_categoria_base"]
                              ["as_propriedades_tem_NOME_FIXO_e_esta_e_a_lista"]["nomes"].keys())
            for pnome in props:
                if pnome not in nomes_fixos:
                    erro("%s / %s: propriedade de base com nome fora da lista fixa do esquema. Aqui "
                         "as propriedades sao MEDIDA, e medida com nome livre e o que faz um "
                         "registro gravar `diametro_cm` e o seguinte `d_cm`" % (onde, pnome))
            if "absorcao_declarada" not in props:
                erro("%s: base sem `absorcao_declarada`. O campo e obrigatorio mesmo quando o "
                     "fabricante nao declara nada — a base absorver ou nao e o que decide a regra 6 "
                     "da F2 e o que separa barro cru de ceramica esmaltada" % onde)
            fo = (props.get("forma") or {}).get("valor")
            if fo is not None and fo not in VOC["forma_da_base"]:
                erro("%s / forma: '%s' fora de `vocabularios.forma_da_base`, que e a lista de formas "
                     "que a F1 calcula" % (onde, fo))

        # ---------------------------------------------------- categoria APOIO
        # A REGRA ESTA EM `regras_da_categoria_apoio` DO ESQUEMA e nasceu em
        # 28/09/2026, ANTES do primeiro SKU, como a da base seis horas antes.
        #
        # O QUE ESTE PORTAO MEDE que nenhum outro mede:
        #  - `servico.ramo` tem de concordar com a ponte NAS DUAS DIRECOES. E a
        #    trava que a mutacao 05 da base ensinou: ponte consultada so num
        #    sentido vira documento, e o registro vira a verdade.
        #  - `material_de_contato` e obrigatorio, e nao e detalhe: a unica frase
        #    de fabricante do banco que nomeia um apoio nomeia o MATERIAL dele —
        #    "desempenadeira de borracha para nao riscar". Gravar so
        #    "desempenadeira" perde a metade da declaracao que decide se a
        #    pastilha de vidro sai riscada.
        #  - `etapa` sai de `etapa_da_montagem` e NAO de `momento_de_uso`: aquele
        #    vocabulario nao tem valor para o ato de COLAR, porque nasceu para o
        #    acabamento, que por definicao nunca cola.
        #  - `risco_declarado` e OBRIGATORIO mesmo null, pelo mesmo motivo que
        #    `contato_com_alimento` no acabamento e `absorcao_declarada` na base:
        #    e a pergunta que o campo ausente faz ninguem fazer, e aqui ela e a
        #    pergunta de quem esta com epoxi na mao.
        if m.get("categoria") == "apoio" and not SEM_PORTAO_APOIO:
            sv = m.get("servico")
            if not sv:
                erro("%s: apoio sem o objeto `servico`" % onde)
            else:
                literal = sv.get("literal_do_fabricante") or ""
                if not literal:
                    erro("%s / servico: sem `literal_do_fabricante`" % onde)
                if sv.get("fonte_id") not in fontes:
                    erro("%s / servico: `fonte_id` nao existe em fontes{}" % onde)

                ramo = sv.get("ramo")
                if ramo not in set(VOC.get("ramo_do_apoio") or []):
                    erro("%s / servico: ramo '%s' fora de `vocabularios.ramo_do_apoio`"
                         % (onde, ramo))
                else:
                    na_ponte = ((PONTE_APOIO or {}).get("tipos") or {}).get(m.get("tipo")) or {}
                    if na_ponte and na_ponte.get("ramo") != ramo:
                        erro("%s / servico: a ponte diz que o tipo '%s' e do ramo '%s' e o registro "
                             "gravou '%s'. Ferramenta gravada como EPI some da lista de quem "
                             "monta e aparece na de quem se protege — e o contrario poe uma luva "
                             "onde a artesa procura o que encosta na peca"
                             % (onde, m.get("tipo"), na_ponte.get("ramo"), ramo))

                mat = sv.get("material_de_contato")
                if mat not in set(VOC.get("material_de_contato_do_apoio") or []):
                    erro("%s / servico: `material_de_contato` '%s' fora de "
                         "`vocabularios.material_de_contato_do_apoio`" % (onde, mat))
                elif mat == "nao_declarado":
                    if not sv.get("motivo_material_de_contato"):
                        erro("%s / servico: `material_de_contato` nao declarado e sem "
                             "`motivo_material_de_contato`" % onde)
                else:
                    trecho = sv.get("trecho_que_declara_o_material_de_contato")
                    if not trecho:
                        erro("%s / servico: `material_de_contato` '%s' sem "
                             "`trecho_que_declara_o_material_de_contato`. Material deduzido do "
                             "nome comercial passa com cara de declaracao do fabricante"
                             % (onde, mat))
                    elif trecho not in literal:
                        erro("%s / servico: `trecho_que_declara_o_material_de_contato` nao e "
                             "pedaco de `literal_do_fabricante`" % onde)

                etapa = sv.get("etapa")
                if etapa not in set(VOC.get("etapa_da_montagem") or []):
                    erro("%s / servico: `etapa` '%s' fora de `vocabularios.etapa_da_montagem`"
                         % (onde, etapa))
                elif etapa == "nao_declarada":
                    if not sv.get("motivo_da_etapa"):
                        erro("%s / servico: `etapa` nao declarada e sem `motivo_da_etapa`" % onde)
                else:
                    trecho = sv.get("trecho_que_declara_a_etapa")
                    if not trecho:
                        erro("%s / servico: `etapa` '%s' sem `trecho_que_declara_a_etapa`. Etapa "
                             "deduzida do mecanismo do produto e deducao com cara de declaracao"
                             % (onde, etapa))
                    elif trecho not in literal:
                        erro("%s / servico: `trecho_que_declara_a_etapa` nao e pedaco de "
                             "`literal_do_fabricante`" % onde)

                nomeia = sv.get("tesselas_do_vocabulario_que_a_frase_nomeia")
                nao = sv.get("tesselas_do_vocabulario_que_a_frase_NAO_nomeia")
                if not isinstance(nomeia, list) or not isinstance(nao, list):
                    erro("%s / servico: as duas listas de tessela tem de existir e ser listas" % onde)
                else:
                    juntos = list(nomeia) + list(nao)
                    if len(juntos) != len(set(juntos)):
                        erro("%s / servico: tessela repetida entre as duas listas" % onde)
                    inteiro = set(VOC["material_tessela"])
                    faltam = sorted(inteiro - set(juntos))
                    sobram = sorted(set(juntos) - inteiro)
                    if faltam:
                        erro("%s / servico: as duas listas de tessela nao cobrem o vocabulario — "
                             "ficou de fora: %s. O que nao entra em nenhuma das duas e silencio "
                             "NAO LIDO" % (onde, ", ".join(faltam)))
                    if sobram:
                        erro("%s / servico: tessela fora do vocabulario: %s"
                             % (onde, ", ".join(sobram)))

                if not isinstance(sv.get("age_sobre_rejunte"), bool):
                    erro("%s / servico: `age_sobre_rejunte` tem de ser true ou false. A unica "
                         "ocorrencia de apoio medida no banco declara a desempenadeira para "
                         "REMOVER O EXCESSO DE REJUNTE, e rejunte nao e valor de `material_tessela` "
                         "nem de `base` — sem este campo a pergunta nao e feita a registro nenhum"
                         % onde)

            decl = m.get("declaracoes") or {}
            preenchidas = sorted(k for k, v in decl.items() if v)
            if preenchidas:
                erro("%s / declaracoes: apoio tem de nascer com as listas VAZIAS e preencheu %s. "
                     "A matriz base x ambiente e o eixo pelo qual a F2 escolhe COLA, e uma "
                     "desempenadeira ali dentro vira candidata a colar peca"
                     % (onde, ", ".join(preenchidas)))
            elif not m.get("motivo_declaracoes_vazias"):
                erro("%s: apoio com `declaracoes` vazias e sem `motivo_declaracoes_vazias`" % onde)

            props = m.get("propriedades") or {}
            nomes_fixos = set(esquema["regras_da_categoria_apoio"]
                              ["as_propriedades_tem_NOME_FIXO_e_esta_e_a_lista"]["nomes"].keys())
            for pnome in props:
                if pnome not in nomes_fixos:
                    erro("%s / %s: propriedade de apoio com nome fora da lista fixa do esquema. "
                         "Nome livre e o que faz a segunda execucao gravar `dureza` onde a "
                         "primeira gravou `dureza_shore_a`" % (onde, pnome))
            if "risco_declarado" not in props:
                erro("%s: apoio sem `risco_declarado`. O campo e obrigatorio mesmo quando o "
                     "fabricante nao declara nada — no EPI e o risco de que o item protege, na "
                     "ferramenta e o dano que ela pode causar a peca, e a ilha recomenda epoxi "
                     "sem uma unica declaracao de protecao no banco" % onde)

    # o cabecalho do arquivo declara numeros; eles tem que bater com a contagem
    dec_link = (arq.get("afiliado") or {}).get("itens_esperando_link")
    dec_img = (arq.get("imagens") or {}).get("itens_sem_imagem")
    conta_link = sum(1 for m in arq.get("materiais", []) if (m.get("afiliado") or {}).get("url") == "")
    conta_img = sum(1 for m in arq.get("materiais", []) if m.get("imagem") is None)
    if dec_link is not None and dec_link != conta_link:
        erro("%s: cabecalho declara %s itens esperando link, o arquivo tem %s" % (nome, dec_link, conta_link))
    if dec_img is not None and dec_img != conta_img:
        erro("%s: cabecalho declara %s itens sem imagem, o arquivo tem %s" % (nome, dec_img, conta_img))

    # O PISO TAMBEM E NUMERO DE CABECALHO, e pela mesma razao que o link: numero
    # que o arquivo declara e a regua reconta nao envelhece calado.
    #
    # O NOME DO CAMPO MUDOU EM 14/09/2026 E O CAMPO VELHO E RECUSADO DE PROPOSITO.
    # `itens_sem_piso` contava quem nao tinha a busca ENCURTADA e chamava isso de
    # "sem piso" — duas perguntas coladas numa so, que davam o mesmo numero
    # enquanto nenhum item tinha busca crua. Deixar o nome velho conviver com o
    # significado novo seria a pior das saidas: o numero continuaria batendo e
    # diria outra coisa. Entao o cabecalho declara os DOIS numeros, com os nomes
    # que dizem o que eles sao, e quem deixar o campo velho para tras e avisado.
    afh = arq.get("afiliado") or {}
    if "itens_sem_piso" in afh:
        erro("%s: o cabecalho ainda declara `itens_sem_piso`, campo aposentado em 14/09/2026 "
             "porque media quem nao tinha a busca ENCURTADA e chamava isso de sem piso. "
             "Declare `itens_sem_saida_de_compra` e `itens_com_piso_nao_rastreavel`" % nome)

    def _sem_saida(m):
        af = m.get("afiliado") or {}
        return not af.get("url") and not af.get("url_busca") and not af.get("url_busca_produto")

    def _nao_rastreavel(m):
        af = m.get("afiliado") or {}
        return bool(af.get("url_busca_produto")) and not af.get("url_busca")

    for campo, conta in (("itens_sem_saida_de_compra", sum(1 for m in arq.get("materiais", []) if _sem_saida(m))),
                         ("itens_com_piso_nao_rastreavel", sum(1 for m in arq.get("materiais", []) if _nao_rastreavel(m)))):
        declarado = afh.get(campo)
        if declarado is None:
            erro("%s: o cabecalho nao declara `afiliado.%s`; o arquivo tem %s"
                 % (nome, campo, conta))
        elif declarado != conta:
            erro("%s: cabecalho declara %s em `%s`, o arquivo tem %s"
                 % (nome, declarado, campo, conta))


# ------------------ A VARREDURA DO APOIO DECLARADO PELO RESTO DO BANCO (28/09/2026)
# A categoria `apoio` e a unica cuja declaracao que mais importa vem DO OUTRO LADO
# DO BALCAO: nao e o fabricante da desempenadeira que diz qual desempenadeira usar,
# e o fabricante da PASTILHA. A Pastilhart escreve "desempenadeira de borracha para
# nao riscar" no assentamento da AF1500, e as 13 pastilhas do banco sao de vidro.
#
# O preco ja estava pago antes desta secao existir, igual ao que aconteceu com a
# `base` na mesma manha: CINCO frases, em QUATRO registros de TRES categorias,
# nomeiam um apoio — e nenhuma tinha campo para onde ir. Foram lidas, classificadas
# e descartadas em silencio.
#
# O portao anda nas DUAS direcoes, como as duas listas de vocabulario do `servico`:
# ocorrencia encontrada tem de estar listada, e ocorrencia listada tem de ser
# encontrada. Sem a segunda metade, uma linha sobreviveria a saida do registro que
# a sustentava, e a secao viraria o "resumo velho lido como fato" da secao 4 do
# contrato.
IND_APOIO = esquema.get("exigencias_de_apoio_ja_declaradas_no_banco")
if IND_APOIO is None and not SEM_PORTAO_APOIO:
    erro("esquema sem `exigencias_de_apoio_ja_declaradas_no_banco`. Sem ela, frase de fabricante "
         "que nomeia ferramenta de apoio continua sendo lida e jogada fora sem ninguem ver")
elif IND_APOIO is not None and not SEM_PORTAO_APOIO:
    ESTADOS_DO_TERMO = ("pousa", "sem_valor_no_vocabulario", "nao_e_ferramenta")
    TIPOS_APOIO = set(VOC["tipo_por_categoria"]["apoio"])
    vigiados = IND_APOIO.get("termos_vigiados")
    if not isinstance(vigiados, dict) or not vigiados:
        erro("varredura de apoio: `termos_vigiados` tem de ser um objeto nao vazio")
        vigiados = {}
    campos_fab = IND_APOIO.get("campos_que_carregam_frase_de_fabricante")
    if not isinstance(campos_fab, list) or not campos_fab:
        erro("varredura de apoio: `campos_que_carregam_frase_de_fabricante` tem de ser uma lista "
             "nao vazia. Varrer o registro inteiro leria a nossa propria `observacao` como se "
             "fosse frase de fabricante")
        campos_fab = []

    for termo, linha in sorted(vigiados.items()):
        linha = linha or {}
        est = linha.get("estado")
        if est not in ESTADOS_DO_TERMO:
            erro("varredura de apoio / %s: estado '%s' fora da lista (%s)"
                 % (termo, est, ", ".join(ESTADOS_DO_TERMO)))
            continue
        if est == "pousa":
            if linha.get("tipo_de_apoio") not in TIPOS_APOIO:
                erro("varredura de apoio / %s: estado `pousa` apontando para '%s', que nao existe "
                     "em `tipo_por_categoria.apoio`" % (termo, linha.get("tipo_de_apoio")))
        elif est == "sem_valor_no_vocabulario":
            proposto = linha.get("valor_proposto")
            if not proposto:
                erro("varredura de apoio / %s: `sem_valor_no_vocabulario` sem `valor_proposto`. "
                     "Buraco sem nome e buraco que a proxima execucao redescobre do zero" % termo)
            elif proposto in TIPOS_APOIO:
                erro("varredura de apoio / %s: `valor_proposto` '%s' JA existe em "
                     "`tipo_por_categoria.apoio` — entao o termo pousa e o estado esta errado"
                     % (termo, proposto))
            if not linha.get("o_que_falta"):
                erro("varredura de apoio / %s: `sem_valor_no_vocabulario` sem `o_que_falta`" % termo)
            if not linha.get("motivo"):
                erro("varredura de apoio / %s: `sem_valor_no_vocabulario` sem `motivo`" % termo)
        elif est == "nao_e_ferramenta":
            if not linha.get("onde_ele_e"):
                erro("varredura de apoio / %s: `nao_e_ferramenta` sem `onde_ele_e`. Termo que nao "
                     "e apoio tem de dizer onde ele mora, senao a proxima execucao o le como "
                     "buraco de vocabulario" % termo)
            if not linha.get("motivo"):
                erro("varredura de apoio / %s: `nao_e_ferramenta` sem `motivo`" % termo)

    def _frases_do_registro(reg):
        """So os campos que carregam frase de FABRICANTE. A nossa `observacao` fica de
        fora de proposito: varrer o registro inteiro leria o nosso julgamento como
        declaracao, que e a familia do numero de tela digitado."""
        saida = []

        def anda(obj, caminho):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    anda(v, "%s.%s" % (caminho, k) if caminho else k)
            elif isinstance(obj, list):
                for i, v in enumerate(obj):
                    anda(v, "%s[%d]" % (caminho, i))
            elif isinstance(obj, str):
                saida.append((caminho, obj))

        for campo in campos_fab:
            if campo in reg:
                anda(reg[campo], campo)
        return saida

    encontradas = set()
    for ident, reg in materiais.items():
        # O REGISTRO DE APOIO FICA DE FORA, e isso e a definicao da secao e nao uma
        # excecao aberta para caber: o que se mede aqui e declaracao que veio DO
        # OUTRO LADO DO BALCAO e nao tinha onde morar. A frase de um fabricante de
        # desempenadeira sobre a propria desempenadeira ja tem campo — e o objeto
        # `servico`, medido acima, registro por registro.
        if reg.get("categoria") == "apoio":
            continue
        for caminho, texto in _frases_do_registro(reg):
            alvo_txt = normalizar(texto)
            for termo in vigiados:
                if re.search(r"\b%s\b" % re.escape(normalizar(termo)), alvo_txt):
                    # A CHAVE E (registro, CAMPO, termo) E NAO (registro, termo).
                    # ACHADO PELA MUTACAO 15, ANTES DO COMMIT: a AF1500 nomeia a
                    # desempenadeira em DOIS campos, e com a chave por registro
                    # apagar uma das duas linhas passava verde — a outra cobria a
                    # que sumiu. A propria secao do esquema ja dizia "a varredura
                    # mede CAMPO, nao registro"; era prosa, e a prosa e que estava
                    # certa. Mesma familia da mutacao 05 da base: portao que mede
                    # numa granularidade e descrito noutra.
                    encontradas.add((ident, caminho, termo))

    listadas = set()
    for oc in IND_APOIO.get("ocorrencias") or []:
        if not isinstance(oc, dict):
            erro("varredura de apoio: ocorrencia que nao e objeto")
            continue
        reg_id = oc.get("registro")
        termo = oc.get("termo")
        for campo in ("registro", "arquivo", "categoria", "campo", "termo", "trecho", "o_que_obriga"):
            if not oc.get(campo):
                erro("varredura de apoio / %s / %s: ocorrencia sem `%s`"
                     % (reg_id, termo, campo))
        if termo not in vigiados:
            erro("varredura de apoio / %s: ocorrencia com termo '%s' que nao esta em "
                 "`termos_vigiados` — termo nao vigiado nao e medido em registro nenhum"
                 % (reg_id, termo))
        if reg_id not in materiais:
            erro("varredura de apoio: ocorrencia aponta para o registro '%s', que nao existe no "
                 "banco. Linha que sobrevive ao registro que a sustentava e resumo velho lido "
                 "como fato" % reg_id)
        listadas.add((reg_id, oc.get("campo"), termo))

    for ident, campo, termo in sorted(encontradas - listadas):
        erro("varredura de apoio: o registro '%s' nomeia '%s' em `%s`, que e frase de fabricante, "
             "e a ocorrencia NAO esta em "
             "`exigencias_de_apoio_ja_declaradas_no_banco.ocorrencias`. Declaracao lida e jogada "
             "fora por falta de campo nosso e o buraco que esta secao existe para fechar"
             % (ident, termo, campo))
    for ident, campo, termo in sorted(listadas - encontradas):
        if ident in materiais:
            erro("varredura de apoio: a ocorrencia '%s / %s / %s' esta listada e a varredura NAO a "
                 "encontra mais. Ou a frase do fabricante mudou, ou o termo saiu dos vigiados — "
                 "nos dois casos a lista virou historia e parou de ser portao"
                 % (ident, campo, termo))

    # (2) PROPOSTA DE VALOR NOVO TEM DE SER SUSTENTADA POR FRASE, NAO POR UM CAMPO
    # DE VALOR QUE NOS MESMOS CRIAMOS. ACHADO PELA MUTACAO 20, ANTES DO COMMIT.
    # `aerossol` aparece uma vez so no banco, e aparece em
    # `propriedades.forma_de_aplicacao.valor` — que e um slot do NOSSO esquema, nao
    # uma frase do fabricante. Trocar o estado dele para
    # `sem_valor_no_vocabulario` passava verde, e a proxima execucao criaria um
    # tipo de apoio chamado aerossol, que e EMBALAGEM e nao ferramenta. Os termos
    # que de fato propoem valor novo — `pincel` e `rolo` — aparecem em `preparo` e
    # em `literal_do_fabricante`, que sao prosa de fabricante. `literal_do_fabricante`
    # e a viga deste esquema inteiro; propor crescimento de vocabulario a partir de
    # um campo nosso e a mesma familia do numero de tela digitado.
    por_termo = {}
    for ident, campo, termo in encontradas:
        por_termo.setdefault(termo, set()).add(campo)

    def _e_frase(campo):
        partes = (campo or "").split(".")
        return not (len(partes) == 3 and partes[0] == "propriedades" and partes[2] == "valor")

    for termo, linha in sorted(vigiados.items()):
        if (linha or {}).get("estado") != "sem_valor_no_vocabulario":
            continue
        campos_do_termo = por_termo.get(termo) or set()
        if campos_do_termo and not any(_e_frase(c) for c in campos_do_termo):
            erro("varredura de apoio / %s: o termo propoe valor novo para "
                 "`tipo_por_categoria.apoio` e so aparece em campo de VALOR do nosso proprio "
                 "esquema (%s), nunca numa frase de fabricante. Vocabulario que cresce a partir "
                 "de um slot nosso nao esta lendo declaracao nenhuma — e o que separa `pincel` e "
                 "`rolo`, que a Cascola e a Quartzolit escrevem em prosa, de `aerossol`, que so "
                 "existe porque nos criamos o campo `forma_de_aplicacao`"
                 % (termo, ", ".join(sorted(campos_do_termo))))

    # A REGRA DE CRESCIMENTO DO VOCABULARIO DE MATERIAL DE CONTATO. `borracha` e
    # `espuma` existem porque DUAS frases de fabricante as declaram (a AF1500 e o
    # verniz de pisos). Um terceiro valor so pode nascer com a terceira frase:
    # vocabulario que cresce por previsao vira promessa vazia.
    declarados = {oc.get("material_de_contato_declarado")
                  for oc in (IND_APOIO.get("ocorrencias") or []) if isinstance(oc, dict)}
    declarados |= {(reg.get("servico") or {}).get("material_de_contato")
                   for reg in materiais.values() if reg.get("categoria") == "apoio"}
    for valor in VOC.get("material_de_contato_do_apoio") or []:
        if valor == "nao_declarado":
            continue
        if valor not in declarados:
            erro("varredura de apoio: `material_de_contato_do_apoio` traz '%s' e nenhuma frase de "
                 "fabricante do banco o declara, nem ha registro de apoio que o use. Vocabulario "
                 "que cresce por previsao vira promessa vazia" % valor)


# ------------------------------------------- as cinco regras de elegibilidade

_perfis = {}


def perfil(m):
    """Traduz as declaracoes literais do fabricante para o vocabulario da ilha."""
    if m.get("id") in _perfis:
        return _perfis[m["id"]]
    d = m.get("declaracoes") or {}
    onde = m.get("id")
    ind_b, ind_a, vagos = traduzir(d.get("indicado_para"), onde)
    proib_b1, proib_a1, _ = traduzir(d.get("nao_usar_em"), onde)
    proib_b2, proib_a2, _ = traduzir(d.get("nao_indicado_para"), onde)
    naorec_b, _, naorec_vagos = traduzir(d.get("nao_recomendado_em"), onde)
    delim_b, delim_a, _ = traduzir(d.get("ambientes_declarados"), onde)
    _, resist_a, _ = traduzir(d.get("resistencias_declaradas"), onde)
    if delim_b:
        aviso("%s: ambientes_declarados traduziu para BASE ('%s'), o que nao faz sentido" % (onde, ", ".join(sorted(delim_b))))
    _perfis[m.get("id")] = {
        "bases_indicadas": ind_b,
        "bases_proibidas": proib_b1 | proib_b2,
        "bases_nao_recomendadas": naorec_b | naorec_vagos | vagos,
        "ambientes_proibidos": proib_a1 | proib_a2,
        "ambientes_delimitados": delim_a,
        "ambientes_cobertos": delim_a | resist_a | ind_a,
        "nivel": min((f["nivel"] for f in (m.get("fontes") or {}).values()), default=9),
    }
    return _perfis[m.get("id")]


def avaliar(m, base, ambiente):
    """Devolve (situacao, score). Situacao: recomendado | ressalva | proibido | silencio."""
    p = perfil(m)
    if base in p["bases_proibidas"] or ambiente in p["ambientes_proibidos"]:
        return "proibido", 0                                        # regra 1
    if base not in p["bases_indicadas"]:
        return "silencio", 0                                        # regra 2
    if p["ambientes_delimitados"] and ambiente not in p["ambientes_delimitados"]:
        return "silencio", 0                                        # regra 3
    if ambiente in CRITICOS and ambiente not in p["ambientes_cobertos"]:
        return "silencio", 0                                        # regra 4
    score = 2 + (2 if ambiente in p["ambientes_cobertos"] else 0)
    if p["nivel"] > NIVEL_MAX:
        return "ressalva", score                                    # regra 5
    return "recomendado", score


def computar_celula(base, ambiente):
    """A matriz da F2 e de COLA. Nada mais entra nela.

    Ate o bloco 3c esta funcao varria o banco inteiro, e as 18 celulas passavam porque o
    banco so tinha cola. O primeiro rejunte gravado fez as 18 falharem de uma vez, cada
    uma acusando os cinco rejuntes como `eliminados_por_silencio` — frase sem sentido para
    um produto que nunca foi candidato a colar coisa nenhuma. O conserto tentador seria
    colar os cinco ids nas 18 celulas do esquema, e a matriz voltaria ao verde dizendo uma
    besteira. O conserto certo e este: a categoria e parte da pergunta.
    """
    recomendados, ressalva, proibidos, silencio = {}, [], [], []
    for ident, m in materiais.items():
        if m.get("status") != "ativo":
            continue
        if m.get("categoria") != CATEGORIA_DA_MATRIZ_F2:
            continue
        situacao, score = avaliar(m, base, ambiente)
        if situacao == "recomendado":
            recomendados[ident] = score
        elif situacao == "ressalva":
            ressalva.append(ident)
        elif situacao == "proibido":
            proibidos.append(ident)
        else:
            silencio.append(ident)
    topo = []
    abaixo = []
    if recomendados:
        maior = max(recomendados.values())
        topo = sorted(i for i, s in recomendados.items() if s == maior)
        abaixo = sorted(i for i, s in recomendados.items() if s < maior)
    return {
        "recomendados_topo": topo,
        "elegiveis_abaixo_do_topo": abaixo,
        "mencionados_com_ressalva": sorted(ressalva),
        "eliminados_por_proibicao": sorted(proibidos),
        "eliminados_por_silencio": sorted(silencio),
    }


matriz = esquema.get("matriz_esperada_da_F2", {}).get("celulas", [])
celulas_conferidas = 0
if materiais and matriz:
    for celula in matriz:
        base, ambiente = celula["base"], celula["ambiente"]
        if base not in BASES:
            erro("matriz: base '%s' fora do vocabulario" % base)
            continue
        if ambiente not in AMBIENTES:
            erro("matriz: ambiente '%s' fora do vocabulario" % ambiente)
            continue
        computado = computar_celula(base, ambiente)
        celulas_conferidas += 1
        for campo in ("recomendados_topo", "elegiveis_abaixo_do_topo",
                      "mencionados_com_ressalva", "eliminados_por_proibicao",
                      "eliminados_por_silencio"):
            esperado = sorted(celula.get(campo, []))
            obtido = computado[campo]
            if esperado != obtido:
                erro("matriz %s x %s / %s: esperado %s, computado %s"
                     % (base, ambiente, campo, esperado or "[]", obtido or "[]"))
        # coerencia da recomendacao (secao 12 do ARQUIPELAGO.md): nunca recomendar
        # em primeiro lugar produto que a propria pagina diz nao servir
        for ident in computado["recomendados_topo"]:
            if ident in computado["eliminados_por_proibicao"]:
                erro("matriz %s x %s: %s esta recomendado E eliminado" % (base, ambiente, ident))

    # toda celula critica sem recomendado tem que estar escrita como faixa descoberta
    for celula in matriz:
        if not celula.get("recomendados_topo") and not celula.get("observacao"):
            erro("matriz %s x %s: celula sem recomendacao e sem observacao dizendo por que"
                 % (celula["base"], celula["ambiente"]))


# ------------------------------------- REGRA 6: a condicao declarada de superficie
#
# Bloco 3e, 13/09/2026. A primeira regra de cola que olha a TESSELA, e ela nasceu de um
# produto: o Cascola PL500 declara "ao menos uma das superficies deve ser porosa, ja que o
# produto seca por evaporacao da agua". Isso nao e base e nao e ambiente — e o PAR.
#
# A lista de quais superficies sao porosas mora no ESQUEMA, nunca aqui (secao 26.2 do
# ARQUIPELAGO.md): lista digitada dentro da regua envelhece calada no dia em que uma base
# nova entrar no vocabulario. E a outra metade da mesma secao e a que quase ninguem escreve:
# a trava tem de REPROVAR quando a lista some. As tres afirmacoes abaixo sao isso.

POROSAS = esquema.get("superficies_porosas")
if not POROSAS:
    erro("esquema sem `superficies_porosas`: a regra 6 nao tem de onde ler a classificacao, "
         "e sem esta trava ela aprovaria tudo em silencio (secao 26.2)")
    POROSAS = {}

BASES_POROSAS = set(POROSAS.get("bases_porosas") or [])
BASES_NAO_POROSAS = set(POROSAS.get("bases_nao_porosas") or [])
TESSELAS_POROSAS = set(POROSAS.get("tesselas_porosas") or [])
TESSELAS_NAO_POROSAS = set(POROSAS.get("tesselas_nao_porosas") or [])
TESSELAS = VOC["material_tessela"]

if POROSAS:
    # cobertura nas DUAS direcoes: superficie do vocabulario sem classificacao seria
    # decidida por omissao, que e exatamente o que a regra 2 desta ilha proibe.
    if BASES_POROSAS | BASES_NAO_POROSAS != set(BASES):
        erro("superficies_porosas: a classificacao de base nao cobre o vocabulario "
             "(faltam %s; sobram %s)"
             % (sorted(set(BASES) - BASES_POROSAS - BASES_NAO_POROSAS) or "nenhuma",
                sorted((BASES_POROSAS | BASES_NAO_POROSAS) - set(BASES)) or "nenhuma"))
    if BASES_POROSAS & BASES_NAO_POROSAS:
        erro("superficies_porosas: base em duas listas ao mesmo tempo: %s"
             % sorted(BASES_POROSAS & BASES_NAO_POROSAS))
    if TESSELAS_POROSAS | TESSELAS_NAO_POROSAS != set(TESSELAS):
        erro("superficies_porosas: a classificacao de tessela nao cobre o vocabulario "
             "(faltam %s; sobram %s)"
             % (sorted(set(TESSELAS) - TESSELAS_POROSAS - TESSELAS_NAO_POROSAS) or "nenhuma",
                sorted((TESSELAS_POROSAS | TESSELAS_NAO_POROSAS) - set(TESSELAS)) or "nenhuma"))
    if TESSELAS_POROSAS & TESSELAS_NAO_POROSAS:
        erro("superficies_porosas: tessela em duas listas ao mesmo tempo: %s"
             % sorted(TESSELAS_POROSAS & TESSELAS_NAO_POROSAS))
    # e a lista tem de ter alguem dos dois lados, senao "cobre o vocabulario" passa a ser
    # verdade de graca com uma das listas vazia
    for nome_lista, conjunto in (("bases_porosas", BASES_POROSAS),
                                 ("bases_nao_porosas", BASES_NAO_POROSAS),
                                 ("tesselas_porosas", TESSELAS_POROSAS),
                                 ("tesselas_nao_porosas", TESSELAS_NAO_POROSAS)):
        if not conjunto:
            erro("superficies_porosas: `%s` vazia — classificacao de um lado so nao e "
                 "classificacao" % nome_lista)


def exige_porosa(m):
    """True quando o fabricante declarou a condicao para este produto."""
    c = ((m.get("condicoes") or {}).get("exige_superficie_porosa") or {})
    return bool(c.get("valor"))


def condicao_cumprida(base, tessela):
    """A condicao do fabricante, medida sobre o PAR. Regua propria: le as listas do
    esquema e nao chama nada de quem produziu o dado."""
    return base in BASES_POROSAS or tessela in TESSELAS_POROSAS


def computar_celula_com_condicao(base, ambiente, tessela):
    """A celula que a PAGINA serve: a de declaracao, filtrada pela regra 6.

    A ordem importa e esta escrita: a condicao roda DEPOIS das cinco e ANTES da
    ordenacao por score. Rodar depois da ordenacao deixaria celula sem topo com
    elegiveis na mao — e a ancora vidro x caco_espelho existe para medir isso.
    """
    recomendados, ressalva, proibidos, silencio, condicao = {}, [], [], [], []
    for ident, m in materiais.items():
        if m.get("status") != "ativo":
            continue
        if m.get("categoria") != CATEGORIA_DA_MATRIZ_F2:
            continue
        situacao, score = avaliar(m, base, ambiente)
        if situacao in ("recomendado", "ressalva") and exige_porosa(m) \
                and not condicao_cumprida(base, tessela):
            condicao.append(ident)
            continue
        if situacao == "recomendado":
            recomendados[ident] = score
        elif situacao == "ressalva":
            ressalva.append(ident)
        elif situacao == "proibido":
            proibidos.append(ident)
        else:
            silencio.append(ident)
    topo, abaixo = [], []
    if recomendados:
        maior = max(recomendados.values())
        topo = sorted(i for i, s in recomendados.items() if s == maior)
        abaixo = sorted(i for i, s in recomendados.items() if s < maior)
    return {
        "recomendados_topo": topo,
        "elegiveis_abaixo_do_topo": abaixo,
        "mencionados_com_ressalva": sorted(ressalva),
        "eliminados_por_proibicao": sorted(proibidos),
        "eliminados_por_silencio": sorted(silencio),
        "eliminados_por_condicao": sorted(condicao),
    }


mc = esquema.get("matriz_esperada_da_condicao_de_superficie")
pares_conferidos = 0
ancoras_conferidas = 0
if mc is None:
    erro("esquema sem `matriz_esperada_da_condicao_de_superficie`: a regra 6 ficaria sem "
         "regua escrita a mao, e duas metades que erram juntas ficam verdes")
elif materiais:
    # 1) os pares em que a condicao falha, contados e comparados um a um
    falha_computada = sorted([b, t] for b in BASES for t in TESSELAS
                             if not condicao_cumprida(b, t))
    falha_escrita = sorted([list(p) for p in mc.get("pares_em_que_a_condicao_FALHA", [])])
    pares_conferidos = len(BASES) * len(TESSELAS)
    if pares_conferidos != mc.get("total_de_pares"):
        erro("matriz da condicao: total_de_pares diz %r e o vocabulario da %d"
             % (mc.get("total_de_pares"), pares_conferidos))
    if falha_computada != falha_escrita:
        erro("matriz da condicao: os pares em que ela falha nao batem.\n      escrito:  %s"
             "\n      computado: %s" % (falha_escrita, falha_computada))

    # 2) quem carrega a condicao hoje — para produto novo com condicao nao entrar mudo
    carregam = sorted(i for i, m in materiais.items()
                      if m.get("categoria") == CATEGORIA_DA_MATRIZ_F2
                      and m.get("status") == "ativo" and exige_porosa(m))
    if carregam != sorted(mc.get("produtos_que_carregam_a_condicao_hoje", [])):
        erro("matriz da condicao: `produtos_que_carregam_a_condicao_hoje` diz %s e o banco "
             "tem %s" % (sorted(mc.get("produtos_que_carregam_a_condicao_hoje", [])), carregam))
    for ident in carregam:
        c = materiais[ident]["condicoes"]["exige_superficie_porosa"]
        if not c.get("literal"):
            erro("%s: condicao sem o texto LITERAL do fabricante" % ident)
        if c.get("fonte_id") not in (materiais[ident].get("fontes") or {}):
            erro("%s: condicao aponta fonte_id inexistente" % ident)
        if not c.get("quem_classifica_a_porosidade"):
            erro("%s: condicao sem dizer QUEM classifica a porosidade — secao 26.3, a tela "
                 "nao pode atribuir ao fabricante uma classificacao que e nossa" % ident)

    # 3) as ancoras ponta a ponta
    for a in mc.get("ancoras_ponta_a_ponta", []):
        if a["tessela"] not in TESSELAS:
            erro("ancora da condicao: tessela '%s' fora do vocabulario" % a["tessela"])
            continue
        c = computar_celula_com_condicao(a["base"], a["ambiente"], a["tessela"])
        ancoras_conferidas += 1
        for campo in ("recomendados_topo", "eliminados_por_condicao"):
            if sorted(a.get(campo, [])) != c[campo]:
                erro("ancora %s x %s x %s / %s: esperado %s, computado %s"
                     % (a["base"], a["ambiente"], a["tessela"], campo,
                        sorted(a.get(campo, [])) or "[]", c[campo] or "[]"))
        if not a.get("por_que"):
            erro("ancora %s x %s x %s: sem `por_que` escrito"
                 % (a["base"], a["ambiente"], a["tessela"]))

    # 4) a condicao NUNCA manda ninguem para o silencio nem ressuscita proibido
    for b in BASES:
        for t in TESSELAS:
            for amb in AMBIENTES:
                sem = computar_celula(b, amb)
                com = computar_celula_com_condicao(b, amb, t)
                if com["eliminados_por_silencio"] != sem["eliminados_por_silencio"]:
                    erro("condicao %s x %s x %s: ela mexeu na lista do silencio, e silencio "
                         "e outra causa" % (b, amb, t))
                if com["eliminados_por_proibicao"] != sem["eliminados_por_proibicao"]:
                    erro("condicao %s x %s x %s: ela mexeu na lista da proibicao" % (b, amb, t))
                movidos = set(com["eliminados_por_condicao"])
                antes = set(sem["recomendados_topo"] + sem["elegiveis_abaixo_do_topo"]
                            + sem["mencionados_com_ressalva"])
                if movidos - antes:
                    erro("condicao %s x %s x %s: moveu %s, que nao estava elegivel antes"
                         % (b, amb, t, sorted(movidos - antes)))


# ------------------------------------------------------- REJUNTE: regua propria
#
# Bloco 3c. Isto NAO reaproveita `perfil()` nem `avaliar()` de proposito, e a razao e a
# trava da secao 8 do ARQUIPELAGO.md: quem confere escreve a propria regua. Mas aqui ha
# um motivo a mais, e ele e de conteudo, nao de metodo — as duas categorias nao respondem
# a mesma pergunta. Na cola, a lista do fabricante nomeia a BASE sobre a qual se cola; no
# rejunte, a mesma lista nomeia a TESSELA que sera rejuntada e o AMBIENTE. Rejunte nao
# toca a base. A variavel que decide um rejunte e a LARGURA DA JUNTA, que nao existe no
# vocabulario da cola.

REJ = esquema.get("regras_de_elegibilidade_do_rejunte")
MAPA_REJ, MAPA_REJ_TESSELA, NAO_TRADUZ_REJ = {}, {}, set()
CRITICOS_REJ = set()
TESSELAS = set(VOC["material_tessela"])

if REJ:
    CRITICOS_REJ = set(REJ["2_ambiente_critico_exige_declaracao_EXPLICITA"]["ambientes"])
    for a in CRITICOS_REJ:
        if a not in AMBIENTES:
            erro("regras do rejunte: ambiente critico '%s' fora do vocabulario" % a)

mapa_rej = esquema.get("mapa_de_termos_do_rejunte")
if mapa_rej:
    for termo in mapa_rej["termos"]:
        MAPA_REJ[normalizar(termo["literal"])] = termo.get("ambiente", [])
    for termo in mapa_rej["termos_tessela"]:
        MAPA_REJ_TESSELA[normalizar(termo["literal"])] = termo.get("tessela", [])
    NAO_TRADUZ_REJ = {normalizar(t["literal"]) for t in mapa_rej["termos_que_nao_traduzem"]}
    for chave, ambs in MAPA_REJ.items():
        for a in ambs:
            if a not in AMBIENTES:
                erro("mapa do rejunte: '%s' aponta para ambiente inexistente '%s'" % (chave, a))
    for chave, tess in MAPA_REJ_TESSELA.items():
        for t in tess:
            if t not in TESSELAS:
                erro("mapa do rejunte: '%s' aponta para tessela inexistente '%s'" % (chave, t))
    for chave in NAO_TRADUZ_REJ:
        if chave in MAPA_REJ or chave in MAPA_REJ_TESSELA:
            erro("mapa do rejunte: '%s' esta ao mesmo tempo no mapa e nos que nao traduzem" % chave)


def _num(m, campo):
    """Le propriedades[campo].valor, aceitando ausencia como null."""
    prop = (m.get("propriedades") or {}).get(campo) or {}
    return prop.get("valor")


def traduzir_rejunte(lista, onde):
    """Devolve (ambientes, tesselas). Termo desconhecido vira aviso e fica na citacao."""
    ambientes, tesselas = set(), set()
    for literal in lista or []:
        chave = normalizar(literal)
        if chave in MAPA_REJ:
            ambientes.update(MAPA_REJ[chave])
        elif chave in MAPA_REJ_TESSELA:
            tesselas.update(MAPA_REJ_TESSELA[chave])
        elif chave in NAO_TRADUZ_REJ:
            continue
        else:
            aviso("%s: termo de rejunte sem traducao no mapa, ficou so na citacao literal: '%s'"
                  % (onde, literal))
    return ambientes, tesselas


def perfil_rejunte(m):
    d = m.get("declaracoes") or {}
    onde = m.get("id")
    amb_ind, tess_ind = traduzir_rejunte(d.get("indicado_para"), onde)
    amb_delim, _ = traduzir_rejunte(d.get("ambientes_declarados"), onde)
    amb_resist, tess_resist = traduzir_rejunte(d.get("resistencias_declaradas"), onde)
    return {
        "junta_min": _num(m, "junta_min_mm"),
        "junta_max": _num(m, "junta_max_mm"),
        "ambientes_cobertos": amb_ind | amb_delim | amb_resist,
        "ambientes_delimitados": amb_delim,
        "tesselas_declaradas": tess_ind | tess_resist,
        "nivel": min((f["nivel"] for f in (m.get("fontes") or {}).values()), default=9),
    }


def avaliar_rejunte(m, junta_mm, ambiente):
    """Devolve (situacao, score).

    situacao: recomendado | ressalva | fora_da_junta | fora_do_ambiente
    """
    p = perfil_rejunte(m)
    # regra 1: as DUAS pontas da faixa precisam existir, e a junta tem que caber nelas.
    # Faixa com ponta null nao e faixa aberta — e faixa desconhecida, e nao passa.
    if p["junta_min"] is None or p["junta_max"] is None:
        return "fora_da_junta", 0
    if not (p["junta_min"] <= junta_mm <= p["junta_max"]):
        return "fora_da_junta", 0
    # regra 3: quem delimita ambiente fica fechado nele
    if p["ambientes_delimitados"] and ambiente not in p["ambientes_delimitados"]:
        return "fora_do_ambiente", 0
    # regra 2: ambiente critico exige declaracao explicita
    if ambiente in CRITICOS_REJ and ambiente not in p["ambientes_cobertos"]:
        return "fora_do_ambiente", 0
    score = 2 + (2 if ambiente in p["ambientes_cobertos"] else 0)
    # regra 4: nivel de fonte limita a recomendacao primaria
    if p["nivel"] > NIVEL_MAX:
        return "ressalva", score
    return "recomendado", score


def computar_celula_rejunte(junta_mm, ambiente):
    recomendados, ressalva, fora_junta, fora_ambiente = {}, [], [], []
    for ident, m in materiais.items():
        if m.get("status") != "ativo" or m.get("categoria") != "rejunte":
            continue
        situacao, score = avaliar_rejunte(m, junta_mm, ambiente)
        if situacao == "recomendado":
            recomendados[ident] = score
        elif situacao == "ressalva":
            ressalva.append(ident)
        elif situacao == "fora_da_junta":
            fora_junta.append(ident)
        else:
            fora_ambiente.append(ident)
    topo, abaixo = [], []
    if recomendados:
        maior = max(recomendados.values())
        topo = sorted(i for i, s in recomendados.items() if s == maior)
        abaixo = sorted(i for i, s in recomendados.items() if s < maior)
    return {
        "recomendados_topo": topo,
        "elegiveis_abaixo_do_topo": abaixo,
        "mencionados_com_ressalva": sorted(ressalva),
        "eliminados_por_faixa_de_junta": sorted(fora_junta),
        "eliminados_por_ambiente": sorted(fora_ambiente),
    }


rejuntes = {i: m for i, m in materiais.items() if m.get("categoria") == "rejunte"}
celulas_rejunte_conferidas = 0

if rejuntes:
    if not REJ or not mapa_rej:
        erro("ha rejunte no banco e o esquema nao tem regras_de_elegibilidade_do_rejunte "
             "ou mapa_de_termos_do_rejunte: categoria sem regua nenhuma")

    # coerencia interna de cada rejunte
    for ident, m in rejuntes.items():
        p = perfil_rejunte(m)
        if p["junta_min"] is not None and p["junta_max"] is not None:
            if p["junta_min"] > p["junta_max"]:
                erro("%s: junta_min (%s) maior que junta_max (%s)"
                     % (ident, p["junta_min"], p["junta_max"]))
        elif (p["junta_min"] is None) != (p["junta_max"] is None):
            erro("%s: faixa de junta pela metade. Uma ponta so nao e faixa — ou as duas "
                 "sao obtidas, ou as duas ficam null com motivo" % ident)

    # os perfis escritos a mao no esquema tem que bater com os recomputados
    for esperado in esquema.get("perfis_esperados_do_rejunte", {}).get("perfis", []):
        ident = esperado["id"]
        if ident not in rejuntes:
            erro("perfis do rejunte: '%s' nao existe no banco" % ident)
            continue
        p = perfil_rejunte(rejuntes[ident])
        obtido_junta = [p["junta_min"], p["junta_max"]]
        if esperado["junta_mm"] != obtido_junta:
            erro("perfil %s / junta: esperado %s, computado %s"
                 % (ident, esperado["junta_mm"], obtido_junta))
        for campo, chave in (("ambientes_cobertos", "ambientes_cobertos"),
                             ("ambientes_delimitados", "ambientes_delimitados")):
            if sorted(esperado[campo]) != sorted(p[chave]):
                erro("perfil %s / %s: esperado %s, computado %s"
                     % (ident, campo, sorted(esperado[campo]), sorted(p[chave])))
        if esperado["nivel"] != p["nivel"]:
            erro("perfil %s / nivel: esperado %s, computado %s"
                 % (ident, esperado["nivel"], p["nivel"]))
    ids_com_perfil = {e["id"] for e in esquema.get("perfis_esperados_do_rejunte", {}).get("perfis", [])}
    for ident in rejuntes:
        if ident not in ids_com_perfil:
            erro("%s: rejunte no banco sem perfil esperado escrito no esquema" % ident)

    # a matriz junta x ambiente
    for celula in esquema.get("matriz_esperada_do_rejunte", {}).get("celulas", []):
        junta, ambiente = celula["junta_mm"], celula["ambiente"]
        if ambiente not in AMBIENTES:
            erro("matriz do rejunte: ambiente '%s' fora do vocabulario" % ambiente)
            continue
        computado = computar_celula_rejunte(junta, ambiente)
        celulas_rejunte_conferidas += 1
        for campo in ("recomendados_topo", "elegiveis_abaixo_do_topo",
                      "mencionados_com_ressalva", "eliminados_por_faixa_de_junta",
                      "eliminados_por_ambiente"):
            if sorted(celula.get(campo, [])) != computado[campo]:
                erro("matriz do rejunte %s mm x %s / %s: esperado %s, computado %s"
                     % (junta, ambiente, campo,
                        sorted(celula.get(campo, [])) or "[]", computado[campo] or "[]"))
        # todo produto do banco aparece em exatamente uma lista da celula
        vistos = (computado["recomendados_topo"] + computado["elegiveis_abaixo_do_topo"]
                  + computado["mencionados_com_ressalva"]
                  + computado["eliminados_por_faixa_de_junta"]
                  + computado["eliminados_por_ambiente"])
        if sorted(vistos) != sorted(rejuntes):
            erro("matriz do rejunte %s mm x %s: a celula nao classifica todos os rejuntes "
                 "exatamente uma vez (%s)" % (junta, ambiente, vistos))
        if not celula.get("recomendados_topo") and not celula.get("observacao"):
            erro("matriz do rejunte %s mm x %s: celula sem recomendacao e sem observacao "
                 "dizendo por que" % (junta, ambiente))

    # a grade tem que pisar nas BORDAS declaradas, senao e amostra com nome de grade
    juntas_na_grade = {c["junta_mm"] for c in esquema.get("matriz_esperada_do_rejunte", {}).get("celulas", [])}
    bordas = set()
    for m in rejuntes.values():
        for campo in ("junta_min_mm", "junta_max_mm"):
            v = _num(m, campo)
            if v is not None:
                bordas.add(v)
    faltando = sorted(b for b in bordas if b not in juntas_na_grade)
    if faltando:
        erro("matriz do rejunte: a grade nao pisa nas bordas declaradas %s. Grade que nao "
             "inclui a borda nao consegue separar 'ate 4' de 'ate 5'" % faltando)
    if bordas and not any(j > max(bordas) for j in juntas_na_grade):
        erro("matriz do rejunte: a grade nao tem nenhum valor ACIMA da maior borda "
             "declarada (%s). Sem isso ninguem prova que a faixa fecha" % max(bordas))

    # regressao do defeito que este bloco corrigiu: rejunte nunca entra na matriz da F2
    for celula in matriz:
        computado = computar_celula(celula["base"], celula["ambiente"])
        for campo in ("recomendados_topo", "elegiveis_abaixo_do_topo",
                      "mencionados_com_ressalva", "eliminados_por_proibicao",
                      "eliminados_por_silencio"):
            invasores = [i for i in computado[campo] if i in rejuntes]
            if invasores:
                erro("matriz da F2 %s x %s / %s: rejunte na matriz de cola (%s). A matriz "
                     "da F2 e de cola: rejunte nao toca a base"
                     % (celula["base"], celula["ambiente"], campo, invasores))


# ---------------------------------------------------------------- TECNICA

# ESTA REGUA FOI ESCRITA EM 12/09 E NUNCA RODOU ATE 14/09/2026, porque o arquivo
# que ela mede nao existia — ela vivia imprimindo a `nota` de baixo. Portao que
# nunca rodou e funcao morta, e este passou tres dias assim. No dia em que o
# arquivo nasceu, o que ela cobrava (id no vocabulario, campo obrigatorio
# presente, enum do estado da revisao) passou de primeira, e passar de primeira
# nao e elogio: e o sinal de que ela cobrava o que qualquer arquivo bem digitado
# teria. O que ela NAO cobrava era tudo o que o esquema diz que esta entidade
# tem de especial, e e isso que entrou agora:
#
#   1. FONTE OBRIGATORIA TEM DE APONTAR PARA UMA FONTE QUE EXISTE. O esquema
#      marca `definicao` com fonte_obrigatoria; sem esta afirmacao, "tem o campo
#      definicao" e "a definicao tem de onde vir" eram a mesma linha, e nao sao.
#   2. O NIVEL DA FONTE E O DO ELO MAIS FRACO (secao 10 do contrato). TECNICA e a
#      unica entidade da ilha sem fabricante, e o esquema lista as origens que
#      ela aceita. A regua le a lista DO ESQUEMA — escrever os tres nomes aqui
#      seria a segunda copia da mesma decisao.
#   3. SILENCIO NUNCA PROMOVE: campo opcional vazio exige o `motivo_sem_<campo>`
#      ao lado. E a mesma regra do `motivo_declaracoes_vazias` do banco de
#      material, e ela existe porque campo vazio sem motivo e indistinguivel de
#      campo esquecido.
#   4. NUMERO SO EXISTE COM FONTE. `junta_tipica_mm` e o unico numero desta
#      entidade e o esquema diz que ele alimenta o valor sugerido da F1. Numero
#      que chega a um campo de entrada de ferramenta sem fonte e o defeito que a
#      secao 13 chama de pior que nao ter o campo.
#   5. O PORTAO DA FAMILIA, e ele e o que decide pagina: uma tecnica so pode
#      declarar pagina depois de reunir 3 itens de banco reais (secao 9). A
#      contagem e feita aqui, item a item, traduzindo categoria+tipo do banco de
#      material para o vocabulario `material_tessela` — nunca comparando texto.
#
# 14/09/2026, 21h17Z — O PORTAO CONTAVA UMA CATEGORIA QUE A PAGINA NAO
# RECOMENDA, E POR ISSO DAVA ZERO COM CINCO ITENS ATRAS DELE. Como estava
# escrito, o item 5 contava SO tessela: quantos produtos da categoria `pastilha`
# o banco tem com o tipo que a tecnica cita. As duas unicas tecnicas com material
# declarado por fonte citam `caco_azulejo` e `caco_louca` — caco de prato e de
# azulejo NAO tem fabricante e nunca terao ficha de produto nesta ilha. O portao
# lia zero, e lia zero para sempre, por mais coleta que acontecesse.
#
# So que a pagina de uma tecnica nao recomenda caquinho: ela responde O QUE
# COMPRAR PARA COLAR AQUELE CAQUINHO, que e o eixo desta ilha escrito no
# PROMPT.md ("o que comprar para fazer a peca X"), e e produto que o banco tem,
# com fabricante, declaracao e link de afiliado. A propria `ARVORE.md` ja dizia
# isso na secao 4b, item 6 — "o caminho mais curto nao e catalogar caco: e ligar
# a tecnica a COLA e ao REJUNTE" —, e o item 3 da mesma secao contava caco assim
# mesmo. As duas metades da mesma secao discordavam, e quem decidia era a que
# tinha numero.
#
# E a mesma familia da V24 da Aquametria, consertada em 14/09 poucas horas antes:
# uma regua que amarra o portao a um campo que o caso certo nunca preenche
# reprova o mundo inteiro e parece rigor. Entao o que a regua conta passa a ser
# O QUE A PAGINA PODE RECOMENDAR, medido pela regua da F2 que ja existe neste
# arquivo, e nunca uma segunda copia dela:
#
#     itens de banco de uma tecnica = as pastilhas do banco cujo tipo e a tessela
#     que a tecnica declara  +  as colas que o fabricante declara elegiveis para
#     aquela tessela, em qualquer par base x ambiente do vocabulario.
#
# TRES COISAS QUE ISSO NAO AFROUXA, e elas sao o que separa conserto de porta dos
# fundos: (a) tecnica que nao declara material continua em ZERO — direto,
# indireto e bizantino seguem sem passar, e cada um tem o `motivo_sem_materiais`
# escrito dizendo por que nao declara; (b) `mencionados_com_ressalva` continua
# fora da conta, pela mesma razao do `cobertura.py`; (c) o rejunte NAO entra:
# a regua dele decide por junta em milimetro e ambiente, nao olha a tessela, e as
# cinco tecnicas tem `junta_tipica_mm` null com motivo. Somar rejunte aqui seria
# contar item que a tecnica nao seleciona.
#
# A VARREDURA E SOBRE O VOCABULARIO, NAO SOBRE A FAIXA DO SNIPPET, e a diferenca
# importa: o `cobertura.py` pergunta "quantos estados da F2 saem descobertos" e
# por isso mede a faixa provocando o PHP. Aqui a pergunta e outra — "quantos
# itens do banco esta tecnica pode recomendar" —, e ela e sobre o banco e o
# vocabulario, nao sobre o formulario de uma ferramenta que nem e a desta pagina.


def itens_de_banco_da_tecnica(tecnica, tesselas_do_banco, tessela_por_tipo=None):
    """O portao de 3 da secao 9 para uma TECNICA, com a conta aberta.

    Devolve o detalhe inteiro — nao so o total — porque e dele que
    `ferramentas/tecnica-x-material.py` monta o arquivo derivado. Uma conta, dois
    leitores: o portao daqui le `total`, o derivado le o resto.
    """
    tesselas = list(tecnica.get("materiais_tipicos") or [])

    pastilhas = []
    for valor in tesselas:
        pastilhas.extend(tesselas_do_banco.get(valor, []))
    pastilhas = sorted(set(pastilhas))

    colas = set()
    estados = []
    for tessela in tesselas:
        for base in VOC["base"]:
            for ambiente in VOC["ambiente"]:
                c = computar_celula_com_condicao(base, ambiente, tessela)
                eleg = sorted(c["recomendados_topo"] + c["elegiveis_abaixo_do_topo"])
                colas.update(eleg)
                estados.append({
                    "tessela": tessela,
                    "base": base,
                    "ambiente": ambiente,
                    "elegiveis": eleg,
                    "quantos_elegiveis": len(eleg),
                    "com_ressalva": c["mencionados_com_ressalva"],
                })

    colas = sorted(colas)
    contagens = [e["quantos_elegiveis"] for e in estados]
    return {
        "tesselas_declaradas": tesselas,
        "pastilhas_do_banco": pastilhas,
        "colas_elegiveis": colas,
        "total": len(pastilhas) + len(colas),
        "estados": estados,
        "estados_varridos": len(estados),
        "estados_com_o_minimo": sum(1 for n in contagens if n >= 3),
        "estados_sem_nenhum_elegivel": sum(1 for n in contagens if n == 0),
        "maior_numero_de_elegiveis_em_um_estado": max(contagens) if contagens else 0,
    }


tecnicas = carregar("tecnicas.json")
if tecnicas is None:
    nota("dados/tecnicas.json ainda nao existe: entidade TECNICA vazia.")
else:
    ESQ_TECNICA = esquema.get("entidades", {}).get("TECNICA", {})
    ORIGENS_ACEITAS = ESQ_TECNICA.get("natureza_da_fonte", {}).get("niveis_aceitos", [])
    if not ORIGENS_ACEITAS:
        erro("esquema-banco.json: a entidade TECNICA nao lista niveis_aceitos de fonte, "
             "e sem essa lista a regua de fonte desta entidade nao tem contra o que medir")

    # Traducao categoria+tipo do banco de MATERIAL -> vocabulario material_tessela.
    # So a categoria `pastilha` produz tessela; cola, rejunte e alicate nao sao
    # material de superficie e por isso nao contam para o portao de 3.
    TESSELA_POR_TIPO = {
        "vidro": "pastilha_vidro",
        "ceramica": "pastilha_ceramica",
        "pedra": "pedra",
        "caco_azulejo": "caco_azulejo",
        "caco_espelho": "caco_espelho",
    }
    tesselas_do_banco = {}
    for mid, m in materiais.items():
        if m.get("categoria") != "pastilha":
            continue
        alvo = TESSELA_POR_TIPO.get(m.get("tipo"))
        if alvo:
            tesselas_do_banco.setdefault(alvo, []).append(mid)

    vistos = set()
    for t in tecnicas.get("tecnicas", []):
        tid = t.get("id")
        onde = "tecnicas.json / %s" % tid
        if tid not in VOC["tecnica"]:
            erro("%s: id fora do vocabulario de tecnica" % onde)
        if tid in vistos:
            erro("%s: id repetido — duas tecnicas com o mesmo id publicam a mesma pagina duas vezes" % onde)
        vistos.add(tid)

        for campo in ("nome", "definicao", "consulta_alvo", "por_que_chega_ao_top_10", "fontes", "revisao_tecnica"):
            if not t.get(campo):
                erro("%s: falta %s" % (onde, campo))
        if t.get("revisao_tecnica") not in ("pendente", "revisada"):
            erro("%s: revisao_tecnica invalida" % onde)
        if "imagem" not in t:
            erro("%s: falta o campo imagem (o esquema o marca obrigatorio, e `null` e resposta)" % onde)

        fontes = t.get("fontes") or {}
        if not isinstance(fontes, dict):
            erro("%s: fontes tem de ser objeto id -> fonte" % onde)
            fontes = {}
        for fid, f in fontes.items():
            for campo in ("url", "origem", "o_que_e", "leitura", "data_leitura"):
                if not (isinstance(f, dict) and f.get(campo)):
                    erro("%s / fonte %s: falta %s" % (onde, fid, campo))
            if isinstance(f, dict) and ORIGENS_ACEITAS and f.get("origem") not in ORIGENS_ACEITAS:
                erro("%s / fonte %s: origem %r fora das aceitas pelo esquema para TECNICA (%s)"
                     % (onde, fid, f.get("origem"), ", ".join(ORIGENS_ACEITAS)))

        # (1) e (4): todo campo com fonte obrigatoria aponta para uma fonte que existe.
        for campo, chave in (("definicao", "definicao_fonte_id"),
                             ("materiais_tipicos", "materiais_tipicos_fonte_id"),
                             ("junta_tipica_mm", "junta_tipica_mm_fonte_id")):
            valor = t.get(campo)
            if valor in (None, [], ""):
                continue
            fid = t.get(chave)
            if not fid:
                erro("%s: %s esta preenchido e nao diz de qual fonte veio (falta %s)" % (onde, campo, chave))
            elif fid not in fontes:
                erro("%s: %s aponta para a fonte %r, que nao existe em fontes" % (onde, chave, fid))

        # (3) silencio nunca promove.
        for campo, motivo in (("como_se_executa", "motivo_sem_como_se_executa"),
                              ("bases_compativeis", "motivo_sem_bases"),
                              ("materiais_tipicos", "motivo_sem_materiais"),
                              ("junta_tipica_mm", "motivo_sem_junta")):
            if t.get(campo) in (None, [], "") and not t.get(motivo):
                erro("%s: %s esta vazio e nao ha %s — campo vazio sem motivo e "
                     "indistinguivel de campo esquecido" % (onde, campo, motivo))

        for campo, voc in (("bases_compativeis", "base"), ("materiais_tipicos", "material_tessela")):
            for valor in (t.get(campo) or []):
                if valor not in VOC.get(voc, []):
                    erro("%s: %s tem %r, fora do vocabulario %s" % (onde, campo, valor, voc))

        junta = t.get("junta_tipica_mm")
        if junta is not None and not isinstance(junta, (int, float)):
            erro("%s: junta_tipica_mm tem de ser numero ou null" % onde)

        # (5) O PORTAO DA FAMILIA.
        conta = itens_de_banco_da_tecnica(t, tesselas_do_banco, TESSELA_POR_TIPO)
        t["__conta_de_banco"] = conta
        t["__itens_de_banco"] = conta["total"]
        if t.get("pagina_publicada") and conta["total"] < 3:
            erro("%s: declara pagina publicada com %d itens de banco. O portao da secao 9 "
                 "pede 3 itens reais e um numero calculado proprio — pagina de tecnica sem "
                 "material que a sustente e pagina fina em dominio que ainda nao indexou "
                 "nada (14.1)" % (onde, conta["total"]))

        # O OUTRO SENTIDO DO MESMO PORTAO, e sem ele a bandeira nunca reprovaria
        # nada: tecnica que REUNE os 3 itens e nao declara pagina e trabalho
        # parado, nao defeito — entao isso e `aviso`, nao `erro`. O que seria
        # defeito e a bandeira dizer o contrario do que a conta diz, e e por isso
        # que os dois lados sao medidos.
        if not t.get("pagina_publicada") and conta["total"] >= 3:
            aviso("%s: reune %d itens de banco e ainda nao declara pagina. O portao da "
                  "secao 9 esta ABERTO para esta tecnica" % (onde, conta["total"]))

    if tecnicas.get("tecnicas"):
        resumo = ", ".join("%s %d" % (t.get("id"), t.get("__itens_de_banco", 0))
                           for t in tecnicas["tecnicas"])
        nota("tecnicas: itens de banco por tecnica (portao de 3 da secao 9; pastilha do "
             "banco + cola que o fabricante declara para a tessela) — %s" % resumo)


# ---------------------------------------------------------------- COTACAO

cotacoes = carregar("cotacoes.json")
if cotacoes is None:
    nota("dados/cotacoes.json ainda nao existe: nenhum preco coletado.")
else:
    for c in cotacoes.get("cotacoes", []):
        onde = "cotacoes.json / %s" % c.get("material_id")
        if c.get("material_id") not in materiais:
            erro("%s: cotacao de material que nao existe no banco" % onde)
        for campo in ("loja", "preco_brl", "unidade", "url", "coletado_em"):
            if not c.get(campo):
                erro("%s: falta %s" % (onde, campo))


# ---------------------------------------------------------------- PECA

# A REGUA MUDOU EM 14/09/2026, E O MOTIVO E A SECAO 24 DO CONTRATO.
#
# Ate aqui esta regua dizia uma frase so: `dados/pecas.json` NAO PODE EXISTIR.
# Ela nasceu certa em 12/09, quando o unico jeito de aquele arquivo aparecer era
# alguem inventar o catalogo da artesa dentro do repositorio — que e a unica
# mentira que esta ilha pode contar sobre uma pessoa de verdade. Depois disso a
# secao 24 entrou no contrato e virou a mesa: dado que uma PESSOA digita dentro
# do WordPress nasce com COPIA no repositorio, e o bloco nao fecha sem ela. Em
# 14/09/2026 a artesa publicou a primeira peca, a execucao daquele dia tirou a
# copia pelo endpoint como a 24.2 manda — e este portao passou a reprovar o
# repositorio por cumprir o contrato. Proibicao que envelheceu vira reprovacao
# de quem acertou.
#
# O QUE A REGUA PROTEGE NAO E A AUSENCIA DO ARQUIVO, e sim que ele seja COPIA e
# nunca FONTE. Peca inventada so chega ao site se alguem SERVIR este arquivo; um
# espelho que ninguem le nao pode mentir na tela. Sao tres afirmacoes, e a do
# meio e a que carrega o sentido:
#
#   1. O manifest o declara com `publicar: false`. Com `true`, o Sync gravaria a
#      copia numa option do site — o site lendo de volta o proprio espelho, que
#      e como uma copia se promove a fonte sem ninguem decidir.
#   2. NENHUM SNIPPET O LE. Este e o portao de verdade, e ele e medido no codigo
#      que vai ao ar, nao na intencao: se um dia uma pagina passar a montar peca
#      a partir deste arquivo, a peca da tela deixa de ser a que a artesa
#      cadastrou, e e exatamente isso que a frase antiga queria impedir.
#   3. O arquivo tem a FORMA da resposta do endpoint, com o `id` de post de cada
#      peca e a `url` no dominio da ilha. Catalogo escrito a mao nao tem id de
#      post nem URL que responde; e `total` tem de bater com o tamanho da lista,
#      porque numero de copia tambem se conta e nunca se digita (secao 8).
CAMINHO_PECAS = os.path.join(DADOS, "pecas.json")
if os.path.exists(CAMINHO_PECAS):
    try:
        copia_pecas = json.load(open(CAMINHO_PECAS, encoding="utf-8"))
    except ValueError as falha:
        copia_pecas = None
        erro("dados/pecas.json nao e JSON valido: %s" % falha)

    manifest_pecas = None
    try:
        manifest_bruto = json.load(open(os.path.join(BASE, "manifest.json"), encoding="utf-8"))
        for item in manifest_bruto.get("dados", []):
            if item.get("arquivo") == "dados/pecas.json":
                manifest_pecas = item
    except (IOError, ValueError):
        pass

    if manifest_pecas is None:
        erro("dados/pecas.json existe e o manifest nao o conhece: arquivo fora do manifest "
             "nunca chega ao site, mas tambem nunca tem sha conferido (secao 3 do contrato).")
    elif manifest_pecas.get("publicar") is not False:
        erro("dados/pecas.json esta no manifest com publicar=%r. A copia da secao 24 e "
             "COPIA DO SITE e nunca fonte dele: publicada, ela viraria option que o site "
             "le de volta." % manifest_pecas.get("publicar"))

    # (2) O PORTAO DE VERDADE: nenhum snippet le este arquivo, e nenhum le a
    # option que ele teria se fosse publicado. Medido no codigo que vai ao ar.
    leitores = []
    pasta_snippets = os.path.join(BASE, "snippets")
    if os.path.isdir(pasta_snippets):
        for nome in sorted(os.listdir(pasta_snippets)):
            if not nome.endswith(".php"):
                continue
            fonte_php = open(os.path.join(pasta_snippets, nome), encoding="utf-8").read()
            # O comentario nao vai ao ar; quem decide e o codigo (a mesma regra do
            # teste-f1, que descarta comentario antes de afirmar sobre o snippet).
            sem_comentario = re.sub(r"/\*.*?\*/", " ", fonte_php, flags=re.S)
            sem_comentario = re.sub(r"(?m)//.*$", " ", sem_comentario)
            for alvo in ("pecas.json", "clubedomosaico_dados_pecas"):
                if alvo in sem_comentario:
                    leitores.append("%s cita %s" % (nome, alvo))
    if leitores:
        erro("A COPIA DA SECAO 24 VIROU FONTE: " + "; ".join(leitores) + ". A peca da tela "
             "tem de ser a que a artesa cadastrou no painel, lida do CPT `peca` — nunca a "
             "do espelho commitado. Peca servida do repositorio e peca que ninguem cadastrou.")

    if isinstance(copia_pecas, dict):
        for campo in ("ilha", "versao_loja", "total", "pecas"):
            if campo not in copia_pecas:
                erro("dados/pecas.json: falta o campo %s da resposta do endpoint — o arquivo "
                     "nao tem a forma de uma copia" % campo)
        lista_pecas = copia_pecas.get("pecas")
        if not isinstance(lista_pecas, list):
            erro("dados/pecas.json: `pecas` nao e lista")
        else:
            if copia_pecas.get("total") != len(lista_pecas):
                erro("dados/pecas.json: total diz %r e a lista tem %d — numero de copia se "
                     "conta, nunca se digita" % (copia_pecas.get("total"), len(lista_pecas)))
            for peca in lista_pecas:
                onde = "pecas.json / %s" % (peca.get("slug") or peca.get("titulo") or "?")
                if not isinstance(peca.get("id"), int):
                    erro("%s: sem `id` de post. Peca cadastrada no painel tem id do "
                         "WordPress; catalogo escrito a mao nao tem." % onde)
                url_peca = str(peca.get("url") or "")
                if not url_peca.startswith("https://clubedomosaico.com.br/"):
                    erro("%s: `url` nao e do dominio da ilha (%r)" % (onde, url_peca))
        if copia_pecas.get("gerado_em"):
            # NAO e erro de dado, e sim de RUIDO: com o carimbo de hora dentro,
            # toda passada da ronda viraria commit, e a 24.2 manda commitar so
            # quando o JSON mudou. Foi decisao escrita no bloco de 14/09/2026.
            erro("dados/pecas.json carrega `gerado_em`: o carimbo de hora fica FORA da copia, "
                 "senao toda passada da ronda vira commit (24.2 manda commitar so quando o "
                 "JSON mudou).")


# ---------------------------------------------------------------- relatorio

# ---------------------------------------------- O CASAMENTO, RECONFERIDO PELA REGRA VIVA
#
# Aqui, e nao dentro do laco, porque a regra precisa do banco INTEIRO: ela so
# aprova um casamento quando UM registro passa nas travas, e isso se mede contra
# todos os outros. Reconferir registro a registro, sem os irmaos na mao, seria a
# metade da regra fingindo ser a regra.
if casamentos_a_reconferir:
    import importlib.util as _iu
    _s = _iu.spec_from_file_location(
        "casar_anuncio", os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      "casar-anuncio.py"))
    _casar = _iu.module_from_spec(_s)
    _s.loader.exec_module(_casar)
    _todos = list(materiais.values())

    def _irmaos(reg):
        marca = (reg.get("marca") or "").lower()
        return [x for x in _todos
                if (x.get("marca") or "").lower() == marca and x.get("id") != reg.get("id")]

    for onde, registro, titulo in casamentos_a_reconferir:
        escolhido, laudo = _casar.casar(titulo, _todos, _irmaos)
        if escolhido is None or escolhido.get("id") != registro.get("id"):
            motivo = ""
            for linha in laudo:
                if linha["id"] == registro.get("id"):
                    motivo = linha["motivo"] or ""
            erro("%s: o titulo gravado em `casamento` NAO identifica mais este registro "
                 "pela regra viva de casar-anuncio.py — %s. Ou a regra mudou, ou o banco "
                 "mudou, e nos dois casos a ficha esta apoiada numa prova que caducou "
                 "(secao 4 do contrato)" % (onde, motivo or "nenhum registro casou"))
    reconferidos = len(casamentos_a_reconferir)

print("Banco do Clube do Mosaico — verificacao do esquema do bloco 3")
print("  materiais no banco ......... %d" % len(materiais))
print("  celulas da F2 recomputadas . %d  (so categoria %s)" % (celulas_conferidas, CATEGORIA_DA_MATRIZ_F2))
print("  celulas do rejunte ......... %d" % celulas_rejunte_conferidas)
print("  pares da condicao (regra 6) . %d  (%d ancoras ponta a ponta)"
      % (pares_conferidos, ancoras_conferidas))
print("  itens esperando link ....... %d" % esperando_link)
print("  itens SEM SAIDA de compra .. %d  (secao 7 — tem de ser 0)" % sem_saida)
print("  piso NAO rastreavel ........ %d  (25.6 — divida de comissao, nao defeito)" % piso_nao_rastreavel)
print("  busca sem endereco cru ..... %d  (25.4-b)" % sem_busca_crua)
print("  a escada da 25.1, por degrau . 1:%d  2:%d  3:%d  4:%d  (soma %d)"
      % (por_degrau[1], por_degrau[2], por_degrau[3], por_degrau[4], sum(por_degrau.values())))
print("  degrau 4 com motivo escrito  %d de %d  (25.4-b.3: causa + ultima tentativa datada)"
      % (degrau_4_com_motivo, degrau_4_sem_ficha))
# A REPARTICAO, e nao so o total: a 25.4-b.4 diz que causas contadas juntas
# "viram um numero que nao diz o que fazer". `marca-nao-anunciada` e pedido de
# decisao ao Raphael; `candidato-barrado-*` e divida nossa. Somados, o pedido
# a ele desaparece dentro de uma divida tecnica que nao e dele.
for _classe in sorted(por_causa_do_degrau_4):
    print("    causa: %-28s %d" % (_classe, por_causa_do_degrau_4[_classe]))
print("  itens sem imagem ........... %d" % sem_imagem)
print("  casamentos reconferidos .... %d  (titulo gravado passado pela regra viva "
      "de casar-anuncio.py, contra o banco inteiro)" % reconferidos)
print("  batismos conferidos ........ %d  (nome_comercial lido contra o nome do arquivo "
      "da fonte que batiza, esquema v8)" % batismos_conferidos)
for n in notas:
    print("  nota: %s" % n)
for a in avisos:
    print("  AVISO: %s" % a)
if erros:
    print("\n%d ERRO(S):" % len(erros))
    for e in erros:
        print("  - %s" % e)
    sys.exit(1)
print("\nOK: o banco cumpre o esquema e a matriz da F2 bate com as declaracoes dos fabricantes.")
