#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O PORTAO da lista de prospeccao do widget. BANCADA: sem rede.

Le `dados/prospeccao-widget.json` e cobra o que a regua
`ferramentas/regua-prospeccao.py` decide. Nao abre site nenhum — nao poderia,
porque o egresso desta nuvem nao alcanca nenhum desses dominios, e esse fato e
justamente o que a lista tem de declarar em vez de esconder.

O QUE ELE EXISTE PARA IMPEDIR, e nenhum dos casos e hipotetico nesta ilha:
  - linha que AFIRMA sem evidencia (o item que a leitura semanal de 23/09 abriu
    sobre 39 links era exatamente isso, do outro lado);
  - URL de um dominio usada como prova sobre OUTRO (a versao 1 do portao do
    espelho do CDN diluiu a propria prova assim, em 24/09/2026);
  - campo ausente valendo como resposta (a mesma porta dos fundos, fechada no
    mesmo dia: "controle" definido por negacao deixava foto sem procedencia
    entrar no grupo por omissao);
  - prioridade escrita a mao envelhecendo calada (a doenca que a `bancada.py`
    matou um andar acima);
  - `.md` e JSON dizendo coisas diferentes (o titulo em duas fontes, 24/09/2026);
  - dominio de marketplace ou rede social entrando como "site proprio", e
    dominio de ILHA do arquipelago entrando como alvo — ilha nao linka ilha
    (secao 10 do contrato).
"""
import importlib.util
import json
import os
import sys

PASTA = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(PASTA)
ARQUIPELAGO = os.path.dirname(os.path.dirname(RAIZ))
JSON = os.path.join(RAIZ, 'dados', 'prospeccao-widget.json')
MD = os.path.join(RAIZ, 'dados', 'prospeccao-widget.md')


def carregar(nome):
    caminho = os.path.join(PASTA, nome)
    spec = importlib.util.spec_from_file_location(nome.replace('-', '_')[:-3], caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def dominios_das_ilhas():
    """Os dominios das ilhas do arquipelago, lidos do manifest de cada uma.

    Leitura, nunca escrita: a secao 3 do contrato proibe EDITAR arquivo de ilha
    que a execucao nao reservou, e este portao so precisa saber os nomes para
    recusar que uma irma entre na lista de prospeccao. Se a pasta nao existir
    (portao rodando fora do repositorio), a regra fica sem material e nao inventa.
    """
    pasta = os.path.join(ARQUIPELAGO, 'ilhas')
    achados = set()
    if not os.path.isdir(pasta):
        return achados
    for nome in sorted(os.listdir(pasta)):
        caminho = os.path.join(pasta, nome, 'manifest.json')
        if not os.path.isfile(caminho):
            continue
        try:
            with open(caminho, encoding='utf-8') as f:
                dominio = json.load(f).get('dominio', '')
        except (OSError, ValueError):
            continue
        if dominio:
            achados.add(dominio.split('://', 1)[-1].strip('/').lower())
    return achados


def validar(dados, regua, md_no_disco=None, ilhas=()):
    """Devolve (afirmacoes, erros). Sem rede, sem efeito colateral."""
    erros = []
    total = 0

    total += 1
    if dados.get('publicar') is not False:
        erros.append('topo: `publicar` tem de ser false — nada desta lista vai para o ar')

    total += 1
    if dados.get('instrumentos_desta_passada') != ['busca']:
        erros.append('topo: `instrumentos_desta_passada` tem de declarar exatamente ["busca"] '
                     'enquanto o egresso estiver fechado')

    candidatos = dados.get('candidatos')
    ocupantes = dados.get('ocupantes_da_serp_de_calculadora')
    total += 2
    if not isinstance(candidatos, list) or not candidatos:
        erros.append('topo: sem lista de candidatos')
        return total, erros
    if not isinstance(ocupantes, list):
        erros.append('topo: sem lista de ocupantes da SERP')
        return total, erros

    vistos_id, vistos_dom = set(), set()
    algum_abriu = False
    for c in candidatos:
        rotulo = c.get('id') or c.get('dominio') or '<sem id>'
        dominio = (c.get('dominio') or '').lower()

        total += 1
        if not dominio:
            erros.append('%s: sem dominio' % rotulo)
            continue

        total += 2
        if c.get('id') in vistos_id:
            erros.append('%s: id repetido' % rotulo)
        if dominio in vistos_dom:
            erros.append('%s: dominio repetido — prospeccao duplicada e abordagem duplicada' % rotulo)
        vistos_id.add(c.get('id'))
        vistos_dom.add(dominio)

        total += 1
        if c.get('publicar') is not False:
            erros.append('%s: `publicar` tem de ser false' % rotulo)

        total += 1
        for proibido in regua.NAO_E_SITE_PROPRIO:
            if dominio == proibido or dominio.endswith('.' + proibido):
                erros.append('%s: %s nao e site proprio — vitrine de plataforma nao instala widget '
                             'e o link de la nao passa autoridade' % (rotulo, dominio))
                break

        total += 1
        if dominio in ilhas:
            erros.append('%s: %s e ILHA do arquipelago — ilha nao linka ilha (secao 10)' % (rotulo, dominio))

        total += 1
        if c.get('tipo') not in regua.TETO_POR_TIPO:
            erros.append('%s: tipo %r nao esta na regua dos tetos' % (rotulo, c.get('tipo')))

        total += len(regua.CAMPOS_DE_FATO)
        for campo in regua.CAMPOS_DE_FATO:
            if c.get(campo) is False:
                erros.append('%s: `%s` = false, e busca nao afirma ausencia — use null' % (rotulo, campo))

        total += 1
        if 'abriu_no_navegador' not in c:
            erros.append('%s: `abriu_no_navegador` ausente — ausencia nao vale como false' % rotulo)
        else:
            total += 1
            tem_navegador = any(ev.get('medido_como') == 'navegador'
                                for ev in c.get('evidencia') or [])
            if c['abriu_no_navegador'] is not tem_navegador:
                erros.append('%s: `abriu_no_navegador` = %r discorda da evidencia'
                             % (rotulo, c['abriu_no_navegador']))
            if c['abriu_no_navegador'] is True:
                algum_abriu = True

        total += 2
        for campo in ('contato', 'plataforma'):
            if c.get(campo) is None and not c.get(campo + '_motivo'):
                erros.append('%s: `%s` null sem motivo escrito — campo vazio calado e onde a '
                             'proxima passada inventa um dado' % (rotulo, campo))

        total += 1
        if not (c.get('porque') or '').strip():
            erros.append('%s: sem `porque` — ordem sem razao escrita e ordem que ninguem contesta' % rotulo)

        erros_ev = regua.erros_de_evidencia(c, dominio, rotulo)
        total += 1
        erros.extend(erros_ev)

        sustentados = set()
        for ev in c.get('evidencia') or []:
            for campo in ev.get('campos') or []:
                sustentados.add(campo)
        for campo in regua.campos_afirmados(c):
            total += 1
            if campo not in sustentados:
                erros.append('%s: afirma `%s` e nenhuma evidencia sustenta esse campo' % (rotulo, campo))

        total += 1
        calculada = regua.prioridade(c)
        if c.get('prioridade') != calculada:
            erros.append('%s: prioridade escrita %r, calculada %d pelos campos medidos'
                         % (rotulo, c.get('prioridade'), calculada))

    total += 1
    if dados.get('ninguem_abriu_nenhum_site') is True and algum_abriu:
        erros.append('topo: diz que ninguem abriu site e ha candidato com abriu_no_navegador=true')

    # O CRUZAMENTO DAS DUAS LISTAS, nas duas direcoes. E ele que impede a lista
    # de calculadora de existir em paralelo com a de candidatos e as duas
    # divergirem — exatamente o defeito do titulo em duas fontes.
    dom_ocupantes = set()
    for o in ocupantes:
        dominio = (o.get('dominio') or '').lower()
        total += 2
        if not dominio:
            erros.append('ocupante %r: sem dominio' % o.get('id'))
            continue
        if not (o.get('o_que_publica') or '').strip():
            erros.append('ocupante %s: sem `o_que_publica`' % dominio)
        dom_ocupantes.add(dominio)
        erros.extend(regua.erros_de_evidencia(o, dominio, 'ocupante %s' % dominio))

    for c in candidatos:
        dominio = (c.get('dominio') or '').lower()
        total += 2
        if c.get('ja_tem_calculadora') is True and dominio not in dom_ocupantes:
            erros.append('%s: afirma ter calculadora e nao esta na lista de ocupantes da SERP' % dominio)
        if dominio in dom_ocupantes and c.get('ja_tem_calculadora') is not True:
            erros.append('%s: esta na lista de ocupantes da SERP e nao afirma ter calculadora' % dominio)

    if md_no_disco is not None:
        total += 1
        if md_no_disco != regua.render_md(dados):
            erros.append('dados/prospeccao-widget.md esta fora de sincronia com o JSON — '
                         'rode `python3 ferramentas/gerar-prospeccao.py`')

    return total, erros


def main():
    regua = carregar('regua-prospeccao.py')
    with open(JSON, encoding='utf-8') as f:
        dados = json.load(f)
    md = None
    if os.path.isfile(MD):
        with open(MD, encoding='utf-8') as f:
            md = f.read()
    else:
        print('FALHA  dados/prospeccao-widget.md nao existe')
        print('REPROVADO: 1 de 1 afirmacoes falharam.')
        return 1
    total, erros = validar(dados, regua, md, dominios_das_ilhas())
    for e in erros:
        print('  FALHA  %s' % e)
    if erros:
        print('REPROVADO: %d de %d afirmacoes falharam.' % (len(erros), total))
        return 1
    print('APROVADO: %d afirmacoes, 0 falha.' % total)
    return 0


if __name__ == '__main__':
    sys.exit(main())
