#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Roda a BANCADA INTEIRA desta ilha com um comando so, e descobre os portoes
em vez de os listar.

    python3 ferramentas/bancada.py             # so o que roda sem rede
    python3 ferramentas/bancada.py --no-ar     # inclui os conferir-*, que abrem o site
    python3 ferramentas/bancada.py --lista     # so imprime o que rodaria, sem rodar

POR QUE ELE EXISTE, e a data e 18/09/2026
-----------------------------------------
A secao 16 do `teste-casca.php` nasceu em 14/09/2026 depois de o cabecalho de
DOIS snippets divergir da constante de versao — a execucao movia o texto e
esquecia o numero, ou o contrario. A regua foi escrita, e ela funciona: em
18/09/2026, as 19h25Z, ela pegou a MESMA divergencia em TRES arquivos de uma vez
(casca 1.10.1/1.11.0, R1 1.10.0/1.11.0, R2 1.8.0/1.9.0), deixados pela execucao
das 16h16Z daquele mesmo dia.

**O defeito nao era a falta de regua: era a regua nao ter rodado.** Cada execucao
desta ilha enumera de cabeca quais bancadas rodar, e escreve a lista no
`REGISTRO.md` como prova. Lista escrita de cabeca esquece — e o que ela esquece
nao aparece em lugar nenhum, porque o verde das outras ocupa o espaco do que
faltou. E a mesma cicatriz que a ilha ja carrega no `robometria_casca_categorias()`
(lista digitada ao lado de lista contada) e no painel da foto da 25.7 (duas
metades contando a mesma coisa sem nunca se falarem), um nivel acima: aqui o que
diverge e a lista de reguas contra a pasta que as guarda.

Entao este arquivo NAO TEM LISTA. Ele varre `ferramentas/` e classifica pela
convencao de nome. Portao novo entra na bancada no dia em que e escrito, sem que
ninguem se lembre dele — e portao que nao casa com nenhuma convencao e
DENUNCIADO em vez de ignorado, porque regua que ninguem roda e regua que nao
existe.

AS TRES CONVENCOES, e elas ja eram as desta pasta antes deste arquivo
---------------------------------------------------------------------
  teste-*.php      -> php ferramentas/<x>.php .      (sem rede)
  teste-*.py       -> python3 ferramentas/<x>.py     (sem rede)
  mutacoes-*.py    -> python3 ferramentas/<x>.py     (sem rede)
  validar-*.py     -> python3 ferramentas/<x>.py     (sem rede)
  conferir-*.py    -> python3 ferramentas/<x>.py     (ABRE O SITE: so com --no-ar)
  *.mjs            -> navegador, fora desta bancada  (denunciado, nao rodado)

O VEREDITO E O CODIGO DE SAIDA, E O TEXTO E CONFERIDO CONTRA ELE
-----------------------------------------------------------------
Toda regua desta ilha sai com `exit(1)` quando reprova. Este arquivo cobra as
DUAS coisas: o codigo de saida e a palavra impressa. Portao que imprime
REPROVADO e sai com 0 — ou que imprime APROVADO e sai com 1 — e **INERTE**, e
aparece nomeado no fim. Portao que so um dos dois lados enxerga e portao que
mente para quem so le a ultima linha.
"""
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA = os.path.join(RAIZ, 'ferramentas')

# Ferramentas de PRODUCAO: geram, coletam ou publicam. Nao sao portao e nao
# entram na bancada. A lista e curta de proposito e cada nome esta aqui porque
# NAO afirma nada — quem afirma tem nome de portao.
NAO_E_PORTAO = re.compile(r'^(gerar|coletar|medir|acentuar|atualizar|cobertura|publicadores|render|varrer|bancada)[-.]')

# A regua do veredito impresso. A VERMELHA nunca casa com uma CONTAGEM ZERO:
# "0 falha(s)." e a frase de aprovacao mais comum desta pasta, e a primeira
# versao deste arquivo a leu como reprovacao e denunciou tres portoes sadios
# como inertes. Contagem so e vermelha a partir de 1.
VERDE = re.compile(r'\bAPROVADO\b|\b(?:0|zero|nenhuma?)\s+falhas?\b|\bnenhuma falha\b', re.I)
VERMELHO = re.compile(r'\bREPROVADO\b|\bFALHA \[|\bfalharam\b|\b[1-9][0-9]*\s+falhas?\b', re.I)


# ---------------------------------------------------------------------------
# A REGUA DO VEREDITO TEM REGUA PROPRIA (--provar)
# ---------------------------------------------------------------------------
# A primeira versao deste arquivo denunciou TRES portoes sadios como inertes
# porque a expressao vermelha casava com "0 falha(s).". O defeito durou um
# minuto e ensina o de sempre: regua escrita de cabeca, sobre texto que existe,
# se mede contra o texto que existe. As linhas abaixo sao as VERDADEIRAS, uma
# de cada portao desta ilha, copiadas da passada de 18/09/2026 — mais as
# contradicoes fabricadas, que sao o que o modo inerte existe para pegar.
LINHAS_REAIS_APROVADAS = [
    'APROVADO: 251 verificacoes, nenhuma falha.',
    '107 medicoes, 0 falha(s)',
    'APROVADO: 164 afirmacoes, 0 falha(s).',
    'APROVADO: 21 afirmações, 0 falha(s).',
    'APROVADO: 879 afirmacoes, 0 falha.',
    'APROVADO: 17 medicoes, zero falhas.',
    'APROVADO: nenhuma invariante do esquema violada.',
    'APROVADO: 8 baterias, todas decidindo certo, ZERO inertes.',
    'APROVADO: 17 mutacoes, todas com o resultado esperado, 0 inertes.',
    '19 de 19 mutacoes reprovadas pela bancada.',
    '10 de 10: toda trava foi vista reprovando, e os mundos sadios passaram.',
    'Nenhuma mutacao inerte: toda trava foi vista reprovando pela regra que nomeia.',
    'Todas as travas reprovam o que tem de reprovar, e nascer tipo novo nao reprova nada.',
    '7 de 7 no resultado esperado',
]
LINHAS_REAIS_REPROVADAS = [
    'REPROVADO: 3 de 251 verificacoes falharam.',
    '  FALHA [robometria-casca] a versao do cabecalho e a da constante      cabecalho 1.10.1 / constante 1.11.0',
    'REPROVADO: 2 de 38 portoes.',
    'APROVADO: 12 medicoes, 1 falha.',
]


def provar():
    erros = 0
    for linha in LINHAS_REAIS_APROVADAS:
        verde = bool(VERDE.search(linha)) and not VERMELHO.search(linha)
        vermelho = bool(VERMELHO.search(linha))
        if vermelho:
            print('  FALHA  linha de APROVACAO lida como reprovacao: %s' % linha)
            erros += 1
        # Nem toda linha de aprovacao desta pasta diz "APROVADO" ou "0 falha" —
        # varias dizem "N de N mutacoes reprovadas". O que se cobra aqui e que
        # nenhuma delas seja lida como VERMELHA; o verde e bonus.
        del verde
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
    if (0 != 0) or (0 == 0 and bool(VERMELHO.search('APROVADO: 21 afirmações, 0 falha(s).'))):
        print('  FALHA  portao sadio denunciado como inerte (o defeito de 18/09)')
        erros += 1

    total = len(LINHAS_REAIS_APROVADAS) + len(LINHAS_REAIS_REPROVADAS) + len(casos) + 1
    if erros:
        print('REPROVADO: %d de %d afirmacoes sobre a regua do veredito.' % (erros, total))
        return 1
    print('APROVADO: %d afirmacoes sobre a regua do veredito, 0 falha.' % total)
    return 0


def classificar(nome):
    """Devolve (comando, categoria) ou (None, motivo) para o que nao roda aqui."""
    if nome.endswith('.mjs'):
        return None, 'navegador'
    if NAO_E_PORTAO.match(nome):
        return None, 'producao'
    if nome.startswith('teste-') and nome.endswith('.php'):
        return ['php', os.path.join('ferramentas', nome), '.'], 'sem_rede'
    if nome.startswith(('teste-', 'mutacoes-', 'validar-')) and nome.endswith('.py'):
        return ['python3', os.path.join('ferramentas', nome)], 'sem_rede'
    if nome.startswith('conferir-') and nome.endswith('.py'):
        return ['python3', os.path.join('ferramentas', nome)], 'no_ar'
    if nome.endswith('.php') or nome.endswith('.py'):
        return None, 'sem_convencao'
    return None, 'ignorado'


def main(argv):
    com_ar = '--no-ar' in argv
    so_lista = '--lista' in argv
    if '--provar' in argv:
        print('A REGUA DO VEREDITO, medida contra as linhas reais desta ilha')
        print('=' * 70)
        return provar()

    arquivos = sorted(os.listdir(PASTA))
    fila, fora, sem_convencao = [], [], []
    for nome in arquivos:
        if nome.startswith('.') or nome == os.path.basename(__file__):
            continue
        cmd, cat = classificar(nome)
        if cmd is None:
            if cat == 'sem_convencao':
                sem_convencao.append(nome)
            continue
        if cat == 'no_ar' and not com_ar:
            fora.append(nome)
            continue
        fila.append((nome, cmd, cat))

    print('BANCADA DA ROBOMETRIA — %d portoes%s' % (len(fila), ', com os do ar' if com_ar else ', sem rede'))
    print('=' * 70)
    if so_lista:
        for nome, cmd, cat in fila:
            print('  %-34s %s' % (nome, ' '.join(cmd)))
        if fora:
            print('\nfora desta passada (abrem o site, use --no-ar): ' + ', '.join(fora))
        if sem_convencao:
            print('\nSEM CONVENCAO, ninguem roda: ' + ', '.join(sem_convencao))
        return 0

    # PORTAO ZERO: a regua do veredito, medida antes de julgar qualquer portao.
    # Ela roda SEMPRE, sem precisar de --provar, porque bancada cuja regua de
    # leitura ninguem confere e a mesma armadilha um andar acima.
    if provar() != 0:
        print('\nREPROVADO na propria regua do veredito — nenhum portao foi rodado.')
        return 1
    print('-' * 70)

    reprovados, inertes = [], []
    for nome, cmd, cat in fila:
        try:
            r = subprocess.run(cmd, cwd=RAIZ, capture_output=True, text=True, timeout=900)
            saida = (r.stdout or '') + (r.stderr or '')
            codigo = r.returncode
        except subprocess.TimeoutExpired:
            saida, codigo = '(estourou 900 s)', 124

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
        print('%-5s %-34s %s' % (marca, nome, ultima[:110]))
        if codigo != 0:
            reprovados.append((nome, codigo, saida))

    print('=' * 70)
    if fora:
        print('fora desta passada (abrem o site, use --no-ar): ' + ', '.join(fora))
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
