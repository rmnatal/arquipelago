#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GRAVAR A FOTO DO FABRICANTE — a outra metade de `coletar-foto-do-fabricante.py`,
prometida no docstring dele desde 20/09/2026 e escrita em 21/09/2026, no dia em
que os hosts de IMAGEM abriram e houve o que gravar.

O coletor nao grava de proposito: a secao 25.3 manda abrir cada imagem COM OS
OLHOS antes de gravar, e olho nao se automatiza. Esta ferramenta e o que
acontece DEPOIS do olho — e ela existe para que o olho deixe rastro em vez de
virar um commit sem procedencia.

O ARQUIVO DO OLHO, e por que ele e a entrada e nao um argumento de linha:

    dados/olho-nas-fotos-<data>.json
    {
     "olhado_em": "2026-09-21",
     "fonte_dos_candidatos": "dados/candidatos-de-foto-2026-09-21.json",
     "vereditos": [
       {"id": "multi-pr10124",
        "url": "https://.../10858_00.jpg?v=...",
        "veredito": "APROVA",
        "o_que_o_olho_viu": "peca sobre fundo branco, ..."},
       ...
     ]
    }

**A URL MORA NOS DOIS LADOS DE PROPOSITO, e essa duplicacao e o portao.** O
olho olhou UM arquivo; o banco tem de receber EXATAMENTE aquele arquivo. Se o
coletor rodar de novo e a loja tiver trocado a foto, a URL do candidato muda e
esta ferramenta PARA com erro em vez de gravar um arquivo que ninguem viu. Sem
essa amarra, "aprovado pelo olho" viraria um carimbo no id do registro, e id
nao e imagem — foi assim que `positivo-11206519` quase entrou errado em 18/09.

**E ELA PEGOU ALGO NO PRIMEIRO DIA EM QUE EXISTIU, 21/09/2026, e nao foi a loja
trocando a foto.** Duas colheitas rodaram ao mesmo tempo por descuido da execucao
e escreveram no MESMO `dados/candidatos-de-foto-<data>.json`, que nao tem trava.
O olho abriu as imagens de uma passada; o arquivo que ficou em disco era da
outra. Quatro registros divergiram — dois com a foto em outro host (`us.roborock`
contra `cdn.shopify`) e dois que numa passada tinham candidato e na outra sairam
com `veredito_nome: NAO`. Sem esta amarra, dois teriam entrado no banco com uma
URL que ninguem abriu e dois com procedencia que a colheita valida nao afirmava.
A licao nao e sobre concorrencia: e que a prova do olho tem de viajar junto com
a URL, porque o arquivo do meio pode mudar debaixo dela por mais de um motivo.

OS TRES PORTOES DA 25.3, cobrados aqui um a um e nenhum afrouxado:

  1. PROCEDENCIA. So grava registro cujo candidato tem `veredito_nome` diferente
     de 'NAO' — isto e, cuja pagina do fabricante nomeia o codigo ou o modelo,
     com a prova escrita ao lado. E so grava o que o olho aprovou.
  2. `imagem.fonte` recebe a URL da PAGINA de origem (`colheita.porta`), nunca a
     do arquivo, para que qualquer foto possa ser removida em um comando se um
     fabricante pedir. (A foto da Open API grava 'shopee-api' pelo mesmo motivo,
     um andar acima: la a origem e a API, aqui e a pagina.)
  3. A PREFERENCIA NUNCA INVERTE. Registro que ja tem `imagem.url` nao e tocado,
     e a ferramenta diz quantos pulou. Foto da Shopee vem com o link de compra
     do lado; foto do fabricante so preenche vazio.

E O QUARTO, que nao e da 25.3 e sim da secao 6: `largura` e `altura` sao LIDAS
do arquivo, com o mesmo leitor de cabecalho que a coleta da Shopee usa
(`coletar-shopee.dimensao_da_imagem`), nunca digitadas. Arquivo que nao entrega
dimensao nao e gravado: sem os dois numeros a pagina pula quando a foto carrega,
e a regra do banco reprovaria no portao seguinte de qualquer jeito.

  python3 ferramentas/aplicar-fotos-do-fabricante.py            # ensaio, nao grava
  python3 ferramentas/aplicar-fotos-do-fabricante.py --gravar
  python3 ferramentas/aplicar-fotos-do-fabricante.py --olho dados/olho-nas-fotos-2026-09-21.json

Prefixo `aplicar-` = ferramenta de producao, fora da bancada (ver bancada.py).
"""

import argparse
import datetime
import importlib.util
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOJE = datetime.date.today().isoformat()

BANCOS = ('dados/pecas.json', 'dados/modelos-robo.json')


def _coletor_shopee():
    """O leitor de cabecalho de imagem mora la. Nome com hifen, sem import direto."""
    caminho = os.path.join(RAIZ, 'ferramentas', 'coletar-shopee.py')
    spec = importlib.util.spec_from_file_location('coletar_shopee', caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def normalizar(url):
    """`//host/caminho` vira `https://host/caminho`, e isso e portao, nao higiene.

    A Xiaomi serve a foto em URL RELATIVA AO PROTOCOLO (`//i02.appmifile.com/...`).
    Gravada assim no banco ela funciona no navegador e quebra em tudo que nao e
    navegador: `curl` le a string como CAMINHO e devolve 000, e `urllib` — que e
    quem mede largura e altura aqui — levanta erro. Medido em 21/09/2026, quando
    13 dos 36 candidatos "nao baixaram" e a causa nao era rede nenhuma: os tres
    hosts `appmifile` respondiam 200 para a mesma foto com `https:` na frente.
    A URL que entra no banco e sempre absoluta.
    """
    return 'https:' + url if url.startswith('//') else url


def texto_alt(reg):
    """A descricao de acessibilidade, MONTADA dos campos do proprio registro.

    A secao 6 pede "descricao de verdade, nao o nome do produto repetido", e
    `validar-banco.py` reprova o alt que e o codigo sozinho. O titulo da loja
    tambem nao serve aqui: pagina de fabricante titula com nome de campanha
    ("LANCAMENTO", "novo"), que a ilha nao escreveu e nao pode datar. Entao o
    alt sai do que a ilha JA SABE e ja validou sobre o registro.
    """
    marca = (reg.get('marca') or '').strip()
    tipo = (reg.get('tipo') or '').strip()
    codigo = (reg.get('codigo') or '').strip()
    if reg.get('entidade') == 'modelo':
        base = 'Robo aspirador %s %s' % (marca.capitalize(), codigo or tipo)
        return base.strip() + ', foto do fabricante'
    pedaco = '%s %s' % (tipo, marca.capitalize()) if tipo else marca.capitalize()
    if codigo:
        pedaco += ' (codigo %s)' % codigo
    return 'Foto do fabricante: %s' % pedaco.strip()


def carregar_olho(caminho):
    with open(os.path.join(RAIZ, caminho), encoding='utf-8') as fp:
        doc = json.load(fp)
    for campo in ('olhado_em', 'fonte_dos_candidatos', 'vereditos'):
        if campo not in doc:
            raise SystemExit('ERRO: o arquivo do olho nao tem `%s`. '
                             'Veredito sem data e sem fonte nao e rastro.' % campo)
    return doc


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument('--olho', default='dados/olho-nas-fotos-%s.json' % HOJE)
    ap.add_argument('--gravar', action='store_true',
                    help='sem isto a ferramenta so imprime o que faria')
    args = ap.parse_args(argv)

    olho = carregar_olho(args.olho)
    candidatos_caminho = olho['fonte_dos_candidatos']
    with open(os.path.join(RAIZ, candidatos_caminho), encoding='utf-8') as fp:
        candidatos = {r['id']: r for r in json.load(fp)['registros']}

    aprovados = [v for v in olho['vereditos'] if v.get('veredito') == 'APROVA']
    reprovados = [v for v in olho['vereditos'] if v.get('veredito') != 'APROVA']

    shopee = _coletor_shopee()
    dim_de = shopee.dimensao_da_imagem

    bancos = {c: json.load(open(os.path.join(RAIZ, c), encoding='utf-8')) for c in BANCOS}
    indice = {}
    for caminho, doc in bancos.items():
        for r in doc['registros']:
            indice[r['id']] = (caminho, r)

    gravados, pulados, recusados = [], [], []

    for v in aprovados:
        rid = v['id']
        if rid not in indice:
            recusados.append((rid, 'nao existe no banco'))
            continue
        if rid not in candidatos:
            recusados.append((rid, 'nao esta na colheita de %s' % candidatos_caminho))
            continue
        cand = candidatos[rid]
        colheita = cand.get('colheita') or {}
        if colheita.get('veredito_nome') in (None, 'NAO'):
            recusados.append((rid, 'a pagina nao nomeia este registro — portao 1 da 25.3'))
            continue
        urls = [normalizar(f['url']) for f in colheita.get('fotos') or []]
        if normalizar(v.get('url') or '') not in urls:
            recusados.append((rid, 'a URL que o olho viu nao esta mais entre os '
                                   'candidatos desta colheita: a loja trocou a foto'))
            continue

        _caminho, reg = indice[rid]
        atual = reg.get('imagem') or {}
        if atual.get('url'):
            pulados.append(rid)
            continue

        url = normalizar(v['url'])
        dim = dim_de(url)
        if not dim:
            recusados.append((rid, 'o arquivo nao entregou largura e altura'))
            continue

        reg['imagem'] = {
            'url': url,
            'largura': int(dim[0]),
            'altura': int(dim[1]),
            'fonte': colheita.get('porta'),
            'coletado_em': olho['olhado_em'],
            'alt': texto_alt(cand),
            'motivo_do_null': None,
        }
        gravados.append((rid, dim, colheita.get('prova_nome')))

    for rid, dim, prova in gravados:
        print('GRAVA   %-34s %dx%d   prova: %s' % (rid, dim[0], dim[1], prova))
    for rid, porque in recusados:
        print('RECUSA  %-34s %s' % (rid, porque))
    for rid in pulados:
        print('pula    %-34s ja tem foto — a preferencia nunca inverte (25.3)' % rid)

    if args.gravar and gravados:
        # A CONTAGEM DO CABECALHO E RECONTADA PELA ESCRITA, NAO DEPOIS DELA.
        # `contagem.itens_com_foto` e numero derivado, e a regra desta ilha e que
        # numero de cabecalho de banco seja contado e nunca digitado. A primeira
        # versao desta ferramenta gravou 30 fotos sem mexer nele, e o
        # `validar-banco.py` REPROVOU na passada seguinte, com as duas contagens
        # paradas em 15 e 14. Reusar o `recontar` do coletor da Shopee e de
        # proposito: a definicao do que conta mora num lugar so, e o validador
        # continua conferindo por fora — duas contas que se conferem sao trava,
        # uma conta que confia em si mesma e um numero digitado com mais passos.
        for doc in bancos.values():
            shopee.recontar(doc)
        for caminho, doc in bancos.items():
            with open(os.path.join(RAIZ, caminho), 'w', encoding='utf-8') as fp:
                json.dump(doc, fp, ensure_ascii=False, indent=1)
                fp.write('\n')

    com_foto = sum(1 for _c, r in indice.values() if (r.get('imagem') or {}).get('url'))
    print('\n%d gravado(s), %d recusado(s), %d pulado(s), %d reprovado(s) pelo olho. '
          'Banco: %d de %d com foto.%s'
          % (len(gravados), len(recusados), len(pulados), len(reprovados),
             com_foto, len(indice), '' if args.gravar else '  (ENSAIO — nada foi escrito)'))
    return 1 if recusados else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
