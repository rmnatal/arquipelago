#!/usr/bin/env python3
"""AS MUTACOES DO PORTAO DA PRIVACIDADE — e elas PRODUZEM O MUNDO, porque o
mundo que interessa aqui ainda nao existe no ar.

    python3 ferramentas/mutacoes-privacidade.py .

POR QUE ESTA BATERIA E DIFERENTE DAS OUTRAS DESTA ILHA. As outras quebram um
arquivo do repositorio e exigem que o portao reprove. Esta nao pode: o que
`conferir-privacidade-no-ar.py` mede e o AR, e o ar nao se edita daqui. Se a
bateria parasse nisso, a regua ficaria como a seção 8 do contrato descreve em
13/09/2026 — uma regua escrita para um mundo que nunca aconteceu, verde desde
sempre e SEM NUNCA TER PODIDO FALHAR. Verde sobre um mundo de um elemento so nao
e medicao; e ausencia de contraexemplo confundida com prova.

A saida e a mesma que o contrato manda: **criar o caso que nao existe.** O juizo
do portao nao mora na rede, mora em quatro funcoes puras — quem e terceiro, o que
carrega sozinho contra o que so e contatado no clique, o que conta como endereco
dito em prosa, e onde termina o corpo da pagina. Cada mutacao abaixo monta uma
pagina que o site de hoje nao serve e cobra a decisao certa sobre ela. A rede e
encanamento; isto e a regua.

AS PORTAS DOS FUNDOS QUE ESTA BATERIA FECHA, e cada uma ja custou caro nesta
fabrica com outra roupa:

  * **O endereco citado dentro de um <script>.** Se o extrator de prosa lesse o
    HTML inteiro, uma pagina que NAO nomeia ninguem passaria, porque o proprio
    script do Google carrega o nome do Google dentro dele. E o mesmo defeito da
    Robometria que achava a resposta dentro do proprio JSON-LD e passava ate com
    resposta inventada.
  * **O endereco citado so no <head>.** Canonical, og: e JSON-LD nao sao o que a
    pagina DIZ ao leitor. Afirmacao sobre o que a pagina diz se mede no corpo.
  * **A pagina que nao nomeia nada.** Sem a afirmacao de que ha ao menos um
    endereco nomeado, uma pagina vazia passaria em todas as outras regras por
    vacuidade.
  * **O subdominio da casa lido como terceiro** — e o contrario, o terceiro cujo
    nome TERMINA com o nome da casa, que uma comparacao por "contem" deixaria
    passar como se fosse da familia.
"""

import importlib.util
import os
import sys

RAIZ = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "."
ALVO = os.path.join(RAIZ, "ferramentas", "conferir-privacidade-no-ar.py")

spec = importlib.util.spec_from_file_location("portao_privacidade", ALVO)
P = importlib.util.module_from_spec(spec)
spec.loader.exec_module(P)

feitas = [0]
falhas = []


def exige(nome, cond, extra=""):
    feitas[0] += 1
    print("  %s %s%s" % ("ok   " if cond else "FALHA", nome, (" — " + extra) if extra else ""))
    if not cond:
        falhas.append(nome)


CABECA = (
    '<html><head><title>t</title>'
    '<link rel="canonical" href="https://aquametria.com.br/politica-de-privacidade/">'
    '<meta property="og:url" content="https://exemplo-do-head.com/x">'
    '<script type="application/ld+json">{"url":"https://schema-do-head.com/y"}</script>'
    '</head>'
)


def pagina(corpo, cabeca=CABECA):
    return cabeca + "<body><main>" + corpo + "</main></body></html>"


def main():
    print("\n== MUNDO 1: quem carrega sozinho e quem so e contatado no clique ==")
    html = pagina(
        '<script src="https://www.googletagmanager.com/gtag/js?id=G-X"></script>'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=X">'
        '<img src="https://down-bs-br.img.susercontent.com/a.jpg">'
        '<a href="https://s.shopee.com.br/ABC">compre</a>')
    auto, clique = P.enderecos_servidos(html)
    exige("script de terceiro conta como 'carrega sozinho'",
          "www.googletagmanager.com" in auto)
    exige("folha de estilo de terceiro conta como 'carrega sozinho'",
          "fonts.googleapis.com" in auto)
    exige("imagem de terceiro conta como 'carrega sozinho'",
          "down-bs-br.img.susercontent.com" in auto)
    exige("link de loja NAO conta como 'carrega sozinho'",
          "s.shopee.com.br" not in auto)
    exige("link de loja conta como 'so se clicar'", "s.shopee.com.br" in clique)

    print("\n== MUNDO 2: um endereco que o site de hoje nao serve ==")
    # A ilha nunca teve um iframe nem um endereco sem esquema. Os dois sao
    # permitidos pelo HTML, entao a regua tem de trata-los HOJE.
    html = pagina('<iframe src="//video-de-terceiro.net/p"></iframe>')
    auto, _ = P.enderecos_servidos(html)
    exige("iframe de terceiro, que esta ilha nunca teve, conta como 'carrega sozinho'",
          "video-de-terceiro.net" in auto)
    exige("endereco sem esquema (//host) e reconhecido",
          P.hospedeiro("//outro-terceiro.com/x") == "outro-terceiro.com")

    print("\n== MUNDO 3: a casa nunca e terceiro, e o sosia da casa nunca e a casa ==")
    exige("o dominio da ilha nao e terceiro", P.hospedeiro("https://aquametria.com.br/a") == "")
    exige("subdominio da ilha nao e terceiro", P.hospedeiro("https://cdn.aquametria.com.br/a") == "")
    exige("SOSIA da casa E terceiro — o nome so TERMINA igual",
          P.hospedeiro("https://naoeaquametria.com.br/a") == "naoeaquametria.com.br",
          "uma comparacao por 'termina com' sem o ponto deixaria este passar por casa")

    print("\n== MUNDO 4: o que conta como endereco DITO na prosa ==")
    citados = P.dominios_citados(
        "a etiqueta vem de www.googletagmanager.com e a foto de "
        "down-bs-br.img.susercontent.com; o litro custa 1,25 e o resto e etc. "
        "nada disso vale para aquametria.com.br")
    exige("endereco em prosa e reconhecido", "www.googletagmanager.com" in citados)
    exige("endereco longo em prosa e reconhecido",
          "down-bs-br.img.susercontent.com" in citados)
    exige("numero com virgula nao vira endereco", "1,25" not in citados)
    exige("a casa nao entra na lista de citados",
          not any("aquametria.com.br" in c for c in citados))
    exige("so entram os dois enderecos de verdade, nem um a mais", len(citados) == 2,
          str(sorted(citados)))

    print("\n== MUNDO 5: as portas dos fundos ==")
    # (a) o nome do terceiro DENTRO do script que o proprio terceiro serve.
    html = pagina('<script>var u="https://www.googletagmanager.com/gtag/js";</script>'
                  '<p>Esta pagina nao nomeia ninguem.</p>')
    citados = P.dominios_citados(P.texto(P.corpo_de(html)))
    exige("endereco dentro de <script> NAO conta como nomeado pela pagina",
          "www.googletagmanager.com" not in citados,
          "senao a pagina que nao diz nada passaria pela regra 2")

    # (b) o nome do terceiro so no <head>.
    html = pagina('<p>Esta pagina nao nomeia ninguem.</p>')
    citados = P.dominios_citados(P.texto(P.corpo_de(html)))
    exige("endereco so no <head> NAO conta como nomeado pela pagina",
          "exemplo-do-head.com" not in citados and "schema-do-head.com" not in citados)

    # (c) a pagina que nao nomeia nada.
    exige("pagina que nao nomeia nada tem lista vazia, e e isso que a regra final pega",
          len(citados) == 0, str(sorted(citados)))

    # (d) o corpo sem <main> cai no <body>, e nunca no <head>.
    html = ('<html><head><script type="application/ld+json">'
            '{"u":"https://schema-do-head.com/y"}</script></head>'
            '<body><p>corpo sem main, com terceiro-do-corpo.com escrito.</p></body></html>')
    citados = P.dominios_citados(P.texto(P.corpo_de(html)))
    exige("sem <main>, o corpo e o <body> — e o <head> continua fora",
          "terceiro-do-corpo.com" in citados and "schema-do-head.com" not in citados)

    print("\n== MUNDO 6: as duas direcoes da comparacao ==")
    # A comparacao em si, com mundos montados: e ela que o portao faz url a url.
    servidos = {"www.googletagmanager.com", "fonts.gstatic.com"}
    exige("endereco no ar e FORA da prosa reprova (direcao 1)",
          not {"fonts.gstatic.com"} <= P.dominios_citados(
              "so falamos de www.googletagmanager.com"),
          "a pagina esqueceu de nomear um terceiro que ela serve")
    citados = P.dominios_citados(
        "servimos www.googletagmanager.com, fonts.gstatic.com e terceiro-que-saiu.com")
    exige("endereco na prosa e FORA do ar reprova (direcao 2)",
          not citados <= servidos,
          "sobrou %s" % sorted(citados - servidos))

    print("\n== MUNDO 7: pagina fina ==")
    exige("corpo curto fica abaixo do piso de 1.500 caracteres",
          len(P.texto(P.corpo_de(pagina("<p>curta.</p>")))) < 1500)
    exige("corpo longo passa do piso",
          len(P.texto(P.corpo_de(pagina("<p>" + ("palavra " * 400) + "</p>")))) >= 1500)

    print("\n%d afirmacoes de mutacao, %d falha(s)" % (feitas[0], len(falhas)))
    for f in falhas:
        print("  FALHOU: %s" % f)
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
