#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A BANCADA da lista de prospeccao do widget (bloco 6 da jornadafly).

    python3 ferramentas/teste-prospeccao.py

Duas coisas, e as duas sao sobre DISCORDAR da referencia em vez de repeti-la:

  1. A ESCADA REESCRITA A MAO. A classificacao de cada candidato e recalculada
     aqui, com codigo escrito do zero a partir da regra em prosa do banco, e
     comparada com o que `prospeccao-referencia.py` devolve. Portao que chama a
     funcao que esta testando nao testa nada -- e a disciplina que o teste-f1
     desta ilha ja usa, reescrevendo a aritmetica em Fraction para poder
     discordar do gerador.

  2. A PROSA CONFERIDA CONTRA O DADO. As afirmacoes numericas do bloco
     `o_achado_desta_passada` sao LIDAS do JSON e conferidas contra
     `dados/experiencias.json` e `dados/corpus-buscas.md`. E a terceira conta que
     a secao 8 do contrato pede, e o defeito que ela impede e o mais barato de
     cometer: a cadeia do achado afirma «quatro experiencias», «tres dos quatro
     operadores sao poder publico» e «64 dominios», e no dia em que o banco
     mudar essas frases viram mentira sem ninguem tocar nelas.
"""

import importlib.util
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "prospeccao_referencia", os.path.join(AQUI, "prospeccao-referencia.py"))
ref = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ref)
RAIZ = ref.RAIZ

falhas = []
afirmacoes = [0]


def afirma(condicao, frase):
    afirmacoes[0] += 1
    if not condicao:
        falhas.append(frase)


# ------------------------------------------------------- a escada, a mao

# Reescrita do zero a partir da prosa de `a_escada_da_prioridade`, sem chamar
# ref.prioridade. Os nomes e a ordem sao os da prosa, nao os do codigo dela.
NAO_HOSPEDAM = (
    "plataforma", "revendedor_de_ingresso", "revendedor_de_passe",
    "portal_de_conteudo", "imprensa_de_trade",
)
HOSPEDAM = ("operador_da_experiencia", "receptivo", "concessionaria_de_bem_publico",
            "guia_autorizado", "pousada")


def classe_a_mao(banco, c):
    disputados = set(banco["a_regra_que_ordena_esta_lista"]["clusters_disputados"])
    mapa = {}
    for cluster, consultas in banco["consultas_do_corpus_por_cluster"].items():
        for q in consultas:
            mapa.setdefault(q, cluster)
    for q in c.get("consultas_do_corpus") or []:
        if mapa.get(q) in disputados:
            return "barrado"
    t = c.get("tipo")
    if t is None or t in NAO_HOSPEDAM:
        return "3"
    if t not in HOSPEDAM:
        return "3"
    if c.get("site_proprio") is not True:
        return "3"
    if c.get("brasileiro") is True:
        if c.get("vende_experiencia") is True and c.get("mais_de_uma_versao_vendida") is True:
            return "1"
        return "2"
    return "2" if c.get("fala_pt_br") is True else "3"


def f1_a_mao(banco, estado, c):
    """A regua da oferta da F1, reescrita a mao a partir de `a_regra_da_oferta`."""
    if classe_a_mao(banco, c) in ("barrado", "3"):
        return False
    atendidas = [i for i in (c.get("experiencias_do_banco_atendidas") or []) if i in estado["ids"]]
    if not atendidas:
        return False
    return c.get("relacao_com_a_versao_do_banco") == "vende_a_mesma_versao"


def main():
    banco, experiencias = ref.carregar()
    estado = ref.estado_do_banco(experiencias)
    with open(os.path.join(RAIZ, "dados", "corpus-buscas.md"), encoding="utf-8") as f:
        corpus = f.read()

    # ---- 1. a escada e a oferta, candidato por candidato
    for c in banco["candidatos"]:
        esperado = classe_a_mao(banco, c)
        obtido, motivo = ref.prioridade(banco, c)
        afirma(esperado == obtido,
               "%s: escada a mao diz %s e a referencia diz %s" % (c["dominio"], esperado, obtido))
        afirma(isinstance(motivo, str) and len(motivo) > 20,
               "%s: a referencia nao explicou a prioridade" % c["dominio"])

        f1_ref = [x for x in ref.ferramentas_ofertaveis(banco, estado, c) if x["ferramenta"] == "F1"][0]
        afirma(f1_a_mao(banco, estado, c) == f1_ref["ofertavel"],
               "%s: a regua da F1 a mao discorda da referencia" % c["dominio"])

        for x in ref.ferramentas_ofertaveis(banco, estado, c):
            afirma(isinstance(x["por_que"], str) and len(x["por_que"]) > 10,
                   "%s/%s: ferramenta sem razao escrita" % (c["dominio"], x["ferramenta"]))

    # ---- 2. as regras da oferta que nao dependem do candidato
    for c in banco["candidatos"]:
        fs = {x["ferramenta"]: x for x in ref.ferramentas_ofertaveis(banco, estado, c)}
        if estado["faixas_diarias"] == 0:
            afirma(fs["F2"]["ofertavel"] is False,
                   "%s: F2 ofertavel com o banco sem nenhuma FAIXA_DIARIA" % c["dominio"])
        if estado["passes_de_cidade"] == 0 or estado["coberturas_de_passe"] == 0:
            afirma(fs["F3"]["ofertavel"] is False,
                   "%s: F3 ofertavel com o banco sem passe ou sem cobertura" % c["dominio"])
        if c.get("vende_passe_de_cidade") is True:
            afirma(fs["F3"]["ofertavel"] is False,
                   "%s: F3 ofertada a quem vende passe de cidade" % c["dominio"])
        if c.get("relacao_com_a_versao_do_banco") == "vende_versao_que_inclui_a_do_banco":
            afirma(fs["F1"]["ofertavel"] is False,
                   "%s: F1 ofertada a quem vende versao que INCLUI a do banco" % c["dominio"])

    # ---- 3. a prosa do achado conferida contra o dado
    cadeia = " ".join(banco["o_achado_desta_passada"]["a_cadeia"])
    afirma("QUATRO experiências" in cadeia and estado["experiencias"] == 4,
           "a cadeia do achado afirma QUATRO experiencias e o banco tem %d" % estado["experiencias"])
    afirma("Três dos quatro operadores" in cadeia and estado["operadores_de_poder_publico"] == 3,
           "a cadeia afirma TRES operadores de poder publico e o banco tem %d"
           % estado["operadores_de_poder_publico"])

    titulo = banco["o_achado_desta_passada"]["titulo"]
    c_cont = ref.contagens(banco, estado)
    nenhuma = all(v == 0 for v in c_cont["com_ferramenta_ofertavel"].values())
    afirma(("NENHUM candidato tem ferramenta ofertável" in titulo) == nenhuma,
           "o titulo do achado diz que nenhum candidato tem ferramenta e as contagens dizem %s"
           % c_cont["com_ferramenta_ofertavel"])

    dominios_do_corpus = set(
        re.findall(r"[a-z0-9][a-z0-9.-]*\.(?:com\.br|com|net|org|it|br|is|fr|pt|paris|kh|cz)", corpus))
    declarado = re.search(r"mediu (\d+) domínios",
                          banco["dominios_do_corpus_nao_classificados"]["por_que_existem"])
    afirma(declarado is not None, "o bloco dos nao classificados nao declara quantos dominios o corpus mediu")
    if declarado:
        afirma(int(declarado.group(1)) == len(dominios_do_corpus),
               "o bloco diz %s dominios no corpus e a contagem deu %d"
               % (declarado.group(1), len(dominios_do_corpus)))

    classificados = set(c["dominio"] for c in banco["candidatos"])
    afirma(len(classificados) < len(dominios_do_corpus),
           "a lista classificou mais dominios do que o corpus mediu, o que nao pode acontecer")

    # ---- 4. o que esta lista NAO pode conter
    for c in banco["candidatos"]:
        afirma(c.get("contato") is None and c.get("plataforma_do_site") is None,
               "%s: contato ou plataforma preenchido, e nenhum site foi aberto" % c["dominio"])
        afirma("http" not in json.dumps(c.get("motivos", []), ensure_ascii=False),
               "%s: motivo com URL dentro; URL mora na evidencia, nao na prosa" % c["dominio"])

    # ---- 5. o texto gerado contem o que importa
    texto = ref.texto(banco, estado)
    for c in banco["candidatos"]:
        afirma(c["dominio"] in texto, "%s: nao aparece no arquivo de leitura" % c["dominio"])
    afirma("publicar" in texto and "false" in texto, "o arquivo de leitura nao diz que nada vai para o ar")

    print("teste-prospeccao: %d afirmacoes, %d falha(s)" % (afirmacoes[0], len(falhas)))
    for f in falhas:
        print("  - %s" % f)
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
