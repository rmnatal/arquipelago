#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A REGRA DE CASAMENTO desta ilha: quando um anuncio da Shopee E o registro do banco.

Este arquivo nao fala com a rede e nao grava nada. Ele e so a regra, separada
de proposito, porque quem a usa (`coletar-shopee.py`) e quem a ATACA
(`mutacoes-casamento.py`) precisam da MESMA funcao — regra copiada em dois
lugares e regra que a bateria mede em um lugar e o banco usa no outro.

---------------------------------------------------------------------------
POR QUE ELA EXISTE, e o numero que a pediu
---------------------------------------------------------------------------
Em 29/09/2026, 28 dos 38 registros deste banco estavam no DEGRAU 4 da escada da
secao 25.1 — o piso, a pagina de busca, que nao esgota e nao apodrece mas
converte pior que ficha de produto. Nenhum deles tinha `url`, e o cabecalho dos
bancos dizia por que, com todas as letras: *"ficha exige casamento de item, que
a 25.7 proibe sem prova de que o anuncio e daquele SKU"*.

A prova nao existia. Agora existe, e e esta funcao.

---------------------------------------------------------------------------
O QUE A API DEVOLVE, medido antes de a regra ser escrita (29/09/2026, 16h2xZ)
---------------------------------------------------------------------------
`verniz acrilico brilhante acrilex`, oito primeiros resultados:

    1  Verniz para Couro Acrilex 100ml Fosco Semibrilho Brilhante Base Agua
    2  Verniz Acrilico Brilhante Transparente Acrilex 250ml Artesanato Tela
    3  Verniz Para Tinta Couro 100ml Acrilex - 1 Unidade de cada (Semibrilho...
    4  Verniz Acrilico Brilhante Acrilex 100ml
    6  Verniz Vitral Acrilex 100ml Incolor Brilhante Madreperola
    7  Verniz Acrilico Acrilex 100ml / 250ml / 500ml (Fosco ou Brilhante)
    8  Verniz Acrilex Acrilfix Fosco, SemiBrilho ou Brilhante Spray 300 ml

O banco tem TRES vernizes da Acrilex: acrilico brilhante, acrilico fosco e
acrilfix brilhante. Dos oito titulos acima, **dois** identificam um registro so
(o 2 e o 4). Os outros seis ou sao outro produto (couro, vitral) ou vendem a
ESCOLHA entre dois registros no mesmo anuncio — e anuncio que cobre dois
registros nao identifica nenhum (armadilha 5 da 25.7).

Repare no 8: ele traz `acrilfix` E `fosco` E `brilhante`. Uma regra que so
exigisse os tokens do registro o aprovaria como acrilfix-brilhante, porque
`acrilfix-fosco` nao existe no banco para disputar. **Por isso a regra tem duas
metades e a segunda e a que vale mais:** nao basta o titulo trazer o que separa
X dos irmaos; ele tambem nao pode trazer o que separa os IRMAOS de X.

---------------------------------------------------------------------------
A REGRA, em cinco travas, e todas as cinco tem de passar
---------------------------------------------------------------------------
1. **MARCA.** A marca de X aparece no titulo. Sem ela, `verniz acrilico
   brilhante` e o catalogo de meio Brasil.
2. **A CABECA DO TITULO E O PRODUTO.** As primeiras quatro palavras do titulo
   trazem pelo menos um token do nome comercial de X que nao seja a marca. E a
   armadilha 1 da 25.7 traduzida para este nicho: *"Kit 3 Pinceis para aplicar
   Verniz Acrilex Brilhante"* tem o verniz no meio e um pincel na cabeca — quem
   compra leva pincel. O tipo tem de ser o objeto, nao uma palavra perdida.
3. **SEPARA DE CADA IRMAO (a metade positiva).** Para cada irmao Y — outro
   registro do banco da MESMA MARCA —, o titulo traz pelo menos um token que
   esta em X e nao esta em Y. Se nao traz, o titulo nao sabe dizer se e X ou Y.
4. **NAO TRAZ O QUE E DO IRMAO (a metade negativa).** Para cada irmao PROXIMO —
   mesma marca E mesmo `tipo` —, o titulo nao traz nenhum token que esteja em Y
   e nao em X. E o titulo 8 la em cima: quem escreve *"Fosco, SemiBrilho ou
   Brilhante"* esta vendendo a escolha, e a escolha nao e um SKU.
5a. **NENHUMA PALAVRA DE ARMADILHA.** `kit`, `combo`, `apostila`, `curso`,
   `molde`, `usado`, `recondicionado` — a armadilha 2 da 25.7 (*"KIT nao e
   quantidade quando o registro nao e um kit"*). A lista NAO tem `manual`, e
   isso e medicao e nao esquecimento: tres registros do banco sao *"Cortador de
   ceramicas e azulejos MANUAL"*, e a palavra e do produto.
5b. **O TITULO TRAZ O NOME COMERCIAL INTEIRO.** Todo token do
   `nome_comercial` de X aparece no titulo. Esta trava nasceu DEPOIS das
   outras cinco e por um casamento errado que elas aprovaram, no ensaio de
   29/09/2026: `quartzolit-fundo-selador` (*"fundo selador quartzolit"*) casou
   com *"Selador PU30 Cinza Quartzolit 600g"*, que e um selante de poliuretano
   e nao o fundo selador acrilico de parede. As travas 3 e 4 nao viram nada
   porque nenhum irmao da Quartzolit disputa a palavra `selador` — e **token
   que nenhum irmao tem nunca era exigido de ninguem**. O buraco nao era do
   irmao: era de nao cobrar do titulo o nome que o fabricante deu ao produto.
   Ela custa falso negativo, e esse e o lado certo de errar: casamento errado
   no banco e pior que casamento nenhum, porque parece dado.

E, por cima das cinco, a **UNICIDADE**: o anuncio casa quando UM registro do
banco passa nas cinco. Dois registros passando e a armadilha 5 — no maximo um
esta certo e nao ha como dizer qual, entao os dois caem.

---------------------------------------------------------------------------
DUAS DECISOES DE TEXTO QUE MUDAM O RESULTADO, escritas para poderem ser atacadas
---------------------------------------------------------------------------
- **Acento e caixa saem antes de comparar.** A Shopee escreve `Acrilico` e
  `Acrilico`; o banco escreve os dois. Comparar com acento faz a regra depender
  de quem digitou.
- **Plural: o `s` final cai em token de 5 letras ou mais.** `pisos`/`piso` e
  `pastilhas`/`pastilha` sao a mesma palavra; `mais`/`mai` nao sao, e e por isso
  que o corte e por tamanho. Sem isso a trava 3 reprova casamento certo por
  causa de uma letra.
"""

import re
import unicodedata

# Palavras que nao separam nada e por isso nao entram em token nenhum: elas
# aparecem em quase todo nome comercial e em quase todo titulo de anuncio, e
# token que esta em todo lugar nao distingue lugar nenhum.
VAZIAS = {
    'de', 'da', 'do', 'das', 'dos', 'e', 'com', 'para', 'por', 'em', 'a', 'o',
    'as', 'os', 'ao', 'na', 'no', 'um', 'uma', 'ou', 'the', 'ml', 'l', 'kg',
    'g', 'cm', 'mm', 'un', 'pc', 'pcs', 'und', 'unidade', 'unidades',
}

# ARMADILHA 2 DA 25.7. `manual` NAO esta aqui: ver a trava 5 no cabecalho.
ARMADILHAS = [
    'kit', 'combo', 'apostila', 'curso', 'ebook', 'e-book', 'molde',
    'usado', 'seminovo', 'recondicionado', 'seminova',
]

CABECA = 4   # quantas palavras do titulo contam como "a cabeca"


def sem_acento(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto or '')
                   if unicodedata.category(c) != 'Mn')


def normalizar(palavra):
    """Uma palavra comparavel: sem acento, minuscula, sem plural obvio."""
    p = sem_acento(palavra).lower()
    if len(p) >= 5 and p.endswith('s'):
        p = p[:-1]
    return p


def tokens(texto):
    """Os tokens comparaveis de um texto, na ordem, sem as palavras vazias.

    A quebra e por caractere que nao seja letra nem digito, entao `VDEC 51` e
    `VDEC-51` dao os mesmos dois tokens e `510` NUNCA e `51`: e a armadilha 4
    da 25.7 (*o sufixo faz outro aparelho*) resolvida pela quebra, nao por uma
    lista de sufixos que alguem teria de lembrar de manter.
    """
    fora = []
    for bruto in re.split(r'[^0-9A-Za-zÀ-ÿ]+', texto or ''):
        if not bruto:
            continue
        p = normalizar(bruto)
        if p and p not in VAZIAS:
            fora.append(p)
    return fora


def _conjunto_do_registro(reg):
    """O que identifica um registro: nome comercial + codigo + marca.

    O `id` NAO entra, de proposito: ele e escrito por nos e carrega palavras que
    nenhum vendedor escreveria (`acrilex-verniz-acrilico-brilhante` traz a marca
    duas vezes). O que se compara com o titulo do vendedor e o que o FABRICANTE
    batiza, que e a secao 26 do contrato.
    """
    partes = [reg.get('nome_comercial') or '', reg.get('marca') or '']
    if reg.get('codigo_fabricante'):
        partes.append(str(reg['codigo_fabricante']))
    return set(tokens(' '.join(partes)))


def _sem_a_marca(conjunto, reg):
    return conjunto - set(tokens(reg.get('marca') or ''))


def compativel(reg, titulo, irmaos):
    """As cinco travas. Devolve (True, None) ou (False, 'o motivo em uma linha').

    `irmaos` e a lista dos outros registros da MESMA MARCA, cada um um dicionario
    do banco. Quem monta a lista e quem chama — esta funcao nao le arquivo.
    """
    t = set(tokens(titulo))
    cabeca = set(tokens(' '.join((titulo or '').split()[:CABECA])))
    meu = _conjunto_do_registro(reg)

    marca = set(tokens(reg.get('marca') or ''))
    if marca and not marca <= t:
        return False, 'a marca %s nao aparece no titulo' % reg.get('marca')

    if not (_sem_a_marca(meu, reg) & cabeca):
        return False, ('a cabeca do titulo nao e este produto: nenhuma das %d '
                       'primeiras palavras esta no nome comercial' % CABECA)

    for palavra in ARMADILHAS:
        if normalizar(palavra) in t:
            return False, 'o titulo traz a palavra de armadilha "%s"' % palavra

    faltando = sorted(set(tokens(reg.get('nome_comercial') or '')) - t)
    if faltando:
        return False, ('o titulo nao traz %s, que esta no nome comercial deste '
                       'registro' % faltando)

    for irmao in irmaos:
        if irmao.get('id') == reg.get('id'):
            continue
        dele = _conjunto_do_registro(irmao)
        so_meu = meu - dele
        if so_meu and not (so_meu & t):
            return False, ('o titulo nao separa este registro de %s: nenhum de %s '
                           'aparece' % (irmao.get('id'), sorted(so_meu)))
        if not so_meu:
            return False, ('este registro nao tem nenhum token que o separe de %s '
                           '— dois registros com o mesmo nome nunca se identificam'
                           % irmao.get('id'))
        mesmo_tipo = (irmao.get('tipo') == reg.get('tipo'))
        if mesmo_tipo:
            so_dele = dele - meu
            invasores = sorted(so_dele & t)
            if invasores:
                return False, ('o titulo traz %s, que e de %s: o anuncio esta '
                               'vendendo a escolha entre os dois'
                               % (invasores, irmao.get('id')))
    return True, None


def casar(titulo, candidatos, irmaos_de):
    """Qual registro este titulo identifica — e so quando identifica UM.

    `candidatos` sao os registros que podem casar; `irmaos_de` e uma funcao que
    devolve os irmaos de um registro. Devolve (registro_ou_None, laudo), e o
    laudo tem uma linha por candidato, sempre — inclusive quando casa, porque
    casamento sem laudo e casamento que ninguem consegue auditar depois.
    """
    passaram, laudo = [], []
    for reg in candidatos:
        ok, motivo = compativel(reg, titulo, irmaos_de(reg))
        laudo.append({'id': reg.get('id'), 'passou': ok, 'motivo': motivo})
        if ok:
            passaram.append(reg)
    if len(passaram) == 1:
        return passaram[0], laudo
    if len(passaram) > 1:
        for linha in laudo:
            if linha['passou']:
                linha['motivo'] = ('passou nas cinco travas, mas %d registros '
                                   'passaram no mesmo titulo — armadilha 5 da '
                                   '25.7, os dois caem' % len(passaram))
                linha['passou'] = False
        return None, laudo
    return None, laudo
