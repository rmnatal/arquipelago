#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mede NO AR o bloco 4d: o painel da artesa e a Loja.

    python3 ferramentas/conferir-atelie-no-ar.py [TOKEN_DO_SYNC]

POR QUE ESTE ARQUIVO EXISTE SEPARADO do `conferir-no-ar.py`: aquele mede as onze
URLs no caso-ANCORA, e este bloco trouxe duas coisas que o caso-ancora nao
alcanca — uma pagina que muda de cara conforme QUEM abre (o painel), e uma URL
que so existe quando a artesa publica uma peca (a ficha). E a mesma razao pela
qual a Robometria escreveu o `conferir-kits-no-ar.py` em 12/09/2026.

O QUE ELE PROVA, e o que ele NAO pode provar:

  PROVA — que /atelie/ responde 200 e serve a tela de entrar; que ela sai com
  `noindex` e FORA do sitemap; que nenhuma pagina publica linka para ela; que a
  usuaria existe, com o papel certo, e a que hora o e-mail de acesso saiu; que a
  Loja esta de pe e que a contagem de pecas que o site declara bate com a que a
  rota conta; e que cada peca publicada serve ficha, description, og: e
  Product+Offer.

  NAO PROVA — que o e-mail CHEGOU na caixa da Hotmail, nem que o dedo dela
  funciona na tela de 360 px. `wp_mail` devolvendo true diz que o servidor
  ACEITOU a mensagem, nao que ela passou do filtro de spam. Isso fica escrito no
  relatorio como o que falta, nunca como conferido.

A REGUA E DESTE ARQUIVO: os endereços, o papel esperado e as sete capacidades
estao escritos literais aqui, copiados do despacho, nunca lidos do snippet.

O TOKEN vem do argumento ou da variavel CDM_SYNC_TOKEN. Sem ele as afirmacoes
que dependem de rota protegida sao PULADAS e contadas como puladas — nunca como
aprovadas, que e a diferenca entre "nao medi" e "esta bom".
"""

import json
import os
import re
import subprocess
import sys
import time

BASE = "https://clubedomosaico.com.br"
PAINEL = "/atelie/"

# As sete capacidades do papel `artesa`, copiadas do despacho de 10/09/2026.
# Escritas aqui de proposito: ler do snippet seria conferir o snippet com ele mesmo.
CAPS_ESPERADAS = {
    "read", "upload_files", "edit_pecas", "publish_pecas", "delete_pecas",
    "edit_published_pecas", "delete_published_pecas",
}
# E as que ela NAO pode ter de jeito nenhum.
CAPS_PROIBIDAS = {
    "manage_options", "edit_others_pecas", "delete_others_pecas",
    "edit_posts", "edit_pages", "edit_theme_options", "install_plugins", "list_users",
}
# As paginas publicas que NAO podem linkar para o painel.
PUBLICAS = ["/", "/loja/", "/materiais/", "/como-fazer/", "/sobre/", "/contato/",
            "/divulgacao-de-afiliados/", "/privacidade/"]

falhas = 0
feitos = 0
pulados = 0


def ok(cond, rotulo, medida=""):
    global falhas, feitos
    feitos += 1
    print(("  ok    " if cond else "  FALHA ") + rotulo.ljust(62) + " " + str(medida))
    if not cond:
        falhas += 1


def pular(rotulo, porque):
    global pulados
    pulados += 1
    print("  PULADO " + rotulo.ljust(62) + " " + porque)


def buscar(url):
    """GET com `?v=` contra o cache duplo da secao 4 do ARQUIPELAGO.md."""
    v = str(int(time.time()))
    sep = "&" if "?" in url else "?"
    r = subprocess.run(["curl", "-s", "--max-time", "40", "-w", "\n%{http_code}", url + sep + "v=" + v],
                       capture_output=True, text=True)
    partes = r.stdout.rsplit("\n", 1)
    return partes[0], (partes[1] if len(partes) > 1 else "000")


def corpo_visivel(html):
    """O que a pessoa VE: dentro de <main>, sem folha e sem script.

    ESCRITO DEPOIS DE ERRAR, na primeira passada no ar de 12/09/2026. A contagem
    de cartoes da vitrine procurava `cdm-card-peca` no HTML INTEIRO e achou 6 numa
    Loja com ZERO peca publicada — as seis eram os seletores da propria folha de
    estilo do snippet. E literalmente o erro que a secao 8 do ARQUIPELAGO.md
    nomeia ("afirmacao sobre o que a pagina diz se mede no CORPO, nunca no HTML
    completo", a mesma familia de contar &#038; na pagina inteira), cometido por
    quem acabara de escrever um teste de bancada que faz isso certo. Vale
    registrar: a bancada media no corpo e o conferidor no ar nao, e nada obrigava
    os dois a concordarem.
    """
    m = re.search(r"<main.*?>(.*?)</main>", html, re.S)
    c = m.group(1) if m else ""
    c = re.sub(r"<style.*?</style>", "", c, flags=re.S)
    c = re.sub(r"<script.*?</script>", "", c, flags=re.S)
    return c


def token():
    if len(sys.argv) > 1 and sys.argv[1].strip():
        return sys.argv[1].strip()
    return os.environ.get("CDM_SYNC_TOKEN", "").strip()


def main():
    tk = token()

    print("\nNO AR — bloco 4d: o painel da artesa e a Loja")
    print("-" * 78)

    # ---------------------------------------------------------------- o painel
    print("\n1. /atelie/ responde, e responde a tela de entrar")
    html, codigo = buscar(BASE + PAINEL)
    ok("200" == codigo, "[/atelie/] HTTP 200", codigo)

    corpo = corpo_visivel(html)
    ok(corpo != "", "[/atelie/] a pagina tem corpo", f"{len(corpo)} caracteres")
    ok("Entrar no meu ateliê" in corpo, "[/atelie/] quem nao entrou ve a tela de entrar")
    ok('name="cdm_senha"' in corpo, "[/atelie/] a tela tem campo de senha")
    ok("Esqueci minha senha" in corpo, "[/atelie/] e oferece recuperar a senha")

    # O QUE NAO PODE APARECER PARA QUEM NAO ENTROU.
    for palavra in ("Nova peça", "Minhas peças", "Olá,"):
        ok(palavra not in corpo, f"[/atelie/] deslogada NAO ve '{palavra}'")
    # E O PORTAO LITERAL DO DESPACHO.
    for palavra in ("WordPress", "wp-admin", "wp-login"):
        ok(palavra.lower() not in corpo.lower(), f"[/atelie/] o corpo nao diz '{palavra}'")

    print("\n2. O painel esta FORA do indice e FORA do sitemap")
    ok('content="noindex, follow"' in html, "[/atelie/] serve noindex, follow")

    mapa, cod_mapa = buscar(BASE + "/wp-sitemap.xml")
    ok("200" == cod_mapa, "[sitemap] o indice responde 200", cod_mapa)
    # O indice do sitemap aponta para os sub-mapas; e neles que a URL apareceria.
    urls_do_mapa = set()
    for sub in re.findall(r"<loc>([^<]+)</loc>", mapa):
        if "sitemap" not in sub:
            urls_do_mapa.add(sub.split("?")[0])
            continue
        filho, _ = buscar(sub)
        for u in re.findall(r"<loc>([^<]+)</loc>", filho):
            urls_do_mapa.add(u.split("?")[0])
    ok(len(urls_do_mapa) > 0, "[sitemap] o sitemap tem URLs", f"{len(urls_do_mapa)} URLs")
    ok(BASE + PAINEL not in urls_do_mapa, "[sitemap] /atelie/ NAO esta no sitemap")

    print("\n3. Nenhuma pagina publica linka para o painel")
    citam = []
    for p in PUBLICAS:
        h, c = buscar(BASE + p)
        if "200" != c:
            ok(False, f"[{p}] HTTP 200", c)
            continue
        if re.search(r'href="[^"]*' + re.escape(PAINEL) + r'"', h):
            citam.append(p)
    ok(not citam, "nenhuma das paginas publicas linka /atelie/",
       "0 links" if not citam else ", ".join(citam))

    # ------------------------------------------------------------------- a loja
    print("\n4. A Loja de pe, e a contagem que o site declara")
    loja_html, loja_cod = buscar(BASE + "/loja/")
    ok("200" == loja_cod, "[/loja/] HTTP 200", loja_cod)

    conta, conta_cod = buscar(BASE + "/wp-json/clubedomosaico/v1/loja")
    dados = {}
    if "200" == conta_cod:
        try:
            dados = json.loads(conta)
        except ValueError:
            dados = {}
    ok("200" == conta_cod and isinstance(dados, dict) and "publicadas" in dados,
       "[rota] a contagem publica da Loja responde", conta_cod)

    publicadas = int(dados.get("publicadas", -1)) if dados else -1
    rascunhos = int(dados.get("rascunhos", -1)) if dados else -1
    print(f"     -> {publicadas} peca(s) publicada(s), {rascunhos} rascunho(s)")

    # A TELA E A ROTA TEM DE CONCORDAR. Duas metades lendo o mesmo banco: se
    # divergirem, uma delas esta servindo cache velho — e e assim que o site fica
    # para tras em silencio (secao 4).
    loja_corpo = corpo_visivel(loja_html)
    cartoes = len(re.findall(r'<li class="cdm-card cdm-card-peca"', loja_corpo))
    if publicadas >= 0:
        if publicadas == 0:
            ok(cartoes == 0 and "cdm-vazio" in loja_corpo,
               "[/loja/] sem peca publicada, a pagina serve o estado vazio honesto",
               f"{cartoes} cartoes no corpo")
            ok("em breve" in loja_corpo.lower(),
               "[/loja/] e o estado vazio nao inventa peca nenhuma")
        else:
            ok(cartoes == publicadas,
               "[/loja/] a vitrine mostra exatamente as pecas que a rota conta",
               f"{cartoes} cartoes / {publicadas} publicadas")
            ok("cdm-vazio" not in loja_corpo, "[/loja/] o estado vazio SOME quando ha peca")

    # ---------------------------------------------------- a ficha de cada peca
    # ------------------------------------------- o snippet de leads, no ar
    #
    # POR QUE ISTO EXISTE SEPARADO DA FICHA: o formulario do adendo 3 so aparece
    # numa pagina de peca, e hoje nao ha peca publicada — entao a secao 5 abaixo
    # PULA, e pular e honesto. O que nao seria honesto e fechar o bloco sem uma
    # unica medicao no ar do snippet que acabou de desembarcar. Estas duas
    # afirmacoes medem o que da para medir hoje: que o snippet esta ATIVO (a
    # folha dele sai no /atelie/, que e pagina dele tambem) e que ele NAO abriu
    # rota nenhuma de lead. A segunda e uma AUSENCIA, e ausencia so nao some
    # sozinha quando alguem a mede.
    print("\n4b. O snippet de leads (adendo 3)")
    at_html, at_cod = buscar(BASE + "/atelie/")
    ok("200" == at_cod and 'id="cdm-leads-folha"' in at_html,
       "[/atelie/] a folha do snippet de leads sai no ar (ele esta ATIVO)", at_cod)
    for rota in ("leads", "lead_peca", "interessados"):
        _, cod_lead = buscar(BASE + "/wp-json/clubedomosaico/v1/" + rota)
        ok(cod_lead in ("404", "401", "403"),
           f"[rota] /v1/{rota} NAO existe (lead nao sai por endpoint)", cod_lead)

    # ------------------------------------------ a aba "Meus dados" (1.2.0)
    #
    # A ABA SO EXISTE PARA QUEM ENTROU, e a Fundacao nao entra — a senha dela nao
    # existe para a nuvem, por desenho. Entao a pergunta que este bloco responde
    # nao e "a aba esta bonita", e sim a que o /status sozinho NAO responde: **a
    # versao nova do snippet esta mesmo servindo esta pagina?** A folha do painel
    # sai no /atelie/ mesmo deslogada, e `.cdm-at-secao` so existe no Atelie
    # 1.2.0 — e uma marca do CODIGO NOVO no corpo servido, que e a diferenca
    # entre "o manifest diz que subiu" e "o site esta servindo".
    #
    # A REGUA E DAQUI: o nome da classe e o endereco estao escritos nesta linha,
    # copiados do snippet uma vez, nunca lidos dele.
    print("\n4c. O Atelie 1.2.0 — a marca da versao nova no corpo servido")
    ok("200" == at_cod and ".cdm-at-secao{" in at_html,
       "[/atelie/] a folha traz .cdm-at-secao (so existe no Atelie 1.2.0)", at_cod)

    # E O ESTADO NOVO NA URL NAO PODE VAZAR NEM ENTRAR NO INDICE. Quem nao entrou
    # tem de cair na tela de entrar, como em qualquer outro estado do painel.
    md_html, md_cod = buscar(BASE + "/atelie/?estado=meus-dados")
    ok("200" == md_cod, "[/atelie/?estado=meus-dados] HTTP 200", md_cod)
    ok('content="noindex, follow"' in md_html,
       "[/atelie/?estado=meus-dados] serve noindex, follow")
    md_corpo = corpo_visivel(md_html)
    ok("Entrar no meu ateliê" in md_corpo,
       "[/atelie/?estado=meus-dados] deslogada cai na tela de entrar")
    for vazamento in ("trocar_senha", "cdm_email_leads", "cdm_artesa_nome", "mina196"):
        ok(vazamento not in md_html,
           f"[/atelie/?estado=meus-dados] deslogada NAO ve '{vazamento}'")

    # ------------------------------------ o despacho do Raphael de 14/09/2026
    #
    # A ARTESA USOU O PAINEL E ACHOU O QUE NENHUMA BANCADA ACHOU. Estas medicoes
    # sao no AR de proposito: as tres primeiras coisas do despacho so existem
    # como defeito no site servido — a bancada nao tem WordPress, e foi
    # justamente o WordPress que mordeu.
    #
    # A REGUA E DAQUI: o nome do parametro, o texto da faixa e a contagem de
    # tecnicas estao escritos nesta secao, nunca lidos dos snippets.
    print("\n4d. O despacho de 14/09 — o 404 ao publicar, a lista e a tecnica nova")

    # ITEM 1. `/atelie/?peca=24` caia no 404 do tema porque `peca` e o nome do
    # tipo de conteudo, registrado com `query_var`. O parametro virou `cdm_peca`.
    # Medido com um id que NAO existe de proposito: o que se mede e o roteamento,
    # nao a peca — se o nome colidir de novo, o 404 volta para qualquer numero.
    _, cod_novo = buscar(BASE + "/atelie/?cdm_peca=999999")
    ok("200" == cod_novo,
       "[/atelie/?cdm_peca=] o painel responde 200 com o parametro de peca na URL", cod_novo)
    _, cod_velho = buscar(BASE + "/atelie/?peca=999999")
    print(f"     -> e a causa medida: /atelie/?peca=999999 responde {cod_velho}"
          " (variavel publica do WordPress; era este o 404 dela)")
    ok('href="' + BASE + '/atelie/?peca=' not in at_html and "'peca' =>" not in at_html,
       "[/atelie/] nenhum link do painel servido usa o nome antigo")

    # ITEM 1, segunda metade: a faixa de "Peca publicada!". Ela so aparece depois
    # de publicar, entao o que da para medir da nuvem e que o CODIGO dela esta
    # servindo — a folha do painel traz a classe, que so existe no Atelie 1.3.0.
    ok("200" == at_cod and ".cdm-at-faixa{" in at_html,
       "[/atelie/] a folha traz .cdm-at-faixa (so existe no Atelie 1.3.0)", at_cod)

    # ITEM 3. A tecnica Picassiete so chega a lista dela se a versao da Loja subir:
    # `cdm_loja_termos_iniciais()` e percorrida uma vez por versao. Antes deste
    # bloco a rota publica dizia 4.
    tecnicas = int(((dados.get("termos") or {}).get("tecnica", -1))) if dados else -1
    ok(tecnicas == 5, "[rota] a Loja declara 5 tecnicas (o Picassiete chegou ao site)",
       f"{tecnicas} tecnicas")

    print("\n5. A ficha de cada peca publicada")
    if publicadas <= 0:
        pular("a ficha da peca", "nenhuma peca publicada ainda — e o estado normal hoje")
        pular("o formulario 'Verificar disponibilidade' no ar",
              "so existe em pagina de peca, e nao ha peca publicada — medido na bancada, nao no ar")
    else:
        for url in sorted(set(re.findall(r'href="(' + re.escape(BASE) + r'/loja/[^"/]+/)"', loja_corpo))):
            h, c = buscar(url)
            curto = url.replace(BASE, "")
            ok("200" == c, f"[{curto}] HTTP 200", c)
            if "200" != c:
                continue
            ok('name="description"' in h, f"[{curto}] serve meta description")
            ok('property="og:title"' in h, f"[{curto}] serve og:")
            ok('id="cdm-peca-jsonld"' in h, f"[{curto}] serve o JSON-LD da peca")
            ok("noindex" not in h, f"[{curto}] a ficha NAO sai do indice")
            ok("cdm-trilha" in h, f"[{curto}] serve a trilha")

            # ---- A GALERIA (item 4 do despacho de 14/09), medida NO AR ----
            #
            # ELA PRECISA SER MEDIDA AQUI, e nao so na bancada: o que monta esta
            # pagina e `the_content`, e o `wpautop` so existe no site. Foi ele que
            # deixou um `</p>` orfao colado no `</button>` das setas na primeira
            # versao deste bloco — HTML quebrado que a bancada nao tinha como ver,
            # porque la o filtro do WordPress nao roda.
            ok("data-cdm-galeria" in h, f"[{curto}] serve a galeria nova")
            ok(h.count('aria-label="Foto anterior"') == 1 and h.count('aria-label="Próxima foto"') == 1,
               f"[{curto}] as duas setas, com nome")
            ok('<div class="cdm-gal-setas">' in h, f"[{curto}] as setas vivem dentro de um bloco")
            minis = len(re.findall(r'<a class="cdm-gal-mini" href="#cdm-foto-', h))
            fotos_n = len(re.findall(r'<figure class="cdm-foto', h))
            ok(minis > 0 and minis == fotos_n,
               f"[{curto}] uma miniatura por foto, e cada uma e ancora", f"{minis} de {fotos_n}")
            ok(len(re.findall(r'data-cdm-grande="http', h)) == fotos_n,
               f"[{curto}] cada foto carrega o endereco da versao grande")
            ok('<dialog class="cdm-gal-lupa"' in h, f"[{curto}] a lupa esta na pagina")
            ok(not re.search(r"<dialog[^>]*\bopen\b", h), f"[{curto}] e nasce FECHADA")
            ok('id="cdm-loja-js"' in h, f"[{curto}] o script da galeria sai no rodape")
            # O DEFEITO EXATO DE 14/09, nomeado: nenhum `<p>` em volta de botao,
            # nenhum `</p>` orfao colado num `</button>`, e a lupa inteira.
            for marca in ("<p><button", "</button></p>", "<p><dialog", "</dialog></p>", "<p></dialog>"):
                ok(marca not in h, f"[{curto}] o wpautop NAO deixou '{marca}' na pagina")
            # O Product tem de ser JSON valido — schema invalido e schema ignorado.
            mm = re.search(r'id="cdm-peca-jsonld">(.*?)</script>', h, re.S)
            valido = False
            tem_oferta = False
            if mm:
                try:
                    g = json.loads(mm.group(1))
                    prod = (g.get("@graph") or [{}])[0]
                    valido = prod.get("@type") == "Product"
                    tem_oferta = "offers" in prod and prod["offers"].get("priceCurrency") == "BRL"
                except (ValueError, AttributeError, IndexError):
                    valido = False
            ok(valido, f"[{curto}] o JSON-LD e um Product valido")
            ok(tem_oferta, f"[{curto}] com Offer em BRL")
            # E a aritmetica que a ficha nao pode errar: o preco da tela e o do schema.
            preco_tela = re.search(r'class="cdm-preco">R\$&nbsp;([\d.,]+)<', h)
            preco_schema = re.search(r'"price":"([\d.]+)"', h)
            if preco_tela and preco_schema:
                da_tela = float(preco_tela.group(1).replace(".", "").replace(",", "."))
                do_schema = float(preco_schema.group(1))
                ok(abs(da_tela - do_schema) < 0.005,
                   f"[{curto}] o preco da TELA e o do SCHEMA sao o mesmo numero",
                   f"{da_tela} / {do_schema}")
            # ---- O FORMULARIO DO ADENDO 3, medido no ar e no CORPO ----
            # A regua esta escrita aqui: o botao, os dois campos, o consentimento
            # e o <details>. E o <details> e o que prova a 22.8 no ar — se um dia
            # alguem trocar por um botao de JavaScript, esta linha reprova.
            cp = corpo_visivel(h)
            ok("Verificar disponibilidade" in cp,
               f"[{curto}] o botao principal e 'Verificar disponibilidade'")
            ok('<details class="cdm-lead"' in cp,
               f"[{curto}] o formulario abre por <details> (funciona sem JavaScript)")
            ok('name="cdm_nome"' in cp and 'name="cdm_zap"' in cp,
               f"[{curto}] pede nome e WhatsApp")
            ok('name="cdm_email"' not in cp and 'name="cdm_cpf"' not in cp,
               f"[{curto}] e NAO pede e-mail nem CPF")
            ok("você autoriza o Clube do Mosaico a entrar em contato" in cp,
               f"[{curto}] o consentimento esta na tela, antes do botao")
            ok('name="cdm_nonce"' in cp, f"[{curto}] o formulario leva nonce")
            # O HONEYPOT esta na pagina e fora da vista das duas maneiras.
            ok('tabindex="-1"' in cp and 'cdm-lead-hp' in cp,
               f"[{curto}] o honeypot esta fora do teclado e fora da vista")

    # -------------------------------------------- o acesso dela, pela rota com token
    print("\n6. O acesso da artesa (rota protegida)")
    if not tk:
        pular("o estado do acesso", "sem token: passe como argumento ou em CDM_SYNC_TOKEN")
        pular("o papel e as capacidades", "sem token")
        pular("a hora do envio do e-mail", "sem token")
    else:
        # SEM TOKEN A ROTA TEM DE RECUSAR. Mede-se a recusa ANTES de usar o token:
        # uma rota que devolve o dado para qualquer um e pior que rota inexistente.
        sem, cod_sem = buscar(BASE + "/wp-json/clubedomosaico/v1/atelie")
        ok(cod_sem in ("401", "403"), "[rota] sem token a rota RECUSA", cod_sem)

        com, cod_com = buscar(BASE + "/wp-json/clubedomosaico/v1/atelie?token=" + tk)
        rel = {}
        if "200" == cod_com:
            try:
                rel = json.loads(com)
            except ValueError:
                rel = {}
        ok("200" == cod_com and rel, "[rota] com token a rota responde", cod_com)

        if rel:
            ok(bool(rel.get("papel_existe")), "o papel artesa existe no site")
            caps = set(rel.get("capacidades") or [])
            ok(CAPS_ESPERADAS.issubset(caps), "as sete capacidades esperadas estao lá",
               ", ".join(sorted(caps)))
            sobrando = caps & CAPS_PROIBIDAS
            ok(not sobrando, "e NENHUMA capacidade proibida",
               "nenhuma" if not sobrando else ", ".join(sorted(sobrando)))
            ok(bool(rel.get("usuaria_existe")), "a usuaria da artesa existe")
            ok("artesa" in (rel.get("usuaria_papeis") or []), "com o papel artesa",
               ", ".join(rel.get("usuaria_papeis") or []))
            ok("*" in str(rel.get("email", "")), "o e-mail sai mascarado na rota",
               rel.get("email", ""))

            ac = rel.get("acesso") or {}
            ok(bool(ac.get("criada")) or bool(ac.get("enviado")),
               "o snippet rodou o caminho do acesso")
            enviado = bool(ac.get("enviado"))
            ok(enviado, "o wp_mail ACEITOU o e-mail de acesso",
               (ac.get("erro") or "") if not enviado else "sim")
            quando = str(ac.get("quando") or "")
            ok(quando != "", "e a hora do envio esta registrada (para o ESTADO.md)", quando)
            if quando:
                print(f"\n     >>> HORA DO ENVIO, em UTC: {quando}")
                print(f"     >>> tentativas: {ac.get('tentativas')}")
            # A senha e a chave NAO podem estar na resposta.
            bruto = json.dumps(rel)
            ok("criar-senha" not in bruto, "a rota NAO devolve link de criar senha")
            ok("mina196" not in bruto, "a rota NAO devolve o e-mail inteiro")

    print("\n" + "-" * 78)
    print(f"{feitos} afirmacoes, {falhas} falha(s), {pulados} pulada(s).")
    print("NAO MEDIDO AQUI, e de proposito: se o e-mail CHEGOU na caixa da Hotmail")
    print("(wp_mail true diz que o servidor aceitou, nao que passou do filtro de spam)")
    print("e se o dedo dela funciona na tela de 360 px. As duas metades precisam de")
    print("um humano, e ficam no relatorio como o que falta.")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
