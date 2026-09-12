#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A VARREDURA DA SECAO 14.3 — quantos produtos elegiveis cada faixa das ferramentas tem.

    python3 ferramentas/cobertura.py              # escreve dados/cobertura.json
    python3 ferramentas/cobertura.py --conferir   # nao escreve; falha se o arquivo estiver velho

O que a secao 14.3 do ARQUIPELAGO.md manda, palavra por palavra: "nenhuma faixa que as
ferramentas da ilha conseguem produzir pode sair sem pelo menos 3 produtos elegiveis.
Mede-se varrendo a faixa de entrada de cada ferramenta de ponta a ponta e contando
quantos itens do banco passam em TODAS as condicoes declaradas. O que falta nessa
varredura e a lista de compras do banco — e o numero final aparece sozinho."

Esta ilha nunca tinha feito essa varredura. O que existia era a matriz escrita a mao do
esquema: 18 celulas de cola e 9 de rejunte, que sao AMOSTRA com nome de grade para uma
ferramenta que serve 45 e 60. A amostra foi escolhida com cuidado — as celulas do rejunte
pisam de proposito nas bordas declaradas — mas amostra nao responde "quantas faixas saem
sem 3 elegiveis", porque a resposta e uma contagem sobre a entrada INTEIRA.

AS TRES FONTES, E POR QUE SAO TRES:

  1. A FAIXA vem de `ferramentas/faixa-da-f2.php`, que a mede PROVOCANDO o snippet. Nao
     ha um numero de estado digitado neste arquivo. Faixa digitada mediria a faixa que
     alguem lembrou, e ficaria verde no dia em que o campo da junta mudasse de teto.

  2. A REGUA e a de `ferramentas/validar-banco.py`, importada daqui. Ela recomputa a
     elegibilidade das DECLARACOES dos fabricantes pelas regras do esquema, e foi escrita
     no bloco 3 antes de existir uma linha do snippet PHP. Reimplementar a regra uma
     terceira vez aqui nao acrescentaria independencia nenhuma — acrescentaria uma copia
     para envelhecer calada, que e a cicatriz que a secao 8 do contrato cobra.

  3. O QUE O SITE SERVE e conferido por `ferramentas/conferir-cobertura.php`, que anda os
     mesmos estados chamando o snippet, um processo por estado. As duas metades tem que
     dar o mesmo numero nos 105 estados. Ate hoje elas so se cruzavam em 27.

O QUE ESTE ARQUIVO NAO FAZ: ele nao decide o que comprar. Ele conta o buraco e nomeia a
causa que o proprio calculo separou — faixa de junta, ambiente nao declarado, silencio do
fabricante, categoria que nao existe no banco. Escolher produto e coleta, e coleta tem
fonte, data e as travas da secao 8.
"""

import io
import json
import os
import subprocess
import sys
import contextlib
import importlib.util

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = os.path.join(BASE, "dados")
FERRAMENTAS = os.path.join(BASE, "ferramentas")
SAIDA = os.path.join(DADOS, "cobertura.json")

# A secao 14.3 do contrato e quem fixa este numero. Ele e REGRA, nao medicao — por isso
# esta escrito, e por isso esta escrito UMA vez, com a citacao ao lado.
MINIMO_DA_SECAO_14_3 = 3
CITACAO = ("secao 14.3 do ARQUIPELAGO.md: nenhuma faixa que as ferramentas da ilha "
           "conseguem produzir pode sair sem pelo menos 3 produtos elegiveis")


def morrer(msg):
    sys.stderr.write("FALHA: %s\n" % msg)
    sys.exit(1)


# ------------------------------------------------------------------ 1. a faixa

def medir_faixa():
    """Pergunta ao snippet qual e a faixa dele. Nunca supoe."""
    script = os.path.join(FERRAMENTAS, "faixa-da-f2.php")
    if not os.path.exists(script):
        morrer("ferramentas/faixa-da-f2.php nao existe; sem ele a faixa seria digitada.")
    r = subprocess.run(["php", script, BASE], capture_output=True, text=True)
    if r.returncode != 0:
        morrer("faixa-da-f2.php falhou:\n%s" % r.stderr.strip())
    return json.loads(r.stdout)["faixa"]


# ------------------------------------------------------------------ 2. a regua

def carregar_regua():
    """Importa validar-banco.py como modulo, calado, e exige que o banco esteja valido.

    Censo sobre banco invalido e numero com cara de conferido — exatamente o que a secao 8
    chama de pior que numero digitado.
    """
    caminho = os.path.join(FERRAMENTAS, "validar-banco.py")
    spec = importlib.util.spec_from_file_location("cdm_validar_banco", caminho)
    mod = importlib.util.module_from_spec(spec)
    silencio = io.StringIO()
    try:
        with contextlib.redirect_stdout(silencio):
            spec.loader.exec_module(mod)
    except SystemExit:
        morrer("validar-banco.py reprovou o banco. O censo nao roda sobre banco invalido.\n"
               + silencio.getvalue())
    if getattr(mod, "erros", None):
        morrer("validar-banco.py acusou %d erro(s); corrija o banco antes do censo."
               % len(mod.erros))
    return mod


# ------------------------------------------------------------------ 3. o censo

def elegiveis(celula):
    """Elegivel e quem a pagina pode recomendar: topo mais os abaixo do topo.

    `mencionados_com_ressalva` NAO conta, e essa e a decisao que mais mexe no numero
    final. Um produto que so entra com ressalva e, pela regra 5 do esquema, sustentado
    por fonte fraca demais para virar recomendacao — contar ele aqui inflaria a cobertura
    exatamente onde a ilha e mais fraca, que e a procedencia. A secao 10 do contrato ja
    decide a direcao quando ha duvida: errar para baixo custa uma frase mais fraca na
    tela; errar para cima faz a ilha declarar um rigor que ela nao tem.
    """
    return sorted(celula["recomendados_topo"] + celula["elegiveis_abaixo_do_topo"])


def varrer(regua, faixa):
    estados = {"cola": [], "rejunte": []}

    for base in faixa["base"]:
        for ambiente in faixa["ambiente"]:
            c = regua.computar_celula(base, ambiente)
            eleg = elegiveis(c)
            estados["cola"].append({
                "base": base,
                "ambiente": ambiente,
                "elegiveis": eleg,
                "quantos_elegiveis": len(eleg),
                "com_ressalva": c["mencionados_com_ressalva"],
                "eliminados_por_proibicao": c["eliminados_por_proibicao"],
                "eliminados_por_silencio": c["eliminados_por_silencio"],
            })

    for junta in faixa["junta_mm"]:
        for ambiente in faixa["ambiente"]:
            c = regua.computar_celula_rejunte(junta, ambiente)
            eleg = elegiveis(c)
            estados["rejunte"].append({
                "junta_mm": junta,
                "ambiente": ambiente,
                "elegiveis": eleg,
                "quantos_elegiveis": len(eleg),
                "com_ressalva": c["mencionados_com_ressalva"],
                "eliminados_por_faixa_de_junta": c["eliminados_por_faixa_de_junta"],
                "eliminados_por_ambiente": c["eliminados_por_ambiente"],
            })

    return estados


def causa_da_cola(e):
    """A causa que o proprio calculo separou. Nunca uma hipotese.

    A secao 7 do contrato cobra isto na TELA e a licao vale na planilha: causa que o
    codigo separa, o texto separa. Aqui ha duas listas na mao, entao a frase diz qual das
    duas esvaziou a celula, e diz 'as duas' quando as duas contribuiram.
    """
    proib = bool(e["eliminados_por_proibicao"])
    sil = bool(e["eliminados_por_silencio"])
    if proib and sil:
        return "o fabricante proibe uns e nao declara os outros"
    if proib:
        return "o fabricante proibe nesta base ou neste ambiente"
    if sil:
        return "o fabricante nao declara esta base ou este ambiente"
    return "o banco nao tem produto suficiente nesta categoria"


def causa_do_rejunte(e):
    faixa = bool(e["eliminados_por_faixa_de_junta"])
    amb = bool(e["eliminados_por_ambiente"])
    if faixa and amb:
        return "a faixa de junta exclui uns e o ambiente nao declarado exclui os outros"
    if faixa:
        return "a faixa de junta declarada nao cobre esta largura"
    if amb:
        return "o fabricante nao declara este ambiente"
    return "o banco nao tem produto suficiente nesta categoria"


def montar(regua, faixa, estados):
    materiais = regua.materiais
    voc_categorias = list(regua.VOC["categoria_material"])

    no_banco = {}
    for m in materiais.values():
        if m.get("status") != "ativo":
            continue
        no_banco[m.get("categoria")] = no_banco.get(m.get("categoria"), 0) + 1

    descobertas = {
        "cola": [e for e in estados["cola"] if e["quantos_elegiveis"] < MINIMO_DA_SECAO_14_3],
        "rejunte": [e for e in estados["rejunte"] if e["quantos_elegiveis"] < MINIMO_DA_SECAO_14_3],
    }

    for e in descobertas["cola"]:
        e["por_que"] = causa_da_cola(e)
    for e in descobertas["rejunte"]:
        e["por_que"] = causa_do_rejunte(e)

    def resumo(chave):
        todos = estados[chave]
        contagens = [e["quantos_elegiveis"] for e in todos]
        return {
            "estados_varridos": len(todos),
            "estados_com_o_minimo": sum(1 for n in contagens if n >= MINIMO_DA_SECAO_14_3),
            "estados_descobertos": sum(1 for n in contagens if n < MINIMO_DA_SECAO_14_3),
            "estados_sem_nenhum_elegivel": sum(1 for n in contagens if n == 0),
            "maior_numero_de_elegiveis_em_um_estado": max(contagens) if contagens else 0,
            "menor_numero_de_elegiveis_em_um_estado": min(contagens) if contagens else 0,
        }

    # A LISTA DE COMPRAS, derivada e nunca digitada: a categoria do vocabulario que o
    # banco nao tem nenhum item e a unica lacuna que nenhuma coleta de cola ou de rejunte
    # fecha, por mais produto que entre.
    categorias_vazias = [c for c in voc_categorias if no_banco.get(c, 0) == 0]

    derivado_de = {}
    for nome in ("esquema-banco.json", "materiais-colas.json", "materiais-rejuntes.json"):
        caminho = os.path.join(DADOS, nome)
        if os.path.exists(caminho):
            with open(caminho, encoding="utf-8") as fh:
                derivado_de[nome] = json.load(fh).get("gerado_em", "sem gerado_em")
    derivado_de["snippets/clubedomosaico-f2.php"] = "a faixa de entrada, medida em cada varredura"

    return {
        "id": "cobertura",
        "ilha": "clubedomosaico",
        "bloco": "varredura da secao 14.3",
        "gerado_por": "ferramentas/cobertura.py",
        # SEM CARIMBO DE RELOGIO, de proposito: o censo e funcao das entradas, nao da
        # hora em que rodou. Com um timestamp dentro, `--conferir` acusaria "arquivo
        # velho" a cada execucao e o portao viraria ruido que alguem desliga. O que
        # data o arquivo e a data das fontes que ele leu.
        "derivado_de": derivado_de,
        "o_que_este_arquivo_e": (
            "O censo de cobertura das duas ferramentas da ilha: para CADA estado que a F2 "
            "consegue servir, quantos produtos do banco sao elegiveis. Serie nao: e uma "
            "fotografia do banco de hoje, e se regenera a cada mudanca de banco ou de faixa."
        ),
        "criterio": CITACAO,
        "minimo_exigido": MINIMO_DA_SECAO_14_3,
        "o_que_conta_como_elegivel": (
            "recomendados_topo + elegiveis_abaixo_do_topo. Mencao com ressalva NAO conta: "
            "pela regra 5 do esquema ela vem de fonte fraca demais para virar recomendacao."
        ),
        "faixa_varrida": {
            "fonte": "ferramentas/faixa-da-f2.php, medindo o proprio snippet",
            "bases": len(faixa["base"]),
            "ambientes": len(faixa["ambiente"]),
            "juntas_mm": len(faixa["junta_mm"]),
            "estados_de_cola": faixa["estados_de_cola"],
            "estados_de_rejunte": faixa["estados_de_rejunte"],
        },
        "banco_hoje": {
            "por_categoria": no_banco,
            "categorias_do_vocabulario_sem_nenhum_item": categorias_vazias,
        },
        "resumo": {"cola": resumo("cola"), "rejunte": resumo("rejunte")},
        "faixas_descobertas": descobertas,
        "estados": estados,
    }


def main():
    conferir = "--conferir" in sys.argv

    faixa = medir_faixa()
    regua = carregar_regua()
    estados = varrer(regua, faixa)
    censo = montar(regua, faixa, estados)

    texto = json.dumps(censo, ensure_ascii=False, indent=2, sort_keys=False) + "\n"

    if conferir:
        if not os.path.exists(SAIDA):
            morrer("dados/cobertura.json nao existe. Rode sem --conferir.")
        atual = open(SAIDA, encoding="utf-8").read()
        if atual != texto:
            morrer("dados/cobertura.json esta velho: o banco ou a faixa mudaram desde a "
                   "ultima varredura. Rode `python3 ferramentas/cobertura.py`.")
        print("OK: dados/cobertura.json bate com o banco e com a faixa de hoje.")
        return

    with open(SAIDA, "w", encoding="utf-8") as fh:
        fh.write(texto)

    r = censo["resumo"]
    print("Cobertura do Clube do Mosaico — varredura da secao 14.3")
    print("  minimo exigido por faixa ... %d produtos elegiveis" % MINIMO_DA_SECAO_14_3)
    for chave in ("cola", "rejunte"):
        s = r[chave]
        print("  %-8s estados varridos %3d | com o minimo %3d | DESCOBERTOS %3d | com zero %3d | teto %d"
              % (chave, s["estados_varridos"], s["estados_com_o_minimo"],
                 s["estados_descobertos"], s["estados_sem_nenhum_elegivel"],
                 s["maior_numero_de_elegiveis_em_um_estado"]))
    vazias = censo["banco_hoje"]["categorias_do_vocabulario_sem_nenhum_item"]
    print("  categorias do vocabulario sem UM item no banco: %d (%s)"
          % (len(vazias), ", ".join(vazias) if vazias else "nenhuma"))
    print("\nEscrito: dados/cobertura.json")


if __name__ == "__main__":
    main()
