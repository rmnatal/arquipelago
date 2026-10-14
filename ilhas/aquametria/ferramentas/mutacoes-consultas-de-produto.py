#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MUTACOES do portao das consultas de produto. BANCADA: sem rede.

Portao que fica verde na primeira passada nao provou nada — provou que o dado de
hoje passa. Este arquivo quebra o dado DE PROPOSITO, uma quebra por vez, e cobra
que a regua fique vermelha pelo MOTIVO CERTO: cada mutacao declara um pedaco da
mensagem que espera. Mutacao pega pela mensagem errada e mutacao INERTE, e inerte
conta como falha aqui.

As mutacoes chamam `regua.erros_do_arquivo`, que e exatamente a funcao que o
`validar-consultas-de-produto.py` chama — regra que o portao tem e a mutacao nao
ve e regra que nunca foi medida.

O `.md` sai do caminho nas mutacoes de DADO (`md_no_disco=None`), porque quase
toda mutacao muda o texto gerado e deixar a regra ligada esconderia a causa
verdadeira atras de "difere do que a regua gera". A regra do `.md` tem mutacao
propria, a ultima.

    python3 ferramentas/mutacoes-consultas-de-produto.py
"""
import copy
import importlib.util
import json
import os
import sys

PASTA = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(PASTA)
JSON = os.path.join(RAIZ, 'dados', 'consultas-de-produto.json')
DADOS = os.path.join(RAIZ, 'dados')


def carregar(nome):
    caminho = os.path.join(PASTA, nome)
    spec = importlib.util.spec_from_file_location(nome.replace('-', '_')[:-3], caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def linha(dados, id_):
    for c in dados['consultas']:
        if c['id'] == id_:
            return c
    raise SystemExit('nenhuma consulta com id %r — mutacao nao pode ser montada' % id_)


def mutacoes():
    # 1. A PORTA DOS FUNDOS MAIS CARA: promover ficha de produto unico de varejo
    #    grande a "pagina dedicada" transforma 14 linhas nao medidas em tomadas,
    #    ou — pior — deixa o veredito escrito como estava e some com a diferenca.
    #    Esta e a mutacao que prova que a coluna `dedicada_a_consulta` decide algo.
    def promove_ficha_a_dedicada(d):
        for o in linha(d, 'filtro-hang-on-para-aquario')['ocupantes']:
            if o['classe'] == 'varejo-grande':
                o['dedicada_a_consulta'] = True

    # 2. A OUTRA PORTA DOS FUNDOS, na direcao que gasta rastreamento: dizer que a
    #    pagina nasce sem ninguem ter aberto a SERP brasileira.
    def nasce_sem_olhos(d):
        c = linha(d, 'filtro-canister-para-aquario')
        c['nasce_agora'] = True

    # 3. UMA LETRA NO VEREDITO ESCRITO. O veredito e calculado e o escrito e
    #    conferido; sem isso a unica linha que esta ilha pode AFIRMAR viraria
    #    texto solto.
    def afrouxa_o_veredito_afirmado(d):
        linha(d, 'aquecedor-para-aquario')['veredito'] = 'nao-medida'

    # 4. INVENTAR `alvo`. E o veredito que a regua nao tem, e e o que autoriza
    #    abrir URL nova: ele tem de reprovar com o nome dele na mensagem.
    def inventa_alvo(d):
        linha(d, 'luminaria-led-para-aquario-plantado')['veredito'] = 'alvo'

    # 5. CONTRABANDEAR O OCUPANTE DA BUSCA ENVIESADA para a contagem. A busca que
    #    nomeia a Cobasi acha a categoria dedicada da Cobasi; deixar esse
    #    ocupante entrar na lista e fabricar dominancia com a pergunta.
    def contrabandeia_enviesado(d):
        c = linha(d, 'luminaria-led-para-aquario-plantado')
        c['ocupantes'].append({
            'url': 'https://www.cobasi.com.br/c/peixes/equipamentos-e-acessorios/iluminacao',
            'titulo': 'Luminária para aquário você encontra aqui',
            'classe': 'varejo-grande', 'dedicada_a_consulta': True,
            'vinda_da_consulta': 'luminária LED para aquário comprar Cobasi Petz Mercado Livre',
        })

    # 6. APAGAR `enviesada` de uma evidencia. Ausencia nao pode valer como
    #    `false`: se puder, a lista ganha um estado em que ninguem sabe se a
    #    consulta nomeava loja — e e justamente esse estado que a 20.2 paga.
    def apaga_enviesada(d):
        del linha(d, 'luminaria-led-para-aquario-plantado')['evidencia'][1]['enviesada']

    # 7. DECLARAR NEUTRA UMA CONSULTA QUE NOMEIA LOJA. A mentira e detectavel do
    #    proprio texto da consulta, e tem de ser detectada.
    def mente_que_e_neutra(d):
        linha(d, 'luminaria-led-para-aquario-plantado')['evidencia'][1]['enviesada'] = False

    # 8. `dedicada_a_consulta: false`. Busca nao afirma ausencia, e `false` aqui
    #    e exatamente a afirmacao de ausencia disfarcada de campo preenchido.
    def dedicada_false(d):
        linha(d, 'termostato-para-aquario')['ocupantes'][0]['dedicada_a_consulta'] = False

    # 9. OCUPANTE SEM URL. A 30.5 termina dizendo "todo veredito continua escrito
    #    com as URLs do top 10 que o sustentam".
    def apaga_a_url(d):
        del linha(d, 'bomba-submersa-para-aquario')['ocupantes'][0]['url']

    # 10. OCUPANTE ORFAO: colado numa linha sem dizer de que consulta do
    #     instrumento veio. E onde a proxima passada cola URL que ninguem mediu.
    def ocupante_orfao(d):
        c = linha(d, 'teste-de-agua-para-aquario')
        c['ocupantes'].append({'url': 'https://www.cobasi.com.br/c/x', 'titulo': 't',
                               'classe': 'varejo-grande', 'dedicada_a_consulta': True,
                               'vinda_da_consulta': 'uma consulta que ninguem declarou'})

    # 11. INFLAR O LASTRO DE BANCO para furar a 30.2 sem colher anuncio nenhum.
    #     O portao nao recontaria o banco, mas o `nasce_agora` calculado muda —
    #     e e a divergencia com o escrito que acusa.
    def infla_o_banco(d):
        linha(d, 'kit-de-co2-para-aquario-plantado')['produtos_reais_no_banco'] = 9

    # 12. APAGAR A PAGINA QUE JA SERVE A CONSULTA, que e como se canibaliza uma
    #     pagina que ja tem impressao (30.4).
    def apaga_a_30_4(d):
        c = linha(d, 'filtro-para-aquario-de-100-litros')
        c['pagina_da_ilha_que_ja_serve'] = None
        c['serp_vista_por'] = 'alguem'
        c['serp_vista_em'] = '2026-10-14'

    # 13. A INTENCAO DE COMPRA SEM O JUIZO ESCRITO. Ela e juizo, nao medicao, e
    #     juizo sem texto e numero que ninguem pode contestar.
    def intencao_sem_juizo(d):
        del linha(d, 'substrato-fertil-para-aquario-plantado')['por_que_a_intencao']

    # 14. APAGAR A DECLARACAO DO INSTRUMENTO DO CABECALHO. Sem ela o arquivo
    #     parece ter visto a SERP brasileira, e e a frase que diz que nao viu.
    def apaga_o_instrumento(d):
        d['o_instrumento_desta_passada'] = ''

    # 15. APAGAR A LISTA DO QUE NAO FOI MEDIDO. "Nao medido" lido como zero e a
    #     doenca que a secao 4 do contrato nomeia.
    def apaga_o_nao_medido(d):
        del d['o_que_nao_foi_medido']

    return [
        ('1. ficha de produto unico promovida a pagina dedicada', promove_ficha_a_dedicada,
         'veredito escrito'),
        ('2. a linha diz que nasce sem ninguem ter visto a SERP', nasce_sem_olhos,
         'sem `serp_vista_por`'),
        ('3. o unico veredito afirmado afrouxado para nao-medida', afrouxa_o_veredito_afirmado,
         'veredito escrito'),
        ('4. veredito `alvo` inventado', inventa_alvo, '`alvo` nao existe'),
        ('5. ocupante da busca enviesada contrabandeado para a contagem', contrabandeia_enviesado,
         'busca ENVIESADA'),
        ('6. `enviesada` apagado de uma evidencia', apaga_enviesada, '`enviesada` tem de ser'),
        ('7. consulta que nomeia loja declarada neutra', mente_que_e_neutra, 'nomeia loja'),
        ('8. `dedicada_a_consulta: false`, que e afirmar ausencia', dedicada_false,
         'e true ou null'),
        ('9. ocupante sem a URL que sustenta o veredito', apaga_a_url, 'sem URL'),
        ('10. ocupante orfao, de consulta que ninguem declarou', ocupante_orfao,
         'que nao esta na evidencia'),
        ('11. lastro de banco inflado para furar a 30.2', infla_o_banco, 'recontado'),
        ('12. a pagina que ja serve a consulta apagada (30.4)', apaga_a_30_4,
         '`nasce_agora` escrito'),
        ('13. intencao de compra sem o juizo escrito', intencao_sem_juizo, 'JUIZO'),
        ('14. a declaracao do instrumento apagada do cabecalho', apaga_o_instrumento,
         'o_instrumento_desta_passada'),
        ('15. a lista do que nao foi medido apagada', apaga_o_nao_medido,
         'sem `o_que_nao_foi_medido`'),
    ]


def main():
    regua = carregar('regua-consultas-de-produto.py')
    with open(JSON, encoding='utf-8') as f:
        original = json.load(f)

    # Antes da primeira mutacao: o mundo de verdade tem de estar verde. Mutacao
    # sobre dado ja vermelho nao mede nada.
    base = regua.erros_do_arquivo(copy.deepcopy(original), None, DADOS)
    if base:
        print('REPROVADO: o arquivo de verdade ja esta vermelho antes da primeira mutacao:')
        for e in base[:5]:
            print('  - %s' % e)
        return 1

    reprovadas = inertes = sobreviveram = 0
    lista = mutacoes()
    for nome, estragar, esperado in lista:
        dados = copy.deepcopy(original)
        estragar(dados)
        erros = regua.erros_do_arquivo(dados, None, DADOS)
        if not erros:
            print('  FALHA  SOBREVIVEU: %s' % nome)
            sobreviveram += 1
            continue
        if not any(esperado in e for e in erros):
            print('  FALHA  INERTE (pega pelo motivo errado): %s' % nome)
            print('         esperava conter: %s' % esperado)
            print('         veio: %s' % erros[0])
            inertes += 1
            continue
        reprovadas += 1

    # A ultima, que e a unica que precisa do texto: `.md` editado a mao.
    md_errado = regua.render_md(original).replace('nasce agora', 'nasce agorA')
    erros = regua.erros_do_arquivo(copy.deepcopy(original), md_errado, DADOS)
    if any('difere do que a regua gera' in e for e in erros):
        reprovadas += 1
    else:
        print('  FALHA  SOBREVIVEU: 16. `.md` editado a mao nao foi visto')
        sobreviveram += 1

    alvo = len(lista) + 1
    if reprovadas == alvo and not inertes and not sobreviveram:
        print('%d de %d mutacoes reprovadas pelo portao, zero inerte.' % (reprovadas, alvo))
        return 0
    print('REPROVADO: %d de %d reprovadas, %d inerte(s), %d sobrevivente(s).' % (
        reprovadas, alvo, inertes, sobreviveram))
    return 1


if __name__ == '__main__':
    sys.exit(main())
