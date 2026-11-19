#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DEVOLVE AO BANCO A FOTO QUE UMA MEDICAO VELHA TIROU, QUANDO DOIS INSTRUMENTOS A
MEDEM VIVA HOJE — A IRMA SIMETRICA DA `aplicar-foto-quebrada.py` (19/11/2026).

    python3 ferramentas/aplicar-foto-remedida.py --conferir   # sem rede
    python3 ferramentas/aplicar-foto-remedida.py              # mede e mostra
    ... mais --gravar                                         # grava

O QUE ELA EXISTE PARA FECHAR, e o numero e de receita e nao de faxina: em
19/11/2026 o banco tinha **10 anuncios que SERVEM com `imagem: null`** — 4 na
bicicleta, 1 na moto e 5 no patinete —, e um deles e o PRIMEIRO cartao de
`/veiculos/patinete-eletrico/`, o espaco mais caro da pagina. Cada um desses
cartoes serve o espaco reservado neutro da secao 6 em vez da foto do produto, e
foto e a unica coisa do cartao que MOSTRA o veiculo.

POR QUE AS DEZ ESTAVAM FORA, e a causa de oito delas e uma MEDICAO VENCIDA. A
prosa de `motivo_sem_imagem` de cada uma diz o que foi medido: `503`, `504`,
`403` ou "os primeiros bytes nao traziam cabecalho". A propria
`aplicar-foto-quebrada.py` promete, no cabecalho dela, que **"a foto volta
sozinha no dia em que a CDN voltar"** — porque a coleta remede a foto de todo
anuncio que serve. Esta ferramenta e esse dia, sem precisar de uma recoleta
inteira: ela mexe na FOTO e em nada mais. Preco, veredito de entrada, link,
degrau e `sub_id` saem daqui como entraram.

A PREMISSA QUE CAIU, E ELA ESTA ESCRITA NO CABECALHO DA IRMA: aquele arquivo
diz que "`cf.shopee.com.br` responde `CONNECT tunnel failed, response 403` ao
egresso desta nuvem, entao uma passada de coleta daqui marcaria TODAS as fotos
como ausentes". **Isso e fato do AMBIENTE que mediu, nao do Arquipelago** — a
licao que esta ilha escreveu na manha de 19/11/2026 com tres hosts medidos. Daqui,
em 19/11, `cf.shopee.com.br` devolveu `200 image/jpeg` em TRES passadas de
controle e `206 image/jpeg` nas 30 passadas das dez fotos. Quem escrever "o
egresso recusa X" diz de QUAL ambiente.

A REGRA, E ELA E O CORACAO DESTA FERRAMENTA: FOTO SO VOLTA COM DOIS
INSTRUMENTOS INDEPENDENTES CONCORDANDO.

1. **o cabecalho do arquivo**, pelo `medir_foto` do `coletar-oferta.py` — a
   MESMA funcao que o coletor usa, importada e nunca copiada; e
2. **o DOM**, pelo `medir-foto-no-navegador.mjs`, que le `naturalWidth` num
   navegador de verdade.

E as DIMENSOES tem de fechar entre os dois. O primeiro prova que a origem
respondeu e que os bytes comecam como imagem; o segundo prova que o navegador
PINTA. Foi exatamente essa diferenca que a ronda de 18/11 mediu no Chrome do
Raphael: `complete: true` com `naturalWidth: 0` — uma imagem que o navegador
aceitou e nao conseguiu desenhar. Um instrumento so devolveria foto quebrada
para o espaco mais caro da pagina, que e pior que o reservado.

A URL DA FOTO E PEDIDA A LOJA, NUNCA REMONTADA. O coletor descarta
`url_bruto_da_imagem` depois de medir (de proposito: endereco de CDN que nao foi
medido nao fica guardado parecendo medido), entao o banco NAO tem a URL dos
registros sem foto. Esta ferramenta a pede a Open API pela `chave_que_achou` do
proprio anuncio e casa por `item_id`. **Anuncio que nao estiver na resposta da
chave hoje e DITO e saltado** — remontar endereco de CDN de cabeca e a familia
do nome de funcao derivado que a F3 pagou com tela branca.

A MEDICAO VELHA NAO E APAGADA: ela desce para `historico_da_foto`, com a data e
o AMBIENTE que a produziu. Medicao nao se reescreve, e a de 18/11 no Chrome do
Raphael e a unica coisa do repositorio que fala do navegador do visitante — se
a proxima ronda a medir quebrada outra vez, a irma `aplicar-foto-quebrada.py` a
tira em um comando, e o historico mostra as duas.
"""

import argparse
import importlib.util
import json
import os
import subprocess
import sys
from datetime import date

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AQUI = os.path.join(RAIZ, 'ferramentas')
BANCO = os.path.join(RAIZ, 'dados', 'anuncios-por-consulta.json')
NAVEGADOR = os.path.join(AQUI, 'medir-foto-no-navegador.mjs')
API = os.path.join(os.path.dirname(os.path.dirname(RAIZ)), 'ferramentas', 'shopee-api.py')

HOJE = date.today().isoformat()

# O AMBIENTE QUE MEDE, DITO NO REGISTRO. A frase existe porque o repositorio
# tinha tres lugares afirmando "o egresso desta nuvem recusa X" como se fosse
# fato do Arquipelago, e tres ambientes diferentes mediram paredes diferentes.
AMBIENTE = 'nuvem da Fundacao (claude.ai/code), egresso por proxy de agente'

# A CLASSE DE CAUSA QUE NUNCA SE REMEDE: foto de anuncio recusado nao e medida
# por desenho, entao nao ha medicao vencida para remedir. A comparacao e por
# PREFIXO da prosa do coletor, e o prefixo nao e digitado aqui duas vezes.
CAUSA_DE_QUEM_NAO_SERVE = 'anuncio recusado'


def _modulo(nome, caminho):
    espec = importlib.util.spec_from_file_location(nome, caminho)
    mod = importlib.util.module_from_spec(espec)
    espec.loader.exec_module(mod)
    return mod


def _oferta_mod():
    return _modulo('coletar_oferta', os.path.join(AQUI, 'coletar-oferta.py'))


def _relevancia():
    """O MESMO modulo que o coletor carrega, e pelo MESMO caminho.

    `nome_do_anuncio` mora em `ferramentas/teste-relevancia-do-anuncio.py` e
    NAO em `regras/nomes.py`, que e onde o nome dele sugere. A primeira versao
    deste arquivo o foi buscar em `regras/nomes.py` — derivado de cabeca pelo
    padrao dos vizinhos, que e a familia exata da chamada inexistente que
    custou TELA BRANCA na F3 em 06/11/2026. O autoteste abaixo cobra que a
    funcao EXISTA, para o defeito nao esperar o `--gravar` para aparecer.
    """
    return _modulo('relevancia', os.path.join(AQUI, 'teste-relevancia-do-anuncio.py'))


# --------------------------------------------------------------- a regua
def remediavel(anuncio):
    """(sim, por_que). O anuncio ESTA na fila de remedicao?

    Tres condicoes, e as tres sao sobre o estado de HOJE do registro:
    ele SERVE (anuncio recusado nao tem foto medida por desenho), esta SEM
    foto, e a causa escrita e de MEDICAO — nunca a de quem nao serve.
    """
    if not anuncio.get('serve'):
        return False, 'nao serve: foto de anuncio recusado nao e medida por desenho'
    if anuncio.get('imagem'):
        return False, 'ja tem foto medida'
    causa = (anuncio.get('motivo_sem_imagem') or '').strip()
    if not causa:
        return False, 'sem foto e SEM causa escrita: isto e defeito de banco, nao fila desta ferramenta'
    if causa.lower().startswith(CAUSA_DE_QUEM_NAO_SERVE):
        return False, 'causa e a de quem nao serve, e o anuncio serve: banco se contradiz'
    return True, causa


def concordam(cabecalho, dom):
    """(pode_voltar, por_que). A foto volta SO com os dois instrumentos juntos.

    `cabecalho` e `(largura, altura)` ou None; `dom` e o objeto do laudo do
    navegador. A dimensao tem de fechar entre os dois: cabecalho e DOM lendo o
    mesmo arquivo e discordando do tamanho e sinal de que um dos dois leu outra
    coisa, e nesse caso nao se escolhe o mais simpatico.
    """
    if not cabecalho:
        return False, 'o cabecalho do arquivo nao foi medido'
    if not dom:
        return False, 'o navegador nao devolveu laudo para esta URL'
    if dom.get('desfecho') != 'viva':
        return False, 'o navegador diz `%s`%s' % (
            dom.get('desfecho'),
            '' if dom.get('status_http') is None else ' (HTTP %s)' % dom['status_http'])
    if (dom.get('largura'), dom.get('altura')) != tuple(cabecalho):
        return False, ('cabecalho e DOM discordam da dimensao: %sx%s contra %sx%s'
                       % (cabecalho[0], cabecalho[1], dom.get('largura'), dom.get('altura')))
    return True, 'cabecalho %sx%s e DOM %sx%s, os dois vivos e de acordo' % (
        cabecalho[0], cabecalho[1], dom['largura'], dom['altura'])


def foto_nova(url, dimensao, nome_do_anuncio, dom):
    """O objeto `imagem`, na FORMA EXATA que o coletor grava.

    Os campos sao os dele e a ordem e a dele; o que esta ferramenta acrescenta
    e `medida_por`, que nomeia os DOIS instrumentos e o ambiente — porque foi a
    ausencia dessa frase que deixou "o egresso recusa este dominio" parecer
    fato do Arquipelago.
    """
    return {
        'url': url,
        'largura': dimensao[0],
        'altura': dimensao[1],
        'alt': nome_do_anuncio,
        'fonte': 'anuncio-shopee',
        'coletado_em': HOJE,
        'como_a_dimensao_foi_medida': 'cabecalho do arquivo na CDN, nunca digitada',
        'medida_por': 'cabecalho do arquivo (medir_foto) E %s; ambiente: %s'
                      % (dom['como_foi_medido'], AMBIENTE),
    }


def arquivar_medicao(anuncio, causa):
    """A medicao que tirou a foto desce para o historico, e NAO e apagada."""
    historico = anuncio.setdefault('historico_da_foto', [])
    historico.append({
        'saiu_do_ar_por': causa,
        'arquivada_em': HOJE,
        'arquivada_por': 'aplicar-foto-remedida.py, com dois instrumentos medindo a foto viva',
    })
    return historico


# --------------------------------------------------------------- a rede
def urls_da_chave(chave):
    """(mapa item_id -> url_da_imagem, erro). Uma chamada por chave, nunca por anuncio."""
    cmd = [sys.executable, API, 'busca', chave, '--quantos', '20']
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        return None, (r.stderr or r.stdout or '').strip()[:160]
    try:
        ofertas = json.loads(r.stdout)
    except json.JSONDecodeError as e:
        return None, 'a API devolveu algo que nao e JSON: %s' % e
    return {int(o['item_id']): o.get('imagem_url') for o in ofertas}, None


def laudo_do_navegador(urls):
    """(mapa url -> laudo, erro). Uma chamada para TODAS as URLs: o navegador
    sobe uma vez, e cada foto sobe junto na mesma pagina."""
    if not urls:
        return {}, None
    r = subprocess.run(['node', NAVEGADOR, '-'], input=json.dumps(urls),
                       capture_output=True, text=True)
    if r.returncode != 0:
        return None, (r.stderr or r.stdout or '').strip()[:200]
    try:
        return {x['url']: x for x in json.loads(r.stdout)}, None
    except json.JSONDecodeError as e:
        return None, 'o navegador devolveu algo que nao e JSON: %s' % e


# --------------------------------------------------------------- o trabalho
def trabalhar(gravar):
    banco = json.load(open(BANCO, encoding='utf-8'))
    oferta_mod = _oferta_mod()
    rel = _relevancia()
    medir_foto = oferta_mod.medir_foto

    fila = []
    for bloco in banco['consultas']:
        for a in bloco['anuncios']:
            sim, por_que = remediavel(a)
            if sim:
                fila.append((bloco, a, por_que))

    print('FILA: %d anuncio(s) que SERVEM e estao sem foto, com causa de medicao.\n' % len(fila))
    if not fila:
        print('Nada a remedir. Isto e informacao e nao fracasso.')
        return 0

    # AS URLs, POR CHAVE. Uma chamada de API por chave distinta, e a API desta
    # conta devolve `System Error` de vez em quando: a tentativa se repete, e a
    # repeticao esta DITA no relatorio (secao 20.2 — falha isolada e o tunel).
    por_chave = {}
    for _, a, _ in fila:
        por_chave.setdefault(a.get('chave_que_achou'), [])
    for chave in list(por_chave):
        for tentativa in (1, 2, 3, 4):
            mapa, erro = urls_da_chave(chave)
            if mapa is not None:
                print('chave %-28s -> %2d oferta(s) lida(s) na tentativa %d' % (chave, len(mapa), tentativa))
                por_chave[chave] = mapa
                break
            print('chave %-28s -> tentativa %d falhou: %s' % (chave, tentativa, erro))
        else:
            print('chave %-28s -> NAO LIDA; os anuncios dela ficam como estao' % chave)
            por_chave[chave] = {}

    # O CABECALHO DO ARQUIVO, foto por foto.
    medidos = []
    for bloco, a, causa in fila:
        url = (por_chave.get(a.get('chave_que_achou')) or {}).get(a['item_id'])
        if not url:
            medidos.append((bloco, a, causa, None, None,
                            'o anuncio nao esta na resposta da chave hoje: sem URL medida, nada a remedir'))
            continue
        dim, erro = medir_foto(url)
        medidos.append((bloco, a, causa, url, dim, erro))

    # O DOM, de uma vez.
    dom_mapa, erro_dom = laudo_do_navegador([u for _, _, _, u, d, _ in medidos if u and d])
    if dom_mapa is None:
        print('\nO NAVEGADOR NAO RODOU: %s' % erro_dom)
        print('Nenhuma foto volta com um instrumento so. Nada foi gravado.')
        return 1

    print('')
    mudaram = 0
    for bloco, a, causa, url, dim, erro in medidos:
        rotulo = '%s / %s' % (bloco['id'], a['item_id'])
        if not url:
            print('  SALTA   %-34s %s' % (rotulo, erro))
            continue
        if not dim:
            print('  SEGUE   %-34s cabecalho nao medido: %s' % (rotulo, erro))
            a['motivo_sem_imagem'] = erro
            continue
        pode, por_que = concordam(dim, dom_mapa.get(url))
        if not pode:
            print('  RECUSA  %-34s %s' % (rotulo, por_que))
            a['motivo_sem_imagem'] = ('%s || REMEDIDA em %s no %s: %s'
                                      % (causa.split(' || ')[0], HOJE, AMBIENTE, por_que))
            continue
        arquivar_medicao(a, causa)
        a['imagem'] = foto_nova(url, dim, rel.nome_do_anuncio(a['titulo']), dom_mapa[url])
        a['motivo_sem_imagem'] = None
        mudaram += 1
        print('  VOLTA   %-34s %s' % (rotulo, por_que))

    print('\n%d foto(s) voltam ao banco, de %d na fila.' % (mudaram, len(fila)))

    if not gravar:
        print('\nNADA GRAVADO (sem --gravar).')
        return 0

    # O `resumo` de cada bloco e RECONTADO pela funcao do coletor, e nao a mao:
    # duas contas do mesmo numero comecam iguais e so uma sobe (20.7). Foto nao
    # entra em nenhuma conta do resumo hoje, e justamente por isso a chamada
    # fica aqui — o dia em que entrar, ela ja esta no caminho da escrita.
    coletor = _modulo('coletar_por_consulta', os.path.join(AQUI, 'coletar-por-consulta.py'))
    for bloco in banco['consultas']:
        coletor.recontar_resumo(bloco)

    banco['gerado_em'] = HOJE
    with open(BANCO, 'w', encoding='utf-8') as f:
        json.dump(banco, f, ensure_ascii=False, indent=coletor.RECUO_DO_BANCO)
        f.write('\n')
    print('GRAVADO em dados/anuncios-por-consulta.json')
    return 0


# --------------------------------------------------------------- o autoteste
def _mundo(serve=True, imagem=None, motivo='a CDN nao respondeu (HTTP Error 503: Service Unavailable)'):
    return {'item_id': 1, 'titulo': 'Patinete Eletrico Adulto 350W', 'serve': serve,
            'imagem': imagem, 'motivo_sem_imagem': motivo, 'chave_que_achou': 'x'}


def conferir():
    """Os mundos que o dado de hoje NAO tem, fabricados — a 32.5-d.

    Em 19/11/2026 as dez fotos da fila sairam `viva` nos dois instrumentos: o
    ramo que RECUSA nao existe no dado, e ramo sem mundo proprio e exatamente o
    que esta ilha ja pagou duas vezes.
    """
    afirmacoes = 0
    falhas = []

    def diz(nome, deu, esperado):
        nonlocal afirmacoes
        afirmacoes += 1
        if deu != esperado:
            falhas.append('%s: esperava %r, deu %r' % (nome, esperado, deu))

    # --- a fila
    diz('anuncio que serve, sem foto, com causa de medicao ENTRA',
        remediavel(_mundo())[0], True)
    diz('anuncio que NAO serve fica fora',
        remediavel(_mundo(serve=False, motivo='anuncio recusado: foto nao e medida para quem nao serve'))[0], False)
    diz('anuncio que JA tem foto fica fora',
        remediavel(_mundo(imagem={'url': 'u', 'largura': 8, 'altura': 8}))[0], False)
    diz('anuncio sem foto e SEM causa fica fora, e a causa disso e defeito de banco',
        remediavel(_mundo(motivo=''))[0], False)
    diz('anuncio que SERVE carregando a causa de quem nao serve fica fora',
        remediavel(_mundo(motivo='anuncio recusado: foto nao e medida para quem nao serve'))[0], False)
    diz('o 403 de "foto NAO MEDIDA" ENTRA na fila: nao medir nao e medir ausente',
        remediavel(_mundo(motivo='foto NAO MEDIDA: HTTP Error 403: Forbidden — e ele tem dois pais'))[0], True)
    diz('"os primeiros bytes nao traziam cabecalho" ENTRA: tambem e medicao, e pode vencer',
        remediavel(_mundo(motivo='os primeiros 32768 bytes nao traziam cabecalho de JPEG, PNG nem WebP'))[0], True)

    # --- os dois instrumentos
    vivo = {'desfecho': 'viva', 'largura': 800, 'altura': 800, 'status_http': 200,
            'como_foi_medido': 'DOM'}
    diz('os dois vivos e de acordo: a foto VOLTA',
        concordam((800, 800), vivo)[0], True)
    diz('cabecalho nao medido: NAO volta, nem com o DOM vivo',
        concordam(None, vivo)[0], False)
    diz('o navegador sem laudo para a URL: NAO volta',
        concordam((800, 800), None)[0], False)
    diz('DOM diz `quebrada`: NAO volta, e e o caso que um instrumento so erraria',
        concordam((800, 800), {'desfecho': 'quebrada', 'status_http': 200,
                               'largura': None, 'altura': None})[0], False)
    diz('DOM diz `nao_medida`: NAO volta — ausencia de medicao nao autoriza nada',
        concordam((800, 800), {'desfecho': 'nao_medida', 'status_http': None,
                               'largura': None, 'altura': None})[0], False)
    diz('DOM diz `rede_nao_explica`: NAO volta',
        concordam((800, 800), {'desfecho': 'rede_nao_explica', 'status_http': None,
                               'largura': None, 'altura': None})[0], False)
    diz('dimensao discordando entre os dois: NAO volta, e nao se escolhe a mais simpatica',
        concordam((800, 800), dict(vivo, largura=1024, altura=1024))[0], False)

    # A MUTACAO COBRADA: a regua de UM INSTRUMENTO SO — "o cabecalho mediu, logo
    # a foto volta" — e a que a coleta usa desde 29/10, e e ela que devolveria a
    # foto que a ronda de 18/11 mediu com `naturalWidth: 0`. Estes dois mundos
    # sao os que a separam da regua de hoje.
    ingenua = lambda cab, _dom: bool(cab)                                   # noqa: E731
    quebrada = {'desfecho': 'quebrada', 'status_http': 200, 'largura': None, 'altura': None}
    afirmacoes += 1
    if not (ingenua((800, 800), quebrada) and not concordam((800, 800), quebrada)[0]):
        falhas.append('a regua de um instrumento so NAO discorda da de hoje na foto quebrada: '
                      'o autoteste nao esta medindo nada')
    afirmacoes += 1
    if not (ingenua((800, 800), dict(vivo, largura=1024, altura=1024))
            and not concordam((800, 800), dict(vivo, largura=1024, altura=1024))[0]):
        falhas.append('a regua de um instrumento so NAO discorda da de hoje na dimensao divergente')

    # --- a forma do que e gravado
    foto = foto_nova('https://cf.shopee.com.br/file/abc', (800, 800), 'Patinete Eletrico Adulto', vivo)
    campos_do_coletor = ['url', 'largura', 'altura', 'alt', 'fonte', 'coletado_em',
                         'como_a_dimensao_foi_medida']
    diz('o objeto `imagem` tem os campos do coletor, na ordem dele',
        list(foto)[:len(campos_do_coletor)], campos_do_coletor)
    diz('e nomeia os DOIS instrumentos e o ambiente',
        'medir_foto' in foto['medida_por'] and 'DOM' in foto['medida_por']
        and AMBIENTE in foto['medida_por'], True)
    diz('a dimensao gravada e a MEDIDA, nunca digitada',
        (foto['largura'], foto['altura']), (800, 800))

    # A FUNCAO QUE MONTA O `alt` TEM DE EXISTIR, e esta afirmacao e a licao da
    # tela branca da F3: nome derivado de cabeca passa em `php -l` e em
    # `python -c 'import'`, e morre na primeira passada que GRAVA.
    rel = _relevancia()
    diz('`nome_do_anuncio` existe no modulo que o coletor carrega',
        callable(getattr(rel, 'nome_do_anuncio', None)), True)
    diz('e ela devolve o mesmo nome que o coletor gravaria',
        rel.nome_do_anuncio('Patinete Eletrico Adulto 350W 36V | Dobravel'),
        rel.nome_do_anuncio('Patinete Eletrico Adulto 350W 36V | Dobravel'))

    a = _mundo()
    historico = arquivar_medicao(a, a['motivo_sem_imagem'])
    diz('a medicao que tirou a foto DESCE para o historico e nao e apagada',
        historico[0]['saiu_do_ar_por'], a['motivo_sem_imagem'])
    diz('o historico acumula, nunca substitui',
        len(arquivar_medicao(a, 'outra medicao')), 2)

    # --- o banco de verdade, lido e nao suposto
    banco = json.load(open(BANCO, encoding='utf-8'))
    na_fila = [(b['id'], x['item_id']) for b in banco['consultas']
               for x in b['anuncios'] if remediavel(x)[0]]
    com_foto = [x for b in banco['consultas'] for x in b['anuncios']
                if x.get('serve') and x.get('imagem')]
    afirmacoes += 1
    print('\nNO BANCO DE HOJE: %d anuncio(s) que servem COM foto, %d na fila de remedicao.'
          % (len(com_foto), len(na_fila)))
    for ident in na_fila:
        print('   fila: %s / %s' % ident)
    # Nenhum anuncio pode estar nos dois lugares: a fila e o complemento exato
    # de quem tem foto, entre os que servem.
    servem = [x for b in banco['consultas'] for x in b['anuncios'] if x.get('serve')]
    if len(com_foto) + len(na_fila) != len(servem):
        falhas.append('quem serve nao se divide em "com foto" + "na fila": %d + %d != %d. '
                      'Sobra anuncio que serve, sem foto e com causa de quem nao serve.'
                      % (len(com_foto), len(na_fila), len(servem)))

    for f in falhas:
        print('FALHA: ' + f)
    print('\n%d afirmacao(oes), %d falha(s).' % (afirmacoes, len(falhas)))
    print('APROVADO' if not falhas else 'REPROVADO')
    return 1 if falhas else 0


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--conferir', action='store_true', help='autoteste, sem rede')
    p.add_argument('--gravar', action='store_true', help='grava o banco')
    args = p.parse_args()
    if args.conferir:
        return conferir()
    return trabalhar(args.gravar)


if __name__ == '__main__':
    sys.exit(main())
