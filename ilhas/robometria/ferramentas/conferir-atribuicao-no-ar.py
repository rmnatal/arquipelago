#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A atribuicao da funcao, medida NO HTML SERVIDO (secao 26.3 do ARQUIPELAGO.md).

    python3 ferramentas/conferir-atribuicao-no-ar.py .

POR QUE ISTO EXISTE SEPARADO DA BANCADA. O ferramentas/teste-r1.php prova que o
codigo esta certo; so o ar prova que ele esta NO AR (secao 4 do contrato). E aqui
a diferenca nao e teorica: o Sync baixa o manifest e cada arquivo em requisicoes
separadas, entao um snippet novo pode estar servindo com dado velho, ou o
contrario — e esta e uma mudanca em que dado e codigo TEM de chegar juntos, porque
o molde da frase depende de um campo que nasceu no mesmo bloco.

O QUE ELE MEDE, e sao os dois lados da regra:

  1. Nas pecas cuja funcao a ilha DERIVOU (funcao.declarada_por diferente de
     'titulo'), nada no corpo servido atribui aquela funcao ao fabricante, e a
     ressalva que diz quem a leu esta la.
  2. Nas pecas cujo TITULO do fabricante declara a funcao, a atribuicao continua
     servida e a ressalva NAO aparece. Sem este segundo lado, uma pagina que
     parasse de atribuir qualquer coisa a qualquer um passaria — e a ilha teria
     jogado fora a frase mais forte que tem.

TRES CUIDADOS QUE ESTA ILHA JA PAGOU PARA APRENDER:

  - Mede-se no CORPO, nunca no HTML inteiro: o JSON-LD e a casca repetem texto, e
    afirmacao sobre o que a pagina diz encontrada dentro do proprio schema passa
    ate com resposta inventada (secao 8).
  - O tamanho da pagina medida sai impresso: bancada ou fetch que serve menos que
    o site mede a metade errada sem erro nenhum aparecer.
  - O modelo de cada peca sai do GABARITO, nunca digitado aqui: lista digitada
    envelhece calada no dia em que a peca mudar de modelo.

A afirmacao "nada atribui X ao fabricante" so e cobrada no modelo em que TODAS as
pecas daquele tipo sao derivadas. Num modelo misto, a mesma frase proibida seria
a frase CERTA da peca vizinha — e cobrar ali seria reprovar a pagina correta, que
e como duas reguas desta ilha ja nasceram erradas.
"""

import json
import os
import re
import sys
import time
import unicodedata
import urllib.request

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL_R1 = 'https://robometria.com.br/qual-peca-serve-no-meu-robo-aspirador/'

falhas = 0
feitos = 0


def ok(condicao, rotulo, medida=''):
    global falhas, feitos
    feitos += 1
    print(('  ok    ' if condicao else '  FALHA ') + rotulo.ljust(62) + ' ' + medida)
    if not condicao:
        falhas += 1
    return condicao


def sem_acento(t):
    return unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode()


def corpo_servido(url):
    """(texto do corpo sem marcacao, bytes do HTML inteiro)."""
    req = urllib.request.Request(url, headers={'User-Agent': 'Robometria-Fundacao'})
    html = urllib.request.urlopen(req, timeout=45).read().decode('utf-8', 'replace')
    m = re.search(r'<main\b.*?</main>', html, re.S) or re.search(r'<body\b.*?</body>', html, re.S)
    texto = re.sub(r'<[^>]+>', ' ', m.group(0))
    return sem_acento(re.sub(r'\s+', ' ', texto)), len(html)


def main(raiz):
    dados = os.path.join(raiz, 'dados')
    with open(os.path.join(dados, 'esquema-banco.json'), encoding='utf-8') as f:
        esquema = json.load(f)
    with open(os.path.join(dados, 'pecas.json'), encoding='utf-8') as f:
        registros = json.load(f)['registros']
    with open(os.path.join(dados, 'r1-referencia.json'), encoding='utf-8') as f:
        gabarito = json.load(f)['respostas']

    tipos = esquema['tipos_que_exigem_funcao_declarada']['tipos']
    derivada, de_titulo = {}, {}
    for r in registros:
        if r['tipo'] not in tipos:
            continue
        d = (r.get('funcao') or {}).get('declarada_por')
        if d == 'titulo':
            de_titulo[r['id']] = r['tipo']
        elif d:
            derivada[r['id']] = (r['tipo'], d)

    # Em que modelo cada peca responde, e quais pecas de cada tipo cada modelo
    # serve. Tudo do gabarito.
    onde = {}
    por_modelo_e_tipo = {}
    for mid, resposta in gabarito.items():
        for grupo in ('fabricante', 'terceiro'):
            for item in resposta[grupo]:
                onde.setdefault(item['peca'], []).append(mid)
                por_modelo_e_tipo.setdefault((mid, item['tipo']), set()).add(item['peca'])

    marca = {
        'contraste-no-catalogo': 'Quem chama esta peca de %s e a Robometria',
        'canal-de-manutencao': 'Quem chama esta peca de %s e o proprio fabricante',
    }
    versao = time.strftime('%H%M%S')
    cache = {}

    def pagina(mid):
        if mid not in cache:
            cache[mid] = corpo_servido('%s?modelo=%s&v=%s' % (URL_R1, mid, versao))
        return cache[mid]

    print('Atribuicao da funcao no HTML servido — %s\n' % URL_R1)

    if not derivada:
        ok(False, 'ha peca de funcao derivada para medir',
           'o banco nao tem nenhuma — a regua nao teria o que afirmar')

    for pid, (tipo, origem) in sorted(derivada.items()):
        if pid not in onde:
            ok(False, '%s nao responde em modelo nenhum' % pid)
            continue
        mid = sorted(onde[pid])[0]
        texto, tamanho = pagina(mid)
        ok(tamanho > 40000, '%s: a pagina medida tem tamanho de pagina' % mid,
           '%d bytes' % tamanho)

        if origem not in marca:
            ok(False, '%s: origem %r sem marca escrita nesta regua' % (pid, origem))
            continue
        ok((marca[origem] % tipo) in texto,
           '%s: a ressalva diz quem leu a funcao (%s)' % (pid, tipo), origem)

        todas_derivadas = all(p in derivada for p in por_modelo_e_tipo[(mid, tipo)])
        if todas_derivadas:
            ok('declara a %s' % tipo not in texto and 'declara o %s' % tipo not in texto,
               '%s: nada atribui "%s" ao fabricante' % (mid, tipo),
               '%d peca(s) do tipo na pagina' % len(por_modelo_e_tipo[(mid, tipo)]))

    # O LADO DE CIMA, num modelo cujo tipo e servido SO por peca de titulo.
    medido_de_titulo = False
    for pid, tipo in sorted(de_titulo.items()):
        for mid in sorted(onde.get(pid, [])):
            if any(p in derivada for p in por_modelo_e_tipo[(mid, tipo)]):
                continue
            texto, tamanho = pagina(mid)
            ok(tamanho > 40000, '%s: a pagina medida tem tamanho de pagina' % mid,
               '%d bytes' % tamanho)
            ok('declara a %s' % tipo in texto or 'declara o %s' % tipo in texto,
               '%s: onde o titulo declara, a atribuicao continua no ar (%s)' % (mid, tipo))
            ok('Quem chama esta peca de' not in texto,
               '%s: e a pagina nao carrega ressalva de funcao derivada' % mid)
            medido_de_titulo = True
            break
        if medido_de_titulo:
            break
    ok(medido_de_titulo, 'a varredura pisou nos dois lados, e nao so no derivado')

    print()
    if falhas:
        print('REPROVADO NO AR: %d falha(s) em %d afirmacoes.' % (falhas, feitos))
        return 1
    print('APROVADO NO AR: %d afirmacoes, 0 falha(s).' % feitos)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else BASE))
