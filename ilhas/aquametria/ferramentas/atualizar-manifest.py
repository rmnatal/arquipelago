# -*- coding: utf-8 -*-
"""Recalcula o sha256 de todo item do manifest e sobe a revisao quando algo mudou.

O manifest e o contrato que o Sync do site confere item a item: sha divergente
faz o item ser recusado no ar. Ate hoje o sha era atualizado a mao, e e o tipo de
passo que se esquece em silencio — o item fica no repositorio e nunca chega ao
site, que e exatamente o defeito da secao 4 do ARQUIPELAGO.md.

    python3 ferramentas/atualizar-manifest.py [--revisao N]

Sem --revisao ele sobe UMA revisao se algum sha mudou, e nao mexe em nada se
nada mudou. Nunca inventa item: arquivo que nao esta no manifest continua fora, e
o script avisa.

ELE TAMBEM RELE O TITULO DO FRONT MATTER, desde 11/09/2026, e essa linha custou
um desembarque inteiro. O `titulo` do manifest e o que o Sync grava em
post_title; o front matter do .md e o que TODA a bancada renderiza. Ate hoje so
o sha era recalculado, entao o dia em que os nove titulos foram reescritos o
manifest continuou com os antigos: 293 afirmacoes ficaram verdes na bancada, o
Sync respondeu "18 aplicado(s)", o corpo das nove paginas mudou no ar — e o H1 e
o <title> das nove continuaram sendo os de antes. Duas fontes para o mesmo dado,
e so uma delas sendo atualizada, e um defeito que nenhum portao que renderiza do
.md pode enxergar. O front matter manda; o manifest o espelha.
"""
import collections
import hashlib
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# "esquema" NAO entra: naquela chave o manifest guarda a documentacao dos campos,
# nao uma lista de arquivos.
SECOES = ("snippets", "conteudo", "dados", "ferramentas")


VERSAO_CONSTANTE = re.compile(
    r"define\(\s*'AQUAMETRIA_[A-Z0-9_]+_VERSAO'\s*,\s*'([^']+)'\s*\)")


def versao_do_snippet(caminho):
    """A versao que o PROPRIO snippet define, ou None se ele nao definir nenhuma.

    Le a constante, nunca o cabecalho em prosa: o docblock e texto e envelhece
    sem que nada quebre, a constante e o que o codigo usa.
    """
    with io.open(caminho, encoding="utf-8") as f:
        achado = VERSAO_CONSTANTE.search(f.read(20000))
    return achado.group(1) if achado else None


def frente(caminho):
    """Os campos do front matter YAML que o manifest espelha.

    Deliberadamente simples: o front matter destas paginas e um mapa raso de
    escalares e uma lista (`fontes`), e nao vale trazer um parser de YAML para
    dentro da fabrica so por causa disto. O que importa e desescapar a aspa do
    escalar entre aspas duplas — foi por nao desescapar que a bancada mediu
    `\\"1 W por litro\\"` num titulo que no ar sai com aspas curvas."""
    with io.open(caminho, encoding="utf-8") as f:
        texto = f.read()
    if not texto.startswith("---"):
        return {}
    fim = texto.find("\n---", 3)
    if fim < 0:
        return {}
    campos = {}
    for linha in texto[3:fim].split("\n"):
        if not linha or linha[0] in " \t#" or ":" not in linha:
            continue
        chave, _, valor = linha.partition(":")
        valor = valor.strip()
        if len(valor) >= 2 and valor[0] == '"' and valor[-1] == '"':
            valor = valor[1:-1].replace('\\"', '"').replace("\\\\", "\\")
        campos[chave.strip()] = valor
    return campos


def sha256(caminho):
    h = hashlib.sha256()
    with open(caminho, "rb") as f:
        for pedaco in iter(lambda: f.read(65536), b""):
            h.update(pedaco)
    return h.hexdigest()


def main():
    alvo = None
    if "--revisao" in sys.argv:
        alvo = int(sys.argv[sys.argv.index("--revisao") + 1])

    caminho = os.path.join(RAIZ, "manifest.json")
    with io.open(caminho, encoding="utf-8") as f:
        m = json.load(f, object_pairs_hook=collections.OrderedDict)

    mudados, ausentes, listados = [], [], set()
    titulos = []
    divergentes = []
    for secao in SECOES:
        for item in m.get(secao) or []:
            arq = item.get("arquivo")
            if not arq:
                continue
            listados.add(arq)
            inteiro = os.path.join(RAIZ, arq)
            if not os.path.exists(inteiro):
                ausentes.append(arq)
                continue
            novo = sha256(inteiro)
            if item.get("sha256") != novo:
                mudados.append((item.get("id"), arq, (item.get("sha256") or "")[:8], novo[:8]))
                item["sha256"] = novo

            # A CONSTANTE do snippet manda na versao; o manifest e espelho dela.
            # Trazido do Clube do Mosaico em 12/09/2026, que pagou a mesma conta
            # no mesmo dia: o manifest dizia casca 1.4.0 e o arquivo definia
            # 1.5.0. O sha estava certo e o site nunca esteve errado — envelheceu
            # a ETIQUETA, que e por onde todo relatorio le o que esta no ar.
            # Aqui a divergencia PARA o script em vez de ser reespelhada calada:
            # versao e decisao de quem escreveu o bloco, e um espelho automatico
            # esconderia o esquecimento em vez de cobra-lo.
            if secao == "snippets" and arq.endswith(".php"):
                constante = versao_do_snippet(inteiro)
                if constante and item.get("versao") and item["versao"] != constante:
                    divergentes.append((arq, item.get("versao"), constante))

            # O front matter manda no titulo; o manifest e espelho dele.
            if secao == "conteudo" and arq.endswith(".md"):
                campos = frente(inteiro)
                titulo = campos.get("titulo")
                if titulo and item.get("titulo") != titulo:
                    titulos.append((arq, item.get("titulo"), titulo))
                    item["titulo"] = titulo

    orfaos = []
    for pasta in ("snippets", "conteudo", "dados", "ferramentas"):
        base = os.path.join(RAIZ, pasta)
        if not os.path.isdir(base):
            continue
        for nome in sorted(os.listdir(base)):
            rel = pasta + "/" + nome
            if os.path.isfile(os.path.join(base, nome)) and rel not in listados:
                orfaos.append(rel)

    for id_, arq, antes, depois in mudados:
        print("  sha  %-42s %s -> %s" % (arq, antes or "(vazio)", depois))
    for arq, antes, depois in titulos:
        print("  TITULO %-40s %r -> %r" % (arq, antes, depois))
    for arq in ausentes:
        print("  AUSENTE no disco, mas listado no manifest: " + arq)
    for arq in orfaos:
        print("  fora do manifest: " + arq)

    if divergentes:
        print("")
        for arq, no_manifest, na_constante in divergentes:
            print("  VERSAO DIVERGENTE  %-44s manifest %s, constante %s"
                  % (arq, no_manifest, na_constante))
        print("\n  NADA FOI GRAVADO. A versao do manifest e a etiqueta por onde todo")
        print("  relatorio le o que esta no ar; deixa-la para tras e publicar certo e")
        print("  contar errado. Atualize a versao E a descricao do item no manifest.")
        return 1

    if alvo is not None:
        m["revisao"] = alvo
    elif mudados or titulos:
        m["revisao"] = m["revisao"] + 1

    if mudados or titulos or alvo is not None:
        from datetime import date
        m["atualizado_em"] = date.today().isoformat()
        with io.open(caminho, "w", encoding="utf-8") as f:
            json.dump(m, f, ensure_ascii=False, indent=2)
            f.write("\n")

    print("\n  %d item(ns) com sha novo, %d titulo(s) reespelhado(s), revisao %s"
          % (len(mudados), len(titulos), m["revisao"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
