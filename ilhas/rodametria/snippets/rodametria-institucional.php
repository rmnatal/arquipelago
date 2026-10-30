<?php
/**
 * RODAMETRIA — AS QUATRO PAGINAS QUE O SITE DEVE A QUEM LE (bloco 5d)
 *
 * `/sobre/`, `/contato/`, `/divulgacao-de-afiliados/` e `/privacidade/`. A 16.1
 * nomeia estas quatro, mais a home, como as UNICAS paginas que podem morar
 * soltas na raiz — sem pai e sem nivel 2 — e a 21.7 as tira do teto de leva,
 * porque "nenhuma delas responde a uma busca".
 *
 * -------------------------------------------------------------------------
 * POR QUE ELAS SAO UM SNIPPET E NAO UM PEDACO DA CASCA
 * -------------------------------------------------------------------------
 * A casca promete, desde a revisao 3 dela, que "nao e editada quando a ilha
 * cresce": pagina nova entra pelos filtros `rodametria_paginas` e
 * `rodametria_instalar`, de dentro do proprio snippet dela. Enfiar quatro
 * paginas de texto na casca quebraria essa promessa e poria prosa publica no
 * arquivo que pinta TODAS as paginas — o lugar onde um erro custa o site
 * inteiro, e nao uma pagina.
 *
 * -------------------------------------------------------------------------
 * AS DUAS METADES, E NENHUM NUMERO E DIGITADO AQUI
 * -------------------------------------------------------------------------
 *   - `dados/paginas-institucionais.json` e DECLARADO: titulo, h1,
 *     description, caixa, secoes, bloco de recusa e dobras. E a voz do
 *     `VOZ.md`, e a prosa dela traz MOLDES no lugar de todo numero —
 *     {VEICULOS_NO_BANCO}, {ITENS_COM_LINK}, {PAGINAS_NO_AR}, {TERCEIROS}...
 *   - O NUMERO e CONTADO aqui, na hora de servir, por `rdm_inst_numeros()`:
 *     do banco que a F2 publica, da vitrine das paginas de produto e do mapa
 *     de paginas da casca. A secao 8 e explicita — "numero de tela nasce
 *     contado, nunca digitado" —, e esta familia de pagina e justamente a que
 *     fala de si mesma ("quantos itens tem link", "quantas paginas no ar"),
 *     que e o caso em que o numero digitado passa a mentir calado.
 *
 * -------------------------------------------------------------------------
 * ORDEM DA TELA: 32.2, E NAO 32.1 — E SEM BLOCO DE COMPRA
 * -------------------------------------------------------------------------
 * Estas quatro nao tem formulario, entao o teto de 700 px da 32.5 e da CAIXA
 * DE RESPOSTA e nao de um formulario que nao existe (32.5-b: "portao que
 * reprova pagina certa e o caminho mais curto para alguem passar a
 * ignora-lo"). E elas nascem SEM bloco de compra: nao ha produto nenhum a
 * vender aqui, e a 32.2 so manda bloco de compra onde ha o que comprar.
 * De cima para baixo: trilha e H1 · caixa de resposta · linha mestra · as
 * secoes VISIVEIS · o bloco de recusa · as dobras · a malha.
 *
 * -------------------------------------------------------------------------
 * O BLOCO DE RECUSA E MARCADO NO MARKUP, E ISSO NAO E ESTETICA
 * -------------------------------------------------------------------------
 * A cicatriz e da clubedomosaico, 11/09/2026, e esta na secao 8: a frase
 * legitima que RECUSA a escassez inventada usa as MESMAS palavras que a secao
 * 7 proibe, e "perdoar por presenca de palavra e adivinhar". Entao a recusa
 * mora numa classe propria (`rdm-inst-recusa`), o portao retira esses blocos
 * antes de proibir o termo no resto, e exige que TODO item do bloco ABRA
 * negando — senao bastaria marcar uma promessa como recusa.
 *
 * Sem `<script>` e sem `<style>` no retorno do shortcode (secao 8): a folha
 * sai no `wp_footer`. Foi o E-comercial duplo dentro de `<script>` que
 * derrubou cinco calculadoras da Aquametria em 08/09/2026.
 */

/* A VERSAO MORA NUMA CONSTANTE, e nao so no comentario: `atualizar-manifest.py`
   casa esta constante com o campo `versao` do manifest. */
if ( ! defined( 'RODAMETRIA_INST_VERSAO' ) ) {
	define( 'RODAMETRIA_INST_VERSAO', '1.0.0' );
}
/* O id da option que o Sync grava. Ele sai de constante porque a casca 1.0.0
   digitou `f2_respostas` com sublinhado onde o manifest diz `f2-respostas` com
   hifen, e a pagina caiu no estado degradado honesto sem uma linha vermelha em
   lugar nenhum. */
if ( ! defined( 'RODAMETRIA_ID_DADOS_INST' ) ) {
	define( 'RODAMETRIA_ID_DADOS_INST', 'paginas-institucionais' );
}
if ( ! defined( 'RODAMETRIA_ID_DADOS_F2_INST' ) ) {
	define( 'RODAMETRIA_ID_DADOS_F2_INST', 'f2-respostas' );
}
if ( ! defined( 'RODAMETRIA_ID_DADOS_VITRINE_INST' ) ) {
	define( 'RODAMETRIA_ID_DADOS_VITRINE_INST', 'vitrine-de-produto' );
}

/* ---------------------------------------------------------------------------
 * 1. A CAMADA DECLARADA
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rdm_inst_declarado' ) ) {
/** A voz. Sem ela nenhuma destas paginas existe, e e assim que deve ser. */
function rdm_inst_declarado() {
	static $d = null;
	if ( null !== $d ) {
		return $d;
	}
	$bruto = rodametria_casca_banco( RODAMETRIA_ID_DADOS_INST );
	$d     = is_array( $bruto ) ? $bruto : array();

	return $d;
}
}

if ( ! function_exists( 'rdm_inst_paginas' ) ) {
/** As paginas declaradas, indexadas por slug. */
function rdm_inst_paginas() {
	static $p = null;
	if ( null !== $p ) {
		return $p;
	}
	$d = rdm_inst_declarado();
	$p = array();
	if ( ! empty( $d['paginas'] ) && is_array( $d['paginas'] ) ) {
		foreach ( $d['paginas'] as $pg ) {
			if ( ! empty( $pg['slug'] ) ) {
				$p[ (string) $pg['slug'] ] = $pg;
			}
		}
	}

	return $p;
}
}

/* ---------------------------------------------------------------------------
 * 2. OS NUMEROS — CONTADOS, NUNCA DIGITADOS (secao 8)
 *
 * Cada molde desta lista e uma contagem feita na hora, sobre a MESMA fonte que
 * o site serve: as options que o Sync grava do banco, e o mapa de paginas da
 * casca. A regra da secao 8 que manda isto e literal: "para cada campo
 * publicado, aponte quem e a fonte e faca a bancada ler DELA".
 *
 * E a contagem de PAGINAS NO AR conta a URL e nao a entrada do mapa: pagina
 * declarada no mapa e ainda nao criada tem URL vazia, e dizer que ela esta no
 * ar seria a mesma mentira que a casca 1.4.0 nasceu para consertar — mapa ja
 * mostrando tres paginas novas e o sitemap com duas.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rdm_inst_itens_com_link' ) ) {
/**
 * Os itens do banco que TEM saida de compra na tela, veiculos e pecas juntos.
 *
 * A fonte e a mesma que a F2 serve (`compra`), e nao o banco cru: o que esta
 * pagina afirma e sobre o que o VISITANTE ve, e quem decide isso e a camada
 * que vai para a tela. Ler o banco cru aqui criaria duas verdades.
 */
function rdm_inst_itens_com_link() {
	static $itens = null;
	if ( null !== $itens ) {
		return $itens;
	}
	$f2    = rodametria_casca_banco( RODAMETRIA_ID_DADOS_F2_INST );
	$itens = array();
	if ( ! is_array( $f2 ) || empty( $f2['compra'] ) || ! is_array( $f2['compra'] ) ) {
		return $itens;
	}
	foreach ( array( 'vitrine', 'pecas_publicaveis' ) as $grupo ) {
		if ( empty( $f2['compra'][ $grupo ] ) || ! is_array( $f2['compra'][ $grupo ] ) ) {
			continue;
		}
		foreach ( $f2['compra'][ $grupo ] as $item ) {
			if ( ! is_array( $item ) ) {
				continue;
			}
			$tem = ( ! empty( $item['url_afiliado_da_ficha'] ) || ! empty( $item['url_busca'] ) );
			if ( $tem ) {
				$itens[] = array(
					'grupo'  => $grupo,
					'degrau' => isset( $item['degrau'] ) ? (int) $item['degrau'] : 0,
				);
			}
		}
	}

	return $itens;
}
}

if ( ! function_exists( 'rdm_inst_paginas_no_ar' ) ) {
/** Quantas paginas desta ilha o visitante consegue abrir AGORA. */
function rdm_inst_paginas_no_ar() {
	$n = 0;
	foreach ( rodametria_casca_paginas() as $slug => $p ) {
		if ( '' !== rodametria_casca_url_do_slug( $slug ) ) {
			$n++;
		}
	}

	return $n;
}
}

if ( ! function_exists( 'rdm_inst_numeros' ) ) {
function rdm_inst_numeros() {
	static $n = null;
	if ( null !== $n ) {
		return $n;
	}

	$f2      = rodametria_casca_banco( RODAMETRIA_ID_DADOS_F2_INST );
	$vitrine = rodametria_casca_banco( RODAMETRIA_ID_DADOS_VITRINE_INST );
	$decl    = rdm_inst_declarado();

	/* --- o banco de veiculos, pela camada que a F2 serve --- */
	$veiculos_total = 0;
	$veiculos_link  = 0;
	$pecas_link     = 0;
	$lojas          = array();
	if ( is_array( $f2 ) && ! empty( $f2['compra'] ) && is_array( $f2['compra'] ) ) {
		$c              = $f2['compra'];
		$veiculos_total = isset( $c['total_registros_veiculos'] ) ? (int) $c['total_registros_veiculos'] : 0;
		foreach ( array( 'vitrine', 'pecas_publicaveis' ) as $grupo ) {
			if ( empty( $c[ $grupo ] ) || ! is_array( $c[ $grupo ] ) ) {
				continue;
			}
			foreach ( $c[ $grupo ] as $item ) {
				if ( ! is_array( $item ) ) {
					continue;
				}
				if ( empty( $item['url_afiliado_da_ficha'] ) && empty( $item['url_busca'] ) ) {
					continue;
				}
				if ( 'vitrine' === $grupo ) {
					$veiculos_link++;
				} else {
					$pecas_link++;
				}
				if ( ! empty( $item['programa'] ) ) {
					$lojas[ (string) $item['programa'] ] = true;
				}
			}
		}
	}

	/* --- os anuncios lidos nas paginas de produto --- */
	$lidas      = 0;
	$recusadas  = 0;
	$publicados = 0;
	$pg_produto = 0;
	if ( is_array( $vitrine ) && ! empty( $vitrine['paginas'] ) && is_array( $vitrine['paginas'] ) ) {
		foreach ( $vitrine['paginas'] as $p ) {
			if ( empty( $p['numeros'] ) || ! is_array( $p['numeros'] ) ) {
				continue;
			}
			$pg_produto++;
			$lidas      += isset( $p['numeros']['lidas'] ) ? (int) $p['numeros']['lidas'] : 0;
			$recusadas  += isset( $p['numeros']['recusadas'] ) ? (int) $p['numeros']['recusadas'] : 0;
			$publicados += isset( $p['numeros']['n'] ) ? (int) $p['numeros']['n'] : 0;
		}
	}

	/* --- a escada da 25.1 por item: ficha (1 a 3) ou busca (4) --- */
	$com_ficha = 0;
	$com_busca = 0;
	foreach ( rdm_inst_itens_com_link() as $i ) {
		if ( $i['degrau'] >= 1 && $i['degrau'] <= 3 ) {
			$com_ficha++;
		} else {
			$com_busca++;
		}
	}

	/* --- os terceiros que carregam, DECLARADOS e conferidos no ar pelo portao --- */
	$terceiros = ( ! empty( $decl['terceiros_que_carregam'] ) && is_array( $decl['terceiros_que_carregam'] ) )
		? $decl['terceiros_que_carregam'] : array();

	/* O nome da loja em portugues, e ele sai de uma tabela e nao do dado cru:
	   `shopee` na tela seria a ilha falando no vocabulario de quem a escreveu. */
	$nomes_de_loja = array(
		'shopee'        => 'Shopee',
		'mercado_livre' => 'Mercado Livre',
		'mercadolivre'  => 'Mercado Livre',
	);
	$nomes = array();
	foreach ( array_keys( $lojas ) as $k ) {
		$nomes[] = isset( $nomes_de_loja[ $k ] ) ? $nomes_de_loja[ $k ] : $k;
	}
	sort( $nomes );

	$n = array(
		'VEICULOS_NO_BANCO'    => $veiculos_total,
		'VEICULOS_COM_LINK'    => $veiculos_link,
		'VEICULOS_SEM_LINK'    => max( 0, $veiculos_total - $veiculos_link ),
		'PECAS_COM_LINK'       => $pecas_link,
		'ITENS_COM_LINK'       => $veiculos_link + $pecas_link,
		'ITENS_COM_FICHA'      => $com_ficha,
		'ITENS_COM_BUSCA'      => $com_busca,
		'ANUNCIOS_LIDOS'       => $lidas,
		'ANUNCIOS_RECUSADOS'   => $recusadas,
		'ANUNCIOS_PUBLICADOS'  => $publicados,
		'PAGINAS_NO_AR'        => rdm_inst_paginas_no_ar(),
		'PAGINAS_DE_PRODUTO'   => $pg_produto,
		'LOJAS'                => count( $nomes ),
		'NOME_DAS_LOJAS'       => $nomes ? implode( ' e ', $nomes ) : 'loja nenhuma',
		'TERCEIROS'            => count( $terceiros ),
		'NOMES_DOS_TERCEIROS'  => rdm_inst_frase_dos_terceiros( $terceiros ),
	);

	return $n;
}
}

if ( ! function_exists( 'rdm_inst_frase_dos_terceiros' ) ) {
/**
 * A frase que NOMEIA cada endereco de fora que carrega junto com a pagina.
 *
 * Ela e montada da lista declarada, nunca escrita a mao na prosa: a pagina de
 * privacidade afirma "os dois estao nomeados abaixo", e se a frase fosse prosa
 * fixa ela continuaria dizendo "os dois" no dia em que entrasse o terceiro.
 * E o portao de ar confere a lista contra o HTML servido de TODAS as paginas,
 * que e o que torna esta frase uma medicao em vez de uma promessa.
 */
function rdm_inst_frase_dos_terceiros( $terceiros ) {
	$partes = array();
	foreach ( (array) $terceiros as $t ) {
		if ( empty( $t['quem'] ) || empty( $t['endereco'] ) ) {
			continue;
		}
		$enderecos = $t['endereco'];
		if ( ! empty( $t['endereco_irmao'] ) ) {
			$enderecos .= ' e ' . $t['endereco_irmao'];
		}
		$partes[] = $t['quem'] . ', que serve ' . ( isset( $t['o_que'] ) ? $t['o_que'] : '' )
			. ' ' . ( isset( $t['onde'] ) ? $t['onde'] : '' ) . ', por ' . $enderecos;
	}

	return $partes ? ( implode( '. ', $partes ) . '.' ) : 'Nenhum endereço de fora carrega junto com esta página.';
}
}

if ( ! function_exists( 'rdm_inst_preencher' ) ) {
/**
 * Troca os moldes da prosa declarada pelo numero contado.
 *
 * Molde que o preenchedor NAO conhece fica na tela como `{ASSIM}`, de
 * proposito: o portao `teste-institucional.py` o acha na hora, e molde cru
 * visivel e barato de ver. O caro e o silencioso — o molde que alguem troca
 * por uma string vazia e ninguem nota a frase mutilada.
 */
function rdm_inst_preencher( $texto ) {
	$n = rdm_inst_numeros();
	foreach ( $n as $chave => $valor ) {
		$texto = str_replace( '{' . $chave . '}', (string) $valor, (string) $texto );
	}

	return $texto;
}
}

/* ---------------------------------------------------------------------------
 * 3. O MAPA DAS PAGINAS — as quatro entram pelo filtro da casca
 *
 * `pai` fica NULO nas quatro, e isso e a 16.1 ao pe da letra: "sem pagina
 * solta na raiz ALEM de home, sobre, contato, divulgacao de afiliados e
 * privacidade". Sao estas, e so estas, e a trilha delas fica `Inicio › Sobre`
 * porque `cadeia_da_trilha()` poe a home na frente de quem nao tem pai.
 *
 * `no_menu` fica TRUE: o `VOZ.md` desta ilha manda um menu curto de assunto
 * ("Ferramentas · Veiculos · Pecas · Guias"), e pagina institucional no menu
 * de cima rouba o lugar do que a pessoa veio procurar. Elas aparecem no
 * RODAPE, que a casca monta de todo o mapa e serve em TODA pagina — o que
 * tambem resolve a 16.4(f) para as quatro de uma vez.
 * ------------------------------------------------------------------------- */

add_filter( 'rodametria_paginas', function ( $mapa ) {
	foreach ( rdm_inst_paginas() as $slug => $pg ) {
		$mapa[ $slug ] = array(
			'nome'        => (string) $pg['nome'],
			'titulo'      => (string) $pg['titulo'],
			'tipo'        => 'institucional',
			'pai'         => null,
			'no_menu'     => true,
			'description' => (string) $pg['description'],
		);
	}

	return $mapa;
}, 30 );

if ( ! function_exists( 'rdm_inst_atual' ) ) {
/** A pagina institucional desta requisicao, ou null. */
function rdm_inst_atual() {
	$slug    = rodametria_casca_slug_atual();
	$paginas = rdm_inst_paginas();

	return isset( $paginas[ $slug ] ) ? $paginas[ $slug ] : null;
}
}

/* ---------------------------------------------------------------------------
 * 4. OS PEDACOS DA TELA
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rdm_inst_secoes_html' ) ) {
function rdm_inst_secoes_html( $secoes ) {
	$html = '';
	foreach ( (array) $secoes as $s ) {
		if ( empty( $s['titulo'] ) ) {
			continue;
		}
		$html .= '<section class="rdm-inst-secao">';
		$html .= '<h2>' . esc_html( rdm_inst_preencher( $s['titulo'] ) ) . '</h2>';
		foreach ( (array) ( isset( $s['paragrafos'] ) ? $s['paragrafos'] : array() ) as $p ) {
			$html .= '<p>' . esc_html( rdm_inst_preencher( $p ) ) . '</p>';
		}
		$html .= '</section>';
	}

	return $html;
}
}

if ( ! function_exists( 'rdm_inst_recusa_html' ) ) {
/**
 * O BLOCO DE RECUSA, marcado no markup (`rdm-inst-recusa`) e nao deduzido pela
 * vizinhanca das palavras. Ver a nota do cabecalho deste arquivo.
 */
function rdm_inst_recusa_html( $recusa ) {
	if ( empty( $recusa['titulo'] ) || empty( $recusa['itens'] ) ) {
		return '';
	}
	$html = '<section class="rdm-inst-secao rdm-inst-recusa">';
	$html .= '<h2>' . esc_html( rdm_inst_preencher( $recusa['titulo'] ) ) . '</h2><ul>';
	foreach ( (array) $recusa['itens'] as $i ) {
		$html .= '<li>' . esc_html( rdm_inst_preencher( $i ) ) . '</li>';
	}
	$html .= '</ul></section>';

	return $html;
}
}

if ( ! function_exists( 'rdm_inst_dobras_html' ) ) {
function rdm_inst_dobras_html( $dobras ) {
	$html = '';
	foreach ( (array) $dobras as $d ) {
		if ( empty( $d['titulo'] ) ) {
			continue;
		}
		$corpo = '';
		foreach ( (array) ( isset( $d['paragrafos'] ) ? $d['paragrafos'] : array() ) as $p ) {
			$corpo .= '<p>' . esc_html( rdm_inst_preencher( $p ) ) . '</p>';
		}
		$html .= rodametria_casca_dobra( rdm_inst_preencher( $d['titulo'] ), $corpo );
	}

	return $html;
}
}

if ( ! function_exists( 'rdm_inst_malha_html' ) ) {
/**
 * A malha das quatro, visivel porque e alvo de link (16.4).
 *
 * A ancora e o NOME da pagina de destino, nunca "saiba mais" nem "clique
 * aqui" — a 16.4(c) e explicita. E a home entra na lista das quatro por um
 * motivo de leitura e nao de SEO: quem cai numa pagina institucional por
 * busca precisa de uma porta para o que o site faz de verdade.
 */
function rdm_inst_malha_html( $pagina ) {
	$html = '<nav class="rdm-malha rdm-inst-malha" aria-label="Veja também">';
	$html .= '<h2>Veja também</h2><ul>';
	$achou = false;
	foreach ( (array) ( isset( $pagina['veja_tambem'] ) ? $pagina['veja_tambem'] : array() ) as $slug ) {
		$link = rodametria_casca_link( (string) $slug );
		if ( '' !== $link ) {
			$html .= '<li>' . $link . '</li>';
			$achou = true;
		}
	}
	$home = rodametria_casca_link( 'inicio', 'os três números antes de comprar um elétrico' );
	if ( '' !== $home ) {
		$html .= '<li>' . $home . '</li>';
		$achou = true;
	}
	$html .= '</ul></nav>';

	return $achou ? $html : '';
}
}

/* ---------------------------------------------------------------------------
 * 5. A PAGINA
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'rdm_inst_pagina_html' ) ) {
function rdm_inst_pagina_html() {
	$pagina = rdm_inst_atual();

	if ( ! $pagina ) {
		/* Pagina DEGRADADA e honesta, pelo mesmo desenho da F2 e das paginas de
		   produto: nunca molde cru, nunca texto inventado para encher. */
		return '<div class="rdm-faixa rdm-pagina">'
			. rodametria_casca_trilha_html()
			. '<h1>Esta página está fora do ar neste momento</h1>'
			. '<p class="rdm-promessa">O texto dela não chegou nesta atualização. '
			. 'Ela prefere não dizer nada a dizer uma parte.</p>'
			. '</div>';
	}

	$html  = '<div class="rdm-faixa rdm-pagina rdm-inst">';
	$html .= rodametria_casca_trilha_html();
	$html .= '<h1>' . esc_html( $pagina['h1'] ) . '</h1>';

	/* (32.2) A CAIXA DE RESPOSTA NO TOPO — o numero e a condicao em uma frase.
	   O numero e CONTADO (secao 2 deste arquivo), nunca digitado no declarado. */
	if ( ! empty( $pagina['caixa'] ) ) {
		$c     = $pagina['caixa'];
		$html .= rodametria_casca_caixa(
			rdm_inst_preencher( isset( $c['rotulo'] ) ? $c['rotulo'] : '' ),
			rdm_inst_preencher( isset( $c['numero'] ) ? $c['numero'] : '' ),
			rdm_inst_preencher( isset( $c['unidade'] ) ? $c['unidade'] : '' ),
			array_map( 'rdm_inst_preencher', (array) ( isset( $c['frases'] ) ? $c['frases'] : array() ) ),
			isset( $c['tom'] ) ? $c['tom'] : 'neutro' );
	}

	if ( ! empty( $pagina['linha_mestra'] ) ) {
		$html .= '<p class="rdm-promessa">' . esc_html( rdm_inst_preencher( $pagina['linha_mestra'] ) ) . '</p>';
	}

	$html .= rdm_inst_secoes_html( isset( $pagina['secoes'] ) ? $pagina['secoes'] : array() );
	$html .= rdm_inst_recusa_html( isset( $pagina['recusa'] ) ? $pagina['recusa'] : array() );
	$html .= rdm_inst_dobras_html( isset( $pagina['dobras'] ) ? $pagina['dobras'] : array() );
	$html .= rdm_inst_malha_html( $pagina );

	$html .= '</div>';

	return $html;
}
}

add_shortcode( 'rodametria_institucional', 'rdm_inst_pagina_html' );

/* ---------------------------------------------------------------------------
 * 6. A FOLHA — no wp_footer, nunca no retorno do shortcode (secao 8)
 *
 * Ela so veste o que e DESTA familia de pagina. Caixa, dobra e carrossel vem
 * da casca (32.6-b), e redecora-los aqui seria a 32.5-c outra vez: "quem
 * conserta a folha de um snippet procura o mesmo defeito nas irmas", e a causa
 * la foi uma folha de pagina vencendo a do molde por ordem de carga.
 * ------------------------------------------------------------------------- */

add_action( 'wp_footer', function () {
	if ( ! rdm_inst_atual() ) {
		return;
	}
	?>
<style id="rdm-inst-folha">
/* NADA AQUI REDECLARA h1, h2 NEM A CAIXA: a casca ja os veste, e folha de
   pagina que os reescreve e a 32.5-c em acao — a folha do Guia da
   clubedomosaico vencia a do molde por ordem de carga. O que esta linha
   acrescenta e so o que e desta familia: a largura de leitura do paragrafo
   corrido e a marca visual do bloco de recusa. */
body.rdm .rdm-inst-secao p{max-width:62ch}
body.rdm .rdm-inst-recusa{border-left:3px solid var(--rdm-traco);padding-left:var(--rdm-e3)}
body.rdm .rdm-inst-recusa ul{max-width:62ch}
body.rdm .rdm-inst-recusa li{margin-bottom:var(--rdm-e2)}
</style>
	<?php
}, 30 );

/* ---------------------------------------------------------------------------
 * 7. INSTALACAO — pelo gancho da casca, nunca em toda requisicao
 *
 * Sem pai, pela 16.1: estas quatro sao as unicas paginas da raiz desta ilha
 * fora da home. `garantir_pagina()` aceita pai ZERO exatamente por elas, e o
 * comentario dele diz isso com o nome das cinco.
 * ------------------------------------------------------------------------- */

add_filter( 'rodametria_instalar', function ( $relato ) {
	$paginas = rdm_inst_paginas();
	if ( ! $paginas ) {
		$relato[] = 'institucional: ERRO — a camada declarada nao chegou';

		return $relato;
	}
	foreach ( $paginas as $slug => $pg ) {
		$p = rodametria_casca_garantir_pagina(
			$slug,
			(string) $pg['titulo'],
			'[rodametria_institucional]' );
		if ( empty( $p['id'] ) ) {
			$relato[] = 'institucional/' . $slug . ': ERRO — '
				. ( isset( $p['erro'] ) ? $p['erro'] : 'sem id' );
			continue;
		}
		$relato[] = 'institucional/' . $slug . ': #' . $p['id'] . ' (' . $p['slug'] . ')'
			. ( empty( $p['slug_ok'] ) ? ' — ATENCAO: slug divergente' : '' );
	}

	return $relato;
}, 30 );
