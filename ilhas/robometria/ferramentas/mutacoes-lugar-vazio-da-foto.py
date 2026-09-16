#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra o painel da foto de propósito e exige REPROVACAO.

    python3 ferramentas/mutacoes-lugar-vazio-da-foto.py

POR QUE ESTE ARQUIVO EXISTE
---------------------------
"A PROVA DE QUE UMA TRAVA REPROVA E PARTE DO BLOCO" (secao 8 do ARQUIPELAGO.md).

Ele nasceu de manha em 16/09/2026, quando o banco tinha 81 registros e ZERO
foto, e por isso as quatro primeiras mutacoes PLANTAVAM a imagem antes de
aplicar o defeito — a secao 8 manda tratar hoje o caso que o esquema permite e
o banco ainda nao tem. **A tarde do mesmo dia a Open API da Shopee trouxe 27
fotos de verdade, e o plantio deixou de ser necessario**: o banco passou a ter
os DOIS mundos ao mesmo tempo, 27 com foto e 46 sem. Este arquivo foi reescrito
para medir o mundo real em vez do plantado — plantar o que ja existe seria
mutacao que nao morde, com outro nome.

O QUE ELE GUARDA, e sao tres defeitos de familias diferentes:

1. O PAINEL VAZIO IMITAVA CARREGAMENTO. `border-radius:50%` com um lado
   transparente e a forma universal do spinner. Quem chegava na pagina nao lia
   "esta peca nao tem foto"; lia "a foto esta carregando" e, como ela nunca
   carrega, lia "este site esta quebrado".

2. AS QUATRO FERRAMENTAS DECIDIAM SOZINHAS. Ate 16/09 cada uma escrevia o
   painel por conta propria, e foi assim que a R2 e a A2 passaram meses
   emitindo o aviso SEM perguntar nada ao item — invisivel porque nenhum item
   tinha foto. Agora a decisao mora numa funcao so, na casca, e as mutacoes
   cobram que continue morando.

3. FOTO SEM DIMENSAO FAZ A PAGINA PULAR. `width` e `height` no HTML sao regra
   da secao 6, e a bancada mede as duas direcoes: sem dimensao a foto NAO entra.

A ULTIMA MUTACAO E O MUNDO SADIO e ela tem de PASSAR: o banco muda de
composicao (uma peca com foto perde a foto, uma sem foto ganha) e nenhuma linha
de codigo se mexe. Sem ela, uma bancada que reprovasse qualquer mudanca de
banco pareceria rigorosa e estaria proibindo a melhora — foi o que CINCO reguas
desta ilha fizeram em 16/09/2026, quatro de manha com os links encurtados e uma
a tarde com a chegada das fichas de produto.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CASCA = 'snippets/robometria-casca.php'
R2 = 'snippets/robometria-r2.php'

# --- a folha ---------------------------------------------------------------
FOLHA_CERTA = ('.rbm-vitrine-vazia{display:block;font-family:var(--rbm-texto);'
               'font-size:.78rem;color:var(--rbm-legenda);}\n'
               '.rbm-vitrine-vazia::after{content:"sem foto";}')
FOLHA_ANEL = ('.rbm-vitrine-vazia{display:block;width:2.4rem;height:2.4rem;'
              'border:2px solid var(--rbm-traco);border-radius:50%;'
              'border-right-color:transparent;}')
FOLHA_MUDA = ('.rbm-vitrine-vazia{display:block;font-family:var(--rbm-texto);'
              'font-size:.78rem;color:var(--rbm-legenda);}')

# --- o painel, na casca ----------------------------------------------------
PORTAO_CERTO = """	if ( '' === $url || $largura < 1 || $altura < 1 ) {"""
PORTAO_SEMPRE_VAZIO = """	if ( true ) {"""
PORTAO_SEM_DIMENSAO = """	if ( '' === $url ) {"""

DIMENSAO_CERTA = """		. ' width="' . $largura . '" height="' . $altura . '"'"""
DIMENSAO_FORA = """		. ''"""

# --- a ferramenta voltando a decidir sozinha -------------------------------
R2_CERTA = """		$html .= robometria_casca_painel_da_foto( isset( $m['imagem'] ) ? $m['imagem'] : null );"""
R2_SOZINHA = ("""		$html .= '<span class="rbm-vitrine-foto" aria-hidden="true">'"""
              """ . '<span class="rbm-vitrine-vazia"></span></span>';""")


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


def _regerar(base, *quais):
    for qual in quais:
        saida = subprocess.run(
            ['python3', os.path.join(base, 'ferramentas/gerar-%s.py' % qual), '--gravar'],
            capture_output=True, text=True, cwd=base)
        if saida.returncode != 0:
            raise AssertionError('gerar-%s.py falhou depois da mutacao: %s'
                                 % (qual, (saida.stderr or saida.stdout)[-240:]))


def _um_de_cada_mundo():
    """Um registro COM foto e um SEM, lidos do banco e nunca digitados.

    Id digitado aqui vira mutacao inerte no dia em que o banco mudar — e o
    banco desta ilha muda toda coleta.
    """
    com, sem = None, None
    for caminho in ('dados/modelos-robo.json', 'dados/pecas.json'):
        with open(os.path.join(RAIZ, caminho), encoding='utf-8') as f:
            doc = json.load(f)
        for r in doc['registros']:
            if r.get('status') != 'publicavel':
                continue
            tem = bool((r.get('imagem') or {}).get('url'))
            if tem and not com:
                com = (caminho, r['id'])
            if not tem and not sem:
                sem = (caminho, r['id'])
    if not com or not sem:
        raise AssertionError('o banco nao tem os dois mundos (com e sem foto) — '
                             'a mutacao do mundo sadio seria inerte')
    return com, sem


# ------------------------------------------------------------------ AS MUTACOES
def _anel_volta_a_folha(base):
    """O defeito exato que estava no ar as 15h de 16/09/2026."""
    _troca(base, CASCA, FOLHA_CERTA, FOLHA_ANEL)


def _folha_fica_muda(base):
    """A metade discreta: tirar o anel sem por a frase. O painel volta a ser um
    retangulo cinza que nao diz nada — melhor que o spinner e pior que o
    conserto, e nenhuma regua de HTTP 200 veria a diferenca."""
    _troca(base, CASCA, FOLHA_CERTA, FOLHA_MUDA)


def _painel_ignora_a_foto(base):
    """O defeito da R2 e da A2, agora concentrado na casca — e por isso pior:
    uma linha so escreveria "sem foto" por cima das 27 fotos do banco, nas
    quatro paginas de uma vez."""
    _troca(base, CASCA, PORTAO_CERTO, PORTAO_SEMPRE_VAZIO)


def _foto_entra_sem_dimensao(base):
    """O portao do banco ja exige largura e altura; este e o outro lado. Sem a
    checagem aqui, um banco afrouxado poria <img> sem dimensao no ar e a pagina
    passaria a pular em toda ferramenta."""
    _troca(base, CASCA, PORTAO_CERTO, PORTAO_SEM_DIMENSAO)


def _atributos_de_dimensao_somem(base):
    """A foto entra e os atributos nao saem no HTML. E a forma mais discreta do
    mesmo defeito: o portao aprova, o banco tem os numeros, e a pagina pula
    assim mesmo porque ninguem os escreveu."""
    _troca(base, CASCA, DIMENSAO_CERTA, DIMENSAO_FORA)


def _r2_volta_a_decidir_sozinha(base):
    """Quatro copias da mesma decisao e como a ilha perde tres delas."""
    _troca(base, R2, R2_CERTA, R2_SOZINHA)
    _regerar(base, 'r2')


def _mundo_sadio(base):
    """O BANCO MUDA DE COMPOSICAO E NENHUMA LINHA DE CODIGO SE MEXE.

    Esta TEM QUE PASSAR. Uma peca com foto perde a foto (a Shopee tira o
    anuncio do ar, que e o que anuncio de vendedor faz) e uma sem foto ganha
    uma (a proxima coleta casa). Bancada que reprova qualquer um dos dois
    movimentos e bancada amarrada ao banco de hoje.
    """
    (arq_com, id_com), (arq_sem, id_sem) = _um_de_cada_mundo()

    for arquivo, ident, ganha in ((arq_com, id_com, False), (arq_sem, id_sem, True)):
        caminho = os.path.join(base, arquivo)
        with open(caminho, encoding='utf-8') as f:
            doc = json.load(f)
        for r in doc['registros']:
            if r['id'] != ident:
                continue
            if ganha:
                r['imagem'] = {
                    'url': 'https://cf.shopee.com.br/file/mutacao-de-bancada',
                    'largura': 800, 'altura': 800, 'fonte': 'shopee-api',
                    'coletado_em': '2026-09-16',
                    'alt': 'Foto plantada pela bancada, para o mundo sadio ter os dois lados',
                    'motivo_do_null': None,
                }
            else:
                r['imagem'] = {
                    'url': None, 'largura': None, 'altura': None, 'fonte': None,
                    'coletado_em': None, 'alt': None,
                    'motivo_do_null': 'Anuncio saiu do ar; a bancada tirou a foto de proposito.',
                }
            break
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(doc, f, ensure_ascii=False, indent=1)
            f.write('\n')

    # As contagens do cabecalho sao conferidas por validar-banco.py, e mudar o
    # banco sem mexer nelas seria reprovar por outro motivo — o que faria esta
    # mutacao "passar no teste errado".
    for arquivo in set((arq_com, arq_sem)):
        caminho = os.path.join(base, arquivo)
        with open(caminho, encoding='utf-8') as f:
            doc = json.load(f)
        pub = [r for r in doc['registros'] if r['status'] == 'publicavel']
        doc['contagem']['itens_com_foto'] = sum(
            1 for r in pub if (r.get('imagem') or {}).get('url'))
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(doc, f, ensure_ascii=False, indent=1)
            f.write('\n')

    _regerar(base, 'r1', 'r2', 'a1', 'a2')


MUTACOES = [
    ('o anel de carregamento volta a folha da vitrine',
     'o defeito que estava NO AR: o painel vazio imita um spinner e o site le como quebrado',
     _anel_volta_a_folha, ('casca',), True),
    ('a folha perde a frase e o painel fica mudo',
     'retangulo cinza que nao diz nada: invisivel para regua de HTTP 200',
     _folha_fica_muda, ('casca',), True),
    ('o painel da casca ignora a foto e emite o aviso SEMPRE',
     'uma linha escreveria "sem foto" por cima das fotos do banco, nas quatro paginas',
     _painel_ignora_a_foto, ('casca',), True),
    ('foto sem largura/altura passa a entrar como <img>',
     'a pagina pula quando a imagem carrega — secao 6, e nenhuma regua de HTTP veria',
     _foto_entra_sem_dimensao, ('casca',), True),
    ('os atributos width/height somem do HTML',
     'a forma discreta: o portao aprova, o banco tem os numeros, e ninguem os escreve',
     _atributos_de_dimensao_somem, ('casca',), True),
    ('a R2 volta a montar o painel por conta propria',
     'quatro copias da mesma decisao e como a ilha perde tres delas',
     _r2_volta_a_decidir_sozinha, ('casca',), True),
    ('MUNDO SADIO: o banco troca de composicao e o codigo nao muda',
     'a bancada NAO pode reprovar a melhora — cinco reguas desta ilha ja fizeram isso',
     _mundo_sadio, ('casca', 'r1', 'r2', 'a2', 'banco'), False),
]


def _php(base, teste):
    return subprocess.run(['php', os.path.join(base, 'ferramentas/teste-%s.php' % teste), base],
                          capture_output=True, text=True, cwd=base)


CORREDORES = {
    'casca': lambda base: _php(base, 'casca'),
    'r1': lambda base: _php(base, 'r1'),
    'r2': lambda base: _php(base, 'r2'),
    'a2': lambda base: _php(base, 'a2'),
    'banco': lambda base: subprocess.run(
        ['python3', os.path.join(base, 'ferramentas/validar-banco.py'), base],
        capture_output=True, text=True, cwd=base),
}


def main():
    certas = 0
    erradas = []

    print('Mutacoes deliberadas no painel da foto — cada uma no resultado esperado\n')

    for nome, porque, aplicar, quais, deve_reprovar in MUTACOES:
        with tempfile.TemporaryDirectory() as tmp:
            base = os.path.join(tmp, 'ilha')
            shutil.copytree(RAIZ, base)
            try:
                aplicar(base)
            except (AssertionError, subprocess.CalledProcessError) as erro:
                print('  ERRO   %-56s %s' % (nome, erro))
                erradas.append(nome)
                continue

            pegou_em, falhas = [], []
            for qual in quais:
                saida = CORREDORES[qual](base)
                if saida.returncode != 0:
                    pegou_em.append(qual)
                    falhas += [l.strip() for l in saida.stdout.splitlines()
                               if l.strip().startswith(('FALHA', 'x ', 'REPROVADO'))]

            if deve_reprovar and not pegou_em:
                print('  PASSOU %-56s <- a trava NAO pegou' % nome)
                print('         (%s)' % porque)
                erradas.append(nome)
                continue
            if not deve_reprovar and pegou_em:
                print('  REPROVOU %-54s <- reprovou o MUNDO SADIO em: %s'
                      % (nome, ', '.join(pegou_em)))
                for l in falhas[:3]:
                    print('         %s' % l[:118])
                erradas.append(nome)
                continue

            if deve_reprovar:
                print('  ok     %-56s pegou em: %s' % (nome, ', '.join(pegou_em)))
                for l in falhas[:2]:
                    print('         %s' % l[:116])
            else:
                print('  ok     %-56s passou, como tem que passar' % nome)
            certas += 1

    print('\n%d de %d mutacoes no resultado esperado.' % (certas, len(MUTACOES)))
    if erradas:
        print('MUTACOES FORA DO ESPERADO:')
        for n in erradas:
            print('  - %s' % n)
        sys.exit(1)


if __name__ == '__main__':
    main()
