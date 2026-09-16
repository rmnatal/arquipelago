#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra a escada de compra de proposito e exige REPROVACAO PELA REGRA QUE NOMEIA.

    python3 ferramentas/mutacoes-escada.py

POR QUE ESTE ARQUIVO EXISTE
---------------------------
"A PROVA DE QUE UMA TRAVA REPROVA E PARTE DO BLOCO" (secao 8 do ARQUIPELAGO.md).
Trava escrita e trava suposta; trava que alguem viu reprovar e trava medida.

DUAS EXIGENCIAS MAIS DURAS QUE O DE COSTUME, E CADA UMA TEM CICATRIZ
---------------------------------------------------------------------
1. CADA MUTACAO DECLARA QUAL PORTAO TEM DE REPROVA-LA E COM QUE PALAVRA. Defeito
   pego pela regra vizinha prova que ALGUMA trava existe, nao que ESTA existe — e
   uma bateria que se contenta com "reprovou" pode estar medindo, passada apos
   passada, a contagem do cabecalho em vez da regra que ela diz cobrar. O runner
   confere a palavra na saida do portao.

2. AS MUTACOES QUE PRODUZEM O MUNDO SAO A MAIORIA, E TINHAM DE SER. Hoje esta ilha
   tem 62 itens publicaveis e ZERO com ficha de produto: nenhum `url`, nenhum
   `degrau`, nenhum `url_produto`. Ou seja, as travas que cuidam da FICHA nasceram
   hoje sobre um banco que nunca as exercita — exatamente a "regua escrita para um
   mundo que nunca aconteceu" que a secao 8 descreve, a que "parece saudavel desde
   sempre" porque nunca pode falhar. Entao as quatro ultimas mutacoes criam o
   PRIMEIRO link de afiliado desta ilha dentro do mundo de bancada e so depois
   quebram a regra nele. A ultima e a UNICA que tem de passar: mundo novo sem
   defeito nao pode reprovar, ou a regua seria falso-positivo esperando o dia em
   que a monetizacao comecar.

E UM CUIDADO QUE JA CUSTOU BLOCO NESTA CASA: mutacao que reprova PELO MOTIVO ERRADO
e tao ruim quanto mutacao inerte. Dar ficha a um item muda `itens_com_ficha` e
`itens_com_piso_nao_rastreavel` no cabecalho, e o validador confere as duas contagens — sem
reescreve-las, toda mutacao do mundo novo reprovaria pela contagem e nenhuma delas
tocaria a regra que nomeia. Por isso o helper que cria o link CONSERTA o cabecalho
antes de entregar o mundo.
"""

import json
import os
import shutil
import subprocess
from urllib.parse import quote
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VALIDADOR = 'ferramentas/validar-banco.py'
PORTAO = 'ferramentas/teste-escada-compra.py'
GERADOR = 'ferramentas/gerar-busca-de-produto.py'
ESQUEMA = 'dados/esquema-banco.json'
MARCAS = 'dados/marcas.json'
MODELOS = 'dados/modelos-robo.json'
PECAS = 'dados/pecas.json'
MEDICAO = 'dados/palavras-chave-medidas.json'

INDENT = {MARCAS: 1, ESQUEMA: 1, MODELOS: 2, PECAS: 1, MEDICAO: 1}

ALVO_MODELO = 'xiaomi-s20'
ALVO_PECA = 'wap-escova-direita-w300'


def _ler_json(base, rel):
    with open(os.path.join(base, rel), encoding='utf-8') as f:
        return json.load(f)


def _gravar_json(base, rel, d):
    with open(os.path.join(base, rel), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=INDENT[rel])
        f.write('\n')


def _registro(d, ident):
    for r in d['registros']:
        if r['id'] == ident:
            return r
    raise AssertionError('%s nao esta mais no banco — a mutacao seria inerte' % ident)


def _refazer_contagem(d):
    """O cabecalho volta a bater com o arquivo. Ver o cuidado no topo: sem isto a
    mutacao reprovaria pela contagem e nunca chegaria na regra que ela nomeia."""
    pub = [r for r in d['registros'] if r['status'] == 'publicavel']
    c = d['contagem']
    # `itens_com_ficha` CONTAVA O LINK DE AFILIADO, igual ao validador contava —
    # as duas copias do mesmo engano, erradas juntas, que e o estado em que uma
    # afirmacao fica verde sem medir nada. Corrigido nos dois lugares em
    # 16/09/2026, quando a Open API da Shopee fez a ficha existir e os dois
    # numeros deixarem de coincidir em zero.
    c['itens_com_ficha'] = sum(1 for r in pub if r['afiliado'].get('url_produto'))
    c['itens_com_link_de_afiliado'] = sum(1 for r in pub if r['afiliado']['url'])
    c['itens_com_foto'] = sum(1 for r in pub if (r.get('imagem') or {}).get('url'))
    c['itens_sem_saida_de_compra'] = sum(
        1 for r in pub if not (r['afiliado']['url'] or r['afiliado']['url_busca']
                               or r['afiliado']['url_busca_produto']))
    c['itens_com_piso_nao_rastreavel'] = sum(
        1 for r in pub if not r['afiliado']['url'] and not r['afiliado']['url_busca']
        and r['afiliado']['url_busca_produto'])
    c['links_sem_degrau'] = sum(1 for r in pub if r['afiliado']['url']
                                and r['afiliado']['degrau'] is None)
    c['esperando_link_de_afiliado'] = sum(1 for r in pub if not r['afiliado']['url'])


def _dar_ficha(base, rel, ident, **campos):
    """PRODUZ O MUNDO: o primeiro link de afiliado da ilha, so que de bancada.

    O padrao e um link SAO — degrau 1, url crua guardada, piso ja encurtado — e
    cada mutacao estraga um campo por vez a partir dele. Assim o que reprova e o
    campo estragado, nunca o resto.
    """
    d = _ler_json(base, rel)
    r = _registro(d, ident)
    a = r['afiliado']
    a['url'] = 'https://s.shopee.com.br/MUNDO-DE-BANCADA'
    a['url_produto'] = 'https://shopee.com.br/loja-oficial/produto-de-bancada-i.1.2'
    a['motivo_sem_url_produto'] = None
    a['degrau'] = 1
    a['url_busca'] = 'https://s.shopee.com.br/BUSCA-DE-BANCADA'
    a['motivo_sem_url_busca'] = None
    a['plataforma'] = 'shopee'
    a['coletado_em'] = '2026-09-13'
    a['conferido_em'] = '2026-09-13'
    a.update(campos)
    # E AS CONTAGENS DO CABECALHO ANDAM JUNTO. Sem isto a mutacao reprova por
    # um numero de cabecalho desatualizado em vez de pela regra que ela nomeia —
    # e a unica que TEM de passar (m16) reprovaria por um defeito que ela mesma
    # criou. Descoberto em 16/09/2026, quando as chaves itens_com_ficha,
    # itens_com_link_de_afiliado e itens_com_foto passaram a ser conferidas.
    _refazer_contagem(d)
    # `intestavel` e DERIVADO no banco de verdade, entao o mundo de bancada tambem o
    # deriva — DEPOIS do update, para a mutacao que estraga `url_produto` continuar
    # reprovando pela regra que ela NOMEIA (a URL crua que falta) e nao por um campo
    # derivado que ficou desatualizado de tabela. Mutacao que reprova pelo motivo
    # errado e verde com outro nome: ela mede a trava que ninguem escreveu.
    if 'intestavel' not in campos:
        a['intestavel'] = bool(a['url'] and not a['url_produto'])
    _refazer_contagem(d)
    _gravar_json(base, rel, d)


# ------------------------------------------------------------------ AS MUTACOES
def m01_piso_apagado(base):
    """O item publicavel perde a palavra-chave. E o estado em que a ilha inteira
    estava ate hoje, e a 25.2 o chama de defeito da 19.1 em qualquer degrau."""
    d = _ler_json(base, MODELOS)
    _registro(d, ALVO_MODELO)['afiliado']['url_busca_produto'] = ''
    _gravar_json(base, MODELOS, d)


def m02_busca_sem_contexto(base):
    """A chave perde o termo de contexto e vira "Xiaomi S20". E a armadilha da
    25.3 na forma que so esta ilha tem: S20 sozinho e um celular de outra marca, e
    a busca devolveria capinha de telefone para quem procura peca de robo."""
    d = _ler_json(base, MODELOS)
    a = _registro(d, ALVO_MODELO)['afiliado']
    a['url_busca_produto'] = a['url_busca_produto'].replace('%20robo%20aspirador', '')
    _gravar_json(base, MODELOS, d)


def m03_busca_so_por_marca(base):
    """A chave perde o codigo do modelo e sobra "Xiaomi robo aspirador" — busca de
    marca, nao de produto. Passaria pela trava do contexto e mesmo assim mandaria o
    leitor para a vitrine inteira do fabricante."""
    d = _ler_json(base, MODELOS)
    a = _registro(d, ALVO_MODELO)['afiliado']
    a['url_busca_produto'] = ('https://shopee.com.br/search?keyword='
                              'Xiaomi%20robo%20aspirador')
    _gravar_json(base, MODELOS, d)


def m04_peca_ganha_o_codigo(base):
    """A peca passa a levar o codigo de fabricante na chave. NAO e um defeito
    obvio — parece melhoria — e e por isso que ela esta aqui: a decisao de deixar
    o codigo de fora esta escrita no esquema com a medicao que falta, e decisao que
    nenhum portao mede vira folclore. Quem inverter isto um dia tem de inverter a
    trava junto, e explicar com que medicao."""
    d = _ler_json(base, PECAS)
    a = _registro(d, ALVO_PECA)['afiliado']
    a['url_busca_produto'] = ('https://shopee.com.br/search?keyword='
                              'WAP%20FC9899%20escova%20lateral%20robo%20aspirador')
    r = _registro(d, ALVO_PECA)
    r['codigo_fabricante'] = 'FC9899'
    r.pop('motivo_sem_codigo', None)
    _gravar_json(base, PECAS, d)


def _multi_volta_ao_nome_de_tela(base):
    d = _ler_json(base, MARCAS)
    for m in d['registros']:
        if m['id'] == 'multi':
            if m['nome_de_busca'] == m['nome']:
                raise AssertionError('nome_de_busca ja era o nome de tela — inerte')
            m['nome_de_busca'] = m['nome']
    _gravar_json(base, MARCAS, d)


def m05_nome_de_busca_vira_o_de_tela(base):
    """A marca volta a ser buscada pelo `nome` de tela E O BANCO E REGERADO.

    QUEM PEGA MUDOU EM 16/09/2026, E A MUDANCA E UM ENDURECIMENTO. Antes da medicao
    de palavra-chave, regerar escrevia "Multi (ex-Multilaser)" dentro da consulta e
    quem reprovava era o PORTAO DA ESCADA, pelo parentese. Agora a chave gravada e a
    chave MEDIDA, e regerar nao consegue mais injetar o nome de tela em lugar
    nenhum: o defeito fica preso dentro do `marcas.json` e quem o pega e o
    VALIDADOR, que le a marca do arquivo em vez de confiar na chave. O buraco que
    isso poderia abrir — chave medida que ninguem mais confere contra a marca — esta
    fechado pela mesma afirmacao que pega a m05b, e as duas mutacoes provam a mesma
    trava por caminhos diferentes de proposito: uma regerando, a outra nao.

    A PRIMEIRA VERSAO DESTA MUTACAO ERA INERTE E QUEM MOSTROU FOI A BATERIA: ela
    so editava o marcas.json, e o portao seguia verde — porque a chave ja gravada
    no banco nao muda sozinha. Mutacao que nao regera mede a intencao de quem
    escreveu, nao o que a maquina produz.
    """
    _multi_volta_ao_nome_de_tela(base)
    p = subprocess.run(['python3', os.path.join(base, GERADOR), '--gravar'],
                       capture_output=True, text=True, cwd=base)
    if p.returncode != 0:
        raise AssertionError('o gerador parou antes de escrever a chave nova')


def m05b_nome_de_busca_diverge_do_banco(base):
    """O MESMO defeito sem regerar, e ele e outro defeito: o marcas.json passa a
    dizer uma coisa e as chaves ja gravadas dizem outra. Duas copias do mesmo fato
    em desacordo, que e a familia de defeito que mais custou a este arquipelago —
    e quem tem de pegar e o VALIDADOR, que le a marca do arquivo em vez de confiar
    na chave. Sem esta mutacao ninguem saberia que o portao sozinho nao ve isso."""
    _multi_volta_ao_nome_de_tela(base)


def m06_marca_nova_muda(base):
    """PRODUZ O MUNDO: entra a sexta marca, sem nome_de_busca. O gerador tem de
    PARAR, em vez de compor uma chave sem marca — e sem esta mutacao a trava nunca
    rodaria, porque as cinco marcas de hoje estao completas."""
    d = _ler_json(base, MARCAS)
    d['registros'].append({
        'id': 'dreame', 'nome': 'Dreame',
        'site_oficial': 'https://br.dreametech.com/',
        'sameAs': ['https://br.dreametech.com/'],
        'verificado_em': '2026-09-13',
    })
    _gravar_json(base, MARCAS, d)


def m07_marca_nova_completa(base):
    """PRODUZ O MUNDO, e este e o caso silencioso: a sexta marca entra COMPLETA, e
    o banco fica valido. Quem tem de falhar e o PORTAO — a regua dele conhece cinco
    marcas escritas a mao, e regua que passa por cima de quem ela nao conhece
    envelhece calada. E a cicatriz de 13/09/2026 pelo avesso."""
    d = _ler_json(base, MARCAS)
    d['registros'].append({
        'id': 'dreame', 'nome': 'Dreame', 'nome_de_busca': 'Dreame',
        'site_oficial': 'https://br.dreametech.com/',
        'sameAs': ['https://br.dreametech.com/'],
        'verificado_em': '2026-09-13',
    })
    _gravar_json(base, MARCAS, d)


def m08_esquema_perde_o_termo(base):
    """PRODUZ O MUNDO PELO ESQUEMA: a entidade `peca` fica sem termo de contexto.
    Regua que le a propria lista de um arquivo de dados e cai para "nada a cobrar"
    quando a chave falta aprova TUDO em silencio."""
    d = _ler_json(base, ESQUEMA)
    del d['tipos_compostos']['afiliado']['escada_de_compra'][
        'termo_de_contexto_por_entidade']['peca']
    _gravar_json(base, ESQUEMA, d)


def m09_escada_some_do_esquema(base):
    """O bloco escada_de_compra inteiro some. O validador nao pode ficar verde por
    falta do que cobrar: sem escada nao ha base, nao ha degrau e nao ha contexto, e
    todas as travas do piso viram enfeite."""
    d = _ler_json(base, ESQUEMA)
    del d['tipos_compostos']['afiliado']['escada_de_compra']
    _gravar_json(base, ESQUEMA, d)


def m10_registro_excluido_ganha_piso(base):
    """Um registro que o portao da categoria RECUSOU ganha busca. A chave diria
    "robo aspirador" sobre um aparelho que o proprio fabricante nao chama assim —
    afirmacao falsa dentro do banco, e ela sairia da ferramenta que a ilha vende."""
    d = _ler_json(base, MODELOS)
    alvo = next(r for r in d['registros'] if r['status'] != 'publicavel')
    alvo['afiliado']['url_busca_produto'] = (
        'https://shopee.com.br/search?keyword=Multilaser%20X%20robo%20aspirador')
    _gravar_json(base, MODELOS, d)


def m11_motivo_apagado(base):
    """O item fica sem piso E sem motivo. A divida continua exatamente do mesmo
    tamanho e deixa de ter causa escrita — e divida sem causa a proxima execucao
    nao sabe se e trabalho dela ou espera de terceiro.

    ELA ESTAVA INERTE E NINGUEM VIU, descoberto em 16/09/2026. A mutacao so
    apagava o `motivo_sem_url_busca`, e isso funcionava enquanto o ALVO_MODELO
    nao tinha piso: motivo ausente com piso ausente e defeito. No dia em que os
    links de busca encurtada chegaram aos modelos, o alvo GANHOU piso, o motivo
    virou legitimamente null — e a mutacao passou a apagar um campo que ja
    estava vazio. Mutacao que nao morde e teste verde com outro nome, e o
    contrato ja nomeia esta armadilha: quando o banco melhora, a regua escrita
    sobre o mundo anterior morre calada.

    O conserto e PRODUZIR O MUNDO em vez de esperar por ele: a mutacao tira o
    piso E o motivo, que e a situacao sobre a qual a regra fala.
    """
    d = _ler_json(base, MODELOS)
    a = _registro(d, ALVO_MODELO)['afiliado']
    a['url_busca'] = ''
    a['motivo_sem_url_busca'] = None
    _refazer_contagem(d)
    _gravar_json(base, MODELOS, d)


def m12_contagem_mente(base):
    """O cabecalho diz que nao ha divida. E o defeito que a casca ja pagou uma vez,
    com o cartao dizendo zero enquanto a categoria tinha cinco produtos: numero de
    cabecalho nasce contado, nunca digitado.

    ELA FICOU INERTE EM 16/09/2026 E O CONSERTO E PRODUZIR O MUNDO. Ate aquele dia
    cinco modelos publicaveis estavam sem link curto, e escrever 0 no cabecalho era
    mentira suficiente. A Open API da 25.6 encurtou os cinco, a divida virou ZERO de
    verdade, e "mentir zero" passou a ser dizer a verdade — mutacao que nao muda
    nada mede a intencao de quem a escreveu, nao a trava. Entao ela agora TIRA o
    link curto de um registro primeiro, criando divida de uma linha, e so depois
    jura no cabecalho que ela nao existe. E a mesma licao da secao 8 que fez a
    mutacao do `intestavel` fabricar o link em vez de esperar por ele.
    """
    d = _ler_json(base, MODELOS)
    a = _registro(d, ALVO_MODELO)['afiliado']
    if not (a.get('url_busca') or '').strip():
        raise AssertionError('%s ja estava sem link curto — a mutacao seria inerte'
                             % ALVO_MODELO)
    a['url'] = ''
    a['url_busca'] = ''
    a['motivo_sem_url_busca'] = 'mundo de bancada: o link curto foi tirado'
    _refazer_contagem(d)
    if d['contagem']['itens_com_piso_nao_rastreavel'] == 0:
        raise AssertionError('a divida nao foi criada — a mentira seguinte seria verdade')
    d['contagem']['itens_com_piso_nao_rastreavel'] = 0
    _gravar_json(base, MODELOS, d)


# ------------------------------------- AS QUATRO DO MUNDO QUE O BANCO NAO TEM
def m13_ficha_sem_degrau(base):
    """PRODUZ O MUNDO: o primeiro link da ilha, sem degrau gravado. O degrau nao se
    le do link curto — s.shopee.com.br encurta a loja oficial e o anuncio de
    vendedor com a MESMA cara, e os dois apodrecem de forma oposta."""
    _dar_ficha(base, MODELOS, ALVO_MODELO, degrau=None)
    d = _ler_json(base, MODELOS)
    _refazer_contagem(d)
    _gravar_json(base, MODELOS, d)


def m14_ficha_sem_url_produto(base):
    """PRODUZ O MUNDO: link escolhido e URL crua perdida, sem motivo. E a divida
    que a Aquametria tem em 39 links e nao consegue mais pagar — sem url_produto a
    ronda nao abre a pagina, e a saude do link fica desconhecida para sempre."""
    _dar_ficha(base, MODELOS, ALVO_MODELO, url_produto=None,
               motivo_sem_url_produto=None)


def m15_degrau_3_sem_busca(base):
    """PRODUZ O MUNDO: anuncio de vendedor comum, o degrau que quebrou quatro links
    em doze horas, sem o piso embaixo. E o beco sem saida que a 25.1 proibe com
    todas as letras neste degrau especifico."""
    _dar_ficha(base, MODELOS, ALVO_MODELO, degrau=3, url_busca='',
               motivo_sem_url_busca='mundo de bancada')


def m16_mundo_do_link_intacto(base):
    """A UNICA QUE TEM DE PASSAR. O primeiro link de afiliado da ilha, inteiro e
    sem defeito: degrau 1, url crua guardada, piso encurtado, motivo ausente porque
    nao ha ausencia. Se a bateria reprovasse aqui, as travas de hoje seriam um
    falso-positivo esperando o dia em que a monetizacao comeca — e quem chegasse
    naquele dia aprenderia a ignora-las."""
    _dar_ficha(base, MODELOS, ALVO_MODELO)


# ---------------- AS DUAS DA MEDICAO DE PALAVRA-CHAVE (despacho da Sentinela 16/09)
def _medida(d, ident):
    for r in d['registros']:
        if r['id'] == ident:
            return r['escolhido']
    raise AssertionError('%s nao esta na medicao — a mutacao seria inerte' % ident)


def m21_chave_medida_em_zero(base):
    """A medicao registra ZERO resultado para a chave que esta no banco.

    E o defeito do item 1 do despacho da Sentinela de 16/09/2026 com procedencia:
    nao a busca vazia que ninguem mediu, e sim a busca vazia MEDIDA, gravada com
    data, e servida assim mesmo. Esta e a pior das duas, porque parece conferida —
    a mesma familia do numero de tela digitado da secao 8.
    """
    d = _ler_json(base, MEDICAO)
    e = _medida(d, ALVO_PECA)
    if e['resultados'] == 0:
        raise AssertionError('a chave de %s ja estava medida em zero — inerte' % ALVO_PECA)
    e['resultados'] = 0
    _gravar_json(base, MEDICAO, d)


def m22_chave_estreitada_sem_medicao(base):
    """Alguem estreita a chave no olho: o banco passa a levar o CODIGO da peca e
    perde o tipo, e a medicao continua dizendo outra coisa.

    Era exatamente o que a trava antiga proibia com a frase *"se isto mudar de
    proposito, mude tambem esta trava e escreva a medicao que sustenta a mudanca"*.
    A medicao chegou e a trava mudou — e o que nao pode e a chave mudar SEM ela.
    """
    d = _ler_json(base, PECAS)
    r = _registro(d, 'multi-pr10205')
    chave = 'Multilaser PR10205 filtro robo aspirador'
    r['afiliado']['url_busca_produto'] = (
        'https://shopee.com.br/search?keyword=' + quote(chave))
    _gravar_json(base, PECAS, d)


# ------------------- AS QUATRO DO DESPACHO DO RAPHAEL DE 14/09/2026 (itens 2 e 3)
def m17_piso_sem_degrau(base):
    """O ESTADO EM QUE A ILHA INTEIRA ESTAVA ATE HOJE, e e por isso que ele vale como
    mutacao: 65 publicaveis com a palavra-chave escrita e o degrau em `null`. Null
    quer dizer "ninguem decidiu", e a decisao estava tomada desde 13/09 — so nao
    estava gravada. Divida escrita como pendencia e divida que ninguem paga."""
    d = _ler_json(base, MODELOS)
    a = _registro(d, ALVO_MODELO)['afiliado']
    a['degrau'] = None
    a['conferido_em'] = None
    _gravar_json(base, MODELOS, d)


def m18_degrau_sem_data(base):
    """O degrau fica e a data some. Degrau e uma DECISAO, e decisao sem data nao da
    para reconferir: a proxima execucao nao sabe se ela foi tomada sobre o banco de
    hoje ou sobre um que nao existe mais."""
    d = _ler_json(base, MODELOS)
    _registro(d, ALVO_MODELO)['afiliado']['conferido_em'] = None
    _gravar_json(base, MODELOS, d)


def m19_piso_jura_degrau_1(base):
    """O item sem ficha nenhuma se declara degrau 1, o da loja oficial do fabricante.
    E a mentira mais cara da escada, porque o degrau 1 e o que a ilha usaria para
    dizer ao leitor que aquele link nao apodrece."""
    d = _ler_json(base, MODELOS)
    _registro(d, ALVO_MODELO)['afiliado']['degrau'] = 1
    _gravar_json(base, MODELOS, d)


def m20_intestavel_mente(base):
    """PRODUZ O MUNDO: o primeiro link encurtado da ilha, sem a URL crua — portanto
    intestavel pela 25.4-b — com o campo dizendo que esta tudo bem. O item 3 do
    despacho manda a impossibilidade ficar VISIVEL; um `false` ali a esconde, e a
    ronda passaria por ele todo dia sem nunca saber que nao consegue confere-lo."""
    _dar_ficha(base, MODELOS, ALVO_MODELO, url_produto=None,
               motivo_sem_url_produto='link herdado sem a URL crua, de bancada',
               intestavel=False)


# nome, o que ela ensina, funcao, portao que tem de reprovar, palavra que tem de
# aparecer na saida (None na unica que passa)
MUTACOES = [
    ('item publicavel sem palavra-chave',
     'o estado em que a ilha inteira estava ate hoje: 62 publicaveis, zero piso',
     m01_piso_apagado, 'validar', 'sem afiliado.url_busca_produto'),
    ('a busca perde o termo de contexto',
     'S20 sozinho e um celular de outra marca — a 25.3 na forma que so esta ilha tem',
     m02_busca_sem_contexto, 'validar', 'termo de contexto'),
    ('a busca fica so com a marca',
     'passaria pela trava do contexto e mandaria o leitor para a vitrine inteira',
     m03_busca_so_por_marca, 'escada', 'sem o codigo'),
    ('a peca passa a levar o codigo de fabricante',
     'decisao que nenhum portao mede vira folclore: inverter exige inverter a trava',
     m04_peca_ganha_o_codigo, 'escada', 'SKU interno'),
    ('a marca volta a ser buscada pelo nome de tela, e o banco e regerado',
     'o parentese de "Multi (ex-Multilaser)" entra na consulta — o defeito de origem',
     m05_nome_de_busca_vira_o_de_tela, 'validar', 'nome_de_busca da marca'),
    ('o nome_de_busca muda e o banco NAO e regerado',
     'duas copias do mesmo fato em desacordo: quem ve e o validador, nao o portao',
     m05b_nome_de_busca_diverge_do_banco, 'validar', 'nome_de_busca da marca'),
    ('MUNDO NOVO: sexta marca sem nome_de_busca',
     'o gerador tem de PARAR, nunca compor chave sem marca',
     m06_marca_nova_muda, 'gerador', 'sem nome_de_busca'),
    ('MUNDO NOVO: sexta marca COMPLETA, banco valido',
     'o portao tem de notar que o universo cresceu, em vez de passar por cima',
     m07_marca_nova_completa, 'escada', 'a regua conhece as marcas'),
    ('MUNDO NOVO: o esquema perde o termo de contexto da peca',
     'regua que cai para "nada a cobrar" quando a chave falta aprova tudo calada',
     m08_esquema_perde_o_termo, 'validar', 'sem termo de contexto'),
    ('a escada some do esquema',
     'sem escada nao ha base, degrau nem contexto: as travas do piso viram enfeite',
     m09_escada_some_do_esquema, 'validar', 'sem escada_de_compra'),
    ('registro recusado pelo portao da categoria ganha piso',
     'a chave diria "robo aspirador" sobre um aparelho que nao e robo',
     m10_registro_excluido_ganha_piso, 'validar', 'nao tem piso a cumprir'),
    ('o item perde o motivo de nao ter piso',
     'divida sem causa escrita a proxima execucao nao sabe se e dela ou de terceiro',
     m11_motivo_apagado, 'validar', 'motivo_sem_url_busca'),
    ('o cabecalho diz que nao ha divida',
     'numero de cabecalho nasce contado, nunca digitado',
     m12_contagem_mente, 'validar', 'itens_com_piso_nao_rastreavel'),
    ('MUNDO NOVO: primeiro link da ilha, sem degrau',
     'degrau nao se le do link curto — a mesma cara esconde durabilidades opostas',
     m13_ficha_sem_degrau, 'validar', 'degrau'),
    ('MUNDO NOVO: primeiro link da ilha, sem a URL crua',
     'sem url_produto a saude do link fica desconhecida para sempre (25.4-b)',
     m14_ficha_sem_url_produto, 'validar', 'url_produto'),
    ('MUNDO NOVO: degrau 3 sem piso embaixo',
     'o degrau que apodrece, sem a busca que a 25.1 exige justamente nele',
     m15_degrau_3_sem_busca, 'validar', 'degrau 3'),
    ('MUNDO NOVO: primeiro link da ilha, INTACTO — esta TEM de passar',
     'regua que reprova o mundo sem defeito e falso-positivo esperando a monetizacao',
     m16_mundo_do_link_intacto, None, None),
    ('a medicao registra ZERO resultado para a chave que esta no banco',
     'busca vazia medida e pior que busca vazia nao medida: ela parece conferida',
     m21_chave_medida_em_zero, 'escada', 'resultado'),
    ('a chave e estreitada no olho, sem medicao que a sustente',
     'chave estreitada fora da medicao e palpite com cara de dado',
     m22_chave_estreitada_sem_medicao, 'escada', 'sem medicao que o sustente'),
    ('o item com piso volta a ter degrau nulo — o estado de ontem',
     'degrau null quer dizer "ninguem decidiu", e a decisao estava tomada havia um dia',
     m17_piso_sem_degrau, 'validar', 'publicavel com piso e degrau'),
    ('o degrau do piso perde a data em que foi decidido',
     'decisao sem data e decisao que a proxima execucao nao sabe se ainda vale',
     m18_degrau_sem_data, 'validar', 'conferido_em'),
    ('o piso jura ser degrau 1, o da loja oficial',
     'sem ficha nenhuma a escada nao parou em lugar nenhum acima da busca',
     m19_piso_jura_degrau_1, 'validar', 'sem ficha de produto'),
    ('MUNDO NOVO: primeiro link da ilha, intestavel, e o campo diz que nao',
     'a impossibilidade de conferir da 25.4-b ficaria escondida, que e o que o item 3 proibe',
     m20_intestavel_mente, 'validar', 'intestavel'),

    # AS MESMAS TRES MUTACOES, CONTRA O OUTRO PORTAO — e isto nao e repeticao.
    # teste-escada-compra.py escreve a propria regua e nao le o esquema; o validador
    # le. Duas travas que lessem a mesma fonte morreriam juntas no dia em que
    # alguem editasse o esquema, e o portao ficaria verde sobre a decisao revogada
    # em silencio. Provar que cada uma morde sozinha e o unico jeito de saber que
    # sao duas testemunhas, e nao uma com eco.
    ('o item com piso volta a ter degrau nulo — contra o portao da escada',
     'a segunda testemunha da 25.1 tem de morder sozinha, sem o validador',
     m17_piso_sem_degrau, 'escada', 'degrau'),
    ('o degrau do piso perde a data — contra o portao da escada',
     'a segunda testemunha tambem cobra a data da decisao',
     m18_degrau_sem_data, 'escada', 'conferido_em'),
    ('MUNDO NOVO: intestavel mente — contra o portao da escada',
     'a segunda testemunha refaz a derivacao a mao, em vez de crer no campo',
     m20_intestavel_mente, 'escada', 'intestavel'),
]

COMANDO = {
    'validar': ['python3', VALIDADOR],
    'escada': ['python3', PORTAO],
    'gerador': ['python3', GERADOR, '--gravar'],
}


def _rodar(base, chave):
    cmd = list(COMANDO[chave])
    cmd[1] = os.path.join(base, cmd[1])
    p = subprocess.run(cmd, capture_output=True, text=True, cwd=base)
    return p.returncode != 0 or 'ERRO ' in p.stdout, p.stdout + p.stderr


def main():
    corretas = 0
    erradas = []
    print('Mutacoes deliberadas na escada de compra (secao 25) — todas reprovam, '
          'menos a ultima\n')

    for nome, porque, aplicar, portao, palavra in MUTACOES:
        with tempfile.TemporaryDirectory() as tmp:
            base = os.path.join(tmp, 'ilha')
            shutil.copytree(RAIZ, base)
            try:
                aplicar(base)
            except (AssertionError, StopIteration, KeyError) as err:
                print('  ERRO   %-58s mutacao INERTE: %s' % (nome, err))
                erradas.append(nome)
                continue

            if portao is None:
                # A que tem de passar: os TRES portoes ficam verdes no mundo novo.
                ruins = [c for c in ('validar', 'escada', 'gerador')
                         if _rodar(base, c)[0]]
                if ruins:
                    print('  ERRADA %-58s reprovou em %s, e devia passar'
                          % (nome, ', '.join(ruins)))
                    erradas.append(nome)
                else:
                    print('  ok     %-58s passou, como tinha de passar' % nome)
                    corretas += 1
                continue

            reprovou, saida = _rodar(base, portao)
            if not reprovou:
                print('  ERRADA %-58s %s ficou VERDE' % (nome, portao))
                erradas.append(nome)
            elif palavra not in saida:
                # Reprovou pelo motivo errado. A regra vizinha pegando o defeito
                # prova que ALGUMA trava existe, nao que ESTA existe.
                print('  ERRADA %-58s %s reprovou sem citar %r'
                      % (nome, portao, palavra))
                erradas.append(nome)
            else:
                print('  ok     %-58s %s reprovou, citando a regra' % (nome, portao))
                corretas += 1

    print('\n%d de %d como esperado.' % (corretas, len(MUTACOES)))
    if erradas:
        print('FALHOU em: %s' % ', '.join(erradas))
        return 1
    print('Nenhuma mutacao inerte: toda trava foi vista reprovando pela regra que nomeia.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
