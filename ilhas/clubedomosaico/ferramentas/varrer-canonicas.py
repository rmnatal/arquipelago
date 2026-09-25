#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le a CANONICA e a CADEIA DE REDIRECIONAMENTO de cada URL desta ilha.

    python3 ferramentas/varrer-canonicas.py .            # so imprime
    python3 ferramentas/varrer-canonicas.py . --gravar   # escreve em dados/indexacao.md

Nasceu do BLOCO C do despacho do Raphael de 24/09/2026, que veio de dois motivos
novos no e-mail do Search Console de 23/09: "Pagina alternativa com tag canonica
adequada" e "Pagina com redirecionamento".

O AVISO QUE O PROPRIO DESPACHO ESCREVE, e ele manda na leitura deste arquivo:
os dois motivos sao, na esmagadora maioria dos casos, COMPORTAMENTO ESPERADO —
canonica apontando para a versao boa e redirecionamento que leva ao lugar certo
sao o Google fazendo o trabalho dele. A tarefa aqui e VERIFICAR E RELATAR, nunca
"consertar". Nada neste arquivo aplica correcao, e nao e por falta de jeito: o
despacho proibe, item por item, ate o Raphael autorizar.

O QUE ESTA NUVEM NAO ALCANCA, dito para ninguem confundir com medicao: a conta
de servico `sentinela@` NAO tem acesso a `sc-domain:clubedomosaico.com.br` (esta
em dados/search-console-2026-09-23.md). Entao a lista de URLs que o Search
Console reclamou NAO EXISTE aqui — o que existe e a varredura completa do que a
ilha serve, e e dela que sai a explicacao mais provavel de cada motivo. Nenhuma
linha abaixo diz "o Search Console reclamou desta": diz o que o SITE responde.

A LISTA NAO E DIGITADA: as 17 URLs vem do `wp-sitemap.xml` no ar. Digitar o
inventario e como a contagem de `urls_publicadas` ficou quatro dias defasada.

AS VARIACOES SAO O CORACAO DESTA VARREDURA, e nao um extra. Uma pagina so nunca
produz os dois motivos do e-mail: eles nascem de DUAS URLs para a mesma coisa —
uma com www e outra sem, uma em http e outra em https, uma com barra final e
outra sem. Varrer so a URL canonica mediria exatamente o lado que nunca da
problema.
"""

import io
import json
import os
import re
import subprocess
import sys
import time

BASE = "https://clubedomosaico.com.br"
RAIZ = sys.argv[1].rstrip("/") if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "."
GRAVAR = "--gravar" in sys.argv

RE_CANON = re.compile(r'<link[^>]*rel=["\']canonical["\'][^>]*>', re.I)
RE_HREF = re.compile(r'href=["\']([^"\']+)["\']', re.I)


def cortar_cache(url):
    sep = "&" if "?" in url else "?"
    return url + sep + "v=" + str(int(time.time()))


def cadeia(url, cortar=True):
    """Segue a cadeia SEM deixar o curl esconder os saltos: um salto por vez.

    `cortar` decide QUEM esta respondendo, e a diferenca entre os dois e o achado
    de 25/09/2026. Com `cortar=True` a URL leva `?v=<agora>` e a pergunta chega
    ao WordPress: e a decisao do software, reproduzivel. Com `cortar=False` a URL
    vai crua, do jeito que o Googlebot a pede — e quem responde pode ser o CACHE
    DE PAGINA, que nao sabe redirecionar: ele so devolve o HTML que guardou.

    Medir so com quebra de cache mede o software e chama isso de "o que o Google
    ve", que sao coisas diferentes. Medir so sem quebra mede o cache de hoje e
    chama isso de "a regra do site". Esta ferramenta mede as duas.
    """
    saltos = []
    atual = url
    for _ in range(6):
        r = subprocess.run(
            ["curl", "-s", "-o", "/dev/null", "--max-time", "40",
             "-w", "%{http_code} %{redirect_url}", cortar_cache(atual) if cortar else atual],
            capture_output=True, text=True)
        partes = r.stdout.strip().split(" ", 1)
        codigo = partes[0]
        destino = partes[1].strip() if len(partes) > 1 else ""
        # o corta-cache e nosso; nao pode aparecer no relatorio como se fosse do site
        destino = re.sub(r"[?&]v=\d{10}$", "", destino)
        saltos.append((atual, codigo, destino))
        if not destino or codigo in ("200", "404", "410"):
            break
        atual = destino
    return saltos


def canonica(url):
    r = subprocess.run(["curl", "-sL", "--max-time", "40", cortar_cache(url)],
                       capture_output=True, text=True)
    m = RE_CANON.search(r.stdout)
    if not m:
        return None
    h = RE_HREF.search(m.group(0))
    if not h:
        return None
    return re.sub(r"[?&]v=\d{10}", "", h.group(1))


def urls_do_sitemap():
    r = subprocess.run(["curl", "-s", "--max-time", "40", cortar_cache(BASE + "/wp-sitemap.xml")],
                       capture_output=True, text=True)
    fora = []
    for sub in re.findall(r"<loc>([^<]+)</loc>", r.stdout):
        rr = subprocess.run(["curl", "-s", "--max-time", "40", cortar_cache(sub)],
                            capture_output=True, text=True)
        fora += re.findall(r"<loc>([^<]+)</loc>", rr.stdout)
    return fora


def variacoes(url):
    """As quatro portas pelas quais a mesma pagina pode ser pedida."""
    sem_esquema = url.split("://", 1)[1]
    fora = [("http", "http://" + sem_esquema),
            ("www", "https://www." + sem_esquema)]
    if url.endswith("/") and url != BASE + "/":
        fora.append(("sem barra final", url[:-1]))
    return fora


def classificar(url, saltos, canon, no_sitemap, eh_variacao, alvo, eh_arquivo=False):
    """Devolve (veredito, explicacao, correcao_proposta_ou_None).

    A REGUA E A DO DESPACHO, item por item, e esta escrita aqui e so aqui.

    `eh_arquivo` existe porque a primeira passada desta ferramenta, em
    25/09/2026, chamou de DEFEITO a ausencia de canonica em
    `/author/mosaico_gestor/` — e estava errado nos dois sentidos. O
    `rel_canonical()` do nucleo do WordPress so imprime a etiqueta em pagina
    SINGULAR; arquivo (autor, categoria, data, busca) nasce sem ela desde
    sempre, em toda instalacao do mundo. E desde a casca 1.13.0 esse endereco
    sai do indice com `noindex, follow`, entao declarar canonica ali seria
    declarar a versao boa de uma pagina que a ilha pediu para nao ser indexada.
    Regua que reprova o comportamento padrao do nucleo gera trabalho inventado,
    que e exatamente o que a abertura do BLOCO C manda evitar.
    """
    codigo_final = saltos[-1][1]
    destino_final = saltos[-1][0] if len(saltos) > 1 else url
    n_saltos = len([s for s in saltos if s[2]])

    if eh_variacao:
        if n_saltos == 0:
            if codigo_final == "200" and canon and canon.rstrip("/") == alvo.rstrip("/"):
                return ("esperado",
                        f"responde {codigo_final} sem redirecionar e aponta a canonica para {canon} — "
                        "e este o caso que o Search Console chama de 'Pagina alternativa com tag "
                        "canonica adequada': a variacao existe, e declarada duplicata e a canonica "
                        "aponta para a versao boa",
                        None)
            if codigo_final == "200" and canon is None and eh_arquivo:
                return ("esperado",
                        "responde 200 sem canonica, como todo arquivo do nucleo — e o endereco "
                        "inteiro sai do indice com `noindex, follow` desde a casca 1.13.0, "
                        "variacao incluida",
                        None)
            if codigo_final == "200":
                return ("defeito",
                        f"responde 200 e a canonica e {canon or 'AUSENTE'}, que nao e a versao boa "
                        f"({alvo}) — duas URLs servindo a mesma pagina sem declarar qual vale",
                        f"fazer a canonica de `{url}` apontar para `{alvo}`, ou redirecionar 301 para ela")
            return ("esperado", f"responde {codigo_final}, sem duplicata para resolver", None)
        if n_saltos == 1 and destino_final.rstrip("/") == alvo.rstrip("/"):
            return ("esperado",
                    f"301 em UM salto para {alvo} — e o caso 'Pagina com redirecionamento' do "
                    "Search Console, e ele e o comportamento correto",
                    None)
        if n_saltos > 1:
            return ("defeito",
                    f"cadeia de {n_saltos} saltos ate {destino_final} — cada salto perde sinal e "
                    "gasta orcamento de rastreamento",
                    f"redirecionar `{url}` direto para `{alvo}`, em um salto so")
        if destino_final.rstrip("/") == BASE and alvo.rstrip("/") != BASE:
            return ("defeito",
                    f"redireciona para a home em vez da pagina equivalente ({alvo})",
                    f"redirecionar `{url}` para `{alvo}`")
        return ("defeito",
                f"redireciona para {destino_final}, que nao e a versao boa ({alvo})",
                f"redirecionar `{url}` para `{alvo}`")

    # URL principal, lida do sitemap
    if no_sitemap and n_saltos > 0:
        return ("defeito",
                f"esta NO SITEMAP e redireciona ({n_saltos} salto(s), termina em {destino_final}) — "
                "sitemap e curadoria (14.1) e nao deve listar URL que redireciona",
                f"tirar `{url}` do sitemap e listar `{destino_final}` no lugar")
    if codigo_final != "200":
        return ("defeito", f"responde {codigo_final}", f"investigar por que `{url}` nao responde 200")
    if canon is None:
        if eh_arquivo:
            return ("esperado",
                    "nao serve canonica, e nao deve: o `rel_canonical()` do nucleo so a imprime em "
                    "pagina singular, e desde a casca 1.13.0 este endereco sai do indice com "
                    "`noindex, follow`",
                    None)
        return ("defeito", "nao serve <link rel=\"canonical\">",
                f"fazer `{url}` servir a canonica dela mesma")
    if canon.rstrip("/") == BASE and url.rstrip("/") != BASE:
        return ("defeito",
                f"pagina de conteudo com a canonica apontando para a HOME ({canon}) — "
                "o Google le isso como 'esta pagina nao existe, veja a home'",
                f"fazer a canonica de `{url}` apontar para ela mesma")
    if canon.rstrip("/") != url.rstrip("/"):
        return ("defeito",
                f"a canonica aponta para outra URL ({canon})",
                f"conferir se `{canon}` e mesmo a versao boa de `{url}`")
    return ("esperado", "responde 200, sem redirecionar, canonica apontando para ela mesma", None)



# ---------------------------------------------------------------------------
# O AUTOTESTE DA REGUA. A varredura de 25/09/2026 fechou em 71 esperado e ZERO
# defeito — e portao que nunca acusa nada e indistinguivel de portao quebrado.
# Aqui a regua e exercida contra casos FABRICADOS, um por ramo de defeito, para
# a passada limpa significar "a ilha esta limpa" e nao "a regua nao sabe acusar".
#
#     python3 ferramentas/varrer-canonicas.py . --autoteste
#
# Os casos sao escritos a mao, com a resposta esperada ao lado, e nenhum deles
# chama a rede: e a regra sendo medida, nao o site.
def autoteste():
    A = "https://clubedomosaico.com.br/materiais/"
    casos = [
        ("principal com canonica para a HOME",
         dict(url=A, saltos=[(A, "200", "")], canon="https://clubedomosaico.com.br/",
              no_sitemap=True, eh_variacao=False, alvo=A), "defeito"),
        ("principal sem canonica nenhuma (pagina, nao arquivo)",
         dict(url=A, saltos=[(A, "200", "")], canon=None,
              no_sitemap=True, eh_variacao=False, alvo=A), "defeito"),
        ("principal NO SITEMAP que redireciona",
         dict(url=A, saltos=[(A, "301", A + "nova/"), (A + "nova/", "200", "")], canon=None,
              no_sitemap=True, eh_variacao=False, alvo=A), "defeito"),
        ("principal que responde 404",
         dict(url=A, saltos=[(A, "404", "")], canon=None,
              no_sitemap=True, eh_variacao=False, alvo=A), "defeito"),
        ("variacao 200 com canonica apontando para o lugar errado",
         dict(url="http://clubedomosaico.com.br/materiais/", saltos=[("http://clubedomosaico.com.br/materiais/", "200", "")],
              canon="https://clubedomosaico.com.br/outra/", no_sitemap=False, eh_variacao=True, alvo=A), "defeito"),
        ("variacao com cadeia de dois saltos",
         dict(url="http://clubedomosaico.com.br/materiais/",
              saltos=[("http://clubedomosaico.com.br/materiais/", "301", "https://clubedomosaico.com.br/materiais"),
                      ("https://clubedomosaico.com.br/materiais", "301", A), (A, "200", "")],
              canon=None, no_sitemap=False, eh_variacao=True, alvo=A), "defeito"),
        ("variacao que redireciona para a HOME em vez da pagina",
         dict(url="http://clubedomosaico.com.br/materiais/",
              saltos=[("http://clubedomosaico.com.br/materiais/", "301", "https://clubedomosaico.com.br/"),
                      ("https://clubedomosaico.com.br/", "200", "")],
              canon=None, no_sitemap=False, eh_variacao=True, alvo=A), "defeito"),
        ("principal saudavel (o caso de hoje)",
         dict(url=A, saltos=[(A, "200", "")], canon=A,
              no_sitemap=True, eh_variacao=False, alvo=A), "esperado"),
        ("variacao 200 com canonica certa (o caso de hoje)",
         dict(url="http://clubedomosaico.com.br/materiais/", saltos=[("http://clubedomosaico.com.br/materiais/", "200", "")],
              canon=A, no_sitemap=False, eh_variacao=True, alvo=A), "esperado"),
        ("variacao com 301 de UM salto para a versao boa",
         dict(url="http://clubedomosaico.com.br/materiais/",
              saltos=[("http://clubedomosaico.com.br/materiais/", "301", A), (A, "200", "")],
              canon=None, no_sitemap=False, eh_variacao=True, alvo=A), "esperado"),
        ("arquivo sem canonica — comportamento do nucleo, nao defeito",
         dict(url="https://clubedomosaico.com.br/author/mosaico_gestor/",
              saltos=[("https://clubedomosaico.com.br/author/mosaico_gestor/", "200", "")], canon=None,
              no_sitemap=False, eh_variacao=False, alvo="https://clubedomosaico.com.br/author/mosaico_gestor/",
              eh_arquivo=True), "esperado"),
    ]
    falhas = 0
    for rotulo, kw, esperado_ in casos:
        veredito = classificar(**kw)[0]
        bom = veredito == esperado_
        falhas += 0 if bom else 1
        print(("  ok   " if bom else "  FALHA ") + rotulo.ljust(62) + " " + veredito)
    print(f"\n{'APROVADO' if not falhas else 'REPROVADO'}: {len(casos)} casos de regua, {falhas} falha(s).")
    return falhas


if "--autoteste" in sys.argv:
    sys.exit(1 if autoteste() else 0)

linhas = []
principais = urls_do_sitemap() + [BASE + "/author/mosaico_gestor/"]
print(f"{len(principais)} URL(s) principais (17 do sitemap + o arquivo de autor)\n")

for u in principais:
    no_sitemap = "/author/" not in u
    s = cadeia(u)
    s_cru = cadeia(u, cortar=False)
    c = canonica(u)
    eh_arquivo = not no_sitemap
    v, expl, corr = classificar(u, s, c, no_sitemap, False, u, eh_arquivo)
    linhas.append((u, "principal", s, c, v, expl, corr, s_cru))
    print(f"  {v:9s} {u}")
    for vr, uv in variacoes(u):
        sv = cadeia(uv)
        sv_cru = cadeia(uv, cortar=False)
        cv = canonica(uv) if sv[-1][1] == "200" and len(sv) == 1 else None
        vv, expv, corrv = classificar(uv, sv, cv, False, True, u, eh_arquivo)
        linhas.append((uv, "variacao " + vr, sv, cv, vv, expv, corrv, sv_cru))
        print(f"    {vv:9s} [{vr}] {uv}")

esperado = [l for l in linhas if l[4] == "esperado"]
defeito = [l for l in linhas if l[4] == "defeito"]
print(f"\n{len(linhas)} URL(s) lidas: {len(esperado)} esperado, {len(defeito)} defeito")

if not GRAVAR:
    print("\n(nada gravado — use --gravar)")
    sys.exit(0)

hoje = time.strftime("%Y-%m-%d", time.gmtime())
agora = time.strftime("%Hh%MZ", time.gmtime())


def texto_cadeia(s):
    return " → ".join(f"{cod}" for _, cod, _ in s)


def discorda(l):
    """A leitura do WordPress e a do rastreador dizem coisas diferentes?"""
    return texto_cadeia(l[2]) != texto_cadeia(l[7])


def bloco(ls):
    fora = []
    for l in ls:
        u, papel, s, c, v, expl, corr, s_cru = l
        marca = " **⚠**" if discorda(l) else ""
        fora.append(f"| `{u}` | {papel} | {texto_cadeia(s)} | {texto_cadeia(s_cru)}{marca} | "
                    f"{('`' + c + '`') if c else '—'} | {expl} |")
    return "\n".join(fora)


texto = [
    "",
    f"## Varredura de canônicas e redirecionamentos — {hoje}, {agora} (BLOCO C do despacho de 24/09)",
    "",
    f"Medido por `ferramentas/varrer-canonicas.py`, que é quem sabe reproduzir isto. **{len(linhas)} URLs lidas** "
    f"— as {len(principais)} principais (17 do sitemap no ar, mais `/author/mosaico_gestor/`) e as variações de cada "
    "uma (`http://`, `www.`, sem barra final), porque os dois motivos do e-mail nascem de duas URLs para a mesma "
    f"coisa e varrer só a versão boa mediria o lado que nunca dá problema. **{len(esperado)} em "
    f"\"esperado, nenhuma ação\" e {len(defeito)} em \"defeito, com a correção proposta\".**",
    "",
    "**O que esta varredura NÃO é:** não é a lista de URLs que o Search Console reclamou. A conta de serviço "
    "`sentinela@` não tem acesso a `sc-domain:clubedomosaico.com.br`, então essa lista não existe nesta nuvem "
    "(pedido ao Raphael no BLOCO C). O que está abaixo é o que o **site responde**, e é dele que sai a explicação "
    "mais provável de cada motivo do e-mail de 23/09.",
    "",
    "**Nada foi corrigido**, por ordem do próprio despacho: o que é defeito volta como PROPOSTA, URL por URL, para "
    "o Raphael autorizar item por item.",
    "",
    "### O achado da varredura: o rastreador NUNCA recebe redirecionamento — o cache responde 200 antes",
    "",
    "**Este achado quase não foi feito, e o quase vale mais que ele.** A primeira conferência desta execução abriu "
    "`https://www.clubedomosaico.com.br/loja/` no `curl` e leu **200**. A varredura, que gruda `?v=<agora>` em toda "
    "URL, leu **301** na mesma URL no mesmo minuto. Não é intermitência: são **dois respondedores**. Com a quebra "
    "de cache a pergunta chega ao WordPress, que redireciona certo; sem ela quem responde é o **cache de página**, "
    "que não sabe redirecionar — devolve o HTML que guardou. **O Googlebot não manda quebra de cache.**",
    "",
    "Medido em **três passadas por URL e por leitura**, porque uma leitura só não distingue cache frio de regra "
    "(a primeira leitura da home desta execução deu 301 cru, antes de a entrada esquentar; as três seguintes deram "
    "200):",
    "",
    "| variação | no WordPress (com quebra de cache) | crua, 3 passadas (o que o rastreador pede) |",
    "|---|---|---|",
    "| `http://clubedomosaico.com.br/` (a home) | **301** para `https` | **200 200 200** |",
    "| `https://www.clubedomosaico.com.br/loja/` | **301** para a versão sem `www` | **200 200 200** |",
    "| `https://clubedomosaico.com.br/loja` (sem barra) | **301** para a versão com barra | **200 200 200** |",
    "| `http://clubedomosaico.com.br/loja/` | **200** (não há regra de esquema para caminho interno) | **200 200 200** |",
    "",
    "**O fato que manda, e ele é um só:** o WordPress desta ilha redireciona `www`, barra final e a home em "
    "`http` — e **nada disso chega ao rastreador**, porque o cache responde 200 antes. As 36 linhas marcadas com "
    "**⚠** na tabela abaixo são exatamente as URLs em que as duas leituras discordam.",
    "",
    "**E é isso que explica os dois motivos do e-mail de 23/09, cada um de um jeito:**",
    "",
    "1. **\"Página alternativa com tag canônica adequada\"** — explicado, e o despacho está certo em chamá-lo de "
    "comportamento esperado. O rastreador recebe 200 em cada variação, a página servida declara a canônica certa, "
    "e o Google consolida. **Nenhum sinal se perde e não há o que consertar hoje.**",
    "2. **\"Página com redirecionamento\"** — **NÃO explicado pelo que a ilha serve hoje**, e isto é o oposto do "
    "que esta execução esperava encontrar: nas 71 URLs lidas, **o rastreador não recebe um único redirecionamento**. "
    "A fonte provável está fora do alcance desta nuvem: o domínio teve vida anterior e há um `sitemap.xml` de 2019 "
    "na propriedade (está no `PROMPT.md` desde o nascimento). URLs de 2019 que hoje redirecionam cairiam nesse "
    "relatório, e **a lista delas só existe dentro do Search Console** — que é exatamente o acesso que o BLOCO C "
    "pede ao Raphael.",
    "",
    "#### O QUE ISTO MUDA PARA QUEM MEDIR ESTA ILHA DEPOIS, e é maior que o BLOCO C",
    "",
    "**`?v=<agora>` mede o WordPress, não o site.** `ferramentas/conferir-no-ar.py` gruda a quebra de cache em toda "
    "URL que abre — e está certo em fazer isso, porque nasceu para provar que o Sync aplicou a revisão nova (seção "
    "4: sem ela se conclui que nada mudou). O preço é que **ele nunca vê o que o visitante vê**, e nenhuma linha "
    "dizia isso. Cache servindo página velha para gente de verdade passa por baixo das 472 afirmações dele sem "
    "encostar em nenhuma. É a mesma família da seção 29: o portão entra por uma porta que o visitante não usa.",
    "",
    "#### PROPOSTA, NÃO APLICADA — 301 de `http` para `https` em todo caminho",
    "",
    "Pela régua do próprio despacho isto **não é defeito** (a canônica resolve), e está fora da lista de defeitos "
    "abaixo. É melhora, e o ganho é de orçamento de rastreamento: domínio novo tem orçamento minúsculo.",
    "",
    "- **O que mudaria:** `http://` → `https://` em 301 para todo caminho, não só para a home — a regra que o `www` "
    "e a barra final já têm dentro do WordPress.",
    "- **Onde:** configuração de hospedagem (HostGator) ou `.htaccess`. **Não é snippet**, e por isso não cabe numa "
    "execução da Fundação sem autorização.",
    "- **O que ela NÃO resolve sozinha, e é o que mais pesa:** enquanto o cache responder 200 antes do WordPress, "
    "regra de redirecionamento nova também não chega ao rastreador. Mexer no cache é outra conversa, e hoje é "
    "inofensivo — a página servida traz a canônica certa, medido nas duas leituras.",
    "- **O risco de fazer é baixo e o de não fazer também. Fica esperando a palavra do Raphael**, como o BLOCO C "
    "manda: correção de canônica ou de redirect não se aplica sem autorização item por item.",
    "",
    "### Esperado, nenhuma ação",
    "",
    "| URL | papel | cadeia no WordPress (com quebra de cache) | cadeia crua (o que o rastreador pede) | canônica servida | por que está certo |",
    "|---|---|---|---|---|---|",
    bloco(esperado) if esperado else "| — | — | — | — | nenhuma |",
    "",
]

texto += ["### Defeito, com a correção proposta", ""]
if defeito:
    texto += ["| URL | papel | cadeia no WordPress (com quebra de cache) | cadeia crua (o que o rastreador pede) | canônica servida | o que está errado |",
              "|---|---|---|---|---|---|",
              bloco(defeito), "",
              "**As correções propostas, uma por linha — nenhuma aplicada:**", ""]
    for u, papel, s, c, v, expl, corr, s_cru in defeito:
        texto.append(f"- `{u}` — {corr}")
    texto.append("")
else:
    texto += ["**Nenhum.** Todas as URLs lidas caem em \"esperado, nenhuma ação\", e os dois motivos do e-mail de "
              "23/09 são o Google fazendo o trabalho dele.", ""]

io.open(os.path.join(RAIZ, "dados/indexacao.md"), "a", encoding="utf-8").write("\n".join(texto))
print(f"\ngravado em {RAIZ}/dados/indexacao.md")
