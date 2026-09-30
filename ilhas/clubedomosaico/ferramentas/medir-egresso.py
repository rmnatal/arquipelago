#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mede, host por host, o que esta nuvem ALCANCA das fontes que os bancos desta ilha citam.

    python3 ferramentas/medir-egresso.py .              # so imprime
    python3 ferramentas/medir-egresso.py . --gravar     # escreve dados/egresso-de-fontes.md (+ .json)
    python3 ferramentas/medir-egresso.py . --autoteste  # 12 casos fabricados, sem tocar na rede

POR QUE ESTE ARQUIVO EXISTE, e a causa esta medida e tem data. Entre 26/09 e 29/09/2026
QUATRO blocos seguidos desta ilha pararam na mesma porta e os quatro escreveram a mesma
frase — "esbarra no egresso", "quartzolit.weber em 403 ao CONNECT". Em 30/09/2026 as 10h22Z
a frase ficou FALSA para quatro dos cinco dominios e ninguem teria descoberto, porque
"bloqueado" era herdado de documento e nao remedido. A 20.2 manda retestar bloqueio herdado
antes de respeita-lo, e a licao da Quartzolit de 29/09 estendeu isso a bloqueio herdado de
DOCUMENTO tanto quanto do ESTADO.md. Isto e essa regra virando comando.

O ACHADO QUE DESENHOU A FERRAMENTA, e ele e o motivo de ela nao medir uma coisa e sim DUAS.
Em 30/09 os apex `quartzolit.weber`, `tekbond.com.br`, `loctite.com.br` e `cascola.com.br`
passaram a estabelecer o CONNECT — o tunel devolve `HTTP/1.1 200 Connection Established` e o
servidor de verdade responde 301, com cabecalho de Apache e de CloudFront. E os quatro
redirecionam TUDO para o host `www.`, que o egresso recusa. Ou seja: o dominio esta liberado
e a fonte continua inalcancavel, e as 36 URLs de fonte que os bancos citam nesses quatro
dominios estao TODAS em `www.`. Um portao que medisse so o CONNECT diria "liberado" e mandaria
a proxima execucao coletar o que nao ha como ler; um que medisse so o codigo final diria
"bloqueado" e esconderia que falta UMA LINHA, nao uma decisao. Por isso cada host sai daqui
com dois vereditos: se o CONNECT passa, e se alguma coisa CHEGA.

AS QUATRO TRAVAS, todas nascidas de defeito que esta ilha ja pagou:

1. A LISTA NAO E DIGITADA. Os hosts saem de `dados/*.json`, de todo campo cujo valor comeca
   em http. Lista escrita a mao envelhece calada — foi assim que `urls_publicadas` ficou
   quatro dias defasada e que o `d2` do cone ficou fora da regua de robo.
2. TRES PASSADAS, nunca uma (20.2: uma falha e o tunel, tres seguidas e a rede). Host que
   falha em uma e responde em duas sai como INTERMITENTE, que e um veredito e nao um erro —
   e o 000 lido como bloqueio, em 11/09, prendeu esta ilha dois dias.
3. CONTROLE OBRIGATORIO. `clubedomosaico.com.br` tem de responder nas tres passadas. Se ele
   cair, a medicao inteira e VOID e nada e gravado: sem controle, queda de tunel escreveria
   "tudo bloqueado" no repositorio com cara de fato.
4. O VEREDITO DE ENTREGA E CALCULADO, nunca escrito. `alcancavel` exige CONNECT E corpo ou
   codigo final em host alcancavel. Apex que so redireciona para host recusado sai como
   `liberado_mas_sem_entrega`, com o host que falta nomeado.
"""

import glob
import json
import os
import re
import subprocess
import sys
import time

RAIZ = sys.argv[1].rstrip("/") if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "."
GRAVAR = "--gravar" in sys.argv
AUTOTESTE = "--autoteste" in sys.argv

RE_CAMPO_DE_DOMINIO = re.compile(r"dominio", re.I)
# Dominio nu em prosa: pelo menos dois rotulos e um TLD de letras. Nao casa numero de versao
# (`1.13.0`) nem nome de arquivo (`validar-banco.py`), porque os dois quebrariam a medicao
# pedindo rede para coisa que nao e host.
RE_DOMINIO_NU = re.compile(r"\b(?!www\.)((?:[a-z0-9][a-z0-9-]*\.)+[a-z]{2,})\b", re.I)
# E a trava que o proprio extrator pediu na primeira tentativa: `validar-banco.py` casa com a
# forma de dominio (dois rotulos, TLD de duas letras) e nao e host. Pedir rede para um nome de
# arquivo e a mesma familia do numero de tela digitado — parece medido e nao e.
NAO_E_TLD = {
    "py", "php", "js", "mjs", "json", "md", "xml", "html", "htm", "png", "jpg", "jpeg",
    "gif", "svg", "webp", "pdf", "txt", "csv", "sh", "css", "yml", "yaml", "zip", "ini",
}


def parece_host(d):
    return d.rsplit(".", 1)[-1].lower() not in NAO_E_TLD

SAIDA_DESTA_FERRAMENTA = {"egresso-de-fontes.json"}
CONTROLE = "clubedomosaico.com.br"
PASSADAS = 3

# Hosts que nao sao fonte de dado tecnico e nao se pede na lista de rede por isso:
# marketplace (o link de afiliado nasce por API, nao por leitura de pagina) e a propria ilha.
NAO_SE_PEDE = {
    CONTROLE: "e a propria ilha, ja liberada",
    "shopee.com.br": "marketplace — o link nasce pela Open API (25.6), nao por leitura de pagina",
    "s.shopee.com.br": "encurtador de link de afiliado, nao e fonte de dado",
    "cf.shopee.com.br": "CDN de imagem de anuncio, nao e fonte de dado",
    "www.mercadolivre.com.br": "marketplace — etiqueta de afiliado, nao e fonte de dado",
    "meli.la": "encurtador do Mercado Livre, nao e fonte de dado",
}


# Sufixos publicos de mais de um rotulo que aparecem nas fontes desta ilha. A lista e curta
# de proposito: dominio registravel adivinhado por "penultimo rotulo" erra em `.com.br` e
# em `.leg.br`, e errar aqui produz um PEDIDO errado — que e o defeito que esta ferramenta
# nasceu para nao repetir. Sufixo desconhecido cai no ultimo rotulo, que e o certo para
# TLD de marca como `.weber`.
SUFIXOS = (
    "com.br", "edu.br", "leg.br", "gov.br", "org.br", "net.br", "art.br", "ind.br",
    "gob.es", "co.uk", "ac.uk", "com.pt", "org.pt",
)


def dominio_registravel(host):
    """`www.quartzolit.weber` -> `quartzolit.weber`; `www2.camara.leg.br` -> `camara.leg.br`."""
    host = host.lower().strip(".")
    for suf in sorted(SUFIXOS, key=len, reverse=True):
        if host == suf:
            return host
        if host.endswith("." + suf):
            resto = host[: -(len(suf) + 1)].split(".")
            return resto[-1] + "." + suf
    partes = host.split(".")
    return ".".join(partes[-2:]) if len(partes) >= 2 else host


def irmaos(host):
    """O apex e o `www.` do mesmo dominio registravel.

    ESTE E O CORACAO DA FERRAMENTA, e ela nasceu sem ele. A primeira versao, de 30/09/2026
    as 10h3xZ, mediu SO os hosts que os bancos citam — e os bancos citam `www.quartzolit.weber`,
    nunca o apex. Resultado: ela imprimiu `bloqueado` para os quatro fabricantes e NAO viu o
    unico fato novo do dia, que e o apex responder. Portao que mede so o que o banco cita ve
    so o lado que o banco ja conhece.
    """
    reg = dominio_registravel(host)
    return [h for h in (reg, "www." + reg) if h != host]


def hosts_dos_bancos(raiz):
    """Todo host citado em campo de URL de `dados/*.json`, com quem o cita."""
    achados = {}

    def andar(obj, arq, caminho):
        if isinstance(obj, dict):
            for k, v in obj.items():
                andar(v, arq, caminho + [str(k)])
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                andar(v, arq, caminho + [str(i)])
        elif isinstance(obj, str) and obj.startswith(("http://", "https://")):
            m = re.match(r"https?://([^/]+)", obj)
            if not m:
                return
            h = m.group(1).lower()
            achados.setdefault(h, {"urls": set(), "citado_por": set()})
            achados[h]["urls"].add(obj)
            achados[h]["citado_por"].add(os.path.basename(arq))
        elif isinstance(obj, str) and caminho and RE_CAMPO_DE_DOMINIO.search(caminho[-1]):
            # O SEGUNDO EXTRATOR, e ele existe porque a fonte que MAIS trava esta ilha nao
            # aparece como URL em lugar nenhum. `regras_da_categoria_base.o_que_falta_para_
            # coletar_o_primeiro_SKU.dominios_em_000` nomeia dez fabricantes de painel de MDF
            # em PROSA — nenhum SKU foi coletado, entao nenhum `url` os cita, entao o primeiro
            # extrator nao os ve. E sao exatamente os que a 20.3 manda conferir: quem escreve
            # a regra que exige a fonte confere se a fonte esta liberada. Campo cujo NOME fala
            # de dominio e lido como lista de dominio, e nao como texto.
            for d in RE_DOMINIO_NU.findall(obj):
                if not parece_host(d):
                    continue
                h = d.lower().strip(".")
                achados.setdefault(h, {"urls": set(), "citado_por": set()})
                achados[h]["citado_por"].add(os.path.basename(arq) + " (campo `" + caminho[-1] + "`)")

    for arq in sorted(glob.glob(os.path.join(raiz, "dados", "*.json"))):
        # A PROPRIA SAIDA NAO E FONTE. Na primeira passada de 30/09 as 10h31Z ela se citou
        # ("citado em: egresso-de-fontes.json") e isso e circular: o portao passaria a se
        # sustentar no que ele mesmo escreveu ontem, que e a forma de "resumo velho lido como
        # fato" da secao 4 aplicada a um arquivo gerado.
        if os.path.basename(arq) in SAIDA_DESTA_FERRAMENTA:
            continue
        try:
            andar(json.load(open(arq, encoding="utf-8")), arq, [])
        except (json.JSONDecodeError, OSError) as e:
            sys.exit("nao consegui ler %s: %s" % (arq, e))

    # A FAIXA QUE NENHUM BANCO ALCANCA: dominio exigido em prosa pelo repositorio e que nenhum
    # registro cita como URL, porque nenhum SKU dele foi coletado. `loctite.com.br` ficou fora
    # da medicao das 10h31Z de 30/09 exatamente assim — a especificacao da F2 o exige e o banco
    # de colas nao o cita. O arquivo diz, linha por linha, QUEM o exige; sem `exigido_por` a
    # linha e recusada, para isto nao virar lista de desejo.
    pedidas = os.path.join(raiz, "dados", "fontes-pedidas.json")
    if os.path.exists(pedidas):
        try:
            decl = json.load(open(pedidas, encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            sys.exit("nao consegui ler %s: %s" % (pedidas, e))
        for linha in decl.get("dominios", []):
            d = (linha.get("dominio") or "").strip().lower()
            if not d:
                continue
            if not linha.get("exigido_por"):
                sys.exit("`%s` esta em fontes-pedidas.json sem `exigido_por` — recusado, "
                         "porque dominio sem quem o exija e lista de desejo, nao medicao." % d)
            achados.setdefault(d, {"urls": set(), "citado_por": set()})
            achados[d]["citado_por"].add("fontes-pedidas.json (exigido em prosa)")

    return achados


def uma_passada(url):
    """Um salto so, sem -L: precisamos ver O SALTO, nao o destino.

    Devolve (codigo, destino, bytes). codigo 0 quer dizer que o CONNECT nao passou —
    e a unica leitura que distingue recusa de egresso de erro do servidor.
    """
    try:
        saida = subprocess.run(
            ["curl", "-s", "-o", "/dev/null", "--connect-timeout", "8", "--max-time", "15",
             "-w", "%{http_code}\t%{redirect_url}\t%{size_download}", url],
            capture_output=True, text=True, timeout=25,
        ).stdout.strip()
        codigo, destino, tam = (saida.split("\t") + ["", "", "0"])[:3]
        return int(codigo or 0), destino, int(tam or 0)
    except (subprocess.TimeoutExpired, ValueError):
        return 0, "", 0


def medir_host(host, url_de_amostra):
    """Tres passadas no host. O veredito de CONNECT sai da maioria, nunca de uma leitura."""
    leituras = [uma_passada(url_de_amostra) for _ in range(PASSADAS)]
    codigos = [c for c, _, _ in leituras]
    passou = sum(1 for c in codigos if c != 0)
    if passou == 0:
        connect = "recusado"
    elif passou == PASSADAS:
        connect = "estabelecido"
    else:
        connect = "intermitente"
    destino = next((d for c, d, _ in leituras if c != 0 and d), "")
    corpo = max((t for c, _, t in leituras), default=0)
    return {
        "connect": connect,
        "codigos": codigos,
        "destino_do_salto": destino,
        "host_do_destino": (re.match(r"https?://([^/]+)", destino).group(1).lower()
                            if destino and re.match(r"https?://([^/]+)", destino) else None),
        "bytes": corpo,
        "url_medida": url_de_amostra,
    }


def entrega(medida, alcancaveis):
    """O veredito que os quatro blocos anteriores nao tinham: CHEGA alguma coisa?

    Calculado dos campos medidos, nunca escrito — e a mesma regra do degrau e da
    prioridade da prospeccao: se a escrita discordar do calculo, o portao reprova.
    """
    if medida["connect"] == "recusado":
        return "bloqueado", "o CONNECT e recusado nas %d passadas (politica de egresso)" % PASSADAS
    if medida["connect"] == "intermitente":
        return "intermitente", "respondeu em %d de %d passadas — a 20.2 nao deixa chamar isto de bloqueio" % (
            sum(1 for c in medida["codigos"] if c != 0), PASSADAS)
    hd = medida["host_do_destino"]
    if hd and hd not in alcancaveis:
        return "liberado_mas_sem_entrega", (
            "o CONNECT passa e o servidor responde %d, mas ele redireciona para `%s`, "
            "que o egresso recusa — nada chega" % (medida["codigos"][0], hd))
    if hd:
        return "alcancavel", "responde %d e redireciona para `%s`, que tambem e alcancavel" % (
            medida["codigos"][0], hd)
    return "alcancavel", "responde %d com %d bytes" % (medida["codigos"][0], medida["bytes"])


# ---------------------------------------------------------------- autoteste

def autoteste():
    """12 casos fabricados. Passada limpa em portao que nunca acusou nada nao prova nada."""
    casos = [
        # (connect, host_do_destino, alcancaveis, veredito esperado)
        ("recusado", None, set(), "bloqueado"),
        ("recusado", "www.x.com", {"www.x.com"}, "bloqueado"),
        ("intermitente", None, set(), "intermitente"),
        ("intermitente", "www.x.com", {"www.x.com"}, "intermitente"),
        ("estabelecido", None, set(), "alcancavel"),
        ("estabelecido", "www.x.com", set(), "liberado_mas_sem_entrega"),
        ("estabelecido", "www.x.com", {"www.x.com"}, "alcancavel"),
        ("estabelecido", "next.outro.com", {"x.com"}, "liberado_mas_sem_entrega"),
        ("estabelecido", "x.com", {"x.com", "y.com"}, "alcancavel"),
        ("recusado", None, {"tudo"}, "bloqueado"),
        ("estabelecido", "WWW.X.COM".lower(), {"www.x.com"}, "alcancavel"),
        ("intermitente", "www.x.com", set(), "intermitente"),
    ]
    falhas = 0
    for i, (connect, hd, alc, esperado) in enumerate(casos, 1):
        m = {"connect": connect, "codigos": [301, 301, 301] if connect == "estabelecido"
             else ([0, 301, 301] if connect == "intermitente" else [0, 0, 0]),
             "host_do_destino": hd, "bytes": 0}
        veredito, _ = entrega(m, alc)
        marca = "ok  " if veredito == esperado else "FALHA"
        if veredito != esperado:
            falhas += 1
        print("  %s caso %2d  connect=%-13s destino=%-14s -> %s (esperado %s)"
              % (marca, i, connect, hd or "-", veredito, esperado))
    # O DOMINIO REGISTRAVEL, que e de onde sai o PEDIDO. Errar aqui produz pedido errado,
    # e pedido errado foi atendido pela metade em 29/09 — e por isso ele tem caso proprio.
    print()
    reg_casos = [
        ("www.quartzolit.weber", "quartzolit.weber"),   # TLD de marca, um rotulo so
        ("quartzolit.weber", "quartzolit.weber"),
        ("www.cascola.com.br", "cascola.com.br"),
        ("s.shopee.com.br", "shopee.com.br"),
        ("www2.camara.leg.br", "camara.leg.br"),         # `leg.br` e sufixo de dois rotulos
        ("run.unl.pt", "unl.pt"),
        ("blog.sagradafamilia.org", "sagradafamilia.org"),
        ("www.cultura.gob.es", "cultura.gob.es"),
        ("fasbam.edu.br", "fasbam.edu.br"),              # ja E o registravel
        ("en.wikipedia.org", "wikipedia.org"),
        ("clubedomosaico.com.br", "clubedomosaico.com.br"),
        ("cortag.com", "cortag.com"),
    ]
    for host, esperado in reg_casos:
        obtido = dominio_registravel(host)
        marca = "ok  " if obtido == esperado else "FALHA"
        if obtido != esperado:
            falhas += 1
        print("  %s registravel  %-26s -> %-22s (esperado %s)" % (marca, host, obtido, esperado))

    # E OS IRMAOS, que sao o que a primeira versao desta ferramenta nao media.
    print()
    irmao_casos = [
        ("www.quartzolit.weber", ["quartzolit.weber"]),
        ("quartzolit.weber", ["www.quartzolit.weber"]),
        ("s.shopee.com.br", ["shopee.com.br", "www.shopee.com.br"]),
        ("fasbam.edu.br", ["www.fasbam.edu.br"]),
    ]
    for host, esperado in irmao_casos:
        obtido = irmaos(host)
        marca = "ok  " if obtido == esperado else "FALHA"
        if obtido != esperado:
            falhas += 1
        print("  %s irmaos de    %-26s -> %s (esperado %s)" % (marca, host, obtido, esperado))

    # O EXTRATOR DE PROSA, cuja primeira versao pediu rede para `validar-banco.py`.
    print()
    prosa = ("dexco.com.br, duratex.com.br e termotecnica.ind.br — com clubedomosaico.com.br "
             "em 200, casca 1.13.0, conferido por validar-banco.py e mutacoes-base.py, secao 20.2")
    obtido = sorted({d.lower() for d in RE_DOMINIO_NU.findall(prosa) if parece_host(d)})
    esperado = ["clubedomosaico.com.br", "dexco.com.br", "duratex.com.br", "termotecnica.ind.br"]
    marca = "ok  " if obtido == esperado else "FALHA"
    if obtido != esperado:
        falhas += 1
    print("  %s prosa -> %s" % (marca, obtido))
    print("       (esperado %s — nem `validar-banco.py` nem `1.13.0` entram)" % esperado)
    prosa_casos = 1

    total = len(casos) + len(reg_casos) + len(irmao_casos) + prosa_casos
    print()
    if falhas:
        sys.exit("AUTOTESTE REPROVADO: %d de %d" % (falhas, total))
    print("AUTOTESTE APROVADO: %d de %d casos. O caso 6 e o mundo medido em 30/09/2026, e os"
          % (total, total))
    print("casos de registravel existem porque foi um pedido escrito pela metade que fez o dia.")


# ---------------------------------------------------------------- relatorio

def montar_md(resultado, quando):
    hosts = resultado["hosts"]
    L = []
    A = L.append
    A("# O QUE ESTA NUVEM ALCANCA DAS FONTES DESTA ILHA")
    A("")
    A("**GERADO por `ferramentas/medir-egresso.py` — nao edite a mao.** A lista de hosts e derivada de")
    A("`dados/*.json` (mais o apex e o `www.` de cada um, que nenhum banco cita e sem os quais nao ha")
    A("diagnostico); medido em **%s**, %d passadas por host, com `%s` como controle." % (quando, PASSADAS, CONTROLE))
    A("")
    A("> **A PERGUNTA QUE ESTE ARQUIVO RESPONDE NAO E \"o dominio esta liberado\": e \"a fonte chega\".**")
    A("> As duas discordaram em 30/09/2026 e a diferenca custou quatro blocos. Apex liberado que")
    A("> redireciona para `www.` recusado entrega **zero** — e ao mesmo tempo `403 ao CONNECT`, que o")
    A("> repositorio afirmava em quatro lugares, era **falso** para os mesmos dominios. Os dois vereditos")
    A("> tem de sair juntos ou nenhum dos dois serve.")
    A("")

    # A TABELA POR DOMINIO REGISTRAVEL, porque e nele que a lista de rede e escrita — e foi
    # medir por host solto que fez a primeira versao desta ferramenta perder o achado do dia.
    A("## POR DOMINIO REGISTRAVEL — e o apex ao lado do `www.`, que e onde o diagnostico mora")
    A("")
    A("| dominio registravel | apex | `www.` | entrega? | URLs de fonte nos bancos |")
    A("|---|---|---|---|---|")
    familias = {}
    for h, r in hosts.items():
        familias.setdefault(r["dominio_registravel"], []).append((h, r))
    def chave(item):
        reg, membros = item
        entrega_alguem = any(r["veredito"] == "alcancavel" for _, r in membros)
        return (entrega_alguem, reg)
    for reg, membros in sorted(familias.items(), key=chave):
        d = dict(membros)
        apex = d.get(reg)
        www = d.get("www." + reg)
        n = sum(r["n_urls"] for _, r in membros)
        def cel(r):
            if r is None:
                return "—"
            return {"alcancavel": "alcanca", "bloqueado": "recusado",
                    "liberado_mas_sem_entrega": "responde, sem entrega",
                    "intermitente": "intermitente"}[r["veredito"]]
        entrega_txt = "**sim**" if any(r["veredito"] == "alcancavel" for _, r in membros) else "**nao**"
        A("| `%s` | %s | %s | %s | %d |" % (reg, cel(apex), cel(www), entrega_txt, n))
    A("")

    # O caso que nomeia o dia: apex que responde e `www.` que nao.
    meio_abertos = [reg for reg, membros in familias.items()
                    if dict(membros).get(reg, {}).get("veredito") in ("alcancavel", "liberado_mas_sem_entrega")
                    and dict(membros).get("www." + reg, {}).get("veredito") == "bloqueado"]
    if meio_abertos:
        A("### A PORTA ESTA PELA METADE, E E ESSE O FATO NOVO")
        A("")
        A("Nestes %d dominios o **apex responde** e o **`www.` e recusado** — e os sites redirecionam" % len(meio_abertos))
        A("tudo para `www.`, entao **nada chega**:")
        A("")
        for reg in sorted(meio_abertos):
            r = dict(familias[reg])[reg]
            A("- `%s` — CONNECT estabelecido, servidor responde **%d** e manda para `%s`, recusado."
              % (reg, r["codigos"][0], r["host_do_destino"] or "?"))
        A("")
        A("**O que isto quer dizer, em uma frase:** o dominio entrou na lista **sem o curinga**, e a 20.1")
        A("manda os dois — `<dominio>` **e** `*.<dominio>`. Falta a metade que serve para algo.")
        A("")

    A("## DETALHE POR HOST")
    A("")
    A("| host | veredito | por que | citado em |")
    A("|---|---|---|---|")
    ordem = {"bloqueado": 0, "liberado_mas_sem_entrega": 1, "intermitente": 2, "alcancavel": 3}
    for h, r in sorted(hosts.items(), key=lambda kv: (ordem.get(kv[1]["veredito"], 9), kv[0])):
        A("| `%s` | **%s** | %s | %s |" % (
            h, r["veredito"], r["motivo"],
            ", ".join(r["citado_por"]) if r["citado_por"] else "_nenhum banco o cita (irmao medido)_"))
    A("")

    pedir = resultado["o_que_pedir"]
    A("## O PEDIDO, DERIVADO DA MEDICAO (20.1 e 20.3)")
    A("")
    if not pedir:
        A("Nada a pedir: toda fonte de que alguma coleta pendente depende chega a esta nuvem.")
    else:
        A("A **20.1** manda acrescentar o dominio **e o curinga**. Caminho: `claude.ai/code` -> seletor de")
        A("ambiente -> Nuvem -> engrenagem -> Dominios permitidos. As linhas, uma por linha:")
        A("")
        A("```")
        for linha in pedir:
            A(linha)
        A("```")
        A("")
        A("**Por que cada um esta na lista** — e nenhum esta por precaucao:")
        A("")
        for reg, arquivos in sorted(resultado.get("por_que_se_pede", {}).items()):
            A("- `%s` — citado por %s." % (reg, ", ".join("`%s`" % a for a in arquivos)))
        A("")
        A("**Enquanto essas linhas nao entrarem, nenhuma execucao da Fundacao le a frase literal do")
        A("fabricante** nesses dominios — e insistir e gastar bloco para reescrever o mesmo motivo, que")
        A("foi o que aconteceu quatro vezes entre 26/09 e 29/09.")
    A("")

    nao_pedidos = sorted(h for h, r in hosts.items()
                         if r["veredito"] != "alcancavel" and h not in NAO_SE_PEDE
                         and r["dominio_registravel"] not in resultado.get("por_que_se_pede", {}))
    if nao_pedidos:
        A("## BLOQUEADO E NAO PEDIDO — porque nenhum trabalho pendente depende dele")
        A("")
        A("Estes hosts tambem nao chegam. Sao **referencia de conteudo ja lida e ja citada** (a fonte esta")
        A("gravada no banco com a data em que foi lida), nao fonte de coleta em aberto. Entram aqui para")
        A("ninguem os confundir com os de cima, e **pedido longo e pedido que nao se atende**:")
        A("")
        for h in nao_pedidos:
            r = hosts[h]
            A("- `%s` — %s." % (h, ", ".join(r["citado_por"]) if r["citado_por"]
                                else "nenhum banco o cita (irmao medido)"))
        A("")

    A("## O QUE NAO SE PEDE POR DESENHO")
    A("")
    for h, por_que in sorted(NAO_SE_PEDE.items()):
        if h in hosts:
            A("- `%s` — %s." % (h, por_que))
    A("")
    return "\n".join(L) + "\n"


def main():
    if AUTOTESTE:
        autoteste()
        return

    achados = hosts_dos_bancos(RAIZ)
    if CONTROLE not in achados:
        sys.exit("o controle `%s` nao aparece em nenhum banco — medicao sem controle e VOID (trava 3)." % CONTROLE)

    print("Hosts derivados de dados/*.json: %d. Controle: %s. Passadas por host: %d.\n"
          % (len(achados), CONTROLE, PASSADAS))

    # Os IRMAOS entram na medicao mesmo sem nenhum banco os citar: sem eles a ferramenta
    # ve so o lado que o banco conhece, e foi assim que a primeira versao nao viu o apex.
    a_medir = dict(achados)
    for h in list(achados):
        for irmao in irmaos(h):
            a_medir.setdefault(irmao, {"urls": set(), "citado_por": set()})

    medidas = {}
    for h in sorted(a_medir):
        amostra = "https://%s/" % h
        medidas[h] = medir_host(h, amostra)
        print("  %-26s connect=%-13s codigos=%s salto=%s%s"
              % (h, medidas[h]["connect"], medidas[h]["codigos"],
                 medidas[h]["host_do_destino"] or "-",
                 "" if h in achados else "   (irmao, nenhum banco o cita)"))

    # TRAVA 3: sem controle verde nas tres passadas, nada e gravado.
    if medidas[CONTROLE]["connect"] != "estabelecido":
        sys.exit("\nVOID: o controle `%s` nao respondeu nas %d passadas (%s). "
                 "Queda de tunel escreveria 'tudo bloqueado' com cara de fato — nada gravado."
                 % (CONTROLE, PASSADAS, medidas[CONTROLE]["codigos"]))

    alcancaveis = {h for h, m in medidas.items() if m["connect"] == "estabelecido"}

    hosts = {}
    for h, m in medidas.items():
        veredito, motivo = entrega(m, alcancaveis)
        hosts[h] = dict(m, veredito=veredito, motivo=motivo,
                        dominio_registravel=dominio_registravel(h),
                        citado_pelo_banco=h in achados,
                        n_urls=len(a_medir[h]["urls"]),
                        citado_por=sorted(a_medir[h]["citado_por"]))

    # O PEDIDO SAI DA MEDICAO E E RESTRITO A QUEM TRAVA COLETA. Host de referencia de conteudo
    # ja lida (enciclopedia, tese, museu) esta bloqueado do mesmo jeito e nao se pede: nenhum
    # trabalho pendente depende dele, e pedido longo e pedido que nao se atende. Quem decide e
    # o arquivo que cita o host, nao uma lista escrita a mao.
    # `fontes-pedidas.json` entra nos gatilhos porque e, por definicao, o arquivo onde uma fonte
    # EXIGIDA e declarada. Ficou de fora na passada das 10h4xZ de 30/09 e o efeito foi absurdo:
    # `loctite.com.br` — o quarto dominio meio-aberto, o que motivou o arquivo — saiu listado em
    # "bloqueado e nao pedido". Portao que nao le o arquivo escrito para ele ler nao mede nada.
    GATILHOS = ("materiais-", "esquema-banco.json", "cobertura.json", "fontes-pedidas.json")

    def trava_coleta(r):
        return any(g in arq for arq in r["citado_por"] for g in GATILHOS)

    nao_se_pede_por_dominio = {dominio_registravel(h) for h in NAO_SE_PEDE}

    pedir, pedir_por_que = [], {}
    for h, r in sorted(hosts.items()):
        if r["dominio_registravel"] in nao_se_pede_por_dominio or r["veredito"] == "alcancavel":
            continue
        # O irmao herda o motivo de quem o banco cita: e o mesmo dominio registravel.
        familia = [x for x in hosts.values()
                   if x["dominio_registravel"] == r["dominio_registravel"]]
        if not any(trava_coleta(x) for x in familia):
            continue
        reg = r["dominio_registravel"]
        for linha in (reg, "*." + reg):
            if linha not in pedir:
                pedir.append(linha)
        pedir_por_que.setdefault(reg, sorted({a for x in familia for a in x["citado_por"]}))
    resultado_pedir_por_que = pedir_por_que

    quando = time.strftime("%Y-%m-%d %H:%MZ", time.gmtime())
    resultado = {"medido_em": quando, "passadas": PASSADAS, "controle": CONTROLE,
                 "hosts": hosts, "o_que_pedir": pedir,
                 "por_que_se_pede": resultado_pedir_por_que}

    print("\nVEREDITOS: " + "  ".join(
        "%s=%d" % (v, sum(1 for r in hosts.values() if r["veredito"] == v))
        for v in ("alcancavel", "liberado_mas_sem_entrega", "intermitente", "bloqueado")))
    if pedir:
        print("A PEDIR (%d linhas): %s" % (len(pedir), " ".join(pedir)))

    if GRAVAR:
        md = os.path.join(RAIZ, "dados", "egresso-de-fontes.md")
        js = os.path.join(RAIZ, "dados", "egresso-de-fontes.json")
        open(md, "w", encoding="utf-8").write(montar_md(resultado, quando))
        json.dump(resultado, open(js, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=2, sort_keys=True, default=list)
        print("\ngravado: %s e %s" % (md, js))


if __name__ == "__main__":
    main()
