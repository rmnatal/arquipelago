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
            # O EIXO e os DIAS DE USO nasceram em 22/10/2026, no bloco 4. Petra e um
            # eixo `por_quantidade` desde que este mundo foi escrito — a escada de dias
            # e exatamente o que ele fabrica —, so que a quantidade vivia na PROSA do
            # rotulo. Agora e campo, e o `declarado_como` acima a declara em digito.
            "dias_de_uso": dias,
            "dias_de_uso_transcrito_de": "a frase `declarado_como` deste mundo de mutacao, "
                                         "que escreve o numero de dias em digito.",
            # A faixa etaria desceu para a VERSAO em 22/10/2026. O mundo acompanhou: as
            # tres versoes declaram a MESMA faixa, com a MESMA frase, porque a fonte foi
            # lida uma vez — e e exatamente isso que a regua das irmas cobra.
            "faixa_etaria": [{"rotulo": "crianca de 2 a 7 anos", "idade_min": 2,
                              "idade_max": 7, "preco": 17, "moeda": "USD",
                              "condicao": None,
                              "motivo_sem_condicao": "mundo de mutacao",
                              "se_nao_cumprir": None,
                              "motivo_sem_se_nao_cumprir": "mundo de mutacao",
                              "declarado_como": "US$ 17 por crianca de 2 a 7 anos",
                              "fonte": "operador-petra-teste",
                              "data_leitura": "2026-09-14"}],
            "faixas_que_a_fonte_declara_e_a_leitura_nao_transcreveu": [],
        }

    banco["experiencias"].append({
        "id": "petra-ingresso-teste",
        "nome": "Ingresso de Petra (mundo de mutação)",
        "cidade": "petra-teste",
        "categoria": "ingresso_de_sitio_publico",
        "eixo_das_versoes": "por_quantidade",
        "nota_do_eixo_das_versoes": "As tres versoes sao MAIS DA MESMA COISA: 1, 2 e 3 dias "
                                    "de entrada no mesmo sitio. E o mundo que exercita a Conta "
                                    "3 da F1 com tres degraus, que o banco real nao tem.",
        "operador": {"nome": "operador de teste", "tipo": "operador_privado",
                     "url": None, "motivo_sem_url": "mundo de mutacao"},
        "versoes": [versao("um-dia", "1 dia", 70, 1),
                    versao("dois-dias", "2 dias", 75, 2),
                    versao("tres-dias", "3 dias", 80, 3)],
        "temporada": {"alta": "abril a outubro", "baixa": "novembro a março",
                      "fonte": "operador-petra-teste", "data_leitura": "2026-09-14"},
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


# ---------------------------------------------------------------------------
# A ESCADA SABER DE SI MESMA — mutacoes de 15/09/2026, com a carga do Coliseu e
# da Torre Eiffel. `existe_hoje` era prosa do esquema que nenhuma regua
# recomputava, e a carga que o moveu (nivel 4 de false para true) e exatamente a
# ocasiao em que um campo desses envelhece calado.
# ---------------------------------------------------------------------------

def mundo_degrau_novo_alcancado(banco):
    """O lado que tem de PASSAR: um degrau que o banco nao pisava passa a ter fonte,
    e o esquema e atualizado junto. Sem este mundo a trava so saberia dizer nao, e
    uma trava assim aprovaria um esquema em que NENHUM degrau existe."""
    banco["fontes"].append({
        "id": "plataforma-lida-na-propria-plataforma",
        "nivel": 5,
        "origem": "plataforma",
        "leitura": "busca_web",
        "autor": "plataforma de reserva, lida na propria plataforma",
        "documento": "pagina de produto da plataforma",
        "url": None,
        "motivo_sem_url": "mundo produzido por mutacao",
        "data_leitura": "2026-09-15",
    })
    # e a fonte tem de ser USADA: fonte colhida que ninguem usa ja e reprovada por
    # outra trava, e mundo que reprova por trava alheia nao mede a sua.
    _achar(banco, "roma-coliseu-ingresso")["versoes"][1]["fonte"] = \
        "plataforma-lida-na-propria-plataforma"
    return sincronizar_resumo(banco)


def q_degrau_alcancado_declarado_inexistente(banco):
    """O `false` velho, que e a direcao SILENCIOSA do defeito: a ilha nega um degrau
    que ja alcancou, e nada no banco contradiz a frase."""
    return banco


def q_degrau_inexistente_declarado_alcancado(banco):
    """A outra direcao: o esquema promete um degrau que nenhuma fonte pisa."""
    return banco


def q_degrau_sem_o_campo(banco):
    """Apagar a chave do ESQUEMA (secao 26.2). Regua que le `existe_hoje` do esquema
    fica sem o que comparar e nao pode aprovar em silencio."""
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
    # A gondola: faixa null porque a tarifa e pela embarcacao. Sem o motivo, a lacuna
    # vira muda. Aponta para a VERSAO desde 22/10/2026 — o campo desceu.
    del banco["experiencias"][0]["versoes"][0]["motivo_sem_faixa_etaria"]
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


# ----------------------------------------------------------------------------
# AS QUEBRAS DA FAIXA ETARIA NA VERSAO (migracao de 22/10/2026)
# Cada uma ataca uma invariante que SO existe depois de o campo descer: com
# `faixa_etaria` na EXPERIENCIA nao havia versao irma para comparar, nem
# `unidade_de_preco` no mesmo objeto para proibir a faixa.
# ----------------------------------------------------------------------------

def _gondola(banco):
    return banco["experiencias"][0]


def _angkor(banco):
    return banco["experiencias"][1]


def _torre(banco):
    return banco["experiencias"][3]


def q_faixa_em_unidade_por_veiculo(banco):
    """A prosa da gondola virou regra: 6 pessoas sao DUAS gondolas, a crianca nao tem
    preco, tem assento. Antes de 22/10 esta quebra nao tinha onde morder."""
    v = _gondola(banco)["versoes"][0]
    del v["motivo_sem_faixa_etaria"]
    v["faixa_etaria"] = [{"rotulo": "crianca de 2 a 7 anos", "preco": 0, "moeda": "EUR",
                          "condicao": None, "motivo_sem_condicao": "quebra",
                          "se_nao_cumprir": None, "motivo_sem_se_nao_cumprir": "quebra",
                          "declarado_como": "crianca nao paga",
                          "fonte": "comune-venezia-tarifa-gondola",
                          "data_leitura": "2026-09-14"}]
    v["faixas_que_a_fonte_declara_e_a_leitura_nao_transcreveu"] = []
    return banco


def q_faixa_em_outra_moeda(banco):
    _torre(banco)["versoes"][0]["faixa_etaria"][1]["moeda"] = "USD"
    return banco


def q_faixa_mais_cara_que_o_bilhete(banco):
    """Faixa a 99 EUR num bilhete de 14,80: nao e faixa, e numero no campo errado."""
    _torre(banco)["versoes"][0]["faixa_etaria"][1]["preco"] = 99
    return banco


def q_faixa_da_irma_desaparece_calada(banco):
    """A Torre Eiffel perde a contagem da lacuna: as duas colunas do meio voltam a ser
    ausencia silenciosa, indistinguivel de 'o operador nao cobra faixa neste bilhete'.
    E o defeito que a migracao existe para tornar visivel."""
    _torre(banco)["versoes"][1]["faixas_que_a_fonte_declara_e_a_leitura_nao_transcreveu"] = []
    return banco


def q_lacuna_sem_causa(banco):
    del _torre(banco)["versoes"][1]["faixas_que_a_fonte_declara_e_a_leitura_nao_transcreveu"][0]["por_que"]
    return banco


def q_faixa_sem_a_lista_de_lacuna(banco):
    del _torre(banco)["versoes"][1]["faixas_que_a_fonte_declara_e_a_leitura_nao_transcreveu"]
    return banco


def q_mesma_faixa_com_duas_frases(banco):
    """A gratuidade dos menores de 4 anos vale igual nos quatro bilhetes e foi lida uma
    vez. Transcrita com duas frases, uma delas e da ilha e nao do operador."""
    _torre(banco)["versoes"][1]["faixa_etaria"][0]["declarado_como"] = \
        "Menores de 4 anos nao pagam neste bilhete."
    return banco


def q_frase_com_preco_de_outra_versao(banco):
    """O achado da migracao: a fonte do Angkor escreve US$ 37, que e o passe de UM DIA, e
    a frase estava guardada num campo que valia para os tres passes."""
    del _angkor(banco)["versoes"][1]["faixa_etaria"][0]["numero_da_frase_e_de_outra_versao"]
    return banco


def q_faixa_sem_preco_e_sem_motivo(banco):
    _torre(banco)["versoes"][0]["faixa_etaria"][1]["preco"] = None
    return banco


def q_faixa_sem_declarado_como(banco):
    del _torre(banco)["versoes"][0]["faixa_etaria"][1]["declarado_como"]
    return banco


def q_faixa_sem_data_de_leitura(banco):
    del _torre(banco)["versoes"][0]["faixa_etaria"][1]["data_leitura"]
    return banco


def q_faixa_com_fonte_inexistente(banco):
    _torre(banco)["versoes"][0]["faixa_etaria"][1]["fonte"] = "fonte-que-nao-existe"
    return banco


def q_faixa_volta_para_a_experiencia(banco):
    """A regressao que a regua existe para impedir: o campo de volta na entidade de onde
    saiu, publicando um preco so para quatro bilhetes que cobram diferente."""
    _torre(banco)["faixa_etaria"] = [{"rotulo": "crianca de 4 a 11 anos", "preco": 3.8,
                                      "moeda": "EUR"}]
    return banco


def q_rotulo_de_faixa_repetido(banco):
    v = _torre(banco)["versoes"][0]
    v["faixa_etaria"].append(copy.deepcopy(v["faixa_etaria"][1]))
    return banco


def q_resumo_de_faixa_digitado(banco):
    banco["resumo"]["faixas_etarias"] = 11 + 1
    return banco


def q_resumo_de_lacuna_digitado(banco):
    banco["resumo"]["faixas_declaradas_nao_transcritas"] = 0
    return banco


def mundo_faixa_sem_preco_declarado(banco):
    """O caso que o esquema permite e o banco nao tem: faixa que a fonte NOMEIA sem dizer
    o preco. Tem de PASSAR com o motivo escrito — nomear a faixa e dado sobre a fonte."""
    v = _torre(banco)["versoes"][1]
    v["faixa_etaria"].append({
        # O rotulo tem de ser o MESMO das versoes irmas, acento incluido: e o rotulo que
        # liga a mesma faixa entre bilhetes, e a primeira versao deste mundo o escreveu
        # sem cedilha — a regua das irmas reprovou tres versoes de uma vez e foi assim
        # que o erro apareceu.
        "rotulo": "criança de 4 a 11 anos",
        "preco": None,
        "motivo_sem_preco": "a grade nomeia a faixa nesta coluna e esta leitura nao "
                            "transcreveu o valor dela",
        "moeda": "EUR",
        "condicao": None,
        "motivo_sem_condicao": "mundo de mutacao",
        "se_nao_cumprir": None,
        "motivo_sem_se_nao_cumprir": "mundo de mutacao",
        "declarado_como": "Criancas de 4 a 11 anos: tarifa reduzida.",
        "fonte": "sete-toureiffel-tarifa-via-busca",
        "data_leitura": "2026-09-15",
    })
    v["faixas_que_a_fonte_declara_e_a_leitura_nao_transcreveu"] = [
        e for e in v["faixas_que_a_fonte_declara_e_a_leitura_nao_transcreveu"]
        if e["rotulo"] != "criança de 4 a 11 anos"]
    return sincronizar_resumo(banco)



# ---------------------------------------------------------------------------
# O EIXO DAS VERSOES E OS DIAS DE USO (nasceram em 22/10/2026, no bloco 4)
#
# Tres MUNDOS aqui sao mundos que o esquema PERMITE e o banco nao tem, e os tres
# existem porque a Conta 3 da F1 e uma recusa que depende de uma RELACAO entre as
# versoes — quantas sao, se os precos empatam, se ha quantidade. A secao 8 do
# ARQUIPELAGO.md diz que recusa assim mora numa funcao pura que recebe a relacao
# ja calculada, justamente para que a bancada possa fabricar o mundo sem fabricar
# um banco falso. Estes tres fabricam o mundo pelo banco; a bancada da F1
# (mutacoes-f1.py) chama a funcao pura direto, com empate, com lista vazia e com
# uma versao so. Sao as duas metades do mesmo cuidado.
# ---------------------------------------------------------------------------

def mundo_eixo_de_quantidade_com_uma_versao_so(banco):
    """Eixo `por_quantidade` com UMA versao: nao ha com que comparar.

    O esquema permite, e o banco nunca teve: tem de PASSAR na regua do banco (o
    campo esta correto) e a F1 e quem diz que nao ha equilibrio a calcular.
    """
    banco = mundo_por_pessoa(banco)
    exp = _achar(banco, "petra-ingresso-teste")
    exp["versoes"] = exp["versoes"][:1]
    exp["declaracoes"] = [d for d in exp["declaracoes"] if d.get("versao") == exp["versoes"][0]["id"]]
    exp["resolucao"]["versao_resolvida"] = exp["versoes"][0]["id"]
    exp["resolucao"]["valor"] = exp["versoes"][0]["preco"]
    return sincronizar_resumo(banco)


def mundo_eixo_de_quantidade_com_empate_de_preco(banco):
    """Duas quantidades diferentes pelo MESMO preco: a mais cara nao existe.

    Mesma familia do empate no topo que o Clube do Mosaico pagou em 08/10/2026 —
    e a regua do banco tem de aprovar, porque empate de preco nao e defeito de
    dado: e um mundo que o operador pode vender.
    """
    banco = mundo_por_pessoa(banco)
    exp = _achar(banco, "petra-ingresso-teste")
    for v in exp["versoes"]:
        v["preco"] = 70
        v["declarado_como"] = "US$ 70 por pessoa, %d dia(s)" % v["dias_de_uso"]
    exp["resolucao"]["valor"] = 70
    return sincronizar_resumo(banco)


def mundo_eixo_null_com_uma_versao_so(banco):
    """Experiencia de UMA versao: sem duas, nao ha eixo a declarar."""
    banco = mundo_por_pessoa(banco)
    exp = _achar(banco, "petra-ingresso-teste")
    exp["versoes"] = exp["versoes"][:1]
    exp["declaracoes"] = [d for d in exp["declaracoes"] if d.get("versao") == exp["versoes"][0]["id"]]
    exp["resolucao"]["versao_resolvida"] = exp["versoes"][0]["id"]
    exp["resolucao"]["valor"] = exp["versoes"][0]["preco"]
    exp["eixo_das_versoes"] = None
    del exp["nota_do_eixo_das_versoes"]
    exp["motivo_sem_eixo_das_versoes"] = ("Uma versao so: nao ha duas coisas para dizer em que "
                                          "grandeza diferem.")
    for v in exp["versoes"]:
        v["dias_de_uso"] = None
        del v["dias_de_uso_transcrito_de"]
        v["motivo_sem_dias_de_uso"] = "Sem eixo declarado nao ha quantidade a declarar."
    return sincronizar_resumo(banco)


def q_eixo_sem_o_campo(banco):
    del banco["experiencias"][0]["eixo_das_versoes"]
    return banco


def q_eixo_null_com_duas_versoes(banco):
    exp = banco["experiencias"][0]        # a gondola: duas versoes
    exp["eixo_das_versoes"] = None
    del exp["nota_do_eixo_das_versoes"]
    exp["motivo_sem_eixo_das_versoes"] = "mundo de mutacao"
    for v in exp["versoes"]:
        v["dias_de_uso"] = None
        v["motivo_sem_dias_de_uso"] = "mundo de mutacao"
    return banco


def q_eixo_null_sem_motivo(banco):
    exp = banco["experiencias"][0]
    exp["eixo_das_versoes"] = None
    del exp["nota_do_eixo_das_versoes"]
    return banco


def q_eixo_fora_do_vocabulario(banco):
    banco["experiencias"][0]["eixo_das_versoes"] = "por_gosto"
    return banco


def q_eixo_sem_nota(banco):
    del banco["experiencias"][0]["nota_do_eixo_das_versoes"]
    return banco


def q_dias_de_uso_sem_o_campo(banco):
    del _achar(banco, "siem-reap-angkor-pass")["versoes"][0]["dias_de_uso"]
    return banco


def q_dias_de_uso_null_no_eixo_de_quantidade(banco):
    v = _achar(banco, "siem-reap-angkor-pass")["versoes"][1]
    v["dias_de_uso"] = None
    del v["dias_de_uso_transcrito_de"]
    v["motivo_sem_dias_de_uso"] = "mundo de mutacao"
    return banco


def q_dias_de_uso_em_eixo_de_escopo(banco):
    """O defeito que esta regra existe para impedir, e ele e o mais caro dos dois.

    Comprar dois ingressos de 24 horas do Coliseu NAO da a area restrita da
    Experiencia Completa. Com `dias_de_uso` aqui, a F1 publicaria um ponto de
    equilibrio entre bilhetes que nao se substituem: aritmetica certa sobre uma
    pergunta sem sentido.
    """
    v = _achar(banco, "roma-coliseu-ingresso")["versoes"][0]
    v["dias_de_uso"] = 1
    v["dias_de_uso_transcrito_de"] = "mundo de mutacao"
    del v["motivo_sem_dias_de_uso"]
    return banco


def q_dias_de_uso_null_sem_motivo(banco):
    del _achar(banco, "roma-coliseu-ingresso")["versoes"][0]["motivo_sem_dias_de_uso"]
    return banco


def q_dias_de_uso_zero(banco):
    _achar(banco, "siem-reap-angkor-pass")["versoes"][0]["dias_de_uso"] = 0
    return banco


def q_dias_de_uso_sem_transcrito_de(banco):
    del _achar(banco, "siem-reap-angkor-pass")["versoes"][0]["dias_de_uso_transcrito_de"]
    return banco


def q_dias_de_uso_que_a_fonte_nao_declara(banco):
    """O numero trocado sem a frase trocar: a terceira conta da secao 8.

    A versao de 3 dias passa a dizer 4, e o `declarado_como` continua escrevendo
    «US$ 62 para 3 dias». Sem esta trava o campo seria um inteiro digitado por
    quem migrou, com cara de transcrito.
    """
    _achar(banco, "siem-reap-angkor-pass")["versoes"][1]["dias_de_uso"] = 4
    return banco


def _intacto(banco):
    """Banco inteiro, de proposito: a quebra destas quatro esta no ESQUEMA.

    Se a chave sumir do esquema, a regua do campo novo para de existir e TODO
    banco passa, inclusive o proximo. E a trava da secao 26.2 aplicada aos dois
    campos que nasceram em 22/10/2026 — a mesma que a `faixa_etaria` ja tinha.
    """
    return banco


def q_dias_de_uso_achado_dentro_de_outro_numero(banco):
    """A armadilha da vizinhanca, que a secao 8 manda nao usar como criterio.

    A versao de 1 dia passa a dizer 3, e o `declarado_como` dela e «US$ 37 para a
    visitacao de um dia»: o digito 3 ESTA na frase, dentro de «37». Regua que
    procurasse o numero por substring aprovaria isto.
    """
    _achar(banco, "siem-reap-angkor-pass")["versoes"][0]["dias_de_uso"] = 3
    return banco


# nome, funcao, espera, esquema_mutado
MUTACOES = [
    ("MUNDO preco por pessoa, escada de dias, crianca e temporada", mundo_por_pessoa, "passa", None),
    ("MUNDO preco por cabine", mundo_por_cabine, "passa", None),
    ("MUNDO item com link rastreado e intestavel", mundo_com_link_rastreado, "passa", None),
    ("MUNDO experiencia sem divergencia nenhuma", mundo_sem_divergencia, "passa", "degrau_6_negado"),
    ("MUNDO autoridade COM documento nomeado vira publicavel", mundo_autoridade_com_documento_nomeado, "passa", None),
    ("MUNDO degrau novo alcancado, esquema e banco juntos", mundo_degrau_novo_alcancado, "passa", "degrau_5_prometido"),
    ("MUNDO faixa que a fonte NOMEIA sem dizer o preco", mundo_faixa_sem_preco_declarado, "passa", None),
    ("MUNDO eixo de quantidade com UMA versao so", mundo_eixo_de_quantidade_com_uma_versao_so, "passa", None),
    ("MUNDO eixo de quantidade com EMPATE de preco", mundo_eixo_de_quantidade_com_empate_de_preco, "passa", None),
    ("MUNDO eixo null com uma versao so", mundo_eixo_null_com_uma_versao_so, "passa", None),

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
    ("ESCADA nega um degrau que o banco ja alcancou", q_degrau_alcancado_declarado_inexistente, "reprova", "degrau_4_negado", "existe_hoje"),
    ("ESCADA promete um degrau que nenhuma fonte pisa", q_degrau_inexistente_declarado_alcancado, "reprova", "degrau_5_prometido", "existe_hoje"),
    ("ESQUEMA sem o campo existe_hoje no degrau", q_degrau_sem_o_campo, "reprova", "degrau_sem_campo", "sem `existe_hoje`"),
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
    ("faixa_etaria null sem motivo (na VERSAO)", q_faixa_etaria_sem_motivo, "reprova", None),
    ("faixa etaria onde a tarifa e por VEICULO", q_faixa_em_unidade_por_veiculo, "reprova", None, "tem assento"),
    ("faixa em moeda diferente da versao", q_faixa_em_outra_moeda, "reprova", None, "cambio"),
    ("faixa mais cara que o bilhete inteiro", q_faixa_mais_cara_que_o_bilhete, "reprova", None, "campo errado"),
    ("faixa da versao irma desaparecendo calada", q_faixa_da_irma_desaparece_calada, "reprova", None, "Ausencia silenciosa"),
    ("lacuna de faixa contada sem causa nomeada", q_lacuna_sem_causa, "reprova", None, "por_que"),
    ("versao com faixa e sem a lista de lacuna", q_faixa_sem_a_lista_de_lacuna, "reprova", None, "nenhuma falta"),
    ("a mesma faixa transcrita com duas frases", q_mesma_faixa_com_duas_frases, "reprova", None, "nao e da fonte"),
    ("frase da fonte com o preco de OUTRA versao", q_frase_com_preco_de_outra_versao, "reprova", None, "nao disse daquele bilhete"),
    ("faixa com preco null e sem motivo", q_faixa_sem_preco_e_sem_motivo, "reprova", None, "lacuna muda"),
    ("faixa sem declarado_como", q_faixa_sem_declarado_como, "reprova", None, "parafraseia"),
    ("faixa sem data de leitura", q_faixa_sem_data_de_leitura, "reprova", None, "preco de crianca"),
    ("faixa com fonte que nao existe em fontes[]", q_faixa_com_fonte_inexistente, "reprova", None, "nao existe em fontes"),
    ("faixa VOLTANDO para a EXPERIENCIA", q_faixa_volta_para_a_experiencia, "reprova", None, "campo da VERSAO"),
    ("rotulo de faixa repetido na mesma versao", q_rotulo_de_faixa_repetido, "reprova", None, "repetido"),
    ("resumo de faixas digitado a mao", q_resumo_de_faixa_digitado, "reprova", None, "faixas_etarias"),
    ("resumo de lacunas digitado a mao", q_resumo_de_lacuna_digitado, "reprova", None, "faixas_declaradas"),
    ("ESQUEMA sem faixa_etaria na VERSAO", lambda b: b, "reprova", "faixa_sem_campo_na_versao", "proibido_quando"),
    ("ESQUEMA com faixa_etaria de volta na EXPERIENCIA", lambda b: b, "reprova", "faixa_de_volta_na_experiencia", "regressao"),
    ("ESQUEMA sem a entidade FAIXA_ETARIA", lambda b: b, "reprova", "sem_entidade_faixa", "forma declarada"),
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
    ("eixo das versoes sem o campo", q_eixo_sem_o_campo, "reprova", None, "eixo_das_versoes"),
    ("eixo null com DUAS versoes", q_eixo_null_com_duas_versoes, "reprova", None, "null com 2 versoes"),
    ("eixo null sem motivo", q_eixo_null_sem_motivo, "reprova", None, "motivo_sem_eixo_das_versoes"),
    ("eixo fora do vocabulario", q_eixo_fora_do_vocabulario, "reprova", None, "fora do vocabulario"),
    ("eixo sem a nota que o justifica", q_eixo_sem_nota, "reprova", None, "nota_do_eixo_das_versoes"),
    ("dias de uso sem o campo", q_dias_de_uso_sem_o_campo, "reprova", None, "falta o campo `dias_de_uso`"),
    ("dias de uso null no eixo de QUANTIDADE", q_dias_de_uso_null_no_eixo_de_quantidade, "reprova", None, "nao diz QUANTO"),
    ("dias de uso num eixo de ESCOPO", q_dias_de_uso_em_eixo_de_escopo, "reprova", None, "area restrita"),
    ("dias de uso null sem motivo", q_dias_de_uso_null_sem_motivo, "reprova", None, "motivo_sem_dias_de_uso"),
    ("dias de uso zero", q_dias_de_uso_zero, "reprova", None, "inteiro maior que zero"),
    ("dias de uso sem transcrito_de", q_dias_de_uso_sem_transcrito_de, "reprova", None, "dias_de_uso_transcrito_de"),
    ("dias de uso que a FONTE nao declara", q_dias_de_uso_que_a_fonte_nao_declara, "reprova", None, "terceira"),
    ("dias de uso achado DENTRO de outro numero", q_dias_de_uso_achado_dentro_de_outro_numero, "reprova", None, "terceira"),
    ("esquema sem o vocabulario do eixo", _intacto, "reprova", "vocab_sem_eixo",
     "vocabularios.eixo_das_versoes"),
    ("esquema sem o campo eixo na EXPERIENCIA", _intacto, "reprova", "exp_sem_eixo",
     "EXPERIENCIA.campos.eixo_das_versoes"),
    ("esquema sem o campo dias_de_uso na VERSAO", _intacto, "reprova", "versao_sem_dias",
     "VERSAO.campos.dias_de_uso"),
    ("esquema sem o registro da Conta 3", _intacto, "reprova", "sem_registro_conta_3",
     "conta_3_da_F1_exige_EIXO_DECLARADO"),
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
    elif mutacao == "degrau_4_negado":
        for d in esquema["escada_de_fontes"]["niveis"]:
            if d["nivel"] == 4:
                d["existe_hoje"] = False
    elif mutacao == "degrau_5_prometido":
        for d in esquema["escada_de_fontes"]["niveis"]:
            if d["nivel"] == 5:
                d["existe_hoje"] = True
    elif mutacao == "degrau_6_negado":
        # O mundo sem divergencia apaga as fontes editoriais junto com as
        # declaracoes que elas sustentavam. Sem elas o degrau 6 deixa de existir
        # NAQUELE mundo, e o esquema tem de acompanhar — e essa e a regra inteira:
        # `existe_hoje` e derivado do banco, entao mundo que muda as fontes muda o
        # campo junto. Foi a regua nova que descobriu isto, em 15/09/2026, ao
        # reprovar um mundo que passava havia uma carga.
        for d in esquema["escada_de_fontes"]["niveis"]:
            if d["nivel"] == 6:
                d["existe_hoje"] = False
    elif mutacao == "faixa_sem_campo_na_versao":
        # A regra mora no esquema (26.2): sem a chave, a gondola volta a poder ter preco
        # de crianca e a regua fica verde sem medir nada.
        del esquema["entidades"]["VERSAO"]["campos"]["faixa_etaria"]
    elif mutacao == "faixa_de_volta_na_experiencia":
        esquema["entidades"]["EXPERIENCIA"]["campos"]["faixa_etaria"] = {
            "tipo": "lista|null", "obrigatorio": True,
            "null_exige": "motivo_sem_faixa_etaria"}
    elif mutacao == "sem_entidade_faixa":
        del esquema["entidades"]["FAIXA_ETARIA"]
    elif mutacao == "vocab_sem_eixo":
        del esquema["vocabularios"]["eixo_das_versoes"]
    elif mutacao == "exp_sem_eixo":
        del esquema["entidades"]["EXPERIENCIA"]["campos"]["eixo_das_versoes"]
    elif mutacao == "versao_sem_dias":
        del esquema["entidades"]["VERSAO"]["campos"]["dias_de_uso"]
    elif mutacao == "sem_registro_conta_3":
        del esquema["conta_3_da_F1_exige_EIXO_DECLARADO_e_nao_sai_do_rotulo"]
    elif mutacao == "degrau_sem_campo":
        for d in esquema["escada_de_fontes"]["niveis"]:
            if d["nivel"] == 3:
                del d["existe_hoje"]
    elif mutacao is not None:
        # TRAVA DE ALVO EXATO (secao 8 do ARQUIPELAGO.md, corolario de higiene).
        # Antes desta linha, chave desconhecida caia aqui e voltava um esquema
        # INTACTO: a mutacao reprovava por outra trava e o relatorio dizia `ok`.
        # Foi exatamente o que aconteceu em 22/10/2026 com as 13 quebras do eixo,
        # cuja FRASE foi escrita na quarta posicao da tupla — que e esta chave — e
        # nao na quinta. Mutacao que nao morde e teste verde com outro nome, e
        # bateria que nao sabe disso e pior do que bateria que nao existe.
        raise SystemExit(
            "mutacao de esquema desconhecida: %r. Ou a chave foi escrita errada, ou "
            "a FRASE esperada foi posta na QUARTA posicao da tupla (que e o "
            "esquema_mutado) em vez da QUINTA." % mutacao)
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
    com_frase = 0
    for entrada in MUTACOES:
        nome, funcao, espera, mut_esquema = entrada[:4]
        # Quinto elemento, opcional: a FRASE que esta quebra tem de ouvir de volta.
        # Nasceu em 15/09/2026, e o motivo cabe numa linha: reprovar nao e a mesma
        # coisa que reprovar PELO MOTIVO CERTO. Sem isto, uma mutacao pode disparar
        # outra trava, voltar verde e nunca ter medido a sua — que e a forma de
        # mutacao inerte mais dificil de ver, porque o relatorio fica todo `ok`.
        frase = entrada[4] if len(entrada) > 4 else None
        banco = funcao(copy.deepcopy(BANCO))
        esquema = esquema_para(mut_esquema)
        erros, _, _ = validar(esquema, banco, CONSTANTES)
        decidiu = "reprova" if erros else "passa"
        marca = "ok " if decidiu == espera else "NAO"
        if decidiu != espera:
            falhas.append((nome, espera, decidiu, erros))
        elif frase is not None:
            com_frase += 1
            if not any(frase in e for e in erros):
                marca = "NAO"
                falhas.append((nome + " (reprovou, mas nao pela frase %r)" % frase,
                               espera, decidiu, erros))
        print("  %s  %-52s espera %-7s deu %s" % (marca, nome[:52], espera, decidiu))

    mundos = sum(1 for m in MUTACOES if m[2] == "passa")
    quebras = len(MUTACOES) - mundos
    print("\n%d mutacoes: %d mundos que tem de PASSAR e %d quebras que tem de REPROVAR."
          % (len(MUTACOES), mundos, quebras))
    print("%d delas declaram a FRASE que esperam ouvir de volta, e foram cobradas por ela."
          % com_frase)

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
