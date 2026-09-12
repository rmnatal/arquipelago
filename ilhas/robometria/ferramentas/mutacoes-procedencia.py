#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra de proposito a procedencia do Pa na R2 e exige REPROVACAO.

    python3 ferramentas/mutacoes-procedencia.py

POR QUE ESTE ARQUIVO EXISTE
---------------------------
"A PROVA DE QUE UMA TRAVA REPROVA E PARTE DO BLOCO" (secao 8 do ARQUIPELAGO.md).
As secoes 16 e 17 do ferramentas/teste-r2.php nasceram VERDES — as duas foram escritas depois da
correcao que medem, entao passar nao prova nada. Nesta ilha cinco travas ja passaram
verdes medindo a si mesmas.

Cada mutacao e uma copia da ilha inteira num diretorio temporario, com UMA
edicao cirurgica, e a bancada tem que sair com codigo diferente de zero.

O QUE UMA MUTACAO PRECISA SER AQUI. As duas primeiras familias sao faceis (o
markup some, a ordem inverte). A terceira e a que importa e a que quase saiu
INERTE: "a atribuicao volta a ser digitada no molde" nao muda um byte da tela
enquanto as onze fontes de Pa do banco forem todas do mesmo degrau — o literal
'pelo fabricante' e, hoje, exatamente o que o degrau devolve. Para ela morder, a
mutacao tem que produzir o mundo em que o defeito aparece: um Pa entrando por
loja oficial da marca, que e um estado que o banco alcanca no dia em que alguem
transcrever um numero de la. So assim se ve a pagina emprestando a autoridade do
fabricante a quem apenas transcreveu — que e o defeito de verdade, e nao a
mudanca de uma string.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

R2 = 'snippets/robometria-r2.php'
ESQUEMA = 'dados/esquema-banco.json'
RESPOSTAS = 'dados/r2-respostas.json'
MODELOS = 'dados/modelos-robo.json'
REFERENCIA = 'ferramentas/cobertura-r2.py'
TESTES = ('ferramentas/teste-r2.php',)

LINHA_FONTE = """\t\t$html .= '<span class="rbm-vitrine-fonte">'
\t\t\t. esc_html( 'Como sabemos — ' . $p['rotulo'] . ', verificado em '
\t\t\t\t. robometria_r2_data( $p['verificado_em'] ) )
\t\t\t. ( empty( $p['url'] ) ? '' : ' · ' . ( function_exists( 'robometria_casca_fonte_link' )
\t\t\t\t? robometria_casca_fonte_link( $p['url'] ) : '' ) )
\t\t\t. '</span>';
"""

BLOCO_ACAO = """\t\t$html .= '<span class="rbm-vitrine-acao">'
\t\t\t. ( function_exists( 'robometria_casca_porta_de_compra' )
\t\t\t\t? robometria_casca_porta_de_compra( $m )
\t\t\t\t: '<span class="rbm-sem-loja">Link de loja em breve</span>' )
\t\t\t. '</span>';
"""

BLOCO_TAG = """\t\tif ( ! empty( $p['ressalva'] ) ) {
\t\t\t$html .= '<span class="rbm-tag">' . esc_html( $p['ressalva'] ) . '</span>';
\t\t}
"""


def trocas(arquivo, pares):
    """Substituicoes exatas, cada uma obrigada a acertar um alvo unico.

    Exigir unicidade nao e preciosismo: mutacao que nao encontra o alvo edita
    NADA, o teste passa, e um teste verde por mutacao que nao aconteceu e a
    mesma ilusao que este arquivo existe para desfazer.
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


def degrau(doc, nivel):
    for n in doc['escada_de_fontes']['niveis']:
        if n['nivel'] == nivel:
            return n
    raise AssertionError('degrau %d nao existe' % nivel)


def _sem_na_tela(doc):
    del degrau(doc, 3)['na_tela']


def _ressalva_nula(doc):
    degrau(doc, 3)['na_tela']['ressalva'] = None


def _rotulo_divergente(doc):
    degrau(doc, 3)['na_tela']['rotulo'] = 'manual do fabricante'


def _tabela_divergente(doc):
    doc['rotulos_de_origem']['fabricante-via-busca']['ressalva'] = None


def _pa_por_loja_oficial(doc):
    """Um Pa entrando por loja oficial da marca — estado que o banco alcanca.

    Nao e ficcao: o degrau 4 existe na escada, ja tem fonte no banco para outros
    campos, e basta alguem transcrever um pascal de la. O modelo escolhido e o
    S20, que esta na lista de elegiveis das NOVE situacoes.
    """
    for r in doc['registros']:
        if r['id'] == 'xiaomi-s20':
            r['fontes']['f-specs']['nivel'] = 4
            r['fontes']['f-specs']['origem'] = 'varejo-oficial-da-marca'
            return
    raise AssertionError('xiaomi-s20 nao esta no banco')


def _atribuicao_digitada(base):
    """Tres passos, e os tres sao a MESMA mutacao: o codigo de antes da correcao,
    posto diante do mundo em que o defeito aparece.

    Com o banco de hoje o literal e indistinguivel do derivado — as onze fontes
    de Pa sao do mesmo degrau —, entao a mutacao seria INERTE. Ela precisa do Pa
    entrando por loja oficial.

    E precisa de um terceiro passo que quase ficou de fora: REGERAR o arquivo de
    dados a partir do banco mutado. Sem ele a mutacao reprova, mas pelo motivo
    ERRADO — o banco e o arquivo que o site consome ficariam divergentes e a
    trava do rotulo dispararia primeiro, deixando a trava da ATRIBUICAO sem ser
    exercitada. Mutacao que reprova por outra coisa e uma trava que continua nao
    medida.
    """
    editar_json(MODELOS, _pa_por_loja_oficial)(base)
    subprocess.run([sys.executable, os.path.join(base, 'ferramentas', 'gerar-r2.py'),
                    '--gravar'], cwd=base, capture_output=True, text=True, check=True)
    troca(R2,
          "$m['procedencia']['quem_declara'],\n"
          "\t\t( $m['pa'] > $seguro['valor'] ) ? 'acima' : 'no m\u00ednimo',",
          "'pelo fabricante',\n"
          "\t\t( $m['pa'] > $seguro['valor'] ) ? 'acima' : 'no m\u00ednimo',")(base)


# --------------------------------------------------------------------------
# A SECAO "EXATAMENTE NO LIMIAR" (R2 1.3.0, 12/09/2026). Mesma familia do
# cartao, outra secao — e a secao que ficou doze dias sem procedencia porque
# ninguem a le como recomendacao. As mutacoes aqui sao as mesmas tres familias,
# mais as duas que so existem neste bloco: a porta de compra que nao pode
# nascer, e a ausencia dela que nao pode voltar ao silencio.
# --------------------------------------------------------------------------

NL_LINHA_FONTE = """\t\t\t$html .= '<span class="rbm-vitrine-fonte">'
\t\t\t\t. esc_html( 'Como sabemos \u2014 ' . $p['rotulo'] . ', verificado em '
\t\t\t\t\t. robometria_r2_data( $p['verificado_em'] ) )
\t\t\t\t. ( empty( $p['url'] ) ? '' : ' \u00b7 ' . ( function_exists( 'robometria_casca_fonte_link' )
\t\t\t\t\t? robometria_casca_fonte_link( $p['url'] ) : '' ) )
\t\t\t\t. '</span>';
"""

NL_BLOCO_TAG = """\t\t\tif ( ! empty( $p['ressalva'] ) ) {
\t\t\t\t$html .= '<span class="rbm-tag">' . esc_html( $p['ressalva'] ) . '</span>';
\t\t\t}
"""

NL_FRASE_SEM_PORTA = """\t\t$html .= '<p class="rbm-nota">' . esc_html( robometria_r2_frase_sem_porta() ) . '</p>';
"""

NL_ATRIBUICAO_PHP = """\t\t$m['procedencia']['quem_declara'],
\t\trobometria_r2_com_artigo( $seguro ),"""

NL_ATRIBUICAO_PY = """        % (rotulo_do_modelo(m), numero_br(pa), p["quem_declara"],
           com_artigo(seguro["publicador"]), numero_br(seguro["valor"]))"""


def _pa_do_limiar_por_loja_oficial(doc):
    """O Pa do E10 entrando por loja oficial da marca.

    O E10 e um dos DOIS modelos que estao exatamente no limiar em oito das nove
    situacoes — e e por isso que ele, e nao o S20 do cartao, e o modelo desta
    mutacao: quem nao aparece na secao medida nao produz o mundo em que o
    defeito dela aparece.
    """
    for r in doc['registros']:
        if r['id'] == 'xiaomi-e10':
            r['fontes']['f-specs']['nivel'] = 4
            r['fontes']['f-specs']['origem'] = 'varejo-oficial-da-marca'
            return
    raise AssertionError('xiaomi-e10 nao esta no banco')


def _atribuicao_do_limiar_digitada(base):
    """A atribuicao do Pa volta a ser o modelo, diante do mundo em que isso mente.

    Os TRES passos do _atribuicao_digitada valem inteiros aqui, mais um quarto
    que e proprio desta frase: ela e comparada, palavra por palavra, com a
    implementacao de referencia (item 3 da bancada). Mudar so o PHP reprovaria
    na comparacao das frases e deixaria a trava da ATRIBUICAO sem exercicio —
    entao a referencia muda junto, e e o gerador que reescreve os dados.
    """
    editar_json(MODELOS, _pa_do_limiar_por_loja_oficial)(base)
    troca(REFERENCIA, NL_ATRIBUICAO_PY,
          """        % (rotulo_do_modelo(m), numero_br(pa), "pelo fabricante",
           com_artigo(seguro["publicador"]), numero_br(seguro["valor"]))""")(base)
    subprocess.run([sys.executable, os.path.join(base, 'ferramentas', 'gerar-r2.py'),
                    '--gravar'], cwd=base, capture_output=True, text=True, check=True)
    troca(R2, NL_ATRIBUICAO_PHP,
          """\t\t'pelo fabricante',
\t\trobometria_r2_com_artigo( $seguro ),""")(base)


def _limiar_sem_quem_publica(base):
    """O segundo numero perde a segunda procedencia.

    A frase publica DOIS numeros de origens diferentes — o Pa do modelo e o
    limiar da fonte editorial. Tirar o nome de quem publica o limiar deixa a
    frase com uma atribuicao so cobrindo os dois, que e a sexta decisao do
    PROMPT.md ao contrario. Referencia e PHP juntos, pelo mesmo motivo de cima.
    """
    troca(REFERENCIA, NL_ATRIBUICAO_PY,
          """        % (rotulo_do_modelo(m), numero_br(pa), p["quem_declara"],
           "a fonte", numero_br(seguro["valor"]))""")(base)
    subprocess.run([sys.executable, os.path.join(base, 'ferramentas', 'gerar-r2.py'),
                    '--gravar'], cwd=base, capture_output=True, text=True, check=True)
    troca(R2, NL_ATRIBUICAO_PHP,
          """\t\t$m['procedencia']['quem_declara'],
\t\t'a fonte',""")(base)


MUTACOES = [
    (
        'a linha de procedencia some da secao "Exatamente no limiar"',
        'a secao nomeia modelo e Pa com a mesma autoridade da vitrine, e voltaria a nao dizer de onde o numero veio',
        troca(R2, NL_LINHA_FONTE, ''),
    ),
    (
        'a ressalva do degrau some da secao "Exatamente no limiar"',
        'o elo mais fraco cala justamente onde a pagina ja esta dizendo que o modelo nao esta acima do limiar',
        troca(R2, NL_BLOCO_TAG, ''),
    ),
    (
        'a atribuicao do limiar volta a ser o modelo, e um Pa entra por loja oficial',
        'a frase diria "declarados pelo fabricante" sobre um numero que quem transcreveu foi a loja — na secao que ninguem le como recomendacao',
        _atribuicao_do_limiar_digitada,
    ),
    (
        'o limiar perde o nome de quem o publica',
        'dois numeros de origens diferentes ficam sob uma atribuicao so, que e a sexta decisao do PROMPT.md ao contrario',
        _limiar_sem_quem_publica,
    ),
    (
        'nasce uma porta de compra dentro da secao do limiar',
        'a pagina acabou de recusar estes modelos; botao embaixo da recusa e recomendar assim mesmo',
        troca(R2,
              "\t\t\t$html .= '</li>';\n\t\t}\n\t\t$html .= '</ul></div>';",
              "\t\t\t$html .= '<span class=\"rbm-vitrine-acao\"><span class=\"rbm-sem-loja\">"
              "Link de loja em breve</span></span>';\n"
              "\t\t\t$html .= '</li>';\n\t\t}\n\t\t$html .= '</ul></div>';"),
    ),
    (
        'a ausencia da porta de compra volta a ser silencio',
        'trocar um silencio por outro nao e conserto: sem a frase, o link de fonte volta a ser a unica coisa clicavel sem explicacao',
        troca(R2, NL_FRASE_SEM_PORTA, ''),
    ),
    (
        'a linha de procedencia some do cartao',
        'o numero que decide a recomendacao volta a ser publicado sem endereco e sem data',
        troca(R2, LINHA_FONTE, ''),
    ),
    (
        'a procedencia vem ANTES da porta de compra',
        'e a cicatriz de 10/09/2026: o link de fonte volta a ser a unica porta clicavel do cartao',
        trocas(R2, [(BLOCO_ACAO, ''), (LINHA_FONTE, LINHA_FONTE + BLOCO_ACAO)]),
    ),
    (
        'a data sai da linha de procedencia',
        'procedencia sem data nao e conferivel, e a secao 5.4 pede a data dentro da propria frase',
        troca(R2,
              "'Como sabemos — ' . $p['rotulo'] . ', verificado em '\n\t\t\t\t. robometria_r2_data( $p['verificado_em'] ) )",
              "'Como sabemos — ' . $p['rotulo'] )"),
    ),
    (
        'o link de fonte vira botao',
        'a procedencia existe para ser conferida, nao clicada: com cara de botao ela volta a competir com a compra',
        # A quebra de linha e a indentacao fazem parte do alvo: desde a 1.3.0 a mesma linha existe
        # tambem na secao "Exatamente no limiar", um tab mais fundo — e quatro
        # tabs sao um pedaco de cinco tabs, entao so a quebra de linha desempata.
        troca(R2,
              "\n\t\t\t\t? robometria_casca_fonte_link( $p['url'] ) : '' ) )",
              "\n\t\t\t\t? '<a class=\"rbm-comprar\" href=\"' . esc_url( $p['url'] ) . '\" rel=\"nofollow noopener\">fonte</a>' : '' ) )"),
    ),
    (
        'a ressalva do degrau some do cartao',
        '"a confirmar no manual" e o elo fraco dito com todas as letras, no lugar onde o leitor decide se compra',
        troca(R2, BLOCO_TAG, ''),
    ),
    (
        'a ressalva sai DEPOIS do botao de compra',
        'ressalva que aparece depois da decisao nao e ressalva, e nota de rodape',
        trocas(R2, [(BLOCO_TAG, ''), (BLOCO_ACAO, BLOCO_ACAO + BLOCO_TAG)]),
    ),
    (
        'a atribuicao volta a ser digitada no molde, e um Pa entra por loja oficial',
        'e o defeito inteiro: a pagina diria "declarados pelo fabricante" sobre um numero que quem transcreveu foi a loja',
        _atribuicao_digitada,
    ),
    (
        'o degrau 3 perde o na_tela na escada',
        'degrau mudo faz a tela imprimir o apelido de campo cru, e so se descobre no ar',
        editar_json(ESQUEMA, _sem_na_tela),
    ),
    (
        'o degrau 3 fica sem ressalva na escada',
        'silencio nunca promove: degrau abaixo da leitura direta sem ressalva publica um rigor que a ilha nao tem',
        editar_json(ESQUEMA, _ressalva_nula),
    ),
    (
        'o degrau 3 se renomeia "manual do fabricante" na escada',
        'a ilha nao tem nivel 2 nenhum; chamar busca de manual e inflar o proprio nivel de fonte',
        editar_json(ESQUEMA, _rotulo_divergente),
    ),
    (
        'a tabela que viaja para o site diverge da escada',
        'duas copias da mesma escada, e a que o site consome perdendo a ressalva sem ninguem ver',
        editar_json(RESPOSTAS, _tabela_divergente),
    ),
]


def main():
    reprovadas = 0
    passaram = []

    print('Mutacoes deliberadas na procedencia do Pa (R2 1.3.0) — cada uma TEM que reprovar\n')

    for nome, porque, aplicar in MUTACOES:
        with tempfile.TemporaryDirectory() as tmp:
            base = os.path.join(tmp, 'ilha')
            shutil.copytree(RAIZ, base)
            try:
                aplicar(base)
            except AssertionError as erro:
                print('  ERRO   %-62s %s' % (nome, erro))
                passaram.append(nome)
                continue

            falhas = []
            pegou_em = []
            for teste in TESTES:
                saida = subprocess.run(
                    ['php', os.path.join(base, teste), base],
                    capture_output=True, text=True)
                if saida.returncode != 0:
                    pegou_em.append(os.path.basename(teste))
                    falhas += [l.strip() for l in saida.stdout.splitlines()
                               if l.strip().startswith('FALHA')]

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
