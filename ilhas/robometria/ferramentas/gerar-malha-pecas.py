#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o combustivel da MALHA DE PECAS (bloco 5b) a partir do banco commitado.

    python3 ferramentas/gerar-malha-pecas.py            # relatorio na tela
    python3 ferramentas/gerar-malha-pecas.py --gravar   # grava os dois arquivos

Grava:
  dados/malha-pecas.json             FATOS, sem prosa. O Sync leva para a option
                                     robometria_dados_malha-pecas e o snippet
                                     robometria-malha.php monta as frases a
                                     partir dele. publicar=true no manifest.
  dados/malha-pecas-referencia.json  GABARITO: as mesmas frases ja escritas, em
                                     ASCII, pela implementacao de REFERENCIA que
                                     e este arquivo. publicar=false — existe para
                                     ferramentas/teste-malha.php comparar, pagina
                                     a pagina, o que o PHP escreve com o que a
                                     referencia escreve, ignorando acento.

POR QUE ASSIM, e nao escrevendo as regras dentro do snippet.

E a decisao 2 do bloco 4 do PROMPT.md desta ilha, que a R1 e os dois artigos ja
seguem: a regra mora na implementacao de referencia e o PHP so escreve a frase,
acentuada. Regra escrita em PHP e regra que so da para conferir com o site no ar.

O QUE ESTE ARQUIVO CONTA, E POR QUE CONTAR E O TRABALHO.

A ordem de levas do ARVORE.md manda abrir /pecas/ + /pecas/filtros/ com TRES
filhas, e ate 21/09/2026 ninguem tinha contado se o banco as sustentava — a 16.5
e regra de documento, e nenhuma regua desta ilha conta filha de categoria que
ainda nao existe. Este gerador conta, e conta a grade INTEIRA (todo tipo de peca
x toda marca), nao so a leva de hoje: assim a proxima categoria custa uma linha
no registro do snippet, e o cartao "em breve" da mae sai do mesmo lugar que o
cartao publicado.

DUAS COISAS QUE ELE FAZ DE PROPOSITO:

  1. KIT ENTREGA PECA. Um item entra na categoria de um tipo quando E daquele
     tipo (avulso) ou quando e um KIT cuja composicao declara aquele tipo. Sem
     isso a Electrolux teria UM filtro no banco e a categoria de filtros nasceria
     com duas filhas em vez de tres — e o que o leitor compra para trocar o
     filtro do ERB80 e, de fato, o kit.
  2. "NAO VENDE AVULSO" E AFIRMACAO SOBRE O CATALOGO INTEIRO DO MODELO, e por
     isso e calculada por MODELO e nunca por item: so vale onde nenhuma peca
     avulsa daquele tipo responde por aquele modelo. E a mesma cicatriz que a
     R1 registrou em 12/09/2026, quando a pagina dizia "a Electrolux declara o
     filtro compativel com o ERB60" e, na frase seguinte, "a Electrolux nao
     vende o filtro avulso para este modelo" — as duas na mesma tela.
"""

import importlib.util
import json
import os
import sys
import unicodedata

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = os.path.join(BASE, "dados")


def _carregar_referencia():
    caminho = os.path.join(BASE, "ferramentas", "cobertura-r1.py")
    spec = importlib.util.spec_from_file_location("cobertura_r1", caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


ref = _carregar_referencia()

# A CATEGORIA DE NIVEL 2 DE CADA TIPO DE PECA. O slug e o do ARVORE.md, secao 1;
# o rotulo e o que a pessoa digita (VOZ.md: filtro, escova, mop, bateria).
#
# Esta lista NAO decide o que esta publicado — quem decide e o registro do
# snippet, porque publicar e URL nova e URL nova obedece ao teto da 21.4. Aqui
# ela decide apenas o que e CONTADO, e contar tudo e o que faz o cartao "em
# breve" da mae sair do mesmo lugar que o cartao publicado.
CATEGORIAS = [
    {"slug": "pecas-filtros", "caminho": "pecas/filtros", "tipo": "filtro",
     "rotulo": "Filtros", "plural": "filtros", "singular": "filtro"},
    {"slug": "pecas-escovas-laterais", "caminho": "pecas/escovas-laterais",
     "tipo": "escova lateral", "rotulo": "Escovas laterais",
     "plural": "escovas laterais", "singular": "escova lateral"},
    {"slug": "pecas-escovas-principais", "caminho": "pecas/escovas-principais",
     "tipo": "escova principal", "rotulo": "Escovas principais",
     "plural": "escovas principais", "singular": "escova principal"},
    {"slug": "pecas-mops", "caminho": "pecas/mops", "tipo": "mop",
     "rotulo": "Mops", "plural": "mops", "singular": "mop"},
    {"slug": "pecas-baterias", "caminho": "pecas/baterias", "tipo": "bateria",
     "rotulo": "Baterias", "plural": "baterias", "singular": "bateria"},
]

def sem_acento(t):
    return "".join(c for c in unicodedata.normalize("NFD", t)
                   if unicodedata.category(c) != "Mn")


def publicavel(registro):
    return registro.get("status") == "publicavel"


def entrega_o_tipo(peca, tipo):
    """'avulso', 'kit' ou None — como este item entrega aquele tipo de peca."""
    if peca["tipo"] == tipo:
        return "avulso"
    if peca["tipo"] == "kit":
        for c in peca.get("composicao") or []:
            if c.get("tipo") == tipo:
                return "kit"
    return None


def modelos_publicaveis_do_par(peca):
    """Os modelos publicaveis que este item responde, na ordem do banco.

    Par que aponta para modelo fora do banco NAO conta: a tela nunca o serve, e
    contar o que a tela nao mostra foi como esta ilha publicou '33 pares' com 32
    na mao (casca 1.2.0)."""
    saida = []
    for c in peca["compatibilidade"]:
        modelo = ref.modelos.get(c["modelo"])
        if modelo and publicavel(modelo) and c["modelo"] not in saida:
            saida.append(c["modelo"])
    return saida


def rotulo_do_modelo(modelo_id):
    m = ref.modelos[modelo_id]
    return "%s %s" % (ref.marcas[m["marca"]]["nome"], m["codigo_fabricante"])


def rotulo_curto_do_modelo(modelo_id):
    """So o codigo do modelo, sem a marca.

    A pagina de uma MARCA ja disse a marca no titulo, no H1 e na trilha; repeti-la
    em cada item ("a Xiaomi declara esta peca para Xiaomi E10, Xiaomi E10C e
    Xiaomi S20") e ruido que empurra o codigo — que e o que a pessoa confere na
    etiqueta embaixo do robo — para o fim da linha. Na tabela da CATEGORIA, que
    mistura marcas, vale o rotulo inteiro."""
    return ref.modelos[modelo_id]["codigo_fabricante"]


def fonte_do_item(peca):
    """A fonte do PRIMEIRO par publicavel do item — a mesma que a R1 cita.

    Um item pode ter mais de uma fonte (uma por par). A pagina de categoria fala
    do ITEM, entao cita a fonte da declaracao que o trouxe para ca, e o link
    leva o leitor ao documento do fabricante."""
    for c in peca["compatibilidade"]:
        modelo = ref.modelos.get(c["modelo"])
        if modelo and publicavel(modelo):
            return peca["fontes"][c["fonte"]]
    return list(peca["fontes"].values())[0]


def foto_de(imagem):
    """A imagem reduzida ao que a TELA usa — os mesmos quatro campos da R1."""
    imagem = imagem or {}
    if not imagem.get("url"):
        return None
    return {
        "url": imagem["url"],
        "largura": imagem.get("largura"),
        "altura": imagem.get("altura"),
        "alt": imagem.get("alt") or "",
    }


def afiliado_do(peca):
    """A oferta do item, na forma que robometria_casca_porta_de_compra() le.

    `sub_id_2` carimba a PAGINA que levou o clique, e quem carimba e o gerador —
    nunca o banco, que so sabe dizer um valor por registro (cicatriz de
    12/09/2026, quando o A1 e o A2 publicavam cliques como se fossem das
    ferramentas)."""
    a = peca.get("afiliado") or {}
    return {
        "url": a.get("url") or "",
        "url_busca": a.get("url_busca") or "",
        "url_busca_cru": a.get("url_busca_produto") or "",
        "programa": a.get("plataforma") or None,
        "sub_id_1": "robometria",
        "sub_id_2": "M-PECAS",
    }


def item_da_categoria(peca, tipo, avulsos_por_modelo):
    entrega = entrega_o_tipo(peca, tipo)
    modelos = modelos_publicaveis_do_par(peca)
    fonte = fonte_do_item(peca)
    vida = peca.get("vida_util_declarada") or {}
    return {
        "peca": peca["id"],
        "marca": peca["marca"],
        "codigo": peca.get("codigo_fabricante"),
        "nome_na_fonte": peca["nome_na_fonte"],
        "entrega": entrega,
        "dentro_de_kit": entrega == "kit",
        "modelos": [{"id": m, "rotulo": rotulo_do_modelo(m),
                     "rotulo_curto": rotulo_curto_do_modelo(m)} for m in modelos],
        # SO POR KIT: os modelos deste item que nenhuma peca AVULSA daquele tipo
        # responde. E o que autoriza a frase "nao vende avulso", e ela e sobre o
        # catalogo do modelo, nunca sobre o item.
        "modelos_so_por_kit": [
            {"id": m, "rotulo": rotulo_do_modelo(m),
             "rotulo_curto": rotulo_curto_do_modelo(m)}
            for m in modelos if entrega == "kit" and m not in avulsos_por_modelo
        ],
        "publicador": fonte.get("publicador") or ref.marcas[peca["marca"]]["nome"],
        "origem": fonte.get("origem"),
        "nivel_da_fonte": fonte.get("nivel"),
        "url": fonte.get("url"),
        "verificado_em": fonte.get("verificado_em"),
        "vida_util": ({"valor": vida.get("valor"), "unidade": vida.get("unidade")}
                      if vida.get("valor") is not None else None),
        "imagem": foto_de(peca.get("imagem")),
        "afiliado": afiliado_do(peca),
        "divergencia": bool(peca.get("divergencias")),
    }


def frases_da_filha(f, categoria):
    """As frases da pagina de uma marca dentro de uma categoria, em ASCII.

    DUAS FRASES CURTAS EM VEZ DE UMA LONGA, e a escolha e do VOZ.md: "frases
    curtas, verbo na frente". Alem da voz, ela paga o preco desta camada — o PHP
    tem de escrever a MESMA frase, acentuada, e molde longo e molde que as duas
    implementacoes divergem sem ninguem ver.

    TODO NUMERO SAI EM DIGITO, nunca por extenso. O DESIGN.md manda todo numero
    para a Mono com tabular-nums, e numero por extenso nao chega la — sairia em
    texto corrido no meio de uma linha que o resto da pagina escreve em digito.
    """
    marca = f["marca_rotulo"]
    plural = categoria["plural"]
    singular = categoria["singular"]
    n = f["itens_no_banco"]
    cobertos = f["modelos_cobertos"]
    total = f["modelos_publicaveis_da_marca"]

    # KIT NAO E FILTRO, e a frase nao pode chama-lo assim. Onde ha kit no meio,
    # o sujeito e "itens que entregam <tipo>" e a composicao sai escrita — dizer
    # "6 filtros Electrolux" seria publicar como peca avulsa uma coisa que o
    # leitor so consegue comprar dentro de um kit.
    if f["itens_em_kit"] > 0:
        quantos = ("Sao %d itens %s que entregam %s: %s e %s que %s %s na "
                   "composicao." % (n, marca, singular,
                                    frase_de_avulsos(f["itens_avulsos"], singular,
                                                     plural, categoria["tipo"]),
                                    frase_de_kits(f["itens_em_kit"]),
                                    "declaram" if f["itens_em_kit"] > 1 else "declara",
                                    singular))
    elif n > 1:
        quantos = "Sao %d %s %s no banco." % (n, plural, marca)
    else:
        quantos = "E 1 %s %s no banco." % (singular, marca)

    tipo = categoria["tipo"]
    g = gramatica_do_tipo(tipo)
    if f["itens_em_kit"] > 0:
        # O sujeito e "itens", masculino, mesmo numa categoria feminina.
        sujeito = "Eles servem" if n > 1 else "Ele serve"
    else:
        sujeito = ("%s servem" % g["sujeito_plural"]) if n > 1 else (
            "%s serve" % g["sujeito_singular"])
    if cobertos == total:
        serve = ("%s em todos os %d modelos %s que a gente acompanha."
                 % (sujeito, total, marca))
    else:
        serve = ("%s em %d dos %d modelos %s que a gente acompanha."
                 % (sujeito, cobertos, total, marca))

    faltam = total - cobertos
    if faltam > 1:
        residuo = ("Nos outros %d modelos nao localizamos declaracao do fabricante "
                   "de %s; nao vamos supor." % (faltam, singular))
    elif faltam == 1:
        residuo = ("No outro modelo nao localizamos declaracao do fabricante de %s; "
                   "nao vamos supor." % singular)
    else:
        residuo = ""

    so_kit = len(f["modelos_so_por_kit"])
    if so_kit > 1:
        kit = ("Em %d desses modelos o %s so vem dentro do kit: %s nao vende o %s "
               "avulso para eles." % (so_kit, singular, f["gramatica_do_publicador"],
                                      singular))
    elif so_kit == 1:
        kit = ("Em 1 desses modelos o %s so vem dentro do kit: %s nao vende o %s "
               "avulso para ele." % (singular, f["gramatica_do_publicador"], singular))
    else:
        kit = ""

    if f["itens_que_atravessam_marca"] == 0:
        marca_cruzada = ("%s %s %s serve em robo de outra marca, pelo que o "
                         "fabricante declara." % (g["nenhum"], g["desses"], plural))
    else:
        marca_cruzada = ("%d desses %s servem tambem em robo de outra marca, pelo que "
                         "o fabricante declara." % (f["itens_que_atravessam_marca"], plural))

    cobertura = ("%d de %d modelos %s do banco tem %s %s pelo fabricante."
                 % (cobertos, total, marca, singular, g["declarado"]))

    return {"quantos": quantos, "serve": serve, "residuo": residuo, "kit": kit,
            "marca_cruzada": marca_cruzada, "cobertura": cobertura}


def genero_do(tipo):
    """('o'|'a', 'avulso'|'avulsa') — LIDO da implementacao de referencia.

    A tabela e a mesma que a R1 usa para escrever "a escova lateral avulsa"; ter
    uma copia dela aqui seria combinar de divergir depois, e concordancia de
    genero ja custou a esta ilha uma frase no ar ("as dois declaracoes", R1
    1.11.1, no mesmo dia deste bloco)."""
    return ref.GENERO_DO_TIPO[tipo]


def frase_de_avulsos(n, singular, plural, tipo):
    _artigo, avulso = genero_do(tipo)
    if n == 1:
        return "1 %s %s" % (singular, avulso)
    return "%d %s %ss" % (n, plural, avulso)


def frase_de_kits(n):
    if n == 1:
        return "1 kit"
    return "%d kits" % n


def gramatica_do_tipo(tipo):
    """A GRAMATICA DO TIPO VIAJA COMO FATO, e nao como tabela dentro do snippet.

    E a mesma decisao que a R1 tomou em 14/09/2026 para o publicador: o PHP nao
    pode carregar tabela de lingua propria, porque ai sao duas tabelas para a
    mesma lingua e elas divergem no dia em que um tipo novo entra. Aqui sai o
    punhado de palavras que os moldes precisam flexionar, ja escolhidas."""
    artigo, avulso = genero_do(tipo)
    feminino = ("a" == artigo)
    return {
        "artigo": artigo,
        "avulso": avulso,
        "avulsos": avulso + "s",
        "sujeito_plural": "Elas" if feminino else "Eles",
        "sujeito_singular": "Ela" if feminino else "Ele",
        "nenhum": "Nenhuma" if feminino else "Nenhum",
        "deles": "delas" if feminino else "deles",
        "desses": "dessas" if feminino else "desses",
        "declarado": "declarada" if feminino else "declarado",
        "juntos": "Juntas" if feminino else "Juntos",
        "eles": "elas" if feminino else "eles",
        "outros": "outras" if feminino else "outros",
    }


def frases_da_categoria(c):
    """As frases de uma categoria de nivel 2.

    NAO HA FRASE DIZENDO QUAIS MARCAS TEM PAGINA PROPRIA, e a ausencia e
    escolha: quem sabe o que esta publicado e o registro do snippet, nao este
    arquivo — e frase derivada de um estado que o gerador nao enxerga nasce
    falsa na primeira leva seguinte. As filhas publicadas aparecem como o que
    sao, links, no bloco de cartoes que o 16.4(a) exige.
    """
    plural = c["plural"]
    singular = c["singular"]
    avulsos = sum(f["itens_avulsos"] for f in c["filhas"])
    em_kit = sum(f["itens_em_kit"] for f in c["filhas"])

    marcas = ("%d marcas" % c["marcas_no_banco"]) if c["marcas_no_banco"] > 1 else "1 marca"
    modelos = (("%d modelos de robo" % c["modelos_cobertos"])
               if c["modelos_cobertos"] > 1 else "1 modelo de robo")
    g = gramatica_do_tipo(c["tipo"])

    if em_kit > 0:
        quantos = ("Sao %d itens de reposicao que entregam %s em %s: %s e %s "
                   "que declaram %s na composicao."
                   % (c["itens_no_banco"], singular, marcas,
                      frase_de_avulsos(avulsos, singular, plural, c["tipo"]),
                      frase_de_kits(em_kit), singular))
        sujeito = "Juntos, eles servem"
    else:
        quantos = ("Sao %d %s de %s no banco."
                   % (c["itens_no_banco"], plural, marcas))
        sujeito = "%s, %s servem" % (g["juntos"], g["eles"])

    serve = "%s em %s." % (sujeito, modelos)

    if c["itens_que_atravessam_marca"] == 0:
        cruz = ("%s %s serve em mais de uma marca: %s de robo aspirador nao e "
                "universal, e o encaixe e por modelo." % (g["nenhum"], g["deles"], singular))
    else:
        cruz = ("%d %s servem em mais de uma marca; %s %s %d sao de uma marca so."
                % (c["itens_que_atravessam_marca"], g["deles"],
                   "as" if "a" == g["artigo"] else "os", g["outros"],
                   c["itens_no_banco"] - c["itens_que_atravessam_marca"]))
    return {"quantos": quantos, "serve": serve, "marca_cruzada": cruz}


def frases_da_secao(s, numeros):
    """As frases de /pecas/.

    OS TRES NUMEROS DA RESPOSTA NAO SAO CONTADOS AQUI: sao lidos de
    dados/casca-fatos.json, que ja os deriva do mesmo banco com a regua escrita
    ao lado de cada um. Contar de novo criaria uma segunda copia de
    `pares_declarados` com o mesmo nome e outra conta — que e, palavra por
    palavra, o defeito que a R1 1.8.0 mediu no ar ("63 pares" no alto e "73
    pares" duas telas abaixo, os dois certos, contando coisas diferentes com o
    mesmo nome). Quem mudar a regua muda um lugar so.
    """
    resposta = ("O banco tem %d pecas publicaveis de %d marcas e %d pares peca x "
                "modelo, todos declarados pelo fabricante." %
                (numeros["pecas_publicaveis"], numeros["marcas"],
                 numeros["pares_declarados"]))
    tipos = ("Sao %d tipos de peca no banco: %s." %
             (len(s["tipos"]), listar([t["rotulo_singular"] for t in s["tipos"]])))
    return {"resposta": resposta, "tipos": tipos}


def listar(itens):
    """a, b e c — a virgula serial nao existe em portugues."""
    itens = list(itens)
    if not itens:
        return ""
    if len(itens) == 1:
        return itens[0]
    return "%s e %s" % (", ".join(itens[:-1]), itens[-1])


def numeros_da_casca():
    """Os numeros da ilha inteira, lidos de dados/casca-fatos.json.

    FALHA ALTO quando o arquivo nao esta la ou nao tem as chaves: a alternativa
    seria recontar aqui, e recontar e exatamente o que este arquivo nao pode
    fazer sem criar uma segunda copia do mesmo numero."""
    fatos = ref.carregar("casca-fatos.json")
    medicao = fatos.get("medicao") or {}
    faltando = [c for c in ("pecas_publicaveis", "marcas", "pares_declarados")
                if not isinstance(medicao.get(c), int)]
    if faltando:
        sys.stderr.write(
            "ERRO: dados/casca-fatos.json nao tem %s. Rode "
            "ferramentas/gerar-casca-fatos.py --gravar antes deste.\n"
            % ", ".join(faltando))
        sys.exit(1)
    return medicao


def gramatica_do(publicador):
    """'a WAP (loja oficial)' — o artigo sai de publicadores.json, nunca digitado
    no molde. Mesma razao da R1: o snippet nao carrega tabela de lingua."""
    for p in ref.carregar("publicadores.json")["registros"]:
        if p["nome"] == publicador:
            return "%s %s" % (p.get("artigo", "a"), publicador)
    return "a %s" % publicador


def montar():
    pecas_pub = [p for p in ref.pecas if publicavel(p)]
    modelos_pub = [m for m in ref.modelos.values() if publicavel(m)]

    categorias = []
    for cat in CATEGORIAS:
        tipo = cat["tipo"]

        # Quais modelos tem AVULSO daquele tipo — a base do "nao vende avulso".
        avulsos_por_modelo = set()
        for p in pecas_pub:
            if entrega_o_tipo(p, tipo) == "avulso":
                avulsos_por_modelo.update(modelos_publicaveis_do_par(p))

        por_marca = {}
        for p in pecas_pub:
            if not entrega_o_tipo(p, tipo):
                continue
            item = item_da_categoria(p, tipo, avulsos_por_modelo)
            if not item["modelos"]:
                # Item sem nenhum modelo publicavel nao entra: a pagina nao teria
                # o que dizer sobre ele, e "serve" sem modelo nao e resposta.
                continue
            por_marca.setdefault(p["marca"], []).append(item)

        filhas = []
        for marca_id, itens in sorted(por_marca.items(),
                                      key=lambda kv: (-len(kv[1]), kv[0])):
            cobertos = []
            so_kit = []
            for i in itens:
                for m in i["modelos"]:
                    if m["id"] not in [x["id"] for x in cobertos]:
                        cobertos.append(m)
                for m in i["modelos_so_por_kit"]:
                    if m["id"] not in [x["id"] for x in so_kit]:
                        so_kit.append(m)
            da_marca = [m for m in modelos_pub if m["marca"] == marca_id]
            sem_peca = [
                {"id": m["id"], "rotulo": rotulo_do_modelo(m["id"]),
                 "rotulo_curto": rotulo_curto_do_modelo(m["id"])}
                for m in da_marca if m["id"] not in [x["id"] for x in cobertos]
            ]
            atravessam = len([
                i for i in itens
                if len({ref.modelos[m["id"]]["marca"] for m in i["modelos"]}) > 1
            ])
            publicador = itens[0]["publicador"]
            filha = {
                "slug": "%s-%s" % (cat["slug"], marca_id),
                "caminho": "%s/%s" % (cat["caminho"], marca_id),
                "marca": marca_id,
                "marca_rotulo": ref.marcas[marca_id]["nome"],
                "tipo": tipo,
                "itens_no_banco": len(itens),
                "itens_avulsos": len([i for i in itens if i["entrega"] == "avulso"]),
                "itens_em_kit": len([i for i in itens if i["entrega"] == "kit"]),
                "modelos_cobertos": len(cobertos),
                "modelos": cobertos,
                "modelos_so_por_kit": so_kit,
                "modelos_publicaveis_da_marca": len(da_marca),
                "modelos_sem_a_peca": sem_peca,
                "itens_que_atravessam_marca": atravessam,
                "publicador": publicador,
                "gramatica_do_publicador": gramatica_do(publicador),
                "itens": itens,
                # PUBLICADA e escrito pelo registro do snippet, nao aqui: quem
                # decide URL nova e a leva, e a leva obedece ao teto da 21.4.
                "publicada": False,
            }
            filha["frases"] = frases_da_filha(filha, cat)
            filhas.append(filha)

        todos = [i for f in filhas for i in f["itens"]]
        modelos_da_cat = []
        for i in todos:
            for m in i["modelos"]:
                if m["id"] not in modelos_da_cat:
                    modelos_da_cat.append(m["id"])
        categoria = dict(cat)
        categoria.update({
            "gramatica": gramatica_do_tipo(cat["tipo"]),
            "itens_avulsos": sum(f["itens_avulsos"] for f in filhas),
            "itens_em_kit": sum(f["itens_em_kit"] for f in filhas),
            "itens_no_banco": len(todos),
            "marcas_no_banco": len(filhas),
            "modelos_cobertos": len(modelos_da_cat),
            "itens_que_atravessam_marca": sum(
                f["itens_que_atravessam_marca"] for f in filhas),
            "filhas": filhas,
            "publicada": False,
        })
        categoria["frases"] = frases_da_categoria(categoria)
        categorias.append(categoria)

    tipos = []
    for cat in categorias:
        tipos.append({
            "tipo": cat["tipo"],
            "categoria": cat["slug"],
            "rotulo": cat["rotulo"],
            "rotulo_singular": cat["singular"],
            "itens_no_banco": cat["itens_no_banco"],
            "marcas_no_banco": cat["marcas_no_banco"],
        })

    secao = {
        "slug": "pecas",
        "caminho": "pecas",
        # OS NUMEROS DA ILHA INTEIRA NAO MORAM AQUI — moram em casca-fatos.json,
        # e a pagina os pede a robometria_casca_numeros(). O que mora aqui e o
        # que so esta camada conta: os tipos de peca e as categorias.
        "chaves_da_resposta": ["pecas_publicaveis", "marcas", "pares_declarados"],
        "tipos": tipos,
    }
    secao["frases"] = frases_da_secao(secao, numeros_da_casca())

    return {
        "id": "malha-pecas",
        "ilha": "robometria",
        "entidade": "malha",
        "esquema": 1,
        "gerado_em": ref.doc_pecas["gerado_em"],
        "nota_de_procedencia": (
            "Todo numero deste arquivo e contado de dados/pecas.json e "
            "dados/modelos-robo.json pelo ferramentas/gerar-malha-pecas.py. "
            "Nada aqui e digitado."
        ),
        "secao": secao,
        "categorias": categorias,
    }


def referencia(fatos):
    """So as frases, em ASCII, para o teste-malha.php comparar com o PHP."""
    saida = {"secao": {"slug": "pecas", "frases": fatos["secao"]["frases"]},
             "categorias": {}, "filhas": {}}
    for c in fatos["categorias"]:
        saida["categorias"][c["slug"]] = c["frases"]
        for f in c["filhas"]:
            saida["filhas"][f["slug"]] = f["frases"]
    return saida


def relatorio(fatos):
    s = fatos["secao"]
    print("Robometria — malha de pecas (bloco 5b)\n")
    print("  /pecas/ .......... %s" % s["frases"]["resposta"])
    for c in fatos["categorias"]:
        print("\n  /%s/ — %d itens, %d marcas, %d modelos"
              % (c["caminho"], c["itens_no_banco"], c["marcas_no_banco"],
                 c["modelos_cobertos"]))
        porta = "ABRE (3 ou mais filhas com 3 ou mais itens)" if len(
            [f for f in c["filhas"] if f["itens_no_banco"] >= 3]) >= 3 else (
            "TRAVADA pelo portao de dado (16.5 + secao 13)")
        print("     portao: %s" % porta)
        for f in c["filhas"]:
            print("     %-12s %2d itens (%d avulso, %d em kit) · %2d de %2d modelos da marca"
                  % (f["marca"], f["itens_no_banco"], f["itens_avulsos"],
                     f["itens_em_kit"], f["modelos_cobertos"],
                     f["modelos_publicaveis_da_marca"]))


def main():
    fatos = montar()
    relatorio(fatos)
    if "--gravar" not in sys.argv:
        print("\n(sem --gravar: nada foi escrito)")
        return 0

    for nome, doc in (("malha-pecas.json", fatos),
                      ("malha-pecas-referencia.json", referencia(fatos))):
        caminho = os.path.join(DADOS, nome)
        with open(caminho, "w", encoding="utf-8") as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=1, sort_keys=False)
            fh.write("\n")
        print("\ngravado: dados/%s" % nome)
    return 0


if __name__ == "__main__":
    sys.exit(main())
