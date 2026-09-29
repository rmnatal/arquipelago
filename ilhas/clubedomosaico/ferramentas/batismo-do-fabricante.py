#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A REGRA DO BATISMO: `nome_comercial` e campo do FABRICANTE, nao da ilha.

Este arquivo nao fala com a rede e nao grava nada. E so a regra, separada de
proposito pelo mesmo motivo de `casar-anuncio.py`: quem a USA
(`validar-banco.py`) e quem a ATACA (`mutacoes-batismo.py`) precisam da MESMA
funcao. Regra copiada em dois lugares e regra que a bateria mede num lugar e o
banco usa no outro.

---------------------------------------------------------------------------
POR QUE ELA EXISTE, e o numero que a pediu
---------------------------------------------------------------------------
Em 29/09/2026 a execucao das 16h17Z subiu dez materiais do degrau 4 da 25.1 e
deixou escrito que TRES dos dezoito que sobraram sao da Quartzolit e que o
defeito deles *"NAO e do link: e do BANCO — `nome_comercial` tem uma DESCRICAO
escrita por nos em vez do batismo do fabricante, que e a secao 26 ao
contrario"*. E concluiu: *"consertar e COLETA, na pagina do fabricante, e
esbarra no mesmo egresso"* — `quartzolit.weber` em 403.

**Nao esbarra.** O batismo ja estava no repositorio, dentro do proprio
registro, desde 25/09: `fontes[].url` guarda o endereco do boletim tecnico do
fabricante, e o NOME DO ARQUIVO e o fabricante batizando o produto.

    BT_Borracha Líquida Elástica Quartzolit_REV110624.pdf

O registro `quartzolit-borracha-liquida-elastica` chamava-se *"impermeabilizante
borracha liquida elastica quartzolit"*. A palavra `impermeabilizante` nao esta
no boletim: ela veio do CAMINHO da pagina de produto
(`/impermeabilizantes-quartzolit/impermeabilizantes-para-paredes-externas-e-fachadas/`),
que e a PRATELEIRA do fabricante, nao o nome do produto. A ilha colou a
classificacao dentro do batismo — a secao 26 exatamente ao contrario.

---------------------------------------------------------------------------
A REGRA JA ERA DO BANCO; O QUE FALTAVA ERA ALGUEM APLICA-LA A ESTE CAMPO
---------------------------------------------------------------------------
`escada_de_fontes` do `dados/esquema-banco.json` diz, desde o bloco 3:

    "Em conflito, o nivel mais alto vence e o outro fica registrado em
     divergencias[]."

O registro citava DUAS fontes do mesmo fabricante — boletim tecnico (nivel 2) e
pagina de produto (nivel 3) — e elas discordam sobre o nome. O banco ja mandava
o nivel 2 vencer. **Nenhum portao media isso para `nome_comercial`**, porque ate
29/09 nada comparava esse campo com um texto de fora. `casar-anuncio.py` foi o
primeiro a comparar, e o que ele achou foi um campo do proprio banco escrito no
papel errado.

---------------------------------------------------------------------------
O ESCOPO E ESTREITO DE PROPOSITO, e duas reguas mais largas foram MEDIDAS E
DESCARTADAS antes desta (29/09/2026, 19h3xZ)
---------------------------------------------------------------------------
Regua descartada 1 — *"o batismo tem de caber na URL da melhor fonte"*: reprova
**20 dos 38** registros, e quase todos sao honestos. Pagina de produto de
fabricante costuma ter endereco generico, e `Verniz Acrilico Brilhante` nao esta
na URL dele. Falso positivo em massa.

Regua descartada 2 — *"o batismo nao comeca com a palavra que a ilha usa para
classificar"*: reprova **20 dos 38**, entre eles `Verniz Acrilico Brilhante`
(tipo `verniz`) e `Rejunte Ceramicas Quartzolit` (categoria `rejunte`). O
fabricante batiza pelo tipo o tempo todo; comecar pelo tipo nao e defeito.

Esta regua, a terceira, mede **7 registros** — os que citam boletim tecnico em
PDF — e reprova **1**. Zero falso positivo no banco de hoje. Uma trava que so
morde onde ha prova e melhor que uma trava larga que a proxima execucao
aprende a ignorar.

---------------------------------------------------------------------------
O NOME DO ARQUIVO CHEGA MACHUCADO, E A COMPARACAO TEM DE SABER DISSO
---------------------------------------------------------------------------
O servidor do fabricante mutila o nome do arquivo de dois jeitos, e os dois
estao medidos neste banco:

  - **apaga a letra acentuada inteira** — `Boletim_Tcnico` por "Técnico",
    `rejunte_epxi_quartzolit.pdf` por "Rejunte Epóxi";
  - **cola as palavras** — `RejuntePorcelanatoseCeramicas`.

Comparar sem saber disso reprovaria `Rejunte Epóxi Quartzolit` e `Rejunte
Porcelanatos e Cerâmicas Quartzolit`, que sao batismos CERTOS. Entao a
comparacao ignora separador dos dois lados e aceita a palavra tambem na forma
em que o servidor a deixaria — sem as letras acentuadas.

**E a marca fica de fora da cobranca**: ela mora no campo `marca` e o fabricante
nem sempre a repete no nome do arquivo (`05._BoletimTcnico_RejunteP...` nao traz
"Quartzolit", e o produto e dele).

---------------------------------------------------------------------------
QUAIS FONTES BATIZAM E DECISAO DO ESQUEMA, NUNCA DESTA FUNCAO (26.2)
---------------------------------------------------------------------------
A lista mora em `dados/esquema-banco.json`, em `batismo_do_fabricante`, e chega
aqui por argumento. Lista digitada dentro da regua envelhece calada: o dia em
que uma fonte nova batizar, ela entra numa linha do esquema e a trava passa a
cobra-la sem uma linha de codigo.

E, como a 26.2 exige, **a trava reprova quando a lista some**. Regua que le a
propria lista de um arquivo de dados aprova tudo, em silencio, no dia em que o
arquivo perder a chave. `conferir()` levanta `EsquemaSemBatismo` nesse caso, em
vez de devolver "nenhum registro em escopo".
"""

import os
import re
import unicodedata
import urllib.parse


class EsquemaSemBatismo(Exception):
    """O esquema nao declara quais fontes batizam. Isto reprova, nunca aprova."""


VAZIAS = {
    'de', 'da', 'do', 'das', 'dos', 'para', 'e', 'em', 'com', 'a', 'o',
    'os', 'as', 'no', 'na', 'nos', 'nas', 'por', 'ao', 'aos', 'um', 'uma',
}


def _sem_acento(texto):
    """Acento removido, letra preservada: `Epóxi` -> `Epoxi`."""
    return ''.join(c for c in unicodedata.normalize('NFD', texto or '')
                   if unicodedata.category(c) != 'Mn')


def _sem_as_acentuadas(texto):
    """A letra acentuada APAGADA, que e o que o servidor do fabricante faz.

    `Técnico` -> `Tcnico`, `Epóxi` -> `Epxi`. Nao e a mesma coisa que tirar o
    acento: aqui a letra some.
    """
    fora = []
    for c in texto or '':
        decomposto = unicodedata.normalize('NFD', c)
        if len(decomposto) > 1 and unicodedata.category(decomposto[1]) == 'Mn':
            continue
        fora.append(c)
    return ''.join(fora)


def _achatar(texto):
    """So letra e digito, minusculo: separador nao conta dos dois lados."""
    return re.sub(r'[^0-9a-z]+', '', _sem_acento(texto or '').lower())


def nome_do_arquivo(url):
    """O nome do arquivo da fonte, ja decodificado — `%C3%AD` volta a ser `i`."""
    caminho = urllib.parse.urlparse(url or '').path
    return urllib.parse.unquote(os.path.basename(caminho))


def _formas_do_arquivo(url):
    """As duas formas comparaveis do nome do arquivo da fonte."""
    nome = nome_do_arquivo(url)
    return {_achatar(nome), _achatar(_sem_as_acentuadas(nome))}


def _formas_da_palavra(palavra):
    """As duas formas em que uma palavra do batismo pode chegar ao arquivo."""
    return {f for f in (_achatar(palavra), _achatar(_sem_as_acentuadas(palavra))) if f}


def palavras_cobradas(reg):
    """O que do `nome_comercial` tem de ser legivel no arquivo do fabricante.

    Fora: palavra vazia, e a MARCA — ela mora no campo dela.
    """
    marca = set()
    for bruto in re.split(r'[^0-9A-Za-zÀ-ÿ]+', reg.get('marca') or ''):
        if bruto:
            marca |= _formas_da_palavra(bruto)
    fora = []
    for bruto in re.split(r'[^0-9A-Za-zÀ-ÿ]+', reg.get('nome_comercial') or ''):
        if not bruto:
            continue
        if _achatar(bruto) in VAZIAS:
            continue
        formas = _formas_da_palavra(bruto)
        if not formas or (formas & marca):
            continue
        fora.append((bruto, formas))
    return fora


def fonte_que_batiza(reg, origens):
    """A fonte de MENOR `nivel` entre as que o esquema manda batizar.

    Devolve (id, fonte) ou (None, None) quando o registro nao cita nenhuma.
    Empate de nivel resolve pelo id, para a regua nao depender da ordem do JSON.
    """
    candidatas = []
    for chave, fonte in sorted((reg.get('fontes') or {}).items()):
        if not isinstance(fonte, dict):
            continue
        if (fonte.get('tipo_de_origem') or _origem_pela_url(fonte)) in origens:
            nivel = fonte.get('nivel')
            candidatas.append((nivel if isinstance(nivel, int) else 99, chave, fonte))
    if not candidatas:
        return None, None
    candidatas.sort(key=lambda c: (c[0], c[1]))
    return candidatas[0][1], candidatas[0][2]


def _origem_pela_url(fonte):
    """Sem campo declarado, a origem sai da extensao do arquivo."""
    caminho = urllib.parse.urlparse(fonte.get('url') or '').path
    return 'documento-pdf-do-fabricante' if caminho.lower().endswith('.pdf') else 'outra'


def conferir(reg, esquema):
    """(ok, laudo). `laudo` diz sempre POR QUE, inclusive quando aprova.

    Levanta `EsquemaSemBatismo` se o esquema nao trouxer a lista (26.2).
    """
    regra = (esquema or {}).get('batismo_do_fabricante')
    if not isinstance(regra, dict):
        raise EsquemaSemBatismo(
            'o esquema nao tem `batismo_do_fabricante`: sem a lista de fontes que '
            'batizam, esta trava nao mede nada e nao pode aprovar (26.2)')
    origens = regra.get('origens_que_batizam')
    if not isinstance(origens, list) or not origens:
        raise EsquemaSemBatismo(
            '`batismo_do_fabricante.origens_que_batizam` esta vazia ou nao e lista: '
            'trava sem lista aprova tudo em silencio (26.2)')
    origens = set(origens)

    chave, fonte = fonte_que_batiza(reg, origens)
    if fonte is None:
        return True, {'em_escopo': False,
                      'motivo': 'nao cita fonte que batize (%s)' % ', '.join(sorted(origens))}

    formas_arquivo = _formas_do_arquivo(fonte.get('url'))
    ausentes = []
    for bruto, formas in palavras_cobradas(reg):
        if not any(any(f in alvo for alvo in formas_arquivo) for f in formas):
            ausentes.append(bruto)
    laudo = {'em_escopo': True, 'fonte': chave, 'nivel': fonte.get('nivel'),
             'arquivo': nome_do_arquivo(fonte.get('url')),
             'ausentes': ausentes}
    if ausentes:
        laudo['motivo'] = (
            '`nome_comercial` traz %s, que o fabricante NAO escreve no batismo dele '
            '(%s, nivel %s). Palavra da prateleira do fabricante ou classificacao '
            'nossa colada no nome do produto e a secao 26 ao contrario'
            % (', '.join('`%s`' % a for a in ausentes), laudo['arquivo'], fonte.get('nivel')))
        return False, laudo
    laudo['motivo'] = 'todo o batismo e legivel em %s (nivel %s)' % (laudo['arquivo'],
                                                                    fonte.get('nivel'))
    return True, laudo
