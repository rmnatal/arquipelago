#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PORTAO DA SEGUNDA COPIA DO CRITERIO DE ORDEM — ITEM 4 DO DESPACHO DE 11/11/2026.
Sem rede.

    python3 ferramentas/teste-criterio-de-ordem.py

O DEFEITO, medido no ar as 14h3xZ de 11/11/2026 pela ronda, e ele era MAIOR do
que o despacho viu. A ronda achou DUAS paginas declarando o mesmo fato — o
criterio que ordena a vitrine — com DUAS reguas diferentes:

    /sobre/                     "quem ordena uma lista aqui e o que o anuncio
                                 declara e o preco, nunca a comissao"
    /divulgacao-de-afiliados/   "Primeiro vem quem a loja mostra como mais
                                 vendido na busca medida, e o desempate e o preco"

A varredura que este portao fez nascer achou mais DUAS, as duas em snippet, as
duas servidas:

    rodametria-casca.php        "Isso nunca muda a ordem das recomendacoes —
                                 quem decide a ordem e o que o FABRICANTE
                                 declara."   <- em TODA pagina da ilha
    rodametria-produto.php      "A ordem e por VENDA MEDIDA e depois por preco."
                                             <- nas paginas de produto

QUATRO declaracoes, QUATRO redacoes, e a ordem real e UMA: vendas que a propria
loja declarou na busca medida (decrescente), e no empate o preco menor. A do
fabricante era simplesmente FALSA. A de "venda medida" dizia que a VENDA foi
medida por nos, e nao foi — foi LIDA da resposta da loja, que e a diferenca que
o `VOZ.md` desta ilha proibe apagar.

A 20.7 ja mediu o que isso da: "duas declaracoes do mesmo fato comecam iguais e
so uma sobe". Aqui foram quatro, e tres estavam velhas ou erradas.

O CONSERTO, E ELE E O DA 32.4-c: "o conserto de uma frase duplicada nao e
consertar as duas: e a segunda deixar de existir". A ordem e declarada UMA vez,
como DADO, na tupla `CHAVES_DE_ORDEM` de
`ferramentas/gerar-vitrine-de-produto.py`; `ordenar()` monta a chave de
ordenacao dela e `frase_do_criterio_de_ordem()` monta a frase de leitor da MESMA
tupla. A frase viaja em `criterio_de_ordem_na_tela` e as tres camadas de tela a
recebem pelo molde `{CRITERIO_DE_ORDEM}`.

O QUE ESTE PORTAO COBRA, e as tres coisas sao diferentes:

1. **A frase nao esta escrita a mao em lugar nenhum.** Se o literal dela
   aparecer numa camada declarada ou num snippet, ela virou copia — e copia
   escrita a mao nao sobe com a ordem.
2. **Quem AFIRMA o criterio usa o molde.** Prosa que declara a ordem sem o molde
   e a segunda copia nascendo. A regua e de VOCABULARIO e nao julga prosa
   (20.5): ela denuncia a ocorrencia e diz o conserto, que e trocar a frase pelo
   molde.
3. **A remissao continua permitida.** O rodape da casca NAO declara o criterio:
   ele diz onde o criterio esta escrito, com link. Dizer onde nao e declarar, e
   portao que reprovasse a remissao reprovaria a pagina certa — o caminho mais
   curto para alguem passar a ignorar o portao (20.5). Por isso o mundo 6 do
   autoteste e a frase do rodape, e ela tem de PASSAR.
"""

import importlib.util
import json
import os
import re
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AQUI = os.path.join(RAIZ, 'ferramentas')
GERADOR = os.path.join(AQUI, 'gerar-vitrine-de-produto.py')
VITRINE = os.path.join(RAIZ, 'dados', 'vitrine-de-produto.json')

MOLDE = '{CRITERIO_DE_ORDEM}'

# As camadas que servem prosa ao leitor: os bancos DECLARADOS e os snippets.
CAMADAS_DECLARADAS = ('paginas-institucionais.json', 'paginas-de-produto.json')
SNIPPETS = ('rodametria-casca.php', 'rodametria-produto.php', 'rodametria-f1.php',
            'rodametria-f2.php', 'rodametria-f3.php', 'rodametria-institucional.php')

# O VOCABULARIO DE QUEM AFIRMA O CRITERIO. Cada padrao e uma forma medida ou
# obvia de DECLARAR a ordem; nenhum deles e uma forma de REMETER a ela.
#
# SAO EXPRESSOES REGULARES DESDE 13/11/2026, e a troca tem causa medida: ate
# aqui eram cadeias cruas, e `a ordem e por` NAO alcanca
# `A ordem DOS CARTOES e por venda medida` — que era exatamente a QUARTA copia,
# viva em `dados/paginas-de-produto.json` e servida nas duas paginas de produto
# desde 11/11. A regra 3 ja varria aquele arquivo; o que faltava era o
# vocabulario morder o sujeito no meio. Padrao que so casa a forma EXATA mede a
# frase de ontem, nao o defeito.
PADROES_DE_AFIRMACAO = (
    r'quem ordena',
    r'quem decide a ordem',
    r'ordena uma lista',
    r'primeiro vem',
    # `a ordem <qualquer sujeito curto> e por ...` — a forma generica da QUARTA
    # copia. O `[^.]` para na frase: sujeito nao atravessa ponto final.
    r'a ordem\b[^.]{0,40}\be por\b',
    r'a ordem da lista e',
    r'ordenamos',
    r'o desempate e\b',
    r'em ordem de preco',
    r'a ordem e o',
    # A FALSIDADE NOMEADA, e ela entra por si: `venda medida` diz que a VENDA foi
    # medida por nos, e nao foi — foi LIDA da resposta da loja. Quem escrever a
    # cadeia fora de comentario esta reabrindo o defeito de 11/11.
    r'\bvenda medida\b',
)


def sem_acento(t):
    t = unicodedata.normalize('NFD', str(t or '').lower())
    return ''.join(c for c in t if unicodedata.category(c) != 'Mn')


def gerador():
    spec = importlib.util.spec_from_file_location('gerador_da_vitrine', GERADOR)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def sem_comentario_php(fonte):
    """O PHP sem os comentarios, para a regua ler o que vai para a TELA.

    Comentario e a memoria da ilha (secao 3) e nele a palavra e livre — inclusive
    `quem decide a ordem`, que aparece nos comentarios deste proprio conserto
    explicando o defeito que ele desfez. Medir o arquivo inteiro confundiria a
    explicacao com a afirmacao, que e o erro que a regua de CSS desta ilha ja
    cometeu uma vez.
    """
    sem = re.sub(r'/\*.*?\*/', ' ', fonte, flags=re.S)
    # `//` so e comentario quando nao e parte de `https://`; a guarda e o
    # caractere anterior, do mesmo jeito que o portao do roteiro faz.
    return re.sub(r'(?<![:\'"])//[^\n]*', ' ', sem)


def afirmacoes_sem_molde(textos):
    """[(onde, padrao, texto)] de quem AFIRMA o criterio sem usar o molde."""
    achados = []
    for onde, texto in textos:
        if MOLDE in (texto or ''):
            continue
        t = sem_acento(texto)
        for padrao in PADROES_DE_AFIRMACAO:
            if re.search(padrao, t):
                achados.append((onde, padrao, texto))
                break
    return achados


def prosa_declarada(caminho):
    """[(onde, texto)] de toda cadeia de um banco declarado."""
    with open(caminho, encoding='utf-8') as f:
        d = json.load(f)
    saida = []

    def andar(o, onde):
        if isinstance(o, dict):
            for k, v in o.items():
                andar(v, '%s/%s' % (onde, k))
        elif isinstance(o, list):
            for i, v in enumerate(o):
                andar(v, '%s/%d' % (onde, i))
        elif isinstance(o, str):
            saida.append((onde, o))

    andar(d, os.path.basename(caminho))
    return saida


def main():
    mod = gerador()
    frase = mod.frase_do_criterio_de_ordem()
    falhas, afirmacoes, notas = [], 0, []

    def diz(ok, msg):
        nonlocal afirmacoes
        afirmacoes += 1
        if not ok:
            falhas.append(msg)

    # ------------------------------------------------------------------
    # 1. A FRASE NASCE DA TUPLA QUE ORDENA, e as duas nao podem divergir
    # ------------------------------------------------------------------
    diz(len(mod.CHAVES_DE_ORDEM) >= 2,
        'CHAVES_DE_ORDEM tem menos de duas chaves: sem desempate declarado a frase '
        'promete um criterio que a ordenacao nao tem')
    for c in mod.CHAVES_DE_ORDEM:
        diz(bool(c.get('na_tela')),
            'a chave de ordem %r nao tem frase de leitor (`na_tela`): ela ordenaria em '
            'silencio, e a pagina declara o criterio' % c.get('campo'))
        diz(c.get('sentido') in ('asc', 'desc'),
            'a chave de ordem %r tem sentido %r, que `ordenar()` nao sabe aplicar'
            % (c.get('campo'), c.get('sentido')))
        diz(sem_acento(c['na_tela']) in sem_acento(frase),
            'a frase do criterio nao cita a chave %r: a ordem tem um degrau que a '
            'pagina nao conta' % c.get('campo'))
    notas.append('a frase servida: %r' % frase)

    # A CHAVE QUE ORDENA DE VERDADE E A DECLARADA — provado em dado fabricado, e
    # nao por leitura do codigo: dois anuncios em que `vendas` e `preco` apontam
    # para lados OPOSTOS. Se alguem trocar a chave de `ordenar()` sem mexer na
    # tupla, este mundo reprova.
    a = {'vendas': 10, 'preco': 999.0, 'titulo': 'o mais vendido e mais caro'}
    b = {'vendas': 1, 'preco': 1.0, 'titulo': 'o mais barato e menos vendido'}
    diz(mod.ordenar([b, a])[0] is a,
        'a ordem real NAO segue CHAVES_DE_ORDEM: com vendas e preco em lados opostos, '
        'quem veio primeiro nao foi o de mais vendas — e a pagina declara que foi')
    diz(mod.ordenar([{'vendas': 5, 'preco': 20.0}, {'vendas': 5, 'preco': 10.0}])[0]['preco'] == 10.0,
        'o desempate de preco nao esta engatado: com vendas iguais, o mais caro veio '
        'primeiro')

    # ------------------------------------------------------------------
    # 2. A FRASE NAO ESTA ESCRITA A MAO EM LUGAR NENHUM
    # ------------------------------------------------------------------
    pedaco = sem_acento(mod.CHAVES_DE_ORDEM[0]['na_tela'])
    for nome in CAMADAS_DECLARADAS:
        caminho = os.path.join(RAIZ, 'dados', nome)
        if not os.path.exists(caminho):
            continue
        cru = sem_acento(open(caminho, encoding='utf-8').read())
        diz(pedaco not in cru,
            '%s traz o literal da frase do criterio: ela e GERADA e chega pelo molde %s. '
            'Copia escrita a mao nao sobe quando a ordem muda (20.7)' % (nome, MOLDE))
    for nome in SNIPPETS:
        caminho = os.path.join(RAIZ, 'snippets', nome)
        if not os.path.exists(caminho):
            continue
        servido = sem_acento(sem_comentario_php(open(caminho, encoding='utf-8').read()))
        diz(pedaco not in servido,
            '%s traz o literal da frase do criterio fora de comentario: ela e GERADA e '
            'chega pelo molde %s' % (nome, MOLDE))

    # ------------------------------------------------------------------
    # 3. QUEM AFIRMA O CRITERIO USA O MOLDE
    # ------------------------------------------------------------------
    for nome in CAMADAS_DECLARADAS:
        caminho = os.path.join(RAIZ, 'dados', nome)
        if not os.path.exists(caminho):
            continue
        for onde, padrao, texto in afirmacoes_sem_molde(prosa_declarada(caminho)):
            diz(False,
                '%s: %r declara o criterio de ordem sem o molde %s — e a segunda copia '
                'nascendo. Troque a frase pelo molde: %r'
                % (nome, padrao, MOLDE, texto[:120]))
    for nome in SNIPPETS:
        caminho = os.path.join(RAIZ, 'snippets', nome)
        if not os.path.exists(caminho):
            continue
        servido = sem_comentario_php(open(caminho, encoding='utf-8').read())
        # LINHA POR LINHA, e nao o arquivo inteiro de uma vez: a prosa do PHP e
        # concatenada em varias linhas, e um arquivo que use o molde em UM lugar
        # ficaria isento no resto dele. O primeiro rascunho desta regua media o
        # arquivo inteiro e por isso o `rodametria-produto.php` — que usa o molde
        # no bloco de compra — teria passado com qualquer segunda copia dentro.
        # A frase do PHP tambem quebra em duas linhas, entao cada linha vai
        # JUNTO COM A SEGUINTE: o molde pode estar na linha de baixo.
        linhas = servido.splitlines()
        pares = [('%s:%d' % (nome, i + 1), l + ' ' + (linhas[i + 1] if i + 1 < len(linhas) else ''))
                 for i, l in enumerate(linhas)]
        for onde, padrao, texto in afirmacoes_sem_molde(pares):
            diz(False,
                '%s declara o criterio de ordem fora de comentario e sem o molde %s '
                '(%r) — %r' % (onde, MOLDE, padrao, texto.strip()[:120]))

    # ------------------------------------------------------------------
    # 4. O DADO GERADO CARREGA A FRASE, que e o que o PHP le
    # ------------------------------------------------------------------
    if os.path.exists(VITRINE):
        with open(VITRINE, encoding='utf-8') as f:
            v = json.load(f)
        diz(v.get('criterio_de_ordem_na_tela') == frase,
            '`criterio_de_ordem_na_tela` gravado %r nao e a frase de agora %r — rode o '
            'gerador' % (v.get('criterio_de_ordem_na_tela'), frase))
    else:
        diz(False, 'dados/vitrine-de-produto.json nao existe: o molde nao teria o que servir')

    # ------------------------------------------------------------------
    # 5. OS MUNDOS FABRICADOS — a regua tem de MORDER e de NAO morder
    # ------------------------------------------------------------------
    mundos = [
        ('o mundo real passa',
         lambda: not afirmacoes_sem_molde([('real', 'A ordem da lista. %s Comparar a taxa '
                                            'de uma loja com a de outra seria trocar a sua '
                                            'compra pela nossa receita.' % MOLDE)])),
        ('a frase do /sobre/ que estava no ar e ACHADA',
         lambda: bool(afirmacoes_sem_molde(
             [('sobre', 'Nao publica "melhor patinete" nem "top dez": quem ordena uma lista '
                        'aqui e o que o anuncio declara e o preco, nunca a comissao.')]))),
        ('a frase do /divulgacao/ que estava no ar e ACHADA',
         lambda: bool(afirmacoes_sem_molde(
             [('divulgacao', 'A ordem da lista. Primeiro vem quem a loja mostra como mais '
                             'vendido na busca medida, e o desempate e o preco.')]))),
        ('a frase do RODAPE da casca que estava no ar e ACHADA',
         lambda: bool(afirmacoes_sem_molde(
             [('casca', 'Isso nunca muda a ordem das recomendacoes — quem decide a ordem e '
                        'o que o fabricante declara.')]))),
        ('a frase do BLOCO DE COMPRA que estava no ar e ACHADA',
         lambda: bool(afirmacoes_sem_molde(
             [('produto', 'Os 16 anuncios abaixo foram lidos em 04/11/2026. A ordem e por '
                          'venda medida e depois por preco.')]))),
        ('a REMISSAO do rodape novo PASSA — dizer onde o criterio esta nao e declara-lo',
         lambda: not afirmacoes_sem_molde(
             [('casca', 'Isso nunca muda a ordem das recomendacoes, e o criterio que decide '
                        'essa ordem esta escrito na pagina que explica como este site ganha '
                        'dinheiro.')])),
        # OS DOIS MUNDOS DA QUARTA COPIA — 13/11/2026, item 3 do despacho da ronda
        # de hoje. As duas cadeias abaixo sao LITERAIS do que
        # `dados/paginas-de-produto.json` servia nas duas paginas de produto, e
        # as duas PASSAVAM pela regua de 11/11: a regra 3 varria aquele arquivo,
        # e o vocabulario dela nao tinha forma que casasse `a ordem DOS CARTOES
        # e por`. Elas estao aqui, e nao so o conserto, porque mundo que reprova
        # e o que impede a terceira volta.
        ('a QUARTA copia do /veiculos/patinete-eletrico/ e ACHADA',
         lambda: bool(afirmacoes_sem_molde(
             [('produto.json', 'A ordem dos cartoes e por venda medida e depois por preco; '
                               'a gente nao compara comissao entre lojas e nao ordena por ela.')]))),
        ('a QUARTA copia do /veiculos/bicicleta-eletrica/ e ACHADA',
         lambda: bool(afirmacoes_sem_molde(
             [('produto.json', 'A ordem dos cartoes e por venda medida e depois por preco; '
                               'comissao nao ordena nada nesta casa.')]))),
        ('a cadeia `venda medida` sozinha e ACHADA — ela diz que a VENDA foi medida por nos',
         lambda: bool(afirmacoes_sem_molde(
             [('qualquer', 'Os cartoes saem por venda medida.')]))),
        ('o CONSERTO de hoje passa — lead-in curto mais o molde',
         lambda: not afirmacoes_sem_molde(
             [('produto.json', 'A ordem dos cartoes. %s' % MOLDE)])),
        ('a MESMA afirmacao COM o molde passa',
         lambda: not afirmacoes_sem_molde(
             [('qualquer', 'A ordem da lista. %s' % MOLDE)])),
        ('comentario de PHP com a palavra proibida NAO reprova',
         lambda: not afirmacoes_sem_molde(
             [('php', sem_comentario_php('/* quem decide a ordem e o fabricante, dizia a '
                                         'frase velha */\n$x = 1;'))])),
        ('`https://` dentro de cadeia nao e lido como comentario',
         lambda: 'shopee' in sem_comentario_php("$u = 'https://s.shopee.com.br/a';")),
    ]
    for nome, caso in mundos:
        ok = False
        try:
            ok = bool(caso())
        except Exception as e:                                 # noqa: BLE001
            falhas.append('AUTOTESTE %s: estourou %s' % (nome, type(e).__name__))
            afirmacoes += 1
            continue
        diz(ok, 'AUTOTESTE: %s — a regra nao morde (ou morde o que nao devia)' % nome)

    for n in notas:
        print('  . ' + n)
    for f in falhas:
        print('FALHA: ' + f)
    print('\n%d afirmacao(oes), %d falha(s).' % (afirmacoes, len(falhas)))
    print('APROVADO' if not falhas else 'REPROVADO')
    return 1 if falhas else 0


if __name__ == '__main__':
    sys.exit(main())
