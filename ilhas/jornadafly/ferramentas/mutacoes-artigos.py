#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra os artigos-ancora e exige que o portao deles VEJA.

    python3 ferramentas/mutacoes-artigos.py

Cada caso abaixo e um mundo com UM defeito. O veredito tem tres valores e so um
e aceitavel:

    REPROVA  o portao viu o defeito e relatou           -- e o que se exige
    INERTE   o portao olhou e aprovou                   -- afirmacao que nao mede
    MORRE    o portao estourou em vez de relatar        -- pior que inerte

POR QUE «MORRE» E PIOR QUE «INERTE», e esta nao e teoria: em 22/10/2026 a bateria
da F3 desta mesma pasta mediu CINCO quebras classificadas `morre`, porque o
portao PEGAVA o defeito e logo depois estourava lendo a lista que a propria
afirmacao acabara de dizer vazia. Portao que morre nao diz qual e o defeito, e
quem le o traceback procura bug na bancada em vez de ler o que ela achou. A regra
que saiu dali vale aqui: afirmar primeiro, e so entao ler o que a afirmacao
garantiu.

E POR QUE ESTA BATERIA EXISTE NO MESMO DIA DO ARTIGO, com a 31.3 na mesa. A 31.3
proibe «ampliar, refatorar, deduplicar ou TESTAR PORTAO QUE JA EXISTE» enquanto
houver item de conteudo aberto. O portao conferido aqui nasceu na mesma passada
que o conteudo que ele guarda -- e o mesmo desenho que a F1, a F2 e a F3 tiveram
em 22/10/2026, cada uma com teste e mutacao na propria passada. Bancada sobre
bancada continua proibida; esta e a bancada DO artigo, e nao uma bancada sobre a
bancada do artigo.
"""

import copy
import importlib.util
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))


def _referencia():
    caminho = os.path.join(AQUI, "artigos-referencia.py")
    spec = importlib.util.spec_from_file_location("artigos_referencia", caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


art = _referencia()


# --- as quebras, uma por defeito -------------------------------------------

def preco_trocado(d):
    c = d["caixa_de_resposta"]
    c["frase"] = c["frase"].replace("€90", "€70").replace("€14,80", "€12,80") \
                           .replace("€18", "€16").replace("US$ 37", "US$ 27")


def preco_sem_data(d):
    d["caixa_de_resposta"]["frase"] = "O passeio custa €90 para o grupo inteiro."


def frase_proibida(d):
    d["description"] = "Uma experiência transformadora em Veneza, e imperdível."


def bastidor_e_secao(d):
    d["caixa_de_resposta"]["promessa"] = (
        "O egresso da nuvem recusou a fonte, veja a seção 25.")


def nome_de_rotina(d):
    d["dobras"][0]["paragrafos"].append("A Sentinela confere isto na ronda.")


def promessa_de_voo(d):
    d["titulo"] = "Quanto custa o voo de gôndola em Veneza"


def consulta_da_ferramenta(d):
    d["h1"] = "Quanto custa a gôndola para 4 pessoas"


def mae_sem_link_no_corpo(d):
    d["mae_no_corpo"] = "Veja as outras respostas de preço desta página."


def trilha_curta(d):
    d["trilha"] = d["trilha"][:3]


def trilha_com_o_atual_linkado(d):
    d["trilha"][-1]["url"] = d["url_planejada"]


def uma_irma_so(d):
    d["veja_tambem"] = d["veja_tambem"][:1]


def irma_de_outra_mae(d):
    d["veja_tambem"][0]["url"] = "/outra-mae/qualquer/"


def irma_de_si_mesma(d):
    d["veja_tambem"][0]["url"] = d["url_planejada"]


def ancora_clique_aqui(d):
    d["veja_tambem"][0]["ancora"] = "clique aqui"


def calcular_fora_da_ferramenta(d):
    d["monte_o_que_a_resposta_pede"][0]["calcular"]["url"] = "/outra-coisa/"


def calcular_sem_parametro(d):
    d["monte_o_que_a_resposta_pede"][0]["calcular"]["url"] = (
        "/calculadoras/quanto-custa-a-experiencia/")


def item_sem_saida_de_compra(d):
    d["monte_o_que_a_resposta_pede"][0]["ver_produtos"]["url"] = None


def link_cru_patrocinado(d):
    d["bloco_de_compra"]["rel"] = "sponsored nofollow noopener"


def link_de_loja_em_breve(d):
    d["bloco_de_compra"]["aviso"] = "Link de loja em breve."


def tabela_recolhida(d):
    d["tabela_recolhida"] = True


def tabela_sem_o_seis(d):
    d["tabela_resumo"] = [l for l in d["tabela_resumo"] if l["pessoas"] != 6]


def linha_de_tabela_sem_data(d):
    for l in d["tabela_resumo"]:
        l["lido_em"] = None


def json_ld_sem_trilha(d):
    d["json_ld"] = [b for b in d["json_ld"] if b["@type"] != "BreadcrumbList"]


def json_ld_sem_article(d):
    d["json_ld"] = [b for b in d["json_ld"] if b["@type"] != "Article"]


def faq_sem_resposta(d):
    d["faq"][0]["resposta"] = "   "


def faq_todo_da_mesma_frase(d):
    """O defeito desta passada, virado quebra.

    A primeira versao do FAQ emparelhava toda pergunta declarada com a frase da
    caixa de resposta. Em tres dos quatro artigos isso publicava um par que nao
    se fecha, e nenhuma afirmacao via.
    """
    for q in d["faq"]:
        q["resposta"] = d["caixa_de_resposta"]["frase"]
        q["resposta_sai_de"] = "caixa"


def faq_sem_dizer_de_onde(d):
    for q in d["faq"]:
        q.pop("resposta_sai_de", None)


def publicar_sem_site(d):
    d["publicar"] = True


def data_no_slug(d):
    d["url_planejada"] = "/guias/quanto-custa/gondola-2026/"


def url_fora_da_mae(d):
    d["url_planejada"] = "/gondola-veneza/"


def divergencia_sem_publicador(d):
    """A quebra mais fina da bateria, e ela foi achada pelo portao e nao por mim.

    O valor de terceiro (€80 da Eurodicas, €34 da GetYourGuide) nao esta no
    conjunto que o banco autoriza -- ele e justamente o numero COM QUE a ilha
    discorda. Ele passa so dentro da frase que nomeia quem o publicou e quando
    foi lido. Tirando o nome do publicador, o valor vira numero sem dono.
    """
    alvo = d["divergencias"][0]["frase"]
    for dobra in d["dobras"]:
        dobra["paragrafos"] = ["publicou €80, lido em 14/09/2026." if p == alvo
                               else p for p in dobra["paragrafos"]]


def divergencia_sem_data(d):
    alvo = d["divergencias"][0]["frase"]
    sem_data = alvo.replace(", lido em 14/09/2026", "")
    for dobra in d["dobras"]:
        dobra["paragrafos"] = [sem_data if p == alvo else p
                               for p in dobra["paragrafos"]]
    d["divergencias"][0]["frase"] = sem_data


def fim_de_funil_com_carro(d):
    d["link_do_momento"] = "aluguel de carro"


def inicio_de_funil_com_experiencia(d):
    d["momento"] = "inicio"


def acentuacao_corrompida(d):
    d["dobras"][0]["paragrafos"][0] = (
        "O preÃ§o Ã© por veículo.")


def ressalva_de_pendente_sumida(d):
    d["caixa_de_resposta"].pop("reconferir", None)


def preco_pendente_na_description(d):
    d["description"] = "O Angkor Pass de 1 dia custa US$ 37 por pessoa."


QUEBRAS = [
    ("preço trocado a mão", "gondola-veneza", preco_trocado),
    ("preço sem a data da coleta", "gondola-veneza", preco_sem_data),
    ("frase proibida pelo VOZ.md", "gondola-veneza", frase_proibida),
    ("bastidor da fábrica e número de seção", "gondola-veneza", bastidor_e_secao),
    ("nome de rotina na página", "gondola-veneza", nome_de_rotina),
    ("promessa de voo no título", "gondola-veneza", promessa_de_voo),
    ("guia tomando a consulta da calculadora", "gondola-veneza",
     consulta_da_ferramenta),
    ("mãe sem link numa frase do corpo", "gondola-veneza", mae_sem_link_no_corpo),
    ("trilha sem um nível", "gondola-veneza", trilha_curta),
    ("trilha com a página atual linkada", "gondola-veneza",
     trilha_com_o_atual_linkado),
    ("uma irmã só no «Veja também»", "gondola-veneza", uma_irma_so),
    ("irmã de outra mãe", "gondola-veneza", irma_de_outra_mae),
    ("a página como irmã de si mesma", "gondola-veneza", irma_de_si_mesma),
    ("âncora «clique aqui»", "gondola-veneza", ancora_clique_aqui),
    ("botão Calcular fora da ferramenta", "gondola-veneza",
     calcular_fora_da_ferramenta),
    ("botão Calcular sem o parâmetro da página", "gondola-veneza",
     calcular_sem_parametro),
    ("item do bloco sem saída de compra", "gondola-veneza",
     item_sem_saida_de_compra),
    ("link cru marcado como patrocinado", "gondola-veneza", link_cru_patrocinado),
    ("«link de loja em breve»", "gondola-veneza", link_de_loja_em_breve),
    ("tabela de casos resolvidos recolhida", "gondola-veneza", tabela_recolhida),
    ("tabela sem o grupo de 6", "gondola-veneza", tabela_sem_o_seis),
    ("linha de tabela com preço e sem data", "gondola-veneza",
     linha_de_tabela_sem_data),
    ("JSON-LD sem BreadcrumbList", "gondola-veneza", json_ld_sem_trilha),
    ("JSON-LD sem Article", "gondola-veneza", json_ld_sem_article),
    ("pergunta do FAQ sem resposta", "gondola-veneza", faq_sem_resposta),
    ("FAQ todo respondido pela mesma frase", "gondola-veneza",
     faq_todo_da_mesma_frase),
    ("FAQ sem dizer de onde sai a resposta", "gondola-veneza",
     faq_sem_dizer_de_onde),
    ("publicar marcado sem site para publicar", "gondola-veneza",
     publicar_sem_site),
    ("data no slug", "gondola-veneza", data_no_slug),
    ("URL do guia fora da mãe", "gondola-veneza", url_fora_da_mae),
    ("divergência sem o publicador na frase", "gondola-veneza",
     divergencia_sem_publicador),
    ("divergência sem a data da leitura", "gondola-veneza", divergencia_sem_data),
    ("fim de funil com link de aluguel de carro", "gondola-veneza",
     fim_de_funil_com_carro),
    ("início de funil com link de experiência", "gondola-veneza",
     inicio_de_funil_com_experiencia),
    ("acentuação corrompida na tela", "gondola-veneza", acentuacao_corrompida),
    ("ressalva de registro pendente sumida", "angkor-pass",
     ressalva_de_pendente_sumida),
    ("preço de registro pendente na description", "angkor-pass",
     preco_pendente_na_description),
    ("preço trocado a mão na Torre Eiffel", "torre-eiffel", preco_trocado),
    ("preço trocado a mão no Coliseu", "coliseu-roma", preco_trocado),
]


# --- as quebras do CONJUNTO, que nenhum artigo sozinho acusa ---------------

def janela_fixa(docs):
    """A quebra que a 16.9(a) existe para pegar.

    Com janela fixa toda pagina lista as MESMAS quatro primeiras irmas: o grau de
    saida continua certo e o de entrada desaba. Portao que conta so o que sai
    fica verde nos dois mundos.
    """
    primeiras = copy.deepcopy(docs[0]["veja_tambem"])
    for d in docs:
        d["veja_tambem"] = copy.deepcopy(primeiras)


def duas_na_mesma_consulta(docs):
    docs[1]["consulta_alvo"] = docs[0]["consulta_alvo"]


def duas_na_mesma_url(docs):
    docs[1]["url_planejada"] = docs[0]["url_planejada"]


def irma_que_nao_existe(docs):
    docs[0]["veja_tambem"][0]["url"] = "/guias/quanto-custa/pagina-que-nao-existe/"


QUEBRAS_DO_CONJUNTO = [
    ("janela de irmãs FIXA em vez de rotacionar", janela_fixa),
    ("duas páginas na mesma consulta-alvo", duas_na_mesma_consulta),
    ("duas páginas na mesma URL", duas_na_mesma_url),
    ("irmã apontada que não existe no conjunto", irma_que_nao_existe),
]


def main():
    docs, falhas = art.todos()
    if falhas:
        print("O MUNDO LIMPO JA ESTA VERMELHO — a bateria não mede nada assim:")
        for f in falhas:
            print("  - [%s] %s :: %s" % (f["artigo"], f["regra"], f["visto"]))
        return 2
    base = {d["id"]: d for d in docs}

    mortes = inertes = reprovas = 0
    for nome, artigo_id, quebra in QUEBRAS:
        d = copy.deepcopy(base[artigo_id])
        quebra(d)
        try:
            vistas = art.conferir(d)
        except Exception as erro:            # noqa: BLE001 — e isto que se mede
            mortes += 1
            print("MORRE    %-46s %s: %s" % (nome, type(erro).__name__, erro))
            continue
        if vistas:
            reprovas += 1
            print("REPROVA  %-46s %s" % (nome, vistas[0]["regra"]))
        else:
            inertes += 1
            print("INERTE   %-46s o portão aprovou o mundo quebrado" % nome)

    for nome, quebra in QUEBRAS_DO_CONJUNTO:
        copias = copy.deepcopy(docs)
        quebra(copias)
        try:
            vistas = art.conferir_o_conjunto(copias)
        except Exception as erro:            # noqa: BLE001
            mortes += 1
            print("MORRE    %-46s %s: %s" % (nome, type(erro).__name__, erro))
            continue
        if vistas:
            reprovas += 1
            print("REPROVA  %-46s %s" % (nome, vistas[0]["regra"]))
        else:
            inertes += 1
            print("INERTE   %-46s o portão aprovou o conjunto quebrado" % nome)

    total = len(QUEBRAS) + len(QUEBRAS_DO_CONJUNTO)
    print("\n%d de %d reprovadas, %d mortes, %d inertes"
          % (reprovas, total, mortes, inertes))
    return 1 if (mortes or inertes) else 0


if __name__ == "__main__":
    sys.exit(main())
