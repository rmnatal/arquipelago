#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra de proposito a procedencia da AREA POR CARGA no cartao do A2 e exige
REPROVACAO.

    python3 ferramentas/mutacoes-a2-procedencia.py

POR QUE ESTE ARQUIVO EXISTE, E O QUE ELE TEM DE DIFERENTE DO IRMAO
------------------------------------------------------------------
"A PROVA DE QUE UMA TRAVA REPROVA E PARTE DO BLOCO" (secao 8 do ARQUIPELAGO.md).
A secao 9 do ferramentas/teste-a2.php nasceu VERDE — foi escrita depois da
correcao, entao passar nao prova nada.

O irmao deste arquivo (mutacoes-procedencia.py, da R2) teve um trabalho que aqui
NAO e preciso, e a diferenca vale ser dita porque ela e o achado do bloco. La, a
mutacao "a atribuicao volta a ser digitada" era INERTE com o banco de hoje: as
onze fontes de Pa sao todas do degrau 3, entao o literal 'pelo fabricante' e
exatamente o que o degrau devolve, e a mutacao precisava PRODUZIR o mundo em que
o defeito aparece. Aqui esse mundo ja e o mundo: os cinco modelos que declaram
area por carga declaram pela fonte f-loja, degrau 4, loja oficial da marca. A
mutacao 7 volta o codigo para o que estava no ar ate 12/09/2026 e a bancada
reprova SEM tocar no banco — porque a frase que estava publicada era falsa.

O que continua exigindo o banco mutado sao as duas travas LATENTES, e elas sao
justamente as que o bloco escreveu de olho no amanha: a atribuicao do SEGUNDO
numero do cartao (a autonomia, que hoje vem da mesma fonte nos cinco) e o titulo
da secao quando os degraus se misturam. Trava latente sem mutacao que produza o
mundo dela e trava nao medida — foi assim que a R2 quase deixou a sua passar.

Cada mutacao e uma copia da ilha inteira num diretorio temporario, com UMA edicao
cirurgica, e a bancada tem que sair com codigo diferente de zero.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

A2 = 'snippets/robometria-a2.php'
GERADOR = 'ferramentas/gerar-a2.py'
ESQUEMA = 'dados/esquema-banco.json'
FATOS = 'dados/a2-fatos.json'
MODELOS = 'dados/modelos-robo.json'
# A BANCADA DESTE ARQUIVO TEM DOIS PORTOES, e o segundo entrou porque uma mutacao
# passou sem ele: "o degrau 4 fica sem ressalva na escada" nao e defeito da
# pagina, e do BANCO, e quem a reprova e validar-banco.py — que ja tinha a trava
# desde 11/09/2026 e simplesmente nao estava sendo chamado aqui. Mutacao no banco
# julgada so pelo teste da pagina mede metade do mundo.
TESTES = ('ferramentas/teste-a2.php', 'ferramentas/validar-banco.py')

LINHA_FONTE = """\t\t$html .= '<span class="rbm-vitrine-fonte">'
\t\t\t. esc_html( 'Como sabemos — ' . $p['rotulo'] . ', verificado em '
\t\t\t\t. robometria_a2_data( $p['verificado_em'] ) )
\t\t\t. ( empty( $p['url'] ) ? '' : ' · ' . ( function_exists( 'robometria_casca_fonte_link' )
\t\t\t\t? robometria_casca_fonte_link( $p['url'] ) : '' ) )
\t\t\t. '</span>';
"""

BLOCO_ACAO = """\t\t$html .= '<span class="rbm-vitrine-acao">'
\t\t\t. ( function_exists( 'robometria_casca_porta_de_compra' )
\t\t\t\t? robometria_casca_porta_de_compra( $i )
\t\t\t\t: '<span class="rbm-sem-loja">Link de loja em breve</span>' )
\t\t\t. '</span>';
"""

BLOCO_TAG = """\t\tif ( ! empty( $p['ressalva'] ) ) {
\t\t\t$html .= '<span class="rbm-tag">' . esc_html( $p['ressalva'] ) . '</span>';
\t\t}
"""

MOLDE_ATRIBUICAO = """\t\t$porque = sprintf( 'Área por carga declarada %s', $p['quem_declara'] );
"""

# O molde EXATO que estava no ar ate 12/09/2026.
MOLDE_DIGITADO = """\t\t$porque = sprintf(
\t\t\t'O fabricante declara %s m² por carga',
\t\t\trobometria_a2_n( $i['cobertura_m2'] )
\t\t);
"""

TITULO_DERIVADO = """\t$html  = '<div class="rbm-secao rbm-compra"><h2>'
\t\t. esc_html( $atr
\t\t\t? sprintf( 'Os modelos cuja área por carga é declarada %s', $atr )
\t\t\t: 'Os modelos cuja área por carga é declarada, e por quem' )
\t\t. '</h2>';
"""

TITULO_DIGITADO = """\t$html  = '<div class="rbm-secao rbm-compra"><h2>Os modelos cujo fabricante publica o número</h2>';
"""

CONJUNTO_EXIGE_ACORDO = """    origens = {i["procedencia"]["origem"] for i in itens}
    if len(origens) != 1:
        return None
    return itens[0]["procedencia"]["quem_declara"]
"""

CONJUNTO_PELO_PRIMEIRO = """    return itens[0]["procedencia"]["quem_declara"]
"""


def trocas(arquivo, pares):
    """Substituicoes exatas, cada uma obrigada a acertar um alvo unico.

    Exigir unicidade nao e preciosismo: mutacao que nao encontra o alvo edita
    NADA, o teste passa, e um teste verde por mutacao que nao aconteceu e a mesma
    ilusao que este arquivo existe para desfazer.
    """
    def aplicar(base):
        caminho = os.path.join(base, arquivo)
        with open(caminho, encoding='utf-8') as f:
            corpo = f.read()
        for velho, novo in pares:
            achados = corpo.count(velho)
            if achados != 1:
                raise AssertionError(
                    'alvo da mutacao nao esta unico em %s: %d ocorrencia(s)'
                    % (arquivo, achados))
            corpo = corpo.replace(velho, novo)
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(corpo)
    return aplicar


def troca(arquivo, velho, novo):
    return trocas(arquivo, [(velho, novo)])


def editar_json(arquivo, funcao):
    def aplicar(base):
        caminho = os.path.join(base, arquivo)
        with open(caminho, encoding='utf-8') as f:
            doc = json.load(f)
        funcao(doc)
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(doc, f, ensure_ascii=False, indent=2)
            f.write('\n')
    return aplicar


def regerar(base):
    """Refaz dados/a2-fatos.json a partir do banco (mutado) daquela copia.

    E o terceiro passo que quase ficou de fora na R2: sem ele a mutacao no banco
    reprova, mas pelo motivo ERRADO — banco e arquivo servido ficam divergentes e
    outra trava dispara primeiro, deixando a trava do bloco sem ser exercitada.
    """
    subprocess.run([sys.executable, os.path.join(base, 'ferramentas', 'gerar-a2.py'),
                    '--gravar'], cwd=base, capture_output=True, text=True, check=True)


def degrau(doc, nivel):
    for n in doc['escada_de_fontes']['niveis']:
        if n['nivel'] == nivel:
            return n
    raise AssertionError('degrau %d nao existe' % nivel)


def _sem_na_tela(doc):
    del degrau(doc, 4)['na_tela']


def _ressalva_nula(doc):
    degrau(doc, 4)['na_tela']['ressalva'] = None


def _rotulo_divergente(doc):
    degrau(doc, 4)['na_tela']['rotulo'] = 'manual do fabricante'


def _atribuicao_inflada(doc):
    degrau(doc, 4)['na_tela']['quem_declara'] = 'pelo fabricante'


def _tabela_divergente(doc):
    doc['rotulos_de_origem']['varejo-oficial-da-marca']['ressalva'] = None


def _cobertura_por_anuncio(registros_doc):
    """A area de UM modelo passando a vir de anuncio de marketplace (degrau 6).

    Nao e ficcao: o degrau existe na escada, ja tem `existe_hoje: true` nesta
    ilha, e basta alguem transcrever um numero de anuncio. E o estado em que a
    lista deixa de ter um publicador so — que e exatamente quando o titulo da
    secao nao pode mais atribuir os cinco a ninguem.
    """
    for r in registros_doc['registros']:
        if r['id'] == 'electrolux-erb44':
            r['fontes']['f-loja'] = dict(r['fontes']['f-loja'])
            r['fontes']['f-loja']['nivel'] = 6
            r['fontes']['f-loja']['origem'] = 'marketplace-anuncio'
            return
    raise AssertionError('electrolux-erb44 nao esta no banco')


def _autonomia_por_anuncio(registros_doc):
    """A AUTONOMIA de um modelo entrando por outro degrau que a area dele.

    Os cinco modelos declaram os dois numeros pela mesma fonte hoje, e e por isso
    que a trava do segundo numero e latente. Aqui ela deixa de ser: o ERB60 passa
    a ter a autonomia transcrita de anuncio e a area continuando na loja oficial.
    """
    for r in registros_doc['registros']:
        if r['id'] == 'electrolux-erb60':
            r['fontes']['f-anuncio'] = {
                'nivel': 6,
                'origem': 'marketplace-anuncio',
                'publicador': 'Marketplace (anuncio)',
                'titulo_na_fonte': 'anuncio de teste da mutacao',
                'url': 'https://exemplo.invalido/anuncio-de-teste',
                'canal_de_coleta': 'mutacao deliberada',
                'verificado_em': '2026-09-12',
            }
            r['autonomia_min_declarada']['fonte'] = 'f-anuncio'
            return
    raise AssertionError('electrolux-erb60 nao esta no banco')


def _autonomia_presumida(base):
    """A trava LATENTE do segundo numero, posta diante do mundo em que morde.

    Tres passos: a autonomia de um modelo passa a vir de outro degrau, o arquivo
    de dados e regerado, e o snippet volta a presumir que os dois numeros da
    frase tem a mesma origem. Sem o primeiro e o segundo passo esta mutacao nao
    muda um byte da tela.
    """
    editar_json(MODELOS, _autonomia_por_anuncio)(base)
    regerar(base)
    troca(A2, "empty( $i['mesma_origem'] )", "false")(base)


def _conjunto_pelo_primeiro(base):
    """O titulo atribuindo os cinco ao degrau do PRIMEIRO, com degraus misturados.

    Mesma familia da anterior: a regra "so nomeia quando todos concordam" nao
    muda nada enquanto todos concordarem. Aqui um dos cinco passa a vir de
    anuncio, e o titulo continuaria dizendo "declarada pela loja oficial da
    marca" sobre uma lista em que isso e falso para um item.
    """
    editar_json(MODELOS, _cobertura_por_anuncio)(base)
    troca(GERADOR, CONJUNTO_EXIGE_ACORDO, CONJUNTO_PELO_PRIMEIRO)(base)
    regerar(base)


MUTACOES = [
    (
        'a linha de procedencia some do cartao',
        'o numero que faz o modelo entrar na lista volta a ser publicado sem endereco e sem data',
        troca(A2, LINHA_FONTE, ''),
    ),
    (
        'a procedencia vem ANTES da porta de compra',
        'e a cicatriz de 10/09/2026: o link de fonte volta a ser a unica porta clicavel do cartao',
        trocas(A2, [(BLOCO_ACAO, ''), (LINHA_FONTE, LINHA_FONTE + BLOCO_ACAO)]),
    ),
    (
        'a data sai da linha de procedencia',
        'procedencia sem data nao e conferivel, e a secao 5.4 pede a data dentro da propria frase',
        troca(A2,
              "'Como sabemos — ' . $p['rotulo'] . ', verificado em '\n\t\t\t\t. robometria_a2_data( $p['verificado_em'] ) )",
              "'Como sabemos — ' . $p['rotulo'] )"),
    ),
    (
        'o endereco da fonte some do cartao',
        'a pagina diz "para voce conferir, e nao para voce acreditar" — sem endereco nao da para conferir',
        troca(A2,
              "\t\t\t. ( empty( $p['url'] ) ? '' : ' · ' . ( function_exists( 'robometria_casca_fonte_link' )\n\t\t\t\t? robometria_casca_fonte_link( $p['url'] ) : '' ) )\n",
              ''),
    ),
    (
        'a ressalva do degrau some do cartao',
        '"confira a embalagem" e o elo fraco dito com todas as letras, no lugar onde o leitor decide se compra',
        troca(A2, BLOCO_TAG, ''),
    ),
    (
        'a ressalva sai DEPOIS do botao de compra',
        'ressalva que aparece depois da decisao nao e ressalva, e nota de rodape',
        trocas(A2, [(BLOCO_TAG, ''), (BLOCO_ACAO, BLOCO_ACAO + BLOCO_TAG)]),
    ),
    (
        'o cartao volta ao molde que estava no ar: "O fabricante declara"',
        'E O DEFEITO INTEIRO, e aqui ele nao precisa de banco mutado: a loja oficial declarou, e a pagina credita o fabricante',
        troca(A2, MOLDE_ATRIBUICAO, MOLDE_DIGITADO),
    ),
    (
        'o titulo da secao volta a ser digitado',
        'o titulo fala dos cinco de uma vez, e dizia "cujo fabricante publica o numero" sobre cinco numeros que a loja publicou',
        troca(A2, TITULO_DERIVADO, TITULO_DIGITADO),
    ),
    (
        'a autonomia herda calada a atribuicao da area, e uma autonomia entra por anuncio',
        'trava LATENTE: o cartao publica dois numeros na mesma frase e passaria a creditar os dois a quem declarou so um',
        _autonomia_presumida,
    ),
    (
        'o titulo atribui a lista ao degrau do primeiro item, com degraus misturados',
        'trava LATENTE: uma frase so nao pode atribuir a lista inteira a um publicador sem mentir sobre parte dela',
        _conjunto_pelo_primeiro,
    ),
    (
        'o degrau 4 perde o na_tela na escada',
        'degrau mudo faz a tela imprimir o apelido de campo cru, e so se descobre no ar',
        editar_json(ESQUEMA, _sem_na_tela),
    ),
    (
        'o degrau 4 fica sem ressalva na escada',
        'silencio nunca promove: degrau de varejo sem ressalva publica um rigor que a ilha nao tem',
        editar_json(ESQUEMA, _ressalva_nula),
    ),
    (
        'o degrau 4 se renomeia "manual do fabricante" na escada',
        'a ilha nao tem nivel 2 nenhum; chamar loja de manual e inflar o proprio nivel de fonte',
        editar_json(ESQUEMA, _rotulo_divergente),
    ),
    (
        'o degrau 4 passa a se atribuir ao fabricante na escada',
        'o mesmo defeito do molde digitado, entrando pela outra porta — a que o snippet obedece',
        editar_json(ESQUEMA, _atribuicao_inflada),
    ),
    (
        'a tabela que viaja para o site diverge da escada',
        'duas copias da mesma escada, e a que o site consome perdendo a ressalva sem ninguem ver',
        editar_json(FATOS, _tabela_divergente),
    ),
]


def main():
    reprovadas = 0
    passaram = []

    print('Mutacoes deliberadas na procedencia da area por carga (A2 1.2.0)'
          ' — cada uma TEM que reprovar\n')

    for nome, porque, aplicar in MUTACOES:
        with tempfile.TemporaryDirectory() as tmp:
            base = os.path.join(tmp, 'ilha')
            shutil.copytree(RAIZ, base)
            try:
                aplicar(base)
            except (AssertionError, subprocess.CalledProcessError) as erro:
                print('  ERRO   %-62s %s' % (nome, erro))
                passaram.append(nome)
                continue

            falhas = []
            pegou_em = []
            for teste in TESTES:
                comando = ([sys.executable] if teste.endswith('.py') else ['php'])
                saida = subprocess.run(
                    comando + [os.path.join(base, teste), base],
                    capture_output=True, text=True)
                if saida.returncode != 0:
                    pegou_em.append(os.path.basename(teste))
                    # "FALHA" e o prefixo da bancada em PHP; "x " o do
                    # validar-banco.py. Ler so um dos dois daria uma mutacao
                    # reprovada sem nenhuma linha explicando por que.
                    falhas += [l.strip() for l in saida.stdout.splitlines()
                               if l.strip().startswith(('FALHA', 'x '))]

            if not pegou_em:
                print('  PASSOU %-62s <- a trava NAO pegou' % nome)
                print('         (%s)' % porque)
                passaram.append(nome)
                continue

            print('  ok     %-62s %d falha(s)' % (nome, len(falhas)))
            for linha in falhas[:2]:
                print('         %s' % linha[:112])
            reprovadas += 1

    print('\n%d de %d mutacoes reprovadas pela bancada.' % (reprovadas, len(MUTACOES)))
    if passaram:
        print('MUTACOES QUE PASSARAM (trava faltando):')
        for nome in passaram:
            print('  - %s' % nome)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
