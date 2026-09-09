# -*- coding: utf-8 -*-
"""Gera o catalogo de aquecedores que a C5 embute no snippet.

Mesmo desenho do gerador dos filtros: o site nao le o repositorio em tempo de
execucao, entao o banco viaja DENTRO do snippet e este script e o que impede as
duas copias de divergirem. Depois de mexer em dados/produtos-aquecedor.json:

    python3 ferramentas/gerar-catalogo-aquecedores.py

Ele reescreve o trecho entre CATALOGO-INICIO e CATALOGO-FIM em
snippets/aquametria-calculadora-aquecedor.php. Nada mais do arquivo e tocado.

Quem entra: exatamente quem o validador considera apto a ser sugerido pela
c5-aquecedor-delta (minimo_para_sugerir do esquema) e nao esta em rascunho nem em
revalidar. Link de afiliado NAO decide quem entra (regra V16).

A faixa de ajuste tem um caminho a mais que a dos filtros: quando o campo
faixa_ajuste_C ficou null por conflito entre fontes do mesmo nivel, o gerador
carrega a intersecao conservadora do conflito (regra V17) e marca o item como
conservador, para a tela poder dizer de onde veio a faixa.
"""
import collections
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ESQUEMA = os.path.join(RAIZ, "dados", "esquema-produtos.json")
AQUECEDORES = os.path.join(RAIZ, "dados", "produtos-aquecedor.json")
ALVO = os.path.join(RAIZ, "snippets", "aquametria-calculadora-aquecedor.php")

INICIO = "\t/* CATALOGO-INICIO — gerado por ferramentas/gerar-catalogo-aquecedores.py */"
FIM = "\t/* CATALOGO-FIM */"

ORDEM_FONTES = ["fabricante", "fabricante-via-busca", "manual", "norma", "varejo",
                "medicao-propria", "marketplace-anuncio"]


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


def conservador_de(produto, campo):
    for c in produto.get("conflitos") or []:
        if c.get("campo") == campo and c.get("tratamento") == "intersecao-conservadora":
            return c
    return None


def atende(produto, requisitos):
    faltando = []
    for req in requisitos:
        ok = False
        for alt in [p.strip() for p in req.split(" OU ")]:
            if alt.startswith("conflito:"):
                c = conservador_de(produto, alt.split(":", 1)[1])
                if c and preenchido(c.get("valor_conservador")):
                    ok = True
            elif preenchido(produto.get(alt)):
                ok = True
        if not ok:
            faltando.append(req)
    return faltando


def faixa_em_texto(valor):
    """'de 125 a 150 L' ou 'ate 100 L'. O varejo brasileiro declara teto sem piso na maioria
    das fichas de aquecedor, e imprimir 'None a 100 L' na tela seria defeito visivel."""
    vmin, vmax = (valor or {}).get("min"), (valor or {}).get("max")
    if vmin is not None and vmax is not None:
        return "de %s a %s L" % (vmin, vmax)
    if vmax is not None:
        return "ate %s L" % vmax
    if vmin is not None:
        return "a partir de %s L" % vmin
    return "volume nao declarado"


def fonte_principal(produto, campo):
    """A fonte de maior nivel que sustenta o campo — e o que a tela cita."""
    fontes = produto.get("fontes") or []
    candidatas = [f for f in fontes if campo in (f.get("campos") or [])]
    if not candidatas:
        candidatas = list(fontes)
    if not candidatas:
        return None

    def peso(f):
        origem = f.get("origem") or ""
        return ORDEM_FONTES.index(origem) if origem in ORDEM_FONTES else len(ORDEM_FONTES)

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
        return "array( " + ", ".join(php_valor(x, nivel) for x in v) + " )"
    if isinstance(v, dict):
        linhas = ["array("]
        for k, val in v.items():
            linhas.append("%s\t'%s' => %s," % (tab, k, php_valor(val, nivel + 1)))
        linhas.append(tab + ")")
        return "\n".join(linhas)
    raise TypeError(repr(v))


def main():
    esquema = carregar(ESQUEMA)
    banco = carregar(AQUECEDORES)
    requisitos = esquema["entidades"]["aquecedor"]["minimo_para_sugerir"]["c5-aquecedor-delta"]

    catalogo = []
    fora = []
    for p in banco["produtos"]:
        faltando = atende(p, requisitos)
        if p.get("status_registro") in ("rascunho", "revalidar"):
            faltando.append("status " + p["status_registro"])
        if faltando:
            fora.append((p["id"], ", ".join(faltando)))
            continue

        fonte = fonte_principal(p, "potencia_w") or {}
        afiliado = p.get("afiliado") or {}
        vol = p.get("volume_atendido_declarado_L") or {}

        faixa = p.get("faixa_ajuste_C")
        conflito = conservador_de(p, "faixa_ajuste_C")
        if preenchido(faixa):
            ajuste_min, ajuste_max = faixa.get("min"), faixa.get("max")
            conservadora = False
            derivacao = None
        else:
            valor = conflito["valor_conservador"]
            ajuste_min, ajuste_max = valor.get("min"), valor.get("max")
            conservadora = True
            derivacao = conflito.get("derivacao")

        # O conflito de volume declarado, quando existe, e conteudo: a tela mostra
        # as duas declaracoes lado a lado em vez de escolher uma calada.
        conflito_vol = None
        for c in p.get("conflitos") or []:
            if c.get("campo") == "volume_atendido_declarado_L":
                conflito_vol = "; ".join(
                    faixa_em_texto(v["valor"]) + " segundo " + (v.get("referencia") or "?")
                    for v in c.get("valores") or [])
                break

        item = collections.OrderedDict()
        item["id"] = p["id"]
        item["marca"] = p.get("marca")
        item["modelo"] = p.get("modelo")
        item["tipo"] = p.get("tipo")
        item["potencia_w"] = p.get("potencia_w")
        item["volume_min_L"] = vol.get("min")
        item["volume_max_L"] = vol.get("max")
        item["ajuste_min_C"] = ajuste_min
        item["ajuste_max_C"] = ajuste_max
        item["ajuste_conservador"] = conservadora
        item["ajuste_derivacao"] = derivacao
        item["precisao_C"] = p.get("precisao_C")
        item["comprimento_cm"] = p.get("comprimento_cm")
        item["seco"] = p.get("protecao_funcionamento_a_seco")
        item["voltagem"] = p.get("voltagem") or []
        item["fonte_ref"] = fonte.get("referencia")
        item["fonte_url"] = fonte.get("url")
        item["fonte_status"] = fonte.get("status")
        item["verificado_em"] = p.get("verificado_em")
        item["link"] = afiliado.get("url")
        item["anuncio"] = afiliado.get("anuncio_shopee")
        item["voltagem_anuncio"] = afiliado.get("voltagem_anuncio")
        item["loja"] = afiliado.get("plataforma")
        item["conflito_volume"] = conflito_vol
        catalogo.append(item)

    catalogo.sort(key=lambda i: (i["potencia_w"], i["marca"] or ""))

    bloco = [INICIO, "\treturn array("]
    bloco.extend("\t\t" + php_valor(item, 2) + "," for item in catalogo)
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

    print("catalogo da C5: %d aquecedor(es) embutido(s)" % len(catalogo))
    for item in catalogo:
        print("  %-28s %4s W  ajuste %s a %s C%s  link: %s"
              % (item["id"], item["potencia_w"], item["ajuste_min_C"], item["ajuste_max_C"],
                 " (conservadora)" if item["ajuste_conservador"] else "",
                 "sim" if item["link"] else "nao"))
    if fora:
        print("fora do catalogo:")
        for pid, motivo in fora:
            print("  %-28s %s" % (pid, motivo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
