#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGUA COMPARTILHADA: mede a DERIVA entre o snippet do repositorio e o que o
gerador de catalogo produz do banco de hoje — sem NUNCA escrever no snippet.

Nao afirma nada sozinha. Quem afirma e `conferir-deriva-do-catalogo.py`
(bancada, sem rede) e quem a exercita contra mundos encenados e
`teste-deriva-do-catalogo.py`. Ela mora num arquivo so porque a medicao tem um
passo PERIGOSO no meio — rodar o gerador — e escrita duas vezes um dos lados
esqueceria a sombra. (Secao 8 do ARQUIPELAGO.md, e a fronteira dela: isto e
DECISAO, entao o portao confere; o jeito de medir mora num arquivo so.)

POR QUE A SOMBRA, e ela e a razao de este arquivo existir
---------------------------------------------------------
`gerar-catalogo-especies.py` reescreve `snippets/aquametria-peixes.php` NO
LUGAR. Para saber quanto o snippet do `main` difere do banco de hoje, as
execucoes de 15/10 e 16/10/2026 rodaram o gerador contra o arquivo de verdade e
o restauraram "byte a byte" DEPOIS — tres vezes em tres passadas, cada uma com
a superficie da ilha congelada pela leitura semanal de 14/10. Medicao com passo
destrutivo no meio so e segura enquanto ninguem erra o restauro, e o restauro
era um ato de memoria.

Esta regua faz o contrario: monta uma RAIZ DE SOMBRA num diretorio temporario
(os dois JSON que o gerador le e uma COPIA do snippet), roda o gerador contra
ela — o gerador recebe a raiz em `sys.argv[1]`, e e por isso que isto e
possivel sem tocar numa linha dele — e compara. O snippet de verdade e lido,
nunca aberto para escrita, e o portao AFIRMA o sha256 dele antes e depois.

O QUE E DERIVA LEGITIMA E O QUE NAO E
--------------------------------------
Deriva legitima e valor de banco que ainda nao desembarcou: ela mora DENTRO dos
dois blocos que o gerador escreve (CATALOGO e BARRADOS) e desembarca junto com
a primeira leva que regerar o catalogo. Linha de deriva FORA desses dois blocos
nunca e legitima: quer dizer que o gerador mexe em parte do arquivo que nao e
dele, ou que o snippet foi editado a mao onde so o gerador escreve.
"""
import difflib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

BLOCOS = (
    ("catalogo", "CATALOGO-INICIO", "CATALOGO-FIM"),
    ("barrados", "BARRADOS-INICIO", "BARRADOS-FIM"),
)


def caminhos(raiz):
    return {
        "banco": os.path.join(raiz, "dados", "especies-agua-doce.json"),
        "esquema": os.path.join(raiz, "dados", "esquema-especies.json"),
        "snippet": os.path.join(raiz, "snippets", "aquametria-peixes.php"),
        "gerador": os.path.join(raiz, "ferramentas", "gerar-catalogo-especies.py"),
    }


def ler(caminho):
    with io.open(caminho, encoding="utf-8") as f:
        return f.read()


def limites_dos_blocos(texto):
    """{nome: (primeira_linha, ultima_linha)} em indice 0, pelos marcadores."""
    linhas = texto.split("\n")
    achados = {}
    for nome, abre, fecha in BLOCOS:
        i = j = None
        for n, linha in enumerate(linhas):
            if abre in linha and i is None:
                i = n
            elif fecha in linha and i is not None and j is None:
                j = n
        if i is None or j is None:
            continue
        achados[nome] = (i, j)
    return achados


def bloco_da_linha(limites, n, lado="+"):
    """Em que bloco do gerador cai a mudanca ancorada na linha `n` do ANTES.

    OS DOIS LADOS NAO SE MEDEM COM A MESMA FRONTEIRA, e isto nao e detalhe: foi
    o `teste-deriva-do-catalogo.py` que reprovou a primeira versao desta funcao,
    que usava `i <= n <= j` para os dois. Linha ACRESCENTADA entra ANTES de
    `a[n]`, entao com `n` igual a linha do marcador de abertura ela nasce FORA
    do bloco — e a primeira versao a chamava de dentro, o que apagaria a unica
    deriva que nunca e legitima. Linha REMOVIDA e a propria `a[n]`, e os dois
    marcadores nao sao conteudo gerado: remover um deles e deriva de fora.
    """
    for nome, (i, j) in limites.items():
        dentro = (i < n <= j) if lado == "+" else (i < n < j)
        if dentro:
            return nome
    return None


def gerar_na_sombra(raiz, banco_texto=None, esquema_texto=None, snippet_texto=None):
    """Roda o gerador numa raiz de sombra. Devolve (php_gerado, saida, codigo).

    Os tres `*_texto` existem para o teste encenar mundo que o banco de hoje nao
    tem; em uso normal os tres sao None e a sombra copia o que esta no disco.
    """
    c = caminhos(raiz)
    sombra = tempfile.mkdtemp(prefix="deriva-catalogo-")
    try:
        os.makedirs(os.path.join(sombra, "dados"))
        os.makedirs(os.path.join(sombra, "snippets"))
        alvos = (
            ("banco", os.path.join(sombra, "dados", "especies-agua-doce.json"), banco_texto),
            ("esquema", os.path.join(sombra, "dados", "esquema-especies.json"), esquema_texto),
            ("snippet", os.path.join(sombra, "snippets", "aquametria-peixes.php"), snippet_texto),
        )
        for chave, destino, texto in alvos:
            if texto is None:
                shutil.copyfile(c[chave], destino)
            else:
                with io.open(destino, "w", encoding="utf-8") as f:
                    f.write(texto)
        p = subprocess.Popen(
            [sys.executable, c["gerador"], sombra],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        saida = p.communicate()[0].decode("utf-8", "replace")
        php = ler(os.path.join(sombra, "snippets", "aquametria-peixes.php"))
        return php, saida, p.returncode
    finally:
        shutil.rmtree(sombra, ignore_errors=True)


def diferencas(antes, depois):
    """As linhas que mudam, com o lado e a linha do ARQUIVO ANTES.

    Devolve lista de dicts: {'lado': '+'|'-', 'linha': texto, 'ancora': n}.
    `ancora` e o numero de linha do arquivo ANTES em que a mudanca se da — e por
    ela que se descobre em que bloco a deriva cai, porque e o arquivo antes que
    tem os marcadores no lugar onde o portao os conferiu.
    """
    a = antes.split("\n")
    b = depois.split("\n")
    saida = []
    for grupo in difflib.SequenceMatcher(None, a, b).get_opcodes():
        tag, i1, i2, j1, j2 = grupo
        if tag in ("replace", "delete"):
            for n in range(i1, i2):
                saida.append({"lado": "-", "linha": a[n], "ancora": n})
        if tag in ("replace", "insert"):
            for n in range(j1, j2):
                saida.append({"lado": "+", "linha": b[n], "ancora": min(i1, len(a) - 1)})
    return saida


def medir_textos(antes, depois):
    """A metade ARITMETICA da medicao, sobre dois textos — e e por aqui que o
    teste encena mundo que o banco de hoje nao tem, sem precisar de gerador."""
    limites = limites_dos_blocos(antes)
    mudancas = diferencas(antes, depois)
    for m in mudancas:
        m["bloco"] = bloco_da_linha(limites, m["ancora"], m["lado"])
    return {
        "mudancas": mudancas,
        "blocos_achados": sorted(limites),
        "fora_de_bloco": [m for m in mudancas if m["bloco"] is None],
    }


def medir(raiz, **encenado):
    """A medicao inteira. LE o snippet de verdade e NUNCA o abre para escrita:
    o gerador so recebe a raiz de sombra, e quem afirma isso e o portao."""
    c = caminhos(raiz)
    antes = ler(c["snippet"])
    depois, saida, codigo = gerar_na_sombra(raiz, **encenado)
    medicao = medir_textos(antes, depois)
    medicao["gerador_codigo"] = codigo
    medicao["gerador_saida"] = saida
    return medicao


def assinatura(mudancas):
    """A deriva como CONJUNTO CONTADO de linhas, nao como um numero.

    74 linhas podem virar 74 OUTRAS linhas sem o total mudar, e aí um portao que
    guardasse so o total ficaria verde sobre a troca.
    """
    contagem = {}
    for m in mudancas:
        chave = m["lado"] + m["linha"]
        contagem[chave] = contagem.get(chave, 0) + 1
    return contagem


def agrupada_por_causa(mudancas):
    """Agrupa pela linha, do mais repetido para o menos — e o que a execucao le."""
    contagem = assinatura(mudancas)
    return sorted(contagem.items(), key=lambda par: (-par[1], par[0]))


MARCA = re.compile(r"^```json\s*$")


def declaracao(caminho):
    """Le a declaracao mais NOVA da serie: o 1o bloco ```json do arquivo.

    A serie cresce por cima (secao nova no topo), como o `dados/posicoes.md`
    desta ilha. Arquivo ausente devolve None, que o portao trata como
    "deriva nao declarada" — e nao como zero.
    """
    if not os.path.exists(caminho):
        return None
    dentro, buf = False, []
    for linha in ler(caminho).split("\n"):
        if not dentro and MARCA.match(linha):
            dentro = True
            continue
        if dentro:
            if linha.strip() == "```":
                break
            buf.append(linha)
    if not buf:
        return None
    return json.loads("\n".join(buf))


def comparar_com_declaracao(mudancas, declarado):
    """O que a medicao tem e a declaracao nao, e o contrario. Listas de frases."""
    medido = assinatura(mudancas)
    if declarado is None:
        return (["a serie nao tem declaracao nenhuma"], [])
    esperado = declarado.get("linhas", {})
    a_mais, a_menos = [], []
    for chave in sorted(set(medido) | set(esperado)):
        m, e = medido.get(chave, 0), esperado.get(chave, 0)
        if m == e:
            continue
        frase = "%d medida(s) contra %d declarada(s): %s" % (m, e, chave)
        (a_mais if m > e else a_menos).append(frase)
    return (a_mais, a_menos)
