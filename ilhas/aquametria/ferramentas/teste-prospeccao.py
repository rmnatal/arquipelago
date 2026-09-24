#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BANCADA da regua da prospeccao. BANCADA: sem rede.

Mede `ferramentas/regua-prospeccao.py` em casos sinteticos. O portao
`validar-prospeccao.py` mede o arquivo de verdade e as `mutacoes-prospeccao.py`
medem o portao; aqui se mede a REGUA, que e onde mora a decisao de ordem.

AS AFIRMACOES SOBRE A PRIORIDADE SAO INVARIANTES, NAO A FORMULA DE NOVO. Repetir
`max(base, teto)` aqui seria escrever a mesma conta duas vezes e chamar a
segunda de teste — o erro entraria nas duas ao mesmo tempo e as duas
concordariam. Entao o que esta escrito abaixo e o que a ordem TEM de obedecer
(quem ja tem calculadora nunca sobe; so loja chega a 1; medir mais nunca piora a
posicao) mais casos nomeados, com o nome da linha real que cada um imita.

    python3 ferramentas/teste-prospeccao.py
"""
import importlib.util
import itertools
import os
import sys

PASTA = os.path.dirname(os.path.abspath(__file__))


def carregar(nome):
    caminho = os.path.join(PASTA, nome)
    spec = importlib.util.spec_from_file_location(nome.replace('-', '_')[:-3], caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class Bancada:
    def __init__(self):
        self.total = 0
        self.falhas = []

    def diz(self, condicao, mensagem):
        self.total += 1
        if not condicao:
            self.falhas.append(mensagem)

    def igual(self, obtido, esperado, mensagem):
        self.diz(obtido == esperado, '%s (esperava %r, veio %r)' % (mensagem, esperado, obtido))


def linha(tipo, vende=None, publica=None, calc=None):
    return {'tipo': tipo, 'vende_equipamento': vende, 'publica_conteudo': publica,
            'ja_tem_calculadora': calc}


def main():
    r = carregar('regua-prospeccao.py')
    b = Bancada()
    tipos = sorted(r.TETO_POR_TIPO)
    valores = (True, None)

    # 1. QUEM JA TEM CALCULADORA NUNCA SOBE. E o achado de 24/09/2026 e a regra
    #    mais forte da lista: vale para todo tipo e para toda combinacao dos
    #    outros dois campos, inclusive as duas em `true`.
    for tipo, vende, publica in itertools.product(tipos, valores, valores):
        b.igual(r.prioridade(linha(tipo, vende, publica, True)), 3,
                'com calculadora propria, %s tem de ficar em 3' % tipo)

    # 2. SO LOJA CHEGA A 1. Fabricante, distribuidora, conteudo, rede-pet e
    #    desconhecido tem teto, e teto nao se fura medindo mais campo.
    for tipo, vende, publica, calc in itertools.product(tipos, valores, valores, valores):
        p = r.prioridade(linha(tipo, vende, publica, calc))
        if tipo != 'loja':
            b.diz(p >= 2, '%s nunca pode chegar a 1' % tipo)
        b.diz(p in (1, 2, 3), '%s devolveu prioridade fora de 1..3' % tipo)

    # 3. MEDIR MAIS NUNCA PIORA A POSICAO. Se o campo passa de nao-medido a
    #    `true`, a prioridade nao pode subir de numero — senao a lista pune quem
    #    foi mais medido, que e o contrario do que ela existe para fazer.
    for tipo, publica in itertools.product(tipos, valores):
        antes = r.prioridade(linha(tipo, None, publica, None))
        depois = r.prioridade(linha(tipo, True, publica, None))
        b.diz(depois <= antes, 'medir vende_equipamento piorou %s' % tipo)
    for tipo, vende in itertools.product(tipos, valores):
        antes = r.prioridade(linha(tipo, vende, None, None))
        depois = r.prioridade(linha(tipo, vende, True, None))
        b.diz(depois <= antes, 'medir publica_conteudo piorou %s' % tipo)

    # 4. A COMBINACAO QUE CHEGA A 1 E UMA SO, e perder qualquer metade derruba.
    b.igual(r.prioridade(linha('loja', True, True)), 1,
            'loja que vende equipamento E publica conteudo (o caso aquariosdorio.com.br)')
    b.igual(r.prioridade(linha('loja', True, None)), 2,
            'loja com catalogo e sem conteudo medido (o caso aquaricamp.com.br)')
    b.igual(r.prioridade(linha('loja', None, True)), 2,
            'loja com conteudo e sem catalogo medido (o caso lojaaquaverso.com.br)')
    b.igual(r.prioridade(linha('loja')), 3,
            'loja sem nada medido cai para 3 — falta medida, nao falta merito')
    b.igual(r.prioridade(linha('loja', None, None, True)), 3,
            'loja que ja tem calculadora (o caso aquariosplantados.com.br)')
    b.igual(r.prioridade(linha('rede-pet', True, True)), 3,
            'rede pet com tudo medido continua em 3 (o caso cobasi.com.br)')
    b.igual(r.prioridade(linha('desconhecido', None, True)), 3,
            'tipo nao medido fica em 3 (o caso kauar.com.br)')
    b.igual(r.prioridade(linha('distribuidora', None, True)), 2,
            'distribuidora com blog (o caso aquaticabrazil.com.br)')
    b.igual(r.prioridade(linha('fabricante', True, None)), 2,
            'fabricante que vende direto (o caso doled.net.br)')
    b.igual(r.prioridade(linha('conteudo', None, True)), 2,
            'site de conteudo (o caso aquariovivo.com.br)')

    # 5. TIPO QUE A REGUA NAO CONHECE CAI PARA 3, nunca para 1. O portao recusa o
    #    tipo desconhecido em outra afirmacao; aqui se cobra que, se ele passar,
    #    o lado seguro do erro e descer.
    b.igual(r.prioridade(linha('loja-de-esquina', True, True)), 3,
            'tipo fora da regua tem de cair para 3')

    # 6. O HOST, E A ARMADILHA DO `endswith` DE TEXTO CRU.
    b.diz(r.do_dominio('https://loja.forfish.com.br/x', 'forfish.com.br'),
          'subdominio proprio conta como site proprio')
    b.diz(r.do_dominio('https://forfish.com.br/', 'forfish.com.br'), 'o dominio conta como ele mesmo')
    b.diz(r.do_dominio('https://WWW.Forfish.COM.BR/x', 'forfish.com.br'), 'maiuscula nao muda o host')
    b.diz(not r.do_dominio('https://forfish.com.br.exemplo.com/x', 'forfish.com.br'),
          'dominio que TERMINA com o nome do outro nao e subdominio dele')
    b.diz(not r.do_dominio('https://naoforfish.com.br/x', 'forfish.com.br'),
          'rotulo colado nao conta como subdominio')
    b.diz(not r.do_dominio('https://exemplo.com/forfish.com.br', 'forfish.com.br'),
          'o nome no CAMINHO nao e o host')
    b.igual(r.host_de('https://loja.exemplo.com.br:8443/a/b?c=1'), 'loja.exemplo.com.br',
            'porta, caminho e consulta saem do host')

    # 7. `tipo: desconhecido` NAO PEDE EVIDENCIA, e todo o resto pede. Nao saber
    #    e um estado declarado; afirmar e que precisa de prova.
    c = linha('desconhecido', True, None, None)
    c['dominio'] = 'exemplo.com.br'
    afirmados = r.campos_afirmados(c)
    b.diz('tipo' not in afirmados, '`tipo: desconhecido` nao e afirmacao e nao pede evidencia')
    b.diz('dominio' in afirmados and 'vende_equipamento' in afirmados,
          'dominio e campo em true pedem evidencia')
    b.diz('publica_conteudo' not in afirmados, 'campo null nao pede evidencia')
    c2 = linha('loja', None, None, None)
    c2['dominio'] = 'exemplo.com.br'
    b.diz('tipo' in r.campos_afirmados(c2), '`tipo: loja` E afirmacao e pede evidencia')

    # 8. A EVIDENCIA, uma afirmacao por defeito possivel.
    boa = {'campos': ['dominio'], 'medido_como': 'busca', 'medido_em': '2026-09-24',
           'consulta': 'x', 'resultado_titulo': 't', 'resultado_url': 'https://exemplo.com.br/a'}
    b.igual(r.erros_de_evidencia({'evidencia': [dict(boa)]}, 'exemplo.com.br', 'x'), [],
            'evidencia completa nao gera erro')
    b.diz(r.erros_de_evidencia({}, 'exemplo.com.br', 'x'), 'linha sem evidencia reprova')
    b.diz(r.erros_de_evidencia({'evidencia': []}, 'exemplo.com.br', 'x'), 'lista vazia reprova')
    for campo in ('consulta', 'resultado_titulo', 'medido_em', 'resultado_url'):
        ruim = dict(boa)
        del ruim[campo]
        b.diz(r.erros_de_evidencia({'evidencia': [ruim]}, 'exemplo.com.br', 'x'),
              'evidencia sem %s reprova' % campo)
    ruim = dict(boa, campos=[])
    b.diz(r.erros_de_evidencia({'evidencia': [ruim]}, 'exemplo.com.br', 'x'),
          'evidencia que nao diz o que sustenta reprova')
    ruim = dict(boa, medido_como='adivinhacao')
    b.diz(r.erros_de_evidencia({'evidencia': [ruim]}, 'exemplo.com.br', 'x'),
          'instrumento fora da lista reprova')
    ruim = dict(boa, medido_como='navegador')
    b.diz(r.erros_de_evidencia({'evidencia': [ruim]}, 'exemplo.com.br', 'x'),
          'navegador sem quem mediu reprova — esta nuvem nao tem navegador')
    ruim = dict(boa, medido_como='navegador', medido_por='Raphael, no Chrome')
    b.igual(r.erros_de_evidencia({'evidencia': [ruim]}, 'exemplo.com.br', 'x'), [],
            'navegador COM quem mediu passa — o instrumento existe, so nao e daqui')
    ruim = dict(boa, medido_como='curl', medido_por='Sentinela, 13/09')
    b.igual(r.erros_de_evidencia({'evidencia': [ruim]}, 'exemplo.com.br', 'x'), [],
            'curl com quem mediu passa')

    # 9. A LISTA DO QUE NAO E SITE PROPRIO tem de conter as duas familias, e a
    #    razao de cada uma esta no cabecalho da regua.
    for esperado in ('mercadolivre.com.br', 'shopee.com.br', 'instagram.com'):
        b.diz(esperado in r.NAO_E_SITE_PROPRIO, '%s tem de estar fora de site proprio' % esperado)

    for f in b.falhas:
        print('  FALHA  %s' % f)
    if b.falhas:
        print('REPROVADO: %d de %d afirmacoes falharam.' % (len(b.falhas), b.total))
        return 1
    print('APROVADO: %d afirmacoes, 0 falha.' % b.total)
    return 0


if __name__ == '__main__':
    sys.exit(main())
