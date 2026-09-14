#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""As DUAS atribuicoes da R1, medidas NO HTML SERVIDO.

Quem nomeou a FUNCAO da peca (secao 26.3 do ARQUIPELAGO.md) e quem DECLAROU a
COMPATIBILIDADE dela (14/09/2026). Sao perguntas diferentes sobre a mesma frase,
e a segunda entrou aqui no dia em que a primeira ja estava no ar havia um dia.

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

A SEGUNDA METADE — QUEM DECLAROU A COMPATIBILIDADE (14/09/2026)
---------------------------------------------------------------
O cartao da vitrine escrevia "o fabricante declara esta peca", DIGITADO, para
qualquer degrau, e a frase do kit sem avulso escrevia "que o fabricante declara"
numa oracao que ja abria com o publicador certo. Em 52 dos 73 itens do banco
daquele dia quem publicou foi a LOJA OFICIAL da marca, e a escada de fontes ja
dizia, com todas as letras, que a atribuicao do degrau 4 e "pela loja oficial da
marca" — falar pela marca (o que decide de que LADO o item cai na pagina) nao e
ser a marca.

E ELA SE MEDE DENTRO DA CLASSE DO CARTAO, nunca no texto corrido: a cauda da
divergencia diz "Um canal do fabricante declara alcance diferente" e esta CERTA.
Medir as duas juntas da falso positivo — foi o que aconteceu na primeira escrita
da regua de bancada, em tres itens. Fronteira de medicao e marcador escrito.
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
    """(texto do corpo sem marcacao, bytes do HTML inteiro, o corpo em marcacao).

    O terceiro item nasceu em 14/09/2026: a atribuicao da COMPATIBILIDADE mora
    numa classe especifica do cartao, e medi-la no texto corrido misturaria a
    oracao do item com a cauda da divergencia — que fala do fabricante com toda a
    razao. Fronteira de medicao e marcador escrito; aqui o marcador e a classe.
    """
    req = urllib.request.Request(url, headers={'User-Agent': 'Robometria-Fundacao'})
    html = urllib.request.urlopen(req, timeout=45).read().decode('utf-8', 'replace')
    m = re.search(r'<main\b.*?</main>', html, re.S) or re.search(r'<body\b.*?</body>', html, re.S)
    texto = re.sub(r'<[^>]+>', ' ', m.group(0))
    return sem_acento(re.sub(r'\s+', ' ', texto)), len(html), m.group(0)


def main(raiz):
    dados = os.path.join(raiz, 'dados')
    with open(os.path.join(dados, 'esquema-banco.json'), encoding='utf-8') as f:
        esquema = json.load(f)
    with open(os.path.join(dados, 'pecas.json'), encoding='utf-8') as f:
        registros = json.load(f)['registros']
    with open(os.path.join(dados, 'r1-referencia.json'), encoding='utf-8') as f:
        gabarito = json.load(f)['respostas']
    # O gabarito guarda so tipo, peca e frase. Quem publicou e de que degrau veio
    # moram no COMBUSTIVEL, que e o mesmo arquivo que o Sync leva para a option —
    # ou seja, o que a pagina tinha na mao quando escreveu a frase medida.
    with open(os.path.join(dados, 'r1-respostas.json'), encoding='utf-8') as f:
        fatos = json.load(f)['respostas']

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
        texto, tamanho, _cru = pagina(mid)
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
            texto, tamanho, _cru = pagina(mid)
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

    # ---------------------------------------------------------------- PARTE 2
    print('\nQuem DECLAROU a compatibilidade — no cartao servido\n')

    # As formas digitadas que este bloco tirou do ar. Nenhuma frase correta as
    # produz, e nenhuma delas colide com a cauda da divergencia.
    DIGITADAS = (
        'o fabricante declara esta peca',
        'o fabricante declara este kit',
        'que o fabricante declara compativel',
    )

    # Um modelo por DEGRAU, escolhido do gabarito e nunca digitado aqui: o
    # defeito era invisivel justamente por degrau, e medir so um deles seria
    # medir metade da regra.
    por_degrau = {}
    for mid, resposta in fatos.items():
        for item in resposta['fabricante']:
            por_degrau.setdefault(item['origem'], set()).add(mid)
    ok(len(por_degrau) > 1, 'o ar serve item de MAIS DE UM degrau da escada',
       ' + '.join(sorted(por_degrau)))

    for origem in sorted(por_degrau):
        mid = sorted(por_degrau[origem])[0]
        texto, tamanho, cru = pagina(mid)
        ok(tamanho > 40000, '[%s] %s: a pagina medida tem tamanho de pagina'
           % (origem, mid), '%d bytes' % tamanho)

        cartoes = re.findall(r'<span class="rbm-vitrine-porque">(.*?)</span>', cru, re.S)
        ok(len(cartoes) > 0, '[%s] %s: a vitrine serve cartao com a frase do porque'
           % (origem, mid), '%d cartao(oes)' % len(cartoes))

        publicadores = sorted({i['publicador']
                               for i in fatos[mid]['fabricante']})
        juntos = sem_acento(re.sub(r'<[^>]+>', ' ', ' '.join(cartoes)))
        faltou = [p for p in publicadores if sem_acento(p) not in juntos]
        ok(not faltou, '[%s] %s: todo cartao nomeia QUEM publicou' % (origem, mid),
           '; '.join(publicadores) if not faltou else 'faltou: ' + '; '.join(faltou))

        achadas = [d for d in DIGITADAS if d in juntos]
        ok(not achadas, '[%s] %s: nenhum cartao escreve a atribuicao digitada'
           % (origem, mid), '' if not achadas else '; '.join(achadas))

        # E a oracao da RESPOSTA, fora do cartao, pelo mesmo criterio. Aqui vale
        # o texto corrido, porque as tres formas acima nao colidem com a cauda.
        achadas = [d for d in DIGITADAS if d in texto]
        ok(not achadas, '[%s] %s: nenhuma frase da resposta escreve a digitada'
           % (origem, mid), '' if not achadas else '; '.join(achadas))

        # A CAUDA DA DIVERGENCIA CONTINUA PODENDO FALAR DO FABRICANTE, e sem
        # esta afirmacao a regua de cima seria satisfeita por uma pagina que
        # tivesse simplesmente parado de atribuir qualquer coisa a alguem.
        if any(i.get('divergencia') for i in fatos[mid]['fabricante']):
            ok('do fabricante' in texto,
               '[%s] %s: e a cauda da divergencia segue nomeando o fabricante'
               % (origem, mid))

    # -------------------------------------------------------------------------
    # O ARTIGO DE QUEM PUBLICA, NO AR (14/09/2026).
    #
    # A metade seguinte do mesmo defeito: tirado "o fabricante" do lugar de quem
    # publicou, o que ficou digitado foi o ARTIGO — "A %s declara", "que a %s
    # declara", "a %s declara esta peca" —, certo por acidente porque todo
    # publicador que chega a essas frases e feminino singular.
    #
    # A REGUA LE dados/publicadores.json, que e o BANCO, e compara com o que o ar
    # serve. Nao le a copia que o gerador gravou dentro de r1-respostas.json: se
    # lesse, banco e tela poderiam errar juntos e esta medicao ficaria verde
    # dentro do proprio buraco.
    with open(os.path.join(dados, 'publicadores.json'), encoding='utf-8') as f:
        artigo_de = {r['nome']: r['artigo'] for r in json.load(f)['registros']}
    formas = esquema['artigos_de_publicador']

    for origem in sorted(por_degrau):
        mid = sorted(por_degrau[origem])[0]
        texto, _tam, cru = pagina(mid)

        cartoes = re.findall(r'<span class="rbm-vitrine-porque">(.*?)</span>', cru, re.S)
        juntos = sem_acento(re.sub(r'<[^>]+>', ' ', ' '.join(cartoes)))

        publicadores = sorted({i['publicador'] for i in fatos[mid]['fabricante']})
        sem_registro = [p for p in publicadores if p not in artigo_de]
        ok(not sem_registro,
           '[%s] %s: todo publicador servido tem artigo declarado no banco' % (origem, mid),
           '%d publicador(es)' % len(publicadores) if not sem_registro
           else '; '.join(sem_registro))

        # No CARTAO a oracao comeca pelo artigo em minuscula ("a Electrolux
        # (loja oficial) declara esta peca...").
        sem_artigo = []
        verbo_torto = []
        for p in publicadores:
            if p not in artigo_de:
                continue
            art = artigo_de[p]
            forma = formas[art]
            esperado = '%s %s %s' % (art, sem_acento(p),
                                     'declaram' if forma['numero'] == 'plural' else 'declara')
            if esperado not in juntos:
                sem_artigo.append(esperado)
            # E a flexao ERRADA nao pode aparecer: sem esta metade, uma pagina
            # que escrevesse as duas passaria.
            errada = '%s %s %s' % (art, sem_acento(p),
                                   'declara' if forma['numero'] == 'plural' else 'declaram')
            if errada in juntos:
                verbo_torto.append(errada)
        ok(not sem_artigo,
           '[%s] %s: todo cartao escreve o artigo DECLARADO e o verbo concordado'
           % (origem, mid),
           '%d publicador(es)' % len(publicadores) if not sem_artigo
           else 'faltou: ' + '; '.join(sem_artigo))
        ok(not verbo_torto,
           '[%s] %s: e nenhum cartao serve a flexao errada do verbo' % (origem, mid),
           '' if not verbo_torto else '; '.join(verbo_torto))

        # NA ORACAO DA RESPOSTA, fora do cartao: o nome nunca aparece solto. A
        # busca e pelo nome do publicador — nunca "alguma coisa parecida com um
        # publicador" —, e a vizinhanca conferida e o artigo declarado, em
        # minuscula ou com a maiuscula que o esquema declara.
        solto = []
        for p in publicadores:
            if p not in artigo_de:
                continue
            art = artigo_de[p]
            alvo = sem_acento(p)
            antes_min = art + ' ' + alvo
            antes_mai = formas[art]['maiuscula'] + ' ' + alvo
            i = texto.find(alvo)
            while i != -1:
                trecho_min = texto[max(0, i - len(art) - 1):i + len(alvo)]
                trecho_mai = texto[max(0, i - len(formas[art]['maiuscula']) - 1):i + len(alvo)]
                if trecho_min != antes_min and trecho_mai != antes_mai:
                    solto.append('%s em ...%s...' % (p, texto[max(0, i - 30):i + len(alvo)]))
                    break
                i = texto.find(alvo, i + len(alvo))
        ok(not solto,
           '[%s] %s: no corpo servido, o nome de quem publica nunca vem sem o artigo declarado'
           % (origem, mid),
           '%d publicador(es)' % len(publicadores) if not solto else solto[0][:90])

    # E A PROVA DE QUE ESTA MEDICAO NAO E DE UM GENERO SO — dita como ela e, e
    # nao mais forte do que e: hoje TODO publicador que chega a R1 e feminino
    # singular, e por isso o ar nao consegue separar artigo derivado de artigo
    # digitado. Quem separa e a bancada, que produz o mundo
    # (ferramentas/mutacoes-artigo-do-publicador.py). O que o ar prova e que o
    # que foi ao ar le o banco: a afirmacao acima quebra no minuto em que um
    # publicador de outro genero entrar e a pagina nao acompanhar.
    artigos_no_ar = sorted({artigo_de[p] for mid in por_degrau.values()
                            for m in [sorted(mid)[0]]
                            for p in {i['publicador'] for i in fatos[m]['fabricante']}
                            if p in artigo_de})
    ok(len(artigos_no_ar) >= 1,
       'os artigos servidos hoje, ditos como sao (a bancada e quem mede os outros generos)',
       ' + '.join(artigos_no_ar))

    # A NOTA QUE JUSTIFICA A ORDEM COMERCIAL, no ar.
    _t, _n, _c = pagina(sorted(por_degrau[sorted(por_degrau)[0]])[0])
    ok('decidida pela declaracao do fabricante' not in _t,
       'a nota da ordem nao atribui o criterio a "o fabricante"')
    ok('declaracao de compatibilidade publicada na fonte' in _t,
       'a nota da ordem diz, no ar, qual e o criterio de verdade')

    print()
    if falhas:
        print('REPROVADO NO AR: %d falha(s) em %d afirmacoes.' % (falhas, feitos))
        return 1
    print('APROVADO NO AR: %d afirmacoes, 0 falha(s).' % feitos)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else BASE))
