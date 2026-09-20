#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grava na medicao as palavras-chave que foram medidas NO NAVEGADOR, fora desta nuvem.

    python3 ferramentas/aplicar-chaves-do-navegador.py <arquivo>            # mostra
    python3 ferramentas/aplicar-chaves-do-navegador.py <arquivo> --gravar   # grava
    python3 ferramentas/aplicar-chaves-do-navegador.py <arquivo> --gravar --encurtar

POR QUE ELE EXISTE, E POR QUE NAO E O `medir-palavras-chave.py`
----------------------------------------------------------------
As duas reguas desta ilha discordam NO SENTIDO QUE ENGANA, e isso esta medido
desde 18/09/2026: a Open API de Afiliados — a unica que a Fundacao alcanca desta
nuvem — mede o catalogo de OFERTAS que paga comissao e diz que as 25 chaves
Roborock e Xiaomi do banco trazem a marca no topo; a busca do SITE, que e a que o
leitor ve, abria em Xiaomi em 5 das 6 chaves Roborock. Passar estas chaves pelo
`medir-palavras-chave.py` devolveria VERDE sobre um defeito vivo, e o despacho do
Raphael de 20/09/2026 proibe isso com todas as letras: *"NAO remeca as chaves pela
Open API de ofertas para decidir nada — ela e a regua otimista"*.

Entao a medicao entra por aqui: o navegador mede, o despacho escreve a tabela, a
tabela vira ARQUIVO DE DADOS commitado, e esta ferramenta so a transcreve para
dentro de `dados/palavras-chave-medidas.json`, que e o lugar onde o
`gerar-busca-de-produto.py` ja sabe ler. Nenhuma chave e inventada aqui: toda
chave gravada tem de estar escrita no arquivo de entrada, com o primeiro resultado
que foi lido e quantos resultados a busca devolveu.

O QUE ELE NUNCA FAZ
-------------------
Nao chama a busca do site (ela nao responde desta nuvem: HTTP 403,
`error 90309999`, remedido em 18/09/2026). Nao escolhe chave. Nao mexe no banco —
quem grava no banco continua sendo `gerar-busca-de-produto.py`, lendo a medicao.
A separacao e a mesma de sempre: a medicao depende do dia e de quem mediu, a
gravacao tem de ser deterministica e conferivel sem rede.

A MARCA `fixada_no_navegador`, E O QUE ELA PROTEGE
---------------------------------------------------
Toda chave escrita por aqui sai com `fixada_no_navegador: true`. E o
`medir-palavras-chave.py` foi ensinado a NAO sobrescrever essas — senao a proxima
passada da regua otimista desfaria, em silencio, o conserto que o navegador pagou
com captcha. Regra que so vale ate alguem rodar a ferramenta errada nao e regra.

O ENCURTAMENTO
--------------
Com `--encurtar` ele pede o link de afiliado de cada chave NOVA a Open API (25.6),
que e o unico uso dela que o despacho autoriza: encurtar nao decide chave nenhuma.
Sem a credencial no ambiente, a chave nova entra com `url_busca` vazio e com o
motivo escrito — e e assim que o proprio despacho manda fazer, porque a chave (o
que o leitor ve) esta certa e a comissao e divida do elo, nao do leitor.
"""
import argparse
import importlib.util
import json
import os
import sys
import urllib.parse

RAIZ_ILHA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ_REPO = os.path.dirname(os.path.dirname(RAIZ_ILHA))

MEDICAO = 'dados/palavras-chave-medidas.json'
BASE = 'https://shopee.com.br/search?keyword='

# O degrau da escada da Open API que uma chave do navegador ocupa: NENHUM. Ela nao
# desceu aquela escada, entao dizer 1 ou 5 seria procedencia falsa. Zero e o unico
# numero que nao mente, e ele esta declarado na lista `escada` da medicao.
DEGRAU_FORA_DA_ESCADA = 0


def caminho(rel):
    return os.path.join(RAIZ_ILHA, rel)


def carregar(rel):
    with open(caminho(rel), encoding='utf-8') as fh:
        return json.load(fh)


def gravar(rel, dados, indent=1):
    with open(caminho(rel), 'w', encoding='utf-8') as fh:
        json.dump(dados, fh, ensure_ascii=False, indent=indent)
        fh.write('\n')


def _encurtador():
    spec = importlib.util.spec_from_file_location(
        'shopee_api', os.path.join(RAIZ_REPO, 'ferramentas', 'shopee-api.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    p = argparse.ArgumentParser()
    p.add_argument('entrada', help='o arquivo de dados com a tabela medida no navegador')
    p.add_argument('--gravar', action='store_true')
    p.add_argument('--encurtar', action='store_true',
                   help='pede o link de afiliado de cada chave nova (exige credencial)')
    args = p.parse_args()

    entrada = carregar(args.entrada)
    medicao = carregar(MEDICAO)
    por_id = {r['id']: r for r in medicao['registros']}
    # O nome pelo qual a marca e procurada na loja. E com ele que se confere,
    # mecanicamente, que o primeiro resultado medido traz a marca do registro —
    # a regua do item 4 do despacho da Sentinela de 18/09/2026. Ler do banco e
    # nao do arquivo de entrada e de proposito: o arquivo de entrada e quem esta
    # sendo conferido.
    nome_de_busca = {m['id']: (m.get('nome_de_busca') or '')
                     for m in carregar('dados/marcas.json')['registros']}

    api = None
    if args.encurtar:
        if not (os.environ.get('SHOPEE_APP_ID') and os.environ.get('SHOPEE_SECRET')):
            print('SHOPEE_APP_ID/SHOPEE_SECRET ausentes do ambiente: as chaves novas '
                  'entram com url_busca vazio e o motivo escrito (despacho de 20/09).')
            args.encurtar = False
        else:
            api = _encurtador()

    motivo_pendente = ('encurtamento pendente — credencial ausente no ambiente em %s'
                       % entrada['medido_em'])

    trocados = mantidos = ausentes = 0
    for grupo in entrada['grupos']:
        marca = nome_de_busca.get(grupo['marca'], '')
        if not marca:
            raise SystemExit('grupo %r com marca %r que nao esta em marcas.json'
                             % (grupo['chave_nova'], grupo['marca']))
        marca_no_topo = marca.lower() in (grupo['primeiro_resultado'] or '').lower()
        if not marca_no_topo:
            # A ENTRADA NAO E ACREDITADA NO PONTO QUE IMPORTA. O item 4 do despacho
            # da Sentinela fecha quando o primeiro resultado traz a marca; chave
            # nova cujo primeiro resultado NAO traz seria trocar um defeito por
            # outro, com data nova e cara de conferido.
            raise SystemExit(
                'chave %r: o primeiro resultado medido (%r) nao traz a marca %r. '
                'O criterio de pronto do item 4 e esse, e trocar a chave sem ele '
                'e a mesma familia do defeito que se esta consertando'
                % (grupo['chave_nova'], grupo['primeiro_resultado'], marca))
        url = BASE + urllib.parse.quote(grupo['chave_nova'])
        curto = ''
        if args.encurtar:
            curto = api.encurtar(url, 'robometria')
        for ident in grupo['registros']:
            reg = por_id.get(ident)
            if reg is None:
                print('  AUSENTE da medicao: %s' % ident)
                ausentes += 1
                continue
            velha = dict(reg.get('escolhido') or {})
            if velha.get('chave') == grupo['chave_nova']:
                # Chave ja aplicada: nao empurra a mesma reprovacao para o historico
                # duas vezes. Rodar de novo o mesmo arquivo tem de ser inofensivo.
                continue
            velha['veredito'] = grupo['veredito_da_velha']
            velha['regua_do_veredito'] = entrada['regua']
            velha['veredito_em'] = entrada['medido_em']
            velha['primeiro_resultado_no_veredito'] = grupo['primeiro_resultado_da_velha']
            historico = list(reg.get('tentativas') or [])
            historico.append(velha)
            reg['tentativas'] = historico
            reg['escolhido'] = {
                'degrau': DEGRAU_FORA_DA_ESCADA,
                'composicao': 'medida no navegador — %s' % entrada['id'],
                'chave': grupo['chave_nova'],
                'resultados': grupo['resultados'],
                'titulo_do_topo': grupo['primeiro_resultado'],
                # `topo_e_a_peca` FICA NULO DE PROPOSITO, e a tentacao de escrever
                # `true` aqui e o defeito que esta ilha mais paga. Aquele campo e o
                # veredito da regua dura da 25.7 (`casa_peca`), que roda dentro do
                # `medir-palavras-chave.py` sobre o titulo devolvido pela API — e
                # essa regua NAO rodou nesta medicao. O que foi medido no navegador
                # esta no campo ao lado, `marca_no_topo`, que e exatamente o criterio
                # de pronto do item 4 do despacho da Sentinela de 18/09: *"o primeiro
                # resultado da busca contiver a marca do registro"*. Preencher um
                # campo com o veredito de outra regua e como dizer que conferiu.
                'topo_e_a_peca': None,
                'marca_no_topo': marca_no_topo,
                'por_que': grupo['por_que'],
                'criterio_literal_do_despacho': None,
                'url_busca_produto': url,
                'url_busca': curto,
                'fixada_no_navegador': True,
                'regua': entrada['regua'],
                'medido_em': entrada['medido_em'],
                'motivo_sem_url_busca': None if curto else motivo_pendente,
            }
            if grupo.get('nota'):
                reg['escolhido']['nota'] = grupo['nota']
            reg['parou_por'] = ('chave fixada no navegador pelo despacho do Raphael '
                                'de %s; a escada da Open API nao decide esta chave'
                                % entrada['medido_em'])
            trocados += 1
            print('  %-38s %s' % (ident, grupo['chave_nova']))

    # AS APROVADAS TAMBEM SAO FIXADAS, e isso nao e zelo: o despacho manda NAO mexer
    # nelas, e sem a marca a proxima passada da regua otimista pode move-las.
    for grupo in entrada.get('aprovadas_sem_troca', []):
        for ident in grupo['registros']:
            reg = por_id.get(ident)
            if reg is None:
                continue
            e = reg.setdefault('escolhido', {})
            if e.get('chave') != grupo['chave']:
                print('  AVISO: %s tem chave %r e o arquivo aprovou %r — nao fixada'
                      % (ident, e.get('chave'), grupo['chave']))
                continue
            e['fixada_no_navegador'] = True
            e['regua'] = entrada['regua']
            e['medido_em'] = entrada['medido_em']
            e['titulo_do_topo'] = grupo['primeiro_resultado']
            e['resultados'] = grupo['resultados']
            e['por_que'] = grupo['por_que']
            e['marca_no_topo'] = (nome_de_busca.get(grupo['marca'], '').lower()
                                  in (grupo['primeiro_resultado'] or '').lower())
            mantidos += 1

    # AS CONTAGENS SAO RECONTADAS COM A MESMA SEMANTICA DE ANTES — por CHAVE
    # DISTINTA de peca, nunca por registro. Trocar a unidade de contagem sem
    # trocar o nome do campo faria a serie do arquivo saltar sem que nada tivesse
    # acontecido no mundo, que e o defeito que a secao 8 chama de numero de tela
    # digitado com outro nome.
    pecas = [r for r in medicao['registros'] if r.get('tipo')]
    chaves = {}
    for r in pecas:
        e = r.get('escolhido') or {}
        if e.get('chave'):
            chaves.setdefault(e['chave'], e)
    medicao['contagem'] = {
        'palavras_chave_distintas_de_peca': len(chaves),
        'com_resultado': sum(1 for e in chaves.values() if (e.get('resultados') or 0) > 0),
        'com_a_peca_no_topo': sum(1 for e in chaves.values() if e.get('topo_e_a_peca')),
        'com_a_marca_no_topo': sum(1 for e in chaves.values() if e.get('marca_no_topo')),
        'criterio_literal_do_despacho': sum(
            1 for e in chaves.values() if e.get('criterio_literal_do_despacho')),
        'registros_de_peca': len(pecas),
        'registros_medidos': len(medicao['registros']),
        'chaves_fixadas_no_navegador': sum(
            1 for r in medicao['registros']
            if (r.get('escolhido') or {}).get('fixada_no_navegador')),
    }
    medicao.setdefault('escada', []).insert(0, {
        'degrau': DEGRAU_FORA_DA_ESCADA,
        'composicao': 'fora da escada: chave medida na busca do SITE, no navegador'})
    medicao['escada'] = [d for i, d in enumerate(medicao['escada'])
                         if d not in medicao['escada'][:i]]
    medicao['fontes_da_medicao'] = sorted(set(
        (medicao.get('fontes_da_medicao') or []) + [entrada['id']]))
    # `gerado_em` continua sendo o dia da passada da Open API, porque e dela que
    # falam as contagens historicas e a trava da 25.2-b. O dia em que o navegador
    # entrou tem campo proprio: duas medicoes com datas diferentes dentro do mesmo
    # arquivo nao podem dividir um campo so, ou a mais nova apagaria a procedencia
    # da mais velha.
    medicao['atualizado_em'] = entrada['medido_em']

    print('')
    print('chaves trocadas ......... %d registro(s)' % trocados)
    print('chaves mantidas ......... %d registro(s)' % mantidos)
    print('ausentes da medicao ..... %d' % ausentes)
    print('fixadas no navegador .... %d' % medicao['contagem']['chaves_fixadas_no_navegador'])

    if args.gravar:
        gravar(MEDICAO, medicao)
        print('gravado em %s' % MEDICAO)
    else:
        print('(passada seca — use --gravar)')
    return 1 if ausentes else 0


if __name__ == '__main__':
    sys.exit(main())
