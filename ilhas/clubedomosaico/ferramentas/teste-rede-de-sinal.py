#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O PORTAO DA REDE DE SINAL — mata cada bateria de mutacao de proposito e
mede se a arvore do git volta limpa.

POR QUE ELE EXISTE. Em 09/10/2026 a `mutacoes-par.py` foi morta por sinal e
deixou `snippets/clubedomosaico-f2.php` mutado no repositorio; quem pegou foi o
`git status` de quem lembrou de olhar. O conserto de codigo (a
`ferramentas/rede-de-sinal.py`) foi escrito no mesmo dia para uma bateria e no
dia seguinte para as catorze — mas conserto sem portao e promessa: a prova de
que ele funciona nas catorze era matar catorze processos a mao, uma vez, e nunca
mais. Este arquivo e essa prova virando comando.

O QUE ELE MEDE, por bateria:

1. a bateria FOI morta no meio do trabalho — nao depois de terminar. A prova e
   positiva e vem da propria bateria: a linha `INTERROMPIDA por sinal 15` so e
   impressa pelo handler. Kill que chega depois do fim nao prova nada, e o
   portao o chama de NAO MEDIDO em vez de aprovado;
2. a arvore do git da ilha voltou LIMPA — nenhum arquivo mutado, nenhum apagado,
   nenhum fabricado deixado para tras;
3. nao sobrou nenhum `<arquivo>.original`, o backup que sete das baterias criam
   antes de mutar e desfazem com `shutil.move` no `finally`. Morrer no meio
   deixava DUAS coisas erradas, e so uma delas o `git status` mostra como `M`.

E ELE MEDE UMA QUARTA COISA, que nao e por bateria e e a que envelhece pior:
TODA `mutacoes-*.py` desta pasta esta classificada. Ou ela chama
`tempfile.mkdtemp(` (trabalha em copia e nao pode sujar nada), ou ela declara a
rede de sinal. Bateria nova que nasca sem nenhum dos dois reprova aqui, no dia
em que nasce, em vez de reprovar no dia em que alguem a matar.

A CLASSIFICACAO E POR CHAMADA, NUNCA POR MENCAO — e esta linha tem custo
medido. O `PROMPT.md` desta ilha mandava derivar a lista com
`grep -L 'mkdtemp\\|copytree' ferramentas/mutacoes-*.py`, e esse comando
ESCONDE a `mutacoes-par.py`: ela trabalha em cima da arvore (foi ela que deixou
o snippet mutado), e some da lista porque o COMENTARIO dela cita `mkdtemp` para
explicar que ela nao usa. O comando prometia treze e a verdade eram catorze, e a
que faltava era justamente a que provou o defeito. Aqui a busca e por `mkdtemp(`
com parentese.

O QUE ELE NAO ALCANCA: SIGKILL. Nada em processo nenhum o alcanca, e por isso a
outra metade da regra continua no `PROMPT.md`: depois de rodar bateria de
mutacao, conferir `git status` e rodar a bancada DE NOVO.

USO:  python3 ferramentas/teste-rede-de-sinal.py .
      python3 ferramentas/teste-rede-de-sinal.py . mutacoes-preparo.py   (uma so)
"""

import glob
import hashlib
import os
import re
import signal
import subprocess
import sys
import threading
import time

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)
_RAIZ_DO_GIT = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                              capture_output=True, text=True, cwd=ILHA).stdout.strip()

# A MARCA QUE PROVA QUE A REDE FALOU. So o handler a imprime, entao ela e prova
# positiva de que o sinal chegou com a bateria viva e passou pela rede — nao
# depois de ela terminar, quando um kill nao prova nada.
MARCA_DO_HANDLER = "INTERROMPIDA por sinal"
TETO_SEGUNDOS = 900.0
PASSO_DA_ESPREITA = 0.05


def estado_da_arvore():
    """O ESTADO da pasta da ilha, nao a limpeza dela — e a diferenca importa.

    A primeira versao deste portao se RECUSAVA a rodar com a arvore suja, e isso
    o tornava inutil exatamente quando ele e mais necessario: na passada que
    acabou de escrever o conserto e quer prova ANTES de commitar. O portao nao
    precisa de arvore limpa, precisa de arvore IGUAL — ele compara o estado de
    antes com o de depois de cada bateria morrer.

    O estado tem tres partes, e nenhuma sozinha basta: as linhas do `git status`
    (pegam arquivo novo, apagado e nao rastreado, que `git diff` nao mostra), o
    sha do `git diff` (pega mudanca de conteudo em arquivo que ja estava
    modificado, que o `git status` mostra como ` M` nos dois casos) e o sha do
    conteudo de cada arquivo nao rastreado (pega mundo fabricado reescrito)."""
    porcelain = subprocess.run(["git", "status", "--porcelain", "--", ILHA],
                               capture_output=True, text=True, cwd=ILHA)
    linhas = [l for l in porcelain.stdout.splitlines() if l.strip()]
    diff = subprocess.run(["git", "diff", "--", ILHA],
                          capture_output=True, cwd=ILHA)
    nao_rastreados = {}
    for l in linhas:
        if l.startswith("??"):
            rel = l[3:].strip().strip('"')
            caminho = os.path.join(_RAIZ_DO_GIT, rel)
            try:
                nao_rastreados[rel] = hashlib.sha256(open(caminho, "rb").read()).hexdigest()
            except (OSError, IsADirectoryError):
                nao_rastreados[rel] = "ilegivel"
    return (tuple(linhas),
            hashlib.sha256(diff.stdout).hexdigest(),
            tuple(sorted(nao_rastreados.items())))


def diferenca(antes, depois):
    """As linhas que explicam a divergencia, em portugues, para o relatorio."""
    saiu = []
    novas = [l for l in depois[0] if l not in antes[0]]
    sumiram = [l for l in antes[0] if l not in depois[0]]
    for l in novas:
        saiu.append("apareceu no git status: %s" % l)
    for l in sumiram:
        saiu.append("desapareceu do git status: %s" % l)
    if antes[1] != depois[1] and not novas and not sumiram:
        saiu.append("o conteudo de arquivo JA modificado mudou (o sha do git diff trocou)")
    de_antes = dict(antes[2])
    for rel, sha in depois[2]:
        if de_antes.get(rel) not in (None, sha):
            saiu.append("o arquivo nao rastreado %s foi reescrito" % rel)
    return saiu


def sobras():
    return sorted(glob.glob(os.path.join(ILHA, "**", "*.original"), recursive=True))


def classifica():
    """Devolve (em_copia, na_arvore, sem_classificacao)."""
    em_copia, na_arvore, orfas = [], [], []
    for caminho in sorted(glob.glob(os.path.join(AQUI, "mutacoes-*.py"))):
        fonte = open(caminho, encoding="utf-8").read()
        nome = os.path.basename(caminho)
        if re.search(r"\bmkdtemp\(", fonte):
            em_copia.append(nome)
        elif "_rede_de_sinal(" in fonte or "restaura_em_sinal(" in fonte:
            na_arvore.append(nome)
        else:
            orfas.append(nome)
    return em_copia, na_arvore, orfas


def mata_no_meio(nome):
    """Roda a bateria, espera a arvore MUDAR, manda SIGTERM nesse instante e
    devolve (chegou_no_meio, viu_o_handler, saida).

    A PRIMEIRA VERSAO ESPREITAVA A SAIDA e procurava `REPROVOU|PASSOU|INERTE`.
    Ela media o VOCABULARIO de cada bateria, e as catorze nao falam igual: a
    `ambiente-do-produto-do-rejunte` imprime `so o portao novo` e `ja pegava` por
    mutacao e nenhuma das duas casava, entao o portao atravessava a fase inteira
    de 45 celulas — minutos — esperando uma palavra que nao vinha. Portao que
    depende do texto da coisa medida envelhece a cada bateria nova.

    O QUE ELE ESPREITA AGORA E O QUE ELE QUER MEDIR: a arvore do git mudar. E o
    instante exato em que existe arquivo mutado no disco, que e a janela em que o
    sinal doi, e nao depende de uma palavra."""
    env = dict(os.environ)
    env["PYTHONUNBUFFERED"] = "1"   # sem isto a marca do handler so chega no fim
    saida = []

    def drena(fluxo):
        for linha in fluxo:
            saida.append(linha.rstrip("\n"))

    proc = subprocess.Popen([sys.executable, os.path.join(AQUI, nome)],
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            text=True, cwd=ILHA, env=env)
    leitor = threading.Thread(target=drena, args=(proc.stdout,), daemon=True)
    leitor.start()

    de_partida = estado_da_arvore()
    no_meio = False
    comeco = time.time()
    while proc.poll() is None and time.time() - comeco < TETO_SEGUNDOS:
        if diferenca(de_partida, estado_da_arvore()):
            no_meio = True
            proc.send_signal(signal.SIGTERM)
            break
        time.sleep(PASSO_DA_ESPREITA)
    try:
        proc.wait(timeout=120)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()
    leitor.join(timeout=20)
    return no_meio, any(MARCA_DO_HANDLER in l for l in saida), saida


def main(argv):
    # `argv[1]` e a raiz, pela convencao das ferramentas desta ilha
    # (`python3 ferramentas/X.py .`) — este portao nao a usa, porque deriva tudo
    # de `__file__`, mas aceita-la e o que faz o comando parecer com os outros. O
    # filtro de UMA bateria e o `argv[2]`. A primeira versao leu a raiz como
    # filtro e reprovou dizendo que `.` nao e bateria.
    so_esta = argv[2] if len(argv) > 2 else None

    antes = estado_da_arvore()
    if antes[0]:
        print("A arvore da ilha ja tem %d alteracao(oes) antes do portao rodar. Ele roda"
              % len(antes[0]))
        print("assim mesmo: o que ele mede e a arvore voltar IGUAL, nunca limpa — e e")
        print("por isso que ele serve a passada que acabou de escrever o conserto.")
        print("")

    em_copia, na_arvore, orfas = classifica()
    print("A CLASSIFICACAO DAS BATERIAS — por chamada de `mkdtemp(`, nunca por mencao")
    print("  em copia (`mkdtemp`), nao podem sujar nada ..... %d" % len(em_copia))
    print("  em cima da arvore, com rede de sinal ........... %d" % len(na_arvore))
    print("  em cima da arvore, SEM rede de sinal ........... %d" % len(orfas))
    for nome in orfas:
        print("     SEM REDE  %s" % nome)
    print("")

    alvos = [n for n in na_arvore if not so_esta or n == so_esta]
    if so_esta and not alvos:
        print("FALHA: %s nao esta na lista das que trabalham em cima da arvore." % so_esta)
        return 1

    print("MATANDO %d bateria(s) no meio do trabalho, com SIGTERM" % len(alvos))
    print("")
    falhas = 0
    nao_medidas = 0
    for nome in alvos:
        no_meio, viu_handler, saida = mata_no_meio(nome)
        depois = diferenca(antes, estado_da_arvore())
        resto = sobras()
        problemas = []
        if not no_meio:
            problemas.append("o sinal nao chegou no meio: a arvore nunca mudou enquanto"
                             " ela rodava")
        elif not viu_handler:
            problemas.append("o handler nao falou: a bateria morreu sem passar pela rede")
        if depois:
            problemas.append("a arvore nao voltou ao estado de antes: " + "; ".join(depois))
        if resto:
            problemas.append("sobrou backup: " + "; ".join(os.path.relpath(s, ILHA) for s in resto))

        if not problemas:
            print("  ok        %-44s morta no meio, arvore igual" % nome)
            continue
        if problemas == ["o sinal nao chegou no meio: a arvore nunca mudou enquanto"
                         " ela rodava"]:
            nao_medidas += 1
            print("  NAO MEDIDO %-43s %s" % (nome, problemas[0]))
            print("             (as ultimas linhas: %s)"
                  % " | ".join(saida[-2:]) if saida else "")
            continue
        falhas += 1
        print("  FALHA     %-44s" % nome)
        for p in problemas:
            print("              - %s" % p)
        print("            as ultimas linhas da bateria:")
        for l in saida[-6:]:
            print("              | %s" % l)
        # Nao conserta por conta propria: deixar o estrago visivel e o que faz o
        # portao valer. Quem rodar ve o nome do arquivo e decide.

    print("")
    print("  baterias medidas ............... %d" % (len(alvos) - nao_medidas))
    print("  nao medidas .................... %d" % nao_medidas)
    print("  falhas ......................... %d" % falhas)
    if orfas:
        print("\nREPROVADO: %d bateria(s) trabalham em cima da arvore sem rede de sinal."
              % len(orfas))
        return 1
    if falhas:
        print("\nREPROVADO: %d bateria(s) deixaram estrago ao morrer por sinal." % falhas)
        return 1
    if nao_medidas:
        print("\nREPROVADO: %d bateria(s) nao chegaram a ser medidas. Portao que nao mede"
              " nao aprova." % nao_medidas)
        return 1
    print("\nAPROVADO: as %d baterias que trabalham em cima da arvore morreram no meio"
          " e devolveram a arvore IGUAL ao estado de antes." % len(alvos))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
