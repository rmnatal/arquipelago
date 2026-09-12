#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Devolve o pronome as frases da R1 e exige REPROVACAO.

    python3 ferramentas/mutacoes-frase-nomeia-o-tipo.py

POR QUE ESTE ARQUIVO EXISTE
---------------------------
"A PROVA DE QUE UMA TRAVA REPROVA E PARTE DO BLOCO" (secao 8 do ARQUIPELAGO.md).
A secao 14 do ferramentas/teste-r1.php nasceu em 12/09/2026, DEPOIS do defeito
que ela existe para pegar — entao ela passar nao prova nada. Estas mutacoes
escrevem o defeito de volta, cada uma de um jeito, e cobram vermelho.

O DEFEITO, e ele ESTAVA NO AR em tres paginas. A frase do kit quando existe a
peca avulsa era:

    "Ele tambem vem dentro do kit <nome>, que a <marca> declara compativel..."

Ela lia certo por SORTE DE ORDEM. As frases da resposta saem na ordem do banco,
e no unico caso que existia (o filtro do ERB60/61/62) o registro da peca avulsa
vinha antes do registro do kit — entao o "Ele" caia logo depois da frase que
nomeava o filtro. Ao entrar o pano de microfibra ERB60/61/62/80 em 12/09/2026, o
mop passou a ter avulso E kit: a frase do kit foi emitida na posicao do KIT, ou
seja, depois da escova lateral e ANTES de o mop ser nomeado. Pronome sem
antecedente, em pagina publicada, e nenhum dos oito portoes via — porque todos
mediam a frase sozinha, e sozinha ela estava certa.

A saida nao foi reordenar a lista: foi a frase parar de depender da vizinhanca,
que e a secao 8 do contrato ("quem decide e a estrutura, nunca a vizinhanca") e
a 5.2 ("frase autossuficiente que sobrevive a ser citada fora de contexto").

O QUE CADA MUTACAO TEM DE FAZER: reprovar pela trava NOVA. As quatro abaixo
foram escolhidas para passar pelos portoes ANTIGOS de proposito — nenhuma delas
muda o numero de frases comparadas, nenhuma mexe em chave, e a (4) mantem ate a
igualdade PHP x referencia que a secao 3 mede, porque quebra os DOIS lados
juntos. Era exatamente assim que o defeito original entrava.
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REFERENCIA = 'ferramentas/cobertura-r1.py'
SNIPPET = 'snippets/robometria-r1.php'
GERADOR = 'ferramentas/gerar-r1.py'
TESTE = ('ferramentas/teste-r1.php',)


def _troca(base, arquivo, antes, depois, quantas=1):
    caminho = os.path.join(base, arquivo)
    with open(caminho, encoding='utf-8') as f:
        texto = f.read()
    if texto.count(antes) != quantas:
        raise AssertionError('%s: esperava %d ocorrencia(s) de %r, achei %d — a mutacao '
                             'seria inerte' % (arquivo, quantas, antes[:48], texto.count(antes)))
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(texto.replace(antes, depois))


def _regerar(base):
    """Sem isto a mutacao na referencia nao chega a dados/r1-respostas.json e a
    trava mediria o arquivo de ontem — mutacao inerte com outro nome."""
    saida = subprocess.run(['python3', os.path.join(base, GERADOR), '--gravar'],
                           capture_output=True, text=True, cwd=base)
    if saida.returncode != 0:
        raise AssertionError('gerar-r1.py falhou depois da mutacao: %s' % saida.stderr[-200:])


PRONOME_PY = ('"%s %s tambem vem dentro do kit %s, que a %s declara compativel com %s "\n'
              '            "(%s, verificado em %s)."\n'
              '            % (artigo.capitalize(), dentro_do_kit, identificacao, publicador, lista,\n'
              '               fonte.get("origem"), data)')

PRONOME_PY_DEFEITO = ('"%s tambem vem dentro do kit %s, que a %s declara compativel com %s "\n'
                      '            "(%s, verificado em %s)."\n'
                      '            % (("ele" if artigo == "o" else "ela").capitalize(), '
                      'identificacao, publicador, lista,\n'
                      '               fonte.get("origem"), data)')

PRONOME_PHP = ("'%1$s %2$s também vem dentro do kit %3$s, que a %4$s declara "
               "compatível com %5$s (%6$s, verificado em %7$s).',\n"
               "\t\t\trobometria_r1_maiuscula( $artigo ), $tipo, $identificacao, "
               "$item['publicador'],")

PRONOME_PHP_DEFEITO = ("'%1$s também vem dentro do kit %2$s, que a %3$s declara "
                       "compatível com %4$s (%5$s, verificado em %6$s).',\n"
                       "\t\t\trobometria_r1_maiuscula( $pronome ), $identificacao, "
                       "$item['publicador'],")


def _pronome_so_na_referencia(base):
    """O defeito original, no lado que produz o dado."""
    _troca(base, REFERENCIA, PRONOME_PY, PRONOME_PY_DEFEITO)
    _regerar(base)


def _pronome_so_no_php(base):
    """O mesmo defeito, no lado que escreve a tela."""
    _troca(base, SNIPPET, PRONOME_PHP, PRONOME_PHP_DEFEITO)


def _pronome_nos_dois_lados(base):
    """A mutacao que PRODUZ O MUNDO do defeito original: as duas metades erram
    juntas, entao a comparacao PHP x referencia da secao 3 continua verde e a
    contagem de frases nao muda. Se so a secao 3 existisse, este seria um
    desembarque com oito portoes verdes e um pronome sem antecedente no ar."""
    _troca(base, REFERENCIA, PRONOME_PY, PRONOME_PY_DEFEITO)
    _troca(base, SNIPPET, PRONOME_PHP, PRONOME_PHP_DEFEITO)
    _regerar(base)


def _tipo_empurrado_para_o_fim_da_frase(base):
    """A porta dos fundos da trava: manter o tipo na frase, mas so DEPOIS do
    ponto final, onde ele nao ajuda quem le a abertura. Se a conferencia
    procurasse o nome do tipo na frase inteira em vez de na primeira oracao,
    esta mutacao passaria — e e a mesma familia do 'contar &#038; na pagina
    inteira' que a secao 8 do contrato registra."""
    _troca(base, REFERENCIA, PRONOME_PY,
           PRONOME_PY_DEFEITO.replace('verificado em %s)."', 'verificado em %s). Trata-se %s %s."')
           .replace('fonte.get("origem"), data)', 'fonte.get("origem"), data, artigo, dentro_do_kit)'))
    _troca(base, SNIPPET, PRONOME_PHP,
           PRONOME_PHP_DEFEITO.replace('verificado em %6$s).',
                                       'verificado em %6$s). Trata-se %7$s %8$s.')
           .replace("$item['publicador'],", "$item['publicador'], $artigo, $tipo,"))
    _regerar(base)


MUTACOES = [
    (
        'a referencia volta ao pronome ("Ele tambem vem dentro do kit")',
        'e o defeito original, do lado que produz o dado que viaja para o site',
        _pronome_so_na_referencia,
    ),
    (
        'o snippet volta ao pronome',
        'o mesmo defeito no lado que escreve a tela — aqui a secao 3 tambem pega, e e de proposito: as duas travas medem coisas diferentes',
        _pronome_so_no_php,
    ),
    (
        'os DOIS lados voltam ao pronome, juntos',
        'PRODUZ O MUNDO do defeito: a comparacao PHP x referencia continua verde, o numero de frases nao muda, e sem a secao 14 isto desembarcaria',
        _pronome_nos_dois_lados,
    ),
    (
        'o tipo existe na frase, mas so depois do ponto final',
        'a porta dos fundos: a abertura continua sendo um pronome, e uma regua que procurasse o nome do tipo na frase INTEIRA daria verde',
        _tipo_empurrado_para_o_fim_da_frase,
    ),
]


def main():
    reprovadas = 0
    passaram = []

    print('Mutacoes deliberadas na frase da R1 — cada uma TEM que reprovar\n')

    for nome, porque, aplicar in MUTACOES:
        with tempfile.TemporaryDirectory() as tmp:
            base = os.path.join(tmp, 'ilha')
            shutil.copytree(RAIZ, base)
            try:
                aplicar(base)
            except (AssertionError, subprocess.CalledProcessError) as erro:
                print('  ERRO   %-62s %s' % (nome, erro))
                passaram.append(nome)
                continue

            falhas = []
            pegou_em = []
            for teste in TESTE:
                cmd = ['php', os.path.join(base, teste), base]
                saida = subprocess.run(cmd, capture_output=True, text=True)
                if saida.returncode != 0:
                    pegou_em.append(os.path.basename(teste))
                    falhas += [l.strip() for l in saida.stdout.splitlines()
                               if l.strip().startswith(('FALHA', 'ERRO'))]

            if not pegou_em:
                print('  PASSOU %-62s <- a trava NAO pegou' % nome)
                print('         (%s)' % porque)
                passaram.append(nome)
                continue

            print('  ok     %-62s %d falha(s) em %s'
                  % (nome, len(falhas), ', '.join(pegou_em)))
            for l in falhas[:2]:
                print('         %s' % l[:120])
            reprovadas += 1

    print('\n%d de %d mutacoes reprovadas pela bancada.' % (reprovadas, len(MUTACOES)))
    if passaram:
        print('MUTACOES QUE PASSARAM (trava faltando):')
        for n in passaram:
            print('  - %s' % n)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
