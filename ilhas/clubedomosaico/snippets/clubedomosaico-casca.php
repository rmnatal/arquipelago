/**
 * Clube do Mosaico Casca — identidade e estrutura do site
 * Versão 1.4.0 (11/09/2026) — DESPACHO DO RAPHAEL (2): O LOGO DELE, INTEIRO, NO
 * CABEÇALHO. "Cadê o logo que eu exigi e subi e mandei até a URL?" e "o nome já
 * está embutido no logo, você não precisa escrever". O cabeçalho passa a servir
 * `logo-clube-do-mosaico.png` em <img> de 52 px de altura, com link para a home
 * e sem UMA LETRA ao lado — o wordmark está dentro do arquivo.
 *
 * A AFIRMAÇÃO QUE SUSTENTAVA A VERSÃO ANTERIOR ESTAVA ERRADA, e ela está escrita
 * três vezes neste arquivo desde 1.2.0: "o arquivo entregue tem fundo preto". Não
 * tem. O Raphael abriu a biblioteca de mídia e mostrou: o PNG de 1536×1024 é
 * TRANSPARENTE. O que aconteceu no ar em 1.1.0 foi outra coisa, e a diferença
 * importa porque uma das duas leituras leva a redesenhar o logo e a outra não: o
 * cabeçalho era PRETO e o wordmark do logo é vinho (#69030C), então ele sumia no
 * fundo — defeito de onde o logo foi posto, nunca do arquivo. O cabeçalho claro
 * de 1.2.0 já tinha consertado a causa; faltou devolver o logo ao lugar dele.
 *
 * O CUSTO DE UM LOGO DE 1,26 MB NUM ESPAÇO DE 78 PX, e o que esta versão faz com
 * ele: o arquivo do Raphael é o original de 1536×1024 e a marca ocupa 78×52 px na
 * tela. Servi-lo cru seria 1,26 MB baixados em toda página de um domínio recém-
 * nascido, e a régua de rastreamento é a primeira coisa que o Google mede num
 * domínio assim (seção 14.1). Não se redesenha nada e não se gera nada — o
 * PROMPT.md proíbe, e com razão: o `src` continua sendo a URL exata que ele
 * mandou, e o `srcset` oferece ao navegador as reduções que o PRÓPRIO WordPress
 * gerou do upload dele (-300x200 com 42 KB, -768x512 com 175 KB). Mesma imagem,
 * mesmo recorte, mesma origem; quem escolhe é o navegador, e quem não entende
 * `srcset` baixa o original e vê a mesma coisa.
 *
 * Versão 1.3.0 (11/09/2026) — A ÁRVORE DA SEÇÃO 16: trilha visível em toda
 * página menos a home, `BreadcrumbList` em JSON-LD e o cluster "Veja também"
 * ligando os três motores da ilha. O mapa mora em `ARVORE.md` e o teste cobra
 * que documento e código digam a mesma coisa.
 *
 * NENHUMA URL MUDOU, e nenhuma precisou mudar: as três seções já eram nível 1,
 * a única página de nível 2 já nascera com mãe em 1.2.0, e as quatro da raiz são
 * as que a 16.1 admite ali. A árvore desta ilha estava certa na estrutura e
 * faltava ficar VISÍVEL — que é o que a 16.3 e a 16.4 pedem. Por isso este bloco
 * não tem 301 nenhum e o sitemap não muda.
 *
 * DUAS COISAS QUE ESTAVAM ERRADAS E NÃO ESTAVAM SENDO PROCURADAS:
 *   (a) o registro do Guia e o `VOZ.md` discordavam nos slugs de duas
 *       categorias (`materiais/colas` × `colas-e-adesivos`, `materiais/alicates`
 *       × `alicates-e-corte`) desde que a casca nasceu. O dia de acertar é o dia
 *       ANTES de a página existir;
 *   (b) o cartão de categoria que ainda não abre trazia "5 no banco, ficha em
 *       construção". O número era certo e contado — e a 16.5 proíbe contagem de
 *       banco justamente nesse cartão, porque é promessa com número num link que
 *       não existe. O número continua na camada de prova, onde quem quer
 *       conferir confere.
 *
 * Versão 1.2.0 (11/09/2026) — DESPACHO DO RAPHAEL: cabeçalho claro, a marca
 * legível, a home deixando de ser manifesto e o Guia falando com quem vai fazer
 * a peça. O Raphael viu a casca no ar e reprovou: "muito ruim o fundo preto no
 * header, o logo sumiu, queria algo mais clean". Esta versão acertou a metade
 * grande — o cabeçalho branco com linha de 1 px e o menu em texto escuro — e
 * errou o diagnóstico do logo sumido, pondo a culpa no arquivo em vez do fundo
 * em que ele foi posto. 1.4.0 desfaz a metade errada. A lótus solta de
 * identidade/logo/lotus-512.png continua TRUNCADA no repositório (o IDAT declara
 * 11.638 bytes num arquivo com 8.770) e segue sem uso no cabeçalho — o que vai
 * ali é o logo completo, que existe e abre.
 *
 * Versão 1.1.0 (11/09/2026) — Bloco 3c: o Guia passou a CONTAR o banco por categoria
 * em vez de trazer um zero digitado. O cartão de Rejuntes dizia "0 no banco" no mesmo
 * dia em que a categoria ganhou cinco produtos — número falso na tela, e o teste não viu
 * porque só media a categoria que existia quando ele foi escrito.
 * Versão 1.0.0 (11/09/2026) — Bloco 3b, a primeira casca desta ilha.
 *
 * Derivada da casca da Robometria 1.0.2 por SUBSTITUIÇÃO DE IDENTIDADE, não por
 * cópia cega. O que sobrou igual sobrou porque já era regra do Arquipélago
 * (seção 6 do ARQUIPELAGO.md): menu sanfona com aria-expanded/aria-controls e
 * links de verdade no HTML servido, favicon próprio no lugar do ícone do
 * WordPress, nenhum <script> ou <style> dentro do retorno de shortcode, e a
 * trava que impede link de listagem para página que não existe.
 *
 * O QUE ESTA CASCA TEM DE DIFERENTE DAS DUAS PRIMEIRAS ILHAS, e por quê:
 *
 *   1. TRÊS MOTORES, não um. Aquametria e Robometria são sites de ferramenta com
 *      conteúdo em volta. Aqui a home tem que apresentar LOJA (peça própria da
 *      artesã, margem cheia), GUIA (fichas de material com afiliado) e ESCOLA
 *      (tutoriais), e a malha fecha o ciclo entre os três. Por isso o catálogo
 *      desta casca não é "ferramentas": são três catálogos, um por motor.
 *   2. A MARCA É UMA IMAGEM ENTREGUE, não um SVG desenhado aqui. O logo do Clube
 *      do Mosaico foi feito por gente e subido pelo Raphael na biblioteca de
 *      mídia; o PROMPT.md da ilha proíbe redesenhar, vetorizar ou escrever o nome
 *      em texto ao lado dele (o arquivo já contém o wordmark). Então a marca sai
 *      em <img>, e o alt carrega o nome para quem não vê a imagem.
 *   3. CABEÇALHO CLARO, RODAPÉ PRETO, MIOLO BRANCO (1.2.0). O preto da identidade
 *      é cor de TEXTO e de detalhe, não bloco grande no topo: quem vende peça
 *      abre a página com a peça, não com uma faixa escura. O coral continua
 *      sendo cor de sinal: um uso por tela, no botão principal e no preço.
 *   4. ESTADO VAZIO HONESTO NA LOJA. Não existe peça cadastrada — o catálogo é
 *      cadastrado pela própria artesã no painel /atelie/ (bloco 4d) e nunca vive
 *      no repositório. Página de coleção sem peça diz "em breve" com todas as
 *      letras; peça inventada é proibida nesta ilha por decisão escrita.
 *
 * Faz oito coisas:
 *   (a) carrega Outfit, Source Sans 3 e JetBrains Mono e injeta a paleta no wp_head;
 *   (b) troca a saída de core/site-title e core/site-logo pelo logo oficial;
 *   (c) troca a saída de core/navigation pelo menu Loja · Materiais · Como fazer · Sobre;
 *   (d) cria, casando pelo slug, as oito páginas da ilha e fixa inicio como home;
 *   (e) manda "Hello world!" e "Sample Page" para a LIXEIRA (nunca apaga);
 *   (f) substitui a template part 'footer' do tema pelo rodapé desta ilha;
 *   (g) redireciona 301 os apelidos de endereço para a página canônica;
 *   (h) publica o ícone do site e o JSON-LD Organization + WebSite (seção 5.3).
 *
 * O conteúdo das oito páginas mora em shortcodes deste snippet: atualizar o
 * snippet atualiza as páginas, sem tocar no editor do WordPress.
 *
 * Idempotente: rodar duas vezes não duplica página, não repete lixeira e não
 * reescreve página editada à mão. flush_rewrite_rules() só quando cria página.
 *
 * Regras herdadas (fase 4b): não usa a superglobal de servidor; sem "<?php" no
 * topo (o Code Snippets põe); texto de tela acentuado em UTF-8; toda função de
 * nível superior dentro de if ( ! function_exists() ).
 */

if ( ! defined( 'ABSPATH' ) ) {
	return;
}

if ( ! defined( 'CDM_CASCA_VERSAO' ) ) {
	define( 'CDM_CASCA_VERSAO', '1.4.0' );
	/* O nome do site e a linha que o WordPress serve no <title> da home. A
	   Aquametria descobriu em 11/09/2026 que a tagline nunca tocada desde o
	   nascimento da ilha continuava sendo a linha mais lida do site — a do
	   resultado de busca. Esta casca grava as duas, como grava page_on_front. */
	define( 'CDM_CASCA_NOME_SITE', 'Clube do Mosaico' );
	define( 'CDM_CASCA_TAGLINE', 'Mosaico feito à mão, uma peça por vez' );
	/* Os dois arquivos que o Raphael subiu na biblioteca de mídia em 11/09/2026.
	   São os únicos endereços de imagem que esta casca conhece, e não se
	   substituem por desenho feito aqui (regra escrita no PROMPT.md da ilha).
	   O logo completo é TRANSPARENTE (conferido por ele na biblioteca de mídia) e
	   serve os dois consumidores: o olho de quem entra, no cabeçalho, e o Google,
	   como `logo` do Organization no JSON-LD. A única coisa que ele não aceita é
	   fundo escuro, porque o wordmark dentro do arquivo é vinho. */
	define( 'CDM_CASCA_LOGO_URL', 'https://clubedomosaico.com.br/wp-content/uploads/2026/09/logo-clube-do-mosaico.png' );
	/* As reduções que o WordPress gerou do upload DELE. Não são arquivo novo nem
	   imagem tratada: é o mesmo PNG, mesmo recorte, servido menor para um espaço
	   de 78 px. Se um dia sumirem, o `src` acima continua de pé sozinho. */
	define( 'CDM_CASCA_LOGO_300', 'https://clubedomosaico.com.br/wp-content/uploads/2026/09/logo-clube-do-mosaico-300x200.png' );
	define( 'CDM_CASCA_LOGO_768', 'https://clubedomosaico.com.br/wp-content/uploads/2026/09/logo-clube-do-mosaico-768x512.png' );
	/* O logo é 1536×1024, então 3:2. No cabeçalho ele sai com 52 px de altura, que
	   é o número do despacho, e 78 px de largura — declarados no <img> para a
	   linha do cabeçalho não pular quando a imagem chegar. */
	define( 'CDM_CASCA_LOGO_ALTURA', 52 );
	define( 'CDM_CASCA_LOGO_LARGURA', 78 );
	define( 'CDM_CASCA_FAVICON_URL', 'https://clubedomosaico.com.br/wp-content/uploads/2026/09/clube-do-mosaico-favicon.png' );
}

/* ---------------------------------------------------------------------------
 * 1. Os três motores da ilha
 *
 * Um catálogo por motor, e cada um existe pela mesma razão da seção 9 do
 * ARQUIPELAGO.md: toda página tem que entrar em pelo menos DUAS listagens. Com
 * os catálogos aqui, página nova aparece na home e no hub do motor dela sem que
 * nenhuma das duas seja editada de novo.
 *
 * As listas de fichas e de tutoriais nascem VAZIAS de propósito: cada página se
 * registra pelo filtro dentro do próprio snippet dela. A casca nunca precisa
 * saber quantas páginas a ilha tem — e uma listagem que promete o que não
 * existe é pior que uma listagem curta.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_casca_ferramentas' ) ) {
/**
 * As duas calculadoras, especificadas no bloco 2 e ainda em construção.
 *
 * Os títulos são a pergunta que a pessoa digita, não o nome interno (seção
 * 14.5). "F1" e "F2" existem para a fila da Fundação; o visitante não precisa
 * saber deles, e por isso o código sai pequeno, acima do título, em monoespaçada.
 */
function cdm_casca_ferramentas() {
	$lista = array(
		array(
			'codigo' => 'F2',
			'titulo' => 'Qual cola e qual rejunte para a sua peça',
			'slug'   => 'qual-cola-usar-no-mosaico',
			'resumo' => 'Você diz sobre o que vai colar — cerâmica, vidro, espelho, MDF, cimento, metal — e onde a peça vai ficar: dentro de casa, na área molhada, no sol e na chuva. Sai a cola, o rejunte e o motivo. Quando o fabricante proíbe aquela base, a gente avisa em vez de sugerir assim mesmo.',
			'estado' => 'em-construcao',
		),
		array(
			'codigo' => 'F1',
			'titulo' => 'Quantas pastilhas e quanto rejunte a sua peça precisa',
			'slug'   => 'quantas-pastilhas-para-mosaico',
			'resumo' => 'A forma da peça, as medidas, o tamanho da pastilha e a folga entre elas. Sai quantas pastilhas comprar, já com sobra, e quanto rejunte levar — pela conta da pastilha pequena, não a do azulejo de obra.',
			'estado' => 'em-construcao',
		),
	);

	$lista = apply_filters( 'cdm_ferramentas', $lista );

	return is_array( $lista ) ? $lista : array();
}
}

if ( ! function_exists( 'cdm_casca_categorias_do_guia' ) ) {
/**
 * As seis categorias do Guia de materiais.
 *
 * 'no_banco' é quantos itens REAIS o repositório já tem naquela categoria, e
 * não uma promessa: é ele que decide se a categoria aparece como ficha aberta ou
 * como categoria ainda sem dado. Nenhum destes números é digitado: cada um vem de
 * cdm_casca_numeros(), que conta o arquivo do banco daquela categoria. Foi assim que
 * o bloco 3c achou o zero de Rejuntes escrito à mão, no dia em que a categoria ganhou
 * cinco produtos — categoria nova sem linha na lista de bancos continua mostrando
 * zero, e é por isso que o teste cobra as duas listas juntas.
 */
function cdm_casca_categorias_do_guia() {
	$n = cdm_casca_numeros();

	$lista = array(
		array(
			'codigo'   => 'G-COLAS',
			'titulo'   => 'Colas e adesivos',
			'slug'     => 'materiais/colas-e-adesivos',
			'resumo'   => 'Cola branca, silicone, cimentcola, epóxi: qual delas segura a sua peça — e em qual base o próprio fabricante manda não usar.',
			'no_banco' => $n['materiais_cola'],
		),
		array(
			'codigo'   => 'G-REJUNTES',
			'titulo'   => 'Rejuntes',
			'slug'     => 'materiais/rejuntes',
			'resumo'   => 'Qual rejunte vai entre os caquinhos, e quanto dele a sua peça come de verdade. A conta que circula por aí é de azulejo de obra, e erra feio na pastilha pequena.',
			'no_banco' => $n['materiais_rejunte'],
		),
		array(
			'codigo'   => 'G-PASTILHAS',
			'titulo'   => 'Pastilhas e tesselas',
			'slug'     => 'materiais/pastilhas',
			'resumo'   => 'Vidro, cerâmica, cristal e caquinho irregular: como cada uma é vendida (por peça, por grama ou na placa) e quanto rende.',
			'no_banco' => 0,
		),
		array(
			'codigo'   => 'G-ALICATES',
			'titulo'   => 'Alicates e corte',
			'slug'     => 'materiais/alicates-e-corte',
			'resumo'   => 'Torquês de roda, alicate de corte e cortador: o que cada um corta sem estilhaçar, e qual deles estraga a peça.',
			'no_banco' => 0,
		),
		array(
			'codigo'   => 'G-BASES',
			'titulo'   => 'Bases',
			'slug'     => 'materiais/bases',
			'resumo'   => 'Vaso de cerâmica, vidro, MDF, cimento, cachepô e tampo. A base muda a cola — é a primeira pergunta de todas.',
			'no_banco' => 0,
		),
		array(
			'codigo'   => 'G-ACABAMENTO',
			'titulo'   => 'Acabamento',
			'slug'     => 'materiais/acabamento',
			'resumo'   => 'Verniz, impermeabilizante e como limpar depois do rejunte. É a etapa que decide se a peça aguenta sol, chuva e pia.',
			'no_banco' => 0,
		),
	);

	$lista = apply_filters( 'cdm_categorias_do_guia', $lista );

	return is_array( $lista ) ? $lista : array();
}
}

if ( ! function_exists( 'cdm_casca_tutoriais' ) ) {
/** Os tutoriais da Escola. Cada um se registra pelo filtro no snippet dele. */
function cdm_casca_tutoriais() {
	$lista = apply_filters( 'cdm_tutoriais', array() );

	return is_array( $lista ) ? $lista : array();
}
}

/**
 * URL REAL da página, ou '' se ela não existe publicada no site.
 *
 * Duas vias, nesta ordem:
 *   1. o id do repositório, que o Sync grava em _clubedomosaico_id. É a
 *      identidade canônica e sobrevive ao WordPress ter mudado o slug por
 *      conflito — quando o slug pedido já está ocupado, wp_insert_post
 *      acrescenta "-2" em silêncio;
 *   2. o slug, para as páginas que não vieram do Sync.
 *
 * Devolve '' quando nenhuma via acha a página, e quem chama NÃO publica link.
 * Link de hub para página inexistente é 404 no ar — a Aquametria pagou esse
 * defeito em 08/09/2026 e as ilhas seguintes nascem com a trava.
 */
if ( ! function_exists( 'cdm_casca_url_se_existir' ) ) {
function cdm_casca_url_se_existir( $slug ) {
	$slug = trim( (string) $slug, '/' );
	if ( '' === $slug ) {
		return '';
	}

	$achados = get_posts( array(
		'post_type'   => 'page',
		'post_status' => 'publish',
		'meta_key'    => '_clubedomosaico_id',
		'meta_value'  => $slug,
		'numberposts' => 1,
	) );
	if ( $achados ) {
		return get_permalink( $achados[0] );
	}

	$pagina = get_page_by_path( $slug, OBJECT, 'page' );
	if ( $pagina && 'publish' === $pagina->post_status ) {
		return get_permalink( $pagina );
	}

	return '';
}
}

/**
 * Link de texto que só vira <a> se a página existir. Sem página, sai o rótulo
 * sozinho — nunca um endereço que devolve 404.
 */
if ( ! function_exists( 'cdm_casca_link_html' ) ) {
function cdm_casca_link_html( $slug, $rotulo ) {
	$url = cdm_casca_url_se_existir( $slug );
	if ( '' === $url ) {
		return '<span class="cdm-sem-link">' . esc_html( $rotulo ) . '</span>';
	}
	return '<a href="' . esc_url( $url ) . '">' . esc_html( $rotulo ) . '</a>';
}
}

/* ---------------------------------------------------------------------------
 * 1b. Apelidos de endereço — o 404 que o visitante não deveria ver
 *
 * Cada apelido plausível redireciona 301 para a página canônica, e o 301 é o
 * que faz o sinal de busca ficar com o endereço canônico em vez de se espalhar.
 *
 * Trava: o redirecionamento SÓ acontece se a página de destino existir
 * publicada. Redirecionar para outro 404 é pior que o 404 original.
 *
 * O que deliberadamente NÃO está aqui: 'atelie'. Esse endereço é o painel da
 * artesã (bloco 4d) e tem dono próprio; um apelido da casca apontando para
 * outro lugar tiraria o painel do ar no dia em que ele nascesse.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_casca_apelidos' ) ) {
function cdm_casca_apelidos() {
	$mapa = array(
		/* Guia de materiais */
		'guia'                       => 'materiais',
		'guia-de-materiais'          => 'materiais',
		'material-para-mosaico'      => 'materiais',
		'materiais-para-mosaico'     => 'materiais',
		'material'                   => 'materiais',
		/* Escola */
		'escola'                     => 'como-fazer',
		'tutoriais'                  => 'como-fazer',
		'tutorial'                   => 'como-fazer',
		'aprender'                   => 'como-fazer',
		'como-fazer-mosaico'         => 'como-fazer',
		'mosaico-para-iniciantes'    => 'como-fazer',
		/* Loja */
		'pecas'                      => 'loja',
		'peca'                       => 'loja',
		'produtos'                   => 'loja',
		'comprar'                    => 'loja',
		/* Páginas da casca */
		'afiliados'                  => 'divulgacao-de-afiliados',
		'divulgacao'                 => 'divulgacao-de-afiliados',
		'politica-de-privacidade'    => 'privacidade',
		'fale-conosco'               => 'contato',
		'quem-somos'                 => 'sobre',
	);

	return apply_filters( 'cdm_apelidos_de_pagina', $mapa );
}
}

/**
 * Slug canônico de um caminho pedido, ou '' se ele não for apelido conhecido.
 * Isolada da requisição de propósito, para o teste poder exercitá-la sozinha.
 */
if ( ! function_exists( 'cdm_casca_apelido_para_slug' ) ) {
function cdm_casca_apelido_para_slug( $caminho ) {
	$caminho = trim( (string) $caminho );
	$caminho = trim( $caminho, '/' );
	if ( '' === $caminho || false !== strpos( $caminho, '/' ) ) {
		return '';
	}

	$caminho = sanitize_title( $caminho );
	$mapa    = cdm_casca_apelidos();

	return isset( $mapa[ $caminho ] ) ? $mapa[ $caminho ] : '';
}
}

/**
 * Caminho pedido nesta requisição, sem a superglobal de servidor (fase 4b: o
 * ModSecurity desta hospedagem mata a gravação do snippet em silêncio quando o
 * nome dela aparece escrito — inclusive dentro de comentário).
 */
if ( ! function_exists( 'cdm_casca_caminho_pedido' ) ) {
function cdm_casca_caminho_pedido() {
	if ( isset( $GLOBALS['wp'] ) && is_object( $GLOBALS['wp'] ) && isset( $GLOBALS['wp']->request ) ) {
		return (string) $GLOBALS['wp']->request;
	}

	$atual = add_query_arg( array() );
	$atual = strtok( (string) $atual, '?' );

	return trim( (string) $atual, '/' );
}
}

if ( ! function_exists( 'cdm_casca_redirecionar_apelido' ) ) {
function cdm_casca_redirecionar_apelido() {
	if ( ! is_404() ) {
		return;
	}

	$destino = cdm_casca_apelido_para_slug( cdm_casca_caminho_pedido() );
	if ( '' === $destino ) {
		return;
	}

	$url = cdm_casca_url_se_existir( $destino );
	if ( '' === $url ) {
		return;
	}

	wp_safe_redirect( $url, 301 );
	exit;
}
}

add_action( 'template_redirect', 'cdm_casca_redirecionar_apelido' );

/* ---------------------------------------------------------------------------
 * 2. Marca, menu e rodapé
 *
 * A MARCA É O ARQUIVO DELE, INTEIRO (1.4.0). Até 1.1.0 o cabeçalho servia esse
 * mesmo arquivo, e o cabeçalho inteiro era PRETO — foi assim que o wordmark
 * vinho de dentro do logo sumiu, e o Raphael reprovou os dois de uma vez ("fundo
 * preto no header, o logo sumiu"). A 1.2.0 leu o sintoma ao contrário: culpou o
 * ARQUIVO, escreveu três vezes neste snippet que ele tinha fundo preto e trocou
 * o logo por um wordmark em texto. O arquivo é transparente — quem estava errado
 * era o fundo em que ele foi posto, e isso a 1.2.0 já tinha consertado.
 *
 * Então agora: o logo completo, 52 px de altura, link para a home, e NENHUM
 * texto ao lado. O nome está desenhado dentro da imagem — escrevê-lo de novo
 * seria a marca em dobro na tela e anunciada duas vezes por leitor de tela. Por
 * isso o `alt` carrega o nome e não existe <span> nenhum aqui: quem não vê a
 * imagem ouve "Clube do Mosaico" uma vez, que é exatamente o que a imagem diz.
 *
 * A lótus solta (identidade/logo/lotus-512.png) NÃO entra no cabeçalho, e agora
 * não é por estar truncada: o lugar dela é ícone pequeno, onde o logo completo
 * não cabe. A constante embutida continua existindo para esses lugares e não tem
 * mais caminho para dentro da marca.
 * ------------------------------------------------------------------------- */

/* MARCA-INICIO — gerado por ferramentas/gerar-marca.php, nao edite a mao */
if ( ! defined( 'CDM_CASCA_MARCA_LOTUS' ) ) {
	define( 'CDM_CASCA_MARCA_LOTUS', '' );
}
/* MARCA-FIM */

if ( ! function_exists( 'cdm_casca_marca_html' ) ) {
function cdm_casca_marca_html() {
	static $ja_impressa = false;
	if ( $ja_impressa ) {
		return '';
	}
	$ja_impressa = true;

	/* O `srcset` oferece as reduções que o PRÓPRIO WordPress gerou do upload dele,
	   e o `sizes` diz a largura real na tela: o navegador baixa 42 KB no lugar de
	   1,26 MB e desenha exatamente o mesmo logo. O `src` continua sendo a URL que
	   o despacho mandou usar, então quem ignorar o srcset vê a mesma imagem. */
	$srcset = esc_url( CDM_CASCA_LOGO_300 ) . ' 300w, '
		. esc_url( CDM_CASCA_LOGO_768 ) . ' 768w, '
		. esc_url( CDM_CASCA_LOGO_URL ) . ' 1536w';

	$html  = '<a class="cdm-marca" href="' . esc_url( home_url( '/' ) ) . '" rel="home">';
	$html .= '<img class="cdm-marca-logo" src="' . esc_url( CDM_CASCA_LOGO_URL ) . '"'
		. ' srcset="' . esc_attr( $srcset ) . '"'
		. ' sizes="' . (int) CDM_CASCA_LOGO_LARGURA . 'px"'
		. ' alt="' . esc_attr( CDM_CASCA_NOME_SITE ) . '"'
		. ' width="' . (int) CDM_CASCA_LOGO_LARGURA . '" height="' . (int) CDM_CASCA_LOGO_ALTURA . '"'
		. ' decoding="async" fetchpriority="high">';
	$html .= '</a>';

	return $html;
}
}

/**
 * O menu. Abaixo de 782 px ele vira sanfona atrás de um botão; acima, é a mesma
 * fileira de links de sempre.
 *
 * Três decisões, e nenhuma é enfeite:
 *
 *   1. Os links saem SEMPRE no HTML servido, dentro de <nav>. O botão não gera
 *      link nenhum: só mostra e esconde o que já está lá. É o que faz o menu
 *      continuar existindo para quem lê sem executar JavaScript — o crawler de
 *      IA, que é regra de primeira classe (seção 5), e o visitante cujo script
 *      não carregou.
 *   2. Quem esconde a lista no celular é o seletor [data-cdm-menu], e esse
 *      atributo quem põe é o JavaScript do rodapé. Sem JavaScript o atributo não
 *      existe, a regra não casa e o menu fica visível como lista.
 *   3. O id é contado, porque o filtro render_block pode trocar mais de um bloco
 *      core/navigation na mesma página, e aria-controls apontando para um id
 *      repetido não controla coisa nenhuma.
 *
 * A ordem dos itens é a dos três motores, e a Loja vem primeiro de propósito:
 * é o único motor com margem cheia, e a seção 9 manda pôr na frente o caminho
 * que termina em compra.
 */
if ( ! function_exists( 'cdm_casca_nav_html' ) ) {
function cdm_casca_nav_html() {
	static $quantos = 0;
	$quantos++;
	$id = 'cdm-nav-lista' . ( $quantos > 1 ? '-' . $quantos : '' );

	$itens = array(
		'loja'       => 'Loja',
		'materiais'  => 'Materiais',
		'como-fazer' => 'Como fazer',
		'sobre'      => 'Sobre',
	);

	$html  = '<div class="cdm-nav-caixa">';
	$html .= '<button type="button" class="cdm-nav-botao" aria-expanded="false" aria-controls="' . esc_attr( $id ) . '">';
	$html .= '<span class="cdm-nav-tracos" aria-hidden="true"></span>';
	$html .= '<span class="cdm-nav-rotulo">Menu</span>';
	$html .= '</button>';
	$html .= '<nav class="cdm-nav" id="' . esc_attr( $id ) . '" aria-label="Navegação principal"><ul>';
	foreach ( $itens as $slug => $rotulo ) {
		$html .= '<li>' . cdm_casca_link_html( $slug, $rotulo ) . '</li>';
	}
	$html .= '</ul></nav>';
	$html .= '</div>';

	return $html;
}
}

if ( ! function_exists( 'cdm_casca_rodape_impresso' ) ) {
/**
 * Marca e consulta se o rodapé desta ilha já saiu nesta requisição.
 * Evita rodapé duplicado quando o filtro render_block já trocou a template part.
 */
function cdm_casca_rodape_impresso( $marcar = false ) {
	static $impresso = false;
	if ( $marcar ) {
		$impresso = true;
	}
	return $impresso;
}
}

if ( ! function_exists( 'cdm_casca_rodape_html' ) ) {
function cdm_casca_rodape_html() {
	cdm_casca_rodape_impresso( true );

	$html  = '<footer class="cdm-rodape"><div class="cdm-rodape-interno">';
	$html .= '<p class="cdm-tagline">' . esc_html( CDM_CASCA_TAGLINE ) . '</p>';
	$html .= '<p>As peças são feitas à mão, uma a uma, por uma artesã. As recomendações de material não são opinião nossa: cada uma cita a declaração do fabricante, com o documento e a data em que foi verificada — e quando o fabricante não declara, a página diz que não declara em vez de supor.</p>';
	$html .= '<p>' . cdm_casca_link_html( 'sobre', 'Sobre' )
		. ' · ' . cdm_casca_link_html( 'contato', 'Contato' )
		. ' · ' . cdm_casca_link_html( 'divulgacao-de-afiliados', 'Divulgação de afiliados' )
		. ' · ' . cdm_casca_link_html( 'privacidade', 'Privacidade' )
		. ' · Clube do Mosaico ' . esc_html( date_i18n( 'Y' ) ) . '</p>';
	$html .= '</div></footer>';

	return $html;
}
}

add_filter( 'render_block', function ( $conteudo, $bloco ) {
	if ( is_admin() || ( defined( 'REST_REQUEST' ) && REST_REQUEST ) ) {
		return $conteudo;
	}
	$nome = isset( $bloco['blockName'] ) ? $bloco['blockName'] : '';
	if ( 'core/site-title' === $nome || 'core/site-logo' === $nome ) {
		return cdm_casca_marca_html();
	}
	if ( 'core/navigation' === $nome ) {
		return cdm_casca_nav_html();
	}
	// A tagline padrão do WordPress é resíduo do tema; a desta ilha está no rodapé.
	if ( 'core/site-tagline' === $nome ) {
		return '';
	}
	// Em tema de blocos o rodapé é uma template part renderizada DENTRO do fluxo do
	// conteúdo. Trocar a saída dela aqui é o que impede os dois rodapés empilhados.
	if ( 'core/template-part' === $nome ) {
		$parte = isset( $bloco['attrs']['slug'] ) ? $bloco['attrs']['slug'] : '';
		if ( 'footer' === $parte || 'rodape' === $parte ) {
			return cdm_casca_rodape_html();
		}
	}
	return $conteudo;
}, 10, 2 );

// Rede de segurança: se o tema NÃO usa template part de rodapé (ou o filtro não
// pegou), o rodapé sai aqui. Se já saiu no lugar da template part, não repete.
add_action( 'wp_footer', function () {
	if ( cdm_casca_rodape_impresso() ) {
		return;
	}

	echo cdm_casca_rodape_html(); // markup próprio, já escapado campo a campo
}, 20 );

/* ---------------------------------------------------------------------------
 * 2b. Ícone do site
 *
 * O WordPress imprime o ícone dele em wp_head na prioridade 99, e sem tirar
 * aquele de lá o site sairia com dois — a aba escolheria um, o iOS outro.
 *
 * Aqui o ícone NÃO é desenhado em SVG como nas duas primeiras ilhas: a lótus é
 * arte entregue, e o PROMPT.md proíbe redesenhá-la. O de 32 px viaja embutido
 * como data URI (identidade/logo/favicon-32.png, entre os marcadores abaixo,
 * gerado por ferramentas/gerar-favicon.php) para a aba não depender de rede; o
 * apple-touch-icon aponta para o arquivo da biblioteca de mídia, que é o mesmo
 * desenho em tamanho grande.
 * ------------------------------------------------------------------------- */

/* FAVICON-INICIO — gerado por ferramentas/gerar-favicon.php, nao edite a mao */
if ( ! defined( 'CDM_CASCA_ICONE_PNG_32' ) ) {
	define( 'CDM_CASCA_ICONE_PNG_32', 'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAAFPElEQVR42u1Va0wUVxQ+987Mwj5ZFpbXACJWnkJEaYq0GpW2BGt91VKamCYi+KIKsanVNi19pLZqrWhSrZpUQ7HWpLFUoatRozY1gRRcQF1wRaWUZXkusLvMvmbu7Y/FFkWb9Icxbfx+3czknO+e853zXUQphUcJDI8YTwj+cwSEACH/KgI9pjGllEoSJQT89JT6D/TwPnpwz/gvQCklhErSwy7KPqQwhBjmLzKgFDAme7bR2hOIUHDY0Vvvj/UKIYTQP1TATrw6Qmh0YLC7uSmI54NjYzmFAhCQfbvoqR9QWAQAJYZqpFLjNWUA4BOEoc7O4a6uqPR0VVgYUAr38rEPkJFhTDU1DZWVSr2e4biMgtdS8vKwVivJAkD0AaUgl2OtlkpSm+H01epq0euxW3um5+dnFRdRQv4u/YEaIIahlPZeNyn1ejYgQLDZ1Dx/eU1JiwOY8u3UbqeCwHy409gj1G8oU0ZGOvv72YBAdUREv/nGxOz3E1BCgBBnT2/fjTafILiGhkMTE9UKZWetoWHdetMtK7OqhFld2tLYaiwr/b3WEBSk0U2Z4rLZRJdr4NZtu9UKhNB755gd3xyEMQAw8sDMwkLPqNPa1KyNi7O3tvlGnarY2PrC4qjm3zyDQ43L56snx7sHBx3mdu2kWMzgqIwMmVLJKhSAMfL3GeMJBBhTpwN13eG0etbap1AqYpYsVSclWE7WeB3DnEqljpskioRirOR50ePx2kd8TufMggJHa5uj/bZ3YJhzu+D6HRoTjzTacYvmr0hw0jPV9GoDGrZ5V7z546oNHosFy2TJRYXpG0vMVd9dLts458vdt20OebBWN9DbsH3H7INfT166+MrnX5i/PUpEMTA6Ztk3e7kjFVQbglKmowXLQaXxa0ABIRiy0YsG8HgIQADxRM6dK9NomMBAu7W771StmtD5VUeDpqVeO3HSdMqgz541//gx1mLtN5y1WyycSiVTKfnnc2Sii2AGRB/99RwM2wAhoBQDwgAA4ZEQGUM9LiKMQnN9/IIXvU6n5HIPNBqZ0JCmTRvlLnfwrKyh9lsDptaI3BfAZL5e/h4KCR5oNBK3W/R4n1qUB8Y6MuqkLgH4WIjg/W1nx2afk0FCKkN8zPI3RKU2IiY+5/sqwWr1dveoEhNCZz5rLC7KTE0lCAPD2hqMTeVbY/OWqOInp68ukkWEq+MmhSRO9WnkXEYWnK8hSWnAyfxSs2PyShJemG/jE26ePt9XV8cCzD586OyhIwSLkJiQsneXae16d0eHTKOWaTVC242oZ2ZN+fiD9gZj/S8XVVr90k/Lz7xSAJws5OnMhJeXhc6cQSXJvxOs3x8QwzhHRuyDQzf37ZfpdJLX27jl3ZzSkkP5r186WjVjXu6i7duj05MVwVq1PjQmN0dQaw4UrzM11SelZiypLK8r3eTssmCWGWlpicrOkjsFpS7YbxuISBLCuNfUWrNlS/LiRbw+vG7zViJKXoeDfy477Z23Lx87fqGiwgNiac3pbmOzQhfMKhQHVq7Qcep5mzdlvrTgykef9De3cAoFExiQteOzzs4O88+GhTt3hiUlUkIQJUT0ei/trnD09BLRl5b/amhI6LWv9rt6+zwOp1ynTS5cyUVHt168YO+w5JZv9Qquc9t2hKelTM3OdpnNrYcrfS4Xp1QoeX5ayVpr1x9tP50EhDQ8P6eslOE4v58Tehei203HgRDiHhqmD8HEX+PD/WnHvWj+AxpbPYTxeA+nkgQIYcwAUEIIUIpZ9n4f80fdzfN4n8wnBP8ngj8BgtPm2pQjSmwAAAAASUVORK5CYII=' );
}
/* FAVICON-FIM */

remove_action( 'wp_head', 'wp_site_icon', 99 );

add_action( 'wp_head', function () {
	if ( defined( 'CDM_CASCA_ICONE_PNG_32' ) && '' !== CDM_CASCA_ICONE_PNG_32 ) {
		echo '<link rel="icon" type="image/png" sizes="32x32" href="' . esc_attr( 'data:image/png;base64,' . CDM_CASCA_ICONE_PNG_32 ) . '">' . "\n";
	}
	// O iOS não aceita data URI neste rel em todas as versões, e aplica a própria
	// máscara de canto — por isso aqui vai o arquivo grande, quadrado, da lótus
	// sobre branco, que é exatamente o que o Raphael entregou.
	echo '<link rel="apple-touch-icon" sizes="180x180" href="' . esc_url( CDM_CASCA_FAVICON_URL ) . '">' . "\n";
	// A barra do navegador no celular acompanha o cabeçalho, e ele ficou claro.
	echo '<meta name="theme-color" content="#FFFFFF">' . "\n";
}, 5 );

/* ---------------------------------------------------------------------------
 * 2c. JSON-LD de entidade (seção 5.3 e 5.6 do ARQUIPELAGO.md)
 *
 * Organization e WebSite em toda página. O que NÃO sai daqui é o sameAs: os
 * perfis de rede social da artesã foram prometidos pelo Raphael e ainda não
 * chegaram, e sameAs apontando para perfil inventado seria exatamente a
 * fabricação que o Arquipélago existe para não fazer. Ele entra no dia em que
 * houver perfil de verdade.
 * ------------------------------------------------------------------------- */

add_action( 'wp_head', function () {
	$org = array(
		'@type'       => 'Organization',
		'@id'         => home_url( '/#organizacao' ),
		'name'        => 'Clube do Mosaico',
		'url'         => home_url( '/' ),
		'logo'        => CDM_CASCA_LOGO_URL,
		'description' => 'Ateliê de mosaico artesanal e guia técnico de materiais: peças feitas à mão e a declaração do fabricante por trás de cada recomendação de cola, rejunte e pastilha.',
		'knowsAbout'  => array( 'mosaico artesanal', 'pastilha de vidro', 'tessela', 'cola para mosaico', 'rejunte', 'silicone neutro', 'técnica bizantina' ),
	);

	$grafo = array(
		'@context' => 'https://schema.org',
		'@graph'   => array(
			$org,
			array(
				'@type'      => 'WebSite',
				'@id'        => home_url( '/#site' ),
				'name'       => 'Clube do Mosaico',
				'url'        => home_url( '/' ),
				'inLanguage' => 'pt-BR',
				'publisher'  => array( '@id' => home_url( '/#organizacao' ) ),
			),
		),
	);

	echo '<script type="application/ld+json" id="cdm-casca-jsonld">'
		. wp_json_encode( $grafo ) . '</script>' . "\n";
}, 6 );

/* ---------------------------------------------------------------------------
 * 3. Tipografia e paleta por cima do tema ativo
 *
 * O coral (#FC483B) é COR DE SINAL: um uso por tela, e nesta ilha esse uso é o
 * botão principal ou o preço. Por isso link não é coral — link é rubi
 * (#8A0F18), que é a mesma família com contraste de 4,5:1 sobre branco. O
 * salmão só aparece em ilustração e em estado de passagem do ponteiro, nunca em
 * texto sobre branco. Ressalva técnica é âmbar (#B9791A), nunca vermelho,
 * porque vermelho é a marca.
 *
 * Preto puro fica no cabeçalho e no rodapé, onde o logo vive; o miolo é branco,
 * com cara de e-commerce. Medida, quantidade, unidade e código saem em
 * JetBrains Mono com tabular-nums; texto corrido NUNCA vai em Mono.
 * ------------------------------------------------------------------------- */

add_action( 'wp_head', function () {
	$fontes = 'https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Source+Sans+3:wght@400;600;700&display=swap';

	echo '<link rel="preconnect" href="https://fonts.googleapis.com">' . "\n";
	echo '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' . "\n";
	echo '<link rel="stylesheet" href="' . esc_url( $fontes ) . '">' . "\n";

	$css = <<<'CSS'
:root{
--cdm-noite:#000000;--cdm-coral:#FC483B;--cdm-salmao:#FA7665;--cdm-vinho:#69030C;
--cdm-rubi:#8A0F18;--cdm-papel:#FFFFFF;--cdm-tinta:#1F1715;--cdm-traco:#E9DCD7;
--cdm-legenda:#6E5F5B;--cdm-ambar:#B9791A;
--cdm-display:"Outfit","Helvetica Neue",Arial,sans-serif;
--cdm-texto:"Source Sans 3",system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;
--cdm-mono:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}
body{
--wp--preset--color--base:#FFFFFF;--wp--preset--color--contrast:#1F1715;
--wp--preset--color--primary:#1F1715;--wp--preset--color--secondary:#6E5F5B;
--wp--preset--font-family--body:var(--cdm-texto);
--wp--preset--font-family--heading:var(--cdm-display);
}
html body{background-color:var(--cdm-papel);color:var(--cdm-tinta);font-family:var(--cdm-texto);font-size:17px;line-height:1.65;-webkit-font-smoothing:antialiased;}
body h1,body h2,body h3,body h4,body h5,body h6{font-family:var(--cdm-display);color:var(--cdm-tinta);line-height:1.2;letter-spacing:-0.01em;}
/* "Clean, cara de e-commerce" (despacho de 11/09): o corpo nao carrega negrito
   de mais. Peso 600 no titulo e 500 na linha de abertura ja separam hierarquia
   num miolo branco; 700 em tudo e o que fazia a pagina parecer manual. */
body h1{font-weight:600;}
body a{color:var(--cdm-rubi);text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:3px;}
body a:hover{color:var(--cdm-coral);}
body code,body kbd,body samp,body pre,body .cdm-num,body .cdm-medida{font-family:var(--cdm-mono);font-variant-numeric:tabular-nums;}
body hr,body .wp-block-separator{border-color:var(--cdm-traco);color:var(--cdm-traco);}
body table{border-collapse:collapse;}
body table th,body table td{border:1px solid var(--cdm-traco);padding:.5rem .7rem;text-align:left;}
body table th{background:var(--cdm-papel);font-family:var(--cdm-display);font-weight:600;}
/* CABECALHO CLARO E RODAPE PRETO (1.2.0). O preto e cor de TEXTO e de detalhe:
   quem vende peca abre a pagina com a peca, nunca com uma faixa escura. O que
   separa o cabecalho do miolo e a linha de 1 px da secao 6 do contrato, e nao
   uma sombra. Sem a regra do tema abaixo, o tema serviria a propria cor. */
.wp-site-blocks > header.wp-block-template-part,body header.wp-block-template-part,body header.wp-block-group,body .wp-block-template-part header{background:var(--cdm-papel);border-bottom:1px solid var(--cdm-traco);box-shadow:none;min-height:5.25rem;}
body header.wp-block-template-part a,body header.wp-block-group a{color:var(--cdm-tinta);}
/* A MARCA E O LOGO DELE, 52 px de altura (despacho de 11/09), numa barra de
   84 px para ele respirar. A altura sai em px e nao em rem de proposito: rem
   segue o tamanho de fonte do leitor, e um logotipo que cresce junto com o texto
   desalinha a barra inteira. Largura auto preserva o 3:2 do arquivo. */
.cdm-marca{display:inline-flex;align-items:center;text-decoration:none;min-height:52px;}
.cdm-marca:hover{text-decoration:none;}
.cdm-marca-logo{display:block;height:52px;width:auto;max-width:100%;}
.cdm-nav ul{display:flex;flex-wrap:wrap;gap:1.4rem;list-style:none;margin:0;padding:0;}
.cdm-nav li{margin:0;}
.cdm-nav a,.cdm-nav .cdm-sem-link{font-family:var(--cdm-texto);font-weight:500;font-size:.95rem;color:var(--cdm-tinta);text-decoration:none;padding-bottom:.15rem;border-bottom:1px solid transparent;}
.cdm-nav a:hover{color:var(--cdm-coral);border-bottom-color:var(--cdm-coral);}
.cdm-nav .cdm-sem-link{color:var(--cdm-legenda);}
.cdm-nav-caixa{position:relative;}
/* O botao do menu so aparece no celular, e so quando ha JavaScript para ele
   comandar (o atributo data-cdm-menu e posto pelo script do rodape). */
.cdm-nav-botao{display:none;align-items:center;gap:.55rem;background:transparent;color:var(--cdm-tinta);border:1px solid var(--cdm-traco);border-radius:2px;padding:.5rem .75rem;font-family:var(--cdm-texto);font-weight:500;font-size:.92rem;line-height:1;cursor:pointer;}
.cdm-nav-botao:hover{border-color:var(--cdm-coral);color:var(--cdm-coral);}
.cdm-nav-tracos{position:relative;display:block;width:1.05rem;height:2px;background:currentColor;border-radius:2px;}
.cdm-nav-tracos::before,.cdm-nav-tracos::after{content:"";position:absolute;left:0;width:100%;height:2px;background:currentColor;border-radius:2px;}
.cdm-nav-tracos::before{top:-.36rem;}
.cdm-nav-tracos::after{top:.36rem;}
.cdm-nav-botao:focus-visible,.cdm-nav a:focus-visible,.cdm-marca:focus-visible,body a:focus-visible{outline:2px solid var(--cdm-coral);outline-offset:3px;}
.cdm-bloco{max-width:52rem;}
.cdm-linha-mestra{font-family:var(--cdm-display);font-size:1.35rem;line-height:1.35;font-weight:500;margin:0 0 .8rem;}
/* A CAMADA DE PROVA (secao 15.2 do contrato). Fonte, data, codigo de documento e
   contagem de banco moram AQUI, nunca no titulo nem no primeiro paragrafo. A
   classe nao e enfeite: e por ela que o portao de voz separa voz de prova pela
   ESTRUTURA, e nao pela vizinhanca da palavra — que e a cicatriz desta ilha de
   11/09/2026, quando uma regua por vizinhanca aprovou "a ficha tecnica do
   silicone acetico mais vendido do Brasil". */
.cdm-prova{margin:2rem 0 0;padding:1rem 0 0;border-top:1px solid var(--cdm-traco);color:var(--cdm-legenda);font-size:.9rem;line-height:1.55;}
.cdm-prova h2,.cdm-prova h3{font-size:1rem;margin:0 0 .4rem;color:var(--cdm-legenda);font-weight:600;}
.cdm-prova p{margin:0 0 .5rem;}
.cdm-prova p:last-child{margin-bottom:0;}
/* Quem faz as pecas, no rodape da home (VOZ.md). */
.cdm-artesa{margin:2.4rem 0 0;padding:1.3rem 1.4rem;border:1px solid var(--cdm-traco);border-radius:3px;}
.cdm-artesa h2{margin:0 0 .5rem;font-size:1.15rem;}
.cdm-artesa p{margin:0 0 .5rem;}
.cdm-artesa p:last-child{margin-bottom:0;}
.cdm-abertura p{margin:0 0 .7rem;}
.cdm-secao{margin:2.4rem 0 0;}
.cdm-secao h2{margin:0 0 .6rem;font-size:1.3rem;}
.cdm-secao h3{margin:1.4rem 0 .4rem;font-size:1.05rem;}
.cdm-cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(19rem,1fr));gap:1rem;margin:1.4rem 0 0;padding:0;list-style:none;}
.cdm-card{background:var(--cdm-papel);border:1px solid var(--cdm-traco);border-radius:3px;padding:1.1rem 1.2rem;display:flex;flex-direction:column;gap:.5rem;margin:0;}
.cdm-card h3{font-family:var(--cdm-display);font-size:1.05rem;margin:0;line-height:1.25;}
.cdm-card p{margin:0;color:var(--cdm-legenda);font-size:.93rem;line-height:1.5;}
.cdm-codigo{font-family:var(--cdm-mono);font-size:.72rem;letter-spacing:.1em;color:var(--cdm-legenda);}
.cdm-acao{margin-top:auto;padding-top:.3rem;}
.cdm-acao a{font-weight:600;text-decoration:none;border-bottom:2px solid var(--cdm-rubi);}
.cdm-sem-link{color:var(--cdm-legenda);}
.cdm-rodape .cdm-sem-link{color:var(--cdm-legenda);}
/* O BOTAO PRINCIPAL e o unico uso do coral por tela (identidade da ilha). */
.cdm-botao{display:inline-block;background:var(--cdm-coral);color:var(--cdm-papel);border:1px solid var(--cdm-coral);border-radius:2px;padding:.7rem 1.2rem;font-family:var(--cdm-texto);font-weight:700;font-size:1rem;text-decoration:none;}
.cdm-botao:hover,.cdm-botao:focus-visible{background:var(--cdm-papel);color:var(--cdm-rubi);}
.cdm-preco{font-family:var(--cdm-display);font-weight:700;color:var(--cdm-coral);font-variant-numeric:tabular-nums;}
/* Estado vazio honesto: a Loja sem peca cadastrada NAO inventa peca. */
.cdm-vazio{border:1px dashed var(--cdm-traco);border-radius:3px;padding:1.6rem 1.4rem;margin:1.4rem 0 0;background:var(--cdm-papel);}
.cdm-vazio h3{margin:0 0 .4rem;font-size:1.1rem;}
.cdm-vazio p{margin:0 0 .6rem;color:var(--cdm-legenda);font-size:.95rem;}
.cdm-vazio p:last-child{margin-bottom:0;}
.cdm-tag{display:inline-block;font-family:var(--cdm-mono);font-size:.68rem;letter-spacing:.08em;text-transform:uppercase;color:var(--cdm-ambar);border:1px solid var(--cdm-ambar);border-radius:2px;padding:.15rem .4rem;}
.cdm-nota{border-left:3px solid var(--cdm-tinta);background:var(--cdm-papel);padding:.85rem 1rem;color:var(--cdm-legenda);font-size:.95rem;margin:1.2rem 0 0;}
.cdm-nota strong{color:var(--cdm-tinta);}
.cdm-lista{margin:.6rem 0 0;padding-left:1.1rem;}
.cdm-lista li{margin:0 0 .45rem;}
.cdm-citacao{border-left:3px solid var(--cdm-traco);background:var(--cdm-papel);margin:1.2rem 0;padding:.9rem 1.1rem;font-size:.95rem;line-height:1.6;}
.cdm-citacao p{margin:0 0 .5rem;}
.cdm-citacao p:last-child{margin-bottom:0;}
.cdm-tabela{margin:1.2rem 0;overflow-x:auto;}
.cdm-quadro{width:100%;margin:1rem 0 0;font-size:.93rem;}
.cdm-quadro td:first-child,.cdm-quadro th:first-child{white-space:nowrap;}
.cdm-quadro .cdm-n{text-align:right;font-family:var(--cdm-mono);font-variant-numeric:tabular-nums;white-space:nowrap;}
/* A TRILHA (16.3). Ela ROLA na horizontal dentro da propria caixa quando nao
   cabe — e o unico jeito de uma trilha longa nao empurrar a pagina inteira e
   fazer o corpo rolar de lado no celular. */
.cdm-trilha{font-family:var(--cdm-texto);font-size:.82rem;line-height:1.5;margin:0 0 1.1rem;max-width:100%;overflow-x:auto;}
.cdm-trilha ol{display:flex;flex-wrap:nowrap;align-items:center;gap:.3rem;list-style:none;margin:0;padding:0;}
.cdm-trilha li{display:flex;align-items:center;gap:.3rem;white-space:nowrap;}
.cdm-trilha li+li::before{content:"\203A";color:var(--cdm-traco);}
.cdm-trilha a{color:var(--cdm-legenda);text-decoration:none;border-bottom:1px solid var(--cdm-traco);}
.cdm-trilha a:hover{color:var(--cdm-coral);border-bottom-color:var(--cdm-coral);}
.cdm-trilha [aria-current="page"]{color:var(--cdm-tinta);font-weight:500;}
/* Degrau de categoria que ainda nao nasceu: texto, nunca link morto, e sem cara
   de promessa — o cartao "em breve" e da mae, nao da trilha. */
.cdm-trilha-espera{color:var(--cdm-legenda);}
.cdm-veja{margin:2.4rem 0 0;padding:1.2rem 0 0;border-top:1px solid var(--cdm-traco);}
.cdm-veja h2{margin:0 0 .5rem;font-size:1.05rem;}
.cdm-veja .cdm-veja-mae{margin:0 0 .6rem;color:var(--cdm-legenda);font-size:.95rem;}
.cdm-veja ul{display:flex;flex-wrap:wrap;gap:.5rem .9rem;list-style:none;margin:0;padding:0;}
.cdm-veja li{margin:0;}
.cdm-veja a{font-family:var(--cdm-texto);font-weight:500;}
.cdm-rodape{background:var(--cdm-noite);color:var(--cdm-papel);padding:2.4rem 1.5rem;margin-top:3.5rem;font-family:var(--cdm-texto);}
.cdm-rodape-interno{max-width:52rem;margin:0 auto;display:flex;flex-direction:column;gap:.7rem;}
.cdm-rodape .cdm-tagline{font-family:var(--cdm-display);font-weight:600;font-size:1.1rem;color:var(--cdm-papel);margin:0;}
.cdm-rodape p{margin:0;font-size:.86rem;line-height:1.55;color:var(--cdm-traco);}
.cdm-rodape a{color:var(--cdm-papel);}
.cdm-rodape a:hover{color:var(--cdm-salmao);}
/* Cinto de seguranca do rodape: o caminho principal e o filtro render_block, que
   troca a template part 'footer' do tema pela desta ilha. Se ele nao pegar, o
   rodape do tema fica visivel acima do nosso — as regras abaixo escondem o
   credito do tema e a template part de rodape que nao seja a nossa. */
.wp-site-blocks > footer.wp-block-template-part .wp-block-group:has(a[href*="wordpress.org"]){display:none;}
body:has(.cdm-rodape) .wp-site-blocks > footer.wp-block-template-part:not(:has(.cdm-rodape)){display:none;}
@media (max-width:600px){
.cdm-linha-mestra{font-size:1.15rem;}
/* No telefone pequeno o logo desce para 44 px: com 52 px ele e o botao do menu
   somam mais que a largura util a 360 px, e o cabecalho quebra em duas linhas. */
.cdm-marca,.cdm-marca-logo{height:44px;min-height:44px;}
}
/* Menu sanfona. 782 px e a largura em que o proprio WordPress considera que a
   tela virou celular; seguir a mesma quebra evita cabecalho meio empilhado.
   Tudo aqui depende de [data-cdm-menu]: sem JavaScript nada disso vale e o menu
   continua sendo a fileira de links, visivel. */
@media (max-width:782px){
.cdm-nav-caixa[data-cdm-menu] .cdm-nav-botao{display:inline-flex;}
.cdm-nav-caixa[data-cdm-menu] .cdm-nav{display:none;position:absolute;right:0;top:calc(100% + .55rem);z-index:60;min-width:13rem;background:var(--cdm-papel);border:1px solid var(--cdm-traco);border-radius:3px;box-shadow:0 12px 32px rgba(31,23,21,.12);padding:.35rem 0;}
.cdm-nav-caixa[data-cdm-menu][data-cdm-aberto="1"] .cdm-nav{display:block;}
.cdm-nav-caixa[data-cdm-menu] .cdm-nav ul,.cdm-nav-caixa[data-cdm-menu] .cdm-nav li{display:block;}
.cdm-nav-caixa[data-cdm-menu] .cdm-nav a,.cdm-nav-caixa[data-cdm-menu] .cdm-nav .cdm-sem-link{display:block;padding:.65rem 1.05rem;font-size:1rem;border-bottom:0;}
.cdm-nav-caixa[data-cdm-menu] .cdm-nav a:hover{color:var(--cdm-coral);}
}
CSS;

	echo '<style id="cdm-casca">' . $css . '</style>' . "\n";
}, 20 );

/* ---------------------------------------------------------------------------
 * 3b. O comando do menu sanfona
 *
 * O script sai no wp_footer, NUNCA dentro do retorno de um shortcode. É a regra
 * da seção 8 do ARQUIPELAGO.md, nascida do defeito de 08/09/2026 na Aquametria:
 * o WordPress roda os filtros de texto do conteúdo sobre o que o shortcode
 * devolve, cada E-comercial vira entidade numérica e o JavaScript inteiro morre
 * com erro de sintaxe. Aqui ele não passa por filtro nenhum.
 *
 * O script não desenha menu: só assume o comando do que o PHP já serviu. A
 * primeira coisa que faz é pôr data-cdm-menu na caixa, e é esse atributo que
 * liga as regras de CSS do celular — ou seja, o menu só se fecha depois que
 * existe alguém para reabri-lo.
 * ------------------------------------------------------------------------- */

add_action( 'wp_footer', function () {
	$js = <<<'JS'
(function () {
	var caixas = document.querySelectorAll('.cdm-nav-caixa');
	if (!caixas.length) { return; }

	Array.prototype.forEach.call(caixas, function (caixa) {
		var botao = caixa.querySelector('.cdm-nav-botao');
		var lista = caixa.querySelector('.cdm-nav');
		if (!botao || !lista) { return; }

		/* A partir daqui o CSS do celular vale: ha quem reabra o menu. */
		caixa.setAttribute('data-cdm-menu', '1');

		function aberto() {
			return caixa.getAttribute('data-cdm-aberto') === '1';
		}
		function estado(abrir) {
			caixa.setAttribute('data-cdm-aberto', abrir ? '1' : '0');
			botao.setAttribute('aria-expanded', abrir ? 'true' : 'false');
		}
		estado(false);

		botao.addEventListener('click', function (ev) {
			ev.preventDefault();
			estado(!aberto());
		});

		/* Escape fecha e devolve o foco ao botao: quem abriu pelo teclado nao
		   pode ficar com o foco preso num menu que sumiu. */
		caixa.addEventListener('keydown', function (ev) {
			if (!aberto()) { return; }
			if (ev.key === 'Escape' || ev.key === 'Esc') {
				estado(false);
				botao.focus();
			}
		});

		document.addEventListener('click', function (ev) {
			if (aberto() && !caixa.contains(ev.target)) { estado(false); }
		});

		/* Girar o telefone ou alargar a janela passa da faixa do celular: o menu
		   volta a ser fileira de links e nao pode continuar marcado como aberto,
		   senao o aria-expanded mente para o leitor de tela. */
		window.addEventListener('resize', function () {
			if (aberto() && window.innerWidth > 782) { estado(false); }
		});
	});
})();
JS;

	echo '<script id="cdm-casca-menu">' . $js . '</script>' . "\n";
}, 25 );

/* ---------------------------------------------------------------------------
 * 4. Números, listagens e conteúdo das páginas
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_casca_numeros' ) ) {
/**
 * Números do banco desta ilha, para a tela.
 *
 * Ordem das vias, e ela importa: primeiro o banco publicado nas options pelo
 * Sync (número vivo), depois o instantâneo medido em 10/09/2026 pelo bloco 3 e
 * conferido por ferramentas/validar-banco.py. O instantâneo está aqui porque
 * hoje os itens de `dados` do manifest estão com publicar=false — são pesquisa,
 * não página — e uma página que promete número não pode ficar em branco
 * esperando. No dia em que o banco virar dado publicado, a via viva assume.
 *
 * ferramentas/teste-casca.php recalcula cada um destes números a partir dos
 * arquivos commitados e reprova se a tela e o repositório se separarem.
 */
function cdm_casca_numeros() {
	$n = array(
		'medido_em'          => '2026-09-11',
		'materiais_cola'     => 5,
		'materiais_rejunte'  => 5,
		'categorias_do_guia' => 6,
		'celulas_matriz'     => 18,
		'celulas_rejunte'    => 9,
		'celulas_com_saida'  => 16,
		'celulas_sem_saida'  => 2,
		'bases'              => 9,
		'ambientes'          => 5,
		'esperando_link'     => 10,
		'sem_imagem'         => 10,
		'pecas_na_loja'      => 0,
	);

	/* Uma linha por categoria que ja tem arquivo de banco. E esta lista que impede o
	   zero digitado de voltar: categoria que ganha arquivo entra aqui, e o teste reprova
	   se ela e os arquivos de dados/ se separarem. */
	$bancos = array(
		'materiais-colas'    => 'materiais_cola',
		'materiais-rejuntes' => 'materiais_rejunte',
	);

	$link_vivo = 0;
	$img_viva  = 0;
	$lidos     = 0;
	foreach ( $bancos as $arquivo => $chave ) {
		$banco = get_option( 'clubedomosaico_dados_' . $arquivo );
		if ( ! is_array( $banco ) || ! isset( $banco['materiais'] ) || ! is_array( $banco['materiais'] ) ) {
			continue;
		}
		$lidos++;
		$n[ $chave ] = count( $banco['materiais'] );
		if ( isset( $banco['afiliado']['itens_esperando_link'] ) ) {
			$link_vivo += (int) $banco['afiliado']['itens_esperando_link'];
		}
		if ( isset( $banco['imagens']['itens_sem_imagem'] ) ) {
			$img_viva += (int) $banco['imagens']['itens_sem_imagem'];
		}
	}

	/* Os totais da ilha so assumem a via viva quando TODOS os bancos chegaram. Somar
	   metade das categorias daria um total menor e com cara de verdadeiro — melhor o
	   instantaneo inteiro, que ao menos diz a data em que foi medido. */
	if ( $lidos === count( $bancos ) ) {
		$n['esperando_link'] = $link_vivo;
		$n['sem_imagem']     = $img_viva;
	}

	/* O TOTAL DE ITENS DA ILHA, SOMADO — nunca digitado, e nunca confundido com o
	   total de UMA categoria. Foi exatamente essa confusão que pôs no ar a frase
	   "hoje 10 dos 5 itens esperam link": os dois números estavam certos sozinhos
	   (10 itens esperando link no banco inteiro, 5 adesivos na categoria cola) e a
	   frase que os juntou era impossível. Denominador de frase sobre a ilha é a
	   soma das categorias; o de frase sobre uma categoria é aquela categoria. */
	$n['itens_no_banco'] = 0;
	foreach ( $bancos as $chave ) {
		$n['itens_no_banco'] += (int) $n[ $chave ];
	}

	/* A Loja conta peça de verdade, nunca estimativa: enquanto o CPT do bloco 4d
	   não existir, o número é zero e a página diz isso com todas as letras. */
	if ( function_exists( 'post_type_exists' ) && post_type_exists( 'peca' ) ) {
		$publicadas       = get_posts( array(
			'post_type'   => 'peca',
			'post_status' => 'publish',
			'numberposts' => 50,
		) );
		$n['pecas_na_loja'] = is_array( $publicadas ) ? count( $publicadas ) : 0;
	}

	return apply_filters( 'cdm_numeros', $n );
}
}

if ( ! function_exists( 'cdm_casca_data_br' ) ) {
/** Data na tela sai como o leitor brasileiro escreve; ISO fica no repositório. */
function cdm_casca_data_br( $iso ) {
	$partes = explode( '-', (string) $iso );
	if ( 3 !== count( $partes ) ) {
		return (string) $iso;
	}
	return $partes[2] . '/' . $partes[1] . '/' . $partes[0];
}
}

if ( ! function_exists( 'cdm_casca_num' ) ) {
/** Número na tela sai sempre em monoespaçada com tabular-nums (identidade). */
function cdm_casca_num( $valor ) {
	return '<span class="cdm-num">' . esc_html( number_format_i18n( (float) $valor ) ) . '</span>';
}
}

if ( ! function_exists( 'cdm_casca_cards_ferramentas_html' ) ) {
function cdm_casca_cards_ferramentas_html() {
	$html = '<ul class="cdm-cards">';
	foreach ( cdm_casca_ferramentas() as $f ) {
		$publicada = ( isset( $f['estado'] ) && 'publicada' === $f['estado'] );
		$html     .= '<li class="cdm-card">';
		$html     .= '<span class="cdm-codigo">' . esc_html( $f['codigo'] ) . '</span>';
		$html     .= '<h3>' . esc_html( $f['titulo'] ) . '</h3>';
		$html     .= '<p>' . esc_html( $f['resumo'] ) . '</p>';
		$html     .= '<span class="cdm-acao">';
		$url = $publicada ? cdm_casca_url_se_existir( $f['slug'] ) : '';
		if ( '' !== $url ) {
			$html .= '<a href="' . esc_url( $url ) . '">Abrir ferramenta</a>';
		} else {
			/* A ferramenta pode ter se anunciado publicada e a página ainda não
			   existir (Sync atrasado, slug tomado). Melhor o selo honesto que um
			   link que devolve 404. */
			$html .= '<span class="cdm-tag">Em construção</span>';
		}
		$html .= '</span></li>';
	}
	$html .= '</ul>';

	return $html;
}
}

if ( ! function_exists( 'cdm_casca_cards_guia_html' ) ) {
/**
 * As seis categorias do Guia.
 *
 * Categoria sem ficha publicada NÃO vira link — vira cartão com o estado
 * escrito. E o estado não é "em breve" genérico: quando a categoria já tem
 * banco, o cartão diz quantos itens ela tem, porque é esse número que separa
 * uma promessa de um trabalho feito.
 */
function cdm_casca_cards_guia_html() {
	$html = '<ul class="cdm-cards">';
	foreach ( cdm_casca_categorias_do_guia() as $c ) {
		$html .= '<li class="cdm-card">';
		$html .= '<span class="cdm-codigo">' . esc_html( $c['codigo'] ) . '</span>';
		$html .= '<h3>' . esc_html( $c['titulo'] ) . '</h3>';
		$html .= '<p>' . esc_html( $c['resumo'] ) . '</p>';
		$html .= '<span class="cdm-acao">';
		$url = cdm_casca_url_se_existir( $c['slug'] );
		if ( '' !== $url ) {
			$html .= '<a href="' . esc_url( $url ) . '">Abrir a ficha</a>';
		} else {
			/* 16.5, ao pé da letra: enquanto a categoria não existe, o cartão não
			   é link e diz "em breve" SEM contagem de banco. Até 1.2.0 ele dizia
			   "5 no banco, ficha em construção" — número certo, contado do
			   arquivo, e ainda assim promessa com número colada num cartão que
			   não abre. O número não sumiu do site: ele mora na camada de prova
			   do Guia e na página Como sabemos (15.2), que é onde quem quer
			   conferir vai conferir. O campo `no_banco` continua existindo e
			   continua sendo cobrado contra o arquivo pelo teste — o que mudou é
			   que ele deixou de ir para a TELA deste cartão. */
			$html .= '<span class="cdm-tag">Em breve</span>';
		}
		$html .= '</span></li>';
	}
	$html .= '</ul>';

	return $html;
}
}

if ( ! function_exists( 'cdm_casca_tutoriais_html' ) ) {
/**
 * A listagem de tutoriais, para a home e para a Escola.
 *
 * Sai '' quando não há tutorial publicado — listagem vazia com título em cima é
 * promessa não cumprida, e quem chama só imprime a seção se receber HTML.
 */
function cdm_casca_tutoriais_html() {
	$itens = array();
	foreach ( cdm_casca_tutoriais() as $t ) {
		$url = cdm_casca_url_se_existir( isset( $t['slug'] ) ? $t['slug'] : '' );
		if ( '' === $url ) {
			continue;
		}
		$itens[] = '<li class="cdm-card">'
			. '<h3><a href="' . esc_url( $url ) . '">' . esc_html( $t['titulo'] ) . '</a></h3>'
			. '<p>' . esc_html( isset( $t['resumo'] ) ? $t['resumo'] : '' ) . '</p>'
			. '</li>';
	}

	if ( ! $itens ) {
		return '';
	}

	return '<ul class="cdm-cards">' . implode( '', $itens ) . '</ul>';
}
}

if ( ! function_exists( 'cdm_casca_vitrine_de_pecas_html' ) ) {
/**
 * As peças publicadas pela artesã, quando existirem.
 *
 * Enquanto o CPT `peca` do bloco 4d não existir, isto devolve '' e quem chama
 * imprime o estado vazio honesto. NUNCA devolve peça de exemplo: peça inventada
 * é proibida nesta ilha por decisão escrita no PROMPT.md, e um "exemplo" que
 * ninguém pode comprar é exatamente isso.
 */
function cdm_casca_vitrine_de_pecas_html( $quantas = 8 ) {
	if ( ! function_exists( 'post_type_exists' ) || ! post_type_exists( 'peca' ) ) {
		return '';
	}

	$pecas = get_posts( array(
		'post_type'   => 'peca',
		'post_status' => 'publish',
		'numberposts' => (int) $quantas,
	) );
	if ( ! $pecas ) {
		return '';
	}

	$html = '<ul class="cdm-cards">';
	foreach ( $pecas as $p ) {
		$preco = get_post_meta( $p->ID, '_cdm_preco', true );
		$html .= '<li class="cdm-card">';
		$html .= '<h3><a href="' . esc_url( get_permalink( $p ) ) . '">' . esc_html( $p->post_title ) . '</a></h3>';
		if ( '' !== $preco ) {
			$html .= '<p><span class="cdm-preco">R$ ' . esc_html( number_format_i18n( (float) $preco, 2 ) ) . '</span></p>';
		}
		$html .= '</li>';
	}
	$html .= '</ul>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 3d. A ÁRVORE — trilha, BreadcrumbList e cluster "Veja também"
 *
 * Seção 16 do ARQUIPELAGO.md. O mapa de quem é mãe de quem está escrito em
 * ARVORE.md; aqui ele vira código, e `ferramentas/teste-casca.php` confere que
 * as duas metades dizem a mesma coisa — documento e código mantidos à mão em
 * dois lugares divergem em silêncio (seção 8).
 *
 * QUATRO DECISÕES, e nenhuma é enfeite:
 *
 *   1. NADA AQUI CRIA URL. As dez páginas de nível 2 da árvore esperam a 16.5,
 *      que é portão de dado. Trilha e cluster cabem antes porque só usam
 *      endereço que já existe.
 *   2. O DEGRAU SEM PÁGINA SAI EM TEXTO, nunca como link morto. Nesta ilha os
 *      três degraus de nível 1 já existem, então hoje nenhum sai em texto — a
 *      via existe para o dia em que uma categoria aparecer na trilha antes de
 *      ter página, que é o estado normal das outras duas ilhas.
 *   3. O JSON-LD NÃO CARREGA DEGRAU SEM ENDEREÇO. Um ListItem intermediário sem
 *      `item` invalida o BreadcrumbList inteiro, e lista inválida é lista
 *      ignorada: o schema "mais completo" publicaria MENOS com cara de publicar
 *      mais.
 *   4. AS IRMÃS SÃO DERIVADAS, NUNCA DIGITADAS. Lista escrita à mão envelhece no
 *      dia da próxima página — é a cicatriz do número de tela digitado (seção
 *      8). Elas saem do mesmo mapa que a trilha usa, e página que não existe
 *      publicada não entra: irmã é link, e link morto não é cluster.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_casca_arvore' ) ) {
/**
 * O mapa da árvore, e a ÚNICA fonte dele nesta casca.
 *
 *   'nivel'  => 1 | 2 | 3, ou 0 para as páginas que a 16.1 admite na raiz
 *   'mae'    => o caminho da mãe, '' quando a mãe é a home
 *   'rotulo' => o degrau na tela, no vocabulário do VOZ.md
 *
 * A home não está aqui de propósito: 16.3 diz que ela não tem trilha, e
 * declará-la seria abrir a porta para uma trilha "Início › Início".
 */
function cdm_casca_arvore() {
	$mapa = array(
		/* Nível 1 — os três motores da ilha, e os três já são página. */
		'loja'                    => array( 'nivel' => 1, 'mae' => '', 'rotulo' => 'Loja' ),
		'materiais'               => array( 'nivel' => 1, 'mae' => '', 'rotulo' => 'Materiais' ),
		'como-fazer'              => array( 'nivel' => 1, 'mae' => '', 'rotulo' => 'Como fazer' ),

		/* Nível 2 — a única no ar é a camada de prova; as outras esperam a 16.5. */
		'materiais/como-sabemos'  => array( 'nivel' => 2, 'mae' => 'materiais', 'rotulo' => 'Como sabemos' ),

		/* Fora da árvore, na raiz, exatamente a lista que a 16.1 admite. */
		'sobre'                   => array( 'nivel' => 0, 'mae' => '', 'rotulo' => 'Sobre' ),
		'contato'                 => array( 'nivel' => 0, 'mae' => '', 'rotulo' => 'Contato' ),
		'divulgacao-de-afiliados' => array( 'nivel' => 0, 'mae' => '', 'rotulo' => 'Divulgação de afiliados' ),
		'privacidade'             => array( 'nivel' => 0, 'mae' => '', 'rotulo' => 'Privacidade' ),
	);

	/* As categorias do Guia entram pelo MESMO registro que desenha os cartões,
	   nunca por uma segunda lista: categoria que nascer lá aparece aqui sozinha,
	   e é assim que o mapa não envelhece. */
	foreach ( cdm_casca_categorias_do_guia() as $c ) {
		if ( empty( $c['slug'] ) || isset( $mapa[ $c['slug'] ] ) ) {
			continue;
		}
		$mapa[ $c['slug'] ] = array( 'nivel' => 2, 'mae' => 'materiais', 'rotulo' => $c['titulo'] );
	}

	/* As ferramentas, nível 3 com mãe /materiais/ direto — dois níveis em vez de
	   três, estado de transição declarado na seção 2 do ARVORE.md. Nenhuma tem
	   página hoje; isto existe para a trilha já nascer certa no dia do bloco 4. */
	foreach ( cdm_casca_ferramentas() as $f ) {
		if ( empty( $f['slug'] ) || isset( $mapa[ $f['slug'] ] ) ) {
			continue;
		}
		$mapa[ $f['slug'] ] = array( 'nivel' => 3, 'mae' => 'materiais', 'rotulo' => $f['titulo'] );
	}

	/* Os tutoriais se registram pelo filtro do snippet de cada um, como na
	   listagem da Escola. Mãe /como-fazer/ enquanto não houver categoria. */
	foreach ( cdm_casca_tutoriais() as $t ) {
		if ( empty( $t['slug'] ) || isset( $mapa[ $t['slug'] ] ) ) {
			continue;
		}
		$mapa[ $t['slug'] ] = array( 'nivel' => 3, 'mae' => 'como-fazer', 'rotulo' => $t['titulo'] );
	}

	return apply_filters( 'cdm_arvore', $mapa );
}
}

if ( ! function_exists( 'cdm_casca_slug_atual' ) ) {
/**
 * O CAMINHO da página que está sendo servida — 'materiais/como-sabemos', não
 * 'como-sabemos'. Devolve '' na home e em tudo que não for página singular, e
 * quem chama não publica trilha nenhuma, que é melhor que trilha inventada.
 *
 * O WordPress guarda só o último nível em post_name; o caminho se remonta pela
 * definição de páginas, que é o mesmo lugar de onde a página nasceu. O teste
 * cobra que nenhum último nível se repita nessa definição — sem isso o caminho
 * seria adivinhação.
 */
function cdm_casca_slug_atual() {
	if ( function_exists( 'is_front_page' ) && is_front_page() ) {
		return '';
	}
	if ( ! function_exists( 'is_singular' ) || ! is_singular() ) {
		return '';
	}
	$post = function_exists( 'get_post' ) ? get_post() : null;
	if ( ! $post || empty( $post->post_name ) ) {
		return '';
	}
	$nome = (string) $post->post_name;

	foreach ( cdm_casca_definicao_paginas() as $caminho => $def ) {
		if ( cdm_casca_slug_final( $caminho ) === $nome ) {
			return $caminho;
		}
	}

	return $nome;
}
}

if ( ! function_exists( 'cdm_casca_degraus' ) ) {
/**
 * Os degraus da trilha, do topo até a página atual. Cada degrau:
 *   array( 'rotulo' => ..., 'url' => '' quando a página ainda não existe )
 * O último é sempre a página atual e nunca leva URL — é onde a pessoa já está.
 */
function cdm_casca_degraus( $slug ) {
	$mapa = cdm_casca_arvore();
	$slug = trim( (string) $slug, '/' );
	if ( '' === $slug || ! isset( $mapa[ $slug ] ) ) {
		return array();
	}

	/* Sobe pela mãe até a raiz. O limite existe para um 'mae' escrito em
	   círculo por engano não travar a página inteira; o teste cobra que ele
	   nunca seja alcançado. */
	$acima = array();
	$passo = $mapa[ $slug ]['mae'];
	$giros = 0;
	while ( '' !== $passo && isset( $mapa[ $passo ] ) && $giros < 8 ) {
		array_unshift( $acima, $passo );
		$passo = $mapa[ $passo ]['mae'];
		$giros++;
	}

	$degraus = array( array( 'rotulo' => 'Início', 'url' => home_url( '/' ) ) );
	foreach ( $acima as $caminho ) {
		$degraus[] = array(
			'rotulo' => $mapa[ $caminho ]['rotulo'],
			'url'    => cdm_casca_url_se_existir( $caminho ),
		);
	}
	$degraus[] = array( 'rotulo' => $mapa[ $slug ]['rotulo'], 'url' => '' );

	return $degraus;
}
}

if ( ! function_exists( 'cdm_casca_trilha_html' ) ) {
/* `<nav>` com `<ol>`, porque é navegação e é ordenada. Degrau sem página sai
   como texto; o atual leva aria-current. */
function cdm_casca_trilha_html( $slug ) {
	$degraus = cdm_casca_degraus( $slug );
	if ( count( $degraus ) < 2 ) {
		return '';
	}

	$ultimo = count( $degraus ) - 1;
	$html   = '<nav class="cdm-trilha" aria-label="Você está em"><ol>';
	foreach ( $degraus as $i => $d ) {
		$html .= '<li>';
		if ( $i === $ultimo ) {
			$html .= '<span aria-current="page">' . esc_html( $d['rotulo'] ) . '</span>';
		} elseif ( '' !== $d['url'] ) {
			$html .= '<a href="' . esc_url( $d['url'] ) . '">' . esc_html( $d['rotulo'] ) . '</a>';
		} else {
			$html .= '<span class="cdm-trilha-espera">' . esc_html( $d['rotulo'] ) . '</span>';
		}
		$html .= '</li>';
	}
	$html .= '</ol></nav>';

	return $html;
}
}

if ( ! function_exists( 'cdm_casca_trilha_jsonld' ) ) {
/* O BreadcrumbList: os degraus COM endereço, mais a página atual. Ver decisão 3
   no topo desta seção. */
function cdm_casca_trilha_jsonld( $slug ) {
	$degraus = cdm_casca_degraus( $slug );
	if ( count( $degraus ) < 2 ) {
		return array();
	}

	$atual = array_pop( $degraus );
	$itens = array();
	$pos   = 0;

	foreach ( $degraus as $d ) {
		if ( '' === $d['url'] ) {
			continue;
		}
		$pos++;
		$itens[] = array(
			'@type'    => 'ListItem',
			'position' => $pos,
			'name'     => $d['rotulo'],
			'item'     => $d['url'],
		);
	}

	$pos++;
	$ultimo    = array( '@type' => 'ListItem', 'position' => $pos, 'name' => $atual['rotulo'] );
	$url_atual = cdm_casca_url_se_existir( $slug );
	if ( '' !== $url_atual ) {
		$ultimo['item'] = $url_atual;
	}
	$itens[] = $ultimo;

	if ( count( $itens ) < 2 ) {
		return array();
	}

	return array(
		'@context'        => 'https://schema.org',
		'@type'           => 'BreadcrumbList',
		'itemListElement' => $itens,
	);
}
}

if ( ! function_exists( 'cdm_casca_irmas' ) ) {
/**
 * As irmãs de uma página: MESMA MÃE, no ar, no máximo quatro (16.4c).
 *
 * Derivadas do mapa, nunca digitadas. A ordem é a do mapa, que é a ordem em que
 * a ilha apresenta os motores — Loja na frente, porque é o caminho que termina
 * em compra (seção 9).
 */
function cdm_casca_irmas( $slug ) {
	$mapa = cdm_casca_arvore();
	$slug = trim( (string) $slug, '/' );
	if ( '' === $slug || ! isset( $mapa[ $slug ] ) ) {
		return array();
	}
	/* Página da raiz não tem irmã: ela não está na árvore, está ao lado dela. */
	if ( 0 === (int) $mapa[ $slug ]['nivel'] ) {
		return array();
	}

	$minha = $mapa[ $slug ]['mae'];
	$irmas = array();
	foreach ( $mapa as $caminho => $def ) {
		if ( $caminho === $slug || $def['mae'] !== $minha || 0 === (int) $def['nivel'] ) {
			continue;
		}
		$url = cdm_casca_url_se_existir( $caminho );
		if ( '' === $url ) {
			continue;
		}
		$irmas[] = array( 'slug' => $caminho, 'rotulo' => $def['rotulo'], 'url' => $url );
	}

	return array_slice( $irmas, 0, 4 );
}
}

if ( ! function_exists( 'cdm_casca_veja_tambem_html' ) ) {
/**
 * O cluster: a frase que linka a mãe (16.4b) e as irmãs (16.4c).
 *
 * Sai '' com menos de duas irmãs no ar. É a mesma regra da listagem de
 * tutoriais: bloco com um item só não é cluster, é enfeite — e inventar a
 * segunda irmã seria publicar link morto.
 */
function cdm_casca_veja_tambem_html( $slug ) {
	$irmas = cdm_casca_irmas( $slug );
	if ( count( $irmas ) < 2 ) {
		return '';
	}

	$mapa = cdm_casca_arvore();
	$html = '<nav class="cdm-veja" aria-label="Veja também"><h2>Veja também</h2>';

	/* A frase da mãe só existe quando a mãe é página de conteúdo. No nível 1 a
	   mãe é a home, que já é link pela marca e pelo primeiro degrau da trilha —
	   uma frase apontando para ela seria ruído (ARVORE.md, seção 6). */
	$mae     = $mapa[ $slug ]['mae'];
	$url_mae = ( '' !== $mae ) ? cdm_casca_url_se_existir( $mae ) : '';
	if ( '' !== $url_mae && isset( $mapa[ $mae ] ) ) {
		$html .= '<p class="cdm-veja-mae">Esta página faz parte de <a href="' . esc_url( $url_mae ) . '">'
			. esc_html( $mapa[ $mae ]['rotulo'] ) . '</a>.</p>';
	} else {
		$html .= '<p class="cdm-veja-mae">Os outros dois lados do Clube do Mosaico:</p>';
	}

	$html .= '<ul>';
	foreach ( $irmas as $irma ) {
		$html .= '<li><a href="' . esc_url( $irma['url'] ) . '">' . esc_html( $irma['rotulo'] ) . '</a></li>';
	}
	$html .= '</ul></nav>';

	return $html;
}
}

if ( ! function_exists( 'cdm_casca_trilha_impressa' ) ) {
/* Uma trilha por página. O `static` vale numa requisição, que é uma página —
   e é por isso que a bancada roda UM PROCESSO POR PÁGINA (seção 8). */
function cdm_casca_trilha_impressa( $marcar = false ) {
	static $impressa = false;
	if ( $marcar ) {
		$impressa = true;
	}
	return $impressa;
}
}

/* A trilha entra no lugar do bloco core/post-title, ANTES do H1 — é o "abaixo
   do header" da 16.3 num tema de blocos. */
add_filter( 'render_block', function ( $conteudo, $bloco ) {
	if ( is_admin() || ( defined( 'REST_REQUEST' ) && REST_REQUEST ) ) {
		return $conteudo;
	}
	if ( 'core/post-title' !== ( isset( $bloco['blockName'] ) ? $bloco['blockName'] : '' ) ) {
		return $conteudo;
	}
	if ( cdm_casca_trilha_impressa() ) {
		return $conteudo;
	}
	$trilha = cdm_casca_trilha_html( cdm_casca_slug_atual() );
	if ( '' === $trilha ) {
		return $conteudo;
	}
	cdm_casca_trilha_impressa( true );

	return $trilha . $conteudo;
}, 10, 2 );

/* Cinto de segurança: sem bloco core/post-title na página, a trilha sai no topo
   do conteúdo. Prioridade 9 para ficar acima do que o conteúdo trouxer. */
add_filter( 'the_content', function ( $html ) {
	if ( is_admin() || ! is_singular() || cdm_casca_trilha_impressa() ) {
		return $html;
	}
	$trilha = cdm_casca_trilha_html( cdm_casca_slug_atual() );
	if ( '' === $trilha ) {
		return $html;
	}
	cdm_casca_trilha_impressa( true );

	return $trilha . $html;
}, 9 );

add_filter( 'the_content', function ( $html ) {
	if ( is_admin() || ! is_singular() ) {
		return $html;
	}

	return $html . cdm_casca_veja_tambem_html( cdm_casca_slug_atual() );
}, 20 );

add_action( 'wp_head', function () {
	$dados = cdm_casca_trilha_jsonld( cdm_casca_slug_atual() );
	if ( ! $dados ) {
		return;
	}
	echo '<script type="application/ld+json" id="cdm-trilha-jsonld">'
		. wp_json_encode( $dados ) . '</script>' . "\n";
}, 7 );

/**
 * A HOME, pelo molde LOJA do VOZ.md (seção 15.3 do contrato).
 *
 * O que saiu daqui em 1.2.0, e por quê: a home abria com um manifesto de três
 * parágrafos sobre o método da ilha, e o terceiro era a ficha técnica de um
 * silicone, com o código do documento e a lista de superfícies proibidas. As
 * duas primeiras frases estão LITERALMENTE na lista de "Proibidas" do VOZ.md —
 * não é coincidência: foi o texto que ela foi escrita para proibir. Quem chega
 * aqui está escolhendo presente num domingo à tarde ou tem um vaso de barro na
 * mão, e nenhum dos dois veio ler o método.
 *
 * O número e a fonte não sumiram do site: mudaram de lugar. Eles moram na
 * camada de prova (seção 15.2) das páginas do Guia, onde quem quiser conferir
 * vai conferir. Uma home é uma vitrine, não a página de metodologia.
 */
add_shortcode( 'cdm_home', function () {
	$html  = '<div class="cdm-bloco">';
	$html .= '<div class="cdm-abertura">';
	$html .= '<p class="cdm-linha-mestra">Mosaico feito à mão, uma peça por vez.</p>';
	$html .= '<p>Vaso, cachepô, quadro, espelho, colar: cada peça é cortada e assentada uma de cada vez, aqui no ateliê. Como nenhuma é feita em série, quando uma sai não existe outra igual.</p>';
	$html .= '<p>E se você quer fazer a sua, a gente ajuda a escolher o material certo para a peça que você tem na mão.</p>';
	$html .= '</div>';

	$html .= '<div class="cdm-secao">';
	$html .= '<h2>Peças do ateliê</h2>';
	$vitrine = cdm_casca_vitrine_de_pecas_html( 8 );
	if ( '' !== $vitrine ) {
		$html .= '<p>Cada peça é feita uma a uma. Se gostou, avisa a gente — a disponibilidade muda rápido.</p>';
		$html .= $vitrine;
	} else {
		$html .= '<div class="cdm-vazio">';
		$html .= '<h3>A vitrine abre em breve</h3>';
		$html .= '<p>A artesã fotografa e cadastra cada peça ela mesma, e a primeira ainda não subiu. Não vamos pôr foto de catálogo aqui só para o espaço não ficar vazio: o que aparecer nesta página vai ser uma peça de verdade, que dá para levar para casa.</p>';
		$html .= '<p>Veio fazer a sua? O caminho é por aqui: ' . cdm_casca_link_html( 'materiais', 'escolher o material' ) . '.</p>';
		$html .= '</div>';
	}
	$html .= '</div>';

	$html .= '<div class="cdm-secao">';
	$html .= '<h2>Vai fazer o seu? A gente ajuda a escolher o material</h2>';
	$html .= '<p>Vaso de barro? Vai de cola branca por dentro de casa. Se ele for pra varanda, é outra cola — a gente te mostra qual, e por quê.</p>';
	$html .= '<p>São seis prateleiras, e em todas a pergunta é a mesma: sobre o que você vai colar, e onde a peça vai ficar.</p>';
	$html .= cdm_casca_cards_guia_html();
	$html .= '</div>';

	$html .= '<div class="cdm-secao">';
	$html .= '<h2>Duas contas que a gente está deixando prontas</h2>';
	$html .= '<p>Uma diz qual cola e qual rejunte servem na sua base; a outra, quantas pastilhas e quanto rejunte a sua peça vai consumir — para você não voltar à loja no meio do trabalho.</p>';
	$html .= cdm_casca_cards_ferramentas_html();
	$html .= '</div>';

	$tutoriais = cdm_casca_tutoriais_html();
	if ( '' !== $tutoriais ) {
		$html .= '<div class="cdm-secao">';
		$html .= '<h2>Como fazer</h2>';
		$html .= '<p>Cada passo a passo termina com a lista do que comprar — e, para quem prefere a peça pronta, o caminho da Loja.</p>';
		$html .= $tutoriais;
		$html .= '</div>';
	}

	/* A artesã fecha a home (VOZ.md). Nome, foto e redes entram no dia em que ela
	   autorizar: o bloco nasce pronto e sem inventar nenhum dos três. */
	$html .= '<div class="cdm-artesa">';
	$html .= '<h2>Quem faz</h2>';
	$html .= '<p>Uma artesã, à mão, uma peça de cada vez. É ela quem corta, assenta, rejunta, fotografa e cadastra cada peça aqui — não tem ninguém no meio.</p>';
	$html .= '<p>O nome, o rosto e as redes dela entram nesta página assim que ela autorizar. Até lá fica escrito assim, sem foto de banco de imagens e sem nome de fantasia.</p>';
	$html .= '</div>';
	$html .= '</div>';

	return $html;
} );

add_shortcode( 'cdm_loja', function () {
	$html  = '<div class="cdm-bloco">';
	$html .= '<p class="cdm-linha-mestra">Peças de mosaico feitas à mão, uma a uma: vasos, cachepôs, quadros, espelhos e colares.</p>';
	$html .= '<p>Não é produção em série e não é revenda. Cada peça sai do ateliê de uma artesã, com a técnica e a base declaradas na ficha, e a foto é a da peça que você vai receber — não uma foto de catálogo.</p>';

	$vitrine = cdm_casca_vitrine_de_pecas_html( 24 );
	if ( '' !== $vitrine ) {
		$html .= $vitrine;
	} else {
		$html .= '<div class="cdm-vazio">';
		$html .= '<h3>Em breve, e sem peça de mentira até lá</h3>';
		$html .= '<p>A área de cadastro da artesã está sendo construída. Enquanto ela não publica a primeira peça, esta página fica assim: sem foto de banco de imagens, sem "produto exemplo" e sem lista de espera que ninguém vai atender.</p>';
		$html .= '<p>Quando abrir, cada peça terá medidas, peso, base, técnica, prazo e um botão para verificar disponibilidade direto com quem fez.</p>';
		$html .= '</div>';
	}

	$html .= '<div class="cdm-secao">';
	$html .= '<h2>Como a compra vai funcionar</h2>';
	$html .= '<ul class="cdm-lista">';
	$html .= '<li><strong>Cada peça é única.</strong> Quando uma é vendida, ela sai do ar — não existe "mais uma igual". Peça parecida é outra peça, com outra ficha e outra foto.</li>';
	$html .= '<li><strong>Você fala com quem fez.</strong> O botão principal da página da peça é <em>Verificar disponibilidade</em>: você deixa nome e WhatsApp, e a artesã responde confirmando prazo e forma de envio.</li>';
	$html .= '<li><strong>Pronta entrega ou sob encomenda</strong>, sempre escrito na ficha, com o prazo em dias. Peça sob encomenda é feita para você e o prazo é o do trabalho, não o do correio.</li>';
	$html .= '<li class="cdm-nao-fazemos"><strong>Nada de contagem regressiva nem "últimas unidades".</strong> Se está no ar, existe; se foi vendida, some. Pressa inventada não é parte do trabalho dela.</li>';
	$html .= '</ul></div>';

	$html .= '<div class="cdm-secao">';
	$html .= '<h2>Prefere fazer a sua?</h2>';
	$html .= '<p>É o outro lado deste site, e não é concorrência do primeiro: o ' . cdm_casca_link_html( 'materiais', 'Guia de materiais' ) . ' diz qual cola, qual rejunte e quantas pastilhas a sua peça pede, com a declaração do fabricante em cada recomendação; a ' . cdm_casca_link_html( 'como-fazer', 'Escola' ) . ' mostra o passo a passo.</p>';
	$html .= '</div>';
	$html .= '</div>';

	return $html;
} );

/**
 * O GUIA DE MATERIAIS, reescrito em 1.2.0 pela regra das camadas (seção 15.2).
 *
 * A página tinha nove seções e sete delas eram bastidor de fábrica: a escada de
 * sete níveis de fonte, a confissão que ela obriga, como resolvemos divergência
 * entre fabricantes, a tabela de contagens do banco. Tudo verdade, tudo
 * importante — e nada disso é o que alguém com um vaso de barro na mão veio ler.
 *
 * Esse material não foi jogado fora: mudou para /materiais/como-sabemos/, que é
 * a página cujo produto É o rigor, com `noindex` até ter texto próprio e fora do
 * sitemap. Aqui ficam as seis prateleiras e o único achado que muda a mão de
 * quem faz: silicone acético não serve em espelho nem em cimento, e o neutro do
 * mesmo fabricante serve.
 */
add_shortcode( 'cdm_materiais', function () {
	$n = cdm_casca_numeros();

	$html  = '<div class="cdm-bloco">';
	$html .= '<div class="cdm-abertura">';
	$html .= '<p class="cdm-linha-mestra">Antes do primeiro caco, duas perguntas: sobre o que você vai colar, e onde a peça vai ficar.</p>';
	$html .= '<p>As duas juntas decidem a cola e o rejunte. A mesma peça feita para a sala e para o jardim leva material diferente — e a que foi feita para dentro não sobrevive lá fora.</p>';
	$html .= '<p>É por isso que uma lista de materiais copiada do vaso de outra pessoa não serve para o seu.</p>';
	$html .= '</div>';

	$html .= '<div class="cdm-secao">';
	$html .= '<h2>As seis prateleiras</h2>';
	$html .= cdm_casca_cards_guia_html();
	$html .= '</div>';

	$html .= '<div class="cdm-secao">';
	$html .= '<h2>O que quase todo mundo erra</h2>';
	$html .= '<p>Se a sua peça é de espelho, de cimento ou de vidro laminado, o <strong>silicone acético</strong> não serve — e é justamente o que a maioria dos tutoriais manda usar. O <strong>silicone neutro</strong> serve, e é do mesmo fabricante: não precisa trocar de marca, precisa pegar o tubo certo na prateleira.</p>';
	$html .= '<p>O acético continua ótimo para o que ele foi feito. O problema é o caquinho de espelho e o vaso de cimento, que são metade do mosaico brasileiro.</p>';
	$html .= '</div>';

	$html .= '<div class="cdm-secao">';
	$html .= '<h2>Onde ficam os links de compra</h2>';
	$html .= '<p>Quando houver link de loja para um material, ele aparece <em>antes</em> da parte que mostra de onde veio a informação — e essa parte continua ali, pequena, para quem quiser conferir. Como isso funciona está em ' . cdm_casca_link_html( 'divulgacao-de-afiliados', 'Divulgação de afiliados' ) . '.</p>';
	$html .= '</div>';

	/* A CAMADA DE PROVA desta página: três linhas e o caminho para a página que
	   guarda o método inteiro. O denominador é o banco INTEIRO, não a categoria
	   cola — a frase "hoje 10 dos 5 itens esperam link" esteve no ar porque os
	   dois números certos foram postos na mesma frase errada. */
	$html .= '<div class="cdm-prova">';
	$html .= '<h2>Como sabemos</h2>';
	$html .= '<p>Nenhuma recomendação daqui veio de blog: cada uma sai do que o fabricante publica sobre o próprio produto, com o documento e a data em que foi lido. Quando ele não fala de uma superfície, a página escreve que não fala — silêncio não vira "pode".</p>';
	$html .= '<p>Hoje o banco tem ' . cdm_casca_num( $n['itens_no_banco'] ) . ' itens de fabricante, sendo ' . cdm_casca_num( $n['materiais_cola'] ) . ' colas e ' . cdm_casca_num( $n['materiais_rejunte'] ) . ' rejuntes, e ' . cdm_casca_num( $n['esperando_link'] ) . ' deles ainda esperam link de loja.</p>';
	$html .= '<p>O método inteiro — de onde vem cada declaração, o que fazemos quando duas fontes discordam e o que ainda não conferimos — está em ' . cdm_casca_link_html( 'materiais/como-sabemos', 'Como sabemos' ) . '.</p>';
	$html .= '</div>';
	$html .= '</div>';

	return $html;
} );

/**
 * /materiais/como-sabemos/ — a página cujo produto é o rigor.
 *
 * Recebeu em 1.2.0 tudo o que era bastidor no Guia. Nasce com `noindex` e fora
 * do sitemap por decisão do despacho: ela existe para ser conferida por quem
 * quer conferir, não para disputar busca. Fina ela não é — a trava de página
 * fina da seção 8 mede o corpo dela como mede o das outras.
 */
add_shortcode( 'cdm_como_sabemos', function () {
	$n = cdm_casca_numeros();

	$html  = '<div class="cdm-bloco">';
	$html .= '<div class="cdm-abertura">';
	$html .= '<p class="cdm-linha-mestra">Toda recomendação desta casa aponta para um documento do fabricante, com data. Esta página mostra como isso é feito — e o que ainda não conferimos.</p>';
	$html .= '<p>Ela existe para ser conferida. Se você achar aqui uma recomendação que contradiz o que o fabricante publica, ela vale mais que a nossa e entra no lugar.</p>';
	$html .= '</div>';

	$html .= '<div class="cdm-secao">';
	$html .= '<h2>O que o banco já sustenta, em número</h2>';
	$html .= '<p>Medido em ' . esc_html( cdm_casca_data_br( $n['medido_em'] ) ) . ':</p>';
	$html .= '<div class="cdm-tabela"><table class="cdm-quadro"><tbody>';
	$html .= '<tr><td>Itens de fabricante no banco</td><td class="cdm-n">' . esc_html( number_format_i18n( $n['itens_no_banco'] ) ) . '</td></tr>';
	$html .= '<tr><td>Adesivos</td><td class="cdm-n">' . esc_html( number_format_i18n( $n['materiais_cola'] ) ) . '</td></tr>';
	$html .= '<tr><td>Rejuntes</td><td class="cdm-n">' . esc_html( number_format_i18n( $n['materiais_rejunte'] ) ) . '</td></tr>';
	$html .= '<tr><td>Bases cobertas (cerâmica, vidro, laminado, espelho, MDF, cimento, alvenaria, metal, plástico)</td><td class="cdm-n">' . esc_html( number_format_i18n( $n['bases'] ) ) . '</td></tr>';
	$html .= '<tr><td>Ambientes cobertos (seco, molhado, externo abrigado, sol e chuva, imersão)</td><td class="cdm-n">' . esc_html( number_format_i18n( $n['ambientes'] ) ) . '</td></tr>';
	$html .= '<tr><td>Combinações base × ambiente mapeadas</td><td class="cdm-n">' . esc_html( number_format_i18n( $n['celulas_matriz'] ) ) . '</td></tr>';
	$html .= '<tr><td>Combinações em que há recomendação com fonte</td><td class="cdm-n">' . esc_html( number_format_i18n( $n['celulas_com_saida'] ) ) . '</td></tr>';
	$html .= '<tr><td>Combinações que ficam <strong>sem resposta</strong>, e a página diz por quê</td><td class="cdm-n">' . esc_html( number_format_i18n( $n['celulas_sem_saida'] ) ) . '</td></tr>';
	$html .= '<tr><td>Itens esperando link de loja</td><td class="cdm-n">' . esc_html( number_format_i18n( $n['esperando_link'] ) ) . '</td></tr>';
	$html .= '</tbody></table></div>';
	$html .= '<p class="cdm-nota"><strong>Publicar as duas que ficam sem resposta é parte do método.</strong> São peça de plástico e peça em contato permanente com água: nenhum dos fabricantes do banco declara substrato plástico, e a única menção que existe a colar debaixo d\'água está em material de imprensa, não em ficha técnica. Um guia que nunca diz "não sei" está inventando em algum lugar.</p>';
	$html .= '</div>';

	$html .= '<div class="cdm-secao">';
	$html .= '<h2>O achado do silicone, com o documento na mão</h2>';
	$html .= '<p>A ficha técnica BRSA004 do Silicone Acético Construção da Tekbond, revisada em 10/2025, lista entre as superfícies em que o produto <strong>não</strong> deve ser usado:</p>';
	$html .= '<div class="cdm-citacao"><p>espelhos, vidro laminado, metal corrosível, superfícies pintadas, superfícies porosas, superfícies alcalinas, concreto, cimento, tijolo, calcário, acrílico, aquário e imersão contínua.</p></div>';
	$html .= '<p>Caco de espelho, vaso de cimento e peça de área molhada são exatamente o que o mosaico artesanal brasileiro cola com silicone acético, por indicação de blog. E a saída vem do mesmo fabricante: o Silicone Neutro da Tekbond é declarado para espelho, concreto, alvenaria e pedra — justamente as restrições do acético. Não é preciso trocar de marca para acertar; é preciso ler a ficha certa.</p>';
	$html .= '</div>';

	$html .= '<div class="cdm-secao">';
	$html .= '<h2>Quando as fontes discordam</h2>';
	$html .= '<p>Duas fontes boas discordando é rotina. A saída proibida é a média, porque ela esconde justamente o desacordo que faz a informação valer. Publicamos as duas declarações com as duas datas e resolvemos para o lado em que <strong>errar dói menos</strong> — e aqui esse lado é sempre o conjunto <strong>mais estreito</strong>: errar para o lado largo faz alguém colar uma peça que vai descolar.</p>';
	$html .= '<p>Um exemplo do próprio banco: a mesma ficha indica alumínio anodizado e proíbe metal corrosível, zinco e chapa galvanizada. Vence a proibição, porque quem monta mosaico em casa não sabe dizer se a chapa dela é galvanizada.</p>';
	$html .= '<p>E silêncio não é permissão. Quando o fabricante simplesmente não fala de uma superfície, isso não vira "pode" nem vira "não pode": vira uma terceira coisa, escrita na tela como não declarada. É por isso que ' . cdm_casca_num( $n['celulas_sem_saida'] ) . ' das ' . cdm_casca_num( $n['celulas_matriz'] ) . ' combinações ficam em aberto em vez de receberem um palpite.</p>';
	$html .= '</div>';

	$html .= '<div class="cdm-secao">';
	$html .= '<h2>De onde vem cada declaração</h2>';
	$html .= '<p>Toda origem tem nível, e o nível decide o que ela pode sustentar. Em conflito, o nível mais alto vence e o outro fica registrado.</p>';
	$html .= '<div class="cdm-tabela"><table class="cdm-quadro"><thead><tr><th>Nível</th><th>Origem</th><th>O que pode sustentar</th><th>Temos hoje</th></tr></thead><tbody>';
	foreach ( cdm_casca_escada_de_fontes() as $degrau ) {
		$html .= '<tr>';
		$html .= '<td class="cdm-n">' . esc_html( $degrau['nivel'] ) . '</td>';
		$html .= '<td>' . esc_html( $degrau['origem'] ) . '</td>';
		$html .= '<td>' . esc_html( $degrau['sustenta'] ) . '</td>';
		$html .= '<td>' . ( $degrau['existe'] ? 'sim' : '—' ) . '</td>';
		$html .= '</tr>';
	}
	$html .= '</tbody></table></div>';
	$html .= '<p class="cdm-nota"><strong>A confissão que essa tabela obriga:</strong> não temos nenhuma ficha técnica lida em PDF, linha a linha, até hoje. O banco está apoiado em ficha identificada por código colhida no domínio do próprio fabricante e em página oficial de produto. Blog, marketplace e agregador não sustentam nada aqui — nem uma linha.</p>';
	$html .= '</div>';

	$html .= '<div class="cdm-secao">';
	$html .= '<h2>Voltar para o Guia</h2>';
	$html .= '<p>Se você veio parar aqui procurando qual cola usar, a resposta está em ' . cdm_casca_link_html( 'materiais', 'Materiais' ) . ' — esta página é o bastidor dela.</p>';
	$html .= '</div>';
	$html .= '</div>';

	return $html;
} );

if ( ! function_exists( 'cdm_casca_escada_de_fontes' ) ) {
/**
 * A escada de fontes, para a tela. É a transposição da que está em
 * dados/esquema-banco.json — e o teste confere que os dois lados batem, para
 * ela não envelhecer aqui em silêncio.
 */
function cdm_casca_escada_de_fontes() {
	$escada = array(
		array( 'nivel' => 1, 'origem' => 'ficha técnica lida', 'sustenta' => 'Qualquer campo técnico, inclusive restrição e tempo de cura, citando o número do documento e a revisão.', 'existe' => false ),
		array( 'nivel' => 2, 'origem' => 'ficha técnica por busca', 'sustenta' => 'Campo técnico atribuído a uma ficha identificada por código e revisão, colhida no domínio do fabricante sem abrir o PDF. Vai para a tela com o código e a data.', 'existe' => true ),
		array( 'nivel' => 3, 'origem' => 'página de produto do fabricante', 'sustenta' => 'Substratos declarados, indicações de uso, embalagem e norma citada pelo próprio fabricante. É o limite do que sustenta recomendação primária.', 'existe' => true ),
		array( 'nivel' => 4, 'origem' => 'material de imprensa do fabricante', 'sustenta' => 'Menção de uso, sempre citada como tal. NÃO sustenta recomendação primária nem entra em fórmula publicada.', 'existe' => true ),
		array( 'nivel' => 5, 'origem' => 'varejo oficial da marca', 'sustenta' => 'Embalagem, unidade de venda, peso líquido e imagem. Campo técnico só com "confira a embalagem" na tela.', 'existe' => false ),
		array( 'nivel' => 6, 'origem' => 'marketplace ou loja', 'sustenta' => 'Apenas preço, unidade de venda e imagem. Nunca compatibilidade, nunca restrição, nunca número que entre em fórmula.', 'existe' => false ),
		array( 'nivel' => 7, 'origem' => 'blog, busca ou agregador', 'sustenta' => 'Nada. Proibido como fonte técnica nesta ilha.', 'existe' => false ),
	);

	return apply_filters( 'cdm_escada_de_fontes', $escada );
}
}

add_shortcode( 'cdm_como_fazer', function () {
	$html  = '<div class="cdm-bloco">';
	$html .= '<p class="cdm-linha-mestra">Passo a passo de mosaico com a lista de materiais ligada ao Guia — e, quando a peça é para presentear, o caminho para comprar uma pronta.</p>';
	$html .= '<p>Um tutorial que manda "passe a cola" sem dizer qual cola serve naquela base e naquele ambiente é meio tutorial. Aqui cada passo a passo termina com a lista do que comprar, e cada item dessa lista aponta para a ficha do material, onde está a declaração do fabricante.</p>';

	$tutoriais = cdm_casca_tutoriais_html();
	if ( '' !== $tutoriais ) {
		$html .= $tutoriais;
	} else {
		$html .= '<div class="cdm-vazio">';
		$html .= '<h3>Os primeiros doze estão sendo escritos</h3>';
		$html .= '<p>Vaso, cachepô, tampo de mesa, quadro, espelho, mandala, filtro de barro, parede, número de casa, colar, técnica bizantina e um roteiro para quem nunca fez.</p>';
		$html .= '<p>Nenhum deles vai ao ar antes de a ficha do material que ele manda comprar existir — porque a lista de materiais é a metade que importa, e ela precisa apontar para algum lugar de verdade.</p>';
		$html .= '</div>';
	}

	$html .= '<div class="cdm-secao">';
	$html .= '<h2>As duas perguntas que vêm antes do primeiro caco</h2>';
	$html .= '<p>Todo tutorial daqui começa pelas mesmas duas, e não é enfeite de método: são elas que decidem o material, e material errado é o que faz a peça descolar semanas depois, quando já não dá para refazer.</p>';
	$html .= '<ul class="cdm-lista">';
	$html .= '<li><strong>Sobre o que você vai colar?</strong> Cerâmica esmaltada, vidro comum, vidro laminado, espelho, MDF, cimento, alvenaria, metal ou plástico. Parecem detalhes do mesmo grupo e não são: o mesmo fabricante que indica um silicone para vidro comum <em>proíbe</em> aquele silicone no vidro laminado e no espelho.</li>';
	$html .= '<li><strong>Onde a peça vai viver?</strong> Dentro de casa e seco, dentro de casa e molhado (banheiro, pia), fora mas abrigado, exposto ao sol e à chuva, ou dentro d\'água. A base pode ser a mesma e a resposta mudar inteira — há adesivo que o fabricante indica para cerâmica e que não declara nenhuma resistência a chuva e raios UV.</li>';
	$html .= '</ul>';
	$html .= '<p>É por isso que uma lista de materiais copiada de outro vaso não serve para o seu. O ' . cdm_casca_link_html( 'materiais', 'Guia de materiais' ) . ' responde essa combinação com a declaração do fabricante na frente, e diz quando não há resposta.</p>';
	$html .= '</div>';

	$html .= '<div class="cdm-secao">';
	$html .= '<h2>Como cada tutorial será escrito</h2>';
	$html .= '<p>Um passo a passo de artesanato costuma ser escrito de memória por quem já faz há anos — e a memória pula justamente o que o iniciante precisa. Estes vão nascer com três coisas obrigatórias:</p>';
	$html .= '<ul class="cdm-lista">';
	$html .= '<li><strong>Lista de materiais com a base e o ambiente declarados</strong>, ligada à ficha de cada item — nunca "cola apropriada".</li>';
	$html .= '<li><strong>Quantidade calculada</strong> para o tamanho da peça do tutorial, e não "o quanto precisar". Quem compra rejunte pela conta que a internet publica compra pouco: aquela conta é de azulejo de obra, e pastilha de artesanato consome várias vezes mais.</li>';
	$html .= '<li><strong>Revisão de quem faz.</strong> Cada tutorial sai marcado como revisado por uma artesã que trabalha com mosaico, ou não sai. Texto de processo escrito só a partir de documento de fabricante erraria na parte que o documento não cobre — a da mão.</li>';
	$html .= '</ul>';
	$html .= '<p>E a ' . cdm_casca_link_html( 'loja', 'Loja' ) . ' é para quem quer a peça e não o processo: é o mesmo trabalho, feito por quem já sabe.</p>';
	$html .= '</div>';
	$html .= '</div>';

	return $html;
} );

add_shortcode( 'cdm_sobre', function () {
	$n = cdm_casca_numeros();

	$html  = '<div class="cdm-bloco">';
	$html .= '<p class="cdm-linha-mestra">O Clube do Mosaico é o ateliê de uma artesã somado a um guia técnico de materiais — e as duas metades seguem a mesma regra: nada é afirmado sem origem.</p>';

	$html .= '<div class="cdm-secao"><h2>Quem faz as peças</h2>';
	/* O bloco da artesã nasce PRONTO e vazio: o Raphael decidiu em 11/09/2026
	   que ela aparece com nome, foto e redes, e esses três não chegaram ainda.
	   Enquanto não chegam, a página escreve "a artesã" — nunca um nome
	   inventado, nunca uma foto de banco de imagens. */
	$html .= '<p>As peças são feitas por <strong>uma artesã</strong>, à mão, uma de cada vez. Ela corta, assenta, rejunta e fotografa cada peça, e é ela mesma quem cadastra cada uma no site — não há intermediário entre o trabalho dela e a ficha que você lê.</p>';
	$html .= '<p>O nome, o rosto e os perfis dela entram nesta página assim que ela os autorizar. Até lá fica escrito assim: sem nome de fantasia, sem foto genérica e sem história inventada para dar cara de marca a um trabalho que já tem uma pessoa de verdade atrás.</p></div>';

	$html .= '<div class="cdm-secao"><h2>Por que existe o guia</h2>';
	$html .= '<p>Porque a pergunta técnica do mosaico artesanal não tem dono. Quem procura "qual cola para mosaico" hoje encontra lojinha, Pinterest, vídeo e blog de 2012 — nenhum deles citando fabricante, código de ficha ou data. É um assunto em que errar custa caro: a peça descola semanas depois, e quem fez não sabe por quê.</p>';
	$html .= '<p>Estado de hoje, sem arredondar para cima: ' . cdm_casca_num( $n['materiais_cola'] ) . ' adesivos de fabricante no banco, ' . cdm_casca_num( $n['celulas_matriz'] ) . ' combinações de base e ambiente mapeadas, e ' . cdm_casca_num( $n['celulas_sem_saida'] ) . ' delas declaradas sem resposta. Nenhuma recomendação foi herdada de blog.</p></div>';

	$html .= '<div class="cdm-secao"><h2>Como é feito</h2>';
	$html .= '<p>O conteúdo técnico é versionado num repositório antes de chegar ao site, e o banco tem um verificador que reprova registro sem fonte, sem data ou com declaração incoerente — a tabela de recomendações é <em>recalculada</em> a partir das declarações dos fabricantes, nunca digitada à mão. O que está no ar passou por ele.</p>';
	$html .= '<p>Quando uma fonte melhor aparece, o campo é substituído e a data de verificação muda junto. Correção não é vergonha: é para isso que a data serve. Achou uma declaração de fabricante que contradiz o que está aqui? Ela vale mais que a nossa, e entra.</p></div>';

	$html .= '<div class="cdm-secao"><h2>O que este site não faz</h2>';
	$html .= '<ul class="cdm-lista">';
	$html .= '<li class="cdm-nao-fazemos">Não publica contagem regressiva, "últimas unidades", selo de mais vendido nem nota de avaliação que não tenha medido.</li>';
	$html .= '<li>Não usa preço nem comissão como critério técnico. A ordem de qualquer lista é: primeiro quem cumpre <em>todas</em> as condições declaradas pelo fabricante, depois quem é mais adequado, e só como desempate entre equivalentes quem tem link de loja.</li>';
	$html .= '<li>Não inventa peça, medida, preço ou foto. Peça que não existe não aparece, nem como exemplo.</li>';
	$html .= '<li>Não aceita link pago nem publieditorial.</li>';
	$html .= '</ul></div>';

	$html .= '<p class="cdm-nota">As peças do ateliê são produto próprio e <strong>não</strong> são links de afiliado. Os materiais do guia podem ter link de afiliado, e isso está explicado em ' . cdm_casca_link_html( 'divulgacao-de-afiliados', 'Divulgação de afiliados' ) . '. Misturar as duas coisas sem avisar seria o começo de deixar a comissão escolher o que recomendar.</p>';
	$html .= '</div>';

	return $html;
} );

add_shortcode( 'cdm_contato', function () {
	$html  = '<div class="cdm-bloco">';
	$html .= '<p class="cdm-linha-mestra">Para falar sobre uma peça, o caminho é o botão <em>Verificar disponibilidade</em> na página dela: a mensagem chega direto à artesã, com o nome da peça junto.</p>';
	$html .= '<p>É de propósito que não há um formulário genérico aqui. Mensagem que chega sem dizer de qual peça se trata vira uma conversa de três trocas antes de começar — e quem responde é uma pessoa só, que também é quem faz as peças.</p>';

	$html .= '<div class="cdm-secao"><h2>Encomenda sob medida</h2>';
	$html .= '<p>Peça feita para um espaço ou para presentear começa do mesmo jeito: escolha na ' . cdm_casca_link_html( 'loja', 'Loja' ) . ' a peça mais parecida com o que você quer e diga o que muda. O prazo depende da peça e é combinado antes, nunca depois.</p>';
	$html .= '<p>Quatro informações encurtam a conversa pela metade, e a última é a que mais gente esquece:</p>';
	$html .= '<ul class="cdm-lista">';
	$html .= '<li><strong>Medida aproximada</strong> — altura e largura, mesmo que em palmos. Peça de mosaico é pesada, e o tamanho muda a base.</li>';
	$html .= '<li><strong>Cores</strong>, ou uma foto do ambiente. Pastilha não é tinta: a paleta é a que existe, e é melhor saber disso no começo.</li>';
	$html .= '<li><strong>Para quando</strong>. Peça sob encomenda é feita do zero, e cada camada tem tempo de secagem que não dá para apressar.</li>';
	$html .= '<li><strong>Onde a peça vai ficar</strong> — dentro de casa, área molhada, varanda, jardim, sol e chuva. Isso não é curiosidade: é o que decide o adesivo e o rejunte. A mesma peça feita para a sala e para o jardim leva material diferente, e a que foi feita para dentro não sobrevive lá fora.</li>';
	$html .= '</ul></div>';

	$html .= '<div class="cdm-secao"><h2>Correção no guia técnico</h2>';
	$html .= '<p>Achou aqui uma recomendação que o próprio fabricante contradiz? Isso é defeito nosso, e a gente quer saber. A regra é a mesma da página ' . cdm_casca_link_html( 'sobre', 'Sobre' ) . ': o que o fabricante publica vale mais que o que está escrito aqui, e entra no lugar assim que for conferido.</p>';
	$html .= '<p class="cdm-nota"><strong>O canal de e-mail ainda está sendo configurado.</strong> Preferimos deixar isto escrito a publicar um endereço que ainda não recebe — mensagem que se perde é pior que canal ausente. Até ele existir, o contato sobre peça acontece pelo botão da própria peça.</p></div>';
	$html .= '</div>';

	return $html;
} );

add_shortcode( 'cdm_afiliados', function () {
	$n = cdm_casca_numeros();

	$html  = '<div class="cdm-bloco">';
	$html .= '<p class="cdm-linha-mestra">Quando houver link de loja para um material deste guia, ele será link de afiliado — e estará marcado como tal.</p>';
	$html .= '<p>Isso significa que, se você comprar por ele, o Clube do Mosaico pode receber uma comissão da loja, sem custo adicional para você. Os programas usados são os de afiliados da Shopee e do Mercado Livre.</p>';

	$html .= '<div class="cdm-secao"><h2>A distinção que vale para este site</h2>';
	$html .= '<p>Há dois tipos de produto aqui, e eles não se misturam:</p>';
	$html .= '<ul class="cdm-lista">';
	$html .= '<li><strong>As peças do ateliê</strong> são produto próprio, feitas à mão pela artesã. Comprar uma delas é comprar direto de quem fez. <em>Nunca</em> são link de afiliado.</li>';
	$html .= '<li><strong>Os materiais do guia</strong> (cola, rejunte, pastilha, alicate) são produtos de fabricantes que este site não fabrica nem vende. É aí, e só aí, que pode existir link de afiliado.</li>';
	$html .= '</ul></div>';

	$html .= '<div class="cdm-secao"><h2>O que a comissão nunca muda</h2>';
	$html .= '<ul class="cdm-lista">';
	$html .= '<li><strong>A ordem da lista.</strong> Primeiro entra quem cumpre todas as condições declaradas pelo fabricante para aquela base e aquele ambiente; depois, entre os que cumprem, quem é tecnicamente mais adequado. Ter link de loja só desempata entre itens equivalentes — e nunca comparamos taxa de comissão entre programas.</li>';
	$html .= '<li><strong>Quem aparece.</strong> Produto que o fabricante proíbe naquela base não sobe para o topo por ter link; ele aparece em seção separada, abaixo, dizendo qual restrição o eliminou.</li>';
	$html .= '<li><strong>O dado técnico.</strong> A fonte de uma especificação é sempre o fabricante. Um link de loja nunca substitui o endereço de origem do dado — e a procedência continua na página, como texto, para ser conferida.</li>';
	$html .= '</ul></div>';

	$html .= '<div class="cdm-secao"><h2>Preço</h2>';
	$html .= '<p>Nenhum preço de material aqui é apresentado como o preço de agora. Ou a página não traz preço, ou traz a faixa com a data em que ela foi coletada. Preço muda mais rápido do que qualquer página estática consegue acompanhar, e fingir o contrário seria enganar. O preço das peças do ateliê é outra coisa: esse é o preço real, definido por quem faz.</p></div>';

	/* A frase "não há nenhum link no ar" era digitada, e frase digitada sobre o
	   próprio banco passa a mentir em silêncio no dia em que o banco muda. Agora
	   ela é a SUBTRAÇÃO entre o que existe e o que espera link: no dia em que o
	   primeiro link entrar, esta página muda sozinha. */
	$com_link = (int) $n['itens_no_banco'] - (int) $n['esperando_link'];
	$html    .= '<p class="cdm-nota"><strong>Estado de hoje:</strong> dos ' . cdm_casca_num( $n['itens_no_banco'] ) . ' materiais do banco, ' . cdm_casca_num( $com_link ) . ' têm link de loja e ' . cdm_casca_num( $n['esperando_link'] ) . ' estão com o lugar do link reservado e vazio. Esta página existe desde o primeiro dia porque a divulgação precisa estar publicada <em>antes</em> do primeiro link, não depois.</p>';
	$html .= '</div>';

	return $html;
} );

add_shortcode( 'cdm_privacidade', function () {
	$html  = '<div class="cdm-bloco">';
	$html .= '<p class="cdm-linha-mestra">Este site coleta o mínimo: nome e WhatsApp, e só quando você pede para verificar a disponibilidade de uma peça.</p>';
	$html .= '<p>Não há cadastro para navegar, não há newsletter e não há pergunta de CPF, endereço ou e-mail para ver preço.</p>';

	$html .= '<div class="cdm-secao"><h2>O que é coletado, e quando</h2>';
	$html .= '<ul class="cdm-lista">';
	$html .= '<li><strong>Nome e WhatsApp</strong>, quando você envia o formulário <em>Verificar disponibilidade</em> de uma peça. Junto vai o registro de qual peça era e a data em que você autorizou o contato.</li>';
	$html .= '<li><strong>Nada além disso.</strong> Não pedimos e-mail, endereço nem documento nesse formulário. Endereço de entrega, quando a compra acontece, é combinado direto na conversa.</li>';
	$html .= '</ul></div>';

	$html .= '<div class="cdm-secao"><h2>Para que é usado, e por quem</h2>';
	$html .= '<p>Para uma finalidade só: a artesã entrar em contato com você pelo WhatsApp sobre aquela peça — disponibilidade, prazo, forma de envio. Quem recebe a mensagem é ela.</p>';
	$html .= '<p><strong>Seus dados não são vendidos, alugados nem repassados a terceiros</strong>, e não entram em lista de disparo. Não usamos o seu WhatsApp para mandar novidade, promoção ou lembrete.</p></div>';

	$html .= '<div class="cdm-secao"><h2>Seus direitos</h2>';
	$html .= '<p>Você pode pedir, a qualquer momento, para ver, corrigir ou apagar o que foi guardado sobre você — basta dizer isso na própria conversa do WhatsApp. Apagar é apagar: o registro sai do site.</p></div>';

	$html .= '<div class="cdm-secao"><h2>Cookies e medição</h2>';
	$html .= '<p>O site usa os cookies essenciais do WordPress para funcionar. Não há remarketing, não há pixel de rede social e não há perfil de comportamento sendo montado sobre você.</p>';
	$html .= '<p>Se um dia houver medição de audiência, esta página será atualizada <em>antes</em> de ela ser ligada, com a data da mudança.</p></div>';

	$html .= '<div class="cdm-secao"><h2>Links para outras lojas</h2>';
	$html .= '<p>Algumas páginas do guia de materiais podem trazer link para loja externa, explicado em ' . cdm_casca_link_html( 'divulgacao-de-afiliados', 'Divulgação de afiliados' ) . '. Ao clicar, você entra no site daquela loja, e o que acontece lá é regido pela política dela, não por esta.</p></div>';
	$html .= '</div>';

	return $html;
} );

/* ---------------------------------------------------------------------------
 * 5. Estrutura do site: páginas, página inicial e limpeza do tema padrão
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_casca_definicao_paginas' ) ) {
/**
 * As páginas da ilha, por slug.
 *
 * O TÍTULO DA HOME NÃO É "INÍCIO" (1.2.0). O tema imprime o título da página
 * como H1, e a home nascia com "Início" porque foi assim que a definição a
 * criou — o Raphael viu isso no ar e reprovou. A palavra Início não diz nada a
 * ninguém e ocupa a linha mais visível da página mais visitada. Agora a home
 * abre com a frase do VOZ.md, que é a mesma que o rodapé e o <title> usam.
 *
 * 'pai' é o slug da página-mãe, e é ele que faz a URL mostrar a árvore da
 * seção 16 do contrato. Só 'noindex' fica fora do sitemap.
 */
function cdm_casca_definicao_paginas() {
	return array(
		'inicio'                  => array( 'titulo' => 'Mosaico feito à mão, uma peça por vez', 'conteudo' => '[cdm_home]' ),
		'loja'                    => array( 'titulo' => 'Loja', 'conteudo' => '[cdm_loja]' ),
		'materiais'               => array( 'titulo' => 'Materiais', 'conteudo' => '[cdm_materiais]' ),
		/* 'camada' => 'prova' é a ÚNICA página em que a linguagem de prova pode
		   ocupar o texto inteiro (seção 15.2). É declarada aqui, é uma só, e o
		   teste conta: sem essa contagem, bastaria declarar a home como prova
		   para o portão de voz parar de valer — que é a porta dos fundos que a
		   Aquametria achou em 11/09/2026 ao tentar quebrar o próprio portão. */
		'materiais/como-sabemos'  => array( 'titulo' => 'Como sabemos', 'conteudo' => '[cdm_como_sabemos]', 'pai' => 'materiais', 'noindex' => true, 'camada' => 'prova' ),
		'como-fazer'              => array( 'titulo' => 'Como fazer', 'conteudo' => '[cdm_como_fazer]' ),
		'sobre'                   => array( 'titulo' => 'Sobre', 'conteudo' => '[cdm_sobre]' ),
		'contato'                 => array( 'titulo' => 'Contato', 'conteudo' => '[cdm_contato]' ),
		'divulgacao-de-afiliados' => array( 'titulo' => 'Divulgação de afiliados', 'conteudo' => '[cdm_afiliados]' ),
		'privacidade'             => array( 'titulo' => 'Privacidade', 'conteudo' => '[cdm_privacidade]' ),
	);
}
}

if ( ! function_exists( 'cdm_casca_slug_final' ) ) {
/** O último nível do caminho: 'materiais/como-sabemos' vira 'como-sabemos'. */
function cdm_casca_slug_final( $caminho ) {
	$partes = explode( '/', trim( (string) $caminho, '/' ) );
	return end( $partes );
}
}

if ( ! function_exists( 'cdm_casca_garantir_paginas' ) ) {
function cdm_casca_garantir_paginas( &$relato ) {
	$ids   = array();
	$criou = false;

	foreach ( cdm_casca_definicao_paginas() as $slug => $def ) {
		$pagina = get_page_by_path( $slug, OBJECT, 'page' );
		/* O pai precisa existir antes da filha, e a ordem da definição garante
		   isso; se não existir, a filha não nasce solta na raiz — ela espera. */
		$pai = 0;
		if ( ! empty( $def['pai'] ) ) {
			if ( empty( $ids[ $def['pai'] ] ) ) {
				$relato[] = 'página ' . $slug . ': adiada, a mãe ' . $def['pai'] . ' ainda não existe';
				continue;
			}
			$pai = (int) $ids[ $def['pai'] ];
		}

		if ( ! $pagina ) {
			$pid = wp_insert_post( array(
				'post_type'      => 'page',
				'post_title'     => $def['titulo'],
				'post_name'      => cdm_casca_slug_final( $slug ),
				'post_parent'    => $pai,
				'post_content'   => $def['conteudo'],
				'post_status'    => 'publish',
				'comment_status' => 'closed',
				'ping_status'    => 'closed',
			), true );
			if ( is_wp_error( $pid ) ) {
				$relato[] = 'página ' . $slug . ': erro — ' . $pid->get_error_message();
				continue;
			}
			update_post_meta( $pid, '_cdm_casca', '1' );
			$ids[ $slug ] = (int) $pid;
			$criou        = true;
			$relato[]     = 'página ' . $slug . ': criada (#' . $pid . ')';
			continue;
		}

		$pid          = (int) $pagina->ID;
		$ids[ $slug ] = $pid;
		$nossa        = ( '1' === get_post_meta( $pid, '_cdm_casca', true ) );

		if ( 'publish' !== $pagina->post_status ) {
			wp_update_post( array( 'ID' => $pid, 'post_status' => 'publish' ) );
			$relato[] = 'página ' . $slug . ': republicada (#' . $pid . ')';
		}
		/* O TÍTULO SE SINCRONIZA, o post_name NÃO. Sem esta linha a página nasce
		   com o título da definição e fica com ele para sempre: foi assim que
		   "Início" sobreviveu a duas versões da casca no ar, e foi assim que a
		   Robometria descobriu o mesmo defeito em 11/09/2026. Mexer no post_name
		   seria outra coisa — URL de página publicada não se move (seção 12.1). */
		if ( $nossa && trim( (string) $pagina->post_title ) !== $def['titulo'] ) {
			wp_update_post( array( 'ID' => $pid, 'post_title' => $def['titulo'] ) );
			$relato[] = 'página ' . $slug . ': título sincronizado (#' . $pid . ')';
		}
		if ( $nossa && (int) $pagina->post_parent !== $pai ) {
			wp_update_post( array( 'ID' => $pid, 'post_parent' => $pai ) );
			$relato[] = 'página ' . $slug . ': mãe ajustada (#' . $pid . ')';
		}
		// Só reescrevemos o corpo de página que é nossa e que perdeu o shortcode.
		if ( $nossa && false === strpos( (string) $pagina->post_content, $def['conteudo'] ) ) {
			wp_update_post( array( 'ID' => $pid, 'post_content' => $def['conteudo'] ) );
			$relato[] = 'página ' . $slug . ': shortcode reposto (#' . $pid . ')';
		}
	}

	if ( $criou ) {
		flush_rewrite_rules( false );
	}

	return $ids;
}
}

if ( ! function_exists( 'cdm_casca_paginas_noindex' ) ) {
/** Os slugs que a ilha declara fora do índice, tirados da própria definição. */
function cdm_casca_paginas_noindex() {
	$fora = array();
	foreach ( cdm_casca_definicao_paginas() as $slug => $def ) {
		if ( ! empty( $def['noindex'] ) ) {
			$fora[] = $slug;
		}
	}
	return $fora;
}
}

if ( ! function_exists( 'cdm_casca_robots_html' ) ) {
/**
 * A etiqueta de robô da página atual, ou '' quando ela é indexável.
 *
 * Devolve texto em vez de imprimir para o teste poder medir os DOIS lados — a
 * página que sai do índice e a que continua nele. Trava que sai de graça e
 * paga sozinha: `noindex` indevido tira do ar uma página que rankeia, e é
 * justamente o tipo de defeito que ninguém vê olhando a tela.
 */
function cdm_casca_robots_html( $id_atual ) {
	$ids = get_option( 'cdm_casca_paginas' );
	if ( ! is_array( $ids ) || ! $id_atual ) {
		return '';
	}
	foreach ( cdm_casca_paginas_noindex() as $slug ) {
		if ( isset( $ids[ $slug ] ) && (int) $ids[ $slug ] === (int) $id_atual ) {
			return '<meta name="robots" content="noindex, follow">' . "\n";
		}
	}
	return '';
}
}

if ( ! function_exists( 'cdm_casca_sitemap_sem_noindex' ) ) {
/**
 * Tira do sitemap o que a ilha declarou fora do índice.
 *
 * Sitemap é curadoria, não inventário (seção 14.1): página com `noindex` dentro
 * dele é um pedido de rastreamento para algo que a própria ilha não quer no
 * índice, e domínio novo tem orçamento de rastreamento minúsculo.
 */
function cdm_casca_sitemap_sem_noindex( $args, $tipo = 'page' ) {
	if ( 'page' !== $tipo ) {
		return $args;
	}
	$ids  = get_option( 'cdm_casca_paginas' );
	$fora = array();
	if ( is_array( $ids ) ) {
		foreach ( cdm_casca_paginas_noindex() as $slug ) {
			if ( ! empty( $ids[ $slug ] ) ) {
				$fora[] = (int) $ids[ $slug ];
			}
		}
	}
	if ( $fora ) {
		$ja                   = isset( $args['post__not_in'] ) && is_array( $args['post__not_in'] ) ? $args['post__not_in'] : array();
		$args['post__not_in'] = array_values( array_unique( array_merge( $ja, $fora ) ) );
	}
	return $args;
}
}

add_filter( 'wp_sitemaps_posts_query_args', 'cdm_casca_sitemap_sem_noindex', 10, 2 );

add_action( 'wp_head', function () {
	$id = function_exists( 'get_queried_object_id' ) ? get_queried_object_id() : 0;
	echo cdm_casca_robots_html( $id ); // markup fixo, sem dado de fora
}, 4 );

if ( ! function_exists( 'cdm_casca_fixar_identidade_do_site' ) ) {
/**
 * Nome e descrição do site, gravados como page_on_front já era.
 *
 * A Aquametria descobriu isto em 11/09/2026 MEDINDO a página pronta: o <title>
 * da home vem do par nome + descrição do WordPress, e a descrição dela nunca
 * tinha sido tocada desde a instalação. A linha mais lida do site — a do
 * resultado de busca — ainda era a frase que o instalador escreveu.
 */
function cdm_casca_fixar_identidade_do_site( &$relato ) {
	if ( get_option( 'blogname' ) !== CDM_CASCA_NOME_SITE ) {
		update_option( 'blogname', CDM_CASCA_NOME_SITE );
		$relato[] = 'blogname: ' . CDM_CASCA_NOME_SITE;
	}
	if ( get_option( 'blogdescription' ) !== CDM_CASCA_TAGLINE ) {
		update_option( 'blogdescription', CDM_CASCA_TAGLINE );
		$relato[] = 'blogdescription: ' . CDM_CASCA_TAGLINE;
	}
}
}

if ( ! function_exists( 'cdm_casca_fixar_home' ) ) {
function cdm_casca_fixar_home( $ids, &$relato ) {
	if ( empty( $ids['inicio'] ) ) {
		return;
	}
	if ( 'page' !== get_option( 'show_on_front' ) ) {
		update_option( 'show_on_front', 'page' );
		$relato[] = 'show_on_front: page';
	}
	if ( (int) get_option( 'page_on_front' ) !== (int) $ids['inicio'] ) {
		update_option( 'page_on_front', (int) $ids['inicio'] );
		$relato[] = 'page_on_front: #' . (int) $ids['inicio'];
	}
}
}

/* ---------------------------------------------------------------------------
 * 5b. O SITEMAP NÃO PODE RESPONDER 404
 *
 * Herdado da Robometria, onde foi medido em 10/09/2026: wp-sitemap.xml servia o
 * XML certo, com as páginas dentro, e um status HTTP 404. Para o Google,
 * sitemap com 404 é sitemap inexistente.
 *
 * A causa nasce na função logo abaixo: uma ilha que manda "Hello world!" para a
 * lixeira fica com ZERO posts publicados. As rotas de sitemap do WordPress
 * passam pela consulta principal, ela volta sem nenhum post, e o handle_404()
 * do núcleo carimba 404 ANTES de o renderizador de sitemap imprimir o XML.
 *
 * Esta ilha nasce no mesmo estado — só páginas, nenhum post —, então o conserto
 * vem junto com a causa, desde a primeira versão da casca. O filtro
 * pre_handle_404 existe no núcleo exatamente para isto e só age em requisição
 * que JÁ é de sitemap: toda outra URL continua podendo 404, que é o certo.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_casca_sitemap_nao_e_404' ) ) {
function cdm_casca_sitemap_nao_e_404( $curto_circuito, $consulta ) {
	if ( is_object( $consulta ) && method_exists( $consulta, 'get' ) && $consulta->get( 'sitemap' ) ) {
		return true;
	}
	return $curto_circuito;
}
}

add_filter( 'pre_handle_404', 'cdm_casca_sitemap_nao_e_404', 10, 2 );

if ( ! function_exists( 'cdm_casca_limpar_padrao' ) ) {
/**
 * "Hello world!" e "Sample Page" para a LIXEIRA — nunca apagados de verdade.
 *
 * Não é acabamento: enquanto a casca não existe, são esses dois itens que o
 * sitemap submetido ao Search Console lista. Sitemap é curadoria, não
 * inventário (seção 14.1), e página de amostra gasta orçamento de rastreamento
 * de domínio novo ensinando ao robô que aqui se publica coisa que não vale
 * voltar para buscar.
 *
 * Atenção desta ilha: o domínio teve vida anterior e há um sitemap de 2019 na
 * propriedade do Search Console. Isso é assunto de redirecionamento, não de
 * lixeira, e está anotado no ESTADO.md.
 */
function cdm_casca_limpar_padrao( &$relato ) {
	if ( 'feito' === get_option( 'cdm_casca_limpeza' ) ) {
		return;
	}

	$slugs   = array( 'hello-world', 'ola-mundo', 'sample-page', 'pagina-exemplo', 'pagina-de-exemplo' );
	$titulos = array( 'Hello world!', 'Olá, mundo!', 'Ola, mundo!', 'Sample Page', 'Página de exemplo', 'Pagina de exemplo' );

	$candidatos = get_posts( array(
		'post_type'        => array( 'post', 'page' ),
		'post_status'      => array( 'publish', 'draft', 'pending', 'private', 'future' ),
		'numberposts'      => 40,
		'orderby'          => 'ID',
		'order'            => 'ASC',
		'suppress_filters' => true,
	) );

	foreach ( $candidatos as $p ) {
		if ( '1' === get_post_meta( $p->ID, '_cdm_casca', true ) ) {
			continue;
		}
		$por_slug   = in_array( $p->post_name, $slugs, true );
		$por_titulo = in_array( trim( $p->post_title ), $titulos, true );
		if ( ! $por_slug && ! $por_titulo ) {
			continue;
		}
		if ( (int) get_option( 'page_on_front' ) === (int) $p->ID ) {
			continue;
		}
		wp_trash_post( $p->ID );
		$relato[] = 'lixeira: ' . $p->post_type . ' #' . $p->ID . ' (' . $p->post_name . ')';
	}

	update_option( 'cdm_casca_limpeza', 'feito', false );
}
}

if ( ! function_exists( 'cdm_casca_montar' ) ) {
function cdm_casca_montar( $forcar = false ) {
	$feita = get_option( 'cdm_casca_estrutura' );
	if ( ! $forcar && CDM_CASCA_VERSAO === $feita ) {
		return array();
	}

	$relato = array();
	$ids    = cdm_casca_garantir_paginas( $relato );
	cdm_casca_fixar_home( $ids, $relato );
	cdm_casca_fixar_identidade_do_site( $relato );
	cdm_casca_limpar_padrao( $relato );

	update_option( 'cdm_casca_paginas', $ids, false );
	update_option( 'cdm_casca_estrutura', CDM_CASCA_VERSAO, false );

	if ( ! $relato ) {
		$relato[] = 'nada a fazer: estrutura já estava de pé';
	}
	$relato[] = 'casca ' . CDM_CASCA_VERSAO . ' em ' . current_time( 'Y-m-d H:i' );
	update_option( 'cdm_casca_relato', $relato, false );

	return $relato;
}
}

if ( ! function_exists( 'cdm_casca_boot' ) ) {
function cdm_casca_boot() {
	static $ja = false;
	if ( $ja ) {
		return;
	}
	$ja = true;

	cdm_casca_montar( false );

	// Remontagem manual: /?cdm_casca=refazer (só para quem administra o site).
	$pedido = filter_input( INPUT_GET, 'cdm_casca', FILTER_DEFAULT );
	if ( 'refazer' === $pedido && current_user_can( 'manage_options' ) ) {
		$relato = cdm_casca_montar( true );
		nocache_headers();
		header( 'Content-Type: application/json; charset=utf-8' );
		echo wp_json_encode( array( 'versao' => CDM_CASCA_VERSAO, 'relato' => $relato ), JSON_UNESCAPED_UNICODE );
		exit;
	}
}
}

add_action( 'init', 'cdm_casca_boot', 20 );

if ( did_action( 'init' ) ) {
	cdm_casca_boot();
}
