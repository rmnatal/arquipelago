#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
O NOME EXIBIDO DE UM REGISTRO — UMA FUNCAO, E E ELA QUE AS TRES FERRAMENTAS CHAMAM.

Nasceu em 09/11/2026, pelo item 1 do despacho da ronda do dia. O defeito medido
era a F2 servindo `scooter-chopper-1000w-48v` e outros TRES identificadores de
repositorio em texto visivel, onde a home e a F3 serviam o nome humano dos
MESMOS registros. A causa nao era a F2: eram TRES geradores decidindo a mesma
coisa em SEIS lugares, com CINCO respostas diferentes para o registro em que
`marca` e `modelo` sao null — e isso e a 20.7 desta ilha em forma de nome,
*"duas declaracoes do mesmo fato comecam iguais e so uma sobe"*.

AS CINCO RESPOSTAS QUE EXISTIAM, MEDIDAS NO HTML SERVIDO ANTES DO CONSERTO:

  1. `regras/f3.py`      -> `titulo_colhido` inteiro. A UNICA CERTA.
  2. `gerar-f1.py:223`   -> `titulo_colhido[:60]`, e o corte NAO e cosmetico:
                            a home servia `(2 x 1.000 ` — cortado no meio do
                            numero, perdendo a unidade e o `72 km/h` — e
                            `(+25 vendid`, cortado no meio da palavra, SEM
                            reticencia nenhuma que avisasse do corte. Numa ilha
                            cuja tese e que o numero do anuncio engana, servir
                            numero decapitado e o defeito dentro do produto.
  3. `gerar-f1.py:470`   -> SEM fallback: `" ".join(...)` devolvia CADEIA VAZIA
                            para registro sem marca e sem modelo. Hoje aquele
                            grupo (`cabem_na_categoria`) esta vazio, entao o
                            buraco nunca foi servido — e ele estava armado para
                            o dia em que o primeiro registro classificasse.
  4. `gerar-f2.py:273`   -> `or r.get("id")`: o slug na tela. O defeito do item 1.
  5. `gerar-f2.py:395`   -> `or r["id"]`: o mesmo, na ficha do cartao.

E a sexta chamada, `coletar-oferta.py`, caia no `id` tambem — e aquela nao vai
para tela, mas e por onde o nome ENTRA, e nome de entrada diferente do nome de
tela e a divergencia da proxima semana.

POR QUE O `titulo_colhido` INTEIRO, E NAO O CORTE: o titulo e a PROVA da tese
desta ilha — e a palavra do VENDEDOR, nao a da ilha (secao 26 do
ARQUIPELAGO.md), e e justamente nele que o watt sem rotulo e a venda contada
aparecem. Cortar em 60 caracteres joga fora a metade que prova. Quem precisar de
nome curto por causa de largura de tela resolve isso no CSS, onde cortar nao
apaga dado: o HTML serve o nome inteiro e a camada que a IA ingere tambem.

POR QUE AQUI E NAO EM `ferramentas/`: a `bancada.py` varre `ferramentas/` e
classifica tudo pela convencao de nome; referencia nao e portao. E a mesma razao
que pos `regras/f1.py`, `f2.py` e `f3.py` nesta pasta, escrita em `regras/LEIA.md`.

O QUE GARANTE QUE ISTO RODA: os tres geradores a importam, a bancada roda os tres
com `--conferir` em toda passada, e `ferramentas/teste-nome-do-registro.py`
denuncia qualquer lugar que volte a derivar nome de `marca`/`modelo` por conta
propria — porque o conserto de hoje seria desfeito pela proxima linha escrita
de cabeca, e ela seria escrita, como foi cinco vezes.
"""

#: Os campos que o nome le, em ordem de prioridade. Lista aqui, nunca espalhada.
CAMPOS_DO_NOME = ("marca", "modelo", "titulo_colhido", "id")


def nome_do_registro(r):
    """O nome que a tela usa, e ele sai do banco, nunca do `id` quando ha titulo.

    Marca + modelo quando os dois existem; o que houver quando falta um. Sem
    marca nem modelo, o `titulo_colhido` INTEIRO — que e a palavra do VENDEDOR e
    nao da ilha (secao 26). Sem nada disso, o `id`, que e o ULTIMO recurso e
    nunca o primeiro: slug com hifen, sem acento e sem espaco e o vocabulario de
    quem escreveu a fabrica, e a 32.4 proibe servi-lo ao visitante.

    Registro sem nenhum dos quatro devolve cadeia vazia, e isso e DENUNCIA e nao
    escolha: quem recebe cadeia vazia daqui tem um registro sem identidade, e o
    validador do banco ja reprova `id` ausente. A funcao nao inventa nome.
    """
    marca = (r.get("marca") or "").strip()
    modelo = (r.get("modelo") or "").strip()
    if marca and modelo:
        return "%s %s" % (marca, modelo)
    if marca or modelo:
        return marca or modelo
    titulo = (r.get("titulo_colhido") or "").strip()
    if titulo:
        return titulo
    return (r.get("id") or "").strip()


def nome_e_fonte(r):
    """O nome e DE ONDE ele veio, para quem precisa dizer isso na tela.

    A F2 nomeia os registros sem marca pelo titulo do anuncio, e a pagina tem o
    direito de avisar que aquele nome e do VENDEDOR. Devolver a fonte junto
    evita que a pagina adivinhe a fonte olhando o nome — que e a heuristica por
    vizinhanca que a secao 8 do ARQUIPELAGO.md proibe.
    """
    marca = (r.get("marca") or "").strip()
    modelo = (r.get("modelo") or "").strip()
    if marca or modelo:
        return nome_do_registro(r), "banco"
    if (r.get("titulo_colhido") or "").strip():
        return nome_do_registro(r), "titulo_do_anuncio"
    return nome_do_registro(r), "id"
