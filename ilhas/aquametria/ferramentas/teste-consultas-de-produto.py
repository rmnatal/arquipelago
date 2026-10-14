#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A BANCADA da regua das consultas de produto. Sem rede, casos sinteticos.

    python3 ferramentas/teste-consultas-de-produto.py

O caso 1 e o mundo medido em 14/10/2026 na `luminaria de LED para aquario
plantado`: nove ocupantes, oito estrangeiros. E o caso que a regua existe para
nao ler como "busca aberta".
"""
import importlib.util
import json
import os
import sys

PASTA = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(PASTA)

afirmacoes = 0
falhas = []


def carregar(nome):
    caminho = os.path.join(PASTA, nome)
    spec = importlib.util.spec_from_file_location(nome.replace('-', '_')[:-3], caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


R = carregar('regua-consultas-de-produto.py')


def afirma(condicao, rotulo):
    global afirmacoes
    afirmacoes += 1
    if not condicao:
        falhas.append(rotulo)


def ocupante(url, classe, dedicada=None, vinda='c'):
    return {'url': url, 'titulo': 't', 'classe': classe,
            'dedicada_a_consulta': dedicada, 'vinda_da_consulta': vinda}


def consulta(ocupantes, **kw):
    base = {
        'id': 'x', 'consulta': 'c', 'familia': 'filtro', 'forma': 'cabeca',
        'intencao_de_compra': 'alta', 'por_que_a_intencao': 'porque',
        'produtos_reais_no_banco': 14, 'pagina_da_ilha_que_ja_serve': None,
        'varejo_grande_com_pagina_dedicada': None,
        'serp_vista_por': None, 'serp_vista_em': None,
        'evidencia': [{'consulta_do_instrumento': 'c', 'medido_como': 'busca',
                       'medido_em': '2026-10-14', 'enviesada': False}],
        'ocupantes': ocupantes,
    }
    base.update(kw)
    base.setdefault('veredito', R.veredito(base))
    nasce, _ = R.nasce_agora(base)
    base.setdefault('nasce_agora', nasce)
    return base


# ---------------------------------------------------------------------------
# CASO 1 — O MUNDO DE 14/10/2026: a busca derivou para fora e isso NAO e "aberta"
# ---------------------------------------------------------------------------
luminaria = consulta(
    [ocupante('https://www.mercadolivre.com.br/blog/mais-vendidos/lampadas-aquarios', 'varejo-grande', True)]
    + [ocupante('https://greenaqua.hu/%d' % i, 'fora-do-brasil') for i in range(8)])
afirma(len(R.ocupantes_br(luminaria)) == 1, 'caso 1: deveria contar 1 ocupante brasileiro de 9')
afirma(R.veredito(luminaria) == 'nao-medida',
       'caso 1: um ocupante brasileiro esta abaixo do piso e NAO sustenta veredito')
nasce, motivo = R.nasce_agora(luminaria)
afirma(nasce is False, 'caso 1: nao pode nascer')
afirma('14.9' in motivo, 'caso 1: o motivo tem de ser a SERP nao vista com os olhos, e foi %r' % motivo)

# E o contrario tambem: oito ocupantes BR que TODOS tomam, e a linha fecha.
tomada = consulta([ocupante('https://www.cobasi.com.br/c/%d' % i, 'varejo-grande', True) for i in range(4)]
                  + [ocupante('https://www.petz.com.br/p/%d' % i, 'varejo-grande') for i in range(4)])
afirma(R.veredito(tomada) == 'tomada', 'caso 1b: 4 dedicadas em 8 brasileiros e metade, logo tomada')
nasce, motivo = R.nasce_agora(tomada)
afirma(nasce is False and '30.5' in motivo, 'caso 1b: tomada fecha a linha pela 30.5')

# ---------------------------------------------------------------------------
# CASO 2 — `alvo` NAO EXISTE, E E ISSO QUE SEGURA O RASTREAMENTO
# ---------------------------------------------------------------------------
afirma('alvo' not in R.VEREDITOS, 'caso 2: `alvo` nao pode estar no vocabulario de veredito')
# Dez ocupantes brasileiros, nenhum que tome: a busca mais "aberta" possivel.
aberta = consulta([ocupante('https://lojinha%d.com.br/x' % i, 'lojinha-do-nicho') for i in range(10)])
afirma(R.veredito(aberta) == 'nao-medida',
       'caso 2: dez lojinhas e ZERO varejo grande ainda assim nao afirma `alvo`')
afirma(R.nasce_agora(aberta)[0] is False, 'caso 2: e nao autoriza pagina nova')
# Com olhos na SERP, a MESMA linha nasce. E a unica chave.
com_olhos = consulta([ocupante('https://lojinha%d.com.br/x' % i, 'lojinha-do-nicho') for i in range(10)],
                     serp_vista_por='Raphael, no Chrome dele', serp_vista_em='2026-10-15')
afirma(R.nasce_agora(com_olhos)[0] is True, 'caso 2: com `serp_vista_por` os quatro portoes abrem')

# ---------------------------------------------------------------------------
# CASO 3 — A 30.5 NOMEIA QUEM NAO TOMA, "SOZINHOS NEM SOMADOS"
# ---------------------------------------------------------------------------
for classe in R.CLASSES_QUE_NAO_TOMAM:
    c = consulta([ocupante('https://x%d.com.br/y' % i, classe, True) for i in range(10)])
    afirma(R.veredito(c) == 'nao-medida',
           'caso 3: dez paginas DEDICADAS da classe %r nao podem tomar a busca' % classe)

# ---------------------------------------------------------------------------
# CASO 4 — FICHA DE UM MODELO NAO E PAGINA DEDICADA A CONSULTA DE FAMILIA
# ---------------------------------------------------------------------------
# O mundo da `filtro hang on para aquario`: DEZ ocupantes brasileiros, OITO de
# varejo grande, e nenhum disputando a consulta.
hangon = consulta([ocupante('https://www.cobasi.com.br/filtro-%d/p' % i, 'varejo-grande') for i in range(5)]
                  + [ocupante('https://www.petz.com.br/produto/filtro-%d' % i, 'varejo-grande') for i in range(3)]
                  + [ocupante('https://www.mercadolivre.com.br/pagina/x', 'anuncio-marketplace'),
                     ocupante('https://www.buscape.com.br/x', 'agregador-de-ofertas')])
afirma(len(R.ocupantes_br(hangon)) == 10, 'caso 4: dez ocupantes brasileiros')
afirma(len(R.ocupantes_que_tomam(hangon)) == 0,
       'caso 4: oito paginas de varejo grande que nao sao dedicadas NAO tomam')
afirma(R.veredito(hangon) == 'nao-medida', 'caso 4: logo a linha fica nao medida')
# E a porta dos fundos: promover as oito a `dedicada` vira TOMADA. Se a regua
# nao visse isso, a coluna `dedicada_a_consulta` seria decorativa.
promovido = json.loads(json.dumps(hangon))
for o in promovido['ocupantes']:
    if o['classe'] == 'varejo-grande':
        o['dedicada_a_consulta'] = True
afirma(R.veredito(promovido) == 'tomada',
       'caso 4: a coluna `dedicada_a_consulta` tem de mudar o veredito, senao e decorativa')

# ---------------------------------------------------------------------------
# CASO 5 — O PISO DE OCUPANTE BRASILEIRO, NA FRONTEIRA
# ---------------------------------------------------------------------------
tres = consulta([ocupante('https://x%d.com.br/y' % i, 'varejo-grande', True) for i in range(3)]
                + [ocupante('https://y%d.co.uk/z' % i, 'fora-do-brasil') for i in range(6)])
afirma(R.veredito(tres) == 'nao-medida', 'caso 5: TRES brasileiros, todos tomando, ainda e amostra fina')
quatro = consulta([ocupante('https://x%d.com.br/y' % i, 'varejo-grande', True) for i in range(4)]
                  + [ocupante('https://y%d.co.uk/z' % i, 'fora-do-brasil') for i in range(6)])
afirma(R.veredito(quatro) == 'tomada', 'caso 5: QUATRO brasileiros tomando fecham')
afirma(R.PISO_DE_OCUPANTES_BR == 4, 'caso 5: o piso e quatro e esta escrito na regua')

# ---------------------------------------------------------------------------
# CASO 6 — OS QUATRO PORTOES DO `nasce_agora`, UM A UM, NA ORDEM DO CONTRATO
# ---------------------------------------------------------------------------
base_ok = dict(serp_vista_por='Raphael', serp_vista_em='2026-10-15')
livre = [ocupante('https://forum%d.com.br/t' % i, 'forum') for i in range(6)]

so_banco = consulta(livre, produtos_reais_no_banco=2, **base_ok)
nasce, motivo = R.nasce_agora(so_banco)
afirma(nasce is False and '30.2' in motivo, 'caso 6: dois produtos no banco fecham pela 30.2')

so_canibal = consulta(livre, pagina_da_ilha_que_ja_serve='/calculadora-de-vazao-do-filtro/', **base_ok)
nasce, motivo = R.nasce_agora(so_canibal)
afirma(nasce is False and '30.4' in motivo, 'caso 6: pagina que ja serve fecha pela 30.4')

so_olhos = consulta(livre)
nasce, motivo = R.nasce_agora(so_olhos)
afirma(nasce is False and '14.9' in motivo, 'caso 6: sem olhos na SERP fecha pela 14.9')

so_tomada = consulta([ocupante('https://x%d.com.br/y' % i, 'fazenda-de-conteudo', True) for i in range(6)], **base_ok)
nasce, motivo = R.nasce_agora(so_tomada)
afirma(nasce is False and '30.5' in motivo, 'caso 6: tomada fecha pela 30.5, antes de todos os outros')

tudo_aberto = consulta(livre, **base_ok)
afirma(R.nasce_agora(tudo_aberto)[0] is True, 'caso 6: os quatro portoes abertos deixam nascer')
# A ordem importa: a linha tomada E sem olhos tem de citar a 30.5, nao a 14.9.
dupla = consulta([ocupante('https://x%d.com.br/y' % i, 'fazenda-de-conteudo', True) for i in range(6)])
afirma('30.5' in R.nasce_agora(dupla)[1], 'caso 6: com dois portoes fechados, o motivo e o primeiro do contrato')

# `serp_vista_por` sem `serp_vista_em` nao vale: ausencia e reprovacao.
meio = consulta(livre, serp_vista_por='Raphael')
afirma(R.serp_vista_com_olhos(meio) is False, 'caso 6: quem viu sem quando nao conta')
afirma(R.nasce_agora(meio)[0] is False, 'caso 6: e nao deixa nascer')

# ---------------------------------------------------------------------------
# CASO 7 — A BUSCA ENVIESADA SO AFIRMA PRESENCA, E NAO ENTRA NA CONTAGEM
# ---------------------------------------------------------------------------
afirma(R.nomeia_loja('luminária LED para aquário comprar Cobasi Petz Mercado Livre') is True,
       'caso 7: consulta que nomeia loja e enviesada')
afirma(R.nomeia_loja('luminária de LED para aquário plantado') is False,
       'caso 7: consulta sem loja e neutra')
enviesada = consulta(
    [ocupante('https://www.cobasi.com.br/c/x', 'varejo-grande', True, vinda='x com Cobasi')],
    evidencia=[{'consulta_do_instrumento': 'x com Cobasi', 'medido_como': 'busca',
                'medido_em': '2026-10-14', 'enviesada': True}])
erros = R.erros_de_ocupantes(enviesada, 'x')
afirma(any('ENVIESADA' in e for e in erros),
       'caso 7: ocupante colhido por busca enviesada nao pode entrar na lista de ocupantes')
# E evidencia que se declara neutra nomeando loja e mentira detectavel.
mentira = consulta(livre, evidencia=[{'consulta_do_instrumento': 'filtro na Cobasi',
                                      'medido_como': 'busca', 'medido_em': '2026-10-14',
                                      'enviesada': False}])
afirma(any('nomeia loja' in e for e in R.erros_de_evidencia(mentira, 'x')),
       'caso 7: evidencia que nomeia loja e se declara neutra reprova')
# Nenhuma evidencia neutra = nao mediu SERP nenhuma.
so_enviesada = consulta(livre, evidencia=[{'consulta_do_instrumento': 'x Cobasi', 'medido_como': 'busca',
                                           'medido_em': '2026-10-14', 'enviesada': True}])
afirma(any('nenhuma evidencia neutra' in e for e in R.erros_de_evidencia(so_enviesada, 'x')),
       'caso 7: lista com so busca enviesada nao mediu SERP')

# ---------------------------------------------------------------------------
# CASO 8 — AUSENCIA E REPROVACAO, NAO OMISSAO TOLERADA
# ---------------------------------------------------------------------------
sem_enviesada = consulta(livre, evidencia=[{'consulta_do_instrumento': 'c', 'medido_como': 'busca',
                                            'medido_em': '2026-10-14'}])
afirma(any('`enviesada` tem de ser' in e for e in R.erros_de_evidencia(sem_enviesada, 'x')),
       'caso 8: `enviesada` ausente nao vale como false')
falso = consulta([dict(ocupante('https://x.com.br/y', 'varejo-grande'), dedicada_a_consulta=False)])
afirma(any('nunca False' in e or 'nunca false' in e.lower() for e in R.erros_de_ocupantes(falso, 'x')),
       'caso 8: `dedicada_a_consulta: false` e recusado; o valor de "nao medido" e null')
sem_url = consulta([{'titulo': 't', 'classe': 'forum', 'dedicada_a_consulta': None, 'vinda_da_consulta': 'c'}])
afirma(any('sem URL' in e for e in R.erros_de_ocupantes(sem_url, 'x')),
       'caso 8: a 30.5 exige a URL que sustenta o veredito')
orfao = consulta([ocupante('https://x.com.br/y', 'forum', vinda='consulta que ninguem declarou')])
afirma(any('que nao esta na evidencia' in e for e in R.erros_de_ocupantes(orfao, 'x')),
       'caso 8: ocupante tem de dizer de que consulta do instrumento veio')
sem_ocupantes = consulta([])
afirma(any('sem ocupantes' in e for e in R.erros_de_ocupantes(sem_ocupantes, 'x')),
       'caso 8: veredito sem ocupante nenhum nao existe')

# ---------------------------------------------------------------------------
# CASO 9 — O VEREDITO E O `nasce_agora` ESCRITOS TEM DE BATER COM OS CALCULADOS
# ---------------------------------------------------------------------------
mentiu_veredito = consulta([ocupante('https://x%d.com.br/y' % i, 'varejo-grande', True) for i in range(6)])
mentiu_veredito['veredito'] = 'nao-medida'
afirma(any('veredito escrito' in e for e in R.erros_da_consulta(mentiu_veredito, 'x')),
       'caso 9: veredito escrito diferente do calculado reprova')
inventou_alvo = consulta(livre)
inventou_alvo['veredito'] = 'alvo'
afirma(any('`alvo` nao existe' in e for e in R.erros_da_consulta(inventou_alvo, 'x')),
       'caso 9: escrever `alvo` reprova com o motivo nomeado')
mentiu_nasce = consulta(livre)
mentiu_nasce['nasce_agora'] = True
afirma(any('`nasce_agora` escrito' in e for e in R.erros_da_consulta(mentiu_nasce, 'x')),
       'caso 9: `nasce_agora` escrito diferente do calculado reprova')
sem_juizo = consulta(livre)
del sem_juizo['por_que_a_intencao']
afirma(any('JUIZO' in e for e in R.erros_da_consulta(sem_juizo, 'x')),
       'caso 9: intencao de compra sem o juizo escrito reprova')
banco_texto = consulta(livre, produtos_reais_no_banco='catorze')
afirma(any('inteiro contado' in e for e in R.erros_da_consulta(banco_texto, 'x')),
       'caso 9: lastro de banco tem de ser inteiro contado')

# ---------------------------------------------------------------------------
# CASO 10 — A ORDEM DA LISTA E A DO DESPACHO: INTENCAO DE COMPRA
# ---------------------------------------------------------------------------
alta_tomada = consulta([ocupante('https://x%d.com.br/y' % i, 'varejo-grande', True) for i in range(6)],
                       id='alta-tomada')
alta_livre = consulta(livre, id='alta-livre')
media = consulta(livre, id='media', intencao_de_compra='media')
ordem = [c['id'] for c in R.ordenada([media, alta_tomada, alta_livre])]
afirma(ordem == ['alta-livre', 'alta-tomada', 'media'],
       'caso 10: intencao primeiro, e dentro dela a nao tomada antes. Saiu %r' % ordem)

# ---------------------------------------------------------------------------
# CASO 11 — O ARQUIVO DE VERDADE PASSA, E O `.md` SAI DO JSON
# ---------------------------------------------------------------------------
with open(os.path.join(RAIZ, 'dados', 'consultas-de-produto.json'), encoding='utf-8') as f:
    reais = json.load(f)
afirma(R.erros(reais) == [], 'caso 11: o arquivo de verdade tem de passar a regua inteira. %r' % R.erros(reais)[:3])
md = R.render_md(reais)
afirma(R.render_md(reais) == md, 'caso 11: o gerador tem de ser deterministico')
# A palavra `alvo` APARECE no `.md`, e tem de aparecer: "consulta-alvo declarada"
# e o nome do campo das paginas da ilha, e o cabecalho explica por que o VEREDITO
# `alvo` nao existe. O que nao pode existir e uma linha de veredito dizendo alvo
# — entao a afirmacao mede a linha de veredito, nao a palavra solta. (A primeira
# versao desta afirmacao media a palavra e reprovou o arquivo correto.)
afirma('alvo' not in str(R.ROTULO_VEREDITO), 'caso 11: nenhum rotulo de veredito pode dizer alvo')
for linha in md.splitlines():
    if linha.startswith('- **veredito da SERP:**'):
        afirma('alvo' not in linha, 'caso 11: linha de veredito dizendo alvo: %r' % linha)
with open(os.path.join(RAIZ, 'dados', 'consultas-de-produto.md'), encoding='utf-8') as f:
    afirma(f.read() == md, 'caso 11: o `.md` no disco tem de ser o que a regua gera')
# Toda URL de ocupante do arquivo real aparece no `.md`: a 30.5 exige as URLs na tela.
for c in reais['consultas']:
    for o in c['ocupantes']:
        afirma(o['url'] in md, 'caso 11: a URL %s tem de aparecer no `.md`' % o['url'])

print('teste-consultas-de-produto: %d afirmacoes, %d falha(s).' % (afirmacoes, len(falhas)))
for f_ in falhas:
    print('  FALHOU: %s' % f_)
sys.exit(1 if falhas else 0)
