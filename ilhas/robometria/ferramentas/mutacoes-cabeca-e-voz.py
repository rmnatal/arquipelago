#!/usr/bin/env python3
"""Quebra de proposito a casca e as bancadas, e exige que o portao REPROVE.

    python3 ferramentas/mutacoes-cabeca-e-voz.py

POR QUE ESTE ARQUIVO EXISTE
---------------------------
"A PROVA DE QUE UMA TRAVA REPROVA E PARTE DO BLOCO" (PROMPT.md desta ilha, e
secao 8 do ARQUIPELAGO.md). Trava que nunca foi vista reprovando e trava nao
medida — e nesta ilha tres travas ja passaram verdes medindo a si mesmas.

Cada mutacao abaixo e uma copia da arvore inteira num diretorio temporario, com
UMA edicao cirurgica, e o teste tem que sair com codigo diferente de zero. Se
alguma passar, o script reprova e diz qual: uma trava que aprova o codigo
quebrado e pior do que trava nenhuma, porque da a sensacao de ter conferido.

A copia e da arvore inteira de proposito: o teste le snippets/, dados/ e
manifest.json, e mutacao aplicada no lugar deixaria residuo se o script morresse
no meio.
"""

import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASCA = 'snippets/robometria-casca.php'
TESTE = 'ferramentas/teste-casca.php'
VOZ = 'ferramentas/teste-voz.php'
ARVORE = 'ferramentas/teste-arvore.php'
ACENTO = 'ferramentas/teste-acentuacao.php'
A1 = 'ferramentas/teste-a1.php'


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
        'a tag some do wp_head',
        'a description volta a nao existir, que e o defeito que a Sentinela mediu',
        troca(CASCA,
              "\techo '<meta name=\"description\" content=\"' . esc_attr( $c['descricao'] ) . '\">' . \"\\n\";",
              "\t/* mutacao: a tag nao sai */"),
    ),
    (
        'duas paginas com a mesma description',
        'texto repetido em endereco diferente e o defeito que a tag existe para nao ter',
        troca(CASCA,
              "'descricao' => 'Uma diz qual peça serve no seu robô aspirador. A outra diz quanta sucção e quanto tempo a metragem da sua casa pede.',",
              "'descricao' => 'Diga a marca e o modelo do seu robô aspirador e veja qual filtro, escova, mop ou bateria o fabricante declarou para ele.',"),
    ),
    (
        'um numero dentro de uma description',
        'numero digitado em texto que ninguem rele passa a mentir em silencio quando o banco cresce',
        troca(CASCA,
              "'descricao' => 'Quanta sucção o seu robô precisa para piso liso, tapete ou pelo de cachorro, e quantos ciclos a metragem da sua casa exige.',",
              "'descricao' => 'Quanta sucção o seu robô precisa: 28 modelos medidos para piso liso, tapete ou pelo de cachorro, com os ciclos da sua casa.',"),
    ),
    (
        'uma description longa demais',
        'acima de 160 o Google corta no meio da frase e devolve um trecho que ninguem escreveu',
        troca(CASCA,
              "'descricao' => 'Quem faz a Robometria, por que ela só afirma o que o fabricante declarou, e como avisar quando uma peça daqui não encaixou.',",
              "'descricao' => 'Quem faz a Robometria, por que ela só afirma o que o fabricante declarou, como avisar quando uma peça daqui não encaixou, o que a ilha publica, o que ela recusa e por quê.',"),
    ),
    (
        'uma pagina publicada sem cabeca',
        'pagina nova entrando sem description e exatamente como a ilha chegou a nove paginas sem nenhuma',
        troca(CASCA,
              "\t\t'quantos-pa-o-robo-aspirador-precisa' => array(",
              "\t\t'quantos-pa-o-robo-aspirador-precisa-MUTADO' => array("),
    ),
    (
        'uma cabeca sobrando, sem pagina',
        'cobrar um lado so foi o defeito de 11/09 no Clube do Mosaico — o teste media so a categoria que existia quando foi escrito',
        troca(CASCA,
              "\t\t'sobre' => array(",
              "\t\t'pagina-que-nunca-existiu' => array(\n\t\t\t'tipo' => 'website',\n\t\t\t'titulo' => 'Uma pagina que nao existe',\n\t\t\t'descricao' => 'Texto de uma pagina que a ilha nunca publicou, aqui so para o portao ver que ele reprova cabeca sobrando no mapa.',\n\t\t),\n\t\t'sobre' => array("),
    ),
    (
        'o H1 da raiz volta a ser "Inicio"',
        'e o H1 da pagina que disputa a marca, e ele nao nomeava o que a ilha faz',
        troca(CASCA,
              "'inicio'                  => array( 'titulo' => 'Seu robô aspirador: qual peça serve, quanta sucção', 'conteudo' => '[robometria_home]' ),",
              "'inicio'                  => array( 'titulo' => 'Início', 'conteudo' => '[robometria_home]' ),"),
    ),
    (
        'termo de dentro da fabrica no primeiro paragrafo da home',
        'a secao 15.2 do contrato manda o vocabulario tecnico morar na camada de prova, nunca na abertura',
        troca(CASCA,
              "<p class=\"rbm-promessa\">Diga a marca e o modelo. A gente mostra o que o fabricante declarou",
              "<p class=\"rbm-promessa\">Esta ferramenta cruza a matriz de compatibilidade e a especificação declarada pelo fabricante"),
    ),
    (
        'a home perde o seletor e volta a ser manifesto',
        'no molde FERRAMENTA a ferramenta E a home; sem esta trava ela podia virar texto de novo sem ninguem reclamar',
        troca(CASCA,
              "\t\t$html .= robometria_r1_formulario();",
              "\t\t$html .= '<p>Use a página de peças para consultar o seu modelo.</p>';"),
    ),
    (
        'os atalhos passam a ser digitados, nao contados',
        'numero de tela nasce contado — e digitar tres tipos quando o banco tem cinco e a cicatriz do cartao que dizia zero',
        troca(CASCA,
              "\tforeach ( (array) $d['tipos'] as $tipo ) {\n\t\t$rotulo = robometria_r1_maiuscula( robometria_r1_nome_do_tipo( $tipo ) );",
              "\tforeach ( array( 'filtro', 'escova lateral', 'bateria' ) as $tipo ) {\n\t\t$rotulo = robometria_r1_maiuscula( robometria_r1_nome_do_tipo( $tipo ) );"),
    ),
    (
        'escassez inventada FORA do bloco de recusa',
        'a seccao 7 proibe selo de "mais vendido"; a frase legitima que o recusa usa as mesmas palavras, e quem separa e a estrutura',
        troca(CASCA,
              "$html .= '<p>Cada marketplace vende as marcas que vende.",
              "$html .= '<p>Mostramos primeiro a peça mais vendida da categoria. Cada marketplace vende as marcas que vende."),
    ),
    (
        'uma promessa escondida DENTRO do bloco de recusa',
        'foi assim que a segunda versao da trava do Clube do Mosaico aprovou "Peça mais vendida, últimas unidades!"',
        troca(CASCA,
              "$html .= '<li>Não publicamos nota nem estrela de avaliação que a gente não tenha medido.</li>';",
              "$html .= '<li>Peça mais vendida do mês, últimas unidades!</li>';"),
    ),
    (
        'a pagina Sobre volta a ser fina',
        'menos de 1.500 caracteres de corpo em dominio novo e orcamento de rastreamento gasto a toa',
        trocas(CASCA, [
            ("$html .= '<p>Sem pessoa em cena: sem rosto, sem vídeo, sem canal, sem presença em fórum. O que sustenta uma resposta aqui é o método e a procedência do dado, e os dois ficam abertos para conferência em cada página. Ferramentas e conteúdo são versionados em repositório público antes de chegarem ao site, e o banco tem um verificador que reprova registro sem fonte, sem data ou com divergência não resolvida — o que está no ar passou por ele.</p>';",
             "$html .= '<p>Sem pessoa em cena.</p>';"),
            ("$html .= '<p>A busca comercial do nicho (\"melhor robô aspirador\") está tomada por listas de compra, e nós não disputamos essa. A busca que ninguém responde direito é a de quem <strong>já tem</strong> o robô: qual filtro serve, qual escova lateral encaixa, qual bateria é a certa. Hoje quem responde isso é o título do anúncio de quem vende a peça. Não existe comparador entre marcas com fonte e data — e é esse buraco que este site ocupa.</p></div>';",
             "$html .= '<p>Existe para responder qual peça serve.</p></div>';"),
        ]),
    ),
    (
        'description generica de reserva para pagina desconhecida',
        'a saida tentadora para o portao acima publicaria a MESMA description em endereco diferente',
        troca(CASCA,
              "\tif ( '' === $slug || ! isset( $cabeca[ $slug ] ) ) {\n\t\treturn;\n\t}",
              "\tif ( '' === $slug || ! isset( $cabeca[ $slug ] ) ) {\n\t\techo '<meta name=\"description\" content=\"Robometria: compatibilidade de peças de robô aspirador.\">' . \"\\n\";\n\t\treturn;\n\t}"),
    ),
    (
        'a folha do formulario volta a ser copiada na R1',
        'foi a divergencia silenciosa entre duas copias que este bloco desfez',
        troca('snippets/robometria-r1.php',
              "\t$css = <<<'CSS'\n.rbm-resposta{margin:2.4rem 0 0;",
              "\t$css = <<<'CSS'\n.rbm-form{display:flex;}\n.rbm-form-campo{flex:1 1 15rem;}\n.rbm-resposta{margin:2.4rem 0 0;"),
    ),

    # -----------------------------------------------------------------------
    # A LEVA DE 11/09/2026 — um nome por pagina, e a bancada que media tres
    # paginas pela metade. Cada uma destas mutacoes reproduz um defeito REAL
    # que estava no repositorio ou no ar nesta manha.
    # -----------------------------------------------------------------------
    (
        'a bancada volta a varrer sem as options do Sync',
        'foi assim que pagina:a1 mediu 1.118 caracteres e a metodologia serviu o aviso de "sem medicao" — tres estados varridos pela metade, sem erro nenhum',
        troca('ferramentas/varrer-corpo.php',
              "robometria_teste_carregar_options( $raiz );\n\nrobometria_teste_carregar( $raiz );",
              "robometria_teste_carregar( $raiz );"),
        ACENTO,
    ),
    (
        'o aviso de estado degradado perde a marca no markup',
        'sem a classe, o estado "estamos sem o banco" volta a ser uma pagina inteira e honesta que nenhuma bancada consegue distinguir da pagina de verdade',
        troca(CASCA,
              "return '<div class=\"rbm-bloco rbm-sem-banco\">'",
              "return '<div class=\"rbm-bloco\">'"),
    ),
    (
        'o <title> volta a ser o que o WordPress monta',
        'e o que estava no ar: "Robometria – Compatibilidade de pecas e dimensionamento de robo aspirador", 73 caracteres de um campo do wp-admin que nenhum arquivo deste repositorio escreve',
        troca(CASCA,
              "add_filter( 'document_title_parts', function ( $partes ) {",
              "add_filter( 'document_title_parts_MUTADO', function ( $partes ) {"),
        VOZ,
    ),
    (
        'o og:title volta a ser uma frase digitada',
        'era exatamente a forma do defeito: um segundo nome ao lado do primeiro, cada um certo no seu lugar, nenhum capaz de corrigir o outro',
        troca(CASCA,
              "echo '<meta property=\"og:title\" content=\"' . esc_attr( robometria_casca_nome_da_pagina( $slug ) ) . '\">' . \"\\n\";",
              "echo '<meta property=\"og:title\" content=\"Quem publica a Robometria\">' . \"\\n\";"),
        VOZ,
    ),
    (
        'uma pagina volta a se chamar pelo nome da gaveta',
        '"Sobre" e o nome da pasta, nao a pergunta que a pessoa digita (secao 14.5) — e com UMA fonte de nome a divergencia some, entao quem pega isto e a regra de voz sobre o nome, nunca a de coerencia',
        troca(CASCA,
              "'sobre'                   => array( 'titulo' => 'Quem publica este site',",
              "'sobre'                   => array( 'titulo' => 'Sobre',"),
        VOZ,
    ),
    (
        'um nome estoura o teto do <title>',
        'acima de 65 o Google corta no meio e mostra um pedaco que ninguem escreveu — e o teto e do NOME, medido antes de publicar',
        troca(CASCA,
              "'metodologia'             => array( 'titulo' => 'Como a gente decide o que publicar',",
              "'metodologia'             => array( 'titulo' => 'Como a gente decide o que publicar, o que recusa e por que motivo',"),
        VOZ,
    ),
    (
        'a abertura volta a comecar falando da propria pagina',
        '"Esta ferramenta responde..." e a forma que o VOZ.md proibe pelo nome; quem entrou quer falar do proprio robo',
        troca('snippets/robometria-r1.php',
              "<p class=\"rbm-linha-mestra\">Diga a marca e o modelo do seu robô",
              "<p class=\"rbm-linha-mestra\">Esta ferramenta responde o que serve no seu robô"),
        VOZ,
    ),
    (
        'procedencia volta a abrir a pagina',
        'nome de fabricante no primeiro paragrafo e o que a secao 15.2 manda morar na camada de prova — foi como os tres artigos da Aquametria abriam',
        troca(CASCA,
              "$html .= '<p class=\"rbm-linha-mestra\">Duas perguntas sobre o seu robô, e só elas:",
              "$html .= '<p class=\"rbm-linha-mestra\">Transcrevemos o catálogo da Electrolux para o seu robô, e só isso:"),
        VOZ,
    ),
    (
        'a linha-mestra se declara camada de prova',
        'a porta dos fundos da excecao por classe: bastaria marcar a abertura como prova para ela sair de toda medicao',
        troca(CASCA,
              "$html .= '<p class=\"rbm-linha-mestra\">Duas perguntas sobre o seu robô, e só elas:",
              "$html .= '<p class=\"rbm-linha-mestra rbm-prova\">Duas perguntas sobre o seu robô, e só elas:"),
        VOZ,
    ),
    (
        'a abertura para de falar com quem entrou',
        'pagina que abre falando da internet em vez de falar com a pessoa foi o que a Aquametria achou em cinco paginas no mesmo dia',
        troca(CASCA,
              "$html .= '<p class=\"rbm-linha-mestra\">Duas perguntas sobre o seu robô, e só elas: que peça encaixa nele, e quanta sucção ele precisa.</p>';",
              "$html .= '<p class=\"rbm-linha-mestra\">Duas perguntas, e só elas: que peça encaixa no robô, e quanta sucção ele precisa.</p>';"),
        VOZ,
    ),
    (
        'o rotulo da mae volta a ser digitado na trilha',
        'a filha dizia "Ferramentas" na trilha enquanto a mae, a um clique, se chamava outra coisa',
        troca(CASCA,
              "'nivel1' => array( $mae, robometria_casca_nome_da_pagina( $mae ) ),",
              "'nivel1' => array( $mae, 'Ferramentas' ),"),
        ARVORE,
    ),
    (
        'o par artigo x ferramenta volta a ser por nome',
        'foi o portao da arvore que pegou isto quando a R2 trocou de nome: o par simplesmente deixou de existir, calado',
        troca('snippets/robometria-a2.php',
              "'ferramenta' => ROBOMETRIA_R2_SLUG,",
              "'ferramenta' => 'Quantos Pa e quanto tempo o seu robô precisa',"),
        ARVORE,
    ),
    (
        'a ferramenta para de reespelhar o titulo da propria pagina',
        'era o estado real ate agora: renomear no repositorio trocava o og:title, o cartao e a trilha, e deixava o H1 e o <title> do ar com o nome antigo — duas fontes para o mesmo campo, e a bancada le a que esta certa',
        troca('snippets/robometria-r2.php',
              "\t\t\twp_update_post( array( 'ID' => $pid, 'post_title' => ROBOMETRIA_R2_TITULO ) );",
              "\t\t\t/* mutacao: o titulo do ar envelhece calado */"),
    ),
    (
        'o titulo do A1 volta a afirmar a tese',
        'a tese tem duas formas escolhidas pela contagem do banco; o titulo tinha uma so, digitada, e ia junto para o headline do JSON-LD',
        troca('snippets/robometria-a1.php',
              "define( 'ROBOMETRIA_A1_TITULO', 'Existe filtro universal de robô aspirador?' );",
              "define( 'ROBOMETRIA_A1_TITULO', 'Por que não existe filtro universal de robô aspirador' );"),
        A1,
    ),
]



def main():
    reprovadas = 0
    passaram = []

    print('Mutacoes deliberadas — cada uma TEM que reprovar, no portao que a nomeia\n')

    for entrada in MUTACOES:
        nome, porque, aplicar = entrada[0], entrada[1], entrada[2]
        teste = entrada[3] if len(entrada) > 3 else TESTE
        with tempfile.TemporaryDirectory() as tmp:
            base = os.path.join(tmp, 'ilha')
            shutil.copytree(RAIZ, base)
            try:
                aplicar(base)
            except AssertionError as erro:
                print('  ERRO   %-56s %s' % (nome, erro))
                passaram.append(nome)
                continue

            saida = subprocess.run(
                ['php', os.path.join(base, teste), base],
                capture_output=True, text=True)

            if saida.returncode == 0:
                print('  PASSOU %-56s <- a trava NAO pegou' % nome)
                print('         (%s)' % porque)
                passaram.append(nome)
                continue

            falhas = [l.strip() for l in saida.stdout.splitlines() if l.strip().startswith('FALHA')]
            print('  ok     %-56s %d falha(s)' % (nome, len(falhas)))
            for linha in falhas[:2]:
                print('         %s' % linha[:110])
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
