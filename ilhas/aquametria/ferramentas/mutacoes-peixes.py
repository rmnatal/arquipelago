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
     troca(PEIXES, "\t\t\t'porque'   => 'Medido em 12/09/2026: o top 7", "\t\t\t'x_porque' => 'Medido em 12/09/2026: o top 7")),

    # ------------------------------------- 3. a regua perde o chao
    ("A COLISAO DE SLUG VOLTA: a categoria do C8 se chama 'peixes' outra vez",
     troca(CASCA, "\t\t'lotacao'           => 'Lotação',", "\t\t'peixes'            => 'Lotação',")),

    ("o catalogo do snippet envelhece: o porte do neon muda no banco e ninguem roda o gerador",
     troca(BANCO, '"porte_adulto_cm": 2.2,', '"porte_adulto_cm": 2.4,')),
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
