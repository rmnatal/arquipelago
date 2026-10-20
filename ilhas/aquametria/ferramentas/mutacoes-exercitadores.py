#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mutila a `regua-exercitadores.py` numa ilha de SOMBRA e exige que o
`teste-exercitadores.py` reprove — e reprove PELA FRASE certa.

Sem rede. A sombra leva so `ferramentas/`, porque esta regua le a arvore
sintatica dos arquivos dela e nao pergunta nada a snippet nem a banco.

POR QUE CADA MUTACAO EXISTE: a regua conta exercicio por tres formas e atribui
o sitio por duas regras, e cada caminho que morrer em silencio devolve a conta
que o item 4 pediu com cara de medida. As mutacoes de 1 a 7 matam um caminho
cada; as de 8 a 11 atacam a ATRIBUICAO, que e onde a conta mente sem errar
nenhum sitio; a 12 e a 13 atacam `orfas()`, que e a unica lista com dentes; e a
14 e a 15 sao a propriedade das copias do `ler_pasta()`, que foi o achado desta
passada — inclusive a mutacao que DESFAZ o conserto e tem de reprovar.

A mutacao 16 mata um simbolo da regua IRMA, para provar que a importacao esta
viva e nao e uma copia disfarcada. E a familia do defeito que o fecho de 20/10
pagou: a `regua-alvos-em-php.py` nasceu com uma COPIA do `_base()` da irma, e a
copia nasceu com o defeito da irma no mesmo dia.
"""

import io
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGUA = os.path.join("ferramentas", "regua-exercitadores.py")
IRMA = os.path.join("ferramentas", "regua-alvos-de-portao.py")
TESTE = os.path.join("ferramentas", "teste-exercitadores.py")
TETO = os.path.join("ferramentas", "regua-teto-do-titulo.py")

inertes = []
sobreviventes = []
sem_frase = []
feitas = 0


def ilha_de_sombra():
    tmp = tempfile.mkdtemp(prefix="aqm-mut-exerc-")
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
    print("MUTACOES DO PORTAO DOS EXERCITADORES — ilha de sombra, sem rede\n")

    # ---- AS TRES FORMAS: uma mutacao por forma ----
    mutacao(
        "1. a regua deixa de ver a REFERENCIA (nome como valor)",
        lambda i: troca_em(i, REGUA,
                           "                forma = CHAMADA if id(no) in funcs_de_chamada else REFERENCIA\n"
                           "                saida.append((no.lineno, no.id, forma))",
                           "                if id(no) in funcs_de_chamada:\n"
                           "                    saida.append((no.lineno, no.id, CHAMADA))"),
        "nome posto numa tupla de casos e REFERENCIA",
    )
    mutacao(
        "2. a regua deixa de ver o nome POR_NOME (string igual ao nome)",
        lambda i: troca_em(i, REGUA,
                           "            if no.value in nomes:\n"
                           "                saida.append((no.lineno, no.value, POR_NOME))",
                           "            if False:\n"
                           "                saida.append((no.lineno, no.value, POR_NOME))"),
        "string igual ao nome e POR_NOME",
    )
    mutacao(
        "3. a regua passa a contar string que CONTEM o nome (prova fraca viraria sitio)",
        lambda i: troca_em(i, REGUA,
                           "            if no.value in nomes:\n"
                           "                saida.append((no.lineno, no.value, POR_NOME))",
                           "            for _n in nomes:\n"
                           "                if _n in no.value:\n"
                           "                    saida.append((no.lineno, _n, POR_NOME))"),
        "string que CONTEM o nome nao e sitio",
    )
    mutacao(
        "4. a regua deixa de ver chamada por ATRIBUTO do modulo (R.alvo())",
        lambda i: troca_em(i, REGUA,
                           "        elif isinstance(no, ast.Attribute) and isinstance(no.ctx, ast.Load):",
                           "        elif False and isinstance(no, ast.Attribute):"),
        "chamada por atributo do modulo e CHAMADA",
    )
    mutacao(
        "5. o cabecalho da propria definicao passa a se exercitar",
        lambda i: troca_em(i, REGUA,
                           "            # seguem contando.\n"
                           "            continue",
                           "            # seguem contando.\n"
                           "            if no.name in nomes:\n"
                           "                saida.append((no.lineno, no.name, REFERENCIA))\n"
                           "            continue"),
        "o cabecalho da propria definicao nao e exercicio",
    )
    mutacao(
        "6. metodo de classe e funcao de dentro passam a contar como definicao",
        lambda i: troca_em(i, REGUA,
                           "        for no in arv.body:\n"
                           "            if isinstance(no, (ast.FunctionDef, ast.AsyncFunctionDef)):",
                           "        for no in ast.walk(arv):\n"
                           "            if isinstance(no, (ast.FunctionDef, ast.AsyncFunctionDef)):"),
        "so funcao de TOPO entra",
    )
    mutacao(
        "7. a conta passa a ser por SITIO em vez de por ARQUIVO",
        lambda i: troca_em(i, REGUA,
                           "    return {k: len(v) for k, v in exercitadores(arquivos).items()}",
                           "    conta = {}\n"
                           "    for quem, _l, nome, _f in exercicios(arquivos):\n"
                           "        for (a, n) in exercitadores(arquivos):\n"
                           "            if n == nome:\n"
                           "                conta[(a, n)] = conta.get((a, n), 0) + 1\n"
                           "    for k in exercitadores(arquivos):\n"
                           "        conta.setdefault(k, 0)\n"
                           "    return conta"),
        "tres sitios no mesmo arquivo sao UM exercitador",
    )

    # ---- A ATRIBUICAO: a conta mente sem errar um sitio ----
    mutacao(
        "8. o homonimo passa a ser atribuido a TODAS as definicoes do nome",
        lambda i: troca_em(i, REGUA,
                           "        elif len(donos) == 1:\n"
                           "            saida[(next(iter(donos)), nome)].add(quem)",
                           "        else:\n"
                           "            for d in donos:\n"
                           "                saida[(d, nome)].add(quem)"),
        "e nenhuma das homonimas recebe o sitio ambiguo",
    )
    mutacao(
        "9. a regua para de respeitar o grafo de CARGA da irma",
        lambda i: troca_em(i, REGUA,
                           "        carregados = donos & cargas.get(quem, set())",
                           "        carregados = set()"),
        "o homonimo vai para a regua que o sitio CARREGA, e so para ela",
    )
    mutacao(
        "10. o sitio ambiguo deixa de ser declarado em ambiguos()",
        lambda i: troca_em(i, REGUA,
                           "        saida.append((quem, linha, nome, sorted(donos)))",
                           "        continue"),
        "homonimo sem carga declarada nao e atribuido a ninguem",
    )
    mutacao(
        "11. COMPARTILHADA passa a ser toda funcao da pasta",
        lambda i: troca_em(i, REGUA,
                           "            if arq in carregados]",
                           "            if True]"),
        "so funcao de arquivo carregado por irmao e compartilhada",
    )

    # ---- orfas(): a unica lista com dentes ----
    mutacao(
        "12. orfas() devolve [] por construcao — regua verde para sempre",
        lambda i: troca_em(i, REGUA,
                           "    tocados = {nome for _quem, _linha, nome, _forma in exercicios(arquivos)}",
                           "    tocados = {nome for _a, nome, _l in definicoes(arquivos)}"),
        "funcao sem UM sitio nas tres formas e orfa",
    )
    mutacao(
        "13. orfas() passa a acusar quem tem sitio AMBIGUO de codigo morto",
        lambda i: troca_em(i, REGUA,
                           "    tocados = {nome for _quem, _linha, nome, _forma in exercicios(arquivos)}",
                           "    tocados = set()\n"
                           "    for (a, n), q in exercitadores(arquivos).items():\n"
                           "        if q:\n"
                           "            tocados.add(n)"),
        "funcao com sitio ambiguo NAO e chamada de morta",
    )

    # ---- A PROPRIEDADE DAS COPIAS, que e o achado desta passada ----
    def desfazer_o_conserto(ilha):
        """Devolve o `regua-teto-do-titulo.py` ao estado de antes de hoje.

        E a mutacao mais importante deste arquivo: se ela SOBREVIVER, o portao
        nao esta cobrando o conserto e a sexta copia nascera com o mesmo
        buraco."""
        return troca_em(ilha, TETO,
                        'with open(os.path.join(pasta, nome), encoding="utf-8", errors="replace") as f:',
                        'with open(os.path.join(pasta, nome), encoding="utf-8") as f:')

    mutacao(
        "14. o conserto de hoje e DESFEITO numa das cinco copias do ler_pasta()",
        desfazer_o_conserto,
        "morreu de UnicodeDecodeError num byte que nao e UTF-8",
    )

    def copia_nova_com_o_buraco(ilha):
        """Uma SEXTA copia entra na pasta com o buraco de ontem.

        Prova que a metade 3 DESCOBRE as copias em vez de as listar: nenhuma
        linha deste portao nomeia o arquivo abaixo."""
        caminho = os.path.join(ilha, "ferramentas", "regua-copia-nova.py")  # ENCENACAO
        with io.open(caminho, "w", encoding="utf-8") as f:
            f.write("import os\n\n\n"
                    "def ler_pasta(pasta=None):\n"
                    "    pasta = pasta or '.'\n"
                    "    saida = {}\n"
                    "    for nome in sorted(os.listdir(pasta)):\n"
                    "        if not nome.endswith('.py'):\n"
                    "            continue\n"
                    "        try:\n"
                    "            with open(os.path.join(pasta, nome), encoding='utf-8') as f:\n"
                    "                saida[nome] = f.read()\n"
                    "        except OSError:\n"
                    "            continue\n"
                    "    return saida\n\n\n"
                    "def main():\n"
                    "    return len(ler_pasta())\n")
        return True

    mutacao(
        "15. uma SEXTA copia do ler_pasta() nasce com o buraco e ninguem a listou",
        copia_nova_com_o_buraco,
        "morreu de UnicodeDecodeError num byte que nao e UTF-8",
    )

    # ---- O LIMITE DE ESCOPO, que e numero e nao prosa ----
    mutacao(
        "18. nomes_sombreados() devolve vazio — o furo de escopo viraria prosa",
        lambda i: troca_em(i, REGUA,
                           "        for n in locais & nomes:\n"
                           "            saida[n] = saida.get(n, 0) + 1",
                           "        for n in []:\n"
                           "            saida[n] = saida.get(n, 0) + 1"),
        "nome que tambem e variavel local aparece em nomes_sombreados",
    )
    mutacao(
        "19. nomes_sombreados() passa a contar TODO nome de funcao como sombreado",
        lambda i: troca_em(i, REGUA,
                           "        for n in locais & nomes:",
                           "        for n in nomes:"),
        "nome que nao e variavel em lugar nenhum nao e sombreado",
    )

    # ---- A IMPORTACAO DA IRMA ESTA VIVA? ----
    mutacao(
        "16. o EXTENSOES da regua IRMA e morto — a importacao nao e copia",
        lambda i: troca_em(i, IRMA,
                           "EXTENSOES = ('.py', '.mjs', '.php')",
                           "EXTENSOES = ()"),
        "os dois idiomas de fora aparecem NOMEADOS no limite",
    )
    mutacao(
        "17. o grafo de carga da irma devolve vazio",
        lambda i: troca_em(i, IRMA,
                           "            if ultimo == CARGA and len(no.args) >= 2:",
                           "            if False and ultimo == CARGA:"),
        "o homonimo vai para a regua que o sitio CARREGA, e so para ela",
    )

    # ---- MUNDOS QUE TEM DE PASSAR ----
    def regua_orfa(ilha):
        # Um arquivo que ninguem carrega entra na pasta. Ele NAO e assunto deste
        # portao — quem denuncia regua orfa e o `regua-classes-da-bancada.py`.
        # E as funcoes dele tem de se exercitar entre si, senao viram orfas de
        # verdade e o portao reprova com razao.
        caminho = os.path.join(ilha, "ferramentas", "regua-ninguem-carrega.py")  # ENCENACAO
        with io.open(caminho, "w", encoding="utf-8") as f:
            f.write("def ajudante():\n    return 1\n\n\n"
                    "def main():\n    return ajudante()\n")
        return True

    mundo_que_passa(
        "A. arquivo que ninguem carrega entra na pasta e ESTE portao nao o cobra",
        regua_orfa,
    )

    def arquivo_que_nao_parseia(ilha):
        # Arquivo torto nao derruba a regua: ele e LIMITE declarado. A pasta real
        # nao tem nenhum, entao a prova precisa de um encenado.
        caminho = os.path.join(ilha, "ferramentas", "regua-torta-de-verdade.py")  # ENCENACAO
        with io.open(caminho, "w", encoding="utf-8") as f:
            f.write("def (\n")
        return True

    mundo_que_passa(
        "B. um .py que nao parseia entra na pasta e a regua o declara em vez de morrer",
        arquivo_que_nao_parseia,
    )

    def byte_torto_na_pasta_real(ilha):
        # E o mundo que o conserto de hoje torna possivel: um arquivo com byte
        # latin-1 DENTRO da pasta, que antes derrubava duas das cinco copias.
        caminho = os.path.join(ilha, "ferramentas", "regua-com-acento-torto.py")  # ENCENACAO
        with io.open(caminho, "wb") as f:
            f.write(b"# acento torto: \xe9\n\n\ndef ajudante():\n    return 1\n\n\n"
                    b"def main():\n    return ajudante()\n")
        return True

    mundo_que_passa(
        "C. byte latin-1 na pasta REAL e as cinco copias continuam de pe",
        byte_torto_na_pasta_real,
    )

    def comentario_que_cita(ilha):
        # Citar o nome de uma funcao em COMENTARIO nao a exercita. Se citasse,
        # esta regua seria a varredura por nome que ela existe para corrigir.
        return troca_em(ilha, REGUA, "import ast\n",
                        "import ast\n# fala da orfas() sem a exercitar\n")

    mundo_que_passa(
        "D. comentario que cita o nome de uma funcao NAO a exercita",
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
