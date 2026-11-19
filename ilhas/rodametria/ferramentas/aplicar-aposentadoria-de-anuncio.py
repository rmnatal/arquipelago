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
  `ofertas_lidas == len(anuncios) + resumo['ofertas_aposentadas_nesta_coleta']` —
  e NAO com a quarentena inteira: aposentado de coleta velha que a loja nao
  devolveu na leitura de hoje nunca entrou no `ofertas_lidas` de hoje (corrigido
  em 17/11/2026, depois de a invariante velha reprovar um banco certo).
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

        # 0. O ROTULO DA CAUSA TEM DE SER UM DOS DECLARADOS, senao a tela nao
        #    tem frase de leitor para ele e a 25.11 fica sem a metade que ela
        #    chama de honesta ("ela e honesta porque e verdade").
        for causa, quantos in sorted(col.causas_em_quarentena(bloco).items()):
            afirmacoes += 1
            if causa not in col.CAUSAS_DE_APOSENTADORIA:
                falhas.append('%s: a quarentena usa a causa %r (%d linha(s)) e ela nao '
                              'esta em CAUSAS_DE_APOSENTADORIA: a tela nao tem frase de '
                              'leitor para ela' % (bid, causa, quantos))
        afirmacoes += 1
        if sum(col.causas_em_quarentena(bloco).values()) != len(apos):
            falhas.append('%s: %d linha(s) de quarentena e %d com rotulo de causa lido: '
                          'linha sem rotulo sai da contagem E sai da LISTA DE BLOQUEIO'
                          % (bid, len(apos), sum(col.causas_em_quarentena(bloco).values())))

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

        # 3. A SOMA FECHA, E ELA NAO FECHA COM `anuncios_aposentados`.
        #    `ofertas_lidas` e fato da coleta do dia: ele conta o que a LOJA
        #    DEVOLVEU naquela leitura. Entao ele tem de ser o que sobrou na lista
        #    mais o que foi aposentado DENTRO daquela leitura — nunca mais a
        #    quarentena inteira. MEDIDO em 17/11/2026 as 19h3xZ, e esta afirmacao
        #    estava REPROVANDO um banco certo: a `patinete-eletrico` tem dois
        #    aposentados, um de 11/11 que a loja NAO devolveu na recoleta de 17/11
        #    e um de 13/11 que ela devolveu e a quarentena recusou. A soma velha
        #    pedia 19 + 2 = 21 sobre 20 lidas; a certa pede 19 + 1 = 20. Aposentado
        #    de coleta velha que a loja nao devolveu hoje NUNCA FOI LIDO hoje, e a
        #    invariante velha so valia na ilha onde recoleta nunca acontece.
        #    (`ofertas_aposentadas` continua cobrado pela afirmacao 2, que e a
        #    conta da QUARENTENA INTEIRA: as duas contas sao diferentes de
        #    proposito e nenhuma substitui a outra.)
        nesta = int(r.get('ofertas_aposentadas_nesta_coleta') or 0)
        afirmacoes += 1
        if nesta > len(apos):
            falhas.append('%s: ofertas_aposentadas_nesta_coleta %d e maior que a quarentena '
                          'inteira (%d aposentado(s)): nao se aposenta nesta coleta mais do '
                          'que existe' % (bid, nesta, len(apos)))
        afirmacoes += 1
        if int(r['ofertas_lidas']) != len(bloco['anuncios']) + nesta:
            falhas.append(
                '%s: ofertas_lidas %d nao fecha com %d anuncio(s) + %d aposentado(s) desta coleta'
                % (bid, r['ofertas_lidas'], len(bloco['anuncios']), nesta))

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

    # ------------------------------------------------------------------
    # A LINHA E MONTADA AQUI DENTRO, NUM MUNDO FABRICADO (18/11/2026).
    #
    # As afirmacoes acima leem o banco; nenhuma delas MONTAVA uma linha, e por
    # isso o `TypeError` de precedencia descrito em `montar_linha` passou dois
    # dias com o portao verde. O mundo e fabricado de proposito: anuncio de
    # verdade muda, e o que esta sob prova e o FORMATO, nao o dado do dia.
    areia = {
        'item_id': 58215666648, 'shop_id': 1136378529,
        'titulo': '  Scooter (Bike) Eletrica Foston X15 Max 1000w 32km/h  ',
        'preco': 8500.0, 'coletado_em': '2026-11-18', 'degrau_da_escada': '1',
        'url_afiliado': 'https://s.shopee.com.br/XXXXXXXXXX', 'loja': 'LOJA DA AREIA',
    }
    afirmacoes += 1
    try:
        montada = montar_linha('2026-11-18', areia, 'esgotado',
                               'a loja serve a palavra Esgotado colada ao titulo',
                               'lida em 18/11/2026 no Chrome do Raphael')
    except Exception as erro:
        montada = None
        falhas.append('montar_linha morreu antes de devolver cadeia: %s: %s'
                      % (type(erro).__name__, erro))
    if montada is not None:
        afirmacoes += 1
        if not col.PADRAO_APOSENTADO.match(montada):
            falhas.append('a linha MONTADA nao casa com PADRAO_APOSENTADO, que e o '
                          'mesmo regex que o coletor le como lista de bloqueio: %r'
                          % (montada[:160],))
        # O COLETOR TEM DE ACHAR O ID NELA: formato que casa o regex e nao
        # devolve o id deixaria o anuncio VOLTAR vivo na coleta seguinte.
        afirmacoes += 1
        achados = col.ids_em_quarentena({'anuncios_aposentados': [montada]})
        if 58215666648 not in achados:
            falhas.append('o coletor nao acha o id na linha montada (leu %r): a '
                          'quarentena E a lista de bloqueio, e linha que o coletor '
                          'nao le deixa o anuncio esgotado voltar como oferta viva'
                          % (achados,))
        afirmacoes += 1
        if col.causas_em_quarentena({'anuncios_aposentados': [montada]}).get('esgotado') != 1:
            falhas.append('o rotulo curto da causa nao e lido de volta da linha montada: '
                          'sem ele a linha sai da contagem E da lista de bloqueio')
        # A REGUA VELHA OBRIGADA A DISCORDAR (20.8): autoteste em que a antiga
        # tambem passa nao mede conserto nenhum. A antiga nao devolve cadeia —
        # ela levanta TypeError —, e e isso que esta afirmacao cobra.
        afirmacoes += 1
        try:
            _ = ('APOSENTADO EM %s — item %d da loja %d — CAUSA (' + 'esgotado'
                 + '): %s '
                 '|| ULTIMA MEDICAO: %s'
                 % ('2026-11-18', 1, 2, 'causa', 'medicao'))
            falhas.append('a montagem ANTIGA (com `+` no meio e `%` no fim) devolveu '
                          'cadeia: se ela passa, este autoteste nao esta medindo o '
                          'conserto de 18/11/2026')
        except TypeError:
            pass

    for f in falhas:
        print('FALHA: ' + f)
    print('\n%d afirmacao(oes), %d falha(s).' % (afirmacoes, len(falhas)))
    print('APROVADO' if not falhas else 'REPROVADO')
    return 1 if falhas else 0


# ---------------------------------------------------------------------------
def rotular(args):
    """PoE o rotulo curto da causa numa linha de quarentena que nasceu sem ele.

    POR QUE ESTE MODO EXISTE, E POR QUE ELE E AQUI. O formato fechado da 25.11
    ganhou o rotulo curto da causa em 16/11/2026, para a frase de leitor poder
    dizer a causa CERTA em palavras — ate aquele dia a tela servia "esgotado"
    para toda aposentadoria, e desde 13/11 isso era falso em
    `/veiculos/patinete-eletrico/`, que tem um anuncio aposentado por "O produto
    nao existe".

    Tres linhas ja estavam gravadas sem rotulo. Editar prosa de quarentena a mao
    e exatamente o que a 25.11 proibe ("o conserto e ferramenta e nao edicao a
    mao"), e o dono da linha e esta ferramenta — entao o rotulo entra por aqui,
    com a troca IMPRESSA e o portao cobrando o formato depois. O modo NAO toca a
    prosa da causa nem a da ultima medicao: ele so insere o rotulo que a
    contagem le.
    """
    banco = carregar()
    col = _coletor()
    if args.causa not in col.CAUSAS_DE_APOSENTADORIA:
        print('REPROVADO: causa %r nao esta em CAUSAS_DE_APOSENTADORIA (%s)'
              % (args.causa, ', '.join(sorted(col.CAUSAS_DE_APOSENTADORIA))))
        return 1
    alvo = None
    for bloco in banco['consultas']:
        for i, linha in enumerate(col.aposentados_de(bloco)):
            if ('item %d da loja' % args.item) in linha:
                alvo = (bloco, i, linha)
    if alvo is None:
        print('REPROVADO: nenhuma linha de quarentena menciona o item %d' % args.item)
        return 1
    bloco, i, linha = alvo
    if ' — CAUSA (' in linha:
        print('nada a fazer: a linha do item %d ja tem rotulo' % args.item)
        return 0
    if ' — CAUSA: ' not in linha:
        print('REPROVADO: a linha do item %d nao tem o trecho " — CAUSA: "' % args.item)
        return 1
    nova = linha.replace(' — CAUSA: ', ' — CAUSA (%s): ' % args.causa, 1)
    if not col.PADRAO_APOSENTADO.match(nova):
        print('REPROVADO: a linha rotulada nao casa com o formato fechado.')
        return 1
    print('ROTULANDO a quarentena do item %d com a causa %r:' % (args.item, args.causa))
    print('  - antes: ...%s...' % linha[linha.index(' — CAUSA: '):][:60])
    print('  - depois: ...%s...' % nova[nova.index(' — CAUSA ('):][:60])
    print('  - a prosa da causa e a da ultima medicao NAO foram tocadas.')
    if not args.gravar:
        print('\nnada gravado (rode outra vez com --gravar).')
        return 0
    bloco['anuncios_aposentados'][i] = nova
    with open(BANCO, 'w', encoding='utf-8') as f:
        json.dump(banco, f, ensure_ascii=False, indent=_recuo_do_banco())
        f.write('\n')
    print('\ngravado em %s' % os.path.relpath(BANCO, RAIZ))
    return 0


# ---------------------------------------------------------------------------
def montar_linha(em, a, causa, causa_prosa, ultima_medicao):
    """A LINHA FECHADA DA 25.11, MONTADA NUM LUGAR SO — e e ESTA funcao que o
    autoteste chama, nunca uma copia dela (18/11/2026).

    O DEFEITO QUE ISTO FECHA, e ele e de PRECEDENCIA e nao de formato: a linha
    era montada com `+` no meio de literais e um `%` no fim, e em Python o `%`
    casa mais apertado que o `+` — entao o `%` recebia so o ULTIMO literal
    (`'): %s || ULTIMA MEDICAO: %s'`, duas vagas) com as DEZ substituicoes, e o
    modo de gravar morria em `TypeError: not all arguments converted during
    string formatting` ANTES de tocar o banco. Medido as 16h2xZ de 18/11/2026,
    na primeira tentativa de aposentar um anuncio desde que o rotulo curto da
    causa entrou na linha, em 16/11: o rotulo foi inserido com `+` no meio da
    cadeia e quebrou o unico caminho que GRAVA.

    E O AUTOTESTE APROVAVA 81 AFIRMACOES, porque todas elas leem as linhas que
    JA ESTAO no banco e nenhuma MONTAVA uma — as tres linhas de quarentena de
    hoje nasceram antes do rotulo e foram retroajustadas por `--rotular`, que e
    outro caminho de codigo. E a familia que esta ilha mais paga: a regua existia
    e nao tinha falhado porque nao tinha rodado. Agora o portao chama esta
    funcao, e a conta nao e de opiniao: a linha montada tem de casar com
    `PADRAO_APOSENTADO`, que e o mesmo regex que o COLETOR le para recusar o
    anuncio na coleta seguinte.
    """
    return ('APOSENTADO EM %s — item %d da loja %d — %s — R$ %s, preco de %s, '
            'degrau %s da escada de chaves, encurtado %s, loja "%s" — '
            'CAUSA (%s): %s || ULTIMA MEDICAO: %s'
            % (em, int(a['item_id']), int(a['shop_id']), (a.get('titulo') or '').strip(),
               (('%.2f' % a['preco']).replace('.', ',')) if a.get('preco') is not None
               else 'sem preco',
               a.get('coletado_em'), a.get('degrau_da_escada'),
               a.get('url_afiliado') or 'sem encurtado', a.get('loja'),
               causa, (causa_prosa or '').strip(), (ultima_medicao or '').strip()))


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

    if args.causa not in col.CAUSAS_DE_APOSENTADORIA:
        print('REPROVADO: causa %r nao esta na lista do coletor (%s). O rotulo e o que a '
              'TELA conta para dizer a causa em palavras (25.11): causa nova se declara '
              'em `CAUSAS_DE_APOSENTADORIA`, com a frase de leitor dela, antes de ser '
              'usada aqui.' % (args.causa, ', '.join(sorted(col.CAUSAS_DE_APOSENTADORIA))))
        return 1

    linha = montar_linha(args.em, a, args.causa,
                         args.causa_prosa, args.ultima_medicao)

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
    # O ITEM QUE SAI AGORA ESTAVA DENTRO DO `ofertas_lidas` DESTA COLETA — ele foi
    # lido nela, e e por isso que ele estava em `anuncios`. Sem esta conta a soma da
    # afirmacao 3 nao fecha, e fecha-la com `len(anuncios_aposentados)` e o que
    # estava errado: ver o comentario dela.
    r['ofertas_aposentadas_nesta_coleta'] = int(r.get('ofertas_aposentadas_nesta_coleta') or 0) + 1
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
        json.dump(banco, f, ensure_ascii=False, indent=_recuo_do_banco())
        f.write('\n')
    print('\ngravado em %s' % os.path.relpath(BANCO, RAIZ))
    print('AGORA RODE: python3 ferramentas/gerar-vitrine-de-produto.py --gravar')
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--conferir', action='store_true', help='portao, sem rede')
    p.add_argument('--rotular', action='store_true',
                   help='poe o rotulo curto da causa numa linha de quarentena antiga '
                        '(pede --item e --causa)')
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
    if a.rotular:
        if a.item is None or not a.causa:
            print('REPROVADO: --rotular pede --item e --causa')
            return 1
        return rotular(a)
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
