#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A REDE DE SINAL DAS BATERIAS DE MUTACAO — uma copia so, para as catorze.

POR QUE ESTE ARQUIVO EXISTE, com data e custo.

Em 09/10/2026 a `mutacoes-par.py` foi morta por sinal no estagio do snippet e
deixou `snippets/clubedomosaico-f2.php` MUTADO no repositorio, com a regra 8
rodando depois da regra 2 e devolvendo `silencio` no lugar de
`ambiente_do_substrato`. `teste-f2.php` foi de 0 para 3 falhas e
`teste-tecnicas.php` de APROVADO para REPROVADO. Quem nomeou o arquivo foi o
`git status`; se a passada tivesse commitado sem remedir, a troca de causa teria
ido ao ar no Sync seguinte.

A causa nao e da `par`, e de FORMA: quatro das dezoito baterias desta ilha
trabalham em `mkdtemp` e nao podem sujar nada; as outras CATORZE trabalham em
cima da arvore do git e restauram no `finally`. E o `finally` NAO RODA quando o
processo morre por sinal — `timeout` e `pkill` mandam SIGTERM, e o SIGTERM
encerra sem passar por ele. A `par` ganhou o conserto no mesmo dia, em seis
linhas; as outras treze ficaram sem, e a lista delas entrou no `ESTADO.md` como
divida da Fundacao.

ESTE ARQUIVO E O PAGAMENTO DESSA DIVIDA, E ELE E UM MODULO E NAO TREZE CopiAS
DE PROPOSITO. Treze copias de seis linhas divergem — a primeira que aprender
algo novo (a sobra de backup abaixo foi exatamente isso) ensina so a si mesma.
Aqui o que uma bateria aprende, as catorze sabem.

O QUE ELE FAZ, E O QUE ELE NAO ALCANCA.

Faz: guarda os BYTES de cada arquivo que a bateria pode escrever, e restaura
esses bytes ANTES de sair quando chega SIGTERM, SIGINT ou SIGHUP. Limpa tambem
a sobra `<arquivo>.original`, porque sete das treze baterias copiam o arquivo
para esse nome antes de mutar e desfazem com `shutil.move` no `finally`: morrer
no meio deixa DUAS coisas erradas, o arquivo mutado e um arquivo a mais que o
manifest nao conhece.

NAO alcanca: SIGKILL. Nada em processo nenhum o alcanca, e por isso a outra
metade da regra continua valendo e esta escrita no `PROMPT.md` desta ilha:
depois de rodar bateria de mutacao, conferir `git status` e rodar a bancada DE
NOVO, nunca so antes. A rede de sinal diminui a chance; o portao de depois e o
que mede.

BYTES, NUNCA O OBJETO DESSERIALIZADO — e isto tambem foi medido. A `apoio` e a
`base` restauravam re-serializando o objeto guardado em memoria, e os arquivos
que elas tocam nao terminavam em quebra de linha: passada verde, conteudo
identico, `sha256` TROCADO. O manifest guarda esse sha e o Sync o compara. Por
isso `retrato()` le em `rb` e `restaura()` escreve em `wb`.
"""

import os
import sys


def retrato(caminhos):
    """Os BYTES de cada arquivo, indexados pelo caminho. Nunca o objeto.

    ARQUIVO QUE NAO EXISTE ENTRA NO RETRATO COM `None`, e isso nao e descuido: a
    `mutacoes-apoio.py` e a `mutacoes-base.py` FABRICAM o mundo delas
    (`dados/materiais-apoio.json`, `dados/materiais-base.json`) e as duas se
    recusam a rodar se o arquivo ja existir, porque existir significaria coleta de
    verdade por baixo. Para essas duas, restaurar e APAGAR — e o estado original
    do arquivo e a ausencia dele."""
    retratados = {}
    for c in caminhos:
        try:
            retratados[c] = open(c, "rb").read()
        except FileNotFoundError:
            retratados[c] = None
    return retratados


def restaura(bytes_de):
    for caminho, b in bytes_de.items():
        if b is None:
            try:
                os.unlink(caminho)
            except OSError:
                pass
            continue
        with open(caminho, "wb") as fh:
            fh.write(b)


def limpa_sobras(caminhos, sufixos=(".original",)):
    """A sobra de backup das baterias que copiam antes de mutar. Devolve a lista
    do que removeu, para a mensagem de saida poder dize-lo."""
    removidas = []
    for caminho in caminhos:
        for sufixo in sufixos:
            sobra = caminho + sufixo
            try:
                if os.path.exists(sobra):
                    os.unlink(sobra)
                    removidas.append(sobra)
            except OSError:
                # Nao trocar a restauracao dos bytes por uma sobra que resistiu:
                # o arquivo a mais o `git status` acusa, o mutado e que engana.
                pass
    return removidas


def restaura_em_sinal(bytes_originais, sufixos=(".original",)):
    """Instala o handler. Chame DEPOIS de `retrato()` e ANTES da primeira
    mutacao — a janela entre as duas chamadas e a unica que fica descoberta."""
    import signal

    def ao_morrer(numero, _quadro):
        restaura(bytes_originais)
        sobras = limpa_sobras(list(bytes_originais), sufixos)
        print("")
        print("INTERROMPIDA por sinal %d — os %d arquivo(s) foram RESTAURADOS byte"
              " a byte antes de sair%s."
              % (numero, len(bytes_originais),
                 "" if not sobras
                 else ", e %d sobra(s) de backup removida(s)" % len(sobras)))
        sys.stdout.flush()
        # 128+N e a convencao de saida por sinal, e e o que o `timeout` devolveria.
        os._exit(128 + numero)

    for numero in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP):
        try:
            signal.signal(numero, ao_morrer)
        except (ValueError, OSError, AttributeError):
            # Sinal que esta plataforma nao tem, ou thread que nao e a principal:
            # o `finally` continua sendo a rede de baixo. Falhar aqui seria trocar
            # uma protecao parcial por nenhuma.
            pass


def arma(caminhos, sufixos=(".original",)):
    """O atalho que as baterias chamam: tira o retrato, instala o handler e
    devolve o retrato, para o `finally` da bateria usar o MESMO retrato."""
    bytes_originais = retrato(caminhos)
    restaura_em_sinal(bytes_originais, sufixos)
    return bytes_originais


def carrega(aqui=None):
    """O carregador, escrito UMA vez aqui para as baterias nao repetirem o
    `importlib`. Nome com hifen nao se importa direto, e renomear o arquivo para
    poder importa-lo seria romper a convencao de nome das ferramentas desta ilha
    por conveniencia de sintaxe."""
    import importlib.util
    pasta = aqui or os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(pasta, "rede-de-sinal.py")
    spec = importlib.util.spec_from_file_location("cdm_rede_de_sinal", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod
