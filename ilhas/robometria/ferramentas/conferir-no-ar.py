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

    conferir_procedencia_da_r2(carimbo)

    print('\n' + '=' * 78)
    if falhas:
        print('REPROVADO NO AR: %d afirmacoes, %d falha(s).' % (feitos, falhas))
        return 1
    print('APROVADO NO AR: %d afirmacoes, 0 falha(s).' % feitos)
    return 0


if __name__ == '__main__':
    sys.exit(main())
