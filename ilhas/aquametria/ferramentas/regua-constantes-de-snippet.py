#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGUA COMPARTILHADA: pergunta ao PHP TODA constante `AQUAMETRIA_*` dos
snippets desta ilha e varre `ferramentas/` procurando quem as redigitou.

Nao afirma nada sozinha e nao abre rede. Quem a exercita contra respostas
ENCENADAS e o `teste-constantes-de-snippet.py`; quem a mutila e o
`mutacoes-constantes-de-snippet.py`.

POR QUE ESTE ARQUIVO EXISTE, e a data e 19/10/2026
--------------------------------------------------
O achado 11 do fecho das 17h04Z desta ilha, deixado sem conserto de proposito
pela 19.2: *"esta passada mediu UMA constante compartilhada — o teto do titulo —
e nao perguntou se ha outras. Quantas OUTRAS constantes de snippet os portoes
desta pasta redigitam hoje e uma pergunta que ninguem fez, e a resposta dela
decide se generalizar a varredura vale um bloco. Quem a tomar comeca contando,
nao generalizando: generalizar regua antes de saber o tamanho do problema e
como se escreve regra que nao serve a caso nenhum."*

ELE E A CONTAGEM, E A CONTAGEM MUDOU O DESENHO DA VARREDURA
-----------------------------------------------------------
A primeira tentativa desta passada foi a obvia: varrer pelo VALOR das 66
constantes. Ela nao presta, e o motivo e medido, nao opinado:

  * **46 das 66 nao se decidem por texto.** Um `3`, um `10`, um `20`, um `45`
    nu nao se distingue de nenhum outro numero da pasta; `1.2.0` e o valor de
    DUAS constantes ao mesmo tempo (`C1_VERSAO` e `SEO_VERSAO`), entao um
    acerto nem se atribui a uma delas.
  * **Das 20 decidiveis, a varredura por valor deu 23 acertos em posicao de
    codigo e os 23 eram PROSA** — lidos um por um. Quatorze deles eram a data
    `12/09/2026`, que e o valor de `AQUAMETRIA_PEIXES_SERP_EM` e tambem a data
    que meia pasta cita contando a propria historia em cabecalho. Isso nao e
    constante redigitada: e uma frase em portugues que por acidente vale o
    mesmo que uma constante.
  * **E a `onde()` inverte os dois sentidos quando o alvo e o valor.** Para uma
    constante de texto, o redigito de verdade mora DENTRO DE ASPAS
    (`SLUG = "calculadora-de-iluminacao"`), que a `onde()` chama de `dado` e
    silencia; e a prosa de docstring mora em linha de CONTINUACAO, que nao
    comeca por marcador nenhum e por isso a `onde()` chama de `codigo` e
    denuncia. A varredura por valor erra calada no caso que importa e grita no
    que nao importa.

Entao esta regua varre pelo NOME, que e o mecanismo que ja funciona — o do
`regua-teto-do-titulo.py`, que procura `TETO = 65` e nao `65` — com o alvo
aberto para as 58 constantes que da para perguntar. A `onde()` e IMPORTADA
daquele arquivo e nao recopiada: ela foi escrita para exatamente esta pergunta
(`NOME = literal`), e nela os tres sentidos valem o que dizem.

O QUE ELA DECIDE, e cada veredito pede um grau diferente de prova
-----------------------------------------------------------------
  * `REDIGITADO` — o nome local casa com uma constante do snippet **e o valor
    tambem**. Duas provas concordando: e uma copia. Unico veredito que reprova.
  * `HOMONIMO` — o nome casa e o valor NAO. Pode ser divida que ja derivou
    (alguem copiou 45 e o snippet foi para 50) ou numero sem parentesco que por
    acaso usa o nome. A regua nao sabe qual, e dizer que sabe seria inventar:
    vira AVISO com os dois valores impressos, para quem le decidir.
  * `isento` — a linha DECLARA que a regua e propria, com o marcador
    `REGUA PROPRIA`. Silencioso.

A PROVA FRACA NAO VIRA AVISO, E ISSO E REGRA E NAO DESCUIDO
------------------------------------------------------------
O nome local candidato sai das caudas do nome da constante
(`AQUAMETRIA_C15_VITRINE_LARGURA_CM` rende `LARGURA_CM`), e cauda de UM segmento
so e prova fraca: `AQUAMETRIA_SEO_NOME_DO_SITE` rende `SITE`, e seis portoes
desta pasta escrevem `SITE = "https://aquametria.com.br"` — que nao tem
parentesco nenhum com o nome do site. Entao o grau de prova do nome decide o que
ele autoriza: **valor igual denuncia com qualquer cauda** (duas provas), e
**valor diferente so avisa quando o nome e forte** — o nome inteiro, o nome sem
o prefixo `AQUAMETRIA_`, ou cauda de dois segmentos ou mais.

A EXENCAO MORA NO ARQUIVO QUE A TOMA, NUNCA NUMA LISTA AQUI DENTRO
-------------------------------------------------------------------
Ha redigito que e CERTO, e o `teste-voz.mjs` desta pasta escreveu o principio:
*"quem confere escreve a propria regua (...) se as duas metades lessem a mesma
lista, apagar um termo faria as duas errarem juntas"*. Vale quando a autoridade
do numero e um DOCUMENTO e nao o snippet — o `VOZ.md`, ou o
`dados/constantes-calculadoras.json`, que diz de si: *"Nenhuma formula pode
citar um valor que nao esteja aqui"*. Ali o snippet e a regua sao dois copistas
do mesmo documento, e a regua ler o snippet poria o policiado escolhendo a lei.

Essa decisao e do arquivo que a toma, entao e nele que ela se declara: o
marcador `REGUA PROPRIA` na MESMA LINHA do numero, com o motivo depois. Mesmo
desenho da `bancada.py`: a pergunta e feita aos arquivos, nunca a uma lista
escrita a mao aqui, que envelheceria calada. Marcador na mesma linha e de
proposito — quem le o numero le a razao dele sem procurar.

E ELA DECLARA AS 8 QUE NAO CONSEGUE PERGUNTAR
---------------------------------------------
O carregador de bancada pula o `aquametria-sync.php` e o
`aquametria-atualizador-sync.php`, que falam com o WordPress de verdade. As 8
constantes deles ficam de fora da varredura, e a regua as devolve em
`nao_perguntadas` para o portao imprimir NAO MEDIDO em vez de zero. Zero medido
e nada medido saem iguais na tela e nao valem o mesmo.

NENHUM CAMINHO DEVOLVE UM PADRAO
--------------------------------
Resposta que falta, resposta ilegivel e resposta sem constante nenhuma levantam
`RespostaInvalida`. Um `except` com uma lista de consolo aqui dentro
reproduziria o defeito que o achado 11 descreve, escondido atras de uma regua
que parece ser a cura.
"""

import importlib.util
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PERGUNTADOR = "listar-constantes-do-snippet.php"
PREFIXO = "AQUAMETRIA_"

# A MARCA DA EXENCAO. Texto e nao expressao regular: quem a escreve tem de poder
# procura-la com um grep e achar todas.
MARCADOR_DE_EXENCAO = "REGUA PROPRIA"

# Cauda com menos caracteres que isto nao e nome: `CM`, `ID`, `EM`.
MINIMO_DO_NOME = 4

# A `onde()` vem do irmao mais velho, que a escreveu para esta mesma pergunta.
# Recopia-la aqui seria o defeito que as duas reguas existem para impedir, um
# andar acima: duas copias da mesma classificacao errando juntas.
_spec = importlib.util.spec_from_file_location(
    "regua_teto_do_titulo", os.path.join(os.path.dirname(os.path.abspath(__file__)), "regua-teto-do-titulo.py")
)
_teto = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_teto)
onde = _teto.onde

# O proprio perguntador, esta regua e a regua de onde a `onde()` vem ficam FORA
# da varredura: nenhum dos tres digita valor de constante, e os dois ultimos
# citam nomes de constante em prosa por oficio.
FORA_DA_VARREDURA = (PERGUNTADOR, "regua-constantes-de-snippet.py", "regua-teto-do-titulo.py")


class RespostaInvalida(Exception):
    """A resposta do perguntador nao presta. Nunca se traduz em valor de consolo."""


def ler_resposta(texto):
    """Recebe o TEXTO da resposta e decide se ela presta.

    Separado do `perguntar()` de proposito: e assim que a bancada encena
    resposta vazia, truncada, sem constante e com tipo errado sem precisar de um
    snippet quebrado no disco.
    """
    if not (texto or "").strip():
        raise RespostaInvalida("resposta vazia")
    try:
        dado = json.loads(texto)
    except ValueError as e:
        raise RespostaInvalida("resposta ilegivel: %s" % e)
    if not isinstance(dado, dict):
        raise RespostaInvalida("resposta nao e objeto: %r" % type(dado).__name__)
    cs = dado.get("constantes")
    if not isinstance(cs, dict) or not cs:
        raise RespostaInvalida("resposta sem constante nenhuma")
    saida = {}
    for nome, campo in cs.items():
        if not isinstance(campo, dict) or "valor" not in campo or "tipo" not in campo:
            raise RespostaInvalida("constante %s sem valor ou sem tipo" % nome)
        if not nome.startswith(PREFIXO):
            raise RespostaInvalida("constante fora do prefixo desta ilha: %s" % nome)
        saida[nome] = {"valor": campo["valor"], "tipo": campo["tipo"]}
    pulados = dado.get("snippets_pulados")
    if not isinstance(pulados, list):
        raise RespostaInvalida("resposta sem a lista de snippets pulados")
    return {"constantes": saida, "snippets_pulados": pulados, "snippets_lidos": dado.get("snippets_lidos") or []}


def perguntar(raiz=None):
    """Pergunta ao PHP e devolve as constantes mais as duas listas de snippet.

    A raiz e argumento para a bancada poder perguntar a uma COPIA da ilha com o
    `define()` trocado — que e a unica forma de provar que o valor e lido.
    """
    raiz = raiz or RAIZ
    script = os.path.join(raiz, "ferramentas", PERGUNTADOR)
    if not os.path.exists(script):
        raise RespostaInvalida("perguntador ausente: %s" % script)
    try:
        saida = subprocess.run(["php", script, raiz], capture_output=True, text=True)
    except OSError as e:
        raise RespostaInvalida("nao deu para rodar o php: %s" % e)
    if saida.returncode != 0:
        raise RespostaInvalida(
            "%s devolveu %d: %s" % (PERGUNTADOR, saida.returncode, (saida.stderr or "").strip()[:200])
        )
    return ler_resposta(saida.stdout)


def nao_perguntadas(resposta, pasta=None):
    """Os nomes que os snippets PULADOS definem — lidos do texto deles, e aqui a
    regex e legitima justamente porque o PHP nao os carrega.

    Eles nao entram na varredura. Existem para o portao dizer NAO MEDIDO.
    """
    pasta = pasta or os.path.join(RAIZ, "snippets")
    re_def = re.compile(r"define\(\s*'(" + PREFIXO + r"[A-Z0-9_]*)'")
    saida = {}
    for nome in resposta.get("snippets_pulados") or []:
        caminho = os.path.join(pasta, nome)
        try:
            with open(caminho, encoding="utf-8") as f:
                texto = f.read()
        except OSError:
            continue
        for achado in re_def.findall(texto):
            if achado not in resposta["constantes"]:
                saida[achado] = nome
    return saida


# ---------------------------------------------------------------------------
# OS NOMES LOCAIS POSSIVEIS
# ---------------------------------------------------------------------------


def nomes_locais(constante):
    """{nome_local: forca} para uma constante do snippet.

    `forca` e `forte` ou `fraca`, e e ela que decide o que o homonimo autoriza.
    Nome inteiro, nome sem o prefixo da ilha e cauda de dois segmentos ou mais
    sao prova FORTE; cauda de um segmento so e FRACA, porque `SITE` e cauda de
    `AQUAMETRIA_SEO_NOME_DO_SITE` e tambem o nome que meia pasta da ao proprio
    dominio.
    """
    curto = constante[len(PREFIXO):] if constante.startswith(PREFIXO) else constante
    saida = {}
    for forte, cand in ((True, constante), (True, curto)):
        if len(cand) >= MINIMO_DO_NOME:
            saida[cand] = "forte"
    partes = curto.split("_")
    for i in range(1, len(partes)):
        cauda = "_".join(partes[i:])
        if len(cauda) < MINIMO_DO_NOME:
            continue
        forca = "forte" if len(partes) - i >= 2 else "fraca"
        # Nome que ja entrou como forte nao e rebaixado por uma cauda.
        if saida.get(cauda) != "forte":
            saida[cauda] = forca
    return saida


def mapa_de_nomes(constantes):
    """{nome_local: [(constante, forca), ...]} para todas as constantes."""
    mapa = {}
    for c in constantes:
        for nome, forca in nomes_locais(c).items():
            mapa.setdefault(nome, []).append((c, forca))
    return mapa


# ---------------------------------------------------------------------------
# A COMPARACAO DE VALOR
# ---------------------------------------------------------------------------

RE_NUMERO = re.compile(r"^-?[0-9]+(?:\.[0-9]+)?$")


def mesmo_valor(literal, valor, tipo):
    """O literal escrito no portao vale o mesmo que a constante do snippet?

    Numero compara como numero — `40`, `40.0` e `40.00` sao o mesmo valor, e
    tratar os tres como diferentes deixaria passar o redigito mais comum. Texto
    compara como texto, sem aparar espaco: no `AQUAMETRIA_TITULO_SEPARADOR` o
    espaco dos dois lados E o valor, e apara-lo faria a regua dizer que ` – ` e
    `–` sao a mesma coisa quando a diferenca muda a conta do teto.
    """
    if literal is None:
        return False
    if tipo == "numero":
        if not RE_NUMERO.match(literal.strip()):
            return False
        try:
            return float(literal) == float(valor)
        except (TypeError, ValueError):
            return False
    return literal == ("%s" % valor)


# A atribuicao, nas tres linguagens da pasta. O grupo `nome` e o nome local e o
# grupo `valor` e o literal; a captura comeca depois de um caractere que nao e de
# nome, para o nome nao casar no meio de outro (`TETO` dentro de `SUBTETO`).
RE_ATRIBUICAO = re.compile(
    r"(?:^|[^0-9A-Za-z_$])(?P<nome>[A-Z][A-Z0-9_]{2,})\s*=\s*"
    r"(?P<valor>-?[0-9]+(?:\.[0-9]+)?|'[^']*'|\"[^\"]*\")"
)


def literal_de(bruto):
    """O valor escrito, sem as aspas se houver."""
    if len(bruto) >= 2 and bruto[0] == bruto[-1] and bruto[0] in ("'", '"'):
        return bruto[1:-1]
    return bruto


def varrer(arquivos, constantes, fora=FORA_DA_VARREDURA):
    """Recebe {nome: texto} e as constantes como DADO; devolve (denuncias, avisos).

    Cada achado e um dicionario com arquivo, linha, nome local, constante,
    valores e o veredito. `denuncias` vazia e o unico resultado que o portao
    aceita; `avisos` ele imprime e nao reprova.
    """
    mapa = mapa_de_nomes(constantes)
    denuncias = []
    avisos = []
    for arquivo in sorted(arquivos):
        if arquivo in fora:
            continue
        for n, linha in enumerate((arquivos[arquivo] or "").split("\n"), 1):
            for m in RE_ATRIBUICAO.finditer(linha):
                nome = m.group("nome")
                if nome not in mapa:
                    continue
                trecho = linha[m.start("nome"):m.end("valor")]
                posicao = onde(linha, trecho)
                if posicao == "dado":
                    continue
                if MARCADOR_DE_EXENCAO in linha:
                    # A linha DECLARA que a regua e propria. Silencioso, e a
                    # razao fica escrita ao lado do numero para quem o ler.
                    continue
                literal = literal_de(m.group("valor"))
                for constante, forca in sorted(mapa[nome]):
                    campo = constantes[constante]
                    igual = mesmo_valor(literal, campo["valor"], campo["tipo"])
                    if igual:
                        veredito = "REDIGITADO"
                    elif forca == "forte":
                        veredito = "HOMONIMO"
                    else:
                        # Prova fraca e valor diferente: nao e achado nenhum.
                        continue
                    achado = {
                        "arquivo": arquivo,
                        "linha": n,
                        "nome": nome,
                        "constante": constante,
                        "literal": literal,
                        "valor": campo["valor"],
                        "posicao": posicao,
                        "veredito": veredito,
                        "texto": linha.strip()[:110],
                    }
                    if veredito == "REDIGITADO" and posicao == "codigo":
                        denuncias.append(achado)
                    else:
                        avisos.append(achado)
    return denuncias, avisos


def ler_pasta(pasta=None):
    """{nome: texto} de todo .py, .mjs e .php de `ferramentas/`. Le o disco; a
    decisao e da `varrer()`, que recebe dado."""
    pasta = pasta or os.path.join(RAIZ, "ferramentas")
    saida = {}
    for nome in sorted(os.listdir(pasta)):
        if not nome.endswith((".py", ".mjs", ".php")):
            continue
        try:
            with open(os.path.join(pasta, nome), encoding="utf-8") as f:
                saida[nome] = f.read()
        except OSError:
            continue
    return saida


if __name__ == "__main__":
    # `--constante NOME` imprime SO o valor, e existe para quem nao fala PHP
    # nem Python — os `.mjs` desta pasta. E o mesmo caminho do
    # `regua-teto-do-titulo.py --teto`, e o motivo de passar pela regua em vez
    # de chamar o PHP direto e o mesmo: uma autoridade para o valor.
    #
    # E ELE NAO DECLARA FAIXA, AO CONTRARIO DO IRMAO, E A DIFERENCA E DE
    # NATUREZA. Lá o valor e um LIMITE — um teto de `<title>` — e ler o limite
    # de quem e limitado deixaria o snippet alargar o portao em silencio, por
    # isso a banda. Aqui o valor e o CASO SERVIDO: qual aquario de referencia a
    # pagina publica. Se o snippet trocar o caso, a pagina troca, e o portao
    # TEM de seguir — seguir e a medicao certa. Caso nao se desconfia; limite,
    # sim.
    if "--constante" in sys.argv[1:]:
        try:
            qual = sys.argv[sys.argv.index("--constante") + 1]
        except IndexError:
            print("FALHA: --constante pede o nome da constante", file=sys.stderr)
            raise SystemExit(2)
        cs = perguntar()["constantes"]
        if qual not in cs:
            print(
                "FALHA: %s nao foi definida pelos snippets que a bancada carrega "
                "(as do aquametria-sync.php e do aquametria-atualizador-sync.php nao sao perguntaveis)" % qual,
                file=sys.stderr,
            )
            raise SystemExit(1)
        print(cs[qual]["valor"])
        raise SystemExit(0)

    resposta = perguntar()
    constantes = resposta["constantes"]
    fora = nao_perguntadas(resposta)
    denuncias, avisos = varrer(ler_pasta(), constantes)

    print("%d constantes perguntadas ao PHP, em %d snippets." % (len(constantes), len(resposta["snippets_lidos"])))
    print(
        "%d NAO MEDIDAS (nao zero): os snippets %s falam com o WordPress e a bancada nao os carrega."
        % (len(fora), ", ".join(sorted(set(fora.values()))) or "—")
    )
    for nome in sorted(fora):
        print("    nao medida  %s  (%s)" % (nome, fora[nome]))
    print("%d denuncia(s), %d aviso(s)." % (len(denuncias), len(avisos)))
    for d in denuncias:
        print(
            "DENUNCIA  %s:%d  %s = %r  — redigita %s"
            % (d["arquivo"], d["linha"], d["nome"], d["literal"], d["constante"])
        )
    for a in avisos:
        print(
            "aviso     %s:%d  %s = %r  — %s vale %r (%s%s)"
            % (
                a["arquivo"],
                a["linha"],
                a["nome"],
                a["literal"],
                a["constante"],
                a["valor"],
                a["veredito"].lower(),
                ", em prosa" if a["posicao"] == "prosa" else "",
            )
        )
    raise SystemExit(1 if denuncias else 0)
