#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BANCADA: sem rede — este confere o REPOSITORIO, nao o site.

A DERIVA DO CATALOGO DE ESPECIES ESTA MEDIDA E DECLARADA?

    python3 ferramentas/conferir-deriva-do-catalogo.py
    python3 ferramentas/conferir-deriva-do-catalogo.py --gravar

POR QUE ELE EXISTE, e a data e 16/10/2026
------------------------------------------
Entre 15/10 e 16/10/2026 TRES execucoes seguidas desta ilha mediram a mesma
coisa do mesmo jeito: rodaram `gerar-catalogo-especies.py` contra o snippet de
VERDADE, leram quantas linhas ele acrescentaria, e restauraram o arquivo "byte
a byte" depois. O numero que saiu dessas tres passadas — 34 linhas, depois 74,
depois 74 outra vez — virou PROSA no `REGISTRO.md` e no `bloco_atual`, e e por
essa prosa que a passada de 21/10 sabe o que tem para desembarcar.

Duas coisas erradas nisso, e a segunda e a que custa caro:

  1. A medicao tem um passo DESTRUTIVO no meio. Ela escreve no arquivo que
     serve 52 URLs, com a superficie da ilha congelada pela leitura semanal de
     14/10, e so volta ao certo porque alguem se lembrou de restaurar. Tres
     vezes seguidas deu certo; o quarto restauro esquecido poe no ar o valor
     que o congelamento existe para segurar.

  2. Numero que a ilha publica sobre si mesma nasce CONTADO (secao 8). "74
     linhas de deriva" nao estava contado em lugar nenhum: estava escrito. E
     numero escrito envelhece calado — e a cicatriz desta pasta inteira, do
     indice de levas em quatro linhas para seis levas ao portao da voz que
     media 36 das 40 paginas.

Este portao faz as duas: a medicao passa a sair de uma RAIZ DE SOMBRA (o
snippet de verdade e lido, nunca aberto para escrita, e o sha256 dele e
AFIRMADO antes e depois), e a deriva passa a ter serie declarada em
`dados/deriva-do-catalogo.md`, que ele confere LINHA POR LINHA.

O QUE ELE AFIRMA
----------------
  1. O snippet de verdade e byte a byte o mesmo depois da medicao. Esta e a
     afirmacao que torna o portao seguro de rodar durante o congelamento, e e a
     primeira de proposito: se ela cair, nada mais do que este arquivo diz
     importa.
  2. O gerador roda e sai com codigo 0 contra o banco de hoje.
  3. Nenhuma linha de deriva cai FORA dos dois blocos que o gerador escreve
     (CATALOGO e BARRADOS). Deriva fora deles nunca e legitima: ou o gerador
     mexe onde nao e dele, ou o snippet foi editado a mao onde so ele escreve.
  4. A deriva medida e a DECLARADA sao a mesma, linha por linha e com
     multiplicidade — nao o mesmo total. 74 linhas podem virar 74 OUTRAS
     linhas, e um portao que guardasse so o numero ficaria verde sobre a troca.

E O QUE ELE NAO FAZ, de proposito: nao decide se a deriva deve desembarcar, nao
regera nada e nao toca no snippet. Desembarque e decisao de leva, e hoje ela tem
data (21/10/2026, pela leitura semanal de 14/10).

QUANDO ELE FICA VERMELHO, O CONSERTO E UM COMANDO
--------------------------------------------------
Mudou o banco e a deriva cresceu? `--gravar` escreve a secao nova da serie, com
a data, e o portao volta a verde. Desembarcou a leva e a deriva virou zero?
`--gravar` tambem — zero declarado e um fato tao contavel quanto 74. O que ele
recusa e o silencio: deriva que ninguem contou nem declarou.
"""
import importlib.util
import io
import json
import os
import re
import sys
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FERRAMENTAS = os.path.join(RAIZ, "ferramentas")
SNIPPET = os.path.join(RAIZ, "snippets", "aquametria-peixes.php")
SERIE = os.path.join(RAIZ, "dados", "deriva-do-catalogo.md")

GRAVAR = "--gravar" in sys.argv[1:]


def carregar_regua():
    caminho = os.path.join(FERRAMENTAS, "regua-deriva-do-catalogo.py")
    spec = importlib.util.spec_from_file_location("regua_deriva_do_catalogo", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


regua = carregar_regua()

falhas = []


def ok(rotulo, condicao, detalhe=""):
    if condicao:
        print("  ok   %s" % rotulo)
    else:
        print("  FALHA %s%s" % (rotulo, (" — " + detalhe) if detalhe else ""))
        falhas.append(rotulo)


def sha256_do_snippet():
    import hashlib
    with io.open(SNIPPET, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def cabecalho_da_serie():
    return (
        "# Serie de DERIVA DO CATALOGO DE ESPECIES — Aquametria\n"
        "\n"
        "Quanto o `snippets/aquametria-peixes.php` do repositorio difere do que\n"
        "`ferramentas/gerar-catalogo-especies.py` produz do banco de hoje. Escreve aqui\n"
        "o `ferramentas/conferir-deriva-do-catalogo.py --gravar`; quem confere e o mesmo\n"
        "arquivo sem a opcao, e ele compara LINHA POR LINHA, nao pelo total.\n"
        "\n"
        "**Secao nova vai no TOPO** (a serie cresce por cima, como `dados/posicoes.md`) e\n"
        "secao antiga NUNCA e sobrescrita: a serie so vale porque cresce. O bloco `json`\n"
        "de cada secao e a declaracao que o portao le — o primeiro do arquivo e o que\n"
        "manda.\n"
        "\n"
        "Deriva **nao e defeito**: e valor de banco que ainda nao desembarcou, e ela\n"
        "desembarca junto com a primeira leva que regerar o catalogo. O que e defeito e\n"
        "deriva que ninguem contou.\n"
    )


def gravar(medicao, agora):
    linhas = regua.assinatura(medicao["mudancas"])
    dados = {
        "medido_em": agora,
        "total_de_linhas": len(medicao["mudancas"]),
        "linhas": linhas,
    }
    secao = ["## %s" % agora, ""]
    if not linhas:
        secao.append("**Deriva ZERO**: o snippet do repositorio e o que o gerador produz do")
        secao.append("banco de hoje dizem a mesma coisa. Nada a desembarcar.")
    else:
        secao.append("**%d linha(s) de deriva**, agrupadas por linha repetida:" % len(medicao["mudancas"]))
        secao.append("")
        for chave, quantas in regua.agrupada_por_causa(medicao["mudancas"]):
            secao.append("- `%d x` `%s`" % (quantas, chave.replace("`", "'")))
    secao += ["", "```json", json.dumps(dados, ensure_ascii=False, indent=2, sort_keys=True), "```", ""]
    novo = "\n".join(secao) + "\n"

    if os.path.exists(SERIE):
        antigo = regua.ler(SERIE)
        corte = antigo.find("\n## ")
        if corte == -1:
            texto = antigo.rstrip("\n") + "\n\n" + novo
        else:
            texto = antigo[:corte + 1] + "\n" + novo + antigo[corte + 1:]
    else:
        texto = cabecalho_da_serie() + "\n" + novo
    with io.open(SERIE, "w", encoding="utf-8") as f:
        f.write(texto)
    print("serie gravada: %s" % os.path.relpath(SERIE, RAIZ))


def main():
    agora = time.strftime("%Y-%m-%d %H:%MZ", time.gmtime())
    print("DERIVA DO CATALOGO DE ESPECIES — medida de raiz de sombra, %s" % agora)
    print("")

    sha_antes = sha256_do_snippet()
    medicao = regua.medir(RAIZ)
    sha_depois = sha256_do_snippet()

    ok("o snippet de verdade e byte a byte o mesmo depois da medicao",
       sha_antes == sha_depois,
       "sha antes %s, depois %s" % (sha_antes[:12], sha_depois[:12]))
    ok("o gerador roda contra o banco de hoje e sai com codigo 0",
       medicao["gerador_codigo"] == 0,
       "codigo %s; saida: %s" % (medicao["gerador_codigo"],
                                 medicao["gerador_saida"].strip().splitlines()[-1:] or ""))
    ok("os dois blocos do gerador existem no snippet (CATALOGO e BARRADOS)",
       medicao["blocos_achados"] == ["barrados", "catalogo"],
       "achados: %s" % medicao["blocos_achados"])

    fora = medicao["fora_de_bloco"]
    ok("nenhuma linha de deriva cai FORA dos dois blocos do gerador",
       not fora,
       "%d fora: %s" % (len(fora), [m["linha"].strip()[:60] for m in fora[:3]]))

    total = len(medicao["mudancas"])
    print("")
    print("DERIVA MEDIDA: %d linha(s)" % total)
    for chave, quantas in regua.agrupada_por_causa(medicao["mudancas"]):
        print("  %4d x %s" % (quantas, chave[:110]))
    por_bloco = {}
    for m in medicao["mudancas"]:
        por_bloco[m["bloco"]] = por_bloco.get(m["bloco"], 0) + 1
    if por_bloco:
        print("  por bloco: %s" % ", ".join(
            "%s %d" % (k, v) for k, v in sorted(por_bloco.items(), key=lambda p: str(p[0]))))
    print("")

    if GRAVAR:
        gravar(medicao, agora)
        return 0 if not falhas else 1

    declarado = regua.declaracao(SERIE)
    a_mais, a_menos = regua.comparar_com_declaracao(medicao["mudancas"], declarado)
    ok("a serie de deriva tem declaracao", declarado is not None,
       "escreva a primeira com --gravar")
    ok("a deriva medida e a declarada sao a mesma, linha por linha",
       not a_mais and not a_menos,
       "a mais: %s | a menos: %s" % (a_mais[:3], a_menos[:3]))
    if declarado is not None:
        ok("o total declarado bate com as linhas declaradas",
           declarado.get("total_de_linhas") == sum(declarado.get("linhas", {}).values()),
           "total %s, soma %s" % (declarado.get("total_de_linhas"),
                                  sum(declarado.get("linhas", {}).values())))

    print("")
    if falhas:
        print("REPROVADO: %d afirmacao(oes)" % len(falhas))
        for f in falhas:
            print("  - %s" % f)
        print("")
        print("Se a deriva mudou de proposito (banco novo, ou leva que desembarcou),")
        print("grave a secao nova da serie: conferir-deriva-do-catalogo.py --gravar")
        return 1
    print("APROVADO: deriva de %d linha(s), medida sem tocar no snippet e declarada na serie." % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
