#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BANCADA: sem rede — exercita a `regua-classes-da-bancada.py` contra pastas
ENCENADAS e contra a pasta REAL desta ilha.

Ele mede as duas metades que o achado do item 6(c) de 19/10/2026 juntou:

  1. **A CONTA**, no mundo real de hoje: quantos arquivos em cada classe, e
     quantos estao na classe errada pela leitura cega. A resposta de hoje e
     ZERO na classe errada, e esta afirmada aqui para deixar de ser recontagem
     a mao — que e a assinatura de instrumento sem portao (`contar-` de 14 a
     19/10).
  2. **A FIACAO**, nos mundos encenados: que a regua le a POSICAO de cada marca
     e nao a presenca dela. Conta certa com fiacao errada foi exatamente como o
     defeito de 19/10 nasceu, entao os dois lados sao cobrados.

E cobra uma terceira coisa, que nenhum dos dois lados ve: que a regua CEGA
guardada no arquivo seja de fato diferente da boa. Portao que encena mundo em
que as duas concordam prova que a regua funciona e nao prova que o conserto
mudou alguma coisa.

O MUNDO QUE IMPORTA MAIS e o caso 3: um `conferir-*` que carrega
`BANCADA: sem rede` como DADO, sem o declarar. A leitura cega o le como
declarado e o manda rodar as cegas na passada padrao; esta regua o manda para a
classe de rede, onde ele aparece nomeado. E o unico dos tres buracos que erra
para o lado perigoso, e hoje ninguem entra por ele — a regra esta escrita antes.
"""

import importlib.util
import os
import re
import sys

PASTA = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "regua_classes_da_bancada", os.path.join(PASTA, "regua-classes-da-bancada.py")
)
R = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(R)

_spec_teto = importlib.util.spec_from_file_location(
    "regua_teto_do_titulo", os.path.join(PASTA, "regua-teto-do-titulo.py")
)
_TETO = importlib.util.module_from_spec(_spec_teto)
_spec_teto.loader.exec_module(_TETO)

falhas = []
afirmacoes = 0


def afirmar(condicao, frase):
    global afirmacoes
    afirmacoes += 1
    if not condicao:
        falhas.append(frase)


def categoria(nome, arquivos):
    return R.classificar(nome, arquivos)[1]


def categoria_cega(nome, arquivos):
    return R.classificar_cega(nome, arquivos)[1]


# ---------------------------------------------------------------------------
# METADE 1 — A FIACAO, EM MUNDOS QUE NAO EXISTEM NO DISCO
# ---------------------------------------------------------------------------
def metade_da_fiacao():
    # CASO 1 — marca do navegador em PROSA. O comentario que explica a marca
    # mandou o portao novo de 19/10 para o Chromium duas vezes.
    so_prosa = {
        'mutacoes-algo.py': (
            '# este portao NAO dirige navegador; quem dirige e o\n'
            '# teste-navegador-c15-vitrine.mjs, citado aqui para explicar a diferenca\n'  # ENCENACAO
            'print("ok")\n'
        ),
    }
    afirmar(categoria('mutacoes-algo.py', so_prosa) == 'sem_rede',
            'marca do navegador citada SO em comentario nao manda o portao para o Chromium')
    afirmar(categoria_cega('mutacoes-algo.py', so_prosa) == 'navegador',
            'a leitura cega manda esse mesmo portao para o Chromium (senao o conserto nao muda nada)')
    afirmar(len(R.divergencias(so_prosa)) == 1,
            'a divergencia entre as duas leituras aparece contada nesse mundo')

    # CASO 2 — invocacao de verdade, que mora DENTRO DE ASPAS. E o mundo dos
    # dois `mutacoes-*-vitrine.py` reais, e o conserto literal o quebraria.
    invoca = {
        'mutacoes-c9-vitrine.py': (
            'import subprocess\n'
            'r = subprocess.run(["node", "ferramentas/teste-navegador-c9-vitrine.mjs", html])\n'  # ENCENACAO
        ),
    }
    afirmar(categoria('mutacoes-c9-vitrine.py', invoca) == 'navegador',
            'invocacao do .mjs entre aspas (posicao `dado`) CONTINUA sendo classe de navegador')
    afirmar(R.posicoes(invoca['mutacoes-c9-vitrine.py'], R.MARCA_NAVEGADOR, regex=True) == {'dado'},
            'a `onde()` chama essa invocacao de `dado`, e e por isso que `dado` vale como ato')

    # CASO 2b — importar o proprio playwright, em posicao de codigo.
    pw = {'teste-x.py': 'from playwright.sync_api import sync_playwright\n'}  # ENCENACAO
    afirmar(categoria('teste-x.py', pw) == 'navegador',
            'importar playwright em posicao de codigo e classe de navegador')  # ENCENACAO

    # CASO 3 — O BURACO PERIGOSO. Um `conferir-` que carrega o marcador como
    # DADO sem o declarar: a leitura cega o poe na passada padrao, rodando as
    # cegas contra um site que ele abre.
    encena = {
        'conferir-coisa.py': (
            '"""Este confere o site de verdade, e abre rede."""\n'
            'MARCA = "BANCADA: sem rede"   # encenacao: o marcador como dado\n'
        ),
    }
    afirmar(categoria('conferir-coisa.py', encena) == 'no_ar',
            'marcador carregado como DADO nao declara nada: o conferir- fica na classe de rede')
    afirmar(categoria_cega('conferir-coisa.py', encena) == 'sem_rede',
            'a leitura cega o poria na passada padrao, rodando as cegas — o lado perigoso do erro')

    # CASO 4 — a declaracao de verdade, em PROSA no cabecalho. Aqui a `onde()`
    # se inverte, e os seis `conferir-*` reais dependem disto.
    declara = {
        'conferir-slugs.py': '"""BANCADA: sem rede — este confere o REPOSITORIO, nao o site."""\n',
    }
    afirmar(categoria('conferir-slugs.py', declara) == 'sem_rede',
            'declaracao em prosa no cabecalho tira o conferir- da classe de rede')
    afirmar(R.posicoes(declara['conferir-slugs.py'], R.MARCA_SEM_REDE) == {'prosa'},
            'a `onde()` chama a declaracao de `prosa`, e e por isso que aqui `prosa` e o ato')
    afirmar('//' and categoria('conferir-entidades.mjs',
                               {'conferir-entidades.mjs': '// BANCADA: sem rede — confere o repositorio\n'}) == 'sem_rede',
            'a declaracao vale igual em .mjs, com marcador de comentario de JavaScript')

    # CASO 5 — declaracao ENTERRADA depois do cabecalho nao declara. Arquivo que
    # cita o marcador na linha 900 esta falando SOBRE a convencao.
    enterrada = {
        'conferir-outra.py': '"""Confere o site."""\n' + ('# enchimento\n' * 900) + '# BANCADA: sem rede\n',
    }
    afirmar(len(enterrada['conferir-outra.py']) > R.CABECALHO,
            'o mundo da declaracao enterrada e de fato maior que o cabecalho')
    afirmar(categoria('conferir-outra.py', enterrada) == 'no_ar',
            'declaracao fora do cabecalho nao declara')

    # CASO 6 — regua citada SO em prosa por um portao. Era carga pela leitura
    # cega, e regua que nenhum portao roda e regua que ninguem roda.
    prosa_de_regua = {
        'regua-nova.py': 'def medir():\n    return 1\n',
        'teste-algo.py': '# o criterio e o mesmo da regua-nova.py, mas este portao nao a carrega\nprint("ok")\n',
    }
    afirmar(categoria('regua-nova.py', prosa_de_regua) == 'sem_convencao',
            'regua citada so em comentario fica DENUNCIADA')
    afirmar(categoria_cega('regua-nova.py', prosa_de_regua) == 'producao',
            'a leitura cega a daria por exercitada — o segundo buraco')

    # CASO 7 — carga de verdade, no idioma desta pasta: o nome entre aspas
    # dentro do `spec_from_file_location`. As dez reguas reais dependem disto.
    carga = {
        'regua-nova.py': 'def medir():\n    return 1\n',
        'teste-algo.py': '_spec = importlib.util.spec_from_file_location("r", "regua-nova.py")\n',
    }
    afirmar(categoria('regua-nova.py', carga) == 'producao',
            'carga pelo nome entre aspas (posicao `dado`) exercita a regua')

    # CASO 8 — a regra de 19/10 que NAO se afrouxa: quem carrega tem de ser
    # PORTAO. Producao citando a regua nao a protege.
    so_producao = {
        'regua-nova.py': 'def medir():\n    return 1\n',
        'gerar-coisa.py': '_spec = importlib.util.spec_from_file_location("r", "regua-nova.py")\n',
    }
    afirmar(categoria('regua-nova.py', so_producao) == 'sem_convencao',
            'regua carregada so por PRODUCAO continua denunciada (regra de 19/10, nao afrouxada)')

    # CASO 9 — `contar-` escapa pela regua dele, e so se um portao a carregar.
    contar_ok = {
        'contar-coisa.py': 'print(1)\n',
        'regua-coisa.py': 'def medir():\n    return 1\n',
        'teste-coisa.py': '_spec = importlib.util.spec_from_file_location("r", "regua-coisa.py")\n',
    }
    afirmar(categoria('contar-coisa.py', contar_ok) == 'producao',
            'contar- escapa da denuncia quando um portao carrega a regua dele')
    contar_prosa = {
        'contar-coisa.py': 'print(1)\n',
        'regua-coisa.py': 'def medir():\n    return 1\n',
        'teste-coisa.py': '# usa a regua-coisa.py e o contar-coisa.py, diz o comentario\nprint("ok")\n',
    }
    afirmar(categoria('contar-coisa.py', contar_prosa) == 'sem_convencao',
            'contar- citado so em prosa, com a regua dele tambem so em prosa, fica denunciado')

    # CASO 10 — as convencoes que nao mudaram de 19/10 para ca.
    convencoes = {
        'gerar-catalogo.py': 'x\n', 'teste-navegador-x.mjs': 'x\n', 'teste-x.php': 'x\n',  # ENCENACAO
        'teste-x.mjs': 'x\n', 'validar-x.py': 'x\n', 'testar-x.py': 'x\n',
        'conferir-x.php': 'x\n', 'leiame.txt': 'x\n', 'bancada.py': 'x\n',
    }
    afirmar(categoria('gerar-catalogo.py', convencoes) == 'producao', 'gerar- e producao')
    afirmar(categoria('bancada.py', convencoes) == 'producao', 'a propria bancada e producao')
    afirmar(categoria('teste-navegador-x.mjs', convencoes) == 'navegador', 'teste-navegador-*.mjs e navegador')  # ENCENACAO
    afirmar(categoria('teste-x.php', convencoes) == 'sem_rede', 'teste-*.php e sem rede')
    afirmar(categoria('teste-x.mjs', convencoes) == 'sem_rede', 'teste-*.mjs e sem rede')
    afirmar(categoria('validar-x.py', convencoes) == 'sem_rede', 'validar-*.py e sem rede')
    afirmar(categoria('testar-x.py', convencoes) == 'sem_rede', 'testar-*.py e sem rede')
    afirmar(categoria('conferir-x.php', convencoes) == 'sem_convencao', 'conferir- em .php nao tem convencao')
    afirmar(categoria('leiame.txt', convencoes) == 'ignorado', 'arquivo que nao e codigo e ignorado')

    # CASO 11 — o comando, que a bancada executa. Classe certa com comando
    # errado nao roda nada.
    cmd, _ = R.classificar('conferir-slugs.py', declara)
    afirmar(cmd == ['python3', os.path.join('ferramentas', 'conferir-slugs.py')],
            'conferir- em .py roda sem o argumento `.` (o conferir-protecao-funcoes.py trata argumento como arquivo)')
    cmd, _ = R.classificar('conferir-entidades.mjs', {'conferir-entidades.mjs': '// BANCADA: sem rede\n'})
    afirmar(cmd == ['node', os.path.join('ferramentas', 'conferir-entidades.mjs'), '.'],
            'conferir- em .mjs roda com o argumento `.`')

    # CASO 12 — A `onde()` E IMPORTADA, NAO RECOPIADA. Duas copias da mesma
    # classificacao erram juntas, e o item 6(a) de 19/10 consertou uma delas num
    # lugar so porque havia um lugar so.
    #
    # A IDENTIDADE DE OBJETO NAO SERVE, e este portao mediu isso em si mesmo na
    # primeira passada: cada `spec_from_file_location` cria um MODULO NOVO, e
    # `R.onde is _TETO.onde` reprovava uma regua que esta certa. O que decide e
    # de qual ARQUIVO o codigo da funcao veio.
    afirmar(os.path.basename(R.onde.__code__.co_filename) == 'regua-teto-do-titulo.py',
            'o codigo da `onde()` desta regua vem do arquivo regua-teto-do-titulo.py')
    afirmar('def onde(' not in open(os.path.join(PASTA, 'regua-classes-da-bancada.py'),
                                    encoding='utf-8').read(),
            'a regua das classes NAO define uma `onde()` propria: ela importa')

    # CASO 12b — O MARCADOR DE ENCENACAO VALE POR LINHA, NAO POR ARQUIVO. Se
    # valesse por arquivo, um portao que encenasse um mundo num canto ficaria
    # cego para a invocacao de verdade no outro — e a exencao viraria a lista de
    # exencao que ela existe para nao ser.
    misto = {
        'mutacoes-misto.py': (
            'ENCENADO = "node ferramentas/teste-navegador-x.mjs"   # ' + R.MARCADOR_DE_ENCENACAO + '\n'  # ENCENACAO
            'import subprocess\n'
            'subprocess.run(["node", "ferramentas/teste-navegador-real.mjs"])\n'  # ENCENACAO
        ),
    }
    afirmar(categoria('mutacoes-misto.py', misto) == 'navegador',
            'declarar encenacao numa linha nao cega a regua para a invocacao de verdade noutra')

    # CASO 13 — a aspa ESCAPADA, que foi o acerto do item 6(a). Se a `onde()`
    # regredir, esta regua regride com ela, e e aqui que isso aparece.
    escapada = {
        'mutacoes-algo.py': 'd = varrer("x = \\"teste-navegador-c15-vitrine.mjs\\"\\n")\n',  # ENCENACAO
    }
    afirmar('codigo' not in R.posicoes(escapada['mutacoes-algo.py'], R.MARCA_NAVEGADOR, regex=True),
            'aspa escapada nao abre string: a marca dentro dela nao e lida como codigo')


# ---------------------------------------------------------------------------
# METADE 2 — A CONTA, NA PASTA REAL DESTA ILHA
# ---------------------------------------------------------------------------
def metade_da_conta():
    arquivos = R.ler_pasta()
    afirmar(len(arquivos) > 100, 'a pasta real foi lida (mais de 100 arquivos)')

    # A CONTA DO ITEM 6(c), E ELA MUDOU ENQUANTO ESTE PORTAO ERA ESCRITO
    # -----------------------------------------------------------------------
    # A varredura da pasta de 19/10 deu ZERO: nenhum portao estava na classe
    # errada, e o defeito da leitura cega era INTEIRAMENTE latente. Ele deixou
    # de ser latente no instante em que alguem escreveu um portao que ENCENA a
    # marca — ou seja, no instante em que este arquivo nasceu. A leitura cega
    # manda este portao para o Chromium, onde ele nunca rodaria na passada
    # padrao; a regua o deixa onde ele e.
    #
    # Entao a afirmacao nao e "a divergencia e zero". E mais forte: **a
    # divergencia e EXATAMENTE o conjunto dos arquivos que se declaram
    # encenacao**, e em cada um deles quem acerta e esta regua.
    # A conta nao se afirma por uma lista de nomes: afirma-se pela CAUSA. Todo
    # arquivo em que as duas leituras discordam tem de discordar porque declara
    # encenacao NA LINHA DA MARCA — qualquer outra causa e defeito. (A palavra
    # `ENCENACAO` aparece em prosa noutros arquivos desta pasta, e nao e isso
    # que conta: o marcador so vale na linha em que a marca esta.)
    div = R.divergencias(arquivos)
    afirmar(div != [],
            'a divergencia NAO e vazia: a leitura cega erraria pelo menos um arquivo desta pasta hoje')
    for nome, cega, boa in div:
        afirmar(cega == 'navegador' and boa == 'sem_rede',
                '%s: a leitura cega o manda ao Chromium (cega=%s) e a regua o mantem na passada padrao (regua=%s)'
                % (nome, cega, boa))
        afirmar(R.posicoes(arquivos[nome], R.MARCA_NAVEGADOR, regex=True) - R.NAO_SAO_ATO == set(),
                '%s diverge porque a marca so aparece nele em posicao que NAO e ato (%s)'
                % (nome, sorted(R.posicoes(arquivos[nome], R.MARCA_NAVEGADOR, regex=True))))

    # E A PROVA DE QUE O MARCADOR CARREGA PESO, nao de que ele afrouxa a regua:
    # tirando as declaracoes do texto deste proprio portao, a regua volta a
    # manda-lo para o Chromium. Se ela nao voltasse, o marcador seria enfeite e
    # a classificacao estaria vindo de outro lugar.
    eu = 'teste-classes-da-bancada.py'
    sem_marcador = dict(arquivos)
    sem_marcador[eu] = arquivos[eu].replace('# ' + R.MARCADOR_DE_ENCENACAO, '')
    afirmar(R.classificar(eu, arquivos)[1] == 'sem_rede',
            'com as declaracoes, este portao roda na passada padrao')
    afirmar(R.classificar(eu, sem_marcador)[1] == 'navegador',
            'sem as declaracoes, a regua manda este portao para o Chromium — o marcador carrega peso')

    por_classe = {}
    for nome in sorted(arquivos):
        _, cat = R.classificar(nome, arquivos)
        por_classe.setdefault(cat, []).append(nome)

    # A PROPRIEDADE, E NAO A LISTA DE NOMES — e esta linha e um conserto contra
    # mim mesmo, pego pelo mundo B das mutacoes na primeira passada
    # ------------------------------------------------------------------------
    # A primeira versao afirmava `nav_py == ['mutacoes-c12-vitrine.py',
    # 'mutacoes-c15-regulagem.py']` e `len(sem_rede_conferir) == 6`, com um
    # comentario dizendo que isso "nao e lista digitada, e a medicao de hoje com
    # nome proprio". Era lista digitada: um `conferir-` novo e honesto fazia o
    # portao reprovar, e o proximo trabalhador teria de se LEMBRAR de alimentar o
    # numero — que e exatamente a doenca que a `bancada.py` inteira existe para
    # curar, e a quarta lista dessa familia que esta ilha acha.
    #
    # O que se afirma e a PROPRIEDADE de cada membro da classe. A contagem
    # continua sendo impressa, como registro, e nao cobrada.
    nav_py = sorted(n for n in por_classe.get('navegador', []) if n.endswith('.py'))
    afirmar(nav_py != [], 'a classe de navegador tem membro em .py: %s' % nav_py)
    for n in nav_py:
        afirmar(R.posicoes(arquivos[n], R.MARCA_NAVEGADOR, regex=True) - R.NAO_SAO_ATO,
                '%s esta na classe de navegador porque INVOCA o .mjs em posicao de ato' % n)

    # Os `conferir-` que se declaram sem rede, e a declaracao de cada um esta em
    # prosa no cabecalho. ESTA e a afirmacao que impede rodar as cegas, e ela
    # vale para quantos existirem.
    sem_rede_conferir = sorted(n for n in por_classe.get('sem_rede', []) if n.startswith('conferir-'))
    afirmar(sem_rede_conferir != [],
            'ha conferir- na passada padrao, e cada um se declara: %s' % sem_rede_conferir)
    for n in sem_rede_conferir:
        afirmar('prosa' in R.posicoes(arquivos[n][:R.CABECALHO], R.MARCA_SEM_REDE),
                '%s declara `BANCADA: sem rede` em prosa, no cabecalho' % n)

    # E os que NAO se declaram abrem o site, e ficam fora da passada padrao.
    for n in sorted(por_classe.get('no_ar', [])):
        afirmar(not R.declara_sem_rede(arquivos[n]),
                '%s esta na classe de rede porque nao se declara sem rede' % n)

    # Toda regua e todo contador desta pasta esta carregado por um PORTAO, em
    # posicao de ato. Esta afirmacao e a que impede regua orfa de nascer.
    alvos = sorted(n for n in arquivos
                   if (n.startswith('regua-') or n.startswith('contar-')) and n.endswith('.py'))
    afirmar(len(alvos) >= 11, 'a pasta tem as reguas e contadores esperados: %d' % len(alvos))
    for n in alvos:
        afirmar(R.exercitada_por_portao(n, arquivos),
                '%s e carregada por algum portao desta pasta, em posicao de ato' % n)

    # A lista de denunciados, que tem de estar VAZIA. Portao ou regua que
    # ninguem roda e o defeito que a bancada inteira existe para pegar.
    afirmar(por_classe.get('sem_convencao', []) == [],
            'a lista de SEM CONVENCAO esta vazia: %s' % por_classe.get('sem_convencao', []))

    # E o total da passada padrao, que e o numero que vai para o REGISTRO.md.
    print('  pasta real: %d arquivos — %s'
          % (len(arquivos),
             ', '.join('%s %d' % (c, len(por_classe[c])) for c in sorted(por_classe))))
    print('  na classe errada pela leitura cega: %d (%s)'
          % (len(div), ', '.join(n for n, _, _ in div) or 'nenhum'))


# ---------------------------------------------------------------------------
# METADE 3 — A REGUA E UMA SO, E ISSO SE PROVA LENDO OS ARQUIVOS
# ---------------------------------------------------------------------------
# Cobrado pela secao 8 do ARQUIPELAGO.md, no paragrafo de 16/10/2026: *"o
# portao que cobra regua unica LE OS ARQUIVOS: cada consumidor tem de carregar
# a regua compartilhada e NENHUM pode redefinir a conta — em qualquer
# indentacao, porque copia aninhada e copia"*, porque *"comportamento igual no
# dado de hoje nao e prova de regua unica; e a ausencia de contraexemplo
# confundida com prova"*.
#
# E e exatamente o caso aqui: as duas leituras dao a MESMA resposta em todos os
# 94 arquivos que ja existiam nesta pasta — medido, um a um. Se a `bancada.py`
# voltasse a ter a propria copia das tres perguntas, nenhuma afirmacao sobre
# comportamento acusaria, porque o dado de hoje nao separa as copias.
def metade_da_regua_unica():
    consumidores = ['bancada.py']
    for nome in consumidores:
        texto = open(os.path.join(PASTA, nome), encoding='utf-8').read()
        afirmar('regua-classes-da-bancada.py' in texto,
                '%s CARREGA a regua compartilhada pelo nome' % nome)
        # `\s*def` cobre qualquer indentacao: copia aninhada e copia.
        for funcao in ('dirige_navegador', 'declara_sem_rede', 'exercitada_por_portao',
                       'regua_exercitada', 'posicoes', 'e_ato_de_codigo', 'e_ato_de_prosa'):
            afirmar(re.search(r'^\s*def\s+%s\s*\(' % funcao, texto, re.M) is None,
                    '%s NAO redefine %s(), em nenhuma indentacao' % (nome, funcao))
        # E as marcas, que sao o outro jeito de a copia voltar: regex igual com
        # nome igual, decidindo por conta propria.
        for marca in ('MARCA_NAVEGADOR', 'MARCA_SEM_REDE', 'NAO_E_PORTAO', 'E_PORTAO'):
            afirmar(re.search(r'^\s*%s\s*=' % marca, texto, re.M) is None,
                    '%s NAO redefine a marca %s' % (nome, marca))
        # A `classificar()` dele existe, e tem de DELEGAR. Funcao com o nome
        # certo e corpo proprio e a copia mais facil de nao ver.
        m = re.search(r'^def classificar\(.*?\n((?:    .*\n|\n)*)', texto, re.M)
        afirmar(m is not None, '%s tem uma classificar()' % nome)
        if m:
            afirmar('CLASSES.classificar(' in m.group(1),
                    'a classificar() do %s delega para a regua, e nao decide nada' % nome)


def main():
    print('A REGUA DAS CLASSES DA BANCADA — fiacao em mundo encenado e conta na pasta real')
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
