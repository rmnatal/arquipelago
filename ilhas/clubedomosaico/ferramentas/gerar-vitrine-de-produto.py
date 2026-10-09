#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GERA `dados/vitrine-de-produto.json`: o recorte COMERCIAL que as oito paginas de
consulta de produto servem no ar, derivado de `dados/anuncios-por-consulta.json`
(a coleta datada) e de `dados/consultas-de-produto.json` (a declaracao e a regra).

    python3 ferramentas/gerar-vitrine-de-produto.py .            # escreve
    python3 ferramentas/gerar-vitrine-de-produto.py . --conferir  # regera e compara

POR QUE ELE EXISTE SEPARADO DA COLETA, e nao e copia dela:

  1. A COLETA NAO PODE IR AO AR INTEIRA. `anuncios-por-consulta.json` tem 258 KB,
     as dezesseis consultas, os anuncios RECUSADOS com o motivo de cada um e o
     `url_afiliado_sem_sub_id` — que e um link de afiliado que NAO rastreia esta
     ilha. Option do WordPress e coisa que a pagina le a cada carga; e link sem
     `sub_id` num arquivo que a pagina le e o defeito de 23/09 esperando acontecer
     de novo. Aqui entra SO o que a pagina mostra: oito consultas, 58 anuncios que
     servem, e o link COM `sub_id_1`.
  2. O NUMERO PROPRIO E RECALCULADO DAS OFERTAS QUE ENTRAM, nunca copiado do
     resumo da coleta. Se o resumo discordar do que esta sendo publicado, este
     arquivo NAO nasce. E a trava que a secao 30.2 pede com outras palavras: o
     numero que a pagina publica sobre si mesma tem de ser contado do que ela
     serve, e as duas metades andaram separadas uma vez nesta ilha (o manifest 113
     declarando um portao de antes da correcao dele, na aquametria).
  3. O PISO DA 30.2 E PORTAO E NAO AVISO. Consulta declarada `publicar: true` que
     chegue aqui com menos de TRES ofertas que servem, ou com uma oferta sem link
     de afiliado, derruba a geracao inteira com codigo 1. Duas destas oito nascem
     com exatamente tres (`base-de-mdf` e `rejunte`), entao este portao e o que
     avisa na proxima coleta em vez de a pagina descobrir no ar.

O QUE ELE NAO DECIDE: nada de editorial. Titulo, `description`, a resposta em duas
frases, o "qual escolher" e as perguntas moram em `dados/paginas-de-produto.json`,
que e DECLARADO e escrito a mao, na voz do `VOZ.md`. Aqui so entra numero e link.
"""
import json
import os
import sys

PISO_DA_30_2 = 3

# `nota` NAO ENTRA, e a ausencia e medida e nao esquecimento. Das 58 ofertas que
# servem, 31 tem `nota: "0"` e uma tem `"1"` — e nenhum arquivo desta ilha diz o
# que o campo significa: nao se sabe se e estrela de 1 a 5, se `0` quer dizer
# "sem avaliacao" ou se e outra escala. Servido na tela, `0` le-se como produto
# pessimo em mais da metade da lista, e `nota 1` num produto que a pagina
# RECOMENDA. A 30.2 lista o que o anuncio sustenta — titulo, preco, foto, medida
# e quantidade declaradas — e `nota` nao esta nela. Publicar numero cuja regua
# ninguem escreveu e inventar o significado, que e o defeito que esta ilha mais
# paga. Quando alguem medir o campo, ele entra aqui e na tabela de uma vez.
CAMPOS_DA_OFERTA = (
    'item_id', 'titulo', 'preco', 'loja', 'imagem_url',
    'url_afiliado', 'quantidade_declarada', 'procedencia_da_quantidade',
)


def erro(msg):
    print('ERRO: ' + msg, file=sys.stderr)
    sys.exit(1)


def por_unidade(preco, quantidade):
    """O preco por peca, com a mesma regua dos dois arquivos de origem."""
    return round(float(preco) / int(quantidade), 4)


def numero_proprio(tipo, ofertas, consulta_id):
    """
    O numero proprio CONTADO das ofertas que esta pagina serve.

    `faixa_de_preco` conta sobre todas; os dois `preco_por_*` contam SO sobre as
    ofertas que declaram quantidade — e e por isso que a base de MDF tem tres
    ofertas e o numero dela sai sobre DUAS. A pagina tem de dizer isso, e o
    campo `sobre_quantas_ofertas` e o que a obriga a poder dizer.
    """
    if tipo == 'faixa_de_preco':
        precos = [float(o['preco']) for o in ofertas]
        return {
            'tipo': tipo,
            'de': min(precos),
            'ate': max(precos),
            'sobre_quantas_ofertas': len(precos),
            'conta': None,
        }

    if tipo not in ('preco_por_pastilha', 'preco_por_plaquinha'):
        erro('numero proprio desconhecido em %s: %s' % (consulta_id, tipo))

    conta = []
    for o in ofertas:
        q = o.get('quantidade_declarada')
        if not q:
            continue
        conta.append({
            'item_id': o['item_id'],
            'preco': float(o['preco']),
            'quantidade': int(q),
            'por_unidade': por_unidade(o['preco'], q),
            'procedencia_da_quantidade': o.get('procedencia_da_quantidade'),
        })
    if not conta:
        erro('%s pede %s e nenhuma oferta declara quantidade' % (consulta_id, tipo))
    unidades = [c['por_unidade'] for c in conta]
    return {
        'tipo': tipo,
        'de': min(unidades),
        'ate': max(unidades),
        'sobre_quantas_ofertas': len(conta),
        'conta': conta,
    }


def montar(raiz):
    declaracao = json.load(open(os.path.join(raiz, 'dados/consultas-de-produto.json'), encoding='utf-8'))
    coleta = json.load(open(os.path.join(raiz, 'dados/anuncios-por-consulta.json'), encoding='utf-8'))
    por_id = {c['id']: c for c in coleta['consultas']}

    paginas = []
    for d in declaracao['consultas']:
        if not d.get('publicar'):
            continue
        if d['id'] not in por_id:
            erro('consulta %s declara publicar e nao tem coleta' % d['id'])
        c = por_id[d['id']]

        ofertas = []
        for a in c['anuncios']:
            if not a.get('serve'):
                continue
            if not a.get('url_afiliado'):
                erro('%s: oferta %s serve e nao tem url_afiliado (motivo: %s)'
                     % (d['id'], a.get('item_id'), a.get('motivo_sem_link')))
            if a.get('sub_id_1') != 'clubedomosaico':
                erro('%s: oferta %s tem sub_id_1 %r, e so o desta ilha pode ir ao ar'
                     % (d['id'], a.get('item_id'), a.get('sub_id_1')))
            ofertas.append({k: a.get(k) for k in CAMPOS_DA_OFERTA})

        if len(ofertas) < PISO_DA_30_2:
            erro('%s declara publicar e tem %d oferta(s) que servem; o piso da 30.2 e %d'
                 % (d['id'], len(ofertas), PISO_DA_30_2))

        # A ORDEM E DO PRECO, do mais barato para o mais caro, e nao a da API: a
        # ordem da API varia entre chamadas (esta escrito no proprio arquivo de
        # coleta), e ordem que muda sozinha faz a pagina mudar sem ninguem editar.
        ofertas.sort(key=lambda o: (float(o['preco']), int(o['item_id'])))

        np = numero_proprio(d['numero_proprio'], ofertas, d['id'])

        # O RESUMO DA COLETA TEM DE CONCORDAR COM O QUE ESTA SENDO PUBLICADO.
        r = c['resumo']
        if int(r['ofertas_que_servem']) != len(ofertas):
            erro('%s: o resumo da coleta diz %s ofertas que servem e entram %d'
                 % (d['id'], r['ofertas_que_servem'], len(ofertas)))
        fonte_np = r.get('numero_proprio') or {}
        for campo in ('de', 'ate', 'sobre_quantas_ofertas'):
            if campo in fonte_np and fonte_np[campo] != np[campo]:
                erro('%s: o resumo da coleta diz %s=%r e a conta das ofertas publicadas da %r'
                     % (d['id'], campo, fonte_np[campo], np[campo]))

        paginas.append({
            'id': d['id'],
            'consulta': d['consulta'],
            'slug': d['slug'],
            'colhido_em': c['colhido_em'],
            'canal': c['canal'],
            'n_ofertas': len(ofertas),
            'numero_proprio': np,
            'ofertas': ofertas,
        })

    if not paginas:
        erro('nenhuma consulta declara publicar; a vitrine nao nasce vazia')

    return {
        'id': 'vitrine-de-produto',
        'ilha': 'clubedomosaico',
        'gerado_em': coleta['gerado_em'],
        'gerado_por': 'ferramentas/gerar-vitrine-de-produto.py',
        'o_que_este_arquivo_e': (
            'O recorte COMERCIAL que as paginas de consulta de produto servem no ar: '
            'so as consultas que publicam, so os anuncios que a regra de relevancia '
            'aprovou, so os campos que a pagina mostra, e o link de afiliado COM '
            'sub_id desta ilha. Nao editar a mao: o portao regera e compara.'
        ),
        'de_onde_ele_vem': (
            'dados/anuncios-por-consulta.json (a coleta datada da API de afiliado da '
            'Shopee) cruzado com dados/consultas-de-produto.json (a declaracao e a '
            'regra de relevancia). O numero proprio de cada pagina e RECALCULADO das '
            'ofertas que entram e conferido contra o resumo da coleta.'
        ),
        'a_fonte_e_uma_so_e_a_pagina_diz_isso': (
            'Todo dado comercial destas paginas vem da SHOPEE. O Mercado Livre '
            'respondeu 403 nas tres passadas de 09/10/2026 (CONNECT aceito pelo proxy, '
            '403 do balanceador deles). Nenhuma pagina pode dizer "o mercado" querendo '
            'dizer "a Shopee".'
        ),
        'o_preco_e_de_UMA_coleta_datada': (
            'A API devolve conjuntos diferentes entre chamadas, entao a faixa de cada '
            'consulta e a de UMA coleta, na data de gerado_em, e nunca o catalogo da '
            'Shopee. A pagina publica a data junto com o numero.'
        ),
        'duas_nascem_no_limite': (
            'base-para-mosaico-mdf e rejunte-para-mosaico tem exatamente 3 ofertas, que '
            'e o minimo da 30.2 e nao uma folga. A proxima coleta que perder uma oferta '
            'derruba a pagina, e este gerador sai com codigo 1 em vez de publicar menos.'
        ),
        'publicar': True,
        'piso_da_30_2': PISO_DA_30_2,
        'n_paginas': len(paginas),
        'n_ofertas': sum(p['n_ofertas'] for p in paginas),
        'paginas': paginas,
    }


def main():
    raiz = sys.argv[1] if len(sys.argv) > 1 else '.'
    conferir = '--conferir' in sys.argv
    destino = os.path.join(raiz, 'dados/vitrine-de-produto.json')

    novo = montar(raiz)
    texto = json.dumps(novo, ensure_ascii=False, indent=1) + '\n'

    if conferir:
        if not os.path.exists(destino):
            erro('--conferir e o arquivo nao existe: %s' % destino)
        atual = open(destino, encoding='utf-8').read()
        if atual != texto:
            erro('dados/vitrine-de-produto.json DIVERGE do que o gerador produz. '
                 'Ele e GERADO: rode sem --conferir em vez de editar a mao.')
        print('APROVADO: dados/vitrine-de-produto.json bate com o gerador '
              '(%d paginas, %d ofertas).' % (novo['n_paginas'], novo['n_ofertas']))
        return

    with open(destino, 'w', encoding='utf-8') as f:
        f.write(texto)
    print('GRAVADO: dados/vitrine-de-produto.json — %d paginas, %d ofertas.'
          % (novo['n_paginas'], novo['n_ofertas']))
    for p in novo['paginas']:
        np = p['numero_proprio']
        print('  %-34s %2d ofertas  %-20s de %s ate %s (sobre %d)'
              % (p['id'], p['n_ofertas'], np['tipo'], np['de'], np['ate'],
                 np['sobre_quantas_ofertas']))


if __name__ == '__main__':
    main()
