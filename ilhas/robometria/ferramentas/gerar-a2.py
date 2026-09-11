#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o combustivel do artigo-ancora A2 a partir do BANCO commitado.

    python3 ferramentas/gerar-a2.py            # relatorio na tela
    python3 ferramentas/gerar-a2.py --gravar   # grava o arquivo abaixo

Grava:
  dados/a2-fatos.json   FATOS, sem prosa. O Sync o leva para a option
                        robometria_dados_a2-fatos e o snippet
                        robometria-a2.php escreve as frases a partir dele.
                        publicar=true no manifest.

POR QUE O ARTIGO TEM GERADOR, e nao e so texto escrito a mao.

Vale aqui a mesma razao do A1, e ela virou decisao 1 do bloco 5 no PROMPT.md
desta ilha: um artigo cuja tese e um NUMERO nao pode ter esse numero digitado
dentro do HTML, porque no dia em que o banco crescer o texto passa a mentir em
silencio — e "em silencio" e o ponto, porque ninguem rele artigo publicado. Aqui
a tese e derivada do mesmo banco que alimenta a R2, e o snippet so escreve a
frase.

O QUE ELE MEDE — tres afirmacoes, separadas de proposito, cada uma com o proprio
molde escolhido pela contagem:

  1. QUEM DECLARA AREA POR CARGA. Quantos modelos publicaveis trazem
     cobertura_m2_declarada, e de quantas MARCAS. E o numero que decide se a
     frase "quase nenhum fabricante declara" pode ser escrita.
  2. OS TRES NUMEROS DA CONTA DE TEMPO. Cobertura por carga, autonomia e
     recarga. Quantos modelos tem os tres — hoje, nenhum. E a medida de por que
     "o robo limpa a sua casa em X horas" nao e uma conta que alguem possa
     fechar com dado publicado.
  3. A DISPERSAO ENTRE OS PARES DECLARADOS. Quando ha dois ou mais pares
     (minutos, m2), a taxa implicita de cada um e o espalhamento entre elas. E o
     argumento mais forte contra a conversao: se o proprio fabricante nao e
     consistente consigo mesmo, uma taxa geral de mercado nao existe.

O QUE ELE NAO FAZ: nao coleta nada e nao chama rede. Todo numero daqui sai de
dados/modelos-robo.json e dados/marcas.json, e a leitura do banco vem da MESMA
implementacao de referencia que a R2 usa (ferramentas/cobertura-r2.py), para as
duas paginas nunca publicarem contagens diferentes da mesma coisa.

O ACENTO. Diferente do que o A1 fez em 10/09/2026, o texto publicavel que sai
daqui — as perguntas e as respostas do FAQPage — sai ACENTUADO. O banco desta
ilha e ASCII porque ele CITA fontes; o que a ilha ESCREVE sai em portugues de
verdade (fase 4b do playbook). O A1 publicou "Nao. Nas 16 pecas..." dentro do
JSON-LD, que e justamente o canal que a secao 5 do ARQUIPELAGO.md diz valer
tanto quanto ranquear. Ver dados/a1-fatos.json, corrigido na mesma execucao.
"""

import importlib.util
import json
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = os.path.join(BASE, "dados")


def _carregar_referencia():
    """Importa ferramentas/cobertura-r2.py como modulo (o hifen impede o import
    normal). A referencia e uma so, e o artigo nao ganha uma copia dela."""
    caminho = os.path.join(BASE, "ferramentas", "cobertura-r2.py")
    spec = importlib.util.spec_from_file_location("cobertura_r2", caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


ref = _carregar_referencia()


def taxa(m):
    """m2 por minuto implicita num par declarado. Duas casas, como a fonte dá."""
    return round(ref.valor(m["cobertura_m2_declarada"])
                 / float(ref.valor(m["autonomia_min_declarada"])), 2)


def num(n):
    return "{:,}".format(int(n)).replace(",", ".")


def dec(v):
    return ("%.2f" % v).replace(".", ",")


# ------------------------------------------------------------------ MEDICAO
def medir():
    pub = ref.publicaveis()

    com_cobertura = [m for m in pub
                     if ref.valor(m.get("cobertura_m2_declarada")) is not None]
    com_autonomia = [m for m in pub
                     if ref.valor(m.get("autonomia_min_declarada")) is not None]
    com_recarga = [m for m in pub
                   if ref.valor(m.get("recarga_min_declarada")) is not None]
    com_os_tres = [m for m in com_cobertura
                   if ref.valor(m.get("recarga_min_declarada")) is not None
                   and ref.valor(m.get("autonomia_min_declarada")) is not None]

    marcas_todas = sorted({m["marca"] for m in pub})
    marcas_com = sorted({m["marca"] for m in com_cobertura})
    marcas_sem = [b for b in marcas_todas if b not in marcas_com]

    # Os pares (minutos, m2): so eles sustentam qualquer conversao, e sao
    # exatamente o que o mercado nao publica.
    pares = [m for m in com_cobertura
             if ref.valor(m.get("autonomia_min_declarada")) is not None]
    pares_fatos = sorted(
        [{
            "modelo": m["id"],
            "rotulo": ref.rotulo_do_modelo(m),
            "marca": ref.marcas[m["marca"]]["nome"],
            "cobertura_m2": ref.valor(m["cobertura_m2_declarada"]),
            "autonomia_min": ref.valor(m["autonomia_min_declarada"]),
            "taxa": taxa(m),
        } for m in pares],
        key=lambda x: (x["taxa"], x["modelo"]),
    )

    taxas = sorted({p["taxa"] for p in pares_fatos})
    marcas_dos_pares = sorted({p["marca"] for p in pares_fatos})

    dispersao = None
    if len(taxas) >= 2:
        dispersao = {
            "taxa_minima": taxas[0],
            "taxa_maxima": taxas[-1],
            "pct": int(round((taxas[-1] / taxas[0] - 1) * 100)),
            "taxas_distintas": len(taxas),
            "marcas": marcas_dos_pares,
            "mesma_marca": len(marcas_dos_pares) == 1,
        }

    return {
        "pub": pub,
        "com_cobertura": com_cobertura,
        "com_autonomia": com_autonomia,
        "com_recarga": com_recarga,
        "com_os_tres": com_os_tres,
        "marcas_todas": marcas_todas,
        "marcas_com": marcas_com,
        "marcas_sem": marcas_sem,
        "pares": pares_fatos,
        "dispersao": dispersao,
    }


# -------------------------------------------------------------------- VITRINE
def vitrine(med):
    """Os modelos que DECLARAM area por carga — e o cartao diz que e por isso.

    NAO e um ranking de qualidade de limpeza, e a pagina escreve isso com todas
    as letras. E a lista dos unicos modelos do banco sobre os quais a pergunta
    do titulo tem resposta do fabricante, o que e uma informacao de compra de
    verdade: com esse numero da para calcular ciclos; sem ele, nao da.

    A ordem e por cobertura declarada, da maior para a menor, e o desempate e o
    id — nunca a comissao, nunca quem tem link (secao 7 do ARQUIPELAGO.md). O
    campo de afiliado viaja mesmo vazio, para a pagina RESERVAR o lugar do link
    em vez de esconder o bloco.
    """
    itens = []
    for m in sorted(med["com_cobertura"],
                    key=lambda x: (-ref.valor(x["cobertura_m2_declarada"]), x["id"])):
        a = m.get("afiliado") or {}
        imagem = m.get("imagem") or {}
        retoma = ref.valor(m.get("retoma_apos_recarga"))
        itens.append({
            "modelo": m["id"],
            "rotulo": ref.rotulo_do_modelo(m),
            "cobertura_m2": ref.valor(m["cobertura_m2_declarada"]),
            "autonomia_min": ref.valor(m.get("autonomia_min_declarada")),
            "recarga_min": ref.valor(m.get("recarga_min_declarada")),
            "retoma_apos_recarga": retoma,
            "tem_imagem": bool(imagem.get("url")),
            "esperando_link": not a.get("url"),
            "afiliado": {
                "url": a.get("url") or "",
                "programa": a.get("plataforma") or None,
                "sub_id_1": a.get("sub_id_1") or "robometria",
                "sub_id_2": a.get("sub_id_2") or "A2",
            },
        })
    return itens


# ------------------------------------------------------------------ PERGUNTAS
def perguntas(f):
    """As perguntas do FAQPage, montadas dos FATOS — nunca escritas a mao.

    Cada uma e uma formulacao real do corpus (dados/corpus-buscas.md, clusters
    B2 e B3), e cada resposta e DERIVADA da contagem, com molde escolhido por
    medicao. Pergunta em JSON-LD que a pagina nao responde e marcacao que promete
    o que nao entrega — e resposta que nao muda quando o banco muda e pior
    ainda, porque continua sendo lida depois de deixar de valer.

    Sai ACENTUADO: e texto que a ilha escreve, nao transcricao de fonte.
    """
    r = f["resumo"]
    lista = []

    # --------------------------------------------------- 1. quantos m2 limpa
    if r["com_cobertura"] == 0:
        resp = (
            "Nenhum dos %s modelos de robô aspirador que a Robometria conferiu tem "
            "área por carga declarada pelo fabricante. Todo número de m² que "
            "circula sobre eles foi calculado por terceiros a partir dos minutos "
            "de autonomia."
            % num(r["modelos_publicaveis"])
        )
    elif len(f["marcas_que_declaram"]) == 1:
        resp = (
            "Depende do fabricante dizer, e quase nenhum diz. Dos %s modelos que a "
            "Robometria conferiu, %s declaram área coberta por carga, e todos são "
            "de uma marca só (%s) — as outras %s não publicam o número em canal "
            "nenhum. Quando um site promete metragem para um robô dessas marcas, "
            "esse número foi calculado por alguém, não declarado pelo fabricante."
            % (num(r["modelos_publicaveis"]), num(r["com_cobertura"]),
               f["marcas_que_declaram"][0], num(len(f["marcas_que_nao_declaram"])))
        )
    else:
        resp = (
            "Depende do fabricante dizer, e poucos dizem. Dos %s modelos que a "
            "Robometria conferiu, %s declaram área coberta por carga, em %s marcas "
            "— as outras %s não publicam o número em canal nenhum."
            % (num(r["modelos_publicaveis"]), num(r["com_cobertura"]),
               num(len(f["marcas_que_declaram"])), num(len(f["marcas_que_nao_declaram"])))
        )
    lista.append({
        "pergunta": "Quantos m² um robô aspirador limpa por carga?",
        "resposta": resp,
    })

    # ------------------------------------------- 2. quanto tempo para limpar
    if r["com_os_tres"] == 0:
        resp2 = (
            "Não dá para saber com dado publicado, e essa é a resposta honesta. A "
            "conta precisa de três números declarados pelo fabricante — área por "
            "carga, autonomia e tempo de recarga — e nenhum dos %s modelos que a "
            "Robometria conferiu tem os três: %s declaram a área, %s declaram a "
            "recarga, e os conjuntos não se sobrepõem em modelo nenhum."
            % (num(r["modelos_publicaveis"]), num(r["com_cobertura"]),
               num(r["com_recarga"]))
        )
    else:
        resp2 = (
            "Dá, para %s dos %s modelos que a Robometria conferiu — são os que têm "
            "os três números declarados pelo fabricante: área por carga, autonomia "
            "e tempo de recarga. Para os outros, qualquer tempo total publicado "
            "usou um número que ninguém declarou."
            % (num(r["com_os_tres"]), num(r["modelos_publicaveis"]))
        )
    lista.append({
        "pergunta": "Quanto tempo um robô aspirador leva para limpar a casa inteira?",
        "resposta": resp2,
    })

    # ------------------------------- 3. da para converter minutos em metros?
    d = f["dispersao"]
    if d is None:
        resp3 = (
            "Não com o que está publicado. A Robometria tem %s par (minutos, m²) "
            "declarado pelo próprio fabricante, e um ponto não é um coeficiente: "
            "com ele não se estima nada sobre um robô diferente."
            % num(len(f["pares"]))
        )
    elif d["mesma_marca"]:
        resp3 = (
            "Não. Os %s pares (minutos, m²) declarados que a Robometria tem são "
            "todos da mesma marca, e mesmo assim a taxa implícita vai de %s a %s "
            "m² por minuto — %s%% de diferença dentro do MESMO fabricante. Se o "
            "fabricante não é consistente consigo mesmo, uma taxa geral de mercado "
            "não existe."
            % (num(len(f["pares"])), dec(d["taxa_minima"]), dec(d["taxa_maxima"]),
               num(d["pct"]))
        )
    else:
        resp3 = (
            "Não com segurança. Entre os %s pares (minutos, m²) declarados que a "
            "Robometria tem, em %s marcas, a taxa implícita vai de %s a %s m² por "
            "minuto — %s%% de diferença. Aplicar uma média a um robô que não está "
            "nessa lista é dar ao leitor um número que nenhum fabricante sustenta."
            % (num(len(f["pares"])), num(len(d["marcas"])), dec(d["taxa_minima"]),
               dec(d["taxa_maxima"]), num(d["pct"]))
        )
    lista.append({
        "pergunta": "Dá para calcular a área que um robô limpa a partir dos minutos de autonomia?",
        "resposta": resp3,
    })

    return lista


# -------------------------------------------------------------------- MONTAR
def montar():
    med = medir()

    esperando = len([m for m in med["com_cobertura"]
                     if not (m.get("afiliado") or {}).get("url")])

    f = {
        "id": "a2-fatos",
        "ilha": "robometria",
        "artigo": "A2",
        "gerado_em": ref.doc_modelos["gerado_em"],
        "nota": (
            "Fatos do artigo-ancora A2, derivados do banco commitado por "
            "ferramentas/gerar-a2.py, lendo o banco pela mesma implementacao de "
            "referencia que a R2 usa. Nenhum numero aqui e digitado: se o banco "
            "crescer e a tese do artigo deixar de valer, e este arquivo que muda, e "
            "ferramentas/teste-a2.php reprova a pagina antes de ela ir ao ar dizendo "
            "o que o banco nao sustenta."
        ),
        "serp": {
            "verificada_nesta_execucao": False,
            "por_que": (
                "O egresso HTTP desta nuvem alcanca apenas os dominios das ilhas, e "
                "esta execucao nao teve busca web. A secao 14.9 do ARQUIPELAGO.md "
                "manda escrever 'nao verifiquei' em vez de inventar diagnostico de "
                "SERP, e e o que este campo faz."
            ),
            "classificacao_herdada": (
                "Secao 2.1 de dados/especificacao-calculadoras.md, de 09/09/2026: a "
                "familia de consultas de m2 e autonomia foi classificada como alvo "
                "PARCIAL — a cabeca ('o que e Pa', 'quantos m2 um robo limpa') esta "
                "tomada por veiculo grande (Canaltech, Mundo Conectado, aprouter) e a "
                "Robometria NAO a disputa; a cauda com a casa da pessoa dentro, e a "
                "pergunta de PROCEDENCIA do numero, e onde a resposta com fonte e data "
                "ganha. Este artigo mira a segunda."
            ),
            "consulta_alvo": "de onde vem o numero de m2 que os sites publicam sobre robo aspirador",
            "por_que_chega_as_dez_primeiras": (
                "Nenhuma das paginas que ocupam a cabeca desta familia publica a "
                "contagem de quantos fabricantes declaram area por carga, nem a "
                "dispersao entre os pares declarados. Elas publicam o numero; esta "
                "publica de onde ele vem, com o catalogo contado e datado."
            ),
        },
        "resumo": {
            "modelos_publicaveis": len(med["pub"]),
            "marcas": len(med["marcas_todas"]),
            "com_cobertura": len(med["com_cobertura"]),
            "sem_cobertura": len(med["pub"]) - len(med["com_cobertura"]),
            "com_autonomia": len(med["com_autonomia"]),
            "com_recarga": len(med["com_recarga"]),
            "com_os_tres": len(med["com_os_tres"]),
            "pares_declarados": len(med["pares"]),
            "modelos_esperando_link": esperando,
        },
        "marcas_que_declaram": [ref.marcas[b]["nome"] for b in med["marcas_com"]],
        "marcas_que_nao_declaram": [ref.marcas[b]["nome"] for b in med["marcas_sem"]],
        "com_recarga_ids": [{"modelo": m["id"], "rotulo": ref.rotulo_do_modelo(m),
                             "recarga_min": ref.valor(m["recarga_min_declarada"])}
                            for m in med["com_recarga"]],
        "pares": med["pares"],
        "dispersao": med["dispersao"],
        "vitrine": vitrine(med),
    }
    f["perguntas"] = perguntas(f)
    return f


def relatorio(f):
    r = f["resumo"]
    print("Robometria — fatos do artigo-ancora A2")
    print("")
    print("  modelos publicaveis ............. %d" % r["modelos_publicaveis"])
    print("  com area por carga declarada .... %d  (marcas: %s)"
          % (r["com_cobertura"], ", ".join(f["marcas_que_declaram"]) or "nenhuma"))
    print("  SEM area por carga .............. %d  (marcas: %s)"
          % (r["sem_cobertura"], ", ".join(f["marcas_que_nao_declaram"]) or "nenhuma"))
    print("  com autonomia declarada ......... %d" % r["com_autonomia"])
    print("  com recarga declarada ........... %d" % r["com_recarga"])
    print("  com os TRES numeros ............. %d  <- a conta de tempo so fecha aqui"
          % r["com_os_tres"])
    print("  pares (minutos, m2) ............. %d" % r["pares_declarados"])
    if f["dispersao"]:
        d = f["dispersao"]
        print("  dispersao entre as taxas ........ %s a %s m2/min  (%d%%, %s)"
              % (dec(d["taxa_minima"]), dec(d["taxa_maxima"]), d["pct"],
                 "mesma marca" if d["mesma_marca"] else "marcas diferentes"))
    print("  itens na vitrine ................ %d" % len(f["vitrine"]))
    print("  destes, esperando link de loja .. %d  <- trabalho pendente (secao 7)"
          % r["modelos_esperando_link"])
    print("")
    print("  PERGUNTAS DO FAQPage")
    for p in f["perguntas"]:
        print("   - %s" % p["pergunta"])
        print("     %s" % p["resposta"][:150])
    print("")


def main():
    f = montar()
    relatorio(f)

    if "--gravar" not in sys.argv:
        print("  (rode com --gravar para escrever dados/a2-fatos.json)")
        return 0

    caminho = os.path.join(DADOS, "a2-fatos.json")
    with open(caminho, "w", encoding="utf-8") as fh:
        json.dump(f, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("  gravado: dados/a2-fatos.json (%d bytes)" % os.path.getsize(caminho))
    return 0


if __name__ == "__main__":
    sys.exit(main())
