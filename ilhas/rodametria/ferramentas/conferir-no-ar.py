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


# ---------------------------------------------------------------------------
# A 32.4 NO QUE A PAGINA SERVE, E NAO SO NO QUE O LEITOR VE (bloco 7, 04/11/2026)
#
# `corpo_da_pagina()` acima tira `<script>` e `<style>` antes de medir, e esta
# CERTO: ali mora CSS e JS, nao prosa, e a afirmacao sobre o que a pagina DIZ se
# mede no corpo. So que a 32.4 nao e sobre o que o leitor VE — e sobre o que a
# pagina SERVE, e e o fonte que a visao geral de IA ingere. Entre as duas
# leituras cabia o defeito medido no ar as 19h2xZ de 04/11/2026: as folhas desta
# ilha serviam 23 comentarios de CSS e 7.486 bytes na home e na F2, com tres
# mencoes a `conferir-32-5-no-navegador.mjs`, uma a `bancada` e varias a numero
# de secao do contrato.
#
# AS DUAS AFIRMACOES SAO SEPARADAS de proposito, porque o conserto de cada uma e
# diferente (20.5): uma diz que a FOLHA servida tem comentario; a outra diz que
# ha PALAVRA de bastidor no HTML servido. A primeira se conserta na casca, a
# segunda no texto que a produziu.
# ---------------------------------------------------------------------------

BASTIDOR = ["egresso", "SERP classificada", "snippet", "wp-sitemap", "manifest.json",
            "ARQUIPELAGO", "Rodametria Sync", "bancada", "dados/", "ferramentas/",
            "regras/", "publicavel", "sha256", "revisao"]

# Extensao de rotina desta fabrica. `.php` NAO entra, e a causa foi MEDIDA em
# 04/11/2026: o WordPress serve `/wp-*.php` e `xmlrpc.php` no proprio `<head>`,
# em duas ocorrencias por pagina, e um termo `.php` reprovaria a pagina certa —
# que e o caminho mais curto para alguem passar a ignorar o portao (20.5).
# `.py` e `.mjs` foram medidos em ZERO fora das nossas folhas nas mesmas 9 URLs.
EXTENSOES_DE_ROTINA = [".py", ".mjs"]


def folhas_da_ilha(html):
    """So as folhas que ESTA ilha escreve, nunca as do WordPress.

    Medido em 04/11/2026 na pagina da F2: 18 blocos `<style>`, dos quais 17 sao
    do proprio WordPress — one-liners de 41 a 103 bytes, 1.254 bytes de
    comentario no total, que nao sao desta ilha e nao saem daqui. O nosso e 1
    bloco com 23 comentarios e 7.486 bytes: 85,6% dos bytes de comentario da
    pagina. Reprovar pelos 17 do WordPress seria reprovar o que esta ilha nao
    pode consertar.
    """
    nossas = []
    for atrib, css in re.findall(r"<style([^>]*)>(.*?)</style>", html, re.S | re.I):
        if "rodametria" in atrib or "rdm-" in atrib:
            m = re.search(r'id="([^"]+)"', atrib)
            nossas.append((m.group(1) if m else "(sem id)", css))

    return nossas


def problemas_da_folha_servida(html):
    """Comentario de CSS dentro de folha DESTA ilha. Funcao pura, sem rede."""
    ruim = []
    for ident, css in folhas_da_ilha(html):
        quantos = len(re.findall(r"/\*", css))
        if quantos:
            bytes_ = sum(len(m) for m in re.findall(r"/\*.*?\*/", css, re.S))
            ruim.append("a folha %s serve %d comentario(s) de CSS (%d bytes) — o comentario "
                        "mora no repositorio (secao 3), nunca na folha impressa"
                        % (ident, quantos, bytes_))

    return ruim


def problemas_de_bastidor_no_servido(html, nomes_de_arquivo=()):
    """A 32.4 sobre o HTML SERVIDO INTEIRO, e a afirmacao e POSITIVA.

    Nao procura "a falha que alguem ja imaginou" num pedaco escolhido: varre o
    byte servido. Medido em 04/11/2026 nas 9 URLs, a UNICA palavra da lista que
    aparecia no HTML inteiro era `bancada`, uma vez, DENTRO da nossa folha —
    entao esta regua nao reprova o WordPress por acidente, e isso foi medido
    antes de ela nascer, nao suposto.
    """
    ruim = []
    baixo = html.lower()
    for termo in BASTIDOR:
        if termo.lower() in baixo:
            ruim.append("32.4 no HTML servido: a palavra de bastidor %r aparece %d vez(es) — "
                        "invisivel para o visitante e legivel para quem le o fonte, que e o "
                        "que a visao geral de IA ingere" % (termo, baixo.count(termo.lower())))
    for ext in EXTENSOES_DE_ROTINA:
        if ext in baixo:
            ruim.append("32.4 no HTML servido: a extensao de rotina %r aparece %d vez(es) — "
                        "nome de arquivo desta fabrica nao e coisa que a pagina sirva"
                        % (ext, baixo.count(ext)))
    for nome in nomes_de_arquivo:
        if nome.lower() in baixo:
            ruim.append("32.4 no HTML servido: o nome de arquivo %r desta pasta aparece na "
                        "pagina" % nome)

    return ruim

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

# A LISTA DA 29.2 MORA NUMA CONSTANTE porque o diagnostico da porta a conta.
PORTAS_DA_292 = (
    ("/robots.txt", "text/plain"),
    ("/wp-sitemap.xml", "xml"),
    ("/wp-json/", "application/json"),
)


def rest(rota):
    """A rota REST pela porta QUE NAO CAI, e nunca pelo caminho bonito.

    MEDIDO NESTA ILHA EM 05/11/2026, as 10h2xZ, e o defeito era DESTE ARQUIVO.
    A porta de entrada caiu (o bloco `# BEGIN WordPress` fora do `.htaccess` da
    raiz, a assinatura da 29 pela QUINTA vez no Arquipelago) e este portao, que
    existe para medir isso, fez duas coisas erradas por ler o REST pelo caminho
    bonito:

      (1) ACUSOU A CASCA DE UM DEFEITO QUE ELA NAO TEM. O indice de rotas era
          lido em `/wp-json/rodametria/v1` — que e caminho bonito, portanto
          morto junto com a porta. O `json.loads` falhava sobre a pagina 404 do
          hospedeiro, `rotas_no_indice` vinha VAZIA, e a saida dizia "esta casca
          nao registra a rota que mede a porta de entrada por dentro". A rota
          ESTAVA registrada: `?rest_route=/rodametria/v1/rotas` respondia 200 na
          mesma passada, e a casca a servia desde 03/11. Quem lesse aquela linha
          iria procurar registro de rota na casca — o conserto errado, no arquivo
          errado, com a porta de entrada do site no chao.

      (2) PAROU DE MEDIR O RESTO. O `/status` era lido pelo caminho bonito, e
          `main()` devolve `encerrar()` quando ele nao da 200: a leitura inteira
          encolheu de 481 afirmacoes (04/11, de tarde) para NOVE. Tudo o que este
          portao sabe sobre conteudo, voz, 32.4 e 32.5 deixou de ser medido
          exatamente no dia em que a ilha mais precisava ser medida.

    E A 29.1 COM UM ANDAR A MAIS, e por isso esta aqui e nao so no registro do
    dia: a 29.1 diz que nenhum portao viu a porta cair porque todos entravam
    pela porta que continuou aberta. Este portao, escrito para ver, entrava pela
    porta que CAI — e por isso ele viu, e culpou a casca.

    O QUE ESTA TROCA NAO AFROUXA, porque afrouxar portao por conveniencia seria
    o conserto virar o defeito seguinte: `/wp-json/` em 200 com
    `application/json` continua sendo afirmacao da 29.2, inteira, logo acima.
    A porta segue cobrada pela afirmacao que existe para cobra-la; o que muda e
    que as OUTRAS afirmacoes param de depender dela. E a 20.5 ao pe da letra —
    portao que reprova pelo motivo errado e o caminho mais curto para alguem
    passar a ignora-lo.
    """
    return "?rest_route=" + rota


def rotas_do_indice(bruto):
    """As rotas que o indice REST declara, ou LISTA VAZIA se nao for JSON.

    Separada de `main()` de proposito, para o `--autoteste` poder dar a ela a
    pagina 404 do hospedeiro e medir o que a regua velha concluia dela.
    """
    try:
        d = json.loads(bruto)
    except Exception:
        return []
    if not isinstance(d, dict):
        return []

    return sorted((d.get("routes") or {}).keys())


def diagnostico_da_porta(cod_home, cods_das_portas, rest_vivo):
    """A ASSINATURA DA 29, NOMEADA — ou None quando ela nao esta na mesa.

    Cinco vezes no Arquipelago com a mesma cara: clubedomosaico em 24/09, 05/10
    e 08/10, robometria em 30/10 e esta ilha em 05/11. Sempre as mesmas quatro
    grandezas juntas: a HOME em 200, as TRES portas da 29.2 em 404, o REST VIVO
    por `?rest_route=` e o caminho bonito morto. O que isso quer dizer tem nome
    e tem conserto, e os dois estao na 29: o bloco `# BEGIN WordPress` saiu do
    `.htaccess` da raiz, e o conserto e o `flush_rewrite_rules( true )` da 29.3.

    POR QUE O PORTAO DIZ A CAUSA E NAO SO OS SINTOMAS: sem esta linha a leitura
    sai como seis ou oito reprovacoes espalhadas, cada uma verdadeira e nenhuma
    dizendo o que fazer, e a de 05/11 ainda saia com uma SETIMA acusando a
    casca. Causa medida cinco vezes e com conserto escrito nao e palpite: e o
    que separa "a ilha esta vermelha" de "a porta caiu, e o conserto e este".

    O QUE ELA NAO AFIRMA, e e por isso que ela cobra as quatro grandezas
    juntas: se a home TAMBEM estiver morta, ou se o REST estiver morto nas duas
    formas, nao e esta a causa — e esta funcao devolve None em vez de nomear a
    errada. Causa inventada e a proxima execucao consertando a coisa errada
    (29.5).
    """
    if cod_home != 200 or not rest_vivo:
        return None
    if not cods_das_portas or any(c == 200 for c in cods_das_portas):
        return None

    return ("29: A PORTA DE ENTRADA CAIU, e a assinatura e a conhecida — home em 200, "
            "as %d portas da 29.2 em %s, e o REST VIVO por `?rest_route=`. O WordPress "
            "esta de pe e o Apache parou de lhe mandar caminho bonito: e o bloco "
            "`# BEGIN WordPress` fora do `.htaccess` da raiz. CONSERTO: o "
            "`flush_rewrite_rules( true )` da 29.3 — `?rest_route=/rodametria/v1/rotas"
            "&token=<token do Sync>&reparar=1`, ou Salvar em Configuracoes > Links "
            "permanentes no wp-admin. O token desta ilha NAO esta no repositorio, "
            "entao o reparo NAO e exercitavel desta nuvem (quinta ocorrencia no "
            "Arquipelago: clubedomosaico 24/09, 05/10 e 08/10; robometria 30/10)"
            % (len(cods_das_portas), "/".join(str(c) for c in cods_das_portas)))


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


# ---------------------------------------------------------------------------
# A CLASSE DO QUANTIFICADOR E DO SUPERLATIVO, VARRIDA NO SITE INTEIRO — 04/11/2026
#
# POR QUE ELA ESTA NESTE PORTAO E NAO NOS OUTROS DOIS. A classe nasceu em
# 03/11/2026 nomeando UMA FRASE dentro do laco das paginas FILHAS de produto; na
# manha de 04/11 ela virou CLASSE, e entrou nas DUAS camadas declaradas que
# tinham portao (produto e institucional), cada uma com a propria lista de termos
# e a propria lista de liberacao. Na mesma tarde a varredura do site inteiro
# achou a MESMA classe numa TERCEIRA pagina, que nenhuma das duas podia ver:
#
#   /autonomia-patinete-eletrico/  ->  "E a lacuna MAIS COMUM do varejo"
#
# A prosa da F2 vive dentro de `snippets/rodametria-f2.php`. O cabecalho do
# portao de produto JA DIZIA, escrito antes deste dia, que existe *"um mundo
# entre os dois — prosa escrita direto no PHP, que a camada declarada nao ve"* —
# e a frase estava no ar desde 29/10 afirmando um ranqueamento que esta ilha
# nunca mediu.
#
# ENTAO O CONSERTO NAO E UM PORTAO POR CAMADA: E UM PORTAO POR SITE. Este laco
# varre TODA URL do sitemap e nao sabe de camada nenhuma — camada nova de pagina
# nasce JA coberta, que e o contrario do que aconteceu tres vezes em tres dias.
# As liberacoes continuam sendo por escrito, e ele le as TRES listas declaradas,
# porque a liberacao e da frase e nao do portao que a encontrou.
QUANTIFICADORES = (
    "quase nunca", "quase sempre", "quase todo", "quase toda", "quase todos",
    "quase todas", "quase ninguem", "quase nenhum", "quase nenhuma", "a maioria",
    "maioria", "a minoria", "minoria", "raramente", "costuma", "costumam",
    "na maior parte", "a maior parte", "maior parte", "boa parte", "grande parte",
    "geralmente", "normalmente", "em geral", "de modo geral", "via de regra",
    "tipicamente", "frequentemente", "na pratica", "poucos", "poucas", "muitos",
    "muitas",
    # O SUPERLATIVO DE FREQUENCIA E DE VENDA: nao e quantificador, e foi por isso
    # que as duas travas de ontem e de hoje de manha aprovaram as tres frases.
    "mais comum", "mais comuns", "mais vendido", "mais vendida",
    "mais vendidos", "mais vendidas", "vende mais", "vendem mais",
    "mais popular", "mais populares", "a media", "na media", "da media",
)

AS_TRES_CAMADAS_DECLARADAS = (
    "paginas-de-produto.json",
    "paginas-institucionais.json",
    # A TERCEIRA nasceu com este laco, para a camada cuja prosa vive no PHP e
    # que por isso nao tem camada declarada onde liberar.
    "liberacoes-de-quantificador.json",
)


def _sem_acento_q(t):
    import unicodedata
    t = unicodedata.normalize("NFD", str(t or "").lower())
    return "".join(c for c in t if unicodedata.category(c) != "Mn")


def ancoras_liberadas_do_site():
    """As ancoras LITERAIS das tres camadas declaradas, juntas.

    A liberacao e da FRASE, nao do portao que a encontrou: frase liberada na
    camada de produto nao pode ser denunciada aqui so porque este laco a achou
    por outro caminho. E ancora ausente no ar e cobrada pelo portao DAQUELA
    camada, que e quem sabe em que pagina ela devia estar.
    """
    ancoras = set()
    for nome in AS_TRES_CAMADAS_DECLARADAS:
        caminho = os.path.join(ILHA, "dados", nome)
        if not os.path.exists(caminho):
            continue
        with open(caminho, encoding="utf-8") as f:
            d = json.load(f)
        for q in d.get("quantificadores_declarados_permitidos") or []:
            a = (q.get("ancora_no_ar") or "").strip()
            if a:
                ancoras.add(_sem_acento_q(a))

    return tuple(sorted(ancoras))


def conferir_classe_no_site(caminho, texto, ancoras):
    """Denuncia a ocorrencia; nunca julga a prosa (20.5)."""
    t = _sem_acento_q(texto)
    for anc in ancoras:
        t = t.replace(anc, " ")
    for q in QUANTIFICADORES:
        i = t.find(q)
        while i >= 0:
            antes = t[i - 1] if i else " "
            depois = t[i + len(q):i + len(q) + 1] or " "
            if not (antes.isalpha() or depois.isalpha()):
                afirma(False,
                       "%s serve uma PROPORCAO ou um SUPERLATIVO por extenso (%r) que nao "
                       "esta liberado em camada declarada nenhuma: %r — e a classe que "
                       "chegou ao ar por TRES camadas em TRES dias, e este laco e o unico "
                       "que varre o site inteiro"
                       % (caminho, q, texto[max(0, i - 60):i + 80]))
                return
            i = t.find(q, i + 1)
    afirma(True, "")


def main():
    manifest = json.load(open(os.path.join(ILHA, "manifest.json"), encoding="utf-8"))
    revisao_esperada = int(manifest["revisao"])

    # -------------------------------------------------------------------
    # 1. A PORTA DE ENTRADA (29.2). Ela cai sozinha, sem nenhum portao
    #    acusar, e foi assim que o Clube do Mosaico passou nove dias fora.
    # -------------------------------------------------------------------
    cods_das_portas = []
    for caminho, tipo in PORTAS_DA_292:
        cod, ct, _ = buscar(caminho)
        cods_das_portas.append(cod)
        afirma(cod == 200, "29.2: %s respondeu %s, nao 200" % (caminho, cod))
        afirma(tipo in ct, "29.2: %s veio como %r e tinha de ser %r" % (caminho, ct, tipo))

    cod_home, _, _ = buscar("/")
    afirma(cod_home == 200, "29.2: a home respondeu %s, nao 200" % cod_home)

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
    _, _, indice = buscar(rest("/rodametria/v1"))
    rotas_no_indice = rotas_do_indice(indice)

    cod_sem, _, _ = buscar(rest(ROTA_DA_293))
    cod_err, _, corpo_err = buscar(rest(ROTA_DA_293) + "&token=token-de-proposito-errado")
    code_err = codigo_do_erro(corpo_err)

    for problema in problemas_da_parede(rotas_no_indice, cod_sem, cod_err, code_err):
        afirma(False, problema)

    # A LINHA DE REGISTRO DIZ O QUE FOI MEDIDO, NUNCA O VEREDITO. A primeira
    # versao dela dizia "a rota esta registrada" — e imprimia isso tambem no
    # mundo em que a rota devolvia 404 e NAO estava registrada. Registro que
    # afirma o que nao mediu e a familia do comentario que declara um
    # mecanismo: parece conferido e nao mede nada (32.5-d). Quem decide aqui
    # sao as afirmacoes acima.
    porta_caida = diagnostico_da_porta(cod_home, cods_das_portas, cod_sem in (200, 401))
    if porta_caida:
        afirma(False, porta_caida)

    registro("29.3: %s %s no indice; sem token -> %s; token errado -> %s com `%s` (a parede medida de fora, sem o token, e o indice lido por ?rest_route= — a porta que nao cai)"
             % (ROTA_DA_293,
                "PRESENTE" if ROTA_DA_293 in rotas_no_indice else "AUSENTE",
                cod_sem, cod_err, code_err))

    # -------------------------------------------------------------------
    # 2. O /status E O PORTAO DO DESEMBARQUE (20.4 e 20.5)
    # -------------------------------------------------------------------
    cod, _, bruto = buscar(rest("/rodametria/v1/status"))
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
    cod, _, bruto = buscar(rest("/rodametria/v1/casca"))
    afirma(cod == 200, "/casca respondeu %s — a casca nao esta ativa no ar" % cod)
    urls = {}
    if cod == 200:
        c = json.loads(bruto)
        registro("casca %s instalada em %s"
                 % (c.get("versao_casca"), (c.get("instalado") or {}).get("em")))

        # ---------------------------------------------------------------
        # 3a. A PURGA DE CACHE DO HOSPEDEIRO ESTA CARREGADA (03/11/2026)
        #
        # O "pronto quando" do despacho da purga pedia `tem_purga_de_cache`
        # saindo `true` no ar. Ele sai no retrato da rota da 29.3 desde que
        # a rota nasceu — e aquele retrato exige o TOKEN DO SYNC, que nao
        # esta no repositorio e nao deve estar. Ou seja: o criterio de
        # pronto do despacho nao era conferivel desta nuvem, e portao que
        # nao roda nao e portao. A casca 1.8.0 passou a servir o mesmo
        # booleano no /casca, que e publico.
        #
        # E ELE NAO E REDUNDANTE COM A VERSAO DO SNIPPET (3b abaixo): a
        # versao diz QUAL BYTE o WordPress carregou; este campo diz que a
        # FUNCAO existe no processo. A chamada dentro do reparo da 29.3 e
        # guardada por `function_exists`, entao e esta pergunta — e nao a
        # versao — que decide se o reparo vai purgar ou nao. E a 20.7 ao
        # contrario: la a ausencia do `id` acusa snippet morto; aqui a
        # presenca do booleano prova a funcao viva.
        # ---------------------------------------------------------------
        afirma(c.get("tem_purga_de_cache") is True,
               "/casca diz tem_purga_de_cache=%r — a purga do hospedeiro NAO esta "
               "carregada, e o reparo da 29.3 vai medir a copia velha depois de "
               "consertar" % (c.get("tem_purga_de_cache"),))

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
    bastidor = BASTIDOR

    # OS NOMES DE ARQUIVO DESTA PASTA, lidos do disco e nunca enumerados: nome
    # de rotina e exatamente o que a 32.4 proibe, e tres comentarios da folha
    # traziam `conferir-32-5-no-navegador.mjs` quando isto foi medido.
    nomes_de_arquivo = []
    for pasta in ("ferramentas", "regras", "dados", "snippets"):
        caminho = os.path.join(ILHA, pasta)
        if os.path.isdir(caminho):
            nomes_de_arquivo += [f for f in os.listdir(caminho)
                                 if os.path.isfile(os.path.join(caminho, f))]
    nomes_de_arquivo += ["manifest.json", "PROMPT.md", "ESTADO.md", "REGISTRO.md",
                         "VOZ.md", "DESIGN.md"]
    registro("nomes de arquivo desta pasta na regua da 32.4: %d" % len(nomes_de_arquivo))

    ancoras_do_site = ancoras_liberadas_do_site()
    registro("liberacoes de quantificador lidas das tres camadas declaradas: %d ancora(s)"
             % len(ancoras_do_site))

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

        # A CLASSE DO QUANTIFICADOR E DO SUPERLATIVO, EM TODA URL DO SITEMAP.
        conferir_classe_no_site(caminho, texto, ancoras_do_site)

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
        # ITEM 2 DO DESPACHO DE 04/11/2026 — `dateModified` EM TODA URL DO SITEMAP.
        # O defeito medido: ZERO ocorrencia de `dateModified` e ZERO de
        # `datePublished` em todo o JSON-LD das 9 URLs, numa ilha cujo produto E
        # "o preco de hoje". As paginas diziam a data em PROSA e a camada que o
        # Google e as IAs leem nao dizia nada — a familia da 25.9: chave ausente
        # nao declara nada.
        #
        # E A AFIRMACAO NAO PARA NA PRESENCA DA CHAVE: a data servida tem de
        # APARECER NA PROSA da propria pagina, no formato brasileiro, quando a
        # pagina publicar alguma data. Sem isso o campo poderia dizer "hoje" em
        # pagina que nao muda desde 30/10, que e precisamente a mentira que um
        # sinal de frescor pode contar — e seria uma SEGUNDA declaracao do mesmo
        # fato, que e o que a 20.7 proibe.
        datas_ld = []
        for j in jsonld:
            try:
                datas_ld += re.findall(r'"dateModified"\s*:\s*"(\d{4}-\d{2}-\d{2})', j)
            except Exception:
                pass
        afirma(len(datas_ld) >= 1,
               "%s: nenhum JSON-LD declara `dateModified`. A ilha que recoleta preco e a que mais "
               "precisa do sinal de frescor, e chave ausente nao declara nada (25.9)" % caminho)
        for d in set(datas_ld):
            br = "%s/%s/%s" % (d[8:10], d[5:7], d[:4])
            datas_na_prosa = set(re.findall(r"\d{2}/\d{2}/\d{4}", texto))
            if datas_na_prosa:
                afirma(br in datas_na_prosa,
                       "%s: o JSON-LD diz dateModified %s (%s) e a prosa da pagina nao traz essa data "
                       "em lugar nenhum (traz %s). Duas declaracoes do mesmo fato comecam iguais e so "
                       "uma sobe (20.7)"
                       % (caminho, d, br, ", ".join(sorted(datas_na_prosa)) or "nenhuma"))
            else:
                registro("%s: dateModified %s, e a pagina nao publica data em prosa para cruzar"
                         % (caminho, d))
        if datas_ld:
            registro("%s: dateModified %s" % (caminho, ", ".join(sorted(set(datas_ld)))))

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

        # A FOLHA DESTA ILHA NAO SERVE OS PROPRIOS COMENTARIOS (bloco 7).
        nossas = folhas_da_ilha(html)
        afirma(len(nossas) >= 1,
               "%s: nao serve nenhuma folha desta ilha — ou o snippet esta gravado e NAO "
               "ativado (20.7), ou a tag <style> deixou de sair da casca" % caminho)
        for problema in problemas_da_folha_servida(html):
            afirma(False, "%s: %s" % (caminho, problema))

        # E A 32.4 SOBRE O HTML SERVIDO INTEIRO, separada da de cima porque o
        # conserto de cada uma e diferente (20.5).
        for problema in problemas_de_bastidor_no_servido(html, nomes_de_arquivo):
            afirma(False, "%s: %s" % (caminho, problema))

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

    # MUNDO 10 — A CLASSE DO QUANTIFICADOR E DO SUPERLATIVO, com as TRES frases
    # REAIS que chegaram ao ar por TRES camadas diferentes em TRES dias. A
    # funcao e pura e nao precisa de rede, entao ela roda sempre.
    pegos = []

    def espiao(cond, msg):
        if not cond:
            pegos.append(msg)

    global afirma
    afirma_de_verdade = afirma
    try:
        afirma = espiao
        AS_TRES = (
            "/veiculos/bicicleta-eletrica/ é a reclamação mais comum de quem compra sem fazer essa conta",
            "/divulgacao-de-afiliados/ os dois são a maneira mais comum de prometer um aparelho",
            "/autonomia-patinete-eletrico/ É a lacuna mais comum do varejo: o anúncio grita o watt",
        )
        for i, frase in enumerate(AS_TRES):
            pegos = []
            conferir_classe_no_site("/x/", frase, ())
            diz(len(pegos) == 1,
                "10.%d a frase REAL que foi ao ar e pega pela classe: %r" % (i + 1, frase[:48]))

        # A LIBERACAO FUNCIONA, E SO PARA A ANCORA: a mesma frase com a ancora
        # declarada passa, e uma ancora de OUTRA frase nao a salva.
        pegos = []
        conferir_classe_no_site(
            "/x/", "a media simples porque a grandeza e um multiplicador",
            ("a media simples porque a grandeza e um multiplicador",))
        diz(not pegos, "10.4 ancora declarada libera a frase dela")
        pegos = []
        conferir_classe_no_site(
            "/x/", "a media simples porque a grandeza e um multiplicador",
            ("selo de mais vendido nem nota de estrela",))
        diz(len(pegos) == 1, "10.5 ancora de OUTRA frase nao libera esta")

        # A BORDA DA PALAVRA, pela licao do `Capacete1`: `na media` dentro de
        # `permeado` nao e ocorrencia.
        pegos = []
        conferir_classe_no_site("/x/", "o texto diz amaioria e nada mais", ())
        diz(not pegos, "10.6 termo colado dentro de outra palavra nao conta")

        # E A REGUA VELHA REFEITA AO LADO DA NOVA: a lista SEM o superlativo
        # APROVA as tres frases que foram ao ar, e a nova as REPROVA. Autoteste
        # em que as duas concordam nao mede conserto nenhum (20.8).
        velha = tuple(q for q in QUANTIFICADORES
                      if q not in ("mais comum", "mais comuns", "mais vendido",
                                   "mais vendida", "mais vendidos", "mais vendidas",
                                   "vende mais", "vendem mais", "mais popular",
                                   "mais populares", "a media", "na media", "da media"))

        def com_a_lista_velha(texto):
            t = _sem_acento_q(texto)
            return [q for q in velha
                    if q in t]

        for i, frase in enumerate(AS_TRES):
            pegos = []
            conferir_classe_no_site("/x/", frase, ())
            diz(not com_a_lista_velha(frase) and len(pegos) == 1,
                "10.7.%d a lista VELHA aprova a frase %r e a nova a reprova — as duas "
                "discordam" % (i + 1, frase[:40]))
    finally:
        afirma = afirma_de_verdade

    # MUNDO 11 — A FOLHA SERVIDA E A 32.4 NO BYTE SERVIDO (bloco 7, 04/11/2026).
    # As duas funcoes sao puras, entao esta metade roda SEMPRE, sem rede.
    #
    # O MUNDO 1 DESTA PARTE E O MUNDO DE VERDADE: a folha da casca como ela
    # estava no ar as 19h2xZ de 04/11/2026 — um comentario que nomeia a rotina
    # `conferir-32-5-no-navegador.mjs`, outro que diz `bancada`, e numero de
    # secao do contrato. A pagina tinha 17 blocos `<style>` do proprio
    # WordPress ao lado, e NENHUM deles pode fazer este portao reprovar.
    wp = ('<style id="wp-block-library-inline-css">/*! normalize */.wp-x{color:red}</style>'
          '<style id="global-styles-inline-css">/* auto-generated */body{margin:0}</style>')
    doente = ('<html><head>' + wp + '<style id="rodametria-casca">\n'
              '/* MEDIDO NO AR a 390 px pelo conferir-32-5-no-navegador.mjs, e a bancada\n'
              '   desta ilha roda o portao da secao 32.5 depois. */\n'
              'body.rdm{margin:0}\n</style></head><body><p>Faz uns 35 km.</p></body></html>')
    sao = ('<html><head>' + wp + '<style id="rodametria-casca">\n'
           'body.rdm{margin:0}\n</style></head><body><p>Faz uns 35 km.</p></body></html>')

    diz(len(folhas_da_ilha(doente)) == 1,
        "11.1 das 3 folhas servidas so 1 e desta ilha — as 2 do WordPress ficam de fora, "
        "porque esta ilha nao pode consertar o que nao escreve")
    diz(len(problemas_da_folha_servida(doente)) == 1,
        "11.2 a folha DOENTE e pega: comentario de CSS dentro da folha desta ilha")
    diz(problemas_da_folha_servida(sao) == [],
        "11.3 a folha SA passa, com os comentarios do WordPress intactos ao lado — portao "
        "que reprova a pagina certa e o caminho mais curto para alguem ignora-lo (20.5)")
    bast = problemas_de_bastidor_no_servido(doente, ("conferir-32-5-no-navegador.mjs",))
    diz(any("bancada" in m for m in bast),
        "11.4 a palavra de bastidor dentro do COMENTARIO da folha e pega pela 32.4 no servido")
    diz(any(".mjs" in m for m in bast),
        "11.5 a extensao de rotina dentro da folha e pega")
    diz(any("conferir-32-5-no-navegador.mjs" in m for m in bast),
        "11.6 o NOME do arquivo desta pasta dentro da folha e pego")
    diz(problemas_de_bastidor_no_servido(sao, ("conferir-32-5-no-navegador.mjs",)) == [],
        "11.7 a pagina SA passa na 32.4 do servido")

    # E A REGUA VELHA REFEITA AO LADO DA NOVA: a velha le o TEXTO VISIVEL, e
    # `corpo_da_pagina()` tira `<style>` antes de medir — entao ela APROVA a
    # pagina doente. As duas tem de discordar, senao este mundo nao mede o
    # conserto (20.8).
    def regua_velha_do_bastidor(html):
        corpo = corpo_da_pagina(html)
        texto = re.sub(r"<[^>]+>", " ", corpo)
        return [t for t in BASTIDOR if t.lower() in texto.lower()]

    diz(regua_velha_do_bastidor(doente) == [] and bast != [],
        "11.8 a regua VELHA (texto visivel) APROVA a pagina doente e a NOVA (byte servido) a "
        "REPROVA — as duas discordam, senao este autoteste nao mede o conserto")

    # MUNDO 12 — A PORTA CAIDA, FABRICADA, E AS DUAS REGUAS LADO A LADO.
    # Este mundo e o de 05/11/2026 as 10h2xZ nesta ilha, e ele existe porque o
    # portao que devia medir a queda entrava pela porta que cai. Os bytes
    # abaixo sao os que o hospedeiro serviu naquela leitura.
    pagina_do_hospedeiro = (
        '<!DOCTYPE html>\n<html lang="pt-BR">\n  <head>\n'
        '    <meta name="robots" content="noindex">\n'
        '    <title>Hospedagem de Site com Dominio Gratis - HostGator</title>\n'
        '  </head>\n  <body>\n    <h3>Erro 404</h3>\n  </body>\n</html>'
    )
    indice_de_verdade = json.dumps({"namespace": "rodametria/v1", "routes": {
        "/rodametria/v1": {}, "/rodametria/v1/casca": {},
        "/rodametria/v1/rotas": {}, "/rodametria/v1/status": {},
        "/rodametria/v1/sync": {}, "/rodametria/v1/token": {}}})

    # (a) A REGUA VELHA lia o indice pelo caminho bonito, entao com a porta no
    #     chao ela recebia a pagina do hospedeiro e concluia LISTA VAZIA.
    velha = rotas_do_indice(pagina_do_hospedeiro)
    nova = rotas_do_indice(indice_de_verdade)
    diz(velha == [] and ROTA_DA_293 in nova,
        "12. a regua VELHA (indice pelo caminho bonito) le a pagina do hospedeiro como "
        "ZERO rota, e a NOVA (?rest_route=) acha a rota — as duas DISCORDAM, senao este "
        "autoteste nao mede o conserto")

    # (b) E a discordancia nao e academica: ela trocava o DONO do defeito.
    acusacao_velha = problemas_da_parede(velha, 401, 401, "rodametria_rotas_token_invalido")
    acusacao_nova = problemas_da_parede(nova, 401, 401, "rodametria_rotas_token_invalido")
    diz(any("NAO aparece no indice" in m for m in acusacao_velha) and acusacao_nova == [],
        "12. com a porta caida a regua VELHA acusa a casca de nao registrar a rota (o "
        "conserto errado, no arquivo errado) e a NOVA nao acusa nada — a rota responde")

    # (c) O CONSERTO NAO AFROUXA O PORTAO: rota de verdade ausente continua pega.
    indice_sem_a_rota = json.dumps({"routes": {
        "/rodametria/v1": {}, "/rodametria/v1/casca": {}, "/rodametria/v1/status": {}}})
    ausente = problemas_da_parede(rotas_do_indice(indice_sem_a_rota), 404, 404, None)
    diz(any("NAO aparece no indice" in m for m in ausente),
        "12. rota DE VERDADE ausente segue sendo pega pela regua nova — o conserto nao "
        "afrouxou a afirmacao, so trocou a porta por onde ela entra")

    # (d) O JSON QUE NAO E DICIONARIO nao pode virar excecao nem rota inventada.
    diz(rotas_do_indice("[]") == [] and rotas_do_indice('{"routes": null}') == [],
        "12. indice que nao e dicionario, e `routes` nulo, devolvem lista vazia sem "
        "estourar — a pagina do hospedeiro nao e o unico corpo que nao e indice")

    # MUNDO 13 — O DIAGNOSTICO NOMEADO, E AS QUATRO GRANDEZAS QUE ELE EXIGE.
    # A causa so e nomeada quando as quatro estao na mesa; fora disso o portao
    # prefere nao dizer causa nenhuma (29.5: causa inventada e a proxima
    # execucao consertando a coisa errada).
    caiu = diagnostico_da_porta(200, [404, 404, 404], True)
    diz(caiu is not None and "PORTA DE ENTRADA CAIU" in caiu and "flush_rewrite_rules" in caiu,
        "13. o mundo de 05/11 e NOMEADO: home 200, as tres portas em 404, REST vivo — e a "
        "linha traz o conserto, nao so o sintoma")

    diz(diagnostico_da_porta(200, [200, 200, 200], True) is None,
        "13. o mundo SADIO nao nomeia causa nenhuma")

    diz(diagnostico_da_porta(404, [404, 404, 404], True) is None,
        "13. home TAMBEM morta nao e esta causa — o site inteiro fora do ar e outro "
        "mundo, e o portao devolve None em vez de nomear a errada")

    diz(diagnostico_da_porta(200, [404, 404, 404], False) is None,
        "13. REST morto nas DUAS formas nao e esta causa: o que esta assinatura exige e o "
        "WordPress de pe atras de uma porta fechada")

    diz(diagnostico_da_porta(200, [404, 200, 404], True) is None,
        "13. UMA das portas viva ja nao e esta assinatura — ela cobra as tres juntas, "
        "porque as tres sao rota virtual e caem juntas")

    diz(diagnostico_da_porta(200, [], True) is None,
        "13. sem porta medida nenhuma nao se nomeia causa — lista vazia nao e prova de "
        "que as portas estao mortas, e `all()` sobre vazio diria que sim")

    print("conferir-no-ar --autoteste: %d de %d afirmacoes, %d falha(s)"
          % (len(ok), len(ok) + len(mal), len(mal)))
    for m in mal:
        print("  REPROVADO: %s" % m)
    print("APROVADO" if not mal else "REPROVADO")

    return 1 if mal else 0


if __name__ == "__main__":
    sys.exit(autoteste() if "--autoteste" in sys.argv else main())
