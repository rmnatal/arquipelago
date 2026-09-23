#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Encurta o piso e colhe ficha e foto pela Open API da Shopee (secao 25.6).

    python3 ferramentas/coletar-shopee.py --ensaio [--so <id>] [--limite N]
    python3 ferramentas/coletar-shopee.py --gravar [--so <id>] [--limite N]

`--ensaio` escreve a proposta em /tmp e NAO toca no banco. A 25.3 manda
conferir uma amostra com os olhos antes de gravar, e ensaio sem gravacao e o
unico jeito de isso ser verdade e nao cerimonia.

Credencial: `SHOPEE_APP_ID` e `SHOPEE_SECRET` no AMBIENTE, nunca em arquivo
(secao 25.6). Esta ferramenta nao le documento nenhum: quem a chama ja passou
os dois em memoria.

---------------------------------------------------------------------------
DUAS CAMADAS, E A PRIMEIRA NAO DEPENDE DE CASAMENTO NENHUM
---------------------------------------------------------------------------
Esta ilha chegou a 23/09/2026 com **78 itens servindo `url_busca` crua** — link
que da saida de compra e nao rende comissao —, e a 25.2-b (18/09) diz com todas
as letras que isso "deixou de ser aceitavel como padrao". A leitura que importa
e que o conserto se reparte em duas camadas de risco muito diferente:

**CAMADA 1 — O PISO ENCURTADO (`afiliado.url_busca`).** A busca ja esta escrita
no banco desde 13/09, em `url_busca_produto`. Encurta-la com o sub-id da ilha e
uma chamada de rede sobre uma URL que **ja foi escolhida e conferida** — nao ha
produto a identificar, nao ha titulo a ler, nao ha como casar errado. Vale para
os 78, sem excecao e sem julgamento. **E a camada que fecha a 25.2-b.**

**CAMADA 2 — A FICHA E A FOTO (`afiliado.url` e `imagem`).** Aqui sim ha
casamento, e casamento errado no banco e pior que casamento nenhum, porque
parece dado. Vale as cinco armadilhas da 25.7 e mais uma que e desta ilha.

As duas sao independentes de proposito: a camada 2 falhar num item nao pode
tirar dele o piso que a camada 1 ja garantiu.

---------------------------------------------------------------------------
A ARMADILHA QUE E DESTA ILHA: A VARIANTE
---------------------------------------------------------------------------
As cinco armadilhas da 25.7 foram medidas na Robometria, que vende PECA. Esta
ilha vende o APARELHO, e o aparelho vem em linha: o Roxin HT-1300/Q3 existe em
25, 50, 100, 200 e 300 W, e o Eheim Jager em 50, 100, 150 e 200 W. O titulo do
anuncio traz a marca certa, a linha certa e a potencia **do vizinho**.

Isto nao e hipotese: esta ilha ja pagou por ele, no ar. O `ESTADO.md` registra,
em 07/09/2026, que entrou `ista-i-401-45` porque *"o anuncio da Shopee e da
luminaria de 45 cm, nao a de 60 do banco — colar o link no registro errado faria
a C15 prometer 3717 lm e entregar 810"*. E o proprio esquema ja escreveu a
regra, em prosa, na lista `afiliado.regras`:

    "Link de afiliado que aponta para OUTRA variante (outra medida, outra
     potencia) e defeito, nao aproximacao: ou existe o registro daquela
     variante, ou o produto fica sem link."

**Prosa nao conta e prosa nao barra anuncio** — e a mesma familia do
`afiliado.intestavel` (14/09) e do `chao_declarado_para` (22/09). Aqui ela vira
codigo, em duas metades:

- **Medida CONFLITANTE barra sempre.** Titulo que declara 300 W para o registro
  de 25 W nao esta calado sobre a medida: esta dizendo outra. Nao custa nada
  conferir e e o sinal mais forte que existe.
- **Medida AUSENTE barra so onde ela discrimina.** Se a linha tem irmaos que
  dividem o mesmo codigo — os cinco Roxin HT-1300, as tres Chihiros WRGB II Pro
  —, o titulo que nao diz a potencia (ou o comprimento) nao prova qual dos
  irmaos e, e nao casa. Se o codigo ja e unico no banco, como o do SunSun
  HW-303B, a medida nao precisa aparecer: o varejo de aquarismo anuncia
  canister pela VAZAO e nunca pelo consumo, e cobrar watt ali reprovaria o
  anuncio certo. **Quem responde qual dos dois casos e o proprio banco**, pela
  comparacao entre irmaos — nao uma lista escrita aqui, que envelheceria calada.

E a mesma comparacao entre irmaos da a terceira regra: **as palavras que, depois
do codigo, nomeiam outro produto do banco**. A Chihiros tem WRGB II, WRGB II Pro
e WRGB II Slim, e a WRGB II 90 e a Pro 90 sao as duas de 90 cm — ali nem a
medida separa, so o sufixo.

O preco de ser conservador aqui e ficar sem ficha; o preco de ser folgado e a
C5 prometer 25 W e entregar 300 W na casa de quem leu. Nao sao comparaveis.
"""

import argparse
import datetime
import glob
import importlib.util
import json
import os
import re
import struct
import sys
import time
import unicodedata
import urllib.parse
import urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

_spec = importlib.util.spec_from_file_location(
    'shopee_api', os.path.abspath(os.path.join(RAIZ, '..', '..', 'ferramentas', 'shopee-api.py')))
shopee = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(shopee)

SUB_ID = 'aquametria'    # a Shopee recusa sub-id com hifen ou sublinhado (25.7)
FONTE_DA_IMAGEM = 'shopee-api'
QUANTOS = 10
PAUSA = 0.35             # a API nao publica limite; folga barata contra 429

BANCOS = ['dados/produtos-aquecedor.json', 'dados/produtos-filtro.json',
          'dados/produtos-iluminacao.json', 'dados/produtos-midia.json']

# PALAVRAS QUE DENUNCIAM QUE O ANUNCIO NAO E O APARELHO (armadilha 1 da 25.7,
# virada do avesso). La a peca era o produto e o aparelho era o ruido; aqui o
# aparelho e o produto e a PECA DELE e o ruido. Loja de aquarismo anuncia a
# tampa, o rotor e o o-ring do canister com o codigo do canister no titulo.
NAO_E_O_APARELHO = [
    'tampa', 'capa', 'protetor', 'carcaca', 'adesivo', 'suporte', 'rotor',
    'impelidor', 'impeller', 'vedacao', 'o-ring', 'oring', 'anel de vedacao',
    'reposicao', 'reparo', 'eixo', 'rotator', 'ventosa', 'mangueira',
    'cabo', 'plug', 'tomada', 'bucha', 'parafuso', 'cesto', 'bandeja',
    'boia', 'valvula', 'registro', 'conector', 'abracadeira', 'esponja para',
]

# A MIDIA E O CASO EM QUE "REFIL" E LEGITIMO. Seachem Matrix, Eheim Substrat e
# JBL MicroMec SAO consumiveis: "refil" no titulo de uma midia e o produto, e
# no titulo de um filtro e uma peca dele. A lista acima nao traz "refil" por
# isso, e "esponja" so e barrada na forma "esponja para" (esponja DE filtro e
# midia; esponja PARA o canister X e peca).
ENTIDADES_CONSUMIVEIS = {'midia'}

# SUFIXO QUE FAZ OUTRO APARELHO (armadilha 4 da 25.7). Aqui ele e literal: o
# SunSun HW-303 e o HW-303B sao filtros diferentes — o B tem UV de 9 W —, e os
# dois moram neste banco. Uma letra colada no codigo nao e detalhe de escrita.
LIGACAO_CURTA = ['de', 'da', 'do', 'e', 'em', 'ou', 'na', 'no', 'a', 'o',
                 'se', 'ao', 'os', 'as', 'p', 'c', 'com', 'para']

SUFIXO_DE_VARIANTE = ['pro', 'plus', 'max', 'ultra', 'lite', 'mini', 'premium',
                      'evo', 'advanced']


def sem_acento(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto or '')
                   if unicodedata.category(c) != 'Mn').lower()


def token_no_titulo(codigo, titulo):
    """O codigo como TOKEN, e nao como pedaco de palavra.

    `HW-303` dentro de `HW-303B` nao e o HW-303, e `2213` dentro de `22130`
    tambem nao. Sem isto a coleta casaria um filtro com o filtro vizinho — o
    defeito que menos parece defeito, porque o titulo tem a marca certa e o
    numero quase certo.

    O separador e o que o varejo troca a vontade: "HT-1300", "HT1300" e
    "ht 1300" sao o mesmo codigo escrito por tres lojas. Entao o codigo vira um
    padrao que aceita qualquer separador ENTRE as suas partes — e o titulo NAO
    e achatado, que foi o primeiro jeito que tentei e que gruda as palavras umas
    nas outras: com o titulo sem espacos, "Roxin" deixa de ter fronteira e o
    portao reprova o anuncio certo dizendo que falta a marca.
    """
    if not codigo:
        return False
    partes = [re.escape(p) for p in re.split(r'[\s\-/_.]+', sem_acento(str(codigo))) if p]
    if not partes:
        return False
    padrao = r'[\s\-/_.]*'.join(partes)
    return re.search(r'(?<![a-z0-9])%s(?![a-z0-9+])' % padrao,
                     sem_acento(titulo)) is not None


def variante_depois_do_codigo(codigo, titulo, extras=()):
    """O codigo aparece, mas seguido de um sufixo que faz outro aparelho?

    Nao vale quando o proprio codigo do registro ja traz o sufixo: `wrgb ii pro`
    casando com "WRGB II Pro" e o casamento certo, nao o errado.

    `extras` sao os sufixos que o BANCO declara (ver `sufixos_irmaos`): as
    palavras que, depois deste codigo, nomeiam um irmao que existe de verdade.
    """
    if not codigo:
        return False
    alvo = sem_acento(str(codigo))
    proibidos = set(SUFIXO_DE_VARIANTE) | {sem_acento(e) for e in extras}
    if any(alvo.endswith(s) for s in proibidos):
        return False
    partes = [re.escape(p) for p in re.split(r'[\s\-/_.]+', alvo) if p]
    if not partes:
        return False
    padrao = r'[\s\-/_.]*'.join(partes)
    achado = re.search(r'(?<![a-z0-9])%s(?![a-z0-9+])\s+([a-z]+)' % padrao,
                       sem_acento(titulo))
    if not achado:
        return False
    seguinte = achado.group(1)
    if seguinte in proibidos:
        return True
    if len(seguinte) <= 2 and seguinte not in LIGACAO_CURTA:
        return True
    return False


# ---------------------------------------------------------------------------
# A MEDIDA DECLARADA — o coracao do portao desta ilha
# ---------------------------------------------------------------------------

def medidas_do_registro(registro):
    """As medidas que separam este registro dos irmaos da mesma linha.

    Devolve uma lista de (unidade, valor). Sai do campo TECNICO quando ele
    existe (`potencia_w`), e da `variante`/`modelo` quando a medida so esta
    escrita ali — que e o caso das luminarias, cujo comprimento e o nome
    comercial e nao um campo proprio do esquema.
    """
    medidas = []

    potencia = registro.get('potencia_w')
    if isinstance(potencia, (int, float)) and potencia > 0:
        medidas.append(('w', float(potencia)))

    texto = ' '.join(str(registro.get(c) or '') for c in ('variante', 'modelo'))
    texto = sem_acento(texto)

    for valor, unidade in re.findall(r'(\d+(?:[.,]\d+)?)\s*(cm|l|ml|w)\b', texto):
        valor = float(valor.replace(',', '.'))
        if unidade == 'ml':
            unidade, valor = 'l', valor / 1000.0
        if (unidade, valor) not in medidas:
            medidas.append((unidade, valor))

    return medidas


def codigo_base(registro):
    """O nome do registro SEM o designador de variante.

    "HT-1300 25 W" e "HT-1300 300 W" tem o mesmo codigo base — `ht-1300` —, e e
    por isso que o codigo sozinho nao os separa. "HW-303B" e "HW-603B" tem
    codigos base DIFERENTES, e o codigo sozinho ja os separa.

    O QUE SAI E O QUE A MEDIDA JA DIZ, e nao "todo numero no fim". Esta foi a
    segunda tentativa: a primeira descartava qualquer numero final e comia o
    `2213` do Eheim classic 250 (2213), que e o codigo de verdade daquele
    filtro e nao a variante dele. Entao cai fora o token de unidade (`w`, `cm`,
    `l`) e o token numerico cujo valor E UMA DAS MEDIDAS DECLARADAS do proprio
    registro — o `25` de "HT-1300 25 W" cai porque `potencia_w` e 25, e o
    `2213` fica porque nenhuma medida do registro vale 2213.
    """
    modelo = sem_acento(registro.get('modelo') or '').replace('(', ' ').replace(')', ' ')
    valores = {v for _, v in medidas_do_registro(registro)}
    guardados = []
    for t in re.split(r'\s+', modelo):
        if not t:
            continue
        if re.fullmatch(r'(?:cm|l|ml|w)', t):
            continue
        casado = re.fullmatch(r'(\d+(?:[.,]\d+)?)(cm|l|ml|w)?', t)
        if casado:
            n = float(casado.group(1).replace(',', '.'))
            if casado.group(2) == 'ml':
                n = n / 1000.0
            if any(abs(n - v) <= max(0.01 * v, 0.001) for v in valores):
                continue
        guardados.append(t)
    return ' '.join(guardados) or modelo


def sufixos_irmaos(registro, irmaos):
    """As palavras que, depois deste codigo, fazem OUTRO produto do banco.

    Sai do banco e nao de uma lista escrita aqui, pelo mesmo motivo que
    `medida_discrimina` sai: lista dentro da regua envelhece calada, e linha
    nova entraria sem regra nenhuma.

    O caso vivo, e ele e serio: a Chihiros tem TRES linhas neste banco — WRGB
    II, WRGB II Pro e WRGB II Slim — e o codigo base da primeira, `wrgb ii`,
    esta inteiro dentro do titulo das outras duas. Pior: a WRGB II 90 e a WRGB
    II Pro 90 tem as duas 90 cm, entao **nem o portao da medida as separa**.
    Sem esta funcao, a luminaria de 100 W casaria com o anuncio da de 110 W, e
    a C15 prometeria o lumen de uma entregando a outra.

    A lista estatica de sufixos comerciais continua valendo por cima desta: ela
    cobre o "Pro" que ainda nao entrou no banco.
    """
    base = codigo_base(registro)
    if not base:
        return set()
    palavras = set()
    for outro in irmaos:
        if outro.get('id') == registro.get('id'):
            continue
        outra_base = codigo_base(outro)
        if outra_base != base and outra_base.startswith(base + ' '):
            resto = outra_base[len(base) + 1:].split()
            if resto:
                palavras.add(resto[0])
    return palavras


def medida_discrimina(registro, irmaos):
    """A medida e o que separa este registro dos irmaos, ou o codigo ja separa?

    ESTA E A REGRA QUE O PROPRIO PORTAO ME CORRIGIU, e ela vale escrita. A
    primeira versao exigia a medida no titulo de TODO registro que declarasse
    uma, e reprovou um casamento certo: *"Filtro Canister SunSun HW-303B
    1400L/H com UV"* foi recusado por nao declarar os 35 W do registro. O
    varejo de aquarismo nao publica o consumo do canister — ele publica a
    VAZAO —, e exigir 35 W ali e cobrar do anuncio um numero que o mercado nao
    usa para nomear o produto.

    A pergunta certa nao e "o registro tem medida?" e sim "**a medida e o que
    distingue este registro do vizinho?**". Para o Roxin HT-1300 e para a
    Chihiros WRGB II Pro a resposta e sim: os cinco aquecedores e as tres
    luminarias compartilham o codigo e so a potencia (ou o comprimento) os
    separa. Para o SunSun HW-303B a resposta e nao: o codigo dele ja e unico
    no banco, e o portao do codigo faz o trabalho sozinho.

    E a resposta sai do BANCO, nao de uma lista escrita aqui: irmao novo
    entrando no banco liga o portao sozinho, e entidade nova nao nasce sem
    regra. Lista dentro da regua envelhece calada.
    """
    base = codigo_base(registro)
    if not base:
        return True
    for outro in irmaos:
        if outro.get('id') == registro.get('id'):
            continue
        if codigo_base(outro) == base:
            return True
    return False


def medida_no_titulo(unidade, valor, titulo):
    """O titulo declara ESTA medida, nesta unidade?

    Le o titulo inteiro atras de qualquer numero com a unidade pedida e compara
    com folga de 1%: "1 L" e "1000 ml" sao o mesmo volume escrito de dois
    jeitos, e "23,0 cm" e "23 cm" tambem.
    """
    t = sem_acento(titulo)
    achados = []
    for bruto, u in re.findall(r'(\d+(?:[.,]\d+)?)\s*(cm|litros|litro|lt|l|ml|w|watts|watt)\b', t):
        n = float(bruto.replace(',', '.'))
        if u in ('ml',):
            u, n = 'l', n / 1000.0
        elif u in ('litros', 'litro', 'lt'):
            u = 'l'
        elif u in ('watts', 'watt'):
            u = 'w'
        achados.append((u, n))
    for u, n in achados:
        if u == unidade and abs(n - valor) <= max(0.01 * valor, 0.001):
            return True
    return False


def medida_conflitante(unidade, declarados, titulo):
    """O titulo declara, nesta unidade, SO valores que o registro nao tem.

    E o sinal mais forte que existe de casamento errado: o anuncio nao esta
    calado sobre a medida, ele esta dizendo uma medida diferente. Um titulo
    como "Roxin HT-1300 300w" para o registro de 25 W cai aqui.

    `declarados` e a lista INTEIRA dos valores que o registro tem naquela
    unidade, e nao um valor de cada vez. A primeira escrita comparava um a um e
    reprovou um casamento certo: *"Filtro Canister SunSun HW-303B com UV 9w
    110v"* foi barrado por "declarar outra medida em w", quando o 9 W e a
    lampada UV **do proprio registro**, escrita na variante dele. Um aparelho
    tem varios numeros na mesma unidade — o consumo da bomba e a potencia da
    UV —, e conflito so existe quando o titulo nao bate com NENHUM deles.
    """
    t = sem_acento(titulo)
    no_titulo = []
    for bruto, u in re.findall(r'(\d+(?:[.,]\d+)?)\s*(cm|litros|litro|lt|l|ml|w|watts|watt)\b', t):
        n = float(bruto.replace(',', '.'))
        if u in ('ml',):
            u, n = 'l', n / 1000.0
        elif u in ('litros', 'litro', 'lt'):
            u = 'l'
        elif u in ('watts', 'watt'):
            u = 'w'
        if u == unidade:
            no_titulo.append(n)
    if not no_titulo:
        return False
    return not any(abs(n - v) <= max(0.01 * v, 0.001)
                   for n in no_titulo for v in declarados)


def e_peca_e_nao_aparelho(titulo, entidade):
    """O anuncio e de uma PECA do aparelho, e nao do aparelho.

    Le a CABECA do titulo, como a armadilha 1 da 25.7 manda: o tipo tem de ser
    o objeto, e nao uma palavra perdida no meio. "Tampa Do Filtro Atman
    AT-3338" abre com a peca; "Filtro Canister Atman AT-3338 com tampa" nao.
    """
    if entidade in ENTIDADES_CONSUMIVEIS:
        return False
    cabeca = sem_acento(titulo)[:40]
    return any(p in cabeca for p in NAO_E_O_APARELHO)


def kit_indevido(titulo, registro):
    """"Kit" no titulo quando o registro nao e um kit (armadilha 2 da 25.7).

    Perde-se algum multipack legitimo, e a troca e consciente: quem comprasse
    levaria outra coisa junto, e o cartao da calculadora prometeu um aparelho.
    """
    declara_kit = 'kit' in sem_acento(
        ' '.join(str(registro.get(c) or '') for c in ('modelo', 'variante', 'linha')))
    return (not declara_kit) and re.search(r'(?<![a-z])kit(?![a-z])',
                                           sem_acento(titulo)) is not None


def chave_de_hoje(registro):
    """A palavra-chave que ja esta no banco, extraida da URL crua da busca."""
    url = ((registro.get('afiliado') or {}).get('url_busca_produto') or '')
    if not url:
        return None
    valores = urllib.parse.parse_qs(urllib.parse.urlparse(url).query).get('keyword')
    return valores[0] if valores else None


def escada(registro):
    """Os degraus de palavra-chave, do mais estrito ao mais folgado (25.6).

    Palavra-chave longa devolve zero, e zero nao e erro: a chave de hoje foi
    escrita para a busca do SITE da Shopee, que perdoa, e a API nao perdoa.
    O degrau em que o item casou fica GRAVADO, porque e procedencia.
    """
    marca = (registro.get('marca') or '').strip()
    linha = (registro.get('linha') or '').strip()
    modelo = (registro.get('modelo') or '').strip()
    variante = (registro.get('variante') or '').strip()

    # O codigo sozinho e o degrau 1 so quando ele E um codigo: "Matrix 1 L" nao
    # identifica nada sozinho na Shopee inteira, e gastaria uma chamada para
    # trazer dez anuncios de coisa nenhuma.
    codigo = modelo if re.search(r'\d', modelo) else ''

    degraus = []
    if codigo:
        degraus.append(('1', codigo))
    if marca and codigo:
        degraus.append(('2', '%s %s' % (marca, codigo)))
    if marca and linha and variante:
        degraus.append(('3', '%s %s %s' % (marca, linha, variante)))
    chave = chave_de_hoje(registro)
    if chave:
        degraus.append(('4', chave))

    vistos, unicos = set(), []
    for nome, termo in degraus:
        if termo.lower() in vistos:
            continue
        vistos.add(termo.lower())
        unicos.append((nome, termo))
    return unicos


def casa(oferta, registro, irmaos=()):
    """Este anuncio E este registro? Devolve (True, None) ou (False, motivo).

    A ordem das recusas importa para o relatorio: a primeira que pega e a que
    fica escrita, e ela e a informacao que a proxima passada usa.

    `irmaos` sao os outros registros do MESMO banco. Eles nao entram por
    capricho: e deles que sai a resposta de se a medida precisa estar escrita
    no titulo (ver `medida_discrimina`).
    """
    titulo = oferta.get('titulo') or ''
    entidade = registro.get('entidade') or ''
    marca = registro.get('marca') or ''
    modelo = registro.get('modelo') or ''
    linha = registro.get('linha') or ''

    if not titulo:
        return False, 'anuncio sem titulo'

    if e_peca_e_nao_aparelho(titulo, entidade):
        return False, 'o titulo abre com uma peca do aparelho, nao com o aparelho'

    if kit_indevido(titulo, registro):
        return False, 'o titulo anuncia um kit e o registro nao e um kit'

    # A MARCA E OBRIGATORIA, E A 25.3 EXPLICA POR QUE ELA SOZINHA NAO BASTA:
    # "JBL e som e e aquario, Aquario e roteador e e peixe, Betta e peixe e e
    # movel". Ela entra como condicao necessaria, nunca suficiente.
    #
    # E REGISTRO SEM MARCA NAO RECEBE FICHA, que e o terceiro defeito que este
    # portao pegou em mim. Dois registros deste banco tem `marca: null` de
    # propósito e com o motivo escrito na propria observacao deles — importado
    # revendido com o nome da loja, que o banco chama de *"o pior caso do
    # banco"*. Sem marca, a condicao necessaria da 25.3 simplesmente nao existe,
    # e o que sobraria para identificar o produto seria "Luminaria LED Aquario
    # 60 cm full spectrum", que e a descricao de metade da categoria. Casar isso
    # com um anuncio qualquer seria inventar procedencia — e a camada 1 ja
    # garantiu o piso deles, entao o que se perde aqui e bonus, nao saida de
    # compra.
    if not marca:
        return False, ('o registro nao declara marca, e sem ela nao ha condicao necessaria '
                       'para identificar o anuncio (25.3) — fica so com o piso')
    if not token_no_titulo(marca, titulo):
        return False, 'o titulo nao traz a marca %s' % marca

    # O CODIGO, quando o registro tem um. Aceita o codigo do modelo ou o da
    # linha — "HT-1300/Q3" e "HT-1300" sao a mesma linha escrita com e sem o
    # sufixo de serie.
    # O CODIGO IDENTIFICA A LINHA; a medida identifica a variante DENTRO dela,
    # e quem cobra a medida e o portao logo abaixo. Por isso aqui se pergunta
    # pelo codigo BASE e nao pelo modelo inteiro: exigir "WRGB II Pro 60" como
    # um token so reprova o anuncio que escreve "WRGB II Pro 60cm", que e o
    # anuncio certo — o `60` colado no `cm` perde a fronteira de token.
    #
    # E O CODIGO BASE E O UNICO, NAO UM ENTRE DOIS. A `linha` entrou aqui como
    # alternativa na primeira escrita e furou o portao na hora: a linha do
    # SunSun HW-303B e so "HW", e "HW" esta no titulo do HW-303, do HW-603B e
    # do HW-702A — o portao aprovou o filtro vizinho dizendo que o codigo
    # estava la. Linha nao identifica produto; ela e o sobrenome. So vale como
    # ultimo recurso, quando o registro nao tem modelo nenhum.
    base = codigo_base(registro) or linha
    if base:
        if not token_no_titulo(base, titulo):
            return False, 'o titulo nao traz o codigo (%s)' % base
        extras = sufixos_irmaos(registro, irmaos)
        if variante_depois_do_codigo(base, titulo, extras):
            return False, ('o codigo vem seguido de sufixo que faz outro aparelho'
                           + (' (irmao no banco: %s)' % ', '.join(sorted(extras)) if extras else ''))

    # A MEDIDA — o portao desta ilha. Ver o cabecalho do arquivo.
    medidas = medidas_do_registro(registro)
    if medidas:
        # A MEDIDA CONFLITANTE BARRA SEMPRE, discrimine ela ou nao: um titulo
        # que declara 300 W para o registro de 25 W nao esta calado sobre a
        # medida, esta dizendo outra. Isso e o sinal mais forte de casamento
        # errado que existe, e nao custa nada conferir.
        por_unidade = {}
        for unidade, valor in medidas:
            por_unidade.setdefault(unidade, []).append(valor)
        for unidade, valores in por_unidade.items():
            if medida_conflitante(unidade, valores, titulo):
                return False, ('o titulo declara outra medida em %s (o registro tem %s)'
                               % (unidade, ', '.join('%g' % v for v in valores)))
        # A AUSENCIA da medida so barra quando e ela que separa este registro
        # do vizinho. Ver `medida_discrimina` — a regra nasceu de o portao ter
        # reprovado um casamento certo.
        if medida_discrimina(registro, irmaos):
            if not any(medida_no_titulo(u, v, titulo) for u, v in medidas):
                return False, ('o titulo nao declara a medida do registro (%s), e nesta linha '
                               'e a medida que separa um irmao do outro — sem ela nao ha como '
                               'provar que e esta variante e nao a vizinha'
                               % ', '.join('%g %s' % (v, u) for u, v in medidas))

    return True, None


def dimensao_da_imagem(url):
    """(largura, altura) lidas do cabecalho do arquivo. None se nao der.

    JPEG, PNG e WebP cobrem o que a Shopee serve. Le so o comeco do arquivo: a
    dimensao mora no cabecalho, e baixar 300 KB por foto para ler 4 bytes seria
    gastar rede por nada. Dimensao digitada e a mesma familia do numero de tela
    digitado: parece conferida (25.7).
    """
    try:
        pedido = urllib.request.Request(url, headers={'User-Agent': 'aquametria/1.0'})
        with urllib.request.urlopen(pedido, timeout=30) as r:
            dados = r.read(262144)
    except Exception:
        return None

    if dados[:2] == b'\xff\xd8':                          # JPEG
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

    if dados[:8] == b'\x89PNG\r\n\x1a\n':                 # PNG
        largura, altura = struct.unpack('>II', dados[16:24])
        return largura, altura

    if dados[:4] == b'RIFF' and dados[8:12] == b'WEBP':   # WebP
        formato = dados[12:16]
        if formato == b'VP8X':
            return (int.from_bytes(dados[24:27], 'little') + 1,
                    int.from_bytes(dados[27:30], 'little') + 1)
        if formato == b'VP8 ':
            return (struct.unpack('<H', dados[26:28])[0] & 0x3FFF,
                    struct.unpack('<H', dados[28:30])[0] & 0x3FFF)
    return None


def carregar(caminho):
    with open(os.path.join(RAIZ, caminho), encoding='utf-8') as f:
        return json.load(f)


def gravar_json(caminho, doc):
    with open(os.path.join(RAIZ, caminho), 'w', encoding='utf-8') as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
        f.write('\n')


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    modo = p.add_mutually_exclusive_group(required=True)
    modo.add_argument('--ensaio', action='store_true',
                      help='escreve a proposta em /tmp e nao toca no banco')
    modo.add_argument('--gravar', action='store_true')
    p.add_argument('--so', default=None, help='um id de registro')
    p.add_argument('--limite', type=int, default=0)
    p.add_argument('--so-piso', action='store_true',
                   help='camada 1 apenas: encurta o piso e nao procura ficha')
    args = p.parse_args()

    hoje = datetime.date.today().isoformat()
    docs = {c: carregar(c) for c in BANCOS}
    proposta = []

    registros = []
    for caminho, doc in docs.items():
        irmaos = doc.get('produtos') or []
        for r in irmaos:
            if args.so and r.get('id') != args.so:
                continue
            registros.append((caminho, r, irmaos))
    if args.limite:
        registros = registros[:args.limite]

    for caminho, r, irmaos in registros:
        af = r.get('afiliado') or {}
        linha = {'id': r['id'], 'banco': caminho, 'entidade': r.get('entidade'),
                 'titulo_do_registro': '%s %s' % (r.get('marca') or '', r.get('modelo') or ''),
                 'piso': None, 'ficha': None, 'imagem': None,
                 'degrau_que_casou': None, 'motivo_sem_ficha': None}

        # ------------------------------------------------------------------
        # CAMADA 1 — o piso encurtado. Sem casamento, sem julgamento.
        # ------------------------------------------------------------------
        crua = af.get('url_busca_produto')
        if af.get('url_busca'):
            linha['piso'] = {'ja_tinha': af['url_busca']}
        elif not crua:
            linha['piso'] = {'erro': 'o registro nao tem url_busca_produto'}
        else:
            try:
                linha['piso'] = {'url_busca': shopee.encurtar(crua, SUB_ID)}
            except shopee.ErroDaShopee as erro:
                linha['piso'] = {'erro': str(erro)}
            time.sleep(PAUSA)

        # ------------------------------------------------------------------
        # CAMADA 2 — a ficha e a foto. Aqui mora o risco.
        # ------------------------------------------------------------------
        if not args.so_piso:
            recusas = []
            for nome, termo in escada(r):
                try:
                    ofertas = shopee.buscar(termo, QUANTOS)
                except shopee.ErroDaShopee as erro:
                    recusas.append('degrau %s (%s): %s' % (nome, termo, erro))
                    continue
                time.sleep(PAUSA)
                if not ofertas:
                    recusas.append('degrau %s (%s): zero resultados' % (nome, termo))
                    continue

                aprovados = []
                for o in ofertas:
                    ok, motivo = casa(o, r, irmaos)
                    if ok:
                        aprovados.append(o)
                    else:
                        recusas.append('degrau %s: "%s" — %s'
                                       % (nome, (o.get('titulo') or '')[:70], motivo))

                # ARMADILHA 5 DA 25.7: dois registros no mesmo anuncio, ou dois
                # anuncios para o mesmo registro, sao o mesmo problema — no
                # maximo um esta certo e nao ha como dizer qual. Aqui a saida e
                # diferente da da Robometria: anuncios DISTINTOS do mesmo
                # produto sao o normal do marketplace (tres lojas vendendo o
                # mesmo Roxin), entao o desempate e pela NOTA da loja, que e o
                # unico criterio que a API devolve e que nao e comissao.
                if aprovados:
                    aprovados.sort(key=lambda o: float(o.get('nota') or 0), reverse=True)
                    escolhido = aprovados[0]
                    try:
                        curto = shopee.encurtar(escolhido['url_produto'], SUB_ID)
                    except shopee.ErroDaShopee as erro:
                        recusas.append('encurtar falhou: %s' % erro)
                        break
                    time.sleep(PAUSA)
                    linha['degrau_que_casou'] = nome
                    linha['ficha'] = {
                        'url': curto,
                        'url_produto': escolhido['url_produto'],
                        'anuncio_shopee': escolhido['titulo'],
                        'loja': escolhido.get('loja'),
                        'nota': escolhido.get('nota'),
                        'outros_aprovados': len(aprovados) - 1,
                    }
                    if escolhido.get('imagem_url'):
                        dim = dimensao_da_imagem(escolhido['imagem_url'])
                        if dim:
                            linha['imagem'] = {'url': escolhido['imagem_url'],
                                               'largura': dim[0], 'altura': dim[1],
                                               'fonte': FONTE_DA_IMAGEM}
                        else:
                            linha['imagem'] = {'erro': 'nao foi possivel medir a dimensao'}
                    break
            if not linha['ficha']:
                linha['motivo_sem_ficha'] = recusas[:12] or ['a escada nao produziu candidato']

        proposta.append(linha)
        sys.stderr.write('.')
        sys.stderr.flush()

    sys.stderr.write('\n')

    casaram = [l for l in proposta if l.get('ficha')]
    piso_novo = [l for l in proposta if (l.get('piso') or {}).get('url_busca')]
    com_foto = [l for l in proposta if (l.get('imagem') or {}).get('url')]

    resumo = {
        'gerado_em': hoje, 'sub_id': SUB_ID, 'registros': len(proposta),
        'piso_encurtado_agora': len(piso_novo),
        'piso_ja_tinha': len([l for l in proposta if (l.get('piso') or {}).get('ja_tinha')]),
        'piso_falhou': len([l for l in proposta if (l.get('piso') or {}).get('erro')]),
        'ficha_casou': len(casaram),
        'ficha_nao_casou': len(proposta) - len(casaram),
        'com_foto_medida': len(com_foto),
        'por_degrau': {n: len([l for l in casaram if l['degrau_que_casou'] == n])
                       for n in ('1', '2', '3', '4')},
    }

    if args.ensaio:
        saida = '/tmp/ensaio-shopee-aquametria.json'
        with open(saida, 'w', encoding='utf-8') as f:
            json.dump({'resumo': resumo, 'itens': proposta}, f,
                      ensure_ascii=False, indent=1)
        print(json.dumps(resumo, ensure_ascii=False, indent=1))
        print('\nensaio escrito em %s — NADA foi gravado no banco.' % saida)
        return 0

    # ----------------------------------------------------------------------
    # GRAVACAO
    # ----------------------------------------------------------------------
    por_id = {l['id']: l for l in proposta}
    for caminho, doc in docs.items():
        mexeu = False
        for r in doc.get('produtos') or []:
            l = por_id.get(r.get('id'))
            if not l:
                continue
            af = r.setdefault('afiliado', {})

            piso = l.get('piso') or {}
            if piso.get('url_busca'):
                af['url_busca'] = piso['url_busca']
                af['sub_id_1'] = SUB_ID
                af.pop('motivo_sem_url_busca', None)
                mexeu = True

            # A TRAVA DA 25.2-b: "ausente e diferente de tentado-e-falhou", e
            # essa distincao e a regra inteira. O campo grava a DATA da
            # tentativa, nao um booleano: tentativa de um mes atras nao e a
            # mesma coisa que tentativa de hoje, e um booleano nao sabe dizer.
            af['encurtamento_tentado_em'] = hoje

            ficha = l.get('ficha')
            if ficha:
                af['plataforma'] = 'shopee'
                af['url'] = ficha['url']
                af['url_produto'] = ficha['url_produto']
                af['anuncio_shopee'] = ficha['anuncio_shopee']
                af['rel'] = 'sponsored'
                af['sub_id_1'] = SUB_ID
                af['degrau'] = 3   # anuncio de vendedor comum (25.1)
                af['verificado_em'] = hoje
                af['intestavel'] = False
                af.pop('motivo_sem_url_produto', None)
                af.pop('motivo', None)
                mexeu = True

            img = l.get('imagem') or {}
            # A PREFERENCIA NUNCA INVERTE (25.3): registro que ja tem imagem
            # nao e sobrescrito. A segunda fonte so preenche vazio.
            if img.get('url') and not r.get('imagem'):
                r['imagem'] = {'url': img['url'], 'largura': img['largura'],
                               'altura': img['altura'], 'fonte': img['fonte'],
                               'alt': 'Foto do anuncio de %s %s'
                                      % (r.get('marca') or '', r.get('modelo') or '')}
                mexeu = True

        if mexeu:
            doc['atualizado_em'] = hoje
            gravar_json(caminho, doc)

    print(json.dumps(resumo, ensure_ascii=False, indent=1))
    return 0


if __name__ == '__main__':
    sys.exit(main())
