#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
O PISO DE COMPRA DA VITRINE — ITEM 4 DO DESPACHO DE 30/10/2026.

O DEFEITO QUE ESTE ARQUIVO EXISTE PARA FECHAR: `dados/vitrine-de-produto.json`
servia 21 ofertas nas duas paginas da secao 30 com SO `url` — o link de afiliado
encurtado da ficha. Sem `url_produto` elas sao INTESTAVEIS pela 25.4-b (nao ha
como conferir se o anuncio esta vivo); sem `url_busca` estao SEM PISO pela 25.2
(no dia em que o anuncio esgotar, o cartao fica sem saida de compra). E a ilha
nao soube: o portao do piso lia `veiculos.json` e `pecas.json` e podia escrever
"intestaveis: ZERO" com verdade sobre o banco que lia e falso sobre um terco dos
links que a ilha servia — a licao literal do painel de 28/10/2026 na
clubedomosaico.

OS TRES PRIMEIROS CAMPOS NAO SE COLHEM: ELES JA ESTAO NO REPOSITORIO.
`dados/anuncios-por-consulta.json` guarda `url_produto`, `shop_id` e `item_id`
de 40 de 40 anuncios, colhidos NA MESMA CHAMADA da API que devolveu
`url_afiliado` — entao o par da 25.4-b.1 e demonstravel sem remendo, e quem os
leva para a vitrine e `gerar-vitrine-de-produto.py`. Era assim que a ronda de
30/10 conseguiu testar 9 das 21: lendo o par no arquivo de anuncios, porque a
vitrine nao o tinha.

O QUE ESTE ARQUIVO COLHE E SO O PISO, porque ele e a unica parte que precisa de
REDE: a busca da loja encurtada com o sub-id da ilha. Ele mora fora do gerador
de proposito — `gerar-vitrine-de-produto.py` roda na bancada com `--conferir`,
sem rede, e gerador que depende de rede nao se reconfere.

UM PISO POR CONSULTA, E NAO UM POR ANUNCIO, e isto e decisao com motivo: a
chave que achou TODOS os anuncios de uma pagina e uma so (`chave_escolhida`), e
e ela que a 25.2 pode oferecer como saida honesta — "a busca da chave que achou
este anuncio". Os titulos dos anuncios sao titulos de marketplace, nao marca
mais modelo, e uma busca por titulo inteiro devolve menos que a chave medida.

    python3 ferramentas/coletar-piso-da-vitrine.py             # mede, nao grava
    python3 ferramentas/coletar-piso-da-vitrine.py --gravar    # mede e grava
    python3 ferramentas/coletar-piso-da-vitrine.py --conferir  # sem rede; portao
"""

import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path
from urllib.parse import quote

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
FABRICA = RAIZ.parent.parent
API = FABRICA / "ferramentas" / "shopee-api.py"
ANUNCIOS = RAIZ / "dados" / "anuncios-por-consulta.json"

# O MOLDE DA BUSCA E O MESMO DO PISO DO BANCO, e ele e um literal so nesta ilha
# por nascimento: duas grafias de busca seriam dois pisos diferentes para a
# mesma loja. Se um dia divergirem, quem diverge esta errado.
BUSCA_CRUA = "https://shopee.com.br/search?keyword=%s"
SUB_ID_1 = "rodametria"


def url_crua(chave):
    return BUSCA_CRUA % quote(chave)


def _api(args):
    """A Open API da Shopee, sempre pelo utilitario compartilhado da fabrica.

    A credencial e lida POR ELE, do ambiente do processo: esta regua nao le, nao
    imprime e nao grava credencial nenhuma."""
    r = subprocess.run([sys.executable, str(API)] + args,
                       capture_output=True, text=True, cwd=str(FABRICA))
    if r.returncode != 0:
        linha = (r.stderr or r.stdout or "").strip().splitlines()
        return None, (linha[-1] if linha else "falha sem mensagem")
    try:
        return json.loads(r.stdout), None
    except json.JSONDecodeError:
        return None, "resposta da API nao e JSON"


def encurtar(url):
    dados, erro = _api(["link", url, "--sub-id", SUB_ID_1])
    if erro:
        return None, erro
    curto = (dados or {}).get("url_afiliado")
    if not curto:
        return None, "generateShortLink nao devolveu link"
    return curto, None


def ler():
    return json.loads(ANUNCIOS.read_text(encoding="utf-8"))


def consultas_que_servem(a):
    """As consultas que viram pagina. Vitrine so nasce de quem abre o portao da
    30.2, e piso de consulta que nao vira pagina seria link gerado por nada."""
    for c in a["consultas"]:
        if c.get("resumo", {}).get("abre_o_portao_da_30_2") and c.get("publicar_declarado"):
            yield c


def trabalhar(a, gravar):
    hoje = date.today().isoformat()
    relatorio = []
    for c in consultas_que_servem(a):
        chave = c["chave_escolhida"]
        crua = url_crua(chave)
        curto, erro = encurtar(crua)
        relatorio.append({"id": c["id"], "chave": chave, "curto": curto, "erro": erro})
        if gravar and curto:
            c["piso_da_busca"] = {
                "chave": chave,
                "url_busca_produto": crua,
                "url_busca": curto,
                "sub_id_1": SUB_ID_1,
                "encurtamento_tentado_em": hoje,
                "medido_em": hoje,
                "por_que_existe": (
                    "PISO DA 25.2 para os cartoes desta pagina: o link de cada cartao e a "
                    "ficha de um anuncio, e ficha apodrece. Quando ela morrer, esta busca e "
                    "a saida que a pessoa ja tinha na tela."),
            }
        elif gravar and erro:
            # A CAUSA FICA GRAVADA, porque motivo velho manda a execucao seguinte
            # nem tentar (25.4-b.3) e lacuna sem motivo manda tentar as cegas.
            c["piso_da_busca"] = {
                "chave": chave,
                "url_busca_produto": crua,
                "url_busca": None,
                "motivo_sem_url_busca": "ULTIMA TENTATIVA em %s: %s" % (hoje, erro),
                "encurtamento_tentado_em": hoje,
            }
    return relatorio


def conferir(a):
    """O portao, SEM REDE: todo o que vira pagina tem piso, e o piso se reconfere
    a partir da chave — URL digitada a mao e o que esta regua existe para
    impedir (a mesma regua do piso do banco, na mesma ilha)."""
    falhas = []
    vistas = 0
    for c in consultas_que_servem(a):
        vistas += 1
        onde = "consulta %s" % c["id"]
        p = c.get("piso_da_busca")
        if not p:
            falhas.append("%s: abre o portao da 30.2 e nao tem `piso_da_busca`. A pagina serve "
                          "cartao com ficha de anuncio e nenhuma saida para o dia em que ela "
                          "esgotar (25.2)." % onde)
            continue
        if p.get("chave") != c["chave_escolhida"]:
            falhas.append("%s: o piso foi medido na chave %r e a consulta escolhe %r hoje. "
                          "Chave mudou e o piso ficou para tras." % (onde, p.get("chave"),
                                                                     c["chave_escolhida"]))
        if p.get("url_busca_produto") != url_crua(c["chave_escolhida"]):
            falhas.append("%s: `url_busca_produto` nao e a URL que a chave produz hoje. URL "
                          "digitada a mao e o que esta regua existe para impedir." % onde)
        if not p.get("encurtamento_tentado_em"):
            falhas.append("%s: tem piso e nao diz QUANDO o encurtamento foi tentado (25.2-b)." % onde)
        if p.get("url_busca"):
            if not str(p["url_busca"]).startswith("https://s.shopee.com.br/"):
                falhas.append("%s: `url_busca` nao e link encurtado da Shopee: %r"
                              % (onde, p["url_busca"]))
            if p.get("sub_id_1") != SUB_ID_1:
                falhas.append("%s: `sub_id_1` = %r, e nesta ilha ele e sempre %r (25.8)."
                              % (onde, p.get("sub_id_1"), SUB_ID_1))
            if p.get("motivo_sem_url_busca"):
                falhas.append("%s: tem `url_busca` E `motivo_sem_url_busca`. Sobra de passada "
                              "velha lida como causa e pior que lacuna." % onde)
        elif not p.get("motivo_sem_url_busca"):
            falhas.append("%s: sem `url_busca` e sem o motivo. Lacuna sem causa manda a "
                          "execucao seguinte tentar as cegas (25.4-b.3)." % onde)
    if not vistas:
        falhas.append("nenhuma consulta abre o portao da 30.2 — este portao ficou cego")
    return falhas, vistas


def main():
    p = argparse.ArgumentParser(add_help=True)
    p.add_argument("--gravar", action="store_true")
    p.add_argument("--conferir", action="store_true")
    a_ = p.parse_args()
    a = ler()

    if a_.conferir:
        falhas, vistas = conferir(a)
        print("CONFERENCIA DO PISO DA VITRINE — RODAMETRIA (sem rede)")
        for f in falhas:
            print("FALHA %s" % f)
        print("")
        print("%d consulta(s) com pagina, %d falha(s)." % (vistas, len(falhas)))
        print("APROVADO" if not falhas else "REPROVADO")
        return 1 if falhas else 0

    rel = trabalhar(a, a_.gravar)
    for l in rel:
        print("PISO  %-22s %-30s %s" % (l["id"], l["chave"], l["curto"] or ("ERRO: %s" % l["erro"])))
    print("")
    print("%d consulta(s) medida(s), %d com link." % (len(rel), sum(1 for l in rel if l["curto"])))
    if a_.gravar:
        ANUNCIOS.write_text(json.dumps(a, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print("GRAVADO em dados/anuncios-por-consulta.json.")
    else:
        print("(nada gravado — use --gravar)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
