#!/usr/bin/env python3
"""Quebra de proposito a casca 1.2.0 e exige que teste-casca.php REPROVE.

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
              "'inicio'                  => array( 'titulo' => 'Robô aspirador: qual peça serve no seu, e quanta sucção precisa', 'conteudo' => '[robometria_home]' ),",
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
]


def main():
    reprovadas = 0
    passaram = []

    print('Mutacoes deliberadas na casca 1.2.0 — cada uma TEM que reprovar\n')

    for nome, porque, aplicar in MUTACOES:
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
                ['php', os.path.join(base, TESTE), base],
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
