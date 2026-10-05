#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MUTACOES DA FORMA DA URL CONTRA O DEGRAU DECLARADO — 05/10/2026.

O portao que esta bateria mede nasceu do item 2 do despacho da ronda diaria
tecnica de 05/10/2026, e o buraco que ele fecha e o terceiro da mesma familia:

  28/09 — o degrau tem de estar ESCRITO (mutacoes-degrau.py);
  30/09 — o degrau 4 tem de dizer POR QUE parou ali (mutacoes-motivo-degrau-4.py);
  05/10 — o degrau escrito tem de DESCREVER o link que esta ao lado dele.

Os dois primeiros olham o campo. Nenhum dos tres primeiros dias olhou se o
numero gravado corresponde a URL, e foi por esse buraco que
`quartzolit-rejunte-acrilico` passou dez dias com `degrau: 2` carregando
`shopee.com.br/product/1462074750/58262414865` — anuncio de vendedor, que a 25.1
poe no degrau 3. A ronda achou, e achou junto a metade mais silenciosa: a MESMA
loja (`shop_id` 1462074750) estava classificada degrau 3 no
`quartzolit-borracha-liquida-elastica`, com o nome dela escrito no campo. O banco
sabia a resposta num registro e dizia outra coisa no outro.

POR QUE NAO E COSMETICO, na formulacao da propria 25.1: o degrau existe para
gravar QUANTO AQUELE LINK DURA, e a 25.2-b ordena a vitrine por degrau. Anuncio
de vendedor rotulado como catalogo e link pereciveel vestido de duravel — ele
sobe na vitrine por uma durabilidade que nao tem, e a contagem por degrau, que e
o que a leitura semanal le para achar o que pode subir, mente exatamente na casa
que mede durabilidade.

AS TRES REGRAS HERDADAS das baterias irmas desta ilha, e as tres mordem aqui:

  (a) Mutacao que o portao ANTIGO ja pegava nao justifica portao novo. Cada
      mutacao roda o `validar-banco.py` duas vezes e separa o que SO o portao
      novo viu, desligando-o com CDM_SEM_PORTAO_FORMA_DO_DEGRAU=1.

  (b) A mutacao mais valiosa e a que PRODUZ O MUNDO que o banco ainda nao tem.
      A m03 e a m05 sao essas: hoje nenhum registro usa a forma `-i.<shop>.<item>`
      da Shopee num degrau de catalogo, e nenhuma loja tem duas classificacoes
      (o conserto de hoje tirou a unica). As duas fabricam esses estados, porque
      portao que so funciona no banco de hoje mede o acaso e nao a regra.

  (c) ESTA BATERIA TAMBEM MEDE O FALSO POSITIVO, e isso e novo entre as irmas.
      Portao que reprova o link CERTO e desligado pela primeira pessoa com
      pressa, e aí ele deixa de medir qualquer coisa. A m00 nao e mutacao: e a
      afirmacao de que as duas formas legitimas da pagina de catalogo do Mercado
      Livre — com rotulo no caminho e na forma curta sem rotulo — continuam
      passando. Uma regua que exigisse o rotulo reprovaria catalogo de verdade.

Uso:  python3 ferramentas/mutacoes-forma-do-degrau.py
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

def m01(b):
    """O DEFEITO EXATO DE 05/10, escrito de volta noutro registro: um degrau 2
    passa a carregar ficha de ANUNCIO de vendedor da Shopee, na forma canonica
    `/product/<shop_id>/<item_id>`. O rejunte epoxi e o alvo porque ele e um
    degrau 2 legitimo hoje — a mutacao troca so a URL e deixa o numero onde
    estava, que e como o defeito original nasceu."""
    af(b, "quartzolit-rejunte-epoxi")["url_produto"] = \
        "https://shopee.com.br/product/1462074750/58262414865"


def m02(b):
    """A FORMA QUE A 25.1 NOMEIA COM TODAS AS LETRAS e que nenhum portao lia:
    `produto.mercadolivre.com.br/MLB-...-_JM` num degrau 2. A 25.1 escreve
    "nunca use (...) quando existir a /p/ — aquela e anuncio de vendedor e
    apodrece igual a Shopee". E a mutacao mais tentadora do arquivo porque o
    dominio e o certo: so o caminho e que diz que e anuncio."""
    af(b, "quartzolit-cimentcola-externo-acii")["url_produto"] = \
        "https://produto.mercadolivre.com.br/MLB-27315078-argamassa-externa-quartzolit-ac-ii-_JM"


def m03(b):
    """PRODUZ O MUNDO: a OUTRA forma em que a Shopee escreve o par (shop, item),
    a de rotulo `...-i.<shop>.<item>`, num degrau 2. O banco usa as duas formas
    (os rejuntes de ceramica usam esta), mas nenhuma delas esta hoje num degrau
    de catalogo. Um portao que lesse so `/product/` aprovaria metade dos
    registros do banco sem dizer que estava olhando metade."""
    af(b, "loctite-durepoxi")["url_produto"] = \
        "https://shopee.com.br/Rejunte-Acrilico-Quartzolit-i.413687078.14557694103"


def m04(b):
    """O degrau 3 perde a `url_busca`. A 25.1 escreve o requisito DENTRO do
    proprio degrau — "quem usa este degrau tem de ter url_busca preenchida" —
    porque foi o degrau que quebrou quatro links em doze horas em 13/09/2026.
    Sem busca, o leitor que cai num anuncio morto cai num beco."""
    a = af(b, "quartzolit-rejunte-ceramicas")
    a["url_busca"] = ""
    a["motivo_sem_url_busca"] = "mutacao: a API respondeu erro"


def m05(b):
    """PRODUZ O MUNDO, e e a metade que a forma da URL nao pega: a mesma loja da
    Shopee em DOIS degraus. O `rejunte-acrilico` sobe para o degrau 1 (loja
    oficial do fabricante) e a `borracha-liquida-elastica`, que e da MESMA
    `shop_id` 1462074750, continua no 3 com o nome "Edu Tintas Ltda" escrito no
    campo. Nenhuma das duas URLs fica mal formada, nenhum degrau sai da escada, e
    e por isso que so o portao da loja ve: ser loja oficial do fabricante e
    propriedade da LOJA, nao do produto."""
    af(b, "quartzolit-rejunte-acrilico")["degrau"] = 1


MUTACOES = [
    ("m01 degrau 2 com ficha de anuncio da Shopee",      "rejuntes",   m01),
    ("m02 degrau 2 com o /MLB-..._JM que a 25.1 proibe", "colas",      m02),
    ("m03 PRODUZ: degrau 2 com a forma -i.<shop>.<item>", "colas",     m03),
    ("m04 degrau 3 sem url_busca, o beco sem saida",     "rejuntes",   m04),
    ("m05 PRODUZ: a mesma loja em dois degraus",         "rejuntes",   m05),
]


# ----------------------------------------- a trava do falso positivo (regra c)
#
# As duas formas LEGITIMAS da pagina de catalogo do Mercado Livre. Nao sao
# mutacoes: as duas tem de PASSAR. A primeira e a que os quatro degraus 2 do
# banco usam; a segunda e a forma curta que o proprio site devolve ao
# compartilhar, e e ela que uma regua exigindo o rotulo no caminho reprovaria.
CATALOGOS_LEGITIMOS = [
    ("com rotulo no caminho",
     "https://www.mercadolivre.com.br/rejunte-epoxi-quartzolit-1kg-cinza-platina/p/MLB25541512"),
    ("na forma curta, sem rotulo",
     "https://www.mercadolivre.com.br/p/MLB25541512"),
]


def troca_url_do_epoxi(url):
    def muta(b):
        af(b, "quartzolit-rejunte-epoxi")["url_produto"] = url
    return muta


def roda(sem_portao_novo=False):
    env = dict(os.environ)
    if sem_portao_novo:
        env["CDM_SEM_PORTAO_FORMA_DO_DEGRAU"] = "1"
    r = subprocess.run([sys.executable, VALIDAR_BANCO], capture_output=True,
                       text=True, cwd=ILHA, env=env)
    return r.returncode != 0


def escreve_e_roda(arquivo, mutado, sem_portao_novo=False):
    backup = arquivo + ".original"
    shutil.copy2(arquivo, backup)
    try:
        with open(arquivo, "w", encoding="utf-8") as fh:
            json.dump(mutado, fh, ensure_ascii=False, indent=2)
        return roda(sem_portao_novo=sem_portao_novo)
    finally:
        shutil.move(backup, arquivo)


def main():
    originais = {k: json.load(open(v, encoding="utf-8")) for k, v in BANCOS.items()}

    if roda():
        print("FALHA: o banco ja esta reprovado ANTES de qualquer mutacao")
        return 1
    if roda(sem_portao_novo=True):
        print("FALHA: o banco ja esta reprovado com o portao da forma desligado")
        return 1

    print("Mutacoes da FORMA DA URL contra o degrau — %d escritas" % len(MUTACOES))
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
        pegou = escreve_e_roda(arquivo, mutado)
        pegou_sem = escreve_e_roda(arquivo, mutado, sem_portao_novo=True)

        if pegou:
            reprovadas += 1
            if not pegou_sem:
                so_o_portao_novo += 1
                print("  REPROVOU  %-52s (so o portao novo viu)" % nome)
            else:
                print("  REPROVOU  %-52s (o portao antigo ja pegava)" % nome)
        else:
            print("  PASSOU    %-52s  <-- NENHUM PORTAO VIU" % nome)

    print("")
    print("  A TRAVA DO FALSO POSITIVO — catalogo de verdade tem de PASSAR:")
    falsos_positivos = 0
    for rotulo, url in CATALOGOS_LEGITIMOS:
        mutado = copy.deepcopy(originais["rejuntes"])
        troca_url_do_epoxi(url)(mutado)
        if escreve_e_roda(BANCOS["rejuntes"], mutado):
            falsos_positivos += 1
            print("    FALSO POSITIVO  %-44s  <-- o portao reprovou catalogo legitimo" % rotulo)
        else:
            print("    passou          %s" % rotulo)

    print("")
    print("  reprovadas ..................... %d de %d" % (reprovadas, len(MUTACOES)))
    print("  so o portao novo viu ........... %d" % so_o_portao_novo)
    print("  falso positivo ................. %d  (tem de ser 0)" % falsos_positivos)
    if reprovadas != len(MUTACOES):
        print("\nREPROVADO: mutacao que passa e buraco de portao.")
        return 1
    if so_o_portao_novo == 0:
        print("\nREPROVADO: se o portao antigo pega tudo, o novo nao se justifica.")
        return 1
    if falsos_positivos:
        print("\nREPROVADO: portao que reprova o link certo e desligado pela primeira "
              "pessoa com pressa.")
        return 1
    print("\nOK: as %d mutacoes reprovaram, %d delas so pelo portao novo, e as %d formas "
          "legitimas de catalogo passaram."
          % (len(MUTACOES), so_o_portao_novo, len(CATALOGOS_LEGITIMOS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
