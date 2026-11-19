#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PORTAO DA DECISAO DO PISO NA TELA — nasceu em 17/11/2026 as 19h4xZ. Sem rede.

    python3 ferramentas/teste-piso-na-tela.py

O DEFEITO QUE ELE EXISTE PARA FECHAR, e ele estava NO AR e o portao que devia
te-lo visto estava VERDE. A recoleta das 16h25Z de 17/11/2026 reescreveu as duas
consultas que viram pagina e apagou o `piso_da_busca` das duas — o campo nao e
escrito por `coletar-por-consulta.py`, e `montar()` monta o bloco DO ZERO. Com
isso `/veiculos/patinete-eletrico/` e `/veiculos/bicicleta-eletrica/` foram ao ar
na revisao 106 servindo 21 cartoes cuja unica saida de compra e a ficha de um
anuncio, sem a busca da loja que a 25.2 exige para o dia em que a ficha morrer —
e as fichas desta ilha morrem: DUAS foram aposentadas na ultima semana.

E A PARTE QUE ESTE ARQUIVO EXISTE PARA IMPEDIR: `conferir-produto-no-ar.py`
rodou DEPOIS do desembarque, com 425 afirmacoes e ZERO falha. Ele tinha dois
ramos — `if len(buscas) == 1` cobrava a linha do piso, `else` cobrava a AUSENCIA
dela ("duas buscas distintas: 'a primeira' e arbitraria") — e o mundo de ZERO
buscas caiu no `else`. A afirmacao VIROU DE LADO: passou a exigir que a pagina
NAO servisse piso, e aprovou a pagina sem piso. Nao era cegueira; era o portao
cobrando o contrario, porque a condicao do ramo saiu da MESMA FONTE que a
afirmacao devia cobrar.

A REGUA VELHA E A NOVA DISCORDAM NO MUNDO MEDIDO, e e isso que faz deste portao
uma medicao em vez de uma intencao (secao 8, e a mesma disciplina da 20.9): o
mundo `(0 buscas, 0 linhas na tela)` e exatamente o da revisao 106, a velha diz
APROVADO e a nova diz REPROVADO. O caso esta na lista abaixo com as duas
respostas escritas a mao.

=============================================================================
A SEGUNDA METADE, DE 19/11/2026: O PISO DA PAGINA QUE EXISTE E ESTA SEM VITRINE
=============================================================================

O DEFEITO, MEDIDO NO AR E NAO SUPOSTO. `/veiculos/moto-eletrica/` — a consulta
de 823 mil buscas/mes desta ilha, a de MAIOR volume do nicho — passou TRES DIAS
servindo a caixa de ausencia com ZERO link de loja: zero cartao, zero ocorrencia
de `shopee.com.br`, zero de `s.shopee`, zero de `sponsored`, e os dois unicos
links externos da pagina eram `fonts.googleapis.com` e `fonts.gstatic.com`.

E O PISO DELA EXISTIA NO BANCO, com os tres campos, desde 16/11. A causa era de
MECANISMO: `piso_da_busca` morava DENTRO do bloco da vitrine, e o bloco da
vitrine e exatamente o que nao nasce quando a coleta do dia nao alcanca o piso da
30.2. **A 25.2 chama o piso de o degrau que "nunca depende de ninguem", e era
justamente ele que desaparecia quando ninguem anuncia.**

E A CEGUEIRA DO PORTAO ERA DE OUTRA FAMILIA QUE A DE 17/11, um degrau ANTES da
afirmacao: a pagina nao estava na lista de alvos. Os alvos saiam do casamento
entre o sitemap e `vitrine['paginas']`, que e o lugar de onde a pagina sem
vitrine esta ausente POR DEFINICAO. O portao fechava 425 afirmacoes em duas
paginas e a terceira nao era aberta — a cegueira que a 32.5-b nomeia: *"regua que
nao varre todas certifica a pagina que o autor abriu"*.

A REGUA VELHA AQUI E A AUSENCIA DE REGUA, e e por isso que a discordancia se
escreve de outro jeito nesta metade: `regua_velha_sem_vitrine` devolve SEMPRE
aprovado, porque era literalmente o que acontecia — nenhuma afirmacao era feita
sobre esta pagina. Os dois mundos de fonte vazia sao onde as duas tem de
discordar.
"""

import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))


def _portao():
    """Carrega o portao de ar SO para usar a funcao pura dele.

    A regra mora no dono do arquivo e e USADA por quem precisa, nunca copiada
    (20.7): copia-la aqui faria as duas metades errarem juntas, que e a cicatriz
    do 'teste que mede a si mesmo' da secao 8.
    """
    caminho = os.path.join(AQUI, 'conferir-produto-no-ar.py')
    spec = importlib.util.spec_from_file_location('conferir_produto_no_ar', caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def regua_velha(quantas_buscas, quantos_na_tela):
    """A REGUA DE ANTES DO CONSERTO, reescrita aqui de proposito e SO aqui.

    Ela existe para uma coisa so: provar que a nova DISCORDA dela no mundo que
    foi medido. Portao que nao mostra a discordancia nao prova que o conserto
    conserta — prova que alguem escreveu codigo novo.
    """
    if quantas_buscas == 1:
        return [] if quantos_na_tela == 1 else ['linha do piso %d vez(es)' % quantos_na_tela]
    return [] if quantos_na_tela == 0 else ['serve a linha unica com %d buscas' % quantas_buscas]


def regua_velha_sem_vitrine(_tem_url, _quantos_na_tela):
    """A REGUA DE ANTES DO CONSERTO DE 19/11/2026, e ela e a AUSENCIA de regua.

    Ela devolve aprovado em todo mundo porque era isso que o portao fazia: a
    pagina sem vitrine nao entrava na lista de alvos, e portanto nenhuma
    afirmacao era feita sobre ela. Escrever "nao havia regua" como funcao e o que
    permite exigir a discordancia da 20.8 nesta metade tambem — sem ela, o
    autoteste provaria apenas que alguem escreveu codigo novo.
    """
    return []


def main():
    mod = _portao()
    veredito = mod.veredito_do_piso_da_tabela
    afirmacoes = 0
    falhas = []
    notas = []

    def diz(ok, msg):
        nonlocal afirmacoes
        afirmacoes += 1
        if not ok:
            falhas.append(msg)

    # (buscas na fonte, linhas de piso na tela, reprova?, nome do mundo)
    MUNDOS = [
        (1, 1, False, 'o mundo saudavel: uma busca na fonte, uma linha na tela'),
        (1, 0, True, 'uma busca na fonte e a tela NAO serve a linha'),
        (1, 2, True, 'uma busca na fonte e a tela serve a linha DUAS vezes'),
        (1, 14, True, 'uma busca e uma linha por cartao: o piso e da consulta, nao do anuncio'),
        (0, 0, True, 'O MUNDO MEDIDO NA REVISAO 106: zero busca na fonte, zero linha na tela'),
        (0, 1, True, 'zero busca na fonte e a tela serve piso: piso sem procedencia'),
        (2, 0, False, 'duas buscas distintas e nenhuma linha unica: "a primeira" e arbitraria'),
        (2, 1, True, 'duas buscas distintas e a tela escolhe uma delas'),
        (3, 0, False, 'tres buscas distintas e nenhuma linha unica'),
    ]
    for buscas, tela, deve_reprovar, nome in MUNDOS:
        try:
            saida = veredito(buscas, tela)
        except Exception as e:                                 # noqa: BLE001
            diz(False, 'MUNDO %s: estourou %s' % (nome, type(e).__name__))
            continue
        diz(isinstance(saida, list), 'MUNDO %s: a funcao nao devolveu lista' % nome)
        diz(bool(saida) == deve_reprovar,
            'MUNDO %s: esperava %s e a funcao disse %s (%r)'
            % (nome, 'REPROVAR' if deve_reprovar else 'APROVAR',
               'REPROVAR' if saida else 'APROVAR', saida))
        # TODA FALHA DIZ O CONSERTO EM PALAVRAS, nunca so o numero: a 20.4 e
        # literal sobre linha que nao diz `ok` trazer o motivo escrito nela.
        for linha in saida:
            diz(len(linha.strip()) > 30 and not linha.strip().startswith('('),
                'MUNDO %s: a falha %r nao diz em palavras o que esta errado' % (nome, linha))

    # A DISCORDANCIA COM A REGUA VELHA, no mundo medido e so nele.
    velha = regua_velha(0, 0)
    nova = veredito(0, 0)
    diz(not velha and bool(nova),
        'A REGUA VELHA TINHA DE APROVAR O MUNDO DA REVISAO 106 E A NOVA DE REPROVAR, e agora '
        'elas dizem velha=%r nova=%r — sem essa discordancia este portao nao prova conserto '
        'nenhum' % (velha, nova))
    notas.append('mundo medido (0 busca, 0 linha): regua velha APROVA, regua nova REPROVA — '
                 'a discordancia vale as 425 afirmacoes verdes da revisao 106')

    # E A DISCORDANCIA E DE UM MUNDO SO: no resto as duas tem de concordar, senao
    # o conserto AFROUXOU alguma coisa em vez de apertar (a trava da secao 8).
    for buscas, tela, _deve, nome in MUNDOS:
        if (buscas, tela) == (0, 0):
            continue
        # O OUTRO MUNDO DE FONTE VAZIA, `(0, 1)`: a velha o reprovava por
        # ACIDENTE (o `else` cobrava ausencia de linha) e a nova o reprova por
        # MOTIVO, dizendo duas coisas porque os consertos sao dois. O veredito e
        # o mesmo nos dois, e e o veredito que se cobra aqui.
        diz(bool(regua_velha(buscas, tela)) == bool(veredito(buscas, tela)),
            'MUNDO %s: o conserto mudou um veredito que nao era o do defeito (velha=%r nova=%r) '
            '— afrouxamento ou aperto nao pedido' % (nome, regua_velha(buscas, tela),
                                                     veredito(buscas, tela)))

    # A FUNCAO E PURA: duas chamadas iguais dao a mesma resposta e ela nao toca
    # arquivo nenhum. Afirmacao barata, e ela e o que autoriza fabricar mundo.
    diz(veredito(0, 0) == veredito(0, 0), 'a funcao nao e deterministica')

    # =====================================================================
    # A SEGUNDA METADE: O PISO DA PAGINA SEM VITRINE (19/11/2026)
    # =====================================================================
    sem = mod.veredito_do_piso_sem_vitrine

    # (tem url na fonte, linhas de piso na tela, reprova?, nome do mundo)
    MUNDOS_SEM = [
        (True, 1, False, 'o mundo saudavel: a fonte tem `url_busca` e a caixa serve UMA linha'),
        (True, 0, True, 'O MUNDO MEDIDO EM 19/11: a fonte tem o piso e a pagina de 823 mil '
                        'buscas/mes nao serve link de loja nenhum'),
        (True, 2, True, 'a fonte tem o piso e a caixa serve a linha DUAS vezes'),
        (False, 0, True, 'a fonte NAO tem piso para ela: a pagina esta no ar sem saida de compra'),
        (False, 1, True, 'a fonte nao tem piso e a tela serve piso: numero de tela sem '
                         'procedencia'),
    ]
    for tem, tela, deve_reprovar, nome in MUNDOS_SEM:
        try:
            saida = sem(tem, tela)
        except Exception as e:                                 # noqa: BLE001
            diz(False, 'MUNDO SEM VITRINE %s: estourou %s' % (nome, type(e).__name__))
            continue
        diz(isinstance(saida, list),
            'MUNDO SEM VITRINE %s: a funcao nao devolveu lista' % nome)
        diz(bool(saida) == deve_reprovar,
            'MUNDO SEM VITRINE %s: esperava %s e a funcao disse %s (%r)'
            % (nome, 'REPROVAR' if deve_reprovar else 'APROVAR',
               'REPROVAR' if saida else 'APROVAR', saida))
        for linha in saida:
            diz(len(linha.strip()) > 30 and not linha.strip().startswith('('),
                'MUNDO SEM VITRINE %s: a falha %r nao diz em palavras o que esta errado'
                % (nome, linha))

    # A DISCORDANCIA DA 20.8 NESTA METADE: a regua velha era a AUSENCIA de regua,
    # entao ela aprova TUDO — e tem de discordar da nova em todo mundo que a nova
    # reprova. Sem isso este bloco nao prova conserto nenhum.
    discordaram = 0
    for tem, tela, deve_reprovar, nome in MUNDOS_SEM:
        velha = regua_velha_sem_vitrine(tem, tela)
        nova_ = sem(tem, tela)
        diz(not velha, 'a regua velha de pagina sem vitrine devia aprovar TUDO (ela era a '
                       'ausencia de regua) e no mundo %s ela disse %r' % (nome, velha))
        if deve_reprovar:
            discordaram += 1
            diz(bool(nova_) and not velha,
                'MUNDO SEM VITRINE %s: a velha aprovava e a nova tinha de reprovar, e elas '
                'dizem velha=%r nova=%r' % (nome, velha, nova_))
    diz(discordaram >= 4,
        'a discordancia com a ausencia de regua tem de aparecer em pelo menos 4 mundos e '
        'apareceu em %d' % discordaram)
    notas.append('pagina sem vitrine: a regua velha era a AUSENCIA de regua (a pagina nao '
                 'entrava na lista de alvos) e a nova REPROVA em %d dos %d mundos — a '
                 'discordancia vale os tres dias de `/veiculos/moto-eletrica/` no ar sem '
                 'nenhum link de loja' % (discordaram, len(MUNDOS_SEM)))

    # A FUNCAO E PURA, igual a irma.
    diz(sem(True, 0) == sem(True, 0),
        'o veredito do piso sem vitrine nao e deterministico')

    # E AS DUAS FUNCOES NAO SAO A MESMA: a da tabela APROVA `(2 buscas, 0 linhas)`
    # porque "a primeira e arbitraria", e a da pagina sem vitrine REPROVA
    # `(sem url, 0 linhas)` porque ali a ausencia nao tem desempate nenhum. Medir
    # as duas com uma regua so era o que fazia a caixa de ausencia aprovar vazia.
    diz(not veredito(2, 0) and bool(sem(False, 0)),
        'as duas familias de pagina sao medidas pela MESMA regua: a da tabela tem de aprovar '
        '(2 buscas, 0 linhas) e a sem vitrine tem de reprovar (sem url, 0 linhas)')

    print('PORTAO DA DECISAO DO PISO NA TELA — RODAMETRIA (sem rede)')
    for n in notas:
        print('  . ' + n)
    for f in falhas:
        print('FALHA: ' + f)
    print('\n%d mundo(s) fabricado(s) e %d afirmacao(oes), %d falha(s).'
          % (len(MUNDOS) + len(MUNDOS_SEM), afirmacoes, len(falhas)))
    print('APROVADO' if not falhas else 'REPROVADO')
    return 1 if falhas else 0


if __name__ == '__main__':
    sys.exit(main())
