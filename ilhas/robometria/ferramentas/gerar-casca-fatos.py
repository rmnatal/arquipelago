#!/usr/bin/env python3
"""Deriva do banco os fatos que a CASCA publica sobre si mesma.

    python3 ferramentas/gerar-casca-fatos.py            # mostra
    python3 ferramentas/gerar-casca-fatos.py --gravar   # escreve dados/casca-fatos.json

POR QUE ESTE ARQUIVO EXISTE
---------------------------
A pagina de metodologia publica a escada de fontes com uma coluna "Temos hoje",
e essa coluna e uma AFIRMACAO SOBRE O BANCO: ela diz em quais degraus a ilha se
apoia e quais estao vazios. Ate 11/09/2026 ela estava digitada dentro do
snippet — `'existe' => false` no nivel 2 — enquanto QUATRO fontes do banco se
declaravam nivel 2. As duas metades nunca se falavam, entao nenhuma podia
corrigir a outra, e a contradicao ficou no ar sem que ninguem tivesse como
perceber.

E o mesmo defeito que o bloco 5 ja tinha nomeado no artigo-ancora: numero que e
a afirmacao da pagina nao pode estar digitado no HTML, porque passa a mentir em
silencio no dia em que o banco muda. A saida e a mesma: o gerador deriva o fato,
o snippet so escreve a frase.

POR QUE UM ARQUIVO NOVO, E NAO LER O BANCO NO SITE
--------------------------------------------------
`pecas.json` e `modelos-robo.json` tem `publicar: false` de proposito — sao 245
KB de banco cru que o site nao precisa carregar em option. Entao o fato viaja
derivado e pequeno, como `a1-fatos.json` e `a2-fatos.json` ja viajam.

A CONTAGEM E SO DE REGISTRO PUBLICAVEL, e isso importa: a coluna fala do que a
ilha publica, nao do que ela guarda. Fonte presa a registro excluido do banco
nao sustenta nada na tela e nao pode aparecer na confissao.

E ELA LE TODAS AS ORIGENS, NAO SO O BANCO DE PECAS
---------------------------------------------------
A primeira versao deste gerador contava `pecas.json` e `modelos-robo.json` e
declarava, com ar de medicao, que a ilha nao tinha fonte editorial — quando ela
tem seis, em `constantes.json`, usadas pela R2 em TODA resposta de Pa. Teria
trocado um numero digitado errado por um numero medido errado, que e pior,
porque este parece conferido.

As constantes nao carregam `nivel`, carregam `tipo`. A ponte entre os dois nao
mora aqui: mora no esquema, em `escada_de_fontes.onde_moram_as_fontes`, para ser
uma regra declarada e revisavel em vez de um dicionario escondido numa
ferramenta.
"""

import collections
import json
import sys

ARQUIVOS = ('dados/pecas.json', 'dados/modelos-robo.json')
ESQUEMA = 'dados/esquema-banco.json'


def main():
    gravar = '--gravar' in sys.argv

    with open(ESQUEMA, encoding='utf-8') as f:
        escada = json.load(f)['escada_de_fontes']

    contagem = collections.Counter()
    por_origem = collections.Counter()
    fora_do_vocabulario = []

    origem_do_nivel = {d['nivel']: d['origem'] for d in escada['niveis']}

    for arquivo in ARQUIVOS:
        with open(arquivo, encoding='utf-8') as f:
            banco = json.load(f)
        for registro in banco['registros']:
            if registro.get('status') != 'publicavel':
                continue
            for fid, fonte in (registro.get('fontes') or {}).items():
                nivel = fonte.get('nivel')
                contagem[nivel] += 1
                por_origem[(nivel, fonte.get('origem'))] += 1
                if origem_do_nivel.get(nivel) != fonte.get('origem'):
                    fora_do_vocabulario.append(
                        '%s/%s/%s: nivel %s declara origem %r, e a escada diz %r'
                        % (arquivo, registro['id'], fid, nivel,
                           fonte.get('origem'), origem_do_nivel.get(nivel))
                    )

    # As constantes: mesma escada, outro arquivo, e a ponte tipo -> nivel e
    # declarada no esquema, nao aqui.
    onde = escada['onde_moram_as_fontes']
    ponte = onde['tipo_de_constante_para_nivel']
    with open('dados/constantes.json', encoding='utf-8') as f:
        constantes = json.load(f)['constantes']
    for constante in constantes:
        if constante.get('status') != 'publicavel':
            continue
        tipo = constante.get('tipo')
        if tipo not in ponte:
            fora_do_vocabulario.append(
                'dados/constantes.json/%s: tipo %r nao esta na ponte declarada no esquema'
                % (constante.get('id'), tipo)
            )
            continue
        nivel = ponte[tipo]
        if nivel is None:
            continue
        contagem[nivel] += 1
        por_origem[(nivel, origem_do_nivel.get(nivel))] += 1

    if fora_do_vocabulario:
        print('RECUSADO: fonte com nivel e origem que nao batem com a escada.')
        for linha in fora_do_vocabulario:
            print('  ' + linha)
        return 2

    niveis = []
    for degrau in escada['niveis']:
        niveis.append({
            'nivel': degrau['nivel'],
            'origem': degrau['origem'],
            'fontes_no_banco': contagem.get(degrau['nivel'], 0),
            'existe_hoje': contagem.get(degrau['nivel'], 0) > 0,
        })

    fatos = {
        'id': 'casca-fatos',
        'ilha': 'robometria',
        'entidade': 'medicao',
        'gerado_por': 'ferramentas/gerar-casca-fatos.py',
        'gerado_em': '2026-09-11',
        'o_que_e': (
            'Fatos que a casca publica sobre o proprio banco. Hoje: a coluna "Temos hoje" da '
            'escada de fontes, na pagina de metodologia. Contagem so de registro publicavel.'
        ),
        'por_que_derivado': (
            'Ate 11/09/2026 a coluna estava digitada dentro do snippet e contradizia o banco: '
            'ela dizia que a ilha nao tinha nenhuma fonte de nivel 2 enquanto quatro fontes se '
            'declaravam nivel 2. Afirmacao da pagina sobre o banco se conta no banco.'
        ),
        'onde_foi_contado': onde['arquivos_com_fontes_de_nivel_explicito'] + ['dados/constantes.json'],
        'total_de_fontes': sum(contagem.values()),
        'niveis': niveis,
    }

    for n in niveis:
        print('  nivel %d %-24s %3d fonte(s)  existe_hoje=%s'
              % (n['nivel'], n['origem'], n['fontes_no_banco'], n['existe_hoje']))
    print('  total: %d fontes em registro publicavel' % fatos['total_de_fontes'])

    if gravar:
        with open('dados/casca-fatos.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(fatos, ensure_ascii=False, indent=2) + '\n')
        print('\ngravado: dados/casca-fatos.json')
    else:
        print('\n(nada gravado — rode com --gravar)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
