#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MUTACOES da lista de prospeccao do widget (bloco 6 da jornadafly).

    python3 ferramentas/mutacoes-prospeccao.py

Quebra o banco de propósito e exige que algum portão VEJA. Portao que nunca
reprovou nada e decoracao, e regra que nenhuma mutacao morde e prosa.

Quatro familias, e cada mutacao declara a frase que espera ouvir:

  A. MUNDOS QUE TEM DE PASSAR. O banco de hoje, e os bancos que o esquema
     permite e que esta lista ainda nao tem: lista com um candidato so, lista sem
     nenhum candidato de prioridade 1, e -- a que mais importa -- o banco de
     EXPERIENCIAS carregado. A regra da oferta e calculada sobre o banco, entao o
     mundo em que o banco tem dado e um mundo que esta bancada precisa saber ler.
  B. QUEBRAS DO BANCO DE CANDIDATOS. Cada uma espera uma frase do portao.
  C. QUEBRAS DA REGUA DA OFERTA, feitas no banco de EXPERIENCIAS. Sao as que
     provam que a regra le o dado em vez de acreditar na lista.
  D. MORTES. Chave que some da fonte tem de MATAR a ferramenta, nunca virar
     literal silencioso.
"""

import copy
import importlib.util
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))


def _carregar(nome, arquivo):
    spec = importlib.util.spec_from_file_location(nome, os.path.join(AQUI, arquivo))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


ref = _carregar("prospeccao_referencia", "prospeccao-referencia.py")
val = _carregar("validar_prospeccao", "validar-prospeccao.py")
RAIZ = ref.RAIZ

with open(os.path.join(RAIZ, "dados", "corpus-buscas.md"), encoding="utf-8") as f:
    CORPUS = f.read()

BANCO, EXPERIENCIAS = ref.carregar()

resultados = []


def mundo():
    return copy.deepcopy(BANCO), copy.deepcopy(EXPERIENCIAS)


def achar(banco, dominio):
    for c in banco["candidatos"]:
        if c["dominio"] == dominio:
            return c
    raise KeyError(dominio)


def passa(nome, mexer):
    """Mundo que TEM de passar o portao."""
    banco, experiencias = mundo()
    if mexer:
        mexer(banco, experiencias)
    try:
        erros = val.conferir(banco, experiencias, CORPUS)
    except Exception as e:                      # noqa: BLE001
        resultados.append((nome, False, "o portao MORREU: %r" % e))
        return
    resultados.append((nome, not erros, "esperava aprovado; veio: %s" % erros[:2]))


def quebra(nome, mexer, frase):
    """Mundo que o portao TEM de reprovar, com a frase declarada."""
    banco, experiencias = mundo()
    mexer(banco, experiencias)
    try:
        erros = val.conferir(banco, experiencias, CORPUS)
    except Exception as e:                      # noqa: BLE001
        resultados.append((nome, False, "o portao MORREU em vez de reprovar: %r" % e))
        return
    achou = any(frase in e for e in erros)
    resultados.append((nome, achou, "esperava ouvir «%s»; veio: %s" % (frase, erros[:2])))


def morte(nome, mexer):
    """Chave que some tem de MATAR a referencia, nunca virar literal."""
    banco, experiencias = mundo()
    mexer(banco, experiencias)
    try:
        ref.texto(banco, ref.estado_do_banco(experiencias))
    except Exception:
        resultados.append((nome, True, ""))
        return
    resultados.append((nome, False, "a referencia seguiu em frente com a chave faltando"))


def espera_oferta(nome, mexer, dominio, ferramenta, ofertavel):
    """A regua da oferta, no mundo que a mutacao constroi."""
    banco, experiencias = mundo()
    if mexer:
        mexer(banco, experiencias)
    estado = ref.estado_do_banco(experiencias)
    fs = {x["ferramenta"]: x for x in ref.ferramentas_ofertaveis(banco, estado, achar(banco, dominio))}
    obtido = fs[ferramenta]["ofertavel"]
    resultados.append((nome, obtido is ofertavel,
                       "esperava %s=%s para %s; veio %s (%s)"
                       % (ferramenta, ofertavel, dominio, obtido, fs[ferramenta]["por_que"])))


FAIXA = {
    "id": "veneza-diaria-hospedagem",
    "cidade": "veneza",
    "o_que_o_numero_e": "faixa de diária de hospedagem publicada por terceiro",
    "publicado_por": "fonte de mutação",
    "url": "https://exemplo.invalido/",
    "data_leitura": "2026-10-23",
}
PASSE = {
    "id": "roma-roma-pass",
    "cidade": "roma",
    "categoria": "passe_de_cidade",
    "operador": {"nome": "operador de mutação", "tipo": "poder_publico"},
    "versoes": [{"rotulo": "48 h"}],
}
COBERTURA = {
    "id": "roma-pass-cobre-coliseu",
    "passe": "roma-roma-pass",
    "experiencia": "roma-coliseu-ingresso",
    "data_leitura": "2026-10-23",
}

# ---------------------------------------------------------------- A. mundos

passa("mundo de hoje passa", None)
passa("lista com UM candidato so passa",
      lambda b, e: b.__setitem__("candidatos", [achar(b, "bondinho.com.br")]))
passa("lista SEM nenhum candidato de prioridade 1 passa",
      lambda b, e: b.__setitem__("candidatos", [c for c in b["candidatos"]
                                                if ref.prioridade(b, c)[0] != "1"]))
passa("banco de experiencias CARREGADO passa",
      lambda b, e: (e["faixas_diarias"].append(FAIXA),
                    e["experiencias"].append(PASSE),
                    e["coberturas_de_passe"].append(COBERTURA)))

# -------------------------------------------- B. quebras do banco de candidatos

quebra("fato em false",
       lambda b, e: achar(b, "bondinho.com.br").__setitem__("publica_conteudo_proprio", False),
       "nao afirma ausencia")
quebra("fato em true sem evidencia que o nomeie",
       lambda b, e: achar(b, "tayratourscusco.com").__setitem__("vende_experiencia", True),
       "sem evidencia que o nomeie")
quebra("tipo escrito sem evidencia",
       lambda b, e: achar(b, "ingressomachupicchu.com").__setitem__("tipo", "revendedor_de_ingresso"),
       "sem evidencia que o nomeie")
quebra("prioridade gravada no banco",
       lambda b, e: achar(b, "bondinho.com.br").__setitem__("prioridade", "1"),
       "campo DERIVADO")
quebra("ferramentas_ofertaveis gravado no banco",
       lambda b, e: achar(b, "bondinho.com.br").__setitem__("ferramentas_ofertaveis", ["F1"]),
       "campo DERIVADO")
quebra("tipo fora do vocabulario",
       lambda b, e: achar(b, "bondinho.com.br").__setitem__("tipo", "operador_de_balao"),
       "fora do vocabulario")
quebra("relacao com a versao do banco fora do vocabulario",
       lambda b, e: achar(b, "bondinho.com.br").__setitem__("relacao_com_a_versao_do_banco", "talvez"),
       "relacao_com_a_versao_do_banco fora do vocabulario")
quebra("origem inventada",
       lambda b, e: achar(b, "bondinho.com.br").__setitem__("origem", "achei_na_memoria"),
       "origem fora do vocabulario")
quebra("consulta que o corpus nao mediu",
       lambda b, e: achar(b, "bondinho.com.br")["consultas_do_corpus"].append("quanto custa o eurostar"),
       "nao esta em nenhum cluster")
quebra("consulta no cabecalho que o corpus nao tem",
       lambda b, e: b["consultas_do_corpus_por_cluster"]["A1"].append("vale a pena o trem bala"),
       "NAO existe em dados/corpus-buscas.md")
quebra("dominio que diz vir do corpus e nao esta nele",
       lambda b, e: achar(b, "perurail.com").__setitem__("dominio", "perurail-brasil.com.br"),
       "NAO aparece em dados/corpus-buscas.md")
quebra("dominio do corpus sem nenhuma consulta citada",
       lambda b, e: achar(b, "perurail.com").__setitem__("consultas_do_corpus", []),
       "nao cita nenhuma consulta do corpus")
quebra("experiencia do banco que nao existe",
       lambda b, e: achar(b, "bondinho.com.br")["experiencias_do_banco_atendidas"].append("rio-pao-de-acucar"),
       "nao existe em dados/experiencias.json")
quebra("candidato sem evidencia nenhuma",
       lambda b, e: achar(b, "bondinho.com.br").__setitem__("evidencias", []),
       "nenhuma evidencia")
quebra("candidato sem motivo escrito",
       lambda b, e: achar(b, "bondinho.com.br").__setitem__("motivos", []),
       "nenhum motivo escrito")
quebra("evidencia com data em prosa",
       lambda b, e: achar(b, "bondinho.com.br")["evidencias"][0].__setitem__("data_leitura", "mes passado"),
       "data_leitura fora de AAAA-MM-DD")
quebra("evidencia que afirma campo inexistente",
       lambda b, e: achar(b, "bondinho.com.br")["evidencias"][0].__setitem__("afirma", ["tem_selo_de_qualidade"]),
       "nao e campo nem afirmacao de metodo")
quebra("afirma em texto em vez de lista",
       lambda b, e: achar(b, "bondinho.com.br")["evidencias"][0].__setitem__("afirma", "tipo"),
       "em texto; tem de ser lista")
quebra("dominio repetido",
       lambda b, e: b["candidatos"].append(copy.deepcopy(achar(b, "bondinho.com.br"))),
       "dominio repetido")
quebra("publicar virou true",
       lambda b, e: b.__setitem__("publicar", True),
       "publicar tem de ser false")
quebra("acento perdido no motivo",
       lambda b, e: achar(b, "bondinho.com.br")["motivos"].append("Nao tem pagina em portugues."),
       "acento perdido")

# ------------------------------------- C. a regua da oferta le o BANCO

espera_oferta("F1 nao vai a quem o banco nao atende (hoje, bondinho)",
              None, "bondinho.com.br", "F1", False)
espera_oferta("F1 nao vai a quem vende versao que INCLUI a do banco (viagemitalia)",
              None, "viagemitalia.com", "F1", False)
espera_oferta("F1 VAI quando o banco ganha a experiencia e a mesma versao",
              lambda b, e: (achar(b, "bondinho.com.br").__setitem__(
                  "experiencias_do_banco_atendidas", ["roma-coliseu-ingresso"]),
                  achar(b, "bondinho.com.br").__setitem__(
                      "relacao_com_a_versao_do_banco", "vende_a_mesma_versao")),
              "bondinho.com.br", "F1", True)
espera_oferta("F1 NAO vai a barrado, mesmo vendendo a mesma versao",
              lambda b, e: (achar(b, "romapravoce.com").__setitem__(
                  "relacao_com_a_versao_do_banco", "vende_a_mesma_versao")),
              "romapravoce.com", "F1", False)
espera_oferta("F2 nao vai a ninguem com o banco sem FAIXA_DIARIA",
              None, "bondinho.com.br", "F2", False)
espera_oferta("F2 VAI quando o banco ganha uma FAIXA_DIARIA",
              lambda b, e: e["faixas_diarias"].append(FAIXA),
              "bondinho.com.br", "F2", True)
espera_oferta("F3 nao vai a ninguem com o banco sem passe e sem cobertura",
              None, "bondinho.com.br", "F3", False)
espera_oferta("F3 VAI quando o banco ganha passe E cobertura",
              lambda b, e: (e["experiencias"].append(PASSE), e["coberturas_de_passe"].append(COBERTURA)),
              "bondinho.com.br", "F3", True)
espera_oferta("F3 NUNCA vai a quem vende passe de cidade, mesmo com o banco cheio",
              lambda b, e: (e["experiencias"].append(PASSE), e["coberturas_de_passe"].append(COBERTURA),
                            achar(b, "bondinho.com.br").__setitem__("vende_passe_de_cidade", True),
                            achar(b, "bondinho.com.br")["evidencias"][0]["afirma"].append("vende_passe_de_cidade")),
              "bondinho.com.br", "F3", False)
espera_oferta("uma medicao de pt-BR move o toureiffel da 3 para a 2, e a F1 abre",
              lambda b, e: (achar(b, "toureiffel.paris").__setitem__("fala_pt_br", True),
                            achar(b, "toureiffel.paris")["evidencias"][0]["afirma"].append("fala_pt_br")),
              "toureiffel.paris", "F1", True)

# ------------------------------------------------------------------ D. mortes

morte("chave `candidatos` que some mata a referencia",
      lambda b, e: b.pop("candidatos"))
morte("bloco `a_regra_que_ordena_esta_lista` que some mata a referencia",
      lambda b, e: b.pop("a_regra_que_ordena_esta_lista"))
morte("bloco `o_achado_desta_passada` que some mata a referencia",
      lambda b, e: b.pop("o_achado_desta_passada"))
morte("cluster que some do cabecalho mata a referencia",
      lambda b, e: b.pop("consultas_do_corpus_por_cluster"))


def main():
    # CONTATO PREENCHIDO nao esta aqui de proposito: quem o proibe e
    # ferramentas/teste-prospeccao.py, nao o portao estrutural. Escrever aqui uma
    # mutacao que espera uma frase que o portao nao diz seria a bateria mentindo
    # sobre o proprio alcance.
    falhas = [(n, m) for n, ok, m in resultados if not ok]
    for n, ok, m in resultados:
        print("%-72s %s" % (n[:72], "OK" if ok else "FALHOU"))
        if not ok:
            print("      %s" % m)
    print("\nmutacoes-prospeccao: %d casos, %d falha(s)" % (len(resultados), len(falhas)))
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
