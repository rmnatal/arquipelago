#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escreve o PISO DE COMPRA da secao 25.2 em todo registro do banco da Rodametria.

    python3 ferramentas/coletar-piso-de-compra.py             # mede e mostra o que mudaria
    python3 ferramentas/coletar-piso-de-compra.py --gravar    # mede e grava
    python3 ferramentas/coletar-piso-de-compra.py --conferir  # SEM REDE: confere o que esta escrito

POR QUE ISTO EXISTE
-------------------
O bloco 3 entregou 24 registros e ZERO publicaveis, com a causa escrita identica
em cada `motivo_do_status`: ninguem tem saida de compra, e a 25.2 do
ARQUIPELAGO.md nao admite item publicavel sem piso. Este arquivo e o bloco que a
frase "o que destrava e o bloco de coleta de link" nomeia.

A 25.2 tem a palavra do dono dentro dela — "deve ser 100% automatico sem eu
tocar" — e por isso o piso e a BUSCA: e o unico elo da corrente que a maquina
fabrica sozinha. A 25.2-b acrescenta a trava: registro publicavel nao entra sem
que o ENCURTAMENTO tenha sido tentado pela API do programa da ilha, e AUSENTE e
diferente de tentado-e-falhou.

AS TRES COISAS QUE ESTE ARQUIVO NAO FAZ
---------------------------------------
1. NAO INVENTA PALAVRA. A chave sai de campos que ja estao no banco (`marca`,
   `modelo`, a medida de encaixe da peca) mais o TERMO DE CONTEXTO, que mora no
   ESQUEMA e nao aqui dentro. Entidade ou tipo sem termo declarado no esquema
   faz este arquivo PARAR — a licao da Robometria: lista dentro da regua
   envelhece calada, e tipo novo entraria sem termo nenhum com o banco verde.
2. NAO COMPOE BUSCA SO POR MARCA, SO POR MODELO NEM SO PELO TERMO. Busca so por
   marca e a armadilha que a 25.3 nomeia; busca so pelo termo nao e deste
   produto, e daria a VINTE registros a MESMA URL.
3. NAO ESCOLHE FICHA DE PRODUTO. Casar oferta da API com registro do banco e o
   casamento das cinco armadilhas da 25.7, e e bloco proprio. Aqui a escada para
   no degrau 4 de proposito, e o degrau fica GRAVADO.

A CHAVE E MEDIDA, NUNCA SUPOSTA
-------------------------------
A 25.6(a) mediu em 16/09/2026 que palavra-chave longa devolve ZERO e que zero
nao e erro: "use escada de palavra-chave, pare no primeiro degrau util e
registre em qual degrau casou, que e procedencia". E o que acontece aqui, com
uma diferenca que a busca permite e a ficha nao: o degrau util nao e aquele que
casa com o registro, e aquele em que a loja TEM o que vender. Chave com zero
oferta e um botao que leva a uma pagina vazia — o beco sem saida que o piso
existe para impedir —, entao ela nao vira piso e a escada desce.

`ofertas_na_medicao` fica gravado junto. Ele nao e enfeite: busca nao esgota,
mas muda de nome, e e esse numero que a ronda compara para ver a palavra-chave
morrer sem ninguem avisar.
"""
import argparse
import json
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.parse import quote

RAIZ = Path(__file__).resolve().parent.parent
FABRICA = RAIZ.parent.parent                      # a raiz do repositorio
API = FABRICA / "ferramentas" / "shopee-api.py"
BUSCA_CRUA = "https://shopee.com.br/search?keyword=%s"
SUB_ID_1 = "rodametria"


# --------------------------------------------------------------- o banco e o esquema
def carregar():
    d = {}
    for nome in ("esquema-banco", "veiculos", "pecas"):
        d[nome] = json.loads((RAIZ / "dados" / ("%s.json" % nome)).read_text(encoding="utf-8"))
    return d


def escada_do_esquema(esquema):
    e = esquema.get("escada_de_compra")
    if not e:
        raise SystemExit("ERRO: `escada_de_compra` nao existe em dados/esquema-banco.json. "
                         "A regra da palavra-chave mora no ESQUEMA, nunca dentro desta regua.")
    return e


def termo_de(escada, entidade, chave):
    """O termo de contexto da entidade. Chave sem termo DECLARADO e erro, nunca silencio."""
    bloco = escada["termo_de_contexto"].get(entidade)
    if bloco is None:
        raise SystemExit("ERRO: a entidade %r nao tem termo de contexto declarado no esquema." % entidade)
    valores = bloco["valores"]
    if chave not in valores:
        raise SystemExit("ERRO: %r nao esta em escada_de_compra.termo_de_contexto.%s.valores. "
                         "Valor novo entra numa linha do esquema; aqui ele PARA a regua."
                         % (chave, entidade))
    return valores[chave]


def medida_de_encaixe(peca):
    c = peca.get("compatibilidade") or {}
    if c.get("chave") in (None, "nenhuma"):
        return None
    v = c.get("valor")
    return str(v) if v else None


def _juntar(*partes):
    """Compoe o degrau SO quando TODAS as partes que o nomeiam existem.

    A primeira versao desta funcao filtrava as partes vazias e devolvia o que
    sobrasse — e com isso o degrau `marca_modelo_termo` de um registro sem
    modelo compunha, na verdade, `marca_termo` e era GRAVADO com o nome errado.
    Procedencia que mente e pior que procedencia ausente: `degrau_da_palavra_chave`
    existe para a execucao seguinte saber por que aquela chave e aquela, e o
    conferidor sem rede recompoe o degrau pelo nome para cobrar isso."""
    if any(p is None or not str(p).strip() for p in partes):
        return None
    return " ".join(str(p).strip() for p in partes)


def candidatas(registro, entidade, escada):
    """A escada de palavra-chave deste registro, do degrau mais especifico ao menos.

    Devolve [(nome_do_degrau, chave)]. Lista vazia quer dizer que o banco nao tem
    com o que compor nada — e isso e resposta, nao lacuna."""
    marca = registro.get("marca")
    if entidade == "VEICULO":
        modelo = registro.get("modelo")
        termo = termo_de(escada, "VEICULO", registro.get("tipo_comercial"))
        bruto = [("marca_modelo_termo", _juntar(marca, modelo, termo)),
                 ("marca_modelo", _juntar(marca, modelo)),
                 ("modelo_termo", _juntar(modelo, termo)),
                 ("marca_termo", _juntar(marca, termo))]
    elif entidade == "PECA":
        termo = termo_de(escada, "PECA", registro.get("tipo"))
        medida = medida_de_encaixe(registro)
        bruto = [("marca_termo_medida", _juntar(marca, termo, medida)),
                 ("marca_termo", _juntar(marca, termo)),
                 ("termo_medida", _juntar(termo, medida))]
    else:
        raise SystemExit("ERRO: entidade %r desconhecida." % entidade)
    vistas, saida = set(), []
    for nome, chave in bruto:
        if chave and chave not in vistas:
            vistas.add(chave)
            saida.append((nome, chave))
    return saida


def url_crua(chave):
    return BUSCA_CRUA % quote(chave)


# --------------------------------------------------------------- a rede, por um canal so
def _api(args):
    """A Open API da Shopee, sempre pelo utilitario compartilhado da fabrica.

    A credencial e lida POR ELE, do ambiente do processo, e nunca passa por aqui:
    esta regua nao le, nao imprime e nao grava credencial nenhuma."""
    r = subprocess.run([sys.executable, str(API)] + args,
                       capture_output=True, text=True, cwd=str(FABRICA))
    if r.returncode != 0:
        return None, (r.stderr or r.stdout or "").strip().splitlines()[-1:] or ["falha sem mensagem"]
    try:
        return json.loads(r.stdout), None
    except json.JSONDecodeError:
        return None, ["resposta da API nao e JSON"]


def quantas_ofertas(chave):
    dados, erro = _api(["busca", chave, "--quantos", "10"])
    if erro:
        return None, erro[0] if isinstance(erro, list) else str(erro)
    return len(dados or []), None


def encurtar(url):
    dados, erro = _api(["link", url, "--sub-id", SUB_ID_1])
    if erro:
        return None, erro[0] if isinstance(erro, list) else str(erro)
    curto = (dados or {}).get("url_afiliado")
    if not curto:
        return None, "generateShortLink nao devolveu link"
    return curto, None


# --------------------------------------------------------------- o trabalho
def trabalhar(dados, gravar):
    escada = escada_do_esquema(dados["esquema-banco"])
    hoje = date.today().isoformat()
    relatorio = []
    for arquivo, entidade in (("veiculos", "VEICULO"), ("pecas", "PECA")):
        for r in dados[arquivo]["registros"]:
            if r.get("status") == "excluido_do_banco":
                continue
            linha = {"id": r["id"], "entidade": entidade, "degraus": []}
            escolhida = None
            for nome, chave in candidatas(r, entidade, escada):
                n, erro = quantas_ofertas(chave)
                linha["degraus"].append({"degrau": nome, "chave": chave,
                                         "ofertas": n, "erro": erro})
                if erro:
                    linha["erro_de_rede"] = erro
                    break
                if n:
                    escolhida = (nome, chave, n)
                    break
            linha["escolhida"] = escolhida
            af = r["afiliado"]
            if escolhida:
                nome, chave, n = escolhida
                crua = url_crua(chave)
                curto, erro = encurtar(crua)
                linha["encurtado"] = curto
                linha["erro_do_encurtamento"] = erro
                if gravar:
                    af["programa"] = "shopee"
                    af["degrau"] = 4
                    af["url"] = ""
                    af["url_produto"] = None
                    af["par_colhido_em"] = None
                    af["url_busca_produto"] = crua
                    af["url_busca"] = curto
                    af["palavra_chave"] = chave
                    af["degrau_da_palavra_chave"] = nome
                    af["ofertas_na_medicao"] = n
                    af["medido_em"] = hoje
                    af["encurtamento_tentado_em"] = hoje
                    af["sub_id_1"] = SUB_ID_1
                    af["sub_id_2"] = None
                    af["motivo_sem_url_produto"] = (
                        "CAUSA: a escada da 25.1 parou no degrau 4 de proposito — escolher ficha de "
                        "produto e casar oferta com registro, que e o casamento das cinco armadilhas da "
                        "25.7 e e bloco proprio. || ULTIMA TENTATIVA: nenhuma em %s; nenhuma ficha foi "
                        "escolhida por esta execucao." % hoje)
                    af["motivo_sem_url_busca"] = None
                    if curto:
                        r["status"] = "publicavel"
                        r["motivo_do_status"] = (
                            "`publicavel` pelo PISO da 25.2: a busca `%s` foi medida na Open API em %s e "
                            "devolveu %d oferta(s) no degrau `%s`, e o encurtamento com `sub_id_1` foi "
                            "feito na mesma passada (25.2-b). O que este registro ainda NAO tem e ficha "
                            "de produto (degrau 4), e o que ele publica e o que o banco declara dele — "
                            "nada alem." % (chave, hoje, n, nome))
                    else:
                        r["motivo_do_status"] = (
                            "`rascunho`: a palavra-chave existe e foi medida (`%s`, %d oferta(s) em %s), "
                            "mas o encurtamento FOI TENTADO E FALHOU em %s. Link cru nao vira piso pela "
                            "25.2-b, e a distincao entre ausente e tentado-e-falhou esta gravada em "
                            "`encurtamento_tentado_em`." % (chave, n, hoje, hoje))
                        af["motivo_sem_url_busca"] = (
                            "CAUSA: generateShortLink nao devolveu link para a busca medida. || "
                            "ULTIMA TENTATIVA: %s." % hoje)
            else:
                if gravar:
                    por_que = linha.get("erro_de_rede")
                    af["encurtamento_tentado_em"] = None
                    if por_que:
                        af["motivo_sem_url_busca"] = (
                            "CAUSA: a medicao da palavra-chave nao chegou a loja. || ULTIMA TENTATIVA: "
                            "%s — %s." % (hoje, por_que))
                    elif not candidatas(r, entidade, escada):
                        af["motivo_sem_url_busca"] = (
                            "CAUSA: o banco nao tem com o que compor chave nenhuma para este registro — "
                            "faltam os dois identificadores que a escada combina, e compor so pelo termo "
                            "daria a varios registros a MESMA busca. Nao e lacuna de regua: e o que a "
                            "fonte declarou. || ULTIMA TENTATIVA: %s." % hoje)
                    else:
                        tent = "; ".join("%s=%s (%s oferta(s))" % (d["degrau"], d["chave"], d["ofertas"])
                                         for d in linha["degraus"])
                        af["motivo_sem_url_busca"] = (
                            "CAUSA: a escada inteira foi percorrida e NENHUM degrau devolveu oferta na "
                            "loja — busca com zero resultado e o beco sem saida que o piso existe para "
                            "impedir. Degraus medidos: %s. || ULTIMA TENTATIVA: %s." % (tent, hoje))
                    r["motivo_do_status"] = (
                        "`rascunho` por falta de PISO (25.2), e a causa esta em "
                        "`afiliado.motivo_sem_url_busca`, medida em %s e nao suposta." % hoje)
            relatorio.append(linha)
    return relatorio


# --------------------------------------------------------------- o portao sem rede
def conferir(dados):
    """SEM REDE. Confere que o que esta gravado e o que a regra do esquema produz."""
    escada = escada_do_esquema(dados["esquema-banco"])
    falhas = []
    for arquivo, entidade in (("veiculos", "VEICULO"), ("pecas", "PECA")):
        for r in dados[arquivo]["registros"]:
            if r.get("status") == "excluido_do_banco":
                # Registro recusado FICA GRAVADO para a proxima execucao nao o recolher de novo, e
                # por isso a coleta o PULA. Cobrar dele o motivo de hoje seria reprovar o banco por
                # um campo que, de proposito, ninguem mais escreve. Foi esta regua que achou a
                # divergencia entre os dois lados: a coleta pulava e a conferencia nao.
                continue
            onde = "%s / %s" % (arquivo, r["id"])
            af = r.get("afiliado") or {}
            cands = dict(((n, c) for n, c in candidatas(r, entidade, escada)))
            chave = af.get("palavra_chave")
            nome = af.get("degrau_da_palavra_chave")
            if af.get("url_busca_produto"):
                if not chave:
                    falhas.append("%s: tem `url_busca_produto` e nao tem `palavra_chave`. A URL sem a "
                                  "palavra que a gerou nao se reconfere." % onde)
                    continue
                if url_crua(chave) != af["url_busca_produto"]:
                    falhas.append("%s: `url_busca_produto` nao e a URL que a chave %r produz. URL "
                                  "digitada a mao e o que esta regua existe para impedir." % (onde, chave))
                if nome not in cands:
                    falhas.append("%s: `degrau_da_palavra_chave` = %r nao e um degrau que o banco de HOJE "
                                  "compoe para este registro (%s). Campo mudou e a chave ficou para tras."
                                  % (onde, nome, ", ".join(sorted(cands)) or "nenhum"))
                elif cands[nome] != chave:
                    falhas.append("%s: a chave gravada e %r e o degrau %r compoe %r hoje."
                                  % (onde, chave, nome, cands[nome]))
                if not isinstance(af.get("ofertas_na_medicao"), int) or af["ofertas_na_medicao"] < 1:
                    falhas.append("%s: tem piso e `ofertas_na_medicao` = %r. Chave que a loja nao responde "
                                  "nao vira piso." % (onde, af.get("ofertas_na_medicao")))
                if not af.get("medido_em"):
                    falhas.append("%s: tem piso e nao diz QUANDO foi medido." % onde)
            else:
                for ch in ("palavra_chave", "url_busca", "ofertas_na_medicao"):
                    if af.get(ch):
                        falhas.append("%s: nao tem `url_busca_produto` e tem `%s` = %r. Sobra de passada "
                                      "velha lida como piso e pior que lacuna." % (onde, ch, af.get(ch)))
                if not cands and af.get("motivo_sem_url_busca") and \
                        "nao tem com o que compor" not in af["motivo_sem_url_busca"]:
                    falhas.append("%s: o banco nao compoe chave nenhuma e o motivo gravado diz outra "
                                  "coisa. Motivo velho manda a execucao seguinte nem tentar (25.4-b.3)."
                                  % onde)
            if r.get("status") == "publicavel" and not af.get("url_busca"):
                falhas.append("%s: `publicavel` sem `url_busca`. Nao existe item publicavel sem piso "
                              "(25.2)." % onde)
            if af.get("url_busca") and not af.get("encurtamento_tentado_em"):
                falhas.append("%s: tem link encurtado e nao tem `encurtamento_tentado_em` (25.2-b)." % onde)
            if af.get("sub_id_1") and af["sub_id_1"] != SUB_ID_1:
                falhas.append("%s: `sub_id_1` = %r, e nesta ilha ele e sempre %r (25.8)."
                              % (onde, af["sub_id_1"], SUB_ID_1))
    return falhas


def main():
    p = argparse.ArgumentParser(add_help=True)
    p.add_argument("--gravar", action="store_true")
    p.add_argument("--conferir", action="store_true")
    a = p.parse_args()
    dados = carregar()

    if a.conferir:
        falhas = conferir(dados)
        print("CONFERENCIA DO PISO DE COMPRA — RODAMETRIA (sem rede)")
        for f in falhas:
            print("FALHA %s" % f)
        print("")
        print("%d falha(s)." % len(falhas))
        print("APROVADO" if not falhas else "REPROVADO")
        return 1 if falhas else 0

    rel = trabalhar(dados, a.gravar)
    com, sem = [], []
    for l in rel:
        (com if l["escolhida"] else sem).append(l)
    for l in rel:
        if l["escolhida"]:
            nome, chave, n = l["escolhida"]
            print("PISO  %-34s %-18s %-55s %3d oferta(s)  %s"
                  % (l["id"], nome, chave, n, l.get("encurtado") or l.get("erro_do_encurtamento")))
        else:
            tent = ", ".join("%s(%s)" % (d["degrau"], d["ofertas"]) for d in l["degraus"]) or "nenhum degrau composto"
            print("-     %-34s %s" % (l["id"], tent))
    print("")
    print("%d com piso, %d sem, de %d registro(s)." % (len(com), len(sem), len(rel)))
    if a.gravar:
        agora = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        for arquivo in ("veiculos", "pecas"):
            dados[arquivo]["piso_de_compra_colhido_em"] = agora
            caminho = RAIZ / "dados" / ("%s.json" % arquivo)
            caminho.write_text(json.dumps(dados[arquivo], ensure_ascii=False, indent=1) + "\n",
                               encoding="utf-8")
        print("GRAVADO em dados/veiculos.json e dados/pecas.json.")
    else:
        print("(nada gravado — use --gravar)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
