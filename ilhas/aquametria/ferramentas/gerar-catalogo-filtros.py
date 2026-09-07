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
"""
import collections
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ESQUEMA = os.path.join(RAIZ, "dados", "esquema-produtos.json")
FILTROS = os.path.join(RAIZ, "dados", "produtos-filtro.json")
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
        item["observacao"] = p.get("observacao")
        catalogo.append(item)

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
        print("  %-28s %5s L/h  %-9s link: %s"
              % (item["id"], item["vazao_lh"], item["tipo"],
                 "sim" if item["link"] else "nao"))
    if fora:
        print("fora do catalogo:")
        for pid, motivo in fora:
            print("  %-28s %s" % (pid, motivo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
