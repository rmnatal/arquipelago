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
import re
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
    # `ferramentas` ENTROU AQUI EM 12/09/2026, e o motivo e a propria cicatriz
    # do cabecalho deste arquivo. O grupo declara `sha256` no esquema do manifest
    # desde que nasceu, e nenhuma linha o recalculava: quem mexesse numa
    # ferramenta de bancada deixava para tras uma etiqueta que dizia o hash de
    # uma versao que nao existe mais. Bancada nao vai para o site, entao isso
    # nunca quebraria uma pagina — e e exatamente por isso que envelheceria
    # calado, que e o defeito, nao a consequencia. Campo declarado sem quem o
    # espelhe e promessa; ou se recalcula, ou sai do esquema.
    for grupo in ("snippets", "conteudo", "dados", "ferramentas"):
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

    # AS QUATRO CONFERENCIAS ABAIXO ACUMULAM, E NAO SE INTERROMPEM, e isto foi
    # medido doendo em 12/09/2026, no bloco do GA4: o `return 1` do descasamento
    # de versao saia ANTES da conferencia de ferramenta orfa, e com isso o
    # `mutacoes-ga4.py` recem-escrito ficou fora do manifest sem uma linha de
    # aviso — numa execucao em que a versao do snippet tinha acabado de subir,
    # que e EXATAMENTE quando ferramenta nova costuma nascer. O portao existia,
    # estava certo, e era inalcancavel: a conferencia que roda primeiro escondia
    # a que interessava. Portao que para no primeiro achado nao mede a entrada
    # inteira — mede o primeiro erro dela, e faz quem conserta descobrir os
    # outros um por rodada, quando descobre.
    problemas = []

    if faltando:
        problemas.append("  ARQUIVO NO MANIFEST QUE NAO EXISTE NO DISCO: " + ", ".join(faltando))

    # A VERSAO DO MANIFEST x A CONSTANTE DENTRO DO SNIPPET.
    #
    # Achado do bloco da F1, em 11/09/2026: o manifest dizia casca 1.4.0 e o
    # arquivo definia CDM_CASCA_VERSAO '1.5.0'. O sha estava certo, entao o
    # Sync aplicou os bytes certos e o site ficou correto — o que envelheceu foi
    # a ETIQUETA, que e por onde qualquer um (e qualquer relatorio) le o que esta
    # no ar. O bloco anterior subiu a casca e reespelhou sha e descricao, e
    # esqueceu a versao, porque NENHUM portao lia essa metade. E a mesma familia
    # da cicatriz que este arquivo ja carrega no cabecalho: espelho que nao
    # confere um campo deixa aquele campo apodrecer calado.
    divergem = []
    for item in manifest.get("snippets", []):
        arquivo = os.path.join(raiz, item["arquivo"])
        with open(arquivo, encoding="utf-8") as fh:
            fonte = fh.read()
        achado = re.search(r"define\(\s*'CDM_[A-Z0-9_]*VERSAO'\s*,\s*'([^']+)'", fonte)
        if not achado:
            divergem.append("%s: o snippet nao define constante de versao" % item["id"])
            continue
        if achado.group(1) != item.get("versao"):
            divergem.append("%s: manifest %s, snippet %s" % (item["id"], item.get("versao"), achado.group(1)))
    if divergem:
        problemas.append("  VERSAO DO MANIFEST DIFERENTE DA CONSTANTE DO SNIPPET:\n"
                         + "\n".join("    " + l for l in divergem))

    # E o outro sentido: arquivo publicavel no disco que o manifest nao conhece
    # nunca chega ao site, e some em silencio. A pergunta e das duas direcoes.
    no_manifest = {i["arquivo"] for g in ("snippets", "conteudo", "dados", "ferramentas")
                   for i in manifest.get(g, [])}
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
        problemas.append("  SNIPPET NO DISCO FORA DO MANIFEST (nunca chega ao site): " + ", ".join(orfaos))

    # A BANCADA TAMBEM E INVENTARIO, e em 12/09/2026 ela estava pela METADE: o
    # manifest listava 9 das 18 ferramentas, e as que faltavam incluiam
    # `teste-f1.php` e `teste-f2.php`, que sao os dois portoes principais da
    # ilha. Ninguem tinha mentido — o grupo so nunca foi cobrado nas duas
    # direcoes, que e a forma silenciosa do mesmo defeito que a secao 8 do
    # contrato descreve para contagem de tela: categoria mostrada sem arquivo e
    # promessa, arquivo sem categoria e trabalho que a tela nunca ve. Ferramenta
    # nao vai para o site, entao um esquecimento aqui nao quebra pagina; quebra
    # a capacidade de qualquer relatorio dizer com o que esta ilha se verifica.
    ferramentas_fora = []
    pasta_f = os.path.join(raiz, "ferramentas")
    if os.path.isdir(pasta_f):
        for nome in sorted(os.listdir(pasta_f)):
            rel = "ferramentas/" + nome
            if nome.endswith((".py", ".php", ".mjs")) and rel not in no_manifest:
                ferramentas_fora.append(rel)
    if ferramentas_fora:
        problemas.append("  FERRAMENTA NO DISCO FORA DO MANIFEST: " + ", ".join(ferramentas_fora))

    # Aqui, e so aqui, a ferramenta desiste — com a lista INTEIRA na tela, para
    # quem conserta consertar tudo numa passada em vez de uma por rodada.
    if problemas:
        print("\n%d problema(s), e nenhum deles escondeu os outros:\n" % len(problemas))
        for linha in problemas:
            print(linha)
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
