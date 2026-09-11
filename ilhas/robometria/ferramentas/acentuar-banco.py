#!/usr/bin/env python3
"""Restaura os acentos dos campos do banco que vao para a TELA.

    python3 ferramentas/acentuar-banco.py            # so mostra o que mudaria
    python3 ferramentas/acentuar-banco.py --gravar   # grava o banco e o livro-razao

POR QUE ISTO EXISTE
-------------------
O banco da Robometria nasceu inteiro em ASCII. Enquanto ele so alimentava
medicao, acento faltando nao custava nada. Com a R1 e a R2 no ar, esse texto e
CITADO dentro da resposta publicada, e a mesma frase da tela passou a sair
metade certa e metade errada:

    "... e a peça certa depende da sua: bateria — o fabricante vende a peca
     PR10127 identificada como 'Versao A'"

"peça" ali foi escrita pela ilha; "peca" e "Versao" vieram do banco. Numa ilha
cuja secao 5 do ARQUIPELAGO.md diz que ser citada pela IA vale tanto quanto
ranquear, servir portugues errado no proprio trecho que prova a procedencia
custa exatamente a coisa que a ilha vende.

O QUE ELE NAO FAZ, E ESSA E A PARTE QUE IMPORTA
-----------------------------------------------
Ele NAO reescreve transcricao. `nome_na_fonte` e `titulo_na_fonte` sao citacao
do texto do fabricante, e a rede desta nuvem nao alcanca fabricante nenhum
(medido de novo em 11/09/2026: `000` em mi.com.br e wap.ind.br) — entao nao ha
como reler a fonte primaria nesta execucao para conferir o que ela escreve.

Por isso a operacao e deliberadamente pequena e PROVAVEL: so diacritico. Toda
mudanca passa pela trava `sem_acento(depois) == antes`, e o arquivo se recusa a
gravar se alguma falhar. Isso torna impossivel, por construcao, que este
programa troque uma palavra, um codigo de peca, um numero ou um modelo: o que
ele produz, quando reduzido a ASCII, e byte a byte o que ja estava no banco.

E como diacritico restaurado nao e diacritico LIDO na fonte, cada mudanca fica
registrada em `dados/acentuacao-restaurada.json`, com arquivo, registro, campo,
antes e depois. Esse arquivo e a lista de conferencia de quem reler os manuais
no dia em que a rede abrir (item (c) do bloco 3c) — nao um log.

O MAPA E BOUNDED DE PROPOSITO
-----------------------------
Ele cobre as palavras que aparecem nos campos que a varredura de
`ferramentas/varrer-corpo.php` mediu na tela, e nada alem. Palavra ambigua
(o "e" que pode ser "é", o "a" que pode ser "à") fica de fora: acertar por
adivinhacao nao e acertar. Quem segura a regra daqui para a frente e
`ferramentas/teste-acentuacao.php`, que le o CORPO servido e escreve a propria
regua — nao esta lista.
"""

import json
import re
import sys
import unicodedata

# Campos que a varredura de 11/09/2026 mediu chegando ao corpo servido.
CAMPOS_DE_TELA = (
    'nome_na_fonte',
    'titulo_na_fonte',
    'publicador',
    'linha',
    'nome',
    'nome_comercial',
    'o_que_muda',
    'canal',
    'conjunto_declarado',
)

# ASCII -> acentuado. So palavra inequivoca em pt-BR; nada de monossilabo
# ambiguo. A forma com inicial maiuscula e a toda-maiuscula entram como
# entradas proprias, porque "Robo" e "ROBO" nao sao o mesmo caso de caixa.
MAPA = {
    'ate': 'até',
    'AGUA': 'ÁGUA',
    'Automatica': 'Automática',
    'Compativel': 'Compatível',
    'endereco': 'endereço',
    'especificacoes': 'especificações',
    'Especificacoes': 'Especificações',
    'FUNCOES': 'FUNÇÕES',
    'INSTRUCOES': 'INSTRUÇÕES',
    'lamina': 'lâmina',
    'Lavavel': 'Lavável',
    'Mao': 'Mão',
    'nao': 'não',
    'pagina': 'página',
    'peca': 'peça',
    'Po': 'Pó',
    'propria': 'própria',
    'proprio': 'próprio',
    'Recarregavel': 'Recarregável',
    'Removivel': 'Removível',
    'RESERVATORIO': 'RESERVATÓRIO',
    'robo': 'robô',
    'Robo': 'Robô',
    'ROBO': 'ROBÔ',
    'Robos': 'Robôs',
    'titulo': 'título',
    'usuario': 'usuário',
    'versao': 'versão',
    'Versao': 'Versão',
}

ARQUIVOS = ('dados/pecas.json', 'dados/modelos-robo.json', 'dados/marcas.json')

# A indentacao dos tres arquivos, conferida por ida-e-volta: reescrever o banco
# sem nenhuma troca devolve byte a byte o mesmo arquivo. E o que faz o diff
# desta execucao mostrar so o que mudou de verdade.
INDENT = 2

# A borda inclui o hifen de proposito: dentro do banco ha endereco de pagina
# citado inteiro ("bateria-para-aspirador-robo-mars-ho041-versao-b--pr8116"),
# e acentuar um pedaco de URL destruiria a evidencia que a citacao existe para
# dar. Palavra colada em hifen nao e tocada.
BORDA_ESQ = r'(?<![0-9A-Za-zÀ-ÿ\-])'
BORDA_DIR = r'(?![0-9A-Za-zÀ-ÿ\-])'
PADRAO = re.compile(
    BORDA_ESQ + '(' + '|'.join(sorted(MAPA, key=len, reverse=True)) + ')' + BORDA_DIR
)


def sem_acento(texto):
    """Tira o DIACRITICO e nada mais.

    A primeira versao disto reduzia a string a ASCII, e a trava reprovou 15
    mudancas corretas: o travessao "—" ja estava no banco ANTES da restauracao,
    e "reduzir a ASCII" o apagava junto com os acentos, fazendo a comparacao
    falhar por um caractere que este programa nunca tocou. Regua errada reprova
    trabalho certo com a mesma cara com que aprova trabalho errado — por isso
    ela desmonta o caractere e joga fora so as marcas combinantes.
    """
    return unicodedata.normalize(
        'NFC',
        ''.join(c for c in unicodedata.normalize('NFD', texto)
                if unicodedata.category(c) != 'Mn'),
    )


def acentuar(texto):
    return PADRAO.sub(lambda m: MAPA[m.group(1)], texto)


def percorrer(no, chave, caminho, saida):
    """Visita todo campo de tela, guardando (caminho, valor) em saida."""
    if isinstance(no, dict):
        for k, v in no.items():
            percorrer(v, k, caminho + '.' + k, saida)
    elif isinstance(no, list):
        for i, v in enumerate(no):
            percorrer(v, chave, caminho + '[%d]' % i, saida)
    elif isinstance(no, str) and chave in CAMPOS_DE_TELA:
        saida.append((caminho, no))


def main():
    gravar = '--gravar' in sys.argv
    livro = []
    recusas = []

    for arquivo in ARQUIVOS:
        with open(arquivo, encoding='utf-8') as f:
            banco = json.load(f)

        for registro in banco['registros']:
            campos = []
            percorrer(registro, None, registro['id'], campos)
            for caminho, antes in campos:
                depois = acentuar(antes)
                if depois == antes:
                    continue
                # A trava: reduzida a ASCII, a string nova tem que ser
                # exatamente a antiga. Se nao for, este programa mudou
                # conteudo, e conteudo nao e trabalho dele.
                if sem_acento(depois) != antes:
                    recusas.append((arquivo, caminho, antes, depois))
                    continue
                livro.append({
                    'arquivo': arquivo,
                    'registro': registro['id'],
                    'caminho': caminho,
                    'antes': antes,
                    'depois': depois,
                })

        if gravar and not recusas:
            aplicar(banco['registros'])
            with open(arquivo, 'w', encoding='utf-8') as f:
                f.write(json.dumps(banco, ensure_ascii=False, indent=INDENT) + '\n')

    if recusas:
        print('RECUSADO: %d mudancas nao sao apenas de acento.' % len(recusas))
        for arquivo, caminho, antes, depois in recusas[:10]:
            print('  %s %s\n    antes : %s\n    depois: %s' % (arquivo, caminho, antes, depois))
        return 2

    print('%d strings restauradas em %d arquivos.' % (len(livro), len(ARQUIVOS)))
    distintas = sorted({(i['antes'], i['depois']) for i in livro})
    print('%d pares distintos:' % len(distintas))
    for antes, depois in distintas[:80]:
        print('  %s\n    -> %s' % (antes, depois))

    if gravar:
        registro = {
            'id': 'acentuacao-restaurada',
            'ilha': 'robometria',
            'entidade': 'medicao',
            'gerado_por': 'ferramentas/acentuar-banco.py',
            'gerado_em': '2026-09-11',
            'o_que_e': (
                'Livro-razao da restauracao de acentos dos campos do banco que vao para a '
                'tela. Cada linha e uma string que a ilha PUBLICA e que estava em ASCII. A '
                'mudanca e so de diacritico, e isso e verificavel sem confiar em ninguem: '
                'reduzida a ASCII, a coluna "depois" e byte a byte igual a coluna "antes".'
            ),
            'o_que_ele_nao_prova': (
                'Que a fonte primaria escreve assim. O acento foi RESTAURADO pela ilha, nao '
                'LIDO no fabricante — a rede desta nuvem nao alcanca fabricante nenhum. Esta '
                'lista e a conferencia de quem reler os manuais quando a rede abrir (item (c) '
                'do bloco 3c do PROMPT.md): se alguma fonte de fato escrever sem acento, a '
                'linha correspondente volta atras e vira excecao declarada.'
            ),
            'campos_de_tela': list(CAMPOS_DE_TELA),
            'total': len(livro),
            'pares_distintos': [{'antes': a, 'depois': d} for a, d in distintas],
            'mudancas': livro,
        }
        with open('dados/acentuacao-restaurada.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(registro, ensure_ascii=False, indent=1) + '\n')
        print('\ngravado: %d mudancas no banco e em dados/acentuacao-restaurada.json' % len(livro))
    else:
        print('\n(nada gravado — rode com --gravar)')
    return 0


def aplicar(no, chave=None):
    """Aplica a troca no proprio objeto, so nos campos de tela."""
    if isinstance(no, dict):
        for k, v in no.items():
            if isinstance(v, str) and k in CAMPOS_DE_TELA:
                no[k] = acentuar(v)
            else:
                aplicar(v, k)
    elif isinstance(no, list):
        for i, v in enumerate(no):
            if isinstance(v, str) and chave in CAMPOS_DE_TELA:
                no[i] = acentuar(v)
            else:
                aplicar(v, chave)


if __name__ == '__main__':
    sys.exit(main())
