#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escreve de volta o rotulo que esteve no ar e exige REPROVACAO.

    python3 ferramentas/mutacoes-rotulo-da-caixa.py

POR QUE ESTE ARQUIVO EXISTE
---------------------------
"A PROVA DE QUE UMA TRAVA REPROVA E PARTE DO BLOCO" (secao 8 do ARQUIPELAGO.md).

O DEFEITO, medido no ar pela ronda diaria de 23/10/2026 e despachado no mesmo dia
(item 1). A caixa de resultado da `/quantos-pa-o-robo-aspirador-precisa/` nasceu
na 1.10.0, com o molde de conversao da secao 32, servindo na PRIMEIRA TELA e em
Mono o numero do limiar seguido do literal `'Pa ou mais'`. "Ou mais" e inclusivo.
Em 8 das 9 situacoes desta ferramenta o limiar seguro e `acima_de` — a Canaltech
escreve "acima de 4.000 Pa" — e a lista e montada em `pa > valor`, porque um
modelo de exatamente 4.000 Pa nao esta acima de 4.000.

Resultado no ar, com `area=110&piso=tapete fino&pelo=curto`: a caixa prometia
`>= 4.000`, a vitrine listava 5 modelos, e o banco tem 7 publicaveis com canal
brasileiro em Pa maior ou igual a 4.000. Os dois que faltavam — `xiaomi-e10` e
`xiaomi-s10`, 4.000 Pa cada — estavam na MESMA pagina, num bloco rotulado que
diz, com todas as letras, que *"estar no numero nao e estar acima dele"*. A
pagina se contradizia a si mesma a duas telas de distancia.

E POR QUE NADA PEGOU, QUE E O QUE IMPORTA AQUI: o `teste-r2.php` ja tinha, desde
10/09, um portao que confere a classificacao INTEIRA contra o operador que a
fonte declara, com conta escrita por ele proprio — e ele estava verde no dia do
defeito, porque estava certo. Ninguem nunca havia perguntado o que a CAIXA
promete. A metade de baixo era medida por duas contas independentes; a frase mais
lida da pagina era um literal digitado a mao, fora do alcance de tudo.

E a mesma familia que esta ilha ja nomeou tres vezes — lista digitada ao lado de
lista contada, `robometria_casca_categorias()`, a frase do `/ferramentas/` — um
andar acima: AQUI O LITERAL ESTAVA AO LADO DA FUNCAO QUE LE O DADO, no mesmo
arquivo, a uma linha de distancia. A frase de leitura da propria caixa ja pegava
o operador por `robometria_r2_escrever_limiar()`.

O QUE CADA MUTACAO TEM DE FAZER: reprovar. A (1) e o mundo de 23/10 letra por
letra. A (3) e a que importa mais — ela troca SO a palavra do rotulo, sem tocar
no dado nem na lista, e portanto e invisivel para todos os outros 41 portoes
desta ilha: se ela passar, o portao novo nao serve para nada.
"""

import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SNIPPET = 'snippets/robometria-r2.php'
TESTE = 'ferramentas/teste-r2.php'
REFERENCIA = 'ferramentas/cobertura-r2.py'

CHAMADA_CERTA = """	$html .= robometria_casca_caixa(
		robometria_r2_rotulo_da_caixa( $s['limiar_seguro'] ),
		robometria_r2_n( $s['limiar_seguro']['valor'] ),
		'Pa',"""


def _trocar(base, arquivo, antes, depois, quantas=1):
    caminho = os.path.join(base, arquivo)
    with open(caminho, encoding='utf-8') as f:
        texto = f.read()
    achadas = texto.count(antes)
    if achadas != quantas:
        raise AssertionError('%s: esperava %d ocorrencia(s) de %r, achei %d — a '
                             'mutacao seria inerte'
                             % (arquivo, quantas, antes[:56], achadas))
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(texto.replace(antes, depois))


def m01_mundo_de_23_10(base):
    """O MUNDO MEDIDO NO AR, letra por letra: o rotulo volta a ser 'Succao a
    procurar' e a unidade volta ao literal 'Pa ou mais'. A lista nao muda."""
    _trocar(base, SNIPPET, CHAMADA_CERTA,
            """	$html .= robometria_casca_caixa(
		'Sucção a procurar',
		robometria_r2_n( $s['limiar_seguro']['valor'] ),
		'Pa ou mais',""")


def m02_ou_acima_no_lugar_de_ou_mais(base):
    """A MESMA MENTIRA COM OUTRAS PALAVRAS. Um portao que soubesse so a string
    'ou mais' aprovaria esta — e e assim que um defeito volta: pela sinonimia."""
    _trocar(base, SNIPPET, CHAMADA_CERTA,
            """	$html .= robometria_casca_caixa(
		'Sucção a procurar',
		robometria_r2_n( $s['limiar_seguro']['valor'] ),
		'Pa ou acima',""")


def m03_operador_do_rotulo_invertido(base):
    """A QUE IMPORTA MAIS, e ela e de uma palavra: o rotulo passa a dizer "a
    partir de" onde a fonte escreve "acima de", e NADA MAIS MUDA — nem o dado,
    nem a lista, nem a contagem, nem uma frase. Invisivel para os outros 41
    portoes desta ilha por construcao: eles conferem o dado contra o dado."""
    _trocar(base, SNIPPET,
            "		. ( 'acima_de' === $l['comparacao'] ? 'acima de' : 'a partir de' );",
            "		. ( 'acima_de' === $l['comparacao'] ? 'a partir de' : 'acima de' );")


def m04_rotulo_sem_operador(base):
    """O ROTULO CALA O OPERADOR. Nao mente — omite, e a caixa volta a nao dizer
    se o numero dela entra ou nao entra. Omissao na primeira tela de uma pagina
    de recomendacao nao e neutra: o leitor preenche o vazio com o inclusivo,
    que e a leitura natural de um piso."""
    _trocar(base, SNIPPET,
            "	return 'Sucção a procurar — '\n"
            "		. ( 'acima_de' === $l['comparacao'] ? 'acima de' : 'a partir de' );",
            "	return 'Sucção a procurar';")


def m05_numero_da_caixa_digitado(base):
    """O NUMERO DA CAIXA SAI DE UM LITERAL em vez do limiar da situacao — o
    mesmo defeito do rotulo, uma linha abaixo. Ele acerta 8 das 9 situacoes,
    que e exatamente o que faz este tipo de defeito sobreviver: a situacao-
    ancora continua certa e a `liso|nao`, de limiar 3.000, passa a mentir."""
    _trocar(base, SNIPPET,
            "		robometria_r2_rotulo_da_caixa( $s['limiar_seguro'] ),\n"
            "		robometria_r2_n( $s['limiar_seguro']['valor'] ),",
            "		robometria_r2_rotulo_da_caixa( $s['limiar_seguro'] ),\n"
            "		'4.000',")


def m06_a_lista_passa_a_incluir_o_empate(base):
    """O DEFEITO PELO OUTRO LADO, e e o que a secao 7 do contrato chama de GRAVE:
    a referencia passa a comparar `>=` tambem no `acima_de`, e um modelo que a
    fonte citada NAO cobre entra na lista de recomendacao. O rotulo continua
    dizendo "acima de" e a contagem na tela vira 7. Esta reprova por dois
    caminhos — o portao da classificacao, que e de 10/09, e o novo —, e esta
    aqui para registrar que os dois cobrem direcoes opostas do mesmo erro."""
    _trocar(base, REFERENCIA,
            '    if limiar["comparacao"] == "acima_de":\n        return pa > limiar["valor"]\n'
            '    return pa >= limiar["valor"]',
            '    return pa >= limiar["valor"]')


def m07_o_leitor_de_rotulo_esquece_ou_mais(base):
    """MATA A REGUA, NAO O MUNDO. O leitor de rotulo do portao deixa de conhecer
    'ou mais' — a propria string que esteve no ar. Sem os 6 casos conhecidos
    isto passaria verde e o portao ficaria cego para o defeito que o fez nascer,
    com cara de medicao fresca. Chave que some da regua tem de matar a regua."""
    _trocar(base, TESTE,
            "	$tem_ou_mais = false !== strpos( $t, 'ou mais' ) || false !== strpos( $t, 'ou acima' );",
            "	$tem_ou_mais = false;")


def m08_mundo_intacto(base):
    """A UNICA QUE TEM DE PASSAR. Regua que reprova o mundo sem defeito e um
    falso-positivo esperando quem chegar amanha para aprender a ignora-la."""
    return


MUTACOES = [
    ('MUNDO DE 23/10 — o literal "Pa ou mais" de volta',
     'a caixa promete >= 4.000 e a vitrine lista > 4.000: 5 na tela, 7 no banco',
     m01_mundo_de_23_10, False),
    ('a mesma mentira por sinonimo: "Pa ou acima"',
     'portao que decora uma string so aprova o defeito que troca de palavra',
     m02_ou_acima_no_lugar_de_ou_mais, False),
    ('SO O OPERADOR DO ROTULO, invertido — nada mais muda',
     'invisivel para os outros 41 portoes: eles conferem o dado contra o dado',
     m03_operador_do_rotulo_invertido, False),
    ('o rotulo cala o operador',
     'caixa que nao diz se o numero dela entra deixa o leitor preencher',
     m04_rotulo_sem_operador, False),
    ('o numero da caixa volta a ser digitado',
     'acerta 8 das 9 situacoes, e e por isso que sobrevive',
     m05_numero_da_caixa_digitado, False),
    ('A LISTA passa a incluir o empate (a referencia compara >=)',
     'modelo que a fonte citada nao cobre entra na recomendacao (secao 7: GRAVE)',
     m06_a_lista_passa_a_incluir_o_empate, False),
    ('MATA A REGUA: o leitor de rotulo esquece "ou mais"',
     'o portao fica cego para o defeito que o fez nascer, e verde',
     m07_o_leitor_de_rotulo_esquece_ou_mais, False),
    ('MUNDO INTACTO — esta TEM de passar',
     'regua que reprova o mundo sadio e falso-positivo com data marcada',
     m08_mundo_intacto, True),
]


def copiar(destino):
    for item in ('dados', 'ferramentas', 'snippets', 'manifest.json', 'ARVORE.md'):
        origem = os.path.join(RAIZ, item)
        alvo = os.path.join(destino, item)
        if os.path.isdir(origem):
            shutil.copytree(origem, alvo)
        else:
            shutil.copy2(origem, alvo)


def medir(base):
    """Regera a R2 e roda o teste-r2.php inteiro. Geracao que morre conta como
    reprovacao: ilha que nao monta tambem nao publica."""
    r = subprocess.run([sys.executable, 'ferramentas/gerar-r2.py', '--gravar'],
                       cwd=base, capture_output=True, text=True)
    if r.returncode != 0:
        return 1, 'gerar-r2.py falhou (a mutacao derrubou a geracao)'
    r = subprocess.run(['php', 'ferramentas/teste-r2.php', '.'],
                       cwd=base, capture_output=True, text=True)
    linhas = [l for l in r.stdout.strip().splitlines() if l.strip()]
    return r.returncode, (linhas[-1] if linhas else '(sem saida)')


def main():
    print('MUTACOES DO ROTULO DA CAIXA DE RESULTADO — item 1 do despacho de 23/10/2026')
    print('=' * 78)
    erros = []
    for nome, porque, aplicar, tem_de_passar in MUTACOES:
        with tempfile.TemporaryDirectory() as tmp:
            copiar(tmp)
            try:
                aplicar(tmp)
            except AssertionError as e:
                erros.append('%s: %s' % (nome, e))
                print('  ERRO   %-62s %s' % (nome, e))
                continue
            codigo, ultima = medir(tmp)
            passou = codigo == 0
            if passou == tem_de_passar:
                print('  ok     %-62s %s' % (nome, ultima))
            else:
                erros.append(nome)
                print('  ERRADA %-62s %s' % (nome, ultima))
                print('         %s' % porque)

    print('\n%d de %d como esperado.' % (len(MUTACOES) - len(erros), len(MUTACOES)))
    if erros:
        print('REPROVADO em: ' + '; '.join(erros))
        return 1
    print('Nenhuma mutacao inerte: o portao do rotulo foi visto reprovando nas 7.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
