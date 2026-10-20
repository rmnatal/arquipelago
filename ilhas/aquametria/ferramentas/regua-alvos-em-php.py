#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGUA COMPARTILHADA: como cada arquivo `.php` de `ferramentas/` NOMEIA o
irmao em que ele age — literal no sitio do ato, literal alcancado por variavel,
ou nome CONSTRUIDO que pode nao existir no texto.

Nao afirma nada sozinha e nao abre rede. Quem a exercita e o
`teste-alvos-em-php.py`; quem a mutila e o `mutacoes-alvos-em-php.py`.

POR QUE ESTE ARQUIVO EXISTE, e a data e 20/10/2026
---------------------------------------------------
O item 7 do fecho de 20/10/2026 (13h18Z) deixou a pergunta escrita em vez de a
responder: *"o `.mjs` e o `.php` desta pasta carregam e invocam irmaos, e
NINGUEM os mediu. Quem a tomar responde primeiro quantos atos existem la, antes
de propor regua nenhuma."*

A `regua-alvos-de-portao.py` le a ARVORE SINTATICA do Python e escreve, no
proprio cabecalho, que os 40 arquivos `.mjs` e `.php` desta pasta estao **fora
do alcance dela** — e eles tambem agem sobre irmaos. Esta regua fecha a metade
do PHP, que e a maior das duas e a que tem o ato mais repetido da pasta: NOVE
arquivos carregam o `render-para-teste.php`.

QUEM LE PHP E O PHP, e isso ja era idioma desta pasta
------------------------------------------------------
O `proteger-funcoes.php` usa `token_get_all()` desde 09/09/2026. Entao a leitura
nao e varredura de texto: o `listar-atos-php.php` devolve a SEQUENCIA DE
OPERANDOS que o tokenizador da propria linguagem ve em cada sitio de ato, e esta
regua decide a posicao a partir dela. Varredura de texto nao distingue string de
comentario de codigo — e foi exatamente esse o defeito que a
`regua-classes-da-bancada.py` pagou em 20/10 de manha.

A DIVISAO DE TRABALHO, e ela e o que permite encenar pasta que nao existe:
o PHP recebe ARQUIVO e devolve TOKEN; esta regua recebe `{nome: texto}` e nao
sabe de disco nenhum. O `_com_pasta_no_disco()` grava os textos numa pasta
temporaria FORA de `ferramentas/`, para que nenhum mundo encenado seja
descoberto pela `bancada.py`.

O ATO, E SO ESTES TRES CONTAM — os mesmos tres da regua irma
-------------------------------------------------------------
  * **carrega**: `require`, `require_once`, `include`, `include_once`, `eval`.
    O `eval( file_get_contents( X ) )` desta pasta e CARGA e nao leitura, e o
    `file_get_contents` de dentro dele nao conta duas vezes.
  * **invoca**: `exec`, `shell_exec`, `system`, `passthru`, `proc_open`, `popen`.
  * **abre**: `file_get_contents`, `file`, `fopen`, `readfile`.

Leitura de JSON em `dados/` e de `.md` em `conteudo/` nao e ato sobre irmao e
nao entra, pelo mesmo motivo que na regua irma: alvo que nao e arquivo desta
pasta e descartado, e sitio que nao resolveu so e cobrado quando FALA da pasta.

A POSICAO DO `.` E MEDIDA POR OPERANDO, NAO PELA DOBRA — e a diferenca com a
regua irma e deliberada
----------------------------------------------------------------------------
A regua irma rebaixa toda concatenacao `+` a CONSTRUIDO e preserva o literal
dentro de `os.path.join()`, e escreve a causa: *"chamadas que so COMPOEM
caminho: atravessa-las nao e indirecao, porque o nome continua escrito ali
dentro"*. O PHP **nao tem** chamada de composicao de caminho: o `.` e a unica
que a linguagem oferece, e `__DIR__ . '/render-para-teste.php'` escreve o nome
ali, do mesmo jeito que o `join` do Python. Entao a regra aqui e a CAUSA e nao a
letra: operando literal cujo ultimo degrau e nome de irmao vale LITERAL; nome
que so aparece COLANDO operandos adjacentes vale CONSTRUIDO.

E a diferenca nao e teorica, esta medida: pela letra, **12 dos 12** atos desta
metade sairiam como `construido` e a coluna de posicao nao discriminaria NADA —
que e exatamente o defeito que a leva 8 da C12 mediu numa regua de catalogo e
deixou escrito no T8 ("a regua da C15 nao discrimina nada numa ferramenta em que
o produto nao e eliminado pela entrada").

O QUE TEM DENTES E O QUE E REGISTRO
------------------------------------
`invisiveis()` e a propriedade que o portao cobra e tem de continuar vazia:
ato sobre irmao cujo nome NAO esta escrito no texto de quem age fica invisivel
para os tres classificadores da `regua-classes-da-bancada.py` de uma vez.
`indiretos()` e registro — mede quanto da visibilidade de hoje e acidente.

A CONTA DE 20/10/2026, medida por esta regua na pasta desta ilha
-----------------------------------------------------------------
**12 atos sobre irmao em 21 arquivos `.php`: 12 literais, 0 indiretos, 0
construidos, e ZERO invisiveis.** Os 12 sao `carrega` e os 12 tem o MESMO alvo.
Nenhum sitio falou da pasta sem resolver. Dois sitios ficaram de fora por
medicao e nao por limite: o `exec( ... __FILE__ ... )` do
`teste-atualizador-sync.php`, que e ato sobre SI MESMO, e o
`file_get_contents( $argv[1] )` do `proteger-funcoes.php`, cujo alvo vem da
linha de comando e nao da pasta.

Os numeros sao de uma DATA e envelhecem com a pasta; quem quiser o de hoje roda
`python3 ferramentas/regua-alvos-em-php.py`, que os imprime. O que o portao
cobra nao e nenhum deles: e a propriedade de `invisiveis()` continuar vazia, que
nao envelhece.

O LIMITE, escrito em vez de descoberto depois
----------------------------------------------
  * **So le PHP.** Os 20 `.mjs` desta pasta continuam fora de alcance, e eles
    tambem agem sobre irmaos — **9 atos, medidos em 20/10/2026**, com o numero e
    a lista em `dados/atos-sobre-irmao-2026-10-20.md`. O motivo de nao haver
    portao sobre eles esta escrito la e e nomeado: o unico analisador de
    JavaScript deste ambiente e AMBIENTE (`/opt/node-tools`), nao esta declarado
    no `package.json` e nem resolve por `import` — so por `createRequire` com
    caminho absoluto. Portao que fica vermelho onde a dependencia nao existe e
    pior que portao nenhum. O que o `teste-alvos-em-php.py` cobra no lugar e a
    **cobertura declarada**: todo arquivo desta pasta ou e lido por uma das duas
    reguas, ou aparece nomeado num limite. Isso nao mede o `.mjs`, mas impede que
    uma linguagem NOVA entre na pasta sem ninguem notar — que e como estes 40
    arquivos ficaram sem medicao por um mes.
  * **`.php` que o tokenizador nao le sai em `nao_lidos()`**, nunca aprovado em
    silencio. Para esta metade isso e FALHA e nao limite: o `php` e exigido pela
    classe sem rede da `bancada.py`, entao `.php` ilegivel aqui e defeito.
  * **Resolucao parcial e declarada.** Sitio cujo alvo esta fora do alcance da
    dobra sai em `nao_resolvidos()` com o texto da expressao, do mesmo jeito que
    a 20.4 manda registrar o item que rolou para fora da janela do log.
"""

import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEITOR = os.path.join(RAIZ, 'ferramentas', 'listar-atos-php.php')

# O VOCABULARIO NAO E COPIADO, E ISSO CUSTOU UM DEFEITO PARA SER APRENDIDO
# ---------------------------------------------------------------------------
# A primeira versao deste arquivo trazia a propria COPIA de `_base()`, das tres
# posicoes e das duas comparacoes de forca — 30 linhas iguais as da regua irma.
# A copia nasceu errada no mesmo dia: `_base('*.php')` devolvia `*.php` como se
# fosse nome de arquivo, entao a carga por `glob` — idioma real desta pasta —
# saia da lista do que NAO RESOLVEU sem entrar na conta dos atos. Desaparecia
# das duas listas de uma vez, que e a pior coisa que uma regua pode fazer.
#
# Quem o achou foi o PORTAO, na primeira passada, no mundo encenado do
# `foreach ( glob( __DIR__ . '/*.php' ) as $f ) { require $f; }`. E o defeito
# nao era desta copia: era da funcao ORIGINAL, onde dormia escondido por
# aritmetica — `*.py` tem 4 caracteres e o `> 4` o barrava, `*.php` tem 5 e
# passava. Foi consertado la, no arquivo que o possui, e o efeito esta medido: a
# conta da metade do Python NAO muda em um unico numero com o conserto (196
# atos, 0 invisiveis, 148 por acidente, 10 por resolver nas duas leituras),
# porque os dois `glob` de `snippets/*.php` daquela metade nao falam de
# `ferramentas/`. **O defeito estava dormindo no Python e acordado no PHP**,
# onde `__DIR__` E a pasta.
#
# A licao e a que a `bancada.py` ja escreve sobre a regua de `noindex`: regra
# escrita duas vezes erra de um lado so. Entao esta regua IMPORTA o vocabulario
# da irma em vez de o repetir, e o conserto de um vale para as duas para sempre.
_spec = importlib.util.spec_from_file_location(
    'regua_alvos_de_portao', os.path.join(RAIZ, 'ferramentas', 'regua-alvos-de-portao.py'))
IRMA = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(IRMA)

EXTENSOES = IRMA.EXTENSOES
LITERAL = IRMA.LITERAL
INDIRETO = IRMA.INDIRETO
CONSTRUIDO = IRMA.CONSTRUIDO
_base = IRMA._base
_mais_forte = IRMA._mais_forte
_mais_fraca = IRMA._mais_fraca
# O `_rebaixar` continua morando aqui, e nao e copia: na regua irma ele e um
# `@staticmethod` da classe `Arquivo`, que esta regua nao instancia. A regra que
# importa — qual posicao e mais fraca — vem da irma no `_mais_fraca` acima.


def _rebaixar(achados, posicao):
    return {nome: _mais_fraca(pos, posicao) for nome, pos in (achados or {}).items()}


# ---------------------------------------------------------------------------
# O LEITOR: o tokenizador do proprio PHP, chamado uma vez por arquivo
# ---------------------------------------------------------------------------
def _com_pasta_no_disco(arquivos):
    """Grava `{nome: texto}` numa pasta temporaria FORA de `ferramentas/`.

    Mundo encenado nao pode morar na pasta de verdade: a `bancada.py` varre
    `ferramentas/` e descobriria o arquivo encenado como portao novo."""
    pasta = tempfile.mkdtemp(prefix='aqm-alvos-php-')
    for nome, texto in arquivos.items():
        with open(os.path.join(pasta, nome), 'w', encoding='utf-8') as f:
            f.write(texto or '')
    return pasta


def ler(arquivos):
    """-> ({nome: {'atos': [...], 'atribuicoes': {...}}}, [(nome, motivo)]).

    O segundo valor sao os `.php` que o tokenizador NAO leu, com o motivo. Nunca
    aprova em silencio: arquivo ausente da primeira metade esta na segunda."""
    if not os.path.isfile(LEITOR):
        return {}, [(n, 'leitor ausente: ferramentas/listar-atos-php.php')
                    for n in sorted(arquivos) if n.endswith('.php')]
    pasta = _com_pasta_no_disco(arquivos)
    lidos, falhos = {}, []
    try:
        for nome in sorted(arquivos):
            if not nome.endswith('.php'):
                continue
            try:
                saida = subprocess.run(
                    ['php', LEITOR, os.path.join(pasta, nome)],
                    capture_output=True, text=True, timeout=120)
            except (OSError, subprocess.SubprocessError) as e:
                falhos.append((nome, 'php nao rodou: %s' % e))
                continue
            if saida.returncode != 0:
                falhos.append((nome, 'php saiu %d: %s'
                               % (saida.returncode, (saida.stderr or '').strip()[:120])))
                continue
            try:
                lidos[nome] = json.loads(saida.stdout)
            except ValueError as e:
                falhos.append((nome, 'saida nao e JSON: %s' % e))
    finally:
        shutil.rmtree(pasta, ignore_errors=True)
    return lidos, falhos


# ---------------------------------------------------------------------------
# A RESOLUCAO DE UM NOME, a partir da sequencia de operandos
# ---------------------------------------------------------------------------
def _dobras(operandos):
    """As colagens de operandos literais ADJACENTES, com 2 ou mais pedacos.

    E aqui que vive o caso com dentes: `'reg' . 'ua.py'` monta um nome que
    NENHUM operando carrega e que pode nao estar escrito no arquivo."""
    fora = []
    corrida = []
    for op in operandos:
        if op.get('k') == 'str':
            corrida.append(op.get('v') or '')
            continue
        if len(corrida) > 1:
            fora.append(''.join(corrida))
        corrida = []
    if len(corrida) > 1:
        fora.append(''.join(corrida))
    return fora


def _nomes_por_variavel(atribuicoes):
    """{variavel: {nome_de_arquivo: posicao}} por PONTO FIXO, nunca por recursao.

    A primeira versao desta regua resolvia variavel por recursao com teto de
    profundidade, e a recursao ESTOUROU na pasta de verdade: 20 arquivos, cada
    variavel atribuida varias vezes e cada atribuicao citando outras, da uma
    arvore que cresce em exponencial e nao termina em tempo util. Medido em
    20/10/2026 — o processo passou de dois minutos de CPU sem imprimir nada.

    Ponto fixo e monotono: o conjunto de nomes de cada variavel so cresce, e a
    varredura para quando nenhuma rodada acrescenta nada. Teto de rodadas igual
    ao numero de variaveis, que e o maximo de passos que uma cadeia pode ter."""
    tabela = {v: {} for v in atribuicoes}
    for _ in range(len(atribuicoes) + 1):
        mudou = False
        for var, listas in atribuicoes.items():
            achados = dict(tabela[var])
            for operandos in listas:
                for op in operandos or []:
                    if op.get('k') == 'str':
                        b = _base(op.get('v'))
                        if b:
                            achados[b] = _mais_forte(achados.get(b), LITERAL)
                    elif op.get('k') == 'var' and op.get('v') != var:
                        for alvo, pos in tabela.get(op.get('v'), {}).items():
                            achados[alvo] = _mais_forte(achados.get(alvo), pos)
                for junto in _dobras(operandos or []):
                    b = _base(junto)
                    if b and b not in achados:
                        achados[b] = CONSTRUIDO
            if achados != tabela[var]:
                tabela[var] = achados
                mudou = True
        if not mudou:
            break
    # Nome alcancado ATRAVES de variavel nunca e literal no sitio do ato.
    return {v: _rebaixar(a, INDIRETO) for v, a in tabela.items()}


def _resolver(operandos, atribuicoes, por_variavel=None):
    """-> {nome_de_arquivo: posicao}. Posicao e a MAIS FORTE encontrada."""
    if por_variavel is None:
        por_variavel = _nomes_por_variavel(atribuicoes)
    achados = {}
    for op in operandos or []:
        k = op.get('k')
        if k == 'str':
            b = _base(op.get('v'))
            if b:
                achados[b] = _mais_forte(achados.get(b), LITERAL)
        elif k == 'var':
            for alvo, pos in por_variavel.get(op.get('v'), {}).items():
                achados[alvo] = _mais_forte(achados.get(alvo), pos)
    for junto in _dobras(operandos or []):
        b = _base(junto)
        if b and b not in achados:
            achados[b] = CONSTRUIDO
    return achados


def _tem_buraco(operandos):
    return any(op.get('k') == 'buraco' for op in operandos or [])


def _fala_da_pasta(operandos, atribuicoes=None, vistos=frozenset()):
    """A expressao fala de `ferramentas/`, mesmo sem nomear arquivo nenhum?

    `__DIR__` num arquivo desta pasta E a pasta, e e por isso que ele conta.
    Sem esta pergunta, um `file_get_contents` de JSON em `dados/` e um de irmao
    seriam a mesma coisa para quem conta o que ficou sem resolver — e o
    relatorio encheria de ruido ate ninguem o ler.

    E ELA SEGUE VARIAVEL, pelo mesmo motivo que a `aponta_para_a_pasta()` da
    regua irma segue: no idioma de quem varre a pasta — `foreach ( glob(
    __DIR__ . '/*.php' ) as $f ) { require $f; }` — o `__DIR__` esta na
    ATRIBUICAO e o sitio do ato so tem `$f`. Perguntando apenas no sitio, a
    carga mais perigosa desta pasta responderia "nao fala da pasta".
    """
    atribuicoes = atribuicoes or {}
    for op in operandos or []:
        k = op.get('k')
        if k == 'dir':
            return True
        if k == 'str' and 'ferramentas' in (op.get('v') or ''):
            return True
        if k == 'var' and op.get('v') not in vistos:
            nome = op.get('v')
            for valores in atribuicoes.get(nome, []):
                if _fala_da_pasta(valores, atribuicoes, vistos | {nome}):
                    return True
    return False


def _proprio(operandos):
    """O ato e sobre SI MESMO? `__FILE__` e como o `teste-atualizador-sync.php`
    se re-invoca, e ato sobre si nao e ato sobre irmao."""
    return any(op.get('k') == 'file' for op in operandos or [])


# ---------------------------------------------------------------------------
# A LEITURA DE UMA PASTA INTEIRA
# ---------------------------------------------------------------------------
def atos(arquivos, lidos=None):
    """[registro] de todo ato sobre irmao, em todo `.php` da pasta.

    registro = (quem, linha, tipo, alvo, posicao, visivel)

    `visivel` e a pergunta que os tres classificadores da
    `regua-classes-da-bancada.py` fazem, e e so esta: o nome do alvo esta
    escrito, como texto, no arquivo de quem age?
    """
    if lidos is None:
        lidos, _ = ler(arquivos)
    irmaos = {n for n in arquivos if n.endswith(EXTENSOES)}
    saida = []
    for quem in sorted(lidos):
        texto = arquivos.get(quem) or ''
        dados = lidos[quem] or {}
        atribuicoes = dados.get('atribuicoes') or {}
        por_variavel = _nomes_por_variavel(atribuicoes)
        for ato in dados.get('atos') or []:
            ops = ato.get('operandos') or []
            for alvo, posicao in sorted(_resolver(ops, atribuicoes, por_variavel).items()):
                if alvo not in irmaos or alvo == quem:
                    continue
                saida.append((quem, ato.get('linha'), ato.get('tipo'),
                              alvo, posicao, alvo in texto))
    return saida


def invisiveis(arquivos, lidos=None):
    """Atos sobre irmao cujo nome NAO esta escrito no arquivo de quem age.

    Deixa de ser `[]` no dia em que alguem montar o nome de um irmao por
    colagem — e ai os tres classificadores ficam cegos para aquele ato de uma
    vez so, que e o que o item 7 nomeou."""
    return [r for r in atos(arquivos, lidos) if not r[5]]


def indiretos(arquivos, lidos=None):
    """Atos que so chegam ao literal por variavel.

    Estes sao VISIVEIS hoje, e e por isso que nao reprovam nada. O numero e
    registro: mede quanto da visibilidade de hoje depende de um literal escrito
    ali por outro motivo."""
    return [r for r in atos(arquivos, lidos) if r[4] != LITERAL and r[5]]


def nao_resolvidos(arquivos, lidos=None):
    """Sitios de ato que falam da pasta e cujo alvo esta regua nao resolveu.

    registro = (quem, linha, tipo, expressao, fala_da_pasta)

    Sao o limite, nao a aprovacao. O ultimo campo e o que separa as duas
    familias, e so a primeira e perigosa: carga que NAO resolve e FALA desta
    pasta pode estar escondendo um irmao; carga que varre OUTRA pasta — o
    `eval( file_get_contents( $arquivo ) )` do `render-para-teste.php` sobre
    `snippets/*.php` — nao pode esconder irmao nenhum, por construcao.
    O portao cobra a primeira familia e imprime a segunda."""
    if lidos is None:
        lidos, _ = ler(arquivos)
    saida = []
    for quem in sorted(lidos):
        dados = lidos[quem] or {}
        atribuicoes = dados.get('atribuicoes') or {}
        por_variavel = _nomes_por_variavel(atribuicoes)
        for ato in dados.get('atos') or []:
            ops = ato.get('operandos') or []
            if _resolver(ops, atribuicoes, por_variavel):
                continue
            if _proprio(ops):
                continue
            if ato.get('tipo') == 'carrega' or _fala_da_pasta(ops, atribuicoes):
                saida.append((quem, ato.get('linha'), ato.get('tipo'),
                              (ato.get('expressao') or '')[:70],
                              _fala_da_pasta(ops, atribuicoes)))
    return saida


def nao_lidos(arquivos, falhos=None):
    """Arquivos da pasta que esta regua NAO le, com o motivo de cada um.

    Sao tres grupos, e nenhum deles e aprovado em silencio: o `.php` que o
    tokenizador recusou (que para esta metade e DEFEITO, nao limite), o `.py`
    que e da regua irma, e tudo o mais — `.mjs` hoje, e qualquer linguagem que
    entre nesta pasta amanha.

    O terceiro grupo e o que da dentes ao portao: estes 40 arquivos ficaram um
    mes sem medicao porque NADA os nomeava. Enquanto `nao_lidos()` nomear todo
    arquivo que nenhuma das duas reguas le, linguagem nova na pasta aparece no
    dia em que chega."""
    if falhos is None:
        _, falhos = ler(arquivos)
    saida = [(n, m) for n, m in falhos]
    recusados = {n for n, _ in falhos}
    for nome in sorted(arquivos):
        if nome in recusados:
            continue
        if nome.endswith('.php'):
            continue                      # lido por esta regua
        if nome.endswith('.py'):
            continue                      # dominio da regua-alvos-de-portao.py
        ext = os.path.splitext(nome)[1] or '(sem extensao)'
        saida.append((nome, 'nao e PHP: %s' % ext))
    return sorted(saida)


def ler_pasta(pasta=None):
    pasta = pasta or os.path.join(RAIZ, 'ferramentas')
    saida = {}
    for nome in sorted(os.listdir(pasta)):
        if nome.startswith('.'):
            continue
        try:
            with open(os.path.join(pasta, nome), encoding='utf-8', errors='replace') as f:
                saida[nome] = f.read()
        except OSError:
            continue
    return saida


if __name__ == '__main__':
    arquivos = ler_pasta()
    lidos, falhos = ler(arquivos)
    todos = atos(arquivos, lidos)
    inv = invisiveis(arquivos, lidos)
    ind = indiretos(arquivos, lidos)
    nr = nao_resolvidos(arquivos, lidos)
    nl = nao_lidos(arquivos, falhos)
    php = sum(1 for n in arquivos if n.endswith('.php'))
    print('ALVOS EM PHP — %d arquivos .php em ferramentas/ (%d lidos), %d atos sobre irmao'
          % (php, len(lidos), len(todos)))
    por_posicao = {}
    for r in todos:
        por_posicao[r[4]] = por_posicao.get(r[4], 0) + 1
    for pos in (LITERAL, INDIRETO, CONSTRUIDO):
        print('  %-12s %d' % (pos, por_posicao.get(pos, 0)))
    por_tipo = {}
    for r in todos:
        por_tipo[r[2]] = por_tipo.get(r[2], 0) + 1
    print('  por ato:    ' + '  '.join('%s %d' % (t, por_tipo.get(t, 0))
                                       for t in ('carrega', 'invoca', 'abre')))
    print('\nATOS INVISIVEIS para a varredura por nome: %d' % len(inv))
    for quem, linha, tipo, alvo, pos, _ in inv:
        print('  %s:%s %s %s (%s)' % (quem, linha, tipo, alvo, pos))
    print('\nVISIVEIS SO POR ACIDENTE (indirecao que termina em literal): %d' % len(ind))
    for quem, linha, tipo, alvo, pos, _ in ind:
        print('  %s:%s %s %s' % (quem, linha, tipo, alvo))
    print('\nTODOS OS ATOS, por quem age:')
    for quem, linha, tipo, alvo, pos, vis in todos:
        print('  %-34s :%-4s %-8s %-34s %-11s %s'
              % (quem, linha, tipo, alvo, pos, 'visivel' if vis else 'INVISIVEL'))
    print('\nSITIOS QUE FALAM DA PASTA E NAO RESOLVERAM: %d' % len(nr))
    for quem, linha, tipo, txt, pasta in nr:
        print('  %s:%s %s %s%s'
              % (quem, linha, tipo, txt, '   [FALA DESTA PASTA]' if pasta else ''))
    print('\nFORA DO ALCANCE DESTA REGUA: %d arquivos (%d .mjs, %d .php recusados)'
          % (len(nl), sum(1 for _, m in nl if m == 'nao e PHP'),
             sum(1 for _, m in nl if m != 'nao e PHP')))
    for nome, motivo in nl:
        if motivo != 'nao e PHP':
            print('  %-40s %s' % (nome, motivo))
    raise SystemExit(0)
