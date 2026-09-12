/**
 * Clube do Mosaico Ateliê — painel da artesã
 * Versão 1.0.0 (12/09/2026) — bloco 4d, itens 2, 3 e 4 do CORTE do despacho do
 * Raphael das 18h20 BRT de 12/09/2026.
 *
 * O Raphael vai à casa dos pais no domingo 13/09 ensinar a própria mãe a
 * cadastrar as peças dela. É a primeira vez que alguém de fora da máquina vai
 * usar o que esta fábrica constrói, e é a mãe dele. Tudo neste arquivo responde a
 * uma pergunta só: **ela consegue fazer isso sozinha, do telefone, sem nunca
 * descobrir o que é WordPress?**
 *
 * ------------------------------------------------------------------------
 * AS SETE DECISÕES, e o que cada uma protege
 * ------------------------------------------------------------------------
 *
 * 1. ELA NUNCA VÊ O wp-admin, E O BLOQUEIO É DUPLO.
 *    `admin_init` devolve o papel `artesa` para /atelie/ antes de qualquer tela
 *    do WordPress ser montada, e `show_admin_bar` fica false para ela. Duas
 *    travas porque elas falham por motivos diferentes: a barra é cosmética e a
 *    outra é acesso, e a primeira vez que ela vir um menu "Posts / Mídia /
 *    Ferramentas" o despacho está descumprido mesmo que nada quebre.
 *
 * 2. A SENHA DELA NÃO EXISTE NESTE REPOSITÓRIO NEM EM LOG NENHUM.
 *    O snippet gera uma senha aleatória que ele DESCARTA sem imprimir, e o que
 *    chega a ela é um link de criação de senha, por e-mail, no endereço dela.
 *    Ninguém — nem o Raphael, nem a Fundação, nem quem ler o log do Sync — vê
 *    senha em nenhum momento. O que a Fundação consegue conferir é se o e-mail
 *    SAIU, e é só isso que ela precisa conferir.
 *
 * 3. A SENHA É CRIADA EM /atelie/, NÃO NO wp-login.php.
 *    Aqui está o desvio conscientemente feito da especificação de 10/09, e ele é
 *    a favor dela: o fluxo nativo do WordPress manda o link para uma tela com a
 *    marca do WordPress, campo "Nova senha" com medidor de força e um link
 *    "← Voltar para Clube do Mosaico". É a definição literal do que o portão
 *    deste despacho reprova ("se qualquer passo exigir saber o que é WordPress,
 *    não está pronto"). A chave de redefinição continua sendo a NATIVA, validada
 *    por `check_password_reset_key()` e consumida por `reset_password()` — nada
 *    de criptografia caseira —, mas a tela onde ela digita é a nossa, com o logo
 *    dela, e ao terminar ela já entra logada no painel. Um passo menos para
 *    explicar no domingo.
 *
 * 4. TUDO FUNCIONA SEM UMA LINHA DE JAVASCRIPT (portão 22.8).
 *    Login, cadastro, envio de fotos, reordenar, remover, publicar, pausar e
 *    apagar são formulários HTML com POST e `submit`. O JavaScript deste arquivo
 *    só acrescenta a pré-visualização das fotos escolhidas e a confirmação de
 *    apagar; desligado, o painel continua inteiro.
 *    É também por isso que reordenar foto é botão "◀ ▶" e não arrastar-e-soltar,
 *    que era o que a especificação pedia: arrastar depende de JavaScript e de
 *    precisão de dedo, e ela vai cadastrar de um celular. Dois botões grandes
 *    resolvem a mesma coisa e não têm como não funcionar.
 *
 * 5. O FORMULÁRIO É UMA TELA SÓ, E SALVAR NUNCA PERDE O QUE ELA DIGITOU.
 *    Uma peça nova nasce como rascunho no PRIMEIRO salvar, e as fotos são anexadas
 *    a ela na mesma requisição. Depois de todo POST há redirecionamento (POST →
 *    redirect → GET), então o botão Voltar do celular nunca reenvia o cadastro e
 *    nenhuma peça sai duplicada.
 *
 * 6. QUEM DECIDE SE A PEÇA PODE IR AO AR É A LOJA, NÃO ESTE ARQUIVO.
 *    `cdm_loja_peca_publicavel()` mora no snippet da Loja e devolve os MOTIVOS.
 *    Este painel só mostra os motivos e desabilita o botão. Uma segunda régua
 *    aqui é o defeito que a seção 8 chama de teste que mede a si mesmo, na versão
 *    mais cara: o painel deixaria publicar o que a loja recusa, e ela veria a
 *    peça sumir sem entender por quê.
 *
 * 7. O PAINEL É `noindex` E FORA DO SITEMAP.
 *    É a área dela, não é página de venda. A casca já tira do sitemap o que se
 *    declara `noindex` na definição de páginas, e é por lá que isto é declarado —
 *    uma linha, no mecanismo que já foi conferido, em vez de uma segunda regra.
 *
 * ------------------------------------------------------------------------
 * O QUE ESTE ARQUIVO NÃO FAZ, e não é esquecimento
 * ------------------------------------------------------------------------
 * Fora do corte de hoje, por escrito no despacho: o formulário "Verificar
 * disponibilidade" e o CPT `lead_peca` (adendo 3 de 11/09), a aba "Interessados",
 * a exportação CSV dos leads, "Meus dados", o feed do Merchant Center e as
 * páginas de coleção e de técnica. Voltam à fila depois de domingo.
 */

if ( ! defined( 'CDM_ATELIE_VERSAO' ) ) {
	define( 'CDM_ATELIE_VERSAO', '1.0.0' );
}
if ( ! defined( 'CDM_ATELIE_SLUG' ) ) {
	define( 'CDM_ATELIE_SLUG', 'atelie' );
}
if ( ! defined( 'CDM_ATELIE_PAPEL' ) ) {
	define( 'CDM_ATELIE_PAPEL', 'artesa' );
}
if ( ! defined( 'CDM_ATELIE_LOGIN' ) ) {
	define( 'CDM_ATELIE_LOGIN', 'artesa' );
}
if ( ! defined( 'CDM_ATELIE_EMAIL' ) ) {
	/* O e-mail da própria artesã, dado pelo Raphael em 11/09/2026. É para cá que
	   o link de criar senha vai, e é o único lugar onde ele vai. */
	define( 'CDM_ATELIE_EMAIL', 'mina196@hotmail.com' );
}
if ( ! defined( 'CDM_ATELIE_AVISO_PARA' ) ) {
	/* O Raphael recebe o AVISO de que o acesso foi enviado — nunca o link. */
	define( 'CDM_ATELIE_AVISO_PARA', 'raphaeh9@gmail.com' );
}
if ( ! defined( 'CDM_ATELIE_MAX_FOTOS' ) ) {
	define( 'CDM_ATELIE_MAX_FOTOS', 8 );
}

/* ---------------------------------------------------------------------------
 * 1. O PAPEL `artesa` — só as peças dela, e a biblioteca de mídia
 *
 * As capacidades são as do `capability_type` do CPT `peca` (snippet da Loja).
 * `edit_others_pecas` NÃO está aqui e é a ausência mais importante do arquivo:
 * é ela que faz o núcleo, por `map_meta_cap`, recusar que ela edite peça de
 * outra pessoa sem uma linha de verificação nossa no meio.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_atelie_capacidades' ) ) {
function cdm_atelie_capacidades() {
	return array(
		'read'                    => true,
		'upload_files'            => true,
		'edit_pecas'              => true,
		'publish_pecas'           => true,
		'delete_pecas'            => true,
		'edit_published_pecas'    => true,
		'delete_published_pecas'  => true,
	);
}
}

if ( ! function_exists( 'cdm_atelie_garantir_papel' ) ) {
/**
 * Cria o papel, ou reescreve as capacidades quando esta versão mudar.
 *
 * A marca em option existe porque `add_role()` não faz nada se o papel já
 * existir: sem ela, acrescentar uma capacidade num bloco futuro seria silencioso.
 */
function cdm_atelie_garantir_papel() {
	if ( ! function_exists( 'get_role' ) ) {
		return array();
	}
	$relato = array();
	$papel  = get_role( CDM_ATELIE_PAPEL );

	if ( ! $papel ) {
		add_role( CDM_ATELIE_PAPEL, 'Artesã', cdm_atelie_capacidades() );
		$relato[] = 'papel ' . CDM_ATELIE_PAPEL . ': criado';
		$papel    = get_role( CDM_ATELIE_PAPEL );
	}
	if ( $papel ) {
		foreach ( cdm_atelie_capacidades() as $cap => $tem ) {
			if ( empty( $papel->capabilities[ $cap ] ) ) {
				$papel->add_cap( $cap );
				$relato[] = 'papel ' . CDM_ATELIE_PAPEL . ': capacidade ' . $cap . ' acrescentada';
			}
		}
	}

	/* O ADMINISTRADOR TAMBÉM PRECISA DAS CAPACIDADES DE `peca`. Com
	   `capability_type` próprio, o papel administrator não as ganha sozinho — e
	   sem isto o Raphael não consegue nem ver a peça dela pelo REST, o que
	   transformaria qualquer socorro no domingo numa conversa sobre SQL. */
	$admin = get_role( 'administrator' );
	if ( $admin ) {
		$todas = array(
			'edit_pecas', 'publish_pecas', 'delete_pecas', 'edit_published_pecas',
			'delete_published_pecas', 'edit_others_pecas', 'delete_others_pecas',
			'read_private_pecas', 'edit_private_pecas', 'delete_private_pecas',
		);
		foreach ( $todas as $cap ) {
			if ( empty( $admin->capabilities[ $cap ] ) ) {
				$admin->add_cap( $cap );
				$relato[] = 'papel administrator: capacidade ' . $cap . ' acrescentada';
			}
		}
	}

	return $relato;
}
}

/* ---------------------------------------------------------------------------
 * 2. A USUÁRIA E O E-MAIL DE ACESSO — o item que tinha de sair mais cedo
 *
 * "Este item é o que precisa estar feito mais cedo, porque o e-mail tem de chegar
 * hoje e ele quer poder conferir antes de sair de casa" (despacho, item 2).
 *
 * Roda no `init` do site, ou seja: na primeira visita depois do Sync. Guardado por
 * option para não reenviar em toda visita — e-mail repetido para a Hotmail é o
 * caminho mais rápido para a caixa de spam, e caixa de spam aqui significa uma
 * pessoa esperando na frente do filho sem conseguir entrar.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_atelie_usuaria' ) ) {
/** A usuária da artesã, ou null. Procura pelo login e pelo e-mail. */
function cdm_atelie_usuaria() {
	if ( ! function_exists( 'get_user_by' ) ) {
		return null;
	}
	$u = get_user_by( 'login', CDM_ATELIE_LOGIN );
	if ( $u ) {
		return $u;
	}
	$u = get_user_by( 'email', CDM_ATELIE_EMAIL );

	return $u ? $u : null;
}
}

if ( ! function_exists( 'cdm_atelie_url' ) ) {
/** O endereço do painel. Uma função só, para o link nunca divergir. */
function cdm_atelie_url( $args = array() ) {
	$base = home_url( '/' . CDM_ATELIE_SLUG . '/' );
	if ( ! $args ) {
		return $base;
	}
	$partes = array();
	foreach ( $args as $k => $v ) {
		$partes[] = rawurlencode( (string) $k ) . '=' . rawurlencode( (string) $v );
	}

	return $base . '?' . implode( '&', $partes );
}
}

if ( ! function_exists( 'cdm_atelie_link_criar_senha' ) ) {
/**
 * O link de criar senha, apontando para O NOSSO painel (decisão 3).
 *
 * A chave é a nativa do WordPress. Se `get_password_reset_key()` falhar, devolve
 * '' — e quem chama NÃO manda e-mail com link quebrado, porque e-mail com link
 * quebrado é pior que e-mail nenhum: ela tenta, não funciona, e desiste.
 */
function cdm_atelie_link_criar_senha( $usuaria ) {
	if ( ! function_exists( 'get_password_reset_key' ) ) {
		return '';
	}
	$chave = get_password_reset_key( $usuaria );
	if ( is_wp_error( $chave ) || ! is_string( $chave ) || '' === $chave ) {
		return '';
	}

	return cdm_atelie_url( array(
		'criar-senha' => $chave,
		'quem'        => $usuaria->user_login,
	) );
}
}

if ( ! function_exists( 'cdm_atelie_email_html' ) ) {
/**
 * O e-mail de acesso: logo, uma frase, UM botão grande, e o endereço do painel.
 *
 * Tudo em tabela e com estilo embutido porque cliente de e-mail é 2003 para
 * sempre — a Hotmail joga fora `<style>` no `<head>` e não entende flexbox.
 * Sem imagem além do logo, que é URL absoluta na própria hospedagem.
 */
function cdm_atelie_email_html( $link ) {
	$logo = defined( 'CDM_CASCA_LOGO_URL' )
		? CDM_CASCA_LOGO_URL
		: 'https://clubedomosaico.com.br/wp-content/uploads/2026/09/logo-clube-do-mosaico.png';

	$h  = '<div style="margin:0;padding:24px 12px;background:#FFFFFF;font-family:Helvetica,Arial,sans-serif;color:#1F1715;">';
	$h .= '<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="max-width:520px;margin:0 auto;">';
	$h .= '<tr><td align="center" style="padding:0 0 24px;">';
	$h .= '<img src="' . esc_url( $logo ) . '" alt="Clube do Mosaico" width="180" style="display:block;width:180px;height:auto;border:0;">';
	$h .= '</td></tr>';
	$h .= '<tr><td style="padding:0 0 16px;">';
	$h .= '<h1 style="margin:0;font-size:24px;line-height:1.25;font-weight:600;color:#1F1715;">Seu ateliê está pronto</h1>';
	$h .= '</td></tr>';
	$h .= '<tr><td style="padding:0 0 20px;font-size:16px;line-height:1.6;color:#1F1715;">';
	$h .= 'O espaço onde você cadastra as suas peças já está no ar. Crie a sua senha no botão abaixo e você entra direto.';
	$h .= '</td></tr>';
	$h .= '<tr><td align="center" style="padding:0 0 24px;">';
	$h .= '<a href="' . esc_url( $link ) . '" style="display:inline-block;background:#FC483B;color:#FFFFFF;';
	$h .= 'font-size:18px;font-weight:700;text-decoration:none;padding:16px 28px;border-radius:8px;">';
	$h .= 'Criar minha senha e entrar</a>';
	$h .= '</td></tr>';
	$h .= '<tr><td style="padding:0 0 8px;font-size:15px;line-height:1.6;color:#6E5F5B;">';
	$h .= 'O endereço do seu painel, para guardar:<br>';
	$h .= '<a href="' . esc_url( cdm_atelie_url() ) . '" style="color:#8A0F18;">' . esc_html( cdm_atelie_url() ) . '</a>';
	$h .= '</td></tr>';
	$h .= '<tr><td style="padding:16px 0 0;border-top:1px solid #E9DCD7;font-size:13px;line-height:1.5;color:#6E5F5B;">';
	$h .= 'Se o botão não abrir, copie e cole este endereço no navegador:<br>' . esc_html( $link );
	$h .= '</td></tr>';
	$h .= '</table></div>';

	return $h;
}
}

if ( ! function_exists( 'cdm_atelie_enviar_html' ) ) {
/**
 * Manda um e-mail HTML e devolve o que o `wp_mail` respondeu.
 *
 * O filtro de tipo de conteúdo é posto e RETIRADO em volta do envio: deixá-lo
 * pendurado faria todo e-mail do site (redefinição de senha do admin, aviso de
 * comentário) sair como HTML cru em cliente de texto.
 */
function cdm_atelie_enviar_html( $para, $assunto, $corpo ) {
	if ( ! function_exists( 'wp_mail' ) ) {
		return false;
	}
	$tipo = function () {
		return 'text/html';
	};
	add_filter( 'wp_mail_content_type', $tipo );

	$de = array(
		'From: Clube do Mosaico <contato@' . preg_replace( '#^https?://(www\.)?#', '', home_url() ) . '>',
		'Content-Type: text/html; charset=UTF-8',
	);
	$ok = wp_mail( $para, $assunto, $corpo, $de );

	remove_filter( 'wp_mail_content_type', $tipo );

	return (bool) $ok;
}
}

if ( ! function_exists( 'cdm_atelie_garantir_usuaria' ) ) {
/**
 * Cria a usuária se ela não existir e manda o acesso UMA vez.
 *
 * O relato que ela devolve é gravado em option e servido pela rota REST do fim
 * deste arquivo — é por ele que a Fundação confere, da nuvem e sem senha, que o
 * e-mail saiu e a que horas. Sem isso, "o e-mail foi enviado" seria fé.
 */
function cdm_atelie_garantir_usuaria() {
	$relato = array( 'criada' => false, 'enviado' => false, 'erro' => '', 'quando' => '' );

	if ( ! function_exists( 'wp_insert_user' ) ) {
		$relato['erro'] = 'wp_insert_user indisponível';
		return $relato;
	}

	$u = cdm_atelie_usuaria();

	if ( ! $u ) {
		/* A SENHA NASCE ALEATÓRIA E MORRE AQUI. Não é impressa, não é gravada, não
		   é devolvida. O que vale é o link do e-mail. */
		$descartada = wp_generate_password( 24, true, false );
		$id         = wp_insert_user( array(
			'user_login'    => CDM_ATELIE_LOGIN,
			'user_email'    => CDM_ATELIE_EMAIL,
			'user_pass'     => $descartada,
			'display_name'  => 'Artesã',
			'first_name'    => 'Artesã',
			'role'          => CDM_ATELIE_PAPEL,
			'show_admin_bar_front' => 'false',
		) );
		unset( $descartada );

		if ( is_wp_error( $id ) ) {
			$relato['erro'] = 'wp_insert_user: ' . $id->get_error_message();
			return $relato;
		}
		$relato['criada'] = true;
		$u                = get_user_by( 'id', (int) $id );
	}

	if ( ! $u ) {
		$relato['erro'] = 'usuária não encontrada depois de criada';
		return $relato;
	}

	/* O PAPEL SE CORRIGE. Usuária que existir com outro papel (importada, criada à
	   mão) tem de acabar como artesã, senão o painel a recusa sem dizer por quê. */
	if ( ! in_array( CDM_ATELIE_PAPEL, (array) $u->roles, true ) && ! user_can( $u, 'manage_options' ) ) {
		$u->set_role( CDM_ATELIE_PAPEL );
	}

	$link = cdm_atelie_link_criar_senha( $u );
	if ( '' === $link ) {
		$relato['erro'] = 'get_password_reset_key falhou; e-mail não enviado';
		return $relato;
	}

	$relato['enviado'] = cdm_atelie_enviar_html(
		CDM_ATELIE_EMAIL,
		'Seu ateliê no Clube do Mosaico está pronto',
		cdm_atelie_email_html( $link )
	);
	$relato['quando'] = gmdate( 'c' );
	if ( ! $relato['enviado'] ) {
		$relato['erro'] = 'wp_mail devolveu false para ' . CDM_ATELIE_EMAIL;
	}

	/* O AVISO PARA O RAPHAEL — sem o link, como o despacho de 11/09 exige. */
	if ( $relato['enviado'] ) {
		cdm_atelie_enviar_html(
			CDM_ATELIE_AVISO_PARA,
			'Clube do Mosaico: o acesso da artesã foi enviado',
			'<p style="font-family:Helvetica,Arial,sans-serif;font-size:15px;color:#1F1715;">'
			. 'O e-mail com o link de criar senha foi enviado para ' . esc_html( CDM_ATELIE_EMAIL ) . '.'
			. ' O painel dela é <a href="' . esc_url( cdm_atelie_url() ) . '">' . esc_html( cdm_atelie_url() ) . '</a>.'
			. '<br><br>O link de senha não vai nesta mensagem, de propósito: ele chega só na caixa dela.</p>'
		);
	}

	return $relato;
}
}

add_action( 'init', function () {
	if ( ! function_exists( 'get_option' ) ) {
		return;
	}
	/* O papel primeiro, sempre: criar a usuária antes do papel existir a deixaria
	   com um papel que não concede nada. */
	$relato_papel = cdm_atelie_garantir_papel();
	if ( $relato_papel ) {
		update_option( 'cdm_atelie_papel_relato', $relato_papel, false );
	}

	/* O ACESSO SAI UMA VEZ. A marca guarda a versão E o e-mail: trocar o endereço
	   dela num bloco futuro tem de disparar um envio novo, e trocar a versão do
	   snippet não pode. */
	$marca = get_option( 'cdm_atelie_acesso' );
	$agora = CDM_ATELIE_EMAIL;
	if ( is_array( $marca ) && isset( $marca['para'] ) && $agora === $marca['para'] && ! empty( $marca['enviado'] ) ) {
		return;
	}

	$r = cdm_atelie_garantir_usuaria();
	update_option( 'cdm_atelie_acesso', array(
		'para'    => $agora,
		'criada'  => ! empty( $r['criada'] ),
		'enviado' => ! empty( $r['enviado'] ),
		'quando'  => isset( $r['quando'] ) ? $r['quando'] : '',
		'erro'    => isset( $r['erro'] ) ? $r['erro'] : '',
		'versao'  => CDM_ATELIE_VERSAO,
		/* Quantas vezes já tentou. Se a Hotmail estiver recusando, é este número
		   que diz que o problema é entrega e não código. */
		'tentativas' => ( is_array( $marca ) && isset( $marca['tentativas'] ) ? (int) $marca['tentativas'] : 0 ) + 1,
	), false );
}, 8 );

/* ---------------------------------------------------------------------------
 * 3. O BLOQUEIO DUPLO DO wp-admin
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_atelie_e_artesa' ) ) {
/** A pessoa logada é a artesã (e não uma administradora)? */
function cdm_atelie_e_artesa( $usuaria = null ) {
	if ( null === $usuaria ) {
		if ( ! function_exists( 'wp_get_current_user' ) ) {
			return false;
		}
		$usuaria = wp_get_current_user();
	}
	if ( ! $usuaria || empty( $usuaria->ID ) ) {
		return false;
	}
	if ( user_can( $usuaria, 'manage_options' ) ) {
		return false;
	}

	return in_array( CDM_ATELIE_PAPEL, (array) $usuaria->roles, true );
}
}

add_action( 'admin_init', function () {
	/* AJAX e REST não passam por aqui como tela; bloquear os dois quebraria o
	   envio de foto, que é feito por `media_handle_upload` numa requisição
	   normal, mas também o `admin-ajax` de qualquer plugin que ela nunca vê. */
	if ( defined( 'DOING_AJAX' ) && DOING_AJAX ) {
		return;
	}
	if ( ! cdm_atelie_e_artesa() ) {
		return;
	}
	wp_safe_redirect( cdm_atelie_url(), 302 );
	exit;
} );

add_filter( 'show_admin_bar', function ( $mostrar ) {
	return cdm_atelie_e_artesa() ? false : $mostrar;
} );

/* Depois de entrar, ela vai para o painel — nunca para o wp-admin. */
add_filter( 'login_redirect', function ( $destino, $pedido, $usuaria ) {
	if ( is_object( $usuaria ) && cdm_atelie_e_artesa( $usuaria ) ) {
		return cdm_atelie_url();
	}

	return $destino;
}, 10, 3 );

/* ---------------------------------------------------------------------------
 * 4. A PÁGINA — registrada na casca, `noindex`, fora do sitemap
 * ------------------------------------------------------------------------- */

add_filter( 'cdm_paginas', function ( $paginas ) {
	if ( ! is_array( $paginas ) ) {
		return $paginas;
	}
	/* `camada => privada` É A DECLARAÇÃO QUE FALTAVA À ILHA, e ela nasceu de um
	   portão reprovando. O `teste-casca.php` cobrava que a ÚNICA página fora do
	   índice fosse a de camada de prova (`/materiais/como-sabemos/`), porque
	   quando ele foi escrito era essa a única razão possível para um `noindex`
	   nesta ilha. O painel sai do índice por outro motivo — é a área de uma
	   pessoa, não um bastidor de método —, e as duas coisas precisam de
	   tratamentos opostos: a página de prova TEM de ser citada por outra página
	   (é prova de algo), e esta não pode ser citada por nenhuma, porque link
	   público para o painel é um convite a todo robô que passar.
	   Declarar a camada em vez de perdoar o slug `atelie` por nome é a regra da
	   seção 8: quem afirma sobre texto declara no markup o que é exceção. */
	$paginas[ CDM_ATELIE_SLUG ] = array(
		'titulo'   => 'Ateliê',
		'conteudo' => '[cdm_atelie]',
		'noindex'  => true,
		'camada'   => 'privada',
	);

	return $paginas;
} );

/* ---------------------------------------------------------------------------
 * 5. AS AÇÕES — POST, então redirecionamento, sempre (decisão 5)
 *
 * Tudo acontece no `template_redirect`, antes de uma linha de HTML sair: é o
 * único lugar onde ainda se pode redirecionar e onde a pessoa logada já é
 * conhecida. O `$_SERVER` não é lido em lugar nenhum (playbook, fase 4b: o
 * ModSecurity mata a gravação em silêncio) — o endereço de volta é sempre
 * `cdm_atelie_url()`.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_atelie_post' ) ) {
/**
 * Um campo do POST, como texto limpo.
 *
 * Aceita qualquer escalar e converte para texto, em vez de devolver o padrão para
 * tudo que não for string. Numa requisição HTTP todo campo chega como texto, então
 * a diferença nunca aparece no site — e foi justamente por isso que ela apareceu
 * na bancada primeiro, com um `99` inteiro fazendo o preço ser APAGADO em silêncio
 * em vez de gravado. Descartar calado um valor que veio preenchido é o pior dos
 * dois comportamentos possíveis; array continua caindo no padrão, porque array
 * aqui é campo que não existe no formulário.
 */
function cdm_atelie_post( $chave, $padrao = '' ) {
	if ( ! isset( $_POST[ $chave ] ) ) {
		return $padrao;
	}
	$v = wp_unslash( $_POST[ $chave ] );
	if ( is_string( $v ) ) {
		return trim( $v );
	}

	return is_scalar( $v ) ? trim( (string) $v ) : $padrao;
}
}

if ( ! function_exists( 'cdm_atelie_get' ) ) {
/**
 * Um campo da URL, como texto limpo.
 *
 * Lê `$_GET` e não `filter_input( INPUT_GET, ... )` pelo mesmo motivo que a F2
 * desta ilha: `filter_input` não vê o que a bancada escreve em `$_GET`, e uma
 * entrada que o teste não consegue variar é uma entrada que só o site conhece —
 * é a metade que a seção 8 diz que some em silêncio. O playbook proíbe `$_SERVER`
 * literal (o ModSecurity mata a gravação), não `$_GET`.
 */
function cdm_atelie_get( $chave, $padrao = '' ) {
	if ( ! isset( $_GET[ $chave ] ) ) {
		return $padrao;
	}
	$v = wp_unslash( $_GET[ $chave ] );

	return ( is_string( $v ) && '' !== $v ) ? trim( $v ) : $padrao;
}
}

if ( ! function_exists( 'cdm_atelie_e_minha_pagina' ) ) {
function cdm_atelie_e_minha_pagina() {
	return function_exists( 'cdm_casca_slug_atual' ) && CDM_ATELIE_SLUG === cdm_casca_slug_atual();
}
}

if ( ! function_exists( 'cdm_atelie_minha_peca' ) ) {
/**
 * A peça de id $id, se ela for dela.
 *
 * A verificação é `current_user_can( 'edit_post', $id )`, que o núcleo resolve
 * por `map_meta_cap` olhando o autor — e não uma comparação nossa de
 * `post_author`, que é a mesma régua escrita duas vezes.
 */
function cdm_atelie_minha_peca( $id ) {
	$id   = (int) $id;
	$peca = $id > 0 ? get_post( $id ) : null;
	if ( ! $peca || 'peca' !== $peca->post_type ) {
		return null;
	}
	if ( ! current_user_can( 'edit_post', $id ) ) {
		return null;
	}

	return $peca;
}
}

if ( ! function_exists( 'cdm_atelie_subir_fotos' ) ) {
/**
 * Anexa à peça as fotos que vieram no formulário, na ordem em que ela escolheu.
 *
 * Devolve array( 'entraram' => n, 'erros' => array ). Foto que falha NÃO derruba
 * o salvamento: ela é nomeada na tela e as outras entram. Perder o cadastro
 * inteiro porque a terceira foto estava num formato esquisito é o tipo de coisa
 * que faz alguém desistir do site.
 */
function cdm_atelie_subir_fotos( $peca_id ) {
	$saida = array( 'entraram' => 0, 'erros' => array() );

	if ( empty( $_FILES['fotos'] ) || ! is_array( $_FILES['fotos'] ) ) {
		return $saida;
	}
	if ( ! function_exists( 'media_handle_upload' ) ) {
		require_once ABSPATH . 'wp-admin/includes/file.php';
		require_once ABSPATH . 'wp-admin/includes/media.php';
		require_once ABSPATH . 'wp-admin/includes/image.php';
	}

	$nomes   = isset( $_FILES['fotos']['name'] ) ? (array) $_FILES['fotos']['name'] : array();
	$galeria = cdm_loja_galeria( $peca_id );

	foreach ( array_keys( $nomes ) as $i ) {
		if ( '' === (string) $_FILES['fotos']['name'][ $i ] ) {
			continue;
		}
		if ( count( $galeria ) >= CDM_ATELIE_MAX_FOTOS ) {
			$saida['erros'][] = 'Só cabem ' . CDM_ATELIE_MAX_FOTOS . ' fotos por peça; as últimas não entraram.';
			break;
		}
		/* `media_handle_upload` lê $_FILES[$chave] como arquivo único, então o
		   item do array é copiado para uma chave própria. É o caminho que o
		   próprio núcleo usa para campo múltiplo. */
		$_FILES['cdm_foto'] = array(
			'name'     => $_FILES['fotos']['name'][ $i ],
			'type'     => $_FILES['fotos']['type'][ $i ],
			'tmp_name' => $_FILES['fotos']['tmp_name'][ $i ],
			'error'    => $_FILES['fotos']['error'][ $i ],
			'size'     => $_FILES['fotos']['size'][ $i ],
		);
		$anexo = media_handle_upload( 'cdm_foto', (int) $peca_id );
		unset( $_FILES['cdm_foto'] );

		if ( is_wp_error( $anexo ) ) {
			$saida['erros'][] = 'A foto "' . $_FILES['fotos']['name'][ $i ] . '" não entrou: ' . $anexo->get_error_message();
			continue;
		}
		if ( ! wp_attachment_is_image( (int) $anexo ) ) {
			wp_delete_attachment( (int) $anexo, true );
			$saida['erros'][] = 'O arquivo "' . $_FILES['fotos']['name'][ $i ] . '" não é uma foto.';
			continue;
		}
		$galeria[] = (int) $anexo;
		$saida['entraram']++;
	}

	update_post_meta( $peca_id, '_cdm_galeria', $galeria );
	/* A capa também é a imagem destacada, que é o que o resto do WordPress e
	   qualquer rede social leem quando não leem a nossa galeria. */
	if ( $galeria ) {
		set_post_thumbnail( (int) $peca_id, (int) $galeria[0] );
	}

	return $saida;
}
}

if ( ! function_exists( 'cdm_atelie_salvar_campos' ) ) {
/** Grava os campos do formulário na peça, cada um pelo tipo declarado. */
function cdm_atelie_salvar_campos( $peca_id ) {
	foreach ( cdm_loja_campos() as $chave => $def ) {
		$campo = 'cdm' . $chave; // _cdm_preco → cdm_cdm_preco, sem colisão com o núcleo
		if ( ! isset( $_POST[ $campo ] ) ) {
			continue;
		}
		$bruto = cdm_atelie_post( $campo );

		switch ( $def['tipo'] ) {
			case 'decimal':
				/* Ela vai digitar 180,50 — é assim que se escreve preço em
				   português, e recusar a vírgula seria a tela ensinando a pessoa a
				   falar a língua do banco de dados. */
				$limpo = str_replace( array( '.', ' ' ), '', $bruto );
				$limpo = str_replace( ',', '.', $limpo );
				$limpo = preg_replace( '/[^0-9.]/', '', $limpo );
				$valor = ( '' === $limpo ) ? '' : (string) round( (float) $limpo, 2 );
				break;
			case 'inteiro':
				$so    = preg_replace( '/\D+/', '', $bruto );
				$valor = ( '' === $so ) ? '' : (string) (int) $so;
				break;
			case 'escolha':
				$opcoes = isset( $def['opcoes'] ) ? $def['opcoes'] : array();
				$valor  = isset( $opcoes[ $bruto ] ) ? $bruto : '';
				break;
			default:
				$valor = sanitize_text_field( $bruto );
		}

		if ( '' === $valor ) {
			delete_post_meta( $peca_id, $chave );
			continue;
		}
		update_post_meta( $peca_id, $chave, $valor );
	}

	/* Prazo só existe para peça sob encomenda: deixar o número de uma escolha
	   anterior gravado faria a ficha dizer "pronta entrega, feita em 20 dias". */
	if ( 'sob_encomenda' !== cdm_loja_meta( $peca_id, '_cdm_disponibilidade' ) ) {
		delete_post_meta( $peca_id, '_cdm_prazo_dias' );
	}

	/* As duas taxonomias, pelos termos que o formulário ofereceu. */
	foreach ( array( 'colecao', 'tecnica' ) as $taxonomia ) {
		if ( ! isset( $_POST[ 'cdm_' . $taxonomia ] ) ) {
			continue;
		}
		$slug  = sanitize_key( cdm_atelie_post( 'cdm_' . $taxonomia ) );
		$termo = ( '' !== $slug ) ? get_term_by( 'slug', $slug, $taxonomia ) : null;
		wp_set_object_terms( $peca_id, ( $termo && ! is_wp_error( $termo ) ) ? (int) $termo->term_id : array(), $taxonomia, false );
	}
}
}

if ( ! function_exists( 'cdm_atelie_agir' ) ) {
/**
 * O despachante das ações do painel. Redireciona sempre, e nunca imprime nada.
 *
 * Toda ação confere o nonce E a capacidade. Nonce sem capacidade protege contra
 * o site de fora e não contra a pessoa errada logada; capacidade sem nonce
 * protege contra a pessoa errada e não contra o formulário de outro site.
 */
function cdm_atelie_agir() {
	if ( ! cdm_atelie_e_minha_pagina() ) {
		return;
	}

	$acao = cdm_atelie_post( 'cdm_acao' );
	if ( '' === $acao ) {
		$acao = cdm_atelie_get( 'cdm_acao' );
	}
	if ( '' === $acao ) {
		return;
	}

	/* --- ENTRAR --- */
	if ( 'entrar' === $acao ) {
		if ( ! wp_verify_nonce( cdm_atelie_post( 'cdm_nonce' ), 'cdm_atelie_entrar' ) ) {
			wp_safe_redirect( cdm_atelie_url( array( 'aviso' => 'nonce' ) ) );
			exit;
		}
		$usuaria = wp_signon( array(
			'user_login'    => cdm_atelie_post( 'cdm_login' ),
			'user_password' => isset( $_POST['cdm_senha'] ) ? (string) wp_unslash( $_POST['cdm_senha'] ) : '',
			'remember'      => true,
		), is_ssl() );

		if ( is_wp_error( $usuaria ) ) {
			wp_safe_redirect( cdm_atelie_url( array( 'aviso' => 'login' ) ) );
			exit;
		}
		wp_safe_redirect( cdm_atelie_url() );
		exit;
	}

	/* --- SAIR --- */
	if ( 'sair' === $acao ) {
		if ( wp_verify_nonce( cdm_atelie_get( 'cdm_nonce' ), 'cdm_atelie_sair' ) ) {
			wp_logout();
		}
		wp_safe_redirect( cdm_atelie_url() );
		exit;
	}

	/* --- CRIAR SENHA --- */
	if ( 'criar_senha' === $acao ) {
		if ( ! wp_verify_nonce( cdm_atelie_post( 'cdm_nonce' ), 'cdm_atelie_criar_senha' ) ) {
			wp_safe_redirect( cdm_atelie_url( array( 'aviso' => 'nonce' ) ) );
			exit;
		}
		$login   = cdm_atelie_post( 'cdm_quem' );
		$chave   = cdm_atelie_post( 'cdm_chave' );
		$usuaria = check_password_reset_key( $chave, $login );
		if ( is_wp_error( $usuaria ) ) {
			wp_safe_redirect( cdm_atelie_url( array( 'aviso' => 'chave' ) ) );
			exit;
		}
		$nova  = isset( $_POST['cdm_senha'] ) ? (string) wp_unslash( $_POST['cdm_senha'] ) : '';
		$nova2 = isset( $_POST['cdm_senha2'] ) ? (string) wp_unslash( $_POST['cdm_senha2'] ) : '';
		if ( strlen( $nova ) < 8 ) {
			wp_safe_redirect( cdm_atelie_url( array( 'criar-senha' => $chave, 'quem' => $login, 'aviso' => 'curta' ) ) );
			exit;
		}
		if ( $nova !== $nova2 ) {
			wp_safe_redirect( cdm_atelie_url( array( 'criar-senha' => $chave, 'quem' => $login, 'aviso' => 'difere' ) ) );
			exit;
		}
		reset_password( $usuaria, $nova );
		/* Ela já entra logada: é o passo que o despacho não pede e que economiza a
		   explicação mais chata do domingo. */
		$logada = wp_signon( array(
			'user_login'    => $usuaria->user_login,
			'user_password' => $nova,
			'remember'      => true,
		), is_ssl() );
		unset( $nova, $nova2 );
		wp_safe_redirect( cdm_atelie_url( is_wp_error( $logada ) ? array( 'aviso' => 'entre' ) : array( 'aviso' => 'bemvinda' ) ) );
		exit;
	}

	/* --- ESQUECI A SENHA --- */
	if ( 'esqueci' === $acao ) {
		if ( ! wp_verify_nonce( cdm_atelie_post( 'cdm_nonce' ), 'cdm_atelie_esqueci' ) ) {
			wp_safe_redirect( cdm_atelie_url( array( 'aviso' => 'nonce' ) ) );
			exit;
		}
		/* A resposta é a MESMA com e-mail conhecido ou desconhecido: dizer "esse
		   e-mail não existe" entrega quem tem conta no site a quem perguntar. */
		$email   = sanitize_email( cdm_atelie_post( 'cdm_email' ) );
		$usuaria = $email ? get_user_by( 'email', $email ) : null;
		if ( $usuaria ) {
			$link = cdm_atelie_link_criar_senha( $usuaria );
			if ( '' !== $link ) {
				cdm_atelie_enviar_html(
					$usuaria->user_email,
					'Criar uma senha nova no Clube do Mosaico',
					cdm_atelie_email_html( $link )
				);
			}
		}
		wp_safe_redirect( cdm_atelie_url( array( 'aviso' => 'enviado' ) ) );
		exit;
	}

	/* Daqui para baixo é área dela: sem sessão, nada acontece. */
	if ( ! is_user_logged_in() || ! current_user_can( 'edit_pecas' ) ) {
		wp_safe_redirect( cdm_atelie_url( array( 'aviso' => 'entre' ) ) );
		exit;
	}

	/* --- SALVAR (nova ou existente) --- */
	if ( 'salvar' === $acao ) {
		if ( ! wp_verify_nonce( cdm_atelie_post( 'cdm_nonce' ), 'cdm_atelie_salvar' ) ) {
			wp_safe_redirect( cdm_atelie_url( array( 'aviso' => 'nonce' ) ) );
			exit;
		}
		$id      = (int) cdm_atelie_post( 'cdm_peca', '0' );
		$titulo  = sanitize_text_field( cdm_atelie_post( 'cdm_titulo' ) );
		$texto   = wp_kses_post( isset( $_POST['cdm_descricao'] ) ? (string) wp_unslash( $_POST['cdm_descricao'] ) : '' );
		$destino = ( 'publicar' === cdm_atelie_post( 'cdm_destino' ) ) ? 'publicar' : 'rascunho';

		if ( '' === $titulo ) {
			wp_safe_redirect( cdm_atelie_url( array( 'estado' => 'nova', 'aviso' => 'semtitulo' ) ) );
			exit;
		}

		if ( $id > 0 ) {
			if ( ! cdm_atelie_minha_peca( $id ) ) {
				wp_safe_redirect( cdm_atelie_url( array( 'aviso' => 'nao-sua' ) ) );
				exit;
			}
			wp_update_post( array( 'ID' => $id, 'post_title' => $titulo, 'post_content' => $texto ) );
		} else {
			if ( ! current_user_can( 'edit_pecas' ) ) {
				wp_safe_redirect( cdm_atelie_url( array( 'aviso' => 'nao-sua' ) ) );
				exit;
			}
			$id = wp_insert_post( array(
				'post_type'      => 'peca',
				'post_title'     => $titulo,
				'post_content'   => $texto,
				'post_status'    => 'draft',
				'post_author'    => get_current_user_id(),
				'comment_status' => 'closed',
				'ping_status'    => 'closed',
			), true );
			if ( is_wp_error( $id ) ) {
				wp_safe_redirect( cdm_atelie_url( array( 'estado' => 'nova', 'aviso' => 'erro' ) ) );
				exit;
			}
			$id = (int) $id;
		}

		cdm_atelie_salvar_campos( $id );
		$fotos = cdm_atelie_subir_fotos( $id );
		if ( ! empty( $fotos['erros'] ) ) {
			update_post_meta( $id, '_cdm_aviso_fotos', $fotos['erros'] );
		} else {
			delete_post_meta( $id, '_cdm_aviso_fotos' );
		}

		if ( 'publicar' === $destino ) {
			$motivos = cdm_loja_peca_publicavel( $id );
			if ( $motivos ) {
				update_post_meta( $id, '_cdm_recusa', $motivos );
				wp_safe_redirect( cdm_atelie_url( array( 'estado' => 'editar', 'peca' => $id, 'aviso' => 'falta' ) ) );
				exit;
			}
			wp_update_post( array( 'ID' => $id, 'post_status' => 'publish' ) );
			wp_safe_redirect( cdm_atelie_url( array( 'aviso' => 'publicada', 'peca' => $id ) ) );
			exit;
		}

		wp_safe_redirect( cdm_atelie_url( array( 'estado' => 'editar', 'peca' => $id, 'aviso' => 'salva' ) ) );
		exit;
	}

	/* --- PUBLICAR / PAUSAR / EXCLUIR, e as fotos --- */
	$id   = (int) cdm_atelie_post( 'cdm_peca', '0' );
	$peca = cdm_atelie_minha_peca( $id );
	if ( ! $peca ) {
		wp_safe_redirect( cdm_atelie_url( array( 'aviso' => 'nao-sua' ) ) );
		exit;
	}

	if ( 'publicar' === $acao ) {
		if ( ! wp_verify_nonce( cdm_atelie_post( 'cdm_nonce' ), 'cdm_atelie_peca_' . $id ) ) {
			wp_safe_redirect( cdm_atelie_url( array( 'aviso' => 'nonce' ) ) );
			exit;
		}
		$motivos = cdm_loja_peca_publicavel( $id );
		if ( $motivos ) {
			update_post_meta( $id, '_cdm_recusa', $motivos );
			wp_safe_redirect( cdm_atelie_url( array( 'estado' => 'editar', 'peca' => $id, 'aviso' => 'falta' ) ) );
			exit;
		}
		wp_update_post( array( 'ID' => $id, 'post_status' => 'publish' ) );
		wp_safe_redirect( cdm_atelie_url( array( 'aviso' => 'publicada', 'peca' => $id ) ) );
		exit;
	}

	if ( 'pausar' === $acao ) {
		if ( ! wp_verify_nonce( cdm_atelie_post( 'cdm_nonce' ), 'cdm_atelie_peca_' . $id ) ) {
			wp_safe_redirect( cdm_atelie_url( array( 'aviso' => 'nonce' ) ) );
			exit;
		}
		wp_update_post( array( 'ID' => $id, 'post_status' => 'draft' ) );
		wp_safe_redirect( cdm_atelie_url( array( 'aviso' => 'pausada', 'peca' => $id ) ) );
		exit;
	}

	if ( 'excluir' === $acao ) {
		if ( ! wp_verify_nonce( cdm_atelie_post( 'cdm_nonce' ), 'cdm_atelie_peca_' . $id ) ) {
			wp_safe_redirect( cdm_atelie_url( array( 'aviso' => 'nonce' ) ) );
			exit;
		}
		/* LIXEIRA, não exclusão definitiva. Ela aperta "Apagar" com o dedo num
		   telefone; a peça tem de dar para voltar. */
		wp_trash_post( $id );
		wp_safe_redirect( cdm_atelie_url( array( 'aviso' => 'apagada' ) ) );
		exit;
	}

	/* TRÊS AÇÕES SEPARADAS, e não uma com um campo de direção. A primeira versão
	   deste bloco era `foto_mover` mais um `<input type="hidden" name="cdm_direcao">`
	   — e um campo escondido é enviado seja qual for o botão apertado, então o ▶
	   mandava "para trás" junto e a foto andava para o lado errado. Botão só
	   carrega o próprio par nome/valor: quem escolhe a direção é o `value` do
	   botão, que é a única coisa que o navegador garante. */
	if ( 'foto_tras' === $acao || 'foto_frente' === $acao || 'foto_remover' === $acao ) {
		if ( ! wp_verify_nonce( cdm_atelie_post( 'cdm_nonce' ), 'cdm_atelie_peca_' . $id ) ) {
			wp_safe_redirect( cdm_atelie_url( array( 'aviso' => 'nonce' ) ) );
			exit;
		}
		$anexo   = (int) cdm_atelie_post( 'cdm_anexo', '0' );
		$galeria = cdm_loja_galeria( $id );
		$pos     = array_search( $anexo, $galeria, true );

		if ( false !== $pos ) {
			if ( 'foto_remover' === $acao ) {
				array_splice( $galeria, $pos, 1 );
			} else {
				$passo = ( 'foto_tras' === $acao ) ? -1 : 1;
				$alvo  = $pos + $passo;
				if ( $alvo >= 0 && $alvo < count( $galeria ) ) {
					$guarda           = $galeria[ $alvo ];
					$galeria[ $alvo ] = $galeria[ $pos ];
					$galeria[ $pos ]  = $guarda;
				}
			}
			update_post_meta( $id, '_cdm_galeria', array_values( $galeria ) );
			if ( $galeria ) {
				set_post_thumbnail( $id, (int) $galeria[0] );
			} else {
				delete_post_thumbnail( $id );
			}
		}
		wp_safe_redirect( cdm_atelie_url( array( 'estado' => 'editar', 'peca' => $id, 'aviso' => 'fotos' ) ) );
		exit;
	}
}
}

add_action( 'template_redirect', 'cdm_atelie_agir', 5 );

/* ---------------------------------------------------------------------------
 * 6. AS TELAS
 *
 * Três, e nenhuma pede saber o que é WordPress: entrar, a lista das peças, e o
 * formulário. Mais a tela de criar senha, que é a primeira que ela vai ver na
 * vida deste site.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_atelie_avisos' ) ) {
/** O texto de cada aviso. Em português de gente, sem código de erro na tela. */
function cdm_atelie_avisos() {
	return array(
		'bemvinda'  => array( 'bom', 'Pronto! Sua senha está criada e você já está no seu ateliê.' ),
		'salva'     => array( 'bom', 'Salvo. A peça está guardada como rascunho — ela ainda não aparece no site.' ),
		'publicada' => array( 'bom', 'Publicada! A peça já está no site.' ),
		'pausada'   => array( 'bom', 'Pausada. A peça saiu do site e continua guardada aqui.' ),
		'apagada'   => array( 'bom', 'A peça foi apagada.' ),
		'fotos'     => array( 'bom', 'Fotos atualizadas.' ),
		'enviado'   => array( 'bom', 'Se esse e-mail tem conta aqui, o link para criar a senha já está na caixa de entrada.' ),
		'falta'     => array( 'atencao', 'Quase! Falta uma coisa para a peça poder ir ao site — está escrito em vermelho embaixo.' ),
		'semtitulo' => array( 'atencao', 'A peça precisa de um nome para ser guardada.' ),
		'login'     => array( 'atencao', 'Esse nome ou essa senha não deram certo. Tente de novo.' ),
		'entre'     => array( 'atencao', 'Entre com a sua senha para continuar.' ),
		'curta'     => array( 'atencao', 'A senha precisa ter pelo menos 8 letras ou números.' ),
		'difere'    => array( 'atencao', 'As duas senhas que você digitou não são iguais.' ),
		'chave'     => array( 'atencao', 'Esse link de criar senha já foi usado ou passou da validade. Peça um novo abaixo.' ),
		'nonce'     => array( 'atencao', 'A página ficou aberta tempo demais e o envio expirou. Tente de novo.' ),
		'nao-sua'   => array( 'atencao', 'Essa peça não está no seu ateliê.' ),
		'erro'      => array( 'atencao', 'Algo deu errado ao guardar. Tente de novo.' ),
	);
}
}

if ( ! function_exists( 'cdm_atelie_aviso_html' ) ) {
function cdm_atelie_aviso_html() {
	$chave  = cdm_atelie_get( 'aviso' );
	$avisos = cdm_atelie_avisos();
	if ( '' === $chave || ! isset( $avisos[ $chave ] ) ) {
		return '';
	}
	list( $tom, $texto ) = $avisos[ $chave ];

	return '<p class="cdm-at-aviso cdm-at-aviso-' . esc_attr( $tom ) . '" role="status">' . esc_html( $texto ) . '</p>';
}
}

if ( ! function_exists( 'cdm_atelie_tela_entrar' ) ) {
function cdm_atelie_tela_entrar() {
	$h  = '<div class="cdm-at cdm-at-entrar">';
	$h .= cdm_atelie_aviso_html();
	$h .= '<h2 class="cdm-at-h2">Entrar no meu ateliê</h2>';
	$h .= '<p class="cdm-at-linha">Aqui é onde você cadastra as suas peças e decide quais aparecem no site.</p>';

	$h .= '<form class="cdm-at-form" method="post" action="' . esc_url( cdm_atelie_url() ) . '">';
	$h .= wp_nonce_field( 'cdm_atelie_entrar', 'cdm_nonce', true, false );
	$h .= '<input type="hidden" name="cdm_acao" value="entrar">';
	$h .= '<p class="cdm-at-campo"><label for="cdm-login">Seu nome de entrada</label>';
	$h .= '<input id="cdm-login" name="cdm_login" type="text" autocomplete="username" autocapitalize="none" spellcheck="false" required value="' . esc_attr( CDM_ATELIE_LOGIN ) . '"></p>';
	$h .= '<p class="cdm-at-campo"><label for="cdm-senha">Sua senha</label>';
	$h .= '<input id="cdm-senha" name="cdm_senha" type="password" autocomplete="current-password" required></p>';
	$h .= '<p class="cdm-at-acao"><button class="cdm-botao cdm-at-botao" type="submit">Entrar</button></p>';
	$h .= '</form>';

	$h .= '<details class="cdm-at-detalhe"><summary>Esqueci minha senha</summary>';
	$h .= '<form class="cdm-at-form" method="post" action="' . esc_url( cdm_atelie_url() ) . '">';
	$h .= wp_nonce_field( 'cdm_atelie_esqueci', 'cdm_nonce', true, false );
	$h .= '<input type="hidden" name="cdm_acao" value="esqueci">';
	$h .= '<p class="cdm-at-campo"><label for="cdm-email">Seu e-mail</label>';
	$h .= '<input id="cdm-email" name="cdm_email" type="email" autocomplete="email" required></p>';
	$h .= '<p class="cdm-at-acao"><button class="cdm-at-botao cdm-at-botao-fraco" type="submit">Mandar um link para criar senha nova</button></p>';
	$h .= '</form></details>';

	$h .= '</div>';

	return $h;
}
}

if ( ! function_exists( 'cdm_atelie_tela_criar_senha' ) ) {
function cdm_atelie_tela_criar_senha( $chave, $quem ) {
	$usuaria = check_password_reset_key( $chave, $quem );

	$h = '<div class="cdm-at cdm-at-entrar">';
	$h .= cdm_atelie_aviso_html();

	if ( is_wp_error( $usuaria ) ) {
		$h .= '<h2 class="cdm-at-h2">Esse link não vale mais</h2>';
		$h .= '<p class="cdm-at-linha">Links de criar senha valem por pouco tempo, por segurança. Peça um novo aqui embaixo e ele chega no seu e-mail em alguns minutos.</p>';
		$h .= '<form class="cdm-at-form" method="post" action="' . esc_url( cdm_atelie_url() ) . '">';
		$h .= wp_nonce_field( 'cdm_atelie_esqueci', 'cdm_nonce', true, false );
		$h .= '<input type="hidden" name="cdm_acao" value="esqueci">';
		$h .= '<p class="cdm-at-campo"><label for="cdm-email">Seu e-mail</label>';
		$h .= '<input id="cdm-email" name="cdm_email" type="email" autocomplete="email" required></p>';
		$h .= '<p class="cdm-at-acao"><button class="cdm-botao cdm-at-botao" type="submit">Mandar link novo</button></p>';
		$h .= '</form></div>';

		return $h;
	}

	$h .= '<h2 class="cdm-at-h2">Crie a sua senha</h2>';
	$h .= '<p class="cdm-at-linha">É só escolher uma senha que você lembre. Depois disso você já entra.</p>';
	$h .= '<form class="cdm-at-form" method="post" action="' . esc_url( cdm_atelie_url() ) . '">';
	$h .= wp_nonce_field( 'cdm_atelie_criar_senha', 'cdm_nonce', true, false );
	$h .= '<input type="hidden" name="cdm_acao" value="criar_senha">';
	$h .= '<input type="hidden" name="cdm_chave" value="' . esc_attr( $chave ) . '">';
	$h .= '<input type="hidden" name="cdm_quem" value="' . esc_attr( $quem ) . '">';
	$h .= '<p class="cdm-at-campo"><label for="cdm-senha">Sua senha nova</label>';
	$h .= '<input id="cdm-senha" name="cdm_senha" type="password" autocomplete="new-password" minlength="8" required>';
	$h .= '<span class="cdm-at-ajuda">Pelo menos 8 letras ou números.</span></p>';
	$h .= '<p class="cdm-at-campo"><label for="cdm-senha2">Digite a senha outra vez</label>';
	$h .= '<input id="cdm-senha2" name="cdm_senha2" type="password" autocomplete="new-password" minlength="8" required></p>';
	$h .= '<p class="cdm-at-acao"><button class="cdm-botao cdm-at-botao" type="submit">Criar minha senha e entrar</button></p>';
	$h .= '</form></div>';

	return $h;
}
}

if ( ! function_exists( 'cdm_atelie_estado_rotulo' ) ) {
function cdm_atelie_estado_rotulo( $estado ) {
	if ( 'publish' === $estado ) {
		return array( 'no-ar', 'No site' );
	}
	if ( 'trash' === $estado ) {
		return array( 'fora', 'Apagada' );
	}

	return array( 'fora', 'Rascunho' );
}
}

if ( ! function_exists( 'cdm_atelie_tela_lista' ) ) {
function cdm_atelie_tela_lista( $usuaria ) {
	$pecas = get_posts( array(
		'post_type'   => 'peca',
		'post_status' => array( 'publish', 'draft', 'pending' ),
		'author'      => (int) $usuaria->ID,
		'numberposts' => 100,
		'orderby'     => 'modified',
		'order'       => 'DESC',
	) );

	$nome = trim( (string) $usuaria->first_name );
	if ( '' === $nome ) {
		$nome = trim( (string) $usuaria->display_name );
	}

	$h  = '<div class="cdm-at">';
	$h .= cdm_atelie_aviso_html();

	$h .= '<div class="cdm-at-cabeca">';
	$h .= '<h2 class="cdm-at-h2">Olá, ' . esc_html( '' !== $nome ? $nome : 'artesã' ) . '</h2>';
	$h .= '<p class="cdm-at-sair"><a href="' . esc_url( cdm_atelie_url( array(
		'cdm_acao'  => 'sair',
		'cdm_nonce' => wp_create_nonce( 'cdm_atelie_sair' ),
	) ) ) . '">Sair</a></p>';
	$h .= '</div>';

	$h .= '<p class="cdm-at-acao cdm-at-acao-grande">';
	$h .= '<a class="cdm-botao cdm-at-botao" href="' . esc_url( cdm_atelie_url( array( 'estado' => 'nova' ) ) ) . '">+ Nova peça</a>';
	$h .= '</p>';

	if ( ! $pecas ) {
		$h .= '<div class="cdm-vazio">';
		$h .= '<h3>Nenhuma peça ainda</h3>';
		$h .= '<p>Toque em <strong>Nova peça</strong> e comece pela foto. Você pode guardar como rascunho e terminar depois — nada vai para o site antes de você tocar em Publicar.</p>';
		$h .= '</div></div>';

		return $h;
	}

	$h .= '<ul class="cdm-at-lista">';
	foreach ( $pecas as $p ) {
		$id = (int) $p->ID;
		list( $classe, $rotulo ) = cdm_atelie_estado_rotulo( $p->post_status );
		$galeria = cdm_loja_galeria( $id );
		$nonce   = wp_create_nonce( 'cdm_atelie_peca_' . $id );

		$h .= '<li class="cdm-at-item">';
		if ( $galeria ) {
			$src = wp_get_attachment_image_src( (int) $galeria[0], 'thumbnail' );
			if ( $src && ! empty( $src[0] ) ) {
				$h .= '<img class="cdm-at-mini" src="' . esc_url( $src[0] ) . '" width="72" height="72" alt="" decoding="async">';
			}
		} else {
			$h .= '<span class="cdm-at-mini cdm-at-mini-vazia" aria-hidden="true"></span>';
		}

		$h .= '<div class="cdm-at-item-texto">';
		$h .= '<h3>' . esc_html( $p->post_title ) . '</h3>';
		$preco = cdm_loja_preco_html( cdm_loja_meta( $id, '_cdm_preco' ) );
		$h .= '<p><span class="cdm-at-etiqueta cdm-at-etiqueta-' . esc_attr( $classe ) . '">' . esc_html( $rotulo ) . '</span>';
		if ( '' !== $preco ) {
			$h .= ' <span class="cdm-preco">' . $preco . '</span>';
		}
		$h .= '</p>';

		$recusa = get_post_meta( $id, '_cdm_recusa', true );
		if ( is_array( $recusa ) && $recusa && 'publish' !== $p->post_status ) {
			$h .= '<p class="cdm-at-falta">Para ir ao site, falta: ' . esc_html( implode( ' ', $recusa ) ) . '</p>';
		}

		$h .= '<p class="cdm-at-item-acoes">';
		$h .= '<a href="' . esc_url( cdm_atelie_url( array( 'estado' => 'editar', 'peca' => $id ) ) ) . '">Editar</a>';
		if ( 'publish' === $p->post_status ) {
			$h .= ' <a href="' . esc_url( get_permalink( $p ) ) . '">Ver no site</a>';
		}
		$h .= '</p>';

		/* Publicar/Pausar é POST com nonce, em formulário próprio: ação que muda o
		   site nunca sai de um link, que qualquer visita de robô segue. */
		$h .= '<form class="cdm-at-mini-form" method="post" action="' . esc_url( cdm_atelie_url() ) . '">';
		$h .= '<input type="hidden" name="cdm_nonce" value="' . esc_attr( $nonce ) . '">';
		$h .= '<input type="hidden" name="cdm_peca" value="' . $id . '">';
		if ( 'publish' === $p->post_status ) {
			$h .= '<button class="cdm-at-botao-fraco" type="submit" name="cdm_acao" value="pausar">Tirar do site</button>';
		} else {
			$h .= '<button class="cdm-at-botao-fraco" type="submit" name="cdm_acao" value="publicar">Publicar</button>';
		}
		$h .= '<button class="cdm-at-botao-fraco cdm-at-apagar" type="submit" name="cdm_acao" value="excluir" data-cdm-confirmar="Apagar a peça ' . esc_attr( $p->post_title ) . '?">Apagar</button>';
		$h .= '</form>';

		$h .= '</div></li>';
	}
	$h .= '</ul></div>';

	return $h;
}
}

if ( ! function_exists( 'cdm_atelie_tela_form' ) ) {
function cdm_atelie_tela_form( $peca ) {
	$id     = $peca ? (int) $peca->ID : 0;
	$campos = cdm_loja_campos();
	$nonce  = $id > 0 ? wp_create_nonce( 'cdm_atelie_peca_' . $id ) : '';

	$h  = '<div class="cdm-at">';
	$h .= cdm_atelie_aviso_html();

	$h .= '<div class="cdm-at-cabeca">';
	$h .= '<h2 class="cdm-at-h2">' . ( $id > 0 ? 'Editar peça' : 'Nova peça' ) . '</h2>';
	$h .= '<p class="cdm-at-sair"><a href="' . esc_url( cdm_atelie_url() ) . '">← Minhas peças</a></p>';
	$h .= '</div>';

	if ( $id > 0 ) {
		$recusa = get_post_meta( $id, '_cdm_recusa', true );
		if ( is_array( $recusa ) && $recusa && 'publish' !== $peca->post_status ) {
			$h .= '<ul class="cdm-at-faltas">';
			foreach ( $recusa as $m ) {
				$h .= '<li>' . esc_html( $m ) . '</li>';
			}
			$h .= '</ul>';
		}
		$avisos = get_post_meta( $id, '_cdm_aviso_fotos', true );
		if ( is_array( $avisos ) && $avisos ) {
			$h .= '<ul class="cdm-at-faltas">';
			foreach ( $avisos as $m ) {
				$h .= '<li>' . esc_html( $m ) . '</li>';
			}
			$h .= '</ul>';
		}
	}

	/* AS FOTOS QUE JÁ ESTÃO NA PEÇA, com mover e remover. Fora do formulário
	   grande de propósito: um formulário dentro de outro é HTML inválido, e
	   remover uma foto não pode exigir salvar o resto. */
	if ( $id > 0 ) {
		$galeria = cdm_loja_galeria( $id );
		if ( $galeria ) {
			$h .= '<div class="cdm-at-galeria"><h3 class="cdm-at-h3">Fotos desta peça</h3>';
			$h .= '<p class="cdm-at-ajuda">A primeira é a capa — é ela que aparece na lista da loja.</p>';
			$h .= '<ul class="cdm-at-fotos">';
			$total = count( $galeria );
			foreach ( $galeria as $i => $anexo ) {
				$src = wp_get_attachment_image_src( (int) $anexo, 'thumbnail' );
				$h  .= '<li class="cdm-at-foto">';
				if ( $src && ! empty( $src[0] ) ) {
					$h .= '<img src="' . esc_url( $src[0] ) . '" width="110" height="110" alt="" decoding="async">';
				}
				if ( 0 === $i ) {
					$h .= '<span class="cdm-at-capa">Capa</span>';
				}
				$h .= '<form method="post" action="' . esc_url( cdm_atelie_url() ) . '">';
				$h .= '<input type="hidden" name="cdm_nonce" value="' . esc_attr( $nonce ) . '">';
				$h .= '<input type="hidden" name="cdm_peca" value="' . $id . '">';
				$h .= '<input type="hidden" name="cdm_anexo" value="' . (int) $anexo . '">';
				if ( $i > 0 ) {
					$h .= '<button type="submit" name="cdm_acao" value="foto_tras" class="cdm-at-fbotao" title="Mover para trás">';
					$h .= '<span aria-hidden="true">◀</span><span class="cdm-at-so-leitor"> mover para trás</span></button>';
				}
				if ( $i < $total - 1 ) {
					$h .= '<button type="submit" name="cdm_acao" value="foto_frente" class="cdm-at-fbotao" title="Mover para frente">';
					$h .= '<span aria-hidden="true">▶</span><span class="cdm-at-so-leitor"> mover para frente</span></button>';
				}
				$h .= '<button type="submit" name="cdm_acao" value="foto_remover" class="cdm-at-fbotao cdm-at-apagar" ';
				$h .= 'data-cdm-confirmar="Remover esta foto?" title="Remover">';
				$h .= '<span aria-hidden="true">✕</span><span class="cdm-at-so-leitor"> remover</span></button>';
				$h .= '</form></li>';
			}
			$h .= '</ul></div>';
		}
	}

	$h .= '<form class="cdm-at-form cdm-at-form-peca" method="post" enctype="multipart/form-data" action="' . esc_url( cdm_atelie_url() ) . '">';
	$h .= wp_nonce_field( 'cdm_atelie_salvar', 'cdm_nonce', true, false );
	$h .= '<input type="hidden" name="cdm_acao" value="salvar">';
	$h .= '<input type="hidden" name="cdm_peca" value="' . $id . '">';

	$h .= '<p class="cdm-at-campo"><label for="cdm-titulo">Nome da peça</label>';
	$h .= '<input id="cdm-titulo" name="cdm_titulo" type="text" required maxlength="120" value="';
	$h .= esc_attr( $peca ? $peca->post_title : '' ) . '">';
	$h .= '<span class="cdm-at-ajuda">Como você chamaria a peça. Ex.: Vaso azul com flores.</span></p>';

	/* FOTOS. `accept="image/*"` com `capture` ausente: no celular o próprio
	   sistema oferece câmera E galeria, que é o que ela precisa. `multiple`
	   deixa escolher várias de uma vez. */
	$h .= '<p class="cdm-at-campo cdm-at-campo-fotos"><label for="cdm-fotos">Fotos</label>';
	$h .= '<input id="cdm-fotos" name="fotos[]" type="file" accept="image/*" multiple>';
	$h .= '<span class="cdm-at-ajuda">Você pode escolher várias de uma vez, até ' . CDM_ATELIE_MAX_FOTOS . '. ';
	$h .= 'A primeira vira a capa, e depois de salvar você pode trocar a ordem.</span></p>';
	$h .= '<div id="cdm-at-previa" class="cdm-at-previa" hidden></div>';

	$h .= '<p class="cdm-at-campo"><label for="cdm-descricao">Sobre a peça</label>';
	$h .= '<textarea id="cdm-descricao" name="cdm_descricao" rows="5">';
	$h .= esc_html( $peca ? $peca->post_content : '' ) . '</textarea>';
	$h .= '<span class="cdm-at-ajuda">Conte com as suas palavras: o que é, como você fez, para que serve.</span></p>';

	foreach ( $campos as $chave => $def ) {
		$campo = 'cdm' . $chave;
		$valor = $id > 0 ? cdm_loja_meta( $id, $chave ) : '';
		$idhtml = 'cdm-' . trim( str_replace( '_', '-', $chave ), '-' );

		$h .= '<p class="cdm-at-campo"><label for="' . esc_attr( $idhtml ) . '">' . esc_html( $def['rotulo'] ) . '</label>';

		if ( 'escolha' === $def['tipo'] ) {
			$h .= '<select id="' . esc_attr( $idhtml ) . '" name="' . esc_attr( $campo ) . '">';
			$h .= '<option value="">Escolha</option>';
			foreach ( $def['opcoes'] as $ov => $or ) {
				$h .= '<option value="' . esc_attr( $ov ) . '"' . ( $valor === $ov ? ' selected' : '' ) . '>';
				$h .= esc_html( $or ) . '</option>';
			}
			$h .= '</select>';
		} elseif ( 'decimal' === $def['tipo'] ) {
			/* `inputmode="decimal"` abre o teclado de número no celular sem
			   recusar a vírgula, que `type="number"` recusaria. */
			$h .= '<input id="' . esc_attr( $idhtml ) . '" name="' . esc_attr( $campo ) . '" type="text" ';
			$h .= 'inputmode="decimal" value="' . esc_attr( $valor ) . '">';
		} elseif ( 'inteiro' === $def['tipo'] ) {
			$h .= '<input id="' . esc_attr( $idhtml ) . '" name="' . esc_attr( $campo ) . '" type="text" ';
			$h .= 'inputmode="numeric" value="' . esc_attr( $valor ) . '">';
		} else {
			$h .= '<input id="' . esc_attr( $idhtml ) . '" name="' . esc_attr( $campo ) . '" type="text" ';
			$h .= 'value="' . esc_attr( $valor ) . '">';
		}

		$h .= '<span class="cdm-at-ajuda">' . esc_html( $def['ajuda'] ) . '</span></p>';
	}

	/* AS DUAS ESCOLHAS QUE LIGAM A PEÇA AO SITE (malha automática). São campos de
	   escolha, nunca texto livre: é por eles que a peça entra na coleção e na
	   técnica, e texto livre criaria "Vaso" e "vasos" como duas coisas. */
	foreach ( array( 'colecao' => 'Onde ela se encaixa', 'tecnica' => 'Técnica que você usou' ) as $tax => $rotulo ) {
		$atual = $id > 0 ? cdm_loja_termo_da_peca( $id, $tax ) : null;
		$h    .= '<p class="cdm-at-campo"><label for="cdm-' . esc_attr( $tax ) . '">' . esc_html( $rotulo ) . '</label>';
		$h    .= '<select id="cdm-' . esc_attr( $tax ) . '" name="cdm_' . esc_attr( $tax ) . '">';
		$h    .= '<option value="">Escolha</option>';
		foreach ( cdm_loja_termos_iniciais()[ $tax ] as $slug => $nome ) {
			$sel = ( $atual && $atual->slug === $slug ) ? ' selected' : '';
			$h  .= '<option value="' . esc_attr( $slug ) . '"' . $sel . '>' . esc_html( $nome ) . '</option>';
		}
		$h .= '</select>';
		$h .= '<span class="cdm-at-ajuda">Precisa escolher para a peça poder ir ao site.</span></p>';
	}

	$h .= '<div class="cdm-at-acao cdm-at-acao-dupla">';
	$h .= '<button class="cdm-at-botao-fraco" type="submit" name="cdm_destino" value="rascunho">Salvar e terminar depois</button>';
	$h .= '<button class="cdm-botao cdm-at-botao" type="submit" name="cdm_destino" value="publicar">Publicar no site</button>';
	$h .= '</div>';
	$h .= '<p class="cdm-at-ajuda">Se faltar alguma coisa para publicar, a gente guarda como rascunho e diz o que falta.</p>';
	$h .= '</form></div>';

	return $h;
}
}

add_shortcode( 'cdm_atelie', function () {
	/* A TELA DE CRIAR SENHA vem antes de tudo: ela é o primeiro contato dela com
	   este site, e nesse momento ela ainda não está logada. */
	$chave = cdm_atelie_get( 'criar-senha' );
	if ( '' !== $chave ) {
		return cdm_atelie_tela_criar_senha( $chave, cdm_atelie_get( 'quem' ) );
	}

	if ( ! is_user_logged_in() ) {
		return cdm_atelie_tela_entrar();
	}

	$usuaria = wp_get_current_user();
	if ( ! current_user_can( 'edit_pecas' ) ) {
		/* Alguém logado que não é a artesã nem administrador. Não é erro dela e
		   não é tela de erro: é uma frase e a saída. */
		$h  = '<div class="cdm-at"><h2 class="cdm-at-h2">Esta área é do ateliê</h2>';
		$h .= '<p class="cdm-at-linha">Sua conta não tem cadastro de peças. Se você é a artesã, saia e entre com o seu acesso.</p>';
		$h .= '<p class="cdm-at-acao"><a class="cdm-at-botao-fraco" href="' . esc_url( cdm_atelie_url( array(
			'cdm_acao'  => 'sair',
			'cdm_nonce' => wp_create_nonce( 'cdm_atelie_sair' ),
		) ) ) . '">Sair</a></p></div>';

		return $h;
	}

	$estado = cdm_atelie_get( 'estado' );
	if ( 'nova' === $estado ) {
		return cdm_atelie_tela_form( null );
	}
	if ( 'editar' === $estado ) {
		$peca = cdm_atelie_minha_peca( (int) cdm_atelie_get( 'peca', '0' ) );
		if ( $peca ) {
			return cdm_atelie_tela_form( $peca );
		}
	}

	return cdm_atelie_tela_lista( $usuaria );
} );

/* ---------------------------------------------------------------------------
 * 7. A FOLHA E O ÚNICO SCRIPT — no `wp_footer` (seção 8)
 *
 * O script faz DUAS coisas e nenhuma é necessária: mostra as fotos escolhidas
 * antes de enviar, e pede confirmação antes de apagar. Com o JavaScript
 * desligado o painel funciona inteiro — o que se perde é a prévia e a pergunta
 * "tem certeza?", e a peça apagada vai para a lixeira de qualquer jeito.
 *
 * Sem um "&" duplo em lugar nenhum, porque o retorno do shortcode passa pelos
 * filtros do conteúdo — mas isto aqui não passa, porque está no rodapé. As duas
 * metades da mesma cicatriz de 08/09/2026.
 * ------------------------------------------------------------------------- */

add_action( 'wp_footer', function () {
	if ( ! cdm_atelie_e_minha_pagina() ) {
		return;
	}
	$css = <<<'CSS'
.cdm-at{max-width:36rem;}
.cdm-at-cabeca{display:flex;align-items:baseline;justify-content:space-between;gap:1rem;flex-wrap:wrap;}
.cdm-at-h2{margin:0 0 .3rem;font-size:1.6rem;font-weight:600;}
.cdm-at-h3{margin:0 0 .2rem;font-size:1.1rem;}
.cdm-at-linha{margin:0 0 1.4rem;color:var(--cdm-legenda);font-size:1rem;}
.cdm-at-sair{margin:0;font-size:.95rem;}
.cdm-at-aviso{margin:0 0 1.2rem;padding:.9rem 1rem;border-radius:8px;font-size:1rem;line-height:1.5;}
.cdm-at-aviso-bom{background:#F3F8F3;border:1px solid #CBE3CB;color:#1F1715;}
.cdm-at-aviso-atencao{background:#FDF6EA;border:1px solid #E8D2A8;color:#1F1715;}
.cdm-at-faltas{margin:0 0 1.2rem;padding:.9rem 1rem .9rem 2.1rem;border:1px solid var(--cdm-coral);border-radius:8px;color:var(--cdm-tinta);font-size:1rem;}
.cdm-at-faltas li{margin:0 0 .3rem;}
.cdm-at-faltas li:last-child{margin-bottom:0;}
/* O FORMULARIO E DE CELULAR PRIMEIRO. 16px no campo e a razao nao e estetica:
   abaixo disso o iOS da zoom sozinho ao focar, a pagina pula e ela perde o
   lugar onde estava digitando. Alvo de toque de 48px de altura minima. */
.cdm-at-form{margin:0 0 1.6rem;}
.cdm-at-campo{display:block;margin:0 0 1.3rem;}
.cdm-at-campo label{display:block;margin:0 0 .35rem;font-family:var(--cdm-display);font-weight:600;font-size:1.05rem;}
.cdm-at-campo input[type=text],.cdm-at-campo input[type=email],.cdm-at-campo input[type=password],.cdm-at-campo select,.cdm-at-campo textarea{display:block;width:100%;box-sizing:border-box;min-height:3rem;padding:.7rem .8rem;font-family:var(--cdm-texto);font-size:16px;line-height:1.4;color:var(--cdm-tinta);background:var(--cdm-papel);border:1px solid var(--cdm-traco);border-radius:8px;}
.cdm-at-campo textarea{min-height:7rem;resize:vertical;}
.cdm-at-campo input[type=file]{display:block;width:100%;box-sizing:border-box;font-size:16px;padding:.8rem;border:1px dashed var(--cdm-traco);border-radius:8px;background:var(--cdm-papel);}
.cdm-at-campo input:focus,.cdm-at-campo select:focus,.cdm-at-campo textarea:focus{outline:2px solid var(--cdm-coral);outline-offset:1px;border-color:var(--cdm-coral);}
.cdm-at-ajuda{display:block;margin:.3rem 0 0;color:var(--cdm-legenda);font-size:.9rem;line-height:1.45;}
.cdm-at-acao{margin:1.6rem 0 0;}
.cdm-at-acao-grande{margin:0 0 1.6rem;}
.cdm-at-botao{min-height:3.25rem;padding:.85rem 1.4rem;font-size:1.05rem;border-radius:8px;display:inline-flex;align-items:center;justify-content:center;}
.cdm-at-botao-fraco{display:inline-flex;align-items:center;justify-content:center;min-height:3rem;padding:.7rem 1.1rem;font-family:var(--cdm-texto);font-size:1rem;font-weight:600;color:var(--cdm-rubi);background:var(--cdm-papel);border:1px solid var(--cdm-traco);border-radius:8px;text-decoration:none;cursor:pointer;}
.cdm-at-botao-fraco:hover{border-color:var(--cdm-coral);color:var(--cdm-coral);}
.cdm-at-acao-dupla{display:flex;flex-direction:column;gap:.7rem;margin:1.8rem 0 .4rem;}
.cdm-at-detalhe{margin:1.6rem 0 0;border-top:1px solid var(--cdm-traco);padding-top:1rem;}
.cdm-at-detalhe summary{cursor:pointer;font-weight:600;font-size:1rem;padding:.4rem 0;}
/* A LISTA DAS PECAS. Cartao alto com a foto a esquerda: e o que cabe num
   telefone em pe sem ela ter de rolar de lado. */
.cdm-at-lista{list-style:none;margin:0;padding:0;}
.cdm-at-item{display:flex;gap:.9rem;align-items:flex-start;margin:0 0 1rem;padding:.9rem;border:1px solid var(--cdm-traco);border-radius:14px;}
.cdm-at-mini{display:block;width:72px;height:72px;flex:0 0 72px;object-fit:cover;border-radius:8px;background:var(--cdm-traco);}
.cdm-at-mini-vazia{border:1px dashed var(--cdm-traco);background:transparent;}
.cdm-at-item-texto{flex:1 1 auto;min-width:0;}
.cdm-at-item-texto h3{margin:0 0 .3rem;font-size:1.1rem;}
.cdm-at-item-texto p{margin:0 0 .5rem;font-size:.95rem;}
.cdm-at-etiqueta{display:inline-block;font-family:var(--cdm-mono);font-size:.7rem;letter-spacing:.06em;text-transform:uppercase;padding:.15rem .45rem;border-radius:4px;border:1px solid;}
.cdm-at-etiqueta-no-ar{color:#2C6B3F;border-color:#CBE3CB;background:#F3F8F3;}
.cdm-at-etiqueta-fora{color:var(--cdm-legenda);border-color:var(--cdm-traco);}
.cdm-at-falta{color:var(--cdm-coral);font-size:.9rem;}
.cdm-at-item-acoes{display:flex;gap:1rem;flex-wrap:wrap;}
.cdm-at-mini-form{display:flex;gap:.5rem;flex-wrap:wrap;margin:.6rem 0 0;}
/* AS FOTOS JA SALVAS, com mover e remover. */
.cdm-at-fotos{list-style:none;display:flex;flex-wrap:wrap;gap:.7rem;margin:.6rem 0 1.4rem;padding:0;}
.cdm-at-foto{position:relative;margin:0;}
.cdm-at-foto img{display:block;width:110px;height:110px;object-fit:cover;border-radius:8px;background:var(--cdm-traco);}
.cdm-at-capa{position:absolute;top:.3rem;left:.3rem;background:var(--cdm-coral);color:var(--cdm-papel);font-family:var(--cdm-mono);font-size:.62rem;letter-spacing:.06em;text-transform:uppercase;padding:.1rem .35rem;border-radius:3px;}
.cdm-at-foto form{display:flex;gap:.25rem;margin:.35rem 0 0;}
.cdm-at-fbotao{display:inline-flex;align-items:center;justify-content:center;min-width:2.4rem;min-height:2.4rem;font-size:.95rem;color:var(--cdm-tinta);background:var(--cdm-papel);border:1px solid var(--cdm-traco);border-radius:6px;cursor:pointer;}
.cdm-at-fbotao:hover{border-color:var(--cdm-coral);color:var(--cdm-coral);}
.cdm-at-so-leitor{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;}
.cdm-at-previa{display:flex;flex-wrap:wrap;gap:.6rem;margin:-.6rem 0 1.3rem;}
.cdm-at-previa img{display:block;width:88px;height:88px;object-fit:cover;border-radius:8px;background:var(--cdm-traco);}
@media (min-width:34rem){
.cdm-at-acao-dupla{flex-direction:row-reverse;justify-content:flex-end;}
}
CSS;
	echo '<style id="cdm-atelie-css">' . $css . '</style>' . "\n";

	$js = <<<'JS'
(function(){
  var campo = document.getElementById('cdm-fotos');
  var previa = document.getElementById('cdm-at-previa');
  if (campo && previa && window.FileReader) {
    campo.addEventListener('change', function(){
      previa.innerHTML = '';
      var lista = campo.files || [];
      if (!lista.length) { previa.hidden = true; return; }
      previa.hidden = false;
      for (var i = 0; i < lista.length; i++) {
        (function(arquivo){
          if (!/^image\//.test(arquivo.type)) { return; }
          var leitor = new FileReader();
          leitor.onload = function(e){
            var img = document.createElement('img');
            img.src = e.target.result;
            img.alt = '';
            previa.appendChild(img);
          };
          leitor.readAsDataURL(arquivo);
        })(lista[i]);
      }
    });
  }
  var apagar = document.querySelectorAll('[data-cdm-confirmar]');
  for (var j = 0; j < apagar.length; j++) {
    apagar[j].addEventListener('click', function(ev){
      if (!window.confirm(this.getAttribute('data-cdm-confirmar'))) {
        ev.preventDefault();
      }
    });
  }
})();
JS;
	echo '<script id="cdm-atelie-js">' . $js . '</script>' . "\n";
}, 22 );

/* ---------------------------------------------------------------------------
 * 8. A ROTA DE CONFERÊNCIA — como a Fundação prova, da nuvem, que o acesso saiu
 *
 * O despacho manda escrever no `ESTADO.md` "a hora exata do envio". A única forma
 * honesta de saber essa hora sem entrar no site é o site dizer. Esta rota devolve
 * o relato que o `init` gravou: se a usuária foi criada, se o `wp_mail` aceitou, a
 * hora em UTC e o erro quando houve.
 *
 * NADA DE SEGREDO SAI DAQUI: nem senha, nem chave de redefinição, nem o e-mail
 * completo — o endereço sai mascarado, porque "o e-mail saiu" é o que se precisa
 * conferir e o endereço inteiro num log de rotina é dado de pessoa à solta. E
 * mesmo assim a rota é protegida pelo token do Sync, porque o estado do acesso de
 * alguém não é informação pública.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_atelie_email_mascarado' ) ) {
function cdm_atelie_email_mascarado( $email ) {
	$partes = explode( '@', (string) $email );
	if ( 2 !== count( $partes ) || '' === $partes[0] ) {
		return '***';
	}
	$nome = $partes[0];
	$vis  = mb_substr( $nome, 0, 2, 'UTF-8' );

	return $vis . str_repeat( '*', max( 1, mb_strlen( $nome, 'UTF-8' ) - 2 ) ) . '@' . $partes[1];
}
}

add_action( 'rest_api_init', function () {
	if ( ! function_exists( 'register_rest_route' ) ) {
		return;
	}
	register_rest_route( 'clubedomosaico/v1', '/atelie', array(
		'methods'             => 'GET',
		'permission_callback' => function ( $pedido ) {
			if ( ! function_exists( 'cdm_loja_token_esperado' ) ) {
				return false;
			}
			$esperado = cdm_loja_token_esperado();
			$vindo    = (string) $pedido->get_param( 'token' );

			return '' !== $esperado && '' !== $vindo && hash_equals( $esperado, $vindo );
		},
		'callback'            => function () {
			$acesso  = get_option( 'cdm_atelie_acesso' );
			$usuaria = cdm_atelie_usuaria();
			$papel   = function_exists( 'get_role' ) ? get_role( CDM_ATELIE_PAPEL ) : null;

			return array(
				'versao_atelie'  => CDM_ATELIE_VERSAO,
				'painel'         => cdm_atelie_url(),
				'papel_existe'   => (bool) $papel,
				'capacidades'    => $papel ? array_keys( array_filter( (array) $papel->capabilities ) ) : array(),
				'usuaria_existe' => (bool) $usuaria,
				'usuaria_papeis' => $usuaria ? array_values( (array) $usuaria->roles ) : array(),
				'email'          => cdm_atelie_email_mascarado( CDM_ATELIE_EMAIL ),
				'acesso'         => is_array( $acesso ) ? array(
					'criada'     => ! empty( $acesso['criada'] ),
					'enviado'    => ! empty( $acesso['enviado'] ),
					'quando'     => isset( $acesso['quando'] ) ? $acesso['quando'] : '',
					'erro'       => isset( $acesso['erro'] ) ? $acesso['erro'] : '',
					'tentativas' => isset( $acesso['tentativas'] ) ? (int) $acesso['tentativas'] : 0,
				) : null,
			);
		},
	) );
} );
