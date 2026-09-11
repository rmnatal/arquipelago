#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testes NEGATIVOS do validador do banco de especies.

Uso (a partir de ilhas/aquametria/):  python3 ferramentas/testar-validador-especies.py

Por que existe: validar-especies.py so prova que o banco de hoje passa. Isso nao prova
que uma regra pega o defeito que ela promete pegar — uma regra escrita errada aprova
tudo em silencio, e o banco parece so. Cada teste aqui corrompe uma copia do banco de
proposito, roda o validador contra a copia e exige que a regra certa reprove. O banco
real nunca e tocado: as copias vao para um diretorio temporario.

Codigo de saida: 0 se todas as regras reprovarem o que deviam, 1 se alguma passar batido.
"""

import copy
import json
import os
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANCO = os.path.join(RAIZ, "dados", "especies-agua-doce.json")
VALIDADOR = os.path.join(RAIZ, "ferramentas", "validar-especies.py")


def pega(banco, rid):
    for r in banco["especies"]:
        if r["id"] == rid:
            return r
    raise KeyError(rid)


# ------------------------------------------------------------------ as corrupcoes
def c_e1(b):
    pega(b, "danio-rerio")["id"] = "peixe-zebra"


def c_e2(b):
    r = pega(b, "danio-rerio")
    r["convivencia"] = None
    r["status_registro"] = "conflito"


def c_e3(b):
    r = pega(b, "corydoras-panda")
    for f in r["fontes"]:
        if "temperatura_C" in f["campos"]:
            f["campos"].remove("temperatura_C")


def c_e4(b):
    pega(b, "betta-splendens")["fontes"][0]["status"] = "verificada-fabricante"


def c_e5(b):
    r = pega(b, "xiphophorus-hellerii")
    for f in r["fontes"]:
        f["origem"] = "varejo"
        f["status"] = "transcrita-varejo"


def c_e6(b):
    pega(b, "astronotus-ocellatus")["porte_medida"] = None


def c_e7(b):
    r = pega(b, "corydoras-panda")
    # base 45 x 30 cm x 30 cm de altura = 40,5 L: litro derivado, gravado a mao
    r["volume_minimo_declarado_L"] = 40.5
    r["fontes"][1]["campos"].append("volume_minimo_declarado_L")


def c_e8(b):
    pega(b, "hemigrammus-erythrozonus")["temperatura_C"] = {"min": 28, "max": 24}


def c_e9(b):
    # conflito de bem-estar cujo conservador nao e o maior
    pega(b, "chromobotia-macracanthus")["conflitos"][0]["valor_conservador"] = 150


def c_e10(b):
    pega(b, "hemigrammus-rhodostomus")["status_registro"] = "completo"


def c_e11(b):
    pega(b, "betta-splendens")["verificado_em"] = "2020-01-01"


def c_e12(b):
    r = pega(b, "astronotus-ocellatus")
    r["cardume_minimo"] = 4  # solitario com cardume preenchido


def c_e13(b):
    r = pega(b, "trichopodus-trichopterus")
    r["temperatura_C"] = {"min": 5, "max": 35}
    r["temperatura_e_tolerancia"] = False


def c_e14(b):
    r = pega(b, "mikrogeophagus-ramirezi")
    r["fontes"] = [r["fontes"][0]]


def c_e15(b):
    # troca o compendio por um espelho do MESMO corpo: duas urls, uma fonte so
    r = pega(b, "corydoras-panda")
    r["fontes"][1]["origem"] = "base-cientifica-via-busca"
    r["fontes"][1]["status"] = "base-cientifica-via-busca"
    r["fontes"][1]["url"] = "https://fishbase.org/summary/12188"


def c_e16_numero(b):
    # o campo passa a dizer um numero que a fonte citada nao diz
    pega(b, "tanichthys-albonubes")["cardume_minimo"] = 12


def c_e16_intervalo(b):
    # um lado do intervalo mexido: a regra tem de olhar min e max separados
    pega(b, "hyphessobrycon-amandae")["temperatura_C"]["max"] = 29


def c_e16_base(b):
    # e dentro do objeto de base tambem, que e onde mora a largura
    pega(b, "hyphessobrycon-amandae")["base_minima_cm"]["largura"] = 35


def c_e16_extenso(b):
    # a fonte da coridora-panda escreve "pelo menos SEIS", por extenso. Trocar o campo
    # para 7 tem de reprovar — e o 6 continuar passando e o que prova que a leitura
    # por extenso e real, e nao um buraco que aprova qualquer numero.
    pega(b, "corydoras-panda")["cardume_minimo"] = 7


TESTES = [
    ("E1", "id que nao corresponde ao nome cientifico", c_e1, "erro"),
    ("E2", "campo obrigatorio faltando sem status parcial", c_e2, "erro"),
    ("E3", "campo tecnico preenchido sem fonte", c_e3, "erro"),
    ("E4", "fonte com status incoerente com a origem", c_e4, "erro"),
    ("E5", "campo de manutencao sustentado so por varejo", c_e5, "erro"),
    ("E6", "porte sem SL ou TL do lado", c_e6, "erro"),
    ("E7", "litro derivado da base gravado a mao", c_e7, "erro"),
    ("E8", "intervalo com min maior que max", c_e8, "erro"),
    ("E9", "conflito de bem-estar com conservador que nao e o maior", c_e9, "erro"),
    ("E10", "conflito declarado com status completo", c_e10, "erro"),
    ("E11", "registro verificado ha mais de 365 dias", c_e11, "aviso"),
    ("E12", "convivencia solitario com cardume_minimo preenchido", c_e12, "erro"),
    ("E13", "tolerancia termica disfarcada de recomendacao", c_e13, "erro"),
    ("E14", "status completo com um corpo de fonte so", c_e14, "erro"),
    ("E15", "duas urls do mesmo corpo passando por duas fontes", c_e15, "aviso"),
    ("E16", "campo com numero que a fonte citada nao diz", c_e16_numero, "erro"),
    ("E16", "um lado do intervalo fora do texto da fonte", c_e16_intervalo, "erro"),
    ("E16", "largura da base fora do texto da fonte", c_e16_base, "erro"),
    ("E16", "numero por extenso na fonte, campo trocado", c_e16_extenso, "erro"),
]


def main():
    original = json.load(open(BANCO, encoding="utf-8"))
    tmp = tempfile.mkdtemp(prefix="aqm-especies-")
    falhas = []

    print("== testes negativos do validador de especies ==")
    for regra, descricao, corromper, esperado in TESTES:
        banco = copy.deepcopy(original)
        corromper(banco)
        caminho = os.path.join(tmp, "banco-%s.json" % regra.lower())
        with open(caminho, "w", encoding="utf-8") as fp:
            json.dump(banco, fp, ensure_ascii=False, indent=2)

        saida = subprocess.run([sys.executable, VALIDADOR, caminho],
                               capture_output=True, text=True)
        marca = "ERRO  [%s]" % regra if esperado == "erro" else "aviso [%s]" % regra
        pegou = marca in saida.stdout
        codigo_certo = (saida.returncode == 1) if esperado == "erro" else True
        ok = pegou and codigo_certo
        print("  %-4s %-56s %s" % (regra, descricao, "pegou" if ok else "PASSOU BATIDO"))
        if not ok:
            falhas.append(regra)

    # o banco real nao pode ter sido tocado por nada disto
    depois = json.load(open(BANCO, encoding="utf-8"))
    if depois != original:
        print("  !! o banco real mudou durante os testes")
        falhas.append("banco-intacto")

    print("\n== resultado ==")
    print("  %d teste(s), %d falha(s)" % (len(TESTES), len(falhas)))
    if falhas:
        print("  regras que nao reprovaram o defeito: %s" % ", ".join(falhas))
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
