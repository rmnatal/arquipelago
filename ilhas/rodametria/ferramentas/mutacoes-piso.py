#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bateria de mutacao do PISO DE COMPRA da Rodametria.

    python3 ferramentas/mutacoes-piso.py
    python3 ferramentas/mutacoes-piso.py --lista

Ela morde `ferramentas/coletar-piso-de-compra.py` — a conferencia SEM REDE dele e a
regra de composicao da palavra-chave —, nunca a rede. O que a rede mede (quantas
ofertas uma chave devolve) nao cabe em bateria: o que cabe, e o que esta bateria
cobra, e que o numero medido tenha sido GRAVADO e que a URL publicada seja a que a
chave produz, e nao uma digitada a mao.

Cinco familias:

  MUNDOS QUE TEM DE PASSAR — o banco de hoje, o banco sem piso nenhum, e o registro
  excluido_do_banco com motivo velho (a coleta o pula de proposito, e cobrar dele o
  motivo de hoje reprovaria banco certo — foi exatamente esse o defeito que esta
  regua achou no dia em que nasceu).
  QUEBRAS — cada uma estraga UMA coisa e declara a frase que espera ouvir.
  MORTES DO ESQUEMA (26.2) — apagar a regra do esquema tem de MATAR a regua, nunca
  faze-la compor chave com o que sobrou.
  A COMPOSICAO — o degrau so nasce quando TODAS as partes que o nomeiam existem, e
  a chave nunca sai so do termo, so da marca ou so do modelo. O primeiro defeito
  desta regua foi um degrau chamado `marca_modelo_termo` que, sem modelo, compunha
  `marca_termo` e era gravado com o nome errado: procedencia que mente e pior que
  procedencia ausente.
  AUTOTESTE DA BATERIA — uma conferencia de mentira, que aprova tudo, tem de fazer
  esta bateria reprovar.
"""
import copy
import importlib.util
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("piso", RAIZ / "ferramentas/coletar-piso-de-compra.py")
P = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(P)

CASOS = []


def caso(nome, espera=None, passa=False, morre=False):
    """espera = pedaco da frase esperada. passa=True: mundo que nao reprova.
    morre=True: a regua tem de levantar SystemExit com essa frase dentro."""
    def deco(fn):
        CASOS.append((nome, espera, passa, morre, fn))
        return fn
    return deco


def base():
    return P.carregar()


def v(d, id_):
    for r in d["veiculos"]["registros"]:
        if r["id"] == id_:
            return r
    raise KeyError(id_)


def com_piso(d):
    """O primeiro registro que tem piso hoje. A bateria para se nao houver nenhum:
    bateria que se adapta ao banco vazio deixa de medir no dia em que mais importa."""
    for r in d["veiculos"]["registros"]:
        if (r.get("afiliado") or {}).get("url_busca_produto"):
            return r
    raise SystemExit("ERRO: nenhum registro tem piso no banco de hoje; esta bateria nao tem o que morder.")


def sem_piso(d):
    for r in d["veiculos"]["registros"]:
        if r.get("status") == "excluido_do_banco":
            continue
        if not (r.get("afiliado") or {}).get("url_busca_produto"):
            return r
    raise SystemExit("ERRO: todo registro tem piso; esta bateria perdeu um dos mundos que mede.")


# ------------------------------------------------------------- mundos que tem de passar
@caso("o banco de hoje, como esta no repositorio", passa=True)
def _(d):
    return d


@caso("o banco SEM PISO NENHUM — nada publicado e um estado legitimo", passa=True)
def _(d):
    for arq in ("veiculos", "pecas"):
        for r in d[arq]["registros"]:
            if r.get("status") == "excluido_do_banco":
                continue
            r["status"] = "rascunho"
            af = r["afiliado"]
            for ch in ("url_busca", "url_busca_produto", "palavra_chave",
                       "degrau_da_palavra_chave", "ofertas_na_medicao", "medido_em"):
                af[ch] = None
            af["motivo_sem_url_busca"] = ("CAUSA: o banco nao tem com o que compor chave nenhuma "
                                          "para este registro. || ULTIMA TENTATIVA: 2026-10-28.")
    return d


@caso("registro excluido_do_banco com motivo VELHO — a coleta o pula de proposito", passa=True)
def _(d):
    for r in d["veiculos"]["registros"]:
        if r.get("status") == "excluido_do_banco":
            r["afiliado"]["motivo_sem_url_busca"] = "CAUSA: frase de outra passada. || ULTIMA TENTATIVA: nenhuma."
            return d
    raise SystemExit("ERRO: nenhum registro excluido_do_banco no banco de hoje.")


# ------------------------------------------------------------- quebras
@caso("URL de busca DIGITADA A MAO, sem bater com a chave", "nao e a URL que a chave")
def _(d):
    com_piso(d)["afiliado"]["url_busca_produto"] = "https://shopee.com.br/search?keyword=qualquer%20coisa"
    return d


@caso("piso sem a palavra-chave que o gerou", "nao tem `palavra_chave`")
def _(d):
    com_piso(d)["afiliado"]["palavra_chave"] = None
    return d


@caso("degrau de OUTRA entidade gravado no veiculo", "nao e um degrau que o banco de HOJE compoe")
def _(d):
    # `marca_termo_medida` e degrau de PECA e nenhum VEICULO o compoe nunca.
    com_piso(d)["afiliado"]["degrau_da_palavra_chave"] = "marca_termo_medida"
    return d


@caso("campo mudou e a chave ficou para tras", "e o degrau")
def _(d):
    r = com_piso(d)
    r["marca"] = "Outra Marca"
    return d


@caso("piso com ZERO oferta medida", "Chave que a loja nao responde")
def _(d):
    com_piso(d)["afiliado"]["ofertas_na_medicao"] = 0
    return d


@caso("piso que nao diz quando foi medido", "nao diz QUANDO foi medido")
def _(d):
    com_piso(d)["afiliado"]["medido_em"] = None
    return d


@caso("sobra de passada velha: chave sem URL", "Sobra de passada velha")
def _(d):
    sem_piso(d)["afiliado"]["palavra_chave"] = "chave de ontem"
    return d


@caso("publicavel sem `url_busca`", "`publicavel` sem `url_busca`")
def _(d):
    r = com_piso(d)
    r["status"] = "publicavel"
    r["afiliado"]["url_busca"] = None
    return d


@caso("link encurtado sem `encurtamento_tentado_em`", "`encurtamento_tentado_em`")
def _(d):
    com_piso(d)["afiliado"]["encurtamento_tentado_em"] = None
    return d


@caso("sub_id_1 de outra ilha", "`sub_id_1`")
def _(d):
    com_piso(d)["afiliado"]["sub_id_1"] = "robometria"
    return d


@caso("motivo VELHO em registro que nao compoe chave nenhuma", "o motivo gravado diz outra coisa")
def _(d):
    for r in d["veiculos"]["registros"]:
        if r.get("status") == "excluido_do_banco":
            continue
        if not P.candidatas(r, "VEICULO", P.escada_do_esquema(d["esquema-banco"])):
            r["afiliado"]["motivo_sem_url_busca"] = ("CAUSA: a escada inteira foi percorrida. || "
                                                     "ULTIMA TENTATIVA: 2026-10-28.")
            return d
    raise SystemExit("ERRO: todo registro compoe alguma chave; esta quebra perdeu o alvo.")


# ------------------------------------------------------------- mortes do esquema (26.2)
@caso("o esquema SEM `escada_de_compra`", "escada_de_compra` nao existe", morre=True)
def _(d):
    d["esquema-banco"].pop("escada_de_compra")
    return d


@caso("o esquema sem o termo de contexto da entidade PECA", "nao tem termo de contexto", morre=True)
def _(d):
    d["esquema-banco"]["escada_de_compra"]["termo_de_contexto"]["PECA"] = None
    return d


@caso("valor de `tipo_comercial` que o esquema deixou de declarar", "nao esta em escada_de_compra", morre=True)
def _(d):
    d["esquema-banco"]["escada_de_compra"]["termo_de_contexto"]["VEICULO"]["valores"].pop("patinete")
    return d


@caso("tipo de peca que o esquema deixou de declarar", "nao esta em escada_de_compra", morre=True)
def _(d):
    d["esquema-banco"]["escada_de_compra"]["termo_de_contexto"]["PECA"]["valores"].pop("camara")
    return d


# ------------------------------------------------------------- a composicao da chave
def composicao():
    """O que nenhuma mutacao de banco alcanca: a forma da chave, caso a caso."""
    f = []
    if P._juntar("Marca", None, "termo") is not None:
        f.append("COMPOSICAO: `marca_modelo_termo` compos sem modelo. Degrau que nasce com parte "
                 "faltando e gravado com o nome errado — procedencia que mente.")
    if P._juntar("Marca", "", "termo") is not None:
        f.append("COMPOSICAO: parte VAZIA (string em branco) passou como se existisse.")
    if P._juntar("Marca", "Modelo", "termo") != "Marca Modelo termo":
        f.append("COMPOSICAO: a chave completa nao e a juncao das tres partes.")

    esquema = P.escada_do_esquema(base()["esquema-banco"])
    so_termo = {"marca": None, "modelo": None, "tipo_comercial": "patinete"}
    if P.candidatas(so_termo, "VEICULO", esquema):
        f.append("COMPOSICAO: registro sem marca e sem modelo compos chave. Busca so pelo termo daria "
                 "a varios registros a MESMA URL.")
    so_marca = {"marca": "Evoo", "modelo": None, "tipo_comercial": "nao_declarado"}
    if P.candidatas(so_marca, "VEICULO", esquema):
        f.append("COMPOSICAO: chave composta so pela MARCA — a armadilha que a 25.3 nomeia.")
    so_modelo = {"marca": None, "modelo": "X13", "tipo_comercial": "nao_declarado"}
    if P.candidatas(so_modelo, "VEICULO", esquema):
        f.append("COMPOSICAO: chave composta so pelo MODELO.")
    peca_nua = {"marca": None, "tipo": "capacete", "compatibilidade": {"chave": "nenhuma"}}
    if P.candidatas(peca_nua, "PECA", esquema):
        f.append("COMPOSICAO: peca sem marca e sem medida compos chave — seria a busca de categoria "
                 "vendida como busca do produto.")
    peca_boa = P.candidatas({"marca": "Kenda", "tipo": "camara",
                             "compatibilidade": {"chave": "aro_largura", "valor": "16 x 3.0"}},
                            "PECA", esquema)
    if not peca_boa or peca_boa[0][0] != "marca_termo_medida":
        f.append("COMPOSICAO: peca com marca e medida nao compos `marca_termo_medida` no topo (%r)."
                 % (peca_boa,))
    cheia = P.candidatas({"marca": "Honeywhale", "modelo": "M2 MAX", "tipo_comercial": "patinete"},
                         "VEICULO", esquema)
    if [n for n, _ in cheia] != ["marca_modelo_termo", "marca_modelo", "modelo_termo", "marca_termo"]:
        f.append("COMPOSICAO: a ordem dos degraus do VEICULO mudou (%r). A escada vai do mais "
                 "especifico ao menos, e parar no primeiro util so faz sentido nessa ordem."
                 % ([n for n, _ in cheia],))
    if P.url_crua("a b") != "https://shopee.com.br/search?keyword=a%20b":
        f.append("COMPOSICAO: a URL crua da busca mudou de forma sem ninguem decidir.")
    return f


# ------------------------------------------------------------- o motor
def rodar():
    falhas_da_bateria = []
    for nome, espera, passa, morre, fn in CASOS:
        d = fn(copy.deepcopy(base()))
        try:
            falhas = P.conferir(d)
            morreu = None
        except SystemExit as e:
            falhas, morreu = [], str(e)
        if morre:
            if morreu is None:
                falhas_da_bateria.append("%s: a regua NAO morreu — ela seguiu com o esquema mutilado" % nome)
            elif espera and espera not in morreu:
                falhas_da_bateria.append("%s: morreu pelo motivo ERRADO. Esperava %r e ouviu %r"
                                         % (nome, espera, morreu))
        elif passa:
            if morreu:
                falhas_da_bateria.append("%s: mundo que tinha de PASSAR matou a regua (%r)" % (nome, morreu))
            elif falhas:
                falhas_da_bateria.append("%s: mundo que tinha de PASSAR reprovou com %r" % (nome, falhas[:3]))
        else:
            if morreu:
                falhas_da_bateria.append("%s: a regua morreu em vez de reprovar (%r)" % (nome, morreu))
            elif not falhas:
                falhas_da_bateria.append("%s: a conferencia APROVOU o banco estragado" % nome)
            elif espera and not any(espera in f for f in falhas):
                falhas_da_bateria.append("%s: reprovou pelo motivo ERRADO. Esperava ouvir %r e ouviu %r"
                                         % (nome, espera, falhas[:3]))
    return falhas_da_bateria + composicao()


def autoteste():
    original = P.conferir
    try:
        P.conferir = lambda d: []
        if not rodar():
            return ["AUTOTESTE: uma conferencia que aprova TUDO passou nesta bateria. A bateria esta "
                    "quebrada e dizia 0 falha(s)."]
    finally:
        P.conferir = original
    return []


def main():
    if "--lista" in sys.argv:
        for nome, espera, passa, morre, _ in CASOS:
            rotulo = "[passa]" if passa else ("[morte]" if morre else "[quebra]")
            print("%-8s %s" % (rotulo, nome))
        print("         [composicao] 10 afirmacoes sobre a forma da chave")
        print("")
        print("%d caso(s) + composicao + 1 autoteste." % len(CASOS))
        return 0
    falhas = autoteste() + rodar()
    for f in falhas:
        print("FALHA %s" % f)
    print("")
    print("%d caso(s) rodado(s) (%d mundos que passam, %d quebras, %d mortes do esquema), mais as "
          "afirmacoes de composicao e 1 autoteste da bateria."
          % (len(CASOS), sum(1 for c in CASOS if c[2]),
             sum(1 for c in CASOS if not c[2] and not c[3]), sum(1 for c in CASOS if c[3])))
    print("%d falha(s)." % len(falhas))
    print("APROVADO" if not falhas else "REPROVADO")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
