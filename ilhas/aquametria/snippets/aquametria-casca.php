/**
 * Aquametria Casca — identidade e estrutura do site
 * Versão: 1.7.1 (12/09/2026) — O DEGRAU DO MEIO PASSA A RESOLVER. Achado no ar,
 * não na bancada: `aquametria_casca_url_se_existir()` pedia a página pelo SLUG
 * solto, e `get_page_by_path()` casa o CAMINHO INTEIRO em tipo hierárquico —
 * então 'tetras' nunca achava /peixes/tetras/. A bancada dava quatro degraus de
 * trilha, todos linkados; o site servia três, com o do meio em texto e o
 * BreadcrumbList com um item a menos. As duas metades liam vias diferentes: no
 * ar a primeira via (`_aquametria_id`) só responde por página que veio do Sync,
 * e as do eixo são criadas pela casca. Agora o caminho sai do mapa de páginas,
 * que é quem sabe quem é mãe de quem, e `ferramentas/render-para-teste.php`
 * imitou as três vias do site em vez de responder por todas.
 *
 * Versão: 1.7.0 (12/09/2026) — A CASCA APRENDE A TER FILHA. T4, leva 1 da malha
 * do eixo /peixes/. Três mudanças, e nenhuma cria página por conta própria:
 *   1. `aquametria_casca_definicao_paginas()` passou a perguntar pelo filtro
 *      `aquametria_paginas`, e cada entrada pode trazer `pai` => slug. É isso
 *      que faz a URL mostrar os três níveis da seção 16.1; até aqui toda página
 *      da ilha nascia na raiz, que é o que a árvore proíbe. Mãe antes de filha,
 *      por profundidade, porque wp_insert_post precisa do ID do pai — e filha
 *      que nasce na raiz por falta de mãe fica com o endereço errado, que não
 *      se move depois (seção 12.1).
 *   2. A CHAVE DE REMONTAGEM VIROU A VERSÃO MAIS UM RESUMO DO MAPA. Sem isso,
 *      página nova anunciada pelo filtro não nasceria até alguém subir a
 *      constante à mão — é o defeito que o Clube do Mosaico pagou em 12/09/2026,
 *      com a ferramenta F1 no ar em 404 e o Sync dizendo "aplicado com sucesso".
 *   3. A trilha e o cluster aprenderam o eixo /peixes/, pelo filtro
 *      `aquametria_peixes`, no mesmo molde do hub de calculadoras: a casca não
 *      guarda cópia de título nenhum, e ficha nova entra na trilha sozinha.
 * A home ganhou a entrada da seção nova (16.4f: toda URL tem dois links
 * internos, um deles da mãe) e o menu ganhou "Peixes".
 *
 * Versão: 1.6.0 (12/09/2026) — a ilha passa a MEDIR. Despacho de prioridade alta
 * de 12/09/2026 (dados/despachos.md): a tag do GA4 entra no wp_head pela casca,
 * nunca por plugin (seção 11.7), com o ID de medição desta ilha em constante no
 * topo deste arquivo. Sem ela a seção 5 do ARQUIPELAGO.md — visibilidade em IA —
 * não é mensurável: a referência de chatgpt.com, perplexity.ai e
 * gemini.google.com só aparece no GA4. Detalhes e o porquê da prioridade 23 na
 * seção 3f, aqui embaixo.
 *   ESTA VERSÃO TAMBÉM ACERTA O NÚMERO DA CASCA, e isso não é detalhe de
 *   etiqueta: a constante estava em 1.4.1 enquanto este cabeçalho, o manifest e
 *   todo o REGISTRO.md documentavam 1.5.0 (a árvore das treze páginas) e 1.5.1
 *   (o degrau da trilha da divulgação). As duas foram ao ar de verdade — o que
 *   nunca subiu foi o número. Como aquametria_casca_montar() só remonta a
 *   estrutura quando a constante muda, subir o número dispara uma remontagem, e
 *   por isso o acerto esperava um bloco que tocasse a casca: é este. A
 *   remontagem é idempotente (não duplica página, não repete a lixeira — que
 *   além disso está travada pela opção aquametria_casca_limpeza, e não
 *   reescreve página editada à mão), então o custo é uma passada de opções. A
 *   1.6.0 carrega as três coisas: a 1.5.0, a 1.5.1 e o GA4.
 * Versão: 1.5.1 (11/09/2026) — o degrau da trilha da página de afiliados passa a
 * dizer o mesmo que o H1 logo abaixo dele. O rodapé continua com o nome
 * reconhecível de aviso de comissão; só a trilha responde pelo nome da página.
 *
 * Versão: 1.5.0 (11/09/2026) — a ÁRVORE chega às treze páginas que já existem.
 * Seção 16 do ARQUIPELAGO.md e o que o despacho do Raphael de 11/09 deixou de
 * pé depois do bloco da voz. Três coisas entram, e NENHUMA cria URL nova — as
 * oito páginas de nível 1 e 2 seguem travadas até a leitura de 16/09 (item 5 do
 * despacho da Sentinela de 10/09 e seção 6 do ARVORE.md):
 *   (a) trilha visível em toda página menos a home (16.3), com o nível 2 em
 *       TEXTO enquanto a categoria não nasce — estado de transição declarado no
 *       ARVORE.md, e que vira link sozinho no dia em que a página existir;
 *   (b) `BreadcrumbList` em JSON-LD, levando só os degraus que têm endereço de
 *       verdade: ListItem intermediário sem `item` invalida a lista inteira, e
 *       breadcrumb inválido é breadcrumb ignorado;
 *   (c) bloco "Veja também" (16.4c) com 2 a 4 irmãs da mesma mãe, DERIVADAS do
 *       mesmo registro que alimenta o hub — irmã digitada à mão envelheceria no
 *       dia em que a próxima calculadora entrasse no ar —, mais a frase que
 *       linka a mãe no corpo (16.4b) com a contagem contada, nunca digitada.
 * O mapa de quem é mãe de quem está no ARVORE.md, e
 * `ferramentas/teste-arvore.mjs` confere que o documento e o código dizem a
 * mesma coisa: duas metades mantidas à mão divergem em silêncio, que é a
 * cicatriz da seção 8 do contrato.
 * Versão: 1.4.1 (11/09/2026) — duas coisas que só apareceram ao MEDIR a página
 * pronta, e as duas já estavam no ar antes desta execução:
 *   (a) o <title> da home vinha da tagline do WordPress, que nunca foi tocada
 *       desde o nascimento da ilha — a linha mais lida da página, no resultado
 *       de busca, na voz antiga. Agora a casca grava a opção blogdescription,
 *       como já grava page_on_front, e o título da home vira
 *       "Aquametria – as contas do seu aquário";
 *   (b) a tabela de constantes da /metodologia/ rolava 67 px na horizontal a
 *       360 px. O conversor de Markdown do Sync embrulha toda tabela vinda de
 *       conteudo/ num bloco que rola; esta é impressa direto pelo shortcode e
 *       por isso nunca passou por lá.
 * Versão: 1.4.0 (11/09/2026) — a home e o header passam a falar como o VOZ.md.
 * Despacho do Raphael de 11/09/2026 (seção 15 do ARQUIPELAGO.md): o rigor de
 * número, fonte e data continua inteiro, mas vira CAMADA DE PROVA — some do
 * título e do primeiro parágrafo, onde quem fala é o amigo aquarista do
 * VOZ.md. O que mudou, e por quê:
 *   (a) a home abre pela pergunta mais frequente da ilha ("Quantos litros tem o
 *       seu aquário?", com as três medidas) em vez do manifesto institucional;
 *   (b) o cartão de cada calculadora vira a PERGUNTA que a pessoa digita —
 *       "Quantos watts de aquecedor você precisa?" no lugar de "Potência do
 *       aquecedor por delta térmico". O código e o slug não mudaram: a URL de
 *       toda página segue onde estava (seção 12.1 do contrato);
 *   (c) a home ganha a prateleira de GUIAS, alimentada pelo filtro
 *       'aquametria_guias' — quem responde é o snippet dos artigos, então guia
 *       novo aparece aqui sozinho e a contagem nunca é digitada;
 *   (d) o menu diz "Como a gente calcula" no lugar de "Metodologia", e o título
 *       das páginas da casca passa a ser sincronizado (só nas que são nossas);
 *   (e) o que é prova — fonte, data, divergência entre fontes — desce para o fim
 *       da página, dentro de um bloco marcado com a classe `aqm-prova`. A marca
 *       existe para o portão poder separar voz de prova pela ESTRUTURA e não
 *       pela vizinhança da palavra (seção 8 do contrato).
 * O menu "Calculadoras · Produtos · Guias" que o VOZ.md descreve fica pela
 * metade de propósito: /produtos/ e /guias/ são páginas que ainda não existem, e
 * o item 5 do despacho da Sentinela congela página nova até 16/09. Elas entram
 * no menu no bloco da árvore (ARVORE.md), depois da leitura daquela data.
 * Versão: 1.3.1 (10/09/2026) — link para artigo-âncora deixa de dar salto de 301.
 * aquametria_casca_url_se_existir() só procurava em post_type 'page', e os três
 * artigos-âncora são 'post'. As duas vias falhavam, quem chamava caía no último
 * recurso (home_url('/<slug>/')) e publicava um endereço que responde 301 para
 * /2026/09/08/<slug>/. Item 3 do despacho da Sentinela de 10/09/2026: as três
 * calculadoras pareadas linkavam o artigo por um salto, e salto é orçamento de
 * rastreamento gasto à toa em domínio novo. Agora existe uma terceira via, que
 * busca o artigo por post_name em post_type 'post' e devolve o permalink real —
 * então o próximo artigo nasce com link canônico sem ninguém lembrar disto.
 * Versão: 1.3.0 (09/09/2026) — casca no celular e ícone próprio. Duas coisas que
 * a Sentinela Técnica pega abrindo o site no telefone: (a) o menu passa a ser um
 * botão sanfona abaixo de 782 px, com aria-expanded/aria-controls, Escape e clique
 * fora fechando — e os três links continuam no HTML servido, dentro de <nav>, para
 * quem lê sem JavaScript (crawler de IA inclusive); sem JavaScript o menu não some,
 * volta a ser a lista de sempre; (b) o ícone do site deixa de ser o do WordPress e
 * passa a ser o recipiente graduado da marca, em SVG na aba e em PNG no iOS, os dois
 * como data URI dentro do snippet — nada sobe para a biblioteca de mídia.
 * Versão: 1.2.0 (08/09/2026) — apelidos de endereço. Endereço adivinhado a partir do nome da
 * calculadora deixa de dar 404: /calculadora-de-aquecedor-de-aquario/ (o que o Raphael pediu),
 * /calculadora-de-aquecedor/, /calculadora-de-litros/ e mais dezoito irmãos redirecionam 301
 * para a página canônica — e só quando ela existe publicada, para nunca trocar um 404 por outro.
 * Versão: 1.1.0 (08/09/2026) — link do hub nunca mais aponta para página que não existe.
 * O endereço de cada calculadora passa a ser resolvido pelo id do repositório (_aquametria_id),
 * não por slug adivinhado, e o card só vira link se a página estiver publicada de verdade;
 * sem página, fica o selo "Em construção". Corrige o defeito 2 de 08/09/2026: o hub publicava
 * /calculadora-de-aquecedor/ para a C5, cuja página é /calculadora-de-potencia-do-aquecedor/,
 * e o clique dava 404. A 1.0.4 tinha ajustado o resumo da C12 no hub.
 *
 * Dá cara de Aquametria ao tema ativo, sozinho, sem construtor de página e sem
 * plugin de tema. Faz seis coisas:
 *   (a) carrega Chivo, IBM Plex Sans e IBM Plex Mono e injeta a paleta no wp_head;
 *   (b) troca a saída de core/site-title e core/site-logo pelo logotipo em SVG
 *       (recipiente graduado com linha de enchimento) mais o wordmark;
 *   (c) troca a saída de core/navigation pelo menu Calculadoras · Metodologia · Sobre;
 *   (d) cria, casando pelo slug, as páginas inicio, calculadoras, metodologia e sobre,
 *       e fixa inicio como página inicial;
 *   (e) manda "Hello world!" e "Sample Page" para a LIXEIRA (nunca apaga);
 *   (f) substitui a template part 'footer' do tema pelo rodapé da Aquametria
 *       (tagline e nota de fontes), para não ficarem dois rodapés empilhados;
 *   (g) redireciona 301 os apelidos de endereço (seção 1b) para a página canônica;
 *   (h) publica o ícone do site (seção 2b), no lugar do que o WordPress imprimiria.
 *
 * O conteúdo das quatro páginas mora em shortcodes deste snippet: atualizar o
 * snippet atualiza as páginas, sem tocar no editor do WordPress.
 *
 * A lista de calculadoras do hub está em aquametria_casca_calculadoras() e passa
 * pelo filtro 'aquametria_calculadoras' — cada calculadora nova vira 'publicada'
 * aqui (ou se registra pelo filtro no próprio snippet dela).
 *
 * Idempotente: rodar duas vezes não duplica página, não repete lixeira e não
 * reescreve página editada à mão. flush_rewrite_rules() só quando cria página.
 *
 * Regras herdadas (fase 4b): não usa a superglobal de servidor; sem "<?php" no
 * topo (o Code Snippets põe); texto de tela acentuado em UTF-8.
 */

if ( ! defined( 'ABSPATH' ) ) {
	return;
}

if ( ! defined( 'AQUAMETRIA_CASCA_VERSAO' ) ) {
	define( 'AQUAMETRIA_CASCA_VERSAO', '1.7.1' );
	/* A tagline é a primeira frase que um visitante lê no rodapé de toda página.
	   Até a 1.3.1 ela era a descrição interna do produto ("Calculadoras e dados
	   técnicos para dimensionar o seu aquário"); agora fala com quem chegou. */
	define( 'AQUAMETRIA_CASCA_TAGLINE', 'A conta do seu aquário, feita antes de você comprar errado' );
	/* A CURTA é outra coisa, e por isso é outra constante: ela vai para a opção
	   blogdescription do WordPress, e o núcleo monta com ela o <title> da HOME —
	   "Aquametria – as contas do seu aquário". Esse título é a linha que a pessoa
	   lê no resultado de busca, e o que estava lá até 11/09/2026 era a descrição
	   interna do produto ("Calculadoras e dados técnicos para dimensionar o seu
	   aquário"), escrita quando a ilha nasceu e nunca mais tocada. A do rodapé
	   pode ser longa porque quem chegou lá já está na página; a do título não,
	   porque o Google corta perto de 60 caracteres. */
	define( 'AQUAMETRIA_CASCA_TAGLINE_CURTA', 'as contas do seu aquário' );
	/* ID de medição do GA4 desta ilha — AQUAMETRIA, propriedade 553860444 na conta
	   'Arquipélago' (407777291), fluxo "Aquametria — site" (15766241359). Mora aqui,
	   no topo, e não no meio do código que imprime a tag, porque o despacho de
	   12/09/2026 é explícito: identificador de medição digitado no meio de uma
	   função é o tipo de dado que ninguém acha quando precisa trocar. A mesma
	   linha está no PROMPT.md da ilha, e é ELE que a bancada lê para conferir esta
	   constante — teste que pergunta ao snippet qual é o ID certo não mede nada
	   (seção 8 do ARQUIPELAGO.md). */
	define( 'AQUAMETRIA_CASCA_GA4_ID', 'G-8Y26XFZF39' );
}

/* ---------------------------------------------------------------------------
 * 1. Catálogo de calculadoras (fonte do hub e da home)
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_casca_calculadoras' ) ) {
function aquametria_casca_calculadoras() {
	$lista = array(
		array(
			'codigo'  => 'C1',
			'categoria' => 'aquario',
			'titulo'  => 'Quantos litros tem o seu aquário?',
			'slug'    => 'calculadora-de-litragem',
			'resumo'  => 'Mede comprimento, largura e altura em centímetros e sai o volume da etiqueta, o que cabe de verdade e a água que você vai tratar. O aquário fica guardado no seu navegador, então as outras contas já vêm preenchidas.',
			'estado'  => 'em-construcao',
		),
		array(
			'codigo'  => 'C3',
			'categoria' => 'filtragem',
			'titulo'  => 'Qual filtro dá conta do seu aquário?',
			'slug'    => 'calculadora-de-vazao-do-filtro',
			'resumo'  => 'A vazão em litros por hora que o seu aquário pede. A faixa é larga porque os próprios fabricantes declaram de 1,8 a 10 renovações por hora para o mesmo aquário — e a tela mostra quem disse cada extremo.',
			'estado'  => 'em-construcao',
		),
		array(
			'codigo'  => 'C5',
			'categoria' => 'aquecimento-e-luz',
			'titulo'  => 'Quantos watts de aquecedor você precisa?',
			'slug'    => 'calculadora-de-potencia-do-aquecedor',
			'resumo'  => 'A conta parte do frio que faz no seu cômodo, não do velho 1 W por litro. E filtra pela sua voltagem, para não chegar em casa um aquecedor de 110 V numa tomada de 220 V.',
			'estado'  => 'em-construcao',
		),
		array(
			'codigo'  => 'C12',
			'categoria' => 'filtragem',
			'titulo'  => 'Quanta mídia biológica cabe no seu filtro?',
			'slug'    => 'calculadora-de-midia-filtrante',
			'resumo'  => 'Quantos mililitros de mídia o seu aquário pede, pelas quatro dosagens que os fabricantes declaram — e que discordam dez vezes entre si. Com o teto do cesto do seu filtro junto, para você não comprar mídia que não entra.',
			'estado'  => 'em-construcao',
		),
		array(
			'codigo'  => 'C15',
			'categoria' => 'aquecimento-e-luz',
			'titulo'  => 'Quanta luz o seu aquário precisa?',
			'slug'    => 'calculadora-de-iluminacao',
			'resumo'  => 'Os lúmens para o seu aquário e quantas horas deixar aceso. As três leituras brasileiras chamam a mesma coisa pelo mesmo nome com números diferentes, e aqui elas aparecem lado a lado.',
			'estado'  => 'em-construcao',
		),
		array(
			'codigo'  => 'C2',
			'categoria' => 'aquario',
			'titulo'  => 'O móvel aguenta o seu aquário cheio?',
			'slug'    => 'calculadora-de-peso-e-carga',
			'resumo'  => 'O peso total e a carga por metro quadrado, ao lado da carga de projeto da NBR 6120. A gente dá o número; quem autoriza é engenheiro, nunca uma calculadora.',
			'estado'  => 'em-construcao',
		),
		array(
			'codigo'  => 'C7',
			'categoria' => 'aquecimento-e-luz',
			'titulo'  => 'Quanto o seu aquário gasta de luz por mês?',
			'slug'    => 'calculadora-de-consumo-de-energia',
			'resumo'  => 'Filtro, aquecedor e luz somados, com o tempo que cada um fica ligado de verdade — multiplicar a potência do aquecedor por 24 horas erra a conta para cima, e erra feio.',
			'estado'  => 'em-construcao',
		),
		array(
			'codigo'  => 'C8',
			'categoria' => 'lotacao',
			'titulo'  => 'Quantos peixes cabem no seu aquário?',
			'slug'    => 'calculadora-de-lotacao',
			'resumo'  => 'Três critérios de lotação lado a lado, com o nome de quem publicou cada um, e o aquário mínimo por espécie quando existe fonte que diga.',
			'estado'  => 'em-construcao',
		),
	);

	$lista = apply_filters( 'aquametria_calculadoras', $lista );

	return is_array( $lista ) ? $lista : array();
}
}

/**
 * Os guias da ilha, para a prateleira do fim da home (molde GUIA do VOZ.md).
 *
 * A casca NÃO guarda a lista: ela pergunta pelo filtro e quem responde é o
 * snippet que publica os artigos. É a mesma escolha do hub de calculadoras, e
 * pelo mesmo motivo — guia novo aparece na home sozinho, e a frase que diz
 * quantos guias existem é CONTADA, nunca digitada. Número de tela digitado à
 * mão foi o defeito que a Robometria e o Clube do Mosaico pagaram em 11/09/2026
 * (seção 8 do ARQUIPELAGO.md): era verdade no dia em que foi escrito e virou
 * mentira em silêncio no dia em que o banco cresceu.
 *
 * Cada entrada: slug (o post_name do artigo), manchete e resumo.
 */
if ( ! function_exists( 'aquametria_casca_guias' ) ) {
function aquametria_casca_guias() {
	$lista = apply_filters( 'aquametria_guias', array() );
	if ( ! is_array( $lista ) ) {
		return array();
	}

	$limpa = array();
	foreach ( $lista as $g ) {
		if ( ! is_array( $g ) || empty( $g['slug'] ) || empty( $g['manchete'] ) ) {
			continue;
		}
		$limpa[] = array(
			'slug'     => (string) $g['slug'],
			'manchete' => (string) $g['manchete'],
			'resumo'   => isset( $g['resumo'] ) ? (string) $g['resumo'] : '',
		);
	}

	return $limpa;
}
}

/**
 * O mapa do eixo /peixes/, vindo de quem publica as páginas dele.
 *
 * Cada entrada: nivel (1, 2 ou 3), pai (slug ou ''), rotulo (o título da
 * página, que é o degrau da trilha) e nivel2 (a categoria, quando houver).
 * Entrada malformada é descartada: trilha inventada é pior que trilha ausente.
 */
if ( ! function_exists( 'aquametria_casca_peixes' ) ) {
function aquametria_casca_peixes() {
	$lista = apply_filters( 'aquametria_peixes', array() );
	if ( ! is_array( $lista ) ) {
		return array();
	}

	$limpa = array();
	foreach ( $lista as $slug => $px ) {
		if ( ! is_array( $px ) || empty( $px['nivel'] ) || empty( $px['rotulo'] ) ) {
			continue;
		}
		$limpa[ (string) $slug ] = array(
			'nivel'  => (int) $px['nivel'],
			'pai'    => isset( $px['pai'] ) ? (string) $px['pai'] : '',
			'rotulo' => (string) $px['rotulo'],
			'nivel2' => isset( $px['nivel2'] ) && is_array( $px['nivel2'] ) ? $px['nivel2'] : array(),
		);
	}

	return $limpa;
}
}

/** O rótulo de uma página do eixo, ou o próprio slug quando ela não se anunciou. */
if ( ! function_exists( 'aquametria_casca_peixes_rotulo' ) ) {
function aquametria_casca_peixes_rotulo( $slug ) {
	$mapa = aquametria_casca_peixes();
	return isset( $mapa[ $slug ] ) ? $mapa[ $slug ]['rotulo'] : (string) $slug;
}
}

/**
 * As irmãs de uma página do eixo /peixes/: MESMA MÃE, no ar, no máximo quatro.
 *
 * Derivadas do mesmo mapa que serve a trilha, nunca digitadas — é a mesma
 * escolha do `aquametria_casca_irmas()` das calculadoras, e pelo mesmo motivo:
 * lista de irmãs escrita à mão envelhece no dia em que a próxima ficha nasce.
 * Página de nível 1 não tem irmã publicada (as outras seções não existem), e
 * devolver array() ali é o certo: cluster de um só não é cluster.
 */
if ( ! function_exists( 'aquametria_casca_irmas_de_peixes' ) ) {
function aquametria_casca_irmas_de_peixes( $slug ) {
	$mapa = aquametria_casca_peixes();
	if ( ! isset( $mapa[ $slug ] ) || '' === $mapa[ $slug ]['pai'] ) {
		return array();
	}
	$pai   = $mapa[ $slug ]['pai'];
	$irmas = array();
	foreach ( $mapa as $outro => $px ) {
		if ( $outro === $slug || $px['pai'] !== $pai ) {
			continue;
		}
		if ( '' === aquametria_casca_url_se_existir( $outro ) ) {
			continue;
		}
		$irmas[] = array( 'slug' => $outro, 'rotulo' => $px['rotulo'] );
		if ( count( $irmas ) >= 4 ) {
			break;
		}
	}
	return $irmas;
}
}

/**
 * O caminho completo de uma página do mapa: 'peixes/tetras' para `tetras`.
 *
 * Sobe a cadeia de mães do mapa de páginas. Slug que não está no mapa volta como
 * veio — é o caso das páginas de `conteudo/`, que o Sync cria na raiz. O teto de
 * cinco voltas existe para mapa com mãe circular não pendurar a página inteira.
 */
if ( ! function_exists( 'aquametria_casca_caminho_de_pagina' ) ) {
function aquametria_casca_caminho_de_pagina( $slug ) {
	$mapa = aquametria_casca_definicao_paginas();
	if ( ! isset( $mapa[ $slug ] ) ) {
		return $slug;
	}

	$partes = array( $slug );
	$sobe   = $mapa[ $slug ]['pai'];
	$voltas = 0;
	while ( '' !== $sobe && isset( $mapa[ $sobe ] ) && $voltas < 5 ) {
		array_unshift( $partes, $sobe );
		$sobe = $mapa[ $sobe ]['pai'];
		$voltas++;
	}

	return implode( '/', $partes );
}
}

/**
 * URL REAL da página, ou '' se ela não existe publicada no site.
 *
 * Duas vias, nesta ordem:
 *   1. o id do repositório, que o Sync grava em _aquametria_id. É a identidade
 *      canônica e sobrevive ao WordPress ter mudado o slug por conflito — quando
 *      o slug pedido já está ocupado, wp_insert_post acrescenta "-2" em silêncio
 *      e o log do Sync ainda diz "ok";
 *   2. o slug, para as páginas que não vieram do Sync.
 *
 * Devolve '' quando nenhuma via acha a página, e quem chama NÃO publica link.
 * Link do hub para página inexistente é 404 no ar: foi o defeito 2 de 08/09/2026.
 */
if ( ! function_exists( 'aquametria_casca_url_se_existir' ) ) {
function aquametria_casca_url_se_existir( $slug ) {
	$slug = sanitize_title( $slug );
	if ( '' === $slug ) {
		return '';
	}

	$achados = get_posts( array(
		'post_type'   => array( 'page', 'post' ),
		'post_status' => 'publish',
		'meta_key'    => '_aquametria_id',
		'meta_value'  => $slug,
		'numberposts' => 1,
	) );
	if ( $achados ) {
		return get_permalink( $achados[0] );
	}

	/* Segunda via: o CAMINHO INTEIRO, e não o slug solto.
	 *
	 * `get_page_by_path()` casa o caminho completo em tipo hierárquico, então
	 * pedir 'tetras' NUNCA acha /peixes/tetras/ — e foi exatamente isso que
	 * aconteceu no ar em 12/09/2026, na primeira leva do eixo: a bancada dava
	 * quatro degraus de trilha, todos linkados, e o site servia três, com o
	 * degrau do meio em texto. A bancada respondia a primeira via pelo mapa de
	 * slugs; no ar a primeira via não responde por página da casca, porque
	 * `_aquametria_id` é meta que o Sync grava em página de `conteudo/`, e as
	 * páginas do eixo são criadas pela casca. Duas metades lendo coisas
	 * diferentes, e só a conferência no HTML servido podia ver.
	 *
	 * O caminho sai do mapa de páginas (que é quem sabe quem é mãe de quem), e
	 * não de uma concatenação adivinhada. Página de raiz continua com o caminho
	 * igual ao slug, então nada muda para as quatro páginas antigas. */
	$pagina = get_page_by_path( aquametria_casca_caminho_de_pagina( $slug ), OBJECT, 'page' );
	if ( $pagina && 'publish' === $pagina->post_status ) {
		return get_permalink( $pagina );
	}

	/* Terceira via: o artigo-âncora, que é `post` e não `page`.
	 *
	 * Sem ela, as duas vias acima falhavam para os três artigos e quem chamasse
	 * aquametria_casca_url_pagina() caía no último recurso, que monta
	 * home_url('/<slug>/') — endereço que EXISTE e responde 301 para
	 * /2026/09/08/<slug>/, porque artigo tem permalink com data. Era o item 3 do
	 * despacho da Sentinela de 10/09/2026: cada calculadora linkava o artigo
	 * pareado por um salto de redirecionamento, e salto é orçamento de rastreamento
	 * gasto à toa — o recurso escasso de domínio novo (seção 14.1 do
	 * ARQUIPELAGO.md). Consertar aqui, e não no HTML de cada calculadora, é o que
	 * faz o próximo artigo nascer com link canônico sem ninguém lembrar disto.
	 *
	 * `name` em vez de get_page_by_path: para tipo não hierárquico o "caminho" é o
	 * post_name puro, e ser explícito evita depender desse detalhe. */
	$artigos = get_posts( array(
		'post_type'   => 'post',
		'post_status' => 'publish',
		'name'        => $slug,
		'numberposts' => 1,
	) );
	if ( $artigos ) {
		return get_permalink( $artigos[0] );
	}

	return '';
}
}

/**
 * Link de texto que só vira <a> se a página existir. Sem página, sai o rótulo
 * sozinho — nunca um endereço que devolve 404.
 */
if ( ! function_exists( 'aquametria_casca_link_html' ) ) {
function aquametria_casca_link_html( $slug, $rotulo ) {
	$url = aquametria_casca_url_se_existir( $slug );
	if ( '' === $url ) {
		return '<span class="aqm-sem-link">' . esc_html( $rotulo ) . '</span>';
	}
	return '<a href="' . esc_url( $url ) . '">' . esc_html( $rotulo ) . '</a>';
}
}

if ( ! function_exists( 'aquametria_casca_url_pagina' ) ) {
function aquametria_casca_url_pagina( $slug ) {
	$url = aquametria_casca_url_se_existir( $slug );
	if ( '' !== $url ) {
		return $url;
	}
	/* Último recurso, só para não devolver href vazio a quem ainda chama isto
	   direto. Quem publica link novo deve usar aquametria_casca_link_html(). */
	return home_url( '/' . sanitize_title( $slug ) . '/' );
}
}

/* ---------------------------------------------------------------------------
 * 1b. Apelidos de endereço — o 404 que o visitante não deveria ver
 *
 * Defeito de 08/09/2026: o Raphael pediu /calculadora-de-aquecedor-de-aquario/
 * e levou 404. Não era slug trocado — a página da C5 está publicada em
 * /calculadora-de-potencia-do-aquecedor/ e o hub aponta certo. O endereço
 * pedido é o que qualquer pessoa (e qualquer buscador) ADIVINHA a partir do
 * nome da calculadora, e adivinhar errado não pode custar um 404.
 *
 * Cada apelido plausível redireciona 301 para a página canônica. 301 porque a
 * URL certa é a canônica e é ela que deve acumular sinal de busca; o apelido é
 * porta de entrada, nunca endereço publicado.
 *
 * Trava: o redirecionamento SÓ acontece se a página de destino existir
 * publicada de verdade (mesma verificação do hub). Sem destino, o 404 segue —
 * redirecionar para outro 404 é pior que o 404 original.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_casca_apelidos' ) ) {
function aquametria_casca_apelidos() {
	$mapa = array(
		/* C1 — litragem */
		'calculadora-de-litros'                          => 'calculadora-de-litragem',
		'calculadora-de-volume'                          => 'calculadora-de-litragem',
		'calculadora-de-volume-de-aquario'               => 'calculadora-de-litragem',
		'calculadora-de-litragem-de-aquario'             => 'calculadora-de-litragem',
		'quantos-litros-tem-meu-aquario'                 => 'calculadora-de-litragem',
		/* C3 — vazão */
		'calculadora-de-vazao'                           => 'calculadora-de-vazao-do-filtro',
		'calculadora-de-vazao-de-filtro'                 => 'calculadora-de-vazao-do-filtro',
		'calculadora-de-filtro'                          => 'calculadora-de-vazao-do-filtro',
		'calculadora-de-filtro-de-aquario'               => 'calculadora-de-vazao-do-filtro',
		'calculadora-de-turnover'                        => 'calculadora-de-vazao-do-filtro',
		/* C5 — aquecedor */
		'calculadora-de-aquecedor'                       => 'calculadora-de-potencia-do-aquecedor',
		'calculadora-de-aquecedor-de-aquario'            => 'calculadora-de-potencia-do-aquecedor',
		'calculadora-de-potencia-do-aquecedor-de-aquario' => 'calculadora-de-potencia-do-aquecedor',
		'calculadora-de-watts'                           => 'calculadora-de-potencia-do-aquecedor',
		'calculadora-de-watts-do-aquecedor'              => 'calculadora-de-potencia-do-aquecedor',
		/* C12 — mídia filtrante */
		'calculadora-de-midia'                           => 'calculadora-de-midia-filtrante',
		'calculadora-de-midia-biologica'                 => 'calculadora-de-midia-filtrante',
		'calculadora-de-midia-filtrante-de-aquario'      => 'calculadora-de-midia-filtrante',
		/* C15 — iluminação */
		'calculadora-de-luz'                             => 'calculadora-de-iluminacao',
		'calculadora-de-lumens'                          => 'calculadora-de-iluminacao',
		'calculadora-de-iluminacao-de-aquario'           => 'calculadora-de-iluminacao',
		'calculadora-de-iluminacao-de-aquario-plantado'  => 'calculadora-de-iluminacao',
	);

	return apply_filters( 'aquametria_apelidos_de_pagina', $mapa );
}
}

/**
 * Slug canônico de um caminho pedido, ou '' se ele não for apelido conhecido.
 * Isolada da requisição de propósito, para o teste poder exercitá-la sozinha.
 */
if ( ! function_exists( 'aquametria_casca_apelido_para_slug' ) ) {
function aquametria_casca_apelido_para_slug( $caminho ) {
	$caminho = trim( (string) $caminho );
	$caminho = trim( $caminho, '/' );
	if ( '' === $caminho || false !== strpos( $caminho, '/' ) ) {
		return '';
	}

	$caminho = sanitize_title( $caminho );
	$mapa    = aquametria_casca_apelidos();

	return isset( $mapa[ $caminho ] ) ? $mapa[ $caminho ] : '';
}
}

/**
 * Caminho pedido nesta requisição, sem a superglobal de servidor (fase 4b).
 * $wp->request já vem sem barra inicial, sem barra final e sem query string.
 */
if ( ! function_exists( 'aquametria_casca_caminho_pedido' ) ) {
function aquametria_casca_caminho_pedido() {
	if ( isset( $GLOBALS['wp'] ) && is_object( $GLOBALS['wp'] ) && isset( $GLOBALS['wp']->request ) ) {
		return (string) $GLOBALS['wp']->request;
	}

	$atual = add_query_arg( array() );
	$atual = strtok( (string) $atual, '?' );

	return trim( (string) $atual, '/' );
}
}

if ( ! function_exists( 'aquametria_casca_redirecionar_apelido' ) ) {
function aquametria_casca_redirecionar_apelido() {
	if ( ! is_404() ) {
		return;
	}

	$destino = aquametria_casca_apelido_para_slug( aquametria_casca_caminho_pedido() );
	if ( '' === $destino ) {
		return;
	}

	$url = aquametria_casca_url_se_existir( $destino );
	if ( '' === $url ) {
		return;
	}

	wp_safe_redirect( $url, 301 );
	exit;
}
}

add_action( 'template_redirect', 'aquametria_casca_redirecionar_apelido' );

/* ---------------------------------------------------------------------------
 * 2. Marca, menu e rodapé
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_casca_logo_svg' ) ) {
function aquametria_casca_logo_svg() {
	$svg  = '<svg viewBox="0 0 40 48" width="30" height="36" role="img" aria-label="Aquametria" focusable="false">';
	$svg .= '<path d="M9 4h22v34a5 5 0 0 1-5 5H14a5 5 0 0 1-5-5z" fill="#FFFFFF" stroke="#0D1B22" stroke-width="2.6" stroke-linejoin="round"/>';
	$svg .= '<path d="M11.6 25h16.8v13a3.4 3.4 0 0 1-3.4 3.4H15a3.4 3.4 0 0 1-3.4-3.4z" fill="#0E7C8C"/>';
	$svg .= '<path d="M11.6 25h16.8" stroke="#0E7C8C" stroke-width="2.6" stroke-linecap="round"/>';
	$svg .= '<g stroke="#0D1B22" stroke-width="1.8" stroke-linecap="round">';
	$svg .= '<path d="M12 10h9"/><path d="M12 14.5h5.5"/><path d="M12 19h9"/>';
	$svg .= '</g>';
	$svg .= '<g stroke="#F4F7F7" stroke-width="1.8" stroke-linecap="round">';
	$svg .= '<path d="M14 30h9"/><path d="M14 34.5h5.5"/>';
	$svg .= '</g>';
	$svg .= '<path d="M7.4 4h25.2" stroke="#0D1B22" stroke-width="2.6" stroke-linecap="round"/>';
	$svg .= '</svg>';

	return $svg;
}
}

if ( ! function_exists( 'aquametria_casca_marca_html' ) ) {
function aquametria_casca_marca_html() {
	static $ja_impressa = false;
	if ( $ja_impressa ) {
		return '';
	}
	$ja_impressa = true;

	return '<a class="aqm-marca" href="' . esc_url( home_url( '/' ) ) . '" rel="home">'
		. aquametria_casca_logo_svg()
		. '<span class="aqm-wordmark">Aquametria</span>'
		. '</a>';
}
}

/**
 * O menu. Abaixo de 782 px ele vira sanfona atrás de um botão; acima, é a mesma
 * fileira de links de sempre.
 *
 * Três decisões, e nenhuma delas é enfeite:
 *
 *   1. Os links saem SEMPRE no HTML servido, dentro de <nav>. O botão não gera
 *      link nenhum: ele só mostra e esconde o que já está lá. É o que faz o menu
 *      continuar existindo para quem lê a página sem executar JavaScript — o
 *      crawler de IA, que é regra de primeira classe do projeto, e o visitante
 *      cujo script não carregou.
 *   2. Quem esconde a lista no celular é o seletor [data-aqm-menu], e esse
 *      atributo quem põe é o JavaScript do rodapé. Sem JavaScript o atributo não
 *      existe, a regra não casa e o menu fica visível como lista, que é
 *      exatamente o que o site fazia antes desta versão. Esconder por padrão e
 *      contar com o script para revelar seria trocar um defeito por outro pior.
 *   3. O id é contado, porque o filtro render_block pode trocar mais de um bloco
 *      core/navigation na mesma página, e aria-controls que aponta para um id
 *      repetido não controla coisa nenhuma.
 */
if ( ! function_exists( 'aquametria_casca_nav_html' ) ) {
function aquametria_casca_nav_html() {
	static $quantos = 0;
	$quantos++;
	$id = 'aqm-nav-lista' . ( $quantos > 1 ? '-' . $quantos : '' );

	/* Rótulo de menu é texto de tela, então fala a língua do VOZ.md: "Metodologia"
	   é como a fábrica chama a página, não como a pessoa pediria para ver o
	   critério. O slug — e portanto a URL — não muda (seção 12.1 do contrato). */
	$itens = array(
		'calculadoras' => 'Calculadoras',
		/* "Peixes" é curto de propósito, e é a ÚNICA superfície onde o nome
		   desta página encurta: o menu tem de caber no celular, e o VOZ.md pede
		   menu curto. Quem responde pelo nome da página é a trilha, e lá ela se
		   chama "Quanto espaço cada peixe pede", igual ao H1. É o mesmo
		   precedente do rodapé, que diz "Divulgação de afiliados" onde a trilha
		   diz "Como a Aquametria ganha dinheiro". */
		'peixes'       => 'Peixes',
		'metodologia'  => 'Como a gente calcula',
		'sobre'        => 'Sobre',
	);

	$html  = '<div class="aqm-nav-caixa">';
	$html .= '<button type="button" class="aqm-nav-botao" aria-expanded="false" aria-controls="' . esc_attr( $id ) . '">';
	$html .= '<span class="aqm-nav-tracos" aria-hidden="true"></span>';
	$html .= '<span class="aqm-nav-rotulo">Menu</span>';
	$html .= '</button>';
	$html .= '<nav class="aqm-nav" id="' . esc_attr( $id ) . '" aria-label="Navegação principal"><ul>';
	foreach ( $itens as $slug => $rotulo ) {
		$html .= '<li>' . aquametria_casca_link_html( $slug, $rotulo ) . '</li>';
	}
	$html .= '</ul></nav>';
	$html .= '</div>';

	return $html;
}
}

if ( ! function_exists( 'aquametria_casca_rodape_impresso' ) ) {
/**
 * Marca e consulta se o rodapé da Aquametria já saiu nesta requisição.
 * Evita rodapé duplicado quando o filtro render_block já trocou a template part.
 */
function aquametria_casca_rodape_impresso( $marcar = false ) {
	static $impresso = false;
	if ( $marcar ) {
		$impresso = true;
	}
	return $impresso;
}
}

if ( ! function_exists( 'aquametria_casca_rodape_html' ) ) {
function aquametria_casca_rodape_html() {
	aquametria_casca_rodape_impresso( true );

	$html  = '<footer class="aqm-rodape"><div class="aqm-rodape-interno">';
	$html .= '<p class="aqm-tagline">' . esc_html( AQUAMETRIA_CASCA_TAGLINE ) . '</p>';
	$html .= '<p class="aqm-prova">Todo número publicado aqui cita a fonte — manual de fabricante, norma técnica ou fonte brasileira nomeada — e leva a data em que foi verificado. Quando as fontes discordam, a Aquametria publica a divergência com a atribuição de cada extremo, nunca a média. Onde não há fonte aceitável, a página diz por que não publica número.</p>';
	$html .= '<p>' . aquametria_casca_link_html( 'metodologia', 'Como a gente calcula' )
		. ' · ' . aquametria_casca_link_html( 'divulgacao-de-afiliados', 'Divulgação de afiliados' )
		. ' · ' . aquametria_casca_link_html( 'sobre', 'Sobre' )
		. ' · Aquametria ' . esc_html( date_i18n( 'Y' ) ) . '</p>';
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
		return aquametria_casca_marca_html();
	}
	if ( 'core/navigation' === $nome ) {
		return aquametria_casca_nav_html();
	}
	// A tagline padrão do WordPress ("Just another WordPress site") é resíduo do
	// tema; a tagline da Aquametria mora no rodapé.
	if ( 'core/site-tagline' === $nome ) {
		return '';
	}
	// Em tema de blocos o rodapé é uma template part renderizada DENTRO do fluxo
	// do conteúdo. Trocar a saída dela aqui é o que impede os dois rodapés
	// empilhados (o do tema, com o crédito "Criado com WordPress", e o nosso).
	if ( 'core/template-part' === $nome ) {
		$parte = isset( $bloco['attrs']['slug'] ) ? $bloco['attrs']['slug'] : '';
		if ( 'footer' === $parte || 'rodape' === $parte ) {
			return aquametria_casca_rodape_html();
		}
	}
	return $conteudo;
}, 10, 2 );

// Rede de segurança: se o tema NÃO usa template part de rodapé (ou o filtro não
// pegou), o rodapé sai aqui. Se já saiu no lugar da template part, não repete.
add_action( 'wp_footer', function () {
	if ( aquametria_casca_rodape_impresso() ) {
		return;
	}

	echo aquametria_casca_rodape_html(); // markup próprio, já escapado campo a campo
}, 20 );

/* ---------------------------------------------------------------------------
 * 2b. Ícone do site
 *
 * O WordPress imprime o ícone dele em wp_head na prioridade 99, e sem tirar
 * aquele de lá o site sairia com dois — a aba escolheria um, o iOS outro. Aqui
 * o ícone é o recipiente graduado da marca, viajando dentro do snippet como
 * data URI: nada sobe para a biblioteca de mídia.
 *
 * O desenho não se edita à mão neste arquivo: ele é gerado por
 * ferramentas/gerar-favicon.php, entre os marcadores abaixo, pelo mesmo motivo
 * que o catálogo de produtos é gerado dentro das calculadoras — desenho mantido
 * em dois lugares diverge em silêncio.
 * ------------------------------------------------------------------------- */

/* FAVICON-INICIO — gerado por ferramentas/gerar-favicon.php, nao edite a mao */
if ( ! defined( 'AQUAMETRIA_CASCA_ICONE_SVG' ) ) {
	define( 'AQUAMETRIA_CASCA_ICONE_SVG', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="6" fill="#0D1B22"/><rect x="7" y="4" width="18" height="1.8" rx=".9" fill="#FFFFFF"/><path d="M9 6.6h14V24a4 4 0 0 1-4 4h-6a4 4 0 0 1-4-4z" fill="#FFFFFF"/><path d="M9 17.4h14V24a4 4 0 0 1-4 4h-6a4 4 0 0 1-4-4z" fill="#0E7C8C"/><g fill="#0D1B22"><rect x="11.6" y="9.6" width="8.8" height="1.8" rx=".9"/><rect x="11.6" y="13.2" width="5.4" height="1.8" rx=".9"/></g></svg>' );
	define( 'AQUAMETRIA_CASCA_ICONE_PNG_180', 'iVBORw0KGgoAAAANSUhEUgAAALQAAAC0CAMAAAAKE/YAAAAAkFBMVEX////7+/sOfo8MeIkMeov9/f0OfI8OfI0MGiAMGiIOHCJQWmDV19mBiYuxtbfv8fHh4+Pv7/H5+fmboaPb3d3j5eXT19edo6V+h4sOeosMdoUMdIVIVFggLDQMbHoMTFhKVFoMLjYMSFIMICgMOkQMHCJcZmoMXGgMTloMaHYMIioMcH4gLDIOHCReZmwMXGo78/qxAAAACXBIWXMAAA7EAAAOxAGVKw4bAAALvElEQVR42u1di5LsphGFuVDAdSUVrxPn/U4cO3aS//+7jMTrdAOagZV6aquudmclIZ2FgabpxylJ+eDvvyFsu7jfj+o+XYol2x35xpCg8ngVyP8JGYjFGZxLA7n6ArzydQtkl0/IaSrslEnilc9fvn7bOog+XijfNF+Hw1fgVR2xUPehDqRnxXW0+IjL4VU7QoEPER+/Zi+NVziZ85RNowIToU5oX67CJWG86o6Dp6Plu6VseAXximqhjmzRGjr/XR6vsl4JWWoCVUqBqqlQywLRS5J4le4LiIDjdBYCFvG7pfGKr0JPbL4rpoJ4mIie4uv6WZQ7mzZsIsnhFZWyLF0BT4P3sERR8fKvwKtmXMBYSZ1wMNU74yqAp+LB/o8P3bH0zUgL4xX+H2K/+kZD4uSByuXxypMv7kGEPJzWIi5gr8CrCePLDxcpYbyq7g7YLL4VsZC/KXhB1F2SwyuPMpV3dQDLshpCXahAHv0r8AqsV1jwA+jTqlvLfYGsveJ4dWRaDa747oosiO+7W92J8Ber9s2m/X4cPxZOx8UP8I/qr6KtAsQdYGAC0THb8b2u+6+OleqtGq2sjsd6q/t+ul+KrdL7nXY/3QrsY/yvDuv3ecpWHzEE4piFxoX/5v7P73Xsf+x2rNLx9nmzudHpnvuZ3k/u7dE2HT3E/3RQP7ZO8bgJX0bzuMBY6rS3tSgd6nrXQDyO8Qf1k2XcM9OQuPA17vCZyWQ63noy1w2iqnJb4oWOTPfx4/qpTMOAhCpCoIPSSOwSuf9oFYc2tipvUTy2S1F6QZJVLnuIH9dfWhdNUw9aPTD7BUzD1Be6dsteqc4zLDVG5amWmqjeQEoe4g/qh7BDINqDGY8exevXVFLjMZn9TER1lQPbSnoX/8eD+pk9HRqZ9r24A5lXlk61rVJdZZoJsWpPu/hfHNYPpypUf7drPFaB+oOOQ556566JN9W1d6nWseatyCZ1vQnC2962tySxD/CP6vfMNO0b3Qd2ZKDRFWH80zLd+njQJ8L4p7UHzl5wk/wr8M/qaaInwU3yr8DDisgc4/7KzlZXjOTL4Z+2PaD0ZNtjuv5Bdov0g+cg2gaVNFjHprblhzSa4afr9zQ+TcwSGleDeIWqq1rSz1YpslBE87p2fr2ua2Mzfrr+cVB97O976E5NV2bSy83Gejjjp+sPw/SFH0bbPLRHN5ZFabSmxe0izxr9fP1egXsQeg5D1UdFQ+1mmY725+6gRJ9Kq2yS5sU8HhezVIEdCvjp+r3CZQhz0iRq6TFYErD/iAZJUmKtIiZRnonW8jm53zVd/1KEqQpB8gGZHFjbEQ8FHgHFL0SYeACza8BQZWSrL4Uq1zYhhP5EVAw/Xb9fiZpmxbyblpss54iA0hZM02iFpr9W5562luGXoqbT8WEw5LXFnka/ivS0bXwBwC/Epxci8eB5ZOOfzsmOj8VWRMQvZAL6+UWmewJRRHmB3tzWqOpSYEYVfbbrtBiWyd5rEQ7N8NP15+xWNv+K8ZjDmznGWYOwm56ugYKskFWOfsXWJG1dVnCd5CdHFxA/XT9kAjqxzYFjaVuFoFp1YY8cW8RM17+UsbVtIHSo5nobwy9kbGGJbNk5Df0iBuKTkq2Li34an6MhgJ+uP6hAcgXet6dl9cy6Mq95UWXdK57CF12d8dP15/h0f0UaBLXB3tjjF5N4y/DT9Q+YNWEU4fE4EVPlnyfx/2X46fqXOExg3uXhFcWD7ZFTB7DQB8io5qs+TUSVjA7782m8JXg7jYfs1gPyE1xlelYcv8SABLt+81b+M4n/juEXGJB+ftu9JG333/v2Ngl/Y/j5BqgBiyEw2kAAfW+zUCfT9Ksp/C8tw0/X79UCfzmZlOhuPY23JYvRuFvX8qfRiKcRLmaHWNsLKVmGl+FP787ULpN7NnMXzWxX663z9it70T4SuoQS4s0ML8OfZrPf0mhCumhrHrGadBajfO/QHgv8ZRYh0l1LuRd4OowwXcyfTplvrdM+y8Iea8qZQf1ms2rL0hGdsOimA16GP01jvFYXZZDDS0SplaMcx7EML8OfVl2+hlWP/Cvbd9Fk+NNPhXrVO0O9Z/OnY9ATo6bbTw2PYq4+Rw+som444GX40yUWUH3EVBKn2h4dK9M05WNtSs+W9ha8DH+68ca/HeGv8sYX+MuWJljsEZ7k99m0VU1Y7EL+NIjnppZ/c4T/OuYHCglEKyLeG16GP83Wu2O87hPfnsafxZ+einpeEjV9f3z6GH9JfPr9mYBj/EWZgGn+MtNePzvCfz1Yv9uo6cX8aZ7d+mqM//aa7NYCfxnTWZE+OsB/rgv3rpTzMk/xMvxpVQxPm1NYlhgcFmxUW3h3OQugGV6GP93mxgcia4c5Aua5XMefxlDvmfzp6fon+NM1rX4yf3q6/uf503D1ZP70dP0flMP0JH+ay/SJ/Onp+v0KL+9k/vQCL2+BgXgyf3qBAbnA9TyZP73CNX2WP01JKifyp6frn+FPe2aansWfnq5/iT/dpuztcW5/UGobb/xC/rS7b2b/GHPf3z/7mcmlLpcaV4voIeJl+NO1hcaY9EltN6TR2/Gn1EoAMbwMfzp2UWxZ2VLXxkvpQmqVc+UGBzdlvAx/uvScc7V3iRwYIi38w/Ay/GmU3OZw0DrnyM0IkuFP0zZg/dDCOg6m12jAy/CnnbsZR5RCPL2RbsXOLwoj3UzwMvzpWN8NO28749LabLSHC16GP21oO5g8u7GY1zFAvAx/2hC9ZkDROVZC9KFDAOBl+NMosUSDJEk1RY5NmY+xi00j8WbvaQH+dBUCU1YLlAPT09MOVhqKl+FP1yWYGRtE7ZnRRHQML8OfLq2E5dhVW8IZg2ZJOaJXK16GP+2a7gVjz4E8sz4GlYd4Gf60IdPMtXNyoAmZLLHF5WL+dF6gN8MTdVfSaQ7VocNTMO8AL8OfpooWzczSmvwt8gpe3AIEpUMZ/nQyMlxXcPF0L7lRYa5GSi6S4U8zMU32T1/Nle3WrP3QaAH+dBlvXFyqcBBHoM46U38pXoY/TXStA7VrQG0TOyOpuZ6udkaGP40rIWt4a/xxBc3sleSNX8+fZlaz6dmffN3ehBrDB60TcDF/msQAag+bYuKBEMNNztV4A16S4U+7onMdEWLHDQ28nq+a+o0SXoY/bYbay7iRILuuE5PFQ4A/jXY903Gl0JHedrXcUb8A4h7X8qfN+7ZP7FyGP43TzAysVK6UnWNxSdMxTa/kT1d1Qdwtgwqk7qv/bUBwOu7WtfxpNwyL9QNPLKRk3DAsdiF/moZLDQ0MGB486NxL8TL86ddrjwX+tKl2JjEybty87q/uhuFl+NPVv+pKSPp8GsoP28vwp19veyzwp90TAchb38rruWgy/Onf9gznGzWgb8XLug1Cve441Hs2f5q44VmvOUgXoVLrxBcYXoY/XfNwmNYiJRhHMMRHNPwOJ8Of/v5Ub/x/Mvzpf7aRLjQwaFoOQv8slpbu/rvQ86dds2o7kG1XC6EAAqWO4KWeP93quU4aBjMBfYMp7qSeP/3vE6OmfxJ7/vSJ8Wm550//eFom4HeCz5/uREpJevB2EGEiFp/o86dPym79WfT508R1ZbFIGoRMy7pzdRmEfIvs86dh7SaclJqfqOc0GZYjqDEJIPv86a7FRhdsM8wRxO2v1z9/GkkNoYh1ZiE0BvQwfVFkeljRFfzpPBkbthgIBg3W1BUc5Ll92uaV/GlMc+VIl3PEZezQERhLy4TmrVaX8qfr/vfLHKZP3ZeFXcifRtX5L8NMUxJC4HGPLNM/BAhlyPCn6XNJ/zHNy/vbu59resYTYKcYkGc8QfZjPqt3nj/N3scij1/hT1Pf5wX4L8+f/vL86S/Pn/6gz59uDQZh/Ap/2o/SUFL4Ff50eyyMX+FPh2deynglfoU/3Q9QCOJX+NPkTXuvwK/wp1Hi/CvwH/MNZwv86boE87cHCuE/6lv7PuD7ET/kmygX+NOVMRxG+clr8Sv86d6Lf0Xx/wfrq4v3M/HvsgAAAABJRU5ErkJggg==' );
	define( 'AQUAMETRIA_CASCA_ICONE_PNG_32', 'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAElBMVEX9/f0MeosMGiDX2dkMangyPkRE6xmSAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAATklEQVQoz2NQQgMMZAowQAETVEAZJsCKUwtUCTNJAiBSAa8AMWYoowowKSmQ5g4VQUdBRxFBESQBMKCxgBJEQAiPgCJYADmiVKAmkBW3AE2xNWcHmXfXAAAAAElFTkSuQmCC' );
}
/* FAVICON-FIM */

remove_action( 'wp_head', 'wp_site_icon', 99 );

add_action( 'wp_head', function () {
	if ( ! defined( 'AQUAMETRIA_CASCA_ICONE_SVG' ) ) {
		return;
	}

	echo '<link rel="icon" type="image/svg+xml" href="' . esc_attr( 'data:image/svg+xml,' . rawurlencode( AQUAMETRIA_CASCA_ICONE_SVG ) ) . '">' . "\n";
	// Segunda linha para quem não desenha SVG na aba: o mesmo desenho, em PNG de
	// 32 px. 'alternate icon' é o rel que o navegador só usa quando desiste do
	// primeiro.
	echo '<link rel="alternate icon" type="image/png" sizes="32x32" href="' . esc_attr( 'data:image/png;base64,' . AQUAMETRIA_CASCA_ICONE_PNG_32 ) . '">' . "\n";
	// O iOS não aceita SVG neste rel, e ele aplica a própria máscara de canto —
	// por isso o PNG é quadrado, em sangria, sem arredondamento por baixo.
	echo '<link rel="apple-touch-icon" sizes="180x180" href="' . esc_attr( 'data:image/png;base64,' . AQUAMETRIA_CASCA_ICONE_PNG_180 ) . '">' . "\n";
	echo '<meta name="theme-color" content="#0D1B22">' . "\n";
}, 5 );

/* ---------------------------------------------------------------------------
 * 3. Tipografia e paleta por cima do tema ativo
 * ------------------------------------------------------------------------- */

add_action( 'wp_head', function () {
	$fontes = 'https://fonts.googleapis.com/css2?family=Chivo:wght@400;700;900&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap';

	echo '<link rel="preconnect" href="https://fonts.googleapis.com">' . "\n";
	echo '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' . "\n";
	echo '<link rel="stylesheet" href="' . esc_url( $fontes ) . '">' . "\n";

	$css = <<<'CSS'
:root{
--aqm-tinta:#0D1B22;--aqm-lamina:#0E7C8C;--aqm-papel:#F4F7F7;--aqm-superficie:#FFFFFF;
--aqm-traco:#DDE5E6;--aqm-legenda:#5C7075;--aqm-alerta:#B5762A;
--aqm-display:"Chivo","Trebuchet MS",Arial,sans-serif;
--aqm-texto:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;
--aqm-mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}
body{
--wp--preset--color--base:#F4F7F7;--wp--preset--color--contrast:#0D1B22;
--wp--preset--color--primary:#0E7C8C;--wp--preset--color--secondary:#5C7075;
--wp--preset--font-family--body:var(--aqm-texto);
--wp--preset--font-family--heading:var(--aqm-display);
}
html body{background-color:var(--aqm-papel);color:var(--aqm-tinta);font-family:var(--aqm-texto);font-size:17px;line-height:1.65;-webkit-font-smoothing:antialiased;}
body h1,body h2,body h3,body h4,body h5,body h6{font-family:var(--aqm-display);color:var(--aqm-tinta);line-height:1.2;letter-spacing:-0.015em;}
body h1{font-weight:900;}
body a{color:var(--aqm-lamina);text-underline-offset:2px;}
body a:hover{color:var(--aqm-tinta);}
body code,body kbd,body samp,body pre,body .aqm-num{font-family:var(--aqm-mono);font-variant-numeric:tabular-nums;}
body .wp-block-button__link,body button,body input[type=submit]{background-color:var(--aqm-lamina);color:var(--aqm-superficie);border:0;border-radius:2px;font-family:var(--aqm-texto);font-weight:600;}
body hr,body .wp-block-separator{border-color:var(--aqm-traco);color:var(--aqm-traco);}
body table{border-collapse:collapse;}
body table th,body table td{border:1px solid var(--aqm-traco);padding:.5rem .7rem;text-align:left;}
body table th{background:var(--aqm-superficie);font-family:var(--aqm-display);font-weight:700;}
body header .wp-block-group,body .wp-block-template-part header{background:var(--aqm-superficie);}
.aqm-marca{display:inline-flex;align-items:center;gap:.6rem;text-decoration:none;}
.aqm-marca:hover{text-decoration:none;}
.aqm-marca svg{display:block;flex:0 0 auto;}
.aqm-wordmark{font-family:var(--aqm-display);font-weight:900;font-size:1.5rem;letter-spacing:-0.03em;color:var(--aqm-tinta);line-height:1;}
.aqm-nav ul{display:flex;flex-wrap:wrap;gap:1.4rem;list-style:none;margin:0;padding:0;}
.aqm-nav li{margin:0;}
.aqm-nav a{font-family:var(--aqm-texto);font-weight:600;font-size:.95rem;color:var(--aqm-tinta);text-decoration:none;padding-bottom:.15rem;border-bottom:2px solid transparent;}
.aqm-nav a:hover{color:var(--aqm-lamina);border-bottom-color:var(--aqm-lamina);}
.aqm-nav-caixa{position:relative;}
/* O botao do menu so aparece no celular, e so quando ha JavaScript para ele
   comandar (o atributo data-aqm-menu e posto pelo script do rodape). */
.aqm-nav-botao{display:none;align-items:center;gap:.55rem;background:transparent;color:var(--aqm-tinta);border:1px solid var(--aqm-traco);border-radius:2px;padding:.5rem .75rem;font-family:var(--aqm-texto);font-weight:600;font-size:.92rem;line-height:1;cursor:pointer;}
.aqm-nav-botao:hover{border-color:var(--aqm-lamina);color:var(--aqm-lamina);}
.aqm-nav-tracos{position:relative;display:block;width:1.05rem;height:2px;background:currentColor;border-radius:2px;}
.aqm-nav-tracos::before,.aqm-nav-tracos::after{content:"";position:absolute;left:0;width:100%;height:2px;background:currentColor;border-radius:2px;}
.aqm-nav-tracos::before{top:-.36rem;}
.aqm-nav-tracos::after{top:.36rem;}
.aqm-nav-botao:focus-visible,.aqm-nav a:focus-visible,.aqm-marca:focus-visible{outline:2px solid var(--aqm-lamina);outline-offset:3px;}
.aqm-bloco{max-width:52rem;}
.aqm-linha-mestra{font-family:var(--aqm-display);font-size:1.35rem;line-height:1.35;font-weight:700;margin:0 0 .8rem;}
.aqm-abertura p{margin:0 0 .7rem;}
.aqm-secao{margin:2.4rem 0 0;}
.aqm-secao h2{margin:0 0 .6rem;font-size:1.35rem;}
.aqm-secao h3{margin:1.4rem 0 .4rem;font-size:1.08rem;}
.aqm-cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(17rem,1fr));gap:1rem;margin:1.4rem 0 0;padding:0;list-style:none;}
.aqm-card{background:var(--aqm-superficie);border:1px solid var(--aqm-traco);border-radius:3px;padding:1.1rem 1.2rem;display:flex;flex-direction:column;gap:.5rem;margin:0;}
.aqm-card h3{font-family:var(--aqm-display);font-size:1.05rem;margin:0;line-height:1.25;}
.aqm-card p{margin:0;color:var(--aqm-legenda);font-size:.93rem;line-height:1.5;}
.aqm-codigo{font-family:var(--aqm-mono);font-size:.72rem;letter-spacing:.1em;color:var(--aqm-legenda);}
/* A pergunta que abre a home e o botao dela. Sem gradiente e sem sombra
   colorida (secao 6 do ARQUIPELAGO.md): quem separa e a linha de 1px. */
.aqm-pergunta{border-bottom:1px solid var(--aqm-traco);padding-bottom:1.4rem;}
.aqm-acao-grande{margin:1.1rem 0 0;}
.aqm-acao-grande a{display:inline-block;background:var(--aqm-lamina);color:var(--aqm-superficie);font-family:var(--aqm-texto);font-weight:600;text-decoration:none;border:1px solid var(--aqm-lamina);border-radius:2px;padding:.7rem 1.15rem;}
.aqm-acao-grande a:hover{background:var(--aqm-tinta);border-color:var(--aqm-tinta);}
.aqm-acao-grande a:focus-visible{outline:2px solid var(--aqm-tinta);outline-offset:3px;}
/* Prateleira de guias: lista de verdade, um link por titulo. */
.aqm-guias{margin:1.2rem 0 0;padding:0;list-style:none;display:grid;gap:1.1rem;}
.aqm-guia{margin:0;padding:0 0 1.1rem;border-bottom:1px solid var(--aqm-traco);}
.aqm-guia:last-child{border-bottom:0;padding-bottom:0;}
.aqm-guia h3{font-family:var(--aqm-display);font-size:1.05rem;margin:0 0 .35rem;line-height:1.3;}
.aqm-guia h3 a{color:var(--aqm-tinta);text-decoration:none;border-bottom:2px solid var(--aqm-lamina);}
.aqm-guia h3 a:hover{color:var(--aqm-lamina);}
.aqm-guia p{margin:0;color:var(--aqm-legenda);font-size:.93rem;line-height:1.55;}
.aqm-acao{margin-top:auto;padding-top:.3rem;}
.aqm-acao a{font-weight:600;text-decoration:none;border-bottom:2px solid var(--aqm-lamina);}
.aqm-sem-link{color:var(--aqm-legenda);}
.aqm-rodape .aqm-sem-link{color:var(--aqm-traco);}
.aqm-tag{display:inline-block;font-family:var(--aqm-mono);font-size:.68rem;letter-spacing:.08em;text-transform:uppercase;color:var(--aqm-alerta);border:1px solid var(--aqm-alerta);border-radius:2px;padding:.15rem .4rem;}
.aqm-tag-viva{color:var(--aqm-lamina);border-color:var(--aqm-lamina);}
.aqm-nota{border-left:3px solid var(--aqm-lamina);background:var(--aqm-superficie);padding:.85rem 1rem;color:var(--aqm-legenda);font-size:.95rem;margin:1.2rem 0 0;}
.aqm-nota strong{color:var(--aqm-tinta);}
.aqm-lista{margin:.6rem 0 0;padding-left:1.1rem;}
/* Citação em bloco vinda do Markdown do repositório (conversor do Sync 1.1.2):
   é onde mora fórmula e regra citada, então sai em monoespaçada. */
.aqm-citacao{border-left:3px solid var(--aqm-lamina);background:var(--aqm-superficie);margin:1.2rem 0;padding:.9rem 1.1rem;font-size:.95rem;line-height:1.6;}
.aqm-citacao p{margin:0 0 .5rem;font-family:var(--aqm-mono);}
.aqm-citacao p:last-child{margin-bottom:0;}
.aqm-tabela{margin:1.2rem 0;}
.aqm-lista li{margin:0 0 .45rem;}
.aqm-quadro{width:100%;margin:1rem 0 0;font-size:.93rem;}
.aqm-quadro td:first-child{font-family:var(--aqm-mono);font-size:.85rem;white-space:nowrap;}
.aqm-quadro td:last-child{text-align:right;font-family:var(--aqm-mono);}
/* A trilha (seção 16.3 do ARQUIPELAGO.md). Ela ROLA na horizontal dentro da
   própria caixa quando não cabe — é o único jeito de uma trilha longa não
   empurrar a largura da página no celular, e a página inteira nunca rola. */
.aqm-trilha{font-family:var(--aqm-texto);font-size:.82rem;line-height:1.5;margin:0 0 1.1rem;max-width:100%;overflow-x:auto;}
.aqm-trilha ol{display:flex;flex-wrap:nowrap;align-items:center;gap:.3rem;list-style:none;margin:0;padding:0;}
.aqm-trilha li{display:flex;align-items:center;gap:.3rem;white-space:nowrap;}
.aqm-trilha li+li::before{content:"\203A";color:var(--aqm-traco);}
.aqm-trilha a{color:var(--aqm-legenda);text-decoration:none;border-bottom:1px solid var(--aqm-traco);}
.aqm-trilha a:hover{color:var(--aqm-lamina);border-bottom-color:var(--aqm-lamina);}
.aqm-trilha [aria-current="page"]{color:var(--aqm-tinta);font-weight:500;}
/* Degrau de categoria que ainda não virou página: texto, e a tela diz isso sem
   promessa — o cartão "em breve" é da mãe, não da trilha. */
.aqm-trilha-espera{color:var(--aqm-legenda);}
/* O cluster do 16.4. */
.aqm-veja{font-family:var(--aqm-texto);border-top:1px solid var(--aqm-traco);margin:2.6rem 0 0;padding:1.4rem 0 0;}
.aqm-veja h2{font-family:var(--aqm-display);font-size:1.05rem;margin:0 0 .55rem;color:var(--aqm-tinta);}
.aqm-veja .aqm-veja-mae{margin:0 0 .7rem;color:var(--aqm-legenda);font-size:.93rem;line-height:1.55;}
.aqm-veja ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:.45rem;}
.aqm-veja li{margin:0;}
.aqm-veja a{color:var(--aqm-tinta);text-decoration:none;border-bottom:2px solid var(--aqm-lamina);font-weight:500;}
.aqm-veja a:hover{color:var(--aqm-lamina);}
.aqm-rodape{background:var(--aqm-tinta);color:var(--aqm-papel);padding:2.4rem 1.5rem;margin-top:3.5rem;font-family:var(--aqm-texto);}
.aqm-rodape-interno{max-width:52rem;margin:0 auto;display:flex;flex-direction:column;gap:.7rem;}
.aqm-rodape .aqm-tagline{font-family:var(--aqm-display);font-weight:700;font-size:1.1rem;color:var(--aqm-superficie);margin:0;}
.aqm-rodape p{margin:0;font-size:.86rem;line-height:1.55;color:var(--aqm-traco);}
.aqm-rodape a{color:var(--aqm-papel);}
/* Cinto de segurança do rodapé: o caminho principal é o filtro render_block, que
   troca a template part 'footer' do tema pela da Aquametria. Se ele não pegar,
   o rodapé do tema fica visível acima do nosso — as regras abaixo escondem o
   crédito do tema e, havendo rodapé da Aquametria na página, a template part
   de rodapé que não seja a nossa. */
.wp-site-blocks > footer.wp-block-template-part .wp-block-group:has(a[href*="wordpress.org"]){display:none;}
body:has(.aqm-rodape) .wp-site-blocks > footer.wp-block-template-part:not(:has(.aqm-rodape)){display:none;}
@media (max-width:600px){
.aqm-linha-mestra{font-size:1.15rem;}
.aqm-wordmark{font-size:1.25rem;}
}
/* Menu sanfona. 782 px e a largura em que o proprio WordPress considera que a
   tela virou celular; seguir a mesma quebra evita cabecalho meio empilhado.
   Tudo aqui depende de [data-aqm-menu]: sem JavaScript nada disso vale e o menu
   continua sendo a fileira de links, visivel, que sempre foi. */
@media (max-width:782px){
.aqm-nav-caixa[data-aqm-menu] .aqm-nav-botao{display:inline-flex;}
.aqm-nav-caixa[data-aqm-menu] .aqm-nav{display:none;position:absolute;right:0;top:calc(100% + .55rem);z-index:60;min-width:13rem;background:var(--aqm-superficie);border:1px solid var(--aqm-traco);border-radius:3px;box-shadow:0 12px 32px rgba(13,27,34,.16);padding:.35rem 0;}
.aqm-nav-caixa[data-aqm-menu][data-aqm-aberto="1"] .aqm-nav{display:block;}
.aqm-nav-caixa[data-aqm-menu] .aqm-nav ul,.aqm-nav-caixa[data-aqm-menu] .aqm-nav li{display:block;}
.aqm-nav-caixa[data-aqm-menu] .aqm-nav a,.aqm-nav-caixa[data-aqm-menu] .aqm-nav .aqm-sem-link{display:block;padding:.65rem 1.05rem;font-size:1rem;border-bottom:0;}
.aqm-nav-caixa[data-aqm-menu] .aqm-nav a:hover{background:var(--aqm-papel);color:var(--aqm-lamina);}
}
CSS;

	echo '<style id="aquametria-casca">' . $css . '</style>' . "\n";
}, 20 );

/* ---------------------------------------------------------------------------
 * 3b. O comando do menu sanfona
 *
 * O script sai no wp_footer, NUNCA dentro do retorno de um shortcode. É a regra
 * que nasceu do defeito de 08/09/2026: o WordPress roda os filtros de texto do
 * conteúdo sobre o que o shortcode devolve, cada E-comercial vira a entidade
 * numérica correspondente e o
 * JavaScript inteiro morre com erro de sintaxe. Aqui ele não passa por filtro
 * nenhum.
 *
 * O script não desenha menu: ele só assume o comando do que o PHP já serviu. A
 * primeira coisa que faz é pôr data-aqm-menu na caixa, e é esse atributo que
 * liga as regras de CSS do celular — ou seja, o menu só se fecha depois que
 * existe alguém para reabri-lo.
 * ------------------------------------------------------------------------- */

add_action( 'wp_footer', function () {
	$js = <<<'JS'
(function () {
	var caixas = document.querySelectorAll('.aqm-nav-caixa');
	if (!caixas.length) { return; }

	Array.prototype.forEach.call(caixas, function (caixa) {
		var botao = caixa.querySelector('.aqm-nav-botao');
		var lista = caixa.querySelector('.aqm-nav');
		if (!botao || !lista) { return; }

		/* A partir daqui o CSS do celular vale: há quem reabra o menu. */
		caixa.setAttribute('data-aqm-menu', '1');

		function aberto() {
			return caixa.getAttribute('data-aqm-aberto') === '1';
		}
		function estado(abrir) {
			caixa.setAttribute('data-aqm-aberto', abrir ? '1' : '0');
			botao.setAttribute('aria-expanded', abrir ? 'true' : 'false');
		}
		estado(false);

		botao.addEventListener('click', function (ev) {
			ev.preventDefault();
			estado(!aberto());
		});

		/* Escape fecha e devolve o foco ao botão: quem abriu pelo teclado não
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
		   volta a ser fileira de links e não pode continuar marcado como aberto,
		   senão o aria-expanded mente para o leitor de tela. */
		window.addEventListener('resize', function () {
			if (aberto() && window.innerWidth > 782) { estado(false); }
		});
	});
})();
JS;

	echo '<script id="aquametria-casca-menu">' . $js . '</script>' . "\n";
}, 25 );

/* ---------------------------------------------------------------------------
 * 4. Conteúdo das quatro páginas (shortcodes)
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_casca_cards_html' ) ) {
function aquametria_casca_cards_html() {
	$html = '<ul class="aqm-cards">';
	foreach ( aquametria_casca_calculadoras() as $c ) {
		$publicada = ( isset( $c['estado'] ) && 'publicada' === $c['estado'] );
		$html     .= '<li class="aqm-card">';
		$html     .= '<span class="aqm-codigo">' . esc_html( $c['codigo'] ) . '</span>';
		$html     .= '<h3>' . esc_html( $c['titulo'] ) . '</h3>';
		$html     .= '<p>' . esc_html( $c['resumo'] ) . '</p>';
		$html     .= '<span class="aqm-acao">';
		$url = $publicada ? aquametria_casca_url_se_existir( $c['slug'] ) : '';
		if ( '' !== $url ) {
			$html .= '<a href="' . esc_url( $url ) . '">Abrir calculadora</a>';
		} else {
			/* A calculadora pode ter se anunciado publicada e a página ainda não
			   existir (Sync atrasado, slug tomado por outra página). Melhor o
			   selo honesto que um link que devolve 404. */
			$html .= '<span class="aqm-tag">Em construção</span>';
		}
		$html .= '</span></li>';
	}
	$html .= '</ul>';

	return $html;
}
}

if ( ! function_exists( 'aquametria_casca_conta_publicadas' ) ) {
function aquametria_casca_conta_publicadas() {
	$n = 0;
	foreach ( aquametria_casca_calculadoras() as $c ) {
		if ( isset( $c['estado'] ) && 'publicada' === $c['estado'] ) {
			$n++;
		}
	}
	return $n;
}
}

/* ---------------------------------------------------------------------------
 * 3d. A ÁRVORE — breadcrumb, BreadcrumbList e cluster de "Veja também"
 *
 * Seção 16 do ARQUIPELAGO.md, e item do despacho do Raphael de 11/09/2026 que
 * o bloco da voz deixou de pé. O mapa de quem é mãe de quem está escrito em
 * ARVORE.md; aqui ele vira código, e `ferramentas/teste-arvore.mjs` confere que
 * as duas metades dizem a mesma coisa — porque documento e código mantidos à
 * mão em dois lugares divergem em silêncio (seção 8 do contrato).
 *
 * CINCO DECISÕES, e nenhuma é enfeite:
 *
 *   1. NADA AQUI CRIA URL. As oito páginas de nível 1 e 2 da árvore estão
 *      travadas até a leitura de 16/09 (item 5 do despacho da Sentinela de
 *      10/09, e seção 6 do ARVORE.md). Breadcrumb e cluster cabem antes porque
 *      só usam endereço que já existe.
 *   2. O NÍVEL 2 SAI EM TEXTO, SEM LINK, porque a categoria ainda não nasceu.
 *      É estado de transição declarado no ARVORE.md, não desenho: no dia em que
 *      a categoria existir, `aquametria_casca_url_se_existir()` a encontra e ela
 *      vira link sozinha, sem ninguém lembrar disto.
 *   3. O JSON-LD NÃO CARREGA O DEGRAU SEM ENDEREÇO. Um ListItem intermediário
 *      sem `item` deixa o BreadcrumbList inteiro inválido, e breadcrumb inválido
 *      é breadcrumb ignorado — o schema publicaria menos do que publica hoje.
 *      Então o schema leva só os degraus que têm URL de verdade, e o teste cobra
 *      exatamente essa relação: os itens do JSON-LD são os degraus LINKADOS da
 *      trilha visível, mais a página atual. A trilha na tela continua mostrando
 *      a categoria, que é o que diz ao leitor onde ele está.
 *   4. AS IRMÃS SÃO DERIVADAS, NUNCA DIGITADAS. Lista de irmãs escrita à mão
 *      envelhece no dia em que uma calculadora entra no ar — é a cicatriz do
 *      número de tela digitado (seção 8). Aqui elas saem do mesmo registro que
 *      alimenta o hub: mesma mãe, mesma categoria primeiro, ordem do mapa
 *      depois. Afinidade declarada, não sorteio.
 *   5. A MÃE SÓ É CITADA NO CORPO QUANDO EXISTE. O 16.4(b) manda a filha linkar
 *      a mãe no breadcrumb E numa frase do corpo; frase apontando para página
 *      que não existe seria link morto, então a frase só sai com mãe publicada —
 *      e o teste cobra a frase justamente onde a mãe existe.
 * ------------------------------------------------------------------------- */

/* Os rótulos de nível 2. O slug é o do ARVORE.md; o rótulo é o nome que a
   pessoa usa, como manda o VOZ.md. */
if ( ! function_exists( 'aquametria_casca_categorias' ) ) {
function aquametria_casca_categorias() {
	/* A categoria do C8 se chamava `peixes` e passou a `lotacao` na 1.7.0, e o
	   motivo é de endereço, não de gosto: a leva 1 do eixo publicou a seção de
	   nível 1 `/peixes/`, e `aquametria_casca_url_se_existir()` acha a página
	   pelo `post_name`, que é o ÚLTIMO pedaço da URL. Com `/peixes/` e
	   `/calculadoras/peixes/` no ar ao mesmo tempo, o hub linkaria uma das duas
	   ao acaso — e a página do C8 ainda não existe, então trocar o slug hoje não
	   move URL nenhuma. `ferramentas/teste-peixes.py` tem a afirmação que impede
	   a colisão de voltar. */
	return array(
		'aquario'           => 'Aquário',
		'filtragem'         => 'Filtragem',
		'aquecimento-e-luz' => 'Aquecimento e luz',
		'lotacao'           => 'Lotação',
	);
}
}

/* A categoria de nível 2 de cada guia, pelo slug do artigo (ARVORE.md seção 5).
   Mora aqui, e não no snippet dos artigos, porque é decisão de ÁRVORE — quem
   decide onde a página mora é o mapa do site, não quem escreve o texto. */
if ( ! function_exists( 'aquametria_casca_categorias_guia' ) ) {
function aquametria_casca_categorias_guia() {
	return array(
		'quantos-watts-de-aquecedor-para-aquario'   => array( 'aquecimento', 'Aquecimento' ),
		'quanta-midia-biologica-o-aquario-precisa'  => array( 'filtragem',   'Filtragem' ),
		'quantos-lumens-por-litro-aquario-plantado' => array( 'iluminacao',  'Iluminação' ),
	);
}
}

/**
 * Onde esta página mora. Devolve:
 *   nivel1      => array(slug, rotulo)  — a seção; slug '' quando ela não existe
 *   nivel2      => array(slug, rotulo)  — a categoria; array() quando não há
 *   rotulo      => o texto do degrau atual (a consulta-alvo, não o nome interno)
 *   irmas       => slugs das irmãs, já escolhidas
 *   fora        => true para as páginas que o ARVORE.md deixa fora da árvore
 * Devolve array() para a home e para página desconhecida — e quem chama não
 * publica trilha nenhuma, que é melhor que publicar trilha inventada.
 */
if ( ! function_exists( 'aquametria_casca_lugar' ) ) {
function aquametria_casca_lugar( $slug ) {
	$slug = sanitize_title( (string) $slug );
	if ( '' === $slug ) {
		return array();
	}

	$categorias = aquametria_casca_categorias();

	/* As páginas que o ARVORE.md mantém na raiz, fora da árvore. */
	$raiz = array(
		'calculadoras'            => 'Calculadoras',
		'metodologia'             => 'Como a gente calcula',
		'sobre'                   => 'Sobre',
		/* O degrau da trilha diz o mesmo que o H1 logo abaixo dele. O rodapé
		   continua dizendo "Divulgação de afiliados" (linha 563) porque ali o
		   nome precisa ser o reconhecível como aviso de comissão — são duas
		   superfícies com trabalhos diferentes, e só a trilha responde pelo
		   nome da página. */
		'divulgacao-de-afiliados' => 'Como a Aquametria ganha dinheiro',
	);
	if ( isset( $raiz[ $slug ] ) ) {
		return array(
			'nivel1' => array( '', '' ),
			'nivel2' => array(),
			'rotulo' => $raiz[ $slug ],
			'irmas'  => array(),
			'fora'   => true,
		);
	}

	/* Calculadora: mãe é /calculadoras/, categoria é a do registro do hub. */
	foreach ( aquametria_casca_calculadoras() as $c ) {
		if ( ! isset( $c['slug'] ) || $c['slug'] !== $slug ) {
			continue;
		}
		$cat = isset( $c['categoria'] ) ? $c['categoria'] : '';
		return array(
			'nivel1' => array( 'calculadoras', 'Calculadoras' ),
			'nivel2' => isset( $categorias[ $cat ] ) ? array( $cat, $categorias[ $cat ] ) : array(),
			'rotulo' => isset( $c['titulo'] ) ? $c['titulo'] : $slug,
			'irmas'  => aquametria_casca_irmas( $slug ),
			'fora'   => false,
		);
	}

	/* O eixo /peixes/, desde a 1.7.0. A casca NÃO guarda o mapa dele: pergunta
	   pelo filtro e quem responde é o snippet que publica as páginas — mesmo
	   molde do hub de calculadoras e da prateleira de guias, e pelo mesmo
	   motivo (ficha nova entra na trilha sozinha, sem ninguém lembrar daqui).

	   O rótulo do degrau é o TÍTULO da página, nunca um nome de menu: em 8 das
	   9 páginas de conteúdo a trilha e o H1 diziam nomes diferentes a uma linha
	   de distância, e foi o achado do bloco da voz de 11/09. O menu é a única
	   superfície que pode encurtar, porque o trabalho dele é caber. */
	foreach ( aquametria_casca_peixes() as $px_slug => $px ) {
		if ( $px_slug !== $slug ) {
			continue;
		}
		$mae = ( '' !== $px['pai'] ) ? $px['pai'] : '';
		$n1  = array( '', '' );
		if ( 3 === $px['nivel'] ) {
			$n1 = array( 'peixes', aquametria_casca_peixes_rotulo( 'peixes' ) );
		} elseif ( 2 === $px['nivel'] && '' !== $mae ) {
			$n1 = array( $mae, aquametria_casca_peixes_rotulo( $mae ) );
		}
		return array(
			'nivel1' => $n1,
			'nivel2' => ( 3 === $px['nivel'] && '' !== $mae )
				? array( $mae, aquametria_casca_peixes_rotulo( $mae ) )
				: array(),
			'rotulo' => $px['rotulo'],
			'irmas'  => aquametria_casca_irmas_de_peixes( $slug ),
			'fora'   => false,
		);
	}

	/* Guia: mãe é /guias/, que ainda não existe como página. */
	$guias_cat = aquametria_casca_categorias_guia();
	foreach ( aquametria_casca_guias() as $g ) {
		if ( $g['slug'] !== $slug ) {
			continue;
		}
		$c2 = isset( $guias_cat[ $slug ] ) ? $guias_cat[ $slug ] : array();
		return array(
			'nivel1' => array( 'guias', 'Guias' ),
			'nivel2' => $c2 ? array( $c2[0], $c2[1] ) : array(),
			'rotulo' => $g['manchete'],
			'irmas'  => aquametria_casca_irmas( $slug ),
			'fora'   => false,
		);
	}

	return array();
}
}

/**
 * As irmãs de uma página: MESMA MÃE, no ar, ordenadas por afinidade — primeiro
 * as da mesma categoria de nível 2, depois as demais na ordem do registro. No
 * máximo quatro, como manda o 16.4(c).
 *
 * Derivada do mesmo registro que alimenta o hub e a prateleira de guias, então
 * calculadora que entra no ar vira irmã de todo mundo sozinha. Página que não
 * existe publicada não entra: irmã é link, e link morto não é cluster.
 */
if ( ! function_exists( 'aquametria_casca_irmas' ) ) {
function aquametria_casca_irmas( $slug ) {
	$slug  = sanitize_title( (string) $slug );
	$irmas = array();

	/* Calculadoras: mesma mãe /calculadoras/. */
	$eu = null;
	$lista = aquametria_casca_calculadoras();
	foreach ( $lista as $c ) {
		if ( isset( $c['slug'] ) && $c['slug'] === $slug ) {
			$eu = $c;
			break;
		}
	}
	if ( null !== $eu ) {
		$minha = isset( $eu['categoria'] ) ? $eu['categoria'] : '';
		$perto = array();
		$longe = array();
		foreach ( $lista as $c ) {
			if ( empty( $c['slug'] ) || $c['slug'] === $slug ) {
				continue;
			}
			if ( ! isset( $c['estado'] ) || 'publicada' !== $c['estado'] ) {
				continue;
			}
			if ( '' === aquametria_casca_url_se_existir( $c['slug'] ) ) {
				continue;
			}
			$item = array( 'slug' => $c['slug'], 'rotulo' => $c['titulo'] );
			if ( '' !== $minha && isset( $c['categoria'] ) && $c['categoria'] === $minha ) {
				$perto[] = $item;
			} else {
				$longe[] = $item;
			}
		}
		$irmas = array_merge( $perto, $longe );
		return array_slice( $irmas, 0, 4 );
	}

	/* Guias: mesma mãe /guias/. */
	$guias = aquametria_casca_guias();
	$sou_guia = false;
	foreach ( $guias as $g ) {
		if ( $g['slug'] === $slug ) {
			$sou_guia = true;
			break;
		}
	}
	if ( ! $sou_guia ) {
		return array();
	}
	$cat_guia = aquametria_casca_categorias_guia();
	$minha    = isset( $cat_guia[ $slug ] ) ? $cat_guia[ $slug ][0] : '';
	$perto    = array();
	$longe    = array();
	foreach ( $guias as $g ) {
		if ( $g['slug'] === $slug ) {
			continue;
		}
		if ( '' === aquametria_casca_url_se_existir( $g['slug'] ) ) {
			continue;
		}
		$item = array( 'slug' => $g['slug'], 'rotulo' => $g['manchete'] );
		if ( '' !== $minha && isset( $cat_guia[ $g['slug'] ] ) && $cat_guia[ $g['slug'] ][0] === $minha ) {
			$perto[] = $item;
		} else {
			$longe[] = $item;
		}
	}
	return array_slice( array_merge( $perto, $longe ), 0, 4 );
}
}

/* Quantas calculadoras estão REALMENTE abertas ao visitante: anunciadas como
   publicadas E com página existindo. É este o número que a frase do cluster
   diz, e ele é contado — nunca digitado (seção 8 do contrato). */
if ( ! function_exists( 'aquametria_casca_conta_no_ar' ) ) {
function aquametria_casca_conta_no_ar() {
	$n = 0;
	foreach ( aquametria_casca_calculadoras() as $c ) {
		if ( ! isset( $c['estado'] ) || 'publicada' !== $c['estado'] || empty( $c['slug'] ) ) {
			continue;
		}
		if ( '' !== aquametria_casca_url_se_existir( $c['slug'] ) ) {
			$n++;
		}
	}
	return $n;
}
}

/**
 * Os degraus da trilha, do topo até a página atual. Cada degrau:
 *   array( 'rotulo' => ..., 'url' => '' quando a página ainda não existe )
 * O último degrau é sempre a página atual e nunca leva URL — é onde a pessoa
 * já está.
 */
if ( ! function_exists( 'aquametria_casca_degraus' ) ) {
function aquametria_casca_degraus( $slug ) {
	$lugar = aquametria_casca_lugar( $slug );
	if ( ! $lugar ) {
		return array();
	}

	$degraus = array( array( 'rotulo' => 'Início', 'url' => home_url( '/' ) ) );

	if ( empty( $lugar['fora'] ) ) {
		list( $n1_slug, $n1_rotulo ) = $lugar['nivel1'];
		if ( '' !== $n1_slug ) {
			$degraus[] = array(
				'rotulo' => $n1_rotulo,
				'url'    => aquametria_casca_url_se_existir( $n1_slug ),
			);
		}
		if ( ! empty( $lugar['nivel2'] ) ) {
			$degraus[] = array(
				'rotulo' => $lugar['nivel2'][1],
				'url'    => aquametria_casca_url_se_existir( $lugar['nivel2'][0] ),
			);
		}
	}

	$degraus[] = array( 'rotulo' => $lugar['rotulo'], 'url' => '' );

	return $degraus;
}
}

/* A trilha visível. `<nav>` com `<ol>`, porque é navegação e é ordenada; o
   degrau sem URL sai como texto e o atual leva aria-current. */
if ( ! function_exists( 'aquametria_casca_trilha_html' ) ) {
function aquametria_casca_trilha_html( $slug ) {
	$degraus = aquametria_casca_degraus( $slug );
	if ( count( $degraus ) < 2 ) {
		return '';
	}

	$ultimo = count( $degraus ) - 1;
	$html   = '<nav class="aqm-trilha" aria-label="Você está em"><ol>';
	foreach ( $degraus as $i => $d ) {
		$html .= '<li>';
		if ( $i === $ultimo ) {
			$html .= '<span aria-current="page">' . esc_html( $d['rotulo'] ) . '</span>';
		} elseif ( '' !== $d['url'] ) {
			$html .= '<a href="' . esc_url( $d['url'] ) . '">' . esc_html( $d['rotulo'] ) . '</a>';
		} else {
			/* Categoria ainda não publicada: texto, nunca link morto. */
			$html .= '<span class="aqm-trilha-espera">' . esc_html( $d['rotulo'] ) . '</span>';
		}
		$html .= '</li>';
	}
	$html .= '</ol></nav>';

	return $html;
}
}

/* O BreadcrumbList. Leva os degraus COM URL mais a página atual, e nada mais —
   ver decisão 3 no topo desta seção. */
if ( ! function_exists( 'aquametria_casca_trilha_jsonld' ) ) {
function aquametria_casca_trilha_jsonld( $slug ) {
	$degraus = aquametria_casca_degraus( $slug );
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

	$url_atual = aquametria_casca_url_se_existir( $slug );
	$pos++;
	$ultimo = array(
		'@type'    => 'ListItem',
		'position' => $pos,
		'name'     => $atual['rotulo'],
	);
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

/* O cluster: a frase que linka a mãe (16.4b) e as irmãs (16.4c). */
if ( ! function_exists( 'aquametria_casca_veja_tambem_html' ) ) {
function aquametria_casca_veja_tambem_html( $slug ) {
	$lugar = aquametria_casca_lugar( $slug );
	if ( ! $lugar || ! empty( $lugar['fora'] ) || empty( $lugar['irmas'] ) ) {
		return '';
	}

	$html = '<nav class="aqm-veja" aria-label="Veja também"><h2>Veja também</h2>';

	/* A frase da mãe, só quando a mãe existe. O número é contado. */
	list( $n1_slug, $n1_rotulo ) = $lugar['nivel1'];
	$url_mae = ( '' !== $n1_slug ) ? aquametria_casca_url_se_existir( $n1_slug ) : '';
	if ( '' !== $url_mae && 'calculadoras' === $n1_slug ) {
		$quantas = aquametria_casca_conta_no_ar();
		$html   .= '<p class="aqm-veja-mae">Esta é uma das <a href="' . esc_url( $url_mae ) . '">'
			. esc_html( $quantas ) . ' contas que já estão no ar</a> aqui na Aquametria.</p>';
	}

	$html .= '<ul>';
	foreach ( $lugar['irmas'] as $irma ) {
		$url = aquametria_casca_url_se_existir( $irma['slug'] );
		if ( '' === $url ) {
			continue;
		}
		$html .= '<li><a href="' . esc_url( $url ) . '">' . esc_html( $irma['rotulo'] ) . '</a></li>';
	}
	$html .= '</ul></nav>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 3e. Onde a trilha e o cluster entram na página
 *
 * A trilha entra no lugar do bloco core/post-title, ANTES do H1 — é o "abaixo
 * do header" do 16.3. Se o tema não renderizar esse bloco (template diferente,
 * outro tema), ela cai na rede de segurança do the_content, no mesmo padrão que
 * o rodapé já usa desde a 1.0.0. Publicar trilha em um lugar só e torcer para o
 * bloco existir seria repetir o defeito do rodapé duplicado, ao contrário.
 *
 * O cluster entra no FIM do the_content, com prioridade 20: depois do
 * do_shortcode, então o que ele acrescenta nunca atravessa os filtros de texto
 * que transformam "&" em entidade. Ele não tem script — mas o lugar certo é o
 * lugar certo mesmo quando o defeito não está ali hoje.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_casca_slug_atual' ) ) {
function aquametria_casca_slug_atual() {
	if ( is_front_page() || ! is_singular() ) {
		return '';
	}
	$post = get_post();
	if ( ! $post || empty( $post->post_name ) ) {
		return '';
	}
	return $post->post_name;
}
}

if ( ! function_exists( 'aquametria_casca_trilha_impressa' ) ) {
function aquametria_casca_trilha_impressa( $marcar = false ) {
	static $impressa = false;
	if ( $marcar ) {
		$impressa = true;
	}
	return $impressa;
}
}

add_filter( 'render_block', function ( $conteudo, $bloco ) {
	if ( is_admin() || ( defined( 'REST_REQUEST' ) && REST_REQUEST ) ) {
		return $conteudo;
	}
	$nome = isset( $bloco['blockName'] ) ? $bloco['blockName'] : '';
	if ( 'core/post-title' !== $nome ) {
		return $conteudo;
	}
	if ( aquametria_casca_trilha_impressa() ) {
		return $conteudo;
	}
	$trilha = aquametria_casca_trilha_html( aquametria_casca_slug_atual() );
	if ( '' === $trilha ) {
		return $conteudo;
	}
	aquametria_casca_trilha_impressa( true );

	return $trilha . $conteudo;
}, 10, 2 );

/* Rede de segurança: sem bloco core/post-title na página, a trilha sai no topo
   do conteúdo. Prioridade 9 para ficar acima de tudo que o conteúdo traz. */
add_filter( 'the_content', function ( $html ) {
	if ( is_admin() || ! is_singular() || aquametria_casca_trilha_impressa() ) {
		return $html;
	}
	$trilha = aquametria_casca_trilha_html( aquametria_casca_slug_atual() );
	if ( '' === $trilha ) {
		return $html;
	}
	aquametria_casca_trilha_impressa( true );

	return $trilha . $html;
}, 9 );

add_filter( 'the_content', function ( $html ) {
	if ( is_admin() || ! is_singular() ) {
		return $html;
	}

	return $html . aquametria_casca_veja_tambem_html( aquametria_casca_slug_atual() );
}, 20 );

add_action( 'wp_head', function () {
	$dados = aquametria_casca_trilha_jsonld( aquametria_casca_slug_atual() );
	if ( ! $dados ) {
		return;
	}
	echo '<script type="application/ld+json" id="aquametria-trilha-jsonld">' . "\n"
		. wp_json_encode( $dados ) . "\n" . '</script>' . "\n";
}, 22 );

/* ---------------------------------------------------------------------------
 * 3f. A tag de medição (GA4)
 *
 * Despacho de 12/09/2026, prioridade alta: sem esta tag a seção 5 do
 * ARQUIPELAGO.md (visibilidade em IA) não é mensurável, porque a referência de
 * chatgpt.com, perplexity.ai e gemini.google.com só aparece no GA4 — o Search
 * Console não a vê. Ela é SNIPPET e não plugin pela seção 11.7: a página
 * pública é território da casca, e o repositório continua sendo o dono.
 *
 * PRIORIDADE 23, e o número é a regra escrita em código. O despacho manda
 * imprimir "o mais cedo possível" E proíbe entrar antes do <title>, da meta
 * descrição ou do JSON-LD. Quem já está no wp_head desta ilha:
 *     1  <title> (o núcleo, _wp_render_title_tag)
 *     3  meta descrição e og: (aquametria-seo-tecnico)
 *     5  ícone do site
 *    20  fontes e paleta; JSON-LD das cinco calculadoras e dos três artigos
 *    22  BreadcrumbList
 * Então 23 é o mais cedo que sobra depois do último JSON-LD, e não é escolha de
 * gosto: é o único número que cumpre as duas metades do despacho ao mesmo tempo.
 *
 * UM PARÂMETRO SÓ NA URL, de propósito. O defeito de 08/09/2026 que derrubou
 * cinco calculadoras foi o E-comercial virando &#038;; aqui o risco não é o
 * mesmo (isto não sai de shortcode), mas esc_url() também escapa & e a tag do
 * Google aceita só o id — então não existe segundo parâmetro para escapar, e o
 * portão que conta &#038; dentro de <script> continua vendo zero.
 *
 * SEM BANNER DE CONSENTIMENTO, por decisão do despacho e da seção 22.4: nada
 * que empurre a resposta para baixo da dobra. Quem declara a medição é a página
 * de transparência da ilha, em uma frase.
 * ------------------------------------------------------------------------- */

add_action( 'wp_head', function () {
	/* Esta guarda NÃO é ramo morto, e é a mesma do ícone do site logo acima: o
	   bloco de constantes do topo inteiro está dentro de
	   `if ( ! defined( 'AQUAMETRIA_CASCA_VERSAO' ) )`, então uma cópia antiga da
	   casca já carregada define a VERSÃO, o bloco é pulado e AQUAMETRIA_CASCA_GA4_ID
	   nunca nasce. Sem esta linha, o site serviria a tag com a constante crua no
	   lugar do ID. Não há guarda de is_admin() nem de is_feed() de propósito: o
	   wp_head não roda em nenhum dos dois (lá são admin_head e rss2_head), e ramo
	   que não roda é código que teste nenhum protege — seção 8 do ARQUIPELAGO.md. */
	if ( ! defined( 'AQUAMETRIA_CASCA_GA4_ID' ) || '' === AQUAMETRIA_CASCA_GA4_ID ) {
		return;
	}

	$id = AQUAMETRIA_CASCA_GA4_ID;

	echo '<script async src="' . esc_url( 'https://www.googletagmanager.com/gtag/js?id=' . $id ) . '"></script>' . "\n";
	echo '<script id="aquametria-ga4">'
		. 'window.dataLayer=window.dataLayer||[];'
		. 'function gtag(){dataLayer.push(arguments);}'
		. "gtag('js',new Date());"
		. "gtag('config'," . wp_json_encode( $id ) . ');'
		. '</script>' . "\n";
}, 23 );

/**
 * A home, no molde GUIA do VOZ.md: a pergunta mais frequente em cima, as
 * calculadoras como cartões na linguagem da pessoa, os guias embaixo — e a
 * prova no fim, dentro de `aqm-prova`.
 *
 * Sem manifesto, que era como ela abria até a 1.3.1 ("A Aquametria dimensiona
 * aquário com número que tem fonte"). A frase não era falsa; ela só falava da
 * fábrica para a fábrica, e quem chega aqui chegou com uma fita métrica na mão.
 */
add_shortcode( 'aquametria_home', function () {
	$total      = count( aquametria_casca_calculadoras() );
	$publicadas = aquametria_casca_conta_publicadas();
	$guias      = aquametria_casca_guias();

	$html  = '<div class="aqm-bloco">';

	/* 1. A pergunta mais frequente da ilha, com as três medidas. */
	$html .= '<div class="aqm-abertura aqm-pergunta">';
	$html .= '<p class="aqm-linha-mestra">Quantos litros tem o seu aquário?</p>';
	$html .= '<p>Pega a fita métrica e anota comprimento, largura e altura em centímetros. A gente devolve os três números que importam: o litro da etiqueta, o que cabe de verdade e a água que você vai tratar — e eles não são iguais.</p>';
	$url_c1 = aquametria_casca_url_se_existir( 'calculadora-de-litragem' );
	if ( '' !== $url_c1 ) {
		$html .= '<p class="aqm-acao-grande"><a href="' . esc_url( $url_c1 ) . '">Fazer a conta dos litros</a></p>';
	}
	$html .= '</div>';

	/* 2. As outras contas. O "N de M" é contado, nunca digitado. */
	$html .= '<div class="aqm-secao">';
	$html .= '<h2>E as outras contas do aquário</h2>';
	if ( 0 === $publicadas ) {
		$html .= '<p>As contas abaixo estão prontas no papel e entram no ar uma por vez.</p>';
	} else {
		$html .= '<p>' . esc_html( $publicadas ) . ' de ' . esc_html( $total ) . ' já estão no ar. As outras entram uma por vez — cada uma só sai quando dá para mostrar de onde veio cada número.</p>';
	}
	$html .= aquametria_casca_cards_html();
	$html .= '</div>';

	/* 2b. O eixo dos peixes, quando a seção existe publicada. A home é a mãe do
	   nível 1 (16.4a e 16.4f: toda URL tem ao menos dois links internos, um
	   deles da mãe — o menu é o outro), e o número de fichas é CONTADO do mapa
	   que o snippet do eixo anuncia, nunca digitado aqui. */
	$url_peixes = aquametria_casca_url_se_existir( 'peixes' );
	if ( '' !== $url_peixes ) {
		$fichas = 0;
		foreach ( aquametria_casca_peixes() as $px_slug => $px ) {
			if ( 3 === $px['nivel'] && '' !== aquametria_casca_url_se_existir( $px_slug ) ) {
				$fichas++;
			}
		}
		$html .= '<div class="aqm-secao">';
		$html .= '<h2>Quantos peixes cabem, espécie por espécie</h2>';
		$html .= '<p>O aquário mínimo de um peixe vem em centímetros de frente, não em litros — é assim que as fontes de aquarismo declaram, e é o que quase nenhuma resposta de busca diz. ';
		if ( $fichas > 0 ) {
			$html .= 'Já são ' . esc_html( $fichas ) . ' espécies com a conta inteira, e cada ficha traz o mínimo declarado ao lado das duas réguas brasileiras de lotação, que discordam em quatro vezes.</p>';
		} else {
			$html .= 'As primeiras fichas entram uma leva por vez.</p>';
		}
		$html .= '<p class="aqm-acao-grande"><a href="' . esc_url( $url_peixes ) . '">Ver quanto espaço cada peixe pede</a></p>';
		$html .= '</div>';
	}

	/* 3. Os guias, quando existem. Quem responde é o snippet dos artigos. */
	if ( ! empty( $guias ) ) {
		$html .= '<div class="aqm-secao">';
		$html .= '<h2>Para entender antes de comprar</h2>';
		$html .= '<p>Quando a conta não basta e você quer saber por que o número é aquele.</p>';
		$html .= '<ul class="aqm-guias">';
		foreach ( $guias as $g ) {
			$url = aquametria_casca_url_se_existir( $g['slug'] );
			$html .= '<li class="aqm-guia">';
			if ( '' !== $url ) {
				$html .= '<h3><a href="' . esc_url( $url ) . '">' . esc_html( $g['manchete'] ) . '</a></h3>';
			} else {
				$html .= '<h3>' . esc_html( $g['manchete'] ) . '</h3>';
			}
			if ( '' !== $g['resumo'] ) {
				$html .= '<p>' . esc_html( $g['resumo'] ) . '</p>';
			}
			$html .= '</li>';
		}
		$html .= '</ul>';
		$html .= '</div>';
	}

	/* 4. A camada de prova. */
	$html .= '<div class="aqm-secao aqm-prova">';
	$html .= '<h2>Como a gente sabe</h2>';
	$html .= '<p>Todo número daqui tem fonte com nome e data: manual do fabricante, norma técnica ou levantamento brasileiro identificado. Quando duas fontes discordam — e no aquarismo brasileiro elas discordam bastante —, as duas aparecem na tela com o nome de quem disse o quê. A gente não tira média, e onde não achamos fonte que preste a página diz isso em vez de chutar.</p>';
	$html .= '<p>' . aquametria_casca_link_html( 'metodologia', 'Ver o critério inteiro' ) . '</p>';
	$html .= '</div>';

	$html .= '</div>';

	return $html;
} );

add_shortcode( 'aquametria_calculadoras', function () {
	$html  = '<div class="aqm-bloco">';
	$html .= '<p class="aqm-linha-mestra">As contas do seu aquário, em um lugar só.</p>';
	$html .= '<p>Comece pelos litros: o aquário que você mede ali fica guardado no seu próprio navegador e as outras contas já vêm preenchidas, sem você redigitar medida nenhuma. Nada sai do seu aparelho — sem conta, sem login, sem cadastro.</p>';
	$html .= aquametria_casca_cards_html();
	$html .= '<p class="aqm-nota aqm-prova"><strong>Em construção não é enfeite.</strong> Uma calculadora só entra no ar com a fonte de cada constante conferida e com a divergência entre fontes exposta na tela. Preferimos uma calculadora impecável a duas medianas.</p>';
	$html .= '</div>';

	return $html;
} );

if ( ! function_exists( 'aquametria_casca_quadro_constantes' ) ) {
function aquametria_casca_quadro_constantes() {
	$vocabulario = array(
		'fisica'                => 'Valor tabelado de física; a fórmula declara o arredondamento usado.',
		'verificada-fabricante' => 'Lida diretamente na página ou no manual do fabricante.',
		'fabricante-via-busca'  => 'Número do fabricante colhido por resultado de busca, com a página ainda por ler direto. Marcada para reconferência.',
		'norma-via-secundaria'  => 'Valor de norma ABNT citado por fonte secundária — a norma é paga e não foi lida direto.',
		'transcrita-varejo'     => 'Rótulo ou ficha transcrita por varejista. A tela pede que você confira a embalagem.',
		'divergente-fontes-br'  => 'As fontes brasileiras conflitam. A resposta publica a faixa inteira e diz de quem é cada extremo.',
		'convencao-editorial'   => 'Escolha da Aquametria, não dado técnico. A tela precisa dizer isso.',
		'pendente'              => 'Sem fonte aceitável. Proibida em fórmula publicada.',
	);

	// Instantâneo de 07/09/2026; se o banco de constantes estiver publicado no site, conta ao vivo.
	$contagem = array(
		'fisica'                => 1,
		'verificada-fabricante' => 1,
		'fabricante-via-busca'  => 3,
		'norma-via-secundaria'  => 1,
		'transcrita-varejo'     => 3,
		'divergente-fontes-br'  => 24,
		'convencao-editorial'   => 1,
		'pendente'              => 8,
	);

	$dados = get_option( 'aquametria_dados_constantes-calculadoras' );
	if ( is_array( $dados ) && ! empty( $dados['constantes'] ) && is_array( $dados['constantes'] ) ) {
		$viva = array_fill_keys( array_keys( $vocabulario ), 0 );
		foreach ( $dados['constantes'] as $c ) {
			if ( isset( $c['status'] ) && isset( $viva[ $c['status'] ] ) ) {
				$viva[ $c['status'] ]++;
			}
		}
		if ( array_sum( $viva ) > 0 ) {
			$contagem = $viva;
		}
	}

	return array( 'vocabulario' => $vocabulario, 'contagem' => $contagem, 'total' => array_sum( $contagem ) );
}
}

add_shortcode( 'aquametria_metodologia', function () {
	$q = aquametria_casca_quadro_constantes();

	$html  = '<div class="aqm-bloco">';
	$html .= '<p class="aqm-linha-mestra">De onde sai cada número que a gente te dá.</p>';
	$html .= '<p>No aquarismo brasileiro a mesma pergunta recebe três respostas diferentes, todas escritas com a mesma segurança. O que está abaixo existe para você conseguir julgar o número em vez de ter que acreditar nele.</p>';

	/* Daqui para baixo é camada de prova (seção 15.2 do ARQUIPELAGO.md), e a
	   página DIZ isso no markup em vez de deixar o portão adivinhar pela
	   vizinhança das palavras — foi assim que o Clube do Mosaico resolveu a
	   mesma classe de problema em 11/09/2026. A marca é uma só, envolve tudo o
	   que vem depois da abertura, e nunca cobre o título nem o primeiro
	   parágrafo: a voz fica fora dela por construção. */
	$html .= '<div class="aqm-prova">';

	$html .= '<div class="aqm-secao"><h2>1. Toda resposta é uma faixa, com critério e fonte em cada extremo</h2>';
	$html .= '<p>Nenhuma calculadora devolve um número seco. A resposta traz o piso, o teto, o critério que define cada um e a fonte que sustenta esse critério. Quando o piso vem de um fabricante e o teto de uma convenção brasileira, isso fica escrito na tela: são coisas de peso diferente.</p></div>';

	$html .= '<div class="aqm-secao"><h2>2. Divergência é publicada, nunca virada em média</h2>';
	$html .= '<p>Tirar média de fontes que discordam fabrica um número que ninguém defende. Um exemplo real do nosso banco: o turnover implícito declarado pelos próprios fabricantes de filtro vai de 1,76 a 10 renovações por hora — os fabricantes divergem entre si por 5,7 vezes, e todos divergem das 5 a 10 x/h repetidas na web brasileira. A calculadora mostra o intervalo inteiro e a atribuição, porque a divergência é a informação.</p></div>';

	$html .= '<div class="aqm-secao"><h2>3. Toda constante tem status</h2>';
	$html .= '<p>Cada número usado numa fórmula está registrado com fonte, endereço, data de verificação e um status que diz o quanto ele é firme. São ' . esc_html( $q['total'] ) . ' constantes registradas até aqui, incluindo as que foram recusadas.</p>';
	/* O quadro entra dentro de um bloco que rola, como TODA tabela desta ilha —
	   é o mesmo `aqm-tabela` que o conversor de Markdown do Sync põe em volta
	   das tabelas que vêm de conteudo/. Esta aqui é impressa direto pelo
	   shortcode e por isso nunca tinha ganhado o embrulho: media 67 px de
	   rolagem horizontal a 360 px e 37 px a 390 px, no ar, desde que a página
	   existe. Não foi a 1.4.0 que quebrou; foi a 1.4.0 que passou a medir. */
	$html .= '<div class="aqm-tabela" style="overflow-x:auto">';
	$html .= '<table class="aqm-quadro"><tr><th>Status</th><th>O que significa</th><th>Hoje</th></tr>';
	foreach ( $q['vocabulario'] as $status => $descricao ) {
		$n     = isset( $q['contagem'][ $status ] ) ? $q['contagem'][ $status ] : 0;
		$html .= '<tr><td>' . esc_html( $status ) . '</td><td>' . esc_html( $descricao ) . '</td><td>' . esc_html( $n ) . '</td></tr>';
	}
	$html .= '</table>';
	$html .= '</div>';
	$html .= '<p class="aqm-nota"><strong>Constante com status pendente é proibida em fórmula publicada.</strong> Ela fica no registro para que a ausência seja auditável, e para que qualquer pessoa saiba exatamente o que falta para o número existir.</p></div>';

	$html .= '<div class="aqm-secao"><h2>4. O que a Aquametria não publica, e por quê</h2>';
	$html .= '<p>Esta lista é parte da metodologia, não uma desculpa. Cada item volta no dia em que a fonte aparecer.</p>';
	$html .= '<ul class="aqm-lista">';
	$html .= '<li><strong>Espessura do vidro por litragem.</strong> Não temos tensão admissível e coeficiente de segurança citáveis. Errar aqui alaga casa.</li>';
	$html .= '<li><strong>O veredito "a sua laje aguenta".</strong> Damos a carga por metro quadrado e a carga de projeto da NBR 6120 para comparação. A autorização é de engenheiro, nunca de calculadora.</li>';
	$html .= '<li><strong>O cálculo físico do aquecedor.</strong> A fórmula de perda térmica exige o coeficiente de transmissão do vidro do aquário, e não achamos esse valor com fonte. Publicamos as regras de bolso com a atribuição de cada uma, e dizemos que nenhuma fonte brasileira cobre diferença de temperatura maior que 10 °C.</li>';
	$html .= '<li><strong>O desconto de substrato na litragem.</strong> As fontes brasileiras discordam em 100 % na densidade do substrato e nenhuma publica porosidade. O volume sai superestimado, e cada calculadora diz para que lado isso a torna segura ou insegura.</li>';
	$html .= '<li><strong>A "regra dos 10 %" de lotação.</strong> A fonte não define sobre qual base os 10 % incidem.</li>';
	$html .= '<li><strong>PPFD por litragem.</strong> Lúmen por litro ignora profundidade e espectro, e nenhuma fonte brasileira publica PPFD por litragem.</li>';
	$html .= '<li><strong>Dosagem de condicionador, sal e medicamento.</strong> Risco letal com apenas duas dosagens verificadas no fabricante, e a litragem superestimada erraria para overdose. Fica fora até haver rótulo conferido em quantidade.</li>';
	$html .= '</ul></div>';

	$html .= '<div class="aqm-secao"><h2>5. Procedência e correção</h2>';
	$html .= '<p>No banco de produtos a procedência é por campo, não por ficha: cada dado de um filtro, aquecedor, luminária ou mídia aponta para a fonte que o sustenta, com endereço e data. Campo sem fonte fica vazio, e vazio é melhor que inventado. Preço é série temporal separada, com loja e data de leitura, e nunca entra em critério técnico de sugestão.</p>';
	$html .= '<p>Quando aparece fonte melhor, a constante é substituída e a data de verificação da página muda junto. Correção não é vergonha: é o que a data serve para permitir.</p></div>';
	$html .= '</div>';
	$html .= '</div>';

	return $html;
} );

add_shortcode( 'aquametria_sobre', function () {
	$html  = '<div class="aqm-bloco">';
	$html .= '<p class="aqm-linha-mestra">A gente faz as contas do seu aquário e mostra de onde elas vieram.</p>';
	$html .= '<p>Aqui você acha as calculadoras e um banco de equipamentos com as medidas de cada um, montado com uma regra só: todo número diz de onde saiu e em que dia isso foi conferido.</p>';

	$html .= '<div class="aqm-secao"><h2>Por que existe</h2>';
	$html .= '<p>Ao levantar o que o aquarismo brasileiro publica, encontramos perguntas frequentes que ninguém responde com número de fonte: quanta mídia biológica cabe por litro de aquário, que potência de aquecedor a sua diferença de temperatura real exige, e qual a dureza da água da torneira na sua cidade. O que existe é regra de bolso repetida de site em site, sem origem. A Aquametria começa por esses vazios.</p></div>';

	$html .= '<div class="aqm-secao"><h2>Como é feita</h2>';
	$html .= '<p>Sem pessoa em cena: sem rosto, sem vídeo, sem canal, sem presença em fórum. O que sustenta uma resposta aqui é a conta e o lugar de onde o número saiu, e os dois ficam à vista na própria página, para você conferir se quiser. Calculadora e texto são guardados num repositório público antes de chegar ao site — o que está no ar tem histórico.</p></div>';

	$html .= '<div class="aqm-secao"><h2>O que a Aquametria não faz</h2>';
	$html .= '<ul class="aqm-lista">';
	$html .= '<li>Não vende equipamento nem intermedia venda.</li>';
	$html .= '<li>Não aceita link pago, publieditorial nem posição paga em ranking.</li>';
	$html .= '<li>Não usa preço como critério técnico. Sugestão de produto sai de campo medido — vazão, potência, volume atendido —, e o preço aparece depois, com loja e data.</li>';
	$html .= '<li>Quando houver link para loja, ele será de afiliado e virá declarado. Comissão não muda ordem de sugestão.</li>';
	$html .= '</ul></div>';

	$html .= '<p class="aqm-nota">Achou um número errado ou uma fonte melhor? A página de ' . aquametria_casca_link_html( 'metodologia', 'metodologia' ) . ' mostra o critério que usamos para aceitar ou recusar cada constante. Correção com fonte entra e muda a data de verificação.</p>';
	$html .= '</div>';

	return $html;
} );

/* ---------------------------------------------------------------------------
 * 5. Estrutura do site: páginas, página inicial e limpeza do tema padrão
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_casca_definicao_paginas' ) ) {
function aquametria_casca_definicao_paginas() {
	/* O título é o H1 que o tema imprime e o <title> que o buscador lê. Desde a
	   1.4.0 ele também fala a língua do VOZ.md — "Início" e "Metodologia" eram
	   nomes de menu de painel, não o que a pessoa procura. O SLUG não muda em
	   nenhum dos quatro: URL de página publicada não se mexe (seção 12.1). */
	$base = array(
		'inicio'       => array( 'titulo' => 'As contas do seu aquário', 'conteudo' => '[aquametria_home]' ),
		'calculadoras' => array( 'titulo' => 'Calculadoras', 'conteudo' => '[aquametria_calculadoras]' ),
		'metodologia'  => array( 'titulo' => 'Como a gente calcula', 'conteudo' => '[aquametria_metodologia]' ),
		'sobre'        => array( 'titulo' => 'Sobre', 'conteudo' => '[aquametria_sobre]' ),
	);

	/* Desde a 1.7.0 a casca não é a única que tem página: quem publica malha se
	   anuncia por este filtro, no mesmo molde do hub de calculadoras. Cada
	   entrada pode trazer 'pai' => slug, e é isso que faz a URL mostrar os três
	   níveis da seção 16.1 — sem pai, toda página nasceria na raiz, e página
	   solta na raiz é justamente o que a árvore proíbe.

	   Entrada malformada é DESCARTADA com o slug na mão, nunca aceita pela
	   metade: página sem título ou sem corpo nasceria fina, e página fina em
	   domínio novo gasta orçamento de rastreamento (seção 14.1). */
	$vindas = apply_filters( 'aquametria_paginas', $base );
	if ( ! is_array( $vindas ) ) {
		return $base;
	}

	$limpa = array();
	foreach ( $vindas as $slug => $def ) {
		$slug = sanitize_title( (string) $slug );
		if ( '' === $slug || ! is_array( $def ) || empty( $def['titulo'] ) || empty( $def['conteudo'] ) ) {
			continue;
		}
		$limpa[ $slug ] = array(
			'titulo'   => (string) $def['titulo'],
			'conteudo' => (string) $def['conteudo'],
			'pai'      => isset( $def['pai'] ) ? sanitize_title( (string) $def['pai'] ) : '',
		);
	}

	/* Mãe antes de filha, sempre: wp_insert_post precisa do ID do pai, e pai
	   que nasce depois deixa a filha na raiz com o endereço errado — e endereço
	   de página publicada não se move (seção 12.1). Ordenar por profundidade
	   resolve isso sem depender da ordem em que os filtros correram. */
	$profundidade = array();
	foreach ( $limpa as $slug => $def ) {
		$n   = 0;
		$sob = $def['pai'];
		while ( '' !== $sob && isset( $limpa[ $sob ] ) && $n < 5 ) {
			$n++;
			$sob = $limpa[ $sob ]['pai'];
		}
		$profundidade[ $slug ] = $n;
	}
	uksort( $limpa, function ( $a, $b ) use ( $profundidade ) {
		if ( $profundidade[ $a ] === $profundidade[ $b ] ) {
			return 0;
		}
		return ( $profundidade[ $a ] > $profundidade[ $b ] ) ? 1 : -1;
	} );

	return $limpa;
}
}

/**
 * A chave de remontagem: a versão da casca MAIS um resumo do mapa de páginas.
 *
 * Por que não só a versão, que é como foi até a 1.6.0: `aquametria_casca_montar()`
 * só remonta quando a chave muda, então página nova anunciada pelo filtro
 * `aquametria_paginas` NÃO NASCERIA até alguém lembrar de subir a constante à
 * mão. O Clube do Mosaico pagou exatamente isso em 12/09/2026: a ferramenta F1
 * nasceu 404 com o Sync dizendo "seis itens aplicados", porque o filtro que ela
 * usava para se registrar ficava inerte. Com o mapa dentro da chave, toda
 * página nova nasce sozinha depois do Sync.
 *
 * O resumo é um hash do mapa inteiro — slug, título, corpo e pai. Trocar o
 * título de uma página também remonta, e é o que se quer: é assim que o título
 * do wp-admin volta a ser o da definição.
 */
if ( ! function_exists( 'aquametria_casca_chave_estrutura' ) ) {
function aquametria_casca_chave_estrutura() {
	$mapa = aquametria_casca_definicao_paginas();
	$cru  = array();
	foreach ( $mapa as $slug => $def ) {
		$cru[] = $slug . '|' . $def['titulo'] . '|' . $def['conteudo'] . '|' . $def['pai'];
	}
	return AQUAMETRIA_CASCA_VERSAO . '+' . substr( md5( implode( "\n", $cru ) ), 0, 12 );
}
}

if ( ! function_exists( 'aquametria_casca_garantir_paginas' ) ) {
function aquametria_casca_garantir_paginas( &$relato ) {
	$ids   = array();
	$criou = false;

	foreach ( aquametria_casca_definicao_paginas() as $slug => $def ) {
		/* O pai precisa existir antes: a ordem de `definicao_paginas()` garante
		   isso, e se ainda assim ele faltar a filha NÃO nasce na raiz. Endereço
		   errado de página publicada é dívida que não se paga (seção 12.1). */
		$pai_id = 0;
		if ( '' !== $def['pai'] ) {
			if ( ! isset( $ids[ $def['pai'] ] ) ) {
				$relato[] = 'página ' . $slug . ': adiada — a mãe ' . $def['pai'] . ' não existe ainda';
				continue;
			}
			$pai_id = (int) $ids[ $def['pai'] ];
		}

		$pagina = get_page_by_path( '' !== $def['pai'] ? $def['pai'] . '/' . $slug : $slug, OBJECT, 'page' );

		if ( ! $pagina ) {
			$pid = wp_insert_post( array(
				'post_type'    => 'page',
				'post_title'   => $def['titulo'],
				'post_name'    => $slug,
				'post_parent'  => $pai_id,
				'post_content' => $def['conteudo'],
				'post_status'  => 'publish',
				'comment_status' => 'closed',
				'ping_status'    => 'closed',
			), true );
			if ( is_wp_error( $pid ) ) {
				$relato[] = 'página ' . $slug . ': erro — ' . $pid->get_error_message();
				continue;
			}
			update_post_meta( $pid, '_aquametria_casca', '1' );
			$ids[ $slug ] = (int) $pid;
			$criou        = true;
			$relato[]     = 'página ' . $slug . ': criada (#' . $pid . ')';
			continue;
		}

		$pid          = (int) $pagina->ID;
		$ids[ $slug ] = $pid;
		$nossa        = ( '1' === get_post_meta( $pid, '_aquametria_casca', true ) );

		if ( 'publish' !== $pagina->post_status ) {
			wp_update_post( array( 'ID' => $pid, 'post_status' => 'publish' ) );
			$relato[] = 'página ' . $slug . ': republicada (#' . $pid . ')';
		}
		// Só reescrevemos o corpo de página que é nossa e que perdeu o shortcode.
		if ( $nossa && false === strpos( (string) $pagina->post_content, $def['conteudo'] ) ) {
			wp_update_post( array( 'ID' => $pid, 'post_content' => $def['conteudo'] ) );
			$relato[] = 'página ' . $slug . ': shortcode reposto (#' . $pid . ')';
		}

		/* O título segue a definição — só nas páginas que são NOSSAS, pela mesma
		   regra do corpo: página que alguém editou à mão não é reescrita.
		   Existe desde a 1.4.0 porque o título é onde a voz da ilha aparece
		   primeiro (VOZ.md), e até aqui ele era gravado uma vez, no dia em que
		   a página nasceu, e nunca mais.
		   O post_name NÃO entra nesta chamada de propósito: o WordPress só gera
		   slug a partir do título quando post_name está vazio, e o destas quatro
		   está preenchido desde a criação. Trocar título aqui não move URL — e
		   mover URL de página publicada é proibido (seção 12.1 do contrato). */
		if ( $nossa && $def['titulo'] !== $pagina->post_title ) {
			wp_update_post( array( 'ID' => $pid, 'post_title' => $def['titulo'] ) );
			$relato[] = 'página ' . $slug . ': título atualizado (#' . $pid . ')';
		}

		/* O pai também se corrige, e só nas nossas. Página que perdeu o pai (por
		   edição no wp-admin, ou porque nasceu antes da mãe) serve a URL de raiz
		   e sai da árvore sem um erro aparecer. */
		if ( $nossa && (int) $pagina->post_parent !== $pai_id ) {
			wp_update_post( array( 'ID' => $pid, 'post_parent' => $pai_id ) );
			$relato[] = 'página ' . $slug . ': mãe reposta (#' . $pid . ' sob #' . $pai_id . ')';
			$criou    = true;
		}
	}

	if ( $criou ) {
		flush_rewrite_rules( false );
	}

	return $ids;
}
}

if ( ! function_exists( 'aquametria_casca_fixar_home' ) ) {
function aquametria_casca_fixar_home( $ids, &$relato ) {
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

/**
 * A tagline do WordPress, que é o que o núcleo põe no <title> da home.
 *
 * Fica junto de fixar_home() porque é da mesma família: opção do site que a
 * casca é dona. Idempotente — só grava quando o valor é diferente.
 */
if ( ! function_exists( 'aquametria_casca_fixar_tagline' ) ) {
function aquametria_casca_fixar_tagline( &$relato ) {
	$atual = (string) get_option( 'blogdescription' );
	if ( AQUAMETRIA_CASCA_TAGLINE_CURTA !== $atual ) {
		update_option( 'blogdescription', AQUAMETRIA_CASCA_TAGLINE_CURTA );
		$relato[] = 'blogdescription: ' . AQUAMETRIA_CASCA_TAGLINE_CURTA;
	}
}
}

if ( ! function_exists( 'aquametria_casca_limpar_padrao' ) ) {
function aquametria_casca_limpar_padrao( &$relato ) {
	if ( 'feito' === get_option( 'aquametria_casca_limpeza' ) ) {
		return;
	}

	$slugs = array( 'hello-world', 'ola-mundo', 'sample-page', 'pagina-exemplo', 'pagina-de-exemplo' );
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
		if ( '1' === get_post_meta( $p->ID, '_aquametria_casca', true ) ) {
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

	update_option( 'aquametria_casca_limpeza', 'feito', false );
}
}

if ( ! function_exists( 'aquametria_casca_montar' ) ) {
function aquametria_casca_montar( $forcar = false ) {
	$feita = get_option( 'aquametria_casca_estrutura' );
	$chave = aquametria_casca_chave_estrutura();
	if ( ! $forcar && $chave === $feita ) {
		return array();
	}

	$relato = array();
	$ids    = aquametria_casca_garantir_paginas( $relato );
	aquametria_casca_fixar_home( $ids, $relato );
	aquametria_casca_fixar_tagline( $relato );
	aquametria_casca_limpar_padrao( $relato );

	update_option( 'aquametria_casca_paginas', $ids, false );
	update_option( 'aquametria_casca_estrutura', $chave, false );

	if ( ! $relato ) {
		$relato[] = 'nada a fazer: estrutura já estava de pé';
	}
	$relato[] = 'casca ' . AQUAMETRIA_CASCA_VERSAO . ' (chave ' . $chave . ') em ' . current_time( 'Y-m-d H:i' );
	update_option( 'aquametria_casca_relato', $relato, false );

	return $relato;
}
}

if ( ! function_exists( 'aquametria_casca_boot' ) ) {
function aquametria_casca_boot() {
	static $ja = false;
	if ( $ja ) {
		return;
	}
	$ja = true;

	aquametria_casca_montar( false );

	// Remontagem manual: /?aquametria_casca=refazer (só para quem administra o site).
	$pedido = filter_input( INPUT_GET, 'aquametria_casca', FILTER_DEFAULT );
	if ( 'refazer' === $pedido && current_user_can( 'manage_options' ) ) {
		$relato = aquametria_casca_montar( true );
		nocache_headers();
		header( 'Content-Type: application/json; charset=utf-8' );
		echo wp_json_encode( array( 'versao' => AQUAMETRIA_CASCA_VERSAO, 'relato' => $relato ), JSON_UNESCAPED_UNICODE );
		exit;
	}
}
}

add_action( 'init', 'aquametria_casca_boot', 20 );

if ( did_action( 'init' ) ) {
	aquametria_casca_boot();
}
