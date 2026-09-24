#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MUTACOES do portao da prospeccao. BANCADA: sem rede.

Portao que fica verde na primeira passada nao provou nada — provou que o dado de
hoje passa. Este arquivo quebra o dado DE PROPOSITO, uma quebra por vez, e cobra
que `validar-prospeccao.py` fique vermelho por MOTIVO CERTO: cada mutacao declara
um pedaco da mensagem que espera. Mutacao pega pela mensagem errada e mutacao
INERTE, e inerte conta como falha aqui — foi assim que esta ilha descobriu, em
15/09/2026, duas mutacoes que nao mediam nada.

O `.md` sai do caminho nas mutacoes de DADO (passa `md_no_disco=None`): quase
toda mutacao muda o texto gerado, e deixar essa regra ligada esconderia a causa
verdadeira atras de "fora de sincronia". A regra do `.md` tem mutacao propria, a
ultima.

    python3 ferramentas/mutacoes-prospeccao.py
"""
import copy
import importlib.util
import json
import os
import sys

PASTA = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(PASTA)
JSON = os.path.join(RAIZ, 'dados', 'prospeccao-widget.json')


def carregar(nome):
    caminho = os.path.join(PASTA, nome)
    spec = importlib.util.spec_from_file_location(nome.replace('-', '_')[:-3], caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def primeiro(dados, **filtros):
    for c in dados['candidatos']:
        if all(c.get(k) == v for k, v in filtros.items()):
            return c
    raise SystemExit('nenhum candidato casa com %r — mutacao nao pode ser montada' % filtros)


# Cada mutacao: (nome, funcao que estraga, pedaco da mensagem esperada)
def mutacoes():
    def topo_publicar(d):
        d['publicar'] = True

    def linha_publicar(d):
        d['candidatos'][0]['publicar'] = True

    def instrumento_do_topo(d):
        d['instrumentos_desta_passada'] = ['busca', 'navegador']

    def dominio_de_marketplace(d):
        c = d['candidatos'][0]
        c['dominio'] = 'mercadolivre.com.br'
        for ev in c['evidencia']:
            ev['resultado_url'] = 'https://mercadolivre.com.br/loja'

    def dominio_de_ilha(d):
        c = d['candidatos'][0]
        c['dominio'] = 'aquametria.com.br'
        for ev in c['evidencia']:
            ev['resultado_url'] = 'https://aquametria.com.br/'

    def tipo_inventado(d):
        d['candidatos'][0]['tipo'] = 'loja-de-esquina'

    def campo_de_fato_false(d):
        d['candidatos'][0]['publica_conteudo'] = False

    def afirma_sem_evidencia(d):
        c = primeiro(d, publica_conteudo=None)
        c['publica_conteudo'] = True

    def evidencia_de_outro_dominio(d):
        d['candidatos'][0]['evidencia'][0]['resultado_url'] = 'https://exemplo.com/pagina'

    def evidencia_que_parece_do_dominio(d):
        # A armadilha do `endswith` de texto cru: um dominio que TERMINA com o
        # nome do outro nao e subdominio dele.
        c = d['candidatos'][0]
        c['evidencia'][0]['resultado_url'] = 'https://%s.exemplo.com/pagina' % c['dominio']

    def evidencia_sem_consulta(d):
        d['candidatos'][0]['evidencia'][0]['consulta'] = ''

    def evidencia_sem_url(d):
        del d['candidatos'][0]['evidencia'][0]['resultado_url']

    def evidencia_sem_data(d):
        del d['candidatos'][0]['evidencia'][0]['medido_em']

    def instrumento_sem_quem(d):
        d['candidatos'][0]['evidencia'][0]['medido_como'] = 'navegador'

    def sem_evidencia_nenhuma(d):
        d['candidatos'][0]['evidencia'] = []

    def abriu_ausente(d):
        del d['candidatos'][0]['abriu_no_navegador']

    def abriu_sem_prova(d):
        d['candidatos'][0]['abriu_no_navegador'] = True

    def topo_mente_sobre_navegador(d):
        c = d['candidatos'][0]
        c['abriu_no_navegador'] = True
        c['evidencia'][0]['medido_como'] = 'navegador'
        c['evidencia'][0]['medido_por'] = 'Raphael, no Chrome'

    def topo_mente_que_alguem_abriu(d):
        # O MUNDO QUE O ESQUEMA PERMITE E O BANCO NAO TEM (secao 8): nenhuma linha
        # foi aberta em navegador hoje, entao a mutacao PRODUZ o caso em vez de
        # esperar por ele — aqui, o topo declarando o contrario do que as linhas
        # dizem, na direcao que sobrevive mais facil.
        d['ninguem_abriu_nenhum_site'] = False

    def contato_sem_motivo(d):
        d['candidatos'][0]['contato_motivo'] = ''

    def plataforma_sem_motivo(d):
        d['candidatos'][0]['plataforma_motivo'] = ''

    def sem_porque(d):
        d['candidatos'][0]['porque'] = '   '

    def prioridade_a_mao(d):
        d['candidatos'][0]['prioridade'] = 1 if d['candidatos'][0]['prioridade'] != 1 else 2

    def promove_quem_tem_calculadora(d):
        c = primeiro(d, ja_tem_calculadora=True)
        c['vende_equipamento'] = True
        c['publica_conteudo'] = True
        c['evidencia'].append({
            'campos': ['vende_equipamento', 'publica_conteudo'],
            'medido_como': 'busca', 'medido_em': '2026-09-24',
            'consulta': 'inventada', 'resultado_titulo': 'inventado',
            'resultado_url': 'https://%s/x' % c['dominio'],
        })
        c['prioridade'] = 1

    def dominio_repetido(d):
        clone = copy.deepcopy(d['candidatos'][0])
        clone['id'] = clone['id'] + '-2'
        d['candidatos'].append(clone)

    def id_repetido(d):
        clone = copy.deepcopy(d['candidatos'][0])
        clone['dominio'] = 'outro-dominio-qualquer.com.br'
        for ev in clone['evidencia']:
            ev['resultado_url'] = 'https://outro-dominio-qualquer.com.br/x'
        d['candidatos'].append(clone)

    def calculadora_fora_dos_ocupantes(d):
        c = primeiro(d, ja_tem_calculadora=True)
        d['ocupantes_da_serp_de_calculadora'] = [
            o for o in d['ocupantes_da_serp_de_calculadora'] if o['dominio'] != c['dominio']]

    def ocupante_que_o_candidato_nega(d):
        c = primeiro(d, ja_tem_calculadora=True)
        c['ja_tem_calculadora'] = None
        c['evidencia'] = [ev for ev in c['evidencia'] if 'ja_tem_calculadora' not in ev['campos']]
        c['prioridade'] = 2

    def ocupante_sem_o_que_publica(d):
        d['ocupantes_da_serp_de_calculadora'][0]['o_que_publica'] = ''

    def ocupante_com_url_de_outro(d):
        d['ocupantes_da_serp_de_calculadora'][0]['evidencia'][0]['resultado_url'] = 'https://exemplo.com/x'

    return [
        ('topo diz publicar: true', topo_publicar, '`publicar` tem de ser false'),
        ('uma linha diz publicar: true', linha_publicar, '`publicar` tem de ser false'),
        ('topo declara instrumento que a nuvem nao tem', instrumento_do_topo, 'exatamente ["busca"]'),
        ('dominio de marketplace como alvo', dominio_de_marketplace, 'nao e site proprio'),
        ('ilha do arquipelago como alvo', dominio_de_ilha, 'ilha nao linka ilha'),
        ('tipo fora da regua dos tetos', tipo_inventado, 'nao esta na regua dos tetos'),
        ('campo de fato em false', campo_de_fato_false, 'busca nao afirma ausencia'),
        ('afirma campo sem evidencia', afirma_sem_evidencia, 'nenhuma evidencia sustenta'),
        ('evidencia de outro dominio', evidencia_de_outro_dominio, 'nao e do dominio'),
        ('evidencia que so PARECE do dominio', evidencia_que_parece_do_dominio, 'nao e do dominio'),
        ('evidencia sem a consulta', evidencia_sem_consulta, 'sem a consulta'),
        ('evidencia sem URL', evidencia_sem_url, 'sem a URL do resultado'),
        ('evidencia sem data', evidencia_sem_data, 'sem data'),
        ('instrumento navegador sem quem mediu', instrumento_sem_quem, 'sem `medido_por`'),
        ('linha sem evidencia nenhuma', sem_evidencia_nenhuma, 'sem lista de evidencia'),
        ('abriu_no_navegador ausente', abriu_ausente, 'ausencia nao vale como false'),
        ('abriu_no_navegador true sem prova', abriu_sem_prova, 'discorda da evidencia'),
        ('topo diz que ninguem abriu e alguem abriu', topo_mente_sobre_navegador, 'ha candidato com abriu_no_navegador=true'),
        ('topo diz que alguem abriu e ninguem abriu', topo_mente_que_alguem_abriu, 'nenhuma linha tem abriu_no_navegador=true'),
        ('contato null sem motivo', contato_sem_motivo, '`contato` null sem motivo'),
        ('plataforma null sem motivo', plataforma_sem_motivo, '`plataforma` null sem motivo'),
        ('linha sem porque', sem_porque, 'sem `porque`'),
        ('prioridade escrita a mao', prioridade_a_mao, 'prioridade escrita'),
        ('quem ja tem calculadora promovido a 1', promove_quem_tem_calculadora, 'prioridade escrita'),
        ('dominio repetido', dominio_repetido, 'dominio repetido'),
        ('id repetido', id_repetido, 'id repetido'),
        ('quem tem calculadora fora dos ocupantes', calculadora_fora_dos_ocupantes, 'nao esta na lista de ocupantes'),
        ('ocupante que o candidato nega', ocupante_que_o_candidato_nega, 'nao afirma ter calculadora'),
        ('ocupante sem o que publica', ocupante_sem_o_que_publica, 'sem `o_que_publica`'),
        ('ocupante com URL de outro dominio', ocupante_com_url_de_outro, 'nao e do dominio'),
    ]


def main():
    regua = carregar('regua-prospeccao.py')
    validador = carregar('validar-prospeccao.py')
    with open(JSON, encoding='utf-8') as f:
        original = json.load(f)
    ilhas = validador.dominios_das_ilhas()

    # PORTAO ZERO: o dado de verdade tem de passar. Mutacao medida contra um dado
    # que ja reprova nao mede mutacao nenhuma.
    total, erros = validador.validar(copy.deepcopy(original), regua, None, ilhas)
    if erros:
        for e in erros:
            print('  FALHA  o dado ORIGINAL nao passa: %s' % e)
        print('REPROVADO: %d de %d afirmacoes falharam antes da primeira mutacao.' % (len(erros), total))
        return 1

    reprovadas = inertes = 0
    lista = mutacoes()
    for nome, estragar, esperado in lista:
        dados = copy.deepcopy(original)
        estragar(dados)
        _, erros = validador.validar(dados, regua, None, ilhas)
        if not erros:
            print('  FALHA  SOBREVIVEU: %s' % nome)
            continue
        if not any(esperado in e for e in erros):
            print('  FALHA  INERTE (pega pelo motivo errado): %s' % nome)
            print('         esperava conter: %s' % esperado)
            print('         veio: %s' % erros[0])
            inertes += 1
            continue
        reprovadas += 1

    # A mutacao do `.md`, que e a unica que precisa do texto.
    total_md = 1
    md_errado = regua.render_md(original).replace('PRIORIDADE 1', 'PRIORIDADE UM')
    _, erros = validador.validar(copy.deepcopy(original), regua, md_errado, ilhas)
    md_ok = any('fora de sincronia' in e for e in erros)
    if not md_ok:
        print('  FALHA  SOBREVIVEU: .md editado a mao nao foi visto')
    else:
        reprovadas += 1

    alvo = len(lista) + total_md
    if reprovadas == alvo and not inertes:
        print('%d de %d mutacoes reprovadas pelo portao, zero inerte.' % (reprovadas, alvo))
        return 0
    print('REPROVADO: %d de %d mutacoes reprovadas, %d inerte(s).' % (reprovadas, alvo, inertes))
    return 1


if __name__ == '__main__':
    sys.exit(main())
