#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Varre as transcricoes do banco de especies atras da clausula de PORTE MAXIMO.

    python3 ferramentas/varrer-porte-maximo.py
    python3 ferramentas/varrer-porte-maximo.py . --gravar

POR QUE ELE EXISTE, e a resposta e uma frase que a leva 9 escreveu no PROMPT.md e
NAO pode cumprir de cabeca: "varrer as transcricoes das 34 do catalogo, gravar o
campo onde a fonte disser *max*, deixar ausente onde a fonte nao disser".

"Onde a fonte disser max" e uma pergunta sobre QUARENTA transcricoes, e a resposta
muda a cada coleta. Respondida a mao ela e uma lista escrita a mao — a mesma
familia que esta ilha ja matou quatro vezes (a lista de portoes do REGISTRO.md, a
lista de paginas do portao da voz, a tabela de levas do indexacao.md e a conta de
categorias possiveis, que virou o varrer-categorias-possiveis.py em 23/09/2026).
O defeito de todas e o mesmo: a lista nao avisa quando alguem esquece de
alimenta-la. Aqui ela decide o ESCOPO de um numero que as tabelas de lotacao
usam para dimensionar aquario.

O QUE ELE CONTA, e sao tres estados e nao dois:
  COM CLAUSULA   — a transcricao traz palavra de maximo E o proprio numero de
                   porte_adulto_cm. Pode (e deve) receber o campo.
  SEM CLAUSULA   — a transcricao traz o numero e NAO diz que ele e maximo. Fica
                   ausente, e ausencia e "nao declarado": a fonte que nao disse
                   nao se corrige de cabeca.
  DIVERGENTE     — o campo escrito no banco discorda do que a varredura ve. E o
                   estado que faz esta ferramenta valer a pena depois de hoje:
                   coleta nova que troque a transcricao aparece aqui.

E ELE ACHA, DE LAMBUJA, O QUE FAZ A FRASE DA PAGINA VALER A TELA: a clausula de
tamanho COMUM, quando a fonte publica os dois. Sao poucas e cada uma e um achado
— a do barbo cereja publica "comprimento comum 2,5 cm" ao lado do maximo de 5,0,
metade do numero que a tabela usa.

O QUE ELE NAO DECIDE, e este e o limite dele: QUAL CLAUSULA COPIAR. Ele imprime as
candidatas; quem escreve o campo e quem le a transcricao inteira, porque recortar
clausula e leitura e nao casamento de palavra. E ele NAO escreve no banco: a
gravacao e do E24, no validar-especies.py, que confere a clausula depois de
escrita. Ferramenta que varre e grava sozinha e as duas metades do mesmo palpite.

A REGUA DE MAXIMO ESTA ESCRITA AQUI, de proposito, e o esquema e lido apenas para
conferir que as duas metades dizem a mesma coisa — a mesma decisao do
gerar-catalogo-especies.py e do varrer-categorias-possiveis.py, e pelo mesmo
motivo (secao 8 do ARQUIPELAGO.md): se este arquivo importasse a regua do
validador, um defeito nela faria as duas metades errarem juntas e concordarem.
"""
import datetime
import io
import json
import os
import re
import sys
import unicodedata

RAIZ = None

# As palavras de maximo que estes DOIS corpos de fonte usam de fato — a base
# cientifica escreve "max length" e "max", e o compendio escreve "maximo". Nao e
# dicionario geral: e o que o banco tem, e quem acrescentar corpo novo acrescenta
# aqui e no validador, nos dois lugares, de proposito.
PALAVRAS_DE_MAXIMO = ("max",)

# As palavras com que os dois corpos declaram o tamanho da MAIORIA dos adultos.
# "comprimento comum" e a forma da base cientifica; "a maioria esta adulta com" e
# a do compendio. `geralmente` ficou FORA: ela aparece em frase de temperamento
# ("especie geralmente pacifica") e traria duas clausulas que nao falam de porte.
PALAVRAS_DE_COMUM = ("comprimento comum", "tamanho comum", "maioria esta adulta",
                     "maioria dos adultos")

NUMERO = re.compile(r"\d+(?:[.,]\d+)?")


def sem_acento(texto):
    return "".join(c for c in unicodedata.normalize("NFD", str(texto or ""))
                   if unicodedata.category(c) != "Mn").lower()


def clausulas(texto):
    """A transcricao partida em clausulas, do jeito que ela foi escrita.

    Os dois corpos separam afirmacao por ponto-e-virgula. A virgula NAO parte:
    "max 5,0 cm TL, comprimento comum 2,5 cm TL" e uma clausula so na fonte, e
    partir nela tiraria o numero decimal do lugar.
    """
    return [p.strip() for p in re.split(r";", texto or "") if p.strip()]


def traz_numero(clausula, valor):
    """O numero do campo esta escrito nesta clausula, no algarismo da fonte?"""
    if valor is None:
        return False
    for bruto in NUMERO.findall(clausula):
        try:
            if round(float(bruto.replace(",", ".")), 4) == round(float(valor), 4):
                return True
        except ValueError:
            pass
    return False


def candidatas_de_maximo(especie):
    """As clausulas que sustentam o campo: palavra de maximo E o numero do porte.

    AS DUAS COISAS, e e a regra inteira desta ferramenta. So a palavra deixaria
    passar a clausula do danio_margaritatus sobre lagoas de "no maximo 30 cm de
    profundidade", que fala da agua e nao do peixe. So o numero deixaria passar a
    clausula que traz o porte sem dizer que ele e maximo — os tres registros que
    escrevem "ate".
    """
    porte = especie.get("porte_adulto_cm")
    achadas = []
    for f in especie.get("fontes", []):
        if "porte_adulto_cm" not in (f.get("campos") or []):
            continue
        for c in clausulas(f.get("referencia")):
            s = sem_acento(c)
            if any(p in s for p in PALAVRAS_DE_MAXIMO) and traz_numero(c, porte):
                achadas.append((f.get("origem"), c))
    return achadas


def candidatas_de_comum(especie):
    """As clausulas que declaram o tamanho da maioria dos adultos.

    Varre TODA fonte do registro, nao so as que declaram porte_adulto_cm: no
    pethia-conchonius quem publica o tamanho comum e o compendio, que nao declara
    o porte. Foi exatamente esse cruzamento que fez o bloco existir.
    """
    achadas = []
    for f in especie.get("fontes", []):
        for c in clausulas(f.get("referencia")):
            s = sem_acento(c)
            if any(p in s for p in PALAVRAS_DE_COMUM):
                achadas.append((f.get("origem"), c))
    return achadas


def escrito_no_banco(especie):
    campo = especie.get("porte_e_maximo_registrado")
    return campo if isinstance(campo, dict) else None


def varrer(banco):
    com, sem, divergentes, comuns = [], [], [], []
    for e in banco["especies"]:
        achadas = candidatas_de_maximo(e)
        campo = escrito_no_banco(e)
        if achadas:
            com.append((e, achadas))
        else:
            sem.append(e)
        # DIVERGENTE nos dois sentidos, porque as duas direcoes doem: campo
        # escrito onde a varredura nao ve clausula afirma o que a fonte nao
        # disse; clausula vista sem campo escrito deixa a pagina sem o escopo.
        if campo and not achadas:
            divergentes.append((e["id"], "campo escrito e NENHUMA clausula de maximo na transcricao"))
        if achadas and not campo:
            divergentes.append((e["id"], "clausula de maximo na transcricao e campo AUSENTE"))
        if campo:
            frase = str(campo.get("frase") or "").strip()
            if frase and not any(frase == c for _, c in achadas):
                divergentes.append((e["id"], "a frase escrita nao e uma das clausulas que a varredura ve"))
        candidatas = candidatas_de_comum(e)
        if candidatas:
            comuns.append((e, candidatas, bool((campo or {}).get("comum"))))
        # A MESMA conferencia dos dois lados para o tamanho comum, pelo mesmo
        # motivo: escrever um comum que nenhuma clausula declara e inventar o
        # numero que a pagina vai usar para dizer "e menos da metade".
        comum = (campo or {}).get("comum")
        if comum and not any(str(comum.get("frase") or "").strip() in c
                             for _, c in candidatas):
            divergentes.append((e["id"], "o comum.frase escrito nao esta em nenhuma "
                                         "clausula de tamanho comum da transcricao"))
    return com, sem, divergentes, comuns


def relatorio(banco):
    com, sem, divergentes, comuns = varrer(banco)
    linhas = []
    w = linhas.append
    total = len(banco["especies"])
    w("== banco ==")
    w("  %d registros | %d com clausula de maximo | %d sem clausula"
      % (total, len(com), len(sem)))
    escritos = sum(1 for e in banco["especies"] if escrito_no_banco(e))
    w("  %d com porte_e_maximo_registrado escrito | %d com tamanho comum declarado"
      % (escritos, sum(1 for _, _, tem in comuns if tem)))
    w("")
    w("== quem NAO tem clausula de maximo, e e por isso que o campo fica ausente ==")
    for e in sorted(sem, key=lambda x: x["id"]):
        refs = [f.get("referencia") or "" for f in e.get("fontes", [])
                if "porte_adulto_cm" in (f.get("campos") or [])]
        trecho = ""
        for r in refs:
            for c in clausulas(r):
                if traz_numero(c, e.get("porte_adulto_cm")):
                    trecho = c[:110]
                    break
            if trecho:
                break
        w("  %-32s %s cm %s" % (e["id"], e.get("porte_adulto_cm"), e.get("porte_medida")))
        w("      a fonte escreve: %s" % trecho)
    w("")
    w("== tamanho COMUM declarado, com a regua de cada lado ==")
    for e, candidatas, tem in sorted(comuns, key=lambda x: x[0]["id"]):
        marca = "escrito" if tem else "NAO escrito"
        w("  %-32s maximo %s cm %s   (%s)"
          % (e["id"], e.get("porte_adulto_cm"), e.get("porte_medida"), marca))
        for origem, c in candidatas:
            w("      %-26s %s" % (origem, c[:120]))
    w("")
    w("== divergencia entre o banco e a transcricao ==")
    if not divergentes:
        w("  nenhuma")
    for rid, texto in divergentes:
        w("  %-32s %s" % (rid, texto))
    return "\n".join(linhas), divergentes


def main():
    global RAIZ
    alvo = ([a for a in sys.argv[1:] if not a.startswith("--")] or ["."])[0]
    RAIZ = os.path.abspath(alvo)
    if os.path.basename(RAIZ) == "ferramentas":
        RAIZ = os.path.dirname(RAIZ)
    banco = json.load(io.open(os.path.join(RAIZ, "dados", "especies-agua-doce.json"),
                              encoding="utf-8"))
    esquema = json.load(io.open(os.path.join(RAIZ, "dados", "esquema-especies.json"),
                                encoding="utf-8"))

    # As duas metades tem de concordar que o campo existe. Se o esquema perder o
    # campo, esta ferramenta para de medir e DIZ isso, em vez de varrer o banco
    # inteiro e imprimir zero com cara de medicao.
    if not any(c["campo"] == "porte_e_maximo_registrado" for c in esquema["campos"]):
        print("ERRO: o esquema nao tem o campo porte_e_maximo_registrado — "
              "a varredura mediria contra um campo que nao existe")
        return 1

    texto, divergentes = relatorio(banco)
    print(texto)

    if "--gravar" in sys.argv:
        serie = os.path.join(RAIZ, "dados", "porte-maximo.md")
        hoje = datetime.date.today().isoformat()
        if not os.path.exists(serie):
            io.open(serie, "w", encoding="utf-8").write(
                "# Serie de escopo do porte — eixo /peixes/ da Aquametria\n\n"
                "Uma secao por varredura, **nunca sobrescrever secao antiga**: a serie so vale "
                "porque cresce. Quem escreve e `ferramentas/varrer-porte-maximo.py . --gravar`. "
                "O que ela conta, o que ela deliberadamente NAO decide e por que a regua mora "
                "nela e nao no esquema esta no cabecalho daquele arquivo.\n\n"
                "**O que esta serie responde:** quantos registros deste banco publicam um porte "
                "que a fonte declarou como MAXIMO REGISTRADO — e nao como o tamanho que o peixe "
                "tem no aquario de quem le. As tabelas de lotacao dimensionam por esse numero.\n")
        with io.open(serie, "a", encoding="utf-8") as fp:
            fp.write("\n## %s\n\n```\n%s\n```\n" % (hoje, texto))
        print("\ngravado em dados/porte-maximo.md (secao %s)" % hoje)

    # DIVERGENCIA E CODIGO DE SAIDA 1, porque ela e a unica coisa que esta
    # ferramenta afirma com certeza: o banco e a transcricao discordam. O resto
    # dela e contagem, e contagem nao reprova nada.
    return 1 if divergentes else 0


if __name__ == "__main__":
    sys.exit(main())
