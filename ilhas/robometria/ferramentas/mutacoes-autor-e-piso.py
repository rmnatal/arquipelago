#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escreve de volta os dois defeitos do despacho da Sentinela de 16/10/2026 e
exige REPROVACAO.

    python3 ferramentas/mutacoes-autor-e-piso.py

ITEM 1 — `Article` SEM `author`. Medido no ar em 16/10 as 14h4xZ e reconferido
em 23/10: `/quantos-m2-o-robo-aspirador-limpa-por-carga/` servia no `Article`
com `publisher` e SEM `author`, enquanto `/filtro-universal-de-robo-aspirador/`
— mesma ilha, mesmo emissor — servia os dois. No repositorio a diferenca era UMA
LINHA de array. O que nenhum portao via: `teste-a1.php` e `teste-a2.php` medem
cada um a SUA pagina, e regua por pagina nao enxerga o que duas paginas deviam
ter em comum. O portao novo (`teste-artigo-com-autor.php`) DESCOBRE as paginas e
cobra `author` de todo no `Article` que achar, que e o que o "pronto quando" do
despacho exige com estas palavras: "em qualquer URL que tenha `Article`".

ITEM 2, metade (b) — O PISO DA 25.2 SEM PORTAO. A outra metade do item 2 foi
ANULADA pela propria Sentinela por medicao, e a errata e explicita sobre o que
sobrou: "vale a pena escrever um portao sem rede que reprove registro
`publicavel` com `url_busca` vazia ou ausente — hoje ele ficaria verde, e e
justamente por isso que e a hora de escreve-lo. E ELE TEM DE OLHAR O `status`,
senao vai reprovar os tres excluidos e a Fundacao seguinte vai 'consertar' o que
esta errata acabou de anular". Entao a bateria prova as DUAS direcoes, como o
"pronto quando" pede: que ele morde em registro publicavel e que NAO morde em
registro `excluido_do_banco`.

AS MUTACOES:

  1. o `author` sai do array do A2 (o defeito de 16/10 tal e qual);
  2. o `author` sai do array do A1 (o lado que estava certo — prova que o portao
     julga as duas paginas e nao uma lista de uma);
  3. o `author` passa a apontar para uma pessoa que esta ilha nao tem;
  4. o filtro de "estou na minha pagina" deixa de ser reposto entre alvos (o
     defeito que o proprio portao cometeu ao nascer: medir a pagina com o estado
     da anterior);
  5. um registro PUBLICAVEL perde a `url_busca`;
  6. um registro publicavel perde a `url_busca` e ganha motivo, mas fica sem
     porta de compra nenhuma;
  7. E A DIRECAO CONTRARIA, que o despacho exige por escrito: um registro
     `excluido_do_banco` continua sem `url_busca` e o portao tem de ficar
     VERDE. Esta e a unica linha desta bateria que exige APROVACAO.
"""

import io
import json
import re
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PORTAO_AUTOR = 'ferramentas/teste-artigo-com-autor.php'
PORTAO_BANCO = 'ferramentas/validar-banco.py'

LINHA_AUTOR = "\t\t'author'           => array( '@id' => home_url( '/#organizacao' ) ),"


def _tirar_author(base, snippet):
    caminho = os.path.join(base, 'snippets', snippet)
    with io.open(caminho, encoding='utf-8') as f:
        texto = f.read()
    if texto.count(LINHA_AUTOR) != 1:
        raise AssertionError('esperava 1 linha de author em %s, achei %d'
                             % (snippet, texto.count(LINHA_AUTOR)))
    with io.open(caminho, 'w', encoding='utf-8') as f:
        f.write(texto.replace(LINHA_AUTOR, '', 1))


def m1_a2_perde_o_author(base):
    _tirar_author(base, 'robometria-a2.php')


def m2_a1_perde_o_author(base):
    _tirar_author(base, 'robometria-a1.php')


def m3_author_vira_pessoa(base):
    caminho = os.path.join(base, 'snippets', 'robometria-a2.php')
    with io.open(caminho, encoding='utf-8') as f:
        texto = f.read()
    novo = ("\t\t'author'           => array( '@type' => 'Person', "
            "'name' => 'Equipe Robometria' ),")
    with io.open(caminho, 'w', encoding='utf-8') as f:
        f.write(texto.replace(LINHA_AUTOR, novo, 1))


def m4_filtro_vaza_entre_alvos(base):
    """O defeito que o proprio portao cometeu ao nascer.

    Sem repor o retrato dos filtros, o `Article` do A1 e creditado a /pecas/ e as
    quatro paginas de malha. O portao nao reprovava nada: ele AFIRMAVA SOBRE
    PAGINA ERRADA, que e pior, porque um `Article` sadio emprestado pelo vizinho
    esconde o defeito da pagina que nao serve nenhum."""
    caminho = os.path.join(base, PORTAO_AUTOR)
    with io.open(caminho, encoding='utf-8') as f:
        texto = f.read()
    alvo = "\t$GLOBALS['__filtros'] = $filtros_da_carga;"
    if alvo not in texto:
        raise AssertionError('nao achei a reposicao do retrato dos filtros')
    with io.open(caminho, 'w', encoding='utf-8') as f:
        f.write(texto.replace(alvo, '', 1))


def _primeiro_publicavel(base, arquivo):
    caminho = os.path.join(base, 'dados', arquivo)
    with io.open(caminho, encoding='utf-8') as f:
        d = json.load(f)
    for r in d['registros']:
        if r.get('status') == 'publicavel' and (
                (r.get('afiliado') or {}).get('url_busca') or '').strip():
            return caminho, d, r
    raise AssertionError('nenhum registro publicavel com url_busca em %s: a '
                         'mutacao seria inerte' % arquivo)


def _gravar(caminho, d):
    with io.open(caminho, 'w', encoding='utf-8') as f:
        f.write(json.dumps(d, ensure_ascii=False, indent=1) + '\n')


def m5_publicavel_perde_a_url_busca(base):
    caminho, d, r = _primeiro_publicavel(base, 'pecas.json')
    r['afiliado']['url_busca'] = ''
    r['afiliado']['motivo_sem_url_busca'] = None
    _gravar(caminho, d)


def m6_motivo_escrito_e_nenhuma_porta(base):
    caminho, d, r = _primeiro_publicavel(base, 'modelos-robo.json')
    r['afiliado']['url_busca'] = ''
    r['afiliado']['url_busca_produto'] = ''
    r['afiliado']['url'] = ''
    r['afiliado']['motivo_sem_url_busca'] = 'a API nao devolveu anuncio para este item'
    _gravar(caminho, d)


def m7_excluido_do_banco_continua_sem_piso(base):
    """A UNICA mutacao desta bateria que exige APROVACAO.

    Ela nao muda nada: ela afirma que o mundo de HOJE — tres pecas e cinco
    modelos `excluido_do_banco`/`nao_publicavel` com `url_busca` vazia — passa
    pelo portao. E a direcao que a errata de 16/10 exige por escrito, e sem ela
    a proxima execucao "consertaria" o que a errata anulou."""
    caminho = os.path.join(base, 'dados', 'pecas.json')
    with io.open(caminho, encoding='utf-8') as f:
        d = json.load(f)
    sem_piso = [r['id'] for r in d['registros']
                if r.get('status') != 'publicavel'
                and not ((r.get('afiliado') or {}).get('url_busca') or '').strip()]
    if not sem_piso:
        raise AssertionError('nenhum registro excluido do banco sem url_busca: a '
                             'afirmacao de nao-mordida seria inerte. PLANTE um aqui.')


MUTACOES = [
    ('o `author` sai do array do A2',
     'e o defeito de 16/10 tal e qual estava no ar',
     m1_a2_perde_o_author, PORTAO_AUTOR, True),
    ('o `author` sai do array do A1',
     'o portao julga as DUAS paginas, nao uma lista de uma',
     m2_a1_perde_o_author, PORTAO_AUTOR, True),
    ('o `author` vira uma pessoa que esta ilha nao tem',
     'sem rosto e decisao escrita do VOZ.md; autor inventado contradiz a pagina /sobre/',
     m3_author_vira_pessoa, PORTAO_AUTOR, True),
    ('o retrato dos filtros deixa de ser reposto entre alvos',
     'o portao passa a afirmar sobre pagina errada, creditando o Article do vizinho',
     m4_filtro_vaza_entre_alvos, PORTAO_AUTOR, True),
    ('um registro PUBLICAVEL perde a `url_busca`',
     'e a porta de tras pela qual 22 dos 95 entraram sem piso em 18/09/2026',
     m5_publicavel_perde_a_url_busca, PORTAO_BANCO, True),
    ('motivo escrito e NENHUMA porta de compra',
     'o motivo explica a falta do link encurtado; ele nao cria porta de compra',
     m6_motivo_escrito_e_nenhuma_porta, PORTAO_BANCO, True),
    ('registro `excluido_do_banco` sem `url_busca` NAO pode reprovar',
     'reprovar aqui faria a proxima execucao gravar link de peca de aspirador vertical',
     m7_excluido_do_banco_continua_sem_piso, PORTAO_BANCO, False),
]


def main():
    print('Robometria — autor do artigo e piso da 25.2 (despacho de 16/10)\n')
    certas = 0
    for titulo, porque, mutar, portao, espera_falha in MUTACOES:
        base = tempfile.mkdtemp(prefix='rbm-autor-')
        alvo = os.path.join(base, 'ilha')
        shutil.copytree(RAIZ, alvo)
        try:
            mutar(alvo)
        except AssertionError as e:
            print('  INERTE %-58s %s' % (titulo[:58], e))
            shutil.rmtree(base, ignore_errors=True)
            continue
        if portao.endswith('.php'):
            cmd = ['php', os.path.join(alvo, portao), alvo]
        else:
            cmd = ['python3', os.path.join(alvo, portao)]
        saida = subprocess.run(cmd, capture_output=True, text=True, cwd=alvo)
        falhou = saida.returncode != 0
        acertou = falhou == espera_falha
        if espera_falha:
            # O VEREDITO VERMELHO NAO TEM A MESMA PALAVRA NOS DOIS PORTOES, e
            # contar "FALHA" nos dois imprimia "0 falha(s)" num portao que
            # reprovou — numero errado ao lado de veredito certo, que e a forma
            # mais barata de alguem deixar de confiar na saida. O
            # teste-artigo-com-autor.php imprime "  FALHA" por afirmacao; o
            # validar-banco.py junta tudo em "REPROVADO — N invariante(s)".
            achado = re.search(r'REPROVADO — (\d+) invariante', saida.stdout)
            quantas = int(achado.group(1)) if achado else saida.stdout.count('  FALHA')
            detalhe = ('%d %s em %s' % (quantas,
                                        'invariante(s)' if achado else 'falha(s)',
                                        os.path.basename(portao))
                       if falhou else 'a trava NAO pegou')
        else:
            detalhe = ('aprovado, como tem de ser' if not falhou
                       else 'REPROVOU o mundo certo')
        print('  %s %-58s %s' % ('ok    ' if acertou else 'ERRADO', titulo[:58], detalhe))
        if not acertou:
            print('         %s' % porque)
        certas += 1 if acertou else 0
        shutil.rmtree(base, ignore_errors=True)

    print('\n%d de %d mutacoes decididas certo pela bancada.' % (certas, len(MUTACOES)))
    return 0 if certas == len(MUTACOES) else 1


if __name__ == '__main__':
    sys.exit(main())
