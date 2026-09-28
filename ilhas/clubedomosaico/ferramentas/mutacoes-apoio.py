#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MUTACOES DA CATEGORIA APOIO — 28/09/2026.

Segunda bateria desta ilha que FABRICA O PROPRIO MUNDO, pelo mesmo motivo da
primeira (`mutacoes-base.py`, da mesma manha): `dados/materiais-apoio.json` NAO
EXISTE. A regra da categoria (`regras_da_categoria_apoio`,
`ponte_do_tipo_de_apoio_para_o_ramo` e
`exigencias_de_apoio_ja_declaradas_no_banco`, no `dados/esquema-banco.json`)
nasceu ANTES do primeiro SKU, e regra escrita sem regua que a meca e promessa.

O QUE ELA MEDE ALEM DO QUE A DA BASE MEDIA, e e uma coisa so mas e grande: esta
categoria tem um portao que NAO OLHA registro de apoio nenhum. A varredura de
`exigencias_de_apoio_ja_declaradas_no_banco` le as OUTRAS categorias, porque a
declaracao que mais importa aqui vem do outro lado do balcao — quem diz qual
desempenadeira usar e o fabricante da PASTILHA, nao o da desempenadeira. Entao as
mutacoes 15 a 22 mutam registros que ja existem no banco de verdade (a AF1500, a
Cascorez, o verniz de pisos) e o esquema, e nao o mundo fabricado.

AS TRES REGRAS HERDADAS, e as tres mordem aqui:

  (a) Mutacao que o portao ANTIGO ja pegava nao justifica portao novo: cada uma
      roda o validador duas vezes e separa o que so o portao novo viu, desligando
      por CDM_SEM_PORTAO_APOIO.
  (b) A mutacao mais valiosa e a que PRODUZ O MUNDO que o banco ainda nao tem. A
      m21 executa a decisao que hoje esta escrita como pendente — `pincel` entra
      em `tipo_por_categoria.apoio` — e mede se o indice acusa que envelheceu no
      mesmo commit em que o vocabulario cresceu.
  (c) O banco de verdade e SEMPRE restaurado, inclusive quando da errado no meio.

Uso:  python3 ferramentas/mutacoes-apoio.py
"""

import copy
import json
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)
BANCO = os.path.join(ILHA, "dados", "materiais-apoio.json")
ESQUEMA = os.path.join(ILHA, "dados", "esquema-banco.json")
PASTILHAS = os.path.join(ILHA, "dados", "materiais-pastilhas.json")
COLAS = os.path.join(ILHA, "dados", "materiais-colas.json")
ACABAMENTO = os.path.join(ILHA, "dados", "materiais-acabamento.json")
VALIDAR_BANCO = os.path.join(AQUI, "validar-banco.py")

AVISO_DE_BANCADA = (
    "ARQUIVO DE BANCADA, NAO E BANCO. Gerado por ferramentas/mutacoes-apoio.py e apagado por ela "
    "no fim da passada. As frases de fabricante aqui dentro sao INVENTADAS para exercitar o portao "
    "da categoria apoio e NAO podem ser lidas como coleta: nenhum SKU de apoio foi coletado ate "
    "28/09/2026, e o motivo esta em "
    "`regras_da_categoria_apoio.o_que_falta_para_coletar_o_primeiro_SKU`."
)

TESSELAS = ["pastilha_vidro", "pastilha_ceramica", "caco_azulejo",
            "caco_louca", "caco_espelho", "pedra"]


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


def afiliado():
    return {
        "programa": "shopee",
        "url": "",
        "url_produto": None,
        "sub_id_1": "clubedomosaico",
        "sub_id_2": "GUIA",
        "etiqueta_ml": None,
        "gerado_em": None,
        "url_busca": "https://s.shopee.com.br/bancada",
        "url_busca_produto": "https://shopee.com.br/search?keyword=bancada",
        "degrau": None,
        "url_busca_gerada_em": "2026-09-28",
        "motivo_da_chave": "bancada",
    }


def registro(ident, tipo, ramo, literal, material, trecho_material,
             etapa, trecho_etapa, nomeia_tessela, age_sobre_rejunte,
             motivo_material=None, motivo_etapa=None, extras=None):
    sv = {
        "literal_do_fabricante": literal,
        "fonte_id": "ficha-%s" % ident,
        "ramo": ramo,
        "material_de_contato": material,
        "etapa": etapa,
        "tesselas_do_vocabulario_que_a_frase_nomeia": list(nomeia_tessela),
        "tesselas_do_vocabulario_que_a_frase_NAO_nomeia":
            [t for t in TESSELAS if t not in nomeia_tessela],
        "age_sobre_rejunte": age_sobre_rejunte,
        "observacao": "Registro FABRICADO pela bateria de mutacao. Nao e coleta.",
    }
    if material == "nao_declarado":
        sv["motivo_material_de_contato"] = motivo_material
    else:
        sv["trecho_que_declara_o_material_de_contato"] = trecho_material
    if etapa == "nao_declarada":
        sv["motivo_da_etapa"] = motivo_etapa
    else:
        sv["trecho_que_declara_a_etapa"] = trecho_etapa

    props = {
        "risco_declarado": {
            "valor": None,
            "unidade": None,
            "motivo": "Bancada: o mundo fabricado nao declara risco.",
        },
    }
    props.update(extras or {})
    return {
        "id": ident,
        "categoria": "apoio",
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
            "Apoio nao adere nada a nada. Ver "
            "`regras_da_categoria_apoio.a_matriz_base_x_ambiente_fica_VAZIA_e_o_motivo`."
        ),
        "servico": sv,
        "propriedades": props,
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
            "bancada-desempenadeira", "desempenadeira", "ferramenta_de_aplicacao",
            "desempenadeira com face de borracha macia, para espalhar e remover o excesso de "
            "rejunte sobre pastilha de vidro sem riscar",
            "borracha", "face de borracha macia",
            "rejuntar", "remover o excesso de rejunte",
            ["pastilha_vidro"], True,
            extras={
                "dureza_shore_a": {
                    "valor": 45, "unidade": "Shore A", "fonte_id": "ficha-bancada-desempenadeira",
                    "declarado_como": "borracha macia",
                },
            },
        ),
        registro(
            "bancada-espatula", "espatula", "ferramenta_de_aplicacao",
            "espatula dentada para aplicar a cola sobre a base antes de assentar",
            "nao_declarado", None,
            "colar", "aplicar a cola sobre a base",
            [], False,
            motivo_material="O fabricante nomeia a ferramenta e nao declara o material da lamina.",
        ),
        registro(
            "bancada-luva", "luva", "equipamento_de_protecao_individual",
            "luva de seguranca para manuseio de material cortante",
            "nao_declarado", None,
            "nao_declarada", None,
            [], False,
            motivo_material="O fabricante declara a luva inteira e nao separa a face de contato.",
            motivo_etapa=("A frase nao diz em que etapa da montagem a luva entra: ela fala de "
                          "material cortante, que aparece no corte e na limpeza."),
        ),
        registro(
            "bancada-oculos", "oculos", "equipamento_de_protecao_individual",
            "oculos de protecao contra impacto de particulas durante o corte",
            "nao_declarado", None,
            "cortar", "durante o corte",
            [], False,
            motivo_material="Nao ha face de contato com a peca: o item protege a pessoa.",
        ),
    ]
    return {
        "id": "materiais-apoio",
        "ilha": "clubedomosaico",
        "categoria": "apoio",
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


def reg_de(arq, ident):
    for m in arq["materiais"]:
        if m["id"] == ident:
            return m
    raise SystemExit("mutacao aponta para registro inexistente no banco real: %s" % ident)


# --------------------------------- as mutacoes DO REGISTRO (mundo fabricado)

def m01(b, e, r):
    """O objeto inteiro apagado: o apoio vira um produto sem o que o define."""
    del item(b, "bancada-desempenadeira")["servico"]


def m02(b, e, r):
    """A frase do fabricante sumida com os campos intactos: o dado 'parece'
    completo e ninguem consegue conferir de onde saiu."""
    item(b, "bancada-espatula")["servico"]["literal_do_fabricante"] = ""


def m03(b, e, r):
    """O RAMO TROCADO: a luva gravada como ferramenta de aplicacao. Some da lista
    de quem se protege e aparece na de quem procura o que encosta na peca — e as
    duas listas existem justamente porque o erro custa coisas diferentes."""
    item(b, "bancada-luva")["servico"]["ramo"] = "ferramenta_de_aplicacao"


def m04(b, e, r):
    """O contrario: a desempenadeira virando EPI. Sai da lista de ferramenta e
    entra na de protecao, onde ninguem a procura."""
    item(b, "bancada-desempenadeira")["servico"]["ramo"] = "equipamento_de_protecao_individual"


def m05(b, e, r):
    """`material_de_contato` deduzido do nome comercial: o trecho some e o valor
    fica. E o defeito que a mutacao 05 do acabamento achou, na versao desta
    categoria — e aqui ele e o mais caro de todos, porque o material da face e
    exatamente o que a unica declaracao do banco sobre apoio nomeia."""
    del item(b, "bancada-desempenadeira")["servico"]["trecho_que_declara_o_material_de_contato"]


def m06(b, e, r):
    """O trecho existe e nao sai da frase: e uma segunda frase escrita por quem
    preencheu, que e a parafrase de volta."""
    item(b, "bancada-desempenadeira")["servico"]["trecho_que_declara_o_material_de_contato"] = \
        "cabo ergonomico de plastico"


def m07(b, e, r):
    """`material_de_contato` nao declarado e sem motivo: silencio indistinguivel
    de coleta que ninguem fez."""
    del item(b, "bancada-espatula")["servico"]["motivo_material_de_contato"]


def m08(b, e, r):
    """A ETAPA DEDUZIDA DO MECANISMO: a luva ganha `cortar` sem que o fabricante
    diga a etapa. Deducao com cara de declaracao e o que a secao 8 do
    ARQUIPELAGO.md proibe, e foi por ela que o `momento_de_uso` do acabamento
    ganhou o trecho obrigatorio."""
    sv = item(b, "bancada-luva")["servico"]
    sv["etapa"] = "cortar"
    sv.pop("motivo_da_etapa", None)


def m09(b, e, r):
    """`trecho_que_declara_a_etapa` que nao sai da frase literal."""
    item(b, "bancada-oculos")["servico"]["trecho_que_declara_a_etapa"] = "ao rejuntar a peca"


def m10(b, e, r):
    """Uma tessela do vocabulario fora das DUAS listas: o silencio nao lido, que
    e como faixa descoberta fica invisivel."""
    sv = item(b, "bancada-desempenadeira")["servico"]
    sv["tesselas_do_vocabulario_que_a_frase_NAO_nomeia"] = [
        t for t in sv["tesselas_do_vocabulario_que_a_frase_NAO_nomeia"] if t != "pedra"
    ]


def m11(b, e, r):
    """`age_sobre_rejunte` removido. Rejunte nao e valor de `material_tessela`
    nem de `base`, e e metade da superficie exposta da peca: sem o campo a
    pergunta nao e feita a registro nenhum."""
    del item(b, "bancada-desempenadeira")["servico"]["age_sobre_rejunte"]


def m12(b, e, r):
    """A matriz base x ambiente preenchida num APOIO: a desempenadeira entra na
    traducao do mapa de termos e vira candidata a COLAR peca."""
    item(b, "bancada-espatula")["declaracoes"]["indicado_para"] = ["ceramica"]


def m13(b, e, r):
    """Propriedade com nome livre: `dureza` onde o esquema fixou
    `dureza_shore_a`."""
    item(b, "bancada-desempenadeira")["propriedades"]["dureza"] = {
        "valor": 45, "unidade": "Shore A", "fonte_id": "ficha-bancada-desempenadeira",
        "declarado_como": "borracha macia",
    }


def m14(b, e, r):
    """`risco_declarado` removido de um EPI. E a pergunta que o campo ausente faz
    ninguem fazer, e num oculos ela e a unica pergunta que existe."""
    del item(b, "bancada-oculos")["propriedades"]["risco_declarado"]


# ------------- as mutacoes DO BANCO DE VERDADE (a varredura do outro lado do balcao)

def m15(b, e, r):
    """A DECLARACAO QUE VOLTA A SER DESCARTADA EM SILENCIO: a linha da AF1500 sai
    de `ocorrencias` e a frase do fabricante continua no banco. E a reconstituicao
    exata do defeito que esta secao nasceu para fechar."""
    oc = e["exigencias_de_apoio_ja_declaradas_no_banco"]["ocorrencias"]
    e["exigencias_de_apoio_ja_declaradas_no_banco"]["ocorrencias"] = [
        o for o in oc
        if not (o["registro"] == "pastilhart-af1500"
                and o["campo"] == "propriedades.assentamento_recomendado.declarado_como")
    ]


def m16(b, e, r):
    """A OUTRA DIRECAO: a frase do fabricante muda no banco e a linha continua
    listada. Linha que sobrevive ao que a sustentava e resumo velho lido como
    fato — a secao 4 do contrato dentro de um arquivo de dados."""
    reg = reg_de(r["pastilhas"], "pastilhart-af1500")
    reg["propriedades"]["assentamento_recomendado"]["declarado_como"] = \
        "utilizar argamassa branca e rejunte flexivel de boa qualidade"
    reg["preparo"] = "Argamassa branca e rejunte flexivel."


def m17(b, e, r):
    """Uma frase NOVA de fabricante nomeando luva, num registro que hoje nao
    nomeia nenhuma. E o mundo do dia em que a FISPQ do epoxi for lida: o portao
    tem de exigir a linha no mesmo commit em que a frase entra."""
    reg = reg_de(r["colas"], "loctite-durepoxi")
    reg["preparo"] = ((reg.get("preparo") or "") +
                      " Usar luvas de protecao durante o manuseio.").strip()


def m18(b, e, r):
    """O termo sai dos vigiados e a ocorrencia fica listada: a lista apontaria
    para um termo que ninguem mede mais."""
    del e["exigencias_de_apoio_ja_declaradas_no_banco"]["termos_vigiados"]["desempenadeira"]


def m19(b, e, r):
    """`campos_que_carregam_frase_de_fabricante` esvaziado: a varredura passaria
    verde sobre um banco inteiro sem ler uma linha."""
    e["exigencias_de_apoio_ja_declaradas_no_banco"]["campos_que_carregam_frase_de_fabricante"] = []


def m20(b, e, r):
    """`aerossol` marcado como buraco de vocabulario em vez de embalagem. A
    proxima execucao criaria um tipo de apoio chamado aerossol, que nao e
    ferramenta nenhuma."""
    t = e["exigencias_de_apoio_ja_declaradas_no_banco"]["termos_vigiados"]["aerossol"]
    t["estado"] = "sem_valor_no_vocabulario"
    t["valor_proposto"] = "aerossol"
    t["o_que_falta"] = "nada"


# ----------------------------------------- as mutacoes DO ESQUEMA (as duas pontes)

def m21(b, e, r):
    """PRODUZ O MUNDO: a decisao pendente E EXECUTADA — `pincel` entra em
    `tipo_por_categoria.apoio` — e o indice fica para tras dizendo
    `sem_valor_no_vocabulario`. E o dia seguinte ao primeiro SKU de pincel, e o
    portao tem de acusar que o indice envelheceu no mesmo commit em que o
    vocabulario cresceu. Sem esta mutacao o indice viraria, ele proprio, o resumo
    velho lido como fato."""
    e["vocabularios"]["tipo_por_categoria"]["apoio"].append("pincel")


def m22(b, e, r):
    """Um tipo do vocabulario apagado da ponte do ramo: volta a ser possivel um
    apoio que a vitrine nao sabe se protege a peca ou a pessoa."""
    del e["ponte_do_tipo_de_apoio_para_o_ramo"]["tipos"]["marcador"]


def m23(b, e, r):
    """A ponte apontando para um ramo que nao existe no vocabulario."""
    e["ponte_do_tipo_de_apoio_para_o_ramo"]["tipos"]["pinca"]["ramo"] = "ferramenta"


def m24(b, e, r):
    """Um terceiro valor de `material_de_contato_do_apoio` nascendo por previsao,
    sem nenhuma frase de fabricante que o declare e sem registro que o use.
    Vocabulario que cresce por previsao vira promessa vazia — a cicatriz que a
    ohmetria pagou, escrita aqui como portao."""
    e["vocabularios"]["material_de_contato_do_apoio"].insert(0, "aco_inox")


MUTACOES = [
    ("01 o objeto `servico` inteiro apagado", m01),
    ("02 a frase do fabricante sumida, campos intactos", m02),
    ("03 luva gravada como ferramenta de aplicacao", m03),
    ("04 desempenadeira gravada como EPI", m04),
    ("05 material de contato deduzido do nome (trecho some)", m05),
    ("06 trecho de material que nao sai da frase", m06),
    ("07 material nao declarado e sem motivo", m07),
    ("08 etapa deduzida do mecanismo do produto", m08),
    ("09 trecho de etapa que nao sai da frase", m09),
    ("10 tessela fora das duas listas (silencio nao lido)", m10),
    ("11 `age_sobre_rejunte` removido", m11),
    ("12 matriz base x ambiente preenchida num APOIO", m12),
    ("13 propriedade com nome livre (dureza)", m13),
    ("14 `risco_declarado` removido de um EPI", m14),
    ("15 declaracao da AF1500 fora de `ocorrencias`", m15),
    ("16 frase do fabricante muda e a linha continua listada", m16),
    ("17 frase NOVA nomeando luva no epoxi, sem linha", m17),
    ("18 termo vigiado apagado com ocorrencia listada", m18),
    ("19 campos de frase de fabricante esvaziados", m19),
    ("20 `aerossol` lido como buraco de vocabulario", m20),
    ("21 PRODUZ O MUNDO: `pincel` no vocabulario, indice velho", m21),
    ("22 tipo de apoio apagado da ponte do ramo", m22),
    ("23 ponte apontando para ramo inexistente", m23),
    ("24 material de contato nascendo por previsao", m24),
]


def roda(sem_portao_novo=False):
    env = dict(os.environ)
    if sem_portao_novo:
        env["CDM_SEM_PORTAO_APOIO"] = "1"
    r = subprocess.run([sys.executable, VALIDAR_BANCO], capture_output=True,
                       text=True, cwd=ILHA, env=env)
    return r.returncode != 0


def grava(caminho, conteudo):
    with open(caminho, "w", encoding="utf-8") as fh:
        json.dump(conteudo, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def main():
    if os.path.exists(BANCO):
        print("FALHA: dados/materiais-apoio.json JA EXISTE. Esta bateria fabrica o proprio mundo e "
              "se recusa a passar por cima de coleta de verdade — quando a categoria for coletada, "
              "ela muda para o desenho das que mutam o banco real.")
        return 1

    esquema_original = json.load(open(ESQUEMA, encoding="utf-8"))
    reais_originais = {
        "pastilhas": json.load(open(PASTILHAS, encoding="utf-8")),
        "colas": json.load(open(COLAS, encoding="utf-8")),
        "acabamento": json.load(open(ACABAMENTO, encoding="utf-8")),
    }
    caminho_real = {"pastilhas": PASTILHAS, "colas": COLAS, "acabamento": ACABAMENTO}
    banco_original = mundo()

    try:
        grava(BANCO, banco_original)
        if roda():
            print("FALHA: o mundo FABRICADO ja esta reprovado antes de qualquer mutacao. Portao "
                  "que reprova o mundo certo nao mede nada.")
            subprocess.run([sys.executable, VALIDAR_BANCO], cwd=ILHA)
            return 1
        if roda(sem_portao_novo=True):
            print("FALHA: o mundo fabricado ja esta reprovado com o portao novo desligado")
            return 1

        print("Mutacoes da categoria APOIO — %d escritas (14 no mundo fabricado, "
              "6 no banco de verdade, 4 no esquema)" % len(MUTACOES))
        print("")
        reprovadas = 0
        so_o_portao_novo = 0
        for nome, funcao in MUTACOES:
            banco = copy.deepcopy(banco_original)
            esq = copy.deepcopy(esquema_original)
            reais = copy.deepcopy(reais_originais)
            funcao(banco, esq, reais)
            if banco == banco_original and esq == esquema_original and reais == reais_originais:
                print("  INERTE  %s — a mutacao nao mudou nada" % nome)
                continue
            grava(BANCO, banco)
            grava(ESQUEMA, esq)
            for chave, conteudo in reais.items():
                grava(caminho_real[chave], conteudo)
            try:
                pegou = roda()
                pegou_sem = roda(sem_portao_novo=True)
            finally:
                grava(BANCO, banco_original)
                grava(ESQUEMA, esquema_original)
                for chave, conteudo in reais_originais.items():
                    grava(caminho_real[chave], conteudo)

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
        for chave, conteudo in reais_originais.items():
            grava(caminho_real[chave], conteudo)
        if os.path.exists(BANCO):
            os.remove(BANCO)

    print("")
    print("  reprovadas ..................... %d de %d" % (reprovadas, len(MUTACOES)))
    print("  so o portao novo viu ........... %d" % so_o_portao_novo)
    print("  o mundo fabricado foi apagado; dados/materiais-apoio.json continua sem existir,")
    print("  e os tres bancos de verdade foram restaurados byte a byte.")
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
