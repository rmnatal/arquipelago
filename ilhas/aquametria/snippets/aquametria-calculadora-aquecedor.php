/**
 * Aquametria Calculadora de Potência do Aquecedor — C5
 * Versão: 1.5.0 (10/09/2026) — BLOCO T8: a VITRINE de produto nasce na C5, a
 *   segunda do Arquipélago depois da C3. Carrossel de cartões em scroll-snap de
 *   CSS puro, sem biblioteca, com foto, marca, modelo, a especificação que fez o
 *   produto entrar, a cotação COM A DATA e o botão de loja — e ele vem ANTES da
 *   ficha técnica e da procedência (contrato 7). Duas vitrines por página: a
 *   pintada, dentro do resultado, e uma SERVIDA no HTML para o aquário de
 *   referência de 100 L, porque um crawler de IA não executa JavaScript e
 *   vitrine que só nasce no clique é vitrine que só o comprador que já chegou vê.
 *   O QUE A C5 TEM E A C3 NÃO TINHA: a lista aqui é partida em dois grupos desde
 *   a 1.4.0, e cartão de vitrine não comporta cabeçalho de grupo. Então a
 *   distinção viaja na frase do próprio cartão — "dentro dos 110 a 160 W que os
 *   108 L pedem" contra "degrau comercial acima dos 160 W do topo" —, e a
 *   sequência que a vitrine desenha é a MESMA que a lista técnica desenha,
 *   calculada uma vez só e passada adiante. A ORDEM NÃO MUDA: a vitrine nunca
 *   reordena por foto, por preço ou por comissão.
 *   PREÇO PASSA A SAIR, sempre datado, e as duas frases que diziam "não
 *   publicamos preço" foram reescritas nesta MESMA versão — página que mostra
 *   preço e diz que não publica preço se contradiz, e contradição na cara do
 *   leitor foi o defeito consertado na 1.4.0.
 *   Vieram junto duas dívidas da seção 6 do contrato que esta página ainda tinha:
 *   a linha de promessa antes do formulário e a barra fixa do celular enquanto o
 *   resultado está fora da tela, com rolagem até o resultado ao calcular.
 *   Nenhuma fórmula, constante ou faixa mudou, e a elegibilidade é a mesma.
 * Versão: 1.4.0 (10/09/2026) — o bloco de produto para de se contradizer.
 *   Item 2 do despacho da Sentinela de 10/09/2026: com 108 L, mínima do cômodo
 *   de 16 °C e alvo de 26 °C, a página publicava a faixa de 110 a 160 W e listava
 *   o Atman AT-200 e o Eheim Jäger 200 W sob o título "Aquecedores que atendem
 *   essa potência" — enquanto o texto do próprio cartão dizia que aquele aparelho
 *   entrega 1,85 W/L "contra" os 1,00 a 1,50 que a diferença pede. A Sentinela não
 *   escolhe qual dos dois lados está errado, e a escolha desta versão é: a
 *   ELEGIBILIDADE ESTÁ CERTA e não muda. Aquecedor não se vende em 160 W; o teto
 *   da lista é de propósito o degrau comercial que cobre o topo da faixa, coisa
 *   que a página anuncia duas telas acima ("na prateleira, isso vira um aquecedor
 *   de 200 W"). O que mentia era o RÓTULO. Então: (a) o h3 do bloco deixa de
 *   afirmar "atendem essa potência" sobre a lista inteira; (b) a lista se parte em
 *   dois grupos com cabeçalho e frase próprios — "Dentro da faixa calculada" e "O
 *   degrau comercial acima — N W", este último dizendo por que ele está ali e o
 *   que a sobra de potência significa num aparelho com termostato; (c) a frase do
 *   cartão sem link de loja para de dizer "aparece aqui porque atende ao seu
 *   número" quando o aparelho é o degrau acima; (d) a tabela pré-renderizada — o
 *   lado que o modelo de linguagem lê sem JavaScript — avisa na célula quando o
 *   aparelho escolhido é o degrau acima do topo. A ORDEM NÃO MUDA em nada:
 *   continua sendo a distância até o topo da faixa dentro de cada grupo, e quem
 *   cabe na faixa continua vindo antes. Comissão não ordena nada (regra V16).
 *   Nenhuma fórmula, constante ou faixa mudou.
 * Versão: 1.3.0 (09/09/2026) — BLOCO 4c, fechamento: a tabela pré-renderizada
 *   passou a dizer QUAL aparelho atende cada faixa. Antes ela respondia ao
 *   leitor e não respondia ao comprador: a pessoa só descobria que existe
 *   recomendação depois de preencher o formulário inteiro e rolar até o fim, e
 *   no celular isso é grave. Agora cada uma das seis linhas traz o aquecedor do
 *   banco cuja potência cai mais perto do topo daquela faixa, com a voltagem que
 *   a ficha declara — ou a frase dizendo que ela não está confirmada, porque
 *   voltagem errada queima aparelho e aqui não se chuta 110 nem 220 —, a
 *   procedência e a data na mesma frase, e o link de loja quando existe
 *   (sponsored, noopener, aba nova), com aviso de comissão junto da tabela.
 *   Quando quem atende melhor ainda não tem link, aparece embaixo e rotulada a
 *   opção da MESMA faixa que tem: a ordem continua por adequação técnica, nunca
 *   por comissão (regra V16). As duas barreiras de segurança do formulário
 *   (voltagem da tomada e faixa de ajuste alcançar o alvo, regra V18) NÃO cabem
 *   na tabela, que não conhece nenhum dos dois, e o texto abaixo dela diz isso
 *   com essas palavras. A linha de 300 L avisa que a faixa passa do maior degrau
 *   da linha de referência e que ali a resposta é mais de um aparelho. O FAQPage
 *   ganhou seis perguntas de compra, cada uma respondida com o mesmo modelo e o
 *   mesmo número que a tabela serve. Nenhuma fórmula mudou.
 * Versão: 1.2.0 (09/09/2026) — BLOCO 4c, visibilidade em IA. A página passou a
 *   servir RESPOSTA no HTML, e não só formulário. Três acréscimos e um conserto:
 *   (a) um bloco de resposta direta no topo, com o número, o critério e a
 *   procedência dentro da própria frase, para sobreviver a ser citado fora de
 *   contexto; (b) uma tabela de seis aquários já resolvidos (30, 60, 100, 150,
 *   200 e 300 L), nos dois cenários de diferença de temperatura, pré-renderizada
 *   no HTML pelo PHP — quem lê esta página por HTTP via um formulário vazio e
 *   agora vê watts; (c) JSON-LD schema.org no wp_head, com WebApplication e
 *   FAQPage. O conserto: as regras de W/L e a linha comercial moravam só dentro
 *   do JavaScript, e qualquer texto que as citasse teria de repeti-las à mão;
 *   agora nascem no PHP, que as entrega ao script como AQM_C5_REGRAS e
 *   AQM_C5_LINHA. Nenhuma fórmula mudou.
 * Versão: 1.1.0 (08/09/2026) — CORREÇÃO GRAVE: o JS e o CSS saíram de dentro do retorno do
 *   shortcode e passaram a ser impressos no wp_head (estilo) e no wp_footer (comportamento).
 *   Dentro do retorno do shortcode eles ainda atravessavam os filtros de texto do conteúdo,
 *   que trocam cada "&" pela entidade numérica dele: o primeiro "&&" do script virava um par
 *   navegador parava com SyntaxError e a calculadora inteira ficava morta — o formulário não
 *   calculava, a resposta não aparecia e o bloco de produto com os links de afiliado nunca
 *   saía do estado oculto. Nenhuma linha de cálculo mudou; mudou o lugar onde o script sai.
 * Versão: 1.0.2 (08/09/2026) — o painel de ligações passou a linkar a C15, publicada nesta data.
 * A 1.0.1 linkou a C12, publicada no mesmo dia
 *
 * Terceira calculadora do lote e a primeira que pergunta uma coisa que nenhuma
 * fonte brasileira do nosso levantamento pergunta: quanto frio faz onde o
 * aquário está. Toda a web repete "1 W por litro" sem dizer para qual diferença
 * de temperatura o número vale — e um aquário a 26 °C num quarto que cai a
 * 22 °C não é o mesmo problema que o mesmo aquário num quarto que cai a 12 °C.
 * Este é o vácuo de conteúdo nº 2 do levantamento do Bloco 1.
 *
 * Registra o shortcode [aquametria_calculadora_aquecedor] e se anuncia no hub
 * pelo filtro 'aquametria_calculadoras' da casca.
 *
 * Todo o cálculo é JavaScript no navegador, de propósito: o site está atrás do
 * cache de página da hospedagem, então HTML que dependesse da query string seria
 * servido errado para o visitante seguinte. Nada é enviado a servidor nenhum.
 *
 * O que esta calculadora NÃO faz, e por quê:
 * - Não publica o cálculo físico P = U · A · ΔT. Falta a constante
 *   'u-vidro-aquario' (status pendente): o coeficiente global de troca do vidro
 *   com convecção natural nas duas faces, mais a perda por evaporação na lâmina
 *   livre, que costuma dominar. Sem fonte, não sai. É a via B da especificação,
 *   e vale um bloco próprio — quando sair, esta página deixa de depender de
 *   regra de bolso e passa a ser a única do nicho no Brasil com física atrás.
 * - Não corrige a potência por aquário tampado ou destampado. A perda pela
 *   lâmina livre é justamente a parcela que a constante pendente cobriria.
 *   O campo existe no formulário e muda o TEXTO, nunca o número: dizer "some
 *   20 % se for destampado" seria inventar constante, e aqui isso é proibido.
 * - Não usa temperatura mínima por cidade. A constante
 *   'temperatura-minima-por-cidade' também está pendente (a coleta prevista é a
 *   Normal Climatológica do INMET 1991-2020). Enquanto não houver a tabela, a
 *   mínima é entrada da pessoa, que é quem sabe quanto esfria no cômodo dela.
 * - Não extrapola regra de bolso para ΔT acima de 10 °C. A única fonte do corpus
 *   que amarrou W/L a um delta declarou até 10 °C. Passou disso, a tela diz com
 *   essas palavras que nenhuma fonte cobre o caso.
 *
 * Bloco de produto: os aquecedores vêm do catálogo embutido mais abaixo, gerado
 * por ferramentas/gerar-catalogo-aquecedores.py a partir de
 * dados/produtos-aquecedor.json. Mexeu no banco, rode o gerador. A ordem é por
 * adequação técnica; link de afiliado não ordena nem filtra (regra V16). Duas
 * barreiras de segurança vêm antes de tudo: a voltagem da tomada (aquecedor na
 * voltagem errada queima) e a faixa de ajuste alcançar a temperatura-alvo
 * (regra V18). Preço entra desde a 1.5.0, e entra sempre como COTAÇÃO COM A DATA
 * da coleta ao lado — nunca como preço de hoje, que é o que a seção 7 do contrato
 * proíbe. Quem publica preço é a vitrine; a tabela de exemplos não.
 *
 * Regras herdadas (fase 4b): sem "<?php" no topo (o Code Snippets põe); toda
 * função de nível superior dentro de function_exists; não usa superglobal de
 * servidor; texto de tela acentuado em UTF-8.
 */

if ( ! defined( 'ABSPATH' ) ) {
	return;
}

if ( ! defined( 'AQUAMETRIA_C5_VERSAO' ) ) {
	define( 'AQUAMETRIA_C5_VERSAO', '1.5.0' );
	define( 'AQUAMETRIA_C5_SLUG', 'calculadora-de-potencia-do-aquecedor' );
	define( 'AQUAMETRIA_C5_VERIFICADO_EM', '08/09/2026' );
	define( 'AQUAMETRIA_C5_ARTIGO', 'quantos-watts-de-aquecedor-para-aquario' );
	define( 'AQUAMETRIA_C5_PAGINA_AFILIADOS', 'divulgacao-de-afiliados' );
	/* Constante 'wl-delta-ate-10' (ReefFlow): a ÚNICA do corpus que amarra
	   W/L a uma diferença de temperatura declarada. Vale até 10 °C. */
	define( 'AQUAMETRIA_C5_DELTA_COBERTO', 10 );
}

/* ---------------------------------------------------------------------------
 * 1. Anúncio no hub da casca
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c5_registrar_no_hub' ) ) {
function aquametria_c5_registrar_no_hub( $lista ) {
	if ( ! is_array( $lista ) ) {
		return $lista;
	}
	foreach ( $lista as $i => $c ) {
		if ( isset( $c['codigo'] ) && 'C5' === $c['codigo'] ) {
			$lista[ $i ]['estado'] = 'publicada';
			$lista[ $i ]['slug']   = AQUAMETRIA_C5_SLUG;
		}
	}
	return $lista;
}
}
add_filter( 'aquametria_calculadoras', 'aquametria_c5_registrar_no_hub' );

/* ---------------------------------------------------------------------------
 * 1b. As regras de watts por litro, e a linha comercial — FONTE ÚNICA
 *
 * Até 09/09/2026 estas duas listas moravam dentro do JavaScript, e o PHP não
 * tinha como citá-las sem repetir os números. Repetir número é combinar de
 * divergir depois. Agora nascem aqui: o rodapé as entrega ao script como
 * AQM_C5_REGRAS e AQM_C5_LINHA, e a tabela de exemplos pré-renderizada lê o
 * mesmo array. Cada regra guarda a CONDIÇÃO que o próprio autor declarou —
 * 'sempre' quer dizer que ele não declarou nenhuma, que é exatamente o problema
 * que esta calculadora existe para expor.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c5_regras' ) ) {
function aquametria_c5_regras() {
	return array(
		array(
			'id'     => 'wl-delta-ate-10',
			'wl'     => array( 1, 1.5 ),
			'quando' => 'delta',
			'fonte'  => 'ReefFlow',
			'rotulo' => 'Regra com delta declarado',
			'nota'   => 'A única fonte do nosso levantamento que amarra watts por litro a uma diferença de temperatura: de 1,0 a 1,5 W/L para até 10 °C de diferença entre o ambiente e a água.',
		),
		array(
			'id'     => 'wl-sul',
			'wl'     => array( 2, 2 ),
			'quando' => 'sul',
			'fonte'  => 'Casa da Ada',
			'rotulo' => 'Leitura do Sul',
			'nota'   => 'Até 2,0 W/L para a região Sul. É a única fonte do corpus que reconhece que o Brasil não tem um clima só — mas ela também não diz para qual diferença de temperatura o número vale.',
		),
		array(
			'id'     => 'wl-generico',
			'wl'     => array( 1, 1 ),
			'quando' => 'sempre',
			'fonte'  => 'repetida sem autoria única na web BR',
			'rotulo' => 'Regra genérica',
			'nota'   => '1 W por litro. É o número que quase toda página brasileira publica, sem autor identificável e sem dizer para qual diferença de temperatura vale.',
		),
		array(
			'id'     => 'wl-ehow',
			'wl'     => array( 1.3, 1.3 ),
			'quando' => 'sempre',
			'fonte'  => 'eHow',
			'rotulo' => 'Variante da regra genérica',
			'nota'   => '1,3 W por litro, também sem condição declarada. Está aqui porque discorda do 1,0 W/L — e a discordância é o conteúdo.',
		),
	);
}
}

/* Constante 'eheim-jager-linha-comercial': os 9 tamanhos da linha. Aquecedor não
   se vende em qualquer potência; a escolha real é entre estes degraus. */
if ( ! function_exists( 'aquametria_c5_linha_comercial' ) ) {
function aquametria_c5_linha_comercial() {
	return array( 25, 50, 75, 100, 125, 150, 200, 250, 300 );
}
}

/* ---------------------------------------------------------------------------
 * 1c. Os seis aquários resolvidos no servidor
 *
 * O motivo, escrito em 09/09/2026: todo o cálculo desta página é JavaScript no
 * navegador, de propósito (o site está atrás de cache de página). A consequência
 * que ninguém tinha medido é que um modelo de linguagem — ou o leitor que não
 * preenche formulário — recebia um formulário VAZIO e ia embora sem um watt
 * sequer. As funções abaixo resolvem seis volumes no PHP, com as MESMAS regras
 * do script, e o resultado sai no HTML servido. É o mesmo cálculo, feito antes.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c5_volumes_exemplo' ) ) {
function aquametria_c5_volumes_exemplo() {
	return array( 30, 60, 100, 150, 200, 300 );
}
}

/* Espelho em PHP do watts() do script: watts é número grosso numa conta que vem
   de regra de bolso, então arredonda para 5 W. Os dois têm de devolver a mesma
   string, senão a tabela servida contradiz a calculadora logo acima dela. */
if ( ! function_exists( 'aquametria_c5_watts' ) ) {
function aquametria_c5_watts( $n ) {
	return number_format_i18n( round( $n / 5 ) * 5, 0 );
}
}

/* Resolve um volume para um cenário. $delta_coberto diz se a diferença entre o
   cômodo e a água está dentro dos 10 °C que a ReefFlow declarou; $sul diz se a
   leitura da região Sul entra. Fora isso, sobram as regras genéricas — que é o
   que acontece acima de 10 °C, e a tela precisa dizer isso com essas palavras. */
if ( ! function_exists( 'aquametria_c5_exemplo' ) ) {
function aquametria_c5_exemplo( $volume, $delta_coberto = true, $sul = false ) {
	$aplicaveis = array();
	foreach ( aquametria_c5_regras() as $g ) {
		$vale = ( 'sempre' === $g['quando'] )
			|| ( 'delta' === $g['quando'] && $delta_coberto )
			|| ( 'sul' === $g['quando'] && $sul );
		if ( $vale ) {
			$aplicaveis[] = $g;
		}
	}

	$piso = null;
	$teto = null;
	foreach ( $aplicaveis as $g ) {
		$min = $volume * $g['wl'][0];
		$max = $volume * $g['wl'][1];
		$piso = ( null === $piso ) ? $min : min( $piso, $min );
		$teto = ( null === $teto ) ? $max : max( $teto, $max );
	}

	$comercial = null;
	foreach ( aquametria_c5_linha_comercial() as $w ) {
		if ( $w >= $teto ) {
			$comercial = $w;
			break;
		}
	}

	return array(
		'volume'     => $volume,
		'piso'       => $piso,
		'teto'       => $teto,
		'wl_piso'    => $piso / $volume,
		'wl_teto'    => $teto / $volume,
		'comercial'  => $comercial,
		'aplicaveis' => $aplicaveis,
	);
}
}

/* O degrau comercial em texto — ou a frase que diz que a faixa passou do maior
   degrau da linha de referência, que é o que acontece a partir de 300 L. */
if ( ! function_exists( 'aquametria_c5_comercial_texto' ) ) {
function aquametria_c5_comercial_texto( $e ) {
	$linha = aquametria_c5_linha_comercial();
	if ( $e['comercial'] ) {
		return number_format_i18n( $e['comercial'], 0 ) . ' W';
	}
	return 'acima dos ' . number_format_i18n( $linha[ count( $linha ) - 1 ], 0 ) . ' W da linha, mais de um aparelho';
}
}

/* ---------------------------------------------------------------------------
 * 1d. O aquecedor do banco que atende cada linha da tabela
 *
 * Pedido do Raphael em 09/09/2026: a tabela pré-renderizada precisa dizer, em
 * cada faixa, QUAL aparelho atende — senão ela responde ao leitor e não responde
 * ao comprador, e a pessoa só descobre que existe recomendação depois de
 * preencher o formulário inteiro e rolar até o fim.
 *
 * O critério é o MESMO do script (função escolher()): potência dentro da faixa,
 * com teto no degrau comercial quando existe, e ordem pela distância até o topo
 * da faixa, que é onde a convenção editorial manda mirar. Comissão não ordena
 * nada (regra V16 do esquema do banco).
 *
 * DUAS BARREIRAS DE SEGURANÇA DO SCRIPT NÃO CABEM AQUI, e isso não é descuido:
 * a tabela não sabe a voltagem da tomada de quem lê nem a temperatura-alvo, que
 * são exatamente os dois cortes que o formulário aplica (regra V18). Aquecedor
 * ligado na voltagem errada queima, então a célula publica a voltagem que a
 * ficha declara — e diz quando ela não está confirmada — e o texto abaixo da
 * tabela avisa que a lista definitiva sai depois do cálculo.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c5_produtos_exemplo' ) ) {
function aquametria_c5_produtos_exemplo( $e ) {
	$teto_corte = $e['comercial'] ? $e['comercial'] : $e['teto'];
	$dentro     = array();

	foreach ( aquametria_c5_catalogo() as $p ) {
		if ( $p['potencia_w'] < $e['piso'] || $p['potencia_w'] > $teto_corte ) {
			continue;
		}
		$dentro[] = $p;
	}

	$alvo = $e['teto'];

	usort(
		$dentro,
		function ( $a, $b ) use ( $alvo ) {
			$da = abs( $a['potencia_w'] - $alvo );
			$db = abs( $b['potencia_w'] - $alvo );
			if ( abs( $da - $db ) < 0.001 ) {
				return strcmp( $a['id'], $b['id'] );
			}
			return ( $da < $db ) ? -1 : 1;
		}
	);

	return $dentro;
}
}

if ( ! function_exists( 'aquametria_c5_produto_exemplo' ) ) {
function aquametria_c5_produto_exemplo( $e ) {
	$lista = aquametria_c5_produtos_exemplo( $e );
	return $lista ? $lista[0] : null;
}
}

/* O primeiro da MESMA ordem que já tem link de loja hoje. Existe porque o modelo
   que atende melhor costuma ser um que o banco ainda não conseguiu link, e aí a
   pessoa fica sem saber onde comprar nenhum. A ordem não muda por isso: quem
   atende melhor continua em primeiro, e o comprável sai embaixo e rotulado. */
if ( ! function_exists( 'aquametria_c5_produto_com_link' ) ) {
function aquametria_c5_produto_com_link( $e ) {
	foreach ( aquametria_c5_produtos_exemplo( $e ) as $p ) {
		if ( $p['link'] ) {
			return $p;
		}
	}
	return null;
}
}

/* Espelho em PHP do dataBr() do script, feito por partes de propósito: converter
   com strtotime traria o fuso do servidor para dentro de uma data que é só um
   rótulo de coleta, e um dia a mais aqui viraria contradição entre a tabela
   servida e o cartão que o script pinta logo abaixo dela. */
if ( ! function_exists( 'aquametria_c5_data_br' ) ) {
function aquametria_c5_data_br( $iso ) {
	if ( ! $iso || ! preg_match( '/^(\d{4})-(\d{2})-(\d{2})$/', $iso, $m ) ) {
		return (string) $iso;
	}
	return $m[3] . '/' . $m[2] . '/' . $m[1];
}
}

/* O vocabulário de fonte_status vira frase: "ficha do transcrita-varejo" não é
   português, e esta é a frase que um modelo de linguagem recorta e leva. */
if ( ! function_exists( 'aquametria_c5_origem_texto' ) ) {
function aquametria_c5_origem_texto( $status ) {
	if ( 'fabricante-via-busca' === $status ) {
		return 'ficha do fabricante';
	}
	if ( 'transcrita-varejo' === $status ) {
		return 'ficha transcrita de varejo especializado';
	}
	return 'ficha de origem ' . $status;
}
}

/* Só o NOME de quem publicou a ficha, do começo de fonte_ref: o resto do campo é
   descrição longa e vem do banco sem acento, porque é chave de dado e não texto
   de tela. */
if ( ! function_exists( 'aquametria_c5_fonte_nome' ) ) {
function aquametria_c5_fonte_nome( $ref ) {
	$corte = strlen( $ref );

	foreach ( array( ',', ' (' ) as $marca ) {
		$pos = strpos( $ref, $marca );
		if ( false !== $pos && $pos < $corte ) {
			$corte = $pos;
		}
	}

	$nome = trim( substr( $ref, 0, $corte ) );
	return '' === $nome ? $ref : $nome;
}
}

/* A voltagem em texto. Ela é o campo que mais falta no banco (nove aquecedores
   do lote de 09/09/2026 estão com voltagem null, e nenhuma fonte de varejo
   confirma versão por versão), e é o campo que queima aparelho quando está
   errado — então a falta aparece escrita, nunca como 110 chutado. */
if ( ! function_exists( 'aquametria_c5_voltagem_texto' ) ) {
function aquametria_c5_voltagem_texto( $p ) {
	if ( empty( $p['voltagem'] ) ) {
		return 'voltagem não confirmada pelas fontes';
	}
	return implode( ' ou ', $p['voltagem'] ) . ' V';
}
}

/* A frase do aparelho: modelo, a especificação QUE FEZ ELE ENTRAR, a voltagem e
   a procedência, tudo na mesma frase — o formato que sobrevive a ser recortado
   por um modelo de linguagem e que um comprador consegue ler de uma vez. */
if ( ! function_exists( 'aquametria_c5_produto_frase' ) ) {
function aquametria_c5_produto_frase( $p, $volume ) {
	return $p['marca'] . ' ' . $p['modelo'] . ' — ' . number_format_i18n( $p['potencia_w'], 0 ) . ' W, '
		. aquametria_c5_voltagem_texto( $p ) . ', para os ' . number_format_i18n( $volume, 0 ) . ' litros, segundo '
		. aquametria_c5_origem_texto( $p['fonte_status'] ) . ' (fonte: ' . aquametria_c5_fonte_nome( $p['fonte_ref'] )
		. '), conferida em ' . aquametria_c5_data_br( $p['verificado_em'] );
}
}

/* O aquecedor entra pela POTÊNCIA, e o volume que a ficha declara é outro número
   — às vezes menor que o do exemplo. O cartão que o script pinta já diz isso; a
   tabela servida e o FAQ precisam dizer também, senão a mesma página afirma duas
   coisas diferentes conforme o leitor execute ou não JavaScript. */
if ( ! function_exists( 'aquametria_c5_volume_ressalva' ) ) {
function aquametria_c5_volume_ressalva( $p, $volume ) {
	if ( null === $p['volume_max_L'] || $p['volume_max_L'] >= $volume ) {
		return '';
	}

	return 'A ficha declara esse modelo para até ' . number_format_i18n( $p['volume_max_L'], 0 )
		. ' litros, abaixo dos ' . number_format_i18n( $volume, 0 )
		. ' deste exemplo: ele entra pela potência, e a declaração de volume não cobre esse caso.';
}
}

if ( ! function_exists( 'aquametria_c5_produto_celula_html' ) ) {
function aquametria_c5_produto_celula_html( $e ) {
	$p = aquametria_c5_produto_exemplo( $e );

	/* Bloco vazio nunca sai mudo: silêncio na tela parece defeito, e o leitor
	   não tem como saber se faltou aparelho ou se quebrou a página. */
	if ( null === $p ) {
		return '<td><span class="aqm-c5-sem">Nenhum aquecedor do banco fica entre '
			. esc_html( aquametria_c5_watts( $e['piso'] ) ) . ' e '
			. esc_html( aquametria_c5_watts( $e['comercial'] ? $e['comercial'] : $e['teto'] ) )
			. ' W. Assim que houver um com ficha completa, ele aparece aqui.</span></td>';
	}

	$nome = $p['marca'] . ' ' . $p['modelo'];

	$h = '<td>';

	/* Acima de 300 L a faixa passa do maior degrau da linha de referência, e a
	   resposta da própria página é MAIS DE UM APARELHO. Indicar um modelo só
	   nessa linha sem dizer isso contradiria a coluna ao lado — e um aquecedor
	   subdimensionado trabalha ininterrupto, que é o pior modo de falha. */
	if ( ! $e['comercial'] ) {
		$h .= '<span class="aqm-c5-sem">A faixa passa do maior degrau da linha de referência: aqui a resposta é mais de um aparelho, e o modelo abaixo é um deles.</span>';
	}

	/* A tabela escolhe o modelo mais próximo do TOPO da faixa, e às vezes o mais
	   próximo é o degrau comercial ACIMA dela — não há aquecedor de 160 W na
	   prateleira. Quando isso acontece, a célula diz. Sem esta linha, a tabela
	   servida no HTML (que é o que um modelo de linguagem lê, e que ele cita fora
	   de contexto) afirmaria que o aparelho atende a faixa quando ele a excede.
	   Item 2 do despacho da Sentinela de 10/09/2026, pelo lado sem JavaScript. */
	if ( $p['potencia_w'] > $e['teto'] ) {
		$h .= '<span class="aqm-c5-sem">Este é o degrau comercial acima da faixa: o topo dela é '
			. esc_html( aquametria_c5_watts( $e['teto'] ) ) . ' W e a prateleira não tem esse número.</span>';
	}

	if ( $p['link'] ) {
		$h .= '<a class="aqm-c5-prod" href="' . esc_url( $p['link'] ) . '" target="_blank" rel="sponsored noopener">'
			. esc_html( $nome ) . '</a>';
	} else {
		$h .= '<span class="aqm-c5-prod">' . esc_html( $nome ) . '</span>';
	}

	$h .= '<span class="aqm-c5-wl">' . esc_html( number_format_i18n( $p['potencia_w'], 0 ) ) . ' W — '
		. esc_html( aquametria_c5_voltagem_texto( $p ) ) . '</span>';

	$ressalva = aquametria_c5_volume_ressalva( $p, $e['volume'] );

	if ( '' !== $ressalva ) {
		$h .= '<span class="aqm-c5-sem">' . esc_html( $ressalva ) . '</span>';
	}

	if ( $p['link'] ) {
		$h .= '<span class="aqm-c5-wl">link patrocinado</span>';
		$h .= '</td>';
		return $h;
	}

	$h .= '<span class="aqm-c5-wl">ainda sem link de loja</span>';

	$c = aquametria_c5_produto_com_link( $e );

	if ( null === $c ) {
		$h .= '<span class="aqm-c5-sem">Nenhum aquecedor dessa faixa tem link de loja no banco hoje.</span>';
		$h .= '</td>';
		return $h;
	}

	$h .= '<span class="aqm-c5-sem">Com link hoje, na mesma faixa: <a class="aqm-c5-prod" href="'
		. esc_url( $c['link'] ) . '" target="_blank" rel="sponsored noopener">' . esc_html( $c['marca'] . ' ' . $c['modelo'] )
		. '</a> — ' . esc_html( number_format_i18n( $c['potencia_w'], 0 ) ) . ' W, '
		. esc_html( aquametria_c5_voltagem_texto( $c ) ) . '. Link patrocinado. '
		. esc_html( aquametria_c5_volume_ressalva( $c, $e['volume'] ) ) . '</span>';

	$h .= '</td>';

	return $h;
}
}

/* ---------------------------------------------------------------------------
 * 1e. A VITRINE — bloco T8, 10/09/2026
 *
 * Copiada do desenho da C3, e não reinventada: uma função de cartão em PHP e o
 * espelho dela em JavaScript, com a MESMA marcação, porque duas marcações para o
 * mesmo cartão viram dois CSS e, mais cedo do que se pensa, duas aparências.
 * Duas vitrines por página — a pintada, dentro do resultado, e a SERVIDA no HTML
 * para o aquário de referência, porque crawler de IA não executa JavaScript.
 * A vitrine vem ANTES da ficha e da procedência (contrato 7), e NUNCA reordena:
 * desenha a mesma sequência que a lista técnica.
 *
 * O QUE É DIFERENTE AQUI, e é a razão de este arquivo não poder copiar a C3 de
 * olhos fechados: a lista da C5 tem DOIS GRUPOS desde a 1.4.0 — quem cabe dentro
 * da faixa calculada e o degrau comercial acima dela. Um cartão de vitrine é
 * pequeno demais para carregar cabeçalho de grupo, e enfiar cabeçalho dentro de
 * um trilho horizontal quebraria o scroll-snap. Então a distinção viaja no
 * próprio cartão, na frase da especificação: quem cabe na faixa diz "dentro dos
 * 110 a 160 W que os 108 L pedem", e o degrau acima diz "degrau comercial acima
 * dos 160 W do topo". Repetir no cartão bonito a frase "atende ao seu número"
 * para um aparelho que a linha ao lado declara fora da faixa seria reencenar,
 * em foto e botão de loja, exatamente a contradição que o item 2 do despacho da
 * Sentinela mandou consertar nesta mesma semana.
 *
 * PREÇO PASSA A SAIR, e sai DATADO. Até a 1.4.0 esta página dizia, duas vezes,
 * que não publicava preço. A razão era boa — preço muda toda semana — mas
 * resolvia o problema errado: o proibido pela seção 7 do contrato é preço
 * CRAVADO COMO ATUAL. Cotação com a data ao lado é permitida, e é o que a seção
 * 6 pede da vitrine. As duas frases foram reescritas nesta mesma versão: página
 * que mostra preço e diz que não publica preço se contradiz.
 *
 * Não há Product/Offer no JSON-LD desta página, e é de propósito: Offer.price
 * afirma preço ATUAL, e o que temos é cotação de uma data. Declarar schema de
 * oferta com número velho seria mentir em formato de máquina, que é pior do que
 * mentir em texto, porque ninguém revisa.
 * ------------------------------------------------------------------------- */

/* Espelho em PHP do litros() do script. Existe por um motivo só: o script
   escreve "60,0" abaixo de 100 L e "100" acima, e a vitrine servida precisa
   dizer a mesma coisa que a pintada quando um dia o aquário de referência for
   menor que 100 L. Repetir number_format_i18n aqui seria combinar de divergir. */
if ( ! function_exists( 'aquametria_c5_litros' ) ) {
function aquametria_c5_litros( $n ) {
	if ( null === $n ) {
		return '—';
	}
	return ( $n >= 100 )
		? number_format_i18n( round( $n ), 0 )
		: number_format_i18n( round( $n * 10 ) / 10, 1 );
}
}

/* A cotação vira frase: valor (ou faixa), loja e a data da coleta. Nunca "de
   R$ X por R$ Y", nunca "a partir de" — os dois sugerem promoção e a Aquametria
   não sabe se há promoção. */
if ( ! function_exists( 'aquametria_c5_preco_texto' ) ) {
function aquametria_c5_preco_texto( $p ) {
	if ( empty( $p['preco'] ) || null === $p['preco']['min'] ) {
		return '';
	}

	$pr    = $p['preco'];
	$valor = 'R$ ' . number_format_i18n( $pr['min'], 2 );

	if ( $pr['max'] > $pr['min'] ) {
		$valor = 'R$ ' . number_format_i18n( $pr['min'], 2 ) . ' a R$ ' . number_format_i18n( $pr['max'], 2 );
	}

	$onde = $pr['loja'] ? ' na ' . $pr['loja'] : '';

	return $valor . $onde . ', cotado em ' . aquametria_c5_data_br( $pr['coletado_em'] );
}
}

/* O cartão tem uma linha só para a marca, então a linha do modelo NÃO repete a
   marca. A voltagem entra quando o banco separou o registro por voltagem, senão
   a vitrine mostra dois cartões de nome idêntico. */
if ( ! function_exists( 'aquametria_c5_modelo_curto' ) ) {
function aquametria_c5_modelo_curto( $p ) {
	$modelo = $p['modelo'];

	if ( is_array( $p['voltagem'] ) && 1 === count( $p['voltagem'] ) ) {
		$modelo .= ' (' . $p['voltagem'][0] . ' V)';
	}

	return $modelo;
}
}

/* A especificação QUE FEZ O PRODUTO ENTRAR, no tamanho de um cartão — e ela
   muda conforme o grupo, que é o ponto inteiro desta função. */
if ( ! function_exists( 'aquametria_c5_vt_espec_frase' ) ) {
function aquametria_c5_vt_espec_frase( $p, $e, $acima ) {
	$w = number_format_i18n( $p['potencia_w'], 0 ) . ' W — ';

	if ( $acima ) {
		return $w . 'degrau comercial acima dos ' . aquametria_c5_watts( $e['teto'] ) . ' W do topo';
	}

	return $w . 'dentro dos ' . aquametria_c5_watts( $e['piso'] ) . ' a ' . aquametria_c5_watts( $e['teto'] )
		. ' W que os ' . aquametria_c5_litros( $e['volume'] ) . ' L pedem';
}
}

/* A ressalva de volume declarado, encurtada para caber no cartão. A frase longa
   continua na ficha logo abaixo; o que não pode acontecer é o cartão bonito
   omitir o que a ficha diz — quem só olha a vitrine merece o mesmo aviso. */
if ( ! function_exists( 'aquametria_c5_vt_ressalva_curta' ) ) {
function aquametria_c5_vt_ressalva_curta( $p, $volume ) {
	if ( null === $p['volume_max_L'] || $p['volume_max_L'] >= $volume ) {
		return '';
	}

	return 'a ficha declara até ' . aquametria_c5_litros( $p['volume_max_L'] ) . ' L';
}
}

/* Um cartão. O MESMO HTML que o script monta em vitrineCartao(). */
if ( ! function_exists( 'aquametria_c5_vitrine_cartao_html' ) ) {
function aquametria_c5_vitrine_cartao_html( $p, $e, $acima ) {
	$preco    = aquametria_c5_preco_texto( $p );
	$ressalva = aquametria_c5_vt_ressalva_curta( $p, $e['volume'] );

	$h = '<li class="aqm-c5-vt-item">';

	if ( $p['link'] ) {
		$h .= '<a class="aqm-c5-vt-cartao" href="' . esc_url( $p['link'] ) . '" target="_blank" rel="sponsored noopener">';
	} else {
		/* Sem link não existe destino, e cartão sem destino não é âncora. O que o
		   contrato proíbe é div com onclick fingindo ser link. */
		$h .= '<div class="aqm-c5-vt-cartao aqm-c5-vt-sem-link">';
	}

	if ( ! empty( $p['imagem'] ) && ! empty( $p['imagem']['url'] ) ) {
		$img = '<img src="' . esc_url( $p['imagem']['url'] ) . '" alt="' . esc_attr( $p['imagem']['alt'] ) . '"';
		if ( ! empty( $p['imagem']['largura'] ) && ! empty( $p['imagem']['altura'] ) ) {
			$img .= ' width="' . esc_attr( $p['imagem']['largura'] ) . '" height="' . esc_attr( $p['imagem']['altura'] ) . '"';
		}
		$img .= ' loading="lazy" decoding="async">';
		$h   .= '<span class="aqm-c5-vt-foto">' . $img . '</span>';
	} else {
		/* Espaço reservado neutro. Produto sem foto NÃO some da vitrine: perder a
		   recomendação técnica certa por falta de imagem é trocar o certo pelo
		   bonito (seção 6 do ARQUIPELAGO.md). Nesta calculadora isso é a regra e
		   não a exceção — 16 dos 18 aquecedores do catálogo não têm foto. */
		$h .= '<span class="aqm-c5-vt-foto aqm-c5-vt-foto-vazia" aria-hidden="true">';
		$h .= '<span class="aqm-c5-vt-sigla">' . esc_html( $p['marca'] ) . '</span></span>';
	}

	$h .= '<span class="aqm-c5-vt-marca">' . esc_html( $p['marca'] ) . '</span>';
	$h .= '<span class="aqm-c5-vt-modelo">' . esc_html( aquametria_c5_modelo_curto( $p ) ) . '</span>';
	$h .= '<span class="aqm-c5-vt-espec">' . esc_html( aquametria_c5_vt_espec_frase( $p, $e, $acima ) ) . '</span>';

	if ( '' !== $ressalva ) {
		$h .= '<span class="aqm-c5-vt-ressalva">' . esc_html( $ressalva ) . '</span>';
	}

	if ( '' !== $preco ) {
		$h .= '<span class="aqm-c5-vt-preco">' . esc_html( $preco ) . '</span>';
	} else {
		$h .= '<span class="aqm-c5-vt-preco aqm-c5-vt-sem-preco">sem cotação coletada</span>';
	}

	if ( $p['link'] ) {
		$h .= '<span class="aqm-c5-vt-botao">Ver na ' . esc_html( 'shopee' === $p['loja'] ? 'Shopee' : $p['loja'] ) . '</span>';
		$h .= '<span class="aqm-c5-vt-selo">link patrocinado</span>';
		$h .= '</a>';
	} else {
		$h .= '<span class="aqm-c5-vt-espera">link de loja em breve</span>';
		$h .= '<span class="aqm-c5-vt-selo">entrou pela ficha técnica, não pelo link</span>';
		$h .= '</div>';
	}

	$h .= '</li>';

	return $h;
}
}

/* A vitrine SERVIDA no HTML, para o aquário de referência de 100 litros. A
   pintada mostra o aquário de quem está lendo; esta existe porque um modelo de
   linguagem e um crawler não executam JavaScript, e vitrine que só nasce no
   clique é vitrine que só o comprador que já chegou vê.

   Ela para em 5 cartões porque a seção 7 do contrato manda de três a cinco
   produtos, e porque o script pinta no máximo cinco: uma vitrine servida mais
   longa que a pintada faria as duas metades da mesma página discordarem. */
if ( ! function_exists( 'aquametria_c5_vitrine_servida_html' ) ) {
function aquametria_c5_vitrine_servida_html() {
	$volume = 100;
	$e      = aquametria_c5_exemplo( $volume );
	$lista  = array_slice( aquametria_c5_produtos_exemplo( $e ), 0, 5 );

	$divulgacao = aquametria_c5_url( AQUAMETRIA_C5_PAGINA_AFILIADOS );

	$h  = '<div class="aqm-c5-painel aqm-c5-vitrine-servida">';
	$h .= '<h3>Os aquecedores para um aquário de ' . esc_html( aquametria_c5_litros( $volume ) ) . ' litros</h3>';

	if ( ! $lista ) {
		$h .= '<p class="aqm-c5-sub">Nenhum aquecedor do banco da Aquametria fica hoje entre '
			. esc_html( aquametria_c5_watts( $e['piso'] ) ) . ' e '
			. esc_html( aquametria_c5_watts( $e['comercial'] ? $e['comercial'] : $e['teto'] ) )
			. ' W. O banco tem ' . esc_html( count( aquametria_c5_catalogo() ) ) . ' aquecedores com ficha completa e cresce a cada coleta. '
			. 'Preferimos não mostrar produto nenhum a mostrar um que não atende ao número.</p>';
		$h .= '</div>';
		return $h;
	}

	$com_link = 0;
	foreach ( $lista as $p ) {
		if ( $p['link'] ) {
			$com_link++;
		}
	}

	$h .= '<p class="aqm-c5-sub">Um aquário de ' . esc_html( aquametria_c5_litros( $volume ) )
		. ' litros num cômodo que cai até ' . esc_html( AQUAMETRIA_C5_DELTA_COBERTO ) . ' °C abaixo da água pede de '
		. esc_html( aquametria_c5_watts( $e['piso'] ) ) . ' a ' . esc_html( aquametria_c5_watts( $e['teto'] ) )
		. ' W, e estes são os aquecedores do banco da Aquametria cuja potência cai nessa faixa. '
		. 'A ordem é pela proximidade do topo dela; nada aqui é ordenado por comissão, e modelo sem link de loja aparece do mesmo jeito. '
		. 'Esta lista de exemplo não aplica as duas barreiras de segurança do formulário — a voltagem da sua tomada e a faixa de ajuste alcançar a sua temperatura-alvo —, '
		. 'porque um exemplo não sabe nenhuma das duas. Preencha o formulário acima para ver a lista do seu caso.</p>';

	$h .= '<ul class="aqm-c5-vt-trilho">';
	foreach ( $lista as $p ) {
		$h .= aquametria_c5_vitrine_cartao_html( $p, $e, $p['potencia_w'] > $e['teto'] );
	}
	$h .= '</ul>';

	$h .= '<p class="aqm-c5-criterio">' . esc_html( $com_link ) . ' de ' . esc_html( count( $lista ) )
		. ' têm link de loja hoje; os outros aparecem do mesmo jeito, com o lugar do botão reservado — '
		. 'quem entra é decidido pela ficha técnica, e nunca por ter ou não link.</p>';

	$h .= '<p class="aqm-c5-aviso-afiliado"><strong>Sobre o preço e o botão.</strong> '
		. 'O valor de cada cartão <strong>não é preço de hoje</strong>: é a cotação que a Aquametria leu naquele anúncio na data escrita ao lado, '
		. 'e preço de aquarismo muda toda semana. Confira no anúncio antes de comprar. '
		. 'Os botões levam a lojas por link de afiliado, marcado como patrocinado: se você comprar por eles, a Aquametria pode receber comissão, sem custo a mais para você. '
		. 'A ficha técnica de cada aquecedor vem do fabricante ou do varejo especializado, com o endereço e a data — o anúncio da loja nunca é a nossa fonte. '
		. '<a href="' . esc_url( $divulgacao ) . '">Como a Aquametria ganha dinheiro</a>.</p>';

	$h .= '</div>';

	return $h;
}
}

/* A linha de promessa, antes do formulário: o que a pessoa recebe se preencher.
   Curta, sem exclamação, sem tom de anúncio (seção 6 do ARQUIPELAGO.md). */
if ( ! function_exists( 'aquametria_c5_promessa_html' ) ) {
function aquametria_c5_promessa_html() {
	return '<p class="aqm-c5-promessa">Calcule a potência do aquecedor pelo frio que faz no seu cômodo '
		. 'e veja quais aparelhos atendem, com a faixa de ajuste e a fonte de cada um.</p>';
}
}

/* A barra do celular. Ela só existe enquanto o resultado está fora da tela, e só
   em tela estreita — o CSS a esconde acima de 600 px, e o script só liga a
   classe depois de um cálculo. Fora do <form> de propósito: position:fixed
   dentro de um painel com rolagem própria briga com o painel. */
if ( ! function_exists( 'aquametria_c5_barra_html' ) ) {
function aquametria_c5_barra_html() {
	$h  = '<div class="aqm-c5-barra" id="aqm-c5-barra" aria-hidden="true">';
	$h .= '<span class="aqm-c5-barra-texto" id="aqm-c5-barra-texto"></span>';
	$h .= '<button type="button" class="aqm-c5-barra-botao" id="aqm-c5-barra-ir">Ver o resultado</button>';
	$h .= '</div>';
	return $h;
}
}

/* ---------------------------------------------------------------------------
 * 2. Catálogo de aquecedores
 *
 * NÃO EDITE À MÃO o trecho entre os marcadores. Ele é a cópia, dentro do
 * snippet, do que dados/produtos-aquecedor.json já tem — porque o site não lê o
 * repositório em tempo de execução. Depois de mexer no banco:
 *
 *     python3 ferramentas/gerar-catalogo-aquecedores.py
 *
 * Entra no catálogo quem o validador considera apto a ser sugerido pela C5
 * (minimo_para_sugerir do esquema) e não está em rascunho nem em revalidar.
 * O campo ajuste_conservador marca quem chegou aqui pela regra V17: a faixa de
 * ajuste é a interseção das fontes em conflito, e a tela diz isso.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c5_catalogo' ) ) {
function aquametria_c5_catalogo() {
	/* CATALOGO-INICIO — gerado por ferramentas/gerar-catalogo-aquecedores.py */
	return array(
		array(
			'id' => 'roxin-ht-1300-q3-25w',
			'marca' => 'Roxin',
			'modelo' => 'HT-1300 25 W',
			'tipo' => 'quartzo',
			'potencia_w' => 25,
			'volume_min_L' => 20,
			'volume_max_L' => 35,
			'ajuste_min_C' => 22,
			'ajuste_max_C' => 32,
			'ajuste_conservador' => true,
			'ajuste_derivacao' => 'intersecao dos dois intervalos: 22 C e o maior dos pisos, 32 C e o menor dos tetos. Nao e media nem escolha de fonte — e a unica faixa que as DUAS fontes concordam que o aparelho cobre. Fora dela, o aparelho pode ou nao alcancar, e a Aquametria nao afirma que alcanca. Regra V17 do esquema.',
			'precisao_C' => null,
			'comprimento_cm' => 23.0,
			'seco' => null,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'WorldFish e AquaMaeda (varejo BR), fichas do HT-1300/Q3 25 W (20 a 35 L, 2,3 x 23 cm, cabo de 90 cm, IP68)',
			'fonte_url' => 'https://worldfish.com.br/produtos/termostato-com-aquecedor-roxin-ht-1300-q3-25w-110v/',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-08',
			'link' => null,
			'anuncio' => null,
			'voltagem_anuncio' => null,
			'loja' => null,
			'conflito_volume' => null,
			'imagem' => null,
			'preco' => null,
		),
		array(
			'id' => 'eheim-jager-50w',
			'marca' => 'Eheim',
			'modelo' => 'Jager 50 W',
			'tipo' => 'resistencia-vidro',
			'potencia_w' => 50,
			'volume_min_L' => 25,
			'volume_max_L' => 50,
			'ajuste_min_C' => 18,
			'ajuste_max_C' => 34,
			'ajuste_conservador' => false,
			'ajuste_derivacao' => null,
			'precisao_C' => 0.5,
			'comprimento_cm' => 25.0,
			'seco' => true,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'Tabela da linha Jager publicada por varejo europeu (Aquaeden, Top Corals) e norte-americano (SaltwaterAquarium), com potencia, volume declarado e comprimento modelo a modelo',
			'fonte_url' => 'https://aquaeden-shop.net/webstore/index.php?id_product=794&controller=product',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-08',
			'link' => null,
			'anuncio' => null,
			'voltagem_anuncio' => null,
			'loja' => null,
			'conflito_volume' => null,
			'imagem' => null,
			'preco' => null,
		),
		array(
			'id' => 'roxin-ht-1300-q3-50w',
			'marca' => 'Roxin',
			'modelo' => 'HT-1300 50 W',
			'tipo' => 'quartzo',
			'potencia_w' => 50,
			'volume_min_L' => 40,
			'volume_max_L' => 60,
			'ajuste_min_C' => 22,
			'ajuste_max_C' => 32,
			'ajuste_conservador' => true,
			'ajuste_derivacao' => 'intersecao dos dois intervalos: 22 C e o maior dos pisos, 32 C e o menor dos tetos. Nao e media nem escolha de fonte — e a unica faixa que as DUAS fontes concordam que o aparelho cobre. Fora dela, o aparelho pode ou nao alcancar, e a Aquametria nao afirma que alcanca. Regra V17 do esquema.',
			'precisao_C' => null,
			'comprimento_cm' => 23.0,
			'seco' => null,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'WorldFish e AquaMaeda (varejo BR), fichas do HT-1300/Q3 50 W (40 a 60 L, 2,3 x 23 cm, cabo de 90 cm, IP68)',
			'fonte_url' => 'https://worldfish.com.br/produtos/termostato-com-aquecedor-roxin-ht-1300-q3-50w-220v/',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-08',
			'link' => 'https://s.shopee.com.br/Ln66ZQPqy',
			'anuncio' => 'Roxin Q3 50 W 220 V',
			'voltagem_anuncio' => '220',
			'loja' => 'shopee',
			'conflito_volume' => null,
			'imagem' => array(
				'url' => 'https://down-bs-br.img.susercontent.com/br-11134207-7r98o-lvyuqrs817sla5.webp',
				'alt' => 'Termostato com aquecedor Roxin Q3 de 50 W, tubo de quartzo submersível com dial de ajuste de temperatura no topo',
				'largura' => null,
				'altura' => null,
				'verificado_em' => null,
			),
			'preco' => array(
				'min' => 66.23,
				'max' => 66.23,
				'loja' => 'Shopee',
				'coletado_em' => '2026-09-09',
				'cotacoes' => 1,
			),
		),
		array(
			'id' => 'atman-at-100',
			'marca' => 'Atman',
			'modelo' => 'AT-100',
			'tipo' => 'quartzo',
			'potencia_w' => 100,
			'volume_min_L' => null,
			'volume_max_L' => 100,
			'ajuste_min_C' => 20,
			'ajuste_max_C' => 34,
			'ajuste_conservador' => false,
			'ajuste_derivacao' => null,
			'precisao_C' => null,
			'comprimento_cm' => 25.0,
			'seco' => null,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'Aqua SN e Aquarius Hobby (varejo BR), ficha do AT-100: 100 W, aquarios de ate 100 L, 25 cm de comprimento',
			'fonte_url' => 'https://www.aquasn.com.br/atman-termostato-eletronico-submerso-100wts-codigo-at-100-220v',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'voltagem_anuncio' => null,
			'loja' => null,
			'conflito_volume' => null,
			'imagem' => null,
			'preco' => null,
		),
		array(
			'id' => 'eheim-jager-100w',
			'marca' => 'Eheim',
			'modelo' => 'Jager 100 W',
			'tipo' => 'resistencia-vidro',
			'potencia_w' => 100,
			'volume_min_L' => 75,
			'volume_max_L' => 100,
			'ajuste_min_C' => 18,
			'ajuste_max_C' => 34,
			'ajuste_conservador' => false,
			'ajuste_derivacao' => null,
			'precisao_C' => 0.5,
			'comprimento_cm' => 32.0,
			'seco' => true,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'Tabela da linha Jager publicada por varejo europeu (Aquaeden, Top Corals) e norte-americano (SaltwaterAquarium), com potencia, volume declarado e comprimento modelo a modelo',
			'fonte_url' => 'https://aquaeden-shop.net/webstore/index.php?id_product=794&controller=product',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-08',
			'link' => null,
			'anuncio' => null,
			'voltagem_anuncio' => null,
			'loja' => null,
			'conflito_volume' => null,
			'imagem' => null,
			'preco' => null,
		),
		array(
			'id' => 'roxin-ht-1300-q3-100w',
			'marca' => 'Roxin',
			'modelo' => 'HT-1300 100 W',
			'tipo' => 'quartzo',
			'potencia_w' => 100,
			'volume_min_L' => 50,
			'volume_max_L' => 150,
			'ajuste_min_C' => 22,
			'ajuste_max_C' => 32,
			'ajuste_conservador' => true,
			'ajuste_derivacao' => 'intersecao dos dois intervalos: 22 C e o maior dos pisos, 32 C e o menor dos tetos. Nao e media nem escolha de fonte — e a unica faixa que as DUAS fontes concordam que o aparelho cobre. Fora dela, o aparelho pode ou nao alcancar, e a Aquametria nao afirma que alcanca. Regra V17 do esquema.',
			'precisao_C' => null,
			'comprimento_cm' => null,
			'seco' => null,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'Mega Aquarios e RS Discus (varejo BR especializado), fichas do HT-1300/Q3 100 W',
			'fonte_url' => 'https://www.megaaquarios.com.br/termostato-aquecedor-roxin-q3-100w-termometro-aquario.html',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-08',
			'link' => 'https://s.shopee.com.br/50YsvKBY0s',
			'anuncio' => 'ROXIN HT-1300 Q3 100W 127V para aquario ate 100 litros',
			'voltagem_anuncio' => '127',
			'loja' => 'shopee',
			'conflito_volume' => null,
			'imagem' => null,
			'preco' => array(
				'min' => 78.9,
				'max' => 78.9,
				'loja' => 'Shopee',
				'coletado_em' => '2026-09-07',
				'cotacoes' => 1,
			),
		),
		array(
			'id' => 'atman-at-150',
			'marca' => 'Atman',
			'modelo' => 'AT-150',
			'tipo' => 'quartzo',
			'potencia_w' => 150,
			'volume_min_L' => null,
			'volume_max_L' => 150,
			'ajuste_min_C' => 20,
			'ajuste_max_C' => 34,
			'ajuste_conservador' => false,
			'ajuste_derivacao' => null,
			'precisao_C' => null,
			'comprimento_cm' => 27.0,
			'seco' => null,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'Aquarius Hobby e Aqua SN (varejo BR), ficha do AT-150: 150 W, aquarios de ate 150 L, 27 cm',
			'fonte_url' => 'https://aquariushobby.commercesuite.com.br/agua-doce/controle-de-temperatura/termostatos-e-aquecedores/aquecedor-com-termostato-atman-150w-at-150',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'voltagem_anuncio' => null,
			'loja' => null,
			'conflito_volume' => null,
			'imagem' => null,
			'preco' => null,
		),
		array(
			'id' => 'eheim-jager-150w',
			'marca' => 'Eheim',
			'modelo' => 'Jager 150 W',
			'tipo' => 'resistencia-vidro',
			'potencia_w' => 150,
			'volume_min_L' => 125,
			'volume_max_L' => 150,
			'ajuste_min_C' => 18,
			'ajuste_max_C' => 34,
			'ajuste_conservador' => false,
			'ajuste_derivacao' => null,
			'precisao_C' => 0.5,
			'comprimento_cm' => 35.0,
			'seco' => true,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'Tabela da linha Jager publicada por varejo europeu (Aquaeden, Top Corals) e norte-americano (SaltwaterAquarium), com potencia, volume declarado e comprimento modelo a modelo',
			'fonte_url' => 'https://aquaeden-shop.net/webstore/index.php?id_product=794&controller=product',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-08',
			'link' => null,
			'anuncio' => null,
			'voltagem_anuncio' => null,
			'loja' => null,
			'conflito_volume' => 'de 125 a 150 L segundo tabela da linha Jager no varejo europeu/americano (Aquaeden, Top Corals); de 200 a 300 L segundo Agrosete (varejo BR), ficha do Eheim 150 W 220 V',
			'imagem' => null,
			'preco' => null,
		),
		array(
			'id' => 'oceantech-warmer-x-5-150w',
			'marca' => 'Ocean Tech',
			'modelo' => 'Warmer X-5 150 W',
			'tipo' => 'quartzo',
			'potencia_w' => 150,
			'volume_min_L' => null,
			'volume_max_L' => 100,
			'ajuste_min_C' => 20,
			'ajuste_max_C' => 34,
			'ajuste_conservador' => false,
			'ajuste_derivacao' => null,
			'precisao_C' => 1.0,
			'comprimento_cm' => 29.0,
			'seco' => null,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'Varejo especializado BR (Aquaricamp, Aquaripesca, Barbusfish, Pet Patao Shop), ficha do Ocean Tech Warmer X-5 150 W: 150 W, 29 cm de comprimento, 3 cm de diametro, cabo de 1,20 m, ajuste de 20 a 34 C com tolerancia menor que 1 C, resistencia de niquel-cromo, tubo de quartzo a prova de explosao, totalmente submerso na vertical, disponivel em 110 e em 220 V',
			'fonte_url' => 'https://www.aquaricamp.com.br/termostato-ocean-tech-warmer-x-5-150w.html',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => 'https://s.shopee.com.br/6VNjRo5IKE',
			'anuncio' => 'OceanTech X-5 150 W 220 V / 110 V',
			'voltagem_anuncio' => '220',
			'loja' => 'shopee',
			'conflito_volume' => 'ate 150 L segundo titulos de varejo BR (Pet Patao Shop; Aquariando Pet): \'para aquarios ate 150 litros\'; ate 130 L segundo ficha de varejo BR lida por resultado de busca, sem pagina atribuida: \'indicado para aquarios de ate 130 litros\'; ate 100 L segundo ficha de varejo BR lida por resultado de busca, sem pagina atribuida: \'indicado para aquario ate 100 litros\'',
			'imagem' => array(
				'url' => 'https://down-bs-br.img.susercontent.com/2bb44a02215e58113eb2e28a852f5552.webp',
				'alt' => 'Termostato aquecedor Ocean Tech Warmer X-5 de 150 W, tubo de quartzo submersível com escala de temperatura e dial de ajuste no topo',
				'largura' => null,
				'altura' => null,
				'verificado_em' => null,
			),
			'preco' => array(
				'min' => 159.9,
				'max' => 159.9,
				'loja' => 'Shopee',
				'coletado_em' => '2026-09-09',
				'cotacoes' => 1,
			),
		),
		array(
			'id' => 'atman-at-200',
			'marca' => 'Atman',
			'modelo' => 'AT-200',
			'tipo' => 'quartzo',
			'potencia_w' => 200,
			'volume_min_L' => null,
			'volume_max_L' => 200,
			'ajuste_min_C' => 20,
			'ajuste_max_C' => 34,
			'ajuste_conservador' => false,
			'ajuste_derivacao' => null,
			'precisao_C' => null,
			'comprimento_cm' => 30.0,
			'seco' => null,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'Pro-Aquarista (varejo BR especializado), ficha do AT-200: 200 W, 30 cm, aquarios de ate 200 L',
			'fonte_url' => 'https://www.proaquarista.com.br/atman-termostato-at-200-200w',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'voltagem_anuncio' => null,
			'loja' => null,
			'conflito_volume' => null,
			'imagem' => null,
			'preco' => null,
		),
		array(
			'id' => 'eheim-jager-200w',
			'marca' => 'Eheim',
			'modelo' => 'Jager 200 W',
			'tipo' => 'resistencia-vidro',
			'potencia_w' => 200,
			'volume_min_L' => 30,
			'volume_max_L' => 400,
			'ajuste_min_C' => 18,
			'ajuste_max_C' => 34,
			'ajuste_conservador' => false,
			'ajuste_derivacao' => null,
			'precisao_C' => 0.5,
			'comprimento_cm' => 41.0,
			'seco' => true,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'Eheim, linha Jager (25 a 300 W, 9 tamanhos, 20 a 1000 L; ajuste 18 a 34 C com precisao de 0,5 C; 200 W declarado para 30 a 400 L, 400 mm de comprimento, 24,5 mm de diametro, cabo de 170 cm, vidro Schott DURAN, desliga fora d\'agua); mesma coleta que gerou a constante eheim-jager-dimensionamento do Bloco 2',
			'fonte_url' => 'https://eheim.com/en_GB/products/technology/heating/thermocontrol/jager',
			'fonte_status' => 'fabricante-via-busca',
			'verificado_em' => '2026-09-08',
			'link' => null,
			'anuncio' => null,
			'voltagem_anuncio' => null,
			'loja' => null,
			'conflito_volume' => 'de 30 a 400 L segundo catalogo do proprio fabricante (Eheim), linha Jager; de 300 a 400 L segundo varejo BR e tabela de varejo da linha (Pata Mania, Aquaeden, Top Corals)',
			'imagem' => null,
			'preco' => null,
		),
		array(
			'id' => 'roxin-ht-1300-q3-200w',
			'marca' => 'Roxin',
			'modelo' => 'HT-1300 200 W',
			'tipo' => 'quartzo',
			'potencia_w' => 200,
			'volume_min_L' => null,
			'volume_max_L' => 200,
			'ajuste_min_C' => 22,
			'ajuste_max_C' => 32,
			'ajuste_conservador' => true,
			'ajuste_derivacao' => 'intersecao dos dois intervalos: 22 C e o maior dos pisos, 32 C e o menor dos tetos. Nao e media nem escolha de fonte — e a unica faixa que as DUAS fontes concordam que o aparelho cobre. Fora dela, o aparelho pode ou nao alcancar, e a Aquametria nao afirma que alcanca. Regra V17 do esquema.',
			'precisao_C' => null,
			'comprimento_cm' => null,
			'seco' => null,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'Petlove e Fundo do Mar Aquarios (varejo BR), ficha do HT-1300 200 W',
			'fonte_url' => 'https://www.petlove.com.br/termostato-com-aquecedor-roxin-ht-1300-200w/p',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-08',
			'link' => 'https://s.shopee.com.br/6L4GVnErqJ',
			'anuncio' => 'Roxin Q3 Ht-1300 Q3 200w 110V',
			'voltagem_anuncio' => '110',
			'loja' => 'shopee',
			'conflito_volume' => null,
			'imagem' => null,
			'preco' => array(
				'min' => 74.99,
				'max' => 74.99,
				'loja' => 'Shopee',
				'coletado_em' => '2026-09-07',
				'cotacoes' => 1,
			),
		),
		array(
			'id' => 'oceantech-warmer-x-5-250w',
			'marca' => 'Ocean Tech',
			'modelo' => 'Warmer X-5 250 W',
			'tipo' => 'quartzo',
			'potencia_w' => 250,
			'volume_min_L' => null,
			'volume_max_L' => 260,
			'ajuste_min_C' => 20,
			'ajuste_max_C' => 34,
			'ajuste_conservador' => false,
			'ajuste_derivacao' => null,
			'precisao_C' => 1.0,
			'comprimento_cm' => 35.0,
			'seco' => null,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'Aquario Itaquera (varejo BR especializado), ficha do Ocean Tech Warmer X-5 250 W em 110 V: recomendado para aquarios de ate 260 litros, cerca de 35 cm de comprimento',
			'fonte_url' => 'https://www.aquarioitaquera.com.br/produtos/termostato-para-aquario-com-aquecedor-ocean-tech-warmer-x-5-250w/',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'voltagem_anuncio' => null,
			'loja' => null,
			'conflito_volume' => null,
			'imagem' => null,
			'preco' => null,
		),
		array(
			'id' => 'atman-at-300',
			'marca' => 'Atman',
			'modelo' => 'AT-300',
			'tipo' => 'quartzo',
			'potencia_w' => 300,
			'volume_min_L' => null,
			'volume_max_L' => 300,
			'ajuste_min_C' => 20,
			'ajuste_max_C' => 34,
			'ajuste_conservador' => false,
			'ajuste_derivacao' => null,
			'precisao_C' => null,
			'comprimento_cm' => 37.0,
			'seco' => null,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'Pro-Aquarista (varejo BR especializado), ficha do AT-300: 300 W, 37 cm de comprimento por 2,3 cm de diametro, aquarios de ate 300 L, escala de 20 a 34 C, vendido em 110 V e em 220 V',
			'fonte_url' => 'https://www.proaquarista.com.br/produto/atman-termostato-at-300-300w-110v.html',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'voltagem_anuncio' => null,
			'loja' => null,
			'conflito_volume' => null,
			'imagem' => null,
			'preco' => null,
		),
		array(
			'id' => 'roxin-ht-1300-q3-300w',
			'marca' => 'Roxin',
			'modelo' => 'HT-1300 300 W',
			'tipo' => 'quartzo',
			'potencia_w' => 300,
			'volume_min_L' => 250,
			'volume_max_L' => 350,
			'ajuste_min_C' => 22,
			'ajuste_max_C' => 32,
			'ajuste_conservador' => true,
			'ajuste_derivacao' => 'intersecao dos dois intervalos: 22 C e o maior dos pisos, 32 C e o menor dos tetos. Nao e media nem escolha de fonte — e a unica faixa que as DUAS fontes concordam que o aparelho cobre. Fora dela, o aparelho pode ou nao alcancar, e a Aquametria nao afirma que alcanca. Regra V17 do esquema.',
			'precisao_C' => null,
			'comprimento_cm' => null,
			'seco' => null,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'Mega Aquarios (varejo BR especializado), ficha do Q3 300 W',
			'fonte_url' => 'https://www.megaaquarios.com.br/termostato-aquecedor-roxin-300w-termometro-aquario.html',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-08',
			'link' => 'https://s.shopee.com.br/AUtpTbdMqc',
			'anuncio' => 'Termostato Com Aquecedor Roxin HT-1300 - Q3 - 300w - 220v',
			'voltagem_anuncio' => '220',
			'loja' => 'shopee',
			'conflito_volume' => null,
			'imagem' => null,
			'preco' => array(
				'min' => 85.5,
				'max' => 85.5,
				'loja' => 'Shopee',
				'coletado_em' => '2026-09-07',
				'cotacoes' => 1,
			),
		),
		array(
			'id' => 'hopar-j-226-400w',
			'marca' => 'Hopar',
			'modelo' => 'J-226 400 W',
			'tipo' => 'quartzo',
			'potencia_w' => 400,
			'volume_min_L' => null,
			'volume_max_L' => 500,
			'ajuste_min_C' => 18,
			'ajuste_max_C' => 34,
			'ajuste_conservador' => false,
			'ajuste_derivacao' => null,
			'precisao_C' => null,
			'comprimento_cm' => 50.0,
			'seco' => null,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'Varejo BR especializado (Rei dos Aquarios; Royal Pets), ficha do Hopar J-226 400 W: termostato interno com protecao anti-explosao, tubo de quartzo resistente a corrosao, vidro resistente com vedacao dupla, fixacao por ventosa, LED indicador de acionamento, ajuste de 18 a 34 C, diametro 3,5 cm, comprimento 50 cm, cabo de 1,02 m, vendido em 127 V e em 220 V, indicado para aquarios de ate 500 litros',
			'fonte_url' => 'https://www.lojareidosaquarios.com.br/produto/hopar-termostato-j-226-400w-127v.html',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'voltagem_anuncio' => null,
			'loja' => null,
			'conflito_volume' => 'ate 500 L segundo Rei dos Aquarios e Royal Pets (varejo BR especializado): \'para aquarios de ate 500 litros\'; ate 400 L segundo titulo de anuncio de marketplace: \'Termostato Aquecedor 400W para Aquarios ate 400 L Hopar J-226\'',
			'imagem' => null,
			'preco' => null,
		),
		array(
			'id' => 'hopar-j-226-500w',
			'marca' => 'Hopar',
			'modelo' => 'J-226 500 W',
			'tipo' => 'quartzo',
			'potencia_w' => 500,
			'volume_min_L' => null,
			'volume_max_L' => 500,
			'ajuste_min_C' => 17,
			'ajuste_max_C' => 35,
			'ajuste_conservador' => false,
			'ajuste_derivacao' => null,
			'precisao_C' => null,
			'comprimento_cm' => 35.0,
			'seco' => null,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'Aquaricamp (varejo BR especializado), ficha do Termostato Hopar J-226 500 W: indicado para aquarios de ate 500 litros, mantem a temperatura entre 17 e 35 C, comprimento aproximado de 35 cm, vidro resistente com protecao adicional e sistema de protecao contra choque termico, duas ventosas, uso na vertical ou na horizontal',
			'fonte_url' => 'https://www.aquaricamp.com.br/termostato-hopar-j-226-500w.html',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'voltagem_anuncio' => null,
			'loja' => null,
			'conflito_volume' => null,
			'imagem' => null,
			'preco' => null,
		),
		array(
			'id' => 'oceantech-warmer-x-5-500w',
			'marca' => 'Ocean Tech',
			'modelo' => 'Warmer X-5 500 W',
			'tipo' => 'quartzo',
			'potencia_w' => 500,
			'volume_min_L' => null,
			'volume_max_L' => 500,
			'ajuste_min_C' => 20,
			'ajuste_max_C' => 34,
			'ajuste_conservador' => false,
			'ajuste_derivacao' => null,
			'precisao_C' => 1.0,
			'comprimento_cm' => 45.0,
			'seco' => null,
			'voltagem' => array( '110', '220' ),
			'fonte_ref' => 'Varejo BR especializado (Aquarista Amador; Fazenda Submersa; Eco Bichos), ficha do Ocean Tech Warmer X-5 500 W: 500 W, 220 V ou 110 V, dimensoes 45 x 2,5 x 2,5 cm, cabo de 1,13 m, ajuste de 20 a 34 C com tolerancia menor que 1 C, tubo de quartzo, totalmente submersivel com duplo isolamento',
			'fonte_url' => 'https://www.aquaristaamador.com.br/termostato-ocen-tech-warmer-x-5-500w',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'voltagem_anuncio' => null,
			'loja' => null,
			'conflito_volume' => 'ate 500 L segundo Rilcomercial e Dinho\'s Reef (varejo BR): \'aquecedor termostato Ocean Tech 500w aquarios 500 litros\'; de 350 a 600 L segundo Mega Aquarios (varejo BR): \'adequado para aquarios de 350 a 600 litros\', com termometro externo adesivo e ventosas na embalagem; de 500 a 1000 L segundo Aquarista Amador (varejo BR): litragem recomendada de 600 L no quadro de especificacoes e \'adequado para aquarios de 500 a 1000 litros\' no texto da MESMA pagina',
			'imagem' => null,
			'preco' => null,
		),
	);
	/* CATALOGO-FIM */
}
}

/* ---------------------------------------------------------------------------
 * 3. Estilo (impresso uma vez por página, junto do primeiro shortcode)
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c5_css' ) ) {
function aquametria_c5_css() {
	return <<<'CSS'
.aqm-c5{--c5-tinta:var(--aqm-tinta,#0D1B22);--c5-lamina:var(--aqm-lamina,#0E7C8C);
--c5-papel:var(--aqm-papel,#F4F7F7);--c5-superficie:var(--aqm-superficie,#FFFFFF);
--c5-traco:var(--aqm-traco,#DDE5E6);--c5-legenda:var(--aqm-legenda,#5C7075);
--c5-alerta:var(--aqm-alerta,#B5762A);
--c5-display:var(--aqm-display,"Chivo","Trebuchet MS",Arial,sans-serif);
--c5-texto:var(--aqm-texto,"IBM Plex Sans",system-ui,Arial,sans-serif);
--c5-mono:var(--aqm-mono,"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace);
max-width:52rem;font-family:var(--c5-texto);color:var(--c5-tinta);}
.aqm-c5 *{box-sizing:border-box;}
.aqm-c5 form{margin:0;}
.aqm-c5-painel{background:var(--c5-superficie);border:1px solid var(--c5-traco);border-radius:3px;padding:1.2rem 1.3rem;margin:0 0 1.2rem;}
.aqm-c5-painel h3{font-family:var(--c5-display);font-size:1.05rem;margin:0 0 .2rem;}
.aqm-c5-painel .aqm-c5-sub{color:var(--c5-legenda);font-size:.9rem;margin:0 0 1rem;line-height:1.5;}
.aqm-c5-grade{display:grid;grid-template-columns:repeat(auto-fit,minmax(10.5rem,1fr));gap:.9rem;}
.aqm-c5-campo{display:flex;flex-direction:column;gap:.25rem;}
.aqm-c5-campo label{font-size:.82rem;font-weight:600;letter-spacing:.01em;}
.aqm-c5-campo .aqm-c5-dica{font-size:.74rem;color:var(--c5-legenda);line-height:1.35;}
.aqm-c5 input[type=text],.aqm-c5 select{width:100%;font-family:var(--c5-mono);font-size:1rem;padding:.5rem .6rem;border:1px solid var(--c5-traco);border-radius:2px;background:var(--c5-superficie);color:var(--c5-tinta);}
.aqm-c5 select{font-family:var(--c5-texto);}
.aqm-c5 input:focus,.aqm-c5 select:focus{outline:2px solid var(--c5-lamina);outline-offset:1px;}
.aqm-c5 input.aqm-c5-erro{border-color:var(--c5-alerta);}
.aqm-c5-caixa{display:flex;align-items:flex-start;gap:.45rem;margin:1rem 0 0;font-size:.9rem;}
.aqm-c5-caixa input{margin-top:.2rem;}
.aqm-c5-botoes{display:flex;flex-wrap:wrap;gap:.7rem;align-items:center;margin:1.1rem 0 0;}
.aqm-c5 button{font-family:var(--c5-texto);font-weight:600;font-size:.95rem;padding:.6rem 1.1rem;border:0;border-radius:2px;background:var(--c5-lamina);color:var(--c5-superficie);cursor:pointer;}
.aqm-c5 button.aqm-c5-secundario{background:transparent;color:var(--c5-lamina);border:1px solid var(--c5-traco);}
.aqm-c5 button:hover{filter:brightness(1.08);}
.aqm-c5-avisos{margin:.9rem 0 0;padding:0;list-style:none;}
.aqm-c5-avisos li{font-size:.88rem;color:var(--c5-alerta);margin:.25rem 0 0;line-height:1.45;}
.aqm-c5-resultado{margin:0 0 1.2rem;}
.aqm-c5-faixa{background:var(--c5-superficie);border:2px solid var(--c5-lamina);border-radius:3px;padding:1.1rem 1.2rem;margin:0 0 1rem;}
.aqm-c5-rotulo{font-family:var(--c5-mono);font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--c5-legenda);}
.aqm-c5-valor{font-family:var(--c5-mono);font-size:2rem;font-weight:600;line-height:1.1;font-variant-numeric:tabular-nums;display:block;margin:.15rem 0 .1rem;}
.aqm-c5-valor .aqm-c5-unidade{font-size:.95rem;font-weight:500;color:var(--c5-legenda);margin-left:.3rem;}
.aqm-c5-criterio{font-size:.83rem;color:var(--c5-legenda);line-height:1.5;margin:0;}
.aqm-c5-delta{display:flex;flex-wrap:wrap;gap:.4rem .9rem;align-items:baseline;margin:.6rem 0 0;font-family:var(--c5-mono);font-size:.86rem;color:var(--c5-legenda);}
.aqm-c5-delta b{color:var(--c5-tinta);font-weight:600;}
.aqm-c5-cartoes{display:grid;grid-template-columns:repeat(auto-fit,minmax(13rem,1fr));gap:.9rem;margin:0 0 1rem;padding:0;list-style:none;}
.aqm-c5-cartao{background:var(--c5-superficie);border:1px solid var(--c5-traco);border-radius:3px;padding:1rem 1.1rem;margin:0;display:flex;flex-direction:column;gap:.3rem;}
.aqm-c5-cartao .aqm-c5-valor{font-size:1.5rem;}
.aqm-c5-cartao.aqm-c5-cartao-fora{border-style:dashed;border-color:var(--c5-alerta);}
.aqm-c5-nota{border-left:3px solid var(--c5-lamina);background:var(--c5-superficie);padding:.85rem 1rem;font-size:.92rem;line-height:1.55;color:var(--c5-legenda);margin:0 0 1rem;}
.aqm-c5-nota strong{color:var(--c5-tinta);}
.aqm-c5-nota.aqm-c5-nota-alerta{border-left-color:var(--c5-alerta);}
.aqm-c5-produtos{margin:0 0 1.2rem;}
.aqm-c5-produtos h3{font-family:var(--c5-display);font-size:1.05rem;margin:0 0 .2rem;}
.aqm-c5-lista{list-style:none;margin:1rem 0 0;padding:0;display:grid;gap:.9rem;}
.aqm-c5-produto{background:var(--c5-superficie);border:1px solid var(--c5-traco);border-radius:3px;padding:1rem 1.1rem;display:grid;grid-template-columns:6.5rem 1fr;gap:1rem;align-items:start;}
.aqm-c5-placa{background:var(--c5-papel);border:1px solid var(--c5-traco);border-radius:2px;padding:.7rem .5rem;text-align:center;display:flex;flex-direction:column;gap:.15rem;justify-content:center;min-height:6rem;}
.aqm-c5-placa .aqm-c5-marca{font-family:var(--c5-display);font-size:.9rem;font-weight:700;line-height:1.15;}
.aqm-c5-placa .aqm-c5-numero{font-family:var(--c5-mono);font-size:1.15rem;font-weight:600;color:var(--c5-lamina);line-height:1.1;}
.aqm-c5-placa .aqm-c5-un{font-family:var(--c5-mono);font-size:.62rem;letter-spacing:.08em;text-transform:uppercase;color:var(--c5-legenda);}
.aqm-c5-produto h4{font-family:var(--c5-display);font-size:1rem;margin:0 0 .35rem;}
.aqm-c5-grupo{margin:.4rem 0 0;padding:0 0 0 .8rem;border-left:2px solid var(--c5-lamina);}
.aqm-c5-grupo h4{font-family:var(--c5-display);font-size:.95rem;margin:0 0 .25rem;}
.aqm-c5-grupo p{font-size:.85rem;line-height:1.5;color:var(--c5-legenda);margin:0;}
/* O degrau comercial acima da faixa fica na mesma lista, sem tom de alerta: ele
   não é um erro, é a prateleira. O que o separa é a linha de 1px do grupo — sem
   gradiente e sem sombra colorida, como manda a seção 6 do ARQUIPELAGO.md. */
.aqm-c5-produto-acima{border-style:dashed;}
.aqm-c5-porque{font-size:.88rem;line-height:1.5;margin:0 0 .5rem;}
.aqm-c5-porque strong{font-family:var(--c5-mono);font-size:.86rem;}
.aqm-c5-ficha{list-style:none;margin:0 0 .6rem;padding:0;font-size:.82rem;color:var(--c5-legenda);line-height:1.5;}
.aqm-c5-ficha li{margin:0;}
.aqm-c5-ficha b{font-family:var(--c5-mono);font-weight:600;color:var(--c5-tinta);}
.aqm-c5-loja{display:inline-block;font-family:var(--c5-texto);font-weight:600;font-size:.88rem;padding:.45rem .9rem;border-radius:2px;background:var(--c5-lamina);color:var(--c5-superficie);text-decoration:none;}
.aqm-c5-loja:hover{filter:brightness(1.08);color:var(--c5-superficie);}
.aqm-c5-semloja{font-size:.82rem;color:var(--c5-legenda);font-style:italic;}
.aqm-c5-voltaviso{font-size:.82rem;color:var(--c5-alerta);font-weight:600;margin:.4rem 0 0;line-height:1.45;}
.aqm-c5-aviso-afiliado{background:var(--c5-papel);border:1px solid var(--c5-traco);border-left:3px solid var(--c5-alerta);border-radius:2px;padding:.8rem 1rem;font-size:.86rem;line-height:1.5;color:var(--c5-legenda);margin:1rem 0 0;}
.aqm-c5-aviso-afiliado strong{color:var(--c5-tinta);}
.aqm-c5-citar{background:var(--c5-papel);border:1px dashed var(--c5-traco);border-radius:3px;padding:.85rem 1rem;font-size:.9rem;line-height:1.5;margin:0 0 1rem;}
.aqm-c5-citar p{margin:0 0 .6rem;}
.aqm-c5-rolagem{overflow-x:auto;-webkit-overflow-scrolling:touch;}
.aqm-c5-fontes{width:100%;min-width:32rem;font-size:.86rem;border-collapse:collapse;margin:.4rem 0 0;}
.aqm-c5-fontes th,.aqm-c5-fontes td{border:1px solid var(--c5-traco);padding:.45rem .6rem;text-align:left;vertical-align:top;}
.aqm-c5-fontes th{background:var(--c5-papel);font-family:var(--c5-display);font-size:.8rem;}
.aqm-c5-fontes td:first-child{font-family:var(--c5-mono);font-size:.8rem;white-space:nowrap;}
.aqm-c5-selo{display:inline-block;font-family:var(--c5-mono);font-size:.66rem;letter-spacing:.08em;text-transform:uppercase;color:var(--c5-alerta);border:1px solid var(--c5-alerta);border-radius:2px;padding:.1rem .35rem;}
.aqm-c5-adiante ul{margin:.5rem 0 0;padding-left:1.1rem;}
.aqm-c5-adiante li{margin:0 0 .4rem;font-size:.94rem;line-height:1.5;}
.aqm-c5-direta{background:var(--c5-papel);border-left:3px solid var(--c5-lamina);border-radius:0 3px 3px 0;padding:1.05rem 1.25rem;margin:0 0 1.2rem;}
.aqm-c5-direta p{font-size:.94rem;line-height:1.62;margin:0 0 .75rem;color:var(--c5-tinta);}
.aqm-c5-direta p:last-child{margin-bottom:0;}
.aqm-c5-direta .aqm-c5-destaque{font-size:1.06rem;line-height:1.5;}
.aqm-c5-direta .aqm-c5-destaque strong{font-family:var(--c5-display);}
.aqm-c5-exemplos .aqm-c5-fontes td{font-size:.84rem;}
.aqm-c5-exemplos .aqm-c5-fontes td:first-child{font-weight:600;color:var(--c5-tinta);}
.aqm-c5-exemplos .aqm-c5-fontes{min-width:52rem;}
.aqm-c5-prod{display:block;font-weight:600;color:var(--c5-tinta);font-size:.86rem;line-height:1.35;}
a.aqm-c5-prod{color:var(--c5-lamina);text-decoration:underline;}
.aqm-c5-sem{display:block;color:var(--c5-legenda);font-size:.78rem;line-height:1.45;}
.aqm-c5-num{font-family:var(--c5-mono);font-variant-numeric:tabular-nums;white-space:nowrap;}
.aqm-c5-wl{display:block;color:var(--c5-legenda);font-family:var(--c5-texto);font-size:.76rem;}
.aqm-c5-oculto{display:none;}
.aqm-c5-promessa{font-family:var(--c5-display);font-size:1.02rem;line-height:1.5;color:var(--c5-tinta);border-left:3px solid var(--c5-lamina);padding:.15rem 0 .15rem .8rem;margin:0 0 1.1rem;}
.aqm-c5-vitrine{margin:1rem 0 0;}
.aqm-c5-vitrine h4{font-family:var(--c5-display);font-size:.95rem;margin:0 0 .15rem;}
.aqm-c5-vt-trilho{display:flex;gap:.8rem;margin:.7rem 0 0;padding:.15rem .15rem .9rem;list-style:none;overflow-x:auto;-webkit-overflow-scrolling:touch;scroll-snap-type:x mandatory;scroll-padding-left:.15rem;}
.aqm-c5-vt-item{flex:0 0 13.5rem;margin:0;scroll-snap-align:start;}
.aqm-c5-vt-cartao{display:flex;flex-direction:column;gap:.28rem;height:100%;background:var(--c5-superficie);border:1px solid var(--c5-traco);border-radius:3px;padding:.7rem .75rem .8rem;text-decoration:none;color:var(--c5-tinta);}
a.aqm-c5-vt-cartao:hover{border-color:var(--c5-lamina);color:var(--c5-tinta);}
a.aqm-c5-vt-cartao:focus-visible{outline:2px solid var(--c5-lamina);outline-offset:1px;}
.aqm-c5-vt-foto{display:flex;align-items:center;justify-content:center;aspect-ratio:1/1;width:100%;max-width:100%;background:var(--c5-papel);border:1px solid var(--c5-traco);border-radius:2px;overflow:hidden;margin:0 0 .35rem;}
.aqm-c5-vt-foto img{display:block;width:100%;height:100%;max-width:100%;object-fit:contain;}
.aqm-c5-vt-foto-vazia .aqm-c5-vt-sigla{font-family:var(--c5-display);font-size:1rem;font-weight:700;color:var(--c5-legenda);letter-spacing:.02em;text-align:center;padding:0 .4rem;}
.aqm-c5-vt-marca{font-family:var(--c5-mono);font-size:.66rem;letter-spacing:.1em;text-transform:uppercase;color:var(--c5-legenda);}
.aqm-c5-vt-modelo{font-family:var(--c5-display);font-size:.92rem;font-weight:700;line-height:1.25;}
.aqm-c5-vt-espec{font-family:var(--c5-mono);font-size:.76rem;line-height:1.4;color:var(--c5-lamina);font-variant-numeric:tabular-nums;}
.aqm-c5-vt-ressalva{font-family:var(--c5-texto);font-size:.74rem;line-height:1.35;color:var(--c5-alerta);}
.aqm-c5-vt-preco{font-family:var(--c5-mono);font-size:.8rem;font-variant-numeric:tabular-nums;color:var(--c5-tinta);}
.aqm-c5-vt-preco.aqm-c5-vt-sem-preco{font-family:var(--c5-texto);font-size:.76rem;color:var(--c5-legenda);font-style:italic;}
.aqm-c5-vt-botao{margin-top:auto;text-align:center;font-family:var(--c5-texto);font-weight:600;font-size:.85rem;padding:.42rem .7rem;border-radius:2px;background:var(--c5-lamina);color:var(--c5-superficie);}
.aqm-c5-vt-espera{margin-top:auto;text-align:center;font-family:var(--c5-texto);font-weight:600;font-size:.82rem;padding:.42rem .7rem;border-radius:2px;background:var(--c5-papel);border:1px dashed var(--c5-traco);color:var(--c5-legenda);}
.aqm-c5-vt-selo{font-family:var(--c5-mono);font-size:.62rem;letter-spacing:.06em;text-transform:uppercase;color:var(--c5-legenda);text-align:center;margin-top:.25rem;}
.aqm-c5-vitrine-servida .aqm-c5-criterio{margin-top:.5rem;}
.aqm-c5-barra{position:fixed;left:0;right:0;bottom:0;z-index:40;display:none;align-items:center;gap:.7rem;background:var(--c5-superficie);border-top:1px solid var(--c5-traco);padding:.55rem .85rem;}
.aqm-c5-barra-texto{flex:1 1 auto;font-family:var(--c5-mono);font-size:.8rem;line-height:1.3;color:var(--c5-tinta);font-variant-numeric:tabular-nums;}
.aqm-c5-barra-botao{flex:0 0 auto;}
@media (max-width:600px){.aqm-c5-valor{font-size:1.6rem;}
.aqm-c5-produto{grid-template-columns:1fr;}
.aqm-c5-vt-item{flex-basis:11.5rem;}
.aqm-c5-barra.aqm-c5-barra-ver{display:flex;}
.aqm-c5-placa{min-height:0;flex-direction:row;gap:.5rem;align-items:baseline;justify-content:flex-start;}}
@media (prefers-reduced-motion:reduce){.aqm-c5-vt-trilho{scroll-behavior:auto;}}
CSS;
}
}

/* ---------------------------------------------------------------------------
 * 4. Comportamento (todo o cálculo mora aqui)
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c5_js' ) ) {
function aquametria_c5_js() {
	return <<<'JS'
(function () {
	'use strict';

	var CHAVE = 'aquametria.aquario';
	var DELTA_COBERTO = 10;   /* wl-delta-ate-10: a fonte declarou até 10 °C */

	/* As regras de bolso do corpus, cada uma com a condição que o PRÓPRIO autor
	   declarou. Não há média entre elas: a faixa vai do menor W/L aplicável ao
	   maior, e cada extremo carrega o nome de quem o publicou.
	   'sempre' = o autor não declarou condição nenhuma — que é justamente o
	   problema que esta calculadora existe para expor. */
	/* As regras de bolso do corpus, cada uma com a condição que o PRÓPRIO autor
	   declarou, e a linha comercial de referência. Desde 09/09/2026 as duas NÃO
	   são escritas aqui: vêm do PHP (aquametria_c5_regras() e
	   aquametria_c5_linha_comercial()) pelas variáveis impressas no rodapé. O
	   motivo é a tabela de exemplos pré-renderizada, que precisa das mesmas
	   regras — e duas cópias das mesmas regras divergem em silêncio.
	   Não há média entre elas: a faixa vai do menor W/L aplicável ao maior, e
	   cada extremo carrega o nome de quem o publicou. 'sempre' quer dizer que o
	   autor não declarou condição nenhuma — que é o problema desta página. */
	var REGRAS = (typeof AQM_C5_REGRAS !== 'undefined') ? AQM_C5_REGRAS : null;
	var LINHA = (typeof AQM_C5_LINHA !== 'undefined') ? AQM_C5_LINHA : null;
	if (!REGRAS || !REGRAS.length || !LINHA || !LINHA.length) { return; }

	var ESPECIES = [
		{ id: 'betta', nome: 'Betta', t: [24, 28], fonte: 'Petz' },
		{ id: 'kinguio', nome: 'Kinguio', t: [18, 24], fonte: 'Petz' },
		{ id: 'guppy', nome: 'Guppy', t: [23, 26], fonte: 'Petz' },
		{ id: 'acara-disco', nome: 'Acará-disco', t: [26, 30], fonte: 'Petz' },
		{ id: 'tetra', nome: 'Tetra', t: [26, 30], fonte: 'Petz' },
		{ id: 'acara-bandeira', nome: 'Acará-bandeira', t: [24, 28], fonte: 'Petz' },
		{ id: 'barbo-sumatra', nome: 'Barbo-sumatra', t: [20, 28], fonte: 'Aquarismo Paulista' },
		{ id: 'paulistinha', nome: 'Paulistinha', t: [18, 28], fonte: 'Aquarismo Paulista' }
	];

	var raiz = document.querySelector('.aqm-c5');
	if (!raiz) { return; }

	function el(id) { return raiz.querySelector('#' + id); }

	function num(v) {
		if (v === null || v === undefined) { return null; }
		var t = String(v).trim().replace(/\s/g, '').replace(',', '.');
		if (t === '') { return null; }
		var n = parseFloat(t);
		return isFinite(n) ? n : null;
	}

	function fmt(n, casas) {
		if (n === null || n === undefined || !isFinite(n)) { return '—'; }
		return n.toLocaleString('pt-BR', { minimumFractionDigits: casas, maximumFractionDigits: casas });
	}

	/* Watts é número grosso: arredondar para 5 W evita a falsa precisão de
	   "137,5 W" numa conta que vem de regra de bolso. */
	function watts(n) {
		if (n === null || !isFinite(n)) { return '—'; }
		return fmt(Math.round(n / 5) * 5, 0);
	}

	function litros(n) {
		if (n === null || !isFinite(n)) { return '—'; }
		return n >= 100 ? fmt(Math.round(n), 0) : fmt(Math.round(n * 10) / 10, 1);
	}

	function graus(n) {
		if (n === null || !isFinite(n)) { return '—'; }
		return fmt(Math.round(n * 10) / 10, 1);
	}

	function especiePorId(id) {
		for (var i = 0; i < ESPECIES.length; i++) {
			if (ESPECIES[i].id === id) { return ESPECIES[i]; }
		}
		return null;
	}

	function campos() {
		var esp = el('aqm-c5-especie').value;
		return {
			volume: num(el('aqm-c5-volume').value),
			especie: esp,
			alvo: num(el('aqm-c5-alvo').value),
			minima: num(el('aqm-c5-minima').value),
			sul: el('aqm-c5-sul').checked,
			tampado: el('aqm-c5-tampado').value,
			voltagem: el('aqm-c5-voltagem').value
		};
	}

	/* --------------------------------------------------------------- alvo */

	/* A temperatura-alvo vem da ficha da espécie, quando há espécie escolhida, e
	   é o MEIO da faixa publicada — que é convenção da Aquametria, declarada na
	   tela, e não constante com fonte. Quem digita o alvo manda sobre a ficha. */
	function resolverAlvo(d) {
		if (d.alvo !== null) {
			return { valor: d.alvo, origem: 'manual' };
		}
		var esp = especiePorId(d.especie);
		if (esp) {
			return {
				valor: (esp.t[0] + esp.t[1]) / 2,
				origem: 'especie',
				especie: esp
			};
		}
		return { valor: null, origem: 'nenhuma' };
	}

	/* ------------------------------------------------------------- o cálculo */

	function calcular(d) {
		var r = { erros: [], avisos: [], editoriais: [] };

		if (d.volume === null) {
			r.erros.push({ campo: 'volume', texto: 'Informe o volume real de água do aquário, em litros.' });
		} else if (d.volume <= 0) {
			r.erros.push({ campo: 'volume', texto: 'O volume precisa ser maior que zero.' });
		} else if (d.volume > 20000) {
			r.erros.push({ campo: 'volume', texto: 'Acima de 20 000 L: confira a unidade (o campo é em litros).' });
		}

		var alvo = resolverAlvo(d);
		if (alvo.valor === null) {
			r.erros.push({ campo: 'alvo', texto: 'Escolha uma espécie ou digite a temperatura-alvo, em graus Celsius.' });
		} else if (alvo.valor < 10 || alvo.valor > 40) {
			r.erros.push({ campo: 'alvo', texto: 'Temperatura-alvo entre 10 e 40 °C. Fora disso, confira a unidade.' });
		}

		if (d.minima === null) {
			r.erros.push({ campo: 'minima', texto: 'Informe a temperatura mínima do cômodo onde o aquário fica, na noite mais fria do ano. É a pergunta que muda tudo — e a que nenhuma outra calculadora faz.' });
		} else if (d.minima < -5 || d.minima > 40) {
			r.erros.push({ campo: 'minima', texto: 'Temperatura mínima do ambiente entre -5 e 40 °C.' });
		}

		if (r.erros.length) { return r; }

		r.entradas = d;
		r.alvo = alvo;
		r.delta = alvo.valor - d.minima;

		if (r.delta <= 0) {
			r.sem_delta = true;
			return r;
		}

		r.delta_coberto = r.delta <= DELTA_COBERTO;

		var V = d.volume;
		r.regras = [];
		REGRAS.forEach(function (g) {
			var vale = (g.quando === 'sempre')
				|| (g.quando === 'delta' && r.delta_coberto)
				|| (g.quando === 'sul' && d.sul);
			if (!vale) {
				r.regras.push({ regra: g, aplicavel: false, motivo: motivoFora(g, r, d) });
				return;
			}
			r.regras.push({
				regra: g, aplicavel: true,
				min: V * g.wl[0], max: V * g.wl[1]
			});
		});

		var aplicaveis = r.regras.filter(function (x) { return x.aplicavel; });
		r.piso = Math.min.apply(null, aplicaveis.map(function (x) { return x.min; }));
		r.teto = Math.max.apply(null, aplicaveis.map(function (x) { return x.max; }));
		r.wl_piso = r.piso / V;
		r.wl_teto = r.teto / V;

		/* Potência comercial: o degrau da linha que cobre o topo da faixa.
		   Escolher o topo é convenção editorial declarada, não constante. */
		r.comercial = LINHA.filter(function (w) { return w >= r.teto; })[0] || null;
		r.comercial_piso = LINHA.filter(function (w) { return w >= r.piso; })[0] || null;
		r.editoriais.push('Entre dois degraus da linha comercial, esta página indica o que cobre o TOPO da faixa. '
			+ 'O motivo: aquecedor subdimensionado trabalha ligado o tempo todo e, na noite mais fria, ainda assim não segura a temperatura; '
			+ 'superdimensionado com termostato que funcione apenas liga menos vezes. É critério editorial da Aquametria, declarado aqui, e não constante com fonte.');

		if (!r.delta_coberto) {
			r.avisos.push('A diferença que você informou é de ' + graus(r.delta) + ' °C, e nenhuma fonte do nosso levantamento cobre esse caso. '
				+ 'A única que amarrou watts por litro a uma diferença de temperatura (ReefFlow) declarou o número para até ' + DELTA_COBERTO + ' °C. '
				+ 'Acima disso, o que sobra são as regras genéricas, que não dizem para qual diferença valem — então a faixa abaixo é um PISO, e pode ser insuficiente. '
				+ 'Extrapolar a regra de bolso para além do delta que a fonte declarou seria inventar constante, e aqui isso não se faz.');
		}

		if (d.tampado === 'nao') {
			r.avisos.push('Aquário destampado perde mais calor, e perde principalmente por evaporação na lâmina livre — que costuma ser a maior parcela da perda. '
				+ 'Não corrigimos o número por isso: a constante que quantificaria essa perda (u-vidro-aquario) está pendente no nosso banco, sem fonte. '
				+ 'Na prática, com o aquário aberto, trate a faixa abaixo como piso e considere o degrau comercial seguinte.');
		}

		if (r.comercial && r.comercial >= 150) {
			r.editoriais.push('Acima de 150 W vale considerar dois aquecedores de metade da potência em vez de um só. '
				+ 'O argumento é modo de falha, não eficiência: termostato que trava ligado num aquecedor de metade da potência aquece menos o aquário, '
				+ 'e termostato que trava desligado deixa o outro segurando alguma coisa. É raciocínio editorial da Aquametria — nenhuma fonte do nosso levantamento publica isso como regra.');
		}

		if (r.alvo.origem === 'especie') {
			r.editoriais.push('A temperatura-alvo veio do meio da faixa que a ficha da espécie publica ('
				+ graus(r.alvo.especie.t[0]) + ' a ' + graus(r.alvo.especie.t[1]) + ' °C, ' + r.alvo.especie.fonte + '). '
				+ 'Mirar no meio de uma faixa publicada é convenção da Aquametria; a faixa é que tem fonte. Se você quer outro ponto dela, digite o alvo.');
		}

		r.produtos = escolher(r, d);
		return r;
	}

	function motivoFora(g, r, d) {
		if (g.quando === 'delta') {
			return 'Vale só até ' + DELTA_COBERTO + ' °C de diferença, e a sua é de ' + graus(r.delta) + ' °C. A fonte não cobre o seu caso.';
		}
		if (g.quando === 'sul') {
			return 'Vale para a região Sul, e você não marcou essa opção.';
		}
		return '';
	}

	/* Adequação técnica, e só ela. Duas barreiras de segurança vêm antes:
	   a voltagem da tomada e a faixa de ajuste alcançar o alvo (regra V18).
	   Link de afiliado não entra no critério nem na ordem (regra V16). */
	function escolher(r, d) {
		var barrados = [];
		var teto = r.comercial || r.teto;
		var dentro = AQM_C5_CATALOGO.filter(function (p) {
			/* A potência vem primeiro, e de propósito: modelo que nunca esteve na
			   faixa não é "barrado", é irrelevante, e listá-lo encheria a tela de
			   ruído. Só quem serviria pela potência merece explicação de por que
			   ficou de fora. */
			if (p.potencia_w < r.piso || p.potencia_w > teto) { return false; }

			if (p.voltagem.indexOf(d.voltagem) === -1) {
				barrados.push(p.marca + ' ' + p.modelo + ' tem a potência certa, mas as fichas que consultamos não o trazem em ' + d.voltagem + ' V.');
				return false;
			}
			if (p.ajuste_max_C !== null && r.alvo.valor > p.ajuste_max_C) {
				barrados.push(p.marca + ' ' + p.modelo + ' tem a potência certa, mas o termostato vai só até '
					+ graus(p.ajuste_max_C) + ' °C' + (p.ajuste_conservador ? ' pela faixa conservadora' : '')
					+ ' e você quer ' + graus(r.alvo.valor) + ' °C.');
				return false;
			}
			if (p.ajuste_min_C !== null && r.alvo.valor < p.ajuste_min_C) {
				barrados.push(p.marca + ' ' + p.modelo + ' tem a potência certa, mas o termostato começa em '
					+ graus(p.ajuste_min_C) + ' °C' + (p.ajuste_conservador ? ' pela faixa conservadora' : '')
					+ ' e você quer ' + graus(r.alvo.valor) + ' °C.');
				return false;
			}
			return true;
		});

		/* A ordem é a distância até o topo da faixa, que é onde a convenção
		   editorial manda mirar. Comissão não ordena nada. */
		dentro.sort(function (a, b) {
			return Math.abs(a.potencia_w - r.teto) - Math.abs(b.potencia_w - r.teto);
		});

		r.barrados = barrados;
		return dentro.slice(0, 5);
	}

	/* ------------------------------------------------------------------ tela */

	function pintar(r) {
		var alvo = el('aqm-c5-saida');
		var ul = el('aqm-c5-erros');
		ul.innerHTML = '';
		raiz.querySelectorAll('.aqm-c5-erro').forEach(function (n) { n.classList.remove('aqm-c5-erro'); });

		if (r.erros && r.erros.length) {
			var vistos = {};
			r.erros.forEach(function (er) {
				var campo = el('aqm-c5-' + er.campo);
				if (campo) { campo.classList.add('aqm-c5-erro'); }
				if (vistos[er.texto]) { return; }
				vistos[er.texto] = true;
				var li = document.createElement('li');
				li.textContent = er.texto;
				ul.appendChild(li);
			});
			alvo.classList.add('aqm-c5-oculto');
			return;
		}

		alvo.classList.remove('aqm-c5-oculto');

		/* Delta zero ou negativo: não há conta de potência a fazer, e dizer isso
		   é mais honesto que devolver um número. */
		var semDelta = el('aqm-c5-semdelta');
		if (r.sem_delta) {
			el('aqm-c5-corpo').classList.add('aqm-c5-oculto');
			semDelta.classList.remove('aqm-c5-oculto');
			semDelta.innerHTML = '<strong>Com os números que você informou, a água nunca cai abaixo da temperatura-alvo.</strong> '
				+ 'A mínima do ambiente (' + graus(r.entradas.minima) + ' °C) é igual ou maior que o alvo (' + graus(r.alvo.valor) + ' °C), '
				+ 'então a diferença de temperatura é zero ou negativa e não existe potência a calcular: nenhuma regra do nosso levantamento dimensiona aquecedor para esse caso. '
				+ 'O que um aquecedor ainda faz aí é segurar a oscilação do dia para a noite, e isso não é conta de watts — é termostato. '
				+ 'Se a sua dúvida é o contrário, ou seja, como impedir que a água passe do alvo no verão, esse é outro problema (resfriamento) e nós ainda não publicamos número sobre ele.';
			/* Sem faixa calculada não há o que a barra do celular prometa: ela
			   ficaria oferecendo "ver o resultado" para uma resposta que é um
			   parágrafo de texto já visível. */
			barraLigada = false;
			mostrarBarra(false);
			guardar(r);
			atualizarEndereco(r.entradas);
			return;
		}
		semDelta.classList.add('aqm-c5-oculto');
		el('aqm-c5-corpo').classList.remove('aqm-c5-oculto');

		el('aqm-c5-faixa-valor').innerHTML = watts(r.piso) + ' a ' + watts(r.teto) + '<span class="aqm-c5-unidade">W</span>';
		el('aqm-c5-faixa-criterio').textContent =
			'São ' + fmt(r.wl_piso, 2) + ' a ' + fmt(r.wl_teto, 2) + ' watts por litro aplicados aos ' + litros(r.entradas.volume) + ' L de água. '
			+ (r.delta_coberto
				? 'A faixa é larga porque as fontes brasileiras discordam entre si — e porque só uma delas diz para qual diferença de temperatura o número dela vale.'
				: 'Trate esta faixa como piso: a sua diferença de temperatura está fora do que a única fonte com delta declarado cobre.');

		el('aqm-c5-delta').innerHTML =
			'<span>alvo <b>' + graus(r.alvo.valor) + ' °C</b></span>'
			+ '<span>mínima do cômodo <b>' + graus(r.entradas.minima) + ' °C</b></span>'
			+ '<span>diferença <b>' + graus(r.delta) + ' °C</b></span>'
			+ '<span>potência comercial <b>' + (r.comercial ? fmt(r.comercial, 0) + ' W' : 'acima da linha') + '</b></span>';

		var lista = el('aqm-c5-regras');
		lista.innerHTML = '';
		r.regras.forEach(function (x) {
			var g = x.regra;
			if (x.aplicavel) {
				lista.appendChild(cartao(
					g.rotulo,
					(x.min === x.max ? watts(x.min) : watts(x.min) + ' a ' + watts(x.max)) + '<span class="aqm-c5-unidade">W</span>',
					g.nota + ' Fonte: ' + g.fonte + ', do nosso levantamento de setembro de 2026.',
					false
				));
			} else {
				lista.appendChild(cartao(
					g.rotulo + ' — não se aplica',
					'<span class="aqm-c5-vazio">fora do caso</span>',
					x.motivo + ' Ela aparece aqui porque saber qual regra NÃO vale para você é parte da resposta.',
					true
				));
			}
		});

		el('aqm-c5-comercial').innerHTML = r.comercial
			? '<strong>Na prateleira, isso vira um aquecedor de ' + fmt(r.comercial, 0) + ' W.</strong> '
				+ 'Aquecedor não se vende em qualquer potência: a linha comercial tem degraus (' + LINHA.join(', ') + ' W), '
				+ 'e o degrau que cobre o topo da sua faixa é o de ' + fmt(r.comercial, 0) + ' W'
				+ (r.comercial_piso && r.comercial_piso !== r.comercial
					? ' — o de ' + fmt(r.comercial_piso, 0) + ' W cobre só o piso dela.'
					: '.')
			: '<strong>A sua faixa passa do maior degrau da linha comercial de referência (' + LINHA[LINHA.length - 1] + ' W).</strong> '
				+ 'Aquário desse tamanho normalmente é aquecido por mais de um aparelho, ou por aquecedor externo em linha, que é outra categoria de produto e ainda não está no nosso banco.';

		el('aqm-c5-confronto').innerHTML =
			'<strong>Não use o volume que vem na caixa do aquecedor para dimensionar.</strong> '
			+ 'A Eheim declara o modelo de 200 W para aquários de 30 a 400 L: uma faixa de 13 vezes, ou de 0,5 a 6,7 W por litro dentro de um mesmo produto. '
			+ 'Na mesma linha, o 25 W é declarado para 25 L, o 50 W para 50 L, o 100 W para 100 L e o 150 W para 150 L — exatamente 1,0 W/L, que é a regra de bolso brasileira. '
			+ 'E há ficha de varejo brasileiro que declara o mesmo 150 W para 200 a 300 L, ou seja, metade disso. '
			+ 'O volume da embalagem serve para escolher entre dois modelos parecidos; ele não sabe quanto frio faz no seu quarto, e é por isso que esta página pergunta.';

		var av = el('aqm-c5-avisos');
		av.innerHTML = '';
		(r.avisos || []).forEach(function (t) {
			var li = document.createElement('li');
			li.textContent = t;
			av.appendChild(li);
		});

		var ed = el('aqm-c5-editoriais');
		ed.innerHTML = '';
		(r.editoriais || []).forEach(function (t) {
			var li = document.createElement('li');
			li.className = 'aqm-c5-criterio';
			li.style.margin = '.35rem 0 0';
			li.textContent = t;
			ed.appendChild(li);
		});

		pintarProdutos(r);

		el('aqm-c5-citacao').textContent =
			'Aquário de ' + litros(r.entradas.volume) + ' L de água real, alvo de ' + graus(r.alvo.valor)
			+ ' °C e mínima de ' + graus(r.entradas.minima) + ' °C no cômodo — diferença de ' + graus(r.delta) + ' °C: '
			+ 'a potência de aquecedor pedida vai de ' + watts(r.piso) + ' a ' + watts(r.teto) + ' W conforme a fonte, '
			+ 'o que na linha comercial vira ' + (r.comercial ? fmt(r.comercial, 0) + ' W' : 'mais de um aparelho')
			+ '. Calculado pela Aquametria, ' + AQM_C5_DATA + '.';

		armarBarra(r);
		guardar(r);
		atualizarEndereco(r.entradas);
	}

	function cartao(rotulo, valor, criterio, fora) {
		var li = document.createElement('li');
		li.className = 'aqm-c5-cartao' + (fora ? ' aqm-c5-cartao-fora' : '');
		var r = document.createElement('span');
		r.className = 'aqm-c5-rotulo';
		r.textContent = rotulo;
		var v = document.createElement('span');
		v.className = 'aqm-c5-valor';
		v.innerHTML = valor;
		var c = document.createElement('p');
		c.className = 'aqm-c5-criterio';
		c.textContent = criterio;
		li.appendChild(r); li.appendChild(v); li.appendChild(c);
		return li;
	}

	/* ------------------------------------------------------------- produtos */

	function pintarProdutos(r) {
		var bloco = el('aqm-c5-produtos');
		var lista = el('aqm-c5-produtos-lista');
		var nada = el('aqm-c5-produtos-nada');
		lista.innerHTML = '';

		if (!r.produtos.length) {
			bloco.classList.add('aqm-c5-oculto');
			el('aqm-c5-vitrine').classList.add('aqm-c5-oculto');
			nada.classList.remove('aqm-c5-oculto');
			nada.textContent = 'Nenhum aquecedor do nosso banco entrega entre ' + watts(r.piso) + ' e '
				+ (r.comercial ? fmt(r.comercial, 0) : watts(r.teto)) + ' W em tomada de ' + r.entradas.voltagem
				+ ' V com termostato que alcance ' + graus(r.alvo.valor) + ' °C'
				+ (r.barrados.length ? ', e ' + r.barrados.length + ' modelo(s) tinham a potência certa mas foram barrados pela voltagem ou pela faixa de ajuste' : '')
				+ '. O banco tem ' + AQM_C5_CATALOGO.length + ' aquecedor(es) com ficha completa hoje e cresce a cada coleta. '
				+ 'Preferimos não mostrar produto nenhum a mostrar um que não atende o seu número — ou pior, que não liga na sua tomada.';
			if (r.barrados.length) {
				nada.textContent += ' Fora da lista: ' + r.barrados.join(' ');
			}
			return;
		}

		nada.classList.add('aqm-c5-oculto');
		bloco.classList.remove('aqm-c5-oculto');
		el('aqm-c5-produtos-sub').textContent =
			'São os aquecedores do nosso banco que entregam entre ' + watts(r.piso) + ' e '
			+ (r.comercial ? fmt(r.comercial, 0) : watts(r.teto)) + ' W, existem em ' + r.entradas.voltagem
			+ ' V e têm termostato capaz de chegar aos ' + graus(r.alvo.valor) + ' °C que você quer. '
			+ 'A ordem é pela proximidade do topo da faixa. Nada aqui é ordenado por comissão, e modelo sem link de loja aparece do mesmo jeito.';

		/* DOIS GRUPOS, e o segundo tem título e frase próprios.
		   Item 2 do despacho da Sentinela de 10/09/2026: com 108 L a faixa
		   publicada era 110 a 160 W e o grupo intitulado "Aquecedores que atendem
		   essa potência" trazia o Atman AT-200 e o Eheim Jäger 200 W, cujos
		   próprios cartões diziam "entrega 1,85 W por litro, contra os 1,00 a 1,50
		   que a sua diferença pede". A elegibilidade estava CERTA — aquecedor não
		   se vende em 160 W, e o teto da lista é de propósito o degrau comercial
		   que cobre o topo da faixa, coisa que a própria página anuncia duas telas
		   acima ("na prateleira, isso vira um aquecedor de 200 W"). Errado estava o
		   RÓTULO: um título dizendo "atendem essa potência" sobre um aparelho que a
		   linha ao lado declara fora da faixa é contradição na cara do leitor, e
		   contradição custa a confiança que separa a Aquametria de uma fazenda de
		   conteúdo. Então a lista se parte: primeiro quem cabe dentro da faixa
		   calculada, depois o degrau comercial acima, com o nome dele e a razão de
		   estar ali. A ordem DENTRO de cada grupo não muda — continua sendo a
		   distância até o topo da faixa, e comissão não ordena nada. */
		var dentro = [];
		var acima  = [];
		r.produtos.forEach(function (p) {
			(p.potencia_w > r.teto ? acima : dentro).push(p);
		});

		/* A sequência que a lista técnica vai desenhar, em uma variável só, para
		   a vitrine copiá-la em vez de recalculá-la. Recalcular a mesma ordem em
		   dois lugares é combinar de divergir depois — e aqui divergir significa
		   um cartão com foto e botão de loja aparecendo antes de quem a ficha
		   técnica pôs na frente, que é a definição de fazenda de conteúdo. */
		var sequencia = dentro.map(function (p) { return { p: p, acima: false }; })
			.concat(acima.map(function (p) { return { p: p, acima: true }; }));

		/* A vitrine vem ANTES da ficha e antes da procedência: contrato 7. */
		pintarVitrine(r, sequencia);

		if (dentro.length && acima.length) {
			lista.appendChild(grupoHtml('Dentro da faixa calculada — ' + watts(r.piso) + ' a ' + watts(r.teto) + ' W',
				'Cada um destes entrega, no seu volume, um número de watts por litro que cai dentro da faixa que as fontes sustentam.'));
		}
		dentro.forEach(function (p) {
			lista.appendChild(produtoHtml(p, r, false));
		});

		if (acima.length) {
			lista.appendChild(grupoHtml(
				dentro.length
					? 'O degrau comercial acima — ' + fmt(r.comercial, 0) + ' W'
					: 'Só o degrau comercial acima — ' + fmt(r.comercial, 0) + ' W',
				'Aquecedor não se vende em qualquer potência. O topo da sua faixa é ' + watts(r.teto)
					+ ' W e a prateleira não tem esse número: o degrau seguinte da linha de referência é o de '
					+ fmt(r.comercial, 0) + ' W, e é por isso que ele aparece aqui. '
					+ (dentro.length
						? 'Ele entrega MAIS watts por litro do que a faixa pede, e por isso vem depois dos que cabem dentro dela — '
						: 'Ele entrega mais watts por litro do que a faixa pede, e é o único caminho na prateleira para o seu número — ')
					+ 'sobra de potência num aquecedor com termostato significa que ele fica menos tempo ligado, '
					+ 'não que a água fique mais quente; o que a sobra cobra é o preço e o tamanho do aparelho.'));
		}
		acima.forEach(function (p) {
			lista.appendChild(produtoHtml(p, r, true));
		});

		if (r.barrados.length) {
			var li = document.createElement('li');
			li.className = 'aqm-c5-criterio';
			li.textContent = 'Fora da lista: ' + r.barrados.join(' ');
			lista.appendChild(li);
		}
	}

	/* Cabeçalho de grupo dentro da lista. É <li> porque a lista é <ul>: pendurar
	   um <h4> solto entre <li> seria HTML inválido, e leitor de tela pula o que
	   não está na estrutura da lista. */
	function grupoHtml(titulo, explicacao) {
		var li = document.createElement('li');
		li.className = 'aqm-c5-grupo';
		var h = document.createElement('h4');
		h.textContent = titulo;
		var p = document.createElement('p');
		p.textContent = explicacao;
		li.appendChild(h);
		li.appendChild(p);
		return li;
	}

	function produtoHtml(p, r, acimaDaFaixa) {
		var V = r.entradas.volume;
		var wl = p.potencia_w / V;

		var li = document.createElement('li');
		li.className = 'aqm-c5-produto' + (acimaDaFaixa ? ' aqm-c5-produto-acima' : '');

		var placa = document.createElement('div');
		placa.className = 'aqm-c5-placa';
		placa.innerHTML = '<span class="aqm-c5-marca">' + esc(p.marca) + '</span>'
			+ '<span class="aqm-c5-numero">' + fmt(p.potencia_w, 0) + '</span>'
			+ '<span class="aqm-c5-un">watts</span>';

		var corpo = document.createElement('div');

		var h = document.createElement('h4');
		h.textContent = p.marca + ' ' + p.modelo;
		corpo.appendChild(h);

		var porque = document.createElement('p');
		porque.className = 'aqm-c5-porque';
		porque.innerHTML = 'No seu aquário de ' + litros(V) + ' L, este aquecedor entrega <strong>'
			+ fmt(Math.round(wl * 100) / 100, 2) + ' W por litro</strong>, '
			/* "contra" anuncia desacordo, e é a palavra certa quando o número
			   está dentro da faixa e o leitor está comparando. No degrau comercial
			   acima o desacordo é esperado e já foi explicado no título do grupo:
			   repetir "contra" ali faria a página parecer estar se desdizendo. */
			+ (acimaDaFaixa ? 'acima dos ' : 'contra os ')
			+ fmt(r.wl_piso, 2) + ' a ' + fmt(r.wl_teto, 2) + ' W/L que a sua diferença de '
			+ graus(r.delta) + ' °C pede. '
			+ (p.volume_max_L
				? 'O fabricante declara que ele atende '
					+ (p.volume_min_L ? 'de ' + litros(p.volume_min_L) + ' a ' : 'até ') + litros(p.volume_max_L) + ' L'
					+ (p.volume_max_L >= V && (!p.volume_min_L || p.volume_min_L <= V)
						? ' — o seu volume cabe nessa declaração, mas repare que a declaração não sabe quanto frio faz aí.'
						: ' — o seu volume está fora dessa declaração, e ainda assim a potência bate com a conta. É o problema desta categoria inteira.')
				: 'O fabricante não declara volume atendido para este modelo.');
		corpo.appendChild(porque);

		var ficha = document.createElement('ul');
		ficha.className = 'aqm-c5-ficha';
		var linhas = [
			'Tipo: <b>' + esc(p.tipo) + '</b>',
			'Faixa de ajuste: <b>' + graus(p.ajuste_min_C) + ' a ' + graus(p.ajuste_max_C) + ' °C</b>'
				+ (p.ajuste_conservador
					? ' <span class="aqm-c5-selo">faixa conservadora</span>'
					: ''),
			'Voltagem: <b>' + (p.voltagem.length ? p.voltagem.join(' ou ') + ' V' : 'não declarada') + '</b>'
		];
		if (p.precisao_C) { linhas.push('Precisão declarada: <b>± ' + graus(p.precisao_C) + ' °C</b>'); }
		if (p.comprimento_cm) { linhas.push('Comprimento: <b>' + graus(p.comprimento_cm) + ' cm</b> — confira se cabe deitado ou em pé no seu aquário'); }
		if (p.seco === true) { linhas.push('Desliga sozinho fora da água: <b>sim</b>'); }
		if (p.ajuste_conservador && p.ajuste_derivacao) {
			linhas.push('Por que a faixa é conservadora: ' + esc(p.ajuste_derivacao));
		}
		if (p.conflito_volume) {
			linhas.push('Volume declarado, em conflito entre fontes: ' + esc(p.conflito_volume));
		}
		linhas.push('Ficha conferida em ' + esc(dataBr(p.verificado_em))
			+ (p.fonte_url ? ' — <a href="' + esc(p.fonte_url) + '" target="_blank" rel="noopener nofollow">fonte da especificação</a>' : '')
			+ (p.fonte_status ? ' (' + esc(p.fonte_status) + ')' : ''));
		ficha.innerHTML = linhas.map(function (t) { return '<li>' + t + '</li>'; }).join('');
		corpo.appendChild(ficha);

		if (p.link) {
			var a = document.createElement('a');
			a.className = 'aqm-c5-loja';
			a.href = p.link;
			a.target = '_blank';
			a.rel = 'sponsored noopener';
			a.textContent = 'Ver na ' + (p.loja === 'shopee' ? 'Shopee' : p.loja);
			corpo.appendChild(a);
			var nota = document.createElement('p');
			nota.className = 'aqm-c5-voltaviso';
			nota.textContent = 'Confira a voltagem no anúncio antes de comprar'
				+ (p.voltagem_anuncio ? ': o anúncio que conferimos em 07/09/2026 era da versão de ' + p.voltagem_anuncio + ' V, e você marcou ' + r.entradas.voltagem + ' V.' : '.')
				+ ' A mesma potência é vendida nas duas tomadas e o anúncio pode mudar. Aquecedor na voltagem errada queima — ou, pior, esquenta demais.';
			corpo.appendChild(nota);
			var patro = document.createElement('p');
			patro.className = 'aqm-c5-semloja';
			patro.textContent = 'Link patrocinado. O anúncio não é a nossa fonte técnica; a ficha acima é.';
			corpo.appendChild(patro);
		} else {
			var sem = document.createElement('p');
			sem.className = 'aqm-c5-semloja';
			/* A frase de sempre dizia "ele aparece aqui porque atende ao seu
			   número". Verdade para quem cabe na faixa; mentira para o degrau
			   comercial acima, que aparece justamente porque a prateleira não tem
			   o número da faixa. Uma frase só para os dois casos era a metade
			   errada da contradição do item 2 do despacho de 10/09/2026. */
			sem.textContent = acimaDaFaixa
				? 'Ainda não temos link de loja para este modelo. Ele aparece aqui porque é o degrau comercial que cobre o topo da sua faixa, e nada além disso decide a lista.'
				: 'Ainda não temos link de loja para este modelo. Ele aparece aqui porque atende ao seu número, e é só isso que decide a lista.';
			corpo.appendChild(sem);
		}

		li.appendChild(placa);
		li.appendChild(corpo);
		return li;
	}

	/* ------------------------------------------------------------- vitrine */

	/* Espelho de aquametria_c5_preco_texto(). Cotação com data, nunca preço
	   atual: é o que a seção 7 do contrato permite publicar. */
	function precoTexto(p) {
		if (!p.preco || p.preco.min === null || p.preco.min === undefined) { return ''; }
		var valor = 'R$ ' + fmt(p.preco.min, 2);
		if (p.preco.max > p.preco.min) { valor += ' a R$ ' + fmt(p.preco.max, 2); }
		return valor + (p.preco.loja ? ' na ' + p.preco.loja : '')
			+ ', cotado em ' + dataBr(p.preco.coletado_em);
	}

	/* Espelho de aquametria_c5_modelo_curto(): o cartão já tem linha de marca, e
	   repeti-la no modelo é a cara de cartão gerado por máquina que ninguém leu. */
	function modeloCurto(p) {
		var modelo = p.modelo;
		if (p.voltagem && p.voltagem.length === 1) { modelo += ' (' + p.voltagem[0] + ' V)'; }
		return modelo;
	}

	/* Espelho de aquametria_c5_vt_espec_frase(). A frase MUDA conforme o grupo:
	   dizer "dentro da faixa" sobre o degrau comercial acima seria repetir, em
	   foto e botão de loja, a contradição consertada na 1.4.0. */
	function especFrase(p, r, acimaDaFaixa) {
		var w = fmt(p.potencia_w, 0) + ' W — ';
		if (acimaDaFaixa) {
			return w + 'degrau comercial acima dos ' + watts(r.teto) + ' W do topo';
		}
		return w + 'dentro dos ' + watts(r.piso) + ' a ' + watts(r.teto) + ' W que os '
			+ litros(r.entradas.volume) + ' L pedem';
	}

	/* Espelho de aquametria_c5_vt_ressalva_curta(). */
	function ressalvaCurta(p, V) {
		if (p.volume_max_L === null || p.volume_max_L === undefined || p.volume_max_L >= V) { return ''; }
		return 'a ficha declara até ' + litros(p.volume_max_L) + ' L';
	}

	/* Espelho de aquametria_c5_vitrine_cartao_html(). Mesma marcação, mesmo CSS —
	   duas marcações para o mesmo cartão viram duas aparências. */
	function vitrineCartao(p, r, acimaDaFaixa) {
		var li = document.createElement('li');
		li.className = 'aqm-c5-vt-item';

		var cartao;
		if (p.link) {
			cartao = document.createElement('a');
			cartao.className = 'aqm-c5-vt-cartao';
			cartao.href = p.link;
			cartao.target = '_blank';
			cartao.rel = 'sponsored noopener';
		} else {
			/* Sem link não existe destino, e cartão sem destino não é âncora. O
			   que o contrato proíbe é div com onclick fingindo ser link. */
			cartao = document.createElement('div');
			cartao.className = 'aqm-c5-vt-cartao aqm-c5-vt-sem-link';
		}

		var foto = document.createElement('span');
		if (p.imagem && p.imagem.url) {
			foto.className = 'aqm-c5-vt-foto';
			var img = document.createElement('img');
			img.src = p.imagem.url;
			img.alt = p.imagem.alt || '';
			if (p.imagem.largura && p.imagem.altura) {
				img.width = p.imagem.largura;
				img.height = p.imagem.altura;
			}
			img.loading = 'lazy';
			img.decoding = 'async';
			foto.appendChild(img);
		} else {
			/* Produto sem foto NÃO some da vitrine: espaço reservado neutro. */
			foto.className = 'aqm-c5-vt-foto aqm-c5-vt-foto-vazia';
			foto.setAttribute('aria-hidden', 'true');
			var sigla = document.createElement('span');
			sigla.className = 'aqm-c5-vt-sigla';
			sigla.textContent = p.marca;
			foto.appendChild(sigla);
		}
		cartao.appendChild(foto);

		cartao.appendChild(linha('aqm-c5-vt-marca', p.marca));
		cartao.appendChild(linha('aqm-c5-vt-modelo', modeloCurto(p)));
		cartao.appendChild(linha('aqm-c5-vt-espec', especFrase(p, r, acimaDaFaixa)));

		var ressalva = ressalvaCurta(p, r.entradas.volume);
		if (ressalva) { cartao.appendChild(linha('aqm-c5-vt-ressalva', ressalva)); }

		var preco = precoTexto(p);
		cartao.appendChild(preco
			? linha('aqm-c5-vt-preco', preco)
			: linha('aqm-c5-vt-preco aqm-c5-vt-sem-preco', 'sem cotação coletada'));

		if (p.link) {
			cartao.appendChild(linha('aqm-c5-vt-botao', 'Ver na ' + (p.loja === 'shopee' ? 'Shopee' : p.loja)));
			cartao.appendChild(linha('aqm-c5-vt-selo', 'link patrocinado'));
		} else {
			cartao.appendChild(linha('aqm-c5-vt-espera', 'link de loja em breve'));
			cartao.appendChild(linha('aqm-c5-vt-selo', 'entrou pela ficha técnica, não pelo link'));
		}

		li.appendChild(cartao);
		return li;
	}

	function linha(classe, texto) {
		var s = document.createElement('span');
		s.className = classe;
		s.textContent = texto;
		return s;
	}

	/* A vitrine NUNCA reordena. Ela recebe a MESMA sequência que a lista técnica
	   desenha — primeiro quem cabe na faixa, depois o degrau comercial acima —,
	   e não a ordem crua de r.produtos, que mistura os dois: um aparelho de 200 W
	   pode estar mais perto do topo de 162 W do que um de 100 W, e é por isso que
	   a lista técnica separa os grupos em vez de confiar na distância sozinha. */
	function pintarVitrine(r, sequencia) {
		var bloco = el('aqm-c5-vitrine');
		var trilho = el('aqm-c5-vitrine-trilho');
		trilho.innerHTML = '';

		if (!sequencia.length) {
			bloco.classList.add('aqm-c5-oculto');
			return;
		}

		bloco.classList.remove('aqm-c5-oculto');

		var comLink = 0;
		sequencia.forEach(function (par) {
			if (par.p.link) { comLink += 1; }
			trilho.appendChild(vitrineCartao(par.p, r, par.acima));
		});

		el('aqm-c5-vitrine-nota').textContent = comLink + ' de ' + sequencia.length
			+ ' têm link de loja hoje; os outros aparecem do mesmo jeito, com o lugar do botão reservado — '
			+ 'quem entra é decidido pela ficha técnica, e nunca por ter ou não link.';
	}

	/* ------------------------------------------------- rolagem e barra fixa */

	/* Rola até o resultado, e SÓ quando ele não está à vista. Rolar uma página em
	   que a resposta já está na tela é tirar o leitor do lugar em que ele está —
	   o que a regra pede é não deixar ninguém calculando no escuro. */
	function irParaResultado() {
		var alvo = el('aqm-c5-saida');
		if (!alvo || alvo.classList.contains('aqm-c5-oculto')) { return; }

		var caixa = alvo.getBoundingClientRect();
		var altura = window.innerHeight || document.documentElement.clientHeight;
		if (caixa.top >= 0 && caixa.top < altura * 0.5) { return; }

		var suave = true;
		try {
			suave = !(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
		} catch (erro) { suave = true; }

		try {
			alvo.scrollIntoView({ behavior: suave ? 'smooth' : 'auto', block: 'start' });
		} catch (erro) {
			alvo.scrollIntoView();
		}
	}

	/* A barra do rodapé no celular: existe enquanto o resultado está fora da
	   tela, e some quando ele entra. Quem decide se ela cabe é o CSS (só abaixo
	   de 600 px); aqui só se liga e desliga a classe. */
	var barraLigada = false;
	var observador = null;

	function armarBarra(r) {
		var barra = el('aqm-c5-barra');
		if (!barra) { return; }

		el('aqm-c5-barra-texto').textContent = watts(r.piso) + ' a ' + watts(r.teto) + ' W para '
			+ litros(r.entradas.volume) + ' L';
		barraLigada = true;

		if (observador || typeof window.IntersectionObserver !== 'function') {
			if (!observador) { mostrarBarra(true); }
			return;
		}

		observador = new window.IntersectionObserver(function (entradas) {
			entradas.forEach(function (entrada) {
				mostrarBarra(barraLigada && !entrada.isIntersecting);
			});
		}, { threshold: 0 });
		observador.observe(el('aqm-c5-saida'));
	}

	function mostrarBarra(ver) {
		var barra = el('aqm-c5-barra');
		if (!barra) { return; }
		barra.classList.toggle('aqm-c5-barra-ver', !!ver);
		barra.setAttribute('aria-hidden', ver ? 'false' : 'true');
	}

	function esc(t) {
		return String(t === null || t === undefined ? '' : t)
			.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
	}

	function dataBr(iso) {
		if (!iso) { return 'data não registrada'; }
		var p = String(iso).split('-');
		return p.length === 3 ? p[2] + '/' + p[1] + '/' + p[0] : iso;
	}

	/* ------------------------------------------------- estado compartilhado */

	function recuperar() {
		try {
			var bruto = window.localStorage.getItem(CHAVE);
			if (!bruto) { return null; }
			var o = JSON.parse(bruto);
			return (o && typeof o === 'object') ? o : null;
		} catch (erro) { return null; }
	}

	/* Mescla: a C1 é dona das medidas e dos volumes, e esta calculadora não
	   pode apagar o que ela nem o que a C3 gravaram. Só acrescenta o que é dela. */
	function guardar(r) {
		var estado = recuperar() || { versao: 1, calculadora: 'c5-aquecedor-delta' };
		estado.volumes = estado.volumes || {};
		if (!estado.volumes.real_L || estado.volumes.real_L !== r.entradas.volume) {
			estado.volumes.real_L = r.entradas.volume;
			if (!estado.volumes.origem) { estado.volumes.origem = 'informado na C5'; }
		}
		estado.clima = estado.clima || {};
		estado.clima.temp_alvo_C = r.alvo.valor;
		estado.clima.temp_alvo_origem = r.alvo.origem;
		estado.clima.especie = r.alvo.especie ? r.alvo.especie.id : null;
		estado.clima.temp_min_ambiente_C = r.entradas.minima;
		estado.clima.delta_C = r.delta;
		estado.clima.regiao_sul = !!r.entradas.sul;
		estado.perfil = estado.perfil || {};
		estado.perfil.tampado = r.entradas.tampado;
		estado.eletrica = estado.eletrica || {};
		estado.eletrica.voltagem = r.entradas.voltagem;
		estado.equipamentos = estado.equipamentos || {};
		estado.equipamentos.aquecedor_potencia_alvo_w = r.sem_delta
			? null
			: [Math.round(r.piso), Math.round(r.teto)];
		estado.equipamentos.aquecedor_potencia_comercial_w = r.comercial || null;
		estado.calculado_em = new Date().toISOString().slice(0, 10);

		try {
			window.localStorage.setItem(CHAVE, JSON.stringify(estado));
			el('aqm-c5-guardado').classList.remove('aqm-c5-oculto');
		} catch (erro) {
			el('aqm-c5-guardado').classList.add('aqm-c5-oculto');
		}
	}

	/* ------------------------------------------- permalink e query string */

	function atualizarEndereco(d) {
		var q = ['v=' + d.volume, 'min=' + d.minima, 'volt=' + d.voltagem, 'tp=' + d.tampado];
		if (d.alvo !== null) { q.push('alvo=' + d.alvo); }
		if (d.especie) { q.push('esp=' + d.especie); }
		if (d.sul) { q.push('sul=1'); }
		var url = window.location.pathname + '?' + q.join('&');
		try { window.history.replaceState(null, '', url); } catch (erro) { /* sem history: segue sem permalink */ }
		el('aqm-c5-link').value = window.location.origin + url;
	}

	function lerQuery() {
		var busca = window.location.search;
		if (!busca || busca.length < 2) { return null; }
		var fora = {};
		busca.substring(1).split('&').forEach(function (par) {
			var p = par.split('=');
			if (p.length === 2) { fora[decodeURIComponent(p[0])] = decodeURIComponent(p[1]); }
		});
		return (fora.v && fora.min) ? fora : null;
	}

	/* ------------------------------------ o aquecedor que a pessoa já tem */

	function veredito() {
		var w = num(el('aqm-c5-tenho').value);
		var V = num(el('aqm-c5-volume').value);
		var saida = el('aqm-c5-tenho-saida');

		if (w === null || w <= 0) {
			saida.textContent = 'Informe a potência do aquecedor, em watts — é o número que vem na caixa e no próprio aparelho.';
			return;
		}

		var texto = 'Um aquecedor de ' + fmt(w, 0) + ' W cobre ';
		var partes = [];
		partes.push('até ' + litros(w / 1.5) + ' L pela regra com delta declarado (1,0 a 1,5 W/L até 10 °C de diferença, ReefFlow), no extremo mais exigente dela, e até '
			+ litros(w / 1.0) + ' L no extremo mais folgado');
		partes.push('até ' + litros(w / 2.0) + ' L pela leitura do Sul (2,0 W/L, Casa da Ada)');
		partes.push('até ' + litros(w / 1.3) + ' L pela variante de 1,3 W/L (eHow)');
		texto += partes.join('; ') + '. ';

		if (V !== null && V > 0) {
			var wl = w / V;
			texto += 'No seu aquário de ' + litros(V) + ' L, ele entrega ' + fmt(Math.round(wl * 100) / 100, 2) + ' W por litro — '
				+ (wl < 1.0
					? 'abaixo de todas as regras do nosso levantamento, inclusive da mais folgada.'
					: (wl < 1.5
						? 'dentro da faixa que a única fonte com delta declarado publica para até 10 °C de diferença. Se onde você mora esfria mais que isso, essa fonte não cobre o seu caso.'
						: 'acima de 1,5 W/L, ou seja, folgado até para a leitura do Sul se a diferença de temperatura for grande.'));
		}
		texto += ' Nenhum desses números pergunta quanto frio faz no seu cômodo — o cálculo lá em cima pergunta.';
		saida.textContent = texto;
	}

	/* ---------------------------------------------------------- ligações */

	function preencher(fora) {
		if (fora.v) { el('aqm-c5-volume').value = fora.v; }
		if (fora.min) { el('aqm-c5-minima').value = fora.min; }
		if (fora.alvo) { el('aqm-c5-alvo').value = fora.alvo; }
		if (fora.esp && especiePorId(fora.esp)) { el('aqm-c5-especie').value = fora.esp; }
		if (fora.volt === '110' || fora.volt === '220') { el('aqm-c5-voltagem').value = fora.volt; }
		if (fora.tp === 'sim' || fora.tp === 'nao' || fora.tp === 'nao-sei') { el('aqm-c5-tampado').value = fora.tp; }
		if (fora.sul === '1') { el('aqm-c5-sul').checked = true; }
	}

	/* A ficha da espécie escolhida aparece embaixo do campo, com a fonte, antes
	   mesmo de calcular: é ela que vira o alvo. */
	function mostrarEspecie() {
		var esp = especiePorId(el('aqm-c5-especie').value);
		var d = el('aqm-c5-especie-ficha');
		if (!esp) {
			d.textContent = 'Sem espécie escolhida, digite a temperatura-alvo ao lado.';
			return;
		}
		d.textContent = esp.nome + ': ' + graus(esp.t[0]) + ' a ' + graus(esp.t[1]) + ' °C, segundo ' + esp.fonte
			+ '. Sem alvo digitado, usamos o meio dessa faixa (' + graus((esp.t[0] + esp.t[1]) / 2) + ' °C).';
	}

	el('aqm-c5-form').addEventListener('submit', function (ev) {
		ev.preventDefault();
		pintar(calcular(campos()));
		/* Só no envio explícito. A pintura automática de quem chegou por link ou
		   com o aquário guardado NÃO rola a página: sequestrar a rolagem de quem
		   acabou de abrir a página é o oposto de ajudar. */
		irParaResultado();
	});

	el('aqm-c5-especie').addEventListener('change', mostrarEspecie);

	el('aqm-c5-limpar').addEventListener('click', function () {
		el('aqm-c5-form').reset();
		el('aqm-c5-saida').classList.add('aqm-c5-oculto');
		el('aqm-c5-erros').innerHTML = '';
		barraLigada = false;
		mostrarBarra(false);
		mostrarEspecie();
		try { window.history.replaceState(null, '', window.location.pathname); } catch (erro) { /* segue */ }
	});

	el('aqm-c5-barra-ir').addEventListener('click', function () {
		var alvo = el('aqm-c5-saida');
		if (!alvo || alvo.classList.contains('aqm-c5-oculto')) { return; }
		try {
			alvo.scrollIntoView({ block: 'start' });
		} catch (erro) {
			alvo.scrollIntoView();
		}
	});

	el('aqm-c5-copiar').addEventListener('click', function () {
		var campo = el('aqm-c5-link');
		campo.select();
		var ok = false;
		try { ok = document.execCommand('copy'); } catch (erro) { ok = false; }
		if (!ok && window.navigator && window.navigator.clipboard) {
			window.navigator.clipboard.writeText(campo.value);
			ok = true;
		}
		el('aqm-c5-copiado').textContent = ok ? 'Link copiado.' : 'Selecione e copie o endereço acima.';
	});

	el('aqm-c5-tenho-calcular').addEventListener('click', veredito);

	mostrarEspecie();

	/* Query string manda; senão, o aquário que a C1 guardou neste navegador.
	   Diferente da C3, aqui o volume não basta para calcular: a mínima do
	   ambiente é entrada e ninguém a adivinha. Então preenchemos e esperamos. */
	var daUrl = lerQuery();
	if (daUrl) {
		preencher(daUrl);
		mostrarEspecie();
		pintar(calcular(campos()));
	} else {
		var guardadoAntes = recuperar();
		var volume = guardadoAntes && guardadoAntes.volumes ? guardadoAntes.volumes.real_L : null;
		if (volume) {
			el('aqm-c5-volume').value = String(volume).replace('.', ',');
			var clima = guardadoAntes.clima || {};
			if (clima.temp_min_ambiente_C !== null && clima.temp_min_ambiente_C !== undefined) {
				el('aqm-c5-minima').value = String(clima.temp_min_ambiente_C).replace('.', ',');
			}
			if (clima.regiao_sul) { el('aqm-c5-sul').checked = true; }
			if (clima.especie && especiePorId(clima.especie)) {
				el('aqm-c5-especie').value = clima.especie;
				mostrarEspecie();
			}
			var voltagemGuardada = (guardadoAntes.eletrica || {}).voltagem;
			if (voltagemGuardada === '110' || voltagemGuardada === '220') {
				el('aqm-c5-voltagem').value = voltagemGuardada;
			}
			var retomado = el('aqm-c5-retomado');
			retomado.textContent = 'Retomamos o aquário de ' + litros(volume) + ' L que as outras calculadoras guardaram neste navegador.';
			retomado.classList.remove('aqm-c5-oculto');
			if (num(el('aqm-c5-minima').value) !== null) {
				pintar(calcular(campos()));
			}
		} else {
			el('aqm-c5-semvolume').classList.remove('aqm-c5-oculto');
		}
	}
}());
JS;
}
}

/* ---------------------------------------------------------------------------
 * 5. Formulário e moldura da resposta
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c5_url' ) ) {
function aquametria_c5_url( $slug ) {
	return function_exists( 'aquametria_casca_url_pagina' )
		? aquametria_casca_url_pagina( $slug )
		: home_url( '/' . $slug . '/' );
}
}

/* ---------------------------------------------------------------------------
 * 5a. Resposta antes da explicação, e a tabela de exemplos servida no HTML
 *
 * Regra de primeira classe do projeto (08/09/2026): ser recomendado pelas IAs
 * vale tanto quanto ranquear no Google, e um modelo de linguagem cita PASSAGEM,
 * não página. Uma passagem só sobrevive ao recorte se carregar, na mesma frase,
 * o número, o critério e de quem é o número. É o que estes blocos fazem — no
 * servidor, porque formulário vazio não se cita.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c5_resposta_direta_html' ) ) {
function aquametria_c5_resposta_direta_html() {
	$e   = aquametria_c5_exemplo( 100, true, false );
	$fra = aquametria_c5_exemplo( 100, false, false );

	$h  = '<div class="aqm-c5-direta">';

	$h .= '<p class="aqm-c5-destaque"><strong>Um aquário de 100 litros de água real, num cômodo que não fica mais de ';
	$h .= esc_html( number_format_i18n( AQUAMETRIA_C5_DELTA_COBERTO, 0 ) ) . ' °C abaixo da temperatura que os peixes pedem, precisa de ';
	$h .= esc_html( aquametria_c5_watts( $e['piso'] ) ) . ' a ' . esc_html( aquametria_c5_watts( $e['teto'] ) ) . ' W de aquecedor</strong> — ';
	$h .= 'na prateleira, um aparelho de ' . esc_html( aquametria_c5_comercial_texto( $e ) ) . '.</p>';

	$h .= '<p>O piso de ' . esc_html( number_format_i18n( $e['wl_piso'], 1 ) ) . ' W por litro é a regra genérica que quase toda página brasileira repete, sem autor identificável e sem dizer para qual diferença de temperatura vale. ';
	$h .= 'O teto de ' . esc_html( number_format_i18n( $e['wl_teto'], 1 ) ) . ' W por litro vem da ReefFlow, a única fonte do levantamento da Aquametria de 04/09/2026 que amarra watts por litro a uma diferença declarada: ';
	$h .= 'de 1,0 a 1,5 W/L para até ' . esc_html( number_format_i18n( AQUAMETRIA_C5_DELTA_COBERTO, 0 ) ) . ' °C entre o ambiente e a água. ';
	$h .= 'Entre dois degraus da linha comercial esta página indica o que cobre o TOPO da faixa, e diz que isso é critério editorial declarado, não constante com fonte.</p>';

	$h .= '<p><strong>A pergunta que decide o número não é o volume do aquário: é quanto o cômodo esfria na noite mais fria do ano.</strong> ';
	$h .= 'Acima de ' . esc_html( number_format_i18n( AQUAMETRIA_C5_DELTA_COBERTO, 0 ) ) . ' °C de diferença nenhuma fonte do nosso levantamento cobre o caso — sobram as regras genéricas, ';
	$h .= 'que para os mesmos 100 litros dariam ' . esc_html( aquametria_c5_watts( $fra['piso'] ) ) . ' a ' . esc_html( aquametria_c5_watts( $fra['teto'] ) ) . ' W, ';
	$h .= 'e essa faixa é um PISO que pode ser insuficiente: extrapolar regra de bolso para além do delta que a fonte declarou seria inventar constante. ';
	$h .= 'É a razão de esta calculadora perguntar a temperatura mínima do cômodo, o que nenhuma outra do nicho pergunta.</p>';

	$h .= '<p class="aqm-c5-criterio">O achado que o próprio catálogo do fabricante entrega, e que esta página publica em vez de esconder: ';
	$h .= 'a linha Eheim Jäger tem 25 W para 25 L, 50 W para 50 L, 100 W para 100 L e 150 W para 150 L — ';
	$h .= 'ou seja, o catálogo do fabricante é construído sobre a mesma regra de 1 W/L que a web repete. ';
	$h .= 'E a mesma Eheim declara o Jäger de 200 W para 30 a 400 litros, uma faixa de treze vezes: serve para escolher potência na loja, não para dimensionar (coletado em 07/09/2026).</p>';

	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c5_exemplos_html' ) ) {
function aquametria_c5_exemplos_html() {
	$h  = '<div class="aqm-c5-painel aqm-c5-exemplos">';
	$h .= '<h3>Seis aquários já resolvidos, nos dois cenários de frio</h3>';
	$h .= '<p class="aqm-c5-sub">É a mesma conta do formulário acima, aplicada aos seis volumes mais comuns do comércio brasileiro e aos dois cenários que mudam tudo: ';
	$h .= 'o cômodo que fica até ' . esc_html( number_format_i18n( AQUAMETRIA_C5_DELTA_COBERTO, 0 ) ) . ' °C abaixo da temperatura da água, e o que fica mais que isso. ';
	$h .= 'Estes números estão prontos no HTML desta página — não é preciso preencher nada.</p>';

	$h .= '<div class="aqm-c5-rolagem"><table class="aqm-c5-fontes">';
	$h .= '<tr><th>Volume real</th><th>Até ' . esc_html( number_format_i18n( AQUAMETRIA_C5_DELTA_COBERTO, 0 ) ) . ' °C de diferença</th><th>Na prateleira</th>';
	$h .= '<th>Acima de ' . esc_html( number_format_i18n( AQUAMETRIA_C5_DELTA_COBERTO, 0 ) ) . ' °C</th><th>Na prateleira</th>';
	/* "que atende" prometia mais do que a coluna entrega: em duas das seis linhas
	   o modelo escolhido é o degrau comercial ACIMA do topo da faixa, porque a
	   prateleira não vende o número exato. A própria célula diz isso agora; o
	   cabeçalho para de dizer o contrário. Item 2 do despacho de 10/09/2026. */
	$h .= '<th>Aquecedor do banco para essa faixa</th></tr>';

	foreach ( aquametria_c5_volumes_exemplo() as $v ) {
		$e   = aquametria_c5_exemplo( $v, true, false );
		$fra = aquametria_c5_exemplo( $v, false, false );

		$h .= '<tr>';
		$h .= '<td>' . esc_html( number_format_i18n( $v, 0 ) ) . ' L</td>';

		$h .= '<td><span class="aqm-c5-num">' . esc_html( aquametria_c5_watts( $e['piso'] ) ) . ' a ' . esc_html( aquametria_c5_watts( $e['teto'] ) ) . ' W</span>';
		$h .= '<span class="aqm-c5-wl">' . esc_html( number_format_i18n( $e['wl_piso'], 1 ) ) . ' a ' . esc_html( number_format_i18n( $e['wl_teto'], 1 ) ) . ' W/L</span></td>';
		$h .= '<td><span class="aqm-c5-num">' . esc_html( aquametria_c5_comercial_texto( $e ) ) . '</span></td>';

		$h .= '<td><span class="aqm-c5-num">' . esc_html( aquametria_c5_watts( $fra['piso'] ) ) . ' a ' . esc_html( aquametria_c5_watts( $fra['teto'] ) ) . ' W</span>';
		$h .= '<span class="aqm-c5-wl">' . esc_html( number_format_i18n( $fra['wl_piso'], 1 ) ) . ' a ' . esc_html( number_format_i18n( $fra['wl_teto'], 1 ) ) . ' W/L, e é piso</span></td>';
		$h .= '<td><span class="aqm-c5-num">' . esc_html( aquametria_c5_comercial_texto( $fra ) ) . '</span></td>';

		$h .= aquametria_c5_produto_celula_html( $e );

		$h .= '</tr>';
	}

	$h .= '</table></div>';

	$h .= '<p class="aqm-c5-criterio" style="margin-top:.8rem">Como ler a tabela. ';
	$h .= 'A coluna da esquerda vale quando o cômodo não fica mais de ' . esc_html( number_format_i18n( AQUAMETRIA_C5_DELTA_COBERTO, 0 ) ) . ' °C abaixo da temperatura da água: ';
	$h .= 'aí entra a ReefFlow, a única fonte do levantamento de 04/09/2026 que declarou para qual diferença o número dela vale (1,0 a 1,5 W/L até 10 °C). ';
	$h .= 'A coluna da direita vale acima disso, e nela sobram apenas as regras sem condição declarada — a genérica de 1,0 W/L, repetida sem autoria na web brasileira, e a de 1,3 W/L do eHow. ';
	$h .= 'Por isso ela está marcada como PISO: nenhuma fonte cobre esse caso, e esticar o número da ReefFlow para além dos 10 °C que ela declarou seria inventar constante. ';
	$h .= 'Quem está na região Sul tem ainda uma terceira leitura, de até 2,0 W/L (Casa da Ada) — marque a opção no formulário e a faixa sobe. ';
	$h .= 'Aquário destampado perde mais calor, principalmente por evaporação, e esta página NÃO corrige o número por isso: a constante que quantificaria a perda está pendente, sem fonte. ';
	$h .= 'A partir de 300 litros a faixa passa do maior degrau da linha de referência (300 W), e a resposta honesta é mais de um aparelho — o que também é o mais seguro, por modo de falha do termostato. ';
	$h .= 'Nenhum número desta tabela foi digitado à mão: todos saem das mesmas regras que a calculadora usa, calculados no servidor a cada carregamento.</p>';

	$divulgacao = aquametria_c5_url( AQUAMETRIA_C5_PAGINA_AFILIADOS );

	$h .= '<p class="aqm-c5-aviso-afiliado"><strong>Sobre a última coluna.</strong> ';
	$h .= 'Ela mostra o aquecedor do banco técnico da Aquametria cuja potência cai mais perto do topo da faixa daquela linha, no cenário da coluna da esquerda — ';
	$h .= 'é o mesmo critério que a calculadora acima aplica, e a comissão não entra nele: modelo sem link de loja aparece do mesmo jeito. ';
	$h .= 'Quando esse modelo ainda não tem link no banco, aparece embaixo, rotulada, a opção da MESMA faixa que já tem — o primeiro da mesma ordem, não o de maior comissão. ';
	$h .= '<strong>Leia a voltagem antes de comprar.</strong> A tabela não sabe duas coisas que o formulário pergunta e que decidem segurança: a voltagem da sua tomada e a temperatura que você quer manter. ';
	$h .= 'Aquecedor ligado na voltagem errada queima, e por isso a célula publica a voltagem que a ficha declara — e diz quando ela não está confirmada — em vez de supor 110 ou 220. ';
	$h .= 'A lista definitiva, já com esses dois cortes aplicados, sai depois do cálculo. ';
	$h .= 'Alguns desses nomes levam a lojas por link de afiliado, marcado como patrocinado: se você comprar por ele, a Aquametria pode receber comissão, sem custo a mais para você. ';
	$h .= 'Esta tabela não traz preço: quem traz é a vitrine acima, e sempre como cotação com a data da coleta ao lado, nunca como preço de hoje. ';
	$h .= '<a href="' . esc_url( $divulgacao ) . '">Como a Aquametria ganha dinheiro</a>.</p>';

	$h .= '</div>';
	return $h;
}
}

/* ---------------------------------------------------------------------------
 * 5b. JSON-LD (schema.org)
 *
 * Sai no wp_head, e por isso NUNCA dentro do retorno do shortcode: o retorno do
 * shortcode atravessa os filtros do the_content, que trocariam cada "&" pela
 * entidade numérica dele e quebrariam o JSON. Mesma regra do script, mesmo
 * motivo. Medido em 09/09/2026: a ilha tinha JSON-LD ZERO em 13 de 13 páginas.
 *
 * Dois nós: WebApplication e FAQPage. Cada resposta do FAQ existe, com o mesmo
 * número, na tabela de exemplos servida acima — FAQPage que promete o que a
 * página não mostra é lixo, e seria lixo detectável.
 * ------------------------------------------------------------------------- */

/* A frase de "onde comprar" da resposta do FAQ, quando quem atende melhor ainda
   não tem link. Fica separada porque só existe nesse caso, e escrevê-la dentro
   do array do FAQ deixaria o array ilegível. */
if ( ! function_exists( 'aquametria_c5_faq_com_link' ) ) {
function aquametria_c5_faq_com_link( $e, $volume ) {
	$c = aquametria_c5_produto_com_link( $e );

	if ( null === $c ) {
		return 'Nenhum aquecedor dessa faixa tem link de loja no banco da Aquametria hoje. ';
	}

	$ressalva = aquametria_c5_volume_ressalva( $c, $volume );

	return 'Esse modelo ainda não tem link de loja no banco; na mesma faixa, o primeiro que tem é o '
		. aquametria_c5_produto_frase( $c, $volume ) . '. ' . ( '' === $ressalva ? '' : $ressalva . ' ' );
}
}

if ( ! function_exists( 'aquametria_c5_jsonld_dados' ) ) {
function aquametria_c5_jsonld_dados() {
	$url    = aquametria_c5_url( AQUAMETRIA_C5_SLUG );
	$artigo = aquametria_c5_url( AQUAMETRIA_C5_ARTIGO );

	$editora = array(
		'@type' => 'Organization',
		'name'  => 'Aquametria',
		'url'   => home_url( '/' ),
	);

	$app = array(
		'@type'                  => 'WebApplication',
		'@id'                    => $url . '#calculadora',
		'name'                   => 'Calculadora de potência do aquecedor de aquário',
		'alternateName'          => 'Aquametria C5 — quantos watts de aquecedor',
		'url'                    => $url,
		'inLanguage'             => 'pt-BR',
		'applicationCategory'    => 'UtilitiesApplication',
		'applicationSubCategory' => 'Calculadora de dimensionamento de aquário',
		'operatingSystem'        => 'Qualquer navegador com JavaScript',
		'browserRequirements'    => 'Requer JavaScript. O cálculo roda no navegador e nenhum dado é enviado a servidor.',
		'isAccessibleForFree'    => true,
		'offers'                 => array(
			'@type'         => 'Offer',
			'price'         => '0',
			'priceCurrency' => 'BRL',
		),
		'softwareVersion' => AQUAMETRIA_C5_VERSAO,
		'description'     => 'Converte o volume real de água e a temperatura mínima do cômodo na faixa de potência de aquecedor que o aquário pede, em watts, '
			. 'e no degrau da linha comercial que a cobre. É a única calculadora do nicho no Brasil que pergunta quanto frio faz onde o aquário está: '
			. 'toda a web repete 1 W por litro sem dizer para qual diferença de temperatura o número vale, e a diferença é o que decide a conta.',
		'featureList' => array(
			'Faixa de potência em watts a partir do volume real e da temperatura mínima do cômodo',
			'Cada regra de watts por litro com a condição que o próprio autor declarou',
			'Aviso explícito quando a diferença de temperatura passa dos 10 °C que a única fonte com delta declarou',
			'Temperatura-alvo a partir da ficha de 8 espécies, com fonte',
			'Degrau da linha comercial que cobre o topo da faixa',
			'Caminho inverso: o aquecedor que você já tem serve para quantos litros',
			'Barreira de voltagem e de faixa de ajuste antes de sugerir qualquer aparelho',
			'Tabela pré-calculada para 30, 60, 100, 150, 200 e 300 litros, nos dois cenários de frio',
			'Aquecedor do banco indicado para cada um desses seis volumes, já no HTML servido',
		),
		'publisher'  => $editora,
		'isBasedOn'  => 'Levantamento de fontes brasileiras da Aquametria, 04/09/2026, e fichas de fabricante coletadas em 07/09/2026',
		'mainEntityOfPage' => $artigo,
	);

	$perguntas = array();
	foreach ( aquametria_c5_volumes_exemplo() as $v ) {
		$e   = aquametria_c5_exemplo( $v, true, false );
		$fra = aquametria_c5_exemplo( $v, false, false );

		$perguntas[] = array(
			'@type' => 'Question',
			'name'  => 'Quantos watts de aquecedor para um aquário de ' . number_format_i18n( $v, 0 ) . ' litros?',
			'acceptedAnswer' => array(
				'@type' => 'Answer',
				'text'  => 'Um aquário de ' . number_format_i18n( $v, 0 ) . ' litros de água real, num cômodo que não fica mais de '
					. number_format_i18n( AQUAMETRIA_C5_DELTA_COBERTO, 0 ) . ' °C abaixo da temperatura da água, pede de '
					. aquametria_c5_watts( $e['piso'] ) . ' a ' . aquametria_c5_watts( $e['teto'] ) . ' W — na prateleira, '
					. aquametria_c5_comercial_texto( $e ) . '. '
					. 'O piso de ' . number_format_i18n( $e['wl_piso'], 1 ) . ' W/L é a regra genérica repetida sem autoria pela web brasileira; '
					. 'o teto de ' . number_format_i18n( $e['wl_teto'], 1 ) . ' W/L vem da ReefFlow, a única fonte do levantamento da Aquametria de 04/09/2026 '
					. 'que declarou para qual diferença de temperatura o número vale (até ' . number_format_i18n( AQUAMETRIA_C5_DELTA_COBERTO, 0 ) . ' °C). '
					. 'Se o cômodo esfriar mais que isso, nenhuma fonte cobre o caso: sobram as regras genéricas, que dariam '
					. aquametria_c5_watts( $fra['piso'] ) . ' a ' . aquametria_c5_watts( $fra['teto'] ) . ' W, e essa faixa é um piso que pode ser insuficiente. '
					. 'O que decide o número não é o volume, é quanto o cômodo esfria na noite mais fria do ano.',
			),
		);
	}

	/* Pergunta de COMPRA, uma por volume. Cada resposta abaixo existe, com o
	   mesmo modelo e a mesma potência, na última coluna da tabela servida. */
	foreach ( aquametria_c5_volumes_exemplo() as $v ) {
		$e = aquametria_c5_exemplo( $v, true, false );
		$p = aquametria_c5_produto_exemplo( $e );

		if ( null === $p ) {
			continue;
		}

		$perguntas[] = array(
			'@type' => 'Question',
			'name'  => 'Qual aquecedor comprar para um aquário de ' . number_format_i18n( $v, 0 ) . ' litros?',
			'acceptedAnswer' => array(
				'@type' => 'Answer',
				'text'  => 'Para um aquário de ' . number_format_i18n( $v, 0 ) . ' litros de água real, num cômodo que não fica mais de '
					. number_format_i18n( AQUAMETRIA_C5_DELTA_COBERTO, 0 ) . ' °C abaixo da temperatura da água, a faixa é de '
					. aquametria_c5_watts( $e['piso'] ) . ' a ' . aquametria_c5_watts( $e['teto'] ) . ' W e o aquecedor do banco técnico da Aquametria '
					. 'que cai mais perto do topo dela é o ' . aquametria_c5_produto_frase( $p, $v ) . '. '
					. ( $e['comercial'] ? '' : 'Atenção: nesse volume a faixa passa do maior degrau da linha de referência (300 W), '
						. 'então a resposta é mais de um aparelho, e esse modelo é um deles. ' )
					. 'O critério é a potência declarada, nunca a comissão: modelo sem link de loja aparece na lista do mesmo jeito. '
					. aquametria_c5_volume_ressalva( $p, $v ) . ( aquametria_c5_volume_ressalva( $p, $v ) ? ' ' : '' )
					. ( $p['link'] ? '' : aquametria_c5_faq_com_link( $e, $v ) )
					. 'Antes de comprar, confirme dois números que esta indicação não conhece: a voltagem da sua tomada, porque aquecedor ligado na voltagem errada queima, '
					. 'e se a faixa de ajuste do termostato alcança a temperatura que você quer manter.',
			),
		);
	}

	$perguntas[] = array(
		'@type' => 'Question',
		'name'  => 'A regra de 1 watt por litro para aquecedor de aquário está certa?',
		'acceptedAnswer' => array(
			'@type' => 'Answer',
			'text'  => 'Ela está incompleta, e de um jeito que importa. 1 W por litro é o número que quase toda página brasileira publica, '
				. 'sem autor identificável e sem dizer para qual diferença de temperatura vale — e um aquário a 26 °C num quarto que cai a 22 °C '
				. 'não é o mesmo problema que o mesmo aquário num quarto que cai a 12 °C. '
				. 'No levantamento da Aquametria de 04/09/2026, a única fonte que amarrou watts por litro a uma diferença declarada foi a ReefFlow: '
				. 'de 1,0 a 1,5 W/L para até ' . number_format_i18n( AQUAMETRIA_C5_DELTA_COBERTO, 0 ) . ' °C. O eHow publica 1,3 W/L, também sem condição; '
				. 'a Casa da Ada publica até 2,0 W/L para a região Sul, o que ao menos reconhece que o Brasil não tem um clima só. '
				. 'A própria linha Eheim Jäger é construída sobre 1 W/L (25 W para 25 L, 100 W para 100 L, 150 W para 150 L), '
				. 'o que explica de onde a regra veio sem torná-la um dimensionamento.',
		),
	);

	$perguntas[] = array(
		'@type' => 'Question',
		'name'  => 'Aquário destampado precisa de aquecedor mais forte?',
		'acceptedAnswer' => array(
			'@type' => 'Answer',
			'text'  => 'Perde mais calor, sim, e perde principalmente por evaporação na lâmina livre, que costuma ser a maior parcela da perda. '
				. 'Mas a Aquametria não corrige o número por isso: a constante que quantificaria essa perda está pendente no nosso banco, sem fonte, '
				. 'e dizer "some 20 % se for destampado" seria inventar constante. '
				. 'Na prática, com o aquário aberto, trate a faixa calculada como piso e considere o degrau comercial seguinte.',
		),
	);

	$faq = array(
		'@type'      => 'FAQPage',
		'@id'        => $url . '#faq',
		'inLanguage' => 'pt-BR',
		'url'        => $url,
		'mainEntity' => $perguntas,
	);

	return array(
		'@context' => 'https://schema.org',
		'@graph'   => array( $app, $faq ),
	);
}
}

if ( ! function_exists( 'aquametria_c5_imprimir_jsonld' ) ) {
function aquametria_c5_imprimir_jsonld() {
	$json = wp_json_encode( aquametria_c5_jsonld_dados(), JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE );
	if ( ! $json ) {
		return;
	}
	echo '<script type="application/ld+json" id="aquametria-c5-jsonld">' . "\n" . $json . "\n" . '</script>' . "\n";
}
}

if ( ! function_exists( 'aquametria_c5_form_html' ) ) {
function aquametria_c5_form_html() {
	$c1 = aquametria_c5_url( 'calculadora-de-litragem' );

	$h  = '<form id="aqm-c5-form" class="aqm-c5-painel" novalidate>';
	$h .= '<h3>O seu aquário e o seu inverno</h3>';
	$h .= '<p class="aqm-c5-sub">A pergunta que decide a potência não é quantos litros o aquário tem — é quanto o cômodo esfria. ';
	$h .= 'Se você já usou as outras calculadoras neste navegador, o volume vem preenchido daqui. Nada é enviado para servidor nenhum.</p>';

	$h .= '<div class="aqm-c5-grade">';

	$h .= '<div class="aqm-c5-campo">';
	$h .= '<label for="aqm-c5-volume">Volume real de água (L)</label>';
	$h .= '<input type="text" inputmode="decimal" autocomplete="off" id="aqm-c5-volume" name="volume" placeholder="110">';
	$h .= '<span class="aqm-c5-dica">A água que está lá dentro, não o número da etiqueta.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c5-campo">';
	$h .= '<label for="aqm-c5-minima">Mínima do cômodo (°C)</label>';
	$h .= '<input type="text" inputmode="decimal" autocomplete="off" id="aqm-c5-minima" name="minima" placeholder="18">';
	$h .= '<span class="aqm-c5-dica">Quanto o ar do cômodo chega a marcar na noite mais fria do ano — não a média da cidade. É a entrada que nenhuma outra calculadora pede.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c5-campo">';
	$h .= '<label for="aqm-c5-especie">Espécie principal</label>';
	$h .= '<select id="aqm-c5-especie" name="especie">';
	$h .= '<option value="">— escolher, ou digitar o alvo ao lado —</option>';
	$h .= '<option value="betta">Betta (24 a 28 °C)</option>';
	$h .= '<option value="kinguio">Kinguio (18 a 24 °C)</option>';
	$h .= '<option value="guppy">Guppy (23 a 26 °C)</option>';
	$h .= '<option value="acara-disco">Acará-disco (26 a 30 °C)</option>';
	$h .= '<option value="tetra">Tetra (26 a 30 °C)</option>';
	$h .= '<option value="acara-bandeira">Acará-bandeira (24 a 28 °C)</option>';
	$h .= '<option value="barbo-sumatra">Barbo-sumatra (20 a 28 °C)</option>';
	$h .= '<option value="paulistinha">Paulistinha (18 a 28 °C)</option>';
	$h .= '</select>';
	$h .= '<span class="aqm-c5-dica" id="aqm-c5-especie-ficha"></span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c5-campo">';
	$h .= '<label for="aqm-c5-alvo">Temperatura-alvo (°C)</label>';
	$h .= '<input type="text" inputmode="decimal" autocomplete="off" id="aqm-c5-alvo" name="alvo" placeholder="26">';
	$h .= '<span class="aqm-c5-dica">Em branco, usamos a ficha da espécie. Preenchido, o seu número manda.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c5-campo">';
	$h .= '<label for="aqm-c5-voltagem">Voltagem da tomada</label>';
	$h .= '<select id="aqm-c5-voltagem" name="voltagem">';
	$h .= '<option value="110">110 V (ou 127 V)</option>';
	$h .= '<option value="220">220 V</option>';
	$h .= '</select>';
	$h .= '<span class="aqm-c5-dica">Filtra a lista de produtos, não o cálculo. Aquecedor na voltagem errada queima.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c5-campo">';
	$h .= '<label for="aqm-c5-tampado">O aquário é tampado?</label>';
	$h .= '<select id="aqm-c5-tampado" name="tampado">';
	$h .= '<option value="sim">sim, tem tampa</option>';
	$h .= '<option value="nao">não, é aberto</option>';
	$h .= '<option value="nao-sei" selected>não sei ainda</option>';
	$h .= '</select>';
	$h .= '<span class="aqm-c5-dica">Muda o texto da resposta, não o número: quantificar essa perda exigiria uma constante que ainda não temos com fonte.</span>';
	$h .= '</div>';

	$h .= '</div>';

	$h .= '<label class="aqm-c5-caixa"><input type="checkbox" id="aqm-c5-sul"> <span>Moro na região Sul — quero que a leitura de 2,0 W/L entre na conta</span></label>';

	$h .= '<div class="aqm-c5-botoes">';
	$h .= '<button type="submit">Calcular a potência</button>';
	$h .= '<button type="button" class="aqm-c5-secundario" id="aqm-c5-limpar">Limpar</button>';
	$h .= '<span class="aqm-c5-dica aqm-c5-oculto" id="aqm-c5-retomado"></span>';
	$h .= '</div>';
	$h .= '<ul class="aqm-c5-avisos" id="aqm-c5-erros"></ul>';
	$h .= '<p class="aqm-c5-criterio aqm-c5-oculto" id="aqm-c5-semvolume" style="margin-top:.9rem">';
	$h .= 'Não sabe o volume real? Ele não é o número da etiqueta: o vidro, a borda livre e as rochas tiram uma parte, e a potência do aquecedor é calculada sobre a água que existe. ';
	$h .= 'A <a href="' . esc_url( $c1 ) . '">calculadora de litragem</a> devolve esse número a partir das medidas em centímetros e o guarda para esta página usar.</p>';
	$h .= '</form>';

	return $h;
}
}

if ( ! function_exists( 'aquametria_c5_resposta_html' ) ) {
function aquametria_c5_resposta_html() {
	$h  = '<div class="aqm-c5-resultado aqm-c5-oculto" id="aqm-c5-saida" aria-live="polite">';

	$h .= '<p class="aqm-c5-nota aqm-c5-nota-alerta aqm-c5-oculto" id="aqm-c5-semdelta"></p>';

	$h .= '<div id="aqm-c5-corpo">';

	$h .= '<div class="aqm-c5-faixa">';
	$h .= '<span class="aqm-c5-rotulo">Potência de aquecedor que o seu caso pede</span>';
	$h .= '<span class="aqm-c5-valor" id="aqm-c5-faixa-valor">—</span>';
	$h .= '<p class="aqm-c5-criterio" id="aqm-c5-faixa-criterio"></p>';
	$h .= '<div class="aqm-c5-delta" id="aqm-c5-delta"></div>';
	$h .= '</div>';

	$h .= '<ul class="aqm-c5-cartoes" id="aqm-c5-regras"></ul>';

	$h .= '<p class="aqm-c5-nota" id="aqm-c5-comercial"></p>';

	$h .= '<ul class="aqm-c5-avisos" id="aqm-c5-avisos"></ul>';

	$h .= '<p class="aqm-c5-nota aqm-c5-nota-alerta" id="aqm-c5-confronto"></p>';

	$h .= '<div class="aqm-c5-painel"><h3>O que aqui é critério nosso, e não fonte de terceiro</h3>';
	$h .= '<p class="aqm-c5-sub" style="margin-bottom:.4rem">Constante tem origem e data; escolha editorial tem nome e fica declarada. Estas são as desta resposta.</p>';
	$h .= '<ul id="aqm-c5-editoriais" style="list-style:none;margin:0;padding:0"></ul></div>';

	$h .= aquametria_c5_produtos_html();

	$h .= '<div class="aqm-c5-citar">';
	$h .= '<p id="aqm-c5-citacao"></p>';
	$h .= '<div class="aqm-c5-campo"><label for="aqm-c5-link">Link desta resposta</label>';
	$h .= '<input type="text" id="aqm-c5-link" readonly></div>';
	$h .= '<div class="aqm-c5-botoes"><button type="button" class="aqm-c5-secundario" id="aqm-c5-copiar">Copiar link</button>';
	$h .= '<span class="aqm-c5-dica" id="aqm-c5-copiado"></span></div>';
	$h .= '<p class="aqm-c5-dica" id="aqm-c5-guardado" style="margin-top:.4rem">Este aquário ficou guardado neste navegador para as próximas calculadoras.</p>';
	$h .= '</div>';

	$h .= '</div>';
	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c5_produtos_html' ) ) {
function aquametria_c5_produtos_html() {
	$divulgacao = aquametria_c5_url( AQUAMETRIA_C5_PAGINA_AFILIADOS );

	$h  = '<div class="aqm-c5-produtos aqm-c5-painel aqm-c5-oculto" id="aqm-c5-produtos">';
	/* O título não afirma mais "atendem essa potência" sobre a lista inteira: ela
	   tem dois grupos, e o segundo é o degrau comercial acima da faixa, que atende
	   a prateleira e não o número (item 2 do despacho da Sentinela de 10/09/2026).
	   Quem afirma passou a ser o cabeçalho de cada grupo, que sabe do que fala. */
	$h .= '<h3>Aquecedores para a potência que você precisa</h3>';
	$h .= '<p class="aqm-c5-sub" id="aqm-c5-produtos-sub"></p>';

	/* A vitrine vem ANTES da ficha e da procedência (contrato 7): a prova de
	   onde veio o número fica, mas ela existe para ser conferida — não para ser
	   o único clique de compra da página. */
	$h .= '<div class="aqm-c5-vitrine aqm-c5-oculto" id="aqm-c5-vitrine">';
	$h .= '<h4>Onde comprar cada um</h4>';
	$h .= '<p class="aqm-c5-criterio">Mesma ordem da lista completa abaixo: primeiro quem cabe na faixa calculada, '
		. 'depois o degrau comercial acima dela, e dentro de cada grupo a potência mais próxima do topo. '
		. 'O cartão de cada aparelho diz por qual dos dois motivos ele está aqui. '
		. 'O valor é cotação com data, não preço de hoje.</p>';
	$h .= '<ul class="aqm-c5-vt-trilho" id="aqm-c5-vitrine-trilho"></ul>';
	$h .= '<p class="aqm-c5-criterio" id="aqm-c5-vitrine-nota"></p>';
	$h .= '</div>';

	$h .= '<ul class="aqm-c5-lista" id="aqm-c5-produtos-lista"></ul>';
	$h .= '<p class="aqm-c5-aviso-afiliado"><strong>Aviso de publicidade.</strong> ';
	$h .= 'Alguns dos botões acima levam a lojas por links de afiliado: se você comprar por eles, a Aquametria pode receber uma comissão, sem custo nenhum a mais para você. ';
	$h .= 'Isso não muda quem aparece na lista nem em que ordem — a ordem é pela potência mais próxima do topo da faixa que o seu caso pede, e modelo sem link aparece do mesmo jeito. ';
	$h .= 'Antes da adequação, duas barreiras de segurança: só entra quem existe na voltagem da sua tomada e cujo termostato alcança a sua temperatura-alvo. ';
	$h .= 'A ficha técnica de cada aquecedor vem do fabricante ou do varejo especializado, com o endereço e a data ao lado; o anúncio da loja nunca é a nossa fonte. ';
	$h .= 'O valor que aparece nos cartões da vitrine <strong>não é preço de hoje</strong>: é a cotação que a Aquametria leu naquele anúncio na data escrita ao lado. ';
	$h .= 'Preço de aquarismo muda toda semana — confira no anúncio antes de comprar, e trate o nosso número como ordem de grandeza, não como promessa. ';
	$h .= '<a href="' . esc_url( $divulgacao ) . '">Como a Aquametria ganha dinheiro</a>.</p>';
	$h .= '</div>';
	$h .= '<p class="aqm-c5-nota aqm-c5-oculto" id="aqm-c5-produtos-nada"></p>';

	return $h;
}
}

if ( ! function_exists( 'aquametria_c5_tenho_html' ) ) {
function aquametria_c5_tenho_html() {
	$h  = '<div class="aqm-c5-painel">';
	$h .= '<h3>Caminho inverso: o aquecedor que eu já tenho serve?</h3>';
	$h .= '<p class="aqm-c5-sub">Informe a potência que vem na caixa e devolvemos até quantos litros ele cobre por cada regra — e, se o volume estiver preenchido acima, quantos watts por litro ele entrega no seu aquário.</p>';
	$h .= '<div class="aqm-c5-grade">';
	$h .= '<div class="aqm-c5-campo"><label for="aqm-c5-tenho">Potência do aquecedor (W)</label>';
	$h .= '<input type="text" inputmode="decimal" id="aqm-c5-tenho" placeholder="100"></div>';
	$h .= '</div>';
	$h .= '<div class="aqm-c5-botoes"><button type="button" id="aqm-c5-tenho-calcular">Ver o que ele cobre</button></div>';
	$h .= '<p class="aqm-c5-criterio" id="aqm-c5-tenho-saida" style="margin-top:.6rem"></p>';
	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c5_fontes_html' ) ) {
function aquametria_c5_fontes_html() {
	$artigo = aquametria_c5_url( AQUAMETRIA_C5_ARTIGO );

	$h  = '<div class="aqm-c5-painel">';
	$h .= '<h3>De onde vem cada número desta página</h3>';
	$h .= '<p class="aqm-c5-sub">Verificado em ' . esc_html( AQUAMETRIA_C5_VERIFICADO_EM ) . '. Calculadora versão ' . esc_html( AQUAMETRIA_C5_VERSAO ) . '.</p>';
	$h .= '<div class="aqm-c5-rolagem"><table class="aqm-c5-fontes">';
	$h .= '<tr><th>Constante</th><th>Valor</th><th>Origem e o que ela significa</th></tr>';

	$h .= '<tr><td>wl-delta-ate-10</td><td>1,0 a 1,5 W/L</td>';
	$h .= '<td>ReefFlow, do levantamento de 04/09/2026 <span class="aqm-c5-selo">divergente entre fontes BR</span>. ';
	$h .= 'É a <strong>única</strong> fonte do nosso corpus que amarra watts por litro a uma diferença de temperatura declarada: vale para até ' . esc_html( AQUAMETRIA_C5_DELTA_COBERTO ) . ' °C entre o ambiente e a água. ';
	$h .= 'Acima disso, ela não afirma nada — e nós também não.</td></tr>';

	$h .= '<tr><td>wl-sul</td><td>2,0 W/L</td>';
	$h .= '<td>Casa da Ada, para a região Sul <span class="aqm-c5-selo">divergente entre fontes BR</span>. ';
	$h .= 'É a única fonte do corpus que reconhece que o Brasil tem mais de um clima. Ainda assim não declara para qual diferença de temperatura o número vale.</td></tr>';

	$h .= '<tr><td>wl-generico</td><td>1,0 W/L</td>';
	$h .= '<td>Repetida sem autoria única na web brasileira <span class="aqm-c5-selo">divergente entre fontes BR</span>. ';
	$h .= 'Nenhuma fonte diz de onde o número saiu nem para qual clima vale. É o vácuo que esta página existe para preencher.</td></tr>';

	$h .= '<tr><td>wl-ehow</td><td>1,3 W/L</td>';
	$h .= '<td>eHow <span class="aqm-c5-selo">divergente entre fontes BR</span>. Também sem condição declarada. Está aqui porque discorda da anterior em 30 %, e a discordância é o conteúdo.</td></tr>';

	$h .= '<tr><td>eheim-jager-linha-comercial</td><td>25 a 300 W, 9 tamanhos</td>';
	$h .= '<td>Eheim Jager / Thermocontrol, ficha do fabricante e tabelas de varejo, completada em 08/09/2026 <span class="aqm-c5-selo">transcrita de varejo</span>. ';
	$h .= 'Dela sai o degrau comercial. E dela sai o achado: 25 W para 25 L, 50 W para 50 L, 100 W para 100 L e 150 W para 150 L — o catálogo do fabricante é construído sobre a mesma regra de 1 W/L que a web repete, ';
	$h .= 'enquanto o mesmo catálogo declara 200 W para 30 a 400 L, uma faixa de 13 vezes.</td></tr>';

	$h .= '<tr><td>especies-parametros-iniciais</td><td>8 espécies</td>';
	$h .= '<td>Petz e Aquarismo Paulista <span class="aqm-c5-selo">transcrita de varejo</span>. Só entram no seletor espécies com ficha e fonte; ';
	$h .= 'o banco completo de espécies é trabalho da C10, ainda em construção.</td></tr>';

	$h .= '<tr><td>u-vidro-aquario</td><td>sem valor <span class="aqm-c5-selo">pendente</span></td>';
	$h .= '<td>O coeficiente de troca térmica do vidro do aquário, que permitiria calcular a potência pela física (P = U · A · ΔT) em vez de por regra de bolso. ';
	$h .= 'Sem ele, esta página não corrige por área, por espessura de vidro nem por tampa. É a entrega que tornaria a Aquametria a única referência do nicho no Brasil, e ela ainda não saiu.</td></tr>';

	$h .= '<tr><td>temperatura-minima-por-cidade</td><td>sem valor <span class="aqm-c5-selo">pendente</span></td>';
	$h .= '<td>A mínima do ar por cidade brasileira. A coleta prevista é a Normal Climatológica do INMET (1991-2020), mínima média do mês mais frio por estação. ';
	$h .= 'Enquanto não existir, a mínima é entrada sua — e é melhor assim: a mínima do seu quarto não é a mínima da sua cidade.</td></tr>';

	$h .= '</table></div>';
	$h .= '<p class="aqm-c5-criterio" style="margin-top:.8rem">A discussão longa de por que essas fontes discordam, e do que acontece quando se segue cada uma delas, está em ';
	$h .= '<a href="' . esc_url( $artigo ) . '">quantos watts de aquecedor o seu aquário precisa</a>.</p>';
	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c5_adiante_html' ) ) {
function aquametria_c5_adiante_html() {
	$hub    = aquametria_c5_url( 'calculadoras' );
	$meto   = aquametria_c5_url( 'metodologia' );
	$c1     = aquametria_c5_url( 'calculadora-de-litragem' );
	$c3     = aquametria_c5_url( 'calculadora-de-vazao-do-filtro' );
	$c12    = aquametria_c5_url( 'calculadora-de-midia-filtrante' );
	$c15    = aquametria_c5_url( 'calculadora-de-iluminacao' );
	$artigo = aquametria_c5_url( AQUAMETRIA_C5_ARTIGO );
	$divul  = aquametria_c5_url( AQUAMETRIA_C5_PAGINA_AFILIADOS );

	$h  = '<div class="aqm-c5-painel aqm-c5-adiante">';
	$h .= '<h3>O que conversa com esta página</h3>';
	$h .= '<ul>';
	$h .= '<li><a href="' . esc_url( $artigo ) . '"><strong>Quantos watts de aquecedor o seu aquário precisa</strong></a> — o texto que explica por que o "1 W por litro" não erra por acaso, e de onde ele veio.</li>';
	$h .= '<li><a href="' . esc_url( $c1 ) . '"><strong>Calculadora de litragem (C1)</strong></a> — é de onde vem o volume real que esta página usa. Se o número acima veio preenchido, veio de lá.</li>';
	$h .= '<li><a href="' . esc_url( $c3 ) . '"><strong>Vazão do filtro (C3)</strong></a> — usa o mesmo volume. O filtro fica ligado 24 horas por dia; o aquecedor, não. Quanto tempo cada um fica ligado é o que a C7 vai calcular.</li>';
	$h .= '<li><a href="' . esc_url( $c12 ) . '"><strong>Mídia filtrante (C12)</strong></a> — quanta mídia biológica o mesmo volume de água pede, pelas quatro dosagens que os fabricantes declaram. A colônia nitrificante também depende de temperatura: aquário frio cicla mais devagar, e é este aquecedor que decide isso.</li>';
	$h .= '<li><a href="' . esc_url( $c15 ) . '"><strong>Iluminação e fotoperíodo (C15)</strong></a> — o outro aparelho que consome energia no aquário, e o único que você pode desligar por 16 horas por dia. Luminária potente também aquece a água: em aquário pequeno e tampado, isso conta contra o trabalho deste aquecedor.</li>';
	$h .= '<li><strong>Consumo elétrico (C7)</strong> — a conta de luz do aquário. Vai ler daqui a potência do aquecedor e a diferença de temperatura, porque é o ciclo do aquecedor que pesa no inverno. Ainda em construção.</li>';
	$h .= '<li><a href="' . esc_url( $meto ) . '"><strong>Como a Aquametria calcula</strong></a> — por que uma faixa com fontes que discordam vale mais que um número redondo sem origem.</li>';
	$h .= '<li><a href="' . esc_url( $divul ) . '"><strong>Como a Aquametria ganha dinheiro</strong></a> — o que é link de afiliado, o que muda (nada na ordem) e o que não publicamos.</li>';
	$h .= '</ul>';
	$h .= '<p class="aqm-c5-criterio">A lista completa, com o estado de cada calculadora, está em <a href="' . esc_url( $hub ) . '">todas as calculadoras</a>.</p>';
	$h .= '</div>';
	return $h;
}
}

/* ---------------------------------------------------------------------------
 * 6. Entrega do estilo e do comportamento — FORA do retorno do shortcode
 *
 * REGRA PERMANENTE DO PROJETO, escrita com sangue em 08/09/2026: JS e CSS de
 * shortcode NUNCA vao dentro do que o shortcode retorna. O retorno do shortcode
 * ainda atravessa os filtros de texto do conteúdo, que trocam cada "&" por
 * a entidade numérica dele — e um único "&&" escapado assim mata o script INTEIRO com
 * SyntaxError: o formulário nunca calcula, a resposta nunca aparece e o bloco de
 * produto com os links de afiliado nunca sai da classe "-oculto". Foi o que
 * derrubou as cinco primeiras calculadoras da ilha.
 *
 * O caminho seguro é imprimir fora dos filtros de conteúdo:
 *   - o estilo no wp_head, para a pagina nao piscar sem estilo;
 *   - o comportamento no wp_footer, depois do HTML que ele controla.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c5_estilo_impresso' ) ) {
function aquametria_c5_estilo_impresso( $marcar = false ) {
	static $impresso = false;
	if ( $marcar ) {
		$impresso = true;
	}
	return $impresso;
}
}

if ( ! function_exists( 'aquametria_c5_pagina_usa' ) ) {
function aquametria_c5_pagina_usa() {
	if ( ! is_singular() ) {
		return false;
	}
	$pagina = get_post();
	if ( ! $pagina || ! isset( $pagina->post_content ) ) {
		return false;
	}
	return has_shortcode( $pagina->post_content, 'aquametria_calculadora_aquecedor' );
}
}

if ( ! function_exists( 'aquametria_c5_imprimir_estilo' ) ) {
function aquametria_c5_imprimir_estilo() {
	if ( aquametria_c5_estilo_impresso() ) {
		return;
	}
	aquametria_c5_estilo_impresso( true );
	echo '<style id="aquametria-c5-estilo">' . "\n" . aquametria_c5_css() . "\n" . '</style>' . "\n";
}
}

if ( ! function_exists( 'aquametria_c5_cabeca' ) ) {
function aquametria_c5_cabeca() {
	if ( ! aquametria_c5_pagina_usa() ) {
		return;
	}
	aquametria_c5_imprimir_estilo();
	aquametria_c5_imprimir_jsonld();
}
}
add_action( 'wp_head', 'aquametria_c5_cabeca', 20 );

if ( ! function_exists( 'aquametria_c5_rodape' ) ) {
function aquametria_c5_rodape() {
	/* Rede de segurança: se o shortcode entrou por um caminho que o wp_head não
	   enxergou (bloco, template, widget), o estilo ainda sai — atrasado, mas sai. */
	aquametria_c5_imprimir_estilo();

	$js  = 'var AQM_C5_DATA = ' . wp_json_encode( AQUAMETRIA_C5_VERIFICADO_EM ) . ";\n";
	$js .= 'var AQM_C5_CATALOGO = ' . wp_json_encode( array_values( aquametria_c5_catalogo() ) ) . ";\n";
	$js .= 'var AQM_C5_REGRAS = ' . wp_json_encode( aquametria_c5_regras() ) . ";\n";
	$js .= 'var AQM_C5_LINHA = ' . wp_json_encode( aquametria_c5_linha_comercial() ) . ";\n";
	$js .= aquametria_c5_js();
	echo '<script id="aquametria-c5-script">' . "\n" . $js . "\n" . '</script>' . "\n";
}
}

/* ---------------------------------------------------------------------------
 * 7. Shortcode — devolve SÓ o HTML. Estilo e comportamento saem acima.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c5_shortcode' ) ) {
function aquametria_c5_shortcode() {
	static $ja_saiu = false;
	if ( $ja_saiu ) {
		/* Uma instância por página: os ids do formulário são únicos e o
		   comportamento liga na primeira. */
		return '';
	}
	$ja_saiu = true;

	/* O comportamento e o estilo saem no rodapé, fora dos filtros de conteúdo. */
	add_action( 'wp_footer', 'aquametria_c5_rodape', 20 );

	$h  = '<div class="aqm-c5">';
	$h .= aquametria_c5_promessa_html();
	$h .= aquametria_c5_resposta_direta_html();
	$h .= aquametria_c5_form_html();
	$h .= aquametria_c5_resposta_html();
	$h .= aquametria_c5_vitrine_servida_html();
	$h .= aquametria_c5_exemplos_html();
	$h .= aquametria_c5_tenho_html();
	$h .= aquametria_c5_fontes_html();
	$h .= aquametria_c5_adiante_html();
	$h .= aquametria_c5_barra_html();
	$h .= '</div>';

	return $h;
}
}
add_shortcode( 'aquametria_calculadora_aquecedor', 'aquametria_c5_shortcode' );
