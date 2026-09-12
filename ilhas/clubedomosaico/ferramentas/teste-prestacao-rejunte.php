<?php
/**
 * PRESTACAO DE CONTAS DO REJUNTE — o portao do despacho da Sentinela de
 * 12/09/2026, nas duas ferramentas.
 *
 *   php ferramentas/teste-prestacao-rejunte.php .
 *
 * O QUE ELE COBRA, e que e a regra nova da ilha:
 *
 *   TODO rejunte do banco e nomeado EXATAMENTE UMA VEZ em cada resposta — ou
 *   na frase de recomendacao (e ai ele esta no bloco de compra), ou numa linha
 *   que diz por que ele nao esta. E a lista de compra serve EXATAMENTE o que a
 *   frase nomeia: nao existe produto empurrado que o texto nao sustente.
 *
 *   Na F1, que filtra por TIPO, a mesma conta vale dentro do tipo escolhido — e
 *   a acusacao tem de bater com a causa: quem cai pelo LUGAR nunca e reportado
 *   como se a folga nao coubesse.
 *
 * OS DOIS DEFEITOS QUE ELE EXISTE PARA IMPEDIR DE VOLTAR (medidos no ar pela
 * Sentinela em 12/09/2026, e reproduzidos nesta bancada antes do conserto):
 *
 *   (1) F1: com o lugar excluindo, a pagina escrevia "Nenhum rejunte do nosso
 *       banco declara folga de N mm" — falso, a folga cabia — e, no pior caso,
 *       negava e afirmava o mesmo fato em duas frases seguidas, porque a linha
 *       de "outro tipo" vinha logo depois dizendo "dentro dessa folga".
 *   (2) F2: a frase dizia "o rejunte e X", singular e definitiva, e a vitrine
 *       servia QUATRO. Dos 5 rejuntes do banco, 3 ficavam no bloco de compra
 *       sem que a pagina dissesse o que eles sao, e um quinto estado
 *       (mencionados_com_ressalva) nao era impresso em lugar nenhum.
 *
 * AS TRES CICATRIZES DA SECAO 8 DO `ARQUIPELAGO.md` QUE ESTE ARQUIVO HERDA:
 *
 *   1. REGUA PROPRIA. A classificacao esperada e recomputada AQUI, a partir de
 *      `perfis_esperados_do_rejunte` do `esquema-banco.json` — que foi escrito
 *      A MAO a partir das declaracoes dos fabricantes — e das regras 1 a 4 do
 *      mesmo esquema, reimplementadas neste arquivo. Nada aqui chama
 *      `cdm_f2_celula_rejunte()`, `cdm_f2_avaliar_rejunte()` nem
 *      `cdm_f2_perfil_rejunte()`: se a regua morasse no snippet, trocar um `>`
 *      por `>=` faria as duas metades errarem juntas.
 *   2. A ENTRADA INTEIRA, com as bordas. F2: 9 bases x 5 lugares x 12 folgas =
 *      540 estados. F1: 3 tipos x 5 lugares x 12 folgas = 180. As folgas vao de
 *      1 a 12 de propostio: 1 e 11 sao os dois primeiros valores fora dos
 *      extremos que algum fabricante declara, e 2, 4, 5 e 10 sao extremos
 *      exatos. Amostra com nome de varredura foi o que deixou cinco testes
 *      verdes na Robometria.
 *   3. UM PROCESSO POR ESTADO e MEDICAO NO CORPO. A afirmacao e sobre o que a
 *      pagina DIZ, entao ela se conta dentro do bloco do rejunte — nunca no
 *      HTML completo, onde o JSON-LD e a tabela pre-renderizada contem os
 *      mesmos nomes e fariam qualquer contagem passar.
 */

$raiz   = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';
$rapido = in_array( '--rapido', $argv, true );

$falhas = 0;
$feitos = 0;

function pr_ok( $condicao, $rotulo, $medida = '' ) {
	global $falhas, $feitos;
	$feitos++;
	if ( $condicao ) {
		if ( ! getenv( 'PR_SILENCIO' ) ) {
			printf( "  ok   %-72s %s\n", $rotulo, $medida );
		}
		return true;
	}
	$falhas++;
	printf( "  FALHA %-72s %s\n", $rotulo, $medida );
	return false;
}

function pr_texto( $html ) {
	return trim( preg_replace( '/\s+/u', ' ', html_entity_decode( strip_tags( $html ), ENT_QUOTES, 'UTF-8' ) ) );
}

function pr_corpo( $html ) {
	return preg_match( '#<main[^>]*>(.*?)</main>#is', $html, $m ) ? $m[1] : '';
}

function pr_render( $raiz, $alvo, $consulta ) {
	$saida  = array();
	$codigo = 0;
	exec( escapeshellcmd( PHP_BINARY ) . ' ' . escapeshellarg( __DIR__ . '/render-para-teste.php' )
		. ' ' . escapeshellarg( $raiz ) . ' ' . escapeshellarg( $alvo ) . ' ' . escapeshellarg( 'hoje' )
		. ' ' . escapeshellarg( $consulta ) . ' 2>/dev/null', $saida, $codigo );

	return 0 === $codigo ? implode( "\n", $saida ) : '';
}

/** O bloco do rejunte da F2: do h2 dele ate a proxima secao. */
function pr_bloco_f2( $corpo ) {
	return preg_match( '#<h2>E o rejunte, que vai entre os caquinhos</h2>(.*?)(?=<div class="cdm-f2-secao[ "]|$)#is', $corpo, $m )
		? $m[1] : '';
}

/** O bloco do rejunte da F1: do h2 dele ate o aviso de afiliado. */
function pr_bloco_f1( $corpo ) {
	return preg_match( '#<h2>Qual rejunte cabe nessa folga</h2>(.*?)(?=<p class="cdm-f1-aviso"|$)#is', $corpo, $m )
		? $m[1] : '';
}

/* ---------------------------------------------------------------------------
 * A REGUA PROPRIA — as regras 1 a 4 do esquema, reescritas aqui.
 * ------------------------------------------------------------------------- */

$esquema  = json_decode( (string) @file_get_contents( $raiz . '/dados/esquema-banco.json' ), true );
$rejuntes = json_decode( (string) @file_get_contents( $raiz . '/dados/materiais-rejuntes.json' ), true );

if ( ! $esquema || ! $rejuntes ) {
	fwrite( STDERR, "Nao consegui ler o esquema ou o banco de rejuntes.\n" );
	exit( 2 );
}

/* Nome comercial e tipo, do banco. O nome e o que a tela imprime; conferir por
   id nao mediria o que a pessoa le. */
$nome_de = array();
$tipo_de = array();
foreach ( $rejuntes['materiais'] as $m ) {
	$nome_de[ $m['id'] ] = $m['nome_comercial'];
	$tipo_de[ $m['id'] ] = isset( $m['tipo'] ) ? $m['tipo'] : '';
}

/* Os perfis ESCRITOS A MAO. Se um dia o banco ganhar um rejunte e ninguem
   escrever o perfil dele aqui, o teste acusa — as duas direcoes. */
$perfis = array();
foreach ( $esquema['perfis_esperados_do_rejunte']['perfis'] as $p ) {
	$perfis[ $p['id'] ] = $p;
}
$ids_banco = array_keys( $nome_de );
sort( $ids_banco );
$ids_perfil = array_keys( $perfis );
sort( $ids_perfil );

echo "REGUA PROPRIA — o banco e os perfis escritos a mao\n";
pr_ok( $ids_banco === $ids_perfil, 'todo rejunte do banco tem perfil escrito a mao, e vice-versa',
	count( $ids_banco ) . ' no banco, ' . count( $ids_perfil ) . ' perfis' );

$criticos = $esquema['regras_de_elegibilidade_do_rejunte']['2_ambiente_critico_exige_declaracao_EXPLICITA']['ambientes'];
$ambientes = array( 'interno_seco', 'interno_molhado', 'externo_abrigado', 'externo_exposto', 'contato_permanente_agua' );
$juntas    = range( 1, 12 );
$bases     = array( 'ceramica_esmaltada_porcelana', 'vidro', 'vidro_laminado', 'espelho', 'mdf_madeira',
	'cimento_concreto', 'alvenaria_tijolo', 'metal', 'plastico' );
$tipos     = array( 'cimenticio', 'acrilico', 'epoxi' );

/**
 * A classificacao esperada de UM rejunte, pelas regras 1 a 4 — reimplementadas.
 * Devolve: topo | abaixo | ressalva | fora_folga | sem_faixa | fora_lugar.
 */
function pr_classificar( $perfil, $junta, $ambiente, $criticos ) {
	$min = $perfil['junta_mm'][0];
	$max = $perfil['junta_mm'][1];

	/* Regra 1 — a junta manda, e precisa das DUAS pontas. */
	if ( null === $min || null === $max ) {
		return 'sem_faixa';
	}
	if ( $junta < $min || $junta > $max ) {
		return 'fora_folga';
	}
	/* Regra 3 — quem delimita ambiente fica fechado nele. */
	if ( $perfil['ambientes_delimitados'] && ! in_array( $ambiente, $perfil['ambientes_delimitados'], true ) ) {
		return 'fora_lugar';
	}
	/* Regra 2 — ambiente critico exige declaracao explicita. */
	if ( in_array( $ambiente, $criticos, true ) && ! in_array( $ambiente, $perfil['ambientes_cobertos'], true ) ) {
		return 'fora_lugar';
	}
	/* Regra 4 — nivel de fonte limita a recomendacao primaria. */
	if ( $perfil['nivel'] > 3 ) {
		return 'ressalva';
	}

	return in_array( $ambiente, $perfil['ambientes_cobertos'], true ) ? 'topo' : 'abaixo';
}

/** A grade inteira de uma celula, pela regua deste arquivo. */
function pr_celula( $perfis, $junta, $ambiente, $criticos ) {
	$out = array( 'topo' => array(), 'abaixo' => array(), 'ressalva' => array(),
		'fora_folga' => array(), 'sem_faixa' => array(), 'fora_lugar' => array() );
	foreach ( $perfis as $id => $p ) {
		$out[ pr_classificar( $p, $junta, $ambiente, $criticos ) ][] = $id;
	}
	/* Sem candidato de topo, NINGUEM e topo: a pagina nao promove o segundo a
	   primeiro, ela diz que nao tem indicacao. E o que o snippet faz (o topo sai
	   do maior score entre os recomendados), e a regua repete a regra em vez de
	   confiar nela. */
	if ( ! $out['topo'] && $out['abaixo'] ) {
		$out['topo']  = $out['abaixo'];
		$out['abaixo'] = array();
	}
	foreach ( $out as $k => $v ) {
		sort( $out[ $k ] );
	}

	return $out;
}

/* Quantas vezes o NOME aparece no bloco. Nome de produto e substring de outro
   ("Rejunte Ceramicas Quartzolit" dentro de "Rejunte Porcelanatos e Ceramicas
   Quartzolit"), entao a contagem desconta as ocorrencias que sao parte do nome
   maior — senao a prestacao de contas fecharia por engano. */
function pr_conta_nome( $texto, $nome, $todos_os_nomes ) {
	$bruto = substr_count( $texto, $nome );
	foreach ( $todos_os_nomes as $outro ) {
		if ( $outro !== $nome && false !== strpos( $outro, $nome ) ) {
			$bruto -= substr_count( $texto, $outro );
		}
	}

	return max( 0, $bruto );
}

echo "\nF2 — a resposta do rejunte, 9 bases x 5 lugares x 12 folgas\n";

$todos_nomes = array_values( $nome_de );
$f2_estados  = 0;
$f2_erros    = array();

foreach ( $bases as $base ) {
	foreach ( $ambientes as $amb ) {
		foreach ( $juntas as $j ) {
			if ( $rapido && ( 'ceramica_esmaltada_porcelana' !== $base ) ) {
				continue;
			}
			$f2_estados++;
			$consulta = 'base=' . $base . '&caco=pastilha_ceramica&onde=' . $amb . '&junta=' . $j;
			$bloco    = pr_bloco_f2( pr_corpo( pr_render( $raiz, 'cdm_f2', $consulta ) ) );
			$onde     = $base . ' / ' . $amb . ' / ' . $j . ' mm';

			if ( '' === $bloco ) {
				$f2_erros[] = "$onde: o bloco do rejunte nao foi servido";
				continue;
			}

			$esperado = pr_celula( $perfis, $j, $amb, $criticos );
			$texto    = pr_texto( $bloco );

			/* (a) TODO rejunte do banco e nomeado UMA VEZ NA PROSA. A prosa e o
			   bloco menos os cartoes: o cartao e a vitrine, e repetir o nome
			   nele e a funcao dele. A prestacao de contas e o texto — e e nele
			   que um produto sumia sem explicacao. */
			$prosa = pr_texto( preg_replace( '#<li\b.*?</li>#is', ' ', $bloco ) );
			foreach ( $nome_de as $id => $nome ) {
				$vezes = pr_conta_nome( $prosa, $nome, $todos_nomes );
				if ( 1 !== $vezes ) {
					$f2_erros[] = "$onde: \"$nome\" aparece $vezes vez(es) na prosa do bloco, e tem de aparecer 1";
				}
			}

			/* (b) A VITRINE SERVE EXATAMENTE O QUE A FRASE NOMEIA. A frase sao os
			   dois paragrafos de classe cdm-f2-frase; os cartoes sao os <li>. */
			preg_match_all( '#<p class="cdm-f2-frase[^"]*">(.*?)</p>#is', $bloco, $mf );
			$frase = pr_texto( implode( ' ', $mf[1] ) );
			preg_match_all( '#<li[^>]*class="cdm-f2-cartao[^"]*"[^>]*>(.*?)</li>#is', $bloco, $mc );
			if ( ! $mc[1] ) {
				preg_match_all( '#<li\b(.*?)</li>#is', $bloco, $mc );
			}
			$na_vitrine = array();
			foreach ( $mc[1] as $cartao ) {
				$t = pr_texto( $cartao );
				foreach ( $nome_de as $id => $nome ) {
					if ( pr_conta_nome( $t, $nome, $todos_nomes ) > 0 ) {
						$na_vitrine[ $id ] = true;
					}
				}
			}
			$na_frase = array();
			foreach ( $nome_de as $id => $nome ) {
				if ( pr_conta_nome( $frase, $nome, $todos_nomes ) > 0 ) {
					$na_frase[ $id ] = true;
				}
			}
			$vit = array_keys( $na_vitrine );
			$fr  = array_keys( $na_frase );
			sort( $vit );
			sort( $fr );
			if ( $vit !== $fr ) {
				$f2_erros[] = "$onde: a vitrine serve [" . implode( ', ', $vit ) . '] e a frase nomeia [' . implode( ', ', $fr ) . ']';
			}

			/* (c) E quem a frase nomeia e exatamente quem a regua propria aprova. */
			$aprovados = array_merge( $esperado['topo'], $esperado['abaixo'] );
			sort( $aprovados );
			if ( $fr !== $aprovados ) {
				$f2_erros[] = "$onde: a frase nomeia [" . implode( ', ', $fr ) . '] e a regua aprova [' . implode( ', ', $aprovados ) . ']';
			}

			/* (d) CADA CAUSA TEM SUA LINHA, e ela nomeia exatamente quem a regua
			   propria poe nela. E aqui que a regua e carga: se ela deixar de
			   valer, a promocao de um elegivel a recomendado primario passa sem
			   ser vista, e a lista de "fora" pode nomear quem nao caiu por
			   aquele motivo. */
			$linhas_esperadas = array(
				'Fora por causa da folga'                  => $esperado['fora_folga'],
				'Fora porque o fabricante não declara este lugar' => $esperado['fora_lugar'],
				'a gente não conseguiu a faixa de junta'   => $esperado['sem_faixa'],
				'Existe menção a'                          => $esperado['ressalva'],
			);
			foreach ( $linhas_esperadas as $marca => $ids ) {
				$tem_linha = ( false !== mb_strpos( $texto, $marca ) );
				if ( $ids && ! $tem_linha ) {
					$f2_erros[] = "$onde: falta a linha \"$marca\" para [" . implode( ', ', $ids ) . ']';
				}
				if ( ! $ids && $tem_linha ) {
					$f2_erros[] = "$onde: a linha \"$marca\" saiu sem ninguem para nomear";
				}
			}

			/* (e) A PROMOCAO SILENCIOSA. Quem a pagina apresenta como a
			   recomendacao primaria e exatamente o topo da regua — nunca um
			   elegivel de segunda promovido. A frase do topo e a primeira; a dos
			   segundos comeca por "Também servem". */
			if ( preg_match( '#<p class="cdm-f2-frase">(.*?)</p>#is', $bloco, $mp ) ) {
				$primeira = pr_texto( $mp[1] );
				$no_topo  = array();
				foreach ( $nome_de as $id => $nome ) {
					if ( pr_conta_nome( $primeira, $nome, $todos_nomes ) > 0 ) {
						$no_topo[] = $id;
					}
				}
				sort( $no_topo );
				if ( $no_topo !== $esperado['topo'] ) {
					$f2_erros[] = "$onde: a frase principal apresenta [" . implode( ', ', $no_topo )
						. '] e o topo da regua e [' . implode( ', ', $esperado['topo'] ) . ']';
				}
			}
		}
	}
}

pr_ok( ! $f2_erros, 'F2: prestacao de contas fecha em todos os estados varridos',
	$f2_estados . ' estados, ' . count( $f2_erros ) . ' erro(s)' );
foreach ( array_slice( $f2_erros, 0, 12 ) as $e ) {
	echo "       -> $e\n";
}

/* ---------------------------------------------------------------------------
 * A TABELA PRE-RENDERIZADA — a metade que um modelo de linguagem le sem
 * preencher formulario nenhum, e onde o defeito e mais caro. Ela foi esquecida
 * na primeira versao deste portao, e uma mutacao deliberada passou por causa
 * disso: bastava a tabela parar de contar um dos grupos de "fora" para tres das
 * nove linhas deixarem de somar o banco, com a resposta com parametro
 * perfeitamente honesta. Duas telas do mesmo fato precisam das duas travas.
 * ------------------------------------------------------------------------- */
echo "\nA tabela pre-renderizada do rejunte — a soma de cada linha\n";

$tab_erros = array();
$corpo_f2  = pr_corpo( pr_render( $raiz, 'cdm_f2', '' ) );
$grade     = $esquema['matriz_esperada_do_rejunte']['celulas'];

if ( ! preg_match( '#<h2>O mesmo, para o rejunte</h2>(.*?)</table>#is', $corpo_f2, $mt ) ) {
	$tab_erros[] = 'a tabela do rejunte nao foi servida no HTML';
} else {
	preg_match_all( '#<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*</tr>#is', $mt[1], $linhas, PREG_SET_ORDER );
	pr_ok( count( $linhas ) === count( $grade ), 'a tabela serve uma linha por celula da grade escrita a mao',
		count( $linhas ) . ' linhas para ' . count( $grade ) . ' celulas' );

	foreach ( $linhas as $i => $l ) {
		$folga_txt = pr_texto( $l[1] );
		$rotulo    = "linha $i ($folga_txt)";

		/* Quem SERVE, contado pelos nomes que a celula nomeia. */
		$servem = 0;
		foreach ( $nome_de as $id => $nome ) {
			$servem += pr_conta_nome( pr_texto( $l[3] ), $nome, $todos_nomes );
		}
		/* Quem esta FORA, somando os numeros que a coluna declara. */
		$fora = 0;
		if ( preg_match_all( '/(\d+)\s+(?:por|porque)/u', pr_texto( $l[4] ), $mn ) ) {
			foreach ( $mn[1] as $n ) {
				$fora += (int) $n;
			}
		}
		if ( $servem + $fora !== count( $nome_de ) ) {
			$tab_erros[] = "$rotulo: $servem servem + $fora fora = " . ( $servem + $fora )
				. ', e o banco tem ' . count( $nome_de ) . ' rejuntes';
		}
	}
}

pr_ok( ! $tab_erros, 'toda linha da tabela soma o banco inteiro de rejuntes',
	count( $grade ) . ' linhas, ' . count( $tab_erros ) . ' erro(s)' );
foreach ( array_slice( $tab_erros, 0, 12 ) as $e ) {
	echo "       -> $e\n";
}

echo "\nF1 — o bloco do rejunte, 3 tipos x 5 lugares x 12 folgas\n";

$f1_estados = 0;
$f1_erros   = array();

foreach ( $tipos as $tipo ) {
	foreach ( $ambientes as $amb ) {
		foreach ( $juntas as $j ) {
			$f1_estados++;
			$consulta = 'forma=disco&d=50&pastilha=p20&esp=6&sobra=15&rejunte=' . $tipo . '&onde=' . $amb . '&junta=' . $j;
			$bloco    = pr_bloco_f1( pr_corpo( pr_render( $raiz, 'cdm_f1', $consulta ) ) );
			$onde     = $tipo . ' / ' . $amb . ' / ' . $j . ' mm';

			if ( '' === $bloco ) {
				$f1_erros[] = "$onde: o bloco do rejunte nao foi servido";
				continue;
			}

			$texto    = pr_texto( $bloco );
			$prosa    = pr_texto( preg_replace( '#<li\b.*?</li>#is', ' ', $bloco ) );
			$esperado = pr_celula( $perfis, $j, $amb, $criticos );

			/* (a) A FRASE QUE A SENTINELA MEDIU NO AR NAO VOLTA. Ela afirmava
			   sobre o banco INTEIRO o que valia, no maximo, para um tipo. */
			if ( false !== mb_strpos( $texto, 'Nenhum rejunte do nosso banco declara folga de' ) ) {
				$f1_erros[] = "$onde: a frase do defeito de 12/09 voltou";
			}

			/* (b) TODO rejunte DO TIPO ESCOLHIDO e nomeado uma vez na prosa — seja
			   porque serve (e ai o cartao dele esta na lista), seja porque a
			   prestacao de contas diz por que ele nao esta. Os de outro tipo
			   aparecem so quando servem, e a linha deles diz isso. */
			foreach ( $nome_de as $id => $nome ) {
				if ( $tipo_de[ $id ] !== $tipo ) {
					continue;
				}
				$vezes = pr_conta_nome( $prosa, $nome, $todos_nomes );
				$no_cartao = ( pr_conta_nome( $texto, $nome, $todos_nomes ) > $vezes );
				if ( 1 !== $vezes + ( $no_cartao ? 1 : 0 ) ) {
					$f1_erros[] = "$onde: \"$nome\" (do tipo escolhido) e contado "
						. ( $vezes + ( $no_cartao ? 1 : 0 ) ) . ' vez(es) entre prosa e lista, e tem de ser 1';
				}
			}

			/* (c) A ACUSACAO BATE COM A CAUSA. Quando nenhum do tipo cai pela
			   folga, a pagina nao pode culpar a folga — foi exatamente isso que
			   o despacho mediu. */
			$do_tipo = function ( $lista ) use ( $tipo_de, $tipo ) {
				$out = array();
				foreach ( $lista as $id ) {
					if ( $tipo_de[ $id ] === $tipo ) {
						$out[] = $id;
					}
				}
				return $out;
			};
			$aprovados_tipo = $do_tipo( array_merge( $esperado['topo'], $esperado['abaixo'] ) );
			$folga_tipo     = $do_tipo( $esperado['fora_folga'] );
			$lugar_tipo     = $do_tipo( $esperado['fora_lugar'] );

			$culpa_a_folga = ( false !== mb_strpos( $texto, 'Fora por causa da folga de' ) );
			if ( $culpa_a_folga && ! $folga_tipo ) {
				$f1_erros[] = "$onde: a pagina culpa a folga e nenhum rejunte deste tipo cai pela folga";
			}
			if ( ! $aprovados_tipo && $lugar_tipo && ! $folga_tipo
				&& false === mb_strpos( $texto, 'é o LUGAR, não a folga' ) ) {
				$f1_erros[] = "$onde: quem exclui e o lugar, e a pagina nao diz isso";
			}

			/* (d) A CONTRADICAO DO MESMO BLOCO, que e o coracao do item 1 do
			   despacho: a NEGACAO EM BLOCO ("nenhum <tipo> do nosso banco serve")
			   e um produto do mesmo tipo listado como servindo, no mesmo lugar da
			   pagina. A linha de "fora por causa da folga" NAO e negacao em
			   bloco: ela nomeia produto e faixa, entao conviver com um vizinho
			   que serve numa faixa diferente e coerente, nao contradicao. */
			$nega_em_bloco = ( false !== mb_strpos( $texto, 'do nosso banco serve para essa peça' ) );
			if ( $nega_em_bloco && $aprovados_tipo ) {
				$f1_erros[] = "$onde: o bloco nega em bloco e lista produto do mesmo tipo servindo";
			}
			if ( ! $nega_em_bloco && ! $aprovados_tipo
				&& false === mb_strpos( $texto, 'Ainda não temos nenhum' ) ) {
				$f1_erros[] = "$onde: nenhum do tipo serve e a pagina nao diz isso";
			}

			/* (e) A linha de outro tipo nao promete folga que a celula ja filtrou
			   por lugar tambem. */
			if ( false !== mb_strpos( $texto, 'De outro tipo, mas dentro dessa folga' ) ) {
				$f1_erros[] = "$onde: a linha de outro tipo voltou a falar so de folga";
			}
		}
	}
}

pr_ok( ! $f1_erros, 'F1: a acusacao bate com a causa em todos os estados varridos',
	$f1_estados . ' estados, ' . count( $f1_erros ) . ' erro(s)' );
foreach ( array_slice( $f1_erros, 0, 12 ) as $e ) {
	echo "       -> $e\n";
}

echo "\n" . str_repeat( '-', 78 ) . "\n";
printf( "%d afirmacoes, %d falha(s). %d estados da F2 e %d da F1, um processo cada.\n",
	$feitos, $falhas, $f2_estados, $f1_estados );

exit( $falhas > 0 ? 1 : 0 );
