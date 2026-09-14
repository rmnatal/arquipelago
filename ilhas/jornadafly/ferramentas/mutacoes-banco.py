#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra o banco da JornadaFly de proposito e verifica que validar-banco.py reprova.

    python3 ferramentas/mutacoes-banco.py

Sai com codigo 1 se qualquer mutacao decidir errado.

POR QUE ESTE ARQUIVO E MAIS IMPORTANTE AQUI DO QUE NAS ILHAS IRMAS.
O banco desta ilha nasce com UM registro. A secao 8 do ARQUIPELAGO.md ja pagou por
isso duas vezes: "regua escrita para um mundo que nunca aconteceu nasce errada sem
poder falhar", e "verde sobre um mundo de um elemento so nao e medicao; e a ausencia
de contraexemplo confundida com prova". Um validador verde sobre um banco de um item
nao prova nada — ele pode estar tratando o caso unico e ignorando todos os outros que
o esquema permite.

Entao as mutacoes aqui sao de DOIS tipos, e e a existencia dos dois que faz a medicao:

  MUNDOS (esperam PASSAR) — constroem o caso que o banco ainda nao tem e exigem que o
  validador o aprove: preco por pessoa, preco por cabine, escada de dias, preco de
  crianca, temporada preenchida, divergencia SEM autoridade, item com link rastreado.
  Sao a metade que prova que a trava nao esta apenas dizendo nao para tudo. O esquema
  lista esses casos em `o_que_o_esquema_permite_e_o_banco_ainda_nao_tem`, e cada linha
  de la tem mutacao aqui.

  QUEBRAS (esperam REPROVAR) — cada uma ataca uma invariante, e varias delas so podem
  ser atacadas DENTRO de um mundo produzido (a media, por exemplo, so existe onde nao
  ha autoridade — e o banco de hoje so tem experiencia COM autoridade).
"""

import copy
import importlib.util
import json
import os
import sys

FERRAMENTAS = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(FERRAMENTAS)

# O validador tem hifen no nome (convencao das ilhas) e por isso nao e importavel
# por `import`. Carregado pelo caminho, para que a regua medida aqui seja
# exatamente a que roda na bancada — nunca uma copia.
_spec = importlib.util.spec_from_file_location(
    "validar_banco", os.path.join(FERRAMENTAS, "validar-banco.py"))
_validador = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_validador)

validar = _validador.validar


def carregar(nome):
    with open(os.path.join(BASE, "dados", nome), encoding="utf-8") as fh:
        return json.load(fh)


ESQUEMA = carregar("esquema-banco.json")
BANCO = carregar("experiencias.json")
CONSTANTES = carregar("constantes.json")


def sincronizar_resumo(banco):
    """Recomputa o resumo de um mundo recem-construido.

    Nao afrouxa a trava do resumo: ela continua sendo medida pela mutacao
    `resumo digitado`, que grava um numero a mao e tem de reprovar.
    """
    _, _, calculado = validar(ESQUEMA, banco, CONSTANTES)
    banco["resumo"] = calculado
    return banco


# ----------------------------------------------------------------------------
# OS MUNDOS QUE O BANCO AINDA NAO TEM
# ----------------------------------------------------------------------------

def mundo_por_pessoa(banco):
    """Petra: preco POR PESSOA, escada de dias como versoes, preco de crianca,
    temporada preenchida, e divergencia SEM autoridade resolvida pelo MAIOR.

    Os numeros sao inventados de proposito e este mundo NUNCA e gravado em disco:
    ele existe dentro deste processo, por dois milissegundos, para que a regua
    possa errar. Gravar qualquer um deles seria a unica coisa que esta ilha
    considera imperdoavel.
    """
    banco["cidades"].append({
        "id": "petra-teste",
        "nome": "Petra",
        "pais": "Jordânia",
        "moeda_local": "USD",
        "slug_plataforma": "petra",
        "slug_plataforma_conferido_em": "2026-09-14",
    })
    banco["fontes"].append({
        "id": "operador-petra-teste",
        "nivel": 4,
        "origem": "operador-via-busca",
        "leitura": "busca_web",
        "autor": "operador de teste",
        "documento": "ficha de teste",
        "url": None,
        "motivo_sem_url": "mundo de mutacao",
        "data_leitura": "2026-09-14",
    })
    banco["fontes"].append({
        "id": "publicador-petra-teste",
        "nivel": 6,
        "origem": "publicador-editorial",
        "leitura": "busca_web",
        "autor": "publicador de teste",
        "documento": None,
        "motivo_sem_documento": "mundo de mutacao",
        "url": None,
        "motivo_sem_url": "mundo de mutacao",
        "data_leitura": "2026-09-14",
    })

    def versao(vid, rotulo, preco, dias):
        return {
            "id": vid,
            "rotulo": rotulo,
            "preco": preco,
            "moeda": "USD",
            "unidade_de_preco": "por_pessoa",
            "unidade_de_preco_declarada_por": "no_texto_da_fonte",
            "capacidade_maxima": None,
            "capacidade_maxima_declarada_por": None,
            "duracao_minutos": None,
            "motivo_sem_duracao": "ingresso de %d dia(s): a duracao e do passe, nao do passeio." % dias,
            "momento_do_dia": "qualquer",
            "acrescimos": [],
            "inclui": ["entrada no sítio"],
            "nao_inclui": [],
            "nao_inclui_motivo_lista_vazia": "mundo de mutacao",
            "fonte": "operador-petra-teste",
            "data_leitura": "2026-09-14",
            "declarado_como": "US$ %d por pessoa, %d dia(s)" % (preco, dias),
        }

    banco["experiencias"].append({
        "id": "petra-ingresso-teste",
        "nome": "Ingresso de Petra (mundo de mutação)",
        "cidade": "petra-teste",
        "categoria": "ingresso_de_sitio_publico",
        "operador": {"nome": "operador de teste", "tipo": "operador_privado",
                     "url": None, "motivo_sem_url": "mundo de mutacao"},
        "versoes": [versao("um-dia", "1 dia", 70, 1),
                    versao("dois-dias", "2 dias", 75, 2),
                    versao("tres-dias", "3 dias", 80, 3)],
        "temporada": {"alta": "abril a outubro", "baixa": "novembro a março",
                      "fonte": "operador-petra-teste", "data_leitura": "2026-09-14"},
        "faixa_etaria": [{"rotulo": "criança de 2 a 7 anos", "idade_min": 2,
                          "idade_max": 7, "preco": 17, "moeda": "USD",
                          "fonte": "operador-petra-teste", "data_leitura": "2026-09-14"}],
        "imagem": None,
        "motivo_sem_imagem": "mundo de mutacao",
        "declaracoes": [{
            "versao": "um-dia",
            "publicador": "publicador de teste",
            "url": None,
            "motivo_sem_url": "mundo de mutacao",
            "valor": 65,
            "moeda": "USD",
            "unidade_de_preco": "por_pessoa",
            "diz": "US$ 65 por pessoa",
            "data_leitura": "2026-09-14",
            "fonte": "publicador-petra-teste",
            "publicavel_na_tela": True,
        }],
        "resolucao": {
            "versao_resolvida": "um-dia",
            "valor": 70,
            "moeda": "USD",
            "unidade_de_preco": "por_pessoa",
            "por_autoridade": False,
            "fonte": "operador-petra-teste",
            "erro_caro": "subestimar: quem chega com dinheiro a menos perde a experiência na porta",
            "texto": "Sem autoridade, vale o maior: US$ 70.",
        },
        "afiliado": {
            "programa": None,
            "url": "",
            "url_produto": None,
            "motivo_sem_url_produto": "mundo de mutacao",
            "url_busca_produto": "https://civitatis.com/br/petra/",
            "rel": "nofollow noopener",
            "intestavel": False,
        },
        "status": "publicavel",
        "entra_por": "mundo de mutacao",
    })
    return sincronizar_resumo(banco)


def mundo_por_cabine(banco):
    """Ha Long: preco POR CABINE, a unidade que o bloco 2 achou escondida dentro de
    uma lista de precos por pessoa."""
    banco = mundo_por_pessoa(banco)
    exp = copy.deepcopy(banco["experiencias"][-1])
    exp["id"] = "halong-cruzeiro-teste"
    exp["nome"] = "Cruzeiro em Ha Long (mundo de mutação)"
    exp["categoria"] = "atividade_de_operador"
    for v in exp["versoes"]:
        v["unidade_de_preco"] = "por_cabine"
        v["capacidade_maxima"] = 2
        v["capacidade_maxima_declarada_por"] = "no_contraste_da_propria_fonte"
    exp["declaracoes"][0]["unidade_de_preco"] = "por_cabine"
    exp["fontes_proprias"] = None
    del exp["fontes_proprias"]
    exp["resolucao"]["unidade_de_preco"] = "por_cabine"
    banco["experiencias"].append(exp)
    return sincronizar_resumo(banco)


def mundo_com_link_rastreado(banco):
    """Item com link de afiliado encurtado e sem url_produto: e o unico caso em que
    `intestavel` pode ser verdadeiro, e ele nao existe no banco de hoje."""
    exp = banco["experiencias"][0]
    exp["afiliado"]["programa"] = "civitatis"
    exp["afiliado"]["url"] = "https://exemplo-de-mutacao.invalid/abc"
    exp["afiliado"]["url_produto"] = None
    exp["afiliado"]["motivo_sem_url_produto"] = "mundo de mutacao"
    exp["afiliado"]["rel"] = "sponsored noopener"
    exp["afiliado"]["intestavel"] = True
    return sincronizar_resumo(banco)


def mundo_sem_divergencia(banco):
    """Experiencia que ninguem mais publicou: declaracoes vazia E sem resolucao.
    Lista vazia e afirmacao, nao lacuna — e tem de passar."""
    exp = banco["experiencias"][0]
    exp["declaracoes"] = []
    exp.pop("resolucao", None)
    # As tres fontes editoriais so existiam para sustentar as declaracoes. Sem elas
    # viram fonte orfa, e fonte orfa e erro duro — de proposito: dado colhido que a
    # tela nunca usa e a outra direcao do numero digitado (secao 8).
    usadas = {v["fonte"] for e in banco["experiencias"] for v in e["versoes"]}
    banco["fontes"] = [f for f in banco["fontes"] if f["id"] in usadas]
    return sincronizar_resumo(banco)


# ----------------------------------------------------------------------------
# AS QUEBRAS
# ----------------------------------------------------------------------------

def q_preco_sem_data(banco):
    del banco["experiencias"][0]["versoes"][0]["data_leitura"]
    return banco


def q_divergencia_sem_resolucao(banco):
    del banco["experiencias"][0]["resolucao"]
    return banco


def q_resolucao_sem_erro_caro(banco):
    del banco["experiencias"][0]["resolucao"]["erro_caro"]
    return banco


def _petra_com_dois_divergentes(banco, preco_resolvido):
    """Mundo de Petra com DUAS declaracoes sobre a MESMA versao (65 e 80) e o preco
    da versao de um dia em `preco_resolvido`.

    A quebra da media so existe assim, e descobrir isso foi o achado da bancada: com
    UMA declaracao, o preco da versao e sempre um extremo do conjunto e nenhuma media
    e construivel. E preciso um desacordo dos DOIS lados para que exista um meio onde
    se esconder.
    """
    banco = mundo_por_pessoa(banco)
    exp = banco["experiencias"][-1]
    segunda = copy.deepcopy(exp["declaracoes"][0])
    segunda["valor"] = 80
    segunda["diz"] = "US$ 80 por pessoa"
    segunda["publicador"] = "segundo publicador de teste"
    exp["declaracoes"].append(segunda)
    exp["versoes"][0]["preco"] = preco_resolvido
    exp["resolucao"]["valor"] = preco_resolvido
    return sincronizar_resumo(banco)


def q_media(banco):
    """72,5 esta entre os 65 e os 80 declarados e nao e nenhum dos dois. Ninguem a
    chama de media; e a forma que a media tem quando ninguem a chama assim."""
    return _petra_com_dois_divergentes(banco, 72.5)


def q_resolve_pelo_menor(banco):
    """65 e o menor dos tres. O erro caro desta ilha e subestimar."""
    return _petra_com_dois_divergentes(banco, 65)


def q_autoridade_inventada(banco):
    banco["experiencias"][0]["resolucao"]["fonte"] = "eurodicas-gondola"
    return banco


def q_nivel_sem_leitura_direta(banco):
    banco["fontes"][0]["nivel"] = 1
    banco["fontes"][0]["origem"] = "ato-de-poder-publico-lido"
    return banco


def q_origem_trocada(banco):
    banco["fontes"][0]["origem"] = "publicador-editorial"
    return banco


def q_unidade_sem_declarada_por(banco):
    del banco["experiencias"][0]["versoes"][0]["unidade_de_preco_declarada_por"]
    return banco


def q_declarada_por_invalida(banco):
    banco["experiencias"][0]["versoes"][0]["unidade_de_preco_declarada_por"] = "porque_parecia"
    return banco


def q_capacidade_sem_declarada_por(banco):
    banco["experiencias"][0]["versoes"][0]["capacidade_maxima_declarada_por"] = None
    return banco


def _achar(banco, eid):
    return next(e for e in banco["experiencias"] if e["id"] == eid)


def _fonte(banco, fid):
    return next(f for f in banco["fontes"] if f["id"] == fid)


def mundo_autoridade_com_documento_nomeado(banco):
    """O outro lado da regra do documento nomeado, e sem ele a regra nao esta medida.

    O mesmo registro do Angkor, com a fonte citando o ato que a sustenta, tem de
    poder ser `publicavel`. Uma trava que so sabe dizer nao aprovaria igualmente um
    banco em que NADA e publicavel — e o dia em que a busca devolver a tabela de
    tarifa, e este mundo que vira o banco real.
    """
    _fonte(banco, "angkor-enterprise-tarifa-via-busca")["documento"] = \
        "Tabela de tarifas do Angkor Pass publicada pela Angkor Enterprise"
    _achar(banco, "siem-reap-angkor-pass")["status"] = "publicavel"
    return sincronizar_resumo(banco)


def q_autoridade_muda_publicavel(banco):
    """A quebra que a carga de 14/09 pagou para descobrir: autoridade de que so se
    ouviu falar sustentando registro `publicavel`."""
    _achar(banco, "siem-reap-angkor-pass")["status"] = "publicavel"
    return banco


def q_autoridade_muda_na_gondola(banco):
    """A mesma quebra do OUTRO lado do banco, e ela e a que prova que a trava le a
    escada e nao um id: some o ato da gondola e o registro dela, que segue
    `publicavel`, tem de reprovar igual."""
    _fonte(banco, "comune-venezia-tarifa-gondola")["documento"] = None
    _fonte(banco, "comune-venezia-tarifa-gondola")["motivo_sem_documento"] = \
        "apagado de proposito por esta mutacao"
    return banco


def q_esquema_sem_regra_do_documento(banco):
    """A mutacao da secao 26.2 aplicada a regra nova: nao estraga registro nenhum,
    apaga a chave do ESQUEMA. Sem ela o banco de hoje volta a passar com o Angkor
    marcado publicavel, e a trava fica verde sem medir nada."""
    _achar(banco, "siem-reap-angkor-pass")["status"] = "publicavel"
    return banco


def q_esquema_sem_lista_de_origem(banco):
    """A mutacao da secao 26.2: nao estraga registro nenhum, apaga a chave do
    ESQUEMA. Regua que le a propria lista de um arquivo de dados aprova tudo, em
    silencio, no dia em que o arquivo perder a chave."""
    return banco


def q_esquema_sem_escada(banco):
    return banco


def q_esquema_sem_molde(banco):
    return banco


def q_item_sem_piso(banco):
    del banco["experiencias"][0]["afiliado"]["url_busca_produto"]
    return banco


def q_piso_digitado(banco):
    banco["experiencias"][0]["afiliado"]["url_busca_produto"] = "https://civitatis.com/br/venezia/"
    return banco


def q_url_de_afiliado_ausente(banco):
    del banco["experiencias"][0]["afiliado"]["url"]
    return banco


def q_sponsored_sem_programa(banco):
    banco["experiencias"][0]["afiliado"]["rel"] = "sponsored noopener"
    return banco


def q_intestavel_errado(banco):
    banco["experiencias"][0]["afiliado"]["intestavel"] = True
    return banco


def q_declaracao_sem_versao_usada_na_conta(banco):
    """A quebra que o achado desta bancada criou: a declaracao de 65 e de UM dia, e
    aqui ela e atribuida a versao de TRES dias. A resolucao continua em 70, que agora
    e menor que o 80 da versao apontada — a conta passa a comparar dois produtos."""
    banco = mundo_por_pessoa(banco)
    banco["experiencias"][-1]["declaracoes"][0]["versao"] = "tres-dias"
    banco["experiencias"][-1]["resolucao"]["versao_resolvida"] = "tres-dias"
    return banco


def q_declaracao_com_versao_inexistente(banco):
    banco["experiencias"][0]["declaracoes"][0]["versao"] = "vespertino"
    return banco


def q_declaracao_sem_versao_e_sem_motivo(banco):
    del banco["experiencias"][0]["declaracoes"][0]["motivo_sem_versao"]
    return banco


def q_declaracao_sem_campo_versao(banco):
    del banco["experiencias"][0]["declaracoes"][0]["versao"]
    del banco["experiencias"][0]["declaracoes"][0]["motivo_sem_versao"]
    return banco


def q_declaracao_sem_dono_publicavel(banco):
    banco["experiencias"][0]["declaracoes"][2]["publicavel_na_tela"] = True
    return banco


def q_declaracao_sem_publicador_e_sem_motivo(banco):
    del banco["experiencias"][0]["declaracoes"][2]["motivo_sem_publicador"]
    return banco


def q_faixa_etaria_sem_motivo(banco):
    del banco["experiencias"][0]["motivo_sem_faixa_etaria"]
    return banco


def q_temporada_sem_motivo(banco):
    del banco["experiencias"][0]["motivo_sem_temporada"]
    return banco


def q_lista_vazia_sem_motivo(banco):
    del banco["experiencias"][0]["versoes"][0]["inclui_motivo_lista_vazia"]
    return banco


def q_capacidade_nula_em_por_veiculo(banco):
    banco["experiencias"][0]["versoes"][0]["capacidade_maxima"] = None
    banco["experiencias"][0]["versoes"][0]["capacidade_maxima_declarada_por"] = None
    return banco


def q_aproximado_virou_numero_seco(banco):
    del banco["experiencias"][0]["versoes"][0]["acrescimos"][0]["aproximado"]
    return banco


def q_ressalva_inventada(banco):
    banco["experiencias"][0]["versoes"][0]["acrescimos"][0]["declarado_como"] = "€40 a cada 20 minutos adicionais"
    return banco


def q_moeda_convertida(banco):
    banco["experiencias"][0]["versoes"][0]["moeda"] = "BRL_do_operador"
    return banco


def q_resumo_digitado(banco):
    banco["resumo"]["versoes"] = 7
    return banco


def q_resumo_com_numero_que_ninguem_refaz(banco):
    banco["resumo"]["paginas_previstas"] = 12
    return banco


def q_cidade_inexistente(banco):
    banco["experiencias"][0]["cidade"] = "veneza-que-nao-existe"
    return banco


def q_fonte_orfa(banco):
    banco["fontes"].append({
        "id": "fonte-que-ninguem-usa",
        "nivel": 6,
        "origem": "publicador-editorial",
        "leitura": "busca_web",
        "autor": "ninguem",
        "documento": None,
        "motivo_sem_documento": "mundo de mutacao",
        "url": None,
        "motivo_sem_url": "mundo de mutacao",
        "data_leitura": "2026-09-14",
    })
    banco["resumo"]["fontes"] = 5
    return banco


def q_frase_proibida(banco):
    banco["experiencias"][0]["afiliado"]["motivo_sem_url_produto"] = "link de loja em breve"
    return banco


def q_versao_repetida(banco):
    versao = copy.deepcopy(banco["experiencias"][0]["versoes"][0])
    banco["experiencias"][0]["versoes"].append(versao)
    banco["resumo"]["versoes"] = 3
    return banco


def q_constante_pendente_usada(banco):
    banco["experiencias"][0]["versoes"][0]["declarado_como"] += \
        " Convertido pela constante cambio-eur-brl."
    return banco


def q_experiencia_sem_versao(banco):
    banco["experiencias"][0]["versoes"] = []
    banco["resumo"]["versoes"] = 0
    return banco


def q_resolucao_de_outra_versao(banco):
    banco["experiencias"][0]["resolucao"]["valor"] = 110
    return banco


# nome, funcao, espera, esquema_mutado
MUTACOES = [
    ("MUNDO preco por pessoa, escada de dias, crianca e temporada", mundo_por_pessoa, "passa", None),
    ("MUNDO preco por cabine", mundo_por_cabine, "passa", None),
    ("MUNDO item com link rastreado e intestavel", mundo_com_link_rastreado, "passa", None),
    ("MUNDO experiencia sem divergencia nenhuma", mundo_sem_divergencia, "passa", None),
    ("MUNDO autoridade COM documento nomeado vira publicavel", mundo_autoridade_com_documento_nomeado, "passa", None),

    ("preco sem data de leitura", q_preco_sem_data, "reprova", None),
    ("divergencia sem resolucao", q_divergencia_sem_resolucao, "reprova", None),
    ("resolucao sem erro caro nomeado", q_resolucao_sem_erro_caro, "reprova", None),
    ("resolucao pela MEDIA (sem autoridade)", q_media, "reprova", None),
    ("resolucao pelo MENOR (sem autoridade)", q_resolve_pelo_menor, "reprova", None),
    ("autoridade inventada sobre fonte editorial", q_autoridade_inventada, "reprova", None),
    ("fonte de nivel 1 lida por busca", q_nivel_sem_leitura_direta, "reprova", None),
    ("origem que nao bate com o nivel", q_origem_trocada, "reprova", None),
    ("unidade de preco sem declarada_por", q_unidade_sem_declarada_por, "reprova", None),
    ("declarada_por fora do vocabulario", q_declarada_por_invalida, "reprova", None),
    ("capacidade maxima sem declarada_por", q_capacidade_sem_declarada_por, "reprova", None),
    ("autoridade sem documento sustentando publicavel", q_autoridade_muda_publicavel, "reprova", None),
    ("a mesma quebra na gondola, para a trava nao ser um id", q_autoridade_muda_na_gondola, "reprova", None),
    ("ESQUEMA sem a regra do documento nomeado", q_esquema_sem_regra_do_documento, "reprova", "sem_regra_documento"),
    ("ESQUEMA sem a lista de campos que exigem origem", q_esquema_sem_lista_de_origem, "reprova", "sem_lista"),
    ("ESQUEMA sem a escada de fontes", q_esquema_sem_escada, "reprova", "sem_escada"),
    ("ESQUEMA sem o molde do piso", q_esquema_sem_molde, "reprova", "sem_molde"),
    ("item sem piso de compra", q_item_sem_piso, "reprova", None),
    ("piso digitado a mao, fora do molde", q_piso_digitado, "reprova", None),
    ("afiliado.url ausente em vez de vazia", q_url_de_afiliado_ausente, "reprova", None),
    ("rel sponsored sem programa cadastrado", q_sponsored_sem_programa, "reprova", None),
    ("intestavel gravado ao contrario da derivacao", q_intestavel_errado, "reprova", None),
    ("declaracao atribuida a versao errada da escada", q_declaracao_sem_versao_usada_na_conta, "reprova", None),
    ("declaracao apontando versao inexistente", q_declaracao_com_versao_inexistente, "reprova", None),
    ("declaracao com versao null e sem motivo", q_declaracao_sem_versao_e_sem_motivo, "reprova", None),
    ("declaracao sem o campo versao", q_declaracao_sem_campo_versao, "reprova", None),
    ("declaracao sem dono marcada como publicavel", q_declaracao_sem_dono_publicavel, "reprova", None),
    ("publicador null sem motivo", q_declaracao_sem_publicador_e_sem_motivo, "reprova", None),
    ("faixa_etaria null sem motivo", q_faixa_etaria_sem_motivo, "reprova", None),
    ("temporada null sem motivo", q_temporada_sem_motivo, "reprova", None),
    ("lista inclui vazia sem motivo", q_lista_vazia_sem_motivo, "reprova", None),
    ("capacidade null com unidade por veiculo", q_capacidade_nula_em_por_veiculo, "reprova", None),
    ("'cerca de' virando numero seco", q_aproximado_virou_numero_seco, "reprova", None),
    ("ressalva inventada onde a fonte nao ressalvou", q_ressalva_inventada, "reprova", None),
    ("preco convertido para moeda que nao e a do operador", q_moeda_convertida, "reprova", None),
    ("resumo digitado diferente da contagem", q_resumo_digitado, "reprova", None),
    ("resumo com numero que ninguem recomputa", q_resumo_com_numero_que_ninguem_refaz, "reprova", None),
    ("experiencia apontando cidade inexistente", q_cidade_inexistente, "reprova", None),
    ("fonte colhida que o banco nunca usa", q_fonte_orfa, "reprova", None),
    ("frase proibida dentro do banco", q_frase_proibida, "reprova", None),
    ("id de versao repetido", q_versao_repetida, "reprova", None),
    ("constante pendente citada no banco", q_constante_pendente_usada, "reprova", None),
    ("experiencia sem nenhuma versao", q_experiencia_sem_versao, "reprova", None),
    ("resolucao com o preco de OUTRA versao", q_resolucao_de_outra_versao, "reprova", None),
]


def esquema_para(mutacao):
    esquema = copy.deepcopy(ESQUEMA)
    if mutacao == "sem_regra_documento":
        del esquema["regra_do_documento_nomeado"]
    elif mutacao == "sem_lista":
        del esquema["campos_que_exigem_declaracao_de_origem"]["campos"]
    elif mutacao == "sem_escada":
        del esquema["escada_de_fontes"]["niveis"]
    elif mutacao == "sem_molde":
        del esquema["piso_de_compra"]["molde"]
    return esquema


def main():
    # Antes de tudo: o banco de verdade tem de passar. Mutacao sobre banco ja
    # vermelho nao mede nada.
    erros, _, _ = validar(ESQUEMA, copy.deepcopy(BANCO), CONSTANTES)
    if erros:
        print("O BANCO REAL JA ESTA REPROVADO — nenhuma mutacao mede nada assim:")
        for e in erros:
            print("  - %s" % e)
        sys.exit(1)

    falhas = []
    for nome, funcao, espera, mut_esquema in MUTACOES:
        banco = funcao(copy.deepcopy(BANCO))
        esquema = esquema_para(mut_esquema)
        erros, _, _ = validar(esquema, banco, CONSTANTES)
        decidiu = "reprova" if erros else "passa"
        marca = "ok " if decidiu == espera else "NAO"
        if decidiu != espera:
            falhas.append((nome, espera, decidiu, erros))
        print("  %s  %-52s espera %-7s deu %s" % (marca, nome[:52], espera, decidiu))

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
