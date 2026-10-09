#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Colhe o dado COMERCIAL das consultas de produto da secao 30, consulta por consulta.

    python3 ferramentas/coletar-por-consulta.py --ensaio  [--so <id>] [--sem-link]
    python3 ferramentas/coletar-por-consulta.py --gravar  [--so <id>] [--sem-link]
    python3 ferramentas/coletar-por-consulta.py --conferir

`--ensaio` nao toca no banco: escreve o laudo na tela e para (25.3). `--conferir`
nao chama a rede: recarrega `dados/anuncios-por-consulta.json`, REAPLICA a regra
de relevancia sobre os titulos gravados e reprova se algum veredito gravado
discordar do calculado, ou se algum numero proprio do resumo nao refizer.

Credencial: `SHOPEE_APP_ID` e `SHOPEE_SECRET` no AMBIENTE (secao 25.6).

---------------------------------------------------------------------------
A DIFERENCA ENTRE ESTA FERRAMENTA E A `coletar-shopee.py`, que e uma so
---------------------------------------------------------------------------
A `coletar-shopee.py` parte de um REGISTRO DO BANCO de fabricante e procura o
anuncio DAQUELE produto: a pergunta dela e *"onde se compra o Vonder VDEC-51"*, e
quem decide e `casar-anuncio.py`, que exige marca e modelo batendo.

Esta parte da CONSULTA e procura os anuncios DO TIPO que a consulta pede: a
pergunta e *"o que aparece quando a pessoa digita `torques para mosaico`"*, e quem
decide e `relevancia-do-anuncio.py`, que nao sabe de marca nenhuma. As duas
convivem porque a secao 30.2 abriu um portao que a 25.1 nao abria — dado
comercial de anuncio vale para a pagina de consulta de produto, e ali o anuncio
nao precisa casar com registro nenhum do banco de fabricante.

---------------------------------------------------------------------------
OS NUMEROS PROPRIOS, e por que eles sao poucos de proposito
---------------------------------------------------------------------------
A 30.2 pede *"1 numero proprio"* por pagina, e a declaracao de cada consulta diz
qual. Sao tres formas, e nenhuma e estimada:

- `faixa_de_preco` — o menor e o maior preco entre os anuncios que SERVEM. Sai
  do campo `preco_min` de cada um, sempre.
- `preco_por_pastilha` e `preco_por_plaquinha` — preco dividido pela QUANTIDADE
  DECLARADA NO TITULO, e so quando o titulo a declara. `quantidade_declarada()`
  abaixo nao adivinha: titulo sem numero de peca sai com `null` e o motivo
  escrito, e a conta nao acontece.

**O numero proprio e recalculado por `--conferir` e comparado com o gravado.** E
a terceira conta que a secao 8 do contrato pede: numero que a ilha publica sobre
si mesma nasce contado, e continua contado na passada seguinte.
"""

import argparse
import datetime
import importlib.util
import json
import os
import re
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FERRAMENTAS = os.path.join(RAIZ, 'ferramentas')
DECLARACAO = os.path.join(RAIZ, 'dados', 'consultas-de-produto.json')
BANCO = os.path.join(RAIZ, 'dados', 'anuncios-por-consulta.json')

SUB_ID = 'clubedomosaico'     # a Shopee recusa sub-id com hifen ou sublinhado
QUANTOS = 20
PAUSA = 0.4
HOJE = datetime.date.today().isoformat()


def _modulo(nome, caminho):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


rel = _modulo('relevancia', os.path.join(FERRAMENTAS, 'relevancia-do-anuncio.py'))


def shopee():
    """A API so e carregada quando a rede vai ser usada: `--conferir` nao a quer."""
    return _modulo('shopee_api', os.path.abspath(
        os.path.join(RAIZ, '..', '..', 'ferramentas', 'shopee-api.py')))


def declaracoes():
    with open(DECLARACAO, encoding='utf-8') as f:
        return json.load(f)


def sub_id_2_de(id_da_consulta):
    """O segundo sub-id desta pagina: so letras e digitos, porque a Shopee recusa o resto.

    E derivado do `id` da consulta e nunca digitado, pelo mesmo motivo que o ID
    de medicao do GA4 mora numa constante: sub-id digitado a mao e sub-id que
    alguem copia junto com o codigo e descobre trocado no relatorio do mes.
    """
    return re.sub(r'[^0-9a-z]', '', (id_da_consulta or '').lower())[:24]


# ---------------------------------------------------------------------------
# A QUANTIDADE DECLARADA NO TITULO
# ---------------------------------------------------------------------------
# Cada molde abaixo nasceu de um titulo REAL desta coleta, e o nome do molde vai
# gravado ao lado do numero — procedencia por campo, como o resto do banco. Nao
# existe molde "generico": numero solto num titulo e medida, cor, polegada ou
# codigo com a mesma frequencia com que e quantidade.
MOLDES_DE_QUANTIDADE = (
    # "Kit com 900 Pastilhas para Mosaico", "Kit com 3388 Pastilhas 2x2cm"
    ('kit-com-n', r'\bkit\s+com\s+([0-9][0-9\.]*)\b'),
    # "Kit 100 plaquinhas mdf cru", "Kit 20 Adesivo"
    ('kit-n', r'\bkit\s+([0-9][0-9\.]*)\s*(?:plaquinha|pastilha|placa|peca|pcs|un)'),
    # "( Pacote com 100 pecas)"
    ('pacote-com-n', r'\bpacote\s+com\s+([0-9][0-9\.]*)\b'),
    # "245pcs", "100 Pcs/Lote", "1200 pecas"
    ('n-pecas', r'\b([0-9][0-9\.]*)\s*(?:pcs|pecas|peca|pc)\b'),
    # "Total 1200 pecas"
    ('total-n', r'\btotal\s+([0-9][0-9\.]*)\b'),
)


def quantidade_declarada(titulo):
    """(quantidade, molde) lidos do titulo, ou (None, motivo). Nunca estimada.

    Quando DOIS moldes diferentes acham numeros DIFERENTES no mesmo titulo, a
    funcao devolve `None` com o motivo: `Kit 5 Plaquinhas de Pastilhas de vidro
    para mosaico 2 x 2 cm - 245pcs` tem o 5 (plaquinhas) e o 245 (pecas), e as
    duas leituras sao defensaveis. Escolher a maior ou a primeira seria a ilha
    decidindo por sorte de ordem de lista, e o preco por peca sairia errado por
    um fator de 49.
    """
    texto = rel.sem_acento(titulo or '').lower()
    achados = []
    for nome, molde in MOLDES_DE_QUANTIDADE:
        m = re.search(molde, texto)
        if m:
            try:
                n = int(m.group(1).replace('.', ''))
            except ValueError:
                continue
            if n > 0:
                achados.append((nome, n))
    if not achados:
        return None, 'o titulo nao declara quantidade de pecas'
    distintos = sorted({n for _, n in achados})
    if len(distintos) > 1:
        return None, ('dois moldes leem quantidades diferentes no mesmo titulo (%s) — '
                      'escolher uma seria decidir por ordem de lista'
                      % ', '.join('%s=%d' % (nome, n) for nome, n in achados))
    return distintos[0], achados[0][0]


def preco(oferta):
    """O preco comparavel de uma oferta, ou None. `preco_min` sempre, nunca a media."""
    bruto = oferta.get('preco_min')
    if bruto in (None, ''):
        return None
    try:
        return round(float(bruto), 2)
    except (TypeError, ValueError):
        return None


def avaliar_consulta(dec, ofertas):
    """Aplica a regra a cada oferta e devolve a lista gravavel, com veredito e motivo."""
    linhas = []
    for o in ofertas:
        veredito = rel.avaliar(o.get('titulo'), dec)
        qtd, molde = quantidade_declarada(o.get('titulo'))
        linhas.append({
            'item_id': o.get('item_id'),
            'shop_id': o.get('shop_id'),
            'titulo': o.get('titulo'),
            'preco': preco(o),
            'moeda': 'BRL',
            'loja': o.get('loja'),
            'nota': o.get('nota'),
            'imagem_url': o.get('imagem_url'),
            'url_produto': o.get('url_produto'),
            'url_afiliado': o.get('url_afiliado'),
            'url_afiliado_sem_sub_id': o.get('url_afiliado_sem_sub_id'),
            'sub_id_1': o.get('sub_id_1'),
            'motivo_sem_link': o.get('motivo_sem_link'),
            'quantidade_declarada': qtd,
            'procedencia_da_quantidade': molde,
            'fonte': 'anuncio-shopee',
            'coletado_em': HOJE,
            'serve': veredito['serve'],
            'recusado_por': veredito['recusado_por'],
            'exigencia_que_faltou': veredito['exigencia_que_faltou'],
            'exigencias_atendidas': veredito['exigencias_atendidas'],
        })
    return linhas


def resumo(dec, linhas):
    """Os numeros proprios desta consulta, calculados — nunca digitados."""
    servem = [l for l in linhas if l['serve']]
    precos = sorted(p for p in (l['preco'] for l in servem) if p is not None)

    r = {
        'ofertas_lidas': len(linhas),
        'ofertas_que_servem': len(servem),
        'ofertas_recusadas': len(linhas) - len(servem),
        'abre_o_portao_da_30_2': len(servem) >= 3,
        'preco_minimo': precos[0] if precos else None,
        'preco_maximo': precos[-1] if precos else None,
        'numero_proprio_pedido': dec.get('numero_proprio'),
        'numero_proprio': None,
        'motivo_sem_numero_proprio': None,
    }

    pedido = dec.get('numero_proprio')
    if pedido == 'faixa_de_preco':
        if precos:
            r['numero_proprio'] = {'de': precos[0], 'ate': precos[-1],
                                   'sobre_quantas_ofertas': len(precos)}
        else:
            r['motivo_sem_numero_proprio'] = 'nenhuma oferta que serve trouxe preco'
    elif pedido in ('preco_por_pastilha', 'preco_por_plaquinha'):
        porunidade = []
        for l in servem:
            if l['preco'] is not None and l['quantidade_declarada']:
                porunidade.append({
                    'item_id': l['item_id'],
                    'preco': l['preco'],
                    'quantidade': l['quantidade_declarada'],
                    'por_unidade': round(l['preco'] / l['quantidade_declarada'], 4),
                    'procedencia_da_quantidade': l['procedencia_da_quantidade'],
                })
        if porunidade:
            valores = sorted(x['por_unidade'] for x in porunidade)
            r['numero_proprio'] = {
                'de': valores[0], 'ate': valores[-1],
                'sobre_quantas_ofertas': len(valores),
                'conta': porunidade,
            }
        else:
            r['motivo_sem_numero_proprio'] = (
                'nenhuma oferta que serve declara quantidade de pecas no titulo, '
                'e quantidade nao se estima')
    elif pedido is None:
        r['motivo_sem_numero_proprio'] = (
            'consulta que nao publica: a declaracao nao pede numero proprio')
    return r


def colher(dec, api, com_link):
    ofertas = api.buscar(dec['consulta'], QUANTOS)
    time.sleep(PAUSA)
    linhas = avaliar_consulta(dec, ofertas)

    # O LINK COM SUB-ID SO E GERADO PARA O QUE SERVE, E SO EM CONSULTA QUE
    # PUBLICA. Gerar para o que a regra recusou, ou para consulta que a
    # declaracao marca `publicar: false`, seria encher a conta de afiliado de
    # links que nenhuma pagina vai servir — e link gerado e link que existe
    # para sempre. As cinco armadilhas e as tres consultas de outro endereco
    # ficam no banco como MEDICAO, com titulo, preco e veredito, e sem link.
    if com_link and dec.get('publicar'):
        s2 = sub_id_2_de(dec['id'])
        for l in linhas:
            if not l['serve']:
                continue
            origem = l['url_produto'] or l['url_afiliado_sem_sub_id']
            if not origem:
                l['motivo_sem_link'] = 'a Shopee nao devolveu endereco de produto'
                continue
            try:
                l['url_afiliado'] = api.encurtar(origem, SUB_ID, s2)
                l['sub_id_1'] = SUB_ID
                l['sub_id_2'] = s2
                l['url_afiliado_gerada_em'] = HOJE
            except Exception as erro:          # noqa: BLE001 — o motivo vai gravado
                l['motivo_sem_link'] = str(erro)
            time.sleep(PAUSA)
    return linhas


def conferir():
    """Reaplica a regra e as contas sobre o banco gravado. Sem rede."""
    if not os.path.exists(BANCO):
        print('REPROVADO: %s nao existe' % os.path.relpath(BANCO, RAIZ))
        return 1
    with open(BANCO, encoding='utf-8') as f:
        banco = json.load(f)
    decs = {d['id']: d for d in declaracoes()['consultas']}

    falhas, afirmacoes = [], 0
    for bloco in banco['consultas']:
        dec = decs.get(bloco['id'])
        if dec is None:
            falhas.append('%s: gravada no banco e ausente da declaracao' % bloco['id'])
            continue

        for l in bloco['anuncios']:
            afirmacoes += 1
            v = rel.avaliar(l['titulo'], dec)
            if bool(v['serve']) != bool(l['serve']):
                falhas.append('%s / item %s: gravado serve=%s, a regra diz %s'
                              % (bloco['id'], l['item_id'], l['serve'], v['serve']))
            if v['serve'] is False and v['recusado_por'] != l.get('recusado_por'):
                falhas.append('%s / item %s: recusado_por gravado %r, a regra diz %r'
                              % (bloco['id'], l['item_id'],
                                 l.get('recusado_por'), v['recusado_por']))
            afirmacoes += 1
            qtd, molde = quantidade_declarada(l['titulo'])
            if qtd != l.get('quantidade_declarada'):
                falhas.append('%s / item %s: quantidade gravada %r, o molde le %r'
                              % (bloco['id'], l['item_id'],
                                 l.get('quantidade_declarada'), qtd))

        afirmacoes += 1
        refeito = resumo(dec, bloco['anuncios'])
        for chave in ('ofertas_lidas', 'ofertas_que_servem', 'ofertas_recusadas',
                      'abre_o_portao_da_30_2', 'preco_minimo', 'preco_maximo',
                      'numero_proprio'):
            if refeito[chave] != bloco['resumo'].get(chave):
                falhas.append('%s: resumo.%s gravado %r, a conta refaz %r'
                              % (bloco['id'], chave,
                                 bloco['resumo'].get(chave), refeito[chave]))

    for f in falhas:
        print('  DEFEITO %s' % f)
    print('%s: %d afirmacoes, %d defeito(s)'
          % ('REPROVADO' if falhas else 'APROVADO', afirmacoes, len(falhas)))
    return 1 if falhas else 0


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--ensaio', action='store_true')
    p.add_argument('--gravar', action='store_true')
    p.add_argument('--conferir', action='store_true')
    p.add_argument('--so', default=None, help='so esta consulta, pelo id')
    p.add_argument('--sem-link', action='store_true',
                   help='nao gera link de afiliado (poupa chamada e nao cria link)')
    p.add_argument('--descartar-links', action='store_true',
                   help='permite que --sem-link apague links de afiliado JA gravados')
    a = p.parse_args()

    if a.conferir:
        raise SystemExit(conferir())
    if not (a.ensaio or a.gravar):
        p.error('escolha --ensaio, --gravar ou --conferir')

    doc = declaracoes()
    api = shopee()
    alvos = [d for d in doc['consultas'] if a.so in (None, d['id'])]
    if not alvos:
        raise SystemExit('nenhuma consulta com id %r' % a.so)

    blocos = []
    for dec in alvos:
        linhas = colher(dec, api, com_link=(a.gravar and not a.sem_link))
        r = resumo(dec, linhas)
        blocos.append({
            'id': dec['id'],
            'consulta': dec['consulta'],
            'slug': dec.get('slug'),
            'publicar_declarado': dec.get('publicar'),
            'colhido_em': HOJE,
            'canal': 'API de afiliado da Shopee (productOfferV2), credencial no ambiente',
            'resumo': r,
            'anuncios': linhas,
        })
        marca = 'ABRE' if r['abre_o_portao_da_30_2'] else 'NAO ABRE'
        print('%-9s %-32s lidas %2d | servem %2d | %s'
              % (marca, dec['id'], r['ofertas_lidas'], r['ofertas_que_servem'],
                 (('R$ %.2f a R$ %.2f' % (r['preco_minimo'], r['preco_maximo']))
                  if r['preco_minimo'] is not None else 'sem preco')))
        for l in linhas:
            if l['serve']:
                print('      serve   R$%-9s %s' % (l['preco'], (l['titulo'] or '')[:74]))

    if a.ensaio:
        print('\nensaio: nada foi gravado.')
        return

    anterior = {}
    if os.path.exists(BANCO) and a.so:
        with open(BANCO, encoding='utf-8') as f:
            anterior = {b['id']: b for b in json.load(f)['consultas']}

        # FALHA FECHADA CONTRA O PROPRIO PE, e ela nasceu de eu ter pisado nele:
        # em 09/10/2026, `--gravar --so torques-para-mosaico --sem-link` SUBSTITUIU
        # o bloco daquela consulta por uma coleta nova sem link, e os 19 links de
        # afiliado que a passada anterior havia gerado sumiram do banco em silencio.
        # Foi uma contagem que pegou, nao um portao. Agora e portao: recoleta de
        # consulta que JA TEM link exige dizer, com todas as letras, que os links
        # vao ser descartados.
        for bloco in (anterior.get(d['id']) for d in alvos):
            if not bloco:
                continue
            com_link = sum(1 for l in bloco['anuncios'] if l.get('url_afiliado'))
            if com_link and a.sem_link and not a.descartar_links:
                raise SystemExit(
                    'RECUSADO: %s ja tem %d anuncio(s) com link de afiliado gravado, e '
                    '--sem-link apagaria todos. Rode sem --sem-link para regerar os links, '
                    'ou com --descartar-links para apagar de proposito.'
                    % (bloco['id'], com_link))
    for b in blocos:
        anterior[b['id']] = b
    ordem = [d['id'] for d in doc['consultas']]

    saida = {
        'id': 'anuncios-por-consulta',
        'ilha': 'clubedomosaico',
        'gerado_em': HOJE,
        'gerado_por': 'ferramentas/coletar-por-consulta.py',
        'o_que_este_arquivo_e': (
            'O dado COMERCIAL da secao 30.2 do ARQUIPELAGO.md: os anuncios que a '
            'API de afiliado da Shopee devolve para cada consulta de produto desta '
            'ilha, com o veredito da regra de relevancia ao lado de cada um. '
            'ARQUIVO GERADO — nao edite a mao. `--conferir` reaplica a regra sobre '
            'os titulos gravados e reprova se algum veredito ou numero discordar.'),
        'abre_o_portao_NAO_e_o_mesmo_que_publica': (
            'LEIA ANTES DE CONTAR: `resumo.abre_o_portao_da_30_2` e SO o portao de DADO '
            '(3 ou mais anuncios que servem). Ele diz TRUE em ONZE consultas e apenas '
            'OITO publicam. As tres diferencas sao `pinca-para-mosaico`, que tem dado de '
            'sobra e sai por CANIBALIZACAO da 30.4 (devolve o mesmo alicate de duas '
            'consultas irmas), e `azulejo-para-mosaico` e `colar-de-mosaico`, que tem '
            'dado e sao intencao de LOJA — o que serve nelas e PECA PRONTA de mosaico, '
            'que e o que a artesa vende. Uma pagina publica quando `abre_o_portao_da_30_2` '
            'E `publicar_declarado` sao os DOIS verdadeiros; o motivo de cada `false` esta '
            'em `nao_publica_porque`, na declaracao. Contar so o portao e publicar tres '
            'paginas que a propria ilha decidiu nao ter.'),
        'o_que_decide_o_veredito': (
            'ferramentas/relevancia-do-anuncio.py, sobre a declaracao daquela '
            'consulta em dados/consultas-de-produto.json. Nenhum anuncio desta '
            'lista foi escolhido ou descartado a mao.'),
        'motivo_do_mercado_livre': (
            'A 30.2 admite anuncio de Mercado Livre com a mesma procedencia, e esta '
            'coleta NAO o alcancou: medido em 09/10/2026, tres passadas, '
            'www.mercadolivre.com.br e lista.mercadolivre.com.br responderam 403 nas '
            'tres, com CONNECT aceito pelo proxy e o 403 vindo do proprio balanceador '
            'deles (server: awselb/2.0, rps: w403), enquanto clubedomosaico.com.br e '
            'shopee.com.br responderam 200 nas mesmas passadas. Nao e a lista de rede '
            'da secao 20 e nao e o egresso: e o anti-robo do Mercado Livre, que a '
            'leitura semanal de 07/10 ja havia registrado pelo lado do navegador '
            '(reCAPTCHA). Entao TODO dado comercial deste arquivo e de UMA fonte, e '
            'a pagina que o publicar nao pode dizer "o mercado" quando quer dizer '
            '"a Shopee".'),
        'consultas': [anterior[i] for i in ordem if i in anterior],
    }
    with open(BANCO, 'w', encoding='utf-8') as f:
        json.dump(saida, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('\ngravado: %s' % os.path.relpath(BANCO, RAIZ))


if __name__ == '__main__':
    main()
