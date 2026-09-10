#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o combustivel da R1 em PHP a partir da implementacao de REFERENCIA.

    python3 ferramentas/gerar-r1.py            # relatorio na tela
    python3 ferramentas/gerar-r1.py --gravar   # grava os dois arquivos abaixo

Grava:
  dados/r1-respostas.json   FATOS, sem prosa. E o que o site consome: o Sync o
                            leva para a option robometria_dados_r1-respostas e o
                            snippet robometria-r1.php monta as frases a partir
                            dele. publicar=true no manifest.
  dados/r1-referencia.json  GABARITO: as mesmas respostas ja em frase, escritas
                            pela implementacao de referencia
                            (ferramentas/cobertura-r1.py). publicar=false — nao
                            vai para o site; existe para ferramentas/teste-r1.php
                            comparar, modelo a modelo, o que o PHP escreve com o
                            que a referencia escreve.

POR QUE ASSIM, e nao reescrevendo a regra da R1 em PHP.

A especificacao (dados/especificacao-calculadoras.md, secao 1) e o PROMPT.md da
ilha dizem que "a saida do snippet PHP tem que BATER com a da referencia".
Reescrever as regras — os tres selos, o conjunto mais estreito, o kit que
responde por uma peca que o fabricante nao vende avulsa, o aviso de variante de
hardware — dentro de um snippet que so da para rodar com o site no ar seria
escrever a regra onde ela nao pode ser conferida, que e exatamente o defeito que
a terceira leva do Bloco 3c registrou. Derivando os fatos da referencia, as duas
implementacoes nao "batem por sorte": elas batem por construcao, e o
teste-r1.php prova isso frase a frase.

O QUE O PHP AINDA FAZ, e por que ele nao recebe a frase pronta: as frases da
referencia sao ASCII, como todo o banco desta ilha. Texto de tela sai ACENTUADO
(fase 4b do playbook), entao quem escreve a frase que o visitante le e o PHP,
com as mesmas pecas de informacao e o mesmo molde. O teste compara as duas
ignorando acento — se o molde divergir, ele reprova.
"""

import importlib.util
import json
import os
import sys
import unicodedata

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = os.path.join(BASE, "dados")


def _carregar_referencia():
    """Importa ferramentas/cobertura-r1.py como modulo (o hifen impede o import
    normal). A referencia e uma so: se ela mudar, este gerador muda junto."""
    caminho = os.path.join(BASE, "ferramentas", "cobertura-r1.py")
    spec = importlib.util.spec_from_file_location("cobertura_r1", caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


ref = _carregar_referencia()


def sem_acento(txt):
    return "".join(
        c for c in unicodedata.normalize("NFD", txt)
        if unicodedata.category(c) != "Mn"
    )


# Como cada origem do banco e NOMEADA na tela, e a ressalva que a escada de
# fontes obriga para ela (a mesma escada da pagina de metodologia). O banco
# guarda um apelido de campo ('fabricante-via-busca'); a tela precisa de uma
# frase em portugues, e a ressalva nao e enfeite: e o degrau da escada dito com
# todas as letras, no lugar onde o leitor decide se compra.
#
# Fica AQUI, e viaja dentro do arquivo de dados, por dois motivos. Primeiro,
# para o snippet nao carregar prosa propria sobre procedencia — se um dia a
# escada mudar, muda num lugar so. Segundo, para ferramentas/teste-r1.php poder
# aplicar a mesma troca sobre a frase da referencia antes de comparar: sem uma
# tabela declarada, a comparacao entre o PHP e a referencia viraria "parece
# igual", que nao e medicao.
ROTULOS_DE_ORIGEM = {
    "manual-fabricante": {
        "rotulo": "manual do fabricante",
        "ressalva": None,
        "nivel": 2,
    },
    "fabricante-via-busca": {
        "rotulo": "página do fabricante",
        "ressalva": "a confirmar no manual",
        "nivel": 3,
    },
    "varejo-oficial-da-marca": {
        "rotulo": "loja oficial da marca",
        "ressalva": "confira a embalagem",
        "nivel": 4,
    },
}


# --------------------------------------------------------------- OS FATOS
def fato_do_item(item, modelo_id):
    """Um item de resposta, reduzido ao que a tela precisa — e nada alem.

    Nada de prosa aqui: publicador, codigo, conjunto declarado, endereco e data
    sao FATOS do banco; a frase e do PHP. O que entra e o que a pagina mostra
    ou o que ela precisa para decidir o que mostrar.
    """
    peca = next(p for p in ref.pecas if p["id"] == item["peca"])
    par = ref.pares_do_modelo(peca, modelo_id)[0]
    fonte = peca["fontes"][par["fonte"]]

    # Origem sem rotulo declarado faria a tela imprimir o apelido de campo cru
    # ('fabricante-via-busca') no meio de uma frase publicada — em silencio, que
    # e como este tipo de defeito costuma chegar ao ar. Melhor parar aqui.
    if fonte.get("origem") not in ROTULOS_DE_ORIGEM:
        sys.stderr.write(
            "ERRO: a peca %r cita a origem %r, que nao tem rotulo de tela em "
            "ROTULOS_DE_ORIGEM. Declare o rotulo e a ressalva da escada de fontes "
            "antes de publicar.\n" % (peca["id"], fonte.get("origem"))
        )
        sys.exit(1)

    declarados = [c.get("codigo_declarado") for c in peca.get("compatibilidade", [])
                  if c.get("codigo_declarado")]

    vida = peca.get("vida_util_declarada") or {}
    imagem = peca.get("imagem") or {}

    return {
        "tipo": item["tipo_respondido"],
        "peca": peca["id"],
        "codigo": peca.get("codigo_fabricante"),
        "nome_na_fonte": peca["nome_na_fonte"],
        "tipo_da_peca": peca["tipo"],
        "dentro_de_kit": peca["tipo"] == "kit",
        # Ver frase_declarada() na referencia: "a marca nao vende o filtro
        # avulso" e uma afirmacao sobre o catalogo inteiro do modelo, e so vale
        # quando nenhuma peca avulsa daquele tipo responde por ele.
        "existe_avulso": bool(item.get("existe_avulso")),
        "publicador": fonte.get("publicador") or ref.marcas[peca["marca"]]["nome"],
        "origem": fonte.get("origem"),
        "nivel_da_fonte": fonte.get("nivel"),
        "url": fonte.get("url"),
        "verificado_em": fonte.get("verificado_em"),
        "declarados": declarados,
        "divergencia": bool(peca.get("divergencias")),
        "variante_do_par": par.get("variante_de_hardware"),
        "vida_util": (
            {"valor": vida.get("valor"), "unidade": vida.get("unidade")}
            if vida.get("valor") is not None else None
        ),
        "tem_imagem": bool(imagem.get("url")),
        "esperando_link": not (peca.get("afiliado", {}) or {}).get("url"),
        # O BLOCO DE COMPRA VIAJA COMO FATO, e nao como decisao do PHP (secao 7
        # do ARQUIPELAGO.md, cicatriz de 10/09/2026). Enquanto a url for vazia,
        # a pagina RESERVA o lugar em vez de esconder o bloco: esconder faria a
        # unica porta de compra voltar a ser o link de procedencia, que e o
        # defeito que o despacho manda corrigir.
        "afiliado": afiliado_do(peca),
    }


def afiliado_do(peca):
    """A oferta de uma peca, na forma que a tela precisa.

    `programa` sai junto porque o rotulo do botao nomeia a loja para quem clica
    ("Ver na Shopee") — link de compra que nao diz para onde leva e pedido de
    confianca, nao oferta. Sem url, os dois campos saem vazios e a tela escreve
    "link de loja em breve".
    """
    a = peca.get("afiliado") or {}
    return {
        "url": a.get("url") or "",
        "programa": a.get("plataforma") or None,
        "sub_id_1": a.get("sub_id_1") or "robometria",
        "sub_id_2": a.get("sub_id_2") or "R1",
    }


def fato_do_kit_fechado(kit, modelo_id):
    peca = next(p for p in ref.pecas if p["id"] == kit["peca"])
    par = ref.pares_do_modelo(peca, modelo_id)[0]
    fonte = peca["fontes"][par["fonte"]]
    return {
        "peca": peca["id"],
        "codigo": peca.get("codigo_fabricante"),
        "nome_na_fonte": peca["nome_na_fonte"],
        "publicador": fonte.get("publicador") or ref.marcas[peca["marca"]]["nome"],
        "origem": fonte.get("origem"),
        "url": fonte.get("url"),
        "verificado_em": fonte.get("verificado_em"),
        "esperando_link": not (peca.get("afiliado", {}) or {}).get("url"),
        "afiliado": afiliado_do(peca),
    }


def exemplos_estruturados(varredura, tipos_ofertados):
    """A tabela da secao 1.7, em CAMPOS em vez de texto pronto.

    A ordem e a da referencia — ref.ordem_dos_exemplos(), a MESMA que gera o
    markdown de dados/tabela-exemplos-r1.md. O que muda aqui e so a forma: a
    referencia entrega a linha ja escrita ("varejo-oficial-da-marca · 09/09/2026"),
    e a tela precisa dos campos separados para nomear a origem em portugues,
    marcar a ressalva da escada de fontes e ligar cada linha ao endereco da
    declaracao. Uma ordem so no projeto; duas tabelas divergiriam em silencio.
    """
    linhas = []
    for l, item in ref.ordem_dos_exemplos(varredura):
        if item["tipo_respondido"] not in tipos_ofertados:
            continue
        fato = fato_do_item(item, l["modelo"])
        linhas.append({
            "modelo": l["modelo"],
            "modelo_rotulo": "%s %s" % (ref.marcas[l["marca"]]["nome"],
                                        l["codigo_fabricante"]),
            "tipo": fato["tipo"],
            "peca": fato["peca"],
            "codigo": fato["codigo"],
            "nome_na_fonte": fato["nome_na_fonte"],
            "dentro_de_kit": fato["dentro_de_kit"],
            "divergencia": fato["divergencia"],
            "origem": fato["origem"],
            "url": fato["url"],
            "verificado_em": fato["verificado_em"],
        })
    return linhas


def divergencias_publicaveis(ids_de_peca):
    """As duas declaracoes que discordam, com as duas datas (secao 1.4).

    Vao inteiras para a tela: a regra do conjunto mais estreito so e verificavel
    pelo leitor se ele puder ver o que foi descartado e por quem foi publicado.
    """
    saida = {}
    for pid in sorted(ids_de_peca):
        peca = next(p for p in ref.pecas if p["id"] == pid)
        if not peca.get("divergencias"):
            continue
        saida[pid] = [
            {
                "canal": d.get("canal"),
                "conjunto": d.get("conjunto_declarado") or [],
                "titulo_na_fonte": d.get("titulo_na_fonte"),
                "url": d.get("url"),
                "verificado_em": d.get("verificado_em"),
            }
            for d in peca["divergencias"]
        ]
    return saida


def montar():
    varredura = ref.varrer()
    publicaveis = varredura["publicaveis"]

    # O seletor e GERADO da varredura, nunca digitado: tipo sem nenhuma peca
    # declarada no banco inteiro fica de fora, porque oferecer uma escolha que
    # sempre devolve recusa contraria a promessa antes do formulario (secao 6 do
    # ARQUIPELAGO.md). O mesmo corte vale para a lista de recusas de uma
    # consulta "todas as pecas": repetir em 28 modelos que nao ha reservatorio
    # nenhum e ruido, e a pagina diz isso UMA vez, no lugar certo.
    tipos_ofertados = [
        t for t in ref.TIPOS_CONSULTAVEIS
        if varredura["por_tipo"][t][ref.DECLARADA] > 0
    ]
    tipos_zerados = [t for t in ref.TIPOS_CONSULTAVEIS if t not in tipos_ofertados]

    respostas = {}
    referencia = {}
    pecas_citadas = set()

    for m in publicaveis:
        r = ref.responder_r1(m["id"])

        fabricante = [fato_do_item(i, m["id"]) for i in r["declarada_fabricante"]
                      if i["tipo_respondido"] in tipos_ofertados]
        terceiro = [fato_do_item(i, m["id"]) for i in r["declarada_terceiro"]
                    if i["tipo_respondido"] in tipos_ofertados]
        kits = [fato_do_kit_fechado(k, m["id"])
                for k in r["kits_de_composicao_nao_transcrita"]]

        for i in fabricante + terceiro:
            pecas_citadas.add(i["peca"])

        variantes = m.get("variantes_de_hardware") or []
        aviso = None
        if len(variantes) >= 2:
            aviso = {
                "rotulos": [str(v.get("rotulo")) for v in variantes],
                "o_que_muda": [str(v.get("o_que_muda")) for v in variantes
                               if v.get("o_que_muda")],
            }

        respostas[m["id"]] = {
            "aviso_de_variante": aviso,
            "fabricante": fabricante,
            "terceiro": terceiro,
            "kits_sem_composicao": kits,
        }

        # O gabarito: a frase da referencia, ASCII, do jeito que ela sai. O
        # teste compara com a do PHP ignorando acento.
        referencia[m["id"]] = {
            "aviso_de_variante": r["aviso_de_variante"],
            "fabricante": [
                {"tipo": i["tipo_respondido"], "peca": i["peca"], "frase": i["frase"]}
                for i in r["declarada_fabricante"]
                if i["tipo_respondido"] in tipos_ofertados
            ],
            "terceiro": [
                {"tipo": i["tipo_respondido"], "peca": i["peca"], "frase": i["frase"]}
                for i in r["declarada_terceiro"]
                if i["tipo_respondido"] in tipos_ofertados
            ],
            "kits_sem_composicao": [
                {"peca": k["peca"], "frase": k["frase"]}
                for k in r["kits_de_composicao_nao_transcrita"]
            ],
            "recusa_por_tipo": {
                t: ref.frase_de_recusa(t) for t in tipos_ofertados
            },
        }

    modelos = [
        {
            "id": m["id"],
            "marca": m["marca"],
            "codigo": m["codigo_fabricante"],
            "linha": m.get("linha"),
            "responde": bool(respostas[m["id"]]["fabricante"]),
            "so_kit": (not respostas[m["id"]]["fabricante"]
                       and bool(respostas[m["id"]]["kits_sem_composicao"])),
        }
        for m in publicaveis
    ]

    # O MODELO-ANCORA: o que a pagina responde quando ninguem escolheu nada.
    #
    # Ele existe porque uma ferramenta que so calcula depois do clique mostra a
    # um modelo de linguagem um formulario vazio (secao 5 do ARQUIPELAGO.md), e
    # a tabela de exemplos sozinha e uma lista — nao uma resposta escrita. A
    # ancora e a resposta inteira, com frase, procedencia e vitrine, servida em
    # HTML antes de qualquer interacao.
    #
    # A escolha e por REGRA, nunca a dedo: mais tipos de peca cobertos, depois
    # mais itens, depois ordem alfabetica. Duas consequencias que importam.
    # Primeiro, a ancora acompanha o banco — quando a coleta melhorar outro
    # modelo, a ancora muda sozinha, sem ninguem lembrar de trocar. Segundo, a
    # regra impede sozinha o erro que a varredura da terceira leva do 3c
    # registrou: o PRA500 e a consulta-alvo escrita na especificacao e a R1 sai
    # VAZIA nele, entao estrear a ferramenta com ele seria estrear com um "nao
    # sabemos".
    ancora = None
    if modelos:
        ancora = sorted(
            [m["id"] for m in modelos if respostas[m["id"]]["fabricante"]],
            key=lambda mid: (
                -len({i["tipo"] for i in respostas[mid]["fabricante"]}),
                -len(respostas[mid]["fabricante"]),
                mid,
            ),
        )[0]

    marcas_usadas = sorted({m["marca"] for m in modelos})

    # QUANTAS PECAS ESPERAM LINK DE LOJA — contadas por PECA, nunca por item de
    # resposta. A mesma peca responde por varios modelos, e somar itens daria um
    # numero maior que o banco inteiro ("45 esperando link" com 16 pecas), o que
    # a pagina publicaria como se fosse tamanho de catalogo. Este numero e
    # trabalho pendente de verdade (secao 7 do contrato) e a pagina o diz em voz
    # alta, em vez de deixar cada cartao sussurrar a falta.
    pecas_citadas_na_tela = {
        i["peca"]
        for x in respostas.values()
        for i in x["fabricante"]
    }
    pecas_sem_link = {
        pid for pid in pecas_citadas_na_tela
        if not (next(p for p in ref.pecas if p["id"] == pid).get("afiliado") or {}).get("url")
    }

    resumo = {
        "modelos_publicaveis": len(publicaveis),
        "modelos_que_respondem": sum(1 for m in modelos if m["responde"]),
        "modelos_com_entrada_vazia": len(varredura["entrada_vazia"]),
        "celulas": sum(varredura["celulas"].values()),
        "celulas_sem_resposta": varredura["celulas"][ref.VAZIA],
        "pares_declarados": ref.doc_pecas["contagem"].get("pares_peca_x_modelo_declarados"),
        "pecas_publicaveis": sum(1 for p in ref.pecas if p["status"] == "publicavel"),
        "marcas": len(marcas_usadas),
        "as_duas_ferramentas": len(varredura["cruzamento"]["as_duas_respondem"]),
        "pecas_recomendadas": len(pecas_citadas_na_tela),
        "pecas_esperando_link": len(pecas_sem_link),
        "pecas_com_link": len(pecas_citadas_na_tela) - len(pecas_sem_link),
    }

    return {
        "id": "r1-respostas",
        "ilha": "robometria",
        "entidade": "medicao",
        "gerado_por": "ferramentas/gerar-r1.py",
        "banco_gerado_em": ref.doc_pecas["gerado_em"],
        "o_que_e": (
            "Combustivel da ferramenta R1 no site: para cada modelo publicavel, "
            "os FATOS de cada peca que o fabricante declarou compativel — codigo, "
            "publicador, conjunto declarado, endereco e data. Sem prosa: a frase "
            "que o visitante le e montada pelo snippet, em portugues acentuado, e "
            "conferida contra a implementacao de referencia por "
            "ferramentas/teste-r1.php."
        ),
        "marcas": [{"id": b, "nome": ref.marcas[b]["nome"]} for b in marcas_usadas],
        "rotulos_de_origem": ROTULOS_DE_ORIGEM,
        "ancora": ancora,
        "tipos": tipos_ofertados,
        "tipos_sem_nenhuma_peca_no_banco": tipos_zerados,
        "modelos": modelos,
        "respostas": respostas,
        "divergencias": divergencias_publicaveis(pecas_citadas),
        "exemplos": exemplos_estruturados(varredura, tipos_ofertados),
        "entrada_vazia": varredura["entrada_vazia"],
        "resumo": resumo,
    }, {
        "id": "r1-referencia",
        "ilha": "robometria",
        "entidade": "medicao",
        "gerado_por": "ferramentas/gerar-r1.py",
        "o_que_e": (
            "GABARITO da R1: a resposta de cada modelo ja em frase, escrita pela "
            "implementacao de referencia ferramentas/cobertura-r1.py. Nao vai para "
            "o site (publicar=false). Existe para ferramentas/teste-r1.php provar, "
            "frase a frase e ignorando acento, que o PHP do snippet diz a MESMA "
            "coisa que a referencia — que e o que a especificacao exige."
        ),
        "respostas": referencia,
    }


def main():
    fatos, gabarito = montar()
    r = fatos["resumo"]

    print("Robometria — combustivel da R1 gerado da implementacao de referencia")
    print("")
    print("  modelos publicaveis ............. %d" % r["modelos_publicaveis"])
    print("  respondem alguma peca ........... %d" % r["modelos_que_respondem"])
    print("  entrada vazia ................... %d" % r["modelos_com_entrada_vazia"])
    print("  tipos no seletor ................ %s" % ", ".join(fatos["tipos"]))
    if fatos["tipos_sem_nenhuma_peca_no_banco"]:
        print("  fora do seletor (zero pecas) .... %s"
              % ", ".join(fatos["tipos_sem_nenhuma_peca_no_banco"]))
    print("  modelo-ancora ................... %s" % fatos["ancora"])
    print("  linhas da tabela de exemplos .... %d" % len(fatos["exemplos"]))
    print("  pecas com divergencia registrada  %d" % len(fatos["divergencias"]))
    print("")

    itens = sum(len(x["fabricante"]) + len(x["terceiro"])
                for x in fatos["respostas"].values())
    print("  itens de resposta ............... %d" % itens)
    esperando = sum(
        1 for x in fatos["respostas"].values()
        for i in x["fabricante"] + x["terceiro"] if i["esperando_link"]
    )
    print("  destes, esperando link de loja .. %d" % esperando)
    print("  pecas recomendadas na tela ...... %d" % r["pecas_recomendadas"])
    print("  destas, esperando link de loja .. %d  <- trabalho pendente (secao 7)"
          % r["pecas_esperando_link"])
    print("")

    if "--gravar" not in sys.argv:
        print("  (rode com --gravar para escrever dados/r1-respostas.json e "
              "dados/r1-referencia.json)")
        return 0

    for nome, doc in (("r1-respostas.json", fatos), ("r1-referencia.json", gabarito)):
        with open(os.path.join(DADOS, nome), "w", encoding="utf-8") as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        tamanho = os.path.getsize(os.path.join(DADOS, nome))
        print("  gravado: dados/%s (%d bytes)" % (nome, tamanho))

    return 0


if __name__ == "__main__":
    sys.exit(main())
