#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mede o CANAL DE ESPELHO: por onde esta nuvem consegue abrir documento de fabricante.

    python3 ferramentas/medir-espelho.py .              # so imprime
    python3 ferramentas/medir-espelho.py . --gravar     # escreve dados/canal-de-espelho.md (+ .json)
    python3 ferramentas/medir-espelho.py . --autoteste  # 39 casos fabricados, sem tocar na rede

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

AS DUAS TRAVAS QUE ESTE ARQUIVO FURAVA, medidas em 13/10/2026 e consertadas aqui. As duas sao
da mesma familia: a coluna que decide estava sendo lida da LINHA errada e do ARQUIVO errado.

(a) A TRAVA 4 DIZ "o titulo da pagina 1" E O CODIGO LIA "a primeira linha da pagina 1" — que
    no molde da Quartzolit e o CABECALHO CORRIDO, e cabecalho corrido e texto de molde que
    envelhece sozinho. Em 3 dos 14 documentos ele nomeia OUTRO produto que nao o do documento:
    `1338838.pdf` tem cabecalho `pastilhas exteriores` e produto `pastilhas interiores`;
    `1430424.pdf` tem cabecalho `porcelanato interno cinza` e produto `porcelanato e piso
    sobre piso externo`; `298182.pdf` tem cabecalho `chapix sbr` e produto `Cimentcola
    Cozinhas e Banheiros`. E em 3 outros — as FISPQ — o cabecalho nomeia uma NORMA
    (`Em conformidade com NBR 14725...`) e o produto mora na linha `Produto:`, que o codigo
    nunca alcancava. Seis de catorze catalogados por uma linha que nao e a identidade.
    O CUSTO NESTA ILHA TEM NOME: `pastilhas interiores` declara pastilha de VIDRO para AREAS
    INTERNAS, e a F2 decide por `ambiente`. Quem fosse buscar no inventario a declaracao de
    um produto "para exteriores" acharia um documento que diz o contrario — e publicaria o
    numero na boca de quem nao o publicou.
(b) A TRAVA 1 SEPARA O QUE E DERIVADO DO QUE E DIGITADO, E A DERIVACAO COMIA O PROPRIO RABO.
    `urls_de_espelho_dos_bancos` varria `dados/*.json` INCLUSIVE o `canal-de-espelho.json`
    que ela mesma gera, entao toda URL do inventario voltava na passada seguinte como
    "derivada dos bancos", `citado_por: ["canal-de-espelho.json"]`. Rodando a derivacao velha
    e a nova sobre os MESMOS 22 JSON de `dados/`: 14 contra 2, e os 12 que sairam eram
    citados por UM arquivo so, o gerado. A derivacao real sao DOIS documentos —
    `1200003.pdf` (`materiais-rejuntes.json`) e `908487.pdf` (`materiais-colas.json`) — e os
    outros 12 sao a lista digitada de `ACHADOS_POR_BUSCA`. Um TERCEIRO, `27073.pdf`, aparece
    em `constantes.json` dentro de um NOME DE CHAVE e nao num campo `url`; a derivacao le
    campo `url`, e isso e desenho e nao esquecimento — chave e prosa de quem escreveu, campo
    e dado com nome. A trava 1 existe para que lista digitada nao envelheca calada, e o
    campo de procedencia estava chamando a lista digitada de derivada — apagando justamente
    a distincao que ela protege, e fazendo o arquivo parecer 7 vezes mais ancorado nos bancos
    do que esta.
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


# Arquivos de `dados/` que ESTE script gera, ou que outro script gera a partir do que ele
# gera. Varrer qualquer um deles faz a derivacao comer o proprio rabo: a URL digitada sai no
# inventario, volta na passada seguinte como "derivada dos bancos" e a trava 1 perde o
# sentido. Medido em 13/10/2026 — os 14 documentos do inventario estavam todos marcados
# "derivada", `citado_por: ["canal-de-espelho.json"]`, e a derivacao de verdade era 2.
GERADOS_QUE_NAO_SAO_BANCO = (
    "canal-de-espelho.json",
)


def urls_de_espelho_dos_bancos(raiz):
    """A metade DERIVADA do inventario: toda url de fonte dos bancos que caia no espelho.

    NAO conta o que este script gera (`GERADOS_QUE_NAO_SAO_BANCO`): banco e o que alguem
    escreveu sobre um material, nunca o inventario que saiu daqui."""
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
        if os.path.basename(arq) in GERADOS_QUE_NAO_SAO_BANCO:
            continue
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


MARCA_DE_PAGINA = re.compile(r"P[\u00e1a]g(?:ina)?\.?\s*:?\s*\d+\s*(?:de|/)\s*\d+", re.I)
MARCA_FISPQ = re.compile(r"\bFISPQ\b|FICHA DE INFORMA", re.I)
LINHA_DE_PRODUTO = re.compile(r"^Produto\s*:?\s+(.+)$", re.I)
MOLDE_DO_CABECALHO = re.compile(r"boletim\s+t[\u00e9e]cnico|ficha\s+t[\u00e9e]cnica|^[\s\u2013\u2014-]+$", re.I)


def linhas_uteis(txt):
    """As linhas da pagina com texto de verdade, normalizadas. O corte em 8 e o mesmo de
    sempre: abaixo dele entram numero de pagina solto, `FISPQ` e sujeira de layout."""
    saida = []
    for linha in (txt or "").splitlines():
        linha = " ".join(linha.split())
        if len(linha) > 8:
            saida.append(linha)
    return saida


def _sem_acento(t):
    import unicodedata
    return "".join(c for c in unicodedata.normalize("NFD", (t or "").lower())
                   if unicodedata.category(c) != "Mn")


def identidade_do_texto(txt):
    """O NUCLEO DESTE ARQUIVO, e ele e PURO de proposito: texto da pagina 1 entra, identidade
    sai. Separado do download para poder ser mutado — a versao anterior misturava os dois e a
    unica regua possivel era abrir a rede.

    Devolve sempre as DUAS leituras, porque sao coisas diferentes e so quem as ve lado a lado
    enxerga o defeito: `cabecalho_corrido` (o texto de molde do topo, que envelhece sozinho) e
    `produto_declarado` (a linha com que o documento nomeia o proprio produto). E devolve o que
    o cabecalho E em relacao ao produto, em tres valores, porque "o cabecalho nao nomeia
    produto" (as FISPQ) e "o cabecalho nomeia OUTRO produto" (3 boletins) nao sao o mesmo
    defeito e nao se consertam do mesmo jeito.

    `produto_declarado` fica `None` quando o molde nao foi reconhecido. NUNCA cai de volta no
    cabecalho: identidade errada e pior que identidade ausente, porque ausencia se ve."""
    linhas = linhas_uteis(txt)
    if not linhas:
        return {"familia_do_documento": "sem_texto", "cabecalho_corrido": None,
                "produto_declarado": None, "o_que_o_cabecalho_e": "nao_ha_cabecalho"}

    # FISPQ primeiro, e a ordem importa: a FISPQ tambem tem marca de pagina, e ela aparece
    # DEPOIS da linha `Produto`, nao antes. Testar a marca de pagina primeiro daria o
    # cabecalho como produto justamente nas tres em que o produto esta escrito com esse nome.
    if any(MARCA_FISPQ.search(l) for l in linhas[:5]):
        produto = None
        for l in linhas[:12]:
            m = LINHA_DE_PRODUTO.match(l)
            if m:
                produto = " ".join(m.group(1).split())
                break
        return {"familia_do_documento": "fispq", "cabecalho_corrido": linhas[0],
                "produto_declarado": produto,
                "o_que_o_cabecalho_e": "nao_nomeia_produto"}

    # Boletim no molde da Quartzolit: cabecalho corrido, marca de pagina, e o titulo do
    # produto na primeira linha depois dela.
    for i, l in enumerate(linhas):
        if MARCA_DE_PAGINA.search(l):
            antes = [x for x in linhas[:i]] + [MARCA_DE_PAGINA.sub("", l).strip(" .:-\u2013\u2014")]
            cabecalho = " / ".join([x for x in antes if len(x) > 8]) or None
            produto = linhas[i + 1] if i + 1 < len(linhas) else None
            return {"familia_do_documento": "boletim", "cabecalho_corrido": cabecalho,
                    "produto_declarado": produto,
                    "o_que_o_cabecalho_e": _cabecalho_contra_produto(cabecalho, produto)}

    return {"familia_do_documento": "molde_nao_reconhecido", "cabecalho_corrido": linhas[0],
            "produto_declarado": None, "o_que_o_cabecalho_e": "nao_comparavel"}


def _cabecalho_contra_produto(cabecalho, produto):
    """Tres valores, nunca dois. O que sobra do cabecalho depois de tirar o texto de molde
    (`Boletim Tecnico`, travessoes) e um NOME DE PRODUTO ou nao e nada; e se for um nome,
    ou e o mesmo do documento ou e o de outro produto."""
    if not cabecalho or not produto:
        return "nao_comparavel"
    resto = " ".join(MOLDE_DO_CABECALHO.sub(" ", cabecalho).replace("/", " ").split())
    resto = resto.strip(" .:-\u2013\u2014")
    if len(resto) < 4:
        return "nao_nomeia_produto"
    a, b = _sem_acento(resto), _sem_acento(produto)
    if a in b or b in a:
        return "nomeia_o_mesmo_produto"
    return "nomeia_OUTRO_produto"


def identidade_do_pdf(url):
    """Baixa, extrai a pagina 1 e entrega para `identidade_do_texto`."""
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
    return identidade_do_texto(txt)


# Os casos de identidade. Cada um e um molde de pagina 1 reduzido ao que decide, e a coluna
# `a_regra_velha_dizia` esta aqui para provar que a bateria NAO E INERTE: era isso que o codigo
# de ate 13/10/2026 devolvia, e em 7 dos 12 casos era a linha errada.
CASOS_DE_IDENTIDADE = [
    ("boletim no molde, cabecalho batendo com o produto",
     "Boletim Tecnico - cimentcola externo quartzolit\n   Pag. 1 de 3\n\n"
     "cimentcola externo quartzolit\nargamassa colante para ceramicas\n1. Descricao:",
     "boletim", "cimentcola externo quartzolit",
     "Boletim Tecnico - cimentcola externo quartzolit", "nomeia_o_mesmo_produto",
     "Boletim Tecnico - cimentcola externo quartzolit"),
    ("O DEFEITO MEDIDO: cabecalho de OUTRO produto (`1338838.pdf`, exteriores x interiores)",
     "Boletim Tecnico - pastilhas exteriores quartzolit\n   Pag. 1 de 3\n\n"
     "pastilhas interiores quartzolit\nargamassa colorida para pastilhas\n1. Descricao:",
     "boletim", "pastilhas interiores quartzolit",
     "Boletim Tecnico - pastilhas exteriores quartzolit", "nomeia_OUTRO_produto",
     "Boletim Tecnico - pastilhas exteriores quartzolit"),
    ("cabecalho em DUAS linhas, a segunda com outro nome (`298182.pdf`, chapix sbr)",
     "Boletim Tecnico\n   chapix sbr quartzolit\n   Pag. 1 de 4\n\n"
     "Cimentcola Cozinhas e Banheiros quartzolit\nArgamassa colante para uso interno",
     "boletim", "Cimentcola Cozinhas e Banheiros quartzolit",
     "Boletim Tecnico / chapix sbr quartzolit", "nomeia_OUTRO_produto",
     "Boletim Tecnico"),
    ("FISPQ: o produto esta na linha `Produto`, e o cabecalho e uma NORMA",
     "FISPQ\nEm conformidade com NBR 14725 - parte 4: 2012\n"
     "FICHA DE INFORMACOES DE SEGURANCA DE PRODUTO QUIMICO\n"
     "Produto OSMOCOLOR ST CORES / TRANSPARENTE\nData da ultima revisao: 28.11.2016\npagina 1 de 18",
     "fispq", "OSMOCOLOR ST CORES / TRANSPARENTE",
     "Em conformidade com NBR 14725 - parte 4: 2012", "nao_nomeia_produto",
     "Em conformidade com NBR 14725 - parte 4: 2012"),
    ("FISPQ com dois-pontos e marca de pagina no formato `Pagina: 1/12`",
     "FISPQ\nEm conformidade com NBR 14725:2014\n"
     "FICHA DE INFORMACOES DE SEGURANCA DE PRODUTOS QUIMICOS\n"
     "Produto: PISO SOBRE PISO INTERNO QUARTZOLIT\nRevisao: 00 Data: 09/06/2016 Pagina: 1/12",
     "fispq", "PISO SOBRE PISO INTERNO QUARTZOLIT",
     "Em conformidade com NBR 14725:2014", "nao_nomeia_produto",
     "Em conformidade com NBR 14725:2014"),
    ("A ARMADILHA DE ORDEM: FISPQ cuja marca de pagina vem ANTES da linha `Produto`",
     "FICHA DE INFORMACOES DE SEGURANCA\npagina 1 de 18\nalguma coisa de layout aqui\n"
     "Produto PENTOX CUPIM 0,9L - Base agua",
     "fispq", "PENTOX CUPIM 0,9L - Base agua",
     "FICHA DE INFORMACOES DE SEGURANCA", "nao_nomeia_produto",
     "FICHA DE INFORMACOES DE SEGURANCA"),
    ("FISPQ SEM linha de produto: produto fica `None`, e a familia continua dita",
     "FISPQ\nEm conformidade com NBR 14725:2014\nFICHA DE INFORMACOES DE SEGURANCA\n"
     "Secao 1 - identificacao do produto e da empresa",
     "fispq", None,
     "Em conformidade com NBR 14725:2014", "nao_nomeia_produto",
     "Em conformidade com NBR 14725:2014"),
    ("molde nao reconhecido: NAO cai de volta no cabecalho",
     "CATALOGO DE PRODUTOS 2026\nlinha de revestimentos\nveja mais em nossa loja",
     "molde_nao_reconhecido", None,
     "CATALOGO DE PRODUTOS 2026", "nao_comparavel",
     "CATALOGO DE PRODUTOS 2026"),
    ("pagina sem texto nenhum (PDF so de imagem)",
     "\n   \n\n", "sem_texto", None, None, "nao_ha_cabecalho", None),
    ("marca de pagina na MESMA linha do cabecalho",
     "Boletim Tecnico - bloco de vidro quartzolit      Pag. 1 de 3\n\n"
     "bloco de vidro quartzolit\nargamassa para assentar blocos de vidro",
     "boletim", "bloco de vidro quartzolit",
     "Boletim Tecnico - bloco de vidro quartzolit", "nomeia_o_mesmo_produto",
     "Boletim Tecnico - bloco de vidro quartzolit Pag. 1 de 3"),
    ("marca de pagina na ULTIMA linha: nao sobra linha de produto, e isso e `None`",
     "Boletim Tecnico - alguma coisa quartzolit\nPag. 1 de 3",
     "boletim", None,
     "Boletim Tecnico - alguma coisa quartzolit", "nao_comparavel",
     "Boletim Tecnico - alguma coisa quartzolit"),
    ("cabecalho SO com o molde: nao nomeia produto nenhum, e nao e divergencia",
     "Boletim Tecnico\n     Pag. 1 de 3\n\nsuper formatos quartzolit\nargamassa colante branca",
     "boletim", "super formatos quartzolit",
     "Boletim Tecnico", "nao_nomeia_produto",
     "Boletim Tecnico"),
]


def autoteste_identidade():
    """As quatro colunas esperadas de cada caso, e a quinta so para registro."""
    falhas = 0
    print("  -- identidade lida DENTRO do documento (o defeito de 13/10/2026)")
    for i, (porque, txt, fam, prod, cabecalho, cab, velha) in enumerate(CASOS_DE_IDENTIDADE, 1):
        d = identidade_do_texto(txt)
        ok = (d["familia_do_documento"] == fam and d["produto_declarado"] == prod
              and d["cabecalho_corrido"] == cabecalho and d["o_que_o_cabecalho_e"] == cab)
        falhas += 0 if ok else 1
        print("  %-5s i%02d  %-62s -> %s | %s"
              % ("ok" if ok else "FALHA", i, porque[:62], d["familia_do_documento"],
                 (d["produto_declarado"] or "None")[:40]))
        if not ok:
            print("            esperado: %s | %s | %s | %s" % (fam, prod, cabecalho, cab))
            print("            obtido:   %s | %s | %s | %s" % (d["familia_do_documento"],
                                                               d["produto_declarado"],
                                                               d["cabecalho_corrido"],
                                                               d["o_que_o_cabecalho_e"]))
        if velha != prod:
            print("            (a regra velha devolvia %r — linha errada)" % velha)
    return falhas, len(CASOS_DE_IDENTIDADE)


def autoteste_derivacao():
    """A trava 1 so vale se a derivacao NAO contar o arquivo que este script gera. Monta um
    `dados/` de mentira com um banco de verdade e um `canal-de-espelho.json` gerado, e cobra
    que so o banco conte."""
    import tempfile
    falhas = 0
    print("  -- a derivacao nao come o proprio rabo (trava 1)")
    with tempfile.TemporaryDirectory() as raiz:
        os.makedirs(os.path.join(raiz, "dados"))
        banco = {"itens": [{"fontes": [{"url": "https://telhanorte.vteximg.com.br/arquivos/111.pdf"}]}]}
        gerado = {"inventario": [{"url": "https://telhanorte.vteximg.com.br/arquivos/222.pdf"}]}
        for nome, obj in (("materiais-teste.json", banco), ("canal-de-espelho.json", gerado)):
            with open(os.path.join(raiz, "dados", nome), "w", encoding="utf-8") as fh:
                json.dump(obj, fh)
        achadas = urls_de_espelho_dos_bancos(raiz)
        casos = [
            ("a URL citada pelo BANCO entra",
             "https://telhanorte.vteximg.com.br/arquivos/111.pdf" in achadas, True),
            ("a URL que so existe no arquivo GERADO nao entra",
             "https://telhanorte.vteximg.com.br/arquivos/222.pdf" in achadas, False),
            ("e quem cita e nomeado pelo arquivo de banco",
             achadas.get("https://telhanorte.vteximg.com.br/arquivos/111.pdf") == ["materiais-teste.json"], True),
        ]
        for j, (porque, obtido, esperado) in enumerate(casos, 1):
            ok = obtido == esperado
            falhas += 0 if ok else 1
            print("  %-5s d%02d  %-62s -> %s" % ("ok" if ok else "FALHA", j, porque[:62], obtido))
    return falhas, 3


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
    f_id, n_id = autoteste_identidade()
    f_de, n_de = autoteste_derivacao()
    falhas += f_id + f_de
    total += n_id + n_de
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
            ident = identidade_do_pdf(url) or {}
            item["familia_do_documento"] = ident.get("familia_do_documento")
            item["cabecalho_corrido"] = ident.get("cabecalho_corrido")
            item["produto_declarado"] = ident.get("produto_declarado")
            item["o_que_o_cabecalho_e"] = ident.get("o_que_o_cabecalho_e")
            # O campo antigo fica, com o MESMO nome e o significado consertado: a identidade e
            # o produto que o documento declara. Quando o molde nao foi reconhecido ele fica
            # `null` em vez de cair no cabecalho — ausencia se ve, identidade errada nao.
            item["identidade_lida_no_documento"] = ident.get("produto_declarado")
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
    A("coluna que vale e a do PRODUTO DECLARADO, lida na linha com que o documento nomeia o")
    A("proprio produto. **A coluna do cabecalho esta ao lado de proposito**: ate 13/10/2026 era ela")
    A("que entrava aqui como identidade, e em 6 dos 14 documentos ela nao nomeia o produto do")
    A("documento — em 3 nomeia OUTRO produto, e nas 3 FISPQ nomeia uma norma.")
    A("")
    A("| arquivo | codigo | tipo | bytes | entrada | molde | cabecalho corrido (molde do topo) | PRODUTO DECLARADO no documento | o cabecalho |")
    A("|---|---|---|---|---|---|---|---|---|")
    for i in r["inventario"]:
        A("| `%s` | %s | %s | %s | %s | %s | %s | **%s** | `%s` |"
          % (i["url"].split("/")[-1], i["codigo"], i.get("content_type") or "-", i.get("bytes") or 0,
             "derivada" if i["procedencia_da_entrada"].startswith("derivada") else "busca",
             i.get("familia_do_documento") or "—",
             i.get("cabecalho_corrido") or "—",
             i.get("produto_declarado") or "— (molde nao reconhecido)",
             i.get("o_que_o_cabecalho_e") or "—"))
    A("")
    divergentes = [i for i in r["inventario"] if i.get("o_que_o_cabecalho_e") == "nomeia_OUTRO_produto"]
    A("### Onde o cabecalho nomeia OUTRO produto — %d de %d documentos lidos" % (len(divergentes), len(pdfs)))
    A("")
    if not divergentes:
        A("Nenhum nesta medicao.")
    else:
        A("| arquivo | o cabecalho diz | o documento e de |")
        A("|---|---|---|")
        for i in divergentes:
            A("| `%s` | %s | **%s** |" % (i["url"].split("/")[-1], i.get("cabecalho_corrido"),
                                          i.get("produto_declarado")))
    A("")
    derivadas_md = [i for i in r["inventario"] if i["procedencia_da_entrada"].startswith("derivada")]
    A("### Quanto deste inventario sai dos bancos, e quanto e lista digitada")
    A("")
    A("**Derivado de banco: %d de %d.** O resto e `ACHADOS_POR_BUSCA`, digitado, e a trava 1 existe"
      % (len(derivadas_md), len(r["inventario"])))
    A("para que isso fique dito. *(Ate 13/10/2026 este numero saia 14 de 14, porque a derivacao varria")
    A("o proprio `canal-de-espelho.json` que ela gera — a lista digitada voltava como derivada, citada")
    A("pelo arquivo gerado. Medido nos dois mundos sobre os mesmos JSON de `dados/`: 14 contra 2.)*")
    A("")
    A("E um terceiro documento, `27073.pdf`, e citado em `constantes.json` dentro de um **nome de")
    A("chave** e nao num campo `url`. A derivacao le campo `url`, por desenho: chave e prosa de quem")
    A("escreveu, campo e dado com nome. Fica dito aqui para ninguem ler a coluna `entrada` como")
    A("\"nenhum banco conhece este arquivo\".")
    A("")
    for i in derivadas_md:
        A("- `%s` — citado por %s" % (i["url"].split("/")[-1], ", ".join("`%s`" % c for c in i["citado_por"]) or "—"))
    A("")
    A("## O que esta medicao NAO autoriza")
    A("")
    A("- **Espelho nao e nivel 1.** Do espelho sai o documento, nao a garantia de que a revisao e a")
    A("  vigente. O boletim do `cimentcola externo` aqui e de **maio de 2016** e a pendencia que ele")
    A("  fecha aponta para o arquivo **2024-09**.")
    A("- **Espelho nao batiza** (26.2). O nome do arquivo e do varejista, e a trava do batismo leu")
    A("  `1200003.pdf` e `908487.pdf` como se fossem o fabricante escrevendo o nome do produto — duas")
    A("  vezes em 05/10/2026, nos dois casos acusando um campo certo.")
    A("- **E o CABECALHO CORRIDO nao batiza tampouco — isto e novo em 13/10/2026.** A coluna do")
    A("  cabecalho esta nesta tabela para ser LIDA CONTRA o produto, nunca para ser copiada: em 3 dos")
    A("  14 documentos ela nomeia outro produto, e nas 3 FISPQ nomeia uma norma. Quem precisar do nome")
    A("  comercial de um produto continua indo ao `batismo_do_fabricante`; o que este inventario")
    A("  responde e **qual produto este arquivo descreve**, que e outra pergunta.")
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
