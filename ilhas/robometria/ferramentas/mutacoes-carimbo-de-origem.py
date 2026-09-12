#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra de proposito o carimbo de origem do link de afiliado e exige REPROVACAO.

    python3 ferramentas/mutacoes-carimbo-de-origem.py

POR QUE ESTE ARQUIVO EXISTE
---------------------------
"A PROVA DE QUE UMA TRAVA REPROVA E PARTE DO BLOCO" (secao 8 do ARQUIPELAGO.md).
A secao 17 do ferramentas/teste-casca.php nasceu em 12/09/2026, DEPOIS da
correcao que ela mede — entao ela passar nao prova coisa nenhuma. Nesta ilha
cinco travas ja passaram verdes medindo a si mesmas.

O DEFEITO QUE ELA MEDE, e ele estava no ar sem quebrar nada:

  `afiliado.sub_id_2` nomeia a PAGINA que levou o clique. Ate 12/09/2026 ele era
  LIDO do banco — e o banco so sabe dizer UM valor por registro: os 33 modelos
  traziam "R2" e as 18 pecas "R1". So que o mesmo modelo aparece na R2 E no
  artigo A2, e a mesma peca na R1 E no artigo A1. Os dois artigos publicavam a
  vitrine deles carimbada com o codigo da ferramenta irma.

  Nada disso aparece na tela. O campo so vira numero no dia do PRIMEIRO link de
  afiliado — e ai a medicao diz que os dois artigos nao vendem nada, com cara de
  numero conferido, e a decisao seguinte e despublicar o que estava vendendo.

O QUE UMA MUTACAO PRECISA SER AQUI. Tirar o carimbo e facil. A que importa e a
que devolve o defeito INTEIRO: o gerador voltando a ler do banco E o banco
voltando a trazer o campo — porque so os dois juntos produzem o mundo em que a
pagina publica o codigo da irma. Mutacao que so apaga o campo mede a trava do
vazio, nao a do carimbo trocado.

E toda mutacao que mexe em gerador REGERA os dados dentro da copia: sem isso ela
reprova pelo motivo errado (o arquivo de dados divergindo do gerador), e a trava
que interessa fica sem exercicio.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODELOS = 'dados/modelos-robo.json'
PECAS = 'dados/pecas.json'
TESTES = ('ferramentas/teste-casca.php',)
VALIDADOR = 'ferramentas/validar-banco.py'

GERADORES = {
    'R1': ('ferramentas/gerar-r1.py', 'dados/r1-respostas.json'),
    'R2': ('ferramentas/gerar-r2.py', 'dados/r2-respostas.json'),
    'A1': ('ferramentas/gerar-a1.py', 'dados/a1-fatos.json'),
    'A2': ('ferramentas/gerar-a2.py', 'dados/a2-fatos.json'),
}


def trocas(arquivo, pares):
    """Substituicoes exatas, cada uma obrigada a acertar um alvo unico.

    Mutacao que nao encontra o alvo edita NADA, a bancada passa, e uma bancada
    verde por mutacao que nao aconteceu e a mesma ilusao que este arquivo existe
    para desfazer.
    """
    def aplicar(base):
        caminho = os.path.join(base, arquivo)
        with open(caminho, encoding='utf-8') as f:
            corpo = f.read()
        for velho, novo in pares:
            achados = corpo.count(velho)
            if achados != 1:
                raise AssertionError(
                    'alvo da mutacao nao esta unico em %s: %d ocorrencia(s)'
                    % (arquivo, achados))
            corpo = corpo.replace(velho, novo)
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(corpo)
    return aplicar


def troca(arquivo, velho, novo):
    return trocas(arquivo, [(velho, novo)])


def devolver_ao_banco(arquivo, valor):
    """O campo volta para os registros do banco, como estava ate 12/09/2026."""
    def aplicar(base):
        caminho = os.path.join(base, arquivo)
        with open(caminho, encoding='utf-8') as f:
            doc = json.load(f)
        for r in doc['registros']:
            if isinstance(r.get('afiliado'), dict):
                r['afiliado']['sub_id_2'] = valor
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(doc, f, ensure_ascii=False, indent=2)
            f.write('\n')
    return aplicar


def regerar(base, *codigos):
    for c in codigos:
        gerador = GERADORES[c][0]
        subprocess.run([sys.executable, os.path.join(base, gerador), '--gravar'],
                       cwd=base, capture_output=True, text=True, check=True)


def _a2_volta_a_ler_o_banco(base):
    """O defeito INTEIRO do A2: gerador lendo o banco, e o banco dizendo "R2".

    E a mutacao central deste arquivo. As duas metades sozinhas sao inertes ou
    quase: com o banco limpo, `a.get("sub_id_2") or "A2"` devolve "A2" e nada
    muda; com o gerador carimbando, o campo no banco e ignorado. Juntas, o
    artigo publica os cinco modelos da vitrine dele como se o clique fosse da
    ferramenta R2 — que e exatamente o que estava no ar.
    """
    devolver_ao_banco(MODELOS, 'R2')(base)
    troca(GERADORES['A2'][0],
          '                "sub_id_1": "robometria",\n                "sub_id_2": "A2",',
          '                "sub_id_1": a.get("sub_id_1") or "robometria",\n'
          '                "sub_id_2": a.get("sub_id_2") or "A2",')(base)
    regerar(base, 'A2')


def _a1_volta_a_copiar_o_afiliado(base):
    """O mesmo defeito no A1, por outro caminho: o gerador repassava o
    `afiliado` INTEIRO do registro da peca, e a peca traz "R1"."""
    devolver_ao_banco(PECAS, 'R1')(base)
    troca(GERADORES['A1'][0],
          '"afiliado": afiliado_do_item(p, "A1"),',
          '"afiliado": p.get("afiliado", {"url": ""}),')(base)
    regerar(base, 'A1')


def _gerador_novo_copia_o_codigo_da_irma(base):
    """A R2 carimba "R1".

    Nao e hipotese: as quatro paginas desta ilha nasceram copiando a anterior, e
    a proxima vai copiar uma destas. E a mesma familia do ID do GA4 esquecido na
    casca copiada — vai ao ar FUNCIONANDO, sem uma linha de defeito visivel.
    """
    troca(GERADORES['R2'][0], '"sub_id_2": "R2",', '"sub_id_2": "R1",')(base)
    regerar(base, 'R2')


def _o_carimbo_some_do_gerador(base):
    """Sem o campo, a vitrine chega ao site sem origem nenhuma.

    Mede a metade contraria da trava: um arquivo vazio de carimbos passaria
    varrendo o nada se a bancada so comparasse os valores que encontrasse.
    """
    troca(GERADORES['A2'][0], '                "sub_id_2": "A2",\n', '')(base)
    regerar(base, 'A2')


MUTACOES = [
    (
        'o A2 volta a ler o carimbo do banco, e o banco volta a dizer "R2"',
        'e o defeito inteiro: o artigo publica a vitrine dele como se o clique fosse da ferramenta irma',
        _a2_volta_a_ler_o_banco,
        TESTES,
    ),
    (
        'o A1 volta a copiar o afiliado inteiro da peca',
        'mesmo defeito por outro caminho — o gerador repassa o registro, e o registro diz "R1"',
        _a1_volta_a_copiar_o_afiliado,
        TESTES,
    ),
    (
        'um gerador copiado carimba o codigo da pagina irma',
        'e como cada pagina desta ilha nasceu: copiando a anterior. O carimbo errado vai ao ar funcionando',
        _gerador_novo_copia_o_codigo_da_irma,
        TESTES,
    ),
    (
        'o carimbo some do gerador',
        'vitrine sem origem nenhuma: a trava do vazio, que e a metade contraria da do carimbo trocado',
        _o_carimbo_some_do_gerador,
        TESTES,
    ),
    (
        'o campo volta ao banco sem ninguem mexer em gerador',
        'campo que parece a regra e nao e, num arquivo publicado, um dia vira a regra de alguem',
        devolver_ao_banco(MODELOS, 'R2'),
        TESTES + (VALIDADOR,),
    ),
]


def main():
    reprovadas = 0
    passaram = []

    print('Mutacoes deliberadas no carimbo de origem — cada uma TEM que reprovar\n')

    for nome, porque, aplicar, testes in MUTACOES:
        with tempfile.TemporaryDirectory() as tmp:
            base = os.path.join(tmp, 'ilha')
            shutil.copytree(RAIZ, base)
            try:
                aplicar(base)
            except (AssertionError, subprocess.CalledProcessError) as erro:
                print('  ERRO   %-62s %s' % (nome, erro))
                passaram.append(nome)
                continue

            falhas = []
            pegou_em = []
            for teste in testes:
                if teste.endswith('.py'):
                    cmd = [sys.executable, os.path.join(base, teste), base]
                else:
                    cmd = ['php', os.path.join(base, teste), base]
                saida = subprocess.run(cmd, capture_output=True, text=True)
                if saida.returncode != 0:
                    pegou_em.append(os.path.basename(teste))
                    falhas += [l.strip() for l in saida.stdout.splitlines()
                               if l.strip().startswith(('FALHA', 'ERRO'))]

            if not pegou_em:
                print('  PASSOU %-62s <- a trava NAO pegou' % nome)
                print('         (%s)' % porque)
                passaram.append(nome)
                continue

            print('  ok     %-62s %d falha(s) em %s'
                  % (nome, len(falhas), ', '.join(pegou_em)))
            for l in falhas[:2]:
                print('         %s' % l[:120])
            reprovadas += 1

    print('\n%d de %d mutacoes reprovadas pela bancada.' % (reprovadas, len(MUTACOES)))
    if passaram:
        print('MUTACOES QUE PASSARAM (trava faltando):')
        for n in passaram:
            print('  - %s' % n)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
