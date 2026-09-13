#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escreve de volta a atribuicao falsa da funcao e exige REPROVACAO.

    python3 ferramentas/mutacoes-atribuicao-da-funcao.py

POR QUE ESTE ARQUIVO EXISTE
---------------------------
"A PROVA DE QUE UMA TRAVA REPROVA E PARTE DO BLOCO" (secao 8 do ARQUIPELAGO.md).

O DEFEITO, que estava NO AR ate 13/09/2026 e que nenhum portao da ilha via. A R1
publicava:

    A WAP (loja oficial) declara a escova lateral "Escova Direita Para Robo
    Aspirador de Po Robot W300" compativel com W300 ...

A WAP nunca usou a palavra "lateral": ela batiza a peca pela POSICAO. Quem leu a
funcao no contraste do catalogo dela foi esta ilha — e a frase emprestava ao
fabricante a unica coisa que a Robometria vende, que e a declaracao dele. A
Xiaomi e o caso extremo: o titulo dela e so "Brush", e nao nomeia nem posicao.

POR QUE NENHUM PORTAO VIA: todos comparavam a frase do PHP com a da referencia, e
as duas diziam a mesma coisa errada. Duas metades que erram juntas ficam verdes —
e e por isso que a regua nova (portao 15 do ferramentas/teste-r1.php) recomputa
quem e derivada lendo dados/pecas.json e o esquema, sem chamar nenhuma das duas.

A BATERIA COBRE OS DOIS LADOS. Proibir a atribuicao na peca derivada, sozinho,
seria atendido por uma frase que nunca atribui nada a ninguem — e a ilha perderia
de graca a autoridade que o titulo do fabricante lhe da. Por isso as mutacoes (5)
e (6) quebram o lado de CIMA: a peca cujo titulo declara a funcao tem de
continuar atribuindo ao fabricante.

AS MUTACOES QUE PRODUZEM O MUNDO — (8), (9) e (10). O esquema desta ilha permite
`canal-de-manutencao` como origem de funcao e o BANCO NAO TEM NENHUMA PECA ASSIM.
A secao 8 do contrato diz o que fazer com isso: "todo caso que o ESQUEMA permite e
o banco ainda nao tem e um caso que a regua precisa tratar HOJE, e a maneira de
provar que ela o trata e a mutacao que PRODUZ O MUNDO". Entao elas criam a peca
que nao existe e so depois quebram a regra nela. A (10) e a unica da bateria que
tem de PASSAR: mundo novo sem defeito nenhum nao pode reprovar, ou a regua seria
um falso-positivo esperando a primeira peca de manual entrar no banco.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TESTE = 'ferramentas/teste-r1.php'
GERADOR = 'ferramentas/gerar-r1.py'
SNIPPET = 'snippets/robometria-r1.php'
REFERENCIA = 'ferramentas/cobertura-r1.py'
BANCO = 'dados/pecas.json'
ESQUEMA = 'dados/esquema-banco.json'

# A peca de contraste com titulo que nomeia POSICAO, e a que nomeia nada. As duas
# entram porque sao os dois motivos diferentes pelos quais a funcao nao esta no
# titulo, e a ressalva publicada precisa ser verdadeira nos dois.
ALVO_WAP = 'wap-escova-direita-w300'
ALVO_XIAOMI = 'xiaomi-b112-zs'


def _ler(base, rel):
    with open(os.path.join(base, rel), encoding='utf-8') as f:
        return f.read()


def _gravar(base, rel, texto):
    with open(os.path.join(base, rel), 'w', encoding='utf-8') as f:
        f.write(texto)


def _trocar(base, rel, antigo, novo, vezes=1):
    """Troca texto exigindo que o alvo exista e seja unico.

    Mutacao que nao acha o alvo e mutacao INERTE — ela passa por 'reprovou' sem
    ter mexido em nada, e uma bateria de inertes e uma bateria verde que nao mede
    coisa nenhuma. Esta ilha ja perdeu duas mutacoes assim, por refatoracao que
    mudou a linha vizinha; entao aqui o alvo e contado, nunca substituido em
    silencio."""
    texto = _ler(base, rel)
    achadas = texto.count(antigo)
    if achadas != vezes:
        raise AssertionError(
            'o alvo aparece %d vez(es) em %s, esperava %d — mutacao INERTE'
            % (achadas, rel, vezes))
    _gravar(base, rel, texto.replace(antigo, novo))


def _banco(base):
    with open(os.path.join(base, BANCO), encoding='utf-8') as f:
        return json.load(f)


def _gravar_banco(base, d):
    with open(os.path.join(base, BANCO), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
        f.write('\n')


def _registro(d, pid):
    for r in d['registros']:
        if r['id'] == pid:
            return r
    raise AssertionError('%s nao esta mais no banco — a mutacao seria inerte' % pid)


# --------------------------------------------------------------- AS MUTACOES
def _php_volta_a_atribuir(base):
    """O DEFEITO ORIGINAL, escrito de volta no PHP: o molde atribuidor vale para
    toda peca, como valia ate 13/09. A referencia continua certa, entao esta
    mutacao tambem mede se o portao olha o PHP e nao so o gabarito."""
    _trocar(base, SNIPPET,
            "} elseif ( ! robometria_r1_funcao_derivada( $item ) ) {",
            "} elseif ( true ) {")


def _php_perde_a_ressalva(base):
    """A frase para de dizer quem leu a funcao. Sozinha, a abertura fica ate
    'honesta' — ela nao atribui nada —, e e exatamente por isso que a regua cobra
    a ressalva alem de proibir a atribuicao: silencio sobre a procedencia da
    classificacao e a mesma divida com outro rosto."""
    _trocar(base, SNIPPET,
            "\t$ressalva = robometria_r1_ressalva_da_funcao( $item, $tipo );",
            "\t$ressalva = '';")


def _php_troca_a_ressalva_de_origem(base):
    """A PORTA DOS FUNDOS: a ressalva existe, esta bem escrita, e diz que quem
    nomeou a funcao foi o FABRICANTE, no canal de manutencao — quando na verdade
    quem leu foi a ilha, no contraste. E a mentira original de volta, so que em
    letra miuda. Sem comparar a ressalva com o campo do banco, passaria."""
    _trocar(base, SNIPPET,
            "'contraste-no-catalogo' => 'Quem chama esta peça de %s é a Robometria, pelo contraste do catálogo do próprio fabricante: o título dela não nomeia a função.',",
            "'contraste-no-catalogo' => 'Quem chama esta peça de %s é o próprio fabricante, no canal de manutenção dele: o título da peça não nomeia a função.',")


def _referencia_volta_a_atribuir(base):
    """O outro lado: quem erra sozinha e a REFERENCIA, e o PHP fica certo. O
    gabarito e regerado depois, entao a frase errada entra no r1-referencia.json
    como se fosse a verdade. Um portao que so comparasse PHP com gabarito ficaria
    verde no dia em que a regra mudasse so de um lado."""
    _trocar(base, REFERENCIA,
            '    elif atribuicao_da_funcao(peca) in (None, "titulo"):',
            '    elif True:')


def _php_para_de_atribuir_no_titulo(base):
    """O LADO DE CIMA. Todas as pecas passam a usar o molde derivado, inclusive a
    Multi e a Positivo, cujos titulos dizem "Escova Lateral" com todas as letras.
    Nao e defeito de honestidade — e desperdicio: a ilha deixa de dizer que quem
    declarou a funcao foi o fabricante, que e a frase mais forte que ela tem."""
    _trocar(base, SNIPPET,
            "} elseif ( ! robometria_r1_funcao_derivada( $item ) ) {",
            "} elseif ( false ) {")


def _php_poe_ressalva_em_todas(base):
    """O mesmo lado de cima pela outra ponta: a ressalva passa a sair em toda
    peca. A pagina comecaria a dizer "quem chama esta peca de escova lateral e a
    Robometria" para a peca que a Multi publica COMO "Escova Lateral" — jogando
    fora a procedencia e confessando uma derivacao que nao houve."""
    _trocar(base, SNIPPET,
            "\tif ( ! robometria_r1_funcao_derivada( $item ) ) {\n\t\treturn '';\n\t}",
            "\tif ( false ) {\n\t\treturn '';\n\t}")


def _esquema_perde_a_lista(base):
    """PRODUZ O MUNDO PELO ESQUEMA. Nenhuma peca fica errada: some a chave
    `tipos_que_exigem_funcao_declarada`, de onde a regua le quais tipos cobrar.
    Uma regua que le a propria lista de um arquivo de dados e cai para "nada a
    cobrar" quando a chave falta aprova TUDO em silencio — o banco de hoje
    continua verde e a peca seguinte entra sem atribuicao nenhuma."""
    caminho = os.path.join(base, ESQUEMA)
    with open(caminho, encoding='utf-8') as f:
        e = json.load(f)
    if 'tipos_que_exigem_funcao_declarada' not in e:
        raise AssertionError('o esquema ja nao tem a chave — a mutacao seria inerte')
    del e['tipos_que_exigem_funcao_declarada']
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(e, f, ensure_ascii=False, indent=1)
        f.write('\n')


def _mundo_do_manual(base):
    """Cria a peca que o ESQUEMA permite e o banco nunca teve: funcao declarada
    pelo CANAL DE MANUTENCAO do fabricante. E o caso em que a funcao E palavra do
    fabricante, so que dita em outro canal que nao o titulo da peca — a ressalva
    correta muda de sujeito, e nenhuma peca do banco de hoje exercita isso."""
    d = _banco(base)
    r = _registro(d, ALVO_XIAOMI)
    r['funcao']['declarada_por'] = 'canal-de-manutencao'
    r['funcao']['declarado_como'] = (
        'MUNDO DE BANCADA: o manual do modelo nomeia esta peca como escova principal'
    )
    _gravar_banco(base, d)


def _mundo_do_manual_com_ressalva_de_contraste(base):
    """O mundo acima, e a ressalva ERRADA servida nele: a pagina diria que quem
    leu a funcao foi a Robometria, quando foi o proprio fabricante no manual.
    Errar para MENOS tambem e errar — a ilha jogaria fora uma declaracao que tem."""
    _mundo_do_manual(base)
    _trocar(base, SNIPPET,
            "'canal-de-manutencao'   => 'Quem chama esta peça de %s é o próprio fabricante, no canal de manutenção dele: o título da peça não nomeia a função.',",
            "'canal-de-manutencao'   => 'Quem chama esta peça de %s é a Robometria, pelo contraste do catálogo do próprio fabricante: o título dela não nomeia a função.',")


def _mundo_do_manual_atribuindo(base):
    """O mundo novo com o defeito de 13/09 dentro dele: a frase volta a dizer
    "a Xiaomi declara a escova principal X". Sem produzir o mundo, esta linha da
    regua nunca rodaria — ela ficaria verde por ausencia de contraexemplo, que e
    a definicao de regua escrita para um mundo que nunca aconteceu."""
    _mundo_do_manual(base)
    _php_volta_a_atribuir(base)


def _mundo_do_manual_intacto(base):
    """A UNICA QUE TEM DE PASSAR. O mundo novo, sem defeito nenhum. Se a regua
    reprovasse aqui, ela seria um falso-positivo esperando a primeira peca de
    manual entrar no banco — e o proximo coletor aprenderia a ignora-la."""
    _mundo_do_manual(base)


MUTACOES = [
    ('o PHP volta a atribuir a funcao ao fabricante',
     'o defeito original de 13/09: "a WAP declara a escova lateral X", palavra que a WAP nunca usou',
     _php_volta_a_atribuir, True, True),
    ('a ressalva some da frase derivada',
     'a frase para de atribuir E para de dizer quem leu: silencio sobre a procedencia da classificacao',
     _php_perde_a_ressalva, True, True),
    ('a ressalva do contraste vira a do canal de manutencao',
     'a porta dos fundos: a mentira original em letra miuda, com a ressalva bem escrita',
     _php_troca_a_ressalva_de_origem, True, True),
    ('a REFERENCIA volta a atribuir, e o gabarito e regerado',
     'quem erra e o gabarito: portao que so compara PHP com gabarito fica verde',
     _referencia_volta_a_atribuir, True, True),
    ('o PHP para de atribuir tambem onde o titulo declara',
     'o lado de cima: a ilha joga fora a frase mais forte que tem, a declaracao do fabricante',
     _php_para_de_atribuir_no_titulo, True, True),
    ('a ressalva passa a sair em TODA peca',
     'a peca que a Multi publica como "Escova Lateral" confessaria uma derivacao que nao houve',
     _php_poe_ressalva_em_todas, True, True),
    ('o ESQUEMA perde a lista de tipos que exigem funcao',
     'PRODUZ O MUNDO: nenhuma peca fica errada e a regua passa a nao ter o que cobrar',
     _esquema_perde_a_lista, False, True),
    ('MUNDO NOVO (canal de manutencao) com a ressalva do contraste',
     'errar para menos tambem e errar: a ilha jogaria fora uma declaracao que o fabricante fez',
     _mundo_do_manual_com_ressalva_de_contraste, True, True),
    ('MUNDO NOVO (canal de manutencao) com a atribuicao de volta',
     'sem produzir o mundo, esta linha da regua nunca rodaria — verde por ausencia de contraexemplo',
     _mundo_do_manual_atribuindo, True, True),
    ('MUNDO NOVO (canal de manutencao) intacto — esta TEM de passar',
     'regua que reprova o mundo novo sem defeito e falso-positivo esperando a primeira peca de manual',
     _mundo_do_manual_intacto, True, False),
]


def main():
    corretas = 0
    erradas = []

    print('Mutacoes deliberadas na atribuicao da funcao — todas reprovam, menos a ultima\n')

    for nome, porque, aplicar, regerar, deve_reprovar in MUTACOES:
        with tempfile.TemporaryDirectory() as tmp:
            base = os.path.join(tmp, 'ilha')
            shutil.copytree(RAIZ, base)
            try:
                aplicar(base)
            except AssertionError as err:
                print('  ERRO   %-62s %s' % (nome, err))
                erradas.append(nome)
                continue

            if regerar:
                gerou = subprocess.run(
                    ['python3', os.path.join(base, GERADOR), '--gravar'],
                    capture_output=True, text=True, cwd=base)
                if gerou.returncode != 0:
                    # Gerador que para tambem e reprovacao: a frase nao chega a
                    # nascer. So vale quando era isso que se esperava.
                    if deve_reprovar:
                        print('  ok     %-62s o gerador parou antes de escrever a frase' % nome)
                        corretas += 1
                    else:
                        print('  ERRADA %-62s o gerador parou num mundo que devia passar' % nome)
                        print('         %s' % gerou.stderr.strip().splitlines()[-1][:110])
                        erradas.append(nome)
                    continue

            saida = subprocess.run(['php', os.path.join(base, TESTE), base],
                                   capture_output=True, text=True, cwd=base)
            reprovou = saida.returncode != 0

            if reprovou == deve_reprovar:
                if deve_reprovar:
                    linhas = [l.strip() for l in saida.stdout.splitlines()
                              if l.strip().startswith('FALHA')]
                    print('  ok     %-62s %d portao(oes) reprovou(aram)' % (nome, len(linhas)))
                    for l in linhas[:2]:
                        print('         %s' % l[:118])
                else:
                    print('  ok     %-62s passou, como tinha de passar' % nome)
                corretas += 1
                continue

            if deve_reprovar:
                print('  PASSOU %-62s <- a trava NAO pegou' % nome)
            else:
                print('  REPROVOU %-60s <- falso-positivo' % nome)
            print('         (%s)' % porque)
            erradas.append(nome)

    print('\n%d de %d mutacoes com o resultado esperado.' % (corretas, len(MUTACOES)))
    if erradas:
        print('SEM TRAVA para:')
        for n in erradas:
            print('  - %s' % n)
        return 1
    print('Todas as travas reprovam o que tem de reprovar, e a regua nao reprova o mundo novo sadio.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
