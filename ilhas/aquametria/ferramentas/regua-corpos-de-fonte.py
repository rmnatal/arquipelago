#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A REGUA DE UMA COISA SO: quantos CORPOS de fonte distintos sustentam isto?

Nao e portao e nao afirma nada sozinha. E a regua que QUATRO portoes usam:
`validar-especies.py` e `varrer-categorias-possiveis.py` (que MEDEM o banco),
`gerar-catalogo-especies.py` (que decide quem entra no snippet que o site serve) e
`teste-peixes.py` (que compara o banco com o HTML servido).

POR QUE ELA NASCEU EM 16/10/2026, E A CAUSA FOI MEDIDA E NAO SUPOSTA
--------------------------------------------------------------------
Em 15/10/2026 a regra E26 tirou a contagem de corpos do hostname e a poe em
`corpos_de_fonte` do esquema, com a procedencia declarada corpo por corpo. O
cabecalho daquela mudanca diz, com todas as letras, que a tabela de espelhos estava
"COPIADA A MAO num segundo arquivo" e que "agora a regua e uma so".

NAO ERA UMA SO. Ela era QUATRO, e so DUAS foram consertadas naquele dia — as duas que
MEDEM. As duas que DECIDEM O QUE VAI A TELA continuaram contando corpo pelo PREFIXO DA
REFERENCIA, cegas a procedencia:

    validar-especies.py          le `corpos_de_fonte`   (consertada em 15/10)
    varrer-categorias-possiveis  le `corpos_de_fonte`   (consertada em 15/10, segunda copia a mao)
    gerar-catalogo-especies.py   nome_do_corpo(referencia)   <- CEGA
    teste-peixes.py              corpo_da_referencia(ref)    <- CEGA

O BURACO, MEDIDO EM 16/10/2026 NO BANCO REAL, nos dois mundos que o esquema permite e
o banco ainda nao tem. Acrescentando ao `poecilia-reticulata` uma fonte do `usgs-nas`
— que esta declarado no esquema como `indeterminada`, porque foi OFERECIDO E RECUSADO
em 15/10 para este mesmo registro:

    validador    1 corpo  (fishbase)                 -> BARRA
    gerador      2 corpos (FishBase, USGS NAS)       -> PUBLICA
    teste-peixes 2 corpos (FishBase, USGS NAS)       -> PUBLICA

E com um corpo declarado `reproduz: fishbase` noutro host, o resultado e o mesmo: o
validador colapsa e barra, os outros dois contam dois e publicam. **O validador barra o
guppy e o gerador o poe na tela com UM corpo real** — e o `teste-peixes.py`, que e o
unico portao que compara banco com HTML servido, CONCORDA COM O GERADOR e por isso
nunca acusaria. O dissenso ficaria so na saida informativa do `minimo_para_sugerir`,
que nao tem codigo de erro.

Dito de outro modo: a recusa do usgs-nas de 15/10 vive HOJE so como prosa no esquema.
Se a execucao seguinte reoferecesse a mesma fonte e a gravasse, nada no caminho da
pagina a barraria. A regra E26 existia e nao alcancava o portao que importa.

POR QUE LER O ESQUEMA AQUI NAO E O ERRO QUE A DECISAO 1 DO GERADOR PROIBE
-------------------------------------------------------------------------
O cabecalho de `gerar-catalogo-especies.py` manda a LISTA DE CAMPOS do portao ser
escrita no proprio script e so CONFERIDA contra o esquema, "senao apagar um campo la
faria as duas metades errarem juntas". Isso continua valendo e nao muda: a lista de
campos e uma DECISAO, e decisao o portao declara por conta propria.

O registro de corpos nao e decisao: e FATO EXTERNO — quais hosts sao a FishBase, de
onde vem o numero de cada corpo. A distincao ja estava escrita nesta pasta antes deste
arquivo, no comentario de `varrer-categorias-possiveis.py`, e e ela que autoriza esta
regua a ser uma so. Fato externo copiado a mao em quatro lugares foi exatamente o que
produziu o buraco acima.

O VOCABULARIO DE PROCEDENCIA, e cada termo decide a contagem de um jeito diferente:
`propria` conta como si; `reproduz` COLAPSA no corpo que ela reproduz, entao duas urls
de hosts diferentes continuam sendo um corpo so; `indeterminada` NAO conta como corpo
nenhum, porque fonte que nao diz de onde veio o numero dela nao e o proprio corpo (nao
se sabe se e dele) nem o de outro (nao se sabe de quem e).
"""
import json
from urllib.parse import urlparse

# host sem "www." -> registro do corpo, lido de `corpos_de_fonte` do esquema.
# Vazio ate alguem chamar carregar(): regua que adivinha corpo e a regua que esta
# sendo aposentada aqui.
CORPOS_DECLARADOS = {}

# O vocabulario mora no esquema; esta tupla e a copia que a regra E26 CONFERE contra
# ele, nunca a definicao. Divergencia entre as duas reprova em vez de passar calada.
PROCEDENCIAS = ("propria", "reproduz", "indeterminada")


def carregar(esquema):
    """Indexa `corpos_de_fonte` do esquema por host. Chamada uma vez, pelo consumidor.

    Recebe o esquema JA CARREGADO de proposito: quem le o arquivo e quem o valida, e
    esta regua nao escolhe caminho de arquivo por ninguem.
    """
    CORPOS_DECLARADOS.clear()
    for corpo in esquema["corpos_de_fonte"]["corpos"]:
        for host in corpo["hosts"]:
            CORPOS_DECLARADOS[host.lower()] = corpo
    return CORPOS_DECLARADOS


def carregar_do_arquivo(caminho):
    """Conveniencia para quem so tem o caminho do esquema na mao."""
    with open(caminho, encoding="utf-8") as f:
        return carregar(json.load(f))


def host_da_fonte(url):
    """O host de uma url, em minusculas e sem o 'www.'.

    O 'www.' sai porque www.fishbase.se e fishbase.se sao o mesmo host, e foi por uma
    das duas copias a mao tirar o prefixo e a outra listar as variantes com ele que as
    duas deixaram de ter a mesma forma (medido em 15/10/2026).
    """
    host = (urlparse(url or "").netloc or "").lower()
    return host[4:] if host.startswith("www.") else host


def corpo_declarado(url):
    """O registro do corpo desta url, ou None se o corpo NAO esta declarado.

    None nao e "corpo desconhecido que conta por si": e falta de declaracao, e quem
    chama tem de reprovar (E26). Era por aqui que o corpo novo entrava calado.
    """
    return CORPOS_DECLARADOS.get(host_da_fonte(url))


def corpo_contavel(url):
    """O nome com que esta url CONTA na contagem de corpos distintos, ou None.

    Quem decide e a PROCEDENCIA declarada, nunca o host e nunca o texto da
    referencia. Devolver None significa "nao conta como corpo nenhum", e os dois
    caminhos que levam a isso sao diferentes: corpo nao declarado (erro de quem
    gravou) e corpo `indeterminada` (fonte que nao diz de onde veio o numero dela).
    Quem precisa separar os dois chama `corpo_declarado()`.
    """
    corpo = corpo_declarado(url)
    if corpo is None:
        return None
    if corpo["procedencia"] == "reproduz":
        return corpo.get("reproduz")
    if corpo["procedencia"] == "indeterminada":
        return None
    return corpo["nome"]


def corpos_de(registro):
    """Os corpos distintos que o REGISTRO cita. E a contagem do E14 e do E15."""
    nomes = {corpo_contavel(f.get("url")) for f in (registro.get("fontes") or []) if f.get("url")}
    nomes.discard(None)
    return nomes


def corpos_por_campo(registro):
    """Campo -> conjunto de corpos CONTAVEIS que o sustentam. E a contagem do E27.

    `corpos_de()` responde quantos corpos o registro CITA; este responde quantos
    sustentam CADA CAMPO, e e a segunda que decide se o numero publicado foi
    conferido: um registro pode citar dois corpos e ter todo o nucleo obrigatorio
    apoiado em um so, porque o segundo sustenta campo OPCIONAL.

    O campo aparece na chave mesmo quando nenhum corpo o sustenta (conjunto vazio):
    apagar a chave faria "campo sem corpo" e "campo que ninguem cita" virarem a mesma
    coisa, e so o primeiro e defeito.
    """
    por_campo = {}
    for f in (registro.get("fontes") or []):
        nome = corpo_contavel(f.get("url"))
        for campo in (f.get("campos") or []):
            por_campo.setdefault(campo, set())
            if nome:
                por_campo[campo].add(nome)
    return por_campo


def urls_sem_corpo_declarado(registro):
    """As urls de fonte deste registro cujo host nao esta em `corpos_de_fonte`.

    Devolve lista e nao booleano porque quem reprova precisa NOMEAR a url: "corpo nao
    declarado" sem dizer qual manda procurar em todo o registro.
    """
    return [f.get("url") for f in (registro.get("fontes") or [])
            if f.get("url") and corpo_declarado(f.get("url")) is None]
