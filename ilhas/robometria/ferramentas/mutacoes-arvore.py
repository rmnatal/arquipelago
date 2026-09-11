#!/usr/bin/env python3
"""Quebra de proposito a arvore da casca 1.3.0 e exige que a bancada REPROVE.

    python3 ferramentas/mutacoes-arvore.py

POR QUE ESTE ARQUIVO EXISTE
---------------------------
"A PROVA DE QUE UMA TRAVA REPROVA E PARTE DO BLOCO" (PROMPT.md desta ilha, e
secao 8 do ARQUIPELAGO.md). Trava que nunca foi vista reprovando e trava nao
medida — e nesta ilha cinco travas ja passaram verdes medindo a si mesmas.

Cada mutacao e uma copia da arvore inteira num diretorio temporario, com UMA
edicao cirurgica, e a bancada tem que sair com codigo diferente de zero. Rodamos
teste-arvore.php E teste-casca.php: a arvore e os numeros da tela mudaram no
mesmo bloco, e uma mutacao que so um dos dois pega continua sendo uma mutacao
pega.

MUTACAO INERTE NAO VALE, e tres foram reescritas por isso enquanto este arquivo
nascia: mexer no teto de irmas nao muda uma linha do que o site serve hoje
(nenhuma pagina tem cinco irmas candidatas), entao ela so morde porque o teste
FABRICA a borda. Mutacao que nao muda nada e teste verde que nao mede nada, do
outro lado do espelho.
"""

import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASCA = 'snippets/robometria-casca.php'
R2 = 'snippets/robometria-r2.php'
ARVORE = 'ARVORE.md'
FATOS = 'dados/casca-fatos.json'
TESTES = ('ferramentas/teste-arvore.php', 'ferramentas/teste-casca.php')


def trocas(arquivo, pares):
    """Substituicoes exatas, cada uma obrigada a acertar um alvo unico.

    Exigir unicidade nao e preciosismo: mutacao que nao encontra o alvo edita
    NADA e o teste passa — e um teste verde por mutacao que nao aconteceu e a
    mesma ilusao que este arquivo existe para desfazer.
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


MUTACOES = [
    (
        'a trilha nao sai mais antes do H1',
        'sem trilha a secao 16.3 nao existe, e a pagina nao diz ao leitor onde ele esta',
        troca(CASCA,
              "\tif ( 'core/post-title' !== $nome || robometria_casca_trilha_impressa() ) {",
              "\tif ( true || 'core/post-title' !== $nome || robometria_casca_trilha_impressa() ) {"),
    ),
    (
        'a trilha sai DEPOIS do H1',
        '"abaixo do header" e antes do titulo; depois dele a trilha vira rodape da cabeca',
        troca(CASCA,
              "\trobometria_casca_trilha_impressa( true );\n\n\treturn $trilha . $conteudo;",
              "\trobometria_casca_trilha_impressa( true );\n\n\treturn $conteudo . $trilha;"),
    ),
    (
        'a home entra na arvore e ganha trilha',
        'a 16.3 diz que na home nao ha breadcrumb — ela e o primeiro degrau, nao um degrau',
        trocas(CASCA, [
            ("\tif ( '' === $slug || 'inicio' === $slug ) {\n\t\treturn array();",
             "\tif ( '' === $slug ) {\n\t\treturn array();"),
            ("\treturn array( 'metodologia', 'sobre', 'divulgacao-de-afiliados' );",
             "\treturn array( 'inicio', 'metodologia', 'sobre', 'divulgacao-de-afiliados' );"),
        ]),
    ),
    (
        'o degrau da secao inexistente vira link',
        'link para pagina que nao existe e 404 no ar — a ilha nasceu com essa trava',
        troca(CASCA,
              "\t\t\t\t'url'    => robometria_casca_url_se_existir( $n1_slug ),",
              "\t\t\t\t'url'    => home_url( '/' . $n1_slug . '/' ),"),
    ),
    (
        'o degrau atual perde o aria-current',
        'sem ele, leitor de tela nao sabe qual degrau e a pagina aberta',
        troca(CASCA,
              "\t\t\t$html .= '<span aria-current=\"page\">' . esc_html( $d['rotulo'] ) . '</span>';",
              "\t\t\t$html .= '<span>' . esc_html( $d['rotulo'] ) . '</span>';"),
    ),
    (
        'o JSON-LD passa a carregar o degrau sem endereco',
        'ListItem do meio sem item invalida a lista inteira: o schema publicaria MENOS',
        troca(CASCA,
              "\tforeach ( $degraus as $d ) {\n\t\tif ( '' === $d['url'] ) {\n\t\t\tcontinue;\n\t\t}\n\t\t$pos++;",
              "\tforeach ( $degraus as $d ) {\n\t\t$pos++;"),
    ),
    (
        'o teto de irmas vira quarenta',
        'so a borda FABRICADA pega esta: com duas ferramentas no ar, nada muda na tela',
        troca(CASCA,
              "\t\treturn array_slice( $irmas, 0, 4 );",
              "\t\treturn array_slice( $irmas, 0, 40 );"),
    ),
    (
        'a pagina vira irma dela mesma',
        'cluster que aponta para si nao passa autoridade nenhuma e confunde o leitor',
        troca(CASCA,
              "\t\t\tif ( empty( $f['slug'] ) || $f['slug'] === $slug ) {\n\t\t\t\tcontinue;\n\t\t\t}\n\t\t\tif ( ! isset( $f['estado'] ) || 'publicada' !== $f['estado'] ) {",
              "\t\t\tif ( empty( $f['slug'] ) ) {\n\t\t\t\tcontinue;\n\t\t\t}\n\t\t\tif ( ! isset( $f['estado'] ) || 'publicada' !== $f['estado'] ) {"),
    ),
    (
        'o numero da frase de mae volta a ser digitado',
        'e a cicatriz do cartao que dizia zero: numero de tela nasce contado, nunca escrito',
        troca(CASCA,
              "\t\t$quantas = robometria_casca_conta_ferramentas_no_ar();",
              "\t\t$quantas = 3;"),
    ),
    (
        'a frase de mae sai tambem onde a mae nao existe',
        'frase apontando para /guias/ hoje seria um link morto no meio do cluster',
        trocas(CASCA, [
            ("\t$url_mae = ( '' !== $n1_slug ) ? robometria_casca_url_se_existir( $n1_slug ) : '';",
             "\t$url_mae = ( '' !== $n1_slug ) ? home_url( '/' . $n1_slug . '/' ) : '';"),
            ("\tif ( '' !== $url_mae && robometria_casca_mae_das_ferramentas() === $n1_slug ) {",
             "\tif ( '' !== $url_mae ) {"),
        ]),
    ),
    (
        'a ferramenta de succao volta a linkar so o guia da outra',
        'e o defeito que a varredura de links achou: o par da 16.4d aberto de um lado so',
        troca(R2,
              "\t$html .= '<p>' . ( function_exists( 'robometria_casca_link_html' )\n\t\t? robometria_casca_link_html( 'quantos-m2-o-robo-aspirador-limpa-por-carga', 'Quantos m² um robô aspirador limpa por carga' )",
              "\t$html .= '<p>' . ( function_exists( 'robometria_casca_link_html' )\n\t\t? robometria_casca_link_html( 'filtro-universal-de-robo-aspirador', 'Quantos m² um robô aspirador limpa por carga' )"),
    ),
    (
        'o codigo ganha uma categoria que o documento nao tem',
        'documento e codigo mantidos em dois lugares divergem em silencio',
        troca(CASCA,
              "\t\t'guias-pecas'           => array( 'guias',   'Peças' ),",
              "\t\t'guias-pecas'           => array( 'guias',   'Peças' ),\n\t\t'guias-manutencao'      => array( 'guias',   'Manutenção' ),"),
    ),
    (
        'o documento ganha uma categoria que o codigo nao tem',
        'mesma divergencia, do outro lado — o documento e o que a proxima execucao le',
        troca(ARVORE,
              "| `/guias/succao/` | `/guias/` | os textos sobre sucção, autonomia e metragem |",
              "| `/guias/succao/` | `/guias/` | os textos sobre sucção, autonomia e metragem |\n| `/guias/manutencao/` | `/guias/` | os textos sobre limpeza e troca |"),
    ),
    (
        'nasce a categoria de reservatorios, que nao tem uma peca sequer',
        'categoria vazia indexada e pagina fina que derruba o resto (16.5)',
        trocas(CASCA, [
            ("\t\t'baterias'              => array( 'pecas',   'Baterias' ),",
             "\t\t'baterias'              => array( 'pecas',   'Baterias' ),\n\t\t'reservatorios'         => array( 'pecas',   'Reservatórios' ),"),
        ]),
    ),
    (
        'a categoria de um guia aponta para categoria inexistente',
        'degrau inventado some da trilha sem ninguem ver, e o cluster fica torto',
        troca(CASCA,
              "\t\t'quantos-m2-o-robo-aspirador-limpa-por-carga' => 'guias-succao',",
              "\t\t'quantos-m2-o-robo-aspirador-limpa-por-carga' => 'guias-manutencao',"),
    ),
    (
        'o par peca x modelo volta ao numero digitado',
        '33 conta o que o banco guarda; a tela fala do que a ilha serve, e sao 32',
        troca(FATOS,
              '"pares_declarados": 32,',
              '"pares_declarados": 33,'),
    ),
    (
        'a contagem de marcas engorda em um',
        'numero de tela que nao nasce contado passa a mentir no dia em que o banco muda',
        troca(FATOS,
              '"marcas": 5,',
              '"marcas": 6,'),
    ),
    (
        'a pagina Sobre volta a ser fina',
        'pagina magra em dominio novo gasta orcamento de rastreamento (14.1)',
        trocas(CASCA, [
            ("\t$html .= '<p>A busca comercial do nicho (\"melhor robô aspirador\") está tomada por listas de compra, e nós não disputamos essa. A busca que ninguém responde direito é a de quem <strong>já tem</strong> o robô: qual filtro serve, qual escova lateral encaixa, qual bateria é a certa. Hoje quem responde isso é o título do anúncio de quem vende a peça. Não existe comparador entre marcas com fonte e data — e é esse buraco que este site ocupa.</p></div>';",
             "\t$html .= '<p>Listas de compra ja cobrem a busca comercial.</p></div>';"),
            ("\t$html .= '<p>Sem pessoa em cena: sem rosto, sem vídeo, sem canal, sem presença em fórum. O que sustenta uma resposta aqui é o método e a procedência do dado, e os dois ficam abertos para conferência em cada página. Ferramentas e conteúdo são versionados em repositório público antes de chegarem ao site, e o banco tem um verificador que reprova registro sem fonte, sem data ou com divergência não resolvida — o que está no ar passou por ele.</p>';",
             "\t$html .= '<p>Sem pessoa em cena.</p>';"),
        ]),
    ),
]


def main():
    reprovadas = 0
    passaram = []

    print('Mutacoes deliberadas na arvore da casca 1.3.0 — cada uma TEM que reprovar\n')

    for nome, porque, aplicar in MUTACOES:
        with tempfile.TemporaryDirectory() as tmp:
            base = os.path.join(tmp, 'ilha')
            shutil.copytree(RAIZ, base)
            try:
                aplicar(base)
            except AssertionError as erro:
                print('  ERRO   %-58s %s' % (nome, erro))
                passaram.append(nome)
                continue

            falhas = []
            pegou_em = []
            for teste in TESTES:
                saida = subprocess.run(
                    ['php', os.path.join(base, teste), base],
                    capture_output=True, text=True)
                if saida.returncode != 0:
                    pegou_em.append(os.path.basename(teste))
                    falhas += [l.strip() for l in saida.stdout.splitlines()
                               if l.strip().startswith('FALHA')]

            if not pegou_em:
                print('  PASSOU %-58s <- a trava NAO pegou' % nome)
                print('         (%s)' % porque)
                passaram.append(nome)
                continue

            print('  ok     %-58s %d falha(s) em %s'
                  % (nome, len(falhas), ', '.join(pegou_em)))
            for linha in falhas[:2]:
                print('         %s' % linha[:112])
            reprovadas += 1

    print('\n%d de %d mutacoes reprovadas pela bancada.' % (reprovadas, len(MUTACOES)))
    if passaram:
        print('MUTACOES QUE PASSARAM (trava faltando):')
        for nome in passaram:
            print('  - %s' % nome)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
