/**
 * Clube do Mosaico Leads — verificar disponibilidade
 * Versão 1.1.0 (13/09/2026) — AS DUAS OPTIONS DESTE ARQUIVO VIRARAM CAMPO DELA.
 * `cdm_email_leads` (para onde vai o aviso de interessado) e `cdm_artesa_nome`
 * (o nome que assina a mensagem no WhatsApp) existiam e funcionavam, e só a
 * Fundação podia mexer nelas. Agora as duas são uma seção da aba "Meus dados"
 * do painel, entregue pelo filtro `cdm_atelie_meus_dados` que o Ateliê 1.2.0
 * abriu. Nada mais mudou: o formulário da peça, o CPT, o e-mail, a aba
 * Interessados e o CSV continuam como estavam.
 *
 * POR QUE OS CAMPOS NASCEM AQUI E NÃO NO ATELIÊ, que é o dono da tela: quem lê
 * a option é quem a escreve. As duas são lidas SÓ por este arquivo, e um campo
 * desenhado no Ateliê gravando uma option que só faz sentido aqui é a promessa
 * de uma tela que o Sync pode desembarcar sem o lado que lhe dá efeito — a
 * mesma razão pela qual a aba "Interessados" também mora aqui.
 *
 * E O VAZIO CONTINUA SIGNIFICANDO O QUE SIGNIFICAVA: e-mail em branco é "avise
 * no endereço da conta"; nome em branco é "a identidade da artesã ainda não
 * chegou", e a mensagem assina "do Clube do Mosaico". Os dois campos DIZEM na
 * tela o que o vazio faz, em vez de deixar ela adivinhar por que o campo está
 * em branco.
 *
 * Versão 1.0.0 (13/09/2026) — o ADENDO 3 de 11/09/2026, que ficou FORA do corte
 * do despacho de 12/09 por escrito, e volta à fila agora que o painel está de pé.
 *
 * O que ele entrega, e é o adendo inteiro: o botão "Verificar disponibilidade" na
 * ficha da peça, o formulário curto de nome e WhatsApp, o CPT `lead_peca`, o
 * e-mail imediato para a artesã com o botão de responder no WhatsApp, a aba
 * "Interessados" dentro de `/atelie/` e a exportação em CSV.
 *
 * ------------------------------------------------------------------------
 * AS SETE DECISÕES, e a cicatriz que cada uma evita
 * ------------------------------------------------------------------------
 *
 * 1. TERCEIRO SNIPPET, E NÃO UM PEDAÇO DA LOJA.
 *    O adendo já preferia assim e a razão é a mesma da separação Loja/Ateliê: o
 *    Sync desembarca um sem o outro. Se o formulário tiver defeito, a ficha da
 *    peça continua no ar; se a Loja mudar, ninguém perde os interessados que já
 *    chegaram. E há uma razão nova, que só apareceu agora: este é o primeiro
 *    snippet desta ilha que guarda DADO DE PESSOA. Mantê-lo num arquivo só faz
 *    a pergunta "onde moram nome e telefone de quem escreveu para o ateliê?"
 *    ter uma resposta de uma linha.
 *
 * 2. A LOJA APLICA UM FILTRO, E ELE É APLICADO DE VERDADE.
 *    `cdm_loja_ficha_html()` passou a servir o bloco de ação por
 *    `apply_filters( 'cdm_peca_acao', $padrao, $peca, $dados )`, e é aqui que o
 *    filtro é atendido. A cicatriz é de 12/09/2026, nesta mesma ilha: duas
 *    linhas de `add_filter` que eu mesma escrevi e que NINGUÉM aplicava —
 *    "portão que nunca roda é função morta". Por isso o `teste-loja.php` cobra
 *    que a Loja CHAME o filtro, e o `teste-leads.php` cobra que o retorno com o
 *    filtro atendido seja diferente do padrão. As duas metades, medidas dos dois
 *    lados.
 *    E o padrão da Loja continua sendo o de hoje: se este snippet não
 *    desembarcar, a ficha volta a dizer que o contato ainda não foi publicado,
 *    em vez de quebrar.
 *
 * 3. O FORMULÁRIO FUNCIONA COM O JAVASCRIPT DESLIGADO (seção 22.8).
 *    É um `<details>` do próprio HTML com um `<form method="post">` dentro.
 *    Nenhuma linha de script participa de abrir, validar ou enviar: o que o
 *    script faz é a máscara do telefone enquanto se digita, e a máscara é
 *    enfeite — a canonização de verdade acontece no PHP, depois do envio. Quem
 *    entra pelo modo leitor, por um robô ou com o JavaScript desligado manda o
 *    lead igual.
 *
 * 4. O NOME DA PESSOA NÃO VIAJA NA URL.
 *    O adendo pede "Pronto, {nome}!" depois de enviar, e o caminho preguiçoso
 *    seria redirecionar para `?cdm_lead=ok&nome=Maria`. Isso põe o nome de uma
 *    cliente no histórico do navegador, no Referer da próxima requisição e no
 *    log de acesso do servidor — três lugares onde ele não tem nada que fazer, e
 *    ainda deixaria qualquer pessoa fabricar a tela de "enviado" digitando a
 *    URL. Em vez disso, o POST guarda a confirmação num transient de 10 minutos
 *    e redireciona com uma CHAVE aleatória. Quem não enviou nada não tem chave,
 *    e a chave não diz nada sobre quem enviou.
 *
 * 5. O `noindex` DO ESTADO COM PARÂMETRO, pela mesma razão da F2.
 *    A ficha da peça com `?cdm_lead=...` é uma URL de verdade servida pelo
 *    servidor. Quem entra no índice é UMA página — a ficha limpa. O canonical
 *    continua sendo o do núcleo, que já imprime o permalink.
 *
 * 6. O LEAD NÃO VAI PARA O REPOSITÓRIO, E A CÓPIA DA SEÇÃO 24 É O CSV.
 *    A seção 24 manda todo bloco que cria tela de digitar dado entregar a
 *    exportação daquele dado no mesmo bloco. Para a PEÇA a cópia é o endpoint
 *    `/wp-json/clubedomosaico/v1/pecas`, protegido pelo token do Sync, que a
 *    ronda commita. Para o LEAD não é, e o adendo já dizia por quê: nome e
 *    WhatsApp de pessoa não entram em arquivo versionado. A cópia dele é o
 *    botão "Baixar em CSV" dentro do painel, na mão da artesã. Por isso NÃO
 *    existe rota REST de lead neste arquivo — e o teste cobra a ausência, que é
 *    a única forma de uma ausência não sumir sozinha num bloco futuro.
 *
 * 7. A ABA NÃO CRIA CAPACIDADE NOVA.
 *    A tentação era um `ler_interessados` no papel `artesa`. Duas razões contra:
 *    o `conferir-atelie-no-ar.py` mede que o papel tem EXATAMENTE as sete
 *    capacidades do bloco anterior e nenhuma das oito proibidas — uma oitava
 *    faria aquele portão reprovar sem defeito nenhum embaixo —, e a régua certa
 *    já existe: quem pode editar as peças pode ver quem perguntou por elas. A
 *    aba é gated por `edit_pecas`, a mesma do painel.
 *
 * ------------------------------------------------------------------------
 * O QUE ESTE ARQUIVO LÊ DE FORA, E O QUE ACONTECE SE FALTAR
 * ------------------------------------------------------------------------
 * Ele depende do snippet da Loja (`cdm_loja_meta`, `cdm_loja_galeria`,
 * `cdm_loja_disponibilidade_frase`, `cdm_loja_preco_html`) e do Ateliê
 * (`cdm_atelie_url`, `cdm_atelie_get`, `cdm_atelie_post`). Os dois já estão no
 * ar desde 12/09. Como o Sync desembarca um item por vez, cada uso é guardado
 * por `function_exists`: faltando a Loja, o formulário não é servido e a ficha
 * fica com o texto padrão dela; faltando o Ateliê, a aba não aparece e o lead
 * continua sendo gravado e enviado por e-mail. Nada quebra pela metade.
 *
 * ------------------------------------------------------------------------
 * O QUE VIGIAR NO DIA EM QUE ESTA ILHA GANHAR CACHE DE PÁGINA
 * ------------------------------------------------------------------------
 * O nonce do formulário é gerado quando a página é montada. Se um dia alguém
 * ligar cache de HTML nesta hospedagem, a ficha da peça passa a ser servida do
 * cache com um nonce cada vez mais velho, e o envio começa a cair em "a página
 * ficou aberta tempo demais". O nonce do WordPress vive de 12 a 24 horas e
 * cache de página costuma ser bem mais curto, então hoje isso não acontece — e
 * hoje esta ilha não tem plugin de cache (Code Snippets, Site Kit, Converter
 * for Media e Limit Login Attempts, medido em 11/09/2026). Fica escrito porque
 * o sintoma é enganoso: parece defeito do formulário e é do cache, e a única
 * pessoa que veria seria uma cliente que desistiu sem avisar ninguém.
 *
 * ------------------------------------------------------------------------
 * SOBRE `$_SERVER`, QUE APARECE UMA VEZ SÓ NESTE ARQUIVO
 * ------------------------------------------------------------------------
 * O playbook (fase 4b) manda evitar `$_SERVER` literal porque o ModSecurity da
 * hospedagem mata em silêncio a gravação de um snippet que o contenha — e o
 * aviso vale para quem salva o código pelo wp-admin. Aqui o endereço de quem
 * enviou é a ÚNICA fonte possível do limite de 5 por hora que o adendo pede, e
 * o núcleo do WordPress não oferece embrulho nenhum para ele. Então ele é lido
 * uma vez, dentro de `cdm_leads_ip_hash()`, e nunca guardado em texto: o que
 * vai para o transient é `wp_hash()` dele. E fica escrito aqui, para a próxima
 * pessoa: **este arquivo desembarca pelo Sync, que grava por PHP e não por
 * formulário do wp-admin.** Se um dia alguém colar este código no editor do
 * Code Snippets e o Salvar não fizer nada, é isto.
 */

if ( ! defined( 'CDM_LEADS_VERSAO' ) ) {
	define( 'CDM_LEADS_VERSAO', '1.1.0' );
}
if ( ! defined( 'CDM_LEADS_TIPO' ) ) {
	define( 'CDM_LEADS_TIPO', 'lead_peca' );
}
/* O limite do adendo: 5 envios por hora, por endereço. */
if ( ! defined( 'CDM_LEADS_TETO' ) ) {
	define( 'CDM_LEADS_TETO', 5 );
}
if ( ! defined( 'CDM_LEADS_JANELA' ) ) {
	define( 'CDM_LEADS_JANELA', 3600 );
}
/* Quanto tempo a tela de "enviado" continua de pé se ela atualizar a página. */
if ( ! defined( 'CDM_LEADS_CONFIRMA_VIDA' ) ) {
	define( 'CDM_LEADS_CONFIRMA_VIDA', 600 );
}
/* O e-mail de destino nasce no da artesã, e a option existe para "Meus dados"
   (que é de um bloco futuro) poder trocá-lo sem tocar em código. */
if ( ! defined( 'CDM_LEADS_EMAIL_PADRAO' ) ) {
	define( 'CDM_LEADS_EMAIL_PADRAO', 'mina196@hotmail.com' );
}

/* ---------------------------------------------------------------------------
 * 1. O TIPO — invisível por todos os lados
 *
 * `public` false já implicaria o resto; os outros quatro estão escritos assim
 * mesmo porque cada um é uma porta diferente, e depender da implicação de um
 * argumento é como o painel quase foi ao índice em 12/09.
 * ------------------------------------------------------------------------- */

add_action( 'init', function () {
	if ( ! function_exists( 'register_post_type' ) ) {
		return;
	}
	register_post_type( CDM_LEADS_TIPO, array(
		'labels'              => array(
			'name'          => 'Interessados',
			'singular_name' => 'Interessado',
		),
		'public'              => false,
		'publicly_queryable'  => false,
		'show_ui'             => false,
		'show_in_menu'        => false,
		'show_in_rest'        => false,
		'show_in_nav_menus'   => false,
		'exclude_from_search' => true,
		'has_archive'         => false,
		'rewrite'             => false,
		'query_var'           => false,
		'supports'            => array( 'title' ),
		'capability_type'     => 'peca',
		'map_meta_cap'        => true,
	) );
}, 6 );

/* ---------------------------------------------------------------------------
 * 2. O TELEFONE — uma régua só, e ela é a da Real 21
 *
 * O adendo manda guardar normalizado com DDI 55 "mesma regra de canonização
 * usada na Real 21: `r21_wa_canonico`, para não duplicar lead por formato". A
 * régua está reescrita aqui porque o código de lá não existe nesta ilha, e
 * copiar comportamento é diferente de copiar arquivo.
 *
 * O que ela decide, e por que cada borda importa:
 *   - só dígitos, então "(11) 98765-4321" e "11987654321" viram o mesmo lead;
 *   - DDI 55 é acrescentado quando não veio, e NUNCA duplicado — "5511..." com
 *     55 na frente de novo viraria um número de 15 dígitos que não existe;
 *   - o zero do DDD antigo ("011") cai, porque ele não entra em número
 *     internacional;
 *   - DDD brasileiro vai de 11 a 99, e nenhum começa com 0 ou 1 no segundo
 *     dígito além dos que existem — a régua aqui é a faixa, não a lista, porque
 *     lista de DDD envelhece e faixa não;
 *   - o assinante tem 8 ou 9 dígitos, e o de 9 começa com 9. Um celular de 8
 *     dígitos ainda existe em telefone fixo, e o adendo pede WhatsApp — mas
 *     recusar 8 dígitos aqui recusaria o número de alguém que digitou certo num
 *     DDD onde o WhatsApp fixo funciona. Os dois passam; quem decide se atende é
 *     a artesã, não este arquivo.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_leads_wa_canonico' ) ) {
function cdm_leads_wa_canonico( $bruto ) {
	$so = preg_replace( '/\D+/', '', (string) $bruto );
	if ( '' === $so ) {
		return '';
	}

	/* Já veio com DDI: tira para tratar o miolo uma vez só. */
	if ( 13 === strlen( $so ) && '55' === substr( $so, 0, 2 ) ) {
		$so = substr( $so, 2 );
	} elseif ( 12 === strlen( $so ) && '55' === substr( $so, 0, 2 ) ) {
		$so = substr( $so, 2 );
	}

	/* O zero de operadora na frente do DDD. */
	if ( strlen( $so ) > 10 && '0' === substr( $so, 0, 1 ) ) {
		$so = substr( $so, 1 );
	}

	if ( 10 !== strlen( $so ) && 11 !== strlen( $so ) ) {
		return '';
	}

	$ddd = (int) substr( $so, 0, 2 );
	if ( $ddd < 11 || $ddd > 99 ) {
		return '';
	}

	$assinante = substr( $so, 2 );
	if ( 9 === strlen( $assinante ) && '9' !== substr( $assinante, 0, 1 ) ) {
		return '';
	}
	/* Número de um dígito só repetido é o que se digita para testar formulário. */
	if ( preg_match( '/^(\d)\1+$/', $assinante ) ) {
		return '';
	}

	return '55' . $so;
}
}

if ( ! function_exists( 'cdm_leads_wa_legivel' ) ) {
/**
 * O canônico de volta em (DD) 9NNNN-NNNN, para a artesã LER na tela e no e-mail.
 *
 * O que se guarda é o canônico; o que se mostra é isto. São coisas diferentes e
 * a diferença é o motivo de existirem duas funções: se a tela guardasse o que
 * mostra, um lead digitado com parêntese e outro sem seriam duas pessoas.
 */
function cdm_leads_wa_legivel( $canonico ) {
	$so = preg_replace( '/\D+/', '', (string) $canonico );
	if ( 12 !== strlen( $so ) && 13 !== strlen( $so ) ) {
		return (string) $canonico;
	}
	$ddd       = substr( $so, 2, 2 );
	$assinante = substr( $so, 4 );
	$corte     = ( 9 === strlen( $assinante ) ) ? 5 : 4;

	return '(' . $ddd . ') ' . substr( $assinante, 0, $corte ) . '-' . substr( $assinante, $corte );
}
}

if ( ! function_exists( 'cdm_leads_primeiro_nome' ) ) {
/** O primeiro nome, para a mensagem pronta. Nome de uma palavra devolve ele mesmo. */
function cdm_leads_primeiro_nome( $nome ) {
	$partes = preg_split( '/\s+/', trim( (string) $nome ) );

	return ( $partes && '' !== $partes[0] ) ? $partes[0] : '';
}
}

/* ---------------------------------------------------------------------------
 * 3. O CONSENTIMENTO — o texto exato, num lugar só
 *
 * Ele é mostrado na tela E guardado no lead junto do carimbo de hora, porque é
 * isso que a LGPD pede: não basta ter havido consentimento, tem de dar para
 * dizer A QUE a pessoa consentiu naquele dia. Se este texto mudar num bloco
 * futuro, os leads antigos continuam guardando o texto antigo — que é o certo, e
 * é por isso que ele é gravado e não apenas referenciado.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_leads_texto_consentimento' ) ) {
function cdm_leads_texto_consentimento() {
	return 'Ao enviar, você autoriza o Clube do Mosaico a entrar em contato pelo WhatsApp sobre esta peça. '
		. 'Seus dados são usados só para esse atendimento e não são repassados a terceiros.';
}
}

if ( ! function_exists( 'cdm_leads_link_privacidade' ) ) {
/**
 * O link para /privacidade/, pelo helper da casca.
 *
 * `cdm_casca_link_html()` só devolve `<a>` se a página EXISTIR publicada — sem
 * ela sai o rótulo sozinho, nunca um endereço que devolve 404. É a régua desta
 * ilha desde a casca 1.0.0 e não há razão para o consentimento ter outra: o
 * texto do consentimento continua inteiro mesmo que a página suma, e é ele que
 * a LGPD pede, não o link.
 */
function cdm_leads_link_privacidade() {
	if ( function_exists( 'cdm_casca_link_html' ) ) {
		return cdm_casca_link_html( 'privacidade', 'Política de privacidade' );
	}

	return '<a href="' . esc_url( home_url( '/privacidade/' ) ) . '">Política de privacidade</a>';
}
}

/* ---------------------------------------------------------------------------
 * 4. O FORMULÁRIO NA FICHA DA PEÇA
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_leads_avisos' ) ) {
/** Os avisos, um lugar só, porque a tela e o teste leem a mesma lista. */
function cdm_leads_avisos() {
	return array(
		'nome'   => 'Faltou o seu nome. É só o primeiro, se preferir.',
		'zap'    => 'Esse número não parece um WhatsApp com DDD. Escreva com o DDD, assim: (11) 98765-4321.',
		'ok'     => 'Falta marcar a autorização de contato, logo acima do botão.',
		'nonce'  => 'A página ficou aberta tempo demais e o envio expirou. Tente de novo.',
		'limite' => 'Já chegaram vários pedidos deste aparelho na última hora. Espere um pouco e tente de novo.',
		'peca'   => 'Não deu para saber de qual peça era o pedido. Volte à peça e tente de novo.',
	);
}
}

if ( ! function_exists( 'cdm_leads_confirmacao' ) ) {
/**
 * A confirmação guardada pelo POST, se a chave da URL for de verdade.
 *
 * Devolve array com nome e id da peça, ou null. Confere que a confirmação é
 * DESTA peça: uma chave válida colada na ficha de outra peça não vira tela de
 * enviado ali.
 */
function cdm_leads_confirmacao( $peca_id ) {
	if ( ! function_exists( 'get_transient' ) || ! function_exists( 'cdm_atelie_get' ) ) {
		return null;
	}
	$chave = cdm_atelie_get( 'cdm_lead' );
	if ( '' === $chave || ! preg_match( '/^[A-Za-z0-9]{12,40}$/', $chave ) ) {
		return null;
	}
	$guardado = get_transient( 'cdm_lead_ok_' . $chave );
	if ( ! is_array( $guardado ) || empty( $guardado['nome'] ) ) {
		return null;
	}
	if ( (int) $peca_id !== (int) ( $guardado['peca'] ?? 0 ) ) {
		return null;
	}

	return $guardado;
}
}

if ( ! function_exists( 'cdm_leads_form_html' ) ) {
/**
 * O bloco de ação inteiro da ficha: confirmação, ou botão + formulário.
 *
 * `$dados` vem da Loja com o que ela já calculou (título, URL, disponibilidade e
 * prazo). Nada é recalculado aqui: dois lugares calculando o mesmo campo é como
 * a bancada e o site passaram a divergir na Aquametria em 11/09.
 */
function cdm_leads_form_html( $peca, $dados = array() ) {
	$id     = (int) $peca->ID;
	$titulo = isset( $dados['titulo'] ) ? (string) $dados['titulo'] : (string) $peca->post_title;
	$url    = isset( $dados['url'] ) ? (string) $dados['url'] : get_permalink( $peca );

	/* --- ENVIADO --- */
	$ok = cdm_leads_confirmacao( $id );
	if ( $ok ) {
		$h  = '<div class="cdm-lead-pronto" id="cdm-quero">';
		$h .= '<h3>Pronto, ' . esc_html( cdm_leads_primeiro_nome( $ok['nome'] ) ) . '!</h3>';
		$h .= '<p>A artesã vai te chamar no WhatsApp para confirmar disponibilidade e prazo da peça ';
		$h .= '<strong>' . esc_html( $titulo ) . '</strong>.</p>';
		$h .= '</div>';

		return $h;
	}

	$avisos = cdm_leads_avisos();
	$aviso  = function_exists( 'cdm_atelie_get' ) ? cdm_atelie_get( 'cdm_lead_erro' ) : '';
	$erro   = isset( $avisos[ $aviso ] ) ? $avisos[ $aviso ] : '';

	/* Com erro o bloco abre sozinho: mandar a pessoa clicar de novo para
	   descobrir o que faltou é o jeito mais rápido de ela desistir. */
	$aberto = ( '' !== $erro ) ? ' open' : '';

	$h  = '<div class="cdm-peca-acao" id="cdm-quero">';
	$h .= '<details class="cdm-lead"' . $aberto . '>';
	$h .= '<summary class="cdm-botao cdm-lead-abre">Verificar disponibilidade</summary>';
	$h .= '<form class="cdm-lead-form" method="post" action="' . esc_url( $url . '#cdm-quero' ) . '">';

	if ( '' !== $erro ) {
		$h .= '<p class="cdm-lead-erro" role="alert">' . esc_html( $erro ) . '</p>';
	}

	$h .= '<input type="hidden" name="cdm_acao" value="lead">';
	$h .= '<input type="hidden" name="cdm_peca" value="' . $id . '">';
	$h .= '<input type="hidden" name="cdm_nonce" value="' . esc_attr( wp_create_nonce( 'cdm_lead_' . $id ) ) . '">';

	/* A origem: a URL da peça mais a UTM, se ela veio na visita. Os campos
	   escondidos existem porque o POST vai para a ficha e a UTM está na URL de
	   QUEM CHEGOU — sem carregá-la aqui, toda campanha viraria "origem: direta". */
	$h .= '<input type="hidden" name="cdm_origem" value="' . esc_attr( cdm_leads_origem_da_visita( $url ) ) . '">';

	$h .= '<p class="cdm-lead-campo">';
	$h .= '<label for="cdm-lead-nome-' . $id . '">Seu nome</label>';
	$h .= '<input id="cdm-lead-nome-' . $id . '" name="cdm_nome" type="text" maxlength="80" autocomplete="name" required>';
	$h .= '</p>';

	$h .= '<p class="cdm-lead-campo">';
	$h .= '<label for="cdm-lead-zap-' . $id . '">Seu WhatsApp, com DDD</label>';
	$h .= '<input id="cdm-lead-zap-' . $id . '" name="cdm_zap" type="tel" inputmode="tel" maxlength="20" ';
	$h .= 'placeholder="(11) 98765-4321" autocomplete="tel" required>';
	$h .= '</p>';

	/* O HONEYPOT. Fica fora da vista por CSS e fora do caminho do teclado por
	   tabindex; quem preenche é robô, e o envio é descartado em silêncio — sem
	   mensagem de erro, que é o que ensinaria o robô a contornar. */
	$h .= '<p class="cdm-lead-hp" aria-hidden="true">';
	$h .= '<label for="cdm-lead-cep-' . $id . '">Deixe este campo em branco</label>';
	$h .= '<input id="cdm-lead-cep-' . $id . '" name="cdm_cep" type="text" tabindex="-1" autocomplete="off">';
	$h .= '</p>';

	$h .= '<p class="cdm-lead-consente">';
	$h .= '<label><input type="checkbox" name="cdm_ok" value="1" required> ';
	$h .= '<span>' . esc_html( cdm_leads_texto_consentimento() ) . ' ';
	$h .= cdm_leads_link_privacidade() . '.</span></label>';
	$h .= '</p>';

	$h .= '<p class="cdm-lead-enviar"><button class="cdm-botao" type="submit">Quero esta peça</button></p>';
	$h .= '</form></details>';
	$h .= '<p class="cdm-peca-nota">Você fala direto com quem fez. Ela confirma se a peça está disponível e como fica o envio.</p>';
	$h .= '</div>';

	return $h;
}
}

if ( ! function_exists( 'cdm_leads_origem_da_visita' ) ) {
/**
 * A URL da peça mais a UTM da visita, quando houver. Nada além disso.
 *
 * Não guarda Referer nem nada que o navegador mande sozinho: o adendo pede
 * "URL da peça + UTM se houver", e campo que ninguém pediu é dado de pessoa
 * guardado sem motivo.
 */
function cdm_leads_origem_da_visita( $url ) {
	if ( ! function_exists( 'cdm_atelie_get' ) ) {
		return (string) $url;
	}
	$utms = array();
	foreach ( array( 'utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term' ) as $chave ) {
		$v = cdm_atelie_get( $chave );
		if ( '' !== $v ) {
			$utms[] = $chave . '=' . rawurlencode( substr( $v, 0, 60 ) );
		}
	}

	return $utms ? $url . '?' . implode( '&', $utms ) : (string) $url;
}
}

/* A ficha da peça pede o bloco de ação por filtro; este é quem o atende. */
add_filter( 'cdm_peca_acao', function ( $padrao, $peca, $dados = array() ) {
	if ( ! is_object( $peca ) || ! function_exists( 'cdm_loja_meta' ) ) {
		return $padrao;
	}

	return cdm_leads_form_html( $peca, $dados );
}, 10, 3 );

/* O `noindex` do estado com parâmetro (decisão 5). Prioridade 4, a mesma que a
   F2 usa, para sair antes do JSON-LD e depois da description. */
add_action( 'wp_head', function () {
	if ( ! function_exists( 'cdm_loja_e_peca' ) || ! cdm_loja_e_peca() ) {
		return;
	}
	if ( ! function_exists( 'cdm_atelie_get' ) ) {
		return;
	}
	if ( '' !== cdm_atelie_get( 'cdm_lead' ) || '' !== cdm_atelie_get( 'cdm_lead_erro' ) ) {
		echo '<meta name="robots" content="noindex, follow">' . "\n";
	}
}, 4 );

/* ---------------------------------------------------------------------------
 * 5. O RECEBIMENTO
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_leads_ip_hash' ) ) {
/**
 * A impressão do endereço de quem enviou, para o limite por hora. Ver o
 * cabeçalho deste arquivo sobre `$_SERVER` e o ModSecurity.
 *
 * Devolve '' quando não há endereço — e quem chama trata '' como "sem limite
 * medível", nunca como "bloqueado". Recusar envio porque o servidor não contou
 * quem era seria punir a cliente por um detalhe de infraestrutura.
 */
function cdm_leads_ip_hash() {
	$ip = isset( $_SERVER['REMOTE_ADDR'] ) ? (string) $_SERVER['REMOTE_ADDR'] : '';
	$ip = trim( $ip );
	if ( '' === $ip ) {
		return '';
	}
	if ( function_exists( 'wp_hash' ) ) {
		return substr( wp_hash( 'cdm-lead|' . $ip ), 0, 32 );
	}

	return substr( hash( 'sha256', 'cdm-lead|' . $ip ), 0, 32 );
}
}

if ( ! function_exists( 'cdm_leads_limite_batido' ) ) {
/** Verdadeiro quando este endereço já mandou CDM_LEADS_TETO na última hora. */
function cdm_leads_limite_batido( $hash ) {
	if ( '' === $hash || ! function_exists( 'get_transient' ) ) {
		return false;
	}

	return (int) get_transient( 'cdm_lead_lim_' . $hash ) >= CDM_LEADS_TETO;
}
}

if ( ! function_exists( 'cdm_leads_contar_envio' ) ) {
/** Soma um no balde da hora. O transient expira sozinho; não há limpeza. */
function cdm_leads_contar_envio( $hash ) {
	if ( '' === $hash || ! function_exists( 'set_transient' ) ) {
		return;
	}
	$agora = (int) get_transient( 'cdm_lead_lim_' . $hash );
	set_transient( 'cdm_lead_lim_' . $hash, $agora + 1, CDM_LEADS_JANELA );
}
}

if ( ! function_exists( 'cdm_leads_estados' ) ) {
/** Os quatro estados do adendo, na ordem em que a vida deles acontece. */
function cdm_leads_estados() {
	return array(
		'novo'      => 'Novo',
		'contatado' => 'Já falei',
		'vendido'   => 'Vendeu',
		'perdido'   => 'Não deu',
	);
}
}

if ( ! function_exists( 'cdm_leads_gravar' ) ) {
/**
 * Grava o lead e devolve o id, ou 0.
 *
 * O TÍTULO DO POST NÃO LEVA O NOME DA PESSOA. Ele é o que apareceria em qualquer
 * lista do WordPress que um dia mostre este tipo, e a peça já identifica o
 * registro. Nome e telefone moram em meta, onde é preciso pedir por eles.
 */
function cdm_leads_gravar( $peca, $nome, $zap_canonico, $origem ) {
	$id = wp_insert_post( array(
		'post_type'   => CDM_LEADS_TIPO,
		'post_status' => 'publish',
		'post_title'  => 'Interesse: ' . (string) $peca->post_title,
	) );
	$id = (int) $id;
	if ( $id <= 0 ) {
		return 0;
	}

	update_post_meta( $id, '_cdm_nome', $nome );
	update_post_meta( $id, '_cdm_whatsapp', $zap_canonico );
	update_post_meta( $id, '_cdm_peca_id', (int) $peca->ID );
	update_post_meta( $id, '_cdm_origem', $origem );
	update_post_meta( $id, '_cdm_status', 'novo' );
	update_post_meta( $id, '_cdm_consentimento', array(
		'em'    => current_time( 'mysql' ),
		'texto' => cdm_leads_texto_consentimento(),
	) );

	return $id;
}
}

if ( ! function_exists( 'cdm_leads_agir' ) ) {
/**
 * O recebimento do formulário. Redireciona sempre; nunca imprime nada.
 *
 * A ORDEM DAS RECUSAS É DELIBERADA: nonce, honeypot, peça, consentimento, nome,
 * telefone, limite. O honeypot vem cedo e sai em silêncio; o limite vem por
 * último, depois de tudo validado, para um robô não conseguir gastar o balde de
 * uma pessoa de verdade com envios inválidos.
 */
function cdm_leads_agir() {
	if ( ! function_exists( 'cdm_atelie_post' ) || ! function_exists( 'cdm_loja_e_peca' ) ) {
		return;
	}
	if ( 'lead' !== cdm_atelie_post( 'cdm_acao' ) ) {
		return;
	}
	$peca = cdm_loja_e_peca();
	if ( ! $peca ) {
		return;
	}
	$id  = (int) $peca->ID;
	$url = get_permalink( $peca );

	$volta = function ( $motivo ) use ( $url ) {
		wp_safe_redirect( $url . ( '' === $motivo ? '' : '?cdm_lead_erro=' . $motivo ) . '#cdm-quero' );
		exit;
	};

	if ( ! wp_verify_nonce( cdm_atelie_post( 'cdm_nonce' ), 'cdm_lead_' . $id ) ) {
		$volta( 'nonce' );
	}
	/* HONEYPOT: preenchido = robô. Sai como se tivesse dado certo, sem gravar e
	   sem avisar — o silêncio é a parte que funciona. */
	if ( '' !== cdm_atelie_post( 'cdm_cep' ) ) {
		$volta( '' );
	}
	if ( (int) cdm_atelie_post( 'cdm_peca', '0' ) !== $id ) {
		$volta( 'peca' );
	}
	if ( '1' !== cdm_atelie_post( 'cdm_ok' ) ) {
		$volta( 'ok' );
	}

	$nome = sanitize_text_field( cdm_atelie_post( 'cdm_nome' ) );
	$nome = trim( preg_replace( '/\s+/', ' ', $nome ) );
	if ( '' === $nome || mb_strlen( $nome ) < 2 ) {
		$volta( 'nome' );
	}
	$nome = mb_substr( $nome, 0, 80 );

	$zap = cdm_leads_wa_canonico( cdm_atelie_post( 'cdm_zap' ) );
	if ( '' === $zap ) {
		$volta( 'zap' );
	}

	$hash = cdm_leads_ip_hash();
	if ( cdm_leads_limite_batido( $hash ) ) {
		$volta( 'limite' );
	}

	$origem = sanitize_text_field( cdm_atelie_post( 'cdm_origem' ) );
	if ( '' === $origem ) {
		$origem = $url;
	}

	$lead_id = cdm_leads_gravar( $peca, $nome, $zap, $origem );
	if ( $lead_id <= 0 ) {
		$volta( 'peca' );
	}

	cdm_leads_contar_envio( $hash );
	cdm_leads_notificar( $lead_id, $peca );

	/* A CHAVE DA CONFIRMAÇÃO (decisão 4). */
	$chave = wp_generate_password( 20, false, false );
	if ( function_exists( 'set_transient' ) ) {
		set_transient( 'cdm_lead_ok_' . $chave, array(
			'nome' => $nome,
			'peca' => $id,
		), CDM_LEADS_CONFIRMA_VIDA );
	}

	wp_safe_redirect( $url . '?cdm_lead=' . rawurlencode( $chave ) . '#cdm-quero' );
	exit;
}
}

/* Prioridade 6: DEPOIS do despachante do Ateliê (5), que já devolve cedo em
   qualquer página que não seja a dele. Duas ações no mesmo gancho não se
   atrapalham porque cada uma reconhece só o `cdm_acao` que é seu. */
add_action( 'template_redirect', 'cdm_leads_agir', 6 );

/* ---------------------------------------------------------------------------
 * 6. O E-MAIL PARA A ARTESÃ
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_leads_nome_da_artesa' ) ) {
/**
 * O nome público da artesã, ou '' enquanto ele não tiver sido ENTREGUE.
 *
 * ESTA FUNÇÃO NASCEU ERRADA E O PORTÃO A PEGOU, e a forma do erro vale mais que
 * o conserto. A primeira versão lia o `first_name` da usuária e descartava o
 * valor quando ele fosse a palavra "artesa" — uma lista de palavras proibidas,
 * exatamente a heurística por vizinhança que a seção 8 do contrato proíbe. Ela
 * falhou na primeira medição pelo motivo mais previsível: o que o snippet do
 * Ateliê grava em `first_name` é `Artesã`, com til e cedilha, e nenhuma lista de
 * palavras acerta a grafia de um texto de espera que ela não escreveu. A
 * mensagem teria saído "Aqui é Artesã" para uma cliente de verdade.
 *
 * A saída não é uma lista melhor: é parar de adivinhar. O nome público é
 * DECLARADO numa option, `cdm_artesa_nome`, que nasce vazia. Vazia significa uma
 * coisa só — a identidade da pasta `identidade/artesa/` ainda não chegou — e é
 * o mesmo estado que o `PROMPT.md` desta ilha já manda a página Sobre respeitar.
 *
 * O `first_name` continua sendo o "Olá, Artesã" do painel, que é a tela DELA e
 * onde o texto de espera não engana ninguém. Aqui, onde a frase vai para uma
 * estranha, quem decide é a declaração.
 */
function cdm_leads_nome_da_artesa() {
	$nome = trim( (string) get_option( 'cdm_artesa_nome', '' ) );

	return ( '' !== $nome ) ? $nome : '';
}
}

if ( ! function_exists( 'cdm_leads_frase_disponibilidade' ) ) {
/**
 * A disponibilidade dentro da mensagem pronta, em português de conversa.
 *
 * O adendo escreve o buraco como "{pronta entrega / sob encomenda, prazo de N
 * dias}". Aqui ele sai como alguém falaria no WhatsApp — os dados são os mesmos
 * e nenhum é inventado. Sem disponibilidade gravada a frase não sai: a mensagem
 * perde uma linha e não ganha uma mentira.
 */
function cdm_leads_frase_disponibilidade( $disp, $prazo ) {
	if ( 'pronta_entrega' === $disp ) {
		return 'Ela está pronta, já feita.';
	}
	if ( 'sob_encomenda' === $disp ) {
		$dias = (int) $prazo;

		return $dias > 0
			? 'Ela é feita sob encomenda, em ' . $dias . ( 1 === $dias ? ' dia' : ' dias' ) . '.'
			: 'Ela é feita sob encomenda.';
	}

	return '';
}
}

if ( ! function_exists( 'cdm_leads_mensagem_para_cliente' ) ) {
/**
 * A mensagem que a artesã manda quando toca no botão, já escrita e codificada.
 *
 * `rawurlencode` de "\n" já devolve %0A — não há `str_replace` de %0D%0A aqui, e
 * a ausência é o mesmo conserto que a Loja registrou em 12/09: linha defensiva
 * contra um caso que não pode acontecer é função morta com cara de cuidado.
 */
function cdm_leads_mensagem_para_cliente( $nome_cliente, $peca_titulo, $disp, $prazo, $url ) {
	$quem  = cdm_leads_nome_da_artesa();
	$texto = 'Olá, ' . cdm_leads_primeiro_nome( $nome_cliente ) . '! ';
	$texto .= 'Aqui é ' . ( '' !== $quem ? $quem : 'do Clube do Mosaico' ) . ' — ';
	$texto .= 'vi que você se interessou pela peça *' . $peca_titulo . '*.';

	$frase = cdm_leads_frase_disponibilidade( $disp, $prazo );
	if ( '' !== $frase ) {
		$texto .= ' ' . $frase;
	}
	$texto .= ' Posso te passar os detalhes de pagamento e envio?';
	$texto .= "\n" . $url;

	return rawurlencode( $texto );
}
}

if ( ! function_exists( 'cdm_leads_link_responder' ) ) {
/** O `wa.me` do CLIENTE, com a mensagem pronta. Nunca o número da artesã. */
function cdm_leads_link_responder( $zap_canonico, $nome_cliente, $peca_titulo, $disp, $prazo, $url ) {
	$so = preg_replace( '/\D+/', '', (string) $zap_canonico );
	if ( '' === $so ) {
		return '';
	}

	return 'https://wa.me/' . $so . '?text='
		. cdm_leads_mensagem_para_cliente( $nome_cliente, $peca_titulo, $disp, $prazo, $url );
}
}

if ( ! function_exists( 'cdm_leads_email_destino' ) ) {
/** Para onde vai o aviso. A option existe para "Meus dados" de um bloco futuro. */
function cdm_leads_email_destino() {
	$e = sanitize_email( (string) get_option( 'cdm_email_leads', '' ) );

	return '' !== $e ? $e : CDM_LEADS_EMAIL_PADRAO;
}
}

if ( ! function_exists( 'cdm_leads_email_html' ) ) {
/**
 * O corpo do e-mail. HTML de tabela e estilo em linha, porque cliente de e-mail
 * não é navegador — a Hotmail, que é a caixa dela, corta folha de estilo.
 *
 * As cores são as do DESIGN.md, escritas aqui porque não há token de CSS dentro
 * de um e-mail. Se a paleta mudar lá, isto fica velho; o `teste-leads.php` cobra
 * que o coral do botão seja o coral da ilha, então a divergência reprova em vez
 * de sumir.
 */
function cdm_leads_email_html( $lead_id, $peca ) {
	$id     = (int) $peca->ID;
	$titulo = (string) $peca->post_title;
	$url    = get_permalink( $peca );

	$nome = (string) get_post_meta( $lead_id, '_cdm_nome', true );
	$zap  = (string) get_post_meta( $lead_id, '_cdm_whatsapp', true );

	$disp  = function_exists( 'cdm_loja_meta' ) ? cdm_loja_meta( $id, '_cdm_disponibilidade' ) : '';
	$prazo = function_exists( 'cdm_loja_meta' ) ? cdm_loja_meta( $id, '_cdm_prazo_dias' ) : '';
	$preco = function_exists( 'cdm_loja_meta' ) ? cdm_loja_meta( $id, '_cdm_preco' ) : '';

	$preco_txt = function_exists( 'cdm_loja_preco_html' ) ? cdm_loja_preco_html( $preco ) : '';
	$preco_txt = str_replace( '&nbsp;', ' ', $preco_txt );
	$disp_txt  = function_exists( 'cdm_loja_disponibilidade_frase' )
		? cdm_loja_disponibilidade_frase( $disp, $prazo )
		: '';

	$foto = '';
	if ( function_exists( 'cdm_loja_galeria' ) ) {
		$galeria = cdm_loja_galeria( $id );
		if ( $galeria ) {
			$src = wp_get_attachment_image_src( (int) $galeria[0], 'medium_large' );
			if ( $src && ! empty( $src[0] ) ) {
				$foto = $src[0];
			}
		}
	}

	$responder = cdm_leads_link_responder( $zap, $nome, $titulo, $disp, $prazo, $url );

	$h  = '<div style="font-family:Arial,Helvetica,sans-serif;color:#1F1715;max-width:520px;margin:0 auto;">';
	$h .= '<p style="margin:0 0 20px;"><img src="https://clubedomosaico.com.br/wp-content/uploads/2026/09/logo-clube-do-mosaico.png" ';
	$h .= 'alt="Clube do Mosaico" width="180" style="display:block;height:auto;border:0;"></p>';

	$h .= '<h1 style="font-size:20px;margin:0 0 6px;">Alguém quer esta peça</h1>';
	$h .= '<p style="margin:0 0 20px;color:#6E5F5B;font-size:14px;">Chegou agora pelo site.</p>';

	if ( '' !== $foto ) {
		$h .= '<p style="margin:0 0 12px;"><img src="' . esc_url( $foto ) . '" alt="' . esc_attr( $titulo ) . '" ';
		$h .= 'width="240" style="display:block;height:auto;border-radius:14px;border:0;"></p>';
	}

	$h .= '<p style="margin:0 0 4px;font-size:18px;font-weight:700;">' . esc_html( $titulo ) . '</p>';
	if ( '' !== $preco_txt ) {
		$h .= '<p style="margin:0 0 2px;font-size:18px;font-weight:700;color:#FC483B;">' . esc_html( $preco_txt ) . '</p>';
	}
	if ( '' !== $disp_txt ) {
		$h .= '<p style="margin:0 0 20px;color:#6E5F5B;font-size:14px;">' . esc_html( $disp_txt ) . '</p>';
	}

	$h .= '<table role="presentation" cellpadding="0" cellspacing="0" border="0" ';
	$h .= 'style="width:100%;border:1px solid #E9DCD7;border-radius:14px;padding:16px;margin:0 0 24px;">';
	$h .= '<tr><td style="font-size:15px;">';
	$h .= '<strong>' . esc_html( $nome ) . '</strong><br>';
	$h .= '<span style="color:#6E5F5B;">' . esc_html( cdm_leads_wa_legivel( $zap ) ) . '</span>';
	$h .= '</td></tr></table>';

	if ( '' !== $responder ) {
		$h .= '<p style="margin:0 0 14px;"><a href="' . esc_url( $responder ) . '" ';
		$h .= 'style="display:block;background:#FC483B;color:#FFFFFF;text-decoration:none;font-size:17px;';
		$h .= 'font-weight:700;padding:16px 20px;border-radius:14px;text-align:center;">Responder no WhatsApp</a></p>';
	}

	$h .= '<p style="margin:0 0 28px;"><a href="' . esc_url( $url ) . '" ';
	$h .= 'style="color:#8A0F18;font-size:14px;">Ver a peça no site</a></p>';

	$h .= '<p style="margin:0;color:#6E5F5B;font-size:12px;line-height:1.5;">';
	$h .= 'Este e-mail foi enviado pelo Clube do Mosaico porque um cliente pediu para verificar disponibilidade.';
	$h .= '</p></div>';

	return $h;
}
}

if ( ! function_exists( 'cdm_leads_notificar' ) ) {
/**
 * Manda o aviso. Nunca derruba o envio: se o e-mail falhar, o lead continua
 * gravado e visível na aba Interessados, que é a razão de a aba existir.
 *
 * `From: contato@` e `Reply-To` vazio são do adendo. O `Reply-To` vazio não é
 * descuido: responder ao e-mail não fala com ninguém — quem fala é o botão.
 */
function cdm_leads_notificar( $lead_id, $peca ) {
	if ( ! function_exists( 'wp_mail' ) ) {
		return false;
	}
	$nome  = (string) get_post_meta( (int) $lead_id, '_cdm_nome', true );
	$assunto = 'Novo interessado: ' . (string) $peca->post_title . ' — ' . $nome;
	$corpo   = cdm_leads_email_html( (int) $lead_id, $peca );

	$ok = wp_mail( cdm_leads_email_destino(), $assunto, $corpo, cdm_leads_cabecalhos() );

	/* A SEGUNDA TENTATIVA, COM O REMETENTE PADRÃO DO SITE.
	 *
	 * O adendo manda usar `From: contato@clubedomosaico.com.br`, e a mesma linha
	 * dele diz que a casca "precisa criar a conta `contato@` no cPanel OU
	 * garantir SPF/DKIM" — isso ainda não foi feito, e é do Raphael. Muita
	 * hospedagem recusa enviar com um remetente que não existe como caixa local,
	 * e aí o `wp_mail` devolve false: o lead fica gravado e a artesã não fica
	 * sabendo dele até abrir o painel.
	 *
	 * Então, se a primeira falhar, vai uma segunda com o remetente que o próprio
	 * WordPress usa — o mesmo que entregou o e-mail de acesso dela em 12/09. Não
	 * é contorno de configuração: é a diferença entre ela ser avisada e não ser,
	 * num dia em que ninguém está olhando. E o caminho usado fica GRAVADO no
	 * lead, para a ronda ver que o `contato@` não está de pé em vez de descobrir
	 * pela ausência.
	 *
	 * Esta execução não conseguiu conferir SPF/DKIM: `dns.google` e
	 * `cloudflare-dns.com` respondem 403 ao CONNECT por política de egresso, em
	 * duas passadas cada (13/09/2026). Fica declarado, não presumido.
	 */
	$como = $ok ? 'contato@' : '';
	if ( ! $ok ) {
		$ok = wp_mail( cdm_leads_email_destino(), $assunto, $corpo, array( 'Content-Type: text/html; charset=UTF-8' ) );
		$como = $ok ? 'remetente padrao (contato@ recusado)' : '';
	}
	update_post_meta( (int) $lead_id, '_cdm_email_enviado',
		$ok ? current_time( 'mysql' ) . ' via ' . $como : 'falhou nas duas tentativas' );

	/* A CÓPIA PARA O RAPHAEL SÓ EXISTE SE ALGUÉM A PEDIR. O adendo é explícito:
	   "O Raphael NÃO recebe cópia de lead, a não ser que a option
	   `cdm_email_leads_copia` seja preenchida." */
	$copia = sanitize_email( (string) get_option( 'cdm_email_leads_copia', '' ) );
	if ( '' !== $copia ) {
		wp_mail( $copia, $assunto, $corpo, cdm_leads_cabecalhos() );
	}

	return $ok;
}
}

if ( ! function_exists( 'cdm_leads_cabecalhos' ) ) {
/**
 * Os cabeçalhos do adendo, num lugar só.
 *
 * `Reply-To` vazio não é descuido: responder ao e-mail não fala com ninguém —
 * quem fala é o botão que abre o WhatsApp do cliente.
 */
function cdm_leads_cabecalhos() {
	return array(
		'Content-Type: text/html; charset=UTF-8',
		'From: Clube do Mosaico <contato@clubedomosaico.com.br>',
	);
}
}

/* ---------------------------------------------------------------------------
 * 7. A ABA "INTERESSADOS" DENTRO DE /atelie/
 * ------------------------------------------------------------------------- */

add_filter( 'cdm_atelie_abas', function ( $abas ) {
	if ( ! is_array( $abas ) ) {
		$abas = array();
	}
	$abas['interessados'] = array( 'rotulo' => 'Interessados' );

	return $abas;
} );

if ( ! function_exists( 'cdm_leads_lista' ) ) {
/** Os leads, do mais novo para o mais velho. */
function cdm_leads_lista( $quantos = 200 ) {
	$leads = get_posts( array(
		'post_type'   => CDM_LEADS_TIPO,
		'post_status' => 'publish',
		'numberposts' => (int) $quantos,
		'orderby'     => 'date',
		'order'       => 'DESC',
	) );

	return is_array( $leads ) ? $leads : array();
}
}

if ( ! function_exists( 'cdm_leads_campos_do_lead' ) ) {
/**
 * Um lead em array, com a peça já resolvida. É a fonte ÚNICA da tela e do CSV.
 *
 * Duas telas lendo o banco por caminhos diferentes é como a ficha da peça e a
 * bancada passaram a divergir no título na Aquametria: o CSV que a artesã baixa
 * tem de ser o que ela vê, e a única forma de garantir isso é os dois lerem daqui.
 */
function cdm_leads_campos_do_lead( $lead ) {
	$id      = (int) $lead->ID;
	$peca_id = (int) get_post_meta( $id, '_cdm_peca_id', true );
	$peca    = $peca_id > 0 ? get_post( $peca_id ) : null;
	$zap     = (string) get_post_meta( $id, '_cdm_whatsapp', true );
	$nome    = (string) get_post_meta( $id, '_cdm_nome', true );

	$titulo = $peca ? (string) $peca->post_title : 'peça apagada';
	$url    = $peca ? get_permalink( $peca ) : '';
	$disp   = ( $peca && function_exists( 'cdm_loja_meta' ) ) ? cdm_loja_meta( $peca_id, '_cdm_disponibilidade' ) : '';
	$prazo  = ( $peca && function_exists( 'cdm_loja_meta' ) ) ? cdm_loja_meta( $peca_id, '_cdm_prazo_dias' ) : '';

	$status = (string) get_post_meta( $id, '_cdm_status', true );
	$estados = cdm_leads_estados();
	if ( ! isset( $estados[ $status ] ) ) {
		$status = 'novo';
	}

	return array(
		'id'        => $id,
		'nome'      => $nome,
		'whatsapp'  => $zap,
		'legivel'   => cdm_leads_wa_legivel( $zap ),
		'peca'      => $titulo,
		'peca_id'   => $peca_id,
		'peca_url'  => $url,
		'status'    => $status,
		'quando'    => (string) $lead->post_date_gmt,
		'origem'    => (string) get_post_meta( $id, '_cdm_origem', true ),
		'responder' => '' !== $url ? cdm_leads_link_responder( $zap, $nome, $titulo, $disp, $prazo, $url ) : '',
	);
}
}

if ( ! function_exists( 'cdm_leads_data_curta' ) ) {
/** "13/09, 11h20" — o que serve para ela saber se já ligou hoje. */
function cdm_leads_data_curta( $mysql ) {
	$t = strtotime( (string) $mysql );
	if ( ! $t ) {
		return '';
	}

	return date( 'd/m', $t ) . ', ' . date( 'H\hi', $t );
}
}

if ( ! function_exists( 'cdm_leads_tela_interessados' ) ) {
/**
 * A aba. Um cartão por interessado, com o botão de responder do lado.
 *
 * A CONTAGEM DO TÍTULO É CONTADA, NUNCA DIGITADA — a cicatriz dos cartões da
 * casca desta ilha, que diziam "0" enquanto o banco tinha cinco rejuntes.
 */
function cdm_leads_tela_interessados( $usuaria ) {
	$leads = cdm_leads_lista();
	$novos = 0;
	$linhas = array();
	foreach ( $leads as $l ) {
		$um = cdm_leads_campos_do_lead( $l );
		if ( 'novo' === $um['status'] ) {
			$novos++;
		}
		$linhas[] = $um;
	}

	$h  = '<div class="cdm-at">';
	if ( function_exists( 'cdm_atelie_aviso_html' ) ) {
		$h .= cdm_atelie_aviso_html();
	}
	$h .= '<div class="cdm-at-cabeca">';
	$h .= '<h2 class="cdm-at-h2">Interessados</h2>';
	if ( function_exists( 'cdm_atelie_url' ) ) {
		$h .= '<p class="cdm-at-sair"><a href="' . esc_url( cdm_atelie_url( array(
			'cdm_acao'  => 'sair',
			'cdm_nonce' => wp_create_nonce( 'cdm_atelie_sair' ),
		) ) ) . '">Sair</a></p>';
	}
	$h .= '</div>';

	if ( function_exists( 'cdm_atelie_abas_html' ) ) {
		$h .= cdm_atelie_abas_html( 'interessados' );
	}

	if ( ! $linhas ) {
		$h .= '<div class="cdm-vazio">';
		$h .= '<h3>Ninguém pediu ainda</h3>';
		$h .= '<p>Quando alguém tocar em <strong>Verificar disponibilidade</strong> numa peça sua, o nome e o WhatsApp aparecem aqui — e um aviso chega no seu e-mail na hora.</p>';
		$h .= '</div>';
		/* TELA SEM LUGAR DE AGIR É UM BECO, e foi o portão do navegador que a
		   nomeou: a aba vazia não tinha uma única ação. Quem chega aqui e não
		   tem interessado precisa de uma saída, e a saída útil é a que faz
		   aparecer interessado — publicar peça. */
		if ( function_exists( 'cdm_atelie_url' ) ) {
			$h .= '<p class="cdm-at-acao cdm-at-acao-grande">';
			$h .= '<a class="cdm-botao cdm-at-botao" href="' . esc_url( cdm_atelie_url( array( 'estado' => 'nova' ) ) ) . '">+ Nova peça</a>';
			$h .= '</p>';
			$h .= '<p class="cdm-at-linha"><a href="' . esc_url( cdm_atelie_url() ) . '">Ver minhas peças</a></p>';
		}
		$h .= '</div>';

		return $h;
	}

	$h .= '<p class="cdm-at-linha cdm-leads-conta">';
	$h .= count( $linhas ) === 1 ? '1 pessoa perguntou' : count( $linhas ) . ' pessoas perguntaram';
	/* "sem resposta" não flexiona, então não há ternário de plural aqui — um que
	   devolvesse a mesma frase dos dois lados seria a "função morta" que esta
	   ilha já nomeou: parece regra e não decide nada. */
	if ( $novos > 0 ) {
		$h .= ' · <strong>' . $novos . ' sem resposta</strong>';
	}
	$h .= '</p>';

	$h .= '<ul class="cdm-at-lista cdm-leads-lista">';
	foreach ( $linhas as $um ) {
		$nonce = wp_create_nonce( 'cdm_lead_status_' . $um['id'] );

		$h .= '<li class="cdm-at-item cdm-lead-item">';
		$h .= '<div class="cdm-at-item-texto">';
		$h .= '<h3>' . esc_html( $um['nome'] ) . '</h3>';
		$h .= '<p class="cdm-lead-zap"><span class="cdm-medida">' . esc_html( $um['legivel'] ) . '</span></p>';
		$h .= '<p class="cdm-lead-sobre">';
		if ( '' !== $um['peca_url'] ) {
			$h .= '<a href="' . esc_url( $um['peca_url'] ) . '">' . esc_html( $um['peca'] ) . '</a>';
		} else {
			$h .= esc_html( $um['peca'] );
		}
		$h .= ' <span class="cdm-lead-quando">' . esc_html( cdm_leads_data_curta( $um['quando'] ) ) . '</span></p>';

		if ( '' !== $um['responder'] ) {
			$h .= '<p class="cdm-at-item-acoes"><a class="cdm-botao cdm-lead-responder" href="' . esc_url( $um['responder'] );
			$h .= '" rel="noopener">Responder no WhatsApp</a></p>';
		}

		/* O estado é um formulário próprio, com nonce: ação que muda dado nunca
		   sai de um link (a mesma regra do publicar/pausar da lista de peças). */
		$h .= '<form class="cdm-at-mini-form cdm-lead-estado" method="post" action="'
			. esc_url( function_exists( 'cdm_atelie_url' ) ? cdm_atelie_url( array( 'estado' => 'interessados' ) ) : '' ) . '">';
		$h .= '<input type="hidden" name="cdm_nonce" value="' . esc_attr( $nonce ) . '">';
		$h .= '<input type="hidden" name="cdm_lead" value="' . (int) $um['id'] . '">';
		$h .= '<label class="cdm-lead-rotulo" for="cdm-lead-st-' . (int) $um['id'] . '">Como ficou</label>';
		$h .= '<select id="cdm-lead-st-' . (int) $um['id'] . '" name="cdm_status">';
		foreach ( cdm_leads_estados() as $chave => $rotulo ) {
			$h .= '<option value="' . esc_attr( $chave ) . '"' . ( $chave === $um['status'] ? ' selected' : '' ) . '>';
			$h .= esc_html( $rotulo ) . '</option>';
		}
		$h .= '</select>';
		$h .= '<button class="cdm-at-botao-fraco" type="submit" name="cdm_acao" value="lead_status">Guardar</button>';
		$h .= '</form>';

		$h .= '</div></li>';
	}
	$h .= '</ul>';

	/* A CÓPIA DA SEÇÃO 24 PARA O LEAD (decisão 6). */
	$h .= '<p class="cdm-at-acao cdm-leads-baixar">';
	$h .= '<a class="cdm-at-botao-fraco" href="' . esc_url( function_exists( 'cdm_atelie_url' ) ? cdm_atelie_url( array(
		'cdm_acao'  => 'leads_csv',
		'cdm_nonce' => wp_create_nonce( 'cdm_leads_csv' ),
	) ) : '' ) . '">Baixar em CSV</a>';
	$h .= '</p>';
	$h .= '<p class="cdm-at-linha cdm-leads-nota">O CSV abre no Excel e no Google Planilhas. É a sua cópia: '
		. 'estes nomes e telefones existem só aqui dentro, e não vão para lugar nenhum além da sua mão.</p>';

	$h .= '</div>';

	return $h;
}
}

/* A tela é servida pelo Ateliê, que pergunta por filtro quem sabe desenhar cada
   aba. O Ateliê APLICA este filtro (ver `clubedomosaico-atelie.php`, seção 6). */
add_filter( 'cdm_atelie_tela', function ( $html, $estado, $usuaria ) {
	if ( 'interessados' !== $estado ) {
		return $html;
	}

	return cdm_leads_tela_interessados( $usuaria );
}, 10, 3 );

/* ---------------------------------------------------------------------------
 * 7b. A SEÇÃO DENTRO DE "MEUS DADOS" — as duas options que eram só nossas
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_leads_form_meus_dados' ) ) {
/**
 * Os dois campos, com o efeito do vazio escrito ao lado de cada um.
 *
 * A ASSINATURA MOSTRA O ESTADO DE HOJE, e mostra o valor REAL — nunca um exemplo
 * fabricado com um nome de cliente inventado. "Hoje as mensagens assinam: do
 * Clube do Mosaico" é um fato que ela confere; "Olá, Maria! Aqui é..." seria uma
 * tela ensinando a ler um dado que não existe.
 */
function cdm_leads_form_meus_dados() {
	$email_gravado = sanitize_email( (string) get_option( 'cdm_email_leads', '' ) );
	$nome_gravado  = trim( (string) get_option( 'cdm_artesa_nome', '' ) );
	$assina        = ( '' !== $nome_gravado ) ? $nome_gravado : 'do Clube do Mosaico';

	$h  = '<form class="cdm-at-form" method="post" action="' . esc_url( cdm_atelie_url() ) . '">';
	$h .= '<input type="hidden" name="cdm_acao" value="leads_dados">';
	$h .= '<input type="hidden" name="cdm_nonce" value="' . esc_attr( wp_create_nonce( 'cdm_leads_dados' ) ) . '">';

	$h .= '<p class="cdm-at-campo"><label for="cdm-leads-email">E-mail para receber os avisos</label>';
	$h .= '<input id="cdm-leads-email" name="cdm_email_leads" type="email" autocomplete="email" inputmode="email" value="'
		. esc_attr( $email_gravado ) . '">';
	$h .= '<span class="cdm-at-ajuda">Deixe em branco para usar o e-mail da sua conta ('
		. esc_html( CDM_LEADS_EMAIL_PADRAO ) . '). Hoje os avisos vão para <strong>'
		. esc_html( cdm_leads_email_destino() ) . '</strong>.</span></p>';

	$h .= '<p class="cdm-at-campo"><label for="cdm-artesa-nome">Como você quer assinar as mensagens</label>';
	$h .= '<input id="cdm-artesa-nome" name="cdm_artesa_nome" type="text" autocomplete="name" maxlength="60" value="'
		. esc_attr( $nome_gravado ) . '">';
	$h .= '<span class="cdm-at-ajuda">É o nome que aparece na mensagem pronta do WhatsApp. '
		. 'Hoje as mensagens assinam: <strong>' . esc_html( $assina ) . '</strong>.</span></p>';

	$h .= '<p class="cdm-at-acao"><button class="cdm-botao cdm-at-botao" type="submit">Guardar</button></p>';
	$h .= '</form>';

	return $h;
}
}

add_filter( 'cdm_atelie_meus_dados', function ( $secoes, $usuaria ) {
	if ( ! is_array( $secoes ) ) {
		$secoes = array();
	}
	$secoes['leads'] = array(
		'titulo' => 'Avisos de interessados',
		'linha'  => 'Quando alguém pede uma peça sua, um aviso sai na hora. Aqui você diz para onde ele vai e como você assina.',
		'html'   => cdm_leads_form_meus_dados(),
	);

	return $secoes;
}, 10, 2 );

/* ---------------------------------------------------------------------------
 * 8. AS AÇÕES DO PAINEL — mudar o estado e baixar o CSV
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'cdm_leads_celula_segura' ) ) {
/**
 * Uma célula que o Excel não vai EXECUTAR.
 *
 * O CSV é a cópia da seção 24 e vai para a planilha de uma pessoa de verdade. O
 * campo `nome` é digitado por qualquer um que abra a ficha de uma peça na
 * internet — e planilha trata célula que começa por `=`, `+`, `-` ou `@` como
 * FÓRMULA, não como texto. Um nome escrito como `=HYPERLINK(...)` vira um link
 * clicável dentro da planilha dela; há variações piores.
 *
 * O escape do CSV não resolve isso: aspas protegem a coluna, não a leitura. O
 * que resolve é um apóstrofo na frente, que é como planilha nenhuma trata a
 * célula como fórmula — e que some da tela quando ela olha.
 *
 * A lista inclui tabulação e retorno de carro porque alguns leitores os pulam
 * antes de decidir o que é fórmula, e aí o `=` volta a ser o primeiro caractere
 * que importa. É a mesma família do "perdoar por presença de palavra é
 * adivinhar": quem decide é a estrutura do começo da célula, não a aparência
 * dela.
 */
function cdm_leads_celula_segura( $valor ) {
	$texto = (string) $valor;
	if ( '' === $texto ) {
		return '';
	}
	$primeiro = substr( $texto, 0, 1 );
	if ( false !== strpos( "=+-@\t\r", $primeiro ) ) {
		return "'" . $texto;
	}

	return $texto;
}
}

if ( ! function_exists( 'cdm_leads_csv' ) ) {
/**
 * O CSV, como texto. Separado da ação que o serve para PODER ser medido.
 *
 * Ponto-e-vírgula e não vírgula: o Excel em português trata a vírgula como
 * separador decimal e joga a planilha inteira numa coluna só. E o BOM na frente,
 * porque sem ele o Excel lê UTF-8 como Latin-1 e o nome de qualquer pessoa com
 * acento chega torto na tela dela.
 */
function cdm_leads_csv( $linhas ) {
	$saida = "\xEF\xBB\xBF";
	$cab   = array( 'quando', 'nome', 'whatsapp', 'peca', 'status', 'origem' );
	$saida .= implode( ';', $cab ) . "\r\n";

	$estados = cdm_leads_estados();
	foreach ( $linhas as $um ) {
		$campos = array(
			$um['quando'],
			$um['nome'],
			$um['legivel'],
			$um['peca'],
			isset( $estados[ $um['status'] ] ) ? $estados[ $um['status'] ] : $um['status'],
			$um['origem'],
		);
		$escapados = array();
		foreach ( $campos as $c ) {
			$escapados[] = '"' . str_replace( '"', '""', cdm_leads_celula_segura( $c ) ) . '"';
		}
		$saida .= implode( ';', $escapados ) . "\r\n";
	}

	return $saida;
}
}

if ( ! function_exists( 'cdm_leads_agir_painel' ) ) {
/**
 * As duas ações da aba. Nonce E capacidade nas duas, como o Ateliê faz — nonce
 * sem capacidade protege do site de fora e não da pessoa errada logada.
 */
function cdm_leads_agir_painel() {
	if ( ! function_exists( 'cdm_atelie_e_minha_pagina' ) || ! cdm_atelie_e_minha_pagina() ) {
		return;
	}
	$acao = cdm_atelie_post( 'cdm_acao' );
	if ( '' === $acao ) {
		$acao = cdm_atelie_get( 'cdm_acao' );
	}

	if ( 'lead_status' === $acao ) {
		$id = (int) cdm_atelie_post( 'cdm_lead', '0' );
		if ( ! current_user_can( 'edit_pecas' ) ) {
			wp_safe_redirect( cdm_atelie_url( array( 'estado' => 'interessados', 'aviso' => 'nonce' ) ) );
			exit;
		}
		if ( ! wp_verify_nonce( cdm_atelie_post( 'cdm_nonce' ), 'cdm_lead_status_' . $id ) ) {
			wp_safe_redirect( cdm_atelie_url( array( 'estado' => 'interessados', 'aviso' => 'nonce' ) ) );
			exit;
		}
		$novo    = cdm_atelie_post( 'cdm_status' );
		$estados = cdm_leads_estados();
		$lead    = $id > 0 ? get_post( $id ) : null;
		if ( $lead && CDM_LEADS_TIPO === $lead->post_type && isset( $estados[ $novo ] ) ) {
			update_post_meta( $id, '_cdm_status', $novo );
		}
		wp_safe_redirect( cdm_atelie_url( array( 'estado' => 'interessados', 'aviso' => 'lead' ) ) );
		exit;
	}

	/* AS DUAS OPTIONS DE "MEUS DADOS". Grava quem as lê, pela decisão do cabeçalho.
	 *
	 * O E-MAIL VAZIO É UM VALOR, não um erro: significa "use o endereço da conta",
	 * e é por isso que o campo em branco GRAVA vazio em vez de ser ignorado — sem
	 * isso ela não teria como desfazer um endereço que digitou por engano. O que
	 * é recusado é endereço INVÁLIDO: aí o antigo fica de pé e a tela diz que não
	 * deu, porque trocar um endereço que funciona por um que não existe é como o
	 * aviso do interessado some sem ninguém perceber.
	 *
	 * O NOME PASSA POR sanitize_text_field E POR UM TETO DE 60: ele vai dentro de
	 * uma URL de wa.me e dentro do corpo de um e-mail, e uma quebra de linha ali
	 * parte a mensagem no meio. */
	/* A GUARDA DO `defined` NÃO É PARANOIA: o Sync desembarca um snippet sem o
	   outro, e este arquivo pode chegar ao ar minutos antes do Ateliê 1.2.0, que
	   é quem declara a constante. Sem ela, a primeira pessoa que abrisse o painel
	   com um POST desta ação levaria um erro fatal do PHP no lugar da tela. Com
	   ela, a ação simplesmente não existe enquanto o outro lado não chega — que é
	   o mesmo que acontece com a seção, porque o filtro não é aplicado. */
	if ( 'leads_dados' === $acao && defined( 'CDM_ATELIE_ABA_DADOS' ) ) {
		$volta = array( 'estado' => CDM_ATELIE_ABA_DADOS );
		if ( ! current_user_can( 'edit_pecas' )
			|| ! wp_verify_nonce( cdm_atelie_post( 'cdm_nonce' ), 'cdm_leads_dados' ) ) {
			$volta['aviso'] = 'nonce';
			wp_safe_redirect( cdm_atelie_url( $volta ) );
			exit;
		}

		$bruto = trim( cdm_atelie_post( 'cdm_email_leads' ) );
		if ( '' === $bruto ) {
			update_option( 'cdm_email_leads', '' );
			$volta['aviso'] = 'dados';
		} else {
			$limpo = sanitize_email( $bruto );
			if ( '' === $limpo ) {
				$volta['aviso'] = 'email-ruim';
			} else {
				update_option( 'cdm_email_leads', $limpo );
				$volta['aviso'] = 'dados';
			}
		}

		$nome = sanitize_text_field( cdm_atelie_post( 'cdm_artesa_nome' ) );
		if ( function_exists( 'mb_substr' ) ) {
			$nome = mb_substr( $nome, 0, 60 );
		} else {
			$nome = substr( $nome, 0, 60 );
		}
		update_option( 'cdm_artesa_nome', trim( $nome ) );

		wp_safe_redirect( cdm_atelie_url( $volta ) );
		exit;
	}

	if ( 'leads_csv' === $acao ) {
		if ( ! current_user_can( 'edit_pecas' )
			|| ! wp_verify_nonce( cdm_atelie_get( 'cdm_nonce' ), 'cdm_leads_csv' ) ) {
			wp_safe_redirect( cdm_atelie_url( array( 'estado' => 'interessados', 'aviso' => 'nonce' ) ) );
			exit;
		}
		$linhas = array();
		foreach ( cdm_leads_lista( 2000 ) as $l ) {
			$linhas[] = cdm_leads_campos_do_lead( $l );
		}
		nocache_headers();
		header( 'Content-Type: text/csv; charset=UTF-8' );
		header( 'Content-Disposition: attachment; filename="interessados-' . date( 'Y-m-d' ) . '.csv"' );
		echo cdm_leads_csv( $linhas ); // CSV montado aqui, já escapado campo a campo.
		exit;
	}
}
}

add_action( 'template_redirect', 'cdm_leads_agir_painel', 6 );

/* ---------------------------------------------------------------------------
 * 9. A FOLHA E A MÁSCARA — no `wp_footer` (seção 8)
 *
 * O script faz UMA coisa e ela é enfeite: põe parêntese e traço no telefone
 * enquanto se digita. Com o JavaScript desligado o formulário funciona inteiro —
 * o número chega sem máscara e a canonização do PHP resolve, que é onde ela
 * sempre esteve.
 *
 * Sem um "&" duplo em lugar nenhum, e isto está no rodapé justamente para não
 * passar pelos filtros do conteúdo (cicatriz de 08/09/2026).
 * ------------------------------------------------------------------------- */

add_action( 'wp_footer', function () {
	$na_peca   = function_exists( 'cdm_loja_e_peca' ) && cdm_loja_e_peca();
	$no_painel = function_exists( 'cdm_atelie_e_minha_pagina' ) && cdm_atelie_e_minha_pagina();
	if ( ! $na_peca && ! $no_painel ) {
		return;
	}

	$css = <<<'CSS'
.cdm-lead{margin:0 0 .75rem;}
.cdm-lead>summary{display:inline-block;cursor:pointer;list-style:none;}
.cdm-lead>summary::-webkit-details-marker{display:none;}
.cdm-lead[open]>summary{margin-bottom:1rem;}
.cdm-lead-form{border:1px solid var(--traco,#E9DCD7);border-radius:14px;padding:1.25rem;background:var(--papel,#fff);}
.cdm-lead-campo{margin:0 0 1rem;}
.cdm-lead-campo label{display:block;font-size:.9375rem;font-weight:600;margin:0 0 .35rem;}
.cdm-lead-campo input{width:100%;box-sizing:border-box;padding:.75rem;font-size:1.0625rem;
	border:1px solid var(--traco,#E9DCD7);border-radius:8px;background:#fff;color:var(--tinta,#1F1715);}
.cdm-lead-campo input:focus{outline:2px solid var(--coral,#FC483B);outline-offset:1px;}
.cdm-lead-hp{position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden;}
/* O ALVO DE TOQUE DO CONSENTIMENTO E O RÓTULO INTEIRO, e é por isso que ele
   tem `min-height`: quem marca um checkbox de 24 px no celular acerta o texto,
   não o quadradinho. O `padding` do rótulo é o que faz a área clicável passar
   dos 44 px que o portão do navegador cobra. */
.cdm-lead-consente{margin:0 0 1.25rem;font-size:.9375rem;line-height:1.6;color:var(--legenda,#6E5F5B);}
.cdm-lead-consente label{display:flex;gap:.6rem;align-items:flex-start;min-height:44px;padding:.35rem 0;cursor:pointer;}
.cdm-lead-consente input{margin-top:.25rem;flex:0 0 auto;width:24px;height:24px;}
.cdm-lead-enviar{margin:0;}
/* 44 px de altura mínima. Ele saía com 43 — um pixel abaixo do alvo de toque, o
   mesmo defeito que os botões de foto do painel tiveram em 12/09, e do mesmo
   jeito: invisível em leitura de código, porque só o motor de layout sabe a
   altura que o botão ficou tendo. Quem o achou foi o portão a 360 px. */
.cdm-lead-enviar .cdm-botao{display:block;width:100%;box-sizing:border-box;
	min-height:44px;padding:.85rem 1rem;text-align:center;}
.cdm-lead-erro{margin:0 0 1rem;padding:.75rem 1rem;border-left:3px solid var(--alerta,#B9791A);
	background:#FDF6EC;font-size:.9375rem;}
.cdm-lead-pronto{border:2px solid var(--coral,#FC483B);border-radius:14px;padding:1.25rem;margin:0 0 1rem;}
.cdm-lead-pronto h3{margin:0 0 .4rem;font-size:1.3125rem;}
.cdm-lead-pronto p{margin:0;}
.cdm-leads-conta{color:var(--legenda,#6E5F5B);font-size:.9375rem;margin:0 0 1rem;}
.cdm-lead-zap{margin:.1rem 0;}
.cdm-lead-sobre{margin:.1rem 0 .6rem;font-size:.9375rem;color:var(--legenda,#6E5F5B);}
.cdm-lead-quando{font-size:.8125rem;}
.cdm-lead-responder{display:inline-block;}
.cdm-lead-estado{display:flex;gap:.5rem;align-items:center;flex-wrap:wrap;margin-top:.5rem;}
.cdm-lead-rotulo{font-size:.8125rem;color:var(--legenda,#6E5F5B);}
/* 44 px e 1 rem: abaixo de 44 o dedo erra, e abaixo de 16 px o iPhone dá zoom
   sozinho ao tocar no campo — a tela pula e ela perde o lugar. Saía com 34 px e
   15 px, e foi o portão a 360 px que contou. */
.cdm-lead-estado select{min-height:44px;padding:.55rem;border:1px solid var(--traco,#E9DCD7);
	border-radius:8px;font-size:1rem;background:var(--papel,#fff);color:var(--tinta,#1F1715);}
.cdm-leads-nota{font-size:.8125rem;color:var(--legenda,#6E5F5B);}
@media (max-width:420px){.cdm-lead-form{padding:1rem;}}
CSS;

	echo '<style id="cdm-leads-folha">' . $css . '</style>' . "\n";

	if ( ! $na_peca ) {
		return;
	}

	$js = <<<'JS'
(function(){
	var campos = document.querySelectorAll('.cdm-lead-form input[type="tel"]');
	if (!campos.length) { return; }
	function formatar(v){
		var d = v.replace(/\D+/g, '').slice(0, 11);
		if (d.length <= 2) { return d; }
		var ddd = d.slice(0, 2), resto = d.slice(2);
		if (resto.length <= 4) { return '(' + ddd + ') ' + resto; }
		var corte = resto.length > 8 ? 5 : 4;
		return '(' + ddd + ') ' + resto.slice(0, corte) + '-' + resto.slice(corte);
	}
	Array.prototype.forEach.call(campos, function(campo){
		campo.addEventListener('input', function(){
			var pos = campo.value.length - campo.selectionStart;
			campo.value = formatar(campo.value);
			campo.selectionStart = campo.selectionEnd = Math.max(0, campo.value.length - pos);
		});
	});
})();
JS;

	echo '<script id="cdm-leads-mascara">' . $js . '</script>' . "\n";
}, 22 );
