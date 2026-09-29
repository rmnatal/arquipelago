#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sobe o degrau da escada da 25.1: acha a FICHA de produto dos itens presos no 4.

    python3 ferramentas/coletar-shopee.py --ensaio  [--so <id>] [--limite N]
    python3 ferramentas/coletar-shopee.py --gravar  [--so <id>] [--limite N]

`--ensaio` nao toca no banco: escreve o laudo na tela e para. A 25.3 manda
conferir uma amostra com os olhos antes de gravar, e ensaio sem gravacao e o
unico jeito de isso ser verdade e nao cerimonia.

Credencial: `SHOPEE_APP_ID` e `SHOPEE_SECRET` no AMBIENTE, nunca em arquivo e
nunca em log (secao 25.6 do ARQUIPELAGO.md). Esta ferramenta nao le documento
nenhum: quem a chama ja passou os dois em memoria.

---------------------------------------------------------------------------
O QUE ELA CONSERTA, com o numero
---------------------------------------------------------------------------
Em 29/09/2026 a escada deste banco era **1:1 · 2:5 · 3:4 · 4:28**. Vinte e oito
dos trinta e oito registros serviam ao leitor uma PAGINA DE BUSCA, que e o piso
garantido da 25.2 — nao apodrece, nao esgota, e converte pior que ficha.

Treze desses 28 sao as pastilhas, e elas NAO entram aqui: a Shopee nao anuncia
a codificacao da Glass Mosaic, e casar `K2501` com *"Pastilha de Vidro Cristal
2,3x2,3 BRANCO CG10"* exige a decisao de `afiliado.tipo_de_casamento:
"equivalente"` descrita em `dados/links-afiliado-pendentes.md` — decisao do
Raphael, nao desta ferramenta. **Sobram 15**, e sao eles o alvo: produto com
marca e nome de fabricante, que e o caso em que casamento se PROVA.

---------------------------------------------------------------------------
A ESCADA DE PALAVRA-CHAVE, e por que a desta ilha nao e a da 25.6 ao pe da letra
---------------------------------------------------------------------------
A 25.6 escreveu a escada na Robometria, onde o degrau 1 e *"o codigo do
fabricante sozinho"* — e la isso funciona porque codigo de peca de robo (`ERB10`,
`KPCEL01`) e escrito no titulo do anuncio pelo vendedor de reposicao. Aqui nao:
os codigos deste banco sao `61341`, `68.51.050.000`, `REV110624`, `BRSA005` —
SKU interno de catalogo industrial, que nenhum vendedor de Shopee digita. Codigo
sozinho aqui devolve numero solto e casa com o mundo, que e a armadilha 3 da
25.7. Entao a escada desta ilha e:

    1. marca + codigo do fabricante       (so quando ha codigo)
    2. marca + nome comercial inteiro
    3. a chave de hoje, `afiliado.url_busca_produto` — ja medida na API
    4. marca + os dois primeiros tokens do nome comercial (a mais larga)

**O degrau em que cada item casou fica GRAVADO**, como a escada de fontes do
banco: e procedencia. Sem ela ninguem sabe se o casamento veio do codigo exato
ou de uma frase folgada, e as duas coisas nao valem o mesmo.

A regra que decide o casamento NAO esta neste arquivo: esta em
`ferramentas/casar-anuncio.py`, sozinha, porque `ferramentas/mutacoes-casamento.py`
ataca a MESMA funcao que esta ferramenta usa.

---------------------------------------------------------------------------
QUAL DEGRAU DA 25.1 O CASAMENTO ENTREGA, e ele nunca e chutado para cima
---------------------------------------------------------------------------
- **Degrau 1** so quando o nome da loja traz a marca do fabricante E uma palavra
  de loja oficial. `arteciaoficial` tem "oficial" e NAO e a Acrilex: revendedor
  que se chama oficial e revendedor. As duas condicoes juntas, ou nao e 1.
- **Degrau 3** em todo o resto: anuncio de vendedor comum, o degrau que quebrou
  quatro links em doze horas em 13/09/2026. Ele exige `url_busca` preenchida
  pela propria 25.1 — e os 15 ja tem, desde 25/09.

Errar para baixo custa uma ressalva mais dura na tela; errar para cima faz a
metodologia declarar um rigor que a ilha nao tem. **Na duvida, 3.**

---------------------------------------------------------------------------
A FOTO ENTRA MEDIDA OU NAO ENTRA (25.7)
---------------------------------------------------------------------------
A API devolve `imageUrl` e NAO devolve dimensao. Largura e altura saem dos
primeiros bytes do arquivo servido, por `ferramentas/medir-imagens.py`, que ja
existia e nao foi reescrito aqui. Se o download falhar ou o formato nao for
reconhecido, **a foto nao entra** — caixa de imagem sem medida e o salto de
layout da 22.4, e dimensao digitada e a mesma familia do numero de tela
digitado: parece conferida.

---------------------------------------------------------------------------
O QUE ELA NUNCA FAZ
---------------------------------------------------------------------------
- Nao clica no link de afiliado da ilha. A 25.8 e explicita: o salto do
  encurtador e onde a plataforma CONTA o clique, e autoclique com a etiqueta da
  ilha destroi o primeiro clique organico, que e o sinal que a leitura semanal
  procura. A prova de vida do anuncio e a API te-lo devolvido nesta passada.
- Nao mexe em `url_busca` nem em `url_busca_produto`: o piso da 25.2 continua
  sendo o piso, e quem o gera e `ferramentas/gerar-links-afiliado.py`.
- Nao toca nas pastilhas, nem que passem na regra. Ver acima.
"""

import argparse
import datetime
import importlib.util
import json
import os
import sys
import time
import urllib.parse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FERRAMENTAS = os.path.join(RAIZ, 'ferramentas')


def _modulo(nome, caminho):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


shopee = _modulo('shopee_api', os.path.abspath(
    os.path.join(RAIZ, '..', '..', 'ferramentas', 'shopee-api.py')))
casar = _modulo('casar_anuncio', os.path.join(FERRAMENTAS, 'casar-anuncio.py'))
medir = _modulo('medir_imagens', os.path.join(FERRAMENTAS, 'medir-imagens.py'))

SUB_ID = 'clubedomosaico'     # a Shopee recusa sub-id com hifen ou sublinhado
QUANTOS = 12
PAUSA = 0.4                   # a API nao publica limite; folga barata contra 429
HOJE = datetime.date.today().isoformat()

# As treze pastilhas ficam de fora por decisao pendente do Raphael, nao por
# falha da regra. Ver o cabecalho.
FORA = ('dados/materiais-pastilhas.json',)

PALAVRAS_DE_LOJA_OFICIAL = ('oficial', 'official', 'store', 'brasil')


def bancos():
    dados = os.path.join(RAIZ, 'dados')
    return sorted(os.path.join(dados, n) for n in os.listdir(dados)
                  if n.startswith('materiais-') and n.endswith('.json'))


def carregar():
    arquivos, registros = {}, []
    for caminho in bancos():
        arquivos[caminho] = json.load(open(caminho, encoding='utf-8'))
        for item in arquivos[caminho]['materiais']:
            item['_arquivo'] = caminho
            registros.append(item)
    return arquivos, registros


def chave_de_hoje(reg):
    """A palavra-chave dentro de `url_busca_produto`, decodificada."""
    bruto = (reg.get('afiliado') or {}).get('url_busca_produto') or ''
    consulta = urllib.parse.urlparse(bruto).query
    return (urllib.parse.parse_qs(consulta).get('keyword') or [''])[0].strip()


def escada(reg):
    """Os degraus de palavra-chave deste registro, do mais preciso ao mais largo."""
    marca = (reg.get('marca') or '').strip()
    nome = (reg.get('nome_comercial') or '').replace('-', ' ').replace(',', ' ')
    nome = ' '.join(nome.split())
    degraus = []
    if reg.get('codigo_fabricante'):
        degraus.append((1, ('%s %s' % (marca, reg['codigo_fabricante'])).strip()))
    degraus.append((2, ('%s %s' % (marca, nome)).strip()))
    de_hoje = chave_de_hoje(reg)
    if de_hoje:
        degraus.append((3, de_hoje))
    largos = [p for p in casar.tokens(nome) if p not in casar.tokens(marca)][:2]
    if largos:
        degraus.append((4, ('%s %s' % (marca, ' '.join(largos))).strip()))
    # Chave repetida e chamada de rede repetida sem resposta nova.
    vistas, unicos = set(), []
    for n, chave in degraus:
        c = chave.lower()
        if c and c not in vistas:
            vistas.add(c)
            unicos.append((n, chave))
    return unicos


def degrau_da_escada_de_compra(loja, marca):
    """1 so quando a loja e do fabricante; 3 em todo o resto. Nunca para cima."""
    nome = casar.sem_acento(loja or '').lower()
    tokens_marca = casar.tokens(marca or '')
    tem_marca = any(t in nome for t in tokens_marca if len(t) >= 4)
    tem_palavra = any(p in nome for p in PALAVRAS_DE_LOJA_OFICIAL)
    if tem_marca and tem_palavra:
        return 1, 'a loja "%s" traz a marca e palavra de loja oficial' % loja
    return 3, 'a loja "%s" e vendedor comum (25.1, degrau 3)' % loja


def foto_medida(url):
    """(largura, altura) lidas do arquivo servido, ou None. Nunca estimadas."""
    dados = medir.baixar(url)
    if not dados:
        return None
    return medir.dimensao(dados)


def procurar(reg, todos, irmaos_de, quantos=QUANTOS):
    """Desce a escada e para no primeiro degrau que identificar UM registro.

    Devolve (oferta, degrau_da_chave, chave, laudo) ou (None, ..., laudo) com o
    motivo escrito — item que desce a escada inteira sem casar fica sem ficha e
    sem foto, e isso e medicao honesta, nao falha (25.6).
    """
    visto = []
    for numero, chave in escada(reg):
        try:
            ofertas = shopee.buscar(chave, quantos)
        except shopee.ErroDaShopee as erro:
            visto.append({'degrau': numero, 'chave': chave, 'erro': str(erro)})
            continue
        time.sleep(PAUSA)
        visto.append({'degrau': numero, 'chave': chave, 'ofertas': len(ofertas)})
        for oferta in ofertas:
            escolhido, laudo = casar.casar(oferta['titulo'], todos, irmaos_de)
            if escolhido is not None and escolhido.get('id') == reg.get('id'):
                return oferta, numero, chave, visto
    return None, None, None, visto


def main():
    p = argparse.ArgumentParser(description='sobe o degrau dos itens presos no 4')
    p.add_argument('--gravar', action='store_true')
    p.add_argument('--ensaio', action='store_true')
    p.add_argument('--so', default=None, help='um id de registro')
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
        if any(reg['_arquivo'].endswith(f) for f in FORA):
            continue
        af = reg.get('afiliado') or {}
        if af.get('url'):
            continue
        if af.get('degrau') != 4:
            continue
        if args.so and reg['id'] != args.so:
            continue
        alvos.append(reg)
    if args.limite:
        alvos = alvos[:args.limite]

    print('alvos: %d registros no degrau 4 e sem ficha (fora as pastilhas)\n' % len(alvos))
    casados = sem_casar = com_foto = 0

    for reg in alvos:
        oferta, numero, chave, visto = procurar(reg, registros, irmaos_de)
        if oferta is None:
            sem_casar += 1
            tentadas = '; '.join(
                '%d "%s" -> %s' % (v['degrau'], v['chave'],
                                   v.get('erro') or ('%s ofertas' % v['ofertas']))
                for v in visto)
            motivo = ('nenhum anuncio identificou este registro sozinho na escada '
                      'de palavra-chave de %s: %s' % (HOJE, tentadas))
            print('  SEM FICHA  %-44s %s' % (reg['id'], tentadas))
            if args.gravar:
                reg['afiliado']['motivo_sem_ficha'] = motivo
                reg['afiliado'].pop('casamento', None)
            continue

        degrau, porque = degrau_da_escada_de_compra(oferta['loja'], reg.get('marca'))
        try:
            curto = shopee.encurtar(oferta['url_produto'], SUB_ID,
                                    (reg['afiliado'] or {}).get('sub_id_2'))
        except shopee.ErroDaShopee as erro:
            sem_casar += 1
            print('  CASOU E NAO ENCURTOU  %-32s %s' % (reg['id'], erro))
            if args.gravar:
                reg['afiliado']['motivo_sem_ficha'] = (
                    'o anuncio casou em %s (degrau de chave %d) e a API recusou '
                    'encurtar: %s. Link sem sub-id nao entra no banco (25.8).'
                    % (HOJE, numero, erro))
            continue

        dimensao = foto_medida(oferta['imagem_url']) if oferta.get('imagem_url') else None
        casados += 1
        print('  CASOU      %-44s degrau %d | chave %d | %s'
              % (reg['id'], degrau, numero, (oferta['titulo'] or '')[:52]))
        if not args.gravar:
            continue

        af = reg['afiliado']
        af['url'] = curto
        af['url_produto'] = oferta['url_produto']
        af['degrau'] = degrau
        af['gerado_em'] = HOJE
        af['conferido_em'] = HOJE
        af.pop('motivo_sem_ficha', None)
        af['casamento'] = {
            'casado_em': HOJE,
            'regra': 'ferramentas/casar-anuncio.py (cinco travas mais unicidade)',
            'degrau_da_palavra_chave': numero,
            'palavra_chave': chave,
            'titulo_do_anuncio': oferta['titulo'],
            'loja': oferta['loja'],
            'item_id': oferta['item_id'],
            'shop_id': oferta['shop_id'],
            'por_que_este_degrau_da_25_1': porque,
            'prova_de_vida': ('a API devolveu este anuncio em %s. Nao foi clicado: '
                              'o salto do encurtador e onde a Shopee conta o clique '
                              'e autoclique com a etiqueta da ilha apaga o primeiro '
                              'clique organico (25.8).' % HOJE),
        }
        if dimensao:
            com_foto += 1
            reg['imagem'] = {
                'url': oferta['imagem_url'],
                'largura': dimensao[0],
                'altura': dimensao[1],
                'fonte': 'Open API de Afiliados da Shopee (25.6), anuncio casado',
                'coletado_em': HOJE,
                'alt': reg.get('nome_comercial') or reg['id'],
            }
        elif oferta.get('imagem_url'):
            print('             foto NAO entrou: dimensao nao lida do arquivo servido')

    print('\ncasaram %d | sem ficha %d | com foto medida %d' % (casados, sem_casar, com_foto))

    if not args.gravar:
        print('\nensaio: nada foi gravado.')
        return 0

    for caminho, conteudo in arquivos.items():
        for item in conteudo['materiais']:
            item.pop('_arquivo', None)
        esperando = sum(1 for m in conteudo['materiais']
                        if not ((m.get('afiliado') or {}).get('url')))
        sem_imagem = sum(1 for m in conteudo['materiais'] if m.get('imagem') is None)
        conteudo.setdefault('afiliado', {})['itens_esperando_link'] = esperando
        conteudo.setdefault('imagens', {})['itens_sem_imagem'] = sem_imagem
        with open(caminho, 'w', encoding='utf-8') as saida:
            json.dump(conteudo, saida, ensure_ascii=False, indent=2)
            saida.write('\n')
    print('bancos gravados.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
