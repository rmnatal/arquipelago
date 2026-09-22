#!/usr/bin/env python3
"""
MUTACOES DELIBERADAS CONTRA O PORTAO DO EIXO /peixes/ — Aquametria.

    python3 ferramentas/mutacoes-peixes.py

Cada mutacao quebra a leva de um jeito que ja aconteceu nesta fabrica ou que
aconteceria na proxima leva, numa COPIA da ilha, e roda o
ferramentas/teste-peixes.py nela. Mutacao que PASSA e o portao nao medindo nada —
o defeito que a secao 8 do ARQUIPELAGO.md persegue desde 10/09/2026, quando tres
travas novas da Robometria aprovaram codigo quebrado.

TRES FAMILIAS, e elas nao sao arbitrarias:

  1. O NUMERO MUDA. Regua de lotacao trocada, extremo errado de um conflito
     declarado, borda da tabela que desaparece. E a familia facil de medir.

  2. O NUMERO FICA E A ESTRUTURA QUEBRA. A especie agressiva ganha lista de
     companheiro; o derivado per capita passa a ser multiplicado; a categoria
     sem filhas vira link. Sao as mutacoes que servem um resultado plausivel, e
     por isso sao as que passam quando o portao so pergunta "existe?".

  3. A REGUA PERDE O CHAO. O catalogo do snippet envelhece em relacao ao banco, e
     a colisao de slug volta. Aqui o site continua servindo pagina bonita: o que
     quebra e a relacao entre duas metades que ninguem olha junto.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PEIXES = "snippets/aquametria-peixes.php"
CASCA = "snippets/aquametria-casca.php"
BANCO = "dados/especies-agua-doce.json"


def troca(arquivo, de, para, vezes=1):
    """Substituicao exata, que RECUSA operar se o alvo nao estiver la.

    E a trava contra a mutacao inerte: alvo que nao existe mais nao quebra nada
    e o teste passa por engano — 18 de 20 mutacoes desta ilha viraram inertes de
    uma vez em 11/09/2026, quando a bancada trocou de fonte.
    """
    def aplicar(base):
        caminho = os.path.join(base, arquivo)
        texto = open(caminho, encoding="utf-8").read()
        if texto.count(de) != vezes:
            raise SystemExit(
                "MUTACAO INERTE: %r aparece %d vez(es) em %s, esperava %d"
                % (de, texto.count(de), arquivo, vezes))
        open(caminho, "w", encoding="utf-8").write(texto.replace(de, para, vezes))
    return aplicar


def banco_json(mudar):
    """Mutacao que edita o BANCO pela estrutura, e nao por texto.

    Existe porque as mutacoes desta familia precisam mexer num campo de UM
    registro, e o valor desse campo aparece igual em varios outros — trocar
    "harem" por texto atingiria quatro especies e a mutacao mediria outra coisa.
    A trava contra a mutacao inerte continua de pe: se o banco sair identico, a
    edicao nao encontrou o alvo e isto para.
    """
    def aplicar(base):
        import json as _json
        caminho = os.path.join(base, BANCO)
        d = _json.load(open(caminho, encoding="utf-8"))
        antes = _json.dumps(d, sort_keys=True, ensure_ascii=False)
        mudar(d)
        if _json.dumps(d, sort_keys=True, ensure_ascii=False) == antes:
            raise SystemExit("MUTACAO INERTE: o banco saiu identico ao original")
        _json.dump(d, open(caminho, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return aplicar


def varias(*aplicadores):
    """Mutacao que toca mais de um arquivo, e as duas coisas sao UMA mudanca.

    Existe para as mutacoes que PRODUZEM O MUNDO: acrescentar uma especie
    barrada a uma categoria muda o snippet E a lista que a bancada declara, e
    aplicar so metade mediria a outra afirmacao. Cada aplicador de dentro mantem
    a propria trava contra a mutacao inerte.
    """
    def aplicar(base):
        for a in aplicadores:
            a(base)
    return aplicar


TESTE = "ferramentas/teste-peixes.py"

# O registro inteiro de UMA barrada, como o gerador o escreve. Serve de alvo
# para as mutacoes que apagam e que duplicam — e escrito aqui por extenso
# porque `troca` recusa alvo que nao exista, entao o dia em que o formato do
# gerador mudar esta mutacao para em vez de virar inerte.
BARRADA_ANCISTRUS = """		'ancistrus-cirrhosus' => array(
			'id' => 'ancistrus-cirrhosus',
			'cientifico' => 'Ancistrus cirrhosus',
			'populares' => array(
				'cascudo-ancistrus',
				'ancistrus',
				'cascudo-barbudo',
			),
			'familia' => 'Loricariidae',
			'faltando' => array(
				'temperatura_C',
			),
		),
"""


def inverter_ordem_dos_barrados(base):
    """Poe os barrados na ordem inversa, sem mudar nenhum dado deles.

    A ordem e uma afirmacao da pagina — "de quem esta mais perto de entrar para
    quem esta mais longe" — e afirmacao de ordem so se mede mexendo na ordem e
    em mais nada: trocar um campo junto mediria o campo.
    """
    caminho = os.path.join(base, PEIXES)
    texto = open(caminho, encoding="utf-8").read()
    antes, resto = texto.split("\t$barrados = array(\n", 1)
    corpo, depois = resto.split("\n\t);\n\treturn $barrados;", 1)
    registros = re.findall(r"\t\t'[a-z0-9-]+' => array\(\n.*?\n\t\t\),", corpo, re.S)
    if len(registros) < 2:
        raise SystemExit("MUTACAO INERTE: achei %d barrados, preciso de 2 ou mais" % len(registros))
    novo = "\n".join(reversed(registros))
    if novo == corpo:
        raise SystemExit("MUTACAO INERTE: a ordem invertida e igual a original")
    open(caminho, "w", encoding="utf-8").write(
        antes + "\t$barrados = array(\n" + novo + "\n\t);\n\treturn $barrados;" + depois)


def mut_campo(d, ident, campo, valor):
    """Troca UM campo de UM registro do banco, recusando alvo que nao existe."""
    for e in d["especies"]:
        if e["id"] == ident:
            if campo not in e:
                raise SystemExit("MUTACAO INERTE: %s nao tem o campo %s" % (ident, campo))
            if e[campo] == valor:
                raise SystemExit("MUTACAO INERTE: %s.%s ja vale %r" % (ident, campo, valor))
            e[campo] = valor
            return
    raise SystemExit("MUTACAO INERTE: %s nao esta no banco" % ident)


MUTACOES = [
    # ------------------- 0. o chao declarado e a populacao para quem ele vale
    #
    # AS QUATRO DESTE GRUPO EXERCITAM UM DEFEITO QUE ESTEVE OITO DIAS NO AR: a
    # ficha do apistogramma agassizi servia "para um harem ... 60 cm de frente
    # por 30 cm de fundo", e os 30 cm sao do compendio, que os declarou para UM
    # CASAL. A proibicao existia — escrita, em maiusculas, no `observacao` do
    # proprio registro — e prosa nao barra pagina.
    ("o portao do escopo some — a ficha volta a prometer ao harem o chao do casal",
     troca(PEIXES, "\tif ( ! aquametria_peixes_chao_serve_o_arranjo( $e ) ) {\n\t\treturn null;\n\t}",
           "\tif ( false ) {\n\t\treturn null;\n\t}")),

    ("harem vira populacao de CASAL — o portao passa a aprovar o que ele existe para barrar",
     troca(PEIXES, "'harem'     => 'grupo',", "'harem'     => 'casal',")),

    ("a ordem dos termos inverte — casal passa a cobrir grupo",
     troca(PEIXES, "\t\t'casal'       => 2,", "\t\t'casal'       => 9,")),

    ("a atribuicao do chao volta a perguntar sempre pelo comprimento — 'essa base e o FishBase' outra vez",
     troca(PEIXES, "$larg ? 'base_minima_cm' : 'comprimento_minimo_aquario_cm'",
           "'comprimento_minimo_aquario_cm'")),

    # ---------------------------------------------------- 1. o numero muda
    ("o criterio conservador vira 3 L/cm — a regua brasileira do extremo apertado muda de valor",
     troca(PEIXES, "define( 'AQUAMETRIA_PEIXES_LOTACAO_CONSERVADORA', 4.0 )",
           "define( 'AQUAMETRIA_PEIXES_LOTACAO_CONSERVADORA', 3.0 )")),

    ("a regra classica vira 1,2 cm por litro — o extremo folgado escorrega",
     troca(PEIXES, "define( 'AQUAMETRIA_PEIXES_LOTACAO_CLASSICA', 1.0 )",
           "define( 'AQUAMETRIA_PEIXES_LOTACAO_CLASSICA', 1.2 )")),

    ("o conflito de frente passa a valer pelo extremo MENOR — o mato-grosso vai ao ar com 60 cm",
     troca(PEIXES, "\treturn array( min( $valores ), max( $valores ) );\n}\n}\n\n/**\n * A leitura per capita",
           "\treturn array( min( $valores ), min( $valores ) );\n}\n}\n\n/**\n * A leitura per capita")),

    ("o porte ignora o conflito declarado — o cardinal calcula carga de peixe de 2,5 cm",
     troca(PEIXES, "\t\tif ( 'porte_adulto_cm' !== $c['campo'] ) {", "\t\tif ( true ) {")),

    ("a tabela perde a linha do cardume minimo — a grade deixa de pisar na borda de baixo",
     troca(PEIXES, "\t$degraus = array( $minimo );", "\t$degraus = array();")),

    ("a altura do meio sai da varredura — sobram os dois extremos e nada no meio",
     troca(PEIXES, "\treturn array( 30, 35, 40 );", "\treturn array( 30, 40 );")),

    ("o volume vira litro de etiqueta: divide por 1.100 em vez de 1.000",
     troca(PEIXES, "\treturn ( (float) $comprimento_cm * (float) $largura_cm * (float) $altura_cm ) / 1000.0;",
           "\treturn ( (float) $comprimento_cm * (float) $largura_cm * (float) $altura_cm ) / 1100.0;")),

    ("quantos cabem passa a arredondar para cima — o aquario ganha um peixe que nao cabe",
     troca(PEIXES, "'classica'     => (int) floor( ( $litros / AQUAMETRIA_PEIXES_LOTACAO_CLASSICA ) / $porte ),",
           "'classica'     => (int) ceil( ( $litros / AQUAMETRIA_PEIXES_LOTACAO_CLASSICA ) / $porte ),")),

    # ------------------------------- 2. o numero fica e a estrutura quebra
    ("a especie AGRESSIVA volta a ganhar lista de companheiro — tetra neon como vizinho do mato-grosso",
     troca(PEIXES, "\tif ( 'agressivo' === $e['comportamento'] ) {\n\t\t$total_faixa",
           "\tif ( false && 'agressivo' === $e['comportamento'] ) {\n\t\t$total_faixa")),

    ("o companheiro agressivo deixa de ser filtrado e entra na tabela de quem divide a agua",
     troca(PEIXES, "\t\tif ( 'agressivo' === $o['comportamento'] ) {\n\t\t\t$agressivos[] = $outro_id;\n\t\t\tcontinue;\n\t\t}",
           "\t\tif ( false ) {\n\t\t\t$agressivos[] = $outro_id;\n\t\t\tcontinue;\n\t\t}")),

    ("O DERIVADO PER CAPITA VOLTA A SER MULTIPLICADO: a tabela ganha coluna de frente por cardume",
     troca(PEIXES, "<th scope=\"col\">Soma dos comprimentos</th>'",
           "<th scope=\"col\">Soma dos comprimentos</th><th scope=\"col\">Frente necessaria</th>'")),

    ("a frase que diz que multiplicar nao tem fonte desaparece",
     troca(PEIXES, "' cm, o que nenhuma fonte sustenta.</p>';", "' cm.</p>';")),

    ("uma categoria VAZIA e registrada como pagina — a 16.5 ao contrario, e ela nasceria no proximo Sync",
     troca(PEIXES, "\t\t'tetras' => array(\n\t\t\t'nivel'    => 2,",
           "\t\t'corydoras' => array(\n\t\t\t'nivel'    => 2,\n\t\t\t'pai'      => 'peixes',\n"
           "\t\t\t'titulo'   => 'Corydoras: quantos litros o grupo pede',\n"
           "\t\t\t'conteudo' => '[aquametria_peixes_categoria]',\n"
           "\t\t\t'consulta' => 'quantos litros para corydoras',\n"
           "\t\t\t'porque'   => 'sem filha nenhuma, e e esse o defeito',\n\t\t),\n"
           "\t\t'tetras' => array(\n\t\t\t'nivel'    => 2,")),

    ("a tabela da categoria passa a ordenar por porte — quem procura aquario pequeno le a lista errada",
     troca(PEIXES, "\t\t$fa = aquametria_peixes_frente_faixa( $a );\n\t\t$fb = aquametria_peixes_frente_faixa( $b );",
           "\t\t$fa = array( 0, (float) $a['porte_cm'] );\n\t\t$fb = array( 0, (float) $b['porte_cm'] );")),

    ("uma especie sai da lista de tetras — a contagem da tela continua bonita e o banco fica maior que ela",
     troca(PEIXES, "\t\t\t\t'gymnocorymbus-ternetzi',\n", "")),

    ("o nome de campo do esquema volta a sair na tela do bloco de divergencia",
     troca(PEIXES, "\t\t\tlist( $rotulo_campo, $unidade ) = aquametria_peixes_campo_na_tela( $c['campo'] );",
           "\t\t\tlist( $rotulo_campo, $unidade ) = array( $c['campo'], '' );")),

    ("a ficha passa a declarar Product no JSON-LD — especie com schema de produto, sem preco nem estoque",
     troca(PEIXES, "\t\t\t'@type'         => 'Article',", "\t\t\t'@type'         => 'Product',")),

    ("o paragrafo que explica a ausencia do link de loja sai, e o silencio parece defeito",
     troca(PEIXES, "\t$html .= '<p class=\"aqm-px-sem-loja\"><strong>Nesta página não tem link de loja",
           "\t$html .= '<p class=\"aqm-px-sem-loja\" hidden><strong>Nesta pagina nao tem nada")),

    ("um terceiro bloco de prova embrulha a tabela — a marcacao da camada de prova viraria porta dos fundos",
     troca(PEIXES, "\t$html .= '<div class=\"aqm-px-rolagem\"><table class=\"aqm-px-tabela aqm-px-declarado\">';",
           "\t$html .= '<div class=\"aqm-prova\"><table class=\"aqm-px-tabela aqm-px-declarado\">';")),

    ("a resposta do FAQ cita um numero que a pagina nao serve — schema prometendo o que a tela nao tem",
     troca(PEIXES, "\t\t\t\t. ' litros brutos de lâmina.';", "\t\t\t\t. ' litros brutos, com 41 cm de coluna.';")),

    ("a ancora da filha vira 'saiba mais' na tabela da categoria",
     troca(PEIXES, "\t\t\t\t\t. esc_html( $registro[ $com_ficha[ $id ] ]['titulo'] ) . '</a>';",
           "\t\t\t\t\t. 'Saiba mais' . '</a>';")),

    ("a promessa da secao 14.9 sai do registro de uma ficha — pagina que nao sabe o que mira",
     # A ANCORA GANHOU CONTEXTO NA LEVA 3, e a trava anti-inercia e quem cobrou:
     # ate aqui ela era o prefixo "...: o top 7", que bastava porque so uma
     # pagina do eixo abria assim. A categoria /peixes/corydoras/ nasceu com uma
     # SERP de sete resultados tambem, o prefixo passou a casar duas vezes e o
     # `troca` recusou operar em vez de mutar a pagina errada em silencio. E o
     # caso exato para o qual a recusa foi escrita, e a primeira vez que ela
     # disparou por crescimento do conteudo e nao por troca de bancada.
     troca(PEIXES, "\t\t\t'porque'   => 'Medido em 12/09/2026: o top 7 é blog de nicho",
                   "\t\t\t'x_porque' => 'Medido em 12/09/2026: o top 7 é blog de nicho")),

    # ------------------------------------- 3. a regua perde o chao
    ("A COLISAO DE SLUG VOLTA: a categoria do C8 se chama 'peixes' outra vez",
     troca(CASCA, "\t\t'lotacao'           => 'Lotação',", "\t\t'peixes'            => 'Lotação',")),

    ("o catalogo do snippet envelhece: o porte do neon muda no banco e ninguem roda o gerador",
     troca(BANCO, '"porte_adulto_cm": 2.2,', '"porte_adulto_cm": 2.4,')),

    # -------------------------------------------------- 4. as regras da leva 2
    #
    # As seis abaixo nasceram com a leva 2 (12/09/2026). As cinco primeiras sao
    # das familias 2 e 3: o numero continua certo e o que quebra e o ESCOPO da
    # frase, a lista que devia crescer junto com o eixo, ou a regra que so morde
    # numa borda que o mundo acabou de produzir.

    # O ALVO FOI REAPONTADO EM 13/09/2026: a abertura deixou de citar a fonte
    # (item 4 do despacho) e esta mutacao ficou INERTE na primeira rodada depois
    # da mudanca — o proprio mutador avisou, e e por isso que ele conta as
    # ocorrencias em vez de substituir em silencio. Mutacao que nao morde e teste
    # verde com outro nome.
    ("BASE VIRA FRENTE: a ficha sem fundo declarado passa a falar da BASE do aquario",
     troca(PEIXES,
           "\t\t$html .= ', e o fundo fica em aberto. O que manda é o COMPRIMENTO do '\n\t\t\t. 'aquário, não o litro.</p>';",
           "\t\t$html .= '. O que manda é a BASE do aquário, não o litro.</p>';")),

    ("O SUMICO SILENCIOSO VOLTA: a pagina sem fundo declarado para de dizer que as tabelas nao saem",
     troca(PEIXES,
           "\t\t$html .= '<p class=\"aqm-px-sem-fundo\">",
           "\t\t$html .= '<p class=\"aqm-px-sem-fundo-desligado\" style=\"display:none\">")),

    ("A ATRIBUICAO ERRA O CAMPO: a fonte do comprimento e anunciada como fonte da base",
     troca(PEIXES,
           "'Quem declara ' . ( $larg ? 'essa base' : 'esse comprimento' ) . ' é o '",
           "'Quem declara essa base é o '")),

    # AS DUAS METADES DO PORTAO DO CARDUME, e cada uma sozinha e inerte.
    #
    # A primeira versao desta mutacao so afrouxava a regua — e PASSOU, porque
    # nenhuma ficha registrada hoje depende dela: com o mundo de hoje, `return
    # true` e `return a regra` dao o mesmo site. E a licao do Clube do Mosaico em
    # 12/09/2026, LEVA 3: AS DUAS MUTACOES DO CARDUME PERDERAM O CHAO E FORAM
    # REESCRITAS. Ate a leva 2 elas registravam a coridora sterbai como ficha
    # para provar que o portao recusa "especie de cardume sem o numero do
    # cardume" — e funcionavam porque a sterbai era, no banco, a unica especie
    # do catalogo nesse estado. Esta leva colheu o numero dela: `podem virar
    # ficha` passou de 26 de 27 para 27 de 27, e com isso O CASO DISCRIMINANTE
    # DEIXOU DE EXISTIR no banco. As duas mutacoes teriam virado inertes de um
    # jeito especialmente traicoeiro — continuariam REPROVANDO, agora por slug
    # duplicado no registro, e o placar seguiria verde medindo outra coisa.
    #
    # Entao elas voltam a PRODUZIR O MUNDO, que e a mesma licao da leva 2 escrita
    # do outro lado: tirar o numero de quem o tem, em vez de dar pagina a quem
    # nao o tinha. E sao duas porque medem metades diferentes — uma tira o
    # numero do BANCO (a regua do teste e recomputada dele, e tem de acusar a
    # ficha que sobrou apontando para especie que nao passa mais), a outra tira
    # do CATALOGO DO SNIPPET (o site serve a tabela abrindo em UM exemplar, e
    # quem tem de acusar e a pagina).
    # A EDICAO E ESTRUTURAL E NAO DE TEXTO, e a troca aconteceu em 14/09/2026
    # depois de esta mutacao MORRER. Ela estava ancorada num bloco de dez linhas
    # do JSON — campos vizinhos inteiros, escolhidos para nao atingir a coridora
    # panda, que tem o mesmo cardume e a mesma frente. O esquema ganhou UM campo
    # (`cardume_recomendado_ate`, versao 4) entre `cardume_minimo` e o vizinho
    # de baixo, e a ancora deixou de existir em TODOS os registros de uma vez.
    # `banco_json` + `mut_campo` fazem a mesma mudanca pelo id do registro, e o
    # id nao se move quando o esquema cresce.
    ("O BANCO PERDE O CARDUME DE QUEM JA TEM FICHA NO AR: a sterbai volta a 'grupo' sem numero",
     banco_json(lambda d: (
         mut_campo(d, "corydoras-sterbai", "cardume_minimo", None),
         mut_campo(d, "corydoras-sterbai", "convivencia", "grupo"),
     ))),

    ("O CATALOGO DO SNIPPET PERDE O CARDUME: a ficha da sterbai abre a tabela em UM exemplar",
     troca(PEIXES,
           # O PORTE ENTRA NA ANCORA e nao e decoracao: sem ele a string casa
           # tambem com a coridora panda, que tem o MESMO cardume (6), a MESMA
           # frente (45) e a mesma convivencia. A trava anti-inercia recusou na
           # primeira escrita desta mutacao, e estava certa — mutar as duas de
           # uma vez mediria outra coisa com o mesmo placar verde.
           "\t\t\t'porte_cm' => 6.8,\n\t\t\t'porte_medida' => 'SL',\n\t\t\t'cardume' => 6,\n\t\t\t'cardume_ate' => null,\n\t\t\t'convivencia' => 'cardume',\n\t\t\t'comportamento' => '',\n\t\t\t'frente_cm' => 45,",
           "\t\t\t'porte_cm' => 6.8,\n\t\t\t'porte_medida' => 'SL',\n\t\t\t'cardume' => null,\n"
           "\t\t\t'cardume_ate' => null,\n"
           "\t\t\t'convivencia' => 'grupo',\n\t\t\t'comportamento' => '',\n"
           "\t\t\t'frente_cm' => 45,")),

    # --- LEVA 3: os tres defeitos que a segunda categoria tornou possiveis.
    # Nenhum dos tres podia existir enquanto o eixo teve uma categoria so, e e
    # por isso que nenhuma mutacao antiga os cobre: com uma mae unica, "a mae" e
    # "a mae certa" eram a mesma frase, e o substantivo da categoria era o unico
    # substantivo possivel.

    ("A MAE TROCADA: a ficha da coridora panda nasce registrada debaixo de /peixes/tetras/",
     troca(PEIXES,
           "\t\t'quantos-litros-para-coridora-panda' => array(\n"
           "\t\t\t'nivel'    => 3,\n"
           "\t\t\t'pai'      => 'corydoras',",
           "\t\t'quantos-litros-para-coridora-panda' => array(\n"
           "\t\t\t'nivel'    => 3,\n"
           "\t\t\t'pai'      => 'tetras',")),

    # O DEFEITO QUE ESTA LEVA REALMENTE PRODUZIU, e que o portao pegou antes do
    # ar: a abertura da categoria dizia "São N tetras" com o substantivo
    # digitado, e a pagina das coridoras serviu "São 4 tetras". A contagem
    # estava certa — e e isso que torna o caso perigoso, porque a trava que
    # existia media a contagem.
    ("O SUBSTANTIVO DA CATEGORIA VOLTA A SER DIGITADO: a pagina das coridoras diz 'tetras'",
     troca(PEIXES,
           "$html .= '<p>São ' . esc_html( count( $dentro ) ) . ' '\n\t\t. esc_html( $cat['plural'] )\n\t\t. ' com aquário mínimo declarado por fonte com nome e data, e o mínimo vai de '",
           "$html .= '<p>São ' . esc_html( count( $dentro ) ) . ' '\n\t\t. 'tetras'\n\t\t. ' com aquário mínimo declarado por fonte com nome e data, e o mínimo vai de '")),

    ("O CLUSTER VAZA ENTRE CATEGORIAS: /peixes/corydoras/ passa a listar um tetra",
     troca(PEIXES,
           "\t\t\t'especies' => array(\n"
           "\t\t\t\t'corydoras-aeneus',\n"
           "\t\t\t\t'corydoras-paleatus',\n"
           "\t\t\t\t'corydoras-panda',\n"
           "\t\t\t\t'corydoras-sterbai',\n"
           "\t\t\t),",
           "\t\t\t'especies' => array(\n"
           "\t\t\t\t'corydoras-aeneus',\n"
           "\t\t\t\t'corydoras-paleatus',\n"
           "\t\t\t\t'corydoras-panda',\n"
           "\t\t\t\t'corydoras-sterbai',\n"
           "\t\t\t\t'paracheirodon-innesi',\n"
           "\t\t\t),")),

    ("A PROMESSA DE LEVA VOLTA COM A FILA VAZIA: a categoria fechada diz que ha filhas na fila",
     troca(PEIXES,
           "\tif ( $na_fila > 0 ) {",
           "\tif ( $na_fila >= 0 ) {")),

    # O teto de quatro irmas do 16.4(c) so passou a ser ALCANCAVEL na leva 2:
    # com tres fichas, cada pagina tinha duas irmas e trocar o 4 por 6 nao mudava
    # uma virgula do que o site servia. Esta mutacao era inerte ate hoje.
    ("O TETO DE IRMAS SOME: o cluster passa a servir as seis irmas em vez de ate quatro",
     troca(CASCA, "for ( $n = 1; $n < $total && count( $irmas ) < 4; $n++ ) {",
                  "for ( $n = 1; $n < $total && count( $irmas ) < 6; $n++ ) {")),

    # A RODA VOLTA A SER UMA FILA. Foi assim que o defeito nasceu, e no ar: com
    # teto de quatro e ordem fixa, toda pagina escolhe as mesmas quatro do topo e
    # a cauda da categoria nao e irma de ninguem. Era inerte com tres fichas.
    ("A CAUDA DA CATEGORIA FICA ORFA: as irmas voltam a ser as quatro primeiras do mapa",
     troca(CASCA,
           "\tfor ( $n = 1; $n < $total && count( $irmas ) < 4; $n++ ) {\n"
           "\t\t$irmas[] = $candidatas[ ( $eu + $n ) % $total ];\n"
           "\t}",
           "\tfor ( $n = 0; $n < $total && count( $irmas ) < 4; $n++ ) {\n"
           "\t\tif ( $n === $eu ) {\n"
           "\t\t\tcontinue;\n"
           "\t\t}\n"
           "\t\t$irmas[] = $candidatas[ $n ];\n"
           "\t}")),

    # ------------------------------------------------------------------------
    # 4. A DATA DA CLASSIFICACAO DE SERP (13/09/2026, snippet 1.3.0)
    #
    # As tres primeiras atacam o caminho que NENHUMA pagina do banco de hoje usa
    # — as doze herdam o padrao —, e por isso as tres so sao mensuraveis no mundo
    # produzido dentro do proprio portao. Sem ele, as tres PASSARIAM: e a familia
    # de defeito que fica verde ate o dia em que importa, e o dia em que ela
    # importa e o da leva 4, que nasce classificada em outra data.
    ("a data propria e ignorada: a funcao devolve o padrao para todo mundo",
     troca(PEIXES,
           "\tif ( isset( $registro[ $slug ]['serp_em'] ) && '' !== $registro[ $slug ]['serp_em'] ) {\n"
           "\t\treturn $registro[ $slug ]['serp_em'];\n"
           "\t}\n",
           "\tif ( false ) {\n"
           "\t\treturn $registro[ $slug ]['serp_em'];\n"
           "\t}\n")),

    ("a pagina serve as DUAS datas: a propria e a do padrao, coladas",
     troca(PEIXES,
           "\t\treturn $registro[ $slug ]['serp_em'];",
           "\t\treturn $registro[ $slug ]['serp_em'] . ' (' . AQUAMETRIA_PEIXES_SERP_EM . ')';")),

    ("a data declarada por UMA pagina vaza para as vizinhas que nao declaram nada",
     troca(PEIXES,
           "\tif ( isset( $registro[ $slug ]['serp_em'] ) && '' !== $registro[ $slug ]['serp_em'] ) {\n"
           "\t\treturn $registro[ $slug ]['serp_em'];\n"
           "\t}\n"
           "\treturn AQUAMETRIA_PEIXES_SERP_EM;",
           "\tforeach ( $registro as $def ) {\n"
           "\t\tif ( isset( $def['serp_em'] ) && '' !== $def['serp_em'] ) {\n"
           "\t\t\treturn $def['serp_em'];\n"
           "\t\t}\n"
           "\t}\n"
           "\treturn AQUAMETRIA_PEIXES_SERP_EM;")),

    # E a quarta ataca o campo que a leva 4 precisa ter decidido antes de existir.
    ("a categoria com especies perde o criterio de quem entra nela",
     troca(PEIXES,
           "\t\t\t'criterio' => 'As espécies que a loja brasileira vende como tetra: os Paracheirodon, os Hemigrammus, os Hyphessobrycon e o Gymnocorymbus. A família não serve de critério aqui — a revisão recente dos caracídeos deixou o banco com tetra em duas famílias diferentes, e Characidae carrega peixe que ninguém vende como tetra.',",
           "\t\t\t'criterio' => '',")),

    # ------------------------------------------------------------------------
    # 5. A CATEGORIA PREPARADA (13/09/2026, snippet 1.5.0)
    #
    # Estas sete atacam a PRIMEIRA VIDA de uma categoria: declarada, com texto
    # escrito, e ainda sem URL. Nenhuma delas era mensuravel antes deste bloco —
    # a `bettas` passou 13/09 inteiro preparada e nada conferia a preparacao —,
    # e quatro delas PRODUZEM O MUNDO, porque o estado que elas quebram nao
    # existe no repositorio de hoje: nao ha categoria preparada com lista cheia,
    # nem familia preparada abaixo do minimo do 16.5.
    ("A PREPARACAO VIRA MEIA PREPARACAO: o criterio dos vivaparos fica e a linha mestra some",
     troca(PEIXES,
           "\t\t\t'linha_mestra' => 'Vivíparo não tem um número: destes três está declarado com quem cada um vive — mais fêmeas do que machos — e nunca quantos. O que decide o seu aquário é a frente, e entre dois peixes do mesmo gênero, vendidos na mesma prateleira, ela varia em duas vezes.',\n",
           "")),

    # MUNDO PRODUZIDO, e ele MUDOU DE ENDERECO em 14/09/2026. Ate a leva 5 esta
    # mutacao preenchia a lista da `vivaparos`, que era a categoria preparada e
    # sem URL do repositorio; com ela no ar, o alvo antigo virou MUTACAO INERTE —
    # o estado que ela quebrava deixou de existir. O que ela mede continua o
    # mesmo e continua valendo: categoria que declara especie e nao esta no
    # registro do eixo vira cartao com link para pagina que nao existe, que e a
    # pagina fina que o 16.5 existe para nao deixar entrar no indice. O alvo
    # passa a ser a `plecos-e-limpa-vidros`, que e uma das duas que hoje estao na
    # primeira vida, e o mundo e produzido inteiro: criterio, linha mestra e uma
    # especie do banco que a categoria sustenta.
    ("MUNDO PRODUZIDO: a categoria sem URL ganha criterio, linha mestra e uma especie",
     troca(PEIXES,
           "\t\t\t'singular' => 'todo pleco e todo limpa-vidros',\n\t\t\t'criterio' => '',\n\t\t\t'especies' => array(),",
           "\t\t\t'singular' => 'todo pleco e todo limpa-vidros',\n"
           "\t\t\t'linha_mestra' => 'Limpa-vidros não é faxineiro: o que decide o seu aquário é o chão que ele tem para raspar.',\n"
           "\t\t\t'criterio' => 'Os peixes de fundo que a loja brasileira vende como limpa-vidros.',\n"
           "\t\t\t'especies' => array(\n"
           "\t\t\t\t'otocinclus-vittatus',\n"
           "\t\t\t),")),

    ("O CRITERIO PARA DE NOMEAR A FAMILIA QUE ELE MESMO DECLARA COMO CRITERIO",
     troca(PEIXES,
           "Os vivíparos da família Poeciliidae que a loja brasileira vende",
           "Os vivíparos que a loja brasileira vende")),

    ("O CRITERIO PASSA A ESCREVER A CONTAGEM QUE ELE PROMETE ESTAR ABAIXO DA TABELA",
     troca(PEIXES,
           " Quantas estão dentro e quantas esperam está contado logo abaixo da tabela, nunca escrito aqui.',",
           " São 3 espécies nesta lista e 2 esperando.',")),

    ("A PROMESSA DO CRITERIO DEIXA DE SER CUMPRIVEL: o bloco de contagem sai da pagina de categoria",
     troca(PEIXES,
           "\t$html .= '<p class=\"aqm-px-fora\">';\n\tif ( $na_fila > 0 ) {\n\t\t$html .= 'Das '",
           "\t$html .= '<p class=\"aqm-px-nota\">';\n\tif ( $na_fila > 0 ) {\n\t\t$html .= 'Das '")),

    ("A CATEGORIA PREPARADA CAI ABAIXO DO MINIMO DO 16.5 E CONTINUA PREPARADA: o vivaparo novo perde a convivencia declarada",
     banco_json(lambda d: mut_campo(d, "xiphophorus-variatus", "convivencia", "cardume"))),

    ("A RAZAO QUE O CRITERIO PUBLICA MUDA NO BANCO E A FRASE FICA: a frente do espada vira 100 cm",
     banco_json(lambda d: mut_campo(d, "xiphophorus-hellerii", "comprimento_minimo_aquario_cm", 100))),

    # ------------------------------------------------------------------------
    # 6. OS BARRADOS (13/09/2026, snippet 1.6.0)
    #
    # A prestacao de contas da secao 7 do ARQUIPELAGO.md alcancou quem NAO esta
    # na tabela. Estas nove atacam as duas metades da coisa: o bloco gerado, que
    # pode envelhecer em relacao ao banco, e a tela, que pode calar, mentir a
    # contagem ou servir codigo de banco na cara do leitor.
    #
    # QUATRO DELAS PRODUZEM O MUNDO. Nenhuma das duas categorias no ar declara
    # especie barrada hoje, entao o ramo cheio da pagina de categoria nao existe
    # no repositorio — e regua sobre mundo que nunca aconteceu nasce errada sem
    # poder falhar (secao 8). Elas criam a declaracao e so depois quebram.
    ("O BLOCO DE AUSENTES SAI DA SECAO: a pagina volta a dizer 29 e a calar sobre os 37 do banco",
     troca(PEIXES,
           "\t$barrados = aquametria_peixes_barrados();\n\tif ( $barrados ) {\n\t\t$total =",
           "\t$barrados = aquametria_peixes_barrados();\n\tif ( false ) {\n\t\t$total =")),

    ("A CONTAGEM DO BANCO VIRA A DO CATALOGO: o total deixa de somar quem ficou de fora",
     troca(PEIXES,
           "\t\t$total = count( $catalogo ) + count( $barrados );",
           "\t\t$total = count( $catalogo );")),

    ("A TRADUCAO DA CAUSA MAIS COMUM SOME DO MAPA: tres ausentes perdem o motivo na tela",
     troca(PEIXES,
           "\t\t'duas fontes distintas'         => 'um segundo corpo de fonte (as duas referências do banco são do mesmo)',\n",
           "")),

    ("UM AUSENTE E APAGADO DO BLOCO GERADO: o snippet envelhece em relacao ao banco",
     troca(PEIXES, BARRADA_ANCISTRUS, "")),

    ("UMA ESPECIE DA TABELA ENTRA TAMBEM NA LISTA DOS AUSENTES: a pagina nega e afirma o mesmo fato",
     troca(PEIXES, BARRADA_ANCISTRUS, BARRADA_ANCISTRUS + BARRADA_ANCISTRUS.replace(
         "'ancistrus-cirrhosus'", "'paracheirodon-innesi'").replace(
         "'cientifico' => 'Ancistrus cirrhosus'", "'cientifico' => 'Paracheirodon innesi'"))),

    ("A ORDEM DOS AUSENTES VIRA A INVERSA: quem esta a quatro campos de distancia sobe para o topo",
     inverter_ordem_dos_barrados),

    # --- as quatro que produzem o mundo
    ("MUNDO PRODUZIDO: a categoria nascida passa a declarar uma barrada e a bancada nao percebe",
     troca(PEIXES,
           "\t\t\t\t'gymnocorymbus-ternetzi',\n\t\t\t),",
           "\t\t\t\t'gymnocorymbus-ternetzi',\n\t\t\t\t'danio-margaritatus',\n\t\t\t),")),

    ("MUNDO PRODUZIDO: a categoria declara a barrada, a bancada sabe, e a pagina cala sobre ela",
     varias(
         troca(PEIXES,
               "\t\t\t\t'gymnocorymbus-ternetzi',\n\t\t\t),",
               "\t\t\t\t'gymnocorymbus-ternetzi',\n\t\t\t\t'danio-margaritatus',\n\t\t\t),"),
         troca(TESTE,
               "        \"rotulo\": \"tetras\",\n        \"barradas\": [],",
               "        \"rotulo\": \"tetras\",\n        \"barradas\": [\"danio-margaritatus\"],"),
         troca(PEIXES,
               "\tif ( $barradas_daqui ) {\n\t\t$html .= '<p class=\"aqm-px-fora\">Fora da tabela",
               "\tif ( false ) {\n\t\t$html .= '<p class=\"aqm-px-fora\">Fora da tabela"),
     )),

    ("MUNDO PRODUZIDO: a lista com alguem esperando do lado de fora continua se dizendo fechada",
     varias(
         troca(PEIXES,
               "\t\t\t\t'gymnocorymbus-ternetzi',\n\t\t\t),",
               "\t\t\t\t'gymnocorymbus-ternetzi',\n\t\t\t\t'danio-margaritatus',\n\t\t\t),"),
         troca(TESTE,
               "        \"rotulo\": \"tetras\",\n        \"barradas\": [],",
               "        \"rotulo\": \"tetras\",\n        \"barradas\": [\"danio-margaritatus\"],"),
         troca(PEIXES, "\t} elseif ( $barradas_daqui ) {", "\t} elseif ( false ) {"),
     )),

    ("MUNDO PRODUZIDO: a categoria declara um id que o banco nao tem e a tabela encolhe em silencio",
     varias(
         troca(PEIXES,
               "\t\t\t\t'gymnocorymbus-ternetzi',\n\t\t\t),",
               "\t\t\t\t'gymnocorymbus-ternetzi',\n\t\t\t\t'hyphessobrycon-serpae',\n\t\t\t),"),
         troca(TESTE,
               "        \"rotulo\": \"tetras\",\n        \"barradas\": [],",
               "        \"rotulo\": \"tetras\",\n        \"barradas\": [\"hyphessobrycon-serpae\"],"),
     )),

    # ------------------------------------------------------------------
    # 4. O ARRANJO SOCIAL — a leva 4, 14/09/2026.
    #
    # Nenhuma destas PRODUZ o mundo, e e a primeira familia desta ilha em que
    # isso e verdade por um motivo bom: ate 13/09 as onze fichas no ar eram
    # todas `convivencia: cardume` e cada uma destas mutacoes teria passado
    # LIMPA, porque nao havia pagina que a palavra "cardume" pudesse traduzir
    # errado. O mundo chegou; o que estas medem e se a regua chegou junto.
    # ------------------------------------------------------------------

    ("O ARRANJO FIXO GANHA A ESCADA DE VOLTA: a ficha do betta volta a oferecer 20 bettas num aquario",
     troca(PEIXES,
           "\tif ( $arranjo && null !== $arranjo['fixo'] ) {\n\t\treturn array( $arranjo['fixo'] );\n\t}",
           "\tif ( false ) {\n\t\treturn array( $arranjo['fixo'] );\n\t}")),

    ("O NUMERO QUE A FONTE FIXA ESCORREGA: o casal da colisa vira um exemplar so",
     troca(PEIXES,
           "\t\t'casal' => array(\n\t\t\t'fixo'     => 2,",
           "\t\t'casal' => array(\n\t\t\t'fixo'     => 1,")),

    ("O SOLITARIO VIRA CASAL: a fonte diz um por aquario e a pagina oferece dois",
     troca(PEIXES,
           "\t\t'solitario' => array(\n\t\t\t'fixo'     => 1,",
           "\t\t'solitario' => array(\n\t\t\t'fixo'     => 2,")),

    ("O GRUPO VOLTA A SER CARDUME NA PRIMEIRA LINHA: o gurami mel, que a fonte declara NAO gregario, abre como peixe de cardume",
     troca(PEIXES,
           "\t\t\t'minimo'   => 'grupo mínimo',", "\t\t\t'minimo'   => 'cardume mínimo',")),

    ("A PALAVRA VAZA PELA LEGENDA: a tabela de lotacao do betta volta a se chamar 'um cardume de'",
     troca(PEIXES,
           "esc_html( $arranjo ? $arranjo['de'] : 'um cardume de' )",
           "esc_html( 'um cardume de' )")),

    ("O CONSELHO DO AGRESSIVO SE INVERTE: a ficha do betta volta a mandar diluir agressao em numero",
     troca(PEIXES,
           "\t\tif ( $arranjo && null !== $arranjo['fixo'] ) {\n\t\t\t$html .= '<p class=\"aqm-px-fora\">O que dá para dizer com o que está medido: a fonte declara '",
           "\t\tif ( false ) {\n\t\t\t$html .= '<p class=\"aqm-px-fora\">O que dá para dizer com o que está medido: a fonte declara '")),

    # LEVA 8, 22/09/2026 — A PORTA DOS FUNDOS DA REGUA QUE ESTA LEVA ESTREITOU.
    # `prosa_propria()` deixou de medir a palavra "cardume" dentro de link cuja
    # ancora e o TITULO de outra pagina do eixo, porque as tres ocorrencias no
    # corpo do oscar eram exatamente isso e a regua reprovava uma pagina certa.
    # Estreitar regua abre buraco, e o buraco tem nome: bastaria a pagina
    # escrever a propria prosa dentro de um <a> para escapar. Esta mutacao faz
    # isso — troca o titulo da mae por uma frase nossa dentro do mesmo link — e
    # a segunda metade da regua (`intrusas`) existe para pega-la.
    ("A PROSA SE ESCONDE DENTRO DO LINK: a frase de mae troca o titulo da categoria por texto proprio com a palavra cardume",
     troca(PEIXES,
           "\t\t\t. esc_html( $registro[ $pai ]['titulo'] ) . '</a>, onde a mesma conta aparece para todas elas na mesma tabela.</p>';",
           "\t\t\t. esc_html( 'o cardume desta categoria' ) . '</a>, onde a mesma conta aparece para todas elas na mesma tabela.</p>';")),

    ("A LINHA UNICA DO ARRANJO FIXO SE CHAMA MINIMA: o teto que a fonte declara vira piso na tela",
     troca(PEIXES,
           "\t$rotulo_minimo = ( $arranjo && '' !== $arranjo['minimo'] && $card ) ? $arranjo['minimo'] : '';",
           "\t$rotulo_minimo = 'cardume mínimo';")),

    ("A COLUNA DA CATEGORIA MISTA VOLTA A SER UM NUMERO: betta e colisa aparecem como 'nao declarado'",
     troca(PEIXES,
           "\t\t? ucfirst( reset( $arranjos )['minimo'] )\n\t\t: 'Como vive';",
           "\t\t? ucfirst( reset( $arranjos )['minimo'] )\n\t\t: 'Cardume mínimo';")),

    ("O SUBSTANTIVO DA LISTA FECHADA VOLTA A SER DIGITADO: a pagina de qualquer categoria diz 'todo tetra'",
     troca(PEIXES,
           "\t\t\t. esc_html( $cat['singular'] ) . ' que o banco desta ilha sustenta com duas fontes já tem a página dele. '",
           "\t\t\t. 'todo tetra que o banco desta ilha sustenta com duas fontes já tem a página dele. '")),

    ("O EXEMPLO DA PERGUNTA VOLTA A SER DIGITADO: a categoria das coridoras pergunta por dez neons",
     troca(PEIXES,
           "\t$html .= '<p>Quem pergunta \"' . esc_html( $registro[ $slug ]['consulta'] ) . '\" quer um número, e a resposta honesta tem duas partes. '",
           "\t$html .= '<p>Quem pergunta \"quantos litros para dez neons\" quer um número, e a resposta honesta tem duas partes. '")),

    ("A CELULA DO ARRANJO PERDE O NUMERO: 'sozinho, 1 por aquario' vira so 'sozinho'",
     troca(PEIXES,
           "\t\treturn $a['curto'] . ', ' . $a['fixo'] . ' por aquário';",
           "\t\treturn $a['curto'];")),

    ("O ARRANJO DE UMA ESPECIE E LIDO PELO DA VIZINHA: o mapa devolve sempre o primeiro",
     troca(PEIXES,
           "\t$chave = isset( $e['convivencia'] ) ? $e['convivencia'] : '';",
           "\t$chave = 'cardume';")),

    ("A NOTA DA SERP SOME DA FICHA DA COLISA: os quatro numeros medidos por fora da ilha deixam de sair",
     troca(PEIXES,
           "\tif ( ! empty( $registro[ $slug ]['serp_nota'] ) ) {",
           "\tif ( false ) {")),

    # --- o teto da faixa de grupo (esquema versao 4, 14/09/2026)

    ("O TETO DA FAIXA SOME DA ABERTURA: a ficha do gurami mel volta a publicar o piso sozinho",
     troca(PEIXES,
           "\t\t\t. ( ! empty( $e['cardume_ate'] ) ? ' a ' . esc_html( (int) $e['cardume_ate'] ) : '' ) . ' '",
           "\t\t\t. ' '")),

    ("O TETO VIRA ARITMETICA SOBRE O PISO: a pagina publica 4 a 8 porque dobrou o minimo",
     troca(PEIXES,
           "\t\t\t. ( ! empty( $e['cardume_ate'] ) ? ' a ' . esc_html( (int) $e['cardume_ate'] ) : '' ) . ' '",
           "\t\t\t. ' a ' . esc_html( (int) $card * 2 ) . ' '")),

    # MUNDO PRODUZIDO, e ele nasceu de uma mutacao que PASSOU em 14/09/2026.
    # A primeira escrita desta mutacao so tirava o teto da escada, e passou
    # limpa — porque o teto do gurami mel e 6, e o 6 ja esta na escada de
    # leitura (6, 8, 10, 12, 15, 20) por conta propria. A mutacao media a
    # coincidencia do banco de hoje, nao a regra. O comentario do proprio codigo
    # tinha previsto: "a escada de leitura so por ACASO carrega o segundo numero
    # de 4 a 6, e numa faixa 5 a 7 o 7 nao apareceria em linha nenhuma". Entao
    # esta mutacao PRODUZ a faixa impar nos dois lados — banco e catalogo — e so
    # depois tira o teto da escada.
    ("MUNDO PRODUZIDO: a faixa vira 4 a 7 e o teto sai da escada — a conta do outro extremo some",
     varias(
         banco_json(lambda d: mut_campo(d, "trichogaster-chuna", "cardume_recomendado_ate", 7)),
         troca(PEIXES, "\t\t\t'cardume_ate' => 6,", "\t\t\t'cardume_ate' => 7,"),
         troca(PEIXES,
               "\tif ( ! empty( $e['cardume_ate'] ) ) {\n\t\t$degraus[] = (int) $e['cardume_ate'];\n\t}",
               "\tif ( false ) {\n\t\t$degraus[] = (int) $e['cardume_ate'];\n\t}"),
     )),

    ("O ROTULO DA TABELA DE FONTES VOLTA A SER DIGITADO: o grupo do gurami mel e chamado de cardume",
     troca(PEIXES,
           "\t\t$rotulo_linha = ( $arranjo && '' !== $arranjo['minimo'] )\n\t\t\t? ucfirst( $arranjo['minimo'] )\n\t\t\t: 'Cardume mínimo';",
           "\t\t$rotulo_linha = 'Cardume mínimo';")),

    ("O VALOR DA TABELA DE FONTES PERDE A FAIXA: a linha diz 4 exemplares onde a fonte diz 4 a 6",
     troca(PEIXES,
           "\t\t$valor_linha = ! empty( $e['cardume_ate'] )\n\t\t\t? esc_html( $card ) . ' a ' . esc_html( (int) $e['cardume_ate'] ) . ' exemplares'\n\t\t\t: esc_html( $card ) . ' exemplares';",
           "\t\t$valor_linha = esc_html( $card ) . ' exemplares';")),

    ("O TETO SOME DA CELULA DA CATEGORIA: a tabela da bettas diz '4 ou mais' onde a fonte diz 4 a 6",
     troca(PEIXES,
           "\t\treturn ! empty( $e['cardume_ate'] )\n\t\t\t? $a['curto'] . ', ' . (int) $e['cardume'] . ' a ' . (int) $e['cardume_ate']\n\t\t\t: $a['curto'] . ', ' . (int) $e['cardume'] . ' ou mais';",
           "\t\treturn $a['curto'] . ', ' . (int) $e['cardume'] . ' ou mais';")),

    ("O BANCO PERDE O TETO DECLARADO e a pagina nao percebe que a faixa encolheu",
     banco_json(lambda d: mut_campo(d, "trichogaster-chuna", "cardume_recomendado_ate", None))),

    # --- a comparacao com a base, que a leva 4 escreveu ERRADA na primeira vez

    ("A COMPARACAO COM A BASE VOLTA A SER FRASE PRONTA: 'bem abaixo' em toda ficha de arranjo fixo",
     troca(PEIXES,
           "\t\t\t. ( '' !== $contra['frase'] ? ', e ' . esc_html( $contra['frase'] ) : '' )",
           "\t\t\t. ', e as duas ficam bem abaixo da base que a fonte declara'")),

    ("A COMPARACAO ERRA O LADO: o ramo do meio some e a faixa que cruza a base vira 'abaixo'",
     troca(PEIXES,
           "\t} elseif ( $l['classica'] >= $base ) {\n\t\t$frase = 'as duas ficam acima dos ';\n\t} else {\n\t\t$frase = 'uma delas fica abaixo e a outra acima dos ';\n\t}",
           "\t} else {\n\t\t$frase = 'as duas ficam abaixo dos ';\n\t}")),

    ("A COMPARACAO USA O EXTREMO ERRADO: o conservador sai da conta e so o classico decide",
     troca(PEIXES,
           "\tif ( $l['conservadora'] < $base ) {",
           "\tif ( $l['classica'] < $base ) {")),

    ("O FAQ VOLTA A REPETIR A PERGUNTA DO TITULO: duas Question de mesmo nome no mesmo FAQPage",
     troca(PEIXES,
           "\t\t\t\t'A regra de 1 cm de peixe por litro serve para o ' . $nome . '?',",
           "\t\t\t\t$def['titulo'],")),

    ("A TABELA INVERSA CALA SOBRE O LIMITE: a ficha do betta volta a dizer quantos 'cabem' e nada mais",
     troca(PEIXES,
           "\t\tif ( isset( $litros_alturas[ $meio_altura ] ) && $arranjo && null !== $arranjo['fixo'] ) {",
           "\t\tif ( false ) {")),

    # ---------------------------------------------------------------------
    # LEVA 5 (14/09/2026) — o mundo do HAREM, e as tres frases que erravam de
    # numero em paginas que ja estavam no ar.
    # ---------------------------------------------------------------------

    ("A ABERTURA PELO ARRANJO VOLTA A SER O RAMO DE RESGATE: abre pela traducao do como_vive()",
     troca(PEIXES,
           "\t\t$html .= 'Para ' . esc_html( $arranjo['de'] ) . ' ' . esc_html( $nome )\n"
           "\t\t\t. ' — ' . esc_html( $arranjo['abertura'] ) . ' —, o seu aquário precisa de '",
           "\t\t$html .= 'Para o ' . esc_html( $nome ) . ', que vive '\n"
           "\t\t\t. esc_html( aquametria_peixes_como_vive( $e ) ) . ', o seu aquário precisa de '")),

    # A GUARDA DA ABERTURA E O ROTULO, e nao a presenca do numero. Esta mutacao
    # PRODUZ o mundo que o esquema permite e o banco nunca teve: cardume_minimo
    # preenchido numa especie de casal. Com a guarda antiga (`$card` sozinho) a
    # pagina abriria "Para um  de 5 colisa-anao", com o rotulo vazio no meio.
    ("MUNDO PRODUZIDO: a especie de casal ganha cardume no banco e a guarda da abertura e testada",
     varias(
         banco_json(lambda d: mut_campo(d, "trichogaster-lalius", "cardume_minimo", 5)),
         troca(PEIXES,
               "\tif ( $card && '' !== $arranjo['minimo'] ) {",
               "\tif ( $card ) {"),
     )),

    ("O HAREM PERDE A ABERTURA PROPRIA e a frase sai com um travessao vazio no meio",
     troca(PEIXES,
           "\t\t\t'abertura' => 'e harém quer dizer mais fêmeas do que machos, nunca um casal',",
           "\t\t\t'abertura' => '',")),

    ("A ABERTURA DO HAREM TROCA DE ARRANJO: o harem passa a se anunciar como casal",
     troca(PEIXES,
           "\t\t\t'abertura' => 'e harém quer dizer mais fêmeas do que machos, nunca um casal',",
           "\t\t\t'abertura' => 'e são dois, não um macho sozinho',")),

    # MUNDO PRODUZIDO, e ele precisou de TRES metades. A primeira escrita desta
    # mutacao so tirava a guarda do portao, e PASSOU LIMPA: sem uma especie de
    # termo desconhecido no banco, a guarda nunca morde, e tirar codigo que o
    # mundo de hoje nao alcanca nao muda uma afirmacao. O mundo tem de ser
    # produzido — uma especie com `convivencia` fora dos cinco valores do esquema
    # e com cardume preenchido —, e so entao a guarda decide alguma coisa: com
    # ela, a ficha nao nasce; sem ela, a pagina abre com o rotulo do arranjo VAZIO
    # no meio da frase, chamando de nada um peixe que a fonte nao classificou.
    ("MUNDO PRODUZIDO: termo fora do vocabulario fechado, com a guarda do portao removida",
     varias(
         banco_json(lambda d: mut_campo(d, "gymnocorymbus-ternetzi", "convivencia", "bando")),
         troca(PEIXES,
               "\t\t\t'cardume' => 5,\n\t\t\t'cardume_ate' => null,\n"
               "\t\t\t'convivencia' => 'cardume',\n\t\t\t'comportamento' => 'pacifico',\n"
               "\t\t\t'frente_cm' => 75,",
               "\t\t\t'cardume' => 5,\n\t\t\t'cardume_ate' => null,\n"
               "\t\t\t'convivencia' => 'bando',\n\t\t\t'comportamento' => 'pacifico',\n"
               "\t\t\t'frente_cm' => 75,"),
         troca(PEIXES,
               "\tif ( null === aquametria_peixes_arranjo( $e ) ) {\n\t\treturn false;\n\t}\n",
               ""),
     )),

    ("A CONCORDANCIA DE NUMERO MORRE: a funcao devolve sempre o plural",
     troca(PEIXES,
           "\treturn ( 1 === (int) $n ) ? $singular : $plural;",
           "\treturn $plural;")),

    ("A DIFERENCA VOLTA A SAIR DAS CONSTANTES em vez dos dois numeros da tela",
     troca(PEIXES,
           "\t\t\t\t$vezes = $q['classica'] / $q['conservadora'];",
           "\t\t\t\t$vezes = AQUAMETRIA_PEIXES_LOTACAO_CONSERVADORA / AQUAMETRIA_PEIXES_LOTACAO_CLASSICA;")),

    # O MUNDO QUE O BANCO NAO TEM, PRODUZIDO — e as DUAS primeiras escritas destas
    # passaram limpas, pelo motivo que a secao 8 do contrato chama de "as duas
    # metades erram juntas": elas mudavam o porte no banco E no catalogo, e a
    # regua do teste recomputa o esperado A PARTIR do banco. Mundo novo em que as
    # duas metades concordam nao e mutacao, e COBERTURA — prova que o ramo roda,
    # nunca que existe trava. Para virar mutacao, o mundo produzido tem de vir
    # acompanhado de uma quebra.
    #
    # Nenhum peixe com ficha e grande o bastante para o criterio conservador nao
    # por nem UM no aquario minimo que a propria fonte declara: o maior e o
    # peixe-espada, com 16 cm, e ele chega a um. Com 40 cm de porte o conservador
    # zera na base de 120 x 30 cm, e e nesse mundo que as duas abaixo mordem.
    ("MUNDO PRODUZIDO: com o conservador em zero, a frase volta a dizer que ele poe um",
     varias(
         banco_json(lambda d: mut_campo(d, "xiphophorus-hellerii", "porte_adulto_cm", 40.0)),
         troca(PEIXES, "\t\t\t'porte_cm' => 16,", "\t\t\t'porte_cm' => 40,"),
         troca(PEIXES,
               "\t\t\t\t$html .= 'o critério apertado não põe nem um ' . esc_html( $nome )",
               "\t\t\t\t$html .= 'o critério apertado põe um ' . esc_html( $nome )"),
     )),

    ("MUNDO PRODUZIDO: com o conservador em zero, o numero do criterio folgado sai errado",
     varias(
         banco_json(lambda d: mut_campo(d, "xiphophorus-hellerii", "porte_adulto_cm", 40.0)),
         troca(PEIXES, "\t\t\t'porte_cm' => 16,", "\t\t\t'porte_cm' => 40,"),
         troca(PEIXES,
               "\t\t\t\t\t. ', e o folgado põe ' . esc_html( $q['classica'] )",
               "\t\t\t\t\t. ', e o folgado põe ' . esc_html( $q['meio'] )"),
     )),

]


def rodar(aplicar):
    base = tempfile.mkdtemp(prefix="mut-peixes-")
    copia = os.path.join(base, "ilha")
    shutil.copytree(RAIZ, copia)
    try:
        aplicar(copia)
        r = subprocess.run(
            [sys.executable, os.path.join(copia, "ferramentas", "teste-peixes.py"), copia],
            capture_output=True, text=True)
        return r.returncode, (r.stdout + r.stderr)
    finally:
        shutil.rmtree(base, ignore_errors=True)


print("MUTACOES CONTRA O PORTAO DO EIXO /peixes/ — %d deliberadas" % len(MUTACOES))
print("A copia limpa tem de PASSAR; toda mutacao tem de REPROVAR.\n")

codigo, saida = rodar(lambda base: None)
if codigo != 0:
    print("A COPIA LIMPA JA REPROVA — conserte o portao antes de mutar:")
    print(saida[-3000:])
    sys.exit(1)
print("copia limpa: passa (%s)\n" % re.search(r"\d+ afirmacoes", saida).group(0))

passaram = []
for i, (nome, aplicar) in enumerate(MUTACOES, 1):
    codigo, saida = rodar(aplicar)
    if codigo == 0:
        print("%2d. PASSOU (portao cego) — %s" % (i, nome))
        passaram.append(nome)
    else:
        motivo = [l.strip() for l in saida.splitlines() if l.strip().startswith("FALHOU:")]
        print("%2d. reprovou — %s" % (i, nome))
        for m in motivo[:2]:
            print("      %s" % m)

print("\n%d de %d reprovadas" % (len(MUTACOES) - len(passaram), len(MUTACOES)))
if passaram:
    print("\nMUTACOES QUE O PORTAO NAO VIU — cada uma e uma trava que falta:")
    for n in passaram:
        print("  - " + n)
    sys.exit(1)
