# -*- coding: utf-8 -*-
"""Gera o catalogo de filtros que a C3 embute no snippet.

O site nao le o repositorio em tempo de execucao: o Sync copia o PHP e pronto.
Entao o banco de produtos precisa viajar DENTRO do snippet. Este script e o que
impede as duas copias de divergirem — depois de mexer em dados/produtos-filtro.json,
rode:

    python3 ferramentas/gerar-catalogo-filtros.py

Ele reescreve o trecho entre CATALOGO-INICIO e CATALOGO-FIM em
snippets/aquametria-calculadora-vazao.php. Nada mais do arquivo e tocado.

Quem entra no catalogo: exatamente quem o validador considera apto a ser sugerido
pela c3-vazao-filtro (minimo_para_sugerir do esquema) e nao esta em rascunho nem
em revalidar. Link de afiliado NAO decide quem entra (regra V16): produto apto
sem link sai no cartao, so que sem botao de loja.

DESDE 10/09/2026 (bloco T8, a vitrine) o item embutido leva mais dois campos:

  imagem — {url, alt, largura, altura, verificado_em}. So sai quando o registro
    tem URL E texto alternativo: a secao 6 do ARQUIPELAGO.md exige alt
    descritivo, e imagem sem alt na vitrine e defeito de acessibilidade que
    ninguem ve passar. Por isso o gerador RECUSA gravar quando acha url sem alt,
    em vez de emitir o cartao mudo. largura e altura viajam como estao no banco,
    inclusive null: a Aquametria nao grava dimensao que nao mediu, e o cartao
    reserva o espaco por aspect-ratio no CSS.

  preco — {min, max, loja, coletado_em, cotacoes}, lido de
    dados/produtos-cotacoes.json. NUNCA e preco atual: e cotacao com data, que e
    o que a secao 7 do contrato permite publicar. Cotacao com disponivel=false
    fica de fora. E o campo comissao_percentual NAO viaja para o snippet, por
    regra: comissao nao aparece na tela e nao ordena nada — o gerador confere
    isso antes de gravar e para se achar qualquer chave de comissao no item.
"""
import collections
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ESQUEMA = os.path.join(RAIZ, "dados", "esquema-produtos.json")
FILTROS = os.path.join(RAIZ, "dados", "produtos-filtro.json")
COTACOES = os.path.join(RAIZ, "dados", "produtos-cotacoes.json")
ALVO = os.path.join(RAIZ, "snippets", "aquametria-calculadora-vazao.php")

INICIO = "\t/* CATALOGO-INICIO — gerado por ferramentas/gerar-catalogo-filtros.py */"
FIM = "\t/* CATALOGO-FIM */"


def carregar(caminho):
    with io.open(caminho, encoding="utf-8") as f:
        return json.load(f, object_pairs_hook=collections.OrderedDict)


def preenchido(valor):
    if valor is None or valor == "":
        return False
    if isinstance(valor, (list, dict)) and len(valor) == 0:
        return False
    if isinstance(valor, dict):
        return any(v is not None for v in valor.values())
    return True


def atende(produto, requisitos):
    faltando = []
    for req in requisitos:
        alternativas = [p.strip() for p in req.split(" OU ")]
        if not any(preenchido(produto.get(alt)) for alt in alternativas):
            faltando.append(req)
    return faltando


def fonte_principal(produto):
    """A fonte de maior nivel que sustenta a vazao nominal — e o que a tela cita."""
    ordem = ["fabricante", "fabricante-via-busca", "manual", "norma", "varejo",
             "medicao-propria", "marketplace-anuncio"]
    fontes = produto.get("fontes") or []
    candidatas = [f for f in fontes if "vazao_nominal_lh" in (f.get("campos") or [])]
    if not candidatas:
        candidatas = list(fontes)
    if not candidatas:
        return None

    def peso(f):
        origem = f.get("origem") or ""
        return ordem.index(origem) if origem in ordem else len(ordem)

    return sorted(candidatas, key=peso)[0]


def imagem_do(produto, problemas):
    """A imagem do cartao da vitrine, ou None. Url sem alt PARA o gerador."""
    im = produto.get("imagem") or {}
    url = im.get("url")
    if not url:
        return None
    if not (im.get("alt") or "").strip():
        problemas.append(
            "%s tem imagem.url e nao tem imagem.alt — a vitrine nao publica "
            "imagem sem texto alternativo (secao 6 do ARQUIPELAGO.md)" % produto["id"]
        )
        return None

    saida = collections.OrderedDict()
    saida["url"] = url
    saida["alt"] = im.get("alt")
    saida["largura"] = im.get("largura")
    saida["altura"] = im.get("altura")
    saida["verificado_em"] = im.get("verificado_em")
    return saida


def preco_do(produto, cotacoes_por_produto):
    """Faixa de cotacao com data. NUNCA preco atual, e nunca comissao."""
    cotacoes = [c for c in cotacoes_por_produto.get(produto["id"], [])
                if c.get("disponivel") is not False and c.get("preco_brl") is not None]
    if not cotacoes:
        return None

    precos = [float(c["preco_brl"]) for c in cotacoes]
    datas = sorted(c.get("cotado_em") for c in cotacoes if c.get("cotado_em"))
    lojas = sorted(set(c.get("loja") for c in cotacoes if c.get("loja")))

    saida = collections.OrderedDict()
    saida["min"] = min(precos)
    saida["max"] = max(precos)
    saida["loja"] = lojas[0] if len(lojas) == 1 else None
    # A data que a tela mostra e a MAIS ANTIGA da faixa: e a que diz ha quanto
    # tempo o numero pode ter envelhecido. Mostrar a mais nova faria a faixa
    # parecer mais fresca do que e.
    saida["coletado_em"] = datas[0] if datas else None
    saida["cotacoes"] = len(cotacoes)
    return saida


def sem_comissao(item):
    """Comissao nunca viaja para o snippet: nao aparece na tela e nao ordena."""
    achados = []

    def varrer(valor, caminho):
        if isinstance(valor, dict):
            for k, v in valor.items():
                if "comiss" in k.lower():
                    achados.append(caminho + "." + k)
                varrer(v, caminho + "." + k)
        elif isinstance(valor, list):
            for i, v in enumerate(valor):
                varrer(v, "%s[%d]" % (caminho, i))

    varrer(item, item.get("id", "?"))
    return achados


def php_valor(v, nivel):
    tab = "\t" * nivel
    if v is None:
        return "null"
    if v is True:
        return "true"
    if v is False:
        return "false"
    if isinstance(v, (int, float)):
        return repr(v)
    if isinstance(v, str):
        return "'" + v.replace("\\", "\\\\").replace("'", "\\'") + "'"
    if isinstance(v, list):
        if not v:
            return "array()"
        itens = ", ".join(php_valor(x, nivel) for x in v)
        return "array( " + itens + " )"
    if isinstance(v, dict):
        linhas = ["array("]
        for k, val in v.items():
            linhas.append("%s\t'%s' => %s," % (tab, k, php_valor(val, nivel + 1)))
        linhas.append(tab + ")")
        return "\n".join(linhas)
    raise TypeError(repr(v))


def main():
    esquema = carregar(ESQUEMA)
    banco = carregar(FILTROS)
    requisitos = esquema["entidades"]["filtro"]["minimo_para_sugerir"]["c3-vazao-filtro"]

    cotacoes_por_produto = collections.defaultdict(list)
    for c in carregar(COTACOES)["cotacoes"]:
        cotacoes_por_produto[c["produto_id"]].append(c)

    problemas = []
    catalogo = []
    fora = []
    for p in banco["produtos"]:
        faltando = atende(p, requisitos)
        if p.get("status_registro") in ("rascunho", "revalidar"):
            faltando.append("status " + p["status_registro"])
        if faltando:
            fora.append((p["id"], ", ".join(faltando)))
            continue

        fonte = fonte_principal(p) or {}
        afiliado = p.get("afiliado") or {}
        vol = p.get("volume_atendido_declarado_L") or {}

        item = collections.OrderedDict()
        item["id"] = p["id"]
        item["marca"] = p.get("marca")
        item["modelo"] = p.get("modelo")
        item["tipo"] = p.get("tipo")
        item["vazao_lh"] = p.get("vazao_nominal_lh")
        item["potencia_w"] = p.get("potencia_w")
        item["coluna_m"] = p.get("coluna_maxima_m")
        item["coluna_na"] = bool(p.get("coluna_maxima_nao_se_aplica"))
        item["volume_min_L"] = vol.get("min")
        item["volume_max_L"] = vol.get("max")
        item["voltagem"] = p.get("voltagem") or []
        item["uv_w"] = p.get("uv_w")
        item["midia"] = p.get("midia_inclusa") or []
        item["fonte_ref"] = fonte.get("referencia")
        item["fonte_url"] = fonte.get("url")
        item["fonte_status"] = fonte.get("status")
        item["verificado_em"] = p.get("verificado_em")
        item["link"] = afiliado.get("url")
        item["anuncio"] = afiliado.get("anuncio_shopee")
        item["loja"] = afiliado.get("plataforma")
        item["imagem"] = imagem_do(p, problemas)
        item["preco"] = preco_do(p, cotacoes_por_produto)
        item["observacao"] = p.get("observacao")

        vazadas = sem_comissao(item)
        if vazadas:
            problemas.append("comissao vazando para o snippet em: " + ", ".join(vazadas))

        catalogo.append(item)

    if problemas:
        print("ERRO: nada foi gravado. %d problema(s):" % len(problemas))
        for t in problemas:
            print("  " + t)
        return 1

    catalogo.sort(key=lambda i: i["vazao_lh"])

    corpo = []
    for item in catalogo:
        corpo.append("\t\t" + php_valor(item, 2) + ",")

    bloco = [INICIO]
    bloco.append("\treturn array(")
    bloco.extend(corpo)
    bloco.append("\t);")
    bloco.append(FIM)
    novo = "\n".join(bloco)

    with io.open(ALVO, encoding="utf-8") as f:
        php = f.read()
    if INICIO not in php or FIM not in php:
        print("ERRO: marcadores CATALOGO-INICIO/CATALOGO-FIM nao encontrados em %s" % ALVO)
        return 1
    antes = php.split(INICIO)[0]
    depois = php.split(FIM, 1)[1]
    with io.open(ALVO, "w", encoding="utf-8") as f:
        f.write(antes + novo + depois)

    print("catalogo da C3: %d filtro(s) embutido(s)" % len(catalogo))
    for item in catalogo:
        preco = item["preco"]
        print("  %-28s %5s L/h  %-9s link: %-3s foto: %-3s cotacao: %s"
              % (item["id"], item["vazao_lh"], item["tipo"],
                 "sim" if item["link"] else "nao",
                 "sim" if item["imagem"] else "nao",
                 ("R$ %.2f (%s)" % (preco["min"], preco["coletado_em"])) if preco else "nao"))

    com_link = [i for i in catalogo if i["link"]]
    print("vitrine: %d de %d com link de loja, %d com foto, %d com cotacao datada"
          % (len(com_link), len(catalogo),
             len([i for i in catalogo if i["imagem"]]),
             len([i for i in catalogo if i["preco"]])))
    esperando = [i["id"] for i in catalogo if not i["link"]]
    if esperando:
        print("esperando link de afiliado (%d): %s" % (len(esperando), ", ".join(esperando)))
    if fora:
        print("fora do catalogo:")
        for pid, motivo in fora:
            print("  %-28s %s" % (pid, motivo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
