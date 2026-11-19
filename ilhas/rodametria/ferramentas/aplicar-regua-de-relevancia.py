#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REAPLICA A REGUA DE RELEVANCIA SOBRE O BANCO JA COLHIDO, E E A PROVA DA 25.9.

    python3 ferramentas/aplicar-regua-de-relevancia.py --conferir
    python3 ferramentas/aplicar-regua-de-relevancia.py            # o laudo, sem gravar
    python3 ferramentas/aplicar-regua-de-relevancia.py --gravar

POR QUE ELA EXISTE. A 25.9 fecha com uma exigencia que nao e "os testes
passaram": *"rodar a regua ANTIGA sobre o banco ANTIGO e a NOVA sobre o NOVO,
registro por registro, e contar quantos (...) vereditos mudaram"*, porque
*"regua afrouxada apareceria aqui como verdadeiro novo em registro que nao tinha
nada a ganhar"*. Sem uma ferramenta, essa conta e feita a mao uma vez, no dia do
conserto, e nunca mais — e a regua seguinte muda sem ninguem refazer a conta.

E ELA NAO GUARDA COPIA DA REGUA ANTIGA, que seria a maneira obvia e errada de
fazer isto (duas declaracoes do mesmo fato comecam iguais e so uma sobe, 20.7).
A trava nova de 16/11/2026 e DECLARADA na consulta
(`recusa_cabeca_de_outra_familia`), entao a regua antiga e a MESMA FUNCAO com a
declaracao vazia — `rel.julgar_declaracao(titulo, familia,
sem_cabeca_de_outra_familia=True)`. No dia em que a trava mudar de forma, esta
ferramenta deixa de medir a diferenca em vez de medir a diferenca errada.

O QUE ELA GRAVA: `serve`, `recusado_por`, `exigencia_que_faltou` e
`exigencias_atendidas` de cada anuncio, e depois chama `recontar_resumo` do
COLETOR — que e o dono do arquivo — para refazer o que serve HOJE. As contagens
de coleta (`ofertas_lidas`, `ofertas_recusadas`, `recusas_por_causa`) NAO sao
tocadas: elas sao fato do dia em que a coleta aconteceu, como a 25.11 ja decidiu
para a quarentena.

ELA NAO COLHE NADA e nao toca a rede. Reaplicar regua sobre o banco colhido e
diferente de colher de novo: a coleta le a loja HOJE e troca o conjunto de
ofertas; esta aqui responde "o que a regua de hoje diria das ofertas que ja
estao no banco", que e a unica pergunta que a 25.9 manda responder.

O PORTAO (`--conferir`) COBRA A ASSIMETRIA, e nao a igualdade: toda divergencia
entre a regua antiga e a nova tem de ser no sentido `serve: True -> False`.
Nunca `False -> True` (isso seria afrouxamento) e nunca troca de NOME de uma
recusa que ja existia (isso seria a trava nova roubando a recusa de outra, e e
por isso que ela e a ultima a decidir dentro do `julgar`).
"""

import argparse
import importlib.util
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FERRAMENTAS = os.path.join(RAIZ, 'ferramentas')
BANCO = os.path.join(RAIZ, 'dados', 'anuncios-por-consulta.json')

# O RECUO DO BANCO SAI DA CONSTANTE DO COLETOR, NUNCA DE UM NUMERO AQUI
# (19/11/2026). Medido: `aplicar-foto-quebrada.py` gravava com `indent=2` e o
# `RECUO_DO_BANCO` do `coletar-por-consulta.py` e **1**. Como foi aquela
# ferramenta que escreveu o banco em 18/11, o arquivo em disco ficou com recuo
# 2 — e a passada seguinte que gravasse por qualquer outro caminho reescrevia
# **2.100 linhas so de recuo**, com a mudanca de verdade escondida dentro
# delas. Diff que some com o que mudou e a familia do instrumento que some com
# o que tentou, medido nesta ilha na manha do mesmo dia. Duas declaracoes do
# mesmo fato comecam iguais e so uma sobe (20.7), e aqui eram CINCO.
def _recuo_do_banco():
    caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'coletar-por-consulta.py')
    espec = importlib.util.spec_from_file_location('coletar_por_consulta_recuo', caminho)
    mod = importlib.util.module_from_spec(espec)
    espec.loader.exec_module(mod)
    return mod.RECUO_DO_BANCO


def _modulo(nome, caminho):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


rel = _modulo('relevancia', os.path.join(FERRAMENTAS, 'teste-relevancia-do-anuncio.py'))
col = _modulo('coletor_por_consulta', os.path.join(FERRAMENTAS, 'coletar-por-consulta.py'))


def carregar():
    with open(BANCO, encoding='utf-8') as f:
        return json.load(f)


def familias():
    """A declaracao de cada consulta, pelo id — lida do dono dela."""
    return {c['id']: c for c in col.declaracao()['consultas']}


def comparar(banco, decl):
    """Devolve (linhas, divergencias). Nao grava nada.

    `linhas` e uma linha por anuncio, com o veredito das DUAS reguas; e
    `divergencias` so as que mudaram, que e o numero que a 25.9 pede.
    """
    linhas, divergencias = [], []
    for bloco in banco['consultas']:
        c = decl.get(bloco['id'])
        if not c or not c.get('familia'):
            continue
        f = c['familia']
        for a in bloco['anuncios']:
            antigo = rel.julgar_declaracao(a['titulo'], f,
                                           sem_cabeca_de_outra_familia=True)
            novo = rel.julgar_declaracao(a['titulo'], f)
            reg = {
                'consulta': bloco['id'],
                'item_id': a['item_id'],
                'titulo': a['titulo'],
                'gravado': (a['serve'], a['recusado_por'], a['exigencia_que_faltou']),
                'antigo': antigo[:3],
                'novo': novo[:3],
                'novo_completo': novo,
            }
            linhas.append(reg)
            if antigo[:3] != novo[:3]:
                divergencias.append(reg)
    return linhas, divergencias


def laudo(gravar=False):
    banco = carregar()
    decl = familias()
    linhas, divergencias = comparar(banco, decl)

    print('A PROVA DA 25.9 — regua ANTIGA (sem a trava da cabeca) contra a NOVA,')
    print('anuncio por anuncio, sobre os %d anuncios do banco:\n' % len(linhas))
    for bid in sorted({l['consulta'] for l in linhas}):
        da_consulta = [l for l in linhas if l['consulta'] == bid]
        muda = [l for l in da_consulta if l in divergencias]
        f = decl[bid]['familia']
        print('  %-20s %2d anuncios | substantivo %-10s | cabeca barrada %s'
              % (bid, len(da_consulta), repr(f.get('substantivo')),
                 f.get('recusa_cabeca_de_outra_familia')))
        print('  %-20s %2d veredito(s) mudado(s)' % ('', len(muda)))
        for l in muda:
            print('      %s  %s' % (l['item_id'], l['titulo'][:78]))
            print('        antiga: serve=%s %s/%s' % l['antigo'])
            print('        nova:   serve=%s %s/%s' % l['novo'])
    print('\n%d de %d vereditos mudaram.' % (len(divergencias), len(linhas)))

    # A ASSIMETRIA, IMPRESSA ANTES DE QUALQUER GRAVACAO.
    afrouxou = [l for l in divergencias if l['novo'][0] and not l['antigo'][0]]
    relabel = [l for l in divergencias
               if not l['antigo'][0] and not l['novo'][0]]
    print('afrouxamentos (serve False -> True): %d' % len(afrouxou))
    print('recusas renomeadas (False -> False, outro nome): %d' % len(relabel))
    if afrouxou or relabel:
        print('REPROVADO: a trava nova so pode tirar o que passava.')
        return 1

    # O QUE ESTA GRAVADO NO BANCO HOJE tem de ser a regua ANTIGA (se nada foi
    # reaplicado ainda) ou a NOVA (se ja foi). Qualquer outra coisa e banco
    # fora das duas reguas, e isso e defeito que esta ferramenta nao conserta.
    fora = [l for l in linhas
            if l['gravado'] != l['antigo'] and l['gravado'] != l['novo']]
    if fora:
        print('\nREPROVADO: %d anuncio(s) com veredito gravado que nao e nem o da '
              'regua antiga nem o da nova:' % len(fora))
        for l in fora[:10]:
            print('   %s / %s: gravado %s | antiga %s | nova %s'
                  % (l['consulta'], l['item_id'], l['gravado'], l['antigo'], l['novo']))
        return 1

    pendentes = [l for l in divergencias if l['gravado'] != l['novo']]
    print('anuncios gravados com a regua VELHA, a reaplicar: %d' % len(pendentes))

    if not gravar:
        if pendentes:
            print('\nnada gravado (rode outra vez com --gravar).')
        return 0

    if not pendentes:
        print('\nnada a gravar: o banco ja esta na regua nova.')
        return 0

    for bloco in banco['consultas']:
        mudou = False
        for a in bloco['anuncios']:
            l = next((x for x in pendentes
                      if x['consulta'] == bloco['id'] and x['item_id'] == a['item_id']), None)
            if not l:
                continue
            serve, por, faltou, atendidas = l['novo_completo']
            print('  %s / %s: serve %s -> %s, recusado_por %r -> %r'
                  % (bloco['id'], a['item_id'], a['serve'], serve, a['recusado_por'], por))
            a['serve'], a['recusado_por'] = serve, por
            a['exigencia_que_faltou'], a['exigencias_atendidas'] = faltou, atendidas
            mudou = True
        if mudou:
            antes = dict(bloco['resumo'])
            col.recontar_resumo(bloco)
            for campo in sorted(bloco['resumo']):
                if antes.get(campo) != bloco['resumo'][campo]:
                    print('  %s / resumo.%s: %r -> %r'
                          % (bloco['id'], campo, antes.get(campo), bloco['resumo'][campo]))
            print('  %s: `ofertas_lidas`, `ofertas_recusadas` e `recusas_por_causa` NAO '
                  'mudam — sao fato da coleta de %s.' % (bloco['id'], bloco.get('colhido_em')))

    with open(BANCO, 'w', encoding='utf-8') as f:
        json.dump(banco, f, ensure_ascii=False, indent=_recuo_do_banco())
        f.write('\n')
    print('\ngravado em %s' % os.path.relpath(BANCO, RAIZ))
    print('AGORA RODE: python3 ferramentas/coletar-por-consulta.py --conferir')
    print('         E: python3 ferramentas/gerar-vitrine-de-produto.py --gravar')
    return 0


def conferir():
    if not os.path.exists(BANCO):
        print('REPROVADO: %s nao existe' % os.path.basename(BANCO))
        return 1
    banco = carregar()
    decl = familias()
    linhas, divergencias = comparar(banco, decl)
    falhas, afirmacoes = [], 0

    for l in divergencias:
        afirmacoes += 1
        if l['novo'][0] and not l['antigo'][0]:
            falhas.append('%s / %s: a regua nova AFROUXOU (serve False -> True)'
                          % (l['consulta'], l['item_id']))
        afirmacoes += 1
        if not l['antigo'][0] and not l['novo'][0]:
            falhas.append('%s / %s: a trava nova ROUBOU a recusa %r (virou %r)'
                          % (l['consulta'], l['item_id'], l['antigo'][1], l['novo'][1]))

    # E O BANCO GRAVADO TEM DE SER UMA DAS DUAS REGUAS, nunca um terceiro
    # estado: banco meio reaplicado e exatamente o que esta ferramenta existe
    # para nao deixar acontecer em silencio.
    for l in linhas:
        afirmacoes += 1
        if l['gravado'] != l['antigo'] and l['gravado'] != l['novo']:
            falhas.append('%s / %s: veredito gravado %s nao e nem a regua antiga %s nem a nova %s'
                          % (l['consulta'], l['item_id'], l['gravado'], l['antigo'], l['novo']))

    # A TRAVA TEM DE PODER FALHAR (secao 8): se a declaracao de toda consulta
    # viesse vazia, esta ferramenta mediria zero diferenca e aprovaria sempre.
    declaradas = [c['id'] for c in decl.values()
                  if c.get('familia') and c['familia'].get('recusa_cabeca_de_outra_familia')]
    afirmacoes += 1
    if not declaradas:
        falhas.append('nenhuma consulta declara `recusa_cabeca_de_outra_familia`: '
                      'este portao nao mede nada')

    for f in falhas:
        print('FALHA: ' + f)
    print('\n%d anuncio(s), %d divergencia(s), %d consulta(s) com a lista declarada.'
          % (len(linhas), len(divergencias), len(declaradas)))
    print('%d afirmacao(oes), %d falha(s).' % (afirmacoes, len(falhas)))
    print('APROVADO' if not falhas else 'REPROVADO')
    return 1 if falhas else 0


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--conferir', action='store_true', help='portao, sem rede')
    p.add_argument('--gravar', action='store_true')
    a = p.parse_args()
    if a.conferir:
        return conferir()
    return laudo(gravar=a.gravar)


if __name__ == '__main__':
    sys.exit(main())
