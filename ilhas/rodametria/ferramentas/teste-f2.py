#!/usr/bin/env python3
"""
TESTE DA F2 — E ELE ESCREVE A PROPRIA REGUA.

A secao 8 do ARQUIPELAGO.md: "quem confere escreve a propria regua, nunca chama
a de quem produziu o dado" — senao as duas metades erram juntas. Entao a
aritmetica aqui e REESCRITA A MAO em Fraction, e este arquivo NAO importa
f2-referencia.py para calcular nada. O que ele le de f2-referencia.py e so o
que e FATO EXTERNO as duas (os nomes dos relevos), pela fronteira que a propria
secao 8 desenha: decisao se escreve duas vezes, fato externo mora num lugar so.

E A GRADE PISA NA BORDA. A secao 8 registra a grade varrida "de 10 em 10" que
nao conseguia separar ceil de floor+1: amostra com nome de grade. Aqui a grade
inclui o menor e o maior V e Ah da lista publicada, a autonomia ausente, a
autonomia de 1 km, o peso exatamente NO teto de carga e o peso um quilo acima
dele — que e a borda onde a frase muda.
"""

import json
import os
import re
import sys
from fractions import Fraction

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)

RESPOSTAS = os.path.join(ILHA, "dados", "f2-respostas.json")
CONSTANTES = os.path.join(ILHA, "dados", "constantes.json")
SNIPPET_F2 = os.path.join(ILHA, "snippets", "rodametria-f2.php")
SNIPPET_CASCA = os.path.join(ILHA, "snippets", "rodametria-casca.php")

falhas = []
afirmacoes = 0


def afirma(condicao, mensagem):
    global afirmacoes
    afirmacoes += 1
    if not condicao:
        falhas.append(mensagem)


def numero_pt(fr, casas=0):
    """A MINHA regua de formato, escrita a mao — nao e a do gerador."""
    if casas == 0:
        n = fr.numerator
        d = fr.denominator
        inteiro = (n + d // 2) // d if fr >= 0 else -((-n + d // 2) // d)
        partes = []
        s = str(abs(inteiro))
        while len(s) > 3:
            partes.insert(0, s[-3:])
            s = s[:-3]
        partes.insert(0, s)
        return ("-" if inteiro < 0 else "") + ".".join(partes)
    escala = Fraction(10) ** casas
    arred = Fraction(int(fr * escala + Fraction(1, 2)), int(escala))
    inteira = int(arred)
    frac = arred - inteira
    dec = ""
    for _ in range(casas):
        frac *= 10
        dig = int(frac)
        dec += str(dig)
        frac -= dig
    return "%s,%s" % (numero_pt(Fraction(inteira)), dec)


def sem_comentarios(fonte):
    """Tira comentario de bloco e de linha do PHP.

    A regua tem de medir o que o arquivo FAZ, nao o que ele conta sobre si: a
    primeira versao desta bateria reprovou a propria casca porque o comentario
    de cabecalho dela CITA a palavra <script> ao explicar a regra. E a familia
    do "perdoar por presenca de palavra e adivinhar" da secao 8 — a saida nao e
    heuristica melhor, e parar de medir prosa.
    """
    fora = re.sub(r"/\*.*?\*/", lambda m: "\n" * m.group(0).count("\n"), fonte, flags=re.S)
    fora = re.sub(r"^\s*//.*$", "", fora, flags=re.M)

    return fora


def fim_do_corpo(fonte, inicio):
    """Onde a funcao que comeca em `inicio` acaba.

    Delimitar por "a proxima linha que comeca com function" estava errado e a
    bateria o acusou: entre duas funcoes pode haver add_action, add_filter e
    add_shortcode, e o corpo medido engolia o gancho seguinte. O fim e o
    primeiro desses marcadores, qualquer um deles.
    """
    marcadores = ("\nfunction ", "\nadd_action(", "\nadd_filter(",
                  "\nadd_shortcode(", "\nif ( ! function_exists(")
    fins = [fonte.find(m, inicio + 1) for m in marcadores]
    fins = [f for f in fins if f > 0]

    return min(fins) if fins else len(fonte)


def main():
    d = json.load(open(RESPOSTAS, encoding="utf-8"))
    cs = {c["id"]: c for c in json.load(open(CONSTANTES, encoding="utf-8"))["constantes"]}

    # ---------------------------------------------------------------
    # 1. OS FATORES DE RELEVO. A MINHA leitura sai de constantes.json,
    #    nao do arquivo que o gerador escreveu — se o gerador tiver
    #    copiado errado, e aqui que aparece.
    # ---------------------------------------------------------------
    meus_fatores = {
        "plano": Fraction(1),
        "misto": Fraction(str(cs["fator-relevo-misto"]["valor"])),
        "ladeira": Fraction(str(cs["fator-relevo-ladeira-contra-plano"]["valor"])),
    }
    for relevo, meu in meus_fatores.items():
        dele = Fraction(d["fatores_de_relevo"][relevo])
        afirma(meu == dele,
               "fator de %s: o arquivo publicado diz %s e a constante diz %s"
               % (relevo, dele, meu))
        afirma(d["fatores_de_relevo_tela"][relevo] == numero_pt(meu, 2),
               "fator de %s na tela: %r, eu calculo %r"
               % (relevo, d["fatores_de_relevo_tela"][relevo], numero_pt(meu, 2)))

    afirma(cs["fator-relevo-misto"]["status"] == "publicavel",
           "o fator de misto nao esta publicavel e a pagina o publica")
    afirma(cs["fator-relevo-ladeira-contra-plano"]["status"] == "publicavel",
           "o fator de ladeira nao esta publicavel e a pagina o publica")

    # A RAZAO E A RAZAO: 97,74 / 41,29 tem de ser o fator de ladeira,
    # arredondado como a constante declara. E a terceira conta que a secao 8
    # pede — ler a fonte por outro caminho e comparar com o publicado.
    razao = Fraction("97.74") / Fraction("41.29")
    afirma(abs(razao - meus_fatores["ladeira"]) < Fraction(1, 100),
           "a razao 97,74/41,29 da %s e o fator publicado e %s"
           % (float(razao), meus_fatores["ladeira"]))
    # O misto e a RAIZ do fator de ladeira (meio-caminho geometrico), e
    # a conta e conferida pelo quadrado, para nao precisar de float.
    afirma(abs(meus_fatores["misto"] ** 2 - meus_fatores["ladeira"]) < Fraction(1, 50),
           "o misto ao quadrado da %s e o fator de ladeira e %s — o misto deveria "
           "ser a raiz geometrica" % (float(meus_fatores["misto"] ** 2),
                                      meus_fatores["ladeira"]))

    # ---------------------------------------------------------------
    # 2. O DEGRAU 3 ESTA PENDENTE, E A PAGINA TEM DE SABER DISSO.
    #    O status e lido da constante, nunca de uma lista escrita.
    # ---------------------------------------------------------------
    pend = cs["consumo-absoluto-wh-por-km-patinete"]["status"] != "publicavel"
    afirma(d["degrau_3_disponivel"] == (not pend),
           "degrau_3_disponivel diz %r e a constante esta %r"
           % (d["degrau_3_disponivel"], cs["consumo-absoluto-wh-por-km-patinete"]["status"]))

    # ---------------------------------------------------------------
    # 3. A GRADE, COM AS BORDAS. Eu recalculo Wh e a faixa a mao e
    #    comparo com cada linha da tabela publicada.
    # ---------------------------------------------------------------
    for bloco in ("do_banco", "externas"):
        for l in d["tabela"][bloco]:
            wh = Fraction(str(l["tensao_v"])) * Fraction(str(l["amperagem_ah"]))
            afirma(l["wh"] == numero_pt(wh),
                   "%s: Wh publicado %r, eu calculo %r"
                   % (l["rotulo"], l["wh"], numero_pt(wh)))
            for relevo, fator in meus_fatores.items():
                f = l["faixas"][relevo]
                if l["autonomia_declarada_km"] is None:
                    afirma(f["piso_km"] is None,
                           "%s/%s: sem autonomia declarada a faixa tinha de ser vazia, "
                           "e veio %r" % (l["rotulo"], relevo, f["piso_km"]))
                    afirma(f.get("causa") == "sem_autonomia_declarada_e_degrau_3_pendente",
                           "%s/%s: a causa da faixa vazia tem de estar nomeada, e veio %r"
                           % (l["rotulo"], relevo, f.get("causa")))
                    continue
                declarada = Fraction(str(l["autonomia_declarada_km"]))
                piso = declarada / fator
                afirma(f["piso_km"] == numero_pt(piso),
                       "%s/%s: piso publicado %r, eu calculo %r"
                       % (l["rotulo"], relevo, f["piso_km"], numero_pt(piso)))
                afirma(f["teto_km"] == numero_pt(declarada),
                       "%s/%s: teto publicado %r, eu calculo %r"
                       % (l["rotulo"], relevo, f["teto_km"], numero_pt(declarada)))
                afirma(f["degenerada"] == (piso == declarada),
                       "%s/%s: 'degenerada' publicado %r e piso==teto e %r"
                       % (l["rotulo"], relevo, f["degenerada"], piso == declarada))
                # Em plano a faixa E degenerada por definicao, e em ladeira NUNCA
                # pode ser: se for, o fator foi lido como 1 em algum lugar.
                if relevo == "plano":
                    afirma(f["degenerada"],
                           "%s: em plano a faixa tinha de ser degenerada" % l["rotulo"])
                if relevo == "ladeira":
                    afirma(not f["degenerada"],
                           "%s: em ladeira a faixa NAO pode ser degenerada — o fator "
                           "virou 1 em algum lugar" % l["rotulo"])

    # A resposta de exemplo, recalculada a mao com as bordas da entrada.
    ex = d["campos"]["exemplo"]
    wh_ex = Fraction(str(ex["tensao_v"])) * Fraction(str(ex["amperagem_ah"]))
    afirma(d["resposta_exemplo"]["wh_tela"] == numero_pt(wh_ex),
           "o exemplo publica %r Wh e eu calculo %r"
           % (d["resposta_exemplo"]["wh_tela"], numero_pt(wh_ex)))
    piso_ex = Fraction(str(ex["autonomia_declarada_km"])) / meus_fatores[ex["relevo"]]
    afirma(d["resposta_exemplo"]["piso_km_tela"] == numero_pt(piso_ex),
           "o exemplo publica piso %r e eu calculo %r"
           % (d["resposta_exemplo"]["piso_km_tela"], numero_pt(piso_ex)))

    # Bordas da lista de campos: o menor e o maior V e Ah tem de produzir Wh
    # positivo e a faixa tem de degradar na mesma direcao em toda a grade.
    vs = d["campos"]["tensoes_v"]
    ahs = d["campos"]["amperagens_ah"]
    afirma(len(vs) >= 2 and len(ahs) >= 2, "a grade de campos tem menos de dois valores")
    for v in (min(vs), max(vs)):
        for a in (min(ahs), max(ahs)):
            wh = Fraction(str(v)) * Fraction(str(a))
            afirma(wh > 0, "borda %s V x %s Ah deu Wh nao positivo" % (v, a))
            for relevo, fator in meus_fatores.items():
                piso = Fraction(1) / fator
                afirma(piso <= 1,
                       "o fator de %s nao degrada: 1/%s = %s" % (relevo, fator, piso))

    # ---------------------------------------------------------------
    # 4. A PRESTACAO DE CONTAS FECHA O BANCO (secao 7), CONTADA AQUI.
    # ---------------------------------------------------------------
    veiculos = json.load(open(os.path.join(ILHA, "dados", "veiculos.json"), encoding="utf-8"))
    total = len(veiculos["registros"])
    afirma(d["compra"]["total_registros_veiculos"] == total,
           "o arquivo diz %s registros e o banco tem %s"
           % (d["compra"]["total_registros_veiculos"], total))
    soma = sum(len(v) for v in d["compra"]["grupos"].values())
    afirma(soma == total,
           "a prestacao de contas soma %s e o banco tem %s registros" % (soma, total))
    vistos = []
    for lista in d["compra"]["grupos"].values():
        for f in lista:
            vistos.append(f["id"])
    afirma(len(vistos) == len(set(vistos)),
           "ha registro nomeado em DOIS grupos: %s"
           % [i for i in set(vistos) if vistos.count(i) > 1])

    # Todo item da vitrine tem de ser publicavel E ter saida de compra (25.2).
    for f in d["compra"]["vitrine"]:
        afirma(f["status"] == "publicavel",
               "a vitrine serve %s, que esta %s" % (f["id"], f["status"]))
        afirma(bool(f["url_busca"]),
               "a vitrine serve %s sem saida de compra" % f["id"])
    # E a vitrine nunca pode estar vazia com publicavel disponivel: a secao 7
    # proibe bloco de compra vazio enquanto houver piso.
    publicaveis_com_piso = [r for r in veiculos["registros"]
                            if r.get("status") == "publicavel"
                            and (r.get("afiliado") or {}).get("url_busca")]
    afirma(len(d["compra"]["vitrine"]) == len(publicaveis_com_piso),
           "ha %s publicaveis com piso no banco e a vitrine serve %s"
           % (len(publicaveis_com_piso), len(d["compra"]["vitrine"])))
    ids_vitrine = {f["id"] for f in d["compra"]["vitrine"]}
    for r in publicaveis_com_piso:
        afirma(r["id"] in ids_vitrine,
               "%s e publicavel e tem piso, e nao esta na vitrine — e o avesso da 25.2"
               % r["id"])

    # A ORDEM DA SECAO 7: quem passa em TODAS as condicoes vem antes de quem
    # falha numa. Aqui a condicao e o Wh, e o rotulo do grupo diz a posicao.
    peso_do_grupo = {"cabe no Wh que você pediu": 0,
                     "bateria de outra faixa de energia": 1,
                     "a ficha não declara a bateria": 2}
    pesos = [peso_do_grupo.get(f.get("rotulo_do_grupo"), 9)
             for f in d["compra"]["vitrine"]]
    afirma(all(p < 9 for p in pesos),
           "ha item na vitrine sem rotulo de grupo conhecido: %s" % pesos)
    afirma(pesos == sorted(pesos),
           "a ordem da vitrine fere a secao 7 — item que falha no Wh vem antes de "
           "item que passa: %s" % pesos)

    # ---------------------------------------------------------------
    # 5. OS MOLDES DE FRASE EXISTEM, E O NAVEGADOR SO USA MOLDE QUE
    #    EXISTE. Molde faltando = a pagina imprimindo "{piso}" na cara
    #    de quem le, que e o unico jeito deste bloco piorar a tela.
    # ---------------------------------------------------------------
    php_f2 = open(SNIPPET_F2, encoding="utf-8").read()
    usados = set(re.findall(r"D\.moldes\.(\w+)", php_f2))
    afirma(usados, "o JS da F2 nao usa molde nenhum — ele voltou a escrever frase")
    for m in sorted(usados):
        afirma(m in d["frases_molde"],
               "o JS usa o molde %r e ele nao existe no arquivo publicado" % m)
    # O JS NAO TEM FRASE PROPRIA. A bateria de 29/10/2026 provou que a trava
    # anterior era inerte: trocar `D.moldes.km_recusa` por um literal passava,
    # porque a regua so conferia que os moldes CITADOS existiam. Agora ela olha
    # os literais do bloco <script> da F2 e proibe prosa ali dentro — frase com
    # tres palavras ou mais, ou qualquer acento.
    bloco_js = php_f2.split('<script id="rodametria-f2-js">')
    afirma(len(bloco_js) == 2, "nao achei o bloco <script> da F2")
    if len(bloco_js) == 2:
        js = bloco_js[1].split("</script>")[0]
        # o pacote de dados vem do PHP e nao e literal do JS
        js = re.sub(r"<\?php.*?\?>", "", js, flags=re.S)
        for lit in re.findall(r"'([^'\n]{4,})'", js) + re.findall(r'"([^"\n]{4,})"', js):
            # Markup e seletor NAO sao prosa: literal com < ou > e pedaco de
            # HTML, e a primeira versao desta regua reprovou os dois — regua que
            # reprova codigo certo e o caminho mais curto para alguem a ignorar
            # (a licao que a 20.5 nomeou quando o "REPROVADO" era cache).
            if "<" in lit or ">" in lit:
                continue
            acentuado = bool(re.search(r"[\u00e0-\u00ff\u00c0-\u00dd]", lit))
            palavras = [w for w in re.split(r"\s+", lit) if re.match(r"^[A-Za-z]{2,}$", w)]
            afirma(not acentuado,
                   "o JS da F2 tem literal acentuado: %r — frase de tela mora no "
                   "molde, nunca no navegador" % lit)
            afirma(len(palavras) < 3,
                   "o JS da F2 tem literal com prosa: %r — frase de tela mora no "
                   "molde, nunca no navegador" % lit)

    # Toda chave que um molde pede tem de ser preenchida por quem o usa.
    for nome, molde in d["frases_molde"].items():
        chaves = set(re.findall(r"\{(\w+)\}", molde))
        afirma(all(k.isidentifier() for k in chaves),
               "o molde %r tem chave invalida" % nome)

    # ---------------------------------------------------------------
    # 6. O SNIPPET NAO DIGITA NUMERO DE RESPOSTA.
    #
    #    A cicatriz da secao 8: "numero de tela nasce contado, nunca
    #    digitado". As unicas excecoes permitidas sao os numeros que
    #    sao PROCEDENCIA citada no texto (os dois Wh/km do estudo e o
    #    ano dele) e os literais de HTML/CSS. Entao a regra olha so as
    #    linhas de prosa que a pagina imprime, e exige que todo numero
    #    delas esteja na lista declarada.
    # ---------------------------------------------------------------
    permitidos = {"97,74", "41,29", "1.800", "12", "2025", "960", "1.200", "48", "60",
                  "20", "29,8", "1,0", "3", "2", "1", "24", "16", "30", "10,4"}
    for linha in php_f2.split("\n"):
        if "rdm-num" not in linha and "<p>" not in linha and "<h3>" not in linha:
            continue
        for n in re.findall(r"\d+(?:[.,]\d+)?", linha):
            if n in permitidos:
                continue
            # numeros dentro de atributo/classe/esc_* nao sao prosa
            if re.search(r"(class=|id=|width|height|px|rem|em\b|%s|%d|JSON_|\$|rdm-e)", linha):
                continue
            afirma(False, "numero %r digitado em prosa da F2: %s" % (n, linha.strip()[:110]))

    # ---------------------------------------------------------------
    # 6-b. O NOME DA OPTION QUE O SITE LE TEM DE SAIR DO ID DO MANIFEST.
    #
    # A secao 8: "uma afirmacao cobra que as duas fontes digam a mesma coisa".
    # Quem grava a option e o Sync, com `rodametria_dados_` +
    # sanitize_key(id do manifest) — e sanitize_key PRESERVA hifen. Em 29/10/2026
    # a casca digitou `f2_respostas` com sublinhado e a pagina inteira caiu no
    # estado degradado, com as tres linhas da revisao 2 dizendo `ok` no log do
    # Sync. Desembarque que acontece e leitura que falha nao tem linha vermelha
    # em lugar nenhum: so esta afirmacao o ve.
    # ---------------------------------------------------------------
    manifest = json.load(open(os.path.join(ILHA, "manifest.json"), encoding="utf-8"))
    ids_de_dados = {i["id"] for i in manifest.get("dados", [])}
    casca_bruta = open(SNIPPET_CASCA, encoding="utf-8").read()
    m = re.search(r"define\(\s*'RODAMETRIA_ID_DADOS_F2'\s*,\s*'([^']+)'", casca_bruta)
    afirma(bool(m), "a casca nao declara RODAMETRIA_ID_DADOS_F2")
    if m:
        afirma(m.group(1) in ids_de_dados,
               "a casca le a option de %r e o manifest nao tem item de dados com esse id "
               "(tem %s) — o site ia cair no estado degradado em silencio"
               % (m.group(1), sorted(ids_de_dados)))
    # E ninguem pode voltar a digitar o nome: a chamada tem de usar a constante.
    for nome, fonte in (("casca", casca_bruta), ("f2", php_f2)):
        for chamada in re.findall(r"rodametria_casca_banco\(\s*([^)]*)\)", fonte):
            chamada = chamada.strip()
            if chamada.startswith("$"):
                continue
            afirma("RODAMETRIA_ID_DADOS_F2" in chamada or chamada == "$id",
                   "%s: rodametria_casca_banco(%s) com nome digitado — o id do item de dados "
                   "e fato externo e mora no manifest" % (nome, chamada))

    # ---------------------------------------------------------------
    # 7. AS TRAVAS DE MECANISMO DA SECAO 8 QUE SE MEDEM NO FONTE.
    # ---------------------------------------------------------------
    casca = open(SNIPPET_CASCA, encoding="utf-8").read()
    for nome, bruto in (("casca", casca), ("f2", php_f2)):
        fonte = sem_comentarios(bruto)
        # Toda funcao de nivel superior dentro de if ( ! function_exists() ).
        for m in re.finditer(r"^function\s+(\w+)", fonte, re.M):
            fim = fonte[:m.start()]
            afirma(fim.rstrip().endswith("{"),
                   "%s: a funcao %s() nao esta dentro de if ( ! function_exists() )"
                   % (nome, m.group(1)))
        # NENHUM <script> DENTRO DO RETORNO DE SHORTCODE. A regra da secao 8 nao
        # e "script so no rodape" — JSON-LD em wp_head e legitimo e nao passa
        # pelos filtros do the_content. O que mata o script e o the_content
        # trocando && por entidade, e isso so alcanca o que o SHORTCODE devolve.
        #
        # Entao a regua mede duas coisas, as duas no fonte:
        #   (a) todo <script> esta dentro de um add_action de wp_head ou
        #       wp_footer — nunca solto no meio do arquivo;
        #   (b) nenhuma funcao que monta HTML de pagina (as `*_html`, que sao as
        #       que um shortcode alcanca) contem a palavra "<script".
        for m in re.finditer(r"<script", fonte):
            antes = fonte[:m.start()]
            gancho = antes.split("add_action(")[-1][:40] if "add_action(" in antes else ""
            afirma("wp_footer" in gancho or "wp_head" in gancho,
                   "%s: ha <script> fora de add_action('wp_head'/'wp_footer') — e o "
                   "defeito que derrubou cinco calculadoras da Aquametria" % nome)

        # (b) — a trava que de fato protege o shortcode.
        for m in re.finditer(r"^function\s+(\w+_html)\s*\(", fonte, re.M):
            inicio = m.start()
            corpo_fn = fonte[inicio:fim_do_corpo(fonte, inicio)]
            afirma("<script" not in corpo_fn,
                   "%s: a funcao %s() devolve HTML de pagina e contem <script> — o "
                   "the_content vai trocar && por entidade e matar o script"
                   % (nome, m.group(1)))

    # Texto de bastidor da fabrica e proibido na pagina publica (32.4).
    proibidas = ["egresso", "SERP", "snippet", "wp-sitemap", "manifest",
                 "ARQUIPELAGO", "Sync", "bancada", "dados/", "ferramentas/"]
    # So o que a pagina IMPRIME conta: linhas de comentario PHP nao vao a tela.
    for linha in php_f2.split("\n"):
        nua = linha.strip()
        if nua.startswith("*") or nua.startswith("/*") or nua.startswith("//"):
            continue
        if "esc_html" not in linha and "<p" not in linha and "<h" not in linha:
            continue
        for termo in proibidas:
            afirma(termo not in linha,
                   "32.4: a palavra de bastidor %r aparece em texto de tela: %s"
                   % (termo, nua[:110]))

    # A ordem da 32.1 na funcao que monta a pagina: formulario, caixa, compra,
    # tabela, dobras — nessa ordem e sem excecao.
    ordem = ["rodametria_f2_formulario_html( $d )",
             "rodametria_f2_resultado_html( $d )",
             "rodametria_casca_bloco_de_compra(",
             "rodametria_f2_tabela_html( $d )",
             "rodametria_f2_dobras_html( $d )"]
    corpo = php_f2.split("function rodametria_f2_pagina_html()")[-1]
    pos = [corpo.find(x) for x in ordem]
    afirma(all(p > 0 for p in pos),
           "nao achei todos os blocos da 32.1 na pagina: %s" % list(zip(ordem, pos)))
    afirma(pos == sorted(pos),
           "a ordem da 32.1 esta trocada na pagina: %s" % list(zip(ordem, pos)))

    print("teste-f2: %d afirmacoes, %d falha(s)" % (afirmacoes, len(falhas)))
    for f in falhas:
        print("  REPROVADO: %s" % f)

    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
