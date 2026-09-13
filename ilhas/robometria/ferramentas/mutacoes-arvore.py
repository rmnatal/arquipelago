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
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASCA = 'snippets/robometria-casca.php'
R2 = 'snippets/robometria-r2.php'
ARVORE = 'ARVORE.md'
FATOS = 'dados/casca-fatos.json'
PECAS = 'dados/pecas.json'
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


def troca_n(arquivo, velho, novo, quantas):
    """Como trocas(), mas o alvo se repete um numero DECLARADO de vezes.

    A unicidade de trocas() existe para que mutacao que nao encontra o alvo nao
    passe por mutacao aplicada. Quando o alvo e legitimamente repetido — duas
    pecas do mesmo tipo, por exemplo — a mesma protecao se faz declarando quantas
    ocorrencias tem de existir: se o banco crescer e virarem tres, a mutacao PARA
    em vez de editar um numero de linhas que ninguem previu.
    """
    def aplicar(base):
        caminho = os.path.join(base, arquivo)
        with open(caminho, encoding='utf-8') as f:
            corpo = f.read()
        achados = corpo.count(velho)
        if achados != quantas:
            raise AssertionError(
                'alvo da mutacao aparece %d vez(es) em %s, e a mutacao declara %d'
                % (achados, arquivo, quantas))
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(corpo.replace(velho, novo))
    return aplicar


def varias(*aplicadores):
    """Uma mutacao que precisa de mais de um arquivo para PRODUZIR o mundo.

    Nasceu em 13/09/2026: a mutacao do reservatorio media a 16.5 enquanto o tipo
    nao tinha peca nenhuma no banco, e o bloco que gravou as duas primeiras a
    deixou INERTE — com a categoria declarada e o tipo povoado, quem a reprovava
    passou a ser a regra VIZINHA, a de documento e codigo divergentes. Defeito
    pego pela regra vizinha prova que ALGUMA trava existe, nao que ESTA existe.
    Para a 16.5 voltar a ser a trava medida, a mutacao tem de esvaziar o tipo E
    declarar a categoria E acertar o documento, tudo na mesma copia.
    """
    def aplicar(base):
        for f in aplicadores:
            f(base)
    return aplicar


def engorda(arquivo, chave):
    """Soma 1 ao numero que a chave guarda hoje, seja ele qual for.

    NASCEU DE UMA MUTACAO QUE MORREU CALADA (12/09/2026). Duas mutacoes daqui
    tinham o numero DIGITADO nos dois lados ('"pares_declarados": 32,' ->
    '... 33,'). No dia em que o banco cresceu, o alvo deixou de existir no
    arquivo e a mutacao passou a nao editar nada — exatamente a "mutacao inerte"
    que este arquivo existe para impedir, e pela mesma causa que a secao 8 do
    ARQUIPELAGO.md registra em numero de tela: quem digita um numero derivado
    assina um cheque contra o banco de amanha. A regra vale para a bancada
    tambem, e nao so para a pagina: numero de mutacao nasce LIDO do arquivo.
    """
    def aplicar(base):
        caminho = os.path.join(base, arquivo)
        with open(caminho, encoding='utf-8') as f:
            corpo = f.read()
        achados = re.findall(r'"%s": (\d+),' % re.escape(chave), corpo)
        if len(achados) != 1:
            raise AssertionError('a chave %r nao esta unica em %s: %d ocorrencia(s)'
                                 % (chave, arquivo, len(achados)))
        hoje = int(achados[0])
        corpo = corpo.replace('"%s": %d,' % (chave, hoje),
                              '"%s": %d,' % (chave, hoje + 1))
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(corpo)
    return aplicar


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
        'nasce a categoria de reservatorios no dia em que as duas pecas saem do banco',
        'categoria vazia indexada e pagina fina que derruba o resto (16.5) — e aqui a '
        '16.5 e a trava MEDIDA, porque o documento tambem ganha a linha e a regra '
        'vizinha da divergencia nao tem do que reclamar',
        varias(
            # o mundo: o tipo 'reservatorio' volta a nao ter peca nenhuma
            # A CONTAGEM E DECLARADA e sobe a mao de proposito: em 13/09/2026 o
            # recipiente FW008543 da WAP virou a TERCEIRA peca deste tipo e a
            # mutacao PAROU, que e o desenho do troca_n. Numero que subisse
            # sozinho deixaria a mutacao editar um numero de linhas que ninguem
            # previu — e mutacao que nao esvazia o tipo nao testa a 16.5.
            troca_n(PECAS, '"tipo": "reservatorio",', '"tipo": "filtro",', 3),
            # a categoria proibida, declarada no codigo
            troca(CASCA,
                  "\t\t'baterias'              => array( 'pecas',   'Baterias' ),",
                  "\t\t'baterias'              => array( 'pecas',   'Baterias' ),\n\t\t'reservatorios'         => array( 'pecas',   'Reservatórios' ),"),
            # e no documento, para a divergencia doc x codigo ficar fora do caminho
            troca(ARVORE,
                  "| `/pecas/baterias/` | `/pecas/` | bateria por modelo |",
                  "| `/pecas/baterias/` | `/pecas/` | bateria por modelo |\n| `/pecas/reservatorios/` | `/pecas/` | recipiente de pó por modelo |"),
        ),
    ),
    (
        'a casca declara uma categoria de peca que o vocabulario do banco nao conhece',
        'e a UNICA mutacao que faz a trava do MUNDO PRODUZIDO da 16.5 reprovar, e ela '
        'nasceu para isso: com o banco cobrindo todos os tipos, as cinco afirmacoes '
        'produzidas passariam para sempre e ninguem teria visto nenhuma delas reprovar. '
        'Categoria sem tipo no vocabulario e o defeito real que ela pega — a arvore '
        'promete uma prateleira que o banco nao sabe encher',
        varias(
            troca(CASCA,
                  "\t\t'baterias'              => array( 'pecas',   'Baterias' ),",
                  "\t\t'baterias'              => array( 'pecas',   'Baterias' ),\n\t\t'reservatorios-de-agua' => array( 'pecas',   'Reservatórios de água' ),"),
            troca(ARVORE,
                  "| `/pecas/baterias/` | `/pecas/` | bateria por modelo |",
                  "| `/pecas/baterias/` | `/pecas/` | bateria por modelo |\n| `/pecas/reservatorios-de-agua/` | `/pecas/` | reservatório de água por modelo |"),
        ),
    ),
    (
        'a categoria de um guia aponta para categoria inexistente',
        'degrau inventado some da trilha sem ninguem ver, e o cluster fica torto',
        troca(CASCA,
              "\t\t'quantos-m2-o-robo-aspirador-limpa-por-carga' => 'guias-succao',",
              "\t\t'quantos-m2-o-robo-aspirador-limpa-por-carga' => 'guias-manutencao',"),
    ),
    (
        'o par peca x modelo engorda em um',
        'a tela fala do que a ilha SERVE, e o numero so pode vir contado do banco — um a mais e o que a contagem digitada produzia',
        engorda(FATOS, 'pares_declarados'),
    ),
    (
        'a contagem de marcas engorda em um',
        'numero de tela que nao nasce contado passa a mentir no dia em que o banco muda',
        engorda(FATOS, 'marcas'),
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
