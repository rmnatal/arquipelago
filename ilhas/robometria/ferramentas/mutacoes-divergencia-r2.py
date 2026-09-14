#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""As travas do item 3 do despacho da Sentinela de 14/09/2026, vistas REPROVANDO.

    python3 ferramentas/mutacoes-divergencia-r2.py

POR QUE ESTA BATERIA EXISTE, E POR QUE ELA E SEPARADA DA mutacoes-divergencia.py
--------------------------------------------------------------------------------
Aquela mede a divergencia da R1 — dois canais discordando sobre uma PECA — e
fecha rodando teste-r1.php. Esta mede a divergencia da R2, que e outra coisa:
duas FONTES BRASILEIRAS discordando sobre quantos Pa a situacao pede. Juntar as
duas num arquivo so faria uma bateria que roda dois testes e nao diz qual regra
mediu.

O QUE A RONDA DE 14/09/2026 ACHOU, e por que precisava de mutacao
-----------------------------------------------------------------
No ar, na situacao-ancora — a que a pagina serve a quem chega sem preencher nada,
e portanto a que o Google indexa e um modelo de linguagem le (secao 5):

  "as fontes brasileiras divergem: o Mundo Conectado recomenda 3.000 Pa e o
   Mundo Conectado trata ate 1.500 Pa ja basta como o piso do consenso"

Tres defeitos numa frase, todos no ar desde 09/09/2026:

  1. promete DESACORDO e apresenta UMA fonte, porque `ha_divergencia` comparava
     os dois NUMEROS e nunca perguntava quem os publicou;
  2. a oracao esta quebrada, porque o molde esperava um sintagma nominal e
     recebia "ate 1.500 Pa ja basta";
  3. a linha de procedencia repetia o mesmo documento tres vezes.

E a quarta, que a ronda nao viu e a passada achou ao ler as nove frases como um
leitor leria: "a unica recomendacao brasileira deste banco e a de a Canaltech",
em carpete|nao. A regra da contracao existia nesta ilha desde a manha do mesmo
dia e este molde nao a usava.

NENHUM PORTAO VIA NADA DISSO, e e por isso que cada conserto nasce com a sua
mutacao aqui: a bancada comparava a frase do PHP com a da referencia, e as duas
diziam a MESMA coisa errada — a cicatriz que esta ilha ja pagou tres vezes.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COBERTURA = 'ferramentas/cobertura-r2.py'
SNIPPET = 'snippets/robometria-r2.php'


def _trocar(base, rel, velho, novo):
    caminho = os.path.join(base, rel)
    with open(caminho, encoding='utf-8') as fh:
        texto = fh.read()
    if texto.count(velho) != 1:
        raise AssertionError('%s: o alvo aparece %d vez(es), e a mutacao precisa de '
                             'UMA. Alvo que nao existe mais edita NADA, e a bateria '
                             'fica verde sem ter medido coisa alguma'
                             % (rel, texto.count(velho)))
    with open(caminho, 'w', encoding='utf-8') as fh:
        fh.write(texto.replace(velho, novo))


def m01_divergencia_volta_a_ser_so_numero(base):
    """O DEFEITO LITERAL DE ONTEM: a divergencia decidida comparando os dois
    numeros, sem perguntar quem os publicou. Em liso|nao os dois limiares sao do
    Mundo Conectado, entao a pagina volta a prometer desacordo com uma fonte so."""
    _trocar(base, COBERTURA,
            '        "ha_divergencia": (piso_efetivo(seguro) != piso_efetivo(minimo)\n'
            '                           and seguro["publicador"] != minimo["publicador"]),',
            '        "ha_divergencia": piso_efetivo(seguro) != piso_efetivo(minimo),')


def m02_oracao_do_piso_volta_ao_molde_unico(base):
    """O molde de um tamanho so: "trata %s como o piso do consenso" recebendo a
    saida de escrever_limiar(). Em liso|nao isso produz, letra por letra, a oracao
    quebrada que estava no ar: "trata ate 1.500 Pa ja basta como o piso do
    consenso". Note que esta mutacao SO morde junto com a m01 — por isso ela
    desfaz as duas, produzindo o mundo de ontem inteiro."""
    m01_divergencia_volta_a_ser_so_numero(base)
    _trocar(base, COBERTURA,
            '               escrever_piso(minimo, com_artigo(minimo["publicador"])),',
            '               "%s trata %s como o piso do consenso"\n'
            '               % (com_artigo(minimo["publicador"]), escrever_limiar(minimo)),')


def m03_contracao_some(base):
    """"a de a Canaltech" volta ao ar em carpete|nao. A contracao mora no banco
    desde 14/09; este molde e o unico lugar da R2 que a usa."""
    _trocar(base, COBERTURA,
            '        "Para %s %s, a unica recomendacao brasileira deste banco e a %s: %s "',
            '        "Para %s %s, a unica recomendacao brasileira deste banco e a de %s: %s "')
    _trocar(base, COBERTURA,
            '        % (piso, pelo, pub.com_de(seguro["publicador"]), escrever_limiar(seguro),',
            '        % (piso, pelo, com_artigo(seguro["publicador"]), escrever_limiar(seguro),')


def m04_procedencia_volta_a_repetir(base):
    """A linha de procedencia volta a ser um item por LIMIAR em vez de um por
    DOCUMENTO, e serve "Mundo Conectado · 09/09/2026 fonte" tres vezes."""
    _trocar(base, SNIPPET,
            "\t\t$chave = $l['url'] . '|' . $l['verificado_em'];\n"
            "\t\tif ( isset( $vistas[ $chave ] ) ) {\n"
            "\t\t\tcontinue;\n"
            "\t\t}\n"
            "\t\t$vistas[ $chave ] = 1;\n",
            "")


def m05_mundo_intacto(base):
    """A UNICA QUE TEM DE PASSAR. Regua que reprova o mundo sem defeito e um
    falso-positivo esperando quem chegar amanha para aprender a ignora-la."""
    return


MUTACOES = [
    ('a divergencia volta a ser decidida so pelos NUMEROS',
     'promete desacordo e apresenta uma fonte so, na situacao-ancora',
     m01_divergencia_volta_a_ser_so_numero, False),
    ('MUNDO DE ONTEM: o molde de um tamanho so para o limiar de baixo',
     'produz "trata ate 1.500 Pa ja basta como o piso do consenso", letra por letra',
     m02_oracao_do_piso_volta_ao_molde_unico, False),
    ('a contracao com "de" some do molde da recomendacao unica',
     '"a de a Canaltech" — a regra existia e o molde nao a usava',
     m03_contracao_some, False),
    ('a linha de procedencia volta a ser um item por limiar',
     'o mesmo documento tres vezes passa a impressao de tres apuracoes',
     m04_procedencia_volta_a_repetir, False),
    ('MUNDO INTACTO — esta TEM de passar',
     'regua que reprova o mundo sadio e falso-positivo com data marcada',
     m05_mundo_intacto, True),
]


def copiar(destino):
    for item in ('dados', 'ferramentas', 'snippets', 'manifest.json', 'ARVORE.md'):
        origem = os.path.join(RAIZ, item)
        alvo = os.path.join(destino, item)
        if os.path.isdir(origem):
            shutil.copytree(origem, alvo)
        else:
            shutil.copy2(origem, alvo)


def medir(base):
    """Regera a R2 e roda teste-r2.php inteiro. Geracao que morre conta como
    reprovacao: ilha que nao monta tambem nao publica."""
    r = subprocess.run([sys.executable, 'ferramentas/gerar-r2.py', '--gravar'],
                       cwd=base, capture_output=True, text=True)
    if r.returncode != 0:
        return 1, 'gerar-r2.py falhou (a mutacao derrubou a geracao)'
    r = subprocess.run(['php', 'ferramentas/teste-r2.php', '.'],
                       cwd=base, capture_output=True, text=True)
    linhas = [l for l in r.stdout.strip().splitlines() if l.strip()]
    return r.returncode, (linhas[-1] if linhas else '(sem saida)')


def main():
    print('MUTACOES DA DIVERGENCIA DA R2 — item 3 do despacho de 14/09/2026')
    print('=' * 78)
    erros = []
    for nome, porque, aplicar, tem_de_passar in MUTACOES:
        with tempfile.TemporaryDirectory() as tmp:
            copiar(tmp)
            try:
                aplicar(tmp)
            except AssertionError as e:
                erros.append('%s: %s' % (nome, e))
                print('  ERRO   %-62s %s' % (nome, e))
                continue
            codigo, ultima = medir(tmp)
            passou = codigo == 0
            if passou == tem_de_passar:
                print('  ok     %-62s %s' % (nome, ultima))
            else:
                erros.append(nome)
                print('  ERRADA %-62s %s' % (nome, ultima))
                print('         %s' % porque)

    print('\n%d de %d como esperado.' % (len(MUTACOES) - len(erros), len(MUTACOES)))
    if erros:
        print('FALHOU em: ' + '; '.join(erros))
        return 1
    print('Nenhuma mutacao inerte: toda trava do item 3 foi vista reprovando.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
