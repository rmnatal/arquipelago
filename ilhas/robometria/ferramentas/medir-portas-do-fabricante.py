#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MEDIR AS PORTAS DO FABRICANTE — a regua do despacho do Raphael de 19/09/2026.

O despacho manda preencher a foto dos 66 publicaveis sem imagem pela SEGUNDA
FONTE da secao 25.3: a pagina do proprio fabricante. Ele nomeia cinco dominios
como "abertos na rede desde 17/09" e manda, antes de declarar bloqueio, conferir
o DNS — porque em 17/09 dois dos cinco enderecos "bloqueados" simplesmente nao
existiam, e host que nao resolve e erro de digitacao, nunca pedido de liberacao.

Esta ferramenta mede as DUAS coisas que decidem se o despacho pode andar, e nao
digita nenhuma delas:

  1. QUAL PORTA cada um dos 66 registros tem. A porta nao se inventa por busca:
     ela ja esta no banco, em `fontes{}.url` e em `canal_brasileiro.valor` — sao
     as paginas de onde o dado daquele registro foi lido. Foto de peca exata se
     colhe da pagina que nomeia aquela peca, e essa pagina ja foi aberta uma vez.
  2. SE A PORTA ABRE daqui, host a host, com DNS e HTTP separados, porque os dois
     sintomas sao iguais no `curl` e opostos no conserto (licao de 17/09/2026,
     hoje na secao 20.2 do ARQUIPELAGO.md).

E classifica cada porta contra `dados/marcas.json`, que e onde esta ilha declara
quais hosts sao de cada fabricante. Host de marca nao declarado ali NAO e
aprovado por parecer: sai como `nao_declarado`, para alguem decidir. A 25.3 diz
"so a foto do FABRICANTE, da PECA EXATA" — entao quem decide o que e fabricante
e o banco de marcas, nao o formato do endereco.

  python3 ferramentas/medir-portas-do-fabricante.py              # mede, imprime
  python3 ferramentas/medir-portas-do-fabricante.py --sem-rede   # so a porta
  python3 ferramentas/medir-portas-do-fabricante.py --relatorio dados/x.md
  python3 ferramentas/medir-portas-do-fabricante.py --gravar     # escreve o motivo

NAO grava foto nenhuma, e isso e de proposito. A 25.3 manda abrir cada imagem
com os olhos antes de gravar, e olho nao se automatiza: o que esta ferramenta
entrega e a LISTA DE PORTAS, para a execucao que tiver a rede aberta ir direto
a pagina certa em vez de recomecar pela busca.

Prefixo `medir-` = ferramenta de producao, fora da bancada (ver bancada.py).
"""

import json
import os
import re
import socket
import subprocess
import sys
from urllib.parse import urlparse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANCOS = ['dados/pecas.json', 'dados/modelos-robo.json']
MARCAS = 'dados/marcas.json'
HOJE = '2026-09-20'

# A linha que esta ferramenta acrescenta ao motivo_do_null. O marcador existe
# para a segunda passada SUBSTITUIR a primeira em vez de empilhar: motivo que
# cresce a cada execucao vira parede de texto e para de ser lido.
MARCADOR = ' || Segunda fonte (25.3), '

# Os cinco hosts que o despacho do Raphael de 17/09/2026 registra como abertos
# na lista de dominios permitidos do ambiente. Estao aqui CITADOS, com a fonte
# ao lado, e nao digitados como verdade: servem para a medicao poder dizer se a
# lista que existe cobre as portas que o banco realmente usa. Se a lista mudar,
# muda aqui, e a diferenca volta a aparecer no relatorio em vez de sumir.
ABERTOS_EM_17_09 = (
    'www.electrolux.com.br',
    'www.multilaser.com.br',
    'mais.conteudo.wap.ind.br',
    'www.mi.com',
    'www.positivotecnologia.com.br',
)


def caminho(rel):
    return os.path.join(RAIZ, rel)


def carregar(rel):
    with open(caminho(rel), encoding='utf-8') as fp:
        return json.load(fp)


def dominio_registravel(host):
    """`lamina.multilaser.com.br` -> `multilaser.com.br`. Trata os .com.br."""
    partes = host.lower().split('.')
    if len(partes) >= 3 and partes[-2] in ('com', 'net', 'org', 'ind', 'gov'):
        return '.'.join(partes[-3:])
    return '.'.join(partes[-2:])


def hosts_por_marca():
    """O que cada marca DECLARA como endereco seu, lido de marcas.json."""
    mapa = {}
    for reg in carregar(MARCAS)['registros']:
        hs = set()
        for chave in ('site_oficial', 'canal_de_pecas'):
            if reg.get(chave):
                hs.add(urlparse(reg[chave]).netloc.lower())
        for url in (reg.get('sameAs') or []):
            hs.add(urlparse(url).netloc.lower())
        mapa[reg['id']] = {h for h in hs if h}
    return mapa


def portas_do_registro(reg):
    """As paginas de onde o dado deste registro ja foi lido, sem repetir."""
    portas, vistas = [], set()
    for fid, fonte in (reg.get('fontes') or {}).items():
        url = (fonte or {}).get('url')
        if not url or url in vistas:
            continue
        vistas.add(url)
        portas.append({
            'url': url,
            'de': fid,
            'nivel': fonte.get('nivel'),
            'origem': fonte.get('origem'),
            'publicador': fonte.get('publicador'),
        })
    canal = reg.get('canal_brasileiro')
    if isinstance(canal, dict) and canal.get('valor') and canal['valor'] not in vistas:
        portas.append({
            'url': canal['valor'],
            'de': 'canal_brasileiro',
            'nivel': None,
            'origem': 'canal-brasileiro-do-fabricante',
            'publicador': canal.get('fonte'),
        })
    return portas


def classificar(porta, marca, declarados):
    """fabricante | nao_declarado | terceiro — e o terceiro nunca vira foto."""
    host = urlparse(porta['url']).netloc.lower()
    pub = (porta.get('publicador') or '').lower()
    if 'terceiro' in pub or 'hospedado por' in pub:
        return 'terceiro', host
    meus = declarados.get(marca, set())
    if host in meus:
        return 'fabricante', host
    if dominio_registravel(host) in {dominio_registravel(h) for h in meus}:
        return 'fabricante', host
    return 'nao_declarado', host


def medir_host(host):
    """DNS e HTTP separados, porque 'nao existe' e 'nao me deixam' sao opostos."""
    try:
        socket.getaddrinfo(host, 443)
        dns = 'resolve'
    except socket.gaierror:
        return {'host': host, 'dns': 'NAO_RESOLVE', 'http': None, 'veredito': 'endereco errado'}
    try:
        saida = subprocess.run(
            ['curl', '-s', '-o', os.devnull, '-w', '%{http_code}',
             '--max-time', '20', 'https://%s/' % host],
            capture_output=True, text=True, timeout=40)
        codigo = (saida.stdout or '').strip()
    except (subprocess.SubprocessError, OSError) as erro:
        codigo = 'erro: %s' % erro
    if codigo in ('000', ''):
        veredito = 'bloqueado por rede'
    elif codigo.startswith(('2', '3')):
        veredito = 'aberto'
    else:
        veredito = 'responde %s' % codigo
    return {'host': host, 'dns': dns, 'http': codigo, 'veredito': veredito}


def medir(com_rede=True):
    declarados = hosts_por_marca()
    registros, hosts = [], {}
    for rel in BANCOS:
        banco = carregar(rel)
        for reg in banco['registros']:
            if reg.get('status') != 'publicavel':
                continue
            if ((reg.get('imagem') or {}).get('url')):
                continue          # a preferencia nunca inverte (25.3)
            portas = []
            for porta in portas_do_registro(reg):
                especie, host = classificar(porta, reg['marca'], declarados)
                porta = dict(porta, especie=especie, host=host)
                portas.append(porta)
                hosts.setdefault(host, None)
            registros.append({
                'id': reg['id'],
                'marca': reg['marca'],
                'arquivo': rel,
                'entidade': banco['entidade'],
                'codigo': reg.get('codigo_fabricante'),
                'tipo': reg.get('tipo') or reg.get('categoria'),
                'portas': portas,
            })
    if com_rede:
        for host in sorted(hosts):
            hosts[host] = medir_host(host)
    return registros, hosts


def veredito_do_registro(reg, hosts):
    """O registro anda se tiver UMA porta de fabricante com host aberto."""
    doFab = [p for p in reg['portas'] if p['especie'] == 'fabricante']
    if not doFab:
        naodecl = [p for p in reg['portas'] if p['especie'] == 'nao_declarado']
        if naodecl:
            return 'porta nao declarada em marcas.json', naodecl
        return 'so porta de terceiro — 25.3 proibe', reg['portas']
    abertas = [p for p in doFab if (hosts.get(p['host']) or {}).get('veredito') == 'aberto']
    if abertas:
        return 'PODE ANDAR', abertas
    # Host que ninguem mediu nao vira veredito: --sem-rede mede a PORTA, nunca o
    # estado dela, e chamar isso de bloqueio seria inventar uma medicao.
    if any(hosts.get(p['host']) is None for p in doFab):
        return 'porta mapeada, estado nao medido', doFab
    sem_dns = [p for p in doFab if (hosts.get(p['host']) or {}).get('dns') == 'NAO_RESOLVE']
    if sem_dns and len(sem_dns) == len(doFab):
        return 'endereco errado no banco', doFab
    return 'bloqueado por rede', doFab


def relatorio(registros, hosts):
    linhas = []
    w = linhas.append
    w('# AS PORTAS DO FABRICANTE — medicao de %s' % HOJE)
    w('')
    w('Gerada por `ferramentas/medir-portas-do-fabricante.py`, para o **despacho do')
    w('Raphael de 19/09/2026** (foto do fabricante para os publicaveis sem imagem).')
    w('**Nenhum numero desta pagina foi digitado:** os registros saem dos dois arquivos')
    w('de banco, as portas saem de `fontes{}.url` e `canal_brasileiro.valor` de cada')
    w('registro, a especie de cada porta sai de `dados/marcas.json`, e o estado de cada')
    w('host sai de uma consulta de DNS mais um `curl`, host a host.')
    w('')
    w('## O placar')
    w('')
    contagem = {}
    for reg in registros:
        v, _ = veredito_do_registro(reg, hosts)
        contagem[v] = contagem.get(v, 0) + 1
    w('| | |')
    w('|---|---|')
    w('| publicaveis sem foto (o alvo do despacho) | **%d** |' % len(registros))
    w('| registros com ao menos uma porta gravada no banco | %d |'
      % sum(1 for r in registros if r['portas']))
    w('| hosts distintos que essas portas usam | %d |' % len(hosts))
    for chave in sorted(contagem):
        w('| registros em "%s" | **%d** |' % (chave, contagem[chave]))
    w('')
    w('## Os hosts, um a um')
    w('')
    w('| host | DNS | HTTP | veredito | registros que dependem dele |')
    w('|---|---|---|---|---|')
    dependem = {}
    for reg in registros:
        for porta in reg['portas']:
            dependem.setdefault(porta['host'], set()).add(reg['id'])
    for host in sorted(hosts, key=lambda h: (-len(dependem.get(h, ())), h)):
        est = hosts[host] or {'dns': 'nao medido', 'http': '-', 'veredito': 'nao medido'}
        w('| `%s` | %s | %s | %s | %d |' % (
            host, est['dns'], est['http'] if est['http'] is not None else '-',
            est['veredito'], len(dependem.get(host, ()))))
    w('')
    w('## A lista de 17/09 contra as portas que o banco usa')
    w('')
    w('O despacho de 17/09/2026 registra cinco hosts abertos na lista de dominios')
    w('permitidos do ambiente. Esta secao compara aquela lista com os hosts que as')
    w('paginas dos 66 registros realmente usam — e a diferenca nao e detalhe:')
    w('pagina de produto raramente mora no `www` institucional da marca.')
    w('')
    # Host de terceiro fica FORA da lista de abrir: abrir manuals.plus nao ajuda
    # o despacho, porque a 25.3 ja proibe a foto que viria de la. Pedir liberacao
    # de um endereco que a regra nao deixa usar e gastar a atencao do Raphael no
    # lugar errado.
    de_terceiro = {p['host'] for reg in registros for p in reg['portas']
                   if p['especie'] == 'terceiro'}
    faltam = sorted(h for h in hosts
                    if h not in ABERTOS_EM_17_09 and h not in de_terceiro)
    sobram = sorted(h for h in ABERTOS_EM_17_09 if h not in hosts)
    w('| | |')
    w('|---|---|')
    w('| hosts da lista de 17/09 | %d |' % len(ABERTOS_EM_17_09))
    w('| desses, usados por alguma porta dos 66 | %d |'
      % (len(ABERTOS_EM_17_09) - len(sobram)))
    w('| hosts usados pelas portas que NUNCA estiveram na lista | **%d** |' % len(faltam))
    w('')
    so_fora = 0
    for reg in registros:
        doFab = [p for p in reg['portas'] if p['especie'] == 'fabricante']
        if doFab and all(p['host'] not in ABERTOS_EM_17_09 for p in doFab):
            so_fora += 1
    w('**%d dos %d registros nao tem NENHUMA porta na lista de 17/09** — para eles,'
      % (so_fora, len(registros)))
    w('a lista daquele dia, mesmo intacta, nunca teria bastado.')
    w('')
    w('| host que falta abrir | registros que dependem dele |')
    w('|---|---|')
    for host in sorted(faltam, key=lambda h: (-len(dependem.get(h, ())), h)):
        w('| `%s` | %d |' % (host, len(dependem.get(host, ()))))
    w('')
    if sobram:
        w('Na lista de 17/09 e sem uso por porta nenhuma dos 66: %s.'
          % ', '.join('`%s`' % h for h in sobram))
        w('')
    if de_terceiro:
        w('**Fora da lista de abrir, de proposito:** %s. Sao paginas de TERCEIRO'
          % ', '.join('`%s`' % h for h in sorted(de_terceiro)))
        w('(manual hospedado por agregador), e a 25.3 proibe a foto que viria de la.')
        w('Abrir esses hosts nao move o despacho um registro.')
        w('')
    w('## O residuo, registro a registro')
    w('')
    w('| registro | marca | tipo | veredito | porta |')
    w('|---|---|---|---|---|')
    for reg in sorted(registros, key=lambda r: (r['marca'], r['id'])):
        v, portas = veredito_do_registro(reg, hosts)
        url = portas[0]['url'] if portas else '(nenhuma)'
        w('| `%s` | %s | %s | %s | %s |' % (
            reg['id'], reg['marca'], reg['tipo'] or '-', v, url))
    w('')
    return '\n'.join(linhas) + '\n'


def gravar_motivos(registros, hosts):
    """Escreve no banco a tentativa de hoje, sem apagar a causa de 18/09."""
    por_id = {r['id']: r for r in registros}
    tocados = 0
    for rel in BANCOS:
        banco = carregar(rel)
        mudou = False
        for reg in banco['registros']:
            alvo = por_id.get(reg['id'])
            if not alvo:
                continue
            img = reg.get('imagem') or {}
            if img.get('url'):
                continue
            v, portas = veredito_do_registro(alvo, hosts)
            hostlist = ', '.join(sorted({p['host'] for p in portas})) or 'nenhum'
            nova = (MARCADOR + '%s: %s. Host(es) tentado(s): %s. '
                    'DNS resolve em todos; o que barra e a lista de dominios '
                    'permitidos do ambiente, nao o endereco.'
                    % (HOJE, v, hostlist))
            antigo = img.get('motivo_do_null') or ''
            base = antigo.split(MARCADOR)[0].rstrip()
            img['motivo_do_null'] = base + nova
            reg['imagem'] = img
            tocados += 1
            mudou = True
        if mudou:
            with open(caminho(rel), 'w', encoding='utf-8') as fp:
                json.dump(banco, fp, ensure_ascii=False, indent=1)
                fp.write('\n')
    return tocados


def main(argv):
    com_rede = '--sem-rede' not in argv
    registros, hosts = medir(com_rede=com_rede)
    texto = relatorio(registros, hosts)
    if '--relatorio' in argv:
        destino = argv[argv.index('--relatorio') + 1]
        with open(caminho(destino) if not os.path.isabs(destino) else destino,
                  'w', encoding='utf-8') as fp:
            fp.write(texto)
        print('relatorio escrito em %s' % destino)
    else:
        sys.stdout.write(texto)
    if '--gravar' in argv:
        if not com_rede:
            print('RECUSADO: --gravar sem rede escreveria veredito que ninguem mediu.')
            return 1
        n = gravar_motivos(registros, hosts)
        print('motivo_do_null reescrito em %d registro(s).' % n)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
