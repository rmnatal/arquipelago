#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Portao SEM REDE das duas funcoes que o item 2 do despacho de 07/10/2026 criou
em ferramentas/search-console.py: `totais()` e `por_pagina()`.

    python3 ferramentas/teste-search-console.py

POR QUE ELE EXISTE, e por que ele mede SO as funcoes puras. O defeito que o item
2 nomeia nao estava na chamada da API: estava na CONTA que o script fazia depois
dela. O script somava as linhas da dimensao `query` e chamava aquilo de
impressoes da ilha; o Google anonimiza a consulta de quase toda impressao de
cauda longa, e na aquametria, na janela de 07/10/2026, 370 das 371 impressoes
sairam anonimizadas. Resultado emitido: "1 impressao, 0 clique" para uma
propriedade que a Search Console mostrava com 371 e 3.

Uma conta errada nao precisa de rede para ser medida, e NAO HAVIA CREDENCIAL
NESTE AMBIENTE quando este portao foi escrito (GOOGLE_SA_B64, GOOGLE_SA_JSON e
GOOGLE_SA_FILE ausentes, conferidos em 14/10/2026). Entao o que este arquivo
mede e a conta, com a resposta da API ENCENADA a partir dos numeros que a
leitura de 07/10 registrou. O que ele NAO mede, e esta escrito para ninguem ler
verde aqui como entrega: que a chamada nova devolve o que se espera dela. Isso
so a passada com credencial diz, e e o que falta do item 2.

O CASO 1 E O MUNDO MEDIDO EM 07/10/2026, em pessoa: 371 impressoes e 3 cliques
na propriedade, contra 1 e 0 na soma da dimensao `query`.
"""
import importlib.util
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# O modulo tem hifen no nome e importa google-auth no topo, com um bootstrap de
# venv no except. Carregar por spec e ler o fonte sem executar o topo seria
# complicado; mais simples e honesto: injetamos um stub dos dois nomes que o
# topo importa, para a importacao nao sair comprando dependencia nenhuma.
for nome, atributos in (
    ('google', ()),
    ('google.oauth2', ('service_account',)),
    ('google.auth', ()),
    ('google.auth.transport', ()),
    ('google.auth.transport.requests', ('AuthorizedSession',)),
):
    if nome in sys.modules:
        continue
    modulo = type(sys)(nome)
    for atributo in atributos:
        setattr(modulo, atributo, object())
    sys.modules[nome] = modulo
sys.modules['google.oauth2'].service_account = object()
sys.modules['google.auth.transport.requests'].AuthorizedSession = object()

# NAO GRAVAR .pyc DESTE MODULO, e isto nao e higiene: e um portao que mentiu.
# Medido em 15/10/2026, rodando duas mutacoes contra este arquivo. A segunda troca
# "sem_veredito" por "nao_indexada" — DOZE caracteres pelos mesmos doze —, entao o
# fonte mutado tem o MESMO TAMANHO do bom. O `.pyc` que a rodada mutada gravou
# passou pela validacao do Python (mtime + tamanho) depois de o fonte ser
# restaurado no mesmo segundo, e o portao reprovou 13 afirmacoes contra um arquivo
# que estava correto em disco. **Portao que le bytecode velho relata um mundo que
# nao existe** — a mesma familia do "resumo velho lido como fato" da secao 4 do
# ARQUIPELAGO.md, um andar abaixo. Com as duas linhas, o portao le sempre o fonte.
sys.dont_write_bytecode = True
importlib.invalidate_caches()

spec = importlib.util.spec_from_file_location(
    'search_console', os.path.join(RAIZ, 'ferramentas', 'search-console.py'))
sc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sc)

contadas = [0]
falhas = []


def depois_de(texto, marca, ate=None):
    """O trecho de `texto` depois de `marca`, ou string vazia se a marca nao existe.

    Existe porque `texto.split(marca)[1]` ESTOURA quando a marca desaparece — e a
    marca desaparecer e exatamente a regressao que este portao existe para pegar.
    Portao que morre no defeito que ele vigia da sinal confuso em vez de reprovar:
    medido em 15/10/2026, mutando o conserto de tres estados de volta para dois.
    """
    if marca not in texto:
        return ''
    trecho = texto.split(marca, 1)[1]
    if ate and ate in trecho:
        trecho = trecho.split(ate, 1)[0]
    return trecho


def ok(nome, cond, extra=''):
    contadas[0] += 1
    print('  %s %s%s' % ('ok   ' if cond else 'FALHA', nome, (' — ' + extra) if extra else ''))
    if not cond:
        falhas.append(nome)


# ---------------------------------------------------------------- totais()
print('totais() — a consulta SEM dimensao')

# CASO 1: o mundo medido em 07/10/2026 na aquametria.
resposta = {'rows': [{'clicks': 3, 'impressions': 371, 'ctr': 0.0080862, 'position': 6.7}]}
t = sc.totais(resposta)
ok('caso 1: 371 impressoes, e nao as 1 que a dimensao query somava',
   t['impressoes'] == 371, str(t['impressoes']))
ok('caso 1: 3 cliques', t['cliques'] == 3, str(t['cliques']))
ok('caso 1: posicao media 6,7', abs(t['posicao'] - 6.7) < 0.001, str(t['posicao']))
ok('caso 1: declara que foi medido', t['medido'] is True)

# CASO 2: a API nao devolve linha. "Nao medido" NAO e "zero" — e a distincao que
# a leitura de 07/10 cobrou com estas palavras sobre o clique de afiliado:
# "nao e zero: e nao medido".
t = sc.totais({'rows': []})
ok('caso 2: resposta vazia devolve medido=False', t['medido'] is False)
ok('caso 2: resposta vazia devolve zeros, e nao None',
   (t['impressoes'], t['cliques']) == (0, 0), repr((t['impressoes'], t['cliques'])))
ok('caso 3: resposta ausente nao estoura', sc.totais(None)['medido'] is False)

# CASO 4: a API omite o ctr. O quociente manda, e nao um campo faltando.
t = sc.totais({'rows': [{'clicks': 1, 'impressions': 4, 'position': 8.1}]})
ok('caso 4: ctr recalculado quando a API nao o manda', abs(t['ctr'] - 0.25) < 1e-9, str(t['ctr']))
t = sc.totais({'rows': [{'clicks': 0, 'impressions': 0, 'position': 0}]})
ok('caso 5: zero impressao nao divide por zero', t['ctr'] == 0.0)

# -------------------------------------------------------------- por_pagina()
print('\npor_pagina() — a dimensao `page`, que o Google NAO anonimiza')

resposta = {'rows': [
    {'keys': ['https://aquametria.com.br/calculadora-de-litragem/'],
     'clicks': 0, 'impressions': 27, 'position': 9.1},
    {'keys': ['https://aquametria.com.br/peixes/bettas/quantos-litros-para-betta/'],
     'clicks': 1, 'impressions': 125, 'position': 8.1},
    {'keys': ['https://aquametria.com.br/peixes/acaras/quantos-litros-para-acara-bandeira/'],
     'clicks': 1, 'impressions': 23, 'position': 5.3},
]}
linhas = sc.por_pagina(resposta, 'aquametria.com.br')
ok('tres paginas entram', len(linhas) == 3, str(len(linhas)))
ok('a ordem e por impressao decrescente — a de 125 vem primeiro',
   linhas[0]['pagina'] == '/peixes/bettas/quantos-litros-para-betta/', linhas[0]['pagina'])
ok('o dominio sai do caminho', all(not x['pagina'].startswith('http') for x in linhas),
   linhas[1]['pagina'])
ok('a banda da pagina do betta e 4-10 (posicao 8,1)', linhas[0]['banda'] == '4-10', linhas[0]['banda'])
ok('a banda da acara-bandeira e 4-10 (posicao 5,3)',
   [x for x in linhas if x['posicao'] == 5.3][0]['banda'] == '4-10')
ok('pagina sem impressao sai com banda "sem impressão"',
   sc.por_pagina({'rows': [{'keys': ['https://x/y/'], 'clicks': 0, 'impressions': 0,
                            'position': 0}]}, 'x')[0]['banda'] == 'sem impressão')
ok('resposta vazia devolve lista vazia, e nao estoura', sc.por_pagina({'rows': []}, 'x') == [])
ok('resposta ausente devolve lista vazia', sc.por_pagina(None, 'x') == [])
ok('linha sem `keys` e descartada em vez de estourar',
   sc.por_pagina({'rows': [{'clicks': 0, 'impressions': 1, 'position': 2}]}, 'x') == [])

# A AFIRMACAO QUE AMARRA AS DUAS: a soma da dimensao `page` tem de poder bater com
# o total da propriedade, que e justamente o que a soma da dimensao `query` nao
# conseguia fazer.
soma_paginas = sum(x['impressoes'] for x in linhas)
ok('a soma da dimensao `page` deste caso da 175 — comparavel ao total, ao contrario da soma de `query`',
   soma_paginas == 175, str(soma_paginas))

# ------------------------------------------------- veredito_de_indexacao()
print('\ncaminho_de() — a chave que cruza o sitemap com a dimensao `page`')

ok('a home vira "/" e nao string vazia',
   sc.caminho_de('https://aquametria.com.br/', 'aquametria.com.br') == '/',
   repr(sc.caminho_de('https://aquametria.com.br/', 'aquametria.com.br')))
ok('dominio sem barra final tambem vira "/"',
   sc.caminho_de('https://aquametria.com.br', 'aquametria.com.br') == '/')
ok('caminho interno perde o dominio e mantem a barra',
   sc.caminho_de('https://aquametria.com.br/peixes/tetras/', 'aquametria.com.br') == '/peixes/tetras/')
ok('query e ancora saem da chave',
   sc.caminho_de('https://aquametria.com.br/x/?v=1#a', 'aquametria.com.br') == '/x/')
ok('http tambem e reconhecido',
   sc.caminho_de('http://aquametria.com.br/sobre/', 'aquametria.com.br') == '/sobre/')

print('\nimpressoes_por_caminho() — o mapa que prova indexacao sem veredito')
mapa = sc.impressoes_por_caminho([
    {'pagina': '/', 'impressoes': 4, 'posicao': 2.3, 'cliques': 0, 'banda': '1-3'},
    {'pagina': '/calculadora-de-litragem/', 'impressoes': 82, 'posicao': 8.1, 'cliques': 0, 'banda': '4-10'},
])
ok('a home entra no mapa com 4 impressoes', mapa.get('/') == 4, str(mapa.get('/')))
ok('a chave existe com e sem barra final — sitemap e Search Console discordam nisso',
   mapa.get('/calculadora-de-litragem') == 82 and mapa.get('/calculadora-de-litragem/') == 82)
ok('lista vazia devolve mapa vazio, e nao estoura', sc.impressoes_por_caminho([]) == {})
ok('lista ausente devolve mapa vazio', sc.impressoes_por_caminho(None) == {})

print('\nveredito_de_indexacao() — TRES estados, e o desconhecido nao e negativo')

# O CASO 1 E O MUNDO MEDIDO EM 14/10/2026: a URL Inspection nao devolveu
# indexStatusResult nenhum para a home da aquametria, e o script antigo imprimiu
# `- / — ?` na lista de nao indexadas.
v = sc.veredito_de_indexacao({}, 4)
ok('caso 1 (home da aquametria, 14/10): sem veredito + 4 impressoes = INDEXADA',
   v['estado'] == 'indexada', v['estado'])
ok('caso 1: a fonte diz que foi a impressao, nao a URL Inspection',
   v['fonte'].startswith('impressão'), v['fonte'])
ok('caso 1: a fonte traz o numero de impressoes que a sustenta', '4' in v['fonte'], v['fonte'])

# Sem veredito E sem impressao: ninguem sabe, e e isso que tem de sair escrito.
v = sc.veredito_de_indexacao({}, 0)
ok('caso 2: sem veredito e sem impressao = SEM VEREDITO, nao "nao indexada"',
   v['estado'] == 'sem_veredito', v['estado'])
ok('caso 2: a cobertura sai como "sem veredito" e nao como "?"',
   v['cobertura'] == 'sem veredito', v['cobertura'])

# VERDICT_UNSPECIFIED e o `?` literal sao a mesma coisa que veredito ausente.
for valor in ('VERDICT_UNSPECIFIED', '?', ''):
    v = sc.veredito_de_indexacao(
        {'inspectionResult': {'indexStatusResult': {'verdict': valor}}}, 0)
    ok('caso 3: verdict %r conta como desconhecido' % valor, v['estado'] == 'sem_veredito', v['estado'])

v = sc.veredito_de_indexacao({'inspectionResult': {'indexStatusResult': {
    'verdict': 'PASS', 'coverageState': 'Submitted and indexed'}}}, 82)
ok('caso 4: PASS = indexada, e a fonte e a URL Inspection',
   v['estado'] == 'indexada' and v['fonte'] == 'URL Inspection', v['fonte'])

# As DUAS maes de 14/10: Discovered - currently not indexed. Continuam NOMEADAS
# como nao indexadas — o conserto do desconhecido nao pode absolve-las.
v = sc.veredito_de_indexacao({'inspectionResult': {'indexStatusResult': {
    'verdict': 'NEUTRAL', 'coverageState': 'Discovered - currently not indexed'}}}, 0)
ok('caso 5 (/peixes/tetras/, 14/10): NEUTRAL com cobertura = NAO INDEXADA',
   v['estado'] == 'nao_indexada', v['estado'])
ok('caso 5: a cobertura da API e preservada para a URL sair nomeada',
   v['cobertura'] == 'Discovered - currently not indexed', v['cobertura'])
ok('caso 5: sem impressao, nao ha divergencia a acusar', v['divergencia'] == '')

v = sc.veredito_de_indexacao({'inspectionResult': {'indexStatusResult': {
    'verdict': 'FAIL', 'coverageState': 'Excluded by noindex tag'}}}, 0)
ok('caso 6: FAIL = nao indexada', v['estado'] == 'nao_indexada', v['estado'])

# O CONTRARIO do defeito de 14/10: veredito negativo em URL COM impressao. A conta
# mantem o veredito, e a contradicao sai escrita em vez de passar em silencio.
v = sc.veredito_de_indexacao({'inspectionResult': {'indexStatusResult': {
    'verdict': 'NEUTRAL', 'coverageState': 'Crawled - currently not indexed'}}}, 9)
ok('caso 7: veredito negativo com impressao continua NAO INDEXADA (o veredito manda)',
   v['estado'] == 'nao_indexada', v['estado'])
ok('caso 7: mas a divergencia do instrumento sai acusada',
   'impress' in v['divergencia'] and 'NEUTRAL' in v['divergencia'], v['divergencia'])

ok('caso 8: resposta None nao estoura',
   sc.veredito_de_indexacao(None, 0)['estado'] == 'sem_veredito')
ok('caso 9: inspectionResult presente e vazio nao estoura',
   sc.veredito_de_indexacao({'inspectionResult': {}}, 0)['estado'] == 'sem_veredito')

# ---------------------------------------------------- resumo_de_indexacao()
print('\nresumo_de_indexacao() — a conta que tem de dar 50 de 52 na aquametria de 14/10')

# O MUNDO DE 14/10/2026, INTEIRO: 52 URLs no sitemap. 49 com PASS, a home sem
# veredito (4 impressoes, logo indexada), /peixes/acaras/ e /peixes/tetras/ em
# "Discovered - currently not indexed". O script antigo publicou 49; o honesto e 50.
detalhes = []
for i in range(49):
    d = sc.veredito_de_indexacao({'inspectionResult': {'indexStatusResult': {
        'verdict': 'PASS', 'coverageState': 'Submitted and indexed'}}}, 1)
    d['url'], d['caminho'] = 'https://aquametria.com.br/p%d/' % i, '/p%d/' % i
    detalhes.append(d)
home = sc.veredito_de_indexacao({}, 4)
home['url'], home['caminho'] = 'https://aquametria.com.br/', '/'
detalhes.append(home)
for caminho in ('/peixes/acaras/', '/peixes/tetras/'):
    d = sc.veredito_de_indexacao({'inspectionResult': {'indexStatusResult': {
        'verdict': 'NEUTRAL', 'coverageState': 'Discovered - currently not indexed'}}}, 0)
    d['url'], d['caminho'] = 'https://aquametria.com.br' + caminho, caminho
    detalhes.append(d)

r = sc.resumo_de_indexacao(detalhes, 52)
ok('O NUMERO DO DESPACHO: a aquametria de 14/10 sai com 50 indexadas, e nao 49',
   r['indexadas'] == 50, str(r['indexadas']))
ok('as duas maes continuam contadas como nao indexadas',
   r['nao_indexadas'] == 2, str(r['nao_indexadas']))
ok('nenhuma sobra em "sem veredito": a home saiu dela pela impressao',
   r['sem_veredito'] == 0, str(r['sem_veredito']))
ok('uma delas conta por impressao medida, e isso sai separado',
   r['por_impressao'] == 1, str(r['por_impressao']))
ok('o total continua sendo o do sitemap', r['total'] == 52, str(r['total']))
ok('as tres contas somam o total — nenhuma URL se perde no caminho',
   r['indexadas'] + r['nao_indexadas'] + r['sem_veredito'] == 52)
ok('a taxa sai 96% e nao 94%', round(r['pct']) == 96, '%.1f' % r['pct'])
ok('sem desconhecido sobrando, piso e teto coincidem', round(r['pct']) == round(r['pct_teto']))
ok('nenhuma divergencia neste mundo', r['divergencias'] == [])

# A REGRESSAO QUE ESTE PORTAO EXISTE PARA PEGAR: se o desconhecido voltar a ser
# somado as nao indexadas, esta afirmacao cai.
sem = [d for d in detalhes if d['estado'] == 'sem_veredito']
ok('a home nao esta na lista de nao indexadas',
   all(d['caminho'] != '/' for d in r['lista_nao_indexadas']),
   str([d['caminho'] for d in r['lista_nao_indexadas']]))

# O MESMO MUNDO, mas SEM a impressao da home: o instrumento nao soube e nao
# tinha a segunda medicao. Aqui o honesto e 49 com UMA desconhecida de fora, e a
# taxa sai como FAIXA — nunca uma taxa unica sobre denominador com desconhecido.
detalhes2 = [d for d in detalhes if d['caminho'] != '/']
h2 = sc.veredito_de_indexacao({}, 0)
h2['url'], h2['caminho'] = 'https://aquametria.com.br/', '/'
detalhes2.append(h2)
r2 = sc.resumo_de_indexacao(detalhes2, 52)
ok('sem impressao da home: 49 indexadas, 2 nao indexadas, 1 SEM VEREDITO',
   (r2['indexadas'], r2['nao_indexadas'], r2['sem_veredito']) == (49, 2, 1),
   repr((r2['indexadas'], r2['nao_indexadas'], r2['sem_veredito'])))
ok('a desconhecida NAO engorda as nao indexadas — continuam 2, e nao 3',
   r2['nao_indexadas'] == 2, str(r2['nao_indexadas']))
ok('a taxa sai como faixa: piso 94%, teto 96%',
   (round(r2['pct']), round(r2['pct_teto'])) == (94, 96),
   repr((round(r2['pct']), round(r2['pct_teto']))))
ok('a sem veredito sai nomeada na lista propria',
   [d['caminho'] for d in r2['lista_sem_veredito']] == ['/'],
   str([d['caminho'] for d in r2['lista_sem_veredito']]))

# A divergencia do caso 7 chega ao resumo.
d7 = sc.veredito_de_indexacao({'inspectionResult': {'indexStatusResult': {
    'verdict': 'NEUTRAL', 'coverageState': 'Crawled - currently not indexed'}}}, 9)
d7['url'], d7['caminho'] = 'https://x/z/', '/z/'
r3 = sc.resumo_de_indexacao([d7], 1)
ok('a divergencia do instrumento chega ao resumo para ser impressa',
   len(r3['divergencias']) == 1, str(len(r3['divergencias'])))

ok('lista vazia nao divide por zero', sc.resumo_de_indexacao([], 0)['pct'] is None)
ok('sem total informado, o total e o tamanho da lista',
   sc.resumo_de_indexacao([home])['total'] == 1)

# ------------------------------------------------ relatorio_de_indexacao()
print('\nrelatorio_de_indexacao() — o que o script IMPRIME, conferido sem rede')

import datetime as _dt
HOJE = _dt.date(2026, 10, 14)

rel = sc.relatorio_de_indexacao(HOJE, ['x'] * 52, r, 509, 4)
serie, blocos = rel['serie'], rel['urls']
texto_serie, texto_blocos = '\n'.join(serie), '\n'.join(blocos)

ok('a linha da serie traz 52, 50 e 96% — e nao 49 e 94%',
   '| 2026-10-14 | 52 | 50 | 96% | 509 | 4 |' in texto_serie,
   serie[1] if len(serie) > 1 else '(vazia)')
ok('a nota das TRES contas sai por extenso',
   '3 estados' in texto_serie.replace('TRÊS', '3'), '')
ok('a nota diz que 1 conta por impressao medida', 'impressão medida' in texto_serie)

# A METADE DO CRITERIO QUE E SOBRE IMPRESSAO: a home sai em secao propria de
# "sem veredito", e NAO na lista de nao indexadas.
ok('existe a secao propria de "SEM VEREDITO ... INDEXADAS por impressao medida"',
   '### URLs SEM VEREDITO da URL Inspection, mas INDEXADAS por impressão medida' in texto_blocos)
bloco_nao = depois_de(texto_blocos, '### URLs não indexadas (URL Inspection)', '###')
ok('a home NAO aparece na secao de nao indexadas',
   bool(bloco_nao) and '\n- / —' not in bloco_nao, bloco_nao.strip() or '(secao ausente)')
ok('as duas maes aparecem na secao de nao indexadas, nomeadas com a cobertura',
   '- /peixes/acaras/ — Discovered - currently not indexed' in bloco_nao
   and '- /peixes/tetras/ — Discovered - currently not indexed' in bloco_nao)
bloco_sem_ver = depois_de(texto_blocos, 'mas INDEXADAS por impressão medida')
ok('a home aparece nessa secao propria, com o numero de impressoes que a sustenta',
   '- / — impressão medida (4 na janela)' in bloco_sem_ver, bloco_sem_ver.strip() or '(secao ausente)')
ok('a secao das sem veredito diz que nenhuma SOBROU, e nao que todas tiveram veredito',
   'nenhuma sobrou sem conta: 1 sem veredito resolvida(s) por impressão medida' in texto_blocos,
   [l for l in blocos if 'nenhuma' in l] and str([l for l in blocos if 'nenhuma' in l]) or '')
ok('e no mundo em que TODAS tiveram veredito, a frase e a outra',
   '(nenhuma — a URL Inspection deu veredito para toda URL do sitemap)'
   in '\\n'.join(sc.relatorio_de_indexacao(HOJE, ['x'], sc.resumo_de_indexacao(
       [dict(sc.veredito_de_indexacao({'inspectionResult': {'indexStatusResult': {
           'verdict': 'PASS', 'coverageState': 'ok'}}}, 1), url='u', caminho='/u/')], 1),
       1, 0)['urls']))

# O MESMO MUNDO SEM A IMPRESSAO DA HOME: ela vai para a secao de desconhecido e
# a taxa sai como faixa. A home continua FORA das nao indexadas.
rel2 = sc.relatorio_de_indexacao(HOJE, ['x'] * 52, r2, 509, 4)
t2s, t2b = '\n'.join(rel2['serie']), '\n'.join(rel2['urls'])
ok('sem a impressao: a linha da serie cai para 49 e 94%',
   '| 2026-10-14 | 52 | 49 | 94% | 509 | 4 |' in t2s, rel2['serie'][1])
ok('sem a impressao: a taxa sai como FAIXA entre 94% e 96%',
   'entre 94% e 96%' in t2s, t2s)
bloco_nao2 = depois_de(t2b, '### URLs não indexadas (URL Inspection)', '###')
ok('sem a impressao: a home AINDA fica fora das nao indexadas',
   bool(bloco_nao2) and '\n- / —' not in bloco_nao2, bloco_nao2.strip() or '(secao ausente)')
ok('sem a impressao: a home sai na secao de SEM VEREDITO, escrita como desconhecido',
   '- / — **desconhecido**' in t2b, t2b)

# Sitemap nao lido: a parte de URL nao existe e o motivo sai escrito.
rel3 = sc.relatorio_de_indexacao(HOJE, [], sc.resumo_de_indexacao([], 0), 0, 0, 'HTTP 404')
ok('sitemap nao lido: a serie sai com n/d e o erro escrito',
   "| n/d | n/d | n/d |" in '\n'.join(rel3['serie']) and 'HTTP 404' in '\n'.join(rel3['serie']),
   '\n'.join(rel3['serie']))
ok('sitemap nao lido: nao ha bloco de URL nenhum', rel3['urls'] == [])

# O aviso de sitemap com XML valido em 404 continua chegando ao relatorio.
rel4 = sc.relatorio_de_indexacao(HOJE, ['x'] * 52, r, 509, 4, '', ['DEFEITO: sitemap em 404'])
ok('aviso de defeito do sitemap chega ao relatorio',
   'DEFEITO: sitemap em 404' in '\n'.join(rel4['serie']))

# A divergencia do instrumento sai impressa.
rel5 = sc.relatorio_de_indexacao(HOJE, ['x'], r3, 9, 0)
ok('a divergencia do instrumento sai impressa com a URL e o motivo',
   'DIVERGÊNCIA DO INSTRUMENTO' in '\n'.join(rel5['urls'])
   and '- /z/ — veredito NEUTRAL com 9 impressão' in '\n'.join(rel5['urls']),
   '\n'.join(rel5['urls']))

# ------------------------------------------------------------- main() inteiro
print('\nmain() de ponta a ponta, com a API ENCENADA — a fiacao, nao so as contas')

# POR QUE ESTE BLOCO EXISTE: as funcoes puras acima podem estar todas certas e o
# `main()` continuar chamando a antiga, ou passando o argumento trocado. Foi
# exatamente assim que o defeito de 14/10/2026 nasceu — a conta estava num lugar
# e a classificacao noutro. Aqui o `main()` roda inteiro, com a sessao da API
# encenada a partir do mundo que a leitura de 14/10 mediu, sem credencial e sem
# rede. O que ele NAO prova continua sendo o mesmo: que a API de verdade devolve
# o que se espera dela. Isso so a passada com credencial diz.

import contextlib
import datetime as _dt
import io as _io

DOM = 'aquametria.com.br'
URLS_52 = ['https://%s/' % DOM] + ['https://%s/p%d/' % (DOM, i) for i in range(49)] + [
    'https://%s/peixes/acaras/' % DOM, 'https://%s/peixes/tetras/' % DOM]

PASS = {'inspectionResult': {'indexStatusResult': {
    'verdict': 'PASS', 'coverageState': 'Submitted and indexed'}}}
DISCOVERED = {'inspectionResult': {'indexStatusResult': {
    'verdict': 'NEUTRAL', 'coverageState': 'Discovered - currently not indexed'}}}


class _Resposta(object):
    def __init__(self, carga):
        self._carga = carga

    def json(self):
        return self._carga


class _SessaoEncenada(object):
    """A Search Console do dia 14/10/2026, de memoria: 509 impressoes e 4 cliques
    na propriedade, 40 linhas por pagina, a home sem veredito e as duas maes em
    "Discovered". A home tem 4 impressoes na posicao 2,3 — e e isso que a prova
    indexada quando a URL Inspection nao devolve veredito para ela."""

    def get(self, rota, **kw):
        return _Resposta({'siteEntry': [{'siteUrl': 'sc-domain:%s' % DOM}]})

    def post(self, rota, json=None, **kw):
        corpo = json or {}
        if 'urlInspection' in rota:
            u = corpo.get('inspectionUrl', '')
            if u.endswith('/peixes/acaras/') or u.endswith('/peixes/tetras/'):
                return _Resposta(DISCOVERED)
            if u == 'https://%s/' % DOM:
                return _Resposta({})            # <- o defeito de 14/10: veredito nenhum
            return _Resposta(PASS)
        dims = corpo.get('dimensions')
        if dims == []:
            return _Resposta({'rows': [{'clicks': 4, 'impressions': 509,
                                        'ctr': 0.00786, 'position': 6.4}]})
        if dims == ['page']:
            return _Resposta({'rows': [
                {'keys': ['https://%s/' % DOM], 'clicks': 0, 'impressions': 4, 'position': 2.3},
                {'keys': ['https://%s/p0/' % DOM], 'clicks': 2, 'impressions': 82, 'position': 8.1},
            ]})
        # a dimensao `query`: ANONIMIZADA EM 100% nesta ilha, medido em 14/10.
        return _Resposta({'rows': []})


_credenciais, _sitemap, _argv = sc.credenciais, sc.urls_do_sitemap, sys.argv
_sessao_real = getattr(sc, 'AuthorizedSession', None)
try:
    sc.credenciais = lambda: None
    sc.AuthorizedSession = lambda cred: _SessaoEncenada()
    sc.urls_do_sitemap = lambda dominio: (sorted(URLS_52), '', [])
    sys.argv = ['search-console.py', 'aquametria']
    saida = _io.StringIO()
    with contextlib.redirect_stdout(saida):
        sc.main()
    texto = saida.getvalue()
finally:
    sc.credenciais, sc.urls_do_sitemap, sys.argv = _credenciais, _sitemap, _argv
    if _sessao_real is not None:
        sc.AuthorizedSession = _sessao_real

hoje = _dt.date.today().isoformat()
ok('main() roda inteiro sem estourar e emite relatorio', len(texto) > 500, '%d chars' % len(texto))
ok('O NUMERO DO DESPACHO, pelo main() inteiro: 52 URLs, 50 indexadas, 96%',
   '| %s | 52 | 50 | 96%% | 509 | 4 |' % hoje in texto,
   str([l for l in texto.splitlines() if l.startswith('| %s |' % hoje)]) or '(linha nao encontrada)')
ok('o total da propriedade e 509 e nao a soma de `query`, que e ZERO nesta ilha',
   '**509 impressão(ões)**' in texto and 'dá 0 impressão(ões)' in texto)
bloco_nao = depois_de(texto, '### URLs não indexadas (URL Inspection)', '###')
ok('a home NAO sai na lista de nao indexadas — era `- / — ?` no script antigo',
   bool(bloco_nao) and '\n- / —' not in bloco_nao, bloco_nao.strip() or '(secao ausente)')
ok('as duas maes saem nomeadas como nao indexadas',
   '- /peixes/acaras/ — Discovered - currently not indexed' in bloco_nao
   and '- /peixes/tetras/ — Discovered - currently not indexed' in bloco_nao)
ok('a home sai em secao propria de SEM VEREDITO, com as 4 impressoes que a sustentam',
   '### URLs SEM VEREDITO da URL Inspection, mas INDEXADAS por impressão medida' in texto
   and '- / — impressão medida (4 na janela)' in texto)
ok('o caractere `?` nao aparece mais como status de URL nenhuma',
   ' — ?' not in texto, str([l for l in texto.splitlines() if ' — ?' in l]))

print('\n' + '=' * 70)
print('%d afirmacoes, %d falha(s).' % (contadas[0], len(falhas)))
for f in falhas:
    print('  FALHA  ' + f)
sys.exit(1 if falhas else 0)
