#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AS MUTACOES DO PORTAO DAS CLASSES DA BANCADA. BANCADA: sem rede.

    python3 ferramentas/mutacoes-classes-da-bancada.py

Codigo de saida 0 se NENHUMA mutacao sobreviver, 1 se alguma passar.

Copia o desenho do `mutacoes-constantes-de-snippet.py`: cada mutacao quebra UMA
afirmacao de proposito, numa ILHA DE SOMBRA (o repositorio de verdade nunca e
tocado), e exige tres coisas — que o arquivo mude (alvo sumido e INERTE e
aparece nomeado), que o portao saia 1, e que ele reprove PELA FRASE esperada,
porque reprovar nao e a mesma coisa que reprovar pelo motivo certo.

AS DUAS MUTACOES QUE MAIS IMPORTAM, e as duas sao direcoes opostas do mesmo
conserto de 20/10/2026:

  * **Voltar a leitura cega** (mutacao 1): trocar `e_ato_de_codigo` por uma
    busca crua no texto. E o defeito do item 6(c) reposto. Sem esta mutacao o
    conserto vale para hoje e nao para a semana que vem.
  * **Afrouxar para `codigo` so** (mutacoes 2 e 3): ler "a linha MEDE alguma
    coisa ali?" como "so `codigo` vale". E o CONSERTO LITERAL, o que poria 18
    arquivos na classe errada, e ele tem de reprovar tambem — senao a contagem
    que decidiu o desenho nao esta guardada em portao nenhum e vira prosa.

E uma terceira, que guarda a exencao: o `ENCENACAO` e a unica porta pela qual
uma marca passa de proposito, e porta que nao se testa e porta escancarada. Se
ele parar de valer por LINHA e passar a valer por ARQUIVO (mutacao 9), uma
declaracao honesta no topo de um portao calaria toda invocacao dele para sempre.
"""
import io
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REGUA = os.path.join("ferramentas", "regua-classes-da-bancada.py")
REGUA_DO_TETO = os.path.join("ferramentas", "regua-teto-do-titulo.py")
TESTE = os.path.join("ferramentas", "teste-classes-da-bancada.py")

inertes = []
sobreviventes = []
sem_frase = []
feitas = 0


def ilha_de_sombra():
    tmp = tempfile.mkdtemp(prefix="aqm-mut-classes-")
    # So a `ferramentas/` entra: esta regua classifica pelo TEXTO dos arquivos
    # dela e nao pergunta nada a snippet nem a banco. Sombra com o que a regua
    # nao le seria copia sem motivo.
    shutil.copytree(os.path.join(RAIZ, "ferramentas"), os.path.join(tmp, "ferramentas"),
                    ignore=shutil.ignore_patterns("__pycache__"))
    return tmp


def troca_em(ilha, arquivo, velho, novo):
    """Troca exata, e devolve False se o alvo nao estava la — e isso e INERTE."""
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
    print("MUTACOES DO PORTAO DAS CLASSES DA BANCADA — ilha de sombra, sem rede\n")

    # ---- 1: O DEFEITO DE 19/10 REPOSTO, que e a razao desta regua existir ----
    mutacao(
        "1. a regua volta a ler a marca no TEXTO, prosa incluida (o item 6(c) reposto)",
        lambda i: troca_em(i, REGUA,
                           "    return bool(posicoes(texto, alvo, regex=regex) - NAO_SAO_ATO)",
                           "    import re as _re\n"
                           "    return bool(alvo.search(texto) if regex else (alvo in texto))"),
        "marca do navegador citada SO em comentario",
    )

    # ---- 2 e 3: O CONSERTO LITERAL, que poria 18 na classe errada ----
    mutacao(
        "2. 'so `codigo` mede' — quebra a INVOCACAO, que mora entre aspas (2 portoes reais)",
        lambda i: troca_em(i, REGUA,
                           "    return bool(posicoes(texto, alvo, regex=regex) - NAO_SAO_ATO)",
                           "    return 'codigo' in posicoes(texto, alvo, regex=regex)"),
        "invocacao do .mjs entre aspas",
    )
    mutacao(
        "3. 'so `codigo` declara' — quebra a DECLARACAO, que mora em prosa (6 conferir- reais)",
        lambda i: troca_em(i, REGUA,
                           "    return 'prosa' in posicoes((texto or '')[:CABECALHO], alvo)",
                           "    return 'codigo' in posicoes((texto or '')[:CABECALHO], alvo)"),
        "declaracao em prosa no cabecalho tira o conferir- da classe de rede",
    )

    # ---- 4: O BURACO PERIGOSO, o unico dos tres que faz rodar as cegas ----
    mutacao(
        "4. o marcador como DADO volta a declarar: o conferir- encenado roda as cegas",
        lambda i: troca_em(i, REGUA,
                           "    return 'prosa' in posicoes((texto or '')[:CABECALHO], alvo)",
                           "    return bool(posicoes((texto or '')[:CABECALHO], alvo))"),
        "marcador carregado como DADO nao declara nada",
    )

    # ---- 5: A DECLARACAO ENTERRADA ----
    mutacao(
        "5. a declaracao passa a valer em qualquer linha, nao so no cabecalho",
        lambda i: troca_em(i, REGUA, "CABECALHO = 4000", "CABECALHO = 10 ** 9"),
        "declaracao fora do cabecalho nao declara",
    )

    # ---- 6 e 7: A REGUA ORFA, que e a doenca que a bancada inteira cura ----
    mutacao(
        "6. citacao em prosa volta a contar como carga: regua orfa escapa da denuncia",
        lambda i: troca_em(i, REGUA,
                           "        if e_ato_de_codigo(arquivos[outro], nome):",
                           "        if nome in arquivos[outro]:"),
        "regua citada so em comentario fica DENUNCIADA",
    )
    mutacao(
        "7. PRODUCAO volta a proteger regua (a regra de 19/10 afrouxada)",
        lambda i: troca_em(i, REGUA,
                           "        if not E_PORTAO.match(outro):\n            continue",
                           "        if False:\n            continue"),
        "regua carregada so por PRODUCAO continua denunciada",
    )

    # ---- 8: O CONTADOR ----
    mutacao(
        "8. `contar-` passa a escapar sem ninguem carregar nada",
        lambda i: troca_em(i, REGUA,
                           "        return (None, 'producao') if exercitado else (None, 'sem_convencao')\n"
                           "    if nome.startswith('teste-navegador-')",  # ENCENACAO
                           "        return (None, 'producao')\n"
                           "    if nome.startswith('teste-navegador-')"),  # ENCENACAO
        "contar- citado so em prosa",
    )

    # ---- 9: A EXENCAO, que e a unica porta aberta de proposito ----
    mutacao(
        "9. o `ENCENACAO` passa a valer por ARQUIVO e nao por LINHA",
        lambda i: troca_em(i, REGUA,
                           "        encenada = MARCADOR_DE_ENCENACAO in linha",
                           "        encenada = MARCADOR_DE_ENCENACAO in texto"),
        "declarar encenacao numa linha nao cega a regua para a invocacao de verdade noutra",
    )
    mutacao(
        "10. o `ENCENACAO` deixa de existir: o portao desta regua volta ao Chromium",
        lambda i: troca_em(i, REGUA,
                           "        encenada = MARCADOR_DE_ENCENACAO in linha",
                           "        encenada = False"),
        "com as declaracoes, este portao roda na passada padrao",
    )
    mutacao(
        "11. o `ENCENACAO` passa a valer SEMPRE: o marcador deixa de carregar peso",
        lambda i: troca_em(i, REGUA,
                           "        encenada = MARCADOR_DE_ENCENACAO in linha",
                           "        encenada = True"),
        "invocacao do .mjs entre aspas",
    )

    # ---- 12 e 13: A `onde()` IMPORTADA, e o conserto de 19/10 que ela guarda ----
    mutacao(
        "12. a regua passa a definir uma `onde()` propria (a segunda copia que erra junto)",
        lambda i: troca_em(i, REGUA,
                           "onde = _teto.onde",
                           "def onde(linha, trecho):\n"
                           "    return 'codigo'\n"),
        "a regua das classes NAO define uma `onde()` propria",
    )
    mutacao(
        "13. a aspa ESCAPADA volta a abrir string (o item 6(a) de 19/10 desfeito)",
        lambda i: troca_em(i, REGUA_DO_TETO,
                           '    limpa = RE_ESCAPADO.sub("\\x00\\x00", nua)',
                           "    limpa = nua"),
        "aspa escapada nao abre string",
    )

    # ---- 14 a 16: AS CONVENCOES QUE NAO MUDARAM ----
    mutacao(
        "14. `conferir-` em .py passa a receber o argumento `.`",
        lambda i: troca_em(i, REGUA,
                           "               else ['python3', os.path.join('ferramentas', nome)])",
                           "               else ['python3', os.path.join('ferramentas', nome), '.'])"),
        "conferir- em .py roda sem o argumento",
    )
    mutacao(
        "15. a lista de producao perde o prefixo `gerar`",
        lambda i: troca_em(i, REGUA, r"r'^(gerar|coletar", r"r'^(coletar"),
        "gerar- e producao",
    )
    mutacao(
        "16. `teste-navegador-*.mjs` deixa de ser classe de navegador",
        lambda i: troca_em(i, REGUA,
                           "    if nome.startswith('teste-navegador-') and nome.endswith('.mjs'):\n"  # ENCENACAO
                           "        return ['node', os.path.join('ferramentas', nome), '.'], 'navegador'",
                           "    if nome.startswith('teste-navegador-') and nome.endswith('.mjs'):\n"  # ENCENACAO
                           "        return ['node', os.path.join('ferramentas', nome), '.'], 'sem_rede'"),
        "teste-navegador-*.mjs e navegador",  # ENCENACAO
    )

    # ---- 17: A REGUA CEGA, QUE E O QUE SE MEDE CONTRA ----
    # Se a cega virar copia da boa, o portao passa a encenar mundo em que as duas
    # concordam: ele provaria que a regua funciona e nao que o conserto mudou
    # alguma coisa. E a mutacao que guarda a propria regua de comparacao.
    mutacao(
        "17. a regua CEGA passa a ser copia da boa: a comparacao deixa de comparar",
        lambda i: troca_em(i, REGUA,
                           "def classificar_cega(nome, arquivos):\n"
                           "    texto = arquivos.get(nome, '')",
                           "def classificar_cega(nome, arquivos):\n"
                           "    return classificar(nome, arquivos)\n"
                           "    texto = arquivos.get(nome, '')"),
        "a leitura cega manda esse mesmo portao para o Chromium",
    )

    # ---- 18: A CONTA DA PASTA REAL, E ELA PRECISA PRODUZIR O MUNDO ----
    # A primeira versao desta mutacao apenas DESLIGAVA a afirmacao da lista de
    # denunciados, e SOBREVIVEU — porque hoje a lista esta vazia e desligar a
    # cobranca de um fato verdadeiro nao muda nada. E a licao do item 6(b) de
    # 19/10, outra vez: mutacao que nao PRODUZ o mundo nao mede a afirmacao.
    # Esta produz: uma regua orfa, que nenhum portao carrega.
    mutacao(
        "18. uma regua ORFA aparece na pasta e o portao tem de denuncia-la",
        # O NOME DA ORFA SE DECLARA ENCENACAO, e isto e a regua acertando contra
        # este arquivo: `mutacoes-*` E PORTAO, e portao que cita um nome entre
        # aspas esta CARREGANDO pelo idioma desta pasta. Sem a declaracao, a
        # orfa criada aqui passava por exercitada POR ESTE ARQUIVO e a mutacao
        # sobrevivia — o alvo se protegia pelo proprio texto de quem o ataca.
        lambda i: bool(io.open(os.path.join(i, "ferramentas", "regua-orfa.py"),  # ENCENACAO
                               "w", encoding="utf-8").write(
            "# regua que nenhum portao desta pasta carrega\n"
            "def medir():\n    return 1\n")),
        "a lista de SEM CONVENCAO esta vazia",
    )

    # ---- 19 a 21: A REGUA UNICA, COBRADA PELA SECAO 8 DO CONTRATO ----
    # As duas leituras dao a MESMA resposta nos 94 arquivos que ja existiam
    # nesta pasta, entao nenhuma afirmacao sobre COMPORTAMENTO separa a copia do
    # original. Quem separa e a afirmacao que LE OS ARQUIVOS, e estas tres
    # mutacoes sao o que prova que ela morde.
    BANCADA = os.path.join("ferramentas", "bancada.py")
    mutacao(
        "19. a `bancada.py` volta a ter a propria `dirige_navegador()`",
        lambda i: troca_em(i, BANCADA,
                           "def classificar(nome, arquivos):",
                           "def dirige_navegador(nome):\n"
                           "    return False\n\n\n"
                           "def classificar(nome, arquivos):"),
        "bancada.py NAO redefine dirige_navegador()",
    )
    mutacao(
        "20. a copia volta ANINHADA, dentro da propria classificar() (copia aninhada e copia)",
        lambda i: troca_em(i, BANCADA,
                           "    return CLASSES.classificar(nome, arquivos)",
                           "    def declara_sem_rede(n):\n"
                           "        return False\n"
                           "    return CLASSES.classificar(nome, arquivos)"),
        "bancada.py NAO redefine declara_sem_rede(), em nenhuma indentacao",
    )
    mutacao(
        "21. a `classificar()` da bancada para de delegar e decide por conta propria",
        lambda i: troca_em(i, BANCADA,
                           "    return CLASSES.classificar(nome, arquivos)",
                           "    return (None, 'producao')"),
        "delega para a regua, e nao decide nada",
    )

    # ---- OS MUNDOS QUE TEM DE PASSAR ----
    print()
    mundo_que_passa("A. a pasta de verdade, sem mutacao nenhuma", None)
    mundo_que_passa(
        "B. um `conferir-` novo que se DECLARA sem rede entra na passada padrao sem reprovar nada",
        lambda i: bool(io.open(os.path.join(i, "ferramentas", "conferir-coisa-nova.py"),
                               "w", encoding="utf-8").write(
            '"""BANCADA: sem rede — confere o repositorio."""\n'
            'print("APROVADO: 1 afirmacao, 0 falha.")\n')),
    )
    # E O MUNDO QUE FECHA O ACHADO: um portao sem rede ganha um COMENTARIO que
    # cita a marca do navegador, e ele continua na passada padrao. E o caso de
    # 19/10 exatamente — o comentario que explicava a marca — e aqui ele passa.
    #
    # Ele PRODUZ o mundo em vez de reescrever um comentario que existia: a
    # primeira versao mutava uma linha da `bancada.py` que esta propria passada
    # tinha removido, e ficou INERTE — a trava de alvo exato acusando, que e o
    # corolario de higiene da secao 8 do contrato funcionando na primeira vez em
    # que teve chance.
    def comentar_portao(i):
        caminho = os.path.join(i, "ferramentas", "teste-robots.py")
        texto = io.open(caminho, encoding="utf-8").read()
        with io.open(caminho, "w", encoding="utf-8") as f:
            f.write(texto + "\n# quem dirige navegador aqui e o "
                            "teste-navegador-casca.mjs, citado so para explicar\n")  # ENCENACAO
        return True

    mundo_que_passa(
        "C. um portao sem rede ganha comentario citando a marca e NAO muda de classe",
        comentar_portao,
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
