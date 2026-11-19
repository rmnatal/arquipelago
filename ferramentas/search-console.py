#!/usr/bin/env python3
"""
Leitura da Search Console pela nuvem — Projeto Arquipélago.

Uso:
    python3 ferramentas/search-console.py <ilha> [--dias 7] [--json]

    <ilha>  slug da ilha (aquametria, robometria...). A propriedade é
            sempre a de domínio: sc-domain:<ilha>.com.br

Credencial: variável de ambiente GOOGLE_SA_B64 (o JSON da conta de serviço em base64,
uma linha só — é o que a caixa de variáveis do ambiente aceita); alternativas GOOGLE_SA_JSON
(conteúdo cru) ou GOOGLE_SA_FILE (caminho). Nunca no repositório.

Saída (markdown pronto para colar nas séries da ilha):
    0) TOTAIS DA PROPRIEDADE, sem dimensão nenhuma (cliques, impressões, CTR, posição média)
    1) linha para dados/indexacao.md  (URLs no sitemap × URLs indexadas)
    2) linhas para dados/posicoes.md  (consulta, página, posição, impressões, cliques, banda)
    3) TABELA POR PÁGINA, dimensão `page` sozinha (página, posição, impressões, cliques, banda)
    4) as URLs NÃO INDEXADAS, nomeadas com o `coverageState` da URL Inspection
    5) as URLs SEM VEREDITO, em seção própria — fora da conta de indexadas E fora
       da conta de não indexadas (ver `veredito_de_indexacao()`)

POR QUE AS SAÍDAS 0 E 3 EXISTEM, e a lição é de 07/10/2026. Até aquela data este
script lia SÓ a dimensão `query`, e somava as linhas dela para dizer quantas
impressões a ilha teve. O Google ANONIMIZA a consulta da esmagadora maioria das
impressões de cauda longa: na aquametria, naquela janela, 370 das 371. O script
emitiu "1 impressão, 0 clique" para uma ilha que a Search Console mostrava com
**371 impressões e 3 cliques** — duas ordens de grandeza a menos, na semana dos
primeiros cliques da história do projeto.

E o custo não era de relatório: uma Sentinela que lesse só o arquivo da nuvem
teria escrito "ainda sem dado" e mantido a rampa. O script não estava errado no
que media; estava medindo a dimensão que o Google esvazia. **Total de propriedade
não depende de dimensão nenhuma, e a dimensão `page` não é anonimizada** — então
as duas passaram a sair, e a soma da dimensão `query` deixou de ser a medida da
ilha. Despacho da Sentinela de 07/10/2026, item 2.

POR QUE A SAÍDA 5 EXISTE, e a lição é de 14/10/2026 (item 4 da leitura semanal da
aquametria). A conta de indexação tinha DOIS estados — `verdict == "PASS"` ou não —
e a URL Inspection não devolveu veredito nenhum para a home da aquametria. O script
imprimiu `- / — ?` na lista de NÃO INDEXADAS, e a ilha saiu da leitura com 49 de 52
quando o número honesto era 50: a home estava indexada, com 4 impressões na posição
2,3 na mesma janela. **Status desconhecido lido como status negativo subestima a ilha
em silêncio** — é a mesma família do defeito da saída 0, onde a dimensão que o Google
esvazia era lida como a medida da ilha. Agora são três estados, o desconhecido tem
seção própria, e a dimensão `page` da mesma janela é o que prova indexação quando a
URL Inspection não dá veredito: impressão em busca é prova de que o Google serve a URL.

O CAMINHO DO SITEMAP É PERGUNTADO À PROPRIEDADE, e a lição é de 19/11/2026. Este
script adivinhava: dois candidatos fixos, `wp-sitemap.xml` e depois `sitemap.xml`.
A variável de erro era SOBRESCRITA a cada candidato, então quando os dois falhavam a
mensagem nomeava só o último — e a leitura semanal de 18/11/2026 leu
`rodametria.com.br/sitemap.xml -> ProxyError` e concluiu, por escrito, que o script
"busca /sitemap.xml" e que o conserto do caminho era da Fundação. Não era: o
`wp-sitemap.xml` já era o primeiro candidato, a causa única era o egresso, e o item
de despacho saiu endereçado a quem não tinha o que fazer. Agora `sitemaps.list`
devolve o caminho que o Google de fato lê, os palpites ficam atrás dele declarados
como palpite, e o erro nomeia TODOS os candidatos tentados com a causa de cada um.

Dependência: google-auth — instalado num venv próprio (~/.venv-search-console) na 1ª execução.
"""
import json, os, sys, datetime as dt, subprocess, urllib.request, urllib.parse, re

def _bootstrap_venv():
    """O Python do ambiente das rotinas tem o pacote `cryptography` do sistema quebrado
    (`_cffi_backend` ausente, pyo3 PanicException). Em vez de depender dele, o script cria
    um venv próprio uma vez (~/.venv-search-console), instala google-auth lá e se re-executa."""
    if os.environ.get("SC_VENV") == "1":
        sys.exit("google-auth não importa nem dentro do venv próprio — ambiente Python inutilizável.")
    venv = os.path.expanduser("~/.venv-search-console")
    py = os.path.join(venv, "bin", "python3")
    if not os.path.exists(py):
        subprocess.check_call([sys.executable, "-m", "venv", venv])
        env = {k: v for k, v in os.environ.items() if k != "PYTHONPATH"}
        for tentativa in range(3):
            if subprocess.call([py, "-m", "pip", "install", "-q", "google-auth", "requests"], env=env) == 0:
                break
        else:
            sys.exit("pip não conseguiu instalar google-auth no venv (3 tentativas).")
    os.environ["SC_VENV"] = "1"
    os.execv(py, [py] + sys.argv)


try:
    from google.oauth2 import service_account
    from google.auth.transport.requests import AuthorizedSession
except BaseException:          # BaseException de propósito: o pyo3 lança PanicException
    _bootstrap_venv()

SCOPE = ["https://www.googleapis.com/auth/webmasters.readonly"]
API = "https://searchconsole.googleapis.com"


def credenciais():
    """Aceita, nesta ordem: GOOGLE_SA_B64 (JSON em base64, uma linha — o formato que a caixa
    de variáveis do ambiente aceita), GOOGLE_SA_JSON (conteúdo cru) ou GOOGLE_SA_FILE (caminho)."""
    import base64
    b64 = os.environ.get("GOOGLE_SA_B64", "").strip().strip("'\"")
    raw = os.environ.get("GOOGLE_SA_JSON", "").strip().strip("'\"")
    path = os.environ.get("GOOGLE_SA_FILE")
    if b64:
        raw = base64.b64decode(b64).decode("utf-8-sig")
    if raw:
        info = json.loads(raw)
        return service_account.Credentials.from_service_account_info(info, scopes=SCOPE)
    if path:
        return service_account.Credentials.from_service_account_file(path, scopes=SCOPE)
    sys.exit("Sem credencial: defina GOOGLE_SA_B64 (base64), GOOGLE_SA_JSON (conteúdo) ou GOOGLE_SA_FILE (caminho).")


def banda(pos, impressoes):
    if impressoes == 0:
        return "sem impressão"
    if pos >= 21:
        return "21+"
    if pos >= 11:
        return "11-20"
    if pos >= 4:
        return "4-10"
    return "1-3"


def totais(resposta):
    """Os totais da propriedade, lidos da consulta SEM dimensão.

    Função pura e separada de propósito: ela é a metade do item 2 do despacho de
    07/10/2026 que NÃO pode depender de dimensão, e separá-la é o que deixa a
    bancada medi-la sem rede (ver ferramentas/teste-search-console.py).

    Resposta sem linha nenhuma devolve zeros e `medido: False` — e essa é a
    diferença que custou a leitura de 07/10: "zero medido" e "não medido" não são
    o mesmo número, e quem some com a distinção publica o primeiro no lugar do
    segundo.
    """
    linhas = (resposta or {}).get("rows") or []
    if not linhas:
        return {"cliques": 0, "impressoes": 0, "ctr": 0.0, "posicao": 0.0, "medido": False}
    linha = linhas[0]
    impressoes = int(linha.get("impressions", 0))
    cliques = int(linha.get("clicks", 0))
    return {
        "cliques": cliques,
        "impressoes": impressoes,
        # O CTR vem da API, mas é recalculado quando ela não o manda: dois campos
        # para o mesmo quociente divergem, e aqui o que manda é a divisão.
        "ctr": float(linha.get("ctr", (cliques / impressoes) if impressoes else 0.0)),
        "posicao": float(linha.get("position", 0.0)),
        "medido": True,
    }


def por_pagina(resposta, dominio):
    """As linhas da dimensão `page`, já ordenadas por impressão e com a banda.

    A dimensão `page` não é anonimizada pelo Google, então esta é a tabela que
    diz quais páginas da ilha estão sendo vistas — a informação que a soma da
    dimensão `query` esconde quando a consulta é esvaziada.
    """
    saida = []
    for linha in (resposta or {}).get("rows") or []:
        chaves = linha.get("keys") or []
        if not chaves:
            continue
        pagina = chaves[0]
        if dominio:
            pagina = pagina.replace("https://%s" % dominio, "")
        impressoes = int(linha.get("impressions", 0))
        pos = float(linha.get("position", 0.0))
        saida.append({
            "pagina": pagina,
            "posicao": pos,
            "impressoes": impressoes,
            "cliques": int(linha.get("clicks", 0)),
            "banda": banda(pos, impressoes),
        })
    saida.sort(key=lambda x: (-x["impressoes"], x["pagina"]))
    return saida


def caminho_de(url, dominio):
    """O caminho de uma URL, sem o domínio, sem query e sem âncora, com a raiz como `/`.

    Existe para a lista do sitemap (URLs inteiras) e a tabela da dimensão `page`
    (caminhos) poderem ser cruzadas por chave igual. Sem isto o cruzamento falha
    exatamente na home, que é a URL em que o domínio é a string inteira.
    """
    for prefixo in ("https://%s" % dominio, "http://%s" % dominio):
        if url.startswith(prefixo):
            url = url[len(prefixo):]
            break
    url = url.split("?")[0].split("#")[0]
    return url or "/"


def impressoes_por_caminho(paginas):
    """Mapa caminho -> impressões, a partir da saída de `por_pagina()`.

    A chave é guardada nas duas grafias de barra final, porque a Search Console e
    o sitemap discordam nisso com frequência e um cruzamento que falha por uma
    barra produz exatamente o defeito que esta medição existe para evitar.
    """
    mapa = {}
    for x in paginas or []:
        c = x["pagina"] or "/"
        for chave in {c, c.rstrip("/") or "/", (c if c.endswith("/") else c + "/")}:
            mapa[chave] = max(mapa.get(chave, 0), int(x["impressoes"]))
    return mapa


def veredito_de_indexacao(inspecao, impressoes=0):
    """Classifica UMA URL em TRÊS estados, e é por isso que esta função existe.

    O defeito, medido na aquametria em 14/10/2026 e nomeado pelo item 4 da leitura
    semanal daquele dia: a conta era `ok = verdict == "PASS"`, com dois estados
    só. A URL Inspection não devolveu veredito nenhum para a home da aquametria —
    `indexStatusResult` ausente, `verdict` ausente — e o script imprimiu `?` na
    lista de **não indexadas**. A home estava indexada: 4 impressões na posição
    2,3 na mesma janela. A ilha saiu subestimada em uma URL (49 em vez de 50), e
    o `?` passou por conta em vez de passar por "não soube".

    **Status desconhecido não é status negativo.** Os três estados:
      - `indexada`      — a URL Inspection deu `PASS`; ou não deu veredito e a
                          dimensão `page` da MESMA janela registra impressão para
                          a URL, o que é prova de que o Google a serve em busca.
      - `nao_indexada`  — veredito presente e diferente de `PASS`. Fica NOMEADA,
                          com o `coverageState` que a API devolveu.
      - `sem_veredito`  — nenhum veredito e nenhuma impressão. Fora das duas
                          contas, impresso como desconhecido.

    O campo `divergencia` acusa o contrário do defeito de cima: veredito negativo
    em URL com impressão na mesma janela. Não muda conta nenhuma — a medição de
    quem tem veredito manda —, mas o instrumento discordando de si mesmo tem de
    sair escrito em vez de passar em silêncio.
    """
    st = ((inspecao or {}).get("inspectionResult") or {}).get("indexStatusResult") or {}
    verdict = (st.get("verdict") or "").strip()
    cobertura = st.get("coverageState") or ""
    impressoes = int(impressoes or 0)
    desconhecido = verdict in ("", "?", "VERDICT_UNSPECIFIED")

    if desconhecido:
        if impressoes > 0:
            return {"estado": "indexada", "cobertura": cobertura,
                    "fonte": "impressão medida (%d na janela) — a URL Inspection não deu veredito" % impressoes,
                    "impressoes": impressoes, "divergencia": ""}
        return {"estado": "sem_veredito", "cobertura": cobertura or "sem veredito",
                "fonte": "a URL Inspection não devolveu veredito e a janela não tem impressão desta URL",
                "impressoes": 0, "divergencia": ""}

    if verdict == "PASS":
        return {"estado": "indexada", "cobertura": cobertura, "fonte": "URL Inspection",
                "impressoes": impressoes, "divergencia": ""}

    return {"estado": "nao_indexada", "cobertura": cobertura or verdict, "fonte": "URL Inspection",
            "impressoes": impressoes,
            "divergencia": ("veredito %s com %d impressão(ões) medidas na mesma janela" % (verdict, impressoes))
                           if impressoes > 0 else ""}


def resumo_de_indexacao(detalhes, total_urls=None):
    """A conta das três listas, com o piso e o teto da taxa quando há desconhecido.

    `indexadas` é o número que vai para a série de `dados/indexacao.md`, e ele NÃO
    inclui as URLs sem veredito — elas não são indexadas nem não indexadas. Por
    isso a taxa sai como faixa quando existe desconhecido: `pct` é o piso (o que
    está provado) e `pct_teto` é o que ela seria se todo desconhecido estivesse no
    índice. Uma taxa única sobre denominador que contém desconhecido é a mesma
    família de defeito que esta função conserta — afirmar o que não se mediu.
    """
    total = len(detalhes) if total_urls is None else int(total_urls)
    ind = [d for d in detalhes if d["estado"] == "indexada"]
    nao = [d for d in detalhes if d["estado"] == "nao_indexada"]
    sem = [d for d in detalhes if d["estado"] == "sem_veredito"]
    return {
        "total": total,
        "indexadas": len(ind),
        "nao_indexadas": len(nao),
        "sem_veredito": len(sem),
        "por_impressao": len([d for d in ind if d["fonte"].startswith("impressão")]),
        "divergencias": [d for d in detalhes if d.get("divergencia")],
        "pct": (100.0 * len(ind) / total) if total else None,
        "pct_teto": (100.0 * (len(ind) + len(sem)) / total) if total else None,
        "lista_indexadas": ind,
        "lista_nao_indexadas": nao,
        "lista_sem_veredito": sem,
    }


def relatorio_de_indexacao(hoje, urls, resumo, impressoes_total, cliques_total,
                           erro_sitemap="", avisos=()):
    """As LINHAS da parte de indexação do relatório, como lista de texto.

    Por que isto é função e não `print` solto dentro do `main()`: metade do
    critério de pronto do item 4 da leitura semanal de 14/10/2026 é sobre o que o
    script **imprime** — "imprimir a home numa seção própria de sem veredito" —, e
    `print` dentro do `main()` só se confere com credencial e rede. Com as linhas
    devolvidas, o portão sem rede confere as seções e os números do mesmo mundo que
    a leitura mediu. É a mesma razão de `totais()` e `por_pagina()` existirem.

    Devolve `{"serie": [...], "urls": [...]}` — duas partes porque elas saem em
    lugares diferentes do relatório: a linha da série vai no topo, perto dos
    totais, e as listas de URL vão no fim, depois das tabelas de posição.
    """
    linhas = []
    pct = f"{resumo['pct']:.0f}%" if urls else "n/d"
    linhas.append("### linha para dados/indexacao.md")
    linhas.append(f"| {hoje.isoformat()} | {len(urls) or 'n/d'} | "
                  f"{resumo['indexadas'] if urls else 'n/d'} | {pct} | "
                  f"{impressoes_total} | {cliques_total} |")
    if not urls:
        # Uma linha por candidato, nunca o erro inteiro colado numa so: a mensagem
        # que some com o que o instrumento tentou e o defeito de 19/11/2026, e o
        # relatorio e onde ela e LIDA por uma pessoa.
        partes = (erro_sitemap or "vazio").splitlines() or ["vazio"]
        linhas.append(f"(sitemap não lido: {partes[0]})")
        for l in partes[1:]:
            linhas.append(l)
    else:
        # As três contas somam o total, e dizer isso por extenso é o que impede
        # alguém de ler `indexadas` como "o resto não está no índice".
        linhas.append(f"- a conta é de TRÊS estados: **{resumo['indexadas']} indexada(s)**, "
                      f"**{resumo['nao_indexadas']} não indexada(s)** e "
                      f"**{resumo['sem_veredito']} sem veredito**, em {resumo['total']} URL(s) do sitemap.")
        if resumo["por_impressao"]:
            linhas.append(f"- {resumo['por_impressao']} delas conta(m) como indexada(s) por "
                          f"**impressão medida nesta mesma janela**, sem veredito da URL Inspection — "
                          f"ver a seção abaixo. Impressão em busca é prova de que o Google serve a URL.")
        if resumo["sem_veredito"]:
            linhas.append(f"- a taxa de indexação está **entre {resumo['pct']:.0f}% e {resumo['pct_teto']:.0f}%**: "
                          f"o piso é o que está provado, o teto é o que seria se todas as sem veredito "
                          f"estivessem no índice. **Status desconhecido fica fora das duas contas** — "
                          f"nunca somado às não indexadas.")
    for a in avisos or ():
        linhas.append(f"- {a}")
    serie, linhas = linhas, []
    if not urls:
        return {"serie": serie, "urls": []}

    linhas += ["### URLs não indexadas (URL Inspection)"]
    if not resumo["lista_nao_indexadas"]:
        linhas.append("(nenhuma — toda URL do sitemap com veredito deu `PASS`)")
    for d in resumo["lista_nao_indexadas"]:
        linhas.append(f"- {d['caminho']} — {d['cobertura']}")

    linhas += ["", "### URLs sem veredito da URL Inspection — NÃO são não indexadas"]
    if not resumo["lista_sem_veredito"]:
        # A frase precisa distinguir "todas tiveram veredito" de "as sem veredito
        # foram resolvidas por impressão". As duas dão lista vazia aqui, e dizer a
        # primeira quando valia a segunda é a mesma imprecisão que esta função
        # conserta um andar acima.
        linhas.append("(nenhuma sobrou sem conta: %d sem veredito resolvida(s) por impressão medida — ver a seção abaixo)"
                      % resumo["por_impressao"] if resumo["por_impressao"]
                      else "(nenhuma — a URL Inspection deu veredito para toda URL do sitemap)")
    for d in resumo["lista_sem_veredito"]:
        linhas.append(f"- {d['caminho']} — **desconhecido**: {d['fonte']}")
    if resumo["lista_sem_veredito"]:
        linhas.append("- estas ficam FORA da conta de indexadas e FORA da conta de não indexadas. "
                      "O instrumento não soube, e não saber é o que está escrito aqui.")

    if resumo["por_impressao"]:
        linhas += ["", "### URLs SEM VEREDITO da URL Inspection, mas INDEXADAS por impressão medida"]
        for d in resumo["lista_indexadas"]:
            if d["fonte"].startswith("impressão"):
                linhas.append(f"- {d['caminho']} — {d['fonte']}")

    if resumo["divergencias"]:
        linhas += ["", "### DIVERGÊNCIA DO INSTRUMENTO — veredito negativo em URL com impressão na janela"]
        for d in resumo["divergencias"]:
            linhas.append(f"- {d['caminho']} — {d['divergencia']} (cobertura: {d['cobertura']})")
        linhas.append("- a conta mantém o veredito da URL Inspection; a linha existe para a contradição "
                      "não passar em silêncio, que é como o defeito de 14/10/2026 durou uma semana.")
    return {"serie": serie, "urls": linhas}


def caminhos_declarados(resposta, dominio):
    """Os sitemaps que a PRÓPRIA PROPRIEDADE declara, lidos de `sitemaps.list`.

    Função pura e separada de propósito, pela mesma razão de `totais()` e
    `por_pagina()`: o portão sem rede (`ferramentas/teste-search-console.py`) mede a
    escolha do caminho sem credencial nenhuma.

    POR QUE ELA EXISTE, e a lição é de 19/11/2026. Até hoje este script ADIVINHAVA o
    caminho do sitemap: dois candidatos fixos, `wp-sitemap.xml` e `sitemap.xml`, nessa
    ordem. Adivinhar acerta em WordPress e erra calado em qualquer ilha que declare
    outro caminho — e "erra calado" aqui é a linha da série de indexação saindo `n/d`
    com cara de ilha sem dado. O Google sabe o caminho, porque é a ele que o sitemap
    foi submetido: `GET /webmasters/v3/sites/<prop>/sitemaps` devolve o `path` de cada
    um. Perguntar à propriedade é mais barato e mais honesto que adivinhar.

    Filtra pelo HOST da ilha de propósito: propriedade de domínio pode ter sitemap
    submetido em subdomínio que esta leitura não mede, e buscar host de fora faria o
    instrumento sair da ilha que ele está medindo.

    Devolve lista na ordem da API, sem repetição. Resposta vazia ou sem `sitemap`
    devolve lista vazia, e isso NÃO é erro: é a propriedade não ter declarado nada, e
    aí os dois candidatos fixos seguem valendo como palpite — dito como palpite.
    """
    saida, vistos = [], set()
    for s in ((resposta or {}).get("sitemap") or []):
        caminho = (s.get("path") or "").strip()
        if not caminho or caminho in vistos:
            continue
        try:
            host = urllib.parse.urlparse(caminho).netloc.lower()
        except Exception:
            continue
        if host not in (dominio.lower(), f"www.{dominio.lower()}"):
            continue
        vistos.add(caminho)
        saida.append(caminho)
    return saida


def urls_do_sitemap(dominio, declarados=()):
    """Lê o sitemap do site com o mesmo cliente HTTP que fala com a API (requests, que respeita
    o proxy e a CA do ambiente). Devolve (urls, erro, avisos) — erro é texto quando nada foi lido.

    `declarados` são os caminhos que a própria propriedade declarou (ver
    `caminhos_declarados()`); eles vêm PRIMEIRO, e os dois fixos ficam atrás como
    palpite para a ilha que não declarou nada.

    O `erro` NOMEIA TODOS OS CANDIDATOS TENTADOS, UM POR LINHA, E DIZ QUANTOS FORAM —
    e isso é o conserto de 19/11/2026, que custou um item de despacho endereçado a
    quem não tinha o que fazer. Até hoje a variável `erro` era SOBRESCRITA a cada
    candidato, então a mensagem saía nomeando só o ÚLTIMO: `rodametria.com.br/sitemap.xml
    -> ProxyError`. A leitura semanal de 18/11/2026 leu aquela linha e concluiu, por
    escrito, que o script *"busca `https://rodametria.com.br/sitemap.xml`"* e que o
    conserto do caminho era da Fundação — quando o `wp-sitemap.xml` já era o primeiro
    candidato desde antes, e a causa única era o egresso. **Mensagem de instrumento que
    some com o que ele tentou produz diagnóstico errado com dono errado**, e é a família
    da 20.4: resumo lido como se fosse a passada inteira.
    """
    import requests
    urls, erros, avisos = [], [], []
    candidatos, vistos = [], set()
    for c in list(declarados) + [f"https://{dominio}/wp-sitemap.xml", f"https://{dominio}/sitemap.xml"]:
        if c not in vistos:
            vistos.add(c)
            candidatos.append(c)
    for candidato in candidatos:
        origem = "declarado pela propriedade" if candidato in tuple(declarados) else "palpite fixo do script"
        try:
            r = requests.get(candidato, timeout=30, headers={"User-Agent": "arquipelago-sentinela"})
            xml = r.text
            if r.status_code != 200:
                if "<sitemapindex" in xml or "<urlset" in xml:
                    # WordPress devolvendo XML válido com status 404: o Google NÃO lê. É defeito da ilha.
                    avisos.append(f"DEFEITO: {candidato} responde HTTP {r.status_code} com XML válido — o Google trata como sitemap inexistente")
                else:
                    erros.append(f"{candidato} ({origem}) -> HTTP {r.status_code}")
                    continue
        except Exception as e:
            erros.append(f"{candidato} ({origem}) -> {type(e).__name__}: {e}")
            continue
        subs = re.findall(r"<loc>([^<]+)</loc>", xml)
        for s in subs:
            if s.endswith(".xml"):
                try:
                    r2 = requests.get(s, timeout=30, headers={"User-Agent": "arquipelago-sentinela"})
                    if r2.status_code != 200:
                        avisos.append(f"DEFEITO: {s} responde HTTP {r2.status_code}")
                    urls += re.findall(r"<loc>([^<]+)</loc>", r2.text)
                except Exception as e:
                    erros.append(f"{s} (sub-sitemap de {candidato}) -> {type(e).__name__}: {e}")
            else:
                urls.append(s)
        if urls:
            break
    erro = ""
    if not urls:
        erro = (f"{len(candidatos)} caminho(s) tentado(s), nenhum devolveu URL"
                + (f" — {len(declarados)} declarado(s) pela propriedade" if declarados
                   else " — a propriedade não declarou nenhum, os dois são palpite fixo")
                + ":\n"
                + "\n".join(f"    - {e}" for e in erros or ["(nenhuma tentativa registrou causa)"]))
    return sorted(set(urls)), erro, avisos


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    ilha = sys.argv[1].strip().lower()
    dias = 7
    if "--dias" in sys.argv:
        dias = int(sys.argv[sys.argv.index("--dias") + 1])
    dominio = f"{ilha}.com.br"
    prop = f"sc-domain:{dominio}"
    sess = AuthorizedSession(credenciais())

    # 0) a conta enxerga a propriedade?
    sites = sess.get(f"{API}/webmasters/v3/sites").json()
    vistos = [s["siteUrl"] for s in sites.get("siteEntry", [])]
    if prop not in vistos:
        sys.exit(f"A conta de serviço não tem acesso a {prop}. Propriedades visíveis: {vistos}")

    hoje = dt.date.today()
    fim = hoje - dt.timedelta(days=2)          # SC atrasa ~2 dias
    ini = fim - dt.timedelta(days=dias - 1)

    rota = f"{API}/webmasters/v3/sites/{urllib.parse.quote(prop, safe='')}/searchAnalytics/query"
    janela = {"startDate": ini.isoformat(), "endDate": fim.isoformat()}

    # 1) posições por consulta+página
    r = sess.post(rota, json=dict(janela, dimensions=["query", "page"], rowLimit=500)).json()
    linhas = r.get("rows", [])

    # 1b) OS TOTAIS DA PROPRIEDADE, sem dimensão nenhuma (item 2 do despacho de
    #     07/10/2026). A soma da dimensão `query` NÃO serve para isto: o Google
    #     anonimiza a consulta da cauda longa e aquela soma deu 1 impressão numa
    #     janela de 371. O que vale como medida da ilha é esta linha.
    t = totais(sess.post(rota, json=dict(janela, dimensions=[])).json())
    impressoes_total = t["impressoes"]
    cliques_total = t["cliques"]

    # 1c) a dimensão `page` sozinha, que o Google não anonimiza
    paginas = por_pagina(sess.post(rota, json=dict(janela, dimensions=["page"], rowLimit=500)).json(),
                         dominio)

    # A soma da dimensão `query`, guardada SÓ para a comparação aparecer no
    # relatório: é ela que mentia, e deixá-la à vista ao lado do total é o que
    # impede o defeito de 07/10 de voltar sem sintoma.
    impressoes_por_consulta = sum(int(x["impressions"]) for x in linhas)
    cliques_por_consulta = sum(int(x["clicks"]) for x in linhas)

    # 2) indexação: URL Inspection por URL do sitemap (cota 2000/dia — ok para ilhas pequenas)
    #    A classificação é de TRÊS estados e mora em `veredito_de_indexacao()`: status
    #    desconhecido não entra na conta das não indexadas (item 4 da leitura semanal
    #    de 14/10/2026). O mapa de impressões da dimensão `page` entra aqui porque é
    #    ele que prova indexação quando a URL Inspection não dá veredito.
    #    O CAMINHO DO SITEMAP SAI DA PROPRIEDADE, NAO DE PALPITE (19/11/2026): a
    #    `sitemaps.list` devolve o `path` de cada sitemap submetido, e e esse que o
    #    Google le. Os dois candidatos fixos ficam atras, como palpite para a ilha
    #    que nao declarou nada. Falha AQUI nao mata a leitura — degrada para o
    #    palpite e DIZ que degradou, porque instrumento que cala a propria limitacao
    #    e o defeito que esta mesma passada consertou um andar abaixo.
    declarados, aviso_declaracao = [], ""
    try:
        rs = sess.get(f"{API}/webmasters/v3/sites/{urllib.parse.quote(prop, safe='')}/sitemaps")
        if rs.status_code == 200:
            declarados = caminhos_declarados(rs.json(), dominio)
            if not declarados:
                aviso_declaracao = ("a propriedade NAO declara sitemap nenhum no host desta ilha "
                                    "(`sitemaps.list` respondeu 200 e veio vazio) — os caminhos "
                                    "abaixo sao palpite do script, nao declaracao do site")
        else:
            aviso_declaracao = (f"`sitemaps.list` respondeu HTTP {rs.status_code}: o caminho do sitemap "
                                f"desta leitura e PALPITE do script, nao o que a propriedade declara")
    except Exception as e:
        aviso_declaracao = (f"`sitemaps.list` nao respondeu ({type(e).__name__}): o caminho do sitemap "
                            f"desta leitura e PALPITE do script, nao o que a propriedade declara")
    urls, erro_sitemap, avisos = urls_do_sitemap(dominio, declarados=declarados)
    if aviso_declaracao:
        avisos = list(avisos) + [aviso_declaracao]
    elif declarados:
        avisos = list(avisos) + [f"caminho do sitemap DECLARADO pela propriedade: {', '.join(declarados)}"]
    impressoes_pagina = impressoes_por_caminho(paginas)
    detalhes = []
    for u in urls:
        caminho = caminho_de(u, dominio)
        ins = sess.post(f"{API}/v1/urlInspection/index:inspect",
                        json={"inspectionUrl": u, "siteUrl": prop}).json()
        v = veredito_de_indexacao(ins, impressoes_pagina.get(caminho, 0))
        v["url"], v["caminho"] = u, caminho
        detalhes.append(v)
    resumo = resumo_de_indexacao(detalhes, len(urls))
    indexadas = resumo["indexadas"]

    if "--json" in sys.argv:
        print(json.dumps({"ilha": ilha, "propriedade": prop, "periodo": [ini.isoformat(), fim.isoformat()],
                          "urls_sitemap": len(urls), "indexadas": indexadas,
                          "indexacao": {k: v for k, v in resumo.items() if not k.startswith("lista_")},
                          "impressoes": impressoes_total, "cliques": cliques_total,
                          "totais_da_propriedade": t, "por_pagina": paginas,
                          "impressoes_por_consulta": impressoes_por_consulta,
                          "cliques_por_consulta": cliques_por_consulta,
                          "posicoes": linhas, "inspecao": detalhes, "erro_sitemap": erro_sitemap, "avisos": avisos}, ensure_ascii=False, indent=1))
        return

    print(f"## {ilha} — leitura Search Console {hoje.isoformat()} (janela {ini}→{fim})")
    print()
    print("### totais da propriedade (sem dimensão nenhuma)")
    if t["medido"]:
        print(f"- **{t['cliques']} clique(s)**, **{t['impressoes']} impressão(ões)**, "
              f"CTR {100*t['ctr']:.1f}%, posição média {t['posicao']:.1f}")
    else:
        print("- a API não devolveu linha para a janela: NÃO MEDIDO (não é zero)")
    print(f"- a soma da dimensão `query` nesta mesma janela dá "
          f"{impressoes_por_consulta} impressão(ões) e {cliques_por_consulta} clique(s). "
          f"A diferença é a anonimização da consulta pelo Google, não defeito do site — "
          f"e é por isso que o número de cima é o que vale.")
    print()
    # A parte de indexação sai de `relatorio_de_indexacao()`, que é função pura e
    # tem portão sem rede: metade do critério do item 4 de 14/10/2026 é sobre o que
    # se IMPRIME, e `print` solto só se confere com credencial na mão.
    rel_indexacao = relatorio_de_indexacao(hoje, urls, resumo, impressoes_total,
                                           cliques_total, erro_sitemap, avisos)
    for l in rel_indexacao["serie"]:
        print(l)
    print()
    print("### linhas para dados/posicoes.md")
    print("| consulta | página | posição hoje | impressões | cliques | banda |")
    for x in sorted(linhas, key=lambda z: -int(z["impressions"]))[:60]:
        q, pg = x["keys"]
        pos = float(x["position"])
        pg = pg.replace(f"https://{dominio}", "")
        print(f"| {q} | {pg} | {pos:.1f} | {int(x['impressions'])} | {int(x['clicks'])} | {banda(pos, int(x['impressions']))} |")
    print()
    print("### linhas por PÁGINA para dados/posicoes.md (dimensão `page`, não anonimizada)")
    print("| página | posição hoje | impressões | cliques | banda |")
    if not paginas:
        print("(a API não devolveu página nenhuma nesta janela)")
    for x in paginas[:60]:
        print(f"| {x['pagina']} | {x['posicao']:.1f} | {x['impressoes']} | {x['cliques']} | {x['banda']} |")

    if rel_indexacao["urls"]:
        print()
        for l in rel_indexacao["urls"]:
            print(l)


if __name__ == "__main__":
    main()
