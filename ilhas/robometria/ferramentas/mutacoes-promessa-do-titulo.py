#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escreve de volta, uma a uma, as formas de a promessa numerica do <title>
apodrecer — e exige REPROVACAO da bancada em todas.

    python3 ferramentas/mutacoes-promessa-do-titulo.py

POR QUE ESTA BATERIA EXISTE
---------------------------
O bloco de 17/09/2026 fez a cabeca de pagina publicar numero pela primeira vez,
e fez isso invertendo uma regra que a propria casca tinha escrito com todas as
letras em 11/09 ("nenhuma descricao carrega numero"). Regra invertida precisa de
prova mais dura que regra nova: a bancada tem de reprovar cada jeito de o numero
voltar a ser o que a regra antiga temia — digitado, orfao, ou certo no universo
errado.

E ha uma segunda razao, que e desta ilha: TRES das cinco travas deste mecanismo
sao SILENCIOSAS por desenho. Se o banco nao chegar ao site, se a chave sumir da
medicao, ou se o titulo estourar o teto de 65, a pagina cai de volta para a
frase sem numero e para a marca — e continua valida, sem sintoma. Trava
silenciosa sem quem a conte e exatamente como o caminho "derivado" de
robometria_casca_numeros() ficou dois dias sendo decoracao nesta ilha. Aqui a
bateria e quem conta.

AS SEIS MUTACOES

  1. A PROMESSA VOLTA A SER DIGITADA. "de 1.400 a 10.000 Pa" escrito a mao no
     mapa, sem `promessa_numeros`. E o mundo que a regra de 11/09 proibia, e o
     unico em que o numero segue no ar depois de o banco mudar.
  2. UMA CHAVE QUE NAO EXISTE NA MEDICAO. `pa_minimo_publicavel` em vez de
     `pa_minimo`: o molde nao resolve, a pagina cai para a frase sem banco e o
     titulo volta para a marca — tudo isso em silencio.
  3. O MOLDE PERDE UM BURACO. Tres chaves, dois `%s`: sobra numero sem lugar.
  4. A FRASE SEM BANCO SOME. E a mutacao que produz o pior estado possivel
     deste mecanismo: o molde cru, com "%1$s" dentro, servido na
     <meta name="description">.
  5. O Pa VOLTA A SER CONTADO SOBRE PUBLICAVEL. E a mutacao substantiva, e a
     unica que a casca sozinha nao tem como notar: o numero continua sendo um
     numero, e passa a ser 15.000 — a succao de um Xiaomi sem canal brasileiro,
     que o portao da R2 nunca recomenda. O titulo prometeria na SERP o que a
     ferramenta se recusa a sugerir. Quem pega e a secao 8 do teste-casca.php,
     que reconta os cinco numeros nos REGISTROS.
  6. O MUNDO SADIO. Nenhuma mutacao. Tem de PASSAR, e e ele que prova que as
     cinco acima reprovaram pela mutacao e nao por ruido da copia.
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CASCA = 'snippets/robometria-casca.php'
GERADOR = 'ferramentas/gerar-casca-fatos.py'
TESTE = 'ferramentas/teste-casca.php'

# A versao do manifest e a da constante tem de bater, e a secao 16 da bancada
# cobra isso. Como a copia carrega o manifest do momento, ela ja bate; nenhuma
# mutacao daqui mexe em versao.


def _troca(base, arquivo, antes, depois, quantas=1):
    caminho = os.path.join(base, arquivo)
    with open(caminho, encoding='utf-8') as f:
        texto = f.read()
    achadas = texto.count(antes)
    if achadas != quantas:
        raise AssertionError('esperava %d ocorrencia(s) em %s, achei %d'
                             % (quantas, arquivo, achadas))
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(texto.replace(antes, depois))


def _regerar_fatos(base):
    saida = subprocess.run(['python3', os.path.join(base, GERADOR), '--gravar'],
                           capture_output=True, text=True, cwd=base)
    if saida.returncode != 0:
        raise AssertionError('gerar-casca-fatos.py falhou depois da mutacao: %s'
                             % saida.stderr[-300:])


def m1_promessa_digitada(base):
    _troca(base, CASCA,
           "'promessa'            => 'de %1$s a %2$s Pa',\n"
           "\t\t\t'promessa_numeros'    => array( 'pa_minimo', 'pa_maximo' ),",
           "'promessa'            => 'de 1.400 a 10.000 Pa',")


def m2_chave_que_nao_existe(base):
    _troca(base, CASCA,
           "'numeros'             => array( 'pa_minimo', 'pa_maximo', 'modelos_recomendaveis_com_pa' ),",
           "'numeros'             => array( 'pa_minimo_publicavel', 'pa_maximo', 'modelos_recomendaveis_com_pa' ),")


def m3_molde_perde_um_buraco(base):
    _troca(base, CASCA,
           'o fabricante declara de %1$s a %2$s Pa nos %3$s modelos que você compra no Brasil.',
           'o fabricante declara de %1$s a %2$s Pa nos modelos que você compra no Brasil.')


def m4_frase_sem_banco_some(base):
    caminho = os.path.join(base, CASCA)
    with open(caminho, encoding='utf-8') as f:
        texto = f.read()
    novo, quantas = re.subn(r"\n\t\t\t'descricao_sem_banco' => '[^']*',", '', texto)
    if quantas != 3:
        raise AssertionError('esperava 3 frases sem banco, achei %d' % quantas)
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(novo)


def m5_pa_sobre_publicavel(base):
    _troca(base, GERADOR,
           "recomendaveis = [r for r in modelos_pub if valor(r.get('canal_brasileiro')) is not None]\n"
           "    pas = [valor(r.get('pa_declarado')) for r in recomendaveis]",
           "recomendaveis = [r for r in modelos_pub if valor(r.get('canal_brasileiro')) is not None]\n"
           "    pas = [valor(r.get('pa_declarado')) for r in modelos_pub]")
    _regerar_fatos(base)


def m6_mundo_sadio(base):
    return


MUTACOES = [
    ('a promessa volta a ser digitada no mapa',
     'o numero sobrevive ao banco mudar — a regra de 11/09 em pessoa',
     m1_promessa_digitada, True),
    ('uma chave que nao existe na medicao',
     'a promessa some em silencio e a pagina fica valida sem sintoma',
     m2_chave_que_nao_existe, True),
    ('o molde perde um buraco e sobra chave',
     'numero sem lugar: o molde resolve pela metade e ninguem ve',
     m3_molde_perde_um_buraco, True),
    ('a frase sem banco some das tres cabecas',
     'o molde cru, com %1$s dentro, servido no resultado da busca',
     m4_frase_sem_banco_some, True),
    ('o Pa volta a ser contado sobre publicavel',
     'o titulo promete 15.000 Pa que a R2 se recusa a recomendar',
     m5_pa_sobre_publicavel, True),
    ('MUNDO SADIO — nenhuma mutacao',
     'a bancada reprova o mundo que ela deveria aprovar',
     m6_mundo_sadio, False),
]


def main():
    print('Robometria — a promessa numerica do <title> (proposta 2 da leitura '
          'semanal de 16/09)\n')
    certas = 0
    for titulo, porque, mutar, deve_reprovar in MUTACOES:
        base = tempfile.mkdtemp(prefix='rbm-promessa-')
        alvo = os.path.join(base, 'ilha')
        shutil.copytree(RAIZ, alvo)
        try:
            mutar(alvo)
        except AssertionError as e:
            print('  INERTE %-52s %s' % (titulo[:52], e))
            shutil.rmtree(base, ignore_errors=True)
            continue
        saida = subprocess.run(['php', os.path.join(alvo, TESTE), alvo],
                               capture_output=True, text=True, cwd=alvo)
        reprovou = saida.returncode != 0
        quantas = saida.stdout.count('  FALHA')
        acertou = (reprovou == deve_reprovar)
        marca = 'ok    ' if acertou else 'PASSOU'
        if deve_reprovar:
            medido = ('%d falha(s) na bancada' % quantas) if reprovou else 'a trava NAO pegou'
        else:
            medido = 'aprovado' if not reprovou else ('%d falha(s) sem mutacao' % quantas)
        print('  %s %-52s %s' % (marca, titulo[:52], medido))
        if not acertou:
            print('         %s' % porque)
        certas += 1 if acertou else 0
        shutil.rmtree(base, ignore_errors=True)

    print('\n%d de %d mutacoes com o resultado esperado.' % (certas, len(MUTACOES)))
    return 0 if certas == len(MUTACOES) else 1


if __name__ == '__main__':
    sys.exit(main())
