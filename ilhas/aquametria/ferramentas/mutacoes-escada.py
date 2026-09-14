#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra DE PROPOSITO a escada da secao 25 e exige que ela seja pega.

    python3 ferramentas/mutacoes-escada.py

Sao dois portoes, e cada mutacao declara qual deles deveria pega-la:

  - `validar-produtos.py` mede o BANCO, regra a regra (V24 a V27);
  - `teste-escada-compra.py` mede o que o validador nao mede — se os numeros do
    relatorio sao CONTADOS, se a escada declarada e a da 25.1 inteira, e se o
    gerador da busca e idempotente.

E a exigencia aqui e mais dura que a das outras baterias desta ilha: nao basta o
portao ficar vermelho, ele tem de ficar vermelho PELA REGRA QUE A MUTACAO NOMEIA.
Defeito pego por outra regra prova que alguma trava existe, nao que ESTA existe —
e o dia em que a regra nomeada sumir, a bateria continuaria verde por causa da
vizinha. Foi por isso que a bateria da dimensao, em 13/09/2026, passou a exigir o
portao nomeado; aqui a exigencia desce um nivel, ate o id da regra.

A MUTACAO QUE MAIS IMPORTA E A 10, e ela nao estraga registro nenhum: tira do
ESQUEMA o termo de contexto de uma entidade. Sem a trava, o gerador passaria a
compor busca so por marca e o banco de hoje continuaria verde — a 25.3 mostra o
que isso traz para dentro do cartao: a JBL de caixa de som e a "Aquario" de
roteador. E a mesma familia da mutacao que a Robometria escreveu no mesmo dia,
quando tirou a lista de tipos de dentro da regua.

Cada mutacao roda num repositorio COPIADO.
"""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

BANCO = 'ferramentas/validar-produtos.py'
ESCADA = 'ferramentas/teste-escada-compra.py'

ESQUEMA = 'dados/esquema-produtos.json'
MIDIA = 'dados/produtos-midia.json'

COM_FICHA = 'seachem-matrix-1l'      # tem url de afiliado
SEM_FICHA = 'jbl-micromec-1l'        # plataforma null


def no_produto(arquivo, id_produto, mudanca):
    """Edita o bloco `afiliado` de UM registro."""
    def aplicar(base: Path):
        caminho = base / arquivo
        d = json.loads(caminho.read_text(encoding='utf-8'))
        for p in d['produtos']:
            if p.get('id') == id_produto:
                mudanca(p.setdefault('afiliado', {}))
                break
        else:
            raise SystemExit('ALVO SUMIU: nenhum produto %r em %s' % (id_produto, arquivo))
        caminho.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return aplicar


def no_esquema(mudanca):
    def aplicar(base: Path):
        caminho = base / ESQUEMA
        d = json.loads(caminho.read_text(encoding='utf-8'))
        mudanca(d)
        caminho.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return aplicar


def busca_de(chave):
    return 'https://shopee.com.br/search?keyword=' + chave.replace(' ', '%20')


MUTACOES = [
    (BANCO, 'V24', 'o link declara um degrau que nao existe na escada da 25.1',
     no_produto(MIDIA, COM_FICHA, lambda a: a.update({'degrau': 7}))),

    (BANCO, 'V24', 'o link fica sem degrau E sem a causa que apaga o degrau — a excecao vira regra',
     no_produto(MIDIA, COM_FICHA, lambda a: a.update({'motivo_sem_url_produto': None}))),

    (BANCO, 'V24', 'produto SEM link ganha degrau: sem escolha nao ha degrau em que parar',
     no_produto(MIDIA, SEM_FICHA, lambda a: a.update({'degrau': 3}))),

    (BANCO, 'V25', 'o link de afiliado perde a url crua e o motivo de nao ter: saude inconferivel em silencio',
     no_produto(MIDIA, COM_FICHA,
                lambda a: a.update({'motivo_sem_url_produto': None, 'degrau': 3}))),

    (BANCO, 'V25', 'nasce um piso e ninguem guarda a busca crua: palavra-chave que morre nao avisa',
     no_produto(MIDIA, SEM_FICHA,
                lambda a: a.update({'url_busca': 'https://s.shopee.com.br/mutacao',
                                    'url_busca_produto': None}))),

    (BANCO, 'V26', 'a palavra-chave da busca some: o piso que a maquina fabrica sozinha deixa de existir',
     no_produto(MIDIA, SEM_FICHA, lambda a: a.update({'url_busca_produto': None}))),

    (BANCO, 'V26', 'o item fica sem piso e sem dizer o que trava o piso: divida que ninguem consegue contar',
     no_produto(MIDIA, SEM_FICHA, lambda a: a.update({'motivo_sem_url_busca': None}))),

    (BANCO, 'V27', 'A ARMADILHA DA 25.3: a busca perde o contexto e vira marca pura',
     no_produto(MIDIA, SEM_FICHA, lambda a: a.update({'url_busca_produto': busca_de('JBL')}))),

    (BANCO, 'V27', 'a busca deixa de sair da base declarada e aponta para outro buscador',
     no_produto(MIDIA, SEM_FICHA,
                lambda a: a.update({'url_busca_produto':
                                    'https://www.google.com/search?q=JBL%20MicroMec'}))),

    (BANCO, 'V27', 'A QUE MAIS IMPORTA: o ESQUEMA perde o termo de contexto de uma entidade',
     no_esquema(lambda d: d['afiliado']['escada_de_compra']
                ['termo_de_contexto_por_entidade'].pop('midia'))),

    (ESCADA, None, 'a escada do esquema perde um degrau da 25.1',
     no_esquema(lambda d: d['afiliado']['escada_de_compra']['degraus'].pop())),

    (ESCADA, None, 'um degrau e rebatizado, e o nome deixa de dizer que loja e aquela',
     no_esquema(lambda d: d['afiliado']['escada_de_compra']['degraus'][0]
                .update({'nome': 'shopee'}))),

    (ESCADA, None, 'O NUMERO DIGITADO: o relatorio passa a jurar que o piso existe',
     lambda base: (base / BANCO).write_text(
         (base / BANCO).read_text(encoding='utf-8').replace(
             'escada["com_piso"], total))', '78, total))'), encoding='utf-8')),

    # ---- A ESCADA DENTRO DO BANCO, nos campos que nasceram em 14/09/2026 ----

    (BANCO, 'V24', 'o item declara o degrau 4 e nao tem piso nenhum: saida de compra que nao existe',
     no_produto(MIDIA, SEM_FICHA, lambda a: a.update({'url_busca_produto': None, 'degrau': 4}))),

    (BANCO, 'V24', 'o item com FICHA e rebaixado para o degrau 4: a escada para no primeiro que serve',
     no_produto(MIDIA, COM_FICHA, lambda a: a.update({'degrau': 4}))),

    (BANCO, 'V25', 'a bandeira intestavel MENTE: o link sem url crua se declara conferivel',
     no_produto(MIDIA, COM_FICHA, lambda a: a.update({'intestavel': False}))),

    (BANCO, 'V25', 'a bandeira intestavel mente ao CONTRARIO: item sem ficha nenhuma se declara inconferivel',
     no_produto(MIDIA, SEM_FICHA, lambda a: a.update({'intestavel': True}))),

    # ---- A ESCADA NA TELA, que e a metade que faltava ate 14/09/2026 --------
    #
    # As quatro abaixo nao tocam no banco: elas quebram o SNIPPET, que e onde a
    # divida morava. O banco estava certo desde 13/09 — a palavra-chave da busca
    # escrita nos 78 itens — e a pagina continuava servindo "link de loja em
    # breve" porque nenhum portao media o que o leitor recebe.

    # A PRIMEIRA ESCRITA DESTA MUTACAO PASSOU, e o defeito era dela e nao do
    # portao: ela trocava o texto do ramo `else` de vitrine_cartao_html(), que
    # so roda quando o item chega sem ficha E sem piso — um mundo que o banco de
    # hoje nao produz. Mutacao que nao muda o HTML servido nao mede nada, do
    # mesmo jeito que regua escrita para um mundo que nunca aconteceu nasce sem
    # poder falhar (secao 8 do ARQUIPELAGO.md). Esta versao PRODUZ o mundo: ela
    # devolve a frase proibida ao selo do cartao que sai pelo piso, que e o ramo
    # que 39 dos 78 itens percorrem.
    (ESCADA, None, 'A FRASE PROIBIDA VOLTA ao selo do cartao que sai pelo piso',
     lambda base: (base / 'snippets/aquametria-calculadora-vazao.php').write_text(
         (base / 'snippets/aquametria-calculadora-vazao.php').read_text(encoding='utf-8').replace(
             "'selo'     => $paga ? 'busca patrocinada' : 'busca na Shopee, sem comissão',",
             "'selo'     => 'link de loja em breve',", 1),
         encoding='utf-8')),

    (ESCADA, None, 'A URL INVENTADA: o cartao passa a apontar para um endereco que o banco nao conhece',
     lambda base: (base / 'snippets/aquametria-calculadora-vazao.php').write_text(
         (base / 'snippets/aquametria-calculadora-vazao.php').read_text(encoding='utf-8').replace(
             "'url'      => $p['busca'],",
             "'url'      => 'https://shopee.com.br/search?keyword=aquario',", 1),
         encoding='utf-8')),

    (ESCADA, None, 'O PISO SOME DO CATALOGO do snippet e o cartao volta a ser <div> sem destino',
     lambda base: (base / 'snippets/aquametria-calculadora-midia.php').write_text(
         (base / 'snippets/aquametria-calculadora-midia.php').read_text(encoding='utf-8').replace(
             "'busca' => 'https://shopee.com.br/search?keyword=JBL",
             "'busca' => null, 'busca_nao' => 'https://shopee.com.br/search?keyword=JBL", 1),
         encoding='utf-8')),

    (ESCADA, None, 'A MENTIRA DE MAQUINA: a busca CRUA vai para a tela marcada como patrocinada',
     lambda base: (base / 'snippets/aquametria-calculadora-aquecedor.php').write_text(
         (base / 'snippets/aquametria-calculadora-aquecedor.php').read_text(encoding='utf-8').replace(
             "return $compra['afiliado'] ? 'sponsored noopener' : 'nofollow noopener';",
             "return 'sponsored noopener';", 1),
         encoding='utf-8')),

    (ESCADA, None, 'o cartao COM ficha perde a linha discreta do piso, e volta a morrer com o anuncio',
     lambda base: (base / 'snippets/aquametria-calculadora-iluminacao.php').write_text(
         (base / 'snippets/aquametria-calculadora-iluminacao.php').read_text(encoding='utf-8').replace(
             "\t\t$h .= aquametria_c15_vitrine_piso_html( $p );\n", "", 1),
         encoding='utf-8')),

    (ESCADA, None, 'o gerador da busca deixa de ser idempotente e move o piso a cada passada',
     lambda base: (base / 'ferramentas/gerar-busca-de-produto.py').write_text(
         (base / 'ferramentas/gerar-busca-de-produto.py').read_text(encoding='utf-8').replace(
             'return " ".join(p for p in partes if p)',
             'import random; return " ".join(p for p in partes if p) + str(random.random())'),
         encoding='utf-8')),
]


def rodar(base: Path, portao: str):
    r = subprocess.run([sys.executable, str(base / portao), str(base)],
                       capture_output=True, text=True, cwd=str(base))
    return r.returncode, r.stdout + r.stderr


def main():
    for portao in (BANCO, ESCADA):
        codigo, saida = rodar(RAIZ, portao)
        if codigo != 0:
            print('O portao %s ja esta VERMELHO no repositorio limpo. Conserte antes de mutar.'
                  % portao)
            print(saida[-2000:])
            return 1
        print('repositorio limpo: %s verde' % portao)
    print()

    reprovou = 0
    for i, (portao, regra, nome, aplicar) in enumerate(MUTACOES, 1):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp) / 'ilha'
            shutil.copytree(RAIZ, base, ignore=shutil.ignore_patterns('node_modules', '.git'))
            aplicar(base)
            codigo, saida = rodar(base, portao)
            marca = Path(portao).name
            if codigo == 0:
                print('  %2d. PASSOU (ERRADO, %s nao viu) — %s' % (i, marca, nome))
                continue
            if regra and ('[%s]' % regra) not in saida:
                # Vermelho pela regra errada e o defeito que esta bateria existe
                # para pegar: no dia em que a regra nomeada sumir, a vizinha
                # manteria a bateria verde e ninguem saberia.
                print('  %2d. VERMELHO PELA REGRA ERRADA (esperava %s) — %s' % (i, regra, nome))
                continue
            reprovou += 1
            print('  %2d. REPROVOU (certo, por %s%s) — %s'
                  % (i, marca, ' ' + regra if regra else '', nome))
            for l in [x.strip() for x in saida.splitlines()
                      if x.strip().startswith(('FALHA', 'ERRO  ['))][:1]:
                print('        %s' % l[:150])

    print('\n%d de %d mutacoes reprovadas pela regra que as nomeia' % (reprovou, len(MUTACOES)))
    return 0 if reprovou == len(MUTACOES) else 1


if __name__ == '__main__':
    sys.exit(main())
