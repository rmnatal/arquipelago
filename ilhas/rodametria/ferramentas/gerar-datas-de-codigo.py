#!/usr/bin/env python3
"""
A DATA DO CODIGO DE CADA PAGINA, DO MANIFEST PARA O AR — a segunda metade do
item 2 do despacho da ronda de 23/11/2026.

    python3 ferramentas/gerar-datas-de-codigo.py            # escreve
    python3 ferramentas/gerar-datas-de-codigo.py --conferir  # nao escreve; falha se divergir

O QUE ESTE ARQUIVO EXISTE PARA RESOLVER
=======================================

O despacho pedia *"o portao de ar cobrando, por URL, que ela nao seja mais
antiga que a revisao do `manifest.json` que a desembarcou"*. A execucao da tarde
de 23/11 fechou a primeira metade — a data de uma pagina e a MAIS RECENTE entre
as datas de tudo de que ela e feita — e escreveu pela 18.3 por que a segunda nao
cabia, em tres alineas:

  (a) o `mudou_em` por item do manifest: FEITO em `atualizar-manifest.py`;
  (b) declarar qual item renderiza qual pagina: FEITO no campo `renderiza` de
      cada item de `snippets`;
  (c) **o campo viajar ate o ar** — e era esta a alinea sem caminho obvio, porque
      a casca NAO le o `manifest.json`: ela le as options que o Sync grava, e o
      Sync so grava item de dado com `publicar: true`.

Este gerador E o caminho da alinea (c): ele compila o manifest em UM arquivo de
dado publicavel, `dados/datas-de-codigo.json`, que o Sync leva a option
`rodametria_dados_datas-de-codigo` e a casca le como le qualquer outro banco.
Dado que o snippet le e dado com `publicar: true` — entao a data do codigo passa
a ser dado.

TRES DECISOES QUE O ARQUIVO CARREGA, E O MOTIVO DE CADA UMA
===========================================================

1. **NADA DE "HOJE" AQUI DENTRO.** O arquivo e funcao PURA do manifest: mesmos
   `mudou_em`, mesmo byte. Se ele estampasse a data da geracao, o `sha256` dele
   trocaria todo dia, a revisao subiria por nada e o proprio `mudou_em` dele
   mentiria sobre o que mudou. Portao que reclama todo dia e portao que alguem
   desliga (20.5).

2. **A UNIAO DOS `renderiza` TEM DE SER EXATAMENTE OS SLUGS QUE A ILHA SERVE.**
   O `renderiza` e declaracao humana, e declaracao humana envelhece. Entao ela
   nao e aceita: e COBRADA. Os slugs de verdade saem das MESMAS fontes de que o
   site sai — `inicio` da casca, os das ferramentas das constantes dos snippets,
   os de produto da vitrine (inclusive a filha DEGRADADA, que e justamente a que
   some de toda lista) e os quatro da 16.1 de `paginas-institucionais.json`.
   Slug sem item que o renderize REPROVA, e item que declara slug inexistente
   REPROVA. Pagina nova obriga a declaracao a crescer no mesmo dia — ruidosamente,
   que e o contrario de envelhecer calada.

3. **`mudou_em: null` NAO VIRA DATA.** `null` e "o git deste clone nao soube
   semear", nunca "nao mudou nunca". Item assim nao contribui data nenhuma, e a
   pagina dele sai com `codigo_nao_sabido: true` para quem ler no ar saber que
   ali nao ha medicao em vez de ler ausencia como aprovacao.

E A `*` DA CASCA NAO E ATALHO: E O FATO
======================================

A casca e `escopo: global` e renderiza TODA pagina desta ilha — cabecalho, trilha,
menu, rodape, o `WebPage` do JSON-LD e os componentes do molde da secao 32. Entao
`renderiza: ["*"]` nela nao e uma lista preguicosa: e a unica declaracao
verdadeira. O custo esta dito na cara: **quando a casca muda, as 11 paginas
mudam**, e as 11 passam a publicar a data de hoje. Isso e verdade e nao
maquiagem — o HTML servido mudou mesmo. O que seria mentira e o contrario: a
pagina afirmar ao Google que nao mudou no dia em que o codigo que a desenha
mudou.
"""

import collections
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)
MANIFEST = os.path.join(ILHA, "manifest.json")
SAIDA = os.path.join(ILHA, "dados", "datas-de-codigo.json")

ID = "datas-de-codigo"


def carregar(caminho):
    with open(caminho, encoding="utf-8") as f:
        return json.load(f, object_pairs_hook=collections.OrderedDict)


def constante(snippet, nome):
    """Le `define( 'NOME', 'valor' )` do PHP. Nunca copia o valor para ca."""
    with open(os.path.join(ILHA, "snippets", snippet), encoding="utf-8") as f:
        m = re.search(r"define\(\s*'" + nome + r"'\s*,\s*'([^']+)'\s*\)", f.read())
    return m.group(1) if m else None


def slugs_que_a_ilha_serve():
    """Os slugs REAIS, das mesmas fontes de que o site sai. (lista, problemas)"""
    problemas = []
    slugs = ["inicio"]          # a home, a unica pagina que a casca cria

    for snippet, nome in (("rodametria-f2.php", "RODAMETRIA_F2_SLUG"),
                          ("rodametria-f3.php", "RODAMETRIA_F3_SLUG"),
                          ("rodametria-produto.php", "RODAMETRIA_PRODUTO_SECAO")):
        v = constante(snippet, nome)
        if not v:
            problemas.append("nao achei a constante %s em snippets/%s — sem ela o slug "
                             "daquela pagina seria DERIVADO de cabeca, que e o defeito "
                             "do RODAMETRIA_INST_VERSAO" % (nome, snippet))
        else:
            slugs.append(v)

    vit = os.path.join(ILHA, "dados", "vitrine-de-produto.json")
    if os.path.exists(vit):
        v = carregar(vit)
        for grupo in ("paginas", "nao_nasceram"):
            for p in (v.get(grupo) or []):
                if p.get("id"):
                    slugs.append(p["id"])
    else:
        problemas.append("dados/vitrine-de-produto.json nao existe — as paginas de "
                         "produto nao puderam ser contadas")

    inst = os.path.join(ILHA, "dados", "paginas-institucionais.json")
    if os.path.exists(inst):
        for p in (carregar(inst).get("paginas") or []):
            if p.get("slug"):
                slugs.append(p["slug"])
    else:
        problemas.append("dados/paginas-institucionais.json nao existe — as quatro "
                         "paginas da 16.1 nao puderam ser contadas")

    repetidos = [s for s, n in collections.Counter(slugs).items() if n > 1]
    if repetidos:
        problemas.append("slug repetido nas fontes: %s" % ", ".join(sorted(repetidos)))

    return sorted(set(slugs)), problemas


def compilar(manifest, slugs_reais):
    """(dado, problemas). `dado` e None quando ha problema que o invalida."""
    problemas = []
    itens = manifest.get("snippets") or []

    por_slug = collections.OrderedDict((s, []) for s in slugs_reais)
    for item in itens:
        decl = item.get("renderiza")
        if decl is None:
            problemas.append("snippets:%s nao declara `renderiza` — sem isso o "
                             "`mudou_em` dele nao alcanca URL nenhuma (alinea (b) "
                             "do despacho de 23/11)" % item["id"])
            continue
        if not isinstance(decl, list) or not decl:
            problemas.append("snippets:%s declara `renderiza` que nao e lista com ao "
                             "menos um slug" % item["id"])
            continue
        alvos = slugs_reais if decl == ["*"] else decl
        if "*" in decl and decl != ["*"]:
            problemas.append("snippets:%s mistura `*` com slug nomeado, e `*` ja quer "
                             "dizer todas — a declaracao fica ambigua" % item["id"])
            continue
        for slug in alvos:
            if slug not in por_slug:
                problemas.append("snippets:%s declara renderizar %r, e esse slug nao "
                                 "esta entre os %d que a ilha serve"
                                 % (item["id"], slug, len(slugs_reais)))
                continue
            por_slug[slug].append(item)

    for slug, quem in por_slug.items():
        if not quem:
            problemas.append("o slug %r nao e renderizado por item nenhum do manifest "
                             "— pagina nova entra na declaracao `renderiza` no mesmo "
                             "dia em que entra no site" % slug)

    if problemas:
        return None, problemas

    paginas = collections.OrderedDict()
    for slug, quem in por_slug.items():
        datas = [i["mudou_em"] for i in quem if i.get("mudou_em")]
        linha = collections.OrderedDict()
        linha["data"] = max(datas) if datas else None
        if not datas:
            linha["codigo_nao_sabido"] = True
        linha["itens"] = [
            collections.OrderedDict((("id", i["id"]),
                                     ("versao", i.get("versao")),
                                     ("mudou_em", i.get("mudou_em"))))
            for i in quem
        ]
        paginas[slug] = linha

    dado = collections.OrderedDict()
    dado["id"] = ID
    dado["ilha"] = manifest.get("ilha")
    dado["o_que_este_arquivo_e"] = (
        "A DATA EM QUE O CODIGO DE CADA PAGINA MUDOU, compilada do `mudou_em` por "
        "item do manifest.json pelo campo `renderiza` de cada snippet. E a TERCEIRA "
        "fonte da data de uma pagina: as duas primeiras sao os bancos de que ela e "
        "feita, e esta e o codigo que a desenha. A casca a compoe com as outras por "
        "`rodametria_casca_data_mais_recente()`, entao a pagina publica a MAIS "
        "RECENTE das tres e nunca uma data mais velha do que o seu proprio HTML."
    )
    dado["por_que_sem_data_de_geracao"] = (
        "Este arquivo e funcao PURA do manifest: mesmos `mudou_em`, mesmo byte. "
        "Estampar a data da geracao faria o `sha256` dele trocar todo dia e a "
        "revisao subir por nada, e o `mudou_em` do proprio arquivo passaria a "
        "dizer que mudou o que nao mudou."
    )
    dado["o_que_null_quer_dizer"] = (
        "`data: null` com `codigo_nao_sabido: true` e `o git deste clone nao soube "
        "semear o `mudou_em`', nunca `nao mudou nunca'. A casca nao publica data "
        "nenhuma a partir disso, e o portao de ar DIZ que nao mediu em vez de "
        "aprovar com cara de completo."
    )
    dado["gerado_por"] = "ferramentas/gerar-datas-de-codigo.py"
    dado["paginas"] = paginas

    return dado, []


def main():
    conferir = "--conferir" in sys.argv
    manifest = carregar(MANIFEST)
    slugs, problemas_slug = slugs_que_a_ilha_serve()
    dado, problemas = compilar(manifest, slugs)
    problemas = problemas_slug + problemas

    if problemas:
        print("REPROVADO: a declaracao `renderiza` nao bate com as paginas da ilha.")
        for p in problemas:
            print("  " + p)
        return 1

    texto = json.dumps(dado, ensure_ascii=False, indent=2) + "\n"

    if conferir:
        if not os.path.exists(SAIDA):
            print("REPROVADO: dados/datas-de-codigo.json nao existe. Rode esta "
                  "ferramenta sem --conferir.")
            return 1
        atual = open(SAIDA, encoding="utf-8").read()
        if atual != texto:
            print("REPROVADO: dados/datas-de-codigo.json nao bate com o manifest.")
            antigas = (carregar(SAIDA).get("paginas") or {})
            for slug, linha in dado["paginas"].items():
                velha = (antigas.get(slug) or {}).get("data")
                if velha != linha["data"]:
                    print("  %-32s  %s -> %s" % (slug, velha or "(ausente)",
                                                 linha["data"] or "null"))
            for slug in antigas:
                if slug not in dado["paginas"]:
                    print("  %-32s  sobra no arquivo e nao e pagina da ilha" % slug)
            return 1
        sem = [s for s, l in dado["paginas"].items() if l.get("codigo_nao_sabido")]
        print("APROVADO: %d pagina(s), %d item(ns) de codigo, %d sem data sabida%s."
              % (len(dado["paginas"]), len(manifest.get("snippets") or []), len(sem),
                 (" (%s)" % ", ".join(sem)) if sem else ""))
        for slug, linha in dado["paginas"].items():
            print("  %-32s %s  <- %s"
                  % (slug, linha["data"] or "null",
                     ", ".join("%s %s" % (i["id"], i["mudou_em"] or "null")
                               for i in linha["itens"])))
        return 0

    antigo = open(SAIDA, encoding="utf-8").read() if os.path.exists(SAIDA) else None
    with open(SAIDA, "w", encoding="utf-8") as f:
        f.write(texto)
    if antigo == texto:
        print("dados/datas-de-codigo.json ja estava em dia; nada mudou.")
    else:
        print("dados/datas-de-codigo.json escrito:")
        antigas = json.loads(antigo).get("paginas", {}) if antigo else {}
        for slug, linha in dado["paginas"].items():
            velha = (antigas.get(slug) or {}).get("data") if antigas else None
            marca = "   " if velha == linha["data"] else "-> "
            print("  %s%-32s %s%s"
                  % (marca, slug, linha["data"] or "null",
                     "" if velha == linha["data"]
                     else ("  (era %s)" % (velha or "ausente"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
