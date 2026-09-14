#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Devolve o artigo digitado as frases publicadas, e exige REPROVACAO.

    python3 ferramentas/mutacoes-artigo-do-publicador.py

POR QUE ESTE ARQUIVO EXISTE
---------------------------
"A PROVA DE QUE UMA TRAVA REPROVA E PARTE DO BLOCO" (secao 8 do ARQUIPELAGO.md).
A secao 18 do teste-r1.php, a secao nova do teste-a1.php e a do teste-r2.php
nasceram em 14/09/2026 e nasceram VERDES sobre o estado ja consertado — o que e
informacao sobre o conserto e nenhuma informacao sobre a regua.

O DEFEITO QUE ELAS EXISTEM PARA PEGAR ESTAVA NO AR, e ele e a divida (a) do
bloco das 11h44Z um degrau acima. Aquele bloco tirou "o fabricante declara",
digitado, do lugar de quem publicou. O que ficou digitado foi o ARTIGO: "A %s
declara", "que a %s declara", "a %s declara esta peca", " da " antes do nome, e
"a recomendacao dele fica folgada" na R2. Cinco formas, quatro arquivos, e todas
certas — por acidente do banco. Todo publicador que chegava a essas frases e
feminino singular, e o banco JA TINHA os dois contraexemplos sem que nenhuma
frase os citasse: "Mundo Conectado", masculino, e "Lojas WAP", plural.

E A R2 PROVA QUE ISSO NAO SE CONSERTA SOZINHO: la o artigo ja vinha do dado
desde 11/09, e mesmo assim o PRONOME da faixa confortavel estava digitado, certo
pelo mesmo acidente ao contrario (o unico publicador com faixa e masculino).
Meia regra aplicada parece regra aplicada.

O QUE ESTA BATERIA MEDE, e o que ela NAO mede: ela reescreve as frases com o
artigo digitado de volta e cobra reprovacao; e produz o mundo que o banco da R1
nao tem — um publicador PLURAL publicando peca — para separar "a regua mede a
gramatica" de "a regua mede o texto que existe hoje".

AS DUAS ULTIMAS TEM DE PASSAR: mundo intacto que reprova e falso-positivo, e
regua que reprova tudo "pega" qualquer defeito sem medir nenhum.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R1 = 'snippets/robometria-r1.php'
A1 = 'snippets/robometria-a1.php'
R2 = 'snippets/robometria-r2.php'
GERADOR_R1 = 'ferramentas/gerar-r1.py'
GERADOR_A1 = 'ferramentas/gerar-a1.py'
PUBLICADORES = 'dados/publicadores.json'
ESQUEMA = 'dados/esquema-banco.json'
PECAS = 'dados/pecas.json'
MARCAS = 'dados/marcas.json'
A1_FATOS = 'dados/a1-fatos.json'
CONSTANTES = 'dados/constantes.json'


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


def mundo_conectado_vira_feminino(doc):
    """O unico publicador MASCULINO do banco passa a declarar 'a'.

    Nao estraga nenhuma frase sozinho: estraga a concordancia que a R2 publica,
    e e a prova de que as reguas leem o BANCO e nao a copia que o gerador gravou.
    """
    for reg in doc['registros']:
        if reg['nome'] == 'Mundo Conectado':
            reg['artigo'] = 'a'
            return
    raise AssertionError('Mundo Conectado saiu de publicadores.json: esta '
                         'mutacao nao tem mundo para produzir')


def some_o_registro_da_xiaomi(doc):
    """Um publicador que as respostas da R1 citam perde o registro.

    A regua que le "so o que esta declarado" aprovaria tudo em silencio; o que
    tem de acontecer e o gerador PARAR com o nome dele na mensagem.
    """
    antes = len(doc['registros'])
    doc['registros'] = [r for r in doc['registros'] if r['nome'] != 'Xiaomi']
    if len(doc['registros']) == antes:
        raise AssertionError('Xiaomi nao estava em publicadores.json')


def some_a_tabela_do_esquema(doc):
    """A lista de artigos some do esquema (26.2: 'a trava tem de reprovar quando
    a lista some'). Nenhum registro do banco e estragado: o que se apaga e a
    declaracao de onde a gramatica se deriva."""
    if 'artigos_de_publicador' not in doc:
        raise AssertionError('artigos_de_publicador ja nao esta no esquema')
    del doc['artigos_de_publicador']


def publicador_vira_plural(doc):
    """PRODUZ O MUNDO: quem publica peca no degrau 4 e um nome PLURAL.

    O banco da R1 nao tem nenhum, e por isso toda frase dela podia escrever
    'declara' no singular por tres blocos sem nunca poder falhar. 'Lojas WAP' ja
    e citado em modelos-robo.json e ja tem artigo declarado — o que muda aqui e
    ele passar a publicar PECA, que e onde as quatro frases moram.
    """
    tocou = 0
    for reg in doc['registros']:
        for fonte in (reg.get('fontes') or {}).values():
            if fonte.get('nivel') == 4:
                fonte['publicador'] = 'Lojas WAP'
                tocou += 1
    if not tocou:
        raise AssertionError('nenhuma fonte de nivel 4 no banco: o mundo desta '
                             'mutacao nao pode ser produzido, e ela mediria nada')


def marca_de_maior_alcance_vira_plural(base_dir):
    """PRODUZ O MUNDO do artigo-ancora: a marca que ele mais cita passa a ter
    nome PLURAL.

    O A1 escreve o publicador a partir do `nome` da marca, e as cinco marcas do
    banco sao femininas singulares — entao "a Multi declara" e " da Multi"
    digitados sao indistinguiveis dos derivados. Com "Lojas WAP" no lugar, o
    digitado publica "a Lojas WAP declara" e " da Lojas WAP", e a regua morde.
    "Lojas WAP" ja e citado em modelos-robo.json e ja tem artigo declarado: o
    mundo produzido nao inventa publicador nenhum.

    A MARCA E COMPUTADA, NUNCA CRAVADA, e isso custou uma mutacao INERTE em
    14/09/2026 para ficar claro. Esta funcao dizia `if reg['id'] == 'multi'`,
    porque a peca de maior alcance do banco era da Multi no dia em que a bateria
    nasceu. A leva do Xiaomi S10 alargou a B106GL-BX para SEIS codigos
    declarados e o maior alcance trocou de dono — a mutacao do " da " digitado
    passou a produzir um mundo em que a Multi e plural e a frase do maior
    alcance nomeia a Xiaomi, singular. O digitado e o derivado voltaram a ser a
    mesma letra, a mutacao editou o arquivo e NAO reprovou nada: verde por nao
    medir. Regua que crava o dado de hoje envelhece calada assim que o banco
    cresce, que e justamente o que o banco existe para fazer. Agora o alvo sai
    de `a1-fatos.json`, que e o mesmo lugar de onde a frase mutada tira o nome.
    """
    with open(os.path.join(base_dir, A1_FATOS), encoding='utf-8') as fh:
        alvo = json.load(fh)['maior_alcance']['marca']
    caminho = os.path.join(base_dir, MARCAS)
    with open(caminho, encoding='utf-8') as fh:
        doc = json.load(fh)
    for reg in doc['registros']:
        if reg['id'] == alvo:
            reg['nome'] = 'Lojas WAP'
            with open(caminho, 'w', encoding='utf-8') as fh:
                json.dump(doc, fh, ensure_ascii=False, indent=1)
                fh.write('\n')
            return
    raise AssertionError(
        'a marca %r, que o maior alcance do A1 nomeia, nao existe em '
        'marcas.json: esta mutacao nao tem mundo para produzir' % alvo)


def faixa_confortavel_vira_feminina(doc):
    """PRODUZ O MUNDO da R2: quem publica a faixa confortavel passa a ser a
    Canaltech, que e feminina.

    Hoje a unica faixa do banco e do Mundo Conectado, masculino — entao o "dele"
    digitado e o derivado sao a mesma letra. O publicador da R2 sai do prefixo do
    campo `fonte`, entao e ele que muda; nenhum numero e tocado.
    """
    for c in doc['constantes']:
        if c.get('faixa_confortavel') and c['fonte'].startswith('Mundo Conectado'):
            c['fonte'] = 'Canaltech' + c['fonte'][len('Mundo Conectado'):]
            return
    raise AssertionError('nenhuma constante com faixa confortavel publicada pelo '
                         'Mundo Conectado: o mundo desta mutacao nao existe')


def intacto(base_dir):
    return None


MUTACOES = [
    (
        'a frase da peca avulsa volta a escrever "A " digitado',
        'o molde mais comum da R1 — 52 dos 73 itens do banco de hoje passam por '
        'ele — e o lugar em que o artigo digitado vivia desde que a ferramenta '
        'nasceu',
        trocar(
            R1,
            "			'%1$s %2$s %3$s %4$s %5$s compatível com %6$s (%7$s, verificado em %8$s).',\n"
            "			$quem_maiusculo, $declara, $artigo, $tipo, $identificacao,",
            "			'A %1$s declara %2$s %3$s %4$s compatível com %5$s (%6$s, verificado em %7$s).',\n"
            "			$item['publicador'], $artigo, $tipo, $identificacao,"),
        False,
    ),
    (
        'a frase do kit sem avulso volta a escrever "A " e "que a " digitados',
        'a frase mais longa da ferramenta, e a unica que poe o publicador DUAS '
        'vezes: um conserto pela metade deixaria uma das duas errada',
        trocar(
            R1,
            "			'%1$s não %2$s %3$s %4$s %5$s para este modelo: %6$s vem dentro do kit %7$s, que %8$s %9$s compatível com %10$s (%11$s, verificado em %12$s).',\n"
            "			$quem_maiusculo, robometria_r1_verbo( $item, 'vende', 'vendem' ),\n"
            "			$artigo, $tipo, $avulso, $pronome,\n"
            "			$identificacao, $quem, $declara, $lista, $rotulo_origem, $data",
            "			'A %1$s não vende %2$s %3$s %4$s para este modelo: %5$s vem dentro do kit %6$s, que a %7$s declara compatível com %8$s (%9$s, verificado em %10$s).',\n"
            "			$item['publicador'], $artigo, $tipo, $avulso, $pronome,\n"
            "			$identificacao, $item['publicador'], $lista, $rotulo_origem, $data"),
        False,
    ),
    (
        'o cartao da vitrine da R1 volta a escrever "a " digitado',
        'a outra superficie da MESMA tela: o bloco das 11h44Z ja tinha pago por '
        'consertar a frase e esquecer o cartao',
        trocar(
            R1,
            "				? '%3$s %4$s este kit compatível com o seu %1$s, e é dentro dele que vem %2$s'\n"
            "				: '%3$s %4$s esta peça (%2$s) compatível com o seu %1$s',",
            "				? 'a %3$s declara este kit compatível com o seu %1$s, e é dentro dele que vem %2$s'\n"
            "				: 'a %3$s declara esta peça (%2$s) compatível com o seu %1$s',"),
        False,
    ),
    (
        'o verbo da R1 para de concordar e volta a ser sempre singular',
        'a metade da regra que e mais facil esquecer: o artigo certo com o verbo '
        'errado publica "as Lojas WAP declara", que e pior do que o defeito '
        'antigo porque parece conserto',
        trocar(
            R1,
            "	return ( 'plural' === $g['numero'] ) ? $plural : $singular;\n}\n}\n\n/**\n * A ORAÇÃO EM QUE ESTE ITEM ATRIBUI",
            "	return $singular;\n}\n}\n\n/**\n * A ORAÇÃO EM QUE ESTE ITEM ATRIBUI"),
        False,
    ),
    (
        'a R1 volta a ADIVINHAR o artigo, com "a" como padrao silencioso',
        'e o defeito na sua forma mais provavel: nao alguem digitando "A" numa '
        'frase, e alguem escrevendo um padrao razoavel para quando o dado '
        'faltar. Padrao silencioso e adivinhacao com cara de robustez',
        trocar(
            R1,
            "		'artigo'    => isset( $g['artigo'] ) ? $g['artigo'] : '',\n"
            "		'maiuscula' => isset( $g['maiuscula'] ) ? $g['maiuscula'] : '',\n"
            "		'numero'    => isset( $g['numero'] ) ? $g['numero'] : 'singular',",
            "		'artigo'    => 'a',\n"
            "		'maiuscula' => 'A',\n"
            "		'numero'    => 'singular',"),
        False,
    ),
    (
        'o gerador da R1 para de carregar a gramatica para a tela',
        'sem o fato, o snippet cai no vazio e a frase sai sem artigo nenhum: '
        'visivel, e por isso o caminho certo — mas ainda assim uma frase '
        'publicada quebrada, e a regua tem de morder',
        trocar(
            GERADOR_R1,
            '        "gramatica_do_publicador": gramatica_do(\n'
            '            fonte.get("publicador") or ref.marcas[peca["marca"]]["nome"]),\n'
            '        "origem": fonte.get("origem"),\n'
            '        "nivel_da_fonte": fonte.get("nivel"),',
            '        "origem": fonte.get("origem"),\n'
            '        "nivel_da_fonte": fonte.get("nivel"),'),
        False,
    ),
    # -- O A1 E A R2 SO SE MEDEM COM O MUNDO PRODUZIDO -------------------------
    #
    # As tres trocas abaixo PASSAM LIMPAS no banco de hoje, e isso foi MEDIDO
    # antes de elas virarem par: o A1 escreve o publicador a partir do `nome` da
    # marca, e as cinco marcas sao femininas singulares; a unica faixa confortavel
    # da R2 e do Mundo Conectado, masculino. Ou seja, "a Multi declara" digitado e
    # o derivado sao a MESMA letra, e "dele" digitado tambem. Nenhuma regua pode
    # separar os dois sem um mundo em que eles diferem — e a primeira escrita
    # desta bateria provou isso deixando as tres INERTES.
    (
        'PRODUZ O MUNDO: a marca do A1 e PLURAL, e o cartao volta a escrever "a " digitado',
        'no mundo de hoje esta troca passa limpa, porque "a Multi declara" '
        'digitado e o derivado sao a mesma letra. Com a marca plural, o digitado '
        'publica "a Lojas WAP declara" e a regua morde',
        lambda base: (
            marca_de_maior_alcance_vira_plural(base),
            trocar(
                A1,
                "				? '%1$s %5$s este kit para %2$d código%3$s de modelo: %4$s'\n"
                "				: '%1$s %5$s esta peça para %2$d código%3$s de modelo: %4$s',\n"
                "			robometria_a1_quem_publica( $i ),",
                "				? 'a %1$s declara este kit para %2$d código%3$s de modelo: %4$s'\n"
                "				: 'a %1$s declara esta peça para %2$d código%3$s de modelo: %4$s',\n"
                "			$i['publicador'],")(base),
        ),
        False,
    ),
    (
        'PRODUZ O MUNDO: a marca do A1 e PLURAL, e o maior alcance volta a " da " digitado',
        'a CONTRACAO e o caso que mais engana, porque nem parece artigo: '
        '"do Mundo Conectado" e "das Lojas WAP" quebram na mesma linha',
        lambda base: (
            marca_de_maior_alcance_vira_plural(base),
            trocar(
                A1,
                "		. esc_html( robometria_a1_quem_publica_com_de( $maior ) ) . ': o fabricante a declara para '",
                "		. 'da ' . esc_html( $maior['publicador'] ) . ': o fabricante a declara para '")(base),
        ),
        False,
    ),
    (
        'PRODUZ O MUNDO: a marca do A1 e PLURAL e NADA MAIS muda',
        'o mundo produzido, sozinho, tem de continuar passando — senao as duas de '
        'cima estariam reprovando por causa do nome trocado, e nao por causa do '
        'artigo digitado',
        marca_de_maior_alcance_vira_plural,
        True,
    ),
    (
        'PRODUZ O MUNDO: quem publica a faixa da R2 e FEMININA, e o pronome volta a ser digitado',
        'a metade que sobrevivia mesmo com o artigo ja vindo do dado desde 11/09: '
        'meia regra aplicada parece regra aplicada. So com a Canaltech publicando '
        'a faixa e que "dele" digitado deixa de coincidir com o derivado',
        lambda base: (
            editar_json(CONSTANTES, faixa_confortavel_vira_feminina)(base),
            trocar(
                R2,
                "			'%s ainda descreve uma faixa confortável entre %s e %s Pa para esta situação — não é um limiar, é onde a recomendação %s fica folgada.',\n"
                "			$f['publicador'], robometria_r2_n( $f['de'] ), robometria_r2_n( $f['ate'] ),\n"
                "			isset( $f['pronome_possessivo'] ) ? $f['pronome_possessivo'] : 'dela'",
                "			'%s ainda descreve uma faixa confortável entre %s e %s Pa para esta situação — não é um limiar, é onde a recomendação dele fica folgada.',\n"
                "			$f['publicador'], robometria_r2_n( $f['de'] ), robometria_r2_n( $f['ate'] )")(base),
        ),
        False,
    ),
    (
        'PRODUZ O MUNDO: a faixa da R2 muda de publicador e NADA MAIS muda',
        'o mundo produzido, sozinho, tem de continuar passando',
        editar_json(CONSTANTES, faixa_confortavel_vira_feminina),
        True,
    ),
    (
        'o banco declara "a" para o unico publicador MASCULINO',
        'nenhum arquivo de codigo e tocado: so o dado. E a prova de que as reguas '
        'leem publicadores.json e nao a copia que o gerador gravou — se lessem a '
        'copia, banco e tela errariam juntos e tudo ficaria verde',
        editar_json(PUBLICADORES, mundo_conectado_vira_feminino),
        False,
    ),
    (
        'um publicador que a R1 cita perde o registro no banco',
        'o caso que a regua nao pode tratar com silencio: sem artigo declarado a '
        'frase teria de adivinhar, e o certo e o gerador PARAR com o nome dele na '
        'mensagem',
        editar_json(PUBLICADORES, some_o_registro_da_xiaomi),
        False,
    ),
    (
        'a LISTA DE ARTIGOS some do esquema',
        'a mutacao da 26.2, e ela nao estraga registro nenhum: regua que le a '
        'propria lista de um arquivo de dados aprova tudo, em silencio, no dia em '
        'que o arquivo perder a chave',
        editar_json(ESQUEMA, some_a_tabela_do_esquema),
        False,
    ),
    # -------------------------------------------- MUTACOES QUE PRODUZEM O MUNDO
    #
    # O PAR ABAIXO E UM SO ARGUMENTO. O banco da R1 nao tem publicador plural
    # nenhum, entao "declara" no singular esta certo em todas as 73 respostas —
    # e ficaria verde com o verbo cravado. So o mundo produzido separa "a regua
    # mede a concordancia" de "a regua mede o texto de hoje".
    (
        'PRODUZ O MUNDO: quem publica peca e PLURAL, e o verbo volta a ser cravado',
        'no mundo de hoje a mutacao do verbo cravado reprova pela secao 18, que '
        'forja os mundos em memoria; aqui ela reprova tambem pelo BANCO, que e '
        'onde o defeito chegaria de verdade',
        lambda base: (
            editar_json(PECAS, publicador_vira_plural)(base),
            trocar(
                R1,
                "	return ( 'plural' === $g['numero'] ) ? $plural : $singular;\n}\n}\n\n/**\n * A ORAÇÃO EM QUE ESTE ITEM ATRIBUI",
                "	return $singular;\n}\n}\n\n/**\n * A ORAÇÃO EM QUE ESTE ITEM ATRIBUI")(base),
        ),
        False,
    ),
    (
        'PRODUZ O MUNDO: o publicador plural entra e NADA MAIS muda',
        'o mundo produzido, sozinho, tem de continuar passando. Sem esta, a de '
        'cima poderia estar reprovando por causa do banco trocado e nao por causa '
        'do verbo — e a regua nao teria medido nada',
        editar_json(PECAS, publicador_vira_plural),
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
    """Regera o combustivel das tres superficies e roda os tres testes.

    Falha de geracao conta como REPROVACAO: o que importa e que o defeito NAO
    passe, e ilha que nao monta tambem nao publica. A ordem importa — validar o
    banco primeiro, porque duas mutacoes so tocam dado.
    """
    r = rodar([sys.executable, 'ferramentas/validar-banco.py'], base_dir)
    if r.returncode != 0:
        return r.returncode, 'validar-banco.py reprovou'
    for gerador in ('gerar-r1.py', 'gerar-a1.py', 'gerar-r2.py'):
        r = rodar([sys.executable, 'ferramentas/' + gerador, '--gravar'], base_dir)
        if r.returncode != 0:
            return r.returncode, '%s falhou (a mutacao derrubou a geracao)' % gerador
    ultimo = '(sem saida)'
    for teste in ('teste-r1.php', 'teste-a1.php', 'teste-r2.php'):
        r = rodar(['php', 'ferramentas/' + teste, '.'], base_dir)
        linhas = [l for l in r.stdout.strip().splitlines() if l.strip()]
        ultimo = '%s: %s' % (teste, linhas[-1] if linhas else '(sem saida)')
        if r.returncode != 0:
            return r.returncode, ultimo
    return 0, ultimo


def copiar(destino):
    for item in ('dados', 'ferramentas', 'snippets', 'manifest.json', 'ARVORE.md'):
        origem = os.path.join(RAIZ, item)
        alvo = os.path.join(destino, item)
        if os.path.isdir(origem):
            shutil.copytree(origem, alvo)
        else:
            shutil.copy2(origem, alvo)


def main():
    print('MUTACOES DO ARTIGO DE QUEM PUBLICA — a gramatica sai do banco, e isso se mede')
    print('=' * 78)
    erros = 0
    inertes = 0
    for nome, porque, aplicar, tem_de_passar in MUTACOES:
        with tempfile.TemporaryDirectory() as tmp:
            base = os.path.join(tmp, 'ilha')
            os.makedirs(base)
            copiar(base)
            try:
                aplicar(base)
            except AssertionError as e:
                print('\nx  %s\n   A MUTACAO NAO PODE SER APLICADA: %s' % (nome, e))
                erros += 1
                continue
            codigo, resumo = medir(base)

        passou = (codigo == 0)
        if passou == tem_de_passar:
            marca = 'ok  '
        else:
            marca = 'X   '
            erros += 1
            if not tem_de_passar:
                inertes += 1
        print('\n%s%s' % (marca, nome))
        print('    por que: %s' % porque)
        print('    esperado: %s | medido: %s | %s'
              % ('PASSAR' if tem_de_passar else 'REPROVAR',
                 'passou' if passou else 'reprovou', resumo))

    print('\n' + '=' * 78)
    if erros:
        print('REPROVADO: %d mutacao(oes) fora do esperado (%d delas INERTES — '
              'defeito que a bancada nao ve).' % (erros, inertes))
        sys.exit(1)
    print('APROVADO: %d mutacoes, todas com o resultado esperado, 0 inertes.'
          % len(MUTACOES))


if __name__ == '__main__':
    main()
