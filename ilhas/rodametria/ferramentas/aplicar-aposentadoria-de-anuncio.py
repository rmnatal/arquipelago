#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
APOSENTA UM ANUNCIO DE `dados/anuncios-por-consulta.json` — ITEM 1 DO DESPACHO
DA RONDA DE 11/11/2026.

    python3 ferramentas/aplicar-aposentadoria-de-anuncio.py --conferir
    python3 ferramentas/aplicar-aposentadoria-de-anuncio.py \
        --consulta patinete-eletrico --item 58212105781 \
        --causa esgotado --em 2026-11-11 \
        --causa-prosa "..." --ultima-medicao "..."            # mostra o que mudaria
    ... mais --gravar                                          # grava

O DEFEITO QUE ELE EXISTE PARA FECHAR, e ele vai acontecer de novo: a ronda de
11/11/2026 abriu a `url_produto` do cartao 2 da `/veiculos/patinete-eletrico/` e
a Shopee serviu a palavra `Esgotado` colada ao titulo, nas DUAS leituras. O
anuncio existia, abria, respondia 200 — e nao vendia. Link morto e dado do banco
(19.2), e a pagina de maior intencao de compra da ilha servia um botao que nao
vende.

POR QUE UMA FERRAMENTA E NAO UMA EDICAO A MAO. Anuncio esgotado nao e evento
raro: e o custo corrente de vender ficha de marketplace, e a 25.1 ja diz que
link de afiliado apodrece. Conserto a mao mexe em SEIS lugares do mesmo arquivo
(a lista de anuncios, tres contagens do `resumo`, o numero proprio e a prosa) e
erra calado no que nao mexer; e a proxima execucao nao tem como saber o que a
anterior fez. Esta ferramenta faz a mesma coisa sempre, IMPRIME cada troca que
faz (secao 8) e deixa o portao que prova o resultado.

A ESCOLHA DE DESENHO, E ELA E A DO PRECEDENTE DA ROBOMETRIA (02/11/2026, o
`electrolux-erb60`): o anuncio aposentado NAO fica num campo vivo. Ele sai da
lista `anuncios` e vira UMA LINHA DE PROSA em `anuncios_aposentados`, com a
historia inteira dentro — ids, loja, titulo, preco, encurtado, degrau, causa e
ultima medicao. O "pronto quando" do despacho pede exatamente isto: *"o anuncio
58212105781 tem zero ocorrencia em campo vivo do banco; e a historia do anuncio
aposentado fica inteira dentro de `motivo_sem_url_produto`, fora dos campos
vivos"*.

E A PROSA NAO E ENFEITE: ELA E A LISTA DE QUARENTENA. `coletar-por-consulta.py
--gravar` reescreve o bloco inteiro a partir da API, e sem quarentena o anuncio
esgotado VOLTA na proxima coleta, com o mesmo id, como oferta viva. Entao o
formato da linha e FECHADO e um portao o cobra:

    APOSENTADO EM <aaaa-mm-dd> — item <item_id> da loja <shop_id> — CAUSA: ... || ULTIMA MEDICAO: ...

O `item <id> da loja <id>` e o que o coletor le para recusar o anuncio de novo, e
o separador `||` e o da 25.4-b.3: a CAUSA nao muda nunca, a ULTIMA MEDICAO e
reescrita a cada passada que tentar de novo. Prosa que guarda as duas misturadas
ou cresce sem fim ou apaga a causa.

O QUE ESTA FERRAMENTA NAO FAZ, de proposito:

- **nao escolhe anuncio novo.** Quem decide quem entra no carrossel e
  `gerar-vitrine-de-produto.py`, pela ordem da secao 7 — e e so rodar depois
  desta. Aqui so SAI quem nao vende.
- **nao testa vida.** O teste de vida da Shopee nao e tarefa desta nuvem (25.4,
  e medido de novo em 11/11: o Chromium daqui abre a ficha em 200 e ela nao
  renderiza, com 23 recursos da CDN de script recusados pelo egresso). Quem mede
  e a ronda, no navegador do Raphael; esta ferramenta aplica o que foi medido, e
  por isso ela EXIGE a prosa da medicao na linha de comando em vez de inventar
  uma.
- **nao apaga contagem de coleta.** `ofertas_lidas` e `ofertas_recusadas` sao
  fatos da coleta do dia em que ela aconteceu e ficam como estao; o que muda e o
  que serve HOJE (`ofertas_que_servem`, `ofertas_com_link_de_afiliado`, o numero
  proprio) mais o campo novo `ofertas_aposentadas`. O portao exige a soma fechar:
  `ofertas_lidas == len(anuncios) + len(anuncios_aposentados)`.
"""

import argparse
import importlib.util
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANCO = os.path.join(RAIZ, 'dados', 'anuncios-por-consulta.json')
COLETOR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       'coletar-por-consulta.py')

# O FORMATO FECHADO DA LINHA, A LEITURA DOS IDS E A RECONTAGEM MORAM NO COLETOR
# (`coletar-por-consulta.py`), que e o dono deste arquivo de dados e o unico que
# o reescreve a partir da API. Aqui elas sao USADAS, nunca copiadas: duas
# declaracoes do mesmo fato comecam iguais e so uma sobe (20.7), e a copia que
# nao sobe seria justamente a que o `--gravar` da coleta le.
def carregar():
    with open(BANCO, encoding='utf-8') as f:
        return json.load(f)


def _coletor():
    """Importa o coletor para reusar `numero_proprio` e `contagem_de_rotulo`.

    A conta do numero proprio mora LA e nao e copiada para ca: duas contas do
    mesmo numero comecam iguais e so uma sobe (20.7).
    """
    spec = importlib.util.spec_from_file_location('coletor_por_consulta', COLETOR)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---------------------------------------------------------------------------
# `--conferir`: sem rede, prova o que a aposentadoria promete
# ---------------------------------------------------------------------------
def conferir():
    if not os.path.exists(BANCO):
        print('REPROVADO: %s nao existe' % os.path.basename(BANCO))
        return 1
    banco = carregar()
    col = _coletor()
    falhas, afirmacoes = [], 0

    for bloco in banco['consultas']:
        bid = bloco['id']
        apos = col.aposentados_de(bloco)
        r = bloco['resumo']

        # 1. O formato da linha e fechado, porque o coletor LE o id dela.
        for linha in apos:
            afirmacoes += 1
            if not col.PADRAO_APOSENTADO.match(linha.strip()):
                falhas.append(
                    '%s: linha de aposentadoria fora do formato fechado '
                    '(APOSENTADO EM <aaaa-mm-dd> — item <id> da loja <id> — ... '
                    'CAUSA: ... || ULTIMA MEDICAO: ...): %r' % (bid, linha[:120]))

        # 2. A contagem declarada e a lista.
        afirmacoes += 1
        if int(r.get('ofertas_aposentadas') or 0) != len(apos):
            falhas.append('%s: ofertas_aposentadas gravado %r, contado %d'
                          % (bid, r.get('ofertas_aposentadas'), len(apos)))

        # 3. A SOMA FECHA. `ofertas_lidas` e fato da coleta e nao se mexe;
        #    entao ele tem de ser o que serve hoje mais o que foi aposentado.
        afirmacoes += 1
        if int(r['ofertas_lidas']) != len(bloco['anuncios']) + len(apos):
            falhas.append(
                '%s: ofertas_lidas %d nao fecha com %d anuncio(s) + %d aposentado(s)'
                % (bid, r['ofertas_lidas'], len(bloco['anuncios']), len(apos)))

        # 4. O ID DO APOSENTADO NAO ESTA EM CAMPO VIVO — e esta e a afirmacao
        #    que o despacho pediu. Ela varre TODOS os campos de todos os
        #    anuncios vivos, nao so os quatro que a gente se lembra de olhar.
        quarentena = col.ids_em_quarentena(bloco)
        for anuncio in bloco['anuncios']:
            vivo = json.dumps(anuncio, ensure_ascii=False)
            for item_id in quarentena:
                afirmacoes += 1
                if str(item_id) in vivo:
                    falhas.append('%s: anuncio APOSENTADO %d aparece em campo vivo'
                                  % (bid, item_id))

        # 5. O numero proprio que a pagina publica REFAZ sobre quem sobrou.
        #    Sem isto a faixa de preco continuaria contando a oferta que nao
        #    existe mais, e a mediana sairia de um conjunto que ninguem pode
        #    comprar.
        num, motivo = col.numero_proprio(r.get('numero_proprio_pedido'), bloco['anuncios'])
        afirmacoes += 1
        if num != r.get('numero_proprio'):
            falhas.append('%s: numero_proprio gravado %r nao refaz sobre quem sobrou: %r'
                          % (bid, r.get('numero_proprio'), num))
        afirmacoes += 1
        if motivo != r.get('motivo_sem_numero_proprio'):
            falhas.append('%s: motivo_sem_numero_proprio gravado %r nao refaz: %r'
                          % (bid, r.get('motivo_sem_numero_proprio'), motivo))

    for f in falhas:
        print('FALHA: ' + f)
    print('\n%d afirmacao(oes), %d falha(s).' % (afirmacoes, len(falhas)))
    print('APROVADO' if not falhas else 'REPROVADO')
    return 1 if falhas else 0


# ---------------------------------------------------------------------------
def aposentar(args):
    banco = carregar()
    col = _coletor()
    bloco = None
    for b in banco['consultas']:
        if b['id'] == args.consulta:
            bloco = b
    if bloco is None:
        print('REPROVADO: consulta %r nao esta no banco' % args.consulta)
        return 1

    alvo = [a for a in bloco['anuncios'] if int(a['item_id']) == args.item]
    if not alvo:
        if args.item in col.ids_em_quarentena(bloco):
            print('nada a fazer: o item %d JA esta aposentado nesta consulta' % args.item)
            return 0
        print('REPROVADO: item %d nao esta nos anuncios de %s' % (args.item, args.consulta))
        return 1
    a = alvo[0]

    linha = ('APOSENTADO EM %s — item %d da loja %d — %s — R$ %s, preco de %s, '
             'degrau %s da escada de chaves, encurtado %s, loja "%s" — CAUSA: %s '
             '|| ULTIMA MEDICAO: %s'
             % (args.em, int(a['item_id']), int(a['shop_id']), a['titulo'].strip(),
                (('%.2f' % a['preco']).replace('.', ',')) if a.get('preco') is not None
                else 'sem preco',
                a.get('coletado_em'), a.get('degrau_da_escada'),
                a.get('url_afiliado') or 'sem encurtado', a.get('loja'),
                args.causa_prosa.strip(), args.ultima_medicao.strip()))

    if not col.PADRAO_APOSENTADO.match(linha):
        print('REPROVADO: a linha montada nao casa com o formato fechado. '
              'Nenhuma troca feita.')
        print(linha)
        return 1

    # AS TROCAS, TODAS IMPRESSAS (secao 8).
    print('APOSENTANDO item %d da consulta %s, causa %r:' % (args.item, args.consulta, args.causa))
    print('  - sai da lista `anuncios`: %s' % a['titulo'][:70])
    print('  - sai o encurtado que ia para o leitor: %s' % (a.get('url_afiliado') or '(nenhum)'))
    print('  - sai a ficha crua: %s' % (a.get('url_produto') or '(nenhuma)'))

    bloco['anuncios'] = [x for x in bloco['anuncios'] if int(x['item_id']) != args.item]
    bloco['anuncios_aposentados'] = col.aposentados_de(bloco) + [linha]

    r = bloco['resumo']
    antes = {k: r.get(k) for k in ('ofertas_que_servem', 'ofertas_com_link_de_afiliado',
                                   'ofertas_aposentadas', 'numero_proprio',
                                   'motivo_sem_numero_proprio',
                                   'contagem_de_rotulo_de_potencia',
                                   'abre_o_portao_da_30_2')}
    col.recontar_resumo(bloco)
    for campo, valor in sorted(antes.items()):
        if valor != r.get(campo):
            print('  - %s: %r -> %r' % (campo, valor, r.get(campo)))
    print('  - `ofertas_lidas` e `ofertas_recusadas` NAO mudam: sao fato da coleta de %s.'
          % bloco.get('colhido_em'))
    print('  + linha de quarentena:\n      %s' % linha)

    if not args.gravar:
        print('\nnada gravado (rode outra vez com --gravar).')
        return 0

    with open(BANCO, 'w', encoding='utf-8') as f:
        json.dump(banco, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('\ngravado em %s' % os.path.relpath(BANCO, RAIZ))
    print('AGORA RODE: python3 ferramentas/gerar-vitrine-de-produto.py --gravar')
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--conferir', action='store_true', help='portao, sem rede')
    p.add_argument('--consulta')
    p.add_argument('--item', type=int)
    p.add_argument('--causa', help='nome curto da causa: esgotado, produto-nao-existe')
    p.add_argument('--em', help='data da medicao, aaaa-mm-dd')
    p.add_argument('--causa-prosa', help='a CAUSA, que nao muda nunca (25.4-b.3)')
    p.add_argument('--ultima-medicao', help='o que a ultima passada mediu (25.4-b.3)')
    p.add_argument('--gravar', action='store_true')
    a = p.parse_args()

    if a.conferir:
        return conferir()
    faltando = [n for n in ('consulta', 'item', 'causa', 'em', 'causa_prosa', 'ultima_medicao')
                if getattr(a, n) in (None, '')]
    if faltando:
        print('REPROVADO: falta %s (ou use --conferir)' % ', '.join('--' + x.replace('_', '-')
                                                                    for x in faltando))
        return 1
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', a.em or ''):
        print('REPROVADO: --em tem de ser aaaa-mm-dd')
        return 1
    return aposentar(a)


if __name__ == '__main__':
    sys.exit(main())
