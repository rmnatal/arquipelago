#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escreve `dados/vitrine-de-produto.json`, que e o que a TELA das paginas da 30 serve.

    python3 ferramentas/gerar-vitrine-de-produto.py            # mostra o que mudaria
    python3 ferramentas/gerar-vitrine-de-produto.py --gravar
    python3 ferramentas/gerar-vitrine-de-produto.py --conferir  # SEM REDE

AS DUAS METADES, E POR QUE ELAS MORAM EM ARQUIVOS SEPARADOS
-----------------------------------------------------------
`dados/paginas-de-produto.json` e DECLARADO e escrito a mao: titulo,
`description`, a resposta em duas frases, o "qual escolher" e as perguntas. E a
voz do `VOZ.md`, e nela NENHUM numero e digitado — a prosa traz moldes
(`{DE}`, `{ATE}`, `{MEDIANA}`, `{N}`, `{DECLARAM_WATT}`, `{DIZEM_QUAL_WATT}`,
`{DATA}`) e quem os preenche e o PHP, com o numero que sai deste arquivo.

`dados/vitrine-de-produto.json` e GERADO daqui: o cartao de compra, a tabela e
os numeros, RECONTADOS de `dados/anuncios-por-consulta.json`. Preco escrito a
mao na frase e preco que mente na coleta seguinte, calado.

A ORDEM DA VITRINE, E ELA E A DA SECAO 7
----------------------------------------
A secao 7 manda: (1) elegibilidade tecnica completa; (2) adequacao tecnica entre
os elegiveis; (3) e so como DESEMPATE entre itens equivalentes, quem tem link de
loja aparece antes. Nesta pagina NAO existe criterio tecnico que separe os
anuncios: o dado tecnico de anuncio e nivel 6 e o esquema desta ilha exige nivel
5 ou melhor em watt, velocidade, acelerador e carga maxima — nenhum deles entra.
Logo os anuncios sao, para a regra, EQUIVALENTES, e o passo 3 e o unico que
vale. A ordem e por `vendas` (medidas na propria API, com data) e depois por
preco crescente, e a pagina DIZ isso no "como sabemos" em vez de ordenar em
silencio.

`vendas` ordena e NAO vai para a tela. A secao 7 proibe "selo de mais vendido" e
"avaliacao que a ilha nao mediu"; esta ilha mediu as vendas, mas publicar a
contagem ao lado do produto e prova social, e prova social nao e o que esta
pagina vende. O que vai para a tela e o que o anuncio DECLARA e o que ele NAO
declara.

O CARROSSEL LEVA DE 3 A 5, A TABELA LEVA TODOS
----------------------------------------------
A 32.1 (item 5) pede "carrossel horizontal de 3 a 5 cartoes" e a 30.3 pede
"tabela comparando os produtos". Sao duas coisas: o carrossel e a primeira tela
e tem teto, a tabela e a prestacao de contas e nao tem. A 32.5-b mede o primeiro
botao de compra antes de 1.400 px, e carrossel de dezesseis cartoes nao muda esse
numero (ele rola na horizontal) — mas a secao 7 manda nomear TODO item uma vez
em cada resposta, e e a tabela que faz isso.
"""
import argparse
import json
import os
import re as _re
import statistics
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANUNCIOS = os.path.join(RAIZ, 'dados', 'anuncios-por-consulta.json')
EDITORIAL = os.path.join(RAIZ, 'dados', 'paginas-de-produto.json')
VITRINE = os.path.join(RAIZ, 'dados', 'vitrine-de-produto.json')

PISO_DA_30_2 = 3
TETO_DO_CARROSSEL = 5


def _textos(valor):
    """Toda string dentro de um valor da camada declarada, em qualquer profundidade.

    Ela e recursiva de proposito: a primeira versao olhava so string e lista de
    string, e as perguntas frequentes sao uma lista de DICIONARIOS — a trava
    passaria por cima de toda pergunta e resposta sem dizer que nao as leu, que
    e a cara do portao que aprova em silencio o que nao mediu (32.5-b).
    """
    if isinstance(valor, str):
        yield valor
    elif isinstance(valor, dict):
        for v in valor.values():
            for t in _textos(v):
                yield t
    elif isinstance(valor, (list, tuple)):
        for v in valor:
            for t in _textos(v):
                yield t


def ler(caminho):
    with open(caminho, encoding='utf-8') as f:
        return json.load(f)


def real(valor):
    """R$ 1.297,13 — o separador do Brasil, feito aqui e nunca no PHP."""
    inteiro, centavos = ('%.2f' % float(valor)).split('.')
    partes = []
    while len(inteiro) > 3:
        partes.insert(0, inteiro[-3:])
        inteiro = inteiro[:-3]
    partes.insert(0, inteiro)

    return 'R$ ' + '.'.join(partes) + ',' + centavos


def data_br(iso):
    a, m, d = (iso or '').split('-')

    return '%s/%s/%s' % (d, m, a)


def o_que_o_anuncio_declara(a):
    """A frase da coluna "o que o anuncio diz", e ela nunca afirma dado tecnico.

    O watt do titulo NAO e atribuido a `potencia_nominal_w` de ninguem: o que a
    pagina diz e que o anuncio declara aquele numero e se ele diz QUAL watt e.
    E a tese do `VOZ.md` em forma de coluna.
    """
    rotulo = a['rotulo_de_potencia']
    if rotulo == 'sem_watt':
        return 'o anúncio não declara potência'
    if rotulo == 'watt_sem_rotulo':
        return 'declara watt, sem dizer se é nominal ou de pico'
    if rotulo == 'pico':
        return 'declara o watt de pico — o nominal, que é o que vale para a regra, não aparece'
    if rotulo == 'nominal':
        return 'declara a potência nominal'

    return 'declara os dois watts, nominal e de pico'


# ---------------------------------------------------------------------------
# A FRASE DO ROTULO DE POTENCIA — contada, nunca digitada
#
# Esta funcao existe por uma cicatriz desta ilha, de HOJE: o `REGISTRO.md` de
# 29/10/2026 as 16h2xZ escreve que a frase de abertura do bloco de compra da F2
# era digitada, dizia "Nenhum destes entrou pela conta de Wh", e teria virado
# mentira calada no dia em que o banco mudasse. A licao esta la com estas
# palavras: **prosa que afirma o estado do banco e numero digitado em outro
# traje.**
#
# A camada declarada NAO pode escrever esta frase, porque ela muda de FORMA e
# nao so de numero: com zero watt declarado, com todos declarados, e com nenhum
# rotulado, as tres pedem frases diferentes, e um molde `{DIZEM_QUAL_WATT}` solto
# produz "sem dizer, em 0 deles, se e o nominal" — portugues que so aparece no
# dia em que a contagem chega em zero.
#
# As cinco formas sao conferidas sobre MUNDOS FABRICADOS em `--conferir`, porque
# o banco de hoje produz uma delas so e regua que nunca viu o mundo dela nasce
# errada sem poder falhar (secao 8).
def frase_do_rotulo(n, declaram_watt, dizem_qual_watt):
    if declaram_watt == 0:
        return ('Nenhum dos %d anúncios declara potência, e é a potência nominal que '
                'decide se precisa de habilitação.' % n)
    if dizem_qual_watt == 0 and declaram_watt == n:
        return ('Todos os %d declaram um watt, e nenhum diz se aquele número é o nominal '
                'ou o de pico — e é o nominal que decide a categoria.' % n)
    if dizem_qual_watt == 0:
        return ('%d dos %d declaram um watt, e nenhum diz se aquele número é o nominal ou '
                'o de pico — e é o nominal que decide a categoria.' % (declaram_watt, n))
    if dizem_qual_watt == declaram_watt:
        return ('Os %d que declaram watt dizem todos qual watt é aquele, o que nesta '
                'família é raro.' % declaram_watt)

    return ('%d dos %d declaram um watt e só %d dizem qual watt é aquele — e é o nominal '
            'que decide a categoria.' % (declaram_watt, n, dizem_qual_watt))


MUNDOS_DO_ROTULO = (
    # (n, declaram, dizem_qual, pedaco que a frase tem de conter)
    (5, 0, 0, 'Nenhum dos 5'),
    (5, 5, 0, 'Todos os 5'),
    (5, 1, 0, '1 dos 5'),
    (5, 3, 3, 'Os 3 que declaram'),
    (16, 15, 1, 'só 1 dizem'),
)


def ordenar(servem):
    """Secao 7, passo 3: desempate entre equivalentes. Ver o cabecalho."""
    return sorted(servem, key=lambda a: (-(a.get('vendas') or 0), a.get('preco') or 0))


def montar(bloco, editorial_da_pagina):
    servem = ordenar([a for a in bloco['anuncios']
                      if a['serve'] and a.get('url_afiliado') and a.get('preco') is not None])
    if len(servem) < PISO_DA_30_2:
        return None, ('menos de %d anuncios que servem COM link e preco: %d'
                      % (PISO_DA_30_2, len(servem)))

    precos = sorted(a['preco'] for a in servem)
    rotulos = {}
    for a in servem:
        rotulos[a['rotulo_de_potencia']] = rotulos.get(a['rotulo_de_potencia'], 0) + 1
    declaram_watt = sum(v for k, v in rotulos.items() if k != 'sem_watt')
    dizem_qual = sum(v for k, v in rotulos.items() if k in ('nominal', 'pico', 'os_dois'))

    cartoes, linhas = [], []
    for i, a in enumerate(servem):
        item = {
            'nome': a['titulo'],
            'preco': real(a['preco']),
            'preco_numero': a['preco'],
            'preco_nota': '(preço de %s)' % data_br(a['coletado_em']),
            'especificacao': o_que_o_anuncio_declara(a),
            'url': a['url_afiliado'],
            'programa': 'shopee',
            'degrau': a['degrau_da_escada'],
            'imagem': a.get('imagem'),
            'loja': a['loja'],
        }
        linhas.append(item)
        if i < TETO_DO_CARROSSEL:
            cartoes.append(item)

    # AS RECUSAS VAO PARA A TELA, porque a secao 7 manda a pagina dizer o que
    # deve ao leitor sobre quem NAO entrou — e aqui o que nao entrou e, na
    # maioria, acessorio e brinquedo que a loja devolve na mesma busca.
    recusas = {}
    for a in bloco['anuncios']:
        if not a['serve']:
            recusas[a['recusado_por']] = recusas.get(a['recusado_por'], 0) + 1

    return {
        'id': bloco['id'],
        'consulta': bloco['consulta'],
        'slug': bloco['slug'],
        'chave_da_loja': bloco['chave_escolhida'],
        'degrau_da_escada': bloco['degrau_escolhido'],
        'colhido_em': bloco['colhido_em'],
        'colhido_em_br': data_br(bloco['colhido_em']),
        'numeros': {
            'n': len(servem),
            'de': real(precos[0]),
            'ate': real(precos[-1]),
            'mediana': real(statistics.median(precos)),
            'de_numero': precos[0],
            'ate_numero': precos[-1],
            'declaram_watt': declaram_watt,
            'dizem_qual_watt': dizem_qual,
            'sem_watt': rotulos.get('sem_watt', 0),
            'frase_do_rotulo': frase_do_rotulo(len(servem), declaram_watt, dizem_qual),
            'lidas': bloco['resumo']['ofertas_lidas'],
            'recusadas': bloco['resumo']['ofertas_recusadas'],
            'recusas_por_causa': recusas,
        },
        'cartoes': cartoes,
        'linhas': linhas,
        'ordem': 'vendas medidas na API (decrescente), depois preço crescente — '
                 'o desempate entre equivalentes da seção 7',
    }, None


def gerar():
    anuncios = ler(ANUNCIOS)
    editorial = ler(EDITORIAL)
    decl = {p['id']: p for p in editorial['paginas']}

    paginas, recusadas = [], []
    for bloco in anuncios['consultas']:
        if not bloco.get('publicar_declarado'):
            recusadas.append({'id': bloco['id'],
                              'causa': 'nao declarada para publicar em consultas-de-produto.json'})
            continue
        if bloco['id'] not in decl:
            recusadas.append({'id': bloco['id'],
                              'causa': 'colhida e sem camada editorial em paginas-de-produto.json'})
            continue
        v, causa = montar(bloco, decl[bloco['id']])
        if v is None:
            recusadas.append({'id': bloco['id'], 'causa': causa})
            continue
        paginas.append(v)

    return {
        'id': 'vitrine-de-produto',
        'ilha': 'rodametria',
        'bloco': '5b',
        'gerado_em': anuncios['gerado_em'],
        'gerado_por': 'ferramentas/gerar-vitrine-de-produto.py',
        'o_que_este_arquivo_e': (
            'O que a TELA das paginas da secao 30 serve: cartoes do carrossel, linhas da '
            'tabela e os numeros, todos RECONTADOS de dados/anuncios-por-consulta.json. '
            'Nenhum numero desta ilha e digitado em prosa: a camada declarada traz moldes e '
            'quem os preenche e o PHP com o numero daqui.'),
        'vendas_ordenam_e_nao_vao_para_a_tela': (
            'A ordem e o desempate entre equivalentes da secao 7, e `vendas` e o unico '
            'desempate honesto porque comissao nunca ordena. Mas a contagem de vendas NAO '
            'e publicada: a secao 7 proibe selo de mais vendido, e prova social nao e o que '
            'esta pagina vende.'),
        'piso_da_30_2': PISO_DA_30_2,
        'teto_do_carrossel': TETO_DO_CARROSSEL,
        'paginas': paginas,
        'nao_nasceram': recusadas,
    }


def conferir():
    if not os.path.exists(VITRINE):
        print('REPROVADO: %s nao existe' % os.path.basename(VITRINE))
        return 1
    gravado = ler(VITRINE)
    calculado = gerar()

    falhas, afirmacoes = [], 0

    afirmacoes += 1
    if [p['id'] for p in gravado['paginas']] != [p['id'] for p in calculado['paginas']]:
        falhas.append('a lista de paginas gravada discorda da calculada')
    afirmacoes += 1
    if gravado.get('nao_nasceram') != calculado.get('nao_nasceram'):
        falhas.append('a lista de `nao_nasceram` gravada discorda da calculada')

    for g, c in zip(gravado['paginas'], calculado['paginas']):
        for campo in ('numeros', 'cartoes', 'linhas', 'chave_da_loja', 'degrau_da_escada',
                      'colhido_em', 'colhido_em_br', 'consulta', 'slug', 'ordem'):
            afirmacoes += 1
            if g.get(campo) != c.get(campo):
                falhas.append('%s: campo %r gravado nao refaz' % (g['id'], campo))
        afirmacoes += 1
        if len(g['cartoes']) > calculado['teto_do_carrossel']:
            falhas.append('%s: carrossel com %d cartoes, teto %d'
                          % (g['id'], len(g['cartoes']), calculado['teto_do_carrossel']))
        afirmacoes += 1
        if len(g['linhas']) < calculado['piso_da_30_2']:
            falhas.append('%s: tabela com %d linhas, piso da 30.2 e %d'
                          % (g['id'], len(g['linhas']), calculado['piso_da_30_2']))
        # Link de compra sem `url` nao e saida de compra, e a secao 7 proibe
        # bloco de compra com item sem saida.
        for item in g['linhas']:
            afirmacoes += 1
            if not (item.get('url') or '').startswith('https://'):
                falhas.append('%s: linha sem url de afiliado' % g['id'])
            afirmacoes += 1
            if 'preço de' not in (item.get('preco_nota') or ''):
                falhas.append('%s: preco sem a data da coleta ao lado (secao 7)' % g['id'])

    # OS CINCO MUNDOS DA FRASE DO ROTULO, e quatro deles o banco de hoje nao
    # produz. Trava que nunca viu o mundo dela nasce errada sem poder falhar.
    for n, decl_w, dizem, pedaco in MUNDOS_DO_ROTULO:
        afirmacoes += 1
        frase = frase_do_rotulo(n, decl_w, dizem)
        if pedaco not in frase:
            falhas.append('frase_do_rotulo(%d,%d,%d) nao traz %r: %r'
                          % (n, decl_w, dizem, pedaco, frase))
        afirmacoes += 1
        if ', 0 ' in frase or frase.endswith(' 0.'):
            falhas.append('frase_do_rotulo(%d,%d,%d) imprime zero no meio da frase: %r'
                          % (n, decl_w, dizem, frase))

    # A CAMADA DECLARADA NAO PODE TRAZER NUMERO DIGITADO. Esta e a trava que a
    # cicatriz do `REGISTRO.md` desta ilha de 29/10 (16h2xZ) deixou escrita:
    # "prosa que afirma o estado do banco e numero digitado em outro traje".
    editorial = ler(EDITORIAL)
    permitidos = tuple(n['texto'] for n in editorial.get('numeros_declarados_permitidos', []))
    # QUALQUER DIGITO, e nao "grupo de dois ou mais": a primeira versao desta
    # trava cobrava `\d{2,}` e a mutacao `Sao 2 familias com pagina hoje` na
    # prosa da mae SOBREVIVEU — justamente a contagem de um digito, que e a
    # contagem que esta ilha tem. Numero pequeno digitado e o que envelhece
    # primeiro: a prosa que diz `2 familias` mente no dia em que a terceira
    # nascer, e nada acusa.
    #
    # O que escapa e so o que esta NOMEADO em `numeros_declarados_permitidos`,
    # com o motivo ao lado — o numero da Resolucao Contran e nome proprio de
    # documento, nao numero de tela. Numero que a prosa precisa dizer e nao e
    # contagem (oito quilometros, cem quilos) se escreve por extenso.
    proibido = _re.compile(r'\d')
    for pag in editorial['paginas'] + [editorial['mae']]:
        for campo, valor in sorted(pag.items()):
            for texto in _textos(valor):
                limpo = texto
                for ok in permitidos:
                    limpo = limpo.replace(ok, '')
                afirmacoes += 1
                achado = proibido.search(limpo)
                if achado:
                    falhas.append('%s: a camada declarada traz numero digitado em %r (%r): %r'
                                  % (pag.get('id', pag.get('slug')), campo,
                                     achado.group(0), texto[:70]))

    for f in falhas:
        print('FALHA: ' + f)
    print('\n%d afirmacao(oes), %d falha(s).' % (afirmacoes, len(falhas)))
    print('APROVADO' if not falhas else 'REPROVADO')

    return 1 if falhas else 0


def main():
    p = argparse.ArgumentParser(description=__doc__)
    g = p.add_mutually_exclusive_group()
    g.add_argument('--gravar', action='store_true')
    g.add_argument('--conferir', action='store_true')
    a = p.parse_args()

    if a.conferir:
        return conferir()

    saida = gerar()
    for pg in saida['paginas']:
        n = pg['numeros']
        print('%s: %d anuncios · %s a %s (mediana %s) · declaram watt %d, dizem qual %d'
              % (pg['id'], n['n'], n['de'], n['ate'], n['mediana'],
                 n['declaram_watt'], n['dizem_qual_watt']))
        print('   carrossel %d cartao(oes) · recusadas %d %s'
              % (len(pg['cartoes']), n['recusadas'], n['recusas_por_causa']))
    for r in saida['nao_nasceram']:
        print('NAO NASCEU %s: %s' % (r['id'], r['causa']))

    if not a.gravar:
        print('\nsem --gravar: nada foi escrito.')
        return 0

    with open(VITRINE, 'w', encoding='utf-8') as f:
        json.dump(saida, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('\ngravado: %s' % os.path.basename(VITRINE))

    return 0


if __name__ == '__main__':
    sys.exit(main())
