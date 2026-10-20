#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mutila a `regua-alvos-de-portao.py` numa ilha de SOMBRA e exige que o
`teste-alvos-de-portao.py` reprove — e reprove PELA FRASE certa.

Sem rede. A sombra leva so `ferramentas/`, porque esta regua le a arvore
sintatica dos arquivos dela e nao pergunta nada a snippet nem a banco.

POR QUE CADA MUTACAO EXISTE: a regua resolve o nome do alvo por cinco caminhos
diferentes (constante, variavel, parametro, chave, `or`), e cada caminho que
morrer em silencio devolve a esta pasta o ponto cego que o item 7 nomeou. Cada
mutacao mata UM caminho. As tres ultimas atacam a CONTA em vez da fiacao, e a
mais importante e a que faz `invisiveis()` devolver `[]` por construcao: regua
que nunca acha nada passa por regua verde para sempre.
"""

import io
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGUA = os.path.join("ferramentas", "regua-alvos-de-portao.py")
TESTE = os.path.join("ferramentas", "teste-alvos-de-portao.py")

inertes = []
sobreviventes = []
sem_frase = []
feitas = 0


def ilha_de_sombra():
    tmp = tempfile.mkdtemp(prefix="aqm-mut-alvos-")
    shutil.copytree(os.path.join(RAIZ, "ferramentas"), os.path.join(tmp, "ferramentas"),
                    ignore=shutil.ignore_patterns("__pycache__"))
    return tmp


def troca_em(ilha, arquivo, velho, novo):
    """Troca exata, e devolve False se o alvo nao estava la — e isso e INERTE.

    A trava de alvo exato existe pelo motivo que o fecho de 19/10 escreveu:
    sem ela, mutacao de alvo sumido passa medindo nada e o relatorio diz
    "0 sobrevivente"."""
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
        if "Traceback" in saida:
            print("  SEM A FRASE  %s — morreu de traceback em vez de reprovar" % rotulo)
            sem_frase.append(rotulo)
            return
        if frase not in saida:
            print("  SEM A FRASE  %s — esperava ouvir %r" % (rotulo, frase))
            sem_frase.append(rotulo)
            return
        print("  ok  %s" % rotulo)
    finally:
        shutil.rmtree(ilha, ignore_errors=True)


def mundo_que_passa(rotulo, aplicar):
    """Mundo que TEM de passar. Portao que reprova tudo nao mede nada."""
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


def main():
    print("MUTACOES DO PORTAO DOS ALVOS DE PORTAO — ilha de sombra, sem rede\n")

    # ---- A FIACAO: um caminho de resolucao por mutacao ----
    mutacao(
        "1. a regua para de seguir VARIAVEL",
        lambda i: troca_em(i, REGUA,
                           "            for valor in self.atribuicoes.get(no.id, []):",
                           "            for valor in []:"),
        "carga por variavel e indireta",
    )
    mutacao(
        "2. a regua para de seguir PARAMETRO ate o sitio de chamada",
        lambda i: troca_em(i, REGUA,
                           "            if dono is not None and (dono, no.id) in self.indice_do_parametro:",
                           "            if False:"),
        "carga por parametro chega ao literal",
    )
    mutacao(
        "3. a regua para de atravessar o `or` do valor padrao",
        lambda i: troca_em(i, REGUA,
                           "        if isinstance(no, ast.BoolOp):",
                           "        if False and isinstance(no, ast.BoolOp):"),
        "valor padrao atras de `or` resolve",
    )
    mutacao(
        "4. a regua para de atravessar CHAVE DE DICIONARIO",
        lambda i: troca_em(i, REGUA,
                           "        if isinstance(no, ast.Subscript):",
                           "        if False and isinstance(no, ast.Subscript):"),
        "chave de dicionario resolve",
    )
    mutacao(
        "5. pathlib `/` passa a ser lido como producao de nome, e o literal vira construido",
        lambda i: troca_em(i, REGUA,
                           "            if isinstance(no.op, ast.Div):            # pathlib: base / 'x.py'\n"
                           "                return self._uniao(self.resolver(no.left, prof + 1, vistos),\n"
                           "                                   self.resolver(no.right, prof + 1, vistos))",
                           "            if isinstance(no.op, ast.Div):\n"
                           "                return self._rebaixar(\n"
                           "                    self._uniao(self.resolver(no.left, prof + 1, vistos),\n"
                           "                                self.resolver(no.right, prof + 1, vistos)), CONSTRUIDO)"),
        "pathlib com o nome dentro da string e literal",
    )

    # ---- O BURACO DO ITEM 7: quem deixar de ver o nome MONTADO devolve o ponto cego ----
    mutacao(
        "6. concatenacao de constantes passa a ser LITERAL — o ponto cego do item 7 de volta",
        lambda i: troca_em(i, REGUA,
                           "                    return {b: CONSTRUIDO} if b else {}",
                           "                    return {b: LITERAL} if b else {}"),
        "montado por concatenacao e CONSTRUIDO e INVISIVEL",
    )
    mutacao(
        "7. f-string com buraco deixa de rebaixar o que monta",
        lambda i: troca_em(i, REGUA,
                           "                return self._rebaixar(achados, CONSTRUIDO) or {}",
                           "                return achados"),
        "f-string com buraco rebaixa a posicao para construido",
    )
    mutacao(
        "8. `.replace()` passa por composicao de caminho em vez de producao de nome",
        lambda i: troca_em(i, REGUA,
                           "PRODUCAO = ('replace', 'format', 'lower', 'upper', 'strip')",
                           "PRODUCAO = ('format', 'lower', 'upper', 'strip')"),
        "nome passado por .replace() e construido",
    )

    # ---- A VISIBILIDADE: e ela que os tres classificadores perguntam ----
    mutacao(
        "9. tudo passa a ser visivel — a pergunta dos tres classificadores morre calada",
        lambda i: troca_em(i, REGUA,
                           "                saida.append((quem, linha, tipo, alvo, posicao, alvo in a.texto))",
                           "                saida.append((quem, linha, tipo, alvo, posicao, True))"),
        "montado por concatenacao e CONSTRUIDO e INVISIVEL",
    )
    mutacao(
        "10. `invisiveis()` devolve [] por construcao — regua que nunca acha nada",
        lambda i: troca_em(i, REGUA,
                           "    return [r for r in atos(arquivos) if not r[5]]",
                           "    return []"),
        "o ato de nome montado entra em invisiveis()",
    )
    mutacao(
        "11. o ato invisivel passa a ser contado TAMBEM como indireto — as duas contas se somam",
        lambda i: troca_em(i, REGUA,
                           "    return [r for r in atos(arquivos) if r[4] != LITERAL and r[5]]",
                           "    return [r for r in atos(arquivos) if r[4] != LITERAL]"),
        "NAO e contado como indireto",
    )
    mutacao(
        "12. a indirecao passa a ser reportada como literal (a posicao sobe em vez de cair)",
        lambda i: troca_em(i, REGUA,
                           "def _mais_fraca(a, b):\n    return a if _ORDEM[a] <= _ORDEM[b] else b",
                           "def _mais_fraca(a, b):\n    return a if _ORDEM[a] >= _ORDEM[b] else b"),
        "carga por variavel e indireta",
    )

    # ---- A FRONTEIRA DO QUE E ATO SOBRE IRMAO ----
    mutacao(
        "13. ler o PROPRIO arquivo passa a contar como alvo",
        lambda i: troca_em(i, REGUA,
                           "                if alvo not in irmaos or alvo == quem:",
                           "                if alvo not in irmaos:"),
        "ler o proprio arquivo nao conta como alvo",
    )
    mutacao(
        "14. alvo FORA da pasta passa a entrar na conta",
        lambda i: troca_em(i, REGUA,
                           "                if alvo not in irmaos or alvo == quem:",
                           "                if alvo == quem:"),
        "alvo fora da pasta nao entra na conta",
    )
    mutacao(
        "15. JSON passa a ser irmao, e o relatorio de ato enche de dado ate ninguem o ler",
        lambda i: troca_em(i, REGUA,
                           "EXTENSOES = ('.py', '.mjs', '.php')",
                           "EXTENSOES = ('.py', '.mjs', '.php', '.json')"),
        "open() de JSON em dados/ nao e ato sobre irmao",
    )

    # ---- O LIMITE DECLARADO: e ele que separa medicao de cobertura imaginada ----
    mutacao(
        "16. `nao_resolvidos()` devolve [] — a carga irresolvivel some do relatorio",
        lambda i: troca_em(i, REGUA,
                           "            if tipo == 'carrega' or a.aponta_para_a_pasta(no):",
                           "            if False:"),
        "carga com alvo irresolvivel sai em nao_resolvidos()",
    )
    mutacao(
        "17. `nao_resolvidos()` para de filtrar por pasta e vira lista de todo open()",
        lambda i: troca_em(i, REGUA,
                           "            if tipo == 'carrega' or a.aponta_para_a_pasta(no):",
                           "            if True:"),
        "NAO vira ruido no relatorio",
    )
    mutacao(
        "18. arquivo que nao parseia some de `nao_lidos()` e passa por medido",
        lambda i: troca_em(i, REGUA,
                           "            saida.append((nome, 'nao parseia: %s' % e.msg))",
                           "            pass"),
        "sai nomeado em nao_lidos()",
    )
    mutacao(
        "19. o `.mjs` some de `nao_lidos()` — o limite vira cobertura imaginada",
        lambda i: troca_em(i, REGUA,
                           "            saida.append((nome, 'nao e Python'))\n            continue",
                           "            continue"),
        "fora do alcance",
    )

    # ---- MUNDOS QUE TEM DE PASSAR ----
    def conferir_novo(ilha):
        # Um `conferir-` novo e honesto, que carrega uma regua pelo nome. Se o
        # portao cobrasse NUMERO em vez de propriedade, este mundo o derrubaria
        # — e o proximo trabalhador teria de lembrar de alimentar a conta. E o
        # defeito 4(c) de 20/10, que nasceu nesta mesma familia.
        with io.open(os.path.join(ilha, "ferramentas", "conferir-coisa-nova.py"),
                     "w", encoding="utf-8") as f:
            f.write("# BANCADA: sem rede\n"
                    "import importlib.util, os\n"
                    "P = os.path.dirname(os.path.abspath(__file__))\n"
                    "s = importlib.util.spec_from_file_location(\n"
                    "    'r', os.path.join(P, 'regua-robots.py'))\n")  # ENCENACAO
        return True

    mundo_que_passa(
        "A. um `conferir-` novo e honesto entra na pasta e NADA reprova",
        conferir_novo,
    )

    def regua_orfa(ilha):
        # Regua que ninguem carrega: a `regua-classes-da-bancada.py` a denuncia,
        # e ESTA regua nao tem nada a dizer sobre ela. Portao que reprovasse aqui
        # estaria medindo a pergunta da outra.
        #
        # OS DOIS NOMES ABAIXO SE DECLARAM ENCENACAO, E ISSO NAO E ZELO: sem o
        # marcador, a mutacao 18 do `mutacoes-classes-da-bancada.py` SOBREVIVE.
        # Ela cria uma `regua-orfa.py` na sombra e espera ve-la denunciada; este
        # arquivo e PORTAO, entao o nome dela escrito aqui entre aspas a fazia
        # passar por CARREGADA por mim, e a orfa se protegia pelo texto de um
        # terceiro. Medido pela bancada em 20/10/2026, 14h1xZ, no dia em que
        # este arquivo nasceu — e e literalmente o laco que o comentario da
        # mutacao 18 ja descrevia para si mesma.
        with io.open(os.path.join(ilha, "ferramentas", "regua-orfa.py"),  # ENCENACAO
                     "w", encoding="utf-8") as f:
            f.write("# ninguem me carrega\n")
        return True

    mundo_que_passa(
        "B. uma regua que ninguem carrega entra na pasta e ESTE portao nao a cobra",
        regua_orfa,
    )

    def comentario_que_cita(ilha):
        # Citar o nome de um irmao em COMENTARIO nao cria ato nenhum. Se criasse,
        # esta regua seria a varredura por nome que ela existe para medir.
        return troca_em(ilha, REGUA, "import ast\n",
                        "import ast\n# fala do conferir-robots-no-ar.py sem agir nele\n")

    mundo_que_passa(
        "C. comentario que cita um irmao NAO vira ato",
        comentario_que_cita,
    )

    print()
    ruim = len(sobreviventes) + len(inertes) + len(sem_frase)
    if ruim:
        if sobreviventes:
            print("SOBREVIVERAM ou reprovaram mundo bom: %s" % ", ".join(sobreviventes))
        if inertes:
            print("INERTES (alvo sumido, nada foi medido): %s" % ", ".join(inertes))
        if sem_frase:
            print("REPROVARAM PELO MOTIVO ERRADO: %s" % ", ".join(sem_frase))
        print("REPROVADO: %d de %d mutacoes nao fecharam." % (ruim, feitas))
        return 1
    print("APROVADO: %d mutacoes, 0 sobrevivente, 0 inerte, 0 sem a frase." % feitas)
    return 0


if __name__ == "__main__":
    sys.exit(main())
