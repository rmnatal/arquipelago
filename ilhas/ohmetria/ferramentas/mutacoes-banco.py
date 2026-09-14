#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prova que ferramentas/validar-banco.py PODE falhar, e nos dois lados da fronteira.

Roda a partir de ilhas/ohmetria/:

    python3 ferramentas/mutacoes-banco.py

POR QUE ELE E OBRIGATORIO NESTE BLOCO, E NAO NO PROXIMO.
O banco desta ilha nasceu com ZERO registros, por egresso fechado. Um validador que
so tenha visto um banco vazio esta verde por AUSENCIA, nao por medicao -- e a secao 8
do ARQUIPELAGO.md tem cicatriz com nome para isso: regua escrita para um mundo que
nunca aconteceu nasce errada sem poder falhar, e passa por tres blocos sem que ninguem
veja. A saida escrita la e esta: todo caso que o ESQUEMA permite e o banco ainda nao
tem e um caso que a regua precisa tratar HOJE, e a maneira de provar que ela o trata e
a mutacao que PRODUZ o mundo, criando o caso em vez de esperar por ele.

Por isso este arquivo tem DOIS tipos de mutacao, e os dois contam:

  - MUNDOS QUE TEM DE PASSAR. Um modulo correto e um alto-falante correto, montados
    aqui, que o banco de hoje nao tem. Se o validador reprovasse um registro valido,
    a carga do bloco 3c bateria de frente com a propria regua -- e descobriria isso
    depois de colher, nao antes.
  - QUEBRAS QUE TEM DE REPROVAR. Cada linha de
    esquema-banco.json -> o_que_o_esquema_permite_e_o_banco_ainda_nao_tem, escrita de
    volta como defeito.

OS REGISTROS DESTE ARQUIVO SAO FICCAO DE BANCADA, e e por isso que eles moram aqui e
nao em dados/. A marca 'Bancada' nao existe, o manual citado nao existe, e nada daqui
pode ser publicado nem contado como item do banco. Fixture no arquivo de dados seria a
ilha inventando produto, que e a unica coisa que ela nunca pode fazer.
"""

import copy
import json
import io
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

validador = __import__("validar-banco")

RAIZ = os.path.dirname(AQUI)
ESQUEMA = json.load(io.open(os.path.join(RAIZ, "dados", "esquema-banco.json"), encoding="utf-8"))
CONSTANTES = json.load(io.open(os.path.join(RAIZ, "dados", "constantes.json"), encoding="utf-8"))
CASOS_F1 = json.load(io.open(os.path.join(RAIZ, "dados", "impedancias-alcancaveis.json"), encoding="utf-8"))


# ----------------------------------------------------------------------------
# os dois registros corretos que o banco ainda nao tem
# ----------------------------------------------------------------------------

FONTE_FORTE = {
    "tipo": "manual_do_fabricante",
    "url": "https://exemplo-de-bancada.invalido/manual-mf-1000.pdf",
    "titulo_ou_codigo": "MN_BANCADA_R00_MF-1000",
    "leitura": "documento_aberto",
    "data_leitura": "2026-09-14",
    "nivel": 1,
}

MODULO_OK = {
    "id": "bancada-mf-1000-1",
    "marca": "Bancada",
    "modelo": "MF 1000.1",
    "canais": 1,
    "impedancias_estaveis": ["1", "2", "4"],
    "impedancias_estaveis_declarada_por": "na_tabela_de_potencia_por_impedancia",
    "rms_por_impedancia": {"1": 1000, "2": 600, "4": 350},
    "potencia": {
        "unidade_declarada": "rms",
        "unidade_declarada_por": "no_titulo_ou_na_prosa_do_fabricante",
    },
    "tensao_alimentacao_v": 14.4,
    "fonte": copy.deepcopy(FONTE_FORTE),
    "afiliado": {
        "programa": "shopee",
        "palavra_chave_busca": "modulo amplificador bancada mf 1000",
        "url_busca_produto": "https://shopee.com.br/search?keyword=modulo%20amplificador%20bancada%20mf%201000",
        "degrau": 4,
        "intestavel": False,
    },
    "publicavel": True,
}

FALANTE_OK = {
    "id": "bancada-bf-12",
    "marca": "Bancada",
    "modelo": "BF 12",
    "polegadas": 12,
    "impedancia_bobinas": "2+2",
    "bobinas": 2,
    "ohms_por_bobina": 2.0,
    "potencia": {
        "rms_w": 500,
        "unidade_declarada": "rms",
        "unidade_declarada_por": "no_titulo_ou_na_prosa_do_fabricante",
    },
    "thiele_small": {"fs_hz": 37.0, "vas_l": 31.5, "qts": 0.5},
    "fonte": copy.deepcopy(FONTE_FORTE),
    "afiliado": {
        "programa": "shopee",
        "palavra_chave_busca": "subwoofer bancada bf 12",
        "url_busca_produto": "https://shopee.com.br/search?keyword=subwoofer%20bancada%20bf%2012",
        "degrau": 4,
        "intestavel": False,
    },
    "publicavel": True,
}


def bancos_com(modulos=None, falantes=None):
    """Monta os dois arquivos de banco em memoria, com o cabecalho que o esquema cobra."""
    def envelope(entidade, itens):
        return {
            "ilha": "ohmetria",
            "bloco": "3",
            "entidade": entidade,
            "publicar": False,
            "motivo_de_estar_vazio": "bancada",
            "itens": itens,
        }
    return {
        "dados/modulos.json": envelope("MODULO", copy.deepcopy(modulos) if modulos else []),
        "dados/alto-falantes.json": envelope("ALTO_FALANTE", copy.deepcopy(falantes) if falantes else []),
    }


# ----------------------------------------------------------------------------
# as mutacoes: (nome, o que muda, o que tem de acontecer)
#   'passa'   = mundo legitimo que o banco ainda nao tem
#   'reprova' = defeito escrito de volta
# ----------------------------------------------------------------------------

def muda_modulo(f):
    def aplicar(esquema, bancos, constantes):
        f(bancos["dados/modulos.json"]["itens"][0])
    return aplicar


def muda_falante(f):
    def aplicar(esquema, bancos, constantes):
        f(bancos["dados/alto-falantes.json"]["itens"][0])
    return aplicar


def muda_esquema(f):
    def aplicar(esquema, bancos, constantes):
        f(esquema)
    return aplicar


def muda_constantes(f):
    def aplicar(esquema, bancos, constantes):
        f(constantes)
    return aplicar


def _apaga_constante(constantes):
    constantes["constantes"] = [c for c in constantes["constantes"]
                                if c.get("id") != "faixa-de-validacao-thiele-small"]


MUTACOES = [
    # ---------------- mundos que tem de PASSAR ----------------
    ("mundo: o banco vazio de hoje, sem afirmar nada sobre o mercado",
     lambda e, b, c: b.clear() or b.update(bancos_com()), "passa"),

    ("mundo: um modulo e um alto-falante corretos, que o banco nao tem",
     lambda e, b, c: None, "passa"),

    ("mundo: modulo com unidade musical, no banco e NAO publicavel, com motivo",
     muda_modulo(lambda m: (m["potencia"].__setitem__("unidade_declarada", "musical"),
                            m.__setitem__("publicavel", False),
                            m.__setitem__("motivo_nao_publicavel",
                                          "o fabricante so publica potencia musical; a ilha so publica RMS"))),
     "passa"),

    ("mundo: manual do fabricante lido por BUSCA, no banco e NAO publicavel",
     muda_modulo(lambda m: (m["fonte"].__setitem__("leitura", "busca_web"),
                            m.__setitem__("publicavel", False),
                            m.__setitem__("motivo_nao_publicavel",
                                          "elo mais fraco: o documento e nivel 1 e a leitura foi busca"))),
     "passa"),

    ("mundo: ficha de afiliado completa, com url e url_produto, no degrau 2",
     muda_modulo(lambda m: (m["afiliado"].__setitem__("degrau", 2),
                            m["afiliado"].__setitem__("url", "https://s.shopee.com.br/bancada"),
                            m["afiliado"].__setitem__("url_produto",
                                                      "https://shopee.com.br/produto-de-bancada-i.1.1"))),
     "passa"),

    ("mundo: alto-falante sem Thiele-Small serve a F1 e nao serve a F2",
     muda_falante(lambda a: a.pop("thiele_small")), "passa"),

    # ---------------- quebras que tem de REPROVAR ----------------
    ("modulo estabiliza em 16 ohm, fora do vocabulario: o ESQUEMA reprova, o modulo nao some",
     muda_modulo(lambda m: (m["impedancias_estaveis"].append("16"),
                            m["rms_por_impedancia"].__setitem__("16", 120))), "reprova"),

    ("rms_por_impedancia CRESCE quando a impedancia sobe: monotonia quebrada",
     muda_modulo(lambda m: m["rms_por_impedancia"].__setitem__("4", 1800)), "reprova"),

    ("impedancias_estaveis tem uma impedancia que a tabela de rms nao tem",
     muda_modulo(lambda m: m["impedancias_estaveis"].append("8")), "reprova"),

    ("a tabela de rms tem uma impedancia que impedancias_estaveis nao tem",
     muda_modulo(lambda m: m["rms_por_impedancia"].__setitem__("0,5", 1400)), "reprova"),

    ("modulo publicavel com unidade musical: a ilha so publica RMS",
     muda_modulo(lambda m: m["potencia"].__setitem__("unidade_declarada", "musical")), "reprova"),

    ("modulo publicavel com manual lido por BUSCA: o elo mais fraco e a leitura",
     muda_modulo(lambda m: m["fonte"].__setitem__("leitura", "busca_web")), "reprova"),

    ("modulo publicavel com ficha de LOJA, que e nivel 3",
     muda_modulo(lambda m: (m["fonte"].__setitem__("tipo", "catalogo_de_loja"),
                            m["fonte"].__setitem__("nivel", 3))), "reprova"),

    ("fonte.nivel DIGITADO diferente do que a escada diz para o tipo",
     muda_modulo(lambda m: m["fonte"].__setitem__("nivel", 3)), "reprova"),

    ("publicavel false sem motivo_nao_publicavel: silencio nao e causa",
     muda_modulo(lambda m: m.__setitem__("publicavel", False)), "reprova"),

    ("impedancias_estaveis sem declarar de onde a lista foi lida (secao 26)",
     muda_modulo(lambda m: m.pop("impedancias_estaveis_declarada_por")), "reprova"),

    ("unidade_declarada_por com uma origem inventada, fora das tres legitimas",
     muda_modulo(lambda m: m["potencia"].__setitem__("unidade_declarada_por", "estava_na_cara")), "reprova"),

    ("modulo sem rms_por_impedancia: um RMS solto e o defeito que a ilha corrige",
     muda_modulo(lambda m: m.pop("rms_por_impedancia")), "reprova"),

    ("item sem url_busca_produto: nao existe item publicavel sem piso (25.2)",
     muda_modulo(lambda m: m["afiliado"].pop("url_busca_produto")), "reprova"),

    ("url_busca_produto DIGITADA a mao, diferente da fabricada pelo molde",
     muda_modulo(lambda m: m["afiliado"].__setitem__(
         "url_busca_produto", "https://shopee.com.br/search?keyword=modulo+bancada")), "reprova"),

    ("item com url de afiliado e sem url_produto: o teste de vida fica impossivel",
     muda_modulo(lambda m: (m["afiliado"].__setitem__("degrau", 2),
                            m["afiliado"].__setitem__("url", "https://s.shopee.com.br/bancada"),
                            m["afiliado"].__setitem__("intestavel", True))), "reprova"),

    ("afiliado.intestavel gravado ao contrario do derivado",
     muda_modulo(lambda m: (m["afiliado"].__setitem__("degrau", 2),
                            m["afiliado"].__setitem__("url", "https://s.shopee.com.br/bancada"),
                            m["afiliado"].__setitem__("url_produto", "https://shopee.com.br/x-i.1.1"),
                            m["afiliado"].__setitem__("intestavel", True))), "reprova"),

    ("id que nao e o slug de marca mais modelo",
     muda_modulo(lambda m: m.__setitem__("id", "mf1000")), "reprova"),

    ("Thiele-Small com Fs de 4 Hz, o erro de extracao que o PROMPT.md registra",
     muda_falante(lambda a: a["thiele_small"].__setitem__("fs_hz", 4.0)), "reprova"),

    ("Thiele-Small com Vas de 672,3 -- cm3 lido como litro, o outro erro registrado",
     muda_falante(lambda a: a["thiele_small"].__setitem__("vas_l", 672.3)), "reprova"),

    ("alto-falante 2+2 gravado com 1 bobina: a string e o derivado discordam",
     muda_falante(lambda a: a.__setitem__("bobinas", 1)), "reprova"),

    ("alto-falante com ohms_por_bobina que a string nao sustenta",
     muda_falante(lambda a: a.__setitem__("ohms_por_bobina", 4.0)), "reprova"),

    ("alto-falante com bobina 3+3, fora do vocabulario",
     muda_falante(lambda a: (a.__setitem__("impedancia_bobinas", "3+3"),
                             a.__setitem__("ohms_por_bobina", 3.0))), "reprova"),

    ("bobina que o esquema aceita e o gerador da F1 NAO enumera: a F1 serviria pagina sem resposta",
     lambda e, b, c: (e["vocabularios"]["impedancia_de_bobina"]["valores"].append("8+8"),
                      b["dados/alto-falantes.json"]["itens"][0].update(
                          {"impedancia_bobinas": "8+8", "bobinas": 2, "ohms_por_bobina": 8.0})),
     "reprova"),

    ("a chave campos_que_exigem_declaracao_de_origem some do esquema (26.2)",
     muda_esquema(lambda e: e.pop("campos_que_exigem_declaracao_de_origem")), "reprova"),

    ("a lista de campos que exigem origem fica vazia, sem sumir a chave",
     muda_esquema(lambda e: e["campos_que_exigem_declaracao_de_origem"].__setitem__("campos", [])), "reprova"),

    ("a constante faixa-de-validacao-thiele-small some de constantes.json",
     muda_constantes(_apaga_constante), "reprova"),

    ("o vocabulario impedancia_de_modulo some do esquema",
     muda_esquema(lambda e: e["vocabularios"].pop("impedancia_de_modulo")), "reprova"),

    ("piso_de_compra.moldes some: o piso deixaria de ser derivado e viraria digitado",
     muda_esquema(lambda e: e["piso_de_compra"].pop("moldes")), "reprova"),

    ("escada_de_fontes.niveis some: o campo nivel ficaria sem com o que ser comparado",
     muda_esquema(lambda e: e["escada_de_fontes"].pop("niveis")), "reprova"),

    ("entidade CAIXA perde o motivo de nao ter banco: lacuna sem causa nomeada",
     muda_esquema(lambda e: e["entidades"]["CAIXA"].pop("motivo_de_nao_ter_banco_ainda")), "reprova"),

    ("o esquema declara um banco que nao existe na pasta",
     muda_esquema(lambda e: e["entidades"]["CAIXA"].__setitem__("arquivo_de_banco", "dados/caixas.json")),
     "reprova"),

    ("existe arquivo de banco que nenhuma entidade do esquema declara",
     lambda e, b, c: b.__setitem__("dados/capacitores.json",
                                   {"entidade": "CAPACITOR", "itens": [], "motivo_de_estar_vazio": "bancada"}),
     "reprova"),

    ("banco vazio e CALADO, sem dizer por que esta vazio",
     lambda e, b, c: (b.clear(), b.update(bancos_com()),
                      b["dados/modulos.json"].pop("motivo_de_estar_vazio"),
                      b["dados/alto-falantes.json"].pop("motivo_de_estar_vazio")), "reprova"),
]


# ----------------------------------------------------------------------------
# O QUE CADA QUEBRA TEM DE OUVIR DE VOLTA
#
# "Reprovou" nao e a mesma coisa que "reprovou pelo motivo certo". Uma mutacao pode
# quebrar o registro de um jeito que dispara OUTRA trava e voltar verde sem nunca ter
# medido a trava que ela existe para medir -- e a cicatriz da Robometria de 14/09/2026
# tem nome para isso: mutacao que nao morde e teste verde com outro nome. Entao cada
# quebra declara um pedaco da frase que espera ouvir, e a bancada cobra que ele apareca
# em ALGUM erro. Quebra sem linha aqui e erro da propria bancada, e ela reprova por isso.
# ----------------------------------------------------------------------------

ESPERA_OUVIR = {
    "modulo estabiliza em 16 ohm": "o vocabulario impedancia_de_modulo nao tem esse valor",
    "rms_por_impedancia CRESCE": "rms_por_impedancia cresce de",
    "impedancias_estaveis tem uma impedancia": "impedancias_estaveis tem 8 e rms_por_impedancia nao",
    "a tabela de rms tem uma impedancia": "rms_por_impedancia tem 0,5 e impedancias_estaveis nao",
    "modulo publicavel com unidade musical": "publicavel true com unidade_declarada",
    "modulo publicavel com manual lido por BUSCA": "lida por 'busca_web'",
    "modulo publicavel com ficha de LOJA": "publicavel true com fonte de nivel 3",
    "fonte.nivel DIGITADO": "O nivel e derivado do tipo, nunca digitado",
    "publicavel false sem motivo": "publicavel false sem motivo_nao_publicavel",
    "impedancias_estaveis sem declarar": "exige impedancias_estaveis_declarada_por",
    "unidade_declarada_por com uma origem inventada": "nao e origem legitima",
    "modulo sem rms_por_impedancia": "sem rms_por_impedancia",
    "item sem url_busca_produto": "sem afiliado.url_busca_produto",
    "url_busca_produto DIGITADA": "nao bate com a fabricada do molde",
    "item com url de afiliado e sem url_produto": "o teste de vida e IMPOSSIVEL",
    "afiliado.intestavel gravado ao contrario": "e o derivado diz",
    "id que nao e o slug": "o id nao e o slug de marca + modelo",
    "Thiele-Small com Fs de 4 Hz": "thiele_small.fs_hz = 4.0 fora da faixa",
    "Thiele-Small com Vas de 672,3": "thiele_small.vas_l = 672.3 fora da faixa",
    "alto-falante 2+2 gravado com 1 bobina": "bobinas = 1 e a string '2+2' diz 2",
    "alto-falante com ohms_por_bobina": "ohms_por_bobina = 4.0 e a string",
    "alto-falante com bobina 3+3": "impedancia_bobinas = '3+3' fora do vocabulario",
    "bobina que o esquema aceita e o gerador": "nao aparece em nenhum dos 24 casos",
    "a chave campos_que_exigem_declaracao_de_origem some": "campos_que_exigem_declaracao_de_origem sumiu",
    "a lista de campos que exigem origem fica vazia": "campos_que_exigem_declaracao_de_origem sumiu",
    "a constante faixa-de-validacao-thiele-small some": "faixa-de-validacao-thiele-small sumiu",
    "o vocabulario impedancia_de_modulo some": "o vocabulario impedancia_de_modulo sumiu",
    "piso_de_compra.moldes some": "piso_de_compra.moldes sumiu",
    "escada_de_fontes.niveis some": "escada_de_fontes.niveis sumiu",
    "entidade CAIXA perde o motivo": "sem motivo_de_nao_ter_banco_ainda",
    "o esquema declara um banco que nao existe": "e o arquivo nao existe",
    "existe arquivo de banco que nenhuma entidade": "nenhuma entidade do esquema o declara",
    "banco vazio e CALADO": "esta vazio e nao diz por que",
}


def fragmento_esperado(nome):
    for prefixo, fragmento in ESPERA_OUVIR.items():
        if nome.startswith(prefixo):
            return fragmento
    return None


def main():
    falhas = []
    print("MUTACOES DO BANCO - OHMETRIA")
    print("Cada linha produz um mundo e pergunta ao validador o que ele decide.\n")

    for nome, aplicar, espera in MUTACOES:
        esquema = copy.deepcopy(ESQUEMA)
        constantes = copy.deepcopy(CONSTANTES)
        bancos = bancos_com([MODULO_OK], [FALANTE_OK])

        aplicar(esquema, bancos, constantes)

        erros, _, _ = validador.validar(esquema, bancos, constantes)
        erros += validador.conferir_contra_o_gerador(bancos, CASOS_F1)

        decidiu = "reprova" if erros else "passa"
        motivo_certo = True
        if espera == "reprova":
            fragmento = fragmento_esperado(nome)
            if fragmento is None:
                falhas.append((nome, espera, "sem linha em ESPERA_OUVIR",
                               ["quebra sem frase esperada: a bancada nao sabe se ela mordeu a trava certa"]))
                motivo_certo = False
            elif decidiu == "reprova" and not any(fragmento in e for e in erros):
                falhas.append((nome, espera, "reprovou por OUTRO motivo",
                               ["esperava ouvir %r" % fragmento] + erros[:2]))
                motivo_certo = False

        marca = "ok " if (decidiu == espera and motivo_certo) else "NAO"
        if decidiu != espera:
            falhas.append((nome, espera, decidiu, erros))
        print("  %s  %-74s espera %-7s deu %s" % (marca, nome[:74], espera, decidiu))

    mundos = sum(1 for m in MUTACOES if m[2] == "passa")
    quebras = len(MUTACOES) - mundos
    print("\n%d mutacoes: %d mundos que tem de PASSAR e %d quebras que tem de REPROVAR."
          % (len(MUTACOES), mundos, quebras))

    if falhas:
        print("\n%d DECIDIRAM ERRADO:" % len(falhas))
        for nome, espera, decidiu, erros in falhas:
            print("  - %s: esperava %s, deu %s" % (nome, espera, decidiu))
            for e in erros[:3]:
                print("      %s" % e)
        sys.exit(1)

    print("Todas decidiram certo, nos DOIS lados da fronteira.")


if __name__ == "__main__":
    main()
