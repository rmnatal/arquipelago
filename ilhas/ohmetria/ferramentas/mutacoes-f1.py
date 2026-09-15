#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BATERIA DE MUTACOES DA F1 -- a prova de que ferramentas/teste-f1.py PODE falhar.

    python3 ferramentas/mutacoes-f1.py

Bancada verde nao mede nada enquanto ninguem provar que ela reprova. Cada linha
abaixo quebra a F1 de um jeito diferente e diz o que espera ouvir de volta.

AS DUAS METADES, e a primeira e a que quase sempre falta:

  MUNDOS QUE TEM DE PASSAR. Secao 8 do ARQUIPELAGO.md: "todo caso que o ESQUEMA
  permite e o banco ainda nao tem e um caso que a regua precisa tratar HOJE, nao
  no dia em que aparecer -- e a maneira de provar que ela o trata e a mutacao que
  PRODUZ o mundo". O banco de modulos desta ilha tem ZERO registros, entao quase
  toda afirmacao da bancada sobre prestacao de contas hoje passa sobre uma lista
  vazia. Aqui ela e medida com 1, com 2 e com um modulo que estabiliza em TODAS as
  impedancias do vocabulario -- que e o mundo em que a proibicao de frase de
  mercado deixa de valer sozinha.

  QUEBRAS QUE TEM DE REPROVAR, e cada uma declara a FRASE que espera ouvir.
  "Reprovou" nao e a mesma coisa que "reprovou pelo motivo certo": uma quebra pode
  disparar OUTRA trava e voltar verde sem nunca ter medido a sua. Quebra cuja
  frase esperada nao aparece na lista de falhas e erro DESTA bateria, e ela
  reprova por isso.

OS REGISTROS DE BANCADA SAO FICCAO e moram aqui dentro, nunca em dados/. Registro
inventado num arquivo de banco seria a ilha fabricando produto -- e produto
fabricado nao se distingue de produto colhido depois de um commit.
"""

import copy
import importlib.util
import io
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(AQUI)
DADOS = os.path.join(BASE, "dados")


def _modulo(nome, arquivo):
    spec = importlib.util.spec_from_file_location(nome, os.path.join(AQUI, arquivo))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _ler(nome):
    return json.load(io.open(os.path.join(DADOS, nome), encoding="utf-8"))


# ---------------------------------------------------------------------------
# FICCAO DE BANCADA. Nao sao produtos: sao mundos.
# ---------------------------------------------------------------------------

def _ficticio(id_, marca, modelo, estaveis, rms):
    return {
        "id": id_,
        "marca": marca,
        "modelo": modelo,
        "canais": 1,
        "impedancias_estaveis": list(estaveis),
        "impedancias_estaveis_declarada_por": "no_titulo_ou_na_prosa_do_fabricante",
        "rms_por_impedancia": dict(rms),
        "potencia": {
            "unidade_declarada": "rms",
            "unidade_declarada_por": "na_tabela_de_potencia_por_impedancia",
        },
        "fonte": {"tipo": "ficcao_de_bancada", "url": None, "data_leitura": None},
        "afiliado": {"programa": "shopee", "degrau": 4},
        "publicavel": False,
        "motivo_nao_publicavel": "FICCAO DE BANCADA: este registro nunca existiu.",
    }


UM_MODULO = [
    _ficticio("ficcao-um", "Marca Fictícia", "Um", ["1", "2", "4"],
              {"1": 1200, "2": 700, "4": 400}),
]

DOIS_MODULOS = UM_MODULO + [
    _ficticio("ficcao-dois", "Marca Fictícia", "Dois", ["2", "4"],
              {"2": 600, "4": 350}),
]

MODULO_EM_TODAS = [
    _ficticio("ficcao-todas", "Marca Fictícia", "Todas", ["0,5", "1", "2", "4", "8"],
              {"0,5": 2000, "1": 1500, "2": 900, "4": 500, "8": 260}),
]


# ---------------------------------------------------------------------------
# AS QUEBRAS. Cada uma recebe o documento montado e o devolve estragado.
# ---------------------------------------------------------------------------

def _estado(doc, bobina, n, pedido):
    for r in doc["respostas"]:
        e = r["entrada"]
        if (e["bobina"], e["alto_falantes"], e["impedancia_do_modulo_pedida"]) == (bobina, n, pedido):
            return r
    raise AssertionError("estado ausente na bateria: %s x %s pedindo %s" % (bobina, n, pedido))


def q_distancia_absoluta(doc, mundo):
    """O criterio da ilha trocado por menor distancia em ohms -- a resposta que
    QUEIMA o modulo. Foi assim que a primeira versao do gerador respondeu 0,5 ohm
    para o par 2+2 pedindo 1 ohm."""
    r = _estado(doc, "2+2 ohms", 2, "1")
    r["veredito"]["frase"] = r["veredito"]["frase"].replace("2 ohms", "0,5 ohm")
    r["compra"]["pisos"] = [dict(p, para_a_impedancia="0,5") for p in r["compra"]["pisos"]]
    return doc, mundo


def q_abaixo_do_minimo_oferecido(doc, mundo):
    """O valor abaixo do minimo do modulo servido como se fosse resposta, sem o
    aviso de que abaixo do minimo e o que queima."""
    r = _estado(doc, "1 ohm", 4, "8")
    r["veredito"]["frase"] = ("Não fecha em 8 ohms. O mais perto que fecha é 4 ohms, com "
                              "todas as 4 bobinas em paralelo.")
    return doc, mundo


def q_piso_em_montagem_que_nao_fecha(doc, mundo):
    """Bloco de compra oferecido a quem nao tem montagem valida: e vender uma coisa
    no lugar de outra."""
    r = _estado(doc, "2+2 ohms", 3, "1")
    r["compra"]["pisos"] = [{
        "programa": "shopee", "para_a_impedancia": "1",
        "palavra_chave_busca": "modulo amplificador 1 ohm",
        "url_busca_produto": "https://shopee.com.br/search?keyword=modulo+amplificador+1+ohm",
        "url_busca": None, "rastreavel": False, "rel": "nofollow noopener", "degrau": 4,
    }]
    return doc, mundo


def q_url_de_piso_digitada(doc, mundo):
    """URL de piso escrita a mao em vez de fabricada do molde do esquema: ela
    envelhece calada no dia em que o molde mudar."""
    r = _estado(doc, "2+2 ohms", 2, "0,5")
    r["compra"]["pisos"][0]["url_busca_produto"] = "https://shopee.com.br/search?keyword=modulo"
    return doc, mundo


def q_prestacao_digitada(doc, mundo):
    """Numero de tela digitado em vez de contado, com o banco tendo um modulo."""
    r = _estado(doc, "2+2 ohms", 2, "1")
    r["prestacao_de_contas"]["modulos_no_banco"] = 0
    return doc, mundo


def q_modulo_nao_nomeado(doc, mundo):
    """Modulo do banco que some da resposta: a soma dos nomeados deixa de fechar."""
    r = _estado(doc, "2+2 ohms", 2, "2")
    p = r["prestacao_de_contas"]
    if p["fora"]:
        p["fora"].pop()
    else:
        p["dentro"].pop()
    return doc, mundo


def q_frase_de_mercado(doc, mundo):
    """A frase que o bloco 3 tirou de circulacao, de volta: afirmacao sobre o
    MERCADO sustentada por uma lista que nenhum registro de banco lastreia."""
    r = _estado(doc, "1+1 ohms", 4, None)
    r["ligacoes"][0]["frase_do_banco"] = "Não existe módulo para 0,125 ohm."
    return doc, mundo


def q_teto_de_rms_afirmado(doc, mundo):
    """Constante pendente entrando em formula publicada."""
    for r in doc["respostas"]:
        r["potencia"]["frase"] = ("O seu falante é 200 W RMS, então o módulo pode ter até "
                                  "200 W RMS nessa impedância.")
        r["potencia"]["rms_do_falante"] = 200
    return doc, mundo


def q_voz_proibida_no_veredito(doc, mundo):
    r = _estado(doc, "2 ohms", 2, None)
    r["veredito"]["frase"] = ("Esta calculadora aplica o critério de associação de impedâncias "
                              "em paralelo.")
    return doc, mundo


def q_tela_sem_acento(doc, mundo):
    """O banco e ASCII e a tela nao: uma ligacao que volta sem acento."""
    r = _estado(doc, "2+2 ohms", 2, None)
    r["ligacoes"][1]["ligacao"] = r["ligacoes"][1]["ligacao"].replace("série", "serie")
    return doc, mundo


def q_tabela_com_uma_linha_a_menos(doc, mundo):
    """A metade que um modelo de linguagem le sem preencher formulario, encolhida."""
    doc["tabela_de_exemplos"].pop()
    return doc, mundo


def q_tabela_com_linha_errada(doc, mundo):
    """Linha da tabela pre-renderizada que discorda da propria conta -- foi ali que
    a F2 do Clube do Mosaico falhou em tres de nove linhas."""
    doc["tabela_de_exemplos"][0]["fecha_em"] = ["0,5"]
    return doc, mundo


def q_ligacao_sem_texto(doc, mundo):
    """Impedancia servida sem dizer COMO ligar: o numero sem o caminho e o que a
    SERP ja publica."""
    r = _estado(doc, "4+4 ohms", 2, None)
    r["ligacoes"][0]["ligacao"] = "   "
    return doc, mundo


def q_nota_de_tres_apagada(doc, mundo):
    """O veredito que nenhuma pagina medida publica, apagado da tela."""
    _estado(doc, "2+2 ohms", 3, None)["nota_da_quantidade"] = None
    return doc, mundo


def q_nota_de_tres_espalhada(doc, mundo):
    """A mesma nota afirmada onde ela e falsa."""
    _estado(doc, "2+2 ohms", 2, None)["nota_da_quantidade"] = (
        "2 alto-falantes iguais não fecham em impedância de módulo nenhuma.")
    return doc, mundo


def q_recusa_removida(doc, mundo):
    """Recusa declarada que some: a F1 volta a omitir em vez de dizer."""
    r = _estado(doc, "2 ohms", 1, "2")
    r["recusas"] = [x for x in r["recusas"] if x["id"] != "ligacao-assimetrica"]
    return doc, mundo


def q_constante_pendente_como_prova(doc, mundo):
    """Constante pendente publicada na linha 'como sabemos'."""
    for r in doc["respostas"]:
        r["como_sabemos"].append({
            "id": "criterio-rms-modulo-nao-passa-do-falante",
            "descricao": "teto de RMS", "fonte": "Taramps", "url": None,
            "verificado_em": "2026-09-14", "status": "pendente",
        })
    return doc, mundo


def q_desacordo_da_serp_removido(doc, mundo):
    """O desacordo que faz a pagina valer, retirado da prova."""
    for r in doc["respostas"]:
        r["como_sabemos"] = [c for c in r["como_sabemos"]
                             if c["id"] != "desacordo-multiplicador-rms-serp"]
    return doc, mundo


def q_aritmetica_alterada(doc, mundo):
    """Uma impedancia alcancavel trocada: a regua propria tem de discordar."""
    r = _estado(doc, "2+2 ohms", 2, None)
    r["ligacoes"][0]["ohms"] = "0,6"
    return doc, mundo


def q_total_digitado(doc, mundo):
    doc["total_de_estados"] = 144000
    return doc, mundo


def q_montagens_digitado(doc, mundo):
    doc["montagens"] = 99
    return doc, mundo


def q_estado_faltando(doc, mundo):
    """Um estado que some do dominio: a F1 deixa de responder uma consulta inteira."""
    r = _estado(doc, "4 ohms", 3, "8")
    doc["respostas"].remove(r)
    doc["total_de_estados"] = len(doc["respostas"])
    return doc, mundo


def q_piso_com_sponsored(doc, mundo):
    """Busca crua carimbada de patrocinada: declara ao leitor uma relacao paga que
    nao existe."""
    r = _estado(doc, "2+2 ohms", 2, "0,5")
    r["compra"]["pisos"][0]["rel"] = "sponsored noopener"
    return doc, mundo


def q_bloco_vazio_sem_motivo(doc, mundo):
    """Bloco de compra vazio e mudo: silencio parece defeito (secao 7)."""
    r = _estado(doc, "2+2 ohms", 3, "1")
    r["compra"]["frase"] = "Sem produtos."
    return doc, mundo


def q_contraexemplo_quebrado(doc, mundo):
    """O contraexemplo que impede a afirmacao de virar 'impar nunca fecha'."""
    _estado(doc, "2 ohms", 1, "2")["veredito"]["codigo"] = "NAO_FECHA_NENHUM"
    return doc, mundo


def q_marcacao_de_vocabulario_invertida(doc, mundo):
    r = _estado(doc, "1+1 ohms", 4, None)
    r["ligacoes"][0]["e_impedancia_de_modulo"] = True
    return doc, mundo


def q_escolha_oferecida_onde_nao_ha(doc, mundo):
    """Falante unico de bobina simples tem UMA ligacao. Oferecer escolha ali e
    devolver a pergunta com cara de resposta."""
    r = _estado(doc, "2 ohms", 1, None)
    r["veredito"]["frase"] = ("Essa montagem alcança 2 ohms, e qual deles você usa depende "
                              "de como liga a bobina.")
    return doc, mundo


def q_modulo_do_banco_ignorado_na_ligacao(doc, mundo):
    """Com modulo no banco, a linha da ligacao continua dizendo que nao ha nenhum."""
    r = _estado(doc, "2+2 ohms", 2, None)
    for l in r["ligacoes"]:
        l["modulos_do_banco"] = []
    return doc, mundo


# ---------------------------------------------------------------------------
# A BATERIA. (nome, mundo, quebra ou None, o que se espera ouvir)
# ---------------------------------------------------------------------------

MUNDOS = {
    "banco vazio (o mundo de hoje)": [],
    "banco com UM modulo": UM_MODULO,
    "banco com DOIS modulos": DOIS_MODULOS,
    "banco com um modulo em TODAS as impedancias": MODULO_EM_TODAS,
}

BATERIA = [
    # --- os quatro mundos que tem de PASSAR ---------------------------------
    ("MUNDO banco vazio, intacto", "banco vazio (o mundo de hoje)", None, "passa"),
    ("MUNDO um modulo, intacto", "banco com UM modulo", None, "passa"),
    ("MUNDO dois modulos, intacto", "banco com DOIS modulos", None, "passa"),
    ("MUNDO modulo em todas as impedancias, intacto",
     "banco com um modulo em TODAS as impedancias", None, "passa"),

    # --- as quebras, cada uma com a frase que espera ouvir ------------------
    ("criterio virado em distancia absoluta", "banco vazio (o mundo de hoje)",
     q_distancia_absoluta, "a saida segura e"),
    ("abaixo do minimo oferecido como resposta", "banco vazio (o mundo de hoje)",
     q_abaixo_do_minimo_oferecido, "queima o modulo e a frase nao avisa"),
    ("piso de compra em montagem que nao fecha", "banco vazio (o mundo de hoje)",
     q_piso_em_montagem_que_nao_fecha, "o piso tem de cobrir"),
    ("URL de piso digitada", "banco vazio (o mundo de hoje)",
     q_url_de_piso_digitada, "URL de piso digitada e nao fabricada do molde"),
    ("prestacao de contas digitada", "banco com UM modulo",
     q_prestacao_digitada, "modulos no banco e o banco carregado tem"),
    ("modulo do banco nao nomeado", "banco com DOIS modulos",
     q_modulo_nao_nomeado, "a soma dos nomeados"),
    ("frase sobre o MERCADO", "banco vazio (o mundo de hoje)",
     q_frase_de_mercado, "afirmacao sobre o MERCADO"),
    ("teto de RMS afirmado com constante pendente", "banco vazio (o mundo de hoje)",
     q_teto_de_rms_afirmado, "teto de RMS afirmado"),
    ("expressao proibida pelo VOZ.md no veredito", "banco vazio (o mundo de hoje)",
     q_voz_proibida_no_veredito, "que o VOZ.md proibe"),
    ("texto de tela sem acento", "banco vazio (o mundo de hoje)",
     q_tela_sem_acento, "texto de tela sem acento"),
    ("tabela pre-renderizada com uma linha a menos", "banco vazio (o mundo de hoje)",
     q_tabela_com_uma_linha_a_menos, "uma linha por montagem"),
    ("linha da tabela discordando da conta", "banco vazio (o mundo de hoje)",
     q_tabela_com_linha_errada, "diz que fecha em"),
    ("impedancia servida sem a ligacao", "banco vazio (o mundo de hoje)",
     q_ligacao_sem_texto, "sem dizer como ligar"),
    ("a nota dos tres falantes apagada", "banco vazio (o mundo de hoje)",
     q_nota_de_tres_apagada, "a nota de quantidade apareceu"),
    ("a nota dos tres falantes afirmada onde e falsa", "banco vazio (o mundo de hoje)",
     q_nota_de_tres_espalhada, "a nota de quantidade apareceu"),
    ("recusa declarada removida", "banco vazio (o mundo de hoje)",
     q_recusa_removida, "recusa declarada faltando"),
    ("constante pendente publicada como prova", "banco vazio (o mundo de hoje)",
     q_constante_pendente_como_prova, "constante pendente publicada como prova"),
    ("desacordo da SERP retirado do 'como sabemos'", "banco vazio (o mundo de hoje)",
     q_desacordo_da_serp_removido, "'como sabemos' traz"),
    ("aritmetica de associacao alterada", "banco vazio (o mundo de hoje)",
     q_aritmetica_alterada, "a regua propria calcula"),
    ("total_de_estados digitado", "banco vazio (o mundo de hoje)",
     q_total_digitado, "total_de_estados esta digitado"),
    ("montagens digitado", "banco vazio (o mundo de hoje)",
     q_montagens_digitado, "o campo montagens esta digitado"),
    ("estado que some do dominio", "banco vazio (o mundo de hoje)",
     q_estado_faltando, "estados ausentes do dominio"),
    ("busca crua carimbada de patrocinada", "banco vazio (o mundo de hoje)",
     q_piso_com_sponsored, "rel=sponsored"),
    ("bloco de compra vazio e mudo", "banco vazio (o mundo de hoje)",
     q_bloco_vazio_sem_motivo, "sem dizer POR QUE"),
    ("o contraexemplo do falante unico quebrado", "banco vazio (o mundo de hoje)",
     q_contraexemplo_quebrado, "tem de FECHAR"),
    ("marcacao de impedancia de modulo invertida", "banco vazio (o mundo de hoje)",
     q_marcacao_de_vocabulario_invertida, "discorda do vocabulario do esquema"),
    ("escolha oferecida onde so ha uma ligacao", "banco vazio (o mundo de hoje)",
     q_escolha_oferecida_onde_nao_ha, "a frase oferece escolha"),
    ("modulo do banco ignorado na linha da ligacao", "banco com UM modulo",
     q_modulo_do_banco_ignorado_na_ligacao, "estabilizando ai e a linha traz"),
]


# ---------------------------------------------------------------------------
# AS QUEBRAS QUE NAO SAO DO DOCUMENTO E SIM DO MUNDO: quando uma chave some da
# FONTE, a referencia tem de MORRER em vez de cair num literal (secao 26.2). Isto
# nao se mede rodando a bancada -- se mede tentando gerar e exigindo o tombo, com
# a frase certa.
# ---------------------------------------------------------------------------

def _sem_chave(dicionario, *caminho):
    d = copy.deepcopy(dicionario)
    alvo = d
    for passo in caminho[:-1]:
        alvo = alvo[passo]
    alvo.pop(caminho[-1], None)
    return d


def _sem_uma_bobina(casos):
    d = copy.deepcopy(casos)
    d["casos"] = [c for c in d["casos"] if c["bobina"] != "4+4 ohms"]
    return d


MORTES = [
    ("esquema sem o vocabulario impedancia_de_modulo",
     lambda e: _sem_chave(e, "vocabularios", "impedancia_de_modulo"), None,
     "nao tem o vocabulario impedancia_de_modulo"),
    ("esquema sem o vocabulario impedancia_de_bobina",
     lambda e: _sem_chave(e, "vocabularios", "impedancia_de_bobina"), None,
     "nao tem o vocabulario impedancia_de_bobina"),
    ("esquema sem o molde do piso de compra",
     lambda e: _sem_chave(e, "piso_de_compra", "moldes"), None,
     "molde de piso de compra"),
    # O outro sentido da mesma trava: o esquema intacto e o banco de casos velho.
    # E o caso que acontece de verdade -- alguem acrescenta bobina ao vocabulario e
    # esquece de rodar ferramentas/impedancias.py.
    ("banco de casos com uma bobina a menos que o esquema",
     None, _sem_uma_bobina,
     "o banco de casos responde pelas bobinas"),
]


def main():
    gerar = _modulo("gerar_f1", "gerar-f1.py")
    teste = _modulo("teste_f1", "teste-f1.py")
    f1 = gerar._referencia()

    esquema = _ler("esquema-banco.json")
    doc_casos = _ler("impedancias-alcancaveis.json")
    constantes = _ler("constantes.json")

    base = {}
    for nome, banco in MUNDOS.items():
        base[nome] = gerar.documento(f1, banco=banco, esquema=esquema,
                                     doc_casos=doc_casos, constantes=constantes)

    certas, erradas = 0, []
    for nome, mundo, quebra, espera in BATERIA:
        doc = copy.deepcopy(base[mundo])
        banco = copy.deepcopy(MUNDOS[mundo])
        if quebra is not None:
            doc, banco = quebra(doc, banco)
        _, falhas = teste.conferir(doc, banco, esquema, doc_casos, constantes)

        if espera == "passa":
            if falhas:
                erradas.append("%s: era para PASSAR e reprovou -- %s" % (nome, falhas[0]))
            else:
                certas += 1
        else:
            if not falhas:
                erradas.append("%s: era para REPROVAR e passou" % nome)
            elif not any(espera in f for f in falhas):
                erradas.append(
                    "%s: reprovou, mas NAO pelo motivo esperado (%r). Primeira falha: %s"
                    % (nome, espera, falhas[0]))
            else:
                certas += 1

    # As mortes: chave que some da FONTE nao pode virar literal silencioso.
    for nome, estraga_esquema, estraga_casos, espera in MORTES:
        try:
            gerar.documento(
                f1, banco=[],
                esquema=estraga_esquema(esquema) if estraga_esquema else esquema,
                doc_casos=estraga_casos(doc_casos) if estraga_casos else doc_casos,
                constantes=constantes)
        except SystemExit as erro:
            if espera in str(erro):
                certas += 1
            else:
                erradas.append("%s: morreu, mas dizendo outra coisa -- %s" % (nome, erro))
        except Exception as erro:  # noqa: BLE001 -- qualquer outro tombo e tombo errado
            erradas.append("%s: morreu por %s, e nao pela chave que sumiu"
                           % (nome, type(erro).__name__))
        else:
            erradas.append("%s: a referencia NAO morreu -- caiu num literal em silencio" % nome)

    # A PROSA TAMBEM E MEDIDA: a secao 7 da especificacao publica a distribuicao dos
    # vereditos e a conta do piso, e numero em prosa envelhece calado. Aqui os dois
    # numeros sao estragados de proposito no texto -- sem tocar no arquivo -- e a
    # bancada tem de acusar.
    espec = io.open(os.path.join(DADOS, "especificacao-calculadoras.md"),
                    encoding="utf-8").read()
    doc_limpo = base["banco vazio (o mundo de hoje)"]
    for nome, estragada, espera in [
        ("a especificacao publica outra contagem de veredito",
         espec.replace("FECHA 37 ·", "FECHA 99 ·"), "e a varredura conta"),
        ("a especificacao publica outra conta de piso",
         espec.replace("São **53** estados", "São **47** estados"), "sem piso e"),
        ("a linha de contagem sumiu da especificacao",
         espec.replace("**FECHA 37 ·", "**"), "nao publica mais a contagem"),
    ]:
        _, falhas = teste.conferir(doc_limpo, [], esquema, doc_casos, constantes, estragada)
        if not falhas:
            erradas.append("%s: era para REPROVAR e passou" % nome)
        elif not any(espera in f for f in falhas):
            erradas.append("%s: reprovou por outro motivo -- %s" % (nome, falhas[0]))
        else:
            certas += 1
    # E o mundo intacto, com a prosa de verdade, tem de passar.
    _, falhas = teste.conferir(doc_limpo, [], esquema, doc_casos, constantes, espec)
    if falhas:
        erradas.append("a especificacao de verdade nao bate com a varredura: %s" % falhas[0])
    else:
        certas += 1

    # A CONFERENCIA DA PROPRIA BATERIA: quebra sem frase esperada e mutacao inerte
    # esperando para acontecer.
    for nome, _, quebra, espera in BATERIA:
        if quebra is not None and (not espera or espera == "passa"):
            erradas.append("%s: quebra sem frase esperada declarada" % nome)

    # E A PROVA DE QUE A CONFERENCIA ACIMA MORDE. "Reprovou" nao e "reprovou pelo
    # motivo certo", e essa distincao so vale se ela mesma for medida: aqui uma
    # quebra real recebe a frase esperada de OUTRA trava real, e esta bateria tem de
    # acusar. Sem isto, o campo espera seria decoracao.
    if "--sem-autoteste" not in sys.argv:
        doc = copy.deepcopy(base["banco vazio (o mundo de hoje)"])
        doc, _ = q_tela_sem_acento(doc, [])
        _, falhas = teste.conferir(doc, [], esquema, doc_casos, constantes)
        frase_de_outra_trava = "URL de piso digitada e nao fabricada do molde"
        if any(frase_de_outra_trava in f for f in falhas) or not falhas:
            erradas.append("o autoteste da bateria nao consegue distinguir uma trava da outra")
        else:
            certas += 1

    for e in erradas:
        print("ERRO: %s" % e)
    print("%d de %d mutacoes decidiram certo, autoteste da bateria incluido"
          % (certas, len(BATERIA) + len(MORTES) + 5))
    return 1 if erradas else 0


if __name__ == "__main__":
    sys.exit(main())
