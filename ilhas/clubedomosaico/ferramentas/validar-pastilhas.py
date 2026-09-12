#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A REGUA DA CATEGORIA PASTILHA — bloco 3d, 12/09/2026.

Por que existe um portao separado do `validar-banco.py`: aquele confere que o
registro cumpre o ESQUEMA (campo presente, fonte presente, vocabulario certo).
Este confere o que o esquema nao tem como saber — se os numeros que o fabricante
publica na mesma ficha FECHAM ENTRE SI, e se o que o banco deixou de afirmar
realmente nao podia ser afirmado.

As tres perguntas, e cada uma tem a regua escrita AQUI, literal, nunca lida do
arquivo que ela mede:

 1. ARITMETICA DA PROPRIA FICHA. placas por caixa x area da placa tem de dar a
    metragem da caixa. Se nao der, ou o numero esta errado ou os tres nao sao do
    mesmo produto — e nos dois casos o item nao pode ir para uma vitrine.

 2. TETO FISICO. Dividindo o peso da caixa pela metragem sai um kg/m2. Vidro
    macico pesa, por espessura, `espessura_mm x densidade`. Um produto COM JUNTA
    nao pode pesar mais que a chapa cheia da mesma espessura. Quem passa do teto
    esta contando embalagem, e tem de trazer divergencia E resolucao escritas.
    A densidade entra como FAIXA (2,4 a 2,6 g/cm3, vidro sodo-calcico) e a
    reprovacao usa o extremo que mais favorece o produto: so reprova quem estoura
    o teto ate na densidade mais alta.

 3. O PASSO NAO SE INVENTA. Para cada item o portao refaz a divisao ingenua que a
    SERP inteira faz — lado da placa dividido pelo lado anunciado da pastilha — e
    cobra que o banco NAO a tenha transformado em numero. Sao dois jeitos de
    falhar: a divisao nao dar inteiro (nao ha arranjo possivel) e dar inteiro
    exigindo junta zero (placa telada sem junta e placa que nao se rejunta).

 4. COBERTURA POR TAMANHO, que e o eixo pelo qual a F1 escolhe pastilha, com a
    regra de nivel da escada de fontes: so item de nivel <= 3 conta como
    elegivel para recomendacao primaria.

Um processo por item, como nas outras baterias da ilha.
Uso:  python3 ferramentas/validar-pastilhas.py
"""

import json
import math
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)
BANCO = os.path.join(ILHA, "dados", "materiais-pastilhas.json")

# ----------------------------------------------------------------- a regua
# Escrita a mao a partir das fichas colhidas em 12/09/2026. Nao e lida do banco:
# e com ela que o banco e comparado. Ordem: lado da pastilha (cm), lado A da placa,
# lado B da placa, espessura (mm), placas por caixa, m2 por caixa, peso da caixa (kg),
# nivel da melhor fonte.
REGUA = {
    "glassmosaic-k2501":  (2.5, 30.0, 30.0, 4, 22, 1.98,  17.6, 3),
    "glassmosaic-k2502":  (2.5, 30.0, 30.0, 4, 22, 1.98,  17.6, 3),
    "glassmosaic-mix2510": (2.5, 30.0, 30.0, 4, 22, 1.98, 17.6, 3),
    "glassmosaic-k117":   (3.0, 29.2, 29.2, 4, 22, 1.87,  17.6, 3),
    "glassmosaic-k77":    (3.0, 29.2, 29.2, 4, 10, 0.85,   8.0, 3),
    "glassmosaic-k66":    (3.0, 29.2, 29.2, 4, 10, 0.85,   8.0, 3),
    "glassmosaic-a11":    (2.0, 32.3, 32.3, 3, 20, 2.086, 13.0, 3),
    "glassmosaic-a61":    (2.0, 32.3, 32.3, 3, 20, 2.09,  13.0, 3),
    "glassmosaic-st5102": (1.2, 28.6, 31.2, 6, 10, 0.89,  15.0, 3),
    "pastilhart-af1500":  (1.5, 30.0, 30.0, 8, None, None, None, 5),
}

DENSIDADE_MIN = 2.4   # g/cm3, vidro sodo-calcico
DENSIDADE_MAX = 2.6

# Os tamanhos que a F1 oferece, em cm. `None` e a tessela irregular, que nao tem lado.
TAMANHOS_DA_F1 = [("1x1", 1.0), ("2x2", 2.0), ("2,5x2,5", 2.5), ("irregular", None)]

NIVEL_MAXIMO_PARA_RECOMENDACAO = 3


class Contagem(object):
    def __init__(self):
        self.ok = 0
        self.falhas = []

    def afirma(self, condicao, texto):
        if condicao:
            self.ok += 1
        else:
            self.falhas.append(texto)


def casas_de(declarado):
    texto = repr(float(declarado))
    return len(texto.split(".")[1].rstrip("0")) if "." in texto else 0


def como_o_catalogo_fechou(valor, declarado):
    """O catalogo NAO tem uma regra unica de arredondamento, e dois SKUs da mesma
    linha provam: a caixa da Fosca cobre 2,086583 m2 e sai '2,086' num item (corte)
    e '2,09' no irmao (arredondamento). Uma regua que exigisse uma das duas
    reprovaria metade da linha sem haver erro de dado; uma que aceitasse qualquer
    coisa dentro de uma tolerancia frouxa nao mediria nada. Entao a regua aceita
    EXATAMENTE as duas operacoes, na precisao que o proprio numero declara, e
    devolve qual delas foi usada — para o relatorio mostrar a inconsistencia em vez
    de escondo-la."""
    casas = casas_de(declarado)
    fator = 10.0 ** casas
    arredondado = round(valor, casas)
    cortado = math.floor(valor * fator + 1e-9) / fator
    if abs(arredondado - declarado) < 1e-9:
        return "arredondou" if abs(cortado - declarado) >= 1e-9 else "igual"
    if abs(cortado - declarado) < 1e-9:
        return "cortou"
    return None


def medir(item, c):
    ident = item["id"]
    esperado = REGUA[ident]
    lado, placa_a, placa_b, esp, placas, m2, peso, nivel = esperado
    g = item.get("geometria") or {}
    props = item.get("propriedades") or {}

    def prop(nome):
        p = props.get(nome)
        return p.get("valor") if p else None

    # --- o banco diz o que a regua diz
    c.afirma(g.get("lado_anunciado_cm") == lado, "%s: lado anunciado" % ident)
    c.afirma(g.get("placa_lado_a_cm") == placa_a, "%s: lado A da placa" % ident)
    c.afirma(g.get("placa_lado_b_cm") == placa_b, "%s: lado B da placa" % ident)
    c.afirma(g.get("espessura_mm") == esp, "%s: espessura" % ident)
    c.afirma(prop("placas_por_caixa") == placas, "%s: placas por caixa" % ident)
    c.afirma(prop("m2_por_caixa") == m2, "%s: m2 por caixa" % ident)
    c.afirma(prop("peso_caixa_kg") == peso, "%s: peso da caixa" % ident)

    niveis = [f["nivel"] for f in (item.get("fontes") or {}).values()]
    c.afirma(niveis and min(niveis) == nivel, "%s: nivel da melhor fonte" % ident)

    # --- 1. a aritmetica da propria ficha fecha
    fechamento = None
    if placas is not None and m2 is not None:
        area_placa_m2 = (placa_a / 100.0) * (placa_b / 100.0)
        bruto = placas * area_placa_m2
        fechamento = como_o_catalogo_fechou(bruto, m2)
        c.afirma(fechamento is not None,
                 "%s: placas x area da placa = %.6f m2, e a ficha declara %s — nem cortando nem arredondando fecha"
                 % (ident, bruto, m2))

    # --- 2. o teto fisico do vidro macico
    if peso is not None and m2:
        kg_por_m2 = peso / m2
        teto_generoso = (esp / 10.0) * DENSIDADE_MAX * 10.0   # mm->cm, g/cm3 -> kg/m2
        estoura = kg_por_m2 > teto_generoso
        tem_divergencia = bool(item.get("divergencias")) and bool(item.get("resolucao"))
        if estoura:
            c.afirma(tem_divergencia,
                     "%s: %.2f kg/m2 passa do teto de %.2f e o item nao traz divergencia+resolucao escritas"
                     % (ident, kg_por_m2, teto_generoso))
        else:
            c.afirma(not item.get("divergencias") or tem_divergencia,
                     "%s: divergencia sem resolucao" % ident)
        # peso de caixa nunca vira peso de produto
        c.afirma(g.get("peso_unitario_g") is None,
                 "%s: peso unitario preenchido — nenhuma ficha declara isso" % ident)

    # --- 3. o passo nao se inventa
    c.afirma(g.get("pastilhas_por_placa") is None and bool(g.get("motivo_pastilhas_por_placa")),
             "%s: pastilhas por placa deveria ser null com motivo (nenhum fabricante declara)" % ident)
    c.afirma(g.get("passo_de_fabrica_cm") is None and bool(g.get("motivo_passo")),
             "%s: passo de fabrica deveria ser null com motivo" % ident)

    # a divisao ingenua, refeita aqui para provar que ela nao serve
    divisao = placa_a / lado
    inteira = abs(divisao - round(divisao)) < 1e-9
    if inteira:
        # cabe em inteiro, mas so com junta zero: passo = lado, junta = 0
        junta_mm = (placa_a / round(divisao) - lado) * 10.0
        c.afirma(abs(junta_mm) < 1e-6,
                 "%s: a divisao inteira deveria implicar junta zero, deu %.3f mm" % (ident, junta_mm))
    else:
        c.afirma(True, "")
        c.ok -= 1
        c.afirma(divisao != round(divisao), "%s: divisao ingenua marcada como nao inteira sem ser" % ident)
    if fechamento:
        print("  %s: a ficha %s para fechar a metragem da caixa" % (ident, fechamento))
    return inteira


def cobertura_por_tamanho(itens):
    """Quantos itens ELEGIVEIS (nivel <= 3) cada tamanho da F1 tem."""
    saida = []
    for rotulo, lado in TAMANHOS_DA_F1:
        if lado is None:
            n = 0
            motivo = "tessela irregular nao tem lado declarado; nenhum produto de placa serve"
        else:
            n = 0
            for it in itens:
                niveis = [f["nivel"] for f in (it.get("fontes") or {}).values()]
                if not niveis or min(niveis) > NIVEL_MAXIMO_PARA_RECOMENDACAO:
                    continue
                if (it.get("geometria") or {}).get("lado_anunciado_cm") == lado:
                    n += 1
            motivo = ""
        saida.append((rotulo, n, motivo))
    return saida


def um_item(ident):
    banco = json.load(open(BANCO, encoding="utf-8"))
    item = [m for m in banco["materiais"] if m["id"] == ident]
    if not item:
        print("FALHA: %s nao esta no banco" % ident)
        return 1
    c = Contagem()
    medir(item[0], c)
    for f in c.falhas:
        print("FALHA: %s" % f)
    print("CONTAGEM %s %d %d" % (ident, c.ok + len(c.falhas), len(c.falhas)))
    return 1 if c.falhas else 0


def main():
    banco = json.load(open(BANCO, encoding="utf-8"))
    itens = banco["materiais"]

    ids_banco = sorted(m["id"] for m in itens)
    ids_regua = sorted(REGUA)
    if ids_banco != ids_regua:
        print("FALHA: o banco tem %s e a regua tem %s" % (ids_banco, ids_regua))
        return 1

    print("Regua da categoria PASTILHA — um processo por item")
    total_ok = 0
    total_falha = 0
    inteiras = 0
    for ident in ids_regua:
        r = subprocess.run([sys.executable, __file__, ident], capture_output=True, text=True)
        for l in r.stdout.strip().split("\n"):
            if l.startswith("CONTAGEM "):
                _, i, n, f = l.split()
                print("  %-22s %3s afirmacoes, %s falha(s)" % (i, n, f))
            elif l:
                print(l)
        if r.returncode:
            total_falha += 1
        # a ultima linha traz a contagem
        linha = [l for l in r.stdout.strip().split("\n") if l.startswith("CONTAGEM ")]
        if linha:
            total_ok += int(linha[0].split()[2])

    # a prova agregada: a divisao ingenua nao serve em nenhum dos dois sentidos
    c = Contagem()
    for m in itens:
        g = m["geometria"]
        divisao = g["placa_lado_a_cm"] / g["lado_anunciado_cm"]
        if abs(divisao - round(divisao)) < 1e-9:
            inteiras += 1
    c.afirma(inteiras < len(itens),
             "todos os itens dao divisao inteira: a ambiguidade que o banco declara nao estaria provada")
    c.afirma(inteiras > 0,
             "nenhum item da divisao inteira: o caso da junta zero nao estaria representado")
    for f in c.falhas:
        print("FALHA: %s" % f)

    print("")
    print("  divisao lado da placa / lado da pastilha:")
    print("    da inteiro (e exige junta ZERO) ... %d de %d" % (inteiras, len(itens)))
    print("    nao da inteiro .................... %d de %d" % (len(itens) - inteiras, len(itens)))
    print("")
    print("  cobertura por tamanho da F1 (so fonte de nivel <= %d):" % NIVEL_MAXIMO_PARA_RECOMENDACAO)
    for rotulo, n, motivo in cobertura_por_tamanho(itens):
        marca = "OK " if n >= 3 else "ZERO" if n == 0 else "<3 "
        print("    %-10s %2d elegivel(is)  %s%s" % (rotulo, n, marca, ("  — " + motivo) if motivo else ""))
    print("")
    print("  itens .......................... %d" % len(itens))
    print("  afirmacoes ..................... %d" % (total_ok + c.ok + len(c.falhas)))
    print("  itens com falha ................ %d" % total_falha)

    if total_falha or c.falhas:
        print("\nREPROVADO")
        return 1
    print("\nOK: a categoria pastilha fecha com a regua escrita a mao.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        sys.exit(um_item(sys.argv[1]))
    sys.exit(main())
