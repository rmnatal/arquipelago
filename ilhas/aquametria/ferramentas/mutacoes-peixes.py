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


MUTACOES = [
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

    ("BASE VIRA FRENTE: a ficha sem fundo declarado volta a dizer que a fonte declara a BASE",
     troca(PEIXES,
           "\t\t$html .= ' — e a fonte declara o COMPRIMENTO do aquário, não o litro.</p>';",
           "\t\t$html .= ' — e a fonte declara a BASE, não o litro.</p>';")),

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
    ("O BANCO PERDE O CARDUME DE QUEM JA TEM FICHA NO AR: a sterbai volta a 'grupo' sem numero",
     lambda base: (
         troca(BANCO,
               '"cardume_minimo": 6,\n   "comprimento_minimo_aquario_cm": 45,\n'
               '   "base_minima_cm": {\n    "comprimento": 45,\n    "largura": 30\n   },\n'
               '   "altura_minima_cm": null,\n   "volume_minimo_declarado_L": null,\n'
               '   "nivel_natacao": "fundo",\n   "comportamento": null,\n'
               '   "convivencia": "cardume",',
               '"cardume_minimo": null,\n   "comprimento_minimo_aquario_cm": 45,\n'
               '   "base_minima_cm": {\n    "comprimento": 45,\n    "largura": 30\n   },\n'
               '   "altura_minima_cm": null,\n   "volume_minimo_declarado_L": null,\n'
               '   "nivel_natacao": "fundo",\n   "comportamento": null,\n'
               '   "convivencia": "grupo",')(base),
     )),

    ("O CATALOGO DO SNIPPET PERDE O CARDUME: a ficha da sterbai abre a tabela em UM exemplar",
     troca(PEIXES,
           # O PORTE ENTRA NA ANCORA e nao e decoracao: sem ele a string casa
           # tambem com a coridora panda, que tem o MESMO cardume (6), a MESMA
           # frente (45) e a mesma convivencia. A trava anti-inercia recusou na
           # primeira escrita desta mutacao, e estava certa — mutar as duas de
           # uma vez mediria outra coisa com o mesmo placar verde.
           "\t\t\t'porte_cm' => 6.8,\n\t\t\t'porte_medida' => 'SL',\n\t\t\t'cardume' => 6,\n\t\t\t'convivencia' => 'cardume',\n\t\t\t'comportamento' => '',\n\t\t\t'frente_cm' => 45,",
           "\t\t\t'porte_cm' => 6.8,\n\t\t\t'porte_medida' => 'SL',\n\t\t\t'cardume' => null,\n"
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
