#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QUEBRA DE PROPOSITO as paginas da secao 30 e cobra que um portao reprove.

    python3 ferramentas/mutacoes-produto.py

Nada e gravado: cada mutacao e aplicada numa COPIA da pasta `dados/` dentro de
um diretorio temporario, o portao roda contra a copia, e a copia e jogada fora.

POR QUE ESTA BATERIA EXISTE
---------------------------
A secao 8 do ARQUIPELAGO.md escreve o motivo em uma frase: "TESTE QUE MEDE A SI
MESMO E UM TESTE VERDE QUE NAO MEDE NADA". A bancada desta ilha fecha verde com
`coletar-por-consulta.py --conferir` e `gerar-vitrine-de-produto.py --conferir`
aprovando; o que nenhuma das duas prova e que elas sabem REPROVAR.

E TODA MUTACAO TEM TRAVA DE ALVO EXATO. Se o texto a mutar nao estiver mais
onde a mutacao o espera, ela PARA a bateria em vez de passar medindo nada —
a cicatriz das 18 de 20 da Robometria, que o contrato chama de mutacao INERTE:
"quando a regua muda de arquivo, toda mutacao que editava o arquivo antigo vira
inerte, e sem a trava cinco mutacoes passam medindo nada e o relatorio diz
`0 sobrevivente`".

OS MUNDOS QUE O BANCO DE HOJE NAO PRODUZ ESTAO AQUI FABRICADOS: foto sem
dimensao, pagina abaixo do piso de tres, carrossel acima do teto de cinco. A
secao 8 e explicita em que regua escrita para um mundo que nunca aconteceu
"nasce errada sem poder falhar".
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FERRAMENTAS = os.path.join(RAIZ, 'ferramentas')

COLETOR = 'coletar-por-consulta.py'
GERADOR = 'gerar-vitrine-de-produto.py'
RELEVANCIA = 'teste-relevancia-do-anuncio.py'

ANUNCIOS = 'anuncios-por-consulta.json'
VITRINE = 'vitrine-de-produto.json'
EDITORIAL = 'paginas-de-produto.json'
DECLARACAO = 'consultas-de-produto.json'


class Inerte(Exception):
    """O alvo da mutacao nao esta mais la. Para a bateria."""


def exigir(condicao, o_que):
    if not condicao:
        raise Inerte(o_que)


# ---------------------------------------------------------------------------
# A BANCADA DE AREIA
# ---------------------------------------------------------------------------
def montar_areia():
    """Uma copia da ilha com `dados/` e `ferramentas/` reais, para mutar `dados/`."""
    areia = tempfile.mkdtemp(prefix='rdm-mut-')
    shutil.copytree(os.path.join(RAIZ, 'dados'), os.path.join(areia, 'dados'))
    shutil.copytree(FERRAMENTAS, os.path.join(areia, 'ferramentas'))
    return areia


def rodar(areia, ferramenta, *argumentos):
    """(codigo, saida). A ferramenta roda DE DENTRO da areia, nunca da ilha."""
    r = subprocess.run(
        [sys.executable, os.path.join(areia, 'ferramentas', ferramenta)] + list(argumentos),
        capture_output=True, text=True, timeout=300)
    return r.returncode, (r.stdout or '') + (r.stderr or '')


def ler(areia, nome):
    with open(os.path.join(areia, 'dados', nome), encoding='utf-8') as f:
        return json.load(f)


def escrever(areia, nome, d):
    with open(os.path.join(areia, 'dados', nome), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)


def primeiro_que_serve(banco, id_consulta='patinete-eletrico'):
    bloco = next(b for b in banco['consultas'] if b['id'] == id_consulta)
    anuncio = next(a for a in bloco['anuncios'] if a['serve'])
    return bloco, anuncio


# ---------------------------------------------------------------------------
# AS MUTACOES. Cada uma: (nome, ferramenta, argumentos, funcao que muta)
# ---------------------------------------------------------------------------
def m_veredito_trocado(areia):
    b = ler(areia, ANUNCIOS)
    _, a = primeiro_que_serve(b)
    exigir(a['serve'] is True and a['recusado_por'] is None,
           'o primeiro anuncio que serve deveria servir e ter recusado_por nulo')
    a['serve'] = False
    a['recusado_por'] = 'acessorio'
    escrever(areia, ANUNCIOS, b)


def m_numero_proprio_mexido(areia):
    b = ler(areia, ANUNCIOS)
    bloco, _ = primeiro_que_serve(b)
    n = bloco['resumo']['numero_proprio']
    exigir(isinstance(n, dict) and 'de' in n, 'o resumo deveria ter numero_proprio com `de`')
    n['de'] = round(n['de'] - 100, 2)
    escrever(areia, ANUNCIOS, b)


def m_rotulo_de_potencia_mexido(areia):
    b = ler(areia, ANUNCIOS)
    _, a = primeiro_que_serve(b)
    exigir(a['rotulo_de_potencia'] != 'nominal',
           'o primeiro anuncio que serve nao deveria declarar watt nominal')
    a['rotulo_de_potencia'] = 'nominal'
    escrever(areia, ANUNCIOS, b)


def m_link_de_afiliado_apagado(areia):
    b = ler(areia, ANUNCIOS)
    _, a = primeiro_que_serve(b)
    exigir(bool(a.get('url_afiliado')), 'o primeiro anuncio que serve deveria ter link')
    a['url_afiliado'] = None
    escrever(areia, ANUNCIOS, b)


def m_sub_id_apagado(areia):
    b = ler(areia, ANUNCIOS)
    _, a = primeiro_que_serve(b)
    exigir(bool(a.get('sub_id_2')), 'o primeiro anuncio que serve deveria ter sub_id_2')
    a['sub_id_2'] = None
    escrever(areia, ANUNCIOS, b)


def m_foto_sem_dimensao(areia):
    """MUNDO FABRICADO: o banco de hoje tem as 21 fotos medidas."""
    b = ler(areia, ANUNCIOS)
    _, a = primeiro_que_serve(b)
    exigir(isinstance(a.get('imagem'), dict) and a['imagem'].get('largura'),
           'o primeiro anuncio que serve deveria ter imagem com largura medida')
    a['imagem']['largura'] = None
    escrever(areia, ANUNCIOS, b)


def m_foto_ausente_sem_causa(areia):
    """MUNDO FABRICADO: foto que nao foi medida e nao diz por que."""
    b = ler(areia, ANUNCIOS)
    _, a = primeiro_que_serve(b)
    exigir('motivo_sem_imagem' in a, 'o anuncio deveria ter o campo motivo_sem_imagem')
    a['imagem'] = None
    a['motivo_sem_imagem'] = ''
    escrever(areia, ANUNCIOS, b)


def m_chave_do_anuncio_trocada(areia):
    b = ler(areia, ANUNCIOS)
    bloco, a = primeiro_que_serve(b)
    exigir(a['chave_que_achou'] == bloco['chave_escolhida'],
           'o anuncio deveria ter sido achado pela chave escolhida')
    a['chave_que_achou'] = 'outra palavra qualquer'
    escrever(areia, ANUNCIOS, b)


def m_chave_fora_da_escada(areia):
    b = ler(areia, ANUNCIOS)
    bloco, _ = primeiro_que_serve(b)
    exigir(bool(bloco['chave_escolhida']), 'o bloco deveria ter chave escolhida')
    bloco['chave_escolhida'] = 'patinete voador'
    for a in bloco['anuncios']:
        a['chave_que_achou'] = 'patinete voador'
    escrever(areia, ANUNCIOS, b)


def m_consulta_sem_motivo_para_nao_publicar(areia):
    d = ler(areia, DECLARACAO)
    c = next(c for c in d['consultas'] if not c.get('publicar_declarado'))
    exigir(bool((c.get('motivo_para_nao_publicar_agora') or '').strip()),
           'a consulta que nao publica deveria dizer por que')
    c['motivo_para_nao_publicar_agora'] = ''
    escrever(areia, DECLARACAO, d)


def m_consulta_promete_pagina_sem_coleta(areia):
    d = ler(areia, DECLARACAO)
    c = next(c for c in d['consultas'] if not c.get('publicar_declarado'))
    exigir(c['id'] not in [b['id'] for b in ler(areia, ANUNCIOS)['consultas']],
           'a consulta escolhida nao deveria ter sido colhida')
    c['publicar_declarado'] = True
    escrever(areia, DECLARACAO, d)


def m_vitrine_contagem_mexida(areia):
    v = ler(areia, VITRINE)
    p = v['paginas'][0]
    exigir(isinstance(p['numeros']['n'], int), 'a vitrine deveria ter `n` inteiro')
    p['numeros']['n'] += 1
    escrever(areia, VITRINE, v)


def m_vitrine_preco_mexido(areia):
    v = ler(areia, VITRINE)
    p = v['paginas'][0]
    exigir(p['linhas'][0]['preco'].startswith('R$'), 'a linha deveria ter preco em reais')
    p['linhas'][0]['preco'] = 'R$ 1,00'
    escrever(areia, VITRINE, v)


def m_vitrine_preco_sem_data(areia):
    v = ler(areia, VITRINE)
    p = v['paginas'][0]
    exigir('preço de' in p['linhas'][0]['preco_nota'],
           'a linha deveria trazer a data da coleta ao lado do preco')
    p['linhas'][0]['preco_nota'] = ''
    escrever(areia, VITRINE, v)


def m_vitrine_url_insegura(areia):
    v = ler(areia, VITRINE)
    p = v['paginas'][0]
    exigir(p['linhas'][0]['url'].startswith('https://'), 'a linha deveria ter url https')
    p['linhas'][0]['url'] = p['linhas'][0]['url'].replace('https://', 'http://', 1)
    escrever(areia, VITRINE, v)


def m_carrossel_acima_do_teto(areia):
    """MUNDO FABRICADO: o gerador nunca escreve mais de cinco."""
    v = ler(areia, VITRINE)
    p = v['paginas'][0]
    exigir(len(p['cartoes']) == v['teto_do_carrossel'],
           'o carrossel desta pagina deveria estar exatamente no teto')
    p['cartoes'] = p['cartoes'] + [p['cartoes'][0]]
    escrever(areia, VITRINE, v)


def m_pagina_abaixo_do_piso(areia):
    """MUNDO FABRICADO: as duas paginas de hoje tem cinco e dezesseis linhas."""
    v = ler(areia, VITRINE)
    p = v['paginas'][0]
    exigir(len(p['linhas']) > v['piso_da_30_2'],
           'a pagina deveria ter mais linhas que o piso')
    p['linhas'] = p['linhas'][:2]
    escrever(areia, VITRINE, v)


def m_ordem_do_carrossel_trocada(areia):
    v = ler(areia, VITRINE)
    p = v['paginas'][0]
    exigir(len(p['cartoes']) >= 2, 'o carrossel deveria ter dois cartoes ou mais')
    p['cartoes'][0], p['cartoes'][1] = p['cartoes'][1], p['cartoes'][0]
    escrever(areia, VITRINE, v)


def m_editorial_com_preco_digitado(areia):
    d = ler(areia, EDITORIAL)
    p = d['paginas'][0]
    exigir(isinstance(p['resposta'], list) and p['resposta'],
           'a pagina deveria ter resposta em lista')
    p['resposta'][0] = 'Custa R$ 1.299,00 e pronto.'
    escrever(areia, EDITORIAL, d)


def m_editorial_com_contagem_digitada(areia):
    d = ler(areia, EDITORIAL)
    p = d['paginas'][0]
    exigir('{N}' in ' '.join(p['resposta']), 'a resposta deveria usar o molde {N}')
    p['resposta'][0] = p['resposta'][0].replace('{N}', '16')
    escrever(areia, EDITORIAL, d)


def m_editorial_com_numero_na_pergunta(areia):
    """A TRAVA DA PROPRIA TRAVA: a primeira versao da regua lia string e lista de
    string, e as perguntas frequentes sao lista de DICIONARIO — ela passava por
    cima de toda pergunta sem dizer que nao as leu."""
    d = ler(areia, EDITORIAL)
    p = d['paginas'][0]
    exigir(isinstance(p['perguntas'], list) and isinstance(p['perguntas'][0], dict),
           'as perguntas deveriam ser uma lista de dicionarios')
    p['perguntas'][0]['resposta'] = 'São 16 anúncios, e 15 declaram watt.'
    escrever(areia, EDITORIAL, d)


def m_editorial_com_numero_na_mae(areia):
    d = ler(areia, EDITORIAL)
    exigir('resposta' in d['mae'], 'a mae deveria ter resposta')
    d['mae']['resposta'][0] = 'São 2 famílias com página hoje.'
    escrever(areia, EDITORIAL, d)


def m_relevancia_sem_a_regra_da_posicao(areia):
    caminho = os.path.join(areia, 'ferramentas', RELEVANCIA)
    with open(caminho, encoding='utf-8') as f:
        t = f.read()
    alvo = "POR_POSICAO = ('acessorio',)"
    exigir(alvo in t, 'a regua deveria declarar POR_POSICAO com `acessorio`')
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(t.replace(alvo, 'POR_POSICAO = ()'))


def m_relevancia_sem_o_grupo_do_brinquedo(areia):
    caminho = os.path.join(areia, 'ferramentas', RELEVANCIA)
    with open(caminho, encoding='utf-8') as f:
        t = f.read()
    alvo = "    ('brinquedo', ("
    exigir(alvo in t, 'a regua deveria ter o grupo `brinquedo`')
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(t.replace(alvo, "    ('brinquedo_desligado', (", 1))


def m_relevancia_sem_o_prefixo_da_bicicleta(areia):
    caminho = os.path.join(areia, 'ferramentas', RELEVANCIA)
    with open(caminho, encoding='utf-8') as f:
        t = f.read()
    alvo = "PREFIXOS = ('eletric', 'adulto', 'bicicleta', 'patinete')"
    exigir(alvo in t, 'a regua deveria declarar os quatro prefixos')
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(t.replace(alvo, "PREFIXOS = ('eletric', 'adulto', 'patinete')"))


def m_relevancia_sem_o_qualificador(areia):
    caminho = os.path.join(areia, 'ferramentas', RELEVANCIA)
    with open(caminho, encoding='utf-8') as f:
        t = f.read()
    alvo = "QUALIFICADOR_ADULTO = ('adulto', 'adultos')"
    exigir(alvo in t, 'a regua deveria declarar o qualificador de adulto')
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(t.replace(alvo, "QUALIFICADOR_ADULTO = ()"))


MUTACOES = (
    ('veredito de um anuncio trocado', COLETOR, ('--conferir',), m_veredito_trocado),
    ('numero proprio mexido no resumo', COLETOR, ('--conferir',), m_numero_proprio_mexido),
    ('rotulo de potencia mexido', COLETOR, ('--conferir',), m_rotulo_de_potencia_mexido),
    ('link de afiliado apagado', COLETOR, ('--conferir',), m_link_de_afiliado_apagado),
    ('sub-id 2 apagado do link', COLETOR, ('--conferir',), m_sub_id_apagado),
    ('foto sem dimensao medida [mundo fabricado]', COLETOR, ('--conferir',), m_foto_sem_dimensao),
    ('foto ausente sem causa escrita [mundo fabricado]', COLETOR, ('--conferir',),
     m_foto_ausente_sem_causa),
    ('chave do anuncio diferente da escolhida', COLETOR, ('--conferir',),
     m_chave_do_anuncio_trocada),
    ('chave escolhida fora da escada declarada', COLETOR, ('--conferir',), m_chave_fora_da_escada),
    ('consulta que nao publica e nao diz por que', COLETOR, ('--conferir',),
     m_consulta_sem_motivo_para_nao_publicar),
    ('consulta que promete pagina sem coleta', COLETOR, ('--conferir',),
     m_consulta_promete_pagina_sem_coleta),
    ('contagem da vitrine mexida', GERADOR, ('--conferir',), m_vitrine_contagem_mexida),
    ('preco da tabela mexido', GERADOR, ('--conferir',), m_vitrine_preco_mexido),
    ('preco sem a data da coleta', GERADOR, ('--conferir',), m_vitrine_preco_sem_data),
    ('link da tabela sem https', GERADOR, ('--conferir',), m_vitrine_url_insegura),
    ('carrossel acima do teto de cinco [mundo fabricado]', GERADOR, ('--conferir',),
     m_carrossel_acima_do_teto),
    ('pagina abaixo do piso de tres [mundo fabricado]', GERADOR, ('--conferir',),
     m_pagina_abaixo_do_piso),
    ('ordem do carrossel trocada', GERADOR, ('--conferir',), m_ordem_do_carrossel_trocada),
    ('preco digitado na prosa declarada', GERADOR, ('--conferir',),
     m_editorial_com_preco_digitado),
    ('contagem digitada no lugar do molde', GERADOR, ('--conferir',),
     m_editorial_com_contagem_digitada),
    ('numero digitado dentro da pergunta frequente', GERADOR, ('--conferir',),
     m_editorial_com_numero_na_pergunta),
    ('numero digitado na prosa da mae', GERADOR, ('--conferir',), m_editorial_com_numero_na_mae),
    ('regua sem a regra da posicao', RELEVANCIA, (),
     m_relevancia_sem_a_regra_da_posicao),
    ('regua sem o grupo do brinquedo', RELEVANCIA, (),
     m_relevancia_sem_o_grupo_do_brinquedo),
    ('regua sem o prefixo da bicicleta', RELEVANCIA, (),
     m_relevancia_sem_o_prefixo_da_bicicleta),
    ('regua sem o qualificador de adulto', RELEVANCIA, (),
     m_relevancia_sem_o_qualificador),
)


def main():
    # PRIMEIRO O MUNDO LIMPO: os portoes tem de APROVAR antes de alguem cobrar
    # que eles reprovem. Portao que reprova tudo nao mede nada.
    areia = montar_areia()
    try:
        for ferramenta, args in ((COLETOR, ('--conferir',)), (GERADOR, ('--conferir',)),
                                 (RELEVANCIA, ())):
            cod, saida = rodar(areia, ferramenta, *args)
            if cod != 0:
                print('PARADO: %s reprova o mundo LIMPO — nao ha o que mutar.\n%s'
                      % (ferramenta, saida[-800:]))
                return 1
        print('mundo limpo: os tres portoes aprovam.\n')
    finally:
        shutil.rmtree(areia, ignore_errors=True)

    sobreviventes, inertes = [], []
    for nome, ferramenta, args, mutar in MUTACOES:
        areia = montar_areia()
        try:
            try:
                mutar(areia)
            except Inerte as erro:
                inertes.append((nome, str(erro)))
                print('INERTE  %-52s %s' % (nome, erro))
                continue
            cod, saida = rodar(areia, ferramenta, *args)
            if cod == 0:
                sobreviventes.append(nome)
                print('SOBREVIVEU  %-48s (%s aprovou)' % (nome, ferramenta))
            else:
                print('reprovada   %-48s (%s)' % (nome, ferramenta))
        finally:
            shutil.rmtree(areia, ignore_errors=True)

    print('\n%d mutacao(oes): %d reprovada(s), %d sobrevivente(s), %d inerte(s).'
          % (len(MUTACOES), len(MUTACOES) - len(sobreviventes) - len(inertes),
             len(sobreviventes), len(inertes)))
    if inertes:
        print('INERTE e pior que sobrevivente: a mutacao nao mediu nada e o alvo dela mudou.')
    print('APROVADO' if not sobreviventes and not inertes else 'REPROVADO')

    return 1 if (sobreviventes or inertes) else 0


if __name__ == '__main__':
    sys.exit(main())
