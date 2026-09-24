#!/usr/bin/env python3
"""BANCADA: sem rede — mede a REGUA de `noindex`, nao o site.

    python3 ferramentas/teste-robots.py

A regua mora em `ferramentas/regua-robots.py` e o cabecalho dela conta por que
ela existe: em 23/09/2026 um item de despacho acusou `/author/aquametria_gestor/`
de estar sem `noindex` porque mediu com `name="robots"`, de aspas DUPLAS, numa
ilha em que quem imprime a tag e o nucleo do WordPress, de aspas SIMPLES. A
pagina estava certa desde 10/09.

ESTE ARQUIVO E A PROVA DE QUE A REGUA NOVA NAO REPETE O ERRO NEM INVENTA OUTRO.
Cada caso abaixo e um HTML escrito a mao com o veredito esperado ao lado, e as
duas direcoes sao cobradas: os casos VERDES sao paginas que realmente mandam nao
indexar, os VERMELHOS sao paginas que nao mandam. Uma regua que dissesse "sim"
para tudo passaria na metade de cima e e por isso que a de baixo existe.

O CASO 1 E O DEFEITO DE 23/09 EM PESSOA: se algum dia esta regua voltar a ler so
aspas duplas, ele fica vermelho aqui, na bancada, em um segundo — e nao num
despacho que manda consertar o que nao esta quebrado.
"""
import importlib.util
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def carregar(nome):
    caminho = os.path.join(RAIZ, "ferramentas", nome)
    spec = importlib.util.spec_from_file_location(nome.replace("-", "_")[:-3], caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


regua = carregar("regua-robots.py")

contadas = [0]
falhas = []


def ok(nome, cond, extra=""):
    contadas[0] += 1
    print("  %s %s%s" % ("ok   " if cond else "FALHA", nome, (" — " + extra) if extra else ""))
    if not cond:
        falhas.append(nome)


# ---------------------------------------------------------------------------
# METADE DE CIMA: paginas que MANDAM nao indexar. A regua tem de dizer sim.
# ---------------------------------------------------------------------------
MANDAM = [
    ("1. aspa SIMPLES, exatamente o que o nucleo do WordPress imprime nesta ilha "
     "(o caso que o despacho de 23/09 leu como ausencia)",
     "<meta name='robots' content='noindex, follow' />"),
    ("2. aspa DUPLA, que e como as ilhas irmas imprimem pelo snippet",
     '<meta name="robots" content="noindex,follow">'),
    ("3. sem aspa nenhuma, que o HTML permite",
     "<meta name=robots content=noindex>"),
    ("4. atributos na ordem trocada",
     "<meta content='noindex, follow' name='robots'>"),
    ("5. NAME com caixa alta, que o HTML nao distingue",
     "<META NAME='ROBOTS' CONTENT='NOINDEX, FOLLOW'>"),
    ("6. noindex no meio de uma lista de diretivas",
     "<meta name='robots' content='follow, noindex, max-snippet:-1'>"),
    ("7. duas metas robots e so a segunda com noindex — o Google resolve pelo "
     "lado restritivo, e a regua tem de ver a segunda",
     "<meta name='robots' content='follow'><meta name='robots' content='noindex'>"),
]
print("PAGINAS QUE MANDAM NAO INDEXAR (a regua diz sim):")
for rotulo, html in MANDAM:
    ok(rotulo, regua.tem_noindex(html))

# ---------------------------------------------------------------------------
# METADE DE BAIXO: paginas que NAO mandam. A regua tem de dizer nao.
#
# Esta metade e a que impede o conserto errado. O item de despacho de 23/09
# mandava ACRESCENTAR noindex; se a regua dissesse sim para tudo, ela aprovaria
# a pagina indexavel que perdeu o indice por engano — que e o defeito oposto e,
# nas 52 URLs do sitemap desta ilha, o caro.
# ---------------------------------------------------------------------------
NAO_MANDAM = [
    ("8. a home desta ilha, que serve robots SEM noindex",
     "<meta name='robots' content='max-image-preview:large' />"),
    ("9. nenhuma meta robots na pagina",
     "<html><head><title>x</title></head><body>noindex</body></html>"),
    ("10. a palavra noindex no CORPO da pagina, longe de qualquer meta",
     "<p>Esta pagina explica o que noindex faz.</p>"),
    ("11. a palavra noindex dentro de um <script>, na mesma linha de robots — "
     "o caso que um grep de linha aceitaria",
     "<script>var robots = {noindex: false};</script>"),
    ("12. meta de OUTRO nome carregando noindex",
     "<meta name='googlebot-news' content='noindex'>"),
    ("13. content vazio, que e o que sobra quando o filtro esvazia o mapa",
     "<meta name='robots' content=''>"),
    ("14. `noindexar`, que contem a palavra e nao e a diretiva",
     "<meta name='robots' content='noindexar'>"),
    ("15. um comentario HTML citando a tag inteira",
     "<!-- <meta name='robots' content='noindex, follow' /> -->"),
    ("16. a tag inteira dentro de um <script>, como texto",
     "<script>var t = \"<meta name='robots' content='noindex'>\";</script>"),
    ("17. a tag inteira dentro de um comentario DENTRO de um <script>",
     "<script>/* <meta name=robots content=noindex> */</script>"),
]
print("\nPAGINAS QUE NAO MANDAM (a regua diz nao):")
for rotulo, html in NAO_MANDAM:
    ok(rotulo, not regua.tem_noindex(html))

# ---------------------------------------------------------------------------
# A CONTAGEM, que e a terceira pergunta e a que o `grep -c` fingia responder.
# ---------------------------------------------------------------------------
print("\nA CONTAGEM DE METAS ROBOTS:")
ok("a home serve UMA meta robots",
   1 == regua.quantas_metas_de_robots("<meta name='robots' content='max-image-preview:large' />"))
ok("pagina sem a tag serve ZERO",
   0 == regua.quantas_metas_de_robots("<html><head></head></html>"))
ok("meta duplicada e contada como DUAS, nao como uma",
   2 == regua.quantas_metas_de_robots(
       "<meta name='robots' content='noindex'><meta name=\"robots\" content=\"follow\">"))
ok("o comentario HTML nao entra na contagem",
   0 == regua.quantas_metas_de_robots("<!-- <meta name='robots' content='noindex'> -->"))

print("\n%d afirmacoes, %d falha(s)" % (contadas[0], len(falhas)))
for f in falhas:
    print("  FALHOU: %s" % f)
sys.exit(1 if falhas else 0)
