#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PORTAO DO SINONIMO DA 30.4 NA TELA — nasceu em 24/11/2026 as 16h4xZ. Sem rede.

    python3 ferramentas/teste-sinonimo-na-tela.py

O DEFEITO QUE ELE EXISTE PARA FECHAR, E ELE ESTAVA NO AR COM A BANCADA INTEIRA
VERDE: 64 portoes sem rede e 70 com rede, 0 falha nas duas, medidos as 16h2xZ de
24/11/2026, minutos antes desta medicao.

A 30.4 do ARQUIPELAGO.md decide que consulta canibalizada NAO recebe URL propria
e e carregada pela pagina que existe, "com a consulta como ancora". Nesta ilha a
declaracao disso e o campo `sinonimos_no_corpo`, em
`dados/consultas-de-produto.json`. AS DUAS MEDICOES DE 24/11/2026, as duas no ar
com quebra de cache:

(1) `/veiculos/moto-eletrica/` declara `motos elétricas para adultos` — consulta
    de 201 MIL BUSCAS/MES, veredito `alvo` visto no Chrome do Raphael em
    27/10/2026 — e servia a expressao **ZERO vez**: zero no texto visivel e zero
    no HTML inteiro. A 30.4 fechou aquela consulta em favor desta pagina; a
    pagina nao diz a palavra. A consulta nao tem URL e tambem nao tem casa.

(2) `/veiculos/patinete-eletrico/` declara `scooter elétrico` e
    `patinete elétrico dobrável`, e as duas estavam na tela POR ACIDENTE: elas
    vinham dos TITULOS DOS ANUNCIOS que a loja escreveu. Contado em
    `dados/vitrine-de-produto.json`: 1 e 4 ocorrencias — exatamente os 1 e 4
    contados no HTML servido, e ZERO na prosa declarada da ilha. O dia em que
    aquela coleta nao alcancar o piso de tres anuncios da 30.2 — que e
    precisamente o que aconteceu com a pagina da moto — as duas palavras somem
    junto com a vitrine.

E A CAUSA DE NINGUEM VER TEM NOME: `sinonimos_no_corpo` nao era lido por
ferramenta, portao nem snippet NENHUM. `grep -rn 'sinonimos_no_corpo'` em
`ferramentas/` e `snippets/` devolvia ZERO. Campo declarado que ninguem le e
RASTRO e nao mecanismo — a 20.7 escrita com outro campo, no mesmo repositorio
que ja a pagou com as constantes de versao dos snippets.

E E O TERCEIRO CASO DA MESMA FAMILIA NA MESMA PAGINA EM CINCO DIAS: a 25.2-c
(19/11, o LINK de compra dentro do bloco que nao nasce) e a 32.9 (20/11, a VOZ
dentro do bloco que nao nasce). Aqui e a PALAVRA.

=============================================================================
A REGUA VELHA E A AUSENCIA DE REGUA, E E ISSO QUE A DISCORDANCIA PROVA
=============================================================================

Nao havia afirmacao nenhuma sobre sinonimo em portao algum desta ilha, entao
`regua_velha` devolve aprovado em TODO mundo — escrever "nao havia regua" como
funcao e o que permite exigir a discordancia da 20.8 aqui tambem. Sem ela, este
arquivo provaria apenas que alguem escreveu codigo novo.

E ESTE PORTAO MORDE O REPOSITORIO, nao so os mundos fabricados: a segunda metade
dele le `dados/consultas-de-produto.json` e `dados/paginas-de-produto.json` de
verdade e cobra, consulta por consulta, que cada sinonimo declarado esteja numa
string SEM MOLDE de um dos `campos_sem_vitrine` — a prosa que sobrevive a
degradacao. Rodado antes do conserto de 24/11, ele reprova em TRES sinonimos de
DUAS paginas.
"""

import importlib.util
import json
import os
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)


def _modulo(nome, arquivo):
    """Carrega o dono da regra SO para usar a funcao pura dele.

    A regra mora no dono do arquivo e e USADA por quem precisa, nunca copiada
    (20.7): copia-la aqui faria as duas metades errarem juntas.
    """
    caminho = os.path.join(AQUI, arquivo)
    spec = importlib.util.spec_from_file_location(nome, caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def regua_velha(_na_voz, _no_html):
    """A REGUA DE ANTES DO CONSERTO DE 24/11/2026, e ela e a AUSENCIA de regua.

    Devolve aprovado em todo mundo porque era isso que a bancada fazia: nenhuma
    afirmacao era feita sobre `sinonimos_no_corpo` em lugar nenhum — o campo nao
    era lido por ninguem.
    """
    return []


def _normalizar(t):
    t = unicodedata.normalize("NFC", str(t))
    return " ".join(t.lower().split())


def main():
    portao = _modulo("rodametria_conferir_produto_no_ar", "conferir-produto-no-ar.py")
    veredito = portao.veredito_do_sinonimo_declarado
    afirmacoes = 0
    falhas = []
    notas = []

    def diz(ok, msg):
        nonlocal afirmacoes
        afirmacoes += 1
        if not ok:
            falhas.append(msg)

    # =====================================================================
    # PRIMEIRA METADE: OS MUNDOS FABRICADOS
    # =====================================================================
    # (na voz declarada, no HTML servido, quantas falhas, nome do mundo)
    MUNDOS = [
        (True, True, 0,
         'o mundo saudavel: a ilha escreve a palavra numa string sem molde e a pagina a serve'),
        (False, True, 1,
         'O MUNDO MEDIDO NO PATINETE EM 24/11: a palavra esta na tela e quem a escreveu foi a '
         'LOJA, no titulo do anuncio — ela vai embora com a vitrine'),
        (True, False, 1,
         'O MUNDO MEDIDO NA MOTO EM 24/11: a ilha declara o sinonimo e a pagina de 201 mil '
         'buscas/mes nao o serve nenhuma vez'),
        (False, False, 2,
         'as duas pontas no chao: a consulta foi fechada por canibalizacao e nao tem URL nem '
         'casa, e nem a voz da ilha a nomeia'),
    ]
    for na_voz, no_html, quantas, nome in MUNDOS:
        try:
            saida = veredito('motos elétricas para adultos', na_voz, no_html)
        except Exception as e:                                 # noqa: BLE001
            diz(False, 'MUNDO %s: estourou %s' % (nome, type(e).__name__))
            continue
        diz(isinstance(saida, list), 'MUNDO %s: a funcao nao devolveu lista' % nome)
        diz(len(saida) == quantas,
            'MUNDO %s: esperava %d falha(s) e a funcao deu %d (%r)'
            % (nome, quantas, len(saida), saida))
        # AS DUAS CAUSAS SAIEM SEPARADAS, nunca somadas numa frase (a licao da
        # 20.5: portao que junta duas causas manda consertar a errada).
        for linha in saida:
            diz(len(linha.strip()) > 40,
                'MUNDO %s: a falha %r nao diz em palavras o que esta errado' % (nome, linha))
            diz('motos elétricas para adultos' in linha,
                'MUNDO %s: a falha %r nao NOMEIA o sinonimo, e sem o nome quem le nao sabe '
                'qual palavra consertar' % (nome, linha))

    # O MUNDO DAS DUAS PONTAS NO CHAO DIZ DUAS COISAS DIFERENTES, e isto e a
    # afirmacao que impede alguem de "simplificar" a funcao somando as causas:
    # os consertos sao dois — um e escrever prosa, o outro e descobrir por que a
    # prosa nao chega a tela.
    duas = veredito('x', False, False)
    diz(len(duas) == 2 and duas[0] != duas[1],
        'as duas pontas no chao tem de produzir DUAS frases diferentes, e produziram %r' % duas)

    # A DISCORDANCIA COM A AUSENCIA DE REGUA, nos mundos medidos e nos dois.
    discordaram = 0
    for na_voz, no_html, quantas, nome in MUNDOS:
        velha = regua_velha(na_voz, no_html)
        nova = veredito('motos elétricas para adultos', na_voz, no_html)
        diz(not velha,
            'a regua velha devia aprovar TUDO (ela era a ausencia de regua) e no mundo %s ela '
            'disse %r' % (nome, velha))
        if quantas:
            discordaram += 1
            diz(bool(nova) and not velha,
                'MUNDO %s: a velha aprovava e a nova tinha de reprovar, e elas dizem velha=%r '
                'nova=%r' % (nome, velha, nova))
    diz(discordaram == 3,
        'a discordancia com a ausencia de regua tem de aparecer nos TRES mundos defeituosos e '
        'apareceu em %d' % discordaram)
    notas.append('mundos fabricados: a regua velha era a AUSENCIA de regua e a nova REPROVA em '
                 '%d dos %d mundos — a discordancia vale os 64 portoes sem rede e os 70 com '
                 'rede que estavam VERDES sobre as duas paginas' % (discordaram, len(MUNDOS)))

    # A FUNCAO E PURA: duas chamadas iguais dao a mesma resposta.
    diz(veredito('x', False, False) == veredito('x', False, False),
        'o veredito do sinonimo nao e deterministico')

    # =====================================================================
    # SEGUNDA METADE: O REPOSITORIO DE VERDADE
    # =====================================================================
    # Aqui o portao morde o arquivo, e e esta metade que vai de REPROVADO para
    # APROVADO com o conserto da prosa. A regua da voz vem do DONO da camada
    # declarada (`gerar-vitrine-de-produto.py`), nunca reescrita aqui.
    gerador = _modulo("rodametria_gerar_vitrine_de_produto", "gerar-vitrine-de-produto.py")
    voz_sem_vitrine = gerador.voz_sem_vitrine

    with open(os.path.join(ILHA, 'dados', 'consultas-de-produto.json'), encoding='utf-8') as f:
        decl = json.load(f)
    with open(os.path.join(ILHA, 'dados', 'paginas-de-produto.json'), encoding='utf-8') as f:
        ed = json.load(f)
    paginas = {p.get('id'): p for p in (ed.get('paginas') or []) if p.get('id')}

    cobrados = 0
    for c in (decl.get('consultas') or []):
        sins = c.get('sinonimos_no_corpo') or []
        if not sins or not c.get('publicar_declarado'):
            continue
        pag = paginas.get(c.get('id'))
        diz(pag is not None,
            'a consulta %s diz `publicar_declarado: true` e nao tem entrada em '
            '`paginas-de-produto.json`: a voz dela nao existe para ser conferida'
            % c.get('id'))
        if pag is None:
            continue
        voz = _normalizar(json.dumps(voz_sem_vitrine(ed, pag), ensure_ascii=False))
        for s_ in sins:
            cobrados += 1
            # SO A PONTA DA VOZ E COBRADA AQUI, e por isso `no_html_servido`
            # entra como True: esta metade nao abre pagina nenhuma, e afirmar
            # sobre o ar sem o ter lido seria o numero de tela digitado. A ponta
            # do ar e de `conferir_os_sinonimos()`, no portao com rede.
            for linha in veredito(s_, _normalizar(s_) in voz, True):
                diz(False, '%s %s' % (c.get('id'), linha))
    diz(cobrados >= 3,
        'esta metade tem de cobrar pelo menos os 3 sinonimos das duas paginas no ar e cobrou '
        '%d — regua que nao varre todas certifica a pagina que o autor abriu (32.5-b)'
        % cobrados)
    notas.append('repositorio: %d sinonimo(s) declarado(s) de pagina publicada cobrados contra '
                 'a voz que sobrevive sem vitrine' % cobrados)

    print('PORTAO DO SINONIMO DA 30.4 NA TELA — RODAMETRIA (sem rede)')
    for n in notas:
        print('  . ' + n)
    for f in falhas:
        print('FALHA: ' + f)
    print('\n%d mundo(s) fabricado(s) e %d afirmacao(oes), %d falha(s).'
          % (len(MUNDOS), afirmacoes, len(falhas)))
    print('APROVADO' if not falhas else 'REPROVADO')
    return 1 if falhas else 0


if __name__ == '__main__':
    sys.exit(main())
