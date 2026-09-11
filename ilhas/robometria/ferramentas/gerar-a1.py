#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o combustivel do artigo-ancora A1 a partir do BANCO commitado.

    python3 ferramentas/gerar-a1.py            # relatorio na tela
    python3 ferramentas/gerar-a1.py --gravar   # grava o arquivo abaixo

Grava:
  dados/a1-fatos.json   FATOS, sem prosa. O Sync o leva para a option
                        robometria_dados_a1-fatos e o snippet
                        robometria-a1.php escreve as frases a partir dele.
                        publicar=true no manifest.

POR QUE O ARTIGO TEM GERADOR, e nao e so texto escrito a mao.

O artigo-ancora da R1 afirma uma coisa que da para MEDIR: peca universal de robo
aspirador nao existe. A secao 9 do ARQUIPELAGO.md exige de toda pagina "pelo
menos 3 itens de banco reais e um numero calculado proprio" — e um artigo cuja
tese e um numero nao pode ter esse numero digitado dentro do HTML, porque no dia
em que o banco crescer o texto passa a mentir em silencio. Entao a tese e
derivada aqui, do mesmo banco que alimenta a R1, e o snippet so escreve a frase.

E O QUE ELE MEDE, com as tres afirmacoes separadas de proposito:

  1. ALCANCE. Quantos codigos de modelo cada peca publicavel tem declarados pelo
     fabricante. O maior alcance do banco e o teto do que "universal" poderia
     significar aqui — e ele e pequeno.
  2. TRAVESSIA DE MARCA. Quantas pecas sao declaradas para modelos de mais de
     uma MARCA. Esta e a afirmacao que mata "universal" de frente.
  3. DISPERSAO DENTRO DA MARCA. Quantos conjuntos DISTINTOS de modelos as pecas
     de uma mesma marca formam. E o achado menos obvio e o mais util para quem
     esta comprando: compatibilidade nao se herda nem dentro do proprio
     catalogo, entao o modelo estar na lista do filtro nao o coloca na lista da
     escova.

O QUE ELE NAO FAZ: nao coleta nada e nao chama rede. Todo numero daqui sai de
dados/pecas.json, dados/modelos-robo.json e dados/marcas.json, e a varredura por
tipo vem da mesma implementacao de referencia que a R1 usa
(ferramentas/cobertura-r1.py), para as duas paginas nunca publicarem contagens
diferentes da mesma coisa.
"""

import importlib.util
import json
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = os.path.join(BASE, "dados")


def _carregar_referencia():
    """Importa ferramentas/cobertura-r1.py como modulo (o hifen impede o import
    normal). A referencia e uma so, e o artigo nao ganha uma copia dela."""
    caminho = os.path.join(BASE, "ferramentas", "cobertura-r1.py")
    spec = importlib.util.spec_from_file_location("cobertura_r1", caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


ref = _carregar_referencia()


# Nome legivel de cada tipo, no singular, como a frase publicada o escreve. O
# banco e ASCII; o acento entra no PHP (fase 4b do playbook), entao aqui fica a
# forma sem acento e o snippet tem a mesma tabela acentuada. teste-a1.php compara
# as duas ignorando acento.
NOME_DO_TIPO = {
    "filtro": "filtro",
    "escova lateral": "escova lateral",
    "escova principal": "escova principal",
    "mop": "mop",
    "bateria": "bateria",
    "reservatorio": "reservatorio",
    "kit": "kit",
}


def composicao_transcrita(peca):
    """O kit tem a composicao transcrita, ou so o titulo?

    Kit sem composicao transcrita NAO entra na vitrine do artigo, e a razao esta
    na secao 7 do ARQUIPELAGO.md: oferecer a compra de um produto sobre o qual a
    propria pagina diz nao saber o que vem dentro e recomendar em primeiro lugar
    um item que a pagina nao sustenta. O kit volta para a vitrine no dia em que a
    coleta transcrever o que ha nele — e essa e a mesma pendencia que o PROMPT.md
    ja registra para a proxima leva do 3c.
    """
    if peca["tipo"] != "kit":
        return True
    return any(i.get("tipo") for i in peca.get("composicao", []))


def tipos_do_kit(peca):
    return sorted({i["tipo"] for i in peca.get("composicao", []) if i.get("tipo")})


def publicaveis_de(registros):
    return [r for r in registros if r.get("status") == "publicavel"]


def alcance_das_pecas():
    """Quantos codigos de modelo cada peca publicavel tem declarados.

    Dois numeros, e a diferenca entre eles importa: `codigos_declarados` e o que
    o FABRICANTE escreveu (e a afirmacao dele, e e ela que a frase cita);
    `modelos_publicaveis` e quantos desses modelos o banco desta ilha publica. O
    segundo e menor quando um codigo aparece so na lista de uma peca, sem pagina
    de produto propria — e publicar um pelo outro daria ao leitor um numero que
    nao e o da fonte.
    """
    marcas_dos_modelos = {m["id"]: m["marca"] for m in ref.modelos.values()}
    publicavel = {m["id"] for m in publicaveis_de(ref.doc_modelos["registros"])}

    linhas = []
    for p in publicaveis_de(ref.pecas):
        pares = p.get("compatibilidade", [])
        modelos = [c["modelo"] for c in pares]
        marcas_atendidas = sorted({marcas_dos_modelos.get(m, "?") for m in modelos})
        identificacao, sem_codigo = ref.identificar_peca(p)
        linhas.append({
            "peca": p["id"],
            "tipo": p["tipo"],
            "marca": p["marca"],
            "publicador": ref.marcas[p["marca"]]["nome"],
            "identificacao": identificacao,
            "sem_codigo_publicado": sem_codigo,
            "nome_na_fonte": p["nome_na_fonte"],
            "codigos_declarados": len(modelos),
            "codigos_na_fonte": [c.get("codigo_declarado") or c["modelo"] for c in pares],
            "modelos_publicaveis": len([m for m in modelos if m in publicavel]),
            "marcas_atendidas": marcas_atendidas,
            "atravessa_marca": len(marcas_atendidas) > 1,
        })

    # Ordem: maior alcance primeiro, e desempate alfabetico para o arquivo nao
    # mudar de ordem entre duas execucoes sem o banco ter mudado.
    linhas.sort(key=lambda l: (-l["codigos_declarados"], l["peca"]))
    return linhas


def dispersao_por_marca(alcance):
    """Quantos conjuntos DISTINTOS de modelos as pecas de uma marca formam.

    Se compatibilidade se herdasse do modelo para a classe de peca, as pecas de
    uma marca tenderiam a repetir o mesmo conjunto de modelos, e este numero
    seria muito menor que o de pecas. Quando ele e IGUAL ao numero de pecas,
    nenhuma peca da marca repete a lista de outra — que e o caso mais duro e o
    que o leitor precisa saber antes de comprar por semelhanca.
    """
    por_marca = {}
    for p in publicaveis_de(ref.pecas):
        conjunto = frozenset(c["modelo"] for c in p.get("compatibilidade", []))
        b = por_marca.setdefault(p["marca"], {"pecas": 0, "conjuntos": set()})
        b["pecas"] += 1
        b["conjuntos"].add(conjunto)

    saida = []
    for marca, b in por_marca.items():
        saida.append({
            "marca": marca,
            "publicador": ref.marcas[marca]["nome"],
            "pecas": b["pecas"],
            "conjuntos_distintos": len(b["conjuntos"]),
            "nenhuma_repete": len(b["conjuntos"]) == b["pecas"] and b["pecas"] > 1,
        })
    saida.sort(key=lambda l: (-l["pecas"], l["marca"]))
    return saida


def cobertura_por_tipo(varredura):
    """Em quantos dos modelos publicaveis a R1 responde cada tipo de peca.

    Vem da varredura da propria R1, nao de uma contagem paralela: se um dia a
    regra do kit mudar, as duas paginas mudam juntas.
    """
    total = len(varredura["publicaveis"])
    saida = []
    for tipo in ref.TIPOS_CONSULTAVEIS:
        c = varredura["por_tipo"][tipo]
        saida.append({
            "tipo": tipo,
            "nome": NOME_DO_TIPO[tipo],
            "modelos_com_declaracao": c[ref.DECLARADA],
            "modelos_publicaveis": total,
        })
    saida.sort(key=lambda l: (-l["modelos_com_declaracao"], l["tipo"]))
    return saida


def vitrine(alcance, quantas=4):
    """Os itens de banco REAIS que o artigo mostra, com a porta de compra.

    Sao as pecas de maior alcance declarado — que e o criterio da propria tese do
    artigo, nao um recorte comercial: a peca que serve em mais modelos e a que
    mais gente que caiu na busca por "universal" esta procurando. A ordem e
    tecnica; ter ou nao link de loja NAO reordena nada (secao 7 do contrato).

    Todo item sai com o campo afiliado presente, mesmo vazio: o snippet reserva o
    lugar e escreve "link de loja em breve", que e o item 0 do despacho de 10/09
    virado regra da ilha.
    """
    por_id = {p["id"]: p for p in ref.pecas}
    itens = []
    for l in alcance:
        if len(itens) >= quantas:
            break
        p = por_id[l["peca"]]
        if not composicao_transcrita(p):
            continue
        fonte = next(iter(p.get("fontes", {}).values()), {})
        itens.append({
            "peca": p["id"],
            "tipo": p["tipo"],
            "nome_do_tipo": NOME_DO_TIPO.get(p["tipo"], p["tipo"]),
            "publicador": ref.marcas[p["marca"]]["nome"],
            "identificacao": l["identificacao"],
            "sem_codigo_publicado": l["sem_codigo_publicado"],
            "nome_na_fonte": p["nome_na_fonte"],
            # A ESPECIFICACAO QUE FEZ O ITEM ENTRAR (secao 6): aqui ela e o
            # alcance declarado, porque e sobre alcance que o artigo fala.
            "codigos_na_fonte": l["codigos_na_fonte"],
            "codigos_declarados": l["codigos_declarados"],
            "tipos_do_kit": tipos_do_kit(p),
            "imagem": p.get("imagem", {}),
            "afiliado": p.get("afiliado", {"url": ""}),
            "fonte_url": fonte.get("url"),
            "fonte_publicador": fonte.get("publicador"),
            "verificado_em": p.get("verificado_em"),
        })
    return itens


def perguntas(fatos):
    """As perguntas do FAQPage, montadas dos FATOS — nunca escritas a mao.

    Cada uma e uma formulacao real do corpus (dados/corpus-buscas.md, cluster
    A1), e cada resposta e uma frase que a propria pagina serve. Pergunta em
    JSON-LD que a pagina nao responde e marcacao que promete o que nao entrega.

    O TEXTO DAQUI SAI ACENTUADO, e isso foi corrigido em 10/09/2026, no bloco 4.
    A primeira versao escreveu as respostas em ASCII, como o resto deste arquivo,
    e elas vao INTEIRAS para o FAQPage do snippet — entao o site publicou "Nao.
    Nas 16 pecas de reposicao..." dentro do JSON-LD. O banco desta ilha e ASCII
    porque ele CITA fontes; o que a ilha ESCREVE sai em portugues de verdade
    (fase 4b do playbook), e o canal em que o defeito apareceu e justamente o que
    a secao 5 do ARQUIPELAGO.md diz valer tanto quanto ranquear. Achado ao
    escrever o A2, que nasceu ja com a trava que mede isso (teste-a2.php).
    """
    r = fatos["resumo"]
    maior = fatos["maior_alcance"]
    lista = []

    # A resposta e DERIVADA da contagem, nao digitada: e a mesma frase que a
    # pagina serve, e ela precisa mudar junto com o banco. Marcacao que afirma o
    # que a pagina deixou de afirmar e pior do que marcacao nenhuma, porque e
    # justamente ela que um modelo de linguagem le como resposta (secao 5).
    if r["pecas_que_atravessam_marca"] == 0:
        resposta_universal = (
            "Não. Nas %d peças de reposição com compatibilidade declarada pelo "
            "fabricante que a Robometria conferiu, nenhuma é declarada para "
            "modelos de mais de uma marca, e a lista mais longa do banco nomeia "
            "%d códigos de modelo, todos da mesma marca."
            % (r["pecas_publicaveis"], maior["codigos_declarados"])
        )
    else:
        resposta_universal = (
            "Quase não. Das %d peças de reposição com compatibilidade declarada "
            "pelo fabricante que a Robometria conferiu, apenas %d é declarada "
            "para modelos de mais de uma marca, e a lista mais longa do banco "
            "nomeia %d códigos de modelo."
            % (r["pecas_publicaveis"], r["pecas_que_atravessam_marca"],
               maior["codigos_declarados"])
        )
    lista.append({
        "pergunta": "Existe filtro universal para robô aspirador?",
        "resposta": resposta_universal,
    })
    lista.append({
        "pergunta": "Uma peça que serve num modelo da marca serve nos outros modelos dela?",
        "resposta": (
            "Nem sempre, e o próprio catálogo dos fabricantes mostra isso: as %d "
            "peças da %s no banco formam %d conjuntos de modelos diferentes. "
            "Compatibilidade é declarada por código de peça, uma a uma, e não se "
            "herda de uma peça para a seguinte."
            % (
                fatos["dispersao"][0]["pecas"],
                fatos["dispersao"][0]["publicador"],
                fatos["dispersao"][0]["conjuntos_distintos"],
            )
        ),
    })
    lista.append({
        "pergunta": "Como descobrir o código da peça certa para o meu robô aspirador?",
        "resposta": (
            "Procurando o modelo na lista de compatibilidade publicada pelo "
            "próprio fabricante. A Robometria reúne essas listas: são %d pares "
            "peça × modelo em %d marcas, todos declarados pelo fabricante e "
            "nenhum inferido, cada um com o endereço da declaração e a data em "
            "que ela foi verificada."
            % (r["pares_declarados"], r["marcas"])
        ),
    })
    return lista


def montar():
    varredura = ref.varrer()
    alcance = alcance_das_pecas()
    dispersao = dispersao_por_marca(alcance)

    pares = sum(l["codigos_declarados"] for l in alcance)
    # So PECAS, e o nome do campo diz isso. ferramentas/validar-banco.py conta 44
    # "esperando link" somando modelos e pecas; publicar os dois numeros com o
    # mesmo rotulo em paginas diferentes seria a ilha se contradizendo sozinha.
    esperando = len([
        p for p in publicaveis_de(ref.pecas)
        if not (p.get("afiliado", {}) or {}).get("url")
    ])

    fatos = {
        "id": "a1-fatos",
        "ilha": "robometria",
        "artigo": "A1",
        "gerado_em": ref.doc_pecas["gerado_em"],
        "nota": (
            "Fatos do artigo-ancora A1, derivados do banco commitado por "
            "ferramentas/gerar-a1.py. Nenhum numero aqui e digitado: se o banco "
            "crescer e a tese do artigo deixar de valer, e este arquivo que "
            "muda, e ferramentas/teste-a1.php reprova a pagina antes de ela ir "
            "ao ar dizendo o que o banco nao sustenta."
        ),
        "resumo": {
            "marcas": len(ref.marcas),
            "modelos_publicaveis": len(varredura["publicaveis"]),
            "pecas_publicaveis": len(publicaveis_de(ref.pecas)),
            "pares_declarados": pares,
            "pecas_que_atravessam_marca": len([l for l in alcance if l["atravessa_marca"]]),
            "celulas_total": sum(varredura["celulas"].values()),
            "celulas_sem_resposta": varredura["celulas"][ref.VAZIA],
            "pecas_esperando_link": esperando,
        },
        "maior_alcance": alcance[0],
        "alcance": alcance,
        "dispersao": dispersao,
        "cobertura_por_tipo": cobertura_por_tipo(varredura),
        "vitrine": vitrine(alcance),
    }
    fatos["perguntas"] = perguntas(fatos)
    return fatos


def relatorio(f):
    r = f["resumo"]
    print("Robometria — fatos do artigo-ancora A1 (gerados do banco commitado)\n")
    print("  marcas ....................... %d" % r["marcas"])
    print("  modelos publicaveis .......... %d" % r["modelos_publicaveis"])
    print("  pecas publicaveis ............ %d" % r["pecas_publicaveis"])
    print("  pares peca x modelo .......... %d" % r["pares_declarados"])
    print("  pecas que ATRAVESSAM marca ... %d" % r["pecas_que_atravessam_marca"])
    print("  PECAS esperando link de afiliado  %d" % r["pecas_esperando_link"])

    m = f["maior_alcance"]
    print("\n  Maior alcance declarado do banco: %s (%s da %s), %d codigos de modelo"
          % (m["identificacao"], m["tipo"], m["publicador"], m["codigos_declarados"]))
    print("    codigos: %s" % ", ".join(m["codigos_na_fonte"]))

    print("\n  Dispersao dentro da marca (pecas -> conjuntos distintos de modelos):")
    for d in f["dispersao"]:
        marca = "%s (%s)" % (d["publicador"], d["marca"])
        print("    %-34s %2d peca(s) -> %d conjunto(s)%s"
              % (marca, d["pecas"], d["conjuntos_distintos"],
                 "   NENHUMA repete a lista de outra" if d["nenhuma_repete"] else ""))

    print("\n  Cobertura por tipo de peca (modelos com declaracao / %d):"
          % r["modelos_publicaveis"])
    for c in f["cobertura_por_tipo"]:
        print("    %-18s %2d" % (c["nome"], c["modelos_com_declaracao"]))

    print("\n  Vitrine do artigo (%d itens, ordem por alcance declarado):" % len(f["vitrine"]))
    for v in f["vitrine"]:
        loja = v["afiliado"].get("url") or "(sem link — reserva o lugar)"
        print("    %-14s %-16s %d codigos   %s"
              % (v["identificacao"], v["tipo"], v["codigos_declarados"], loja))

    if r["pecas_que_atravessam_marca"] == 0:
        print("\n  A TESE DO ARTIGO SE SUSTENTA: nenhuma peca do banco e declarada "
              "para modelos de mais de uma marca.")
    else:
        print("\n  ATENCAO: %d peca(s) atravessam marca. A tese do artigo mudou de "
              "forma e o texto precisa ser reescrito antes de ir ao ar."
              % r["pecas_que_atravessam_marca"])


def main():
    f = montar()
    relatorio(f)
    if "--gravar" in sys.argv:
        caminho = os.path.join(DADOS, "a1-fatos.json")
        with open(caminho, "w", encoding="utf-8") as fh:
            json.dump(f, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        print("\n  gravado: dados/a1-fatos.json")
    else:
        print("\n  (rode com --gravar para escrever dados/a1-fatos.json)")


if __name__ == "__main__":
    main()
