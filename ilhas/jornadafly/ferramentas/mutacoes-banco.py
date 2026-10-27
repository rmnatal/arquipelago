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
            "elegibilidade": None,
            "motivo_sem_elegibilidade": "mundo de mutacao: a fonte de bancada nao declara tarifa por residencia nem nacionalidade.",
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
    # QUAIS FONTES CONTINUAM USADAS — e esta conta estava INCOMPLETA, o que so deu
    # para ver em 27/10/2026, com a carga do Bondinho. Ela olhava apenas `versao.fonte`,
    # e por isso podava fonte que uma DECLARACAO, uma FAIXA ETARIA, uma ELEGIBILIDADE
    # ou a RESOLUCAO de outra experiencia ainda referencia — derrubando este mundo por
    # fonte orfa que nao era orfa. O Bondinho e a primeira experiencia deste banco cujas
    # declaracoes se apoiam numa fonte que NENHUMA versao usa (o blog do proprio
    # operador, que discorda da pagina de bilhete dele), e foi ela que expos a conta
    # pela metade. Agora a conta varre todo lugar do banco que aponta para uma fonte.
    usadas = set()
    for e in banco["experiencias"]:
        for v in e["versoes"]:
            usadas.add(v.get("fonte"))
            for lista in ("faixa_etaria", "elegibilidade"):
                for item in (v.get(lista) or []):
                    usadas.add(item.get("fonte"))
        for dec in (e.get("declaracoes") or []):
            usadas.add(dec.get("fonte"))
        if isinstance(e.get("resolucao"), dict):
            usadas.add(e["resolucao"].get("fonte"))
    for lista in ("faixas_diarias", "coberturas_de_passe"):
        for item in (banco.get(lista) or []):
            usadas.add(item.get("fonte"))
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
# ---------------------------------------------------------------------------
# A FAIXA_DIARIA — a entidade que nasceu em 22/10/2026 para a F2
#
# O banco tem ZERO faixas, entao sem estas mutacoes as regras que o validador ganhou
# hoje NUNCA SERIAM EXECUTADAS por ninguem: regua que nao falhou porque nao rodou e o
# defeito que fez nascer o descobridor de portoes na aquametria. Os numeros 203.87 e
# 396.84 sao os dois que o bloco 1 mediu na mesma pagina de resultados, em 14/09/2026,
# e estao aqui porque sao o caso que a regra existe para tratar.
# ---------------------------------------------------------------------------

def _faixa_de_bancada(**campos):
    base = {
        "id": "bancada-hospedagem",
        "cidade": "veneza",
        "categoria_de_custo": "hospedagem",
        "padrao": "economico",
        "valor_min": 100,
        "valor_max": 150,
        "moeda": "EUR",
        "base": "por_pessoa_por_dia",
        "base_transcrita_de": "valor por pessoa, por dia",
        "pessoas_por_quarto": None,
        "o_que_o_numero_e": "faixa_publicada",
        "metodo_declarado": "de 100 a 150 euros por pessoa por dia",
        "publicado_por": "Publicador de bancada",
        "url": "https://exemplo.invalido/bancada",
        "data_leitura": "2026-09-14",
        "status": "publicavel",
    }
    base.update(campos)
    return base


def _com_faixas(banco, faixas):
    banco["faixas_diarias"] = faixas
    banco["resumo"]["faixas_diarias"] = len(faixas)
    banco["resumo"]["faixas_diarias_publicaveis"] = sum(
        1 for f in faixas if f.get("status") == "publicavel")
    return banco


def mundo_faixa_por_pessoa(banco):
    """Uma faixa publicavel completa. O banco de hoje nao tem nenhuma."""
    return _com_faixas(banco, [_faixa_de_bancada()])


def mundo_faixa_de_quarto_com_ocupacao(banco):
    """Diaria de quarto duplo com a ocupacao TRANSCRITA da frase da fonte."""
    return _com_faixas(banco, [_faixa_de_bancada(
        id="bancada-quarto", base="por_quarto_por_dia", pessoas_por_quarto=2,
        base_transcrita_de="diaria de quarto duplo, para 2 pessoas",
        metodo_declarado="diaria de quarto duplo entre 100 e 150 euros")])


def mundo_faixa_de_quarto_com_ocupacao_por_extenso(banco):
    """A ocupacao declarada POR EXTENSO na frase: «quarto para duas pessoas».

    O validador confere em palavra inteira e aceita digito ou extenso, igual ao
    `dias_de_uso`. Este mundo e o lado do extenso, que o banco nao tem como produzir.
    """
    return _com_faixas(banco, [_faixa_de_bancada(
        id="bancada-quarto-extenso", base="por_quarto_por_dia", pessoas_por_quarto=2,
        base_transcrita_de="diaria de quarto para duas pessoas",
        metodo_declarado="diaria de quarto duplo entre 100 e 150 euros")])


def mundo_faixa_de_quarto_sem_ocupacao_COM_motivo(banco):
    """Sem ocupacao mas COM o motivo escrito: o banco aceita, e a F2 recusa a linha.

    Sao as duas metades da mesma honestidade: o banco guarda o que foi lido, a
    ferramenta e quem se nega a escalar o numero.
    """
    return _com_faixas(banco, [_faixa_de_bancada(
        id="bancada-quarto-cego", base="por_quarto_por_dia", pessoas_por_quarto=None,
        base_transcrita_de="diaria de quarto",
        motivo_sem_pessoas_por_quarto=(
            "A fonte publica a diaria do quarto e nao diz quantas pessoas ele cobre. "
            "Supor dois seria escolher a ocupacao no lugar de quem publicou o preco."),
        metodo_declarado="diaria de quarto entre 100 e 150 euros")])


def mundo_duas_naturezas_de_numero(banco):
    """O CASO MEDIDO: uma media e um minimo na mesma cidade, categoria e padrao.

    Isto NAO e erro de banco — as duas podem ser verdadeiras —, e por isso o validador
    responde com AVISO. Quem se nega a somar e a F2.
    """
    return _com_faixas(banco, [
        _faixa_de_bancada(id="bancada-media", valor_min=203.87, valor_max=203.87,
                          o_que_o_numero_e="media_de_periodo",
                          publicado_por="Publicador da media",
                          metodo_declarado="media de 203,87 nos ultimos 30 dias"),
        _faixa_de_bancada(id="bancada-minimo", valor_min=396.84, valor_max=396.84,
                          o_que_o_numero_e="menor_encontrado",
                          publicado_por="Publicador do minimo",
                          metodo_declarado="a diaria mais baixa encontrada foi 396,84"),
    ])


def mundo_faixa_sem_url_COM_motivo(banco):
    """Sem endereco mas com o motivo, como a tarifa da gondola fez com a FONTE."""
    return _com_faixas(banco, [_faixa_de_bancada(
        url=None,
        motivo_sem_url=("A pagina foi lida por busca e o endereco exato nao ficou "
                        "registrado. O publicador esta nomeado e a data esta gravada."))])


def q_faixa_sem_publicado_por(banco):
    return _com_faixas(banco, [_faixa_de_bancada(publicado_por="")])


def q_faixa_sem_metodo_declarado(banco):
    return _com_faixas(banco, [_faixa_de_bancada(metodo_declarado="")])


def q_faixa_sem_base_transcrita(banco):
    return _com_faixas(banco, [_faixa_de_bancada(base_transcrita_de="   ")])


def q_faixa_invertida(banco):
    return _com_faixas(banco, [_faixa_de_bancada(valor_min=200, valor_max=100)])


def q_faixa_com_valor_zero(banco):
    return _com_faixas(banco, [_faixa_de_bancada(valor_min=0)])


def q_faixa_de_quarto_sem_ocupacao_e_sem_motivo(banco):
    return _com_faixas(banco, [_faixa_de_bancada(
        base="por_quarto_por_dia", pessoas_por_quarto=None,
        base_transcrita_de="diaria de quarto")])


def q_ocupacao_que_a_frase_nao_declara(banco):
    """A ocupacao gravada e TRES e a frase da fonte diz «quarto duplo»."""
    return _com_faixas(banco, [_faixa_de_bancada(
        base="por_quarto_por_dia", pessoas_por_quarto=3,
        base_transcrita_de="diaria de quarto duplo")])


def q_ocupacao_achada_dentro_de_outro_numero(banco):
    """A frase diz «R$ 2.400 por quarto» e a ocupacao gravada e 2.

    Mesma armadilha que o `dias_de_uso` pagou: procurar por vizinhanca acha o 2 de
    2.400 e aprova uma ocupacao que a fonte nunca declarou.
    """
    return _com_faixas(banco, [_faixa_de_bancada(
        base="por_quarto_por_dia", pessoas_por_quarto=2,
        base_transcrita_de="diaria de 2400 reais por quarto")])


def q_ocupacao_fora_da_base_de_quarto(banco):
    return _com_faixas(banco, [_faixa_de_bancada(pessoas_por_quarto=2)])


def q_faixa_diaria_sem_data_de_leitura(banco):
    return _com_faixas(banco, [_faixa_de_bancada(data_leitura=None)])


def q_faixa_de_cidade_que_nao_existe(banco):
    return _com_faixas(banco, [_faixa_de_bancada(cidade="cidade-que-nao-existe")])


def q_faixa_com_categoria_fora_do_vocabulario(banco):
    return _com_faixas(banco, [_faixa_de_bancada(categoria_de_custo="lavanderia")])


def q_faixa_com_base_fora_do_vocabulario(banco):
    return _com_faixas(banco, [_faixa_de_bancada(base="por_semana")])


def q_faixa_sem_url_e_sem_motivo(banco):
    return _com_faixas(banco, [_faixa_de_bancada(url=None)])


def q_faixa_com_id_repetido(banco):
    return _com_faixas(banco, [_faixa_de_bancada(), _faixa_de_bancada(valor_min=90)])


def q_resumo_de_faixas_digitado(banco):
    banco = _com_faixas(banco, [_faixa_de_bancada()])
    banco["resumo"]["faixas_diarias"] = 7
    return banco


# ---------------------------------------------------------------------------
# O PASSE DE CIDADE E A COBERTURA — a entidade que nasceu em 22/10/2026 para a F3
#
# O banco tem ZERO passes e ZERO coberturas, e por isso as ~130 linhas que o validador
# ganhou hoje NUNCA SERIAM EXECUTADAS por ninguem: e a mesma situacao da FAIXA_DIARIA
# ha um bloco, com a diferenca de que agora ela e conhecida. Uma delas estourava na
# PRIMEIRA cobertura gravada e em nenhum momento antes — a secao usava um indice de
# experiencias que nao existia —, e so um mundo com cobertura dentro a enxerga.
#
# O passe de bancada mora em ROMA de proposito: e a unica cidade do banco com uma
# atracao cuja cobertura faz sentido (o ingresso do Coliseu), e cobertura precisa dos
# DOIS lados para existir.
# ---------------------------------------------------------------------------

def _versao_de_passe(vid, rotulo, preco, dias):
    return {
        "id": vid,
        "rotulo": rotulo,
        "preco": preco,
        "moeda": "EUR",
        "unidade_de_preco": "por_pessoa",
        "unidade_de_preco_declarada_por": "no_texto_da_fonte",
        "capacidade_maxima": None,
        "capacidade_maxima_declarada_por": None,
        "duracao_minutos": None,
        "motivo_sem_duracao": "passe de cidade nao tem duracao de passeio: tem validade.",
        "momento_do_dia": "qualquer",
        "acrescimos": [],
        "inclui": ["entrada nas atracoes cobertas"],
        "nao_inclui": [],
        "nao_inclui_motivo_lista_vazia": "mundo de mutacao",
        "fonte": "roma-pass-operador-teste",
        "data_leitura": "2026-09-14",
        "declarado_como": "%d euros por pessoa, validade de %d dias" % (preco, dias),
        "dias_de_uso": dias,
        "dias_de_uso_transcrito_de": "a frase `declarado_como` deste mundo de mutacao, "
                                     "que escreve a validade em digito.",
        "faixa_etaria": None,
        "motivo_sem_faixa_etaria": "mundo de mutacao: a fonte de bancada nao declara faixa.",
        "faixas_que_a_fonte_declara_e_a_leitura_nao_transcreveu": [],
            "elegibilidade": None,
            "motivo_sem_elegibilidade": "mundo de mutacao: a fonte de bancada nao declara tarifa por residencia nem nacionalidade.",
    }


def _passe_em_roma(banco, declaradas=2, transcrito=None, versoes=None):
    banco["fontes"].append({
        "id": "roma-pass-operador-teste",
        "nivel": 4,
        "origem": "operador-via-busca",
        "leitura": "busca_web",
        "autor": "operador de passe de teste",
        "documento": "pagina de tarifas do passe de bancada",
        "url": None,
        "motivo_sem_url": "mundo de mutacao",
        "data_leitura": "2026-09-14",
    })
    exp = {
        "id": "roma-passe-teste",
        "nome": "Passe de Roma (mundo de mutação)",
        "cidade": "roma",
        "categoria": "passe_de_cidade",
        "eixo_das_versoes": "por_quantidade",
        "nota_do_eixo_das_versoes": "As duas versoes sao MAIS DA MESMA COISA: 2 e 3 dias de "
                                    "validade do mesmo passe. E o eixo que a Conta 3 da F1 "
                                    "usa, e aqui ele tambem diz se o passe cobre a estadia.",
        "operador": {"nome": "operador de passe de teste", "tipo": "concessionaria_de_bem_publico",
                     "url": None, "motivo_sem_url": "mundo de mutacao"},
        "versoes": versoes if versoes is not None else [
            _versao_de_passe("48h", "2 dias", 32, 2),
            _versao_de_passe("72h", "3 dias", 52, 3)],
        "temporada": None,
        "motivo_sem_temporada": "mundo de mutacao",
        "imagem": None,
        "motivo_sem_imagem": "mundo de mutacao",
        "declaracoes": [],
        "motivo_sem_declaracoes": "mundo de mutacao: ninguem mais publicou numero diferente.",
        "resolucao": None,
        "motivo_sem_resolucao": "mundo de mutacao: sem divergencia nao ha o que resolver.",
        "afiliado": {
            "programa": None,
            "url": "",
            "url_produto": None,
            "motivo_sem_url_produto": "mundo de mutacao",
            "url_busca_produto": "https://civitatis.com/br/roma/",
            "rel": "nofollow noopener",
            "intestavel": False,
        },
        "status": "publicavel",
        "entra_por": "mundo de mutacao: o passe de cidade que o vocabulario permite e o "
                     "banco nao tem.",
        "atracoes_declaradas_pelo_passe": declaradas,
        "atracoes_declaradas_transcrito_de": transcrito if transcrito is not None else (
            "o passe da entrada em %d atracoes de Roma" % declaradas),
    }
    banco["experiencias"].append(exp)
    return exp


def _cobertura(**campos):
    base = {
        "id": "bancada-cobertura-coliseu",
        "passe": "roma-passe-teste",
        "experiencia": "roma-coliseu-ingresso",
        "versao_coberta": "padrao-24h",
        "como": "entrada_incluida",
        "reserva_obrigatoria": True,
        "reserva_transcrita_de": "a reserva de horario e obrigatoria e feita a parte",
        "desconto_percentual": None,
        "desconto_e_no_maximo": None,
        "desconto_transcrito_de": None,
        "declarada_por": "no_texto_da_fonte",
        "fonte": "roma-pass-operador-teste",
        "data_leitura": "2026-09-14",
        "status": "publicavel",
    }
    base.update(campos)
    return base


def _com_coberturas(banco, coberturas):
    banco["coberturas_de_passe"] = coberturas
    return sincronizar_resumo(banco)


def mundo_passe_sem_cobertura_lida(banco):
    """Passe no banco e NENHUMA cobertura lida. E o estado em que todo passe nasce.

    Tem de PASSAR com aviso: o banco guarda o que foi lido, e a F3 e quem se nega a
    publicar ponto de equilibrio sem cobertura. Supor cobertura aqui seria inventar o
    produto do passe.
    """
    _passe_em_roma(banco)
    return sincronizar_resumo(banco)


def mundo_passe_com_cobertura(banco):
    """O mundo inteiro: passe, cobertura lida, versao coberta nomeada e reserva."""
    _passe_em_roma(banco)
    return _com_coberturas(banco, [_cobertura()])


def mundo_cobertura_sem_versao_declarada(banco):
    """A fonte do passe diz «o ingresso do Coliseu» e NAO diz qual bilhete.

    E o caso COMUM, e e ele que faz a F3 publicar faixa em vez de numero.
    """
    _passe_em_roma(banco)
    return _com_coberturas(banco, [_cobertura(
        versao_coberta=None,
        motivo_sem_versao_coberta="A fonte escreve «entrada no Coliseu» e o Coliseu tem "
                                  "dois bilhetes: ela nao diz qual.")])


def mundo_cobertura_com_desconto(banco):
    """Desconto percentual CHEIO, com o numero dentro da frase da fonte."""
    _passe_em_roma(banco)
    return _com_coberturas(banco, [_cobertura(
        como="desconto_declarado", desconto_percentual=50, desconto_e_no_maximo=False,
        desconto_transcrito_de="50% de desconto na entrada para quem tem o passe")])


def mundo_cobertura_com_desconto_que_e_teto(banco):
    """«Ate 50%» — a hedge virada FAIXA, que e a troca que esta entidade faz."""
    _passe_em_roma(banco)
    return _com_coberturas(banco, [_cobertura(
        como="desconto_declarado", desconto_percentual=50, desconto_e_no_maximo=True,
        desconto_transcrito_de="até 50% de desconto na entrada")])


def mundo_cobertura_sem_efeito_no_preco(banco):
    """O passe da fila preferencial e NAO abate nada. Zero entra como zero declarado."""
    _passe_em_roma(banco)
    return _com_coberturas(banco, [_cobertura(
        id="bancada-cobertura-fila", como="sem_efeito_no_preco",
        reserva_obrigatoria=False, reserva_transcrita_de=None)])


def mundo_passe_de_uma_validade_so(banco):
    """Passe de UMA versao: eixo null COM `dias_de_uso` preenchido.

    E o mundo que o esquema sempre permitiu e a regua NAO CONFERIA — as duas direcoes
    do `dias_de_uso` cobravam `por_quantidade` e proibiam os outros eixos, e o null nao
    caia em nenhuma. Fechado em 22/10/2026 pelo bloco da F3, que precisou da validade
    do passe neste mundo exato.
    """
    exp = _passe_em_roma(banco, versoes=[_versao_de_passe("72h", "3 dias", 52, 3)])
    exp["eixo_das_versoes"] = None
    del exp["nota_do_eixo_das_versoes"]
    exp["motivo_sem_eixo_das_versoes"] = ("Uma validade so: nao ha duas coisas para dizer "
                                          "em que grandeza diferem.")
    return sincronizar_resumo(banco)


def q_passe_sem_atracoes_declaradas(banco):
    exp = _passe_em_roma(banco)
    del exp["atracoes_declaradas_pelo_passe"]
    return sincronizar_resumo(banco)


def q_passe_com_atracoes_que_a_frase_nao_declara(banco):
    _passe_em_roma(banco, declaradas=45,
                   transcrito="o passe da entrada nas atracoes de Roma")
    return sincronizar_resumo(banco)


def q_atracoes_declaradas_num_ingresso_avulso(banco):
    _achar(banco, "roma-coliseu-ingresso")["atracoes_declaradas_pelo_passe"] = 3
    return sincronizar_resumo(banco)


def q_cobertura_de_passe_que_nao_e_passe(banco):
    _passe_em_roma(banco)
    return _com_coberturas(banco, [_cobertura(passe="roma-coliseu-ingresso",
                                              experiencia="roma-passe-teste")])


def q_cobertura_de_atracao_que_nao_existe(banco):
    _passe_em_roma(banco)
    return _com_coberturas(banco, [_cobertura(experiencia="atracao-que-nao-existe",
                                              versao_coberta=None,
                                              motivo_sem_versao_coberta="mundo de mutacao")])


def q_cobertura_cruzando_cidade(banco):
    _passe_em_roma(banco)
    return _com_coberturas(banco, [_cobertura(
        experiencia="paris-torre-eiffel", versao_coberta="topo-elevador")])


def q_cobertura_de_passe_sobre_passe(banco):
    _passe_em_roma(banco)
    segundo = _achar(banco, "roma-passe-teste")
    copia = copy.deepcopy(segundo)
    copia["id"] = "roma-passe-teste-2"
    copia["nome"] = "Segundo passe de Roma (mundo de mutação)"
    banco["experiencias"].append(copia)
    return _com_coberturas(banco, [_cobertura(experiencia="roma-passe-teste-2",
                                              versao_coberta="48h")])


def q_duas_coberturas_do_mesmo_par(banco):
    _passe_em_roma(banco)
    return _com_coberturas(banco, [_cobertura(),
                                   _cobertura(id="bancada-cobertura-coliseu-2")])


def q_cobertura_com_versao_que_nao_e_da_atracao(banco):
    _passe_em_roma(banco)
    return _com_coberturas(banco, [_cobertura(versao_coberta="topo-elevador")])


def q_cobertura_sem_o_campo_versao(banco):
    _passe_em_roma(banco)
    cob = _cobertura()
    del cob["versao_coberta"]
    return _com_coberturas(banco, [cob])


def q_cobertura_sem_versao_e_sem_motivo(banco):
    _passe_em_roma(banco)
    return _com_coberturas(banco, [_cobertura(versao_coberta=None)])


def q_cobertura_com_reserva_null(banco):
    _passe_em_roma(banco)
    return _com_coberturas(banco, [_cobertura(reserva_obrigatoria=None,
                                              reserva_transcrita_de=None)])


def q_cobertura_com_reserva_sem_a_frase(banco):
    _passe_em_roma(banco)
    return _com_coberturas(banco, [_cobertura(reserva_transcrita_de=None)])


def q_desconto_sem_percentual(banco):
    _passe_em_roma(banco)
    return _com_coberturas(banco, [_cobertura(
        como="desconto_declarado", desconto_percentual=None, desconto_e_no_maximo=False,
        desconto_transcrito_de="desconto na entrada para quem tem o passe")])


def q_desconto_de_cem_por_cento(banco):
    _passe_em_roma(banco)
    return _com_coberturas(banco, [_cobertura(
        como="desconto_declarado", desconto_percentual=100, desconto_e_no_maximo=False,
        desconto_transcrito_de="100% de desconto na entrada")])


def q_desconto_que_a_frase_nao_declara(banco):
    _passe_em_roma(banco)
    return _com_coberturas(banco, [_cobertura(
        como="desconto_declarado", desconto_percentual=50, desconto_e_no_maximo=False,
        desconto_transcrito_de="desconto de 30% na entrada")])


def q_desconto_sem_dizer_se_e_teto(banco):
    _passe_em_roma(banco)
    return _com_coberturas(banco, [_cobertura(
        como="desconto_declarado", desconto_percentual=50, desconto_e_no_maximo=None,
        desconto_transcrito_de="50% de desconto na entrada")])


def q_hedge_lida_como_numero_cheio(banco):
    """O DEFEITO QUE O PAR DE CAMPOS EXISTE PARA IMPEDIR: «ate 50%» gravado como 50%.

    A frase traz a hedge e o campo diz que o desconto e o valor. O resultado continua
    parecendo dinheiro, que e por que ninguem ve.
    """
    _passe_em_roma(banco)
    return _com_coberturas(banco, [_cobertura(
        como="desconto_declarado", desconto_percentual=50, desconto_e_no_maximo=False,
        desconto_transcrito_de="até 50% de desconto na entrada")])


def q_desconto_fora_da_forma_que_o_usa(banco):
    _passe_em_roma(banco)
    return _com_coberturas(banco, [_cobertura(desconto_percentual=50)])


def q_cobertura_com_forma_fora_do_vocabulario(banco):
    _passe_em_roma(banco)
    return _com_coberturas(banco, [_cobertura(como="meia_entrada")])


def q_cobertura_sem_data_de_leitura(banco):
    _passe_em_roma(banco)
    return _com_coberturas(banco, [_cobertura(data_leitura=None)])


def q_cobertura_com_fonte_inexistente(banco):
    _passe_em_roma(banco)
    return _com_coberturas(banco, [_cobertura(fonte="fonte-que-nao-existe")])


def q_cobertura_com_id_repetido(banco):
    _passe_em_roma(banco)
    return _com_coberturas(banco, [_cobertura(),
                                   _cobertura(experiencia="roma-coliseu-ingresso",
                                              versao_coberta="experiencia-completa")])


def q_resumo_de_coberturas_digitado(banco):
    banco = mundo_passe_com_cobertura(banco)
    banco["resumo"]["coberturas_de_passe"] = 9
    return banco


def q_dias_de_uso_sem_transcrito_em_eixo_null(banco):
    """A METADE QUE ESTAVA SEM REGUA ATE HOJE: eixo null, `dias_de_uso` preenchido e
    SEM a frase de onde o numero saiu. Antes de 22/10/2026 isto PASSAVA."""
    versao = _versao_de_passe("72h", "3 dias", 52, 3)
    del versao["dias_de_uso_transcrito_de"]
    exp = _passe_em_roma(banco, versoes=[versao])
    exp["eixo_das_versoes"] = None
    del exp["nota_do_eixo_das_versoes"]
    exp["motivo_sem_eixo_das_versoes"] = "Uma validade so."
    return sincronizar_resumo(banco)


def q_dias_de_uso_que_a_fonte_nao_declara_em_eixo_null(banco):
    """Eixo null, validade 7 e a frase da fonte dizendo 3. A outra metade do mesmo."""
    versao = _versao_de_passe("72h", "3 dias", 52, 3)
    versao["dias_de_uso"] = 7
    exp = _passe_em_roma(banco, versoes=[versao])
    exp["eixo_das_versoes"] = None
    del exp["nota_do_eixo_das_versoes"]
    exp["motivo_sem_eixo_das_versoes"] = "Uma validade so."
    return sincronizar_resumo(banco)


def q_dias_de_uso_null_sem_motivo_em_eixo_null(banco):
    versao = _versao_de_passe("72h", "3 dias", 52, 3)
    versao["dias_de_uso"] = None
    del versao["dias_de_uso_transcrito_de"]
    exp = _passe_em_roma(banco, versoes=[versao])
    exp["eixo_das_versoes"] = None
    del exp["nota_do_eixo_das_versoes"]
    exp["motivo_sem_eixo_das_versoes"] = "Uma validade so."
    return sincronizar_resumo(banco)


# ======================================================================
# A ELEGIBILIDADE (27/10/2026, carga do Bondinho Pao de Acucar)
#
# A troca entre faixa etaria e elegibilidade e o defeito que estas quebras existem
# para pegar, e ela e SILENCIOSA: os dois campos guardam um preco menor com uma
# condicao escrita ao lado, e lidos de longe parecem a mesma coisa. O que os separa
# e O QUE SE PROVA na porta — idade de um lado, residencia do outro.
# As duas primeiras medem os DOIS SENTIDOS da troca, e o sentido que a ilha ia errar
# e o segundo: na carga de hoje os cinco precos do mesmo bilhete vieram na mesma
# leitura, e a saida barata era chamar os cinco de faixa.
def _bondinho(banco):
    return _achar(banco, "rio-de-janeiro-bondinho-pao-de-acucar")


def _bilhete(banco):
    return _bondinho(banco)["versoes"][0]


def q_idade_gravada_como_elegibilidade(banco):
    """Primeiro sentido: a condicao da elegibilidade passa a declarar idade."""
    _bilhete(banco)["elegibilidade"][0]["condicao"] = "crianca de 3 a 12 anos"
    return banco


def q_residencia_gravada_como_faixa_etaria(banco):
    """Segundo sentido, e o que a ilha ia errar: a promocional de brasileiro desce
    para `faixa_etaria`, que e o campo da idade. R$ 160 nao e preco de uma idade."""
    v = _bilhete(banco)
    v["faixa_etaria"].append({
        "rotulo": "Promocional para Brasileiros", "preco": 160,
        "moeda": "BRL_do_operador",
        "condicao": "ter nascido no Brasil E morar no Brasil",
        "se_nao_cumprir": "paga R$ 205",
        "declarado_como": "todas as pessoas nascidas e moradoras do Brasil pagam R$ 160",
        "fonte": "parque-bondinho-tarifa-via-busca", "data_leitura": "2026-10-27"})
    return sincronizar_resumo(banco)


def q_elegibilidade_null_sem_motivo(banco):
    del _bondinho(banco)["versoes"][1]["motivo_sem_elegibilidade"]
    return banco


def q_elegibilidade_sem_o_campo(banco):
    del _bondinho(banco)["versoes"][1]["elegibilidade"]
    return banco


def q_elegibilidade_lista_vazia(banco):
    _bondinho(banco)["versoes"][1]["elegibilidade"] = []
    return banco


def q_elegibilidade_fora_do_vocabulario(banco):
    _bilhete(banco)["elegibilidade"][0]["o_que_se_prova"] = "idade"
    return banco


def q_elegibilidade_mais_cara_que_o_bilhete(banco):
    """R$ 300 num bilhete de R$ 205: desconto que custa mais que a tarifa cheia nao
    e desconto de ninguem."""
    _bilhete(banco)["elegibilidade"][1]["preco"] = 300
    return banco


def q_elegibilidade_em_outra_moeda(banco):
    _bilhete(banco)["elegibilidade"][0]["moeda"] = "EUR"
    return banco


def q_elegibilidade_sem_declarado_como(banco):
    del _bilhete(banco)["elegibilidade"][0]["declarado_como"]
    return banco


def q_elegibilidade_sem_data_de_leitura(banco):
    del _bilhete(banco)["elegibilidade"][1]["data_leitura"]
    return banco


def q_elegibilidade_sem_se_nao_cumprir(banco):
    """A metade que custa dinheiro na porta: sem ela a tela diz que ha um preco de
    R$ 89 e nao diz o que paga quem nao prova que e do Rio."""
    _bilhete(banco)["elegibilidade"][1]["se_nao_cumprir"] = None
    return banco


def q_elegibilidade_com_fonte_inexistente(banco):
    _bilhete(banco)["elegibilidade"][0]["fonte"] = "fonte-que-nao-existe"
    return banco


def q_rotulo_de_elegibilidade_repetido(banco):
    v = _bilhete(banco)
    v["elegibilidade"][1]["rotulo"] = v["elegibilidade"][0]["rotulo"]
    return banco


def q_soma_presumida_com_campo_null(banco):
    """O campo que impede a F1 de multiplicar: null numa versao que TEM faixa etaria
    e exatamente o caso em que a regua precisa saber se pode somar. Medido: metade de
    R$ 89 e R$ 44,50 e o operador cobra R$ 44 — cinquenta centavos inventados."""
    _bilhete(banco)["elegibilidade"][0]["acumula_com_faixa_etaria"] = None
    return banco


def q_soma_autorizada_sem_frase_da_fonte(banco):
    """`acumula` true sem a frase da fonte que autoriza somar. Ressalva inventada e
    invencao, e autorizacao inventada e pior."""
    _bilhete(banco)["elegibilidade"][0]["acumula_com_faixa_etaria"] = True
    return banco


def q_elegibilidade_sem_o_campo_acumula(banco):
    del _bilhete(banco)["elegibilidade"][1]["acumula_com_faixa_etaria"]
    return banco


def q_resumo_de_elegibilidade_digitado(banco):
    banco["resumo"]["elegibilidades"] = 9
    return banco


def q_elegibilidade_na_experiencia(banco):
    _bondinho(banco)["elegibilidade"] = [{"rotulo": "Promocional para Brasileiros"}]
    return banco


def q_brl_contado_a_mao(banco):
    """O contador que contava a coisa errada ate 27/10/2026: ele vivia dentro do ramo
    de ERRO da conferencia de moeda e publicava sob um nome que dizia o contrario.
    Com o banco todo em EUR e USD saia 0, e 0 era a verdade por acidente."""
    banco["resumo"]["experiencias_com_preco_em_brl"] = 0
    return banco


MUTACOES = [
    ("MUNDO preco por pessoa, escada de dias, crianca e temporada", mundo_por_pessoa, "passa", None),
    ("MUNDO preco por cabine", mundo_por_cabine, "passa", None),
    ("MUNDO item com link rastreado e intestavel", mundo_com_link_rastreado, "passa", None),
    # O PAR `degrau_6_negado` SAIU EM 27/10/2026, e a saida e a propria regra
    # funcionando. Este mundo esvazia as declaracoes da GONDOLA, e ate ontem isso
    # apagava do banco todas as fontes de nivel 6 — logo o esquema tinha de negar
    # o degrau 6 junto, porque `existe_hoje` e DERIVADO das fontes. Com a carga do
    # Bondinho ha fontes de nivel 6 em OUTRA experiencia (a imprensa dos 114 anos e
    # o blog da Civitatis), que este mundo nao toca: o degrau 6 continua existindo,
    # e negar-lho no esquema e que viraria o erro. Mundo passa com o esquema INTACTO.
    ("MUNDO experiencia sem divergencia nenhuma", mundo_sem_divergencia, "passa", None),
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
    ("MUNDO faixa diaria por pessoa", mundo_faixa_por_pessoa, "passa", None),
    ("MUNDO faixa diaria de QUARTO com a ocupacao declarada", mundo_faixa_de_quarto_com_ocupacao, "passa", None),
    ("MUNDO ocupacao do quarto declarada POR EXTENSO", mundo_faixa_de_quarto_com_ocupacao_por_extenso, "passa", None),
    ("MUNDO faixa diaria de quarto sem ocupacao, COM o motivo escrito", mundo_faixa_de_quarto_sem_ocupacao_COM_motivo, "passa", None),
    ("MUNDO media e minimo na mesma cidade: AVISO e nao erro", mundo_duas_naturezas_de_numero, "passa", None),
    ("MUNDO faixa diaria sem url, COM o motivo escrito", mundo_faixa_sem_url_COM_motivo, "passa", None),

    ("faixa diaria sem o nome de quem publicou", q_faixa_sem_publicado_por, "reprova", None, "publicado_por"),
    ("faixa diaria sem a frase do metodo", q_faixa_sem_metodo_declarado, "reprova", None, "metodo_declarado"),
    ("faixa diaria com base sem a frase de onde ela saiu", q_faixa_sem_base_transcrita, "reprova", None, "base_transcrita_de"),
    ("faixa diaria com o teto menor que o piso", q_faixa_invertida, "reprova", None, "intervalo vazio"),
    ("faixa diaria com valor zero", q_faixa_com_valor_zero, "reprova", None, "maior que zero"),
    ("faixa diaria de quarto sem ocupacao e sem motivo", q_faixa_de_quarto_sem_ocupacao_e_sem_motivo, "reprova", None, "TRES quartos"),
    ("ocupacao que a frase da fonte NAO declara", q_ocupacao_que_a_frase_nao_declara, "reprova", None, "TRANSCRITO"),
    ("ocupacao achada DENTRO de outro numero", q_ocupacao_achada_dentro_de_outro_numero, "reprova", None, "TRANSCRITO"),
    ("ocupacao gravada fora da base de quarto", q_ocupacao_fora_da_base_de_quarto, "reprova", None, "PROIBE ocupacao"),
    ("faixa diaria sem data de leitura", q_faixa_diaria_sem_data_de_leitura, "reprova", None, "data_leitura"),
    ("faixa diaria de cidade que nao esta no banco", q_faixa_de_cidade_que_nao_existe, "reprova", None, "nao esta no banco"),
    ("faixa diaria com categoria fora do vocabulario", q_faixa_com_categoria_fora_do_vocabulario, "reprova", None, "fora do vocabulario"),
    ("faixa diaria com base fora do vocabulario", q_faixa_com_base_fora_do_vocabulario, "reprova", None, "fora do vocabulario"),
    ("faixa diaria sem url e sem motivo", q_faixa_sem_url_e_sem_motivo, "reprova", None, "motivo_sem_url"),
    ("faixa diaria com id repetido", q_faixa_com_id_repetido, "reprova", None, "repetido"),
    ("resumo de faixas digitado em vez de contado", q_resumo_de_faixas_digitado, "reprova", None, "faixas_diarias"),
    ("esquema sem a entidade FAIXA_DIARIA", _intacto, "reprova", "sem_entidade_faixa_diaria",
     "FAIXA_DIARIA"),
    ("esquema com vocabulario novo que a regua nao sabe extrair", _intacto, "reprova",
     "vocab_novo_sem_extrator", "sem extrator"),

    ("esquema sem o registro da Conta 3", _intacto, "reprova", "sem_registro_conta_3",
     "conta_3_da_F1_exige_EIXO_DECLARADO"),

    # --- O PASSE DE CIDADE E A COBERTURA (22/10/2026, bloco da F3)
    ("MUNDO passe de cidade SEM cobertura lida", mundo_passe_sem_cobertura_lida, "passa", None),
    ("MUNDO passe com cobertura lida e versao nomeada", mundo_passe_com_cobertura, "passa", None),
    ("MUNDO cobertura que NAO diz qual bilhete cobre", mundo_cobertura_sem_versao_declarada, "passa", None),
    ("MUNDO cobertura com desconto percentual cheio", mundo_cobertura_com_desconto, "passa", None),
    ("MUNDO cobertura com desconto que e TETO («ate 50%»)", mundo_cobertura_com_desconto_que_e_teto, "passa", None),
    ("MUNDO cobertura sem efeito no preco (fila preferencial)", mundo_cobertura_sem_efeito_no_preco, "passa", None),
    ("MUNDO passe de UMA validade: eixo null com dias_de_uso", mundo_passe_de_uma_validade_so, "passa", None),

    ("passe sem o campo atracoes_declaradas_pelo_passe", q_passe_sem_atracoes_declaradas, "reprova", None, "atracoes_declaradas_pelo_passe"),
    ("passe com numero de atracoes que a frase NAO declara", q_passe_com_atracoes_que_a_frase_nao_declara, "reprova", None, "TRANSCRITO"),
    ("atracoes declaradas num ingresso avulso", q_atracoes_declaradas_num_ingresso_avulso, "reprova", None, "PROIBE"),
    ("cobertura cujo passe nao e passe", q_cobertura_de_passe_que_nao_e_passe, "reprova", None, "nao e"),
    ("cobertura de atracao que nao esta no banco", q_cobertura_de_atracao_que_nao_existe, "reprova", None, "nao esta no banco"),
    ("cobertura cruzando cidade", q_cobertura_cruzando_cidade, "reprova", None, "cruzando cidade"),
    ("passe que cobre outro passe", q_cobertura_de_passe_sobre_passe, "reprova", None, "duas vezes"),
    ("duas coberturas do MESMO par passe x atracao", q_duas_coberturas_do_mesmo_par, "reprova", None, "segunda cobertura"),
    ("cobertura com versao que nao e da atracao", q_cobertura_com_versao_que_nao_e_da_atracao, "reprova", None, "nao e uma versao"),
    ("cobertura sem o campo versao_coberta", q_cobertura_sem_o_campo_versao, "reprova", None, "falta o campo"),
    ("cobertura sem versao e sem motivo", q_cobertura_sem_versao_e_sem_motivo, "reprova", None, "motivo_sem_versao_coberta"),
    ("cobertura com reserva_obrigatoria null", q_cobertura_com_reserva_null, "reprova", None, "nao e booleano"),
    ("cobertura com reserva obrigatoria e sem a frase", q_cobertura_com_reserva_sem_a_frase, "reprova", None, "reserva_transcrita_de"),
    ("desconto declarado sem percentual", q_desconto_sem_percentual, "reprova", None, "desconto_percentual"),
    ("desconto de 100 por cento", q_desconto_de_cem_por_cento, "reprova", None, "entrada incluida"),
    ("desconto que a frase da fonte NAO declara", q_desconto_que_a_frase_nao_declara, "reprova", None, "transcrito"),
    ("desconto sem dizer se e teto", q_desconto_sem_dizer_se_e_teto, "reprova", None, "desconto_e_no_maximo"),
    ("HEDGE lida como numero cheio: «ate 50%» gravado como 50%", q_hedge_lida_como_numero_cheio, "reprova", None, "hedge virando numero cheio"),
    ("desconto gravado fora da forma que o usa", q_desconto_fora_da_forma_que_o_usa, "reprova", None, "PROIBE desconto"),
    ("cobertura com forma fora do vocabulario", q_cobertura_com_forma_fora_do_vocabulario, "reprova", None, "fora do vocabulario"),
    ("cobertura sem data de leitura", q_cobertura_sem_data_de_leitura, "reprova", None, "data_leitura"),
    ("cobertura com fonte inexistente", q_cobertura_com_fonte_inexistente, "reprova", None, "fontes[]"),
    ("cobertura com id repetido", q_cobertura_com_id_repetido, "reprova", None, "repetido"),
    ("resumo de coberturas digitado em vez de contado", q_resumo_de_coberturas_digitado, "reprova", None, "coberturas_de_passe"),
    ("esquema sem a entidade COBERTURA_DO_PASSE", _intacto, "reprova", "sem_entidade_cobertura", "COBERTURA_DO_PASSE"),
    ("esquema sem as tres regras da cobertura", _intacto, "reprova", "sem_as_tres_regras", "as_tres_regras"),
    ("esquema sem o vocabulario forma_de_cobertura", _intacto, "reprova", "vocab_sem_forma_de_cobertura", "forma_de_cobertura"),

    # --- A METADE DO `dias_de_uso` QUE O EIXO NULL ESCONDIA (22/10/2026)
    ("eixo null com dias_de_uso e SEM a frase de onde saiu", q_dias_de_uso_sem_transcrito_em_eixo_null, "reprova", None, "dias_de_uso_transcrito_de"),
    ("eixo null com dias_de_uso que a fonte NAO declara", q_dias_de_uso_que_a_fonte_nao_declara_em_eixo_null, "reprova", None, "declarado_como"),
    ("eixo null com dias_de_uso null e sem motivo", q_dias_de_uso_null_sem_motivo_em_eixo_null, "reprova", None, "motivo_sem_dias_de_uso"),

    # --- A ELEGIBILIDADE (27/10/2026, carga do Bondinho)
    ("IDADE gravada como elegibilidade", q_idade_gravada_como_elegibilidade, "reprova", None, "e de FAIXA_ETARIA"),
    ("RESIDENCIA gravada como faixa etaria", q_residencia_gravada_como_faixa_etaria, "reprova", None, "e de ELEGIBILIDADE"),
    ("elegibilidade null sem motivo", q_elegibilidade_null_sem_motivo, "reprova", None, "motivo_sem_elegibilidade"),
    ("versao sem o campo elegibilidade", q_elegibilidade_sem_o_campo, "reprova", None, "Ausencia de chave"),
    ("elegibilidade como lista vazia", q_elegibilidade_lista_vazia, "reprova", None, "lista NAO vazia"),
    ("o_que_se_prova fora do vocabulario (idade)", q_elegibilidade_fora_do_vocabulario, "reprova", None, "fora do vocabulario"),
    ("elegibilidade mais cara que o bilhete inteiro", q_elegibilidade_mais_cara_que_o_bilhete, "reprova", None, "campo errado"),
    ("elegibilidade em moeda diferente da versao", q_elegibilidade_em_outra_moeda, "reprova", None, "cambio"),
    ("elegibilidade sem declarado_como", q_elegibilidade_sem_declarado_como, "reprova", None, "parafraseia"),
    ("elegibilidade sem data de leitura", q_elegibilidade_sem_data_de_leitura, "reprova", None, "preco de brasileiro"),
    ("elegibilidade sem se_nao_cumprir", q_elegibilidade_sem_se_nao_cumprir, "reprova", None, "motivo_sem_se_nao_cumprir"),
    ("elegibilidade com fonte que nao existe", q_elegibilidade_com_fonte_inexistente, "reprova", None, "nao existe em fontes"),
    ("rotulo de elegibilidade repetido na versao", q_rotulo_de_elegibilidade_repetido, "reprova", None, "repetido"),
    ("A SOMA PRESUMIDA: acumula null com faixa etaria na versao", q_soma_presumida_com_campo_null, "reprova", None, "nao sabe"),
    ("soma autorizada sem a frase da fonte", q_soma_autorizada_sem_frase_da_fonte, "reprova", None, "AUTORIZA somar"),
    ("elegibilidade sem o campo acumula_com_faixa_etaria", q_elegibilidade_sem_o_campo_acumula, "reprova", None, "a_soma_nao_se_presume"),
    ("resumo de elegibilidades digitado a mao", q_resumo_de_elegibilidade_digitado, "reprova", None, "elegibilidades"),
    ("elegibilidade gravada na EXPERIENCIA", q_elegibilidade_na_experiencia, "reprova", "eleg_na_experiencia", "da VERSAO"),
    ("o contador de BRL digitado a mao (0 era verdade por acidente)", q_brl_contado_a_mao, "reprova", None, "experiencias_com_preco_em_brl"),
    ("esquema sem a entidade ELEGIBILIDADE", _intacto, "reprova", "sem_entidade_elegibilidade", "ELEGIBILIDADE"),
    ("esquema sem o campo elegibilidade na VERSAO", _intacto, "reprova", "eleg_sem_campo_na_versao", "null_exige"),
    ("esquema sem a regra_da_elegibilidade", _intacto, "reprova", "sem_regra_da_elegibilidade", "regra_da_elegibilidade"),
    ("esquema sem a regra dos dois sentidos da troca", _intacto, "reprova", "sem_os_dois_sentidos", "idade_nunca_entra_em_elegibilidade"),
    ("esquema sem o vocabulario o_que_se_prova", _intacto, "reprova", "vocab_sem_o_que_se_prova", "fora do vocabulario"),
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
    elif mutacao == "sem_entidade_cobertura":
        del esquema["entidades"]["COBERTURA_DO_PASSE"]
    elif mutacao == "sem_as_tres_regras":
        del esquema["regra_da_cobertura_do_passe"]["as_tres_regras"]
    elif mutacao == "vocab_sem_forma_de_cobertura":
        del esquema["vocabularios"]["forma_de_cobertura"]
    elif mutacao == "vocab_sem_eixo":
        del esquema["vocabularios"]["eixo_das_versoes"]
    elif mutacao == "exp_sem_eixo":
        del esquema["entidades"]["EXPERIENCIA"]["campos"]["eixo_das_versoes"]
    elif mutacao == "versao_sem_dias":
        del esquema["entidades"]["VERSAO"]["campos"]["dias_de_uso"]
    elif mutacao == "sem_registro_conta_3":
        del esquema["conta_3_da_F1_exige_EIXO_DECLARADO_e_nao_sai_do_rotulo"]
    elif mutacao == "sem_entidade_faixa_diaria":
        del esquema["entidades"]["FAIXA_DIARIA"]
    elif mutacao == "vocab_novo_sem_extrator":
        # Vocabulario novo no esquema que a regua nao sabe extrair. Antes de
        # 22/10/2026 isto PASSAVA em silencio, e foi assim que `declarada_por` e
        # `canal_de_leitura` ficaram 37 dias sem ser conferidos por ninguem.
        esquema["vocabularios"]["tipo_de_quarto"] = ["duplo", "triplo"]
    elif mutacao == "sem_entidade_elegibilidade":
        del esquema["entidades"]["ELEGIBILIDADE"]
    elif mutacao == "eleg_sem_campo_na_versao":
        del esquema["entidades"]["VERSAO"]["campos"]["elegibilidade"]
    elif mutacao == "eleg_na_experiencia":
        esquema["entidades"]["EXPERIENCIA"]["campos"]["elegibilidade"] = {
            "tipo": "lista|null", "obrigatorio": True,
            "null_exige": "motivo_sem_elegibilidade"}
    elif mutacao == "sem_regra_da_elegibilidade":
        del esquema["regra_da_elegibilidade"]
    elif mutacao == "sem_os_dois_sentidos":
        del esquema["regra_da_elegibilidade"]["idade_nunca_entra_em_elegibilidade"]
    elif mutacao == "vocab_sem_o_que_se_prova":
        # A regua varre `vocabularios` do esquema: tirar a chave faz o extrator de
        # `o_que_se_prova` conferir vocabulario que nao existe, e a trava de
        # 22/10/2026 e quem ve.
        del esquema["vocabularios"]["o_que_se_prova"]
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
