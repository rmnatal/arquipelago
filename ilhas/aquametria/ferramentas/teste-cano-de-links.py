#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Portao do portao: exercita a REGUA e o PORTAO do cano de links.

    python3 ferramentas/teste-cano-de-links.py

CINCO METADES, e cada uma mede o que a de cima nao alcanca:

  (A) A ARITMETICA, caso a caso, sobre bancos ENCENADOS. E a metade que so
      existe porque a contagem saiu de dentro do contador e virou regua com
      RAIZ parametrizada: antes de 19/10/2026 nao havia como contar um banco de
      mentira, e por isso a conta nunca tinha sido medida por nada. Inclui o
      caso que decide o desenho da serie: DOIS registros trocando de estado
      entre si, com todos os totais identicos.

  (B) ESTRUTURAL, e nao comportamental, de proposito. Ela le os arquivos e
      cobra que o contador nao tenha contagem propria e que o portao pergunte
      quais bancos foram lidos. Medir comportamento provaria so que a segunda
      copia da aritmetica nao divergiu NESTA passada — nao que ela saiu. E a
      licao escrita em 16/10/2026, no portao da deriva.

  (C) O VERDE VAZIO. Banco nenhum lido da zero sem piso, e zero sem piso le-se
      como "o cano esta inteiro". E a unica forma de este portao mentir sem
      ninguem editar uma linha dele, e por isso ela e afirmada contra uma raiz
      sem banco nenhum.

  (D) O PORTAO INTEIRO numa ILHA DE SOMBRA: verde com a serie, vermelho sem
      ela, vermelho quando um registro muda de estado com o total intacto,
      vermelho quando entra registro novo, e verde de novo depois do --gravar.
      E a metade que mede o codigo de saida junto com a palavra impressa.

  (E) A DENUNCIA DA BANCADA, nos dois sentidos. O portao deste cano nasceu de
      uma denuncia da `bancada.py` ("SEM CONVENCAO, ninguem roda"), e a regra
      que a apagou e nova: `contar-` e producao SE um portao carregar a conta
      dele. Regra que so sabe calar e pior que denuncia nenhuma, entao esta
      metade cobra as duas direcoes — o contador de hoje sai da lista, e um
      contador cuja regua nenhum portao carrega CONTINUA denunciado.
"""
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

afirmacoes = 0
falhas = []


def afirma(texto, condicao, detalhe=""):
    global afirmacoes
    afirmacoes += 1
    if condicao:
        print("  ok   %s" % texto)
    else:
        print("  FALHA %s%s" % (texto, (" — " + detalhe) if detalhe else ""))
        falhas.append(texto)


def carregar_regua():
    caminho = os.path.join(RAIZ, "ferramentas", "regua-cano-de-links.py")
    spec = importlib.util.spec_from_file_location("regua_cano_de_links", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def banco_de_mentira(raiz, nome, produtos):
    os.makedirs(os.path.join(raiz, "dados"), exist_ok=True)
    caminho = os.path.join(raiz, "dados", "produtos-%s.json" % nome)
    with io.open(caminho, "w", encoding="utf-8") as f:
        json.dump({"id": nome, "produtos": produtos}, f, ensure_ascii=False)
    return caminho


def item(pid, busca=True, produto=False, url=False, degrau=None, intestavel=False):
    af = {}
    if busca:
        af["url_busca"] = "https://s.shopee.com.br/%s" % pid
    if produto:
        af["url_produto"] = "https://shopee.com.br/produto/%s" % pid
    if url:
        af["url"] = "https://s.shopee.com.br/anuncio-%s" % pid
    if degrau is not None:
        af["degrau"] = degrau
    if intestavel:
        af["intestavel"] = True
    return {"id": pid, "afiliado": af}


# ---------------------------------------------------------------------------
# (A) A ARITMETICA, CASO A CASO
# ---------------------------------------------------------------------------
def metade_a(regua):
    print("\n(A) a aritmetica da regua, sobre bancos encenados")

    tmp = tempfile.mkdtemp(prefix="aqm-cano-a-")
    try:
        banco_de_mentira(tmp, "filtro", [
            item("com-tudo", produto=True, url=True, degrau=3),
            item("so-piso", degrau=4),
            item("anuncio-sem-ficha", url=True, intestavel=True),
        ])
        banco_de_mentira(tmp, "midia", [
            item("sem-piso-nenhum", busca=False),
        ])
        c = regua.contar(tmp)
        t = c["totais"]
        afirma("conta os registros dos dois bancos", t["registros"] == 4, str(t))
        afirma("conta o registro sem piso (25.2)", t["sem_url_busca"] == 1, str(t))
        afirma("conta os registros sem ficha", t["sem_url_produto"] == 3, str(t))
        afirma("conta url sem ficha, a divida da 25.4-b", t["url_sem_url_produto"] == 1, str(t))
        afirma("conta a bandeira intestavel", t["intestaveis"] == 1, str(t))
        afirma("agrupa por degrau e o nulo viaja como '-'",
               c["degraus"] == {"3": 1, "4": 1, "-": 2}, str(c["degraus"]))
        afirma("a identidade do item traz o banco e o id",
               "filtro/com-tudo" in c["itens"] and "midia/sem-piso-nenhum" in c["itens"],
               str(sorted(c["itens"])))
        afirma("nomeia por um os sem piso e os sem ficha",
               c["sem_busca"] == ["midia/sem-piso-nenhum"] and len(c["sem_produto"]) == 3,
               "%s | %s" % (c["sem_busca"], c["sem_produto"]))
        afirma("conta por banco",
               c["por_banco"]["produtos-filtro.json"]["n"] == 3
               and c["por_banco"]["produtos-midia.json"]["sem_busca"] == 1,
               str(c["por_banco"]))
        afirma("os totais saem das frases de estado, nao de uma segunda contagem",
               regua.totais(c["itens"]) == t, "%s contra %s" % (regua.totais(c["itens"]), t))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    # O CASO QUE DECIDE O DESENHO DA SERIE: dois itens trocando de estado entre
    # si. Todos os totais ficam IDENTICOS, e uma declaracao por total ficaria
    # verde sobre a troca — exatamente o que a serie da deriva aprendeu em
    # 16/10/2026 ("74 linhas podem virar 74 OUTRAS linhas").
    antes = tempfile.mkdtemp(prefix="aqm-cano-a2-")
    depois = tempfile.mkdtemp(prefix="aqm-cano-a3-")
    try:
        banco_de_mentira(antes, "filtro", [
            item("alfa", produto=True, degrau=3),
            item("beta", degrau=4),
        ])
        banco_de_mentira(depois, "filtro", [
            item("alfa", degrau=4),
            item("beta", produto=True, degrau=3),
        ])
        a = regua.contar(antes)
        b = regua.contar(depois)
        afirma("a troca de estado entre dois itens nao muda total nenhum",
               a["totais"] == b["totais"] and a["degraus"] == b["degraus"],
               "%s / %s" % (a["totais"], b["totais"]))
        novos, sumidos, mudados = regua.comparar_com_declaracao(
            b["itens"], {"itens": a["itens"]})
        afirma("e a comparacao item por item acusa as duas mudancas",
               not novos and not sumidos and len(mudados) == 2, str(mudados))
    finally:
        shutil.rmtree(antes, ignore_errors=True)
        shutil.rmtree(depois, ignore_errors=True)

    # Registro novo e registro sumido sao falhas de natureza diferente, porque
    # o conserto de cada uma e outro.
    afirma("registro novo aparece como novo, nao como mudanca",
           regua.comparar_com_declaracao({"a/x": "piso:1"}, {"itens": {}}) == (["a/x"], [], []),
           str(regua.comparar_com_declaracao({"a/x": "piso:1"}, {"itens": {}})))
    afirma("registro que saiu do banco aparece como sumido",
           regua.comparar_com_declaracao({}, {"itens": {"a/x": "piso:1"}}) == ([], ["a/x"], []),
           str(regua.comparar_com_declaracao({}, {"itens": {"a/x": "piso:1"}})))
    afirma("declaracao ausente nao se le como cano vazio",
           regua.comparar_com_declaracao({}, None)[0] == ["a serie nao tem declaracao nenhuma"],
           str(regua.comparar_com_declaracao({}, None)))
    afirma("campo() le a frase de estado por nome e nao por posicao",
           regua.campo("piso:1 ficha:0 anuncio:1 degrau:- intestavel:1", "degrau") == "-"
           and regua.campo("piso:1 ficha:0", "intestavel") == "",
           "leu %r" % regua.campo("piso:1 ficha:0 anuncio:1 degrau:- intestavel:1", "degrau"))


# ---------------------------------------------------------------------------
# (B) ESTRUTURAL: a segunda copia da aritmetica SAIU, e isso nao se prova rodando
# ---------------------------------------------------------------------------
def metade_b():
    print("\n(B) estrutural: o contador nao conta, e o portao pergunta quais bancos leu")

    contador = io.open(os.path.join(RAIZ, "ferramentas", "contar-cano-de-links.py"),
                       encoding="utf-8").read()
    portao = io.open(os.path.join(RAIZ, "ferramentas", "conferir-cano-de-links.py"),
                     encoding="utf-8").read()
    regua_txt = io.open(os.path.join(RAIZ, "ferramentas", "regua-cano-de-links.py"),
                        encoding="utf-8").read()

    afirma("o contador carrega a regua compartilhada",
           "regua-cano-de-links.py" in contador and "regua.contar(RAIZ)" in contador)
    afirma("o contador nao abre banco nenhum por conta propria",
           "json.load" not in contador and "glob" not in contador,
           "ele voltou a ter contagem propria")
    afirma("o portao carrega a mesma regua",
           "regua-cano-de-links.py" in portao and "regua.contar(RAIZ)" in portao)
    afirma("o portao nao tem contagem propria",
           "json.load" not in portao and "glob" not in portao)
    afirma("o portao pergunta a regua QUAIS bancos foram lidos",
           "regua.bancos(RAIZ)" in portao and 'contagem["bancos"]' in portao,
           "sem isso, zero banco lido passa por cano inteiro")
    afirma("o portao compara item por item, e nao por total",
           "comparar_com_declaracao" in portao)
    afirma("o portao se declara sem rede para a bancada",
           "BANCADA: sem rede" in portao)
    importados = [l.strip() for l in regua_txt.split("\n")
                  if l.startswith(("import ", "from "))]
    afirma("a regua nao importa nada de rede nem de processo",
           not [l for l in importados
                if any(m in l for m in ("requests", "urllib", "socket", "subprocess", "http"))],
           "importa: %s" % importados)
    afirma("a regua recebe a raiz em toda funcao de contagem",
           "def contar(raiz)" in regua_txt and "def bancos(raiz)" in regua_txt
           and "def registros(raiz)" in regua_txt)
    afirma("o portao nao reescreve a regra V26 do validador de produtos",
           "V26" in portao and "validar-produtos.py" in portao,
           "a fronteira com o validador tem de estar escrita no portao")


# ---------------------------------------------------------------------------
# (C) O VERDE VAZIO
# ---------------------------------------------------------------------------
def metade_c(regua):
    print("\n(C) o verde vazio: zero banco lido nao e cano inteiro")

    vazia = tempfile.mkdtemp(prefix="aqm-cano-c-")
    try:
        os.makedirs(os.path.join(vazia, "dados"))
        c = regua.contar(vazia)
        afirma("raiz sem banco nenhum conta zero banco", c["bancos"] == [], str(c["bancos"]))
        afirma("e da zero sem piso, que lido sozinho diria 'cano inteiro'",
               c["totais"]["sem_url_busca"] == 0 and c["totais"]["registros"] == 0,
               str(c["totais"]))
        banco_de_mentira(vazia, "filtro", [])
        c2 = regua.contar(vazia)
        afirma("banco presente e vazio conta o banco e zero registro",
               c2["bancos"] == ["produtos-filtro.json"] and c2["totais"]["registros"] == 0,
               "%s / %s" % (c2["bancos"], c2["totais"]))
    finally:
        shutil.rmtree(vazia, ignore_errors=True)


# ---------------------------------------------------------------------------
# (D) O PORTAO INTEIRO, NUMA ILHA DE SOMBRA
# ---------------------------------------------------------------------------
def ilha_de_sombra():
    tmp = tempfile.mkdtemp(prefix="aqm-cano-ilha-")
    for pasta in ("dados", "ferramentas"):
        shutil.copytree(os.path.join(RAIZ, pasta), os.path.join(tmp, pasta),
                        ignore=shutil.ignore_patterns("__pycache__"))
    return tmp


def rodar_portao(ilha, *extra):
    p = subprocess.Popen(
        ["python3", os.path.join(ilha, "ferramentas", "conferir-cano-de-links.py")] + list(extra),
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    saida = p.communicate()[0].decode("utf-8", "replace")
    return p.returncode, saida


def mexer_num_registro(ilha, nome, mexida):
    caminho = os.path.join(ilha, "dados", "produtos-%s.json" % nome)
    with io.open(caminho, encoding="utf-8") as f:
        dados = json.load(f)
    mexida(dados["produtos"])
    with io.open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False)


def metade_d():
    print("\n(D) o portao inteiro, numa ilha de sombra")

    ilha = ilha_de_sombra()
    try:
        serie = os.path.join(ilha, "dados", "cano-de-links.md")
        codigo, saida = rodar_portao(ilha)
        afirma("a ilha de sombra nasce com o portao VERDE (a serie veio do main)",
               codigo == 0 and "APROVADO" in saida, saida.strip().splitlines()[-1:])

        guardada = io.open(serie, encoding="utf-8").read()
        os.remove(serie)
        codigo, saida = rodar_portao(ilha)
        afirma("sem a serie o portao REPROVA e diz que falta declaracao",
               codigo == 1 and "REPROVADO" in saida and "declaracao" in saida,
               saida.strip().splitlines()[-1:])
        with io.open(serie, "w", encoding="utf-8") as f:
            f.write(guardada)

        # A MUDANCA QUE NAO MOVE TOTAL NENHUM: um registro de degrau 3 perde a
        # ficha e outro, de degrau 4, ganha uma. Totais e distribuicao de degrau
        # ficam iguais; o que muda e QUEM esta em cada degrau.
        def trocar(produtos):
            com = [p for p in produtos if (p.get("afiliado") or {}).get("url_produto")]
            sem = [p for p in produtos if not (p.get("afiliado") or {}).get("url_produto")]
            alvo_sem = sem[0]
            alvo_com = com[0]
            alvo_sem["afiliado"]["url_produto"] = alvo_com["afiliado"].pop("url_produto")

        mexer_num_registro(ilha, "aquecedor", trocar)
        codigo, saida = rodar_portao(ilha)
        afirma("registro que muda de estado com o total intacto REPROVA o portao",
               codigo == 1 and "REPROVADO" in saida and "item por item" in saida,
               saida.strip().splitlines()[-1:])
        afirma("e o portao nomeia os dois registros que mudaram",
               saida.count("medido '") >= 1, "a falha tem de dizer quem mudou")

        codigo, saida = rodar_portao(ilha, "--gravar")
        afirma("--gravar fecha a serie e sai com codigo 0", codigo == 0, str(codigo))
        codigo, saida = rodar_portao(ilha)
        afirma("depois do --gravar o portao volta a VERDE",
               codigo == 0 and "APROVADO" in saida, saida.strip().splitlines()[-1:])
        texto = io.open(serie, encoding="utf-8").read()
        afirma("a serie cresceu por cima e nao sobrescreveu a secao antiga",
               texto.count("\n## ") >= 2, "%d secao(oes)" % texto.count("\n## "))

        # REGISTRO NOVO: a leva que entra pela porta de tras (25.2-b).
        def acrescentar(produtos):
            produtos.append({"id": "leva-nova-sem-piso", "afiliado": {}})

        mexer_num_registro(ilha, "midia", acrescentar)
        codigo, saida = rodar_portao(ilha)
        afirma("registro novo sem declaracao REPROVA o portao",
               codigo == 1 and "midia/leva-nova-sem-piso" in saida,
               saida.strip().splitlines()[-3:])

        # DECLARACAO COM TOTAL DIGITADO: o numero ao lado nao manda.
        codigo, _ = rodar_portao(ilha, "--gravar")
        texto = io.open(serie, encoding="utf-8").read()
        # O numero ao lado nao manda: some um registro do total DECLARADO sem
        # tocar nos itens declarados. Lido do proprio arquivo, nunca digitado.
        marca = '"registros": '
        i = texto.index(marca) + len(marca)
        j = i
        while texto[j].isdigit():
            j += 1
        texto = texto[:i] + str(int(texto[i:j]) - 1) + texto[j:]
        with io.open(serie, "w", encoding="utf-8") as f:
            f.write(texto)
        codigo, saida = rodar_portao(ilha)
        afirma("total declarado que nao fecha com os itens declarados REPROVA",
               codigo == 1 and "totais declarados" in saida,
               saida.strip().splitlines()[-1:])
    finally:
        shutil.rmtree(ilha, ignore_errors=True)


# ---------------------------------------------------------------------------
# (E) A DENUNCIA DA BANCADA, NOS DOIS SENTIDOS
# ---------------------------------------------------------------------------
def rodar_bancada(ilha):
    p = subprocess.Popen(
        ["python3", os.path.join(ilha, "ferramentas", "bancada.py"), "--lista"],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=ilha)
    return p.communicate()[0].decode("utf-8", "replace")


def metade_e():
    print("\n(E) a denuncia da bancada, nos dois sentidos")

    ilha = ilha_de_sombra()
    try:
        saida = rodar_bancada(ilha)
        afirma("a bancada nao denuncia mais o contador do cano",
               "contar-cano-de-links.py" not in saida.split("SEM CONVENCAO")[-1],
               saida.strip().splitlines()[-1:])
        afirma("e os tres portoes do cano entraram na passada sem rede",
               all(n in saida for n in ("conferir-cano-de-links.py",
                                        "teste-cano-de-links.py",
                                        "mutacoes-cano-de-links.py")))

        # O CONTRARIO: contador com regua que portao nenhum carrega. Ele TEM de
        # continuar denunciado, senao a regra nova so serviu para calar.
        #
        # OS DOIS NOMES SAO MONTADOS POR PEDACO, E ISSO NAO E ENFEITE: a
        # pergunta da bancada e "algum portao desta pasta CITA este nome?", e
        # ESTE ARQUIVO e um portao. Escrito inteiro aqui, o nome do arquivo de
        # mentira apareceria citado por mim e a bancada o chamaria de protegido
        # — o teste provaria o contrario do que pretende. Medido na primeira
        # passada desta metade, em 19/10/2026: as duas afirmacoes falharam
        # exatamente assim.
        falso_contador = "contar-" + "ninguem" + ".py"
        falsa_regua = "regua-" + "ninguem" + ".py"
        falso_gerador = "gerar-" + "ninguem" + ".py"
        # O TERCEIRO ARQUIVO E O QUE DA SENTIDO AOS DOIS PRIMEIROS: um arquivo
        # de PRODUCAO que carrega a falsa regua. E ele que separa a pergunta
        # estrita ("algum PORTAO carrega?") da antiga ("algum arquivo cita?").
        # Sem ele, a falsa regua nao e citada por ninguem e as duas afirmacoes
        # abaixo ficariam verdes com qualquer uma das duas perguntas — medido em
        # 19/10/2026, quando a mutacao que apaga o filtro SOBREVIVEU a esta
        # metade.
        #
        # E A CITACAO TEM DE SER UM ATO, NAO UM COMENTARIO (20/10/2026). Ate
        # hoje o corpo do falso gerador era `# producao que carrega <regua>`, e
        # isso bastava porque a bancada perguntava se o nome APARECIA no texto.
        # Desde 20/10 ela pergunta em que POSICAO ele aparece, e comentario nao
        # carrega nada — entao o mundo deixou de discriminar e a mutacao 15
        # SOBREVIVEU outra vez, pelo motivo oposto ao de 19/10. O corpo agora
        # CARREGA de verdade, no idioma desta pasta (o nome entre aspas dentro
        # do `spec_from_file_location`), e o filtro do PORTAO volta a ser a
        # unica coisa entre a falsa regua e a protecao.
        carga = ('import importlib.util\n'
                 '_s = importlib.util.spec_from_file_location("r", "%s")\n')
        for nome, corpo in ((falso_contador, carga % falsa_regua),
                            (falso_gerador, carga % falsa_regua),
                            (falsa_regua, "# nenhum portao me carrega\n")):
            with io.open(os.path.join(ilha, "ferramentas", nome), "w", encoding="utf-8") as f:
                f.write("#!/usr/bin/env python3\n" + corpo)
        saida = rodar_bancada(ilha)
        denunciados = saida.split("SEM CONVENCAO, ninguem roda:")[-1]
        afirma("contador cuja regua nenhum portao carrega CONTINUA denunciado",
               falso_contador in denunciados, denunciados.strip())
        afirma("e a regua que portao nenhum carrega tambem",
               falsa_regua in denunciados, denunciados.strip())
    finally:
        shutil.rmtree(ilha, ignore_errors=True)


def main():
    print("TESTE DO CANO DE LINKS — regua, contador e portao")
    regua = carregar_regua()
    metade_a(regua)
    metade_b()
    metade_c(regua)
    metade_d()
    metade_e()
    print("")
    if falhas:
        print("REPROVADO: %d de %d afirmacoes falharam" % (len(falhas), afirmacoes))
        for f in falhas:
            print("  - %s" % f)
        return 1
    print("APROVADO: %d afirmacoes, 0 falha" % afirmacoes)
    return 0


if __name__ == "__main__":
    sys.exit(main())
