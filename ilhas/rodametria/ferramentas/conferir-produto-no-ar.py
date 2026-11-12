#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CONFERE NO AR AS PAGINAS DE VITRINE (secao 30) — A ESCADA DA 25.2 NA TELA.

    python3 ferramentas/conferir-produto-no-ar.py

POR QUE ELE NASCEU EM 30/10/2026, e a causa e uma LACUNA e nao um defeito:
`conferir-no-ar.py` confere a casca e a F2, e `conferir-institucional-no-ar.py`
confere as quatro paginas do bloco 5d. As paginas de VITRINE — `/veiculos/` e as
filhas — nao tinham portao de ar NENHUM desde que nasceram em 29/10. O que as
media era `conferir-32-5-no-navegador.mjs`, que julga PIXEL, e `mutacoes-produto.py`,
que roda sem rede sobre o gerador. **Entre os dois faltava quem lesse o HTML
servido.** E foi justamente ali que a escada da 25.2 tinha TRES lugares lendo a
`url` crua do dado.

O QUE ELE COBRA, e cada item e uma coisa que o dado de hoje NAO exercita:
  1. ZERO `href=""` no HTML servido. Era o estado em que a celula "Comprar" da
     tabela cairia no dia em que uma ficha morresse — e `href=""` nao e botao
     morto: e um botao que RECARREGA A PROPRIA PAGINA, com o rotulo "Ver na
     Shopee" do lado.
  2. A LINHA DISCRETA DO PISO da 25.2, UMA vez por pagina. Uma, e nao uma por
     linha, porque o piso e da CONSULTA e nao do anuncio — ha UMA `url_busca`
     distinta por pagina, e repeti-la seria o mesmo link dezesseis vezes.
  3. TODO anuncio da vitrine NOMEADO na tabela (secao 7) e com saida de compra.
  4. `rel="sponsored noopener"` e `target="_blank"` em TODO link de afiliado.
  5. O JSON-LD: nenhuma `Offer` com `url` vazia; NENHUMA com `availability` ou
     `priceValidUntil`; e TODA com `priceSpecification.validFrom` igual a data
     de coleta daquela linha, que e a MESMA que a tela imprime ao lado do
     numero. Ate 12/11/2026 este item dizia "`availability` so onde ha ficha", e
     a frase estava meia certa: ficha EXISTIR nao e estar VENDENDO, e
     `availability` nao tem onde pendurar a data da medicao. Ver a secao 7-b do
     `rodametria-produto.php` e o `teste-oferta-datada.php`.
  6. A SECAO MAE (`/veiculos/`), ACRESCENTADA EM 02/11/2026 no bloco que a poe no
     molde. Ela nao aparecia aqui porque este portao descobre as paginas CASANDO o
     sitemap com os slugs da vitrine — e a mae nao e uma consulta, entao nao tem
     linha na vitrine e CAIA FORA de todo portao de ar desta ilha. O que ele cobra
     nela: a CAIXA DE RESPOSTA da 32.2 existe e vem ANTES dos cartoes; o numero
     dela e a SOMA dos anuncios das filhas publicadas, contada aqui da fonte;
     nenhum molde `{...}` cru na tela; o botao de cada familia cai no `#comprar` de
     uma URL que esta no sitemap; e ZERO link patrocinado, porque a mae nao vende
     nada e link de afiliado fora de bloco de compra e reprovacao da 32.5.

ELE DESCOBRE AS URLs NO `wp-sitemap.xml` LIDO NO AR, nunca de uma lista, pela
frase da 32.5-b: "regua que nao varre todas certifica a pagina que o autor
abriu". Pagina de vitrine nova entra no dia em que desembarca.
"""
import html as html_lib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)
DOMINIO = "https://rodametria.com.br"

falhas = []
registros = []
afirmacoes = 0


def afirma(cond, msg):
    global afirmacoes
    afirmacoes += 1
    if not cond:
        falhas.append(msg)
    return bool(cond)


def registro(msg):
    registros.append(msg)


def buscar(caminho):
    """Quebra de cache sempre: as afirmacoes daqui sao sobre a ORIGEM."""
    url = DOMINIO + caminho
    url += ("&" if "?" in caminho else "?") + "v=" + str(int(time.time() * 1000))
    req = urllib.request.Request(url, headers={
        "User-Agent": "rodametria-conferir/1.0",
        "Accept-Encoding": "identity",
    })
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")
    except Exception as e:
        return 0, "ERRO: %s" % e


def corpo_da_pagina(html):
    """So o CORPO: `<script>` fora, senao a afirmacao sobre o que a pagina DIZ
    se acha dentro do proprio JSON-LD."""
    m = re.search(r"<body[^>]*>(.*)</body>", html, re.S | re.I)
    corpo = m.group(1) if m else html
    corpo = re.sub(r"<script.*?</script>", " ", corpo, flags=re.S | re.I)
    corpo = re.sub(r"<style.*?</style>", " ", corpo, flags=re.S | re.I)
    return corpo


def urls_do_sitemap():
    """TODA URL do sitemap, lida no ar. O sitemap do WordPress e um indice."""
    cod, xml = buscar("/wp-sitemap.xml")
    if cod != 200:
        return cod, []
    urls = []
    for sub in re.findall(r"<loc>([^<]+)</loc>", xml):
        if "wp-sitemap" in sub:
            c2, x2 = buscar(sub.replace(DOMINIO, ""))
            if c2 == 200:
                urls += re.findall(r"<loc>([^<]+)</loc>", x2)
        else:
            urls.append(sub)
    return cod, sorted(set(urls))


def vitrine_do_repositorio():
    """A FONTE, lida do repositorio: o que a tela DEVIA servir."""
    with open(os.path.join(ILHA, "dados", "vitrine-de-produto.json"), encoding="utf-8") as f:
        d = json.load(f)
    return {p["slug"]: p for p in d.get("paginas", []) if p.get("slug")}


def normalizar(t):
    """O NOME COMO ELE E COMPARAVEL, e as tres normalizacoes sao CICATRIZ.

    (1) `unescape`, porque `esc_html()` troca a aspa reta por `&quot;` e um
        titulo desta vitrine tem `10"`.
    (2) espaco colapsado, porque dois titulos trazem ESPACO DUPLO da loja.
    (3) TRAVESSAO VIRA HIFEN, e esta e a que vale registro: o WordPress roda os
        filtros do `the_content` sobre o retorno do shortcode, e o `wptexturize`
        troca o hifen CERCADO DE ESPACOS por EN DASH. Medido em 30/10/2026 no
        `patinete-eletrico`: o dado diz `550W - 40km/h` e o corpo serve
        `550W &#8211; 40km/h`. O JSON-LD, que sai no `wp_head` e NAO passa por
        aquele filtro, serve o hifen cru — entao o MESMO nome sai de duas formas
        na MESMA pagina. Nao e defeito a consertar: e tipografia do WordPress, e
        brigar com ela custa mais do que vale. E a mesma pedra que esta ilha ja
        tem escrita no topo da casca ("o WordPress troca && por &#038;&#038; no
        retorno do shortcode"), num traje novo — e quem nao a souber escreve uma
        regua que reprova a pagina certa.
    """
    t = html_lib.unescape(str(t or ""))
    t = t.replace("\u2013", "-").replace("\u2014", "-")
    return re.sub(r"\s+", " ", t).strip()


def texto_do_corpo(html):
    """O texto que a PESSOA le, com as entidades JA DESFEITAS.

    O `unescape` nao e detalhe, e esta regua o aprendeu reprovando a pagina
    CERTA na primeira passada: `esc_html()` transforma a aspa reta em `&quot;`,
    e o anuncio `Patinete Eletrico Scooter 350W 10" com App` nunca casaria com o
    nome do dado. E a mesma pedra em que `conferir-institucional-no-ar.py`
    bateu, e o comentario dele diz por que ela importa: portao que reprova
    pagina certa e o caminho mais curto para alguem passar a ignora-lo.
    """
    return normalizar(re.sub(r"<[^>]+>", " ", corpo_da_pagina(html)))



def _sem_acento(t):
    import unicodedata
    t = unicodedata.normalize("NFD", str(t or "").lower())
    return "".join(c for c in t if unicodedata.category(c) != "Mn")


# OS TERMOS SAO OS MESMOS DO `gerar-vitrine-de-produto.py`, e a lista esta
# DUPLICADA de proposito: aquele portao julga o REPOSITORIO e este julga o AR, e
# ha um mundo entre os dois — prosa escrita direto no PHP, que a camada declarada
# nao ve. Lista unica num modulo compartilhado faria este portao medir o mesmo
# arquivo duas vezes e perder exatamente o caso que ele existe para pegar.
QUANTIFICADORES = (
    "quase nunca", "quase sempre", "quase todo", "quase toda", "quase todos",
    "quase todas", "quase ninguem", "quase nenhum", "quase nenhuma", "a maioria",
    "maioria", "a minoria", "minoria", "raramente", "costuma", "costumam",
    "na maior parte", "a maior parte", "maior parte", "boa parte", "grande parte",
    "geralmente", "normalmente", "em geral", "de modo geral", "via de regra",
    "tipicamente", "frequentemente", "na pratica", "poucos", "poucas", "muitos",
    "muitas",
    # A CLASSE DO SUPERLATIVO DE FREQUENCIA E DE VENDA, acrescentada em
    # 04/11/2026: ela NAO e quantificador e por isso a lista acima nao a via.
    # Medido no ar no mesmo dia, em TRES paginas de TRES camadas diferentes:
    # "a RECLAMACAO MAIS COMUM de quem compra sem fazer essa conta" (produto),
    # "a maneira MAIS COMUM de prometer um aparelho e entregar outro"
    # (institucional) e "e a lacuna MAIS COMUM do varejo" (F2, prosa em PHP).
    # Nenhuma das tres tem um digito e nenhuma tem um quantificador — as duas
    # travas anteriores aprovavam as tres. Venda entra na mesma lista porque a
    # secao 7 proibe afirmacao de venda na tela, e "vende mais" e a forma dela
    # sem numero. "a media" entra porque media e distribuicao, e esta ilha nao
    # mede distribuicao de nada: ela conta titulos.
    "mais comum", "mais comuns", "mais vendido", "mais vendida",
    "mais vendidos", "mais vendidas", "vende mais", "vendem mais",
    "mais popular", "mais populares", "a media", "na media", "da media",
)


def ancoras_liberadas():
    """Os pedacos LITERAIS dentro dos quais um quantificador esta liberado.

    Lidos da camada declarada, nunca escritos aqui: quem libera uma frase responde
    por escrito no arquivo, e `gerar-vitrine-de-produto.py --conferir` cobra que a
    ancora exista no texto e contenha o proprio termo.
    """
    with open(os.path.join(ILHA, "dados", "paginas-de-produto.json"), encoding="utf-8") as f:
        d = json.load(f)
    return tuple(sorted({
        _sem_acento(q.get("ancora_no_ar") or "")
        for q in d.get("quantificadores_declarados_permitidos", [])
        if (q.get("ancora_no_ar") or "").strip()}))


def conferir_quantificadores(caminho, texto, ancoras):
    """A CLASSE NO AR, EM TODA PAGINA DESTE MOTOR — e ela substitui a afirmacao
    que nomeava UMA frase.

    POR QUE ELA NASCEU ASSIM, e a causa esta medida duas vezes em dois dias:

      03/11 — a pagina do patinete servia "a carga maxima QUASE NUNCA ESTA NO
              TITULO" com SEIS dos DEZESSEIS declarando. O conserto trocou a
              frase por uma contagem e escreveu, aqui, uma afirmacao que nomeava
              a frase aposentada inteira.
      04/11 — a MESMA afirmacao estava viva na secao MAE, servida o dia inteiro.
              A afirmacao de 03/11 nao a pegou porque ela morava no laco das
              FILHAS, e a mae nao e uma delas — e o cabecalho deste portao JA
              DIZIA que a mae "caia fora de todo portao de ar desta ilha", de um
              defeito identico de 02/11. A trava nomeava a INSTANCIA; o que
              envelhece e a CLASSE.

    Ela nao julga prosa (20.5): denuncia a ocorrencia e exige que ela esteja
    liberada por escrito, com ancora, na camada declarada.
    """
    t = _sem_acento(texto)
    for anc in ancoras:
        t = t.replace(anc, " ")
    for q in QUANTIFICADORES:
        i = t.find(q)
        while i >= 0:
            antes = t[i - 1] if i else " "
            depois = t[i + len(q):i + len(q) + 1] or " "
            if not (antes.isalpha() or depois.isalpha()):
                afirma(False,
                       "%s serve uma PROPORCAO por extenso (%r) que nao esta liberada na "
                       "camada declarada: %r — prosa que afirma o estado do catalogo "
                       "envelhece calada, e foi assim que a frase da carga ficou cinco dias "
                       "no ar na filha e um dia na mae"
                       % (caminho, q, texto[max(0, i - 60):i + 80]))
                return
            i = t.find(q, i + 1)
    afirma(True, "")
    registro("%s: zero quantificador por extenso fora da lista liberada" % caminho)

ROTULO_DO_PISO = "Veja todos disponíveis aqui"

# A LINHA DO PISO DA TABELA SE CONTA PELA CLASSE, NUNCA PELA FRASE, e a primeira
# versao desta regua contou pela frase e reprovou a pagina certa: a MESMA frase e
# a linha discreta de cada CARTAO do carrossel (25.2), entao ela aparece 5 vezes
# numa pagina sa antes de a tabela existir. Contar a frase e medir duas coisas
# diferentes com a mesma regua — a familia das sete reguas desta fabrica que
# quebraram por procurar o rotulo de UM degrau.
CLASSE_DO_PISO_DA_TABELA = 'class="rdm-tabela-piso"'


def main():
    ancoras = ancoras_liberadas()
    cod, urls = urls_do_sitemap()
    if not afirma(cod == 200, "o wp-sitemap.xml nao respondeu 200 (deu %s)" % cod):
        return encerrar()

    fonte = vitrine_do_repositorio()
    afirma(bool(fonte), "dados/vitrine-de-produto.json nao tem pagina nenhuma")

    # AS PAGINAS DE VITRINE SE DESCOBREM PELO CASAMENTO entre o sitemap no ar e
    # os slugs da fonte — nunca por uma lista digitada aqui.
    # O `slug` da fonte e o CAMINHO INTEIRO (`veiculos/patinete-eletrico`), nao a
    # ultima parte — e a primeira versao desta regua comparou a ultima parte e
    # achou ZERO pagina, denunciando-se com "este portao ficou cego" em vez de
    # aprovar em silencio. E o que a 32.5-b pede: regua que nao varre todas diz
    # que nao varreu.
    alvos = []
    for u in urls:
        caminho = u.replace(DOMINIO, "")
        slug = caminho.strip("/")
        if slug in fonte:
            alvos.append((caminho, slug))

    if not afirma(alvos, "nenhuma pagina de vitrine achada no sitemap: este portao ficou cego"):
        return encerrar()
    registro("paginas de vitrine descobertas no sitemap: %d (%s)"
             % (len(alvos), ", ".join(s for _, s in alvos)))

    for caminho, slug in alvos:
        pg = fonte[slug]
        linhas = pg.get("linhas", [])
        cod, html = buscar(caminho)
        if not afirma(cod == 200, "%s nao respondeu 200 (deu %s)" % (caminho, cod)):
            continue
        corpo = corpo_da_pagina(html)

        # (1) O href VAZIO, e ele e medido no HTML INTEIRO e nao so no corpo.
        vazios = len(re.findall(r'href=""', html)) + len(re.findall(r"href=''", html))
        afirma(vazios == 0,
               "%s serve %d href vazio: botao que recarrega a propria pagina" % (caminho, vazios))

        # (2) A LINHA DISCRETA DO PISO, uma vez.
        buscas = {str(l.get("url_busca") or "").strip() for l in linhas}
        buscas.discard("")
        quantos = corpo.count(CLASSE_DO_PISO_DA_TABELA)
        nos_cartoes = corpo.count(ROTULO_DO_PISO) - quantos
        if len(buscas) == 1:
            afirma(quantos == 1,
                   "%s serve a linha do piso da TABELA %d vez(es) e devia servir UMA: o piso e da "
                   "consulta, nao do anuncio" % (caminho, quantos))
            afirma(list(buscas)[0] in corpo,
                   "%s nao serve o piso da 25.2 (%s)" % (caminho, list(buscas)[0]))
        else:
            afirma(quantos == 0,
                   "%s tem %d buscas distintas na fonte e ainda serve a linha unica do piso da "
                   "tabela: 'a primeira' e arbitraria" % (caminho, len(buscas)))

        # (3) TODO anuncio NOMEADO, e TODO anuncio com saida de compra.
        texto = texto_do_corpo(html)
        for l in linhas:
            # OS DOIS LADOS PASSAM PELA MESMA NORMALIZACAO, nunca um so: regua
            # que normaliza metade reprova a pagina certa (ver `normalizar`).
            nome = normalizar(l.get("nome"))
            afirma(nome in texto,
                   "%s nao nomeia o anuncio %r: a secao 7 manda nomear todo item uma vez"
                   % (caminho, nome[:40]))
            saida = str(l.get("url") or "").strip() or str(l.get("url_busca") or "").strip()
            afirma(saida != "",
                   "%s: o anuncio %r nao tem saida de compra NENHUMA no dado — defeito da 19.1 "
                   "pela 25.2" % (caminho, nome[:40]))
            if saida:
                afirma(saida in corpo,
                       "%s: a saida de compra do anuncio %r nao esta no ar" % (caminho, nome[:40]))
        afirma("rdm-tabela" in corpo, "%s nao serve a tabela pre-renderizada (32.1 item 6)" % caminho)
        afirma("sem link de compra hoje" not in corpo,
               "%s serve celula 'sem link de compra hoje': ha anuncio sem saida no ar" % caminho)

        # (3-b) A COLUNA DA CARGA MAXIMA — 03/11/2026, e as quatro afirmacoes
        # abaixo existem por um defeito MEDIDO NO AR naquele dia: esta pagina
        # servia, na dobra "Qual escolher", a frase declarada "a carga maxima
        # declarada e o primeiro filtro, e ela QUASE NUNCA ESTA NO TITULO",
        # enquanto SEIS dos DEZESSEIS anuncios dela a declaravam no titulo, de 60
        # a 150 kg. Nenhum portao podia pegar aquilo, porque nenhum comparava a
        # prosa declarada com o que a regua le dos titulos.
        afirma("Carga máxima no título" in corpo,
               "%s nao serve a coluna de carga maxima da tabela" % caminho)
        celulas = corpo.count('class="rdm-tabela-carga"')
        afirma(celulas == len(linhas),
               "%s serve %d celula(s) de carga para %d linha(s): a coluna nao cobre a tabela"
               % (caminho, celulas, len(linhas)))
        # A FRASE E A CONTADA, byte por byte. Se a camada declarada voltar a
        # escrever a mao o estado do catalogo, o molde deixa de ser preenchido com
        # ela e esta afirmacao fica vermelha.
        frase = str(pg["numeros"].get("frase_da_carga") or "")
        afirma(frase != "", "%s: a vitrine do repositorio nao tem frase_da_carga" % caminho)
        afirma(normalizar(frase) in normalizar(texto),
               "%s nao serve a frase contada da carga: %r" % (caminho, frase[:70]))
        # A FRASE CONTADA DO PIVO DA F1 — 04/11/2026, e e a contagem que mais
        # vale nesta ilha: hoje ZERO dos 22 anuncios que ela publica diz se o
        # veiculo tem acelerador, que e o que decide se precisa de habilitacao.
        pivo = str(pg["numeros"].get("frase_do_pivo") or "")
        afirma(pivo != "", "%s: a vitrine do repositorio nao tem frase_do_pivo" % caminho)
        afirma(normalizar(pivo) in normalizar(texto),
               "%s nao serve a frase contada do pivo da F1: %r" % (caminho, pivo[:70]))
        dobr = str(pg["numeros"].get("frase_do_dobravel") or "")
        afirma(dobr != "", "%s: a vitrine do repositorio nao tem frase_do_dobravel" % caminho)

        # A CLASSE, NAO A FRASE APOSENTADA. A versao anterior desta afirmacao
        # nomeava "quase nunca esta no titulo" e vigiava SO as filhas; a mesma
        # frase viveu um dia na secao mae por isso. A varredura esta numa funcao
        # unica, chamada daqui E de `conferir_a_mae`.
        conferir_quantificadores(caminho, texto, ancoras)

        # (4) rel e target em TODO link de afiliado.
        for a in re.findall(r"<a[^>]*s\.shopee\.com\.br[^>]*>", corpo):
            afirma('rel="sponsored noopener"' in a,
                   "%s: link de afiliado sem rel sponsored: %s" % (caminho, a[:90]))
            afirma('target="_blank"' in a,
                   "%s: link de afiliado sem target _blank: %s" % (caminho, a[:90]))

        # (5) O JSON-LD, que e o lugar mais silencioso dos tres: `"url": ""` numa
        #     `Offer` e dado estruturado invalido que olho humano nao ve.
        ofertas = 0
        com_disponibilidade = 0
        com_data = 0
        for bloco in re.findall(
                r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
            try:
                dado = json.loads(bloco)
            except Exception:
                afirma(False, "%s serve JSON-LD que nao parseia" % caminho)
                continue
            if not isinstance(dado, dict) or dado.get("@type") != "ItemList":
                continue
            itens = dado.get("itemListElement") or []
            afirma(len(itens) == len(linhas),
                   "%s: o ItemList tem %d itens e a vitrine tem %d linhas"
                   % (caminho, len(itens), len(linhas)))
            for i, it in enumerate(itens):
                of = ((it or {}).get("item") or {}).get("offers") or {}
                if not of:
                    continue
                ofertas += 1
                afirma(str(of.get("url") or "").strip() != "",
                       "%s: uma Offer do JSON-LD esta com url vazia" % caminho)
                if of.get("availability"):
                    com_disponibilidade += 1
                # A OFERTA DATADA, NO AR — 12/11/2026. A regua e a mesma que o
                # `teste-oferta-datada.php` aplica do chao sobre a funcao; aqui
                # ela mede o que o WordPress SERVIU, que e a camada que a visao
                # geral de IA ingere sem abrir a pagina (32.4-c). A data
                # esperada sai da linha da vitrine de MESMA POSICAO — o
                # `ItemList` e ordenado pela mesma lista, e a afirmacao de
                # contagem logo acima e o que torna o pareamento por indice
                # legitimo.
                esperada = ""
                if i < len(linhas):
                    esperada = str(linhas[i].get("preco_colhido_em") or "")
                afirma("priceValidUntil" not in of,
                       "%s: uma Offer declara priceValidUntil — validade FUTURA que esta ilha "
                       "nao mediu" % caminho)
                if not esperada:
                    afirma("priceSpecification" not in of,
                           "%s: a linha %d nao tem data de coleta e a Offer serve uma "
                           "priceSpecification" % (caminho, i + 1))
                    continue
                ps = of.get("priceSpecification") or {}
                afirma(bool(ps),
                       "%s: a Offer da linha %d serve `price` CRU, sem a data da coleta, "
                       "enquanto a tela diz %r ao lado do mesmo numero"
                       % (caminho, i + 1, linhas[i].get("preco_nota")))
                if not ps:
                    continue
                com_data += 1
                afirma(ps.get("@type") == "UnitPriceSpecification",
                       "%s: a priceSpecification da linha %d nao e UnitPriceSpecification"
                       % (caminho, i + 1))
                afirma(ps.get("validFrom") == esperada,
                       "%s: o `validFrom` da linha %d e %r e a data da coleta e %r"
                       % (caminho, i + 1, ps.get("validFrom"), esperada))
                afirma(ps.get("price") == of.get("price"),
                       "%s: os dois `price` da Offer da linha %d discordam (%r e %r)"
                       % (caminho, i + 1, of.get("price"), ps.get("price")))
                # AS DUAS SUPERFICIES DIZEM A MESMA DATA, no HTML servido: a
                # frase que o leitor le e o campo que a maquina recebe. Enquanto
                # a data existia so em portugues, nao havia como afirmar isto.
                br = "%s/%s/%s" % (esperada[8:10], esperada[5:7], esperada[0:4])
                afirma(br in str(linhas[i].get("preco_nota") or ""),
                       "%s: a nota da tela da linha %d (%r) nao diz a data que o JSON-LD serve "
                       "(%s)" % (caminho, i + 1, linhas[i].get("preco_nota"), br))
                afirma(br in corpo,
                       "%s: a data %s do `validFrom` da linha %d nao aparece no corpo servido — "
                       "a tela e o dado divergiram" % (caminho, br, i + 1))
        afirma(ofertas == len(linhas),
               "%s: o JSON-LD serve %d Offer(s) e a vitrine tem %d linhas"
               % (caminho, ofertas, len(linhas)))
        # ZERO, E ESTE ZERO E A REGRA E NAO UM ACIDENTE DO DADO DE HOJE.
        # Ate 12/11/2026 esta afirmacao cobrava `availability` em toda linha com
        # ficha. Ficha EXISTIR nao e estar VENDENDO: a garantia desta ilha e
        # "nenhuma ficha foi medida esgotada na ULTIMA LEITURA" — afirmacao
        # datada, e `availability` nao tem data. A ronda de 11/11/2026 achou UMA
        # ficha esgotada entre 24.
        com_ficha = sum(1 for l in linhas if str(l.get("url") or "").strip())
        afirma(com_disponibilidade == 0,
               "%s: %d Offer(s) declaram availability — promessa de estoque no presente do "
               "indicativo sobre leitura de dias atras" % (caminho, com_disponibilidade))
        afirma(com_data == ofertas,
               "%s: %d de %d Offer(s) dizem a data do preco" % (caminho, com_data, ofertas))

        registro("%s: %d linha(s), %d com ficha, %d href vazio, piso da tabela %dx, a MESMA frase "
                 "%dx nos cartoes do carrossel, %d Offer(s) (%d com availability, %d datadas)"
                 % (caminho, len(linhas), com_ficha, vazios, quantos, nos_cartoes, ofertas,
                    com_disponibilidade, com_data))

    conferir_a_mae(urls, fonte, ancoras)

    registro("NAO MEDIDO AQUI: pixel. A 32.5 e trabalho de "
             "conferir-32-5-no-navegador.mjs, que abre a pagina a 390 px num navegador.")
    return encerrar()


def conferir_a_mae(urls, fonte, ancoras):
    """A SECAO MAE, que nao tinha portao de ar nenhum ate 02/11/2026.

    O numero da caixa dela e AGREGADO das filhas, entao ele se confere de um jeito
    que nenhuma outra pagina desta ilha permite: somando a fonte do repositorio e
    comparando com o que a tela diz. Numero de tela contado contra a fonte e a
    unica forma de a secao 8 ser obedecida numa pagina que fala do estado do banco.
    """
    caminho = "/veiculos/"
    if not afirma(DOMINIO + caminho in urls,
                  "a secao mae nao esta no wp-sitemap.xml"):
        return

    cod, html = buscar(caminho)
    if not afirma(cod == 200, "%s nao respondeu 200 (deu %s)" % (caminho, cod)):
        return
    corpo = corpo_da_pagina(html)

    # (a) A CAIXA DE RESPOSTA EXISTE. Ate 02/11 ela NAO existia, e o portao de
    #     pixel listava esta pagina como "sem componente de molde nenhum" — o que
    #     significa que os 700 px da 32.5 nunca a julgaram (32.5-c).
    # A CAIXA SE CONTA PELO CONTEINER, NUNCA PELO PREFIXO DA CLASSE, e esta regua
    # aprendeu isso REPROVANDO A PAGINA CERTA na primeira passada depois do
    # desembarque: `class="rdm-molde-caixa` casa tambem
    # `rdm-molde-caixa-rotulo`, `-numero`, `-unidade` e cada `-frase`, entao uma
    # caixa sa com tres frases contava SETE. E a mesma pedra da linha do piso da
    # tabela ("se conta pela CLASSE, nunca pela frase") com o sinal invertido —
    # aqui a classe e prefixo de outras seis. Portao que reprova pagina certa e o
    # caminho mais curto para alguem passar a ignora-lo (20.5).
    caixas = len(re.findall(r'class="rdm-molde-caixa rdm-molde-caixa-(?:verde|alerta|neutro)"',
                            corpo))
    afirma(caixas == 1,
           "%s serve %d caixa de resposta do molde (a 32.2 pede uma)" % (caminho, caixas))

    # (b) E ELA VEM ANTES DOS CARTOES. "Caixa no topo" e ordem, nao presenca:
    #     caixa depois da lista passaria a afirmacao (a) e reprovaria a 32.2.
    i_caixa = corpo.find("rdm-molde-caixa")
    i_cartoes = corpo.find('class="rdm-cartoes"')
    afirma(i_caixa != -1 and i_cartoes != -1 and i_caixa < i_cartoes,
           "%s nao serve a caixa de resposta ANTES dos cartoes das familias" % caminho)

    # (c) O NUMERO DA CAIXA E A SOMA DAS FILHAS PUBLICADAS, contada da fonte.
    #     So entram as familias que estao no sitemap: a vitrine pode trazer uma
    #     familia que ainda nao desembarcou, e somar o que a tela nao mostra seria
    #     cobrar da pagina um numero que ela nao tem como ter.
    no_ar = [p for slug, p in fonte.items()
             if DOMINIO + "/" + slug + "/" in urls]
    soma = sum(int(p.get("numeros", {}).get("n") or 0) for p in no_ar)
    m = re.search(r'class="rdm-molde-caixa-numero"[^>]*>\s*<span class="rdm-num">([^<]+)</span>',
                  corpo)
    if afirma(m is not None, "%s nao serve o numero da caixa em Mono" % caminho):
        afirma(normalizar(m.group(1)) == str(soma),
               "%s diz %r anuncios na caixa e a fonte das %d familia(s) no ar soma %d"
               % (caminho, normalizar(m.group(1)), len(no_ar), soma))

    # (d) NENHUM MOLDE CRU NA TELA. A prosa da caixa vem da camada declarada com
    #     moldes, e molde que o preenchedor nao conhece sai literal para quem le —
    #     a cicatriz que `teste-institucional.py` ja cobra na irma institucional.
    crus = re.findall(r"\{[A-Z_]{2,}\}", texto_do_corpo(html))
    afirma(not crus, "%s serve molde cru na tela: %s" % (caminho, ", ".join(sorted(set(crus)))))

    # (d-2) A CLASSE, NA MAE, PELA MESMA FUNCAO QUE JULGA AS FILHAS — 04/11/2026.
    #     Esta e a afirmacao que faltava, e a falta tem data: a frase declarada
    #     "o filtro que quase ninguem olha e que QUASE NUNCA ESTA NO TITULO" foi
    #     aposentada da pagina do patinete em 03/11 e serviu NESTA pagina o dia
    #     inteiro depois disso, com SEIS dos DEZESSEIS anuncios da filha
    #     declarando a carga no titulo. O portao escrito em 03/11 para impedir o
    #     retorno dela nomeava a frase e vivia no laco das FILHAS.
    conferir_quantificadores(caminho, texto_do_corpo(html), ancoras)

    # (d-3) A FRASE DA CARGA DA MAE E A CONTADA, AGREGADA DAS FILHAS NO AR, e ela
    #     se recalcula aqui da fonte em vez de ser lida de campo gravado — a mae
    #     nao tem arquivo gerado, o numero dela nasce em PHP na hora de servir.
    declaram = sum(int(p.get("numeros", {}).get("declaram_carga") or 0) for p in no_ar)
    valores = [p["numeros"][k] for p in no_ar for k in ("carga_de", "carga_ate")
               if p.get("numeros", {}).get(k) is not None]
    if declaram and valores:
        menor, maior = min(valores), max(valores)
        esperado = ("%d dos %d anúncios desta seção declaram a carga máxima no título"
                    % (declaram, soma))
        afirma(normalizar(esperado) in normalizar(texto_do_corpo(html)),
               "%s nao serve a contagem agregada da carga: %r" % (caminho, esperado))
        afirma(("de %d a %d kg" % (menor, maior)) in texto_do_corpo(html),
               "%s nao serve a faixa agregada da carga (de %d a %d kg)"
               % (caminho, menor, maior))
    else:
        afirma(("Nenhum dos %d" % soma) in texto_do_corpo(html),
               "%s: nenhuma filha declara carga e a mae nao diz isso" % caminho)

    # (e) O BOTAO DE CADA FAMILIA CAI NO BLOCO DE COMPRA DELA, e o alvo existe.
    #     Link interno para 404 e o defeito que a casca desta ilha publica a rota
    #     `/casca` para ninguem precisar adivinhar.
    botoes = re.findall(r'<a class="rdm-molde-cartao-botao" href="([^"]+)"', corpo)
    afirma(len(botoes) == len(no_ar),
           "%s serve %d botao de familia para %d familia(s) no ar"
           % (caminho, len(botoes), len(no_ar)))
    for u in botoes:
        afirma(u.endswith("#comprar"),
               "%s: o botao da familia nao cai no bloco de compra: %s" % (caminho, u))
        afirma(u.split("#")[0] in urls,
               "%s: o botao da familia aponta para fora do sitemap: %s" % (caminho, u))

    # (f) ZERO href VAZIO e ZERO LINK PATROCINADO. A mae nao vende nada; link de
    #     afiliado FORA de um bloco de compra e reprovacao no portao de pixel,
    #     porque sem o componente o teto de 1.400 px nao teria o que medir.
    vazios = len(re.findall(r'href=""', html)) + len(re.findall(r"href=''", html))
    afirma(vazios == 0, "%s serve %d href vazio" % (caminho, vazios))
    patrocinados = len(re.findall(r'rel="[^"]*sponsored', html))
    afirma(patrocinados == 0,
           "%s serve %d link patrocinado e nao tem bloco de compra" % (caminho, patrocinados))

    registro("%s: %d caixa de resposta (numero %s = soma das %d familia(s) no ar), "
             "%d botao(oes) de familia para o #comprar da filha, %d molde cru, "
             "%d link patrocinado"
             % (caminho, caixas, m.group(1) if m else "?", len(no_ar),
                len(botoes), len(crus), patrocinados))


def encerrar():
    for r in registros:
        print("  . %s" % r)
    print("")
    for f in falhas:
        print("FALHA %s" % f)
    print("")
    print("%d afirmacao(oes), %d falha(s)." % (afirmacoes, len(falhas)))
    print("APROVADO" if not falhas else "REPROVADO")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
