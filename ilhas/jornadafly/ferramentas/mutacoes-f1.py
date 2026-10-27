#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra a F1 de proposito e verifica que ferramentas/teste-f1.py reprova.

    python3 ferramentas/mutacoes-f1.py

Sai com codigo 1 se qualquer mutacao decidir errado.

E O UNICO PORTAO DESTA PASTA QUE MEDE OS OUTROS PORTOES. Quatro tipos:

  MUNDOS (esperam PASSAR) -- constroem o caso que o banco ainda nao tem e exigem
  que o portao o aprove: eixo de quantidade com uma versao so, empate de preco
  entre quantidades, `inclui` preenchido, item com programa de afiliado. Sao a
  metade que prova que o portao nao esta apenas dizendo nao para tudo.

  QUEBRAS DE REFERENCIA (esperam REPROVAR) -- editam o CODIGO da f1-referencia.py e
  exigem que o portao as veja. Cada uma declara a FRASE que espera ouvir de volta,
  porque reprovar nao e a mesma coisa que reprovar PELO MOTIVO CERTO.

  QUEBRAS DE BANCO (esperam REPROVAR) -- mexem no dado, nao no codigo.

  MORTES (esperam MORRER) -- tiram do esquema ou das constantes uma chave de que a
  F1 depende, e exigem que ela LEVANTE em vez de cair num literal. Chave que some da
  fonte tem de matar a referencia; regua que le a propria lista de um arquivo de
  dados aprova tudo, em silencio, no dia em que o arquivo perder a chave (26.2).

TRAVA DE ALVO EXATO, e ela e o que separa esta bateria de um relatorio verde: toda
quebra de referencia declara o TEXTO que vai editar, e `_referencia_mutada` RECUSA
OPERAR se o texto nao estiver mais la. Quando a regra muda de linha, a mutacao que
editava a linha antiga vira inerte -- a cicatriz das 18 de 20 da Robometria -- e sem
a trava cinco mutacoes passam medindo nada e o relatorio diz "0 sobrevivente".
"""

import copy
import importlib.util
import io
import json
import os
import sys
import types

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(AQUI)
DADOS = os.path.join(BASE, "dados")

REFERENCIA = os.path.join(AQUI, "f1-referencia.py")


def _ler(nome):
    with io.open(os.path.join(DADOS, nome), encoding="utf-8") as f:
        return json.load(f)


def _portao():
    spec = importlib.util.spec_from_file_location(
        "teste_f1", os.path.join(AQUI, "teste-f1.py"))
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def _gerador():
    spec = importlib.util.spec_from_file_location(
        "gerar_f1", os.path.join(AQUI, "gerar-f1.py"))
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


FONTE_DA_REFERENCIA = io.open(REFERENCIA, encoding="utf-8").read()


def _referencia_mutada(trocas=()):
    """Carrega a f1-referencia.py com o codigo editado, de um texto em memoria.

    Nunca grava nada em disco. `trocas` e uma lista de (antes, depois), e cada
    `antes` tem de aparecer EXATAMENTE uma vez na fonte -- senao esta funcao
    levanta, e a bateria para. E a trava de alvo exato.
    """
    fonte = FONTE_DA_REFERENCIA
    for antes, depois in trocas:
        quantas = fonte.count(antes)
        if quantas != 1:
            raise SystemExit(
                "MUTACAO INERTE: o alvo %r aparece %d vezes na f1-referencia.py (tem "
                "de aparecer 1). A regra mudou de linha e esta mutacao parou de medir "
                "o que diz medir." % (antes[:70], quantas))
        fonte = fonte.replace(antes, depois)
    modulo = types.ModuleType("f1_referencia_mutada")
    modulo.__file__ = REFERENCIA
    codigo = compile(fonte, REFERENCIA, "exec")
    exec(codigo, modulo.__dict__)
    return modulo


# ---------------------------------------------------------------------------
# OS MUNDOS
# ---------------------------------------------------------------------------

def _achar(banco, eid):
    for e in banco["experiencias"]:
        if e["id"] == eid:
            return e
    raise SystemExit("MUTACAO INERTE: a experiencia %r saiu do banco." % eid)


def mundo_eixo_de_quantidade_com_uma_versao(banco, esquema, constantes):
    """Angkor com UMA versao: o eixo continua sendo de quantidade e nao ha conta.

    O esquema permite e o banco nao tem. A F1 tem de dizer que nao ha com que
    comparar, em vez de cair numa lista vazia com cara de conta feita.
    """
    exp = _achar(banco, "siem-reap-angkor-pass")
    exp["versoes"] = exp["versoes"][:1]
    return banco, esquema, constantes


def mundo_empate_de_preco_entre_quantidades(banco, esquema, constantes):
    """1, 3 e 7 dias pelo MESMO preco: a versao mais cara nao existe.

    Mesma familia do empate no topo que o Clube do Mosaico pagou em 08/10/2026.
    """
    exp = _achar(banco, "siem-reap-angkor-pass")
    for v in exp["versoes"]:
        v["preco"] = 37
    return banco, esquema, constantes


def mundo_com_inclui_preenchido(banco, esquema, constantes):
    """Lista `inclui` NAO vazia: o banco de hoje tem as 11 versoes com lista vazia."""
    v = _achar(banco, "veneza-passeio-de-gondola")["versoes"][0]
    v["inclui"] = ["o gondoleiro", "o percurso pelos canais"]
    return banco, esquema, constantes


def mundo_com_programa_de_afiliado(banco, esquema, constantes):
    """Programa cadastrado: o link passa a ser patrocinado, e isso e CERTO.

    Nenhum programa esta cadastrado hoje, e por isso o portao que proibe
    `sponsored` em link cru nunca viu o outro lado da fronteira. Este mundo e o
    outro lado.
    """
    exp = _achar(banco, "veneza-passeio-de-gondola")
    exp["afiliado"]["programa"] = "civitatis"
    return banco, esquema, constantes


# ---------------------------------------------------------------------------
# OS MUNDOS QUE AS QUEBRAS COMBINADAS PRECISAM
# ---------------------------------------------------------------------------

def _molde_mudado(esquema):
    """O molde do piso muda -- e e a unica coisa que se muda quando ele muda.

    No banco de hoje a URL DERIVADA e a URL GRAVADA sao a mesma letra por letra,
    porque o validador obriga. Entao a quebra "ler do registro em vez de derivar" nao
    tem como morder: as duas copias concordam. Mexer no molde produz a divergencia --
    e e o mundo REAL do dia em que a plataforma mudar o endereco dela, que e
    justamente o dia em que ninguem vai querer editar 4 registros a mao.
    """
    esquema["piso_de_compra"]["molde"] = "https://exemplo-de-mutacao.invalid/{slug_plataforma}/"
    return esquema


def _sem_url_de_produto(banco):
    """Tira o degrau 1 de todos os itens, para que o piso seja o degrau 2 em todos.

    Sem isto a gondola continuaria no degrau 1 (ela tem `url_produto`) e a quebra do
    molde nao a alcancaria -- e ela e a unica experiencia com declaracoes
    divergentes, ou seja a mais medida desta bateria.
    """
    for exp in banco["experiencias"]:
        exp["afiliado"]["url_produto"] = None
        exp["afiliado"]["motivo_sem_url_produto"] = "mundo de mutacao"
    return banco


def _coliseu_com_dias_de_uso(banco):
    """Da quantidade aos dois bilhetes do Coliseu, que diferem em ESCOPO.

    E o mundo em que a quebra da escada morde. Sem ele, abrir o calculo para o eixo
    de escopo nao produz escada nenhuma: as versoes de escopo tem `dias_de_uso` null,
    o calculo cai na recusa de dado faltando e a mutacao volta VERDE sem medir nada.
    Este mundo e MENTIROSO de proposito, e quem o reprova e o validar-banco.py; aqui
    ele existe so para fazer a trava da escada ser alcancavel.
    """
    exp = _achar(banco, "roma-coliseu-ingresso")
    for i, v in enumerate(exp["versoes"]):
        v["dias_de_uso"] = i + 1
    return banco

# ---------------------------------------------------------------------------
# AS QUEBRAS DE REFERENCIA: (nome, trocas, frase esperada, muda_o_dado?)
#
# O QUARTO ELEMENTO NASCEU MEDIDO, em 22/10/2026, com duas mutacoes desta
# bateria voltando VERDES. O motivo e o que a secao 8 do ARQUIPELAGO.md chama de
# ausencia de contraexemplo confundida com prova: a mutacao do piso de compra
# trocava a derivacao pela leitura do registro, e os dois dao a MESMA URL em
# todos os registros do banco de hoje -- porque o validador obriga. E a mutacao
# da escada abria o calculo para o eixo de escopo, onde nenhuma versao tem
# quantidade, entao o calculo caia na recusa de dado faltando e nada acontecia.
# Nos dois casos o mundo em que a quebra morde exige MEXER NO DADO junto, e
# produzir o mundo e a unica forma de medir a trava.
# ---------------------------------------------------------------------------

ALVO_DA_FAIXA_SEM_MOTIVO = '        if unidade == UNIDADE_POR_PESSOA:\n            recusa("sem_faixa_etaria",\n                   "Desconto por idade: o operador não declara tarifa diferente por "\n                   "idade neste bilhete.")'
ALVO_DA_FAIXA_COM_MOTIVO = '        if True:\n            recusa("sem_faixa_etaria",\n                   "Desconto por idade: %s" % versao.get("motivo_sem_faixa_etaria"))'

QUEBRAS_DE_REFERENCIA = [
    ("o degrau de capacidade virou divisao para baixo",
     [("    return int(math.ceil(float(pessoas) / capacidade_maxima))",
       "    return max(1, int(float(pessoas) // capacidade_maxima))")],
     "degrau de capacidade nao dobrou", None),

    ("o arredondamento do centavo virou o do banqueiro",
     [('    return Decimal(str(valor)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)',
       '    return Decimal(str(valor)).quantize(Decimal("0.01"))')],
     "por pessoa", None),

    ("a frase-resposta perdeu o acento",
     [('        frase_unidade = "O preço é por pessoa."',
       '        frase_unidade = "O preco e por pessoa."')],
     "sem acento", None),

    # O ALVO AQUI E O `motivo_sem_faixa_etaria`, nao o `inclui_motivo_lista_vazia`.
    # A primeira versao desta mutacao atacava o segundo e PASSOU: o motivo da lista
    # vazia da gondola e prosa sem nome de campo dentro, entao nenhuma forma de
    # bastidor aparece e o portao nao tem como ver. O `motivo_sem_faixa_etaria` tem
    # nome de campo entre acentos graves, data de migracao e numero de secao -- e e
    # ele que a primeira versao da f1-referencia.py repassava para a tela. A licao e
    # de MUTACAO e nao de codigo: quebra que ataca a forma errada do mesmo defeito
    # volta verde e parece prova.
    ("o motivo do banco voltou para a tela",
     [(ALVO_DA_FAIXA_SEM_MOTIVO, ALVO_DA_FAIXA_COM_MOTIVO)],
     "texto de bastidor da fabrica", None),

    ("o piso de compra passou a ser lido do registro, com o molde mudado",
     [('        url, degrau = degrau_2, 2',
       '        url, degrau = afiliado.get("url_busca_produto"), 2')],
     "a derivacao da", lambda b, e, c: (_sem_url_de_produto(b), _molde_mudado(e), c)),

    ("link cru saindo como patrocinado",
     [('        "rel": rel if not programa else "sponsored nofollow noopener",',
       '        "rel": "sponsored nofollow noopener",')],
     "link CRU", None),

    ("a frase-resposta perdeu a data de leitura",
     [('        "%s para %s, %s: %s no total, %s por pessoa. %s %s. Leitura de %s."',
       '        "%s para %s, %s: %s no total, %s por pessoa. %s %s.%.0s"')],
     "SEM a data de leitura", None),

    ("a prestacao de contas deixou de nomear as outras versoes",
     [("        escolhida = v.get(\"id\") == versao_escolhida.get(\"id\")",
       "        escolhida = v.get(\"id\") == versao_escolhida.get(\"id\")\n"
       "        if not escolhida:\n"
       "            continue")],
     "a prestacao de contas nomeia", None),

    ("a escada passou a ser calculada tambem no eixo de escopo",
     [('    if eixo != "por_quantidade":',
       '    if eixo not in ("por_quantidade", "por_escopo", "por_momento"):')],
     "calculou escada onde a conta a mao diz que nao ha",
     lambda b, e, c: (_coliseu_com_dias_de_uso(b), e, c)),

    ("a tabela pre-renderizada parou em 4 pessoas",
     [("PESSOAS_DA_TABELA = (1, 2, 4, 6)", "PESSOAS_DA_TABELA = (1, 2, 4)")],
     "as pessoas da tabela da referencia", None),

    ("o teto do grupo subiu sem a especificacao subir",
     [("PESSOAS_MAXIMO = 12", "PESSOAS_MAXIMO = 20")],
     "a faixa de grupo da referencia", None),

    ("o grupo de 13 pessoas passou a receber conta",
     [("            or pessoas < PESSOAS_MINIMO or pessoas > PESSOAS_MAXIMO:",
       "            or pessoas < PESSOAS_MINIMO or pessoas > PESSOAS_MAXIMO + 1:")],
     "deveria recusar por grupo fora da faixa", None),

    ("a tela passou a publicar um valor em real",
     [('        "pessoa." % (("%g" % iof["valor"]).replace(".", ","),',
       '        "pessoa. Em real, R$ 0,00." % (("%g" % iof["valor"]).replace(".", ","),')],
     # A FRASE DO PORTAO MUDOU EM 27/10/2026, e a regra com ela: ele dizia «valor
     # em real» porque proibia o SIMBOLO, o que estava certo por acidente num
     # banco todo em euro e dolar. Agora proibe CONVERSAO — valor numa moeda que
     # nenhum registro daquela experiencia declara —, e e por essa frase que esta
     # quebra e cobrada. A quebra em si nao mudou: ela poe real na tela da gondola,
     # que cobra em euro, e isso continua sendo cambio com constante pendente.
     "so sai de conversao", None),

    ("a frase proibida do contrato entrou na tela",
     [('                "frase": "O operador não declara o que está %s neste bilhete." % rotulo,',
       '                "frase": "Link de loja em breve.",')],
     "frase proibida", None),

    ("o id da constante de cambio voltou para a tela",
     [('               "ainda não tem uma fonte de câmbio com data para publicar. A conta acima "',
       '               "ainda não tem fonte para o cambio-eur-brl publicar. A conta acima "')],
     "texto de bastidor da fabrica", None),
]


# ---------------------------------------------------------------------------
# AS QUEBRAS DE BANCO
# ---------------------------------------------------------------------------

def q_banco_sem_data_de_leitura(banco, esquema, constantes):
    _achar(banco, "veneza-passeio-de-gondola")["versoes"][0]["data_leitura"] = "14/09/2026"
    return banco, esquema, constantes


def q_banco_com_dias_em_eixo_de_escopo(banco, esquema, constantes):
    """O defeito mais caro que a Conta 3 pode cometer: comparar bilhetes que nao se
    substituem. Aqui o Coliseu ganha quantidade e a escada passa a existir."""
    exp = _achar(banco, "roma-coliseu-ingresso")
    exp["eixo_das_versoes"] = "por_quantidade"
    for i, v in enumerate(exp["versoes"]):
        v["dias_de_uso"] = i + 1
    return banco, esquema, constantes


def q_banco_sem_piso_de_compra(banco, esquema, constantes):
    exp = _achar(banco, "roma-coliseu-ingresso")
    exp["afiliado"]["url_busca_produto"] = None
    cidade = [c for c in banco["cidades"] if c["id"] == exp["cidade"]][0]
    cidade["slug_plataforma"] = None
    return banco, esquema, constantes


# NENHUMA QUEBRA DE BANCO SOBROU NESTA BATERIA, e a ausencia e um resultado medido
# em 22/10/2026, nao um esquecimento. As tres que foram escritas aqui decidiram
# diferente do esperado, e as tres pelo mesmo motivo de fronteira:
#
#   - data de leitura fora de AAAA-MM-DD e piso de compra sem slug MATAM a
#     referencia em vez de a fazerem publicar errado. Morrer e a reacao honesta, e
#     por isso as duas desceram para MORTES, abaixo.
#   - banco dando QUANTIDADE a bilhetes que diferem em ESCOPO passou, e tem de
#     passar: o portao da F1 confere a REFERENCIA contra o banco, e um banco que
#     MENTE e trabalho do validar-banco.py -- que o reprova, na quebra
#     `dias de uso num eixo de ESCOPO`. Esta e a fronteira entre os dois portoes, e
#     ela esta escrita aqui para a proxima execucao nao escrever a mesma mutacao de
#     novo esperando outra resposta. (Ele sobrevive nesta bateria como MUNDO, por
#     isso mesmo: e a prova de que o portao da F1 nao finge medir o que nao mede.)
QUEBRAS_DE_BANCO = []


# ---------------------------------------------------------------------------
# AS MORTES
# ---------------------------------------------------------------------------

def m_esquema_sem_molde(banco, esquema, constantes):
    del esquema["piso_de_compra"]["molde"]
    return banco, esquema, constantes


def m_esquema_sem_vocabulario_de_unidade(banco, esquema, constantes):
    del esquema["vocabularios"]["unidade_de_preco"]
    return banco, esquema, constantes


def m_esquema_sem_moeda_no_vocabulario(banco, esquema, constantes):
    esquema["vocabularios"]["moeda"] = [m for m in esquema["vocabularios"]["moeda"]
                                        if m != "EUR"]
    return banco, esquema, constantes


def m_esquema_sem_rel(banco, esquema, constantes):
    del esquema["piso_de_compra"]["rel_enquanto_nao_ha_programa"]
    return banco, esquema, constantes


def m_iof_pendente(banco, esquema, constantes):
    for c in constantes["constantes"]:
        if c["id"] == "iof-compra-internacional-cartao-pessoa-fisica":
            c["status"] = "pendente"
    return banco, esquema, constantes


def m_iof_removido(banco, esquema, constantes):
    constantes["constantes"] = [c for c in constantes["constantes"]
                                if c["id"] != "iof-compra-internacional-cartao-pessoa-fisica"]
    return banco, esquema, constantes


MORTES = [
    ("banco com data de leitura fora de AAAA-MM-DD", q_banco_sem_data_de_leitura),
    ("banco sem piso de compra derivavel", q_banco_sem_piso_de_compra),
    ("esquema sem o molde do piso de compra", m_esquema_sem_molde),
    ("esquema sem o vocabulario de unidade de preco", m_esquema_sem_vocabulario_de_unidade),
    ("esquema sem a moeda EUR no vocabulario", m_esquema_sem_moeda_no_vocabulario),
    ("esquema sem o rel do link cru", m_esquema_sem_rel),
    ("IOF com status pendente", m_iof_pendente),
    ("IOF fora do arquivo de constantes", m_iof_removido),
]


MUNDOS = [
    ("MUNDO eixo de quantidade com UMA versao", mundo_eixo_de_quantidade_com_uma_versao),
    ("MUNDO empate de preco entre quantidades", mundo_empate_de_preco_entre_quantidades),
    ("MUNDO versao com `inclui` preenchido", mundo_com_inclui_preenchido),
    ("MUNDO item com programa de afiliado cadastrado", mundo_com_programa_de_afiliado),
    ("MUNDO banco que MENTE: quantidade em bilhete de escopo (do validador, nao daqui)",
     q_banco_com_dias_em_eixo_de_escopo),
]


# ---------------------------------------------------------------------------
# A BATERIA
# ---------------------------------------------------------------------------

def _rodar(portao, gerador, f1, banco, esquema, constantes):
    """Roda o portao sobre um mundo, com o arquivo de respostas GERADO daquele mundo.

    Gerar o arquivo junto e o que impede a mutacao de reprovar pelo motivo errado:
    sem isto, toda quebra reprovaria tambem na secao 5 do portao (o arquivo gravado
    discordando do banco mutado), e nenhuma provaria reprovar pela sua propria
    afirmacao.
    """
    try:
        doc = gerador.montar(f1, banco, esquema, constantes)
    except Exception as erro:          # a referencia morreu ao gerar o dominio
        return "morre", ["%s: %s" % (type(erro).__name__, erro)]
    try:
        falhas, _ = portao.conferir(f1, banco, esquema, constantes, doc)
    except Exception as erro:
        return "morre", ["%s: %s" % (type(erro).__name__, erro)]
    return ("reprova" if falhas else "passa"), falhas


def main():
    portao = _portao()
    gerador = _gerador()
    banco = _ler("experiencias.json")
    esquema = _ler("esquema-banco.json")
    constantes = _ler("constantes.json")

    # Antes de tudo: o mundo REAL tem de passar. Mutacao sobre portao ja vermelho
    # nao mede nada.
    f1 = _referencia_mutada()
    decidiu, falhas = _rodar(portao, gerador, f1, copy.deepcopy(banco),
                             copy.deepcopy(esquema), copy.deepcopy(constantes))
    if decidiu != "passa":
        print("O MUNDO REAL JA ESTA REPROVADO — nenhuma mutacao mede nada assim (%s):"
              % decidiu)
        for f in falhas[:10]:
            print("  - %s" % f)
        sys.exit(1)

    resultados = []
    com_frase = 0

    for nome, funcao in MUNDOS:
        f1 = _referencia_mutada()
        b, e, c = funcao(copy.deepcopy(banco), copy.deepcopy(esquema),
                         copy.deepcopy(constantes))
        decidiu, falhas = _rodar(portao, gerador, f1, b, e, c)
        resultados.append((nome, "passa", decidiu, falhas, None))

    for nome, trocas, frase, muda_o_dado in QUEBRAS_DE_REFERENCIA:
        f1 = _referencia_mutada(trocas)
        b, e, c = (copy.deepcopy(banco), copy.deepcopy(esquema),
                   copy.deepcopy(constantes))
        if muda_o_dado is not None:
            b, e, c = muda_o_dado(b, e, c)
        decidiu, falhas = _rodar(portao, gerador, f1, b, e, c)
        resultados.append((nome, "reprova", decidiu, falhas, frase))
        if frase:
            com_frase += 1

    for nome, funcao, frase in QUEBRAS_DE_BANCO:
        f1 = _referencia_mutada()
        b, e, c = funcao(copy.deepcopy(banco), copy.deepcopy(esquema),
                         copy.deepcopy(constantes))
        decidiu, falhas = _rodar(portao, gerador, f1, b, e, c)
        resultados.append((nome, "reprova", decidiu, falhas, frase))
        if frase:
            com_frase += 1

    for nome, funcao in MORTES:
        f1 = _referencia_mutada()
        b, e, c = funcao(copy.deepcopy(banco), copy.deepcopy(esquema),
                         copy.deepcopy(constantes))
        decidiu, falhas = _rodar(portao, gerador, f1, b, e, c)
        resultados.append((nome, "morre", decidiu, falhas, None))

    erradas = []
    for nome, espera, decidiu, falhas, frase in resultados:
        marca = "ok " if decidiu == espera else "NAO"
        if decidiu != espera:
            erradas.append((nome, espera, decidiu, falhas))
        elif frase is not None and not any(frase in f for f in falhas):
            marca = "NAO"
            erradas.append((nome + " (reprovou, mas nao pela frase %r)" % frase,
                            espera, decidiu, falhas))
        print("  %s  %-58s espera %-8s deu %s" % (marca, nome[:58], espera, decidiu))

    print("\n%d mutacoes: %d mundos que tem de PASSAR, %d quebras que tem de REPROVAR "
          "e %d mortes que tem de MATAR a referencia."
          % (len(resultados), len(MUNDOS),
             len(QUEBRAS_DE_REFERENCIA) + len(QUEBRAS_DE_BANCO), len(MORTES)))
    print("%d delas declaram a FRASE que esperam ouvir de volta, e foram cobradas por ela."
          % com_frase)

    if erradas:
        print("\n%d DECIDIRAM ERRADO:" % len(erradas))
        for nome, espera, decidiu, falhas in erradas:
            print("  - %s: esperava %s, deu %s" % (nome, espera, decidiu))
            for f in falhas[:3]:
                print("      %s" % f)
        sys.exit(1)
    print("Todas decidiram certo, nos TRES lados da fronteira.")


if __name__ == "__main__":
    main()
