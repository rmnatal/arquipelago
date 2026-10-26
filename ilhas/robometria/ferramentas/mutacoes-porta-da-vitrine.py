#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escreve de volta o defeito do item 1 do despacho da Sentinela de 26/10/2026
e exige REPROVACAO.

    python3 ferramentas/mutacoes-porta-da-vitrine.py

O DEFEITO, e ele nao estava no ar: foi pego no caminho. O `electrolux-erb60`
ficou ESGOTADO na Shopee (lido no navegador pela ronda das 15h0xZ de 26/10, com
o rotulo "Esgotado" junto ao titulo e "0 Vendidos"), e era o PRIMEIRO dos cinco
botoes de compra de /quantos-m2-o-robo-aspirador-limpa-por-carga/. Pela 25.2 a
busca sobe e vira o botao, sem esperar ninguem — e o banco desceu o registro do
degrau 3 para o 4.

O QUE ESTAVA PRONTO PARA SAIR ERRADO. A contagem do rodape do bloco de compra
desta pagina conhecia DOIS estados: "tem ficha" e "ainda nao tem link de loja".
Ela contava `empty(afiliado.url)` e chamava o resultado de pendencia. Isso era
VERDADE POR COINCIDENCIA DO BANCO: enquanto nenhum item desta vitrine tinha
descido para o degrau 4, "sem ficha" e "sem porta de compra" eram o mesmo
conjunto. No primeiro dia em que um desceu, a pagina diria

    "Um destes modelos ainda nao tem link de loja"

tres linhas abaixo de servir, para esse mesmo modelo, um botao escrito
"Ver ofertas na Shopee". A R1 e a R2 separavam os tres estados desde 18/09/2026
(item 3 do despacho daquele dia); este arquivo era o que tinha ficado para tras,
e ficou EM SILENCIO porque o terceiro estado ainda nao existia no banco.

POR QUE ESTA BATERIA EXISTE. O conserto e uma trava NOVA sobre um banco JA
consertado — e trava verde em banco consertado nao prova nada. Aqui o mundo que
produz o defeito e escrito de volta, uma mutacao por vez, e a trava tem de morder
em todas. Cada mutacao e um jeito real pelo qual o defeito volta:

  1. o snippet volta a conhecer dois estados (o defeito tal e qual ele seria);
  2. a frase da busca e emudecida (a contagem certa, a prosa calada);
  3. um SEGUNDO item desce para o degrau 4 e a frase fica no molde de um
     (a conta digitada em vez de recontada);
  4. os CINCO descem e a frase insiste no molde com numero
     ("5 destes 5 modelos", a assinatura de contador solto);
  5. o rotulo informativo do portao volta a contar a busca duas vezes
     (o numero errado impresso por quem confere);
  6. o piso da 25.2 e arrancado do item que desceu, e o cartao fica sem porta
     (contra a regua antiga, a de que o bloco de compra nunca fica vazio).

A MUTACAO 6 E CONTRA OUTRA TRAVA de proposito. Ela mede que a regua de 16/09
continua viva ao lado da nova: a nova cobra ACORDO entre a prosa e os cartoes, a
velha cobra que todo cartao tenha saida. Sao perguntas diferentes, e uma passando
nao cobre a outra.
"""

import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PORTAO = 'ferramentas/teste-a2.php'
SNIPPET = 'snippets/robometria-a2.php'
GERADOR = 'ferramentas/gerar-a2.py'

# O A1 ENTROU NESTA BATERIA NA MESMA EXECUCAO, porque o defeito dele NAO era por
# vir: ele estava NO AR. O portao `conferir-frase-de-compra-no-ar.py`, no minuto
# em que deixou de ter lista, achou `/filtro-universal-de-robo-aspirador/`
# servindo QUATRO botoes "Ver ofertas na Shopee" e escrevendo "Nenhuma destas 4
# pecas tem link de loja ainda". Duas paginas, o mesmo defeito, uma trava so.
PORTAO_A1 = 'ferramentas/teste-a1.php'
SNIPPET_A1 = 'snippets/robometria-a1.php'

# Os dois outros itens da vitrine que ainda estao no degrau da ficha. Escritos a
# mao, porque regua que deriva o alvo do banco erra junto com o banco — e
# conferidos contra ele em `_exigir_o_mundo_de_hoje()`, que PARA se o mundo mudar.
OUTRO_DA_VITRINE = 'electrolux-erb61'
VITRINE_INTEIRA = ('electrolux-erb60', 'electrolux-erb61', 'electrolux-erb62',
                   'electrolux-erb80', 'electrolux-erb44')


def _ler(base, nome):
    with io.open(os.path.join(base, 'dados', nome), encoding='utf-8') as f:
        return json.load(f)


def _gravar(base, nome, d):
    with io.open(os.path.join(base, 'dados', nome), 'w', encoding='utf-8') as f:
        f.write(json.dumps(d, ensure_ascii=False, indent=1) + '\n')


def _trocar(base, rel, de, para, quantas=1):
    caminho = os.path.join(base, rel)
    with io.open(caminho, encoding='utf-8') as f:
        texto = f.read()
    if texto.count(de) < 1:
        raise AssertionError('nao achei %r em %s' % (de[:60], rel))
    with io.open(caminho, 'w', encoding='utf-8') as f:
        f.write(texto.replace(de, para, quantas))


def _regerar(base):
    saida = subprocess.run(['python3', os.path.join(base, GERADOR), '--gravar'],
                           capture_output=True, text=True, cwd=base)
    if saida.returncode != 0:
        raise AssertionError('gerar-a2.py falhou depois da mutacao: %s'
                             % saida.stderr[-300:])


def _descer_para_a_busca(base, ids):
    """Tira a ficha dos registros nomeados, como o ERB60 perdeu a dele hoje.

    Nao e um atalho de teste: e exatamente o que a 25.2 manda fazer quando a
    ronda marca a ficha como morta, e e por isso que o mundo desta mutacao e um
    mundo que a fabrica produz sozinha.
    """
    d = _ler(base, 'modelos-robo.json')
    achados = 0
    for r in d['registros']:
        if r['id'] in ids:
            a = r['afiliado']
            if not (a.get('url') or '').strip():
                continue
            a['url'] = ''
            a['url_produto'] = None
            a['degrau'] = 4
            a['motivo_sem_url_produto'] = 'mutacao: a ficha foi marcada morta'
            achados += 1
    if not achados:
        raise AssertionError('nenhum dos ids %r tinha ficha para perder' % (ids,))
    _gravar(base, 'modelos-robo.json', d)
    _regerar(base)


def _exigir_o_mundo_de_hoje():
    """A bateria PARA se o banco deixar de sustentar as mutacoes.

    Tres das seis precisam de um item NA BUSCA (o ERB60 de hoje) e duas precisam
    de um item COM FICHA para descer. No dia em que a vitrine inteira estiver num
    degrau so, metade destas mutacoes fica inerte e imprime verde sem medir — a
    morte por melhora que a `mutacoes-par-sem-modelo.py` desta ilha ja pagou.
    """
    with io.open(os.path.join(RAIZ, 'dados', 'a2-fatos.json'), encoding='utf-8') as f:
        vitrine = json.load(f)['vitrine']
    com_ficha = [i for i in vitrine if (i['afiliado'].get('url') or '').strip()]
    na_busca = [i for i in vitrine if not (i['afiliado'].get('url') or '').strip()
                and (i['afiliado'].get('url_busca') or '').strip()]
    if not na_busca:
        raise SystemExit(
            'PARADA: nenhum cartao da vitrine para na busca hoje, entao as '
            'mutacoes 1, 2 e 5 seriam inertes — a frase que elas atacam nao '
            'existiria na pagina nem antes da mutacao.')
    if len(com_ficha) < 2:
        raise SystemExit(
            'PARADA: a vitrine tem %d cartao(oes) com ficha, e as mutacoes 3 e 4 '
            'precisam de pelo menos 2 para descer.' % len(com_ficha))
    ids = {i['modelo'] for i in vitrine}
    if set(VITRINE_INTEIRA) != ids:
        raise SystemExit(
            'PARADA: a vitrine mudou de composicao. Esta regua conhece %r e o '
            'banco serve %r — a lista a mao envelheceu e tem de ser reescrita '
            'por quem conferir o novo mundo.' % (sorted(VITRINE_INTEIRA), sorted(ids)))


# ------------------------------------------------------------------ MUTACOES
def m1_snippet_volta_a_dois_estados(base):
    _trocar(base, SNIPPET,
            "\t\t$degrau = robometria_casca_degrau_da_porta( $i );\n"
            "\t\tif ( 'sem_saida' === $degrau ) {\n"
            "\t\t\t$sem_link++;\n"
            "\t\t} elseif ( 'ficha' !== $degrau ) {\n"
            "\t\t\t$so_busca++;\n"
            "\t\t}",
            "\t\tif ( empty( $i['afiliado']['url'] ) ) {\n"
            "\t\t\t$sem_link++;\n"
            "\t\t}")


def m2_frase_da_busca_emudece(base):
    _trocar(base, SNIPPET, "\tif ( $so_busca > 0 ) {", "\tif ( false ) {")


def m3_segundo_desce_e_a_frase_fica_no_singular(base):
    _descer_para_a_busca(base, (OUTRO_DA_VITRINE,))
    # A conta passa a dar 2 e a frase insiste no molde de um: e o conserto pela
    # metade mais provavel de todos, porque o molde de hoje esta certo HOJE.
    _trocar(base, SNIPPET,
            "\t\t\t\t( 1 === $so_busca ) ? 'Um destes modelos abre a busca da loja, já filtrada, em vez da ficha de um produto'\n"
            "\t\t\t\t\t: '%s destes modelos abrem a busca da loja, já filtrada, em vez da ficha de um produto',",
            "\t\t\t\t'Um destes modelos abre a busca da loja, já filtrada, em vez da ficha de um produto',")


def m4_todos_descem_e_a_frase_insiste_no_numero(base):
    _descer_para_a_busca(base, VITRINE_INTEIRA)
    _trocar(base, SNIPPET,
            "\t\tif ( $so_busca === $total ) {\n"
            "\t\t\t$busca_frase = ( 1 === $total )",
            "\t\tif ( false ) {\n"
            "\t\t\t$busca_frase = ( 1 === $total )")


def m5_rotulo_do_portao_volta_a_contar_duas_vezes(base):
    _trocar(base, PORTAO,
            "$ficha_a2    = $botoes_a2 - $busca_a2;",
            "$ficha_a2    = $botoes_a2 + $busca_a2 - $busca_a2 - $crua_a2;")
    # A aritmetica velha somava a busca duas vezes e descontava uma: o jeito mais
    # fiel de escrever isso de volta e somar o botao da busca ao total de botoes.
    _trocar(base, PORTAO,
            "$botoes_a2   = substr_count( $retorno, 'class=\"rbm-comprar' );",
            "$botoes_a2   = substr_count( $retorno, 'class=\"rbm-comprar' )\n"
            "\t+ substr_count( $retorno, 'rbm-comprar-busca' );")


def m6_piso_e_arrancado_e_o_cartao_fica_sem_porta(base):
    d = _ler(base, 'modelos-robo.json')
    for r in d['registros']:
        if r['id'] == 'electrolux-erb60':
            r['afiliado']['url_busca'] = ''
            r['afiliado']['url_busca_produto'] = ''
            r['afiliado']['motivo_sem_url_busca'] = 'mutacao: o piso foi arrancado'
    _gravar(base, 'modelos-robo.json', d)
    _regerar(base)


def m7_a1_volta_a_dois_estados(base):
    _trocar(base, SNIPPET_A1,
            "\t\t$degrau = robometria_casca_degrau_da_porta( $i );\n"
            "\t\tif ( 'sem_saida' === $degrau ) {\n"
            "\t\t\t$sem_link++;\n"
            "\t\t} elseif ( 'ficha' !== $degrau ) {\n"
            "\t\t\t$so_busca++;\n"
            "\t\t}",
            "\t\tif ( empty( $i['afiliado']['url'] ) ) {\n"
            "\t\t\t$sem_link++;\n"
            "\t\t}")


def m8_a1_frase_da_busca_emudece(base):
    _trocar(base, SNIPPET_A1, "\tif ( $so_busca > 0 ) {", "\tif ( false ) {")


MUTACOES = [
    ('o snippet volta a conhecer dois estados',
     'o defeito tal e qual ele seria: "nao tem link de loja" tres linhas abaixo do botao',
     m1_snippet_volta_a_dois_estados),
    ('a frase da busca e emudecida',
     'a contagem certa e a prosa calada: o leitor clica sem saber onde cai',
     m2_frase_da_busca_emudece),
    ('um SEGUNDO item desce e a frase fica no molde de um',
     'a conta digitada em vez de recontada — o molde de hoje esta certo so hoje',
     m3_segundo_desce_e_a_frase_fica_no_singular),
    ('os CINCO descem e a frase insiste no molde com numero',
     '"5 destes 5 modelos" e a assinatura de contador solto (secao 15)',
     m4_todos_descem_e_a_frase_insiste_no_numero),
    ('o rotulo do portao volta a contar a busca duas vezes',
     'numero errado impresso por quem confere e o pior lugar para ele morar',
     m5_rotulo_do_portao_volta_a_contar_duas_vezes),
    ('o piso da 25.2 e arrancado e o cartao fica sem porta',
     'contra a regua de 16/09: o bloco de compra nunca fica vazio',
     m6_piso_e_arrancado_e_o_cartao_fica_sem_porta),
    ('o A1 volta a conhecer dois estados',
     'o defeito que ESTAVA NO AR: quatro botoes e a pagina negando os quatro',
     m7_a1_volta_a_dois_estados, PORTAO_A1),
    ('a frase da busca do A1 e emudecida',
     'quatro botoes de busca e a pagina calada sobre onde eles caem',
     m8_a1_frase_da_busca_emudece, PORTAO_A1),
]


def main():
    _exigir_o_mundo_de_hoje()
    print('Robometria — a porta de compra da vitrine do A2 (despacho de 26/10, item 1)\n')
    reprovadas = 0
    for linha in MUTACOES:
        titulo, porque, mutar = linha[0], linha[1], linha[2]
        portao = linha[3] if len(linha) > 3 else PORTAO
        base = tempfile.mkdtemp(prefix='rbm-porta-')
        alvo = os.path.join(base, 'ilha')
        shutil.copytree(RAIZ, alvo)
        try:
            mutar(alvo)
        except AssertionError as e:
            print('  INERTE %-58s %s' % (titulo[:58], e))
            shutil.rmtree(base, ignore_errors=True)
            continue
        saida = subprocess.run(['php', os.path.join(alvo, portao), alvo],
                               capture_output=True, text=True, cwd=alvo)
        falhou = saida.returncode != 0
        quantas = saida.stdout.count('  FALHA')
        print('  %s %-58s %s' % ('ok    ' if falhou else 'PASSOU', titulo[:58],
                                 ('%d falha(s) em %s' % (quantas, os.path.basename(portao)))
                                 if falhou else 'a trava NAO pegou'))
        if not falhou:
            print('         %s' % porque)
        reprovadas += 1 if falhou else 0
        shutil.rmtree(base, ignore_errors=True)

    print('\n%d de %d mutacoes reprovadas pela bancada.' % (reprovadas, len(MUTACOES)))
    return 0 if reprovadas == len(MUTACOES) else 1


if __name__ == '__main__':
    sys.exit(main())
