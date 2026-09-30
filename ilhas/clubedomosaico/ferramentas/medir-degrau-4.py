#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""POR QUE ESTE ITEM PAROU NO DEGRAU 4 — medido hoje, nunca herdado.

    python3 ferramentas/medir-degrau-4.py --ensaio  [--so <id>] [--limite N]
    python3 ferramentas/medir-degrau-4.py --gravar  [--so <id>] [--limite N]

`--ensaio` nao toca no banco. `--gravar` escreve `afiliado.motivo_sem_ficha` nos
itens medidos, e so neles.

---------------------------------------------------------------------------
O NUMERO QUE PEDIU ESTA FERRAMENTA
---------------------------------------------------------------------------
Ronda diaria tecnica de 30/09/2026: **17 dos 38 registros deste banco estao no
degrau 4** e **12 deles nao escrevem por que**. Tinham so
`motivo_da_chave: "familia: medida"`, que diz como a chave foi MONTADA e nao o
que a escada devolveu. A 25.4-b.4 diz que "nao casou" tem duas causas que
parecem uma — o produto nao esta anunciado (so se resolve quando o mercado
mudar) ou os candidatos foram BARRADOS por trava (pode se resolver com trava
melhor ou com um registro de variante que falta). **Contadas juntas, viram um
numero que nao diz o que fazer.**

---------------------------------------------------------------------------
POR QUE ELA NAO E O `coletar-shopee.py`, QUE JA DESCE A MESMA ESCADA
---------------------------------------------------------------------------
Sao dois trabalhos com dois direitos diferentes. O coletor existe para SUBIR o
degrau: quando a regra de casamento identifica um anuncio, ele grava `url`,
`url_produto`, foto e a prova. Por isso ele exclui as treze pastilhas por
`FORA = ('dados/materiais-pastilhas.json',)` — subir o degrau delas dependeria
de `afiliado.tipo_de_casamento: "equivalente"`, que e decisao do Raphael e nao
de uma ferramenta.

**Esta aqui nao sobe nada e por isso pode medi-las.** Ela desce a mesma escada
com a MESMA regra (`casar-anuncio.py`, importada, nunca copiada) e grava apenas
o que ouviu de volta. Nenhum `url` e escrito aqui, em nenhuma hipotese: se um
anuncio casar, ela GRITA na tela e deixa a decisao para quem tem o direito de
tomá-la. Medir nao e o mesmo que agir, e foi por confundir os dois que as treze
pastilhas ficaram dezessete dias sem ninguem perguntar nada a elas.

---------------------------------------------------------------------------
A FORMA DO CAMPO, E ELA E A 25.4-b.3 AO PE DA LETRA
---------------------------------------------------------------------------
A 25.4-b.3 diz que campo de motivo guarda **duas** coisas com vidas diferentes:
a **causa** (nao muda) e a **ultima tentativa** (muda a cada passada), separadas
por um marcador, e que so a segunda se reescreve. Sem isso, "ou a prosa cresce
sem fim, ou a causa e apagada pela tentativa de hoje" — e foi exatamente o que
aconteceu com os 39 links da Aquametria, que carregaram de 13/09 a 23/09 um
motivo dizendo *"TENTADA E RECUSADA"* que havia deixado de ser verdade em 16/09
e, enquanto esteve la, mandava a execucao seguinte **nem tentar**.

O marcador e ` || ` e a forma e esta, uma linha:

    CAUSA (<classe>): <o que nao muda>  ||  ULTIMA TENTATIVA <AAAA-MM-DD>: <o
    que esta passada tentou e o que ouviu de volta>

**AS CLASSES SAO QUATRO, E A PRIMEIRA VERSAO DESTA FERRAMENTA TINHA TRES E
ERRADAS.** Ela classificava pela trava que barrou o candidato, e o ensaio das
17 devolveu **17 de 17 na mesma classe** — exatamente o numero que nao diz nada
de que o despacho de 30/09 reclama. A causa do erro vale mais que o erro: em
`casar.compativel` as travas correm em ORDEM e a primeira que falha encerra o
julgamento, e a trava 5b (o titulo tem de trazer o nome comercial inteiro) quase
sempre falha antes de qualquer trava de irmao ser avaliada. **"Nenhuma trava de
irmao foi acionada" media a ordem do codigo, nao o mundo.** Regua que mede a
ordem em que o portao pergunta nunca reprova o portao.

O que separa as causas no MUNDO e uma pergunta so, e ela e a trava 1: **algum
anuncio da escada traz a marca deste registro?**

- `nao-anunciado` — a escada inteira devolveu ZERO oferta. Nenhum candidato, e
  nenhuma trava acionada. So o mercado resolve.
- `marca-nao-anunciada` — houve oferta e **nenhuma traz a marca**. O produto
  nao e vendido sob o nome que este banco guarda. E o caso das pastilhas Glass
  Mosaic: os degraus 1 e 2 (marca + codigo, marca + nome comercial) devolvem
  zero, e os degraus largos devolvem catalogo de outras marcas. A Shopee TEM o
  produto e o anuncia como CG10/CG21/CG33 — subir o degrau exigiria casar por
  ATRIBUTO (medida, acabamento, cor), que e
  `afiliado.tipo_de_casamento: "equivalente"`, **decisao do Raphael registrada
  em `dados/links-afiliado-pendentes.md`**. A classe existe separada porque este
  caso pede uma RESPOSTA e nao uma trava melhor: contado junto com o de baixo, o
  pedido a ele desaparece dentro de uma divida tecnica que nao e dele.
- `candidato-barrado-nome` — ha anuncio COM a marca, e o que o barra e o NOME:
  a trava 5b (o titulo nao traz o `nome_comercial` inteiro) ou a trava 2 (a
  cabeca do titulo nao e este produto). **A regra nao separa as duas leituras
  possiveis, e por isso o rotulo nao afirma nenhuma:** ou o nosso
  `nome_comercial` e uma frase descritiva escrita por nos em vez do batismo do
  fabricante (secao 26 — e o caso dos tres registros da Quartzolit), ou o
  anuncio e de OUTRO produto da mesma marca cuja diferenca esta exatamente no
  token que falta (e o caso do torques da Cortag, onde os anuncios sao de corte
  RETO e o registro e o CURVO). Nos dois a divida e nossa e nos dois o conserto
  comeca abrindo o anuncio — mas um se conserta no banco e o outro na regra, e
  quem escrever um rotulo que decide isso sem abrir o anuncio esta chutando.
- `candidato-barrado-variante` — ha anuncio COM a marca e um IRMAO do banco
  disputou o titulo. Divida nossa, e do lado da REGRA ou de um registro de
  variante que falta. E a distincao que a 25.4-b.4 pede, e ela so aparece
  quando a marca ja passou.

A classe sai da MEDICAO, nunca de uma lista escrita a mao com ids dentro: o que
a decide e o laudo da propria regra de casamento, lido candidato por candidato.

"""

import argparse
import datetime
import importlib.util
import json
import os
import sys
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FERRAMENTAS = os.path.join(RAIZ, 'ferramentas')

MARCADOR = ' || '
HOJE = datetime.date.today().isoformat()
QUANTOS = 12
PAUSA = 0.4


def _modulo(nome, caminho):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


shopee = _modulo('shopee_api', os.path.abspath(
    os.path.join(RAIZ, '..', '..', 'ferramentas', 'shopee-api.py')))
casar = _modulo('casar_anuncio', os.path.join(FERRAMENTAS, 'casar-anuncio.py'))
coletor = _modulo('coletar_shopee', os.path.join(FERRAMENTAS, 'coletar-shopee.py'))

# A escada de palavra-chave e a do coletor, importada. Regra copiada em dois
# lugares e regra que a bateria mede em um lugar e o banco usa no outro.
escada = coletor.escada
carregar = coletor.carregar

# A TRAVA 1 E A PERGUNTA QUE SEPARA AS CAUSAS: a marca esta no titulo? O texto
# e o que `casar.compativel` devolve quando ela falha, e a comparacao e por
# prefixo porque o resto da frase traz o nome da marca medida.
TRAVA_DA_MARCA = 'a marca '

# AS TRAVAS DE IRMAO: as unicas que falam de OUTRO registro do banco. Sao as que
# dizem que a divida e de variante, e nao de batismo.
TRAVAS_DE_IRMAO = (
    'o titulo nao separa este registro de ',
    'este registro nao tem nenhum token que o separe de ',
    'o titulo traz ',
)


def _sem_marca(motivo):
    return (motivo or '').startswith(TRAVA_DA_MARCA)


def _e_trava_de_irmao(motivo):
    return any((motivo or '').startswith(p) for p in TRAVAS_DE_IRMAO)


def descer(reg, irmaos):
    """Desce a escada inteira e devolve o laudo, degrau por degrau.

    Nao para no primeiro degrau que casa, ao contrario do coletor: quem mede
    quer a escada TODA, senao o motivo escrito fala de um degrau e cala os
    outros tres.
    """
    passos = []
    for numero, chave in escada(reg):
        passo = {'degrau': numero, 'chave': chave, 'ofertas': 0,
                 'barrados': [], 'casou': False, 'erro': None}
        try:
            ofertas = shopee.buscar(chave, QUANTOS)
        except shopee.ErroDaShopee as erro:
            passo['erro'] = str(erro)
            passos.append(passo)
            continue
        time.sleep(PAUSA)
        passo['ofertas'] = len(ofertas)
        for oferta in ofertas:
            titulo = oferta['titulo'] or ''
            ok, motivo = casar.compativel(reg, titulo, irmaos)
            if ok:
                passo['casou'] = True
                passo['barrados'].append({'titulo': titulo, 'motivo': None})
            else:
                passo['barrados'].append({'titulo': titulo, 'motivo': motivo})
        passos.append(passo)
    return passos


def classificar(passos):
    """A classe da causa, e ela sai do laudo — nunca de uma lista de ids."""
    ofertas = sum(p['ofertas'] for p in passos)
    if any(p['casou'] for p in passos):
        return 'casou', 'algum anuncio passou nas cinco travas'
    if ofertas == 0:
        return 'nao-anunciado', ('a escada inteira devolveu zero oferta: nenhuma '
                                 'trava foi acionada porque nao houve candidato')
    barrados = [b['motivo'] for p in passos for b in p['barrados'] if b['motivo']]
    com_marca = [m for m in barrados if not _sem_marca(m)]
    if not com_marca:
        return 'marca-nao-anunciada', (
            'a escada devolveu %d ofertas e NENHUMA traz a marca deste registro; '
            'os degraus por codigo e por nome comercial devolveram zero. O produto '
            'nao e vendido sob o nome que este banco guarda, e subir o degrau '
            'dependeria de casar por atributo — `tipo_de_casamento: "equivalente"`, '
            'decisao do Raphael em dados/links-afiliado-pendentes.md' % len(barrados))
    de_irmao = [m for m in com_marca if _e_trava_de_irmao(m)]
    if de_irmao:
        return 'candidato-barrado-variante', (
            'ha anuncio COM a marca (%d de %d ofertas) e um irmao do banco disputou '
            'o titulo em %d deles: a divida e da regra de casamento ou de um '
            'registro de variante que falta, nao do mercado'
            % (len(com_marca), len(barrados), len(de_irmao)))
    return 'candidato-barrado-nome', (
        'ha anuncio COM a marca (%d de %d ofertas) e o que barra todos e o NOME: o '
        'titulo do vendedor nao traz o `nome_comercial` inteiro deste registro, ou '
        'a cabeca do titulo nao e este produto. Nenhum irmao do banco disputou, '
        'entao a divida e nossa: ou o `nome_comercial` e descricao e nao o batismo '
        'do fabricante (secao 26), ou o anuncio e outro produto da mesma marca. '
        'Quem consertar abre o anuncio — a regra nao separa os dois'
        % (len(com_marca), len(barrados)))


def resumo_da_tentativa(passos):
    """A metade que se reescreve: o que a passada de hoje tentou e ouviu.

    A oferta "mais proxima" e sempre uma que TRAZ A MARCA, quando existe: anuncio
    sem a marca e catalogo de outro fabricante, e citar o motivo dele como se
    fosse o candidato mais proximo e o que faria a linha parecer divida tecnica
    onde ela e pedido de decisao.
    """
    partes = []
    for p in passos:
        if p['erro']:
            partes.append('%d "%s" -> ERRO %s' % (p['degrau'], p['chave'], p['erro']))
            continue
        motivos = [b['motivo'] for b in p['barrados'] if b['motivo']]
        com_marca = [m for m in motivos if not _sem_marca(m)]
        extra = ''
        if com_marca:
            # A mais proxima e a que chegou MAIS LONGE no portao, e as travas
            # correm em ordem: quem foi barrado por um irmao ja passou pela
            # marca, pela cabeca, pelas armadilhas e pelo nome comercial inteiro.
            de_irmao = [m for m in com_marca if _e_trava_de_irmao(m)]
            extra = (', %d com a marca, a mais proxima barrada por: %s'
                     % (len(com_marca), (de_irmao or com_marca)[0]))
        elif motivos:
            extra = ', nenhuma com a marca'
        partes.append('%d "%s" -> %d ofertas%s' % (p['degrau'], p['chave'],
                                                   p['ofertas'], extra))
    return '; '.join(partes)


def causa_gravada(motivo_atual):
    """A causa que ja esta no campo, quando ela ja esta na forma da 25.4-b.3."""
    if motivo_atual and MARCADOR in motivo_atual:
        return motivo_atual.split(MARCADOR, 1)[0].strip()
    return None


def montar(reg, passos, motivo_atual):
    classe, porque = classificar(passos)
    anterior = causa_gravada(motivo_atual)
    if anterior:
        # A CAUSA NAO SE REESCREVE (25.4-b.3): so a tentativa. Se a medicao de
        # hoje discorda da causa gravada, isso e noticia e vai para a tela — nao
        # se conserta calado, porque causa que muda sozinha nao e causa.
        causa = anterior
        if not anterior.startswith('CAUSA (%s)' % classe):
            print('     ATENCAO  a causa gravada nao e a classe medida hoje (%s): %s'
                  % (classe, anterior[:90]))
    else:
        causa = 'CAUSA (%s): %s' % (classe, porque)
    return classe, causa + MARCADOR + ('ULTIMA TENTATIVA %s: %s'
                                        % (HOJE, resumo_da_tentativa(passos)))


def main():
    p = argparse.ArgumentParser(description='por que este item parou no degrau 4')
    p.add_argument('--gravar', action='store_true')
    p.add_argument('--ensaio', action='store_true')
    p.add_argument('--so', default=None)
    p.add_argument('--limite', type=int, default=0)
    args = p.parse_args()
    if not (args.gravar or args.ensaio):
        p.error('escolha --ensaio ou --gravar')

    arquivos, registros = carregar()

    def irmaos_de(reg):
        marca = (reg.get('marca') or '').lower()
        return [x for x in registros
                if (x.get('marca') or '').lower() == marca and x['id'] != reg['id']]

    alvos = []
    for reg in registros:
        af = reg.get('afiliado') or {}
        if af.get('degrau') != 4 or af.get('url'):
            continue
        if args.so and reg['id'] != args.so:
            continue
        alvos.append(reg)
    if args.limite:
        alvos = alvos[:args.limite]

    print('alvos: %d registros no degrau 4 e sem ficha\n' % len(alvos))
    contagem = {}
    casou_alguem = []

    for reg in alvos:
        passos = descer(reg, irmaos_de(reg))
        classe, motivo = montar(reg, passos, (reg.get('afiliado') or {}).get('motivo_sem_ficha'))
        contagem[classe] = contagem.get(classe, 0) + 1
        print('  %-26s %-44s %s' % (classe, reg['id'], resumo_da_tentativa(passos)[:110]))
        if classe == 'casou':
            casou_alguem.append(reg['id'])
            # Subir degrau NAO e trabalho desta ferramenta. Ver o cabecalho.
            print('     >>> ESTE REGISTRO TEM ANUNCIO QUE A REGRA IDENTIFICA. '
                  'Rode coletar-shopee.py e decida — esta ferramenta nao grava url.')
        if args.gravar:
            reg['afiliado']['motivo_sem_ficha'] = motivo
            # `motivo_da_chave` fica: ele conta como a chave foi MONTADA, que e
            # outra pergunta. O que ele nunca podia e responder pela escada.

    print('')
    for classe in sorted(contagem):
        print('  %-28s %d' % (classe, contagem[classe]))

    if not args.gravar:
        print('\nensaio: nada foi gravado.')
        return 1 if casou_alguem else 0

    for caminho, conteudo in arquivos.items():
        for m in conteudo['materiais']:
            m.pop('_arquivo', None)
        with open(caminho, 'w', encoding='utf-8') as fh:
            json.dump(conteudo, fh, ensure_ascii=False, indent=2)
            fh.write('\n')
    print('\ngravado em %d bancos.' % len(arquivos))
    return 1 if casou_alguem else 0


if __name__ == '__main__':
    sys.exit(main())
