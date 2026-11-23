#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PORTAO DA CONTA DE ENTRADA DO CLUSTER — nasceu em 23/11/2026. Sem rede.

    python3 ferramentas/teste-cluster-de-entrada.py

O DEFEITO QUE ELE EXISTE PARA FECHAR ESTAVA NO AR E A REGUA DESTA ILHA ESTAVA
VERDE. Medido na ronda tecnica de 23/11/2026, no HTML servido das 11 URLs e
dentro do `<main>`: `/veiculos/moto-eletrica/` — a consulta de 823 mil
buscas/mes, a de MAIOR volume do nicho — recebia **ZERO** link de entrada de
miolo, contra os 2 que a 16.4(f) exige. As outras dez recebiam de 3 a 10. A mae
`/veiculos/` servia 6 links de miolo e nenhum era o dela; as duas irmas listavam
uma a outra e nunca a moto; e a moto listava as duas — o grafo de UM LADO SO que
a 16.9(a) manda nao acontecer.

A REGUA VELHA NAO ERA CEGA: ELA CONTAVA A COISA ERRADA. O veredito da leitura de
18/11 dizia, com estas palavras, *"zero pagina orfa na direcao de ENTRADA (as 11
recebem 10 links de entrada cada)"* — e 10 e o MENU mais o RODAPE, que a casca
desta ilha serve em TODA pagina por construcao. **Contagem de entrada que inclui
a navegacao global fica verde em qualquer mundo possivel**, inclusive num site em
que uma pagina nao recebe um unico link de corpo. E a familia do "resumo verde
nao e entrega" da 20.4, aplicada a link interno: a navegacao e um numero que
sempre esta la, e por isso ele nao mede nada.

A CAUSA DO DEFEITO ERA DE MECANISMO E E A MESMA FONTE DA 25.2-c: a listagem de
filhas da mae e o bloco "Veja tambem" nasciam de `rdm_produto_paginas_prontas()`,
a lista de quem TEM VITRINE, e a pagina degradada pelo piso da 30.2 esta ausente
dela POR DEFINICAO. Aquela fonte ja havia tirado desta mesma pagina a CABECA
(consertado em 18/11) e a SAIDA DE COMPRA (19/11). O cluster era o terceiro
andar.

A REGUA VELHA E A NOVA DISCORDAM NO MUNDO MEDIDO, e e isso que faz deste portao
uma medicao em vez de uma intencao (secao 8, e a mesma disciplina do
`teste-piso-na-tela.py`): no mundo de 23/11 a velha APROVA — porque conta 10
entradas de navegacao — e a nova REPROVA, porque conta ZERO de miolo.

O QUE ELE NAO MEDE, e a linha esta aqui para ninguem ler verde a mais: a
EXTRACAO do miolo (`miolo_da_pagina`) e do conjunto de caminhos
(`caminhos_internos`) e exercitada aqui sobre HTML fabricado, mas o grafo de
verdade so existe no ar — quem o monta e `conferir-produto-no-ar.py`, que roda
com `--no-ar`. A funcao pura e a DECISAO; a leitura e do portao de rede.
"""

import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))

MAE = "/veiculos/"
PATINETE = "/veiculos/patinete-eletrico/"
BICICLETA = "/veiculos/bicicleta-eletrica/"
MOTO = "/veiculos/moto-eletrica/"
HOME = "/"
F2 = "/autonomia-patinete-eletrico/"

# O MENU E O RODAPE DESTA CASCA, medidos no HTML servido em 23/11/2026: 5 links
# em cada um, em TODA pagina. Eles estao aqui para a regua VELHA poder conta-los,
# que e a unica coisa que eles fazem numa conta de cluster.
NAVEGACAO_GLOBAL = (HOME, MAE, F2, "/peso-maximo-patinete-eletrico/", "/sobre/")


def _portao():
    """Carrega o portao de ar SO para usar as funcoes puras dele.

    A regra mora no dono do arquivo e e USADA por quem precisa, nunca copiada
    (20.7): copia-la aqui faria as duas metades errarem juntas, que e a cicatriz
    do 'teste que mede a si mesmo' da secao 8.
    """
    caminho = os.path.join(AQUI, 'conferir-produto-no-ar.py')
    spec = importlib.util.spec_from_file_location('conferir_produto_no_ar', caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def regua_velha(filhas, quem_aponta_no_documento):
    """A REGUA DE ANTES DO CONSERTO, reescrita aqui de proposito e SO aqui.

    Ela conta `href` no DOCUMENTO INTEIRO — menu e rodape dentro — e aprova quem
    tiver 2 ou mais. Era literalmente o que a leitura de 18/11 fazia quando
    escreveu "as 11 recebem 10 links de entrada cada". Ela existe para uma coisa
    so: provar que a nova DISCORDA dela no mundo que foi medido. Portao que nao
    mostra a discordancia nao prova que o conserto conserta — prova que alguem
    escreveu codigo novo.
    """
    falhas = []
    for filha in sorted(filhas):
        if len(set(quem_aponta_no_documento.get(filha, set())) - {filha}) < 2:
            falhas.append('%s recebe menos de 2 links' % filha)
    return falhas


def com_navegacao(quem_aponta_de_miolo, paginas):
    """O MESMO mundo visto pela regua velha: cada pagina recebe, alem do miolo, o
    link do menu e do rodape de TODAS as paginas do site."""
    cheio = {k: set(v) for k, v in quem_aponta_de_miolo.items()}
    for alvo in NAVEGACAO_GLOBAL:
        cheio.setdefault(alvo, set()).update(paginas)
    # E o menu desta casca lista a secao mae e as ferramentas, nao as filhas de
    # produto; a 18/11 contou 10 entradas em TODAS as 11, entao o mundo da regua
    # velha e o mundo em que toda pagina recebe a navegacao.
    for alvo in paginas:
        cheio.setdefault(alvo, set()).update(paginas)
    return cheio


def main():
    mod = _portao()
    veredito = mod.veredito_do_cluster_de_entrada
    afirmacoes = 0
    falhas = []
    notas = []

    def diz(ok, msg):
        nonlocal afirmacoes
        afirmacoes += 1
        if not ok:
            falhas.append(msg)

    # (filhas no ar, quem aponta no MIOLO, reprova?, nome do mundo)
    MUNDOS = [
        ([PATINETE, BICICLETA, MOTO],
         {PATINETE: {MAE, BICICLETA, MOTO}, BICICLETA: {MAE, PATINETE, MOTO}, MOTO: set()},
         True,
         'O MUNDO MEDIDO EM 23/11/2026: a moto com ZERO entrada de miolo e as duas irmas '
         'servidas pela mae'),
        ([PATINETE, BICICLETA, MOTO],
         {PATINETE: {MAE, BICICLETA, MOTO}, BICICLETA: {MAE, PATINETE, MOTO},
          MOTO: {MAE, PATINETE, BICICLETA}},
         False,
         'o mundo consertado: a mae lista as tres e o grafo de irmas fecha nas duas direcoes'),
        ([PATINETE, BICICLETA, MOTO],
         {PATINETE: {MAE, BICICLETA}, BICICLETA: {MAE, PATINETE}, MOTO: {PATINETE, BICICLETA}},
         True,
         'o grafo de irmas fecha e a MAE nao lista a moto: a 16.4(a) pede a mae explicitamente'),
        ([PATINETE, BICICLETA, MOTO],
         {PATINETE: {MAE, BICICLETA}, BICICLETA: {MAE, PATINETE}, MOTO: {MAE}},
         True,
         'a moto recebe SO a mae: 1 link contra os 2 da 16.4(f), e e o mundo da sexta filha '
         'da clubedomosaico em 12/10'),
        ([PATINETE],
         {PATINETE: {MAE, HOME}},
         False,
         'UMA filha no ar: ela recebe a mae e a home, e nao ha irma de quem cobrar'),
        ([PATINETE],
         {PATINETE: {MAE}},
         True,
         'UMA filha no ar recebendo SO a mae: a 16.4(f) pede 2 links, e ela vale tambem para '
         'quem nao tem irma'),
        ([],
         {},
         True,
         'ZERO filha achada no ar: ou a secao esta sem filha (16.5) ou o portao esta cego'),
        ([PATINETE, BICICLETA, MOTO],
         {PATINETE: {MAE, BICICLETA, MOTO}, BICICLETA: {MAE, PATINETE, MOTO},
          MOTO: {MAE, MOTO}},
         True,
         'a moto aponta para SI MESMA e recebe a mae: ancora na propria pagina nao e link de '
         'entrada'),
    ]

    for filhas, aponta, deve_reprovar, nome in MUNDOS:
        try:
            saida = veredito(MAE, filhas, aponta)
        except Exception as e:                                 # noqa: BLE001
            diz(False, 'MUNDO %s: estourou %s' % (nome, type(e).__name__))
            continue
        diz(isinstance(saida, list), 'MUNDO %s: a funcao nao devolveu lista' % nome)
        diz(bool(saida) == deve_reprovar,
            'MUNDO %s: esperava %s e a funcao disse %s (%r)'
            % (nome, 'REPROVAR' if deve_reprovar else 'APROVAR',
               'REPROVAR' if saida else 'APROVAR', saida))
        # TODA FALHA DIZ O CONSERTO EM PALAVRAS, nunca so o numero (20.4).
        for linha in saida:
            diz(len(linha.strip()) > 30 and not linha.strip().startswith('('),
                'MUNDO %s: a falha %r nao diz em palavras o que esta errado' % (nome, linha))

    # A DISCORDANCIA COM A REGUA VELHA, no mundo medido e so nele.
    filhas, aponta, _d, _n = MUNDOS[0]
    paginas = set(filhas) | {MAE, HOME, F2}
    velha = regua_velha(filhas, com_navegacao(aponta, paginas))
    nova = veredito(MAE, filhas, aponta)
    diz(not velha and bool(nova),
        'A REGUA VELHA TINHA DE APROVAR O MUNDO DE 23/11 E A NOVA DE REPROVAR, e agora elas '
        'dizem velha=%r nova=%r — sem essa discordancia este portao nao prova conserto nenhum'
        % (velha, nova))
    notas.append('mundo medido em 23/11 (moto com 0 entrada de miolo): a regua velha, que conta '
                 'menu e rodape, APROVA com 10 entradas; a nova REPROVA com 0 — a discordancia '
                 'vale a frase "zero pagina orfa na direcao de ENTRADA" da leitura de 18/11')

    # E ELA CONCORDA COM A VELHA NO MUNDO CONSERTADO: conserto que reprova tudo
    # nao e aperto, e pessimismo (a trava da secao 8).
    filhas_ok, aponta_ok, _d, _n = MUNDOS[1]
    diz(not regua_velha(filhas_ok, com_navegacao(aponta_ok, paginas))
        and not veredito(MAE, filhas_ok, aponta_ok),
        'no mundo CONSERTADO as duas reguas tem de aprovar, e elas dizem velha=%r nova=%r'
        % (regua_velha(filhas_ok, com_navegacao(aponta_ok, paginas)),
           veredito(MAE, filhas_ok, aponta_ok)))

    # A FUNCAO E PURA: duas chamadas iguais dao a mesma resposta, e ela nao toca
    # arquivo nenhum. Afirmacao barata, e ela e o que autoriza fabricar mundo.
    diz(veredito(MAE, filhas, aponta) == veredito(MAE, filhas, aponta),
        'o veredito do cluster nao e deterministico')
    # E ELA NAO MEXE NO QUE RECEBE: dicionario de entrada alterado faria a
    # segunda chamada medir outro mundo, e o portao de rede a chama uma vez.
    copia = {k: set(v) for k, v in aponta.items()}
    veredito(MAE, filhas, aponta)
    diz(copia == {k: set(v) for k, v in aponta.items()},
        'o veredito MEXEU no mapa de quem aponta que recebeu')

    # =====================================================================
    # A EXTRACAO: o `<main>` e os caminhos internos, sobre HTML fabricado
    # =====================================================================
    miolo_de = mod.miolo_da_pagina
    caminhos_de = mod.caminhos_internos

    PAGINA = (
        '<html><body>'
        '<header class="rdm-cabecalho"><a href="/">Rodametria</a>'
        '<a href="/veiculos/">Veículos</a><a href="/veiculos/moto-eletrica/">Moto</a></header>'
        '<main id="x"><h1>Patinete</h1>'
        '<a href="/veiculos/">todos os veículos elétricos</a>'
        '<a href="https://rodametria.com.br/veiculos/bicicleta-eletrica/">bicicleta</a>'
        '<a href="#comprar">ver preços</a>'
        '<a href="/veiculos/patinete-eletrico/?v=1#comprar">o bloco de compra</a>'
        '<a href="https://shopee.com.br/x">Ver na Shopee</a>'
        '<script>var a = \'<a href="/veiculos/moto-eletrica/">\';</script>'
        '</main>'
        '<footer class="rdm-rodape"><a href="/veiculos/moto-eletrica/">Moto</a>'
        '<a href="/sobre/">Sobre</a></footer>'
        '</body></html>')

    miolo = miolo_de(PAGINA)
    diz('rdm-cabecalho' not in miolo and 'rdm-rodape' not in miolo,
        'o miolo extraido ainda traz o cabecalho ou o rodape da casca: a navegacao global '
        'voltaria a contar, que e o defeito inteiro')
    diz('<script' not in miolo,
        'o miolo extraido traz `<script>`: href dentro de JS nao e link de entrada')

    achados = caminhos_de(miolo)
    diz(achados == {MAE, BICICLETA, PATINETE},
        'os caminhos internos do miolo fabricado tinham de ser a mae, a bicicleta e a propria '
        'pagina (que quem chama descarta), e vieram %r' % sorted(achados))
    diz(MOTO not in achados,
        'o caminho da moto entrou pela extracao: ele so aparece no rodape e dentro de um '
        '`<script>` desta pagina fabricada, e nenhum dos dois e link de miolo')
    diz(not any('shopee' in c for c in achados),
        'link externo entrou na conta de link INTERNO')

    SEM_MAIN = '<html><body><header class="rdm-cabecalho"><a href="/">x</a></header>' \
               '<div><a href="/veiculos/">y</a></div></body></html>'
    diz(miolo_de(SEM_MAIN) == '',
        'pagina SEM `<main>` devolveu miolo: cair no `<body>` inteiro poria o menu de volta '
        'na conta, e pagina sem miolo e pagina NAO MEDIDA (20.8)')

    print('PORTAO DA CONTA DE ENTRADA DO CLUSTER — RODAMETRIA (sem rede)')
    for n in notas:
        print('  . ' + n)
    for f in falhas:
        print('FALHA: ' + f)
    print('\n%d mundo(s) fabricado(s) e %d afirmacao(oes), %d falha(s).'
          % (len(MUNDOS) + 2, afirmacoes, len(falhas)))
    print('APROVADO' if not falhas else 'REPROVADO')
    return 1 if falhas else 0


if __name__ == '__main__':
    sys.exit(main())
