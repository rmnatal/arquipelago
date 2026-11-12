<?php
/**
 * AS GUARDAS DO ÚNICO CÓDIGO DESTA ILHA QUE APAGA ARQUIVO.
 *
 *   php ferramentas/teste-purga-cache.php .
 *
 * `rodametria_casca_esvaziar_pasta()` existe porque o gancho de purga do
 * hospedeiro pode mudar de nome entre versões, e gancho que ninguém escuta falha
 * em silêncio. O preço de não depender do nome do gancho é uma recursão que
 * chama `unlink()` e `rmdir()` — e a robometria e a clubedomosaico publicaram
 * essa mesma função **sem portão nenhum**, e esta ilha não a publicou até ter
 * este arquivo. Guarda que ninguém mede é guarda que
 * sobrevive até a primeira pessoa que mexer na recursão.
 *
 * ESTE ARQUIVO CHEGOU AQUI JUNTO COM A FUNÇÃO, EM 03/11/2026, e essa é a
 * condição que o despacho escreveu: a purga desta ilha não entrava sem os dois
 * portões da aquametria do lado. A ilha ficou sete dias no ar sem purga de
 * propósito — a seção 12 da casca registrou a falta em vez de escondê-la — e
 * portar a função de carona, no fim do bloco que mexeu na porta de entrada, é
 * exatamente como a armadilha abaixo entrou no Arquipélago.
 *
 * O PORTÃO SE PAGOU NO PRIMEIRO MINUTO DE VIDA NA AQUAMETRIA, e o caso 5 abaixo
 * é o acidente virado afirmação. `realpath('')` **não** devolve `false` em PHP:
 * devolve o diretório de trabalho atual. Com caminho e raiz vazios, a guarda de
 * contenção comparava o diretório atual consigo mesmo, aprovava, e a recursão
 * esvaziava a pasta de onde o teste estava sendo rodado — a pasta da ilha, 117
 * arquivos, recuperados com `git checkout` porque o repositório é o lugar do
 * trabalho (seção 3). A casca ganhou uma linha que recusa o vazio antes da
 * comparação; o caso 5 é o que impede essa linha de ser retirada por parecer
 * redundante.
 *
 * O QUE ESTE TESTE NÃO É: ele não prova que a purga esvazia o cache do
 * hospedeiro. Isso só se mede no ar, e quem mede é
 * `ferramentas/conferir-no-ar.py`. Aqui se mede a outra metade, a que o
 * ar nunca mostraria: que a função, quando levada para fora da pasta dela por um
 * link simbólico, por um `..`, por uma raiz inexistente ou por um caminho vazio,
 * **para**.
 *
 * As armadilhas são construídas em disco de verdade, numa pasta temporária, e
 * cada uma tem uma TESTEMUNHA do lado de fora: um arquivo que não pode
 * desaparecer. Afirmação sobre o que foi apagado é metade da prova; a que
 * importa é a afirmação sobre o que CONTINUA LÁ.
 */
$raiz = isset( $argv[1] ) ? rtrim( $argv[1], '/' ) : '.';
$raiz = realpath( $raiz );
if ( ! $raiz ) {
	fwrite( STDERR, "FALHA: raiz da ilha não encontrada.\n" );
	exit( 1 );
}

/* O snippet inteiro pede meio WordPress; só a seção 13 interessa.
 *
 * O DIA QUE A VERSÃO ANTERIOR DESTE COMENTÁRIO PREVIU CHEGOU, EM 12/11/2026.
 * Ele dizia: *"nesta ilha a seção 13 vai até o fim do arquivo (...) se um dia
 * nascer uma seção 14 depois dela, este corte passa a arrastar código que não é
 * desta medição — e a afirmação de FRONTEIRA logo abaixo é o que denuncia isso
 * em vez de deixar passar"*. Nasceu a **seção 14** (a cura da porta, exceção
 * nomeada da 29.4), e a afirmação de fronteira **denunciou na primeira
 * passada** — `FALHA: nasceu código depois da seção 13; este corte virou
 * mentira`, em `teste-purga-cache.php` e nas oito baterias de
 * `mutacoes-purga-cache.py`, as oito reprovando "pelo motivo ERRADO", que é o
 * aviso de que o instrumento parou antes de medir.
 *
 * ENTÃO O CORTE PASSA A SER ENTRE DOIS MARCADORES, como na aquametria — e a
 * fronteira continua AFIRMADA, agora sobre o novo vizinho de baixo: entre o
 * gatilho da purga e a primeira linha da seção 14 não pode nascer função
 * nenhuma. Previsão escrita que, no dia, apontou o arquivo e a linha vale mais
 * que portão que não quebra: este não deixou passar, parou e disse o nome. */
$src = file_get_contents( $raiz . '/snippets/rodametria-casca.php' );
$ini = strpos( $src, "if ( ! function_exists( 'rodametria_casca_purgar_cache' ) ) {" );
if ( false === $ini ) {
	fwrite( STDERR, "FALHA: a seção 13 da casca não foi encontrada no snippet.\n" );
	exit( 1 );
}
/* O vizinho de baixo é a seção 14. Ausente, o corte vai até o fim do arquivo —
   que é o mundo de antes de 12/11/2026 e continua sendo um mundo válido. */
$ini14 = strpos( $src, "if ( ! defined( 'RODAMETRIA_CASCA_CURA_INTERVALO' ) ) {" );
$fim   = ( false === $ini14 ) ? strlen( $src ) : $ini14;

/* A FRONTEIRA É AFIRMADA, NÃO SUPOSTA, e agora ela mede o espaço ENTRE as duas
   seções: o gatilho da purga é a última linha de código da 13, e a primeira da
   14 é o `define` acima. Função nascida nesse vão não é desta medição e não
   pode entrar no `eval` caladamente. */
$gatilho = strpos( $src, "add_action( 'added_option', 'rodametria_casca_purgar_ao_gravar', 10, 1 );" );
$vao     = substr( $src, $gatilho, $fim - $gatilho );
if ( 1 === preg_match( '/^\s*function\s+\w+\s*\(/m', $vao ) ) {
	fwrite( STDERR, "FALHA: nasceu função entre o gatilho da seção 13 e a seção 14; este corte virou mentira.\n" );
	exit( 1 );
}

$ganchos = array();
$funcoes = array();
function do_action( $h ) { global $ganchos; $ganchos[] = $h; }
function add_action( $h, $f, $p = 10, $a = 1 ) { global $funcoes; $funcoes[] = $h . ':' . $f; }
function wp_cache_clear_cache() {}

eval( substr( $src, $ini, $fim - $ini ) );

$falhas = 0; $casos = 0;
function afirmar( $cond, $rotulo, $detalhe = '' ) {
	global $falhas, $casos;
	$casos++;
	if ( ! $cond ) {
		$falhas++;
		echo "  FALHA  $rotulo" . ( '' !== $detalhe ? "  ($detalhe)" : '' ) . "\n";
	}
}

$tmp = sys_get_temp_dir() . '/rdm-purga-' . getmypid();

/**
 * Monta, do zero, o mundo de cada caso: uma raiz de cache com arquivo e
 * subpasta, e uma pasta VIZINHA com a testemunha que não pode ser tocada.
 */
function montar( $tmp ) {
	apagar_tudo( $tmp );
	mkdir( $tmp . '/cache/sub', 0777, true );
	mkdir( $tmp . '/fora', 0777, true );
	file_put_contents( $tmp . '/cache/pagina.html', 'cacheada' );
	file_put_contents( $tmp . '/cache/sub/outra.html', 'cacheada' );
	file_put_contents( $tmp . '/fora/testemunha.txt', 'NAO PODE SUMIR' );
}

function apagar_tudo( $caminho ) {
	if ( is_link( $caminho ) || is_file( $caminho ) ) { @unlink( $caminho ); return; }
	if ( ! is_dir( $caminho ) ) { return; }
	foreach ( array_diff( scandir( $caminho ), array( '.', '..' ) ) as $i ) {
		apagar_tudo( $caminho . '/' . $i );
	}
	@rmdir( $caminho );
}

echo "pasta de trabalho: $tmp\n";

/* ------------------------------------------------------------------ *
 * 1. O CAMINHO FELIZ. Sem ele as outras afirmações seriam satisfeitas
 *    por uma função que não faz nada — a forma mais fácil de passar num
 *    teste de guarda é não ter o que guardar.
 * ------------------------------------------------------------------ */
echo "\n1. ESVAZIA A PASTA DE CACHE (e não some com ela)\n";
montar( $tmp );
rodametria_casca_esvaziar_pasta( $tmp . '/cache', $tmp . '/cache' );
afirmar( ! file_exists( $tmp . '/cache/pagina.html' ), 'o arquivo de cache foi apagado' );
afirmar( ! file_exists( $tmp . '/cache/sub' ), 'a subpasta foi apagada' );
afirmar( is_dir( $tmp . '/cache' ), 'a RAIZ continua de pé — o plugin a recria, e sumir com ela não é direito desta ilha' );
afirmar( file_exists( $tmp . '/fora/testemunha.txt' ), 'a testemunha de fora continua lá' );

/* ------------------------------------------------------------------ *
 * 2. LINK SIMBÓLICO NÃO É SEGUIDO. Apagar o link é seguro; apagar o que
 *    ele aponta é sair da pasta sem perceber. Este é o caso que uma
 *    hospedagem compartilhada torna plausível de verdade.
 * ------------------------------------------------------------------ */
echo "\n2. LINK SIMBÓLICO PARA FORA: apaga o LINK, nunca o alvo\n";
montar( $tmp );
$ok_link = @symlink( $tmp . '/fora', $tmp . '/cache/atalho' );
if ( ! $ok_link ) {
	echo "  (este sistema não deixa criar link simbólico; caso pulado — e isso é dito, não escondido)\n";
} else {
	rodametria_casca_esvaziar_pasta( $tmp . '/cache', $tmp . '/cache' );
	afirmar( ! is_link( $tmp . '/cache/atalho' ), 'o link em si foi apagado' );
	afirmar( is_dir( $tmp . '/fora' ), 'a pasta apontada pelo link CONTINUA LÁ' );
	afirmar( file_exists( $tmp . '/fora/testemunha.txt' ), 'a testemunha dentro dela continua lá' );
}

/* ------------------------------------------------------------------ *
 * 3. A PASTA PEDIDA ESTÁ FORA DA RAIZ. É a guarda que a recursão usa a
 *    cada nível: o caminho REAL tem de começar pelo caminho REAL da raiz.
 * ------------------------------------------------------------------ */
echo "\n3. PASTA FORA DA RAIZ: a função PARA\n";
montar( $tmp );
rodametria_casca_esvaziar_pasta( $tmp . '/fora', $tmp . '/cache' );
afirmar( file_exists( $tmp . '/fora/testemunha.txt' ), 'pasta irmã não é esvaziada' );

montar( $tmp );
rodametria_casca_esvaziar_pasta( $tmp . '/cache/../fora', $tmp . '/cache' );
afirmar( file_exists( $tmp . '/fora/testemunha.txt' ), 'o ".." não atravessa a raiz' );

montar( $tmp );
rodametria_casca_esvaziar_pasta( $tmp, $tmp . '/cache' );
afirmar( file_exists( $tmp . '/fora/testemunha.txt' ), 'a PAI da raiz não é esvaziada' );
afirmar( file_exists( $tmp . '/cache/pagina.html' ), 'e nada dentro da raiz foi apagado de passagem' );

/* O prefixo comum não basta: uma pasta cujo nome COMEÇA pelo da raiz é
   outra pasta. A guarda compara com a barra no fim, e é isto que mede a
   diferença. */
montar( $tmp );
mkdir( $tmp . '/cachedeoutro', 0777, true );
file_put_contents( $tmp . '/cachedeoutro/testemunha.txt', 'NAO PODE SUMIR' );
rodametria_casca_esvaziar_pasta( $tmp . '/cachedeoutro', $tmp . '/cache' );
afirmar( file_exists( $tmp . '/cachedeoutro/testemunha.txt' ),
	'pasta cujo nome COMEÇA pelo da raiz não é a raiz' );

/* ------------------------------------------------------------------ *
 * 4. RAIZ QUE NÃO EXISTE. `realpath()` devolve false, e false comparado
 *    com string casaria por acidente se a guarda fosse escrita ao
 *    contrário. Aqui ela tem de PARAR.
 * ------------------------------------------------------------------ */
echo "\n4. RAIZ INEXISTENTE: a função PARA\n";
montar( $tmp );
rodametria_casca_esvaziar_pasta( $tmp . '/cache', $tmp . '/nao-existe' );
afirmar( file_exists( $tmp . '/cache/pagina.html' ), 'raiz inexistente não autoriza nada' );

/* ------------------------------------------------------------------ *
 * 5. O CAMINHO VAZIO — o acidente de 15/09/2026, virado afirmação.
 *
 *    `realpath('')` devolve o DIRETÓRIO DE TRABALHO ATUAL, não `false`.
 *    Sem a recusa explícita do vazio, a guarda compara o diretório atual
 *    consigo mesmo, aprova, e a recursão esvazia de onde o processo está
 *    rodando. Foi assim que este teste apagou a pasta da ilha.
 *
 *    A armadilha é reproduzida DE PROPÓSITO e num lugar sacrificável: o
 *    processo entra numa pasta temporária, com uma testemunha dentro, e
 *    chama a função com vazio nos dois argumentos. Se a linha de recusa
 *    for retirada da casca, a testemunha some e este caso reprova — que é
 *    a única forma de a correção não ser desfeita por parecer redundante.
 * ------------------------------------------------------------------ */
echo "\n5. CAMINHO VAZIO: a função PARA (realpath('') é o diretório atual)\n";
montar( $tmp );
mkdir( $tmp . '/sacrificavel', 0777, true );
file_put_contents( $tmp . '/sacrificavel/testemunha.txt', 'NAO PODE SUMIR' );
$antes = getcwd();
chdir( $tmp . '/sacrificavel' );
rodametria_casca_esvaziar_pasta( '', '' );
rodametria_casca_esvaziar_pasta( '.', '' );
rodametria_casca_esvaziar_pasta( '', '.' );
chdir( $antes );
afirmar( file_exists( $tmp . '/sacrificavel/testemunha.txt' ),
	'caminho vazio NÃO esvazia o diretório de trabalho' );
afirmar( file_exists( $tmp . '/cache/pagina.html' ),
	'e o resto do mundo continua intacto' );

/* ------------------------------------------------------------------ *
 * 6. O GATILHO. A purga escuta a gravação de option, e option de
 *    terceiro não é assunto desta ilha.
 * ------------------------------------------------------------------ */
echo "\n6. O GATILHO SÓ DISPARA NAS OPTIONS DA ILHA\n";
afirmar( in_array( 'updated_option:rodametria_casca_purgar_ao_gravar', $funcoes, true ),
	'a purga está ligada em updated_option' );
afirmar( in_array( 'added_option:rodametria_casca_purgar_ao_gravar', $funcoes, true ),
	'a purga está ligada em added_option' );

$ganchos = array();
rodametria_casca_purgar_ao_gravar( 'algum_plugin_de_terceiro' );
afirmar( array() === $ganchos, 'option de terceiro NÃO dispara a purga',
	implode( ',', $ganchos ) );

$ganchos = array();
rodametria_casca_purgar_ao_gravar( 'rodametria_dados_f2-respostas' );
afirmar( in_array( 'epc_purge', $ganchos, true ), 'option da ilha dispara a purga',
	implode( ',', $ganchos ) );
afirmar( in_array( 'litespeed_purge_all', $ganchos, true ),
	'a lista defensiva inteira é percorrida' );

/* UMA VEZ POR REQUISIÇÃO: uma revisão grava vinte options, e vinte purgas
   seriam vinte varreduras de pasta na mesma requisição do Sync. */
$ganchos = array();
rodametria_casca_purgar_ao_gravar( 'rodametria_casca_instalado' );
rodametria_casca_purgar_ao_gravar( 'rodametria_sync_estado' );
afirmar( array() === $ganchos, 'a purga roda UMA vez por requisição, mesmo com vinte options',
	implode( ',', $ganchos ) );

apagar_tudo( $tmp );

echo "\n" . str_repeat( '=', 70 ) . "\n";
if ( $falhas ) {
	echo "REPROVADO: $casos afirmações, $falhas falha(s).\n";
	exit( 1 );
}
echo "APROVADO: $casos afirmações, 0 falha(s).\n";
exit( 0 );
