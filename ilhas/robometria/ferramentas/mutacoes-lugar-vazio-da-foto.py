#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra o lugar vazio da foto de propósito e exige REPROVACAO.

    python3 ferramentas/mutacoes-lugar-vazio-da-foto.py

POR QUE ESTE ARQUIVO EXISTE
---------------------------
"A PROVA DE QUE UMA TRAVA REPROVA E PARTE DO BLOCO" (secao 8 do ARQUIPELAGO.md).
E aqui ela e obrigatoria por um motivo especifico, escrito na propria secao 8:

    "todo caso que o ESQUEMA permite e o banco ainda nao tem e um caso que a
     regua precisa tratar HOJE, nao no dia em que aparecer — e a maneira de
     provar que ela o trata e a mutacao que PRODUZ O MUNDO."

O esquema desta ilha declara `imagem{url,largura,altura,fonte,coletado_em,alt}`
desde o primeiro registro. O banco tem 81 registros e **zero** com `imagem.url`.
Entao toda afirmacao sobre "cartao COM foto" e, hoje, verdadeira por ausencia de
contraexemplo — que e a definicao do teste verde que nao mede nada. Quatro das
seis mutacoes abaixo PLANTAM a foto antes de aplicar o defeito.

O DEFEITO QUE ESTE ARQUIVO GUARDA, nas duas metades que o despacho do Raphael de
16/09/2026 nomeou:

1. O PAINEL VAZIO IMITAVA CARREGAMENTO. `border-radius:50%` com um lado
   transparente e a forma universal do spinner. Quem chegava na pagina nao lia
   "esta peca nao tem foto"; lia "a foto esta carregando" e, como ela nunca
   carrega, lia "este site esta quebrado". Numa ilha cujo argumento inteiro e
   procedencia, parecer quebrada custa mais do que parecer simples.

2. A R2 E A A2 EMITIAM O PAINEL SEMPRE, sem perguntar nada ao item. Nao aparecia
   porque nenhum item tinha foto: verdade por coincidencia do banco, a mesma
   familia dos dois 63 da R1 e do portao do canal brasileiro. No dia da primeira
   foto as duas escreveriam "sem foto" POR CIMA de um cartao com foto — e o
   despacho da API da Shopee, aberto no mesmo dia, e exatamente o que traz essa
   primeira foto.

A ULTIMA MUTACAO E O MUNDO SADIO e ela tem de PASSAR: planta a foto e nao mexe
em codigo nenhum. Sem ela, uma bancada que reprovasse qualquer banco com imagem
pareceria rigorosa e estaria proibindo a melhora — foi o que as quatro reguas da
escada de compra fizeram em 16/09/2026, reprovando NO AR a chegada dos links
encurtados.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CASCA = 'snippets/robometria-casca.php'
R1 = 'snippets/robometria-r1.php'
R2 = 'snippets/robometria-r2.php'
A1 = 'snippets/robometria-a1.php'
A2 = 'snippets/robometria-a2.php'

# --- a folha ---------------------------------------------------------------
FOLHA_CERTA = ('.rbm-vitrine-vazia{display:block;font-family:var(--rbm-texto);'
               'font-size:.78rem;color:var(--rbm-legenda);}\n'
               '.rbm-vitrine-vazia::after{content:"sem foto";}')
FOLHA_ANEL = ('.rbm-vitrine-vazia{display:block;width:2.4rem;height:2.4rem;'
              'border:2px solid var(--rbm-traco);border-radius:50%;'
              'border-right-color:transparent;}')
FOLHA_MUDA = ('.rbm-vitrine-vazia{display:block;font-family:var(--rbm-texto);'
              'font-size:.78rem;color:var(--rbm-legenda);}')

# --- a emissao -------------------------------------------------------------
R2_CERTA = ("""		$html .= '<span class="rbm-vitrine-foto" aria-hidden="true">'
			. ( $m['tem_imagem'] ? '' : '<span class="rbm-vitrine-vazia"></span>' )
			. '</span>';""")
R2_SEMPRE = ("""		$html .= '<span class="rbm-vitrine-foto" aria-hidden="true">'
			. '<span class="rbm-vitrine-vazia"></span>'
			. '</span>';""")

A2_CERTA = ("""		$html .= '<span class="rbm-vitrine-foto" aria-hidden="true">'
			. ( $i['tem_imagem'] ? '' : '<span class="rbm-vitrine-vazia"></span>' )
			. '</span>';""")
A2_SEMPRE = ("""		$html .= '<span class="rbm-vitrine-foto" aria-hidden="true">'
			. '<span class="rbm-vitrine-vazia"></span>'
			. '</span>';""")

R1_CERTA = ("""			. ( $i['tem_imagem'] ? '' : '<span class="rbm-vitrine-vazia"></span>' )""")
R1_SEMPRE = ("""			. '<span class="rbm-vitrine-vazia"></span>'""")

# O modelo que a R2 recomenda e que recebe a foto plantada: o xiaomi-s20 e um
# dos 6 da situacao-ancora, entao o cartao dele existe na tela. Os alvos da A2 e
# da R1 NAO sao digitados — saem dos proprios artefatos, porque as tres vitrines
# tem populacoes diferentes (a A2 so lista quem declara cobertura) e plantar a
# foto onde a regua nao olha e mutacao inerte com cara de mutacao.
MODELO_PLANTADO = 'xiaomi-s20'

FOTO = {
    'url': 'https://down-br.img.susercontent.com/file/mutacao-de-bancada.webp',
    'largura': 800,
    'altura': 800,
    'fonte': 'mutacao-de-bancada',
    'coletado_em': '2026-09-16',
    'alt': 'Foto plantada pela bancada para produzir o mundo que o banco ainda nao tem',
    'motivo_do_null': None,
}


def _troca(base, arquivo, antes, depois, quantas=1):
    caminho = os.path.join(base, arquivo)
    with open(caminho, encoding='utf-8') as f:
        texto = f.read()
    if texto.count(antes) != quantas:
        raise AssertionError('%s: esperava %d ocorrencia(s) de %r, achei %d — a mutacao '
                             'seria inerte' % (arquivo, quantas, antes[:48],
                                               texto.count(antes)))
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(texto.replace(antes, depois))


def _plantar_foto(base, arquivo, ident):
    """PRODUZ O MUNDO. Sem isto nao existe cartao com foto em lugar nenhum, e
    toda afirmacao sobre 'cartao COM foto' passa sem poder falhar."""
    caminho = os.path.join(base, arquivo)
    with open(caminho, encoding='utf-8') as f:
        banco = json.load(f)
    for r in banco['registros']:
        if r['id'] == ident:
            r['imagem'] = dict(FOTO)
            break
    else:
        raise AssertionError('%s saiu do banco — a mutacao seria inerte' % ident)
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(banco, f, ensure_ascii=False, indent=1)
        f.write('\n')


def _regerar(base, *quais):
    """A foto plantada mora no BANCO; a tela le os artefatos. Sem regerar, a
    mutacao mediria o arquivo de ontem — mutacao inerte com outro nome."""
    for qual in quais:
        saida = subprocess.run(
            ['python3', os.path.join(base, 'ferramentas/gerar-%s.py' % qual), '--gravar'],
            capture_output=True, text=True, cwd=base)
        if saida.returncode != 0:
            raise AssertionError('gerar-%s.py falhou depois da mutacao: %s'
                                 % (qual, (saida.stderr or saida.stdout)[-240:]))


# ------------------------------------------------------------------ AS MUTACOES
def _anel_volta_a_folha(base):
    """O defeito exato que estava no ar em 16/09/2026."""
    _troca(base, CASCA, FOLHA_CERTA, FOLHA_ANEL)


def _folha_fica_muda(base):
    """A metade discreta: tirar o anel sem por a frase. O painel volta a ser um
    retangulo cinza que nao diz nada — melhor que o spinner e pior que o
    conserto, e nenhuma regua de HTTP 200 veria a diferenca."""
    _troca(base, CASCA, FOLHA_CERTA, FOLHA_MUDA)


def _r2_volta_a_emitir_sempre(base):
    """PRODUZ O MUNDO e aplica o defeito: com a foto no banco, a R2 sem checagem
    escreve "sem foto" por cima de um cartao que tem foto."""
    _plantar_foto(base, 'dados/modelos-robo.json', MODELO_PLANTADO)
    _troca(base, R2, R2_CERTA, R2_SEMPRE)
    _regerar(base, 'r2')


def _a2_volta_a_emitir_sempre(base):
    _plantar_foto(base, 'dados/modelos-robo.json', _um_modelo_da_vitrine_a2())
    _troca(base, A2, A2_CERTA, A2_SEMPRE)
    _regerar(base, 'a2')


def _r1_volta_a_emitir_sempre(base):
    """A R1 ja checava — esta mutacao existe para a regua dela nao poder
    adoecer: ate 16/09/2026 a afirmacao da R1 cobrava UM painel por peca, o que
    e a mesma coisa que exigir que nenhuma peca tenha foto."""
    _plantar_foto(base, 'dados/pecas.json', _uma_peca_da_vitrine())
    _troca(base, R1, R1_CERTA, R1_SEMPRE)
    _regerar(base, 'r1')


def _mundo_sadio(base):
    """A FOTO CHEGA E NADA MAIS MUDA. Esta TEM QUE PASSAR: bancada que reprova a
    melhora e o defeito que as quatro reguas da escada de compra cometeram no
    mesmo dia, duas delas no ar."""
    _plantar_foto(base, 'dados/modelos-robo.json', MODELO_PLANTADO)
    _plantar_foto(base, 'dados/modelos-robo.json', _um_modelo_da_vitrine_a2())
    _plantar_foto(base, 'dados/pecas.json', _uma_peca_da_vitrine())
    _regerar(base, 'r1', 'r2', 'a1', 'a2')


def _uma_peca_da_vitrine():
    """A peca que a R1 serve NO CASO-ANCORA, lida do artefato e nunca digitada.

    Tem de ser a ancora, e nao uma peca qualquer: e sobre a ancora que a
    `teste-r1.php` conta os paineis. Peca de outra resposta plantaria a foto
    onde a regua nao olha — mutacao inerte com cara de mutacao."""
    with open(os.path.join(RAIZ, 'dados/r1-respostas.json'), encoding='utf-8') as f:
        resp = json.load(f)
    for i in resp['respostas'][resp['ancora']]['fabricante']:
        return i['peca']
    raise AssertionError('a ancora da R1 nao serve peca nenhuma — a mutacao seria inerte')


def _um_modelo_da_vitrine_a2():
    """O modelo que a A2 lista, lido do artefato. A A2 so lista quem declara
    cobertura, e o modelo que a R2 recomenda nao e necessariamente um deles —
    plantar no modelo errado faria a regua da A2 nao morder."""
    with open(os.path.join(RAIZ, 'dados/a2-fatos.json'), encoding='utf-8') as f:
        fatos = json.load(f)
    for i in fatos['vitrine']:
        return i['modelo']
    raise AssertionError('a vitrine da A2 esta vazia — a mutacao seria inerte')


MUTACOES = [
    (
        'o anel de carregamento volta a folha da vitrine',
        'o defeito que estava NO AR: o painel vazio imita um spinner e o site le como quebrado',
        _anel_volta_a_folha,
        ('casca',),
        True,
    ),
    (
        'a folha perde a frase e o painel fica mudo',
        'retangulo cinza que nao diz nada: melhor que o spinner, pior que o conserto, invisivel para regua de HTTP',
        _folha_fica_muda,
        ('casca',),
        True,
    ),
    (
        'a R2 volta a emitir o painel vazio SEMPRE, com foto no banco',
        'PRODUZ O MUNDO: a R2 escreve "sem foto" por cima de um cartao que tem foto',
        _r2_volta_a_emitir_sempre,
        ('casca', 'r2'),
        True,
    ),
    (
        'a A2 volta a emitir o painel vazio SEMPRE, com foto no banco',
        'PRODUZ O MUNDO: a A2 escreve "sem foto" por cima de um cartao que tem foto',
        _a2_volta_a_emitir_sempre,
        ('casca', 'a2'),
        True,
    ),
    (
        'a R1 volta a emitir o painel vazio SEMPRE, com foto no banco',
        'PRODUZ O MUNDO: a regua da R1 nao pode voltar a cobrar um painel por peca',
        _r1_volta_a_emitir_sempre,
        ('casca', 'r1'),
        True,
    ),
    (
        'MUNDO SADIO: a foto chega e nenhuma linha de codigo muda',
        'a bancada NAO pode reprovar a melhora — foi o erro das quatro reguas da escada de compra',
        _mundo_sadio,
        ('casca', 'r1', 'r2', 'a2'),
        False,
    ),
]


def _php(base, teste):
    return subprocess.run(['php', os.path.join(base, 'ferramentas/teste-%s.php' % teste), base],
                          capture_output=True, text=True, cwd=base)


CORREDORES = {
    'casca': lambda base: _php(base, 'casca'),
    'r1': lambda base: _php(base, 'r1'),
    'r2': lambda base: _php(base, 'r2'),
    'a2': lambda base: _php(base, 'a2'),
}


def main():
    certas = 0
    erradas = []

    print('Mutacoes deliberadas no lugar vazio da foto — cada uma no resultado esperado\n')

    for nome, porque, aplicar, quais, deve_reprovar in MUTACOES:
        with tempfile.TemporaryDirectory() as tmp:
            base = os.path.join(tmp, 'ilha')
            shutil.copytree(RAIZ, base)
            try:
                aplicar(base)
            except (AssertionError, subprocess.CalledProcessError) as erro:
                print('  ERRO   %-58s %s' % (nome, erro))
                erradas.append(nome)
                continue

            pegou_em = []
            falhas = []
            for qual in quais:
                saida = CORREDORES[qual](base)
                if saida.returncode != 0:
                    pegou_em.append(qual)
                    falhas += [l.strip() for l in saida.stdout.splitlines()
                               if l.strip().startswith(('FALHA', 'x ', 'REPROVADO'))]

            if deve_reprovar and not pegou_em:
                print('  PASSOU %-58s <- a trava NAO pegou' % nome)
                print('         (%s)' % porque)
                erradas.append(nome)
                continue
            if not deve_reprovar and pegou_em:
                print('  REPROVOU %-56s <- a bancada reprovou o MUNDO SADIO em: %s'
                      % (nome, ', '.join(pegou_em)))
                for l in falhas[:3]:
                    print('         %s' % l[:118])
                erradas.append(nome)
                continue

            if deve_reprovar:
                print('  ok     %-58s pegou em: %s' % (nome, ', '.join(pegou_em)))
                for l in falhas[:2]:
                    print('         %s' % l[:118])
            else:
                print('  ok     %-58s passou, como tem que passar' % nome)
            certas += 1

    print('\n%d de %d mutacoes no resultado esperado.' % (certas, len(MUTACOES)))
    if erradas:
        print('MUTACOES FORA DO ESPERADO:')
        for n in erradas:
            print('  - %s' % n)
        sys.exit(1)


if __name__ == '__main__':
    main()
