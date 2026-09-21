/**
 * Robometria R1 — Qual peça serve no meu robô aspirador
 * Versão: 1.11.1 (21/09/2026) — A CAUDA DA DIVERGÊNCIA CONCORDA EM GÊNERO. Ela
 * conta `declarações`, que é palavra feminina, e o numeral saía da tabela
 * masculina: com UM canal divergente a página servia "as dois declarações".
 * Medido no ar em 21/09, no filtro `positivo-11206516` — o primeiro registro
 * desta ilha com exatamente um canal divergente. Com dois ou mais ninguém podia
 * ver, porque do três em diante o numeral não flexiona. A referência em Python
 * mudou na mesma passada, que é o que o teste-r1.php compara frase a frase, e
 * `mutacoes-divergencia.py` ganhou a mutação que devolve o masculino.
 *
 * Versão: 1.11.0 (18/09/2026) — A FRASE DE AUSÊNCIA PAROU DE NEGAR O BOTÃO QUE
 * ESTA PÁGINA SERVE. A contagem de "sem link de loja" olhava `afiliado.url` (a
 * ficha) e chamava de ausência todo item cuja porta era a busca — e a busca é o
 * PISO da 25.2, que estava lá, com link de afiliado vivo dois centímetros
 * abaixo da frase. Quem decide agora é `robometria_casca_degrau_da_porta()`, a
 * mesma função que monta o botão, e a tela passou a separar dois fatos
 * diferentes: item SEM porta e item cuja porta abre a BUSCA da loja em vez da
 * ficha do produto. Item 3 do despacho da Sentinela de 18/09/2026.
 *
 * Versão: 1.10.0 (16/09/2026) — a vitrine mostra a foto, e o painel dela sai da
 * casca. A imagem vem da Open API da Shopee (seção 25.6), com dimensão MEDIDA
 * do arquivo.
 *
 * Versão: 1.9.1 (16/09/2026) — o comentário do painel vazio deixa de prometer
 * um encaixe em traço que nunca foi ao ar, e a régua da vitrine passa a contar
 * item SEM foto em vez de um painel por peça.
 *
 * Versão: 1.9.0 (14/09/2026) — A DESCRIÇÃO EM JSON-LD PARA DE ENUMERAR OS TIPOS
 * DE CABEÇA, e ela estava VELHA no ar. A frase que um modelo de linguagem lê
 * para saber o que esta ferramenta faz dizia "filtro, escova lateral, escova
 * principal, mop e bateria" — cinco tipos — enquanto o seletor oferecia SEIS
 * desde 13/09, quando o reservatório entrou com quatro peças declaradas. A
 * lista estava digitada dentro do sprintf, colada a dois números (pares e
 * marcas) que sempre foram computados do banco: é isso que faz uma lista velha
 * passar por medida e ninguém reconferir. Agora ela sai de $d['tipos'], que já
 * era gerado da varredura. Nenhuma URL mudou, nenhuma peça entrou ou saiu, e o
 * único texto servido que muda é essa frase. A mesma cópia existia em
 * ferramentas/cobertura-r1.py e também morreu: a lista de tipos consultáveis
 * passou a ser DERIVADA do esquema (tipos_consultaveis_na_r1), pela 26.2.
 * Versão: 1.8.0 (14/09/2026) — AS TRÊS CONTAS DA TABELA GANHAM NOME (item 2 do
 * despacho da Sentinela). A página dizia "63 pares peça × modelo" no alto e "73
 * pares peça × modelo" duas telas abaixo: dois números certos contando coisas
 * diferentes com o mesmo nome. Contado, a diferença não é a que parecia — a
 * tabela tem uma linha por (modelo, tipo, peça), responde 63 células e mostra 56
 * pares, enquanto o banco declara 63. Os DOIS 63 são grandezas diferentes que
 * hoje coincidem por acidente, e igualar os números teria colado duas contas que
 * não são a mesma. A seção 19 do teste-r1.php recomputa as quatro do banco.
 * Versão: 1.7.0 (14/09/2026) — a cópia local da escada de compra MORREU. Esta
 * ferramenta repetia a porta de compra inteira para o caso de a casca não estar
 * carregada, com a frase "Link de loja em breve" que a seção 7 proibiu hoje —
 * segunda cópia da mesma decisão é combinar de divergir depois, que é a cicatriz
 * do artigo do publicador de manhã. Agora a saída degradada diz o que é e não
 * promete nada, e quem serve o piso da 25.2 é a casca, num lugar só.
 * Versão: 1.6.0 (14/09/2026) — O ARTIGO DE QUEM PUBLICA SAI DO BANCO, e a
 * concordância junto. Até 1.5.0 o "A " que abre a frase e o "que a " do meio
 * dela eram DIGITADOS, em quatro moldes e no cartão da vitrine, e o verbo era
 * sempre singular. Estava certo por acidente: todo publicador que chega a essas
 * frases é feminino singular — e o mesmo banco já publica "Mundo Conectado"
 * (masculino) e "Lojas WAP" (plural). Agora o artigo, a maiúscula de começo de
 * frase e o número viajam como fato em `gramatica_do_publicador`, derivados de
 * dados/publicadores.json e da tabela do esquema. Nenhuma tabela de língua mora
 * neste arquivo. Ver a seção 18 de ferramentas/teste-r1.php e a bateria
 * ferramentas/mutacoes-artigo-do-publicador.py.
 * Versão: 1.5.0 (14/09/2026) — QUEM DECLARA É O PUBLICADOR, E NUNCA O RÓTULO DO
 * LADO. O cartão da vitrine escrevia "o fabricante declara esta peça", digitado,
 * para qualquer degrau, e a frase do kit sem avulso escrevia "que o fabricante
 * declara" na mesma oração que já nomeava "A Electrolux (loja oficial)". O
 * degrau 4 tem fala_pela_marca verdadeiro — por isso o item fica do lado do
 * fabricante na divisão da página —, e a escada de fontes decidiu, com todas as
 * letras, que a atribuição dele é "pela loja oficial da marca", porque quem
 * transcreveu foi a loja. Falar pela marca não é ser a marca. Agora as quatro
 * frases de resposta e o cartão citam o publicador do item, lido do banco.
 * Nenhuma URL mudou e nenhuma peça entrou ou saiu.
 * NOTA DE VERSÃO: a constante ROBOMETRIA_R1_VERSAO estava em 1.3.0 enquanto este
 * cabeçalho já dizia 1.4.0 — a execução de 13/09 moveu o texto e não a constante.
 * Não houve efeito no ar (a constante só decide se a ESTRUTURA da página é
 * refeita, e a 1.4.0 não mexeu em título, slug nem shortcode), mas era a versão
 * que o teste imprime e que o manifest descreve. Sobe para 1.5.0 nas duas.
 * Versão: 1.4.0 (13/09/2026) — QUEM DIVERGE DECIDE A FRASE. A cauda da
 * divergência era fixa ("Dois canais do fabricante discordam") e o título do
 * bloco dizia o mesmo; as duas eram verdadeiras por acidente do banco, porque
 * toda divergência de peça vinha de canal de fabricante. Com o primeiro registro
 * cujos canais divergentes são marketplace e varejista, elas passaram a emprestar
 * a autoridade do FABRICANTE a quem só revende. Agora o número sai contado e o
 * lado é lido do degrau que cada divergência declara (fala_pela_marca, no
 * esquema). Nenhuma URL mudou.
 * Versão: 1.3.0 (13/09/2026) — a frase devolve a função a quem a leu (seção 26.3
 * do ARQUIPELAGO.md). "A WAP declara a escova lateral 'Escova Direita ...'"
 * estava no ar em cinco peças e a WAP nunca usou a palavra "lateral": ela batiza
 * pela posição, e a Xiaomi nem isso — publica "Brush". Onde a função não veio do
 * título, o verbo "declara" passa a recair sobre o que o fabricante de fato
 * declarou (o nome da peça e a lista de modelos) e a atribuição da função vira
 * ressalva própria. Nenhuma URL mudou e nenhuma peça saiu do banco.
 * Versão: 1.2.0 (11/09/2026) — a abertura fala com quem entrou e a procedência
 * desce um parágrafo, para a camada de prova; o catálogo da casca recebe o
 * título desta constante; e garantir_pagina() passou a reespelhar o post_title
 * quando o nome muda — sem isso, o nome do ar envelhecia calado.
 * Versão: 1.1.2 (11/09/2026) — devolve à casca a folha do FORMULÁRIO, pelo mesmo
 * motivo por que já tinha devolvido a da porta de compra: as regras .rbm-promessa
 * e .rbm-form* estavam idênticas aqui e na R2, e a home passou a servir o mesmo
 * formulário. Três cópias divergem em silêncio; uma não. Nenhuma regra mudou de
 * valor — a versão da casca é a união das duas — e nenhuma frase de resposta
 * mudou.
 * Versão: 1.1.1 (10/09/2026) — Bloco 5: a ferramenta ganha o link de volta para
 * o artigo-âncora (mão dupla, seção 9 do ARQUIPELAGO.md) e devolve à casca a
 * folha da porta de compra, que agora tem um dono só e vale para toda página que
 * recomenda item. Nenhuma frase de resposta mudou.
 * Versão: 1.1.0 (10/09/2026) — despacho da Sentinela de 10/09, item 0: a
 * procedência deixa de ser a única porta de compra. Versão 1.0.0 (10/09/2026):
 * Bloco 4 da fila, com a vitrine do Bloco 4e junto, porque a seção 6 do
 * ARQUIPELAGO.md manda a vitrine nascer na PRIMEIRA ferramenta e não como
 * acabamento depois.
 *
 * O QUE A 1.1.0 CORRIGE, e é uma cicatriz do arquipélago inteiro (seção 7 do
 * ARQUIPELAGO.md): a versão 1.0.0 publicou 45 pares peça × modelo em que o
 * ÚNICO link clicável de cada peça levava para a loja do FABRICANTE. A página
 * ficou impecável de procedência e perfeita para a Electrolux — quem decidia
 * comprar clicava no único link que existia, e a ilha não ganhava nada. Agora:
 * (1) o bloco de compra, com link de afiliado, vem ANTES da prova de
 * procedência, na mesma resposta; (2) o link de procedência é discreto, com o
 * texto "fonte" e rel="nofollow noopener", nunca um botão; (3) o bloco de
 * compra nunca fica vazio: sem ficha de produto ele desce a escada da 25.1 até a
 * busca, que a máquina fabrica sozinha (14/09/2026). A página publica quantas
 * peças ainda não têm link RASTREÁVEL — que é dívida de comissão, não de saída.
 *
 * A ferramenta de compatibilidade desta ilha: dado um modelo de robô, ela diz
 * qual filtro, escova, mop ou bateria o FABRICANTE declarou — com o código, o
 * conjunto de modelos que ele citou, o endereço da declaração e a data. Quando
 * não há declaração, ela recusa com todas as letras e para ali.
 *
 * ---------------------------------------------------------------------------
 * AS QUATRO DECISÕES DE DESENHO, e por que cada uma é assim
 * ---------------------------------------------------------------------------
 *
 * 1. A RESPOSTA É SERVIDA PELO SERVIDOR, NUNCA MONTADA POR JAVASCRIPT.
 *    O formulário é um GET para a própria página, e quem monta a resposta é o
 *    PHP. É a seção 5 do ARQUIPELAGO.md levada a sério: calculadora que calcula
 *    no navegador mostra a um modelo de linguagem um formulário vazio, nunca uma
 *    resposta. Aqui cada consulta tem a resposta inteira no HTML servido — a do
 *    modelo escolhido, a do modelo-âncora quando ninguém escolheu nada, e as 45
 *    linhas da tabela de exemplos, sempre. Sem JavaScript a ferramenta continua
 *    funcionando por completo.
 *
 * 2. AS REGRAS NÃO FORAM REESCRITAS AQUI.
 *    Os três selos, o conjunto mais estreito, o kit que responde por uma peça
 *    que o fabricante não vende avulsa e o aviso de variante de hardware vivem
 *    em ferramentas/cobertura-r1.py, a implementação de referência, que roda
 *    contra o banco sem site e sem rede. Este snippet recebe os FATOS já
 *    apurados por ela (ferramentas/gerar-r1.py grava dados/r1-respostas.json) e
 *    escreve a frase. Isso não é comodidade: escrever a regra dentro de um
 *    snippet que só roda com o site no ar é escrevê-la onde ela não pode ser
 *    conferida. ferramentas/teste-r1.php compara, modelo a modelo, o que este
 *    arquivo escreve com o que a referência escreve.
 *
 * 3. A FRASE É MONTADA AQUI, E EM PORTUGUÊS ACENTUADO.
 *    O banco desta ilha é ASCII; texto de tela sai acentuado (fase 4b do
 *    playbook). Então o que a referência entrega é informação — publicador,
 *    código, conjunto declarado, endereço, data — e o molde da frase é o mesmo
 *    nos dois lados. O que está entre aspas continua como a fonte escreveu:
 *    título de página e nome de publicador são transcrição, não texto nosso.
 *
 * 4. CONSULTA NÃO VIRA URL INDEXÁVEL.
 *    Endereço com ?modelo=… sai com noindex e canônica apontando para a página
 *    limpa. Domínio novo tem orçamento de rastreamento minúsculo (seção 14.1), e
 *    196 combinações de modelo × tipo viradas em URL fraca gastariam esse
 *    orçamento ensinando ao robô que aqui se publica coisa fina. O que precisa
 *    ser indexado — a resposta-âncora e a tabela inteira — está na página limpa.
 *
 * Regras herdadas: sem "<?php" no topo (o Code Snippets põe); nenhuma
 * superglobal de servidor; nenhum <script> nem <style> dentro do retorno do
 * shortcode (o WordPress passa os filtros do the_content sobre ele e cada
 * E-comercial vira entidade — foi o que derrubou cinco calculadoras da
 * Aquametria em 08/09/2026); toda função de nível superior dentro de
 * if ( ! function_exists() ).
 */

if ( ! defined( 'ABSPATH' ) ) {
	return;
}

if ( ! defined( 'ROBOMETRIA_R1_VERSAO' ) ) {
	define( 'ROBOMETRIA_R1_VERSAO', '1.11.1' );
	define( 'ROBOMETRIA_R1_SLUG', 'qual-peca-serve-no-meu-robo-aspirador' );
	define( 'ROBOMETRIA_R1_TITULO', 'Qual peça serve no meu robô aspirador' );
	define( 'ROBOMETRIA_R1_DADOS', 'robometria_dados_r1-respostas' );
}

/* ---------------------------------------------------------------------------
 * 1. Os dados: o que o Sync trouxe do repositório
 *
 * dados/r1-respostas.json entra no manifest com publicar=true e o Sync o grava
 * na option robometria_dados_r1-respostas (autoload desligado). É o mesmo
 * caminho que qualquer dado publicado desta ilha usa — o snippet não carrega
 * cópia do banco dentro de si, porque banco mantido em dois lugares diverge em
 * silêncio, que é exatamente o defeito que a seção 4 do contrato descreve.
 *
 * Quando a option não existe (o Sync ainda não rodou, ou rodou e o item falhou),
 * a página NÃO finge: diz que o banco não chegou e não mostra formulário. Uma
 * ferramenta que devolve vazio parecendo funcionar é pior do que uma que avisa.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_r1_dados' ) ) {
function robometria_r1_dados() {
	static $cache = null;
	if ( null !== $cache ) {
		return $cache;
	}

	$d = get_option( ROBOMETRIA_R1_DADOS );
	$d = apply_filters( 'robometria_r1_dados', $d );

	if ( ! is_array( $d ) || empty( $d['modelos'] ) || empty( $d['respostas'] ) ) {
		$cache = array();
		return $cache;
	}

	$cache = $d;
	return $cache;
}
}

/** Um modelo do banco pelo id, ou null. */
if ( ! function_exists( 'robometria_r1_modelo' ) ) {
function robometria_r1_modelo( $id ) {
	$d = robometria_r1_dados();
	if ( empty( $d['modelos'] ) ) {
		return null;
	}
	foreach ( $d['modelos'] as $m ) {
		if ( $m['id'] === $id ) {
			return $m;
		}
	}
	return null;
}
}

/** Nome da marca como ela é publicada. */
if ( ! function_exists( 'robometria_r1_marca' ) ) {
function robometria_r1_marca( $id ) {
	$d = robometria_r1_dados();
	foreach ( ( isset( $d['marcas'] ) ? $d['marcas'] : array() ) as $m ) {
		if ( $m['id'] === $id ) {
			return $m['nome'];
		}
	}
	return $id;
}
}

/** "Electrolux ERB60" — como o modelo aparece em título e em frase. */
if ( ! function_exists( 'robometria_r1_rotulo_modelo' ) ) {
function robometria_r1_rotulo_modelo( $modelo ) {
	if ( ! is_array( $modelo ) ) {
		return '';
	}
	return robometria_r1_marca( $modelo['marca'] ) . ' ' . $modelo['codigo'];
}
}

/* ---------------------------------------------------------------------------
 * 2. As peças da frase
 * ------------------------------------------------------------------------- */

/**
 * Gênero e artigo de cada tipo de peça.
 *
 * Existe porque a frase da R1 é a resposta principal da página, e "não vende
 * escova lateral avulso" é defeito visível numa ilha cujo único ativo é a
 * confiança. A tabela é a mesma da implementação de referência — foi rodando a
 * regra contra o banco, antes de ela virar PHP, que este defeito apareceu.
 */
if ( ! function_exists( 'robometria_r1_genero' ) ) {
function robometria_r1_genero( $tipo ) {
	$mapa = array(
		'filtro'           => array( 'o', 'avulso', 'ele' ),
		'escova lateral'   => array( 'a', 'avulsa', 'ela' ),
		'escova principal' => array( 'a', 'avulsa', 'ela' ),
		'mop'              => array( 'o', 'avulso', 'ele' ),
		'bateria'          => array( 'a', 'avulsa', 'ela' ),
		'reservatorio'     => array( 'o', 'avulso', 'ele' ),
	);
	return isset( $mapa[ $tipo ] ) ? $mapa[ $tipo ] : array( 'o', 'avulso', 'ele' );
}
}

/** O tipo de peça como ele vai para a tela, acentuado. */
if ( ! function_exists( 'robometria_r1_nome_do_tipo' ) ) {
function robometria_r1_nome_do_tipo( $tipo ) {
	$mapa = array( 'reservatorio' => 'reservatório' );
	return isset( $mapa[ $tipo ] ) ? $mapa[ $tipo ] : $tipo;
}
}

/** "HO041, HO400 e OB010" — a lista do jeito que se lê em voz alta. */
if ( ! function_exists( 'robometria_r1_lista' ) ) {
function robometria_r1_lista( $itens ) {
	$itens = array_values( array_filter( (array) $itens, 'strlen' ) );
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

/**
 * Como a peça é chamada na frase.
 *
 * Nem todo fabricante publica código: a Electrolux identifica várias peças só
 * pelo título e a Xiaomi pelo nome do acessório. Nesse caso a frase cita o
 * TÍTULO da fonte, entre aspas, e a página avisa que ali não há código — é a
 * mesma regra do valor nulo com motivo que vale para os números do banco.
 * Escrever "sem código publicado" no lugar do código produziria frase sem
 * sentido ("vem dentro do sem código publicado").
 */
if ( ! function_exists( 'robometria_r1_identificacao' ) ) {
function robometria_r1_identificacao( $item ) {
	if ( ! empty( $item['codigo'] ) ) {
		return array( $item['codigo'], false );
	}
	return array( '"' . $item['nome_na_fonte'] . '"', true );
}
}

/**
 * Primeira letra maiúscula, sem depender do locale do servidor.
 *
 * ucfirst() é byte a byte e estragaria a primeira letra de qualquer palavra
 * acentuada. As palavras que passam por aqui hoje são "ele" e "ela", mas a
 * função não pode ser a que quebra no dia em que passar outra.
 */
if ( ! function_exists( 'robometria_r1_maiuscula' ) ) {
function robometria_r1_maiuscula( $texto ) {
	if ( function_exists( 'mb_substr' ) ) {
		return mb_strtoupper( mb_substr( $texto, 0, 1, 'UTF-8' ), 'UTF-8' )
			. mb_substr( $texto, 1, null, 'UTF-8' );
	}
	return ucfirst( $texto );
}
}

/** Data na tela como o leitor brasileiro escreve; ISO fica no repositório. */
if ( ! function_exists( 'robometria_r1_data' ) ) {
function robometria_r1_data( $iso ) {
	$p = explode( '-', (string) $iso );
	if ( 3 !== count( $p ) ) {
		return (string) $iso;
	}
	return $p[2] . '/' . $p[1] . '/' . $p[0];
}
}

/**
 * O rótulo e a ressalva de uma origem, vindos do arquivo de dados.
 *
 * A tabela mora em ferramentas/gerar-r1.py e viaja dentro de
 * dados/r1-respostas.json, e não aqui, para a escada de fontes ter um lugar só.
 * Origem sem rótulo declarado é barrada no gerador, antes de virar página.
 */
if ( ! function_exists( 'robometria_r1_origem' ) ) {
function robometria_r1_origem( $origem ) {
	$d = robometria_r1_dados();
	$t = isset( $d['rotulos_de_origem'][ $origem ] ) ? $d['rotulos_de_origem'][ $origem ] : array();
	return array(
		isset( $t['rotulo'] ) ? $t['rotulo'] : $origem,
		isset( $t['ressalva'] ) ? $t['ressalva'] : null,
	);
}
}

/**
 * O LINK DE PROCEDÊNCIA — discreto por regra, e nunca um botão.
 *
 * Cicatriz de 10/09/2026 (seção 7 do ARQUIPELAGO.md): a R1 publicou 45 pares
 * peça × modelo em que o ÚNICO link clicável era o da loja do fabricante. Quem
 * queria comprar clicava na procedência, porque não havia outra porta — e a
 * ilha mandava a venda para a Electrolux de graça.
 *
 * A procedência FICA: é ela que dá à página o direito de afirmar compatibilidade
 * e é o que o Google e um modelo de linguagem conferem. O que muda é o peso: ela
 * existe para ser CONFERIDA, não para ser clicada. Por isso o texto é "fonte",
 * o `rel` leva `nofollow` — a ilha não passa autoridade para a loja do
 * fabricante — e nenhuma regra de CSS a transforma em botão.
 */
if ( ! function_exists( 'robometria_r1_fonte_link' ) ) {
function robometria_r1_fonte_link( $url ) {
	if ( empty( $url ) ) {
		return '';
	}
	/* A regra mora na casca desde 10/09/2026 (secao 1c dela); aqui fica so o
	   nome que esta ferramenta ja usava, para nada a montante mudar. */
	if ( function_exists( 'robometria_casca_fonte_link' ) ) {
		return robometria_casca_fonte_link( $url );
	}
	return '<a class="rbm-fonte" href="' . esc_url( $url )
		. '" target="_blank" rel="nofollow noopener">fonte</a>';
}
}

/**
 * O rótulo do botão de compra.
 *
 * Nomeia a loja para quem vai clicar: link de compra que não diz para onde leva
 * é pedido de confiança, e confiança é o único ativo desta ilha. Programa que o
 * banco ainda não declarou sai como "loja parceira" — nunca inventando o nome
 * de um marketplace que ninguém conferiu.
 */
if ( ! function_exists( 'robometria_r1_rotulo_da_loja' ) ) {
function robometria_r1_rotulo_da_loja( $programa ) {
	if ( function_exists( 'robometria_casca_rotulo_da_loja' ) ) {
		return robometria_casca_rotulo_da_loja( $programa );
	}
	$nomes = array(
		'shopee'       => 'na Shopee',
		'mercadolivre' => 'no Mercado Livre',
		'amazon'       => 'na Amazon',
	);
	return isset( $nomes[ $programa ] ) ? $nomes[ $programa ] : 'na loja parceira';
}
}

/**
 * A PORTA DE COMPRA de uma peça — presente mesmo quando o link ainda não existe.
 *
 * O lugar é RESERVADO em vez de escondido, e a diferença não é cosmética: bloco
 * que só nasce quando o link chega faz a ferramenta voltar, sozinha, ao defeito
 * de ter a procedência como única porta clicável durante todas as semanas em que
 * o cano de links está enchendo (seção 7). Reservado, o visitante vê que a
 * compra é assunto da página, e a ilha vê o buraco todo dia.
 */
if ( ! function_exists( 'robometria_r1_porta_de_compra' ) ) {
function robometria_r1_porta_de_compra( $item ) {
	if ( function_exists( 'robometria_casca_porta_de_compra' ) ) {
		return robometria_casca_porta_de_compra( $item );
	}

	/* A CÓPIA LOCAL DA ESCADA MORREU EM 14/09/2026, e o motivo é o que esta ilha
	   acabou de pagar duas vezes no mesmo dia: metade de uma regra aplicada
	   parece a regra aplicada. Esta função repetia a escada inteira para o caso
	   de a casca não estar carregada, e uma segunda cópia da mesma decisão é
	   combinar de divergir depois — foi exatamente assim que o artigo do
	   publicador ficou certo por acidente em dois arquivos e errado nos outros
	   quatro. A saída degradada diz o que é e não promete nada. */
	return '<span class="rbm-sem-saida">Saída de compra fora do ar agora</span>';
}
}

/* ---------------------------------------------------------------------------
 * 3. As frases
 *
 * O molde é o da implementação de referência, palavra por palavra — o que muda
 * é o acento e o nome legível da origem. ferramentas/teste-r1.php compara as
 * duas ignorando acento e aplicando a mesma tabela de rótulos, e reprova se
 * divergirem.
 * ------------------------------------------------------------------------- */

/**
 * Quem nomeou a FUNÇÃO desta peça — seção 26.3 do ARQUIPELAGO.md.
 *
 * O vocabulário desta ilha classifica pela função ("escova lateral" x "escova
 * principal"); o fabricante batiza pela posição ("Direita", "Central",
 * "Frontal") ou nem isso (a Xiaomi publica só "Brush"). Enquanto a página
 * escrevia "A WAP declara a escova lateral X", ela emprestava à WAP uma palavra
 * que a WAP nunca usou — e a declaração do fabricante é a única coisa que esta
 * ilha vende.
 *
 * O campo viaja como FATO em `funcao_declarada_por` (ferramentas/gerar-r1.py),
 * lido do banco: vazio nos tipos que não dependem disso, "titulo" quando o
 * fabricante escreveu a palavra, "contraste-no-catalogo" ou
 * "canal-de-manutencao" quando quem leu a função foi outra pessoa.
 */
if ( ! function_exists( 'robometria_r1_funcao_derivada' ) ) {
function robometria_r1_funcao_derivada( $item ) {
	$d = isset( $item['funcao_declarada_por'] ) ? $item['funcao_declarada_por'] : null;
	return ( null !== $d && '' !== $d && 'titulo' !== $d );
}
}

/**
 * De que lado da fronteira estão os canais que discordam desta peça:
 * 'fabricante', 'terceiro' ou 'misto'.
 *
 * O lado é LIDO do degrau que cada divergência declara (fala_pela_marca, escrito
 * no esquema e carregado pelo gerador), nunca deduzido do nome do canal — deduzir
 * do nome seria a heurística por vizinhança que a seção 8 do contrato proíbe.
 */
if ( ! function_exists( 'robometria_r1_lado_da_divergencia' ) ) {
function robometria_r1_lado_da_divergencia( $lista ) {
	$lados = array();
	foreach ( (array) $lista as $dv ) {
		$lados[ ! empty( $dv['fala_pela_marca'] ) ? 'fabricante' : 'terceiro' ] = true;
	}
	if ( 1 === count( $lados ) ) {
		return key( $lados );
	}
	return 'misto';
}
}

/**
 * A cauda de divergência da frase, com o número CONTADO e a natureza lida do degrau.
 *
 * Até 13/09/2026 esta cauda era uma frase fixa — "Dois canais do fabricante
 * discordam" — e ela era verdadeira por acidente do banco: todas as divergências
 * de peça vinham de canal de fabricante. O primeiro registro cujos canais
 * divergentes eram marketplace e varejista fez a frase emprestar a autoridade do
 * FABRICANTE a quem só revende. São duas afirmações diferentes e elas não podem
 * sair com as mesmas palavras.
 */
if ( ! function_exists( 'robometria_r1_frase_da_divergencia' ) ) {
function robometria_r1_frase_da_divergencia( $peca_id, $lista = null ) {
	/* A LISTA ENTRA PELO ARGUMENTO quando quem chama ja a tem. Não é conveniência:
	   é o que permite à bancada PRODUZIR o mundo misto, que o banco de hoje não
	   tem — e afirmação que só o banco de hoje consegue exercitar é afirmação que
	   o banco de amanhã desliga. Sem argumento, a lista sai dos dados servidos. */
	if ( null === $lista ) {
		$d    = robometria_r1_dados();
		$mapa = isset( $d['divergencias'] ) ? $d['divergencias'] : array();
		$lista = isset( $mapa[ $peca_id ] ) ? $mapa[ $peca_id ] : array();
	}
	if ( empty( $lista ) ) {
		return '';
	}
	$n     = count( $lista );
	$lado  = robometria_r1_lado_da_divergencia( $lista );
	/* +1: a declaração desta página também está publicada e datada. */
	/* O NUMERO DAS DECLARACOES SAI NO FEMININO, e isto foi medido no ar em
	   21/09/2026, na leva dos quatro filtros. `declaracoes` e palavra feminina e
	   o numeral saia da tabela masculina: com UM canal divergente — o primeiro
	   caso de n=1 que esta ilha publicou, o filtro `positivo-11206516` — a
	   pagina servia *"as dois declaracoes estao publicadas"*. Com dois ou mais
	   canais ninguem podia ver, porque a partir do tres o numeral nao flexiona.
	   E a mesma familia do artigo do publicador, consertado em 14/09/2026: a
	   frase e montada e por isso a concordancia tambem e trabalho da montagem. */
	$total   = robometria_r1_strtolower( robometria_r1_numeral( $n + 1, true ) );
	$canal   = ( 1 === $n ) ? 'canal' : 'canais';
	$declara = ( 1 === $n ) ? 'declara' : 'declaram';

	if ( 'fabricante' === $lado ) {
		return sprintf(
			'%1$s %2$s do fabricante %3$s alcance diferente para esta peça: vale o conjunto MAIS ESTREITO, e as %4$s declarações estão publicadas com as suas datas.',
			robometria_r1_numeral( $n ), $canal, $declara, $total
		);
	}
	if ( 'terceiro' === $lado ) {
		return sprintf(
			'%1$s %2$s de fora do fabricante %3$s para esta peça um alcance que o fabricante não declara: quem decide aqui é o fabricante, e as %4$s declarações estão publicadas com o nome de cada canal e a sua data.',
			robometria_r1_numeral( $n ), $canal, $declara, $total
		);
	}
	return sprintf(
		'%1$s canais declaram alcances diferentes para esta peça, e parte deles está fora do fabricante: vale o conjunto MAIS ESTREITO, e as %2$s declarações estão publicadas com o nome de cada canal e a sua data.',
		robometria_r1_numeral( $n ), $total
	);
}
}

/**
 * O número da frase sai contado e por extenso; acima de dez, em algarismo.
 *
 * `$feminino` existe porque só DOIS números do português flexionam em gênero —
 * um/uma e dois/duas —, e é exatamente por isso que o defeito de 21/09/2026
 * ficou invisível: toda frase desta ilha com três ou mais canais saía certa, e
 * a errada só apareceu no dia em que um registro entrou com UM canal
 * divergente. Quem chamar esta função para contar substantivo feminino passa
 * `true`; o padrão continua o masculino, que é o que as outras chamadas usam
 * ("Um canal", "Dois canais").
 */
if ( ! function_exists( 'robometria_r1_numeral' ) ) {
function robometria_r1_numeral( $n, $feminino = false ) {
	$mapa = array( 1 => 'Um', 2 => 'Dois', 3 => 'Três', 4 => 'Quatro', 5 => 'Cinco',
		6 => 'Seis', 7 => 'Sete', 8 => 'Oito', 9 => 'Nove', 10 => 'Dez' );
	if ( $feminino ) {
		$mapa[1] = 'Uma';
		$mapa[2] = 'Duas';
	}
	return isset( $mapa[ $n ] ) ? $mapa[ $n ] : (string) $n;
}
}

/**
 * Minúscula que não estraga acento — mb_strtolower quando existe, e a tabela das
 * iniciais que esta função de fato encontra quando não existe.
 */
if ( ! function_exists( 'robometria_r1_strtolower' ) ) {
function robometria_r1_strtolower( $texto ) {
	if ( function_exists( 'mb_strtolower' ) ) {
		return mb_strtolower( $texto, 'UTF-8' );
	}
	return strtr( $texto, array( 'T' => 't', 'U' => 'u', 'D' => 'd', 'Q' => 'q',
		'C' => 'c', 'S' => 's', 'O' => 'o', 'N' => 'n' ) );
}
}

/**
 * A ressalva que devolve a função a quem a leu. Vazia quando a função veio do
 * título — ali o fabricante escreveu a palavra, e a frase pode atribuí-la a ele.
 *
 * A ressalva diz só o que vale para TODOS os casos que ela cobre: "o título não
 * nomeia a função". A primeira versão dizia "o título nomeia a posição, não a
 * função" — verdade na WAP ("Escova Direita") e falsa na Xiaomi, cujo título é
 * só "Brush". Afirmação em bloco tem o escopo do que foi medido (seção 8).
 */
if ( ! function_exists( 'robometria_r1_ressalva_da_funcao' ) ) {
function robometria_r1_ressalva_da_funcao( $item, $tipo ) {
	if ( ! robometria_r1_funcao_derivada( $item ) ) {
		return '';
	}
	$ressalvas = array(
		'contraste-no-catalogo' => 'Quem chama esta peça de %s é a Robometria, pelo contraste do catálogo do próprio fabricante: o título dela não nomeia a função.',
		'canal-de-manutencao'   => 'Quem chama esta peça de %s é o próprio fabricante, no canal de manutenção dele: o título da peça não nomeia a função.',
	);
	$d = $item['funcao_declarada_por'];
	/* Origem de função que chegue sem ressalva escrita não sai calada: a página
	   diria a função sem dizer quem a leu, que é o defeito inteiro de volta. O
	   gerador já para antes disso (cobertura-r1.py), e aqui a página avisa em
	   vez de publicar a atribuição por omissão. */
	if ( ! isset( $ressalvas[ $d ] ) ) {
		return sprintf(
			'A função desta peça foi lida em %s, e ainda não temos a frase que explica esse caminho — confira na fonte antes de comprar.',
			$d
		);
	}
	return sprintf( $ressalvas[ $d ], $tipo );
}
}

/**
 * QUEM PUBLICA, COM O ARTIGO QUE O BANCO DECLARA — e nunca com o que o nome
 * sugere (14/09/2026).
 *
 * Até hoje o "A " que abre a frase e o "que a " do meio dela eram DIGITADOS, em
 * quatro moldes e no cartão da vitrine, e o verbo era sempre singular. Estava
 * certo por acidente do banco: todo publicador que chega a essas frases é
 * feminino singular. O mesmo banco já tem os dois contraexemplos — "Mundo
 * Conectado", que é masculino e que a R2 já escrevia com "o" por uma segunda
 * tabela digitada, e "Lojas WAP", que é PLURAL e que nenhuma frase cita ainda.
 *
 * O artigo, a maiúscula de começo de frase e o número do verbo viajam como FATO
 * em `gramatica_do_publicador` (ferramentas/gerar-r1.py), derivados de
 * `dados/publicadores.json` e da tabela `artigos_de_publicador` do esquema.
 * Nenhuma tabela de língua mora aqui: snippet que decide concordância é a mesma
 * família do mapa de nomes duplicado que a casca 1.2.0 pagou.
 *
 * A FALTA É EXPLÍCITA em vez de silenciosa: item sem a gramática cai no nome sem
 * artigo nenhum ("Electrolux declara…"), que lê estranho e é visível, em vez de
 * publicar a concordância errada com cara de frase pronta. O gerador já para
 * antes disso; isto é a rede de baixo.
 */
if ( ! function_exists( 'robometria_r1_gramatica' ) ) {
function robometria_r1_gramatica( $fonte ) {
	$g = isset( $fonte['gramatica_do_publicador'] ) ? $fonte['gramatica_do_publicador'] : array();
	return array(
		'artigo'    => isset( $g['artigo'] ) ? $g['artigo'] : '',
		'maiuscula' => isset( $g['maiuscula'] ) ? $g['maiuscula'] : '',
		'numero'    => isset( $g['numero'] ) ? $g['numero'] : 'singular',
	);
}
}

/** "a Electrolux (loja oficial)", "o Mundo Conectado", "as Lojas WAP". */
if ( ! function_exists( 'robometria_r1_quem_publica' ) ) {
function robometria_r1_quem_publica( $fonte ) {
	$g = robometria_r1_gramatica( $fonte );
	return trim( $g['artigo'] . ' ' . $fonte['publicador'] );
}
}

/** O mesmo, abrindo frase. A maiúscula vem do esquema: "as" vira "As". */
if ( ! function_exists( 'robometria_r1_quem_publica_maiusculo' ) ) {
function robometria_r1_quem_publica_maiusculo( $fonte ) {
	$g = robometria_r1_gramatica( $fonte );
	return trim( $g['maiuscula'] . ' ' . $fonte['publicador'] );
}
}

/** "declara" ou "declaram", pelo número DECLARADO de quem publica. */
if ( ! function_exists( 'robometria_r1_verbo' ) ) {
function robometria_r1_verbo( $fonte, $singular, $plural ) {
	$g = robometria_r1_gramatica( $fonte );
	return ( 'plural' === $g['numero'] ) ? $plural : $singular;
}
}

/**
 * A ORAÇÃO EM QUE ESTE ITEM ATRIBUI A COMPATIBILIDADE — e o nome dela é a
 * fronteira (14/09/2026).
 *
 * Ela sempre esteve aqui, como as quatro primeiras linhas de
 * robometria_r1_frase(); o que não existia era um NOME para ela. Sem nome, uma
 * régua que quisesse medir "a quem este item atribui" só podia medir a frase
 * inteira — e a frase inteira carrega a cauda da divergência, que fala do
 * fabricante com toda a razão ("Um canal do fabricante declara alcance
 * diferente"). Medir as duas juntas dá falso positivo, e foi exatamente o que
 * aconteceu ao escrever a seção 17 do teste: a régua reprovou a cauda certa.
 *
 * A saída é a mesma que a tabela de exemplos da R1 aprendeu em 13/09, quando os
 * conferidores delimitavam "a resposta" pela primeira coisa parecida com uma
 * tabela: **fronteira de teste é marcador escrito, nunca "a primeira coisa
 * parecida com".** Aqui o marcador é esta função.
 */
if ( ! function_exists( 'robometria_r1_atribuicao_do_item' ) ) {
function robometria_r1_atribuicao_do_item( $item ) {
	list( $identificacao, $sem_codigo ) = robometria_r1_identificacao( $item );
	list( $rotulo_origem )              = robometria_r1_origem( $item['origem'] );

	$lista = robometria_r1_lista( $item['declarados'] );
	$data  = robometria_r1_data( $item['verificado_em'] );
	$tipo  = robometria_r1_nome_do_tipo( $item['tipo'] );

	/* O ARTIGO E O NÚMERO DE QUEM PUBLICA SAEM DO BANCO (14/09/2026). Ver
	   robometria_r1_quem_publica() logo acima para o porquê inteiro. */
	$quem           = robometria_r1_quem_publica( $item );
	$quem_maiusculo = robometria_r1_quem_publica_maiusculo( $item );
	$declara        = robometria_r1_verbo( $item, 'declara', 'declaram' );

	if ( ! empty( $item['dentro_de_kit'] ) && ! empty( $item['existe_avulso'] ) ) {
		/* Existe a peça avulsa para este modelo: o kit é um caminho A MAIS, e
		   dizer "não vende avulso" seria negar, na mesma tela, a peça que a
		   frase anterior acabou de mostrar. A contradição só apareceu lendo a
		   resposta inteira como um leitor lê — verificação por regra objetiva
		   não pega defeito de julgamento.

		   E ela NOMEIA O TIPO, nunca um pronome: escrita como "Ele também vem
		   dentro do kit…", só lia certo enquanto a peça avulsa do mesmo tipo
		   caísse logo antes por ordem do banco. Ver o porquê inteiro em
		   ferramentas/cobertura-r1.py, frase_declarada(). */
		list( $artigo, $avulso, $pronome ) = robometria_r1_genero( $item['tipo'] );
		$frase = sprintf(
			'%1$s %2$s também vem dentro do kit %3$s, que %4$s %5$s compatível com %6$s (%7$s, verificado em %8$s).',
			robometria_r1_maiuscula( $artigo ), $tipo, $identificacao, $quem, $declara,
			$lista, $rotulo_origem, $data
		);
	} elseif ( ! empty( $item['dentro_de_kit'] ) ) {
		list( $artigo, $avulso, $pronome ) = robometria_r1_genero( $item['tipo'] );
		$frase = sprintf(
			/* "que o fabricante declara" era DIGITADO aqui, e a mesma frase
			   já abria com o publicador certo — "A Electrolux (loja oficial)
			   não vende…". Ver robometria_r1_vitrine() para o porquê inteiro:
			   falar pela marca não é ser a marca. */
			'%1$s não %2$s %3$s %4$s %5$s para este modelo: %6$s vem dentro do kit %7$s, que %8$s %9$s compatível com %10$s (%11$s, verificado em %12$s).',
			$quem_maiusculo, robometria_r1_verbo( $item, 'vende', 'vendem' ),
			$artigo, $tipo, $avulso, $pronome,
			$identificacao, $quem, $declara, $lista, $rotulo_origem, $data
		);
	} elseif ( ! robometria_r1_funcao_derivada( $item ) ) {
		/* O fabricante escreveu a palavra do eixo no título ("Escova Lateral",
		   "Side Brush", "Escova Central"), ou o tipo nem depende disso (filtro,
		   mop, bateria, reservatório). Só aqui a frase pode dizer que ele
		   DECLARA o tipo: é o que ele fez. */
		list( $artigo ) = robometria_r1_genero( $item['tipo'] );
		$frase = sprintf(
			'%1$s %2$s %3$s %4$s %5$s compatível com %6$s (%7$s, verificado em %8$s).',
			$quem_maiusculo, $declara, $artigo, $tipo, $identificacao,
			$lista, $rotulo_origem, $data
		);
	} else {
		/* A FUNÇÃO NÃO VEIO DO TÍTULO (seção 26.3 do ARQUIPELAGO.md). O
		   fabricante declarou duas coisas — o nome da peça e a compatibilidade
		   dela — e a frase diz exatamente essas duas. O tipo abre a frase, para
		   o leitor continuar sabendo de que peça se fala na primeira oração,
		   mas fora do escopo do verbo "declara". Quem nomeou a função vai na
		   ressalva logo abaixo. */
		$frase = sprintf(
			'%1$s: %2$s, que %3$s %4$s compatível com %5$s (%6$s, verificado em %7$s).',
			robometria_r1_maiuscula( $tipo ), $identificacao, $quem, $declara,
			$lista, $rotulo_origem, $data
		);
	}

	return $frase;
}
}

if ( ! function_exists( 'robometria_r1_frase' ) ) {
function robometria_r1_frase( $item ) {
	list( , $sem_codigo ) = robometria_r1_identificacao( $item );
	$tipo  = robometria_r1_nome_do_tipo( $item['tipo'] );
	$frase = robometria_r1_atribuicao_do_item( $item );

	/* A RESSALVA VEM ANTES DAS OUTRAS CAUDAS porque ela qualifica a afirmação
	   principal — quem leu a função —, enquanto as de baixo qualificam detalhes
	   do registro (sem código publicado, canais que discordam, variante). */
	$ressalva = robometria_r1_ressalva_da_funcao( $item, $tipo );
	if ( '' !== $ressalva ) {
		$frase .= ' ' . $ressalva;
	}

	if ( $sem_codigo ) {
		$frase .= ' Este fabricante não publica código de peça nesta página: identifique o item pelo título e pela lista de modelos.';
	}
	if ( ! empty( $item['divergencia'] ) ) {
		$frase .= ' ' . robometria_r1_frase_da_divergencia( $item['peca'] );
	}
	if ( ! empty( $item['variante_do_par'] ) ) {
		$frase .= sprintf( ' Vale para a versão %s deste modelo.', $item['variante_do_par'] );
	}

	return $frase;
}
}

/**
 * O kit que serve o modelo e cuja composição a coleta ainda não transcreveu.
 *
 * A R1 sabe QUE o kit serve e não sabe dizer O QUE vem dentro. Esconder isso
 * seria pior do que mostrar: a ferramenta mostra o kit e diz o que ainda não
 * sabe. Afirmar que o filtro está lá dentro, sem a lista, seria supor.
 */
if ( ! function_exists( 'robometria_r1_frase_kit' ) ) {
function robometria_r1_frase_kit( $kit ) {
	list( $rotulo_origem ) = robometria_r1_origem( $kit['origem'] );
	return sprintf(
		'%1$s %2$s o %3$s compatível com este modelo (%4$s, verificado em %5$s), mas não transcrevemos ainda a lista do que vem dentro — então não afirmamos qual peça o kit cobre.',
		robometria_r1_quem_publica_maiusculo( $kit ),
		robometria_r1_verbo( $kit, 'declara', 'declaram' ),
		$kit['nome_na_fonte'], $rotulo_origem,
		robometria_r1_data( $kit['verificado_em'] )
	);
}
}

/** Selo nao_declarada. O texto é explícito de propósito: silêncio parece defeito. */
if ( ! function_exists( 'robometria_r1_frase_recusa' ) ) {
function robometria_r1_frase_recusa( $tipo ) {
	return sprintf(
		'Não localizamos declaração do fabricante de %s para este modelo; não vamos supor.',
		robometria_r1_nome_do_tipo( $tipo )
	);
}
}

/** Quando o mesmo código de modelo tem revisões com peças diferentes. */
if ( ! function_exists( 'robometria_r1_frase_variante' ) ) {
function robometria_r1_frase_variante( $aviso ) {
	if ( empty( $aviso['rotulos'] ) || count( $aviso['rotulos'] ) < 2 ) {
		return '';
	}
	/* Dois pontos, e não ponto final, antes do que o fabricante escreveu: o
	   texto do banco começa em minúscula, e depois de ponto final ele sairia
	   como frase começando em minúscula na tela. */
	$o_que_muda = rtrim( implode( '; ', (array) $aviso['o_que_muda'] ), '.' );
	return sprintf(
		'Este modelo tem mais de uma versão de hardware conhecida (%s), e a peça certa depende da sua: %s. Confira a etiqueta do aparelho antes de comprar.',
		robometria_r1_lista( $aviso['rotulos'] ), $o_que_muda
	);
}
}

/* ---------------------------------------------------------------------------
 * 4. A entrada
 *
 * Lista fechada nos dois campos, sempre. Texto livre é proibido na entrada de
 * modelo (seção 1.2 da especificação): o corpus já mostrou anúncio de "escova
 * lateral V3 V5 A4 A6" sem marca no título, e campo livre faria a ferramenta
 * adivinhar de qual fabricante é o "V3". Adivinhar compatibilidade é o defeito
 * que esta ilha existe para não cometer.
 *
 * A leitura passa por um filtro para ferramentas/teste-r1.php poder montar
 * qualquer consulta sem site e sem navegador.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_r1_entrada' ) ) {
function robometria_r1_entrada() {
	$bruto = array(
		'modelo' => filter_input( INPUT_GET, 'modelo', FILTER_DEFAULT ),
		'peca'   => filter_input( INPUT_GET, 'peca', FILTER_DEFAULT ),
	);
	$bruto = apply_filters( 'robometria_r1_entrada', $bruto );

	$d      = robometria_r1_dados();
	$modelo = '';
	$peca   = '';

	$pedido = isset( $bruto['modelo'] ) ? (string) $bruto['modelo'] : '';
	if ( '' !== $pedido && robometria_r1_modelo( $pedido ) ) {
		$modelo = $pedido;
	}

	$tipos  = isset( $d['tipos'] ) ? (array) $d['tipos'] : array();
	$pedido = isset( $bruto['peca'] ) ? (string) $bruto['peca'] : '';
	if ( '' !== $pedido && in_array( $pedido, $tipos, true ) ) {
		$peca = $pedido;
	}

	return array( 'modelo' => $modelo, 'peca' => $peca );
}
}

/** Houve consulta de verdade? É o que decide o noindex e a rolagem. */
if ( ! function_exists( 'robometria_r1_houve_consulta' ) ) {
function robometria_r1_houve_consulta() {
	$e = robometria_r1_entrada();
	return ( '' !== $e['modelo'] || '' !== $e['peca'] );
}
}

/* ---------------------------------------------------------------------------
 * 5. A resposta em HTML
 * ------------------------------------------------------------------------- */

/** Itens de um modelo, filtrados pelo tipo pedido (vazio = todos). */
if ( ! function_exists( 'robometria_r1_itens' ) ) {
function robometria_r1_itens( $lista, $tipo ) {
	if ( '' === $tipo ) {
		return $lista;
	}
	$saida = array();
	foreach ( (array) $lista as $i ) {
		if ( $i['tipo'] === $tipo ) {
			$saida[] = $i;
		}
	}
	return $saida;
}
}

/**
 * A VITRINE, que desde 10/09/2026 é o BLOCO DE COMPRA (seções 6 e 7).
 *
 * Carrossel de cartões dentro do resultado, com scroll-snap em CSS puro, sem
 * biblioteca. Cada cartão diz a especificação que fez a peça entrar — que aqui
 * é a própria declaração do fabricante — e é um link de verdade, nunca um
 * <div> com onclick.
 *
 * A MUDANÇA DO DESPACHO: o cartão tinha um único link, e ele ia para a loja do
 * fabricante. Agora a ordem dentro do cartão é a da seção 7 — primeiro a porta
 * de compra (afiliado, ou o lugar reservado enquanto o link não existe), depois
 * a procedência, discreta, com o texto "fonte" e `nofollow`. Comprar e conferir
 * são duas ações diferentes, e a página parou de misturá-las num link só.
 *
 * Três honestidades que a seção 6 e a seção 7 obrigam, e que hoje valem para
 * TODOS os itens desta ilha:
 *   - peça sem imagem NÃO some: aparece com espaço reservado neutro e o código
 *     em destaque. Perder a peça certa por falta de foto é trocar o certo pelo
 *     bonito;
 *   - peça sem ficha de produto NÃO fica sem saída: o bloco de compra desce a
 *     escada da 25.1 e serve a busca. Sumir com o bloco devolveria a procedência
 *     ao papel de única porta clicável; reservá-lo com uma promessa, que foi o
 *     que esta ilha fez até 14/09/2026, é a mesma coisa com educação;
 *   - o número de peças esperando link sai NA TELA, porque é trabalho pendente
 *     de verdade e não estatística interna.
 */
if ( ! function_exists( 'robometria_r1_vitrine' ) ) {
function robometria_r1_vitrine( $itens, $modelo ) {
	if ( ! $itens ) {
		return '';
	}

	/* Um cartão por PEÇA, não por par: o Kit Performance responde filtro, mop e
	   escova lateral do mesmo modelo, e três cartões idênticos do mesmo produto
	   seriam três vezes o mesmo conselho. O cartão diz todos os tipos que aquela
	   peça cobre. */
	$por_peca = array();
	foreach ( $itens as $i ) {
		if ( ! isset( $por_peca[ $i['peca'] ] ) ) {
			$por_peca[ $i['peca'] ]          = $i;
			$por_peca[ $i['peca'] ]['tipos'] = array();
		}
		$por_peca[ $i['peca'] ]['tipos'][] = $i['tipo'];
	}

	/* O QUE ESTAS PEÇAS TÊM DE PORTA DE COMPRA. Contado no que está na tela
	   agora, não no banco inteiro: a frase fala do que o visitante está vendo.

	   ATÉ 18/09/2026 ESTA CONTA OLHAVA `afiliado.url` — a FICHA — e chamava de
	   "sem link de loja" todo item que não tivesse ficha. Só que o botão vem da
	   escada da 25.2, cujo piso é a BUSCA, e a busca estava lá: em 66 dos 95
	   itens publicáveis a página negava um botão que ela mesma servia logo
	   abaixo, com link de afiliado vivo. Item 3 do despacho da Sentinela de
	   18/09/2026, medido no HTML servido em duas entradas reais.

	   Agora quem decide é a MESMA função que monta o botão. São duas contas
	   diferentes porque são dois fatos diferentes, e misturá-los foi o defeito:
	   `$sem_porta` é ausência de botão (defeito da 25.2, que o banco não produz)
	   e `$so_busca` é botão que abre a busca da loja em vez da ficha do produto
	   — que não é ausência nenhuma, e o leitor merece saber qual dos dois é. */
	$total_pecas = count( $por_peca );
	$sabe_a_porta = function_exists( 'robometria_casca_degrau_da_porta' );
	$sem_porta    = 0;
	$so_busca     = 0;
	if ( $sabe_a_porta ) {
		foreach ( $por_peca as $i ) {
			$degrau = robometria_casca_degrau_da_porta( $i );
			if ( 'sem_saida' === $degrau ) {
				$sem_porta++;
			} elseif ( 'ficha' !== $degrau ) {
				$so_busca++;
			}
		}
	}

	$html  = '<div class="rbm-secao rbm-compra"><h3>Onde comprar estas peças</h3>';

	/* AVISO DE COMISSÃO VISÍVEL NA PÁGINA (seção 7), e no bloco de compra — não
	   só no rodapé. Quem vê o botão precisa ver o aviso sem rolar. */
	/* "decidida pela declaração do fabricante" era a mesma atribuição digitada,
	   e na frase que justifica a ORDEM comercial da lista — o lugar mais caro
	   da página para emprestar autoridade. O critério verdadeiro é a declaração
	   de compatibilidade publicada na fonte de cada peça, seja ela o fabricante
	   ou a loja oficial dele. */
	$html .= '<p class="rbm-aviso-comissao">Os botões de compra abaixo são links de afiliado: se você comprar por eles, a Robometria pode receber comissão, sem custo a mais para você. Isso não muda a ordem da lista — ela é decidida pela declaração de compatibilidade publicada na fonte de cada peça, e só por ela. '
		. ( function_exists( 'robometria_casca_link_html' )
			? robometria_casca_link_html( 'divulgacao-de-afiliados', 'Como isto funciona' )
			: 'Veja a página de divulgação de afiliados' ) . '.</p>';

	if ( $sem_porta > 0 ) {
		/* Três moldes, porque "3 destas 3 peças" é o tipo de frase que só nasce
		   de contador solto e denuncia texto montado por máquina. */
		if ( $sem_porta === $total_pecas ) {
			$quantas = sprintf(
				1 === $total_pecas
					? 'Esta peça ainda não tem link de loja'
					: 'Nenhuma destas %d peças tem link de loja ainda',
				$total_pecas
			);
		} elseif ( 1 === $sem_porta ) {
			$quantas = sprintf( 'Uma destas %d peças ainda não tem link de loja', $total_pecas );
		} else {
			$quantas = sprintf( '%d destas %d peças ainda não têm link de loja', $sem_porta, $total_pecas );
		}

		$html .= '<p class="rbm-nota">' . esc_html( $quantas )
			. esc_html( ', e o cartão diz isso em vez de fazer o bloco sumir. Enquanto o link não existe, o endereço da declaração continua aqui — embaixo de cada cartão, como "fonte", para você conferir.' )
			. '</p>';
	}

	/* A FRASE QUE SUBSTITUI A FALSA, e ela diz o que é verdade: o botão existe e
	   abre a BUSCA da loja, não a ficha daquela peça. É informação de compra —
	   quem vai clicar sabe se cai numa página de produto ou numa vitrine filtrada
	   — e é o contrário de uma promessa, que é o que a seção 7 proíbe. */
	if ( $so_busca > 0 ) {
		if ( $so_busca === $total_pecas ) {
			$busca_frase = ( 1 === $total_pecas )
				? 'O botão desta peça abre a busca da loja, já filtrada, e não a ficha de um produto'
				: sprintf( 'Os botões destas %d peças abrem a busca da loja, já filtrada, e não a ficha de um produto', $total_pecas );
		} elseif ( 1 === $so_busca ) {
			$busca_frase = sprintf( 'Uma destas %d peças abre a busca da loja, já filtrada, em vez da ficha de um produto', $total_pecas );
		} else {
			$busca_frase = sprintf( '%d destas %d peças abrem a busca da loja, já filtrada, em vez da ficha de um produto', $so_busca, $total_pecas );
		}
		$html .= '<p class="rbm-nota">' . esc_html( $busca_frase )
			. esc_html( '. A busca não esgota e não sai do ar, e é por isso que ela é o piso: preferimos a vitrine certa a um link de produto que morre em doze horas.' )
			. '</p>';
	}

	$html .= '<ul class="rbm-vitrine">';

	foreach ( $por_peca as $i ) {
		$tipos_do_cartao = array_map( 'robometria_r1_nome_do_tipo', array_unique( $i['tipos'] ) );

		list( $identificacao, $sem_codigo ) = robometria_r1_identificacao( $i );
		list( $rotulo_origem, $ressalva )   = robometria_r1_origem( $i['origem'] );

		$html .= '<li class="rbm-vitrine-item">';

		/* Espaço reservado neutro, e nunca uma foto de banco de imagem: a peça
		   não tem foto e a página não finge que tem.

		   O PAINEL DIZ O QUE É, e esse é o conserto de 16/09/2026. Este
		   comentário prometia "o mesmo encaixe da marca, em traço" e o que foi
		   ao ar era um anel com um quarto faltando — a forma universal do
		   carregamento. Quem chegava na página não lia "sem foto", lia "a foto
		   está carregando" e, como ela nunca carrega, "este site está
		   quebrado". Hoje o painel escreve "sem foto", pela regra de
		   `.rbm-vitrine-vazia` em `robometria_casca_css_vitrine()`. */
		/* O painel sai da CASCA desde 16/09/2026 — uma decisao, quatro
		   ferramentas. Ver robometria_casca_painel_da_foto(). */
		$html .= robometria_casca_painel_da_foto( isset( $i['imagem'] ) ? $i['imagem'] : null );

		$html .= '<span class="rbm-vitrine-tipo">' . esc_html( robometria_r1_lista( $tipos_do_cartao ) ) . '</span>';
		$html .= '<span class="rbm-codigo-peca">'
			. esc_html( $sem_codigo ? 'sem código publicado' : $i['codigo'] ) . '</span>';
		$html .= '<span class="rbm-vitrine-nome">' . esc_html( $i['nome_na_fonte'] ) . '</span>';

		/* A especificação que fez a peça entrar, com o modelo consultado dentro
		   da frase — é o que a seção 6 pede do cartão.

		   QUEM DECLARA É O PUBLICADOR, LIDO DO ITEM (14/09/2026). Até aqui o
		   cartão escrevia "o fabricante declara", digitado, para QUALQUER
		   degrau — e 52 dos 73 itens deste banco vêm do degrau 4, cujo
		   publicador é a loja oficial da marca. A página se atribuía duas
		   coisas diferentes na mesma tela: a frase da resposta dizia "A
		   Electrolux (loja oficial) declara o filtro…" e o cartão da MESMA
		   peça, três linhas abaixo, dizia "o fabricante declara esta peça".

		   O degrau 4 tem `fala_pela_marca` verdadeiro, e é por isso que o item
		   fica do lado do fabricante na divisão da página — mas a escada de
		   fontes decidiu, com todas as letras, que a ATRIBUIÇÃO dele é "pela
		   loja oficial da marca", "porque quem transcreveu foi a loja".
		   **Falar pela marca não é ser a marca**: o rótulo do LADO não serve
		   de sujeito para a frase de UM item. É a mesma cicatriz da cauda de
		   divergência de 13/09, e a mesma do artigo A2 de 12/09. */
		$html .= '<span class="rbm-vitrine-porque">' . esc_html( sprintf(
			$i['dentro_de_kit']
				? '%3$s %4$s este kit compatível com o seu %1$s, e é dentro dele que vem %2$s'
				: '%3$s %4$s esta peça (%2$s) compatível com o seu %1$s',
			robometria_r1_rotulo_modelo( $modelo ),
			robometria_r1_lista( $tipos_do_cartao ),
			robometria_r1_quem_publica( $i ),
			robometria_r1_verbo( $i, 'declara', 'declaram' )
		) ) . '</span>';

		if ( ! empty( $i['vida_util'] ) && null !== $i['vida_util']['valor'] ) {
			$html .= '<span class="rbm-vitrine-vida">vida útil declarada: <span class="rbm-num">'
				. esc_html( $i['vida_util']['valor'] ) . '</span> '
				. esc_html( $i['vida_util']['unidade'] ) . '</span>';
		}

		if ( $ressalva ) {
			$html .= '<span class="rbm-tag">' . esc_html( $ressalva ) . '</span>';
		}

		/* PRIMEIRO A PORTA DE COMPRA. A ordem destes dois <span> é a regra da
		   seção 7 escrita em código: inverter os dois é reabrir o defeito. */
		$html .= '<span class="rbm-vitrine-acao">' . robometria_r1_porta_de_compra( $i ) . '</span>';

		/* DEPOIS A PROCEDÊNCIA, discreta. O rótulo da origem entra depois do
		   travessão, e não regido por preposição: "no loja oficial da marca" é
		   erro de concordância que nasceria de colar rótulo em preposição fixa. */
		$html .= '<span class="rbm-vitrine-fonte">'
			. esc_html( 'Como sabemos — ' . $rotulo_origem )
			. ( empty( $i['url'] ) ? '' : ' · ' . robometria_r1_fonte_link( $i['url'] ) )
			. '</span>';

		$html .= '</li>';
	}

	$html .= '</ul></div>';
	return $html;
}
}

/**
 * As duas declarações que discordam, com as duas datas (seção 1.4).
 *
 * Vão inteiras para a tela: a regra do conjunto mais estreito só é verificável
 * pelo leitor se ele puder ver o que foi descartado, por quem foi publicado e
 * quando. Publicar a regra sem o descarte seria pedir confiança em vez de
 * oferecer prova.
 */
if ( ! function_exists( 'robometria_r1_divergencias' ) ) {
function robometria_r1_divergencias( $itens ) {
	$d     = robometria_r1_dados();
	$mapa  = isset( $d['divergencias'] ) ? $d['divergencias'] : array();
	$html  = '';
	$vistas = array();

	foreach ( (array) $itens as $i ) {
		if ( empty( $i['divergencia'] ) || isset( $vistas[ $i['peca'] ] ) || empty( $mapa[ $i['peca'] ] ) ) {
			continue;
		}
		$vistas[ $i['peca'] ] = true;

		list( $identificacao ) = robometria_r1_identificacao( $i );
		/* O TÍTULO DO BLOCO SEGUE O MESMO DEGRAU DA FRASE. Ele dizia "os canais do
		   fabricante" para qualquer divergência, e num registro cujos canais
		   divergentes são marketplace e varejista isso é atribuir ao fabricante o
		   que ele não disse — no título, que é a linha mais lida do bloco. */
		$lado = robometria_r1_lado_da_divergencia( $mapa[ $i['peca'] ] );
		if ( 'fabricante' === $lado ) {
			$titulo = 'O que os canais do fabricante discordam sobre ';
			$regra  = 'Vale o conjunto mais estreito. Errar para o lado largo faria você comprar uma peça que não encaixa — e é essa assimetria, não a média, que decide a direção.';
		} elseif ( 'terceiro' === $lado ) {
			$titulo = 'O que canais de fora do fabricante declaram sobre ';
			$regra  = 'Nenhuma destas declarações é do fabricante: quem decide aqui é ele, e o que vale nesta página é o conjunto que ele declarou. Elas estão publicadas porque a regra do conjunto mais estreito só é verificável por quem enxerga o que foi descartado — errar para o lado largo faria você comprar uma peça que não encaixa.';
		} else {
			$titulo = 'O que os canais declaram sobre ';
			$regra  = 'Vale o conjunto mais estreito, e parte destas declarações não é do fabricante. Errar para o lado largo faria você comprar uma peça que não encaixa — e é essa assimetria, não a média, que decide a direção.';
		}
		$html .= '<div class="rbm-secao"><h3>' . esc_html( $titulo . $identificacao ) . '</h3>';
		$html .= '<p>' . esc_html( $regra ) . '</p>';
		$html .= '<div class="rbm-tabela"><table class="rbm-quadro"><thead><tr><th>Canal</th><th>Modelos que ele declara</th><th>Verificado em</th></tr></thead><tbody>';
		foreach ( $mapa[ $i['peca'] ] as $dv ) {
			$html .= '<tr>';
			/* O nome do canal é o DADO da linha e sai como texto; o endereço vai
			   junto como "fonte", discreto e com nofollow (seção 7). */
			$html .= '<td>' . esc_html( $dv['canal'] )
				. ( empty( $dv['url'] ) ? '' : ' ' . robometria_r1_fonte_link( $dv['url'] ) ) . '</td>';
			$html .= '<td>' . esc_html( robometria_r1_lista( $dv['conjunto'] ) ) . '</td>';
			$html .= '<td class="rbm-n">' . esc_html( robometria_r1_data( $dv['verificado_em'] ) ) . '</td>';
			$html .= '</tr>';
		}
		$html .= '</tbody></table></div></div>';
	}

	return $html;
}
}

/**
 * A resposta inteira de um modelo.
 *
 * Ordem da tela, e ela é a da seção 7 do ARQUIPELAGO.md: primeiro o que o
 * fabricante declara; depois, em bloco SEPARADO e rotulado, o que só terceiro
 * declara; depois o kit cuja composição não foi transcrita; e por último a
 * recusa, tipo a tipo. Declaração de terceiro nunca aparece misturada e nunca
 * em primeiro lugar.
 */
if ( ! function_exists( 'robometria_r1_resposta' ) ) {
function robometria_r1_resposta( $modelo_id, $tipo, $e_ancora = false ) {
	$d       = robometria_r1_dados();
	$modelo  = robometria_r1_modelo( $modelo_id );
	$resp    = isset( $d['respostas'][ $modelo_id ] ) ? $d['respostas'][ $modelo_id ] : null;
	if ( ! $modelo || ! $resp ) {
		return '';
	}

	$rotulo     = robometria_r1_rotulo_modelo( $modelo );
	$fabricante = robometria_r1_itens( $resp['fabricante'], $tipo );
	$terceiro   = robometria_r1_itens( $resp['terceiro'], $tipo );
	$tipos      = ( '' === $tipo ) ? (array) $d['tipos'] : array( $tipo );

	$respondidos = array();
	foreach ( $fabricante as $i ) {
		$respondidos[ $i['tipo'] ] = true;
	}

	$html = '<div class="rbm-resposta" id="resultado">';

	if ( $e_ancora ) {
		$html .= '<p class="rbm-legenda-bloco">Exemplo servido nesta página, sem precisar clicar em nada — escolha o seu modelo acima para trocar a resposta.</p>';
	}

	$html .= '<h2>' . esc_html( $rotulo ) . ( '' === $tipo
		? ' — o que o fabricante declara'
		: ' — ' . esc_html( robometria_r1_nome_do_tipo( $tipo ) ) ) . '</h2>';

	if ( $fabricante ) {
		foreach ( $fabricante as $i ) {
			$html .= '<p class="rbm-frase">' . esc_html( robometria_r1_frase( $i ) ) . '</p>';
		}
	}

	if ( ! empty( $resp['aviso_de_variante'] ) ) {
		$frase = robometria_r1_frase_variante( $resp['aviso_de_variante'] );
		if ( '' !== $frase ) {
			$html .= '<p class="rbm-nota"><strong>Antes de comprar:</strong> ' . esc_html( $frase ) . '</p>';
		}
	}

	$html .= robometria_r1_vitrine( $fabricante, $modelo );

	if ( $terceiro ) {
		/* Seção separada, abaixo, rotulada — nunca misturada e nunca em
		   primeiro lugar (seção 7 do contrato). */
		$html .= '<div class="rbm-secao rbm-terceiro"><h3>Declarado por terceiro, não pelo fabricante</h3>';
		$html .= '<p>O que vem abaixo foi afirmado por lojista ou anunciante. Não localizamos declaração do fabricante para estes casos, e por isso eles não sobem para a lista de cima.</p>';
		foreach ( $terceiro as $i ) {
			$html .= '<p class="rbm-frase">' . esc_html( robometria_r1_frase( $i ) ) . '</p>';
		}
		$html .= '</div>';
	}

	if ( ! empty( $resp['kits_sem_composicao'] ) ) {
		$html .= '<div class="rbm-secao"><h3>Um kit serve este modelo, e ainda não sabemos o que vem dentro</h3>';
		foreach ( $resp['kits_sem_composicao'] as $k ) {
			$html .= '<p class="rbm-frase">' . esc_html( robometria_r1_frase_kit( $k ) ) . '</p>';
		}
		$html .= '</div>';
	}

	$sem_resposta = array();
	foreach ( $tipos as $t ) {
		if ( empty( $respondidos[ $t ] ) ) {
			$sem_resposta[] = $t;
		}
	}

	if ( $sem_resposta ) {
		$html .= '<div class="rbm-secao"><h3>' . ( $fabricante
			? 'O que não encontramos para este modelo'
			: 'Não temos declaração de fabricante para este modelo' ) . '</h3>';
		$html .= '<ul class="rbm-lista">';
		foreach ( $sem_resposta as $t ) {
			$html .= '<li>' . esc_html( robometria_r1_frase_recusa( $t ) ) . '</li>';
		}
		$html .= '</ul>';
		if ( ! $fabricante ) {
			$html .= '<p>Isso não quer dizer que não exista peça: quer dizer que o fabricante não publicou, em canal que a gente tenha localizado, qual peça serve neste modelo. Anúncio de marketplace afirmando compatibilidade não conta como declaração, e é por isso que ele não aparece aqui.</p>';
			/* Seção 7: sem item que atenda, o bloco não lista — mas DIGA por quê.
			   Silêncio no lugar do bloco de compra parece defeito de página. */
			$html .= '<p><strong>E é por isso que esta resposta não tem bloco de compra.</strong> Nós ganhamos comissão quando alguém compra por um link nosso, e é exatamente por isso que ele não pode aparecer aqui: vender uma peça que o fabricante não declarou para o seu robô seria transformar em receita justamente o que a página não sabe.</p>';
		}
		$html .= '</div>';
	}

	$html .= robometria_r1_divergencias( $fabricante );
	$html .= '</div>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 6. O formulário
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_r1_url_da_pagina' ) ) {
function robometria_r1_url_da_pagina() {
	if ( function_exists( 'robometria_casca_url_se_existir' ) ) {
		$url = robometria_casca_url_se_existir( ROBOMETRIA_R1_SLUG );
		if ( '' !== $url ) {
			return $url;
		}
	}
	return home_url( '/' . ROBOMETRIA_R1_SLUG . '/' );
}
}

if ( ! function_exists( 'robometria_r1_formulario' ) ) {
function robometria_r1_formulario() {
	$d = robometria_r1_dados();
	$e = robometria_r1_entrada();

	/* Marcas na ordem em que estão no banco, e dentro de cada uma os modelos na
	   ordem do banco. O <optgroup> existe para a pessoa achar a marca dela sem
	   ler 28 linhas — e para o modelo continuar sendo lista fechada. */
	$por_marca = array();
	foreach ( (array) $d['modelos'] as $m ) {
		$por_marca[ $m['marca'] ][] = $m;
	}

	$html  = '<form class="rbm-form" method="get" action="' . esc_url( robometria_r1_url_da_pagina() ) . '">';

	$html .= '<p class="rbm-form-campo"><label for="rbm-modelo">O seu robô</label>';
	$html .= '<select id="rbm-modelo" name="modelo">';
	$html .= '<option value="">escolha a marca e o modelo</option>';
	foreach ( $por_marca as $marca => $modelos ) {
		$html .= '<optgroup label="' . esc_attr( robometria_r1_marca( $marca ) ) . '">';
		foreach ( $modelos as $m ) {
			$rotulo = $m['codigo'] . ( empty( $m['linha'] ) ? '' : ' — ' . $m['linha'] );
			$html  .= '<option value="' . esc_attr( $m['id'] ) . '"'
				. ( $e['modelo'] === $m['id'] ? ' selected' : '' ) . '>'
				. esc_html( $rotulo ) . '</option>';
		}
		$html .= '</optgroup>';
	}
	$html .= '</select></p>';

	/* O seletor de tipo é GERADO da varredura do banco: tipo sem nenhuma peça
	   declarada fica de fora, porque oferecer uma escolha que sempre devolve
	   recusa contraria a promessa antes do formulário (seção 6) e ensina o
	   visitante que a ferramenta não sabe responder. Ele volta no dia em que a
	   primeira peça dele entrar no banco. */
	$html .= '<p class="rbm-form-campo"><label for="rbm-peca">Que peça</label>';
	$html .= '<select id="rbm-peca" name="peca">';
	$html .= '<option value="">todas as peças</option>';
	foreach ( (array) $d['tipos'] as $t ) {
		$html .= '<option value="' . esc_attr( $t ) . '"'
			. ( $e['peca'] === $t ? ' selected' : '' ) . '>'
			. esc_html( robometria_r1_nome_do_tipo( $t ) ) . '</option>';
	}
	$html .= '</select></p>';

	$html .= '<p class="rbm-form-acao"><button type="submit">Ver o que o fabricante declarou</button></p>';
	$html .= '</form>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 7. A tabela de exemplos pré-renderizada (seção 5 do ARQUIPELAGO.md)
 *
 * Sem ela a R1 é um formulário vazio para o robô do Google e para um modelo de
 * linguagem: os dois leem o HTML servido, e no HTML servido não existe nenhum
 * resultado de JavaScript. As linhas são GERADAS do banco — nunca digitadas —
 * e a ordem alterna marcas de propósito, porque em ordem alfabética as nove
 * primeiras seriam todas Electrolux e a promessa desta ilha é comparação
 * cross-marca.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'robometria_r1_tabela_exemplos' ) ) {
function robometria_r1_tabela_exemplos() {
	$d = robometria_r1_dados();
	if ( empty( $d['exemplos'] ) ) {
		return '';
	}

	/* O ID EXISTE PARA A BANCADA TER UMA FRONTEIRA DECLARADA. Os conferidores de
	   ar delimitavam "a resposta" de id=resultado ate o primeiro `rbm-quadro`, e
	   `rbm-quadro` e a classe de QUALQUER tabela — inclusive a de divergencias,
	   que fica DENTRO da resposta. O resultado era um bloco cortado ao meio, e
	   uma tabela publicada que nenhuma regua lia. Fronteira de teste tem de ser
	   um marcador escrito, nunca "a primeira coisa parecida com uma tabela". */
	$html  = '<div class="rbm-secao" id="rbm-exemplos"><h2>Tudo o que esta ferramenta responde hoje</h2>';
	/* A FRASE DIZIA "pares peça × modelo" E O NÚMERO ERA OUTRA COISA — item 2 do
	   despacho da Sentinela de 14/09/2026, que mediu no ar "63 pares" no alto da
	   página e "73 pares" duas telas abaixo. Os dois números estavam certos e
	   contavam coisas diferentes com o mesmo nome, que é a forma mais cara de
	   erro nesta ilha porque nenhuma régua consegue vê-lo.

	   Contado, a diferença não é a que parecia: a tabela tem uma linha por
	   (modelo, tipo, peça), responde 63 células (modelo, tipo) e mostra 56 pares
	   peça × modelo — enquanto o banco declara 63 pares. Os DOIS 63 são
	   grandezas diferentes que hoje dão o mesmo número por acidente. Igualar os
	   números teria colado duas contas que não são a mesma; o conserto é cada
	   uma dizer o que conta, e as 10 linhas a mais saírem com a causa escrita. */
	$res     = isset( $d['resumo'] ) && is_array( $d['resumo'] ) ? $d['resumo'] : array();
	$linhas  = isset( $res['linhas_da_tabela'] ) ? (int) $res['linhas_da_tabela'] : count( $d['exemplos'] );
	$celulas = isset( $res['celulas_respondidas'] ) ? (int) $res['celulas_respondidas'] : 0;
	$extras  = isset( $res['linhas_de_segunda_peca'] ) ? (int) $res['linhas_de_segunda_peca'] : 0;
	$html .= '<p>São <span class="rbm-num">' . esc_html( number_format_i18n( $linhas ) )
		. '</span> linhas, cada uma com o código, quem declarou, o endereço e a data. Elas respondem <span class="rbm-num">'
		. esc_html( number_format_i18n( $celulas ) )
		. '</span> perguntas do tipo "qual peça desta função serve neste modelo"';
	if ( $extras > 0 ) {
		$html .= ' — são mais linhas do que perguntas porque em <span class="rbm-num">'
			. esc_html( number_format_i18n( $extras ) )
			. '</span> delas o fabricante declara mais de uma peça para a mesma função do mesmo robô, e a tabela mostra as duas em vez de escolher uma';
	}
	$html .= '. A tabela sai do mesmo banco que a ferramenta consulta: se ela mudar, esta lista muda junto.</p>';

	$html .= '<div class="rbm-tabela"><table class="rbm-quadro"><thead><tr>'
		. '<th>Modelo</th><th>Peça</th><th>Código do fabricante</th><th>Como sabemos</th><th>Verificado em</th>'
		. '</tr></thead><tbody>';

	foreach ( $d['exemplos'] as $l ) {
		list( $rotulo_origem, $ressalva ) = robometria_r1_origem( $l['origem'] );

		$html .= '<tr>';
		$html .= '<td>' . esc_html( $l['modelo_rotulo'] ) . '</td>';
		$html .= '<td>' . esc_html( robometria_r1_nome_do_tipo( $l['tipo'] ) )
			. ( $l['dentro_de_kit'] ? ' <span class="rbm-tag">dentro de kit</span>' : '' ) . '</td>';
		$html .= '<td>' . ( empty( $l['codigo'] )
			? '<span class="rbm-sem-link">o fabricante não publica código</span>'
			: '<span class="rbm-codigo-peca">' . esc_html( $l['codigo'] ) . '</span>' )
			. ( $l['divergencia'] ? ' <span class="rbm-tag">divergência registrada</span>' : '' ) . '</td>';
		$html .= '<td>' . esc_html( $rotulo_origem )
			. ( empty( $l['url'] ) ? '' : ' ' . robometria_r1_fonte_link( $l['url'] ) ) . '</td>';
		$html .= '<td class="rbm-n">' . esc_html( robometria_r1_data( $l['verificado_em'] ) ) . '</td>';
		$html .= '</tr>';
	}

	$html .= '</tbody></table></div></div>';
	return $html;
}
}

/**
 * Onde a ferramenta sai vazia — publicado, e não escondido.
 *
 * Um comparador que nunca diz "não sei" está inventando em algum lugar. Esta
 * lista também é a lista de compras da coleta: são exatamente os modelos que a
 * próxima leva do banco precisa tirar do vazio.
 */
if ( ! function_exists( 'robometria_r1_lista_vazia' ) ) {
function robometria_r1_lista_vazia() {
	$d = robometria_r1_dados();
	if ( empty( $d['entrada_vazia'] ) ) {
		return '';
	}

	$rotulos = array();
	foreach ( $d['entrada_vazia'] as $mid ) {
		$m = robometria_r1_modelo( $mid );
		if ( $m ) {
			$rotulos[] = robometria_r1_rotulo_modelo( $m );
		}
	}
	sort( $rotulos );

	$html  = '<div class="rbm-secao"><h2>Onde esta ferramenta ainda não responde</h2>';
	$html .= '<p>Em <span class="rbm-num">' . esc_html( count( $rotulos ) ) . '</span> dos <span class="rbm-num">'
		. esc_html( count( $d['modelos'] ) ) . '</span> modelos do banco, não localizamos nenhuma peça declarada pelo fabricante — e a ferramenta diz isso em vez de mostrar um anúncio: '
		. esc_html( implode( ', ', $rotulos ) ) . '.</p>';
	$html .= '<p>A causa é de mercado e está medida: Electrolux e Multi publicam página de peça com a lista de modelos compatíveis e não publicam sucção em pascal; Xiaomi e WAP publicam pascal e não publicam código de peça. Enquanto for assim, um robô costuma ter resposta numa ferramenta desta ilha e recusa na outra.</p>';
	$html .= '</div>';

	return $html;
}
}

/* ---------------------------------------------------------------------------
 * 8. O shortcode
 * ------------------------------------------------------------------------- */

add_shortcode( 'robometria_r1', function () {
	$d = robometria_r1_dados();

	if ( empty( $d['modelos'] ) ) {
		/* Sem banco a ferramenta não existe — e dizer isso é melhor do que
		   servir um formulário que devolve vazio para tudo. */
		return robometria_casca_sem_banco_html(
			'Esta ferramenta está sem o banco de peças no momento.',
			'O banco é publicado a partir do repositório da Robometria. Enquanto ele não chegar, preferimos avisar a mostrar um formulário que responderia vazio para qualquer modelo.'
		);
	}

	$e       = robometria_r1_entrada();
	$r       = isset( $d['resumo'] ) ? $d['resumo'] : array();
	$ancora  = isset( $d['ancora'] ) ? $d['ancora'] : '';
	$escolhido = ( '' !== $e['modelo'] ) ? $e['modelo'] : $ancora;

	$html = '<div class="rbm-bloco">';

	/* RESPOSTA ANTES DA EXPLICAÇÃO (seção 5.2): frase autossuficiente, com
	   número e data, que sobrevive a ser citada fora de contexto. */
	$html .= '<div class="rbm-abertura">';
	$html .= '<p class="rbm-linha-mestra">Diga a marca e o modelo do seu robô e veja o filtro, a escova, o mop e a bateria que encaixam nele — e quais ninguém confirmou que encaixam.</p>';
	$html .= '<p class="rbm-prova">Aqui só está escrito que uma peça serve quando o fabricante declarou que serve, com o código, o endereço da declaração e a data. Hoje são <span class="rbm-num">' . esc_html( number_format_i18n( isset( $r['pares_declarados'] ) ? $r['pares_declarados'] : 0 ) )
		. '</span> pares peça × modelo declarados, em <span class="rbm-num">' . esc_html( number_format_i18n( isset( $r['marcas'] ) ? $r['marcas'] : 0 ) )
		. '</span> marcas, cobrindo <span class="rbm-num">' . esc_html( number_format_i18n( isset( $r['modelos_que_respondem'] ) ? $r['modelos_que_respondem'] : 0 ) )
		. '</span> dos <span class="rbm-num">' . esc_html( number_format_i18n( isset( $r['modelos_publicaveis'] ) ? $r['modelos_publicaveis'] : 0 ) )
		. '</span> modelos do banco. Nos outros, a resposta é "não localizamos declaração do fabricante" — e ela aparece com essas palavras, porque supor qual peça encaixa é o erro que custa caro para quem compra.</p>';
	$html .= '</div>';

	/* PROMESSA ANTES DO FORMULÁRIO (seção 6): uma linha dizendo o que a pessoa
	   recebe, antes de ela gastar um clique. */
	$html .= '<div class="rbm-secao"><h2>Escolha o seu robô</h2>';
	$html .= '<p class="rbm-promessa">Você recebe o código da peça, o conjunto de modelos que o fabricante citou, o endereço da declaração e a data em que ela foi verificada. Sem cadastro e sem e-mail.</p>';
	$html .= robometria_r1_formulario();
	$html .= '</div>';

	$html .= robometria_r1_resposta( $escolhido, $e['peca'], ( '' === $e['modelo'] ) );

	$html .= robometria_r1_tabela_exemplos();
	$html .= robometria_r1_lista_vazia();

	$html .= '<div class="rbm-secao"><h2>Como esta página foi montada</h2>';
	$html .= '<p><strong>Nenhuma das páginas de fabricante deste banco foi lida diretamente.</strong> O acesso direto a esses endereços está bloqueado no ambiente em que a Robometria é construída, e tudo foi colhido por busca restrita ao domínio da própria fonte. É por isso que cada resposta traz o endereço da declaração: para você conferir, e não para você acreditar.</p>';
	$html .= '<p>Também não completamos lista por analogia. Um modelo estar na lista de compatibilidade de uma peça não o coloca na lista da peça seguinte, e isso não é cautela nossa — é o que o catálogo dos próprios fabricantes mostra.</p>';
	if ( ! empty( $d['tipos_sem_nenhuma_peca_no_banco'] ) ) {
		$nomes = array_map( 'robometria_r1_nome_do_tipo', (array) $d['tipos_sem_nenhuma_peca_no_banco'] );
		$html .= '<p>O seletor acima não oferece ' . esc_html( robometria_r1_lista( $nomes ) )
			. ' porque o banco não tem nenhuma peça desse tipo, em modelo nenhum. Oferecer a escolha só para devolver recusa seria gastar o seu tempo — o tipo volta ao seletor no dia em que a primeira peça dele entrar.</p>';
	}
	$html .= '<p>' . ( function_exists( 'robometria_casca_link_html' )
		? robometria_casca_link_html( 'metodologia', 'A metodologia completa, com a escada de fontes' )
		: 'A metodologia completa, com a escada de fontes' ) . ' · '
		. ( function_exists( 'robometria_casca_link_html' )
			? robometria_casca_link_html( 'divulgacao-de-afiliados', 'Divulgação de afiliados' )
			: 'Divulgação de afiliados' ) . '</p>';
	$html .= '</div>';

	/* INTERLINKAGEM entre as duas ferramentas (seção 3 da especificação): o
	   conselho recorrente em fórum é "cheque a peça de reposição antes de
	   comprar", e o link entre as duas é a materialização desse conselho. O
	   auxiliar da casca só imprime <a> quando a página existe publicada — link
	   para página inexistente é 404 no ar. */
	$html .= '<p class="rbm-nota"><strong>Antes de comprar o robô, e não depois:</strong> '
		. ( function_exists( 'robometria_casca_link_html' )
			? robometria_casca_link_html( 'quantos-pa-o-robo-aspirador-precisa', 'quantos Pa e quanto tempo a sua casa exige' )
			: 'a ferramenta de sucção e autonomia' )
		. ' — a peça de reposição de um modelo é o que decide se ele continua limpando daqui a um ano.</p>';

	/* LINK DE MÃO DUPLA com o artigo-âncora (seção 9): o artigo aponta para esta
	   ferramenta e esta ferramenta aponta de volta. Sem os dois sentidos, a
	   página que recebe o link vira um beco, e a regra da malha do Arquipélago
	   pede mão dupla justamente porque é ela que faz as duas serem lidas como um
	   assunto só. Quem chega aqui por "qual filtro serve" já sabe o que quer; o
	   artigo é para quem chegou perguntando se existe peça universal. */
	$html .= '<div class="rbm-leia-tambem">';
	$html .= '<h2>Leia também</h2>';
	$html .= '<p>' . ( function_exists( 'robometria_casca_link_html' )
		? robometria_casca_link_html( 'filtro-universal-de-robo-aspirador', 'Por que não existe filtro universal de robô aspirador' )
		: 'Por que não existe filtro universal de robô aspirador' )
		. ' — o que o catálogo dos fabricantes mostra quando se conta quantos modelos cada peça declara.</p>';
	$html .= '</div>';

	$html .= '</div>';

	return $html;
} );

/* ---------------------------------------------------------------------------
 * 9. Cabeça da página: JSON-LD, canônica e noindex de consulta
 *
 * Tudo aqui sai no wp_head, NUNCA dentro do retorno do shortcode: o WordPress
 * roda os filtros do the_content sobre o retorno e transforma cada E-comercial
 * em entidade, o que mataria qualquer JSON-LD e qualquer script.
 * ------------------------------------------------------------------------- */

/** Estamos na página da R1? O filtro existe para o teste de bancada. */
if ( ! function_exists( 'robometria_r1_na_pagina' ) ) {
function robometria_r1_na_pagina() {
	$forcado = apply_filters( 'robometria_r1_na_pagina', null );
	if ( null !== $forcado ) {
		return (bool) $forcado;
	}
	if ( ! function_exists( 'is_page' ) ) {
		return false;
	}
	return is_page( ROBOMETRIA_R1_SLUG );
}
}

add_action( 'wp_head', function () {
	if ( ! robometria_r1_na_pagina() ) {
		return;
	}

	$d = robometria_r1_dados();
	if ( empty( $d['modelos'] ) ) {
		return;
	}

	$url = robometria_r1_url_da_pagina();

	/* A consulta é útil para quem pergunta e inútil para o índice: são 196
	   combinações de modelo × tipo, e cada URL fraca gasta orçamento de
	   rastreamento que uma página boa precisaria (seção 14.1). A resposta que
	   merece indexação — a âncora e as 45 linhas da tabela — está na página
	   limpa, e é para ela que a canônica aponta. */
	if ( robometria_r1_houve_consulta() ) {
		echo '<meta name="robots" content="noindex,follow">' . "\n";
		echo '<link rel="canonical" href="' . esc_url( $url ) . '">' . "\n";
	}

	$r = isset( $d['resumo'] ) ? $d['resumo'] : array();

	$app = array(
		'@type'              => 'WebApplication',
		'@id'                => $url . '#ferramenta',
		'name'               => ROBOMETRIA_R1_TITULO,
		'url'                => $url,
		'applicationCategory' => 'UtilitiesApplication',
		'operatingSystem'    => 'Web',
		'inLanguage'         => 'pt-BR',
		'isAccessibleForFree' => true,
		/* A LISTA DE TIPOS SAI DO BANCO, NUNCA DIGITADA AQUI (14/09/2026).
		   Esta frase é o que um modelo de linguagem lê para saber o que a
		   ferramenta faz — seção 5 do ARQUIPELAGO.md, visibilidade em IA é
		   regra de primeira classe. Até hoje ela vinha digitada, nomeando
		   "filtro, escova lateral, escova principal, mop e bateria": CINCO
		   tipos, enquanto o seletor oferecia SEIS desde 13/09, quando o
		   reservatório entrou com quatro peças declaradas. E o pior não era a
		   lista velha: era ela estar colada em dois números — pares e marcas —
		   que SEMPRE foram computados do banco. Número computado ao lado de
		   lista digitada faz a lista parecer medida, e ninguém reconfere o que
		   parece medido. Agora as três partes saem do mesmo lugar. */
		'description'        => sprintf(
			'Localiza a peça de reposição que o fabricante declarou compatível com um modelo de robô aspirador: %s, com o código do fabricante, o endereço da declaração e a data da verificação. Cobre %d pares peça × modelo em %d marcas.',
			robometria_r1_lista( array_map( 'robometria_r1_nome_do_tipo', (array) $d['tipos'] ) ),
			isset( $r['pares_declarados'] ) ? $r['pares_declarados'] : 0,
			isset( $r['marcas'] ) ? $r['marcas'] : 0
		),
		'publisher'          => array( '@id' => home_url( '/#organizacao' ) ),
	);

	/* FAQPage montado do BANCO, nunca escrito à mão: cada pergunta é uma
	   consulta real do corpus ("qual filtro serve no <modelo>") e cada resposta
	   é a frase que a própria página serve. Pergunta inventada em JSON-LD é
	   marcação que promete o que a página não entrega. */
	$perguntas = array();
	foreach ( array_slice( (array) $d['exemplos'], 0, 8 ) as $l ) {
		$resp = isset( $d['respostas'][ $l['modelo'] ] ) ? $d['respostas'][ $l['modelo'] ] : null;
		if ( ! $resp ) {
			continue;
		}
		foreach ( $resp['fabricante'] as $i ) {
			if ( $i['peca'] !== $l['peca'] || $i['tipo'] !== $l['tipo'] ) {
				continue;
			}
			$perguntas[] = array(
				'@type'          => 'Question',
				'name'           => sprintf(
					'Qual %s serve no robô aspirador %s?',
					robometria_r1_nome_do_tipo( $l['tipo'] ),
					$l['modelo_rotulo']
				),
				'acceptedAnswer' => array(
					'@type' => 'Answer',
					'text'  => robometria_r1_frase( $i ),
				),
			);
			break;
		}
	}

	$grafo = array( '@context' => 'https://schema.org', '@graph' => array( $app ) );
	if ( $perguntas ) {
		$grafo['@graph'][] = array(
			'@type'      => 'FAQPage',
			'@id'        => $url . '#perguntas',
			'inLanguage' => 'pt-BR',
			'mainEntity' => $perguntas,
		);
	}

	echo '<script type="application/ld+json" id="robometria-r1-jsonld">'
		. wp_json_encode( $grafo ) . '</script>' . "\n";
}, 7 );

/* ---------------------------------------------------------------------------
 * 10. Estilo próprio da ferramenta
 *
 * Vai no wp_head, junto do da casca e depois dele, e usa as variáveis de cor da
 * casca — a paleta continua tendo um dono só. A varredura (#CC3311) é cor de
 * sinal, de um uso por tela, e na casca esse uso é a peça do logotipo: por isso
 * aqui ela aparece apenas em foco de teclado, que é momentâneo.
 * ------------------------------------------------------------------------- */

add_action( 'wp_head', function () {
	if ( ! robometria_r1_na_pagina() ) {
		return;
	}

	/* A PROMESSA E O FORMULARIO NAO MORAM MAIS AQUI (casca 1.2.0, 11/09/2026).
	   As regras .rbm-promessa e .rbm-form* estavam duplicadas aqui e na R2, e a
	   home passou a servir o MESMO formulario — seriam tres copias. Quem manda
	   nelas agora e robometria-casca.php, em toda pagina da ilha, como ja
	   acontece com a folha da porta de compra. Abaixo fica so o que e da R1. */
	$css = <<<'CSS'
.rbm-resposta{margin:2.4rem 0 0;padding-top:1.6rem;border-top:1px solid var(--rbm-traco);}
.rbm-resposta h2{margin:0 0 .8rem;font-size:1.3rem;}
.rbm-legenda-bloco{font-family:var(--rbm-mono);font-size:.72rem;letter-spacing:.06em;text-transform:uppercase;color:var(--rbm-legenda);margin:0 0 .5rem;}
.rbm-frase{margin:0 0 .8rem;}
.rbm-terceiro{border-left:3px solid var(--rbm-alerta);padding-left:1rem;}
.rbm-codigo-peca{font-size:.9rem;letter-spacing:.03em;}
.rbm-leia-tambem{margin:2.4rem 0 0;padding-top:1.4rem;border-top:1px solid var(--rbm-traco);}
.rbm-leia-tambem h2{margin:0 0 .5rem;font-size:1.15rem;}
/* Barra fixa do celular: so aparece quando o resultado esta fora da tela, e so
   quando ha JavaScript para saber disso (o atributo vem do rodape). */
.rbm-barra{display:none;}
@media (max-width:782px){
body[data-rbm-r1-barra="1"] .rbm-barra{display:block;position:fixed;left:0;right:0;bottom:0;z-index:70;background:var(--rbm-tinta);color:var(--rbm-piso);padding:.7rem 1rem;text-align:center;font-family:var(--rbm-texto);font-size:.92rem;box-shadow:0 -6px 20px rgba(22,25,29,.18);}
body[data-rbm-r1-barra="1"] .rbm-barra a{color:var(--rbm-piso);font-weight:600;}
}
CSS;

	/* A folha da porta de compra tem UM dono, na casca (secao 1c dela). Aqui
	   ela e so concatenada — se um dia esta pagina precisar de peso diferente
	   no botao de compra, a regra muda na casca e muda para todas. */
	if ( function_exists( 'robometria_casca_css_vitrine' ) ) {
		$css = robometria_casca_css_vitrine() . "\n" . $css;
	}

	echo '<style id="robometria-r1">' . $css . '</style>' . "\n";
}, 21 );

/* ---------------------------------------------------------------------------
 * 11. O rodapé da página: a barra do celular e a rolagem até o resultado
 *
 * Duas coisas, as duas pedidas pela seção 6 do ARQUIPELAGO.md, e as duas
 * OPCIONAIS por desenho: sem JavaScript a ferramenta responde igual, porque
 * quem monta a resposta é o servidor. O script no wp_footer nunca passa pelos
 * filtros do the_content — é a regra da seção 8, nascida do defeito que matou
 * cinco calculadoras da Aquametria em 08/09/2026.
 * ------------------------------------------------------------------------- */

add_action( 'wp_footer', function () {
	if ( ! robometria_r1_na_pagina() ) {
		return;
	}
	$d = robometria_r1_dados();
	if ( empty( $d['modelos'] ) ) {
		return;
	}

	$js = <<<'JS'
(function () {
	var alvo = document.getElementById('resultado');
	if (!alvo) { return; }

	/* Rolagem ate o resultado quando a pagina volta com uma consulta: o
	   servidor ja escreveu a resposta, e a pessoa nao deveria ter que
	   procura-la. Respeita quem pediu menos movimento no sistema. */
	if (document.body.classList.contains('rbm-r1-consulta')) {
		var suave = !window.matchMedia || !window.matchMedia('(prefers-reduced-motion: reduce)').matches;
		alvo.scrollIntoView({ behavior: suave ? 'smooth' : 'auto', block: 'start' });
	}

	var barra = document.querySelector('.rbm-barra');
	if (!barra || !('IntersectionObserver' in window)) { return; }

	/* A barra so existe enquanto o resultado esta fora da tela. Quem ja esta
	   lendo a resposta nao precisa de um atalho para ela. */
	var observador = new IntersectionObserver(function (entradas) {
		entradas.forEach(function (e) {
			document.body.setAttribute('data-rbm-r1-barra', e.isIntersecting ? '0' : '1');
		});
	}, { threshold: 0 });
	observador.observe(alvo);
})();
JS;

	echo '<script id="robometria-r1-comando">' . $js . '</script>' . "\n";
}, 26 );

/**
 * A barra fixa e o sinal de consulta.
 *
 * Os dois moram no <body>, fora do retorno do shortcode, porque o retorno do
 * shortcode é filtrado. A barra nasce escondida no CSS e só aparece quando o
 * rodapé marca o corpo — sem JavaScript ela não existe, e a página continua
 * inteira.
 */
add_action( 'wp_footer', function () {
	if ( ! robometria_r1_na_pagina() ) {
		return;
	}
	$d = robometria_r1_dados();
	if ( empty( $d['modelos'] ) ) {
		return;
	}
	echo '<div class="rbm-barra"><a href="#resultado">Ver a resposta ↓</a></div>' . "\n";
}, 24 );

/* O sinal que o script do rodapé lê para saber se houve consulta. Sai como
   classe do <body>, pelo filtro do próprio WordPress: assim ele não passa nem
   perto do retorno do shortcode, e não precisa de um segundo <script> só para
   comunicar um booleano. */
add_filter( 'body_class', function ( $classes ) {
	if ( robometria_r1_na_pagina() && robometria_r1_houve_consulta() ) {
		$classes[] = 'rbm-r1-consulta';
	}
	return $classes;
} );

/* ---------------------------------------------------------------------------
 * 12. A página, e o cartão dela no hub
 *
 * A casca já lista a R1 em robometria_casca_ferramentas() com estado
 * 'em-construcao'. Aqui ela passa a 'publicada' — mas o auxiliar da casca só
 * imprime <a> quando a página existe mesmo, então nenhum cartão vira link para
 * um 404 se a criação da página falhar.
 * ------------------------------------------------------------------------- */

add_filter( 'robometria_ferramentas', function ( $lista ) {
	foreach ( $lista as $i => $f ) {
		if ( isset( $f['codigo'] ) && 'R1' === $f['codigo'] ) {
			$lista[ $i ]['estado'] = 'publicada';
			$lista[ $i ]['slug']   = ROBOMETRIA_R1_SLUG;
			/* O NOME DA PÁGINA TEM UM DONO SÓ, e é quem a cria no WordPress.
			   A semente do catálogo na casca serve à ferramenta que ainda não
			   tem snippet; assim que ele existe, quem grava o post_title passa
			   a ser também quem nomeia o cartão, a trilha e o og:title. */
			$lista[ $i ]['titulo'] = ROBOMETRIA_R1_TITULO;
		}
	}
	return $lista;
} );

if ( ! function_exists( 'robometria_r1_garantir_pagina' ) ) {
function robometria_r1_garantir_pagina() {
	$feita = get_option( 'robometria_r1_estrutura' );
	if ( ROBOMETRIA_R1_VERSAO === $feita ) {
		return;
	}

	$conteudo = '[robometria_r1]';
	$pagina   = get_page_by_path( ROBOMETRIA_R1_SLUG, OBJECT, 'page' );

	if ( ! $pagina ) {
		$pid = wp_insert_post( array(
			'post_type'      => 'page',
			'post_title'     => ROBOMETRIA_R1_TITULO,
			'post_name'      => ROBOMETRIA_R1_SLUG,
			'post_content'   => $conteudo,
			'post_status'    => 'publish',
			'comment_status' => 'closed',
			'ping_status'    => 'closed',
		), true );
		if ( is_wp_error( $pid ) ) {
			return;
		}
		update_post_meta( $pid, '_robometria_casca', '1' );
		update_post_meta( $pid, '_robometria_id', ROBOMETRIA_R1_SLUG );
		flush_rewrite_rules( false );
	} else {
		$pid = (int) $pagina->ID;
		if ( 'publish' !== $pagina->post_status ) {
			wp_update_post( array( 'ID' => $pid, 'post_status' => 'publish' ) );
		}
		/* Só repomos o shortcode em página que é nossa: página editada à mão
		   pelo Raphael não é reescrita por snippet. */
		if ( '1' === get_post_meta( $pid, '_robometria_casca', true )
			&& false === strpos( (string) $pagina->post_content, $conteudo ) ) {
			wp_update_post( array( 'ID' => $pid, 'post_content' => $conteudo ) );
		}

		/* O TÍTULO TAMBÉM É NOSSO — e esta linha faltava nos quatro snippets de
		   página desta ilha. A casca aprendeu isso na 1.2.0 (o H1 da raiz ficou
		   "Início" depois de a casca já ter mudado três vezes); ferramenta e
		   artigo, não. A página nascia com o título da constante e ficava com
		   ele para sempre: renomear aqui mudaria o og:title, o cartão e a
		   trilha — que são derivados — e deixaria o H1 e o <title> do ar com o
		   nome antigo, que é a divergência que este bloco existe para desfazer,
		   agora em duas fontes que nenhuma bancada compara. O post_name NÃO é
		   tocado: a URL não muda com o nome (seção 12.1 do contrato). */
		if ( '1' === get_post_meta( $pid, '_robometria_casca', true )
			&& (string) $pagina->post_title !== (string) ROBOMETRIA_R1_TITULO ) {
			wp_update_post( array( 'ID' => $pid, 'post_title' => ROBOMETRIA_R1_TITULO ) );
		}
	}

	update_option( 'robometria_r1_estrutura', ROBOMETRIA_R1_VERSAO, false );
}
}

if ( ! function_exists( 'robometria_r1_boot' ) ) {
function robometria_r1_boot() {
	static $ja = false;
	if ( $ja ) {
		return;
	}
	$ja = true;
	robometria_r1_garantir_pagina();
}
}

add_action( 'init', 'robometria_r1_boot', 21 );

if ( did_action( 'init' ) ) {
	robometria_r1_boot();
}
