#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AS MUTACOES DO PORTAO DO TITULO SERVIDO NO AR.

    python3 ferramentas/mutacoes-titulo-no-ar.py

Sem rede. Codigo de saida 0 se NENHUMA mutacao sobreviver, 1 se alguma passar.

O QUE ELAS PROVAM, e por que o `teste-titulo-no-ar.py` nao basta sozinho: um
portao verde prova que o mundo de hoje passa, nunca que o portao MORDE. Cada
mutacao daqui quebra uma afirmacao de proposito, numa ILHA DE SOMBRA (copia de
`ferramentas/` num diretorio temporario — o repositorio de verdade nunca e
tocado), e exige TRES coisas:

  1. que o arquivo mude de verdade (mutacao que nao encontra o alvo e INERTE, e
     aparece nomeada em vez de contar como sucesso);
  2. que o teste saia com codigo 1;
  3. que ele reprove PELA FRASE que a mutacao espera ouvir de volta.

A (3) e a licao de 15/10/2026 desta ilha: reprovar nao e a mesma coisa que
reprovar PELO MOTIVO CERTO — sem a frase, uma mutacao pode disparar outra trava,
voltar verde e nunca ter medido a sua.

E DOIS MUNDOS TEM DE PASSAR, porque bateria que so sabe reprovar nao distingue
"o portao morde" de "o portao morde tudo".

AS DUAS MUTACOES QUE MAIS IMPORTAM AQUI
---------------------------------------
  * a que troca a comparacao PAGINA POR PAGINA pela comparacao por TOTAL. E a
    volta ao desenho que esta ilha ja viu falhar duas vezes — na serie da
    deriva em 16/10/2026 e na do cano em 19/10 — e ela tem de reprovar pelo
    caso da TROCA de titulos, nao pelo mundo de hoje.
  * a que desliga a DECODIFICACAO das entidades. Ela e silenciosa do pior jeito:
    o portao continua verde, so passa a medir o teto de 65 sobre a fonte em vez
    da tela, e `&#8211;` sozinho custa 6 caracteres de erro por titulo.
"""
import io
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REGUA = os.path.join("ferramentas", "regua-titulo-no-ar.py")
PORTAO = os.path.join("ferramentas", "conferir-titulo-no-ar.py")
TESTE = os.path.join("ferramentas", "teste-titulo-no-ar.py")

inertes = []
sobreviventes = []
sem_frase = []
feitas = 0


def ilha_de_sombra():
    tmp = tempfile.mkdtemp(prefix="aqm-mut-titulo-ar-")
    shutil.copytree(os.path.join(RAIZ, "ferramentas"), os.path.join(tmp, "ferramentas"),
                    ignore=shutil.ignore_patterns("__pycache__"))
    return tmp


def troca_em(ilha, arquivo, velho, novo):
    """Troca exata, e devolve False se o alvo nao estava la — e isso e INERTE.

    `str.replace` cru de alvo sumido NAO falha: ele devolve o mesmo texto e a
    mutacao vira verde sobre nada. Foi assim que quatro mutacoes de
    `mutacoes-escada.py` morreram caladas em 23/09/2026.
    """
    caminho = os.path.join(ilha, arquivo)
    texto = io.open(caminho, encoding="utf-8").read()
    if velho not in texto:
        return False
    with io.open(caminho, "w", encoding="utf-8") as f:
        f.write(texto.replace(velho, novo, 1))
    return True


def rodar_teste(ilha):
    p = subprocess.Popen([sys.executable, os.path.join(ilha, TESTE)],
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    saida = p.communicate()[0].decode("utf-8", "replace")
    return p.returncode, saida


def mutacao(rotulo, aplicar, frase):
    global feitas
    feitas += 1
    ilha = ilha_de_sombra()
    try:
        if not aplicar(ilha):
            print("  INERTE  %s — o alvo nao estava no arquivo" % rotulo)
            inertes.append(rotulo)
            return
        codigo, saida = rodar_teste(ilha)
        if codigo == 0:
            print("  SOBREVIVEU  %s" % rotulo)
            sobreviventes.append(rotulo)
            return
        if frase not in saida:
            print("  SEM A FRASE  %s — esperava ouvir %r" % (rotulo, frase))
            sem_frase.append(rotulo)
            return
        print("  ok  %s" % rotulo)
    finally:
        shutil.rmtree(ilha, ignore_errors=True)


def mundo_que_passa(rotulo, aplicar):
    global feitas
    feitas += 1
    ilha = ilha_de_sombra()
    try:
        if aplicar is not None and not aplicar(ilha):
            print("  INERTE  %s — o alvo nao estava no arquivo" % rotulo)
            inertes.append(rotulo)
            return
        codigo, saida = rodar_teste(ilha)
        if codigo != 0:
            print("  REPROVOU MUNDO BOM  %s" % rotulo)
            sobreviventes.append(rotulo)
            return
        print("  ok  %s" % rotulo)
    finally:
        shutil.rmtree(ilha, ignore_errors=True)


def main():
    print("MUTACOES DO PORTAO DO TITULO SERVIDO NO AR — ilha de sombra, sem rede\n")

    # ---------------------------------------------------------- A LEITURA
    mutacao(
        "1. a decodificacao de entidade sai — o teto passa a ser medido na FONTE",
        lambda i: troca_em(i, REGUA,
                           'return re.sub(r"\\s+", " ", _html.unescape(bruto or "")).strip()',
                           'return re.sub(r"\\s+", " ", (bruto or "")).strip()'),
        "e o tamanho medido e o da TELA")

    mutacao(
        "2. `<title>` com atributo deixa de casar",
        lambda i: troca_em(i, REGUA,
                           'r"<title[^>]*>([\\s\\S]*?)</title>"',
                           'r"<title>([\\s\\S]*?)</title>"'),
        "le o <title> com atributo na tag")

    mutacao(
        "3. a meta description so casa com aspas duplas",
        lambda i: troca_em(i, REGUA,
                           'r"<meta\\s+name=[\\"\']description[\\"\']\\s+content=[\\"\']([\\s\\S]*?)[\\"\']\\s*/?>"',
                           'r\'<meta\\s+name="description"\\s+content="([\\s\\S]*?)"\\s*/?>\''),
        "le a meta description com aspas simples")

    mutacao(
        "4. o espaco deixa de ser normalizado — quebra de linha no titulo conta duas vezes",
        lambda i: troca_em(i, REGUA,
                           'return re.sub(r"\\s+", " ", _html.unescape(bruto or "")).strip()',
                           'return _html.unescape(bruto or "").strip()'),
        "quebra de linha dentro do <title> nao duplica espaco")

    mutacao(
        "5. o slug passa a ser o PRIMEIRO degrau do caminho, nao o ultimo",
        lambda i: troca_em(i, REGUA,
                           "return partes[-1] if partes else \"\"",
                           "return partes[0] if partes else \"\""),
        "o slug e o ultimo degrau do caminho")

    mutacao(
        "6. a quebra de cache deixa de ser tirada do slug",
        lambda i: troca_em(i, REGUA,
                           'caminho = re.sub(r"^https?://[^/]+", "", (url or "").split("?")[0])',
                           'caminho = re.sub(r"^https?://[^/]+", "", (url or ""))'),
        "a quebra de cache nao entra no slug")

    # ---------------------------------------------------------- A PROMESSA
    mutacao(
        "7. promessa de SO ESPACO passa a contar como promessa declarada",
        lambda i: troca_em(i, REGUA, "if p.strip():", "if p:"),
        "promessa so de espaco nao conta como promessa")

    mutacao(
        "8. a promessa deixa de ser procurada no titulo — `promessa_chegou` sempre diz sim",
        lambda i: troca_em(i, REGUA,
                           'return promessa in (estado_servido or {}).get("titulo", "")',
                           "return True"),
        "promessa que NAO chegou e pega")

    mutacao(
        "9. a promessa passa a casar pelo PREFIXO — promessa truncada no ar vira chegada",
        lambda i: troca_em(i, REGUA,
                           'return promessa in (estado_servido or {}).get("titulo", "")',
                           'return promessa[:10] in (estado_servido or {}).get("titulo", "")'),
        "promessa truncada nao passa por chegada")

    # ---------------------------------------------------------- O CONTROLE
    mutacao(
        "10. o controle deixa de ser conferido: `sem_promessa` sempre diz que esta intacto",
        lambda i: troca_em(i, REGUA,
                           'return not (estado_servido or {}).get("digito", False)',
                           "return True"),
        "controle PERDIDO e pego")

    mutacao(
        "11. `digito` deixa de ver algarismo — o controle fica cego pelo outro lado",
        lambda i: troca_em(i, REGUA,
                           '"digito": any(c.isdigit() for c in t),',
                           '"digito": False,'),
        "controle PERDIDO e pego")

    # ------------------------------------------------------- O VERDE VAZIO
    mutacao(
        "12. `titulo_mais_longo` sobre nada passa a explodir em vez de devolver 0",
        lambda i: troca_em(i, REGUA,
                           '"titulo_mais_longo": max([e["n"] for e in itens.values()] or [0]),',
                           '"titulo_mais_longo": max([e["n"] for e in itens.values()]),'),
        "titulo_mais_longo sobre nada e 0")

    mutacao(
        "13. o teto deixa de morder a fronteira: 66 passa a ser aceito",
        lambda i: troca_em(i, REGUA,
                           'return sorted(u for u, e in (medido or {}).items() if e["n"] > teto)',
                           'return sorted(u for u, e in (medido or {}).items() if e["n"] > teto + 1)'),
        "titulo de 66 esta acima do teto")

    mutacao(
        "14. o portao deixa de exigir URL do sitemap — verde vazio passa",
        lambda i: troca_em(i, PORTAO,
                           'ok("o sitemap trouxe URL (verde vazio nao passa por aprovado)",\n'
                           '       len(urls) > 0, "%d URL(s)" % len(urls))',
                           'ok("o sitemap trouxe URL (verde vazio nao passa por aprovado)",\n'
                           '       True, "%d URL(s)" % len(urls))'),
        "sitemap sem URL nenhuma REPROVA em vez de aprovar vazio")

    # ------------------------------------- A COMPARACAO PAGINA POR PAGINA
    mutacao(
        "15. A COMPARACAO POR TOTAL volta: a troca de titulos entre duas paginas fica verde",
        lambda i: troca_em(i, REGUA,
                           '''    mudadas = []
    for url in sorted(set(medido) & set(esperado)):
        if medido[url] == esperado[url]:
            continue
        mudadas.append("%s: %s" % (url, quais_campos(medido[url], esperado[url])))
    return (novas, sumidas, mudadas)''',
                           '''    mudadas = []
    if totais(medido) != totais(esperado):
        mudadas.append("os totais divergem")
    return (novas, sumidas, mudadas)'''),
        "e a comparacao pagina por pagina acusa AS DUAS")

    mutacao(
        "16. a descricao sai da comparacao — meta trocada em silencio fica verde",
        lambda i: troca_em(i, REGUA,
                           'for campo in ("titulo", "descricao", "n", "descricao_n", "digito"):',
                           'for campo in ("titulo", "n", "digito"):')
        and troca_em(i, REGUA,
                     "        if medido[url] == esperado[url]:\n            continue",
                     '        if medido[url].get("titulo") == (esperado[url] or {}).get("titulo"):\n            continue'),
        "descricao trocada com titulo igual TAMBEM e divergencia")

    mutacao(
        "17. a frase da divergencia deixa de nomear o campo",
        lambda i: troca_em(i, REGUA,
                           'partes.append("%s servido %r contra declarado %r" % (campo, a, b))',
                           'partes.append("servido %r contra declarado %r" % (a, b))'),
        "e nomeia QUAL campo divergiu")

    mutacao(
        "18. declaracao AUSENTE passa a ser lida como mundo vazio, nao como ausencia",
        lambda i: troca_em(i, REGUA,
                           '        return (["a serie nao tem declaracao nenhuma"], [], [])',
                           "        return ([], [], [])"),
        "declaracao ausente nao e tratada como zero")

    mutacao(
        "19. a serie passa a ser lida do ULTIMO bloco json, nao do primeiro",
        lambda i: troca_em(i, REGUA,
                           '            if linha.strip() == "```":\n                break',
                           '            if linha.strip() == "```":\n                dentro = False\n                continue'),
        "com a serie gravada o portao APROVA")

    mutacao(
        "20. o portao para de cobrar que o total declarado feche com as paginas declaradas",
        lambda i: troca_em(i, PORTAO,
                           'declarado.get("totais") == regua.totais(declarado.get("paginas", {})),',
                           "True,"),
        "declaracao cujo total nao fecha com as paginas dela reprova")

    mutacao(
        "21. o portao deixa de exigir a resposta do listar-promessas.php",
        lambda i: troca_em(i, PORTAO,
                           '       mapa is not None, erro.strip()[:200])',
                           '       True, erro.strip()[:200])'),
        "PROMESSA QUE NAO DESEMBARCOU reprova")

    # ------------------------------------------------- OS MUNDOS QUE PASSAM
    mundo_que_passa("M1. o mundo de hoje, sem mutacao nenhuma", None)
    mundo_que_passa(
        "M2. comentario novo na regua nao muda veredito",
        lambda i: troca_em(i, REGUA, "import html as _html",
                           "# um comentario que nao muda nada\nimport html as _html"))

    print("")
    print("%d mutacao(oes) aplicada(s)" % feitas)
    if inertes:
        print("INERTES (%d) — nao mediram nada:" % len(inertes))
        for r in inertes:
            print("  - %s" % r)
    if sem_frase:
        print("SEM A FRASE (%d) — reprovaram, mas nao pelo motivo esperado:" % len(sem_frase))
        for r in sem_frase:
            print("  - %s" % r)
    if sobreviventes:
        print("SOBREVIVENTES (%d):" % len(sobreviventes))
        for r in sobreviventes:
            print("  - %s" % r)
    if inertes or sem_frase or sobreviventes:
        return 1
    print("NENHUMA SOBREVIVEU, NENHUMA INERTE, NENHUMA SEM A FRASE.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
