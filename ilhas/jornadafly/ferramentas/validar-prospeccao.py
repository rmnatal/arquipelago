#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O PORTAO do banco de prospeccao do widget (bloco 6 da jornadafly).

    python3 ferramentas/validar-prospeccao.py

Reprova com codigo 1 e imprime cada defeito com o dominio ao lado. As regras, e
cada uma existe por causa de um defeito que e facil de cometer neste arquivo:

  1. PRESENCA, NUNCA AUSENCIA. Campo de fato aceita `true` ou `null`. `false` e
     RECUSADO: busca nao sabe afirmar ausencia (regra do ARQUIPELAGO.md, vinda da
     regua-prospeccao.py da aquametria, 24/09/2026).
  2. TODA AFIRMACAO TEM EVIDENCIA QUE A NOMEIA. Campo de fato em `true` -- e
     `tipo` preenchido -- exige uma evidencia cujo `afirma` seja aquele campo.
     Sem isso o arquivo vira palpite com cara de medicao, e e o defeito que mais
     barato se comete: o nome do dominio «parece» de operador.
  3. NADA DE DERIVADO GRAVADO. `prioridade`, `ferramentas_ofertaveis`, `veredito`
     e `classe` nao podem existir dentro de uma linha: quem os gravar cria uma
     segunda verdade que envelhece calada.
  4. VOCABULARIO FECHADO em `tipo`, `relacao_com_a_versao_do_banco` e `origem`.
  5. AS DUAS METADES SE FALAM, e esta e a regra que pega evidencia inventada:
     toda consulta citada em `consultas_do_corpus` tem de existir em
     dados/corpus-buscas.md, E todo dominio de origem `corpus-bloco-1` tem de
     aparecer naquele arquivo. Afirmar que o corpus mediu algo que ele nao mediu
     e a invencao mais difundida que esta fabrica ja pagou.
  6. EXPERIENCIA DO BANCO EXISTE. Todo id em `experiencias_do_banco_atendidas`
     tem de existir em dados/experiencias.json.
  7. ACENTO NO TEXTO DE TELA. Todo texto que a referencia renderiza passa por uma
     regua de palavras que, em portugues correto, levam acento. E a cicatriz da
     Robometria, e na aquametria essa mesma regua pegou um defeito que nao era de
     acento.
  8. O ARQUIVO DE LEITURA E O QUE A REFERENCIA GERA. Regera e compara byte a byte.
  9. AUTOTESTE: `--autoteste` prova que cada regra acima MORDE, construindo o
     mundo que ela tem de reprovar. Portao que nunca reprovou nada e decoracao.
"""

import importlib.util
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "prospeccao_referencia", os.path.join(AQUI, "prospeccao-referencia.py"))
ref = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ref)
RAIZ = ref.RAIZ

# Palavras que em portugues correto levam acento. Se uma delas aparecer SEM
# acento num texto de tela, e acento perdido.
#
# E A REGUA NAO ADIVINHA PELA VIZINHANCA: ela RETIRA o que esta entre craseadas
# antes de olhar. Caminho de arquivo, nome de ferramenta e valor de vocabulario
# sao corretamente sem acento, e a primeira versao desta regua reprovou
# `dados/experiencias.json` e `prospeccao-referencia.py` -- texto legitimo. A
# saida nao e uma heuristica melhor, e estrutura: o ARQUIPELAGO.md ja ensina isso
# na quarta trava da familia (linha 303), aprendida no Clube do Mosaico -- «quando
# o texto legitimo e o proibido sao a mesma palavra, quem decide e a estrutura,
# nunca a vizinhanca».
PALAVRAS_COM_ACENTO = (
    "nao", "sao", "pagina", "paginas", "proprio", "propria", "proprios", "proprias",
    "medicao", "medicoes", "execucao", "execucoes", "secao", "secoes", "razao",
    "numero", "numeros", "preco", "precos", "publico", "publicos", "unico", "unica",
    "dominio", "dominios", "criterio", "criterios", "tres", "apos", "ate", "tambem",
    "orgao", "experiencia", "experiencias", "versao", "versoes",
    "concessionaria", "prospeccao", "informacao", "ingles",
)

# Codigo, caminho de arquivo e nome de ferramenta moram entre craseadas e NAO
# passam pela regua de acento.
CRASEADAS = re.compile(r"`[^`]*`")


def sem_codigo(texto):
    return CRASEADAS.sub(" ", texto)

CAMPOS_OBRIGATORIOS = (
    "dominio", "nome", "tipo", "pais", "origem", "consultas_do_corpus",
    "experiencias_do_banco_atendidas", "relacao_com_a_versao_do_banco",
    "evidencias", "motivos", "contato", "plataforma_do_site",
)

# `afirma` e uma LISTA: uma medicao sustenta varios fatos de uma vez, e dizer
# QUAIS e o que separa a evidencia da impressao. «operador, e tres URLs dele» na
# SERP sustenta tipo, site proprio e venda de experiencia -- e nao sustenta
# «publica conteudo proprio», que e outra coisa e precisa da propria medicao.
# Fora dos campos de fato, `afirma` aceita estas afirmacoes de metodo:
AFIRMACOES_DE_METODO = ("tipo", "site_proprio", "presenca_medida_uma_vez_so")


def _texto_de_tela(banco):
    """Os textos que a referencia renderiza para a tela, com o caminho de cada um."""
    saida = []
    for chave in ("o_que_este_arquivo_e", "acentuacao",
                  "o_que_mediu_isto_e_o_que_ele_nao_alcanca", "presenca_nunca_ausencia"):
        saida.append((chave, banco[chave]))
    for bloco in ("a_regra_que_ordena_esta_lista", "a_escada_da_prioridade",
                  "a_regra_da_oferta", "dominios_do_corpus_nao_classificados"):
        for k, v in banco[bloco].items():
            if isinstance(v, str):
                saida.append(("%s.%s" % (bloco, k), v))
    a = banco["o_achado_desta_passada"]
    for k, v in a.items():
        if isinstance(v, str):
            saida.append(("o_achado_desta_passada.%s" % k, v))
        elif isinstance(v, list):
            for i, item in enumerate(v):
                saida.append(("o_achado_desta_passada.%s[%d]" % (k, i), item))
    for c in banco["candidatos"]:
        saida.append(("%s.nome" % c["dominio"], c["nome"]))
        for i, m in enumerate(c.get("motivos", [])):
            saida.append(("%s.motivos[%d]" % (c["dominio"], i), m))
        for i, e in enumerate(c.get("evidencias", [])):
            saida.append(("%s.evidencias[%d].diz" % (c["dominio"], i), e.get("diz", "")))
    return saida


def conferir(banco, experiencias, corpus, md_atual=None):
    """Devolve a lista de defeitos. Lista vazia = aprovado."""
    erros = []
    estado = ref.estado_do_banco(experiencias)
    corpus_minusculo = corpus.lower()
    vistos = set()

    if banco.get("publicar") is not False:
        erros.append("cabecalho: publicar tem de ser false nesta lista")

    for c in banco["candidatos"]:
        d = c.get("dominio", "<sem dominio>")

        if d in vistos:
            erros.append("%s: dominio repetido" % d)
        vistos.add(d)

        for campo in CAMPOS_OBRIGATORIOS:
            if campo not in c:
                erros.append("%s: falta o campo obrigatorio `%s`" % (d, campo))

        # regra 3
        for proibido in ref.CAMPOS_PROIBIDOS_NO_BANCO:
            if proibido in c:
                erros.append("%s: campo DERIVADO `%s` gravado no banco" % (d, proibido))

        # regra 1 e 2
        afirmados = set()
        for e in c.get("evidencias", []):
            afirma = e.get("afirma")
            if isinstance(afirma, str):
                erros.append("%s: evidencia com `afirma` em texto; tem de ser lista" % d)
                afirma = [afirma]
            for nome in (afirma or []):
                afirmados.add(nome)
        for campo in ref.CAMPOS_DE_FATO:
            valor = c.get(campo)
            if valor is False:
                erros.append("%s: `%s` esta false, e este arquivo nao afirma ausencia" % (d, campo))
            elif valor is True and campo not in afirmados:
                erros.append("%s: `%s` afirmado em true sem evidencia que o nomeie" % (d, campo))
            elif valor not in (True, None, False):
                erros.append("%s: `%s` tem valor fora de true/null: %r" % (d, campo, valor))

        # regra 2, para o tipo
        if c.get("tipo") is not None and "tipo" not in afirmados:
            erros.append("%s: `tipo` preenchido (%s) sem evidencia que o nomeie" % (d, c["tipo"]))

        # regra 4
        if c.get("tipo") is not None and c["tipo"] not in ref.TIPOS_VALIDOS:
            erros.append("%s: tipo fora do vocabulario: %s" % (d, c["tipo"]))
        if c.get("relacao_com_a_versao_do_banco") not in ref.RELACOES_VALIDAS:
            erros.append("%s: relacao_com_a_versao_do_banco fora do vocabulario: %r"
                         % (d, c.get("relacao_com_a_versao_do_banco")))
        origem = c.get("origem", "")
        if origem != "corpus-bloco-1" and not re.match(r"^busca-\d{4}-\d{2}-\d{2}$", origem):
            erros.append("%s: origem fora do vocabulario: %r" % (d, origem))

        if not c.get("evidencias"):
            erros.append("%s: nenhuma evidencia" % d)
        for e in c.get("evidencias", []):
            for k in ("afirma", "como", "onde", "data_leitura", "diz"):
                if not e.get(k):
                    erros.append("%s: evidencia sem `%s`" % (d, k))
            for nome in (e.get("afirma") or []):
                if nome not in tuple(ref.CAMPOS_DE_FATO) + AFIRMACOES_DE_METODO:
                    erros.append("%s: evidencia afirma `%s`, que nao e campo nem afirmacao de metodo"
                                 % (d, nome))
            if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(e.get("data_leitura", ""))):
                erros.append("%s: evidencia com data_leitura fora de AAAA-MM-DD: %r"
                             % (d, e.get("data_leitura")))

        # regra 5
        for consulta in c.get("consultas_do_corpus", []):
            if ref.cluster_da_consulta(banco, consulta) is None:
                erros.append("%s: consulta `%s` nao esta em nenhum cluster do cabecalho" % (d, consulta))
            if consulta.lower() not in corpus_minusculo:
                erros.append("%s: consulta `%s` NAO existe em dados/corpus-buscas.md" % (d, consulta))
        if c.get("origem") == "corpus-bloco-1" and d.lower() not in corpus_minusculo:
            erros.append("%s: origem diz corpus-bloco-1 e o dominio NAO aparece em dados/corpus-buscas.md" % d)
        if c.get("origem") == "corpus-bloco-1" and not c.get("consultas_do_corpus"):
            erros.append("%s: origem diz corpus-bloco-1 e nao cita nenhuma consulta do corpus" % d)

        # regra 6
        for i in c.get("experiencias_do_banco_atendidas", []):
            if i not in estado["ids"]:
                erros.append("%s: experiencia `%s` nao existe em dados/experiencias.json" % (d, i))

        if not c.get("motivos"):
            erros.append("%s: nenhum motivo escrito" % d)

    # as consultas do cabecalho tambem precisam existir no corpus
    for cluster, consultas in banco["consultas_do_corpus_por_cluster"].items():
        for consulta in consultas:
            if consulta.lower() not in corpus_minusculo:
                erros.append("cabecalho: cluster %s cita `%s`, que NAO existe em dados/corpus-buscas.md"
                             % (cluster, consulta))

    # regra 7
    for caminho, texto in _texto_de_tela(banco):
        limpo = sem_codigo(texto)
        for palavra in PALAVRAS_COM_ACENTO:
            if re.search(r"\b%s\b" % palavra, limpo, flags=re.IGNORECASE):
                erros.append("%s: acento perdido na palavra `%s`" % (caminho, palavra))

    # regra 8
    if md_atual is not None:
        if md_atual != ref.texto(banco, estado):
            erros.append("dados/prospeccao-widget.md NAO e o que a referencia gera agora")

    return erros


# ------------------------------------------------------------------- autoteste

def _mundo_base():
    banco, experiencias = ref.carregar()
    with open(os.path.join(RAIZ, "dados", "corpus-buscas.md"), encoding="utf-8") as f:
        corpus = f.read()
    return banco, experiencias, corpus


def autoteste():
    """Prova que cada regra morde. Cada caso constroi o mundo que ela reprova."""
    casos = []

    def caso(nome, mexer, espera):
        banco, experiencias, corpus = _mundo_base()
        mexer(banco, experiencias)
        erros = conferir(banco, experiencias, corpus)
        achou = any(espera in e for e in erros)
        casos.append((nome, achou, espera, erros[:3]))

    caso("fato em false e recusado",
         lambda b, e: b["candidatos"][0].__setitem__("vende_experiencia", False),
         "nao afirma ausencia")
    caso("fato em true sem evidencia e recusado",
         lambda b, e: b["candidatos"][2].__setitem__("vende_experiencia", True),
         "sem evidencia que o nomeie")
    caso("tipo sem evidencia e recusado",
         lambda b, e: b["candidatos"][2].__setitem__("tipo", "receptivo"),
         "sem evidencia que o nomeie")
    caso("prioridade gravada no banco e recusada",
         lambda b, e: b["candidatos"][0].__setitem__("prioridade", "1"),
         "campo DERIVADO")
    caso("tipo fora do vocabulario e recusado",
         lambda b, e: b["candidatos"][0].__setitem__("tipo", "loja_de_aquarismo"),
         "fora do vocabulario"),
    caso("consulta que o corpus nao tem e recusada",
         lambda b, e: b["candidatos"][0]["consultas_do_corpus"].append("quanto custa um robo aspirador"),
         "nao esta em nenhum cluster")
    caso("consulta do cabecalho que o corpus nao tem e recusada",
         lambda b, e: b["consultas_do_corpus_por_cluster"]["A2"].append("quanto custa um filtro canister"),
         "NAO existe em dados/corpus-buscas.md")
    caso("dominio que diz vir do corpus e nao esta nele e recusado",
         lambda b, e: b["candidatos"][0].__setitem__("dominio", "inventado-pela-fundacao.com.br"),
         "NAO aparece em dados/corpus-buscas.md")
    caso("experiencia que o banco nao tem e recusada",
         lambda b, e: b["candidatos"][0]["experiencias_do_banco_atendidas"].append("rio-pao-de-acucar"),
         "nao existe em dados/experiencias.json")
    caso("acento perdido no texto de tela e recusado",
         lambda b, e: b["candidatos"][0]["motivos"].append("Este candidato nao tem pagina em portugues."),
         "acento perdido")
    caso("dominio repetido e recusado",
         lambda b, e: b["candidatos"].append(dict(b["candidatos"][0])),
         "dominio repetido")
    caso("evidencia sem data e recusada",
         lambda b, e: b["candidatos"][0]["evidencias"][0].__setitem__("data_leitura", "ontem"),
         "data_leitura fora de AAAA-MM-DD")
    caso("afirma em texto em vez de lista e recusado",
         lambda b, e: b["candidatos"][0]["evidencias"][0].__setitem__("afirma", "tipo"),
         "`afirma` em texto"),
    caso("caminho de arquivo entre craseadas NAO e acento perdido",
         lambda b, e: b["candidatos"][0]["motivos"].append("Ver `dados/experiencias.json` e `prospeccao-referencia.py`."),
         "" if False else "NUNCA_ESPERADO")
    casos[-1] = (casos[-1][0], not casos[-1][1], "nenhum erro de acento", casos[-1][3])
    caso("publicar true e recusado",
         lambda b, e: b.__setitem__("publicar", True),
         "publicar tem de ser false")

    falhas = 0
    for nome, achou, espera, amostra in casos:
        print("%-62s %s" % (nome, "OK" if achou else "NAO MORDEU"))
        if not achou:
            falhas += 1
            print("    esperava conter: %s" % espera)
            print("    primeiros erros: %s" % amostra)
    print("\nautoteste: %d casos, %d falha(s)" % (len(casos), falhas))
    return 1 if falhas else 0


def main(argv):
    if "--autoteste" in argv:
        return autoteste()

    banco, experiencias, corpus = _mundo_base()
    md = None
    destino = os.path.join(RAIZ, "dados", "prospeccao-widget.md")
    if os.path.exists(destino):
        with open(destino, encoding="utf-8") as f:
            md = f.read()
    else:
        print("FALTA dados/prospeccao-widget.md -- rode ferramentas/gerar-prospeccao.py")
        return 1

    erros = conferir(banco, experiencias, corpus, md)
    if erros:
        print("REPROVADO -- %d defeito(s):\n" % len(erros))
        for e in erros:
            print("  - %s" % e)
        return 1

    estado = ref.estado_do_banco(experiencias)
    c = ref.contagens(banco, estado)
    print("APROVADO -- %d candidatos, %s" % (
        c["candidatos"],
        ", ".join("%s: %d" % (k, v) for k, v in sorted(c["por_prioridade"].items()))))
    print("           o .md e identico ao que a referencia gera")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
