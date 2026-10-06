/**
 * Clube do Mosaico F2 — Qual cola usar no mosaico, e qual rejunte
 * Versão 1.9.0 (06/10/2026) — A PÁGINA PASSA A DIZER O QUE FAZER ANTES DE
 * PASSAR A COLA, e a frase é do fabricante. O campo `preparo` existia no banco
 * desde 10/09/2026, em nove registros, como texto solto sem fonte — e a palavra
 * `preparo` não aparecia em NENHUM dos nove snippets desta ilha. Nove
 * declarações de fabricante lidas, gravadas e descartadas em silêncio, que é o
 * defeito que esta ilha já mediu com quatro outros nomes. Entram
 * `cdm_f2_preparo()` (os três estados do campo, esquema v12) e
 * `cdm_f2_preparo_html()`, chamada nas DUAS respostas — a da cola e a do
 * rejunte. O que sobe é só o `literal_do_fabricante` com documento e data; a
 * paráfrase antiga NÃO sobe, e isso foi medido e não escolhido: das quatro
 * paráfrases que deu para conferir contra a fonte em 06/10, as quatro perdiam
 * informação dela. E quem não tem a instrução aparece pelo nome, com a causa —
 * lista que só mostra quem passou faz o leitor ler ausência como "não precisa".
 * Versão 1.8.0 (06/10/2026) — a REGRA 7 nasce, e ela entra consertando um
 * defeito que esta página servia desde 11/09: o Tekbond Silicone Acético
 * Construção aparecia no TOPO da recomendação para quem respondeu CACO DE
 * ESPELHO sobre cerâmica, e a Tekbond escreve "espelhos" na lista do que este
 * produto não deve tocar desde o dia em que o registro entrou no banco. A frase
 * era lida como BASE e só como base: na base "espelho" o produto saía proibido,
 * com o espelho no caquinho ele saía recomendado. O ácido acético da cura ataca
 * a prata e a pintura de proteção do espelho — e é por isso que a MESMA Tekbond
 * vende um silicone NEUTRO declarando "espelhos" entre os usos dele. A regra 7
 * é a segunda a olhar o caquinho (a 6 foi a primeira) e a primeira a eliminá-lo
 * por proibição declarada: a frase é do fabricante, a lista de quais caquinhos
 * do nosso vocabulário caem nela é NOSSA, e a tela diz as duas coisas em
 * orações separadas (seção 26.3). Ela roda ANTES da regra 6, porque proibição é
 * afirmação mais forte que condição não cumprida.
 * (O 1.6.0 e o 1.7.0 NÃO têm entrada aqui, e isso é defeito desta lista, não
 * salto de numeração: o 1.6.0 entrou em `4240501` — dez materiais saindo do
 * piso da 25.2 — e o 1.7.0 em `8dc288e` — a marca cedendo o lugar ao número no
 * `<title>`. Nos dois a constante `CDM_F2_VERSAO` subiu e este changelog não.
 * O portão de `atualizar-manifest.py` compara o manifest com a CONSTANTE, não
 * com este cabeçalho, então esta metade envelheceu calada — a mesma família da
 * cicatriz que aquele arquivo carrega no próprio cabeçalho.)
 * Versão 1.5.0 (14/09/2026) — A FRASE PROIBIDA SAI DA ILHA, E O QUE FALTAVA NÃO
 * ERA DECISÃO: ERA A TELA LER O CAMPO. A seção 7 do contrato passou a proibir
 * "link de loja em breve" em 14/09/2026, e esta ilha ainda a servia em 15 dos 25
 * itens do banco — 13 pastilhas e 2 colas —, nos cartões da F2 e na vitrine de
 * pastilha da F1, que chama esta mesma função. A escada de `cdm_f2_compra_html()`
 * ganhou o degrau 4 da seção 25.1: a busca CRUA (`afiliado.url_busca_produto`)
 * vira o botão quando não há ficha nem busca encurtada. Ela sai
 * `rel="nofollow noopener"` e não `sponsored`, porque não rende comissão — o
 * atributo declara a relação paga, e chamar de patrocinado um link que não paga
 * seria mentir ao leitor sobre a única coisa que ele tem o direito de saber sobre
 * nós. Dois dos 15 já tinham a palavra-chave escrita no banco desde 13/09.
 * Versão 1.4.0 (13/09/2026) — a matriz escrita à mão do esquema vai de 18 para
 * 45 células, a grade inteira de base x lugar, e a tabela pré-renderizada desta
 * página passa a servir as 45 linhas. Foi essa régua independente que achou o
 * defeito no ar: em quatro estados (vidro, madeira, alvenaria e metal dentro da
 * água) a página negava, na frase-resposta e na vitrine vazia, a mesma declaração
 * de nível 4 que ela imprimia duas seções abaixo. A faixa descoberta agora nomeia
 * qual das três causas a segura: silêncio, procedência da fonte, ou ambiente
 * delimitado pelo próprio fabricante.
 * Versão 1.3.0 (13/09/2026) — a REGRA 6 nasce, e com ela as duas faixas que esta
 * página declarava não saber responder deixam de ser buracos. A regra 6 é a
 * primeira regra de cola que olha o CAQUINHO: o Cascola PL500 declara que "ao
 * menos uma das superfícies deve ser porosa", e isso não é base nem ambiente, é o
 * PAR. A entrada do caquinho existia desde a 1.0.0 e nenhuma régua de cola a lia.
 * Versão 1.2.0 (13/09/2026) — a escada da seção 25 chega à tela. O `url_busca`
 * estava no banco desde 13/09 e nenhuma linha de código o lia: a escada existia
 * no dado e não no site. Ver `cdm_f2_compra_html()`.
 * Versão 1.0.0 (11/09/2026) — bloco 4 da fila, a primeira ferramenta da ilha e
 * a primeira página de nível 3 dela.
 *
 * O QUE ELA RESPONDE, e por que ganha (seção 14.9 do ARQUIPELAGO.md): a SERP de
 * "qual cola para mosaico" é blog sem fabricante, sem código de documento, sem
 * data e sem separar dentro de casa de sol e chuva — o bloco 1 mediu isso
 * consulta a consulta. Esta página responde a mesma pergunta com a declaração
 * do próprio fabricante do adesivo, e é a única em português que diz o que NÃO
 * usar, e por quê.
 *
 * ------------------------------------------------------------------------
 * AS QUATRO DECISÕES DE DESENHO, e a cicatriz que cada uma evita
 * ------------------------------------------------------------------------
 *
 * 1. A RESPOSTA É SERVIDA PELO SERVIDOR, NUNCA CALCULADA NO NAVEGADOR.
 *    O formulário é um GET para a própria página e o PHP monta a resposta. Não
 *    existe uma linha de decisão em JavaScript, e isso não é purismo: era o
 *    caminho mais curto para o defeito que a seção 5 do contrato nomeia —
 *    ferramenta que calcula no navegador mostra a um modelo de linguagem um
 *    formulário VAZIO. Aqui todo estado da entrada é HTML servido de verdade,
 *    e a segunda metade da mesma decisão é que não há régua duplicada entre PHP
 *    e JS para as duas se separarem em silêncio.
 *    O preço disso é URL com parâmetro, e ele é pago na mesma linha: estado com
 *    parâmetro sai com `noindex, follow` e com `canonical` para o endereço
 *    limpo. Quem entra no índice é a página-âncora, uma só (seções 14.1 e 14.4).
 *
 * 2. A ELEGIBILIDADE É RECOMPUTADA DAS DECLARAÇÕES, NUNCA DIGITADA.
 *    As cinco regras da cola e as quatro do rejunte estão escritas em
 *    `dados/esquema-banco.json` e implementadas aqui em PHP; `ferramentas/
 *    validar-banco.py` as implementa em Python, separado, e as duas metades são
 *    comparadas contra as matrizes escritas À MÃO no mesmo esquema. É a trava da
 *    seção 8: quem confere escreve a própria régua.
 *
 * 3. O BLOCO DE COMPRA VEM ANTES DA PROVA DE PROCEDÊNCIA (seção 7, cicatriz da
 *    Robometria de 10/09/2026), e desde a 1.2.0 ele DESCE A ESCADA DA SEÇÃO 25:
 *    ficha de produto no botão, busca encurtada na linha discreta abaixo; sem
 *    ficha, a busca encurtada sobe e vira o botão; sem ela, a busca CRUA vira o
 *    botão (desde a 1.5.0). Item sem nenhuma das três não chega ao ar: é falha
 *    dura do `validar-banco.py`, não etiqueta na tela. A régua inteira está em
 *    `cdm_f2_compra_html()`. O link de procedência continua
 *    sendo texto pequeno, `rel="nofollow noopener"`, nunca botão.
 *
 * 4. A CATEGORIA É PARTE DA PERGUNTA. A régua da cola decide sobre BASE; a do
 *    rejunte, sobre LARGURA DE JUNTA. São duas funções separadas de propósito —
 *    rejunte não toca a base, e traduzir uma no vocabulário da outra produz uma
 *    afirmação sem sentido que entra calada no cálculo. Foi o defeito que o
 *    bloco 3c encontrou no validador em 11/09/2026.
 *
 * ------------------------------------------------------------------------
 * O QUE ESTA PÁGINA DIZ QUE NÃO SABE
 * ------------------------------------------------------------------------
 * AS DUAS FAIXAS QUE ESTAVAM ESCRITAS AQUI FECHARAM EM 13/09/2026, e o registro
 * do que elas eram fica porque explica a forma das duas regras novas:
 *
 * - **Base de plástico** ficava vazia porque o único produto que falava de
 *   plástico dizia "certos tipos de plástico", que não nomeia tipo nenhum.
 *   Abriu com o Cascola PL500, que lista "plásticos" sem qualificador — e que
 *   trouxe junto a condição de porosidade, porque colar sobre plástico é
 *   exatamente o caso em que a condição decide.
 * - **Peça em contato permanente com água** ficava vazia porque a única
 *   declaração de colagem submersa era press release de 2018 (nível 4, abaixo
 *   do mínimo de 3). Abriu com o Silicone Acético Maxx, cuja declaração de
 *   aquário e piscina está na página de produto do fabricante.
 *
 * O QUE CONTINUA SEM RESPOSTA, dito com o tamanho certo: das nove bases, o Maxx
 * só entra em cerâmica, porque "cerâmicas vitrificadas" é a única superfície que
 * o fabricante nomeia — as outras oito seguem descobertas dentro da água. E o
 * PL500 é de uso interno declarado, então a base de plástico só está coberta
 * dentro de casa, em lugar seco. Faixa que fechou em uma célula não fechou na
 * linha inteira, e a página não finge que sim.
 */

if ( ! defined( 'CDM_F2_VERSAO' ) ) {
	define( 'CDM_F2_VERSAO', '1.9.0' );
}
if ( ! defined( 'CDM_F2_SLUG' ) ) {
	/* Nível 3 com mãe /materiais/ direto — dois níveis em vez de três, estado de
	   transição declarado na seção 2 do ARVORE.md. A categoria definitiva
	   (`colas-e-adesivos`) só nasce quando tiver três filhas com dado real (16.5),
	   e mover a URL depois disso é proibido para página posicionada (12.1) —
	   por isso a escolha de hoje é a mãe que JÁ existe. */
	define( 'CDM_F2_SLUG', 'materiais/qual-cola-usar-no-mosaico' );
}
if ( ! defined( 'CDM_F2_TITULO' ) ) {
	/* UM NOME POR PÁGINA, em toda superfície: é este texto que sai no cartão da
	   home, no cartão do Guia, no degrau da trilha, no H1 e no <title>. A
	   Aquametria pagou em 11/09/2026 por ter oito páginas em que o degrau e o H1
	   diziam nomes diferentes a uma linha de distância. 41 caracteres; com o
	   sufixo do site o <title> fica em 60, abaixo do teto de 65. */
	define( 'CDM_F2_TITULO', 'Qual cola usar no mosaico, e qual rejunte' );
}

/* ---------------------------------------------------------------------------
 * 1. Registro na casca — a página, o cartão e o degrau da trilha
 * ------------------------------------------------------------------------- */

add_filter( 'cdm_paginas', function ( $paginas ) {
	if ( ! is_array( $paginas ) ) {
		return $paginas;
	}
	$paginas[ CDM_F2_SLUG ] = array(
		'titulo'   => CDM_F2_TITULO,
		'conteudo' => '[cdm_f2]',
		'pai'      => 'materiais',
	);

	return $paginas;
} );

add_filter( 'cdm_ferramentas', function ( $lista ) {
	if ( ! is_array( $lista ) ) {
		return $lista;
	}
	foreach ( $lista as $i => $f ) {
		if ( isset( $f['codigo'] ) && 'F2' === $f['codigo'] ) {
			$lista[ $i ]['titulo'] = CDM_F2_TITULO;
			$lista[ $i ]['slug']   = CDM_F2_SLUG;
			$lista[ $i ]['estado'] = 'publicada';
		}
	}

	return $lista;
} );

/* ---------------------------------------------------------------------------
 * 2. O banco, lido das options que o Sync grava
 *
 * Sem banco a página NÃO inventa recomendação: ela diz que a medição não chegou.
 * É a mesma trava que a Robometria escreveu em 11/09/2026 depois de descobrir
 * que a option que alimentava os números dela nunca existira no site, porque o
 * item do manifest estava com publicar=false e ninguém tinha olhado.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f2_banco' ) ) {
function cdm_f2_banco() {
	static $banco = null;
	if ( null !== $banco ) {
		return $banco;
	}

	$esquema  = get_option( 'clubedomosaico_dados_esquema-banco' );
	$colas    = get_option( 'clubedomosaico_dados_materiais-colas' );
	$rejuntes = get_option( 'clubedomosaico_dados_materiais-rejuntes' );

	$materiais = array();
	foreach ( array( $colas, $rejuntes ) as $arquivo ) {
		if ( ! is_array( $arquivo ) || empty( $arquivo['materiais'] ) || ! is_array( $arquivo['materiais'] ) ) {
			continue;
		}
		foreach ( $arquivo['materiais'] as $m ) {
			if ( empty( $m['id'] ) || 'ativo' !== ( isset( $m['status'] ) ? $m['status'] : '' ) ) {
				continue;
			}
			$materiais[ $m['id'] ] = $m;
		}
	}
	ksort( $materiais );

	$banco = array(
		'esquema'   => is_array( $esquema ) ? $esquema : array(),
		'materiais' => $materiais,
		'colas'     => is_array( $colas ) ? $colas : array(),
		'rejuntes'  => is_array( $rejuntes ) ? $rejuntes : array(),
		'completo'  => ( is_array( $esquema ) && $materiais ),
	);

	return $banco;
}
}

if ( ! function_exists( 'cdm_f2_normalizar' ) ) {
/**
 * Minúsculas, sem acento, espaços colapsados — e a comparação com o mapa de
 * termos é EXATA depois disso. "ceramica" (a superfície sobre a qual se cola) e
 * "ceramicas" (a peça que se assenta) são termos diferentes de propósito, e
 * confundi-los foi exatamente o defeito que o bloco 3 achou na cimentcola.
 */
function cdm_f2_normalizar( $texto ) {
	$t = mb_strtolower( trim( (string) $texto ), 'UTF-8' );
	$de = array( 'á','à','â','ã','ä','é','ê','ë','í','ï','ó','ô','õ','ö','ú','ü','ç','ñ' );
	$pa = array( 'a','a','a','a','a','e','e','e','i','i','o','o','o','o','u','u','c','n' );
	$t  = str_replace( $de, $pa, $t );

	return preg_replace( '/\s+/u', ' ', $t );
}
}

if ( ! function_exists( 'cdm_f2_mapa_cola' ) ) {
/** O mapa de termos do fabricante, do esquema, indexado pelo termo normalizado. */
function cdm_f2_mapa_cola() {
	static $mapa = null;
	if ( null !== $mapa ) {
		return $mapa;
	}
	$banco = cdm_f2_banco();
	$fonte = isset( $banco['esquema']['mapa_de_termos_do_fabricante'] ) ? $banco['esquema']['mapa_de_termos_do_fabricante'] : array();
	$mapa  = array( 'termos' => array(), 'vagos' => array(), 'nao_traduz' => array() );

	foreach ( ( isset( $fonte['termos'] ) ? $fonte['termos'] : array() ) as $t ) {
		$chave                    = cdm_f2_normalizar( $t['literal'] );
		$mapa['termos'][ $chave ] = array(
			'base'     => isset( $t['base'] ) ? $t['base'] : array(),
			'ambiente' => isset( $t['ambiente'] ) ? $t['ambiente'] : array(),
		);
		if ( ! empty( $t['vago'] ) ) {
			$mapa['vagos'][ $chave ] = true;
		}
	}
	foreach ( ( isset( $fonte['termos_que_nao_traduzem'] ) ? $fonte['termos_que_nao_traduzem'] : array() ) as $t ) {
		$mapa['nao_traduz'][ cdm_f2_normalizar( $t['literal'] ) ] = true;
	}

	return $mapa;
}
}

if ( ! function_exists( 'cdm_f2_traduzir_cola' ) ) {
/**
 * Uma lista literal do fabricante vira vocabulário da ilha.
 *
 * Devolve também QUAIS literais casaram com cada alvo: é esse pedaço que vai
 * para a tela como "a declaração que fez o produto entrar" (seção 7). Sem ele a
 * página diria "serve" sem dizer por quê, que é a metade que separa esta ilha
 * de um blog.
 */
function cdm_f2_traduzir_cola( $lista ) {
	$mapa = cdm_f2_mapa_cola();
	$out  = array( 'base' => array(), 'ambiente' => array(), 'vago' => array(), 'literais' => array() );

	foreach ( (array) $lista as $literal ) {
		$chave = cdm_f2_normalizar( $literal );
		if ( isset( $mapa['nao_traduz'][ $chave ] ) || ! isset( $mapa['termos'][ $chave ] ) ) {
			continue;
		}
		$alvo = $mapa['termos'][ $chave ];
		foreach ( $alvo['base'] as $b ) {
			if ( isset( $mapa['vagos'][ $chave ] ) ) {
				$out['vago'][ $b ] = true;
			} else {
				$out['base'][ $b ] = true;
			}
			$out['literais'][ $b ][] = $literal;
		}
		foreach ( $alvo['ambiente'] as $a ) {
			$out['ambiente'][ $a ]   = true;
			$out['literais'][ $a ][] = $literal;
		}
	}

	return $out;
}
}

if ( ! function_exists( 'cdm_f2_nivel' ) ) {
/** O nível da fonte de um material é o MELHOR (menor) que ele tem. */
function cdm_f2_nivel( $m ) {
	$niveis = array();
	foreach ( (array) ( isset( $m['fontes'] ) ? $m['fontes'] : array() ) as $f ) {
		if ( isset( $f['nivel'] ) ) {
			$niveis[] = (int) $f['nivel'];
		}
	}

	return $niveis ? min( $niveis ) : 9;
}
}

if ( ! function_exists( 'cdm_f2_perfil_cola' ) ) {
/** As declarações de um adesivo, já traduzidas para o vocabulário da ilha. */
function cdm_f2_perfil_cola( $m ) {
	static $cache = array();
	$id = isset( $m['id'] ) ? $m['id'] : '';
	if ( isset( $cache[ $id ] ) ) {
		return $cache[ $id ];
	}
	$d = isset( $m['declaracoes'] ) ? $m['declaracoes'] : array();

	$ind    = cdm_f2_traduzir_cola( isset( $d['indicado_para'] ) ? $d['indicado_para'] : array() );
	$pro1   = cdm_f2_traduzir_cola( isset( $d['nao_usar_em'] ) ? $d['nao_usar_em'] : array() );
	$pro2   = cdm_f2_traduzir_cola( isset( $d['nao_indicado_para'] ) ? $d['nao_indicado_para'] : array() );
	$naorec = cdm_f2_traduzir_cola( isset( $d['nao_recomendado_em'] ) ? $d['nao_recomendado_em'] : array() );
	$delim  = cdm_f2_traduzir_cola( isset( $d['ambientes_declarados'] ) ? $d['ambientes_declarados'] : array() );
	$resist = cdm_f2_traduzir_cola( isset( $d['resistencias_declaradas'] ) ? $d['resistencias_declaradas'] : array() );

	$literais_proibicao = array();
	foreach ( array( $pro1, $pro2 ) as $p ) {
		foreach ( $p['literais'] as $alvo => $ls ) {
			$literais_proibicao[ $alvo ] = array_merge( isset( $literais_proibicao[ $alvo ] ) ? $literais_proibicao[ $alvo ] : array(), $ls );
		}
	}
	$literais_cobertura = array();
	foreach ( array( $delim, $resist, $ind ) as $p ) {
		foreach ( $p['literais'] as $alvo => $ls ) {
			$literais_cobertura[ $alvo ] = array_merge( isset( $literais_cobertura[ $alvo ] ) ? $literais_cobertura[ $alvo ] : array(), $ls );
		}
	}

	$cache[ $id ] = array(
		'bases_indicadas'       => $ind['base'],
		'bases_proibidas'       => $pro1['base'] + $pro2['base'],
		'bases_vagas'           => $ind['vago'] + $naorec['base'] + $naorec['vago'],
		'ambientes_proibidos'   => $pro1['ambiente'] + $pro2['ambiente'],
		'ambientes_delimitados' => $delim['ambiente'],
		'ambientes_cobertos'    => $delim['ambiente'] + $resist['ambiente'] + $ind['ambiente'],
		'literais_indicacao'    => $ind['literais'],
		'literais_proibicao'    => $literais_proibicao,
		'literais_cobertura'    => $literais_cobertura,
		'nivel'                 => cdm_f2_nivel( $m ),
	);

	return $cache[ $id ];
}
}

if ( ! function_exists( 'cdm_f2_criticos_cola' ) ) {
function cdm_f2_criticos_cola() {
	$banco = cdm_f2_banco();
	$r     = isset( $banco['esquema']['regras_de_elegibilidade']['4_ambiente_critico_exige_declaracao_EXPLICITA']['ambientes'] )
		? $banco['esquema']['regras_de_elegibilidade']['4_ambiente_critico_exige_declaracao_EXPLICITA']['ambientes']
		: array();

	return array_flip( (array) $r );
}
}

if ( ! function_exists( 'cdm_f2_nivel_maximo' ) ) {
function cdm_f2_nivel_maximo() {
	$banco = cdm_f2_banco();

	return isset( $banco['esquema']['escada_de_fontes']['nivel_minimo_para_recomendacao_primaria'] )
		? (int) $banco['esquema']['escada_de_fontes']['nivel_minimo_para_recomendacao_primaria']
		: 3;
}
}

if ( ! function_exists( 'cdm_f2_porosas' ) ) {
/**
 * A classificação de porosidade, LIDA DO ESQUEMA — nunca escrita aqui.
 *
 * Seção 26.2 do ARQUIPELAGO.md: lista digitada dentro da régua envelhece calada no
 * dia em que uma base nova entrar no vocabulário. E a outra metade da mesma seção é
 * a que morde aqui: régua que lê a própria lista de um arquivo de dados aprova tudo,
 * em silêncio, no dia em que o arquivo perder a chave. Por isso o retorno vazio NÃO
 * é tratado como "nada é poroso" — `cdm_f2_condicao_conhecida()` separa "a condição
 * não se aplica" de "a gente não sabe classificar", e quem não sabe não recomenda.
 */
function cdm_f2_porosas() {
	static $cache = null;
	if ( null !== $cache ) {
		return $cache;
	}
	$banco = cdm_f2_banco();
	$p     = isset( $banco['esquema']['superficies_porosas'] ) ? $banco['esquema']['superficies_porosas'] : array();
	$cache = array(
		'bases'    => array_flip( (array) ( isset( $p['bases_porosas'] ) ? $p['bases_porosas'] : array() ) ),
		'tesselas' => array_flip( (array) ( isset( $p['tesselas_porosas'] ) ? $p['tesselas_porosas'] : array() ) ),
		'existe'   => ( isset( $p['bases_porosas'] ) && isset( $p['tesselas_porosas'] ) ),
	);

	return $cache;
}
}

if ( ! function_exists( 'cdm_f2_grupos_de_peca' ) ) {
/**
 * A classificação de quais caquinhos caem em cada GRUPO DE PEÇA proibido.
 *
 * Irmã de `cdm_f2_porosas()` e escrita pelo mesmo motivo (seção 26.2: a lista
 * mora no esquema, nunca dentro da régua), com UMA diferença que é o oposto de
 * um detalhe: aqui a lista decide quem PERDE a recomendação. Então, quando ela
 * falta, a direção segura é a contrária — `cdm_f2_peca_proibida()` passa a
 * eliminar o produto em TODO caquinho, em vez de em nenhum. Nos dois casos a
 * ilha prefere deixar de indicar a indicar sem conferir.
 */
function cdm_f2_grupos_de_peca() {
	static $cache = null;
	if ( null !== $cache ) {
		return $cache;
	}
	$banco  = cdm_f2_banco();
	$raiz   = isset( $banco['esquema']['grupos_de_tessela_proibidos'] )
		? $banco['esquema']['grupos_de_tessela_proibidos'] : array();
	$grupos = isset( $raiz['grupos'] ) ? (array) $raiz['grupos'] : array();
	$mapa   = array();
	foreach ( $grupos as $chave => $g ) {
		if ( empty( $g['tesselas_no_grupo'] ) ) {
			continue;
		}
		$mapa[ $chave ] = array(
			'tesselas' => array_flip( (array) $g['tesselas_no_grupo'] ),
			'literal'  => isset( $g['literal_que_o_origina'] ) ? $g['literal_que_o_origina'] : '',
		);
	}
	$cache = array( 'grupos' => $mapa, 'existe' => ! empty( $mapa ) );

	return $cache;
}
}

if ( ! function_exists( 'cdm_f2_grupos_de_peca_conhecidos' ) ) {
/** A ilha ainda sabe classificar caquinho em grupo de peça? */
function cdm_f2_grupos_de_peca_conhecidos() {
	$g = cdm_f2_grupos_de_peca();

	return ! empty( $g['existe'] );
}
}

if ( ! function_exists( 'cdm_f2_proibe_grupos_de_peca' ) ) {
/** Os grupos de peça que ESTE produto proíbe, pela declaração dele. */
function cdm_f2_proibe_grupos_de_peca( $m ) {
	$c = isset( $m['condicoes']['proibe_grupos_de_tessela'] )
		? $m['condicoes']['proibe_grupos_de_tessela'] : array();

	return isset( $c['valor'] ) ? (array) $c['valor'] : array();
}
}

if ( ! function_exists( 'cdm_f2_peca_proibida' ) ) {
/**
 * Os grupos declarados por este produto em que ESTE caquinho cai.
 *
 * Devolve a lista, e não um booleano, porque a tela cita a frase do grupo que
 * mordeu — dizer "o fabricante proíbe" sem mostrar onde é a metade da frase que
 * a seção 15.2 não aceita.
 */
function cdm_f2_peca_proibida( $m, $tessela ) {
	$declarados = cdm_f2_proibe_grupos_de_peca( $m );
	if ( ! $declarados ) {
		return array();
	}
	if ( ! cdm_f2_grupos_de_peca_conhecidos() ) {
		return $declarados;
	}
	$mapa  = cdm_f2_grupos_de_peca();
	$morde = array();
	foreach ( $declarados as $g ) {
		if ( ! isset( $mapa['grupos'][ $g ] ) || isset( $mapa['grupos'][ $g ]['tesselas'][ $tessela ] ) ) {
			$morde[] = $g;
		}
	}

	return $morde;
}
}

if ( ! function_exists( 'cdm_f2_caquinhos_fora_dos_grupos' ) ) {
/**
 * Os caquinhos do vocabulário que NENHUM dos grupos dados alcança — o "troque
 * por isto e ele volta a servir" da regra 7. Contado do esquema, nunca digitado.
 */
function cdm_f2_caquinhos_fora_dos_grupos( $grupos ) {
	$banco = cdm_f2_banco();
	$rot   = cdm_f2_rotulos();
	$mapa  = cdm_f2_grupos_de_peca();
	$nomes = array();
	foreach ( (array) $banco['esquema']['vocabularios']['material_tessela'] as $t ) {
		$dentro = false;
		foreach ( (array) $grupos as $g ) {
			if ( isset( $mapa['grupos'][ $g ]['tesselas'][ $t ] ) ) {
				$dentro = true;
			}
		}
		if ( ! $dentro && isset( $rot['tessela'][ $t ] ) ) {
			$nomes[] = mb_strtolower( $rot['tessela'][ $t ], 'UTF-8' );
		}
	}

	return cdm_f2_lista_humana( $nomes );
}
}

if ( ! function_exists( 'cdm_f2_exige_porosa' ) ) {
/** O fabricante declarou, para ESTE produto, que uma das superfícies tem de ser porosa. */
function cdm_f2_exige_porosa( $m ) {
	return ! empty( $m['condicoes']['exige_superficie_porosa']['valor'] );
}
}

if ( ! function_exists( 'cdm_f2_condicao_conhecida' ) ) {
/**
 * A ilha ainda sabe classificar porosidade?
 *
 * Existe para a página nunca confundir "a condição não se aplica" com "a
 * classificação sumiu". Se alguém apagar `superficies_porosas` do esquema, a
 * régua acima passa a reprovar TODO produto com condição em TODA combinação —
 * que é a direção segura — e é esta função que faz a tela dizer o motivo certo
 * em vez de acusar o par de superfícies de uma coisa que ninguém mediu.
 */
function cdm_f2_condicao_conhecida() {
	$p = cdm_f2_porosas();

	return ! empty( $p['existe'] ) && $p['bases'] && $p['tesselas'];
}
}

if ( ! function_exists( 'cdm_f2_condicao_cumprida' ) ) {
/** A condição do fabricante, medida sobre o PAR de superfícies coladas. */
function cdm_f2_condicao_cumprida( $base, $tessela ) {
	$p = cdm_f2_porosas();

	return isset( $p['bases'][ $base ] ) || isset( $p['tesselas'][ $tessela ] );
}
}

if ( ! function_exists( 'cdm_f2_avaliar_cola' ) ) {
/**
 * As cinco regras, na ordem em que elas decidem.
 * Devolve array( situacao, score ). Situação: recomendado | ressalva |
 * proibido | silencio.
 */
function cdm_f2_avaliar_cola( $m, $base, $ambiente ) {
	$p = cdm_f2_perfil_cola( $m );

	/* 1 — proibição vence indicação dentro do mesmo produto. O acético indica
	   "alumínio comum e anodizado" e proíbe "metal corrosível, zinco e chapa
	   galvanizada": vale o conjunto MAIS ESTREITO, porque quem monta mosaico não
	   sabe dizer se a chapa dela é galvanizada. */
	if ( isset( $p['bases_proibidas'][ $base ] ) || isset( $p['ambientes_proibidos'][ $ambiente ] ) ) {
		return array( 'proibido', 0 );
	}
	/* 2 — base sem declaração não é recomendação. Silêncio não vira "pode". */
	if ( ! isset( $p['bases_indicadas'][ $base ] ) ) {
		return array( 'silencio', 0 );
	}
	/* 3 — quem delimita ambiente fica fechado nele. */
	if ( $p['ambientes_delimitados'] && ! isset( $p['ambientes_delimitados'][ $ambiente ] ) ) {
		return array( 'silencio', 0 );
	}
	/* 4 — ambiente crítico exige declaração explícita. */
	$criticos = cdm_f2_criticos_cola();
	if ( isset( $criticos[ $ambiente ] ) && ! isset( $p['ambientes_cobertos'][ $ambiente ] ) ) {
		return array( 'silencio', 0 );
	}

	$score = 2 + ( isset( $p['ambientes_cobertos'][ $ambiente ] ) ? 2 : 0 );

	/* 5 — nível de fonte limita a recomendação primária. */
	if ( $p['nivel'] > cdm_f2_nivel_maximo() ) {
		return array( 'ressalva', $score );
	}

	return array( 'recomendado', $score );
}
}

if ( ! function_exists( 'cdm_f2_celula_cola' ) ) {
/**
 * A célula base × ambiente. SÓ materiais de categoria cola entram aqui — a
 * categoria é parte da pergunta, e um rejunte listado como "eliminado por
 * silêncio" numa célula de colagem é uma frase sem sentido.
 *
 * O TERCEIRO ARGUMENTO É A REGRA 6, e ele é opcional de propósito. Com `null`
 * (que é o que a tabela pré-renderizada passa) a função devolve a camada de
 * DECLARAÇÃO, que é a que a `matriz_esperada_da_F2` confere célula a célula.
 * Com uma tessela, ela aplica a condição declarada do fabricante sobre o PAR de
 * superfícies — e é essa que a resposta da pessoa usa, porque a pergunta dela
 * sempre tem as duas.
 *
 * A ORDEM ESTÁ ESCRITA E IMPORTA: a condição roda DEPOIS das cinco regras e
 * ANTES da ordenação por score. Rodar depois da ordenação deixaria célula sem
 * topo com elegíveis na mão — em `vidro` + `caco de espelho` o produto com
 * condição é justamente o primeiro colocado, e quem sobe no lugar dele são os
 * dois silicones que estavam abaixo.
 */
function cdm_f2_celula_cola( $base, $ambiente, $tessela = null ) {
	$banco       = cdm_f2_banco();
	$recomendados = array();
	$ressalva     = array();
	$proibidos    = array();
	$silencio     = array();
	$condicao     = array();
	$peca         = array();

	foreach ( $banco['materiais'] as $id => $m ) {
		if ( 'cola' !== ( isset( $m['categoria'] ) ? $m['categoria'] : '' ) ) {
			continue;
		}
		list( $situacao, $score ) = cdm_f2_avaliar_cola( $m, $base, $ambiente );
		/* A REGRA 7 ANTES DA 6, e a ordem está escrita no esquema: proibição é
		   afirmação mais forte que condição não cumprida — a mesma hierarquia da
		   regra 1. Quem caísse nas duas tem de sair pela proibição, com as
		   palavras dela: a elegibilidade seria igual nas duas ordens e a frase
		   que o leitor recebe, não. */
		if ( null !== $tessela
			&& ( 'recomendado' === $situacao || 'ressalva' === $situacao )
			&& cdm_f2_peca_proibida( $m, $tessela ) ) {
			$peca[] = $id;
			continue;
		}
		if ( null !== $tessela
			&& ( 'recomendado' === $situacao || 'ressalva' === $situacao )
			&& cdm_f2_exige_porosa( $m )
			&& ! cdm_f2_condicao_cumprida( $base, $tessela ) ) {
			$condicao[] = $id;
			continue;
		}
		if ( 'recomendado' === $situacao ) {
			$recomendados[ $id ] = $score;
		} elseif ( 'ressalva' === $situacao ) {
			$ressalva[] = $id;
		} elseif ( 'proibido' === $situacao ) {
			$proibidos[] = $id;
		} else {
			$silencio[] = $id;
		}
	}

	$topo   = array();
	$abaixo = array();
	if ( $recomendados ) {
		$maior = max( $recomendados );
		foreach ( $recomendados as $id => $score ) {
			if ( $score === $maior ) {
				$topo[] = $id;
			} else {
				$abaixo[] = $id;
			}
		}
	}
	sort( $topo );
	sort( $abaixo );
	sort( $ressalva );
	sort( $proibidos );
	sort( $silencio );
	sort( $condicao );
	sort( $peca );

	return array(
		'recomendados_topo'             => $topo,
		'elegiveis_abaixo_do_topo'      => $abaixo,
		'mencionados_com_ressalva'      => $ressalva,
		'eliminados_por_proibicao'      => $proibidos,
		'eliminados_por_silencio'       => $silencio,
		'eliminados_por_condicao'       => $condicao,
		'eliminados_por_proibicao_da_peca' => $peca,
	);
}
}

/* ---------------------------------------------------------------------------
 * 3. O rejunte — régua própria, e a variável que decide é a LARGURA DA JUNTA
 *
 * Isto NÃO reaproveita as funções da cola, e a razão é de conteúdo antes de ser
 * de método: na cola a lista do fabricante nomeia a BASE sobre a qual se cola;
 * no rejunte, a mesma lista nomeia a TESSELA que será rejuntada e o ambiente.
 * Rejunte não toca a base. E a lista de ambientes críticos é maior aqui — três
 * em vez de dois, porque o rejunte é a superfície exposta: na pia e no
 * banheiro, quem falha primeiro é ele.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f2_mapa_rejunte' ) ) {
function cdm_f2_mapa_rejunte() {
	static $mapa = null;
	if ( null !== $mapa ) {
		return $mapa;
	}
	$banco = cdm_f2_banco();
	$fonte = isset( $banco['esquema']['mapa_de_termos_do_rejunte'] ) ? $banco['esquema']['mapa_de_termos_do_rejunte'] : array();
	$mapa  = array( 'ambiente' => array(), 'tessela' => array(), 'nao_traduz' => array() );

	foreach ( ( isset( $fonte['termos'] ) ? $fonte['termos'] : array() ) as $t ) {
		$mapa['ambiente'][ cdm_f2_normalizar( $t['literal'] ) ] = isset( $t['ambiente'] ) ? $t['ambiente'] : array();
	}
	foreach ( ( isset( $fonte['termos_tessela'] ) ? $fonte['termos_tessela'] : array() ) as $t ) {
		$mapa['tessela'][ cdm_f2_normalizar( $t['literal'] ) ] = isset( $t['tessela'] ) ? $t['tessela'] : array();
	}
	foreach ( ( isset( $fonte['termos_que_nao_traduzem'] ) ? $fonte['termos_que_nao_traduzem'] : array() ) as $t ) {
		$mapa['nao_traduz'][ cdm_f2_normalizar( $t['literal'] ) ] = true;
	}

	return $mapa;
}
}

if ( ! function_exists( 'cdm_f2_traduzir_rejunte' ) ) {
function cdm_f2_traduzir_rejunte( $lista ) {
	$mapa = cdm_f2_mapa_rejunte();
	$out  = array( 'ambiente' => array(), 'tessela' => array(), 'literais' => array() );

	foreach ( (array) $lista as $literal ) {
		$chave = cdm_f2_normalizar( $literal );
		if ( isset( $mapa['nao_traduz'][ $chave ] ) ) {
			continue;
		}
		if ( isset( $mapa['ambiente'][ $chave ] ) ) {
			foreach ( $mapa['ambiente'][ $chave ] as $a ) {
				$out['ambiente'][ $a ]   = true;
				$out['literais'][ $a ][] = $literal;
			}
		} elseif ( isset( $mapa['tessela'][ $chave ] ) ) {
			foreach ( $mapa['tessela'][ $chave ] as $t ) {
				$out['tessela'][ $t ]    = true;
				$out['literais'][ $t ][] = $literal;
			}
		}
	}

	return $out;
}
}

if ( ! function_exists( 'cdm_f2_prop' ) ) {
/** propriedades[campo].valor, aceitando ausência como null. */
function cdm_f2_prop( $m, $campo ) {
	return isset( $m['propriedades'][ $campo ]['valor'] ) ? $m['propriedades'][ $campo ]['valor'] : null;
}
}

if ( ! function_exists( 'cdm_f2_perfil_rejunte' ) ) {
function cdm_f2_perfil_rejunte( $m ) {
	static $cache = array();
	$id = isset( $m['id'] ) ? $m['id'] : '';
	if ( isset( $cache[ $id ] ) ) {
		return $cache[ $id ];
	}
	$d = isset( $m['declaracoes'] ) ? $m['declaracoes'] : array();

	$ind    = cdm_f2_traduzir_rejunte( isset( $d['indicado_para'] ) ? $d['indicado_para'] : array() );
	$delim  = cdm_f2_traduzir_rejunte( isset( $d['ambientes_declarados'] ) ? $d['ambientes_declarados'] : array() );
	$resist = cdm_f2_traduzir_rejunte( isset( $d['resistencias_declaradas'] ) ? $d['resistencias_declaradas'] : array() );

	$literais = array();
	foreach ( array( $ind, $delim, $resist ) as $p ) {
		foreach ( $p['literais'] as $alvo => $ls ) {
			$literais[ $alvo ] = array_merge( isset( $literais[ $alvo ] ) ? $literais[ $alvo ] : array(), $ls );
		}
	}

	$cache[ $id ] = array(
		'junta_min'             => cdm_f2_prop( $m, 'junta_min_mm' ),
		'junta_max'             => cdm_f2_prop( $m, 'junta_max_mm' ),
		'ambientes_cobertos'    => $ind['ambiente'] + $delim['ambiente'] + $resist['ambiente'],
		'ambientes_delimitados' => $delim['ambiente'],
		'tesselas_declaradas'   => $ind['tessela'] + $resist['tessela'],
		'literais'              => $literais,
		'nivel'                 => cdm_f2_nivel( $m ),
	);

	return $cache[ $id ];
}
}

if ( ! function_exists( 'cdm_f2_criticos_rejunte' ) ) {
function cdm_f2_criticos_rejunte() {
	$banco = cdm_f2_banco();
	$r     = isset( $banco['esquema']['regras_de_elegibilidade_do_rejunte']['2_ambiente_critico_exige_declaracao_EXPLICITA']['ambientes'] )
		? $banco['esquema']['regras_de_elegibilidade_do_rejunte']['2_ambiente_critico_exige_declaracao_EXPLICITA']['ambientes']
		: array();

	return array_flip( (array) $r );
}
}

if ( ! function_exists( 'cdm_f2_avaliar_rejunte' ) ) {
/** Situação: recomendado | ressalva | fora_da_junta | fora_do_ambiente. */
function cdm_f2_avaliar_rejunte( $m, $junta_mm, $ambiente ) {
	$p = cdm_f2_perfil_rejunte( $m );

	/* 1 — a junta manda, e precisa das DUAS pontas. Faixa com uma ponta só não é
	   faixa aberta, é faixa desconhecida: o produto fica fora da grade inteira e
	   a tela diz que a faixa dele não foi obtida. É o caso do rejunte piscinas,
	   o único do banco que nomeia pastilha de vidro submersa. */
	if ( null === $p['junta_min'] || null === $p['junta_max'] ) {
		return array( 'fora_da_junta', 0 );
	}
	if ( $junta_mm < $p['junta_min'] || $junta_mm > $p['junta_max'] ) {
		return array( 'fora_da_junta', 0 );
	}
	/* 3 — quem delimita ambiente fica fechado nele. */
	if ( $p['ambientes_delimitados'] && ! isset( $p['ambientes_delimitados'][ $ambiente ] ) ) {
		return array( 'fora_do_ambiente', 0 );
	}
	/* 2 — ambiente crítico exige declaração explícita. */
	$criticos = cdm_f2_criticos_rejunte();
	if ( isset( $criticos[ $ambiente ] ) && ! isset( $p['ambientes_cobertos'][ $ambiente ] ) ) {
		return array( 'fora_do_ambiente', 0 );
	}

	$score = 2 + ( isset( $p['ambientes_cobertos'][ $ambiente ] ) ? 2 : 0 );

	/* 4 — nível de fonte limita a recomendação primária. */
	if ( $p['nivel'] > cdm_f2_nivel_maximo() ) {
		return array( 'ressalva', $score );
	}

	return array( 'recomendado', $score );
}
}

if ( ! function_exists( 'cdm_f2_celula_rejunte' ) ) {
function cdm_f2_celula_rejunte( $junta_mm, $ambiente ) {
	$banco        = cdm_f2_banco();
	$recomendados = array();
	$ressalva     = array();
	$fora_junta   = array();
	$fora_amb     = array();

	foreach ( $banco['materiais'] as $id => $m ) {
		if ( 'rejunte' !== ( isset( $m['categoria'] ) ? $m['categoria'] : '' ) ) {
			continue;
		}
		list( $situacao, $score ) = cdm_f2_avaliar_rejunte( $m, $junta_mm, $ambiente );
		if ( 'recomendado' === $situacao ) {
			$recomendados[ $id ] = $score;
		} elseif ( 'ressalva' === $situacao ) {
			$ressalva[] = $id;
		} elseif ( 'fora_da_junta' === $situacao ) {
			$fora_junta[] = $id;
		} else {
			$fora_amb[] = $id;
		}
	}

	$topo   = array();
	$abaixo = array();
	if ( $recomendados ) {
		$maior = max( $recomendados );
		foreach ( $recomendados as $id => $score ) {
			if ( $score === $maior ) {
				$topo[] = $id;
			} else {
				$abaixo[] = $id;
			}
		}
	}
	sort( $topo );
	sort( $abaixo );
	sort( $ressalva );
	sort( $fora_junta );
	sort( $fora_amb );

	return array(
		'recomendados_topo'           => $topo,
		'elegiveis_abaixo_do_topo'    => $abaixo,
		'mencionados_com_ressalva'    => $ressalva,
		'eliminados_por_faixa_de_junta' => $fora_junta,
		'eliminados_por_ambiente'     => $fora_amb,
	);
}
}

/* ---------------------------------------------------------------------------
 * 4. A entrada, no vocabulário da pessoa
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f2_rotulos' ) ) {
/**
 * Os rótulos da tela. Palavras que a pessoa usa (VOZ.md): vaso, caquinho,
 * pastilha, cola, rejunte. "Substrato", "tessela" e "ficha" ficam de fora do
 * que ela lê — o vocabulário do fabricante aparece só na camada de prova.
 *
 * As CHAVES são o vocabulário controlado do esquema; se alguém acrescentar uma
 * base lá sem rótulo aqui, o teste reprova nas duas direções.
 */
function cdm_f2_rotulos() {
	return array(
		'base' => array(
			'ceramica_esmaltada_porcelana' => 'Cerâmica ou porcelana (vaso, azulejo, prato)',
			'vidro'                        => 'Vidro comum (garrafa, pote, vidro liso)',
			'vidro_laminado'               => 'Vidro laminado (o de para-brisa, com película no meio)',
			'espelho'                      => 'Espelho',
			'mdf_madeira'                  => 'MDF ou madeira',
			'cimento_concreto'             => 'Cimento ou concreto (vaso de cimento, tampo)',
			'alvenaria_tijolo'             => 'Alvenaria, tijolo ou pedra',
			'metal'                        => 'Metal (lata, bandeja, moldura de metal)',
			'plastico'                     => 'Plástico ou acrílico',
		),
		'base_curto' => array(
			'ceramica_esmaltada_porcelana' => 'cerâmica',
			'vidro'                        => 'vidro comum',
			'vidro_laminado'               => 'vidro laminado',
			'espelho'                      => 'espelho',
			'mdf_madeira'                  => 'MDF ou madeira',
			'cimento_concreto'             => 'cimento',
			'alvenaria_tijolo'             => 'alvenaria, tijolo ou pedra',
			'metal'                        => 'metal',
			'plastico'                     => 'plástico',
		),
		'ambiente' => array(
			'interno_seco'            => 'Dentro de casa, em lugar seco',
			'interno_molhado'         => 'Dentro de casa, em área molhada (banheiro, cozinha)',
			'externo_abrigado'        => 'Fora de casa, mas abrigado (varanda coberta)',
			'externo_exposto'         => 'Fora de casa, no sol e na chuva',
			'contato_permanente_agua' => 'Dentro da água o tempo todo (fonte, vaso com água)',
		),
		'ambiente_curto' => array(
			'interno_seco'            => 'dentro de casa, em lugar seco',
			'interno_molhado'         => 'na área molhada',
			'externo_abrigado'        => 'na varanda coberta',
			'externo_exposto'         => 'no sol e na chuva',
			'contato_permanente_agua' => 'dentro da água',
		),
		'tessela' => array(
			'pastilha_vidro'   => 'Pastilha de vidro',
			'pastilha_ceramica' => 'Pastilha de cerâmica',
			'caco_azulejo'     => 'Caquinho de azulejo',
			'caco_louca'       => 'Caquinho de louça ou prato',
			'caco_espelho'     => 'Caquinho de espelho',
			'pedra'            => 'Pedrinha ou pedra natural',
		),
	);
}
}

if ( ! function_exists( 'cdm_f2_entrada' ) ) {
/**
 * O que a pessoa escolheu, saneado contra o vocabulário — nunca contra uma
 * lista escrita aqui. Valor fora do vocabulário volta ao padrão em silêncio, e
 * o padrão é o caso mais comum do nicho: vaso de cerâmica, dentro de casa,
 * junta de 2 mm.
 */
function cdm_f2_entrada() {
	$rot  = cdm_f2_rotulos();
	$base = isset( $_GET['base'] ) ? sanitize_key( wp_unslash( $_GET['base'] ) ) : '';
	$amb  = isset( $_GET['onde'] ) ? sanitize_key( wp_unslash( $_GET['onde'] ) ) : '';
	$tes  = isset( $_GET['caco'] ) ? sanitize_key( wp_unslash( $_GET['caco'] ) ) : '';
	$jun  = isset( $_GET['junta'] ) ? (int) $_GET['junta'] : 0;

	$escolheu = ( isset( $rot['base'][ $base ] ) || isset( $rot['ambiente'][ $amb ] ) || $jun > 0 || isset( $rot['tessela'][ $tes ] ) );

	return array(
		'base'     => isset( $rot['base'][ $base ] ) ? $base : 'ceramica_esmaltada_porcelana',
		'ambiente' => isset( $rot['ambiente'][ $amb ] ) ? $amb : 'interno_seco',
		'tessela'  => isset( $rot['tessela'][ $tes ] ) ? $tes : 'pastilha_vidro',
		/* ATE 12 mm, e o teto NAO e enfeite: a grade conferida no esquema pisa em
		   11 mm de proposito — o primeiro valor depois do maior extremo que
		   algum fabricante declara (10 mm). Com o campo parando em 10, quem
		   tem folga de 11 caia calado no padrao de 2 mm e recebia uma resposta
		   que nao era a dele. Agora ele recebe a verdade: nenhum rejunte do
		   banco cobre essa folga. */
		'junta'    => ( $jun >= 1 && $jun <= 12 ) ? $jun : 2,
		'escolheu' => $escolheu,
	);
}
}

/* ---------------------------------------------------------------------------
 * 5. Peças de tela
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f2_nome' ) ) {
function cdm_f2_nome( $id ) {
	$banco = cdm_f2_banco();
	if ( ! isset( $banco['materiais'][ $id ] ) ) {
		return $id;
	}
	$m     = $banco['materiais'][ $id ];
	$marca = isset( $m['marca'] ) ? (string) $m['marca'] : '';
	$nome  = (string) $m['nome_comercial'];

	/* A marca só entra quando o nome do produto ainda não a carrega. Sem esta
	   linha a tela dizia "Quartzolit Rejunte Cerâmicas Quartzolit": os cinco
	   rejuntes têm a marca dentro do nome comercial e as cinco colas não. */
	if ( '' === $marca || false !== mb_stripos( $nome, $marca ) ) {
		return trim( $nome );
	}

	return trim( $marca . ' ' . $nome );
}
}

if ( ! function_exists( 'cdm_f2_fonte_principal' ) ) {
/** A fonte de melhor nível do material, com a data em que foi lida. */
function cdm_f2_fonte_principal( $m ) {
	$melhor = null;
	foreach ( (array) ( isset( $m['fontes'] ) ? $m['fontes'] : array() ) as $f ) {
		if ( null === $melhor || (int) $f['nivel'] < (int) $melhor['nivel'] ) {
			$melhor = $f;
		}
	}

	return $melhor;
}
}

if ( ! function_exists( 'cdm_f2_preparo' ) ) {
/**
 * O `preparo` de UM produto, nos três estados do esquema v12 — e a leitura é a
 * régua, não a prosa ao lado dela.
 *
 * Devolve `array( 'literal' => ..., 'fonte' => ... )` quando o fabricante
 * escreveu e a gente leu o documento dele; `array( 'literal' => null )` nos
 * outros dois estados. A tela serve o primeiro e NUNCA os outros dois.
 *
 * POR QUE A PARÁFRASE NÃO SOBE, e isto foi medido e não escolhido: de 10/09 a
 * 06/10/2026 nove registros carregaram `preparo` como texto solto, sem dizer de
 * qual documento tinham saído. Em 06/10 quatro deles puderam ser conferidos
 * contra a fonte, e AS QUATRO perdiam informação dela — uma fechou lista que o
 * fabricante deixou aberta, uma apagou o motivo de uma instrução, uma apagou a
 * condição que ele escreve dentro do preparo e uma apagou sete frases de oito.
 * Servir um resumo entre aspas seria publicar a instrução dele menos a parte
 * que a gente deixou cair, com o nome dele embaixo (seção 26.3).
 */
function cdm_f2_preparo( $m ) {
	$p = isset( $m['preparo'] ) && is_array( $m['preparo'] ) ? $m['preparo'] : array();
	if ( empty( $p['literal_do_fabricante'] ) || empty( $p['fonte_id'] ) ) {
		return array( 'literal' => null, 'fonte' => null );
	}
	$fontes = isset( $m['fontes'] ) && is_array( $m['fontes'] ) ? $m['fontes'] : array();
	if ( ! isset( $fontes[ $p['fonte_id'] ] ) ) {
		/* Fonte que o registro aponta e não tem é o mesmo que não ter fonte: a
		   frase não sobe sem o endereço dela. O validador do banco já reprova
		   isso; aqui a tela não depende de o portão ter rodado. */
		return array( 'literal' => null, 'fonte' => null );
	}

	return array(
		'literal'    => $p['literal_do_fabricante'],
		'fonte'      => $fontes[ $p['fonte_id'] ],
		'lido_em'    => isset( $p['lido_em'] ) ? $p['lido_em'] : '',
		/* O NOME QUE O LEITOR OUVE, e não o campo `tipo` da fonte. O `tipo` é
		   prosa de arquivo: o do boletim do rejunte piscinas chega sem um acento
		   ("boletim tecnico do fabricante, PDF ABERTO E LIDO pagina a pagina") e o
		   da cimentcola traz `escada_de_fontes` e o nome de um arquivo do
		   repositório dentro da frase. Foi um render que mostrou isso, não uma
		   ideia: a primeira versão deste bloco servia o `tipo`, como o bloco de
		   prova da cola ainda faz — e nas colas passa, porque o `tipo` delas é
		   curto e acentuado. */
		'documento'  => isset( $p['como_a_tela_chama_o_documento'] ) ? $p['como_a_tela_chama_o_documento'] : '',
	);
}
}

if ( ! function_exists( 'cdm_f2_preparo_provas' ) ) {
/**
 * AS PROCEDENCIAS DO PREPARO, uma frase por produto, para o chamador JUNTAR na
 * camada de prova que ele já abre. Nunca um bloco novo: o `teste-casca.php`
 * cobra no máximo DOIS `cdm-prova` por página, e a trava é o que impede
 * declarar a página inteira como camada de prova e desligar o portão de voz.
 */
function cdm_f2_preparo_provas( $ids ) {
	$banco  = cdm_f2_banco();
	$frases = array();
	foreach ( (array) $ids as $id ) {
		if ( ! isset( $banco['materiais'][ $id ] ) ) {
			continue;
		}
		$p = cdm_f2_preparo( $banco['materiais'][ $id ] );
		if ( ! $p['literal'] ) {
			continue;
		}
		$fonte    = $p['fonte'];
		$frases[] = esc_html( cdm_f2_nome( $id ) ) . ': o preparo está escrito '
			. esc_html( $p['documento'] ? $p['documento'] : 'num documento dele que a gente não soube nomear' )
			. ( ! empty( $p['lido_em'] ) && function_exists( 'cdm_casca_data_br' )
				? ', lido em ' . esc_html( cdm_casca_data_br( $p['lido_em'] ) ) : '' )
			. ( ! empty( $fonte['url'] ) ? ' (<a href="' . esc_url( $fonte['url'] ) . '" rel="nofollow noopener" target="_blank">abrir</a>)' : '' );
	}

	return $frases;
}
}

if ( ! function_exists( 'cdm_f2_preparo_html' ) ) {
/**
 * O BLOCO DE PREPARO DA RESPOSTA. Recebe os ids que a página acabou de
 * recomendar e o verbo da ação ("colar" ou "rejuntar"), e serve duas coisas: a
 * instrução de quem a tem, na palavra do fabricante, e o nome de quem não a
 * tem, com a causa.
 *
 * A SEGUNDA METADE É A QUE IMPORTA MAIS, e ela é a mesma cicatriz da prestação
 * de contas do rejunte: lista que só mostra quem passou faz o leitor ler
 * ausência como "não precisa de preparo". Não é isso que a ausência quer dizer
 * aqui — quer dizer que o servidor do fabricante recusa a gente, ou que ninguém
 * leu ainda, e as duas são nossas, não dele.
 */
function cdm_f2_preparo_html( $ids, $verbo ) {
	$banco = cdm_f2_banco();
	$com   = array();
	$sem   = array();

	foreach ( (array) $ids as $id ) {
		if ( ! isset( $banco['materiais'][ $id ] ) ) {
			continue;
		}
		$m = $banco['materiais'][ $id ];
		$p = cdm_f2_preparo( $m );
		if ( $p['literal'] ) {
			$com[ $id ] = $p;
		} else {
			$sem[] = $id;
		}
	}

	if ( ! $com && ! $sem ) {
		return '';
	}

	$html = '<div class="cdm-f2-preparo">';
	$html .= '<h3>Antes de ' . esc_html( $verbo ) . ', o que o fabricante manda fazer</h3>';

	/* A PROCEDENCIA NAO SAI AQUI, e isso nao e estilo: ela sai em
	   `cdm_f2_preparo_provas()`, para o chamador juntar a camada de prova que ele
	   ja tem. A primeira versao deste bloco abria um `cdm-prova` por literal, e o
	   `teste-casca.php` reprovou na hora — a pagina passou a servir TRES camadas
	   de prova, e o maximo e DOIS. A trava existe porque embrulhar a pagina
	   inteira em `cdm-prova` e a porta dos fundos do portao de voz: quem pode
	   abrir quantos blocos quiser desliga a regua sem mudar uma palavra. */
	foreach ( $com as $id => $p ) {
		$html .= '<p class="cdm-f2-preparo-item"><strong>' . esc_html( cdm_f2_nome( $id ) ) . '</strong>: '
			. '<em>' . esc_html( $p['literal'] ) . '</em></p>';
	}

	if ( $sem ) {
		$nomes = array();
		foreach ( $sem as $id ) {
			$nomes[] = cdm_f2_nome( $id );
		}
		$html .= '<p class="cdm-f2-silencio">De <strong>' . esc_html( cdm_f2_lista_humana( $nomes ) )
			. '</strong> a gente não tem a instrução de preparo na palavra do fabricante: o documento '
			. 'dele não abre daqui, ou ninguém o leu ainda. A gente prefere dizer isso a resumir — '
			. 'resumo de instrução é instrução pela metade, e o nome que ficaria embaixo dela é o dele.</p>';
	}

	$html .= '</div>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f2_lista_humana' ) ) {
/** "a, b e c" — como gente escreve, nunca "a, b, c". */
function cdm_f2_lista_humana( $itens ) {
	$itens = array_values( array_unique( array_filter( (array) $itens ) ) );
	$n     = count( $itens );
	if ( 0 === $n ) {
		return '';
	}
	if ( 1 === $n ) {
		return $itens[0];
	}
	$ultimo = array_pop( $itens );

	return implode( ', ', $itens ) . ' e ' . $ultimo;
}
}

if ( ! function_exists( 'cdm_f2_compra_html' ) ) {
/**
 * O BLOCO DE COMPRA, E ELE DESCE A ESCADA DA SEÇÃO 25 DO CONTRATO.
 *
 * Até a 1.1.0 este bloco tinha dois estados: link de ficha, ou a etiqueta "Link
 * de loja em breve". A seção 25.2 — decisão do Raphael de 13/09/2026, textual,
 * "deve ser 100% automático sem eu tocar" — criou um terceiro, e ele é o mais
 * importante dos três: **a busca é o PISO de todo item, e piso não espera
 * ninguém.** O link de busca já estava no banco desde 13/09; o que faltava era
 * a tela, e é essa a metade que esta versão entrega.
 *
 * OS TRÊS ESTADOS, e o que cada um diz ao leitor:
 *
 * 1. TEM FICHA — a ficha é o botão ("Ver na loja") e a busca desce para a linha
 *    discreta logo abaixo ("Veja todos disponíveis aqui"), palavra por palavra
 *    como a 25.2 a escreve. As duas convivem de propósito: ficha converte
 *    melhor, e a busca é a saída de quem chegou num anúncio esgotado. O degrau 3
 *    da escada — anúncio de vendedor comum — é justamente o que quebrou quatro
 *    links em doze horas, e é ele que mais precisa dessa segunda porta.
 * 2. SÓ TEM BUSCA — a busca SOBE e vira o botão, com texto próprio ("Ver as
 *    opções na loja"). O texto muda junto com o papel, e não por estilo: o botão
 *    abre uma LISTA, não um produto, e prometer "Ver na loja" ali seria o leitor
 *    clicar esperando a ficha do que a página acabou de recomendar. A 25.2 manda
 *    que este caso nunca diga "em breve" — a página está monetizada.
 * 3. SÓ TEM A BUSCA CRUA — nasceu em 14/09/2026 e é o degrau que fez a etiqueta
 *    "Link de loja em breve" SUMIR desta ilha. A busca crua
 *    (`afiliado.url_busca_produto`, `shopee.com.br/search?keyword=…`) vira o
 *    botão, com o MESMO texto do estado 2, porque para quem lê os dois abrem a
 *    mesma coisa: uma lista na loja. O que muda é o `rel`, e essa parte não é
 *    estética — ver abaixo.
 * 4. NÃO TEM NADA — a etiqueta sumiu e no lugar dela ficou uma FALHA DURA do
 *    `validar-banco.py`. Este ramo não imprime mais promessa nenhuma: ele
 *    devolve o bloco vazio, porque item sem nenhuma saída de compra não pode
 *    chegar ao ar (seção 7, 14/09/2026: a frase "link de loja em breve" está
 *    proibida e item que chegaria a ela é defeito, não estado de espera).
 *
 * O QUE ESTE BLOCO CORRIGIU, e ele vale mais do que a frase que saiu: os 15
 * itens que caíam na etiqueta JÁ TINHAM a palavra-chave da busca escrita no
 * banco — dois em `url_busca_produto` desde 13/09, e os treze da pastilha foram
 * escritos agora. Em nenhum momento faltou decisão; faltava a TELA ler o campo.
 * É a mesma distância entre repositório e ar que a seção 4 do contrato paga mais
 * caro, uma camada abaixo.
 *
 * POR QUE ISTO É FUNÇÃO PRÓPRIA, e não um `if` dentro do cartão: a escada é
 * regra do Arquipélago e o cartão é desenho desta ilha. Quem for servir a escada
 * na ficha do Guia, na vitrine de pastilha da F1 ou na página da peça chama esta
 * função em vez de reescrever os quatro estados — e três cópias de uma escada de
 * quatro degraus é o jeito mais curto de dois degraus discordarem em silêncio.
 *
 * O `rel` SAI DO QUE O LINK É, NUNCA DO FORMATO DA PÁGINA DE DESTINO.
 * `rel="sponsored"` é a declaração de uma relação PAGA: vale para a ficha e para
 * a busca ENCURTADA, que são links de afiliado e rendem comissão. A busca CRUA
 * não rende nada — ninguém paga por aquele clique —, então ela sai
 * `rel="nofollow noopener"`. Chamar de patrocinado um link que não paga seria
 * mentir ao leitor sobre a única coisa que ele tem o direito de saber sobre nós.
 */
function cdm_f2_compra_html( $afiliado ) {
	$ficha = ( is_array( $afiliado ) && ! empty( $afiliado['url'] ) ) ? $afiliado['url'] : '';
	$busca = ( is_array( $afiliado ) && ! empty( $afiliado['url_busca'] ) ) ? $afiliado['url_busca'] : '';
	$crua  = ( is_array( $afiliado ) && ! empty( $afiliado['url_busca_produto'] ) ) ? $afiliado['url_busca_produto'] : '';

	$html = '<span class="cdm-f2-compra">';

	if ( '' !== $ficha ) {
		$html .= '<a class="cdm-f2-botao" href="' . esc_url( $ficha ) . '"'
			. ' rel="sponsored noopener" target="_blank">Ver na loja</a>';
		if ( '' !== $busca ) {
			$html .= '<a class="cdm-f2-busca" href="' . esc_url( $busca ) . '"'
				. ' rel="sponsored noopener" target="_blank">Veja todos disponíveis aqui</a>';
		}
	} elseif ( '' !== $busca ) {
		$html .= '<a class="cdm-f2-botao cdm-f2-botao-busca" href="' . esc_url( $busca ) . '"'
			. ' rel="sponsored noopener" target="_blank">Ver as opções na loja</a>';
	} elseif ( '' !== $crua ) {
		$html .= '<a class="cdm-f2-botao cdm-f2-botao-busca cdm-f2-botao-busca-crua" href="' . esc_url( $crua ) . '"'
			. ' rel="nofollow noopener" target="_blank">Ver as opções na loja</a>';
	}

	$html .= '</span>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f2_cartao_html' ) ) {
/**
 * O cartão do bloco de compra (seção 6 e 7 do contrato).
 *
 * Traz a declaração que fez o produto entrar — "cerâmica" e "azulejo" saídos da
 * lista do fabricante, não adjetivo de marketing —, o bloco de compra e, depois
 * de tudo, o link discreto de procedência. Produto sem foto NÃO some: aparece
 * com espaço reservado neutro, porque perder a recomendação certa por falta de
 * imagem é trocar o certo pelo bonito.
 *
 * O BLOCO DE COMPRA DESCE A ESCADA DA SEÇÃO 25 — ver `cdm_f2_compra_html()`.
 */
function cdm_f2_cartao_html( $id, $motivo, $classe = '' ) {
	$banco = cdm_f2_banco();
	if ( ! isset( $banco['materiais'][ $id ] ) ) {
		return '';
	}
	$m     = $banco['materiais'][ $id ];
	$fonte = cdm_f2_fonte_principal( $m );

	$html  = '<li class="cdm-f2-cartao' . ( $classe ? ' ' . esc_attr( $classe ) : '' ) . '">';

	if ( ! empty( $m['imagem']['url'] ) ) {
		$html .= '<img class="cdm-f2-foto" src="' . esc_url( $m['imagem']['url'] ) . '"'
			. ' width="' . (int) $m['imagem']['largura'] . '" height="' . (int) $m['imagem']['altura'] . '"'
			. ' loading="lazy" alt="' . esc_attr( $m['imagem']['alt'] ) . '">';
	} else {
		$html .= '<span class="cdm-f2-sem-foto" aria-hidden="true"></span>';
	}

	$html .= '<span class="cdm-f2-marca">' . esc_html( isset( $m['marca'] ) ? $m['marca'] : '' ) . '</span>';
	$html .= '<h3>' . esc_html( $m['nome_comercial'] ) . '</h3>';
	if ( '' !== $motivo ) {
		$html .= '<p class="cdm-f2-motivo">' . $motivo . '</p>';
	}

	/* O BLOCO DE COMPRA VEM ANTES DA PROCEDÊNCIA, e nasce mesmo vazio. */
	$html .= cdm_f2_compra_html( isset( $m['afiliado'] ) ? $m['afiliado'] : array() );

	if ( $fonte && ! empty( $fonte['url'] ) ) {
		$html .= '<span class="cdm-f2-fonte"><a href="' . esc_url( $fonte['url'] ) . '"'
			. ' rel="nofollow noopener" target="_blank">fonte</a>'
			. ' · lido em ' . esc_html( cdm_casca_data_br( $fonte['coletado_em'] ) ) . '</span>';
	}

	$html .= '</li>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f2_motivo_indicacao' ) ) {
/** "o fabricante escreve cerâmica e azulejo" — os literais que casaram. */
function cdm_f2_motivo_indicacao( $id, $base, $ambiente ) {
	$banco = cdm_f2_banco();
	$m     = $banco['materiais'][ $id ];
	$p     = cdm_f2_perfil_cola( $m );
	$termos = isset( $p['literais_indicacao'][ $base ] ) ? $p['literais_indicacao'][ $base ] : array();
	$amb    = isset( $p['literais_cobertura'][ $ambiente ] ) ? $p['literais_cobertura'][ $ambiente ] : array();

	$texto = '';
	if ( $termos ) {
		$texto = 'A ' . esc_html( $m['fabricante'] ) . ' escreve <em>'
			. esc_html( cdm_f2_lista_humana( $termos ) ) . '</em> entre as superfícies deste produto.';
	}
	if ( $amb ) {
		$texto .= ' Declara também <em>' . esc_html( cdm_f2_lista_humana( $amb ) ) . '</em>.';
	}

	return $texto;
}
}

if ( ! function_exists( 'cdm_f2_motivo_proibicao' ) ) {
function cdm_f2_motivo_proibicao( $id, $base, $ambiente ) {
	$banco  = cdm_f2_banco();
	$m      = $banco['materiais'][ $id ];
	$p      = cdm_f2_perfil_cola( $m );
	$termos = array();
	foreach ( array( $base, $ambiente ) as $alvo ) {
		if ( isset( $p['literais_proibicao'][ $alvo ] ) ) {
			$termos = array_merge( $termos, $p['literais_proibicao'][ $alvo ] );
		}
	}
	if ( ! $termos ) {
		return '';
	}

	return 'A ' . esc_html( $m['fabricante'] ) . ' escreve <em>' . esc_html( cdm_f2_lista_humana( $termos ) )
		. '</em> na lista do que este produto não deve tocar.';
}
}

/* ---------------------------------------------------------------------------
 * 6. A resposta
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f2_resposta_cola_html' ) ) {
function cdm_f2_resposta_cola_html( $base, $ambiente, $tessela ) {
	$rot    = cdm_f2_rotulos();
	$celula = cdm_f2_celula_cola( $base, $ambiente, $tessela );
	$nb     = $rot['base_curto'][ $base ];
	$na     = $rot['ambiente_curto'][ $ambiente ];

	$html = '<div class="cdm-f2-resposta">';

	if ( $celula['recomendados_topo'] ) {
		$nomes = array();
		foreach ( $celula['recomendados_topo'] as $id ) {
			$nomes[] = cdm_f2_nome( $id );
		}
		$quantos = count( $nomes );
		$html   .= '<p class="cdm-f2-frase">Para colar em <strong>' . esc_html( $nb ) . '</strong>, numa peça que vai ficar <strong>'
			. esc_html( $na ) . '</strong>, use <strong>' . esc_html( cdm_f2_lista_humana( $nomes ) ) . '</strong>'
			. ( $quantos > 1 ? ' — os ' . ( 2 === $quantos ? 'dois' : $quantos ) . ' servem aqui, e a gente não escolhe por você o que o fabricante não separou.' : '.' )
			. '</p>';
	} elseif ( $celula['eliminados_por_proibicao_da_peca'] ) {
		/* A SEXTA CAUSA, e ela precisou de frase própria pelo mesmo motivo que a
		   quarta: não é nenhuma das cinco anteriores. Não é silêncio (o
		   fabricante falou), não é condição (ele não pôs exigência: ele proibiu)
		   e não é a proibição de base, que fala de onde a peça fica, não do que
		   se cola. E é a única das seis que não tem conserto trocando o
		   ambiente: só trocando o caquinho — e é isso que a frase diz. */
		$nomes = array();
		foreach ( $celula['eliminados_por_proibicao_da_peca'] as $id ) {
			$nomes[] = cdm_f2_nome( $id );
		}
		$quantos = count( $nomes );
		$html   .= '<p class="cdm-f2-frase cdm-f2-faixa">Não dá para indicar cola aqui com esse '
			. 'caquinho, e o motivo não é falta de declaração: <strong>'
			. esc_html( cdm_f2_lista_humana( $nomes ) ) . '</strong> '
			. ( 1 === $quantos ? 'é declarado' : 'são declarados' ) . ' pelo fabricante para <strong>'
			. esc_html( $nb ) . '</strong>, e o mesmo fabricante escreve que não se usa '
			. ( 1 === $quantos ? 'esse produto' : 'esses produtos' ) . ' no que você vai colar. '
			. 'Logo abaixo está a frase dele, e com que caquinho a resposta mudaria.</p>';
	} elseif ( $celula['eliminados_por_condicao'] ) {
		/* A RECUSA NOMEIA A CAUSA QUE A PÁGINA MEDIU (seção 7 do ARQUIPELAGO.md).
		   A frase antiga dizia "nenhum dos adesivos do nosso banco é declarado
		   pelo próprio fabricante para esse caso", e ela era verdadeira enquanto
		   só existiam duas causas de exclusão. Com a regra 6 ela passou a ser
		   FALSA exatamente onde mais importa: em plástico, dentro de casa, o
		   Cascola PL500 É declarado pelo fabricante — ele só não cumpre uma
		   condição que este par de superfícies não atende. Dizer "ninguém
		   declara" ali seria afirmar sobre uma declaração que existe, e no mesmo
		   parágrafo em que a página está prestes a citá-la. */
		$nomes = array();
		foreach ( $celula['eliminados_por_condicao'] as $id ) {
			$nomes[] = cdm_f2_nome( $id );
		}
		$quantos = count( $nomes );
		$html   .= '<p class="cdm-f2-frase cdm-f2-faixa">Não dá para indicar cola aqui, e o motivo '
			. 'não é falta de declaração: <strong>' . esc_html( cdm_f2_lista_humana( $nomes ) ) . '</strong> '
			. ( 1 === $quantos ? 'é declarado' : 'são declarados' ) . ' pelo fabricante para <strong>'
			. esc_html( $nb ) . '</strong>, mas ' . ( 1 === $quantos ? 'exige' : 'exigem' )
			. ' uma condição que este caso não cumpre. Logo abaixo está qual é, e o que mudaria.</p>';
	} elseif ( $celula['mencionados_com_ressalva'] ) {
		/* A QUINTA CAUSA, e ela é a MESMA cicatriz da anterior aparecendo noutro
		   lugar — achada em 13/09/2026 pela matriz escrita à mão indo de 18 para
		   45 células. As 18 antigas TODAS tinham recomendação, então nenhuma
		   régua independente jamais pisou numa faixa descoberta, e o `else` aqui
		   embaixo era código morto para o portão. Ele estava no ar em quatro
		   estados: vidro, madeira, alvenaria e metal em contato permanente com
		   água. Nos quatro a página dizia "nenhum dos adesivos do nosso banco é
		   declarado pelo próprio fabricante para esse caso" — e duas seções
		   abaixo, na mesma página, imprimia "existe menção a Loctite Durepoxi".
		   A frase era FALSA: a Henkel declara metal e declara secar submerso, as
		   duas coisas. O que segura a recomendação é a PROCEDÊNCIA da fonte, que
		   é régua nossa (regra 5), não o silêncio do fabricante, que é fato dele.
		   Trocar uma causa pela outra é a mistura que a seção 7 do contrato
		   proíbe, e ela é pior aqui do que em qualquer outro lugar da página:
		   está dentro da frase que o leitor recebe como confissão de honestidade.

		   A ATRIBUIÇÃO SAI DIVIDIDA, como na regra 6 (seção 26.3): a declaração
		   é do fabricante e o nível do documento é classificação da ilha — duas
		   orações separadas, e o tipo do documento é LIDO do banco, nunca
		   digitado aqui. */
		$nomes = array();
		$tipos = array();
		foreach ( $celula['mencionados_com_ressalva'] as $id ) {
			$banco   = cdm_f2_banco();
			$m       = $banco['materiais'][ $id ];
			$fonte   = cdm_f2_fonte_principal( $m );
			$nomes[] = cdm_f2_nome( $id );
			$tipos[] = $fonte ? $fonte['tipo'] : 'fonte não registrada';
		}
		$quantos = count( $nomes );
		$html   .= '<p class="cdm-f2-frase cdm-f2-faixa">Não temos cola para indicar em <strong>'
			. esc_html( $nb ) . '</strong> ' . esc_html( $na ) . ', e o motivo não é falta de declaração: '
			. '<strong>' . esc_html( cdm_f2_lista_humana( $nomes ) ) . '</strong> '
			. ( 1 === $quantos ? 'é declarado' : 'são declarados' ) . ' pelo próprio fabricante para esse caso. '
			. 'O que segura a recomendação é a procedência, e essa régua é nossa: '
			. ( 1 === $quantos ? 'o que sustenta essa declaração é ' : 'o que sustenta essas declarações são ' )
			. esc_html( cdm_f2_lista_humana( $tipos ) ) . '. '
			. 'Em cima disso a gente não publica recomendação — a menção fica logo abaixo, com o documento.</p>';
	} else {
		$html .= '<p class="cdm-f2-frase cdm-f2-faixa">Não temos cola para indicar em <strong>' . esc_html( $nb )
			. '</strong> ' . esc_html( $na ) . '. Nenhum dos adesivos do nosso banco é declarado pelo próprio fabricante para esse caso — e a gente prefere dizer isso a chutar o de sempre.</p>';
	}

	/* A camada de prova: a mesma resposta, agora com quem declarou, em qual
	   documento e em que dia foi lido (seção 15.2 — a prova desce um parágrafo,
	   dentro da mesma caixa, para quem citar a caixa levar a fonte junto). */
	$provas = array();
	foreach ( array_merge( $celula['recomendados_topo'], $celula['elegiveis_abaixo_do_topo'] ) as $id ) {
		$banco  = cdm_f2_banco();
		$m      = $banco['materiais'][ $id ];
		$p      = cdm_f2_perfil_cola( $m );
		$fonte  = cdm_f2_fonte_principal( $m );
		$termos = isset( $p['literais_indicacao'][ $base ] ) ? $p['literais_indicacao'][ $base ] : array();
		$provas[] = esc_html( cdm_f2_nome( $id ) ) . ': o fabricante declara <em>'
			. esc_html( cdm_f2_lista_humana( $termos ) ) . '</em> ('
			. esc_html( $fonte ? $fonte['tipo'] : 'fonte não registrada' ) . ', lido em '
			. esc_html( cdm_casca_data_br( $fonte ? $fonte['coletado_em'] : '' ) ) . ')';
	}
	/* A PROVA DESCEU PARA O FIM DA CAIXA em 06/10/2026, com o bloco de preparo.
	   Antes ela saía aqui, logo depois da frase, e o preparo teria de abrir uma
	   segunda camada de prova para citar o documento dele — o que estoura a trava
	   de DOIS blocos do `teste-casca.php`. Com uma caixa só no pé, a página tem
	   UMA camada de prova por resposta, que é o que o VOZ.md pede com outras
	   palavras: "número, fonte e data moram na camada de prova, nunca na voz". */

	/* A CONDIÇÃO DE QUEM FICOU, e a atribuição dividida ao meio (seção 26.3 do
	   ARQUIPELAGO.md). O fabricante declarou a CONDIÇÃO — "ao menos uma das
	   superfícies deve ser porosa" — e não declarou QUAIS superfícies são
	   porosas: quem classifica o MDF, o caquinho de azulejo e o vidro somos nós.
	   Escrever "a Cascola declara que a pastilha de cerâmica é porosa" seria
	   emprestar autoridade dela para uma frase nossa, que é exatamente o defeito
	   que a 26.3 nomeia. Por isso as duas metades saem em orações separadas, e o
	   portão mede que as duas estão lá. */
	$com_condicao = array();
	foreach ( array_merge( $celula['recomendados_topo'], $celula['elegiveis_abaixo_do_topo'] ) as $id ) {
		$banco = cdm_f2_banco();
		$m     = $banco['materiais'][ $id ];
		if ( ! cdm_f2_exige_porosa( $m ) ) {
			continue;
		}
		$p        = cdm_f2_porosas();
		$quem     = isset( $p['bases'][ $base ] )
			? $rot['base_curto'][ $base ]
			: mb_strtolower( $rot['tessela'][ $tessela ], 'UTF-8' );
		$com_condicao[] = '<strong>' . esc_html( cdm_f2_nome( $id ) ) . '</strong> só serve aqui '
			. 'porque uma das duas superfícies é porosa. A ' . esc_html( $m['fabricante'] )
			. ' escreve <em>' . esc_html( $m['condicoes']['exige_superficie_porosa']['literal'] )
			. '</em>; quem diz que <em>' . esc_html( $quem ) . '</em> é a superfície porosa deste caso '
			. 'somos nós, não ela.';
	}
	if ( $com_condicao ) {
		$html .= '<div class="cdm-f2-condicao"><p>' . implode( ' ', $com_condicao ) . '</p></div>';
	}

	/* O PREPARO (esquema v12, 06/10/2026). Ele vem DEPOIS da prova e da condição
	   de propósito: a prova diz por que este produto foi indicado, a condição diz
	   o que ele exige das superfícies, e só então a página diz o que fazer antes
	   de passar cola. Quem lê de cima para baixo recebe a decisão, o motivo e a
	   instrução nessa ordem.

	   Ele cobre o MESMO conjunto do bloco de prova — o topo mais os elegíveis que
	   a frase nomeia — e não a vitrine: produto que a página não indicou não
	   recebe instrução de aplicação, porque instrução sem indicação é receita de
	   usar o que a gente acabou de dizer que não serve. */
	$recomendados = array_merge( $celula['recomendados_topo'], $celula['elegiveis_abaixo_do_topo'] );
	$html .= cdm_f2_preparo_html( $recomendados, 'colar' );

	$provas = array_merge( $provas, cdm_f2_preparo_provas( $recomendados ) );
	if ( $provas ) {
		$html .= '<div class="cdm-prova"><p>' . implode( '. ', $provas ) . '.</p></div>';
	}

	$html .= '</div>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f2_vitrine_html' ) ) {
/**
 * O carrossel de compra. Ordem: (1) elegibilidade técnica completa; (2)
 * adequação; (3) ter link de loja SÓ como desempate entre equivalentes. Nunca
 * comparar comissão, nunca promover produto pior porque paga mais.
 */
function cdm_f2_vitrine_html( $base, $ambiente, $tessela ) {
	$celula = cdm_f2_celula_cola( $base, $ambiente, $tessela );
	$banco  = cdm_f2_banco();

	$ordem = $celula['recomendados_topo'];
	/* Desempate permitido, e o único: entre equivalentes, quem tem link de loja
	   aparece antes. Estável: quem já estava na frente continua na frente quando
	   nenhum dos dois tem link (que é o estado de hoje, com os dez itens vazios). */
	usort( $ordem, function ( $a, $b ) use ( $banco ) {
		$la = empty( $banco['materiais'][ $a ]['afiliado']['url'] ) ? 1 : 0;
		$lb = empty( $banco['materiais'][ $b ]['afiliado']['url'] ) ? 1 : 0;
		if ( $la === $lb ) {
			return strcmp( $a, $b );
		}

		return $la - $lb;
	} );

	$html = '<div class="cdm-f2-secao">';
	$html .= '<h2>Onde comprar</h2>';

	if ( ! $ordem && ! $celula['elegiveis_abaixo_do_topo'] ) {
		/* Mesma correção de escopo da frase de recusa: onde quem caiu foi a
		   condição, "nenhum produto passa no que o fabricante declara" é falso —
		   ele passa no que o fabricante declara e não passa na condição que o
		   mesmo fabricante põe. E o terceiro ramo nasceu junto com a matriz de 45
		   em 13/09/2026, pelo mesmo motivo e no mesmo lugar: quando existe menção
		   de nível 4, o produto TAMBÉM passa no que o fabricante declara, e quem
		   o segura é a régua de procedência da ilha. A vitrine vazia repetia a
		   frase errada da resposta, uma seção acima dela. */
		if ( $celula['eliminados_por_condicao'] ) {
			$html .= '<p>Não há o que listar aqui. Não é que ninguém sirva para esta base: é que quem serve põe uma condição que este caso não cumpre, e ela está explicada logo abaixo. Vender assim mesmo seria o contrário do que esta página existe para fazer.</p>';
		} elseif ( $celula['mencionados_com_ressalva'] ) {
			$html .= '<p>Não há o que listar aqui. Não é que ninguém declare esta combinação: é que a única declaração que existe está apoiada em documento fraco demais para virar recomendação, e ela está nomeada logo abaixo. Vender assim mesmo seria o contrário do que esta página existe para fazer.</p>';
		} else {
			$html .= '<p>Não há o que listar aqui: nesta combinação nenhum produto do nosso banco passa no que o fabricante declara. Listar assim mesmo seria o contrário do que esta página existe para fazer.</p>';
		}
		$html .= '</div>';

		return $html;
	}

	$html .= '<ul class="cdm-f2-vitrine">';
	foreach ( $ordem as $id ) {
		$html .= cdm_f2_cartao_html( $id, cdm_f2_motivo_indicacao( $id, $base, $ambiente ) );
	}
	foreach ( $celula['elegiveis_abaixo_do_topo'] as $id ) {
		$html .= cdm_f2_cartao_html( $id, cdm_f2_motivo_indicacao( $id, $base, $ambiente ), 'cdm-f2-segundo' );
	}
	$html .= '</ul>';
	$html .= '<p class="cdm-f2-aviso">Alguns links desta página são de loja parceira e podem nos render comissão, sem mudar o seu preço — e sem mudar a ordem da lista, que sai do que o fabricante declara. Quem manda aqui é a ' . cdm_casca_link_html( 'divulgacao-de-afiliados', 'nossa regra de divulgação' ) . '.</p>';
	$html .= '</div>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f2_fora_html' ) ) {
/**
 * "O que não usar neste caso" — a seção que nenhuma outra página em português
 * tem, e a razão de a ferramenta existir.
 *
 * Dois grupos, com frases DIFERENTES, porque as duas coisas são diferentes:
 * proibido pelo fabricante não é a mesma coisa que não declarado por ele.
 * Misturar os dois seria inventar proibição — que é tão desonesto quanto
 * inventar indicação.
 */
function cdm_f2_fora_html( $base, $ambiente, $tessela ) {
	$celula = cdm_f2_celula_cola( $base, $ambiente, $tessela );
	$rot    = cdm_f2_rotulos();
	$banco  = cdm_f2_banco();

	if ( ! $celula['eliminados_por_proibicao'] && ! $celula['eliminados_por_silencio']
		&& ! $celula['mencionados_com_ressalva'] && ! $celula['eliminados_por_condicao']
		&& ! $celula['eliminados_por_proibicao_da_peca'] ) {
		return '';
	}

	$html = '<div class="cdm-f2-secao cdm-f2-fora">';
	$html .= '<h2>O que não usar em ' . esc_html( $rot['base_curto'][ $base ] ) . ', e por quê</h2>';

	if ( $celula['eliminados_por_proibicao'] ) {
		$html .= '<ul class="cdm-f2-lista-fora">';
		foreach ( $celula['eliminados_por_proibicao'] as $id ) {
			$html .= '<li><strong>' . esc_html( cdm_f2_nome( $id ) ) . '</strong> — '
				. cdm_f2_motivo_proibicao( $id, $base, $ambiente ) . '</li>';
		}
		$html .= '</ul>';
	}

	if ( $celula['eliminados_por_silencio'] ) {
		$nomes = array();
		foreach ( $celula['eliminados_por_silencio'] as $id ) {
			$nomes[] = cdm_f2_nome( $id );
		}
		$html .= '<p class="cdm-f2-silencio">Estes não estão proibidos, mas também não estão indicados: '
			. esc_html( cdm_f2_lista_humana( $nomes ) )
			. '. O fabricante simplesmente não fala desta superfície, e silêncio não vira "pode".</p>';

		/* A DECLARAÇÃO VAGA NÃO É SILÊNCIO, e merece ser dita com o nome dela.
		   "Certos tipos de plástico" não nomeia tipo nenhum: o produto não entra
		   nos recomendados, mas dizer só "o fabricante não fala" seria falso —
		   ele falou, e falou de um jeito que não dá para usar. É a diferença
		   entre não ter dado e ter dado que não decide. */
		$vagos = array();
		foreach ( $celula['eliminados_por_silencio'] as $id ) {
			$p = cdm_f2_perfil_cola( $banco['materiais'][ $id ] );
			if ( isset( $p['bases_vagas'][ $base ] ) && isset( $p['literais_indicacao'][ $base ] ) ) {
				$vagos[] = esc_html( cdm_f2_nome( $id ) ) . ' (o fabricante escreve <em>'
					. esc_html( cdm_f2_lista_humana( $p['literais_indicacao'][ $base ] ) ) . '</em>)';
			}
		}
		if ( $vagos ) {
			$html .= '<p class="cdm-f2-silencio">Um caso à parte: ' . implode( '; ', $vagos )
				. '. Isso não nomeia material nenhum, então não dá para virar recomendação — é declaração que existe e não decide.</p>';
		}
	}

	if ( $celula['mencionados_com_ressalva'] ) {
		$nomes = array();
		foreach ( $celula['mencionados_com_ressalva'] as $id ) {
			$nomes[] = cdm_f2_nome( $id );
		}
		$html .= '<p class="cdm-f2-ressalva">Existe menção a ' . esc_html( cdm_f2_lista_humana( $nomes ) )
			. ', mas o que sustenta isso é material de imprensa do fabricante, não documento de produto — por isso ele aparece aqui embaixo e não na recomendação.</p>';
	}

	/* O GRUPO DA CONDIÇÃO — quarta causa, e ela precisou de frase própria porque
	   não é nenhuma das três anteriores. Não é proibição: o fabricante não proíbe
	   nada aqui. Não é silêncio: ele falou, e falou desta superfície. Não é fonte
	   fraca: a fonte é a mesma que sustenta a recomendação dele em outros casos.
	   É uma condição que ESTA combinação não cumpre — e juntar isso ao balde do
	   silêncio seria a mistura de causas que a seção 7 do contrato proíbe desde
	   12/09/2026, escrita nesta mesma ilha. */
	if ( $celula['eliminados_por_condicao'] ) {
		foreach ( $celula['eliminados_por_condicao'] as $id ) {
			$m = $banco['materiais'][ $id ];
			if ( ! cdm_f2_condicao_conhecida() ) {
				/* A classificação sumiu do esquema. A direção segura é não
				   recomendar, e a frase honesta é dizer o que aconteceu — nunca
				   acusar as superfícies de uma coisa que ninguém mediu. */
				$html .= '<p class="cdm-f2-condicao-fora"><strong>' . esc_html( cdm_f2_nome( $id ) )
					. '</strong> — a ' . esc_html( $m['fabricante'] ) . ' exige uma condição de superfície '
					. 'para este produto e a nossa classificação de superfícies não está disponível agora, '
					. 'então ele fica de fora. Preferimos deixar de indicar a indicar sem conferir.</p>';
				continue;
			}
			$html .= '<p class="cdm-f2-condicao-fora"><strong>' . esc_html( cdm_f2_nome( $id ) )
				. '</strong> — não está proibido e não é falta de declaração: a '
				. esc_html( $m['fabricante'] ) . ' escreve <em>'
				. esc_html( $m['condicoes']['exige_superficie_porosa']['literal'] ) . '</em>, e '
				. 'nem <em>' . esc_html( $rot['base_curto'][ $base ] )
				. '</em> nem <em>' . esc_html( mb_strtolower( $rot['tessela'][ $tessela ], 'UTF-8' ) )
				. '</em> absorvem água. Essa última parte é classificação nossa, não dela. '
				. 'Trocando por ' . esc_html( cdm_f2_caquinhos_porosos_lista() ) . ', ele voltaria a servir.</p>';
		}
	}

	/* O GRUPO DA PROIBIÇÃO DE PEÇA — sexta causa, e a atribuição sai dividida ao
	   meio, igual à da regra 6 (seção 26.3). O fabricante declarou a PROIBIÇÃO —
	   "espelhos" — e não declarou QUAIS caquinhos do nosso vocabulário são
	   espelho: classificar o caco de espelho dentro dessa palavra é leitura
	   nossa. Escrever "a Tekbond declara que caco de espelho é espelho" seria
	   emprestar a autoridade dela para uma frase nossa — e aqui a tentação é
	   maior que na regra 6, porque a nossa leitura parece óbvia. */
	if ( $celula['eliminados_por_proibicao_da_peca'] ) {
		foreach ( $celula['eliminados_por_proibicao_da_peca'] as $id ) {
			$m      = $banco['materiais'][ $id ];
			$grupos = cdm_f2_peca_proibida( $m, $tessela );
			if ( ! cdm_f2_grupos_de_peca_conhecidos() ) {
				/* A classificação sumiu do esquema. A direção segura é não
				   recomendar, e a frase honesta é dizer o que aconteceu. */
				$html .= '<p class="cdm-f2-peca-fora"><strong>' . esc_html( cdm_f2_nome( $id ) )
					. '</strong> — a ' . esc_html( $m['fabricante'] ) . ' proíbe este produto em '
					. 'certo tipo de peça e a nossa classificação de caquinhos não está '
					. 'disponível agora, então ele fica de fora. Preferimos deixar de indicar '
					. 'a indicar sem conferir.</p>';
				continue;
			}
			$literais = array();
			foreach ( $grupos as $g ) {
				if ( isset( $m['condicoes']['proibe_grupos_de_tessela']['literais'][ $g ] ) ) {
					$literais[] = $m['condicoes']['proibe_grupos_de_tessela']['literais'][ $g ];
				}
			}
			$sobram = cdm_f2_caquinhos_fora_dos_grupos( $grupos );
			$html  .= '<p class="cdm-f2-peca-fora"><strong>' . esc_html( cdm_f2_nome( $id ) )
				. '</strong> — não é falta de declaração e não é o lugar da peça: a '
				. esc_html( $m['fabricante'] ) . ' escreve <em>'
				. esc_html( cdm_f2_lista_humana( $literais ) ) . '</em>, e quem diz que <em>'
				. esc_html( mb_strtolower( $rot['tessela'][ $tessela ], 'UTF-8' ) ) . '</em> entra '
				. 'nessa frase somos nós, não ela. Aqui não dá para trocar o lugar da peça: '
				. ( '' !== $sobram
					? 'o que muda a resposta é o caquinho, e com ' . esc_html( $sobram ) . ' ele voltaria a servir.'
					: 'nenhum caquinho do nosso vocabulário escapa dessa frase.' )
				. '</p>';
		}
	}

	$html .= '</div>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f2_rejuntes_do_banco' ) ) {
/**
 * Os ids de TODO rejunte do banco, contados — nunca digitados.
 *
 * Existe para a prestação de contas da resposta e da tabela poderem fechar
 * contra o banco em vez de contra um número escrito à mão (seção 8 do
 * `ARQUIPELAGO.md`: número de tela nasce contado). Banco que cresce corrige
 * as duas telas sozinho.
 */
function cdm_f2_rejuntes_do_banco() {
	$banco = cdm_f2_banco();
	$ids   = array();
	foreach ( $banco['materiais'] as $id => $m ) {
		if ( 'rejunte' === ( isset( $m['categoria'] ) ? $m['categoria'] : '' ) ) {
			$ids[] = $id;
		}
	}
	sort( $ids );

	return $ids;
}
}

if ( ! function_exists( 'cdm_f2_rejunte_nomes' ) ) {
/** Lista de ids → lista de nomes comerciais, na ordem recebida. */
function cdm_f2_rejunte_nomes( $ids ) {
	$nomes = array();
	foreach ( (array) $ids as $id ) {
		$nomes[] = cdm_f2_nome( $id );
	}

	return $nomes;
}
}

if ( ! function_exists( 'cdm_f2_resposta_rejunte_html' ) ) {
/**
 * A resposta do rejunte — e a PRESTAÇÃO DE CONTAS dela.
 *
 * Consertado em 12/09/2026 (despacho da Sentinela de 12/09, item 2). O defeito:
 * a frase dizia "o rejunte é X", no singular e em definitivo, e o bloco de
 * compra logo abaixo servia QUATRO cartões — os três a mais eram os elegíveis
 * abaixo do topo, que entravam na vitrine sem que uma linha da página dissesse
 * o que eles são. Pior: `mencionados_com_ressalva` não era impresso em lugar
 * nenhum, então havia um quinto estado invisível. Somando, a página falava de
 * 2 a 4 dos 5 rejuntes do banco e o leitor não tinha como saber o que era o
 * resto.
 *
 * A regra que passa a valer, e ela é uma só: **todo rejunte do banco é nomeado
 * exatamente uma vez em cada resposta** — ou na frase de recomendação (e aí ele
 * está na vitrine), ou numa linha de prestação de contas que diz por que ele
 * não está. A vitrine serve EXATAMENTE o que a frase nomeia; não existe produto
 * no bloco de compra que o texto não sustente.
 *
 * Por que os elegíveis abaixo do topo continuam à venda, em vez de saírem: eles
 * passam nas duas travas que importam — cobrem a folga e não estão excluídos do
 * lugar. O que os separa do topo é o fabricante não NOMEAR o lugar, e a régua
 * do rejunte só transforma silêncio em exclusão nos ambientes críticos (regra 2
 * do esquema). Tirá-los da vitrine esconderia do leitor produto que serve;
 * mantê-los sem dizer o que são era a contradição. A saída é a frase dizer.
 */
function cdm_f2_resposta_rejunte_html( $junta, $ambiente, $tessela ) {
	$rot    = cdm_f2_rotulos();
	$celula = cdm_f2_celula_rejunte( $junta, $ambiente );
	$banco  = cdm_f2_banco();
	$na     = $rot['ambiente_curto'][ $ambiente ];

	$html  = '<div class="cdm-f2-secao">';
	$html .= '<h2>E o rejunte, que vai entre os caquinhos</h2>';

	if ( $celula['recomendados_topo'] ) {
		$nomes = cdm_f2_rejunte_nomes( $celula['recomendados_topo'] );
		$html .= '<p class="cdm-f2-frase">Com <strong>' . cdm_casca_num( $junta ) . ' mm</strong> de espaço entre uma pastilha e outra, '
			. esc_html( $na ) . ', o rejunte é <strong>' . esc_html( cdm_f2_lista_humana( $nomes ) ) . '</strong>'
			. ( count( $nomes ) > 1 ? ' — o fabricante nomeia este lugar nos ' . ( 2 === count( $nomes ) ? 'dois' : count( $nomes ) ) . '.' : '.' )
			. '</p>';

		/* OS SEGUNDOS SÃO NOMEADOS NA FRASE, e é por isso que eles podem ficar
		   na vitrine. Enquanto esta linha não existia, o bloco de compra servia
		   três produtos que o texto da página não sustentava. */
		if ( $celula['elegiveis_abaixo_do_topo'] ) {
			$segundos = cdm_f2_rejunte_nomes( $celula['elegiveis_abaixo_do_topo'] );
			$html    .= '<p class="cdm-f2-frase cdm-f2-segunda-linha">Também servem, e por isso estão na lista de compra: <strong>'
				. esc_html( cdm_f2_lista_humana( $segundos ) ) . '</strong>. '
				. ( 1 === count( $segundos ) ? 'Ele cobre' : 'Eles cobrem' ) . ' essa folga e o fabricante não proíbe este lugar — o que ele não faz é '
				. 'nomear o lugar por escrito, e é só isso que separa ' . ( 1 === count( $segundos ) ? 'esse' : 'esses' ) . ' do primeiro.</p>';
		}

		$html .= '<ul class="cdm-f2-vitrine">';
		foreach ( array_merge( $celula['recomendados_topo'], $celula['elegiveis_abaixo_do_topo'] ) as $id ) {
			$p      = cdm_f2_perfil_rejunte( $banco['materiais'][ $id ] );
			$motivo = 'Cobre junta de ' . cdm_casca_num( $p['junta_min'] ) . ' a ' . cdm_casca_num( $p['junta_max'] ) . ' mm.';
			if ( isset( $p['literais'][ $ambiente ] ) ) {
				$motivo .= ' O fabricante declara <em>' . esc_html( cdm_f2_lista_humana( $p['literais'][ $ambiente ] ) ) . '</em>.';
			}
			if ( isset( $p['tesselas_declaradas'][ $tessela ] ) ) {
				$motivo .= ' E nomeia <em>' . esc_html( mb_strtolower( $rot['tessela'][ $tessela ], 'UTF-8' ) ) . '</em> por escrito.';
			}
			$html .= cdm_f2_cartao_html( $id, $motivo, in_array( $id, $celula['recomendados_topo'], true ) ? '' : 'cdm-f2-segundo' );
		}
		$html .= '</ul>';

	} else {
		/* A RECUSA NÃO OFERECE HIPÓTESE — as linhas de prestação de contas logo
		   abaixo nomeiam quem caiu por qual motivo, e é delas que o leitor tira
		   a causa. A versão anterior desta frase enumerava "ou a folga, ou o
		   lugar" tendo as duas listas na mão; a que a substituiu tentou escolher
		   entre três casos (só folga, só lugar, os dois) e o caso "só lugar"
		   nasceu INALCANÇÁVEL, porque o rejunte de faixa desconhecida vive no
		   balde da folga e nunca sai dele. Código que não pode rodar não é
		   cuidado, é um ramo que ninguém vai medir: quem diz a causa são as
		   linhas, uma por motivo. */
		$html .= '<p class="cdm-f2-frase cdm-f2-faixa">Não temos rejunte para indicar com <strong>' . cdm_casca_num( $junta )
			. ' mm</strong> de junta ' . esc_html( $na ) . '. Abaixo, um a um, o motivo de cada produto do nosso banco ter ficado de fora.</p>';
	}

	/* ------------------------------------------------------------------
	 * A PRESTAÇÃO DE CONTAS. Os grupos que NÃO estão na vitrine, cada um com
	 * nome próprio e motivo próprio. Somados aos nomeados na frase, fecham o
	 * banco inteiro — é essa soma que o portão cobra, em toda combinação de
	 * folga × lugar, na resposta e na tabela.
	 *
	 * SÃO QUATRO GRUPOS, e não três: a célula junta num balde só quem tem faixa
	 * publicada e não cobre a folga e quem NÃO TEM FAIXA NENHUMA — para decidir
	 * elegibilidade tanto faz, os dois estão fora. Para o texto não tanto faz:
	 * dizer "fora por causa da folga" de um produto cuja faixa a gente nunca
	 * conseguiu é afirmar sobre uma declaração que não foi lida. A F1 já fazia
	 * esse corte; aqui ele faltava, e era isso que tornava o ramo acima morto.
	 * ------------------------------------------------------------------ */
	$fora_folga = array();
	$sem_faixa  = array();
	foreach ( $celula['eliminados_por_faixa_de_junta'] as $id ) {
		$p = cdm_f2_perfil_rejunte( $banco['materiais'][ $id ] );
		if ( null === $p['junta_min'] || null === $p['junta_max'] ) {
			$sem_faixa[] = $id;
		} else {
			$fora_folga[] = $id;
		}
	}
	if ( $fora_folga ) {
		$linhas = array();
		foreach ( $fora_folga as $id ) {
			$p        = cdm_f2_perfil_rejunte( $banco['materiais'][ $id ] );
			$linhas[] = esc_html( cdm_f2_nome( $id ) ) . ' (o fabricante publica de ' . $p['junta_min'] . ' a ' . $p['junta_max'] . ' mm)';
		}
		$html .= '<p class="cdm-f2-silencio">Fora por causa da folga: ' . implode( '; ', $linhas ) . '.</p>';
	}
	if ( $celula['eliminados_por_ambiente'] ) {
		$html .= '<p class="cdm-f2-silencio">Fora porque o fabricante não declara este lugar: '
			. esc_html( cdm_f2_lista_humana( cdm_f2_rejunte_nomes( $celula['eliminados_por_ambiente'] ) ) ) . '.</p>';
	}
	if ( $celula['mencionados_com_ressalva'] ) {
		/* O QUINTO ESTADO, que não era impresso em lugar nenhum até 12/09/2026.
		   Enquanto o banco tivesse só fonte de nível bom ele ficava vazio, e um
		   grupo vazio não denuncia que a tela não sabe imprimi-lo: no dia em que
		   um rejunte entrasse por fonte fraca, ele sumiria da página inteira —
		   nem na vitrine, nem na prestação de contas. */
		$html .= '<p class="cdm-f2-ressalva">Existe menção a '
			. esc_html( cdm_f2_lista_humana( cdm_f2_rejunte_nomes( $celula['mencionados_com_ressalva'] ) ) )
			. ', mas o que sustenta isso é material de imprensa do fabricante, não documento de produto — por isso ele não entra na indicação nem na lista de compra.</p>';
	}

	if ( $sem_faixa ) {
		$html .= '<p class="cdm-f2-silencio">De ' . esc_html( cdm_f2_lista_humana( cdm_f2_rejunte_nomes( $sem_faixa ) ) )
			. ' a gente não conseguiu a faixa de junta que o fabricante publica, então '
			. ( 1 === count( $sem_faixa ) ? 'ele não entra' : 'eles não entram' ) . ' em recomendação nenhuma — '
			. 'nem para dizer que cabe, nem para dizer que não cabe.</p>';
	}
	$html .= '</div>';

	/* O PREPARO DO REJUNTE SAI EM SEÇÃO IRMÃ, e o motivo é a prestação de contas
	   acima dele. A regra desta ilha, do despacho da Sentinela de 12/09/2026, é
	   que TODO rejunte do banco é nomeado EXATAMENTE UMA VEZ na resposta — ou na
	   frase de recomendação, ou numa linha que diz por que ele não está — e
	   `teste-prestacao-rejunte.php` recomputa essa conta nos 540 estados. A
	   primeira versão deste bloco nasceu DENTRO da seção e nomeou os produtos uma
	   segunda vez: 1.017 erros em 540 estados, de um portão que mede o que a
	   página diz e não o que ela pretende dizer. A instrução de aplicação não é
	   prestação de contas, e agora as duas não moram no mesmo cômodo — a fronteira
	   que a bancada lê é a classe `cdm-f2-secao`, e ela é esta.

	   Nesta metade da página o preparo é mais caro do que na da cola: a junta
	   típica desta ilha é de 2 a 3 mm, e a Quartzolit manda molhar com água limpa
	   toda junta de até 3 mm antes de rejuntar. Era essa a frase que o banco
	   guardava desde 10/09 e que nenhuma tela servia. */
	$recomendados = array_merge( $celula['recomendados_topo'], $celula['elegiveis_abaixo_do_topo'] );
	$preparo      = cdm_f2_preparo_html( $recomendados, 'rejuntar' );
	if ( '' !== $preparo ) {
		$html .= '<div class="cdm-f2-secao cdm-f2-preparo-secao">';
		$html .= $preparo;
		$provas_r = cdm_f2_preparo_provas( $recomendados );
		if ( $provas_r ) {
			$html .= '<div class="cdm-prova"><p>' . implode( '. ', $provas_r ) . '.</p></div>';
		}
		$html .= '</div>';
	}

	return $html;
}
}

if ( ! function_exists( 'cdm_f2_espera_html' ) ) {
/**
 * O tempo de espera — o número que a SERP nunca dá, e que é a diferença entre a
 * peça pronta e a peça que solta o caquinho no dia seguinte.
 */
function cdm_f2_espera_html( $base, $ambiente, $tessela ) {
	$celula = cdm_f2_celula_cola( $base, $ambiente, $tessela );
	$banco  = cdm_f2_banco();
	$linhas = array();

	foreach ( $celula['recomendados_topo'] as $id ) {
		$m    = $banco['materiais'][ $id ];
		$cura = isset( $m['propriedades']['cura_apos_24h'] ) ? $m['propriedades']['cura_apos_24h'] : null;
		$seca = isset( $m['propriedades']['tempo_de_secagem'] ) ? $m['propriedades']['tempo_de_secagem'] : null;
		if ( $cura ) {
			$linhas[] = 'Com ' . esc_html( cdm_f2_nome( $id ) ) . ', a peça descansa <strong>24 horas</strong> antes do rejunte — é o que o fabricante declara para '
				. cdm_casca_num( $cura['valor'] ) . ' mm de cura.';
		} elseif ( $seca && null !== $seca['valor'] ) {
			$linhas[] = 'Com ' . esc_html( cdm_f2_nome( $id ) ) . ', o fabricante declara secagem em <strong>'
				. esc_html( is_array( $seca['valor'] ) ? implode( ' a ', $seca['valor'] ) : $seca['valor'] ) . ' ' . esc_html( $seca['unidade'] ) . '</strong>.';
		} elseif ( $seca ) {
			/* O CAMPO EXISTE E ESTA VAZIO COM MOTIVO ESCRITO — e a pagina diz isso,
			   em vez de simplesmente não ter a seção. Sumir com a linha faria a
			   ferramenta parecer que o tempo de espera não importa para este
			   produto; o que acontece é que a gente não colheu. Silêncio parece
			   defeito, texto honesto não (seção 7 do contrato). */
			$linhas[] = 'Com ' . esc_html( cdm_f2_nome( $id ) ) . ', a gente ainda não publica o tempo de espera: '
				. 'não achamos essa declaração nas fontes do fabricante que lemos.';
		}
	}

	if ( ! $linhas ) {
		return '';
	}

	return '<div class="cdm-f2-secao"><h2>Quanto esperar antes de rejuntar</h2><p>' . implode( ' ', $linhas ) . '</p></div>';
}
}

/* ---------------------------------------------------------------------------
 * 7. As tabelas pré-renderizadas — o que um modelo de linguagem lê
 *
 * São as células escritas À MÃO no esquema e reconferidas pelo validador, não
 * uma amostra bonita: 18 combinações de base × ambiente e 9 de junta ×
 * ambiente, com a frase de justificativa em cada linha. É esta parte que
 * sobrevive a ser citada fora de contexto, e é ela que existe quando ninguém
 * preenche o formulário.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f2_caquinhos_porosos_texto' ) ) {
/**
 * "pastilha de cerâmica, caquinho de azulejo, de louça e pedrinha servem; de
 * vidro e de espelho não" — DERIVADO, nunca digitado.
 *
 * A primeira versão desta resposta trazia as seis palavras escritas à mão, e
 * seria a terceira lista digitada deste mesmo bloco a envelhecer calada: bastaria
 * uma tessela nova no vocabulário para a página ensinar errado com cara de
 * conferido. Aqui ela sai das mesmas duas listas que a régua usa, então a
 * resposta da pessoa e a decisão do código não têm como discordar.
 */
function cdm_f2_caquinhos_porosos_texto() {
	$rot = cdm_f2_rotulos();
	$p   = cdm_f2_porosas();

	$servem = array();
	$nao    = array();
	foreach ( $rot['tessela'] as $id => $rotulo ) {
		$nome = mb_strtolower( $rotulo, 'UTF-8' );
		if ( isset( $p['tesselas'][ $id ] ) ) {
			$servem[] = $nome;
		} else {
			$nao[] = $nome;
		}
	}

	if ( ! $servem ) {
		return 'nenhum dos caquinhos que a gente conhece resolve, e por isso este produto não entra aqui';
	}
	if ( ! $nao ) {
		return 'qualquer um dos caquinhos que a gente conhece resolve';
	}

	return cdm_f2_lista_humana( $servem ) . ' resolvem; '
		. cdm_f2_lista_humana( $nao ) . ' não';
}
}

if ( ! function_exists( 'cdm_f2_caquinhos_porosos_lista' ) ) {
/**
 * Só os caquinhos que resolvem a condição, em lista humana — DERIVADO.
 *
 * A primeira versão desta frase trazia "cerâmica, azulejo, louça ou pedra"
 * escrito à mão, e teria sido a QUARTA lista digitada deste mesmo bloco a
 * envelhecer calada. Uma tessela nova no vocabulário e a página passa a ensinar
 * errado com cara de conferida — e aqui doeria mais do que nas outras três,
 * porque esta é a frase que diz à pessoa o que fazer para a peça não descolar.
 */
function cdm_f2_caquinhos_porosos_lista() {
	$rot = cdm_f2_rotulos();
	$p   = cdm_f2_porosas();

	$servem = array();
	foreach ( $rot['tessela'] as $id => $rotulo ) {
		if ( isset( $p['tesselas'][ $id ] ) ) {
			$servem[] = mb_strtolower( $rotulo, 'UTF-8' );
		}
	}

	return $servem ? cdm_f2_lista_humana( $servem ) : 'nenhum caquinho do nosso vocabulário';
}
}

if ( ! function_exists( 'cdm_f2_cobertura' ) ) {
/**
 * A COBERTURA DA FERRAMENTA, CONTADA UMA VEZ E LIDA POR TRÊS (02/10/2026).
 *
 * A varredura é a entrada INTEIRA — base × lugar × caquinho —, e os números dela
 * sustentam agora TRÊS afirmações que antes não se falavam: a seção "o que a
 * gente ainda não responde" na tela, a promessa do `<title>` e a
 * `<meta name="description">`. Contar a mesma coisa em três lugares seria a
 * família de defeito que esta ilha mais pagou — duas metades contando a mesma
 * coisa sem nunca se falarem.
 *
 * O texto abaixo é o da seção de tela, e ele continua valendo:
 *
 * O que a ilha ainda NÃO responde — DERIVADO do banco, nunca digitado.
 *
 * Esta seção era duas frases escritas à mão, e as duas eram exatas no dia em que
 * nasceram: "não indicamos cola para peça de plástico" e "nem para peça que fica
 * dentro da água o tempo todo". Em 13/09/2026 entraram no banco o Cascola PL500
 * e o Silicone Acético Maxx, e as duas frases passaram a mentir — no ar, em voz
 * de confissão, o que é pior, porque frase de honestidade é a última que alguém
 * desconfia. É a mesma família do número de tela digitado que esta ilha já pagou
 * uma vez: o texto nasce certo e envelhece calado enquanto o dado embaixo dele
 * muda.
 *
 * Então ela passa a ser contada. A varredura é a entrada INTEIRA — base ×
 * lugar × caquinho, as três perguntas que a ferramenta faz —, porque desde a
 * regra 6 o caquinho decide junto, e varrer só base × lugar seria afirmar sobre
 * um escopo maior do que o medido.
 */
function cdm_f2_cobertura() {
	static $conta = null;
	if ( null !== $conta ) {
		return $conta;
	}

	$rot   = cdm_f2_rotulos();
	$bases = array_keys( $rot['base_curto'] );
	$ambs  = array_keys( $rot['ambiente_curto'] );
	$tess  = array_keys( $rot['tessela'] );

	$total       = 0;
	$descobertos = 0;
	$vazio_base  = array();   // base => quantos casos dela saem sem indicação
	$vazio_amb   = array();
	foreach ( $bases as $b ) {
		$vazio_base[ $b ] = 0;
		foreach ( $ambs as $a ) {
			if ( ! isset( $vazio_amb[ $a ] ) ) {
				$vazio_amb[ $a ] = 0;
			}
			foreach ( $tess as $t ) {
				$total++;
				$c = cdm_f2_celula_cola( $b, $a, $t );
				if ( ! $c['recomendados_topo'] && ! $c['elegiveis_abaixo_do_topo'] ) {
					$descobertos++;
					$vazio_base[ $b ]++;
					$vazio_amb[ $a ]++;
				}
			}
		}
	}

	$conta = array(
		'total'       => $total,
		'descobertos' => $descobertos,
		'respondidos' => $total - $descobertos,
		'vazio_base'  => $vazio_base,
		'vazio_amb'   => $vazio_amb,
		'por_base'    => count( $ambs ) * count( $tess ),
		'por_amb'     => count( $bases ) * count( $tess ),
		'bases'       => count( $bases ),
		'ambientes'   => count( $ambs ),
		'tesselas'    => count( $tess ),
		'colas'       => cdm_f2_quantas_colas(),
	);

	return $conta;
}
}

if ( ! function_exists( 'cdm_f2_quantas_colas' ) ) {
/**
 * QUANTAS COLAS O BANCO TEM — varrido do banco, nunca digitado.
 *
 * A categoria é lida de cada registro, e não o tamanho da lista inteira: o
 * mesmo banco traz os rejuntes, e a frase "10 dos 5 itens" que esta ilha já
 * serviu no ar em 12/09/2026 nasceu exatamente de contar um denominador que
 * não era o da afirmação.
 */
function cdm_f2_quantas_colas() {
	$n = 0;
	foreach ( cdm_f2_banco()['materiais'] as $m ) {
		if ( 'cola' === ( isset( $m['categoria'] ) ? $m['categoria'] : '' ) ) {
			$n++;
		}
	}

	return $n;
}
}

if ( ! function_exists( 'cdm_f2_faixas_descobertas_html' ) ) {
function cdm_f2_faixas_descobertas_html() {
	$rot   = cdm_f2_rotulos();
	$conta = cdm_f2_cobertura();

	$total       = $conta['total'];
	$descobertos = $conta['descobertos'];
	$vazio_base  = $conta['vazio_base'];
	$vazio_amb   = $conta['vazio_amb'];
	$por_base    = $conta['por_base'];
	$por_amb     = $conta['por_amb'];

	$html  = '<div class="cdm-f2-secao">';
	$html .= '<h2>O que a gente ainda não responde</h2>';

	if ( 0 === $descobertos ) {
		$html .= '<p>Hoje toda combinação desta página sai com pelo menos uma cola indicada pelo próprio fabricante. Quando deixar de ser assim, esta seção volta a listar o que falta — ela é contada do nosso banco, não escrita à mão.</p>';
		$html .= '</div>';

		return $html;
	}

	$html .= '<p>Esta página responde <strong>' . cdm_casca_num( $total ) . '</strong> combinações de base, lugar e caquinho. '
		. 'Em <strong>' . cdm_casca_num( $descobertos ) . '</strong> delas a gente ainda não tem cola para indicar, '
		. 'e prefere dizer isso a chutar o de sempre. Esta contagem sai do nosso banco a cada vez que a página é servida.</p>';

	/* Base que sai vazia em TODOS os casos dela tem nome próprio: é a faixa que
	   falta inteira, e não um canto dela. */
	$inteiras = array();
	foreach ( $vazio_base as $b => $n ) {
		if ( $n === $por_base ) {
			$inteiras[] = $rot['base_curto'][ $b ];
		}
	}
	if ( $inteiras ) {
		$html .= '<p class="cdm-f2-faixa">Não indicamos cola nenhuma, em lugar nenhum, para: <strong>'
			. esc_html( cdm_f2_lista_humana( $inteiras ) ) . '</strong>.</p>';
	}

	$ambs_inteiros = array();
	foreach ( $vazio_amb as $a => $n ) {
		if ( $n === $por_amb ) {
			$ambs_inteiros[] = mb_strtolower( $rot['ambiente_curto'][ $a ], 'UTF-8' );
		}
	}
	if ( $ambs_inteiros ) {
		$html .= '<p class="cdm-f2-faixa">E não indicamos cola nenhuma, sobre base nenhuma, para peça que fica <strong>'
			. esc_html( cdm_f2_lista_humana( $ambs_inteiros ) ) . '</strong>.</p>';
	}

	/* Os cantos: base que responde em parte. É aqui que mora a diferença entre
	   "a gente não sabe" e "a gente sabe num caso e não no outro" — e dizer as
	   duas com a mesma frase seria afirmar num escopo maior do que o medido. */
	$parciais = array();
	foreach ( $vazio_base as $b => $n ) {
		if ( $n > 0 && $n < $por_base ) {
			$parciais[] = $rot['base_curto'][ $b ] . ' (' . $n . ' de ' . $por_base . ')';
		}
	}
	if ( $parciais ) {
		$html .= '<p class="cdm-f2-faixa">Estas bases a gente responde em parte, e o buraco é o resto: <strong>'
			. esc_html( cdm_f2_lista_humana( $parciais ) ) . '</strong>. O que decide, caso a caso, é o lugar onde a peça vai ficar e o caquinho que você vai colar — troque os dois no formulário lá em cima e a resposta muda.</p>';
	}

	$html .= '<p>Ter metade da resposta não é ter a resposta, e a peça precisa das duas.</p>';
	$html .= '</div>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f2_tabela_cola_html' ) ) {
function cdm_f2_tabela_cola_html() {
	$banco  = cdm_f2_banco();
	$rot    = cdm_f2_rotulos();
	$grade  = isset( $banco['esquema']['matriz_esperada_da_F2']['celulas'] ) ? $banco['esquema']['matriz_esperada_da_F2']['celulas'] : array();

	if ( ! $grade ) {
		return '';
	}

	$html  = '<div class="cdm-f2-secao"><h2>A tabela inteira, sem preencher nada</h2>';
	$html .= '<p>Cada linha é uma combinação que a gente já conferiu: a base, o lugar onde a peça vai ficar, a cola que serve, a que não serve, e a condição que o fabricante põe quando ele põe alguma.</p>';
	$html .= '<div class="cdm-f2-rolagem"><table class="cdm-f2-tabela"><thead><tr>'
		. '<th scope="col">Sobre o que você vai colar</th><th scope="col">Onde a peça vai ficar</th>'
		. '<th scope="col">Use</th><th scope="col">Não use, e por quê</th>'
		. '<th scope="col">Com que condição</th></tr></thead><tbody>';

	foreach ( $grade as $c ) {
		if ( ! isset( $rot['base_curto'][ $c['base'] ] ) || ! isset( $rot['ambiente_curto'][ $c['ambiente'] ] ) ) {
			continue;
		}
		/* A célula sai RECOMPUTADA das declarações, nunca lida do campo escrito à
		   mão que está ao lado dela no esquema. Se o banco e a matriz se
		   separarem, quem acusa é o validador — a tela nunca finge concordância
		   copiando o esperado. */
		$celula = cdm_f2_celula_cola( $c['base'], $c['ambiente'] );

		$usa = array();
		foreach ( $celula['recomendados_topo'] as $id ) {
			$usa[] = cdm_f2_nome( $id );
		}
		$nao = array();
		foreach ( $celula['eliminados_por_proibicao'] as $id ) {
			$m      = $banco['materiais'][ $id ];
			$p      = cdm_f2_perfil_cola( $m );
			$termos = array();
			foreach ( array( $c['base'], $c['ambiente'] ) as $alvo ) {
				if ( isset( $p['literais_proibicao'][ $alvo ] ) ) {
					$termos = array_merge( $termos, $p['literais_proibicao'][ $alvo ] );
				}
			}
			$nao[] = cdm_f2_nome( $id ) . ' — a ' . $m['fabricante'] . ' escreve ' . cdm_f2_lista_humana( $termos );
		}

		/* A COLUNA DA CONDIÇÃO, e ela existe por aritmética, não por capricho.
		   Esta tabela é a camada de DECLARAÇÃO: ela não tem o caquinho, porque
		   cruzá-lo aqui daria 108 linhas numa página cuja tabela existe para ser
		   lida inteira por um modelo de linguagem. Sem esta coluna, a linha
		   "plástico, dentro de casa: use Cascola PL500" seria servida no HTML
		   como se valesse sempre — e ela só vale com caquinho poroso. É a
		   afirmação em bloco com escopo maior do que o medido, que a seção 7 do
		   contrato nomeia, e a tabela pré-renderizada é onde ela custa mais
		   caro, porque é a metade que se lê sem preencher formulário. */
		$cond = array();
		foreach ( $celula['recomendados_topo'] as $id ) {
			$m = $banco['materiais'][ $id ];
			if ( cdm_f2_exige_porosa( $m ) ) {
				$cond[] = cdm_f2_nome( $id ) . ': ' . $m['condicoes']['exige_superficie_porosa']['literal'];
			}
			/* A MESMA ARITMÉTICA DA COLUNA, agora para a regra 7 — e aqui ela
			   morde de verdade: esta tabela é a camada de DECLARAÇÃO e não tem o
			   caquinho, então a linha "cerâmica, no sol e na chuva: use Tekbond
			   Silicone Acético Construção" era servida no HTML como se valesse
			   sempre, e ela não vale com caco de espelho. É a metade da página
			   que se lê sem preencher formulário, e é onde a afirmação sem
			   escopo custa mais caro. */
			$grupos_do_m = cdm_f2_proibe_grupos_de_peca( $m );
			if ( $grupos_do_m ) {
				$mapa_g   = cdm_f2_grupos_de_peca();
				$caquinhos = array();
				foreach ( $grupos_do_m as $g ) {
					foreach ( array_keys( isset( $mapa_g['grupos'][ $g ]['tesselas'] ) ? $mapa_g['grupos'][ $g ]['tesselas'] : array() ) as $tq ) {
						if ( isset( $rot['tessela'][ $tq ] ) ) {
							$caquinhos[ $tq ] = mb_strtolower( $rot['tessela'][ $tq ], 'UTF-8' );
						}
					}
				}
				$lits = array();
				foreach ( $grupos_do_m as $g ) {
					if ( isset( $m['condicoes']['proibe_grupos_de_tessela']['literais'][ $g ] ) ) {
						$lits[] = $m['condicoes']['proibe_grupos_de_tessela']['literais'][ $g ];
					}
				}
				if ( $caquinhos ) {
					$cond[] = cdm_f2_nome( $id ) . ': não com ' . cdm_f2_lista_humana( array_values( $caquinhos ) )
						. ' — o fabricante escreve "' . cdm_f2_lista_humana( $lits )
						. '", e a classificação do caquinho é nossa';
				}
			}
		}

		$html .= '<tr>';
		$html .= '<td>' . esc_html( $rot['base_curto'][ $c['base'] ] ) . '</td>';
		$html .= '<td>' . esc_html( $rot['ambiente_curto'][ $c['ambiente'] ] ) . '</td>';
		$html .= '<td>' . ( $usa ? esc_html( cdm_f2_lista_humana( $usa ) ) : '<span class="cdm-f2-vazio">a gente não indica nenhuma</span>' ) . '</td>';
		$html .= '<td>' . ( $nao ? esc_html( cdm_f2_lista_humana( $nao ) ) : '—' ) . '</td>';
		$html .= '<td>' . ( $cond ? esc_html( implode( '; ', $cond ) ) : '—' ) . '</td>';
		$html .= '</tr>';
	}

	$html .= '</tbody></table></div></div>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f2_tabela_rejunte_html' ) ) {
function cdm_f2_tabela_rejunte_html() {
	$banco = cdm_f2_banco();
	$rot   = cdm_f2_rotulos();
	$grade = isset( $banco['esquema']['matriz_esperada_do_rejunte']['celulas'] ) ? $banco['esquema']['matriz_esperada_do_rejunte']['celulas'] : array();

	if ( ! $grade ) {
		return '';
	}

	$html  = '<div class="cdm-f2-secao"><h2>O mesmo, para o rejunte</h2>';
	$html .= '<p>Aqui quem manda é a folga que você deixa entre uma pastilha e outra. A faixa de cada produto é a que o fabricante publica.</p>';
	$html .= '<div class="cdm-f2-rolagem"><table class="cdm-f2-tabela"><thead><tr>'
		. '<th scope="col">Folga entre as pastilhas</th><th scope="col">Onde a peça vai ficar</th>'
		. '<th scope="col">Rejunte que serve</th><th scope="col">Fora, e por quê</th></tr></thead><tbody>';

	foreach ( $grade as $c ) {
		if ( ! isset( $rot['ambiente_curto'][ $c['ambiente'] ] ) ) {
			continue;
		}
		$celula = cdm_f2_celula_rejunte( (int) $c['junta_mm'], $c['ambiente'] );

		/* A MESMA PRESTAÇÃO DE CONTAS DA RESPOSTA, na tabela — e pelo mesmo
		   motivo, que aqui é mais caro ainda: esta é a metade que um modelo de
		   linguagem lê sem preencher formulário nenhum. Até 12/09/2026 a coluna
		   "serve" trazia só o topo e a coluna "fora" só dois dos três grupos, e
		   três das nove linhas não somavam os 5 rejuntes do banco. */
		$usa = array();
		if ( $celula['recomendados_topo'] ) {
			$usa[] = cdm_f2_lista_humana( cdm_f2_rejunte_nomes( $celula['recomendados_topo'] ) )
				. ' (o fabricante nomeia este lugar)';
		}
		if ( $celula['elegiveis_abaixo_do_topo'] ) {
			$usa[] = cdm_f2_lista_humana( cdm_f2_rejunte_nomes( $celula['elegiveis_abaixo_do_topo'] ) )
				. ( 1 === count( $celula['elegiveis_abaixo_do_topo'] ) ? ' (cobre' : ' (cobrem' )
				. ' a folga, e o fabricante não fala deste lugar)';
		}

		$t_folga = array();
		$t_sem   = array();
		foreach ( $celula['eliminados_por_faixa_de_junta'] as $id ) {
			$p = cdm_f2_perfil_rejunte( $banco['materiais'][ $id ] );
			if ( null === $p['junta_min'] || null === $p['junta_max'] ) {
				$t_sem[] = $id;
			} else {
				$t_folga[] = $id;
			}
		}
		$fora = array();
		if ( $t_folga ) {
			$fora[] = count( $t_folga ) . ' por causa da folga';
		}
		if ( $celula['eliminados_por_ambiente'] ) {
			$fora[] = count( $celula['eliminados_por_ambiente'] ) . ' porque o fabricante não declara este lugar';
		}
		if ( $celula['mencionados_com_ressalva'] ) {
			$fora[] = count( $celula['mencionados_com_ressalva'] ) . ' porque a fonte é material de imprensa';
		}
		if ( $t_sem ) {
			$fora[] = count( $t_sem ) . ' porque a faixa de folga dele não foi obtida';
		}

		$html .= '<tr>';
		$html .= '<td>' . cdm_casca_num( $c['junta_mm'] ) . ' mm</td>';
		$html .= '<td>' . esc_html( $rot['ambiente_curto'][ $c['ambiente'] ] ) . '</td>';
		$html .= '<td>' . ( $usa ? esc_html( implode( '; ', $usa ) ) : '<span class="cdm-f2-vazio">a gente não indica nenhum</span>' ) . '</td>';
		$html .= '<td>' . ( $fora ? esc_html( cdm_f2_lista_humana( $fora ) ) : '—' ) . '</td>';
		$html .= '</tr>';
	}

	$html .= '</tbody></table></div></div>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 8. O formulário
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f2_select_html' ) ) {
function cdm_f2_select_html( $nome, $rotulo, $opcoes, $escolhido, $ajuda = '' ) {
	$id    = 'cdm-f2-' . $nome;
	$html  = '<p class="cdm-f2-campo"><label for="' . esc_attr( $id ) . '">' . esc_html( $rotulo ) . '</label>';
	if ( '' !== $ajuda ) {
		$html .= '<span class="cdm-f2-ajuda">' . esc_html( $ajuda ) . '</span>';
	}
	$html .= '<select id="' . esc_attr( $id ) . '" name="' . esc_attr( $nome ) . '">';
	foreach ( $opcoes as $valor => $texto ) {
		$html .= '<option value="' . esc_attr( $valor ) . '"' . ( (string) $valor === (string) $escolhido ? ' selected' : '' )
			. '>' . esc_html( $texto ) . '</option>';
	}
	$html .= '</select></p>';

	return $html;
}
}

if ( ! function_exists( 'cdm_f2_form_html' ) ) {
function cdm_f2_form_html( $entrada ) {
	$rot = cdm_f2_rotulos();

	$juntas = array();
	for ( $i = 1; $i <= 12; $i++ ) {
		$juntas[ $i ] = $i . ' mm' . ( 2 === $i ? ' (o mais comum)' : '' );
	}

	/* GET para a própria página, e sem $_SERVER literal: o playbook (fase 4b)
	   manda usar add_query_arg( array() ), porque o ModSecurity desta hospedagem
	   mata a gravação em silêncio quando o snippet toca $_SERVER. */
	$html  = '<form class="cdm-f2-form" method="get" action="' . esc_url( add_query_arg( array() ) ) . '#resposta">';
	$html .= cdm_f2_select_html( 'base', 'Sobre o que você vai colar?', $rot['base'], $entrada['base'] );
	$html .= cdm_f2_select_html( 'onde', 'Onde a peça vai ficar?', $rot['ambiente'], $entrada['ambiente'] );
	$html .= cdm_f2_select_html( 'caco', 'O que você vai colar em cima?', $rot['tessela'], $entrada['tessela'],
		'Isto não muda a cola — quem manda na cola é a base. Serve para a gente avisar quando o fabricante do rejunte cita o seu caquinho por escrito.' );
	$html .= cdm_f2_select_html( 'junta', 'Quanto espaço entre uma pastilha e outra?', $juntas, $entrada['junta'],
		'Entre 2 e 3 mm é o comum, mas quem decide é a sua peça.' );
	$html .= '<p class="cdm-f2-acao"><button type="submit" class="cdm-f2-botao">Ver o que usar</button></p>';
	$html .= '</form>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 9. A página
 * ------------------------------------------------------------------------- */

add_shortcode( 'cdm_f2', function () {
	$banco = cdm_f2_banco();

	if ( empty( $banco['completo'] ) ) {
		/* Sem banco a página NÃO inventa: diz que a medição não chegou. Uma
		   ferramenta que responde com o banco vazio é pior que uma fora do ar. */
		return '<div class="cdm-bloco"><p class="cdm-linha-mestra">Esta ferramenta está sem os dados de fabricante neste momento.</p>'
			. '<p>Ela não responde de cabeça: cada recomendação sai do que o fabricante publica sobre o próprio produto. Volte em alguns minutos.</p></div>';
	}

	$e   = cdm_f2_entrada();
	$rot = cdm_f2_rotulos();
	$n   = cdm_casca_numeros();

	$html  = '<div class="cdm-bloco cdm-f2">';
	$html .= '<div class="cdm-abertura">';
	$html .= '<p class="cdm-linha-mestra">Diga sobre o que você vai colar e onde a peça vai ficar. A gente mostra a cola, o rejunte, quanto esperar — e o que <em>não</em> usar no seu caso.</p>';
	$html .= '<p>A resposta muda mais do que parece: a mesma peça feita para a sala e para o jardim leva material diferente, e a cola que a maioria dos tutoriais manda usar é justamente a que o fabricante proíbe em espelho, em cimento e em vidro laminado.</p>';
	$html .= '<p>Esta página faz parte do nosso guia de ' . cdm_casca_link_html( 'materiais', 'Materiais' ) . '.</p>';
	$html .= '</div>';

	$html .= cdm_f2_form_html( $e );

	$html .= '<div class="cdm-f2-saida" id="resposta">';
	$html .= cdm_f2_resposta_cola_html( $e['base'], $e['ambiente'], $e['tessela'] );
	$html .= cdm_f2_vitrine_html( $e['base'], $e['ambiente'], $e['tessela'] );
	$html .= cdm_f2_espera_html( $e['base'], $e['ambiente'], $e['tessela'] );
	$html .= cdm_f2_resposta_rejunte_html( $e['junta'], $e['ambiente'], $e['tessela'] );
	$html .= cdm_f2_fora_html( $e['base'], $e['ambiente'], $e['tessela'] );
	$html .= '</div>';

	$html .= cdm_f2_tabela_cola_html();
	$html .= cdm_f2_tabela_rejunte_html();

	$html .= cdm_f2_faixas_descobertas_html();

	/* PERGUNTAS QUE AS PESSOAS REALMENTE FAZEM — as mesmas do FAQPage abaixo. O
	   texto na tela e o do schema saem da MESMA função, senão os dois envelhecem
	   separados e o schema passa a prometer o que a página não diz. */
	$html .= '<div class="cdm-f2-secao"><h2>Perguntas que sempre chegam</h2><dl class="cdm-f2-faq">';
	foreach ( cdm_f2_perguntas() as $p ) {
		$html .= '<dt>' . esc_html( $p['pergunta'] ) . '</dt><dd>' . esc_html( $p['resposta'] ) . '</dd>';
	}
	$html .= '</dl></div>';

	/* A CAMADA DE PROVA da página (15.2): quem declarou, em qual documento, em
	   que dia a gente leu, e o que ainda não foi lido direto. */
	$html .= '<div class="cdm-prova">';
	$html .= '<h2>Como sabemos</h2>';
	$html .= '<p>As ' . cdm_casca_num( $n['materiais_cola'] ) . ' colas e os ' . cdm_casca_num( $n['materiais_rejunte'] )
		. ' rejuntes desta página vêm do que cada fabricante publica sobre o próprio produto, com o documento e a data em que foi lido. A recomendação é <em>recalculada</em> das declarações a cada carregamento, nunca digitada — são '
		. cdm_casca_num( $n['celulas_matriz'] ) . ' combinações de base e ambiente e ' . cdm_casca_num( $n['celulas_rejunte'] )
		. ' de folga e ambiente conferidas uma a uma.</p>';
	/* A SEGUNDA METADE DESTE PARAGRAFO ERA UM DISCLOSURE VELHO, E ELE MENTIA.
	   Ela dizia "Nenhum PDF de fabricante foi aberto linha a linha: a leitura foi
	   feita no dominio de cada um, em 10 e 11/09/2026". Era verdade quando foi
	   escrita, em 11/09/2026. Em 05 e 06/10/2026 DOIS boletins tecnicos foram
	   abertos e lidos pagina a pagina pelo canal de espelho — e e de um deles que
	   sai a instrucao de preparo do rejunte piscinas que esta pagina agora serve.
	   A frase envelheceu calada, na unica camada da pagina cujo produto inteiro e
	   o rigor; e a mesma cicatriz que a casca 1.18.0 pagou com os 28 botoes de
	   afiliado declarados como nao-afiliado.

	   Entao a conta passa a ser CONTADA e a sair so pela via viva (`numeros_vivos`),
	   como a da divulgacao: com o instantaneo, a pagina diz onde a leitura foi
	   feita e nao afirma quantidade nenhuma. Numero de tela nasce contado. */
	$html .= '<p>A mais importante delas é a ficha técnica BRSA004 do Silicone Acético Construção Tekbond, revisada em 10/2025, que lista espelho, concreto, cimento, tijolo, calcário, superfície alcalina, pintada ou porosa, acrílico, aquário, metal corrosível e imersão contínua entre as superfícies em que o produto não deve ser usado. '
		. ( ! empty( $n['numeros_vivos'] )
			? 'Dos ' . cdm_casca_num( $n['documentos_no_banco'] ) . ' documentos que o banco cita, '
				. ( (int) $n['documentos_abertos'] > 0
					? cdm_casca_num( $n['documentos_abertos'] ) . ' '
						. ( 1 === (int) $n['documentos_abertos'] ? 'foi aberto' : 'foram abertos' )
						. ' e ' . ( 1 === (int) $n['documentos_abertos'] ? 'lido' : 'lidos' ) . ' página a página'
					: 'nenhum foi aberto página a página' )
				. '; o resto foi lido no domínio de cada fabricante, e isso está declarado item a item no nosso banco.'
			: 'A leitura foi feita no domínio de cada fabricante, e quais documentos foram abertos página a página está declarado item a item no nosso banco.' )
		. '</p>';
	$html .= '<p>Hoje ' . cdm_casca_num( $n['esperando_link'] ) . ' dos ' . cdm_casca_num( $n['itens_no_banco'] )
		. ' itens do banco ainda esperam link de loja. O método inteiro está em ' . cdm_casca_link_html( 'materiais/como-sabemos', 'Como sabemos' ) . '.</p>';
	$html .= '</div>';

	$html .= '</div>';

	return $html;
} );

if ( ! function_exists( 'cdm_f2_perguntas' ) ) {
/**
 * Uma fonte só para a tela e para o FAQPage. Toda resposta aqui é sustentada
 * por declaração que já está no banco — nenhuma pergunta existe só para encher
 * schema, que é o que faz FAQPage virar spam.
 */
function cdm_f2_perguntas() {
	return array(
		array(
			'pergunta' => 'Posso usar silicone acético para colar caquinho de espelho?',
			'resposta' => 'Não. A Tekbond escreve espelhos na lista do que o Silicone Acético Construção não deve tocar. O Silicone Neutro, do mesmo fabricante, é declarado para espelho — não precisa trocar de marca, precisa pegar o tubo certo na prateleira.',
		),
		array(
			'pergunta' => 'E no vaso de cimento, serve silicone acético?',
			'resposta' => 'Não. Concreto, cimento e superfícies alcalinas estão na lista do que a Tekbond diz para não usar com o acético. Quem responde ao vaso de cimento é o silicone neutro, que declara concreto e alvenaria.',
		),
		array(
			'pergunta' => 'Cola branca serve para mosaico?',
			'resposta' => 'Serve em MDF e madeira, dentro de casa e em lugar seco: a Cascola declara MDF, compensado e madeira para o Cascorez Extra, e delimita o uso a ambientes internos. Em área molhada ou fora de casa ela não declara nada, e a gente não transforma silêncio em indicação.',
		),
		array(
			'pergunta' => 'Quanto tempo esperar antes de rejuntar?',
			'resposta' => 'Com silicone acético, 24 horas: é o tempo em que o fabricante declara 3 mm de cura, a 23 graus e 55% de umidade. Rejuntar antes disso é mexer na peça enquanto a cola ainda está trabalhando.',
		),
		/* A PERGUNTA QUE A ILHA PASSOU A SABER RESPONDER EM 13/09/2026, e ela é a
		   cara da regra 6: a resposta depende das DUAS superfícies, e a página
		   diz qual das duas resolve. Vaso de plástico é peça comum de mosaico
		   (a busca existe no corpus do bloco 1) e até hoje a ilha não tinha o
		   que responder. */
		array(
			'pergunta' => 'Dá para colar mosaico em vaso de plástico?',
			'resposta' => 'Dá, com uma condição, e ela não é nossa: a Cascola declara plásticos entre os materiais em que o Adesivo de Montagem PL500 adere, e diz que ao menos uma das superfícies tem de ser porosa, porque o produto seca por evaporação da água. O plástico não é poroso — então quem resolve é o caquinho: '
				. cdm_f2_caquinhos_porosos_texto() . '. Quem classificou essas superfícies fomos nós, não o fabricante. E vale só dentro de casa, em lugar seco: o produto é declarado para uso interno.',
		),
		array(
			'pergunta' => 'Qual rejunte para peça que fica no sol e na chuva?',
			'resposta' => 'A gente não tem resposta para esse caso, e prefere dizer isso: nenhum dos cinco rejuntes do nosso banco declara resistência a sol e chuva pelo nome. Peça de jardim, número de casa e mandala de parede externa ficam nessa faixa descoberta.',
		),
	);
}
}

/* ---------------------------------------------------------------------------
 * 10. Cabeça da página: description, canonical, robôs e JSON-LD
 *
 * O canonical e o `noindex` do estado com parâmetro andam juntos e existem pela
 * mesma razão: a resposta é servida pelo servidor, então cada combinação é uma
 * URL de verdade — e quem entra no índice tem que ser UMA página, a âncora, com
 * a tabela inteira (seções 14.1 e 14.4 do contrato).
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_f2_e_minha_pagina' ) ) {
function cdm_f2_e_minha_pagina() {
	return function_exists( 'cdm_casca_slug_atual' ) && CDM_F2_SLUG === cdm_casca_slug_atual();
}
}

/* O CANONICAL NAO SAI DAQUI, e a ausencia e deliberada: `rel_canonical()` do
   nucleo ja imprime o permalink limpo em toda pagina singular, e esta ilha nao
   tem plugin de SEO que o remova. Imprimir o nosso serviria DOIS canonicals
   identicos — inofensivo para o Google e sujo numa pagina cujo proposito inteiro
   e ter UM endereco no indice.

   E A `description` DESTA PAGINA E DECLARADA, NAO IMPRESSA (28/09/2026), pelo
   mesmo argumento uma linha acima: ate aqui este arquivo dava `echo` na propria
   num `wp_head` paralelo, que e o desenho que fez a etiqueta de ROBO sair
   dobrada e que a casca 1.13.0 consertou em 25/09. Agora quem imprime e a
   casca, uma vez.
      O TEXTO MUDOU EM 02/10/2026, e esta e a pagina que pediu o bloco: 7,8 de
   posicao, 17 impressoes, CTR ZERO — a melhor linha do Arquipelago inteiro. O
   BLOCO A do despacho do Raphael de 24/09 mandava esperar a janela de 30/09, e
   ela fechou. A frase antiga tinha 183 caracteres (fora da faixa de 120 a 160
   do item 4 do despacho de 28/09), dizia a procedencia e NAO dizia numero
   nenhum; a Proposta 1 de 23/09 pede, com estas palavras, "um numero que a
   propria pagina calcula, com a fonte".
      E O NUMERO NAO E DIGITADO: ele sai de `cdm_f2_cobertura()`, a mesma
   varredura que escreve a secao "o que a gente ainda nao responde" na tela.
   Entao a promessa do resultado da busca e a confissao do fim da pagina nao tem
   como discordar — e no dia em que o banco mudar, as duas mudam juntas. */
add_filter( 'cdm_descricao', function ( $d ) {
	if ( ! cdm_f2_e_minha_pagina() ) {
		return $d;
	}

	$c = cdm_f2_cobertura();

	$com_numero = cdm_casca_preencher_promessa(
		'Qual cola e qual rejunte pela declaração do fabricante: {colas} colas em {casos} casos de base, lugar e caquinho, e os {sem} que a gente ainda não responde.',
		array( 'colas' => $c['colas'], 'casos' => $c['total'], 'sem' => $c['descobertos'] )
	);

	/* A FRASE SEM NUMERO E A SAIDA DO BANCO QUE NAO CHEGOU, e ela tambem cabe na
	   faixa de 120 a 160: servir o molde cru, ou uma frase de 40 caracteres,
	   seria trocar um defeito por outro no lugar onde o clique se decide. */
	return '' !== $com_numero
		? $com_numero
		: 'Qual cola e qual rejunte usar no mosaico, pela declaração do próprio fabricante: cerâmica, vidro, espelho, MDF, cimento, metal ou madeira.';
} );

/* A PROMESSA DO `<title>`, declarada e nao impressa — quem monta o titulo e a
   casca 1.19.0, uma vez, pelo mesmo contrato que a `description` tem desde
   28/09 e a etiqueta de robo desde 25/09.
      OS DOIS NUMEROS SAO CONTADOS: as colas, do banco; as bases, do vocabulario
   que a propria ferramenta oferece no formulario. Com nome de 41 caracteres e
   separador de 3, o titulo fica em 64 — abaixo do teto de 65 — e a marca sai do
   fim. Se o banco crescer e a frase estourar o teto, a casca devolve a marca e
   a promessa desaparece sozinha: e a trava 1, e e de proposito. */
add_filter( 'cdm_promessa', function ( $p, $slug ) {
	if ( CDM_F2_SLUG !== $slug ) {
		return $p;
	}

	$c = cdm_f2_cobertura();

	return cdm_casca_preencher_promessa(
		'{colas} colas para {bases} bases',
		array( 'colas' => $c['colas'], 'bases' => $c['bases'] )
	);
}, 10, 2 );

/* O ESTADO COM PARAMETRO SAI DO INDICE, e quem IMPRIME a etiqueta e a casca.
   O paragrafo acima explica por que o canonical NAO sai daqui — "serviria DOIS
   canonicals (...) sujo numa pagina cujo proposito inteiro e ter UM endereco no
   indice" — e ate 25/09/2026 este arquivo fazia exatamente isso com a etiqueta
   de robo, tres linhas abaixo. Medido no ar naquele dia. Agora a condicao e
   declarada e a casca junta tudo num vetor so (casca 1.13.0). */
if ( ! function_exists( 'cdm_f2_parametros' ) ) {
/** OS NOMES DE PARAMETRO QUE SAO DESTA FERRAMENTA. Os mesmos quatro que
    `cdm_f2_entrada()` le, numa lista so — para a pergunta do `noindex` e a do
    formulario nao envelhecerem separadas. */
function cdm_f2_parametros() {
	return array( 'base', 'onde', 'caco', 'junta' );
}
}

if ( ! function_exists( 'cdm_f2_tem_parametro' ) ) {
/**
 * ESTA URL E UM ESTADO COM PARAMETRO? — a pergunta do `noindex`, e ela NAO e a
 * pergunta do `escolheu` (28/09/2026).
 *
 * ESTA PAGINA E A QUE FOI MEDIDA. A ronda da Sentinela de 28/09/2026 abriu as
 * tres no ar e as tres serviam UMA etiqueta de robo SEM `noindex`:
 *
 *     ?base=ceramica&onde=externo
 *     ?base=mdf
 *     ?base=ceramica&caco=louca&junta=fina&onde=interno
 *
 * Os nomes dos quatro parametros sao reais; NENHUM dos valores existe no
 * vocabulario desta ferramenta — as chaves sao `ceramica_esmaltada_porcelana`,
 * `externo_exposto`, `mdf_madeira`, `caco_louca`, e `junta` e numero. Entao o
 * `escolheu` daqui, que pergunta se o valor esta no vocabulario, respondia
 * "nao escolheu nada" e a pagina entrava no indice com tres enderecos a mais.
 *
 * A reconferencia do conserto de 25/09 FALHOU nesta metade por isso, e o
 * criterio que falhou foi escrito pelo proprio conserto: "os estados com
 * parametro da F1 e da F2 servem UMA etiqueta com `noindex, follow`".
 *
 * O ATENUANTE, medido junto e escrito aqui para ninguem tratar isto como
 * incendio: as tres servem `rel="canonical"` para o endereco limpo, e o HTML
 * servido com parametro e byte a byte igual ao sem parametro — esta ferramenta
 * resolve no cliente. O risco era orcamento de rastreamento e duplicata, nunca
 * pagina errada no indice.
 *
 * A SEPARACAO DAS DUAS PERGUNTAS esta escrita por extenso em
 * `cdm_f1_tem_parametro()`, no snippet irmao, e vale igual aqui: `escolheu`
 * manda na TELA e continua medindo o VALOR — valor fora do vocabulario volta ao
 * padrao e a pagina que sai e a ancora, e dizer "voce escolheu" sobre uma
 * escolha nao honrada seria mentir na tela. Esta funcao manda no `noindex` e
 * mede a PRESENCA, porque duplicata se conta por endereco e o conjunto dos
 * valores invalidos e infinito.
 */
function cdm_f2_tem_parametro( $query = null ) {
	$query = is_array( $query ) ? $query : ( isset( $_GET ) ? (array) $_GET : array() );
	foreach ( cdm_f2_parametros() as $nome ) {
		if ( array_key_exists( $nome, $query ) ) {
			return true;
		}
	}

	return false;
}
}

add_filter( 'cdm_fora_do_indice', function ( $fora ) {
	if ( ! cdm_f2_e_minha_pagina() ) {
		return $fora;
	}

	return $fora || cdm_f2_tem_parametro();
} );

add_action( 'wp_head', function () {
	if ( ! cdm_f2_e_minha_pagina() ) {
		return;
	}
	$limpa = home_url( '/' . CDM_F2_SLUG . '/' );

	$perguntas = array();
	foreach ( cdm_f2_perguntas() as $p ) {
		$perguntas[] = array(
			'@type'          => 'Question',
			'name'           => $p['pergunta'],
			'acceptedAnswer' => array( '@type' => 'Answer', 'text' => $p['resposta'] ),
		);
	}

	$grafo = array(
		'@context' => 'https://schema.org',
		'@graph'   => array(
			array(
				'@type'                => 'WebApplication',
				'@id'                  => $limpa . '#ferramenta',
				'name'                 => CDM_F2_TITULO,
				'url'                  => $limpa,
				'applicationCategory'  => 'UtilitiesApplication',
				'operatingSystem'      => 'Web',
				'inLanguage'           => 'pt-BR',
				'isAccessibleForFree'  => true,
				'description'          => 'Seletor de cola e rejunte para mosaico artesanal: a recomendação é recalculada das declarações publicadas pelos fabricantes, com a superfície, o ambiente e a largura da junta.',
				'publisher'            => array( '@id' => home_url( '/#organizacao' ) ),
			),
			array(
				'@type'      => 'FAQPage',
				'@id'        => $limpa . '#perguntas',
				'mainEntity' => $perguntas,
			),
		),
	);

	echo '<script type="application/ld+json" id="cdm-f2-jsonld">' . wp_json_encode( $grafo ) . '</script>' . "\n";
}, 8 );

/* ---------------------------------------------------------------------------
 * 11. Folha e script — no rodapé, NUNCA dentro do retorno do shortcode
 *
 * O WordPress roda os filtros do the_content sobre o que o shortcode devolve e
 * converte o E-comercial duplo em entidade HTML, matando o script inteiro. Foi
 * o defeito que derrubou cinco calculadoras da Aquametria em 08/09/2026.
 *
 * O script daqui NÃO calcula nada: ele só evita o recarregamento quando a
 * pessoa troca uma opção, e some por inteiro sem JavaScript. A conta é do
 * servidor, e é por isso que esta página existe para um modelo de linguagem.
 * ------------------------------------------------------------------------- */

add_action( 'wp_footer', function () {
	if ( ! cdm_f2_e_minha_pagina() ) {
		return;
	}
	echo <<<'HTML'
<style id="cdm-f2-css">
.cdm-f2-form{margin:1.6rem 0;padding:1.2rem;border:1px solid var(--cdm-traco);border-radius:2px;background:var(--cdm-papel);}
.cdm-f2-campo{margin:0 0 1rem;display:flex;flex-direction:column;gap:.3rem;}
.cdm-f2-campo:last-of-type{margin-bottom:0;}
.cdm-f2-campo label{font-family:var(--cdm-display);font-weight:600;font-size:1rem;}
.cdm-f2-ajuda{color:var(--cdm-legenda);font-size:.88rem;line-height:1.45;}
.cdm-f2-form select{font-family:var(--cdm-texto);font-size:1rem;padding:.6rem .7rem;border:1px solid var(--cdm-traco);border-radius:2px;background:var(--cdm-papel);color:var(--cdm-tinta);max-width:100%;}
.cdm-f2-acao{margin:1.2rem 0 0;}
.cdm-f2-botao{display:inline-block;background:var(--cdm-coral);color:#FFFFFF;border:0;border-radius:2px;padding:.7rem 1.2rem;font-family:var(--cdm-display);font-weight:600;font-size:1rem;cursor:pointer;text-decoration:none;}
.cdm-f2-botao:hover{background:var(--cdm-vinho);color:#FFFFFF;text-decoration:none;}
.cdm-f2-resposta{margin:1.6rem 0;padding:1.2rem;border:1px solid var(--cdm-traco);border-left:3px solid var(--cdm-coral);border-radius:2px;}
.cdm-f2-frase{font-size:1.15rem;line-height:1.5;margin:0;}
/* A segunda linha da recomendacao — os que servem sem o fabricante nomear o
   lugar. Ela e frase, nao nota de rodape, entao fica no corpo do texto; o
   degrau de tamanho e o que diz ao olho que o primeiro e o primeiro. */
.cdm-f2-frase.cdm-f2-segunda-linha{font-size:1rem;margin:.7rem 0 0;color:var(--cdm-tinta);}
.cdm-f2-resposta .cdm-prova{margin-top:1rem;}
.cdm-f2-secao{margin:2rem 0;}
.cdm-f2-secao h2{font-size:1.25rem;margin:0 0 .6rem;}
.cdm-f2-vitrine{display:flex;gap:1rem;list-style:none;margin:1rem 0 0;padding:0 0 .6rem;overflow-x:auto;scroll-snap-type:x mandatory;}
.cdm-f2-cartao{scroll-snap-align:start;flex:0 0 15rem;border:1px solid var(--cdm-traco);border-radius:2px;padding:.9rem;display:flex;flex-direction:column;gap:.45rem;}
.cdm-f2-cartao.cdm-f2-segundo{opacity:.85;}
.cdm-f2-foto,.cdm-f2-sem-foto{display:block;width:100%;height:7rem;object-fit:contain;background:#F6F1EE;border-radius:2px;}
.cdm-f2-marca{font-family:var(--cdm-mono);font-size:.78rem;letter-spacing:.04em;text-transform:uppercase;color:var(--cdm-legenda);}
.cdm-f2-cartao h3{font-size:1rem;margin:0;}
.cdm-f2-motivo{font-size:.9rem;line-height:1.45;margin:0;color:var(--cdm-tinta);}
.cdm-f2-compra{margin-top:auto;display:flex;flex-direction:column;align-items:flex-start;gap:.4rem;}
/* A SEGUNDA PORTA DA ESCADA (25.2) É LINHA DE TEXTO, NUNCA SEGUNDO BOTÃO. Dois
   botões no mesmo cartão disputam o clique e o leitor não sabe qual é a
   recomendação; a busca está ali para quem o primeiro link deixou na mão. */
.cdm-f2-busca{font-size:.82rem;color:var(--cdm-legenda);text-decoration:underline;}
.cdm-f2-busca:hover{color:var(--cdm-rubi);}
/* Quando a busca É o botão, ela não vira texto pequeno: é o único caminho de
   compra do cartão, e esconder o único caminho é o "em breve" com outro nome. */
.cdm-f2-botao-busca{background:var(--cdm-rubi);}
.cdm-f2-botao-busca:hover{background:var(--cdm-vinho);}
.cdm-f2-fonte{font-size:.8rem;color:var(--cdm-legenda);}
.cdm-f2-aviso{font-size:.88rem;color:var(--cdm-legenda);margin:.8rem 0 0;}
.cdm-f2-lista-fora{margin:.6rem 0 0;padding-left:1.1rem;}
.cdm-f2-lista-fora li{margin:0 0 .5rem;}
.cdm-f2-silencio,.cdm-f2-ressalva{font-size:.95rem;color:var(--cdm-legenda);margin:.7rem 0 0;}
.cdm-f2-condicao-fora{font-size:.95rem;color:var(--cdm-legenda);margin:.7rem 0 0;}
.cdm-f2-peca-fora{font-size:.95rem;color:var(--cdm-legenda);margin:.7rem 0 0;}
/* A condicao de quem FICOU na recomendacao nao e nota de rodape: ela e parte da
   resposta, entao fica no corpo e nao na cor de legenda. Sem sombra e sem
   gradiente (secao 6), separada por linha de 1px como o resto da ilha. */
.cdm-f2-condicao{margin:.9rem 0 0;padding:.7rem .8rem;border:1px solid var(--cdm-traco);border-radius:2px;font-size:.95rem;}
.cdm-f2-condicao p{margin:0;}
/* O PREPARO (esquema v12). Mesma familia visual da condicao: parte da resposta,
   no corpo e nao em cor de legenda, separado por linha de 1px. O literal vai em
   italico porque e citacao, e a procedencia desce para a cdm-prova logo abaixo,
   que e onde a prova mora nesta ilha (secao 15.2). */
.cdm-f2-preparo{margin:1.1rem 0 0;padding:.8rem .9rem;border:1px solid var(--cdm-traco);border-radius:2px;}
.cdm-f2-preparo h3{font-family:var(--cdm-display);font-size:1rem;font-weight:600;margin:0 0 .5rem;}
.cdm-f2-preparo-item{margin:.5rem 0 0;font-size:.95rem;line-height:1.6;}
.cdm-f2-preparo .cdm-prova{margin:.4rem 0 .8rem;padding:.4rem 0 0;}
.cdm-f2-preparo .cdm-f2-silencio{margin:.7rem 0 0;}
.cdm-f2-rolagem{overflow-x:auto;}
.cdm-f2-tabela{width:100%;font-size:.93rem;}
.cdm-f2-vazio{color:var(--cdm-ambar);}
.cdm-f2-faq{margin:.8rem 0 0;}
.cdm-f2-faq dt{font-family:var(--cdm-display);font-weight:600;margin:1rem 0 .25rem;}
.cdm-f2-faq dd{margin:0;}
@media (max-width:600px){
.cdm-f2-cartao{flex:0 0 78%;}
.cdm-f2-frase{font-size:1.05rem;}
}
</style>
<script id="cdm-f2-js">
/* Troca de opcao ja envia o formulario, para a pessoa nao precisar do botao.
   Nada aqui decide nada: quem responde e o servidor, e sem JavaScript a pagina
   continua inteira — o botao esta la, visivel, e faz o mesmo. */
(function(){
	var f = document.querySelector('.cdm-f2-form');
	if (!f) { return; }
	var selects = f.querySelectorAll('select');
	for (var i = 0; i < selects.length; i++) {
		selects[i].addEventListener('change', function(){ f.submit(); });
	}
	/* Chegou com resposta na tela: leva a pessoa ate ela. */
	if (window.location.search.indexOf('base=') !== -1) {
		var alvo = document.getElementById('resposta');
		if (alvo && !window.location.hash) { alvo.scrollIntoView({behavior:'smooth', block:'start'}); }
	}
})();
</script>
HTML;
}, 20 );
