#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mede a PALAVRA-CHAVE de busca de cada registro publicavel contra a Open API
da Shopee, e desce uma escada ate achar uma que traga a peca certa no topo.

    python3 ferramentas/medir-palavras-chave.py            # mede e imprime
    python3 ferramentas/medir-palavras-chave.py --gravar   # grava a medicao
    python3 ferramentas/medir-palavras-chave.py --so <id>  # um registro so

Credencial: `SHOPEE_APP_ID` e `SHOPEE_SECRET` no AMBIENTE, nunca em arquivo
(secao 25.6 do ARQUIPELAGO.md). Esta ferramenta nao le documento nenhum: quem a
chama ja passou os dois em memoria.

O QUE ELA EXISTE PARA CONSERTAR
-------------------------------
Os itens 1 e 3 do despacho da Sentinela de 16/09/2026. O item 1 mediu que quatro
registros apontavam o botao de compra para uma busca de ZERO resultado; o item 3
mediu que em 9 das 18 palavras-chave o PRIMEIRO resultado nao era a peca pedida
— seis vezes o mesmo robo inteiro. Os dois achados tem a mesma causa e ela ja
estava escrita no contrato antes de ser medida: a secao 26 diz que **o
vocabulario da ilha classifica pela FUNCAO e o fabricante batiza pela POSICAO**.
A palavra-chave de hoje e composta do `tipo` — `escova principal`, `escova
lateral` —, que e vocabulario da ILHA. Nenhum vendedor digita isso. O vendedor
digita o batismo do fabricante: "Escova Central", "Escova Rotativa", "Escova
Direita", "Escova Frontal".

Medido em 16/09/2026 pela Open API: das 18 chaves de hoje, TRES devolvem zero, e
as tres sao `escova principal` — da Electrolux, da Positivo e da WAP. A quarta,
`Xiaomi escova principal`, so sobrevive porque um vendedor de kit por acaso
escreveu a palavra da ilha no titulo.

O ESTREITAMENTO JA TINHA DATA E DONO, E O DIA CHEGOU
-----------------------------------------------------
`esquema-banco.json > afiliado > escada_de_compra > por_que_a_peca_nao_leva_o_codigo`
terminava assim, escrito em 13/09/2026: *"O estreitamento e melhoria, nao
conserto, e ele ja tem data e dono: a Open API da 25.6 (...) No dia em que ela
responder, quem estreita a chave consegue provar que ela traz resultado antes de
gravar."* Este arquivo e esse dia. Nenhuma chave nova entra no banco sem ter sido
CHAMADA antes — e o que ela devolveu fica gravado com a data.

A ESCADA DA BUSCA, e por que os degraus estao nesta ordem
----------------------------------------------------------
Para no primeiro degrau em que o TOPO e a peca do registro. A ordem e de
especificidade decrescente, que e o contrario da escada de coleta da 25.6: la a
pergunta e "este anuncio e este registro?" e o codigo exato ganha; aqui a
pergunta e "esta busca serve o leitor?", e uma busca precisa ter mais de um
resultado para ser busca.

  1. marca + TIPO + contexto ....... a chave de hoje, no vocabulario da ilha.
  2. marca + BATISMO + contexto .... o nome que o FABRICANTE deu a peca, lido da
     cabeca de `nome_na_fonte` e com o nome da marca retirado. Nao e palavra
     inventada: e transcricao de campo do banco. E a traducao da secao 26 para
     dentro da busca.
  3. marca + CODIGO DA PECA + substantivo do tipo ... o esquema supunha, desde
     13/09/2026, que este degrau devolve zero — *"o codigo de peca e SKU
     interno de fabricante e o vendedor de marketplace nao o digita no
     titulo"*. A suposicao estava escrita ao lado da confissao de que nao havia
     como medi-la. Agora ha, e ela e parcialmente FALSA: loja de reposicao
     digita FW008024 e PR10205 no titulo, sim.
  4. marca + CODIGO DO MODELO compativel + substantivo do tipo ... quando nem o
     batismo casa, o que o vendedor digita e o aparelho: "Positivo PRA800
     escova" devolve 4 resultados onde "Positivo Escova Central" devolve 0.
     Tenta TODOS os modelos compativeis publicaveis, nao so o primeiro.
  5. marca + contexto .............. o piso largo. Nao traz a peca no topo e a
     medicao diz isso com todas as letras — mas nao e beco sem saida, e o piso
     da 25.2 e sobre nao haver beco sem saida.

TODO DEGRAU CARREGA O TERMO DE CONTEXTO, E QUEM COBRA ISSO NAO E ESTE ARQUIVO
-----------------------------------------------------------------------------
A primeira versao dos degraus 3 e 4 largava o `robo aspirador` do fim da chave,
porque sem ele a busca devolvia mais resultado. O `validar-banco.py` REPROVOU as
cinco chaves na hora, citando a invariante do esquema: marca sem contexto e
armadilha (25.3), e nesta ilha o CODIGO sem contexto tambem e — `S20` sozinho e
um celular de outra marca. A invariante esta certa e a medicao e que estava
folgada: com o contexto de volta, quatro das cinco chaves continuam vivas e a
quinta desce mais um degrau. Regra de banco reprovando ferramenta nova e a trava
funcionando, nao atrito.

O QUE ELA NUNCA FAZ
-------------------
Nao inventa palavra, igual ao `gerar-busca-de-produto.py`: todo degrau e
composto de campo que ja esta no banco. E nao grava no banco — quem grava e o
`gerar-busca-de-produto.py`, lendo o arquivo que esta aqui produz. A separacao e
de proposito: a medicao depende da rede e do dia, a gravacao tem de ser
deterministica e conferivel sem rede. Com `--encurtar` ela tambem PEDE o link de
afiliado da busca escolhida e o guarda no mesmo arquivo — quem escreve no banco
continua sendo um so.

A REGUA DO TOPO E A MESMA DA COLETA, E ISSO NAO E ECONOMIA
------------------------------------------------------------
`casa_peca` e `abre_com_o_tipo` sao IMPORTADOS de `coletar-shopee.py`, nao
recopiados. A secao 25.7 fechou com a licao de que quatro ferramentas escrevendo
a mesma regra por conta propria foi como esta ilha passou meses emitindo o
espaco vazio da foto sem perguntar nada ao item. Duas reguas de casamento que
divergem em silencio dariam o mesmo resultado: a coleta gravaria uma foto que a
medicao da busca chamaria de errada, e nenhuma das duas estaria obviamente
errada para quem olhasse.
"""
import argparse
import importlib.util
import json
import os
import re
import sys
import urllib.parse
from datetime import date

RAIZ_ILHA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ_REPO = os.path.dirname(os.path.dirname(RAIZ_ILHA))

SAIDA = 'dados/palavras-chave-medidas.json'
QUANTOS = 10
# O ultimo degrau da escada, o `marca + contexto`. Ele tem nome porque a regra
# de preferencia precisa nomea-lo: e o unico degrau que a propria escada declara
# nao servir para trazer a peca no topo, e por isso o unico que perde para um
# criterio mais fraco vindo de um degrau mais estreito.
DEGRAU_DO_PISO_LARGO = 5


def _modulo(caminho, nome):
    """Import de arquivo com hifen no nome. Os dois modulos que esta ferramenta
    precisa se chamam `shopee-api.py` e `coletar-shopee.py`, e hifen nao e nome
    de modulo em Python. Renomear os dois seria mexer em ferramenta que ja
    funciona para agradar o import; carrega-los pelo caminho nao mexe em nada."""
    spec = importlib.util.spec_from_file_location(nome, caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


API = _modulo(os.path.join(RAIZ_REPO, 'ferramentas', 'shopee-api.py'), 'shopee_api')
COLETA = _modulo(os.path.join(RAIZ_ILHA, 'ferramentas', 'coletar-shopee.py'), 'coletar_shopee')

# Onde a cabeca do titulo do fabricante TERMINA. Tudo daqui em diante e o
# aparelho a que a peca serve, nunca o nome da peca: "Escova Rotativa Central
# Electrolux PARA Robos Aspiradores ERB60" -> a peca chama "Escova Rotativa
# Central". A lista mora aqui e nao no esquema de proposito: ela nao e
# vocabulario do banco, e gramatica do portugues do titulo.
FIM_DA_CABECA = ['para', 'p/', 'compativel', 'compativeis', 'original',
                 'originais', 'de reposicao', 'reposicao', '-', '(']


def caminho(rel):
    return os.path.join(RAIZ_ILHA, rel)


def carregar(rel):
    with open(caminho(rel), encoding='utf-8') as fh:
        return json.load(fh)


def _cabeca(nome, nome_de_busca):
    """A cabeca de um nome comercial, cortada em FIM_DA_CABECA e sem a marca.

    E a mesma regra do `batismo_do_fabricante`, extraida para valer nas duas
    entidades: "ObaDuster (Obabox)" -> "ObaDuster". Uma funcao, dois chamadores —
    duas copias da mesma regra divergiriam calado, que e a licao da 25.7.
    """
    nome = (nome or '').strip()
    if not nome:
        return None
    cabeca = []
    for p in re.split(r'\s+', nome):
        limpo = COLETA.sem_acento(p).strip('.,;:')
        if limpo in FIM_DA_CABECA or limpo.startswith('('):
            break
        cabeca.append(p)
    marca_tokens = COLETA.sem_acento(nome_de_busca).split()
    cabeca = [p for p in cabeca
              if COLETA.sem_acento(p).strip('.,;:') not in marca_tokens]
    texto = ' '.join(cabeca).strip(' ,;:-')
    return texto or None


def batismo_do_fabricante(registro, nome_de_busca):
    """A cabeca de `nome_na_fonte`, sem o nome da marca.

    E o unico lugar do banco onde esta escrito como o FABRICANTE chama a peca, e
    a secao 26 diz que e outro nome que o da ilha. Devolve None quando a cabeca
    sai igual ao `tipo` — ai o degrau 2 seria o degrau 1 com outra roupa.
    """
    texto = _cabeca(registro.get('nome_na_fonte'), nome_de_busca)
    if not texto:
        return None
    if COLETA.sem_acento(texto) == COLETA.sem_acento(registro.get('tipo') or ''):
        return None
    return texto


def substantivo_do_tipo(tipo):
    """Delega para a coleta. A funcao morava aqui e desceu para
    `coletar-shopee.py` em 18/09/2026, junto com `palavras_estritas_do_tipo`."""
    return COLETA.substantivo_do_tipo(tipo)


def palavras_estritas_do_tipo(tipo):
    """A lista da coleta MENOS o substantivo pelado, quando o tipo tem
    qualificador. **A REGRA MORA NA COLETA DESDE 18/09/2026** e aqui so se
    chama, porque as duas camadas passaram a precisar da mesma aparagem: la ela
    guarda o caminho do modelo compativel, aqui ela guarda a medicao da chave.

    O texto que justificava a aparagem continua valendo inteiro: a secao 26 diz
    que `lateral` e `principal` sao FUNCOES OPOSTAS, e aprovar uma busca de
    escova principal porque o topo e uma escova frontal (que e lateral) e
    publicar a troca de peca como acerto. Medido: com o substantivo pelado,
    `wap-escova-central-wsmart` "passava" com uma escova frontal no topo.
    """
    return COLETA.palavras_estritas_do_tipo(tipo)


def escada_da_busca(peca, marcas, modelos, contexto):
    marca = marcas.get(peca['marca'], {})
    nome_de_busca = marca.get('nome_de_busca') or marca.get('nome') or peca['marca']
    tipo = (peca.get('tipo') or '').strip()

    degraus = []
    if tipo:
        degraus.append((1, 'marca + tipo + contexto',
                        ' '.join([nome_de_busca, tipo, contexto])))
    batismo = batismo_do_fabricante(peca, nome_de_busca)
    if batismo:
        degraus.append((2, 'marca + batismo do fabricante + contexto',
                        ' '.join([nome_de_busca, batismo, contexto])))
    codigo_da_peca = (peca.get('codigo_fabricante') or '').strip()
    if codigo_da_peca:
        degraus.append((3, 'marca + codigo da peca + substantivo do tipo + contexto',
                        ' '.join([nome_de_busca, codigo_da_peca,
                                  substantivo_do_tipo(tipo), contexto])))
    vistos = set()
    for c in (peca.get('compatibilidade') or []):
        m = modelos.get(c.get('modelo')) or {}
        if (m.get('status') or 'publicavel') != 'publicavel':
            continue
        codigo = (m.get('codigo_fabricante') or '').strip()
        if not codigo or codigo in vistos:
            continue
        vistos.add(codigo)
        degraus.append((4, 'marca + codigo do modelo compativel + substantivo do tipo + contexto',
                        ' '.join([nome_de_busca, codigo,
                                  substantivo_do_tipo(tipo), contexto])))
    degraus.append((5, 'marca + contexto', ' '.join([nome_de_busca, contexto])))
    return nome_de_busca, degraus


def topo_e_a_peca(oferta, peca, modelos, nome_de_busca):
    """O PRIMEIRO resultado e a peca deste registro?

    Tres coisas, e as tres saem da regua da coleta: a marca aparece no titulo, o
    titulo nao troca o objeto (tampa de filtro nao e filtro) e o TIPO e a cabeca
    do titulo. Nao se exige o codigo da peca: quem escolhe uma busca escolhe uma
    vitrine, e vitrine de marca certa com a peca certa na frente e o que o item
    3 do despacho pediu.
    """
    titulo = oferta.get('titulo') or ''
    t = COLETA.sem_acento(titulo)
    if COLETA.sem_acento(nome_de_busca) not in t:
        return False, 'a marca nao aparece no titulo'
    if COLETA.troca_o_objeto(titulo):
        return False, 'o titulo troca o objeto (a peca que cobre a peca)'
    tipo = peca.get('tipo') or ''
    if not COLETA.abre_com_o_tipo(titulo, tipo, palavras_estritas_do_tipo(tipo)):
        if not COLETA.e_acessorio(titulo):
            return False, 'o topo e o aparelho inteiro, nao uma peca'
        return False, 'o tipo da peca nao e a cabeca do titulo'
    return True, 'a marca e o tipo estao no topo'


def criterio_literal_do_despacho(oferta, peca, nome_de_busca):
    """A regua que o item 3 do despacho escreveu, ao pe da letra: *"o primeiro
    resultado contiver a marca E o tipo de peca do registro"*.

    Ela e mais frouxa que a de cima, e a diferenca e exatamente a armadilha 1 da
    25.7: *"Tampa Do Filtro Do Aspirador Robo Multilaser Ho041"* contem a marca
    e contem `filtro`, entao PASSA aqui e REPROVA la. As duas sao impressas lado
    a lado porque o despacho pediu um numero e o contrato cobra o outro, e
    esconder a folga entre os dois seria escolher qual regra citar depois de ver
    o resultado.
    """
    titulo = COLETA.sem_acento(oferta.get('titulo') or '')
    if COLETA.sem_acento(nome_de_busca) not in titulo:
        return False
    # "o tipo de peca DO REGISTRO" — e o tipo do registro e `escova principal`,
    # nao `escova`. A lista estrita e usada tambem aqui porque a alternativa
    # seria contar "Escova Frontal" (que e LATERAL, secao 26) como acerto de uma
    # busca de escova principal, e ai o numero publicado mediria a palavra em vez
    # da funcao.
    return any(p in titulo for p in palavras_estritas_do_tipo(peca.get('tipo') or ''))


def medir(peca, marcas, modelos, contexto, cache):
    nome_de_busca, degraus = escada_da_busca(peca, marcas, modelos, contexto)
    tentativas = []
    escolhido = None
    primeiro_literal = None
    primeiro_com_resultado = None
    for numero, nome, chave in degraus:
        if chave not in cache:
            cache[chave] = API.buscar(chave, quantos=QUANTOS)
        ofertas = cache[chave]
        registro = {
            'degrau': numero,
            'composicao': nome,
            'chave': chave,
            'resultados': len(ofertas),
            'titulo_do_topo': (ofertas[0].get('titulo') if ofertas else None),
            'topo_e_a_peca': False,
            'por_que': 'a busca devolveu zero resultado',
            'criterio_literal_do_despacho': False,
        }
        if ofertas:
            ok, por_que = topo_e_a_peca(ofertas[0], peca, modelos, nome_de_busca)
            registro['topo_e_a_peca'] = ok
            registro['por_que'] = por_que
            registro['criterio_literal_do_despacho'] = criterio_literal_do_despacho(
                ofertas[0], peca, nome_de_busca)
            if primeiro_com_resultado is None:
                primeiro_com_resultado = registro
            if registro['criterio_literal_do_despacho'] and primeiro_literal is None:
                primeiro_literal = registro
            if ok:
                escolhido = registro
        tentativas.append(registro)
        # PARA NO PRIMEIRO DEGRAU QUE SERVE, PELO CRITERIO QUE FOR. A escada esta
        # ordenada por especificidade decrescente, e chave mais especifica que
        # serve o leitor ganha de chave mais larga que tambem serve — sempre.
        #
        # A primeira versao so parava na regua dura e depois escolhia entre os
        # degraus que tinham sobrado. Medido: `wap-escova-direita-w300` passava no
        # criterio do despacho no degrau 2 ("WAP Escova Direita robo aspirador") e
        # ainda assim terminava com "WAP robo aspirador" do degrau 5, porque por
        # acaso o topo do degrau 5 naquele minuto era uma escova frontal. Chave
        # que so serve enquanto o topo de hoje nao mudar nao e chave: e sorte
        # gravada no banco com data.
        #
        # O `or primeiro_literal` SAIU EM 21/09/2026, E A MEDICAO QUE O DERRUBOU
        # ESTA NA LEVA DOS TRES FILTROS DA WAP. Com ele, a escada PARAVA no
        # degrau 1 sempre que a regua frouxa passasse — e o degrau 1 e a chave no
        # vocabulario da ILHA, que e justamente a que a secao 26 diz que o
        # vendedor nao digita. Medido nos tres registros novos, degrau a degrau:
        # `WAP filtro robo aspirador` (d1) devolve no topo *"Kit APZ Aspirador De
        # Robo Filtro De Escova Para Mondial, Multilaser WAP100, etc."* — passa na
        # frouxa (tem `wap` e tem `filtro` no titulo) e reprova na dura; enquanto
        # `WAP Filtro HEPA robo aspirador` (d2) devolve *"Filtro Hepa para Robo
        # Aspirador Wap W310"* e `WAP FW006270 filtro robo aspirador` (d3)
        # devolve *"Filtro Hepa Para Wap Robot W300 - FW006270"*, os dois na
        # regua DURA. A parada no d1 jogava fora um degrau melhor que ja estava
        # medido, e mandava o botao de compra desta ilha abrir num kit de OUTRA
        # marca — que e o defeito 4 da ronda de 18/09 com outra roupa.
        #
        # O QUE ISTO NAO DESFAZ: a trava que o comentario acima descreve. O caso
        # `wap-escova-direita-w300` — literal no d2, dura por ACASO no d5 —
        # continua resolvido, e nao era o `break` que o resolvia: quem o resolve e
        # a linha de preferencia logo abaixo, que devolve o degrau MAIS ESPECIFICO
        # quando os dois criterios apontam para degraus diferentes. O `break` era
        # redundante com ela para aquele caso e destrutivo para este.
        if escolhido:
            break
    # A ORDEM DE PREFERENCIA, e ela e o coracao desta ferramenta. A regua dura
    # da 25.7 (o tipo e a CABECA do titulo) e a regua do item 3 do despacho (o
    # titulo CONTEM a marca e o tipo) respondem a perguntas diferentes, e as
    # duas estao certas na sua. A primeira foi escrita para decidir se um
    # anuncio E este registro, e ai kit misto e engano; a segunda foi escrita
    # para decidir se uma VITRINE serve o leitor, e ai "Kit de Reposicao para
    # Xiaomi S10+: Escova Principal, Escova Lateral, Filtro" no topo de uma
    # busca de escova principal da Xiaomi e exatamente o que o leitor queria
    # ver. Entao a escada tenta a dura, aceita a do despacho, e so cai no
    # "tem resultado" quando nenhuma das duas aparece em degrau nenhum.
    final = escolhido or primeiro_literal or primeiro_com_resultado or tentativas[-1]
    # A PREFERENCIA PELO DEGRAU MAIS ESPECIFICO VALE CONTRA O PISO LARGO, E SO
    # CONTRA ELE (corrigido em 21/09/2026, na mesma leva que derrubou o `break`).
    #
    # Escrita sem essa fronteira, ela dizia "chave mais especifica ganha sempre" e
    # devolvia, nos tres filtros da WAP, o degrau 1 — que passa na regua FROUXA
    # com um kit de outra marca no topo — por cima do degrau 2 e do 3, que passam
    # na regua DURA com o filtro exato do registro no topo. Preferir a chave mais
    # estreita que NAO mostra a peca a uma chave um pouco mais larga que MOSTRA e
    # inverter a pergunta que a 25.7 faz: quem escolhe uma busca escolhe uma
    # vitrine, e vitrine e o que esta na frente dela.
    #
    # O caso que criou esta linha continua coberto, porque ele era sobre o degrau
    # 5: `wap-escova-direita-w300` passava na frouxa no d2 e na dura no d5 por
    # ACASO — o d5 e o piso largo (`marca + contexto`), e a propria escada declara
    # que ele "nao traz a peca no topo". Passar la e sorte do minuto, nao regua,
    # e por isso e o unico degrau que perde para um criterio mais fraco.
    if (escolhido and primeiro_literal
            and escolhido['degrau'] == DEGRAU_DO_PISO_LARGO
            and primeiro_literal['degrau'] < escolhido['degrau']):
        final = primeiro_literal
    return {
        'id': peca['id'],
        'marca': peca['marca'],
        'tipo': peca.get('tipo'),
        'nome_na_fonte': peca.get('nome_na_fonte'),
        'escolhido': final,
        'parou_por': ('o topo e a peca pela regua dura da 25.7' if escolhido else
                      ('nenhum degrau passa na regua dura; ficou o primeiro que passa '
                       'no criterio do item 3 do despacho' if primeiro_literal else
                       ('nenhum degrau passa em criterio nenhum; ficou o primeiro com '
                        'resultado' if primeiro_com_resultado else
                        'NENHUM degrau devolveu resultado'))),
        'tentativas': tentativas,
    }


def encurtar_as_buscas(medidas, pecas, base, sub_id):
    """O ENCURTAMENTO, que ate 16/09/2026 era clique do Raphael.

    A 25.2 chama o link de busca de PISO e diz que ele e o unico elo que a
    maquina fabrica sozinha do comeco ao fim. Ate hoje isso era meia verdade: a
    ESCOLHA da palavra era automatica e o ENCURTAMENTO esperava a sessao logada
    do painel — esta ilha carregava 65 registros com o motivo escrito no campo
    `motivo_sem_url_busca`. A Open API da 25.6 tem `generateShortLink`, aceita
    sub-id, e fecha o elo que faltava.

    So encurta o que MUDOU: chave igual a que ja esta no banco fica com o link
    curto que ja esta no banco. Regerar os 35 gastaria 35 chamadas para trocar 35
    links que funcionam por 35 links equivalentes, e encheria o diff de linhas
    que nao mudaram nada — a mesma razao pela qual `conferido_em` so e reescrito
    quando o degrau muda.
    """
    por_id = {r['id']: r for r in pecas}
    novos = reaproveitados = 0
    for m in medidas:
        escolhido = m['escolhido']
        url = base + urllib.parse.quote(escolhido['chave'])
        escolhido['url_busca_produto'] = url
        afil = (por_id.get(m['id']) or {}).get('afiliado') or {}
        if afil.get('url_busca_produto') == url and (afil.get('url_busca') or '').strip():
            escolhido['url_busca'] = afil['url_busca']
            reaproveitados += 1
            continue
        escolhido['url_busca'] = API.encurtar(url, sub_id)
        novos += 1
    print('encurtamento: %d link(s) novo(s), %d reaproveitado(s) do banco'
          % (novos, reaproveitados))


def medir_modelos(modelos, marcas, contexto, base, sub_id, pecas_e_modelos_no_banco):
    """O MODELO nao desce escada, e a assimetria e antiga e continua certa.

    `gerar-busca-de-produto.py` explica por que: o codigo do modelo E o nome
    comercial do produto — ninguem vende "Electrolux robo aspirador", vende
    ERB60 —, enquanto o codigo de peca e SKU interno. Entao aqui nao ha o que
    escolher: ha o que CONFERIR. A chave e a de sempre, e esta funcao so mede
    quantos resultados ela devolve e pede o link curto de quem ainda nao tem.

    Ela existe porque cinco modelos publicaveis desta ilha entraram no banco
    depois da ultima geracao de link e ficaram com `url_busca` vazia — o piso da
    25.2 aberto, em silencio, enquanto o campo `motivo_sem_url_busca` dizia que
    faltava a sessao logada do Raphael. Nao faltava mais.
    """
    saida = []
    novos = reaproveitados = 0
    for m in modelos:
        marca = marcas.get(m['marca'], {})
        nome_de_busca = marca.get('nome_de_busca') or marca.get('nome') or m['marca']
        codigo = (m.get('codigo_fabricante') or '').strip()
        degraus = [(1, 'marca + codigo do modelo + contexto',
                    ' '.join(p for p in [nome_de_busca, codigo, contexto] if p))]
        # O SEGUNDO DEGRAU DO MODELO, e ele nasceu de um beco sem saida que esta
        # propria ferramenta achou em 16/09/2026, fora do despacho que a pediu:
        # `Multilaser OB010 robo aspirador` devolve ZERO. O codigo do modelo E o
        # nome comercial — menos quando nao e. A Multi vende esse aparelho como
        # ObaDuster, da Obabox, e ninguem anuncia o OB010. A cabeca de `linha`,
        # cortada no parentese e sem o nome da marca, devolve "ObaDuster" e a
        # busca passa a ter tres resultados. Mesma regra da peca, mesmo campo de
        # origem: o nome que o FABRICANTE deu, transcrito do banco.
        linha = _cabeca(m.get('linha') or m.get('nome_comercial') or '', nome_de_busca)
        if linha and COLETA.sem_acento(linha) != COLETA.sem_acento(codigo):
            degraus.append((2, 'marca + cabeca da linha comercial + contexto',
                            ' '.join(p for p in [nome_de_busca, linha, contexto] if p)))

        escolhido = None
        tentativas = []
        for numero, composicao, chave in degraus:
            ofertas = API.buscar(chave, quantos=QUANTOS)
            tentativas.append({'degrau': numero, 'composicao': composicao,
                               'chave': chave, 'resultados': len(ofertas),
                               'titulo_do_topo': (ofertas[0].get('titulo')
                                                  if ofertas else None)})
            if ofertas:
                escolhido = tentativas[-1]
                break
        passo = escolhido or tentativas[0]
        numero, composicao, chave = passo['degrau'], passo['composicao'], passo['chave']
        ofertas = [] if passo['resultados'] == 0 else [{'titulo': passo['titulo_do_topo']}]
        url = base + urllib.parse.quote(chave)
        afil = (pecas_e_modelos_no_banco.get(m['id']) or {}).get('afiliado') or {}
        if afil.get('url_busca_produto') == url and (afil.get('url_busca') or '').strip():
            curto = afil['url_busca']
            reaproveitados += 1
        else:
            curto = API.encurtar(url, sub_id)
            novos += 1
        saida.append({
            'id': m['id'], 'marca': m['marca'], 'tipo': None, 'nome_na_fonte': None,
            'escolhido': {
                'degrau': numero, 'composicao': composicao,
                'chave': chave, 'resultados': passo['resultados'],
                'titulo_do_topo': passo['titulo_do_topo'],
                'topo_e_a_peca': None,
                'por_que': ('o codigo do modelo E o nome comercial' if numero == 1
                            else 'o codigo devolveu zero: quem vende chama pela linha'),
                'criterio_literal_do_despacho': None,
                'url_busca_produto': url, 'url_busca': curto,
            },
            'parou_por': ('entidade MODELO_ROBO: o codigo bastou' if numero == 1
                          else 'entidade MODELO_ROBO: o codigo devolveu zero e a '
                               'linha comercial respondeu'),
            'tentativas': tentativas,
        })
    print('modelos: %d medido(s), %d link(s) novo(s), %d reaproveitado(s)'
          % (len(saida), novos, reaproveitados))
    return saida


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--gravar', action='store_true')
    p.add_argument('--encurtar', action='store_true',
                   help='gera o link de afiliado da busca escolhida (exige --gravar)')
    p.add_argument('--so', action='append', default=[])
    args = p.parse_args()

    esquema = carregar('dados/esquema-banco.json')
    escada = esquema['tipos_compostos']['afiliado']['escada_de_compra']
    contexto = escada['termo_de_contexto_por_entidade']['peca']

    marcas = {r['id']: r for r in carregar('dados/marcas.json')['registros']}
    modelos = {r['id']: r for r in carregar('dados/modelos-robo.json')['registros']}
    pecas = carregar('dados/pecas.json')['registros']

    alvo = [r for r in pecas if r.get('status') == 'publicavel'
            and (not args.so or r['id'] in args.so)]

    # ---------------------------------- A CHAVE FIXADA NO NAVEGADOR NAO SE REMEDE
    #
    # As duas reguas desta ilha discordam NO SENTIDO QUE ENGANA, e isso esta
    # medido: em 18/09/2026 esta ferramenta deu como boas as 25 chaves Roborock e
    # Xiaomi do banco — `com a marca no topo`, 25 de 25 — enquanto a busca do SITE,
    # medida no navegador, abria num Xiaomi em 5 das 6 chaves de modelo Roborock.
    # Ela mede o catalogo de OFERTAS que paga comissao; o leitor ve outra coisa.
    #
    # Entao a chave que o navegador fixou (`aplicar-chaves-do-navegador.py`) e
    # COPIADA daqui em vez de remedida. Sem isto, a primeira passada desta
    # ferramenta com a credencial no ambiente desfaria, em silencio e com cara de
    # medicao fresca, o conserto de 20/09 — e o despacho que o mandou fazer proibe
    # justamente isso com todas as letras: *"NAO remeca as chaves pela Open API de
    # ofertas para decidir nada"*. Regra que so vale ate alguem rodar a ferramenta
    # errada nao e regra.
    try:
        anterior_doc = carregar(SAIDA)
    except FileNotFoundError:
        anterior_doc = {}
    anterior = {r['id']: r for r in anterior_doc.get('registros', [])}
    fixadas = {i: r for i, r in anterior.items()
               if ((r.get('escolhido') or {}).get('fixada_no_navegador'))}

    cache = {}
    medidas = []
    for peca in alvo:
        if peca['id'] in fixadas:
            medidas.append(fixadas[peca['id']])
            continue
        medidas.append(medir(peca, marcas, modelos, contexto, cache))
    if fixadas:
        print('%d chave(s) fixada(s) no navegador: copiadas, nao remedidas '
              '(despacho do Raphael de 20/09/2026)' % len(fixadas))

    print('%-46s %4s %3s %-4s %-4s %s' % ('REGISTRO','DEG','N','ITEM3','25.7','TOPO'))
    for m in medidas:
        e = m['escolhido']
        print('%-46s %4s %3d %-4s %-4s %s' % (
            m['id'][:46],
            'nav' if e.get('fixada_no_navegador') else e['degrau'],
            e['resultados'] or 0,
            'sim' if e['criterio_literal_do_despacho'] else 'NAO',
            'sim' if e['topo_e_a_peca'] else 'nao',
            (e['titulo_do_topo'] or '(zero resultado)')[:58]))

    chaves = {}
    for m in medidas:
        chaves.setdefault(m['escolhido']['chave'], []).append(m)
    vivas = [k for k, v in chaves.items() if v[0]['escolhido']['resultados'] > 0]
    com_peca = [k for k, v in chaves.items() if v[0]['escolhido']['topo_e_a_peca']]
    literal = [k for k, v in chaves.items()
               if v[0]['escolhido']['criterio_literal_do_despacho']]

    print('')
    print('PALAVRAS-CHAVE DISTINTAS ........................ %d' % len(chaves))
    print('  com resultado (o piso da 25.2 de pe) .......... %d de %d' % (len(vivas), len(chaves)))
    print('  com a PECA no topo (regua da 25.7) ............ %d de %d' % (len(com_peca), len(chaves)))
    print('  criterio LITERAL do item 3 do despacho ........ %d de %d' % (len(literal), len(chaves)))
    print('REGISTROS PUBLICAVEIS ........................... %d' % len(medidas))
    print('  com resultado ................................. %d' % sum(
        1 for m in medidas if m['escolhido']['resultados'] > 0))
    print('  com a PECA no topo ............................ %d' % sum(
        1 for m in medidas if m['escolhido']['topo_e_a_peca']))

    if args.encurtar:
        # O ENCURTAMENTO ALCANCA A CHAVE FIXADA, e tem de alcancar: ele nao DECIDE
        # chave nenhuma, so pede o link de afiliado da chave que ja esta escolhida.
        # E exatamente a divida que o despacho de 20/09 deixou aberta quando a
        # credencial faltou no ambiente daquele dia.
        encurtar_as_buscas(medidas, pecas, escada['base_da_busca'], 'robometria')
        for m in medidas:
            e = m.get('escolhido') or {}
            if e.get('fixada_no_navegador') and e.get('url_busca'):
                e['motivo_sem_url_busca'] = None
        no_banco = {r['id']: r for r in pecas}
        no_banco.update({r['id']: r for r in
                         carregar('dados/modelos-robo.json')['registros']})
        alvo_modelos = [r for r in carregar('dados/modelos-robo.json')['registros']
                        if r.get('status') == 'publicavel'
                        and (not args.so or r['id'] in args.so)]
        medidas = medidas + medir_modelos(
            alvo_modelos, marcas,
            escada['termo_de_contexto_por_entidade']['modelo_robo'],
            escada['base_da_busca'], 'robometria', no_banco)

    if args.gravar:
        # ---------------------------------------------------------------
        # `--so` MEDE UM PEDACO E GRAVA O ARQUIVO INTEIRO (21/09/2026).
        #
        # Ate hoje a gravacao escrevia `medidas` — a lista do que ESTA passada
        # mediu — por cima do arquivo. Com `--so`, isso apagava a medicao de
        # todos os outros registros, e o estrago nao era teorico nem silencioso
        # por muito tempo: medindo os quatro filtros desta leva com
        # `--so`, o arquivo caiu de 95 registros para 4 e levou junto as 26
        # CHAVES FIXADAS NO NAVEGADOR — exatamente o conserto de 20/09 que o
        # bloco acima protege com tres paragrafos. Na passada seguinte
        # `gerar-busca-de-produto.py` reescreveu 34 chaves do banco pela
        # composicao padrao e 30 registros perderam o link curto, porque para
        # ele um registro fora da medicao e um registro nunca medido.
        #
        # A regra: quem mede um PEDACO grava o pedaco DENTRO do arquivo, nunca
        # no lugar dele. Sem `--so` nada muda — a lista medida e o arquivo.
        if args.so:
            por_id = {m['id']: m for m in medidas}
            gravados = [por_id.pop(r['id'], r)
                        for r in (anterior_doc.get('registros') or [])]
            gravados += [m for m in medidas if m['id'] in por_id]
        else:
            gravados = medidas

        # AS CONTAGENS SAO DO ARQUIVO, NAO DA PASSADA. A tela acima conta o que
        # esta execucao mediu; o cabecalho conta o que fica gravado, que e a
        # invariante que o validar-banco.py cobra dos dois arquivos de banco e
        # que aqui nao existia por nao haver, ate hoje, diferenca entre as duas.
        chaves_g = {}
        for m in gravados:
            chaves_g.setdefault(m['escolhido']['chave'], []).append(m)
        vivas_g = [k for k, v in chaves_g.items() if v[0]['escolhido']['resultados'] > 0]
        com_peca_g = [k for k, v in chaves_g.items() if v[0]['escolhido']['topo_e_a_peca']]
        literal_g = [k for k, v in chaves_g.items()
                     if v[0]['escolhido']['criterio_literal_do_despacho']]

        doc = {
            'id': 'palavras-chave-medidas',
            'ilha': 'robometria',
            'entidade': 'MEDICAO',
            'publicar': False,
            'gerado_em': date.today().isoformat(),
            'gerado_por': 'ferramentas/medir-palavras-chave.py',
            'fonte_da_medicao': 'Open API de Afiliados da Shopee (productOfferV2), '
                                'secao 25.6 do ARQUIPELAGO.md',
            'nota_de_universo': (
                'A API de afiliado e o catalogo de OFERTAS do programa, e nao a busca do '
                'site que o leitor ve. As duas discordam e a discordancia foi medida em '
                '16/09/2026: `WAP escova lateral robo aspirador` devolve zero na busca do '
                'site (medida pela Sentinela no Chrome do Raphael) e dez aqui. A busca do '
                'site NAO e mensuravel desta nuvem — `/api/v4/search/search_items` '
                'devolve `error 90309999, redirect_to_error_page` e a pagina de busca '
                'serve casca de JavaScript identica byte a byte para palavras diferentes. '
                'Entao esta medicao prova o que prova: que a chave existe no catalogo que '
                'PAGA comissao. Chave com zero AQUI e pior que chave com zero la.'),
            'escada': [
                {'degrau': 0,
                 'composicao': 'fora da escada: chave medida na busca do SITE, no navegador'},
                {'degrau': 1, 'composicao': 'marca + tipo + contexto'},
                {'degrau': 2, 'composicao': 'marca + batismo do fabricante + contexto'},
                {'degrau': 3, 'composicao': 'marca + codigo da peca + substantivo do tipo + contexto'},
                {'degrau': 4, 'composicao': 'marca + codigo do modelo compativel + substantivo do tipo + contexto'},
                {'degrau': 5, 'composicao': 'marca + contexto'},
            ],
            # CADA NUMERO DESTA CONTAGEM DIZ DE QUE UNIVERSO ELE SAI, e a licao
            # e do item 2 do mesmo despacho que pediu esta ferramenta: `71 pares`
            # ao lado de `38 modelos` sao dois numeros certos contando universos
            # diferentes na mesma frase. A primeira versao daqui chamava de
            # `registros_publicaveis` um numero que valia 73 — peca MAIS modelo —
            # enquanto as quatro chaves acima falavam so de PECA, e a tela da
            # propria ferramenta imprimia 35. Errar do mesmo jeito no mesmo dia
            # em que se conserta o erro e o motivo de ele estar escrito aqui.
            'contagem': {
                'palavras_chave_distintas_de_peca': len(chaves_g),
                'com_resultado': len(vivas_g),
                'com_a_peca_no_topo': len(com_peca_g),
                'criterio_literal_do_despacho': len(literal_g),
                'com_a_marca_no_topo': sum(
                    1 for e in {m['escolhido']['chave']: m['escolhido']
                                for m in gravados if m.get('tipo')}.values()
                    if e.get('marca_no_topo')),
                'registros_de_peca': len([m for m in gravados if m.get('tipo')]),
                'registros_medidos': len(gravados),
                'medidos_nesta_passada': len(medidas),
                'chaves_fixadas_no_navegador': sum(
                    1 for m in gravados
                    if (m.get('escolhido') or {}).get('fixada_no_navegador')),
            },
            'fontes_da_medicao': sorted(set(
                (anterior_doc.get('fontes_da_medicao') or []))),
            'atualizado_em': anterior_doc.get('atualizado_em'),
            'registros': gravados,
            'nota_das_contagens': (
                'As contagens acima sao de PECA. Registros de MODELO_ROBO entram na '
                'lista com `topo_e_a_peca` nulo de proposito: a pergunta do item 3 do '
                'despacho e sobre peca, e modelo nao desce escada (ver medir_modelos).'),
        }
        with open(caminho(SAIDA), 'w', encoding='utf-8') as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=1)
            fh.write('\n')
        print('\ngravado: %s' % SAIDA)
    return 0


if __name__ == '__main__':
    sys.exit(main())
