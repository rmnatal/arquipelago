#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A REGUA DA 30.5 — remede o veredito de SERP das consultas de PRODUTO.

    python3 ferramentas/recalibrar-30-5.py            # mostra o remedido
    python3 ferramentas/recalibrar-30-5.py --gravar    # escreve em serp-das-filhas.json
    python3 ferramentas/recalibrar-30-5.py --conferir  # refaz e reprova se divergir

A secao 30.5 do ARQUIPELAGO.md, decidida pelo Raphael em 09/10/2026, manda:

    *"lojinha pequena do nicho, anuncio solto de marketplace, Pinterest, YouTube,
    forum e blog antigo NAO tornam a busca tomada, sozinhos nem somados. Tomada e
    quando o top 10 e dominado por varejo grande, fabricante forte ou fazenda de
    conteudo com pagina dedicada aquela consulta. Veredito TOMADA antigo de
    consulta de produto e remedido por esta regua antes de valer."*

E e por isso que esta ferramenta existe em vez de alguem reescrever os vereditos a
mao: *remedir* cinco vereditos a mao e cinco chances de puxar o resultado para o
lado de quem quer publicar. Aqui a classificacao de cada OCUPANTE e declarada no
arquivo, com motivo, e o VEREDITO e calculado dela — e `--conferir` reprova se o
gravado discordar do calculado.

---------------------------------------------------------------------------
QUEM CONTA E QUEM NAO CONTA, e a lista e a da propria 30.5
---------------------------------------------------------------------------
CONTAM para `tomada` (os tres que a secao nomeia):
  varejo_grande        — Telhanorte, Leroy Merlin, MadeiraMadeira, Extra, Casas
                         Bahia, Magazine Luiza, Americanas, Amazon
  fabricante_forte     — fabricante com marca nacional e pagina dedicada
  fazenda_de_conteudo  — dominio que publica em escala para ocupar busca

NAO CONTAM (os seis que a secao nomeia, mais tres que ela implica):
  lojinha_do_nicho · anuncio_de_marketplace · pinterest · video · forum ·
  blog_antigo · agregador · obra_ou_revestimento · fora_do_pais · institucional

---------------------------------------------------------------------------
O LIMIAR, nomeado em vez de sentido
---------------------------------------------------------------------------
A 30.5 diz `dominado` e nao diz um numero. Aqui `dominado` e **6 ou mais das 10
vagas** ocupadas por quem CONTA — maioria absoluta do top 10.

O limiar nao foi escolhido no vacuo: ele e o unico numero que separa os dois casos
extremos que esta ilha ja tinha medido, e separa com folga nos dois lados.
`pergunta:pastilha-placa-ou-caixa` tem Telhanorte com 4 paginas, Extra com 3 e
MadeiraMadeira com 2 — **9 vagas de varejo grande**, e nenhuma leitura honesta
chama isso de aberto. `alicate/torques` tem Cortag Pro e mais nada: **1 vaga**, com
as outras 9 em ferramentaria pequena, YouTube e dois blogs. Qualquer limiar entre 2
e 9 daria o mesmo veredito para esses dois; 6 e o meio, e e o que a palavra
`dominado` quer dizer em portugues.

**O MARCADOR `anuncio_de_marketplace` E O QUE MAIS MUDA DE VEREDITO, e ele e a
decisao mais discutivel desta regua — por isso esta escrita aqui e nao escondida
no codigo.** Mercado Livre, Shopee e Elo7 sao marketplace, nao varejo grande, e a
30.5 nomeia *"anuncio solto de marketplace"* entre os que NAO contam. Uma pagina de
LISTA do Mercado Livre para `pastilhas para mosaico` e, sim, uma pagina dedicada
aquela consulta — e continua sendo a agregacao que o marketplace gera sozinho, sem
ninguem responder nada. E exatamente o que a ilha existe para vencer: o PROMPT.md
mediu em 10/09/2026 que o top 10 destas consultas e *"lojinhas WooCommerce pequenas,
listas do Mercado Livre, Pinterest, YouTube, Wikipedia, blog de 2012"* e que
**"ninguem responde as perguntas tecnicas"**. Entao lista de marketplace nao conta.
Se o Raphael decidir o contrario, muda-se a linha de `CONTAM` e os vereditos se
recalculam todos juntos, que e a razao de a conta nao estar em prosa.

---------------------------------------------------------------------------
O QUE ESTA FERRAMENTA NAO FAZ
---------------------------------------------------------------------------
- **Nao mede SERP.** Ela reclassifica OCUPANTE JA MEDIDO. Medir e busca, e o canal
  desta nuvem tem os cinco limites escritos em `serp-das-filhas.json`.
- **Nao alcanca consulta que nunca foi medida.** As paginas de consulta de produto
  do despacho (3) sao slugs NOVOS; o que esta regua remede sao os vereditos que
  existem. O que falta para cada slug novo esta escrito no proprio arquivo.
- **Nao decide se a pagina nasce.** Isso e `cruzamento-14-9.py`, com os dois portoes.
"""

import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERP = os.path.join(RAIZ, 'dados', 'serp-das-filhas.json')

CONTAM = ('varejo_grande', 'fabricante_forte', 'fazenda_de_conteudo')
NAO_CONTAM = ('lojinha_do_nicho', 'anuncio_de_marketplace', 'pinterest', 'video',
              'forum', 'blog_antigo', 'agregador', 'obra_ou_revestimento',
              'fora_do_pais', 'institucional')
LIMIAR = 6
VAGAS = 10


def veredito(ocupantes):
    """(classificacao, vagas_que_contam, motivo) a partir dos ocupantes classificados.

    `ocupantes` e a lista de {nome, vagas, tipo, motivo} daquela medicao.
    """
    desconhecidos = [o['nome'] for o in ocupantes
                     if o['tipo'] not in CONTAM + NAO_CONTAM]
    if desconhecidos:
        raise SystemExit('tipo de ocupante desconhecido em %s — '
                         'tipo novo entra na lista desta ferramenta, nunca calado'
                         % ', '.join(desconhecidos))

    contam = sum(int(o['vagas']) for o in ocupantes if o['tipo'] in CONTAM)
    quem = [o for o in ocupantes if o['tipo'] in CONTAM]

    if contam >= LIMIAR:
        motivo = ('%d das %d vagas sao de quem a 30.5 conta (%s) — %d ou mais e '
                  'dominado' % (contam, VAGAS,
                                '; '.join('%s, %s, %d vaga(s)'
                                          % (o['nome'], o['tipo'], o['vagas'])
                                          for o in quem), LIMIAR))
        return 'TOMADA', contam, motivo

    if quem:
        lista = '; '.join('%s (%s, %d)' % (o['nome'], o['tipo'], o['vagas']) for o in quem)
        motivo = ('so %d das %d vagas sao de quem a 30.5 conta (%s); as outras %d sao '
                  'lojinha do nicho, anuncio de marketplace, video, forum ou blog '
                  'antigo, que pela 30.5 NAO tornam a busca tomada, sozinhos nem '
                  'somados' % (contam, VAGAS, lista, VAGAS - contam))
    else:
        motivo = ('NENHUMA das %d vagas e de varejo grande, fabricante forte ou '
                  'fazenda de conteudo; o top 10 inteiro e de quem a 30.5 declara '
                  'que nao toma a busca' % VAGAS)
    return 'ABERTA', contam, motivo


def recalibrar(doc):
    """Devolve (linhas, mudancas). Nao escreve nada."""
    linhas, mudancas = [], []
    for m in doc['medicoes']:
        oc = m.get('ocupantes_30_5')
        if not oc:
            continue
        novo, contam, motivo = veredito(oc)
        antes = m.get('classificacao')
        linhas.append({'recorte': m['recorte'], 'consulta': m['consulta'],
                       'antes': antes, 'depois': novo, 'vagas_que_contam': contam,
                       'motivo': motivo})
        if novo != antes:
            mudancas.append(linhas[-1])
    return linhas, mudancas


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--gravar', action='store_true')
    p.add_argument('--conferir', action='store_true')
    a = p.parse_args()

    with io.open(SERP, encoding='utf-8') as f:
        doc = json.load(f)

    linhas, mudancas = recalibrar(doc)
    if not linhas:
        print('nenhuma medicao tem `ocupantes_30_5` — a regua nao tem o que remedir')
        return 0

    for l in linhas:
        seta = '%s -> %s' % (l['antes'], l['depois'])
        print('  %-36s %-26s %d/%d contam' % (l['recorte'], seta,
                                              l['vagas_que_contam'], VAGAS))

    if a.conferir:
        falhas = []
        for m in doc['medicoes']:
            if not m.get('ocupantes_30_5'):
                continue
            novo, contam, _ = veredito(m['ocupantes_30_5'])
            if m.get('classificacao_30_5') != novo:
                falhas.append('%s: gravado %r, a regua calcula %r'
                              % (m['recorte'], m.get('classificacao_30_5'), novo))
            if m.get('vagas_que_contam_30_5') != contam:
                falhas.append('%s: vagas gravadas %r, a regua conta %r'
                              % (m['recorte'], m.get('vagas_que_contam_30_5'), contam))
        for f in falhas:
            print('  DEFEITO %s' % f)
        print('%s: %d medicoes remedidas, %d defeito(s)'
              % ('REPROVADO' if falhas else 'APROVADO', len(linhas), len(falhas)))
        return 1 if falhas else 0

    if a.gravar:
        for m in doc['medicoes']:
            if not m.get('ocupantes_30_5'):
                continue
            novo, contam, motivo = veredito(m['ocupantes_30_5'])
            m['classificacao_30_5'] = novo
            m['vagas_que_contam_30_5'] = contam
            m['motivo_30_5'] = motivo
        with io.open(SERP, 'w', encoding='utf-8') as f:
            json.dump(doc, f, ensure_ascii=False, indent=1)
            f.write('\n')
        print('\ngravado: %s (%d medicoes, %d trocaram de veredito)'
              % (os.path.relpath(SERP, RAIZ), len(linhas), len(mudancas)))
    else:
        print('\n%d medicoes, %d trocariam de veredito (nada gravado; use --gravar)'
              % (len(linhas), len(mudancas)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
