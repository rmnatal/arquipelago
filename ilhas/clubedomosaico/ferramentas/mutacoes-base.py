#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MUTACOES DA CATEGORIA BASE — 28/09/2026.

Esta bateria e diferente das quatro anteriores desta ilha, e a diferenca esta na
primeira linha do arquivo que ela mede: `dados/materiais-base.json` NAO EXISTE.

A regra desta ilha e que regra escrita sem regua que a meca e promessa. A regra da
categoria `base` (`regras_da_categoria_base` e `ponte_do_tipo_para_o_vocabulario_base`,
no `dados/esquema-banco.json`) nasceu ANTES do primeiro SKU, porque a coleta esbarrou
no egresso — o canal de busca desta execucao devolve resumo e traducao das paginas de
fabricante, e `literal_do_fabricante` e a viga de todo o esquema. Entao a regua nasceu
junto, e ela nao tem banco para ler.

O QUE ESTA BATERIA FAZ, e por que isso e mais forte e nao mais fraco:

  1. FABRICA O MUNDO. Escreve um `dados/materiais-base.json` com CINCO registros, um
     por tipo do vocabulario, cobrindo os tres estados da ponte: dois que POUSAM
     (mdf_cru, cimento), dois SEM VALOR NO VOCABULARIO (ceramica_crua,
     isopor_estrutural) e um que NAO E MATERIAL (moldura, que aponta para o material
     dela). Nenhum deles vai para o repositorio: sao dados de bancada, apagados no
     fim, e os textos de fabricante sao INVENTADOS de proposito e marcados como tal.
  2. Confere que o mundo fabricado PASSA. Portao que reprova tudo nao mede nada.
  3. Muta, uma por vez, e confere que cada defeito e REPROVADO — inclusive os defeitos
     do ESQUEMA, que e o que nenhuma bateria desta ilha media ate hoje: a ponte e
     um documento que mede outro documento.
  4. Restaura tudo, sempre, mesmo quando da errado no meio.

DUAS REGRAS HERDADAS dos blocos anteriores, e as duas mordem aqui:

  (a) Mutacao que o portao ANTIGO ja pegava nao justifica portao novo. Cada mutacao
      roda o `validar-banco.py` duas vezes e separa o que so os portoes novos viram,
      desligando-os por CDM_SEM_PORTAO_BASE e CDM_SEM_PORTAO_PONTE.
  (b) A mutacao mais valiosa e a que PRODUZ O MUNDO que o banco ainda nao tem. Aqui o
      mundo inteiro e produzido, e a m14 vai alem: ela EXECUTA a ponte (acrescenta
      `isopor_eps` ao vocabulario) e mede se o esquema continua coerente no dia em que
      a decisao que hoje espera 30/09 finalmente sair.

Uso:  python3 ferramentas/mutacoes-base.py
"""

import copy
import json
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)
BANCO = os.path.join(ILHA, "dados", "materiais-base.json")
ESQUEMA = os.path.join(ILHA, "dados", "esquema-banco.json")
VALIDAR_BANCO = os.path.join(AQUI, "validar-banco.py")

AVISO_DE_BANCADA = (
    "ARQUIVO DE BANCADA, NAO E BANCO. Gerado por ferramentas/mutacoes-base.py e apagado "
    "por ela no fim da passada. As frases de fabricante aqui dentro sao INVENTADAS para "
    "exercitar o portao da categoria base e NAO podem ser lidas como coleta: nenhum SKU "
    "de base foi coletado ate 28/09/2026, e o motivo esta em "
    "`regras_da_categoria_base.o_que_falta_para_coletar_o_primeiro_SKU`."
)


def fonte(fid, nivel=3):
    return {
        fid: {
            "url": "https://exemplo-de-bancada.invalido/%s" % fid,
            "tipo": "pagina de produto do fabricante (FABRICADA para a bancada)",
            "nivel": nivel,
            "coletado_em": "2026-09-28",
            "conferir_no_pdf": False,
        }
    }


_URL_PRODUTO = None                                   # o mundo fabricado nao tem anuncio casado
_URL_BUSCA = "https://s.shopee.com.br/bancada"        # e tem busca, que e o degrau 4 da 25.1


def afiliado():
    return {
        "programa": "shopee",
        "url": "",
        "url_produto": _URL_PRODUTO,
        "sub_id_1": "clubedomosaico",
        "sub_id_2": "GUIA",
        "etiqueta_ml": None,
        "gerado_em": None,
        "url_busca": _URL_BUSCA,
        "url_busca_produto": "https://shopee.com.br/search?keyword=bancada",
        # O DEGRAU E CALCULADO DOS CAMPOS ACIMA, nunca cravado: sem `url_produto` e com
        # `url_busca`, a 25.1 diz degrau 4 — item que serve so busca. Ele era `None` desde
        # 28/09, quando esta bateria nasceu, e ficou VALIDO por um dia: a leva de 29/09 as
        # 16h17Z tornou o degrau obrigatorio para todo item que serve link de compra, e a
        # partir dali o MUNDO FABRICADO desta bateria passou a ser reprovado ANTES de
        # qualquer mutacao — "portao que reprova o mundo certo nao mede nada". As duas
        # baterias (`base` e `apoio`) ficaram assim, e nao e vermelho inofensivo: bateria
        # que se recusa a rodar deixa os portoes novos das duas categorias SEM NINGUEM
        # MEDINDO, e foi por isso que ninguem viu por um dia inteiro. Achado de passagem em
        # 30/09/2026, medido vermelho no `main` limpo antes de qualquer mudanca desta
        # execucao. Calcular em vez de cravar e o que impede o proximo aperto de regra de
        # apagar esta bateria outra vez.
        "degrau": 4 if _URL_BUSCA and not _URL_PRODUTO else None,
        "url_busca_gerada_em": "2026-09-28",
        "motivo_da_chave": "bancada",
    }


def registro(ident, tipo, literal, trecho, valor_base, nomeia_amb, motivo_sem_valor=None):
    TODOS = ["interno_seco", "interno_molhado", "externo_abrigado",
             "externo_exposto", "contato_permanente_agua"]
    sub = {
        "literal_do_fabricante": literal,
        "fonte_id": "ficha-%s" % ident,
        "valor_do_vocabulario_base": valor_base,
        "ambientes_do_vocabulario_que_a_frase_nomeia": list(nomeia_amb),
        "ambientes_do_vocabulario_que_a_frase_NAO_nomeia":
            [a for a in TODOS if a not in nomeia_amb],
        "preparo_declarado": None,
        "motivo_preparo": "Bancada: o mundo fabricado nao declara preparo.",
        "observacao": "Registro FABRICADO pela bateria de mutacao. Nao e coleta.",
    }
    if valor_base == "sem_valor_no_vocabulario":
        sub["motivo_sem_valor"] = motivo_sem_valor
    else:
        sub["trecho_que_declara_o_material"] = trecho
    return {
        "id": ident,
        "categoria": "base",
        "tipo": tipo,
        "marca": "Bancada",
        "fabricante": "Bancada de Teste Ltda (FABRICADO)",
        "nome_comercial": ident,
        "codigo_fabricante": None,
        "motivo_sem_codigo": "Bancada: o mundo fabricado nao tem codigo de catalogo.",
        "declaracoes": {
            "indicado_para": [],
            "nao_usar_em": [],
            "nao_recomendado_em": [],
            "nao_indicado_para": [],
            "ambientes_declarados": [],
            "resistencias_declaradas": [],
        },
        "motivo_declaracoes_vazias": (
            "Base nao adere sobre nada — ela E a superficie. Ver "
            "`regras_da_categoria_base.a_matriz_base_x_ambiente_fica_VAZIA_e_o_motivo`."
        ),
        "substrato": sub,
        "propriedades": {
            "forma": {
                "valor": "nao_declarada",
                "unidade": None,
                "fonte_id": "ficha-%s" % ident,
                "declarado_como": "bancada",
            },
            "absorcao_declarada": {
                "valor": None,
                "unidade": None,
                "motivo": "Bancada: o mundo fabricado nao declara absorcao.",
            },
        },
        "venda": [],
        "afiliado": afiliado(),
        "imagem": None,
        "fontes": fonte("ficha-%s" % ident),
        "divergencias": [],
        "resolucao": None,
        "status": "ativo",
        "motivo_do_descarte": None,
        "usada_por": [],
        "observacao": "FABRICADO para a bancada.",
    }


def mundo():
    itens = [
        registro(
            "bancada-disco-mdf", "mdf_cru",
            "painel de MDF cru para uso interno, indicado para receber pintura e revestimento",
            "painel de MDF cru", "mdf_madeira", ["interno_seco"],
        ),
        registro(
            "bancada-tampo-cimento", "cimento",
            "peca moldada em concreto, resistente a area externa exposta ao sol e a chuva",
            "moldada em concreto", "cimento_concreto",
            ["interno_seco", "externo_abrigado", "externo_exposto"],
        ),
        registro(
            "bancada-vaso-barro", "ceramica_crua",
            "vaso de barro cru, sem esmalte, absorve agua pela parede",
            "vaso de barro cru", "sem_valor_no_vocabulario", ["interno_seco"],
            motivo_sem_valor=(
                "O unico valor de ceramica no eixo e `ceramica_esmaltada_porcelana`, que e a "
                "ceramica VIDRADA. Barro cru absorve; esmaltada nao. Ver a ponte."
            ),
        ),
        registro(
            "bancada-esfera-isopor", "isopor_estrutural",
            "esfera de poliestireno expandido para artesanato, nao usar produto a base de solvente",
            "poliestireno expandido", "sem_valor_no_vocabulario", ["interno_seco"],
            motivo_sem_valor=(
                "Nao ha valor de poliestireno expandido no eixo. Ver a ponte e a linha "
                "`poliestireno expandido` de `termos_que_nao_traduzem`."
            ),
        ),
        registro(
            "bancada-moldura-mdf", "moldura",
            "moldura em MDF cru para quadro e espelho, uso interno",
            "moldura em MDF cru", "mdf_madeira", ["interno_seco"],
        ),
    ]
    return {
        "id": "materiais-base",
        "ilha": "clubedomosaico",
        "categoria": "base",
        "bloco": "BANCADA — nao e coleta",
        "gerado_em": "2026-09-28",
        "esquema": "dados/esquema-banco.json",
        "o_que_este_arquivo_e": AVISO_DE_BANCADA,
        "afiliado": {
            "itens_esperando_link": len(itens),
            "itens_sem_saida_de_compra": 0,
            "itens_com_piso_nao_rastreavel": 0,
        },
        "imagens": {"itens_sem_imagem": len(itens)},
        "materiais": itens,
    }


def item(banco, ident):
    for m in banco["materiais"]:
        if m["id"] == ident:
            return m
    raise SystemExit("mutacao aponta para item inexistente: %s" % ident)


# ------------------------------------------- as mutacoes DO REGISTRO (banco)

def m01(b, e):
    """O objeto inteiro apagado: a base vira um material sem o que a define."""
    del item(b, "bancada-disco-mdf")["substrato"]


def m02(b, e):
    """A frase do fabricante sumida com as listas intactas — o dado 'parece'
    completo e ninguem consegue conferir de onde o material saiu."""
    item(b, "bancada-tampo-cimento")["substrato"]["literal_do_fabricante"] = ""


def m03(b, e):
    """O material deduzido do NOME COMERCIAL: o trecho some e o valor fica. E o
    defeito que a mutacao 05 do acabamento achou, na versao desta categoria —
    'disco MDF 20 cm' e nome de produto, nao declaracao tecnica."""
    del item(b, "bancada-disco-mdf")["substrato"]["trecho_que_declara_o_material"]


def m04(b, e):
    """O trecho existe mas nao sai da frase: e uma segunda frase escrita por quem
    preencheu, que e a parafrase de novo."""
    item(b, "bancada-disco-mdf")["substrato"]["trecho_que_declara_o_material"] = \
        "fabricado em madeira de reflorestamento"


def m05(b, e):
    """O buraco escondido pelo vizinho: o vaso de barro cru entra como ceramica
    ESMALTADA. As duas absorvem de maneira oposta, e a ponte diz que o tipo nao
    pousa em lugar nenhum — este e o defeito mais caro desta categoria, porque
    ele nao deixa rastro: some um buraco e nasce uma recomendacao errada."""
    sub = item(b, "bancada-vaso-barro")["substrato"]
    sub["valor_do_vocabulario_base"] = "ceramica_esmaltada_porcelana"
    sub["trecho_que_declara_o_material"] = "vaso de barro cru"
    sub.pop("motivo_sem_valor", None)


def m06(b, e):
    """O contrario: um tipo que POUSA se declara sem valor. Inventa um buraco que
    a ponte nao reconhece, e buraco inventado gasta o credito dos de verdade."""
    sub = item(b, "bancada-tampo-cimento")["substrato"]
    sub["valor_do_vocabulario_base"] = "sem_valor_no_vocabulario"
    sub["motivo_sem_valor"] = "inventado"
    sub.pop("trecho_que_declara_o_material", None)


def m07(b, e):
    """Um ambiente do vocabulario que nao entra em NENHUMA das duas listas: o
    silencio nao lido, que e como faixa descoberta fica invisivel."""
    sub = item(b, "bancada-tampo-cimento")["substrato"]
    sub["ambientes_do_vocabulario_que_a_frase_NAO_nomeia"] = [
        a for a in sub["ambientes_do_vocabulario_que_a_frase_NAO_nomeia"]
        if a != "contato_permanente_agua"
    ]


def m08(b, e):
    """`preparo_declarado` removido. E o campo que liga esta categoria ao selador
    do banco de acabamento (`momento_de_uso: antes_de_colar`) — sem ele, a
    pergunta 'precisa selar antes?' nunca e feita a registro nenhum."""
    del item(b, "bancada-disco-mdf")["substrato"]["preparo_declarado"]


def m09(b, e):
    """`absorcao_declarada` removido. Mesma familia do `contato_com_alimento` do
    acabamento: e a pergunta que decide a regra 6 da F2 e a que separa barro cru
    de ceramica esmaltada."""
    del item(b, "bancada-vaso-barro")["propriedades"]["absorcao_declarada"]


def m10(b, e):
    """Propriedade com nome livre: `diametro` onde o esquema fixou `diametro_cm`.
    Aqui as propriedades sao MEDIDA, e medida com nome livre e o que faz a F1 ler
    um registro e nao o outro."""
    item(b, "bancada-disco-mdf")["propriedades"]["diametro"] = {
        "valor": 20, "unidade": "cm", "fonte_id": "ficha-bancada-disco-mdf",
        "declarado_como": "20 cm",
    }


def m11(b, e):
    """Forma fora de `vocabularios.forma_da_base` — 'retangulo' nao e uma das seis
    formas que a F1 calcula, e a F1 nao saberia o que fazer com ela."""
    item(b, "bancada-moldura-mdf")["propriedades"]["forma"]["valor"] = "retangulo"


def m12(b, e):
    """A matriz base x ambiente preenchida numa BASE. Um disco de MDF em
    `indicado_para` entra na traducao do mapa de termos e a F2 passa a oferecer
    madeira como candidata a COLAR madeira."""
    item(b, "bancada-disco-mdf")["declaracoes"]["indicado_para"] = ["MDF"]


def m13(b, e):
    """A moldura gravando o proprio nome do tipo como base. A ponte diz que
    moldura NAO E MATERIAL; gravar 'moldura' no eixo criaria um valor que a F2
    nunca pergunta e que nenhuma cola declara."""
    item(b, "bancada-moldura-mdf")["substrato"]["valor_do_vocabulario_base"] = "moldura"


# ------------------------------------------- as mutacoes DO ESQUEMA (a ponte)

def m14(b, e):
    """PRODUZ O MUNDO: a ponte E EXECUTADA — `isopor_eps` entra em
    `vocabularios.base` — e o estado do tipo fica para tras em
    `sem_valor_no_vocabulario`. E exatamente o mundo do dia seguinte a 30/09, e o
    portao tem de acusar que a ponte envelheceu no mesmo commit em que o
    vocabulario cresceu. Sem esta mutacao a ponte viraria, ela propria, o resumo
    velho lido como fato da secao 4 do contrato."""
    e["vocabularios"]["base"].append("isopor_eps")


def m15(b, e):
    """Um tipo do vocabulario apagado da ponte: volta a ser possivel um tipo de
    base calado, que e o estado em que os tres estavam ate 28/09/2026."""
    del e["ponte_do_tipo_para_o_vocabulario_base"]["tipos"]["ceramica_crua"]


def m16(b, e):
    """`sem_valor_no_vocabulario` sem `valor_proposto`: buraco sem nome e buraco
    que a proxima execucao redescobre do zero."""
    del e["ponte_do_tipo_para_o_vocabulario_base"]["tipos"]["isopor_estrutural"]["valor_proposto"]


def m17(b, e):
    """`nao_e_material` sem `onde_ele_e`: a moldura desaparece do arquipelago em
    vez de ir para a F1."""
    del e["ponte_do_tipo_para_o_vocabulario_base"]["tipos"]["moldura"]["onde_ele_e"]


def m18(b, e):
    """A linha condicional do mapa de termos sai da ponte. E a reconstituicao
    exata do defeito que esta secao nasceu para fechar: `poliestireno expandido`
    recusa a traducao SOB CONDICAO ('se virar base, entra no vocabulario
    primeiro'), a condicao ja estava cumprida no mesmo arquivo, e nada conferia as
    duas linhas juntas."""
    linhas = e["ponte_do_tipo_para_o_vocabulario_base"]["condicionais_do_mapa_de_termos"]["linhas"]
    e["ponte_do_tipo_para_o_vocabulario_base"]["condicionais_do_mapa_de_termos"]["linhas"] = [
        l for l in linhas if l["literal"] != "poliestireno expandido"
    ]


def m19(b, e):
    """A medicao da condicional sem `por_onde`: 'cumprida' sem dizer por onde foi
    medida e opiniao com cara de numero."""
    e["ponte_do_tipo_para_o_vocabulario_base"]["condicionais_do_mapa_de_termos"]["linhas"][0].pop("por_onde")


def m20(b, e):
    """Um tipo pousando em valor que nao existe no eixo. A ponte apontaria para
    fora do vocabulario e nada acusaria."""
    e["ponte_do_tipo_para_o_vocabulario_base"]["tipos"]["mdf_cru"]["pousa_em"] = ["madeira"]


MUTACOES = [
    ("01 o objeto `substrato` inteiro apagado", m01),
    ("02 a frase do fabricante sumida, listas intactas", m02),
    ("03 material deduzido do nome comercial (trecho some)", m03),
    ("04 trecho que nao sai da frase literal", m04),
    ("05 barro cru escondido como ceramica esmaltada", m05),
    ("06 tipo que pousa se declarando sem valor", m06),
    ("07 ambiente fora das duas listas (silencio nao lido)", m07),
    ("08 `preparo_declarado` removido", m08),
    ("09 `absorcao_declarada` removida", m09),
    ("10 propriedade com nome livre (diametro)", m10),
    ("11 forma fora do vocabulario da F1", m11),
    ("12 matriz base x ambiente preenchida numa BASE", m12),
    ("13 moldura gravando o proprio tipo como base", m13),
    ("14 PRODUZ O MUNDO: a ponte executada e nao atualizada", m14),
    ("15 tipo do vocabulario apagado da ponte", m15),
    ("16 `sem_valor_no_vocabulario` sem `valor_proposto`", m16),
    ("17 `nao_e_material` sem `onde_ele_e`", m17),
    ("18 condicional do mapa de termos fora da ponte", m18),
    ("19 condicional medida sem `por_onde`", m19),
    ("20 ponte apontando para base inexistente", m20),
]


def roda(sem_portao_novo=False):
    env = dict(os.environ)
    if sem_portao_novo:
        env["CDM_SEM_PORTAO_BASE"] = "1"
        env["CDM_SEM_PORTAO_PONTE"] = "1"
    r = subprocess.run([sys.executable, VALIDAR_BANCO], capture_output=True,
                       text=True, cwd=ILHA, env=env)
    return r.returncode != 0


def grava(caminho, conteudo):
    with open(caminho, "w", encoding="utf-8") as fh:
        json.dump(conteudo, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def main():
    if os.path.exists(BANCO):
        print("FALHA: dados/materiais-base.json JA EXISTE. Esta bateria fabrica o proprio "
              "mundo e se recusa a passar por cima de coleta de verdade — quando a "
              "categoria for coletada, esta bateria muda para o desenho das outras quatro, "
              "que mutam o banco real.")
        return 1

    esquema_original = json.load(open(ESQUEMA, encoding="utf-8"))
    banco_original = mundo()

    try:
        grava(BANCO, banco_original)
        if roda():
            print("FALHA: o mundo FABRICADO ja esta reprovado antes de qualquer mutacao. "
                  "Portao que reprova o mundo certo nao mede nada.")
            subprocess.run([sys.executable, VALIDAR_BANCO], cwd=ILHA)
            return 1
        if roda(sem_portao_novo=True):
            print("FALHA: o mundo fabricado ja esta reprovado com os portoes novos desligados")
            return 1

        print("Mutacoes da categoria BASE — %d escritas (13 no registro, 7 no esquema)"
              % len(MUTACOES))
        print("")
        reprovadas = 0
        so_o_portao_novo = 0
        for nome, funcao in MUTACOES:
            banco = copy.deepcopy(banco_original)
            esq = copy.deepcopy(esquema_original)
            funcao(banco, esq)
            if banco == banco_original and esq == esquema_original:
                print("  INERTE  %s — a mutacao nao mudou nada" % nome)
                continue
            grava(BANCO, banco)
            grava(ESQUEMA, esq)
            try:
                pegou = roda()
                pegou_sem = roda(sem_portao_novo=True)
            finally:
                grava(BANCO, banco_original)
                grava(ESQUEMA, esquema_original)

            if pegou:
                reprovadas += 1
                if not pegou_sem:
                    so_o_portao_novo += 1
                    print("  REPROVOU  %-54s (so o portao novo viu)" % nome)
                else:
                    print("  REPROVOU  %-54s (o esquema ja pegava)" % nome)
            else:
                print("  PASSOU    %-54s  <-- NENHUM PORTAO VIU" % nome)
    finally:
        grava(ESQUEMA, esquema_original)
        if os.path.exists(BANCO):
            os.remove(BANCO)

    print("")
    print("  reprovadas ..................... %d de %d" % (reprovadas, len(MUTACOES)))
    print("  so o portao novo viu ........... %d" % so_o_portao_novo)
    print("  o mundo fabricado foi apagado; dados/materiais-base.json continua sem existir.")
    if reprovadas != len(MUTACOES):
        print("\nREPROVADO: mutacao que passa e buraco de portao.")
        return 1
    if so_o_portao_novo == 0:
        print("\nREPROVADO: se o esquema antigo pega tudo, o portao novo nao se justifica.")
        return 1
    print("\nOK: as %d mutacoes reprovaram." % len(MUTACOES))
    return 0


if __name__ == "__main__":
    sys.exit(main())
