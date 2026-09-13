#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra de proposito a frase da divergencia e exige REPROVACAO do teste-r1.

    python3 ferramentas/mutacoes-divergencia.py

POR QUE ESTE ARQUIVO EXISTE
---------------------------
"A PROVA DE QUE UMA TRAVA REPROVA E PARTE DO BLOCO" (secao 8 do ARQUIPELAGO.md).
A secao 16 do teste-r1.php nasceu verde, o que e bom sinal sobre o banco de hoje e
nenhum sinal sobre ela.

E O DEFEITO QUE ELA EXISTE PARA PEGAR JA ESTEVE NO AR. Ate 13/09/2026 a cauda da
frase da R1 era fixa — "Dois canais do fabricante discordam sobre o alcance desta
peca" — e o titulo do bloco dizia "O que os canais do fabricante discordam sobre
X". As duas frases eram verdadeiras por ACIDENTE do banco: as sete divergencias de
peca que existiam vinham todas de canal de fabricante. No dia em que entrou o
primeiro registro cujos canais divergentes eram marketplace e varejista (o
recipiente FW008543 da WAP), as duas passaram a emprestar a autoridade do
FABRICANTE a quem so revende — que e o defeito exato que esta ilha existe para nao
cometer. Oito portoes seguiram verdes, porque nenhum deles media QUEM diverge.

AS MUTACOES QUE PRODUZEM O MUNDO SAO A METADE QUE IMPORTA. O banco de hoje tem
registro do lado 'fabricante' e registro do lado 'terceiro', e NENHUM misto — e
uma mutacao que so estragasse o banco de hoje deixaria o ramo do meio sem medicao
para sempre. Por isso duas delas nao quebram nada: elas CRIAM a situacao (um canal
que fala pela marca ao lado de um que nao fala) e exigem que a regua a apanhe.

A ULTIMA MUTACAO TEM DE PASSAR: mundo intacto que reprova e falso-positivo, e
regua que reprova tudo "pega" qualquer defeito sem medir nenhum.
"""

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PECAS = 'dados/pecas.json'
ESQUEMA = 'dados/esquema-banco.json'
SNIPPET = 'snippets/robometria-r1.php'

WAP = 'wap-fw008543'      # o unico registro cujos canais divergentes revendem
MULTI = 'multi-pr10205'   # divergencia entre dois canais do proprio fabricante


def editar_json(arquivo, mudar):
    def aplicar(base_dir):
        caminho = os.path.join(base_dir, arquivo)
        with open(caminho, encoding='utf-8') as fh:
            doc = json.load(fh)
        mudar(doc)
        with open(caminho, 'w', encoding='utf-8') as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=1)
            fh.write('\n')
    return aplicar


def registro(doc, id_do_registro):
    alvo = [r for r in doc['registros'] if r['id'] == id_do_registro]
    if len(alvo) != 1:
        raise AssertionError('o registro %r nao esta unico no banco: %d'
                             % (id_do_registro, len(alvo)))
    return alvo[0]


def trocar_no_snippet(de, para, vezes=1):
    """Edita o PHP publicado. `vezes` e DECLARADO e conferido: alvo que aparece
    um numero diferente de vezes do que esta escrito aqui muda de natureza, e a
    mutacao para em vez de editar menos (ou mais) do que anuncia."""
    def aplicar(base_dir):
        caminho = os.path.join(base_dir, SNIPPET)
        with open(caminho, encoding='utf-8') as fh:
            texto = fh.read()
        achados = texto.count(de)
        if achados != vezes:
            raise AssertionError(
                'a mutacao esperava %d ocorrencia(s) de %r no snippet e achou %d. '
                'Mutacao que nao morde e teste verde com outro nome.'
                % (vezes, de[:60], achados))
        with open(caminho, 'w', encoding='utf-8') as fh:
            fh.write(texto.replace(de, para))
    return aplicar


# ------------------------------------------------------- MUTACOES QUE ESTRAGAM
def frase_volta_a_ser_fixa(base_dir):
    """O mundo de ontem, literal: a cauda vira de novo a frase digitada."""
    caminho = os.path.join(base_dir, SNIPPET)
    with open(caminho, encoding='utf-8') as fh:
        texto = fh.read()
    novo, n = re.subn(
        r"\$frase \.= ' ' \. robometria_r1_frase_da_divergencia\( \$item\['peca'\] \);",
        "$frase .= ' Dois canais do fabricante discordam sobre o alcance desta "
        "peça: vale o conjunto MAIS ESTREITO, e as duas declarações estão "
        "publicadas com as suas datas.';",
        texto)
    if n != 1:
        raise AssertionError('a chamada da cauda da divergencia nao foi achada '
                             'uma unica vez no snippet: %d' % n)
    with open(caminho, 'w', encoding='utf-8') as fh:
        fh.write(novo)


def intacto(base_dir):
    return None


MUTACOES = [
    (
        'a cauda da frase volta a ser a frase FIXA de ontem',
        'e o defeito literal que este bloco consertou: "Dois canais do fabricante" '
        'dito sobre tres anuncios de revendedor, com o numero digitado junto',
        frase_volta_a_ser_fixa,
        False,
    ),
    (
        'o lado passa a ser lido do NOME do canal, e nao do degrau',
        'a heuristica por vizinhanca que a secao 8 do contrato proibe: funcionaria '
        'hoje, porque os canais de revenda tem "marketplace" escrito no nome, e '
        'erraria calada no primeiro canal cujo nome nao denuncia o que ele e',
        trocar_no_snippet(
            "$lados[ ! empty( $dv['fala_pela_marca'] ) ? 'fabricante' : 'terceiro' ] = true;",
            "$lados[ false === stripos( $dv['canal'], 'marketplace' ) ? 'fabricante' : 'terceiro' ] = true;"),
        False,
    ),
    (
        'o titulo do bloco volta a nomear o fabricante em toda divergencia',
        'o titulo e a linha mais lida do bloco, e ele dizia "os canais do '
        'fabricante" para anuncio de marketplace',
        trocar_no_snippet(
            "$titulo = 'O que canais de fora do fabricante declaram sobre ';",
            "$titulo = 'O que os canais do fabricante discordam sobre ';"),
        False,
    ),
    (
        'o numero da frase volta a ser digitado',
        'a cicatriz do numero de tela, ja paga duas vezes nesta ilha: a frase diria '
        '"Dois" sobre tres canais',
        trocar_no_snippet(
            "robometria_r1_numeral( $n ), $canal, $declara, $total\n\t\t);\n\t}\n\tif ( 'terceiro' === $lado ) {",
            "'Dois', $canal, $declara, $total\n\t\t);\n\t}\n\tif ( 'terceiro' === $lado ) {"),
        False,
    ),
    (
        'a origem some das divergencias do banco',
        'sem ela o gerador nao tem o que carregar e o snippet volta a adivinhar; a '
        'trava tem de gritar em vez de cair para "nada a cobrar"',
        editar_json(PECAS, lambda d: [dv.pop('origem', None)
                                      for r in d['registros']
                                      for dv in (r.get('divergencias') or [])]),
        False,
    ),
    (
        'a fronteira some do esquema (fala_pela_marca)',
        'regua que le a propria lista de um arquivo de dados aprova tudo em '
        'silencio no dia em que o arquivo perde a chave — a mutacao da secao 26.2 '
        'do contrato, aplicada a este campo',
        editar_json(ESQUEMA, lambda d: [n.pop('fala_pela_marca', None)
                                        for n in d['escada_de_fontes']['niveis']]),
        False,
    ),
    # ------------------------------------------------ MUTACOES QUE PRODUZEM O MUNDO
    (
        'PRODUZ O MUNDO: a divergencia do fabricante ganha um canal de revenda',
        'o multi-pr10205 e hoje 100% canal de fabricante. Com um anuncio junto ele '
        'vira MISTO, e a frase nao pode mais dizer "do fabricante" — este ramo nao '
        'existe no banco de hoje e sem produzi-lo ele nunca seria medido',
        editar_json(PECAS, lambda d: registro(d, MULTI)['divergencias'].append({
            'canal': 'uma loja qualquer',
            'origem': 'marketplace-anuncio',
            'conjunto_declarado': ['HO041', 'OB010'],
            'titulo_na_fonte': 'anuncio de terceiro',
            'url': 'https://exemplo.invalido/anuncio',
            'verificado_em': '2026-09-13',
        })),
        False,
    ),
    (
        'PRODUZ O MUNDO: o degrau do marketplace passa a falar pela marca',
        'nenhum registro do banco muda — muda a FRONTEIRA, no esquema. A frase do '
        'FW008543 passaria a chamar tres anuncios de canais do fabricante, e e '
        'exatamente esse o defeito de atribuicao que a secao 16 mede',
        editar_json(ESQUEMA, lambda d: [
            n.__setitem__('fala_pela_marca', True)
            for n in d['escada_de_fontes']['niveis']
            if n['origem'] in ('marketplace-anuncio', 'varejo-especializado')]),
        False,
    ),
    (
        'MUNDO INTACTO — esta tem de PASSAR',
        'regua que reprova o mundo sadio pega qualquer defeito sem medir nenhum',
        intacto,
        True,
    ),
]


def rodar(cmd, cwd, ambiente=None):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, env=ambiente)


def medir(base_dir):
    """Regera o catalogo da R1 e roda o teste-r1.php inteiro.

    Falha de geracao conta como REPROVACAO: o que importa aqui e que o defeito
    NAO passe, e ilha que nao monta tambem nao publica.
    """
    r = rodar([sys.executable, 'ferramentas/gerar-r1.py', '--gravar'], base_dir)
    if r.returncode != 0:
        return r.returncode, 'gerar-r1.py falhou (a mutacao derrubou a geracao)'
    r = rodar(['php', 'ferramentas/teste-r1.php', '.'], base_dir)
    linhas = [l for l in r.stdout.strip().splitlines() if l.strip()]
    return r.returncode, (linhas[-1] if linhas else '(sem saida)')


def copiar(destino):
    for item in ('dados', 'ferramentas', 'snippets', 'manifest.json', 'ARVORE.md'):
        origem = os.path.join(RAIZ, item)
        alvo = os.path.join(destino, item)
        if os.path.isdir(origem):
            shutil.copytree(origem, alvo)
        else:
            shutil.copy2(origem, alvo)


def main():
    print('MUTACOES DA DIVERGENCIA — quem diverge decide a frase, e isso se mede')
    print('=' * 78)
    erros = 0
    for nome, porque, aplicar, tem_de_passar in MUTACOES:
        with tempfile.TemporaryDirectory() as tmp:
            base = os.path.join(tmp, 'ilha')
            os.makedirs(base)
            copiar(base)
            aplicar(base)
            codigo, ultima = medir(base)
        passou = codigo == 0
        certo = passou is tem_de_passar
        if not certo:
            erros += 1
        print('  %s %s' % ('ok    ' if certo else 'ERRO  ', nome))
        print('         %s' % ultima)
        if not certo:
            print('         esperado: %s' % ('PASSAR' if tem_de_passar else 'REPROVAR'))
            print('         por que: %s' % porque)
    print('=' * 78)
    if erros:
        print('%d de %d mutacoes NAO se comportaram como declarado.'
              % (erros, len(MUTACOES)))
        sys.exit(1)
    print('%d de %d: toda trava foi vista reprovando, e o mundo sadio passou.'
          % (len(MUTACOES), len(MUTACOES)))


if __name__ == '__main__':
    main()
