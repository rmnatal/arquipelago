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

mutacao("9. o `--gravar` do portao grava o total e esquece as linhas",
        lambda ilha: troca_em(ilha, PORTAO, '        "linhas": linhas,',
                              '        "linhas": {},'),
        "serie gravada pelo proprio portao")

# A 10 E DUPLA DE PROPOSITO, E A RAZAO E UM ACHADO DESTA BATERIA. A primeira
# versao dela mexia so na afirmacao "a serie de deriva tem declaracao" e
# SOBREVIVEU: sem a serie, o portao continuava vermelho pela afirmacao seguinte,
# a da comparacao linha por linha, que com `declarado is None` tambem acusa. As
# duas metades guardam a mesma porta, e e por isso que nenhuma mutacao SIMPLES
# consegue abri-la — o que a bateria mede aqui e justamente isso: para o
# silencio passar por verde, duas afirmacoes tem de cair juntas.
def mutacao_10(ilha):
    um = troca_em(ilha, PORTAO,
                  '    ok("a serie de deriva tem declaracao", declarado is not None,',
                  '    ok("a serie de deriva tem declaracao", True,')
    dois = troca_em(ilha, REGUA,
                    '        return (["a serie nao tem declaracao nenhuma"], [])',
                    "        return ([], [])")
    return um and dois


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
