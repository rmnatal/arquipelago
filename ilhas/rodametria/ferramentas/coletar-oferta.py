#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Casa a OFERTA da loja com o REGISTRO do banco — os degraus 1 a 3 da 25.1.

    python3 ferramentas/coletar-oferta.py             # mede e mostra o que mudaria
    python3 ferramentas/coletar-oferta.py --gravar    # mede e grava
    python3 ferramentas/coletar-oferta.py --conferir  # SEM REDE: confere o que esta escrito

POR QUE ISTO EXISTE
-------------------
`coletar-piso-de-compra.py` para no degrau 4 de proposito, e escreveu o motivo
em todo registro: *"escolher ficha de produto e casar oferta com registro, que e
o casamento das cinco armadilhas da 25.7, e e bloco proprio"*. Este arquivo e
esse bloco.

Ele resolve TRES coisas de uma vez, e as tres sao da 25.4-b e da 32.1:
  - `url_produto`, sem a qual o teste de vida da 25.4-b nao existe nesta ilha;
  - a FOTO que o cartao do molde pede — os cartoes da F2 servem espaco
    reservado de 44 px porque nenhum registro tem imagem;
  - a ficha, que e o caminho para o campo tecnico que o anuncio de busca nao da.

O QUE ELE NAO FAZ, e e a regra inteira da 25.4-b.1
--------------------------------------------------
Ele NAO grampeia `url_produto` ao lado de um `url` que ja existia. Os dois saem
da MESMA oferta, medida nesta passada: `url_produto` e o `productLink` da oferta
escolhida, e `url` e o encurtamento DAQUELA url, pedido com o `sub_id` da ilha.
`par_colhido_em` e a prova de que ninguem juntou duas coisas que nunca se viram.

E ele NAO apaga o piso. Pela 25.2 a ficha vira o BOTAO e a busca desce para a
linha discreta: ficha morre, busca nao.

ONDE AS REGRAS MORAM
--------------------
Em `dados/esquema-banco.json`, na secao `casamento_de_oferta` — identidade
minima, as seis travas, a ordem de escolha, como se mede o degrau 1 e as tres
causas separadas de "nao casou". Aqui mora so a MAQUINA que as aplica. E o mesmo
motivo da `escada_de_compra`: lista dentro da regua envelhece calada, e caso novo
entraria sem trava nenhuma com o banco verde.

A LICAO QUE ESTE ARQUIVO HERDA PRONTA (25.9)
--------------------------------------------
"Nao casou" tem TRES causas que parecem uma, e contadas juntas viram um numero
que nao diz o que fazer. Na Aquametria o numero `12` foi lido como mercado
QUATRO vezes seguidas, e a quinta medicao — item por item, degrau por degrau —
achou `9 de mercado + 2 barrados com razao + 1 defeito nosso`. Por isso aqui a
contagem sai separada em `mercado_nao_anuncia`, `candidato_barrado` e
`sem_identidade_minima`, sempre, mesmo quando uma delas e zero.
"""
import argparse
import importlib.util
import json
import re
import struct
import sys
import unicodedata
import urllib.error
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SUB_ID_1 = "rodametria"
BYTES_DO_CABECALHO = 32768          # o bastante para o cabecalho de JPEG, PNG e WebP
TEMPO_LIMITE = 45


# --------------------------------------------------------------- o piso, por um canal so
def _piso():
    """`coletar-piso-de-compra.py`, importado em vez de copiado.

    A escada de palavra-chave, o termo de contexto e a medida de encaixe sao os
    MESMOS desta ilha, e duas copias delas divergiriam na primeira vez que o
    esquema mudasse. O nome do arquivo tem hifen, que nao e nome de modulo
    Python, entao a importacao e por caminho."""
    caminho = RAIZ / "ferramentas" / "coletar-piso-de-compra.py"
    spec = importlib.util.spec_from_file_location("rdm_piso", caminho)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["rdm_piso"] = mod
    spec.loader.exec_module(mod)
    return mod


PISO = _piso()


def regras(esquema):
    r = esquema.get("casamento_de_oferta")
    if not r:
        raise SystemExit("ERRO: `casamento_de_oferta` nao existe em dados/esquema-banco.json. "
                         "As travas da 25.7 moram no ESQUEMA, nunca dentro desta regua.")
    return r


# --------------------------------------------------------------- a lingua do anuncio
def normalizar(texto):
    """Minuscula, sem acento, `+` virando o token `plus`, resto virando espaco.

    O `+` e tratado ANTES de tudo porque `S10+` e outro aparelho que `S10`
    (25.7(4)) e a normalizacao ingenua apagaria justamente o caractere que os
    separa."""
    if not texto:
        return ""
    t = unicodedata.normalize("NFD", str(texto))
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    t = t.lower().replace("+", " plus ")
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def fichas(texto):
    return normalizar(texto).split() if normalizar(texto) else []


def ocorrencias(agulha, palheiro):
    """Indices em que a sequencia de tokens `agulha` comeca dentro de `palheiro`.

    Comparacao por TOKEN e nao por substring: `v1` nao casa com `v10`, e
    `m2 max` nao casa com `m2 maxi`. Isto e a trava 6 (modelo CONTIGUO) e e o
    que a 25.9 manda NAO afrouxar: o conserto e do dado, nunca da trava."""
    if not agulha:
        return []
    n = len(agulha)
    return [i for i in range(len(palheiro) - n + 1) if palheiro[i:i + n] == agulha]


def tokens_dos_termos(escada):
    """Todo token de todo termo de contexto declarado no esquema, por entidade.

    DERIVADO, nunca escrito aqui: tipo novo no esquema passa a proteger os
    outros no dia em que e declarado."""
    por_entidade = {}
    for entidade, bloco in escada["termo_de_contexto"].items():
        if not isinstance(bloco, dict) or "valores" not in bloco:
            continue
        toks = set()
        for termo in bloco["valores"].values():
            toks.update(fichas(termo))
        por_entidade[entidade] = toks
    return por_entidade


def primeiras_palavras_dos_termos(escada, entidade):
    """A PRIMEIRA palavra de cada termo daquela entidade — o nome do objeto.

    `camara de ar` -> `camara`; `patinete eletrico` -> `patinete`. E com ela que
    a trava 3(b) decide se a cabeca do titulo comeca com outro objeto."""
    bloco = escada["termo_de_contexto"].get(entidade) or {}
    saida = set()
    for termo in (bloco.get("valores") or {}).values():
        t = fichas(termo)
        if t:
            saida.add(t[0])
    return saida


# --------------------------------------------------------------- as seis travas da 25.7
def _tem_palavra(lista, tokens):
    """True quando qualquer entrada da lista aparece na sequencia de tokens.

    Entrada com espaco (`par de`) e casada como sequencia, nao como palavra."""
    for bruto in lista or []:
        alvo = fichas(bruto)
        if alvo and ocorrencias(alvo, tokens):
            return True
    return False


def trava_cobertura(oferta, regra, cabeca_tokens):
    if _tem_palavra(regra["palavras"], cabeca_tokens):
        achada = next(p for p in regra["palavras"]
                      if ocorrencias(fichas(p), cabeca_tokens))
        return "a cabeca do titulo diz `%s`: a coisa que cobre o objeto nao e o objeto (25.7(1))" % achada
    return None


def trava_kit(oferta, regra, tokens, primeira_do_termo):
    if _tem_palavra(regra["palavras"], tokens):
        achada = next(p for p in regra["palavras"] if ocorrencias(fichas(p), tokens))
        return "o titulo diz `%s` e o registro nao e um kit (25.7(2))" % achada
    # multipack: numeral MAIOR QUE UM colado no nome do objeto. `01 Camara` e um.
    for i, tok in enumerate(tokens[:-1]):
        if not tok.isdigit():
            continue
        seguinte = tokens[i + 1]
        if int(tok) > 1 and (seguinte in primeira_do_termo
                             or seguinte.rstrip("s") in primeira_do_termo):
            return ("o titulo anuncia `%s %s`: multipack, e o cartao publicaria o preco de %s "
                    "unidades para um registro que declara uma (25.7(2))" % (tok, seguinte, tok))
    return None


def trava_produto_na_cabeca(oferta, tokens, cabeca_tokens, termo, objetos_de_fora, proprio_objeto):
    termo_tokens = fichas(termo) if termo else []
    if termo_tokens and not ocorrencias(termo_tokens, tokens):
        return "o titulo nao traz o termo `%s`, que e o que diz O QUE o produto e (25.7(3))" % termo
    for i, tok in enumerate(cabeca_tokens[:3]):
        if tok in objetos_de_fora and tok != proprio_objeto:
            return ("a cabeca do titulo comeca por `%s`, que e o nome de outro objeto no esquema "
                    "desta ilha: loja de reposicao escreve o nome do aparelho no titulo da peca "
                    "(25.7(3))" % tok)
    return None


def trava_sufixo(oferta, regra, tokens, modelo_tokens, termo_tokens, frase_curta):
    """TODAS as ocorrencias do modelo, nao a primeira.

    Anuncio que enumera a serie (`M2 Pro,M2 MAX,M2 MAX-B`) tem uma ocorrencia
    limpa e uma sufixada; aprovar pela limpa e aprovar o anuncio inteiro, que e
    a armadilha 5 entrando pela porta da 4."""
    if not modelo_tokens:
        return None
    for i in ocorrencias(modelo_tokens, tokens):
        j = i + len(modelo_tokens)
        if j >= len(tokens):
            continue
        seguinte = tokens[j]
        if len(seguinte) > 4:
            continue
        if re.match(r"^[0-9]+[a-z]*$", seguinte):
            continue
        if seguinte in termo_tokens or seguinte in frase_curta:
            continue
        return ("o modelo vem seguido de `%s`, que e sufixo de modelo e faz outro aparelho "
                "(25.7(4))" % seguinte)
    return None


def trava_enumeracao_da_serie(oferta, tokens, modelo_tokens, modelo):
    """O modelo aparecendo MAIS DE UMA VEZ e anuncio que enumera a serie.

    Esta trava existe porque a trava 4 ja barrava estes anuncios — pelo motivo
    ERRADO. Medido em 29/10/2026: `HONEYWHALE M2 Pro,M2 MAX,M2 MAX-B modelos da
    serie` era recusado com *"o modelo vem seguido de `m2`, que e sufixo de
    modelo"*, e `m2` ali nao e sufixo: e o comeco do modelo SEGUINTE da lista. O
    veredito estava certo e a frase, que e o que a execucao seguinte le dentro do
    banco, estava errada. Motivo que explica mal e da familia do motivo que
    envelhece calado (25.4-b.3): ele manda consertar a coisa errada."""
    if not modelo_tokens:
        return None
    if len(ocorrencias(modelo_tokens, tokens)) > 1:
        return ("o titulo nomeia `%s` mais de uma vez: e anuncio que ENUMERA a serie, e no maximo "
                "um dos modelos enumerados e este registro — nao ha como dizer qual, entao caem "
                "todos (25.7(5))" % modelo)
    return None


def trava_outro_registro(oferta, tokens, modelos_irmaos, meu_modelo_tokens):
    for ident, irmao in modelos_irmaos:
        alvo = fichas(irmao)
        if not alvo or alvo == meu_modelo_tokens:
            continue
        if ocorrencias(alvo, tokens):
            return ("o titulo tambem nomeia o modelo `%s` (registro `%s` deste banco): "
                    "casamento que nao identifica UM registro nao identifica nenhum "
                    "(25.7(5))" % (irmao, ident))
    return None


def trava_faixa_de_preco(oferta):
    pmin, pmax = oferta.get("preco_min"), oferta.get("preco_max")
    if pmin is None or pmax is None:
        return None
    try:
        if float(pmin) != float(pmax):
            return ("o anuncio tem preco em FAIXA (%s a %s): e anuncio de multipla variante, e o "
                    "cartao publica UM preco (25.7(5))" % (pmin, pmax))
    except (TypeError, ValueError):
        return None
    return None


def trava_modelo_contiguo(oferta, tokens, modelo_tokens, modelo):
    if modelo_tokens and not ocorrencias(modelo_tokens, tokens):
        return "o titulo nao traz o modelo `%s` com as partes contiguas (25.9(1))" % modelo
    return None


def julgar(oferta, registro, entidade, escada, reg, modelos_irmaos):
    """(aprovada, motivo). Motivo em portugues, sempre, inclusive na aprovacao."""
    tokens = fichas(oferta.get("titulo"))
    if not tokens:
        return False, "a oferta veio sem titulo"
    quantos = reg["travas"]["3_o_produto_na_cabeca"].get("cabeca_em_caracteres")
    if not isinstance(quantos, int):
        raise SystemExit("ERRO: `travas.3_o_produto_na_cabeca.cabeca_em_caracteres` tem de ser um "
                         "numero no esquema. O tamanho da cabeca e regra, e regra nao se le de "
                         "dentro de uma frase em prosa.")
    cabeca_tokens = normalizar(oferta.get("titulo"))[:quantos].split()

    modelo = registro.get("modelo")
    modelo_tokens = fichas(modelo) if modelo else []

    if entidade == "VEICULO":
        termo = PISO.termo_de(escada, "VEICULO", registro.get("tipo_comercial"))
        proprio = (fichas(termo) or [None])[0]
        de_fora = primeiras_palavras_dos_termos(escada, "PECA")
    else:
        termo = PISO.termo_de(escada, "PECA", registro.get("tipo"))
        proprio = (fichas(termo) or [None])[0]
        de_fora = primeiras_palavras_dos_termos(escada, "PECA") | \
            primeiras_palavras_dos_termos(escada, "VEICULO")

    termo_tokens = set(fichas(termo)) if termo else set()
    frase_curta = set(reg["travas"]["4_o_sufixo_faz_outro_aparelho"]
                      ["o_que_NAO_e_sufixo"]["palavras_de_frase_curtas"])
    primeira_do_termo = primeiras_palavras_dos_termos(
        escada, "VEICULO" if entidade == "VEICULO" else "PECA")

    marca = registro.get("marca")
    if marca and not ocorrencias(fichas(marca), tokens):
        return False, "o titulo nao traz a marca `%s`" % marca

    for motivo in (
        trava_modelo_contiguo(oferta, tokens, modelo_tokens, modelo),
        trava_cobertura(oferta, reg["travas"]["1_cobertura_nao_e_o_objeto"], cabeca_tokens),
        trava_kit(oferta, reg["travas"]["2_kit_nao_e_quantidade"], tokens, primeira_do_termo),
        trava_produto_na_cabeca(oferta, tokens, cabeca_tokens, termo, de_fora, proprio),
        trava_enumeracao_da_serie(oferta, tokens, modelo_tokens, modelo),
        trava_sufixo(oferta, reg["travas"]["4_o_sufixo_faz_outro_aparelho"],
                     tokens, modelo_tokens, termo_tokens, frase_curta),
        trava_outro_registro(oferta, tokens, modelos_irmaos, modelo_tokens),
        trava_faixa_de_preco(oferta),
    ):
        if motivo:
            return False, motivo

    return True, "marca, modelo contiguo e o produto na cabeca, sem sufixo, sem kit e com preco unico"


# --------------------------------------------------------------- a fonte desta leitura
FONTE = "open-api-afiliados"


def declarar_fonte(registro, hoje, oferta):
    """Declara `open-api-afiliados` em `fontes{}` do registro, no NIVEL 6.

    Isto nao e burocracia e nao foi ideia desta regua: a BANCADA a cobrou. A
    primeira versao deste arquivo gravou uma cotacao citando a fonte
    `open-api-afiliados` e NAO a declarou, e `validar-banco.py` reprovou com
    *"cotacao aponta a fonte 'open-api-afiliados', que nao esta em fontes{}"* —
    a regra de que todo campo cita uma fonte DECLARADA, que o bloco 3 escreveu,
    pegando um defeito do bloco 3d antes de ele chegar ao ar.

    O NIVEL E 6 e a escada do esquema diz por que: o nivel e o do ELO MAIS FRACO
    entre autoria, custodia e leitura. A LEITURA aqui e melhor que a do
    `painel-shopee` — e mecanica, sem ninguem transcrevendo numero a mao —, mas a
    AUTORIA continua sendo o vendedor do anuncio. Logo nivel 6: sustenta preco,
    disponibilidade e o nome comercial, e NAO sustenta campo tecnico que a F1 leia.
    """
    fontes = registro.setdefault("fontes", {})
    fontes[FONTE] = {
        "url": "https://open-api.affiliate.shopee.com.br/graphql (productOfferV2)",
        "tipo": "api-de-afiliado",
        "nivel": 6,
        "origem": "anuncio-de-marketplace",
        "autoria": "o vendedor do anuncio",
        "custodia": "Shopee",
        "leitura": "mecanica, pela Open API de Afiliados — sem transcricao a mao",
        "data_leitura": hoje,
        "observacao": ("Lida pelo bloco 3d em %s, no casamento da 25.1. O nivel e 6 pelo elo mais "
                       "fraco: a leitura e mecanica, e a autoria continua sendo o vendedor. "
                       "Oferta %s na loja %r." % (hoje, oferta.get("item_id"), oferta.get("loja"))),
    }


# --------------------------------------------------------------- identidade minima
def identidade_minima(registro, entidade, reg):
    """(tem, o_que_falta). Registro sem identidade NAO pede ficha, e isso e
    resposta medida e nao lacuna: o piso da 25.2 ja esta nele."""
    bloco = reg["identidade_minima"].get(entidade) or {}
    falta = []
    if "marca" in bloco.get("exige", []) and not registro.get("marca"):
        falta.append("marca")
    if "modelo" in bloco.get("exige", []) and not registro.get("modelo"):
        falta.append("modelo")
    if "medida_de_encaixe" in bloco.get("exige", []) and not PISO.medida_de_encaixe(registro):
        falta.append("medida_de_encaixe")
    if "atributo_que_o_mercado_distingue" in bloco.get("exige", []):
        mapa = bloco.get("atributo_que_o_mercado_distingue") or {}
        tipo = registro.get("tipo")
        if tipo not in mapa:
            raise SystemExit(
                "ERRO: o tipo de peca %r nao esta declarado em "
                "casamento_de_oferta.identidade_minima.PECA.atributo_que_o_mercado_distingue. "
                "Tipo novo entra numa linha do esquema; aqui ele PARA a regua." % tipo)
        atributo = mapa[tipo]
        if atributo and not registro.get(atributo):
            falta.append(atributo)
    return (not falta), falta


# --------------------------------------------------------------- a foto, medida
def dimensao_dos_bytes(dados):
    """(largura, altura) lidas do CABECALHO do arquivo, ou None.

    Mesma leitura de `ilhas/aquametria/ferramentas/regua-cdn-shopee.py`, que a
    nasceu pela 25.7: dimensao DIGITADA e da familia do numero de tela digitado
    — parece conferida. Ou sai do cabecalho, ou nao sai, e sem as duas a foto
    nao entra."""
    if not dados:
        return None
    if dados[:2] == b"\xff\xd8":                                  # JPEG
        i = 2
        while i < len(dados) - 9:
            if dados[i] != 0xFF:
                i += 1
                continue
            marcador = dados[i + 1]
            if marcador in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                            0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                altura, largura = struct.unpack(">HH", dados[i + 5:i + 9])
                return largura, altura
            if marcador in (0xD8, 0xD9) or 0xD0 <= marcador <= 0xD7:
                i += 2
                continue
            if i + 4 > len(dados):
                return None
            i += 2 + struct.unpack(">H", dados[i + 2:i + 4])[0]
        return None
    if dados[:8] == b"\x89PNG\r\n\x1a\n":                         # PNG
        if len(dados) < 24:
            return None
        largura, altura = struct.unpack(">II", dados[16:24])
        return largura, altura
    if dados[:4] == b"RIFF" and dados[8:12] == b"WEBP":           # WebP
        formato = dados[12:16]
        if formato == b"VP8X" and len(dados) >= 30:
            return (int.from_bytes(dados[24:27], "little") + 1,
                    int.from_bytes(dados[27:30], "little") + 1)
        if formato == b"VP8 " and len(dados) >= 30:
            return (struct.unpack("<H", dados[26:28])[0] & 0x3FFF,
                    struct.unpack("<H", dados[28:30])[0] & 0x3FFF)
        if formato == b"VP8L" and len(dados) >= 25:
            if dados[20] != 0x2F:
                return None
            v = int.from_bytes(dados[21:25], "little")
            return ((v & 0x3FFF) + 1, ((v >> 14) & 0x3FFF) + 1)
    return None


def medir_foto(url):
    """(dimensao, erro). Le so o comeco: a dimensao mora no cabecalho, e baixar
    300 KB por foto para ler 4 bytes seria gastar rede por nada."""
    if not url:
        return None, "a oferta veio sem endereco de imagem"
    pedido = urllib.request.Request(url, headers={"Range": "bytes=0-%d" % (BYTES_DO_CABECALHO - 1)})
    try:
        with urllib.request.urlopen(pedido, timeout=TEMPO_LIMITE) as r:
            dados = r.read(BYTES_DO_CABECALHO)
    except (urllib.error.URLError, urllib.error.HTTPError, OSError) as erro:
        return None, "a CDN nao respondeu (%s)" % str(erro)[:80]
    d = dimensao_dos_bytes(dados)
    if not d:
        return None, "os primeiros %d bytes nao traziam cabecalho de JPEG, PNG nem WebP" % len(dados)
    return d, None


# --------------------------------------------------------------- o degrau
def degrau_da_oferta(registro, oferta, reg):
    """(degrau, como_foi_medido). Degrau 1 so pelo NOME DA LOJA carregar a marca.

    NUNCA pelo `shopType`: medido em 29/10/2026 que ele e o programa de vendedor
    da Shopee e nao `loja oficial do fabricante` — `[1]` saiu em `RM BIKES` e em
    `Auto Home Shop`, e a `HONEYWHALE-Scooter`, que carrega a marca, saiu `[]`."""
    marca = registro.get("marca")
    loja = oferta.get("loja") or ""
    if marca and ocorrencias(fichas(marca), fichas(loja)):
        return 1, ("o nome da loja (`%s`) carrega a marca `%s` do registro. `tipo_de_loja` da API "
                   "veio %s e NAO foi usado para decidir isto." % (loja, marca,
                                                                   json.dumps(oferta.get("tipo_de_loja"))))
    return 3, ("o nome da loja (`%s`) nao carrega a marca do registro: anuncio de vendedor comum, "
               "degrau 3 da 25.1, e e por isso que `url_busca` continua gravada. `tipo_de_loja` "
               "da API veio %s e NAO foi usado para decidir isto."
               % (loja, json.dumps(oferta.get("tipo_de_loja"))))


# --------------------------------------------------------------- a rede
def buscar(chave):
    dados, erro = PISO._api(["busca", chave, "--quantos", "10"])
    if erro:
        return None, erro[0] if isinstance(erro, list) else str(erro)
    return dados or [], None


def encurtar(url):
    return PISO.encurtar(url)


# --------------------------------------------------------------- o trabalho
def trabalhar(dados, gravar):
    esquema = dados["esquema-banco"]
    escada = PISO.escada_do_esquema(esquema)
    reg = regras(esquema)
    hoje = date.today().isoformat()

    irmaos = [(r["id"], r.get("modelo"))
              for arq in ("veiculos", "pecas")
              for r in dados[arq]["registros"] if r.get("modelo")]

    # `candidatos_barrados_no_total` e o numero que PROVA que as travas da 25.7
    # trabalharam. Sem ele, um registro que casou esconde os candidatos errados
    # que foram recusados no caminho, e a passada parece nao ter barrado nada —
    # que e exatamente a leitura que a 25.9 mediu custar doze dias.
    placar = {"casou": 0, "mercado_nao_anuncia": 0, "candidato_barrado": 0,
              "sem_identidade_minima": 0, "excluido": 0, "foto_sem_dimensao": 0,
              "ofertas_julgadas_no_total": 0, "candidatos_barrados_no_total": 0}
    linhas = []

    for arq, entidade in (("veiculos", "VEICULO"), ("pecas", "PECA")):
        for r in dados[arq]["registros"]:
            if r.get("status") == "excluido_do_banco":
                placar["excluido"] += 1
                continue

            af = r.setdefault("afiliado", {})
            tem, falta = identidade_minima(r, entidade, reg)
            if not tem:
                placar["sem_identidade_minima"] += 1
                causa = ("CAUSA: o registro nao tem identidade minima para pedir ficha — falta %s. "
                         "Pela `identidade_minima` do esquema, marca sozinha e a armadilha da 25.3 e "
                         "modelo curto sozinho e a armadilha 3 da 25.7, medida nesta ilha: a chave "
                         "`MAXSHOT` devolveu pelicula de celular e suplemento. O piso da 25.2 "
                         "continua no registro e a pagina continua com porta de compra."
                         % " + ".join("`%s`" % f for f in falta))
                af["motivo_sem_url_produto"] = (
                    "%s || ULTIMA TENTATIVA: nenhuma chamada em %s — colher %s e trabalho de "
                    "coleta, nao de casamento." % (causa, hoje, " e ".join(falta)))
                linhas.append(("sem_identidade", r["id"], "falta " + " + ".join(falta)))
                continue

            chaves = PISO.candidatas(r, entidade, escada)
            barrados, medidos, escolhida, chave_usada, degrau_chave = [], [], None, None, None

            for nome_degrau, chave in chaves:
                ofertas, erro = buscar(chave)
                if erro:
                    medidos.append((nome_degrau, chave, "erro: %s" % erro))
                    continue
                medidos.append((nome_degrau, chave, "%d oferta(s)" % len(ofertas)))
                aprovadas = []
                for o in ofertas:
                    placar["ofertas_julgadas_no_total"] += 1
                    ok, motivo = julgar(o, r, entidade, escada, reg, irmaos)
                    if ok:
                        aprovadas.append(o)
                    else:
                        placar["candidatos_barrados_no_total"] += 1
                        barrados.append((o.get("titulo"), motivo))
                if aprovadas:
                    # A ordem da 25.7/secao 7, declarada em
                    # `casamento_de_oferta.ordem_de_escolha.criterios_em_ordem`:
                    # vendas, depois nota, depois `item_id` so para o desempate
                    # ser estavel entre passadas. A COMISSAO nunca ordena.
                    aprovadas.sort(key=lambda o: (-_num(o.get("vendas")),
                                                  -_num(o.get("nota")),
                                                  _num(o.get("item_id"))))
                    escolhida, chave_usada, degrau_chave = aprovadas[0], chave, nome_degrau
                    break

            if not escolhida:
                if barrados:
                    placar["candidato_barrado"] += 1
                    qual = "candidato_barrado"
                    causa = ("CAUSA: houve candidato e as travas da 25.7 o barraram. Isto NAO e "
                             "ausencia de oferta, e e a distincao que a 25.9 mediu custar caro: "
                             "lido como mercado, o numero se confirma sozinho em toda medicao "
                             "seguinte. Pode se resolver com dado melhor no registro; nunca com "
                             "trava mais frouxa (25.9(1)).")
                    detalhe = "; ".join("%r -> %s" % (t[:60], m) for t, m in barrados[:4])
                else:
                    placar["mercado_nao_anuncia"] += 1
                    qual = "mercado_nao_anuncia"
                    causa = ("CAUSA: a escada inteira devolveu ZERO oferta. Nenhuma trava foi "
                             "acionada — o produto nao esta anunciado nesta loja, e isso so se "
                             "resolve quando o mercado mudar. Zero nao e erro: e medicao (25.6(a)).")
                    detalhe = "; ".join("%s=%s" % (n, q) for n, _c, q in medidos)
                af["motivo_sem_url_produto"] = (
                    "%s || ULTIMA TENTATIVA: %s, degraus medidos: %s" % (causa, hoje, detalhe))
                linhas.append((qual, r["id"], detalhe[:150]))
                continue

            # --- o par, e ele vem da MESMA oferta (25.4-b.1)
            url_produto = escolhida.get("url_produto")
            curto, erro = encurtar(url_produto)
            if erro or not curto:
                placar["candidato_barrado"] += 1
                af["motivo_sem_url_produto"] = (
                    "CAUSA: uma oferta passou as travas da 25.7 e o ENCURTAMENTO dela falhou, e pela "
                    "25.4-b.1 nenhum dos dois campos entra sozinho — gravar `url_produto` ao lado de "
                    "um `url` que nao e dele e fabricar a aparencia de um par conferido. "
                    "|| ULTIMA TENTATIVA: %s, oferta %s, a API respondeu: %s"
                    % (hoje, escolhida.get("item_id"), erro or "sem link"))
                linhas.append(("encurtamento_falhou", r["id"], str(erro)[:120]))
                continue

            degrau, como = degrau_da_oferta(r, escolhida, reg)
            af.update({
                "programa": "shopee",
                "degrau": degrau,
                "degrau_como_foi_medido": como,
                "url": curto,
                "url_produto": url_produto,
                "par_colhido_em": hoje,
                "item_id": escolhida.get("item_id"),
                "shop_id": escolhida.get("shop_id"),
                "loja": escolhida.get("loja"),
                "vendas_na_medicao": escolhida.get("vendas"),
                "nota_na_medicao": escolhida.get("nota"),
                "tipo_de_loja_na_medicao": escolhida.get("tipo_de_loja"),
                "titulo_da_oferta": escolhida.get("titulo"),
                "chave_do_casamento": chave_usada,
                "degrau_da_chave_do_casamento": degrau_chave,
                "candidatos_barrados": [{"titulo": t, "motivo": m} for t, m in barrados],
                "motivo_sem_url_produto": None,
            })
            af.setdefault("sub_id_1", SUB_ID_1)

            # --- a fonte DESTA leitura, declarada antes de qualquer campo cita-la
            declarar_fonte(r, hoje, escolhida)

            # --- a foto, MEDIDA nos primeiros bytes (25.7)
            dim, erro_foto = medir_foto(escolhida.get("imagem_url"))
            if dim:
                nome = " ".join(x for x in (r.get("marca"), r.get("modelo")) if x) or r["id"]
                r["imagem"] = {
                    "url": escolhida.get("imagem_url"),
                    "largura": dim[0],
                    "altura": dim[1],
                    "alt": nome,
                    "fonte": FONTE,
                    "de_qual_oferta": escolhida.get("item_id"),
                    "dimensao_medida_em": hoje,
                    "como_a_dimensao_foi_medida": "cabecalho do arquivo na CDN, primeiros %d bytes"
                                                  % BYTES_DO_CABECALHO,
                }
            else:
                placar["foto_sem_dimensao"] += 1
                r["imagem"] = None
                af["motivo_sem_imagem"] = (
                    "CAUSA: a 25.7 exige largura e altura MEDIDAS, e sem as duas a foto nao entra — "
                    "salto de layout quando a imagem carrega e pior que nao ter foto. "
                    "|| ULTIMA TENTATIVA: %s — %s" % (hoje, erro_foto))

            # --- a cotacao entra como SERIE, nunca substituindo a anterior
            preco = _preco(escolhida)
            if preco is not None:
                serie = r.setdefault("cotacoes", [])
                if not any(c.get("data_leitura") == hoje and c.get("item_id") == escolhida.get("item_id")
                           for c in serie):
                    serie.insert(0, {
                        "valor_brl": preco,
                        "loja": "Shopee",
                        "programa": "shopee",
                        "item_id": escolhida.get("item_id"),
                        "comissao_declarada_pct": None,
                        "vendas_declaradas": escolhida.get("vendas"),
                        "data_leitura": hoje,
                        "fonte": "open-api-afiliados",
                    })

            placar["casou"] += 1
            linhas.append(("casou", r["id"],
                           "degrau %s, %s, %s, %d candidato(s) barrado(s) no caminho"
                           % (degrau, escolhida.get("loja"),
                              "foto %dx%d" % dim if dim else "SEM foto", len(barrados))))
            for titulo, motivo in barrados:
                linhas.append(("barrado", r["id"], "%r -> %s" % ((titulo or "")[:58], motivo)))

    return placar, linhas


def _num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def _preco(oferta):
    pmin, pmax = oferta.get("preco_min"), oferta.get("preco_max")
    if pmin is None:
        return None
    try:
        if pmax is not None and float(pmin) != float(pmax):
            return None            # faixa nao e preco; a trava ja barrou, isto e cinto
        return round(float(pmin), 2)
    except (TypeError, ValueError):
        return None


# --------------------------------------------------------------- o conferidor, SEM REDE
def conferir(dados):
    """Confere o que esta ESCRITO, sem tocar na rede.

    Ele nao repete a medicao: ele cobra a FORMA do que a medicao gravou — e e o
    que pega grampeamento, par pela metade e foto sem dimensao."""
    esquema = dados["esquema-banco"]
    reg = regras(esquema)
    falhas, afirmacoes = [], 0

    def exigir(cond, texto):
        nonlocal afirmacoes
        afirmacoes += 1
        if not cond:
            falhas.append(texto)

    exigir(esquema.get("versao_esquema", 0) >= 3,
           "o esquema tem de estar na versao 3 ou mais: `casamento_de_oferta` entrou nela")
    for chave in ("identidade_minima", "travas", "ordem_de_escolha", "degrau_que_se_grava",
                  "a_foto", "o_par_vem_da_MESMA_oferta", "quando_nao_casa"):
        exigir(chave in reg, "`casamento_de_oferta.%s` tem de existir no esquema" % chave)
    exigir(len(reg["travas"]) >= 7,
           "as SEIS travas da 25.7/25.9 mais a regra-mae tem de estar declaradas no esquema")

    for arq in ("veiculos", "pecas"):
        for r in dados[arq]["registros"]:
            if r.get("status") == "excluido_do_banco":
                continue
            ident, af = r["id"], (r.get("afiliado") or {})
            tem_u, tem_p = bool(af.get("url")), bool(af.get("url_produto"))

            exigir(tem_u == tem_p,
                   "%s: `url` e `url_produto` tem de existir os DOIS ou NENHUM — a 25.4-b.1 proibe "
                   "grampear um ao lado do outro (url=%s, url_produto=%s)" % (ident, tem_u, tem_p))

            if tem_u and tem_p:
                exigir(bool(af.get("par_colhido_em")),
                       "%s: par sem `par_colhido_em` nao tem prova de que os dois sairam da mesma "
                       "oferta (25.4-b.1)" % ident)
                exigir(af.get("degrau") in (1, 2, 3),
                       "%s: registro com ficha tem de estar no degrau 1, 2 ou 3 (esta em %r)"
                       % (ident, af.get("degrau")))
                exigir(bool(af.get("degrau_como_foi_medido")),
                       "%s: o degrau tem de dizer COMO foi medido — o esquema proibe decidi-lo pelo "
                       "`shopType`" % ident)
                exigir("NAO foi usado para decidir" in (af.get("degrau_como_foi_medido") or ""),
                       "%s: o `degrau_como_foi_medido` tem de dizer, em palavras, que o "
                       "`tipo_de_loja` da API nao decidiu o degrau — foi medido em 29/10/2026 que "
                       "ele nao diz `loja oficial do fabricante`" % ident)
                exigir(bool(af.get("url_busca")),
                       "%s: ganhar ficha NAO apaga o piso — a 25.2 manda a busca descer para a linha "
                       "discreta, nao sair" % ident)
                exigir(af.get("motivo_sem_url_produto") is None,
                       "%s: registro COM ficha nao pode carregar motivo de ficha ausente" % ident)
                exigir(bool(af.get("titulo_da_oferta")),
                       "%s: sem o titulo da oferta escolhida ninguem consegue reconferir o "
                       "casamento com os olhos (25.3)" % ident)
            else:
                exigir(bool(af.get("motivo_sem_url_produto")),
                       "%s: registro sem ficha tem de dizer POR QUE, e o silencio e o defeito que a "
                       "25.9 mediu custar doze dias" % ident)
                m = af.get("motivo_sem_url_produto") or ""
                exigir("CAUSA:" in m and "|| ULTIMA TENTATIVA:" in m,
                       "%s: o motivo tem de separar CAUSA de ULTIMA TENTATIVA (25.4-b.3) — motivo "
                       "velho manda a execucao seguinte nem tentar" % ident)

            img = r.get("imagem")
            if img:
                exigir(bool(img.get("url")), "%s: imagem sem endereco" % ident)
                exigir(isinstance(img.get("largura"), int) and img["largura"] > 0,
                       "%s: imagem sem largura MEDIDA (25.7)" % ident)
                exigir(isinstance(img.get("altura"), int) and img["altura"] > 0,
                       "%s: imagem sem altura MEDIDA (25.7)" % ident)
                exigir(bool(img.get("como_a_dimensao_foi_medida")),
                       "%s: a imagem tem de dizer de onde a dimensao saiu — numero digitado e da "
                       "familia do numero de tela digitado (25.7)" % ident)
                exigir(bool(af.get("url_produto")),
                       "%s: imagem veio de uma oferta; sem `url_produto` ela nao tem procedencia"
                       % ident)

            for c in (r.get("cotacoes") or []):
                exigir(bool(c.get("data_leitura")),
                       "%s: cotacao sem data — a secao 7 proibe preco cravado como atual" % ident)

    return afirmacoes, falhas


# --------------------------------------------------------------- impressao e main
def imprimir(placar, linhas):
    ordem = ("casou", "barrado", "sem_identidade", "mercado_nao_anuncia", "candidato_barrado",
             "encurtamento_falhou")
    for qual in ordem:
        destas = [l for l in linhas if l[0] == qual]
        if not destas:
            continue
        print("  %s (%d):" % (qual.upper(), len(destas)))
        for _q, ident, detalhe in destas:
            print("    %-32s %s" % (ident, detalhe))
    print()
    print("  PLACAR, e as tres causas de `nao casou` saem SEPARADAS pela 25.4-b.4:")
    for k in ("casou", "mercado_nao_anuncia", "candidato_barrado", "sem_identidade_minima",
              "foto_sem_dimensao", "excluido", "ofertas_julgadas_no_total",
              "candidatos_barrados_no_total"):
        print("    %-24s %d" % (k, placar[k]))


def main():
    p = argparse.ArgumentParser(
        description="Casa a oferta da loja com o registro do banco (degraus 1 a 3 da 25.1)")
    p.add_argument("--gravar", action="store_true", help="grava no banco")
    p.add_argument("--conferir", action="store_true", help="SEM REDE: confere o que esta escrito")
    args = p.parse_args()

    dados = PISO.carregar()

    if args.conferir:
        afirmacoes, falhas = conferir(dados)
        print("coletar-oferta --conferir: %d afirmacao(oes) sobre o que esta escrito" % afirmacoes)
        for f in falhas:
            if f:
                print("  FALHA: %s" % f)
        reais = [f for f in falhas if f]
        print("REPROVADO (%d falha(s))" % len(reais) if reais else "APROVADO")
        return 1 if reais else 0

    placar, linhas = trabalhar(dados, args.gravar)
    print("coletar-oferta%s" % (" --gravar" if args.gravar else " (medindo, sem gravar)"))
    imprimir(placar, linhas)

    if not args.gravar:
        print()
        print("  NADA FOI GRAVADO. Rode com --gravar para levar isto ao banco.")
        return 0

    agora = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    for arq in ("veiculos", "pecas"):
        d = dados[arq]
        d["casamento_de_oferta_colhido_em"] = agora
        d["versao_esquema"] = dados["esquema-banco"].get("versao_esquema")
        (RAIZ / "dados" / ("%s.json" % arq)).write_text(
            json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print()
    print("  GRAVADO em dados/veiculos.json e dados/pecas.json (%s)" % agora)
    return 0


if __name__ == "__main__":
    sys.exit(main())
