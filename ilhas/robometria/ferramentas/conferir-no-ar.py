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
  0. A PORTA DE ENTRADA (secao 29.2, nasceu em 02/11/2026): /wp-sitemap.xml,
     /robots.txt e /wp-json/ em 200 e com o content-type certo, mais o 404 que
     tem de ser 404 na pagina DESTA ilha e nao na do hospedeiro. As tres sao
     rota virtual do WordPress, nenhuma pagina as linka, e por isso sao as
     primeiras a morrer quando a reescrita do .htaccess some — foi o que
     derrubou esta ilha por quatro dias a partir de 30/10/2026 sem nenhum
     portao acusar;
  1. HTTP 200 nas nove;
  2. o <title> e o nome da pagina mais a cauda, e cabe em 65 caracteres. A
     cauda e " – Robometria" nas seis paginas sem promessa numerica e, nas tres
     que a leitura semanal de 16/09 mediu na primeira pagina com CTR zero, a
     PROMESSA: um numero derivado do banco no lugar da marca (casca 1.10.0).
     A FORMA da promessa esta escrita aqui, o VALOR nao — este arquivo exige
     "de <n> a <n> Pa" e recusa "de 1.400 a 10.000 Pa", porque conferir o valor
     contra o mesmo banco que o produziu seria as duas metades errando juntas;
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
import os
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

def paginas_da_malha():
    """As paginas de malha, LIDAS do registro do snippet que as publica.

    A lista acima e digitada e foi assim que esta ilha comecou; o registro da
    malha nao pode ser copiado para ca, porque quem decide o que esta publicado
    e ele — e lista digitada ao lado de lista contada diverge calada (a cicatriz
    do nome da pagina, da lista de categorias e das tres contagens da R1). O
    render da bancada imprime o registro em JSON para quem mede de fora do PHP.

    FALHA ALTO: sem o registro, esta conferencia estaria medindo menos paginas
    do que o site serve, e o verde dela seria sobre a metade que ela conhece.
    """
    saida = subprocess.run(
        ['php', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'render-para-teste.php'),
         '.', '--registro-da-malha'],
        capture_output=True, text=True)
    if saida.returncode != 0 or not saida.stdout.strip():
        raise SystemExit('ERRO: nao consegui ler o registro da malha do snippet '
                         '(php render-para-teste.php . --registro-da-malha): %s'
                         % saida.stderr.strip()[:300])
    return [(p['caminho'], p['titulo']) for p in json.loads(saida.stdout)]


PAGINAS += paginas_da_malha()

MARCA = ' – Robometria'
TETO = 65

# A CAUDA ESPERADA DO <title>, por pagina: a FORMA da promessa, nunca o valor.
# Pagina que nao esta aqui tem de servir a marca — e isso e afirmado adiante,
# para promessa nova nascer visivel em vez de nascer calada.
CAUDA_PROMETIDA = {
    '/quantos-pa-o-robo-aspirador-precisa/':         r'de [\d.]+ a [\d.]+ Pa',
    '/filtro-universal-de-robo-aspirador/':          r'[\d.]+ das [\d.]+ peças',
    '/quantos-m2-o-robo-aspirador-limpa-por-carga/': r'[\d.]+ de [\d.]+ marcas',
}

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


# O CABECALHO QUE FALTAVA, E ELE DECIDIA QUAL PAGINA ESTA FERRAMENTA LIA.
#
# Medido em 14/09/2026, fechando o item 1 do despacho da Sentinela do mesmo dia.
# Ela achou o sintoma — "a ilha serve HTML de 11/09 a quem nao pede gzip" — e a
# medicao seguinte afinou a CAUSA, que e mais estreita e mais perigosa: o que
# devolve a copia velha nao e pedir sem compressao, e pedir SEM CABECALHO NENHUM.
# Medido nas mesmas URLs, em /metodologia/:
#
#   Accept-Encoding: gzip ....... pagina de hoje
#   Accept-Encoding: identity ... pagina de hoje
#   Accept-Encoding: br ......... pagina de hoje
#   (nenhum cabecalho) .......... copia de 11/09, sem trilha e sem BreadcrumbList
#
# `curl -s` cru nao manda o cabecalho; navegador e Googlebot mandam. Ou seja: o
# leitor e o Google estavam certos e ERA ESTA FERRAMENTA que vinha conferindo,
# havia tres dias, uma pagina que nao existe mais — e passando, porque a de 11/09
# tambem era valida. E a familia do "parece conferido" que o contrato ja nomeou
# duas vezes.
#
# `identity` e nao `gzip` de proposito: pede a pagina de hoje SEM compressao, entao
# o corpo chega legivel sem o subprocesso precisar descomprimir nada. E a correcao
# NAO fecha o defeito por baixo do pano — a Sentinela proibiu isso com todas as
# letras ("nao feche este item ampliando a regua"). Quem mede a variante quebrada
# e conferir_variante_sem_cabecalho(), abaixo, e ela REPROVA enquanto o cache velho
# estiver de pe.
ACCEPT_ENCODING = 'Accept-Encoding: identity'


def buscar(url, tentativas=3):
    """Uma falha de rede so vira bloqueio depois de repetir (secao 20.2)."""
    for n in range(tentativas):
        r = subprocess.run(['curl', '-s', '-H', ACCEPT_ENCODING,
                            '-w', '\\n%{http_code}', '--max-time', '40', url],
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


# O ORCAMENTO DA PURGA, declarado e nao adivinhado. A unica medicao que esta
# ilha tem e de 166 s (Sync da revisao 43 as 19h30:50Z, canonico virado as
# 19h33:36Z, 14/09/2026). O teto e o dobro arredondado: largo o bastante para a
# janela medida nao virar alarme falso, estreito o bastante para "o leitor ficou
# na pagina de antes" continuar reprovando. Quem medir um atraso maior sobe
# ESTE numero e escreve a medicao ao lado — nunca apaga a afirmacao.
PURGA_ORCAMENTO_S = 360
PURGA_INTERVALO_S = 15


def _impressao_do_leitor(corpo, chave):
    """O QUE O LEITOR VE, reduzido a uma string comparavel.

    Tira marcacao, desfaz entidade e junta espaco: o que sobra e a palavra na
    tela. A CHAVE DE QUEBRA DE CACHE SAI ANTES, porque ela aparece dentro de
    link interno e do canonical da propria pagina — compara-la seria garantir
    desacordo e chamar isso de defeito.
    """
    corpo = corpo.replace('?' + chave, '').replace('&' + chave, '')
    texto = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', ' ', corpo)
    texto = re.sub(r'<[^>]+>', ' ', texto)
    return re.sub(r'\s+', ' ', html.unescape(texto)).strip()


# O QUE O CARTAO DA R2 TEM QUE DIZER, escrito LITERALMENTE aqui.
#
# Nao e lido do banco nem do arquivo de dados de proposito: se esta conferencia
# derivasse do mesmo lugar de onde a pagina deriva, as duas metades erravam
# juntas e o verde nao mediria nada. O dia em que um destes tres textos mudar no
# repositorio, esta lista TEM que ser reescrita a mao — e e exatamente esse
# atrito que faz dela uma medicao.
R2_CAMINHO = '/quantos-pa-o-robo-aspirador-precisa/'
# A DATA SAIU DESTA CONSTANTE EM 17/09/2026, E A REGRA DO CABECALHO ACIMA CONTINUA
# VALENDO INTEIRA. Ela dizia, literalmente, "verificado em 09/09/2026" — e passou
# seis dias verde porque os cinco cartoes serviam a mesma data, o que nunca foi uma
# propriedade da pagina: era VERDADE POR COINCIDENCIA DA COLETA, a mesma frase que
# esta ilha usou para descrever o portao do canal brasileiro antes de ele existir.
# Cada cartao carrega o `verificado_em` da FONTE dele, e no dia em que entrou um
# modelo coletado em outra data (o Roborock Q8 Max, 17/09) a regua acusou defeito
# num cartao que estava certo. O que e fixo na linha e a FRASE; a data e por cartao.
# Entao o literal digitado continua digitado — nao se le nada do banco aqui —, e o
# que mudou e a granularidade: exige-se a frase E uma data no formato da tela.
R2_PROCEDENCIA = 'Como sabemos — página do fabricante, verificado em '
R2_PROCEDENCIA_DATA = re.compile(
    re.escape(R2_PROCEDENCIA) + r'[0-3][0-9]/[01][0-9]/20[0-9][0-9]')
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

    sem_linha = [i for i, c in enumerate(cartoes) if not R2_PROCEDENCIA_DATA.search(c)]
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

    sem_linha = [i for i, c in enumerate(itens)
                 if not R2_PROCEDENCIA_DATA.search(html.unescape(c))]
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
                 if 'rbm-comprar' in c or 'rbm-sem-saida' in c]
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

    # A LINHA DA CURA DENTRO DA JANELA DO DESEMBARQUE — a regua da 20.4
    # consertada na mesma passada em que esta ilha recebeu a cura (29.4).
    # Ela SAI da conta de itens e ganha afirmacoes PROPRIAS; nunca e descartada
    # em silencio. Na maioria dos dias nao havera nenhuma, e isso e a trava 4
    # funcionando — porta que fala quando esta de pe enche a janela de 40
    # linhas, e janela cheia e item que rolou para fora dela sem ser conferido.
    itens_da_revisao, curas_da_revisao = itens_e_curas_da_janela(estado.get('log'))
    print('\n0-a. A JANELA DO LOG (20.4) — %d item(ns) de desembarque e %d linha(s) de cura'
          % (len(itens_da_revisao), len(curas_da_revisao)))
    if not curas_da_revisao:
        print('  --    nenhuma linha `cura da porta:` na janela — pela trava 4 da 29.4'
              ' esse e o silencio da porta DE PE, nao ausencia de instrumento')
    for linha in curas_da_revisao:
        print('  linha: %s' % linha)
        for cond, rotulo, medido in afirmacoes_da_linha_da_cura(linha):
            ok(cond, rotulo, medido)

    conferir_porta_de_entrada(carimbo)

    for caminho, nome in PAGINAS:
        url = DOMINIO + caminho + '?v=' + carimbo
        print('\n[%s] %s' % (caminho, nome))
        corpo, codigo = buscar(url)
        if not ok('200' == codigo, 'HTTP 200', codigo):
            continue

        titulo = texto_da_tag(corpo, r'<title>(.*?)</title>')
        forma = CAUDA_PROMETIDA.get(caminho)
        if forma is None:
            ok(titulo == nome + MARCA, 'o <title> e o nome mais a marca', titulo)
        else:
            esperado = re.compile('^' + re.escape(nome + ' – ') + forma + '$')
            ok(bool(esperado.match(titulo)),
               'o <title> e o nome mais a promessa numerica', titulo)
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
    conferir_variante_sem_cabecalho()
    conferir_cache_do_host()
    conferir_piso_no_ar()
    conferir_lugar_vazio_da_foto(carimbo)
    conferir_datas_no_ar(carimbo)
    conferir_busca_com_resultado(carimbo)

    print('\n' + '=' * 78)
    if falhas:
        print('REPROVADO NO AR: %d afirmacoes, %d falha(s).' % (feitos, falhas))
        return 1
    print('APROVADO NO AR: %d afirmacoes, 0 falha(s).' % feitos)
    return 0



def buscar_com_tipo(url, tentativas=3):
    """Como buscar(), mas devolve tambem o content-type.

    A 29.2 nao cobra so o 200: ela cobra que /wp-sitemap.xml venha com tipo de
    XML e /robots.txt com text/plain, porque a pagina do hospedeiro responde
    text/html para os tres e um portao que so conta 200 aprovaria isso.
    """
    for _ in range(tentativas):
        r = subprocess.run(['curl', '-s', '-H', ACCEPT_ENCODING,
                            '-w', '\\n%{http_code}\\n%{content_type}',
                            '--max-time', '40', url],
                           capture_output=True, text=True)
        partes = r.stdout.rsplit('\n', 2)
        if len(partes) == 3:
            corpo, codigo, tipo = partes
            if codigo.strip() and codigo.strip() != '000':
                return corpo, codigo.strip(), tipo.strip().lower()
        time.sleep(4)
    return '', '000', ''



# =============================================================================
# A PORTA DE ENTRADA NOMEADA PELA CAUSA — as grandezas da 29.7(3), a regua da
# linha da cura (20.4) e o retrato publico da 29.4-b/29.4-c
# (20/11/2026, na mesma passada em que esta ilha recebeu a cura da porta)
#
# POR QUE ISTO NASCEU AQUI E AGORA. Esta ilha era a UNICA no ar sem a cura da
# porta da 29.4, e o despacho ALTA de 19/11/2026 mediu a consequencia: 7 de 7
# paginas internas em 404 e a fabrica sem instrumento para dizer o que fazer. O
# `conferir_porta_de_entrada()` acima media as tres portas uma a uma e
# devolvia, na queda, SEIS reprovacoes espalhadas — cada uma verdadeira e
# nenhuma dizendo o que fazer. A 29.4 manda que a ilha que recebe a cura receba
# as afirmacoes dela na MESMA passada, e e isso que este bloco e.
#
# AS TRES QUEDAS DESTA RAIZ, para o numero nao sair de cabeca: 30/10 a 02/11
# (quatro dias), 11/11, e 19/11 a 20/11. Nas tres o tempo no chao foi decidido
# por quando alguem rodou um comando.
#
# AS FUNCOES SAO PURAS DE PROPOSITO, e e isso que faz o `--autoteste` fabricar
# o mundo em vez de esperar que ele aconteca: nenhuma queda se encena no disco
# deste conteiner, e regua de queda que so roda na queda e regua que estreia no
# pior dia.
# =============================================================================

# O FECHO DE REVISAO, que e o que corta a janela da 20.4. O corte e POSICIONAL:
# o log vem do mais novo para o mais velho, entao a janela da revisao corrente
# vai do topo ate o fecho ANTERIOR, exclusive.
REV_RE = re.compile(r'revis\w*\s+(\d+)\s*:')

# A LINHA DA CURA DA PORTA (29.4), que mora no MESMO log do desembarque e NAO e
# item dele. O nome e escrito pela casca em `robometria_casca_cura_registrar()`;
# a forma e a que a trava 3 exige — o antes e o depois em bytes E em blocos.
#
# O RECONHECIMENTO E PELA FRASE `cura da porta:`, NUNCA PELO NOME DO ARQUIVO, e
# isso e a 20.4 lida ao pe da letra: um snippet chamado `cura-da-porta` sendo
# APLICADO **e** item de desembarque, e tira-lo da conta seria o mesmo furo pelo
# avesso. O MUNDO 4 do autoteste prende essa confusao.
CURA_RE = re.compile(r'cura da porta\s*:')
CURA_FORMA_RE = re.compile(
    r'cura da porta:.*?(\d+)\s*bytes\s*\[([^\]]*)\]\s*->\s*(\d+)\s*bytes\s*\[([^\]]*)\]')


def diagnostico_da_porta(cod_home, cods_das_portas, rest_vivo, porta_publica=None):
    """A ASSINATURA DA 29, NOMEADA — ou None quando ela nao esta na mesa.

    Dez vezes no Arquipelago com a mesma cara, e TRES delas nesta ilha. Sempre
    as mesmas quatro grandezas juntas: a HOME em 200, as TRES portas da 29.2 em
    404, o REST VIVO por `?rest_route=` e o caminho bonito morto. O que isso
    quer dizer tem nome e tem conserto, e os dois estao na 29: o bloco
    `# BEGIN WordPress` saiu do `.htaccess` da raiz.

    O QUE ELA NAO AFIRMA, e e por isso que cobra as quatro juntas: se a home
    TAMBEM estiver morta, ou se o REST estiver morto nas duas formas, nao e esta
    a causa — e esta funcao devolve None em vez de nomear a errada. Causa
    inventada e a proxima execucao consertando a coisa errada (29.5).

    A QUINTA E A SEXTA GRANDEZA entram pelo `porta_publica`, o retrato minimo
    que o `/casca` desta ilha passou a servir SEM TOKEN em 20/11/2026. Sem ele a
    linha DIZ que nao separou os dois mundos, em vez de escolher um e soar
    conferida.
    """
    if cod_home != 200 or not rest_vivo:
        return None
    if not cods_das_portas or any(c == 200 for c in cods_das_portas):
        return None

    return ('29: A PORTA DE ENTRADA CAIU, e a assinatura e a conhecida — home em 200, '
            'as %d portas da 29.2 em %s, e o REST VIVO por `?rest_route=`. O WordPress '
            'esta de pe e o Apache parou de lhe mandar caminho bonito: e o bloco '
            '`# BEGIN WordPress` fora do `.htaccess` da raiz. CONSERTO: o '
            '`flush_rewrite_rules( true )` da 29.3 — '
            '`?rest_route=/robometria/v1/rotas&token=<token do Sync>&reparar=1`, ou '
            'Salvar em Configuracoes > Links permanentes no wp-admin. O TOKEN DESTA '
            'ILHA ESTA NO REPOSITORIO, na linha `Sync:` do `PROMPT.md` dela: o '
            'despacho ALTA de 19/11/2026 afirmou o contrario e por isso pediu gesto do '
            'Raphael para um reparo que saiu desta nuvem em um minuto no dia seguinte. '
            'Pela 29.3-a, TENTE antes de escrever que nao da — causa de impossibilidade '
            'envelhece. E desde 20/11/2026 esta ilha tem a cura da porta da 29.4 '
            '(casca 1.16.0, secao 6), o que muda o que esta linha significa: com a cura '
            'carregada, porta no chao e a cura LIVRE e um mundo que se conserta na '
            'proxima requisicao. (Ocorrencias no Arquipelago: clubedomosaico 24/09, '
            '05/10, 08/10 e tres vezes em 11-12/11; robometria 30/10, 11/11 e 19-20/11; '
            'rodametria 05/11 e 17/11.) %s'
            % (len(cods_das_portas), '/'.join(str(c) for c in cods_das_portas),
               leitura_do_retrato_da_porta(porta_publica))
            + leitura_do_contador_da_porta(porta_publica))


def diagnostico_das_quatro_grandezas(cod_home, cods_das_portas, rest_vivo):
    """A REGUA VELHA, DE PROPOSITO — as QUATRO grandezas e nada mais.

    Ela existe para o autoteste poder OBRIGAR as duas a discordar (20.8).
    Autoteste em que a regua velha e a nova concordam nao mede conserto nenhum:
    mede o mundo. Esta e identica a de cima nas quatro grandezas, e e justamente
    isso que tem de ser verdade nos dois mundos que a quinta separa.
    """
    if cod_home != 200 or not rest_vivo:
        return None
    if not cods_das_portas or any(c == 200 for c in cods_das_portas):
        return None

    return '29: A PORTA DE ENTRADA CAIU (quatro grandezas). CONSERTO: rode o flush.'


def leitura_do_retrato_da_porta(porta_publica):
    """A QUINTA GRANDEZA LIDA — e, quando ela nao foi lida, DIZER ISSO.

    Nao escolhe mundo por omissao: retrato ausente devolve a frase que declara a
    ausencia. "Nao medido" escrito e informacao; "nao medido" lido como um dos
    dois vereditos e a familia do comentario que declara mecanismo — parece
    conferido e nao mede nada (32.5-d).

    OS DOIS MUNDOS, e os consertos sao OPOSTOS: (a) o bloco esta no arquivo e o
    Apache o ignora => `AllowOverride` desligado, e pela 29.4 isso e CHAMADO;
    (b) o bloco foi apagado de novo e a trava de uma tentativa por hora ainda
    esta queimada => a ilha volta quando a hora vencer, e nao ha chamado a abrir
    por esta leitura. Mandar abrir chamado em (b), ou mandar esperar em (a), sao
    os dois erros que a 20.5 nomeia.
    """
    if not isinstance(porta_publica, dict) or 'tem_bloco_wordpress' not in porta_publica:
        return ('E A QUINTA GRANDEZA NAO FOI LIDA, e por isso esta linha NAO separa os '
                'dois mundos: `/casca` nao serviu o campo `porta` (casca anterior a '
                '1.16.0 nesta ilha, ou o campo caiu). Sem ele nao se sabe se o bloco '
                'esta no arquivo e o Apache o ignora (AllowOverride => chamado) ou se '
                'ele foi apagado de novo com a hora da trava 2 queimada (=> esperar).')

    tem = porta_publica.get('tem_bloco_wordpress')
    espera = porta_publica.get('cura_liberada_em_s')
    try:
        espera = int(espera)
    except (TypeError, ValueError):
        espera = None

    if tem is None:
        return ('E A QUINTA GRANDEZA DIZ `nao sei`: o arquivo da porta esta ausente ou '
                'ilegivel para o PHP desta ilha, e isso NUNCA se le como porta de pe. '
                'O retrato com token (29.3) e quem fecha este caso.')
    if tem is True:
        return ('E A QUINTA GRANDEZA FECHA A CAUSA, E ELA NAO E DESTA FABRICA: o bloco '
                '`# BEGIN WordPress` ESTA no arquivo e o Apache esta em 404 de todo '
                'jeito. Rodar o `flush` outra vez nao muda nada — isto e '
                '`AllowOverride` desligado do lado do hospedeiro, e pela 29.4 o desfecho '
                'e CHAMADO na HostGator sobre o `.htaccess` da raiz, nao codigo de ilha '
                'nenhuma.')
    if espera and espera > 0:
        return ('E A QUINTA GRANDEZA DIZ QUE NAO HA O QUE CONSERTAR AQUI AGORA: o bloco '
                'esta AUSENTE e a trava 2 da 29.4 (uma tentativa por hora) ainda tem '
                '%d s queimados, entao a cura nao vai tentar antes disso e a ilha fica '
                'no chao ate la. O apagamento passou a ser mais frequente que a trava — '
                'isso e materia do chamado, nao conserto de codigo.' % espera)

    return ('E A QUINTA GRANDEZA DIZ QUE ESTA PASSADA MESMA CONSERTA: bloco AUSENTE com '
            'a cura LIVRE. Abra a raiz desta ilha com uma quebra de cache, que e o que '
            'dispara o gancho, e releia o `/status` procurando a linha `cura da porta:`.')


def leitura_do_contador_da_porta(porta_publica):
    """A SEXTA GRANDEZA — A FREQUENCIA, QUE E O ARGUMENTO DO CHAMADO (29.4-c).

    As cinco grandezas dizem O QUE esta errado e QUAL dos dois consertos e o
    certo. Nenhuma diz QUANTAS VEZES — e a frequencia e a unica coisa que o
    chamado na HostGator ainda nao tinha medida, porque ela era contada pelas
    linhas `cura da porta:` do log, e a cura tenta no maximo uma vez por hora.
    Apagamento que cai dentro da hora queimada nao escreve linha nenhuma; e o
    log e uma janela de 40 linhas que ROLA. Contador nao rola.

    Devolve STRING VAZIA quando nao ha contador, e nao uma frase dizendo zero:
    casca sem a 14-c nao tem o campo, e zero aqui soaria "nunca caiu" com cara
    de conferido. A ausencia e o sinal (20.7), e o campo e `null` por isso.
    """
    if not isinstance(porta_publica, dict):
        return ''
    q = porta_publica.get('quedas')
    if not isinstance(q, dict):
        return ''

    try:
        ep = int(q.get('episodios_vistos'))
    except (TypeError, ValueError):
        return ''
    if ep <= 0:
        return (' E A SEXTA GRANDEZA (a frequencia) DIZ ZERO, e zero aqui NAO quer dizer '
                'que esta porta nunca caiu: o contador conta desde que entrou no ar em '
                '20/11/2026, e as TRES quedas anteriores a ele estao em '
                '`dados/consertos.md`.')

    pedacos = [' E A SEXTA GRANDEZA E A FREQUENCIA, QUE E O ARGUMENTO DO CHAMADO: '
               'o contador viu %d queda(s) nesta porta' % ep]
    try:
        pedacos.append(', com %d reposicao(oes) da cura' % int(q.get('reposicoes_da_cura')))
    except (TypeError, ValueError):
        pass
    primeira = q.get('primeira_no_chao')
    if isinstance(primeira, str) and primeira:
        pedacos.append(', a primeira em %s' % primeira)

    ep_atual = q.get('episodio')
    if isinstance(ep_atual, dict):
        try:
            dur = int(ep_atual.get('duracao_minima_s'))
        except (TypeError, ValueError):
            dur = None
        if dur is not None:
            pedacos.append('. A queda corrente: pelo menos %d s no chao, medidos entre a '
                           'primeira e a ultima leitura (%s a %s) — e `pelo menos` porque '
                           'ela comecou antes da primeira leitura e pode nao ter terminado '
                           'na ultima'
                           % (dur, ep_atual.get('comecou'), ep_atual.get('ultima_no_chao')))
        if ep_atual.get('reposto_depois') is True:
            pedacos.append('. A cura repos o bloco DEPOIS da ultima leitura no chao, '
                           'entao esta queda ja terminou do lado do arquivo')

    pedacos.append('. ESTE NUMERO NAO ROLA com a janela de 40 linhas do log e conta '
                   'tambem o apagamento que cai DENTRO da hora queimada da trava 2, que '
                   'no log nao deixa rastro nenhum. Copie-o para `dados/consertos.md` '
                   'antes de ele ser a unica copia.')

    return ''.join(pedacos)


def itens_e_curas_da_janela(log):
    """SEPARA A LINHA DA CURA DOS ITENS DO DESEMBARQUE — a regua da 20.4.

    POR QUE ISTO E NECESSARIO, e o custo foi medido na rodametria em 12/11/2026,
    2h45 depois de a cura dela ir ao ar: o log vem do mais novo para o mais
    velho, o corte da 20.4 e POSICIONAL, e a linha da cura caiu DENTRO do grupo
    da revisao corrente. A conta de itens acusou 8 declarados contra 9 lidos, e
    a afirmacao positiva do `ok` reprovou uma linha que NUNCA vai dizer `ok`,
    porque nao e um item sendo aplicado. O portao reprovou a ilha sa, e o
    defeito era da regua.

    A LINHA DA CURA SAI DA CONTA DE ITENS E GANHA AFIRMACOES PROPRIAS. Nunca e
    descartada em silencio: linha de classe nova descartada e o mesmo que item
    que rolou para fora da janela — aprovar sobre o que sobrou.

    Devolve (itens, curas) da janela da revisao corrente: do topo ate o fecho
    anterior, exclusive.
    """
    linhas = [l for l in (log or []) if isinstance(l, str)]
    janela = []
    for i, l in enumerate(linhas):
        if REV_RE.search(l) and i > 0:
            break
        janela.append(l)

    curas = [l for l in janela if CURA_RE.search(l)]
    itens = [l for l in janela if not CURA_RE.search(l)]

    return itens, curas


def afirmacoes_da_linha_da_cura(linha):
    """AS AFIRMACOES PROPRIAS DA LINHA DA CURA (trava 3 da 29.4).

    Devolve lista de (condicao, rotulo, medido). Funcao pura: o autoteste
    fabrica a linha, inclusive as deformadas.

    O que ela cobra, lido DA LINHA e nao do codigo que a escreveu: o antes e o
    depois em bytes E em blocos; o bloco do WordPress presente no DEPOIS; o
    arquivo NAO encolhendo (repor bloco nao diminui arquivo — linha que diga
    isso e sinal de que a cura CORTOU em vez de repor); e NENHUM conteudo do
    `.htaccess` dentro da linha, porque o log do `/status` e publico e a 29.3
    poe o conteudo do arquivo atras do token.
    """
    m = CURA_FORMA_RE.search(linha or '')
    if not m:
        return [(False,
                 'a linha da cura tem a forma da trava 3 (bytes e blocos, antes -> depois)',
                 (linha or '(vazia)')[:90])]

    antes_b, antes_bl, depois_b, depois_bl = int(m.group(1)), m.group(2), int(m.group(3)), m.group(4)
    blocos_depois = [b.strip() for b in depois_bl.split(',') if b.strip()]

    return [
        (True, 'a linha da cura tem a forma da trava 3 (bytes e blocos, antes -> depois)',
         '%d [%s] -> %d [%s]' % (antes_b, antes_bl, depois_b, depois_bl)),
        (any(b.lower() == 'wordpress' for b in blocos_depois),
         'o bloco WordPress esta no DEPOIS da linha da cura', depois_bl or '(vazio)'),
        (depois_b >= antes_b,
         'o arquivo NAO encolheu: repor bloco nao diminui .htaccess',
         '%d -> %d bytes' % (antes_b, depois_b)),
        (not re.search(r'Rewrite(Rule|Cond|Engine|Base)|<IfModule', linha, re.I),
         'a linha da cura NAO carrega conteudo do .htaccess (29.3)',
         '%d caracteres' % len(linha)),
    ]


def conferir_porta_de_entrada(carimbo):
    """AS TRES URLs QUE O GOOGLE USA E NENHUMA PAGINA LINKA — secao 29.2.

    ESTE PORTAO NASCEU EM 02/11/2026, QUATRO DIAS DEPOIS DE A ILHA CAIR, E A
    DIVIDA ERA DELE. A 29.2 manda, desde 24/09/2026, que o conferir-no-ar.py de
    TODA ilha meca /wp-sitemap.xml, /robots.txt e /wp-json/ mais o 404 que tem
    de ser 404. Esta ferramenta nao media nenhum dos quatro: a lista PAGINAS
    dela e feita de paginas, e as tres nao sao paginas — sao rota virtual do
    WordPress, nao existem como arquivo em disco, e por isso sao as PRIMEIRAS a
    morrer quando a reescrita do .htaccess some.

    O que custou: em 30/10/2026 a ronda achou 13 de 14 URLs desta ilha em 404,
    servindo a pagina de erro do hospedeiro. Nos quatro dias seguintes o
    `/status` respondeu 200 com a revisao certa, a bancada fechou verde e esta
    ferramenta teria fechado verde na parte do /status — porque todo portao
    desta ilha entra pela raiz, que e a unica porta que continuou aberta (29.1).

    E O 404 QUE TEM DE SER 404 e a metade que quase ninguem escreve: portao que
    so cobra 200 aprova um servidor que responde 200 para tudo, e "tudo
    responde" e um jeito conhecido de uma ilha inteira sair do indice sem
    ninguem ver. O que se mede aqui e de QUEM e a pagina de erro: a do
    hospedeiro tem assinatura propria e nao e a desta ilha.
    """
    print('\n0. A PORTA DE ENTRADA DO SITE (secao 29.2) — as tres URLs que nenhuma pagina linka')

    # (url, rotulo, fragmento obrigatorio do content-type, marca no corpo)
    PORTAS = [
        ('/wp-sitemap.xml', 'xml',   ('xml',),            None),
        ('/robots.txt',     'texto', ('text/plain',),     None),
        ('/wp-json/',       'json',  ('application/json',), None),
    ]

    for caminho, rotulo, tipos, _ in PORTAS:
        corpo, codigo, tipo = buscar_com_tipo(DOMINIO + caminho + '?v=' + carimbo)
        if not ok('200' == codigo, '%s: HTTP 200' % caminho, codigo):
            # A assinatura do hospedeiro, escrita aqui porque e ela que separa
            # "a ilha nao tem a rota" de "o Apache nao entregou ao WordPress".
            if 'hostgator' in corpo.lower():
                print('        ^ o corpo e a pagina de erro do HOSPEDEIRO:'
                      ' assinatura da queda do .htaccess da raiz (29.2/29.3)')
            continue
        ok(any(t in tipo for t in tipos),
           '%s: content-type de %s' % (caminho, rotulo), tipo)

    # O SITEMAP TEM DE TRAZER SITEMAP, nao a pagina do hospedeiro com 200.
    corpo, codigo, _ = buscar_com_tipo(DOMINIO + '/wp-sitemap.xml?v=' + carimbo)
    if '200' == codigo:
        ok(bool(re.search(r'<(sitemap|url)\b', corpo, re.I)),
           '/wp-sitemap.xml: traz XML de sitemap de verdade',
           '%d bytes' % len(corpo))

    # O 404 QUE TEM DE SER 404, e tem de ser o DESTA ilha.
    virgem = '/nao-existe-%s-xyz/' % carimbo
    corpo, codigo, _ = buscar_com_tipo(DOMINIO + virgem)
    if ok('404' == codigo, 'um caminho que a ilha nunca teve responde 404', codigo):
        ok('hostgator' not in corpo.lower(),
           'o 404 NAO e a pagina de erro do hospedeiro',
           '%d bytes' % len(corpo))
        ok('Robometria' in corpo,
           'o 404 e a pagina da PROPRIA ilha', '%d bytes' % len(corpo))

    # ------------------------------------------------------------------
    # A CAUSA NOMEADA (29.7(3)) E O RETRATO PUBLICO DA PORTA (29.4-b/c)
    #
    # ATE 20/11/2026 ESTA FUNCAO TERMINAVA ACIMA, e na queda ela devolvia seis
    # reprovacoes espalhadas — cada uma verdadeira e nenhuma dizendo o que
    # fazer. Foi assim que a queda de 19/11 saiu do relatorio de uma execucao
    # que estava medindo outra coisa.
    #
    # E O PORTAO QUE MEDE A PORTA NAO ENTRA POR ELA (29.7): a leitura do REST
    # aqui e por `?rest_route=`, nunca pelo caminho bonito `/wp-json/...`.
    # Com a porta no chao o caminho bonito morre ANTES do PHP, entao ler por
    # ele mediria a porta duas vezes e nunca o WordPress. A forma bonita
    # continua cobrada acima, como afirmacao da 29.2 — o que muda e que as
    # OUTRAS afirmacoes param de depender dela.
    cods_das_portas = []
    for caminho, _r, _t, _m in PORTAS:
        _c, cod, _tp = buscar_com_tipo(DOMINIO + caminho + '?v=' + carimbo + 'b')
        try:
            cods_das_portas.append(int(cod))
        except (TypeError, ValueError):
            cods_das_portas.append(0)

    _c, cod_home, _tp = buscar_com_tipo(DOMINIO + '/?v=' + carimbo + 'h')
    try:
        cod_home = int(cod_home)
    except (TypeError, ValueError):
        cod_home = 0

    bruto_rest, cod_rest, _tp = buscar_com_tipo(DOMINIO + '/?rest_route=/&v=' + carimbo)
    rest_vivo = ('200' == str(cod_rest))

    # O RETRATO PUBLICO, SEM TOKEN. Ele e a quinta e a sexta grandeza, e a
    # leitura dele NAO reprova nada por si: quem reprova e a porta no chao.
    porta_publica = None
    bruto_casca, cod_casca, _tp = buscar_com_tipo(
        DOMINIO + '/?rest_route=/robometria/v1/casca&v=' + carimbo)
    if '200' == str(cod_casca):
        try:
            d = json.loads(bruto_casca)
        except Exception:
            d = {}
        if isinstance(d, dict):
            ok(d.get('tem_cura_da_porta') is True,
               'a cura da porta da 29.4 esta CARREGADA nesta ilha',
               'tem_cura_da_porta=%s' % d.get('tem_cura_da_porta'))
            # `fonte_do_log_da_cura` em `null` e o UNICO mundo em que a cura,
            # por desenho, NAO acontece: ela nao tem onde escrever a linha da
            # trava 3. Sem este campo, "a cura nunca escreveu linha nenhuma"
            # seria indistinguivel de "a cura nunca precisou escrever".
            ok(bool(d.get('fonte_do_log_da_cura')),
               'a cura tem POR ONDE escrever a linha da trava 3',
               str(d.get('fonte_do_log_da_cura')))
            if isinstance(d.get('porta'), dict):
                porta_publica = d['porta']
                print('        retrato da porta: %s' % json.dumps(porta_publica,
                                                                  ensure_ascii=False))
    else:
        ok(False, 'o /casca responde 200 (retrato publico da porta, 29.4-b)',
           str(cod_casca))

    causa = diagnostico_da_porta(cod_home, cods_das_portas, rest_vivo, porta_publica)
    if causa:
        # ELA E IMPRESSA E NAO AFIRMADA: a reprovacao ja aconteceu acima, nas
        # tres portas. Esta linha diz o que FAZER, e transformar a causa numa
        # afirmacao a mais somaria uma reprovacao em vez de somar informacao.
        print('\n  >>> CAUSA NOMEADA (29.7(3)):\n      ' + causa.replace('. ', '.\n      '))
    else:
        ok(True, 'a assinatura da queda da porta (29) NAO esta na mesa',
           'home %s | portas %s | REST %s' % (cod_home, cods_das_portas,
                                              'vivo' if rest_vivo else 'morto'))

def conferir_cache_do_host():
    """O ENDERECO CANONICO SERVE O QUE O SITE ACABOU DE PUBLICAR? — 14/09/2026.

    A REGUA QUE FALTAVA, e a falta dela deixou esta ferramenta aprovar a revisao
    37 com a pagina de compatibilidade servindo, no ar, a copia das 14h40: sem um
    botao de compra e com a frase proibida pela secao 7 em quatro cartoes. O
    `/status` dizia 37, o log do Sync dizia "10 aplicado(s)", as nove URLs davam
    200 e o titulo batia — tudo verdade, e o leitor na pagina de antes.

    A causa tem assinatura no HTML: `<!--Generated by Endurance Page Cache-->`, o
    cache em arquivo do hospedeiro. Ele purga quando um POST e salvo no wp-admin,
    e o Sync desta ilha grava OPTIONS e atualiza SNIPPETS — nunca passa por la.

    COMO SE MEDE, e por que assim: o mesmo endereco e pedido DUAS vezes, uma
    limpa e outra com uma chave de quebra de cache. A versao com chave nao pode
    ser cacheada, entao ela e o que o WordPress produz AGORA; a limpa e o que o
    leitor recebe. As duas tem que dizer a mesma coisa. Comparar bytes daria
    falso alarme (a chave aparece em link interno e em canonical), entao a
    comparacao e sobre o que o LEITOR ve.

    ESTA REGUA ERA CEGA PARA MUDANCA DE TEXTO, E ISSO FOI MEDIDO EM 14/09/2026,
    19h33Z, pelo teste que o item (b) do despacho da Sentinela pedia. Ela
    comparava TRES CONTAGENS DE MARCADOR e mais nada — enquanto o docstring
    prometia comparar "a revisao servida", que nao existe no HTML e nunca foi
    implementada. A leva do Xiaomi S10 mudou QUAL codigo o artigo-ancora nomeia
    ("HO041, HO400, HO401, HO407, OB010" virou "S20, S10, E10, S12, E12, X20") e
    os numeros contados da ferramenta (63 pares para 71, 73 linhas para 78).
    NENHUMA das tres contagens se move com isso. Medido no ar as 19h33:30Z: o
    canonico servia o texto VELHO, a quebra de cache servia o NOVO, um segundo
    de distancia — e esta funcao aprovaria as duas paginas. Regua que so conta
    estrutura aprova pagina velha sempre que o desembarque mudou palavra.

    ENTAO A AFIRMACAO PASSA A SER SOBRE O TEXTO, e com ela vem a segunda metade
    do que aquele teste mediu: a purga NAO e instantanea. O Sync da revisao 43
    aplicou as 19h30:50Z e o canonico so virou as 19h33:36Z — 166 segundos, com
    a entrada de cache nova criada as 19h33:35Z (`expires` de 21h33:35 com
    `max-age` de 7200 s). Ou seja: a purga pega, e nao pega na hora. Reprovar no
    primeiro segundo transformaria essa janela conhecida em alarme falso — foi
    lendo essa mesma janela como falha que a execucao das 15h17Z gastou quatro
    revisoes de diagnostico e chegou a RETIRAR a purga que funcionava. Por isso
    a comparacao de texto REPETE dentro de um orcamento declarado e IMPRIME o
    atraso que mediu: janela conhecida vira numero, e so o que passa dela
    reprova.
    """
    print('\n10. O ENDERECO CANONICO ESTA SERVINDO O QUE FOI PUBLICADO?')
    chave = 'rbm_quebra_de_cache=%d' % int(time.time())
    for caminho, _nome in PAGINAS:
        url = DOMINIO + caminho
        limpa, _c = buscar(url)
        sep = '&' if '?' in url else '?'
        agora, _c2 = buscar(url + sep + chave)

        for marca, rotulo in (('rbm-comprar', 'saidas de compra'),
                              ('rbm-trilha', 'trilha'),
                              ('rbm-vitrine-acao', 'blocos de compra')):
            n_limpa, n_agora = limpa.count(marca), agora.count(marca)
            ok(n_limpa == n_agora,
               '%s: %s iguais no canonico e no recem-gerado' % (caminho or '/', rotulo),
               '%d contra %d' % (n_limpa, n_agora))

        alvo = _impressao_do_leitor(agora, chave)
        atraso = 0
        if _impressao_do_leitor(limpa, chave) != alvo:
            # A JANELA DA PURGA, gasta so quando ha desacordo — o caso comum
            # nao paga nada. `PURGA_ORCAMENTO_S` e DECLARADO: janela que cresce
            # sozinha vira "espera ate passar", que e o contrario de medir.
            inicio = time.time()
            while time.time() - inicio < PURGA_ORCAMENTO_S:
                time.sleep(PURGA_INTERVALO_S)
                limpa, _c = buscar(url)
                atraso = int(time.time() - inicio)
                if _impressao_do_leitor(limpa, chave) == alvo:
                    break
        ok(_impressao_do_leitor(limpa, chave) == alvo,
           '%s: o TEXTO do canonico e o do recem-gerado' % (caminho or '/'),
           'igual na hora' if not atraso else 'igual depois de %d s' % atraso)


def conferir_piso_no_ar():
    """O PISO DA 25.2 CHEGOU A TELA? — item 4 do despacho do Raphael de 14/09/2026.

    A regua nao le o banco nem o arquivo de dados: ela conta, no HTML servido, os
    marcadores que a porta de compra publica, e cobra a AUSENCIA da frase que a
    secao 7 proibiu. Medir a ausencia e a metade que mais importa — trava que so
    confere o texto novo aprova uma pagina que sirva os dois.
    """
    print('\n11. O PISO DA 25.2 NA TELA (item 4 do despacho do Raphael)')
    com_vitrine = ('/qual-peca-serve-no-meu-robo-aspirador/',
                   '/quantos-pa-o-robo-aspirador-precisa/',
                   '/filtro-universal-de-robo-aspirador/',
                   '/quantos-m2-o-robo-aspirador-limpa-por-carga/')
    for caminho, _nome in PAGINAS:
        corpo, _c = buscar(DOMINIO + caminho)
        m = re.search(r'<main[^>]*>(.*?)</main>', corpo, re.S | re.I)
        miolo = m.group(1) if m else ''
        # A REGUA MEDIA A PALAVRA E NAO A COISA, e em 21/09/2026 ela reprovou
        # duas paginas CERTAS por isso.
        #
        # O que a secao 7 proibe, com todas as letras, e "link de loja em breve":
        # uma PROMESSA no lugar de uma saida de compra que nao existe — "item que
        # chegaria a ela e defeito da 19.1, nao e estado aceitavel de pagina no
        # ar". E o que a 16.5 MANDA, com as mesmas letras, e que o cartao de uma
        # categoria ainda nao publicada "nao e link e diz 'em breve', sem contagem
        # de banco".
        #
        # Sao duas frases iguais em dois lugares diferentes: uma promete um LINK
        # DE COMPRA que a ilha nao tem, a outra avisa que uma PAGINA ainda nao
        # nasceu. Medir a palavra solta no miolo inteiro confundia as duas e
        # fazia a primeira leva de malha reprovar por obedecer ao contrato.
        #
        # Entao a regua passou a medir onde a proibicao vale — o bloco de compra
        # e a vitrine — e a frase inteira em qualquer lugar. Isto NAO e afrouxar:
        # a proibicao da secao 7 continua cobrada byte a byte onde ela existe, e
        # o que saiu de cobranca e o que o contrato manda publicar.
        vitrine = ' '.join(re.findall(
            r'<(?:li|div|span|p)[^>]*class="[^"]*(?:rbm-vitrine|rbm-comprar|rbm-compra)[^"]*"[^>]*>.*?'
            r'</(?:li|div|span|p)>', miolo, re.S | re.I))
        proibida = ('link de loja em breve' in miolo.lower()) or ('em breve' in vitrine.lower())
        ok(not proibida,
           '%s: sem a frase proibida pela secao 7 (promessa no lugar da compra)' % (caminho or '/'),
           'ausente' if not proibida else 'AINDA NO AR')
        ok('rbm-sem-saida' not in miolo,
           '%s: nenhum item sem saida de compra' % (caminho or '/'))
        if caminho in com_vitrine:
            # EM 16/09/2026 ESTA CONTA PAROU DE MEDIR UM DEGRAU E PASSOU A MEDIR A
            # ESCADA. Ela cobrava `rbm-comprar-cru` > 0, ou seja, exigia que a
            # vitrine saisse pelo degrau 4 da 25.1 — a busca CRUA. No dia em que
            # os 35 links de busca encurtada entraram no banco, as duas paginas de
            # PECA subiram para o degrau 3 e esta regua reprovou as duas, no ar,
            # por terem melhorado. As de MODELO continuaram cruas, porque os links
            # chegaram nas pecas e nao nos modelos — entao a regua nem sequer
            # reprovava de forma uniforme: ela premiava quem nao tinha avancado.
            #
            # O que ela quer dizer, e sempre quis, e "a vitrine TEM saida de
            # compra". O degrau e informacao, nao criterio — e sai impresso ao
            # lado, porque saber em qual degrau cada pagina esta e o jeito de ver
            # o encurtamento avancando sem precisar de outra medicao.
            # E EM 16/09/2026, A TARDE, ELA CAIU DE NOVO — pelo MESMO motivo,
            # um degrau acima. A correcao da manha trocou `rbm-comprar-cru` por
            # `rbm-comprar-busca` e continuou amarrada a UM degrau: quando a
            # Open API da Shopee trouxe ficha de produto, os cinco modelos do
            # A2 subiram outra vez, a busca sumiu da pagina e a regua reprovou
            # a melhora NO AR. Sexta regua desta ilha a cometer o mesmo erro.
            #
            # Trocar a classe de novo so adiaria a terceira queda. O que
            # sobrevive a qualquer degrau e contar CARTAO contra BLOCO DE
            # COMPRA: a vitrine tem saida quando todo cartao tem um, e o degrau
            # de cada um sai impresso ao lado como informacao.
            cru = miolo.count('rbm-comprar-cru')
            busca = miolo.count('rbm-comprar-busca')
            cartoes = miolo.count('class="rbm-vitrine-item"')
            blocos = miolo.count('class="rbm-vitrine-acao"')
            ficha = blocos - busca - cru
            ok(cartoes > 0 and blocos == cartoes,
               '%s: todo cartao da vitrine tem bloco de compra' % caminho,
               '%d cartao(oes), %d bloco(s) | degraus: %d ficha, %d busca, %d crua'
               % (cartoes, blocos, ficha, busca, cru))
            pagos = re.findall(r'<a class="[^"]*rbm-comprar-cru[^"]*"[^>]*rel="[^"]*sponsored',
                               miolo, re.I)
            ok(not pagos,
               '%s: a busca crua nao se declara patrocinada' % caminho,
               '%d carimbada(s) por engano' % len(pagos))


def conferir_variante_sem_cabecalho():
    """O ITEM 1 DO DESPACHO DA SENTINELA DE 14/09/2026, medido e nao fechado por cima.

    A correcao obvia — mandar um Accept-Encoding e seguir a vida — conserta a
    LEITURA desta ferramenta e apaga o defeito da vista, e a Sentinela proibiu
    isso com todas as letras: "nao feche este item ampliando a regua. Isso troca o
    defeito por uma regua que nao o enxerga. A regua tem de continuar medindo a
    variante que hoje esta errada."

    Entao ela e medida AQUI, de proposito, como a unica parte desta ferramenta que
    pede a pagina do jeito errado. Enquanto o cache guardar a copia de 11/09 para
    quem chega sem cabecalho, esta funcao REPROVA e a conferencia no ar da ilha
    inteira fica vermelha — que e o estado honesto: metade dos clientes que nao
    negociam compressao le uma pagina de tres dias atras, sem trilha e sem
    BreadcrumbList, e a secao 5 chama visibilidade em IA de regra de primeira
    classe.

    O CRITERIO E O QUE A PROPRIA SENTINELA ESCREVEU: para cada URL do sitemap, o
    numero de ocorrencias da trilha e o <title> servido tem de ser IGUAIS nas duas
    variantes. Nao se mede tamanho em bytes: compressao muda o tamanho e nao muda a
    pagina.
    """
    print('\n9. A VARIANTE QUE O CACHE CONGELOU (item 1 do despacho de 14/09)')
    for caminho, _nome in PAGINAS:
        url = DOMINIO + caminho
        com, _c1 = buscar(url)
        # REPETIR RESPOSTA VAZIA NAO E AMPLIAR A REGUA, e a diferenca importa
        # porque a Sentinela proibiu ampliar com todas as letras em 14/09/2026:
        # *"nao feche este item ampliando a regua"*. O pedido continua sendo o
        # MESMO pedido errado de sempre — sem cabecalho nenhum, que e o defeito
        # que esta funcao existe para medir. O que mudou e que corpo VAZIO deixou
        # de ser comparado com uma pagina: vazio nao e "outra pagina", e
        # NENHUMA pagina, e comparar pagina com nada mede o tunel e nao o cache.
        # Medido em 16/09/2026: a resposta vazia caiu em /metodologia/ numa
        # passada e em /divulgacao-de-afiliados/ na seguinte, e as duas
        # devolveram 200 com a trilha inteira em tres e quatro repeticoes.
        # URL que muda a cada passada e rede; defeito de cache fica parado.
        sem = ''
        for _tentativa in range(3):
            r = subprocess.run(['curl', '-s', '--max-time', '40', url],
                               capture_output=True, text=True)
            sem = r.stdout
            if sem.strip():
                break
            time.sleep(2)

        t_com = texto_da_tag(com, r'<title[^>]*>(.*?)</title>')
        t_sem = texto_da_tag(sem, r'<title[^>]*>(.*?)</title>')
        ok(t_com == t_sem,
           'mesmo <title> com e sem cabecalho em %s' % (caminho or '/'),
           'com: %r | sem: %r' % (t_com[:34], t_sem[:34]))

        n_com, n_sem = com.count('rbm-trilha'), sem.count('rbm-trilha')
        ok(n_com == n_sem,
           'mesma trilha com e sem cabecalho em %s' % (caminho or '/'),
           '%d contra %d' % (n_com, n_sem))


def conferir_lugar_vazio_da_foto(carimbo):
    """O DESPACHO DO RAPHAEL DE 16/09/2026, medido no HTML SERVIDO.

    O lugar vazio da foto estava desenhado como `border-radius:50%` com um lado
    transparente — a forma universal do spinner. Quem chegava na pagina nao lia
    "esta peca nao tem foto"; lia "a foto esta carregando" e, como ela nunca
    carrega, lia "este site esta quebrado". Numa ilha cujo argumento inteiro e
    procedencia, parecer quebrada custa mais do que parecer simples.

    POR QUE ISTO E MEDIDO NO AR E NAO SO NA BANCADA: a frase "sem foto" nao
    esta no HTML que o shortcode devolve — ela sai de `content:` numa regra da
    folha da casca, e a folha so chega ao leitor porque a casca a imprime num
    <style> da propria pagina. Bancada verde com folha que nao embarcou e
    exatamente o defeito do titulo da Aquametria em 11/09/2026: cada portao
    lendo a metade que estava certa.

    E A AFIRMACAO DO PAINEL E LIDA POR ESTRUTURA, NUNCA POR CONTAGEM FIXA. Cada
    `.rbm-vitrine-foto` tem de trazer OU uma <img> OU o painel vazio, nunca os
    dois e nunca nenhum. Contar "um painel por cartao" seria o mesmo que exigir
    que nenhum item tenha foto — a regua morreria no dia da primeira imagem, que
    e o dia que o despacho da API da Shopee esta trazendo.
    """
    print('\n12. O LUGAR VAZIO DA FOTO DIZ O QUE E (despacho do Raphael, 16/09)')

    # Uma pagina por ferramenta: R1, R2, A1 e A2, nesta ordem.
    das_ferramentas = [
        '/qual-peca-serve-no-meu-robo-aspirador/',
        '/quantos-pa-o-robo-aspirador-precisa/',
        '/filtro-universal-de-robo-aspirador/',
        '/quantos-m2-o-robo-aspirador-limpa-por-carga/',
    ]

    paineis_medidos = 0
    for caminho in das_ferramentas:
        corpo_servido, codigo = buscar(DOMINIO + caminho + '?v=' + carimbo)
        if not ok('200' == codigo, 'HTTP 200 em %s' % caminho, codigo):
            continue

        folha = '\n'.join(re.findall(r'<style\b[^>]*>(.*?)</style>',
                                     corpo_servido, re.S | re.I))
        ok('.rbm-vitrine-vazia::after{content:"sem foto";}' in folha,
           '%s: a folha servida escreve "sem foto" no painel vazio' % caminho)

        regra = re.search(r'\.rbm-vitrine-vazia\{([^}]*)\}', folha)
        ok(regra is not None, '%s: a folha servida declara .rbm-vitrine-vazia' % caminho)
        if regra:
            ok('border-radius' not in regra.group(1),
               '%s: o painel vazio NAO e um anel' % caminho,
               regra.group(1)[:60])

        # AS AFIRMACOES SOBRE O QUE A PAGINA DIZ SE MEDEM NO CORPO (secao 8):
        # a folha tambem cita a classe, e conta-la no HTML inteiro daria um a
        # mais sem nenhum cartao a mais.
        miolo = corpo_da_pagina(corpo_servido)
        # O recorte vai do painel ate o irmao seguinte, que e sempre
        # `rbm-vitrine-tipo` nas quatro ferramentas. Contar aninhamento de
        # <span> na mao seria mais fragil, nao menos: o painel guarda OU um
        # <img> OU um <span>, e o irmao seguinte e o mesmo nas quatro.
        paineis = re.findall(
            r'<span class="rbm-vitrine-foto"[^>]*>(.*?)<span class="rbm-vitrine-tipo"',
            miolo, re.S)
        painel_ruim = []
        for dentro in paineis:
            tem_img = '<img' in dentro
            tem_vazio = 'rbm-vitrine-vazia' in dentro
            if tem_img and tem_vazio:
                painel_ruim.append('foto E "sem foto" no mesmo painel')
            elif not tem_img and not tem_vazio:
                painel_ruim.append('painel sem foto e sem aviso')
        paineis_medidos += len(paineis)
        ok(not painel_ruim,
           '%s: todo painel traz OU a foto OU o aviso, nunca os dois' % caminho,
           '%d painel(eis)%s' % (len(paineis),
                                 '' if not painel_ruim else ': ' + painel_ruim[0]))

    # CONTRA O PORTAO INERTE: quatro paginas de ferramenta servem vitrine, entao
    # zero painel medido e defeito da regua, nao aprovacao da pagina.
    ok(paineis_medidos > 0, 'a conferencia mediu painel de verdade',
       '%d painel(eis) nas quatro ferramentas' % paineis_medidos)

    # ---------------------------------------------------------------- A FOTO
    # Acrescentado as 17h de 16/09/2026, quando a Open API da Shopee trouxe as
    # 27 primeiras fotos desta ilha. A afirmacao NAO conta fotos: contar seria
    # amarrar a regua a composicao do banco de hoje, que e o erro que cinco
    # reguas desta ilha ja cometeram. O que ela cobra e que TODA foto servida
    # seja utilizavel — dimensao declarada (senao a pagina pula), alt de
    # verdade (acessibilidade e leitura de IA, secao 5) e endereco que existe
    # no banco (senao a tela publica imagem que ninguem colheu).
    with open('dados/pecas.json', encoding='utf-8') as f:
        _banco = [r for r in json.load(f)['registros']]
    with open('dados/modelos-robo.json', encoding='utf-8') as f:
        _banco += [r for r in json.load(f)['registros']]
    urls_do_banco = set(
        (r.get('imagem') or {}).get('url') for r in _banco
        if (r.get('imagem') or {}).get('url'))

    fotos_servidas, defeitos = 0, []
    for caminho in das_ferramentas:
        corpo_servido, codigo = buscar(DOMINIO + caminho + '?v=' + carimbo)
        if '200' != codigo:
            continue
        for tag in re.findall(r'<img class="rbm-vitrine-img"[^>]*>', corpo_servido):
            fotos_servidas += 1
            src = re.search(r'src="([^"]*)"', tag)
            alt = re.search(r'alt="([^"]*)"', tag)
            largura = re.search(r'width="(\d+)"', tag)
            altura = re.search(r'height="(\d+)"', tag)
            if not (largura and altura and int(largura.group(1)) > 0
                    and int(altura.group(1)) > 0):
                defeitos.append('%s: <img> sem dimensao declarada' % caminho)
            if not (alt and alt.group(1).strip()):
                defeitos.append('%s: <img> sem alt' % caminho)
            if 'loading="lazy"' not in tag:
                defeitos.append('%s: <img> sem loading=lazy' % caminho)
            if not src or html.unescape(src.group(1)) not in urls_do_banco:
                defeitos.append('%s: <img> com endereco que nao esta no banco' % caminho)

    ok(not defeitos, 'toda foto servida tem dimensao, alt, lazy e endereco do banco',
       '%d foto(s) nas quatro ferramentas%s'
       % (fotos_servidas, '' if not defeitos else ' | ' + defeitos[0]))


def conferir_datas_no_ar(carimbo):
    """AS DUAS DATAS DO JSON-LD SERVIDO — item 4 do despacho da Sentinela de
    16/09/2026.

    A regua le `dados/datas-das-paginas.json`, que e a fonte unica do campo, e
    exige que o HTML SERVIDO traga exatamente aquelas duas datas no no Article.
    Nao basta o snippet estar certo: o defeito que o despacho mediu era de
    ORIGEM do campo, e origem errada passa por qualquer bancada que compare o
    snippet consigo mesmo.

    E ela cobra a AUSENCIA do valor antigo: enquanto `gerado_em` dos fatos
    divergir da data da pagina, servir `gerado_em` reprova. Medir so o valor
    novo aprovaria uma pagina que servisse os dois.
    """
    print('\n13. AS DUAS DATAS DO JSON-LD (item 4 do despacho da Sentinela)')
    doc = json.load(open('dados/datas-das-paginas.json', encoding='utf-8'))
    # O SLUG DE UMA PAGINA DE MALHA NAO E O ENDERECO DELA: o slug e a chave
    # (pecas-filtros-xiaomi) e o endereco tem tres niveis
    # (/pecas/filtros/xiaomi/). Montar a URL a partir do slug aqui media um 404
    # e reprovava a pagina certa.
    caminho_da_malha = {p[0].strip('/').replace('/', '-'): p[0]
                        for p in paginas_da_malha()}
    for registro in doc['registros']:
        caminho = caminho_da_malha.get(registro['slug'], '/%s/' % registro['slug'])
        corpo, codigo = buscar(DOMINIO + caminho + '?v=' + carimbo)
        if not ok('200' == codigo, '%s: HTTP 200' % caminho, codigo):
            continue
        artigo = {}
        for bruto in re.findall(
                r'<script type="application/ld\+json"[^>]*>(.*?)</script>',
                corpo, re.S | re.I):
            try:
                grafo = json.loads(html.unescape(bruto))
            except Exception:
                continue
            for no in (grafo.get('@graph') if isinstance(grafo, dict)
                       and grafo.get('@graph') else [grafo]):
                # ARTICLE OU COLLECTIONPAGE: as duas datas nao sao do artigo, sao
                # da PAGINA, e desde 21/09/2026 ha paginas desta ilha que nao sao
                # artigo nenhum. Exigir 'Article' aqui era exigir que toda pagina
                # datada fosse um texto — e reprovaria a malha por servir o
                # schema certo.
                if isinstance(no, dict) and no.get('@type') in ('Article', 'CollectionPage'):
                    artigo = no
        if not ok(bool(artigo), '%s: o no com as datas do JSON-LD foi encontrado' % caminho):
            continue
        ok(artigo.get('datePublished') == registro['publicada_em'],
           '%s: datePublished servido e o da fonte unica' % caminho,
           '%s x %s' % (artigo.get('datePublished'), registro['publicada_em']))
        ok(artigo.get('dateModified') == registro['modificada_em'],
           '%s: dateModified servido e o da fonte unica, medida do git' % caminho,
           '%s x %s' % (artigo.get('dateModified'), registro['modificada_em']))

def conferir_busca_com_resultado(carimbo):
    """A BUSCA DO BOTAO TEM RESULTADO? — itens 1 e 3 do despacho da Sentinela de
    16/09/2026.

    O item 1 mediu que quatro registros mandavam o leitor a uma busca de ZERO
    resultado, e nomeou a pagina em que isso doi mais: a de PECA do W300, cujo
    assunto inteiro e a saida de compra. A trava nao consegue contar resultado
    daqui — `shopee.com.br/api/v4/search/search_items` devolve
    `error 90309999, redirect_to_error_page` desta nuvem e a pagina de busca serve
    casca de JavaScript identica byte a byte para palavras diferentes (remedido em
    16/09/2026). O que ela CONSEGUE, e e o que fecha o item: exigir que todo link
    de compra servido nessa pagina seja um link cuja palavra-chave foi MEDIDA e
    devolveu resultado.

    O elo que isso guarda e o unico que o encurtamento esconde: depois de
    encurtado, `s.shopee.com.br/XXXX` nao diz mais para onde vai. Sem esta
    conferencia, trocar a palavra-chave sem regerar o link curto serviria a busca
    de ontem com o carimbo de hoje, e nenhuma regua veria.
    """
    print('\n14. A BUSCA DO BOTAO TEM RESULTADO (itens 1 e 3 do despacho)')
    medicao = json.load(open('dados/palavras-chave-medidas.json', encoding='utf-8'))
    pecas = json.load(open('dados/pecas.json', encoding='utf-8'))['registros']
    por_id = {r['id']: r for r in pecas}
    medido = {r['id']: r['escolhido'] for r in medicao['registros']}

    caminho = '/qual-peca-serve-no-meu-robo-aspirador/?modelo=wap-w300&peca=escova%20lateral'
    corpo, codigo = buscar(DOMINIO + caminho + '&v=' + carimbo)
    if not ok('200' == codigo, 'a pagina do W300 com escova lateral responde 200', codigo):
        return
    curtos = set(re.findall(r'https://s\.shopee\.com\.br/[A-Za-z0-9]+', corpo))
    ok(len(curtos) >= 2, 'a pagina serve os botoes de compra das duas escovas',
       '%d link(s) curto(s)' % len(curtos))

    # De quem e cada link curto servido, e a chave dele tinha resultado?
    dono = {}
    for ident, reg in por_id.items():
        for chave in ('url', 'url_busca'):
            valor = (reg.get('afiliado') or {}).get(chave) or ''
            if valor:
                dono[valor] = ident
    orfaos = [u for u in curtos if u not in dono]
    ok(not orfaos, 'todo link curto servido esta no banco desta ilha',
       'orfaos: %s' % (orfaos[:2] if orfaos else 'nenhum'))

    sem_resultado = []
    for u in curtos:
        ident = dono.get(u)
        if ident and (medido.get(ident) or {}).get('resultados', 0) <= 0:
            sem_resultado.append(ident)
    ok(not sem_resultado,
       'nenhum botao servido aponta para busca medida em ZERO resultado',
       'medicao de %s | %s' % (medicao['gerado_em'],
                               sem_resultado or 'todos com resultado'))

    # E A VARREDURA INTEIRA, porque uma pagina nao e a ilha (secao 8).
    zeradas = [r['id'] for r in medicao['registros']
               if (r.get('escolhido') or {}).get('resultados', 0) <= 0]
    ok(not zeradas, 'nenhum registro publicavel tem palavra-chave medida em zero',
       '%d de %d registros medidos' % (len(zeradas), len(medicao['registros'])))



def autoteste():
    """OS MUNDOS DA PORTA, FABRICADOS — porque nenhum deles se encena no disco.

    POR QUE ELE EXISTE. As funcoes acima decidem, na queda, qual dos DOIS
    consertos opostos e o certo: chamado na HostGator ou esperar a trava vencer.
    Regua que so roda na queda e regua que estreia no pior dia possivel. Aqui os
    mundos sao dados a ela, e cada um tem de sair com um desfecho DIFERENTE.

    E A REGUA VELHA E OBRIGADA A DISCORDAR (20.8): as quatro grandezas tem de
    ser IDENTICAS nos dois mundos que a quinta separa — se elas ja os
    separassem, a quinta nao estaria consertando nada e este autoteste estaria
    medindo o mundo em vez da regua.
    """
    global falhas, feitos
    print('AUTOTESTE — as grandezas da porta (29.7(3)), a janela da 20.4 e a linha da cura')
    print('=' * 78)

    def diz(cond, rotulo, medido=''):
        ok(cond, rotulo, medido)

    PORTAS_CAIDAS = [404, 404, 404]

    # ---- 1. A ASSINATURA NAO ESTA NA MESA: a funcao DEVOLVE None -------------
    # Causa inventada e a proxima execucao consertando a coisa errada (29.5),
    # entao cada um destes mundos tem de recusar o diagnostico.
    diz(diagnostico_da_porta(200, [200, 200, 200], True) is None,
        '1. portas em 200: nao ha causa a nomear')
    diz(diagnostico_da_porta(200, [404, 200, 404], True) is None,
        '1-b. UMA porta em 200 ja tira a assinatura da mesa')
    diz(diagnostico_da_porta(500, PORTAS_CAIDAS, True) is None,
        '1-c. home MORTA e outro mundo: a causa nao e esta')
    diz(diagnostico_da_porta(200, PORTAS_CAIDAS, False) is None,
        '1-d. REST morto nas duas formas e outro mundo: a causa nao e esta')
    diz(diagnostico_da_porta(200, [], True) is None,
        '1-e. nenhuma porta medida nao e queda medida')

    # ---- 2. A ASSINATURA ESTA NA MESA ---------------------------------------
    base = diagnostico_da_porta(200, PORTAS_CAIDAS, True)
    diz(base is not None, '2. assinatura na mesa: a causa e nomeada')
    diz('BEGIN WordPress' in base,
        '2-b. a causa NOMEIA o bloco que saiu do .htaccess')
    diz('flush_rewrite_rules' in base and 'reparar=1' in base,
        '2-c. a causa carrega o CONSERTO, nao so o sintoma')
    diz('ESTA NO REPOSITORIO' in base,
        '2-d. a causa diz que o token DESTA ilha esta no repositorio — '
        'a deducao errada de 19/11 nao volta por aqui')

    # ---- 3. A QUINTA GRANDEZA SEPARA OS DOIS MUNDOS -------------------------
    # E A REGUA VELHA TEM DE SER IDENTICA NOS DOIS. Esta e a unica prova de que
    # a quinta grandeza conserta algo.
    m_allowoverride = {'tem_bloco_wordpress': True,  'cura_liberada_em_s': 0}
    m_hora_queimada = {'tem_bloco_wordpress': False, 'cura_liberada_em_s': 2057}
    m_cura_livre    = {'tem_bloco_wordpress': False, 'cura_liberada_em_s': 0}
    m_nao_sei       = {'tem_bloco_wordpress': None,  'cura_liberada_em_s': 0}

    velha_a = diagnostico_das_quatro_grandezas(200, PORTAS_CAIDAS, True)
    velha_b = diagnostico_das_quatro_grandezas(200, PORTAS_CAIDAS, True)
    diz(velha_a == velha_b and velha_a is not None,
        '3. a regua VELHA (quatro grandezas) e IDENTICA nos dois mundos (20.8)')

    nova_a = diagnostico_da_porta(200, PORTAS_CAIDAS, True, m_allowoverride)
    nova_b = diagnostico_da_porta(200, PORTAS_CAIDAS, True, m_hora_queimada)
    diz(nova_a != nova_b,
        '3-b. e a NOVA os separa — autoteste em que as duas concordam nao mede conserto')
    diz('CHAMADO na HostGator' in nova_a and 'AllowOverride' in nova_a,
        '3-c. bloco PRESENTE com portas em 404 => chamado, nao flush de novo')
    diz('2057 s queimados' in nova_b and 'nao conserto de codigo' in nova_b,
        '3-d. bloco AUSENTE com a hora queimada => esperar, e o numero sai do retrato')
    nova_c = diagnostico_da_porta(200, PORTAS_CAIDAS, True, m_cura_livre)
    diz('ESTA PASSADA MESMA CONSERTA' in nova_c,
        '3-e. bloco AUSENTE com a cura LIVRE => abrir a raiz conserta')
    nova_d = diagnostico_da_porta(200, PORTAS_CAIDAS, True, m_nao_sei)
    diz('`nao sei`' in nova_d and 'NUNCA se le como porta de pe' in nova_d,
        '3-f. `null` e "nao sei" e NUNCA porta de pe — a confusao que custa um chamado')

    # ---- 4. O RETRATO QUE NAO VEIO DIZ QUE NAO VEIO -------------------------
    # "Nao medido" escrito e informacao; "nao medido" lido como veredito e a
    # familia do comentario que declara mecanismo (32.5-d).
    for ruim in (None, {}, [], 'sei la', {'cura_liberada_em_s': 0}):
        linha = diagnostico_da_porta(200, PORTAS_CAIDAS, True, ruim)
        diz('NAO FOI LIDA' in linha,
            '4. retrato %r: a linha DIZ que nao separou os mundos' % (ruim,))

    # ---- 5. A SEXTA GRANDEZA ------------------------------------------------
    # Ela ACRESCENTA a linha das cinco, nunca a reescreve.
    com_contador = dict(m_hora_queimada)
    com_contador['quedas'] = {
        'episodios_vistos': 4, 'leituras_no_chao': 91, 'leituras_nao_sei': 0,
        'reposicoes_da_cura': 2, 'primeira_no_chao': '2026-11-19 19:30',
        'episodio': {'comecou': '2026-11-20 09:00',
                     'ultima_no_chao': '2026-11-20 10:16',
                     'duracao_minima_s': 4560, 'reposto_depois': False},
    }
    linha6 = diagnostico_da_porta(200, PORTAS_CAIDAS, True, com_contador)
    diz(linha6.startswith(nova_b),
        '5. a sexta grandeza ACRESCENTA a linha das cinco, nunca a reescreve')
    diz('viu 4 queda(s)' in linha6 and '2 reposicao(oes)' in linha6,
        '5-b. a frequencia sai do contador, nao do log')
    diz('pelo menos 4560 s no chao' in linha6,
        '5-c. a duracao e dita como PISO, porque a queda comecou antes da 1a leitura')
    diz('NAO ROLA' in linha6 and 'consertos.md' in linha6,
        '5-d. a linha manda copiar o numero antes de ele ser a unica copia')

    # ZERO NAO E "NUNCA CAIU", e esta ilha tem TRES quedas anteriores ao contador.
    zero = dict(m_hora_queimada)
    zero['quedas'] = {'episodios_vistos': 0, 'leituras_no_chao': 0,
                      'leituras_nao_sei': 3, 'reposicoes_da_cura': 0}
    l_zero = diagnostico_da_porta(200, PORTAS_CAIDAS, True, zero)
    diz('DIZ ZERO' in l_zero and 'TRES quedas anteriores' in l_zero,
        '5-e. zero no contador diz o que o zero NAO prova')

    # CONTADOR QUE NAO E CONTADOR NAO E PROVA DE NADA: a sexta grandeza se cala.
    for ruim in (None, {}, [], '4', {'episodios_vistos': 'muitas'}):
        corpo = dict(m_hora_queimada)
        corpo['quedas'] = ruim
        l = diagnostico_da_porta(200, PORTAS_CAIDAS, True, corpo)
        diz(l == nova_b,
            '5-f. `quedas` = %r: a sexta grandeza se CALA e as cinco ficam '
            'inteiras' % (ruim,))

    # ---- 6. A JANELA DA 20.4 E A LINHA DA CURA ------------------------------
    # O corte e POSICIONAL: do topo ate o fecho ANTERIOR, exclusive.
    CURA = ('2026-11-20 10:15 cura da porta: bloco WordPress reposto — '
            '1057 bytes [NFD EPC] -> 1580 bytes [NFD EPC, WordPress]')
    log = [
        'revisao 97: 3 aplicado(s), 0 aguardando desembarque',
        'snippets/robometria-casca: ok',
        CURA,
        'snippets/robometria-sync: ok',
        'revisao 96: 1 aplicado(s), 0 aguardando desembarque',
        'snippets/robometria-r2: ok',
    ]
    itens, curas = itens_e_curas_da_janela(log)
    diz(len(curas) == 1, '6. a linha da cura e ACHADA dentro da janela corrente',
        '%d cura(s)' % len(curas))
    diz(len(itens) == 3,
        '6-b. e ela SAI da conta de itens: 3 itens, nao 4 — o defeito de 12/11/2026 '
        'da irma, em que 8 declarados contra 9 lidos reprovou a ilha sa',
        '%d item(ns)' % len(itens))
    diz(all(CURA_RE.search(l) is None for l in itens),
        '6-c. nenhuma linha de cura sobrou entre os itens')
    diz(not any('revisao 96' in l for l in itens),
        '6-d. a janela para no fecho ANTERIOR: o corte e posicional')

    # A CONFUSAO PELO AVESSO: um snippet CHAMADO cura-da-porta sendo APLICADO
    # **e** item de desembarque, e tira-lo da conta seria o mesmo furo.
    log_avesso = ['revisao 98: 1 aplicado(s), 0 aguardando desembarque',
                  'snippets/robometria-cura-da-porta: ok']
    itens2, curas2 = itens_e_curas_da_janela(log_avesso)
    diz(len(curas2) == 0 and len(itens2) == 2,
        '6-e. snippet CHAMADO cura-da-porta sendo aplicado CONTINUA sendo item — '
        'o reconhecimento e pela frase `cura da porta:`, nunca pelo nome do arquivo')

    # LOG VAZIO OU AUSENTE NAO EXPLODE E NAO INVENTA JANELA.
    for vazio in (None, [], ['linha solta sem fecho de revisao']):
        i, c = itens_e_curas_da_janela(vazio)
        diz(isinstance(i, list) and isinstance(c, list) and not c,
            '6-f. log %r: nenhuma cura e nenhuma excecao' % (vazio,))

    # ---- 7. AS AFIRMACOES PROPRIAS DA LINHA DA CURA -------------------------
    boas = afirmacoes_da_linha_da_cura(CURA)
    diz(all(c for c, _r, _m in boas),
        '7. a linha de cura BEM FORMADA passa nas quatro afirmacoes da trava 3',
        '%d afirmacao(oes)' % len(boas))

    # E CADA DEFORMACAO TEM DE REPROVAR, senao a afirmacao nao mede nada.
    SEM_WP = ('2026-11-20 10:15 cura da porta: bloco WordPress reposto — '
              '1057 bytes [NFD EPC] -> 1057 bytes [NFD EPC]')
    diz(any(not c for c, _r, _m in afirmacoes_da_linha_da_cura(SEM_WP)),
        '7-b. depois SEM o bloco WordPress REPROVA')

    ENCOLHEU = ('2026-11-20 10:15 cura da porta: bloco WordPress reposto — '
                '1580 bytes [NFD EPC, WordPress] -> 900 bytes [WordPress]')
    rep = afirmacoes_da_linha_da_cura(ENCOLHEU)
    diz(any(not c for c, r, _m in rep if 'NAO encolheu' in r),
        '7-c. arquivo que ENCOLHEU reprova: repor bloco nao diminui .htaccess — '
        'linha que diga isso e sinal de que a cura CORTOU em vez de repor')

    VAZOU = ('2026-11-20 10:15 cura da porta: bloco WordPress reposto — '
             '1057 bytes [NFD EPC] -> 1580 bytes [NFD EPC, WordPress] '
             'RewriteRule ^index.php$ - [L]')
    diz(any(not c for c, r, _m in afirmacoes_da_linha_da_cura(VAZOU)
            if 'conteudo do .htaccess' in r),
        '7-d. linha que CARREGA conteudo do .htaccess reprova (29.3): o log do '
        '/status e publico e a rota de diagnostico pelo menos pede token')

    for disforme in ('', None, 'cura da porta: deu certo',
                     'cura da porta: 1057 -> 1580'):
        r = afirmacoes_da_linha_da_cura(disforme)
        diz(len(r) == 1 and not r[0][0],
            '7-e. linha %r: a FORMA da trava 3 reprova de uma vez' % (disforme,))

    # A LINHA DE RECUSA DA CURA NAO E A LINHA DE SUCESSO, e a 20.5 cobra palavra
    # DIFERENTE: o conserto dos dois mundos nao e o mesmo.
    FALHOU = ('2026-11-20 10:15 cura da porta FALHOU: o flush rodou e o bloco '
              'WordPress NAO voltou — 1057 bytes [NFD EPC]')
    diz(CURA_FORMA_RE.search(FALHOU) is None,
        '7-f. a linha de FALHA nao e lida como sucesso: ela nao tem a forma '
        'antes -> depois, porque nao houve depois')

    print('=' * 78)
    print('autoteste: %d afirmacoes, %d falha(s)' % (feitos, falhas))
    print('APROVADO' if falhas == 0 else 'REPROVADO')
    return 1 if falhas else 0


if __name__ == '__main__':
    # O AUTOTESTE RODA SEM REDE, de proposito: ele mede a REGUA, nunca a ilha.
    # E por isso que o `bancada.py` desta ilha o alcanca sem `--no-ar`.
    if '--autoteste' in sys.argv:
        sys.exit(autoteste())
    sys.exit(main())
