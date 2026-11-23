#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PORTAO DA DATA DO CODIGO DE CADA PAGINA — nasceu em 23/11/2026. Sem rede.

    python3 ferramentas/teste-datas-de-codigo.py

O QUE ELE EXISTE PARA FECHAR. A segunda metade do item 2 do despacho da ronda de
23/11/2026 pedia *"o portao de ar cobrando, por URL, que ela nao seja mais antiga
que a revisao do `manifest.json` que a desembarcou"*. A execucao da tarde fechou a
primeira metade — a data de uma pagina e a MAIS RECENTE entre as datas de tudo de
que ela e feita — e escreveu, pela 18.3, que a segunda nao cabia porque **a data
em que uma pagina muda quando o CODIGO dela muda nao existia em lugar nenhum**: o
`manifest.json` tinha UM `atualizado_em` para a revisao inteira, e revisao inteira
nao distingue a pagina que mudou da que nao mudou.

O CAMINHO INTEIRO, E CADA DEGRAU TEM UM PORTAO:

  manifest.json      `mudou_em` por item, datado no gesto em que o `sha256` troca
                     (`atualizar-manifest.py`), e `renderiza` por snippet
         |
         v
  gerar-datas-de-codigo.py   compila os dois em `dados/datas-de-codigo.json`
         |                   ESTE ARQUIVO e o portao deste degrau
         v
  Sync -> option      porque `publicar: true` (a casca NAO le o manifest)
         |
         v
  casca               compoe com as outras fontes pelo MAIS RECENTE
         |            (portao: `teste-data-da-pagina.php`)
         v
  JSON-LD no ar       (portao: `conferir-no-ar.py`, por URL)

O QUE ESTE PORTAO MEDE, e nenhuma data e digitada aqui:

  1. O ARQUIVO NO DISCO E O QUE O MANIFEST DE HOJE IMPLICA. Arquivo gerado que
     envelhece e a 20.12 ao pe da letra: "arquivo gerado nao e fonte".
  2. A `*` DA CASCA EXPANDE PARA TODAS as paginas, e a uniao dos `renderiza` e
     EXATAMENTE o conjunto de slugs que a ilha serve. Slug sem renderizador
     REPROVA; slug declarado que nao existe REPROVA.
  3. A DATA DE UMA PAGINA E O MAXIMO dos `mudou_em` dos itens que a renderizam —
     nao o primeiro, nao o ultimo, nao o da casca. O mundo com datas FORA DE
     ORDEM e fabricado, porque no manifest de hoje os seis snippets mudaram no
     MESMO dia e um `max()` errado passaria verde (secao 8: "regua escrita para
     um mundo que nunca aconteceu nasce errada sem poder falhar").
  4. `mudou_em: null` NAO VIRA DATA, e a pagina sai com `codigo_nao_sabido`.
     `null` e "o git deste clone nao soube semear", nunca "nao mudou nunca".
  5. O COMPILADOR E FUNCAO PURA: duas chamadas, mesmo byte, e NENHUMA data de
     hoje entra num manifest que nao tem data de hoje. Se ele estampasse a data
     da geracao, o `sha256` do arquivo trocaria todo dia e a revisao subiria por
     nada.
  6. O ESPELHO `sha256` DO MANIFEST ESTA EM DIA com os arquivos do repositorio,
     e TODO item tem o campo `mudou_em`. *(A primeira versao desta linha dizia
     que `atualizar-manifest.py` "nao e descoberto pela bancada" e isso e FALSO:
     medido na passada que escreveu este arquivo, `bancada.py` roda
     `atualizar-manifest.py --conferir` e `gerar-datas-de-codigo.py --conferir`
     entre os 64 portoes sem rede — ela descobre `--conferir` de ferramenta que
     escreve, nao so os prefixos `teste-`/`validar-`/`mutacoes-`. A afirmacao
     daqui nao e redundante por isso: ela e a que NOMEIA o item fora do espelho
     dentro deste assunto, e a do `mudou_em` presente nao existe la.)*

O QUE ELE NAO MEDE, e a linha esta aqui para ninguem ler verde a mais: ele nao
abre o ar. Se a option nao viajar, ou se o snippet carregado for velho, quem
pega e `conferir-no-ar.py`.
"""

import copy
import hashlib
import importlib.util
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)


def modulo(nome_arquivo, nome_modulo):
    """Importa uma ferramenta desta ilha cujo nome tem hifen."""
    caminho = os.path.join(AQUI, nome_arquivo)
    spec = importlib.util.spec_from_file_location(nome_modulo, caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


G = modulo("gerar-datas-de-codigo.py", "gerar_datas_de_codigo")

falhas = []
notas = []
afirmacoes = 0


def diz(cond, msg):
    global afirmacoes
    afirmacoes += 1
    if not cond:
        falhas.append(msg)


def nota(msg):
    notas.append(msg)


def snip(ident, mudou_em, renderiza, versao="1.0.0"):
    return {"id": ident, "arquivo": "snippets/%s.php" % ident, "sha256": "x" * 64,
            "versao": versao, "renderiza": renderiza, "mudou_em": mudou_em}


def main():
    manifest = G.carregar(os.path.join(ILHA, "manifest.json"))
    slugs, problemas = G.slugs_que_a_ilha_serve()

    # ---------------------------------------------------------------- 1 e 2
    diz(not problemas,
        "as fontes dos slugs reclamaram: %s" % "; ".join(problemas))
    diz(len(slugs) == len(set(slugs)) and len(slugs) >= 1,
        "a lista de slugs da ilha veio vazia ou com repeticao: %r" % slugs)
    nota("a ilha serve %d slug(s): %s" % (len(slugs), ", ".join(slugs)))

    dado, probs = G.compilar(manifest, slugs)
    diz(dado is not None,
        "o manifest de hoje nao compila: %s" % "; ".join(probs))
    if dado is None:
        encerrar()
        return 1

    arq = os.path.join(ILHA, "dados", "datas-de-codigo.json")
    diz(os.path.exists(arq),
        "dados/datas-de-codigo.json nao existe, e e ele que viaja para o ar")
    if os.path.exists(arq):
        no_disco = open(arq, encoding="utf-8").read()
        esperado = json.dumps(dado, ensure_ascii=False, indent=2) + "\n"
        diz(no_disco == esperado,
            "dados/datas-de-codigo.json nao e o que o manifest de hoje implica — "
            "arquivo gerado que envelhece e a 20.12 ao pe da letra. Rode "
            "ferramentas/gerar-datas-de-codigo.py")

    diz(set(dado["paginas"].keys()) == set(slugs),
        "o arquivo cobre %d pagina(s) e a ilha serve %d"
        % (len(dado["paginas"]), len(slugs)))

    casca = [i for i in manifest["snippets"] if i.get("renderiza") == ["*"]]
    diz(len(casca) == 1,
        "esperava EXATAMENTE um item com `renderiza: [\"*\"]` (a casca, que e "
        "`escopo: global` e desenha toda pagina) e achei %d" % len(casca))
    if casca:
        ident = casca[0]["id"]
        todas = all(any(i["id"] == ident for i in l["itens"])
                    for l in dado["paginas"].values())
        diz(todas, "a `*` de %s nao alcancou todas as paginas" % ident)
        nota("a `*` de %s alcanca as %d paginas" % (ident, len(dado["paginas"])))

    for slug, linha in dado["paginas"].items():
        diz(len(linha["itens"]) >= 1,
            "o slug %r saiu sem item nenhum, e o compilador tinha de ter reprovado"
            % slug)
    nota("datas por pagina: " + ", ".join(
        "%s %s" % (s, l["data"] or "null") for s, l in dado["paginas"].items()))

    # ------------------------------------------------------- 3: o MAXIMO
    # As datas sao FABRICADAS e fora de ordem de proposito: no manifest de hoje
    # os seis snippets mudaram no MESMO dia, entao um `max()` errado (primeiro,
    # ultimo, ou o da casca) passaria verde sobre o dado real.
    reais = ["inicio", "autonomia-patinete-eletrico", "veiculos"]
    m1 = {"ilha": "rodametria", "snippets": [
        snip("casca", "2026-03-02", ["*"]),
        snip("ferramenta", "2026-01-01", ["autonomia-patinete-eletrico"]),
        snip("produto", "2026-09-09", ["veiculos"]),
    ]}
    d1, p1 = G.compilar(m1, reais)
    diz(d1 is not None, "o mundo das datas fora de ordem nao compilou: %s" % p1)
    if d1:
        diz(d1["paginas"]["veiculos"]["data"] == "2026-09-09",
            "a pagina com item de 2026-09-09 e casca de 2026-03-02 devia servir "
            "2026-09-09 (o MAXIMO) e serviu %r" % d1["paginas"]["veiculos"]["data"])
        diz(d1["paginas"]["autonomia-patinete-eletrico"]["data"] == "2026-03-02",
            "a pagina cujo proprio item e de 2026-01-01 e cuja casca e de "
            "2026-03-02 devia servir a da CASCA, e serviu %r"
            % d1["paginas"]["autonomia-patinete-eletrico"]["data"])
        diz(d1["paginas"]["inicio"]["data"] == "2026-03-02",
            "a pagina que so a casca renderiza devia servir a data da casca e "
            "serviu %r" % d1["paginas"]["inicio"]["data"])

    # --------------------------------------------- 4: `null` nao vira data
    m2 = {"ilha": "rodametria", "snippets": [
        snip("casca", None, ["*"]),
        snip("ferramenta", None, ["autonomia-patinete-eletrico"]),
        snip("produto", "2026-09-09", ["veiculos"]),
    ]}
    d2, _ = G.compilar(m2, reais)
    diz(d2 is not None, "o mundo do `mudou_em: null` nao compilou")
    if d2:
        diz(d2["paginas"]["inicio"]["data"] is None
            and d2["paginas"]["inicio"].get("codigo_nao_sabido") is True,
            "pagina cujos itens todos tem `mudou_em: null` devia sair com "
            "`data: null` e `codigo_nao_sabido: true`, e saiu %r"
            % d2["paginas"]["inicio"])
        diz(d2["paginas"]["veiculos"]["data"] == "2026-09-09"
            and "codigo_nao_sabido" not in d2["paginas"]["veiculos"],
            "o `null` da casca contaminou a pagina que TEM data: %r"
            % d2["paginas"]["veiculos"])
        diz("2026-" not in json.dumps(d2["paginas"]["inicio"]["data"]),
            "o `null` virou data em algum lugar")

    # ------------------------------------------------- 5: pureza do compilador
    a, _ = G.compilar(copy.deepcopy(m1), reais)
    b, _ = G.compilar(copy.deepcopy(m1), reais)
    diz(json.dumps(a, ensure_ascii=False) == json.dumps(b, ensure_ascii=False),
        "duas compilacoes do MESMO manifest sairam diferentes — o compilador nao "
        "e funcao pura, e o `sha256` do arquivo passaria a trocar sozinho")
    import datetime
    hoje = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    diz(hoje not in json.dumps(a, ensure_ascii=False),
        "a data de HOJE (%s) entrou num arquivo compilado de um manifest que nao "
        "a tem: o compilador esta lendo o relogio, e com isso o `sha256` dele "
        "trocaria todo dia e a revisao subiria por nada" % hoje)

    # ------------------------------------------- 6: o espelho sha256 em dia
    fora = []
    for grupo in ("snippets", "conteudo", "dados"):
        for item in manifest.get(grupo, []):
            caminho = os.path.join(ILHA, item["arquivo"])
            if not os.path.exists(caminho):
                fora.append("%s:%s AUSENTE" % (grupo, item["id"]))
                continue
            with open(caminho, "rb") as f:
                real = hashlib.sha256(f.read()).hexdigest()
            if item.get("sha256") != real:
                fora.append("%s:%s" % (grupo, item["id"]))
            if "mudou_em" not in item:
                fora.append("%s:%s sem `mudou_em`" % (grupo, item["id"]))
    diz(not fora,
        "o manifest nao espelha o repositorio em %s — rode "
        "ferramentas/atualizar-manifest.py" % ", ".join(fora))

    # --------------------------------------------------- as MUTACOES, 6 delas
    def reprova(manifest_torto, slugs_do_mundo, porque):
        d, p = G.compilar(manifest_torto, slugs_do_mundo)
        diz(d is None and bool(p), porque)

    # MUTACAO 1 — E A PRIMEIRA VERSAO DELA NAO MORDIA, pelo motivo que vale
    # escrito: o mundo tinha a casca com `*` e um slug novo, e `*` expande para
    # TODAS as paginas, inclusive a nova — ou seja, **enquanto existir um item
    # global, pagina orfa de renderizador nao existe por construcao.** O mundo em
    # que a afirmacao morde e o SEM item global, e e ele que esta aqui. A regra
    # continua valendo e continua valendo a pena: o dia em que a casca deixar de
    # ser global, ou em que um segundo grupo de paginas nascer de um snippet que
    # ninguem declarou, e este ramo que pega.
    reprova({"ilha": "x", "snippets": [snip("produto", "2026-01-01", ["veiculos"])]},
            reais,
            "MUTACAO 1 PASSOU: slug que item nenhum renderiza foi aceito. Pagina "
            "nova tem de obrigar a declaracao a crescer no mesmo dia")
    reprova({"ilha": "x", "snippets": [snip("casca", "2026-01-01", ["*"]),
                                       snip("fantasma", "2026-01-01", ["nao-existe"])]},
            reais,
            "MUTACAO 2 PASSOU: item que declara renderizar slug inexistente foi "
            "aceito, e e assim que uma declaracao fica apontando para pagina morta")
    reprova({"ilha": "x", "snippets": [
                {"id": "sem-campo", "arquivo": "a.php", "sha256": "x", "versao": "1"},
                snip("casca", "2026-01-01", ["*"])]},
            reais,
            "MUTACAO 3 PASSOU: snippet SEM `renderiza` foi aceito, e sem o campo o "
            "`mudou_em` dele nao alcanca URL nenhuma")
    reprova({"ilha": "x", "snippets": [snip("casca", "2026-01-01", ["*"]),
                                       snip("vazio", "2026-01-01", [])]},
            reais,
            "MUTACAO 4 PASSOU: `renderiza` vazio foi aceito")
    reprova({"ilha": "x", "snippets": [snip("casca", "2026-01-01", ["*"]),
                                       snip("texto", "2026-01-01", "inicio")]},
            reais,
            "MUTACAO 5 PASSOU: `renderiza` que e string e nao lista foi aceito — "
            "iterar a string renderizaria uma pagina por LETRA")
    reprova({"ilha": "x", "snippets": [snip("casca", "2026-01-01", ["*", "inicio"])]},
            reais,
            "MUTACAO 6 PASSOU: `*` misturado com slug nomeado foi aceito, e a "
            "declaracao fica ambigua sobre o que ela quer dizer")

    encerrar()
    return 1 if falhas else 0


def encerrar():
    print("PORTAO DA DATA DO CODIGO DE CADA PAGINA — RODAMETRIA (sem rede)")
    for n in notas:
        print("  . " + n)
    for f in falhas:
        print("FALHA: " + f)
    print("\n%d afirmacao(oes), %d falha(s)." % (afirmacoes, len(falhas)))
    print("APROVADO" if not falhas else "REPROVADO")


if __name__ == "__main__":
    sys.exit(main())
