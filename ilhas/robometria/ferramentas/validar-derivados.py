#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Portao: TODO arquivo derivado commitado ainda bate com o banco de hoje?

    python3 ferramentas/validar-derivados.py

NASCEU EM 21/09/2026, DE UM DEFEITO QUE FICOU UM DIA INTEIRO NO AR COM A
BANCADA VERDE. Em 20/09 as 15h39Z o portao do canal brasileiro anulou 7
canais e levou `recomendaveis_pela_r2` de 17 para 13. A interseccao da R1 com
a R2 caiu de 15 para 11 no mesmo instante — e `dados/cobertura-r1.json`,
gravado em 18/09, continuou afirmando 15. `dados/casca-fatos.json` LE aquele
arquivo, entao herdou o 15; a option herdou do casca-fatos; e /ferramentas/
serviu "So 15 dos 45 modelos do banco sao atendidos pelas duas ferramentas"
ate 21/09. As 38 passadas da bancada aprovaram o dia inteiro, porque NENHUMA
delas reconstruia o derivado: `cobertura-r1.py` e ferramenta de PRODUCAO pela
classificacao da bancada, e ferramenta de producao "nao afirma nada".

A CAUSA, e ela e de familia conhecida nesta ilha: o derivado so podia ser
conferido SOBRESCREVENDO-O. Perguntar "o arquivo de ontem ainda vale?" exigia
rodar `--gravar` e olhar o `git diff` — isto e, exigia destruir a resposta
para ve-la, e por isso ninguem perguntava. E a mesma familia do numero de tela
digitado da secao 8 do ARQUIPELAGO.md, um andar acima: ali o que parece
medido e o numero; aqui e a FRESCURA dele.

O CONSERTO TEM DUAS METADES. A primeira foi partir os geradores: o dicionario
que cada um grava saiu de dentro do main() e virou funcao pura
(`cobertura-r1.documento`, `gerar-casca-fatos.fatos_do_banco`, os `montar()`
da R1 e da R2, que ja eram). A segunda e este arquivo: ele monta o derivado em
MEMORIA e compara com o disco, sem escrever nada.

E A TERCEIRA REGRA, que e o que impede este portao de envelhecer igual ao que
ele conserta: ele nao tem so a lista do que cobre. Ele VARRE `dados/*.json`
atras de `gerado_por` e REPROVA quando acha um derivado que nao esta nem na
lista de cobertos nem na de nao-reconstruiveis-aqui, com o motivo escrito.
Derivado novo nasce coberto ou nasce denunciado — nunca calado. (A lista de
nao-reconstruiveis nao e desculpa: e divida escrita, com o motivo ao lado.)
"""

import datetime
import importlib.util
import json
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = os.path.join(BASE, 'dados')
FERRAMENTAS = os.path.join(BASE, 'ferramentas')

# Derivado que esta camada NAO consegue reconstruir, com o motivo. Nao e
# isencao: e divida escrita, e quem cobrir um deles apaga a linha daqui.
NAO_RECONSTRUIVEIS = {
    'dados/palavras-chave-medidas.json':
        'medicao do MUNDO DE FORA (Open API da Shopee) — reconstruir daqui '
        'exigiria rede e credencial, e a 25.2-b manda preservar a medicao '
        'datada em vez de refaze-la',
    'dados/acentuacao-restaurada.json':
        'registro historico da restauracao de 11/09/2026 — e a lista de '
        'conferencia de quem reler os manuais, nao uma funcao do banco de hoje',
    'dados/datas-das-paginas.json':
        'derivado do HISTORICO do git (data do ultimo commit de cada arquivo), '
        'entao ele muda a cada commit por desenho — comparar com o disco '
        'reprovaria toda vez que alguem commitasse, que e verde barato ao '
        'contrario',
    'dados/cobertura-r2.json':
        'o dicionario ainda mora dentro do main() de cobertura-r2.py — falta '
        'parti-lo como o da R1 foi partido em 21/09/2026. DIVIDA, nao isencao',
}


class Recusado(object):
    """O gerador se RECUSOU a contar — nao e divergencia, e impossibilidade, e
    as duas precisam de palavras diferentes. Nasceu em 21/09/2026 porque a
    bateria de mutacoes pegou este portao morrendo de traceback, com codigo 1 e
    sem a palavra REPROVADO na tela: INERTE ao contrario, e igualmente cego para
    quem le so o fim da saida."""

    def __init__(self, motivo):
        self.motivo = motivo


def carregar_modulo(nome_arquivo, apelido):
    caminho = os.path.join(FERRAMENTAS, nome_arquivo)
    spec = importlib.util.spec_from_file_location(apelido, caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def ler_json(rel):
    with open(os.path.join(BASE, rel), encoding='utf-8') as fh:
        return json.load(fh)


def ler_texto(rel):
    with open(os.path.join(BASE, rel), encoding='utf-8') as fh:
        return fh.read()


def diferencas(esperado, achado, caminho=''):
    """Lista as divergencias FOLHA A FOLHA, para a mensagem dizer o numero e
    nao so 'o arquivo mudou'. Quem le a saida precisa saber que caiu de 15
    para 11, nao que 4 KB diferem."""
    saida = []
    if type(esperado) is not type(achado) and not (
            isinstance(esperado, (int, float)) and isinstance(achado, (int, float))):
        return ['%s: no disco e %s, reconstruido e %s'
                % (caminho or '(raiz)', type(achado).__name__, type(esperado).__name__)]
    if isinstance(esperado, dict):
        for chave in sorted(set(esperado) | set(achado)):
            sub = '%s.%s' % (caminho, chave) if caminho else chave
            if chave not in achado:
                saida.append('%s: falta no disco (reconstruido tem %r)'
                             % (sub, resumir(esperado[chave])))
            elif chave not in esperado:
                saida.append('%s: sobra no disco (%r) e a reconstrucao nao tem'
                             % (sub, resumir(achado[chave])))
            else:
                saida.extend(diferencas(esperado[chave], achado[chave], sub))
    elif isinstance(esperado, list):
        if len(esperado) != len(achado):
            saida.append('%s: no disco tem %d item(ns), reconstruido tem %d'
                         % (caminho, len(achado), len(esperado)))
        for i, (e, a) in enumerate(zip(esperado, achado)):
            saida.extend(diferencas(e, a, '%s[%d]' % (caminho, i)))
    elif esperado != achado:
        saida.append('%s: no disco %r, reconstruido %r'
                     % (caminho, resumir(achado), resumir(esperado)))
    return saida


def resumir(valor):
    texto = valor if isinstance(valor, str) else json.dumps(valor, ensure_ascii=False)
    return texto if len(texto) <= 120 else texto[:117] + '...'


def sem_as_datas_da_varredura(doc):
    """`casca-fatos.json` carrega a data em que a VARREDURA rodou, e ela muda
    todo dia por desenho (o proprio gerador documenta: 'a data desta varredura,
    nunca a data em que o banco foi colhido'). Comparar essas duas chaves faria
    o portao reprovar todo dia seguinte ao da geracao, e portao que reprova por
    envelhecer do relogio vira portao desligado. O resto do arquivo — todos os
    numeros — e comparado inteiro."""
    doc = json.loads(json.dumps(doc))
    doc.pop('gerado_em', None)
    if isinstance(doc.get('medicao'), dict):
        doc['medicao'].pop('medido_em', None)
    return doc


def reconstruir():
    """Devolve [(arquivo, reconstruido, no_disco, comparador, depende_de)]."""
    itens = []

    cob = carregar_modulo('cobertura-r1.py', 'cobertura_r1')
    v = cob.varrer()
    itens.append(('dados/cobertura-r1.json', cob.documento(v),
                  ler_json('dados/cobertura-r1.json'), diferencas, None))
    itens.append(('dados/tabela-exemplos-r1.md',
                  cob.markdown_da_tabela(cob.tabela_de_exemplos(v)),
                  ler_texto('dados/tabela-exemplos-r1.md'), None, None))

    r1 = carregar_modulo('gerar-r1.py', 'gerar_r1')
    fatos_r1, gabarito_r1 = r1.montar()
    itens.append(('dados/r1-respostas.json', fatos_r1,
                  ler_json('dados/r1-respostas.json'), diferencas, None))
    itens.append(('dados/r1-referencia.json', gabarito_r1,
                  ler_json('dados/r1-referencia.json'), diferencas, None))

    r2 = carregar_modulo('gerar-r2.py', 'gerar_r2')
    fatos_r2, gabarito_r2 = r2.montar()
    itens.append(('dados/r2-respostas.json', fatos_r2,
                  ler_json('dados/r2-respostas.json'), diferencas, None))
    itens.append(('dados/r2-referencia.json', gabarito_r2,
                  ler_json('dados/r2-referencia.json'), diferencas, None))

    # O casca-fatos LE o cobertura-r1.json DO DISCO. Se aquele arquivo estiver
    # podre, reconstruir este daqui reproduz a mesma podridao e o resultado
    # bate — foi exatamente assim que o 15 chegou a tela. Entao ele declara a
    # dependencia e o main NAO o julga enquanto o de cima estiver reprovado:
    # dizer "ok" ali seria medir a propria ignorancia e chamar de veredito.
    casca = carregar_modulo('gerar-casca-fatos.py', 'gerar_casca_fatos')
    anterior = os.getcwd()
    try:
        os.chdir(BASE)            # este gerador le por caminho relativo
        reconstruido = sem_as_datas_da_varredura(casca.fatos_do_banco())
    except casca.Recusa as erro:
        reconstruido = Recusado(str(erro).replace('\n  ', '; '))
    finally:
        os.chdir(anterior)
    itens.append(('dados/casca-fatos.json', reconstruido,
                  sem_as_datas_da_varredura(ler_json('dados/casca-fatos.json')),
                  diferencas, 'dados/cobertura-r1.json'))

    return itens


def derivados_nao_declarados(cobertos):
    """A varredura que impede este portao de envelhecer: derivado no disco que
    nao esta em nenhuma das duas listas."""
    achados = []
    for nome in sorted(os.listdir(DADOS)):
        if not nome.endswith('.json'):
            continue
        rel = 'dados/' + nome
        try:
            doc = ler_json(rel)
        except (ValueError, UnicodeDecodeError) as erro:
            achados.append('%s: nao e JSON legivel (%s)' % (rel, erro))
            continue
        if not isinstance(doc, dict) or not doc.get('gerado_por'):
            continue
        if rel in cobertos or rel in NAO_RECONSTRUIVEIS:
            continue
        achados.append(
            '%s diz gerado_por %r e NAO esta coberto nem declarado — '
            'cubra-o aqui ou escreva o motivo em NAO_RECONSTRUIVEIS'
            % (rel, doc['gerado_por']))
    return achados


def main():
    print('Robometria — o derivado commitado ainda bate com o banco de hoje?')
    print('')

    falhas = []
    nao_julgados = []
    reprovados = set()
    itens = reconstruir()
    for arquivo, reconstruido, no_disco, comparador, depende_de in itens:
        if depende_de in reprovados:
            nao_julgados.append((arquivo, depende_de))
            print('  NAO JULGADO %-31s le %s, que reprovou'
                  % (arquivo, depende_de))
            continue
        if isinstance(reconstruido, Recusado):
            falhas.append((arquivo, ['o gerador recusou contar: %s'
                                     % reconstruido.motivo]))
            reprovados.add(arquivo)
            print('  REPROVADO  %-32s o gerador recusou contar' % arquivo)
            continue
        if comparador is None:
            divergencias = ([] if reconstruido == no_disco else
                            ['%s: o texto reconstruido difere do commitado '
                             '(%d caracteres no disco, %d reconstruidos)'
                             % (arquivo, len(no_disco), len(reconstruido))])
        else:
            divergencias = comparador(reconstruido, no_disco)
        if divergencias:
            falhas.append((arquivo, divergencias))
            reprovados.add(arquivo)
            print('  REPROVADO  %-32s %d divergencia(s)'
                  % (arquivo, len(divergencias)))
        else:
            print('  ok         %-32s bate com o banco' % arquivo)

    orfaos = derivados_nao_declarados({i[0] for i in itens})
    for linha in orfaos:
        print('  REPROVADO  %s' % linha)

    for arquivo, motivo in sorted(NAO_RECONSTRUIVEIS.items()):
        print('  fora       %-32s %s' % (arquivo, motivo.split(' — ')[0]))

    if falhas or orfaos:
        print('')
        print('REPROVADO: %d arquivo(s) derivado(s) fora de sincronia com o banco'
              '%s.'
              % (len(falhas) + len(orfaos),
                 '' if not nao_julgados else
                 ', e %d nao julgado(s) por dependerem de um deles'
                 % len(nao_julgados)))
        for arquivo, divergencias in falhas:
            print('')
            print('  %s' % arquivo)
            for linha in divergencias[:40]:
                print('    . %s' % linha)
            if len(divergencias) > 40:
                print('    . (mais %d divergencia(s))' % (len(divergencias) - 40))
        print('')
        print('  O conserto e rodar o gerador de cada um com --gravar e conferir')
        print('  o que mudou no git diff ANTES de commitar: derivado que muda')
        print('  sozinho e o banco falando, nao ruido.')
        return 1

    print('')
    print('APROVADO: %d derivado(s) reconstruido(s) e identico(s) ao commitado, '
          '%d declarado(s) fora do alcance desta camada.'
          % (len(itens), len(NAO_RECONSTRUIVEIS)))
    return 0


def _blindado():
    """Portao que morre de traceback sai com codigo 1 e SEM a palavra do
    veredito — e a bancada desta ilha julga as duas metades. Aqui a palavra sai
    sempre, com o erro junto."""
    try:
        return main()
    except Exception as erro:                      # noqa: BLE001 — de proposito
        import traceback
        traceback.print_exc()
        print('')
        print('REPROVADO: o portao dos derivados morreu ao reconstruir (%s: %s).'
              % (type(erro).__name__, erro))
        return 1


if __name__ == '__main__':
    sys.exit(_blindado())
