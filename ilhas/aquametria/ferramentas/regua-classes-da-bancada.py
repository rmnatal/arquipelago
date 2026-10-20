#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGUA COMPARTILHADA: decide a CLASSE de cada arquivo de `ferramentas/` —
portao sem rede, portao do ar, portao de navegador, producao ou denunciado.

Nao afirma nada sozinha e nao abre rede. Quem a exercita contra pastas
ENCENADAS e o `teste-classes-da-bancada.py`; quem a mutila e o
`mutacoes-classes-da-bancada.py`. Quem a USA em producao e a `bancada.py`, que
deixou de ter as tres perguntas aqui dentro.

POR QUE ESTE ARQUIVO EXISTE, e a data e 20/10/2026
---------------------------------------------------
O item 6(c) do fecho de 19/10/2026, deixado sem conserto de proposito pela
19.2: *"A bancada mandou o portao novo para a classe de Chromium DUAS vezes, e
a segunda foi o comentario que explicava a primeira: ela classifica pela marca
no TEXTO do arquivo, prosa incluida."* E o proximo passo que aquele fecho
escreveu: *"o conserto certo nao e remendo — a classe deveria sair de 'a linha
MEDE alguma coisa ali?', que e o que a `onde()` ja responde, e quem tomar
COMECA CONTANDO quantos portoes estao hoje na classe errada."*

A CONTAGEM FOI FEITA PRIMEIRO, E ELA VIROU O DESENHO DESTE ARQUIVO
-------------------------------------------------------------------
**A resposta e ZERO: nenhum portao desta pasta esta hoje na classe errada.** Os
dois `mutacoes-*.py` que a bancada manda para o Chromium dirigem o navegador de
verdade, os seis `conferir-*` que se declaram sem rede conferem o repositorio
mesmo, e as onze reguas e contadores estao todos carregados por portao. Zero
medido e nada medido nao valem o mesmo (achado 1 de 19/10), e aqui o zero foi
medido: esta regua imprime a contagem com `--contar`, para ela nunca mais ser
uma recontagem a mao.

**E A CONTAGEM SALVOU O CONSERTO, porque o conserto LITERAL poria 18 na classe
errada.** Ler "a linha MEDE alguma coisa ali?" como "so `codigo` vale" quebra
os tres classificadores ao mesmo tempo, e cada um por um motivo diferente:

  * **2 portoes de navegador** perderiam a classe e passariam a rodar na
    passada padrao, reprovando por FALTA DE PLAYWRIGHT — que e exatamente a
    falha de ambiente lida como defeito da ilha que a marca existe para
    impedir. O nome do `.mjs` que eles invocam mora DENTRO DE ASPAS, porque e
    argumento de `subprocess.run`: a `onde()` o chama de `dado`, e aqui `dado`
    E a medicao.
  * **6 portoes `conferir-*`** perderiam a declaracao `BANCADA: sem rede` e
    sairiam da passada padrao, porque essa declaracao mora no CABECALHO por
    convencao desta pasta — ou seja, em `prosa`, de proposito. Aqui a `onde()`
    se inverte: `prosa` e a unica posicao que declara.
  * **10 reguas e contadores** seriam DENUNCIADOS como "ninguem roda", porque o
    idioma de carga desta pasta e `importlib.util.spec_from_file_location`, que
    carrega o irmao pelo NOME entre aspas — `dado` outra vez.

A REGRA QUE SOBROU, E ELA E MAIS CURTA QUE AS TRES EXCECOES
------------------------------------------------------------
**`prosa` nunca e ato.** O que conta como ato e que muda de classificador para
classificador, e isso nao e inconsistencia: e que os tres perguntam coisas
diferentes.

  * **Invocar** (navegador) e **carregar** (regua exercitada) sao atos de
    CODIGO, e nesta pasta os dois se escrevem com o nome do alvo entre aspas.
    Valem `codigo` e `dado`; `prosa` nao.
  * **Declarar** (`BANCADA: sem rede`) e ato de PROSA, e so dela. Vale `prosa`
    no cabecalho; `codigo` e `dado` nao declaram nada — sao um arquivo
    MANIPULANDO o marcador como texto, que e o que esta regua e os portoes dela
    fazem a pagina inteira.

O BURACO QUE ISTO FECHA E O TERCEIRO, e ele e o unico perigoso dos tres
-----------------------------------------------------------------------
Os dois primeiros erram para o lado seguro: portao que vai para a classe errada
de navegador fica FORA da passada e aparece nomeado em "fora desta passada". O
terceiro erra para o lado que faz esta bancada existir — **um `conferir-*` que
carregasse o marcador como DADO, sem o declarar, era lido como declarado e
passava a rodar as cegas na passada padrao.** Hoje nenhum o faz; o portao desta
regua encena um que faz, porque regra escrita antes de alguem entrar pela porta
custa uma linha e regra escrita depois custa uma leva.

E O MESMO VALE PARA A REGUA NAO EXERCITADA: citacao em comentario passava por
carga, entao uma regua que nenhum portao roda escapava da denuncia. `prosa` nao
carrega nada.

A `onde()` e IMPORTADA do `regua-teto-do-titulo.py` e nao recopiada, pelo mesmo
motivo escrito na `regua-constantes-de-snippet.py`: duas copias da mesma
classificacao erram juntas, e o item 6(a) de 19/10 ja consertou uma delas (a
aspa escapada) num lugar so porque havia um lugar so.

O LIMITE, escrito em vez de descoberto depois
----------------------------------------------
A `onde()` nao e um analisador de sintaxe, e esta regua herda esse limite
inteiro — esta escrito na docstring dela. Em cima dele, dois limites proprios:

  * **A classe sai do TEXTO do arquivo, nao de executa-lo.** Um portao que
    montasse o nome do `.mjs` por concatenacao, ou importasse a regua por uma
    variavel, nao seria visto. E o preco de classificar 135 arquivos sem rodar
    nenhum, e o lado seguro do erro e a denuncia.
  * **`REDIGITO QUE RENOMEIA ESCAPA DE VARREDURA POR NOME`** (achado 5 de
    19/10) vale aqui tambem: quem copiar o `.mjs` para outro nome foge da marca.
    Esta escrito aqui em vez de virar promessa de cobertura que a regua nao tem.
"""

import importlib.util
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# A `onde()` vem do irmao mais velho. Recopia-la seria o defeito que as tres
# reguas desta familia existem para impedir, um andar acima.
_spec = importlib.util.spec_from_file_location(
    "regua_teto_do_titulo",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "regua-teto-do-titulo.py"),
)
_teto = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_teto)
onde = _teto.onde

# AS CONVENCOES DESTA PASTA. Elas vinham da `bancada.py` e passaram para ca sem
# mudar de texto: o que mudou foi quem PERGUNTA a posicao de cada marca.
NAO_E_PORTAO = re.compile(
    r'^(gerar|coletar|medir|aplicar|acentuar|atualizar|cobertura|render|varrer|listar|proteger|bancada)[-.]'
)
E_PORTAO = re.compile(r'^(teste|testar|mutacoes|validar|conferir)-')
MARCA_NAVEGADOR = re.compile(r'teste-navegador-|playwright')
MARCA_SEM_REDE = 'BANCADA: sem rede'

# A MARCA DA ENCENACAO, E ELA NASCEU DE UM ACERTO DESTA REGUA CONTRA O PORTAO
# DELA MESMA, na primeira passada de 20/10/2026
# ---------------------------------------------------------------------------
# O `teste-classes-da-bancada.py` encena mundos em que um portao invoca o
# `.mjs` — ele TEM de conter o padrao, como o `teste-teto-do-titulo.py` tem de
# conter `TETO = 65`. E a encenacao mora dentro de aspas, igual a invocacao de
# verdade: a `onde()` chama as duas de `dado`, porque as duas SAO a mesma coisa
# para quem le posicao. Resultado: a regua mandou o proprio portao dela para a
# classe de Chromium — o mesmo defeito do item 6(c), um andar acima, e a
# terceira vez que um instrumento desta pasta se pegou.
#
# Os tres consertos possiveis, e por que este:
#   * afrouxar o padrao do navegador quebraria os dois portoes reais, que e o
#     dano de 18 que a contagem mediu. Seria trocar a regua pelo resultado.
#   * uma lista de exencao aqui dentro e exatamente a lista escrita a mao que a
#     `bancada.py` inteira existe para acabar.
#   * entao a exencao mora na MESMA LINHA do padrao, que e a regra que a
#     `regua-constantes-de-snippet.py` ja usa com o `REGUA PROPRIA`, e a frase
#     que o `regua-teto-do-titulo.py` escreveu antes das duas:
#     **"Encenacao que se declara encenacao nao e divida."**
#
# O LADO DO ERRO E O SEGURO, e e isso que autoriza a exencao existir: declarar
# `ENCENACAO` num portao que dirige navegador DE VERDADE o joga na passada
# padrao, onde ele reprova por falta de Playwright — alto e na hora. Declarar de
# menos o tira da passada e o imprime nomeado em "fora desta passada". Nenhum
# dos dois lados e silencioso.
MARCADOR_DE_ENCENACAO = 'ENCENACAO'

# A declaracao mora no CABECALHO. O limite em caracteres e o mesmo que a
# `bancada.py` usava em bytes, e esta aqui pelo mesmo motivo: declaracao
# enterrada no meio de mil linhas nao e declaracao, e um arquivo que cita o
# marcador na linha 900 esta falando SOBRE a convencao, nao a usando.
CABECALHO = 4000

EXTENSOES = ('.py', '.mjs', '.php')


# ---------------------------------------------------------------------------
# O ATO: a pergunta que os tres classificadores fazem, cada um com o seu sentido
# ---------------------------------------------------------------------------
def posicoes(texto, alvo, regex=False):
    """Em que posicoes o alvo aparece neste texto: {`codigo`, `prosa`, `dado`}.

    Recebe TEXTO como dado e nao abre arquivo nenhum — quem le o disco e a
    `ler_pasta()`, para o portao poder encenar pasta que nao existe. Quem
    precisa olhar so o cabecalho recorta o texto ANTES de chamar, e nao por um
    parametro aqui: o recorte e decisao de quem pergunta.
    """
    achadas = set()
    for linha in (texto or '').split('\n'):
        encenada = MARCADOR_DE_ENCENACAO in linha
        if regex:
            for m in alvo.finditer(linha):
                achadas.add('encenacao' if encenada else onde(linha, m.group(0)))
        elif alvo in linha:
            achadas.add('encenacao' if encenada else onde(linha, alvo))
    return achadas


# `prosa` nao e ato porque nao mede nada; `encenacao` nao e ato porque o arquivo
# DECLARA que ali esta montando um mundo, e nao agindo nele.
NAO_SAO_ATO = {'prosa', 'encenacao'}


def e_ato_de_codigo(texto, alvo, regex=False):
    """Invocar e carregar: valem `codigo` e `dado`, nunca `prosa` nem encenacao."""
    return bool(posicoes(texto, alvo, regex=regex) - NAO_SAO_ATO)


def e_ato_de_prosa(texto, alvo):
    """Declarar: vale `prosa` no cabecalho, e so ela."""
    return 'prosa' in posicoes((texto or '')[:CABECALHO], alvo)


# ---------------------------------------------------------------------------
# OS TRES CLASSIFICADORES
# ---------------------------------------------------------------------------
def dirige_navegador(texto):
    """O arquivo INVOCA um teste de navegador, ou importa o proprio playwright?

    Comentario que explica a marca nao dirige navegador nenhum — e foi um
    comentario desses que mandou o portao novo de 19/10 para o Chromium duas
    vezes.
    """
    return e_ato_de_codigo(texto, MARCA_NAVEGADOR, regex=True)


def declara_sem_rede(texto):
    """O arquivo DECLARA, no cabecalho, que nao abre o site?

    Sem a declaracao, `conferir-` e tratado como rede e fica fora da passada
    padrao, com o nome impresso. O lado seguro do erro e ficar de fora e
    aparecer, nunca rodar as cegas ou sumir calado — e e por isso que o
    marcador como DADO nao declara: um `conferir-` que o encenasse passaria a
    rodar as cegas.
    """
    return e_ato_de_prosa(texto, MARCA_SEM_REDE)


def exercitada_por_portao(nome, arquivos):
    """Algum PORTAO desta pasta CARREGA este arquivo pelo nome?

    A pergunta e feita aos arquivos, nunca a uma lista aqui dentro. Citacao em
    comentario nao carrega nada: regua que nenhum portao roda e regua que
    ninguem roda, que e a doenca que a `bancada.py` inteira existe para curar.
    """
    for outro in sorted(arquivos):
        if outro == nome or not outro.endswith(EXTENSOES):
            continue
        if not E_PORTAO.match(outro):
            continue
        if e_ato_de_codigo(arquivos[outro], nome):
            return True
    return False


def classificar(nome, arquivos):
    """Devolve (comando, categoria) ou (None, motivo), como a `bancada.py` pede.

    Recebe a pasta inteira como DADO porque duas das perguntas sao sobre os
    OUTROS arquivos, nao sobre este.
    """
    texto = arquivos.get(nome, '')
    if NAO_E_PORTAO.match(nome):
        return None, 'producao'
    if nome.startswith('regua-') and nome.endswith('.py'):
        return (None, 'producao') if exercitada_por_portao(nome, arquivos) else (None, 'sem_convencao')
    # `contar-` responde a mesma pergunta do `regua-`: ele CONTA e nao afirma,
    # mas a contagem dele e numero que a ilha publica sobre si mesma (secao 8),
    # entao so escapa da denuncia se um portao o carregar — ele mesmo ou a
    # regua dele.
    if nome.startswith('contar-') and nome.endswith('.py'):
        regua_dele = nome.replace('contar-', 'regua-', 1)
        exercitado = (exercitada_por_portao(nome, arquivos)
                      or (regua_dele in arquivos and exercitada_por_portao(regua_dele, arquivos)))
        return (None, 'producao') if exercitado else (None, 'sem_convencao')
    if nome.startswith('teste-navegador-') and nome.endswith('.mjs'):
        return ['node', os.path.join('ferramentas', nome), '.'], 'navegador'
    if nome.startswith('conferir-'):
        if not nome.endswith(('.py', '.mjs')):
            return None, 'sem_convencao'
        # O `.` so vai para os .mjs. Os .py desta pasta acham a raiz sozinhos, e
        # um deles — o conferir-protecao-funcoes.py — trata ARGUMENTO COMO
        # ARQUIVO: passar '.' a ele seria pedir que conferisse um diretorio e
        # colher uma falha que nao e da ilha.
        cmd = (['node', os.path.join('ferramentas', nome), '.'] if nome.endswith('.mjs')
               else ['python3', os.path.join('ferramentas', nome)])
        return cmd, 'sem_rede' if declara_sem_rede(texto) else 'no_ar'
    if nome.startswith('teste-') and nome.endswith('.php'):
        return ['php', os.path.join('ferramentas', nome), '.'], 'sem_rede'
    if nome.startswith('teste-') and nome.endswith('.mjs'):
        return ['node', os.path.join('ferramentas', nome), '.'], 'sem_rede'
    if nome.startswith(('teste-', 'testar-', 'mutacoes-', 'validar-')) and nome.endswith('.py'):
        cat = 'navegador' if dirige_navegador(texto) else 'sem_rede'
        return ['python3', os.path.join('ferramentas', nome)], cat
    if nome.endswith(EXTENSOES):
        return None, 'sem_convencao'
    return None, 'ignorado'


# ---------------------------------------------------------------------------
# A REGUA CEGA, GUARDADA DE PROPOSITO: ELA E O QUE SE MEDE CONTRA
# ---------------------------------------------------------------------------
# Esta e a pergunta que a `bancada.py` fazia ate 19/10/2026 — a marca no TEXTO,
# prosa incluida. Ela NAO e usada para classificar nada: existe para a
# `divergencias()` poder contar, com um comando, quantos arquivos as duas
# leituras classificam diferente. Sem ela a contagem do item 6(c) voltaria a
# ser um script de rascunho que ninguem roda duas vezes, que e a assinatura de
# instrumento sem portao.
def classificar_cega(nome, arquivos):
    texto = arquivos.get(nome, '')
    if NAO_E_PORTAO.match(nome):
        return None, 'producao'
    if nome.startswith('regua-') and nome.endswith('.py'):
        return (None, 'producao') if _citada_cega(nome, arquivos) else (None, 'sem_convencao')
    if nome.startswith('contar-') and nome.endswith('.py'):
        regua_dele = nome.replace('contar-', 'regua-', 1)
        exercitado = (_citada_cega(nome, arquivos)
                      or (regua_dele in arquivos and _citada_cega(regua_dele, arquivos)))
        return (None, 'producao') if exercitado else (None, 'sem_convencao')
    if nome.startswith('teste-navegador-') and nome.endswith('.mjs'):
        return ['node', os.path.join('ferramentas', nome), '.'], 'navegador'
    if nome.startswith('conferir-'):
        if not nome.endswith(('.py', '.mjs')):
            return None, 'sem_convencao'
        cmd = (['node', os.path.join('ferramentas', nome), '.'] if nome.endswith('.mjs')
               else ['python3', os.path.join('ferramentas', nome)])
        return cmd, 'sem_rede' if MARCA_SEM_REDE in texto[:CABECALHO] else 'no_ar'
    if nome.startswith('teste-') and nome.endswith('.php'):
        return ['php', os.path.join('ferramentas', nome), '.'], 'sem_rede'
    if nome.startswith('teste-') and nome.endswith('.mjs'):
        return ['node', os.path.join('ferramentas', nome), '.'], 'sem_rede'
    if nome.startswith(('teste-', 'testar-', 'mutacoes-', 'validar-')) and nome.endswith('.py'):
        cat = 'navegador' if MARCA_NAVEGADOR.search(texto) else 'sem_rede'
        return ['python3', os.path.join('ferramentas', nome)], cat
    if nome.endswith(EXTENSOES):
        return None, 'sem_convencao'
    return None, 'ignorado'


def _citada_cega(nome, arquivos):
    for outro in sorted(arquivos):
        if outro == nome or not outro.endswith(EXTENSOES):
            continue
        if not E_PORTAO.match(outro):
            continue
        if nome in arquivos[outro]:
            return True
    return False


def divergencias(arquivos):
    """[(nome, categoria_cega, categoria_desta_regua)] onde as duas discordam.

    DISCORDANCIA NAO E ERRO, E A PRIMEIRA VERSAO DESTA FRASE DIZIA QUE ERA
    (corrigido em 20/10/2026, 14h0xZ, pela execucao seguinte a que a escreveu).
    Ela dizia *"`[]` e a resposta de hoje"* — e era verdade no instante em que
    foi escrita e deixou de ser algumas horas depois, no MESMO dia e na MESMA
    execucao, quando o `MARCADOR_DE_ENCENACAO` nasceu. Desde entao a resposta
    e **2**, e os dois sao os portoes desta propria regua, que encenam a marca
    do navegador e se declaram encenacao. Nos dois, quem acerta e esta regua.

    O que esta lista conta, portanto, e **onde as duas leituras discordam** —
    e cada discordancia e de uma destas duas familias:
      * a leitura cega erra e esta regua acerta (encenacao declarada, hoje 2);
      * esta regua erra, que e o caso que nunca aconteceu e que o
        `teste-classes-da-bancada.py` cobra pela CAUSA, nao pelo numero: todo
        arquivo que diverge tem de divergir porque a marca so aparece nele em
        posicao que nao e ato.
    Chamar isto de "portao na classe errada" era ler a segunda familia no
    numero da primeira, que e o defeito que esta pasta chama de numero errado
    com cara de medido.
    """
    saida = []
    for nome in sorted(arquivos):
        _, cega = classificar_cega(nome, arquivos)
        _, boa = classificar(nome, arquivos)
        if cega != boa:
            saida.append((nome, cega, boa))
    return saida


def ler_pasta(pasta=None):
    """{nome: texto} de todo arquivo de `ferramentas/`. Le o disco; a decisao e
    das funcoes acima, que recebem dado."""
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
    if '--contar' in sys.argv[1:]:
        contas = {}
        for nome in sorted(arquivos):
            _, cat = classificar(nome, arquivos)
            contas[cat] = contas.get(cat, 0) + 1
        print('CLASSES DA BANCADA — %d arquivos em ferramentas/' % len(arquivos))
        for cat in sorted(contas):
            print('  %-14s %d' % (cat, contas[cat]))
        div = divergencias(arquivos)
        print('\nONDE AS DUAS LEITURAS DISCORDAM (a cega inclui prosa): %d' % len(div))
        print('  — discordancia nao e erro: nos de hoje quem acerta e esta regua.')
        for nome, cega, boa in div:
            print('  %-40s cega=%-10s regua=%s' % (nome, cega, boa))
        raise SystemExit(0)
    for nome in sorted(arquivos):
        cmd, cat = classificar(nome, arquivos)
        print('%-42s %-12s %s' % (nome, cat, ' '.join(cmd) if cmd else ''))
