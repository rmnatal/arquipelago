#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O portao das quatro paginas que o site deve a quem le (bloco 5d).

Roda SEM rede. Ele julga `dados/paginas-institucionais.json` e
`snippets/rodametria-institucional.php`, e o que ele cobra e:

  (1) as quatro paginas sao EXATAMENTE as que a 16.1 nomeia por nome — nem uma
      a mais na raiz, nem uma a menos;
  (2) ZERO digito na prosa declarada fora de `digitos_permitidos`. Numero de
      tela nasce CONTADO (secao 8), e digito solto na prosa e a forma mais
      comum de um numero envelhecer calado;
  (3) todo molde {ASSIM} usado na prosa e um que o preenchedor do PHP conhece —
      lido do proprio PHP, nunca duplicado aqui;
  (4) todo item do bloco de recusa ABRE negando. A cicatriz e da clubedomosaico
      (11/09/2026, secao 8): perdoar por presenca de palavra e adivinhar, e uma
      promessa dentro de um bloco chamado "recusa" passou por uma regua que so
      pedia negacao em algum lugar;
  (5) o corpo de cada pagina tem o piso de 1.500 caracteres da secao 8 na conta
      SECA da prosa declarada. **Este nao e o veredito** — o veredito e no ar,
      por `conferir-no-ar.py`, e esta conta e so uma margem para a pagina nao
      ser desembarcada fina. Foi a mae `/veiculos/` que ensinou isso em 29/10:
      a conta de antes do desembarque dava 1.253 e a pagina no ar passou;
  (6) as afirmacoes de CODIGO que a pagina de privacidade faz sao provaveis nos
      arquivos desta ilha: nenhum snippet escreve cookie, carrega medidor de
      audiencia ou pede dado por formulario que ENVIA. Afirmacao sobre codigo
      nao e contavel do banco, entao ela se prova aqui — e a outra metade, a do
      HTML servido, e do portao de ar.

A DECISAO MORA EM FUNCAO PURA, e nao dentro da varredura: e o que torna o
`--autoteste` capaz de FABRICAR o mundo em que cada regra morde, em vez de
esperar que o dado real o produza algum dia (secao 8, a cicatriz das 270 colas).
O autoteste roda SEMPRE, junto com a passada normal.
"""
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ILHA = AQUI.parent

DECLARADO = ILHA / "dados" / "paginas-institucionais.json"
PHP = ILHA / "snippets" / "rodametria-institucional.php"

# A 16.1 nomeia estas cinco como as UNICAS da raiz. A home nao e desta familia.
AS_QUATRO = ("sobre", "contato", "divulgacao-de-afiliados", "privacidade")

PISO_DE_CORPO = 1500
TETO_DE_DESCRIPTION = 200

# Abertura de negacao aceita. Lista curta de proposito: quem precisar de uma
# sexta forma escreve a frase de outro jeito, porque bloco de recusa que aceita
# qualquer abertura deixa de separar recusa de promessa.
ABRE_NEGANDO = ("Não ", "Nunca ", "Nenhum", "Nenhuma", "Nem ")

falhas = []
notas = []


def afirma(cond, msg):
    if not cond:
        falhas.append(msg)
    return bool(cond)


def nota(msg):
    notas.append(msg)


# ---------------------------------------------------------------------------
# O QUE E FATO EXTERNO: lido de UM lugar so (secao 8)
# ---------------------------------------------------------------------------

def moldes_que_o_php_conhece(texto_php):
    """As chaves do array que `rdm_inst_numeros()` devolve.

    Fato externo a este portao: quem decide o que o preenchedor sabe trocar e o
    PHP. Reescrever a lista aqui criaria duas verdades, e a segunda envelhece.
    """
    bloco = re.search(r"\$n\s*=\s*array\(\s*(.*?)\n\s*\);", texto_php, re.S)
    if not bloco:
        return set()
    return set(re.findall(r"'([A-Z_]+)'\s*=>", bloco.group(1)))


# ---------------------------------------------------------------------------
# AS DECISOES: funcoes puras, para o autoteste poder fabricar o mundo
# ---------------------------------------------------------------------------

def regras_de_css(folha):
    """Os pares (seletor, corpo) de uma folha, com os comentarios FORA.

    Comentario e prosa, e prosa nao veste pixel nenhum. Medir a palavra solta
    no texto inteiro da folha confunde o comentario que explica a regra com a
    regra, e foi o que a primeira versao desta regua fez.
    """
    sem_comentario = re.sub(r"/\*.*?\*/", " ", folha, flags=re.S)
    return [(m.group(1).strip(), m.group(2))
            for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", sem_comentario)]


# O que e da casca e nao se reveste aqui, com o nome de cada coisa.
DA_CASCA = (
    (re.compile(r"(^|[\s,>+~])h[1-6]\b"), "titulo, vestido pela casca"),
    (re.compile(r"\.rdm-molde-caixa"), "a caixa do molde (32.1)"),
    (re.compile(r"\.rdm-molde-dobra"), "a dobra do molde (32.1)"),
    (re.compile(r"\.rdm-molde-cart"), "o cartao de compra do molde (32.1)"),
    (re.compile(r"\.rdm-trilha"), "a trilha (16.3)"),
    (re.compile(r"\.rdm-rodape"), "o rodape da casca"),
    (re.compile(r"\.rdm-nav"), "o menu da casca"),
)


def seletores_da_casca_na_folha(folha):
    """Os seletores desta folha que invadem o que a casca ja veste."""
    achados = []
    for seletor, _corpo in regras_de_css(folha):
        if seletor.startswith("@"):
            continue
        for padrao, por_que in DA_CASCA:
            if padrao.search(seletor):
                achados.append((seletor, por_que))
                break
    return achados


def prosa_da_pagina(pg):
    """Todo texto da pagina que vai para a tela, numa lista de (onde, texto)."""
    saida = []
    for campo in ("h1", "titulo", "description", "linha_mestra"):
        if pg.get(campo):
            saida.append((campo, str(pg[campo])))
    c = pg.get("caixa") or {}
    for campo in ("rotulo", "numero", "unidade"):
        if c.get(campo):
            saida.append(("caixa.%s" % campo, str(c[campo])))
    for i, f in enumerate(c.get("frases") or []):
        saida.append(("caixa.frases[%d]" % i, str(f)))
    for i, s in enumerate(pg.get("secoes") or []):
        saida.append(("secoes[%d].titulo" % i, str(s.get("titulo", ""))))
        for j, p in enumerate(s.get("paragrafos") or []):
            saida.append(("secoes[%d].paragrafos[%d]" % (i, j), str(p)))
    r = pg.get("recusa") or {}
    if r.get("titulo"):
        saida.append(("recusa.titulo", str(r["titulo"])))
    for i, it in enumerate(r.get("itens") or []):
        saida.append(("recusa.itens[%d]" % i, str(it)))
    for i, d in enumerate(pg.get("dobras") or []):
        saida.append(("dobras[%d].titulo" % i, str(d.get("titulo", ""))))
        for j, p in enumerate(d.get("paragrafos") or []):
            saida.append(("dobras[%d].paragrafos[%d]" % (i, j), str(p)))
    return saida


def digitos_soltos(pg, permitidos):
    """Onde ha digito na prosa fora da lista de permitidos. Lista vazia = limpo.

    O MOLDE NAO CONTA como digito solto: `{VEICULOS_NO_BANCO}` nao tem digito, e
    e justamente ele que o digito deveria ter sido.
    """
    achados = []
    for onde, texto in prosa_da_pagina(pg):
        limpo = texto
        for p in permitidos:
            limpo = limpo.replace(p, " ")
        if re.search(r"\d", limpo):
            achados.append((onde, re.findall(r"\S*\d\S*", limpo)))
    return achados


def moldes_usados(pg):
    usados = set()
    for _, texto in prosa_da_pagina(pg):
        usados |= set(re.findall(r"\{([A-Z_]+)\}", texto))
    return usados


def recusa_mal_formada(pg):
    """Os problemas do bloco de recusa. Lista vazia = bloco bem formado."""
    r = pg.get("recusa") or {}
    problemas = []
    itens = r.get("itens") or []
    if not r.get("titulo"):
        problemas.append("sem titulo")
    if len(itens) < 3:
        problemas.append("tem %d item(ns) e o piso e 3" % len(itens))
    for i, it in enumerate(itens):
        if not str(it).startswith(ABRE_NEGANDO):
            problemas.append("o item %d nao ABRE negando: %r" % (i, str(it)[:60]))
    return problemas


def corpo_em_caracteres(pg):
    """A conta SECA da prosa que vai para a tela. Nao e o veredito: ver o modulo."""
    return sum(len(t) for onde, t in prosa_da_pagina(pg) if onde != "titulo" and onde != "description")


def defeitos_de_forma(pg, slugs_conhecidos):
    """Campos obrigatorios e as duas travas de forma da caixa e da malha."""
    d = []
    for campo in ("slug", "nome", "titulo", "h1", "description"):
        if not pg.get(campo):
            d.append("sem %s" % campo)
    if pg.get("description") and len(str(pg["description"])) > TETO_DE_DESCRIPTION:
        d.append("description com %d caracteres e o teto do portao de ar e %d"
                 % (len(str(pg["description"])), TETO_DE_DESCRIPTION))
    c = pg.get("caixa") or {}
    if not c:
        d.append("sem caixa de resposta, e a 32.2 a poe no topo")
    elif not re.fullmatch(r"\{[A-Z_]+\}", str(c.get("numero", "")).strip()):
        # O numero da caixa e o numero GRANDE da primeira tela. Ele nunca e
        # literal: e ele que a secao 8 chama de "numero de tela digitado".
        d.append("o numero da caixa nao e um molde: %r" % c.get("numero"))
    if len(pg.get("secoes") or []) < 2:
        d.append("tem menos de 2 secoes visiveis")
    if len(pg.get("dobras") or []) < 1:
        d.append("sem nenhuma dobra")
    for s in pg.get("veja_tambem") or []:
        if s not in slugs_conhecidos:
            d.append("veja_tambem aponta para %r, que nao e pagina desta familia" % s)
    if pg.get("slug") in (pg.get("veja_tambem") or []):
        d.append("veja_tambem aponta para a propria pagina")
    return d


# ---------------------------------------------------------------------------
# A PASSADA NORMAL
# ---------------------------------------------------------------------------

def passada(declarado, texto_php):
    paginas = declarado.get("paginas") or []
    por_slug = {p.get("slug"): p for p in paginas}
    permitidos = declarado.get("digitos_permitidos") or []

    afirma(tuple(sorted(por_slug)) == tuple(sorted(AS_QUATRO)),
           "as paginas declaradas sao %s e a 16.1 nomeia %s"
           % (sorted(por_slug), sorted(AS_QUATRO)))

    conhecidos = moldes_que_o_php_conhece(texto_php)
    afirma(len(conhecidos) >= 10,
           "o PHP so declarou %d molde(s) — ou o preenchedor encolheu, ou esta regua "
           "deixou de achar o array dele (e ai ela nao mede nada)" % len(conhecidos))
    nota("o preenchedor do PHP conhece %d molde(s)" % len(conhecidos))

    for slug in sorted(por_slug):
        pg = por_slug[slug]

        for d in defeitos_de_forma(pg, set(AS_QUATRO)):
            afirma(False, "%s: %s" % (slug, d))

        for onde, achados in digitos_soltos(pg, permitidos):
            afirma(False, "%s: digito na prosa em %s — %s. Numero de tela nasce contado, "
                          "e o lugar dele e um molde" % (slug, onde, achados))

        usados = moldes_usados(pg)
        orfaos = sorted(usados - conhecidos)
        afirma(not orfaos,
               "%s: usa molde que o preenchedor nao conhece: %s — ele iria para a tela cru"
               % (slug, orfaos))

        for p in recusa_mal_formada(pg):
            afirma(False, "%s: bloco de recusa %s" % (slug, p))

        n = corpo_em_caracteres(pg)
        afirma(n >= PISO_DE_CORPO,
               "%s: a prosa declarada tem %d caracteres e o piso da secao 8 e %d — e esta "
               "conta e a MARGEM, nao o veredito: quem decide e conferir-no-ar.py"
               % (slug, n, PISO_DE_CORPO))
        nota("%s: %d caracteres de prosa declarada (o veredito e no ar)" % (slug, n))

    # --- os terceiros que a pagina de privacidade nomeia ---
    terceiros = declarado.get("terceiros_que_carregam") or []
    afirma(len(terceiros) >= 1,
           "nenhum terceiro declarado — e a pagina de privacidade afirma sobre eles")
    for t in terceiros:
        for campo in ("quem", "o_que", "endereco", "onde", "medido_em"):
            afirma(bool(t.get(campo)),
                   "terceiro %r sem %s — sem isso a frase da tela sai incompleta"
                   % (t.get("quem"), campo))
    nota("terceiros declarados: %s" % ", ".join(t.get("endereco", "?") for t in terceiros))

    # --- as afirmacoes de CODIGO da pagina de privacidade ---
    proibidos_no_codigo = (
        ("setcookie", "a pagina de privacidade afirma que este site nao escreve cookie"),
        ("googletagmanager", "a pagina de privacidade afirma que nao ha medidor de audiencia"),
        ("google-analytics", "a pagina de privacidade afirma que nao ha medidor de audiencia"),
        ("gtag(", "a pagina de privacidade afirma que nao ha medidor de audiencia"),
        ("connect.facebook", "a pagina de privacidade afirma que nao ha pixel de rede social"),
        ("fbq(", "a pagina de privacidade afirma que nao ha pixel de rede social"),
        ('method="post"', "a pagina de privacidade afirma que nenhuma pagina pede um dado seu"),
        ("method='post'", "a pagina de privacidade afirma que nenhuma pagina pede um dado seu"),
    )
    for php in sorted((ILHA / "snippets").glob("*.php")):
        corpo = php.read_text(encoding="utf-8")
        for agulha, por_que in proibidos_no_codigo:
            afirma(agulha not in corpo,
                   "%s tem %r e %s — a pagina tem de mudar ANTES do codigo"
                   % (php.name, agulha, por_que))
    nota("%d snippet(s) desta ilha conferidos contra as afirmacoes de codigo da privacidade"
         % len(list((ILHA / "snippets").glob("*.php"))))

    # --- a versao do PHP existe como constante (o manifest a casa) ---
    afirma(bool(re.search(r"RODAMETRIA_INST_VERSAO'\s*,\s*'\d+\.\d+\.\d+'", texto_php)),
           "o PHP nao declara RODAMETRIA_INST_VERSAO com tres numeros")
    # --- a folha nao redecora o que e da casca (32.5-c) ---
    folha = re.search(r"<style id=\"rdm-inst-folha\">(.*?)</style>", texto_php, re.S)
    if afirma(bool(folha), "o PHP nao tem a folha desta familia"):
        # A REGUA MEDE O SELETOR, NUNCA A PALAVRA SOLTA. A primeira versao desta
        # linha procurava "h1" no texto da folha e REPROVOU a folha certa, por
        # causa do comentario que explica justamente por que ela nao mexe em h1 —
        # e portao que reprova pagina certa e o caminho mais curto para alguem
        # passar a ignora-lo (20.5 e 32.5-b, as duas pelo nome).
        for seletor, por_que in seletores_da_casca_na_folha(folha.group(1)):
            afirma(False,
                   "a folha desta familia veste %r, que e %s — e a 32.5-c: folha de pagina "
                   "vencendo a do molde por ordem de carga" % (seletor, por_que))
        nota("a folha desta familia tem %d regra(s), nenhuma sobre o que e da casca"
             % len(regras_de_css(folha.group(1))))


# ---------------------------------------------------------------------------
# O AUTOTESTE — fabrica o mundo em que cada regra morde
# ---------------------------------------------------------------------------

def autoteste(declarado, texto_php):
    """Prova que as cinco decisoes REPROVAM, cada uma no mundo que as morde.

    Sem isto, uma regra escrita para um mundo que nunca aconteceu nasce errada
    sem poder falhar (secao 8). Os mundos sao fabricados a partir do declarado
    real, mexendo UMA coisa de cada vez.
    """
    import copy

    base = copy.deepcopy(declarado["paginas"][0])
    permitidos = declarado.get("digitos_permitidos") or []
    conhecidos = moldes_que_o_php_conhece(texto_php)

    casos = []

    # (1) o mundo real tem de PASSAR em todas — se nao, o autoteste mede nada
    casos.append(("o mundo real passa: digito solto",
                  lambda: not digitos_soltos(base, permitidos)))
    casos.append(("o mundo real passa: recusa bem formada",
                  lambda: not recusa_mal_formada(base)))
    casos.append(("o mundo real passa: molde conhecido",
                  lambda: not (moldes_usados(base) - conhecidos)))
    casos.append(("o mundo real passa: forma",
                  lambda: not defeitos_de_forma(base, set(AS_QUATRO))))

    # (2) digito plantado na prosa
    com_digito = copy.deepcopy(base)
    com_digito["secoes"][0]["paragrafos"][0] += " São 17 veículos no banco hoje."
    casos.append(("digito plantado na prosa e ACHADO",
                  lambda: bool(digitos_soltos(com_digito, permitidos))))

    # (3) digito plantado DENTRO de um permitido continua passando (a trava nao
    #     pode reprovar a citacao legal que ela existe para tolerar)
    so_citacao = copy.deepcopy(base)
    so_citacao["secoes"][0]["paragrafos"][0] += " Resolução Contran nº 996/2023."
    casos.append(("citacao legal permitida NAO e reprovada",
                  lambda: not digitos_soltos(so_citacao, permitidos)))

    # (4) molde que o preenchedor nao conhece
    com_orfao = copy.deepcopy(base)
    com_orfao["secoes"][0]["paragrafos"][0] += " Hoje temos {MOLDE_QUE_NINGUEM_PREENCHE}."
    casos.append(("molde orfao e ACHADO",
                  lambda: bool(moldes_usados(com_orfao) - conhecidos)))

    # (5) promessa escondida dentro do bloco de recusa — a cicatriz literal
    promessa = copy.deepcopy(base)
    promessa["recusa"]["itens"].append("Peça já, últimas unidades!")
    casos.append(("promessa dentro do bloco de recusa e ACHADA",
                  lambda: bool(recusa_mal_formada(promessa))))

    # (6) negacao no MEIO da frase nao basta: ela tem de ABRIR negando
    negacao_tardia = copy.deepcopy(base)
    negacao_tardia["recusa"]["itens"].append(
        "A ficha deste produto lista as superfícies em que ele NÃO deve ser usado.")
    casos.append(("negacao no meio da frase nao passa por recusa",
                  lambda: bool(recusa_mal_formada(negacao_tardia))))

    # (7) bloco de recusa com menos de tres itens
    recusa_curta = copy.deepcopy(base)
    recusa_curta["recusa"]["itens"] = recusa_curta["recusa"]["itens"][:2]
    casos.append(("recusa com dois itens e ACHADA",
                  lambda: bool(recusa_mal_formada(recusa_curta))))

    # (8) numero literal na caixa — o "numero de tela digitado" da secao 8
    caixa_literal = copy.deepcopy(base)
    caixa_literal["caixa"]["numero"] = "17"
    casos.append(("numero literal na caixa e ACHADO",
                  lambda: bool(defeitos_de_forma(caixa_literal, set(AS_QUATRO)))))

    # (9) veja_tambem apontando para fora da familia
    malha_torta = copy.deepcopy(base)
    malha_torta["veja_tambem"] = ["metodologia"]
    casos.append(("veja_tambem para fora da familia e ACHADO",
                  lambda: bool(defeitos_de_forma(malha_torta, set(AS_QUATRO)))))

    # (10) pagina fina
    fina = copy.deepcopy(base)
    fina["secoes"] = [{"titulo": "Curta", "paragrafos": ["Pouco texto."]}]
    fina["dobras"] = [{"titulo": "Dobra", "paragrafos": ["Nada."]}]
    fina["linha_mestra"] = "Nada."
    casos.append(("pagina fina e ACHADA pela conta seca",
                  lambda: corpo_em_caracteres(fina) < PISO_DE_CORPO))

    # (11) a regua da folha: ela mede SELETOR e nao palavra solta, e as duas
    #      metades sao provadas — o comentario que fala de h1 NAO reprova, e o
    #      seletor que veste h2 reprova. A primeira versao desta regua reprovou
    #      a folha certa por causa do proprio comentario.
    folha_real = re.search(r"<style id=\"rdm-inst-folha\">(.*?)</style>", texto_php, re.S)
    casos.append(("a folha real passa, apesar de o comentario dela citar h1 e h2",
                  lambda: folha_real is not None
                  and not seletores_da_casca_na_folha(folha_real.group(1))))
    casos.append(("comentario que cita h2 NAO e lido como seletor",
                  lambda: not seletores_da_casca_na_folha(
                      "/* nada aqui mexe em h2 nem em .rdm-molde-caixa */\n.x{color:red}")))
    casos.append(("seletor que veste h2 e ACHADO",
                  lambda: bool(seletores_da_casca_na_folha(
                      "body.rdm .rdm-inst-secao h2{font-size:1rem}"))))
    casos.append(("seletor que veste a caixa do molde e ACHADO",
                  lambda: bool(seletores_da_casca_na_folha(
                      "body.rdm .rdm-molde-caixa{border:0}"))))
    casos.append(("@media nao e confundido com seletor",
                  lambda: not seletores_da_casca_na_folha(
                      "@media (max-width:480px){body.rdm .rdm-inst-secao p{max-width:40ch}}")))

    # (12) a trava de alvo exato da propria bateria: se o declarado deixar de ter
    #      a forma que estes mundos mexem, o autoteste PARA em vez de passar
    #      medindo nada (a cicatriz das 18 mutacoes inertes da Robometria)
    casos.append(("a bateria ainda alcanca o que muta",
                  lambda: bool(base.get("secoes") and base["secoes"][0].get("paragrafos")
                               and base.get("recusa", {}).get("itens")
                               and base.get("caixa", {}).get("numero"))))

    for nome, prova in casos:
        afirma(prova(), "AUTOTESTE: %s — a regra nao morde" % nome)
    nota("autoteste: %d caso(s)" % len(casos))


def main():
    if not DECLARADO.exists():
        print("REPROVADO — %s nao existe" % DECLARADO)
        return 1
    if not PHP.exists():
        print("REPROVADO — %s nao existe" % PHP)
        return 1

    declarado = json.loads(DECLARADO.read_text(encoding="utf-8"))
    texto_php = PHP.read_text(encoding="utf-8")

    passada(declarado, texto_php)
    autoteste(declarado, texto_php)

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
