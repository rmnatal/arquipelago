#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O PORTAO DA REGUA DE CORPOS DE FONTE — e ele tem TRES metades, nao uma.

    python3 ferramentas/teste-regua-de-corpos.py

Sem rede. Codigo de saida 0 se tudo passar, 1 na primeira falha contada.

POR QUE TRES METADES, e cada uma pega um defeito que as outras duas nao veem:

  (A) A REGUA, caso a caso. `propria` conta como si, espelho colapsa, `reproduz`
      colapsa no corpo que reproduz, `indeterminada` nao conta, host nao declarado nao
      conta e e NOMEADO. Isto e aritmetica e se prova com entradas.

  (B) NENHUM CONSUMIDOR TEM COPIA PROPRIA. Esta e a metade que a ilha pagou tres vezes
      e e a razao de o arquivo existir: em 15/10/2026 a tabela de corpos saiu do
      hostname e foi para o esquema, e o cabecalho daquela mudanca escreveu "agora a
      regua e uma so" — quando ela era QUATRO. As duas que MEDEM foram consertadas; as
      duas que DECIDEM O QUE VAI A TELA continuaram contando corpo pelo prefixo da
      referencia. Regra nova nao tem como alcancar copia que ninguem sabe que existe,
      entao esta metade NAO mede comportamento: ela le os arquivos e cobra que os
      quatro chamem a regua e que nenhum redefina a contagem por conta propria.

  (C) O MUNDO QUE O ESQUEMA PERMITE E O BANCO AINDA NAO TEM. As duas metades acima
      passariam com o buraco aberto, porque no banco de HOJE as quatro reguas dao a
      mesma resposta — medido em 16/10/2026: zero divergencia em 40 registros. O que as
      separava era o mundo em que uma fonte `indeterminada` ou um `reproduz` entra no
      registro, e esse mundo tem nome e data: o usgs-nas foi OFERECIDO E RECUSADO em
      15/10/2026 para o `poecilia-reticulata`, e a recusa vivia so como prosa no
      esquema. Medido antes do conserto, com a fonte acrescentada ao guppy:

          validador     1 corpo  -> BARRA
          gerador       2 corpos -> PUBLICA
          teste-peixes  2 corpos -> PUBLICA

      Esta metade PRODUZ esse mundo num banco temporario e cobra que o GERADOR barre o
      registro. Regua que so mede o banco de hoje e regua com metade do mundo
      desligada.
"""
import copy
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FERRAMENTAS = os.path.join(RAIZ, "ferramentas")
ESQUEMA = os.path.join(RAIZ, "dados", "esquema-especies.json")
BANCO = os.path.join(RAIZ, "dados", "especies-agua-doce.json")
SNIPPET = os.path.join(RAIZ, "snippets", "aquametria-peixes.php")

total = 0
falhas = 0


def afirma(texto, condicao, detalhe=""):
    global total, falhas
    total += 1
    if condicao:
        print("  ok    " + texto)
    else:
        falhas += 1
        print("  FALHA " + texto + (("  -> " + str(detalhe)) if detalhe else ""))


def carregar_regua():
    caminho = os.path.join(FERRAMENTAS, "regua-corpos-de-fonte.py")
    spec = importlib.util.spec_from_file_location("regua_corpos_de_fonte", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def fonte(url, campos=("porte_adulto_cm",), ref="Corpo qualquer — ficha"):
    return {"origem": "base-cientifica-via-busca", "status": "base-cientifica-via-busca",
            "referencia": ref, "url": url, "verificado_em": "2026-10-16",
            "campos": list(campos)}


# ---------------------------------------------------------------- (A) a regua
def metade_a(regua, esquema):
    print("\n### (A) a regua, caso a caso")
    regua.carregar(esquema)

    afirma("propria conta como si (fishbase.se -> fishbase)",
           regua.corpo_contavel("https://fishbase.se/x") == "fishbase",
           regua.corpo_contavel("https://fishbase.se/x"))
    afirma("o 'www.' nao cria um corpo novo",
           regua.corpo_contavel("https://www.fishbase.se/x") == "fishbase")
    afirma("espelho colapsa: fishbase.se e fishbase.org sao UM corpo",
           len(regua.corpos_de({"fontes": [fonte("https://fishbase.se/a"),
                                           fonte("https://fishbase.org/b")]})) == 1)
    afirma("dois corpos proprios contam dois",
           len(regua.corpos_de({"fontes": [fonte("https://fishbase.se/a"),
                                           fonte("https://seriouslyfish.com/b")]})) == 2)
    afirma("indeterminada NAO conta (usgs-nas, recusado em 15/10)",
           regua.corpo_contavel("https://nas.er.usgs.gov/x") is None)
    afirma("indeterminada esta DECLARADA, e nao e o mesmo que ausente",
           regua.corpo_declarado("https://nas.er.usgs.gov/x") is not None)
    afirma("host nao declarado nao conta",
           regua.corpo_contavel("https://corpo-que-ninguem-declarou.org/x") is None)
    afirma("host nao declarado e NOMEADO por urls_sem_corpo_declarado",
           regua.urls_sem_corpo_declarado(
               {"fontes": [fonte("https://corpo-que-ninguem-declarou.org/x"),
                           fonte("https://fishbase.se/a")]})
           == ["https://corpo-que-ninguem-declarou.org/x"])

    # o ramo `reproduz` nao tem ocupante no esquema de hoje, entao a afirmacao PRODUZ o
    # mundo em vez de o supor — e e por isso que ela mora aqui e nao numa mutacao.
    com_reprodutor = copy.deepcopy(esquema)
    com_reprodutor["corpos_de_fonte"]["corpos"].append(
        {"nome": "reprodutor-de-teste", "hosts": ["reprodutor-de-teste.org"],
         "procedencia": "reproduz", "reproduz": "fishbase",
         "por_que": "mundo produzido por teste-regua-de-corpos.py"})
    regua.carregar(com_reprodutor)
    afirma("reproduz colapsa no corpo que reproduz",
           regua.corpo_contavel("https://reprodutor-de-teste.org/x") == "fishbase")
    afirma("reprodutor + o corpo que ele reproduz contam UM corpo, em hosts diferentes",
           len(regua.corpos_de({"fontes": [fonte("https://fishbase.se/a"),
                                           fonte("https://reprodutor-de-teste.org/b")]})) == 1)
    regua.carregar(esquema)

    por_campo = regua.corpos_por_campo(
        {"fontes": [fonte("https://nas.er.usgs.gov/x", campos=["temperatura_C"])]})
    afirma("campo sustentado SO por indeterminada aparece na chave com conjunto vazio",
           por_campo.get("temperatura_C") == set(), por_campo)
    afirma("o vocabulario da regua e o do esquema, nao uma copia dele",
           set(regua.PROCEDENCIAS)
           == set(esquema["corpos_de_fonte"]["vocabulario_de_procedencia"]),
           regua.PROCEDENCIAS)


# -------------------------------------------- (B) nenhum consumidor tem copia
CONSUMIDORES = ("validar-especies.py", "varrer-categorias-possiveis.py",
                "gerar-catalogo-especies.py", "teste-peixes.py")


def metade_b():
    print("\n### (B) nenhum consumidor conta corpo por conta propria")
    for nome in CONSUMIDORES:
        texto = open(os.path.join(FERRAMENTAS, nome), encoding="utf-8").read()
        afirma("%s carrega a regua" % nome, "regua-corpos-de-fonte.py" in texto)
        # `def corpos_de(` de volta num consumidor e a copia ressuscitando. A regua
        # propria e o unico arquivo onde estes nomes podem ser definidos.
        #
        # A ANCORA E `^\s*def`, COM O ESPACO, E NAO `^def` — e quem achou a diferenca foi
        # a mutacao 2 do `mutacoes-regua-de-corpos.py`, que SOBREVIVEU a primeira versao
        # desta afirmacao. Ela devolve a contagem propria ao `teste-peixes.py` definindo-a
        # DENTRO da funcao que a usa, indentada, e `^def` ancorado na coluna zero nao a
        # via. Copia aninhada e copia: a regua tem de cobrar a definicao em qualquer
        # indentacao, e o rebind do nome para qualquer coisa que nao venha da regua.
        redefine = re.findall(
            r"(?m)^[ \t]*def[ \t]+(corpo_contavel|corpos_de|corpo_declarado)[ \t]*\(",
            texto)
        # O REBIND SE MEDE PELO LADO DIREITO, E NAO POR LOOKAHEAD NEGATIVO — a primeira
        # versao usava `=\s*(?!regua_corpos\.)` e acusava as proprias linhas de alias do
        # validador: o `\s*` casa ZERO caracteres por backtracking, o lookahead olha o
        # espaco antes do nome e "nao e regua_corpos." passa a ser verdade. Asserir o que o
        # lado direito E custa uma linha e nao tem essa fuga.
        rebind = []
        for nome_lig, direita in re.findall(
                r"(?m)^[ \t]*(corpo_contavel|corpos_de|corpo_declarado)[ \t]*=[ \t]*(\S+)",
                texto):
            if not direita.startswith(("regua_corpos.", "mod.")):
                rebind.append("%s = %s" % (nome_lig, direita))
        afirma("%s nao redefine a contagem (%s)"
               % (nome, ", ".join(redefine + rebind) or "nenhuma"),
               not redefine and not rebind, redefine + rebind)


# --------------------------------------------------- (C) o mundo, pelo gerador
def gerador_sobre(banco):
    """Roda gerar-catalogo-especies.py sobre um banco temporario e devolve a saida."""
    tmp = tempfile.mkdtemp(prefix="aqm-regua-corpos-")
    try:
        os.makedirs(os.path.join(tmp, "dados"))
        os.makedirs(os.path.join(tmp, "snippets"))
        shutil.copy(ESQUEMA, os.path.join(tmp, "dados", "esquema-especies.json"))
        shutil.copy(SNIPPET, os.path.join(tmp, "snippets", "aquametria-peixes.php"))
        with open(os.path.join(tmp, "dados", "especies-agua-doce.json"), "w",
                  encoding="utf-8") as f:
            json.dump(banco, f, ensure_ascii=False)
        p = subprocess.run([sys.executable,
                            os.path.join(FERRAMENTAS, "gerar-catalogo-especies.py"), tmp],
                           capture_output=True, text=True)
        return p.returncode, p.stdout + p.stderr
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def guppy_barrado(saida):
    """O gerador barrou o poecilia-reticulata por falta de dois corpos?"""
    for linha in saida.split("\n"):
        if "barrado:" in linha and "poecilia-reticulata" in linha:
            return "duas fontes distintas" in linha
    return False


def metade_c(banco_real, regua, esquema):
    print("\n### (C) o mundo que o esquema permite e o banco ainda nao tem")

    cod, saida = gerador_sobre(banco_real)
    afirma("controle: o gerador roda sobre o banco real", cod == 0, saida[-400:])
    # O NUMERO DEIXOU DE SER LITERAL EM 21/10/2026. Esta afirmacao procurava
    # "podem virar ficha: 34 de 34" e reprovou no dia em que o catalogo foi a 35,
    # porque a lista de 21/10 deu segundo corpo ao guppy. Contagem de catalogo
    # digitada num portao reprova em TODA leva — ela mede o calendario, nao a
    # regua. O que esta metade precisa do controle e outra coisa: que as duas
    # pontas da conta do gerador fechem entre si. Essa propriedade nao vence.
    m_conta = re.search(r"podem virar ficha: (\d+) de (\d+) no catalogo", saida)
    afirma("controle: o gerador declara a conta do catalogo, e as duas pontas fecham",
           m_conta is not None and m_conta.group(1) == m_conta.group(2),
           [l for l in saida.split("\n") if "podem virar ficha" in l])

    # O MUNDO DO CORPO UNICO E CONSTRUIDO, E NAO ENCONTRADO — 21/10/2026. Ate hoje
    # estas afirmacoes usavam o guppy como ele estava no banco: ele era o unico
    # registro barrado por UM motivo so, "duas fontes de corpos distintos", e isso
    # o tornava a cobaia perfeita. A lista de 21/10 lhe deu o segundo corpo, o
    # guppy entrou no catalogo, e as tres afirmacoes que o usavam viraram FALSAS
    # de uma vez — nenhuma delas por defeito da regua. E a mesma lição dos quatro
    # casos do E28 e da afirmacao do lado da deriva, consertados no mesmo dia:
    # afirmacao presa ao estado de hoje do banco vence sozinha quando o banco anda.
    #
    # Agora o mundo e produzido: tiramos do guppy toda fonte cujo corpo CONTAVEL
    # nao e o primeiro dele, o que o devolve ao estado de "um corpo so" seja qual
    # for o banco do dia. A regua que decide isso e a mesma que esta metade mede —
    # e ela esta sob as afirmacoes da metade (A), que a medem caso a caso.
    regua.carregar(esquema)

    def guppy_com_um_corpo_so(banco):
        b = copy.deepcopy(banco)
        for e in b["especies"]:
            if e["id"] != "poecilia-reticulata":
                continue
            primeiro = regua.corpo_contavel(e["fontes"][0]["url"])
            e["fontes"] = [f for f in e["fontes"]
                           if regua.corpo_contavel(f["url"]) == primeiro]
        return b

    um_corpo = guppy_com_um_corpo_so(banco_real)
    cod, saida_um = gerador_sobre(um_corpo)
    afirma("o mundo PRODUZIDO tem o guppy barrado por um corpo so",
           cod == 0 and guppy_barrado(saida_um),
           [l for l in saida_um.split("\n") if "poecilia-reticulata" in l])
    # E a outra ponta da mesma prova: no banco REAL de hoje ele nao esta barrado
    # assim, senao a afirmacao de cima passaria sem o mundo ser produzido.
    afirma("e no banco real de hoje ele NAO esta barrado por isso — o mundo e produzido mesmo",
           not guppy_barrado(saida),
           [l for l in saida.split("\n") if "poecilia-reticulata" in l])

    def com_fonte_no_guppy(f):
        b = copy.deepcopy(um_corpo)
        for e in b["especies"]:
            if e["id"] == "poecilia-reticulata":
                e["fontes"].append(f)
        return b

    # (1) o mundo medido em 16/10/2026: a fonte indeterminada que foi oferecida e
    # recusada em 15/10 para ESTE registro. Antes do conserto o gerador a contava como
    # segundo corpo e punha o guppy na tela.
    indeterminada = fonte("https://nas.er.usgs.gov/queries/FactSheet.aspx?SpeciesID=863",
                          campos=["porte_adulto_cm", "porte_medida"],
                          ref="USGS NAS — Poecilia reticulata, ficha da especie")
    cod, saida = gerador_sobre(com_fonte_no_guppy(indeterminada))
    afirma("fonte indeterminada NAO vira segundo corpo: o gerador barra o guppy",
           guppy_barrado(saida),
           [l for l in saida.split("\n") if "poecilia-reticulata" in l])

    # (2) o reprodutor, que e o buraco que o E26 nomeou: outro host, o numero de um
    # terceiro. Precisa do esquema com o corpo declarado, entao o mundo e produzido nos
    # dois arquivos ao mesmo tempo.
    print("  (o mundo do reprodutor precisa do esquema, e ele e produzido junto)")
    tmp = tempfile.mkdtemp(prefix="aqm-regua-corpos-rep-")
    try:
        os.makedirs(os.path.join(tmp, "dados"))
        os.makedirs(os.path.join(tmp, "snippets"))
        shutil.copy(SNIPPET, os.path.join(tmp, "snippets", "aquametria-peixes.php"))
        esq = json.load(open(ESQUEMA, encoding="utf-8"))
        esq["corpos_de_fonte"]["corpos"].append(
            {"nome": "reprodutor-de-teste", "hosts": ["reprodutor-de-teste.org"],
             "procedencia": "reproduz", "reproduz": "fishbase",
             "por_que": "mundo produzido por teste-regua-de-corpos.py"})
        with open(os.path.join(tmp, "dados", "esquema-especies.json"), "w",
                  encoding="utf-8") as f:
            json.dump(esq, f, ensure_ascii=False)
        b = com_fonte_no_guppy(fonte("https://reprodutor-de-teste.org/poecilia-reticulata",
                                     campos=["porte_adulto_cm", "porte_medida"],
                                     ref="Fishes of the World — Poecilia reticulata"))
        with open(os.path.join(tmp, "dados", "especies-agua-doce.json"), "w",
                  encoding="utf-8") as f:
            json.dump(b, f, ensure_ascii=False)
        p = subprocess.run([sys.executable,
                            os.path.join(FERRAMENTAS, "gerar-catalogo-especies.py"), tmp],
                           capture_output=True, text=True)
        afirma("reprodutor noutro host NAO vira segundo corpo: o gerador barra o guppy",
               guppy_barrado(p.stdout + p.stderr),
               [l for l in (p.stdout + p.stderr).split("\n") if "poecilia-reticulata" in l])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    # (3) corpo NAO DECLARADO: antes do conserto bastava a referencia ter nome legivel
    # para a fonte viajar para a tela. Agora o gerador a recusa pelo nome da falta.
    #
    # E A FONTE VAI NUM REGISTRO QUE PASSA, nao no guppy, e o motivo e uma ordem do
    # proprio gerador que esta afirmacao descobriu: registro barrado no portao de CAMPOS
    # nunca chega ao laco das fontes (ha um `continue` antes dele), entao a recusa por
    # corpo nao declarado so alcanca quem passou em todo o resto. Isso esta certo —
    # barrado e barrado, e nomear duas vezes a mesma falta nao informa ninguem —, mas
    # cobrar a recusa no guppy fazia a afirmacao medir o `continue` em vez da recusa.
    nao_declarado = fonte("https://corpo-que-ninguem-declarou.org/ficha",
                          campos=["porte_adulto_cm"],
                          ref="Corpo Que Ninguem Declarou — ficha")
    b = copy.deepcopy(banco_real)
    alvo = "paracheirodon-innesi"      # passa no portao de pagina hoje
    for e in b["especies"]:
        if e["id"] == alvo:
            e["fontes"].append(nao_declarado)
    cod, saida = gerador_sobre(b)
    afirma("corpo nao declarado PARA o gerador, com a url e o registro na mensagem",
           cod != 0 and "corpo nao declarado em corpos_de_fonte" in saida
           and "corpo-que-ninguem-declarou.org" in saida and alvo in saida,
           (cod, [l for l in saida.split("\n") if "nao declarado" in l]))
    afirma("e ele NAO vira motivo de tela: nada foi escrito no bloco de barrados",
           "barrado: " + alvo not in saida,
           [l for l in saida.split("\n") if "barrado:" in l])


def main():
    regua = carregar_regua()
    esquema = json.load(open(ESQUEMA, encoding="utf-8"))
    banco_real = json.load(open(BANCO, encoding="utf-8"))

    metade_a(regua, esquema)
    metade_b()
    metade_c(banco_real, regua, esquema)

    print("\n%d afirmacoes, %d falha(s)" % (total, falhas))
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
