#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recalcula o sha256 de todo item do manifest, reespelha a versao de cada
snippet a partir da CONSTANTE dele, e sobe a revisao quando algo mudou.

    python3 ferramentas/atualizar-manifest.py [--revisao N]

Sem --revisao ele sobe UMA revisao se algo mudou, e nao mexe em nada se nada
mudou.

POR QUE ELE EXISTE, e por que ele IMPRIME cada troca que faz.

O manifest e o contrato que o Sync do site confere item a item: sha divergente
faz o item ser recusado no ar, e sha esquecido faz o trabalho ficar no
repositorio sem nunca chegar ao site — o defeito da secao 4 do ARQUIPELAGO.md,
que ja custou tres revisoes presas nesta fabrica. Ate 11/09/2026 esta ilha nao
tinha a ferramenta: o sha e a versao eram escritos A MAO no manifest, e o
resultado apareceu no bloco anterior, quando o manifest dizia que o R2 estava na
1.0.2 enquanto a constante do proprio snippet dizia 1.0.1. Duas copias do mesmo
fato, e a unica coisa que as separava era alguem lembrar.

A VERSAO TEM UMA FONTE SO, e ela e a constante dentro do snippet — o mesmo
principio que a casca 1.4.0 aplicou ao nome da pagina. O manifest e espelho.

E ELE IMPRIME CADA TROCA porque espelho que envelhece calado e pior que duas
copias: a Aquametria perdeu um desembarque inteiro em 11/09/2026 com uma
ferramenta que reespelhava sha e nao dizia o que tinha mudado. Quem roda este
script tem que conseguir ler, na tela, exatamente o que ele mexeu.
"""
import collections
import hashlib
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# "esquema" NAO entra: naquela chave o manifest guarda a documentacao dos
# campos, nao uma lista de arquivos.
SECOES = ("snippets", "conteudo", "dados", "ferramentas")

CONSTANTE = re.compile(r"define\(\s*'(ROBOMETRIA_[A-Z0-9_]+_VERSAO)',\s*'([^']+)'")


def sha256(caminho):
    h = hashlib.sha256()
    with open(caminho, "rb") as f:
        for pedaco in iter(lambda: f.read(65536), b""):
            h.update(pedaco)
    return h.hexdigest()


def versao_do_snippet(caminho):
    """A versao declarada pela constante do proprio snippet, ou None.

    Deliberadamente nao le o cabecalho em prosa: o cabecalho e historico e tem
    uma linha por versao. Quem manda e a constante, que e o que o codigo usa.
    """
    with io.open(caminho, encoding="utf-8") as f:
        achado = CONSTANTE.search(f.read())
    return achado.group(2) if achado else None


def main():
    alvo = None
    if "--revisao" in sys.argv:
        alvo = int(sys.argv[sys.argv.index("--revisao") + 1])

    caminho = os.path.join(RAIZ, "manifest.json")
    with io.open(caminho, encoding="utf-8") as f:
        m = json.load(f, object_pairs_hook=collections.OrderedDict)

    mudados, versoes, ausentes, mudos, listados = [], [], [], [], set()

    # QUEM DECIDE QUAIS CAMPOS ESTA FERRAMENTA ESPELHA E O PROPRIO MANIFEST, na
    # chave "esquema" — nao uma lista escrita aqui. A primeira versao deste
    # script gravou sha256 nas 20 ferramentas de bancada, e a secao "ferramentas"
    # do esquema nao declara esse campo: seria um campo inventado, dentro do
    # arquivo que existe justamente para ser contrato, e ainda faria a revisao
    # subir por mudanca que nunca vai ao site. Espelhar so o que o contrato pede
    # e a mesma regra que o resto da ilha ja segue.
    campos = {s: set(d) for s, d in (m.get("esquema") or {}).items()
              if isinstance(d, dict)}

    for secao in SECOES:
        tem_sha = "sha256" in campos.get(secao, set())
        tem_versao = "versao" in campos.get(secao, set())
        for item in m.get(secao) or []:
            arq = item.get("arquivo")
            if not arq:
                continue
            listados.add(arq)
            inteiro = os.path.join(RAIZ, arq)
            if not os.path.exists(inteiro):
                ausentes.append(arq)
                continue

            if tem_sha:
                novo = sha256(inteiro)
                if item.get("sha256") != novo:
                    mudados.append((arq, (item.get("sha256") or "")[:8], novo[:8]))
                    item["sha256"] = novo

            # A constante manda na versao; o manifest e espelho dela.
            if tem_versao and arq.endswith(".php"):
                v = versao_do_snippet(inteiro)
                if v is None:
                    mudos.append(arq)
                elif item.get("versao") != v:
                    versoes.append((arq, item.get("versao"), v))
                    item["versao"] = v

    orfaos = []
    for pasta in SECOES:
        base = os.path.join(RAIZ, pasta)
        if not os.path.isdir(base):
            continue
        for nome in sorted(os.listdir(base)):
            rel = pasta + "/" + nome
            if os.path.isfile(os.path.join(base, nome)) and rel not in listados:
                orfaos.append(rel)

    for arq, antes, depois in mudados:
        print("  sha     %-44s %s -> %s" % (arq, antes or "(vazio)", depois))
    for arq, antes, depois in versoes:
        print("  VERSAO  %-44s %s -> %s" % (arq, antes, depois))
    for arq in ausentes:
        print("  AUSENTE no disco, mas listado no manifest: " + arq)
    for arq in mudos:
        print("  SEM CONSTANTE de versao (a versao do manifest nao tem espelho): " + arq)
    for arq in orfaos:
        print("  fora do manifest: " + arq)

    if alvo is not None:
        m["revisao"] = alvo
    elif mudados or versoes:
        m["revisao"] = m["revisao"] + 1

    if mudados or versoes or alvo is not None:
        from datetime import date
        m["atualizado_em"] = date.today().isoformat()
        with io.open(caminho, "w", encoding="utf-8") as f:
            json.dump(m, f, ensure_ascii=False, indent=2)
            f.write("\n")

    print("\n  %d item(ns) com sha novo, %d versao(oes) reespelhada(s), revisao %s"
          % (len(mudados), len(versoes), m["revisao"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
