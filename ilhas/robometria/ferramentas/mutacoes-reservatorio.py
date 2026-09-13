#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra de proposito o que o bloco do reservatorio entregou e exige REPROVACAO.

    python3 ferramentas/mutacoes-reservatorio.py

POR QUE ESTE ARQUIVO EXISTE
---------------------------
"A PROVA DE QUE UMA TRAVA REPROVA E PARTE DO BLOCO" (secao 8 do ARQUIPELAGO.md).
A conferencia `conferir-reservatorio-no-ar.py` nasceu verde na primeira rodada —
o que e bom sinal sobre o site e nenhum sinal sobre ela. Regua que nunca foi vista
falhar e regua nao medida, e nesta ilha cinco travas ja passaram verdes medindo a
si mesmas.

O PROBLEMA ESPECIFICO DE UMA REGUA DE AR, e como ele se resolve
---------------------------------------------------------------
Conferencia no ar nao se muta: o site e um so, e fabricar o defeito nele seria
publicar defeito para depois medi-lo — exatamente o que nenhum portao pode
exigir. A saida foi separar o que a regua AFIRMA do lugar de onde ela LE. Com
RBM_BANCADA no ambiente, ela le cada estado de um arquivo renderizado em vez da
rede; aqui, cada mutacao monta uma ilha inteira num diretorio temporario, quebra
UMA coisa, regera o catalogo da R1, renderiza os quatro estados e roda a MESMA
regua, sem uma linha dela mudada. O site nao e tocado.

A ENTRADA VARIAVEL PRECISOU DE UM RENDER NOVO. A R1 responde por consulta, e o
render solto so sabia produzir o caso-ANCORA — por isso os estados de consulta
nunca tinham sido medidos fora do ar. O `render-para-teste.php` ganhou dois
argumentos (modelo e tipo) que entram pelo filtro `robometria_r1_entrada`, que e
o mesmo caminho que o snippet ja oferecia a quem monta a pagina fora do
WordPress. Nao ha $_GET forjado: o teste-r1.php cobra que o snippet nunca toque na
superglobal, e um render que a forjasse mediria um caminho que o site nao usa.

A ULTIMA MUTACAO TEM DE PASSAR, e ela nao e enfeite: mundo intacto que reprova e
falso-positivo, e regua que reprova tudo "pega" qualquer defeito sem medir nenhum.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PECAS = 'dados/pecas.json'

W300 = 'wap-recipiente-de-po-w300'
WSMART = 'wap-fw008024'
W100_W90 = 'wap-fw008543'

# Os quatro estados que a regua le, e o argumento de render de cada um. O nome do
# arquivo e o contrato entre este arquivo e a regua: rbm-r1-<estado>.html.
ESTADOS = (
    ('ancora', None, None),
    ('w300', 'wap-w300', 'reservatorio'),
    ('wsmart', 'wap-wsmart', 'reservatorio'),
    ('erb60', 'electrolux-erb60', 'reservatorio'),
    # OS DOIS ESTADOS DA TERCEIRA PECA (13/09/2026). Sem eles a regua nao acha os
    # arquivos, devolve 000 e REPROVA tudo — inclusive o mundo intacto, que e a
    # unica mutacao que tem de passar. Estado novo na regua e estado novo aqui:
    # foi assim que esta bateria comecou a reprovar pelo motivo errado, e reprovar
    # pelo motivo errado nao prova trava nenhuma.
    ('w100', 'wap-w100', 'reservatorio'),
    ('w90', 'wap-w90', 'reservatorio'),
)


def editar_banco(id_do_registro, mudar):
    """Aplica uma edicao ao pecas.json da copia, pelo id do registro.

    `mudar` recebe o dicionario do registro e o altera no lugar. Se o id nao
    existir, ou existir duas vezes, a mutacao PARA: mutacao que nao encontra o
    alvo edita NADA, e o verde que ela produz e a ilusao que este arquivo existe
    para desfazer.
    """
    def aplicar(base_dir):
        caminho = os.path.join(base_dir, PECAS)
        with open(caminho, encoding='utf-8') as fh:
            doc = json.load(fh)
        alvo = [r for r in doc['registros'] if r['id'] == id_do_registro]
        if len(alvo) != 1:
            raise AssertionError('o registro %r nao esta unico no banco: %d'
                                 % (id_do_registro, len(alvo)))
        mudar(alvo[0])
        with open(caminho, 'w', encoding='utf-8') as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=1)
            fh.write('\n')
    return aplicar


def remover_do_banco(*ids):
    def aplicar(base_dir):
        caminho = os.path.join(base_dir, PECAS)
        with open(caminho, encoding='utf-8') as fh:
            doc = json.load(fh)
        antes = len(doc['registros'])
        doc['registros'] = [r for r in doc['registros'] if r['id'] not in ids]
        if antes - len(doc['registros']) != len(ids):
            raise AssertionError('a mutacao nao removeu os %d registros pedidos'
                                 % len(ids))
        with open(caminho, 'w', encoding='utf-8') as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=1)
            fh.write('\n')
    return aplicar


def intacto(base_dir):
    """O controle: nao mexe em nada."""
    return None


MUTACOES = [
    (
        'as duas pecas de reservatorio saem do banco',
        'e o mundo de ontem: o tipo cai fora do seletor e a frase da ausencia volta. '
        'Se a regua nao reprovar isto, ela nao mede a promessa que a pagina fazia',
        remover_do_banco(W300, WSMART),
        False,
    ),
    (
        'o codigo do WSMART no banco deixa de ser o que a loja publica',
        'codigo derivando do que a fonte declara e o defeito que a R1 nao pode ter: '
        'a pessoa procura a peca pelo que esta escrito na tela',
        editar_banco(WSMART, lambda r: r.__setitem__('codigo_fabricante', 'FW000000')),
        False,
    ),
    (
        'o recipiente do W300 toma emprestado o codigo do irmao do WSMART',
        'a maneira mais barata de esta ilha mentir: a peca sem codigo ganha o do '
        'vizinho e a pagina fica com cara de mais precisa do que a fonte permite',
        editar_banco(W300, lambda r: r.__setitem__('codigo_fabricante', 'FW008024')),
        False,
    ),
    (
        'o recipiente do W300 passa a ser declarado tambem para o ERB60',
        'compatibilidade inventada entre marcas, que e a unica coisa que esta ilha '
        'vende — e o estado NEGATIVO da regua existe exatamente para isto',
        editar_banco(W300, lambda r: r['compatibilidade'].append({
            'modelo': 'electrolux-erb60',
            'codigo_declarado': 'ERB60',
            'variante_de_hardware': None,
            'selo': 'declarada_fabricante',
            'fonte': 'f-peca',
        })),
        False,
    ),
    (
        'o titulo do recipiente do W300 deixa de ser o publicado pela loja',
        'a peca sem codigo e identificada pelo TITULO, e titulo que nao e o da fonte '
        'manda a pessoa procurar uma coisa que nao esta a venda com esse nome',
        editar_banco(W300, lambda r: r.__setitem__(
            'nome_na_fonte', 'Recipiente de Pó para robô aspirador WAP')),
        False,
    ),
    (
        'a terceira peca sai do banco',
        'e o mundo de ontem a esta execucao: o W100 e o W90 voltam ao vazio da R1 '
        'e as duas consultas passam a recusar. Sem esta mutacao, os dois estados '
        'novos da regua nunca foram vistos reprovando',
        remover_do_banco(W100_W90),
        False,
    ),
    (
        'a peca deixa de ser declarada para o W90 e fica so no W100',
        'a peca e UMA e os modelos sao DOIS. Sem esta, bastaria o segundo par sumir '
        'do banco para a bancada seguir verde medindo so o primeiro',
        editar_banco(W100_W90, lambda r: r.__setitem__(
            'compatibilidade', [c for c in r['compatibilidade']
                                if c['modelo'] != 'wap-w90'])),
        False,
    ),
    (
        'a compatibilidade do varejo vira declaracao do fabricante (o W100C entra)',
        'a EXTENSAO POR VIZINHANCA, que e a recusa central deste bloco: tres '
        'revendedores anunciam esta peca para o W100C e o fabricante nao a declara. '
        'Se ela entrasse, um terceiro modelo sairia do vazio hoje — e a pagina '
        'recomendaria uma peca com a autoridade de quem nunca a declarou',
        editar_banco(W100_W90, lambda r: r['compatibilidade'].append({
            'modelo': 'wap-w100c',
            'codigo_declarado': 'WAP Robot W100C',
            'variante_de_hardware': None,
            'selo': 'declarada_fabricante',
            'fonte': 'f-peca',
        })),
        False,
    ),
    (
        'o quadro de divergencia some do banco',
        'a regra do conjunto mais estreito so e verificavel por quem enxerga o que '
        'foi descartado. Sem o quadro, a pagina pede confianca em vez de dar prova '
        '— e a frase que atribui a divergencia a quem revende fica sem lastro',
        editar_banco(W100_W90, lambda r: r.__setitem__('divergencias', [])),
        False,
    ),
    (
        'MUNDO INTACTO — esta tem de PASSAR',
        'regua que reprova o mundo sadio pega qualquer defeito sem medir nenhum',
        intacto,
        True,
    ),
]

def rodar(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)


def medir(base_dir):
    """Regera o catalogo, renderiza os quatro estados e roda a regua.

    Devolve (codigo_de_saida, ultima_linha_util). Falha de geracao ou de render
    conta como REPROVACAO: ilha que nao monta e ilha quebrada, e a regua nunca
    chega a ser chamada — o que importa aqui e que o defeito NAO passe.
    """
    r = rodar([sys.executable, 'ferramentas/gerar-r1.py', '--gravar'], base_dir)
    if r.returncode != 0:
        return r.returncode, 'gerar-r1.py falhou'
    saida = os.path.join(base_dir, '_estados')
    os.makedirs(saida, exist_ok=True)
    for estado, modelo, tipo in ESTADOS:
        cmd = ['php', 'ferramentas/render-para-teste.php', '.', 'robometria_r1']
        if modelo:
            cmd += [modelo, tipo]
        r = rodar(cmd, base_dir)
        if r.returncode != 0 or not r.stdout:
            return 1, 'render do estado %s falhou' % estado
        with open(os.path.join(saida, 'rbm-r1-%s.html' % estado), 'w',
                  encoding='utf-8') as fh:
            fh.write(r.stdout)
    ambiente = dict(os.environ, RBM_BANCADA=saida)
    r = subprocess.run([sys.executable, 'ferramentas/conferir-reservatorio-no-ar.py'],
                       cwd=base_dir, capture_output=True, text=True, env=ambiente)
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
    print('MUTACOES DO RESERVATORIO — a regua de ar vista reprovando, sem tocar no site')
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
    print('=' * 78)
    if erros:
        print('%d de %d mutacoes NAO se comportaram como declarado.' % (erros, len(MUTACOES)))
        sys.exit(1)
    print('%d de %d: toda trava foi vista reprovando, e o mundo sadio passou.'
          % (len(MUTACOES), len(MUTACOES)))


if __name__ == '__main__':
    main()
