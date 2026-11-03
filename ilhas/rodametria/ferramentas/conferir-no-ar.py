#!/usr/bin/env python3
"""
CONFERE A ILHA NO AR — o portao que a secao 8 do ARQUIPELAGO.md exige por escrito.

    "Depois de publicar, busque a URL no ar e confira com numero medido:
     (1) HTTP 200; (2) zero entidades &#038; DENTRO de <script>; (3) o corpo
     comeca pelo texto e nao por metadado; (4) o script vem do rodape e a tabela
     de exemplos aparece no HTML servido; (5) a revisao aplicada bate com a do
     manifest."

Mais o que as outras secoes cobram e que esta ilha tinha de herdar pronto:
  - a PORTA DE ENTRADA da 29.2 (robots.txt em text/plain, wp-sitemap.xml em
    application/xml, wp-json em application/json, e caminho virgem em 404);
  - a ROTA QUE MEDE A PORTA POR DENTRO, da 29.3, lida SEM o token: ela existe
    no indice de rotas, nega quem nao tem token, e o CODIGO da negativa prova
    que a parede achou a fonte do token e comparou. Nasceu em 03/11/2026, com
    a rota, e reprovou contra o ar ANTES do desembarque — quatro falhas, as
    quatro certas;
  - o PORTAO DO DESEMBARQUE da 20.4: o log do /status e lido LINHA POR LINHA e
    nenhuma linha da revisao corrente pode deixar de dizer `ok`. Resumo verde
    nao e entrega;
  - a 20.5: revisao atrasada com log de AGORA e cache do GitHub, nao defeito —
    e o portao diz qual dos dois e, em vez de reprovar os dois igual;
  - a 20.4 OUTRA VEZ, por outro caminho (02/11/2026): a VERSAO que o WordPress
    carregou de cada snippet, lida em `/casca` -> `versoes`, contra o campo
    `versao` do manifest. O sha256 e sobre o byte do repositorio e NAO alcanca
    snippet `gravado mas NAO ativado`; o `id` que falta no /casca e esse defeito,
    e o portao diz "nao ativado" e "versao diferente" separados, porque o
    conserto das duas nao e o mesmo;
  - a 32.4: zero palavra de bastidor da fabrica no texto servido;
  - a 32.5 pede medicao a 390 px num navegador de verdade, e ISSO NAO E AQUI:
    quem faz e `conferir-32-5-no-navegador.mjs` (a copiar do modelo da
    clubedomosaico quando esta ilha tiver molde em mais de uma pagina). Este
    portao mede o que se mede no HTML servido, e DIZ que nao mediu pixel —
    aprovar em silencio o que nao se mediu e o defeito que a 32.5-b nomeou.

TODA URL E PEDIDA COM QUEBRA DE CACHE: as afirmacoes aqui sao sobre a ORIGEM.
Quem le como o Google le, sem quebra de cache, e outro portao.
"""

# A FUNCAO VEM COM NOME PROPRIO, E NAO O MODULO: `import html` seria SOMBREADO
# dentro do laco, porque a variavel que guarda o corpo da pagina tambem se chama
# `html` (a linha do `cod, ct, html = buscar(...)`) — e a chamada ao modulo
# morreria com AttributeError na PRIMEIRA description medida. Nenhuma LEITURA
# pega isso: o nome existe, certinho, nos dois lugares. Quem pegou foi perguntar
# ao arquivo quem MAIS usa o nome, antes de empurrar.
from html import unescape as desescapar_entidades
import json
import os
import re
import sys
import urllib.error
import urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)
DOMINIO = "https://rodametria.com.br"

falhas = []
registros = []
afirmacoes = 0


def afirma(cond, msg):
    global afirmacoes
    afirmacoes += 1
    if not cond:
        falhas.append(msg)


def registro(msg):
    registros.append(msg)


def buscar(caminho, v=True):
    url = DOMINIO + caminho
    if v:
        url += ("&" if "?" in caminho else "?") + "v=" + str(int(__import__("time").time()))
    req = urllib.request.Request(url, headers={
        "User-Agent": "rodametria-conferir/1.0",
        "Accept-Encoding": "identity",
    })
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            return r.status, r.headers.get("Content-Type", ""), r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("Content-Type", ""), e.read().decode("utf-8", "replace")
    except Exception as e:
        return 0, "", "ERRO: %s" % e


def corpo_da_pagina(html):
    """So o CORPO, nunca o HTML completo.

    A secao 8: "afirmacao sobre o que a pagina diz se mede no CORPO, nunca no
    HTML completo" — a trava que achava o texto dentro do proprio JSON-LD e
    passava ate com resposta inventada.
    """
    m = re.search(r"<body[^>]*>(.*)</body>", html, re.S | re.I)
    corpo = m.group(1) if m else html
    corpo = re.sub(r"<script.*?</script>", " ", corpo, flags=re.S | re.I)
    corpo = re.sub(r"<style.*?</style>", " ", corpo, flags=re.S | re.I)

    return corpo


REV_RE = re.compile(r"revis\w*\s+(\d+)\s*:")


def linhas_da_revisao(log, n):
    """Devolve (linha de FECHO da revisao n, [linhas de ITEM dela]).

    O LOG VEM DO MAIS NOVO PARA O MAIS VELHO, E A LINHA DE FECHO E ESCRITA POR
    ULTIMO — entao ela aparece ANTES dos itens que resume. A primeira versao
    desta regua supunha o contrario, com estas palavras no comentario: "cada
    revisao COMECA com a linha `revisao N:`. As linhas desta entrega sao as que
    vao do topo ate essa linha, inclusive." Com o fecho no topo, esse corte
    devolvia UMA linha — a de fecho — e o portao imprimia "1 da revisao 29, 0
    linha de falha nesta entrega".

    MEDIDO EM 02/11/2026 as 17h4xZ, no desembarque da revisao 29: o log tinha 15
    linhas, a revisao 29 tinha 1 linha de fecho e 8 de item, e o portao leu 1.
    As 8 linhas de item NUNCA foram lidas por ele — e linha de item e justamente
    onde mora `gravado (#13) mas NAO ativado`, o defeito que a 20.4 existe para
    pegar e que custou SETE paginas na clubedomosaico duas vezes em tres dias.

    E A IRONIA E EXATA: a 20.4 diz "a revisao do /status E O RESUMO, E RESUMO
    VERDE NAO E ENTREGA". O portao escrito para cobrar isso estava lendo SO O
    RESUMO, e dizia "lido linha por linha" ao fazer isso. As execucoes de 30/10
    e das 14h14Z de hoje escreveram "as 7 linhas" e "as 5 linhas da revisao
    corrente dizendo ok" — numeros que saiam de leitura A MAO, nao deste portao,
    que nas duas vezes tinha lido 1.
    """
    inicio = None
    for k, l in enumerate(log):
        m = REV_RE.search(l)
        if m and int(m.group(1)) == n:
            inicio = k
            break
    if inicio is None:
        return None, []
    itens = []
    for l in log[inicio + 1:]:
        if REV_RE.search(l):
            break
        itens.append(l)
    return log[inicio], itens


def aplicados_declarados(fecho):
    """Quantos itens a LINHA DE FECHO diz ter aplicado, ou None.

    E a regua que fecha o buraco de verdade: o fecho declara um numero, e o
    portao conta as linhas que leu. Se a janela do log rolou e levou itens, a
    conta nao fecha e o portao DIZ isso, em vez de aprovar com cara de completo
    sobre as linhas que sobraram.
    """
    m = re.search(r"(\d+)\s+aplicado", fecho or "")
    return int(m.group(1)) if m else None


ROTA_DA_293 = "/rodametria/v1/rotas"


def codigo_do_erro(bruto):
    """O campo `code` do JSON de erro do WordPress, ou None se nao for um."""
    try:
        d = json.loads(bruto)
    except Exception:
        return None

    return d.get("code") if isinstance(d, dict) else None


def problemas_da_parede(rotas_no_indice, cod_sem_token, cod_token_errado, code_errado):
    """A rota da 29.3 lida DE FORA, sem nunca ter o token.

    E FUNCAO PURA DE PROPOSITO, e e isso que faz o `--autoteste` poder fabricar
    os tres mundos que esta nuvem nao consegue produzir de verdade: a rota
    AUSENTE, a parede ABERTA e o PORTAO MORTO. Portao de rede cujo autoteste
    precisa de rede nao roda (20.8).

    A AFIRMACAO FORTE E A DO `code`, e ela e POSITIVA. Procurar "nao deu 200" e
    a leitura pelo avesso que a 20.8 nomeia: ela aprova um 404 e aprova uma
    casca que nega TODO pedido porque nao acha o token. O que prova que a
    parede esta VIVA e `rodametria_rotas_token_invalido` — esse codigo so sai
    depois de a casca achar a fonte do token E rodar o `hash_equals`. Ele e
    legivel sem o token, e e por isso que esta ilha o tem (ver a divergencia
    (b) da secao 12 da casca: o Sync dela nao esta no repositorio, entao o nome
    da fonte do token foi herdado e nao conferido no chao).
    """
    p = []

    if ROTA_DA_293 not in rotas_no_indice:
        p.append("29.3: %s NAO aparece no indice de rotas do WordPress — esta casca nao registra a rota que mede a porta de entrada por dentro"
                 % ROTA_DA_293)

    if 404 in (cod_sem_token, cod_token_errado):
        p.append("29.3: a rota respondeu 404 — ela nao existe neste site, e a porta de entrada segue sem instrumento (foi essa falta que custou QUATRO DIAS de ar na robometria)")

    if 200 in (cod_sem_token, cod_token_errado):
        p.append("29.3: A PAREDE ESTA ABERTA — a rota devolveu 200 SEM o token do Sync, e ela mostra o retrato do roteamento do servidor")

    if code_errado == "rodametria_rotas_sem_fonte_de_token":
        p.append("29.3: PORTAO MORTO — a casca nao achou de onde ler o token do Sync, entao a rota nega TODO pedido, inclusive o certo. O nome da funcao ou da option do token esta errado nesta ilha")
    elif code_errado != "rodametria_rotas_token_invalido":
        p.append("29.3: com token ERRADO a rota devia dizer `rodametria_rotas_token_invalido` e disse %r — sem esse codigo nao existe prova, desta nuvem, de que a parede achou a fonte do token e comparou"
                 % (code_errado,))

    if cod_token_errado != 401:
        p.append("29.3: com token errado a rota respondeu %s e tinha de responder 401 — o `status` vai EXPLICITO no WP_Error porque sem ele o WordPress devolve 500"
                 % (cod_token_errado,))

    return p


def main():
    manifest = json.load(open(os.path.join(ILHA, "manifest.json"), encoding="utf-8"))
    revisao_esperada = int(manifest["revisao"])

    # -------------------------------------------------------------------
    # 1. A PORTA DE ENTRADA (29.2). Ela cai sozinha, sem nenhum portao
    #    acusar, e foi assim que o Clube do Mosaico passou nove dias fora.
    # -------------------------------------------------------------------
    porta = (
        ("/robots.txt", "text/plain"),
        ("/wp-sitemap.xml", "xml"),
        ("/wp-json/", "application/json"),
    )
    for caminho, tipo in porta:
        cod, ct, _ = buscar(caminho)
        afirma(cod == 200, "29.2: %s respondeu %s, nao 200" % (caminho, cod))
        afirma(tipo in ct, "29.2: %s veio como %r e tinha de ser %r" % (caminho, ct, tipo))

    virgem = "/caminho-que-nunca-existiu-%d/" % int(__import__("time").time())
    cod, _, _ = buscar(virgem, v=False)
    afirma(cod == 404, "29.2: caminho virgem respondeu %s e tinha de ser 404" % cod)

    # -------------------------------------------------------------------
    # 1-b. A ROTA QUE MEDE A PORTA POR DENTRO (29.3). Ela nasceu nesta ilha
    #      em 03/11/2026, e a divida era de nascimento: a varredura do
    #      despacho de 02/11 listou esta ilha com `NAO` nesta coluna, ao lado
    #      da aquametria. A robometria pagou QUATRO DIAS fora do ar por nao
    #      te-la — em 30/10 o despacho escreveu "nao e consertavel pelo
    #      repositorio", e era verdade sobre aquela ilha e falso sobre o
    #      Arquipelago.
    #
    #      O QUE ESTE PORTAO CONSEGUE PROVAR SEM O TOKEN, que nao esta no
    #      repositorio e nao deve estar: que a rota EXISTE, que a parede
    #      NEGA, e — pelo codigo de erro — que a parede negou depois de achar
    #      a fonte do token e comparar. O reparo em si nao e exercitavel
    #      daqui, e isso esta dito em vez de maquiado.
    # -------------------------------------------------------------------
    _, _, indice = buscar("/wp-json/rodametria/v1")
    try:
        rotas_no_indice = sorted(json.loads(indice).get("routes", {}).keys())
    except Exception:
        rotas_no_indice = []

    cod_sem, _, _ = buscar("?rest_route=/rodametria/v1/rotas")
    cod_err, _, corpo_err = buscar("?rest_route=/rodametria/v1/rotas&token=token-de-proposito-errado")
    code_err = codigo_do_erro(corpo_err)

    for problema in problemas_da_parede(rotas_no_indice, cod_sem, cod_err, code_err):
        afirma(False, problema)

    # A LINHA DE REGISTRO DIZ O QUE FOI MEDIDO, NUNCA O VEREDITO. A primeira
    # versao dela dizia "a rota esta registrada" — e imprimia isso tambem no
    # mundo em que a rota devolvia 404 e NAO estava registrada. Registro que
    # afirma o que nao mediu e a familia do comentario que declara um
    # mecanismo: parece conferido e nao mede nada (32.5-d). Quem decide aqui
    # sao as afirmacoes acima.
    registro("29.3: %s %s no indice; sem token -> %s; token errado -> %s com `%s` (a parede medida de fora, sem o token)"
             % (ROTA_DA_293,
                "PRESENTE" if ROTA_DA_293 in rotas_no_indice else "AUSENTE",
                cod_sem, cod_err, code_err))

    # -------------------------------------------------------------------
    # 2. O /status E O PORTAO DO DESEMBARQUE (20.4 e 20.5)
    # -------------------------------------------------------------------
    cod, _, bruto = buscar("/wp-json/rodametria/v1/status")
    afirma(cod == 200, "/status respondeu %s" % cod)
    if cod != 200:
        return encerrar()

    st = json.loads(bruto)
    revisao_no_ar = int(st.get("revisao", -1))
    log = st.get("log", [])
    ultimo = str(st.get("ultimo", ""))

    if revisao_no_ar < revisao_esperada:
        # 20.5: cache do GitHub, ou Sync que nao rodou? Quem decide e o log.
        afirma(False,
               "o manifest esta na revisao %d e o /status esta na %d. O ultimo log e de %s — "
               "pela 20.5, log recente aqui significa CACHE do GitHub (reacione de dois em dois) "
               "e log antigo significa que o Sync NAO RODOU."
               % (revisao_esperada, revisao_no_ar, ultimo))
        return encerrar()

    afirma(revisao_no_ar == revisao_esperada,
           "o /status esta na revisao %d e o manifest na %d" % (revisao_no_ar, revisao_esperada))

    # O LOG LINHA POR LINHA, E SO AS LINHAS DA REVISAO CORRENTE.
    #
    # A 20.4 e literal: "a execucao le as linhas da REVISAO CORRENTE no log do
    # /status, e nenhuma pode deixar de dizer `ok`". Duas versoes anteriores
    # desta regua erraram, cada uma para um lado, e as duas estao registradas
    # porque as duas sao licao:
    #
    #   (1) a primeira lia a JANELA INTEIRA e reprovou a entrega de 29/10 por
    #       causa de quatro linhas `FALHA manifest: HTTP 404` de 28/10 — de
    #       antes de o manifest existir, ou seja a historia de um defeito ja
    #       consertado. Regua que reprova entrega certa e o caminho mais curto
    #       para alguem passar a ignora-la (20.5), e a janela e append-only:
    #       ela SEMPRE vai carregar o passado.
    #   (2) a segunda cortou do topo ate a linha de fecho, supondo que a
    #       revisao COMECA por ela. O log vem do mais novo para o mais velho e
    #       o fecho e escrito por ULTIMO: ele esta no TOPO do grupo. O corte
    #       devolvia 1 linha — o RESUMO — e o portao chamava isso de "lido
    #       linha por linha". Medido no desembarque da revisao 29, em 02/11.
    #
    # AGORA O PORTAO NAO ACREDITA NA PROPRIA CONTAGEM: a linha de fecho DECLARA
    # quantos itens foram aplicados, e as linhas lidas tem de ser esse numero.
    # Janela que rolou e levou item deixa a conta aberta, e aberta ela e dita.
    fecho, itens_da_revisao = linhas_da_revisao(log, revisao_no_ar)
    afirma(fecho is not None,
           "20.4: o log do /status nao tem a linha de fecho da revisao %d — a janela pode "
           "ter rolado, e entrega sem linha de fecho nao foi conferida" % revisao_no_ar)

    declarados = aplicados_declarados(fecho)
    afirma(declarados is not None,
           "20.4: a linha de fecho da revisao %d nao declara quantos itens aplicou (%r) — sem "
           "esse numero o portao nao tem contra o que conferir o que leu" % (revisao_no_ar, fecho))
    afirma(declarados is None or len(itens_da_revisao) == declarados,
           "20.4: a linha de fecho da revisao %d declara %s item(ns) aplicado(s) e o log traz %d "
           "linha(s) de item. A janela e append-only e tem teto: item que rolou para fora dela "
           "NAO foi conferido, e aprovar sobre o que sobrou e aprovar com cara de completo"
           % (revisao_no_ar, declarados, len(itens_da_revisao)))

    # A AFIRMACAO E POSITIVA DE PROPOSITO: "nenhuma pode deixar de dizer `ok`".
    # Procurar palavra de falha (FALHA, erro, NAO) e a leitura pelo avesso, e ela
    # so pega as falhas que alguem ja imaginou. Linha de item com redacao nova
    # que nao diz `ok` passaria calada — e e exatamente assim que
    # `gravado (#13) mas NAO ativado` chegou ao ar duas vezes.
    muda = [l for l in itens_da_revisao if not re.search(r"\bok\b", l)]
    afirma(not muda,
           "20.4: a revisao %d tem %d linha(s) de item que NAO dizem `ok`: %s"
           % (revisao_no_ar, len(muda), muda))
    registro("20.4: log lido linha por linha — janela de %d linha(s); a revisao %d declara %s "
             "item(ns) aplicado(s) e as %d linha(s) de item dela foram lidas uma por uma, "
             "todas dizendo `ok`"
             % (len(log), revisao_no_ar, declarados, len(itens_da_revisao)))

    antigas = [l for l in log if l not in itens_da_revisao and l != fecho
               and ("FALHA" in l or "erro" in l.lower())]
    if antigas:
        registro("20.4: a janela do log carrega %d linha(s) de FALHA de revisoes ANTERIORES, e "
                 "elas nao sao desta entrega: %s" % (len(antigas), antigas[:2]))
    if len(log) >= 15:
        registro("20.4: a janela do log tem %d linhas e esta CHEIA — item de revisao ANTERIOR "
                 "que rolou para fora dela nao foi conferido por ninguem. Registro, nao "
                 "aprovacao. (Os itens DESTA entrega estao conferidos pela conta do fecho.)"
                 % len(log))

    # -------------------------------------------------------------------
    # 3. A CASCA INSTALOU AS PAGINAS QUE DIZ TER INSTALADO
    # -------------------------------------------------------------------
    cod, _, bruto = buscar("/wp-json/rodametria/v1/casca")
    afirma(cod == 200, "/casca respondeu %s — a casca nao esta ativa no ar" % cod)
    urls = {}
    if cod == 200:
        c = json.loads(bruto)
        registro("casca %s instalada em %s"
                 % (c.get("versao_casca"), (c.get("instalado") or {}).get("em")))

        # ---------------------------------------------------------------
        # 3b. A VERSAO QUE O WORDPRESS CARREGOU, E A AUSENCIA E O SINAL
        #     (02/11/2026)
        #
        # O `sha256` do manifest e sobre o BYTE do repositorio. Ele nao
        # alcanca a cicatriz da 20.4, que custou SETE paginas servindo o
        # tema cru na clubedomosaico DUAS VEZES em tres dias: o Sync grava
        # o snippet INATIVO de proposito e ATIVA depois, e quando a
        # ativacao falha ele escreve `gravado (#13) mas NAO ativado` numa
        # linha do log, SEGUE EM FRENTE e sobe a revisao. O byte estava
        # certo no repositorio nas duas vezes.
        #
        # A partir da casca 1.6.0 o /casca serve `versoes`, que o coletor
        # monta por filtro. Snippet que nao esta ATIVO nao roda, nao
        # pendura o filtro, e o `id` dele NAO APARECE — entao `id` que
        # falta aqui e snippet que nao carregou, nao snippet com versao
        # errada. As duas coisas tem conserto diferente, e por isso o
        # portao as diz separadas em vez de reprovar as duas igual (20.5).
        #
        # E a leitura so e honesta porque `teste-versao-dos-snippets.php`
        # garante, no chao e antes de o ar ser consultado, que todo
        # snippet `publicar: true` SE REGISTRA com o proprio `id`: sem
        # isso, `id` ausente poderia ser descuido do repositorio, e o
        # portao estaria acusando o ar de um defeito da bancada.
        # ---------------------------------------------------------------
        esperadas = dict((it["id"], it.get("versao"))
                         for it in manifest["snippets"] if it.get("publicar"))
        no_ar = c.get("versoes")
        afirma(isinstance(no_ar, dict),
               "o /casca nao serve `versoes` — a casca no ar e anterior a 1.6.0, ou o campo "
               "sumiu. Sem ele o espelho de versao para no repositorio e o ar segue sem regua")
        if isinstance(no_ar, dict):
            faltando = [i for i in esperadas if i not in no_ar]
            afirma(not faltando,
                   "20.4: o /casca nao traz a versao de %s. Snippet que nao esta ATIVO nao "
                   "pendura o filtro, entao `id` ausente aqui significa GRAVADO E NAO ATIVADO "
                   "— o defeito que a 20.4 nomeia, e o conserto e acionar o Sync outra vez"
                   % ", ".join(sorted(faltando)))
            for ident, declarada in sorted(esperadas.items()):
                if ident in no_ar:
                    afirma(no_ar[ident] == declarada,
                           "%s: o manifest declara `versao` %r e o WordPress carregou %r. O "
                           "sha256 bate com o byte do repositorio e o codigo no ar e OUTRO: "
                           "e snippet gravado sem ativar, ou ativacao que pegou a passada "
                           "anterior" % (ident, declarada, no_ar[ident]))
            sobrando = [i for i in no_ar if i not in esperadas]
            if sobrando:
                registro("o /casca traz %d versao(oes) que o manifest nao publica: %s"
                         % (len(sobrando), ", ".join(sorted(sobrando))))
            registro("versao no ar conferida contra o manifest em %d de %d snippet(s) "
                     "publicaveis: %s"
                     % (len([i for i in esperadas if i in no_ar]), len(esperadas),
                        ", ".join("%s %s" % (i, no_ar[i])
                                  for i in sorted(esperadas) if i in no_ar)))
        for linha in ((c.get("instalado") or {}).get("relato") or []):
            afirma("ERRO" not in linha and "ATENCAO" not in linha,
                   "a instalacao da casca relatou: %s" % linha)
            registro("instalacao: %s" % linha)
        for slug, p in (c.get("paginas") or {}).items():
            afirma(bool(p.get("url")),
                   "a pagina %r esta no mapa da casca e nao tem URL no ar — link interno "
                   "para 404 e o defeito de 08/09/2026" % slug)
            if p.get("url"):
                urls[slug] = p["url"]

    # -------------------------------------------------------------------
    # 4. O SITEMAP, E TODA URL DELE EM 200
    # -------------------------------------------------------------------
    cod, _, mapa = buscar("/wp-sitemap.xml")
    sub = re.findall(r"<loc>([^<]+)</loc>", mapa)
    todas = []
    for s in sub:
        c2, _, x = buscar(s.replace(DOMINIO, ""), v=True)
        afirma(c2 == 200, "sub-sitemap %s respondeu %s" % (s, c2))
        todas.extend(re.findall(r"<loc>([^<]+)</loc>", x))
    todas = sorted(set(todas))
    registro("sitemap: %d URL(s) publicada(s)" % len(todas))
    afirma(len(todas) >= 1, "o sitemap nao publica nenhuma URL")

    # O SITEMAP E CURADORIA, NAO INVENTARIO (14.1). Medido em 29/10/2026: quatro
    # das seis URLs eram lixo de fabrica do WordPress, num dominio de dois dias.
    lixo = ("hello-world", "sample-page", "/author/", "/category/", "ola-mundo",
            "pagina-exemplo", "/tag/", "?p=")
    for u in todas:
        for termo in lixo:
            afirma(termo not in u,
                   "14.1: o sitemap publica %s, que e URL fraca de dominio novo — sitemap e "
                   "curadoria, nao inventario" % u)
    for s in sub:
        afirma("users" not in s and "taxonomies" not in s,
               "14.1: o sitemap ainda tem o sub-sitemap %s — arquivo de autor e de "
               "categoria nao e pagina de verdade nesta ilha" % s)

    # -------------------------------------------------------------------
    # 5. CADA PAGINA, UMA POR UMA
    # -------------------------------------------------------------------
    bastidor = ["egresso", "SERP classificada", "snippet", "wp-sitemap", "manifest.json",
                "ARQUIPELAGO", "Rodametria Sync", "bancada", "dados/", "ferramentas/",
                "regras/", "publicavel", "sha256", "revisao"]

    for u in todas:
        caminho = u.replace(DOMINIO, "")
        cod, ct, html = buscar(caminho)
        afirma(cod == 200, "%s respondeu %s" % (caminho, cod))
        if cod != 200:
            continue

        # (2) zero &#038; DENTRO de <script> — contado SO nos blocos script.
        scripts = re.findall(r"<script[^>]*>(.*?)</script>", html, re.S | re.I)
        dentro = sum(s.count("&#038;") for s in scripts)
        afirma(dentro == 0,
               "%s: ha %d entidade(s) &#038; dentro de <script> — e o defeito que derrubou "
               "cinco calculadoras da Aquametria" % (caminho, dentro))

        corpo = corpo_da_pagina(html)
        texto = re.sub(r"<[^>]+>", " ", corpo)
        texto = re.sub(r"\s+", " ", texto).strip()

        # (3) o corpo comeca pelo texto, e nao por metadado YAML.
        afirma(not texto.startswith("---"),
               "%s: o corpo comeca por metadado e nao por texto" % caminho)

        # Pagina fina nao entra no indice de dominio novo (secao 8).
        afirma(len(texto) >= 1500,
               "%s: o corpo tem %d caracteres e o piso e 1.500 — pagina fina gasta orcamento "
               "de rastreamento de dominio novo" % (caminho, len(texto)))
        registro("%s: %d caracteres de corpo" % (caminho, len(texto)))

        # <title>, H1, description e JSON-LD (32.3: nenhum deles muda com o molde).
        afirma(bool(re.search(r"<title>[^<]{10,}</title>", html)),
               "%s: sem <title>" % caminho)
        h1 = re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.S | re.I)
        afirma(len(h1) == 1, "%s: tem %d <h1> e tinha de ter 1" % (caminho, len(h1)))
        desc = re.search(r'<meta name="description" content="([^"]{20,})"', html)
        afirma(bool(desc), "%s: sem meta description" % caminho)
        if desc:
            # ITEM 5 DO DESPACHO DE 30/10/2026. O teto era 200 e por isso ele
            # APROVOU uma description de 193 e uma de 161: a ronda achou as duas
            # a olho, com o portao verde. 160 e o numero que o despacho declara.
            # E O QUE SE CONTA E O TEXTO, NAO A MARCACAO: o atributo vem
            # escapado do `esc_attr` do WordPress, entao um apostrofo chega como
            # `&#039;` e contaria 6 caracteres no lugar de 1 — a familia do
            # `&#038;` que a propria 12 cobra dentro de <script>. Desfazer as
            # entidades antes de medir e o que faz o numero ser o do leitor.
            texto_desc = desescapar_entidades(desc.group(1))
            afirma(len(texto_desc) <= 160,
                   "%s: description com %d caracteres e o teto e 160"
                   % (caminho, len(texto_desc)))
            registro("%s: description com %d caracteres" % (caminho, len(texto_desc)))
        jsonld = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
        afirma(len(jsonld) >= 1, "%s: sem JSON-LD" % caminho)
        for j in jsonld:
            try:
                json.loads(j)
            except Exception as e:
                afirma(False, "%s: JSON-LD invalido (%s)" % (caminho, e))
        if caminho not in ("/", ""):
            afirma(any("BreadcrumbList" in j for j in jsonld),
                   "%s: sem BreadcrumbList, e a 16.4 o exige em toda pagina que nao e a home"
                   % caminho)
            afirma("rdm-trilha" in html, "%s: sem trilha na tela" % caminho)

        # Menu acessivel (secao 6), favicon proprio e marca.
        afirma('aria-expanded' in html and 'aria-controls' in html,
               "%s: o botao do menu esta sem aria-expanded/aria-controls" % caminho)
        afirma('rel="icon"' in html and "image/svg+xml" in html,
               "%s: sem favicon proprio — icone padrao do WordPress na aba e bloco reprovado"
               % caminho)
        afirma("rdm-marca" in html, "%s: a casca nao pintou a marca" % caminho)
        afirma(html.count("rdm-rodape") >= 1, "%s: sem rodape da casca" % caminho)
        afirma(len(re.findall(r'class="rdm-rodape"', html)) <= 1,
               "%s: DOIS rodapes empilhados" % caminho)

        # Imagem com width/height e alt (secao 6 e 32.3).
        for img in re.findall(r"<img[^>]*>", corpo):
            afirma("alt=" in img, "%s: <img> sem alt: %s" % (caminho, img[:80]))
            afirma("width=" in img and "height=" in img,
                   "%s: <img> sem width/height: %s" % (caminho, img[:80]))

        # 32.4: zero palavra de bastidor no texto SERVIDO.
        for termo in bastidor:
            afirma(termo.lower() not in texto.lower(),
                   "32.4: a palavra de bastidor %r aparece no texto servido de %s"
                   % (termo, caminho))

        # Shortcode cru na tela e desembarque que nao aconteceu.
        afirma("[rodametria_" not in texto,
               "%s: shortcode cru servido na tela — o snippet nao esta ativo" % caminho)

    # -------------------------------------------------------------------
    # 6. A F2, AFIRMACAO POR AFIRMACAO CONTRA O BANCO
    # -------------------------------------------------------------------
    d = json.load(open(os.path.join(ILHA, "dados", "f2-respostas.json"), encoding="utf-8"))
    alvo = None
    for u in todas:
        if "autonomia" in u:
            alvo = u.replace(DOMINIO, "")
    afirma(alvo is not None, "a F2 nao esta no sitemap")
    if alvo:
        cod, _, html = buscar(alvo)
        corpo = corpo_da_pagina(html)
        texto = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", corpo))

        # (4) o script vem do RODAPE e a tabela aparece no HTML servido.
        pos_script = html.find('id="rodametria-f2-js"')
        pos_corpo = html.find("rdm-tabela")
        afirma(pos_script > pos_corpo > 0,
               "a F2 serve o script antes da tabela — o JS tinha de vir do rodape")
        afirma("rdm-tabela" in html, "a F2 nao serve a tabela pre-renderizada")

        # A CAIXA DE RESULTADO ESTA PRE-RENDERIZADA: o numero do exemplo tem de
        # estar no HTML servido, sem ninguem clicar em nada. E a 32.1 item 4 e a
        # secao 5 (visibilidade em IA) na mesma afirmacao.
        r = d["resposta_exemplo"]
        afirma(r["piso_km_tela"] in corpo,
               "a F2 nao serve o piso de km do exemplo (%s) no HTML" % r["piso_km_tela"])
        afirma(r["teto_km_tela"] in corpo,
               "a F2 nao serve o teto de km do exemplo (%s) no HTML" % r["teto_km_tela"])
        for f in r["frases_km"] + r["frases_peso"]:
            limpo = re.sub(r"\s+", " ", f)
            afirma(limpo[:60] in texto,
                   "a F2 nao serve a frase do banco: %r" % limpo[:70])

        # A RESSALVA DO PESO ESTA DEPOIS DO BLOCO DE COMPRA, e nao dentro da
        # caixa: e o que mantem o primeiro botao de compra acima do teto de
        # 1.400 px da 32.5 no telefone de 390 px.
        pos_compra = corpo.find("rdm-molde-compra")
        pos_ressalva = corpo.find("rdm-f2-ressalva")
        afirma(0 < pos_compra < pos_ressalva,
               "a ressalva do peso nao esta depois do bloco de compra (compra em %d, "
               "ressalva em %d)" % (pos_compra, pos_ressalva))

        # TODA linha da tabela do banco esta no ar, com o Wh que o banco diz.
        for l in d["tabela"]["do_banco"] + d["tabela"]["externas"]:
            afirma(l["rotulo"] in corpo,
                   "a linha %r da tabela nao esta no ar" % l["rotulo"])
            afirma(l["wh"] in corpo,
                   "o Wh %r da linha %r nao esta no ar" % (l["wh"], l["rotulo"]))

        # O BLOCO DE COMPRA: conta CARTAO contra BLOCO, nunca a classe de um
        # degrau (secao 8 — sete reguas quebraram por procurar o rotulo do
        # degrau). O degrau viaja como registro, nunca como criterio.
        cartoes = re.findall(r'class="rdm-molde-cartao"', corpo)
        afirma(len(cartoes) == len(d["compra"]["vitrine"]),
               "o bloco de compra serve %d cartao(oes) e a vitrine do banco tem %d"
               % (len(cartoes), len(d["compra"]["vitrine"])))
        afirma(len(cartoes) >= 1,
               "o bloco de compra esta VAZIO, e a secao 7 proibe: o piso e o link de busca")
        for f in d["compra"]["vitrine"]:
            afirma(f["url_busca"] in corpo,
                   "a saida de compra de %s nao esta no ar" % f["id"])
            afirma(f["nome"] in corpo, "o nome de %s nao esta no ar" % f["id"])
        for a in re.findall(r"<a[^>]*s\.shopee\.com\.br[^>]*>", corpo):
            afirma('rel="sponsored noopener"' in a,
                   "link de afiliado sem rel sponsored: %s" % a[:90])
            afirma('target="_blank"' in a,
                   "link de afiliado sem target _blank: %s" % a[:90])
        registro("bloco de compra: %d cartao(oes), degrau(s) %s"
                 % (len(cartoes), sorted({f["degrau"] for f in d["compra"]["vitrine"]})))

        # A PRESTACAO DE CONTAS FECHA NO AR, e o numero e lido da TELA.
        total = d["compra"]["total_registros_veiculos"]
        soma = sum(len(v) for v in d["compra"]["grupos"].values())
        afirma(soma == total, "a prestacao de contas do banco nao fecha: %d de %d" % (soma, total))
        m = re.search(r"São (\d+) veículos nomeados de (\d+) no banco", texto)
        afirma(bool(m), "a F2 nao serve a frase que fecha a prestacao de contas")
        if m:
            afirma(int(m.group(1)) == int(m.group(2)) == total,
                   "a tela diz %s nomeados de %s e o banco tem %d"
                   % (m.group(1), m.group(2), total))

        # Toda dobra e <details> de verdade: o texto continua no HTML servido.
        dobras = re.findall(r"<details[^>]*class=\"rdm-molde-dobra\"", corpo)
        afirma(len(dobras) >= 3,
               "a F2 tem %d dobra(s) e a 32.1 item 7 pede o texto recolhivel em secoes" % len(dobras))

        # O aviso de comissao existe e esta visivel (secao 7).
        afirma("comiss" in texto.lower(), "a F2 nao serve o aviso de comissao")

    # -------------------------------------------------------------------
    # 7. O QUE ESTE PORTAO NAO MEDIU — dito, nunca aprovado em silencio
    # -------------------------------------------------------------------
    # Esta linha dizia "que esta ilha ainda nao tem", e envelheceu em UMA HORA:
    # o portao nasceu na mesma execucao. Frase sobre o estado da fabrica dentro
    # de um portao e a mesma divida do numero de tela digitado — ela nao fala
    # com o que descreve. Agora ela CONFERE que o arquivo existe.
    tem_portao_de_pixel = os.path.exists(
        os.path.join(AQUI, "conferir-32-5-no-navegador.mjs"))
    registro("NAO MEDIDO AQUI: a 32.5 (formulario antes de 700 px, primeiro botao de compra "
             "antes de 1.400 px) se mede a 390 px num navegador de verdade. O portao de "
             "pixel %s — rode `node ferramentas/conferir-32-5-no-navegador.mjs`."
             % ("EXISTE nesta ilha e NAO foi rodado por este portao"
                if tem_portao_de_pixel else
                "NAO EXISTE nesta ilha, e a 32.5 segue sem ser medida em pixel"))
    registro("NAO MEDIDO AQUI: a leitura SEM quebra de cache (como o Google le). Toda URL acima "
             "foi pedida com ?v=<agora>, entao estas afirmacoes sao sobre a ORIGEM.")

    return encerrar()


def encerrar():
    print("conferir-no-ar: %d afirmacoes, %d falha(s)" % (afirmacoes, len(falhas)))
    for r in registros:
        print("  registro: %s" % r)
    for f in falhas:
        print("  REPROVADO: %s" % f)
    print("APROVADO" if not falhas else "REPROVADO")

    return 1 if falhas else 0


def autoteste():
    """O CORTE DO LOG, MEDIDO SEM REDE — e o primeiro mundo e o mundo de verdade.

        python3 ferramentas/conferir-no-ar.py --autoteste

    Nasceu em 02/11/2026 junto com o conserto do corte, porque a regua que
    estava errada estava VERDE: ela imprimia "0 linha de falha nesta entrega"
    sobre uma unica linha, a de resumo. Conserto sem mundo fabricado e conserto
    que a proxima mudanca desfaz calada — e a 32.5-d e literal sobre isso: "a
    regra do molde que nunca rodou contra o dado de verdade esta quebrada e
    parece sa".
    """
    ok = []
    mal = []

    def diz(cond, msg):
        (ok if cond else mal).append(msg)

    # MUNDO 1 — O LOG DE VERDADE, lido no /status as 17h40Z de 02/11/2026, no
    # desembarque da revisao 29. E o mundo em que a regua velha devolvia 1.
    real = [
        "2026-11-02 17:40 revisão 29: 8 aplicado(s), 6 aguardando desembarque",
        "2026-11-02 17:40 dados/paginas-institucionais: ok (option rodametria_dados_paginas-institucionais)",
        "2026-11-02 17:40 dados/vitrine-de-produto: ok (option rodametria_dados_vitrine-de-produto)",
        "2026-11-02 17:40 dados/paginas-de-produto: ok (option rodametria_dados_paginas-de-produto)",
        "2026-11-02 17:40 dados/f2-respostas: ok (option rodametria_dados_f2-respostas)",
        "2026-11-02 17:40 snippets/rodametria-institucional: ok (snippet #9 atualizado)",
        "2026-11-02 17:40 snippets/rodametria-produto: ok (snippet #8 atualizado)",
        "2026-11-02 17:40 snippets/rodametria-f2: ok (snippet #7 atualizado)",
        "2026-11-02 17:40 snippets/rodametria-casca: ok (snippet #6 atualizado)",
        "2026-11-02 14:10 revisão 28: 5 aplicado(s), 6 aguardando desembarque",
        "2026-11-02 14:10 dados/paginas-institucionais: ok (option rodametria_dados_paginas-institucionais)",
        "2026-11-02 14:10 dados/vitrine-de-produto: ok (option rodametria_dados_vitrine-de-produto)",
        "2026-11-02 14:10 dados/paginas-de-produto: ok (option rodametria_dados_paginas-de-produto)",
        "2026-11-02 14:10 dados/f2-respostas: ok (option rodametria_dados_f2-respostas)",
        "2026-11-02 14:10 snippets/rodametria-produto: ok (snippet #8 atualizado)",
    ]
    fecho, itens = linhas_da_revisao(real, 29)
    diz(fecho is not None and "revisão 29" in fecho, "1. acha a linha de fecho da revisao 29")
    diz(len(itens) == 8, "1. le 8 linhas de item da revisao 29 (a regua velha lia 1)")
    diz(aplicados_declarados(fecho) == 8, "1. le `8 aplicado(s)` da linha de fecho")
    diz(all(re.search(r"\bok\b", l) for l in itens), "1. as 8 linhas dizem `ok`")

    # MUNDO 2 — A REVISAO ANTERIOR, no meio da janela: o corte nao pode
    # atravessar para a de cima nem para a de baixo.
    fecho28, itens28 = linhas_da_revisao(real, 28)
    diz(len(itens28) == 5, "2. le 5 linhas de item da revisao 28, sem invadir a 29")
    diz(aplicados_declarados(fecho28) == 5, "2. a conta da 28 fecha em 5")
    diz(not any("17:40" in l for l in itens28), "2. nenhuma linha da 29 vazou para a 28")

    # MUNDO 3 — UMA LINHA DE ITEM QUE NAO DIZ `ok`. E a cicatriz com nome: o
    # Sync grava inativo e ativa depois, e na falha escreve esta linha e SEGUE.
    quebrado = list(real)
    quebrado[5] = "2026-11-02 17:40 snippets/rodametria-institucional: gravado (#9) mas NÃO ativado"
    _, itens_q = linhas_da_revisao(quebrado, 29)
    muda = [l for l in itens_q if not re.search(r"\bok\b", l)]
    diz(len(muda) == 1 and "ativado" in muda[0],
        "3. a linha `gravado mas NAO ativado` e PEGA (a regua velha nao a lia)")

    # MUNDO 4 — A JANELA ROLOU E LEVOU ITEM: o fecho declara 8, sobraram 3. A
    # conta nao fecha, e e isso que o portao tem de dizer.
    rolado = real[:4]
    fecho_r, itens_r = linhas_da_revisao(rolado, 29)
    diz(aplicados_declarados(fecho_r) == 8 and len(itens_r) == 3,
        "4. janela rolada: o fecho declara 8 e so 3 itens sobraram — a conta abre")

    # MUNDO 5 — REVISAO QUE NAO ESTA NA JANELA.
    fecho_x, itens_x = linhas_da_revisao(real, 99)
    diz(fecho_x is None and itens_x == [],
        "5. revisao fora da janela devolve nada, em vez de devolver a janela toda")

    # MUNDO 6 — FECHO SEM NUMERO DE APLICADOS.
    diz(aplicados_declarados("2026-11-02 17:40 revisão 29: nada a fazer") is None,
        "6. fecho sem `N aplicado(s)` devolve None, e nao um numero inventado")

    # MUNDO 7 — A REGUA VELHA, REFEITA AQUI, TEM DE DISCORDAR DESTA. Se as duas
    # concordarem, este autoteste nao esta medindo o conserto.
    velhas = []
    for l in real:
        velhas.append(l)
        if REV_RE.search(l) and int(REV_RE.search(l).group(1)) == 29:
            break
    diz(len(velhas) == 1 and len(itens) == 8,
        "7. a regua VELHA devolve 1 linha e a nova devolve 8 — o conserto move algo")

    # MUNDO 8 — A ROTA DA 29.3, OS QUATRO MUNDOS QUE ESTA NUVEM NAO PRODUZ.
    # O site de verdade (se tudo estiver sao) devolve SEMPRE o mundo sadio, e
    # portao que so viu o mundo sadio nao mediu nada.
    indice_com = ["/rodametria/v1", "/rodametria/v1/casca", "/rodametria/v1/rotas",
                  "/rodametria/v1/status", "/rodametria/v1/sync", "/rodametria/v1/token"]
    indice_sem = [r for r in indice_com if r != "/rodametria/v1/rotas"]

    diz(problemas_da_parede(indice_com, 401, 401, "rodametria_rotas_token_invalido") == [],
        "8. o mundo SADIO passa (rota no indice, 401 nas duas, codigo de token invalido)")

    sem_rota = problemas_da_parede(indice_sem, 404, 404, None)
    diz(len(sem_rota) >= 2 and any("NAO aparece no indice" in m for m in sem_rota)
        and any("404" in m for m in sem_rota),
        "8. a rota AUSENTE e pega pelo indice E pelo 404 — foi este o mundo da robometria por quatro dias")

    aberta = problemas_da_parede(indice_com, 200, 200, None)
    diz(any("PAREDE ESTA ABERTA" in m for m in aberta),
        "8. a parede ABERTA e pega: 200 sem token entrega o retrato do servidor")

    morto = problemas_da_parede(indice_com, 401, 401, "rodametria_rotas_sem_fonte_de_token")
    diz(any("PORTAO MORTO" in m for m in morto),
        "8. o PORTAO MORTO e pego: 401 nas duas, rota no indice, e a casca negando TODO pedido")

    quinhentos = problemas_da_parede(indice_com, 500, 500, None)
    diz(any("401" in m for m in quinhentos),
        "8. 500 na parede e pego — e o que sai quando o WP_Error nao traz `status`")

    # MUNDO 9 — A REGUA VELHA DESTA LEITURA, refeita ao lado da nova: a que
    # so pergunta "nao deu 200?". Ela APROVA o portao morto e APROVA o 404 —
    # e e por isso que a afirmacao do codigo e positiva (20.8).
    regua_velha = lambda cod: [] if cod != 200 else ["deu 200"]
    diz(regua_velha(401) == [] and morto != [],
        "9. a regua velha APROVA o portao morto e a nova o REPROVA — as duas discordam, senao este autoteste nao mede o conserto")
    diz(regua_velha(404) == [] and sem_rota != [],
        "9. a regua velha APROVA a rota AUSENTE e a nova a REPROVA")

    print("conferir-no-ar --autoteste: %d de %d afirmacoes, %d falha(s)"
          % (len(ok), len(ok) + len(mal), len(mal)))
    for m in mal:
        print("  REPROVADO: %s" % m)
    print("APROVADO" if not mal else "REPROVADO")

    return 1 if mal else 0


if __name__ == "__main__":
    sys.exit(autoteste() if "--autoteste" in sys.argv else main())
