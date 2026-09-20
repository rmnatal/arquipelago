#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
O CANAL BRASILEIRO APODRECE, E ATE HOJE NADA MEDIA ISSO (20/09/2026).

`canal_brasileiro` e o PORTAO DA RECOMENDACAO desta ilha: preenchido, a R2 pode
recomendar o modelo; `null` com motivo, a R2 nao recomenda e diz na tela quantos
ficaram de fora e por que. O campo guarda a URL da pagina do proprio fabricante
que publica aquele codigo — e uma URL e uma afirmacao sobre o mundo de fora, que
o mundo de fora pode desmentir a qualquer momento sem avisar ninguem.

Foi o que aconteceu. Em 20/09/2026, tentando colher a foto do fabricante, cinco
das seis paginas da Roborock Brasil gravadas no banco devolveram **404** — e as
cinco estavam **servidas no ar**, dentro da R2, como prova de canal brasileiro.
O leitor clicava numa prova que nao existia mais. A prova tinha data de quando
foi colhida e nenhuma de quando foi reconferida, e por isso envelheceu em
silencio: e a mesma familia do "o site fica para tras em silencio" da secao 4 do
ARQUIPELAGO.md, um andar acima — aqui o que envelhece nao e o resumo do estado,
e a evidencia que um portao usa para decidir.

    python3 ferramentas/medir-canal-brasileiro-no-ar.py            # mede, imprime
    python3 ferramentas/medir-canal-brasileiro-no-ar.py --gravar   # anula as mortas

O VEREDITO EXIGE DUAS PROVAS QUE DISCORDAM POR MOTIVOS DIFERENTES, e isto nao e
zelo: mudanca de endereco e fim de linha do produto parecem iguais no `curl`, e
so uma das duas justifica tirar o modelo da recomendacao.

  1. A URL gravada responde, em DUAS tentativas separadas. Uma falha isolada e o
     tunel, nunca veredito (secao 20.2). Bloqueio de rede (`000`) sai como
     `incerta` e NUNCA anula nada: nao saber e diferente de saber que morreu.
  2. O CODIGO do modelo aparece em algum endereco do sitemap do proprio host
     brasileiro. E a pergunta que separa as duas causas: pagina que mudou de
     lugar continua no sitemap com outro caminho; produto que saiu da linha
     some do sitemap inteiro. So `morta` — 4xx nas duas tentativas E ausente do
     sitemap — vira `null`, e o motivo gravado diz as duas coisas.

NENHUM NUMERO DESTE ARQUIVO E DIGITADO: os codigos saem do banco, as URLs saem
de `canal_brasileiro.valor`, e os estados saem de `curl`.

Prefixo `medir-` = ferramenta de producao, fora da bancada (ver bancada.py).
"""

import json
import os
import re
import subprocess
import sys
import time
from urllib.parse import urlparse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANCOS = ('dados/modelos-robo.json', 'dados/pecas.json')
HOJE = '2026-09-20'
UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/124.0 Safari/537.36')


def caminho(rel):
    return os.path.join(RAIZ, rel)


def carregar(rel):
    with open(caminho(rel), encoding='utf-8') as fp:
        return json.load(fp)


def indentacao_do_arquivo(rel):
    with open(caminho(rel), encoding='utf-8') as fp:
        fp.readline()
        segunda = fp.readline()
    return len(segunda) - len(segunda.lstrip(' '))


def bater(url, tempo=25):
    try:
        r = subprocess.run(
            ['curl', '-sLo', os.devnull, '--compressed', '-A', UA,
             '--max-time', str(tempo), '-w', '%{http_code}', url],
            capture_output=True, text=True, timeout=tempo + 15)
        return (r.stdout or '').strip() or '000'
    except (subprocess.SubprocessError, OSError):
        return '000'


def baixar(url, tempo=30):
    try:
        r = subprocess.run(
            ['curl', '-sL', '--compressed', '-A', UA, '--max-time', str(tempo), url],
            capture_output=True, text=True, timeout=tempo + 15)
        return r.stdout or ''
    except (subprocess.SubprocessError, OSError):
        return ''


def enderecos_do_sitemap(host, cache):
    """Todo `<loc>` que o host publica, seguindo um nivel de indice."""
    if host in cache:
        return cache[host]
    vistos = set()
    fila = ['https://%s/sitemap.xml' % host, 'https://%s/sitemap_index.xml' % host]
    for _ in range(2):
        novas = []
        for u in fila:
            corpo = baixar(u)
            locs = re.findall(r'<loc>\s*([^<\s]+)\s*</loc>', corpo)
            for loc in locs:
                if loc.endswith('.xml'):
                    novas.append(loc)
                else:
                    vistos.add(loc)
            m = re.search(r'url=([^"\'>]+)', corpo)
            if m and not locs:
                novas.append(m.group(1) if m.group(1).startswith('http')
                             else 'https://%s%s' % (host, m.group(1)))
        fila = [n for n in novas if n not in fila][:12]
        if not fila:
            break
    cache[host] = vistos
    return vistos


def fatia(texto):
    """`Q8 Max` -> `q8-?max`, para achar o codigo dentro de uma URL."""
    pedacos = [re.escape(p.lower()) for p in re.split(r'[\s/_-]+', texto) if p]
    return re.compile('[-/]?'.join(pedacos)) if pedacos else None


def medir():
    cache, linhas = {}, []
    for rel in BANCOS:
        banco = carregar(rel)
        for reg in banco['registros']:
            canal = reg.get('canal_brasileiro')
            if not isinstance(canal, dict) or not canal.get('valor'):
                continue
            url = canal['valor']
            host = urlparse(url).netloc.lower()
            um = bater(url)
            dois = um
            if not um.startswith('2'):
                time.sleep(3)
                dois = bater(url)
            codigo = (reg.get('codigo_fabricante') or reg['id'].split('-', 1)[-1])
            padrao = fatia(codigo)
            no_sitemap, tamanho = None, None
            if not (um.startswith('2') or dois.startswith('2')):
                enderecos = enderecos_do_sitemap(host, cache)
                tamanho = len(enderecos)
                no_sitemap = bool(padrao and any(padrao.search(e.lower()) for e in enderecos))
            if um.startswith('2') or dois.startswith('2'):
                veredito = 'viva'
            elif um == '000' or dois == '000' or um.startswith('5') or dois.startswith('5'):
                veredito = 'incerta'
            elif no_sitemap:
                veredito = 'mudou de endereco'
            elif not tamanho:
                # SEGUNDA PROVA VAZIA NAO E SEGUNDA PROVA. Host sem sitemap
                # legivel devolve "nao esta no sitemap" para TUDO, inclusive para
                # a pagina que esta la. Anular um portao com isso seria medir a
                # propria ignorancia e chamar de veredito — o defeito que esta
                # ilha mais paga, com outra roupa.
                veredito = 'incerta (sitemap ilegivel)'
            else:
                veredito = 'morta'
            linhas.append({'id': reg['id'], 'arquivo': rel, 'codigo': codigo,
                           'url': url, 'host': host, 'http_1': um, 'http_2': dois,
                           'no_sitemap': no_sitemap, 'enderecos_no_sitemap': tamanho,
                           'veredito': veredito})
    return linhas


def motivo(linha):
    return ('a pagina do fabricante que provava o canal brasileiro deste codigo saiu '
            'do ar. Medido em %s: %s devolveu %s e, numa segunda tentativa, %s; e o '
            'codigo %r nao aparece em nenhum endereco do sitemap de %s. As duas '
            'provas juntas separam mudanca de endereco (que continua no sitemap) de '
            'fim de linha no canal brasileiro (que some dele) — e o sitemap daquele '
            'host publica %d enderecos hoje, entao a ausencia foi medida contra um '
            'sitemap que existe. O registro continua no '
            'banco porque a COMPATIBILIDADE declarada pelo fabricante vale para quem '
            'ja tem o aparelho; a recomendacao de compra da R2 nao o alcanca mais, '
            'porque recomendar o que o fabricante nao publica mais aqui e um beco.'
            % (HOJE, linha['url'], linha['http_1'], linha['http_2'],
               linha['codigo'], linha['host'], linha['enderecos_no_sitemap']))


def main(argv):
    gravar = '--gravar' in argv
    linhas = medir()
    largura = max(len(l['id']) for l in linhas) if linhas else 10
    for l in sorted(linhas, key=lambda x: (x['veredito'], x['id'])):
        print('%-*s %-6s %-6s sitemap=%-5s locs=%-5s %s'
              % (largura, l['id'], l['http_1'], l['http_2'],
                 '-' if l['no_sitemap'] is None else ('sim' if l['no_sitemap'] else 'nao'),
                 '-' if l.get('enderecos_no_sitemap') is None else l['enderecos_no_sitemap'],
                 l['veredito']))
    conta = {}
    for l in linhas:
        conta[l['veredito']] = conta.get(l['veredito'], 0) + 1
    print('\n%d canal(is) medido(s): %s' % (
        len(linhas), ', '.join('%d %s' % (v, k) for k, v in sorted(conta.items()))))

    mortas = [l for l in linhas if l['veredito'] == 'morta']
    if not mortas:
        print('nada a anular.')
        return 0
    if not gravar:
        print('%d a anular (rode com --gravar).' % len(mortas))
        return 0
    por_arquivo = {}
    for l in mortas:
        por_arquivo.setdefault(l['arquivo'], []).append(l)
    for rel, grupo in por_arquivo.items():
        banco = carregar(rel)
        alvo = {l['id']: l for l in grupo}
        for reg in banco['registros']:
            if reg['id'] not in alvo:
                continue
            l = alvo[reg['id']]
            antigo = reg['canal_brasileiro']
            reg['canal_brasileiro'] = {
                'valor': None,
                'unidade': None,
                # A URL morta NAO e apagada: ela vira historico, porque quem for
                # reabrir esta decisao precisa saber qual pagina existia e o que
                # ela declarava. Apagar a evidencia e como nunca te-la colhido.
                'motivo_do_null': motivo(l),
                'valor_anterior': antigo.get('valor'),
                'declarado_como_anterior': antigo.get('declarado_como'),
                'fonte_anterior': antigo.get('fonte'),
                'aferido_em': HOJE,
            }
            print('  anulado: %s' % reg['id'])
        # AS TRES CONTAGENS DO PORTAO SAO RECONTADAS AQUI, e nao e opcional:
        # `validar-banco.py` compara cada uma com o arquivo e REPROVA quando
        # divergem — de proposito, porque contagem que nao bate com o arquivo e
        # pior que contagem nenhuma. Anular um canal sem recontar deixaria o
        # banco reprovando na propria bancada, com o numero velho dizendo que a
        # R2 recomenda modelos que ela nao recomenda mais.
        pub = [r for r in banco['registros'] if r.get('status') == 'publicavel']
        com = [r for r in pub if (r.get('canal_brasileiro') or {}).get('valor') is not None]
        if 'com_canal_brasileiro' in (banco.get('contagem') or {}):
            banco['contagem']['com_canal_brasileiro'] = len(com)
            banco['contagem']['sem_canal_brasileiro'] = len(pub) - len(com)
            banco['contagem']['recomendaveis_pela_r2'] = sum(
                1 for r in com if (r.get('pa_declarado') or {}).get('valor') is not None)
            print('  contagem: %d com canal, %d sem, %d recomendaveis pela R2'
                  % (banco['contagem']['com_canal_brasileiro'],
                     banco['contagem']['sem_canal_brasileiro'],
                     banco['contagem']['recomendaveis_pela_r2']))
        # A INDENTACAO SE MEDE DO ARQUIVO, nunca se adivinha. Os dois bancos
        # desta ilha nao concordam, e regravar com a errada reescreve o arquivo
        # inteiro num diff de milhares de linhas, escondendo as poucas que a
        # execucao de fato mudou. A licao ja estava escrita em
        # `gerar-busca-de-produto.py`; aqui ela foi reaprendida em 20/09/2026,
        # com um diff de 11 mil linhas para sete campos anulados.
        indent = indentacao_do_arquivo(rel)
        with open(caminho(rel), 'w', encoding='utf-8') as fp:
            json.dump(banco, fp, ensure_ascii=False, indent=indent)
            fp.write('\n')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
