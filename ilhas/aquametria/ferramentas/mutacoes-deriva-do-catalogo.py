#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AS MUTACOES DO PORTAO DE DERIVA DO CATALOGO.

    python3 ferramentas/mutacoes-deriva-do-catalogo.py

Sem rede. Codigo de saida 0 se NENHUMA mutacao sobreviver, 1 se alguma passar.

O QUE ELAS PROVAM, e por que o `teste-deriva-do-catalogo.py` nao basta sozinho:
um portao verde prova que o mundo de hoje passa, nunca que o portao MORDE. Cada
mutacao daqui quebra uma afirmacao de proposito, numa ILHA DE SOMBRA (copia de
`dados/`, `snippets/` e `ferramentas/` num diretorio temporario — o repositorio
de verdade nunca e tocado), e exige TRES coisas:

  1. que o arquivo mude de verdade (mutacao que nao encontra o alvo e INERTE, e
     aparece nomeada em vez de contar como sucesso);
  2. que o teste saia com codigo 1;
  3. que ele reprove PELA FRASE que a mutacao espera ouvir de volta.

A (3) e a lição de 15/10/2026 desta ilha: reprovar nao e a mesma coisa que
reprovar PELO MOTIVO CERTO — sem a frase, uma mutacao pode disparar outra trava,
voltar verde e nunca ter medido a sua.

E DUAS DELAS SAO MUNDOS QUE TEM DE PASSAR, porque bateria que so sabe reprovar
nao distingue "o portao morde" de "o portao morde tudo".
"""
import io
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REGUA = os.path.join("ferramentas", "regua-deriva-do-catalogo.py")
PORTAO = os.path.join("ferramentas", "conferir-deriva-do-catalogo.py")
TESTE = os.path.join("ferramentas", "teste-deriva-do-catalogo.py")
SNIPPET_REL = os.path.join("snippets", "aquametria-peixes.php")

inertes = []
sobreviventes = []
sem_frase = []
feitas = 0


def ilha_de_sombra():
    tmp = tempfile.mkdtemp(prefix="aqm-mut-deriva-")
    for pasta in ("dados", "snippets", "ferramentas"):
        shutil.copytree(os.path.join(RAIZ, pasta), os.path.join(tmp, pasta),
                        ignore=shutil.ignore_patterns("__pycache__"))
    return tmp


def troca_em(ilha, arquivo, velho, novo):
    """Troca exata, e devolve False se o alvo nao estava la — e isso e INERTE.

    `str.replace` cru de alvo sumido NAO falha: ele devolve o mesmo texto e a
    mutacao vira verde sobre nada. Foi assim que quatro mutacoes de
    `mutacoes-escada.py` morreram caladas em 23/09/2026.
    """
    caminho = os.path.join(ilha, arquivo)
    texto = io.open(caminho, encoding="utf-8").read()
    if velho not in texto:
        return False
    with io.open(caminho, "w", encoding="utf-8") as f:
        f.write(texto.replace(velho, novo, 1))
    return True


def rodar_teste(ilha):
    p = subprocess.Popen([sys.executable, os.path.join(ilha, TESTE)],
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    saida = p.communicate()[0].decode("utf-8", "replace")
    return p.returncode, saida


def rodar_portao(ilha, *extra):
    """O portao na ilha de sombra. Serve a mutacao que PRODUZ o mundo antes de o
    quebrar: ela precisa declarar na serie a deriva que acabou de criar, e quem
    escreve a serie e o proprio portao, com `--gravar`."""
    p = subprocess.Popen([sys.executable, os.path.join(ilha, PORTAO)] + list(extra),
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    saida = p.communicate()[0].decode("utf-8", "replace")
    return p.returncode, saida


def mutacao(rotulo, aplicar, frase):
    """Aplica a mutacao numa ilha de sombra e exige reprovacao PELA frase."""
    global feitas
    feitas += 1
    ilha = ilha_de_sombra()
    try:
        if not aplicar(ilha):
            print("  INERTE  %s — o alvo nao estava no arquivo" % rotulo)
            inertes.append(rotulo)
            return
        codigo, saida = rodar_teste(ilha)
        if codigo == 0:
            print("  SOBREVIVEU  %s" % rotulo)
            sobreviventes.append(rotulo)
            return
        if frase not in saida:
            print("  SEM A FRASE  %s — esperava ouvir %r" % (rotulo, frase))
            sem_frase.append(rotulo)
            return
        print("  ok  %s" % rotulo)
    finally:
        shutil.rmtree(ilha, ignore_errors=True)


def mundo_que_passa(rotulo, aplicar):
    global feitas
    feitas += 1
    ilha = ilha_de_sombra()
    try:
        if aplicar is not None and not aplicar(ilha):
            print("  INERTE  %s — o alvo nao estava no arquivo" % rotulo)
            inertes.append(rotulo)
            return
        codigo, saida = rodar_teste(ilha)
        if codigo != 0:
            print("  REPROVOU MUNDO BOM  %s" % rotulo)
            sobreviventes.append(rotulo)
            return
        print("  ok  %s" % rotulo)
    finally:
        shutil.rmtree(ilha, ignore_errors=True)


print("MUNDOS QUE TEM DE PASSAR")
mundo_que_passa("1. a ilha como ela esta", None)
mundo_que_passa(
    "2. comentario trocado na regua (a bateria nao pode estar presa ao texto)",
    lambda ilha: troca_em(ilha, REGUA, "# -*- coding: utf-8 -*-",
                          "# -*- coding: utf-8 -*-\n# comentario novo, inofensivo"))

print("")
print("QUEBRAS QUE TEM DE REPROVAR")

# A fronteira dos dois lados. Esta e a mutacao que o teste JA achou de verdade:
# a primeira versao da regua media os dois lados com `i <= n <= j`, e com isso
# linha acrescentada ANTES do marcador de abertura virava deriva "de dentro".
mutacao("1. os dois lados do diff medidos com a MESMA fronteira do bloco",
        lambda ilha: troca_em(
            ilha, REGUA,
            'dentro = (i < n <= j) if lado == "+" else (i < n < j)',
            "dentro = i <= n <= j"),
        "FORA dos dois blocos")

mutacao("2. a comparacao com a declaracao olha so o TOTAL",
        lambda ilha: troca_em(
            ilha, REGUA,
            "    for chave in sorted(set(medido) | set(esperado)):",
            "    if sum(medido.values()) == sum(esperado.values()):\n"
            "        return ([], [])\n"
            "    for chave in sorted(set(medido) | set(esperado)):"),
        "ACUSA a troca de mesmo total")

mutacao("3. a assinatura esquece o LADO da mudanca",
        lambda ilha: troca_em(ilha, REGUA, 'chave = m["lado"] + m["linha"]',
                              'chave = m["linha"]'),
        "NAO se cancelam")

mutacao("4. serie ausente lida como deriva zero",
        lambda ilha: troca_em(ilha, REGUA,
                              "    if not os.path.exists(caminho):\n        return None",
                              "    if not os.path.exists(caminho):\n"
                              '        return {"total_de_linhas": 0, "linhas": {}}'),
        "devolve None, nunca zero")

mutacao("5. a declaracao lida e a do FIM do arquivo, nao a do topo",
        lambda ilha: troca_em(ilha, REGUA,
                              '            if linha.strip() == "```":\n                break',
                              '            if linha.strip() == "```":\n'
                              "                dentro = False\n"
                              "                buf2 = buf\n"
                              "                buf = []\n"
                              "                continue"),
        "a do TOPO")

mutacao("6. o portao para de COMPARAR o sha do snippet antes e depois",
        lambda ilha: troca_em(ilha, PORTAO,
                              "       sha_antes == sha_depois,",
                              "       True,"),
        "COMPARA os dois sha")

# A MUTACAO QUE IMPORTA MAIS: o passo destrutivo voltando. Ela roda dentro da
# ilha de sombra, entao o unico snippet que ela poderia reescrever e a copia.
mutacao("7. o gerador volta a ser chamado com a raiz de VERDADE, nao a de sombra",
        lambda ilha: troca_em(ilha, REGUA,
                              '[sys.executable, c["gerador"], sombra]',
                              '[sys.executable, c["gerador"], raiz]'),
        "raiz de SOMBRA")

mutacao("8. a regua para de achar o bloco BARRADOS",
        lambda ilha: troca_em(ilha, REGUA,
                              '    ("barrados", "BARRADOS-INICIO", "BARRADOS-FIM"),',
                              ""),
        "blocos sao achados pelos marcadores")

# A 9 PRODUZ O MUNDO ANTES DE O QUEBRAR, DESDE 21/10/2026, E ELA SOBREVIVEU NO
# DIA EM QUE A DERIVA ZEROU. Ate 20/10 a ilha tinha 74 linhas de deriva de pe, e
# gravar o total esquecendo as linhas deixava a serie dizendo "74 linhas, {}" —
# que o portao reprova na releitura. Em 21/10 a lista de 21/10 regerou o catalogo,
# a deriva virou 0 e {} passou a ser a resposta CERTA: a corrupcao ficou inerte
# sem o `troca_em` perceber, porque o alvo continuava no arquivo. A mutacao passa
# a CRIAR a deriva primeiro — apaga do snippet de sombra uma linha que o gerador
# produz, o que da exatamente uma linha do lado `+` — e a declarar essa deriva na
# serie com o portao LIMPO, para que o mundo de partida seja um mundo que passa.
# So depois ela quebra o `--gravar`. E a "mutacao de duas edicoes" da secao 8 do
# ARQUIPELAGO.md, e aqui a segunda edicao e o mundo, nunca uma segunda regra.
LINHA_DO_CATALOGO = ("\t\t\t\t\t'url' => "
                     "'https://www.fishbase.se/summary/Paracheirodon-innesi',\n")


def mutacao_9(ilha):
    # (1) o mundo: o snippet de sombra perde UMA linha que o gerador produz
    if not troca_em(ilha, SNIPPET_REL, LINHA_DO_CATALOGO, ""):
        return False
    # (2) a serie declara essa deriva, escrita pelo portao ainda LIMPO
    codigo, _ = rodar_portao(ilha, "--gravar")
    if codigo != 0:
        return False
    # (3) e agora a quebra: o --gravar passa a gravar o total e a esquecer as linhas
    return troca_em(ilha, PORTAO, '        "linhas": linhas,', '        "linhas": {},')


mutacao("9. o `--gravar` do portao grava o total e esquece as linhas (com deriva PRODUZIDA)",
        mutacao_9,
        "serie gravada pelo proprio portao")

# A 10 E DUPLA DE PROPOSITO, E A RAZAO E UM ACHADO DESTA BATERIA. A primeira
# versao dela mexia so na afirmacao "a serie de deriva tem declaracao" e
# SOBREVIVEU: sem a serie, o portao continuava vermelho pela afirmacao seguinte,
# a da comparacao linha por linha, que com `declarado is None` tambem acusa. As
# duas metades guardam a mesma porta, e e por isso que nenhuma mutacao SIMPLES
# consegue abri-la — o que a bateria mede aqui e justamente isso: para o
# silencio passar por verde, duas afirmacoes tem de cair juntas.
# A 11 E A IRMA DA 9 E NASCEU NO MESMO DIA, E E ELA QUE GUARDA O CONSERTO DE
# 21/10/2026. Naquele dia a afirmacao do lado da deriva foi afrouxada de
# `== {"+"}` para `<= {"+"}`, porque a forma antiga cobrava DUAS coisas — que
# nenhuma linha fosse do lado `-` e que houvesse pelo menos uma linha — e a
# segunda fazia o portao reprovar justamente quando um desembarque zerava a
# deriva. Afrouxar sem guarda e como se perde uma regua: esta mutacao produz o
# mundo que a metade SOBREVIVENTE tem de pegar — uma linha do lado `-` — e exige
# que o portao a nomeie. Ela e mundo e nao quebra de regra: o snippet de sombra
# GANHA uma linha que o gerador nunca produz, e a serie declara essa deriva com o
# portao limpo, para que a UNICA afirmacao que cai seja a do lado.
MARCA_INICIO = "\t/* CATALOGO-INICIO — gerado por ferramentas/gerar-catalogo-especies.py */\n"


def mutacao_11(ilha):
    if not troca_em(ilha, SNIPPET_REL, MARCA_INICIO,
                    MARCA_INICIO + "\t/* linha que o gerador nunca produz */\n"):
        return False
    codigo, _ = rodar_portao(ilha, "--gravar")
    # o `--gravar` do portao limpo declara a deriva que acabamos de criar; se ele
    # proprio nao conseguir aprovar depois disso, o mundo nao e o que queremos
    return codigo == 0


def mutacao_10(ilha):
    um = troca_em(ilha, PORTAO,
                  '    ok("a serie de deriva tem declaracao", declarado is not None,',
                  '    ok("a serie de deriva tem declaracao", True,')
    dois = troca_em(ilha, REGUA,
                    '        return (["a serie nao tem declaracao nenhuma"], [])',
                    "        return ([], [])")
    return um and dois


mutacao("11. uma linha do lado `-` aparece na deriva, e o portao tem de a nomear",
        mutacao_11,
        "nao tem linha do lado `-`")

mutacao("10. as DUAS afirmacoes que guardam a serie ausente caem juntas",
        mutacao_10,
        "silencio nao e deriva zero")

print("")
ruins = len(sobreviventes) + len(inertes) + len(sem_frase)
if ruins:
    print("REPROVADO: %d de %d mutacoes nao mediram o que deviam" % (ruins, feitas))
    for nome in sobreviventes:
        print("  - sobreviveu (ou reprovou mundo bom): %s" % nome)
    for nome in inertes:
        print("  - inerte: %s" % nome)
    for nome in sem_frase:
        print("  - reprovou por outro motivo: %s" % nome)
    sys.exit(1)
print("APROVADO: %d mutacoes, 0 sobrevivente, 0 inerte, todas cobradas pela FRASE" % feitas)
