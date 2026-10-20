#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BANCADA: sem rede — exercita a `regua-exercitadores.py` contra pastas
ENCENADAS, contra a pasta REAL desta ilha, e cobra a propriedade que a conta
dela achou.

As tres metades:

  1. **A FIACAO**, em mundos encenados: que a regua conte as TRES formas de
     exercicio (chamada, referencia, nome como texto), que o `def` de uma
     funcao nao a exercite, que exercicio seja contado por ARQUIVO e nao por
     sitio, e que nome homonimo em dois arquivos nao seja atribuido por
     adivinhacao.
  2. **A CONTA**, na pasta real de hoje: `orfas()` vazia. Funcao definida que
     nenhum sitio desta pasta alcanca, em nenhuma das tres formas, e codigo
     morto — e o achado 11 do fecho de 20/10/2026 tirou tres destas antes do
     commit, a mao, porque nao havia portao.
  3. **A PROPRIEDADE DAS COPIAS**, que e o achado desta passada: todo
     `ler_pasta()` desta pasta tem de SOBREVIVER a um byte que nao e UTF-8. As
     copias nao sao listadas aqui — sao DESCOBERTAS pela arvore sintatica, e e
     por isso que a sexta copia, se nascer, ja entra cobrada.

O QUE ESTE PORTAO NAO AFIRMA, e esta escrito para nao ser lido como cobertura:
nem o numero de `dormindo()`, nem o de `so_o_proprio()`, nem o de `ambiguos()`.
Os tres sao IMPRESSOS e nenhum e cobrado. Ajudante privado chamado de um lugar
so e desenho correto na maior parte dos casos, e cobrar o numero faria deste
portao a lista digitada que esta pasta ja pegou tres vezes — a do
`teste-voz.mjs`, a da tabela de levas do `dados/indexacao.md` e a dos alvos do
`teste-arvore`.
"""

import ast
import importlib.util
import os
import sys
import tempfile

PASTA = os.path.dirname(os.path.abspath(__file__))


def _carregar(nome, apelido):
    spec = importlib.util.spec_from_file_location(apelido, os.path.join(PASTA, nome))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


E = _carregar('regua-exercitadores.py', 'regua_exercitadores')

falhas = []
afirmacoes = 0


def afirmar(condicao, frase):
    global afirmacoes
    afirmacoes += 1
    if not condicao:
        falhas.append(frase)


def mundo(**arquivos):
    """Uma pasta encenada: nome -> texto, exatamente o que a regua recebe."""
    return dict(arquivos)


def conta_de(arquivos):
    return {('%s|%s' % (a, n)): q for (a, n), q in E.contagem(arquivos).items()}


def formas_de(arquivos):
    return sorted((q, n, f) for q, _l, n, f in E.exercicios(arquivos))


# ---------------------------------------------------------------------------
# METADE 1 — A FIACAO
# ---------------------------------------------------------------------------
def metade_da_fiacao():
    print('\n1. A FIACAO — as tres formas, a atribuicao e a contagem por arquivo')

    # (a) As definicoes saem do TOPO, e so do topo.
    m = mundo(**{'regua-a.py': 'def no_topo():\n    def dentro():\n        pass\n'
                                'class C:\n    def metodo(self):\n        pass\n'})
    d = sorted(n for _a, n, _l in E.definicoes(m))
    afirmar(d == ['no_topo'],
            'so funcao de TOPO entra; metodo e funcao de dentro ficam fora: %r' % (d,))

    # (b) CHAMADA, a forma obvia.
    m = mundo(**{'regua-a.py': 'def alvo():\n    pass\n',
                 'teste-a.py': "import x\nR = x.carregar('regua-a.py')\nR.alvo()\n"})
    f = formas_de(m)
    afirmar(('teste-a.py', 'alvo', E.CHAMADA) in f,
            'chamada por atributo do modulo e CHAMADA: %r' % (f,))

    # (c) REFERENCIA: o nome como VALOR. E o idioma de toda bancada desta pasta,
    #     e e o que faz a varredura por chamada achar 82 orfas falsas.
    m = mundo(**{'regua-a.py': 'def caso_um():\n    pass\n'
                               'CASOS = (("E1", caso_um, "erro"),)\n'})
    f = formas_de(m)
    afirmar(f == [('regua-a.py', 'caso_um', E.REFERENCIA)],
            'nome posto numa tupla de casos e REFERENCIA, nao chamada: %r' % (f,))

    # (d) POR_NOME: o nome como TEXTO, e so quando a string e o nome INTEIRO.
    m = mundo(**{'regua-a.py': 'def alvo():\n    pass\n',
                 'mutacoes-a.py': "troca('alvo')\n"})
    f = formas_de(m)
    afirmar(('mutacoes-a.py', 'alvo', E.POR_NOME) in f,
            'string igual ao nome e POR_NOME: %r' % (f,))

    m = mundo(**{'regua-a.py': 'def alvo():\n    pass\n',
                 'mutacoes-a.py': "troca('def alvo(x):')\n"})
    f = formas_de(m)
    afirmar([x for x in f if x[0] == 'mutacoes-a.py'] == [],
            'string que CONTEM o nome nao e sitio — prova fraca nao conta: %r' % (f,))

    # (e) O `def` nao se exercita, e o portao disto e o caso em que o arquivo
    #     que define nao tem nenhum outro sitio: a conta tem de dar ZERO.
    m = mundo(**{'regua-a.py': 'def sozinha():\n    pass\n'})
    afirmar(conta_de(m) == {'regua-a.py|sozinha': 0},
            'o cabecalho da propria definicao nao e exercicio: %r' % (conta_de(m),))

    # (f) Chamada recursiva faz do PROPRIO arquivo o primeiro exercitador — e
    #     foi exatamente a condicao do `_base`: um exercitador, e ele mesmo.
    m = mundo(**{'regua-a.py': 'def rec(n):\n    return rec(n - 1)\n'})
    afirmar(conta_de(m) == {'regua-a.py|rec': 1},
            'chamada no proprio arquivo conta UM exercitador: %r' % (conta_de(m),))

    # (g) Contado por ARQUIVO, nunca por sitio. Dez chamadas no mesmo arquivo
    #     continuam sendo um exercitador — o que acordou o `_base` foi o
    #     segundo ARQUIVO, nao a decima chamada.
    m = mundo(**{'regua-a.py': 'def alvo():\n    pass\n'
                               'def um():\n    return alvo()\n'
                               'def dois():\n    return alvo()\n'
                               'def tres():\n    return alvo()\n'})
    afirmar(conta_de(m)['regua-a.py|alvo'] == 1,
            'tres sitios no mesmo arquivo sao UM exercitador: %r' % (conta_de(m),))

    # (h) Dois arquivos, dois exercitadores — e o segundo so conta porque ele
    #     CARREGA quem define, ou porque o nome e unico na pasta.
    m = mundo(**{'regua-a.py': 'def alvo():\n    pass\n'
                               'def um():\n    return alvo()\n',
                 'teste-a.py': "import importlib.util\n"
                               "importlib.util.spec_from_file_location('r', 'regua-a.py')\n"
                               "R.alvo()\n"})
    afirmar(conta_de(m)['regua-a.py|alvo'] == 2,
            'arquivo que carrega quem define e o segundo exercitador: %r' % (conta_de(m),))

    # (i) HOMONIMO: o mesmo nome em dois arquivos, e um terceiro que nao carrega
    #     nenhum dos dois. A regua NAO escolhe — o sitio vai para ambiguos().
    m = mundo(**{'regua-a.py': 'def main():\n    pass\n',
                 'regua-b.py': 'def main():\n    pass\n',
                 'teste-c.py': 'main()\n'})
    amb = [(q, n, d) for q, _l, n, d in E.ambiguos(m)]
    afirmar(amb == [('teste-c.py', 'main', ['regua-a.py', 'regua-b.py'])],
            'homonimo sem carga declarada nao e atribuido a ninguem: %r' % (amb,))
    c = conta_de(m)
    afirmar(c['regua-a.py|main'] == 0 and c['regua-b.py|main'] == 0,
            'e nenhuma das homonimas recebe o sitio ambiguo: %r' % (c,))

    # (j) E o sitio ambiguo ainda assim IMPEDE a acusacao de codigo morto: ele
    #     exercita uma das duas, e a regua nao sabe qual. `main` e protocolo,
    #     entao o mundo usa outro nome para medir isto.
    m = mundo(**{'regua-a.py': 'def forma():\n    pass\n',
                 'regua-b.py': 'def forma():\n    pass\n',
                 'teste-c.py': 'forma()\n'})
    orf = [(a, n) for a, n, _l in E.orfas(m)]
    afirmar(orf == [],
            'funcao com sitio ambiguo NAO e chamada de morta: %r' % (orf,))

    # (k) Agora a orfa de verdade: nenhuma das tres formas, em nenhum arquivo.
    # O `chama()` tem de ser exercitado tambem, senao ele e orfa do mesmo jeito
    # — foi o que esta afirmacao mediu errado na primeira passada, e o mundo
    # estava incompleto, nao a regua.
    m = mundo(**{'regua-a.py': 'def viva():\n    pass\n'
                               'def chama():\n    return viva()\n'
                               'def morta():\n    pass\n'
                               'chama()\n'})
    orf = [n for _a, n, _l in E.orfas(m)]
    afirmar(orf == ['morta'],
            'funcao sem UM sitio nas tres formas e orfa, e so ela: %r' % (orf,))

    # (l) `main` nao e orfa nunca: quem a exercita e o `if __name__`, que nao e
    #     sitio de chamada nenhum. Protocolo declarado em vez de descoberto.
    m = mundo(**{'regua-a.py': 'def main():\n    return 0\n'})
    afirmar([n for _a, n, _l in E.orfas(m)] == [],
            'nome de protocolo nao entra em orfas()')

    # (m) COMPARTILHADA e so a funcao de arquivo que um IRMAO carrega. Funcao
    #     de dentro de um portao nao tem segundo leitor possivel.
    m = mundo(**{'regua-a.py': 'def da_regua():\n    pass\n',
                 'teste-a.py': "import importlib.util\n"
                               "importlib.util.spec_from_file_location('r', 'regua-a.py')\n"
                               "def do_portao():\n    pass\n"})
    comp = sorted(n for _a, n in E.compartilhadas(m))
    afirmar(comp == ['da_regua'],
            'so funcao de arquivo carregado por irmao e compartilhada: %r' % (comp,))

    # (n) DORMINDO e a resposta do item 4: compartilhada com um exercitador so.
    m = mundo(**{'regua-a.py': 'def dorme():\n    pass\n'
                               'def acorda():\n    return dorme()\n',
                 'teste-a.py': "import importlib.util\n"
                               "importlib.util.spec_from_file_location('r', 'regua-a.py')\n"
                               "R.acorda()\n"})
    dorm = [(a, n, u) for a, n, u in E.dormindo(m)]
    afirmar(dorm == [('regua-a.py', 'acorda', 'teste-a.py'),
                     ('regua-a.py', 'dorme', 'regua-a.py')],
            'as DUAS tem um exercitador so, e so uma delas o proprio arquivo: %r' % (dorm,))
    afirmar([n for _a, n in E.so_o_proprio(m)] == ['dorme'],
            'e ela entra em so_o_proprio(), que e o subconjunto do `_base`')

    # (o) Duas leituras acordam a funcao, e e a frase inteira do item 4.
    m = mundo(**{'regua-a.py': 'def dorme():\n    pass\n',
                 'teste-a.py': "import importlib.util\n"
                               "importlib.util.spec_from_file_location('r', 'regua-a.py')\n"
                               "R.dorme()\n",
                 'teste-b.py': "import importlib.util\n"
                               "importlib.util.spec_from_file_location('r', 'regua-a.py')\n"
                               "R.dorme()\n"})
    afirmar(E.dormindo(m) == [],
            'com DOIS leitores ela sai de dormindo(): %r' % (E.dormindo(m),))

    # (p) A pasta e dado, e a regua nao abre disco nenhum para decidir.
    m = mundo(**{'regua-a.py': 'def so_aqui():\n    pass\n'})
    afirmar([n for _a, n, _l in E.definicoes(m)] == ['so_aqui'],
            'a regua decide sobre pasta que nao existe no disco')

    # (q) Arquivo que nao parseia nao derruba a regua: ele vai para nao_lidos().
    m = mundo(**{'regua-a.py': 'def viva():\n    pass\n'
                               'def chama():\n    return viva()\n'
                               'chama()\n',
                 'regua-torta.py': 'def (\n'})
    nl = [n for n, _m in E.nao_lidos(m)]
    afirmar(nl == ['regua-torta.py'],
            'arquivo que nao parseia e LIMITE declarado, nao excecao: %r' % (nl,))
    afirmar([n for _a, n, _l in E.orfas(m)] == [],
            'e ele nao faz ninguem virar orfa')

    # (r) `.mjs` e `.php` nao sao lidos, e isso e dito e nao calado.
    m = mundo(**{'regua-a.py': 'def viva():\n    pass\n'
                               'def chama():\n    return viva()\n'
                               'chama()\n',
                 'teste-voz.mjs': 'function f() {}\n',
                 'render.php': '<?php function g() {} ?>\n'})
    nl = dict(E.nao_lidos(m))
    afirmar(sorted(nl) == ['render.php', 'teste-voz.mjs'],
            'os dois idiomas de fora aparecem NOMEADOS no limite: %r' % (nl,))


# ---------------------------------------------------------------------------
# METADE 2 — A CONTA, NA PASTA REAL
# ---------------------------------------------------------------------------
def metade_da_conta():
    print('\n2. A CONTA — na pasta real desta ilha, hoje')
    arquivos = E.ler_pasta()
    afirmar(len(arquivos) > 100,
            'a pasta real tem mais de cem arquivos (%d)' % len(arquivos))

    defs = E.definicoes(arquivos)
    afirmar(len(defs) > 300,
            'e mais de trezentas funcoes de topo (%d)' % len(defs))

    orf = E.orfas(arquivos)
    afirmar(orf == [],
            'ZERO funcao orfa na pasta real — %d achada(s): %s'
            % (len(orf), ', '.join('%s:%s' % (a, n) for a, n, _l in orf[:6])))

    ex = E.exercicios(arquivos)
    formas = {f for _q, _l, _n, f in ex}
    afirmar(formas == {E.CHAMADA, E.REFERENCIA, E.POR_NOME},
            'as TRES formas aparecem na pasta real — nenhum ramo esta morto: %r' % (formas,))

    por_forma = {}
    for _q, _l, _n, f in ex:
        por_forma[f] = por_forma.get(f, 0) + 1
    afirmar(por_forma.get(E.REFERENCIA, 0) > 500,
            'a REFERENCIA nao e caso de borda nesta pasta: %d sitios'
            % por_forma.get(E.REFERENCIA, 0))

    comp = sorted(set(E.compartilhadas(arquivos)))
    afirmar(len(comp) > 100,
            'ha mais de cem funcoes compartilhadas (%d)' % len(comp))

    # IMPRESSO E NAO COBRADO, de proposito — ver a docstring deste arquivo.
    dorm = E.dormindo(arquivos)
    print('   compartilhadas: %d | com um exercitador so: %d | sem leitor de fora: %d'
          % (len(comp), len(dorm), len(E.so_o_proprio(arquivos))))
    print('   sitios: %d | nao atribuidos (homonimo): %d'
          % (len(ex), len(E.ambiguos(arquivos))))


# ---------------------------------------------------------------------------
# METADE 3 — A PROPRIEDADE DAS COPIAS
# ---------------------------------------------------------------------------
def copias_de(nome_da_funcao):
    """Os arquivos desta pasta que definem `nome_da_funcao` no topo.

    DESCOBERTO pela arvore, nunca listado: a quinta copia do `ler_pasta()`
    nasceu sem ninguem notar, e lista escrita a mao nao avisa quem falta."""
    arquivos = E.ler_pasta()
    return sorted(a for a, n, _l in E.definicoes(arquivos) if n == nome_da_funcao)


def pasta_com_byte_torto():
    """Uma pasta de verdade, com um `.py` que tem um byte que nao e UTF-8.

    O byte `0xe9` e o `e` acentuado em latin-1, que e o jeito realista de isto
    acontecer nesta ilha: arquivo com acento salvo na codificacao errada."""
    pasta = tempfile.mkdtemp(prefix='aqm-exerc-utf8-')
    with open(os.path.join(pasta, 'regua-torta.py'), 'wb') as f:
        f.write(b'# -*- coding: utf-8 -*-\n# acento torto: \xe9\ndef f():\n    pass\n')
    with open(os.path.join(pasta, 'regua-sa.py'), 'w', encoding='utf-8') as f:
        f.write('def g():\n    pass\n')
    return pasta


def metade_das_copias():
    print('\n3. AS COPIAS DO `ler_pasta()` — todas sobrevivem a byte que nao e UTF-8')
    copias = copias_de('ler_pasta')
    afirmar(len(copias) >= 4,
            'esta pasta tem QUATRO ou mais `ler_pasta()`, e elas foram descobertas: %r'
            % (copias,))
    afirmar('regua-alvos-de-portao.py' in copias,
            'a copia da irma esta entre as descobertas')

    pasta = pasta_com_byte_torto()
    for nome in copias:
        apelido = nome[:-3].replace('-', '_')
        try:
            mod = _carregar(nome, apelido)
        except Exception as e:
            afirmar(False, '%s nao carrega: %s' % (nome, type(e).__name__))
            continue
        try:
            lido = mod.ler_pasta(pasta)
        except Exception as e:
            afirmar(False,
                    '%s morreu de %s num byte que nao e UTF-8 — um arquivo torto '
                    'nesta pasta derruba esta regua inteira' % (nome, type(e).__name__))
            continue
        afirmar('regua-torta.py' in lido,
                '%s LEU o arquivo torto em vez de o perder calada' % nome)
        afirmar(lido.get('regua-sa.py') == 'def g():\n    pass\n',
                '%s continua lendo o arquivo sao' % nome)

    # E a propriedade vale na pasta REAL tambem: nenhuma copia morre nela.
    for nome in copias:
        apelido = 'real_' + nome[:-3].replace('-', '_')
        try:
            mod = _carregar(nome, apelido)
            n = len(mod.ler_pasta())
        except Exception as e:
            afirmar(False, '%s morreu lendo a pasta real: %s' % (nome, type(e).__name__))
            continue
        afirmar(n > 50, '%s le a pasta real inteira (%d arquivos)' % (nome, n))


# ---------------------------------------------------------------------------
# METADE 4 — A REGUA E UMA SO
# ---------------------------------------------------------------------------
def metade_da_regua_unica():
    print('\n4. A REGUA E UMA SO — o vocabulario de pasta vem da irma, nao de uma copia')
    with open(os.path.join(PASTA, 'regua-exercitadores.py'), encoding='utf-8') as f:
        regua = f.read()
    afirmar('regua-alvos-de-portao.py' in regua,
            'a regua nova IMPORTA a irma pelo nome, e por isso nao a recopia')
    afirmar('\ndef atos(' not in regua,
            'ela NAO tem um atos() proprio — o grafo de carga e da irma')
    arv = ast.parse(regua)
    corpos = [n.name for n in arv.body
              if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
    afirmar('ler_pasta' in corpos,
            'ela expoe ler_pasta() para o portao poder chamar, e delega o corpo')
    afirmar('import ast' in regua,
            'ela le a ARVORE e nao o texto — e o que a separa da varredura por nome')
    afirmar('LIMITE' in regua or 'limite' in regua,
            'ela escreve o limite dela no proprio arquivo')

    with open(os.path.join(PASTA, 'teste-exercitadores.py'), encoding='utf-8') as f:
        meu = f.read()
    afirmar('\ndef definicoes(' not in meu,
            'este portao NAO tem uma definicoes() propria')
    # Afirmacao sobre o proprio ESTADO, nunca sobre o proprio TEXTO: o achado 5
    # do fecho de 20/10 mostrou que afirmacao sobre o texto do proprio arquivo
    # o autor nao satisfaz sem mentir.
    afirmar(hasattr(E, 'orfas') and hasattr(E, 'dormindo'),
            'o portao chega a regua pelo namespace, nao por procurar palavra no texto')


def main():
    print('EXERCITADORES — quantos arquivos de ferramentas/ exercitam cada funcao')
    print('=' * 78)
    metade_da_fiacao()
    metade_da_conta()
    metade_das_copias()
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
