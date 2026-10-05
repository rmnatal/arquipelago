#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mede o CANAL DE ESPELHO: por onde esta nuvem consegue abrir documento de fabricante.

    python3 ferramentas/medir-espelho.py .              # so imprime
    python3 ferramentas/medir-espelho.py . --gravar     # escreve dados/canal-de-espelho.md (+ .json)
    python3 ferramentas/medir-espelho.py . --autoteste  # 18 casos fabricados, sem tocar na rede

POR QUE ESTE ARQUIVO EXISTE. Em 05/10/2026, as 13h2xZ, um bloco desta ilha descobriu que o
boletim tecnico da Quartzolit abre pelo CDN da Telha Norte e escreveu o achado em
`escada_de_fontes.canal_de_espelho` do esquema, com UM host medido e uma explicacao que
parecia bastar: "a Telha Norte e varejista do proprio grupo Saint-Gobain". Seis horas depois,
nesta execucao, a explicacao se mostrou a parte errada do achado: `leroymerlin`, `mkpcoral`,
`cec`, `balaroti`, `chatuba` e `tumelero` respondem do MESMO jeito no mesmo CDN, e nenhum
deles e do grupo Saint-Gobain. O que esta liberado e a FAMILIA DE HOSTS do CDN, nao um
varejista. Relacao de grupo nao explica nada — e, pior, uma explicacao errada estreita a porta
na cabeca de quem le: quem acreditasse nela nao tentaria o CDN de nenhuma outra loja.

E ESTE ARQUIVO MEDE A OUTRA METADE, que e a que decide o que se pode planejar. O canal e
ARQUIVO POR NOME CONHECIDO, e nao catalogo navegavel: os hosts que permitiriam DESCOBRIR o
nome de um arquivo — a loja (`www.<loja>.com.br`), a API de catalogo VTEX
(`<loja>.vtexcommercestable.com.br`) e o painel (`<loja>.myvtex.com`) — estao todos fechados.
Entao achar o boletim de um produto novo e problema de INDICE DE BUSCA, nunca de egresso, e
"o egresso nao abre PDF de fabricante" e "nao sei o nome do arquivo" sao dois bloqueios
diferentes que quatro blocos desta ilha escreveram com a mesma frase.

AS QUATRO TRAVAS, as mesmas de medir-egresso.py porque as causas sao as mesmas:

1. O INVENTARIO E DERIVADO, nao digitado — a parte que pode ser. Todo `fontes[].url` dos
   bancos que caia num host de espelho entra sozinho. Lista digitada envelhece calada.
   O que NAO da para derivar esta num bloco separado e declarado como digitado, com o motivo:
   o canal nao tem indice, entao documento achado por busca e a unica coisa que nao sai de
   dentro do repositorio.
2. TRES PASSADAS, nunca uma (20.2: uma falha e o tunel, tres seguidas e a rede). Host que
   falha em uma e responde em duas sai como INTERMITENTE, que e veredito e nao erro.
3. CONTROLE OBRIGATORIO. `clubedomosaico.com.br` tem de responder nas tres passadas. Se cair,
   a medicao inteira e VOID e nada e gravado: sem controle, queda de tunel escreveria "tudo
   fechado" no repositorio com cara de fato.
4. O INVENTARIO SE CONFERE LENDO O DOCUMENTO, nunca o nome do arquivo. Cada PDF alcancado e
   aberto e o titulo da pagina 1 e extraido, porque o nome do arquivo no espelho e codigo do
   varejista (`908487.pdf`) e nao diz que produto e — foi exatamente dai que saiu o falso
   positivo do batismo que esta ilha pagou duas vezes em 05/10/2026.
"""

import glob
import json
import os
import re
import subprocess
import sys

RAIZ = sys.argv[1].rstrip("/") if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "."
GRAVAR = "--gravar" in sys.argv
AUTOTESTE = "--autoteste" in sys.argv

CONTROLE = "https://clubedomosaico.com.br/"
PASSADAS = 3

# As familias de host que servem documento de fabricante sem ser o fabricante. O sufixo e o
# que esta medido como liberado; os membros abaixo existem para PROVAR que e a familia e nao
# um membro — era a conclusao errada de 05/10 as 13h2xZ.
FAMILIAS_DE_ESPELHO = ["vteximg.com.br", "vtexassets.com"]

SONDAS = [
    # (grupo, host, caminho, o_que_esta_sonda_prova)
    ("familia_de_espelho", "telhanorte.vteximg.com.br", "/",
     "o membro que o achado de 13h2xZ mediu"),
    ("familia_de_espelho", "leroymerlin.vteximg.com.br", "/",
     "varejista FORA do grupo Saint-Gobain: se responde, a explicacao de grupo cai"),
    ("familia_de_espelho", "mkpcoral.vteximg.com.br", "/",
     "outro ramo do varejo, achado por busca servindo boletim da Coral"),
    ("familia_de_espelho", "cec.vteximg.com.br", "/", "terceiro membro"),
    ("familia_de_espelho", "balaroti.vteximg.com.br", "/", "quarto membro"),
    ("familia_de_espelho", "chatuba.vteximg.com.br", "/", "quinto membro"),
    ("familia_de_espelho", "tumelero.vteximg.com.br", "/", "sexto membro"),
    ("familia_de_espelho", "telhanorte.vtexassets.com", "/",
     "a familia NOVA do mesmo fornecedor de CDN"),
    ("familia_de_espelho", "leroymerlin.vtexassets.com", "/", "segundo membro da familia nova"),

    ("descoberta", "www.telhanorte.com.br", "/",
     "a loja: se abrisse, daria para procurar o produto e achar o link do boletim"),
    ("descoberta", "telhanorte.vtexcommercestable.com.br", "/",
     "a API de catalogo da VTEX: e o jeito limpo de listar produto e anexo"),
    ("descoberta", "telhanorte.myvtex.com", "/", "o painel, o outro endereco da mesma API"),

    ("escapatoria", "web.archive.org", "/",
     "espelho de tudo: resolveria o fabricante fechado se estivesse aberto"),
    ("escapatoria", "r.jina.ai", "/", "proxy de leitura"),
    ("escapatoria", "docs.google.com", "/", "visualizador de PDF de terceiro"),

    ("fabricante", "www.quartzolit.weber", "/",
     "o host onde moram TODAS as URLs de boletim que os bancos citam — o nivel 1 da escada"),
    ("fabricante", "quartzolit.weber", "/",
     "o apex, que entrou na lista de rede em 30/09 e so redireciona para o www"),
]

# O que a busca achou e o repositorio nao tem como derivar. DIGITADO, e declarado como tal:
# o canal nao tem indice proprio, entao nome de arquivo novo so chega por fora.
ACHADOS_POR_BUSCA = [
    "https://telhanorte.vteximg.com.br/arquivos/908487.pdf",
    "https://telhanorte.vteximg.com.br/arquivos/27073.pdf",
    "https://telhanorte.vteximg.com.br/arquivos/1463217.pdf",
    "https://telhanorte.vteximg.com.br/arquivos/1458361.pdf",
    "https://telhanorte.vteximg.com.br/arquivos/1338838.pdf",
    "https://telhanorte.vteximg.com.br/arquivos/1156527.pdf",
    "https://telhanorte.vteximg.com.br/arquivos/1430424.pdf",
    "https://telhanorte.vteximg.com.br/arquivos/1463705.pdf",
    "https://telhanorte.vteximg.com.br/arquivos/59668.pdf",
    "https://telhanorte.vteximg.com.br/arquivos/298182.pdf",
    "https://telhanorte.vteximg.com.br/arquivos/1399250.pdf",
    "https://telhanorte.vteximg.com.br/arquivos/101494.pdf",
    "https://telhanorte.vteximg.com.br/arquivos/90387.pdf",
]


def e_de_espelho(url):
    """True quando a URL mora numa familia de espelho. Compara por SUFIXO DE ROTULO, nunca
    por `in`: `vteximg.com.br.exemplo.com` nao e a familia, e um `in` o aceitaria."""
    m = re.match(r"https?://([^/:]+)", url or "")
    if not m:
        return False
    host = m.group(1).lower().rstrip(".")
    for suf in FAMILIAS_DE_ESPELHO:
        if host == suf or host.endswith("." + suf):
            return True
    return False


def urls_de_espelho_dos_bancos(raiz):
    """A metade DERIVADA do inventario: toda url de fonte dos bancos que caia no espelho."""
    achadas = {}

    def andar(obj, arq):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == "url" and isinstance(v, str) and e_de_espelho(v):
                    achadas.setdefault(v, set()).add(os.path.basename(arq))
                else:
                    andar(v, arq)
        elif isinstance(obj, list):
            for v in obj:
                andar(v, arq)

    for arq in sorted(glob.glob(os.path.join(raiz, "dados", "*.json"))):
        try:
            andar(json.load(open(arq, encoding="utf-8")), arq)
        except (ValueError, OSError):
            continue
    return {u: sorted(v) for u, v in achadas.items()}


def uma_passada(url):
    """Devolve (codigo, content_type, bytes). Codigo '000' e falha de alcance."""
    try:
        saida = subprocess.run(
            ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code} %{content_type} %{size_download}",
             "--max-time", "20", url],
            capture_output=True, text=True, timeout=40).stdout.strip()
    except (subprocess.TimeoutExpired, OSError):
        return ("000", "", 0)
    partes = saida.split()
    if not partes:
        return ("000", "", 0)
    cod = partes[0]
    ct = partes[1] if len(partes) > 2 else ""
    try:
        tam = int(partes[-1])
    except ValueError:
        tam = 0
    return (cod, ct, tam)


def veredito_de_host(codigos):
    """O veredito sai da MAIORIA das tres passadas, nunca de uma leitura.

    E o ponto que mais custou a esta ilha: `400` do CDN NAO e fechado. O CDN reclamando de
    caminho e o host RESPONDENDO — prova de que o egresso deixou passar. Fechado e so nao
    chegar a conversar, que o curl escreve como `000`."""
    vivos = sum(1 for c in codigos if c != "000")
    if vivos == len(codigos):
        return "aberto"
    if vivos == 0:
        return "fechado"
    return "intermitente"


def veredito_de_entrega(codigos):
    """O SEGUNDO veredito, e ele existe porque o primeiro sozinho mente.

    `veredito_de_host` responde "o egresso deixou conversar?". Esta responde "chegou alguma
    coisa?". A licao e de 30/09/2026 desta mesma ilha, com estas palavras: um portao que
    olhasse so o CONNECT diria "liberado" e mandaria coletar o que nao ha como ler; um que
    olhasse so o codigo final diria "bloqueado" e esconderia que falta uma linha. Os dois
    saem juntos ou nenhum dos dois serve. Caso vivo nesta execucao: `www.quartzolit.weber`
    responde 403 nas tres passadas — conversa, e recusa."""
    maioria = max(set(codigos), key=codigos.count)
    if maioria == "000":
        return "fechado"
    if maioria.startswith("2"):
        return "entrega"
    if maioria.startswith("3"):
        return "redireciona"
    return "conversa_sem_entrega"


def titulo_do_pdf(url):
    """Abre o PDF e devolve a primeira linha com texto. O nome do arquivo no espelho e codigo
    do varejista, entao a identidade do documento se le DENTRO dele."""
    destino = "/tmp/espelho-%s" % re.sub(r"[^A-Za-z0-9._-]", "_", url.split("/")[-1])
    try:
        subprocess.run(["curl", "-sL", "-o", destino, "--max-time", "40", url],
                       capture_output=True, timeout=60)
        txt = subprocess.run(["pdftotext", "-layout", "-f", "1", "-l", "1", destino, "-"],
                             capture_output=True, text=True, timeout=60).stdout
    except (subprocess.TimeoutExpired, OSError):
        return None
    finally:
        if os.path.exists(destino):
            os.remove(destino)
    for linha in (txt or "").splitlines():
        linha = " ".join(linha.split())
        if len(linha) > 8:
            return linha
    return None


def autoteste():
    casos_veredito = [
        (["200", "200", "200"], "aberto", "host que responde sempre"),
        (["400", "400", "400"], "aberto", "CDN reclamando de caminho E host respondendo — a trava que mais importa"),
        (["403", "403", "403"], "aberto", "403 e resposta do servidor, nao bloqueio de egresso"),
        (["000", "000", "000"], "fechado", "nunca conversou"),
        (["000", "200", "200"], "intermitente", "uma falha e o tunel (20.2)"),
        (["200", "000", "000"], "intermitente", "duas falhas ainda nao sao as tres que a 20.2 pede"),
        (["301", "301", "301"], "aberto", "apex que so redireciona ainda CONVERSOU"),
    ]
    casos_familia = [
        ("https://telhanorte.vteximg.com.br/arquivos/1.pdf", True, "membro medido"),
        ("https://leroymerlin.vtexassets.com/x.pdf", True, "familia nova"),
        ("https://vteximg.com.br/x.pdf", True, "o proprio sufixo, sem subdominio"),
        ("https://www.quartzolit.weber/files/br/a.pdf", False, "fabricante nao e espelho"),
        ("https://vteximg.com.br.exemplo.com/x.pdf", False, "SUFIXO FALSO: um `in` aceitaria isto"),
        ("https://naovteximg.com.br/x.pdf", False, "rotulo colado: so casa em fronteira de ponto"),
        ("https://TELHANORTE.VTEXIMG.COM.BR/x.pdf", True, "caixa alta"),
        ("https://telhanorte.vteximg.com.br./x.pdf", True, "ponto final de FQDN"),
        ("", False, "vazio"),
        ("nao e url", False, "lixo"),
        ("https://s3.amazonaws.com/x.pdf", False, "aberto nao e o mesmo que ser espelho desta familia"),
    ]
    casos_entrega = [
        (["200", "200", "200"], "entrega", "chega corpo"),
        (["400", "400", "400"], "conversa_sem_entrega", "o CDN conversa e nao entrega nada neste caminho"),
        (["403", "403", "403"], "conversa_sem_entrega", "www.quartzolit.weber nesta execucao: conversa, e recusa"),
        (["301", "301", "301"], "redireciona", "apex que manda para outro host"),
        (["000", "000", "000"], "fechado", "nunca conversou"),
        (["000", "200", "200"], "entrega", "a maioria manda, e ela entrega"),
    ]
    falhas = 0
    print("Autoteste de medir-espelho.py")
    for i, (cods, esperado, porque) in enumerate(casos_veredito, 1):
        obtido = veredito_de_host(cods)
        ok = obtido == esperado
        falhas += 0 if ok else 1
        print("  %-5s %02d  %-28s -> %-13s (esperado %-13s) %s"
              % ("ok" if ok else "FALHA", i, ",".join(cods), obtido, esperado, porque))
    for j, (url, esperado, porque) in enumerate(casos_familia, len(casos_veredito) + 1):
        obtido = e_de_espelho(url)
        ok = obtido == esperado
        falhas += 0 if ok else 1
        print("  %-5s %02d  %-44s -> %-5s (esperado %-5s) %s"
              % ("ok" if ok else "FALHA", j, (url or "(vazio)")[:44], obtido, esperado, porque))
    base = len(casos_veredito) + len(casos_familia)
    for k, (cods, esperado, porque) in enumerate(casos_entrega, base + 1):
        obtido = veredito_de_entrega(cods)
        ok = obtido == esperado
        falhas += 0 if ok else 1
        print("  %-5s %02d  %-28s -> %-21s (esperado %-21s) %s"
              % ("ok" if ok else "FALHA", k, ",".join(cods), obtido, esperado, porque))
    total = base + len(casos_entrega)
    print("  %d de %d" % (total - falhas, total))
    return 0 if falhas == 0 else 1


def medir():
    cod_ctrl = [uma_passada(CONTROLE)[0] for _ in range(PASSADAS)]
    if any(c == "000" for c in cod_ctrl):
        return {"veredito_da_medicao": "VOID", "controle": cod_ctrl,
                "por_que": "O controle clubedomosaico.com.br falhou em alguma passada. Sem controle verde, "
                           "esta medicao escreveria queda de tunel no repositorio com cara de fato (trava 3)."}

    hosts = []
    for grupo, host, caminho, porque in SONDAS:
        leituras = [uma_passada("https://%s%s" % (host, caminho)) for _ in range(PASSADAS)]
        codigos = [l[0] for l in leituras]
        hosts.append({"grupo": grupo, "host": host, "codigos": codigos,
                      "veredito": veredito_de_host(codigos),
                      "entrega": veredito_de_entrega(codigos),
                      "o_que_prova": porque})

    derivadas = urls_de_espelho_dos_bancos(RAIZ)
    inventario = []
    for url in sorted(set(list(derivadas.keys()) + ACHADOS_POR_BUSCA)):
        cod, ct, tam = uma_passada(url)
        item = {"url": url, "codigo": cod, "content_type": ct, "bytes": tam,
                "citado_por": derivadas.get(url, []),
                "procedencia_da_entrada": "derivada dos bancos" if url in derivadas else "achada por busca (digitada)"}
        if cod == "200" and "pdf" in (ct or ""):
            item["identidade_lida_no_documento"] = titulo_do_pdf(url)
        inventario.append(item)

    return {"veredito_da_medicao": "valida", "controle": cod_ctrl,
            "hosts": hosts, "inventario": inventario}


def resumo(r):
    por_grupo = {}
    for h in r.get("hosts", []):
        por_grupo.setdefault(h["grupo"], []).append(h)
    linhas = []
    for g in ("familia_de_espelho", "descoberta", "escapatoria", "fabricante"):
        hs = por_grupo.get(g, [])
        abertos = [h["host"] for h in hs if h["veredito"] == "aberto"]
        entregam = [h["host"] for h in hs if h["entrega"] in ("entrega", "redireciona")]
        linhas.append((g, len(hs), len(abertos), len(entregam)))
    pdfs = [i for i in r.get("inventario", []) if i.get("codigo") == "200" and "pdf" in (i.get("content_type") or "")]
    return linhas, pdfs


def montar_md(r, quando):
    L = []
    A = L.append
    A("# O canal de espelho — por onde esta nuvem abre documento de fabricante")
    A("")
    A("**GERADO por `ferramentas/medir-espelho.py`. Nao edite a mao.** Medido em %s." % quando)
    A("")
    if r["veredito_da_medicao"] == "VOID":
        A("## MEDICAO VOID")
        A("")
        A(r["por_que"])
        A("")
        A("Controle: `%s`." % ", ".join(r["controle"]))
        return "\n".join(L) + "\n"
    linhas, pdfs = resumo(r)
    A("## O numero que manda")
    A("")
    A("| grupo | hosts sondados | o egresso deixou conversar | chegou alguma coisa |")
    A("|---|---|---|---|")
    for g, n, a, e in linhas:
        A("| `%s` | %d | **%d** | **%d** |" % (g, n, a, e))
    A("")
    A("**Documentos de fabricante alcancados e LIDOS: %d.**" % len(pdfs))
    A("")
    A("## Host por host")
    A("")
    A("| grupo | host | tres passadas | conversou | entrega | o que esta sonda prova |")
    A("|---|---|---|---|---|---|")
    for h in r["hosts"]:
        A("| `%s` | `%s` | %s | **`%s`** | **`%s`** | %s |"
          % (h["grupo"], h["host"], " ".join(h["codigos"]), h["veredito"], h["entrega"],
             h["o_que_prova"]))
    A("")
    A("## O inventario, e cada linha se confere lendo o documento")
    A("")
    A("O nome do arquivo no espelho e codigo do varejista e **nao diz que produto e** — por isso a")
    A("coluna que vale e a ultima, lida na pagina 1 do PDF.")
    A("")
    A("| arquivo | codigo | tipo | bytes | entrada | identidade lida DENTRO do documento |")
    A("|---|---|---|---|---|---|")
    for i in r["inventario"]:
        A("| `%s` | %s | %s | %s | %s | %s |"
          % (i["url"].split("/")[-1], i["codigo"], i.get("content_type") or "-", i.get("bytes") or 0,
             "derivada" if i["procedencia_da_entrada"].startswith("derivada") else "busca",
             i.get("identidade_lida_no_documento") or "—"))
    A("")
    A("## O que esta medicao NAO autoriza")
    A("")
    A("- **Espelho nao e nivel 1.** Do espelho sai o documento, nao a garantia de que a revisao e a")
    A("  vigente. O boletim do `cimentcola externo` aqui e de **maio de 2016** e a pendencia que ele")
    A("  fecha aponta para o arquivo **2024-09**.")
    A("- **Espelho nao batiza** (26.2). O nome do arquivo e do varejista, e a trava do batismo leu")
    A("  `1200003.pdf` e `908487.pdf` como se fossem o fabricante escrevendo o nome do produto — duas")
    A("  vezes em 05/10/2026, nos dois casos acusando um campo certo.")
    A("- **Conversar nao e entregar, e o grupo `fabricante` e o exemplo vivo.** `www.quartzolit.weber`")
    A("  responde **403 nas tres passadas** — o egresso deixou conversar e o SERVIDOR recusa. O")
    A("  repositorio registrava este host como `connect_rejected` desde 30/09/2026; isso deixou de")
    A("  ser verdade, e a consequencia pratica e nenhuma: 403 nao entrega boletim. O que mudou e de")
    A("  quem e a porta — era politica de egresso, agora e o servidor do fabricante.")
    A("- **Canal aberto nao e documento achado.** Os hosts de `descoberta` estao fechados, entao nome")
    A("  de arquivo novo so chega por indice de busca. `rejunte acrilico` e `rejunte epoxi` da")
    A("  Quartzolit **nao estao** neste inventario, e nenhuma consulta desta execucao os achou em host")
    A("  algum da familia: isso e falta de INDICE, nao de egresso, e sao bloqueios diferentes.")
    return "\n".join(L) + "\n"


def main():
    if AUTOTESTE:
        return autoteste()
    r = medir()
    if r["veredito_da_medicao"] == "VOID":
        print("MEDICAO VOID — controle %s" % ", ".join(r["controle"]))
        print(r["por_que"])
        return 1
    linhas, pdfs = resumo(r)
    print("Canal de espelho — Clube do Mosaico")
    for g, n, a, e in linhas:
        print("  %-20s %d sondado(s), %d conversou(ram), %d entrega(m)" % (g, n, a, e))
    print("  documentos de fabricante alcancados e lidos .. %d" % len(pdfs))
    for h in r["hosts"]:
        print("  %-13s %-38s %s  %-12s %s"
              % (h["grupo"], h["host"], " ".join(h["codigos"]), h["veredito"], h["entrega"]))
    if GRAVAR:
        import datetime
        quando = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%MZ")
        r["gerado_em"] = quando
        r["gerado_por"] = "ferramentas/medir-espelho.py"
        with open(os.path.join(RAIZ, "dados", "canal-de-espelho.json"), "w", encoding="utf-8") as fh:
            json.dump(r, fh, ensure_ascii=False, indent=2)
        with open(os.path.join(RAIZ, "dados", "canal-de-espelho.md"), "w", encoding="utf-8") as fh:
            fh.write(montar_md(r, quando))
        print("Escrito: dados/canal-de-espelho.json e dados/canal-de-espelho.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
