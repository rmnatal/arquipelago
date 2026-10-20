#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BANCADA: sem rede — exercita a `regua-alvos-em-php.py` contra pastas
ENCENADAS e contra a pasta REAL desta ilha.

As tres metades, pelo mesmo desenho do `teste-alvos-de-portao.py`:

  1. **A FIACAO**, em mundos encenados: que a regua siga o nome do alvo por
     literal, por variavel e por cadeia de variaveis; que ela ache o nome
     COLADO que nao existe no texto, que e o buraco inteiro do item 7; que o
     `eval( file_get_contents( X ) )` conte UMA vez e nao duas; que ato sobre SI
     MESMO nao vire ato sobre irmao; e que o nome escrito num COMENTARIO nao
     produza ato nenhum, que e o que separa ler a linguagem de varrer o texto.
  2. **A CONTA**, na pasta real de hoje: zero ato invisivel, e nenhuma CARGA
     por resolver. Carga sempre nomeia um arquivo so; carga que nao resolve e
     exatamente onde um alvo invisivel se esconderia.
  3. **A COBERTURA DECLARADA**, que e a parte nova e e a que tem dentes sobre os
     `.mjs`: todo arquivo de `ferramentas/` ou e lido por uma das duas reguas,
     ou aparece NOMEADO num limite de uma delas. Esta afirmacao nao mede
     JavaScript nenhum — ela impede que uma linguagem nova entre na pasta e
     fique sem medicao por um mes, que e exatamente o que aconteceu com estes
     40 arquivos entre 22/09 e 20/10/2026.

O QUE ESTE PORTAO NAO AFIRMA, e esta escrito para nao ser lido como cobertura:
  * O numero de `indiretos()` e de `nao_resolvidos()` e IMPRESSO e nao e
    cobrado, pelo mesmo motivo da regua irma — cobrar o numero seria a lista
    digitada que o achado 4(c) de 20/10 ja pegou uma vez nesta familia.
  * **Alvo pendurado nao e defeito desta regua.** `require __DIR__ .
    '/nao-existe.php'` e literal, visivel, e simplesmente nao aparece na conta,
    porque o alvo nao e arquivo desta pasta. Quem quiser cobrar alvo que nao
    existe precisa de outra regua, e ela nao nasce aqui.
  * **Nenhuma afirmacao sobre `.mjs`.** A metade 3 fala dos NOMES deles, nunca
    do que eles fazem.
"""

import importlib.util
import os
import sys
import types

PASTA = os.path.dirname(os.path.abspath(__file__))


def _carregar(arquivo, apelido):
    spec = importlib.util.spec_from_file_location(apelido, os.path.join(PASTA, arquivo))
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


R = _carregar('regua-alvos-em-php.py', 'regua_alvos_em_php')
IRMA = _carregar('regua-alvos-de-portao.py', 'regua_alvos_de_portao')

falhas = []
afirmacoes = 0


def afirmar(condicao, frase):
    global afirmacoes
    afirmacoes += 1
    if not condicao:
        falhas.append(frase)


# OS NOMES ENCENADOS ABAIXO SE DECLARAM ENCENACAO, e isso nao e zelo: sem o
# marcador, a `regua-classes-da-bancada.py` leria este portao como quem
# EXERCITA um irmao de verdade, e uma regua orfa de nome parecido passaria a
# escapar da denuncia pelo texto deste arquivo. O laco esta medido no achado 4
# do fecho de 20/10/2026 as 13h18Z.
QUEM_AGE = 'teste-quem-age.php'   # ENCENACAO
ALVO = 'regua-alvo.php'           # ENCENACAO


def mundo(corpo, extras=None):
    """Uma pasta encenada: quem age mais os irmaos que ela precisa ter."""
    arquivos = {QUEM_AGE: '<?php\n' + corpo + '\n'}
    for nome in (extras if extras is not None else [ALVO]):
        arquivos[nome] = "<?php\n// irmao encenado\n"
    return arquivos


def _uma_vez(corpos):
    """Le TODOS os mundos de uma metade com UMA chamada de `php` por arquivo.

    Cada mundo e uma pasta temporaria propria; ler um a um e o desenho, e o
    custo e um processo de `php` por arquivo encenado. Esta funcao existe para
    a metade da fiacao nao pagar duas vezes pelo mesmo mundo."""
    return [R.ler(m) for m in corpos]


def atos_de(corpo, extras=None):
    m = mundo(corpo, extras)
    lidos, falhos = R.ler(m)
    assert not falhos, falhos
    return [(r[2], r[3], r[4], r[5]) for r in R.atos(m, lidos)]


def nao_resolvidos_de(corpo, extras=None):
    m = mundo(corpo, extras)
    lidos, _ = R.ler(m)
    return R.nao_resolvidos(m, lidos)


def invisiveis_de(corpo, extras=None):
    m = mundo(corpo, extras)
    lidos, _ = R.ler(m)
    return R.invisiveis(m, lidos)


# ---------------------------------------------------------------------------
# METADE 1 — A FIACAO
# ---------------------------------------------------------------------------
def metade_da_fiacao():
    print('1. A FIACAO, em mundos encenados')

    # (a) o idioma real desta pasta: 12 dos 12 atos de hoje tem esta forma
    a = atos_de("require __DIR__ . '/" + ALVO + "';")
    afirmar(a == [('carrega', ALVO, R.LITERAL, True)],
            'require __DIR__ . literal -> carrega, literal, visivel  (deu %r)' % (a,))

    # (b) require_once, include e include_once sao a mesma carga
    for palavra in ('require_once', 'include', 'include_once'):
        a = atos_de(palavra + " __DIR__ . '/" + ALVO + "';")
        afirmar(a == [('carrega', ALVO, R.LITERAL, True)],
                '%s tambem e carga  (deu %r)' % (palavra, a))

    # (c) por variavel: o nome chega ao literal, e a posicao CAI para indireto
    a = atos_de("$x = __DIR__ . '/" + ALVO + "';\nrequire $x;")
    afirmar(a == [('carrega', ALVO, R.INDIRETO, True)],
            'variavel -> indireto, e continua visivel  (deu %r)' % (a,))

    # (d) cadeia de duas variaveis: o ponto fixo atravessa mais de um degrau
    a = atos_de("$x = '" + ALVO + "';\n$y = $x;\nrequire $y;")
    afirmar(a == [('carrega', ALVO, R.INDIRETO, True)],
            'cadeia de duas variaveis resolve  (deu %r)' % (a,))

    # (e) O CASO COM DENTES: nome COLADO de dois pedacos, e ele NAO esta no texto
    corpo = "require 'regua-' . 'alvo.php';"   # ENCENACAO
    a = atos_de(corpo)
    afirmar(a == [('carrega', ALVO, R.CONSTRUIDO, False)],
            'nome colado de dois literais -> construido e INVISIVEL  (deu %r)' % (a,))
    afirmar(len(invisiveis_de(corpo)) == 1,
            'e esse mundo faz invisiveis() deixar de ser vazia — a propriedade morde')

    # (f) o eval desta pasta e UMA carga, nao uma carga mais uma leitura
    a = atos_de("eval( file_get_contents( __DIR__ . '/" + ALVO + "' ) );")
    afirmar(a == [('carrega', ALVO, R.LITERAL, True)],
            'eval(file_get_contents(X)) conta UMA vez, como carga  (deu %r)' % (a,))

    # (g) leitura e invocacao, cada uma com o seu rotulo
    a = atos_de("$s = file_get_contents( __DIR__ . '/" + ALVO + "' );")
    afirmar(a == [('abre', ALVO, R.LITERAL, True)],
            'file_get_contents fora do eval -> abre  (deu %r)' % (a,))
    a = atos_de("exec( 'php ' . __DIR__ . '/" + ALVO + "' );")
    afirmar(a == [('invoca', ALVO, R.LITERAL, True)],
            'exec -> invoca  (deu %r)' % (a,))
    for palavra in ('shell_exec', 'system', 'passthru'):
        a = atos_de(palavra + "( 'php ' . __DIR__ . '/" + ALVO + "' );")
        afirmar(a == [('invoca', ALVO, R.LITERAL, True)],
                '%s tambem e invocacao  (deu %r)' % (palavra, a))

    # (h) ATO SOBRE SI MESMO nao e ato sobre irmao, e nao fica por resolver.
    #     E o `exec( ... __FILE__ ... )` com que o teste-atualizador-sync.php se
    #     re-invoca; sem o operando `file` ele sairia como limite inventado.
    a = atos_de("exec( escapeshellarg( PHP_BINARY ) . ' ' . escapeshellarg( __FILE__ ) );")
    afirmar(a == [], 'ato sobre __FILE__ nao e ato sobre irmao  (deu %r)' % (a,))
    afirmar(nao_resolvidos_de(
        "exec( escapeshellarg( __FILE__ ) );") == [],
        'e ele tambem nao entra na lista do que nao resolveu')
    #     E O MUNDO EM QUE ISSO IMPORTA DE VERDADE e o da re-invocacao que
    #     nomeia a PASTA: `__DIR__` faz o sitio falar desta pasta, entao sem a
    #     pergunta do `__FILE__` ele sairia na lista do que nao resolveu — um
    #     limite inventado, num ato cujo alvo e perfeitamente conhecido. A
    #     primeira versao deste portao nao tinha este mundo, e DUAS mutacoes
    #     sobreviveram por isso: o `_proprio()` era codigo sem efeito observavel.
    nr = nao_resolvidos_de("exec( 'php ' . __DIR__ . '/' . basename( __FILE__ ) );")
    afirmar(nr == [],
            're-invocacao de SI MESMO pela pasta nao e limite nenhum  (deu %r)' % (nr,))

    # (i) QUEM LE PHP E O PHP: o nome dentro de um COMENTARIO nao produz ato.
    #     Esta e a afirmacao que separa esta regua de uma varredura de texto, e
    #     e o defeito que a regua-classes-da-bancada.py pagou em 20/10 de manha.
    a = atos_de("// require __DIR__ . '/" + ALVO + "';\n$nada = 1;")
    afirmar(a == [], 'nome em comentario de linha nao e ato  (deu %r)' % (a,))
    a = atos_de("/* require __DIR__ . '/" + ALVO + "'; */\n$nada = 1;")
    afirmar(a == [], 'nome em comentario de bloco nao e ato  (deu %r)' % (a,))
    a = atos_de("$frase = \"require __DIR__ . '/" + ALVO + "';\";")
    afirmar(a == [], 'nome dentro de string que nao e ato nao e ato  (deu %r)' % (a,))

    # (j) alvo que nao e desta pasta nao entra — nem JSON, nem markdown
    a = atos_de("$j = file_get_contents( __DIR__ . '/../dados/produtos-filtros.json' );")
    afirmar(a == [], 'JSON de dados/ nao e ato sobre irmao  (deu %r)' % (a,))
    afirmar(nao_resolvidos_de(
        "$j = file_get_contents( $raiz . '/../dados/x.json' );") == [],
        'e leitura de dado que nao fala da pasta nao polui o que nao resolveu')

    # (k) o que NAO resolve, e os dois casos sao idiomas reais desta pasta
    nr = nao_resolvidos_de("require $desconhecido;")
    afirmar(len(nr) == 1 and nr[0][2] == 'carrega',
            'carga por variavel nunca atribuida fica por RESOLVER, nomeada  (deu %r)' % (nr,))
    nr = nao_resolvidos_de("$nome = 'alvo';\n$f = \"regua-$nome.php\";\nrequire $f;")
    afirmar(len(nr) == 1,
            'nome com buraco de interpolacao fica por resolver  (deu %r)' % (nr,))

    #     E O BURACO TEM DE SER BURACO MESMO QUANDO O PEDACO QUE FALTA CARREGA O
    #     NOME INTEIRO. Aqui `$nome` vale o nome do irmao e a interpolacao o
    #     costura num caminho: quem tratar a variavel interpolada como variavel
    #     comum vai RESOLVER o alvo a partir de dentro de uma string, que e
    #     exatamente o molde que esta regua declara nao executar. A regua irma
    #     faz o mesmo com a f-string, e as duas erram para baixo de proposito.
    corpo = "$nome = '" + ALVO + "';\n$f = \"x/$nome\";\nrequire $f;"
    afirmar(atos_de(corpo) == [],
            'variavel INTERPOLADA em string nao resolve alvo  (deu %r)' % (atos_de(corpo),))
    afirmar(len(nao_resolvidos_de(corpo)) == 1,
            'e o sitio sai NOMEADO no que nao resolveu, nunca calado')
    nr = nao_resolvidos_de(
        "foreach ( glob( __DIR__ . '/*.php' ) as $f ) { require $f; }")
    afirmar(len(nr) == 1,
            'o idioma de quem varre a pasta inteira fica por resolver  (deu %r)' % (nr,))
    # E ELA TEM DE SER RECONHECIDA COMO CARGA QUE FALA DESTA PASTA, que e a
    # unica familia que o portao cobra na metade 2. Aqui o `__DIR__` esta na
    # ATRIBUICAO e o sitio do ato so tem `$f`: quem nao seguir a variavel vai
    # responder "nao fala da pasta" justamente na carga mais perigosa que o
    # idioma desta pasta permite.
    afirmar(len(nr) == 1 and nr[0][4] is True,
            'e ela e reconhecida como carga que FALA desta pasta  (deu %r)' % (nr,))
    nr = nao_resolvidos_de(
        "foreach ( glob( __DIR__ . '/../snippets/*.php' ) as $f ) { require $f; }")
    afirmar(len(nr) == 1 and nr[0][4] is True,
            'carga por varredura ainda fala da pasta quando o caminho sai dela por '
            '__DIR__  (deu %r)' % (nr,))

    # (o) ATO SOBRE O PROPRIO ARQUIVO, por nome e nao por __FILE__: tambem nao e
    #     ato sobre irmao. Sem esta afirmacao, a exclusao de `alvo == quem` em
    #     atos() poderia morrer em silencio — e a conta desta pasta ganharia 12
    #     auto-cargas que nunca existiram.
    a = atos_de("require __DIR__ . '/" + QUEM_AGE + "';")
    afirmar(a == [], 'carga do PROPRIO arquivo nao e ato sobre irmao  (deu %r)' % (a,))

    # (p) METODO HOMONIMO NAO E A FUNCAO DO PHP. `file()` e funcao da linguagem e
    #     tambem e nome de metodo plausivel; `$o->file(...)` nao abre arquivo
    #     nenhum. Quem nao distinguir conta ato que nao aconteceu.
    a = atos_de("$o = new Coisa();\n$o->file( __DIR__ . '/" + ALVO + "' );")
    afirmar(a == [], 'metodo com nome de funcao do PHP nao e ato  (deu %r)' % (a,))

    # (l) a pasta e DADO: um mundo sem irmao nenhum nao produz ato
    a = atos_de("require __DIR__ . '/" + ALVO + "';", extras=[])
    afirmar(a == [], 'sem o irmao na pasta nao ha ato sobre irmao  (deu %r)' % (a,))

    # (m) SINTAXE QUEBRADA NAO E RECUSA, E ISSO FOI MEDIDO AQUI.
    #     A primeira versao desta afirmacao encenava `require 1 1 1 ;` esperando
    #     que o leitor recusasse o arquivo — e ele LEU, porque
    #     `token_get_all()` nao e um analisador sintatico: ele tokeniza
    #     qualquer sequencia de bytes e nunca falha. Entao a regua le o `.php`
    #     sintaticamente quebrado e mede os atos que os tokens mostrarem, que e
    #     mais cobertura e nao menos — e nao autoriza ninguem a ler esta regua
    #     como conferencia de sintaxe. O portao que confere sintaxe de PHP
    #     existe e e outro: o `--check` do `conferir-entidades.mjs`.
    m = {QUEM_AGE: '<?php\nrequire 1 1 1 ;\n'}
    lidos, falhos = R.ler(m)
    afirmar(falhos == [] and QUEM_AGE in lidos,
            'sintaxe quebrada NAO e recusa: o tokenizador le e a regua mede  (deu %r)'
            % (falhos,))

    # (n) A FALHA DE LEITURA QUE EXISTE DE VERDADE e o leitor em PHP ausente, e
    #     ela sai NOMEADA em vez de virar pasta sem ato nenhum. O lado seguro do
    #     erro: sem leitor, `invisiveis()` ficaria vazia por falta de medicao e
    #     o portao aprovaria o nada — e e por isso que a metade 2 cobra
    #     `falhos == []` em separado.
    leitor_real = R.LEITOR
    try:
        R.LEITOR = os.path.join(PASTA, 'leitor-que-nao-existe.php')   # ENCENACAO
        m = mundo("require __DIR__ . '/" + ALVO + "';")
        lidos, falhos = R.ler(m)
        afirmar(lidos == {} and sorted(n for n, _ in falhos) == sorted(m),
                'sem o leitor em PHP, TODO .php sai nomeado em falhos  (deu %r)' % (falhos,))
        afirmar(R.atos(m, lidos) == [],
                'e a conta fica vazia — e por isso a metade 2 cobra falhos vazia')
        afirmar(all(n in {x for x, _ in R.nao_lidos(m, falhos)} for n in m),
                'os dois arquivos aparecem em nao_lidos(), nenhum aprovado em silencio')
    finally:
        R.LEITOR = leitor_real


# ---------------------------------------------------------------------------
# METADE 2 — A CONTA, na pasta real
# ---------------------------------------------------------------------------
def metade_da_conta():
    print('\n2. A CONTA, na pasta real desta ilha')
    arquivos = R.ler_pasta()
    lidos, falhos = R.ler(arquivos)
    todos = R.atos(arquivos, lidos)
    inv = R.invisiveis(arquivos, lidos)
    ind = R.indiretos(arquivos, lidos)
    nr = R.nao_resolvidos(arquivos, lidos)

    # A AFIRMACAO COM DENTES, e ela e uma PROPRIEDADE e nao um numero.
    afirmar(inv == [],
            'ZERO ato sobre irmao com nome invisivel nos .php  (achados: %r)'
            % ([(r[0], r[1], r[3]) for r in inv],))

    # A PERGUNTA CERTA NAO E "nenhuma carga por resolver", E FOI O CONSERTO DO
    # `_base` QUE MOSTROU ISSO. Com o `*.php` deixando de passar por nome de
    # arquivo, o `eval( file_get_contents( $arquivo ) )` do
    # `render-para-teste.php` apareceu como carga por resolver — e ele varre
    # `snippets/`, nao `ferramentas/`. Carga que varre OUTRA pasta nao pode
    # esconder irmao nenhum, por construcao. A carga perigosa e a que nao
    # resolve E FALA DESTA PASTA, e e essa que o portao cobra.
    cargas_daqui = [r for r in nr if r[2] == 'carrega' and r[4]]
    afirmar(cargas_daqui == [],
            'nenhuma CARGA que fala de ferramentas/ ficou por resolver  (achadas: %r)'
            % (cargas_daqui,))

    afirmar(falhos == [],
            'todo .php da pasta foi lido pelo tokenizador — aqui recusa e DEFEITO, '
            'nao limite, porque a classe sem rede da bancada exige o php  (deu %r)'
            % (falhos,))

    # A regua mede de verdade, e nao esta passando por conta vazia — a doenca
    # que a secao 8 do contrato chama de portao inerte.
    afirmar(len(todos) > 0,
            'a regua mede a pasta real de verdade (%d atos sobre irmao)' % len(todos))
    afirmar(any(r[2] == 'carrega' for r in todos),
            'o ato de CARGA aparece na pasta real — o ramo nao esta morto')

    print('   atos sobre irmao em .php: %d  (indiretos %d, por resolver %d)'
          % (len(todos), len(ind), len(nr)))
    for quem, linha, tipo, txt, pasta in nr:
        print('   por resolver: %s:%s %s %s%s'
              % (quem, linha, tipo, txt, '   [FALA DESTA PASTA]' if pasta else ''))


# ---------------------------------------------------------------------------
# METADE 3 — A COBERTURA DECLARADA
# ---------------------------------------------------------------------------
def metade_da_cobertura():
    print('\n3. A COBERTURA DECLARADA — nenhum arquivo da pasta fica sem nome')
    arquivos = R.ler_pasta()
    lidos, falhos = R.ler(arquivos)

    meus_limites = {n for n, _ in R.nao_lidos(arquivos, falhos)}
    limites_da_irma = {n for n, _ in IRMA.nao_lidos(arquivos)}
    lidos_pela_irma = {n for n in arquivos
                       if n.endswith('.py') and n not in limites_da_irma}

    coberto = set(lidos) | meus_limites | lidos_pela_irma | limites_da_irma
    sobra = sorted(set(arquivos) - coberto)
    afirmar(sobra == [],
            'todo arquivo de ferramentas/ e LIDO por uma das duas reguas ou aparece '
            'NOMEADO num limite delas  (orfaos: %r)' % (sobra,))

    # E as duas metades nao se sobrepoem: .py e da irma, .php e desta.
    afirmar(not (set(lidos) & lidos_pela_irma),
            'as duas reguas nao leem o mesmo arquivo — nao ha conta dobrada')
    afirmar(all(n.endswith('.php') for n in lidos),
            'esta regua le .php e so .php')

    mjs = sorted(n for n in arquivos if n.endswith('.mjs'))
    afirmar(all(n in meus_limites for n in mjs),
            'os .mjs aparecem nomeados no limite desta regua, um por um')

    # LINGUAGEM QUE NENHUMA DAS DUAS REGUAS CONHECE e o caso que da razao ao
    # terceiro grupo de `nao_lidos()`. A regua irma so nomeia `.py`, `.mjs` e
    # `.php`; um `.sh` ou um `.ts` que entre nesta pasta amanha nao esta em
    # NENHUMA das duas listas de extensao, e era assim — sem ninguem nomeando —
    # que estes 40 arquivos ficaram um mes sem medicao.
    inventada = dict(arquivos)
    inventada['varrer-coisa.sh'] = '#!/bin/sh\necho nada\n'   # ENCENACAO
    lidos_i, falhos_i = R.ler(inventada)
    limites_i = {n for n, _ in R.nao_lidos(inventada, falhos_i)}
    limites_irma_i = {n for n, _ in IRMA.nao_lidos(inventada)}
    afirmar('varrer-coisa.sh' in limites_i,
            'linguagem que nenhuma das duas reguas le aparece NOMEADA no limite desta')
    afirmar('varrer-coisa.sh' not in limites_irma_i,
            'e a regua irma nao a nomeia — e por isso que o terceiro grupo existe')
    print('   %d arquivos na pasta: %d lidos aqui, %d lidos pela regua irma, '
          '%d nomeados em limite' % (len(arquivos), len(lidos), len(lidos_pela_irma),
                                     len(meus_limites | limites_da_irma)))
    print('   dos nomeados em limite, %d sao .mjs — a metade que CONTINUA sem portao, '
          'medida em dados/atos-sobre-irmao-2026-10-20.md' % len(mjs))


# ---------------------------------------------------------------------------
# METADE 4 — A REGUA E UMA SO
# ---------------------------------------------------------------------------
def metade_da_regua_unica():
    print('\n4. A REGUA E UMA SO — ninguem recopia a leitura do PHP')
    with open(os.path.join(PASTA, 'teste-alvos-em-php.py'), encoding='utf-8') as f:
        meu = f.read()
    afirmar('regua-alvos-em-php.py' in meu,
            'este portao CARREGA a regua pelo nome, e por isso ela nao e denunciada')
    # DUAS VERSOES DESTA AFIRMACAO NAO PODIAM PASSAR NUNCA, e as duas pelo mesmo
    # motivo: elas procuravam, no texto DESTE arquivo, a palavra que a propria
    # frase da afirmacao escreve. Arquivo que fala SOBRE uma convencao parece
    # estar a usando — a mesma familia do achado 4 do fecho de 20/10 as 13h18Z,
    # onde um nome entre aspas fazia um portao "exercitar" uma regua orfa.
    #
    # O conserto nao e procurar melhor no texto: e perguntar a coisa certa. O
    # que importa nao e que palavra esta escrita aqui, e se este portao tem na
    # mao algum modulo capaz de abrir processo. Isso se pergunta ao NAMESPACE, e
    # ai o literal da frase nao contamina a resposta.
    meus_modulos = {n for n, v in list(globals().items())
                    if isinstance(v, types.ModuleType)}
    afirmar('subprocess' not in meus_modulos,
            'este portao nao importa quem abre processo: quem chama o PHP e a regua '
            '(importados: %r)' % (sorted(meus_modulos),))
    with open(os.path.join(PASTA, 'regua-alvos-em-php.py'), encoding='utf-8') as f:
        regua = f.read()
    afirmar('listar-atos-php.php' in regua,
            'a regua chama o leitor em PHP pelo nome, e nao varre texto')
    afirmar('LIMITE' in regua or 'limite' in regua,
            'a regua escreve o limite dela no proprio arquivo')
    with open(os.path.join(PASTA, 'listar-atos-php.php'), encoding='utf-8') as f:
        leitor = f.read()
    afirmar('token_get_all' in leitor,
            'quem le PHP e o PHP — o leitor usa o tokenizador da propria linguagem')
    afirmar('preg_match' not in leitor and 'strpos' not in leitor,
            'e o leitor nao tem varredura de texto nenhuma por tras do tokenizador')


def main():
    print('ALVOS EM PHP — como cada .php de ferramentas/ nomeia o irmao em que age')
    print('=' * 78)
    metade_da_fiacao()
    metade_da_conta()
    metade_da_cobertura()
    metade_da_regua_unica()
    print('=' * 78)
    if falhas:
        for f in falhas:
            print('FALHA  %s' % f)
        print('REPROVADO: %d de %d afirmacoes falharam.' % (len(falhas), afirmacoes))
        return 1
    print('APROVADO: %d afirmacoes, 0 falha.' % afirmacoes)
    return 0


if __name__ == '__main__':
    sys.exit(main())
