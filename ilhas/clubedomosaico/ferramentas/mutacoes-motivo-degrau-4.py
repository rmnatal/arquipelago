#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MUTACOES DO MOTIVO DO DEGRAU 4 — 30/09/2026.

O portao que esta bateria mede nasceu no mesmo bloco que ela, e nasceu de um
buraco que o portao anterior nao podia ver. O de 28/09 cobra que
`afiliado.degrau` esteja ESCRITO — e passou a valer para quem serve busca, nao
so para quem serve ficha. **Ele nao ve o degrau 4 que nao diz por que parou
ali.** Medido pela ronda diaria tecnica de 30/09/2026 no `main` daquele dia: dos
17 registros no degrau 4, **cinco escreviam o motivo e doze traziam so
`motivo_da_chave`** — texto como `"familia: medida"`, que conta como a chave foi
MONTADA e nao o que a escada de palavra-chave devolveu. Os dois estados eram a
mesma tela e ninguem os distinguia.

Nao e zelo de arquivo, e a 25.4-b.4 diz por que: "nao casou" tem causas que
PARECEM uma. Produto que ninguem anuncia sob aquele nome so se resolve quando o
mercado mudar — ou, nas pastilhas, quando o Raphael decidir o casamento por
atributo. Candidato barrado por trava se resolve com trava melhor ou com um
registro de variante que falta, e isso e divida nossa. **Contadas juntas, viram
um numero que nao diz o que fazer, e o pedido a ele desaparece dentro de uma
divida tecnica que nao e dele.**

AS TRES REGRAS HERDADAS das baterias anteriores desta ilha, e as tres mordem aqui:

  (a) Mutacao que o portao ANTIGO ja pegava nao justifica portao novo. Cada
      mutacao roda o `validar-banco.py` duas vezes e separa o que so o portao
      novo viu, desligando-o com CDM_SEM_PORTAO_MOTIVO_DEGRAU_4=1.

  (b) A mutacao mais valiosa e a que PRODUZ O MUNDO que o banco ainda nao tem. A
      m07 e a m08 sao essas: hoje nenhum registro serve ficha de produto sem
      `url`, e nenhum caiu do degrau 3 de volta para o 4. As duas fabricam esses
      estados, porque portao que so funciona no banco de hoje mede o acaso.

  (c) A regua cobra a FORMA, nunca o texto de hoje. Nenhuma mutacao daqui depende
      de o banco ter 38 itens, nem de a reparticao por causa ser
      13 marca-nao-anunciada / 2 nome / 2 variante — sao os numeros de 30/09/2026
      e o proximo bloco que gerar link os muda.

Uso:  python3 ferramentas/mutacoes-motivo-degrau-4.py
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

# Uma causa e uma tentativa bem formadas, para as mutacoes poderem estragar UMA
# metade por vez. Estragar as duas de uma vez nao mede qual delas o portao le.
CAUSA_OK = "CAUSA (marca-nao-anunciada): nenhuma oferta da escada traz a marca"
TENTATIVA_OK = ('ULTIMA TENTATIVA 2026-09-30: 1 "Glass Mosaic K2501" -> 0 ofertas')


def item(banco, ident):
    for m in banco["materiais"]:
        if m["id"] == ident:
            return m
    raise SystemExit("mutacao aponta para item inexistente: %s" % ident)


def af(banco, ident):
    return item(banco, ident)["afiliado"]


def recontar_esperando(banco):
    """O cabecalho declara quantos itens esperam link, e outro portao o confere.

    As mutacoes m08 e m09 derrubam um item do degrau 3 para o 4, o que muda esse
    numero — e sem recontar era o portao do CABECALHO que as pegava, nao o do
    motivo. Mutacao pega pelo portao errado nao prova o portao novo: e por isso
    que esta funcao existe, e nao para deixar a mutacao mais bonita. Um bloco de
    verdade tambem recontaria, porque e o que `coletar-shopee.py` faz ao gravar.
    """
    esperando = sum(1 for m in banco["materiais"]
                    if not ((m.get("afiliado") or {}).get("url")))
    banco.setdefault("afiliado", {})["itens_esperando_link"] = esperando


# --------------------------------------------------------------- as mutacoes

def m01(b):
    """O DEFEITO EXATO que a ronda mediu em 30/09: item no degrau 4 com
    `motivo_da_chave` e sem motivo nenhum da escada. Este era o estado de doze
    dos dezessete, e nenhum portao o via."""
    a = af(b, "glassmosaic-k2501")
    a.pop("motivo_sem_ficha", None)
    a["motivo_da_chave"] = "familia: linha + medida"


def m02(b):
    """O mesmo defeito em outro banco, porque o buraco era do PORTAO e nao do
    arquivo: o de acabamento, que era um dos cinco que escreviam o motivo."""
    af(b, "quartzolit-protetor-para-fachadas").pop("motivo_sem_ficha", None)


def m03(b):
    """A FORMA DE 29/09: prosa de uma metade so, sem o marcador. Ela era honesta
    e passava — e e exatamente o que a 25.4-b.3 proibe, porque sem separar a
    causa da tentativa a passada seguinte reescreve a prosa inteira e apaga a
    causa, ou a deixa crescer sem fim."""
    af(b, "cascola-pl500-adesivo-de-montagem")["motivo_sem_ficha"] = (
        "nenhum anuncio identificou este registro sozinho na escada de "
        'palavra-chave de 2026-09-29: 1 "Cascola PL500" -> 12 ofertas')


def m04(b):
    """Marcador no lugar e a causa sem a palavra CAUSA nem a classe. O campo
    parece na forma e a reparticao por causa fica cega: sem a classe, o portao
    conta "tem motivo" e ninguem sabe se e pedido ao Raphael ou divida nossa."""
    af(b, "cortag-torques-azulejista-corte-curvo")["motivo_sem_ficha"] = (
        "os anuncios sao de corte reto || " + TENTATIVA_OK)


def m05(b):
    """A classe escrita em PROSA, com maiuscula e espaco. `CAUSA (Marca Nao
    Anunciada)` parece a mesma coisa para o olho e nao e a mesma chave para a
    contagem: duas grafias da mesma causa viram duas causas, e a reparticao passa
    a somar errado sem nunca reprovar."""
    af(b, "quartzolit-fundo-selador")["motivo_sem_ficha"] = (
        "CAUSA (Marca Nao Anunciada): a marca nao aparece || " + TENTATIVA_OK)


def m06(b):
    """A tentativa SEM DATA. E a mutacao que mais importa, porque e a que a
    25.4-b.3 nomeia: motivo sem data envelhece calado e manda a execucao seguinte
    nem tentar. "hoje" e a palavra mais perigosa que um campo pode guardar."""
    af(b, "glassmosaic-a11")["motivo_sem_ficha"] = (
        CAUSA_OK + " || ULTIMA TENTATIVA hoje: a escada devolveu zero")


def m07(b):
    """A data em formato BRASILEIRO. `30/09/2026` e legivel e nao e ordenavel:
    duas passadas com formatos diferentes nao se comparam, e a pergunta "qual
    motivo esta mais velho?" deixa de ter resposta por maquina."""
    af(b, "glassmosaic-k77")["motivo_sem_ficha"] = (
        CAUSA_OK + " || ULTIMA TENTATIVA 30/09/2026: a escada devolveu zero")


def m08(b):
    """PRODUZ O MUNDO que o banco nao tem: um registro que ACHOU a ficha de
    produto e nao conseguiu encurtar o link — `url_produto` cheio, `url` vazio,
    degrau 4 — e que escreve o motivo na forma velha. E um caminho real do
    `coletar-shopee.py` ("CASOU E NAO ENCURTOU") que hoje nao existe no banco. Se
    o portao so funciona enquanto todo degrau 4 for busca pura, ele mede o
    formato de hoje e nao a regra."""
    a = af(b, "quartzolit-rejunte-acrilico")
    a["url"] = ""
    a["url_produto"] = "https://shopee.com.br/product/000/111"
    a["degrau"] = 4
    a.pop("casamento", None)
    a["motivo_sem_ficha"] = "a API recusou encurtar o link"
    recontar_esperando(b)


def m09(b):
    """PRODUZ O MUNDO, o outro lado: um item CAI do degrau 3 de volta para o 4 —
    o anuncio saiu do ar e a passada seguinte devolve o registro para a busca.
    Ninguem previu esse caminho porque o banco so subiu degrau ate hoje, e o
    campo de motivo e justamente o que tem de nascer nessa queda."""
    a = af(b, "acrilex-verniz-acrilico-brilhante")
    a["url"] = ""
    a["url_produto"] = None
    a["degrau"] = 4
    a.pop("casamento", None)
    a.pop("motivo_sem_ficha", None)
    recontar_esperando(b)


def m10(b):
    """A causa VAZIA dentro da forma certa. `CAUSA (marca-nao-anunciada):` sem
    nada depois passa em qualquer portao que so procure o marcador — e um campo
    que parece preenchido e nao diz nada e pior que o campo ausente, porque o
    ausente ainda aparece numa contagem."""
    af(b, "glassmosaic-a61")["motivo_sem_ficha"] = (
        "CAUSA (marca-nao-anunciada): || " + TENTATIVA_OK)


MUTACOES = [
    ("m01 o defeito de 30/09: degrau 4 calado",        "pastilhas",  m01),
    ("m02 o mesmo defeito em outro banco",             "acabamento", m02),
    ("m03 a forma de 29/09, de uma metade so",         "colas",      m03),
    ("m04 marcador certo, causa sem classe",           "alicates",   m04),
    ("m05 classe em prosa, com maiuscula e espaco",    "acabamento", m05),
    ("m06 tentativa SEM data — o motivo que envelhece", "pastilhas",  m06),
    ("m07 data em formato brasileiro, nao ordenavel",  "pastilhas",  m07),
    ("m08 PRODUZ: ficha achada e link nao encurtado",  "rejuntes",   m08),
    ("m09 PRODUZ: item CAI do degrau 3 para o 4",      "acabamento", m09),
    ("m10 causa vazia dentro da forma certa",          "pastilhas",  m10),
]


def roda(sem_portao_novo=False):
    env = dict(os.environ)
    if sem_portao_novo:
        env["CDM_SEM_PORTAO_MOTIVO_DEGRAU_4"] = "1"
    r = subprocess.run([sys.executable, VALIDAR_BANCO], capture_output=True,
                       text=True, cwd=ILHA, env=env)
    return r.returncode != 0


def main():
    originais = {k: json.load(open(v, encoding="utf-8")) for k, v in BANCOS.items()}

    if roda():
        print("FALHA: o banco ja esta reprovado ANTES de qualquer mutacao")
        return 1
    if roda(sem_portao_novo=True):
        print("FALHA: o banco ja esta reprovado com o portao do motivo desligado")
        return 1

    print("Mutacoes do MOTIVO DO DEGRAU 4 (25.4-b.3 e 25.4-b.4) — %d escritas, "
          "nos cinco bancos" % len(MUTACOES))
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
                fh.write("\n")
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
                print("  REPROVOU  %-50s (outro portao ja pegava)" % nome)
        else:
            print("  PASSOU    %-50s  <-- NENHUM PORTAO VIU" % nome)

    print("")
    print("  reprovadas ..................... %d de %d" % (reprovadas, len(MUTACOES)))
    print("  so o portao novo viu ........... %d" % so_o_portao_novo)
    if reprovadas != len(MUTACOES):
        print("\nREPROVADO: mutacao que passa e buraco de portao.")
        return 1
    if so_o_portao_novo == 0:
        print("\nREPROVADO: se os portoes antigos pegam tudo, o novo nao se justifica.")
        return 1
    print("\nOK: as %d mutacoes reprovaram, %d delas so pelo portao novo."
          % (len(MUTACOES), so_o_portao_novo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
