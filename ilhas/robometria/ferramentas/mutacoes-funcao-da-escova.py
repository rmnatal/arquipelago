#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escreve de volta o defeito da funcao lida do nome do produto e exige REPROVACAO.

    python3 ferramentas/mutacoes-funcao-da-escova.py

POR QUE ESTE ARQUIVO EXISTE
---------------------------
"A PROVA DE QUE UMA TRAVA REPROVA E PARTE DO BLOCO" (secao 8 do ARQUIPELAGO.md).

O DEFEITO, medido em 13/09/2026 na leva de pecas da WAP. O vocabulario desta ilha
separa `escova lateral` de `escova principal` — sao FUNCOES. O fabricante batiza a
peca pela POSICAO: "Escova Direita", "Escova Esquerda", "Escova Central", "Escova
Frontal", "Escova Rotativa". As duas nomenclaturas nao coincidem, e a WAP prova
isso sozinha, no proprio canal:

  - o conteudo declarado do W300 chama de "escovas GIRATORIAS direita e esquerda"
    o par LATERAL;
  - o artigo de limpeza do W90, no blog da mesma marca, chama de "Escova Principal
    (Escova GIRATORIA)" a PRINCIPAL.

Mesma palavra, mesmo fabricante, funcoes opostas. Quem ler "Escova Rotativa Para
Robo Aspirador de Po WAP Robot W90" e gravar `escova lateral` porque "rotativa
parece lateral" acerta ou erra por sorte — e a R1 publica o palpite com cara de
declaracao do fabricante, que e o unico produto desta ilha.

Foi por isso que a escova do W90 NAO entrou no banco em 13/09: o catalogo daquele
modelo tem UMA escova publicada e nenhum contraste, enquanto o proprio canal de
manutencao declara que o W90 tem DUAS. Nao ha de onde ler a funcao.

A trava nova esta em `ferramentas/validar-banco.py` e exige `funcao{}` em toda
peca cujo tipo esteja em `tipos_que_exigem_funcao_declarada` — lista que mora no
ESQUEMA, nao dentro da regua.

O QUE CADA MUTACAO TEM DE FAZER: reprovar. A (5) e a que importa — ela nao mexe em
nenhum registro, mexe no ESQUEMA, e e o unico jeito de a trava morrer sem que uma
linha de peca fique errada.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VALIDADOR = 'ferramentas/validar-banco.py'
BANCO = 'dados/pecas.json'
ESQUEMA = 'dados/esquema-banco.json'

# A peca que nasceu de contraste de catalogo: o titulo dela ("Escova Direita") nao
# tem uma palavra do eixo lateral<->central, entao ela e a que MAIS depende do
# campo novo. Se a trava so pegasse as de titulo explicito, ela estaria medindo o
# caso que nao precisa dela.
ALVO_CONTRASTE = 'wap-escova-direita-w300'
ALVO_TITULO = 'xiaomi-b106gl-bx'


def _banco(base):
    with open(os.path.join(base, BANCO), encoding='utf-8') as f:
        return json.load(f)


def _gravar_banco(base, d):
    with open(os.path.join(base, BANCO), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
        f.write('\n')


def _registro(d, pid):
    for r in d['registros']:
        if r['id'] == pid:
            return r
    raise AssertionError('%s nao esta mais no banco — a mutacao seria inerte' % pid)


def _sem_funcao_nenhuma(base):
    """O defeito original: a peca volta a declarar so o tipo, como era ate 13/09."""
    d = _banco(base)
    r = _registro(d, ALVO_CONTRASTE)
    del r['funcao']
    _gravar_banco(base, d)


def _sem_funcao_na_de_titulo(base):
    """A mesma falta, na peca cujo titulo DIZ 'Side Brush'. Tem de reprovar igual:
    a trava cobra o campo, nao a dificuldade do caso. Se ela deixasse passar
    quando o titulo e obvio, a proxima peca obvia entraria sem procedencia e a
    seguinte copiaria o vizinho."""
    d = _banco(base)
    r = _registro(d, ALVO_TITULO)
    del r['funcao']
    _gravar_banco(base, d)


def _funcao_aponta_para_fonte_que_nao_existe(base):
    """A PORTA DOS FUNDOS MAIS PROVAVEL: o campo existe, esta preenchido, e a
    fonte citada nao esta em fontes{}. Sem esta afirmacao, 'declarei de onde li'
    viraria texto livre — e texto livre nao se reconfere."""
    d = _banco(base)
    r = _registro(d, ALVO_CONTRASTE)
    r['funcao']['fonte'] = 'f-manual-que-ninguem-leu'
    _gravar_banco(base, d)


def _funcao_sem_declarado_como(base):
    """Campo preenchido pela metade: declarada_por e fonte no lugar, e nada
    transcrito. A proxima passada nao teria o que reconferir, e a tela nao teria
    o que citar."""
    d = _banco(base)
    r = _registro(d, ALVO_CONTRASTE)
    r['funcao']['declarado_como'] = ''
    _gravar_banco(base, d)


def _declarada_por_fora_do_vocabulario(base):
    """'achei parecido' escrito com todas as letras. E o defeito que esta trava
    existe para nomear, e ele tem de reprovar mesmo com a fonte certa e a
    transcricao no lugar."""
    d = _banco(base)
    r = _registro(d, ALVO_CONTRASTE)
    r['funcao']['declarada_por'] = 'parece-pelo-nome'
    _gravar_banco(base, d)


def _esquema_perde_a_lista(base):
    """PRODUZ O MUNDO PELO ESQUEMA, e nao por um registro.

    Nenhuma peca fica errada nesta mutacao — todas continuam com funcao{} certa.
    O que some e a chave `tipos_que_exigem_funcao_declarada`, que e de onde a
    trava le quais tipos cobrar. Uma trava que le a propria lista de um arquivo
    de dados aprova TUDO no dia em que a lista sumir, e aprova em silencio: o
    banco de hoje continuaria verde, e a peca seguinte entraria sem o campo sem
    uma falha. E a mesma familia do piso digitado que o teste-acentuacao carregava
    ate 13/09 — regua que depende de um dado externo tem de reprovar quando o dado
    falta, nunca cair para 'nada a cobrar'."""
    caminho = os.path.join(base, ESQUEMA)
    with open(caminho, encoding='utf-8') as f:
        e = json.load(f)
    if 'tipos_que_exigem_funcao_declarada' not in e:
        raise AssertionError('o esquema ja nao tem a chave — a mutacao seria inerte')
    del e['tipos_que_exigem_funcao_declarada']
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(e, f, ensure_ascii=False, indent=1)
        f.write('\n')


def _funcao_em_peca_que_nao_e_escova(base):
    """O caminho inverso, e ele pega o erro de quem copia registro: `funcao{}`
    num filtro. Nao e cosmetico — campo que aparece onde nao vale ensina a
    proxima pessoa que ele e decorativo, e dai ele fica vazio na escova."""
    d = _banco(base)
    r = _registro(d, 'multi-pr10205')  # filtro
    r['funcao'] = {'declarada_por': 'titulo', 'fonte': 'f-peca',
                   'declarado_como': 'o titulo diz Filtro'}
    _gravar_banco(base, d)


MUTACOES = [
    (
        'a peca de contraste volta a nao declarar a funcao',
        'o defeito original: o tipo da escova vira palpite com cara de declaracao do fabricante',
        _sem_funcao_nenhuma,
    ),
    (
        'a peca de titulo explicito perde a funcao',
        'a trava cobra o campo, nao a dificuldade do caso — senao a peca obvia entra sem procedencia',
        _sem_funcao_na_de_titulo,
    ),
    (
        'a funcao aponta para uma fonte que nao existe',
        'a porta dos fundos: sem esta afirmacao, "declarei de onde li" vira texto livre',
        _funcao_aponta_para_fonte_que_nao_existe,
    ),
    (
        'a funcao fica sem declarado_como',
        'campo pela metade: nada para reconferir na proxima passada, nada para a tela citar',
        _funcao_sem_declarado_como,
    ),
    (
        'declarada_por sai do vocabulario ("parece-pelo-nome")',
        'o palpite escrito com todas as letras tem de reprovar mesmo com fonte e transcricao certas',
        _declarada_por_fora_do_vocabulario,
    ),
    (
        'o ESQUEMA perde a lista de tipos que exigem funcao',
        'PRODUZ O MUNDO: nenhuma peca fica errada e a trava passa a aprovar tudo, em silencio',
        _esquema_perde_a_lista,
    ),
    (
        'um filtro ganha funcao{}',
        'o caminho inverso: campo onde nao vale ensina que ele e decorativo, e dai ele falta na escova',
        _funcao_em_peca_que_nao_e_escova,
    ),
]


def main():
    reprovadas = 0
    passaram = []

    print('Mutacoes deliberadas na funcao da escova — cada uma TEM que reprovar\n')

    for nome, porque, aplicar in MUTACOES:
        with tempfile.TemporaryDirectory() as tmp:
            base = os.path.join(tmp, 'ilha')
            shutil.copytree(RAIZ, base)
            try:
                aplicar(base)
            except (AssertionError, subprocess.CalledProcessError) as err:
                print('  ERRO   %-62s %s' % (nome, err))
                passaram.append(nome)
                continue

            saida = subprocess.run(['python3', os.path.join(base, VALIDADOR)],
                                   capture_output=True, text=True, cwd=base)
            if saida.returncode == 0:
                print('  PASSOU %-62s <- a trava NAO pegou' % nome)
                print('         (%s)' % porque)
                passaram.append(nome)
                continue

            linhas = [l.strip() for l in saida.stdout.splitlines()
                      if l.strip().startswith('x ')]
            print('  ok     %-62s %d invariante(s) violada(s)' % (nome, len(linhas)))
            for l in linhas[:2]:
                print('         %s' % l[:118])
            reprovadas += 1

    print('\n%d de %d mutacoes reprovadas pela bancada.' % (reprovadas, len(MUTACOES)))
    if passaram:
        print('MUTACOES QUE PASSARAM (trava faltando):')
        for n in passaram:
            print('  - %s' % n)
        sys.exit(1)


if __name__ == '__main__':
    main()
