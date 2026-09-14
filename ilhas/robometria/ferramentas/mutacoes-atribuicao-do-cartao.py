#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Devolve a atribuicao digitada ao cartao e a frase, e exige REPROVACAO.

    python3 ferramentas/mutacoes-atribuicao-do-cartao.py

POR QUE ESTE ARQUIVO EXISTE
---------------------------
"A PROVA DE QUE UMA TRAVA REPROVA E PARTE DO BLOCO" (secao 8 do ARQUIPELAGO.md).
A secao 17 do teste-r1.php nasceu em 14/09/2026 e nasceu verde sobre o estado
consertado — o que e informacao sobre o conserto e nenhuma informacao sobre a
regua.

O DEFEITO QUE ELA EXISTE PARA PEGAR ESTAVA NO AR, em duas superficies da MESMA
tela. O cartao da vitrine escrevia "o fabricante declara esta peca", DIGITADO,
para qualquer degrau, e a frase do kit sem avulso escrevia "que o fabricante
declara" numa oracao que ja abria com "A Electrolux (loja oficial) nao vende...".
Em 52 dos 73 itens do banco daquele dia o publicador e a LOJA OFICIAL da marca, e
a escada de fontes ja decidia, com todas as letras, que a atribuicao do degrau 4
e "pela loja oficial da marca", "porque quem transcreveu foi a loja". Falar pela
marca (fala_pela_marca, que e o que decide de que LADO o item cai na pagina) nao
e ser a marca.

E NENHUM DOS PORTOES MORDIA. A secao 3 do teste-r1.php compara cada frase do PHP
com a da implementacao de referencia — as duas erravam IGUAL, entao ela ficava
verde. A secao 16 media o LADO, que estava certo. Trava vizinha verde prova que
ALGUMA trava existe, nunca que ESTA existe.

UMA HIPOTESE DESTE BLOCO FOI MEDIDA E ESTAVA ERRADA, e ela fica escrita porque a
medicao so faz sentido ao lado da expectativa que a produziu. A previsao era que
citar a MARCA em vez de quem publicou passaria limpa no banco de hoje, porque
todo publicador do degrau 4 tem a marca escrita dentro do nome — e portanto que
so um publicador sem o nome da marca (uma assistencia autorizada) separaria as
duas medicoes. Rodada, a mutacao REPROVOU no banco de hoje: a regua cobra o
publicador INTEIRO, e "Electrolux" nao e "Electrolux (loja oficial)". O parenteses
que a coleta transcreveu ja separa as duas coisas hoje, sem mundo nenhum
produzido. O mundo da assistencia continua aqui porque cobre o caso em que o
publicador nao divide UMA LETRA com a marca, que o banco de hoje nao tem — mas
ele nao e mais o que sustenta a regua, e dizer o contrario seria vender cobertura
que a medicao nao comprou.

A ULTIMA MUTACAO TEM DE PASSAR: mundo intacto que reprova e falso-positivo, e
regua que reprova tudo "pega" qualquer defeito sem medir nenhum.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNIPPET = 'snippets/robometria-r1.php'
REFERENCIA = 'ferramentas/cobertura-r1.py'
PECAS = 'dados/pecas.json'
PUBLICADORES = 'dados/publicadores.json'


def trocar(arquivo, de, para, vezes=1):
    """Edita um arquivo da ilha. `vezes` e DECLARADO e conferido: alvo que
    aparece um numero diferente de vezes do que esta escrito aqui mudou de
    natureza, e a mutacao para em vez de editar menos (ou mais) do que anuncia —
    mutacao que nao morde e teste verde com outro nome."""
    def aplicar(base_dir):
        caminho = os.path.join(base_dir, arquivo)
        with open(caminho, encoding='utf-8') as fh:
            texto = fh.read()
        achados = texto.count(de)
        if achados != vezes:
            raise AssertionError(
                'a mutacao esperava %d ocorrencia(s) de %r em %s e achou %d.'
                % (vezes, de[:70], arquivo, achados))
        with open(caminho, 'w', encoding='utf-8') as fh:
            fh.write(texto.replace(de, para))
    return aplicar


def editar_json(arquivo, mudar):
    def aplicar(base_dir):
        caminho = os.path.join(base_dir, arquivo)
        with open(caminho, encoding='utf-8') as fh:
            doc = json.load(fh)
        mudar(doc)
        with open(caminho, 'w', encoding='utf-8') as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=1)
            fh.write('\n')
    return aplicar


def publicador_vira_assistencia(doc):
    """PRODUZ O MUNDO: quem publica fala pela marca e NAO carrega o nome dela.

    Uma rede autorizada esta no degrau 4 com todo o direito, e o nome dela nao
    tem "Electrolux" dentro. E o unico mundo em que "cita o publicador" e "cita
    a marca" deixam de ser a mesma medicao.
    """
    tocou = 0
    for reg in doc['registros']:
        for fonte in (reg.get('fontes') or {}).values():
            if fonte.get('nivel') == 4:
                fonte['publicador'] = 'Rede Autorizada Sul Servicos'
                tocou += 1
    if not tocou:
        raise AssertionError('nenhuma fonte de nivel 4 no banco: o mundo desta '
                             'mutacao nao pode ser produzido, e ela mediria nada')


def declarar_a_assistencia(doc):
    """A assistencia autorizada entra tambem em publicadores.json.

    NASCEU EM 14/09/2026, com a trava do artigo de quem publica: desde ela,
    publicador sem artigo declarado DERRUBA o gerador, de proposito. Entao o
    mundo desta bateria — uma rede autorizada publicando no degrau 4 — passou a
    exigir a declaracao junto, que e exatamente o que um bloco de verdade teria
    de escrever. Sem isto a mutacao "o mundo sadio, sozinho, passa" reprovava
    pela trava nova, e nao pelo que ela mede.
    """
    if any(r['nome'] == 'Rede Autorizada Sul Servicos' for r in doc['registros']):
        raise AssertionError('a assistencia ja estava declarada: o mundo desta '
                             'mutacao nao seria produzido')
    doc['registros'].append({
        'id': 'rede-autorizada-sul-servicos',
        'nome': 'Rede Autorizada Sul Servicos',
        'artigo': 'a',
        'motivo': 'mundo produzido pela bateria de mutacoes: o nucleo do nome e '
                  '"Rede", feminino singular.',
    })


def mundo_da_assistencia(base_dir):
    """As duas metades do mesmo mundo: quem publica, e a gramatica dele."""
    editar_json(PECAS, publicador_vira_assistencia)(base_dir)
    editar_json(PUBLICADORES, declarar_a_assistencia)(base_dir)


def intacto(base_dir):
    return None


MUTACOES = [
    (
        'o cartao volta a escrever "o fabricante declara esta peca"',
        'o defeito literal que este bloco tirou do ar, palavra por palavra, em '
        'todo cartao de todo degrau',
        trocar(
            SNIPPET,
            "				? '%3$s %4$s este kit compatível com o seu %1$s, e é dentro dele que vem %2$s'\n"
            "				: '%3$s %4$s esta peça (%2$s) compatível com o seu %1$s',",
            "				? 'o fabricante declara este kit compatível com o seu %1$s, e é dentro dele que vem %2$s'\n"
            "				: 'o fabricante declara esta peça (%2$s) compatível com o seu %1$s',"),
        False,
    ),
    (
        'a frase do kit sem avulso volta a dizer "que o fabricante declara"',
        'a outra metade do mesmo defeito, e ela estava em 18 itens no ar: a '
        'oracao abria com o publicador certo e emprestava a autoridade do '
        'fabricante 15 palavras depois, dentro de UMA frase',
        trocar(
            SNIPPET,
            "que %8$s %9$s compatível com %10$s (%11$s, verificado em %12$s).',\n"
            "			$quem_maiusculo, robometria_r1_verbo( $item, 'vende', 'vendem' ),\n"
            "			$artigo, $tipo, $avulso, $pronome,\n"
            "			$identificacao, $quem, $declara, $lista, $rotulo_origem, $data",
            "que o fabricante declara compatível com %8$s (%9$s, verificado em %10$s).',\n"
            "			$quem_maiusculo, robometria_r1_verbo( $item, 'vende', 'vendem' ),\n"
            "			$artigo, $tipo, $avulso, $pronome,\n"
            "			$identificacao, $lista, $rotulo_origem, $data"),
        False,
    ),
    (
        'o cartao troca o publicador pelo ROTULO DO DEGRAU',
        'e a confusao central que este bloco desfez: o rotulo responde "de que '
        'lado esta este item", nunca "quem declarou". Hoje ele acertaria a loja '
        'oficial por coincidencia de texto, e erraria todo degrau 3, cujo rotulo '
        'e "pagina do fabricante" e cujo publicador e a marca',
        trocar(
            SNIPPET,
            "			robometria_r1_lista( $tipos_do_cartao ),\n"
            "			robometria_r1_quem_publica( $i ),\n"
            "			robometria_r1_verbo( $i, 'declara', 'declaram' )\n"
            "		) ) . '</span>';",
            "			robometria_r1_lista( $tipos_do_cartao ),\n"
            "			$rotulo_origem,\n"
            "			'declara'\n"
            "		) ) . '</span>';"),
        False,
    ),
    (
        'a nota da ordem volta a dizer que o criterio e a declaracao do fabricante',
        'e a frase que justifica a ORDEM comercial da lista, logo acima dos '
        'botoes de afiliado — o lugar mais caro da pagina para emprestar '
        'autoridade a quem so transcreveu',
        trocar(
            SNIPPET,
            'ela é decidida pela declaração de compatibilidade publicada na fonte de cada peça, e só por ela.',
            'ela é decidida pela declaração do fabricante, e só ela.'),
        False,
    ),
    (
        'a oracao de atribuicao deixa de ser o comeco da frase publicada',
        'a fronteira nomeada e o que esta secao mede; se a frase publicada '
        'parasse de crescer a partir dela, a secao 17 inteira viraria medicao de '
        'codigo morto, verde e inutil',
        trocar(
            SNIPPET,
            "	$frase = robometria_r1_atribuicao_do_item( $item );",
            "	$frase = 'Compatibilidade declarada. ' . robometria_r1_atribuicao_do_item( $item );"),
        False,
    ),
    (
        'a referencia e o snippet erram JUNTOS',
        'e por isso que a secao 3 nao pegou nada: ela compara as duas frases '
        'entre si. Duas metades que erram igual ficam verdes na comparacao — a '
        'regua da atribuicao tem de morder mesmo quando as duas concordam',
        lambda base: (
            trocar(
                SNIPPET,
                "que %8$s %9$s compatível com %10$s (%11$s, verificado em %12$s).',\n"
                "			$quem_maiusculo, robometria_r1_verbo( $item, 'vende', 'vendem' ),\n"
                "			$artigo, $tipo, $avulso, $pronome,\n"
                "			$identificacao, $quem, $declara, $lista, $rotulo_origem, $data",
                "que o fabricante declara compatível com %8$s (%9$s, verificado em %10$s).',\n"
                "			$quem_maiusculo, robometria_r1_verbo( $item, 'vende', 'vendem' ),\n"
                "			$artigo, $tipo, $avulso, $pronome,\n"
                "			$identificacao, $lista, $rotulo_origem, $data")(base),
            trocar(
                REFERENCIA,
                '"%s nao %s %s %s %s para este modelo: %s vem dentro do kit %s, que %s "\n'
                '            "%s compativel com %s (%s, verificado em %s)."\n'
                '            % (quem_maiusculo, vende, artigo, dentro_do_kit, avulso, pronome,\n'
                '               identificacao, quem, declara, lista, fonte.get("origem"), data)',
                '"%s nao %s %s %s %s para este modelo: %s vem dentro do kit %s, que o "\n'
                '            "fabricante declara compativel com %s (%s, verificado em %s)."\n'
                '            % (quem_maiusculo, vende, artigo, dentro_do_kit, avulso, pronome,\n'
                '               identificacao, lista, fonte.get("origem"), data)')(base),
        ),
        False,
    ),
    # -------------------------------------------- MUTACOES QUE PRODUZEM O MUNDO
    #
    # O PAR ABAIXO E UM SO ARGUMENTO, e ele so existe inteiro: a MESMA troca —
    # o cartao citando a MARCA derivada do id da peca em vez de quem publicou —
    # PASSA LIMPA no banco de hoje e REPROVA no mundo produzido. E a prova, e
    # nao a promessa, de que a assistencia autorizada comprou cobertura: sem
    # ela, "cita quem publicou" e "cita a marca" sao a mesma medicao, e a regua
    # ficaria verde exatamente dentro do proprio buraco.
    (
        'o cartao cita a MARCA em vez de quem publicou, no banco de hoje',
        'a previsao era que esta passasse limpa, e ela REPROVOU: a regua cobra o '
        'publicador inteiro, e o parenteses que a coleta transcreveu ja separa a '
        'marca de quem transcreveu ("Electrolux" nao e "Electrolux (loja '
        'oficial)"). E a atribuicao errada mais provavel de todas — a que alguem '
        'escreveria de boa-fe achando que esta citando a fonte',
        trocar(
            SNIPPET,
            "			robometria_r1_lista( $tipos_do_cartao ),\n"
            "			robometria_r1_quem_publica( $i ),\n"
            "			robometria_r1_verbo( $i, 'declara', 'declaram' )\n"
            "		) ) . '</span>';",
            "			robometria_r1_lista( $tipos_do_cartao ),\n"
            "			ucfirst( strtok( $i['peca'], '-' ) ),\n"
            "			'declara'\n"
            "		) ) . '</span>';"),
        False,
    ),
    (
        'PRODUZ O MUNDO: a mesma troca, com a assistencia autorizada publicando',
        'o caso extremo, que o banco de hoje nao tem: quem publica no degrau 4 e '
        'uma rede autorizada, que fala pela marca e nao divide uma letra com o '
        'nome dela. A regua tem de morder tambem aqui, e nao so quando sobra do '
        'publicador um pedaco que a marca nao cobre',
        lambda base: (
            mundo_da_assistencia(base),
            trocar(
                SNIPPET,
                "			robometria_r1_lista( $tipos_do_cartao ),\n"
                "			robometria_r1_quem_publica( $i ),\n"
                "			robometria_r1_verbo( $i, 'declara', 'declaram' )\n"
                "		) ) . '</span>';",
                "			robometria_r1_lista( $tipos_do_cartao ),\n"
                "			ucfirst( strtok( $i['peca'], '-' ) ),\n"
                "			'declara'\n"
                "		) ) . '</span>';")(base),
        ),
        False,
    ),
    (
        'PRODUZ O MUNDO: a assistencia autorizada entra e NADA MAIS muda',
        'o mundo produzido, sozinho, tem de continuar passando. Sem esta, a '
        'mutacao de cima poderia estar reprovando por causa do banco trocado, e '
        'nao por causa da troca do publicador — e a regua nao teria medido nada',
        mundo_da_assistencia,
        True,
    ),
    (
        'o mundo intacto',
        'mundo sadio que reprova e falso-positivo, e regua que reprova tudo nao '
        'mede nada',
        intacto,
        True,
    ),
]


def rodar(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)


def medir(base_dir):
    """Regera o catalogo da R1 e roda o teste-r1.php inteiro.

    Falha de geracao conta como REPROVACAO: o que importa e que o defeito NAO
    passe, e ilha que nao monta tambem nao publica.
    """
    r = rodar([sys.executable, 'ferramentas/gerar-r1.py', '--gravar'], base_dir)
    if r.returncode != 0:
        return r.returncode, 'gerar-r1.py falhou (a mutacao derrubou a geracao)'
    r = rodar(['php', 'ferramentas/teste-r1.php', '.'], base_dir)
    linhas = [l for l in r.stdout.strip().splitlines() if l.strip()]
    return r.returncode, (linhas[-1] if linhas else '(sem saida)')


def copiar(destino):
    for item in ('dados', 'ferramentas', 'snippets', 'manifest.json', 'ARVORE.md'):
        origem = os.path.join(RAIZ, item)
        alvo = os.path.join(destino, item)
        if os.path.isdir(origem):
            shutil.copytree(origem, alvo)
        else:
            shutil.copy2(origem, alvo)


def main():
    print('MUTACOES DA ATRIBUICAO — quem declara e o publicador, e isso se mede')
    print('=' * 78)
    erros = 0
    inertes = 0
    for nome, porque, aplicar, tem_de_passar in MUTACOES:
        with tempfile.TemporaryDirectory() as tmp:
            base = os.path.join(tmp, 'ilha')
            os.makedirs(base)
            copiar(base)
            aplicar(base)
            codigo, ultima = medir(base)
        passou = codigo == 0
        certo = passou is tem_de_passar
        if not certo:
            erros += 1
        if aplicar is not intacto and passou and not tem_de_passar:
            inertes += 1
        print('  %s %s' % ('ok    ' if certo else 'ERRO  ', nome))
        print('         %s' % ultima)
        if not certo:
            print('         esperado: %s' % ('PASSAR' if tem_de_passar else 'REPROVAR'))
            print('         por que: %s' % porque)
    print('=' * 78)
    if erros:
        print('%d de %d mutacoes NAO se comportaram como declarado (%d inerte(s)).'
              % (erros, len(MUTACOES), inertes))
        sys.exit(1)
    print('%d de %d: toda trava foi vista reprovando, e os mundos sadios passaram.'
          % (len(MUTACOES), len(MUTACOES)))


if __name__ == '__main__':
    main()
