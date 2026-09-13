<?php
/**
 * OS TAMANHOS DE PASTILHA DA F1, MEDIDOS NO PRÓPRIO SNIPPET — nunca digitados
 * em quem os consome.
 *
 *   php ferramentas/tamanhos-da-f1.php .            # JSON para a varredura
 *   php ferramentas/tamanhos-da-f1.php . --humano   # a mesma coisa, legível
 *
 * POR QUE ESTE ARQUIVO NASCEU, e a data importa: 13/09/2026, no bloco que fechou
 * o tamanho 2×2 da categoria pastilha. O `ferramentas/validar-pastilhas.py`
 * carregava a lista dos tamanhos da F1 numa constante escrita à mão — quatro
 * linhas, com o comentário "os tamanhos que a F1 oferece". A F1 oferece CINCO:
 * 1×1, **1,5×1,5**, 2×2, 2,5×2,5 e o caquinho irregular. A cópia tinha nascido
 * certa e envelheceu calada no dia em que a ferramenta ganhou o 1,5.
 *
 * O CUSTO NÃO ERA COSMÉTICO, e é ele que justifica um arquivo novo em vez de uma
 * linha a mais na constante. A seção 14.3 do `ARQUIPELAGO.md` manda varrer "a
 * faixa de entrada de cada ferramenta de ponta a ponta"; a cobertura por tamanho
 * era publicada sobre quatro linhas de uma faixa de cinco, então **um tamanho que
 * a ferramenta serve nunca apareceu no relatório do buraco**. E logo esse: 1,5 cm
 * é o lado do `pastilhart-af1500`, o único item do banco sustentado por
 * distribuidor (nível 5). A mutação 07 da bateria desta categoria diz, com todas
 * as letras, que promover o distribuidor "faz 1,5 cm passar de zero para um
 * elegível" — uma afirmação sobre uma linha que o relatório não tinha. A mutação
 * reprovava por outro motivo (o nível na régua por item) e ninguém percebeu.
 *
 * É a mesma família do "número de tela nasce contado, nunca digitado" (seção 8) e
 * da lista de tipos que a Robometria tirou de dentro da régua em 13/09/2026, pela
 * seção 26: lista dentro da régua envelhece calada, e o sintoma é o portão verde.
 *
 * ELE NÃO LÊ O CÓDIGO-FONTE: PROVOCA A FERRAMENTA, como o irmão
 * `faixa-da-f2.php`. As chaves saem de `cdm_f1_pastilhas_disponiveis()`, que é a
 * declaração da própria F1 e não uma cópia; cada uma é então posta em
 * `$_GET['pastilha']` e passada por `cdm_f1_entrada()` — a MESMA função que sanea
 * a consulta de quem visita — para provar que ela sobrevive ao saneamento. As
 * duas metades importam e falham por motivos diferentes: tamanho declarado que o
 * saneamento derruba é tamanho que a tela lista e a ferramenta não aceita.
 *
 * E o superconjunto tem que passar dos dois lados, ou não mede borda nenhuma: uma
 * chave inventada é provocada junto, e a ferramenta tem obrigação de recusá-la
 * caindo no padrão. Se o inventado passar, isto FALHA — saneamento que aceita
 * qualquer coisa não tem faixa.
 */

require __DIR__ . '/render-para-teste.php';

$raiz   = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';
$humano = in_array( '--humano', $argv, true );

cdm_teste_carregar( $raiz );
cdm_teste_carregar_options( $raiz );

if ( ! function_exists( 'cdm_f1_entrada' ) || ! function_exists( 'cdm_f1_pastilhas_disponiveis' ) ) {
	fwrite( STDERR, "FALHA: a F1 nao carregou; sem ela nao ha tamanho a medir.\n" );
	exit( 1 );
}

/* A chave inventada que o saneamento tem obrigação de recusar. */
$INVENTADO = 'tamanho_que_nao_existe_no_vocabulario';

/**
 * Põe a chave em $_GET, deixa a ferramenta sanear, e devolve o que sobrou.
 */
function cdm_tamanho_sanear( $chave ) {
	$_GET = array( 'pastilha' => $chave );
	$e    = cdm_f1_entrada();
	$_GET = array();

	return array( $e['tamanho'], $e['lado_mm'] );
}

$declarados = cdm_f1_pastilhas_disponiveis();
$erros      = array();
$tamanhos   = array();
$afirmacoes = 0;

foreach ( $declarados as $chave => $dados ) {
	list( $sobreviveu, $lado_mm ) = cdm_tamanho_sanear( $chave );
	$afirmacoes++;
	if ( $sobreviveu !== $chave ) {
		$erros[] = sprintf(
			'a tela lista "%s" e o saneamento o troca por "%s": tamanho que a ferramenta nao aceita',
			$chave,
			$sobreviveu
		);
		continue;
	}
	/* O irregular não tem lado: quem o escolhe digita o lado médio, e `lado_mm`
	   passa a vir do campo `ladoeq`. Por isso ele entra com lado null — e é o
	   único que pode. */
	$lado_cm = ( null === $dados['lado_mm'] ) ? null : $dados['lado_mm'] / 10.0;
	$tamanhos[] = array(
		'chave'   => $chave,
		'rotulo'  => $dados['rotulo'],
		'lado_cm' => $lado_cm,
	);
}

/* A borda: o inventado tem que cair no padrão, e o padrão tem que ser um dos
   declarados — senão a ferramenta atende uma consulta fora da própria faixa. */
list( $caiu_em, ) = cdm_tamanho_sanear( $INVENTADO );
$afirmacoes += 2;
if ( $caiu_em === $INVENTADO ) {
	$erros[] = 'o saneamento aceitou uma chave inventada: nao existe faixa';
} elseif ( ! isset( $declarados[ $caiu_em ] ) ) {
	$erros[] = sprintf( 'o padrao do saneamento e "%s", que a tela nao lista', $caiu_em );
}

/* Sem lado nenhum não há eixo de escolha, e o relatório de cobertura ficaria
   medindo o vazio com cara de medição. */
$com_lado = 0;
foreach ( $tamanhos as $t ) {
	if ( null !== $t['lado_cm'] ) {
		$com_lado++;
	}
}
$afirmacoes++;
if ( $com_lado < 1 ) {
	$erros[] = 'nenhum tamanho declara lado: nao ha eixo pelo qual a F1 escolha pastilha';
}

if ( $erros ) {
	foreach ( $erros as $e ) {
		fwrite( STDERR, "FALHA: $e\n" );
	}
	exit( 1 );
}

if ( $humano ) {
	echo "Tamanhos de pastilha que a F1 serve, medidos no snippet:\n";
	foreach ( $tamanhos as $t ) {
		printf(
			"  %-10s %-46s %s\n",
			$t['chave'],
			$t['rotulo'],
			null === $t['lado_cm'] ? 'sem lado declarado' : sprintf( '%s cm', $t['lado_cm'] )
		);
	}
	printf( "  %d tamanhos, %d com lado, %d afirmacoes.\n", count( $tamanhos ), $com_lado, $afirmacoes );
	exit( 0 );
}

echo wp_json_encode(
	array(
		'medido_em'  => 'ferramentas/tamanhos-da-f1.php',
		'medido_de'  => 'cdm_f1_pastilhas_disponiveis() + cdm_f1_entrada(), por provocacao',
		'tamanhos'   => $tamanhos,
		'afirmacoes' => $afirmacoes,
	)
), "\n";
