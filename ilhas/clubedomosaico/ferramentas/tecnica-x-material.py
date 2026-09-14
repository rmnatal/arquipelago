#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O OUTRO LADO DO BANCO — a que material cada TECNICA chega, e por qual regua.

    python3 ferramentas/tecnica-x-material.py              # escreve dados/tecnica-x-material.json
    python3 ferramentas/tecnica-x-material.py --conferir   # nao escreve; falha se o arquivo estiver velho

POR QUE ESTE ARQUIVO EXISTE. O `dados/tecnicas.json` nasceu em 14/09/2026 dizendo, no
proprio cabecalho, o que lhe faltava: "este arquivo e o primeiro dos dois lados; o outro
e o banco de material declarando a que tecnica ele serve, e ele NAO existe". Este e o
outro lado — e ele nao e coleta nem digitacao: e uma CONTA sobre o que ja esta declarado
pelos fabricantes no banco de colas, feita pela regua que o `validar-banco.py` escreveu
no bloco 3 e que a F2 serve no ar desde 11/09/2026.

O QUE ELE RESPONDE, e a pergunta e a do portao da secao 9 do ARQUIPELAGO.md: quantos
itens de banco REAIS uma pagina desta tecnica poderia recomendar, e em que estados.

O QUE MUDOU NA CONTA, EM 14/09/2026, E POR QUE ISSO NAO E AFROUXAR O PORTAO. Ate hoje o
portao contava so TESSELA: quantos produtos da categoria `pastilha` o banco tem com o
tipo que a tecnica cita. As duas unicas tecnicas com material declarado por fonte citam
`caco_azulejo` e `caco_louca` — caco de prato e de azulejo nao tem fabricante e nunca
terao ficha de produto nesta ilha. O portao lia ZERO, e leria zero para sempre.

So que a pagina de uma tecnica nao recomenda caquinho. Ela responde O QUE COMPRAR PARA
COLAR AQUELE CAQUINHO, que e o eixo desta ilha escrito no PROMPT.md, e isso e produto com
fabricante, declaracao datada e link de afiliado. A `ARVORE.md` ja dizia isso na secao
4b item 6 e contava caco no item 3 da mesma secao: duas metades da mesma pagina
discordando, e quem decidia era a que tinha numero. A regua agora conta o que a pagina
pode recomendar, e ela continua mordendo — tres das cinco tecnicas seguem em zero,
porque nao declaram material nenhum e cada uma diz por escrito por que nao declara.

UMA CONTA, DOIS LEITORES. A conta mora em `validar-banco.py`
(`itens_de_banco_da_tecnica`), e este arquivo a importa em vez de reescrever. Segunda
copia de decisao e a cicatriz que esta ilha ja pagou duas vezes — com a palavra-chave da
busca em 14/09 e com o `itens_sem_piso` no mesmo dia.

O QUE ESTE ARQUIVO NAO FAZ: ele nao autoriza pagina e nao escolhe endereco. Quem decide
onde a familia mora e a `ARVORE.md` secao 4b; o que este arquivo entrega e o numero que
aquela secao mandava medir.
"""

import contextlib
import io
import importlib.util
import json
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = os.path.join(BASE, "dados")
FERRAMENTAS = os.path.join(BASE, "ferramentas")
SAIDA = os.path.join(DADOS, "tecnica-x-material.json")

# A secao 9 do contrato e quem fixa este numero. Escrito UMA vez, com a citacao ao lado.
MINIMO_DA_SECAO_9 = 3
CITACAO = ("secao 9 do ARQUIPELAGO.md: pelo menos 3 itens de banco reais e um numero "
           "calculado proprio por pagina")


def morrer(msg):
    sys.stderr.write("FALHA: %s\n" % msg)
    sys.exit(1)


def carregar_regua():
    """Importa validar-banco.py como modulo, calado, e exige banco valido.

    Mesmo desenho do `cobertura.py`, e pela mesma razao: derivado sobre banco invalido e
    numero com cara de conferido.
    """
    caminho = os.path.join(FERRAMENTAS, "validar-banco.py")
    if not os.path.exists(caminho):
        morrer("ferramentas/validar-banco.py nao existe; sem ele a regua seria uma copia.")
    spec = importlib.util.spec_from_file_location("cdm_validar_banco", caminho)
    mod = importlib.util.module_from_spec(spec)
    silencio = io.StringIO()
    try:
        with contextlib.redirect_stdout(silencio):
            spec.loader.exec_module(mod)
    except SystemExit:
        morrer("validar-banco.py reprovou o banco. O derivado nao roda sobre banco invalido.\n"
               + silencio.getvalue())
    except Exception as e:
        # Sem este ramo, quem tira a conta de la morre com um traceback cru, e traceback
        # nao diz a uma pessoa o que fazer. O caso e real: e o que acontece quando alguem
        # renomeia ou apaga `itens_de_banco_da_tecnica` supondo que ela so serve ao
        # validador.
        morrer("validar-banco.py nao carregou (%s: %s). A conta desta ilha mora la; se ela "
               "foi renomeada ou apagada, o conserto e la, nunca uma copia aqui."
               % (type(e).__name__, e))
    if getattr(mod, "erros", None):
        morrer("validar-banco.py acusou %d erro(s); corrija o banco antes." % len(mod.erros))
    for nome in ("itens_de_banco_da_tecnica", "tecnicas", "tesselas_do_banco",
                 "TESSELA_POR_TIPO", "materiais"):
        if not hasattr(mod, nome):
            morrer("validar-banco.py nao expoe %r — a conta tem de morar la, nao aqui." % nome)
    return mod


def motivo_do_zero(t):
    """Por que esta tecnica chega a zero — dito com o campo que o proprio banco escreveu.

    Zero sem causa nomeada e o que faz a proxima execucao redescobrir o bloqueio do zero.
    """
    if t.get("materiais_tipicos"):
        return ("declara material, e nenhum item do banco serve a ele — e lacuna de "
                "COLETA, nomeada estado a estado em `estados`")
    return (t.get("motivo_sem_materiais")
            or "nao declara material e nao diz por que (o validador acusa isso como erro)")


def montar(regua):
    tecnicas = regua.tecnicas.get("tecnicas", [])
    if not tecnicas:
        morrer("dados/tecnicas.json nao tem tecnica nenhuma.")

    linhas = []
    for t in tecnicas:
        conta = regua.itens_de_banco_da_tecnica(t, regua.tesselas_do_banco,
                                                regua.TESSELA_POR_TIPO)
        abre = conta["total"] >= MINIMO_DA_SECAO_9
        linha = {
            "tecnica": t.get("id"),
            "nome": t.get("nome"),
            "consulta_alvo": t.get("consulta_alvo"),
            "serp_classe": t.get("serp_classe"),
            "tesselas_declaradas": conta["tesselas_declaradas"],
            "itens_de_banco": conta["total"],
            "portao_da_secao_9": "ABERTO" if abre else "FECHADO",
            "pastilhas_do_banco": conta["pastilhas_do_banco"],
            "colas_elegiveis": conta["colas_elegiveis"],
            "estados_varridos": conta["estados_varridos"],
            "estados_com_o_minimo": conta["estados_com_o_minimo"],
            "estados_sem_nenhum_elegivel": conta["estados_sem_nenhum_elegivel"],
            "maior_numero_de_elegiveis_em_um_estado": conta["maior_numero_de_elegiveis_em_um_estado"],
            "estados": conta["estados"],
        }
        if not abre:
            linha["por_que_fechado"] = motivo_do_zero(t)
        linhas.append(linha)

    derivado_de = {}
    for nome in ("esquema-banco.json", "tecnicas.json", "materiais-colas.json",
                 "materiais-pastilhas.json"):
        caminho = os.path.join(DADOS, nome)
        if os.path.exists(caminho):
            with open(caminho, encoding="utf-8") as fh:
                derivado_de[nome] = json.load(fh).get("gerado_em", "sem gerado_em")
    derivado_de["ferramentas/validar-banco.py"] = "a regua, importada e nunca copiada"

    abertas = [l["tecnica"] for l in linhas if l["portao_da_secao_9"] == "ABERTO"]

    return {
        "id": "tecnica-x-material",
        "ilha": "clubedomosaico",
        "bloco": "o outro lado do banco — a tecnica encontra o material",
        "gerado_por": "ferramentas/tecnica-x-material.py",
        # SEM CARIMBO DE RELOGIO, pela razao escrita no cobertura.py: o derivado e funcao
        # das entradas, nao da hora em que rodou.
        "derivado_de": derivado_de,
        "o_que_este_arquivo_e": (
            "A ligacao TECNICA x MATERIAL desta ilha, calculada e nunca digitada: para cada "
            "tecnica, quais itens do banco uma pagina dela poderia recomendar, e em que "
            "estados de base e ambiente. Fotografia do banco de hoje, nao serie."
        ),
        "o_que_este_arquivo_NAO_e": (
            "Nao e pagina e nao autoriza nenhuma. Onde a familia das tecnicas mora esta "
            "decidido na ARVORE.md secao 4b; aqui esta so o numero que aquela secao mandava "
            "medir. Tambem nao e coleta: nenhuma linha daqui saiu de fonte nova."
        ),
        "criterio": CITACAO,
        "minimo_exigido": MINIMO_DA_SECAO_9,
        "o_que_conta_como_item_de_banco": (
            "as pastilhas do banco cujo tipo e a tessela que a tecnica declara, MAIS as "
            "colas que o fabricante declara elegiveis para aquela tessela em algum par "
            "base x ambiente do vocabulario. Mencao com ressalva NAO conta (mesma razao do "
            "cobertura.py). REJUNTE NAO CONTA: a regua dele decide por junta em milimetro e "
            "ambiente e nao olha a tessela, e as cinco tecnicas tem junta_tipica_mm null."
        ),
        "por_que_a_varredura_e_sobre_o_vocabulario": (
            "A pergunta aqui e sobre o BANCO — quantos itens esta tecnica pode recomendar —, "
            "nao sobre o formulario da F2. Por isso base e ambiente vem do vocabulario do "
            "esquema, e nao da faixa medida no snippet como faz o cobertura.py, que responde "
            "outra pergunta."
        ),
        "resumo": {
            "tecnicas": len(linhas),
            "com_o_portao_aberto": len(abertas),
            "quais": abertas,
            "com_o_portao_fechado": len(linhas) - len(abertas),
        },
        "tecnicas": linhas,
    }


def main():
    conferir = "--conferir" in sys.argv
    regua = carregar_regua()
    derivado = montar(regua)
    texto = json.dumps(derivado, ensure_ascii=False, indent=2, sort_keys=False) + "\n"

    if conferir:
        if not os.path.exists(SAIDA):
            morrer("dados/tecnica-x-material.json nao existe. Rode sem --conferir.")
        if open(SAIDA, encoding="utf-8").read() != texto:
            morrer("dados/tecnica-x-material.json esta velho: o banco ou as tecnicas "
                   "mudaram. Rode `python3 ferramentas/tecnica-x-material.py`.")
        print("OK: dados/tecnica-x-material.json bate com o banco de hoje.")
        return

    with open(SAIDA, "w", encoding="utf-8") as fh:
        fh.write(texto)

    print("Tecnica x material — Clube do Mosaico")
    print("  minimo da secao 9 ........ %d itens de banco por pagina" % MINIMO_DA_SECAO_9)
    for l in derivado["tecnicas"]:
        print("  %-11s %-8s itens %2d | pastilhas %d | colas %d | estados com o minimo %2d de %2d"
              % (l["tecnica"], l["portao_da_secao_9"], l["itens_de_banco"],
                 len(l["pastilhas_do_banco"]), len(l["colas_elegiveis"]),
                 l["estados_com_o_minimo"], l["estados_varridos"]))
    r = derivado["resumo"]
    print("  portao ABERTO em %d de %d tecnicas (%s)"
          % (r["com_o_portao_aberto"], r["tecnicas"],
             ", ".join(r["quais"]) if r["quais"] else "nenhuma"))
    print("\nEscrito: dados/tecnica-x-material.json")


if __name__ == "__main__":
    main()
