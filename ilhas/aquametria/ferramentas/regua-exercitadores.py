#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGUA COMPARTILHADA: quantos arquivos de `ferramentas/` exercitam cada
funcao desta pasta — e quais funcoes ninguem exercita.

Nao afirma nada sozinha e nao abre rede. Quem a exercita e o
`teste-exercitadores.py`; quem a mutila e o `mutacoes-exercitadores.py`.

POR QUE ESTE ARQUIVO EXISTE, e a data e 20/10/2026
---------------------------------------------------
O item 4 do PROXIMO PASSO do fecho de 20/10/2026 (16h18Z), escrito pela
execucao que acabou de pagar o preco: *"o defeito do `_base` so foi achado
porque um SEGUNDO leitor exercitou a mesma funcao sobre outra linguagem — ele
estava dormindo havia dias com um caller so. Quantas funcoes compartilhadas de
`ferramentas/` tem hoje um unico exercitador? Quem a tomar conta primeiro,
antes de propor conserto nenhum."*

O defeito do `_base` nao era de logica difícil: `*.php` passava pelo teste de
extensao e o sitio DESAPARECIA das duas listas de uma vez. Ele sobreviveu dias
porque havia **um** exercitador, e um exercitador nunca discorda de si mesmo.
Dois leitores sobre a mesma funcao foram o que o acordou.

A PERGUNTA SE PARTE EM DUAS, E A PRIMEIRA E MAIS BARATA QUE A SEGUNDA
----------------------------------------------------------------------
  * **ZERO exercitador** e codigo morto: funcao definida que ninguem alcanca.
    Nao e defeito dormindo, e afirmacao que ninguem pode contradizer — foi
    exatamente o achado 11 do fecho de 20/10, que tirou tres destes dos
    arquivos daquela execucao antes do commit. Isto tem dentes: `orfas()` tem
    de continuar vazia.
  * **UM exercitador** e o defeito dormindo da pergunta. Isto **nao** tem
    dentes e nao pode ter: ajudante privado chamado de um lugar so e desenho
    correto na maior parte dos casos, e cobrar o numero transformaria a regua
    na lista digitada que esta pasta ja pegou tres vezes. O numero e REGISTRO,
    e serve para escolher onde por o segundo leitor.

O QUE CONTA COMO EXERCICIO, E SAO TRES FORMAS — NAO UMA
--------------------------------------------------------
Este e o buraco que a pergunta nao via, e ele foi medido antes de esta regua
nascer: uma varredura que conte so `nome(...)` acha **82 funcoes orfas** nesta
pasta e as 82 sao FALSAS. As `c_e1` ... `c_e28` do
`testar-validador-especies.py` nao sao chamadas em lugar nenhum — elas entram
numa tupla de casos e quem as chama e o laco, pela referencia. O mesmo vale
para as mutacoes do `mutacoes-purga-cache.py` e do `mutacoes-c15-regulagem.py`.

  * **chamada**: `nome(...)` ou `M.nome(...)`, o sitio obvio.
  * **referencia**: o nome usado como VALOR — passado como argumento, posto
    numa tupla de casos, atribuido, usado como decorador. E o idioma de toda
    bancada desta pasta, e e exercicio tanto quanto a chamada.
  * **por_nome**: o nome como TEXTO, em `getattr`, `globals()[...]` ou numa
    string qualquer. E a forma mais fraca e a mais perigosa, pela mesma razao
    que a `regua-alvos-de-portao.py` separa `indireto` de `literal`: quem a usa
    some de toda varredura no dia em que o literal for reescrito.

`orfas()` exige a ausencia das TRES. Ela erra de proposito para o lado de nao
acusar: string solta igual ao nome de uma funcao e prova fraca, e prova fraca
nao basta para chamar codigo de morto, mas basta para nao o acusar.

A ATRIBUICAO QUANDO O NOME EXISTE EM DOIS ARQUIVOS, E ELA E DECLARADA
----------------------------------------------------------------------
Nesta pasta **425 das 807** definicoes de topo tem nome que existe em outro
arquivo tambem (`main`, `afirmar`, `mundo`, `rodar_teste`). Um exercicio no
arquivo C nao pertence a nenhuma delas por adivinhacao. A regra:

  * o sitio esta no PROPRIO arquivo que define -> e dele;
  * o sitio esta num arquivo que CARREGA o que define -> e dele, e o grafo de
    carga vem da `regua-alvos-de-portao.py`, que ja o mede;
  * nenhuma das duas, com o nome definido em dois ou mais arquivos -> vai para
    `ambiguos()` e **nao e atribuido a ninguem**.

E por isso que `orfas()` conta o exercicio ANTES da atribuicao: funcao com
sitio ambiguo nao e orfa, porque alguem a exercita — so nao se sabe de que
arquivo. Chamar de morta o que nao se conseguiu atribuir seria a regua
confundindo o limite dela com um defeito da pasta.

O LIMITE, escrito em vez de descoberto depois
----------------------------------------------
  * **So le PYTHON**, como a irma. Os 21 `.php` e os 20 `.mjs` desta pasta
    tem funcao e tem exercitador, e esta regua nao os le. A metade do PHP tem
    leitor proprio (`regua-alvos-em-php.py`) para OUTRA pergunta, nao para
    esta; a do `.mjs` segue sem analisador declarado nesta ilha.
  * **So funcao de TOPO.** Metodo de classe e funcao de dentro de funcao nao
    entram: o `_base` da pergunta era de topo, e metodo chamado por `self.x()`
    pediria resolucao de tipo, que e executar o codigo.
  * **O exercicio e contado por ARQUIVO, nunca por sitio.** Dez chamadas no
    mesmo arquivo continuam sendo UM exercitador — o que acordou o `_base` foi
    o segundo ARQUIVO, nao a decima chamada.
  * **A pasta e dado.** Quem le o disco e `ler_pasta()`, importada da irma;
    tudo o mais recebe `{nome: texto}`, para o portao poder encenar pasta que
    nao existe.
"""

import ast
import importlib.util
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA = os.path.join(RAIZ, 'ferramentas')


def _irma():
    """A `regua-alvos-de-portao.py`, IMPORTADA e nunca copiada.

    O fecho de 20/10/2026 pagou para aprender isto: a `regua-alvos-em-php.py`
    nasceu com uma COPIA do `_base()` da irma e a copia nasceu com o defeito
    que a irma tinha. O conserto nao foi arrumar as duas — foi apagar a copia.
    Aqui se importa o vocabulario de pasta (`ler_pasta`, `EXTENSOES`) e o grafo
    de carga (`atos`), e a mutacao que mata o `EXTENSOES` da irma prova que
    esta importacao esta viva."""
    spec = importlib.util.spec_from_file_location(
        'regua_alvos_de_portao', os.path.join(PASTA, 'regua-alvos-de-portao.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# As tres formas de exercicio, da mais forte para a mais fraca.
CHAMADA = 'chamada'
REFERENCIA = 'referencia'
POR_NOME = 'por_nome'

_FORCA = {CHAMADA: 3, REFERENCIA: 2, POR_NOME: 1}

# Nomes que o proprio Python exercita por fora de todo sitio: quem os define
# nao precisa de chamador escrito em arquivo nenhum.
PROTOCOLO = ('main', '__init__', '__repr__', '__str__', '__enter__', '__exit__')


def ler_pasta(pasta=None):
    """Delegada a irma de proposito — pasta e vocabulario dela."""
    return _irma().ler_pasta(pasta or PASTA)


def _arvore(texto):
    try:
        return ast.parse(texto or '')
    except SyntaxError:
        return None


def definicoes(arquivos):
    """[(arquivo, nome, linha)] de toda funcao de TOPO em `.py` da pasta."""
    saida = []
    for quem in sorted(arquivos):
        if not quem.endswith('.py'):
            continue
        arv = _arvore(arquivos[quem])
        if arv is None:
            continue
        for no in arv.body:
            if isinstance(no, (ast.FunctionDef, ast.AsyncFunctionDef)):
                saida.append((quem, no.name, no.lineno))
    return saida


def _sitios_de_um(texto, nomes):
    """[(linha, nome, forma)] de todo sitio que exercita um dos `nomes`.

    O `def` de uma funcao NAO e sitio dela; o nome dela escrito no corpo de
    outra, sim — chamada recursiva inclusive, e e por isso que o arquivo que
    define costuma ser o primeiro exercitador."""
    arv = _arvore(texto)
    if arv is None:
        return []
    saida = []
    funcs_de_chamada = set()
    for no in ast.walk(arv):
        if isinstance(no, ast.Call):
            funcs_de_chamada.add(id(no.func))
    for no in ast.walk(arv):
        if isinstance(no, (ast.FunctionDef, ast.AsyncFunctionDef)):
            # O cabecalho da propria definicao nao exercita nada. Os filhos do
            # no continuam visitados pelo `walk`, entao decorador e corpo
            # seguem contando.
            continue
        if isinstance(no, ast.Name) and isinstance(no.ctx, ast.Load):
            if no.id in nomes:
                forma = CHAMADA if id(no) in funcs_de_chamada else REFERENCIA
                saida.append((no.lineno, no.id, forma))
        elif isinstance(no, ast.Attribute) and isinstance(no.ctx, ast.Load):
            if no.attr in nomes:
                forma = CHAMADA if id(no) in funcs_de_chamada else REFERENCIA
                saida.append((no.lineno, no.attr, forma))
        elif isinstance(no, ast.Constant) and isinstance(no.value, str):
            if no.value in nomes:
                saida.append((no.lineno, no.value, POR_NOME))
    return saida


def exercicios(arquivos):
    """[(quem_exercita, linha, nome, forma)] em toda a pasta."""
    nomes = {n for _, n, _ in definicoes(arquivos)}
    if not nomes:
        return []
    saida = []
    for quem in sorted(arquivos):
        if not quem.endswith('.py'):
            continue
        for linha, nome, forma in _sitios_de_um(arquivos[quem], nomes):
            saida.append((quem, linha, nome, forma))
    return saida


def carga(arquivos):
    """{arquivo: {irmao que ele carrega}} — medido pela regua irma, nao aqui."""
    R = _irma()
    saida = {}
    for quem, _linha, tipo, alvo, _pos, _vis in R.atos(arquivos):
        if tipo == 'carrega':
            saida.setdefault(quem, set()).add(alvo)
    return saida


def _por_nome(arquivos):
    mapa = {}
    for arq, nome, _linha in definicoes(arquivos):
        mapa.setdefault(nome, set()).add(arq)
    return mapa


def exercitadores(arquivos):
    """{(arquivo, nome): {arquivo que a exercita}}, pela regra de atribuicao.

    Chave e a DEFINICAO, nunca o nome solto: duas funcoes homonimas em dois
    arquivos sao duas funcoes, e somar os exercitadores delas e o jeito mais
    rapido de uma orfa se esconder atras da homonima movimentada da irma."""
    onde = _por_nome(arquivos)
    cargas = carga(arquivos)
    saida = {(arq, nome): set() for arq, nome, _l in definicoes(arquivos)}
    for quem, _linha, nome, _forma in exercicios(arquivos):
        donos = onde.get(nome, set())
        if quem in donos:
            saida[(quem, nome)].add(quem)
            continue
        carregados = donos & cargas.get(quem, set())
        if carregados:
            for d in carregados:
                saida[(d, nome)].add(quem)
        elif len(donos) == 1:
            saida[(next(iter(donos)), nome)].add(quem)
    return saida


def ambiguos(arquivos):
    """[(quem, linha, nome, [arquivos que definem])] que nao se atribuiu.

    Limite declarado, nao defeito da pasta: o sitio existe e exercita alguma
    das homonimas. Por isso ele conta em `orfas()` e nao conta em
    `exercitadores()` — acusar de morta uma funcao que esta regua nao
    conseguiu atribuir seria confundir o limite dela com um achado."""
    onde = _por_nome(arquivos)
    cargas = carga(arquivos)
    saida = []
    for quem, linha, nome, _forma in exercicios(arquivos):
        donos = onde.get(nome, set())
        if quem in donos or len(donos) < 2:
            continue
        if donos & cargas.get(quem, set()):
            continue
        saida.append((quem, linha, nome, sorted(donos)))
    return saida


def orfas(arquivos):
    """[(arquivo, nome, linha)] de funcao sem UM sitio de exercicio na pasta.

    Esta e a lista com dentes, e a propriedade dela nao envelhece: funcao
    definida que nenhum sitio desta pasta alcanca, por chamada, por referencia
    ou por nome, e codigo morto. O achado 11 do fecho de 20/10/2026 tirou tres
    destas antes do commit; o portao existe para a quarta nao esperar dias.

    Conta o sitio ANTES da atribuicao, de proposito: um sitio que exercita
    `main` sem que se saiba qual `main` ainda e um sitio, e nenhuma das
    homonimas e morta por causa dele."""
    tocados = {nome for _quem, _linha, nome, _forma in exercicios(arquivos)}
    return [(arq, nome, linha) for arq, nome, linha in definicoes(arquivos)
            if nome not in tocados and nome not in PROTOCOLO]


def contagem(arquivos):
    """{(arquivo, nome): quantos arquivos distintos a exercitam}."""
    return {k: len(v) for k, v in exercitadores(arquivos).items()}


def compartilhadas(arquivos):
    """[(arquivo, nome)] de funcao de topo definida num arquivo que ALGUM
    irmao carrega — as reguas da pasta, e so elas.

    E a fronteira da pergunta do item 4: funcao de dentro de um portao so
    pertence a ele, e nao ha segundo leitor possivel. Funcao de regua tem um
    segundo leitor possivel hoje, e a conta diz quantas ainda nao o tem."""
    cargas = carga(arquivos)
    carregados = set()
    for alvos in cargas.values():
        carregados |= alvos
    return [(arq, nome) for arq, nome, _l in definicoes(arquivos)
            if arq in carregados]


def dormindo(arquivos):
    """[(arquivo, nome, o_unico)] de funcao COMPARTILHADA com um exercitador so.

    E a resposta da pergunta, e e REGISTRO e nao reprovacao. O que ela mede: em
    quantas funcoes de regua desta pasta um defeito teria hoje um unico leitor
    para o contradizer — que foi a condicao exata em que o `_base` dormiu."""
    conta = exercitadores(arquivos)
    saida = []
    for arq, nome in sorted(set(compartilhadas(arquivos))):
        quem = conta.get((arq, nome), set())
        if len(quem) == 1:
            saida.append((arq, nome, next(iter(quem))))
    return saida


def so_o_proprio(arquivos):
    """[(arquivo, nome)] de funcao compartilhada cujo UNICO exercitador e o
    arquivo que a define.

    E o subconjunto de `dormindo()` que mais se parece com o `_base`: a funcao
    esta num arquivo que irmaos carregam, logo ela e alcancavel de fora, e
    ninguem de fora a alcanca. Irmao nenhum a contradiz porque irmao nenhum a
    toca."""
    return [(arq, nome) for arq, nome, unico in dormindo(arquivos) if unico == arq]


def nao_lidos(arquivos):
    """Arquivos da pasta que esta regua NAO le. Limite calado vira cobertura
    imaginada — a frase e da irma e a razao e a mesma."""
    saida = []
    for nome in sorted(arquivos):
        if not nome.endswith(_irma().EXTENSOES):
            continue
        if not nome.endswith('.py'):
            saida.append((nome, 'nao e Python'))
            continue
        if _arvore(arquivos[nome]) is None:
            saida.append((nome, 'nao parseia'))
    return saida


if __name__ == '__main__':
    arquivos = ler_pasta()
    defs = definicoes(arquivos)
    ex = exercicios(arquivos)
    comp = sorted(set(compartilhadas(arquivos)))
    conta = contagem(arquivos)
    orf = orfas(arquivos)
    dorm = dormindo(arquivos)
    proprio = so_o_proprio(arquivos)
    amb = ambiguos(arquivos)
    nl = nao_lidos(arquivos)

    print('EXERCITADORES — %d arquivos em ferramentas/, %d funcoes de topo em %d .py'
          % (len(arquivos), len(defs), sum(1 for n in arquivos if n.endswith('.py'))))
    por_forma = {}
    for _q, _l, _n, forma in ex:
        por_forma[forma] = por_forma.get(forma, 0) + 1
    print('  sitios de exercicio: %d' % len(ex))
    for forma in (CHAMADA, REFERENCIA, POR_NOME):
        print('    %-12s %d' % (forma, por_forma.get(forma, 0)))

    print('\nFUNCOES ORFAS (nenhum sitio, em nenhuma das tres formas): %d' % len(orf))
    for arq, nome, linha in orf:
        print('  %s:%d  %s' % (arq, linha, nome))

    print('\nCOMPARTILHADAS (de arquivo que algum irmao carrega): %d' % len(comp))
    faixas = {1: 0, 2: 0, 3: 0}
    for chave in comp:
        n = conta.get(chave, 0)
        faixas[1 if n <= 1 else (2 if n == 2 else 3)] += 1
    print('  com 1 exercitador: %d   com 2: %d   com 3 ou mais: %d'
          % (faixas[1], faixas[2], faixas[3]))

    print('\nA RESPOSTA DO ITEM 4 — compartilhadas com UM exercitador so: %d' % len(dorm))
    for arq, nome, unico in dorm:
        marca = '  (so o proprio)' if unico == arq else ''
        print('  %-34s %-28s <- %s%s' % (arq, nome, unico, marca))
    print('\n  dessas, sem NENHUM leitor de fora: %d' % len(proprio))

    print('\nSITIOS NAO ATRIBUIDOS (nome definido em 2+ arquivos): %d' % len(amb))
    nomes_amb = sorted({n for _q, _l, n, _d in amb})
    print('  em %d nomes: %s' % (len(nomes_amb), ', '.join(nomes_amb[:12])
                                 + (' ...' if len(nomes_amb) > 12 else '')))

    print('\nFORA DO ALCANCE DESTA REGUA: %d arquivos' % len(nl))
    raise SystemExit(0)
