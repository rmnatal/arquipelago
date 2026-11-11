<?php
/**
 * O ROTEIRO SERVIDO NAO TEM OS PROPRIOS COMENTARIOS — PORTAO DO CHAO, 11/11/2026.
 *
 * O DEFEITO que este portao existe para impedir, medido no ar as 13h2xZ de
 * 11/11/2026 nas 10 URLs do sitemap: os quatro blocos `<script>` desta ilha
 * serviam 14 comentarios e 3.489 bytes, em 3 das 10 paginas (5 e 1.142 bytes
 * na home, 1 e 562 na F2, 8 e 1.785 na F3). SEIS deles traziam exatamente o
 * vocabulario que a 32.4 proibe: um nomeava OUTRA ILHA do arquipelago (*"a
 * cicatriz que a clubedomosaico pagou em 12/10/2026"*), um dizia `despacho` e
 * citava o numero de uma secao do contrato (*"o item 2 do despacho de
 * 30/10/2026"*, *"32.5"*), e outros diziam `cerebro` e `secao`.
 *
 * E A CAUSA DE NINGUEM VER E A DE 04/11 UM ANDAR AO LADO: a 32.4-b nasceu
 * nesta ilha e foi aplicada a uma METADE SO da pagina. O portao que ela criou
 * conta comentario dentro de `<style>` e nunca olhou `<script>`; a regua de
 * palavra de bastidor varre o HTML inteiro, mas com uma LISTA, e nenhuma das
 * palavras destes 14 comentarios estava nela. Entre a regua que mede o lugar
 * certo com a lista curta e a que tem a lista boa e mede o lugar errado cabia
 * o defeito inteiro.
 *
 * ESTE PORTAO E PHP pelo motivo que o `teste-folha-sem-comentario.php` ja
 * escreveu: a remocao e decidida em PHP, entao a regua CHAMA a funcao. Regua
 * em outra linguagem sobre o texto do PHP conferiria a FORMA.
 *
 * O QUE CADA METADE PROVA, dito separado porque o conserto de cada uma e
 * diferente (20.5):
 *
 *   (1) MUNDOS FABRICADOS, com a saida esperada escrita A MAO, e eles cobrem
 *       as tres armadilhas que o CSS nao tem: `//` dentro de URL em string,
 *       `/*` dentro de expressao regular, e a QUEBRA DE LINHA que tem de
 *       ficar porque o JavaScript fecha instrucao com ela.
 *   (2) A REGUA VELHA AO LADO DA NOVA, e elas tem de DISCORDAR (20.8):
 *       autoteste em que as duas concordam nao mede conserto nenhum. A velha
 *       e o removedor ingenuo de duas linhas — o que qualquer um escreveria.
 *   (3) OS QUATRO ROTEIROS DE VERDADE desta ilha, lidos dos snippets: zero
 *       comentario na saida, NADA INVENTADO, a conta do que desapareceu, e —
 *       a trava que vale mais que todas — `node --check` aprovando a ENTRADA
 *       e a SAIDA. Roteiro cortado errado quase sempre deixa de ser
 *       JavaScript valido, e quem diz isso nao e opiniao: e o proprio motor.
 *
 * O QUE ESTE PORTAO NAO PROVA, escrito para ninguem ler mais do que esta
 * aqui: que o roteiro continua FAZENDO o que fazia. Sintaxe valida nao e
 * comportamento igual. Quem mede isso e `ferramentas/teste-f1-arvore.mjs`
 * (que executa a arvore da F1 extraida do snippet) do chao, e
 * `ferramentas/medir-console-no-navegador.mjs` mais
 * `ferramentas/conferir-32-5-no-navegador.mjs` depois do desembarque —
 * roteiro quebrado aparece como mensagem de console e como pixel errado antes
 * de aparecer como qualquer outra coisa.
 */

if ( ! function_exists( 'esc_attr' ) ) {
	function esc_attr( $s ) { return htmlspecialchars( (string) $s, ENT_QUOTES ); }
}

$RAIZ = dirname( __DIR__ );

/**
 * Carrega UMA funcao de um snippet, equilibrando chaves.
 *
 * ESTE PORTAO TEM O SEU PROPRIO CARREGADOR, e nao e arrumacao: o das tres
 * baterias irmas conta `{` e `}` sem saber o que e STRING, e as funcoes desta
 * data comparam chave COMO DADO (`'{' === $js[ $i + 1 ]`). Com o contador
 * ingenuo, aquela chave solta dentro de aspas fecha a funcao cedo e o `eval`
 * morre com `Unmatched '}'` — medido na primeira versao desta bateria. Entao
 * aqui a varredura pula string, comentario de bloco e comentario de linha
 * antes de contar.
 */
function carregar_funcao( $src, $nome ) {
	$i = strpos( $src, "function $nome(" );
	if ( false === $i ) { return false; }
	$k = strpos( $src, '{', $i );
	$n = 0;
	$t = strlen( $src );
	while ( $k < $t ) {
		$c = $src[ $k ];
		if ( "'" === $c || '"' === $c ) {
			$k++;
			while ( $k < $t && $src[ $k ] !== $c ) {
				$k += ( '\\' === $src[ $k ] ) ? 2 : 1;
			}
			$k++;
			continue;
		}
		if ( '/' === $c && $k + 1 < $t && '*' === $src[ $k + 1 ] ) {
			$f = strpos( $src, '*' . '/', $k + 2 );
			$k = ( false === $f ) ? $t : $f + 2;
			continue;
		}
		if ( ( '/' === $c && $k + 1 < $t && '/' === $src[ $k + 1 ] ) || '#' === $c ) {
			$k += strcspn( $src, "\n", $k );
			continue;
		}
		if ( '{' === $c ) { $n++; }
		elseif ( '}' === $c ) { $n--; if ( 0 === $n ) { break; } }
		$k++;
	}
	eval( substr( $src, $i, $k - $i + 1 ) );

	return true;
}

$casca      = file_get_contents( $RAIZ . '/snippets/rodametria-casca.php' );
$falhas     = array();
$afirmacoes = 0;

function afirma( $cond, $msg ) {
	global $falhas, $afirmacoes;
	$afirmacoes++;
	if ( ! $cond ) { $falhas[] = $msg; }
}

/* A FUNCAO E AS QUATRO QUE ELA CHAMA. Cada uma e carregada pelo nome: derivar
   a lista do arquivo seria adivinhar, e `zero funcao achada` sairia como
   `portao verde`. */
foreach ( array(
	'rodametria_casca_js_fim_do_literal',
	'rodametria_casca_js_fim_da_substituicao',
	'rodametria_casca_js_abre_regex',
	'rodametria_casca_js_fim_da_regex',
	'rodametria_casca_js_sem_comentario',
) as $nome ) {
	afirma( carregar_funcao( $casca, $nome ), "a funcao $nome nao foi achada na casca" );
}
if ( ! function_exists( 'rodametria_casca_js_sem_comentario' ) ) {
	print( "teste-roteiro-sem-comentario: 1 falha(s)\n  REPROVADO: a casca nao tem a funcao\n" );
	exit( 1 );
}

/**
 * A REGUA VELHA — o removedor ingenuo que qualquer um escreveria, e que esta
 * aqui para DISCORDAR da nova (20.8). Ela nao sabe o que e literal: apaga
 * todo `/* ... * /` e todo `//` ate o fim da linha, levando a quebra.
 */
function regua_velha( $js ) {
	$js = preg_replace( '~/\*.*?\*/~s', '', $js );
	$js = preg_replace( '~//[^\n]*\n?~', '', $js );

	return trim( $js, "\n" );
}

/* ---------------------------------------------------------------------------
 * (1) OS MUNDOS FABRICADOS, com a saida esperada escrita A MAO
 * ------------------------------------------------------------------------- */

$A = '/' . '*';
$F = '*' . '/';

$mundos = array(
	array(
		'nome'    => '`//` dentro de string de URL sobrevive',
		'entrada' => "var u = 'https://s.shopee.com.br/a';",
		'espera'  => "var u = 'https://s.shopee.com.br/a';",
		'discorda_da_velha' => true,
	),
	array(
		'nome'    => '`' . $A . '` dentro de string sobrevive',
		'entrada' => 'var s = "abre ' . $A . ' aqui";',
		'espera'  => 'var s = "abre ' . $A . ' aqui";',
		'discorda_da_velha' => false,
	),
	array(
		'nome'    => '`//` dentro de template sobrevive',
		'entrada' => 'var t = `veja https://x/y e pronto`;',
		'espera'  => 'var t = `veja https://x/y e pronto`;',
		'discorda_da_velha' => true,
	),
	array(
		'nome'    => 'template com `${}` que tem `}` dentro de string',
		'entrada' => 'var t = `a${ f("}") }b`; ' . $A . ' nota ' . $F,
		'espera'  => 'var t = `a${ f("}") }b`;',
		'discorda_da_velha' => false,
	),
	/* `' . $A . '` DENTRO DE CLASSE DE CARACTERE, e nao no comeco da expressao:
	   em JavaScript uma `/` seguida de `*` e SEMPRE comentario, porque `*`
	   nao pode abrir expressao regular (quantificador sem nada para repetir).
	   A primeira versao deste mundo esperava `/' . $A . '/g` sobrevivendo e
	   estava ERRADA — e o node concordou com a funcao, nao com o mundo. */
	array(
		'nome'    => '`' . $A . '` dentro de CLASSE de expressao regular sobrevive',
		'entrada' => 'var r = s.replace(/[/*]/g, ""); ' . $A . ' nota ' . $F,
		'espera'  => 'var r = s.replace(/[/*]/g, "");',
		'discorda_da_velha' => true,
	),
	array(
		'nome'    => 'expressao regular com `/` dentro de classe sobrevive',
		'entrada' => 'var r = /[/]/g; ' . $A . ' nota ' . $F,
		'espera'  => 'var r = /[/]/g;',
		'discorda_da_velha' => false,
	),
	array(
		'nome'    => 'comentario de LINHA sai e A QUEBRA FICA (ponto e virgula automatico)',
		'entrada' => "var a = 1 // conta\nvar b = 2",
		'espera'  => "var a = 1\nvar b = 2",
		'discorda_da_velha' => true,
	),
	array(
		'nome'    => 'comentario COLADO entre dois caracteres de palavra vira UM espaco',
		'entrada' => 'var ab' . $A . 'x' . $F . 'cd = 1;',
		'espera'  => 'var ab cd = 1;',
		'discorda_da_velha' => true,
	),
	array(
		'nome'    => 'comentario de bloco SEM FECHAR come o resto, como no navegador',
		'entrada' => "var a = 1;\n" . $A . " nota que ninguem fechou\nvar b = 2;",
		'espera'  => 'var a = 1;',
		'discorda_da_velha' => true,
	),
	array(
		'nome'    => 'divisao NAO e lida como expressao regular',
		'entrada' => 'var x = a / b; ' . $A . ' nota ' . $F . ' var y = c / d;',
		'espera'  => 'var x = a / b;  var y = c / d;',
		'discorda_da_velha' => false,
	),
	/* `return /re/` E O CASO QUE A POSICAO DECIDE: quem le a `/` depois de
	   `return` como DIVISAO continua a varredura dentro da expressao, ve o
	   `//` da classe como comentario de linha e come `]/.test(s); }` ate o
	   fim da linha. A regua ingenua faz exatamente isso. */
	array(
		'nome'    => '`return /re/` abre expressao regular, e nao divide',
		'entrada' => 'function f(s){ return /[//]/.test(s); }',
		'espera'  => 'function f(s){ return /[//]/.test(s); }',
		'discorda_da_velha' => true,
	),
	array(
		'nome'    => 'roteiro sem comentario nenhum sai IDENTICO',
		'entrada' => "var a = 1;\nvar b = 2;",
		'espera'  => "var a = 1;\nvar b = 2;",
		'discorda_da_velha' => false,
	),
);

$discordancias = 0;
foreach ( $mundos as $m ) {
	$saiu = rodametria_casca_js_sem_comentario( $m['entrada'] );
	afirma( $saiu === $m['espera'],
		sprintf( 'mundo %s: saiu %s, esperava %s',
			$m['nome'], var_export( $saiu, true ), var_export( $m['espera'], true ) ) );

	$velha = regua_velha( $m['entrada'] );
	if ( $m['discorda_da_velha'] ) {
		afirma( $velha !== $saiu,
			sprintf( 'mundo %s: a regua VELHA devolveu o MESMO que a nova — autoteste em '
				. 'que as duas concordam nao mede conserto nenhum (20.8)', $m['nome'] ) );
		if ( $velha !== $saiu ) { $discordancias++; }
	}
}
afirma( $discordancias >= 6,
	sprintf( 'so %d mundo(s) separam a regua nova da velha; a bateria pede ao menos 6',
		$discordancias ) );
printf( "   mundos fabricados: %d, e %d deles separam a regua nova da ingenua\n",
	count( $mundos ), $discordancias );

/* ---------------------------------------------------------------------------
 * (2) OS QUATRO ROTEIROS DE VERDADE DESTA ILHA
 *
 * Lidos do snippet entre a abertura e o fechamento da captura — o mesmo par
 * que o WordPress executa.
 * ------------------------------------------------------------------------- */

$ROTEIROS = array(
	'rodametria-casca' => 'rodametria-casca-js',
	'rodametria-f1'    => 'rodametria-f1-js',
	'rodametria-f2'    => 'rodametria-f2-js',
	'rodametria-f3'    => 'rodametria-f3-js',
);

$roteiros = array();
foreach ( $ROTEIROS as $arquivo => $ident ) {
	$src = file_get_contents( $RAIZ . '/snippets/' . $arquivo . '.php' );
	$i   = strpos( $src, '<?php rodametria_casca_abrir_roteiro(); ?>' );
	afirma( false !== $i, "$arquivo: nao chama rodametria_casca_abrir_roteiro() — o roteiro "
		. 'dele nao passa pelo conserto, e e a 32.5-c outra vez (regra que nao viaja)' );
	if ( false === $i ) { continue; }
	$i = strpos( $src, "\n", $i ) + 1;
	$j = strpos( $src, "<?php rodametria_casca_fechar_roteiro( '$ident' ); ?>", $i );
	afirma( false !== $j, "$arquivo: abre a captura do roteiro e nao a fecha com o id $ident" );
	if ( false === $j ) { continue; }
	$roteiros[ $arquivo ] = substr( $src, $i, $j - $i );
}
afirma( count( $ROTEIROS ) === count( $roteiros ),
	sprintf( 'eram %d roteiros a conferir e foram achados %d',
		count( $ROTEIROS ), count( $roteiros ) ) );

/* O `node` e quem diz se o corte deixou JavaScript valido. Sem ele a bateria
   perde a sua trava mais forte, e isso vai IMPRESSO em vez de passar calado. */
$node = trim( (string) shell_exec( 'command -v node 2>/dev/null' ) );
$checados = 0;

function node_aprova( $node, $js, &$erro ) {
	$arq = tempnam( sys_get_temp_dir(), 'rdm' ) . '.mjs';
	file_put_contents( $arq, $js );
	$saida = array();
	$cod   = 0;
	exec( escapeshellarg( $node ) . ' --check ' . escapeshellarg( $arq ) . ' 2>&1', $saida, $cod );
	unlink( $arq );
	$erro = implode( "\n", array_slice( $saida, 0, 4 ) );

	return 0 === $cod;
}

foreach ( $roteiros as $nome => $js ) {
	$saiu = rodametria_casca_js_sem_comentario( $js );

	/* (a) comentario de ENTRADA existe em ao menos um deles — bateria que roda
	       sobre roteiro sem comentario nenhum aprova sem medir. A conta por
	       roteiro sai impressa; a exigencia e no TOTAL, porque o roteiro da
	       casca e curto e pode legitimamente nao ter comentario. */
	$entrada_coment = preg_match_all( '~' . preg_quote( $A, '~' ) . '~', $js );

	/* (b) comentario de SAIDA e zero, nas duas formas. E o `//` se conta FORA
	       de literal, com uma regua escrita AQUI: a de dentro da funcao decide
	       o que APAGAR, esta decide o que CONTAR (secao 8). */
	afirma( 0 === preg_match_all( '~' . preg_quote( $A, '~' ) . '~', $saiu ),
		sprintf( '%s: o roteiro SAIU com %d `%s` ainda dentro', $nome,
			preg_match_all( '~' . preg_quote( $A, '~' ) . '~', $saiu ), $A ) );
	afirma( false === strpos( $saiu, $F ),
		"$nome: o roteiro saiu com um fechamento de comentario solto" );
	$sem_literal = preg_replace(
		array( '~"(?:\\\\.|[^"\\\\])*"~s', "~'(?:\\\\.|[^'\\\\])*'~s", '~`(?:\\\\.|[^`\\\\])*`~s' ),
		'""', $saiu );
	afirma( 0 === preg_match_all( '~//~', $sem_literal ),
		sprintf( '%s: o roteiro saiu com %d `//` fora de literal', $nome,
			preg_match_all( '~//~', $sem_literal ) ) );

	/* (c) comentario SEM FECHAR no roteiro do repositorio e defeito: ele
	       comeria o resto dele, e a funcao faz o mesmo de proposito. */
	$abertos  = preg_match_all( '~' . preg_quote( $A, '~' ) . '~', $js );
	$fechados = preg_match_all( '~' . preg_quote( $F, '~' ) . '~', $js );
	afirma( $abertos === $fechados,
		sprintf( '%s: %d comentario(s) abertos contra %d fechados — roteiro com comentario '
			. 'sem fechar perde o resto de si no navegador', $nome, $abertos, $fechados ) );

	/* (d) NADA INVENTADO: a saida, sem espaco em branco, e subsequencia da
	       entrada sem espaco em branco. A funcao so APAGA — o unico caractere
	       que ela acrescenta e espaco, e espaco esta fora desta conta. */
	$a  = preg_replace( '~\s+~', '', $js );
	$b  = preg_replace( '~\s+~', '', $saiu );
	$pa = 0;
	for ( $pb = 0; $pb < strlen( $b ); $pb++ ) {
		while ( $pa < strlen( $a ) && $a[ $pa ] !== $b[ $pb ] ) { $pa++; }
		if ( $pa >= strlen( $a ) ) { break; }
		$pa++;
	}
	afirma( $pb === strlen( $b ),
		sprintf( '%s: a saida NAO e subsequencia da entrada — a funcao inventou byte '
			. '(parou no caractere %d de %d)', $nome, $pb, strlen( $b ) ) );

	/* (e) O QUE DESAPARECEU E EXATAMENTE O QUE MORAVA DENTRO DE COMENTARIO.
	       A conta usa o achador INGENUO de comentario sobre o roteiro de
	       verdade, e isso e legitimo porque uma afirmacao a parte MEDE que nos
	       quatro roteiros de hoje o ingenuo e o verdadeiro acham o mesmo: zero
	       `//` e zero `' . $A . '` dentro de literal. No dia em que um deles
	       ganhar uma URL no codigo, aquela afirmacao fica VERMELHA e aponta
	       para o lugar certo, em vez de esta conta aprovar errado em silencio. */
	afirma( 0 === preg_match_all( '~//~', preg_replace(
			array( '~"(?:\\\\.|[^"\\\\])*"~s', "~'(?:\\\\.|[^'\\\\])*'~s", '~`(?:\\\\.|[^`\\\\])*`~s' ),
			'""', $js ) ),
		sprintf( '%s: o roteiro de ENTRADA tem `//` fora de literal, e a conta do item (e) '
			. 'desta bateria supoe que nao ha — leia o comentario dela antes de mexer', $nome ) );
	$dentro = array( '{' => 0, '}' => 0, ';' => 0, '(' => 0, ')' => 0 );
	preg_match_all( '~' . preg_quote( $A, '~' ) . '.*?' . preg_quote( $F, '~' ) . '~s', $js, $achados );
	foreach ( $achados[0] as $c ) {
		foreach ( array_keys( $dentro ) as $t ) { $dentro[ $t ] += substr_count( $c, $t ); }
	}
	foreach ( $dentro as $t => $q ) {
		afirma( substr_count( $saiu, $t ) === substr_count( $js, $t ) - $q,
			sprintf( '%s: %d `%s` na saida, e a conta pedia %d (%d na entrada menos %d que '
				. 'moravam dentro de comentario) — a funcao cortou codigo de verdade',
				$nome, substr_count( $saiu, $t ), $t,
				substr_count( $js, $t ) - $q, substr_count( $js, $t ), $q ) );
	}

	/* (f) E A TRAVA QUE VALE MAIS QUE TODAS: `node --check` na ENTRADA e na
	       SAIDA. O pacote de dado do rodape e PHP, entao ele entra como `null`
	       — e o que esta bateria julga nao e o dado, e o corte. */
	if ( '' !== $node ) {
		$erro = '';
		$ent  = preg_replace( '~<\?php.*?\?>~s', 'null', $js );
		$sai  = preg_replace( '~<\?php.*?\?>~s', 'null', $saiu );
		afirma( node_aprova( $node, $ent, $erro ),
			sprintf( '%s: a ENTRADA nao e JavaScript valido nem antes do corte: %s', $nome, $erro ) );
		afirma( node_aprova( $node, $sai, $erro ),
			sprintf( '%s: o corte deixou de ser JavaScript valido: %s', $nome, $erro ) );
		$checados++;
	}

	printf( "   %-20s %6d -> %6d bytes  (-%d, %d comentario(s) de bloco)\n",
		$nome, strlen( $js ), strlen( $saiu ), strlen( $js ) - strlen( $saiu ), $fechados );
}

$total_coment = 0;
foreach ( $roteiros as $js ) {
	$total_coment += preg_match_all( '~' . preg_quote( $A, '~' ) . '~', $js );
}
afirma( $total_coment > 0,
	'nenhum dos quatro roteiros tem um comentario — esta bateria estaria aprovando sobre nada' );

if ( '' === $node ) {
	print( "   SEM `node` NESTA MAQUINA: os 8 `--check` NAO foram rodados, e esta linha "
		. "existe para ninguem ler o verde como se eles tivessem passado\n" );
} else {
	printf( "   node --check: %d roteiro(s) conferidos antes E depois do corte\n", $checados );
}

/* ---------------------------------------------------------------------------
 * (3) NENHUM SNIPPET ESCREVE A TAG `<script>` DE ROTEIRO A MAO
 *
 * A conta e no HTML CRU do snippet — o texto FORA de `<?php ... ?>`, que e o
 * unico lugar de onde uma tag sai sem passar pela casca. O `<script
 * type="application/ld+json">` e ECHOADO do PHP e nao e roteiro: ele serve
 * dado estruturado, nao codigo, e nao tem comentario para esconder.
 * ------------------------------------------------------------------------- */
$com_tag = array();
foreach ( glob( $RAIZ . '/snippets/*.php' ) as $arq ) {
	/* O HTML CRU SAI DO TOKENIZADOR DO PHP, nunca de recorte de texto. A
	   primeira versao desta afirmacao cortava `<?php ... ?>` com expressao
	   regular nao-gulosa e REPROVOU a casca certa: o arquivo abre em `<?php`
	   na linha 1 e o primeiro `?>` esta dentro de uma funcao, entao todo o
	   PHP seguinte entrava na conta como se fosse HTML — e o `echo '<script
	   type="application/ld+json">'` virava tag escrita a mao. Quem sabe onde
	   o PHP acaba e o PHP. */
	$cru = '';
	foreach ( token_get_all( file_get_contents( $arq ) ) as $t ) {
		if ( is_array( $t ) && T_INLINE_HTML === $t[0] ) { $cru .= $t[1]; }
	}
	if ( preg_match( '~<script(?![^>]*ld\+json)~i', $cru ) ) {
		$com_tag[] = basename( $arq );
	}
}
afirma( array() === $com_tag,
	sprintf( 'estes snippets escrevem a tag `<script>` de roteiro a mao, fora da casca: %s '
		. '— roteiro que nasce assim nao passa pelo conserto (32.5-c)',
		implode( ', ', $com_tag ) ) );

printf( "teste-roteiro-sem-comentario: %d afirmacoes, %d falha(s)\n", $afirmacoes, count( $falhas ) );
foreach ( $falhas as $f ) { print( "  REPROVADO: $f\n" ); }
print( count( $falhas ) ? "REPROVADO\n" : "APROVADO\n" );
exit( count( $falhas ) ? 1 : 0 );
