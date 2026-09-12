#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o combustivel da R2 em PHP a partir da implementacao de REFERENCIA.

    python3 ferramentas/gerar-r2.py            # relatorio na tela
    python3 ferramentas/gerar-r2.py --gravar   # grava os dois arquivos abaixo

Grava:
  dados/r2-respostas.json   FATOS, sem prosa. E o que o site consome: o Sync o
                            leva para a option robometria_dados_r2-respostas e o
                            snippet robometria-r2.php monta as frases a partir
                            dele. publicar=true no manifest.
  dados/r2-referencia.json  GABARITO: a GRADE de respostas ja em frase, escrita
                            pela implementacao de referencia
                            (ferramentas/cobertura-r2.py). publicar=false — nao
                            vai para o site; existe para ferramentas/teste-r2.php
                            comparar, caso a caso, o que o PHP escreve com o que
                            a referencia escreve.

POR QUE A PROVA DA R2 TEM FORMA DIFERENTE DA PROVA DA R1.

A entrada da R1 e uma lista fechada de 28 modelos, entao o gerador consegue
pre-calcular TODA resposta possivel e o snippet vira um escritor de frases. A
entrada da R2 tem uma metragem continua de 10 a 400 m2: pre-calcular tudo seria
um arquivo enorme e, pior, mentiria sobre o que o snippet faz — porque ele
PRECISA fazer a aritmetica dos ciclos.

Entao a decisao 2 do desenho desta ilha ("a regra mora na referencia e o PHP nao
a reescreve") vale aqui assim: o que e REGRA — qual fonte se aplica a qual
situacao, qual limiar vale, quem passa na elegibilidade, em que ordem — sai
inteiro da referencia e viaja como fato. O que e ARITMETICA declarada — ceil da
divisao, soma de minutos — o PHP faz, e a prova de que faz igual e uma GRADE
que o teste percorre inteira: as 9 situacoes, e a metragem varrida de 10 em 10
m2 contra cada um dos modelos de referencia. Grade nao e amostra.

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

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = os.path.join(BASE, "dados")


def _carregar_referencia():
    """Importa ferramentas/cobertura-r2.py como modulo (o hifen impede o import
    normal). A referencia e uma so: se ela mudar, este gerador muda junto."""
    caminho = os.path.join(BASE, "ferramentas", "cobertura-r2.py")
    spec = importlib.util.spec_from_file_location("cobertura_r2", caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


ref = _carregar_referencia()


def chave(piso, pelo):
    """A chave de situacao que viaja para o PHP. Sem acento e sem espaco, porque
    ela e indice de array nos dois lados e id de elemento na tela."""
    return "%s|%s" % (piso.replace(" ", "-"), pelo)


def fato_do_modelo(m):
    """Um modelo do banco reduzido ao que a tela precisa — e nada alem.

    Nada de prosa: Pa, cobertura, autonomia, recarga, retomada, imagem e oferta
    sao FATOS do banco; a frase e do PHP.
    """
    imagem = m.get("imagem") or {}
    a = m.get("afiliado") or {}
    return {
        "id": m["id"],
        "marca": m["marca"],
        "rotulo": ref.rotulo_do_modelo(m),
        "codigo": m.get("codigo_fabricante"),
        "linha": m.get("linha"),
        "pa": ref.valor(m.get("pa_declarado")),
        "cobertura_m2": ref.valor(m.get("cobertura_m2_declarada")),
        "autonomia_min": ref.valor(m.get("autonomia_min_declarada")),
        "recarga_min": ref.valor(m.get("recarga_min_declarada")),
        "retoma_apos_recarga": ref.valor(m.get("retoma_apos_recarga")),
        "fonte": (m.get("pa_declarado") or {}).get("fonte")
                 if isinstance(m.get("pa_declarado"), dict) else None,
        # A PROCEDENCIA DO NUMERO QUE DECIDE viaja como fato, com o degrau da
        # escada ja resolvido em rotulo, ressalva e atribuicao. O snippet nao
        # sabe o que e uma escada de fontes: ele escreve a frase acentuada com
        # as pecas que chegam. Ver cobertura-r2.procedencia_do_pa().
        "procedencia": ref.procedencia_do_pa(m),
        "tem_imagem": bool(imagem.get("url")),
        "esperando_link": not a.get("url"),
        # A PORTA DE COMPRA VIAJA COMO FATO (secao 7 do ARQUIPELAGO.md, cicatriz
        # de 10/09/2026): enquanto a url for vazia a pagina RESERVA o lugar em vez
        # de esconder o bloco. Esconder faria a unica porta clicavel voltar a ser
        # o link de procedencia, que e exatamente o defeito.
        "afiliado": {
            "url": a.get("url") or "",
            "programa": a.get("plataforma") or None,
            # O CODIGO DA PAGINA DE ORIGEM E CARIMBADO POR QUEM MONTA A PAGINA, e o
            # banco nao opina. Ate 12/09/2026 este campo era LIDO do registro, e o
            # registro trazia um valor so: `sub_id_2: "R2"` nos 33 modelos e `"R1"` nas
            # 18 pecas. So que o campo nao e do produto — e da PAGINA que levou o
            # clique, e cada produto aparece em mais de uma. O A2 publicava os cinco
            # modelos da vitrine carimbados "R2", e o A1 as pecas dele carimbadas "R1":
            # no dia do primeiro link de afiliado, todo clique dos dois artigos seria
            # contado como das ferramentas, e a medicao diria que os artigos nao vendem
            # nada. Nao se conserta trocando o valor no banco, porque nenhum valor
            # unico e certo la: conserta-se cada gerador carimbando o proprio codigo.
            "sub_id_1": "robometria",
            "sub_id_2": "R2",
        },
    }


def fato_do_limiar(l):
    """Um limiar, com a procedencia inteira e o artigo do publicador.

    O artigo viaja junto pelo mesmo motivo que ROTULOS_DE_ORIGEM viaja na R1: se
    ele ficasse no snippet, publicador novo sairia na tela com o artigo errado, em
    silencio, no meio de uma frase que a pagina afirma.
    """
    return {
        "constante": l["constante"],
        "valor": l["valor"],
        "comparacao": l["comparacao"],
        "publicador": l["publicador"],
        "artigo": ref.ARTIGO_DO_PUBLICADOR[l["publicador"]],
        "fonte": l["fonte"],
        "url": l["url"],
        "verificado_em": l["verificado_em"],
        "palavras_da_fonte": l["palavras_da_fonte"],
    }


def montar():
    v = ref.varrer()

    m_ancora = ref.modelo_de_referencia_ancora()
    sit_ancora = ref.situacao_ancora()
    area_ancora = ref.area_ancora(m_ancora)

    if sit_ancora is None or m_ancora is None:
        sys.stderr.write(
            "ERRO: sem situacao-ancora ou sem modelo de referencia, a pagina "
            "nasceria como formulario vazio para um modelo de linguagem "
            "(secao 5 do ARQUIPELAGO.md).\n"
        )
        sys.exit(1)

    # ------------------------------------------------------------- SITUACOES
    situacoes = {}
    classificacao = {}
    referencia_situacoes = {}

    for piso in ref.PISOS:
        for pelo in ref.PELOS:
            sit = ref.situacao(piso, pelo)
            if sit is None:
                continue
            k = chave(piso, pelo)

            situacoes[k] = {
                "piso": piso,
                "pelo": pelo,
                "limiares": [fato_do_limiar(l) for l in sit["limiares"]],
                "limiar_seguro": fato_do_limiar(sit["limiar_seguro"]),
                "limiar_minimo": fato_do_limiar(sit["limiar_minimo"]),
                "ha_divergencia": sit["ha_divergencia"],
                "por_ponte": sit["por_ponte"],
                "faixa_confortavel": sit["faixa_confortavel"],
                "teto": fato_do_limiar(sit["teto"]) if sit["teto"] else None,
            }

            g = ref.classificar_modelos(sit)
            # A ORDEM E DA REFERENCIA, e o PHP nao reordena. Ordenar de novo na
            # tela seria a terceira camada da secao 7 do contrato escrita duas
            # vezes — e duas listas ordenadas por regras parecidas divergem em
            # silencio no dia em que uma das duas muda.
            classificacao[k] = {
                "elegiveis": [m["id"] for m in g["elegiveis"]],
                "no_limiar": [m["id"] for m in g["no_limiar"]],
                "nao_atendem": len(g["nao_atendem"]),
                "sem_pa_declarado": len(g["sem_pa_declarado"]),
            }

            r = ref.responder_r2(area_ancora, piso, pelo)
            referencia_situacoes[k] = {
                "frase": r["frase"],
                "frase_do_teto": r["frase_do_teto"],
                "frase_vazia": r["frase_vazia"],
                "no_limiar": [{"modelo": i["modelo"], "frase": i["frase"]}
                              for i in r["no_limiar"]],
            }

    # ------------------------------------------------- OS MODELOS QUE APARECEM
    citados = set()
    for k in classificacao:
        citados.update(classificacao[k]["elegiveis"])
        citados.update(classificacao[k]["no_limiar"])

    refs = ref.modelos_de_referencia()
    for m in refs:
        citados.add(m["id"])

    modelos = [fato_do_modelo(m) for m in ref.publicaveis() if m["id"] in citados]
    modelos.sort(key=lambda x: x["id"])

    # ------------------------------------------------------------- A GRADE
    #
    # Os cartoes dependem da metragem so quando o modelo declara cobertura por
    # carga (a ressalva de "passa da carga"). Hoje nenhum elegivel declara, entao
    # a frase do cartao nao varia com a area — mas a grade cobre tres metragens
    # de qualquer jeito, para o dia em que declarar. Prova que so mede o caso de
    # hoje deixa de medir exatamente quando o banco melhora.
    areas_de_cartao = sorted({ref.AREA_MINIMA, area_ancora, ref.AREA_MAXIMA})

    cartoes = {}
    for k, s in situacoes.items():
        for area in areas_de_cartao:
            r = ref.responder_r2(area, s["piso"], s["pelo"])
            cartoes["%s@%d" % (k, area)] = [
                {"modelo": i["modelo"], "ressalvas": i["ressalvas"], "frase": i["frase"]}
                for i in r["elegiveis"]
            ]

    # A metragem varrida de ponta a ponta contra cada modelo de referencia. E a
    # prova de que o ceil do PHP e o ceil da referencia — e a grade inclui os
    # MULTIPLOS EXATOS da cobertura e os vizinhos deles, porque foi so ali que a
    # quebra proposital de 10/09/2026 conseguiu separar ceil de floor+1.
    ciclos = {}
    for m in refs:
        for area in ref.areas_da_grade(m):
            t = ref.tempo(area, m)
            ciclos["%s@%d" % (m["id"], area)] = {
                "ciclos": t["ciclos"],
                "multiciclo_valido": t["multiciclo_valido"],
                "tempo_de_limpeza_min": t["tempo_de_limpeza_min"],
                "tempo_total_min": t["tempo_total_min"],
                "frase": ref.frase_do_ciclo(area, m, t),
            }

    # --------------------------------------------------- TABELA DE EXEMPLOS
    exemplos = []
    for area, piso, pelo in ref.ordem_dos_exemplos():
        r = ref.responder_r2(area, piso, pelo, m_ancora["id"])
        exemplos.append({
            "area": area,
            "situacao": chave(piso, pelo),
            "elegiveis": len(r["elegiveis"]),
            "ciclos": r["referencia"]["ciclos"] if r["referencia"] else None,
            "multiciclo_valido": r["referencia"]["multiciclo_valido"] if r["referencia"] else None,
            "tempo_de_limpeza_min": r["referencia"]["tempo_de_limpeza_min"] if r["referencia"] else None,
        })

    # --------------------------------------------------------------- CONTEXTO
    #
    # Os tres paragrafos derivados da pagina viajam como NUMERO, nunca como
    # prosa: quem escreve a frase acentuada e o PHP, e o teste confere contra a
    # frase da referencia. Assim o dia em que uma marca passar a declarar area
    # muda a pagina sozinho.
    pares = [m for m in ref.publicaveis()
             if ref.valor(m.get("cobertura_m2_declarada")) is not None
             and ref.valor(m.get("autonomia_min_declarada")) is not None]
    taxas = sorted({round(ref.valor(m["cobertura_m2_declarada"])
                          / float(ref.valor(m["autonomia_min_declarada"])), 2)
                    for m in pares})
    marcas_todas = sorted({m["marca"] for m in ref.publicaveis()})
    marcas_com_cobertura = sorted({m["marca"] for m in pares})
    marcas_sem_cobertura = [b for b in marcas_todas if b not in marcas_com_cobertura]

    sem_pa = [m for m in ref.publicaveis() if ref.valor(m.get("pa_declarado")) is None]
    marcas_com_pa = {m["marca"] for m in ref.publicaveis()
                     if ref.valor(m.get("pa_declarado")) is not None}
    marcas_sem_pa = sorted({m["marca"] for m in sem_pa})

    contexto = {
        "conversao": {
            "marcas_publicaveis": len(marcas_todas),
            "marcas_sem_cobertura": [ref.marcas[b]["nome"] for b in marcas_sem_cobertura],
            "taxa_minima": taxas[0] if taxas else None,
            "taxa_maxima": taxas[-1] if taxas else None,
            "dispersao_pct": (int(round((taxas[-1] / taxas[0] - 1) * 100))
                              if len(taxas) >= 2 else None),
        },
        "funil": {
            "sem_pa": len(sem_pa),
            "publicaveis": len(ref.publicaveis()),
            "marcas_mudas": [ref.marcas[b]["nome"] for b in marcas_sem_pa
                             if b not in marcas_com_pa],
            "marcas_parciais": [ref.marcas[b]["nome"] for b in marcas_sem_pa
                                if b in marcas_com_pa],
        },
        "tempo_total": {
            "com_cobertura": len(v["tempo_total"]["modelos_com_cobertura_declarada"]),
            "com_recarga": len(v["tempo_total"]["modelos_com_recarga_declarada"]),
            "com_os_tres": len(v["tempo_total"]["modelos_com_os_tres_numeros"]),
        },
    }

    modelos_esperando = [m for m in modelos if m["esperando_link"]]

    resumo = {
        "modelos_publicaveis": len(ref.publicaveis()),
        "modelos_na_tela": len(modelos),
        "modelos_esperando_link": len(modelos_esperando),
        "modelos_com_link": len(modelos) - len(modelos_esperando),
        "modelos_de_referencia": len(refs),
        "situacoes": len(situacoes),
        "situacoes_por_ponte": sum(1 for s in situacoes.values() if s["por_ponte"]),
        "situacoes_no_portao": sum(
            1 for k in classificacao if len(classificacao[k]["elegiveis"]) >= 3),
        "linhas_de_exemplo": len(exemplos),
        "marcas": len(marcas_todas),
    }

    fatos = {
        "id": "r2-respostas",
        "ilha": "robometria",
        "entidade": "medicao",
        "gerado_por": "ferramentas/gerar-r2.py",
        "banco_gerado_em": ref.doc_modelos["gerado_em"],
        "o_que_e": (
            "Combustivel da ferramenta R2 no site: as 9 situacoes de piso x pelo com "
            "os limiares de Pa que cada fonte brasileira declara para elas, a "
            "classificacao dos modelos do banco em cada situacao, e os numeros de cada "
            "modelo de referencia. Sem prosa: a frase que o visitante le e montada "
            "pelo snippet, em portugues acentuado, e conferida contra a implementacao "
            "de referencia por ferramentas/teste-r2.php."
        ),
        "entrada": {
            "area_minima": ref.AREA_MINIMA,
            "area_maxima": ref.AREA_MAXIMA,
            "pisos": [{"id": p, "rotulo": ref.NOME_DO_PISO[p]} for p in ref.PISOS],
            "pelos": [{"id": p, "rotulo": ref.NOME_DO_PELO[p]} for p in ref.PELOS],
        },
        "ancora": {
            "area": area_ancora,
            "situacao": chave(sit_ancora[0], sit_ancora[1]),
            "modelo_de_referencia": m_ancora["id"],
            "metragens_do_corpus": [{"m2": a, "onde": o}
                                    for a, o in ref.METRAGENS_DO_CORPUS],
        },
        "situacoes": situacoes,
        "classificacao": classificacao,
        # A escada inteira, e nao so o degrau dos modelos de hoje: e ela que o
        # teste le como regua e e dela que sai a linha de procedencia do cartao.
        "rotulos_de_origem": ref.ROTULOS_DE_ORIGEM,
        "modelos": modelos,
        "modelos_de_referencia": [m["id"] for m in refs],
        "exemplos": exemplos,
        "contexto": contexto,
        "resumo": resumo,
    }

    gabarito = {
        "id": "r2-referencia",
        "ilha": "robometria",
        "entidade": "medicao",
        "gerado_por": "ferramentas/gerar-r2.py",
        "o_que_e": (
            "GABARITO da R2: a GRADE de respostas ja em frase, escrita pela "
            "implementacao de referencia ferramentas/cobertura-r2.py. Nao vai para o "
            "site (publicar=false). Existe para ferramentas/teste-r2.php provar, caso a "
            "caso e ignorando acento, que o PHP do snippet diz a MESMA coisa que a "
            "referencia — nas 9 situacoes inteiras e na metragem varrida de %d em %d m2 "
            "contra cada modelo de referencia." % (ref.PASSO_DA_VARREDURA,
                                                   ref.PASSO_DA_VARREDURA)
        ),
        "areas_de_cartao": areas_de_cartao,
        "situacoes": referencia_situacoes,
        "cartoes": cartoes,
        "ciclos": ciclos,
        "contexto": {
            "conversao": ref.frase_da_recusa_de_conversao(),
            "funil": ref.frase_do_funil_partido(),
            "classe_de_fonte": ref.frase_da_classe_de_fonte(),
        },
    }

    return fatos, gabarito


def main():
    fatos, gabarito = montar()
    r = fatos["resumo"]

    print("Robometria — combustivel da R2 gerado da implementacao de referencia")
    print("")
    print("  situacoes (piso x pelo) ......... %d" % r["situacoes"])
    print("    por ponte ..................... %d" % r["situacoes_por_ponte"])
    print("    passam no portao de 3 itens ... %d" % r["situacoes_no_portao"])
    print("  modelos publicaveis ............. %d" % r["modelos_publicaveis"])
    print("  modelos que aparecem na tela .... %d" % r["modelos_na_tela"])
    print("  modelos de referencia ........... %d" % r["modelos_de_referencia"])
    print("  linhas da tabela de exemplos .... %d" % r["linhas_de_exemplo"])
    print("")
    print("  ancora .......................... %s m2, %s"
          % (fatos["ancora"]["area"], fatos["ancora"]["situacao"]))
    print("  modelo de referencia da ancora .. %s" % fatos["ancora"]["modelo_de_referencia"])
    print("")
    print("  casos no gabarito ............... %d situacoes + %d cartoes + %d ciclos"
          % (len(gabarito["situacoes"]), len(gabarito["cartoes"]), len(gabarito["ciclos"])))
    print("")
    print("  modelos esperando link de loja .. %d  <- trabalho pendente (secao 7)"
          % r["modelos_esperando_link"])
    print("")

    if "--gravar" not in sys.argv:
        print("  (rode com --gravar para escrever dados/r2-respostas.json e "
              "dados/r2-referencia.json)")
        return 0

    for nome, doc in (("r2-respostas.json", fatos), ("r2-referencia.json", gabarito)):
        caminho = os.path.join(DADOS, nome)
        with open(caminho, "w", encoding="utf-8") as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        print("  gravado: dados/%s (%d bytes)" % (nome, os.path.getsize(caminho)))

    return 0


if __name__ == "__main__":
    sys.exit(main())
