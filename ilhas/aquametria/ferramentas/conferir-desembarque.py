#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O PORTAO DO DESEMBARQUE: le o LOG do /status, nao so a revisao dele.

POR QUE ESTE ARQUIVO EXISTE, com a data e o custo (12/10/2026, 19h42Z-19h52Z).
A regra desta fabrica desde 11/09 e "commit sem Sync nao e entrega" (secao 20 do
ARQUIPELAGO.md), e a conferencia que toda execucao faz e: a `revisao` do /status
bate com a do `manifest.json`? Hoje ela bateu — **82 nos dois** — e SETE paginas
do Guia estavam servindo o tema cru do WordPress, sem meta description, sem
tabela e sem numero.

O que aconteceu: o Sync acionado com `forcar=1` reescreve TODO item, inclusive
os snippets. Ele grava snippet INATIVO de proposito (o Code Snippets executa o
codigo ao gravar snippet ativo, e isso quebra se o snippet ja esta carregado
naquela requisicao) e ATIVA depois, por `activate_snippet()`. A ativacao do
snippet do Guia voltou com `o codigo nao passou na validacao`, e o Sync
registrou isso numa linha do log:

    snippets/guia: gravado (#13) mas NAO ativado: Nao foi possivel ativar o
    snippet: o codigo nao passou na validacao.

E seguiu em frente. **A revisao subiu, o `/status` ficou verde e o snippet
ficou desativado.** Quem conferiu so a revisao leu "entregue". A segunda
passada do Sync ativou o snippet na hora — porque dessa vez ele estava inativo
e, portanto, nao carregado na requisicao — e as sete paginas voltaram inteiras.

O defeito foi pego por SORTE: o `conferir-no-ar.py` tem uma afirmacao que exige
meta description nas 32 URLs do sitemap, e foi ela que reprovou. Se o snippet
desativado fosse um que nao serve `<head>`, ninguem teria visto. **Portao que
depende de sorte nao e portao**, e a linha que acusa o defeito ja estava
escrita, em portugues, dentro do proprio /status: faltava alguem le-la.

O QUE ESTE PORTAO MEDE:
  1. o /status responde e e JSON;
  2. a `revisao` dele bate com a do `manifest.json` (a conferencia antiga,
     que continua certa e nao basta);
  3. NENHUMA linha do log da revisao corrente deixa de dizer `ok` — e cada
     linha que nao diz e impressa inteira, porque o motivo vem escrito nela;
  4. quantas linhas da revisao corrente a janela do log mostra, contra o
     numero de aplicados que o cabecalho dela declara. O log e uma JANELA
     (hoje 15 linhas), entao item aplicado pode ter rolado para fora: isso e
     REGISTRO, nunca aprovacao com cara de completo.

COPIADO PARA A AQUAMETRIA EM 14/10/2026, e a 20.4 manda isso com estas palavras:
"Toda ilha com Sync copia esse portao — o Sync e o mesmo codigo nas tres — e quem
o copiar troca so o dominio e o nome da rota." Foi so o que se trocou, mais os
casos 9 e 10 do autoteste, que sao o mundo desta ilha e desta data.

E A RAZAO DE COPIAR NAO FOI ZELO: foi medicao. O desembarque da revisao 119, as
14h03Z de 14/10/2026, aplicou 20 itens e a janela do log mostrou 15 — e os CINCO
que rolaram para fora incluiam exatamente os tres snippets que aquele bloco
mudou (o seo-tecnico, o da vazao e o do aquecedor). As vinte linhas podiam todas
dizer `ok`, e tres das mudancas daquela entrega nao foram conferidas pelo log.
Foi o ar que as provou, nao o /status. O item 4 deste portao existe para dizer
isso em voz alta — "o que nao esta na janela NAO foi conferido" — em vez de
aprovar com cara de completo.

Uso:
    python3 ferramentas/conferir-desembarque.py .
    python3 ferramentas/conferir-desembarque.py . --autoteste
"""

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

RAIZ = sys.argv[1].rstrip("/") if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "."
AUTOTESTE = "--autoteste" in sys.argv

STATUS = "https://aquametria.com.br/wp-json/aquametria/v1/status"

# A linha de cabecalho da revisao: `2026-10-12 19:52 revisão 82: 18 aplicado(s), ...`
RE_CABECALHO = re.compile(r"revis\w*\s+(\d+):\s*(\d+)\s+aplicado", re.I)


def ler_status(url=STATUS):
    """Com quebra de cache: a borda desta ilha guarda resposta por 2 horas."""
    sep = "&" if "?" in url else "?"
    req = urllib.request.Request(url + sep + "v=" + str(int(time.time() * 1000)),
                                 headers={"User-Agent": "conferir-desembarque/1.0",
                                          "Cache-Control": "no-cache"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def analisar(status, revisao_do_manifest):
    """O veredito inteiro, sem rede: e isto que o autoteste mede.

    Devolve (falhas, linhas_do_relatorio). `falhas` e lista de texto; lista
    vazia e aprovacao.
    """
    falhas, saida = [], []
    rev = status.get("revisao")
    log = status.get("log") or []

    saida.append(("ok" if rev == revisao_do_manifest else "FALHA",
                  "a revisao do /status bate com a do manifest.json",
                  "/status %s | manifest %s" % (rev, revisao_do_manifest)))
    if rev != revisao_do_manifest:
        falhas.append("revisao divergente: /status %s, manifest %s" % (rev, revisao_do_manifest))

    # A JANELA DA REVISAO CORRENTE: do cabecalho dela ate o cabecalho anterior.
    # Linha de outra revisao nao e desta entrega e nao se julga aqui — julgar o
    # passado faria o portao reprovar para sempre por um defeito ja consertado.
    inicio, declarados, rev_do_log = None, None, None
    for i, linha in enumerate(log):
        m = RE_CABECALHO.search(str(linha))
        if m:
            inicio, rev_do_log, declarados = i, int(m.group(1)), int(m.group(2))
            break
    if inicio is None:
        falhas.append("o log nao tem linha de cabecalho de revisao — nao da para dizer o que esta entrega aplicou")
        saida.append(("FALHA", "o log declara a revisao que aplicou", "nenhuma linha de cabecalho"))
        return falhas, saida

    fim = len(log)
    for j in range(inicio + 1, len(log)):
        if RE_CABECALHO.search(str(log[j])):
            fim = j
            break
    itens = [str(l) for l in log[inicio + 1:fim]]

    saida.append(("ok" if rev_do_log == rev else "FALHA",
                  "o cabecalho do log e da revisao que o /status declara",
                  "log %s | status %s" % (rev_do_log, rev)))
    if rev_do_log != rev:
        falhas.append("o log mais novo e da revisao %s e o /status diz %s" % (rev_do_log, rev))

    # O CORACAO: toda linha de item desta revisao tem de dizer `ok`.
    ruins = [l for l in itens if ": ok" not in l]
    saida.append(("ok" if not ruins else "FALHA",
                  "nenhuma linha da revisao %s deixa de dizer ok" % rev_do_log,
                  "%d linha(s) de item lidas" % len(itens)))
    for l in ruins:
        falhas.append("linha do Sync que nao diz ok: " + l)
        saida.append(("FALHA", "  -> " + l[:160], ""))

    # REGISTRO, NUNCA PORTAO: a janela pode ter cortado linha de item.
    saida.append(("registro", "linhas de item visiveis contra aplicados declarados",
                  "%d visiveis de %d aplicado(s)%s" % (
                      len(itens), declarados,
                      "" if len(itens) >= declarados
                      else " — a janela do log cortou %d, e o que nao esta na janela NAO foi conferido"
                           % (declarados - len(itens)))))
    return falhas, saida


def autoteste():
    """Cada caso mata o portao de proposito, e o caso 1 e o mundo de hoje."""
    casos = [
        ("O MUNDO MEDIDO AS 19h42Z DE HOJE: revisao certa, snippet do Guia NAO ativado", 82, {
            "revisao": 82,
            "log": [
                "2026-10-12 19:42 revisão 82: 17 aplicado(s), 18 aguardando desembarque [forçado]",
                "2026-10-12 19:42 dados/esquema-banco: ok (option clubedomosaico_dados_esquema-banco)",
                "2026-10-12 19:42 snippets/guia: gravado (#13) mas NÃO ativado: Não foi possível "
                "ativar o snippet: o código não passou na validação.",
                "2026-10-12 19:42 snippets/leads: ok (snippet #11 atualizado)",
            ]}, "reprova"),
        ("O MUNDO MEDIDO AS 19h52Z: a segunda passada ativou e tudo diz ok", 82, {
            "revisao": 82,
            "log": [
                "2026-10-12 19:52 revisão 82: 18 aplicado(s), 18 aguardando desembarque [forçado]",
                "2026-10-12 19:52 dados/esquema-banco: ok (option clubedomosaico_dados_esquema-banco)",
                "2026-10-12 19:52 snippets/guia: ok (snippet #13 atualizado)",
            ]}, "aprova"),
        ("revisao do /status atrasada em relacao ao manifest (commit sem Sync)", 83, {
            "revisao": 82,
            "log": ["2026-10-12 19:52 revisão 82: 1 aplicado(s), 18 aguardando desembarque",
                    "2026-10-12 19:52 dados/tecnicas: ok (option clubedomosaico_dados_tecnicas)"],
        }, "reprova"),
        ("sha divergente num item, com a revisao batendo", 82, {
            "revisao": 82,
            "log": ["2026-10-12 19:52 revisão 82: 2 aplicado(s), 18 aguardando desembarque",
                    "2026-10-12 19:52 dados/tecnicas: sha256 divergente — não aplicado",
                    "2026-10-12 19:52 snippets/guia: ok (snippet #13 atualizado)"],
        }, "reprova"),
        ("snippet gravado e inativo pelo OUTRO caminho (continua inativo apos activate)", 82, {
            "revisao": 82,
            "log": ["2026-10-12 19:52 revisão 82: 1 aplicado(s), 18 aguardando desembarque",
                    "2026-10-12 19:52 snippets/guia: gravado (#13) mas continua inativo após activate_snippet"],
        }, "reprova"),
        ("LINHA RUIM DE UMA REVISAO ANTERIOR nao reprova a entrega de agora", 82, {
            "revisao": 82,
            "log": ["2026-10-12 19:52 revisão 82: 1 aplicado(s), 18 aguardando desembarque",
                    "2026-10-12 19:52 snippets/guia: ok (snippet #13 atualizado)",
                    "2026-10-12 19:42 revisão 81: 1 aplicado(s), 18 aguardando desembarque",
                    "2026-10-12 19:42 snippets/guia: gravado (#13) mas NÃO ativado: validação"],
        }, "aprova"),
        ("log sem cabecalho de revisao: nao da para saber o que foi aplicado", 82, {
            "revisao": 82, "log": ["2026-10-12 19:52 dados/tecnicas: ok (option x)"],
        }, "reprova"),
        ("JANELA CURTA: 1 linha visivel de 9 aplicados e REGISTRO, nao reprovacao", 82, {
            "revisao": 82,
            "log": ["2026-10-12 19:52 revisão 82: 9 aplicado(s), 18 aguardando desembarque",
                    "2026-10-12 19:52 dados/tecnicas: ok (option clubedomosaico_dados_tecnicas)"],
        }, "aprova"),
        ("A AQUAMETRIA AS 14h03Z DE 14/10/2026: revisao 119, 20 aplicados e 15 na janela — "
         "aprova, E DIZ que cortou 5", 119, {
            "revisao": 119,
            "log": ["2026-10-14 14:03 revisão 119: 20 aplicado(s), 15 aguardando desembarque [forçado]",
                    "2026-10-14 14:03 conteudo/politica-de-privacidade: ok (page #121 atualizado)",
                    "2026-10-14 14:03 conteudo/calculadora-de-iluminacao: ok (page #22 atualizado)",
                    "2026-10-14 14:03 snippets/aquametria-peixes: ok (snippet #15 atualizado)",
                    "2026-10-14 14:03 snippets/aquametria-calculadora-midia: ok (snippet #10 atualizado)"],
        }, "aprova"),
        ("O MESMO DESEMBARQUE COM O SEO-TECNICO RECUSADO NA ATIVACAO — e o defeito de "
         "12/10 nesta ilha, no snippet que serve TODA meta description", 119, {
            "revisao": 119,
            "log": ["2026-10-14 14:03 revisão 119: 20 aplicado(s), 15 aguardando desembarque [forçado]",
                    "2026-10-14 14:03 conteudo/calculadora-de-iluminacao: ok (page #22 atualizado)",
                    "2026-10-14 14:03 snippets/aquametria-seo-tecnico: gravado (#12) mas NÃO ativado: "
                    "Não foi possível ativar o snippet: o código não passou na validação."],
        }, "reprova"),
    ]
    erradas = 0
    for i, (nome, rev_manifest, status, esperado) in enumerate(casos, 1):
        falhas, _ = analisar(status, rev_manifest)
        obtido = "reprova" if falhas else "aprova"
        marca = "ok  " if obtido == esperado else "FALHA"
        if obtido != esperado:
            erradas += 1
        print("  %s caso %d  %-66s -> %s (esperado %s)" % (marca, i, nome[:66], obtido, esperado))
    print()
    if erradas:
        sys.exit("AUTOTESTE REPROVADO: %d de %d" % (erradas, len(casos)))
    print("AUTOTESTE APROVADO: %d de %d casos. O caso 1 e o defeito de 12/10/2026 as 19h42Z,"
          % (len(casos), len(casos)))
    print("que subiu a revisao, deixou o /status verde e desativou o snippet de SETE paginas")
    print("na clubedomosaico. Os casos 9 e 10 sao desta ilha: a entrega de 14/10/2026, em que a")
    print("janela do log cortou CINCO das vinte linhas, tres delas de snippet mudado naquele bloco.")


def main():
    if AUTOTESTE:
        autoteste()
        return 0

    caminho = os.path.join(RAIZ, "manifest.json")
    try:
        manifest = json.load(open(caminho, encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        sys.exit("nao consegui ler %s: %s" % (caminho, e))

    try:
        status = ler_status()
    except (urllib.error.URLError, json.JSONDecodeError, OSError) as e:
        sys.exit("o /status nao respondeu ou nao e JSON: %s. Pela 20.2, repita antes de "
                 "chamar de bloqueio." % e)

    falhas, saida = analisar(status, manifest.get("revisao"))
    print("O DESEMBARQUE, lido no LOG do /status e nao so na revisao dele:\n")
    for marca, afirmacao, medida in saida:
        print("  %-9s %-62s %s" % (marca, afirmacao, medida))
    print()
    if falhas:
        print("REPROVADO: %d problema(s) no desembarque da revisao %s." % (len(falhas), status.get("revisao")))
        print("Acione o Sync outra vez e releia: snippet gravado inativo ativa na passada seguinte,")
        print("porque nela ele nao esta carregado na requisicao. O que nao se faz e ler a revisao")
        print("como entrega — foi isso que custou sete paginas do Guia em 12/10/2026.")
        return 1
    print("APROVADO: revisao %s no manifest e no /status, e toda linha do log desta revisao diz ok."
          % status.get("revisao"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
