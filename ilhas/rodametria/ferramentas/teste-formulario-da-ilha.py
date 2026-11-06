#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A PRIMEIRA PONTA DA 32.1-b — o `name=` de todo campo de formulario desta ilha
carrega o prefixo da ilha, e toda pagina com formulario serve `<noscript>`.

Roda SEM rede. Ele le os `snippets/*.php` desta pasta e cobra tres coisas:

  (1) **PREFIXO, e nunca a lista.** Todo `name=` de campo de formulario comeca
      com `rdm_`. A 32.1-b e explicita sobre por que a regra e de ESPACO DE
      NOMES e nao de lista: sao mais de trinta query vars reservadas do
      WordPress, todas de nome curto, e **a lista muda com a versao do
      WordPress**. Prefixo proprio torna a classe inteira impossivel; conferir
      contra a lista conserta o caso de hoje e deixa o de amanha passar.

  (2) **A LISTA, como SEGUNDA afirmacao, para quem prefixar errado.** Um campo
      que nao leva o prefixo e cujo nome esta entre as reservadas ganha uma
      falha a mais, com o nome da query var e o que ela significa no
      WordPress — porque ai o defeito nao e de arrumacao: a URL que o botao
      monta responde **404**, e so para quem aperta o botao.

  (3) **`<noscript>` em todo snippet que serve formulario.** A outra metade da
      32.1-b: com a URL respondendo 200, o botao recarrega a pagina e a caixa
      volta a servir o CASO DE EXEMPLO — a pagina responde outra pergunta e
      parece responder a da pessoa. Do lado de fora as duas paginas sao
      identicas, entao nem a 22.8 nem a 32.5 cobrem isso: quem cobre e a frase
      que a pagina serve a quem esta sem JavaScript.

POR QUE ESTE PORTAO EXISTE, E A DATA IMPORTA: a 32.1-b foi escrita em
06/11/2026, de manha, pela execucao que levou a F1 ao ar, e ela manda o portao
ter DUAS PONTAS. A segunda — a que **aperta o botao** no ar — nasceu naquela
mesma passada, em `conferir-no-ar.py`. **A primeira nao nasceu**, e a tarde do
mesmo dia mediu o custo: a F1, escrita depois da regra, tem os quatro campos
prefixados (`rdm_w`, `rdm_kmh`, `rdm_acel`, `rdm_mun`) e serve `<noscript>`; a
**F2**, escrita em 29/10, tem **cinco campos nus** (`v`, `ah`, `peso`, `relevo`,
`aut`) e **zero** `<noscript>`. A regra nasceu, foi aplicada na pagina que a
descobriu, e **nao viajou para a irma** — a 32.5-c ao pe da letra, na mesma
fabrica, no mesmo dia.

E A SEGUNDA PONTA NAO PEGAVA, e isso e o que justifica esta existir: ela exige
**200** da URL que o botao monta, e `?v=`, `?ah=`, `?peso=`, `?relevo=` e
`?aut=` respondem **200** — foi medido no proprio levantamento da 32.1-b. O ar
estava verde porque nenhum dos cinco nomes colide HOJE. **Zero medido e
informacao; zero suposto nao e** — e o risco nomeado pela propria regra e "o
proximo campo que alguem acrescentar".

A DECISAO MORA EM FUNCAO PURA, fora da varredura, e e o que torna o
`--autoteste` capaz de FABRICAR o mundo em que cada regra morde em vez de
esperar que o dado real o produza. O autoteste roda SEMPRE, junto com a passada
normal, porque a bancada desta ilha so descobre `--autoteste` nos portoes de
REDE e este e dos sem rede: portao que depende de alguem lembrar nao roda.
"""
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ILHA = AQUI.parent
SNIPPETS = ILHA / "snippets"

# O prefixo desta ilha. A 32.1-b nomeia os quatro do arquipelago (`rdm_`,
# `cdm_`, `aqm_`, `rbm_`); aqui mora o desta, e so ele.
PREFIXO = "rdm_"

# As tags que de fato enviam valor quando o formulario e submetido. `<meta
# name=>` NAO e uma delas, e e exatamente onde a regua ingenua erra — ver o
# mundo da 20.8 no autoteste.
TAGS_DE_CAMPO = ("input", "select", "textarea", "button")

# A LISTA, e ela e SEGUNDA afirmacao e nunca a primeira. Query vars publicas do
# WordPress, na redacao da 32.1-b mais as que o nucleo documenta. Ela esta aqui
# para NOMEAR o estrago de quem prefixar errado, nao para decidir o que passa:
# a regra e o prefixo, e esta lista envelhece com a versao do WordPress.
RESERVADAS_DO_WORDPRESS = {
    "m": "o arquivo de data (ano+mes) do WordPress",
    "p": "o ID do post",
    "w": "a SEMANA do arquivo de data",
    "s": "a busca do site",
    "cat": "a categoria por ID",
    "tag": "a tag por slug",
    "name": "o slug do post",
    "title": "o titulo do post",
    "order": "a ordem da listagem",
    "orderby": "o campo de ordenacao",
    "author": "o autor por ID ou nome",
    "author_name": "o autor por slug",
    "paged": "a pagina da listagem",
    "page": "a pagina interna do post",
    "page_id": "o ID da pagina",
    "feed": "o tipo de feed (rss2, atom)",
    "year": "o ano do arquivo de data",
    "monthnum": "o mes do arquivo de data",
    "day": "o dia do arquivo de data",
    "hour": "a hora do arquivo de data",
    "minute": "o minuto do arquivo de data",
    "second": "o segundo do arquivo de data",
    "term": "o termo de taxonomia",
    "taxonomy": "a taxonomia",
    "preview": "o modo de previa do editor",
    "error": "a pagina de erro",
    "embed": "a resposta de incorporacao (oEmbed)",
    "attachment": "o anexo por slug",
    "attachment_id": "o anexo por ID",
    "pagename": "o nome da pagina",
    "post_type": "o tipo de post",
    "cpage": "a pagina de comentarios",
    "search": "a busca (alias)",
    "static": "a flag de pagina estatica",
    "subpost": "o subpost",
    "robots": "a diretiva de robots",
    "sentence": "a busca por frase inteira",
    "calendar": "o calendario",
    "withcomments": "a listagem com comentarios",
    "withoutcomments": "a listagem sem comentarios",
}

falhas = []
notas = []


def afirma(condicao, mensagem):
    if not condicao:
        falhas.append(mensagem)


def nota(texto):
    notas.append(texto)


# ---------------------------------------------------------------------------
# AS FUNCOES PURAS. A varredura nao decide nada: ela le arquivo e pergunta.
# ---------------------------------------------------------------------------

_CAMPO = re.compile(
    r"<\s*(input|select|textarea|button)\b[^>]*?\bname\s*=\s*(['\"])(.*?)\2",
    re.IGNORECASE | re.DOTALL)


def campos_de_formulario(texto):
    """Devolve [(tag, nome)] de todo campo que ENVIA valor, na ordem do arquivo.

    So `input`, `select`, `textarea` e `button`. O recorte e pela TAG e nunca
    pelo `name=` solto, e e essa a diferenca que o mundo da 20.8 no autoteste
    prova: `<meta name="description">` casa com `name=` e nao e campo de
    formulario nenhum — reprovar por causa dele seria reprovar a pagina certa,
    que e o caminho mais curto para alguem passar a ignorar o portao (20.5).
    """
    achados = []
    for m in _CAMPO.finditer(texto):
        tag = m.group(1).lower()
        nome = m.group(3).strip()
        if nome:
            achados.append((tag, nome))
    return achados


def regua_ingenua(texto):
    """A regua VELHA, reproduzida de proposito para o autoteste provar que as
    duas DISCORDAM (20.8): todo `name=` do arquivo, sem olhar a tag.

    Autoteste em que a regua nova e a velha concordam nao mede conserto nenhum.
    """
    return [m.group(2).strip()
            for m in re.finditer(r"\bname\s*=\s*(['\"])(.*?)\1", texto, re.DOTALL)
            if m.group(2).strip()]


def prefixo_ok(nome, prefixo=PREFIXO):
    """A PRIMEIRA afirmacao, e ela e sobre espaco de nomes.

    O nome tem de comecar com o prefixo E ter algo depois dele: `rdm_` pelado
    nao nomeia campo nenhum.
    """
    return nome.startswith(prefixo) and len(nome) > len(prefixo)


def reservada_do_wordpress(nome):
    """A SEGUNDA afirmacao. Devolve o que a query var significa, ou None.

    O nome e normalizado para minusculas porque o WordPress resolve query var
    em minuscula; `W` colidiria igual a `w`.
    """
    return RESERVADAS_DO_WORDPRESS.get(nome.strip().lower())


def tem_formulario(texto):
    """Serve formulario? Pela TAG `<form`, que e o que o navegador submete."""
    return bool(re.search(r"<\s*form\b", texto, re.IGNORECASE))


# O componente da casca que escreve o aviso. O snippet pode servir a tag ele
# mesmo OU chamar o componente — as duas atendem a 32.1-b, e cobrar so a tag
# reprovaria justamente o snippet que fez a coisa certa.
COMPONENTE_DO_AVISO = "rodametria_casca_noscript("


def tem_noscript(texto):
    """Serve `<noscript>`? A outra metade da 32.1-b.

    DUAS FORMAS CONTAM, e esta funcao nasceu com UMA e foi corrigida na mesma
    passada por ter reprovado a pagina certa: a tag escrita no proprio snippet,
    OU a chamada do componente da casca que a escreve (32.6-b). Quando o aviso
    da F1 saiu do snippet e virou componente — que e exatamente o conserto que
    a regra pede —, este portao ficou VERMELHO na F1. Portao que reprova quem
    obedeceu e o caminho mais curto para alguem passar a ignora-lo (20.5).

    E ESTA FUNCAO NAO E O VEREDITO, e isso esta dito para ninguem a ler como
    tal: ela mede o REPOSITORIO. Quem mede o que a pagina SERVE e
    `conferir-no-ar.py`, que le o HTML de cada URL do sitemap e exige o
    `<noscript>` onde houver `<form>`. Esta aqui e a margem que pega o defeito
    antes do desembarque; a de la e a que conta.
    """
    if re.search(r"<\s*noscript\b", texto, re.IGNORECASE):
        return True
    return COMPONENTE_DO_AVISO in texto


# ---------------------------------------------------------------------------
# A PASSADA SOBRE OS ARQUIVOS DE VERDADE
# ---------------------------------------------------------------------------

def passada():
    arquivos = sorted(SNIPPETS.glob("*.php"))
    afirma(bool(arquivos), "nenhum snippet em %s — o portao nao tem o que medir" % SNIPPETS)

    total_campos = 0
    com_formulario = []

    for caminho in arquivos:
        texto = caminho.read_text(encoding="utf-8")
        rotulo = caminho.name

        campos = campos_de_formulario(texto)
        total_campos += len(campos)

        for tag, nome in campos:
            afirma(prefixo_ok(nome),
                   "32.1-b: em %s o campo <%s name=\"%s\"> nao carrega o prefixo "
                   "`%s` desta ilha. A regra e de espaco de nomes e nao de lista: "
                   "as query vars reservadas do WordPress sao mais de trinta, "
                   "todas de nome curto, e a lista muda com a versao."
                   % (rotulo, tag, nome, PREFIXO))

            # SEGUNDA afirmacao, e ela so faz sentido para quem furou a primeira.
            if not prefixo_ok(nome):
                significado = reservada_do_wordpress(nome)
                afirma(significado is None,
                       "32.1-b: em %s o campo <%s name=\"%s\"> usa uma query var "
                       "RESERVADA do WordPress (%s). A URL que o botao monta "
                       "responde 404, e so para quem aperta o botao: a pagina "
                       "responde 200, o portao de ar fica verde e o de pixel "
                       "tambem." % (rotulo, tag, nome, significado))

        if tem_formulario(texto):
            com_formulario.append(rotulo)
            afirma(tem_noscript(texto),
                   "32.1-b: %s serve <form> e nao serve <noscript>. Com a URL em "
                   "200, o botao recarrega a pagina e a caixa volta a servir o "
                   "CASO DE EXEMPLO — a pagina responde outra pergunta e parece "
                   "responder a da pessoa. Do lado de fora as duas paginas sao "
                   "identicas, entao nenhum outro portao desta ilha ve isso."
                   % rotulo)

        if campos:
            nota("%s: %d campo(s) — %s"
                 % (rotulo, len(campos), ", ".join(n for _, n in campos)))

    nota("%d snippet(s) lidos, %d campo(s) de formulario, %d com <form>: %s"
         % (len(arquivos), total_campos, len(com_formulario),
            ", ".join(com_formulario) if com_formulario else "nenhum"))

    # A TRAVA DE ALVO EXATO DESTA BATERIA: se os snippets deixarem de ter campo
    # de formulario, este portao passa a medir NADA e ficaria verde dizendo
    # isso. A cicatriz e dos 18 portoes inertes da Robometria.
    afirma(total_campos > 0,
           "o portao nao achou NENHUM campo de formulario nos snippets desta "
           "ilha. Ou a varredura quebrou, ou as ferramentas sairam do ar — nos "
           "dois casos este verde seria falso.")
    afirma(bool(com_formulario),
           "nenhum snippet serve <form>: a afirmacao do <noscript> nao mediu nada.")


# ---------------------------------------------------------------------------
# O AUTOTESTE — mundos FABRICADOS, cada um com a saida escrita a mao
# ---------------------------------------------------------------------------

def autoteste():
    casos = []

    # (1) o mundo SAO: campo prefixado, dentro de tag de campo
    sao = '<form><input name="rdm_peso" type="number"></form><noscript>aviso</noscript>'
    casos.append(("campo prefixado passa",
                  lambda: campos_de_formulario(sao) == [("input", "rdm_peso")]
                  and prefixo_ok("rdm_peso")))

    # (2) o mundo MEDIDO em 06/11/2026: os cinco campos nus da F2
    for nome in ("v", "ah", "peso", "relevo", "aut"):
        casos.append(("o campo nu `%s` da F2 e pego" % nome,
                      lambda n=nome: not prefixo_ok(n)))

    # (3) O CASO QUE CUSTOU O 404, e ele e o mundo medido da 32.1-b: `w`
    casos.append(("`w` e pego pelo prefixo",
                  lambda: not prefixo_ok("w")))
    casos.append(("`w` e NOMEADO pela lista como a semana do arquivo de data",
                  lambda: "SEMANA" in (reservada_do_wordpress("w") or "").upper()))
    casos.append(("`W` maiusculo colide igual",
                  lambda: reservada_do_wordpress("W") is not None))

    # (4) prefixo PELADO nao nomeia campo
    casos.append(("`rdm_` pelado nao passa", lambda: not prefixo_ok("rdm_")))

    # (5) prefixo de OUTRA ilha nao passa nesta
    casos.append(("`cdm_peso` nao passa nesta ilha", lambda: not prefixo_ok("cdm_peso")))

    # (6) O MUNDO DA 20.8: a regua NOVA e a VELHA tem de DISCORDAR.
    #     `<meta name="description">` casa com `name=` e NAO e campo. A regua
    #     velha o pegaria e reprovaria a pagina certa.
    meta = ('<meta name="description" content="x">'
            '<form><select name="rdm_relevo"></select></form>'
            '<noscript>aviso</noscript>')
    casos.append(("a regua nova ignora <meta name=>",
                  lambda: campos_de_formulario(meta) == [("select", "rdm_relevo")]))
    casos.append(("a regua VELHA pegaria o <meta> — as duas DISCORDAM (20.8)",
                  lambda: "description" in regua_ingenua(meta)
                  and "description" not in [n for _, n in campos_de_formulario(meta)]))

    # (7) as quatro tags que enviam valor sao alcancadas, e so elas
    quatro = ('<input name="rdm_a"><select name="rdm_b"></select>'
              '<textarea name="rdm_c"></textarea><button name="rdm_d"></button>'
              '<meta name="rdm_nao"><div name="rdm_tambem_nao"></div>')
    casos.append(("as quatro tags de campo entram e as outras duas nao",
                  lambda: [t for t, _ in campos_de_formulario(quatro)]
                  == ["input", "select", "textarea", "button"]))

    # (8) aspas simples, quebra de linha e espaco em volta do `=` — como o PHP
    #     de verdade escreve, em varias linhas
    torto = ("<input\n\tid='x'\n\tname = 'rdm_carga'\n\ttype='number'>")
    casos.append(("campo escrito em varias linhas e com aspas simples e lido",
                  lambda: campos_de_formulario(torto) == [("input", "rdm_carga")]))

    # (9) o <noscript> e cobrado SO de quem serve <form>
    casos.append(("snippet sem <form> nao e cobrado de <noscript>",
                  lambda: not tem_formulario('<div><p>texto</p></div>')))
    casos.append(("snippet com <form> e sem <noscript> e pego",
                  lambda: tem_formulario('<form><input name="rdm_x"></form>')
                  and not tem_noscript('<form><input name="rdm_x"></form>')))
    casos.append(("<form> e achado pela tag e nao pela palavra",
                  lambda: not tem_formulario('<p>o formulario acima</p>')))

    # (9-b) O MUNDO QUE ESTE PORTAO REPROVOU ERRADO, FABRICADO PARA NAO VOLTAR.
    #       Quando o aviso da F1 saiu do snippet e virou componente da casca —
    #       que e o conserto que a 32.1-b pede —, a primeira versao desta regua
    #       ficou VERMELHA na F1, porque procurava a TAG e o snippet passou a
    #       ter a CHAMADA. As duas formas atendem a regra.
    casos.append(("a chamada do componente da casca conta como aviso",
                  lambda: tem_noscript('$h .= rodametria_casca_noscript( array( "x" ) );')))
    casos.append(("a tag escrita no snippet continua contando",
                  lambda: tem_noscript('<noscript><p>x</p></noscript>')))
    casos.append(("quem nao faz nenhuma das duas e pego",
                  lambda: not tem_noscript('$h .= rodametria_casca_caixa( "a", "1", "W", array() );')))

    # (10) campo sem `name=` nao entra (botao de submit sem nome e comum e legal)
    casos.append(("<button> sem name nao entra na conta",
                  lambda: campos_de_formulario('<button type="submit">Calcular</button>') == []))

    # (11) A TRAVA DE ALVO EXATO: os arquivos de verdade ainda tem a forma que
    #      estes mundos mexem. Sem isto, a bateria passaria medindo nada no dia
    #      em que os snippets mudassem de forma.
    def alvo_exato():
        arquivos = sorted(SNIPPETS.glob("*.php"))
        if not arquivos:
            return False
        junto = "".join(c.read_text(encoding="utf-8") for c in arquivos)
        return bool(campos_de_formulario(junto)) and tem_formulario(junto)

    casos.append(("a bateria ainda alcanca o que muta", alvo_exato))

    for nome, prova in casos:
        afirma(prova(), "AUTOTESTE: %s — a regra nao morde" % nome)
    nota("autoteste: %d caso(s)" % len(casos))


def main():
    if not SNIPPETS.is_dir():
        print("REPROVADO — %s nao existe" % SNIPPETS)
        return 1

    passada()
    autoteste()

    for n in notas:
        print("  . %s" % n)
    print("")
    for f in falhas:
        print("FALHA %s" % f)
    print("")
    print("%d falha(s)." % len(falhas))
    print("APROVADO" if not falhas else "REPROVADO")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
