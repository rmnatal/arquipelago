#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Roda a BANCADA INTEIRA desta ilha com um comando so, e DESCOBRE os portoes
em vez de os listar.

    python3 ferramentas/bancada.py              # so o que roda sem rede
    python3 ferramentas/bancada.py --no-ar      # inclui os que abrem o site
    python3 ferramentas/bancada.py --navegador  # inclui os de Chromium (dezenas de minutos)
    python3 ferramentas/bancada.py --lista      # so imprime o que rodaria, sem rodar
    python3 ferramentas/bancada.py --provar     # mede a propria regua do veredito

POR QUE ELE EXISTE NESTA ILHA, e a data e 22/09/2026
----------------------------------------------------
Esta ilha tem 70 arquivos em `ferramentas/` e nenhum lugar que diga quais sao
portao. Cada execucao enumera DE CABECA quais bancadas rodar e escreve a lista
no `REGISTRO.md` como prova — e lista escrita de cabeca esquece. O que ela
esquece nao aparece em lugar nenhum, porque o verde das outras ocupa o espaco do
que faltou.

Nao e hipotese: em 22/09/2026 a leva 7 achou QUATRO paginas no ar havia oito
dias sem nunca terem passado pelo portao da voz, e no mesmo dia achou a tabela
de levas do `dados/indexacao.md` em quatro linhas para seis levas. As duas sao a
mesma doenca — lista escrita a mao que a leva seguinte tem de lembrar de
alimentar, e que nao avisa quando alguem esquece. A lista de REGUAS A RODAR e a
terceira lista dessa familia, um andar acima: e a lista de quem vigia as outras.

O molde e o `ferramentas/bancada.py` da ROBOMETRIA (18/09/2026), portado com as
convencoes desta ilha — do mesmo jeito que a aquametria portou de la a purga de
cache e a robometria portou daqui os dois portoes dela. **Nada aqui foi copiado
sem medir**: a regua do veredito abaixo foi calibrada contra as linhas REAIS que
os portoes desta ilha imprimem, e nao contra as da outra.

Entao este arquivo NAO TEM LISTA. Ele varre `ferramentas/` e classifica pela
convencao de nome. Portao novo entra na bancada no dia em que e escrito, sem que
ninguem se lembre dele — e portao que nao casa com nenhuma convencao e
DENUNCIADO em vez de ignorado, porque regua que ninguem roda e regua que nao
existe.

AS CONVENCOES, e elas ja eram as desta pasta antes deste arquivo
-----------------------------------------------------------------
> PONTEIRO DE 20/10/2026: a lista abaixo continua sendo a convencao, e deixou de
> ser o CODIGO. Quem classifica agora e a `regua-classes-da-bancada.py`, que
> pergunta a POSICAO de cada marca em vez da presenca dela — porque este arquivo
> classificava pelo TEXTO, prosa incluida, e mandou um portao novo para a classe
> de Chromium duas vezes em 19/10/2026 (item 6(c) daquele fecho). A diferenca de
> comportamento esta medida no `teste-classes-da-bancada.py`, e ela nao e
> hipotetica em nenhuma das duas direcoes: a leitura antiga errava um arquivo
> desta pasta hoje, e o conserto literal erraria 18.

  teste-*.php               -> php ferramentas/<x>.php .        (sem rede)
  teste-*.py                -> python3 ferramentas/<x>.py       (sem rede)
  testar-*.py               -> python3 ferramentas/<x>.py       (sem rede)
  mutacoes-*.py             -> python3 ferramentas/<x>.py       (sem rede)
  validar-*.py              -> python3 ferramentas/<x>.py       (sem rede)
  teste-*.mjs               -> node ferramentas/<x>.mjs .       (sem rede)
  teste-navegador-*.mjs     -> Chromium real: so com --navegador
  conferir-*                -> ABRE O SITE: so com --no-ar
  qualquer um que chame um teste-navegador-* -> Chromium: so com --navegador
  gerar-|coletar-|atualizar-|render-|varrer-|listar-|proteger-|aplicar-  -> producao, nao e portao
  regua-*.py                -> REGUA COMPARTILHADA: nao afirma nada sozinha, entao
                               nao e portao — mas so escapa da denuncia se algum
                               portao desta pasta a IMPORTAR pelo nome. Regua que
                               nenhum portao exercita e regua que ninguem roda, que
                               e a doenca deste arquivo inteiro. Nasceu em
                               24/09/2026 com a `regua-robots.py`, que e usada
                               pelo `teste-robots.py` (bancada) e pelo
                               `conferir-robots-no-ar.py` (no ar): a regua de
                               `noindex` mora num arquivo so justamente porque
                               escrita duas vezes ela erra de um lado, e foi um
                               erro desses que gerou o falso positivo de 23/09.

A EXCECAO DO `conferir-`, E ELA E DECLARADA PELO PROPRIO ARQUIVO. Tres
`conferir-*` desta ilha nao abrem o site nenhum (`conferir-slugs.py`,
`conferir-protecao-funcoes.py`, `conferir-entidades.mjs`): eles conferem o
repositorio. Quem decide nao e uma lista aqui dentro — e uma linha no cabecalho
do proprio arquivo, `BANCADA: sem rede`. Sem essa linha, `conferir-` e tratado
como rede e fica FORA da passada padrao, com o nome impresso. O lado seguro do
erro e ficar de fora e aparecer, nunca rodar as cegas ou sumir calado.

ANTES DE TUDO, DUAS COISAS QUE NAO SAO ARQUIVO DE PORTAO
---------------------------------------------------------
  1. a regua do veredito abaixo, medida contra si mesma;
  2. `php -l` em TODO snippet da pasta `snippets/` — que tambem era lista
     digitada, no "php -l nos 11 snippets" de cada REGISTRO.md.
As duas rodam sempre, e as duas reprovam a bancada inteira: snippet que nem
analisa faz todo portao medir outra coisa.

O VEREDITO E O CODIGO DE SAIDA, E O TEXTO E CONFERIDO CONTRA ELE
-----------------------------------------------------------------
Todo portao desta ilha sai com `exit(1)` quando reprova. Este arquivo cobra as
DUAS coisas: o codigo de saida e a palavra impressa. Portao que imprime verde e
sai com 1 — ou que imprime vermelho e sai com 0 — e INERTE, e aparece nomeado no
fim. Portao que so um dos dois lados enxerga e portao que mente para quem so le
a ultima linha.
"""
import importlib.util
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA = os.path.join(RAIZ, 'ferramentas')

# A CLASSIFICACAO MORA NUMA REGUA COMPARTILHADA DESDE 20/10/2026
# ---------------------------------------------------------------------------
# As tres perguntas que decidem a classe — quem dirige navegador, quem se
# declara sem rede e quem carrega uma regua — moravam AQUI, e as tres liam a
# marca no TEXTO do arquivo, prosa incluida. Em 19/10/2026 isso mandou um portao
# novo para a classe de Chromium DUAS vezes, e a segunda foi o COMENTARIO que
# explicava a primeira (item 6(c) daquele fecho).
#
# Agora a autoridade e a `regua-classes-da-bancada.py`, que pergunta a POSICAO
# de cada marca pela `onde()` do `regua-teto-do-titulo.py` — e que recebe a
# pasta como DADO, para o portao dela poder encenar pastas que nao existem.
# Quem a exercita e o `teste-classes-da-bancada.py`; quem a mutila e o
# `mutacoes-classes-da-bancada.py`.
#
# **A contagem que decidiu o desenho, e ela esta no portao daquela regua:**
# nenhum portao desta pasta estava na classe errada em 19/10 — o defeito era
# inteiramente latente — e o conserto LITERAL ("so `codigo` mede") poria 18 na
# classe errada, porque invocar e carregar se escrevem com o nome entre aspas
# (`dado`) e declarar se escreve em comentario (`prosa`).
_spec_classes = importlib.util.spec_from_file_location(
    'regua_classes_da_bancada', os.path.join(PASTA, 'regua-classes-da-bancada.py'))
CLASSES = importlib.util.module_from_spec(_spec_classes)
_spec_classes.loader.exec_module(CLASSES)

# A regua do veredito. A VERMELHA nunca casa com uma CONTAGEM ZERO: "0 falha(s)"
# e a frase de aprovacao mais comum desta pasta, e uma regua que a lesse como
# reprovacao denunciaria portao sadio como inerte — o defeito que a robometria
# cometeu e mediu em 18/09/2026, no primeiro minuto do arquivo original.
VERDE = re.compile(r'\bAPROVADO\b|\bTUDO OK\b|\b(?:0|zero|nenhuma?)\s+falhas?\b|\bnenhuma falha\b', re.I)
VERMELHO = re.compile(r'\bREPROVADO\b|^FALHA\b|\bFALHA \[|\bfalharam\b|\b[1-9][0-9]*\s+FALHA\(S\)|\b[1-9][0-9]*\s+falhas?\b', re.I)



# A REGUA DO VEREDITO TEM REGUA PROPRIA
# ---------------------------------------------------------------------------
# As linhas abaixo sao REAIS: cada uma e a ultima linha impressa por um portao
# desta ilha, copiada da passada de 22/09/2026 — mais as contradicoes
# fabricadas, que sao o que o modo inerte existe para pegar. Regua escrita de
# cabeca, sobre texto que existe, se mede contra o texto que existe.
LINHAS_REAIS_APROVADAS = [
    'TUDO OK',
    'APROVADO: 21 afirmações, 0 falha(s).',
    '3158 afirmacoes, 0 falha',
    '30 de 30 mutacoes reprovadas pelo portao',
    '90 de 90 mutacoes reprovadas, zero inerte',
    'APROVADO: 39 registros, 0 erro, 1 aviso.',
    '24 testes, 0 falha',
    '644 afirmacoes, 0 falha',
    'nenhuma falha',
]
LINHAS_REAIS_REPROVADAS = [
    'REPROVADO: 3 de 251 verificacoes falharam.',
    '4 FALHA(S)',
    'FALHA toda página publicada passou pela régua da voz — danios-e-rasboras',
    '2 de 30 mutacoes falharam',
    'APROVADO: 12 medicoes, 1 falha.',
]

def provar():
    erros = 0
    for linha in LINHAS_REAIS_APROVADAS:
        if VERMELHO.search(linha):
            print('  FALHA  linha de APROVACAO lida como reprovacao: %s' % linha)
            erros += 1
    for linha in LINHAS_REAIS_REPROVADAS:
        if not VERMELHO.search(linha):
            print('  FALHA  linha de REPROVACAO nao foi lida como tal: %s' % linha)
            erros += 1
    # As duas contradicoes que definem portao inerte.
    casos = [
        ('APROVADO: 10 afirmacoes, 0 falha.', 1, 'imprime verde e sai com erro'),
        ('REPROVADO: 3 de 10 verificacoes falharam.', 0, 'imprime vermelho e sai com zero'),
    ]
    for ultima, codigo, nome in casos:
        diz_verde = bool(VERDE.search(ultima)) and not VERMELHO.search(ultima)
        diz_vermelho = bool(VERMELHO.search(ultima))
        inerte = (codigo != 0 and diz_verde) or (codigo == 0 and diz_vermelho)
        if not inerte:
            print('  FALHA  nao foi visto como inerte: %s' % nome)
            erros += 1
    # E o mundo sadio, que TEM de passar: verde com saida 0 nao e inerte.
    if VERMELHO.search('TUDO OK'):
        print('  FALHA  portao sadio denunciado como inerte')
        erros += 1

    total = len(LINHAS_REAIS_APROVADAS) + len(LINHAS_REAIS_REPROVADAS) + len(casos) + 1
    if erros:
        print('REPROVADO: %d de %d afirmacoes sobre a regua do veredito.' % (erros, total))
        return 1
    print('APROVADO: %d afirmacoes sobre a regua do veredito, 0 falha.' % total)
    return 0


def lint_dos_snippets():
    """`php -l` em TODO snippet da pasta, e a pasta e quem diz quais sao.

    Ele entrava na bancada pela memoria de quem escrevia o REGISTRO.md ("php -l
    nos 11 snippets"), e o numero 11 era digitado: snippet novo nasceria sem
    lint e sem ninguem notar. Aqui a lista e a pasta, e zero arquivo REPROVA.
    """
    import glob
    arquivos = sorted(glob.glob(os.path.join(RAIZ, 'snippets', '*.php')))
    if not arquivos:
        print('FALHA php -l nao achou snippet nenhum — isto e reprovacao, nao aprovacao.')
        return 1
    ruins = []
    for arq in arquivos:
        r = subprocess.run(['php', '-l', arq], capture_output=True, text=True)
        if r.returncode != 0:
            ruins.append((os.path.basename(arq), (r.stdout + r.stderr).strip().splitlines()[0]))
    for nome, erro in ruins:
        print('FALHA php -l %s: %s' % (nome, erro))
    print('%s php -l em %d snippets, %d falha(s).'
          % ('REPROVADO:' if ruins else 'APROVADO:', len(arquivos), len(ruins)))
    return 1 if ruins else 0


# A `classificar()` DELEGA, E ESTE ARQUIVO NAO TEM MAIS COPIA NENHUMA DA REGRA
# ---------------------------------------------------------------------------
# A pasta e lida UMA vez por passada e entregue a regua como dado. Antes cada
# pergunta reabria os arquivos — `regua_exercitada` sozinha relia a pasta
# inteira uma vez por regua —, e a leitura repetida e o que fazia a regra morar
# em tres lugares.
def classificar(nome, arquivos):
    return CLASSES.classificar(nome, arquivos)


def main(argv):
    com_ar = '--no-ar' in argv
    com_navegador = '--navegador' in argv
    so_lista = '--lista' in argv
    if '--provar' in argv:
        print('A REGUA DO VEREDITO, medida contra as linhas reais desta ilha')
        print('=' * 70)
        return provar()

    arquivos = CLASSES.ler_pasta(PASTA)
    fila, fora_ar, fora_nav, sem_convencao = [], [], [], []
    for nome in sorted(arquivos):
        if nome == os.path.basename(__file__):
            continue
        cmd, cat = classificar(nome, arquivos)
        if cmd is None:
            if cat == 'sem_convencao':
                sem_convencao.append(nome)
            continue
        if cat == 'no_ar' and not com_ar:
            fora_ar.append(nome)
            continue
        if cat == 'navegador' and not com_navegador:
            fora_nav.append(nome)
            continue
        fila.append((nome, cmd, cat))

    print('BANCADA DA AQUAMETRIA — %d portoes%s%s' % (
        len(fila), ', com os do ar' if com_ar else ', sem rede',
        ', com os de navegador' if com_navegador else ''))
    print('=' * 70)
    if so_lista:
        for nome, cmd, cat in fila:
            print('  %-36s %s' % (nome, ' '.join(cmd)))
        if fora_ar:
            print('\nfora desta passada (abrem o site, use --no-ar): ' + ', '.join(fora_ar))
        if fora_nav:
            print('fora desta passada (Chromium, use --navegador): ' + ', '.join(fora_nav))
        if sem_convencao:
            print('\nSEM CONVENCAO, ninguem roda: ' + ', '.join(sem_convencao))
        return 0

    # PORTAO ZERO: a regua do veredito, medida antes de julgar qualquer portao.
    # Ela roda SEMPRE, porque bancada cuja regua de leitura ninguem confere e a
    # mesma armadilha um andar acima.
    if provar() != 0:
        print('\nREPROVADO na propria regua do veredito — nenhum portao foi rodado.')
        return 1
    if lint_dos_snippets() != 0:
        print('\nREPROVADO no php -l — nenhum portao foi rodado, porque snippet que nem '
              'analisa faz todo portao medir outra coisa.')
        return 1
    print('-' * 70)

    reprovados, inertes = [], []
    for nome, cmd, cat in fila:
        try:
            r = subprocess.run(cmd, cwd=RAIZ, capture_output=True, text=True, timeout=3600)
            saida = (r.stdout or '') + (r.stderr or '')
            codigo = r.returncode
        except subprocess.TimeoutExpired:
            saida, codigo = '(estourou 3600 s)', 124

        ultima = ''
        for linha in reversed(saida.strip().splitlines()):
            if linha.strip():
                ultima = linha.strip()
                break

        diz_verde = bool(VERDE.search(ultima)) and not VERMELHO.search(ultima)
        diz_vermelho = bool(VERMELHO.search(ultima))
        if (codigo != 0 and diz_verde) or (codigo == 0 and diz_vermelho):
            inertes.append((nome, codigo, ultima))

        marca = 'ok  ' if codigo == 0 else 'FALHA'
        print('%-5s %-36s %s' % (marca, nome, ultima[:100]))
        if codigo != 0:
            reprovados.append((nome, codigo, saida))

    print('=' * 70)
    if fora_ar:
        print('fora desta passada (abrem o site, use --no-ar): ' + ', '.join(fora_ar))
    if fora_nav:
        print('fora desta passada (Chromium, use --navegador): ' + ', '.join(fora_nav))
    if sem_convencao:
        print('SEM CONVENCAO, ninguem roda: ' + ', '.join(sem_convencao))
    if inertes:
        print('\nPORTOES INERTES — o texto e o codigo de saida discordam:')
        for nome, codigo, ultima in inertes:
            print('  %s (saida %d) disse: %s' % (nome, codigo, ultima))

    if reprovados:
        print('\nREPROVADO: %d de %d portoes.' % (len(reprovados), len(fila)))
        for nome, codigo, saida in reprovados:
            print('\n--- %s (saida %d) ---' % (nome, codigo))
            print('\n'.join(saida.strip().splitlines()[-25:]))
        return 1
    if inertes:
        print('\nREPROVADO por portao inerte: %d.' % len(inertes))
        return 1
    print('\nAPROVADO: %d portoes, 0 falha.' % len(fila))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
