# -*- coding: utf-8 -*-
"""PORTAO DA REMISSAO DE CAMADA — a frase que a camada que a serve nao pode cumprir.

NASCEU DE DOIS DEFEITOS MEDIDOS NO AR AS 13h4xZ DE 09/11/2026, e os dois na
camada do `application/ld+json`, que e a que a visao geral de IA ingere.

(1) `https://rodametria.com.br/peso-maximo-patinete-eletrico/` — a resposta da
    pergunta *"Quais modelos voces indicam para o meu peso?"* do `FAQPage`
    terminava com **"Os nomes estao logo abaixo, com a carga de cada um."** No
    JSON-LD **nao existe "abaixo"**: o bloco nao tem vizinho, nao tem ordem e
    nao carrega os tres nomes. A frase e VERDADEIRA na pagina — a lista vem duas
    telas depois, com MAXSHOT V1, MAXSHOT V1SPRO e PLAYBIK, 120 kg cada — e
    FALSA na camada que a cita. A classe tem nome: REMISSAO LOCATIVA.

(2) `https://rodametria.com.br/` — a resposta de *"A potencia de pico do anuncio
    serve para classificar?"* servia **"Nao. A regra le a potencia NOMINAL, que
    fica na ficha. O numero grande do anuncio nao e o que a regra le: ela le a
    potencia NOMINAL, que fica na ficha."** A MESMA oracao, palavra por palavra,
    duas vezes em duas frases seguidas — a abertura escrita a mao repetindo a
    abertura do molde que ela mesma chama. E a 20.7 em miniatura (*"duas
    declaracoes do mesmo fato comecam iguais e so uma sobe"*), com o agravante
    de que aqui as duas subiram na MESMA resposta.

POR QUE NENHUM PORTAO VIA NENHUM DOS DOIS, e e a 32.4-c literal: as reguas de
texto desta ilha medem AFIRMACAO (habilitacao, peso, quantificador por extenso)
e nenhuma media a FORMA da frase na camada em que ela e servida. A 32.4-c
consertou a SUPERFICIE — *"toda regua de TEXTO de uma pagina vale para o HTML
SERVIDO e nao para o texto visivel"* — e as duas classes deste arquivo nao sao
de superficie: elas sao sobre o que a camada PODE cumprir. JSON-LD nao tem
vizinho; entao prosa que aponta para vizinho e sempre falsa ali, por mais certa
que esteja na tela.

ESTE ARQUIVO E O DONO DA REGUA. Ele a aplica ao REPOSITORIO (os bancos e os
moldes, sem rede) e fabrica os mundos que o dado de hoje nao tem;
`ferramentas/conferir-no-ar.py` a IMPORTA e a aplica ao JSON-LD de toda URL do
`wp-sitemap.xml`. Duas copias da mesma regua sao a segunda declaracao do mesmo
fato que a 20.7 proibe aqui.
"""
from __future__ import unicode_literals

import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)
LIBERACOES = os.path.join(ILHA, "dados", "liberacoes-de-remissao.json")

# ---------------------------------------------------------------------------
# (A) A REMISSAO LOCATIVA
#
# A lista e das formas que DEFEREM conteudo para um lugar da pagina, e nao de
# todo adverbio de lugar — a diferenca foi MEDIDA e custaria um falso positivo
# caro: a home serve *"4.000 W com 50 km/h e o teto do ciclomotor, que e a
# categoria logo acima"*, onde `logo acima` e a categoria seguinte na escada da
# resolucao e NAO um lugar da tela. Portao que reprova pagina certa e o caminho
# mais curto para alguem passar a ignora-lo (20.5), e por isso essa ocorrencia
# entra por LIBERACAO ESCRITA, com ancora literal, e nao por lista mais curta.
TERMOS = (
    "logo abaixo",
    "logo acima",
    "mais abaixo",
    "mais acima",
    "aqui embaixo",
    "aqui em cima",
    "veja abaixo",
    "veja acima",
    "veja a seguir",
    "a seguir nesta",
    "na tabela abaixo",
    "na tabela acima",
    "na lista abaixo",
    "na lista acima",
    "no quadro abaixo",
    "no quadro acima",
    "dito abaixo",
    "dita abaixo",
    "ditos abaixo",
    "ditas abaixo",
    "no fim da página",
    "no fim desta página",
    "no topo da página",
    "no topo desta página",
    "no primeiro bloco",
    "no bloco acima",
    "no bloco abaixo",
    "logo em seguida",
)


def _normal(t):
    return re.sub(r"\s+", " ", (t or "")).strip()


def carregar_liberacoes(caminho=None):
    """As liberacoes escritas, ou lista vazia se o arquivo nao existir.

    Arquivo ausente NAO e liberacao implicita: e zero liberacao, e toda
    ocorrencia passa a ser denunciada. Liberacao que nao esta escrita nao existe.
    """
    caminho = caminho or LIBERACOES
    if not os.path.exists(caminho):
        return []
    with io.open(caminho, encoding="utf-8") as f:
        return list(json.load(f).get("remissoes_declaradas_permitidas") or [])


def problemas_de_remissao(onde, textos, liberacoes=None):
    """As remissoes locativas de uma camada sem vizinho, uma por ocorrencia.

    `textos` e a lista de strings da camada (as do JSON-LD, no ar; as dos bancos,
    no chao). Devolve uma lista de frases de reprovacao — vazia quer dizer limpo.

    A LIBERACAO E POR OCORRENCIA E A ANCORA E LITERAL, como a de quantificador
    desta ilha: a ancora tem de aparecer no proprio texto e tem de conter o
    termo. Ancora que nao casa com nada NAO libera — liberacao morta e tao
    perigosa quanto frase sem liberacao, porque ela parece conferida.
    """
    liberacoes = carregar_liberacoes() if liberacoes is None else liberacoes
    maus = []
    for texto in textos:
        t = _normal(texto)
        baixo = t.lower()
        for termo in TERMOS:
            if termo not in baixo:
                continue
            liberada = False
            for lib in liberacoes:
                ancora = _normal(lib.get("ancora_no_ar"))
                if (lib.get("termo") == termo and ancora
                        and termo in ancora.lower() and ancora in t):
                    liberada = True
                    break
            if liberada:
                continue
            maus.append(
                "%s: a remissao locativa %r aponta para um lugar que esta camada "
                "nao tem (JSON-LD nao tem vizinho nem ordem) — %r"
                % (onde, termo, t[:200]))
    return maus


# ---------------------------------------------------------------------------
# (B) A ORACAO REPETIDA DENTRO DA MESMA RESPOSTA
#
# A REGUA NAO E DE ORACAO IGUAL: e de MAIOR PEDACO REPETIDO, e a diferenca foi
# medida. O que foi ao ar nao era a mesma oracao duas vezes — era *"A regra le a
# potencia NOMINAL, que fica na ficha"* seguido de *"ela le a potencia NOMINAL,
# que fica na ficha"*. Partindo por virgula e ponto, os pedacos NAO coincidem; o
# que coincide e o trecho de 41 caracteres `le a potencia NOMINAL, que fica na
# ficha.`, que atravessa a virgula. Regua de oracao igual fica VERDE sobre o
# defeito de hoje — a primeira versao desta ficou, e e por isso que esta linha
# esta escrita.
#
# O PISO DE 30 FOI MEDIDO E NAO ESCOLHIDO, nas 22 respostas de `FAQPage` que as
# dez URLs desta ilha serviam as 13h3xZ de 09/11/2026 (27 blocos de JSON-LD: 1
# WebSite, 10 WebPage, 9 BreadcrumbList, 5 FAQPage e 2 ItemList): o defeito tem **41**
# caracteres e a maior repeticao LEGITIMA de todas as outras tem **21** (`da
# bicicleta eletrica`, na resposta dos dois limites). 30 cai no meio de um vao de
# vinte caracteres, com zero falso positivo em dez URLs. Piso mais baixo
# reprovaria pagina certa; piso de 45 nao teria pegado o defeito de hoje.
PISO_DA_REPETICAO = 30


def _maior_pedaco_repetido(texto):
    """O maior trecho que aparece DUAS vezes no mesmo texto, alinhado a palavra.

    O alinhamento a comeco de palavra existe para a conta nao ser inflada por
    terminacao comum (`-mente`, `-cao`), que repete em qualquer prosa e nao e
    declaracao repetida de nada.
    """
    t = _normal(texto)
    if not t:
        return ""
    inicios = [0] + [m.start() + 1 for m in re.finditer(r"\s", t)]
    melhor = ""
    for a in range(len(inicios)):
        for b in range(a + 1, len(inicios)):
            i, j = inicios[a], inicios[b]
            k = 0
            while j + k < len(t) and t[i + k] == t[j + k]:
                k += 1
            pedaco = t[i:i + k]
            # corta a palavra pela metade no fim, quando houve corte no meio dela
            if i + k < len(t) and t[i + k].strip():
                pedaco = re.sub(r"\S*$", "", pedaco)
            pedaco = pedaco.strip()
            if len(pedaco) > len(melhor):
                melhor = pedaco
    return melhor


def problemas_de_oracao_repetida(onde, pares):
    """Resposta de `FAQPage` que declara o mesmo fato duas vezes.

    `pares` e a lista de (pergunta, resposta). A conta e DENTRO de cada resposta:
    o mesmo trecho em duas respostas diferentes e repeticao entre perguntas, que
    e normal e as vezes necessaria — as paginas de familia desta ilha servem, de
    proposito, a mesma oracao de recusa de habilitacao em duas perguntas. O mesmo
    trecho DUAS VEZES na MESMA resposta e a abertura escrita a mao repetindo o
    molde que ela chama, que e o defeito medido no ar na home em 09/11/2026.
    """
    maus = []
    for pergunta, resposta in pares:
        pedaco = _maior_pedaco_repetido(resposta)
        if len(pedaco) >= PISO_DA_REPETICAO:
            maus.append(
                "%s: a resposta de %r repete %d caracteres dentro de si mesma — "
                "%r. Duas declaracoes do mesmo fato na MESMA resposta (20.7), e "
                "e a camada que a visao geral de IA ingere"
                % (onde, _normal(pergunta)[:80], len(pedaco), pedaco[:140]))
    return maus


# ---------------------------------------------------------------------------
# O PORTAO, quando este arquivo roda sozinho: o repositorio e os mundos
# fabricados.
# ---------------------------------------------------------------------------
AFIRMACOES = [0]
FALHAS = []


def ok(cond, msg):
    AFIRMACOES[0] += 1
    if not cond:
        FALHAS.append(msg)


def _banco(nome):
    with io.open(os.path.join(ILHA, "dados", nome), encoding="utf-8") as f:
        return json.load(f)


def metade_a_mundos_fabricados():
    """A REGUA SE PROVA MORDENDO, com o texto que foi ao ar (20.8)."""
    # O DEFEITO DE 09/11, LETRA POR LETRA, como o JSON-LD o servia.
    foi_ao_ar = (
        "3 dos 3 veículos que declaram carga máxima no nosso banco aguentariam "
        "os seus 108 kg com folga — e nenhum deles tem oferta aberta hoje. Não "
        "montamos vitrine com item sem link de loja, porque o botão que não leva "
        "a lugar nenhum é pior que a ausência dele. Os nomes estão logo abaixo, "
        "com a carga de cada um.")
    maus = problemas_de_remissao("mundo fabricado", [foi_ao_ar], liberacoes=[])
    ok(len(maus) == 1,
       "a regua NAO reprova a frase que foi ao ar em 09/11/2026 com `logo "
       "abaixo` no JSON-LD: %r" % (maus,))

    # E A MESMA FRASE, COM OS NOMES NO LUGAR DA SETA, TEM DE PASSAR.
    curada = foi_ao_ar.replace(
        "Os nomes estão logo abaixo, com a carga de cada um.",
        "São eles, com a carga que cada um declara: MAXSHOT V1 (120 kg), "
        "MAXSHOT V1SPRO (120 kg) e PLAYBIK (120 kg).")
    ok(not problemas_de_remissao("mundo fabricado", [curada], liberacoes=[]),
       "a regua reprova a frase JA CURADA, que carrega os nomes em vez de apontar")

    # A LIBERACAO POR ANCORA LIBERA ESTA OCORRENCIA E NENHUMA OUTRA.
    certa = ("4.000 W com 50 km/h é o teto do ciclomotor, que é a categoria "
             "logo acima.")
    lib = [{"termo": "logo acima", "ancora_no_ar": "a categoria logo acima"}]
    ok(not problemas_de_remissao("mundo fabricado", [certa], liberacoes=lib),
       "a liberacao com ancora literal nao libera a ocorrencia que ela nomeia")
    ok(problemas_de_remissao(
           "mundo fabricado",
           ["O preço de cada um está logo acima, no cartão."], liberacoes=lib),
       "a liberacao de `logo acima` vazou para OUTRA frase da mesma camada — "
       "liberacao e por ocorrencia, nunca por termo")
    ok(problemas_de_remissao("mundo fabricado", [certa],
                             liberacoes=[{"termo": "logo acima",
                                          "ancora_no_ar": "ancora que nao existe"}]),
       "ancora que NAO aparece no texto liberou a frase: liberacao morta parece "
       "conferida e nao mede nada")

    # (B) A ORACAO REPETIDA, com o par que foi ao ar na home.
    par = [("A potência de pico do anúncio serve para classificar?",
            "Não. A regra lê a potência NOMINAL, que fica na ficha. O número "
            "grande do anúncio não é o que a regra lê: ela lê a potência "
            "NOMINAL, que fica na ficha. Dos 14 anúncios que a gente colheu, 13 "
            "declaram um watt sem dizer se é nominal ou de pico, e NENHUM "
            "declara o nominal.")]
    ok(problemas_de_oracao_repetida("mundo fabricado", par),
       "a regua NAO reprova a resposta que foi ao ar na home de 09/11/2026 com "
       "a mesma oracao duas vezes")
    curado = [("A potência de pico do anúncio serve para classificar?",
               "Não. O número grande do anúncio não é o que a regra lê: ela lê "
               "a potência NOMINAL, que fica na ficha. Dos 14 anúncios que a "
               "gente colheu, 13 declaram um watt sem dizer se é nominal ou de "
               "pico, e NENHUM declara o nominal.")]
    ok(not problemas_de_oracao_repetida("mundo fabricado", curado),
       "a regua reprova a resposta JA CURADA, com a oracao uma vez so")

    # E A REGUA NAO PODE CONFUNDIR REPETICAO ENTRE RESPOSTAS COM REPETICAO
    # DENTRO DE UMA: as paginas de familia desta ilha servem, de proposito, a
    # MESMA oracao de recusa de habilitacao em duas perguntas diferentes.
    duas = [("Patinete elétrico precisa de CNH?",
             "Sobre habilitação esta página não responde, e o motivo é de fonte: "
             "a Resolução Contran nº 996/2023 decide a categoria do veículo."),
            ("Bicicleta elétrica precisa de CNH?",
             "Sobre habilitação esta página não responde, e o motivo é de fonte: "
             "a Resolução Contran nº 996/2023 decide a categoria do veículo.")]
    ok(not problemas_de_oracao_repetida("mundo fabricado", duas),
       "a regua reprovou a MESMA oracao em DUAS respostas diferentes, que e "
       "repeticao legitima entre perguntas")

    # E A PROVA QUE A 20.8 EXIGE: a regua VELHA e a NOVA tem de DISCORDAR num
    # mundo. A velha existiu de verdade — foi a primeira versao deste arquivo,
    # escrita meia hora antes — e ela partia o texto por ponto e virgula e
    # comparava ORACOES IGUAIS. Ela fica VERDE sobre o defeito de hoje, porque o
    # que se repete atravessa uma virgula e as duas metades comecam diferente
    # ("A regra le" / "ela le"). Autoteste em que as duas concordam nao mede
    # conserto nenhum.
    def _regua_velha(resposta):
        vistas = {}
        for o in re.split(r"[.;:,—\u2014]", _normal(resposta)):
            o = o.strip().lower()
            if len(o) >= 40:
                vistas[o] = vistas.get(o, 0) + 1
        return [o for o, n in vistas.items() if n > 1]

    ok(not _regua_velha(par[0][1]),
       "a regua VELHA (oracao igual) tambem reprova o defeito de hoje — entao "
       "ela nao era a causa e este portao nao prova conserto nenhum")
    ok(problemas_de_oracao_repetida("mundo fabricado", par),
       "a regua NOVA nao reprova onde a velha ficou verde: as duas concordam, e "
       "o autoteste nao esta medindo o conserto (20.8)")
    print("  mundos fabricados: os dois defeitos de 09/11 reprovados letra por "
          "letra, os dois curados aprovados, e a liberacao provada por ancora")


def metade_b_o_repositorio():
    """A camada autocontida do banco, no chao, ANTES do ar.

    A frase que o `FAQPage` da F3 serve nasce em `frases_vazio_autocontidas`, e
    e aqui que ela e barrada — no ponto em que o dado vira texto, nunca no ponto
    em que o texto e impresso.
    """
    f3 = _banco("f3-respostas.json")
    r = f3.get("resposta_exemplo") or {}
    auto = list(r.get("frases_vazio_autocontidas") or [])
    tela = list(r.get("frases_vazio") or [])

    ok(auto, "o banco da F3 nao traz `frases_vazio_autocontidas`: a resposta do "
             "`FAQPage` ficaria sem frase, ou voltaria a ler a da tela")
    ok(len(auto) == len(tela),
       "as duas camadas da F3 tem tamanhos diferentes (%d na tela, %d "
       "autocontida): item por item elas tem de falar da MESMA causa"
       % (len(tela), len(auto)))
    maus = problemas_de_remissao("f3-respostas/frases_vazio_autocontidas", auto)
    ok(not maus, "a camada autocontida da F3 traz remissao locativa: %s"
       % (maus[:1],))

    # E A DA TELA TEM DE CONTINUAR APONTANDO: a seta e correta la, e some-la
    # seria consertar a camada certa.
    ok(any("logo abaixo" in t for t in tela),
       "a frase da TELA da F3 perdeu a remissao aos nomes — ela e VERDADEIRA ali "
       "(a lista vem logo abaixo) e e isso que distingue as duas camadas")

    # OS NOMES TEM DE ESTAR NA FRASE, e sao os que a pagina serve.
    nomes = [x.get("nome") for x in (f3.get("compra") or {}).get(
        "serviriam_sem_oferta") or []]
    if nomes and auto:
        faltam = [n for n in nomes if n and n not in auto[0]]
        ok(not faltam,
           "a frase autocontida da F3 nao carrega %d nome(s) que a pagina serve "
           "(%s): a seta foi tirada e o conteudo nao entrou" % (len(faltam), faltam))

    # OS MOLDES DOS DOIS BANCOS DE FERRAMENTA, no chao: molde com remissao
    # locativa chega a camada da IA no dia em que alguem o usar la.
    for nome in ("f1-respostas.json", "f2-respostas.json", "f3-respostas.json"):
        b = _banco(nome)
        moldes = b.get("frases_molde") or {}
        for k, v in sorted(moldes.items()):
            if k in ("vazio_remissao_aos_nomes",):
                continue  # o molde da TELA, e so ela o serve
            maus = problemas_de_remissao("%s/frases_molde/%s" % (nome, k), [v])
            ok(not maus, maus[0] if maus else "")
    print("  repositorio: a camada autocontida da F3 limpa, a da tela com a seta "
          "preservada, e os moldes dos tres bancos varridos")


def main():
    print("PORTAO DA REMISSAO DE CAMADA — RODAMETRIA")
    metade_a_mundos_fabricados()
    metade_b_o_repositorio()
    print()
    print("teste-remissao-de-camada: %d afirmacoes, %d falha(s)"
          % (AFIRMACOES[0], len(FALHAS)))
    for f in FALHAS[:40]:
        print("  FALHA", f)
    print("REPROVADO" if FALHAS else "APROVADO")
    return 1 if FALHAS else 0


if __name__ == "__main__":
    sys.exit(main())
