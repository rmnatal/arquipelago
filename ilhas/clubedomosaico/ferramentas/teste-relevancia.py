#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BANCADA DA REGRA DE RELEVANCIA — 09/10/2026.

    python3 ferramentas/teste-relevancia.py

Mede `ferramentas/relevancia-do-anuncio.py` contra as declaracoes reais de
`dados/consultas-de-produto.json` e contra TITULOS REAIS, colhidos da API da
Shopee em 09/10/2026 e copiados aqui com o preco ao lado. Nenhum titulo desta
bancada foi inventado: cada um apareceu numa das 16 consultas do despacho, e e
por isso que ela mede o mundo em que a regra trabalha e nao um mundo de teste.

AS DUAS DIRECOES, e a bancada falha se faltar uma:
- **tem de SERVIR** — o produto que a consulta pede. Regra que recusa o certo
  custa tanto quanto regra que aceita o errado, e so os dois lados juntos pegam
  as duas. Foi exatamente o que o ensaio de 09/10 achou: `pastilha` nao casava
  com `Pastilhas` e os CINCO kits de verdade eram recusados enquanto DUAS
  ofertas de obra e de adesivo passavam, na mesma consulta.
- **tem de ser RECUSADO** — e com o termo certo escrito. Recusar nao e a mesma
  coisa que recusar PELO MOTIVO CERTO: anuncio derrubado pelo termo errado e
  uma recusa que sobrevive a lista de recusa sendo reescrita, e a bancada
  passaria verde sobre uma regra que mudou de causa.
"""

import importlib.util
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DECLARACAO = os.path.join(RAIZ, 'dados', 'consultas-de-produto.json')


def _modulo(nome, caminho):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


rel = _modulo('relevancia', os.path.join(RAIZ, 'ferramentas', 'relevancia-do-anuncio.py'))
col = _modulo('coletar', os.path.join(RAIZ, 'ferramentas', 'coletar-por-consulta.py'))


# (consulta, titulo real, serve?, termo de recusa esperado ou None)
CASOS = [
    # --- torques: a consulta mais limpa das dezesseis -----------------------
    ('torques-para-mosaico',
     'Torquês Para Mosaico Com Roldanas de Metal Duro - 61341 - Cortag', True, None),
    ('torques-para-mosaico',
     'Torques Para Mosaico 8 203mm - Berg', True, None),
    ('torques-para-mosaico',
     'Torquês para Mosaico 8 Pol com Roldanas Vonder', True, None),
    # A PECA DE REPOSICAO, que e o defeito desta familia: anuncio honesto do
    # produto errado para esta pagina.
    ('torques-para-mosaico',
     'Roldanas para reposição no torquês para mosaico, VONDER', False, 'reposicao'),

    # --- alicate: a enxurrada medida, 14 de 20 ------------------------------
    ('alicate-para-mosaico',
     'Alicate Cortador de Mosaico 8" Boca Redonda/Plana Para Vidro Cerâmica DIY', True, None),
    ('alicate-para-mosaico',
     'Beautyus Carboneto de Para Alicate de Telha 22 * 6 * 2mm Mosaico Substituir Corte des',
     False, 'carboneto'),
    ('alicate-para-mosaico',
     '[Zutimy] Carboneto de Para Alicate de Telha 22 * 6 * 2mm Mosaico Substituir Corte des CO',
     False, 'carboneto'),

    # --- pastilhas: o caso que o ensaio achou, e ele vai nos DOIS lados -----
    ('pastilhas-para-mosaico',
     'Kit com 900 Pastilhas para Mosaico, Artesanato – Escolha', True, None),
    ('pastilhas-para-mosaico',
     'Kit com 3388 Pastilhas para Mosaico 2x2cm – Escolha', True, None),
    # A PLACA DE NUMERO DE CASA: usa mosaico de pastilha e nao E pastilha.
    ('pastilhas-para-mosaico',
     'Placa para Número de Casa com Moldura Branca Arabescos com Mosaico de Pastilhas Cinzas e Pretas',
     False, 'placa para numero'),
    ('pastilhas-para-mosaico',
     'Número para Casa Branco Arabescos com Mosaico de Pastilhas de Vidro - informe seu número',
     False, 'numero para casa'),
    # O ADESIVO que imita pastilha — o plural e o ponto: `Adesivos`, nao `adesivo`.
    ('pastilhas-para-mosaico',
     'Kit 5 Adesivos Placa 30x30 Azulejo Pastilha Cozinha Mosaico', False, 'adesivo'),
    ('pastilhas-para-mosaico',
     'Pastilhas Adesivas papel de parede faixas para Azulejo Frete Grátis Cozinha, Banheiro Mosaico',
     False, 'adesiva'),
    # O REVESTIMENTO DE OBRA — e aqui o plural tambem decide: `Lavabos`.
    ('pastilhas-para-mosaico',
     'Placa Pastilha De Vidro Decorativas Cromo Prata Mosaico 30x30cm - Lavabos, Cozinhas, Áreas',
     False, 'lavabo'),

    # --- pastilha de vidro: o `exige` divergente, e e a unica diferenca -----
    ('pastilha-de-vidro-para-mosaico',
     'Pastilhas de vidro para Mosaico ( Pacote com 100 peças)', True, None),
    # SEM a palavra vidro: serve na mae e NAO serve aqui. E o unico caso da
    # bancada em que a mesma oferta tem dois vereditos, e e de proposito.
    ('pastilha-de-vidro-para-mosaico',
     'Kit com 900 Pastilhas para Mosaico, Artesanato – Escolha', False, None),

    # --- base de MDF: `quadro mosaico` e impresso EM MDF -------------------
    ('base-para-mosaico-mdf',
     'Kit 100 plaquinhas mdf cru 5x5 cm base para artesanato biscuit imã jogo memoria mosaico',
     True, None),
    ('base-para-mosaico-mdf',
     'Kit Quadros Decorativo Mosaico Urso Leão Coelho 3 peças 20x30 mdf alta qualidade',
     False, 'quadro'),

    # --- espelho: o termo de LUGAR separa material de peca pronta -----------
    ('espelho-para-mosaico',
     'Rolo De Espelhos Artesanato Fitas 4mm x 4mm 1 metro C/ Adesivo espelhos de mosaico',
     True, None),
    ('espelho-para-mosaico',
     '[sourcecome] 100 Pçs/Lote 2x2cm Mini Espelho De Vidro Quadrado Mosaico Azulejos Para Parede',
     False, 'parede'),
    ('espelho-para-mosaico',
     'Espelho Decorativo 3D Vidro Autocolante Kit Painel Mosaico para Sala Quarto',
     False, 'painel'),
    ('espelho-para-mosaico',
     'Estátua De Cacto De Bola De Discoteca , Decoração Mosaico De Espelho Verde , Ornamento Retrô',
     False, 'discoteca'),

    # --- as CINCO armadilhas: a regra existe para PROVAR o zero ------------
    ('kit-mosaico',
     'Kit 3 Quadros Decorativos Mosaico Jesus e Maria Cristão Estilo Vitral Decoração Sala',
     False, 'quadro'),
    ('azulejo-para-mosaico',
     'Papel De Parede Adesivo Para Cozinha Azulejo Ladrilho Retrô Mosaico Desenho Azul E Branco',
     False, 'papel de parede'),
    ('tela-para-mosaico',
     'Quadro Decorativo Mosaico 5 Peças Darth Vader Star Wars Filme Personagem Cinema Sala Quarto',
     False, 'quadro'),
    ('mandala-de-mosaico',
     'Quadro Decorativo Mosaico 5 Peças Mandala Azul Gold', False, 'quadro'),
    ('material-para-mosaico',
     # A RECUSA E `gesso` E NAO `forma 3d`, e a diferenca e a adjacencia: o
     # titulo diz `Forma Para Gesso 3d`, entao as duas palavras do termo
     # `forma 3d` nao sao vizinhas e o termo nao casa. Quem derruba e `gesso`.
     # Fixacao corrigida pela propria bancada em 09/10/2026 — ela esperava o
     # termo errado e a regra estava certa.
     'Forma Para Gesso 3d Mosaico de Pedra São Tomé 28x28cm ABS 2mm Forma para Gesso ou cimento',
     False, 'gesso'),

    # --- a consulta de outro endereco, medida e nao suposta ----------------
    ('vaso-de-mosaico', 'Vaso de Parede Delta Mosaico', True, None),
    ('vaso-de-mosaico',
     'Quadro Decorativo Mosaico Vaso De Flores Sala Quarto Escritório', False, 'quadro'),
]

# (titulo, quantidade esperada, molde esperado ou None quando a leitura e ambigua)
CASOS_DE_QUANTIDADE = [
    ('Kit com 900 Pastilhas para Mosaico, Artesanato – Escolha', 900, 'kit-com-n'),
    ('Kit com 3388 Pastilhas para Mosaico 2x2cm – Escolha', 3388, 'kit-com-n'),
    ('Pastilhas de vidro para Mosaico ( Pacote com 100 peças)', 100, 'pacote-com-n'),
    ('Kit 100 plaquinhas mdf cru 5x5 cm base para artesanato', 100, 'kit-n'),
    # A AMBIGUIDADE REAL, e ela custa um fator de 49: `Kit 5 Plaquinhas` e
    # `245pcs` sao duas leituras defensaveis do mesmo titulo. A funcao devolve
    # None com o motivo em vez de escolher por ordem de lista.
    ('Kit 5 Plaquinhas de Pastilhas de vidro para mosaico 2 x 2 cm - 245pçs - Escolha', None, None),
    # Titulo sem quantidade nenhuma: null e o motivo, nunca uma estimativa.
    ('Torquês Para Mosaico Com Roldanas de Metal Duro - 61341 - Cortag', None, None),
]


def main():
    with io.open(DECLARACAO, encoding='utf-8') as f:
        decs = {d['id']: d for d in json.load(f)['consultas']}

    falhas, afirmacoes = [], 0

    for id_consulta, titulo, esperado, termo in CASOS:
        dec = decs.get(id_consulta)
        if dec is None:
            falhas.append('a declaracao %r sumiu de consultas-de-produto.json' % id_consulta)
            continue
        v = rel.avaliar(titulo, dec)
        afirmacoes += 1
        if bool(v['serve']) is not bool(esperado):
            falhas.append('%s: esperava serve=%s e veio %s\n      %s'
                          % (id_consulta, esperado, v['serve'], titulo[:88]))
            continue
        if esperado is False and termo is not None:
            afirmacoes += 1
            if v['recusado_por'] != termo:
                falhas.append('%s: recusado pelo termo errado — esperava %r e veio %r\n      %s'
                              % (id_consulta, termo, v['recusado_por'], titulo[:88]))

    for titulo, qtd, molde in CASOS_DE_QUANTIDADE:
        lido, procedencia = col.quantidade_declarada(titulo)
        afirmacoes += 1
        if lido != qtd:
            falhas.append('quantidade: esperava %r e veio %r\n      %s' % (qtd, lido, titulo[:88]))
            continue
        if qtd is not None:
            afirmacoes += 1
            if procedencia != molde:
                falhas.append('quantidade: molde errado — esperava %r e veio %r\n      %s'
                              % (molde, procedencia, titulo[:88]))
        else:
            afirmacoes += 1
            if not procedencia or 'molde' not in procedencia and 'declara' not in procedencia:
                falhas.append('quantidade: sem numero e sem motivo escrito\n      %s' % titulo[:88])

    # A FALHA FECHADA: declaracao sem exigencia aceitaria o mundo.
    afirmacoes += 1
    if rel.avaliar('qualquer coisa', {'exige': [], 'recusa': []})['serve']:
        falhas.append('declaracao SEM exigencia aceitou o titulo — a falha tem de ser fechada')
    afirmacoes += 1
    if rel.avaliar('qualquer coisa', {'exige': [[]], 'recusa': []})['serve']:
        falhas.append('grupo de exigencia VAZIO passou — ele tornaria a exigencia decorativa')

    # A RECUSA VENCE A EXIGENCIA, dita como afirmacao e nao como comentario.
    afirmacoes += 1
    sozinha = {'exige': [['pastilha'], ['mosaico']], 'recusa': ['adesivo']}
    if rel.avaliar('Pastilha Adesivo Mosaico', sozinha)['serve']:
        falhas.append('a recusa NAO venceu a exigencia, e ela tem de vencer sempre')

    # O PLURAL, nos dois lados, que e o defeito de 09/10 virado afirmacao.
    for titulo in ('Pastilhas Mosaico', 'Pastilha Mosaico'):
        afirmacoes += 1
        if not rel.avaliar(titulo, {'exige': [['pastilha'], ['mosaico']], 'recusa': []})['serve']:
            falhas.append('o plural quebrou a exigencia: %r' % titulo)
    for titulo in ('Pastilha Adesivos Mosaico', 'Pastilha Adesivo Mosaico'):
        afirmacoes += 1
        if rel.avaliar(titulo, sozinha)['serve']:
            falhas.append('o plural quebrou a recusa: %r' % titulo)

    # GRUPO VAZIO AO LADO DE UM GRUPO VALIDO. As tres afirmacoes abaixo nasceram
    # da BATERIA DE MUTACAO de 09/10/2026: as mutacoes m05, m06 e m08 PASSARAM na
    # primeira rodada, e mutacao que passa e trava que a bancada nao mede. O caso
    # do `exige: [[]]` sozinho, que esta acima, nao as pegava — ele e absorvido
    # pela falha fechada do `not atendidas`, entao o grupo vazio precisa aparecer
    # ao LADO de um grupo que casa.
    afirmacoes += 1
    vazio = rel.avaliar('Pastilha Mosaico', {'exige': [['pastilha'], []], 'recusa': []})
    if vazio['serve']:
        falhas.append('grupo VAZIO ao lado de um grupo valido passou — '
                      'ele tem de recusar, nao ser ignorado')
    # E O VEREDITO NAO BASTA, porque ele e REDUNDANTE: medido pela mutacao m05 em
    # 09/10/2026, tirar o ramo dedicado ao grupo vazio NAO muda o `serve`, porque
    # o `casou is None` do ramo seguinte derruba o grupo vazio do mesmo jeito. O
    # que so o ramo dedicado entrega e o DIAGNOSTICO: ele nomeia o grupo como ele
    # foi declarado, em vez de devolver a lista filtrada e vazia. Sem esta
    # afirmacao a m05 passava — e uma trava cuja unica contribuicao e a mensagem
    # precisa ser medida PELA mensagem, nao pelo veredito.
    afirmacoes += 1
    if vazio['exigencia_que_faltou'] != [rel.GRUPO_VAZIO]:
        falhas.append('grupo vazio: esperava o marcador %r em exigencia_que_faltou e veio %r'
                      % (rel.GRUPO_VAZIO, vazio['exigencia_que_faltou']))

    # PALAVRA INTEIRA, com um caso que de fato e substring: `cola` esta dentro de
    # `colar`, e esta ilha tem as duas palavras no vocabulario (cola de colagem e
    # colar de mosaico). A fixacao anterior usava `tela` dentro de `telha` e NAO
    # mordia, porque `telha` nao contem `tela` — ela parecia medir e nao media.
    afirmacoes += 1
    if rel.avaliar('Colar de Mosaico com pingente',
                   {'exige': [['cola'], ['mosaico']], 'recusa': []})['serve']:
        falhas.append('`cola` casou dentro de `colar` — a regra voltou a casar pedaco de palavra')
    afirmacoes += 1
    if not rel.avaliar('Colar de Mosaico com pingente',
                       {'exige': [['colar'], ['mosaico']], 'recusa': ['cola']})['serve']:
        falhas.append('`recusa: cola` derrubou `Colar` — recusa por pedaco de palavra')

    # O PLURAL NO TERMO DECLARADO, nao so no titulo. As declaracoes reais desta
    # ilha trazem termo no plural (`espelhos`, `pincas`, `quadros`), e o corte
    # tem de valer nos DOIS lados da comparacao.
    afirmacoes += 1
    if not rel.avaliar('Espelho de Mosaico',
                       {'exige': [['espelhos'], ['mosaico']], 'recusa': []})['serve']:
        falhas.append('termo declarado no PLURAL nao casou titulo no singular — '
                      'o corte de plural parou de valer no termo')
    afirmacoes += 1
    if rel.avaliar('Quadro Decorativo Mosaico',
                   {'exige': [['mosaico']], 'recusa': ['quadros']})['serve']:
        falhas.append('`recusa: quadros` nao derrubou `Quadro` — '
                      'o corte de plural parou de valer no termo de recusa')

    for f in falhas:
        print('  DEFEITO %s' % f)
    print('%s: %d afirmacoes, %d defeito(s)'
          % ('REPROVADO' if falhas else 'APROVADO', afirmacoes, len(falhas)))
    return 1 if falhas else 0


if __name__ == '__main__':
    sys.exit(main())
