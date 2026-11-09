#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
O NOME EXIBIDO DE UM REGISTRO E DECIDIDO NUM LUGAR SO — E ESTE PORTAO IMPEDE A
SEXTA COPIA DE NASCER (09/11/2026, item 1 do despacho da ronda de hoje).

POR QUE ELE EXISTE, e nao e para conferir a funcao: e para conferir que NINGUEM
A CONTORNA. O defeito do item 1 nao foi uma funcao errada — foi a MESMA pergunta
respondida em SEIS lugares, com CINCO respostas, e a resposta certa existindo
desde 29/10 dentro de `regras/f3.py`, onde ninguem a achava. Consertar os seis
sem este portao conserta hoje: a proxima linha de gerador escrita de cabeca
reabre o buraco, e ela SERA escrita, porque `" ".join(x for x in (r.get("marca"),
r.get("modelo")) if x)` e o que sai da mao de quem esta com pressa.

E A LICAO QUE ESTA ILHA JA TINHA ESCRITA, na 20.4 do ARQUIPELAGO.md: *"conserto
escrito em registro de ilha conserta aquele dia; regra escrita aqui vale para as
tres ilhas"*. Aqui o andar e um abaixo — conserto escrito em seis linhas conserta
aquelas seis; portao escrito contra a CLASSE vale para a setima.

AS DUAS METADES:

  1. A FUNCAO FAZ O QUE DIZ, em mundos fabricados, inclusive os QUATRO registros
     de verdade que estavam servindo slug no ar.
  2. NINGUEM DERIVA NOME POR CONTA PROPRIA. A varredura procura o padrao
     `marca`+`modelo` montado a mao em `ferramentas/` e `regras/`, e DENUNCIA.
     A afirmacao e POSITIVA no sentido da 20.8: nao procuro a frase ruim que
     imaginei — exijo que todo lugar que toque `marca` e `modelo` juntos seja
     `regras/nomes.py` ou uma chamada a ele.

E A TERCEIRA METADE, A QUE FAZ ISTO SER MEDICAO E NAO INTENCAO (20.8): um dos
mundos refaz a REGRA VELHA ao lado da nova e EXIGE QUE AS DUAS DISCORDEM. As
cinco regras velhas discordavam da nova em registro sem marca; autoteste em que
as duas concordam nao mede conserto nenhum.
"""
import importlib.util
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)

_spec = importlib.util.spec_from_file_location("nomes", os.path.join(ILHA, "regras", "nomes.py"))
nomes = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(nomes)

FALHAS = []


def falha(msg):
    FALHAS.append(msg)
    print("FALHA %s" % msg)


# ---------------------------------------------------------------------------
# AS CINCO REGRAS VELHAS, REESCRITAS AQUI PARA O MUNDO DA DISCORDANCIA (20.8).
# Elas nao sao chamadas pelo codigo de producao: existem para que o portao possa
# provar que o conserto MUDOU a resposta. Autoteste que nao sabe o que havia
# antes nao sabe se consertou.
# ---------------------------------------------------------------------------
def velha_f2_cai_no_id(r):
    return " ".join(x for x in (r.get("marca"), r.get("modelo")) if x) or r.get("id")


def velha_f1_corta_em_60(r):
    return (" ".join(x for x in (r.get("marca"), r.get("modelo")) if x)
            or (r.get("titulo_colhido") or "")[:60])


def velha_f1_sem_fallback(r):
    return " ".join(x for x in (r.get("marca"), r.get("modelo")) if x)


# ---------------------------------------------------------------------------
# 1. A FUNCAO
# ---------------------------------------------------------------------------
MUNDOS = [
    ("marca e modelo", {"marca": "MAXSHOT", "modelo": "V1", "id": "maxshot-v1"}, "MAXSHOT V1"),
    ("so marca", {"marca": "SOUSA", "modelo": None, "id": "sousa-x"}, "SOUSA"),
    ("so modelo", {"marca": None, "modelo": "V1SPRO", "id": "v1spro"}, "V1SPRO"),
    ("marca com espaco em volta", {"marca": "  MAXSHOT  ", "modelo": " V1 ", "id": "m"},
     "MAXSHOT V1"),
    ("so titulo colhido", {"marca": None, "modelo": None,
                           "titulo_colhido": "Patinete eletrico adulto com banco (147 vendas)",
                           "id": "patinete-adulto-com-banco-shopee"},
     "Patinete eletrico adulto com banco (147 vendas)"),
    ("titulo LONGO nao e cortado", {"marca": None, "modelo": None,
                                    "titulo_colhido": "o modelo 'melhor de 2026' de uma lista "
                                                      "comercial (2 x 1.000 W, 72 km/h)",
                                    "id": "guia-melhor-de-2026"},
     "o modelo 'melhor de 2026' de uma lista comercial (2 x 1.000 W, 72 km/h)"),
    ("titulo vazio cai no id", {"marca": None, "modelo": None, "titulo_colhido": "",
                                "id": "ultimo-recurso"}, "ultimo-recurso"),
    ("sem nada devolve vazio, e isso e denuncia", {}, ""),
]

for nome_do_mundo, registro, esperado in MUNDOS:
    obtido = nomes.nome_do_registro(registro)
    if obtido != esperado:
        falha("mundo %r: esperava %r e veio %r" % (nome_do_mundo, esperado, obtido))

for nome_do_mundo, registro, _esp in MUNDOS:
    _n, fonte = nomes.nome_e_fonte(registro)
    esperada = ("banco" if (registro.get("marca") or registro.get("modelo"))
                else ("titulo_do_anuncio" if (registro.get("titulo_colhido") or "").strip()
                      else "id"))
    if fonte != esperada:
        falha("mundo %r: a fonte do nome deveria ser %r e veio %r"
              % (nome_do_mundo, esperada, fonte))

# ---------------------------------------------------------------------------
# 1-b. O MUNDO DA DISCORDANCIA (20.8): as regras velhas TEM de divergir da nova
#      nos quatro registros de verdade. Se concordarem, este portao nao mede
#      conserto nenhum e diz isso em vez de aprovar.
# ---------------------------------------------------------------------------
with open(os.path.join(ILHA, "dados", "veiculos.json"), encoding="utf-8") as f:
    REGISTROS = json.load(f)["registros"]

SEM_NOME_NO_BANCO = [r for r in REGISTROS if not (r.get("marca") or r.get("modelo"))]
if not SEM_NOME_NO_BANCO:
    falha("nenhum registro do banco tem `marca` e `modelo` null. Este portao perdeu o mundo "
          "que o justifica: era nesses quatro que as cinco regras divergiam. Ou o banco "
          "mudou e isto pede nova medicao, ou a leitura esta errada")

for r in SEM_NOME_NO_BANCO:
    novo = nomes.nome_do_registro(r)
    if novo == velha_f2_cai_no_id(r):
        falha("`%s`: a regra NOVA e a VELHA da F2 concordam (%r). A velha caia no `id` e era "
              "o defeito do item 1 — concordancia aqui significa que o conserto nao mudou "
              "nada" % (r.get("id"), novo))
    if novo == velha_f1_sem_fallback(r):
        falha("`%s`: a regra NOVA concorda com a que NAO tinha fallback (%r), que devolvia "
              "cadeia vazia" % (r.get("id"), novo))
    if novo != r.get("titulo_colhido"):
        falha("`%s`: o nome novo (%r) nao e o `titulo_colhido` inteiro (%r)"
              % (r.get("id"), novo, r.get("titulo_colhido")))

CORTADOS = [r for r in SEM_NOME_NO_BANCO
            if len(r.get("titulo_colhido") or "") > 60]
if not CORTADOS:
    falha("nenhum registro sem marca tem `titulo_colhido` com mais de 60 caracteres. O corte "
          "da F1 era INVISIVEL sem um desses, e a home servia `(2 x 1.000 ` — cortado no meio "
          "do numero. Sem este mundo o portao nao vigia o corte")
for r in CORTADOS:
    if nomes.nome_do_registro(r) == velha_f1_corta_em_60(r):
        falha("`%s`: a regra NOVA e a que cortava em 60 concordam. O corte era o defeito "
              "da home" % r.get("id"))

# ---------------------------------------------------------------------------
# 2. NINGUEM DERIVA NOME POR CONTA PROPRIA.
#
# O PADRAO PROCURADO E O LITERAL que estava nos seis lugares: `marca` e `modelo`
# citados na MESMA expressao. Nao e heuristica de nome de variavel e nao depende
# de alguem ter chamado a coisa de "nome": depende de tocar os dois campos
# juntos, que e o que derivar um nome exige.
#
# O CORTE E POR LINHA LOGICA e nao por linha de arquivo: a expressao original
# ocupava DUAS linhas em `gerar-f1.py`, e um corte por linha fisica nao a veria.
# E a mesma licao do corte de frase da regua de habilitacao, de 06/11.
# ---------------------------------------------------------------------------
#
# E O CORTE ATRAVESSA A QUEBRA DE LINHA, o que foi MEDIDO pelo proprio portao
# reprovando a si mesmo na primeira vez que rodou: a primeira versao deste padrao
# dizia `[^\n]`, e com ela `regras/nomes.py` — a propria funcao — NAO casava,
# porque ela le os dois campos em duas linhas seguidas. O comentario acima ja
# dizia "por linha logica e nao por linha de arquivo" e o codigo dizia o
# contrario: comentario que declara um mecanismo parece conferido e nao mede nada
# (32.5-d). Pior que a liberacao vencida que ele acusou: com `[^\n]`, quem
# escrevesse a derivacao em duas linhas passava CALADO por este portao.
PADRAO = re.compile(r'get\(\s*["\']marca["\']\s*\)[\s\S]{0,240}?get\(\s*["\']modelo["\']\s*\)'
                    r'|get\(\s*["\']modelo["\']\s*\)[\s\S]{0,240}?get\(\s*["\']marca["\']\s*\)')

#: Quem tem o direito de tocar os dois campos juntos. Lista CURTA de proposito:
#: cada nome aqui e uma excecao que alguem teve de justificar.
DONOS = {
    os.path.join("regras", "nomes.py"): "e a propria funcao",
    os.path.join("ferramentas", "teste-nome-do-registro.py"): "e este portao, que refaz as "
                                                              "regras velhas para o mundo da "
                                                              "discordancia",
}

#: NAO HA LISTA DE "QUEM CONFERE IDENTIDADE", E A AUSENCIA FOI MEDIDA — por este
#: portao, reprovando a mim, na terceira vez que rodou (09/11/2026). Eu havia
#: liberado `validar-banco.py` e `mutacoes-banco.py` de antemao, raciocinando que
#: eles cobram a simetria `marca`/`motivo_sem_marca` e portanto tocariam os dois
#: campos juntos. O portao respondeu que as duas liberacoes estao VENCIDAS no
#: minuto em que nasceram: aqueles arquivos leem os campos por um laco sobre
#: tuplas (`for c, mot in (("marca", ...), ("modelo", ...))`) e nunca casam o
#: padrao. Liberacao preventiva e um BURACO PRE-ABERTO — quem escrevesse a
#: derivacao de nome naqueles dois arquivos passaria calado, e eu teria aberto a
#: porta por um raciocinio que nunca medi. Fica escrito porque a tentacao de
#: liberar "para nao dar falso positivo" volta a cada portao novo.

#: QUEM COMPOE CHAVE DE BUSCA TAMBEM NAO ESTA NOMEANDO, E ESTA DISTINCAO FOI
#: MEDIDA POR ESTE PORTAO NA PRIMEIRA VEZ QUE ELE RODOU INTEIRO (09/11/2026).
#: Ele acusou `coletar-piso-de-compra.py`, e a leitura do trecho mostrou outra
#: pergunta: a escada de palavra-chave da 25.1 compoe `marca + modelo + termo`
#: para o buscador da LOJA, e ela PRECISA nao cair no `titulo_colhido` — titulo de
#: anuncio de 70 caracteres e uma busca pessima, e o degrau existe justamente
#: para compor a chave curta que a loja casa. Nome de TELA e para gente ler;
#: chave de BUSCA e para maquina casar. Mesmos dois campos, perguntas opostas.
#: E `coletar-oferta.py` so confere PRESENCA dos campos que o bloco exige.
BUSCAM = {
    os.path.join("ferramentas", "coletar-piso-de-compra.py"): "compoe a escada de chave de "
                                                              "busca da 25.1, que e para a "
                                                              "loja casar e nao para a "
                                                              "pessoa ler",
    os.path.join("ferramentas", "coletar-oferta.py"): "confere a PRESENCA dos campos que o "
                                                      "bloco exige, e chama "
                                                      "`nome_do_registro` para nomear",
}

LIBERADOS = dict(DONOS)
LIBERADOS.update(BUSCAM)

achados = []
for pasta in ("ferramentas", "regras"):
    base = os.path.join(ILHA, pasta)
    for nome_arq in sorted(os.listdir(base)):
        if not nome_arq.endswith((".py", ".php", ".mjs")):
            continue
        rel = os.path.join(pasta, nome_arq)
        caminho = os.path.join(base, nome_arq)
        try:
            texto = open(caminho, encoding="utf-8").read()
        except (OSError, UnicodeDecodeError):
            continue
        # Fora de comentario: linha de comentario Python/PHP citando o defeito
        # antigo e MEMORIA, nao codigo, e este portao nao censura memoria.
        sem_comentario = "\n".join(
            l for l in texto.split("\n")
            if not l.lstrip().startswith(("#", "//", "*"))
        )
        for m in PADRAO.finditer(sem_comentario):
            if rel in LIBERADOS:
                continue
            achados.append((rel, m.group(0)[:120].replace("\n", " ")))

for rel, trecho in achados:
    falha("%s deriva nome de `marca`+`modelo` por conta propria: `%s`. O nome exibido de um "
          "registro e decidido em `regras/nomes.py`, e SO lá. Esta linha e a sexta copia do "
          "item 1 do despacho de 09/11/2026, em que a mesma pergunta tinha cinco respostas e "
          "a F2 servia `scooter-chopper-1000w-48v` na tela" % (rel, trecho))

# A AFIRMACAO POSITIVA: TODA liberacao tem de existir e tem de casar o padrao.
# Liberacao de arquivo que nao casa nada e liberacao que envelheceu — e a proxima
# pessoa a le como se ainda houvesse algo ali, e pior: ela e um buraco pre-aberto,
# porque quem escrever a derivacao NAQUELE arquivo passa calado. A lista inteira
# entra nesta conta, e nao so os donos: foi a metade `CONFEREM`/`BUSCAM` que
# cresceu hoje, e e ela que vai envelhecer.
for rel, por_que in sorted(LIBERADOS.items()):
    caminho = os.path.join(ILHA, rel)
    if not os.path.exists(caminho):
        falha("%s esta LIBERADO de tocar `marca`+`modelo` e NAO EXISTE (%s)"
              % (rel, por_que))
        continue
    if not PADRAO.search(open(caminho, encoding="utf-8").read()):
        falha("%s esta LIBERADO de tocar `marca`+`modelo` e nao os toca em lugar nenhum "
              "(%s). Liberacao sem uso e liberacao vencida, e ela nao e so enfeite: e um "
              "buraco pre-aberto, porque quem escrever a derivacao nesse arquivo passa "
              "calado por este portao" % (rel, por_que))

# E OS TRES GERADORES TEM DE CHAMAR A FUNCAO. Portao que so proibe o padrao
# antigo aprovaria um gerador que parou de nomear o registro.
for ferramenta in ("gerar-f1.py", "gerar-f2.py", "gerar-f3.py"):
    caminho = os.path.join(ILHA, "ferramentas", ferramenta)
    texto = open(caminho, encoding="utf-8").read()
    if "nome_do_registro" not in texto and "nomes.nome" not in texto:
        falha("ferramentas/%s nao chama `nome_do_registro`. Os tres geradores nomeiam "
              "registro na tela, e os tres tem de nomear pela MESMA funcao" % ferramenta)

print()
print("%d mundo(s) de funcao, %d registro(s) sem nome no banco, %d arquivo(s) liberado(s)."
      % (len(MUNDOS), len(SEM_NOME_NO_BANCO), len(LIBERADOS)))
print("%d falha(s)." % len(FALHAS))
print("REPROVADO" if FALHAS else "APROVADO")
sys.exit(1 if FALHAS else 0)
