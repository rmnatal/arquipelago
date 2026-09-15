#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grava dados/f1-respostas.json: o dominio de resposta INTEIRO da F1.

    python3 ferramentas/gerar-f1.py             # relatorio na tela
    python3 ferramentas/gerar-f1.py --gravar    # grava o arquivo

O que o arquivo e: as 144 respostas da F1 (24 montagens x o pedido vazio mais as
5 impedancias de modulo do vocabulario), cada uma ja em frase acentuada, mais a
TABELA PRE-RENDERIZADA da secao 5 do ARQUIPELAGO.md -- os casos resolvidos que um
modelo de linguagem le sem preencher formulario nenhum.

publicar: false HOJE, e o motivo nao e qualidade do arquivo. Esta ilha nao tem
WordPress: nao ha manifest.json, nao ha Sync e nao ha /status. Quando a casca
nascer (bloco 3b), este arquivo entra no manifest e o snippet PHP monta a pagina
a partir dele -- e ate la dizer que ele esta no ar seria inventar.

O RMS DO FALANTE NAO E DIMENSAO DESTE ARQUIVO, e a razao merece uma linha: hoje a
F1 nao AFIRMA nada a partir do RMS -- o criterio do fabricante esta pendente em
constantes.json e constante pendente nao entra em formula publicada. Entao o RMS
entra na resposta como numero do visitante, nao como eixo de estado, e a bancada
mede as duas metades: com RMS e sem.
"""

import importlib.util
import io
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(AQUI)


def _referencia():
    caminho = os.path.join(AQUI, "f1-referencia.py")
    spec = importlib.util.spec_from_file_location("f1_referencia", caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def documento(f1, banco=None, esquema=None, doc_casos=None, constantes=None):
    """Sem argumento, le tudo do disco. Com argumento, monta o documento sobre o
    mundo que voce entregar -- e por essa porta que ferramentas/mutacoes-f1.py
    FABRICA o mundo que o banco ainda nao tem (secao 8: todo caso que o esquema
    permite e o banco ainda nao tem e um caso que a regua trata hoje)."""
    esquema = esquema if esquema is not None else f1.carregar_esquema()
    doc_casos = doc_casos if doc_casos is not None else f1.carregar_casos()
    banco = banco if banco is not None else f1.carregar_modulos()["itens"]
    constantes = constantes if constantes is not None else f1.carregar_constantes()

    respostas = f1.todas_as_respostas(banco=banco, esquema=esquema, doc_casos=doc_casos,
                                      constantes=constantes)
    tabela = f1.tabela_de_exemplos(respostas)

    return {
        "ilha": "ohmetria",
        "ferramenta": "F1",
        "bloco": "4",
        "titulo": "Qual módulo fecha com o seu falante",
        "gerado_por": "ferramentas/gerar-f1.py, a partir de ferramentas/f1-referencia.py",
        "gerado_em": "2026-09-15",
        "publicar": False,
        "por_que_publicar_false": (
            "A ilha ainda nao tem WordPress: sem manifest, sem Sync e sem /status, nada aqui "
            "pode ir ao ar nem ser conferido no ar. Vira true no bloco 3b, junto com a casca."),
        "o_que_este_arquivo_e": (
            "O dominio de resposta da F1, enumerado. Cada estado de entrada -- montagem x "
            "impedancia de modulo pedida, mais o pedido vazio -- com o veredito, as ligacoes, "
            "a prestacao de contas do banco, o bloco de compra e o 'como sabemos'. Nao e banco "
            "de produto: o unico banco que ele le e dados/modulos.json, que hoje tem 0 itens."),
        "o_que_a_F1_nao_afirma_hoje": [
            "nada sobre o MERCADO: enquanto o vocabulario impedancia_de_modulo tiver entrada "
            "sem lastro no banco, a unica frase verdadeira e 'nenhum modulo do nosso banco'",
            "nenhum teto de RMS: criterio-rms-modulo-nao-passa-do-falante esta pendente",
            "nenhuma recomendacao de produto: o bloco de compra serve busca derivada da "
            "resposta, e diz na tela que nao e recomendacao",
        ],
        "total_de_estados": len(respostas),
        "modulos_no_banco": len(banco),
        "montagens": len(tabela),
        "tabela_de_exemplos": tabela,
        "respostas": respostas,
    }


def main():
    f1 = _referencia()
    doc = documento(f1)
    if "--gravar" in sys.argv:
        destino = os.path.join(BASE, "dados", "f1-respostas.json")
        with io.open(destino, "w", encoding="utf-8") as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
        print("gravado dados/f1-respostas.json")
    print("%d estados, %d montagens na tabela pre-renderizada, %d modulos no banco" % (
        doc["total_de_estados"], doc["montagens"], doc["modulos_no_banco"]))
    vereditos = {}
    for r in doc["respostas"]:
        vereditos[r["veredito"]["codigo"]] = vereditos.get(r["veredito"]["codigo"], 0) + 1
    for codigo in sorted(vereditos):
        print("  %-22s %3d" % (codigo, vereditos[codigo]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
