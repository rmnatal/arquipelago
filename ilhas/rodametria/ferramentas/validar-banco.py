#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validador do banco da Rodametria — o portao que cobra dados/esquema-banco.json.

Roda sem rede. Uso:

    python3 ferramentas/validar-banco.py            # da raiz da ilha
    python3 ferramentas/validar-banco.py --json      # so o veredito, para outro portao ler

NADA AQUI E LISTA DIGITADA DE CABECA. O enum de cada campo, o piso de nivel de fonte por
campo, a lista de campos que exigem procedencia de leitura e os grupos de prestacao de contas
saem todos do ESQUEMA; o status de constante sai de dados/constantes.json. Regua que guarda a
propria lista envelhece calada (secao 26.2 do ARQUIPELAGO.md), e e por isso que a bateria
ferramentas/mutacoes-banco.py apaga chaves DO ESQUEMA e exige que este arquivo REPROVE.
"""
import json
import sys
from pathlib import Path


def carregar(raiz):
    raiz = Path(raiz)
    def ler(rel):
        return json.loads((raiz / rel).read_text(encoding="utf-8"))
    return {
        "esquema": ler("dados/esquema-banco.json"),
        "constantes": ler("dados/constantes.json"),
        "veiculos": ler("dados/veiculos.json"),
        "pecas": ler("dados/pecas.json"),
        "municipios": ler("dados/municipios.json"),
    }


# --------------------------------------------------------------------- auxiliares
def _slug(s):
    return isinstance(s, str) and s == s.lower() and " " not in s and s.strip("-") == s \
        and all(c.isalnum() or c == "-" for c in s)


def _status_da_constante(constantes, id_):
    for c in constantes.get("constantes", []):
        if c.get("id") == id_:
            return c.get("status")
    return None


def _campos_tecnicos_do_esquema(esquema):
    tec = esquema["entidades"]["VEICULO"]["campos_tecnicos"]
    # `forma_do_campo` e prosa (string) e cai fora sozinho; `acelerador` NAO tem unidade e
    # precisa entrar — filtrar por "unidade" o deixava de fora, e ele e o PIVO da F1.
    return {k: v for k, v in tec.items() if isinstance(v, dict)}


def grupos_f1(v):
    """Onde este veiculo cai na prestacao de contas da F1. Lista, para que o
    validador possa provar que ela tem EXATAMENTE um elemento."""
    g = []
    if not v.get("_piso"):
        g.append("sem_saida_de_compra")
    elif (v.get("potencia_nominal_w") or {}).get("valor") is None:
        g.append("sem_potencia_nominal_declarada")
    elif v.get("categoria") is None:
        # categoria null com nominal declarado so acontece enquanto o limiar e pendente;
        # a F1 nao esta no ar nesse estado, e o registro nao e candidato de nenhum grupo.
        g.append("sem_categoria_derivada")
    else:
        g.append("cabe_na_categoria_ou_de_outra")
    return g


def grupos_f2(v):
    g = []
    if not v.get("_piso"):
        g.append("sem_saida_de_compra")
    elif (v.get("tensao_v") or {}).get("valor") is None or \
         (v.get("amperagem_ah") or {}).get("valor") is None:
        g.append("nao_declara_tensao_ou_amperagem")
    else:
        g.append("cabe_no_wh_pedido_ou_de_outro_wh")
    return g


def grupos_f3(v):
    g = []
    if not v.get("_piso"):
        g.append("sem_saida_de_compra")
    elif (v.get("carga_max_kg") or {}).get("valor") is None:
        g.append("nao_declara_carga_maxima")
    else:
        g.append("aguenta_com_folga_ou_limite_ou_nao")
    return g


# --------------------------------------------------------------------- o portao
def validar(dados):
    """Devolve (falhas, avisos, contagem). Falha = o banco esta errado. Aviso = o banco
    esta certo e incompleto, e o numero vai para o relatorio."""
    falhas, avisos = [], []
    cont = {}
    esq = dados["esquema"]
    const = dados["constantes"]

    def falha(onde, o_que):
        falhas.append("%s: %s" % (onde, o_que))

    # ---- 0. o esquema tem de ter as chaves que este portao LE. Chave que some aprova
    #         tudo em silencio, e e isso que a 26.2 manda reprovar.
    exigidas = [
        ("campos_que_exigem_procedencia_de_leitura", ["campos", "origens_legitimas_de_leitura"]),
        ("escada_de_fontes", ["niveis", "origens_validas", "niveis_que_exigem_leitura_declarada",
                              "niveis_minimos_por_campo"]),
        ("entidades", ["VEICULO", "PECA", "MUNICIPIO"]),
        ("grupos_de_prestacao_de_contas", ["F1", "F2", "F3"]),
    ]
    for chave, subs in exigidas:
        if chave not in esq:
            falha("esquema", "a chave `%s` desapareceu do esquema. Este portao LE essa chave; "
                             "sem ela ele aprovaria o banco em silencio (26.2)" % chave)
            continue
        for s in subs:
            if s not in esq[chave]:
                falha("esquema", "a chave `%s.%s` desapareceu do esquema (26.2)" % (chave, s))
    if falhas:
        return falhas, avisos, cont

    esc = esq["escada_de_fontes"]
    origem_por_nivel = {n["nivel"]: n["origem"] for n in esc["niveis"]}
    exigem_leitura = set(esc["niveis_que_exigem_leitura_declarada"])
    piso_por_campo = esc["niveis_minimos_por_campo"]["pior_nivel_aceito"]
    campos_com_leitura = set(esq["campos_que_exigem_procedencia_de_leitura"]["campos"])
    origens_leitura = set(esq["campos_que_exigem_procedencia_de_leitura"]["origens_legitimas_de_leitura"])
    tecnicos = _campos_tecnicos_do_esquema(esq)
    ident = esq["entidades"]["VEICULO"]["campos_de_identidade"]
    enum_tipo_comercial = set(ident["tipo_comercial"]["valores"])
    derivados = esq["entidades"]["VEICULO"]["campos_derivados"]
    enum_categoria = set(x for x in derivados["categoria"]["valores"] if x)
    enum_acelerador = set(tecnicos["acelerador"]["valores"])
    enum_status = set(esq["entidades"]["VEICULO"]["campos_de_estado"]["status"]["valores"])
    enum_tipo_peca = set(esq["entidades"]["PECA"]["campos_de_identidade"]["tipo"]["valores"])
    chave_por_tipo_peca = esq["entidades"]["PECA"]["compatibilidade"]["por_tipo"]

    # ---- 1. os dois enums de classificacao nao podem ter valor em comum
    comum = enum_tipo_comercial & enum_categoria
    if comum:
        falha("esquema", "`tipo_comercial` e `categoria` compartilham %s. O que o anuncio chama "
                         "nao pode ser gravavel como categoria da resolucao" % sorted(comum))

    # ---- 2. a constante que trava a categoria
    st_limiar = _status_da_constante(const, "limiares-categoria-contran-996-2023")
    if st_limiar is None:
        falha("constantes", "a constante `limiares-categoria-contran-996-2023` nao existe mais em "
                            "dados/constantes.json. Este portao le o STATUS dela para decidir se "
                            "`categoria` pode ser nao-null")
    categoria_travada = (st_limiar != "publicavel")

    # ---- 3. VEICULO, registro por registro
    vistos = set()
    regs = dados["veiculos"].get("registros", [])
    if dados["veiculos"].get("versao_esquema") != esq["versao_esquema"]:
        falha("veiculos.json", "versao_esquema %r nao bate com a do esquema (%r)"
              % (dados["veiculos"].get("versao_esquema"), esq["versao_esquema"]))

    for v in regs:
        onde = "veiculo %s" % v.get("id")
        if not _slug(v.get("id")):
            falha(onde, "`id` nao e slug")
        if v.get("id") in vistos:
            falha(onde, "`id` repetido")
        vistos.add(v.get("id"))

        for c, mot in (("marca", "motivo_sem_marca"), ("modelo", "motivo_sem_modelo")):
            if c not in v:
                falha(onde, "a chave `%s` esta ausente — ausente e diferente de null" % c)
            elif v.get(c) is None and not v.get(mot):
                falha(onde, "`%s` e null e nao ha `%s`. Null e resposta, e resposta tem motivo" % (c, mot))

        if not v.get("titulo_colhido"):
            falha(onde, "`titulo_colhido` vazio. O titulo literal e PROVA: a tese da ilha e que o nome "
                        "do anuncio nao e o que a regra le, e sem o literal a tese nao se demonstra")
        if v.get("tipo_comercial") not in enum_tipo_comercial:
            falha(onde, "`tipo_comercial` %r fora do enum" % v.get("tipo_comercial"))

        fontes = v.get("fontes") or {}
        if not fontes:
            falha(onde, "sem `fontes{}`. Nenhum numero entra no banco sem entrada em fontes{}")
        for fid, f in fontes.items():
            o = "%s / fonte %s" % (onde, fid)
            nivel = f.get("nivel")
            if nivel not in origem_por_nivel:
                falha(o, "`nivel` %r nao existe na escada" % nivel)
                continue
            if f.get("origem") != origem_por_nivel[nivel]:
                falha(o, "`origem` %r nao e a que a escada da ao nivel %s (%r). O defeito da Robometria "
                         "entrava por aqui, porque so o numero era conferido"
                      % (f.get("origem"), nivel, origem_por_nivel[nivel]))
            if nivel in exigem_leitura and not f.get("leitura"):
                falha(o, "nivel %s exige `leitura` declarada, e silencio nunca promove" % nivel)
            for campo_obrig in ("url", "autoria", "custodia", "data_leitura"):
                if campo_obrig not in f:
                    falha(o, "falta `%s`" % campo_obrig)

        # campos tecnicos
        for nome, decl in tecnicos.items():
            if nome not in v:
                falha(onde, "a chave `%s` esta ausente. Campo ausente no mundo e {valor: null, "
                            "motivo: ...}, nunca chave faltando" % nome)
                continue
            obj = v[nome] or {}
            val = obj.get("valor")
            if val is None:
                if nome == "acelerador":
                    falha(onde, "`acelerador` com valor null. E o PIVO da F1 e nao aceita nulo: enum de "
                                "tres valores, e `nao_declarado` e o terceiro")
                elif not obj.get("motivo"):
                    falha(onde, "`%s` e null e nao ha `motivo`" % nome)
                continue
            # valor presente
            if nome == "acelerador":
                if val not in enum_acelerador:
                    falha(onde, "`acelerador` %r fora do enum %s" % (val, sorted(enum_acelerador)))
            sentinela = decl.get("valor_sentinela_de_ausencia")
            if sentinela is not None and val == sentinela:
                # O conteudo deste valor E a ausencia de declaracao: exigir `declarado_como` dele
                # seria cobrar o literal de uma frase que nao existe. Exige-se onde se olhou e por que
                # nao se achou. O nome da sentinela sai do ESQUEMA, nunca daqui (26.2).
                if not obj.get("motivo"):
                    falha(onde, "`%s` = %r (sentinela de ausencia) sem `motivo`. O terceiro valor tem "
                                "frase propria, e a frase nasce do motivo" % (nome, sentinela))
                if obj.get("fonte") not in fontes:
                    falha(onde, "`%s` = %r aponta a fonte %r, que nao esta em fontes{}. A sentinela "
                                "dispensa o literal, nunca o registro de ONDE se olhou"
                          % (nome, sentinela, obj.get("fonte")))
                continue
            if nome == "energia_wh":
                pass  # conferido abaixo, como derivado
            else:
                if obj.get("declarado_como") in (None, ""):
                    falha(onde, "`%s` tem valor e nao tem `declarado_como` (o texto LITERAL da fonte)" % nome)
                fid = obj.get("fonte")
                if fid not in fontes:
                    falha(onde, "`%s` aponta a fonte %r, que nao esta em fontes{}" % (nome, fid))
                else:
                    nivel = fontes[fid].get("nivel")
                    if nivel == 8:
                        falha(onde, "`%s` se sustenta em fonte de nivel 8 (fazenda ou catalogo comercial), "
                                    "que nao sustenta campo nenhum" % nome)
                    piso = piso_por_campo.get(nome)
                    if piso is not None and isinstance(nivel, int) and nivel > piso:
                        falha(onde, "`%s` vem de fonte nivel %s e o pior nivel aceito neste campo e %s "
                                    "(escada_de_fontes.niveis_minimos_por_campo)" % (nome, nivel, piso))
                if nome in campos_com_leitura:
                    dp = obj.get("declarada_por")
                    if dp not in origens_leitura:
                        falha(onde, "`%s` tem valor e `declarada_por` %r nao e uma das origens legitimas "
                                    "de leitura %s (secao 26.1)" % (nome, dp, sorted(origens_leitura)))

        # energia_wh: DERIVADA de V x Ah
        tv = (v.get("tensao_v") or {}).get("valor")
        ah = (v.get("amperagem_ah") or {}).get("valor")
        wh = (v.get("energia_wh") or {}).get("valor")
        if tv is not None and ah is not None:
            esperado = round(tv * ah)
            if wh is None:
                falha(onde, "tem tensao e amperagem e `energia_wh` esta null. Wh = V x Ah e identidade, "
                            "nao fonte: com os dois lados preenchidos o derivado existe (%s Wh)" % esperado)
            elif round(wh) != esperado:
                falha(onde, "`energia_wh` %r nao e V x Ah (%s x %s = %s). O campo guarda o DERIVADO; Wh "
                            "declarado em desacordo vai para divergencias[], nunca para ca, e nunca a media"
                      % (wh, tv, ah, esperado))
            elif not (v.get("energia_wh") or {}).get("derivado_de"):
                falha(onde, "`energia_wh` sem `derivado_de`. Derivado que nao se declara derivado passa a "
                            "ser lido como digitado na primeira releitura")
        elif wh is not None:
            falha(onde, "`energia_wh` tem valor (%r) sem tensao e amperagem dos dois lados. Wh copiado de "
                        "anuncio e exatamente o que o esquema proibe" % wh)

        # categoria
        if "categoria" not in v:
            falha(onde, "a chave `categoria` esta ausente")
        elif categoria_travada and v.get("categoria") is not None:
            falha(onde, "`categoria` = %r com a constante `limiares-categoria-contran-996-2023` em %r. "
                        "A 1.3 da especificacao proibe a F1 de ir ao ar com numero de portal, e gravar "
                        "categoria a mao e o anuncio escrevendo a regra"
                  % (v.get("categoria"), st_limiar))
        elif v.get("categoria") is not None and v.get("categoria") not in enum_categoria:
            falha(onde, "`categoria` %r fora do enum" % v.get("categoria"))
        if categoria_travada and v.get("categoria") is None and not v.get("motivo_categoria_null"):
            falha(onde, "`categoria` null sem `motivo_categoria_null`")

        # estado
        if v.get("status") not in enum_status:
            falha(onde, "`status` %r fora do enum" % v.get("status"))
        if not v.get("motivo_do_status"):
            falha(onde, "`motivo_do_status` vazio — ele e escrito inclusive em `publicavel`")
        if v.get("status") == "excluido_do_banco" and not v.get("excluido_do_banco_por_que"):
            falha(onde, "`excluido_do_banco` sem `excluido_do_banco_por_que`. Recusa que nao se escreve e "
                        "recusa que a proxima coleta repete")

        # conteudo
        for lista in ("divergencias", "afirmacao_do_vendedor", "alteracao_pos_compra", "cotacoes"):
            if not isinstance(v.get(lista), list):
                falha(onde, "`%s` nao e lista. Lista vazia e AFIRMACAO; chave ausente e silencio" % lista)
        for d in v.get("divergencias") or []:
            if not d.get("resolucao"):
                falha(onde, "divergencia em `%s` sem `resolucao` escrita. Divergencia sem resolucao e a "
                            "ilha empurrando a duvida para o visitante" % d.get("campo"))
        for c in v.get("cotacoes") or []:
            if not c.get("data_leitura"):
                falha(onde, "cotacao sem `data_leitura`. Preco sem a data da leitura e proibido")
            if not isinstance(c.get("valor_brl"), (int, float)):
                falha(onde, "cotacao com `valor_brl` %r" % c.get("valor_brl"))
            if c.get("fonte") not in fontes:
                falha(onde, "cotacao aponta a fonte %r, que nao esta em fontes{}" % c.get("fonte"))

        # afiliado e os derivados da escada de compra
        af = v.get("afiliado") or {}
        for ch in ("programa", "degrau", "url", "url_produto", "url_busca", "url_busca_produto",
                   "encurtamento_tentado_em"):
            if ch not in af:
                falha(onde, "`afiliado.%s` ausente" % ch)
        piso = bool(af.get("url_busca")) and bool(af.get("url_busca_produto"))
        intestavel = bool(af.get("url")) and not af.get("url_produto")
        v["_piso"] = piso
        if af.get("url") and af.get("url_produto") and not af.get("par_colhido_em"):
            falha(onde, "tem `url` e `url_produto` e nao tem `par_colhido_em`. Os dois vem da MESMA oferta "
                        "na MESMA chamada, ou nenhum entra (25.4-b.1)")
        if af.get("degrau") == 4 and af.get("url"):
            falha(onde, "degrau 4 com `url` preenchida. No degrau 4 a busca sobe e vira o botao pela "
                        "escada da casca, nao pela ficha")
        if af.get("degrau") in (1, 2, 3) and af.get("url") and not af.get("url_produto"):
            falha(onde, "degrau %s com `url` e sem `url_produto`: link cuja saude e desconhecida e "
                        "permanecera desconhecida (25.4-b)" % af.get("degrau"))
        for mot in ("motivo_sem_url_produto", "motivo_sem_url_busca"):
            texto = af.get(mot)
            if texto and "||" not in texto:
                falha(onde, "`afiliado.%s` nao separa CAUSA de ULTIMA TENTATIVA pelo marcador `||`. "
                            "Motivo velho manda a execucao seguinte nem tentar (25.4-b.3)" % mot)
        if v.get("status") == "publicavel":
            if not piso:
                falha(onde, "`publicavel` sem piso de compra (`url_busca` e `url_busca_produto`). "
                            "Nao existe item publicavel sem piso (25.2)")
            if not af.get("encurtamento_tentado_em"):
                falha(onde, "`publicavel` sem `encurtamento_tentado_em`. AUSENTE e diferente de "
                            "tentado-e-falhou, e essa distincao e a regra inteira (25.2-b)")
            if intestavel and af.get("degrau") != 4:
                falha(onde, "`publicavel` e intestavel fora do degrau 4")

        if "imagem" not in v:
            falha(onde, "a chave `imagem` esta ausente. Imagem ausente nao elimina o registro, mas a "
                        "chave e declarada")

    # ---- 4. prestacao de contas: os grupos tem de ser EXAUSTIVOS e EXCLUSIVOS
    for nome, fn in (("F1", grupos_f1), ("F2", grupos_f2), ("F3", grupos_f3)):
        for v in regs:
            g = fn(v)
            if len(g) != 1:
                falha("prestacao de contas %s / %s" % (nome, v.get("id")),
                      "caiu em %d grupos (%s). A secao 7 exige que todo item seja nomeado EXATAMENTE "
                      "uma vez" % (len(g), g))

    # ---- 5. PECA
    vistos = set()
    for p in dados["pecas"].get("registros", []):
        onde = "peca %s" % p.get("id")
        if not _slug(p.get("id")):
            falha(onde, "`id` nao e slug")
        if p.get("id") in vistos:
            falha(onde, "`id` repetido")
        vistos.add(p.get("id"))
        if p.get("tipo") not in enum_tipo_peca:
            falha(onde, "`tipo` %r fora do vocabulario da ilha %s" % (p.get("tipo"), sorted(enum_tipo_peca)))
        if not p.get("titulo_colhido"):
            falha(onde, "`titulo_colhido` vazio")
        if p.get("status") not in enum_status:
            falha(onde, "`status` %r fora do enum" % p.get("status"))
        if not p.get("motivo_do_status"):
            falha(onde, "`motivo_do_status` vazio")
        comp = p.get("compatibilidade")
        if not isinstance(comp, dict):
            falha(onde, "sem `compatibilidade{}`")
        else:
            chave = comp.get("chave")
            esperada = chave_por_tipo_peca.get(p.get("tipo"), "")
            if chave is None and not comp.get("motivo"):
                falha(onde, "`compatibilidade.chave` null sem `motivo`. Compatibilidade nao se deduz, e "
                            "a ausencia dela e dado")
            if chave and chave != "nenhuma":
                if comp.get("valor") in (None, ""):
                    falha(onde, "`compatibilidade.chave` = %r e `valor` vazio" % chave)
                if comp.get("declarada_por") not in origens_leitura:
                    falha(onde, "compatibilidade declarada por %r, fora das origens legitimas de leitura"
                          % comp.get("declarada_por"))
                if comp.get("declarado_como") in (None, ""):
                    falha(onde, "compatibilidade com valor e sem `declarado_como` literal")
            if chave == "nenhuma" and "nenhuma" not in str(esperada):
                falha(onde, "`chave: nenhuma` num tipo cuja chave de encaixe no esquema e %r" % esperada)
        for c in p.get("cotacoes") or []:
            if not c.get("data_leitura"):
                falha(onde, "cotacao sem `data_leitura`")

    # ---- 6. MUNICIPIO
    enum_mun = set(esq["entidades"]["MUNICIPIO"]["campos"]["status"]["valores"])
    for m in dados["municipios"].get("registros", []):
        onde = "municipio %s" % m.get("id")
        if not _slug(m.get("id")):
            falha(onde, "`id` nao e slug")
        if m.get("status") not in enum_mun:
            falha(onde, "`status` %r fora do enum" % m.get("status"))
        if not m.get("motivo_do_status"):
            falha(onde, "`motivo_do_status` vazio")
        fontes = m.get("fontes") or {}
        if not fontes:
            falha(onde, "sem `fontes{}`")
        if m.get("status") == "publicavel":
            niveis = [f.get("nivel") for f in fontes.values()]
            if not any(isinstance(n, int) and n <= 3 for n in niveis):
                falha(onde, "`publicavel` sem fonte de nivel 3 ou melhor (ato lido no dominio .gov.br do "
                            "municipio). Materia sobre o ato nao e o ato")
        if m.get("limite_velocidade_kmh") is None and m.get("limite_potencia_w") is None \
           and m.get("status") == "publicavel":
            falha(onde, "`publicavel` sem nenhum dos dois limites. Municipio sem limite nao e camada 2")

    # ---- 7. contagem, SAINDO DO BANCO e nunca digitada
    pub = [v for v in regs if v.get("status") == "publicavel"]
    cont["veiculos"] = len(regs)
    cont["veiculos_publicaveis"] = len(pub)
    cont["veiculos_excluidos"] = sum(1 for v in regs if v.get("status") == "excluido_do_banco")
    cont["veiculos_com_piso_de_compra"] = sum(1 for v in regs if v.get("_piso"))
    cont["veiculos_com_nominal_declarado"] = sum(
        1 for v in regs if (v.get("potencia_nominal_w") or {}).get("valor") is not None)
    cont["veiculos_com_watt_sem_rotulo"] = sum(
        1 for v in regs if (v.get("potencia_declarada_sem_rotulo_w") or {}).get("valor") is not None)
    cont["veiculos_com_wh_derivado"] = sum(
        1 for v in regs if (v.get("energia_wh") or {}).get("valor") is not None)
    cont["veiculos_com_carga_max"] = sum(
        1 for v in regs if (v.get("carga_max_kg") or {}).get("valor") is not None)
    cont["veiculos_com_categoria"] = sum(1 for v in regs if v.get("categoria") is not None)
    cont["veiculos_publicaveis_com_tensao_e_amperagem"] = sum(
        1 for v in pub if (v.get("tensao_v") or {}).get("valor") is not None
        and (v.get("amperagem_ah") or {}).get("valor") is not None)
    cont["veiculos_publicaveis_com_carga_max"] = sum(
        1 for v in pub if (v.get("carga_max_kg") or {}).get("valor") is not None)
    cont["pecas"] = len(dados["pecas"].get("registros", []))
    cont["municipios"] = len(dados["municipios"].get("registros", []))
    cont["municipios_publicaveis"] = sum(
        1 for m in dados["municipios"].get("registros", []) if m.get("status") == "publicavel")

    # ---- 8. avisos: o banco esta certo e incompleto, e o numero e registro, nao aprovacao
    if cont["veiculos_publicaveis"] == 0:
        avisos.append("ZERO veiculo publicavel, e a prestacao de contas das tres ferramentas e portanto "
                      "VERDADEIRA POR VACUIDADE. Isto e REGISTRO e nao aprovacao: a regra da secao 7 so "
                      "sera exercitada quando o primeiro registro ganhar piso de compra. A causa do zero "
                      "esta em cada `motivo_do_status`, e e uma so: ninguem tem saida de compra ainda.")
    if cont["veiculos_publicaveis"] and not (cont["veiculos_publicaveis_com_tensao_e_amperagem"]
                                             or cont["veiculos_publicaveis_com_carga_max"]):
        avisos.append(
            "O PISO E O DADO TECNICO CAIRAM EM REGISTROS DIFERENTES, E A INTERSECAO E VAZIA: dos %d "
            "veiculos publicaveis, ZERO declara tensao+amperagem (entrada da F2) e ZERO declara carga "
            "maxima (entrada da F3), enquanto %d registro(s) com Wh derivado e %d com carga maxima estao "
            "entre os que NAO tem saida de compra. Nao e coincidencia e nao se conserta com mais link: o "
            "anuncio que nomeia MARCA e MODELO e achavel na loja e nao publica ficha; o que publica 60 V "
            "20 Ah ou 120 kg empacota tres nomes no titulo e nao e achavel por nome nenhum. CONSEQUENCIA "
            "PARA QUEM FOR CONSTRUIR A CASCA: o bloco de compra da 32.1 pede o produto QUE A FERRAMENTA "
            "ESCOLHEU, e hoje nenhuma das tres escolhe um publicavel. O que destrava nao e piso: e o "
            "casamento do registro com a oferta (degraus 1 a 3 da 25.1), que traz a ficha e, com ela, o "
            "campo tecnico."
            % (cont["veiculos_publicaveis"], cont["veiculos_com_wh_derivado"],
               cont["veiculos_com_carga_max"]))
    if cont["veiculos_com_nominal_declarado"] == 0:
        avisos.append("ZERO veiculo com `potencia_nominal_w` declarada, contra %d com um watt SEM ROTULO. "
                      "Nao e lacuna de coleta: e a medicao da tese da ilha. Enquanto for zero, a F1 nao "
                      "tem candidato nenhum na vitrine, nem com os limiares na mao."
                      % cont["veiculos_com_watt_sem_rotulo"])
    if cont["municipios_publicaveis"] == 0:
        avisos.append("ZERO municipio publicavel: a camada 2 da F1 tem HOJE duas saidas iguais em vez de "
                      "tres (1.1 da especificacao).")
    if st_limiar != "publicavel":
        avisos.append("`limiares-categoria-contran-996-2023` em %r: `categoria` e null em todo registro "
                      "por forca do esquema, e a F1 nao vai ao ar." % st_limiar)
    return falhas, avisos, cont


def main():
    raiz = Path(__file__).resolve().parent.parent
    dados = carregar(raiz)
    falhas, avisos, cont = validar(dados)
    if "--json" in sys.argv:
        print(json.dumps({"falhas": falhas, "avisos": avisos, "contagem": cont},
                         ensure_ascii=False, indent=1))
        return 1 if falhas else 0
    print("VALIDADOR DO BANCO — RODAMETRIA (esquema versao %s)" % dados["esquema"]["versao_esquema"])
    print("")
    for k in sorted(cont):
        print("  %-34s %s" % (k, cont[k]))
    print("")
    for a in avisos:
        print("AVISO: %s" % a)
    if avisos:
        print("")
    for f in falhas:
        print("FALHA %s" % f)
    print("")
    print("%d falha(s)." % len(falhas))
    print("APROVADO" if not falhas else "REPROVADO")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
