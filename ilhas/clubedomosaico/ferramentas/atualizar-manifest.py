#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recalcula o `sha256` de cada item do manifest e IMPRIME cada troca.

    python3 ferramentas/atualizar-manifest.py .            # so mostra
    python3 ferramentas/atualizar-manifest.py . --gravar   # aplica

O `--gravar` tambem aceita `--revisao N` para incrementar a revisao no mesmo
passo, e `--em AAAA-MM-DD` para a data.

POR QUE ELE IMPRIME O QUE TROCOU. Cicatriz da Aquametria, 11/09/2026: a
ferramenta equivalente de la espelhava um campo de uma fonte para outra em
silencio, e quando parou de espelhar ninguem viu — o corpo de nove paginas
trocou no ar e os nove titulos nao, porque o `titulo` do manifest nunca era
reespelhado e nenhum portao lia aquela metade. Espelho que nao imprime o que
trocou envelhece calado.

O QUE ESTA ILHA NAO PRECISA ESPELHAR, e vale registrar para nao ser copiado
sem pensar: aqui o titulo da pagina NAO mora no manifest. Ele mora em
`cdm_casca_definicao_paginas()`, que e a MESMA funcao de onde o Sync cria a
pagina e de onde a bancada monta o H1 — uma fonte so para o campo, que e o que
a cicatriz de la pede. O manifest desta ilha carrega snippet e dado, e o unico
campo derivado dele e o sha.
"""

import hashlib
import json
import os
import sys


def sha(caminho):
    with open(caminho, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def main():
    raiz = sys.argv[1] if len(sys.argv) > 1 else "."
    gravar = "--gravar" in sys.argv
    revisao = None
    em = None
    if "--revisao" in sys.argv:
        revisao = int(sys.argv[sys.argv.index("--revisao") + 1])
    if "--em" in sys.argv:
        em = sys.argv[sys.argv.index("--em") + 1]

    caminho = os.path.join(raiz, "manifest.json")
    with open(caminho, encoding="utf-8") as fh:
        manifest = json.load(fh)

    trocas = 0
    faltando = []
    for grupo in ("snippets", "conteudo", "dados"):
        for item in manifest.get(grupo, []):
            arquivo = os.path.join(raiz, item["arquivo"])
            if not os.path.exists(arquivo):
                faltando.append(item["arquivo"])
                continue
            novo = sha(arquivo)
            if item.get("sha256") != novo:
                trocas += 1
                print("  %-28s %s  ->  %s" % (item["id"], (item.get("sha256") or "—")[:12], novo[:12]))
                item["sha256"] = novo

    if faltando:
        print("\n  ARQUIVO NO MANIFEST QUE NAO EXISTE NO DISCO: " + ", ".join(faltando))
        return 1

    # E o outro sentido: arquivo publicavel no disco que o manifest nao conhece
    # nunca chega ao site, e some em silencio. A pergunta e das duas direcoes.
    no_manifest = {i["arquivo"] for g in ("snippets", "conteudo", "dados") for i in manifest.get(g, [])}
    orfaos = []
    for pasta in ("snippets",):
        for nome in sorted(os.listdir(os.path.join(raiz, pasta))):
            rel = pasta + "/" + nome
            # O Sync se pula a si mesmo por desenho: correcao nele chega pelo
            # snippet atualizador, nunca por ele mesmo. E a unica excecao, e ela
            # esta nomeada aqui em vez de virar regra geral.
            if nome == "clubedomosaico-sync.php":
                continue
            if nome.endswith(".php") and rel not in no_manifest:
                orfaos.append(rel)
    if orfaos:
        print("\n  SNIPPET NO DISCO FORA DO MANIFEST (nunca chega ao site): " + ", ".join(orfaos))
        return 1

    if revisao is not None:
        print("  revisao %s -> %s" % (manifest.get("revisao"), revisao))
        manifest["revisao"] = revisao
    if em is not None:
        manifest["atualizado_em"] = em

    if gravar:
        with open(caminho, "w", encoding="utf-8") as fh:
            json.dump(manifest, fh, ensure_ascii=False, indent=2)
            fh.write("\n")

    print("\n  %d sha recalculado(s)%s" % (trocas, " GRAVADO(S)" if gravar else " (nada gravado; use --gravar)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
