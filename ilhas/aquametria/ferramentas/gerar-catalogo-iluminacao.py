# -*- coding: utf-8 -*-
"""Gera o catalogo de luminarias que a C15 embute no snippet.

O site nao le o repositorio em tempo de execucao: o Sync copia o PHP e pronto.
Entao o banco de produtos precisa viajar DENTRO do snippet. Este script e o que
impede as duas copias de divergirem — depois de mexer em
dados/produtos-iluminacao.json, rode:

    python3 ferramentas/gerar-catalogo-iluminacao.py

Ele reescreve o trecho entre CATALOGO-INICIO e CATALOGO-FIM em
snippets/aquametria-calculadora-iluminacao.php. Nada mais do arquivo e tocado.

Quem entra no catalogo: quem o validador considera apto a ser sugerido pela
c15-iluminacao (minimo_para_sugerir do esquema) e nao esta em rascunho nem em
revalidar. Desde 08/09/2026 esse minimo exige comprimento_aquario_cm DECLARADO,
por causa da convencao editorial 'cobertura-luminaria-declarada': o comprimento
da peca nao vira cobertura, porque nos registros que declaram os dois numeros a
razao entre eles varia de 1,15 a 1,59 vez e nao ha constante a extrair.

Link de afiliado NAO decide quem entra nem a ordem (regra V16): produto apto sem
link sai no cartao, so que sem botao de loja. O script tambem carrega, para a
tela, os produtos BARRADOS e o motivo de cada um — a C15 publica essa lista, que
e o conteudo desta entidade: o varejo brasileiro vende luminaria por centimetro
de peca e omite o lumen, que e a grandeza que dimensiona.

DESDE 11/09/2026 (bloco T8, a vitrine da C15) o item embutido leva mais dois
campos, com o MESMO desenho dos geradores de filtros e de aquecedores — de
proposito, porque tres regras diferentes para o mesmo cartao viram tres telas
diferentes:

  imagem — {url, alt, largura, altura, verificado_em}. So sai quando o registro
    tem URL E texto alternativo: a secao 6 do ARQUIPELAGO.md exige alt
    descritivo, e imagem sem alt na vitrine e defeito de acessibilidade que
    ninguem ve passar. Por isso o gerador RECUSA gravar quando acha url sem alt.
    largura e altura viajam como estao no banco, inclusive null: a Aquametria nao
    grava dimensao que nao mediu, e o cartao reserva o espaco por aspect-ratio.

  preco — {min, max, loja, coletado_em, cotacoes}, lido de
    dados/produtos-cotacoes.json. NUNCA e preco atual: e cotacao com data, que e
    o que a secao 7 do contrato permite publicar. Cotacao com disponivel=false
    fica de fora. E o campo comissao_percentual NAO viaja para o snippet, por
    regra: comissao nao aparece na tela e nao ordena nada — o gerador confere
    isso antes de gravar e para se achar qualquer chave de comissao no item.

O QUE ESTE BANCO ENSINOU, e vale para o proximo que montar vitrine: das 10
luminarias com foto, 8 sao Soma que NAO declaram lumen e por isso nem chegam ao
catalogo. Foto e link se contam DEPOIS do portao de elegibilidade, nunca antes —
e por isso a linha 'vitrine:' do fim deste script existe.
"""
import collections
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ESQUEMA = os.path.join(RAIZ, "dados", "esquema-produtos.json")
BANCO = os.path.join(RAIZ, "dados", "produtos-iluminacao.json")
COTACOES = os.path.join(RAIZ, "dados", "produtos-cotacoes.json")
ALVO = os.path.join(RAIZ, "snippets", "aquametria-calculadora-iluminacao.php")

INICIO = "\t/* CATALOGO-INICIO — gerado por ferramentas/gerar-catalogo-iluminacao.py */"
FIM = "\t/* CATALOGO-FIM */"

INICIO_FORA = "\t/* BARRADOS-INICIO — gerado por ferramentas/gerar-catalogo-iluminacao.py */"
FIM_FORA = "\t/* BARRADOS-FIM */"

INICIO_REGULA = "\t/* REGULA-INICIO — gerado por ferramentas/gerar-catalogo-iluminacao.py */"
FIM_REGULA = "\t/* REGULA-FIM */"

ROTULO_CAMPO = {
    "fluxo_lm": "não declara o fluxo luminoso (lúmens)",
    "potencia_w": "não declara a potência",
    "voltagem": "não declara a voltagem",
    "comprimento_aquario_cm": "não declara o comprimento de aquário que cobre",
}


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
    """A fonte de maior nivel que sustenta o lumen — e o que a tela cita."""
    ordem = ["fabricante", "fabricante-via-busca", "manual", "norma", "varejo",
             "medicao-propria", "marketplace-anuncio"]
    fontes = produto.get("fontes") or []
    candidatas = [f for f in fontes if "fluxo_lm" in (f.get("campos") or [])]
    if not candidatas:
        candidatas = [f for f in fontes if f.get("origem") != "marketplace-anuncio"]
    if not candidatas:
        candidatas = list(fontes)
    if not candidatas:
        return None

    def peso(f):
        origem = f.get("origem") or ""
        return ordem.index(origem) if origem in ordem else len(ordem)

    return sorted(candidatas, key=peso)[0]


def nota_de_conflito(produto):
    """Conflito de comprimento vira uma linha na ficha do cartao.

    O texto da tela NAO sai daqui: o banco e escrito sem acento e a tela da
    Aquametria sai acentuada. Entao o que viaja e a estrutura (campo, valor e
    origem de cada leitura) e quem escreve a frase e o JavaScript do snippet.
    """
    for c in produto.get("conflitos") or []:
        if "comprimento" not in (c.get("campo") or ""):
            continue
        return collections.OrderedDict([
            ("campo", c.get("campo")),
            ("tratamento", c.get("tratamento")),
            ("valores", [collections.OrderedDict([
                ("valor", v.get("valor")),
                ("origem", v.get("origem")),
            ]) for v in c.get("valores") or []]),
        ])
    return None


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
        return "array( " + ", ".join(php_valor(x, nivel) for x in v) + " )"
    if isinstance(v, dict):
        linhas = ["array("]
        for k, val in v.items():
            linhas.append("%s\t'%s' => %s," % (tab, k, php_valor(val, nivel + 1)))
        linhas.append(tab + ")")
        return "\n".join(linhas)
    raise TypeError(repr(v))


def escrever_bloco(php, inicio, fim, corpo):
    if inicio not in php or fim not in php:
        raise SystemExit("ERRO: marcadores %s/%s nao encontrados em %s" % (inicio, fim, ALVO))
    antes = php.split(inicio)[0]
    depois = php.split(fim, 1)[1]
    return antes + "\n".join([inicio] + corpo + [fim]) + depois


def main():
    esquema = carregar(ESQUEMA)
    banco = carregar(BANCO)
    requisitos = esquema["entidades"]["iluminacao"]["minimo_para_sugerir"]["c15-iluminacao"]
    decl_regulagem = next(
        (c for c in esquema["entidades"]["iluminacao"]["campos"] if c.get("campo") == "regulagem"),
        {})

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

        cobertura = p.get("comprimento_aquario_cm") or {}
        nome = " ".join(x for x in [p.get("marca"), p.get("modelo")] if x)

        if faltando:
            fora.append(collections.OrderedDict([
                ("id", p["id"]),
                ("nome", nome),
                ("motivo", "; ".join(ROTULO_CAMPO.get(c, c) for c in faltando)),
                ("tem_link", bool((p.get("afiliado") or {}).get("url"))),
            ]))
            continue

        fonte = fonte_principal(p) or {}
        afiliado = p.get("afiliado") or {}

        item = collections.OrderedDict()
        item["id"] = p["id"]
        item["marca"] = p.get("marca")
        item["modelo"] = p.get("modelo")
        item["tipo"] = p.get("tipo")
        item["potencia_w"] = p.get("potencia_w")
        item["fluxo_lm"] = p.get("fluxo_lm")
        item["kelvin"] = p.get("temperatura_cor_k")
        item["espectro"] = p.get("espectro")
        item["peca_cm"] = p.get("comprimento_luminaria_cm")
        item["aquario_min_cm"] = cobertura.get("min")
        item["aquario_max_cm"] = cobertura.get("max")
        item["voltagem"] = p.get("voltagem") or []
        item["regulagem"] = p.get("regulagem")
        item["ppfd"] = p.get("ppfd_declarado")
        item["ppfd_distancia_cm"] = p.get("ppfd_distancia_cm")
        item["fonte_ref"] = fonte.get("referencia")
        item["fonte_url"] = fonte.get("url")
        item["fonte_status"] = fonte.get("status")
        item["verificado_em"] = p.get("verificado_em")
        item["link"] = afiliado.get("url")
        item["anuncio"] = afiliado.get("anuncio_shopee")
        item["loja"] = afiliado.get("plataforma")
        item["conflito"] = nota_de_conflito(p)
        item["observacao"] = p.get("observacao")
        item["imagem"] = imagem_do(p, problemas)
        item["preco"] = preco_do(p, cotacoes_por_produto)

        vazadas = sem_comissao(item)
        if vazadas:
            problemas.append("comissao vazando para o snippet em: " + ", ".join(vazadas))

        catalogo.append(item)

    if problemas:
        print("ERRO: nada foi gravado. %d problema(s):" % len(problemas))
        for t in problemas:
            print("  " + t)
        return 1

    catalogo.sort(key=lambda i: i["fluxo_lm"])

    corpo = ["\treturn array("]
    corpo.extend("\t\t" + php_valor(i, 2) + "," for i in catalogo)
    corpo.append("\t);")

    corpo_fora = ["\treturn array("]
    corpo_fora.extend("\t\t" + php_valor(i, 2) + "," for i in fora)
    corpo_fora.append("\t);")

    # A classificacao do esquema viaja junto, para o snippet parar de guardar uma
    # terceira copia dela. Se a chave sumir do esquema, isto para: lista vazia
    # aqui faria a C15 recusar TODA regulagem em silencio, que e o defeito com o
    # sinal trocado.
    regula = decl_regulagem.get("regula_intensidade") or []
    if not regula:
        problemas.append(
            "o esquema nao declara 'regulagem.regula_intensidade': sem essa lista a C15 "
            "nao tem como saber qual comando abaixa o brilho, e recusaria todos em silencio")
    fora_do_vocabulario = [v for v in regula if v not in (decl_regulagem.get("vocabulario") or [])]
    if fora_do_vocabulario:
        problemas.append(
            "'regulagem.regula_intensidade' lista valor que nao existe no vocabulario: "
            + ", ".join(fora_do_vocabulario))
    corpo_regula = ["\treturn array("]
    corpo_regula.extend("\t\t" + php_valor(v, 2) + "," for v in regula)
    corpo_regula.append("\t);")

    if problemas:
        print("ERRO: nada foi gravado. %d problema(s):" % len(problemas))
        for t in problemas:
            print("  " + t)
        return 1

    with io.open(ALVO, encoding="utf-8") as f:
        php = f.read()
    php = escrever_bloco(php, INICIO, FIM, corpo)
    php = escrever_bloco(php, INICIO_FORA, FIM_FORA, corpo_fora)
    php = escrever_bloco(php, INICIO_REGULA, FIM_REGULA, corpo_regula)
    with io.open(ALVO, "w", encoding="utf-8") as f:
        f.write(php)

    print("catalogo da C15: %d luminaria(s) embutida(s)" % len(catalogo))
    for i in catalogo:
        preco = i["preco"]
        print("  %-26s %6s lm  %5s W  cobre %s a %s cm  link: %-3s foto: %-3s cotacao: %s"
              % (i["id"], i["fluxo_lm"], i["potencia_w"],
                 i["aquario_min_cm"] if i["aquario_min_cm"] is not None else "—",
                 i["aquario_max_cm"], "sim" if i["link"] else "nao",
                 "sim" if i["imagem"] else "nao",
                 ("R$ %.2f (%s)" % (preco["min"], preco["coletado_em"])) if preco else "nao"))

    # Foto e link se contam DEPOIS do portao: o numero medido no banco inteiro
    # responderia outra pergunta, e foi assim que a C5 escolheu errado a ordem.
    com_link = [i for i in catalogo if i["link"]]
    print("vitrine: %d de %d com link de loja, %d com foto, %d com cotacao datada"
          % (len(com_link), len(catalogo),
             len([i for i in catalogo if i["imagem"]]),
             len([i for i in catalogo if i["preco"]])))
    esperando = [i["id"] for i in catalogo if not i["link"]]
    if esperando:
        print("esperando link de afiliado (%d): %s" % (len(esperando), ", ".join(esperando)))

    print("barrados (a tela publica a lista e o motivo): %d" % len(fora))
    for i in fora:
        print("  %-26s %s%s" % (i["id"], i["motivo"],
                                "  [tem link de afiliado e mesmo assim nao e sugerida]" if i["tem_link"] else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
