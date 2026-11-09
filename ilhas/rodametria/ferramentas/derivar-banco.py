#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Preenche os campos DERIVADOS do banco da Rodametria: `energia_wh` e `afiliado.intestavel`.

    python3 ferramentas/derivar-banco.py            # escreve
    python3 ferramentas/derivar-banco.py --conferir # nao escreve; sai 1 se houver o que escrever

Por que isto e um programa e nao uma coluna digitada: `energia_wh` e IDENTIDADE (Wh = V x Ah,
constante `energia-wh-tensao-vezes-amperagem`), e numero de identidade digitado a mao e numero
que vai divergir da conta um dia, sem ninguem ver. Quem escreve o campo e este arquivo; quem
confere e ferramentas/validar-banco.py, que recalcula e reprova divergencia. Sao duas metades
e elas nao se falam por acaso: a segunda existe para discordar da primeira.

O SEGUNDO DERIVADO NASCEU EM 04/11/2026, pelo item 4 do despacho da ronda daquele
dia: `afiliado.intestavel` estava AUSENTE nos 17 registros de `veiculos.json` e nos
3 de `pecas.json`. A 25.9 (item 2) diz, com todas as letras, que campo declarado em
todo registro existe "pela mesma razao do `intestavel`" — e nesta ilha o `intestavel`
era justamente o que nao estava declarado em lugar nenhum. O validador o RECALCULAVA
de cabeca numa variavel local (`bool(url) and not url_produto`), entao a ronda que
media "0 intestavel" nesta ilha estava medindo a AUSENCIA DA CHAVE, nao a saude dos
itens. Hoje nao esconde nada — os 20 derivam `false` —, e e por isso que entra agora:
campo ausente que se comporta como o valor certo espera o dia em que o valor certo
muda, e nesse dia nenhum portao acusa.

O QUE ELE SIGNIFICA, e e a 25.4-b literal: item com link de ficha (`url`) e sem o par
cru (`url_produto`) e "um link cuja saude e desconhecida e PERMANECERA desconhecida",
porque a 25.4 proibe clicar no proprio link de afiliado para conferir. Item de degrau
4, que nao tem ficha nenhuma e vive do piso de busca, nao e intestavel: nao ha ficha
para testar, e a busca nao esgota.

E POR QUE DUAS DECLARACOES DO MESMO FATO, se a 20.7 avisa que "duas declaracoes do
mesmo fato comecam iguais e so uma sobe": porque aqui elas NAO sao duas declaracoes,
sao um espelho e um portao. Esta ferramenta escreve; `validar-banco.py` RECALCULA e
reprova divergencia — exatamente como ja faz com `energia_wh`. Espelho sem portao
envelhece calado; portao sem espelho obriga toda ronda a refazer a conta de cabeca.

O FATOR NUNCA VEM DAQUI. A relacao sai de dados/constantes.json, pelo id da constante, e o
programa PARA se a constante nao estiver `publicavel` — literal numerico de conversao dentro
deste arquivo seria a mesma doenca que a 1.3 da especificacao proibe na F1.
"""
import json
import sys
from pathlib import Path

ID_CONSTANTE = "energia-wh-tensao-vezes-amperagem"
RAIZ = Path(__file__).resolve().parent.parent


def constante_publicavel():
    const = json.loads((RAIZ / "dados/constantes.json").read_text(encoding="utf-8"))
    for c in const.get("constantes", []):
        if c.get("id") == ID_CONSTANTE:
            return c
    return None


# ---------------------------------------------------------------------------
# O TERCEIRO DERIVADO NASCEU EM 06/11/2026, PELO ITEM 5 DO DESPACHO DA RONDA
# DAQUELE DIA — E ELE NAO E UM CAMPO DE REGISTRO: E UMA FRASE DE METADADO.
#
# O `nota` de `dados/veiculos.json` terminava assim: *"NENHUM registro e
# `publicavel`, e a causa e uma so: nenhum tem saida de compra, e a 25.2 nao
# admite item publicavel sem piso."* A primeira metade continua VERDADEIRA (os 17
# seguem com `publicavel` false); a segunda era FALSA — quatro registros tem
# `afiliado` preenchido, e os quatro aparecem como cartao no ar, com botao que o
# teste de vida da ronda achou VIVO.
#
# NAO QUEBRA PAGINA NENHUMA, e e por isso que e a pior especie de defeito: o
# arquivo e `publicar: false`, entao nada dele vai para a tela. O risco e de
# METODO — a proxima execucao que ler esse `nota` como fato conclui que a ilha nao
# tem monetizacao nenhuma, e ela tem. E a familia que a 20.7 nomeia nesta ilha:
# *"duas declaracoes do mesmo fato comecam iguais e so uma sobe"*.
#
# O DESPACHO DEIXOU A ESCOLHA PARA A FUNDACAO (19.2), entre apagar a frase e fazer
# o gerador reconta-la. ESCOLHI RECONTAR, por um motivo e nao por gosto: apagar
# conserta hoje e nao impede o proximo numero digitado de entrar amanha. Recontado
# pelo gerador, o campo nao pode mais envelhecer — e o `validar-banco.py` recalcula
# e reprova divergencia, que e o par espelho+portao que esta ilha ja usa no
# `energia_wh` e no `intestavel`.
#
# E O DESPACHO ERROU O NUMERO, no mesmo defeito que estava relatando: ele escreveu
# *"CINCO tem"* e nomeou QUATRO, com a quinta linha dizendo "e o quinto por
# `url_busca`" — contado no arquivo, sao QUATRO, e os quatro ja estao entre os
# nomeados. Numero de prosa escrito a mao, dentro do relatorio sobre numero de
# prosa escrito a mao.
# ---------------------------------------------------------------------------
# `publicavel` E VALOR DE `status`, NUNCA CAMPO — E ESPELHO E PORTAO QUE LEEM A
# MESMA CHAVE INEXISTENTE CONCORDAM, O QUE E INDISTINGUIVEL DE CONFERENCIA
# (09/11/2026, item 2 do despacho da ronda de hoje).
#
# O item 2 do despacho diz que a contagem de publicaveis do `nota` "continuou
# escrita a mao". MEDIDO, ela NAO estava: ela era derivada desde 06/11, e era
# derivada de `r.get("publicavel")` — um campo BOOLEANO QUE NAO EXISTE EM
# REGISTRO NENHUM deste banco (0 de 17 o carregam). O banco diz publicavel pelo
# `status`, e `dados/esquema-banco.json` escreve isso com todas as letras:
# *"universo: todo VEICULO com status publicavel"*. A chave booleana foi
# INVENTADA pelas duas metades ao mesmo tempo.
#
# POR QUE SOBREVIVEU TRES DIAS DEBAIXO DO PORTAO QUE NASCEU PARA ISSO: o espelho
# (aqui) e o portao (`validar-banco.py`, linha da contagem) liam a MESMA chave
# ausente, entao os dois contavam ZERO e os dois CONCORDAVAM. A 20.7 desta ilha
# ensina que "duas declaracoes do mesmo fato comecam iguais e so uma sobe"; este
# e o caso em que as duas comecam iguais e as duas ESTAO ERRADAS — e a
# concordancia entre elas tem exatamente a cara da conferencia. Pior: o MESMO
# `validar-banco.py` le o conceito do jeito certo (`status == "publicavel"`) em
# quatro outros lugares, a algumas centenas de linhas de distancia.
#
# A REGRA, E ELA E A LICAO DO ITEM: quem conta publicavel chama ESTA funcao, e
# quem invento o booleano e DENUNCIADO pelo validador. Chave ausente lida por
# duas metades independentes nao e divergencia — e silencio em estereo.
def e_publicavel(r):
    """Publicavel e um VALOR de `status`. Nao existe campo booleano `publicavel`."""
    return r.get("status") == STATUS_PUBLICAVEL


STATUS_PUBLICAVEL = "publicavel"


def contar_saida_de_compra(registros):
    """Conta, no proprio arquivo, quem tem saida de compra e quem e publicavel.

    SAIDA DE COMPRA e qualquer um dos quatro campos de URL do `afiliado`: a ficha
    (`url`), o par cru (`url_produto`) e os dois de busca (`url_busca` e
    `url_busca_produto`). A 25.2 poe o piso em `url_busca`, entao item de degrau 4
    TEM saida de compra mesmo sem ficha — e era justamente isso que a frase velha
    negava.
    """
    campos = ("url", "url_produto", "url_busca", "url_busca_produto")
    com, publicaveis = [], []
    for r in registros:
        af = r.get("afiliado")
        if isinstance(af, dict) and any(af.get(c) for c in campos):
            com.append(r.get("id"))
        if e_publicavel(r):
            publicaveis.append(r.get("id"))

    return com, publicaveis


def frase_da_saida_de_compra(registros):
    """A frase do `nota`, montada da contagem. Nenhum numero daqui e digitado."""
    com, publicaveis = contar_saida_de_compra(registros)
    total = len(registros)
    if publicaveis:
        # OS NOMES ENTRAM NA FRASE pelo mesmo motivo que entram na metade da
        # saida de compra: numero sozinho envelhece sem acusar QUAL registro
        # mudou, e o validador so pode cobrar o que a frase diz. Com os nomes,
        # registro que entra ou sai de `publicavel` reprova a bancada.
        quantos = ("%d dos %d registros estao `publicavel` (%s)"
                   % (len(publicaveis), total, ", ".join(publicaveis))
                   if len(publicaveis) != total
                   else "os %d registros estao `publicavel` (%s)"
                   % (total, ", ".join(publicaveis)))
    else:
        quantos = "NENHUM dos %d registros esta `publicavel`" % total
    if not com:
        saida = ("e nenhum deles tem saida de compra, que e o piso que a 25.2 exige "
                 "de item publicavel")
    elif len(com) == 1:
        saida = ("e 1 deles JA tem saida de compra (%s), entao a falta de piso da "
                 "25.2 nao e mais a causa de todos" % com[0])
    else:
        saida = ("e %d deles JA tem saida de compra (%s), entao a falta de piso da "
                 "25.2 nao e mais a causa de todos" % (len(com), ", ".join(com)))

    return ("%s %s, %s. Numero de prosa digitado a mao envelhece calado, e este "
            "envelheceu uma vez."
            % (MARCA_DA_FRASE, quantos, saida))


# A MARCA ABRE A FRASE E NAO A FECHA, e isto foi medido: com a marca no fim, o
# corte `nota.split(MARCA)[0]` devolvia a frase recontada DENTRO do `base`, e a
# ferramenta reescrevia o campo em toda passada — `--conferir` reprovando para
# sempre, logo depois de escrever. Marca no comeco corta o bloco derivado inteiro.
MARCA_DA_FRASE = ("SAIDA DE COMPRA E PUBLICAVEIS, RECONTADOS POR "
                  "ferramentas/derivar-banco.py e conferidos por "
                  "ferramentas/validar-banco.py:")


def nota_com_a_frase(nota, registros):
    """Troca a ultima afirmacao do `nota` pela frase recontada, preservando o resto."""
    base = nota.split(MARCA_DA_FRASE)[0]
    # A frase VELHA, de 28/10/2026, era a ultima sentenca do campo. Ela sai pela
    # marca quando ja foi trocada uma vez, e pelo texto dela na primeira troca.
    velha = ("NENHUM registro e `publicavel`, e a causa e uma so: nenhum tem saida "
             "de compra, e a 25.2 nao admite item publicavel sem piso.")
    base = base.replace(velha, "").rstrip()
    if base and not base.endswith("."):
        base += "."

    return (base + " " + frase_da_saida_de_compra(registros)).strip()


def main():
    conferir = "--conferir" in sys.argv
    c = constante_publicavel()
    if c is None:
        print("PAROU: a constante `%s` nao existe em dados/constantes.json. Este programa nao "
              "carrega a relacao Wh = V x Ah dentro de si de proposito." % ID_CONSTANTE)
        return 1
    if c.get("status") != "publicavel":
        print("PAROU: a constante `%s` esta em %r. A secao 10 do ARQUIPELAGO.md proibe constante "
              "`pendente` dentro de formula publicada." % (ID_CONSTANTE, c.get("status")))
        return 1

    alvo = RAIZ / "dados/veiculos.json"
    d = json.loads(alvo.read_text(encoding="utf-8"))
    mudou, zerados = [], []
    intestaveis = []
    for v in d.get("registros", []):
        tv = (v.get("tensao_v") or {}).get("valor")
        ah = (v.get("amperagem_ah") or {}).get("valor")
        atual = (v.get("energia_wh") or {}).get("valor")
        if tv is None or ah is None:
            if atual is not None:
                v["energia_wh"] = {
                    "valor": None,
                    "motivo": "nao derivavel: falta tensao_v ou amperagem_ah. Wh copiado de anuncio e "
                              "proibido pelo esquema — o declarado vai para divergencias[].",
                }
                zerados.append(v["id"])
            continue
        novo = round(tv * ah)
        if atual != novo or not (v.get("energia_wh") or {}).get("derivado_de"):
            v["energia_wh"] = {
                "valor": novo,
                "unidade": "Wh",
                "derivado": True,
                "derivado_de": "tensao_v x amperagem_ah",
                "constante": ID_CONSTANTE,
                "conta": "%s V x %s Ah = %s Wh" % (tv, ah, novo),
                "fonte": None,
                "motivo_sem_fonte": "identidade matematica: vale por definicao de unidade e nao depende "
                                    "de fonte. As fontes sao as dos dois lados da conta (tensao_v e "
                                    "amperagem_ah), cada uma com a sua.",
            }
            mudou.append("%s -> %s Wh" % (v["id"], novo))

    # O `nota` DE veiculos.json, com a ultima afirmacao RECONTADA (item 5 do
    # despacho de 06/11/2026). Ver `frase_da_saida_de_compra()` acima.
    nota_atual = d.get("nota") or ""
    nota_nova = nota_com_a_frase(nota_atual, d.get("registros", []))
    nota_mudou = nota_nova != nota_atual
    if nota_mudou:
        d["nota"] = nota_nova

    # `afiliado.intestavel` — nos DOIS bancos que tem a chave `afiliado`.
    bancos = [(alvo, d)]
    pecas_caminho = RAIZ / "dados/pecas.json"
    pecas = json.loads(pecas_caminho.read_text(encoding="utf-8"))
    bancos.append((pecas_caminho, pecas))
    for caminho, banco in bancos:
        for r in banco.get("registros", []):
            af = r.get("afiliado")
            if not isinstance(af, dict):
                continue
            novo = bool(af.get("url")) and not af.get("url_produto")
            if af.get("intestavel") != novo or "intestavel" not in af:
                af["intestavel"] = novo
                intestaveis.append("%s:%s -> %s"
                                   % (caminho.name, r.get("id"), "true" if novo else "false"))
            else:
                af["intestavel"] = novo

    if conferir:
        if mudou or zerados or intestaveis or nota_mudou:
            print("REPROVADO: %d derivado(s) a escrever, %d a zerar, %d `intestavel` a "
                  "espelhar e o `nota` %s."
                  % (len(mudou), len(zerados), len(intestaveis),
                     "A RECONTAR" if nota_mudou else "em dia"))
            if nota_mudou:
                print("  nota:       %s" % frase_da_saida_de_compra(d.get("registros", [])))
            for m in mudou:
                print("  a escrever: %s" % m)
            for z in zerados:
                print("  a zerar:    %s" % z)
            for i in intestaveis:
                print("  intestavel: %s" % i)
            return 1
        print("0 falha(s).")
        print("APROVADO: todo `energia_wh` bate com V x Ah e todo `afiliado.intestavel` bate "
              "com a regra da 25.4-b.")
        return 0

    if mudou or zerados or intestaveis or nota_mudou:
        # A NOVA-LINHA FINAL E PARTE DO ARQUIVO: sem ela, todo commit desta
        # ferramenta carrega um "\ No newline at end of file" que nao e dela.
        alvo.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    # `pecas.json` SO E REESCRITO SE ALGO NELE MUDOU, e isto foi medido em
    # 06/11/2026: a condicao anterior era `any(c.name == "pecas.json" ...)`, que e
    # sempre VERDADEIRA porque o arquivo esta sempre na lista `bancos`. Qualquer
    # escrita em veiculos.json reescrevia pecas.json tambem — e como este programa
    # grava com `indent=1` e aquele arquivo nasceu com `indent=2`, o commit vinha
    # com 186 linhas trocadas e ZERO byte de conteudo diferente. Diff de ruido
    # esconde diff de verdade, e e o mesmo custo da 23.4: so entra no arquivo o
    # que esta passada mudou.
    if any(i.startswith("pecas.json:") for i in intestaveis):
        pecas_caminho.write_text(json.dumps(pecas, ensure_ascii=False, indent=1) + "\n",
                                 encoding="utf-8")
    for m in mudou:
        print("escrito: %s" % m)
    for z in zerados:
        print("zerado:  %s" % z)
    for i in intestaveis:
        print("espelhado: %s" % i)
    if nota_mudou:
        print("recontado: o `nota` de veiculos.json")
    print("%d derivado(s) escrito(s), %d zerado(s), %d `intestavel` espelhado(s), `nota` %s."
          % (len(mudou), len(zerados), len(intestaveis),
             "recontado" if nota_mudou else "em dia"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
