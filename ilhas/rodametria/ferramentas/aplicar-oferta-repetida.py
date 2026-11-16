#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
APLICA A PASSADA DA OFERTA REPETIDA PELA PROPRIA LOJA SOBRE O BANCO JA COLHIDO.

    python3 ferramentas/aplicar-oferta-repetida.py --conferir
    python3 ferramentas/aplicar-oferta-repetida.py            # o laudo, sem gravar
    python3 ferramentas/aplicar-oferta-repetida.py --gravar

O DEFEITO QUE ELA FECHA, MEDIDO NO AR EM `/veiculos/moto-eletrica/` ÀS 19h2xZ DE
16/11/2026 — a pagina que nasceu na manha do mesmo dia:

    cartao 1   "11.11 Moto Eletrica Adulto Panda A4 ... 150kg"    R$ 1.096,38
    cartao 2   "Moto Eletrica Adulto Panda A4 ... 150kg"          R$ 1.522,76

os dois da loja `francyellenoliveira` (shop_id 277054573), itens 58273014613 e
58273026115: o MESMO veiculo nos dois cartoes mais caros da tela. Quem clicasse
no segundo pagaria R$ 426,38 MAIS (38,9%) pelo mesmo produto da mesma loja; a
mediana publicada era R$ 5.011,38 e sobre as 3 ofertas distintas e R$ 8.500,00;
e toda frase "X dos 4" contava o mesmo anuncio duas vezes. A regra mora no
coletor (`marcar_repeticao_da_loja`), que e o dono do arquivo; esta ferramenta e
quem a aplica ao banco sem rede e quem a MEDE.

POR QUE ELA EXISTE SEPARADA DA COLETA. A marca e DERIVADA e se refaz em toda
passada de `recontar_resumo` — mas o banco de hoje foi colhido ANTES de a regra
existir, e colher de novo seria trocar o conjunto de ofertas para consertar uma
conta: a Open API responde desta nuvem com `System Error` intermitente, e a
pergunta que importa nao e "o que a loja tem agora", e "o que a regra de hoje
diz das ofertas que JA estao no banco". E a mesma separacao que
`aplicar-regua-de-relevancia.py` fez em 16/11 pela manha.

O PORTAO (`--conferir`) COBRA A ASSIMETRIA DA 25.9 E AS DUAS METADES DA REGUA:
nenhuma oferta pode ENTRAR na pagina por causa desta passada (so sair), quem
sobrou e sempre o mais barato do grupo, a marca e idempotente, e a regua nao
morde onde nao deve — mundos fabricados com duas LOJAS diferentes de titulo
igual, e com produtos diferentes da mesma loja, tem de passar intactos.
"""

import argparse
import importlib.util
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FERRAMENTAS = os.path.join(RAIZ, 'ferramentas')
BANCO = os.path.join(RAIZ, 'dados', 'anuncios-por-consulta.json')


def _modulo(nome, caminho):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


rel = _modulo('relevancia', os.path.join(FERRAMENTAS, 'teste-relevancia-do-anuncio.py'))
col = _modulo('coletor_por_consulta', os.path.join(FERRAMENTAS, 'coletar-por-consulta.py'))


def carregar():
    with open(BANCO, encoding='utf-8') as f:
        return json.load(f)


def real(v):
    return 'R$ ' + ('%.2f' % v).replace('.', ',')


# ---------------------------------------------------------------------------
# OS MUNDOS FABRICADOS. Tres deles o banco de hoje NAO tem, e sao os que
# sustentam a regua: sem eles o `--conferir` provaria apenas que ela acertou uma
# vez. O quarto e o mundo REAL de 16/11, reproduzido com os numeros medidos.
# ---------------------------------------------------------------------------
def _ad(item_id, shop_id, titulo, preco, loja='loja', serve=True):
    return {'item_id': item_id, 'shop_id': shop_id, 'titulo': titulo,
            'preco': preco, 'loja': loja, 'serve': serve,
            'rotulo_de_potencia': 'watt_sem_rotulo', 'url_afiliado': 'x'}


PANDA = ('Moto Elétrica Adulto Panda A4 Bateria De Lítio 1000W 60V 24ah '
         'Velocidade Max 32km h Capacidade De Carga 150kg')

MUNDOS = (
    ('o mundo real de 16/11/2026: a mesma loja, o mesmo nome, a cabeca de '
     'campanha num deles',
     [_ad(58273014613, 277054573, '11.11 ' + PANDA, 1096.38, 'francyellenoliveira'),
      _ad(58273026115, 277054573, PANDA, 1522.76, 'francyellenoliveira'),
      _ad(58270189618, 1223506816, 'VYRON Moto Elétrica Cross GT600 7500W Pico', 13999.0, 'AUMOX')],
     [58273026115]),
    ('DUAS LOJAS com o titulo identico: NAO se deduplica, e esta e a metade que '
     'a 25.9 protege — titulo parecido entre lojas nao e prova de nada',
     [_ad(1, 111, PANDA, 1096.38, 'loja A'),
      _ad(2, 222, PANDA, 1522.76, 'loja B')],
     []),
    ('a MESMA loja com produtos DIFERENTES: A4 e A5 nao sao a mesma oferta',
     [_ad(1, 111, PANDA, 1096.38),
      _ad(2, 111, PANDA.replace('Panda A4', 'Panda A5'), 1522.76)],
     []),
    ('a mesma loja, o mesmo nome, SEM cabeca de campanha em nenhum dos dois: a '
     'repeticao nua, e ela tambem conta',
     [_ad(1, 111, PANDA, 2000.0),
      _ad(2, 111, PANDA, 1500.0)],
     [1]),
    ('TRES do mesmo nome na mesma loja: fica UM, o mais barato, e nao dois',
     [_ad(1, 111, PANDA, 3000.0),
      _ad(2, 111, '11.11 ' + PANDA, 1000.0),
      _ad(3, 111, PANDA, 2000.0)],
     [1, 3]),
    ('precos IGUAIS: o desempate e o `item_id` menor, nunca a ordem do arquivo',
     [_ad(9, 111, PANDA, 1500.0),
      _ad(4, 111, PANDA, 1500.0)],
     [9]),
    ('o repetido que NAO SERVE nao e julgado duas vezes: ele ja esta fora por '
     'relevancia, e marcar-lo esconderia a causa de verdade',
     [_ad(1, 111, PANDA, 1096.38),
      _ad(2, 111, PANDA, 1522.76, serve=False)],
     []),
    ('anuncio SEM PRECO nao e julgado: sem preco nao existe "mais barato" a '
     'medir, e inventar desempate seria escolher no escuro',
     [_ad(1, 111, PANDA, None),
      _ad(2, 111, PANDA, None)],
     []),
)


def conferir():
    falhas, afirmacoes = [], 0

    # ---- OS MUNDOS FABRICADOS ----
    for nome, anuncios, esperados in MUNDOS:
        bloco = {'anuncios': anuncios}
        marcados = col.marcar_repeticao_da_loja(bloco)
        obtidos = sorted(int(a['item_id']) for a in marcados)
        afirmacoes += 3
        if obtidos != sorted(esperados):
            falhas.append('FALHOU mundo %r: marcou %s, esperava %s'
                          % (nome[:60], obtidos, sorted(esperados)))
        # A MARCA E IDEMPOTENTE: rodar duas vezes nao pode marcar mais nem
        # menos. Marca derivada que acumula e a divida que a 25.11 pagou do
        # outro lado, e ela so aparece na SEGUNDA passada.
        de_novo = sorted(int(a['item_id'])
                         for a in col.marcar_repeticao_da_loja(bloco))
        if de_novo != obtidos:
            falhas.append('FALHOU idempotencia em %r: 1a passada %s, 2a %s'
                          % (nome[:60], obtidos, de_novo))
        # QUEM FICOU E O MAIS BARATO DO GRUPO, sempre. Sem esta afirmacao a
        # regua poderia tirar o certo e deixar o caro, que e o avesso exato do
        # defeito que ela existe para fechar.
        for a in marcados:
            fica = next((x for x in anuncios
                         if x.get('item_id') == a['repetido_por']['mesmo_que']), None)
            if fica is None or fica['preco'] > a['preco']:
                falhas.append('FALHOU mais barato em %r: item %s ficou de fora e '
                              'aponta para %s' % (nome[:60], a['item_id'],
                                                  a['repetido_por'].get('mesmo_que')))

    # ---- O BANCO REAL, E A ASSIMETRIA DA 25.9 ----
    banco = carregar()
    mudaram, total = [], 0
    for bloco in banco['consultas']:
        antes = {int(a.get('item_id') or 0): bool(a.get('serve'))
                 for a in bloco['anuncios']}
        col.marcar_repeticao_da_loja(bloco)
        for a in bloco['anuncios']:
            total += 1
            iid = int(a.get('item_id') or 0)
            afirmacoes += 1
            depois = col.entra_na_pagina(a)
            if depois != antes[iid]:
                mudaram.append((bloco['slug'], iid, antes[iid], depois))
            # A ASSIMETRIA: a passada so pode TIRAR da pagina. `False -> True`
            # seria afrouxamento, e nao ha caminho no codigo que o produza — e
            # por isso mesmo a afirmacao existe, para o dia em que houver.
            if depois and not antes[iid]:
                falhas.append('FALHOU assimetria: %s item %s entrou na pagina por '
                              'causa desta passada' % (bloco['slug'], iid))
            # TODA MARCA TRAZ A FRASE DE COMO FOI MEDIDA, em palavras, no
            # proprio registro — a exigencia que a 25.10 poe no degrau de
            # compra, e ela vale igual aqui.
            marca = a.get('repetido_por')
            if marca:
                afirmacoes += 3
                if marca.get('causa') != col.CAUSA_DA_REPETICAO:
                    falhas.append('FALHOU causa: %s item %s -> %r'
                                  % (bloco['slug'], iid, marca.get('causa')))
                if not (marca.get('como_foi_medido') or '').strip():
                    falhas.append('FALHOU procedencia: %s item %s sem a frase de como '
                                  'foi medido' % (bloco['slug'], iid))
                if not marca.get('mesmo_que'):
                    falhas.append('FALHOU par: %s item %s nao diz de quem e repeticao'
                                  % (bloco['slug'], iid))

        # O `resumo` GRAVADO TEM DE REFAZER. Portao que aplica a regra e nao
        # confere o arquivo deixaria o banco e a tela discordando em silencio.
        gravado = json.loads(json.dumps(bloco['resumo']))
        col.recontar_resumo(bloco)
        afirmacoes += 1
        if gravado != bloco['resumo']:
            diferentes = sorted(k for k in set(gravado) | set(bloco['resumo'])
                                if gravado.get(k) != bloco['resumo'].get(k))
            falhas.append('FALHOU resumo gravado de %s: %s nao refaz'
                          % (bloco['slug'], ', '.join(diferentes)))

    # A PROSA DO NOME NA TELA: nenhum nome publicado pode comecar por marcador
    # de campanha, e o nome tem de ser o FIM do titulo da loja.
    for bloco in banco['consultas']:
        for a in bloco['anuncios']:
            if not col.entra_na_pagina(a):
                continue
            afirmacoes += 2
            nome = rel.nome_do_anuncio(a['titulo'])
            if rel.marcador_de_campanha(nome)[0]:
                falhas.append('FALHOU nome: %s item %s ainda comeca por marcador: %r'
                              % (bloco['slug'], a.get('item_id'), nome[:50]))
            if not (a['titulo'] or '').strip().endswith(nome):
                falhas.append('FALHOU nome: %s item %s -> %r nao e o fim do titulo'
                              % (bloco['slug'], a.get('item_id'), nome[:50]))

    # ---- O TEXTO QUE A VITRINE PUBLICA, E A AFIRMACAO E POSITIVA ----
    # A 20.8 e literal sobre isto: procurar `11.11` seria a leitura pelo avesso,
    # que so pega o marcador que alguem ja imaginou. Aqui se exige que TODO
    # texto publicado passe pela regua — nome e `alt`, nos cartoes e nas linhas.
    # O `alt` entrou porque o conserto do nome foi AO AR sem ele em 16/11/2026
    # (revisao 102): o nome visivel estava limpo e o `alt` da foto do primeiro
    # cartao de `/veiculos/moto-eletrica/` ainda dizia "11.11 Moto Eletrica
    # Adulto Panda A4 ...". Quem o achou foi um `grep` no HTML servido, e nao
    # um portao — e e por isso que esta afirmacao existe.
    vitrine = os.path.join(RAIZ, 'dados', 'vitrine-de-produto.json')
    if os.path.exists(vitrine):
        with open(vitrine, encoding='utf-8') as f:
            v = json.load(f)
        for pagina in v.get('paginas') or []:
            for onde in ('cartoes', 'linhas'):
                for item in pagina.get(onde) or []:
                    nome = item.get('nome') or ''
                    afirmacoes += 1
                    if rel.marcador_de_campanha(nome)[0]:
                        falhas.append('FALHOU nome publicado: %s %s %r comeca por '
                                      'marcador de campanha'
                                      % (pagina['slug'], onde, nome[:50]))
                    imagem = item.get('imagem') or {}
                    alt = imagem.get('alt')
                    if alt is None:
                        continue
                    afirmacoes += 2
                    if rel.marcador_de_campanha(alt)[0]:
                        falhas.append('FALHOU alt publicado: %s %s %r comeca por '
                                      'marcador de campanha'
                                      % (pagina['slug'], onde, alt[:50]))
                    # E O `alt` E O NOME DA TELA, nao outro texto: duas frases
                    # para a mesma coisa comecam iguais e so uma sobe (20.7).
                    if alt != nome[:120]:
                        falhas.append('FALHOU alt publicado: %s %s o alt %r nao e o '
                                      'nome da tela %r'
                                      % (pagina['slug'], onde, alt[:40], nome[:40]))

    print('A CONTA DA 25.9 SOBRE O BANCO DE VERDADE: %d anuncio(s) julgado(s), '
          '%d veredito(s) mudaram.' % (total, len(mudaram)))
    for slug, iid, antes_v, depois_v in mudaram:
        print('  %s item %s: entra_na_pagina %s -> %s' % (slug, iid, antes_v, depois_v))
    for f in falhas:
        print(f)
    print('\n%d mundo(s) fabricado(s) e %d afirmacao(oes), %d falha(s).'
          % (len(MUNDOS), afirmacoes, len(falhas)))
    print('APROVADO' if not falhas else 'REPROVADO')

    return 1 if falhas else 0


def laudo(gravar=False):
    banco = carregar()
    marcados_total = 0
    for bloco in banco['consultas']:
        print('=== %s' % bloco['slug'])
        antes = json.loads(json.dumps(bloco['resumo']))
        marcados = col.marcar_repeticao_da_loja(bloco, dizer=True)
        marcados_total += len(marcados)
        col.recontar_resumo(bloco)
        depois = bloco['resumo']
        for campo in sorted(set(antes) | set(depois)):
            if antes.get(campo) != depois.get(campo):
                print('    %s: %r -> %r' % (campo, antes.get(campo), depois.get(campo)))
        if not marcados:
            print('    nenhuma repeticao da propria loja nesta consulta.')

    print('\n%d anuncio(s) marcado(s) como repeticao da propria loja.' % marcados_total)
    if gravar:
        with open(BANCO, 'w', encoding='utf-8') as f:
            # O RECUO SAI DO DONO DO ARQUIVO, nunca digitado aqui: digitado, ele
            # saiu `2` contra o `1` do coletor e o diff veio com 2.199 linhas
            # reformatadas para marcar UM anuncio.
            json.dump(banco, f, ensure_ascii=False, indent=col.RECUO_DO_BANCO)
            f.write('\n')
        print('GRAVADO em %s' % os.path.relpath(BANCO, RAIZ))
    else:
        print('NADA GRAVADO (use --gravar).')

    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--conferir', action='store_true',
                   help='o portao: mundos fabricados mais a assimetria da 25.9 '
                        'sobre o banco de verdade, sem gravar')
    p.add_argument('--gravar', action='store_true',
                   help='grava a marca derivada no banco')
    args = p.parse_args()
    if args.conferir:
        return conferir()

    return laudo(gravar=args.gravar)


if __name__ == '__main__':
    sys.exit(main())
