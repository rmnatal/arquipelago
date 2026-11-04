<?php
/**
 * A FOLHA SERVIDA NAO TEM OS PROPRIOS COMENTARIOS — PORTAO DO CHAO, 04/11/2026.
 *
 * O DEFEITO que este portao existe para impedir, medido no ar as 19h2xZ de
 * 04/11/2026 nas 9 URLs do sitemap: as folhas desta ilha serviam 23
 * comentarios de CSS e 7.486 bytes na home e na F2, 24 e 7.866 nas tres de
 * produto, 24 e 7.827 nas quatro institucionais. Tres deles nomeiam uma rotina
 * desta pasta (`conferir-32-5-no-navegador.mjs`), um diz `bancada`, e varios
 * trazem numero de secao do contrato e prosa de bastidor — a lista da 32.4.
 *
 * ESTE PORTAO E PHP pelo motivo que o `teste-escada-de-compra.php` ja escreveu:
 * a remocao e decidida em PHP, entao a regua CHAMA a funcao. Regua em Python
 * sobre o texto do PHP conferiria a FORMA.
 *
 * O QUE CADA METADE PROVA, dito separado porque o conserto de cada uma e
 * diferente (20.5):
 *
 *   (1) MUNDOS FABRICADOS, com a saida esperada escrita A MAO: e aqui que a
 *       independencia vive. `content:"/*"`, `url(data:...)` com `/*` dentro,
 *       string de aspa simples, aspa escapada, comentario COLADO entre dois
 *       caracteres de palavra e comentario SEM FECHAR. Se a funcao e a regua
 *       dividissem a nocao de comentario em todos os casos, este portao nao
 *       mediria nada — nestes seis a saida e literal.
 *   (2) A REGUA VELHA AO LADO DA NOVA, e elas tem de DISCORDAR (20.8):
 *       autoteste em que as duas concordam nao mede conserto nenhum. A velha e
 *       o removedor ingenuo de uma linha.
 *   (3) AS TRES FOLHAS DE VERDADE desta ilha, lidas dos snippets: zero `/*` na
 *       saida, chaves equilibradas, e NADA INVENTADO — a saida, sem espaco em
 *       branco, tem de ser subsequencia da entrada sem espaco em branco.
 *
 * O QUE ESTE PORTAO NAO PROVA, e esta escrito para ninguem ler mais do que
 * esta aqui: que a folha de verdade continua PINTANDO igual. Isso nao se
 * afirma do chao — quem o mede e
 * `ferramentas/conferir-32-5-no-navegador.mjs`, no navegador, depois do
 * desembarque, porque folha cortada errado aparece como pixel errado antes de
 * aparecer como qualquer outra coisa.
 */

if ( ! function_exists( 'esc_attr' ) ) {
	function esc_attr( $s ) { return htmlspecialchars( (string) $s, ENT_QUOTES ); }
}

$RAIZ = dirname( __DIR__ );

/** Carrega UMA funcao de um snippet, equilibrando chaves — o mesmo mecanismo
 *  do `teste-escada-de-compra.php` e do `teste-nota-de-preco.php`. */
function carregar_funcao( $src, $nome ) {
	$i = strpos( $src, "function $nome(" );
	if ( false === $i ) { return false; }
	$j = strpos( $src, '{', $i );
	$n = 0;
	for ( $k = $j; $k < strlen( $src ); $k++ ) {
		if ( '{' === $src[ $k ] ) { $n++; }
		elseif ( '}' === $src[ $k ] ) { $n--; if ( 0 === $n ) { break; } }
	}
	eval( substr( $src, $i, $k - $i + 1 ) );

	return true;
}

$casca = file_get_contents( $RAIZ . '/snippets/rodametria-casca.php' );
$falhas = array();
$afirmacoes = 0;

function afirma( $cond, $msg ) {
	global $falhas, $afirmacoes;
	$afirmacoes++;
	if ( ! $cond ) { $falhas[] = $msg; }
}

afirma( carregar_funcao( $casca, 'rodametria_casca_css_sem_comentario' ),
	'a funcao rodametria_casca_css_sem_comentario nao foi achada na casca' );
if ( ! function_exists( 'rodametria_casca_css_sem_comentario' ) ) {
	echo "REPROVADO: a funcao do conserto nao existe na casca.\n";
	exit( 1 );
}

/** A REGUA VELHA, reproduzida de proposito: o removedor ingenuo de uma linha,
 *  que e o que qualquer um escreveria primeiro. Ela existe para DISCORDAR. */
function regua_velha( $css ) {
	return preg_replace( '~/\*.*?\*/~s', '', (string) $css );
}

$A = '/*';   /* montados para o `*` + `/` de fechamento nao fechar ESTE comentario */
$F = '*' . '/';

/* ---------------------------------------------------------------------------
 * (1) OS SEIS MUNDOS FABRICADOS, com a saida esperada escrita A MAO
 * ------------------------------------------------------------------------- */
$mundos = array(
	array(
		'nome'    => 'comentario simples sai inteiro',
		'entrada' => ".a{color:red}\n" . $A . ' nota ' . $F . "\n.b{color:blue}",
		'espera'  => ".a{color:red}\n.b{color:blue}",
		'discorda_da_velha' => false,
	),
	array(
		/* O MUNDO QUE A REGUA VELHA DESTROI: o `/*` vive dentro de uma string e
		   o `*` + `/` de um comentario de verdade vem DEPOIS. A velha casa de um
		   ao outro e leva `.b` junto. */
		'nome'    => 'content com /* DENTRO de aspas duplas SOBREVIVE, e .b com ele',
		'entrada' => '.a::before{content:"' . $A . '"}.b{color:red}' . $A . ' nota ' . $F,
		'espera'  => '.a::before{content:"' . $A . '"}.b{color:red}',
		'discorda_da_velha' => true,
	),
	array(
		'nome'    => 'url(data:...) com /* dentro SOBREVIVE, sem quote',
		'entrada' => ".a{background:url(data:image/svg+xml;utf8,<svg x='" . $A . "'/>)}"
			. '.b{color:red}' . $A . ' nota ' . $F,
		'espera'  => ".a{background:url(data:image/svg+xml;utf8,<svg x='" . $A . "'/>)}"
			. '.b{color:red}',
		'discorda_da_velha' => true,
	),
	array(
		'nome'    => 'string de aspa SIMPLES com /* dentro SOBREVIVE',
		'entrada' => ".a::after{content:'" . $A . "'}.b{color:red}" . $A . ' nota ' . $F,
		'espera'  => ".a::after{content:'" . $A . "'}.b{color:red}",
		'discorda_da_velha' => true,
	),
	array(
		/* A aspa ESCAPADA nao fecha a string: se fechasse, o `/*` de dentro
		   passaria a ser comentario e a declaracao sairia cortada. */
		'nome'    => 'aspa ESCAPADA nao fecha a string antes da hora',
		'entrada' => '.a::before{content:"x\\"' . $A . 'y"}.b{color:red}' . $A . ' n ' . $F,
		'espera'  => '.a::before{content:"x\\"' . $A . 'y"}.b{color:red}',
		'discorda_da_velha' => true,
	),
	array(
		/* OS DOIS VIZINHOS SAO CARACTERE DE PALAVRA: `v` e `s`. Tirar o
		   comentario como nada escreveria `divspan`, que e um terceiro seletor
		   que ninguem escreveu. */
		'nome'    => 'comentario COLADO entre dois caracteres de palavra vira UM espaco',
		'entrada' => 'div' . $A . 'x' . $F . 'span{color:red}',
		'espera'  => 'div span{color:red}',
		'discorda_da_velha' => true,
	),
	array(
		'nome'    => 'comentario SEM FECHAR come o resto, como no navegador',
		'entrada' => ".a{color:red}\n" . $A . " nota que ninguem fechou\n.b{color:blue}",
		'espera'  => '.a{color:red}',
		'discorda_da_velha' => true,
	),
	array(
		'nome'    => 'folha sem comentario nenhum sai IDENTICA',
		'entrada' => ".a{color:red}\n.b{color:blue}",
		'espera'  => ".a{color:red}\n.b{color:blue}",
		'discorda_da_velha' => false,
	),
);

$discordancias = 0;
foreach ( $mundos as $m ) {
	$saiu = rodametria_casca_css_sem_comentario( $m['entrada'] );
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

/* ---------------------------------------------------------------------------
 * (2) AS TRES FOLHAS DE VERDADE DESTA ILHA
 *
 * A folha e lida do snippet entre a abertura e o fechamento da captura — o
 * mesmo par que o WordPress executa. Ler o arquivo aqui e o certo: o CSS e
 * texto literal no snippet, e o que esta bateria julga e o que a FUNCAO faz
 * com ele.
 * ------------------------------------------------------------------------- */
$folhas = array();
foreach ( array( 'rodametria-casca', 'rodametria-institucional', 'rodametria-produto' ) as $nome ) {
	$src = file_get_contents( $RAIZ . '/snippets/' . $nome . '.php' );
	$i = strpos( $src, 'rodametria_casca_abrir_folha(); ?>' );
	afirma( false !== $i, "$nome: nao chama rodametria_casca_abrir_folha() — a folha dele "
		. 'nao passa pelo conserto, e e a 32.5-c outra vez (regra que nao viaja para as irmas)' );
	if ( false === $i ) { continue; }
	$i = strpos( $src, "\n", $i ) + 1;
	$j = strpos( $src, '<?php rodametria_casca_fechar_folha(', $i );
	afirma( false !== $j, "$nome: abre a captura da folha e nao a fecha" );
	if ( false === $j ) { continue; }
	$folhas[ $nome ] = substr( $src, $i, $j - $i );
}
afirma( 3 === count( $folhas ), sprintf( 'eram 3 folhas a conferir e foram achadas %d', count( $folhas ) ) );

foreach ( $folhas as $nome => $css ) {
	$saiu = rodametria_casca_css_sem_comentario( $css );

	/* (a) comentario de ENTRADA existe — bateria que roda sobre folha sem
	       comentario nenhum aprova sem medir. */
	$quantos = preg_match_all( '~/\*~', $css );
	afirma( $quantos > 0, "$nome: a folha de entrada nao tem um `/*` — esta bateria estaria "
		. 'aprovando sobre nada' );

	/* (b) comentario de SAIDA e zero. */
	afirma( 0 === preg_match_all( '~/\*~', $saiu ),
		sprintf( '%s: a folha SAIU com %d `/*` ainda dentro', $nome,
			preg_match_all( '~/\*~', $saiu ) ) );
	afirma( false === strpos( $saiu, '*' . '/' ),
		"$nome: a folha saiu com um fechamento de comentario solto" );

	/* (c) comentario SEM FECHAR na folha do repositorio e defeito: ele comeria
	       o resto dela no navegador, e a funcao faz o mesmo de proposito. */
	$abertos = preg_match_all( '~/\*~', $css );
	$fechados = preg_match_all( '~\*/~', $css );
	afirma( $abertos === $fechados,
		sprintf( '%s: %d comentario(s) abertos contra %d fechados — folha com comentario sem '
			. 'fechar perde o resto de si no navegador', $nome, $abertos, $fechados ) );

	/* (d) chaves equilibradas na saida. */
	afirma( substr_count( $saiu, '{' ) === substr_count( $saiu, '}' ),
		sprintf( '%s: a saida tem %d `{` contra %d `}`', $nome,
			substr_count( $saiu, '{' ), substr_count( $saiu, '}' ) ) );

	/* (e) NADA INVENTADO: a saida, sem espaco em branco, e subsequencia da
	       entrada sem espaco em branco. A funcao so APAGA — o unico caractere
	       que ela acrescenta e espaco, e espaco esta fora desta conta. */
	$a = preg_replace( '~\s+~', '', $css );
	$b = preg_replace( '~\s+~', '', $saiu );
	$pa = 0;
	for ( $pb = 0; $pb < strlen( $b ); $pb++ ) {
		while ( $pa < strlen( $a ) && $a[ $pa ] !== $b[ $pb ] ) { $pa++; }
		if ( $pa >= strlen( $a ) ) { break; }
		$pa++;
	}
	afirma( $pb === strlen( $b ),
		sprintf( '%s: a saida NAO e subsequencia da entrada — a funcao inventou byte '
			. '(parou no caractere %d de %d)', $nome, $pb, strlen( $b ) ) );

	/* (f) O QUE DESAPARECEU E EXATAMENTE O QUE MORAVA DENTRO DE COMENTARIO, e
	       esta e a trava mais forte desta bateria: a contagem de `{`, `}` e `;`
	       da saida tem de ser a da entrada MENOS a que estava dentro dos
	       comentarios. Medido na folha da casca em 04/11/2026: 145 `{` para
	       140, 282 `;` para 280 — e dentro dos 23 comentarios havia
	       exatamente 5 `{`, 5 `}` e 2 `;`, que eram CSS comentado na prosa. Se
	       a funcao cortasse uma declaracao de verdade, esta conta abriria. */
	$dentro = array( '{' => 0, '}' => 0, ';' => 0 );
	preg_match_all( '~/\*.*?\*/~s', $css, $achados );
	foreach ( $achados[0] as $c ) {
		foreach ( array_keys( $dentro ) as $t ) { $dentro[ $t ] += substr_count( $c, $t ); }
	}
	foreach ( $dentro as $t => $q ) {
		afirma( substr_count( $saiu, $t ) === substr_count( $css, $t ) - $q,
			sprintf( '%s: %d `%s` na saida, e a conta pedia %d (%d na entrada menos %d que '
				. 'moravam dentro de comentario) — a funcao cortou CSS de verdade',
				$nome, substr_count( $saiu, $t ), $t,
				substr_count( $css, $t ) - $q, substr_count( $css, $t ), $q ) );
	}

	/* (g) a folha encolheu, e o quanto esta impresso para a proxima execucao
	       comparar em vez de supor. */
	afirma( strlen( $saiu ) < strlen( $css ),
		"$nome: a folha saiu do mesmo tamanho — nenhum comentario foi tirado" );
	printf( "   %-26s %6d -> %6d bytes  (-%d, %d comentario(s))\n",
		$nome, strlen( $css ), strlen( $saiu ), strlen( $css ) - strlen( $saiu ), $fechados );
}

/* ---------------------------------------------------------------------------
 * (3) NENHUM SNIPPET ESCREVE A TAG `<style>` A MAO
 *
 * A conta e feita no HTML CRU do snippet — o texto que fica FORA de
 * `<?php ... ?>`, que e o unico lugar de onde uma tag sai sem passar por
 * funcao. Mencao a `<style>` em comentario ou em string de PHP nao e tag
 * servida, e contar o arquivo inteiro reprovaria o proprio conserto: e o
 * perigo da 20.5 (portao que reprova a pagina certa e o caminho mais curto
 * para alguem ignora-lo).
 * ------------------------------------------------------------------------- */
foreach ( array( 'rodametria-casca', 'rodametria-institucional', 'rodametria-produto',
	'rodametria-f2' ) as $nome ) {
	$src = file_get_contents( $RAIZ . '/snippets/' . $nome . '.php' );
	$html_cru = preg_replace( '~<\?php.*?\?>~s', '', $src );
	$cru = preg_match_all( '~</?style~i', $html_cru );
	afirma( 0 === $cru, sprintf( '%s: o HTML cru dele traz %d tag(s) <style> — a tag sai da '
		. 'casca, em um lugar so, senao folha nova nasce fora do conserto', $nome, $cru ) );
}

/* E a casca e o UNICO lugar que imprime a tag. */
$quantos_imprimem = 0;
foreach ( array( 'rodametria-casca', 'rodametria-institucional', 'rodametria-produto',
	'rodametria-f2' ) as $nome ) {
	$src = file_get_contents( $RAIZ . '/snippets/' . $nome . '.php' );
	if ( false !== strpos( $src, "echo \"\\n\" . '<style id=\"'" ) ) { $quantos_imprimem++; }
}
afirma( 1 === $quantos_imprimem,
	sprintf( '%d snippet(s) imprimem a tag <style>; tem de ser exatamente 1 (a casca)',
		$quantos_imprimem ) );

echo "\n";
if ( $falhas ) {
	echo sprintf( "REPROVADO: %d falha(s) em %d afirmacao(oes).\n", count( $falhas ), $afirmacoes );
	foreach ( $falhas as $f ) { echo "  - $f\n"; }
	exit( 1 );
}
echo sprintf( "APROVADO: %d afirmacao(oes), 0 falha. %d mundo(s) fabricado(s), %d deles "
	. "separando a regua nova da velha.\n", $afirmacoes, count( $mundos ), $discordancias );
exit( 0 );
