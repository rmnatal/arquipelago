#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mede pelo ESPELHO a dimensao das fotos que a nuvem nao alcanca, e grava.

    python3 ferramentas/coletar-dimensao-imagens.py --ensaio
    python3 ferramentas/coletar-dimensao-imagens.py --gravar

Producao, nao portao. Quem mede a regra e `teste-cdn-shopee.py` (bancada) e
`conferir-espelho-cdn.py` (no ar, com o grupo de controle).

---------------------------------------------------------------------------
O QUE ESTA FERRAMENTA MUDA E O QUE ELA NAO MUDA
---------------------------------------------------------------------------
MUDA: `imagem.largura`, `imagem.altura`, `imagem.medida_em` e
`imagem.medida_como`; e apaga `motivo_sem_medida`, que descrevia uma ausencia
que deixou de existir (V19 recusa o registro que tenha os dois).

NAO MUDA, e cada um por um motivo diferente:

- **`imagem.url`.** Continua apontando para `down-bs-br.img.susercontent.com`.
  As oito fotos do grupo de controle PROVAM que aquele host entrega o arquivo a
  quem tem navegador — a Sentinela as mediu ali, no Chrome, em 13/09/2026. Ou
  seja, o host funciona para o visitante; quem nao o alcanca e esta nuvem.
  Trocar o que o visitante recebe para contornar um limite da maquina que
  constroi o site seria o rabo abanando o cachorro.

- **`imagem.verificado_em`.** Continua `null`. Esse campo e a data em que
  ALGUEM ABRIU A URL SERVIDA e viu a imagem carregar, e ninguem abriu. Ler o
  cabecalho pelo espelho prova que o arquivo existe e que e imagem; nao prova
  que o endereco servido entrega. Tres datas, tres vidas — `coletado_em`,
  `verificado_em` e `medida_em` sao atos diferentes, e so o terceiro aconteceu
  aqui. Encostar um no outro para o campo parecer preenchido e exatamente o que
  o esquema desta ilha chama de numero com cara de medido.

- **`imagem.alt` e `imagem.alt_origem`.** Quem le bytes nao ve imagem. As 24
  fotos desta fila tem `alt` descritivo escrito por quem viu a foto, e essa e
  a metade que esta ferramenta nao tem como produzir nem como conferir.
"""

import argparse
import glob
import importlib.util
import json
import os
import sys
from datetime import date

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_spec = importlib.util.spec_from_file_location(
    'regua_cdn', os.path.join(RAIZ, 'ferramentas', 'regua-cdn-shopee.py'))
regua = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(regua)

# O TEXTO DO `medida_como` E PARTE DO DADO, e nao um comentario. Quem ler este
# banco daqui a tres meses precisa saber que o numero NAO veio da URL que esta
# ao lado dele, e precisa saber por que confiar nele mesmo assim.
COMO = ('cabecalho do arquivo lido pelo ESPELHO do CDN da Shopee '
        '(%s), que serve o MESMO identificador de arquivo da url ao lado — '
        'esta nuvem nao alcanca o host daquela url e por isso nao a le direto. '
        'A identidade entre os dois hosts nao e suposta: '
        'ferramentas/conferir-espelho-cdn.py remede, a cada passada, as 8 fotos '
        'deste banco que estao no host bloqueado e cuja dimensao a Sentinela '
        'mediu no Chrome do Raphael em 13/09/2026 (naturalWidth x '
        'naturalHeight) — 8 de 8 batem, inclusive em 265, 692, 726 e 1001, que '
        'sao os numeros que um espelho servindo miniatura nao reproduziria.'
        % regua.HOST_ALCANCAVEL)


def bancos():
    return sorted(glob.glob(os.path.join(RAIZ, 'dados', 'produtos-*.json')))


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    modo = p.add_mutually_exclusive_group(required=True)
    modo.add_argument('--ensaio', action='store_true')
    modo.add_argument('--gravar', action='store_true')
    p.add_argument('--so', default=None)
    args = p.parse_args()

    hoje = date.today().isoformat()
    medidas, falhou, pulados = [], [], 0

    for caminho in bancos():
        with open(caminho, encoding='utf-8') as f:
            dados = json.load(f)
        mudou = False
        for produto in dados.get('produtos') or []:
            img = produto.get('imagem') or {}
            if not img.get('url'):
                continue
            if args.so and produto.get('id') != args.so:
                continue
            if img.get('largura') is not None:
                pulados += 1
                continue

            L, A, alvo, erro = regua.medir_no_espelho(img['url'])
            if L is None:
                falhou.append((produto['id'], alvo, erro))
                continue
            # DIMENSAO NAO POSITIVA NAO E DIMENSAO. O V19 recusa `<= 0`, e e
            # melhor o registro seguir com `motivo_sem_medida` do que receber um
            # par que o validador vai recusar depois, fora do alcance de quem
            # escreveu.
            if L <= 0 or A <= 0:
                falhou.append((produto['id'], alvo, 'dimensao nao positiva: %dx%d' % (L, A)))
                continue

            medidas.append((produto['id'], L, A, alvo))
            if args.gravar:
                img['largura'] = L
                img['altura'] = A
                img['medida_em'] = hoje
                img['medida_como'] = COMO
                img.pop('motivo_sem_medida', None)
                mudou = True

        if mudou:
            dados['atualizado_em'] = hoje
            with open(caminho, 'w', encoding='utf-8') as f:
                # indent=2 E O FORMATO DESTE BANCO, e nao uma preferencia.
                # A primeira versao gravou com indent=1 e reformatou 2.500
                # linhas para mudar 24 campos — diff que ninguem revisa e a
                # maneira mais eficiente de esconder uma mudanca real no meio
                # de ruido. `coletar-shopee.py` grava o mesmo banco com 2.
                json.dump(dados, f, ensure_ascii=False, indent=2)
                f.write('\n')

    print('%d ja tinham dimensao e nao foram tocadas' % pulados)
    print('%d medidas pelo espelho:' % len(medidas))
    for ident, L, A, alvo in medidas:
        print('  %-30s %4d x %-4d  %s' % (ident, L, A, alvo))
    if falhou:
        print('\n%d NAO mediram, e seguem com motivo_sem_medida:' % len(falhou))
        for ident, alvo, erro in falhou:
            print('  %-30s %s — %s' % (ident, alvo, erro))
    if args.ensaio:
        print('\nensaio: NADA foi gravado no banco.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
