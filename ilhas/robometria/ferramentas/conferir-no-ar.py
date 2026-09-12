#!/usr/bin/env python3
"""Confere NO AR o que a revisao 17 prometeu — com regua propria.

    python3 ferramentas/conferir-no-ar.py

POR QUE ELE EXISTE, e por que a regua e literal aqui dentro
-----------------------------------------------------------
A secao 8 do ARQUIPELAGO.md manda buscar a URL no ar e conferir com numero
medido, e a secao 4 lembra que "aplicado com sucesso" no log do Sync nao e
evidencia de nada. Mas ha um jeito de fazer isso e continuar sem medir: ler a
regua do MESMO codigo que produziu a pagina. Se o nome da pagina sair da funcao
da casca e for comparado com o que a casca serviu, as duas metades erram juntas
e o verde nao significa nada — e esta ilha ja pagou tres vezes por testes assim.

Entao os nove enderecos e os nove nomes estao ESCRITOS aqui, copiados da decisao
do bloco, e nao lidos de snippet nenhum. Quem mudar um nome no repositorio e
esquecer deste arquivo ve a conferencia reprovar, que e exatamente o que se quer
de uma segunda testemunha.

O que ele mede, no HTML que o servidor devolve:
  1. HTTP 200 nas nove;
  2. o <title> e o nome da pagina mais " – Robometria", e cabe em 65 caracteres;
  3. o og:title e o MESMO nome (era aqui que seis paginas divergiam);
  4. o H1 e o MESMO nome;
  5. nenhuma das nove serve o estado degradado (classe rbm-sem-banco);
  6. zero &#038; DENTRO de <script> — contado so nos blocos de script, nunca na
     pagina inteira;
  7. a revisao do /status e a do manifest;
  8. a procedencia do Pa dentro de cada cartao da R2 — o rotulo do degrau, a
     data, a ressalva, o link discreto, e a porta de compra ANTES da fonte.
     Os tres textos estao escritos literalmente aqui dentro, como os nomes das
     paginas: derivar do mesmo lugar de onde a pagina deriva faria as duas
     metades errarem juntas.
"""

import html
import json
import re
import subprocess
import sys
import time

DOMINIO = 'https://robometria.com.br'
STATUS = DOMINIO + '/wp-json/robometria/v1/status'

# endereco -> nome canonico da pagina. Literal de proposito: ver o cabecalho.
PAGINAS = [
    ('/',                                             'Seu robô aspirador: qual peça serve, quanta sucção'),
    ('/ferramentas/',                                 'As duas ferramentas'),
    ('/metodologia/',                                 'Como a gente decide o que publicar'),
    ('/sobre/',                                       'Quem publica este site'),
    ('/divulgacao-de-afiliados/',                     'Como este site ganha dinheiro'),
    ('/qual-peca-serve-no-meu-robo-aspirador/',       'Qual peça serve no meu robô aspirador'),
    ('/quantos-pa-o-robo-aspirador-precisa/',         'Quantos Pa o seu robô aspirador precisa'),
    ('/filtro-universal-de-robo-aspirador/',          'Existe filtro universal de robô aspirador?'),
    ('/quantos-m2-o-robo-aspirador-limpa-por-carga/', 'Quantos m² um robô aspirador limpa por carga'),
]

MARCA = ' – Robometria'
TETO = 65

falhas = 0
feitos = 0


def ok(condicao, rotulo, medido=''):
    global falhas, feitos
    feitos += 1
    if condicao:
        print('  ok    %-58s %s' % (rotulo, medido))
    else:
        falhas += 1
        print('  FALHA %-58s %s' % (rotulo, medido))
    return condicao


def buscar(url, tentativas=3):
    """Uma falha de rede so vira bloqueio depois de repetir (secao 20.2)."""
    for n in range(tentativas):
        r = subprocess.run(['curl', '-s', '-w', '\\n%{http_code}', '--max-time', '40', url],
                           capture_output=True, text=True)
        corpo = r.stdout
        codigo = corpo.rsplit('\n', 1)[-1].strip()
        if codigo and codigo != '000':
            return corpo.rsplit('\n', 1)[0], codigo
        time.sleep(4)
    return '', '000'


def texto_da_tag(corpo, padrao):
    m = re.search(padrao, corpo, re.S | re.I)
    if not m:
        return ''
    return html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).strip()


# O QUE O CARTAO DA R2 TEM QUE DIZER, escrito LITERALMENTE aqui.
#
# Nao e lido do banco nem do arquivo de dados de proposito: se esta conferencia
# derivasse do mesmo lugar de onde a pagina deriva, as duas metades erravam
# juntas e o verde nao mediria nada. O dia em que um destes tres textos mudar no
# repositorio, esta lista TEM que ser reescrita a mao — e e exatamente esse
# atrito que faz dela uma medicao.
R2_CAMINHO = '/quantos-pa-o-robo-aspirador-precisa/'
R2_PROCEDENCIA = 'Como sabemos — página do fabricante, verificado em 09/09/2026'
R2_RESSALVA = '<span class="rbm-tag">a confirmar no manual</span>'
R2_ATRIBUICAO = 'Pa declarados pelo fabricante'

# A secao "Exatamente no limiar" (R2 1.3.0, 12/09/2026). Os dois modelos que
# estao EXATAMENTE em 4.000 Pa na situacao-ancora, escritos aqui literalmente
# como manda o cabecalho deste arquivo: ler a lista do r2-respostas.json seria
# conferir a pagina com o arquivo que a produziu.
R2_LIMIAR_TITULO = 'Exatamente no limiar — não acima dele'
R2_LIMIAR_SEM_PORTA = 'a página não recomenda estes modelos para a sua situação'
R2_LIMIAR_MODELOS = ('Xiaomi E10', 'Xiaomi S10')
R2_LIMIAR_FRASE = '4.000 Pa declarados pelo fabricante, e a Canaltech escreve "acima de 4.000 Pa"'

# O MESMO, PARA O CARTAO DO A2 — e repare que o degrau NAO e o mesmo. A area por
# carga dos cinco Electrolux vem da loja oficial da marca (degrau 4), e nao do
# fabricante. Foi por credita-la ao fabricante, com a atribuicao digitada no
# molde, que a pagina passou dois dias no ar dizendo uma frase falsa.
#
# A ULTIMA LINHA E A MAIS IMPORTANTE DESTA LISTA: ela mede a AUSENCIA da frase
# antiga. Trava que so confere o texto novo aprova uma pagina que sirva os dois.
A2_CAMINHO = '/quantos-m2-o-robo-aspirador-limpa-por-carga/'
A2_PROCEDENCIA = 'Como sabemos — loja oficial da marca, verificado em 09/09/2026'
A2_RESSALVA = '<span class="rbm-tag">confira a embalagem</span>'
A2_ATRIBUICAO = 'Área por carga declarada pela loja oficial da marca'
A2_TITULO = 'Os modelos cuja área por carga é declarada pela loja oficial da marca'
A2_FRASE_ANTIGA = 'O fabricante declara'

# A TAG DE MEDICAO, com o ID DESTA ILHA escrito aqui pela mesma razao de sempre.
#
# Ler a constante do snippet e compara-la com o que o site serviu seria comparar
# a constante consigo mesma. E o erro que essa comparacao nunca pegaria e o unico
# que importa: a casca copiada para a ilha seguinte com o ID da anterior, que vai
# para o ar funcionando, sem uma linha de defeito visivel, gravando sessao na
# propriedade errada por meses.
GA4_ID = 'G-RM7KS75QP2'
GA4_SRC = 'https://www.googletagmanager.com/gtag/js?id=' + GA4_ID
# Onde a frase que conta o que o site mede tem que estar. No <head> a palavra
# googletagmanager aparece nas nove paginas: medir no HTML inteiro aprovaria uma
# pagina que nao diz uma palavra sobre medicao.
GA4_CAMINHO_DA_FRASE = '/divulgacao-de-afiliados/'


def corpo_da_pagina(html_servido):
    m = re.search(r'<main\b[^>]*>(.*?)</main>', html_servido, re.S | re.I)
    return m.group(1) if m else ''


def conferir_medicao(corpo, caminho):
    """A tag de medicao no HTML SERVIDO: o ID certo, async, e DEPOIS do que ela
    nao pode preceder. O que se mede e ORDEM: 'a tag esta ai' e a afirmacao que
    um JSON-LD novo acima dela aprovaria sem piscar."""
    pos = corpo.find(GA4_SRC)
    if not ok(pos > -1, 'serve a tag de medicao com o ID desta ilha', GA4_ID):
        return
    abertura = corpo[max(0, corpo.rfind('<script', 0, pos)):pos + 200]
    ok('async' in abertura, 'o script de terceiro vai com async')
    ok(("gtag('config', '%s')" % GA4_ID) in corpo, 'configura a propriedade desta ilha')

    fim_titulo = corpo.rfind('</title>')
    ok(-1 < fim_titulo < pos, 'a tag vem DEPOIS do <title>')

    lds = [m.start() for m in re.finditer(r'<script[^>]*type="application/ld\+json"', corpo, re.I)]
    ok(bool(lds) and lds[-1] < pos, 'a tag vem DEPOIS do ultimo JSON-LD',
       'blocos de JSON-LD: %d' % len(lds))

    terceiros = [s for s in re.findall(r'<script[^>]*\bsrc="(https?://[^"]+)"', corpo, re.I)
                 if 'robometria.com.br' not in s]
    ok(len(terceiros) == 1 and terceiros[0].startswith(GA4_SRC),
       'um unico script de terceiro, e e o da medicao', ' '.join(terceiros))

    if caminho == GA4_CAMINHO_DA_FRASE:
        miolo = corpo_da_pagina(corpo)
        ok('Google Analytics' in miolo, 'a pagina de divulgacao nomeia a ferramenta de medicao')
        ok(bool(re.search('medir audi[êe]ncia', miolo, re.I)),
           'e diz, no corpo, para que ela serve')


def conferir_procedencia_da_r2(carimbo):
    """A procedencia do Pa, medida no cartao SERVIDO (R2 1.2.0)."""
    print('\n[%s] procedencia do Pa no cartao' % R2_CAMINHO)
    corpo, codigo = buscar(DOMINIO + R2_CAMINHO + '?v=' + carimbo)
    if not ok('200' == codigo, 'HTTP 200', codigo):
        return

    cartoes = re.findall(r'<li class="rbm-vitrine-item">(.*?)</li>', corpo, re.S)
    if not ok(len(cartoes) >= 3, 'a vitrine serve o portao de 3 itens', '%d cartoes' % len(cartoes)):
        return

    sem_linha = [i for i, c in enumerate(cartoes) if R2_PROCEDENCIA not in c]
    ok(not sem_linha, 'todo cartao diz de onde veio o Pa, com a data',
       'todos os %d' % len(cartoes) if not sem_linha else 'cartao(oes) %s' % sem_linha)

    sem_ressalva = [i for i, c in enumerate(cartoes) if R2_RESSALVA not in c]
    ok(not sem_ressalva, 'todo cartao carrega a ressalva do degrau 3',
       'todos os %d' % len(cartoes) if not sem_ressalva else 'cartao(oes) %s' % sem_ressalva)

    sem_atribuicao = [i for i, c in enumerate(cartoes) if R2_ATRIBUICAO not in c]
    ok(not sem_atribuicao, 'a atribuicao dentro da frase e a do degrau',
       'todos os %d' % len(cartoes) if not sem_atribuicao else 'cartao(oes) %s' % sem_atribuicao)

    fora_de_ordem = []
    sem_fonte = []
    for i, c in enumerate(cartoes):
        a = c.find('class="rbm-vitrine-acao"')
        f = c.find('class="rbm-vitrine-fonte"')
        if a < 0 or f < 0 or a > f:
            fora_de_ordem.append(i)
        if not re.search(r'<a class="rbm-fonte"[^>]*rel="nofollow noopener"', c):
            sem_fonte.append(i)
    ok(not fora_de_ordem, 'a porta de compra vem antes da procedencia, em todo cartao',
       'todos os %d' % len(cartoes) if not fora_de_ordem else 'cartao(oes) %s' % fora_de_ordem)
    ok(not sem_fonte, 'o link de fonte e discreto e nofollow, em todo cartao',
       'todos os %d' % len(cartoes) if not sem_fonte else 'cartao(oes) %s' % sem_fonte)


def conferir_secao_do_limiar(carimbo):
    """A secao "Exatamente no limiar" SERVIDA (R2 1.3.0).

    Ela nomeia modelo e Pa com a mesma autoridade da vitrine e, ate 12/09/2026,
    nao dizia de onde o numero vinha. Aqui se mede o que o SERVIDOR serve, na
    situacao-ancora — a pagina sem parametro nenhum, que e a que um modelo de
    linguagem le.
    """
    print('\n[%s] a secao "Exatamente no limiar"' % R2_CAMINHO)
    corpo, codigo = buscar(DOMINIO + R2_CAMINHO + '?v=' + carimbo)
    if not ok('200' == codigo, 'HTTP 200', codigo):
        return

    texto = html.unescape(corpo)
    if not ok(R2_LIMIAR_TITULO in texto, 'a secao existe na pagina servida'):
        return

    itens = re.findall(r'<li class="rbm-no-limiar-item">(.*?)</li>', corpo, re.S)
    if not ok(len(itens) == len(R2_LIMIAR_MODELOS), 'a secao serve os itens esperados',
              '%d item(ns)' % len(itens)):
        return

    faltando = [m for m in R2_LIMIAR_MODELOS
                if not any(m in html.unescape(i) for i in itens)]
    ok(not faltando, 'os modelos da secao sao os que estao exatamente no limiar',
       ', '.join(R2_LIMIAR_MODELOS) if not faltando else 'faltou %s' % faltando)

    sem_frase = [i for i, c in enumerate(itens) if R2_LIMIAR_FRASE not in html.unescape(c)]
    ok(not sem_frase, 'a frase atribui o Pa ao degrau E nomeia quem publica o limiar',
       'todos os %d' % len(itens) if not sem_frase else 'item(ns) %s' % sem_frase)

    sem_linha = [i for i, c in enumerate(itens) if R2_PROCEDENCIA not in html.unescape(c)]
    ok(not sem_linha, 'todo item diz de onde veio o Pa, com a data',
       'todos os %d' % len(itens) if not sem_linha else 'item(ns) %s' % sem_linha)

    sem_ressalva = [i for i, c in enumerate(itens) if R2_RESSALVA not in c]
    ok(not sem_ressalva, 'todo item carrega a ressalva do degrau 3',
       'todos os %d' % len(itens) if not sem_ressalva else 'item(ns) %s' % sem_ressalva)

    sem_fonte = [i for i, c in enumerate(itens)
                 if not re.search(r'<a class="rbm-fonte"[^>]*rel="nofollow noopener"', c)]
    ok(not sem_fonte, 'o link de fonte e discreto e nofollow, em todo item',
       'todos os %d' % len(itens) if not sem_fonte else 'item(ns) %s' % sem_fonte)

    # A SECAO NAO VENDE, e a falta esta dita. Medir so a ausencia do botao
    # aprovaria o silencio que estava la antes — e silencio e o defeito.
    com_botao = [i for i, c in enumerate(itens)
                 if 'rbm-comprar' in c or 'rbm-sem-loja' in c]
    ok(not com_botao, 'nenhum item da secao tem porta de compra',
       'nenhum dos %d' % len(itens) if not com_botao else 'item(ns) %s' % com_botao)

    bloco = texto[texto.find(R2_LIMIAR_TITULO):]
    ok(R2_LIMIAR_SEM_PORTA in bloco, 'a secao diz por que nao tem botao de compra')

    # E ela vem DEPOIS da lista principal. Em primeiro lugar, a excecao rotulada
    # vira recomendacao de quem a fonte nao cobre.
    p_lista = texto.find('Modelos do banco que atendem')
    p_limiar = texto.find(R2_LIMIAR_TITULO)
    ok(0 <= p_lista < p_limiar, 'a secao vem depois da lista principal',
       'lista em %d, limiar em %d' % (p_lista, p_limiar))


def conferir_procedencia_do_a2(carimbo):
    """A procedencia da area por carga, medida no cartao SERVIDO (A2 1.2.0)."""
    print('\n[%s] procedencia da area por carga no cartao' % A2_CAMINHO)
    corpo, codigo = buscar(DOMINIO + A2_CAMINHO + '?v=' + carimbo)
    if not ok('200' == codigo, 'HTTP 200', codigo):
        return

    cartoes = re.findall(r'<li class="rbm-vitrine-item">(.*?)</li>', corpo, re.S)
    if not ok(len(cartoes) > 0, 'a vitrine serve cartoes', '%d cartoes' % len(cartoes)):
        return

    sem_linha = [i for i, c in enumerate(cartoes) if A2_PROCEDENCIA not in c]
    ok(not sem_linha, 'todo cartao diz de onde veio a area, com a data',
       'todos os %d' % len(cartoes) if not sem_linha else 'cartao(oes) %s' % sem_linha)

    sem_ressalva = [i for i, c in enumerate(cartoes) if A2_RESSALVA not in c]
    ok(not sem_ressalva, 'todo cartao carrega a ressalva do degrau 4',
       'todos os %d' % len(cartoes) if not sem_ressalva else 'cartao(oes) %s' % sem_ressalva)

    sem_atribuicao = [i for i, c in enumerate(cartoes)
                      if A2_ATRIBUICAO not in html.unescape(c)]
    ok(not sem_atribuicao, 'a atribuicao e a da LOJA OFICIAL, nao a do fabricante',
       'todos os %d' % len(cartoes) if not sem_atribuicao else 'cartao(oes) %s' % sem_atribuicao)

    creditam_fabricante = [i for i, c in enumerate(cartoes)
                           if A2_FRASE_ANTIGA in html.unescape(c)]
    ok(not creditam_fabricante,
       'a frase falsa que estava no ar sumiu do cartao',
       'nenhum dos %d' % len(cartoes) if not creditam_fabricante
       else 'cartao(oes) %s' % creditam_fabricante)

    ok(A2_TITULO in html.unescape(corpo),
       'o titulo da secao nomeia o degrau, e nao o fabricante')

    fora_de_ordem = []
    ressalva_tarde = []
    sem_fonte = []
    for i, c in enumerate(cartoes):
        t = c.find('class="rbm-tag"')
        a = c.find('class="rbm-vitrine-acao"')
        f = c.find('class="rbm-vitrine-fonte"')
        if a < 0 or f < 0 or a > f:
            fora_de_ordem.append(i)
        if t < 0 or a < 0 or t > a:
            ressalva_tarde.append(i)
        if not re.search(r'<a class="rbm-fonte"[^>]*rel="nofollow noopener"', c):
            sem_fonte.append(i)
    ok(not fora_de_ordem, 'a porta de compra vem antes da procedencia, em todo cartao',
       'todos os %d' % len(cartoes) if not fora_de_ordem else 'cartao(oes) %s' % fora_de_ordem)
    ok(not ressalva_tarde, 'a ressalva vem antes da porta de compra, em todo cartao',
       'todos os %d' % len(cartoes) if not ressalva_tarde else 'cartao(oes) %s' % ressalva_tarde)
    ok(not sem_fonte, 'o link de fonte e discreto e nofollow, em todo cartao',
       'todos os %d' % len(cartoes) if not sem_fonte else 'cartao(oes) %s' % sem_fonte)


def main():
    carimbo = time.strftime('%H%M%S')
    print('CONFERENCIA NO AR — Robometria, revisao %d' % json.load(open('manifest.json', encoding='utf-8'))['revisao'])
    print('=' * 78)

    manifest = json.load(open('manifest.json', encoding='utf-8'))
    revisao_esperada = manifest['revisao']

    corpo, codigo = buscar(STATUS + '?v=' + carimbo)
    ok('200' == codigo, 'o /status responde 200', codigo)
    try:
        estado = json.loads(corpo)
    except Exception:
        estado = {}
    ok(estado.get('revisao') == revisao_esperada,
       'a revisao aplicada e a do manifest',
       'ar %s / manifest %s' % (estado.get('revisao'), revisao_esperada))

    for caminho, nome in PAGINAS:
        url = DOMINIO + caminho + '?v=' + carimbo
        print('\n[%s] %s' % (caminho, nome))
        corpo, codigo = buscar(url)
        if not ok('200' == codigo, 'HTTP 200', codigo):
            continue

        titulo = texto_da_tag(corpo, r'<title>(.*?)</title>')
        ok(titulo == nome + MARCA, 'o <title> e o nome mais a marca', titulo)
        ok(len(titulo) <= TETO, 'o <title> cabe em %d caracteres' % TETO, '%d' % len(titulo))

        m = re.search(r'<meta property="og:title" content="([^"]*)"', corpo, re.I)
        og = html.unescape(m.group(1)) if m else ''
        ok(og == nome, 'o og:title e o mesmo nome', og)

        h1 = texto_da_tag(corpo, r'<h1[^>]*>(.*?)</h1>')
        ok(h1 == nome, 'o H1 e o mesmo nome', h1)

        ok('rbm-sem-banco' not in corpo, 'a pagina servida NAO e o estado degradado')

        scripts = '\n'.join(re.findall(r'<script\b[^>]*>(.*?)</script>', corpo, re.S | re.I))
        n = scripts.count('&#038;')
        ok(0 == n, 'zero &#038; dentro de <script>', 'achados: %d' % n)

        conferir_medicao(corpo, caminho)

    conferir_procedencia_da_r2(carimbo)
    conferir_secao_do_limiar(carimbo)
    conferir_procedencia_do_a2(carimbo)

    print('\n' + '=' * 78)
    if falhas:
        print('REPROVADO NO AR: %d afirmacoes, %d falha(s).' % (feitos, falhas))
        return 1
    print('APROVADO NO AR: %d afirmacoes, 0 falha(s).' % feitos)
    return 0


if __name__ == '__main__':
    sys.exit(main())
