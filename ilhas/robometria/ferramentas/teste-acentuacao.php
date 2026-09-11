<?php
/**
 * A ilha nao serve portugues sem acento. Medido no CORPO, em todo estado de
 * pagina que ela consegue servir.
 *
 *   php ferramentas/teste-acentuacao.php .
 *
 * POR QUE ELE EXISTE
 * ------------------
 * O banco da Robometria nasceu em ASCII. Enquanto so alimentava medicao, nao
 * custava nada; com a R1 e a R2 no ar, o texto do banco e CITADO dentro da
 * resposta, e a mesma frase passou a sair metade certa e metade errada:
 *
 *   "... e a peça certa depende da sua: bateria — o fabricante vende a peca
 *    PR10127 identificada como 'Versao A'"
 *
 * "peça" foi escrita pela ilha; "peca" e "Versao" vieram do banco. Numa ilha
 * cuja secao 5 do ARQUIPELAGO.md diz que ser citada pela IA vale tanto quanto
 * ranquear, servir portugues errado justamente no trecho que prova a
 * procedencia custa a coisa que a ilha vende.
 *
 * A CORRECAO FOI FEITA UMA VEZ. ESTE ARQUIVO E O QUE IMPEDE A VOLTA.
 *
 * TRES CUIDADOS, E CADA UM E UMA CICATRIZ DO ARQUIPELAGO
 * -------------------------------------------------------
 * 1. QUEM CONFERE ESCREVE A PROPRIA REGUA. A lista abaixo e escrita AQUI, a
 *    mao, e nao importa a de `ferramentas/acentuar-banco.py`. Se as duas
 *    fossem a mesma, trocar uma entrada faria as duas metades errarem juntas
 *    e o teste passar — foi assim que a regua da elegibilidade da R2 morou
 *    no snippet e o teste a chamou para conferir o snippet.
 * 2. A AFIRMACAO SE MEDE NO CORPO. Nao no HTML completo: o `&#038;` ja foi
 *    contado na pagina inteira e a resposta do FAQPage ja foi achada dentro do
 *    proprio JSON-LD. Aqui o corpo vem de `varrer-corpo.php`, sem <script>,
 *    sem <style> e sem marcacao.
 * 3. A EXCECAO SE DECLARA NO MARKUP, e vem contada. O wordmark da ilha e
 *    "ROBO" + "METRIA" coladas, e ROBO ali e a assinatura, nao a palavra —
 *    acentua-lo destruiria a identidade. A pagina marca esse bloco com a
 *    classe `rbm-wordmark`, o teste o retira e EXIGE que cada bloco retirado
 *    seja exatamente a assinatura. Perdoar por vizinhanca ("tem 'METRIA' do
 *    lado, entao deve ser a marca") e adivinhar, e foi o que deixou passar
 *    "Peça mais vendido, últimas unidades!" no Clube do Mosaico.
 *
 * E A VARREDURA E DA ENTRADA INTEIRA. Renderizar so as nove paginas fixas mede
 * o caso-ancora da R1 e mais nada: "Aspirador Robo" e "Versao A" so aparecem
 * quando alguem escolhe um modelo da Multi. Sao 72 estados.
 */

$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';

$falhas = 0;
$medicoes = 0;

function rbm_ok( $condicao, $o_que, $medido = '' ) {
	global $falhas, $medicoes;
	$medicoes++;
	if ( $condicao ) {
		echo "  . $o_que" . ( '' !== $medido ? " ($medido)" : '' ) . "\n";
		return true;
	}
	$falhas++;
	echo "  x $o_que" . ( '' !== $medido ? " ($medido)" : '' ) . "\n";
	return false;
}

/* ---------------------------------------------------------------------------
 * A REGUA, escrita aqui. Forma ASCII => o que ela deveria ser em pt-BR.
 *
 * Ela cobre a palavra que, escrita assim, NAO existe em portugues ou muda de
 * sentido — nada de monossilabo ambiguo, porque reprovar "e" que deveria ser
 * "é" exigiria entender a frase, e teste que interpreta frase e opiniao.
 * ------------------------------------------------------------------------- */
$PROIBIDAS = array(
	'robo'           => 'robô',
	'robos'          => 'robôs',
	'versao'         => 'versão',
	'versoes'        => 'versões',
	'peca'           => 'peça',
	'pecas'          => 'peças',
	'succao'         => 'sucção',
	'sucao'          => 'sucção',
	'potencia'       => 'potência',
	'autonomia'      => null,   // acentuada nao existe; fica fora da regua
	'pagina'         => 'página',
	'paginas'        => 'páginas',
	'titulo'         => 'título',
	'usuario'        => 'usuário',
	'endereco'       => 'endereço',
	'especificacao'  => 'especificação',
	'especificacoes' => 'especificações',
	'instrucoes'     => 'instruções',
	'funcoes'        => 'funções',
	'automatica'     => 'automática',
	'compativel'     => 'compatível',
	'removivel'      => 'removível',
	'lavavel'        => 'lavável',
	'recarregavel'   => 'recarregável',
	'reservatorio'   => 'reservatório',
	'nivel'          => 'nível',
	'niveis'         => 'níveis',
	'maxima'         => 'máxima',
	'maximo'         => 'máximo',
	'minimo'         => 'mínimo',
	'medio'          => 'médio',
	'area'           => 'área',
	'areas'          => 'áreas',
	'agua'           => 'água',
	'litio'          => 'lítio',
	'obstaculos'     => 'obstáculos',
	'comodos'        => 'cômodos',
	'selecao'        => 'seleção',
	'propria'        => 'própria',
	'proprio'        => 'próprio',
	'lamina'         => 'lâmina',
	'dominio'        => 'domínio',
	'util'           => 'útil',
	'ultimas'        => 'últimas',
	'mao'            => 'mão',
);
unset( $PROIBIDAS['autonomia'] );

/* Palavra que e ASCII de proposito e nao pode ser confundida com as de cima:
   codigo, marca e endereco de pagina citado. Declarada aqui, nomeada uma a uma,
   nunca deduzida por formato. */
$EXCECOES_DE_PALAVRA = array(
	'robot',   // Xiaomi Robot Vacuum, WAP Robot — linha de produto, em ingles
	'robotic',
);

/* ---------------------------------------------------------------------------
 * O corpo de todo estado de pagina.
 * ------------------------------------------------------------------------- */
echo "Robometria — acentuacao do que a ilha SERVE\n\n";
echo "1. A varredura cobre a entrada inteira, nao uma amostra\n";

$saida = array();
$codigo = 0;
exec( 'php ' . escapeshellarg( __DIR__ . '/varrer-corpo.php' ) . ' ' . escapeshellarg( $raiz )
	. ' --com-excecao=rbm-wordmark 2>&1', $saida, $codigo );
rbm_ok( 0 === $codigo, 'a varredura de corpo roda sem erro', 'codigo ' . $codigo );

$estados = array();
$excecoes_por_estado = array();
$atual = null;
foreach ( $saida as $linha ) {
	if ( preg_match( '/^=== (.+) ===$/', $linha, $m ) ) {
		$atual = $m[1];
		$estados[ $atual ] = '';
		$excecoes_por_estado[ $atual ] = array();
		continue;
	}
	if ( preg_match( '/^--- excecao (\S+): (.*)$/', $linha, $m ) ) {
		$excecoes_por_estado[ $atual ][] = array( 'classe' => $m[1], 'texto' => $m[2] );
		continue;
	}
	if ( null !== $atual ) {
		$estados[ $atual ] .= $linha . ' ';
	}
}

rbm_ok( count( $estados ) >= 70, 'a varredura monta 70 estados ou mais', count( $estados ) . ' estados' );
$com_r1 = 0;
foreach ( array_keys( $estados ) as $rotulo ) {
	if ( 0 === strpos( $rotulo, 'r1:' ) ) { $com_r1++; }
}
rbm_ok( $com_r1 >= 28, 'a R1 e medida em pelo menos 28 estados — um por modelo do banco',
	$com_r1 . ' estados de R1' );
$bytes = array_sum( array_map( 'strlen', $estados ) );
rbm_ok( $bytes > 400000, 'o corpo somado tem tamanho de pagina inteira, nao de meia pagina',
	number_format( $bytes ) . ' bytes' );

/* ---------------------------------------------------------------------------
 * 2. A excecao declarada no markup: contada e conferida uma a uma.
 * ------------------------------------------------------------------------- */
echo "\n2. A excecao e declarada no markup, e vem contada (secao 8)\n";

$total_excecoes = 0;
$excecao_fora_do_esperado = array();
foreach ( $excecoes_por_estado as $rotulo => $blocos ) {
	foreach ( $blocos as $bloco ) {
		$total_excecoes++;
		/* O bloco marcado como wordmark tem que SER o wordmark. Se um dia
		   alguem marcar um paragrafo inteiro com esta classe para calar o
		   teste, esta linha reprova. */
		if ( 'ROBOMETRIA' !== preg_replace( '/\s+/u', '', $bloco['texto'] ) ) {
			$excecao_fora_do_esperado[] = $rotulo . ': ' . $bloco['texto'];
		}
	}
}
rbm_ok( $total_excecoes === count( $estados ),
	'existe exatamente um bloco de excecao por estado — o wordmark do cabecalho',
	$total_excecoes . ' blocos em ' . count( $estados ) . ' estados' );
rbm_ok( empty( $excecao_fora_do_esperado ),
	'todo bloco marcado como wordmark E a assinatura ROBOMETRIA, e nada mais',
	empty( $excecao_fora_do_esperado ) ? 'todos' : $excecao_fora_do_esperado[0] );

/* ---------------------------------------------------------------------------
 * 3. Nenhuma palavra da regua no corpo servido.
 * ------------------------------------------------------------------------- */
echo "\n3. Nenhuma palavra sem acento no corpo de nenhum estado\n";

$ocorrencias = array();
$alternativas = implode( '|', array_map( function ( $p ) { return preg_quote( $p, '#' ); },
	array_keys( $PROIBIDAS ) ) );
$padrao = '#(?<![0-9A-Za-zÀ-ÿ])(' . $alternativas . ')(?![0-9A-Za-zÀ-ÿ])#iu';

foreach ( $estados as $rotulo => $corpo ) {
	if ( preg_match_all( $padrao, $corpo, $m, PREG_OFFSET_CAPTURE ) ) {
		foreach ( $m[1] as $achado ) {
			$palavra = $achado[0];
			if ( in_array( mb_strtolower( $palavra, 'UTF-8' ), $EXCECOES_DE_PALAVRA, true ) ) {
				continue;
			}
			$trecho = trim( mb_substr( $corpo, max( 0, $achado[1] - 60 ), 130, 'UTF-8' ) );
			$ocorrencias[] = array( 'estado' => $rotulo, 'palavra' => $palavra, 'trecho' => $trecho );
		}
	}
}

$por_palavra = array();
foreach ( $ocorrencias as $o ) {
	$chave = mb_strtolower( $o['palavra'], 'UTF-8' );
	$por_palavra[ $chave ] = isset( $por_palavra[ $chave ] ) ? $por_palavra[ $chave ] + 1 : 1;
}
if ( ! rbm_ok( empty( $ocorrencias ),
	'zero palavra da regua no corpo servido, nos ' . count( $estados ) . ' estados',
	empty( $ocorrencias ) ? '0 ocorrencia' : count( $ocorrencias ) . ' ocorrencias' ) ) {
	foreach ( $por_palavra as $palavra => $n ) {
		echo "      '$palavra' x$n — deveria ser '" . $PROIBIDAS[ $palavra ] . "'\n";
	}
	foreach ( array_slice( $ocorrencias, 0, 6 ) as $o ) {
		echo "      [{$o['estado']}] ...{$o['trecho']}...\n";
	}
}

/* ---------------------------------------------------------------------------
 * 4. O livro-razao: a restauracao mexeu SO em acento, e isso se prova.
 * ------------------------------------------------------------------------- */
echo "\n4. O livro-razao da restauracao prova que nada de conteudo mudou\n";

$livro = json_decode( file_get_contents( $raiz . '/dados/acentuacao-restaurada.json' ), true );
rbm_ok( is_array( $livro ) && ! empty( $livro['mudancas'] ),
	'dados/acentuacao-restaurada.json existe e lista as mudancas',
	is_array( $livro ) ? count( $livro['mudancas'] ) . ' mudancas' : 'ausente' );

/**
 * Tira o diacritico e nada mais. Escrita aqui de proposito: se ela viesse do
 * mesmo lugar que a do corretor, as duas metades poderiam errar juntas.
 */
function rbm_sem_diacritico( $texto ) {
	$de = array(
		'á','à','â','ã','ä','é','è','ê','ë','í','ì','î','ï','ó','ò','ô','õ','ö','ú','ù','û','ü','ç','ñ',
		'Á','À','Â','Ã','Ä','É','È','Ê','Ë','Í','Ì','Î','Ï','Ó','Ò','Ô','Õ','Ö','Ú','Ù','Û','Ü','Ç','Ñ',
	);
	$para = array(
		'a','a','a','a','a','e','e','e','e','i','i','i','i','o','o','o','o','o','u','u','u','u','c','n',
		'A','A','A','A','A','E','E','E','E','I','I','I','I','O','O','O','O','O','U','U','U','U','C','N',
	);
	return str_replace( $de, $para, $texto );
}

$nao_sao_so_acento = array();
$nao_mudaram = array();
$ausentes_do_banco = array();

$bancos = array();
foreach ( array( 'pecas', 'modelos-robo', 'marcas' ) as $nome ) {
	$bancos[ 'dados/' . $nome . '.json' ] = file_get_contents( $raiz . '/dados/' . $nome . '.json' );
}

foreach ( (array) $livro['mudancas'] as $mudanca ) {
	if ( rbm_sem_diacritico( $mudanca['depois'] ) !== $mudanca['antes'] ) {
		$nao_sao_so_acento[] = $mudanca['caminho'];
	}
	if ( $mudanca['depois'] === $mudanca['antes'] ) {
		$nao_mudaram[] = $mudanca['caminho'];
	}
	/* E o "depois" tem que ser o que o banco tem HOJE. Livro-razao que nao
	   bate com o banco e historia, nao prova. */
	$agulha = json_encode( $mudanca['depois'], JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES );
	$agulha = substr( $agulha, 1, -1 );
	if ( isset( $bancos[ $mudanca['arquivo'] ] ) && false === strpos( $bancos[ $mudanca['arquivo'] ], $agulha ) ) {
		$ausentes_do_banco[] = $mudanca['caminho'];
	}
}

rbm_ok( empty( $nao_sao_so_acento ),
	'toda mudanca, reduzida a sem-diacritico, e IDENTICA ao que estava no banco antes',
	empty( $nao_sao_so_acento ) ? count( $livro['mudancas'] ) . ' conferidas' : $nao_sao_so_acento[0] );
rbm_ok( empty( $nao_mudaram ), 'nenhuma linha do livro-razao registra uma nao-mudanca',
	empty( $nao_mudaram ) ? 'nenhuma' : $nao_mudaram[0] );
rbm_ok( empty( $ausentes_do_banco ),
	'todo "depois" do livro-razao esta no banco commitado de hoje',
	empty( $ausentes_do_banco ) ? count( $livro['mudancas'] ) . ' encontradas' : $ausentes_do_banco[0] );
rbm_ok( ! empty( $livro['o_que_ele_nao_prova'] ),
	'o livro-razao diz o que NAO prova — que a fonte primaria escreve assim' );

/* ---------------------------------------------------------------------------
 * 5. A escada de fontes nao se contradiz: a coluna e contada, nao digitada.
 * ------------------------------------------------------------------------- */
echo "\n5. A coluna 'Temos hoje' da escada e contada no banco (regra do elo mais fraco)\n";

$fatos = json_decode( file_get_contents( $raiz . '/dados/casca-fatos.json' ), true );
$esquema = json_decode( file_get_contents( $raiz . '/dados/esquema-banco.json' ), true );

/* A contagem e refeita AQUI, do banco cru, sem olhar para o que o gerador
   escreveu. Duas contas independentes que batem sao medicao; uma conta sozinha
   e o que o autor achou. */
$conta = array_fill( 1, 7, 0 );
foreach ( array( 'pecas', 'modelos-robo' ) as $nome ) {
	$banco = json_decode( file_get_contents( $raiz . '/dados/' . $nome . '.json' ), true );
	foreach ( $banco['registros'] as $registro ) {
		if ( ! isset( $registro['status'] ) || 'publicavel' !== $registro['status'] ) { continue; }
		foreach ( (array) ( isset( $registro['fontes'] ) ? $registro['fontes'] : array() ) as $fonte ) {
			if ( isset( $fonte['nivel'] ) && isset( $conta[ (int) $fonte['nivel'] ] ) ) {
				$conta[ (int) $fonte['nivel'] ]++;
			}
		}
	}
}
$ponte = $esquema['escada_de_fontes']['onde_moram_as_fontes']['tipo_de_constante_para_nivel'];
$constantes = json_decode( file_get_contents( $raiz . '/dados/constantes.json' ), true );
foreach ( $constantes['constantes'] as $constante ) {
	if ( 'publicavel' !== $constante['status'] ) { continue; }
	$nivel = isset( $ponte[ $constante['tipo'] ] ) ? $ponte[ $constante['tipo'] ] : null;
	if ( null !== $nivel ) { $conta[ (int) $nivel ]++; }
}

$bate = true;
$divergente = '';
foreach ( $fatos['niveis'] as $degrau ) {
	if ( (int) $degrau['fontes_no_banco'] !== $conta[ (int) $degrau['nivel'] ] ) {
		$bate = false;
		$divergente = 'nivel ' . $degrau['nivel'] . ': fatos dizem ' . $degrau['fontes_no_banco']
			. ', o banco tem ' . $conta[ (int) $degrau['nivel'] ];
	}
}
rbm_ok( $bate, 'a contagem publicada bate com a recontagem independente do banco',
	$bate ? implode( '/', array_values( $conta ) ) : $divergente );

$niveis_altos_ocupados = array();
foreach ( array( 'pecas', 'modelos-robo' ) as $nome ) {
	$banco = json_decode( file_get_contents( $raiz . '/dados/' . $nome . '.json' ), true );
	foreach ( $banco['registros'] as $registro ) {
		foreach ( (array) ( isset( $registro['fontes'] ) ? $registro['fontes'] : array() ) as $fid => $fonte ) {
			if ( isset( $fonte['nivel'] ) && (int) $fonte['nivel'] <= 2
				&& ( ! isset( $fonte['leitura'] ) || 'direta-na-fonte-primaria' !== $fonte['leitura'] ) ) {
				$niveis_altos_ocupados[] = $registro['id'] . '/' . $fid;
			}
		}
	}
}
rbm_ok( empty( $niveis_altos_ocupados ),
	'nenhuma fonte ocupa nivel 1 ou 2 sem DECLARAR leitura na fonte primaria',
	empty( $niveis_altos_ocupados ) ? 'nenhuma' : $niveis_altos_ocupados[0] );

/* A tela nao pode dizer que a ilha tem um degrau que o banco nao sustenta. */
$corpo_metodologia = isset( $estados['pagina:metodologia'] ) ? $estados['pagina:metodologia'] : '';
rbm_ok( '' !== $corpo_metodologia, 'a pagina de metodologia foi medida' );
$diz_que_nao_tem_2 = ( false !== mb_strpos( $corpo_metodologia, 'nem de nível 2' ) );
$tem_2_no_banco = $conta[2] > 0;
rbm_ok( $diz_que_nao_tem_2 !== $tem_2_no_banco,
	'a confissao da pagina sobre o nivel 2 concorda com o banco',
	'pagina diz que nao tem: ' . ( $diz_que_nao_tem_2 ? 'sim' : 'nao' )
		. ' | banco tem: ' . $conta[2] );

/* ---------------------------------------------------------------------------
 * Fecho.
 * ------------------------------------------------------------------------- */
echo "\n";
if ( $falhas ) {
	echo "REPROVADO: $falhas de $medicoes medicoes falharam.\n";
	exit( 1 );
}
echo "APROVADO: $medicoes medicoes, zero falhas.\n";
exit( 0 );
