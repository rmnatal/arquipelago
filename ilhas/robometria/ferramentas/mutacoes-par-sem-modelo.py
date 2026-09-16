#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escreve de volta o defeito do par com `modelo` null e exige REPROVACAO.

    python3 ferramentas/mutacoes-par-sem-modelo.py

POR QUE ESTE ARQUIVO EXISTE
---------------------------
"A PROVA DE QUE UMA TRAVA REPROVA E PARTE DO BLOCO" (secao 8 do ARQUIPELAGO.md).

O DEFEITO, achado em 13/09/2026 na leva de pecas da Xiaomi. O esquema desta ilha
diz, com estas palavras, que `compatibilidade[].modelo` e "ref MODELO_ROBO.id, ou
null quando o codigo aparece na declaracao mas o modelo ainda nao esta no banco".
Ate aquele dia o banco NAO TINHA UM UNICO PAR ASSIM — zero, medido —, e duas
reguas do gerador do artigo-ancora A1 foram escritas como se o null nao pudesse
existir:

  1. `marcas_atendidas` resolvia o modelo desconhecido para a marca "?" e a
     contava. A PRIMEIRA peca com um par null fazia `atravessa_marca` virar
     verdadeiro sozinha — e `pecas_que_atravessam_marca` e o numero que escolhe
     entre as DUAS formas da frase de abertura do A1, cuja tese e que nao existe
     peca universal. Com as oito pecas novas, o gerador anunciou "4 pecas
     atravessam marca" e mandou reescrever o artigo. Nenhuma atravessa.
  2. A dispersao montava o conjunto com ids de MODELO. Num frozenset, os varios
     nulls de uma peca viram UM elemento so, e duas pecas de conjuntos declarados
     diferentes (a B112-ZS, de E10/E12/E10C/S20, e a B112-CH, de E10/E10C/S20)
     passam a contar como o mesmo conjunto. O numero encolhe em silencio — e ele
     e publicado como prova de que compatibilidade nao se herda de uma peca para
     a seguinte.

E a mesma familia que esta ilha ja nomeou duas vezes: "categoria nova herda a
regua da antiga em silencio" e "regua que depende de um caso raro do banco morre
no dia em que o banco melhora". Aqui e o contrario do segundo: a regua dependia
de um caso que NUNCA tinha acontecido, e nasceu errada sem poder falhar.

A regua passou a ser o CODIGO DECLARADO, que existe em todo par por exigencia do
esquema e nunca e null, nos dois lados e em tres contas independentes.

O QUE CADA MUTACAO TEM DE FAZER: reprovar. A (4) e a que importa — ela quebra o
gerador E o teste juntos, entao a comparacao "as duas contas batem" fica VERDE, e
so a terceira conta pega.
"""

import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GERADOR = 'ferramentas/gerar-a1.py'
TESTE_PHP = 'ferramentas/teste-a1.php'
TESTES = ('ferramentas/teste-a1.php',)

MARCAS_CERTO = ('marcas_atendidas = sorted({marcas_dos_modelos[m] for m in modelos\n'
                '                                   if m is not None and m in marcas_dos_modelos})')
MARCAS_DEFEITO = 'marcas_atendidas = sorted({marcas_dos_modelos.get(m, "?") for m in modelos})'

DISPERSAO_CERTO = 'conjunto = frozenset(c["codigo_declarado"] for c in p.get("compatibilidade", []))'
DISPERSAO_DEFEITO = 'conjunto = frozenset(c["modelo"] for c in p.get("compatibilidade", []))'

PHP_CERTO = "\t\t$conjunto[] = $c['codigo_declarado'];"
PHP_DEFEITO = "\t\t$conjunto[] = $c['modelo'];"


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
    """Sem isto a mutacao no gerador nao chega a dados/a1-fatos.json e a trava
    mediria o arquivo de ontem — mutacao inerte com outro nome."""
    saida = subprocess.run(['python3', os.path.join(base, GERADOR), '--gravar'],
                           capture_output=True, text=True, cwd=base)
    if saida.returncode != 0:
        raise AssertionError('gerar-a1.py falhou depois da mutacao: %s' % saida.stderr[-200:])


def _plantar_par_null(base):
    """PRODUZ O MUNDO que esta bateria mede, em vez de torcer para o banco o ter.

    ATE 16/09/2026 ELA NAO FAZIA ISSO, E O PRECO VENCEU NO MESMO DIA. A bateria
    nasceu em 13/09 medindo um defeito real: o banco tinha pares com `modelo`
    null — codigos que o fabricante declarava e que ainda nao tinham registro de
    modelo — e o gerador do A1 os contava como uma segunda marca. A mutacao
    reescrevia o gerador de volta ao defeito e o teste reprovava, porque havia
    nulls no banco para o defeito morder.

    Em 16/09/2026 os cinco modelos Xiaomi que faltavam (E10C, E12, S12, S40 Pro,
    X20) entraram no banco e os NOVE pares null viraram zero. A mutacao continuou
    rodando, continuou aplicando o defeito, e passou a ser INERTE: sem null no
    banco, o gerador com defeito produz exatamente o mesmo numero que o gerador
    certo. A bancada disse "PASSOU — a trava NAO pegou", e a trava esta la,
    inteira e funcionando.

    E a familia que o docstring deste arquivo ja nomeava, virada do avesso:
    "regua que depende de um caso raro do banco morre no dia em que o banco
    melhora". Ela morreu de melhora — que e a unica morte que da para prever e,
    por isso mesmo, a que nao tem desculpa.

    Entao a mutacao passa a PLANTAR o par null antes de aplicar o defeito. O
    mundo deixa de ser sorteado pelo estado da coleta.
    """
    import json
    caminho = os.path.join(base, 'dados/pecas.json')
    with open(caminho, encoding='utf-8') as f:
        banco = json.load(f)
    for r in banco['registros']:
        if r['id'] == 'xiaomi-b112-zs':
            r['compatibilidade'].append({
                'modelo': None,
                'codigo_declarado': 'E14',
                'variante_de_hardware': None,
                'selo': 'declarada_fabricante',
                'fonte': list(r['fontes'])[0],
            })
            break
    else:
        raise AssertionError('xiaomi-b112-zs sumiu — a mutacao seria inerte')
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(banco, f, ensure_ascii=False, indent=1)
        f.write('\n')


def _marca_do_null(base):
    """O defeito 1: modelo desconhecido contado como uma segunda marca."""
    _plantar_par_null(base)
    _troca(base, GERADOR, MARCAS_CERTO, MARCAS_DEFEITO)
    _regerar(base)


def _mundo_novo_intacto(base):
    """A OUTRA METADE, e ela tem de PASSAR.

    Plantar o par null e aplicar NENHUM defeito. Se esta bateria reprovasse aqui,
    a trava estaria reprovando o mundo sadio — ou seja, o banco nao poderia mais
    receber um codigo declarado sem registro de modelo, que e justamente o que o
    esquema permite e o que a coleta faz toda semana.
    """
    _plantar_par_null(base)
    _regerar(base)


def _dispersao_por_modelo(base):
    """O defeito 2, so no gerador."""
    _plantar_par_null(base)
    _troca(base, GERADOR, DISPERSAO_CERTO, DISPERSAO_DEFEITO)
    _regerar(base)


def _dispersao_por_modelo_so_no_php(base):
    """O mesmo defeito, do lado de quem confere."""
    _plantar_par_null(base)
    _regerar(base)
    _troca(base, TESTE_PHP, PHP_CERTO, PHP_DEFEITO)


def _dispersao_nos_dois_lados(base):
    """PRODUZ O MUNDO. Gerador e teste erram juntos, entao a afirmacao que
    compara as duas contas fica verde e o numero publicado encolhe sem que nada
    discorde. So a terceira conta — a que le codigo declarado e compara com o
    que foi PUBLICADO — pega."""
    _plantar_par_null(base)
    _troca(base, GERADOR, DISPERSAO_CERTO, DISPERSAO_DEFEITO)
    _troca(base, TESTE_PHP, PHP_CERTO, PHP_DEFEITO)
    _regerar(base)


def _par_sem_codigo_declarado(base):
    """A PORTA DOS FUNDOS PELO DADO, e nao pelo codigo. A regua nova se apoia em
    `codigo_declarado` existir em todo par. Se um par perder o codigo, o conjunto
    daquela peca encolhe em silencio e nenhuma das contas por codigo discorda da
    outra — as tres passam a contar a mesma coisa errada. E o ramo
    `__sem_codigo__` da terceira conta que existe para isto, e ate 13/09/2026 ele
    nunca tinha sido visto reprovando.

    Ela apaga o codigo de UM par da peca de maior alcance, que e a mesma peca
    que o artigo cita pelo nome na frase do maior alcance declarado."""
    import json
    caminho = os.path.join(base, 'dados/pecas.json')
    with open(caminho, encoding='utf-8') as f:
        banco = json.load(f)
    mexeu = False
    for r in banco['registros']:
        if r['id'] == 'multi-pr10124':
            r['compatibilidade'][0]['codigo_declarado'] = ''
            mexeu = True
    if not mexeu:
        raise AssertionError('multi-pr10124 nao esta mais no banco — a mutacao seria inerte')
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(banco, f, ensure_ascii=False, indent=1)
        f.write('\n')
    _regerar(base)


MUTACOES = [
    (
        'MUNDO NOVO intacto: o par null plantado e NENHUM defeito',
        'esta TEM de passar — se reprovar, a trava esta barrando o que o esquema permite',
        _mundo_novo_intacto,
        'passa',
    ),
    (
        'o modelo null volta a contar como a marca "?"',
        'o defeito original: a primeira peca com par null faz a tese do A1 trocar de forma sozinha',
        _marca_do_null,
    ),
    (
        'a dispersao do GERADOR volta a contar por id de modelo',
        'os nulls de uma peca colapsam num elemento so e duas pecas viram o mesmo conjunto',
        _dispersao_por_modelo,
    ),
    (
        'a dispersao do TESTE volta a contar por id de modelo',
        'o mesmo defeito do lado de quem confere — aqui quem pega e a comparacao entre as duas contas',
        _dispersao_por_modelo_so_no_php,
    ),
    (
        'gerador e teste voltam a contar por id de modelo, JUNTOS',
        'PRODUZ O MUNDO: as duas contas concordam, o numero publicado encolhe, e sem a terceira conta isto desembarcaria',
        _dispersao_nos_dois_lados,
    ),
    (
        'um par perde o codigo declarado no banco',
        'a porta dos fundos pelo DADO: as tres contas passam a contar a mesma coisa errada, e quem pega e o ramo __sem_codigo__',
        _par_sem_codigo_declarado,
    ),
]


def main():
    reprovadas = 0
    passaram = []

    print('Mutacoes deliberadas no par sem modelo — cada uma TEM que reprovar\n')

    for entrada in MUTACOES:
        # A bateria passou a ter DOIS tipos de linha em 16/09/2026: as que tem de
        # reprovar (o normal) e a do MUNDO NOVO INTACTO, que tem de passar. Sem a
        # segunda, plantar o par null so mostraria que a trava morde — e nao que
        # ela morde apenas o defeito.
        nome, porque, aplicar = entrada[0], entrada[1], entrada[2]
        espera = entrada[3] if len(entrada) > 3 else 'reprova'
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
            for teste in TESTES:
                cmd = ['php', os.path.join(base, teste), base]
                saida = subprocess.run(cmd, capture_output=True, text=True)
                if saida.returncode != 0:
                    pegou_em.append(os.path.basename(teste))
                    falhas += [l.strip() for l in saida.stdout.splitlines()
                               if l.strip().startswith(('FALHA', 'ERRO'))]

            if espera == 'passa':
                if pegou_em:
                    print('  REPROVOU %-60s <- o mundo SADIO foi reprovado' % nome)
                    print('         (%s)' % porque)
                    for l in falhas[:2]:
                        print('         %s' % l[:120])
                    passaram.append(nome)
                else:
                    print('  ok     %-62s mundo sadio passou' % nome)
                    reprovadas += 1
                continue

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
        sys.exit(1)


if __name__ == '__main__':
    main()
