#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MUTACOES DA SOBRA DECLARADA — 06/10/2026, esquema v13.

O buraco que esta bateria fecha nao era um campo errado nem um campo sem portao:
era um campo CERTO, COMPLETO E INVISIVEL. `propriedades.sobra_recomendada_pct`
foi gravado em 30/09/2026 no `pastilhart-af1500`, com valor, unidade, fonte_id e
`declarado_como` — e passou seis dias sem uma linha de tela le-lo, na ferramenta
que PERGUNTA a sobra ao visitante. O validador aprovava, porque a forma estava
certa; a bancada aprovava, porque nenhuma afirmacao falava do campo.

E PIOR: em 06/10/2026 dois lugares do repositorio — o `PROMPT.md` da ilha e dois
campos de prosa do proprio registro — escreveram que o numero "nao foi gravado
como propriedade de proposito" e que `propriedades.sobra_declarada_pct` seria
CAMPO NOVO. Quem seguisse a promessa ao pe da letra teria gravado a MESMA
declaracao duas vezes, uma das duas vazia, e a tela que lesse a vazia publicaria
ausencia sobre um dado que o banco tem.

POR QUE ESTA BATERIA RODA DUAS FERRAMENTAS, e nao so o validador como as irmas:
porque o defeito desta familia nao mora na forma do dado, mora no SILENCIO da
tela. Portao de forma nunca o pegaria — ele nao pegou, por seis dias, com o dado
em forma perfeita. Entao metade das mutacoes daqui vai ao `validar-banco.py` (a
forma e o nome) e metade vai ao `teste-f1.php` (a tela): apagar a declaracao do
banco TEM de fazer a bancada da F1 reprovar, e e essa reprovacao que prova que a
pagina le o campo em vez de repetir um texto fixo que parece le-lo.

AS TRES REGRAS HERDADAS das baterias irmas, e as tres mordem aqui:

  (a) Mutacao que o portao ANTIGO ja pegava nao justifica portao novo. Cada
      mutacao de forma roda o validador duas vezes, desligando o portao novo com
      CDM_SEM_PORTAO_SOBRA=1.

  (b) A mutacao mais valiosa e a que PRODUZ O MUNDO que o banco nao tem. Sao
      tres aqui, e sao as tres mais caras: m08 faz um produto RECOMENDAVEL
      (nivel 3, dentro do teto da escada) declarar sobra, estado que hoje nao
      existe — o unico declarante do banco e nivel 5; m09 faz um FABRICANTE
      declarar, para a atribuicao da tela ter de mudar de palavra; e m10 cria o
      SEGUNDO declarante, que e o que quebra qualquer frase escrita no singular.

  (c) ESTA BATERIA MEDE O FALSO POSITIVO. Tres estados legitimos tem de passar,
      entre eles o que mais se parece com defeito: produto que simplesmente NAO
      declara sobra, que e o estado de 12 dos 13 itens.

Uso:  python3 ferramentas/mutacoes-sobra.py
"""

import copy
import json
import os
import shutil
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)
VALIDAR_BANCO = os.path.join(AQUI, "validar-banco.py")
TESTE_F1 = os.path.join(AQUI, "teste-f1.php")

ARQUIVOS = {
    "pastilhas": os.path.join(ILHA, "dados", "materiais-pastilhas.json"),
    "esquema":   os.path.join(ILHA, "dados", "esquema-banco.json"),
}

DECLARANTE = "pastilhart-af1500"
CHAVE = "sobra_recomendada_pct"


def item(banco, ident):
    for m in banco["materiais"]:
        if m["id"] == ident:
            return m
    raise SystemExit("mutacao aponta para item inexistente: %s" % ident)


def sb(banco, ident=DECLARANTE):
    return item(banco, ident)["propriedades"][CHAVE]


def sem_declaracao(banco, ident):
    """Um item que NAO declara sobra, para servir de molde."""
    for m in banco["materiais"]:
        if m["id"] == ident:
            return m
    raise SystemExit("molde inexistente: %s" % ident)


# ------------------------------------------------- mutacoes de FORMA (validador)

def m01(b):
    """O NOME EM DOBRO, e e a mutacao que restaura a promessa que o repositorio
    tinha escrito: o mesmo numero ganha uma SEGUNDA chave, `sobra_declarada_pct`.
    Nao e hipotese — era o que o PROMPT.md e o proprio registro mandavam fazer em
    06/10/2026. Duas chaves para a mesma declaracao envelhecem separadas, e a tela
    que ler a vazia publica ausencia sobre um dado que o banco tem."""
    p = item(b, DECLARANTE)["propriedades"]
    p["sobra_declarada_pct"] = copy.deepcopy(p[CHAVE])


def m02(b):
    """A segunda chave nasce VAZIA, que e como ela teria nascido de verdade: quem
    cria campo novo para um numero que ja existe grava o campo antes de ter o
    numero. E a forma silenciosa da m01 — sem valor, nenhuma regra de propriedade
    a cobra."""
    item(b, DECLARANTE)["propriedades"]["sobra_declarada_pct"] = {
        "valor": None,
        "motivo": "a coletar",
    }


def m03(b):
    """Valor sem `literal_do_fabricante`. O numero vai a tela e a linha dele nao:
    a pagina passa a afirmar que ele pede 10% com as palavras da ilha, que e a
    26.3 ao contrario com um numero dentro."""
    sb(b)["literal_do_fabricante"] = ""


def m04(b):
    """Valor sem `declarada_por`. Sem ele a tela so pode ADIVINHAR a atribuicao —
    e a atribuicao certa aqui e `distribuidor`, nao fabricante. E o campo de 26.1
    que torna a diferenca mensuravel."""
    del sb(b)["declarada_por"]


def m05(b):
    """`declarada_por` fora do vocabulario do esquema. `importadora` parece certo
    e nao e uma das tres classes — e quem le o banco nao sabe se a tela pode
    chamar isso de fabricante."""
    sb(b)["declarada_por"] = "importadora"


def m06(b):
    """Valor sem `como_a_tela_chama_quem_declarou`. O artigo vem no campo porque
    genero de substantivo nao se adivinha em PHP — mesma razao da preposicao em
    `como_a_tela_chama_o_documento`, que o bloco do preparo pagou com um render
    servindo `Esta escrito em a pagina de produto dele`."""
    sb(b)["como_a_tela_chama_quem_declarou"] = ""


def m07(b):
    """Unidade trocada de `%` para `pct`. A F1 soma este numero a uma porcentagem;
    unidade errada aqui nao e erro de catalogo, e pastilha comprada a mais ou a
    menos."""
    sb(b)["unidade"] = "pct"


def m07b(b):
    """Valor fora da faixa de porcentagem. 110% de sobra nao e sobra: e o dobro da
    compra, e passaria calado por qualquer regua que so olhasse presenca."""
    sb(b)["valor"] = 110


def m07c(b):
    """Valor como TEXTO. `"10"` parece igual a 10 e nao e: a conta da F1 soma, e
    quem soma texto em PHP herda a coercao silenciosa da linguagem."""
    sb(b)["valor"] = "10"


def m07d(b):
    """Valor sem `lido_em`. Quem cita linha de documento diz o dia em que a abriu —
    documento relido hoje e outra coisa de documento lido em setembro."""
    sb(b)["lido_em"] = "06 de outubro"


def m08e(b):
    """A TRAVA DA 26.2, primeira metade: o esquema perde
    `regras_do_campo_sobra_declarada` e o portao fica sem regra. Regua que le a
    propria lista de um arquivo de dados aprova tudo em silencio no dia em que o
    arquivo perder a chave."""
    del b["regras_do_campo_sobra_declarada"]


def m08f(b):
    """A TRAVA DA 26.2, segunda metade: a chave do esquema continua e o VOCABULARIO
    de quem pode declarar fica vazio. E a forma silenciosa do mesmo defeito — o
    portao continua existindo e nao cobra ninguem."""
    b["regras_do_campo_sobra_declarada"]["quem_pode_declarar"] = {}


def m08g(b):
    """O esquema deixa de dizer QUAL e o nome do campo. Sem ele o portao do nome em
    dobro nao tem contra o que comparar, e a m01 volta a passar."""
    b["regras_do_campo_sobra_declarada"]["o_nome_do_campo_e_UM_e_este"] = "a sobra declarada"


# ----------------------------------------------------- mutacoes de TELA (bancada)

def t01(b):
    """A DECLARACAO DESAPARECE DO BANCO. Esta e a mutacao que mede o defeito
    original: se a bancada da F1 continuar verde sem a declaracao, a pagina nao a
    le — ela repete um texto que PARECE le-la. Foi exatamente esse o estado de
    30/09 a 06/10."""
    del item(b, DECLARANTE)["propriedades"][CHAVE]


def t02(b):
    """O NUMERO MUDA e a tela tem de mudar com ele. 10 vira 20, que e uma das
    opcoes do seletor — entao o link de refazer a conta tambem tem de mudar. Numero
    de tela digitado passaria aqui sem piscar."""
    s = sb(b)
    s["valor"] = 20
    s["literal_do_fabricante"] = "Compre 20% a mais para cortes e ajustes na aplicação."


def t03(b):
    """PRODUZ O MUNDO: o declarante vira RECOMENDAVEL. A fonte dele cai para nivel
    3, dentro do teto da escada, e a ressalva de "nao entra na nossa recomendacao"
    TEM de sair da tela. Hoje este estado nao existe no banco — o unico declarante
    e nivel 5 —, e regua escrita para um mundo que nunca acontece nasce errada sem
    poder falhar (secao 8)."""
    m = item(b, DECLARANTE)
    for f in m["fontes"].values():
        f["nivel"] = 3


def t04(b):
    """PRODUZ O MUNDO: quem declara passa a ser FABRICANTE. A tela nao pode mais
    dizer "e nao quem fabrica a pastilha" — a palavra da atribuicao sai do campo,
    nao do codigo, e e esta mutacao que prova isso."""
    s = sb(b)
    s["declarada_por"] = "fabricante"
    s["como_a_tela_chama_quem_declarou"] = "a própria fábrica da pastilha"


def t05(b):
    """PRODUZ O MUNDO: o SEGUNDO declarante. Um item de 2,5 cm passa a declarar
    sobra, e com ele cai qualquer frase escrita no singular — "1 de 13", "um deles
    e", "publica". O banco tem um declarante so, e verde sobre um mundo de um
    elemento nao e medicao."""
    m = sem_declaracao(b, "glassmosaic-k2501")
    fonte_id = list(m["fontes"].keys())[0]
    m["propriedades"][CHAVE] = {
        "valor": 15,
        "unidade": "%",
        "fonte_id": fonte_id,
        "declarado_como": "comprar 15% a mais",
        "literal_do_fabricante": "Compre 15% a mais para recortes.",
        "declarada_por": "fabricante",
        "como_a_tela_chama_quem_declarou": "a Glass Mosaic, que fabrica a pastilha",
        "lido_em": "2026-10-06",
    }


MUTACOES_FORMA = [
    ("m01 PRODUZ: a segunda chave do mesmo numero (a promessa escrita)", "pastilhas", m01),
    ("m02 a segunda chave nasce VAZIA (a forma silenciosa da m01)",     "pastilhas", m02),
    ("m03 valor sem literal_do_fabricante",                             "pastilhas", m03),
    ("m04 valor sem declarada_por",                                     "pastilhas", m04),
    ("m05 declarada_por fora do vocabulario do esquema",                "pastilhas", m05),
    ("m06 valor sem como_a_tela_chama_quem_declarou",                   "pastilhas", m06),
    ("m07 unidade trocada de %% para pct",                              "pastilhas", m07),
    ("m08 valor fora da faixa de porcentagem (110)",                    "pastilhas", m07b),
    ("m09 valor como TEXTO em vez de numero",                           "pastilhas", m07c),
    ("m10 valor sem lido_em em forma ISO",                              "pastilhas", m07d),
    ("m11 26.2: o esquema perde regras_do_campo_sobra_declarada",       "esquema",   m08e),
    ("m12 26.2: o vocabulario quem_pode_declarar fica vazio",           "esquema",   m08f),
    ("m13 26.2: o esquema deixa de dizer o nome do campo",              "esquema",   m08g),
]

# A METADE DE TELA NAO COBRA REPROVACAO, E ISSO FOI MEDIDO E NAO ESCOLHIDO. A
# primeira versao deste arquivo exigia que toda mutacao de banco deixasse a
# bancada da F1 VERMELHA, e duas passaram verdes: trocar os 10% por 20% e baixar
# a fonte para nivel 3. Nao eram buracos — eram a bancada funcionando. As
# afirmacoes da secao 6b do `teste-f1.php` DERIVAM do arquivo, entao quando o
# mundo muda elas mudam com ele; exigir vermelho ali era exigir que a regua
# reprovasse a MELHORA, que e a cicatriz da regua amarrada a um degrau (secao 8).
#
# Mundo que muda nao e defeito. O que PRECISA ser medido e outra coisa, e e a
# dobradica deste bloco inteiro: que a PAGINA SERVIDA mude quando o banco muda.
# Tela que repete um texto fixo parecido com o dado fica identica — e foi
# exatamente esse o estado de 30/09 a 06/10/2026, com o campo gravado e nenhuma
# linha de snippet lendo a palavra.
#
# Entao cada mutacao de tela declara TRES coisas: o estado da pagina a medir, o
# que tem de APARECER nela depois da mutacao, e o que tem de DESAPARECER. Mais a
# exigencia, para todas, de a bancada continuar verde.

ESTADO_P15 = "forma=cilindro&d=25&h=35&pastilha=p15&junta=2&sobra=15&esp=4&rejunte=cimenticio"
ESTADO_P25 = "forma=cilindro&d=25&h=35&pastilha=p25&junta=2&sobra=15&esp=4&rejunte=cimenticio"

MUTACOES_TELA = [
    {
        "nome": "t01 a declaracao DESAPARECE do banco",
        "qual": "pastilhas", "funcao": t01, "estado": ESTADO_P15,
        "sai": ["Compre 10% a mais", "a Pastilhart, que importa"],
        "entra": [],
        "por_que": "sem o campo, o bloco inteiro tem de sumir da pagina — era o estado real de 30/09 a 06/10",
    },
    {
        "nome": "t02 o numero muda de 10 para 20",
        "qual": "pastilhas", "funcao": t02, "estado": ESTADO_P15,
        "sai": ["Compre 10% a mais", "sobra=10"],
        "entra": ["Compre 20% a mais", "sobra=20"],
        "por_que": "o numero e o link de refazer a conta saem do banco; texto fixo ficaria identico",
    },
    {
        "nome": "t03 PRODUZ: o declarante vira RECOMENDAVEL (nivel 3)",
        "qual": "pastilhas", "funcao": t03, "estado": ESTADO_P15,
        "sai": ["não entra na nossa recomendação"],
        "entra": [],
        "por_que": "dentro do teto da escada a ressalva do nivel nao se aplica e nao pode ser servida",
    },
    {
        "nome": "t04 PRODUZ: quem declara passa a ser FABRICANTE",
        "qual": "pastilhas", "funcao": t04, "estado": ESTADO_P15,
        "sai": ["não quem fabrica a pastilha", "a Pastilhart, que importa"],
        "entra": ["a própria fábrica da pastilha"],
        "por_que": "a palavra da atribuicao sai do campo `declarada_por`, nunca do codigo (26.3)",
    },
    {
        "nome": "t05 PRODUZ: nasce o SEGUNDO declarante",
        "qual": "pastilhas", "funcao": t05, "estado": ESTADO_P25,
        "sai": [],
        "entra": ["Compre 15% a mais", "a Glass Mosaic, que fabrica a pastilha"],
        "por_que": "o lado de 2,5 cm nao tinha bloco nenhum; com o segundo declarante ele passa a ter",
    },
]


# ----------------------------------------- a trava do falso positivo (regra c)

def fp1(b):
    """O ESTADO DE 12 DOS 13 ITENS: produto que simplesmente nao declara sobra. E o
    que mais se parece com defeito e e o mais comum do banco — portao que o
    reprovasse cobraria doze motivos que ninguem ia ler."""
    item(b, "glassmosaic-k77")["propriedades"]["peso_caixa_kg"]["valor"] = \
        item(b, "glassmosaic-k77")["propriedades"]["peso_caixa_kg"]["valor"]
    item(b, "glassmosaic-k77")["observacao"] = \
        (item(b, "glassmosaic-k77").get("observacao") or "") + " "


def fp2(b):
    """Sobra ZERO declarada. Zero e numero e e declaracao: um fabricante que diga
    "nao precisa comprar a mais" tem de passar, e a faixa comeca em 0 por isso."""
    s = sb(b)
    s["valor"] = 0
    s["literal_do_fabricante"] = "Não é preciso comprar a mais: a placa já vem com folga."


def fp3(b):
    """Sobra declarada por LOJA, que e a terceira classe do vocabulario e a mais
    fraca. Ela tem de passar pela forma — o que a classe muda e a PALAVRA da tela,
    nunca o direito de o dado existir."""
    s = sb(b)
    s["declarada_por"] = "loja"
    s["como_a_tela_chama_quem_declarou"] = "a loja que vende a placa"


FALSOS_POSITIVOS = [
    ("produto que NAO declara sobra (12 dos 13)",       "pastilhas", fp1),
    ("sobra ZERO declarada, que e declaracao",          "pastilhas", fp2),
    ("sobra declarada por LOJA (a classe mais fraca)",  "pastilhas", fp3),
]


def roda_validador(sem_portao_novo=False):
    env = dict(os.environ)
    if sem_portao_novo:
        env["CDM_SEM_PORTAO_SOBRA"] = "1"
    r = subprocess.run([sys.executable, VALIDAR_BANCO], capture_output=True,
                       text=True, cwd=ILHA, env=env)
    return r.returncode != 0


def roda_bancada():
    r = subprocess.run(["php", TESTE_F1, "."], capture_output=True, text=True, cwd=ILHA)
    return r.returncode != 0


RENDER = os.path.join(AQUI, "render-para-teste.php")


def serve(estado):
    """O HTML que a pagina serve naquele estado, pelo render de bancada."""
    r = subprocess.run(["php", RENDER, ".", "cdm_f1", "hoje", estado],
                       capture_output=True, text=True, cwd=ILHA)
    return r.stdout


def mede_tela(mut):
    """Devolve (bancada_verde, html). Um processo por estado, como a secao 8 manda."""
    return (not roda_bancada(), serve(mut["estado"]))


def escreve_e_roda(arquivo, mutado, como):
    backup = arquivo + ".original"
    shutil.copy2(arquivo, backup)
    try:
        with open(arquivo, "w", encoding="utf-8") as fh:
            json.dump(mutado, fh, ensure_ascii=False, indent=2)
        return como()
    finally:
        shutil.move(backup, arquivo)


def main():
    originais = {k: json.load(open(v, encoding="utf-8")) for k, v in ARQUIVOS.items()}

    if roda_validador():
        print("FALHA: o banco ja esta reprovado ANTES de qualquer mutacao")
        return 1
    if roda_validador(sem_portao_novo=True):
        print("FALHA: o banco ja esta reprovado com o portao da sobra desligado")
        return 1
    if roda_bancada():
        print("FALHA: a bancada da F1 ja esta vermelha ANTES de qualquer mutacao")
        return 1

    print("Mutacoes da sobra declarada (esquema v13) — %d de forma + %d de tela"
          % (len(MUTACOES_FORMA), len(MUTACOES_TELA)))
    print("")
    print("  A FORMA E O NOME — quem pega e o validar-banco.py:")
    reprovadas = 0
    so_o_portao_novo = 0
    for nome, qual, funcao in MUTACOES_FORMA:
        arquivo = ARQUIVOS[qual]
        mutado = copy.deepcopy(originais[qual])
        funcao(mutado)
        if mutado == originais[qual]:
            print("    INERTE  %s — a mutacao nao mudou nada" % nome)
            continue
        pegou = escreve_e_roda(arquivo, mutado, roda_validador)
        pegou_sem = escreve_e_roda(arquivo, mutado, lambda: roda_validador(sem_portao_novo=True))
        if pegou:
            reprovadas += 1
            if not pegou_sem:
                so_o_portao_novo += 1
                print("    REPROVOU  %-60s (so o portao novo viu)" % nome)
            else:
                print("    REPROVOU  %-60s (outro portao tambem pega)" % nome)
        else:
            print("    PASSOU    %-60s  <-- NENHUM PORTAO VIU" % nome)

    print("")
    print("  A TELA — a pagina servida tem de MUDAR quando o banco muda, e a")
    print("  bancada tem de continuar verde (mundo que muda nao e defeito):")
    tela_ok = 0
    html_base = {}
    for mut in MUTACOES_TELA:
        html_base.setdefault(mut["estado"], serve(mut["estado"]))
    for mut in MUTACOES_TELA:
        arquivo = ARQUIVOS[mut["qual"]]
        mutado = copy.deepcopy(originais[mut["qual"]])
        mut["funcao"](mutado)
        if mutado == originais[mut["qual"]]:
            print("    INERTE  %s — a mutacao nao mudou nada" % mut["nome"])
            continue
        verde, html = escreve_e_roda(arquivo, mutado, lambda: mede_tela(mut))
        faltas = []
        if not verde:
            faltas.append("a bancada ficou VERMELHA (a regua nao e derivada)")
        if html == html_base[mut["estado"]]:
            faltas.append("o HTML servido NAO mudou (a tela nao le o campo)")
        for termo in mut["sai"]:
            if termo in html:
                faltas.append("ficou na tela o que devia sair: %s" % termo)
        for termo in mut["entra"]:
            if termo not in html:
                faltas.append("nao entrou na tela o que devia entrar: %s" % termo)
        if not faltas:
            tela_ok += 1
            print("    REAGIU    %-60s %s" % (mut["nome"], mut["por_que"]))
        else:
            print("    FALHOU    %-60s  <-- %s" % (mut["nome"], "; ".join(faltas)))

    print("")
    print("  A TRAVA DO FALSO POSITIVO — o banco certo tem de PASSAR:")
    falsos = 0
    for rotulo, qual, funcao in FALSOS_POSITIVOS:
        mutado = copy.deepcopy(originais[qual])
        funcao(mutado)
        if escreve_e_roda(ARQUIVOS[qual], mutado, roda_validador):
            falsos += 1
            print("    FALSO POSITIVO  %-50s  <-- o portao reprovou banco legitimo" % rotulo)
        else:
            print("    passou          %s" % rotulo)

    print("")
    print("  reprovadas pela forma .......... %d de %d" % (reprovadas, len(MUTACOES_FORMA)))
    print("  so o portao novo viu ........... %d" % so_o_portao_novo)
    print("  a tela reagiu .................. %d de %d" % (tela_ok, len(MUTACOES_TELA)))
    print("  falso positivo ................. %d  (tem de ser 0)" % falsos)
    if reprovadas != len(MUTACOES_FORMA) or tela_ok != len(MUTACOES_TELA):
        print("\nREPROVADO: mutacao de forma que passa e buraco de portao; mutacao de tela "
              "que nao muda o HTML e tela que nao le o banco, que e o defeito inteiro "
              "deste bloco.")
        return 1
    if so_o_portao_novo == 0:
        print("\nREPROVADO: se os portoes antigos pegam tudo, o novo nao se justifica.")
        return 1
    if falsos:
        print("\nREPROVADO: portao que reprova o banco certo e desligado pela primeira "
              "pessoa com pressa.")
        return 1
    print("\nOK: as %d mutacoes de forma reprovaram (%d so pelo portao novo), a tela reagiu "
          "as %d mudancas de banco sem a bancada ficar vermelha, e os %d estados legitimos "
          "passaram." % (len(MUTACOES_FORMA), so_o_portao_novo, len(MUTACOES_TELA),
                         len(FALSOS_POSITIVOS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
