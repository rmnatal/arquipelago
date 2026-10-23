#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grava dados/artigos-ancora.json: os artigos-ancora desta ilha, inteiros.

    python3 ferramentas/gerar-artigos.py             # relatorio na tela
    python3 ferramentas/gerar-artigos.py --gravar    # grava o arquivo

O que o arquivo e: os artigos do bloco 5, cada um montado do banco pela regra de
`artigos-referencia.py` -- caixa de resposta, bloco «Monte / Compre o que esta
resposta pede», tabela de casos resolvidos, dobras, «Veja tambem», «Como
sabemos», FAQ e JSON-LD --, mais os artigos que NAO foram escritos, com o motivo
medido e o critério que destrava cada um.

`publicar: false` em todos, e o motivo nao e qualidade. Esta ilha nao tem
WordPress, nao tem Sync e nao tem /status, e o dominio nao esta na lista de
Dominios permitidos deste ambiente. Quando a casca nascer, este arquivo entra no
manifest e o snippet PHP monta a pagina a partir dele, frase a frase.

E ELE NAO GRAVA SE UM ARTIGO ESTIVER VERMELHO. Arquivo gravado de mundo
reprovado e o pior dos dois: ele parece entrega e carrega o defeito.
"""

import io
import importlib.util
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(AQUI)
SAIDA = os.path.join(BASE, "dados", "artigos-ancora.json")


def _referencia():
    caminho = os.path.join(AQUI, "artigos-referencia.py")
    spec = importlib.util.spec_from_file_location("artigos_referencia", caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def montar(art=None):
    art = art or _referencia()
    docs, falhas = art.todos()
    if falhas:
        return None, falhas

    pre = art.pre_registrados()

    # Toda contagem sai do que foi gerado, nunca digitada.
    linhas_de_tabela = sum(len(d["tabela_resumo"]) for d in docs)
    paragrafos = sum(len(x["paragrafos"]) for d in docs for x in d["dobras"])
    perguntas = sum(len(d["faq"]) for d in docs)
    valores = sum(len(d.get("divergencias") or []) for d in docs)

    documento = {
        "ilha": "jornadafly",
        "bloco": 5,
        "versao": 1,
        "publicar": False,
        "motivo_publicar_false": docs[0]["motivo_publicar_false"],
        "cumpre": "dados/especificacao-calculadoras.md, secao 7 (artigos-ancora)",
        "gerado_por": ("ferramentas/gerar-artigos.py, a partir de "
                       "ferramentas/artigos-referencia.py"),
        "le_de": ["dados/experiencias.json", "dados/esquema-banco.json",
                  "dados/constantes.json", "VOZ.md"],
        "nenhum_numero_e_digitado": (
            "Toda frase de preco destes artigos sai de ferramentas/f1-referencia.py, "
            "a mesma regra que a bancada mede. O artigo e MONTAGEM, nao redacao: "
            "artigo escrito a mao carrega numero digitado, e numero digitado "
            "envelhece calado -- no dia da recarga do banco a ferramenta publica o "
            "preco novo e o artigo continua publicando o velho, com a mesma cara de "
            "verdade. O portao do arquivo confere valor por valor contra o conjunto "
            "que o banco autoriza."),
        "o_valor_de_terceiro_tem_dono": (
            "O numero com que a ilha DISCORDA tambem vai para a tela, e e o "
            "diferencial medido: quatro dos sete ocupantes da consulta da gondola "
            "publicam valores que se contradizem sobre uma tarifa de ato oficial e "
            "nenhum diz em que dia leu. Esse valor passa so dentro da frase que "
            "nomeia quem o publicou e quando foi lido; sem o nome, e numero sem "
            "dono e o portao reprova."),
        "acentuacao": (
            "Toda frase destes artigos e destinada a TELA e por isso sai ACENTUADA. "
            "E a cicatriz da Robometria, que publicou portugues sem acento no ar. O "
            "que o portao mede e mojibake e a procedencia do valor; a regua de "
            "acentuacao foi TENTADA em tres formas em 23/10/2026 e as tres "
            "reprovaram texto correto -- o registro das tres esta na afirmacao (8) "
            "de artigos-referencia.py, para a proxima execucao nao gastar a mesma "
            "hora."),
        "resumo": {
            "artigos_escritos": len(docs),
            "artigos_pre_registrados": len(pre),
            "ferramentas_pareadas": sorted({d["ferramenta_pareada"] for d in docs}),
            "nivel_1": art.NIVEL_1,
            "nivel_2": art.NIVEL_2,
            "linhas_de_tabela": linhas_de_tabela,
            "paragrafos_de_dobra": paragrafos,
            "perguntas_de_faq": perguntas,
            "valores_de_terceiro_com_publicador": valores,
            "irmas_por_pagina": min(4, len(docs) - 1),
        },
        "artigos": docs,
        "nao_escritos": pre,
    }
    return documento, []


def main():
    art = _referencia()
    documento, falhas = montar(art)
    if falhas:
        print("REPROVADO — nada foi gravado. %d falha(s):" % len(falhas))
        for f in falhas:
            print("  - [%s] %s :: %s" % (f["artigo"], f["regra"], f["visto"]))
        return 1

    r = documento["resumo"]
    print("artigos escritos: %d  |  pre-registrados: %d" % (
        r["artigos_escritos"], r["artigos_pre_registrados"]))
    print("linhas de tabela: %d  |  paragrafos de dobra: %d  |  FAQ: %d" % (
        r["linhas_de_tabela"], r["paragrafos_de_dobra"], r["perguntas_de_faq"]))
    print("irmas por pagina: %d  |  valores de terceiro atribuidos: %d" % (
        r["irmas_por_pagina"], r["valores_de_terceiro_com_publicador"]))
    for d in documento["artigos"]:
        print("  %-16s %s" % (d["id"], d["url_planejada"]))

    if "--gravar" in sys.argv:
        with io.open(SAIDA, "w", encoding="utf-8") as f:
            json.dump(documento, f, ensure_ascii=False, indent=1, sort_keys=False)
            f.write("\n")
        print("\ngravado: %s (%d bytes)" % (SAIDA, os.path.getsize(SAIDA)))
    else:
        print("\n(nada gravado — rode com --gravar)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
