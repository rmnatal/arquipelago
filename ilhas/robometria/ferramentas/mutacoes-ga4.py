#!/usr/bin/env python3
"""Quebra de proposito a tag de medicao da casca 1.5.0 e exige que a bancada REPROVE.

    python3 ferramentas/mutacoes-ga4.py

POR QUE ESTE ARQUIVO EXISTE
---------------------------
"A PROVA DE QUE UMA TRAVA REPROVA E PARTE DO BLOCO" (secao 8 do ARQUIPELAGO.md).
Esta ilha ja viu cinco travas passarem verdes medindo a si mesmas, e a tag de
medicao e um alvo facil para a sexta: ela nao muda NADA na tela. Nenhum leitor,
nenhuma ronda e nenhum olho humano percebe a diferenca entre medir a propriedade
certa e medir a errada, entre a tag vir antes ou depois do JSON-LD, ou entre o ID
morar numa constante e estar digitado no meio de uma funcao. Se o portao nao
pegar, ninguem pega — e o defeito vive meses gravando dado no lugar errado.

A MAIS IMPORTANTE DA LISTA e a de numero 5, "um JSON-LD novo nasce acima da tag":
ela nao tira a tag da pagina e nao muda uma letra do codigo da medicao. Uma trava
que so pergunta "a tag esta ai?" aprova essa mutacao com folga, e era exatamente
essa a trava facil de escrever. Por causa dela o portao mede ORDEM.

A segunda mais importante e a de numero 2, "o ID e o da ilha vizinha": e o que
acontece de verdade no dia em que alguem copiar esta casca para a ilha seguinte,
como a casca da Robometria foi copiada da Aquametria em 10/09/2026. O ID daqui
esta ESCRITO na regua do teste justamente para essa copia reprovar.
"""

import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASCA = 'snippets/robometria-casca.php'
TESTES = ('ferramentas/teste-casca.php',)

# O ID DA AQUAMETRIA, a ilha de onde esta casca foi copiada. Nao e um ID
# inventado de proposito: e o que a copia cega deixaria para tras.
ID_DA_VIZINHA = 'G-8Y26XFZF39'


def trocas(arquivo, pares):
    """Substituicoes exatas, cada uma obrigada a acertar um alvo unico.

    Mutacao que nao encontra o alvo edita NADA e o teste passa — teste verde por
    mutacao que nao aconteceu e a mesma ilusao que este arquivo desfaz.
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


JSONLD_INTRUSO = """}, 22 );

add_action( 'wp_head', function () {
	echo '<script type="application/ld+json" id="robometria-intruso">'
		. wp_json_encode( array( '@type' => 'WebPage' ) ) . '</script>' . "\\n";
}, 24 );
"""

MUTACOES = [
    (
        '1. a tag nao sai em pagina nenhuma',
        'sem tag a secao 5 do contrato nao e mensuravel, e o zero do GA4 mede a ausencia dela',
        troca(CASCA,
              "\tif ( ! defined( 'ROBOMETRIA_CASCA_GA4' ) || '' === ROBOMETRIA_CASCA_GA4 ) {",
              "\tif ( true ) {"),
    ),
    (
        '2. o ID e o da ilha vizinha (a copia cega)',
        'a ilha nova nasceria mandando dado para a propriedade da anterior, com a tag NO AR',
        troca(CASCA, "'G-RM7KS75QP2'", "'%s'" % ID_DA_VIZINHA),
    ),
    (
        '3. o src esta certo e o config mede outra propriedade',
        'meia tag: o endereco carrega a biblioteca certa e a sessao vai para o lugar errado',
        troca(CASCA,
              "\t\t. \"gtag('config', '\" . $id . \"');\";",
              "\t\t. \"gtag('config', '%s');\";" % ID_DA_VIZINHA),
    ),
    (
        '4. o script de terceiro perde o async',
        'sem async ele bloqueia o parser, e a medicao passa a custar o LCP que o despacho protege',
        troca(CASCA,
              "echo '<script async src=\"https://www.googletagmanager.com/gtag/js?id='",
              "echo '<script src=\"https://www.googletagmanager.com/gtag/js?id='"),
    ),
    (
        '5. um JSON-LD novo nasce ACIMA da tag',
        'a tag continua na pagina e passa a vir antes do JSON-LD — trava de presenca aprova isto',
        troca(CASCA, "}, 22 );\n", JSONLD_INTRUSO),
    ),
    (
        '6. a tag sobe para a prioridade 3',
        'entraria antes da description e do JSON-LD, que e literalmente o que o despacho proibe',
        troca(CASCA, "}, 23 );", "}, 3 );"),
    ),
    (
        '7. o ID volta a ser digitado no meio do codigo',
        'na tela as duas formas sao identicas; e no arquivo que a proxima ilha erra a copia',
        troca(CASCA, "\t$id = ROBOMETRIA_CASCA_GA4;", "\t$id = 'G-RM7KS75QP2';"),
    ),
    (
        '8. um segundo script de terceiro entra na pagina publica',
        'a medicao e o UNICO terceiro permitido (secao 22.3); o segundo entra sempre "so desta vez"',
        troca(CASCA,
              "\techo '<link rel=\"stylesheet\" href=\"' . esc_url( $fontes ) . '\">' . \"\\n\";",
              "\techo '<link rel=\"stylesheet\" href=\"' . esc_url( $fontes ) . '\">' . \"\\n\";\n"
              "\techo '<script src=\"https://cdn.exemplo.com/enfeite.js\"></script>' . \"\\n\";"),
    ),
    (
        '9. a pagina para de contar o que o site mede',
        'medir sem dizer e o que a frase do despacho existe para impedir',
        troca(CASCA,
              "\t$html .= '<p>Este site usa o Google Analytics 4 para medir audiência: quantas pessoas chegam, por onde chegaram e quais páginas leram. É isso, e é agregado — a gente não sabe quem você é, não pede cadastro, não tem login e não vende nada que você faça por aqui para ninguém.</p>';",
              "\t$html .= '<p>A gente acompanha de longe quantas pessoas passam por aqui.</p>';"),
    ),
]


def main():
    reprovadas = 0
    passaram = []

    print('Mutacoes deliberadas na tag de medicao da casca 1.5.0 — cada uma TEM que reprovar\n')

    for nome, porque, aplicar in MUTACOES:
        with tempfile.TemporaryDirectory() as tmp:
            base = os.path.join(tmp, 'ilha')
            shutil.copytree(RAIZ, base)
            try:
                aplicar(base)
            except AssertionError as erro:
                print('  ERRO   %-58s %s' % (nome, erro))
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
                print('  PASSOU %-58s <- a trava NAO pegou' % nome)
                print('         (%s)' % porque)
                passaram.append(nome)
                continue

            print('  ok     %-58s %d falha(s) em %s'
                  % (nome, len(falhas), ', '.join(pegou_em)))
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
