#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A data de publicacao e a data de modificacao de cada pagina que as declara.

    python3 ferramentas/gerar-datas-das-paginas.py            # mostra
    python3 ferramentas/gerar-datas-das-paginas.py --gravar   # grava

O DEFEITO QUE ELE FECHA — item 4 do despacho da Sentinela de 16/09/2026
------------------------------------------------------------------------
Medido no JSON-LD servido as 14h50Z de 16/09/2026: os dois artigos publicavam
`dateModified: 2026-09-13` e as duas paginas tinham mudado em 16/09, na revisao
52 — o bloco de compra passou a sair por link encurtado com `rel="sponsored"` e
as contas da divulgacao mudaram. O campo estava atras do que o leitor e o Google
recebiam. E `/quantos-m2-.../` nao publicava `datePublished` nenhum.

`dateModified` esta na lista da 19.1 e a Sentinela consertaria — mas a ORIGEM do
campo o tirou de la, e a analise dela e o ponto de partida deste arquivo: ele era
derivado de `gerado_em` dos arquivos `dados/a1-fatos.json` e `dados/a2-fatos.json`,
que significam *a data em que os FATOS foram gerados*. Carimbar 16/09 ali seria
mentir sobre a geracao dos fatos para acertar a data da pagina.

DE QUAL CAMPO ELE PASSA A SAIR, E POR QUE NAO DOS OUTROS DOIS
--------------------------------------------------------------
O despacho deixou a escolha aberta entre tres: a geracao dos fatos, a revisao do
manifest, ou um campo novo. E um campo novo, e a razao e que os outros dois nao
sabem responder a pergunta que o campo faz.

  . A GERACAO DOS FATOS mede outra coisa, e ja esta escrito acima. Alem disso ela
    e cega para metade do que a pagina serve: a revisao 52 nao regerou fato
    nenhum, mexeu na CASCA.
  . A REVISAO DO MANIFEST e da ILHA INTEIRA. Ela sobe quando qualquer arquivo de
    qualquer pagina muda — entao `dateModified` do artigo do filtro se mexeria
    porque a ferramenta R2 ganhou uma linha. Data que se mexe sem a pagina ter
    mudado e ruido, e ruido num campo que o Google usa para decidir se vale
    reindexar e pior que campo velho: ensina a ignorar o campo.
  . O CAMPO NOVO responde a pergunta certa — *quando o HTML desta pagina mudou
    pela ultima vez* — e a resposta nao e opiniavel: e a data do commit mais
    recente entre os arquivos que compoem a pagina. Medida do git, nunca digitada.

O CONJUNTO DE ARQUIVOS DE CADA PAGINA INCLUI A CASCA, E ISSO E DECISAO
-----------------------------------------------------------------------
A casca nao e enfeite em volta: ela escreve a cabeca, a trilha, o painel da foto e
o bloco de compra que o leitor ve DENTRO do artigo — foi exatamente uma mudanca de
casca que deixou o campo atrasado em 16/09. Entao mudanca de casca muda o HTML
servido, e dizer o contrario seria escolher uma definicao de "mudou" que faz o
numero ficar bonito. O preco esta na mesa: a casca muda com frequencia, e o
`dateModified` das duas paginas vai andar junto com ela. Em troca, o campo nunca
afirma que a pagina esta parada quando ela nao esta — que e a direcao em que errar
custa menos (secao 10).

`modificado_por` grava QUAL arquivo deu a data. Sem isso, o dia em que alguem
achar que a casca nao deveria contar nao teria como medir quanto ela pesa.

E `datePublished` NAO SAI DO GIT, e a razao e medida
-----------------------------------------------------
O historico do `main` deste repositorio foi reescrito: `git log --reverse` diz que
TODOS os arquivos desta ilha nasceram em 15/09/2026, inclusive os que estao no ar
desde 10/09. Data de nascimento lida dali seria falsa nas duas paginas. Entao ela
e DECLARADA aqui, com a entrada do `REGISTRO.md` que a sustenta citada ao lado —
que e a mesma exigencia que o banco faz de todo numero: o valor vem com a fonte.
"""
import argparse
import json
import os
import subprocess
import sys
from datetime import date

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# A raiz do REPOSITORIO, que e de onde o git tem de ser chamado: caminho passado
# a `git log` e relativo ao diretorio de trabalho, e rodar de dentro da pasta da
# ilha faria `ilhas/robometria/...` nao existir para ele — o git responderia
# vazio, sem erro, e a ferramenta leria "arquivo sem commit" onde ha historia.
RAIZ_REPO = os.path.dirname(os.path.dirname(RAIZ))
PREFIXO = os.path.relpath(RAIZ, RAIZ_REPO)
SAIDA = 'dados/datas-das-paginas.json'

CASCA = 'snippets/robometria-casca.php'

# A CASCA ENTRA NO CONJUNTO DE TODA PAGINA. Escrita uma vez, aqui, para pagina
# nova nao nascer sem ela por esquecimento.
PAGINAS = {
    'filtro-universal-de-robo-aspirador': {
        'titulo': 'Existe filtro universal de robo aspirador?',
        'publicada_em': '2026-09-10',
        'fonte_da_publicacao': (
            'REGISTRO.md, entrada "2026-09-10 21h15Z — Bloco 5: o ARTIGO-ANCORA da '
            'R1 existe, e a malha da ilha fechou" — snippet robometria-a1.php v1.0.0, '
            'manifest revisao 12 conferida no /status'),
        'arquivos': ['snippets/robometria-a1.php', 'dados/a1-fatos.json', CASCA],
    },
    'quantos-m2-o-robo-aspirador-limpa-por-carga': {
        'titulo': 'Quantos m2 o robo aspirador limpa por carga?',
        'publicada_em': '2026-09-11',
        'fonte_da_publicacao': (
            'REGISTRO.md, entrada "2026-09-11 (00h07Z) — Bloco 5: o ARTIGO-ANCORA da '
            'R2, e o acento que faltava no A1" — snippet robometria-a2.php v1.0.0, '
            'manifest revisao 13 conferida no /status'),
        'arquivos': ['snippets/robometria-a2.php', 'dados/a2-fatos.json', CASCA],
    },
}


MALHA = 'snippets/robometria-malha.php'
FATOS_MALHA = 'dados/malha-pecas.json'
FONTE_MALHA = (
    'REGISTRO.md, entrada "2026-09-21 — Bloco 5b: a primeira leva de malha, '
    '/pecas/ e /pecas/filtros/ com as tres filhas" — snippet '
    'robometria-malha.php v1.0.0, revisao do manifest conferida no /status')

# AS CINCO PAGINAS DA MALHA. O conjunto de arquivos de cada uma e o mesmo, e
# isso e correto e nao preguica: as cinco sao montadas pelo mesmo snippet, com
# os mesmos fatos, dentro da mesma casca. Mudar qualquer um dos tres muda o HTML
# servido das cinco.
for _slug, _titulo in (
        ('pecas', 'Pecas de reposicao de robo aspirador'),
        ('pecas-filtros', 'Filtro de robo aspirador: qual serve no seu'),
        ('pecas-filtros-xiaomi', 'Filtro de robo aspirador Xiaomi'),
        ('pecas-filtros-wap', 'Filtro de robo aspirador WAP'),
        ('pecas-filtros-electrolux', 'Filtro de robo aspirador Electrolux')):
    PAGINAS[_slug] = {
        'titulo': _titulo,
        'publicada_em': '2026-09-21',
        'fonte_da_publicacao': FONTE_MALHA,
        'arquivos': [MALHA, FATOS_MALHA, CASCA],
    }


def _git(args):
    saida = subprocess.run(['git'] + args, capture_output=True, text=True,
                           cwd=RAIZ_REPO)
    if saida.returncode != 0:
        raise SystemExit('git %s falhou: %s' % (' '.join(args), saida.stderr.strip()))
    return saida.stdout.strip()


def data_do_arquivo(rel, hoje):
    """A data em que este arquivo mudou pela ultima vez.

    Arquivo com mudanca NAO COMMITADA vale HOJE. Sem isto a ferramenta rodada no
    meio de um bloco carimbaria a data do commit anterior e o `dateModified`
    nasceria um dia atrasado no mesmo instante em que foi gerado — que e
    exatamente o defeito que ela existe para fechar, so que mais rapido.
    """
    caminho = os.path.join(PREFIXO, rel)
    sujo = _git(['status', '--porcelain', '--', caminho])
    if sujo:
        return hoje, 'nao commitado'
    data = _git(['log', '-1', '--format=%cd', '--date=short', '--', caminho])
    if not data:
        raise SystemExit('%s nao tem commit nenhum e nao esta modificado — o git nao '
                         'sabe deste arquivo' % rel)
    return data, 'commit'


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--gravar', action='store_true')
    args = p.parse_args()

    hoje = date.today().isoformat()
    registros = []
    for slug, cfg in PAGINAS.items():
        por_arquivo = {}
        for rel in cfg['arquivos']:
            if not os.path.exists(os.path.join(RAIZ, rel)):
                raise SystemExit('%s: %s nao existe. Conjunto de arquivos de pagina '
                                 'que aponta para arquivo inexistente mede o vazio'
                                 % (slug, rel))
            data, como = data_do_arquivo(rel, hoje)
            por_arquivo[rel] = {'data': data, 'como': como}
        modificado_em = max(v['data'] for v in por_arquivo.values())
        modificado_por = sorted(k for k, v in por_arquivo.items()
                                if v['data'] == modificado_em)
        if modificado_em < cfg['publicada_em']:
            raise SystemExit('%s: modificado_em %s e anterior a publicada_em %s. A '
                             'pagina nao pode ter mudado antes de existir — provavel '
                             'historia reescrita no git' % (slug, modificado_em,
                                                            cfg['publicada_em']))
        registros.append({
            'slug': slug,
            'titulo': cfg['titulo'],
            'publicada_em': cfg['publicada_em'],
            'fonte_da_publicacao': cfg['fonte_da_publicacao'],
            'modificada_em': modificado_em,
            'modificada_por': modificado_por,
            'arquivos': por_arquivo,
        })
        print('%-46s publicada %s   modificada %s  (%s)'
              % (slug[:46], cfg['publicada_em'], modificado_em,
                 ', '.join(os.path.basename(a) for a in modificado_por)))

    doc = {
        'id': 'datas-das-paginas',
        'ilha': 'robometria',
        'entidade': 'medicao',
        'gerado_por': 'ferramentas/gerar-datas-das-paginas.py',
        'gerado_em': hoje,
        'o_que_e': (
            'A data de publicacao e a data da ultima modificacao de cada pagina que '
            'publica as duas no JSON-LD. `modificada_em` e MEDIDA do git, sobre os '
            'arquivos que compoem a pagina; `publicada_em` e DECLARADA, com a entrada '
            'do REGISTRO.md que a sustenta, porque o historico do main foi reescrito e '
            'o git diz que todos os arquivos nasceram em 15/09/2026.'),
        'por_que_nao_sai_de_gerado_em': (
            '`gerado_em` de a1-fatos.json e a2-fatos.json significa a data em que os '
            'FATOS foram gerados. Carimbar ali a data da pagina seria mentir sobre a '
            'geracao dos fatos para acertar outra coisa — e a revisao 52, que foi o '
            'que deixou o campo atrasado, nao regerou fato nenhum: mexeu na casca.'),
        'registros': registros,
    }

    if args.gravar:
        with open(os.path.join(RAIZ, SAIDA), 'w', encoding='utf-8') as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=1)
            fh.write('\n')
        print('\ngravado: %s' % SAIDA)
    return 0


if __name__ == '__main__':
    sys.exit(main())
