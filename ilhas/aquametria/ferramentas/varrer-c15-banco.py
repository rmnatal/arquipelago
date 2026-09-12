# -*- coding: utf-8 -*-
"""Regua PROPRIA de cobertura da C15, medida no BANCO e nao na tela.

Por que ela existe, e por que nao basta o varrer-cobertura.mjs
--------------------------------------------------------------
`ferramentas/varrer-cobertura.mjs` abre a calculadora num Chromium e conta os
cartoes desenhados. E a medicao certa do que o site ENTREGA, e continua sendo a
medicao de fechamento. So que ela responde depois do fato: para decidir O QUE
COLHER, quem monta a lista de compras precisa perguntar ao banco quantas
luminarias sobreviveriam a cada faixa — inclusive faixas que hoje saem vazias,
onde a tela nao tem cartao nenhum para contar e portanto nao diz por que.

Esta regua e independente de proposito (secao 8 do ARQUIPELAGO.md, "quem confere
escreve a propria regua"): ela NAO chama o gerador de catalogo, NAO le o trecho
gerado dentro do snippet e NAO importa uma linha de JavaScript da calculadora.
Le `dados/produtos-iluminacao.json` e a declaracao `minimo_para_sugerir` do
`dados/esquema-produtos.json`, e reimplementa a regra publicada da C15:

  V (litros)  = comprimento x 40 x 40 / 1000   (secao transversal de 40 x 40 cm,
                a mesma do varrer-cobertura.mjs, para as duas series serem
                comparaveis entre si)
  min, max    = V x faixa consolidada do nivel  (baixa 10-20, media 20-40,
                alta 40-60 lm/L, com o teto da ALTA aberto)
  cobre       = o comprimento do aquario cabe na cobertura DECLARADA do registro
  dentro      = cobre E fluxo_lm >= min E (nivel alto OU fluxo_lm <= max)

As tres faixas consolidadas sao constantes publicadas na propria pagina; estao
repetidas aqui de proposito, porque regua que importa a constante de quem produz
o dado erra junto com ele. Se a pagina mudar a faixa, esta regua passa a
discordar dela, e discordar e o resultado util: e o sinal de que uma das duas
mudou sozinha.

Uso:
    python3 ferramentas/varrer-c15-banco.py           # tabela + resumo
    python3 ferramentas/varrer-c15-banco.py --compras # so a lista de compras
"""
import collections
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANCO = os.path.join(RAIZ, "dados", "produtos-iluminacao.json")
ESQUEMA = os.path.join(RAIZ, "dados", "esquema-produtos.json")

# Faixas consolidadas da C15, em lm/L. O teto da alta e ABERTO: a fonte publica
# "acima de 40 lm/L" e para ai, e a pagina trata isso como faixa sem teto.
NIVEIS = collections.OrderedDict([
    ("baixa", {"rotulo": "exigencia baixa", "min": 10, "max": 20, "aberto": False}),
    ("media", {"rotulo": "exigencia media", "min": 20, "max": 40, "aberto": False}),
    ("alta", {"rotulo": "exigencia alta", "min": 40, "max": 60, "aberto": True}),
])

LARGURA_CM = 40.0
ALTURA_CM = 40.0

PISO_DE_FAIXA = 3   # secao 14.3 do ARQUIPELAGO.md


def carregar(caminho):
    with io.open(caminho, encoding="utf-8") as f:
        return json.load(f, object_pairs_hook=collections.OrderedDict)


def valor(registro, campo):
    """Le um campo do registro, resolvendo a alternativa 'conflito:campo'."""
    if campo.startswith("conflito:"):
        alvo = campo.split(":", 1)[1]
        for c in registro.get("conflitos", []) or []:
            if c.get("campo") == alvo and c.get("valor_conservador") is not None:
                return c.get("valor_conservador")
        return None
    return registro.get(campo)


def preenchido(v):
    if v is None:
        return False
    if isinstance(v, (list, tuple)):
        return len(v) > 0
    if isinstance(v, dict):
        return any(x is not None for x in v.values())
    if isinstance(v, str):
        return v.strip() != ""
    return True


def apto(registro, exigidos):
    """Aplica minimo_para_sugerir. Devolve (bool, [campos que faltam])."""
    faltando = []
    for exigencia in exigidos:
        alternativas = [p.strip() for p in exigencia.split(" OU ")]
        if not any(preenchido(valor(registro, a)) for a in alternativas):
            faltando.append(alternativas[0])
    return (not faltando), faltando


def cobertura(registro):
    """Faixa de comprimento de aquario DECLARADA pelo registro, em cm."""
    c = registro.get("comprimento_aquario_cm") or {}
    if isinstance(c, (int, float)):
        return float(c), float(c)
    return c.get("min"), c.get("max")


def cobre(registro, cm):
    mn, mx = cobertura(registro)
    if mn is not None and cm < mn:
        return False
    if mx is not None and cm > mx:
        return False
    return True


def catalogo():
    banco = carregar(BANCO)
    esquema = carregar(ESQUEMA)
    exigidos = esquema["entidades"]["iluminacao"]["minimo_para_sugerir"]["c15-iluminacao"]

    dentro, barrados = [], []
    for p in banco["produtos"]:
        if p.get("status_registro") in ("rascunho", "revalidar"):
            barrados.append((p, ["status_registro=" + str(p.get("status_registro"))]))
            continue
        ok, faltando = apto(p, exigidos)
        (dentro if ok else barrados).append((p, faltando))
    return dentro, barrados, exigidos


def regula_intensidade(esquema):
    """Quais valores de 'regulagem' abaixam o brilho, lidos do esquema.

    A C15 tem DOIS jeitos de oferecer uma luminaria: quem cai dentro da faixa, e
    quem passa do teto mas tem regulagem declarada e por isso pode trabalhar
    abaixo do maximo. Contar so o primeiro mede metade da prateleira — e foi
    exatamente por isso que a serie de 09/09/2026 leu como "falta produto" um
    problema que era de um campo com duas grafias.
    """
    for c in esquema["entidades"]["iluminacao"]["campos"]:
        if c.get("campo") == "regulagem":
            return list(c.get("regula_intensidade") or [])
    return []


def varrer(de=30, ate=120, passo=5):
    sugeriveis, barrados, exigidos = catalogo()
    regula = regula_intensidade(carregar(ESQUEMA))
    linhas = []
    for chave, nivel in NIVEIS.items():
        for cm in range(de, ate + 1, passo):
            v = round(cm * LARGURA_CM * ALTURA_CM / 1000.0)
            lm_min = v * nivel["min"]
            lm_max = v * nivel["max"]
            elegiveis, reguláveis = [], []
            for p, _ in sugeriveis:
                if not cobre(p, cm):
                    continue
                fluxo = p.get("fluxo_lm")
                if fluxo is None:
                    continue
                if fluxo >= lm_min and (nivel["aberto"] or fluxo <= lm_max):
                    elegiveis.append(p["id"])
                elif fluxo > lm_max and p.get("regulagem") in regula:
                    reguláveis.append(p["id"])
            reguláveis = reguláveis[:2]   # a pagina serve no maximo dois
            linhas.append({
                "nivel": chave,
                "rotulo": nivel["rotulo"],
                "cm": cm,
                "litros": v,
                "lm_min": lm_min,
                "lm_max": None if nivel["aberto"] else lm_max,
                "n": len(elegiveis),
                "n_regulavel": len(reguláveis),
                "n_total": len(elegiveis) + len(reguláveis),
                "ids": elegiveis,
                "ids_regulavel": reguláveis,
            })
    return linhas, sugeriveis, barrados


def agrupar(linhas, chave="n_total"):
    """Junta comprimentos vizinhos com a MESMA contagem, como a serie de 09/09."""
    saida = []
    for linha in linhas:
        if (saida and saida[-1]["nivel"] == linha["nivel"]
                and saida[-1]["n"] == linha[chave]
                and saida[-1]["n_faixa"] == linha["n"]):
            saida[-1]["ate"] = linha["cm"]
        else:
            saida.append({"nivel": linha["nivel"], "rotulo": linha["rotulo"],
                          "de": linha["cm"], "ate": linha["cm"],
                          "n": linha[chave], "n_faixa": linha["n"],
                          "n_regulavel": linha["n_regulavel"]})
    return saida


def main():
    linhas, sugeriveis, barrados = varrer()
    faixas = agrupar(linhas)

    so_compras = "--compras" in sys.argv

    if not so_compras:
        print("C15 — cobertura medida NO BANCO (regua propria, sem navegador)")
        print("catalogo sugerivel: %d de %d registros; barrados: %d"
              % (len(sugeriveis), len(sugeriveis) + len(barrados), len(barrados)))
        print("")
        print("| condicao declarada | faixa | na faixa | + regulavel | total | |")
        print("|---|---|---:|---:|---:|---|")
        for f in faixas:
            faixa = ("%d cm" % f["de"]) if f["de"] == f["ate"] else ("%d a %d cm" % (f["de"], f["ate"]))
            if f["n"] == 0:
                marca = "**VAZIA**"
            elif f["n"] < PISO_DE_FAIXA:
                marca = "**abaixo de 3**"
            else:
                marca = "ok"
            print("| %s | %s | %d | %d | %d | %s |"
                  % (f["rotulo"], faixa, f["n_faixa"], f["n_regulavel"], f["n"], marca))
        print("")

    vazias = [f for f in faixas if f["n"] == 0]
    baixas = [f for f in faixas if 0 < f["n"] < PISO_DE_FAIXA]
    boas = [f for f in faixas if f["n"] >= PISO_DE_FAIXA]
    print("Faixas medidas: %d | VAZIAS: %d | abaixo do piso de %d: %d | cumprem: %d"
          % (len(faixas), len(vazias), PISO_DE_FAIXA, len(baixas), len(boas)))
    print("")

    # Lista de compras: para cada faixa que nao cumpre, que fluxo faltou.
    print("LISTA DE COMPRAS — o que um registro novo precisaria declarar")
    pendentes = [l for l in linhas if l["n"] < PISO_DE_FAIXA]
    por_nivel = collections.OrderedDict()
    for l in pendentes:
        por_nivel.setdefault(l["nivel"], []).append(l)
    for nivel, ls in por_nivel.items():
        cms = [l["cm"] for l in ls]
        lm_lo = min(l["lm_min"] for l in ls)
        lm_hi = max((l["lm_max"] or l["lm_min"] * 2) for l in ls)
        print("  %-16s %d comprimentos sem piso (de %d a %d cm), fluxo pedido de %s a %s lm"
              % (NIVEIS[nivel]["rotulo"], len(ls), min(cms), max(cms),
                 "{:,}".format(int(lm_lo)).replace(",", "."),
                 "{:,}".format(int(lm_hi)).replace(",", ".")))
    print("")
    print("BARRADOS (o campo que falta e a lista de compras de verdade)")
    porque = collections.Counter()
    for p, faltando in barrados:
        for f in faltando:
            porque[f] += 1
    for campo, n in porque.most_common():
        print("  %-28s %d registro(s)" % (campo, n))
    return 0


if __name__ == "__main__":
    sys.exit(main())
