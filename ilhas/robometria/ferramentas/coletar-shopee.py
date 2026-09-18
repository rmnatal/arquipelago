#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Coleta foto, ficha de produto e link com sub-id pela Open API da Shopee.

    python3 ferramentas/coletar-shopee.py --ensaio  [--so <id>] [--limite N]
    python3 ferramentas/coletar-shopee.py --gravar  [--so <id>] [--limite N]

`--ensaio` escreve a proposta em `/tmp` e NAO toca no banco. A 25.3 manda
conferir uma amostra com os olhos antes de gravar, e ensaio sem gravacao e o
unico jeito de isso ser verdade e nao cerimonia.

Credencial: `SHOPEE_APP_ID` e `SHOPEE_SECRET` no AMBIENTE, nunca em arquivo
(secao 25.6). Esta ferramenta nao le documento nenhum: quem a chama ja passou
os dois em memoria.

---------------------------------------------------------------------------
A ESCADA DE PALAVRA-CHAVE, e por que ela existe (adendo de 16/09/2026)
---------------------------------------------------------------------------
A chave gravada em `afiliado.url_busca_produto` foi escrita para a BUSCA DO
SITE da Shopee, que perdoa. A API nao perdoa: `Electrolux KPCEL01 kit
performance` devolve **0 resultados** e `Xiaomi S10 robo aspirador` devolve 3.
Entao a consulta desce uma escada e para no primeiro degrau util:

    1. o codigo do fabricante sozinho
    2. marca + codigo
    3. marca + modelo + tipo de peca  (para modelo: marca + linha + codigo)
    4. a chave de hoje, a que foi escrita para a busca do site

**O degrau em que cada item casou fica GRAVADO**, do mesmo jeito que a escada
de fontes do banco: e procedencia, e sem ela ninguem sabe se o casamento veio
do codigo exato ou de uma frase folgada. Item que desce a escada inteira sem
casar fica sem foto e sem ficha, com o motivo escrito — isso e medicao
honesta, nao falha.

---------------------------------------------------------------------------
A REGRA DE CASAMENTO, mais dura que a do despacho, e o porque
---------------------------------------------------------------------------
O despacho pede: o titulo tem de conter o codigo da peca ou o nome do modelo.
A segunda metade, sozinha, aprovaria justamente o defeito que a ronda de 16/09
mediu no ar — `Xiaomi mop robo aspirador` devolvendo em primeiro lugar
*"Robo Xiaomi S40 PRO ORIGINAL"*, que e um ROBO e nao um mop. Nome de modelo
aparece no titulo de todo acessorio daquele modelo E no titulo do proprio
aparelho.

Entao:

- **peca** casa quando o titulo traz o CODIGO dela; ou quando traz o codigo de
  um modelo compativel **e** uma palavra do tipo da peca.
- **modelo** casa quando o titulo traz o codigo dele **e** nao e acessorio —
  titulo com "escova", "filtro", "mop", "saco", "pano", "bateria", "kit",
  "suporte" ou "reservatorio" e peca daquele modelo, nao o modelo.

Um casamento errado no banco e pior que casamento nenhum, porque parece dado.
"""

import argparse
import json
import os
import re
import sys
import time
import unicodedata
import struct
import urllib.parse
import urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(RAIZ), '..', 'ferramentas'))
sys.path.insert(0, os.path.abspath(os.path.join(RAIZ, '..', '..', 'ferramentas')))

import importlib.util

_spec = importlib.util.spec_from_file_location(
    'shopee_api', os.path.abspath(os.path.join(RAIZ, '..', '..', 'ferramentas', 'shopee-api.py')))
shopee = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(shopee)

SUB_ID = 'robometria'   # a Shopee recusa sub-id com hifen ou sublinhado
FONTE_DA_IMAGEM = 'shopee-api'
QUANTOS = 10
PAUSA = 0.35            # a API nao publica limite; folga barata contra 429

# Palavras que denunciam ACESSORIO num titulo. Usadas nas duas direcoes: um
# modelo nao pode casar com elas, e uma peca precisa de uma delas quando casa
# pelo nome do modelo em vez do proprio codigo.
PALAVRAS_DO_TIPO = {
    'filtro': ['filtro', 'hepa'],
    'escova lateral': ['escova lateral', 'escova direita', 'escova esquerda',
                       'escova frontal', 'escova'],
    'escova principal': ['escova principal', 'escova central', 'escova rolo',
                         'rolo', 'escova'],
    'mop': ['mop', 'pano'],
    'bateria': ['bateria'],
    # 'recipiente' entrou em 16/09/2026 pela regua de palavra-chave: o batismo
    # da propria WAP para esta peca, escrito em `nome_na_fonte` de dois
    # registros do banco, e "Recipiente de Po" — e a lista nao o conhecia, entao
    # "Recipiente Reservatorio Compativel com Robo Aspirador WAP W90" era
    # reprovado por nao abrir com o tipo. A palavra saiu do banco, nao da
    # cabeca de quem escreve a lista.
    'reservatorio': ['reservatorio', 'recipiente', 'tanque', 'deposito'],
    'kit': ['kit'],
}

# PALAVRA QUE DENUNCIA PECA NUM TITULO DE MODELO. A lista e longa de proposito
# e ficou longa por medicao: a primeira versao tinha nove palavras e deixou
# passar *"Carcaca Inferior P/ Aspirador Robo Electrolux Erb10"* como se fosse o
# ERB10, *"Placa de Potencia"* como o ERB11 e *"Controle Remoto"* como o ERB20.
# Loja de reposicao escreve o nome do robo no titulo da peca — e a peca e
# justamente o produto desta ilha, entao o banco esta cheio de codigo que a
# busca devolve em titulo de peca.
MARCA_DE_ACESSORIO = ['escova', 'filtro', 'hepa', 'mop', 'pano', 'saco',
                      'bateria', 'kit', 'reservatorio', 'suporte', 'rodizio',
                      'roda', 'sensor', 'carregador', 'fonte', 'adaptador',
                      'peca', 'reposicao', 'acessorio', 'carcaca', 'placa',
                      'controle', 'bocal', 'mangueira', 'pelicula', 'tampa',
                      'capa', 'contato', 'motor', 'cabo', 'parachoque',
                      'para-choque', 'lamina', 'lixeira', 'engrenagem',
                      'modulo', 'antena', 'chicote', 'suporte', 'base',
                      'protetor', 'rolamento', 'corrediça', 'corredica',
                      # CONSUMIVEL TAMBEM NAO E O ROBO, e este entrou por
                      # medicao: "Xiaomi Robot Vacuum 5 / 5 Pro / S40 S40C /
                      # S40 Pro M40S H40 Fluido Especial Para Limpeza" casou
                      # como se fosse o S40. O titulo abre com a marca e com
                      # "Robot", entao a regra de cabeca o aprovava; a palavra
                      # que o denuncia e "Fluido".
                      'fluido', 'liquido', 'detergente', 'solucao', 'spray',
                      'refil', 'aromatizante', 'higienizador', 'desinfetante']

# O que abre o titulo de um ROBO de verdade. Usado pela mesma regra de cabeca
# de titulo que vale para peca: o objeto e a primeira palavra que nomeia algo,
# e nao qualquer palavra que apareca no meio.
PALAVRAS_DO_ROBO = ['robo', 'aspirador', 'smart', 'robot']

# QUALIFICADOR QUE TROCA O OBJETO — medido no ensaio de 16/09/2026, e e por
# isto que a 25.3 manda conferir uma amostra com os olhos antes de gravar.
#
# A primeira versao desta ferramenta casou `multi-pr10205` (um FILTRO) com
# *"Tampa Do Filtro Do Aspirador Robo Multilaser Ho041"* e `multi-pr10127` (uma
# BATERIA) com *"Tampa Da Bateria"*. Tampa nao e filtro e nao e bateria: e a
# peca que cobre a peca. O titulo trazia o codigo do modelo e a palavra do
# tipo, entao a regra do despacho aprovava — e o leitor compraria a tampa
# achando que comprou o filtro.
QUALIFICADOR_QUE_TROCA_O_OBJETO = [
    'tampa', 'capa', 'protetor', 'carcaca', 'adesivo', 'manual', 'etiqueta',
    'controle remoto', 'berco', 'base de carregamento', 'suporte de parede',
]

# Palavra de quantidade que pode abrir um titulo legitimo antes do nome da
# peca: "2x Escova Lateral", "Par De Escovas".
ABERTURA_DE_QUANTIDADE = ['par', 'de', 'com', 'unidades', 'unidade', 'pcs',
                          'pecas', 'x']

# "KIT" NAO E QUANTIDADE QUANDO O REGISTRO NAO E UM KIT — segunda coisa que a
# conferencia de olho da 25.3 pegou, em 16/09/2026. `multi-pr10205` e um FILTRO
# e casou com *"Kit Filtro Pinos e Lamina Pecas do Reservatorio de Po"*, que e
# um kit misto: quem comprasse levaria pinos e lamina achando que levava o
# filtro. Perde-se aqui algum multipack legitimo ("Kit 2 Panos Mop"), e a troca
# e consciente: casamento errado no banco e pior que casamento nenhum.
ABERTURA_DE_CONJUNTO = ['kit', 'conjunto', 'combo', 'jogo']


def sem_acento(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto or '')
                   if unicodedata.category(c) != 'Mn').lower()


def token_no_titulo(codigo, titulo):
    """O codigo como TOKEN, e nao como pedaco de palavra.

    `E10` dentro de `E100` nao e o E10, e `S10` dentro de `MS106` tambem nao.
    Sem isto a coleta casaria modelo com modelo vizinho — o defeito que menos
    parece defeito, porque o titulo tem a marca certa e o numero quase certo.
    """
    if not codigo:
        return False
    alvo = sem_acento(str(codigo)).replace(' ', '')
    if not alvo:
        return False
    # O "+" CONTA COMO PARTE DO CODIGO. No catalogo da Xiaomi, `S10` e `S10+`
    # sao aparelhos diferentes, e a escova principal de um nao e a do outro.
    # No ensaio de 16/09/2026 `xiaomi-b106gl-zx` (escova do S10) casou com um
    # anuncio de "S20+ X20+ S10+ X10+" — quatro modelos, nenhum deles o S10.
    return re.search(r'(?<![a-z0-9])%s(?![a-z0-9+])' % re.escape(alvo),
                     sem_acento(titulo)) is not None


# SUFIXO QUE FAZ OUTRO APARELHO. "S40" e "S40 Pro" sao modelos diferentes, e o
# S40 Pro e justamente o que o portao do canal brasileiro tira da recomendacao.
# No ensaio de 16/09/2026 o `xiaomi-s40` casou com *"Robo Aspirador Xiaomi Robot
# Vacuum S40 PRO"*: o token do codigo estava la, e o aparelho era outro. Mesma
# familia do `S10` casando com `S10+` — o codigo nao termina onde parece.
SUFIXO_DE_VARIANTE = ['pro', 'plus', 'max', 'ultra', 'lite', 'mini', 'premium']

# E A VARIANTE TAMBEM VEM SOLTA, COM UM ESPACO NO MEIO. Terceira passada do
# mesmo ensaio: com o "Pro" barrado, o `xiaomi-s40` foi casar com *"Robo
# Aspirador Xiaomi S40 C Alexa"* — que e o S40C escrito com espaco. Uma letra
# solta depois do codigo e sufixo de modelo, nao palavra de frase; as palavras
# curtas que SAO de frase estao na lista abaixo e nao contam.
LIGACAO_CURTA = ['de', 'da', 'do', 'e', 'em', 'ou', 'na', 'no', 'a', 'o',
                 'se', 'ao', 'os', 'as', 'p', 'c']


def variante_depois_do_codigo(codigo, titulo):
    """O codigo aparece, mas seguido de um sufixo que faz outro aparelho?

    Nao vale quando o proprio codigo do registro ja traz o sufixo: `s40 pro`
    casando com "S40 Pro" e o casamento certo, nao o errado.
    """
    if not codigo:
        return False
    alvo = sem_acento(str(codigo))
    if any(alvo.endswith(' ' + s) or alvo.endswith(s) for s in SUFIXO_DE_VARIANTE):
        return False
    achado = re.search(r'(?<![a-z0-9])%s(?![a-z0-9+])\s+([a-z]+)'
                       % re.escape(alvo.replace(' ', '')), sem_acento(titulo))
    if not achado:
        return False
    seguinte = achado.group(1)
    if seguinte in SUFIXO_DE_VARIANTE:
        return True
    # "c" esta em LIGACAO_CURTA como "c/" de "com", entao ele so e barrado
    # quando vem logo depois do codigo — que e exatamente o caso do "S40 C".
    if len(seguinte) <= 2 and (seguinte not in LIGACAO_CURTA or seguinte == 'c'):
        return True
    return False


def e_acessorio(titulo):
    t = sem_acento(titulo)
    return any(p in t for p in MARCA_DE_ACESSORIO)


def palavras_do_tipo(tipo):
    return PALAVRAS_DO_TIPO.get(sem_acento(tipo).strip(), [sem_acento(tipo)])


def chave_de_hoje(registro):
    """A palavra-chave que ja esta no banco, extraida da URL crua da busca."""
    url = ((registro.get('afiliado') or {}).get('url_busca_produto') or '')
    if not url:
        return None
    consulta = urllib.parse.urlparse(url).query
    valores = urllib.parse.parse_qs(consulta).get('keyword')
    return valores[0] if valores else None


def escada_de_peca(peca, marcas, modelos):
    marca = marcas.get(peca['marca'], {})
    nome_busca = marca.get('nome_de_busca') or marca.get('nome') or peca['marca']
    codigo = peca.get('codigo_fabricante')

    compat = [c.get('modelo') for c in (peca.get('compatibilidade') or [])]
    linhas = []
    for mid in compat:
        m = modelos.get(mid) or {}
        rotulo = m.get('nome_comercial') or m.get('linha') or m.get('codigo_fabricante')
        if rotulo and rotulo not in linhas:
            linhas.append(rotulo)

    degraus = []
    if codigo:
        degraus.append((1, codigo))
        degraus.append((2, '%s %s' % (nome_busca, codigo)))
    if linhas:
        degraus.append((3, '%s %s %s' % (nome_busca, linhas[0], peca.get('tipo') or '')))
    chave = chave_de_hoje(peca)
    if chave:
        degraus.append((4, chave))
    return degraus


def escada_de_modelo(modelo, marcas):
    marca = marcas.get(modelo['marca'], {})
    nome_busca = marca.get('nome_de_busca') or marca.get('nome') or modelo['marca']
    codigo = modelo.get('codigo_fabricante')
    rotulo = modelo.get('nome_comercial') or modelo.get('linha')

    degraus = []
    if codigo:
        degraus.append((1, codigo))
        degraus.append((2, '%s %s' % (nome_busca, codigo)))
    if rotulo:
        degraus.append((3, '%s %s robo aspirador' % (nome_busca, rotulo)))
    chave = chave_de_hoje(modelo)
    if chave:
        degraus.append((4, chave))
    return degraus


def troca_o_objeto(titulo):
    """O titulo nomeia OUTRA peca que apenas cita a nossa? Ver o comentario da
    constante: tampa de filtro nao e filtro."""
    t = sem_acento(titulo)
    return any(q in t for q in QUALIFICADOR_QUE_TROCA_O_OBJETO)


def abre_com_o_tipo(titulo, tipo, alvos=None):
    """O TIPO E A CABECA DO TITULO, e nao uma palavra perdida no meio dele.

    `alvos` permite a quem chama apertar a lista de palavras sem recopiar esta
    funcao: `medir-palavras-chave.py` retira o substantivo pelado (`escova`)
    porque a pergunta dele e outra — ver `palavras_estritas_do_tipo` la. A
    regra de CABECA, que e o que esta funcao guarda, continua sendo uma so.

    "Filtro Hepa Para Robo Multilaser HO041" abre com o tipo e e o filtro.
    "Tampa Do Filtro Do Aspirador Ho041" cita o filtro e vende a tampa. A
    diferenca entre as duas nao esta em quais palavras aparecem — esta em
    QUAL delas e o objeto. Palavra de quantidade ("Kit 2 Panos Mop") pode
    abrir, porque nao troca o objeto, so conta.
    """
    palavras = [p for p in re.split(r'[^a-z0-9]+', sem_acento(titulo)) if p]
    alvos = alvos if alvos is not None else palavras_do_tipo(tipo)
    # ALVO DE DUAS PALAVRAS SO CASA COM AS DUAS, EM SEQUENCIA. Ate 16/09/2026
    # esta comparacao era `palavra == a or a.startswith(palavra + ' ') or palavra
    # in a.split()`, e as duas ultimas metades deixavam a palavra SOLTA casar com
    # o alvo composto: `escova` casava com `escova principal`. Dentro da coleta
    # isso nunca apareceu, porque la o codigo do registro ou do modelo ja tinha
    # amarrado o anuncio antes — mas a regua de palavra-chave, que pergunta outra
    # coisa, aprovou "Escova Frontal De Limpeza (...) Wap W90" como topo legitimo
    # de uma busca de ESCOVA PRINCIPAL. Frontal e lateral; a secao 26 diz que sao
    # funcoes OPOSTAS. A comparacao por sequencia fecha isso sem tirar nada de
    # quem chama com lista de uma palavra so.
    alvos_em_palavras = [a.split() for a in alvos]
    # "Kit" so abre titulo legitimo quando o proprio registro e um kit.
    abertura = list(ABERTURA_DE_QUANTIDADE)
    if sem_acento(tipo).strip() == 'kit':
        abertura += ABERTURA_DE_CONJUNTO
    for pos in range(min(6, len(palavras))):
        if any(palavras[pos:pos + len(a)] == a for a in alvos_em_palavras):
            # tudo que veio antes tem de ser quantidade, nunca outro objeto
            return all(p in abertura or p.isdigit() for p in palavras[:pos])
    return False


def substantivo_do_tipo(tipo):
    """A primeira palavra do tipo. `escova principal` -> `escova`. E o que sobra
    do tipo quando o qualificador dele e vocabulario da ilha e nao do vendedor."""
    return (tipo or '').strip().split(' ')[0]


def palavras_estritas_do_tipo(tipo):
    """A lista de `PALAVRAS_DO_TIPO` MENOS o substantivo pelado, quando o tipo
    tem qualificador.

    `PALAVRAS_DO_TIPO['escova lateral']` termina em `'escova'` — e `escova`
    sozinha nao diz QUAL escova. A secao 26 chama `lateral` e `principal` de
    funcoes OPOSTAS, e todo modelo do banco tem as duas.

    Esta funcao morava em `medir-palavras-chave.py` desde 16/09/2026 e desceu
    para ca em 18/09/2026, quando a coleta precisou dela — a regra e uma so e
    passou a morar na camada de baixo, com a lista que ela apara.
    """
    palavras = palavras_do_tipo(tipo)
    if len((tipo or '').strip().split(' ')) > 1:
        raiz = sem_acento(substantivo_do_tipo(tipo))
        palavras = [p for p in palavras if p != raiz]
    return palavras


def casa_peca(oferta, peca, modelos):
    titulo = oferta.get('titulo') or ''
    if troca_o_objeto(titulo):
        return None

    codigo = peca.get('codigo_fabricante')
    if token_no_titulo(codigo, titulo) and not variante_depois_do_codigo(codigo, titulo):
        return 'codigo da peca'

    # O SUBSTANTIVO PELADO NAO SERVE NO CAMINHO DO MODELO COMPATIVEL, e ate
    # 18/09/2026 servia. O comentario de `palavras_estritas_do_tipo` dizia que
    # `escova` sozinha basta "para a coleta", porque la "o codigo do registro ou
    # do modelo ja amarrou o anuncio". A primeira metade e verdadeira; a segunda
    # e falsa, e foi medida: quando quem amarra e o codigo do MODELO, o anuncio
    # esta preso ao APARELHO, e o aparelho tem escova lateral E escova principal.
    #
    # Medido na segunda passada de fotos de 18/09/2026: `positivo-11206519`
    # (escova PRINCIPAL, o rolo) casou com *"Escova E Filtro Hepa Para Robo
    # Aspirador Positivo Pra800"* — o codigo PRA800 no titulo e `escova` na
    # cabeca. A foto do anuncio, aberta com os olhos pela 25.3, traz um filtro e
    # uma escova LATERAL de tres bracos, e nenhum rolo. O banco tem
    # `positivo-11206518` (escova lateral) para o MESMO modelo, entao o titulo
    # descreve a irma e nao este registro. E a mesma familia da regra dos dois
    # registros no mesmo anuncio: casamento que nao identifica UM registro nao
    # identifica nenhum — aqui o que nao identifica e a palavra, nao o anuncio.
    if not abre_com_o_tipo(titulo, peca.get('tipo') or '',
                           palavras_estritas_do_tipo(peca.get('tipo') or '')):
        return None
    for c in (peca.get('compatibilidade') or []):
        m = modelos.get(c.get('modelo')) or {}
        if token_no_titulo(m.get('codigo_fabricante'), titulo):
            return 'modelo compativel %s + o tipo na cabeca do titulo' % m.get('codigo_fabricante')
    return None


def abre_com_o_robo(titulo, nome_da_marca):
    """O objeto do titulo e o ROBO, e nao uma peca que cita o robo.

    Mesma regra de cabeca de titulo que vale para peca. Aqui ela e ainda mais
    necessaria: o produto desta ilha e reposicao, entao o codigo de todo modelo
    do banco aparece em titulo de peca o dia inteiro. "Robo Aspirador
    Electrolux 4 em 1" abre com o robo; "Carcaca Inferior P/ Aspirador Robo
    Electrolux Erb10" abre com a carcaca.
    """
    palavras = [p for p in re.split(r'[^a-z0-9]+', sem_acento(titulo)) if p]
    marca = [p for p in re.split(r'[^a-z0-9]+', sem_acento(nome_da_marca)) if p]
    abertura = ABERTURA_DE_QUANTIDADE + marca
    for pos, palavra in enumerate(palavras[:6]):
        if palavra in PALAVRAS_DO_ROBO:
            return all(p in abertura or p.isdigit() for p in palavras[:pos])
    return False


def casa_modelo(oferta, modelo, nome_da_marca):
    titulo = oferta.get('titulo') or ''
    codigo = modelo.get('codigo_fabricante')
    if not token_no_titulo(codigo, titulo):
        return None
    if variante_depois_do_codigo(codigo, titulo):
        return None

    # CODIGO DE MODELO E CURTO E O MUNDO E GRANDE. `S10`, `E10`, `W100` e `S40`
    # sozinhos casaram, no ensaio de 16/09/2026, com mangueira de ar
    # condicionado, mascara capilar, whey protein e fechadura de Volvo S40. Por
    # isso o casamento de modelo exige TRES coisas juntas: o codigo, a marca e
    # o robo como objeto do titulo.
    if not token_no_titulo(nome_da_marca, titulo):
        return None
    if e_acessorio(titulo):
        return None
    if not abre_com_o_robo(titulo, nome_da_marca):
        return None
    return 'codigo do modelo + marca + o robo na cabeca do titulo'


def descer_a_escada(registro, degraus, casa):
    """Desce a escada e para no PRIMEIRO degrau que casar de verdade.

    Zero resultado nao e erro (secao 25.6): e so o degrau seguinte.
    """
    tentativas = []
    for degrau, palavra in degraus:
        try:
            ofertas = shopee.buscar(palavra, QUANTOS)
        except shopee.ErroDaShopee as erro:
            tentativas.append({'degrau': degrau, 'palavra': palavra,
                               'resultados': None, 'erro': str(erro)})
            continue
        time.sleep(PAUSA)
        tentativas.append({'degrau': degrau, 'palavra': palavra,
                           'resultados': len(ofertas)})
        for oferta in ofertas:
            porque = casa(oferta)
            if porque:
                return oferta, degrau, palavra, porque, tentativas
    return None, None, None, None, tentativas



# ---------------------------------------------------------------------------
# LARGURA E ALTURA SAO MEDIDAS, NUNCA SUPOSTAS
#
# A secao 6 do ARQUIPELAGO.md exige `largura` e `altura` quando ha `url`, e a
# razao e de tela: sem os dois no HTML a pagina PULA quando a foto carrega. A
# API da Shopee nao devolve dimensao nenhuma — mas a CDN dela
# (`cf.shopee.com.br`) responde 200 desta nuvem, medido em 16/09/2026. Entao o
# numero sai do ARQUIVO, lido dos primeiros bytes, e nao de um palpite sobre o
# que a Shopee costuma servir. Dimensao digitada e a mesma familia do numero de
# tela digitado: parece conferida.
# ---------------------------------------------------------------------------

def dimensao_da_imagem(url):
    """(largura, altura) lidas do cabecalho do arquivo. None se nao der.

    JPEG, PNG e WebP cobrem o que a Shopee serve. Le so o comeco do arquivo:
    a dimensao mora no cabecalho e baixar 300 KB por foto para ler 4 bytes
    seria gastar rede por nada.
    """
    try:
        pedido = urllib.request.Request(url, headers={'User-Agent': 'robometria/1.0'})
        with urllib.request.urlopen(pedido, timeout=30) as r:
            dados = r.read(262144)
    except Exception:
        return None

    if dados[:2] == b'\xff\xd8':                      # JPEG
        i = 2
        while i < len(dados) - 9:
            if dados[i] != 0xFF:
                i += 1
                continue
            marcador = dados[i + 1]
            if marcador in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                            0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                altura, largura = struct.unpack('>HH', dados[i + 5:i + 9])
                return largura, altura
            if marcador in (0xD8, 0xD9) or 0xD0 <= marcador <= 0xD7:
                i += 2
                continue
            tamanho = struct.unpack('>H', dados[i + 2:i + 4])[0]
            i += 2 + tamanho
        return None

    if dados[:8] == b'\x89PNG\r\n\x1a\n':             # PNG
        largura, altura = struct.unpack('>II', dados[16:24])
        return largura, altura

    if dados[:4] == b'RIFF' and dados[8:12] == b'WEBP':  # WebP (VP8X/VP8L/VP8 )
        formato = dados[12:16]
        if formato == b'VP8X':
            largura = int.from_bytes(dados[24:27], 'little') + 1
            altura = int.from_bytes(dados[27:30], 'little') + 1
            return largura, altura
        if formato == b'VP8 ':
            largura = struct.unpack('<H', dados[26:28])[0] & 0x3FFF
            altura = struct.unpack('<H', dados[28:30])[0] & 0x3FFF
            return largura, altura
    return None


def medir_imagens():
    """Preenche largura/altura de todo registro que ja tem `imagem.url`."""
    medidos, falharam = 0, []
    for caminho in ('dados/pecas.json', 'dados/modelos-robo.json'):
        doc = json.load(open(os.path.join(RAIZ, caminho), encoding='utf-8'))
        for r in doc['registros']:
            imagem = r.get('imagem') or {}
            if not imagem.get('url'):
                continue
            dim = dimensao_da_imagem(imagem['url'])
            if not dim:
                falharam.append(r['id'])
                continue
            imagem['largura'], imagem['altura'] = dim
            medidos += 1
            sys.stderr.write('  %-40s %dx%d\n' % (r['id'], dim[0], dim[1]))
        with open(os.path.join(RAIZ, caminho), 'w', encoding='utf-8') as f:
            json.dump(doc, f, ensure_ascii=False, indent=1)
            f.write('\n')
    sys.stderr.write('%d imagem(ns) medida(s); %d sem dimensao: %s\n'
                     % (medidos, len(falharam), ', '.join(falharam) or '-'))
    return 0


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--ensaio', action='store_true')
    p.add_argument('--gravar', action='store_true')
    p.add_argument('--so', default=None, help='um id so, para conferir com os olhos')
    p.add_argument('--limite', type=int, default=0)
    # SEGUNDA PASSADA (18/09/2026). A primeira coleta rodou sobre o banco de
    # 16/09 e o banco cresceu 30 registros depois dela. Repetir a escada inteira
    # sobre quem JA tem foto gasta chamada e, pior, troca por outro anuncio uma
    # foto que ja foi conferida com os olhos pela 25.3 — conferencia velha
    # aplicada a dado novo. Entao a passada de cobertura pede so quem falta.
    p.add_argument('--sem-foto', action='store_true', dest='sem_foto',
                   help='so os registros publicaveis sem `imagem.url`')
    p.add_argument('--saida', default='/tmp/coleta-shopee.json')
    # APLICAR A PROPOSTA JA CONFERIDA, sem repetir a coleta. A 25.3 manda olhar
    # a amostra antes de gravar; se gravar refizesse as chamadas, o que entra no
    # banco nao seria o que foi conferido — seria uma coleta nova, com os mesmos
    # criterios e outros resultados. Conferir uma coisa e gravar outra e o mesmo
    # defeito do teste que mede a si mesmo, na hora da gravacao.
    p.add_argument('--aplicar', default=None,
                   help='grava a proposta deste arquivo, sem chamar a API')
    p.add_argument('--medir', action='store_true',
                   help='le largura e altura do ARQUIVO de cada imagem ja gravada')
    args = p.parse_args()

    if args.medir:
        return medir_imagens()

    if not (args.ensaio or args.gravar or args.aplicar):
        p.error('escolha --ensaio, --gravar, --aplicar ou --medir')

    if args.aplicar:
        with open(args.aplicar, encoding='utf-8') as f:
            proposta = json.load(f)['itens']
        pecas_doc = json.load(open(os.path.join(RAIZ, 'dados/pecas.json'), encoding='utf-8'))
        modelos_doc = json.load(open(os.path.join(RAIZ, 'dados/modelos-robo.json'), encoding='utf-8'))
        gravar(proposta, pecas_doc, modelos_doc, time.strftime('%Y-%m-%d'))
        return 0

    marcas = {r['id']: r for r in json.load(
        open(os.path.join(RAIZ, 'dados/marcas.json'), encoding='utf-8'))['registros']}
    pecas_doc = json.load(open(os.path.join(RAIZ, 'dados/pecas.json'), encoding='utf-8'))
    modelos_doc = json.load(open(os.path.join(RAIZ, 'dados/modelos-robo.json'), encoding='utf-8'))
    modelos = {r['id']: r for r in modelos_doc['registros']}

    alvos = []
    for r in pecas_doc['registros']:
        if r.get('status') == 'publicavel':
            alvos.append(('peca', r))
    for r in modelos_doc['registros']:
        if r.get('status') == 'publicavel':
            alvos.append(('modelo', r))
    if args.sem_foto:
        alvos = [a for a in alvos if not (a[1].get('imagem') or {}).get('url')]
    if args.so:
        alvos = [a for a in alvos if a[1]['id'] == args.so]
    if args.limite:
        alvos = alvos[:args.limite]

    hoje = time.strftime('%Y-%m-%d')
    proposta = []

    for tipo, registro in alvos:
        if tipo == 'peca':
            degraus = escada_de_peca(registro, marcas, modelos)
            casa = lambda o, r=registro: casa_peca(o, r, modelos)
        else:
            degraus = escada_de_modelo(registro, marcas)
            _marca = marcas.get(registro['marca'], {})
            _nome = _marca.get('nome_de_busca') or _marca.get('nome') or registro['marca']
            casa = lambda o, r=registro, n=_nome: casa_modelo(o, r, n)

        oferta, degrau, palavra, porque, tentativas = descer_a_escada(registro, degraus, casa)

        item = {'id': registro['id'], 'entidade': tipo,
                'codigo': registro.get('codigo_fabricante'),
                'tentativas': tentativas}

        if not oferta:
            # A CAUSA DO RESIDUO TEM DE SER SEPARAVEL, e ate 18/09/2026 nao era.
            # Um motivo unico para toda falha junta duas coisas opostas: "a
            # Shopee nao anuncia isto" (nao ha o que colher, e coleta nenhuma
            # muda) e "a Shopee anuncia e nenhum titulo nomeia o registro" (ha
            # o que colher e o portao barrou, e a porta e outra fonte ou outra
            # chave). Quem le um motivo so nao consegue decidir o passo
            # seguinte — que e justamente o que esta passada existe para
            # entregar. O numero de resultados vistos fica escrito ao lado,
            # porque e a prova, e nao o adjetivo.
            vistos = sum(t['resultados'] for t in tentativas)
            if vistos == 0:
                item['causa'] = 'sem anuncio na shopee'
                item['motivo'] = ('a escada inteira foi percorrida e a Open API devolveu '
                                  'ZERO resultado em todos os degraus: nao ha anuncio a '
                                  'casar, e nao e o portao que barra')
            else:
                item['causa'] = 'titulo nao nomeia o registro'
                item['motivo'] = ('a escada inteira foi percorrida, a Open API devolveu %d '
                                  'resultado(s) e nenhum traz o codigo do registro com o '
                                  'tipo certo' % vistos)
            item['resultados_vistos'] = vistos
            proposta.append(item)
            sys.stderr.write('  -- %-42s sem casamento\n' % registro['id'])
            continue

        try:
            curto = shopee.encurtar(oferta['url_produto'], SUB_ID)
            time.sleep(PAUSA)
        except shopee.ErroDaShopee as erro:
            curto = None
            item['motivo_sem_link'] = str(erro)

        item.update({
            'casou': True,
            'degrau_da_palavra_chave': degrau,
            'palavra_chave': palavra,
            'porque_casou': porque,
            'titulo_na_shopee': oferta['titulo'],
            'item_id': oferta['item_id'],
            'shop_id': oferta['shop_id'],
            'loja': oferta['loja'],
            'preco_min': oferta['preco_min'],
            'imagem_url': oferta['imagem_url'],
            'url_produto': oferta['url_produto'],
            'url_afiliado': curto,
        })
        proposta.append(item)
        sys.stderr.write('  ok %-42s degrau %d  %s\n'
                         % (registro['id'], degrau, (oferta['titulo'] or '')[:52]))

    # DOIS REGISTROS NO MESMO ANUNCIO: no maximo um esta certo, e nao ha como
    # dizer qual. Medido no ensaio de 16/09/2026, quando `multi-pr10127` e
    # `multi-pr8116` — duas baterias distintas do banco — casaram com o MESMO
    # anuncio. Casamento que nao identifica nao e casamento: os dois caem.
    donos = {}
    for i in proposta:
        if i.get('casou'):
            donos.setdefault(i['item_id'], []).append(i)
    for item_id, disputantes in donos.items():
        if len(disputantes) > 1:
            nomes = ', '.join(d['id'] for d in disputantes)
            for d in disputantes:
                d['casou'] = False
                d['causa'] = 'casamento ambiguo'
                d['motivo'] = ('%d registros do banco casaram com o MESMO anuncio '
                               '(%s): %s. Casamento que nao identifica um registro '
                               'so nao identifica nenhum.'
                               % (len(disputantes), item_id, nomes))
                d.pop('url_afiliado', None)
                d.pop('imagem_url', None)
                d.pop('url_produto', None)
            sys.stderr.write('  !! anuncio %s disputado por %s — os dois caem\n'
                             % (item_id, nomes))

    casaram = [i for i in proposta if i.get('casou')]
    sys.stderr.write('\n%d de %d registros casaram (%d com link com sub-id)\n'
                     % (len(casaram), len(proposta),
                        sum(1 for i in casaram if i.get('url_afiliado'))))
    por_degrau = {}
    for i in casaram:
        por_degrau[i['degrau_da_palavra_chave']] = por_degrau.get(i['degrau_da_palavra_chave'], 0) + 1
    sys.stderr.write('degraus: %s\n' % ', '.join('%d -> %d' % (d, n)
                                                 for d, n in sorted(por_degrau.items())))

    # O RESIDUO AGRUPADO POR CAUSA, impresso pela propria passada. A cobertura
    # maxima que o criterio permite e metade do entregavel; a outra metade e
    # esta lista, e ela so serve se disser por que cada um ficou de fora.
    residuo = {}
    for i in proposta:
        if not i.get('casou'):
            residuo.setdefault(i.get('causa') or 'nao casou', []).append(i['id'])
    if residuo:
        sys.stderr.write('\nRESIDUO POR CAUSA (%d registro(s)):\n'
                         % sum(len(v) for v in residuo.values()))
        for causa in sorted(residuo, key=lambda c: -len(residuo[c])):
            sys.stderr.write('  %-32s %3d\n' % (causa, len(residuo[causa])))
            for ident in sorted(residuo[causa]):
                sys.stderr.write('      %s\n' % ident)

    with open(args.saida, 'w', encoding='utf-8') as f:
        json.dump({'gerado_em': hoje, 'sub_id_1': SUB_ID, 'itens': proposta},
                  f, ensure_ascii=False, indent=1)
    sys.stderr.write('proposta em %s\n' % args.saida)

    if not args.gravar:
        return 0

    gravar(proposta, pecas_doc, modelos_doc, hoje)
    return 0


def gravar(proposta, pecas_doc, modelos_doc, hoje):
    """Escreve no banco o que a proposta diz, e SO isso.

    A foto e a ficha entram; o `url_busca` de hoje **nao sai**, porque ele e o
    piso da 25.2 e piso nao se troca por bonus. E `afiliado.url` so recebe link
    que carregue o sub-id — sem ele, o campo fica como estava.
    """
    por_id = {i['id']: i for i in proposta}
    trocas = 0

    for doc in (pecas_doc, modelos_doc):
        for r in doc['registros']:
            i = por_id.get(r['id'])
            if not i:
                continue
            a = r.setdefault('afiliado', {})
            if not i.get('casou'):
                # O MOTIVO QUE VAI AO BANCO E O DA PROPOSTA, NAO UM TEXTO FIXO
                # (18/09/2026). Ate hoje as tres causas — sem anuncio, titulo
                # que nao nomeia, casamento ambiguo — desciam ao banco com a
                # mesma frase, e a frase dizia a segunda. Registro sem anuncio
                # nenhum ficava gravado como se o portao o tivesse barrado, o
                # que manda a proxima passada procurar chave melhor para um
                # produto que a Shopee nao vende.
                porque = i.get('motivo') or (
                    'a escada de palavra-chave da Open API da Shopee foi percorrida '
                    'inteira e nenhum resultado traz o codigo deste registro com o '
                    'tipo certo')
                r['imagem'] = {
                    'url': None, 'largura': None, 'altura': None, 'fonte': None,
                    'coletado_em': None, 'alt': None,
                    'motivo_do_null': (
                        'Coleta de %s — causa: %s. %s. Casamento errado no banco e pior '
                        'que casamento nenhum, porque parece dado. O registro NAO some '
                        'da vitrine: aparece com espaco reservado neutro (secao 6).'
                        % (hoje, i.get('causa') or 'nao casou', porque)),
                }
                a['motivo_sem_url_produto'] = (
                    'sem ficha (%s): %s (%s)' % (i.get('causa') or 'nao casou', porque, hoje))
                trocas += 1
                continue

            r['imagem'] = {
                'url': i['imagem_url'],
                'largura': None,
                'altura': None,
                'fonte': FONTE_DA_IMAGEM,
                'coletado_em': hoje,
                'alt': i['titulo_na_shopee'],
                'motivo_do_null': None,
            }
            a['url_produto'] = i['url_produto']
            a['motivo_sem_url_produto'] = None
            a['item_id_shopee'] = i['item_id']
            a['shop_id_shopee'] = i['shop_id']
            a['degrau_da_palavra_chave'] = i['degrau_da_palavra_chave']
            a['palavra_chave_que_casou'] = i['palavra_chave']
            a['titulo_na_loja'] = i['titulo_na_shopee']
            a['conferido_em'] = hoje
            if i.get('url_afiliado'):
                a['url'] = i['url_afiliado']
                a['degrau'] = 3   # anuncio de vendedor na Shopee (25.1)
            trocas += 1

    recontar(pecas_doc)
    recontar(modelos_doc)

    for caminho, doc in (('dados/pecas.json', pecas_doc),
                         ('dados/modelos-robo.json', modelos_doc)):
        with open(os.path.join(RAIZ, caminho), 'w', encoding='utf-8') as f:
            json.dump(doc, f, ensure_ascii=False, indent=1)
            f.write('\n')
    sys.stderr.write('gravado: %d registro(s) tocado(s)\n' % trocas)


def recontar(doc):
    """As quatro contagens do cabecalho que ESTA ferramenta move.

    "Numero de cabecalho de banco e numero de tela: contado, nunca digitado" —
    e ate 18/09/2026 a coleta era o unico jeito de mover esses quatro numeros
    sem reescrever nenhum deles. Quem pegava era o `validar-banco.py`, no passo
    seguinte, e o conserto era a mao. Portao que morde depois e melhor que
    portao nenhum, mas contagem que a propria escrita atualiza e melhor que os
    dois: o banco nunca chega a existir errado.

    As definicoes sao as do `validar-banco.py`, palavra por palavra, e e de
    proposito que ele continue conferindo — duas contas que se conferem sao uma
    trava; uma conta que confia em si mesma e um numero digitado com mais
    passos.
    """
    pub = [r for r in doc['registros'] if r.get('status') == 'publicavel']
    c = doc.get('contagem')
    if not c:
        return
    for chave, valor in (
            ('esperando_link_de_afiliado',
             sum(1 for r in pub if not (r.get('afiliado') or {}).get('url'))),
            ('itens_com_ficha',
             sum(1 for r in pub if (r.get('afiliado') or {}).get('url_produto'))),
            ('itens_com_link_de_afiliado',
             sum(1 for r in pub if (r.get('afiliado') or {}).get('url'))),
            ('itens_com_foto',
             sum(1 for r in pub if (r.get('imagem') or {}).get('url')))):
        if chave in c:
            c[chave] = valor


if __name__ == '__main__':
    sys.exit(main())
