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
        if af.get("etiqueta_ml") and not af["etiqueta_ml"].startswith("clubedomosaico-"):
            erro("%s: etiqueta do Mercado Livre fora do formato clubedomosaico-<codigo>" % onde)

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

    # o cabecalho do arquivo declara numeros; eles tem que bater com a contagem
    dec_link = (arq.get("afiliado") or {}).get("itens_esperando_link")
    dec_img = (arq.get("imagens") or {}).get("itens_sem_imagem")
    conta_link = sum(1 for m in arq.get("materiais", []) if (m.get("afiliado") or {}).get("url") == "")
    conta_img = sum(1 for m in arq.get("materiais", []) if m.get("imagem") is None)
    if dec_link is not None and dec_link != conta_link:
        erro("%s: cabecalho declara %s itens esperando link, o arquivo tem %s" % (nome, dec_link, conta_link))
    if dec_img is not None and dec_img != conta_img:
        erro("%s: cabecalho declara %s itens sem imagem, o arquivo tem %s" % (nome, dec_img, conta_img))


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

tecnicas = carregar("tecnicas.json")
if tecnicas is None:
    nota("dados/tecnicas.json ainda nao existe: entidade TECNICA vazia.")
else:
    for t in tecnicas.get("tecnicas", []):
        onde = "tecnicas.json / %s" % t.get("id")
        if t.get("id") not in VOC["tecnica"]:
            erro("%s: id fora do vocabulario de tecnica" % onde)
        for campo in ("nome", "definicao", "consulta_alvo", "por_que_chega_ao_top_10", "fontes", "revisao_tecnica"):
            if not t.get(campo):
                erro("%s: falta %s" % (onde, campo))
        if t.get("revisao_tecnica") not in ("pendente", "revisada"):
            erro("%s: revisao_tecnica invalida" % onde)


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

if os.path.exists(os.path.join(DADOS, "pecas.json")):
    erro("dados/pecas.json existe. PECA NAO vive no repositorio: o catalogo da Loja e "
         "cadastrado pela artesa no painel /atelie/ e mora no CPT `peca` do WordPress. "
         "Peca inventada e a unica mentira que esta ilha pode contar sobre uma pessoa real.")


# ---------------------------------------------------------------- relatorio

print("Banco do Clube do Mosaico — verificacao do esquema do bloco 3")
print("  materiais no banco ......... %d" % len(materiais))
print("  celulas da F2 recomputadas . %d  (so categoria %s)" % (celulas_conferidas, CATEGORIA_DA_MATRIZ_F2))
print("  celulas do rejunte ......... %d" % celulas_rejunte_conferidas)
print("  itens esperando link ....... %d" % esperando_link)
print("  itens sem imagem ........... %d" % sem_imagem)
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
