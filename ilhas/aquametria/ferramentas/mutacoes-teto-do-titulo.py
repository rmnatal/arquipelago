#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AS MUTACOES DO PORTAO DO TETO DO TITULO.

    python3 ferramentas/mutacoes-teto-do-titulo.py

Sem rede. Codigo de saida 0 se NENHUMA mutacao sobreviver, 1 se alguma passar.

O QUE ELAS PROVAM, e por que o `teste-teto-do-titulo.py` nao basta sozinho: um
portao verde prova que o mundo de hoje passa, nunca que o portao MORDE. Cada
mutacao daqui quebra uma afirmacao de proposito, numa ILHA DE SOMBRA (copia de
`ferramentas/` e de `snippets/` num diretorio temporario — o repositorio de
verdade nunca e tocado), e exige TRES coisas:

  1. que o arquivo mude de verdade (mutacao que nao encontra o alvo e INERTE, e
     aparece nomeada em vez de contar como sucesso);
  2. que o teste saia com codigo 1;
  3. que ele reprove PELA FRASE que a mutacao espera ouvir de volta — a licao de
     15/10/2026 desta ilha: reprovar nao e a mesma coisa que reprovar PELO
     MOTIVO CERTO.

A MUTACAO QUE MAIS IMPORTA AQUI E A PRIMEIRA, e ela e o defeito que o conserto
de 19/10 poderia ter introduzido no lugar do que consertou: uma regua que PARECE
perguntar e devolve 65 quando a pergunta falha. Com ela no lugar, as 61 afirmacoes
de teto desta ilha ficariam verdes para sempre, agora com a aparencia de estarem
lendo a fonte — que e pior que o `TETO = 65` honesto que estava la antes.

A SEGUNDA QUE MAIS IMPORTA E A DECIMA TERCEIRA: ela REDIGITA o teto dentro do
`conferir-titulo-no-ar.py`, ou seja desfaz o conserto do jeito mais natural do
mundo, e tem de ser pega pela varredura. Sem ela, o conserto de hoje vale para
hoje e nao para a semana que vem.
"""
import io
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REGUA = os.path.join("ferramentas", "regua-teto-do-titulo.py")
PERGUNTADOR = os.path.join("ferramentas", "listar-teto-do-titulo.php")
PORTAO_DO_AR = os.path.join("ferramentas", "conferir-titulo-no-ar.py")
PORTAO_DA_VOZ = os.path.join("ferramentas", "teste-voz.mjs")
TESTE = os.path.join("ferramentas", "teste-teto-do-titulo.py")

inertes = []
sobreviventes = []
sem_frase = []
feitas = 0


def ilha_de_sombra():
    tmp = tempfile.mkdtemp(prefix="aqm-mut-teto-")
    shutil.copytree(os.path.join(RAIZ, "ferramentas"), os.path.join(tmp, "ferramentas"),
                    ignore=shutil.ignore_patterns("__pycache__"))
    # Os snippets entram porque a metade (C) do portao le a ilha de VERDADE: ela
    # pergunta ao PHP e compara com o texto do `define()`. Sombra sem snippet
    # reprovaria por ausencia de arquivo, e ausencia de arquivo lida como
    # mutacao pega e mutacao que nunca foi medida.
    shutil.copytree(os.path.join(RAIZ, "snippets"), os.path.join(tmp, "snippets"))
    return tmp


def troca_em(ilha, arquivo, velho, novo):
    """Troca exata, e devolve False se o alvo nao estava la — e isso e INERTE.

    `str.replace` cru de alvo sumido NAO falha: ele devolve o mesmo texto e a
    mutacao vira verde sobre nada.
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


def main():
    print("MUTACOES DO PORTAO DO TETO DO TITULO — ilha de sombra, sem rede\n")

    # ---- O DEFEITO QUE O CONSERTO PODERIA TER TRAZIDO: o valor de consolo ----
    mutacao(
        "a regua devolve 65 em vez de levantar quando a resposta vem vazia",
        lambda i: troca_em(i, REGUA,
                           'raise RespostaInvalida("o perguntador nao devolveu nada")',
                           'return {"teto": 65, "separador": " – ", "marca": "Aquametria"}'),
        "resposta vazia e recusada")

    mutacao(
        "a regua aceita teto que nao e inteiro",
        lambda i: troca_em(i, REGUA,
                           'raise RespostaInvalida("teto nao e inteiro: %r" % (teto,))',
                           'teto = 65'),
        "teto em texto e recusado")

    mutacao(
        "a regua perde a banda crivel e obedece a qualquer numero",
        lambda i: troca_em(i, REGUA, "if not TETO_MINIMO_CRIVEL <= teto <= TETO_MAXIMO_CRIVEL:",
                           "if False:"),
        "teto acima da banda e recusado")

    mutacao(
        "a regua nao cobra mais separador nem marca",
        lambda i: troca_em(i, REGUA, 'for c in ("separador", "marca"):',
                           'for c in ():'),
        "separador vazio e recusado")

    mutacao(
        "a cauda volta a ser digitada em vez de derivada",
        lambda i: troca_em(i, REGUA, 'return c["separador"] + c["marca"]',
                           'return " – Aquametria"'),
        "trocar o separador muda a cauda")

    # ---- A PERGUNTA DE VERDADE: se ela nao sai, nada do resto importa ----
    mutacao(
        "perguntar() devolve um dicionario fixo em vez de abrir o php",
        lambda i: troca_em(i, REGUA, "return ler_resposta(saida.stdout)",
                           'return {"teto": 65, "separador": " – ", "marca": "Aquametria"}'),
        "define com 41 devolve 41")

    mutacao(
        "perguntar() ignora o codigo de saida do php",
        lambda i: troca_em(i, REGUA, "if saida.returncode != 0:", "if False:"),
        "ilha sem o perguntador e recusada")

    mutacao(
        "o perguntador php inventa um teto quando a constante falta",
        lambda i: troca_em(i, PERGUNTADOR,
                           "fwrite( STDERR, 'FALHA: constante nao definida apos carregar os snippets: ' "
                           ". implode( ', ', $faltando ) . \"\\n\" );\n\texit( 1 );",
                           "define( 'AQUAMETRIA_TITULO_TETO', 65 );\n\t"
                           "define( 'AQUAMETRIA_TITULO_SEPARADOR', ' – ' );\n\t"
                           "define( 'AQUAMETRIA_TITULO_MARCA', 'Aquametria' );"),
        "perguntador sem o define sai diferente de zero")

    # ---- A VARREDURA, que e o que impede o conserto de ser desfeito ----
    mutacao(
        "a varredura deixa de ver `TETO` atribuido a numero",
        lambda i: troca_em(i, REGUA, 'NOMES_DO_TETO = r"(?:TETO|TITULO_MAXIMO)"',
                           'NOMES_DO_TETO = r"(?:XXNUNCAXX)"'),
        "atribuido a numero e denunciado")

    mutacao(
        "a varredura deixa de ver separador e marca digitados",
        lambda i: troca_em(i, REGUA, 'NOMES_DO_TEXTO = r"(?:SEPARADOR|MARCA|CAUDA)"',
                           'NOMES_DO_TEXTO = r"(?:XXNUNCAXX)"'),
        "em texto e denunciado")

    mutacao(
        "a varredura passa a chamar TUDO de codigo, e a prosa vira denuncia",
        lambda i: troca_em(i, REGUA,
                           '    nua = linha.strip()\n    if nua.startswith(MARCADORES_DE_PROSA):',
                           '    return "codigo"\n    nua = linha.strip()\n'
                           '    if nua.startswith(MARCADORES_DE_PROSA):'),
        "comentario que cita o numero e AVISO"),

    mutacao(
        "a varredura passa a chamar TUDO de prosa, e nada mais reprova",
        lambda i: troca_em(i, REGUA,
                           '    nua = linha.strip()\n    if nua.startswith(MARCADORES_DE_PROSA):',
                           '    return "prosa"\n    nua = linha.strip()\n'
                           '    if nua.startswith(MARCADORES_DE_PROSA):'),
        "atribuido a numero e denunciado")

    mutacao(
        "a varredura denuncia comparacao com QUALQUER numero, nao com o teto",
        lambda i: troca_em(i, REGUA, "if int(m.group(1)) == teto:", "if True:"),
        "comparacao com numero que NAO e o teto nao e denunciada")

    mutacao(
        "a varredura deixa de exigir que a linha fale de titulo",
        lambda i: troca_em(i, REGUA,
                           'RE_FALA_DE_TITULO = re.compile(r"title|titulo|título|\\baba\\b", re.I)',
                           'RE_FALA_DE_TITULO = re.compile(r"", re.I)'),
        "em linha que NAO fala de titulo nao e denunciada")

    # ---- E A MUTACAO QUE DESFAZ O CONSERTO DO JEITO MAIS NATURAL ----
    mutacao(
        "alguem redigita o teto dentro do conferir-titulo-no-ar.py",
        lambda i: troca_em(i, PORTAO_DO_AR,
                           'TETO = carregar("regua-teto-do-titulo.py", "regua_teto_do_titulo").perguntar(RAIZ)["teto"]',
                           "TETO = 65"),
        "nao tem NENHUMA denuncia")

    mutacao(
        "alguem tira a pergunta do teste-voz.mjs",
        lambda i: troca_em(i, PORTAO_DA_VOZ, "/ferramentas/regua-teto-do-titulo.py",
                           "/ferramentas/nao-existe.py"),
        "teste-voz.mjs tem uma string que E o caminho da regua")

    # ---- E OS MUNDOS QUE TEM DE PASSAR ----
    # Bateria que so sabe reprovar nao distingue "o portao morde" de "o portao
    # morde tudo".
    mundo_que_passa("a ilha intacta APROVA", None)
    mundo_que_passa(
        "mexer num comentario da regua nao reprova nada",
        lambda i: troca_em(i, REGUA, "# A BANDA E A REGUA QUE ESTE ARQUIVO ESCREVE PARA SI",
                           "# COMENTARIO MEXIDO DE PROPOSITO PELAS MUTACOES"))
    mundo_que_passa(
        "trocar o teto do snippet por outro numero da banda NAO reprova — ele e lido",
        lambda i: troca_em(i, os.path.join("snippets", "aquametria-seo-tecnico.php"),
                           "define( 'AQUAMETRIA_TITULO_TETO', 65 );",
                           "define( 'AQUAMETRIA_TITULO_TETO', 58 );"))

    print("\n%d mutacao(oes): %d sobrevivente(s), %d inerte(s), %d sem a frase"
          % (feitas, len(sobreviventes), len(inertes), len(sem_frase)))
    for rotulo in sobreviventes:
        print("  SOBREVIVEU  %s" % rotulo)
    for rotulo in inertes:
        print("  INERTE  %s" % rotulo)
    for rotulo in sem_frase:
        print("  SEM A FRASE  %s" % rotulo)
    return 1 if (sobreviventes or inertes or sem_frase) else 0


if __name__ == "__main__":
    sys.exit(main())
