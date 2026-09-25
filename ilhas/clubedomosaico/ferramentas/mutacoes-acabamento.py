#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MUTACOES DA CATEGORIA ACABAMENTO — 25/09/2026.

A categoria nasceu junto com a regra que a define (`regras_da_categoria_acabamento`
no `dados/esquema-banco.json`) e com o portao que a mede (o bloco de acabamento do
`validar-banco.py`). Passada limpa em portao que nunca acusou nada nao prova nada:
cada mutacao aqui e um defeito ESCRITO DE VOLTA no banco, e portao que nao reprova
nao vale o arquivo que ocupa.

DUAS REGRAS HERDADAS dos blocos anteriores desta ilha, e as duas mordem aqui:

  (a) Mutacao que o portao ANTIGO ja pegava nao justifica portao novo. Este arquivo
      roda o `validar-banco.py` UMA vez por mutacao e separa o que so o bloco de
      acabamento viu — rodando o mesmo script com o bloco de acabamento desligado
      pela variavel de ambiente CDM_SEM_PORTAO_ACABAMENTO.

  (b) A mutacao mais valiosa e a que PRODUZ O MUNDO que o banco ainda nao tem. A
      m07 e essa: ela faz um dos sete NOMEAR vidro, que e o estado que hoje nao
      existe em registro nenhum, e mede se o portao continua coerente quando o
      achado central deste arquivo deixar de valer.

Uso:  python3 ferramentas/mutacoes-acabamento.py
"""

import copy
import json
import os
import shutil
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)
BANCO = os.path.join(ILHA, "dados", "materiais-acabamento.json")
VALIDAR_BANCO = os.path.join(AQUI, "validar-banco.py")


def item(banco, ident):
    for m in banco["materiais"]:
        if m["id"] == ident:
            return m
    raise SystemExit("mutacao aponta para item inexistente: %s" % ident)


# --------------------------------------------------------------- as mutacoes

def m01(b):
    """O objeto inteiro apagado: o registro vira um material sem o que o define."""
    del item(b, "acrilex-verniz-acrilico-fosco")["protecao"]


def m02(b):
    """A frase do fabricante sumida, com as listas intactas. E o defeito mais
    tentador de todos: o dado 'parece' completo e ninguem consegue conferir de
    onde as listas sairam."""
    item(b, "acrilex-verniz-acrilico-brilhante")["protecao"]["literal_do_fabricante"] = ""


def m03(b):
    """Um valor do vocabulario que nao entra em NENHUMA das duas listas. E o
    silencio nao lido, que e como faixa descoberta fica invisivel."""
    pr = item(b, "quartzolit-fundo-selador")["protecao"]
    pr["bases_do_vocabulario_que_a_frase_NAO_nomeia"] = [
        x for x in pr["bases_do_vocabulario_que_a_frase_NAO_nomeia"] if x != "mdf_madeira"
    ]


def m04(b):
    """O mesmo valor nas duas listas: a frase nomeia e nao nomeia ao mesmo tempo."""
    pr = item(b, "quartzolit-protetor-para-fachadas")["protecao"]
    pr["tesselas_do_vocabulario_que_a_frase_NAO_nomeia"].append("pedra")


def m05(b):
    """Momento deduzido do mecanismo do produto, sem o fabricante ter declarado —
    e o motivo apagado junto, que e o que torna a deducao invisivel."""
    pr = item(b, "quartzolit-protetor-para-fachadas")["protecao"]
    pr["momento_de_uso"] = "depois_de_rejuntar"
    pr["motivo_do_momento"] = None


def m06(b):
    """`nao_declarado` sem dizer por que: o silencio deixa de ser dito."""
    item(b, "acrilex-verniz-acrilfix-brilhante")["protecao"]["motivo_do_momento"] = None


def m07(b):
    """PRODUZ O MUNDO: o verniz passa a NOMEAR vidro, que e o estado que nenhum dos
    sete tem hoje — e o achado central deste arquivo depende de nenhum ter. Se o
    portao so funciona enquanto a lista de 'nomeia' estiver vazia, ele nao mede a
    regra, mede o acaso. Aqui a mutacao move o valor sem tirar da outra lista."""
    pr = item(b, "acrilex-verniz-acrilico-fosco")["protecao"]
    pr["bases_do_vocabulario_que_a_frase_nomeia"] = ["mdf_madeira", "vidro"]


def m08(b):
    """`nomeia_rejunte` como texto em vez de booleano: 'nao' e uma string que em
    Python e verdadeira, e a pergunta passaria a ter a resposta contraria."""
    item(b, "quartzolit-borracha-liquida-elastica")["protecao"]["nomeia_rejunte"] = "nao"


def m09(b):
    """A propriedade com nome livre: o mesmo dado com outro nome. Nenhuma regua
    consegue comparar dois registros depois disto, e o portao velho nao ve."""
    p = item(b, "quartzolit-fundo-selador")["propriedades"]
    p["secagem_horas"] = p.pop("tempo_de_secagem_h")


def m10(b):
    """`contato_com_alimento` removido — a pergunta que ninguem faz. E o campo que
    decide se a pagina de um centro de mesa pode dizer alguma coisa sobre comida."""
    del item(b, "quartzolit-verniz-protetor-para-pisos")["propriedades"]["contato_com_alimento"]


def m11(b):
    """Acabamento visual fora do vocabulario: 'acetinado' existe no mundo e nao
    existe nesta ilha, e vocabulario que aceita qualquer palavra nao e vocabulario."""
    item(b, "acrilex-verniz-acrilico-brilhante")["propriedades"]["acabamento_visual"]["valor"] = "acetinado"


def m12(b):
    """O numero incoerente que esta execucao RECUSOU, escrito de volta: o rendimento
    da borracha liquida com valor e sem fonte que o sustente."""
    p = item(b, "quartzolit-borracha-liquida-elastica")["propriedades"]["rendimento_m2"]
    p["valor"] = 70
    p["motivo"] = None


def m13(b):
    """A matriz base x ambiente preenchida num verniz: e o que faria a F2 considerar
    verniz onde ela decide COLA, e e a razao inteira de `declaracoes` ficar vazia."""
    it = item(b, "acrilex-verniz-acrilico-fosco")
    it["declaracoes"]["indicado_para"] = ["madeira", "ceramica"]
    it["motivo_declaracoes_vazias"] = None


def m14(b):
    """A fonte da frase apontando para uma chave que nao existe em fontes{}: a
    procedencia vira endereco quebrado."""
    item(b, "quartzolit-fundo-selador")["protecao"]["fonte_id"] = "boletim-que-ninguem-leu"


MUTACOES = [
    ("01 objeto `protecao` apagado", m01),
    ("02 frase do fabricante sumida, listas intactas", m02),
    ("03 valor do vocabulario fora das duas listas", m03),
    ("04 mesmo valor nomeado e nao nomeado", m04),
    ("05 momento deduzido do mecanismo, motivo apagado", m05),
    ("06 `nao_declarado` sem motivo escrito", m06),
    ("07 PRODUZ O MUNDO: o verniz passa a nomear vidro", m07),
    ("08 `nomeia_rejunte` como texto em vez de booleano", m08),
    ("09 propriedade com nome livre (secagem_horas)", m09),
    ("10 `contato_com_alimento` removido", m10),
    ("11 acabamento visual fora do vocabulario", m11),
    ("12 o rendimento incoerente escrito de volta", m12),
    ("13 matriz base x ambiente preenchida num verniz", m13),
    ("14 fonte da frase apontando para chave inexistente", m14),
]


def roda(sem_portao_novo=False):
    env = dict(os.environ)
    if sem_portao_novo:
        env["CDM_SEM_PORTAO_ACABAMENTO"] = "1"
    r = subprocess.run([sys.executable, VALIDAR_BANCO], capture_output=True,
                       text=True, cwd=ILHA, env=env)
    return r.returncode != 0


def main():
    original = json.load(open(BANCO, encoding="utf-8"))

    if roda():
        print("FALHA: o banco ja esta reprovado ANTES de qualquer mutacao")
        return 1
    if roda(sem_portao_novo=True):
        print("FALHA: o banco ja esta reprovado com o portao de acabamento desligado")
        return 1

    print("Mutacoes da categoria ACABAMENTO — %d escritas" % len(MUTACOES))
    print("")
    reprovadas = 0
    so_o_portao_novo = 0
    for nome, funcao in MUTACOES:
        mutado = copy.deepcopy(original)
        funcao(mutado)
        if mutado == original:
            print("  INERTE  %s — a mutacao nao mudou nada" % nome)
            continue
        backup = BANCO + ".original"
        shutil.copy2(BANCO, backup)
        try:
            with open(BANCO, "w", encoding="utf-8") as fh:
                json.dump(mutado, fh, ensure_ascii=False, indent=2)
            pegou = roda()
            pegou_sem = roda(sem_portao_novo=True)
        finally:
            shutil.move(backup, BANCO)

        if pegou:
            reprovadas += 1
            if not pegou_sem:
                so_o_portao_novo += 1
                print("  REPROVOU  %-52s (so o portao novo viu)" % nome)
            else:
                print("  REPROVOU  %-52s (o esquema ja pegava)" % nome)
        else:
            print("  PASSOU    %-52s  <-- NENHUM PORTAO VIU" % nome)

    print("")
    print("  reprovadas ..................... %d de %d" % (reprovadas, len(MUTACOES)))
    print("  so o portao novo viu ........... %d" % so_o_portao_novo)
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
