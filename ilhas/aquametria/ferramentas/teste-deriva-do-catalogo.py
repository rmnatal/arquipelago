#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O PORTAO DA REGUA DE DERIVA DO CATALOGO — e ele tem QUATRO metades.

    python3 ferramentas/teste-deriva-do-catalogo.py

Sem rede. Codigo de saida 0 se tudo passar, 1 se alguma afirmacao cair.

POR QUE QUATRO METADES, e cada uma pega um defeito que as outras nao veem:

  (A) A ARITMETICA, caso a caso, sobre textos encenados. Deriva zero, deriva
      dentro do bloco, deriva FORA do bloco, a assinatura como conjunto
      CONTADO (e nao como total), e a leitura da serie. Isto se prova com
      entradas e nao precisa do gerador.

  (B) O PASSO DESTRUTIVO NAO EXISTE, e esta metade e ESTRUTURAL de proposito.
      A razao de este portao existir e que a medicao antiga escrevia no
      snippet que serve 52 URLs e o restaurava depois, de memoria. Medir
      comportamento nao prova que o passo destrutivo saiu: prova que ele nao
      disparou NESTA passada. Entao esta metade LE os dois arquivos e cobra
      que o snippet de verdade nunca seja aberto para escrita, que o gerador
      so receba raiz de sombra, e que o portao compare o sha256 antes e
      depois. (Secao 8 do ARQUIPELAGO.md, 16/10/2026: "a prova disto e
      ESTRUTURAL e nunca comportamental".)

  (C) O MUNDO QUE O BANCO DE HOJE NAO TEM. A deriva de hoje sao 74 linhas,
      todas do bloco CATALOGO, todas do lado `+`. Um portao medido so contra
      ela ficaria verde sem nunca ver uma REMOCAO, uma troca de mesmo total,
      nem deriva fora de bloco. Esta metade produz os tres mundos.

  (D) O PORTAO INTEIRO, numa ILHA DE SOMBRA. Copia `dados/`, `snippets/` e
      `ferramentas/` para um diretorio temporario e roda o
      `conferir-deriva-do-catalogo.py` de la — verde com a serie declarada,
      VERMELHO sem ela e VERMELHO quando o banco muda. E a unica metade que
      mede o codigo de saida junto com a palavra impressa, que e o que a
      bancada chama de portao nao inerte.
"""
import hashlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FERRAMENTAS = os.path.join(RAIZ, "ferramentas")
SNIPPET = os.path.join(RAIZ, "snippets", "aquametria-peixes.php")
BANCO = os.path.join(RAIZ, "dados", "especies-agua-doce.json")
REGUA = os.path.join(FERRAMENTAS, "regua-deriva-do-catalogo.py")
PORTAO = os.path.join(FERRAMENTAS, "conferir-deriva-do-catalogo.py")

contadas = 0
falhas = []


def afirma(texto, condicao, detalhe=""):
    global contadas
    contadas += 1
    if not condicao:
        falhas.append(texto)
        print("  FALHA %s%s" % (texto, (" — " + detalhe) if detalhe else ""))


def carregar_regua():
    spec = importlib.util.spec_from_file_location("regua_deriva_do_catalogo", REGUA)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def snippet_de_mentira(catalogo_dentro, barrados_dentro=("\tfalse,",), extra_fora=()):
    """Um arquivo com os dois marcadores, no formato que o gerador exige."""
    linhas = ["<?php", "// cabecalho que o gerador nunca toca"]
    linhas += list(extra_fora)
    linhas.append("\t/* CATALOGO-INICIO — gerado por ferramentas/gerar-catalogo-especies.py */")
    linhas += list(catalogo_dentro)
    linhas.append("\t/* CATALOGO-FIM */")
    linhas.append("// meio que o gerador nunca toca")
    linhas.append("\t/* BARRADOS-INICIO — gerado por ferramentas/gerar-catalogo-especies.py */")
    linhas += list(barrados_dentro)
    linhas.append("\t/* BARRADOS-FIM */")
    linhas.append("// rodape que o gerador nunca toca")
    return "\n".join(linhas) + "\n"


# ---------------------------------------------------------------- METADE A
def metade_a(regua):
    print("(A) A ARITMETICA, CASO A CASO")

    base = snippet_de_mentira(["\t'a' => 1,"])
    m = regua.medir_textos(base, base)
    afirma("caso 1: texto igual a si mesmo da deriva ZERO",
           m["mudancas"] == [] and m["fora_de_bloco"] == [])
    afirma("caso 1b: os dois blocos sao achados pelos marcadores",
           m["blocos_achados"] == ["barrados", "catalogo"], str(m["blocos_achados"]))

    depois = snippet_de_mentira(["\t'a' => 1,", "\t'b' => 2,"])
    m = regua.medir_textos(base, depois)
    afirma("caso 2: linha a mais DENTRO do catalogo e deriva, e e do bloco catalogo",
           len(m["mudancas"]) == 1 and m["mudancas"][0]["bloco"] == "catalogo"
           and m["mudancas"][0]["lado"] == "+", str(m["mudancas"]))
    afirma("caso 2b: deriva dentro do bloco NAO cai na lista de fora de bloco",
           m["fora_de_bloco"] == [])

    m = regua.medir_textos(depois, base)
    afirma("caso 3: linha a MENOS e deriva do lado `-` (a direcao que o banco de hoje nao tem)",
           len(m["mudancas"]) == 1 and m["mudancas"][0]["lado"] == "-", str(m["mudancas"]))

    fora = snippet_de_mentira(["\t'a' => 1,"], extra_fora=("// linha que ninguem gerou",))
    m = regua.medir_textos(base, fora)
    afirma("caso 4: linha a mais FORA dos dois blocos e NOMEADA como fora de bloco",
           len(m["fora_de_bloco"]) == 1, str(m["mudancas"]))

    m = regua.medir_textos(base, snippet_de_mentira(["\t'a' => 1,"], barrados_dentro=["\ttrue,"]))
    afirma("caso 5: deriva no bloco BARRADOS e atribuida a ele, e nao ao catalogo",
           [x["bloco"] for x in m["mudancas"]] == ["barrados", "barrados"]
           or {x["bloco"] for x in m["mudancas"]} == {"barrados"}, str(m["mudancas"]))

    # A assinatura e um CONJUNTO CONTADO. Dois mundos de mesmo TOTAL e linhas
    # diferentes tem de discordar — e o total e exatamente o que a prosa do
    # REGISTRO.md guardava ("74 linhas"), que e por que isto e afirmacao.
    um = regua.medir_textos(base, snippet_de_mentira(["\t'a' => 1,", "\t'x' => 9,"]))
    outro = regua.medir_textos(base, snippet_de_mentira(["\t'a' => 1,", "\t'y' => 9,"]))
    afirma("caso 6: dois mundos de mesmo TOTAL (1 linha) tem assinaturas diferentes",
           len(um["mudancas"]) == len(outro["mudancas"])
           and regua.assinatura(um["mudancas"]) != regua.assinatura(outro["mudancas"]))
    a_mais, a_menos = regua.comparar_com_declaracao(
        outro["mudancas"], {"linhas": regua.assinatura(um["mudancas"])})
    afirma("caso 6b: a comparacao com a declaracao ACUSA a troca de mesmo total",
           bool(a_mais) and bool(a_menos), "a mais %s, a menos %s" % (a_mais, a_menos))

    # A assinatura separa os dois LADOS: sem isso, remover e acrescentar a mesma
    # linha se cancelariam e a deriva sumiria do contador.
    mais = [{"lado": "+", "linha": "\tigual,", "ancora": 0, "bloco": "catalogo"}]
    menos = [{"lado": "-", "linha": "\tigual,", "ancora": 0, "bloco": "catalogo"}]
    afirma("caso 7: a mesma linha acrescentada e removida NAO se cancelam na assinatura",
           regua.assinatura(mais) != regua.assinatura(menos))

    # A SERIE: a declaracao que manda e a do TOPO, e arquivo ausente e None.
    tmp = tempfile.mkdtemp(prefix="aqm-deriva-serie-")
    try:
        caminho = os.path.join(tmp, "deriva-do-catalogo.md")
        afirma("caso 8: serie inexistente devolve None, nunca zero",
               regua.declaracao(caminho) is None)
        with io.open(caminho, "w", encoding="utf-8") as f:
            f.write("# cabecalho\n\n## 2026-10-16 19h5xZ\n\n```json\n"
                    + json.dumps({"total_de_linhas": 2, "linhas": {"+a": 2}})
                    + "\n```\n\n## 2026-10-15 13h19Z\n\n```json\n"
                    + json.dumps({"total_de_linhas": 34, "linhas": {"+velha": 34}})
                    + "\n```\n")
        d = regua.declaracao(caminho)
        afirma("caso 9: com duas secoes, a declaracao lida e a do TOPO (a mais nova)",
               d is not None and d.get("total_de_linhas") == 2, str(d))
        with io.open(caminho, "w", encoding="utf-8") as f:
            f.write("# cabecalho sem secao nenhuma\n")
        afirma("caso 10: serie sem bloco json devolve None",
               regua.declaracao(caminho) is None)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    a_mais, a_menos = regua.comparar_com_declaracao(mais, None)
    afirma("caso 11: declaracao ausente e acusada, e nao tratada como deriva zero",
           bool(a_mais))


# ---------------------------------------------------------------- METADE B
def metade_b():
    print("(B) O PASSO DESTRUTIVO NAO EXISTE — afirmacao ESTRUTURAL")

    regua_txt = io.open(REGUA, encoding="utf-8").read()
    portao_txt = io.open(PORTAO, encoding="utf-8").read()

    corpo = regua_txt.split('"""', 2)[-1]
    afirma("estrutural 1: a regua nunca abre arquivo para escrita fora da sombra",
           corpo.count('"w"') == 1 and 'os.path.join(sombra' in corpo,
           "ocorrencias de modo w no corpo: %d" % corpo.count('"w"'))
    afirma("estrutural 2: o gerador so e chamado com a raiz de SOMBRA",
           'c["gerador"], sombra]' in corpo and 'c["gerador"], raiz]' not in corpo)
    afirma("estrutural 3: a sombra e um diretorio temporario e e apagada no fim",
           "tempfile.mkdtemp" in corpo and "shutil.rmtree(sombra" in corpo)
    afirma("estrutural 4: `medir` LE o snippet de verdade (ler) e nao o abre para escrita",
           'antes = ler(c["snippet"])' in corpo)

    corpo_portao = portao_txt.split('"""', 2)[-1]
    afirma("estrutural 5: o portao mede o sha256 do snippet ANTES e DEPOIS da medicao",
           corpo_portao.count("sha256_do_snippet()") >= 2)
    afirma("estrutural 6: o portao COMPARA os dois sha numa afirmacao",
           "sha_antes == sha_depois" in corpo_portao)
    afirma("estrutural 7: o portao nao escreve no snippet em nenhuma linha",
           "aquametria-peixes.php" in corpo_portao
           and 'io.open(SNIPPET, "w"' not in corpo_portao)
    # O portao ESCREVE a serie (`--gravar`) e nao a LE por conta propria: quem
    # le e a regua. Copia propria do parser aqui faria as duas metades
    # discordarem sobre qual secao manda — e e a secao do topo que manda.
    afirma("estrutural 8: o portao le a serie pela regua, sem copia propria do parser",
           "regua.declaracao(SERIE)" in corpo_portao
           and "json.loads" not in corpo_portao)

    # E a metade de comportamento, que sozinha nao provaria nada: o sha do
    # snippet de verdade nao muda com uma medicao inteira.
    regua = carregar_regua()
    with io.open(SNIPPET, "rb") as f:
        antes = hashlib.sha256(f.read()).hexdigest()
    regua.medir(RAIZ)
    with io.open(SNIPPET, "rb") as f:
        depois = hashlib.sha256(f.read()).hexdigest()
    afirma("comportamento: uma medicao inteira deixa o snippet de verdade byte a byte igual",
           antes == depois)


# ---------------------------------------------------------------- METADE C
def metade_c(regua):
    print("(C) O MUNDO QUE O BANCO DE HOJE NAO TEM")

    hoje = regua.medir(RAIZ)
    afirma("a deriva de hoje e medida e esta inteira dentro dos blocos do gerador",
           hoje["fora_de_bloco"] == [] and hoje["gerador_codigo"] == 0,
           "fora %d, codigo %s" % (len(hoje["fora_de_bloco"]), hoje["gerador_codigo"]))
    # ESTA AFIRMACAO EXIGIA QUE A DERIVA EXISTISSE, E REPROVOU NO DIA EM QUE ELA
    # ZEROU — 21/10/2026, quando a lista de 21/10 regerou o catalogo e as 74
    # linhas de 16/10 desembarcaram. Escrita como `== {"+"}`, ela cobrava duas
    # coisas de uma vez: que nenhuma linha fosse do lado `-` (o que ela existe
    # para dizer, porque e por isso que o lado `-` se encena nos mundos abaixo) e
    # que houvesse PELO MENOS UMA linha (o que e o estado do banco naquele dia, e
    # nao uma propriedade da regua). Deriva zero e o ALVO de todo desembarque,
    # entao a segunda metade fazia o portao reprovar exatamente quando o trabalho
    # dava certo. Agora ela cobra so a primeira, e conjunto vazio passa.
    #
    # E A FAMILIA E A MESMA DOS QUATRO CASOS DO E28 CONSERTADOS NO MESMO DIA, no
    # `testar-validador-especies.py`: afirmacao presa ao estado de hoje do banco
    # vence sozinha no dia em que o banco anda. Quem a reapertar para `== {"+"}`
    # volta a travar o proximo desembarque, e a mutacao 11 do
    # `mutacoes-deriva-do-catalogo.py` reprova se o lado `-` deixar de ser cobrado.
    lados = {m["lado"] for m in hoje["mudancas"]}
    afirma("a deriva de hoje nao tem linha do lado `-` — por isso o lado `-` se encena",
           lados <= {"+"},
           "lados medidos: %s (deriva de %d linha(s))" % (sorted(lados) or "nenhum",
                                                          len(hoje["mudancas"])))

    # MUNDO 1: o banco perde um campo que o catalogo publica. A deriva tem de
    # MUDAR, e e assim que o portao descobre banco mexido sem declaracao.
    banco = json.load(io.open(BANCO, encoding="utf-8"))
    alvo = None
    for e in banco["especies"]:
        if e.get("nomes_populares_br"):
            alvo = e
            break
    afirma("mundo 1: o banco tem registro com nome popular para encenar", alvo is not None)
    if alvo is not None:
        alvo["nomes_populares_br"] = list(alvo["nomes_populares_br"]) + ["nome-que-nao-existe"]
        outro = regua.medir(RAIZ, banco_texto=json.dumps(banco, ensure_ascii=False))
        afirma("mundo 1: banco mexido muda a assinatura da deriva",
               regua.assinatura(outro["mudancas"]) != regua.assinatura(hoje["mudancas"]))
        a_mais, _ = regua.comparar_com_declaracao(
            outro["mudancas"], {"linhas": regua.assinatura(hoje["mudancas"])})
        afirma("mundo 1: a comparacao com a declaracao de hoje ACUSA o banco mexido",
               bool(a_mais), str(a_mais[:2]))

    # MUNDO 2: o snippet que o gerador escreve nao e o que o portao compara —
    # o caso em que deriva nasce FORA dos dois blocos. Nao acontece no banco de
    # hoje, e e o unico jeito de a afirmacao do fora-de-bloco nao ser inerte.
    snippet = io.open(SNIPPET, encoding="utf-8").read()
    mexido = "// linha de fora que ninguem gerou\n" + snippet
    afirma("mundo 2: a encenacao mexe de verdade no arquivo que o gerador recebe",
           mexido != snippet)
    m = regua.medir(RAIZ, snippet_texto=mexido)
    afirma("mundo 2: linha fora dos blocos no arquivo que o gerador recebe e NOMEADA",
           len(m["fora_de_bloco"]) >= 1, "fora %d" % len(m["fora_de_bloco"]))


# ---------------------------------------------------------------- METADE D
def ilha_de_sombra():
    tmp = tempfile.mkdtemp(prefix="aqm-deriva-ilha-")
    for pasta in ("dados", "snippets", "ferramentas"):
        shutil.copytree(os.path.join(RAIZ, pasta), os.path.join(tmp, pasta),
                        ignore=shutil.ignore_patterns("__pycache__"))
    return tmp


def rodar_portao(ilha, *extra):
    p = subprocess.Popen(
        [sys.executable, os.path.join(ilha, "ferramentas", "conferir-deriva-do-catalogo.py")]
        + list(extra), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    saida = p.communicate()[0].decode("utf-8", "replace")
    return p.returncode, saida


def metade_d():
    print("(D) O PORTAO INTEIRO, NUMA ILHA DE SOMBRA")
    ilha = ilha_de_sombra()
    try:
        codigo, saida = rodar_portao(ilha)
        afirma("o portao APROVA a ilha como ela esta, e sai com 0",
               codigo == 0 and "APROVADO" in saida, "codigo %s" % codigo)
        afirma("e ele imprime a deriva medida, nao so o veredito",
               "DERIVA MEDIDA:" in saida)

        serie = os.path.join(ilha, "dados", "deriva-do-catalogo.md")
        guardada = io.open(serie, encoding="utf-8").read()
        os.remove(serie)
        codigo, saida = rodar_portao(ilha)
        afirma("sem a serie o portao REPROVA e sai com 1 — silencio nao e deriva zero",
               codigo == 1 and "REPROVADO" in saida, "codigo %s" % codigo)
        afirma("e ele diz qual e o conserto, que e um comando",
               "--gravar" in saida)

        codigo, saida = rodar_portao(ilha, "--gravar")
        afirma("--gravar escreve a serie e o portao volta a aprovar",
               codigo == 0 and os.path.exists(serie))
        codigo, saida = rodar_portao(ilha)
        afirma("a serie gravada pelo proprio portao e lida por ele sem reclamar",
               codigo == 0 and "APROVADO" in saida, saida[-200:])

        with io.open(serie, "w", encoding="utf-8") as f:
            f.write(guardada)

        banco = os.path.join(ilha, "dados", "especies-agua-doce.json")
        d = json.load(io.open(banco, encoding="utf-8"))
        for e in d["especies"]:
            if e.get("nomes_populares_br"):
                e["nomes_populares_br"] = list(e["nomes_populares_br"]) + ["encenado"]
                break
        with io.open(banco, "w", encoding="utf-8") as f:
            f.write(json.dumps(d, ensure_ascii=False))
        codigo, saida = rodar_portao(ilha)
        afirma("banco mexido sem declaracao nova: o portao REPROVA e sai com 1",
               codigo == 1 and "REPROVADO" in saida, "codigo %s" % codigo)
        afirma("e a reprovacao nomeia a linha que apareceu, nao so o total",
               "medida(s) contra" in saida or "a mais" in saida)
    finally:
        shutil.rmtree(ilha, ignore_errors=True)


def main():
    regua = carregar_regua()
    metade_a(regua)
    metade_b()
    metade_c(regua)
    metade_d()
    print("")
    if falhas:
        print("REPROVADO: %d de %d afirmacoes" % (len(falhas), contadas))
        for f in falhas:
            print("  - %s" % f)
        return 1
    print("APROVADO: %d afirmacoes, 0 falha" % contadas)
    return 0


if __name__ == "__main__":
    sys.exit(main())
