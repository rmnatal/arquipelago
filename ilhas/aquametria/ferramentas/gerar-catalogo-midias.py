# -*- coding: utf-8 -*-
"""Gera os dois catalogos que a C12 embute no snippet.

O site nao le o repositorio em tempo de execucao: o Sync copia o PHP e pronto.
Entao o banco precisa viajar DENTRO do snippet. Este script e o que impede as
copias de divergirem — depois de mexer em dados/produtos-midia.json ou em
dados/produtos-filtro.json, rode:

    python3 ferramentas/gerar-catalogo-midias.py

Ele reescreve dois trechos de snippets/aquametria-calculadora-midia.php:

  CATALOGO-MIDIAS-INICIO / FIM    as midias que a C12 pode sugerir
  CATALOGO-FILTROS-INICIO / FIM   os filtros que declaram volume util de midia

Nada mais do arquivo e tocado.

Quem entra: exatamente quem o validador considera apto (minimo_para_sugerir do
esquema) e nao esta em rascunho nem em revalidar. Link de afiliado NAO decide
quem entra (regra V16): produto apto sem link sai no cartao, so que sem botao
de loja.
"""
import collections
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ESQUEMA = os.path.join(RAIZ, "dados", "esquema-produtos.json")
MIDIAS = os.path.join(RAIZ, "dados", "produtos-midia.json")
FILTROS = os.path.join(RAIZ, "dados", "produtos-filtro.json")
COTACOES = os.path.join(RAIZ, "dados", "produtos-cotacoes.json")
ALVO = os.path.join(RAIZ, "snippets", "aquametria-calculadora-midia.php")

MARCAS = {
    "midias": ("\t/* CATALOGO-MIDIAS-INICIO — gerado por ferramentas/gerar-catalogo-midias.py */",
               "\t/* CATALOGO-MIDIAS-FIM */"),
    "filtros": ("\t/* CATALOGO-FILTROS-INICIO — gerado por ferramentas/gerar-catalogo-midias.py */",
                "\t/* CATALOGO-FILTROS-FIM */"),
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


ORDEM_FONTE = ["fabricante", "fabricante-via-busca", "manual", "norma", "varejo",
               "medicao-propria", "marketplace-anuncio"]


def fonte_de(produto, campo):
    """A fonte de maior nivel que sustenta o campo — e o que a tela cita."""
    fontes = produto.get("fontes") or []
    candidatas = [f for f in fontes if campo in (f.get("campos") or [])] or list(fontes)
    if not candidatas:
        return {}

    def peso(f):
        origem = f.get("origem") or ""
        return ORDEM_FONTE.index(origem) if origem in ORDEM_FONTE else len(ORDEM_FONTE)

    return sorted(candidatas, key=peso)[0]


def conflito_de(produto, campo):
    for c in produto.get("conflitos") or []:
        if c.get("campo") == campo:
            return c
    return None


def mL_por_L(dose):
    if not isinstance(dose, dict) or not dose.get("por_volume_agua_L"):
        return None
    return round(dose["volume_midia_mL"] / float(dose["por_volume_agua_L"]), 3)


def imagem_do(produto, problemas):
    """A imagem do cartao da vitrine, ou None. Url sem alt PARA o gerador.

    Mesmo portao dos geradores de filtro, de aquecedor e de iluminacao: a
    vitrine nao publica imagem sem texto alternativo (secao 6 do
    ARQUIPELAGO.md). O alt e texto de TELA, entao ele mora acentuado no banco.
    """
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
    # tempo o numero pode ter envelhecido.
    saida["coletado_em"] = datas[0] if datas else None
    saida["cotacoes"] = len(cotacoes)
    return saida


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


def montar_midias(esquema, banco, cotacoes_por_produto, problemas):
    requisitos = esquema["entidades"]["midia"]["minimo_para_sugerir"]["c12-midia-filtrante"]
    catalogo, fora = [], []
    for p in banco["produtos"]:
        faltando = atende(p, requisitos)
        if p.get("status_registro") in ("rascunho", "revalidar"):
            faltando.append("status " + p["status_registro"])
        if faltando:
            fora.append((p["id"], ", ".join(faltando)))
            continue

        fonte = fonte_de(p, "dosagem_declarada") or {}
        afiliado = p.get("afiliado") or {}
        vol = p.get("volume_atendido_declarado_L") or {}
        conflito = conflito_de(p, "dosagem_declarada")

        item = collections.OrderedDict()
        item["id"] = p["id"]
        item["marca"] = p.get("marca")
        item["modelo"] = p.get("modelo")
        item["tipo"] = p.get("tipo")
        item["material"] = p.get("material")
        item["embalagem_L"] = p.get("volume_embalagem_L")
        item["peso_g"] = p.get("peso_g")
        item["area_m2_L"] = p.get("area_superficial_m2_por_L")
        item["dose_mL_por_L"] = mL_por_L(p.get("dosagem_declarada"))
        item["dose_texto"] = None
        if p.get("dosagem_declarada"):
            d = p["dosagem_declarada"]
            item["dose_texto"] = "%s mL para %s L" % (d["volume_midia_mL"], d["por_volume_agua_L"])
        # Conflito de dosagem: a segunda leitura vai junto, com atribuicao.
        item["dose_alt_mL_por_L"] = None
        item["dose_alt_texto"] = None
        item["dose_alt_ref"] = None
        if conflito:
            leituras = [v for v in conflito["valores"] if mL_por_L(v.get("valor")) is not None]
            atual = item["dose_mL_por_L"]
            outras = [v for v in leituras if mL_por_L(v["valor"]) != atual]
            if outras:
                alt = outras[0]
                d = alt["valor"]
                item["dose_alt_mL_por_L"] = mL_por_L(d)
                item["dose_alt_texto"] = "%s mL para %s L" % (d["volume_midia_mL"], d["por_volume_agua_L"])
                item["dose_alt_ref"] = alt.get("referencia")
        item["granulometria_mm"] = p.get("granulometria_mm")
        item["regeneravel"] = p.get("regeneravel")
        item["vida_util_meses"] = p.get("vida_util_declarada_meses")
        item["posicao"] = p.get("posicao_no_fluxo")
        # O volume que a DOSAGEM declarada atende. O V21 cobra que ele seja o
        # denominador da propria dosagem: os dois sao a mesma declaracao.
        item["volume_max_L"] = vol.get("max")
        # DERIVADO, e por isso calculado aqui e nunca digitado no banco (V4):
        # quanto de aquario UMA embalagem cobre nessa dosagem. Para o Seachem
        # Matrix da 800 L, quatro vezes os 200 L da declaracao — porque a
        # embalagem de 1 L sao quatro doses de 250 mL. Era exatamente essa
        # diferenca que o cartao da C12 apagava ao chamar os 200 L de
        # "uma embalagem atende".
        item["rende_L"] = None
        if item["dose_mL_por_L"] and item["embalagem_L"]:
            item["rende_L"] = round(item["embalagem_L"] * 1000.0 / item["dose_mL_por_L"], 1)
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
        catalogo.append(item)

    # Ordem declarada na tela: da dosagem declarada mais economica para a mais
    # generosa; midia sem dosagem declarada vai para o fim, porque nao responde
    # a pergunta da pagina. Link de afiliado nao entra na ordenacao (V16).
    catalogo.sort(key=lambda i: (i["dose_mL_por_L"] is None,
                                 i["dose_mL_por_L"] or 0,
                                 i["id"]))
    return catalogo, fora


def montar_filtros(banco):
    catalogo, fora = [], []
    for p in banco["produtos"]:
        if not preenchido(p.get("volume_filtragem_L")):
            fora.append((p["id"], "sem volume_filtragem_L"))
            continue
        if p.get("status_registro") in ("rascunho", "revalidar"):
            fora.append((p["id"], "status " + p["status_registro"]))
            continue

        fonte = fonte_de(p, "volume_filtragem_L") or {}
        vol = p.get("volume_atendido_declarado_L") or {}
        conflito = conflito_de(p, "volume_filtragem_L")

        item = collections.OrderedDict()
        item["id"] = p["id"]
        item["marca"] = p.get("marca")
        item["modelo"] = p.get("modelo")
        item["tipo"] = p.get("tipo")
        item["midia_L"] = p.get("volume_filtragem_L")
        item["midia_L_alt"] = None
        item["midia_alt_ref"] = None
        item["midia_ref"] = None
        if conflito:
            valores = [v for v in conflito["valores"] if isinstance(v.get("valor"), (int, float))]
            for v in valores:
                if v["valor"] == item["midia_L"]:
                    item["midia_ref"] = v.get("referencia")
                elif item["midia_L_alt"] is None:
                    item["midia_L_alt"] = v["valor"]
                    item["midia_alt_ref"] = v.get("referencia")
        item["volume_min_L"] = vol.get("min")
        item["volume_max_L"] = vol.get("max")
        item["fonte_ref"] = fonte.get("referencia")
        item["fonte_url"] = fonte.get("url")
        item["fonte_status"] = fonte.get("status")
        item["verificado_em"] = p.get("verificado_em")
        catalogo.append(item)

    catalogo.sort(key=lambda i: i["midia_L"])
    return catalogo, fora


def escrever(php, chave, catalogo):
    inicio, fim = MARCAS[chave]
    if inicio not in php or fim not in php:
        raise SystemExit("ERRO: marcadores %s nao encontrados em %s" % (chave, ALVO))
    bloco = [inicio, "\treturn array("]
    for item in catalogo:
        bloco.append("\t\t" + php_valor(item, 2) + ",")
    bloco.append("\t);")
    bloco.append(fim)
    antes = php.split(inicio)[0]
    depois = php.split(fim, 1)[1]
    return antes + "\n".join(bloco) + depois


def main():
    esquema = carregar(ESQUEMA)
    cotacoes_por_produto = collections.defaultdict(list)
    for c in carregar(COTACOES)["cotacoes"]:
        cotacoes_por_produto[c["produto_id"]].append(c)

    problemas = []
    midias, fora_midias = montar_midias(esquema, carregar(MIDIAS),
                                        cotacoes_por_produto, problemas)
    filtros, fora_filtros = montar_filtros(carregar(FILTROS))

    if problemas:
        for t in problemas:
            print("  ERRO   " + t)
        raise SystemExit("catalogo NAO gerado: %d problema(s)" % len(problemas))

    with io.open(ALVO, encoding="utf-8") as f:
        php = f.read()
    php = escrever(php, "midias", midias)
    php = escrever(php, "filtros", filtros)
    with io.open(ALVO, "w", encoding="utf-8") as f:
        f.write(php)

    print("catalogo da C12: %d midia(s) e %d filtro(s) embutido(s)" % (len(midias), len(filtros)))
    for i in midias:
        print("  midia   %-28s %-10s %s mL/L  rende: %-7s link: %-3s foto: %-3s cotacao: %s"
              % (i["id"], i["tipo"],
                 i["dose_mL_por_L"] if i["dose_mL_por_L"] is not None else "  sem",
                 i["rende_L"] if i["rende_L"] is not None else "sem",
                 "sim" if i["link"] else "nao",
                 "sim" if i["imagem"] else "nao",
                 "R$ %.2f" % i["preco"]["min"] if i["preco"] else "sem"))

    # A medida CERTA para escolher a proxima vitrine e esta, e ela e contada
    # DEPOIS do portao de elegibilidade — foi o que a C5 ensinou em 11/09/2026.
    # Aqui a vitrine e a das midias biologicas, que sao as que a pagina
    # dimensiona; as quimicas so entram quando o leitor pede.
    bio = [i for i in midias if i["tipo"] == "biologica"]
    print("  vitrine: %d de %d com link, %d com foto, %d com cotacao"
          % (sum(1 for i in bio if i["link"]), len(bio),
             sum(1 for i in bio if i["imagem"]),
             sum(1 for i in bio if i["preco"])))
    for i in filtros:
        print("  filtro  %-28s %s L de midia%s"
              % (i["id"], i["midia_L"],
                 "" if i["midia_L_alt"] is None else " (outra leitura: %s L)" % i["midia_L_alt"]))
    for pid, motivo in fora_midias + fora_filtros:
        print("  fora    %-28s %s" % (pid, motivo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
