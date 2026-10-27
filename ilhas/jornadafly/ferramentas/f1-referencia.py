#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""F1 -- QUANTO CUSTA A EXPERIENCIA PARA O SEU GRUPO. Implementacao de REFERENCIA.

Bloco 4 da jornadafly. Este arquivo e o CEREBRO da F1: dado um estado de entrada
(experiencia, versao, numero de pessoas) ele devolve a resposta inteira -- frase
de resposta, a linha do cartao brasileiro, o que esta incluso, o bloco de compra,
a prestacao de contas das versoes, as recusas e o "como sabemos" -- ja em frase
acentuada, do jeito que o visitante le.

    python3 ferramentas/f1-referencia.py                       # uma resposta de exemplo
    python3 ferramentas/f1-referencia.py --contar              # o tamanho do dominio
    python3 ferramentas/f1-referencia.py <experiencia> <versao> <pessoas>

POR QUE A REFERENCIA E PYTHON E NAO PHP, e isto e decisao registrada do bloco 4:
esta ilha NAO TEM SITE. Os passos 2 a 8 da secao 11 (dominio adicional no cPanel,
WordPress, SSL) sao trabalho de navegador e estao com o Raphael, e o dominio desta
ilha nao esta na lista de Dominios permitidos deste ambiente -- remedido em
22/10/2026, `CONNECT tunnel failed, response 403` em seis medicoes. Sem casca, um
snippet PHP so poderia ser medido por um render de bancada que serve MENOS do que
o site serve, que e a cicatriz que a secao 8 do ARQUIPELAGO.md mais cobra. Entao a
regra nasce onde pode ser conferida hoje, e o PHP, quando nascer, e TRADUTOR desta
referencia frase a frase -- o mesmo desenho que a ohmetria usou na F1 dela e que a
robometria usa entre cobertura-r1.py e robometria-r1.php.

O QUE ESTE ARQUIVO NAO FAZ, de proposito:

  - NAO PUBLICA VALOR EM REAL. `cambio-eur-brl` e `cambio-usd-brl` estao com status
    `pendente` em dados/constantes.json, e constante pendente e proibida dentro de
    formula publicada (secao 10). A F1 diz isso ao leitor em vez de esconder, e a
    recusa e CONTADA como as outras.
  - NAO INVENTA MEDIA. Onde as declaracoes divergem, quem manda e a resolucao
    gravada no banco, e as divergentes vao para a tela com o nome de quem as
    publicou e a data em que foram lidas.
  - NAO DIGITA NUMERO SOBRE O PROPRIO BANCO. Toda contagem sai do banco carregado
    (secao 8: numero de tela nasce contado, nunca digitado).
  - NAO LE PROSA COMO SE FOSSE CAMPO. A Conta 3 (o ponto de equilibrio entre as
    versoes) exige `eixo_das_versoes` na EXPERIENCIA e `dias_de_uso` na VERSAO,
    nascidos no esquema versao 5 em 22/10/2026 exatamente porque a quantidade de
    uso de cada bilhete so existia no texto do `rotulo`.
  - NAO TEM COPIA DE NENHUMA LISTA DO ESQUEMA. Vocabulario, molde do piso de compra
    e o `rel` do link sao lidos do esquema; se a chave sumir, a referencia MORRE em
    vez de cair num literal (secao 26.2).

AS QUATRO CONTAS, e a quarta e o diferencial (especificacao 2.5):

  1. NORMALIZAR A UNIDADE. `por_pessoa` multiplica pelo numero de pessoas;
     `por_veiculo`, `por_cabine` e `por_grupo` multiplicam pelo TETO de
     pessoas / capacidade. E o degrau que nenhuma pagina medida mostra: 6 pessoas
     na gondola sao DUAS gondolas, 180 EUR, e nao "90 EUR divididos por 6".
  2. POR PESSOA, sempre ao lado do total, porque e assim que o grupo divide.
  3. O PONTO DE EQUILIBRIO entre as versoes, quando -- e SO quando -- a
     experiencia declara que suas versoes se comparam em quantidade.
  4. O IOF DE 3,5% do cartao brasileiro. Nenhuma das paginas medidas em 14/09/2026
     o menciona, e ele nao depende de cambio: e percentual, entao incide na moeda
     do operador.
"""

import datetime
import io
import json
import math
import os
import sys
from decimal import Decimal, ROUND_HALF_UP

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(AQUI)
DADOS = os.path.join(BASE, "dados")

ESQUEMA = os.path.join(DADOS, "esquema-banco.json")
BANCO = os.path.join(DADOS, "experiencias.json")
CONSTANTES = os.path.join(DADOS, "constantes.json")

# A faixa de grupo que a F1 aceita. O teto e DECISAO da especificacao (2.6): acima
# de 12 a compra vira negociacao com o operador, e multiplicar seria responder uma
# pergunta que o operador nao responde assim.
PESSOAS_MINIMO = 1
PESSOAS_MAXIMO = 12

# As pessoas da TABELA PRE-RENDERIZADA (especificacao 2.8). O 6 e obrigatorio: e
# onde o degrau de capacidade aparece, e tabela que para em 4 esconde exatamente o
# que esta ferramenta tem de diferente das paginas medidas.
PESSOAS_DA_TABELA = (1, 2, 4, 6)

# Como cada moeda do vocabulario se ESCREVE na tela. E decisao de apresentacao
# desta ferramenta, por isso mora aqui -- mas e COBRADA contra o vocabulario do
# esquema por `conferir_moedas_do_vocabulario()`, nas duas direcoes: moeda no
# vocabulario sem forma de escrita publicaria o codigo cru no lugar do preco, e
# forma de escrita sem moeda no vocabulario e tela para um mundo que o esquema nao
# permite mais.
SIMBOLO_DA_MOEDA = {
    "EUR": "€",
    "USD": "US$ ",
    "BRL_do_operador": "R$ ",
}

# As unidades que produzem DEGRAU (o teto de pessoas / capacidade). A lista e
# derivada do vocabulario do esquema menos `por_pessoa`, e e conferida contra ele
# em `conferir_unidades_do_vocabulario()`: unidade nova no vocabulario sem conta
# definida aqui faria a F1 escolher uma conta por conta propria.
UNIDADE_POR_PESSOA = "por_pessoa"
UNIDADES_COM_CAPACIDADE = ("por_veiculo", "por_cabine", "por_grupo")

# Como cada unidade se ESCREVE na tela, acentuada. Nasceu porque a primeira versao
# desta ferramenta montava o rotulo com `unidade.replace("_", " ")` e publicava "por
# veiculo" sem acento -- a cicatriz da Robometria, cometida dentro do arquivo que
# existe para nao a cometer. A lista e conferida contra o vocabulario do esquema,
# nas duas direcoes, por `conferir_unidades_do_vocabulario()`.
ROTULO_DA_UNIDADE = {
    "por_pessoa": "por pessoa",
    "por_veiculo": "por ve\u00edculo",
    "por_cabine": "por cabine",
    "por_grupo": "por grupo",
}


class BancoIncompleto(Exception):
    """A fonte perdeu uma chave de que a referencia depende, ou ganhou um valor
    para o qual ela nao tem conta.

    Levantada em vez de cair num literal: regua que le a propria lista de um
    arquivo de dados aprova tudo, em silencio, no dia em que o arquivo perder a
    chave (secao 26.2). Morrer e a unica reacao honesta.
    """


# ---------------------------------------------------------------------------
# CARGA
# ---------------------------------------------------------------------------

def _ler(caminho):
    with io.open(caminho, encoding="utf-8") as f:
        return json.load(f)


def carregar_esquema():
    return _ler(ESQUEMA)


def carregar_banco():
    return _ler(BANCO)


def carregar_constantes():
    return _ler(CONSTANTES)


def vocabulario(esquema, nome):
    valores = (esquema.get("vocabularios") or {}).get(nome)
    if not isinstance(valores, list) or not valores:
        raise BancoIncompleto(
            "esquema: vocabularios.%s ausente ou vazio. A F1 le o vocabulario do "
            "esquema e nunca de dentro de si; sem ele ela nao sabe o que o banco "
            "pode dizer." % nome)
    return valores


def molde_do_piso(esquema):
    molde = (esquema.get("piso_de_compra") or {}).get("molde")
    if not isinstance(molde, str) or "{slug_plataforma}" not in molde:
        raise BancoIncompleto(
            "esquema: piso_de_compra.molde ausente ou sem {slug_plataforma}. O piso "
            "da 25.2 e DERIVADO da cidade; sem molde ele viraria URL digitada dentro "
            "desta ferramenta, que e o defeito que o molde existe para impedir.")
    return molde


def rel_do_piso(esquema):
    rel = (esquema.get("piso_de_compra") or {}).get("rel_enquanto_nao_ha_programa")
    if not isinstance(rel, str) or not rel:
        raise BancoIncompleto(
            "esquema: piso_de_compra.rel_enquanto_nao_ha_programa ausente. Link cru "
            "sai sem `sponsored` por decisao registrada -- `sponsored` declara relacao "
            "PAGA e ninguem esta pagando por aquele clique -- e e o esquema que guarda "
            "a decisao.")
    return rel


def iof_publicavel(constantes):
    """O IOF de 3,5%: a unica constante desta ilha que entra em formula publicada.

    Constante com status diferente de `publicavel` NAO entra (secao 10), e e por
    isso que esta funcao reprova em vez de usar o numero que achou.
    """
    for c in (constantes.get("constantes") or []):
        if c.get("id") == "iof-compra-internacional-cartao-pessoa-fisica":
            if c.get("status") != "publicavel":
                raise BancoIncompleto(
                    "constantes: o IOF esta com status %r. Constante que nao e "
                    "`publicavel` nao entra em formula publicada (secao 10), e a linha "
                    "do cartao brasileiro depende dele." % c.get("status"))
            valor = c.get("valor")
            if not isinstance(valor, (int, float)) or valor <= 0:
                raise BancoIncompleto("constantes: IOF %r nao e numero positivo." % (valor,))
            return c
    raise BancoIncompleto(
        "constantes: nao achei `iof-compra-internacional-cartao-pessoa-fisica`. A linha "
        "do cartao brasileiro e o diferencial mais barato desta ilha, e ela nao se "
        "escreve de cabeca.")


def constantes_pendentes(constantes):
    """As constantes que a F1 NAO pode usar hoje, lidas do arquivo e nao digitadas.

    E daqui que sai a recusa do valor em real: a frase nomeia as constantes que
    faltam, entao no dia em que uma delas ganhar valor e data a frase muda sozinha.
    """
    return [c for c in (constantes.get("constantes") or []) if c.get("status") == "pendente"]


def conferir_moedas_do_vocabulario(esquema):
    faltas = []
    vocab = vocabulario(esquema, "moeda")
    for moeda in vocab:
        if moeda not in SIMBOLO_DA_MOEDA:
            faltas.append("moeda %r do vocabulario do esquema sem forma de escrita "
                          "nesta ferramenta" % moeda)
    for moeda in SIMBOLO_DA_MOEDA:
        if moeda not in vocab:
            faltas.append("forma de escrita para %r, que nao esta mais no vocabulario "
                          "do esquema" % moeda)
    return faltas


def conferir_unidades_do_vocabulario(esquema):
    faltas = []
    vocab = vocabulario(esquema, "unidade_de_preco")
    conhecidas = (UNIDADE_POR_PESSOA,) + UNIDADES_COM_CAPACIDADE
    for unidade in vocab:
        if unidade not in conhecidas:
            faltas.append("unidade_de_preco %r do vocabulario do esquema sem conta "
                          "definida nesta ferramenta" % unidade)
        if unidade not in ROTULO_DA_UNIDADE:
            faltas.append("unidade_de_preco %r sem rotulo de tela acentuado" % unidade)
    for unidade in conhecidas:
        if unidade not in vocab:
            faltas.append("conta definida para a unidade %r, que nao esta mais no "
                          "vocabulario do esquema" % unidade)
    for unidade in ROTULO_DA_UNIDADE:
        if unidade not in vocab:
            faltas.append("rotulo de tela para %r, que nao esta mais no vocabulario "
                          "do esquema" % unidade)
    return faltas


# ---------------------------------------------------------------------------
# NUMERO E PALAVRA
# ---------------------------------------------------------------------------

def _centavo(valor):
    """Arredonda para centavo com ROUND_HALF_UP.

    O padrao do Python e banqueiro (ROUND_HALF_EVEN) e levaria 23,285 para 23,28; a
    especificacao (2.5) publica 23,29 nesse caso, e preco de tela que discorda do
    exemplo escrito e o tipo de divergencia que ninguem procura.
    """
    return Decimal(str(valor)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def dinheiro(valor, moeda):
    """O numero como o visitante brasileiro le: virgula decimal, ponto de milhar.

    Valor inteiro sai sem centavo (90 EUR e nao 90,00 EUR), porque a tarifa foi
    publicada assim; valor com centavo sai com os dois.
    """
    simbolo = SIMBOLO_DA_MOEDA.get(moeda)
    if simbolo is None:
        raise BancoIncompleto(
            "moeda %r sem forma de escrita. A F1 nao publica codigo de moeda no lugar "
            "do preco." % (moeda,))
    d = _centavo(valor)
    if d == d.to_integral_value():
        corpo = "{:,.0f}".format(d).replace(",", ".")
    else:
        corpo = "{:,.2f}".format(d)
        corpo = corpo.replace(",", "\x00").replace(".", ",").replace("\x00", ".")
    return simbolo + corpo


def dinheiro_ou_faixa(valor, moeda):
    """Escreve `valor` de uma DECLARACAO, que pelo esquema pode ser numero OU faixa.

    O campo `valor` da DECLARACAO e, no esquema, `numero|objeto|null`, com a
    observacao «objeto {minimo, maximo} quando a fonte publica faixa» — e isso esta
    escrito lá desde 14/09/2026. A F1 chamava `dinheiro()` direto nele e QUEBRAVA com
    `decimal.InvalidOperation` numa faixa: nenhuma das quatro experiencias anteriores
    tinha declaracao em faixa, entao o caminho nunca foi pisado. Achado em 27/10/2026,
    na carga do Bondinho, pela primeira declaracao de faixa deste banco (a Civitatis
    publica «de cerca de R$ 85 a R$ 295»). E a familia do mundo que o esquema permite
    e o banco ainda nao tem — a mesma que a mutacao da ohmetria nomeou: so a carga que
    PRODUZ o mundo o enxerga.
    """
    if isinstance(valor, dict):
        minimo, maximo = valor.get("minimo"), valor.get("maximo")
        if minimo is None or maximo is None:
            raise BancoIncompleto(
                "declaracao com valor em faixa sem `minimo` ou sem `maximo`: %r. Faixa "
                "sem uma das duas pontas nao e faixa." % (valor,))
        return "de %s a %s" % (dinheiro(minimo, moeda), dinheiro(maximo, moeda))
    if valor is None:
        return None
    return dinheiro(valor, moeda)


def dias_de_validade(esquema, fonte):
    """Quantos dias um preco daquela fonte vale antes de precisar ser relido.

    A regra mora no esquema (`validade_do_preco`) e o que a escolhe e a ORIGEM da
    fonte: tarifa de poder publico envelhece devagar, preco de operador privado
    rapido. Esta funcao nasceu em 22/10/2026, no bloco da F3, porque a F3 e a primeira
    ferramenta que leva o vencimento para a TELA — ate aqui ele era so aviso de
    bancada, escrito dentro de ferramentas/validar-banco.py. Quem quiser as duas
    metades conferidas uma contra a outra: o portao da F3 compara o veredito desta
    funcao com a lista `vencidos` do validador, versao por versao do banco.
    """
    validade = esquema.get("validade_do_preco") or {}
    if not validade:
        raise BancoIncompleto(
            "esquema: `validade_do_preco` ausente. Sem ela a ilha nao sabe quando um "
            "preco lido deixa de poder ser republicado sem releitura, e a data de "
            "leitura na tela viraria enfeite.")
    origem = (fonte or {}).get("origem") or ""
    if "poder-publico" in origem:
        dias = validade.get("tarifa_de_poder_publico_dias")
    else:
        dias = validade.get("operador_privado_dias")
    if not isinstance(dias, int) or isinstance(dias, bool) or dias < 1:
        raise BancoIncompleto(
            "esquema: validade_do_preco para a origem %r deu %r, que nao e inteiro "
            "positivo." % (origem, dias))
    return dias


def preco_vencido(esquema, fonte, data_leitura, hoje):
    """(vencido, dias_desde_a_leitura, dias_de_validade). Funcao pura sobre datas.

    `hoje` e sempre RECEBIDO, nunca lido do relogio aqui dentro: regua que pega a data
    do sistema nao pode ser testada na borda, e a borda — o dia exato em que o preco
    vence — e o unico lugar em que ela pode errar.
    """
    dias = dias_de_validade(esquema, fonte)
    if not isinstance(data_leitura, str):
        raise BancoIncompleto(
            "data de leitura %r nao e texto: nao ha vencimento a calcular."
            % (data_leitura,))
    lido = datetime.date.fromisoformat(data_leitura)
    passados = (hoje - lido).days
    return passados > dias, passados, dias


def _plural(n, singular, plural):
    return singular if n == 1 else plural


def pessoas_em_palavra(n):
    return "%d %s" % (n, _plural(n, "pessoa", "pessoas"))


def dias_em_palavra(n):
    return "%d %s" % (n, _plural(n, "dia", "dias"))


def data_em_portugues(iso):
    """2026-09-14 -> 14/09/2026. Data de leitura e obrigatoria na tela."""
    if not isinstance(iso, str) or len(iso) != 10 or iso[4] != "-" or iso[7] != "-":
        raise BancoIncompleto(
            "data de leitura %r nao esta em AAAA-MM-DD. O preco datado e o produto "
            "desta ilha: data que a tela nao sabe escrever e preco sem data." % (iso,))
    return "%s/%s/%s" % (iso[8:10], iso[5:7], iso[0:4])


# ---------------------------------------------------------------------------
# AS CONTAS, COMO FUNCOES PURAS
#
# Nenhuma delas varre o banco. E a regra da secao 8 do ARQUIPELAGO.md, aprendida no
# Clube do Mosaico em 08/10/2026: recusa que depende de uma RELACAO entre os dados
# -- empate, ausencia, borda, limite -- mora numa funcao pura que recebe a relacao
# JA calculada, senao ela so e testavel no dia em que o banco produzir o caso, e e
# esse o dia em que ela vai estar errada. Por isso a bancada chama estas quatro
# direto, com lista vazia, com empate e com uma versao so.
# ---------------------------------------------------------------------------

def unidades_necessarias(unidade, capacidade_maxima, pessoas):
    """Quantos veiculos/cabines/grupos o grupo precisa. Funcao pura.

    `por_pessoa` devolve 1 porque nao ha veiculo a contar -- e nao 0, que faria a
    conta do total dar zero.
    """
    if unidade == UNIDADE_POR_PESSOA:
        return 1
    if unidade not in UNIDADES_COM_CAPACIDADE:
        raise BancoIncompleto(
            "unidade_de_preco %r sem conta definida. A F1 nao escolhe conta por conta "
            "propria: unidade nova entra no vocabulario do esquema e na conta desta "
            "ferramenta na mesma passada." % (unidade,))
    if not isinstance(capacidade_maxima, int) or capacidade_maxima < 1:
        raise BancoIncompleto(
            "unidade %r com capacidade_maxima %r. Quando a unidade nao e por pessoa, e "
            "a capacidade que produz o degrau: sem ela a conta do grupo nao fecha."
            % (unidade, capacidade_maxima))
    return int(math.ceil(float(pessoas) / capacidade_maxima))


def total_do_grupo(preco, unidade, capacidade_maxima, pessoas):
    """CONTA 1 e CONTA 2. Funcao pura. Devolve (total, por_pessoa, unidades).

    O total e EXATO (Decimal sem arredondar): e ele que a pessoa paga. O por
    pessoa e arredondado ao centavo, porque e divisao -- e a tela publica os dois
    lado a lado para que a diferenca de centavo seja visivel em vez de escondida.
    """
    if not isinstance(pessoas, int) or isinstance(pessoas, bool):
        raise BancoIncompleto("pessoas %r nao e inteiro." % (pessoas,))
    if pessoas < 1:
        raise BancoIncompleto("pessoas %r menor que 1." % (pessoas,))
    if preco is None:
        raise BancoIncompleto(
            "preco null: nao ha conta a fazer, e a F1 tem de dizer isso em vez de "
            "publicar zero.")
    unidades = unidades_necessarias(unidade, capacidade_maxima, pessoas)
    if unidade == UNIDADE_POR_PESSOA:
        total = Decimal(str(preco)) * pessoas
    else:
        total = Decimal(str(preco)) * unidades
    return total, _centavo(total / Decimal(pessoas)), unidades


def com_iof(total, percentual):
    """CONTA 4. Funcao pura. O IOF incide na moeda do operador, sem cambio."""
    return total * (Decimal(1) + Decimal(str(percentual)) / Decimal(100))


def ponto_de_equilibrio(eixo, degraus):
    """CONTA 3. Funcao PURA sobre a relacao ja calculada.

    `degraus` e uma lista de dicionarios {id, rotulo, preco, dias_de_uso}. Esta
    funcao NAO abre o banco: e por isso que a bancada consegue fabricar o empate, a
    lista vazia, a versao unica e o preco null sem fabricar um banco falso.

    Devolve {aplicavel, motivo, base, linhas}. `motivo` e sempre uma frase para a
    tela, nunca um codigo -- a pagina diz POR QUE nao ha conta, em vez de calar.
    """
    vazio = {"aplicavel": False, "motivo": None, "base": None, "linhas": []}

    if eixo != "por_quantidade":
        vazio["motivo"] = (
            "As versões desta experiência não se comparam em quantidade: elas diferem "
            "em %s. Não existe «a partir de quantos dias a mais cara vale», porque "
            "comprar duas vezes a mais barata não dá o que a mais cara dá."
            % {"por_escopo": "escopo — o que cada bilhete dá",
               "por_momento": "horário — a mesma coisa em outra hora do dia",
               None: "uma grandeza que a experiência não declarou"}.get(eixo, "outra grandeza"))
        return vazio

    if len(degraus) < 2:
        vazio["motivo"] = (
            "Esta experiência declara que suas versões se comparam em quantidade e tem "
            "%s só: não há com que comparar."
            % _plural(len(degraus), "uma versão", "versões"))
        return vazio

    sem_dado = [d for d in degraus
                if d.get("preco") is None or not isinstance(d.get("dias_de_uso"), int)]
    if sem_dado:
        vazio["motivo"] = (
            "Falta o dado em %d das %d versões (o preço ou a quantidade de dias), e sem "
            "ele o ponto de equilíbrio seria um número certo sobre uma conta "
            "incompleta." % (len(sem_dado), len(degraus)))
        return vazio

    # A BASE e a versao de MENOR quantidade -- e o bilhete que se repete. Empate de
    # quantidade na base: vence o de menor preco, porque e esse que a pessoa
    # compraria duas vezes. Empate nos dois: vence o primeiro, e a ordem e a do
    # banco; o desempate nao muda numero nenhum porque os dois dao a mesma conta.
    base = sorted(degraus, key=lambda d: (d["dias_de_uso"], Decimal(str(d["preco"]))))[0]
    linhas = []
    for d in degraus:
        if d["id"] == base["id"]:
            continue
        if d["dias_de_uso"] == base["dias_de_uso"]:
            mais_barata = Decimal(str(d["preco"])) <= Decimal(str(base["preco"]))
            linhas.append({
                "de": base["id"],
                "para": d["id"],
                "a_partir_de": None,
                "nunca_vale": not mais_barata,
                "frase": ("«%s» e «%s» dão a mesma quantidade de dias (%s), então não há "
                          "ponto de equilíbrio entre as duas: a escolha é por preço, e "
                          "«%s» custa %s."
                          % (base["rotulo"], d["rotulo"], dias_em_palavra(d["dias_de_uso"]),
                             d["rotulo"], "menos ou o mesmo" if mais_barata else "mais")),
            })
            continue

        preco_base = Decimal(str(base["preco"]))
        preco_alvo = Decimal(str(d["preco"]))
        achou = None
        for dias in range(1, d["dias_de_uso"] + 1):
            copias = int(math.ceil(float(dias) / base["dias_de_uso"]))
            if copias * preco_base >= preco_alvo:
                achou = dias
                break
        if achou is None:
            linhas.append({
                "de": base["id"],
                "para": d["id"],
                "a_partir_de": None,
                "nunca_vale": True,
                "frase": ("«%s» não passa a valer em nenhum número de dias dentro da "
                          "própria validade: até %s, comprar «%s» quantas vezes forem "
                          "necessárias ainda custa menos."
                          % (d["rotulo"], dias_em_palavra(d["dias_de_uso"]), base["rotulo"])),
            })
        else:
            linhas.append({
                "de": base["id"],
                "para": d["id"],
                "a_partir_de": achou,
                "nunca_vale": False,
                "frase": ("A partir de %s de visita, «%s» passa a valer mais a pena que "
                          "comprar «%s» de novo."
                          % (dias_em_palavra(achou), d["rotulo"], base["rotulo"])),
            })

    return {"aplicavel": True, "motivo": None, "base": base["id"], "linhas": linhas}


# ---------------------------------------------------------------------------
# INDICES DO BANCO
# ---------------------------------------------------------------------------

def indexar(banco):
    cidades = {}
    for c in (banco.get("cidades") or []):
        cidades[c.get("id")] = c
    fontes = {}
    for f in (banco.get("fontes") or []):
        fontes[f.get("id")] = f
    experiencias = {}
    for e in (banco.get("experiencias") or []):
        experiencias[e.get("id")] = e
    return cidades, fontes, experiencias


def versao_de(experiencia, versao_id):
    for v in (experiencia.get("versoes") or []):
        if v.get("id") == versao_id:
            return v
    return None


def degraus_da_experiencia(experiencia):
    """Extrai a RELACAO que a Conta 3 recebe. Nenhuma decisao mora aqui."""
    return [{"id": v.get("id"), "rotulo": v.get("rotulo"),
             "preco": v.get("preco"), "dias_de_uso": v.get("dias_de_uso")}
            for v in (experiencia.get("versoes") or [])]


# ---------------------------------------------------------------------------
# O BLOCO DE COMPRA (especificacao 2.9)
# ---------------------------------------------------------------------------

def bloco_de_compra(esquema, experiencia, cidade):
    """O piso e DERIVADO da cidade pelo molde do esquema, nunca lido do registro.

    Comparar o derivado com o gravado e trabalho do validador; aqui a F1 usa o
    DERIVADO, porque URL que a tela publica tem de vir do molde -- senao ela
    envelhece calada no dia em que o molde mudar, e quem muda o molde nao mexe em
    cada registro.
    """
    molde = molde_do_piso(esquema)
    rel = rel_do_piso(esquema)
    afiliado = experiencia.get("afiliado") or {}
    slug = (cidade or {}).get("slug_plataforma")
    if not slug:
        raise BancoIncompleto(
            "cidade %r sem `slug_plataforma`: sem ela o piso de compra nao e "
            "fabricavel, e item sem piso e defeito duro da 25.2."
            % (experiencia.get("cidade"),))

    degrau_1 = afiliado.get("url_produto")
    degrau_2 = molde.replace("{slug_plataforma}", slug)
    programa = afiliado.get("programa")

    if degrau_1:
        url, degrau = degrau_1, 1
        o_que_e = "a página desta experiência na plataforma, em português"
    else:
        url, degrau = degrau_2, 2
        o_que_e = "a página de %s na plataforma" % ((cidade or {}).get("nome") or slug)

    if programa:
        aviso = ("Este link rende comissão para a JornadaFly, sem mudar o preço de "
                 "quem compra.")
    else:
        aviso = ("Este link NÃO rende comissão: a JornadaFly ainda não tem programa de "
                 "afiliado cadastrado, e por isso ele sai sem a marcação de link "
                 "patrocinado.")

    return {
        "degrau": degrau,
        "o_que_e": o_que_e,
        "url": url,
        "rel": rel if not programa else "sponsored nofollow noopener",
        "programa": programa,
        "aviso": aviso,
        "motivo_sem_degrau_1": afiliado.get("motivo_sem_url_produto") if not degrau_1 else None,
    }


# ---------------------------------------------------------------------------
# PRESTACAO DE CONTAS (especificacao 2.7)
# ---------------------------------------------------------------------------

def prestacao_de_contas(experiencia, versao_escolhida):
    """Toda versao do banco daquela experiencia aparece EXATAMENTE uma vez.

    A escolhida com o preco; as outras numa linha que diz por que nao estao. A soma
    dos nomeados fecha contra o tamanho CONTADO do banco, nunca contra um numero
    digitado -- e e por isso que esta funcao devolve as duas contagens.
    """
    linhas = []
    for v in (experiencia.get("versoes") or []):
        escolhida = v.get("id") == versao_escolhida.get("id")
        if v.get("preco") is None:
            valor = "sem preço lido"
        else:
            valor = dinheiro(v["preco"], v.get("moeda"))
        if escolhida:
            frase = "%s: %s, a versão que você escolheu." % (v.get("rotulo"), valor)
        else:
            frase = "%s: %s, outra versão vendida pelo operador." % (v.get("rotulo"), valor)
        linhas.append({"versao": v.get("id"), "escolhida": escolhida, "frase": frase})
    return {
        "linhas": linhas,
        "versoes_nomeadas": len(linhas),
        "versoes_no_banco": len(experiencia.get("versoes") or []),
    }


# ---------------------------------------------------------------------------
# A FAIXA ETARIA, E AS TRES RECUSAS QUE ANTES ERAM UMA (especificacao 2.6)
# ---------------------------------------------------------------------------

def faixa_etaria_da_versao(versao):
    """Le a faixa DA VERSAO escolhida, nunca da experiencia.

    Essa e a diferenca entre responder o preco do grupo e responder o preco de um
    grupo que compra outro bilhete: na Torre Eiffel a crianca de 4 a 11 anos paga
    3,80 EUR pela escada e 9,20 EUR pelo elevador ate o topo.
    """
    faixas = versao.get("faixa_etaria")
    lacunas = versao.get("faixas_que_a_fonte_declara_e_a_leitura_nao_transcreveu") or []

    frases = []
    de_outro_bilhete = []
    if faixas:
        for f in faixas:
            if f.get("preco") is None:
                frases.append(
                    "%s: o operador declara esta faixa e NÃO publica o preço dela. %s"
                    % (f.get("rotulo"), f.get("declarado_como") or ""))
            elif Decimal(str(f["preco"])) == 0:
                frases.append("%s: não paga. %s" % (f.get("rotulo"),
                                                    f.get("condicao") or ""))
            else:
                frases.append("%s: %s neste bilhete."
                              % (f.get("rotulo"), dinheiro(f["preco"], f.get("moeda"))))
            if f.get("numero_da_frase_e_de_outra_versao"):
                de_outro_bilhete.append({
                    "faixa": f.get("rotulo"),
                    "frase": ("O operador escreve: «%s». Esse número é de OUTRO bilhete, "
                              "e a JornadaFly não o usa como se fosse deste."
                              % (f.get("se_nao_cumprir") or f.get("declarado_como") or "")),
                })

    nao_lidas = []
    for l in lacunas:
        nao_lidas.append({
            "faixa": l.get("rotulo"),
            "frase": ("O operador cobra uma tarifa de %s neste bilhete e nós ainda não a "
                      "lemos. Isso é diferente de «o operador não declara tarifa de %s»: "
                      "confundir as duas é cobrar de você o preço cheio de quem tinha "
                      "desconto." % (l.get("rotulo"), l.get("rotulo"))),
        })

    return {
        "tem_faixa": bool(faixas),
        "frases": frases,
        "motivo_sem_faixa": versao.get("motivo_sem_faixa_etaria") if not faixas else None,
        "declaradas_e_nao_lidas": nao_lidas,
        "numero_de_outro_bilhete": de_outro_bilhete,
    }


# ---------------------------------------------------------------------------
# A ELEGIBILIDADE — O PRECO DE QUEM PROVA O QUE NAO E IDADE (27/10/2026)
#
# Esta e a metade da resposta que esta ilha nao tinha e que mais importa para o
# leitor DELA. O eixo declarado da F1 e `dias x pessoas x padrao`, e no Bondinho o
# que mais move o preco nao e nenhum dos tres: e quem compra. O mesmo Bilhete
# Bondinho custa R$ 205 no balcao, R$ 160 de quem nasceu e mora no Brasil e R$ 89
# de quem e do estado do Rio — 2,3 vezes entre a ponta cheia e a ponta barata,
# maior que qualquer diferenca de versao deste banco. Uma ilha escrita em portugues
# do Brasil que servisse os R$ 205 calada cobraria do proprio leitor 28% a mais do
# que o operador cobra dele.
#
# A CONTA NAO MUDA, E ISSO E REGRA E NAO PREGUICA. O total continua saindo da
# tarifa cheia, porque a regra de divergencia desta ilha resolve para o MAIOR
# quando nao ha autoridade e porque o erro caro e subestimar: quem chega a
# bilheteria sem o comprovante de residencia paga o cheio. O que a tela ganha e a
# escada de quem compra, com a condicao, a frase da fonte e o que se paga sem
# provar. E a F1 NUNCA multiplica elegibilidade por faixa etaria — medido na mesma
# carga: metade de R$ 89 e R$ 44,50 e o operador cobra R$ 44 por crianca moradora
# do Rio. Cinquenta centavos inventados numa conta que pareceria certa.
# ---------------------------------------------------------------------------

def elegibilidade_da_versao(versao):
    """Le a elegibilidade DA VERSAO escolhida, nunca da experiencia.

    Mesma razao da faixa etaria: no Bondinho a promocional de brasileiro existe no
    Bilhete Bondinho e nao existe nas tarifas que ja sao promocionais.
    """
    elegs = versao.get("elegibilidade")
    frases = []
    nao_acumulam = []
    if elegs:
        for e in elegs:
            if e.get("preco") is None:
                frases.append(
                    "%s: o operador declara esta tarifa e NÃO publica o preço dela. %s"
                    % (e.get("rotulo"), e.get("declarado_como") or ""))
            elif Decimal(str(e["preco"])) == 0:
                frases.append("%s: não paga. %s"
                              % (e.get("rotulo"), e.get("condicao") or ""))
            else:
                frases.append(
                    "%s: %s neste bilhete, para quem prova %s. Sem provar, %s."
                    % (e.get("rotulo"), dinheiro(e["preco"], e.get("moeda")),
                       e.get("condicao") or "a condição",
                       e.get("se_nao_cumprir") or "paga a tarifa cheia"))
            if e.get("acumula_com_faixa_etaria") is False:
                nao_acumulam.append({
                    "elegibilidade": e.get("rotulo"),
                    "frase": ("%s não se soma ao desconto por idade: o operador vende as "
                              "duas coisas separadas, e a JornadaFly não multiplica uma "
                              "pela outra para inventar um terceiro preço."
                              % e.get("rotulo")),
                })
    return {
        "tem_elegibilidade": bool(elegs),
        "frases": frases,
        "motivo_sem_elegibilidade": None if elegs else versao.get("motivo_sem_elegibilidade"),
        "nao_acumulam_com_faixa_etaria": nao_acumulam,
        # A conta NUNCA usa estes numeros. O campo existe para o portao poder afirmar
        # isso: ele confere que nenhum preco de elegibilidade aparece no total.
        "precos_que_a_conta_NAO_usa": [e.get("preco") for e in (elegs or [])
                                       if e.get("preco") is not None],
    }


# ---------------------------------------------------------------------------
# A RESPOSTA INTEIRA
# ---------------------------------------------------------------------------

def responder(experiencia_id, versao_id, pessoas, banco=None, esquema=None,
              constantes=None):
    banco = banco if banco is not None else carregar_banco()
    esquema = esquema if esquema is not None else carregar_esquema()
    constantes = constantes if constantes is not None else carregar_constantes()

    faltas = conferir_moedas_do_vocabulario(esquema) + conferir_unidades_do_vocabulario(esquema)
    if faltas:
        raise BancoIncompleto(
            "a F1 e o vocabulario do esquema discordam: %s. Vocabulario novo entra no "
            "esquema e na ferramenta na mesma passada." % "; ".join(faltas))

    cidades, fontes, experiencias = indexar(banco)

    resposta = {
        "estado": {"experiencia": experiencia_id, "versao": versao_id, "pessoas": pessoas},
        "recusa_dura": None,
        "frase_resposta": None,
        "cartao_brasileiro": None,
        "contas": None,
        "escada": None,
        "inclui": None,
        "nao_inclui": None,
        "faixa_etaria": None,
        "bloco_de_compra": None,
        "prestacao_de_contas": None,
        "recusas": [],
        "como_sabemos": None,
    }

    def recusa(codigo, frase):
        resposta["recusas"].append({"codigo": codigo, "frase": frase})

    # ---- as duas recusas DURAS: elas nao publicam numero nenhum.
    if not isinstance(pessoas, int) or isinstance(pessoas, bool) \
            or pessoas < PESSOAS_MINIMO or pessoas > PESSOAS_MAXIMO:
        resposta["recusa_dura"] = {
            "codigo": "grupo_fora_da_faixa",
            "frase": ("A JornadaFly responde para grupos de %d a %d pessoas. Acima de %d a "
                      "compra vira negociação com o operador, e multiplicar o preço de "
                      "tabela daria um número que ninguém vai cobrar de você."
                      % (PESSOAS_MINIMO, PESSOAS_MAXIMO, PESSOAS_MAXIMO)),
        }
        return resposta

    experiencia = experiencias.get(experiencia_id)
    if experiencia is None:
        resposta["recusa_dura"] = {
            "codigo": "experiencia_desconhecida",
            "frase": ("A JornadaFly não tem esta experiência no banco. A lista da tela é "
                      "fechada e sai do banco: ela nunca aceita texto livre."),
        }
        return resposta

    versao = versao_de(experiencia, versao_id)
    if versao is None:
        resposta["recusa_dura"] = {
            "codigo": "versao_desconhecida",
            "frase": ("Esta experiência não tem esta versão no banco. O seletor de versão "
                      "só oferece o que o operador realmente vende e o banco conhece."),
        }
        return resposta

    if versao.get("preco") is None:
        resposta["recusa_dura"] = {
            "codigo": "preco_nao_lido",
            "frase": ("O operador vende esta versão e a JornadaFly ainda não leu o preço "
                      "dela. A página diz isso em vez de mostrar um número que ninguém "
                      "conferiu."),
        }
        return resposta

    cidade = cidades.get(experiencia.get("cidade"))
    moeda = versao.get("moeda")

    # ---- CONTAS 1 e 2
    total, por_pessoa, unidades = total_do_grupo(
        versao["preco"], versao.get("unidade_de_preco"),
        versao.get("capacidade_maxima"), pessoas)

    # ---- CONTA 4: O IOF, E ELE NAO EXISTE EM COMPRA EM REAL (27/10/2026)
    #
    # O IOF de 3,5% e imposto sobre COMPRA INTERNACIONAL no cartao — o id da
    # constante diz isso com todas as letras:
    # `iof-compra-internacional-cartao-pessoa-fisica`. Ate 27/10/2026 esta conta
    # rodava em TODA versao, e estava certa POR ACIDENTE: as quatro experiencias
    # deste banco cobravam em euro e em dolar, e para elas a linha do cartao
    # brasileiro e o diferencial mais barato da ilha. Entrou o Bondinho, que cobra
    # R$ 205 de um brasileiro no caixa dele, e a mesma conta passou a publicar
    # «R$ 144,90» num bilhete de R$ 140 — imposto de compra no exterior somado a uma
    # compra que nao sai do pais. Dinheiro INVENTADO na pagina do dinheiro, e a
    # pagina pareceria certa, porque a aritmetica esta certa: so a pergunta e que
    # nao existia.
    #
    # E e o TERCEIRO defeito desta mesma familia achado na mesma carga, com o
    # contador `experiencias_com_preco_em_brl` do validar-banco.py e o portao do
    # cambio do teste-f1.py. Os tres foram escritos num mundo sem real, os tres
    # estavam corretos enquanto o mundo nao mudou, e os tres erram calados.
    compra_internacional = moeda != "BRL_do_operador"
    if compra_internacional:
        iof = iof_publicavel(constantes)
        total_iof = com_iof(total, iof["valor"])
        por_pessoa_iof = _centavo(total_iof / Decimal(pessoas))
    else:
        # A constante continua sendo LIDA, e de proposito: se ela deixar de ser
        # `publicavel`, a ilha tem de saber disso mesmo nas paginas em real, porque e
        # a mesma constante que as outras quatro experiencias usam. O que nao se faz
        # e aplica-la.
        iof_publicavel(constantes)
        iof = None
        total_iof = None
        por_pessoa_iof = None

    data = data_em_portugues(versao.get("data_leitura"))
    unidade = versao.get("unidade_de_preco")

    resposta["contas"] = {
        "preco_unitario": versao["preco"],
        "unidade_de_preco": unidade,
        "capacidade_maxima": versao.get("capacidade_maxima"),
        "unidades_necessarias": unidades,
        "moeda": moeda,
        "total": str(total),
        "total_escrito": dinheiro(total, moeda),
        "por_pessoa": str(por_pessoa),
        "por_pessoa_escrito": dinheiro(por_pessoa, moeda),
        "iof_percentual": iof["valor"] if iof else None,
        "compra_internacional": compra_internacional,
        "motivo_sem_iof": None if compra_internacional else (
            "O operador cobra em real e a compra nao e internacional: o IOF de 3,5%% "
            "incide sobre compra internacional no cartao, e somar aqui seria cobrar do "
            "leitor um imposto que ele nao paga. Esta e a primeira experiencia deste "
            "banco em real, e e por ela que a conta passou a perguntar a moeda."),
        "total_com_iof": str(_centavo(total_iof)) if total_iof is not None else None,
        "total_com_iof_escrito": dinheiro(total_iof, moeda) if total_iof is not None else None,
        "por_pessoa_com_iof_escrito": dinheiro(por_pessoa_iof, moeda) if por_pessoa_iof is not None else None,
        "data_leitura": versao.get("data_leitura"),
    }

    # ---- A FRASE-RESPOSTA. Numero primeiro, data ao lado, segunda pessoa, e a
    # unidade declarada quando ela NAO e por pessoa -- que e o defeito medido em
    # quatro das sete paginas de 14/09/2026.
    quem_declara = {
        "no_ato_oficial": "Tarifa oficial",
        "no_texto_da_fonte": "Preço publicado pelo operador",
        "no_contraste_da_propria_fonte": "Preço publicado pelo operador",
    }.get(versao.get("unidade_de_preco_declarada_por"), "Preço lido")

    if unidade == UNIDADE_POR_PESSOA:
        frase_unidade = "O preço é por pessoa."
    else:
        frase_unidade = (
            "O preço é %s, não por pessoa, e %s %s. Para %s, %s %s."
            % (ROTULO_DA_UNIDADE[unidade],
               _plural(versao.get("capacidade_maxima") or 0, "cabe", "cabem"),
               pessoas_em_palavra(versao.get("capacidade_maxima") or 0),
               pessoas_em_palavra(pessoas),
               _plural(unidades, "é", "são"),
               "%d %s" % (unidades, _plural(unidades, "unidade", "unidades"))))

    resposta["frase_resposta"] = (
        "%s para %s, %s: %s no total, %s por pessoa. %s %s. Leitura de %s."
        % (experiencia.get("nome"), pessoas_em_palavra(pessoas), versao.get("rotulo"),
           dinheiro(total, moeda), dinheiro(por_pessoa, moeda), frase_unidade,
           quem_declara, data))

    # A LINHA DO CARTAO SO EXISTE EM COMPRA INTERNACIONAL. Em compra em real ela nao
    # some calada: a tela diz POR QUE nao ha IOF, porque o leitor que veio de uma
    # pagina de euro desta mesma ilha aprendeu a esperar essa linha, e a ausencia dela
    # sem explicacao parece esquecimento. Lista vazia nao some da tela, e linha que
    # nao se aplica tambem nao.
    if compra_internacional:
        resposta["cartao_brasileiro"] = (
            "No cartão brasileiro, o IOF de %s%% entra por cima: %s no total, ou %s por "
            "pessoa." % (("%g" % iof["valor"]).replace(".", ","),
                         dinheiro(total_iof, moeda), dinheiro(por_pessoa_iof, moeda)))
    else:
        resposta["cartao_brasileiro"] = (
            "Sem IOF: o operador cobra em real, e o IOF de %s%% incide sobre compra "
            "internacional no cartão. O que está acima é o que você paga."
            % ("%g" % iof_publicavel(constantes)["valor"]).replace(".", ","))

    # ---- CONTA 3
    resposta["escada"] = ponto_de_equilibrio(
        experiencia.get("eixo_das_versoes"), degraus_da_experiencia(experiencia))

    # ---- INCLUI / NAO INCLUI. Lista vazia NAO some: ela diz que o operador nao
    # declara, que e um fato sobre o operador e e informacao (especificacao 2.4).
    # A F1 ESCREVE A PROPRIA FRASE DE TELA, e nunca repassa o `motivo_*` do banco.
    # Os motivos do banco sao escritos para a PROXIMA EXECUCAO -- citam nome de campo,
    # data de migracao e numero de secao do contrato -- e a 32.4 proibe texto de
    # bastidor da fabrica na pagina publica. Quem achou isto foi o portao desta
    # ferramenta, pela regua de acento: `unidade_de_preco` dentro de um motivo do
    # banco reprovava como portugues sem acento, e o defeito embaixo era maior que o
    # acento. O motivo continua no banco, onde ele serve; a tela recebe a frase que
    # responde ao visitante. Lista vazia NAO some (especificacao 2.4): ela diz que o
    # operador nao declara, que e um fato sobre o operador e e informacao.
    for campo, rotulo in (("inclui", "incluso"), ("nao_inclui", "fora")):
        itens = versao.get(campo) or []
        if itens:
            resposta[campo] = {"itens": itens,
                               "frase": "O que está %s: %s." % (rotulo, ", ".join(itens))}
        else:
            resposta[campo] = {
                "itens": [],
                "frase": "O operador não declara o que está %s neste bilhete." % rotulo,
            }

    # ---- FAIXA ETARIA, e as tres recusas que antes eram uma
    faixa = faixa_etaria_da_versao(versao)
    resposta["faixa_etaria"] = faixa

    # ---- A ELEGIBILIDADE, ao lado da faixa e nunca dentro dela
    eleg = elegibilidade_da_versao(versao)
    resposta["elegibilidade"] = eleg
    if not eleg["tem_elegibilidade"]:
        recusa("sem_elegibilidade",
               "Preço por residência ou nacionalidade: o operador não declara tarifa "
               "diferente por onde você mora ou de onde você é neste bilhete.")
    for n in eleg["nao_acumulam_com_faixa_etaria"]:
        recusa("elegibilidade_nao_acumula", n["frase"])
    if not faixa["tem_faixa"]:
        if unidade == UNIDADE_POR_PESSOA:
            recusa("sem_faixa_etaria",
                   "Desconto por idade: o operador não declara tarifa diferente por "
                   "idade neste bilhete.")
        else:
            recusa("sem_faixa_etaria",
                   "Desconto por idade: não há nenhum a declarar, porque o preço é %s e "
                   "não por pessoa. A criança não tem bilhete: ela ocupa lugar."
                   % ROTULO_DA_UNIDADE[unidade])
    for l in faixa["declaradas_e_nao_lidas"]:
        recusa("faixa_declarada_e_nao_lida", l["frase"])
    for n in faixa["numero_de_outro_bilhete"]:
        recusa("numero_da_frase_e_de_outro_bilhete", n["frase"])

    # ---- A RECUSA DO REAL, com as constantes nomeadas em vez de descritas
    # A frase NAO nomeia as constantes: id de constante na tela e a ilha falando com o
    # visitante no vocabulario de quem a escreveu (32.4), e foi assim que a primeira
    # versao desta ferramenta publicou `cambio-eur-brl`. O que decide a frase continua
    # sendo o ARQUIVO: sem constante de cambio pendente, ela nao nasce.
    pendentes = [c for c in constantes_pendentes(constantes)
                 if str(c.get("id") or "").startswith("cambio")]
    if pendentes:
        recusa("sem_valor_em_real",
               "O valor em real depende do câmbio do dia do seu cartão, e a JornadaFly "
               "ainda não tem uma fonte de câmbio com data para publicar. A conta acima "
               "está na moeda que o operador cobra, que é a que não muda.")

    # ---- TEMPORADA
    if experiencia.get("temporada") is None:
        recusa("sem_temporada",
               "Alta e baixa temporada: o operador não declara preço diferente entre "
               "uma e outra, e a JornadaFly não inventa a diferença. Se o seu mês for "
               "de alta, confirme o valor com ele antes de fechar.")

    # ---- O STATUS DO REGISTRO, dito ao leitor e nao escondido
    if experiencia.get("status") != "publicavel":
        recusa("registro_pendente_de_releitura",
               "Este preço veio de uma leitura que a JornadaFly ainda não conferiu na "
               "fonte da própria autoridade, e por isso ela não o chama de confirmado. "
               "Ele está aqui com a data em que foi lido, para você decidir sabendo "
               "disso.")

    # ---- ACRESCIMOS declarados como aproximados: faixa, nunca dentro do total
    for a in (versao.get("acrescimos") or []):
        if a.get("aproximado"):
            recusa("acrescimo_aproximado",
                   "%s: o operador declara «%s». A JornadaFly não soma número aproximado "
                   "no total." % (a.get("o_que_e"), a.get("declarado_como")))

    resposta["bloco_de_compra"] = bloco_de_compra(esquema, experiencia, cidade)
    resposta["prestacao_de_contas"] = prestacao_de_contas(experiencia, versao)

    # ---- COMO SABEMOS (a camada de prova, depois do bloco de compra)
    fonte = fontes.get(versao.get("fonte")) or {}
    divergentes = []
    for d in (experiencia.get("declaracoes") or []):
        if not d.get("publicavel_na_tela"):
            continue
        escrito = dinheiro_ou_faixa(d.get("valor"), d.get("moeda"))
        divergentes.append({
            "publicador": d.get("publicador"),
            "frase": "%s publicou %s (%s), lido em %s."
                     % (d.get("publicador"), escrito,
                        d.get("diz"), data_em_portugues(d.get("data_leitura"))),
            # Fonte com interesse comercial se declara AO LADO do numero, nunca depois
            # dele: a regra vem de constantes.json e vale para toda declaracao.
            "interesse_comercial": d.get("interesse_comercial"),
        })

    resposta["como_sabemos"] = {
        "operador": (experiencia.get("operador") or {}).get("nome"),
        "url_operador": (experiencia.get("operador") or {}).get("url"),
        "motivo_sem_url_operador": (experiencia.get("operador") or {}).get("motivo_sem_url"),
        "fonte": versao.get("fonte"),
        "documento": fonte.get("documento"),
        "motivo_sem_documento": fonte.get("motivo_sem_documento"),
        "canal_de_leitura": fonte.get("leitura"),
        "data_leitura": versao.get("data_leitura"),
        "declarado_como": versao.get("declarado_como"),
        "unidade_declarada_por": versao.get("unidade_de_preco_declarada_por"),
        "divergentes": divergentes,
    }

    return resposta


# ---------------------------------------------------------------------------
# O DOMINIO INTEIRO, E A TABELA PRE-RENDERIZADA
# ---------------------------------------------------------------------------

def estados(banco=None):
    """Todo (experiencia, versao, pessoas) que a F1 serve, mais as duas bordas.

    As bordas entram no dominio de proposito: 0 e 13 pessoas sao as recusas duras,
    e grade que nao pisa na borda e amostra com nome de grade (secao 8).
    """
    banco = banco if banco is not None else carregar_banco()
    saida = []
    for exp in (banco.get("experiencias") or []):
        for v in (exp.get("versoes") or []):
            for pessoas in list(range(PESSOAS_MINIMO, PESSOAS_MAXIMO + 1)) + [0, PESSOAS_MAXIMO + 1]:
                saida.append((exp.get("id"), v.get("id"), pessoas))
    return saida


def todas_as_respostas(banco=None, esquema=None, constantes=None):
    banco = banco if banco is not None else carregar_banco()
    esquema = esquema if esquema is not None else carregar_esquema()
    constantes = constantes if constantes is not None else carregar_constantes()
    return [responder(e, v, p, banco, esquema, constantes) for e, v, p in estados(banco)]


def tabela_pre_renderizada(banco=None, esquema=None, constantes=None):
    """A metade que um modelo de linguagem le sem preencher formulario (secao 5).

    Cada experiencia x cada versao x 1, 2, 4 e 6 pessoas. O 6 e o que mostra o
    degrau de capacidade: para a gondola, a linha de 6 pessoas diz 180 EUR e nao
    90 EUR divididos por 6, e e esse numero que nenhuma das sete paginas medidas
    em 14/09/2026 publica.
    """
    banco = banco if banco is not None else carregar_banco()
    esquema = esquema if esquema is not None else carregar_esquema()
    constantes = constantes if constantes is not None else carregar_constantes()

    linhas = []
    for exp in (banco.get("experiencias") or []):
        for v in (exp.get("versoes") or []):
            for pessoas in PESSOAS_DA_TABELA:
                r = responder(exp.get("id"), v.get("id"), pessoas, banco, esquema, constantes)
                if r["recusa_dura"] or not r["contas"]:
                    continue
                c = r["contas"]
                linhas.append({
                    "experiencia": exp.get("nome"),
                    "versao": v.get("rotulo"),
                    "pessoas": pessoas,
                    "total": c["total_escrito"],
                    "por_pessoa": c["por_pessoa_escrito"],
                    "unidade_de_preco": c["unidade_de_preco"],
                    "unidades_necessarias": c["unidades_necessarias"],
                    "com_iof": c["total_com_iof_escrito"],
                    "lido_em": data_em_portugues(c["data_leitura"]),
                })
    return linhas


# ---------------------------------------------------------------------------
# TELA
# ---------------------------------------------------------------------------

def imprimir(r):
    out = []
    if r["recusa_dura"]:
        out.append("RECUSA (%s): %s" % (r["recusa_dura"]["codigo"], r["recusa_dura"]["frase"]))
        return "\n".join(out)
    out.append(r["frase_resposta"])
    out.append(r["cartao_brasileiro"])
    out.append("")
    out.append(r["inclui"]["frase"])
    out.append(r["nao_inclui"]["frase"])
    out.append("")
    if r["escada"]["aplicavel"]:
        for l in r["escada"]["linhas"]:
            out.append("ESCADA: %s" % l["frase"])
    else:
        out.append("ESCADA: %s" % r["escada"]["motivo"])
    out.append("")
    b = r["bloco_de_compra"]
    out.append("COMPRA (degrau %d, %s): %s  [rel=%s]" % (b["degrau"], b["o_que_e"], b["url"], b["rel"]))
    out.append("  %s" % b["aviso"])
    out.append("")
    out.append("AS VERSÕES DESTE OPERADOR (%d de %d nomeadas):"
               % (r["prestacao_de_contas"]["versoes_nomeadas"],
                  r["prestacao_de_contas"]["versoes_no_banco"]))
    for l in r["prestacao_de_contas"]["linhas"]:
        out.append("  - %s" % l["frase"])
    if r["faixa_etaria"]["frases"]:
        out.append("")
        out.append("IDADE:")
        for f in r["faixa_etaria"]["frases"]:
            out.append("  - %s" % f)
    out.append("")
    out.append("O QUE NÃO RESPONDEMOS (%d):" % len(r["recusas"]))
    for rec in r["recusas"]:
        out.append("  - [%s] %s" % (rec["codigo"], rec["frase"]))
    out.append("")
    cs = r["como_sabemos"]
    out.append("COMO SABEMOS: %s | fonte %s | lido em %s | %s"
               % (cs["operador"], cs["fonte"], data_em_portugues(cs["data_leitura"]),
                  cs["declarado_como"]))
    for d in cs["divergentes"]:
        out.append("  divergente: %s" % d["frase"])
    return "\n".join(out)


def main():
    argumentos = sys.argv[1:]
    if argumentos and argumentos[0] == "--contar":
        banco = carregar_banco()
        todos = estados(banco)
        print("experiencias: %d" % len(banco.get("experiencias") or []))
        print("versoes:      %d" % sum(len(e.get("versoes") or [])
                                       for e in (banco.get("experiencias") or [])))
        print("estados:      %d  (versoes x %d numeros de pessoas, com as duas bordas)"
              % (len(todos), PESSOAS_MAXIMO - PESSOAS_MINIMO + 3))
        print("linhas da tabela pre-renderizada: %d" % len(tabela_pre_renderizada(banco)))
        return

    if len(argumentos) == 3:
        eid, vid, pessoas = argumentos[0], argumentos[1], int(argumentos[2])
    else:
        # O caso que ESPECIFICA a ferramenta (especificacao 2.2): a gondola de
        # Veneza, de dia, para 4 pessoas. 90 EUR no total e 22,50 por pessoa -- e
        # nao "80 EUR" nem "34 EUR por pessoa", que e o que esta no ar.
        eid, vid, pessoas = "veneza-passeio-de-gondola", "diurno", 4

    print(imprimir(responder(eid, vid, pessoas)))


if __name__ == "__main__":
    main()
