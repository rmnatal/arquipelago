#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BANCADA: sem rede — exercita a `regua-alvos-de-portao.py` contra pastas
ENCENADAS e contra a pasta REAL desta ilha.

As duas metades, pelo mesmo desenho do `teste-classes-da-bancada.py`:

  1. **A FIACAO**, em mundos encenados: que a regua siga o nome do alvo por
     variavel, parametro, chave de dicionario, `or` de valor padrao e juncao de
     caminho — e que ela ACHE o ato cujo nome e CONSTRUIDO e nao existe no
     texto, que e o buraco inteiro do item 7.
  2. **A CONTA**, na pasta real de hoje: zero ato invisivel, e nenhuma CARGA
     por resolver. Carga sempre nomeia um arquivo so; carga que nao resolve e
     exatamente onde um alvo invisivel se esconderia.

O QUE ESTE PORTAO NAO AFIRMA, e esta escrito para nao ser lido como cobertura:
o numero de `indiretos()` e de `nao_resolvidos()` e IMPRESSO e nao e cobrado.
Cobrar o numero seria a lista digitada que o achado 4(c) de 20/10 ja pegou uma
vez nesta familia: `conferir-` novo e honesto faria o portao reprovar, e o
proximo trabalhador teria de se lembrar de alimentar a conta.
"""

import importlib.util
import os
import sys

PASTA = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "regua_alvos_de_portao", os.path.join(PASTA, "regua-alvos-de-portao.py")
)
R = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(R)

falhas = []
afirmacoes = 0


def afirmar(condicao, frase):
    global afirmacoes
    afirmacoes += 1
    if not condicao:
        falhas.append(frase)


def mundo(corpo, extras=None):
    """Uma pasta encenada: quem age mais os irmaos que ela precisa ter."""
    arquivos = {'teste-quem-age.py': corpo}
    for nome in (extras or ['regua-alvo.py']):
        arquivos[nome] = '# irmao encenado\n'
    return arquivos


def atos_de(corpo, extras=None):
    return [(r[2], r[3], r[4], r[5]) for r in R.atos(mundo(corpo, extras))]


# ---------------------------------------------------------------------------
# METADE 1 — A FIACAO
# ---------------------------------------------------------------------------
def metade_da_fiacao():
    print('\n1. A FIACAO — a regua segue o nome ate o literal, ou acusa que nao ha literal')

    # (a) O caso simples: o nome esta no proprio sitio do ato.
    a = atos_de("import importlib.util, os\n"
                "importlib.util.spec_from_file_location('x', os.path.join(P, 'regua-alvo.py'))\n")
    afirmar(a == [('carrega', 'regua-alvo.py', R.LITERAL, True)],
            'carga com o nome no sitio e literal e visivel: %r' % (a,))

    # (b) Por variavel: a regua segue a atribuicao, e a posicao CAI para indireto.
    a = atos_de("import importlib.util, os\n"
                "CAMINHO = os.path.join(P, 'regua-alvo.py')\n"
                "importlib.util.spec_from_file_location('x', CAMINHO)\n")
    afirmar(a == [('carrega', 'regua-alvo.py', R.INDIRETO, True)],
            'carga por variavel e indireta, e continua visivel: %r' % (a,))

    # (c) Por parametro, seguido ate o sitio de chamada — o idioma `carregar(nome)`
    #     que esta pasta usa em sete arquivos.
    a = atos_de("import importlib.util, os\n"
                "def carregar(nome):\n"
                "    importlib.util.spec_from_file_location('x', os.path.join(P, nome))\n"
                "carregar('regua-alvo.py')\n")
    afirmar(a == [('carrega', 'regua-alvo.py', R.INDIRETO, True)],
            'carga por parametro chega ao literal do sitio de chamada: %r' % (a,))

    # (d) Por valor padrao atras de um `or` — o idioma do `teste-teto-do-titulo.py`.
    a = atos_de("import importlib.util, os\n"
                "def carregar(caminho=None):\n"
                "    caminho = caminho or os.path.join(P, 'regua-alvo.py')\n"
                "    importlib.util.spec_from_file_location('x', caminho)\n")
    afirmar(a == [('carrega', 'regua-alvo.py', R.INDIRETO, True)],
            'carga com valor padrao atras de `or` resolve: %r' % (a,))

    # (e) Por chave de dicionario — o idioma do `teste-dimensao-imagem.py`.
    a = atos_de("import subprocess, os\n"
                "PAGINAS = {'vazao': 'regua-alvo.py'}\n"
                "subprocess.run(['python3', os.path.join(P, PAGINAS['vazao'])])\n")
    afirmar(a == [('invoca', 'regua-alvo.py', R.INDIRETO, True)],
            'invocacao por chave de dicionario resolve: %r' % (a,))

    # (f) Por pathlib, que e juncao e NAO indirecao: o nome esta ali.
    a = atos_de("import subprocess\n"
                "from pathlib import Path\n"
                "subprocess.run(['python3', str(base / 'ferramentas/regua-alvo.py')])\n")
    afirmar(a == [('invoca', 'regua-alvo.py', R.LITERAL, True)],
            'pathlib com o nome dentro da string e literal: %r' % (a,))

    # (g) O BURACO DO ITEM 7, e e o unico mundo em que a regua tem de REPROVAR
    #     alguma coisa: o nome sai de concatenacao e NAO existe no texto.
    corpo = ("import importlib.util, os\n"
             "PREFIXO = 'regua-'\n"
             "importlib.util.spec_from_file_location('x', os.path.join(P, PREFIXO + 'alvo' + '.py'))\n")
    a = atos_de(corpo)
    afirmar(a == [('carrega', 'regua-alvo.py', R.CONSTRUIDO, False)],
            'nome montado por concatenacao e CONSTRUIDO e INVISIVEL: %r' % (a,))
    afirmar(len(R.invisiveis(mundo(corpo))) == 1,
            'o ato de nome montado entra em invisiveis()')
    afirmar(R.indiretos(mundo(corpo)) == [],
            'ato invisivel NAO e contado como indireto — as duas contas nao se somam')

    # (h) Construido mas VISIVEL: o nome sai de concatenacao e por acaso esta
    #     escrito em outro lugar do arquivo. Nao e buraco, e nao pode entrar em
    #     invisiveis() — se entrasse, a conta de hoje nao seria zero.
    corpo = ("import importlib.util, os\n"
             "# a regua de verdade e a regua-alvo.py, citada aqui\n"
             "importlib.util.spec_from_file_location('x', os.path.join(P, 'regua-' + 'alvo.py'))\n")
    a = atos_de(corpo)
    afirmar(a == [('carrega', 'regua-alvo.py', R.CONSTRUIDO, True)],
            'nome montado que existe no texto e construido e VISIVEL: %r' % (a,))
    afirmar(R.invisiveis(mundo(corpo)) == [],
            'construido visivel nao e invisivel')

    # (i) f-string: a regua rebaixa para CONSTRUIDO porque o nome FINAL sai de
    #     um molde com buraco, e ela nao executa molde nenhum. O rebaixamento e
    #     pessimista de proposito — quem decide se ha buraco de verdade e a
    #     coluna `visivel`, que e medida e nao inferida.
    corpo = ("import importlib.util\n"
             "importlib.util.spec_from_file_location('x', f'{P}/regua-alvo.py')\n")
    a = atos_de(corpo)
    afirmar(a == [('carrega', 'regua-alvo.py', R.CONSTRUIDO, True)],
            'f-string com buraco rebaixa a posicao para construido: %r' % (a,))
    corpo_sem_nome = ("import importlib.util, os\n"
                      "alvo = 'alvo'\n"
                      "importlib.util.spec_from_file_location('x', os.path.join(P, f'regua-{alvo}.py'))\n")
    afirmar(len(R.invisiveis(mundo(corpo_sem_nome))) == 0,
            'f-string cujo nome final a regua nao monta nao inventa ato')
    corpo_pct = ("import importlib.util, os\n"
                 "MOLDE = 'regua-alvo.py'\n"
                 "importlib.util.spec_from_file_location('x', os.path.join(P, MOLDE % 1))\n")
    a = atos_de(corpo_pct)
    afirmar(a and a[0][2] == R.CONSTRUIDO,
            'nome passado por %% e construido: %r' % (a,))

    # (j) `.replace()` produz nome novo — e o idioma que a propria
    #     `regua-classes-da-bancada.py` usa para achar a regua de um `contar-`.
    corpo = ("import importlib.util, os\n"
             "N = 'regua-alvo.py'\n"
             "importlib.util.spec_from_file_location('x', os.path.join(P, N.replace('a', 'b')))\n")
    a = atos_de(corpo)
    afirmar(a and a[0][2] == R.CONSTRUIDO,
            'nome passado por .replace() e construido: %r' % (a,))

    # (k) `open()` de dado NAO e ato sobre irmao, e isto e o que impede o
    #     relatorio de encher de JSON ate ninguem o ler. O mundo poe o proprio
    #     JSON DENTRO da pasta, que e a unica forma de a fronteira ser exercida:
    #     com o arquivo so em `dados/`, rebaixar a fronteira nao mudaria nada e
    #     a mutacao passaria medindo o vazio.
    arquivos = mundo("import os\n"
                     "open(os.path.join(RAIZ, 'dados', 'produtos-filtros.json'))\n")
    arquivos['produtos-filtros.json'] = '{}\n'
    a = [(r[2], r[3]) for r in R.atos(arquivos)]
    afirmar(a == [], 'open() de JSON em dados/ nao e ato sobre irmao: %r' % (a,))
    afirmar([n for n, _ in R.nao_lidos(arquivos)] == [],
            'o .json nem entra na lista de arquivos fora do alcance — ele nao e da conta')

    # (l) `open()` de IRMAO e ato — e o que todo `mutacoes-*` faz com o portao
    #     que mutila.
    a = atos_de("import os\n"
                "open(os.path.join(P, 'regua-alvo.py'), encoding='utf-8')\n")
    afirmar(a == [('abre', 'regua-alvo.py', R.LITERAL, True)],
            'open() de irmao e ato: %r' % (a,))

    # (m) Agir sobre si mesmo nao e ato sobre IRMAO.
    a = atos_de("import os\nopen(os.path.join(P, 'teste-quem-age.py'))\n")
    afirmar(a == [], 'ler o proprio arquivo nao conta como alvo: %r' % (a,))

    # (n) Nome que parece arquivo mas nao esta na pasta: fica de fora, e e por
    #     isso que mundo encenado com nome falso nao polui a conta real.
    a = atos_de("import os\nopen(os.path.join(P, 'regua-que-nao-existe.py'))\n")
    afirmar(a == [], 'alvo fora da pasta nao entra na conta: %r' % (a,))

    # (o) Arquivo que nao parseia nao derruba a regua inteira — ele e DECLARADO
    #     em nao_lidos(), que e o limite escrito em vez de descoberto depois.
    quebrado = {'teste-quebrado.py': 'def (\n', 'regua-alvo.py': '#\n'}
    afirmar(R.atos(quebrado) == [], 'arquivo que nao parseia nao quebra atos()')
    afirmar([n for n, _ in R.nao_lidos(quebrado)] == ['teste-quebrado.py'],
            'arquivo que nao parseia sai nomeado em nao_lidos()')
    mjs = {'teste-coisa.mjs': "import('./regua-alvo.py')\n", 'regua-alvo.py': '#\n'}
    afirmar([n for n, _ in R.nao_lidos(mjs)] == ['teste-coisa.mjs'],
            'o .mjs sai nomeado como fora do alcance, em vez de passar por medido')

    # (p) A carga nao resolvida e o caso perigoso, e sai nomeada.
    nr = R.nao_resolvidos(mundo("import importlib.util\n"
                                "importlib.util.spec_from_file_location('x', vem_de_fora)\n"))
    afirmar(len(nr) == 1 and nr[0][2] == 'carrega',
            'carga com alvo irresolvivel sai em nao_resolvidos(): %r' % (nr,))
    nr = R.nao_resolvidos(mundo("import os\nopen(os.path.join(RAIZ, 'dados', caminho))\n"))
    afirmar(nr == [], 'open() de dado irresolvivel NAO vira ruido no relatorio: %r' % (nr,))


# ---------------------------------------------------------------------------
# METADE 2 — A CONTA NA PASTA REAL
# ---------------------------------------------------------------------------
def metade_da_conta():
    print('\n2. A CONTA — a pasta real desta ilha, hoje')
    arquivos = R.ler_pasta(PASTA)
    todos = R.atos(arquivos)
    inv = R.invisiveis(arquivos)
    ind = R.indiretos(arquivos)
    nr = R.nao_resolvidos(arquivos)
    nl = R.nao_lidos(arquivos)

    por_posicao = {}
    for r in todos:
        por_posicao[r[4]] = por_posicao.get(r[4], 0) + 1
    print('   %d atos sobre irmao: %d literais, %d indiretos, %d construidos'
          % (len(todos), por_posicao.get(R.LITERAL, 0),
             por_posicao.get(R.INDIRETO, 0), por_posicao.get(R.CONSTRUIDO, 0)))
    print('   %d visiveis so por acidente, %d sitios da pasta por resolver, '
          '%d arquivos fora do alcance' % (len(ind), len(nr), len(nl)))

    # A AFIRMACAO COM DENTES, e ela e uma propriedade e nao um numero.
    afirmar(inv == [],
            'nenhum ato desta pasta e invisivel para a varredura por nome: %r'
            % (inv[:5],))
    # Carga que nao resolve e onde um alvo invisivel se esconderia da regua.
    cargas = [x for x in nr if x[2] == 'carrega']
    afirmar(cargas == [],
            'nenhuma CARGA desta pasta ficou por resolver: %r' % (cargas,))
    # A regua tem de estar MEDINDO: pasta real sem ato nenhum seria regua morta
    # passando por regua verde, que e a doenca que a secao 8 chama de inerte.
    afirmar(len(todos) > 100,
            'a regua mede a pasta real de verdade (%d atos)' % len(todos))
    afirmar(any(r[2] == 'carrega' for r in todos)
            and any(r[2] == 'invoca' for r in todos)
            and any(r[2] == 'abre' for r in todos),
            'os tres atos aparecem na pasta real — nenhum ramo esta morto')


# ---------------------------------------------------------------------------
# METADE 3 — A REGUA E UMA SO
# ---------------------------------------------------------------------------
def metade_da_regua_unica():
    print('\n3. A REGUA E UMA SO — ninguem recopia a resolucao de nome')
    with open(os.path.join(PASTA, 'teste-alvos-de-portao.py'), encoding='utf-8') as f:
        meu = f.read()
    afirmar('regua-alvos-de-portao.py' in meu,
            'este portao CARREGA a regua pelo nome, e por isso ela nao e denunciada')
    afirmar('\ndef resolver(' not in meu and '\n    def resolver(' not in meu,
            'este portao NAO tem uma resolver() propria')
    with open(os.path.join(PASTA, 'regua-alvos-de-portao.py'), encoding='utf-8') as f:
        regua = f.read()
    afirmar('import ast' in regua,
            'a regua le a ARVORE e nao o texto — e o que a separa da varredura por nome')
    afirmar('LIMITE' in regua or 'limite' in regua,
            'a regua escreve o limite dela no proprio arquivo')


def main():
    print('ALVOS DE PORTAO — como cada arquivo de ferramentas/ nomeia o irmao em que age')
    print('=' * 78)
    metade_da_fiacao()
    metade_da_conta()
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
