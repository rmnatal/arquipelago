#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O `dateModified` que a ilha publica esta atrasado em relacao ao git?

    python3 ferramentas/validar-datas-das-paginas.py
    python3 ferramentas/validar-datas-das-paginas.py --autoteste

O DEFEITO QUE ELE FECHA — item 2 do despacho da Sentinela de 23/10/2026
------------------------------------------------------------------------
Medido no JSON-LD servido em 23/10/2026: `/filtro-universal-de-robo-aspirador/` e
`/quantos-m2-o-robo-aspirador-limpa-por-carga/` serviam `dateModified:
2026-09-21`. O bloco do molde de conversao de 21/10 reescreveu NOVE paginas desta
ilha — casca 1.13.0, R1 1.12.0, R2 1.10.0, A1 1.6.0, A2 1.6.0, malha 1.1.0 — e
nao rodou `ferramentas/gerar-datas-das-paginas.py`. Os sete registros de
`dados/datas-das-paginas.json` ficaram em 2026-09-21, um mes atras.

O cabecalho do `robometria-casca.php` ja diz por que isto importa: *"ausente o
Google infere, errada ele acredita — e o campo existe justamente para ele decidir
se vale reindexar"*. Uma ilha que acabou de trocar o molde de nove paginas e
exatamente a que mais precisa do contrario.

E O MOTIVO DE NINGUEM TER PEGADO ESTA ESCRITO, COM TODAS AS LETRAS, DENTRO DO
PORTAO QUE DEVIA PEGAR. `ferramentas/validar-derivados.py` ISENTA este arquivo,
na lista `NAO_RECONSTRUIVEIS`, com esta justificativa:

    'derivado do HISTORICO do git (data do ultimo commit de cada arquivo),
     entao ele muda a cada commit por desenho — comparar com o disco
     reprovaria toda vez que alguem commitasse, que e verde barato ao
     contrario'

A analise esta certa para a comparacao que aquele portao faz — BYTE A BYTE do
documento inteiro, `gerado_em` incluido, e `gerado_em` e a data em que o gerador
RODOU. Mas a isencao foi escrita para um arquivo e virou isencao para a PERGUNTA:
desde 16/09 ninguem mais pergunta se a data publicada e a data do git. **Isencao
de regua e divida escrita, e esta venceu em 21/10.** O conserto nao e tirar a
isencao: e fazer a pergunta certa.

A PERGUNTA CERTA, E ELA NAO REPROVA POR COMMITAR
-------------------------------------------------
Este portao compara so o que e FUNCAO DO GIT — `modificada_em`, `modificada_por`
e a data por arquivo —, nunca `gerado_em`. E usa o PROPRIO gerador para
recalcular: importa `PAGINAS` e `data_do_arquivo()` dele, em vez de reescrever o
mapa de pagina para arquivo. Duas listas escritas a mao da mesma coisa e a
familia de defeito que esta ilha ja pagou quatro vezes; aqui havia como nao
pagar a quinta.

Com isso ele fica VERDE no caminho normal do trabalho — a execucao que mexe numa
pagina roda o gerador antes de commitar, e o gerador conta arquivo nao commitado
como HOJE, de proposito — e fica VERMELHO exatamente no mundo de 21/10: arquivo
de pagina mudou e a data publicada ficou para tras.

QUANDO ELE REPROVAR, O CONSERTO E UM COMANDO:

    python3 ferramentas/gerar-datas-das-paginas.py --gravar
"""

import argparse
import importlib.util
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARQUIVO = 'dados/datas-das-paginas.json'


def _carregar_gerador():
    """O gerador tem traco no nome e nao se importa por `import`. Carregar pelo
    caminho e o que permite ter UM mapa de pagina para arquivo no lugar de dois."""
    caminho = os.path.join(RAIZ, 'ferramentas', 'gerar-datas-das-paginas.py')
    spec = importlib.util.spec_from_file_location('gerar_datas_das_paginas', caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


# ---------------------------------------------------------------- a medicao
def medir(gerador, doc, hoje):
    """Devolve a lista de divergencias entre o publicado e o que o git diz.

    Compara SO o que e funcao do git. `gerado_em` fica fora por desenho: ele mede
    quando o gerador rodou, e cobrar isso aqui seria reprovar por commitar — que
    e o erro que a isencao do validar-derivados.py evitou e esta regua nao
    repete.
    """
    publicados = {r['slug']: r for r in doc.get('registros', [])}
    problemas = []

    faltando = sorted(set(gerador.PAGINAS) - set(publicados))
    for slug in faltando:
        problemas.append('%s: a pagina existe no gerador e NAO esta no arquivo '
                         'publicado' % slug)
    sobrando = sorted(set(publicados) - set(gerador.PAGINAS))
    for slug in sobrando:
        problemas.append('%s: esta no arquivo publicado e nao existe mais no '
                         'gerador' % slug)

    for slug in sorted(set(gerador.PAGINAS) & set(publicados)):
        cfg = gerador.PAGINAS[slug]
        reg = publicados[slug]
        por_arquivo = {}
        for rel in cfg['arquivos']:
            data, _como = gerador.data_do_arquivo(rel, hoje)
            por_arquivo[rel] = data
        esperado = max(por_arquivo.values())
        tido = reg.get('modificada_em')
        if tido != esperado:
            qual = 'ATRASADA' if (tido or '') < esperado else 'ADIANTADA'
            problemas.append(
                '%s: modificada_em publicada %s, o git diz %s (%s) — %s'
                % (slug, tido, esperado, qual,
                   ', '.join('%s %s' % (os.path.basename(k), v)
                             for k, v in sorted(por_arquivo.items()))))
            continue
        esperado_por = sorted(k for k, v in por_arquivo.items() if v == esperado)
        if sorted(reg.get('modificada_por') or []) != esperado_por:
            problemas.append('%s: modificada_por publicada %s, o git diz %s'
                             % (slug, reg.get('modificada_por'), esperado_por))
        for rel, data in sorted(por_arquivo.items()):
            tida = ((reg.get('arquivos') or {}).get(rel) or {}).get('data')
            if tida != data:
                problemas.append('%s/%s: data publicada %s, o git diz %s'
                                 % (slug, rel, tida, data))
    return problemas


# ------------------------------------------------------------- o autoteste
class _GeradorFalso(object):
    """Um gerador de mentira, para a regua ser medida sem tocar no git."""

    def __init__(self, paginas, datas):
        self.PAGINAS = paginas
        self._datas = datas

    def data_do_arquivo(self, rel, hoje):
        return self._datas[rel], 'commit'


def autoteste():
    """SEIS MUNDOS, e o primeiro e o de 21/10/2026 — o que esteve no ar."""
    paginas = {
        'pagina-a': {'arquivos': ['snippets/casca.php', 'dados/fatos.json']},
    }
    datas = {'snippets/casca.php': '2026-10-21', 'dados/fatos.json': '2026-09-18'}

    def doc(**campos):
        base = {'slug': 'pagina-a', 'modificada_em': '2026-10-21',
                'modificada_por': ['snippets/casca.php'],
                'arquivos': {'snippets/casca.php': {'data': '2026-10-21'},
                             'dados/fatos.json': {'data': '2026-09-18'}}}
        base.update(campos)
        return {'registros': [base]}

    casos = [
        ('MUNDO DE 21/10: a casca mudou e a data publicada ficou um mes atras',
         doc(modificada_em='2026-09-21', modificada_por=['dados/fatos.json'],
             arquivos={'snippets/casca.php': {'data': '2026-09-21'},
                       'dados/fatos.json': {'data': '2026-09-18'}}), False),
        ('mundo sadio: a data publicada e a do git',
         doc(), True),
        ('data ADIANTADA — alguem digitou o campo a mao',
         doc(modificada_em='2026-11-30'), False),
        ('a data esta certa e `modificada_por` nomeia o arquivo errado',
         doc(modificada_por=['dados/fatos.json']), False),
        ('a data da pagina esta certa e a de um arquivo dela, nao',
         doc(arquivos={'snippets/casca.php': {'data': '2026-10-21'},
                       'dados/fatos.json': {'data': '2026-10-21'}}), False),
        ('pagina que o gerador conhece e o arquivo publicado nao tem',
         {'registros': []}, False),
    ]

    falso = _GeradorFalso(paginas, datas)
    erros = []
    print('AUTOTESTE — %d mundos' % len(casos))
    for nome, documento, tem_de_passar in casos:
        problemas = medir(falso, documento, '2026-10-23')
        passou = not problemas
        if passou == tem_de_passar:
            print('  ok     %-66s %s' % (nome[:66],
                                         'sem divergencia' if passou
                                         else problemas[0][:60]))
        else:
            erros.append(nome)
            print('  ERRADO %-66s %s' % (nome[:66], problemas[0][:60] if problemas
                                         else 'aprovou'))
    if erros:
        print('\nREPROVADO: a regua nao decide certo em %d mundo(s).' % len(erros))
        return 1
    print('\nAPROVADO: %d de %d mundos decididos certo.' % (len(casos), len(casos)))
    return 0


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--autoteste', action='store_true')
    args = p.parse_args()
    if args.autoteste:
        return autoteste()

    # PORTAO ZERO: a regua se mede ANTES de medir a ilha, sempre, como a
    # `bancada.py` desta ilha faz com a regua que julga os portoes. Regua que so
    # e conferida quando alguem lembra de passar `--autoteste` nao e conferida —
    # e esta nasceu justamente de uma isencao que ninguem reabriu em 37 dias.
    if autoteste() != 0:
        print('\nA REGUA FALHOU ANTES DE MEDIR A ILHA. Nada abaixo vale.')
        return 1
    print()

    gerador = _carregar_gerador()
    with open(os.path.join(RAIZ, ARQUIVO), encoding='utf-8') as fh:
        doc = json.load(fh)
    from datetime import date
    problemas = medir(gerador, doc, date.today().isoformat())
    if problemas:
        print('REPROVADO: %s nao bate com o git em %d ponto(s).'
              % (ARQUIVO, len(problemas)))
        for linha in problemas:
            print('  - %s' % linha)
        print('\nO conserto e um comando:\n'
              '    python3 ferramentas/gerar-datas-das-paginas.py --gravar')
        return 1
    print('APROVADO: as %d paginas publicam a data que o git mede.'
          % len(doc.get('registros', [])))
    return 0


if __name__ == '__main__':
    sys.exit(main())
