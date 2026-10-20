#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mutila a `regua-alvos-em-php.py` E o `listar-atos-php.php` numa ilha de
SOMBRA, e exige que o `teste-alvos-em-php.py` reprove — e reprove PELA FRASE
certa.

Sem rede. A sombra leva so `ferramentas/`, porque esta regua le os arquivos
dela pelo tokenizador do PHP e nao pergunta nada a snippet nem a banco.

POR QUE CADA MUTACAO EXISTE: a medicao desta metade tem DUAS metades proprias —
o LEITOR em PHP, que diz o que o tokenizador viu, e a REGUA em Python, que
decide a posicao. Defeito de qualquer uma devolve a esta pasta o ponto cego que
o item 7 nomeou, e as duas tem de ser mutiladas. As mutacoes do leitor sao as
que ninguem escreveria lendo so o Python.

E UMA DELAS ATACA A REGUA IRMA DE PROPOSITO: a mutacao do `PADRAO` mexe no
`regua-alvos-de-portao.py`, porque o vocabulario desta regua e IMPORTADO de la
em vez de copiado. Se ela sobreviver, a importacao virou decoracao e a copia
voltou por outro caminho.
"""

import io
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGUA = os.path.join("ferramentas", "regua-alvos-em-php.py")
LEITOR = os.path.join("ferramentas", "listar-atos-php.php")
IRMA = os.path.join("ferramentas", "regua-alvos-de-portao.py")
TESTE = os.path.join("ferramentas", "teste-alvos-em-php.py")

inertes = []
sobreviventes = []
sem_frase = []
feitas = 0


def ilha_de_sombra():
    tmp = tempfile.mkdtemp(prefix="aqm-mut-alvos-php-")
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


def morte(rotulo, aplicar):
    """Mutacao que tem de MATAR o portao, nunca virar numero errado.

    Chave que some do leitor nao pode degradar para "zero ato": ou o portao
    reprova, ou a bateria o diz. Diferente das outras, aqui traceback TAMBEM
    conta como fechada — o que nao conta e passar."""
    global feitas
    feitas += 1
    ilha = ilha_de_sombra()
    try:
        if not aplicar(ilha):
            print("  INERTE  %s — o alvo nao estava no arquivo" % rotulo)
            inertes.append(rotulo)
            return
        codigo, _ = rodar_teste(ilha)
        if codigo == 0:
            print("  SOBREVIVEU  %s" % rotulo)
            sobreviventes.append(rotulo)
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
    print("MUTACOES DO PORTAO DOS ALVOS EM PHP — ilha de sombra, sem rede\n")

    # ---------------------------------------------------------------
    # O LEITOR EM PHP — as mutacoes que ninguem escreveria lendo o Python
    # ---------------------------------------------------------------
    print(" O LEITOR EM PHP")
    mutacao(
        "1. o leitor deixa de marcar o span do `eval` como ja contado",
        lambda i: troca_em(i, LEITOR,
                           "\t\t\t$consumido[] = $j;",
                           "\t\t\t$nada = $j;"),
        "eval(file_get_contents(X)) conta UMA vez",
    )
    mutacao(
        "2. o leitor para de reconhecer `__FILE__`, e ato sobre si vira ato sobre irmao",
        lambda i: troca_em(i, LEITOR,
                           "\t\t\tcase T_FILE:\n\t\t\t\t$fora[] = array( 'k' => 'file' );",
                           "\t\t\tcase T_FILE:\n\t\t\t\t$nada = array( 'k' => 'file' );"),
        "re-invocacao de SI MESMO pela pasta nao e limite nenhum",
    )
    mutacao(
        "3. variavel DENTRO de string dupla deixa de ser buraco e vira variavel comum",
        lambda i: troca_em(i, LEITOR,
                           "'k' => $em_string ? 'buraco' : 'var'",
                           "'k' => 'var'"),
        "variavel INTERPOLADA em string nao resolve alvo",
    )
    mutacao(
        "4. metodo homonimo passa a contar como funcao do PHP",
        lambda i: troca_em(i, LEITOR,
                           "array( T_OBJECT_OPERATOR, T_DOUBLE_COLON, T_FUNCTION )",
                           "array( T_FUNCTION )"),
        "metodo com nome de funcao do PHP nao e ato",
    )
    morte(
        "5. o span da chamada encolhe para um token e nenhum operando e visto",
        lambda i: troca_em(i, LEITOR,
                           "function aqm_fim_parenteses( $tokens, $i ) {\n\t$n     = count( $tokens );",
                           "function aqm_fim_parenteses( $tokens, $i ) {\n\treturn $i;\n\t$n     = count( $tokens );"),
    )

    # ---------------------------------------------------------------
    # A REGUA EM PYTHON — um caminho de resolucao por mutacao
    # ---------------------------------------------------------------
    print("\n A REGUA EM PYTHON")
    mutacao(
        "6. a regua para de seguir VARIAVEL no sitio do ato",
        lambda i: troca_em(i, REGUA, "        elif k == 'var':", "        elif k == 'nunca':"),
        "variavel -> indireto",
    )
    mutacao(
        "7. a regua para de COLAR operandos adjacentes, e o nome invisivel desaparece",
        lambda i: troca_em(i, REGUA,
                           "            corrida.append(op.get('v') or '')",
                           "            corrida.append('')"),
        "construido e INVISIVEL",
    )
    mutacao(
        "8. nome alcancado por variavel deixa de ser rebaixado e passa por LITERAL",
        lambda i: troca_em(i, REGUA,
                           "    return {v: _rebaixar(a, INDIRETO) for v, a in tabela.items()}",
                           "    return tabela"),
        "variavel -> indireto",
    )
    mutacao(
        "9. ato sobre SI MESMO volta a contar como ato sobre irmao",
        lambda i: troca_em(i, REGUA,
                           "    return any(op.get('k') == 'file' for op in operandos or [])",
                           "    return False"),
        "re-invocacao de SI MESMO pela pasta nao e limite nenhum",
    )
    mutacao(
        "10. `_fala_da_pasta` para de seguir variavel, e a carga por varredura se disfarca",
        lambda i: troca_em(i, REGUA,
                           "        if k == 'var' and op.get('v') not in vistos:",
                           "        if False and op.get('v') not in vistos:"),
        "reconhecida como carga que FALA desta pasta",
    )
    mutacao(
        "11. a regua para de descartar o PROPRIO arquivo como alvo",
        lambda i: troca_em(i, REGUA,
                           "                if alvo not in irmaos or alvo == quem:",
                           "                if alvo not in irmaos:"),
        "carga do PROPRIO arquivo nao e ato sobre irmao",
    )
    mutacao(
        "12. a regua para de exigir que o alvo exista na pasta",
        lambda i: troca_em(i, REGUA,
                           "                if alvo not in irmaos or alvo == quem:",
                           "                if alvo == quem:"),
        "sem o irmao na pasta nao ha ato sobre irmao",
    )
    mutacao(
        "13. `nao_lidos` para de nomear o que nenhuma das duas reguas le "
        "(e a regua irma NAO cobre o buraco: ela so nomeia .py, .mjs e .php)",
        lambda i: troca_em(i, REGUA,
                           "        saida.append((nome, 'nao e PHP: %s' % ext))",
                           "        ext = ext"),
        "os .mjs aparecem nomeados no limite desta regua",
    )
    mutacao(
        "14. `ler` engole a falta do leitor e devolve pasta sem defeito nenhum",
        lambda i: troca_em(i, REGUA,
                           "        return {}, [(n, 'leitor ausente: ferramentas/listar-atos-php.php')\n"
                           "                    for n in sorted(arquivos) if n.endswith('.php')]",
                           "        return {}, []"),
        "TODO .php sai nomeado em falhos",
    )

    # ---------------------------------------------------------------
    # A REGUA IRMA — a importacao do vocabulario tem de estar viva
    # ---------------------------------------------------------------
    print("\n A REGUA IRMA, de onde o vocabulario e IMPORTADO")
    mutacao(
        "15. a barreira de PADRAO cai na regua irma, e `*.php` volta a passar por nome",
        lambda i: troca_em(i, IRMA, "PADRAO = ('*', '?', '[')", "PADRAO = ()"),
        "o idioma de quem varre a pasta inteira fica por resolver",
    )

    # ---------------------------------------------------------------
    # OS MUNDOS QUE TEM DE PASSAR
    # ---------------------------------------------------------------
    print("\n OS MUNDOS QUE TEM DE PASSAR")

    def php_novo_e_honesto(ilha):
        # Um `.php` novo que carrega um irmao pelo idioma desta pasta nao
        # reprova nada: a conta cresce e a propriedade continua valendo.
        alvo = os.path.join(ilha, "ferramentas", "render-novo-para-teste.php")  # ENCENACAO
        with io.open(alvo, "w", encoding="utf-8") as f:
            f.write("<?php\nrequire __DIR__ . '/render-para-teste.php';\n")  # ENCENACAO
        return True

    mundo_que_passa(
        "A. um .php novo e honesto entra na pasta e nada reprova",
        php_novo_e_honesto,
    )

    def mjs_novo(ilha):
        # Linguagem que esta regua NAO le entra na pasta: ela tem de aparecer
        # nomeada no limite, e a metade da cobertura continua verde. E o lado
        # oposto da mutacao 13.
        alvo = os.path.join(ilha, "ferramentas", "teste-coisa-nova.mjs")  # ENCENACAO
        with io.open(alvo, "w", encoding="utf-8") as f:
            f.write("// irmao encenado, nao e lido por esta regua\n")
        return True

    mundo_que_passa(
        "B. um .mjs novo entra na pasta e a cobertura declarada continua fechada",
        mjs_novo,
    )

    def comentario_que_cita(ilha):
        # Citar o nome de um irmao em COMENTARIO de PHP nao cria ato nenhum. Se
        # criasse, esta regua seria a varredura por nome que ela existe para
        # medir — e a `regua-classes-da-bancada.py` ja pagou esse defeito.
        return troca_em(ilha, LEITOR, "<?php\n",
                        "<?php\n// fala do render-para-teste.php sem agir nele\n")  # ENCENACAO

    mundo_que_passa(
        "C. comentario de PHP que cita um irmao NAO vira ato",
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
