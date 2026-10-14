#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A REGUA DA LISTA DE CONSULTAS DE PRODUTO — o que a lista pode afirmar.

Nao e portao. E a regua que tres arquivos carregam: `validar-consultas-de-produto.py`
(o portao sobre o arquivo de verdade), `teste-consultas-de-produto.py` (a bancada,
sobre casos sinteticos) e `gerar-consultas-de-produto.py` (a producao, que escreve o
`.md`). Mora num arquivo proprio pelo motivo que esta ilha ja pagou varias vezes:
regua escrita duas vezes erra em um dos lados, e o lado errado fica verde.

POR QUE ELA NASCEU EM 14/10/2026
--------------------------------
Item 1 do DESPACHO DO RAPHAEL de 09/10/2026, que estende a secao 30 do contrato a
esta ilha: *"Montar em dados/consultas-de-produto.md a lista das consultas de
produto do aquarismo (...), em ordem de intencao de compra, cada uma com a SERP
classificada pela regua nova e as URLs do top 10."* A regua nova e a **30.5**.

E O INSTRUMENTO DESTA NUVEM E UM SO, e ele e quem decide tudo o que esta escrito
aqui: o egresso responde 403 no CONNECT para todo dominio fora da lista de
permitidos, e ninguem abre o site de ninguem daqui. O que existe e **BUSCA** — o
mesmo nivel 3 da escada de coleta com que este banco inteiro foi construido, e o
mesmo instrumento que a `regua-prospeccao.py` declarou em 24/09/2026.

A ASSIMETRIA, QUE E A UNICA REGRA IMPORTANTE DESTE ARQUIVO
-----------------------------------------------------------
A 30.5 define TOMADA como um fato POSITIVO: *"Tomada e quando o top 10 e dominado
por varejo grande, fabricante forte ou fazenda de conteudo com pagina dedicada
aquela consulta."* E define ALVO, pela 14.9, como a AUSENCIA desses ocupantes.

**Busca sabe afirmar presenca, nunca ausencia.** Entao esta regua emite dois
vereditos e nao tres:

  `tomada`      — fato positivo, medido: os ocupantes que a busca devolveu JA sao
                  dominados por pagina dedicada de varejo grande, fabricante forte
                  ou fazenda de conteudo. Isto se afirma, porque e presenca.
  `nao-medida`  — tudo o mais. Inclui o caso em que a busca devolveu lojinha,
                  anuncio solto, agregador e site estrangeiro: isso **nao prova**
                  que o top 10 brasileiro do Google nao tem varejo grande, prova
                  que a busca nao o mostrou.

**`alvo` NAO EXISTE NESTA REGUA, e a ausencia dele e o conteudo.** O veredito
`alvo` autoriza gastar rastreamento de dominio e URL nova, e a 14.9 diz o que
custa errar nele: *"Publicar ali e gastar rastreamento de dominio novo para
estacionar na pagina 4."* Quem quiser `alvo` abre a SERP com os olhos — no Chrome
do Raphael, que e o unico instrumento do arquipelago que ve a SERP brasileira — e
escreve `serp_vista_por` na linha. Sem isso a lista nunca diz "pode nascer".

O ERRO QUE ISTO EVITA, MEDIDO NA PROPRIA PASSADA QUE ESCREVEU A REGUA: em
14/10/2026 a busca neutra de `luminaria de LED para aquario plantado` devolveu
NOVE ocupantes, oito deles estrangeiros (ukaps.org, greenaqua.hu,
charterhouse-aquatics.com, natureaquariums.com, aquariumsupplyonline.com). Lido
como SERP brasileira, aquilo e uma busca vazia pedindo pagina nova. Medido com a
pergunta certa — a busca enviesada que NOMEIA o varejo, logo abaixo — a Cobasi
tem `/c/peixes/equipamentos-e-acessorios/iluminacao`, pagina de categoria
dedicada, e o Mercado Livre tem cinco listagens. A consulta mais parecida com
"aberta" das doze era a que o varejo grande ja ocupa.

A BUSCA ENVIESADA, E POR QUE ELA E LEGITIMA
-------------------------------------------
Uma busca que NOMEIA `Cobasi Petz Mercado Livre` dentro da consulta nao mede a
SERP: ela mede se aquelas lojas tem pagina dedicada aquela familia de produto.
Isso e evidencia de **presenca** e so pode empurrar o veredito para `tomada` ou
para o aviso `varejo_grande_com_pagina_dedicada`. **Nunca** pode sustentar
`nao-medida` virando "aberta", e nunca entra na contagem de dominancia dos
ocupantes neutros. O campo `enviesada: true` na evidencia e obrigatorio quando a
consulta do instrumento nomeia loja, e o portao cobra isso.

AS QUATRO TRAVAS DE FATO
------------------------
  1. O VEREDITO NAO SE ESCREVE, SE CALCULA — `veredito()` sai dos ocupantes
     medidos. A lista diz o veredito e o portao RECALCULA; se discordarem, fica
     vermelho. Mesma doenca que a `bancada.py` matou um andar acima.
  2. `nasce_agora` TAMBEM SE CALCULA, e de QUATRO portoes independentes (30.5 via
     veredito, 30.2 via banco, 30.4 via pagina que ja serve, e 14.9 via SERP
     vista com os olhos). Nenhum deles se escreve a mao.
  3. OCUPANTE SEM URL NAO EXISTE. A 30.5 termina dizendo: *"Todo veredito
     continua escrito com as URLs do top 10 que o sustentam."* Ocupante e uma URL
     com classe e com a consulta que o produziu, ou e opiniao.
  4. `dedicada_a_consulta` E `true` OU `null`, nunca `false`. Dizer que a pagina
     do Hopar 1800 L/h na Cobasi NAO e dedicada a `filtro canister para aquario`
     e leitura de slug, e leitura de slug erra; dizer que nao foi medido e
     verdade. E so `true` conta para dominancia, entao `null` ja e conservador.
"""

# ---------------------------------------------------------------------------
# AS CLASSES DE OCUPANTE, e o que cada uma faz com o veredito.
# ---------------------------------------------------------------------------
# A 30.5 e explicita nas duas direcoes. O que CONTA para tomada:
#   "varejo grande, fabricante forte ou fazenda de conteudo com pagina dedicada
#    aquela consulta"
# O que NAO conta, e nao conta "sozinhos nem somados":
#   "lojinha pequena do nicho, anuncio solto de marketplace, Pinterest, YouTube,
#    forum e blog antigo"
# `calculadora-concorrente` nasceu nesta passada e nao esta na lista da 30.5: e
# uma pagina dedicada a consulta, de quem faz o que esta ilha faz. Ela conta,
# porque e exatamente o ocupante que a 14.9 manda olhar antes de publicar.
# `fora-do-brasil` nao conta e nao e defeito do site: e defeito do instrumento,
# e esta contado a parte justamente para ficar visivel quando a busca derivou.
CLASSES_QUE_TOMAM = (
    'varejo-grande',
    'fabricante-forte',
    'fazenda-de-conteudo',
    'calculadora-concorrente',
)
CLASSES_QUE_NAO_TOMAM = (
    'lojinha-do-nicho',
    'anuncio-marketplace',
    'agregador-de-ofertas',
    'forum',
    'video',
    'blog-antigo',
    'rede-social',
    'desconhecido',
)
CLASSE_FORA = 'fora-do-brasil'
CLASSES = CLASSES_QUE_TOMAM + CLASSES_QUE_NAO_TOMAM + (CLASSE_FORA,)

FORMAS = ('cabeca', 'parametrica', 'modelo')
INTENCOES = ('alta', 'media', 'baixa')
VEREDITOS = ('tomada', 'nao-medida')
INSTRUMENTOS = ('busca', 'navegador', 'curl')

# O PISO DE OCUPANTE BRASILEIRO PARA A CONTAGEM VALER. Com menos de quatro
# ocupantes no Brasil entre os devolvidos, a busca derivou para fora e a amostra
# nao sustenta veredito nenhum — nem `tomada`. Quatro e o numero em que a
# dominancia por metade deixa de poder ser decidida por um ocupante unico.
PISO_DE_OCUPANTES_BR = 4

# O PISO DE PRODUTO REAL DA 30.2: "A pagina nasce com 3 ou mais produtos reais
# colhidos assim, mais 1 numero proprio".
PISO_DE_PRODUTOS_30_2 = 3


def ocupantes_br(consulta):
    """Os ocupantes que NAO sao de fora do Brasil. A base de toda contagem."""
    return [o for o in consulta.get('ocupantes', []) if o.get('classe') != CLASSE_FORA]


def ocupantes_que_tomam(consulta):
    """Os ocupantes que a 30.5 deixa contar para `tomada`.

    Duas condicoes, e as duas vem da letra da 30.5: a classe tem de ser uma das
    que tomam, E a pagina tem de ser **dedicada aquela consulta**. Pagina de UM
    modelo numa loja grande nao e pagina dedicada a consulta de familia — e por
    isso que a Cobasi aparece sete vezes nesta lista e toma duas consultas.
    """
    return [o for o in ocupantes_br(consulta)
            if o.get('classe') in CLASSES_QUE_TOMAM and o.get('dedicada_a_consulta') is True]


def veredito(consulta):
    """O veredito CALCULADO. Nunca o escrito no arquivo.

    Dois valores, pela assimetria do cabecalho deste arquivo: `tomada` e um fato
    positivo e se afirma; a ausencia dele nao se afirma, e chama `nao-medida`.
    """
    br = ocupantes_br(consulta)
    if len(br) < PISO_DE_OCUPANTES_BR:
        return 'nao-medida'
    if len(ocupantes_que_tomam(consulta)) * 2 >= len(br):
        return 'tomada'
    return 'nao-medida'


def serp_vista_com_olhos(consulta):
    """Alguem abriu a SERP brasileira desta consulta?

    E o unico caminho para `nasce_agora`. `serp_vista_por` nomeia QUEM viu, e
    `serp_vista_em` quando — ausencia e reprovacao, nao omissao tolerada, pela
    mesma porta dos fundos que o portao do espelho do CDN fechou em 24/09/2026.
    """
    return bool(consulta.get('serp_vista_por')) and bool(consulta.get('serp_vista_em'))


def nasce_agora(consulta):
    """A pagina desta consulta pode nascer nesta ilha, hoje?

    QUATRO portoes independentes, e a pagina nasce so com os quatro abertos.
    Devolve (bool, motivo). O motivo e do PRIMEIRO portao fechado, na ordem em
    que o contrato os poe, e vai para a tela: lista que diz `nao` sem dizer por
    que vira lista que a proxima passada reabre do zero.
    """
    if veredito(consulta) == 'tomada':
        return False, '30.5/14.9: SERP tomada por pagina dedicada de varejo grande, fabricante forte, fazenda de conteudo ou calculadora concorrente'
    if not serp_vista_com_olhos(consulta):
        return False, '14.9: "ANTES de criar a pagina, olhe a SERP" — e a busca desta nuvem nao ve a SERP brasileira; falta `serp_vista_por`'
    if consulta.get('pagina_da_ilha_que_ja_serve'):
        return False, '30.4: a consulta ja e servida por %s, que e reforcada em vez de ganhar URL nova' % consulta['pagina_da_ilha_que_ja_serve']
    if (consulta.get('produtos_reais_no_banco') or 0) < PISO_DE_PRODUTOS_30_2:
        return False, '30.2: a pagina nasce com %d ou mais produtos reais colhidos de anuncio, e o banco tem %d' % (
            PISO_DE_PRODUTOS_30_2, consulta.get('produtos_reais_no_banco') or 0)
    return True, 'os quatro portoes abertos: SERP vista com os olhos e nao tomada, consulta nao servida por pagina da ilha, e lastro de banco'


def erros_de_evidencia(consulta, rotulo):
    """As afirmacoes sobre a lista de evidencia de UMA consulta."""
    erros = []
    evidencias = consulta.get('evidencia')
    if not isinstance(evidencias, list) or not evidencias:
        return ['%s: sem lista de evidencia' % rotulo]
    neutras = 0
    for i, ev in enumerate(evidencias):
        onde = '%s evidencia[%d]' % (rotulo, i)
        instrumento = ev.get('medido_como')
        if instrumento not in INSTRUMENTOS:
            erros.append('%s: instrumento desconhecido (%r)' % (onde, instrumento))
        elif instrumento != 'busca' and not ev.get('medido_por'):
            erros.append('%s: %r sem `medido_por`; esta nuvem nao tem esse instrumento' % (onde, instrumento))
        if not ev.get('consulta_do_instrumento'):
            erros.append('%s: sem a consulta que a produziu' % onde)
        if not ev.get('medido_em'):
            erros.append('%s: sem data' % onde)
        if ev.get('enviesada') not in (True, False):
            # Ausencia nao vale como `false`: e justamente a busca enviesada que
            # nao pode entrar na contagem, e campo que pode faltar cria o estado
            # em que ninguem sabe se ela entrou.
            erros.append('%s: `enviesada` tem de ser true ou false, nunca ausente' % onde)
        elif ev.get('enviesada') is False and nomeia_loja(ev.get('consulta_do_instrumento') or ''):
            erros.append('%s: a consulta nomeia loja e a evidencia se declara neutra' % onde)
        if ev.get('enviesada') is False:
            neutras += 1
    if not neutras:
        erros.append('%s: nenhuma evidencia neutra; busca enviesada nao mede SERP' % rotulo)
    return erros


# As lojas cuja mencao dentro da consulta a torna enviesada. Nomear a loja na
# consulta e perguntar "esta loja tem pagina disto?", que e outra pergunta.
LOJAS_QUE_ENVIESAM = (
    'cobasi', 'petz', 'mercado livre', 'mercadolivre', 'shopee', 'amazon',
    'magazine luiza', 'magalu', 'americanas', 'casas bahia', 'extra',
    'zoom', 'buscape', 'buscapé',
)


def nomeia_loja(texto):
    """A consulta do instrumento nomeia uma loja? Entao ela e enviesada."""
    t = (texto or '').lower()
    return any(loja in t for loja in LOJAS_QUE_ENVIESAM)


def erros_de_ocupantes(consulta, rotulo):
    """As afirmacoes sobre a lista de ocupantes de UMA consulta."""
    erros = []
    ocupantes = consulta.get('ocupantes')
    if not isinstance(ocupantes, list) or not ocupantes:
        return ['%s: sem ocupantes; a 30.5 exige as URLs que sustentam o veredito' % rotulo]
    consultas_declaradas = {ev.get('consulta_do_instrumento') for ev in consulta.get('evidencia', [])}
    enviesada_por_consulta = {ev.get('consulta_do_instrumento'): ev.get('enviesada')
                              for ev in consulta.get('evidencia', [])}
    for i, o in enumerate(ocupantes):
        onde = '%s ocupante[%d]' % (rotulo, i)
        if not o.get('url'):
            erros.append('%s: sem URL' % onde)
        if not o.get('titulo'):
            erros.append('%s: sem titulo do resultado' % onde)
        if o.get('classe') not in CLASSES:
            erros.append('%s: classe desconhecida (%r)' % (onde, o.get('classe')))
        if o.get('dedicada_a_consulta') not in (True, None):
            erros.append('%s: `dedicada_a_consulta` e true ou null, nunca %r' % (onde, o.get('dedicada_a_consulta')))
        vinda_de = o.get('vinda_da_consulta')
        if not vinda_de:
            erros.append('%s: nao diz de que consulta do instrumento veio' % onde)
        elif vinda_de not in consultas_declaradas:
            erros.append('%s: veio de %r, que nao esta na evidencia' % (onde, vinda_de))
        elif enviesada_por_consulta.get(vinda_de) is True and o.get('classe') != CLASSE_FORA:
            # A trava central: ocupante colhido por busca enviesada nao entra na
            # contagem de dominancia, entao nao pode entrar na lista de ocupantes.
            # O lugar dele e `varejo_grande_com_pagina_dedicada`, que e aviso e
            # nao contagem.
            erros.append('%s: veio de busca ENVIESADA (%r) e ocupante so entra por busca neutra' % (onde, vinda_de))
    return erros


def erros_da_consulta(consulta, rotulo):
    """Tudo o que UMA linha da lista pode ter de errado."""
    erros = []
    for campo in ('id', 'consulta', 'familia'):
        if not consulta.get(campo):
            erros.append('%s: sem `%s`' % (rotulo, campo))
    if consulta.get('forma') not in FORMAS:
        erros.append('%s: forma desconhecida (%r)' % (rotulo, consulta.get('forma')))
    if consulta.get('intencao_de_compra') not in INTENCOES:
        erros.append('%s: intencao de compra desconhecida (%r)' % (rotulo, consulta.get('intencao_de_compra')))
    if not consulta.get('por_que_a_intencao'):
        erros.append('%s: a intencao de compra e JUIZO e tem de vir escrita' % rotulo)
    produtos = consulta.get('produtos_reais_no_banco')
    if not isinstance(produtos, int) or produtos < 0:
        erros.append('%s: `produtos_reais_no_banco` tem de ser inteiro contado, nao %r' % (rotulo, produtos))
    if consulta.get('varejo_grande_com_pagina_dedicada') not in (True, None):
        erros.append('%s: `varejo_grande_com_pagina_dedicada` e true ou null, nunca %r' % (
            rotulo, consulta.get('varejo_grande_com_pagina_dedicada')))
    erros += erros_de_evidencia(consulta, rotulo)
    erros += erros_de_ocupantes(consulta, rotulo)
    # O veredito e o `nasce_agora` escritos tem de bater com os calculados.
    escrito = consulta.get('veredito')
    if escrito not in VEREDITOS:
        erros.append('%s: veredito fora do vocabulario (%r). `alvo` nao existe nesta regua' % (rotulo, escrito))
    else:
        calculado = veredito(consulta)
        if escrito != calculado:
            erros.append('%s: veredito escrito %r e calculado %r' % (rotulo, escrito, calculado))
    nasce_escrito = consulta.get('nasce_agora')
    if nasce_escrito not in (True, False):
        erros.append('%s: `nasce_agora` tem de ser true ou false' % rotulo)
    else:
        nasce_calc, _ = nasce_agora(consulta)
        if nasce_escrito != nasce_calc:
            erros.append('%s: `nasce_agora` escrito %r e calculado %r' % (rotulo, nasce_escrito, nasce_calc))
    return erros


def erros(dados):
    """Todos os erros do arquivo. Lista vazia = portao verde."""
    e = []
    # `o_que_nao_foi_medido` entrou nesta lista pela mutacao 15, que SOBREVIVEU na
    # primeira passada: a lista do que nao foi medido podia ser apagada inteira e
    # o portao ficava verde. "Nao medido" apagado e lido como zero, que e a
    # doenca que a secao 4 do contrato nomeia.
    for campo in ('esquema', 'versao', 'ilha', 'atualizado_em', 'o_que_este_arquivo_e',
                  'o_instrumento_desta_passada', 'por_que_alvo_nao_existe',
                  'o_que_nao_foi_medido'):
        if not dados.get(campo):
            e.append('cabecalho: sem `%s`' % campo)
    consultas = dados.get('consultas')
    if not isinstance(consultas, list) or not consultas:
        return e + ['sem lista de consultas']
    vistos = set()
    for c in consultas:
        rotulo = c.get('id') or '<sem id>'
        if rotulo in vistos:
            e.append('%s: id repetido' % rotulo)
        vistos.add(rotulo)
        e += erros_da_consulta(c, rotulo)
    return e


# ---------------------------------------------------------------------------
# O LASTRO DE BANCO SE RECONTA, NAO SE LE
# ---------------------------------------------------------------------------
# Nasceu da mutacao 11 de `mutacoes-consultas-de-produto.py`, que SOBREVIVEU na
# primeira passada: inflar `produtos_reais_no_banco` de 0 para 9 na linha do CO2
# nao mudava nada, porque aquela linha ja estava fechada por outro portao e o
# numero nao era conferido contra nada. Lido ao pe da letra, o campo era um
# numero DIGITADO no meio de um arquivo cujo cabecalho inteiro existe para dizer
# que numero de tela nasce contado. Agora ele se reconta dos
# `dados/produtos-*.json`, e o portao fica vermelho quando os dois discordam.
BANCO_POR_FAMILIA = {
    'filtro': 'produtos-filtro.json',
    'aquecedor': 'produtos-aquecedor.json',
    'iluminacao': 'produtos-iluminacao.json',
    'midia': 'produtos-midia.json',
}
# As familias que o despacho do Raphael nomeia e o banco desta ilha NAO tem.
# Elas valem zero CONTADO, nao zero suposto: a ausencia do arquivo e a contagem.
FAMILIAS_SEM_BANCO = ('bomba', 'substrato', 'co2', 'teste-de-agua', 'termostato')


def contar_no_banco(consulta, pasta_dados):
    """Quantos produtos REAIS, colhidos de anuncio, esta consulta tem no banco.

    A 30.2 pede *"3 ou mais produtos reais colhidos assim"*, e "assim" e anuncio
    de marketplace com fonte e data — nesta ilha, `afiliado.anuncio_shopee`.
    Registro sem anuncio colhido nao conta: ele e uma ficha de fabricante, que a
    30.2 trata como dado TECNICO e nao como produto real a vender.

    Para `forma: modelo` o lastro e do registro nomeado em `registro_do_banco`,
    nunca da familia: a pagina de UM modelo nao se sustenta nos irmaos dele.
    Devolve None quando nao ha como contar, e `None` nunca vira zero.
    """
    import json as _json
    import os as _os
    familia = consulta.get('familia')
    arquivo = BANCO_POR_FAMILIA.get(familia)
    if arquivo is None:
        return 0 if familia in FAMILIAS_SEM_BANCO else None
    caminho = _os.path.join(pasta_dados, arquivo)
    if not _os.path.exists(caminho):
        return None
    with open(caminho, encoding='utf-8') as f:
        produtos = _json.load(f).get('produtos', [])
    if consulta.get('forma') == 'modelo':
        alvo = consulta.get('registro_do_banco')
        if not alvo:
            return None
        return sum(1 for p in produtos
                   if p.get('id') == alvo and (p.get('afiliado') or {}).get('anuncio_shopee'))
    return sum(1 for p in produtos if (p.get('afiliado') or {}).get('anuncio_shopee'))


def erros_do_banco(dados, pasta_dados):
    """O lastro escrito bate com o recontado? Lista de mensagens."""
    e = []
    for c in dados.get('consultas', []):
        rotulo = c.get('id') or '<sem id>'
        if c.get('forma') == 'modelo' and not c.get('registro_do_banco'):
            e.append('%s: `forma: modelo` exige `registro_do_banco` para o lastro poder ser recontado' % rotulo)
            continue
        contado = contar_no_banco(c, pasta_dados)
        if contado is None:
            e.append('%s: familia %r sem banco conhecido; o lastro nao pode ser recontado' % (
                rotulo, c.get('familia')))
        elif contado != c.get('produtos_reais_no_banco'):
            e.append('%s: `produtos_reais_no_banco` escrito %r e recontado %d no banco' % (
                rotulo, c.get('produtos_reais_no_banco'), contado))
    return e


def erros_do_arquivo(dados, md_no_disco=None, pasta_dados=None):
    """TODOS os erros do arquivo de verdade, regra do `.md` incluida.

    Mora aqui, e nao dentro do `validar-...py`, pelo motivo deste arquivo
    existir: regra escrita duas vezes erra em um dos lados. O portao chama isto,
    e as `mutacoes-...py` chamam ISTO MESMO — entao mutacao nao pode passar por
    uma regra que o portao tem e ela nao ve.

    `md_no_disco=None` desliga a comparacao do texto, que e o que as mutacoes de
    DADO precisam: quase toda mutacao muda o texto gerado, e deixar a regra
    ligada esconderia a causa verdadeira atras de "difere do que a regua gera".
    """
    e = list(erros(dados))
    if pasta_dados is not None:
        e += erros_do_banco(dados, pasta_dados)
    for c in dados.get('consultas', []):
        rotulo = c.get('id') or '<sem id>'
        if veredito(c) == 'tomada' and not ocupantes_que_tomam(c):
            e.append('%s: veredito `tomada` sem um ocupante que tome' % rotulo)
        if c.get('nasce_agora') is True and not serp_vista_com_olhos(c):
            e.append('%s: diz que nasce agora sem `serp_vista_por`' % rotulo)
    if md_no_disco is not None and md_no_disco != render_md(dados):
        e.append('dados/consultas-de-produto.md difere do que a regua gera do JSON '
                 '(editado a mao?); rode `gerar-consultas-de-produto.py`')
    return e


# ---------------------------------------------------------------------------
# O `.md` E GERADO, NUNCA ESCRITO
# ---------------------------------------------------------------------------
# Duas fontes para o mesmo fato divergem. A lista tem UMA fonte (o JSON) e o
# `.md` sai dela por esta funcao; o portao regera em memoria e compara, entao
# `.md` editado a mao fica vermelho.
ROTULO_VEREDITO = {
    'tomada': 'SERP TOMADA — medido, e a pagina NAO nasce (14.9)',
    'nao-medida': 'SERP NAO MEDIDA — a busca desta nuvem nao ve a SERP brasileira',
}

ORDEM_INTENCAO = {'alta': 0, 'media': 1, 'baixa': 2}


def ordenada(consultas):
    """A ordem da lista: intencao de compra primeiro, como o despacho pediu.

    *"em ordem de intencao de compra"*. Empate: a consulta TOMADA desce, porque
    a lista existe para dizer onde trabalhar e nao onde nao trabalhar. Empate
    ainda: o lastro de banco maior primeiro, que e o que a 30.2 cobra. E por
    fim o id, para a ordem ser estavel entre passadas.
    """
    return sorted(consultas, key=lambda c: (
        ORDEM_INTENCAO.get(c.get('intencao_de_compra'), 9),
        0 if veredito(c) == 'nao-medida' else 1,
        -(c.get('produtos_reais_no_banco') or 0),
        c.get('id') or '',
    ))


def render_md(dados):
    """O `.md` inteiro, a partir do JSON. Mesma fonte, uma so."""
    L = []
    A = L.append
    A('# CONSULTAS DE PRODUTO DA AQUAMETRIA — item 1 do despacho do Raphael de 09/10/2026')
    A('')
    A('> **ARQUIVO GERADO por `ferramentas/gerar-consultas-de-produto.py` a partir de**')
    A('> **`dados/consultas-de-produto.json`. Nao edite a mao:** o portao')
    A('> `validar-consultas-de-produto.py` regera este texto e compara, e edicao a')
    A('> mao fica vermelha. Mude o JSON e rode o gerador.')
    A('')
    A('- Ilha: **%s** · versao do esquema **%s** · atualizado em **%s**' % (
        dados['ilha'], dados['versao'], dados['atualizado_em']))
    A('- Regua: **secao 30.5** do `ARQUIPELAGO.md`, com a 14.9, a 30.2 e a 30.4 nos outros tres portoes.')
    A('')
    A('## O que este arquivo e')
    A('')
    A(dados['o_que_este_arquivo_e'])
    A('')
    A('## O instrumento desta passada, e o que ele nao alcanca')
    A('')
    A(dados['o_instrumento_desta_passada'])
    A('')
    A('## POR QUE O VEREDITO `alvo` NAO APARECE NENHUMA VEZ NESTE ARQUIVO')
    A('')
    A(dados['por_que_alvo_nao_existe'])
    A('')

    consultas = ordenada(dados['consultas'])
    tomadas = [c for c in consultas if veredito(c) == 'tomada']
    nascem = [c for c in consultas if nasce_agora(c)[0]]
    A('## O placar, contado e nao digitado')
    A('')
    A('| | |')
    A('|---|---|')
    A('| consultas na lista | **%d** |' % len(consultas))
    A('| SERP **tomada**, medido — nao nascem | **%d** |' % len(tomadas))
    A('| SERP **nao medida** — esperam olhos na SERP brasileira | **%d** |' % (len(consultas) - len(tomadas)))
    A('| com aviso de varejo grande com pagina dedicada | **%d** |' % sum(
        1 for c in consultas if c.get('varejo_grande_com_pagina_dedicada') is True))
    A('| **nascem agora** | **%d** |' % len(nascem))
    A('| ocupantes de SERP registrados com URL | **%d** |' % sum(len(c.get('ocupantes', [])) for c in consultas))
    A('')

    A('## A lista, em ordem de intencao de compra')
    A('')
    for c in consultas:
        nasce, motivo = nasce_agora(c)
        A('### `%s`' % c['consulta'])
        A('')
        A('- **id:** `%s` · **familia:** %s · **forma:** %s' % (c['id'], c['familia'], c['forma']))
        A('- **intencao de compra:** %s — %s' % (c['intencao_de_compra'], c['por_que_a_intencao']))
        A('- **veredito da SERP:** %s' % ROTULO_VEREDITO[veredito(c)])
        if c.get('varejo_grande_com_pagina_dedicada') is True:
            A('- **AVISO:** varejo grande TEM pagina dedicada a esta familia — %s' % c['onde_o_varejo_tem_pagina'])
        A('- **lastro de banco (30.2):** %d produtos reais colhidos de anuncio' % c['produtos_reais_no_banco'])
        if c.get('pagina_da_ilha_que_ja_serve'):
            A('- **30.4 — a ilha ja serve esta consulta por:** `%s`%s' % (
                c['pagina_da_ilha_que_ja_serve'],
                ' — ' + c['ressalva_da_30_4'] if c.get('ressalva_da_30_4') else ''))
        A('- **SERP vista com os olhos:** %s' % (
            '%s em %s' % (c['serp_vista_por'], c['serp_vista_em']) if serp_vista_com_olhos(c)
            else '**nao** — ninguem abriu a SERP brasileira desta consulta'))
        A('- **nasce agora:** %s — %s' % ('**SIM**' if nasce else 'nao', motivo))
        if c.get('observacao'):
            A('- **nota:** %s' % c['observacao'])
        A('')
        A('**Ocupantes que a busca neutra devolveu** (a 30.5 exige as URLs que sustentam o veredito):')
        A('')
        A('| # | classe | dedicada a consulta | titulo | URL |')
        A('|---|---|---|---|---|')
        for i, o in enumerate(c['ocupantes'], 1):
            A('| %d | %s | %s | %s | %s |' % (
                i, o['classe'],
                'sim' if o.get('dedicada_a_consulta') is True else 'nao medido',
                o['titulo'].replace('|', '\\|'), o['url']))
        A('')
        A('**Evidencia:**')
        A('')
        for ev in c['evidencia']:
            A('- `%s` · %s · %s · %s' % (
                ev['consulta_do_instrumento'], ev['medido_como'], ev['medido_em'],
                'ENVIESADA (nomeia loja; so afirma presenca)' if ev.get('enviesada') else 'neutra'))
        A('')

    A('## O que esta lista NAO mede, dito como nao medido e nao como zero')
    A('')
    for linha in dados['o_que_nao_foi_medido']:
        A('- %s' % linha)
    A('')
    return '\n'.join(L) + '\n'
