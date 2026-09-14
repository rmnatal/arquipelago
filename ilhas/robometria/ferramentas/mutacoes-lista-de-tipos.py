#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escreve de volta a lista de tipos DIGITADA e exige REPROVACAO.

    python3 ferramentas/mutacoes-lista-de-tipos.py

POR QUE ESTE ARQUIVO EXISTE
---------------------------
"A PROVA DE QUE UMA TRAVA REPROVA E PARTE DO BLOCO" (secao 8 do ARQUIPELAGO.md).

O DEFEITO, medido NO AR as 23h40Z de 14/09/2026. A descricao do WebApplication
no JSON-LD da R1 — a frase que um modelo de linguagem le para saber o que esta
ferramenta faz, e que a secao 5 do contrato chama de superficie de primeira
classe — servia isto:

    Localiza a peca de reposicao que o fabricante declarou compativel com um
    modelo de robo aspirador: filtro, escova lateral, escova principal, mop e
    bateria, com o codigo do fabricante [...]. Cobre 71 pares peca x modelo em
    5 marcas.

CINCO tipos. O seletor oferecia SEIS desde 13/09, quando o reservatorio entrou
com quatro pecas declaradas, e a varredura de cobertura ja contava 198 celulas
como "33 modelos x 6 tipos". A frase estava um dia inteira errada.

O QUE FAZ ESTE DEFEITO SER DE FAMILIA, E NAO DESCUIDO: a lista digitada estava
COLADA A DOIS NUMEROS COMPUTADOS. Os "71 pares" e as "5 marcas" da mesma frase
saem do banco e sempre sairam. Numero computado ao lado de lista digitada faz a
lista PARECER medida — e ninguem reconfere o que parece medido. E a mesma
familia do numero de tela digitado que esta ilha ja pagou duas vezes.

E HAVIA TRES COPIAS DA MESMA LISTA, nao duas:
  1. `vocabularios.tipo_de_peca`, no esquema — a fonte.
  2. `TIPOS_CONSULTAVEIS`, digitada dentro de ferramentas/cobertura-r1.py, sob um
     comentario que dizia "vocabulario de tipo_de_peca do esquema, menos 'kit'".
     O arquivo DESCREVIA a derivacao e IMPLEMENTAVA uma copia.
  3. a frase em portugues, digitada dentro do sprintf do snippet — a que
     envelheceu.
A copia 2 estava certa por sorte no dia da medicao; a 3 nao. Copia de lista
dentro de regua e o defeito que a secao 26.2 nomeia com todas as letras.

O QUE A BATERIA COBRE, e ela cobre os DOIS sentidos do erro. Uma regua que so
conferisse "todo tipo ofertado aparece na frase" seria atendida por uma frase
que nomeia tipos A MAIS — o caso simetrico, e o pior dos dois, porque promete a
um modelo de linguagem uma faixa que a pagina recusa. Por isso ha mutacao dos
dois lados, e ha a que produz o mundo pelo ESQUEMA: tipo novo nascendo.
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

# A peca que a bateria reclassifica para dar a PRIMEIRA peca ao tipo novo. E um
# reservatorio, e sobram outros dois do mesmo tipo no banco: assim o tipo antigo
# continua ofertado e a unica mudanca no seletor e o tipo NOVO aparecendo.
ALVO_RECLASSIFICAR = 'wap-fw008543'

# A LINHA VIVA do snippet, a que passou a derivar a lista do banco. Toda mutacao
# que mexe na frase parte dela, e _trocar() conta as ocorrencias: se uma
# refatoracao mudar esta linha, a bateria ACUSA em vez de ficar verde por nao
# medir. Foi assim que a bateria do artigo do publicador pegou a propria inercia
# em 14/09.
LINHA_DERIVADA = (
    "\t\t\trobometria_r1_lista( array_map( 'robometria_r1_nome_do_tipo', "
    "(array) $d['tipos'] ) ),"
)


def _ler(base, rel):
    with open(os.path.join(base, rel), encoding='utf-8') as f:
        return f.read()


def _gravar(base, rel, texto):
    with open(os.path.join(base, rel), 'w', encoding='utf-8') as f:
        f.write(texto)


def _trocar(base, rel, antigo, novo, vezes=1):
    """Troca texto exigindo que o alvo exista e seja unico.

    Mutacao que nao acha o alvo e mutacao INERTE — passa por 'reprovou' sem ter
    mexido em nada. Aqui o alvo e contado, nunca substituido em silencio."""
    texto = _ler(base, rel)
    achadas = texto.count(antigo)
    if achadas != vezes:
        raise AssertionError(
            'o alvo aparece %d vez(es) em %s, esperava %d — mutacao INERTE'
            % (achadas, rel, vezes))
    _gravar(base, rel, texto.replace(antigo, novo))


def _esquema(base):
    with open(os.path.join(base, ESQUEMA), encoding='utf-8') as f:
        return json.load(f)


def _gravar_esquema(base, e):
    with open(os.path.join(base, ESQUEMA), 'w', encoding='utf-8') as f:
        json.dump(e, f, ensure_ascii=False, indent=1)
        f.write('\n')


# --------------------------------------------------------------- AS MUTACOES
def _frase_volta_a_ser_digitada(base):
    """O DEFEITO ORIGINAL, exatamente como estava no ar ate hoje: a lista de
    cinco tipos digitada dentro do sprintf, sem o reservatorio."""
    _trocar(base, SNIPPET, LINHA_DERIVADA,
            "\t\t\t'filtro, escova lateral, escova principal, mop e bateria',")


def _frase_digitada_certa_hoje(base):
    """A PORTA DOS FUNDOS, e e a mutacao mais importante desta bateria — foi ela
    que mostrou, na primeira passada, que a regua escrita hoje ainda nao a
    pegava. A lista volta a ser digitada com os SEIS tipos de hoje, ou seja
    CERTA no momento em que se escreve; e ai a bateria MOVE O MUNDO por baixo
    dela, reclassificando uma peca para um tipo novo.

    Nao ha como distinguir uma lista digitada de uma derivada olhando so a saida
    de hoje: as duas produzem o mesmo texto. So o mundo se mexendo separa as
    duas. E por isso esta prova mora AQUI, na bateria, e nao no teste estatico —
    e por isso ela reproduz, passo a passo, o defeito de verdade: a frase estava
    certa em 12/09, o reservatorio entrou em 13/09, e ela envelheceu calada."""
    _mundo_do_tipo_novo_com_peca(base)
    _trocar(base, SNIPPET, LINHA_DERIVADA,
            "\t\t\t'filtro, escova lateral, escova principal, mop, bateria e "
            "reservatório',")


def _frase_promete_tipo_a_mais(base):
    """O LADO SIMETRICO, e o pior dos dois. A frase nomeia um tipo que o seletor
    NAO oferece. Para um modelo de linguagem isso nao e lista velha: e promessa
    de faixa que a pagina recusa quando alguem chega. Errar para mais custa a
    confianca que a ilha inteira existe para ter."""
    _trocar(base, SNIPPET, LINHA_DERIVADA,
            "\t\t\trobometria_r1_lista( array_merge( array_map( "
            "'robometria_r1_nome_do_tipo', (array) $d['tipos'] ), "
            "array( 'kit' ) ) ),")


def _referencia_volta_a_digitar(base):
    """A COPIA 2 DE VOLTA: TIPOS_CONSULTAVEIS digitada dentro da referencia, com
    os cinco de ontem. E o mesmo defeito uma camada abaixo — e nesta camada ele
    nao para na frase: a varredura passaria a medir cinco faixas, o seletor a
    oferecer cinco, e a cobertura publicada na metodologia mudaria de numero sem
    que nenhuma peca tivesse saido do banco."""
    _trocar(base, REFERENCIA,
            "TIPOS_CONSULTAVEIS = [t for t in VOC_TIPO if t not in _excluidos]",
            "TIPOS_CONSULTAVEIS = ['filtro', 'escova lateral', "
            "'escova principal', 'mop', 'bateria']")


def _esquema_perde_a_regra(base):
    """PRODUZ O MUNDO PELO ESQUEMA, e nenhum dado fica errado: some a chave
    `tipos_consultaveis_na_r1`, de onde a referencia deriva as faixas. A 26.2
    exige que a trava reprove quando a LISTA SOME — regua que cai para "nada a
    cobrar" no dia em que o dado falta aprova tudo em silencio. Aqui seria pior
    que aprovar: a varredura mediria zero faixa e imprimiria cobertura vazia com
    cara de banco vazio."""
    e = _esquema(base)
    if 'tipos_consultaveis_na_r1' not in e:
        raise AssertionError('o esquema ja nao tem a chave — a mutacao seria inerte')
    del e['tipos_consultaveis_na_r1']
    _gravar_esquema(base, e)


def _esquema_exclui_tipo_inexistente(base):
    """A exclusao que nao exclui nada: `excluidos` passa a nomear um tipo que nao
    esta no vocabulario. Sem trava isso e silencioso — a derivacao devolve a
    lista inteira, o kit volta a ser consultavel e a R1 ganha uma faixa que a
    26.2 diz que ninguem busca."""
    e = _esquema(base)
    e['tipos_consultaveis_na_r1']['excluidos'] = ['conjunto']
    _gravar_esquema(base, e)


def _mundo_do_tipo_novo(base):
    """PRODUZ O MUNDO QUE A ILHA VAI VIVER. Nasce um tipo no vocabulario — e este
    e o caso real que espera decisao no banco desde 13/09, a tampa de escova com
    codigo proprio publicada pela Xiaomi. Nenhuma peca usa o tipo ainda, entao
    ele entra em `tipos_sem_nenhuma_peca_no_banco` e NAO pode ser prometido pela
    descricao. Sem produzir o mundo, a linha da regua que trata o tipo nao
    ofertado nunca rodaria: ficaria verde por ausencia de contraexemplo."""
    e = _esquema(base)
    if 'tampa de escova' in e['vocabularios']['tipo_de_peca']:
        raise AssertionError('o tipo ja existe — a mutacao seria inerte')
    e['vocabularios']['tipo_de_peca'].append('tampa de escova')
    _gravar_esquema(base, e)


def _mundo_do_tipo_novo_com_peca(base):
    """O MUNDO QUE MOVE A LISTA: o tipo novo nasce E ganha a primeira peca, por
    reclassificacao de uma que ja existe. E o unico jeito de separar lista
    digitada de lista derivada, porque as duas dao o mesmo texto enquanto o
    mundo fica parado. O seletor passa de seis para sete tipos."""
    _mundo_do_tipo_novo(base)
    caminho = os.path.join(base, BANCO)
    with open(caminho, encoding='utf-8') as f:
        d = json.load(f)
    alvo = None
    for r in d['registros']:
        if r['id'] == ALVO_RECLASSIFICAR:
            alvo = r
            break
    if alvo is None:
        raise AssertionError(
            '%s nao esta mais no banco — a mutacao seria inerte' % ALVO_RECLASSIFICAR)
    if alvo['tipo'] == 'tampa de escova':
        raise AssertionError('a peca ja e do tipo novo — a mutacao seria inerte')
    alvo['tipo'] = 'tampa de escova'
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
        f.write('\n')


def _mundo_do_tipo_novo_prometido(base):
    """O mundo acima com o defeito dentro dele: a frase promete o tipo novo, que
    nao tem peca nenhuma. E o caminho pelo qual um tipo entra no vocabulario
    'para ja ir ficando pronto' e vira promessa vazia no JSON-LD antes de
    existir a primeira peca."""
    _mundo_do_tipo_novo(base)
    _trocar(base, SNIPPET, LINHA_DERIVADA,
            "\t\t\trobometria_r1_lista( array_merge( array_map( "
            "'robometria_r1_nome_do_tipo', (array) $d['tipos'] ), "
            "array( 'tampa de escova' ) ) ),")


def _mundo_do_tipo_novo_intacto(base):
    """A UNICA QUE TEM DE PASSAR. O tipo novo no vocabulario, sem peca e sem
    defeito: a derivacao o conta como faixa possivel, a varredura o mede vazio,
    o seletor nao o oferece e a descricao nao o promete. Se a regua reprovasse
    aqui, nascer tipo novo exigiria consertar portao — e o custo de nascer um
    tipo e exatamente o que esta decisao precisa que seja baixo."""
    _mundo_do_tipo_novo(base)


MUTACOES = [
    ('a frase volta a ser digitada, com os cinco de ontem',
     'o defeito que estava NO AR: a descricao em JSON-LD sem o reservatorio',
     _frase_volta_a_ser_digitada, True, True),
    ('a frase volta a ser digitada, CERTA hoje',
     'a porta dos fundos: certa por coincidencia, esperando o proximo tipo para envelhecer calada',
     _frase_digitada_certa_hoje, True, True),
    ('a frase promete um tipo que o seletor nao oferece',
     'o lado simetrico: promessa de faixa que a pagina recusa quando alguem chega',
     _frase_promete_tipo_a_mais, True, True),
    ('a REFERENCIA volta a digitar TIPOS_CONSULTAVEIS',
     'a copia uma camada abaixo: a varredura mediria cinco faixas sem peca nenhuma sair do banco',
     _referencia_volta_a_digitar, True, True),
    ('o ESQUEMA perde a regra de derivacao',
     'PRODUZ O MUNDO: nenhum dado fica errado e a varredura mediria faixa nenhuma',
     _esquema_perde_a_regra, True, True),
    ('o ESQUEMA exclui um tipo que nao existe',
     'exclusao que nao exclui nada: o kit voltaria a ser consultavel em silencio',
     _esquema_exclui_tipo_inexistente, True, True),
    ('MUNDO NOVO (tipo no vocabulario) prometido sem ter peca',
     'sem produzir o mundo, a linha do tipo nao ofertado nunca rodaria — verde por ausencia de contraexemplo',
     _mundo_do_tipo_novo_prometido, True, True),
    ('MUNDO NOVO (tipo no vocabulario) intacto — esta TEM de passar',
     'nascer tipo novo nao pode exigir conserto de portao, ou a decisao fica cara e ninguem a toma',
     _mundo_do_tipo_novo_intacto, True, False),
]


def main():
    corretas = 0
    erradas = []

    print('Mutacoes deliberadas na lista de tipos — todas reprovam, menos a ultima\n')

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
    print('Todas as travas reprovam o que tem de reprovar, e nascer tipo novo nao reprova nada.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
