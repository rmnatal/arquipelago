#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PORTAO DA REPETICAO DA SHOPEE — nasceu em 23/11/2026. Sem rede.

    python3 ferramentas/teste-shopee-repeticao.py

O QUE ELE EXISTE PARA GUARDAR. Medido em 23/11/2026, desta nuvem, com a
credencial do ambiente e o mesmo corpo de consulta: `error [10000]: System
Error`, com HTTP 200, em **2 de 10** chamadas identicas e seguidas. As outras
oito voltaram com a lista de ofertas. Nao e credencial, nao e assinatura e nao e
egresso — e o servidor da Shopee recusando uma chamada que ele aceita no segundo
seguinte.

POR QUE UM EM CINCO E PIOR DO QUE PARECE: a coleta de uma ilha faz DEZENAS de
chamadas numa passada (a escada de chaves de cada consulta, mais o encurtador por
anuncio). Sem repeticao, a coleta inteira morre quase sempre, e morre NO MEIO — e
o que a execucao le e um traceback, que tem cara de defeito do codigo ou de
credencial vencida. O item 3 do despacho de 23/11 morreu exatamente assim, na
primeira consulta da primeira tentativa.

A REGRA E A DA SECAO 4 E DA 20.2, aplicada a esta porta: *"falha de rede so vira
bloqueio depois de repetir"* — uma falha isolada e o tunel, tres seguidas e
bloqueio. E o que NAO se repete e recusa de CREDENCIAL ou de ASSINATURA: repetir
ali e bater na porta com a chave errada, e a frase de erro e justamente o que diz
ao Raphael o que fazer (25.6). Esta e a unica coisa que este portao mede, e ela e
a decisao: QUANDO vale repetir.

POR QUE ELE E UM PORTAO E NAO UMA CONFERENCIA DE CABECA: repeticao e trava que so
e exercitada quando o mundo quebra, e mundo que quebra nao acontece sob demanda
(secao 8: "regua escrita para um mundo que nunca aconteceu nasce errada sem poder
falhar"). A decisao foi extraida para `_vale_repetir()`, funcao pura, e aqui os
mundos sao FABRICADOS.
"""

import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))


def _api():
    """Carrega a ferramenta SO para usar a funcao pura dela — nunca copia a
    regra (20.7): copia-la aqui faria as duas metades errarem juntas."""
    caminho = os.path.join(AQUI, 'shopee-api.py')
    spec = importlib.util.spec_from_file_location('shopee_api', caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    mod = _api()
    vale = mod._vale_repetir
    erro = mod.ErroDaShopee
    falhas, afirmacoes, notas = [], 0, []

    def diz(ok, msg):
        nonlocal afirmacoes
        afirmacoes += 1
        if not ok:
            falhas.append(msg)

    MUNDOS = [
        ('erro da API: [10000] System Error', True,
         'O MUNDO MEDIDO EM 23/11/2026: 2 de 10 chamadas identicas'),
        ('erro da API: error [10000]: System Error', True,
         'a MESMA recusa na outra forma de frase que a ferramenta monta — as duas '
         'existem no codigo (`errors` do GraphQL e `error` da raiz), e uma regua que '
         'so visse uma delas repetiria metade das vezes'),
        ('a Shopee devolveu HTTP 502', True, 'gateway da Shopee'),
        ('a Shopee devolveu HTTP 503', True, 'servico da Shopee indisponivel'),
        ('erro da API: [10020] Invalid Credential', False,
         'CREDENCIAL: repetir e bater na porta com a chave errada, e o conserto e do '
         'Raphael (25.6)'),
        ('erro da API: Invalid Signature', False,
         'ASSINATURA: corpo assinado duas vezes nao melhora na terceira'),
        ('a Shopee devolveu HTTP 401', False, 'recusa de autorizacao, nao intermitencia'),
        ('nao foi possivel alcancar https://open-api.affiliate.shopee.com.br/graphql '
         '(egresso)', False,
         'EGRESSO FECHADO nao e intermitencia da Shopee: a frase de erro nomeia a lista '
         'de dominios permitidos, que e passo do Raphael (20.1), e repetir esconderia '
         'isso atras de uma espera'),
        ('a Shopee devolveu algo que nao e JSON (0 bytes)', False,
         'resposta que nao e JSON e defeito a investigar, nao a esperar'),
    ]
    for texto, espera, nome in MUNDOS:
        try:
            deu = vale(erro(texto))
        except Exception as e:                                 # noqa: BLE001
            diz(False, 'MUNDO %s: estourou %s' % (nome, type(e).__name__))
            continue
        diz(isinstance(deu, bool), 'MUNDO %s: a decisao nao e booleana' % nome)
        diz(deu is espera,
            'MUNDO %s (%r): esperava %s e a funcao disse %s'
            % (nome, texto, 'REPETIR' if espera else 'NAO REPETIR',
               'REPETIR' if deu else 'NAO REPETIR'))

    # A REGUA VELHA ERA A AUSENCIA DE REGUA — nenhuma chamada era repetida —,
    # entao a discordancia da 20.8 se escreve assim: ela diz NAO REPETIR em todo
    # mundo, e tem de discordar da nova exatamente nos transitorios.
    discordaram = sum(1 for texto, espera, _n in MUNDOS if espera)
    diz(discordaram >= 4,
        'a discordancia com a ausencia de repeticao tem de aparecer em pelo menos 4 '
        'mundos e apareceu em %d' % discordaram)
    notas.append('a regua velha era a AUSENCIA de repeticao (uma recusa transitoria '
                 'matava a coleta inteira no meio) e a nova repete em %d dos %d mundos'
                 % (discordaram, len(MUNDOS)))

    # OS NUMEROS DA TRAVA NAO SAO DIGITADOS AQUI: saem da ferramenta. Numero
    # repetido em teste comeca igual e envelhece de um lado so (20.7).
    diz(mod.TENTATIVAS >= 3,
        'TENTATIVAS e %d, e com 20%% de recusa por chamada menos de tres tentativas '
        'ainda deixa a coleta morrer com frequencia' % mod.TENTATIVAS)
    diz(mod.ESPERA_ENTRE_TENTATIVAS >= 1,
        'ESPERA_ENTRE_TENTATIVAS e %s: repetir no mesmo instante repete a mesma recusa'
        % mod.ESPERA_ENTRE_TENTATIVAS)
    diz('10000' in mod.ERROS_QUE_SE_REPETEM,
        'o codigo medido em 23/11 (10000) saiu da lista dos que se repetem')
    diz(not any(c in ('10020',) for c in mod.ERROS_QUE_SE_REPETEM),
        'a lista dos que se repetem ganhou o codigo de CREDENCIAL: repetir ali e bater '
        'na porta com a chave errada')

    # A FUNCAO E PURA e nao usa rede: e isso que autoriza fabricar mundo.
    diz(vale(erro('erro da API: [10000] System Error'))
        == vale(erro('erro da API: [10000] System Error')),
        'a decisao nao e deterministica')

    print('PORTAO DA REPETICAO DA SHOPEE — ARQUIPELAGO (sem rede)')
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
