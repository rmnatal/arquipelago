#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra o portao do canal brasileiro de propósito e exige REPROVACAO.

    python3 ferramentas/mutacoes-canal-brasileiro.py

POR QUE ESTE ARQUIVO EXISTE
---------------------------
"A PROVA DE QUE UMA TRAVA REPROVA E PARTE DO BLOCO" (secao 8 do ARQUIPELAGO.md).
E aqui ela e mais necessaria que o normal, porque o portao que nasceu em
16/09/2026 NAO MUDOU UMA LINHA DA TELA: antes dele a R2 recomendava 11 modelos,
depois dele recomenda os mesmos 11. Trava que nasce sem mudar nada e trava que
ninguem sabe se existe — e a unica forma de saber e mover o mundo ate ela morder.

O MUNDO QUE FAZ ELA MORDER JA ESTAVA NO BANCO, e e isso que torna este arquivo
mais que cerimonia. Em 16/09/2026 entraram cinco modelos Xiaomi (E10C, E12, S12,
S40 Pro, X20) cujos codigos as proprias paginas de acessorio da Xiaomi ja
declaravam, e que a Xiaomi Brasil nao lista. Um deles, o S40 Pro, declara 15.000
Pa — a MAIOR succao deste banco inteiro. Sem o portao ele nao entraria so na
lista: entraria em PRIMEIRO lugar em toda situacao de pelo, que e a consulta que
mais vende no nicho. O leitor receberia como primeira recomendacao um aparelho
que o fabricante nao vende no Brasil.

E o custo de errar aqui e assimetrico do jeito que a secao 10 do contrato
descreve: recomendar de menos deixa dinheiro na mesa; recomendar o que nao se
compra queima a confianca na pagina inteira, que e o unico ativo desta ilha.

O QUE CADA MUTACAO TEM DE FAZER: reprovar. A (3) e a que importa — ela quebra a
referencia E regera o artefato, entao as duas metades da R2 ficam de acordo entre
si, exatamente como no defeito do A1 em que gerador e teste erravam juntos. So a
terceira conta, que le o artefato publicado, discorda.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REFERENCIA = 'ferramentas/cobertura-r2.py'
CRUZAMENTO = 'ferramentas/cobertura-r1.py'

PORTAO_CERTO = """        if not tem_canal_brasileiro(m):
            sem_canal.append(m)
            continue
"""
PORTAO_FORA = """        if False:
            sem_canal.append(m)
            continue
"""

CRUZA_CERTO = """            (modelos[mid].get("pa_declarado") or {}).get("valor") is not None
            and (modelos[mid].get("canal_brasileiro") or {}).get("valor") is not None"""
CRUZA_FROUXO = """            (modelos[mid].get("pa_declarado") or {}).get("valor") is not None
            and True"""


def _troca(base, arquivo, antes, depois, quantas=1):
    caminho = os.path.join(base, arquivo)
    with open(caminho, encoding='utf-8') as f:
        texto = f.read()
    if texto.count(antes) != quantas:
        raise AssertionError('%s: esperava %d ocorrencia(s) de %r, achei %d — a mutacao '
                             'seria inerte' % (arquivo, quantas, antes[:48],
                                               texto.count(antes)))
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(texto.replace(antes, depois))


def _regerar(base):
    """Sem isto a mutacao na referencia nao chega a dados/r2-respostas.json e a
    conta que le o artefato mediria o arquivo de ontem — mutacao inerte com outro
    nome."""
    saida = subprocess.run(['python3', os.path.join(base, 'ferramentas/gerar-r2.py'),
                            '--gravar'], capture_output=True, text=True, cwd=base)
    if saida.returncode != 0:
        raise AssertionError('gerar-r2.py falhou depois da mutacao: %s'
                             % saida.stderr[-200:])


# ------------------------------------------------------------------ AS MUTACOES
def _portao_fora_da_referencia(base):
    """PRODUZ O MUNDO. A referencia volta a olhar so o Pa, o artefato e regerado,
    e as duas metades da R2 voltam a concordar — erradas juntas."""
    _troca(base, REFERENCIA, PORTAO_CERTO, PORTAO_FORA)
    _regerar(base)


def _canal_apagado_do_banco(base):
    """A PORTA DOS FUNDOS PELO DADO. O codigo fica intacto e o campo some de um
    modelo que HOJE e recomendado. O portao passa a barrar quem nao devia, a
    lista encolhe, e o cabecalho do banco deixa de bater."""
    caminho = os.path.join(base, 'dados/modelos-robo.json')
    with open(caminho, encoding='utf-8') as f:
        banco = json.load(f)
    mexeu = False
    for r in banco['registros']:
        if r['id'] == 'xiaomi-s20':
            r['canal_brasileiro'] = {'valor': None, 'unidade': None,
                                     'motivo_do_null': 'apagado pela mutacao'}
            mexeu = True
    if not mexeu:
        raise AssertionError('xiaomi-s20 nao esta mais no banco — a mutacao seria inerte')
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(banco, f, ensure_ascii=False, indent=1)
        f.write('\n')


def _canal_aponta_para_marketplace(base):
    """O portao aceitando marketplace e o portao deixando de existir: todo codigo
    tem busca em marketplace, entao um campo assim aprovaria os 38."""
    caminho = os.path.join(base, 'dados/modelos-robo.json')
    with open(caminho, encoding='utf-8') as f:
        banco = json.load(f)
    for r in banco['registros']:
        if r['id'] == 'xiaomi-s40-pro':
            r['fontes']['f-loja'] = {
                'nivel': 4, 'origem': 'varejo-via-busca', 'publicador': 'Shopee',
                'titulo_na_fonte': 'busca', 'url': 'https://shopee.com.br/search?keyword=S40+Pro',
                'canal_de_coleta': 'mutacao', 'verificado_em': '2026-09-16'}
            r['canal_brasileiro'] = {
                'valor': 'https://shopee.com.br/search?keyword=S40+Pro', 'unidade': None,
                'fonte': 'f-loja', 'declarado_como': 'busca'}
            break
    else:
        raise AssertionError('xiaomi-s40-pro sumiu — a mutacao seria inerte')
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(banco, f, ensure_ascii=False, indent=1)
        f.write('\n')


def _canal_digitado_diferente_da_fonte(base):
    """Endereco digitado ao lado de endereco derivado. Os dois comecam iguais e
    divergem no dia em que alguem corrige um so — a mesma familia dos tres
    lugares que declaravam a lista de tipos da R1."""
    caminho = os.path.join(base, 'dados/modelos-robo.json')
    with open(caminho, encoding='utf-8') as f:
        banco = json.load(f)
    for r in banco['registros']:
        if r['id'] == 'xiaomi-s10':
            r['canal_brasileiro']['valor'] = 'https://www.mi.com/br/product/outro-modelo/'
            break
    else:
        raise AssertionError('xiaomi-s10 sumiu — a mutacao seria inerte')
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(banco, f, ensure_ascii=False, indent=1)
        f.write('\n')


def _trocar_endereco(base, ident, endereco):
    """Troca o endereco do canal E o da fonte que ele cita, no mesmo movimento.
    Trocar so um dos dois faria a mutacao reprovar pela trava do 'endereco
    digitado diferente do derivado' — reprovaria, sim, e pela regra ERRADA, que
    e a forma mais silenciosa de uma bateria mentir que cobre uma trava."""
    caminho = os.path.join(base, 'dados/modelos-robo.json')
    with open(caminho, encoding='utf-8') as f:
        banco = json.load(f)
    for r in banco['registros']:
        if r['id'] == ident:
            fonte = r['canal_brasileiro']['fonte']
            r['canal_brasileiro']['valor'] = endereco
            r['fontes'][fonte]['url'] = endereco
            break
    else:
        raise AssertionError('%s sumiu — a mutacao seria inerte' % ident)
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(banco, f, ensure_ascii=False, indent=1)
        f.write('\n')


def _canal_sem_marca_de_brasil(base):
    """A TRAVA QUE FOI AFROUXADA EM 17/09/2026 TEM DE CONTINUAR MORDENDO. Naquele
    dia a Roborock entrou no banco e mostrou que a regua so conhecia duas formas
    de um endereco dizer Brasil — `.br` no dominio e `/br/` no caminho —, e que
    `https://br.roborock.com/...` nao tem nenhuma das duas: tem o SUBDOMINIO. A
    regua passou a aceitar tambem o rotulo `br.` na frente do host, e afrouxar
    trava sem plantar o mundo em que ela morde e como nao ter trava. Aqui o
    endereco do canal vira o global da mesma marca, que nao diz Brasil de forma
    nenhuma, e o portao tem de reprovar."""
    _trocar_endereco(base, 'roborock-q8-max',
                     'https://global.roborock.com/pages/q8-max-plus')


def _canal_com_br_no_meio_do_host(base):
    """E A OUTRA METADE DO MESMO AFROUXAMENTO, que e a que quase ninguem escreve:
    a regua nova NAO pode ter virado 'contem br em algum lugar'. Um host como
    `cbr.roborock.com` carrega as letras `br.` dentro de si e nao e canal
    brasileiro de coisa nenhuma — ele so passaria se a checagem fosse por
    substring em vez de por ROTULO. Esta mutacao existe para provar que a
    checagem e pelo rotulo, e ela e a unica desta bateria que reprovaria a
    versao mais obvia do conserto."""
    _trocar_endereco(base, 'roborock-q8-max',
                     'https://cbr.roborock.com/pages/q8-max-plus')


def _cruzamento_volta_a_contar_so_o_pa(base):
    """A REGUA DA META. O item 2 da definicao de pronta desta ilha e um numero
    sobre o cruzamento das duas ferramentas. Se ele voltar a contar Pa sozinho,
    os cinco modelos sem canal brasileiro entram na intersecao e a meta anda 5
    passos sem que UMA pessoa a mais seja atendida. A meta se fecharia sozinha."""
    _troca(base, CRUZAMENTO, CRUZA_CERTO, CRUZA_FROUXO)


MUTACOES = [
    (
        'o portao sai da referencia da R2 e o artefato e regerado',
        'PRODUZ O MUNDO: as duas metades da R2 concordam, e o S40 Pro (15.000 Pa) entra em primeiro lugar',
        _portao_fora_da_referencia,
        ('canal', 'banco'),
    ),
    (
        'o canal brasileiro e apagado de um modelo hoje recomendado',
        'a porta dos fundos pelo DADO: o codigo fica certo e a lista encolhe em silencio',
        _canal_apagado_do_banco,
        ('banco',),
    ),
    (
        'o canal brasileiro passa a apontar para marketplace',
        'o portao que aceita marketplace aprova os 38, porque todo codigo tem busca em marketplace',
        _canal_aponta_para_marketplace,
        ('banco',),
    ),
    (
        'o canal brasileiro e digitado diferente da fonte que ele cita',
        'endereco digitado ao lado de endereco derivado — os dois divergem sem ninguem ver',
        _canal_digitado_diferente_da_fonte,
        ('banco',),
    ),
    (
        'o canal passa a apontar para o endereco GLOBAL da mesma marca',
        'a marca de Brasil some do endereco inteiro e o portao tem de reprovar — a trava afrouxada em 17/09 continua mordendo',
        _canal_sem_marca_de_brasil,
        ('banco',),
    ),
    (
        'o host carrega as letras "br." no meio e nao no rotulo da frente',
        'cbr.roborock.com so passaria se o conserto de 17/09 fosse por substring; ele e por ROTULO, e esta e a mutacao que separa os dois',
        _canal_com_br_no_meio_do_host,
        ('banco',),
    ),
    (
        'o cruzamento das duas ferramentas volta a contar so o Pa',
        'a REGUA DA META afrouxa e a intersecao sobe 5 sem atender ninguem a mais',
        _cruzamento_volta_a_contar_so_o_pa,
        ('meta',),
    ),
]


def _rodar_canal(base):
    return subprocess.run(['python3', os.path.join(base, 'ferramentas/conferir-canal-na-resposta.py'), base],
                          capture_output=True, text=True, cwd=base)


def _rodar_banco(base):
    return subprocess.run(['python3', os.path.join(base, 'ferramentas/validar-banco.py'), base],
                          capture_output=True, text=True, cwd=base)


def _rodar_meta(base):
    """A meta nao tem teste proprio: o numero e a saida da varredura. Entao a
    trava aqui e a comparacao com o que a R2 REALMENTE recomenda, lida do banco
    por um caminho que nao e o do cruzamento."""
    saida = subprocess.run(['python3', os.path.join(base, 'ferramentas/cobertura-r1.py'), '--gravar'],
                           capture_output=True, text=True, cwd=base)
    if saida.returncode != 0:
        return saida
    with open(os.path.join(base, 'dados/cobertura-r1.json'), encoding='utf-8') as f:
        cob = json.load(f)
    with open(os.path.join(base, 'dados/modelos-robo.json'), encoding='utf-8') as f:
        banco = json.load(f)
    canal = {r['id']: (r.get('canal_brasileiro') or {}).get('valor')
             for r in banco['registros']}
    intersecao = cob['cruzamento_com_a_r2']['as_duas_respondem']
    ruins = [m for m in intersecao if canal.get(m) is None]
    if ruins:
        saida.returncode = 1
        saida.stdout += ('\nFALHA meta: %d modelo(s) contados na intersecao das duas '
                         'ferramentas nao tem canal brasileiro e a R2 nao recomenda: %s\n'
                         % (len(ruins), ', '.join(ruins)))
    return saida


CORREDORES = {'canal': _rodar_canal, 'banco': _rodar_banco, 'meta': _rodar_meta}


def main():
    reprovadas = 0
    passaram = []

    print('Mutacoes deliberadas no portao do canal brasileiro — cada uma TEM que reprovar\n')

    for nome, porque, aplicar, quais in MUTACOES:
        with tempfile.TemporaryDirectory() as tmp:
            base = os.path.join(tmp, 'ilha')
            shutil.copytree(RAIZ, base)
            try:
                aplicar(base)
            except (AssertionError, subprocess.CalledProcessError) as erro:
                print('  ERRO   %-62s %s' % (nome, erro))
                passaram.append(nome)
                continue

            pegou_em = []
            falhas = []
            for qual in quais:
                saida = CORREDORES[qual](base)
                if saida.returncode != 0:
                    pegou_em.append(qual)
                    falhas += [l.strip() for l in saida.stdout.splitlines()
                               if l.strip().startswith(('FALHA', 'x ', 'REPROVADO'))]

            if not pegou_em:
                print('  PASSOU %-62s <- a trava NAO pegou' % nome)
                print('         (%s)' % porque)
                passaram.append(nome)
                continue

            print('  ok     %-62s pegou em: %s' % (nome, ', '.join(pegou_em)))
            for l in falhas[:2]:
                print('         %s' % l[:118])
            reprovadas += 1

    print('\n%d de %d mutacoes reprovadas pela bancada.' % (reprovadas, len(MUTACOES)))
    if passaram:
        print('MUTACOES QUE PASSARAM (trava faltando):')
        for n in passaram:
            print('  - %s' % n)
        sys.exit(1)


if __name__ == '__main__':
    main()
