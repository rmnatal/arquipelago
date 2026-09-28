#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MUTACOES DO DEGRAU DA ESCADA DA 25.1 — 28/09/2026.

O portao que esta bateria mede nasceu no mesmo bloco que ela, e nasceu porque o
anterior tinha um buraco que ninguem via da tela: ele cobrava `afiliado.degrau`
so de quem tinha `afiliado.url` — a ficha de produto — e o esquema dizia o mesmo
em `obrigatorio_quando: "url estiver preenchida"`. Item que serve BUSCA nao tem
`url`. Resultado medido pela ronda da Sentinela em 28/09/2026: **13 dos 38 itens
do banco** serviam degrau 4 na tela com `degrau: null` no arquivo — os 7 de
acabamento e os 6 de alicate, todos com a busca encurtada gerada em 25/09.

Nao era cosmetico, e o motivo esta na propria 25.1: `degrau` e o campo pelo qual
a leitura semanal acha o que pode SUBIR de degrau. Treze itens em `null` eram
treze oportunidades que ninguem conseguia contar — e um banco em que a pergunta
"o que da para melhorar?" devolvia a resposta errada em silencio.

TRES REGRAS HERDADAS das baterias anteriores desta ilha, e as tres mordem aqui:

  (a) Mutacao que o portao ANTIGO ja pegava nao justifica portao novo. Cada
      mutacao roda o `validar-banco.py` duas vezes e separa o que so o portao
      novo viu, desligando-o com CDM_SEM_PORTAO_DEGRAU=1 — que restaura
      exatamente a regra velha (`url` e so `url`).

  (b) A mutacao mais valiosa e a que PRODUZ O MUNDO que o banco ainda nao tem. A
      m07 e a m08 sao essas: hoje os 13 recem-gravados estao todos no degrau 4 e
      nenhum item do banco serve ficha SEM `url`; as duas fabricam esses estados
      para medir se o portao continua coerente quando o banco mudar de forma.

  (c) A regua cobra a REGRA, nunca o numero de hoje. Nenhuma mutacao daqui
      depende de o banco ter 38 itens nem de a contagem por degrau ser
      1:1 2:5 3:4 4:28 — sao os numeros de 28/09/2026 e eles mudam no proximo
      bloco que gerar link.

Uso:  python3 ferramentas/mutacoes-degrau.py
"""

import copy
import json
import os
import shutil
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)
VALIDAR_BANCO = os.path.join(AQUI, "validar-banco.py")

# A bateria varre os CINCO bancos de material, nao um. O defeito de 28/09 morava
# em dois arquivos e o portao velho era o mesmo para os cinco: bateria de um
# arquivo so teria aprovado o buraco nos outros quatro.
BANCOS = {
    "acabamento": os.path.join(ILHA, "dados", "materiais-acabamento.json"),
    "alicates":   os.path.join(ILHA, "dados", "materiais-alicates.json"),
    "colas":      os.path.join(ILHA, "dados", "materiais-colas.json"),
    "pastilhas":  os.path.join(ILHA, "dados", "materiais-pastilhas.json"),
    "rejuntes":   os.path.join(ILHA, "dados", "materiais-rejuntes.json"),
}


def item(banco, ident):
    for m in banco["materiais"]:
        if m["id"] == ident:
            return m
    raise SystemExit("mutacao aponta para item inexistente: %s" % ident)


def af(banco, ident):
    return item(banco, ident)["afiliado"]


# --------------------------------------------------------------- as mutacoes
#
# Cada uma devolve (arquivo, funcao que escreve o defeito naquele arquivo).

def m01(b):
    """O defeito EXATO que a ronda mediu, escrito de volta num dos sete de
    acabamento: serve busca encurtada e nao diz de que degrau ela veio. Este e o
    unico caso que o portao velho deixava passar em producao, e e o motivo de a
    bateria existir."""
    af(b, "acrilex-verniz-acrilico-brilhante")["degrau"] = None


def m02(b):
    """O mesmo defeito no outro arquivo, porque o buraco era do portao e nao do
    arquivo: um dos seis alicates volta para null."""
    af(b, "vonder-vdec-51")["degrau"] = None


def m03(b):
    """Degrau em branco num item que serve FICHA de produto (`url_produto`) sem
    ter `url`. O portao velho lia `url` e so `url`, entao este estado — link cuja
    saude a 25.4-b manda conferir, sem degrau declarado — passava tambem."""
    a = af(b, "tekbond-silicone-acetico-maxx")
    a["url_produto"] = "https://shopee.com.br/product/000/111"
    a["degrau"] = None


def m04(b):
    """Degrau FORA da escada. Um 5 nao existe na 25.1, e um banco com degrau 5
    faz a leitura semanal procurar um degrau que nao tem para onde subir."""
    af(b, "quartzolit-rejunte-acrilico")["degrau"] = 5


def m05(b):
    """Degrau ZERO — o valor que parece 'nenhum degrau' e e igualmente invalido.
    Escrito separado do m04 de proposito: um portao que compare `> 4` e nao
    `in (1,2,3,4)` pega o 5 e aprova o 0."""
    af(b, "glassmosaic-k2501")["degrau"] = 0


def m06(b):
    """Degrau como TEXTO. `"4"` em JSON e uma string, e em Python toda string
    nao vazia e verdadeira: uma regua escrita com `if af.get("degrau")` aprovaria
    isto, e a contagem por degrau nunca somaria este item em lugar nenhum."""
    af(b, "cortag-torques-mosaico-roldanas")["degrau"] = "4"


def m07(b):
    """PRODUZ O MUNDO que o banco nao tem: um item de acabamento SOBE para o
    degrau 1 (loja oficial do fabricante) e o campo `url` fica vazio junto com o
    degrau. Hoje os sete de acabamento estao todos no 4 e o achado desta bateria
    depende disso; se o portao so funciona enquanto todos estiverem no mesmo
    degrau, ele mede o acaso e nao a regra."""
    a = af(b, "quartzolit-fundo-selador")
    a["degrau"] = None
    a["url_busca"] = "https://s.shopee.com.br/ZZZfundoselador"
    a["url_busca_produto"] = "https://shopee.com.br/search?keyword=quartzolit%20fundo%20selador"


def m08(b):
    """PRODUZ O MUNDO, o outro lado: um item que serve SO a busca CRUA, sem a
    encurtada, e sem degrau. E o estado da 25.2-b (tentado-e-falhou) com a
    declaracao do degrau faltando por cima — dois campos ausentes ao mesmo tempo,
    para medir se o portao do degrau sobrevive ao portao vizinho disparando."""
    a = af(b, "cascola-pl500-adesivo-de-montagem")
    a["degrau"] = None
    a["url_busca"] = ""
    a["motivo_sem_url_busca"] = "mutacao: a API respondeu erro"


MUTACOES = [
    ("m01 acabamento serve busca e nao diz o degrau", "acabamento", m01),
    ("m02 alicate serve busca e nao diz o degrau",    "alicates",   m02),
    ("m03 ficha de produto sem `url` e sem degrau",   "colas",      m03),
    ("m04 degrau 5, fora da escada da 25.1",          "rejuntes",   m04),
    ("m05 degrau 0, o invalido que parece vazio",     "pastilhas",  m05),
    ("m06 degrau como texto, verdadeiro em Python",   "alicates",   m06),
    ("m07 PRODUZ: acabamento sem degrau com par novo", "acabamento", m07),
    ("m08 PRODUZ: so busca crua, sem degrau",         "colas",      m08),
]


def roda(sem_portao_novo=False):
    env = dict(os.environ)
    if sem_portao_novo:
        env["CDM_SEM_PORTAO_DEGRAU"] = "1"
    r = subprocess.run([sys.executable, VALIDAR_BANCO], capture_output=True,
                       text=True, cwd=ILHA, env=env)
    return r.returncode != 0


def main():
    originais = {k: json.load(open(v, encoding="utf-8")) for k, v in BANCOS.items()}

    if roda():
        print("FALHA: o banco ja esta reprovado ANTES de qualquer mutacao")
        return 1
    if roda(sem_portao_novo=True):
        print("FALHA: o banco ja esta reprovado com o portao do degrau desligado")
        return 1

    print("Mutacoes do DEGRAU da escada da 25.1 — %d escritas, nos cinco bancos" % len(MUTACOES))
    print("")
    reprovadas = 0
    so_o_portao_novo = 0
    for nome, qual, funcao in MUTACOES:
        arquivo = BANCOS[qual]
        mutado = copy.deepcopy(originais[qual])
        funcao(mutado)
        if mutado == originais[qual]:
            print("  INERTE  %s — a mutacao nao mudou nada" % nome)
            continue
        backup = arquivo + ".original"
        shutil.copy2(arquivo, backup)
        try:
            with open(arquivo, "w", encoding="utf-8") as fh:
                json.dump(mutado, fh, ensure_ascii=False, indent=2)
            pegou = roda()
            pegou_sem = roda(sem_portao_novo=True)
        finally:
            shutil.move(backup, arquivo)

        if pegou:
            reprovadas += 1
            if not pegou_sem:
                so_o_portao_novo += 1
                print("  REPROVOU  %-50s (so o portao novo viu)" % nome)
            else:
                print("  REPROVOU  %-50s (o portao antigo ja pegava)" % nome)
        else:
            print("  PASSOU    %-50s  <-- NENHUM PORTAO VIU" % nome)

    print("")
    print("  reprovadas ..................... %d de %d" % (reprovadas, len(MUTACOES)))
    print("  so o portao novo viu ........... %d" % so_o_portao_novo)
    if reprovadas != len(MUTACOES):
        print("\nREPROVADO: mutacao que passa e buraco de portao.")
        return 1
    if so_o_portao_novo == 0:
        print("\nREPROVADO: se o portao antigo pega tudo, o novo nao se justifica.")
        return 1
    print("\nOK: as %d mutacoes reprovaram, %d delas so pelo portao novo."
          % (len(MUTACOES), so_o_portao_novo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
