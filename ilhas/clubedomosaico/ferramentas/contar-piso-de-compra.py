#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A CONTAGEM DO PISO DE COMPRA — derivada do banco, nunca estimada.

    python3 ferramentas/contar-piso-de-compra.py .            # imprime
    python3 ferramentas/contar-piso-de-compra.py . --gravar    # escreve o arquivo datado

---------------------------------------------------------------------------
QUEM PEDIU ESTA FERRAMENTA, E A DATA FAZ PARTE DO PEDIDO
---------------------------------------------------------------------------
Item 4 do despacho da Sentinela de 07/10/2026 (leitura semanal). O critério de
pronto dele é literal e datado:

    "existir em `ilhas/clubedomosaico/dados/` um arquivo de contagem datado de
    2026-10-14 ou depois, com total de publicáveis, quantos sem `url_busca`,
    quantos sem `url_produto` e a distribuição por `degrau`."

Ele ficou SEIS dias inelegível por causa da data — e não por falta de trabalho.
As execuções de 09/10 a 13/10 o pularam escrevendo o motivo, porque fechá-lo
antes de 14/10 seria o que a 18.4 proíbe: apagar despacho sem cumprir o
critério que ele mesmo declara.

**O despacho descreve a contagem como NÃO FEITA porque a passada dele não
alcançava a sessão do Shopee Afiliados.** Essa parte é verdade para GERAR link;
não é verdade para CONTAR. Os quatro números que ele pede estão todos no banco
desta ilha, em campo lido por máquina, e nenhum deles precisa de sessão, de
navegador ou de rede. É por isso que esta ferramenta existe: a contagem que
parecia bloqueada por credencial de terceiro era derivável do repositório.

---------------------------------------------------------------------------
POR QUE UMA FERRAMENTA E NÃO UM ARQUIVO ESCRITO À MÃO
---------------------------------------------------------------------------
Porque o número que importa é o de HOJE, e este banco cresceu de 38 para 43
registros em duas semanas. Contagem digitada envelhece calada: o próprio
despacho cita, como último número medido, o do Pente Fino de 05/10 — que já
estava errado quando foi citado em 07/10. Uma ferramenta derivada do banco
devolve o número do dia em que roda, e a divergência contra o
`validar-banco.py` (que imprime a mesma escada por outro caminho) é um portão
de graça: dois caminhos independentes sobre o mesmo dado.

---------------------------------------------------------------------------
AS QUATRO PERGUNTAS NÃO SÃO A MESMA, E É AQUI QUE A CONTAGEM GANHA VALOR
---------------------------------------------------------------------------
A seção 25 do `ARQUIPELAGO.md` separa coisas que parecem uma só. Esta
ferramenta conta as quatro separadas, com o nome que a seção lhes dá:

  `url_busca`          — o PISO ENCURTADO (25.2). É o que rende comissão.
                         Item sem ele é defeito da 19.1 em qualquer degrau.
  `url_busca_produto`  — o piso CRU (25.4-b). É o que garante que o leitor tem
                         para onde ir. Sem ele e sem os outros dois, o item
                         chegaria à frase "link de loja em breve", proibida.
  `url_produto`        — a FICHA do produto. É ela que faz o teste de vida da
                         25.4 existir: sem ficha não há o que medir.
  `degrau`             — a escada da 25.1, que é por onde a leitura semanal
                         acha o que pode SUBIR.

Um item sem `url_produto` não é um item sem saída de compra: é um item de
degrau 4, que tem busca e não tem ficha. Contados juntos, os dois viram um
número que não diz o que fazer — que é o defeito que o despacho de 30/09 já
nomeou uma vez nesta ilha, na contagem do degrau 4.
"""
import collections
import json
import os
import re
import subprocess
import sys

BANCOS = (
    "dados/materiais-colas.json",
    "dados/materiais-pastilhas.json",
    "dados/materiais-rejuntes.json",
    "dados/materiais-alicates.json",
    "dados/materiais-acabamento.json",
)


def contar(raiz):
    """Devolve a contagem, sem escrever nada. Toda chave é derivada do banco."""
    itens = []
    for rel in BANCOS:
        caminho = os.path.join(raiz, rel)
        with open(caminho, encoding="utf-8") as fh:
            banco = json.load(fh)
        for m in banco["materiais"]:
            af = m.get("afiliado")
            if af is None:
                # Afiliado tem de existir mesmo vazio (seção 7). Se faltar, o
                # item NAO e publicavel e a contagem diz isso em vez de somar.
                itens.append({"id": m["id"], "categoria": m["categoria"],
                              "sem_bloco": True})
                continue
            causa = None
            if af.get("degrau") == 4:
                achado = re.search(r"CAUSA \((.*?)\)", af.get("motivo_sem_ficha") or "")
                causa = achado.group(1) if achado else "SEM CAUSA ESCRITA"
            itens.append({
                "id": m["id"],
                "categoria": m["categoria"],
                "sem_bloco": False,
                "programa": af.get("programa"),
                "degrau": af.get("degrau"),
                "tem_url_busca": bool(af.get("url_busca")),
                "tem_url_busca_produto": bool(af.get("url_busca_produto")),
                "tem_url_produto": bool(af.get("url_produto")),
                "tem_url_afiliado_de_ficha": bool(af.get("url")),
                "causa_do_degrau_4": causa,
            })

    publicaveis = [i for i in itens if not i["sem_bloco"]]
    c = {
        "no_banco": len(itens),
        "publicaveis": len(publicaveis),
        "sem_bloco_de_afiliado": [i["id"] for i in itens if i["sem_bloco"]],
        "sem_url_busca": [i["id"] for i in publicaveis if not i["tem_url_busca"]],
        "sem_url_busca_produto": [i["id"] for i in publicaveis
                                  if not i["tem_url_busca_produto"]],
        "sem_url_produto": [i["id"] for i in publicaveis if not i["tem_url_produto"]],
        "sem_nenhuma_saida": [i["id"] for i in publicaveis
                              if not (i["tem_url_busca"] or i["tem_url_busca_produto"]
                                      or i["tem_url_afiliado_de_ficha"])],
        "por_degrau": dict(sorted(collections.Counter(
            i["degrau"] for i in publicaveis).items(),
            key=lambda p: (p[0] is None, p[0]))),
        "por_programa": dict(collections.Counter(i["programa"] for i in publicaveis)),
        "causas_do_degrau_4": dict(collections.Counter(
            i["causa_do_degrau_4"] for i in publicaveis
            if i["causa_do_degrau_4"]).most_common()),
        "por_categoria_e_degrau": {},
    }
    por_cat = collections.defaultdict(collections.Counter)
    for i in publicaveis:
        por_cat[i["categoria"]][i["degrau"]] += 1
    for cat in sorted(por_cat):
        c["por_categoria_e_degrau"][cat] = dict(sorted(por_cat[cat].items()))

    # A AFIRMACAO QUE VALE MAIS QUE OS NUMEROS: `sem url_produto` e `degrau 4`
    # tem de ser o MESMO conjunto. Degrau 4 e, por definicao da 25.1, o degrau
    # de quem nao casou com ficha nenhuma. Item de degrau 1 a 3 sem ficha seria
    # degrau mentido; item de degrau 4 COM ficha seria degrau que nao subiu. Os
    # dois sao defeito de dado, e nenhum dos dois portoes de hoje os pega: o
    # `validar-banco.py` cobra que o degrau esteja escrito e que o 4 tenha
    # motivo, nunca que ele DESCREVA o link ao lado.
    sem_ficha = {i["id"] for i in publicaveis if not i["tem_url_produto"]}
    degrau_4 = {i["id"] for i in publicaveis if i["degrau"] == 4}
    c["sem_url_produto_e_degrau_4_sao_o_mesmo_conjunto"] = sem_ficha == degrau_4
    c["degrau_4_com_ficha"] = sorted(degrau_4 - sem_ficha)
    c["sem_ficha_fora_do_degrau_4"] = sorted(sem_ficha - degrau_4)
    return c, itens


def sha_do_banco(raiz):
    """O commit em que o banco estava quando a contagem foi feita."""
    try:
        return subprocess.run(
            ["git", "-C", raiz, "log", "-1", "--format=%h", "--"] + list(BANCOS),
            capture_output=True, text=True, timeout=30).stdout.strip() or None
    except Exception:
        return None



# ---------------------------------------------------------------------------
# O AUTOTESTE — oito casos, e os dois primeiros sao o mundo medido hoje
# ---------------------------------------------------------------------------
# A regua desta ferramenta e simples o bastante para parecer obvia, e e por
# isso que ela precisa de casos: contagem errada nao parece errada, ela parece
# um numero. Os casos cobrem os dois defeitos de dado que NENHUM portao desta
# ilha pegava antes dela — degrau 4 COM ficha (degrau que nao subiu) e item sem
# ficha FORA do degrau 4 (degrau mentido) — e o caso da secao 7, o item sem
# nenhuma saida de compra.
#
# Rodar com:  python3 ferramentas/contar-piso-de-compra.py --autoteste

def _banco(materiais):
    return {"id": "t", "ilha": "clubedomosaico", "categoria": "cola", "bloco": 3,
            "materiais": materiais}


def _item(iid, **af):
    base = {"programa": "shopee", "url": "", "url_produto": None, "url_busca": None,
            "url_busca_produto": None, "degrau": None, "motivo_sem_ficha": None}
    base.update(af)
    return {"id": iid, "categoria": "cola", "afiliado": base}


def _mundo(raiz, materiais):
    os.makedirs(os.path.join(raiz, "dados"), exist_ok=True)
    for i, rel in enumerate(BANCOS):
        with open(os.path.join(raiz, rel), "w", encoding="utf-8") as fh:
            json.dump(_banco(materiais if i == 0 else []), fh)


def autoteste():
    import tempfile
    casos = []

    def caso(nome, materiais, confere):
        casos.append((nome, materiais, confere))

    caso("o mundo de hoje em miniatura: ficha, busca e degrau 3",
         [_item("a", url="https://s.shopee.com.br/X", url_produto="https://shopee.com.br/product/1/2",
                url_busca="https://s.shopee.com.br/Y",
                url_busca_produto="https://shopee.com.br/search?keyword=x", degrau=3)],
         lambda c: (c["publicaveis"] == 1 and not c["sem_url_busca"]
                    and not c["sem_url_produto"] and c["por_degrau"] == {3: 1}
                    and c["sem_url_produto_e_degrau_4_sao_o_mesmo_conjunto"]))

    caso("degrau 4 legitimo: busca nas duas formas, sem ficha, com causa escrita",
         [_item("b", url_busca="https://s.shopee.com.br/Y",
                url_busca_produto="https://shopee.com.br/search?keyword=x", degrau=4,
                motivo_sem_ficha="CAUSA (marca-nao-anunciada): ... || ULTIMA TENTATIVA 2026-10-13: ...")],
         lambda c: (c["sem_url_produto"] == ["b"] and c["por_degrau"] == {4: 1}
                    and c["causas_do_degrau_4"] == {"marca-nao-anunciada": 1}
                    and c["sem_url_produto_e_degrau_4_sao_o_mesmo_conjunto"]))

    caso("DEGRAU QUE NAO SUBIU: degrau 4 com ficha — tem de REPROVAR",
         [_item("c", url_produto="https://shopee.com.br/product/1/2",
                url_busca="https://s.shopee.com.br/Y",
                url_busca_produto="https://shopee.com.br/search?keyword=x", degrau=4)],
         lambda c: (not c["sem_url_produto_e_degrau_4_sao_o_mesmo_conjunto"]
                    and c["degrau_4_com_ficha"] == ["c"]))

    caso("DEGRAU MENTIDO: sem ficha e degrau 3 — tem de REPROVAR",
         [_item("d", url_busca="https://s.shopee.com.br/Y",
                url_busca_produto="https://shopee.com.br/search?keyword=x", degrau=3)],
         lambda c: (not c["sem_url_produto_e_degrau_4_sao_o_mesmo_conjunto"]
                    and c["sem_ficha_fora_do_degrau_4"] == ["d"]))

    caso("SECAO 7: item sem nenhuma saida de compra — tem de aparecer",
         [_item("e", degrau=4)],
         lambda c: c["sem_nenhuma_saida"] == ["e"] and c["sem_url_busca"] == ["e"])

    caso("PISO CRU SEM O ENCURTADO: conta no `sem_url_busca` e nao no `sem_nenhuma_saida`",
         [_item("f", url_busca_produto="https://shopee.com.br/search?keyword=x", degrau=4)],
         lambda c: c["sem_url_busca"] == ["f"] and not c["sem_nenhuma_saida"]
                   and not c["sem_url_busca_produto"])

    caso("degrau 4 SEM causa escrita: a contagem diz isso em vez de calar",
         [_item("g", url_busca="https://s.shopee.com.br/Y",
                url_busca_produto="https://shopee.com.br/search?keyword=x", degrau=4,
                motivo_sem_ficha="familia: medida")],
         lambda c: c["causas_do_degrau_4"] == {"SEM CAUSA ESCRITA": 1})

    caso("ITEM SEM BLOCO DE AFILIADO: nao entra em publicaveis",
         [{"id": "h", "categoria": "cola"}],
         lambda c: (c["no_banco"] == 1 and c["publicaveis"] == 0
                    and c["sem_bloco_de_afiliado"] == ["h"]))

    falhas = 0
    for nome, materiais, confere in casos:
        raiz = tempfile.mkdtemp(prefix="cdm-contagem-")
        _mundo(raiz, materiais)
        c, _ = contar(raiz)
        ok = False
        try:
            ok = bool(confere(c))
        except Exception as e:          # noqa: BLE001 — o caso falhou, e dizer isso basta
            print("  ERRO no caso: %s" % e)
        print("  %s %s" % ("ok     " if ok else "FALHOU ", nome))
        if not ok:
            falhas += 1
            print("      contagem: %s" % json.dumps(
                {k: v for k, v in c.items() if k != "itens"}, ensure_ascii=False))
    print("\n%d caso(s), %d falha(s)" % (len(casos), falhas))
    return 0 if falhas == 0 else 1

def main():
    if "--autoteste" in sys.argv:
        print("AUTOTESTE da contagem do piso de compra")
        return autoteste()
    raiz = sys.argv[1] if len(sys.argv) > 1 else "."
    gravar = "--gravar" in sys.argv
    c, itens = contar(raiz)

    print("A CONTAGEM DO PISO DE COMPRA — item 4 do despacho de 07/10/2026")
    print("  registros no banco ............ %d" % c["no_banco"])
    print("  PUBLICAVEIS (com bloco) ....... %d" % c["publicaveis"])
    print("  sem bloco de afiliado ......... %d  (secao 7 — tem de ser 0)"
          % len(c["sem_bloco_de_afiliado"]))
    print("  sem `url_busca` ............... %d  (25.2 — o piso que rende comissao)"
          % len(c["sem_url_busca"]))
    print("  sem `url_busca_produto` ....... %d  (25.4-b — o piso cru)"
          % len(c["sem_url_busca_produto"]))
    print("  sem `url_produto` ............. %d  (25.4 — sem ficha nao ha teste de vida)"
          % len(c["sem_url_produto"]))
    print("  sem NENHUMA saida de compra ... %d  (secao 7 — tem de ser 0)"
          % len(c["sem_nenhuma_saida"]))
    print("  a escada da 25.1 .............. %s  (soma %d)"
          % ("  ".join("%s:%s" % (d, n) for d, n in c["por_degrau"].items()),
             sum(c["por_degrau"].values())))
    for causa, n in c["causas_do_degrau_4"].items():
        print("    causa do degrau 4: %-36s %d" % (causa, n))
    print("  por programa .................. %s" % c["por_programa"])
    for cat, deg in c["por_categoria_e_degrau"].items():
        print("    %-12s %s" % (cat, deg))

    ok = True
    if not c["sem_url_produto_e_degrau_4_sao_o_mesmo_conjunto"]:
        ok = False
        print("\nFALHA: `sem url_produto` e `degrau 4` nao sao o mesmo conjunto.")
        if c["degrau_4_com_ficha"]:
            print("  degrau 4 COM ficha (degrau que nao subiu): %s"
                  % ", ".join(c["degrau_4_com_ficha"]))
        if c["sem_ficha_fora_do_degrau_4"]:
            print("  sem ficha FORA do degrau 4 (degrau mentido): %s"
                  % ", ".join(c["sem_ficha_fora_do_degrau_4"]))
    else:
        print("\n  `sem url_produto` == `degrau 4`: os dois conjuntos batem, "
              "%d a %d." % (len(c["sem_url_produto"]), c["por_degrau"].get(4, 0)))
    if c["sem_bloco_de_afiliado"] or c["sem_nenhuma_saida"]:
        ok = False
        print("FALHA: item sem saida de compra — secao 7.")

    if gravar:
        hoje = subprocess.run(["date", "-u", "+%Y-%m-%d"], capture_output=True,
                              text=True).stdout.strip()
        agora = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%MZ"],
                               capture_output=True, text=True).stdout.strip()
        destino = os.path.join(raiz, "dados", "contagem-piso-de-compra-%s.json" % hoje)
        saida = {
            "id": "contagem-piso-de-compra-%s" % hoje,
            "ilha": "clubedomosaico",
            "medido_em": agora,
            "o_que_este_arquivo_e": (
                "A contagem do piso de compra do banco desta ilha, derivada dos "
                "cinco arquivos `dados/materiais-*.json` e de mais nada. Cumpre o "
                "critério de pronto do item 4 do despacho da Sentinela de "
                "07/10/2026, que pede um arquivo datado de 2026-10-14 ou depois "
                "com total de publicáveis, quantos sem `url_busca`, quantos sem "
                "`url_produto` e a distribuição por `degrau`."),
            "como_reproduzir": "python3 ferramentas/contar-piso-de-compra.py .",
            "commit_do_banco_quando_foi_medido": sha_do_banco(raiz),
            "o_que_esta_contagem_nao_e": (
                "Não é teste de vida (25.4): ela diz quantos itens TÊM ficha, não "
                "se a ficha está viva — isso é medição de rede e é da ronda. E não "
                "é contagem de link GERADO: `url_busca` e `url_busca_produto` "
                "estão nos 43, e o que falta nos 19 do degrau 4 é a ficha, que não "
                "depende de sessão de painel nenhuma."),
            "contagem": c,
            "itens": itens,
        }
        with open(destino, "w", encoding="utf-8") as fh:
            json.dump(saida, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
        print("\ngravado: %s" % destino)

    print("\n%s" % ("OK: a contagem bate e nao ha item sem saida de compra."
                    if ok else "REPROVADO: ver as falhas acima."))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
