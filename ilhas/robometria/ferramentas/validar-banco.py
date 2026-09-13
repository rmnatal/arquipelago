#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica se marcas.json, modelos-robo.json e pecas.json cumprem o contrato de
dados/esquema-banco.json.

Roda sem dependencia e sem rede:

    python3 ferramentas/validar-banco.py

Sai com codigo 1 se qualquer invariante for violada. Este arquivo NUNCA e publicado
no site: e ferramenta de bancada, como manda o esquema do manifest.

Por que ele existe: nesta ilha o produto e a afirmacao de compatibilidade. Uma
afirmacao errada aqui destroi a confianca inteira, e defeito de banco nao aparece
lendo o arquivo — aparece quando alguem compra a peca errada. O verificador e o que
transforma as regras escritas do esquema em algo que falha alto.
"""

import json
import os
import sys
from urllib.parse import unquote

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = os.path.join(BASE, "dados")

erros = []
avisos = []


def erro(msg):
    erros.append(msg)


def aviso(msg):
    avisos.append(msg)


def carregar(nome):
    with open(os.path.join(DADOS, nome), encoding="utf-8") as fh:
        return json.load(fh)


esquema = carregar("esquema-banco.json")
marcas = carregar("marcas.json")
modelos = carregar("modelos-robo.json")
pecas = carregar("pecas.json")

VOC = esquema["vocabularios"]
NIVEIS = {n["nivel"] for n in esquema["escada_de_fontes"]["niveis"]}

CAMPOS_MODELO_OBRIGATORIOS = [
    "pa_declarado", "potencia_w_declarada", "autonomia_min_declarada",
    "cobertura_m2_declarada", "recarga_min_declarada", "retoma_apos_recarga",
    "bateria_mah", "voltagem", "base_autoesvaziamento",
]

CHAVES_IMAGEM = {"url", "largura", "altura", "fonte", "coletado_em", "alt"}
# O `sub_id_2` SAIU DAQUI em 12/09/2026, e a ausencia dele e uma regra, nao uma
# limpeza. Ele nomeia a PAGINA que levou o clique, e o mesmo produto aparece em
# mais de uma: os 33 modelos traziam "R2" e as 18 pecas "R1", entao o A2 e o A1
# publicavam a vitrine deles com o codigo da ferramenta irma. Nao ha valor unico
# certo para escrever no registro — quem sabe qual e a pagina e quem a monta, e
# por isso cada gerador carimba o proprio codigo. Campo que parece a regra e nao
# e, num arquivo publicado, e o mesmo defeito da funcao morta no snippet: um dia
# alguem o usa.
CHAVES_AFILIADO = {"url", "url_produto", "motivo_sem_url_produto", "degrau",
                   "url_busca", "url_busca_produto", "motivo_sem_url_busca",
                   "plataforma", "coletado_em", "sub_id_1"}

# ---------------------------------------------------- A ESCADA DE COMPRA (25)
# Seis chaves entraram no campo afiliado na versao 5 do esquema, em 13/09/2026,
# e elas nao sao enfeite: a 25.2 diz que item publicavel SEM PISO e defeito da
# 19.1, sempre, em qualquer degrau. Ate hoje esta ilha tinha 62 itens publicaveis
# e ZERO piso, com a tela dizendo "link de loja em breve" em todo cartao.
#
# A REGUA DAQUI E PROPRIA E MAIS FRACA QUE A DO GERADOR, DE PROPOSITO. Ela NAO
# recompoe a palavra-chave chamando ferramentas/gerar-busca-de-produto.py: se
# chamasse, as duas metades errariam juntas e o portao ficaria verde sobre a mesma
# frase errada — foi exatamente assim que a atribuicao da funcao da R1 passou por
# todos os portoes ate hoje de manha. O que ela afirma, lendo o esquema e o
# marcas.json por conta propria, e o que precisa ser verdade seja qual for a
# composicao: a busca sai da base declarada, carrega a MARCA e carrega o TERMO DE
# CONTEXTO. As duas ultimas sao a 25.3 escrita em codigo — marca sem contexto e
# armadilha, e nesta ilha o CODIGO sem contexto tambem e ("S20" sozinho e um
# celular Samsung).
ESCADA = esquema["tipos_compostos"]["afiliado"].get("escada_de_compra")
if not isinstance(ESCADA, dict):
    erro("esquema-banco.json/tipos_compostos/afiliado: sem escada_de_compra. Sem ela "
         "nenhuma trava do piso da 25.2 tem regua, e todas aprovariam tudo")
    ESCADA = {"base_da_busca": "", "termo_de_contexto_por_entidade": {}, "degraus": []}

BASE_DA_BUSCA = ESCADA.get("base_da_busca") or ""
TERMOS_DE_CONTEXTO = ESCADA.get("termo_de_contexto_por_entidade") or {}
DEGRAUS = {d.get("degrau") for d in ESCADA.get("degraus", [])}

if not BASE_DA_BUSCA:
    erro("esquema-banco.json/escada_de_compra: sem base_da_busca")
if DEGRAUS != {1, 2, 3, 4}:
    erro("esquema-banco.json/escada_de_compra: os degraus declarados sao %s e a "
         "secao 25.1 tem exatamente 1, 2, 3 e 4" % sorted(d for d in DEGRAUS if d))
for _d in ESCADA.get("degraus", []):
    if not (_d.get("nome") or "").strip():
        erro("esquema-banco.json/escada_de_compra: degrau %r sem nome" % _d.get("degrau"))

# As duas entidades que geram busca. A lista mora aqui porque quem confere escreve a
# propria regua; o que ela cobra e que o ESQUEMA declare termo para cada uma, e nao
# o contrario.
ENTIDADE_DO_ARQUIVO = {"modelos-robo.json": "modelo_robo", "pecas.json": "peca"}
for _arq, _ent in ENTIDADE_DO_ARQUIVO.items():
    if not (TERMOS_DE_CONTEXTO.get(_ent) or "").strip():
        erro("esquema-banco.json/escada_de_compra: entidade %r (de %s) sem termo de "
             "contexto. Entidade muda faria a busca sair so com a marca, que e a "
             "armadilha que a 25.3 nomeia" % (_ent, _arq))

# Os tipos que o titulo do fabricante NAO separa. Lidos do esquema de proposito:
# ver tipos_que_exigem_funcao_declarada la, e o principio "FUNCAO NAO SE LE DO NOME
# DO PRODUTO". Se um dia esta chave sumir do esquema, a trava cai em silencio — por
# isso ela e exigida aqui em vez de ter valor de reserva.
if "tipos_que_exigem_funcao_declarada" not in esquema:
    erro("esquema-banco.json: sem tipos_que_exigem_funcao_declarada. A trava da funcao "
         "da escova le a lista daqui, e lista ausente faria a trava aprovar tudo")
TIPOS_COM_FUNCAO = set(
    esquema.get("tipos_que_exigem_funcao_declarada", {}).get("tipos", []))
for _t in TIPOS_COM_FUNCAO:
    if _t not in esquema["vocabularios"]["tipo_de_peca"]:
        erro("esquema-banco.json/tipos_que_exigem_funcao_declarada: %r nao existe no "
             "vocabulario tipo_de_peca" % _t)


ORIGEM_DO_NIVEL = {n["nivel"]: n["origem"] for n in esquema["escada_de_fontes"]["niveis"]}

# O degrau que chega a TELA. Ver escada_de_fontes.o_degrau_chega_a_TELA_pelo_na_tela.
NA_TELA = {n["origem"]: n.get("na_tela") for n in esquema["escada_de_fontes"]["niveis"]}
NIVEL_DA_ORIGEM = {n["origem"]: n["nivel"] for n in esquema["escada_de_fontes"]["niveis"]}

# Os dois degraus em que nada fica por confirmar: medicao propria e manual lido
# direto na fonte primaria. Do 3 para baixo a ressalva e obrigatoria, porque e
# ela que carrega a fraqueza do elo — e o cartao a imprime no lugar onde o
# leitor decide se compra.
NIVEIS_SEM_RESSALVA = {1, 2}
CHAVES_NA_TELA = {"rotulo", "ressalva", "quem_declara"}


def checar_escada_na_tela():
    """Todo degrau declara como ele APARECE na tela — os geradores leem daqui.

    Ate 11/09/2026 o rotulo e a ressalva de cada degrau moravam DIGITADOS dentro
    de ferramentas/gerar-r1.py, enquanto a escada os descrevia em prosa neste
    esquema. Duas copias do mesmo fato, nenhuma capaz de corrigir a outra: e a
    forma exata do defeito dos dois mapas de nome da casca 1.2.0. Agora a copia
    e uma so, e esta trava existe para que degrau novo nao nasca mudo — origem
    sem rotulo faria a tela imprimir o apelido de campo cru
    ('fabricante-via-busca') no meio de uma frase publicada.
    """
    for n in esquema["escada_de_fontes"]["niveis"]:
        onde = "esquema-banco/escada_de_fontes/nivel %d" % n["nivel"]
        t = n.get("na_tela")
        if not isinstance(t, dict):
            erro("%s: sem na_tela. Degrau que nao declara como aparece na tela "
                 "publica o apelido de campo cru para o leitor" % onde)
            continue
        if set(t) != CHAVES_NA_TELA:
            erro("%s: na_tela tem as chaves %s e o contrato pede %s"
                 % (onde, sorted(t), sorted(CHAVES_NA_TELA)))
            continue
        for campo in ("rotulo", "quem_declara"):
            if not isinstance(t[campo], str) or not t[campo].strip():
                erro("%s: na_tela.%s vazio" % (onde, campo))
        sem_ressalva = n["nivel"] in NIVEIS_SEM_RESSALVA
        if sem_ressalva and t["ressalva"] is not None:
            erro("%s: nivel %d nao deveria ter ressalva — nada fica por "
                 "confirmar acima do degrau 3" % (onde, n["nivel"]))
        if not sem_ressalva and not (isinstance(t["ressalva"], str) and t["ressalva"].strip()):
            erro("%s: nivel %d sem ressalva na tela. Do degrau 3 para baixo a "
                 "ressalva e o elo fraco dito com todas as letras, e ela e o "
                 "que impede a pagina de publicar um rigor que a ilha nao tem"
                 % (onde, n["nivel"]))

# Degraus que exigem ter LIDO o documento na fonte primaria. Ver
# escada_de_fontes.o_nivel_e_o_elo_mais_fraco no esquema.
NIVEIS_QUE_EXIGEM_LEITURA_DIRETA = {1, 2}
LEITURA_DIRETA = "direta-na-fonte-primaria"


def checar_fontes(reg, arquivo):
    """Toda fonte declarada tem nivel valido, origem coerente e data."""
    for fid, f in reg.get("fontes", {}).items():
        onde = "%s/%s/fontes/%s" % (arquivo, reg["id"], fid)
        if f.get("nivel") not in NIVEIS:
            erro("%s: nivel %r fora da escada_de_fontes" % (onde, f.get("nivel")))
        # O buraco por onde a contradicao de 11/09/2026 entrou: o nivel era
        # conferido e a ORIGEM nao, entao um manual de fabricante guardado por
        # terceiro podia se declarar nivel 2 com origem 'manual-fabricante' e
        # nada reprovava — enquanto a pagina de metodologia publicava "nivel 2:
        # temos hoje —". As duas metades nunca se encontravam.
        elif f.get("origem") != ORIGEM_DO_NIVEL[f["nivel"]]:
            erro("%s: nivel %d declara origem %r, e a escada diz %r. Nivel e origem sao "
                 "o mesmo degrau escrito duas vezes; divergir e contradizer a pagina de "
                 "metodologia, que le a escada"
                 % (onde, f["nivel"], f.get("origem"), ORIGEM_DO_NIVEL[f["nivel"]]))
        # A REGRA DO ELO MAIS FRACO, mecanica. Uma origem tem tres elos — quem
        # escreveu, quem guarda e como nos lemos — e o nivel e o do mais fraco.
        # Os dois degraus de cima exigem leitura na fonte primaria, e a unica
        # forma de provar isso e DECLARAR: silencio nunca promove. Adivinhar
        # pelo texto do canal_de_coleta seria a mesma heuristica por vizinhanca
        # que a secao 8 do ARQUIPELAGO.md proibe.
        if f.get("nivel") in NIVEIS_QUE_EXIGEM_LEITURA_DIRETA and f.get("leitura") != LEITURA_DIRETA:
            erro("%s: nivel %d sem declarar leitura=%r. Documento colhido por busca, ou "
                 "guardado por terceiro, e nivel 3 — errar para cima faz a ilha publicar "
                 "um rigor que ela nao tem, e a metodologia e a pagina cujo unico produto "
                 "e o rigor" % (onde, f["nivel"], LEITURA_DIRETA))
        if not f.get("verificado_em"):
            erro("%s: sem verificado_em" % onde)
        if not f.get("titulo_na_fonte"):
            erro("%s: sem titulo_na_fonte — a frase publicada nao tem o que citar" % onde)
        if not f.get("canal_de_coleta"):
            erro("%s: sem canal_de_coleta" % onde)
        # Origem citada pelo banco tem que saber se apresentar na tela. A trava
        # de cima cobre a escada; esta cobre o caminho inverso, que e por onde o
        # defeito entraria de verdade: um registro citando uma origem que a
        # escada nao tem.
        if f.get("origem") not in NA_TELA:
            erro("%s: origem %r nao existe na escada_de_fontes, entao nao tem "
                 "rotulo de tela" % (onde, f.get("origem")))


def checar_campo_de_valor(reg, campo, arquivo):
    """Valor nao nulo precisa de fonte existente; valor nulo precisa de motivo."""
    onde = "%s/%s/%s" % (arquivo, reg["id"], campo)
    v = reg.get(campo)
    if v is None:
        erro("%s: campo obrigatorio ausente" % onde)
        return
    if not isinstance(v, dict) or "valor" not in v:
        erro("%s: nao tem a forma campo_de_valor {valor, fonte, declarado_como}" % onde)
        return
    if v["valor"] is None:
        if not v.get("motivo_do_null"):
            erro("%s: valor null sem motivo_do_null. 'nao sei' e resposta legitima, "
                 "mas precisa estar escrita" % onde)
    else:
        fid = v.get("fonte")
        if not fid:
            erro("%s: valor %r sem fonte. Numero sem procedencia nao vai para a tela"
                 % (onde, v["valor"]))
        elif fid not in reg.get("fontes", {}):
            erro("%s: aponta para a fonte %r, que nao existe neste registro" % (onde, fid))
        if not v.get("declarado_como"):
            erro("%s: sem declarado_como — sem a transcricao a pagina parafraseia o "
                 "fabricante em vez de cita-lo" % onde)


# ---------------------------------------------------------------- MARCAS
ids_marca = set()
for m in marcas["registros"]:
    if m["id"] in ids_marca:
        erro("marcas.json: id duplicado %r" % m["id"])
    ids_marca.add(m["id"])
    for c in ("nome", "nome_de_busca", "site_oficial", "sameAs", "verificado_em"):
        if not m.get(c):
            erro("marcas.json/%s: campo obrigatorio %s vazio" % (m["id"], c))

NOME_DE_BUSCA = {m["id"]: (m.get("nome_de_busca") or "").strip()
                 for m in marcas["registros"]}


def checar_escada_de_compra(reg, onde, arquivo):
    """O PISO da secao 25.2, item por item.

    Tres coisas diferentes sao cobradas aqui, e vale separar porque elas falham por
    motivos diferentes:

    1. PISO. Registro publicavel tem url_busca_produto, e ela carrega marca e
       contexto. Registro NAO publicavel tem que estar VAZIO: ele nao tem pagina,
       entao nao tem piso a cumprir, e escrever "robo aspirador" na busca de um
       aspirador vertical seria afirmacao falsa dentro do banco.
    2. HONESTIDADE DO QUE FALTA. Piso sem o link encurtado exige motivo escrito, e
       motivo escrito COM o link seria mentira sobrando.
    3. DEGRAU. Ficha de produto sem degrau e link cuja durabilidade ninguem sabe: o
       mesmo encurtador serve loja oficial e anuncio de vendedor com a MESMA cara, e
       os dois apodrecem de forma oposta. E degrau 3 sem busca e o beco sem saida que
       quebrou quatro links em doze horas no Clube do Mosaico.
    """
    a = reg.get("afiliado") or {}
    publicavel = reg.get("status") == "publicavel"
    entidade = ENTIDADE_DO_ARQUIVO.get(arquivo, "")
    termo = (TERMOS_DE_CONTEXTO.get(entidade) or "").strip()
    busca = a.get("url_busca_produto") or ""

    if publicavel:
        if not busca:
            erro("%s: publicavel sem afiliado.url_busca_produto. A 25.2 e explicita — "
                 "item publicavel sem PISO e defeito da 19.1, em qualquer degrau. "
                 "Rode ferramentas/gerar-busca-de-produto.py --gravar" % onde)
        else:
            if not busca.startswith(BASE_DA_BUSCA):
                erro("%s: url_busca_produto nao comeca pela base declarada no esquema "
                     "(%r)" % (onde, BASE_DA_BUSCA))
            legivel = unquote(busca[len(BASE_DA_BUSCA):]) if \
                busca.startswith(BASE_DA_BUSCA) else unquote(busca)
            marca = NOME_DE_BUSCA.get(reg.get("marca"), "")
            if marca and marca.lower() not in legivel.lower():
                erro("%s: a busca %r nao carrega o nome_de_busca da marca (%r)"
                     % (onde, legivel, marca))
            if termo and termo.lower() not in legivel.lower():
                erro("%s: a busca %r nao carrega o termo de contexto %r. Marca sem "
                     "contexto e armadilha (25.3), e nesta ilha o codigo sem contexto "
                     "tambem e: 'S20' sozinho e um celular de outra marca"
                     % (onde, legivel, termo))
    elif busca:
        erro("%s: registro %r com url_busca_produto escrita. Registro sem pagina nao "
             "tem piso a cumprir, e a busca diria 'robo aspirador' sobre um aparelho "
             "que o portao da categoria ja recusou" % (onde, reg.get("status")))

    tem_busca_encurtada = bool(a.get("url_busca"))
    motivo_busca = a.get("motivo_sem_url_busca")
    if publicavel and not tem_busca_encurtada and not (motivo_busca or "").strip():
        erro("%s: sem afiliado.url_busca e sem motivo_sem_url_busca. Piso que falta "
             "sem motivo escrito e divida que a proxima execucao nao sabe medir" % onde)
    if tem_busca_encurtada and motivo_busca:
        erro("%s: tem url_busca E motivo_sem_url_busca. O motivo explica uma ausencia "
             "que nao existe mais" % onde)

    tem_ficha = bool(a.get("url"))
    degrau = a.get("degrau")
    if tem_ficha:
        if degrau not in {1, 2, 3, 4}:
            erro("%s: tem ficha de produto e degrau %r. Degrau nao se le do link curto "
                 "— s.shopee.com.br encurta a loja oficial e o anuncio de vendedor com "
                 "a MESMA cara, e os dois apodrecem de forma oposta" % (onde, degrau))
        if not a.get("url_produto") and not (a.get("motivo_sem_url_produto") or "").strip():
            erro("%s: tem ficha e nao tem url_produto nem motivo_sem_url_produto. Sem a "
                 "URL crua a ronda nao consegue abrir a pagina para ler 'O produto nao "
                 "existe' — e item que ninguem consegue conferir e defeito da 19.1 com "
                 "outro nome (25.4-b)" % onde)
        if degrau == 3 and not tem_busca_encurtada:
            erro("%s: degrau 3 (anuncio de vendedor) sem url_busca. A 25.1 exige a busca "
                 "justamente neste degrau, que e o que apodrece" % onde)
    else:
        if degrau is not None:
            erro("%s: degrau %r sem ficha de produto. Degrau descreve ONDE a ficha "
                 "parou, e ficha que nao existe nao parou em lugar nenhum"
                 % (onde, degrau))
        if a.get("url_produto"):
            erro("%s: url_produto sem url. A URL crua existe para conferir a ficha que "
                 "foi escolhida, e nao ha ficha" % onde)

# ---------------------------------------------------------- MODELOS DE ROBO
ids_modelo = {}
for r in modelos["registros"]:
    onde = "modelos-robo.json/%s" % r["id"]
    if r["id"] in ids_modelo:
        erro("%s: id duplicado" % onde)
    ids_modelo[r["id"]] = r

    if r["marca"] not in ids_marca:
        erro("%s: marca %r nao existe em marcas.json" % (onde, r["marca"]))
    if r["categoria"] not in VOC["categoria"]:
        erro("%s: categoria %r fora do vocabulario" % (onde, r["categoria"]))
    if r["status"] not in VOC["status_do_registro"]:
        erro("%s: status %r fora do vocabulario" % (onde, r["status"]))

    # O PORTAO: so robo confirmado pode ser publicavel.
    if r["status"] == "publicavel" and r["categoria"] != "robo":
        erro("%s: PORTAO VIOLADO — status publicavel com categoria %r. So entra no site "
             "modelo que o proprio fabricante chama de aspirador robo" % (onde, r["categoria"]))
    if r["status"] != "publicavel" and not r.get("motivo_do_status"):
        erro("%s: status %r sem motivo_do_status" % (onde, r["status"]))

    checar_fontes(r, "modelos-robo.json")
    for campo in CAMPOS_MODELO_OBRIGATORIOS:
        checar_campo_de_valor(r, campo, "modelos-robo.json")

    if set(r.get("imagem", {})) < CHAVES_IMAGEM:
        erro("%s: imagem{} incompleta — falta %s"
             % (onde, sorted(CHAVES_IMAGEM - set(r.get("imagem", {})))))
    if "sub_id_2" in (r.get("afiliado") or {}):
        erro("%s: afiliado.sub_id_2 no banco. O codigo da pagina de origem e "
             "carimbado por quem monta a pagina (gerar-r1/r2/a1/a2), porque o "
             "mesmo modelo aparece em mais de uma" % onde)
    elif set(r.get("afiliado", {})) != CHAVES_AFILIADO:
        erro("%s: afiliado{} fora da forma do esquema" % onde)
    elif r["afiliado"]["sub_id_1"] != "robometria":
        erro("%s: sub_id_1 tem que ser 'robometria'" % onde)
    checar_escada_de_compra(r, onde, "modelos-robo.json")

    for var in r.get("variantes_de_hardware", []):
        if var.get("fonte") not in r.get("fontes", {}):
            erro("%s: variante %r aponta para fonte inexistente" % (onde, var.get("rotulo")))

    v = r.get("voltagem", {})
    if v.get("valor") is not None and str(v["valor"]) not in [x for x in VOC["voltagem"] if x]:
        erro("%s: voltagem %r fora do vocabulario. Nunca chutar 127 ou 220" % (onde, v["valor"]))

    # Divergencia de ESPECIFICACAO DE APARELHO, nova na versao 3 do esquema. Ate a versao 2
    # so PECA divergia, porque a divergencia conhecida era de compatibilidade. O PRA500
    # declara 1600 Pa na ficha e 2000 Pa no texto de venda da MESMA pagina — e um numero
    # de succao errado manda alguem comprar um robo fraco demais para a casa dele.
    if "divergencias" not in r:
        erro("%s: divergencias ausente. Lista vazia e afirmacao ('nao encontramos "
             "declaracao divergente'); ausencia e omissao" % onde)
    if r.get("divergencias") and not r.get("resolucao"):
        erro("%s: tem divergencias e nao diz qual valor valeu nem qual e o erro caro que "
             "decidiu a direcao. Divergencia sem resolucao escrita e a ilha empurrando a "
             "duvida para o visitante — e escolher pela media e proibido" % onde)
    for dv in r.get("divergencias", []):
        campo = dv.get("campo")
        if not campo:
            erro("%s: item de divergencias sem 'campo' — nao da para saber o que diverge"
                 % onde)
        elif campo not in r:
            erro("%s: divergencia sobre o campo %r, que nao existe neste registro"
                 % (onde, campo))
        if not dv.get("transcricao"):
            erro("%s: divergencia sem transcricao. Sem o texto do fabricante a pagina "
                 "parafraseia os DOIS lados em vez de citar" % onde)

# ------------------------------------------------------------------ PECAS
ids_peca = set()
pares = 0
for p in pecas["registros"]:
    onde = "pecas.json/%s" % p["id"]
    if p["id"] in ids_peca:
        erro("%s: id duplicado" % onde)
    ids_peca.add(p["id"])

    if p["marca"] not in ids_marca:
        erro("%s: marca %r nao existe em marcas.json" % (onde, p["marca"]))
    if p["tipo"] not in VOC["tipo_de_peca"]:
        erro("%s: tipo %r fora do vocabulario" % (onde, p["tipo"]))

    # A FUNCAO NAO SE LE DO NOME DO PRODUTO (esquema, principio de 13/09/2026).
    # O fabricante batiza a peca pela POSICAO e o banco a classifica pela FUNCAO. A
    # WAP prova que as duas nao coincidem: o conteudo declarado do W300 chama de
    # 'escovas giratorias' o PAR LATERAL e o artigo de limpeza do W90 chama de
    # 'escova giratoria' a PRINCIPAL — mesma palavra, mesmo fabricante, funcoes
    # opostas. Quem grava tem de dizer de ONDE leu.
    # A lista de tipos mora no ESQUEMA e nao aqui: numero e lista digitados dentro
    # da regua envelhecem calados, e esta ilha ja pagou por isso no teste-acentuacao.
    if p["tipo"] in TIPOS_COM_FUNCAO:
        f = p.get("funcao")
        if not f:
            erro("%s: tipo %r sem funcao{}. O titulo do fabricante nomeia a posicao, nao a "
                 "funcao — sem dizer onde a funcao foi declarada, o tipo e um palpite com "
                 "cara de dado" % (onde, p["tipo"]))
        else:
            if f.get("declarada_por") not in VOC["funcao_declarada_por"]:
                erro("%s: funcao.declarada_por %r fora do vocabulario"
                     % (onde, f.get("declarada_por")))
            if f.get("fonte") not in p.get("fontes", {}):
                erro("%s: funcao aponta para a fonte %r, que nao existe em fontes{}"
                     % (onde, f.get("fonte")))
            if not f.get("declarado_como"):
                erro("%s: funcao sem declarado_como — nao sobra o que citar nem o que "
                     "reconferir na proxima passada" % onde)
    elif p.get("funcao"):
        erro("%s: funcao{} em peca do tipo %r. O campo existe para os tipos que o titulo "
             "do fabricante nao separa, e esta lista esta no esquema" % (onde, p["tipo"]))

    # Kit e caixa fechada ate declarar o que tem dentro. Sem isto a R1 sabe QUE o kit
    # serve e nao consegue dizer que o filtro do ERB10 vem dentro dele — que e a resposta
    # que a pessoa procurou.
    if p["tipo"] == "kit":
        if not p.get("composicao"):
            erro("%s: tipo kit sem composicao. Kit sem composicao e caixa fechada: a R1 nao "
                 "consegue responder 'qual filtro serve no meu modelo'" % onde)
        for item in p.get("composicao", []):
            t = item.get("tipo")
            if t == "kit":
                erro("%s: composicao com item do tipo kit — kit dentro de kit nao existe "
                     "neste banco" % onde)
            elif t is not None and t not in VOC["tipo_de_peca"]:
                erro("%s: composicao com tipo %r fora do vocabulario" % (onde, t))
            elif t is None and not item.get("descricao_na_fonte"):
                erro("%s: item de composicao sem tipo E sem descricao_na_fonte — nao sobra "
                     "nada para a tela" % onde)
    elif p.get("composicao"):
        erro("%s: composicao so existe em peca do tipo kit" % onde)

    # Nem todo fabricante publica codigo. Isso e resposta, e como toda resposta null
    # nesta ilha, ela tem que estar escrita.
    if p.get("codigo_fabricante") is None and not p.get("motivo_sem_codigo"):
        erro("%s: codigo_fabricante null sem motivo_sem_codigo. 'o fabricante nao publica "
             "codigo' e resposta legitima, mas precisa estar escrita" % onde)
    if p["status"] not in VOC["status_do_registro"]:
        erro("%s: status %r fora do vocabulario" % (onde, p["status"]))
    if p["status"] != "publicavel" and not p.get("motivo_do_status"):
        erro("%s: status %r sem motivo_do_status" % (onde, p["status"]))
    if not p.get("nome_na_fonte"):
        erro("%s: sem nome_na_fonte" % onde)

    checar_fontes(p, "pecas.json")
    checar_campo_de_valor(p, "vida_util_declarada", "pecas.json")

    if "divergencias" not in p:
        erro("%s: divergencias ausente. Lista vazia e afirmacao ('nao encontramos "
             "declaracao divergente'); ausencia e omissao" % onde)
    if p.get("divergencias") and not p.get("resolucao"):
        erro("%s: tem divergencias e nao diz qual conjunto valeu. Divergencia sem "
             "resolucao escrita e a ilha empurrando a duvida para o visitante" % onde)

    if set(p.get("imagem", {})) < CHAVES_IMAGEM:
        erro("%s: imagem{} incompleta" % onde)
    if "sub_id_2" in (p.get("afiliado") or {}):
        erro("%s: afiliado.sub_id_2 no banco. O codigo da pagina de origem e "
             "carimbado por quem monta a pagina (gerar-r1/r2/a1/a2), porque a "
             "mesma peca aparece em mais de uma" % onde)
    elif set(p.get("afiliado", {})) != CHAVES_AFILIADO:
        erro("%s: afiliado{} fora da forma do esquema" % onde)
    checar_escada_de_compra(p, onde, "pecas.json")

    if not p.get("compatibilidade"):
        erro("%s: peca sem nenhum par de compatibilidade" % onde)
    for c in p.get("compatibilidade", []):
        if c["selo"] not in VOC["selo_de_compatibilidade"]:
            erro("%s: selo %r fora do vocabulario" % (onde, c["selo"]))
        if c["selo"] == "nao_declarada":
            erro("%s: par com selo nao_declarada listado como compatibilidade "
                 "afirmativa. nao_declarada e o caso em que a R1 diz que nao achou "
                 "e para ali" % onde)
        if c.get("fonte") not in p.get("fontes", {}):
            erro("%s: par %r aponta para fonte inexistente" % (onde, c.get("codigo_declarado")))
        if not c.get("codigo_declarado"):
            erro("%s: par sem codigo_declarado" % onde)
        if c.get("modelo") is None:
            aviso("%s: par %r sem modelo no banco (permitido, mas e lista de compras)"
                  % (onde, c.get("codigo_declarado")))
        elif c["modelo"] not in ids_modelo:
            erro("%s: par aponta para o modelo %r, que nao existe em modelos-robo.json"
                 % (onde, c["modelo"]))
        else:
            alvo = ids_modelo[c["modelo"]]
            if p["status"] == "publicavel" and alvo["status"] == "excluido_do_banco":
                erro("%s: peca publicavel declarada compativel com %r, que esta "
                     "excluido do banco por nao ser robo" % (onde, c["modelo"]))
            rotulos = [x.get("rotulo") for x in alvo.get("variantes_de_hardware", [])]
            if rotulos and c.get("variante_de_hardware") is None:
                aviso("%s: o modelo %r tem variantes %s e este par esta com "
                      "variante null, o que pelo esquema significa 'serve em todas as "
                      "conhecidas'. Confirmar na fonte que vale para %s antes de a R1 "
                      "afirmar isso na tela"
                      % (onde, c["modelo"], rotulos, " e ".join(map(str, rotulos))))
            if c.get("variante_de_hardware") and c["variante_de_hardware"] not in rotulos:
                erro("%s: variante %r nao existe no modelo %r"
                     % (onde, c["variante_de_hardware"], c["modelo"]))
        if p["status"] == "publicavel":
            pares += 1

# --------------------------------------------------- CONTAGENS DO CABECALHO
def conferir_contagem(doc, arquivo, chave, esperado):
    declarado = doc.get("contagem", {}).get(chave)
    if declarado != esperado:
        erro("%s: contagem.%s diz %r e o arquivo tem %r"
             % (arquivo, chave, declarado, esperado))

conferir_contagem(modelos, "modelos-robo.json", "total", len(modelos["registros"]))

# O cabecalho de modelos-robo.json anuncia a cobertura do campo que decide se a R2 sai com
# lista ou vazia. Contagem que nao bate com o arquivo e pior que contagem nenhuma: e um
# numero que a proxima execucao vai acreditar sem conferir.
_pub = [r for r in modelos["registros"] if r["status"] == "publicavel"]
conferir_contagem(modelos, "modelos-robo.json", "publicavel", len(_pub))
conferir_contagem(modelos, "modelos-robo.json", "com_pa_declarado",
                  sum(1 for r in _pub if r["pa_declarado"]["valor"] is not None))
conferir_contagem(modelos, "modelos-robo.json", "com_par_minutos_m2_declarado",
                  sum(1 for r in _pub if r["autonomia_min_declarada"]["valor"] is not None
                      and r["cobertura_m2_declarada"]["valor"] is not None))
conferir_contagem(modelos, "modelos-robo.json", "marcas_que_declaram_pa",
                  sorted({r["marca"] for r in _pub
                          if r["pa_declarado"]["valor"] is not None}))
conferir_contagem(modelos, "modelos-robo.json", "esperando_link_de_afiliado",
                  sum(1 for r in _pub if not r["afiliado"]["url"]))
conferir_contagem(pecas, "pecas.json", "total", len(pecas["registros"]))

# A DIVIDA DO PISO DEIXA DE SER PROSA E VIRA NUMERO CONTADO, em 13/09/2026. Enquanto
# ela morava no ESTADO.md em forma de frase, a divida nao tinha tamanho: o cabecalho
# dizia "nenhum link de loja em nenhum cartao" e NAO dizia quantos itens estavam sem
# PISO, que e outra coisa e e a que a 25.2 chama de defeito. Vale a mesma regra que a
# casca aprendeu com o cartao que dizia zero: numero de tela nasce contado, nunca
# digitado — e numero de cabecalho de banco tambem.
for _doc, _arq in ((modelos, "modelos-robo.json"), (pecas, "pecas.json")):
    _p = [r for r in _doc["registros"] if r["status"] == "publicavel"]
    conferir_contagem(_doc, _arq, "itens_com_ficha",
                      sum(1 for r in _p if r["afiliado"]["url"]))
    conferir_contagem(_doc, _arq, "itens_sem_piso",
                      sum(1 for r in _p if not r["afiliado"]["url_busca"]))
    conferir_contagem(_doc, _arq, "links_sem_degrau",
                      sum(1 for r in _p if r["afiliado"]["url"]
                          and r["afiliado"]["degrau"] is None))
conferir_contagem(pecas, "pecas.json", "pares_peca_x_modelo_declarados", pares)

esperando = ([r["id"] for r in modelos["registros"]
              if r["status"] == "publicavel" and not r["afiliado"]["url"]] +
             [p["id"] for p in pecas["registros"]
              if p["status"] == "publicavel" and not p["afiliado"]["url"]])

checar_escada_na_tela()

# ------------------------------------------------------------------ SAIDA
print("Robometria — verificacao do banco (esquema versao %s)" % esquema["versao_esquema"])
print("  marcas ............... %d" % len(marcas["registros"]))
print("  modelos de robo ...... %d (%d publicaveis, %d excluidos por nao serem robo)"
      % (len(modelos["registros"]),
         sum(1 for r in modelos["registros"] if r["status"] == "publicavel"),
         sum(1 for r in modelos["registros"] if r["status"] == "excluido_do_banco")))
print("  pecas ................ %d (%d publicaveis)"
      % (len(pecas["registros"]),
         sum(1 for p in pecas["registros"] if p["status"] == "publicavel")))
print("  pares peca x modelo .. %d, todos DECLARADOS pelo fabricante" % pares)
print("  esperando link de afiliado ... %d" % len(esperando))
_sem_piso = [r["id"] for _doc in (modelos, pecas) for r in _doc["registros"]
             if r["status"] == "publicavel" and not r["afiliado"]["url_busca"]]
_sem_chave = [r["id"] for _doc in (modelos, pecas) for r in _doc["registros"]
              if r["status"] == "publicavel" and not r["afiliado"]["url_busca_produto"]]
print("  SEM PISO (25.2) ............. %d de %d publicaveis, e %d deles sem nem a "
      "palavra-chave escrita"
      % (len(_sem_piso),
         sum(1 for _doc in (modelos, pecas) for r in _doc["registros"]
             if r["status"] == "publicavel"),
         len(_sem_chave)))

if avisos:
    print("\nAvisos (%d) — nao reprovam, sao lista de trabalho:" % len(avisos))
    for a in avisos:
        print("  . " + a)

if erros:
    print("\nREPROVADO — %d invariante(s) violada(s):" % len(erros))
    for e in erros:
        print("  x " + e)
    sys.exit(1)

print("\nAPROVADO: nenhuma invariante do esquema violada.")
