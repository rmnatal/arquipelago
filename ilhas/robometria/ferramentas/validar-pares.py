#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Portao: todas as copias do numero de pares peca x modelo dizem a mesma coisa?

    python3 ferramentas/validar-pares.py

NASCEU EM 26/10/2026, FECHANDO O ITEM 1 DO DESPACHO DA SENTINELA DE 02/10 —
ABERTO 24 DIAS. A ilha publicava DOIS numeros para a mesma frase, nas quatro
URLs que a publicam:

    /sobre/                                  91 pares peca x modelo
    /qual-peca-serve-no-meu-robo-aspirador/  91
    /pecas/                                  91
    /filtro-universal-de-robo-aspirador/     92

Os dois estavam certos sob definicoes diferentes. Somando a `compatibilidade`
com selo do fabricante dos 54 registros publicaveis de `dados/pecas.json` dao
**92** pares; cruzando com os **45** modelos publicaveis de
`dados/modelos-robo.json`, EXATAMENTE UM par aponta para modelo nao publicavel
— `multi-pr10124` x `multi-ho401` —, e tirando-o sobram **91**. Entao
91 = par com as DUAS pontas publicaveis; 92 = par declarado, contado do lado da
peca. E nenhuma das quatro paginas dizia qual delas estava dizendo.

POR QUE ESTE PORTAO NAO COMPARTILHA DERIVACAO, e isto e a parte que importa.
O "pronto quando" do despacho pedia que os derivados passassem a tirar o numero
da MESMA derivacao. Esta ilha decidiu o contrario em 16/09/2026, por escrito,
dentro do `gerar-r1.py`: *"a conta e feita aqui, a mao, e nao lida de `contagem`
nem importada do `gerar-casca-fatos.py`, que conta a mesma coisa por conta
propria. Se as duas lessem a mesma fonte, errariam juntas e todo portao ficaria
verde"*. Derivacao unica nao e menos copia: e copia sem testemunha. Cada gerador
continua contando por conta propria, e ESTE ARQUIVO e o unico lugar onde as
contas se encontram — o que faltava em 02/10 nao era uma derivacao, era um
portao. Tres contas independentes com uma regua entre elas acham o erro; uma
conta sozinha nao tem com quem discordar.

A TERCEIRA REGRA, a mesma do `validar-derivados.py`: este portao nao tem so a
lista do que cobre. Ele VARRE `dados/*.json` atras de chave que fale de par
peca x modelo e REPROVA quando acha uma que nao esta na lista de cobertas nem na
de dispensadas, com o motivo escrito. Copia nova nasce coberta ou nasce
denunciada — nunca calada. Foi exatamente uma copia calada que custou 24 dias.
"""

import glob
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ERROS = []
AFIRMACOES = [0]


def erro(msg):
    ERROS.append(msg)


def ok(condicao, titulo, detalhe=''):
    AFIRMACOES[0] += 1
    if condicao:
        print('  ok     %s' % titulo)
    else:
        print('  FALHA  %s%s' % (titulo, ('  — ' + detalhe) if detalhe else ''))
        erro(titulo + ((' — ' + detalhe) if detalhe else ''))


def carregar(nome):
    with io.open(os.path.join(RAIZ, 'dados', nome), encoding='utf-8') as f:
        return json.load(f)


def texto(caminho):
    with io.open(os.path.join(RAIZ, caminho), encoding='utf-8') as f:
        return f.read()


def codigo(caminho):
    """O arquivo PHP SEM os comentarios — e a diferenca nao e detalhe.

    A primeira versao desta regua procurava `ROBOMETRIA_PARES_DEFINICAO` no
    arquivo inteiro, e a mutacao 8 da `mutacoes-pares-de-tela.py` PASSOU: ela
    tira a constante do molde da frase, e o nome dela continua no cabecalho de
    versao, que e comentario. Portao que le comentario aprova a intencao escrita
    no lugar do codigo que roda — e intencao escrita e exatamente o que esta
    ilha tem de sobra. A bateria achou isto antes de qualquer visitante.
    """
    s = texto(caminho)
    s = re.sub(r'/\*.*?\*/', ' ', s, flags=re.S)
    s = re.sub(r'(?m)^\s*//.*$', ' ', s)
    return s


# ---------------------------------------------------------------------------
# A CONTA DESTE PORTAO, feita aqui e de mais nenhum lugar
# ---------------------------------------------------------------------------
# Quarta contagem independente do mesmo fato, de proposito: as outras tres
# moram em gerar-casca-fatos.py, gerar-r1.py e gerar-a1.py. Se este arquivo
# importasse qualquer uma delas, o portao aprovaria o erro dela junto.
def contar():
    pecas = carregar('pecas.json')
    modelos = carregar('modelos-robo.json')
    publicaveis = {m['id'] for m in modelos['registros']
                   if m.get('status') == 'publicavel'}
    duas_pontas, sem_destino = 0, []
    for p in pecas['registros']:
        if p.get('status') != 'publicavel':
            continue
        for c in (p.get('compatibilidade') or []):
            if c.get('selo') != 'declarada_fabricante':
                continue
            if c.get('modelo') in publicaveis:
                duas_pontas += 1
            else:
                sem_destino.append('%s x %s' % (p['id'], c.get('modelo')))
    sem_destino.sort()
    return {
        'duas_pontas': duas_pontas,
        'lado_da_peca': duas_pontas + len(sem_destino),
        'sem_destino': sem_destino,
    }


# ---------------------------------------------------------------------------
# AS COPIAS COBERTAS — onde o numero vive e qual universo cada chave guarda
# ---------------------------------------------------------------------------
# `universo` diz qual das duas contas aquela chave DEVE trazer:
#   'duas_pontas'  = o numero que vai para a tela (91 hoje)
#   'lado_da_peca' = o declarado, contado do lado da peca (92 hoje)
#   'sem_destino'  = quantos ficam no banco sem destino (1 hoje)
#   'quais'        = a lista que NOMEIA os de sem destino
COBERTAS = [
    ('pecas.json', ('contagem', 'pares_peca_x_modelo_declarados'), 'lado_da_peca'),
    ('pecas.json', ('contagem', 'pares_peca_x_modelo_publicaveis_nas_duas_pontas'),
     'duas_pontas'),
    ('pecas.json', ('contagem', 'pares_para_modelo_nao_publicavel'), 'sem_destino'),
    ('pecas.json', ('contagem', 'pares_para_modelo_nao_publicavel_quais'), 'quais'),
    ('casca-fatos.json', ('medicao', 'pares_declarados'), 'duas_pontas'),
    ('a1-fatos.json', ('resumo', 'pares_declarados'), 'duas_pontas'),
    ('a1-fatos.json', ('resumo', 'pares_declarados_no_banco'), 'lado_da_peca'),
    ('a1-fatos.json', ('resumo', 'pares_para_modelo_nao_publicavel'), 'sem_destino'),
    ('r1-respostas.json', ('resumo', 'pares_declarados'), 'duas_pontas'),
    ('r1-respostas.json', ('resumo', 'pares_declarados_no_banco'), 'lado_da_peca'),
    ('r1-respostas.json', ('resumo', 'pares_para_modelo_nao_publicavel'), 'sem_destino'),
]

# DISPENSADAS, com o motivo ao lado — e a lista nao e desculpa, e divida escrita.
DISPENSADAS = {
    ('a2-fatos.json', 'pares_declarados'):
        'o A2 conta par (minutos, m2) e nao par peca x modelo: mesma palavra, '
        'outra entidade. Sao 5 hoje, e o numero nunca encostou no dos pares de peca',
    ('malha-pecas.json', 'pares_declarados'):
        'a secao /pecas/ guarda o NOME da chave da casca em chaves_da_resposta, '
        'nao o valor: o numero da frase e lido de casca-fatos.json em tempo de '
        'geracao, e a frase inteira e conferida abaixo',
    ('malha-pecas-referencia.json', 'pares_declarados'):
        'mesma coisa do malha-pecas.json: nome de chave, nao valor',
    ('a2-fatos.json', 'pares'):
        'o A2 lista os pares (minutos, m2) declarados por modelo — outra '
        'entidade, com 5 itens hoje. A palavra "par" e a mesma e o fato nao e',
    ('acentuacao-restaurada.json', 'pares_distintos'):
        'par (texto sem acento, texto com acento) da restauracao de acentos: '
        'nao tem peca nem modelo dentro',
    ('r1-respostas.json', 'pares_na_tabela'):
        'TERCEIRO universo, e ele e da TABELA e nao do banco: par (modelo, peca) '
        'distinto que a tabela de exemplos mostra. Hoje da 91, o MESMO numero do '
        'par com as duas pontas publicaveis — e por acidente do banco, nao por '
        'definicao. A jurisprudencia do item 2 do despacho de 14/09/2026 manda '
        'manter os dois com nomes separados exatamente ENQUANTO sao iguais, '
        'porque e enquanto sao iguais que ninguem percebe que foram confundidos; '
        'quem o cobrisse aqui como "duas_pontas" colaria duas contas diferentes. '
        'Quem o confere e a secao 19 do teste-r1.php, recontando das linhas',
}

# ONDE A FRASE DA TELA E CONFERIDA. O numero sozinho nao fecha o despacho: ele
# pede a DEFINICAO escrita na propria frase das quatro paginas, porque numero
# sem definicao foi o que permitiu os dois conviverem.
DEFINICAO = 'contando só os pares em que a peça e o modelo estão os dois publicados aqui'
DEFINICAO_SEM_ACENTO = 'contando so os pares em que a peca e o modelo estao os dois publicados aqui'

# Quem publica o numero, e por onde a definicao chega a cada um.
QUEM_PUBLICA = [
    ('/sobre/', 'snippets/robometria-casca.php', 'ROBOMETRIA_PARES_DEFINICAO'),
    ('/qual-peca-serve-no-meu-robo-aspirador/', 'snippets/robometria-r1.php',
     'ROBOMETRIA_PARES_DEFINICAO'),
    ('/pecas/', 'snippets/robometria-malha.php', 'ROBOMETRIA_PARES_DEFINICAO'),
    ('/filtro-universal-de-robo-aspirador/', 'snippets/robometria-a1.php',
     'ROBOMETRIA_PARES_DEFINICAO'),
]


def valor(doc, caminho):
    alvo = doc
    for chave in caminho:
        if not isinstance(alvo, dict) or chave not in alvo:
            return None, False
        alvo = alvo[chave]
    return alvo, True


def main():
    print('Robometria — as copias do par peca x modelo (despacho de 02/10, item 1)')
    print('=' * 72)
    c = contar()
    esperado = {
        'duas_pontas': c['duas_pontas'],
        'lado_da_peca': c['lado_da_peca'],
        'sem_destino': len(c['sem_destino']),
        'quais': c['sem_destino'],
    }
    print('  contado aqui: %d com as duas pontas, %d do lado da peca, %d sem destino'
          % (c['duas_pontas'], c['lado_da_peca'], len(c['sem_destino'])))
    if c['sem_destino']:
        print('                sem destino: %s' % ', '.join(c['sem_destino']))
    print()

    print('1. Cada copia traz o numero do universo que ela promete')
    docs = {}
    for arquivo, caminho, universo in COBERTAS:
        if arquivo not in docs:
            docs[arquivo] = carregar(arquivo)
        achado, existe = valor(docs[arquivo], caminho)
        rotulo = '%s > %s' % (arquivo, '.'.join(caminho))
        if not existe:
            ok(False, '%s existe' % rotulo,
               'chave ausente: o derivado foi gerado por uma versao velha do '
               'gerador, ou alguem a tirou')
            continue
        ok(achado == esperado[universo],
           '%s = %s (%s)' % (rotulo, esperado[universo], universo),
           'o arquivo diz %r' % (achado,))

    print('\n2. A conta fecha: duas pontas + sem destino = lado da peca')
    ok(c['duas_pontas'] + len(c['sem_destino']) == c['lado_da_peca'],
       'os dois universos sao o mesmo conjunto menos os pares sem destino',
       '%d + %d != %d' % (c['duas_pontas'], len(c['sem_destino']), c['lado_da_peca']))

    print('\n3. O numero que vai para a TELA e o das duas pontas, nunca o outro')
    # A regua que faltava em 02/10 dita de uma vez: as quatro paginas servem
    # UM numero. O valor sai dos derivados que cada snippet le, e a afirmacao
    # compara os derivados entre si — se um deles servir o 92, ela morde.
    da_tela = []
    for arquivo, caminho, universo in COBERTAS:
        if universo == 'duas_pontas':
            achado, existe = valor(docs[arquivo], caminho)
            if existe:
                da_tela.append((arquivo, achado))
    ok(len({v for _, v in da_tela}) == 1,
       'as %d copias que vao para a tela trazem o MESMO numero' % len(da_tela),
       '; '.join('%s=%r' % (a, v) for a, v in da_tela))
    ok(all(v == c['duas_pontas'] for _, v in da_tela),
       'e esse numero e o do par com as duas pontas publicaveis (%d)' % c['duas_pontas'],
       '; '.join('%s=%r' % (a, v) for a, v in da_tela))

    print('\n4. A DEFINICAO esta escrita na propria frase das quatro paginas')
    casca = codigo('snippets/robometria-casca.php')
    ok(("define( 'ROBOMETRIA_PARES_DEFINICAO', '%s' )" % DEFINICAO) in casca,
       'a definicao mora numa constante so, na casca',
       'ROBOMETRIA_PARES_DEFINICAO ausente ou com outro texto')
    for url, arquivo, constante in QUEM_PUBLICA:
        fonte = codigo(arquivo)
        ok(constante in fonte,
           '%s diz a definicao, lida da constante (%s)' % (url, os.path.basename(arquivo)),
           '%s nao cita %s' % (arquivo, constante))
    # E A FRASE DE /pecas/ E GERADA EM PYTHON, entao ela carrega a definicao
    # escrita, nao a constante. As duas tem de dizer a mesma coisa.
    malha = carregar('malha-pecas.json')
    frase = ((malha.get('secao') or {}).get('frases') or {}).get('resposta', '')
    ok(DEFINICAO_SEM_ACENTO in frase,
       'a frase gerada de /pecas/ traz a mesma definicao, sem acento',
       'a frase e %r' % frase[:160])
    ok(str(c['duas_pontas']) in frase,
       'e o numero dentro dela e o das duas pontas (%d)' % c['duas_pontas'],
       'a frase e %r' % frase[:160])

    print('\n5. Copia NOVA nasce coberta ou nasce denunciada')
    # Varre dados/*.json atras de chave que fale de par peca x modelo. A lista
    # de cobertas e a de dispensadas sao o unico lugar onde uma chave dessas
    # pode existir em paz.
    padrao = re.compile(r'^pares(_peca_x_modelo)?(_|$)')
    cobertas = {(a, caminho[-1]) for a, caminho, _ in COBERTAS}
    achadas, orfas = 0, []

    def varrer(doc, arquivo):
        pilha = [doc]
        while pilha:
            no = pilha.pop()
            if isinstance(no, dict):
                for k, v in no.items():
                    if isinstance(k, str) and padrao.match(k):
                        yield k
                    if isinstance(v, (dict, list)):
                        pilha.append(v)
            elif isinstance(no, list):
                for v in no:
                    if isinstance(v, (dict, list)):
                        pilha.append(v)

    for caminho_json in sorted(glob.glob(os.path.join(RAIZ, 'dados', '*.json'))):
        arquivo = os.path.basename(caminho_json)
        try:
            with io.open(caminho_json, encoding='utf-8') as f:
                doc = json.load(f)
        except ValueError:
            continue
        for chave in set(varrer(doc, arquivo)):
            achadas += 1
            if (arquivo, chave) in cobertas or (arquivo, chave) in DISPENSADAS:
                continue
            orfas.append('%s > %s' % (arquivo, chave))
    ok(not orfas,
       '%d chave(s) de par varrida(s) em dados/*.json, nenhuma orfa' % achadas,
       'orfa(s): %s. Ponha na lista COBERTAS (com o universo) ou na DISPENSADAS '
       '(com o motivo) — chave calada e como o 92 ficou 24 dias no ar'
       % ', '.join(orfas))

    print()
    if ERROS:
        print('REPROVADO: %d de %d afirmacoes sobre as copias do par.'
              % (len(ERROS), AFIRMACOES[0]))
        return 1
    print('APROVADO: %d afirmacoes sobre as copias do par, 0 falha.' % AFIRMACOES[0])
    return 0


if __name__ == '__main__':
    sys.exit(main())
