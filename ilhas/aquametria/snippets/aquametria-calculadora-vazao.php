/**
 * Aquametria Calculadora de Vazão do Filtro — C3
 * Versão: 1.5.0 (10/09/2026) — BLOCO T8, a VITRINE. A primeira do Arquipélago,
 *   e a C3 é a primeira porque é a que tem mais itens com foto e link. O que
 *   muda, em uma frase: até aqui a página vendia por ficha técnica, e ficha é o
 *   que convence depois que a pessoa decidiu comparar. Agora existe, antes da
 *   ficha, um carrossel de cartões com foto, marca, modelo, a especificação que
 *   fez o produto entrar ("1.000 L/h — atende os 190 L do seu aquário"), a
 *   cotação com a data da coleta e o botão da loja. Cinco acréscimos:
 *   (a) VITRINE PINTADA, dentro do resultado e ANTES da ficha e da procedência,
 *   como manda o contrato 7 depois da cicatriz da Robometria de 10/09/2026;
 *   (b) VITRINE SERVIDA no HTML para o caso de referência de 100 L, pelo mesmo
 *   motivo da tabela de exemplos: quem lê esta página por máquina não executa
 *   JavaScript, e vitrine que só nasce no clique é vitrine que só o comprador
 *   que já chegou vê;
 *   (c) PREÇO, e datado. Até a 1.4.0 a página dizia três vezes que não publicava
 *   preço. A razão era boa e resolvia o problema errado: o proibido pelo
 *   contrato é preço CRAVADO COMO ATUAL, e cotação com data é o que a seção 6
 *   pede da vitrine. As três frases foram reescritas na mesma versão — página
 *   que mostra preço e diz que não publica preço se contradiz, e contradição na
 *   cara do leitor foi o defeito da C5 corrigido nesta mesma semana;
 *   (d) LINHA DE PROMESSA no topo e, no celular, barra fixa no rodapé enquanto
 *   o resultado está fora da tela, com rolagem até ele no envio do formulário —
 *   e só no envio explícito, nunca na pintura automática de quem chegou por
 *   link;
 *   (e) o gerador do catálogo passou a carregar imagem e cotação, e RECUSA
 *   gravar imagem sem texto alternativo.
 *   Nenhuma fórmula, constante, faixa ou regra de elegibilidade mudou, e a ordem
 *   da lista é exatamente a mesma: a vitrine desenha a mesma sequência de
 *   r.produtos, sem reordenar nada.
 * Versão: 1.3.0 (09/09/2026) — BLOCO 4c, fechamento: a tabela pré-renderizada
 *   passou a dizer QUAL produto atende cada faixa. Antes ela respondia ao leitor
 *   e não respondia ao comprador: a pessoa só descobria que existe recomendação
 *   depois de preencher o formulário inteiro e rolar até o fim, e no celular
 *   isso é grave. Agora cada uma das seis linhas traz o filtro do banco cuja
 *   vazão cai mais perto do meio daquela faixa, com a especificação que o fez
 *   entrar, a procedência e a data na mesma frase, e o link de loja quando
 *   existe (sponsored, noopener, aba nova), com aviso de comissão junto da
 *   tabela. Quando quem atende melhor ainda não tem link, aparece embaixo e
 *   rotulada a opção da MESMA faixa que tem — a ordem continua sendo por
 *   adequação técnica, nunca por comissão (regra V16). O FAQPage ganhou seis
 *   perguntas de compra ("qual filtro comprar para X litros"), cada uma
 *   respondida com o mesmo modelo e o mesmo número que a tabela serve. Nenhuma
 *   fórmula mudou.
 * Versão: 1.4.0 (09/09/2026) — DUPLA CONDIÇÃO e ordem em três degraus, depois
 *   de três coisas vistas pelo Raphael na página no ar (aquário de 189,6 L,
 *   plantado, carga média):
 *   (a) DEFEITO GRAVE. O primeiro item recomendado era o Atman HF-0600, e o
 *   próprio cartão dele escrevia que o fabricante declara o modelo para até
 *   150 L e que "a declaração do fabricante não cobre o seu caso". A página
 *   recomendava em primeiro lugar um filtro que ela mesma dizia não servir,
 *   porque a elegibilidade olhava só a VAZÃO. Agora entra nos recomendados só
 *   quem passa nas DUAS condições — vazão dentro da faixa E volume do visitante
 *   dentro do volume declarado pelo fabricante. Quem não declara volume entra,
 *   com a ressalva escrita. Quem declara e não cobre sai para uma seção
 *   separada, ABAIXO, rotulada "atendem a vazão, mas o fabricante não cobre
 *   esse volume". Nunca misturado, nunca em primeiro lugar.
 *   (b) O topo da lista não vendia: os dois primeiros traziam "ainda não temos
 *   link de loja". A ordem passa a ter três degraus — elegibilidade técnica
 *   dupla, adequação técnica entre os elegíveis, e SÓ COMO DESEMPATE entre
 *   itens tecnicamente equivalentes (mesmo décimo da largura da faixa), quem
 *   tem link aparece antes. Não é ordenar por comissão: taxa de comissão não é
 *   comparada em lugar nenhum, produto pior nunca sobe por pagar mais, e a
 *   frase "produto sem link de loja aparece do mesmo jeito" continua valendo —
 *   muda a POSIÇÃO de quem já era equivalente, não a presença de ninguém.
 *   (c) O catálogo embutido foi regerado: entraram o Eheim classic 600 (2217)
 *   em 127 V e em 220 V e o SunSun HW-702B 220 V, os três com link de loja.
 *   Nenhuma fórmula mudou.
 * Versão: 1.2.0 (09/09/2026) — BLOCO 4c, visibilidade em IA. A página passou a
 *   servir RESPOSTA no HTML, e não só formulário. Três acréscimos e um conserto:
 *   (a) um bloco de resposta direta no topo, com o número, o critério e a
 *   procedência dentro da própria frase, para sobreviver a ser citado fora de
 *   contexto; (b) uma tabela de seis aquários já resolvidos (30, 60, 100, 150,
 *   200 e 300 L), pré-renderizada no HTML pelo PHP — um modelo de linguagem que
 *   lê esta página via HTTP via um formulário vazio e agora lê números;
 *   (c) JSON-LD schema.org no wp_head, com WebApplication e FAQPage. O conserto:
 *   as bandas de turnover moravam em dois lugares (no JavaScript e na cabeça de
 *   quem escrevesse uma tabela) e agora moram só no PHP, que as entrega ao
 *   script como AQM_C3_BANDAS. Nenhuma fórmula mudou.
 * Versão: 1.1.0 (08/09/2026) — CORREÇÃO GRAVE: o JS e o CSS saíram de dentro do retorno do
 *   shortcode e passaram a ser impressos no wp_head (estilo) e no wp_footer (comportamento).
 *   Dentro do retorno do shortcode eles ainda atravessavam os filtros de texto do conteúdo,
 *   que trocam cada "&" pela entidade numérica dele: o primeiro "&&" do script virava um par
 *   navegador parava com SyntaxError e a calculadora inteira ficava morta — o formulário não
 *   calculava, a resposta não aparecia e o bloco de produto com os links de afiliado nunca
 *   saía do estado oculto. Nenhuma linha de cálculo mudou; mudou o lugar onde o script sai.
 * Versão: 1.0.3 (08/09/2026) — o painel de ligações passou a linkar a C15, publicada nesta data:
 * em aquário plantado a corrente e a iluminação decidem juntas o que acontece com o CO2. A 1.0.2 linkou a C12, publicada
 * data: é ela que diz quanta mídia o filtro escolhido aqui precisa carregar. A 1.0.1 linkou a C5
 *
 * Segunda calculadora do lote e a primeira com bloco de produto. Converte o
 * volume real do aquário (herdado da C1 pelo localStorage) na faixa de vazão
 * que os filtros precisam entregar — e publica o achado que a página existe
 * para publicar: o fabricante dimensiona 1,76 renovações por hora e a web
 * brasileira pede de 3 a 10. É uma divergência de até 5,7 vezes, e nenhuma
 * fonte brasileira do nosso levantamento confronta as duas.
 *
 * Registra o shortcode [aquametria_calculadora_vazao] e se anuncia no hub pelo
 * filtro 'aquametria_calculadoras' da casca: enquanto este snippet estiver
 * ativo, o cartão da C3 aparece como publicada. Nada para editar em dois lugares.
 *
 * Todo o cálculo é JavaScript no navegador, de propósito: o site está atrás do
 * cache de página da hospedagem, então HTML que dependesse da query string seria
 * servido errado para o visitante seguinte. Nada é enviado a servidor nenhum.
 *
 * O que esta calculadora NÃO faz, e por quê:
 * - Não aplica fator de perda de carga. Vazão nominal é medida sem mídia e a
 *   coluna zero; a perda com mídia suja não tem fonte no nosso levantamento e
 *   constante inventada é proibida aqui. Em vez do fator, a página entrega o
 *   protocolo do balde, que é medição própria do visitante.
 * - Não publica turnover para aquário marinho: o corpus não tem essa constante.
 *   Quem marca "tenho sump" recebe o volume mínimo do sump, que tem fonte, e a
 *   página diz que o resto não tem.
 *
 * Bloco de produto: os filtros vêm do catálogo embutido mais abaixo, gerado por
 * ferramentas/gerar-catalogo-filtros.py a partir de dados/produtos-filtro.json.
 * Mexeu no banco, rode o gerador — as duas cópias não podem divergir. Quem entra
 * na lista é decidido pela ficha técnica e por nada mais (regra V16 do esquema):
 * elegibilidade dupla (vazão na faixa E volume declarado cobrindo o visitante,
 * regra V22), depois adequação técnica. Link de afiliado não filtra ninguém e só
 * desempata entre itens tecnicamente equivalentes. Produto sem link aparece
 * igual, só que sem botão de loja. Preço entra desde a 1.5.0, e entra sempre
 * como COTAÇÃO COM DATA (de dados/produtos-cotacoes.json), nunca como preço
 * atual: o snippet é estático e o número envelhece na tela — dizer quando ele
 * foi lido é o que o torna honesto.
 *
 * Regras herdadas (fase 4b): sem "<?php" no topo (o Code Snippets põe); toda
 * função de nível superior dentro de function_exists; não usa superglobal de
 * servidor; texto de tela acentuado em UTF-8.
 */

if ( ! defined( 'ABSPATH' ) ) {
	return;
}

if ( ! defined( 'AQUAMETRIA_C3_VERSAO' ) ) {
	define( 'AQUAMETRIA_C3_VERSAO', '1.5.0' );
	define( 'AQUAMETRIA_C3_SLUG', 'calculadora-de-vazao-do-filtro' );
	define( 'AQUAMETRIA_C3_VERIFICADO_EM', '09/09/2026' );
	/* Constante 'eheim-classic-250-2213' (dados/constantes-calculadoras.json):
	   440 L/h declarados para até 250 L, ou seja 1,76 renovações por hora. É o
	   contraponto do fabricante às regras de bolso brasileiras. */
	define( 'AQUAMETRIA_C3_FABRICANTE_XH', 1.76 );
	/* Constante 'sump-proporcao-minima': 20 % do volume do aquário. */
	define( 'AQUAMETRIA_C3_SUMP_PCT', 20 );
	define( 'AQUAMETRIA_C3_PAGINA_AFILIADOS', 'divulgacao-de-afiliados' );
}

/* ---------------------------------------------------------------------------
 * 1. Anúncio no hub da casca
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c3_registrar_no_hub' ) ) {
function aquametria_c3_registrar_no_hub( $lista ) {
	if ( ! is_array( $lista ) ) {
		return $lista;
	}
	foreach ( $lista as $i => $c ) {
		if ( isset( $c['codigo'] ) && 'C3' === $c['codigo'] ) {
			$lista[ $i ]['estado'] = 'publicada';
			$lista[ $i ]['slug']   = AQUAMETRIA_C3_SLUG;
		}
	}
	return $lista;
}
}
add_filter( 'aquametria_calculadoras', 'aquametria_c3_registrar_no_hub' );

/* ---------------------------------------------------------------------------
 * 2. Catálogo de filtros
 *
 * NÃO EDITE À MÃO o trecho entre os marcadores. Ele é a cópia, dentro do
 * snippet, do que dados/produtos-filtro.json já tem — porque o site não lê o
 * repositório em tempo de execução. Depois de mexer no banco:
 *
 *     python3 ferramentas/gerar-catalogo-filtros.py
 *
 * Entra no catálogo quem o validador considera apto a ser sugerido pela C3
 * (minimo_para_sugerir do esquema) e não está em rascunho nem em revalidar.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c3_catalogo' ) ) {
function aquametria_c3_catalogo() {
	/* CATALOGO-INICIO — gerado por ferramentas/gerar-catalogo-filtros.py */
	return array(
		array(
			'id' => 'sunsun-hw-603b',
			'marca' => 'SunSun',
			'modelo' => 'HW-603B',
			'tipo' => 'canister',
			'vazao_lh' => 400,
			'potencia_w' => 6,
			'coluna_m' => 0.85,
			'coluna_na' => false,
			'volume_min_L' => null,
			'volume_max_L' => 80,
			'voltagem' => array( '110', '220' ),
			'uv_w' => null,
			'midia' => array( 'espuma', 'manta' ),
			'fonte_ref' => 'Pro-Aquarista (varejo BR especializado), ficha do SunSun HW-603B: 400 L/h, 2,3 L de camara de midia, 110 V',
			'fonte_url' => 'https://www.proaquarista.com.br/produto/sunsun-canister-hw-603b-23l-400lh-110v.html',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'imagem' => null,
			'preco' => null,
			'observacao' => 'Primeiro canister de verdade do banco para aquario pequeno: 2,3 L de camara de midia para os 80 L declarados dao 28,8 mL de midia por litro de agua, contra os 12 mL/L do cesto do Eheim classic 250 e os 6,0 mL/L do Seachem Tidal 55. E o item que faltava para a faixa de 30 a 80 L tanto na C3 quanto na C12. O campo de volume atendido carrega os 80 L do varejo BR, que e a declaracao mais conservadora das duas; a de 120 L do varejo estrangeiro sai atribuida ao lado. Coluna maxima de 0,85 m: nao vence movel alto, e isso precisa aparecer na tela.',
		),
		array(
			'id' => 'eheim-classic-250-2213',
			'marca' => 'Eheim',
			'modelo' => 'classic 250 (2213)',
			'tipo' => 'canister',
			'vazao_lh' => 440,
			'potencia_w' => 8,
			'coluna_m' => 1.5,
			'coluna_na' => false,
			'volume_min_L' => null,
			'volume_max_L' => 250,
			'voltagem' => array( '110' ),
			'uv_w' => null,
			'midia' => array( 'EHEIM SUBSTRAT pro' ),
			'fonte_ref' => 'Eheim, dados do classic 250 (2213); mesma coleta que gerou a constante eheim-classic-250-2213 do Bloco 2',
			'fonte_url' => 'https://eheim.com/en_GB/aquatics/aquarium-technology/filter/external-filter/classic-250',
			'fonte_status' => 'fabricante-via-busca',
			'verificado_em' => '2026-09-07',
			'link' => 'https://s.shopee.com.br/6fh6u1wYls',
			'anuncio' => 'Filtro Canister Classic 250 440lh Eheim - 2213',
			'loja' => 'shopee',
			'imagem' => array(
				'url' => 'https://down-bs-br.img.susercontent.com/br-11134207-7r98o-m8eusegtvu9dea.webp',
				'alt' => 'Filtro canister Eheim classic 250 (2213) verde-escuro, corpo cilíndrico com cabeçote e torneiras duplas de mangueira',
				'largura' => null,
				'altura' => null,
				'verificado_em' => null,
			),
			'preco' => array(
				'min' => 1600.0,
				'max' => 1600.0,
				'loja' => 'Shopee',
				'coletado_em' => '2026-09-07',
				'cotacoes' => 1,
			),
			'observacao' => 'O registro que ancora a C3: 440 L/h para 250 L da 1,8 renovacoes/h, de 3 a 6 vezes ABAIXO das 5 a 10 x/h que as fontes brasileiras repetem. Voltagem 110 V confirmada em varejo BR em 08/09/2026, o que libera a sugestao da C3. ATENCAO: o anuncio de afiliado nao declara voltagem, e por isso o cartao de produto obriga o aviso de conferir a voltagem antes de comprar.',
		),
		array(
			'id' => 'atman-hf-0400',
			'marca' => 'Atman',
			'modelo' => 'HF-0400',
			'tipo' => 'hang-on',
			'vazao_lh' => 440,
			'potencia_w' => 6.0,
			'coluna_m' => null,
			'coluna_na' => true,
			'volume_min_L' => null,
			'volume_max_L' => 90,
			'voltagem' => array( '110', '220' ),
			'uv_w' => null,
			'midia' => array( 'espuma', 'carvao ativado' ),
			'fonte_ref' => 'Aquaricamp (varejo BR especializado), ficha do Atman HF-0400: vazao 440 L/h, 6,0 W, aquarios de ate 90 L',
			'fonte_url' => 'https://www.aquaricamp.com.br/atman-filtro-externo-hang-on-hf-0400-440l-h.html',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'imagem' => null,
			'preco' => null,
			'observacao' => 'Hang-on: nao tem altura maxima de recalque, bombeia contra a propria carcaca (coluna_maxima_nao_se_aplica). 440 L/h para os 90 L declarados da 4,9 renovacoes/h, dentro da faixa de bolso brasileira de 5 a 10 x/h e muito acima das 1,8 x/h que a Eheim declara no classic 250. E a opcao de entrada do banco para a faixa de 30 a 90 L, que ate 09/09/2026 nao tinha filtro nenhum sugerivel.',
		),
		array(
			'id' => 'atman-hf-0600',
			'marca' => 'Atman',
			'modelo' => 'HF-0600',
			'tipo' => 'hang-on',
			'vazao_lh' => 650,
			'potencia_w' => 8.0,
			'coluna_m' => null,
			'coluna_na' => true,
			'volume_min_L' => null,
			'volume_max_L' => 150,
			'voltagem' => array( '110', '220' ),
			'uv_w' => null,
			'midia' => array( 'espuma', 'carvao ativado' ),
			'fonte_ref' => 'Aquaricamp (varejo BR especializado), ficha do Atman HF-0600: 650 L/h, 8 W, aquarios de ate 150 L',
			'fonte_url' => 'https://www.aquaricamp.com.br/filtro-atman-hang-on-650l-h-60hz-4404.html',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'imagem' => null,
			'preco' => null,
			'observacao' => 'Hang-on (coluna_maxima_nao_se_aplica). 650 L/h para 150 L declarados da 4,3 renovacoes/h. Cobre a faixa de 100 a 150 L, que so tinha canister ate 09/09/2026.',
		),
		array(
			'id' => 'atman-at-3336',
			'marca' => 'Atman',
			'modelo' => 'AT-3336',
			'tipo' => 'canister',
			'vazao_lh' => 800,
			'potencia_w' => 20,
			'coluna_m' => 1.8,
			'coluna_na' => false,
			'volume_min_L' => 180,
			'volume_max_L' => 250,
			'voltagem' => array( '110', '220' ),
			'uv_w' => null,
			'midia' => array( 'ceramica', 'espuma', 'carvao ativado' ),
			'fonte_ref' => 'Aquaricamp e Atlantida Aquarios (varejo BR especializado), ficha do canister Atman AT-3336: 800 L/h, 20 W, 1,8 m de coluna, aquarios de 180 a 250 L, 3 cestas',
			'fonte_url' => 'https://www.aquaricamp.com.br/atman-filtro-canister-at-3336-vaz-o-800-l-h.html',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'imagem' => null,
			'preco' => null,
			'observacao' => 'Irmao menor do AT-3338 (CF-1200) que ja estava no banco. 800 L/h para os 250 L do topo declarado da 3,2 renovacoes/h. Volume util de midia nao publicado por nenhuma das fontes vistas — por isso nao entra na sugestao da C12, so na da C3 e da C7.',
		),
		array(
			'id' => 'atman-hf-0800',
			'marca' => 'Atman',
			'modelo' => 'HF-0800',
			'tipo' => 'hang-on',
			'vazao_lh' => 900,
			'potencia_w' => 8.3,
			'coluna_m' => null,
			'coluna_na' => true,
			'volume_min_L' => null,
			'volume_max_L' => 250,
			'voltagem' => array( '110', '220' ),
			'uv_w' => null,
			'midia' => array( 'espuma', 'carvao ativado' ),
			'fonte_ref' => 'Pet Sonaga (varejo BR), ficha do Atman HF-0800: 900 L/h, 8,3 W, 110 V — a unica fonte vista que publica a potencia com uma casa decimal',
			'fonte_url' => 'https://www.petsonaga.com.br/aquario/bomba/aquario/filtro-externo-atman-hf-0800-900lh-8-3w-110v',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'imagem' => null,
			'preco' => null,
			'observacao' => 'Hang-on (coluna_maxima_nao_se_aplica). Com 900 L/h para 250 L sao 3,6 renovacoes/h; com os 750 L/h da fonte divergente, 3,0 x/h. A tela precisa dizer que a vazao do HF-800 nao e consenso entre as lojas brasileiras.',
		),
		array(
			'id' => 'seachem-tidal-55',
			'marca' => 'Seachem',
			'modelo' => 'Tidal 55',
			'tipo' => 'hang-on',
			'vazao_lh' => 1000,
			'potencia_w' => 6,
			'coluna_m' => null,
			'coluna_na' => true,
			'volume_min_L' => null,
			'volume_max_L' => 200,
			'voltagem' => array( '110', '220' ),
			'uv_w' => null,
			'midia' => array( 'Seachem Matrix' ),
			'fonte_ref' => 'Seachem/Sicce, manual do Tidal 55/75/110 (250 US gph = 1000 L/h; 55 US gal = 200 L; 6 W em 120 V/60 Hz e 5 W em 230 V/50 Hz; cesto de 0,32 US gal = 1,2 L)',
			'fonte_url' => 'https://www.sicce.com/media/wysiwyg/ISTRUZIONI/80N567-A_Tidal_instructions.pdf',
			'fonte_status' => 'fabricante-via-busca',
			'verificado_em' => '2026-09-08',
			'link' => 'https://s.shopee.com.br/1LfaYURnHi',
			'anuncio' => 'Filtro externo (Hang-on) - Tidal 55 - Seachem',
			'loja' => 'shopee',
			'imagem' => array(
				'url' => 'https://down-bs-br.img.susercontent.com/sg-11134201-8259a-mfv658qccpho62.webp',
				'alt' => 'Filtro externo hang-on Seachem Tidal 55 preto, caixa retangular com bomba interna e cesto de mídia visível pela tampa',
				'largura' => null,
				'altura' => null,
				'verificado_em' => null,
			),
			'preco' => array(
				'min' => 1041.0,
				'max' => 1041.0,
				'loja' => 'Shopee',
				'coletado_em' => '2026-09-07',
				'cotacoes' => 1,
			),
			'observacao' => 'Hang-on. NAO tem altura maxima de recalque: o filtro fica pendurado na borda e bombeia contra a propria carcaca, entao coluna_maxima_m nao se aplica (campo coluna_maxima_nao_se_aplica). Em 08/09/2026 saiu de \'revalidar\' para \'completo\': a eficiencia de 167 L/h por W, que o validador apontava como implausivel, e a declaracao do proprio fabricante e coerente com um hang-on trabalhando a coluna quase zero - o limite de 120 L/h por W foi calibrado para canister, e a regra V10 passou a valer so para canister e sump. Em 08/09/2026 ganhou volume_filtragem_L = 1,2 L (coleta da C12): 1,2 L de midia para os 200 L que o fabricante declara atender da 6,0 mL de midia por litro de agua - metade dos 12 mL/L do cesto do Eheim classic 250. Dois fabricantes, o mesmo problema, o dobro de midia.',
		),
		array(
			'id' => 'sunsun-hw-702b-220v',
			'marca' => 'SunSun',
			'modelo' => 'HW-702B',
			'tipo' => 'canister',
			'vazao_lh' => 1000,
			'potencia_w' => null,
			'coluna_m' => 1.4,
			'coluna_na' => false,
			'volume_min_L' => null,
			'volume_max_L' => 200,
			'voltagem' => array( '220' ),
			'uv_w' => 9.0,
			'midia' => array(),
			'fonte_ref' => 'Pet Hobby (varejo BR especializado), ficha do SunSun HW-702A: canister de 1000 L/h para aquarios de ate 200 L',
			'fonte_url' => 'https://www.pethobby.com.br/filtro-canister-hw-702a-sunsun-1000lh-aquarios-ate-200l',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => 'https://s.shopee.com.br/gPwXrF9Pl',
			'anuncio' => 'Filtro Canister HW-702-B Sunsun 1000 l/h 220 V',
			'loja' => 'shopee',
			'imagem' => array(
				'url' => 'https://down-bs-br.img.susercontent.com/sg-11134201-825af-mgfepyprq7m0f6.webp',
				'alt' => 'Filtro canister SunSun HW-702B, corpo cilíndrico branco e azul com cabeçote escuro e módulo UV, mangueiras e conexões ao lado',
				'largura' => null,
				'altura' => null,
				'verificado_em' => null,
			),
			'preco' => array(
				'min' => 699.0,
				'max' => 699.0,
				'loja' => 'Shopee',
				'coletado_em' => '2026-09-09',
				'cotacoes' => 1,
			),
			'observacao' => 'Fecha os cinco campos do minimo_para_sugerir da C3 COM link e foto, e por isso e sugerido; fica \'parcial\' porque potencia_w, que e obrigatorio da entidade e alimenta a C7, continua null. Na faixa de 150 a 200 L e o primeiro canister do banco com link E foto: 1000 L/h declarados para ate 200 L dao 5,0 renovacoes por hora no teto do volume, exatamente o piso da regra de bolso brasileira. O UV de 9 W entra no consumo total da C7 e nao no dimensionamento da C3. A potencia da bomba ficou null porque a unica ficha que a publica (Wiltec) diz 24 W no titulo e 15 W na descricao — numero que briga consigo mesmo nao vai para a tela, e somar 15 W de bomba com 9 W de UV para chegar aos 24 W seria derivacao nossa, nao declaracao de fabricante.',
		),
		array(
			'id' => 'eheim-classic-600-2217-220v',
			'marca' => 'Eheim',
			'modelo' => 'classic 600 (2217)',
			'tipo' => 'canister',
			'vazao_lh' => 1000,
			'potencia_w' => 20.0,
			'coluna_m' => 2.25,
			'coluna_na' => false,
			'volume_min_L' => null,
			'volume_max_L' => 600,
			'voltagem' => array( '220' ),
			'uv_w' => null,
			'midia' => array( 'EHEIM SUBSTRAT pro', 'EHEIM MECH', 'espuma', 'perlon' ),
			'fonte_ref' => 'AquaMaeda, Pro-Aquarista, Fazenda Submersa e AquaBetta (varejo BR especializado), fichas do Eheim classic 600 (2217): 1000 L/h, 20 W, coluna d\'agua de ate 2,25 m, aquarios de ate 600 L',
			'fonte_url' => 'https://www.aquamaeda.com.br/filtro-canister-eheim-classic-600-1000-lh-2217',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => 'https://s.shopee.com.br/9AOUfYKdQv',
			'anuncio' => 'Filtro Canister Eheim Classic 600 (2217) 1000 l/h 20 W 220 V',
			'loja' => 'shopee',
			'imagem' => array(
				'url' => 'https://down-bs-br.img.susercontent.com/sg-11134201-7rd58-m7bniamcy29b62.webp',
				'alt' => 'Filtro canister Eheim classic 600 (2217) em 220 V, corpo cilíndrico verde-escuro com cabeçote e torneiras duplas de mangueira',
				'largura' => null,
				'altura' => null,
				'verificado_em' => null,
			),
			'preco' => array(
				'min' => 2700.76,
				'max' => 2700.76,
				'loja' => 'Shopee',
				'coletado_em' => '2026-09-09',
				'cotacoes' => 1,
			),
			'observacao' => 'O contraponto de cima da C3, e o primeiro registro do banco que fecha os cinco campos do minimo_para_sugerir com link E foto na faixa acima de 200 L: 1000 L/h declarados para ate 600 L dao 1,7 renovacoes por hora no teto do volume — o mesmo dimensionamento conservador do classic 250 (2213), tres a seis vezes abaixo da regra de bolso brasileira, e por isso ele aparece com folga em aquarios de 100 a 300 L. Coluna de 2,25 m: vence movel alto, que e onde os canister baratos do banco (0,85 a 1,4 m) caem fora. Registro separado por voltagem de proposito: e chave de compatibilidade e cada anuncio vende uma versao so.',
		),
		array(
			'id' => 'eheim-classic-600-2217-127v',
			'marca' => 'Eheim',
			'modelo' => 'classic 600 (2217)',
			'tipo' => 'canister',
			'vazao_lh' => 1000,
			'potencia_w' => 20.0,
			'coluna_m' => 2.25,
			'coluna_na' => false,
			'volume_min_L' => null,
			'volume_max_L' => 600,
			'voltagem' => array( '127' ),
			'uv_w' => null,
			'midia' => array( 'EHEIM SUBSTRAT pro', 'EHEIM MECH', 'espuma', 'perlon' ),
			'fonte_ref' => 'AquaMaeda, Pro-Aquarista, Fazenda Submersa e AquaBetta (varejo BR especializado), fichas do Eheim classic 600 (2217): 1000 L/h, 20 W, coluna d\'agua de ate 2,25 m, aquarios de ate 600 L',
			'fonte_url' => 'https://www.aquamaeda.com.br/filtro-canister-eheim-classic-600-1000-lh-2217',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-09',
			'link' => 'https://s.shopee.com.br/6Akt6313pJ',
			'anuncio' => 'Filtro Canister Eheim Classic 600 (2217) 1000 l/h 20 W 127 V',
			'loja' => 'shopee',
			'imagem' => array(
				'url' => 'https://down-bs-br.img.susercontent.com/sg-11134201-7rdvk-m192mqgywnem2a.webp',
				'alt' => 'Filtro canister Eheim classic 600 (2217) em 127 V, corpo cilíndrico verde-escuro com cabeçote e torneiras duplas de mangueira',
				'largura' => null,
				'altura' => null,
				'verificado_em' => null,
			),
			'preco' => array(
				'min' => 2700.76,
				'max' => 2700.76,
				'loja' => 'Shopee',
				'coletado_em' => '2026-09-09',
				'cotacoes' => 1,
			),
			'observacao' => 'O contraponto de cima da C3, e o primeiro registro do banco que fecha os cinco campos do minimo_para_sugerir com link E foto na faixa acima de 200 L: 1000 L/h declarados para ate 600 L dao 1,7 renovacoes por hora no teto do volume — o mesmo dimensionamento conservador do classic 250 (2213), tres a seis vezes abaixo da regra de bolso brasileira, e por isso ele aparece com folga em aquarios de 100 a 300 L. Coluna de 2,25 m: vence movel alto, que e onde os canister baratos do banco (0,85 a 1,4 m) caem fora. Registro separado por voltagem de proposito: e chave de compatibilidade e cada anuncio vende uma versao so.',
		),
		array(
			'id' => 'atman-at-3338',
			'marca' => 'Atman',
			'modelo' => 'AT-3338',
			'tipo' => 'canister',
			'vazao_lh' => 1200,
			'potencia_w' => 35,
			'coluna_m' => 1.8,
			'coluna_na' => false,
			'volume_min_L' => null,
			'volume_max_L' => 450,
			'voltagem' => array( '110', '127', '220' ),
			'uv_w' => null,
			'midia' => array( 'ceramica' ),
			'fonte_ref' => 'Aquaricamp (varejo BR especializado) e outras lojas brasileiras que replicam a mesma ficha',
			'fonte_url' => 'https://www.aquaricamp.com.br/atman-filtro-canister-at-3338-vaz-o-1200-l-h-gratis-1-litro-ceramica.html',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-08',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'imagem' => null,
			'preco' => null,
			'observacao' => '1200 L/h para ate 450 L = 2,7 renovacoes/h declaradas pela propria ficha. Primeiro registro da semente com todos os campos obrigatorios da entidade preenchidos. Em 08/09/2026 a coleta da C12 trouxe o volume de midia, e trouxe junto uma ambiguidade que a C12 publica em vez de esconder: 1,6 L no conjunto ou 1,6 L por cesto (4,8 L). Pelos 450 L que a ficha declara atender, isso e a diferenca entre 3,6 e 10,7 mL de midia por litro de agua.',
		),
		array(
			'id' => 'sunsun-hw-303b',
			'marca' => 'SunSun',
			'modelo' => 'HW-303B',
			'tipo' => 'canister',
			'vazao_lh' => 1400,
			'potencia_w' => 35,
			'coluna_m' => 2.0,
			'coluna_na' => false,
			'volume_min_L' => null,
			'volume_max_L' => 350,
			'voltagem' => array( '110', '220' ),
			'uv_w' => 9,
			'midia' => array( 'ceramica', 'espuma', 'carvao ativado' ),
			'fonte_ref' => 'SunSun, especificacao do HW-303B (370 GPH = 1400 L/h; UV 9 W), replicada na pagina do produto na Amazon.com.br',
			'fonte_url' => 'https://www.amazon.com.br/SunSun-Hw303B-370GPH-filtro-esterilizador/dp/B00MH2NRIQ',
			'fonte_status' => 'fabricante-via-busca',
			'verificado_em' => '2026-09-09',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'imagem' => null,
			'preco' => null,
			'observacao' => 'Em 09/09/2026 ganhou coluna_maxima_m = 2,0 m e mangueira de 16 mm, colhidos no varejo especializado estrangeiro, e passou a ser sugerivel pela C3 — era o filtro de maior vazao do banco e estava barrado por um campo so. Saiu de \'parcial\' para \'completo\': todos os obrigatorios de filtro estao preenchidos com fonte. O volume util de midia (volume_filtragem_L) continua sem fonte nenhuma, e por isso o filtro nao entra na C12 — campo opcional na ficha, requisito daquela calculadora. 1400 L/h para 350 L = 4,0 renovacoes/h.',
		),
		array(
			'id' => 'atman-at-3338s',
			'marca' => 'Atman',
			'modelo' => 'AT-3338S',
			'tipo' => 'canister',
			'vazao_lh' => 1500,
			'potencia_w' => 18,
			'coluna_m' => 1.5,
			'coluna_na' => false,
			'volume_min_L' => 150,
			'volume_max_L' => 400,
			'voltagem' => array( '220' ),
			'uv_w' => null,
			'midia' => array(),
			'fonte_ref' => 'AquaSN (varejo BR especializado), ficha do AT-3338S 220 V',
			'fonte_url' => 'https://www.aquasn.com.br/atman-filtro-canister-at-3338s-1500-lh-220v',
			'fonte_status' => 'transcrita-varejo',
			'verificado_em' => '2026-09-08',
			'link' => null,
			'anuncio' => null,
			'loja' => null,
			'imagem' => null,
			'preco' => null,
			'observacao' => 'O caso que justificou o campo variante: uma letra a mais no modelo muda vazao (1200 para 1500 L/h), potencia (35 para 18 W), coluna (1,8 para 1,5 m) e volume atendido (ate 450 para 150 a 400 L). Sao dois produtos, nunca um. Turnover implicito de 3,8 (no teto) a 10,0 (no piso) renovacoes/h. Em 08/09/2026 ganhou volume_filtragem_L pela coleta da C12. Aqui a ficha se contradiz sozinha: as dimensoes que ela mesma publica nao comportam a capacidade que ela mesma declara por cesto.',
		),
	);
	/* CATALOGO-FIM */
}
}

/* ---------------------------------------------------------------------------
 * 3. Estilo (impresso uma vez por página, junto do primeiro shortcode)
 * ------------------------------------------------------------------------- */

/* ---------------------------------------------------------------------------
 * 2b. Bandas de turnover — FONTE ÚNICA (09/09/2026)
 *
 * Até hoje estas faixas moravam dentro do JavaScript, e qualquer texto da
 * página que quisesse citá-las tinha de repetir os números à mão. Repetir é
 * divergir mais cedo ou mais tarde. Agora elas nascem aqui: o rodapé as entrega
 * ao script como AQM_C3_BANDAS e a tabela de exemplos pré-renderizada lê o
 * mesmo array. Mudar a faixa em um lugar muda nos dois, porque só há um lugar.
 *
 * Cada faixa é uma constante registrada em dados/constantes-calculadoras.json,
 * com fonte, url e data. O piso da resposta NÃO está aqui: ele é único e vem do
 * fabricante (AQUAMETRIA_C3_FABRICANTE_XH).
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c3_bandas' ) ) {
function aquametria_c3_bandas() {
	return array(
		'comunitario' => array(
			array(
				'id'     => 'turnover-comunitario-mybest',
				'rotulo' => 'Leitura conservadora BR',
				'curto'  => 'leitura conservadora da my-best BR',
				'faixa'  => array( 4, 5 ),
				'fonte'  => 'my-best BR',
			),
			array(
				'id'     => 'turnover-comunitario-br',
				'rotulo' => 'Regra de bolso BR',
				'curto'  => 'regra de bolso brasileira',
				'faixa'  => array( 5, 10 ),
				'fonte'  => 'Aquarismo Paulista; AquaOnline',
			),
		),
		'plantado' => array(
			array(
				'id'     => 'turnover-plantado',
				'rotulo' => 'Plantado BR',
				'curto'  => 'faixa brasileira para plantado',
				'faixa'  => array( 3, 5 ),
				'fonte'  => 'AquaPeixes',
			),
		),
	);
}
}

/* A banda de bolso é a ÚLTIMA da lista do perfil — a que a maioria das fontes
   brasileiras repete e sobre a qual a carga de peixes se posiciona. O JavaScript
   usa exatamente a mesma convenção (r.bolso), e é por isso que ela está escrita
   aqui em vez de ficar subentendida. */
if ( ! function_exists( 'aquametria_c3_banda_bolso' ) ) {
function aquametria_c3_banda_bolso( $perfil ) {
	$bandas = aquametria_c3_bandas();
	$lista  = isset( $bandas[ $perfil ] ) ? $bandas[ $perfil ] : $bandas['comunitario'];
	return $lista[ count( $lista ) - 1 ];
}
}

/* ---------------------------------------------------------------------------
 * 2c. Os seis aquários resolvidos no servidor
 *
 * O motivo desta seção existir, escrito em 09/09/2026: todo o cálculo desta
 * página é JavaScript no navegador, de propósito (o site está atrás de cache de
 * página). A consequência que ninguém tinha medido é que um modelo de linguagem
 * — ou qualquer leitor que não preencha o formulário — recebia um formulário
 * VAZIO e ia embora sem um número sequer. As funções abaixo resolvem seis
 * volumes no PHP, com as MESMAS constantes do script, e o resultado sai no HTML
 * servido. Não é um segundo cálculo: é o mesmo, feito antes.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c3_volumes_exemplo' ) ) {
function aquametria_c3_volumes_exemplo() {
	return array( 30, 60, 100, 150, 200, 300 );
}
}

/* Espelho em PHP do lh() do script: vazão é número grosso, então arredonda para
   a dezena abaixo de 1000 L/h e para a cinquentena acima. Os dois têm de
   devolver a mesma string, senão a tabela servida contradiz a calculadora. */
if ( ! function_exists( 'aquametria_c3_lh' ) ) {
function aquametria_c3_lh( $n ) {
	$passo = ( $n >= 1000 ) ? 50 : 10;
	return number_format_i18n( round( $n / $passo ) * $passo, 0 );
}
}

if ( ! function_exists( 'aquametria_c3_exemplo' ) ) {
function aquametria_c3_exemplo( $volume ) {
	$bolso_com = aquametria_c3_banda_bolso( 'comunitario' );
	$bolso_pla = aquametria_c3_banda_bolso( 'plantado' );

	$piso = $volume * AQUAMETRIA_C3_FABRICANTE_XH;

	return array(
		'volume'       => $volume,
		'piso'         => $piso,
		'com_teto'     => $volume * $bolso_com['faixa'][1],
		'com_xh'       => $bolso_com['faixa'],
		'com_mira'     => ( $volume * $bolso_com['faixa'][0] + $volume * $bolso_com['faixa'][1] ) / 2,
		'pla_teto'     => $volume * $bolso_pla['faixa'][1],
		'pla_xh'       => $bolso_pla['faixa'],
		'razao'        => ( $volume * $bolso_com['faixa'][1] ) / $piso,
	);
}
}

/* ---------------------------------------------------------------------------
 * 2d. O filtro do banco que atende cada linha da tabela
 *
 * Pedido do Raphael em 09/09/2026: a tabela pré-renderizada precisa dizer, em
 * cada faixa, QUAL produto atende — senão ela responde ao leitor e não responde
 * ao comprador, e a pessoa só descobre que existe recomendação depois de
 * preencher o formulário inteiro e rolar até o fim.
 *
 * A escolha é o MESMO critério do script (função escolher()): vazão declarada
 * dentro da faixa calculada E volume da linha dentro do volume declarado pelo
 * fabricante, ordem pela distância até o meio da faixa com o link desempatando
 * entre equivalentes. Duas diferenças, e as duas são por honestidade e não por
 * atalho: a tabela não sabe o tipo de filtro que a pessoa quer nem a altura da
 * coluna do móvel dela, então não pode aplicar esses dois cortes — e o texto
 * abaixo da tabela diz isso com essas palavras. Link de afiliado NÃO decide quem
 * entra (regra V16 do esquema do banco); ele só desempata quem já era
 * tecnicamente equivalente.
 * ------------------------------------------------------------------------- */

/* A DUPLA CONDIÇÃO, escrita em 09/09/2026 depois de um defeito visto no ar.
 *
 * O que acontecia: a C3 elegia o filtro só pela VAZÃO. Num aquário de 189,6 L,
 * o primeiro da lista era o Atman HF-0600 — 650 L/h, dentro da faixa — e o
 * próprio cartão dele dizia, embaixo do nome, que o fabricante declara o modelo
 * para até 150 L e que "a declaração do fabricante não cobre o seu caso". A
 * página recomendava em primeiro lugar um filtro que ela mesma dizia não servir.
 *
 * A regra passa a ser: entra nos recomendados quem passa nas DUAS condições —
 * vazão dentro da faixa calculada E volume do visitante dentro do volume que o
 * fabricante declara. Quem não declara volume entra, com a ressalva escrita.
 * Quem declara e não cobre sai da lista de recomendados e vai para uma seção
 * separada, abaixo e rotulada. Nunca misturado, nunca em primeiro lugar. */
if ( ! function_exists( 'aquametria_c3_cobre_volume' ) ) {
function aquametria_c3_cobre_volume( $p, $volume ) {
	if ( null !== $p['volume_max_L'] && $volume > $p['volume_max_L'] ) {
		return false;
	}
	if ( null !== $p['volume_min_L'] && $volume < $p['volume_min_L'] ) {
		return false;
	}
	return true;
}
}

/* A ordem, em três degraus e nesta ordem: (1) elegibilidade técnica dupla, que
 * já aconteceu no filtro acima; (2) adequação técnica entre os elegíveis, que é
 * a distância até o meio da faixa; (3) e SÓ COMO DESEMPATE entre itens
 * tecnicamente equivalentes, quem tem link de loja aparece antes.
 *
 * "Tecnicamente equivalentes" precisa de um número, senão o desempate come a
 * ordem técnica: dois filtros são equivalentes quando as distâncias deles até o
 * meio da faixa caem no mesmo décimo da largura da faixa. É convenção editorial
 * da Aquametria, declarada, e não constante de fabricante.
 *
 * Isto NÃO é ordenar por comissão, e a proibição continua integral: taxa de
 * comissão não é comparada em lugar nenhum, e produto pior nunca sobe por pagar
 * mais. Muda a POSIÇÃO de quem já era equivalente, não a presença de ninguém. */
if ( ! function_exists( 'aquametria_c3_degrau_adequacao' ) ) {
function aquametria_c3_degrau_adequacao( $p, $piso, $teto ) {
	$meio   = ( $piso + $teto ) / 2;
	$passo  = ( $teto - $piso ) / 10;
	$dist   = abs( $p['vazao_lh'] - $meio );

	if ( $passo <= 0 ) {
		return $dist;
	}

	return floor( $dist / $passo );
}
}

if ( ! function_exists( 'aquametria_c3_ordenar' ) ) {
function aquametria_c3_ordenar( $lista, $piso, $teto ) {
	usort(
		$lista,
		function ( $a, $b ) use ( $piso, $teto ) {
			$ga = aquametria_c3_degrau_adequacao( $a, $piso, $teto );
			$gb = aquametria_c3_degrau_adequacao( $b, $piso, $teto );

			if ( $ga !== $gb ) {
				return ( $ga < $gb ) ? -1 : 1;
			}

			$la = $a['link'] ? 0 : 1;
			$lb = $b['link'] ? 0 : 1;

			if ( $la !== $lb ) {
				return $la - $lb;
			}

			$meio = ( $piso + $teto ) / 2;
			$da   = abs( $a['vazao_lh'] - $meio );
			$db   = abs( $b['vazao_lh'] - $meio );

			if ( abs( $da - $db ) >= 0.001 ) {
				return ( $da < $db ) ? -1 : 1;
			}

			return strcmp( $a['id'], $b['id'] );
		}
	);

	return $lista;
}
}

if ( ! function_exists( 'aquametria_c3_produtos_exemplo' ) ) {
function aquametria_c3_produtos_exemplo( $piso, $teto, $volume ) {
	$dentro = array();

	foreach ( aquametria_c3_catalogo() as $p ) {
		if ( $p['vazao_lh'] < $piso || $p['vazao_lh'] > $teto ) {
			continue;
		}
		if ( ! aquametria_c3_cobre_volume( $p, $volume ) ) {
			continue;
		}
		$dentro[] = $p;
	}

	return aquametria_c3_ordenar( $dentro, $piso, $teto );
}
}

/* Os que atendem a vazão e o fabricante NÃO cobre o volume. Existem na tela,
   separados e rotulados, porque esconder o modelo inteiro seria pior: a pessoa
   procuraria por ele e não saberia por que sumiu. */
if ( ! function_exists( 'aquametria_c3_produtos_fora_do_volume' ) ) {
function aquametria_c3_produtos_fora_do_volume( $piso, $teto, $volume ) {
	$fora = array();

	foreach ( aquametria_c3_catalogo() as $p ) {
		if ( $p['vazao_lh'] < $piso || $p['vazao_lh'] > $teto ) {
			continue;
		}
		if ( aquametria_c3_cobre_volume( $p, $volume ) ) {
			continue;
		}
		$fora[] = $p;
	}

	return aquametria_c3_ordenar( $fora, $piso, $teto );
}
}

if ( ! function_exists( 'aquametria_c3_produto_exemplo' ) ) {
function aquametria_c3_produto_exemplo( $piso, $teto, $volume ) {
	$lista = aquametria_c3_produtos_exemplo( $piso, $teto, $volume );
	return $lista ? $lista[0] : null;
}
}

/* O primeiro da MESMA ordem que já tem link de loja hoje. Depois do desempate
   por link, o caso em que os dois são diferentes ficou raro — ele sobra quando
   quem atende melhor está um degrau de adequação à frente de todo mundo que tem
   link, e aí a ordem técnica manda e este aqui sai embaixo, rotulado. */
if ( ! function_exists( 'aquametria_c3_produto_com_link' ) ) {
function aquametria_c3_produto_com_link( $piso, $teto, $volume ) {
	foreach ( aquametria_c3_produtos_exemplo( $piso, $teto, $volume ) as $p ) {
		if ( $p['link'] ) {
			return $p;
		}
	}
	return null;
}
}

/* A frase que o cartão da tabela publica. Ela carrega, junto, o modelo, a
   especificação QUE FEZ ELE ENTRAR e o número do aquário daquela linha — é o
   formato que sobrevive a ser recortado por um modelo de linguagem, e é também
   o que um comprador precisa ler para saber por que aquele aparelho e não outro. */
/* O banco separa por VOLTAGEM quando cada anúncio vende uma versão só — o Eheim
   classic 600 (2217) está lá duas vezes, em 127 V e em 220 V. Sem a voltagem no
   nome, a lista mostra dois itens de nome idêntico e o leitor acha que é defeito.
   Ela entra só quando o registro declara uma voltagem, que é quando ela
   identifica; registro que declara duas não ganha nada aqui. */
if ( ! function_exists( 'aquametria_c3_nome_produto' ) ) {
function aquametria_c3_nome_produto( $p ) {
	$nome = $p['marca'] . ' ' . $p['modelo'];

	if ( is_array( $p['voltagem'] ) && 1 === count( $p['voltagem'] ) ) {
		$nome .= ' (' . $p['voltagem'][0] . ' V)';
	}

	return $nome;
}
}

if ( ! function_exists( 'aquametria_c3_produto_frase' ) ) {
function aquametria_c3_produto_frase( $p, $volume ) {
	$turno = $p['vazao_lh'] / $volume;

	return aquametria_c3_nome_produto( $p ) . ' — ' . aquametria_c3_lh( $p['vazao_lh'] ) . ' L/h, '
		. number_format_i18n( round( $turno * 10 ) / 10, 1 ) . ' renovações por hora nos '
		. number_format_i18n( $volume, 0 ) . ' litros, segundo ' . aquametria_c3_origem_texto( $p['fonte_status'] )
		. ' (fonte: ' . aquametria_c3_fonte_nome( $p['fonte_ref'] ) . '), conferida em ' . aquametria_c3_data_br( $p['verificado_em'] );
}
}

/* Só o NOME de quem publicou a ficha, tirado do começo de fonte_ref. O resto do
   campo é descrição longa e vem do banco sem acento (é chave de dado, não texto
   de tela) — e esta frase é justamente a que um modelo de linguagem recorta e
   leva embora, então ela precisa sair em português correto. */
if ( ! function_exists( 'aquametria_c3_fonte_nome' ) ) {
function aquametria_c3_fonte_nome( $ref ) {
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

/* O vocabulário de fonte_status vira frase. Ele é chave de dado, não texto de
   tela: "ficha do transcrita-varejo" não é português, e uma passagem citada por
   um modelo de linguagem carrega para fora justamente essa frase. */
if ( ! function_exists( 'aquametria_c3_origem_texto' ) ) {
function aquametria_c3_origem_texto( $status ) {
	if ( 'fabricante-via-busca' === $status ) {
		return 'ficha do fabricante';
	}
	if ( 'transcrita-varejo' === $status ) {
		return 'ficha transcrita de varejo especializado';
	}
	return 'ficha de origem ' . $status;
}
}

/* Espelho em PHP do dataBr() do script. Feito por partes de propósito: converter
   com data/strtotime traria o fuso do servidor para dentro de uma data que é só
   um rótulo de coleta, e um dia a mais ou a menos aqui viraria contradição entre
   a tabela servida e o cartão que o script pinta. */
if ( ! function_exists( 'aquametria_c3_data_br' ) ) {
function aquametria_c3_data_br( $iso ) {
	if ( ! $iso || ! preg_match( '/^(\d{4})-(\d{2})-(\d{2})$/', $iso, $m ) ) {
		return (string) $iso;
	}
	return $m[3] . '/' . $m[2] . '/' . $m[1];
}
}

/* Desde a dupla condição de 09/09/2026, um recomendado NUNCA fura o volume
   declarado. O que sobra para ressalvar é o outro caso: o fabricante que não
   declara volume nenhum. Esse entra na lista, por decisão escrita, mas o leitor
   precisa saber que ali não existe declaração para conferir. A tabela servida e
   o FAQ dizem a mesma coisa que o cartão do script, senão a mesma página afirma
   duas coisas diferentes conforme o leitor execute ou não JavaScript. */
if ( ! function_exists( 'aquametria_c3_volume_ressalva' ) ) {
function aquametria_c3_volume_ressalva( $p, $volume ) {
	if ( null !== $p['volume_max_L'] ) {
		return '';
	}

	return 'O fabricante não declara volume atendido para esse modelo: ele entra pela vazão, '
		. 'e não há declaração de volume para conferir contra os ' . number_format_i18n( $volume, 0 )
		. ' litros deste exemplo.';
}
}

/* A frase da seção separada: atende a vazão, e o fabricante não cobre o volume.
   Nunca sai misturada com os recomendados nem em primeiro lugar. */
if ( ! function_exists( 'aquametria_c3_fora_do_volume_frase' ) ) {
function aquametria_c3_fora_do_volume_frase( $p, $volume ) {
	if ( null !== $p['volume_max_L'] && $volume > $p['volume_max_L'] ) {
		return 'O fabricante declara esse modelo para até ' . number_format_i18n( $p['volume_max_L'], 0 )
			. ' litros, abaixo dos ' . number_format_i18n( $volume, 0 )
			. ' deste caso: a vazão cabe na faixa, a declaração de volume não cobre.';
	}

	if ( null !== $p['volume_min_L'] && $volume < $p['volume_min_L'] ) {
		return 'O fabricante declara esse modelo a partir de ' . number_format_i18n( $p['volume_min_L'], 0 )
			. ' litros, acima dos ' . number_format_i18n( $volume, 0 )
			. ' deste caso: a vazão cabe na faixa, a declaração de volume não cobre.';
	}

	return '';
}
}

if ( ! function_exists( 'aquametria_c3_produto_celula_html' ) ) {
function aquametria_c3_produto_celula_html( $e ) {
	$p = aquametria_c3_produto_exemplo( $e['piso'], $e['com_teto'], $e['volume'] );

	/* Bloco vazio nunca sai mudo: silêncio na tela parece defeito, e o leitor
	   não tem como saber se faltou produto ou se quebrou a página. */
	if ( null === $p ) {
		return '<td><span class="aqm-c3-sem">Nenhum filtro do banco declara vazão entre '
			. esc_html( aquametria_c3_lh( $e['piso'] ) ) . ' e ' . esc_html( aquametria_c3_lh( $e['com_teto'] ) )
			. ' L/h. Assim que houver um com ficha completa, ele aparece aqui.</span></td>';
	}

	$nome  = aquametria_c3_nome_produto( $p );
	$turno = $p['vazao_lh'] / $e['volume'];

	$h = '<td>';

	if ( $p['link'] ) {
		$h .= '<a class="aqm-c3-prod" href="' . esc_url( $p['link'] ) . '" target="_blank" rel="sponsored noopener">'
			. esc_html( $nome ) . '</a>';
	} else {
		$h .= '<span class="aqm-c3-prod">' . esc_html( $nome ) . '</span>';
	}

	$h .= '<span class="aqm-c3-xh">' . esc_html( aquametria_c3_lh( $p['vazao_lh'] ) ) . ' L/h — '
		. esc_html( number_format_i18n( round( $turno * 10 ) / 10, 1 ) ) . ' renovações/h nos '
		. esc_html( number_format_i18n( $e['volume'], 0 ) ) . ' L</span>';

	$ressalva = aquametria_c3_volume_ressalva( $p, $e['volume'] );

	if ( '' !== $ressalva ) {
		$h .= '<span class="aqm-c3-sem">' . esc_html( $ressalva ) . '</span>';
	}

	if ( $p['link'] ) {
		$h .= '<span class="aqm-c3-xh">link patrocinado</span>';
		$h .= '</td>';
		return $h;
	}

	$h .= '<span class="aqm-c3-xh">ainda sem link de loja</span>';

	$c = aquametria_c3_produto_com_link( $e['piso'], $e['com_teto'], $e['volume'] );

	if ( null === $c ) {
		$h .= '<span class="aqm-c3-sem">Nenhum filtro dessa faixa tem link de loja no banco hoje.</span>';
		$h .= '</td>';
		return $h;
	}

	$h .= '<span class="aqm-c3-sem">Com link hoje, na mesma faixa: <a class="aqm-c3-prod" href="'
		. esc_url( $c['link'] ) . '" target="_blank" rel="sponsored noopener">' . esc_html( aquametria_c3_nome_produto( $c ) )
		. '</a> — ' . esc_html( aquametria_c3_lh( $c['vazao_lh'] ) ) . ' L/h, '
		. esc_html( number_format_i18n( round( ( $c['vazao_lh'] / $e['volume'] ) * 10 ) / 10, 1 ) ) . ' renovações/h. Link patrocinado. '
		. esc_html( aquametria_c3_volume_ressalva( $c, $e['volume'] ) ) . '</span>';

	$h .= '</td>';

	return $h;
}
}

/* ---------------------------------------------------------------------------
 * 2e. A VITRINE — bloco T8, 10/09/2026
 *
 * O que muda em relação à lista que já existia: a lista é ficha técnica, e ficha
 * técnica é o que convence depois que a pessoa decidiu comparar. A vitrine é o
 * que convence antes — foto, nome, a especificação que fez o produto entrar,
 * a cotação com data e o botão da loja, tudo em um cartão que cabe no polegar.
 * Ela vem ANTES da ficha e antes da procedência (contrato 7, cicatriz da
 * Robometria de 10/09/2026): a prova de onde veio o número fica, mas ela existe
 * para ser conferida, não para ser o único clique de compra da página.
 *
 * Três decisões que valem para a próxima ilha que montar vitrine:
 *
 *   1. PREÇO PASSA A SAIR, e sai DATADO. Até a 1.4.0 esta página dizia, três
 *      vezes, que não publicava preço. A razão era boa — preço muda toda semana
 *      e número velho na tela é pior que nenhum — mas ela resolvia o problema
 *      errado: o proibido pelo contrato (seção 7) é preço CRAVADO COMO ATUAL.
 *      Cotação com a data ao lado é permitida, e é o que a seção 6 pede da
 *      vitrine. As três frases foram reescritas na mesma versão: página que
 *      mostra preço e diz que não publica preço se contradiz, e contradição na
 *      cara do leitor foi o defeito da C5 corrigido nesta mesma semana.
 *
 *   2. CARTÃO SEM LINK NÃO É LINK. O contrato manda que os cartões sejam âncoras
 *      de verdade e não div com onclick. Produto sem link de loja não tem para
 *      onde apontar, então ele sai como <div>, com o lugar do botão reservado e
 *      escrito "link de loja em breve" — que é exatamente o que o contrato 7
 *      manda a ferramenta fazer enquanto afiliado.url estiver vazio.
 *
 *   3. LARGURA E ALTURA NÃO SE INVENTAM. O banco não mediu as imagens (o egresso
 *      da nuvem barra o CDN da Shopee) e a Aquametria não grava dimensão que não
 *      mediu. Em vez de chutar um par de números para satisfazer a letra da
 *      regra, o cartão reserva o espaço com aspect-ratio 1/1 e object-fit
 *      contain: o layout não salta qualquer que seja a proporção real, que é a
 *      coisa que a regra existe para garantir. Quando o banco trouxer medida,
 *      os atributos saem sozinhos — o código já os imprime quando existem.
 *
 * Não há Product/Offer no JSON-LD desta página, e é de propósito: Offer.price
 * afirma preço ATUAL, e o que temos é cotação de uma data. Declarar schema de
 * oferta com número velho seria mentir em formato de máquina, que é pior do que
 * mentir em texto, porque ninguém revisa.
 * ------------------------------------------------------------------------- */

/* A cotação vira frase: valor (ou faixa), loja e a data da coleta. Nunca "de
   R$ X por R$ Y", nunca "a partir de" — os dois sugerem promoção e a Aquametria
   não sabe se há promoção. */
if ( ! function_exists( 'aquametria_c3_preco_texto' ) ) {
function aquametria_c3_preco_texto( $p ) {
	if ( empty( $p['preco'] ) || null === $p['preco']['min'] ) {
		return '';
	}

	$pr    = $p['preco'];
	$valor = 'R$ ' . number_format_i18n( $pr['min'], 2 );

	if ( $pr['max'] > $pr['min'] ) {
		$valor = 'R$ ' . number_format_i18n( $pr['min'], 2 ) . ' a R$ ' . number_format_i18n( $pr['max'], 2 );
	}

	$onde = $pr['loja'] ? ' na ' . $pr['loja'] : '';

	return $valor . $onde . ', cotado em ' . aquametria_c3_data_br( $pr['coletado_em'] );
}
}

/* A especificação que fez o produto entrar, na forma que o contrato pede:
   "440 L/h — atende os 190 L do seu aquário". É a mesma frase que o cartão da
   ficha desenvolve em três linhas, condensada no tamanho de um cartão de
   vitrine. O rótulo do volume muda entre a vitrine servida (um exemplo) e a
   pintada pelo script (o aquário de quem está lendo). */
if ( ! function_exists( 'aquametria_c3_espec_frase' ) ) {
function aquametria_c3_espec_frase( $p, $volume, $de_quem ) {
	return aquametria_c3_lh( $p['vazao_lh'] ) . ' L/h — atende os '
		. number_format_i18n( $volume, 0 ) . ' L ' . $de_quem;
}
}

/* O cartão da vitrine tem uma linha só para a marca, então a linha do modelo NÃO
   repete a marca — "Atman / Atman HF-0600" é a cara de um cartão gerado por
   máquina que ninguém leu. A voltagem continua junto do modelo pelo motivo de
   sempre: ela identifica o registro quando o banco separa por voltagem, e sem
   ela a vitrine mostra dois cartões de nome idêntico. */
if ( ! function_exists( 'aquametria_c3_modelo_curto' ) ) {
function aquametria_c3_modelo_curto( $p ) {
	$modelo = $p['modelo'];

	if ( is_array( $p['voltagem'] ) && 1 === count( $p['voltagem'] ) ) {
		$modelo .= ' (' . $p['voltagem'][0] . ' V)';
	}

	return $modelo;
}
}

/* Um cartão. O MESMO HTML que o script monta em vitrineCartao(): duas marcações
   diferentes para o mesmo cartão dariam dois CSS e, mais cedo do que se pensa,
   duas aparências. */
if ( ! function_exists( 'aquametria_c3_vitrine_cartao_html' ) ) {
function aquametria_c3_vitrine_cartao_html( $p, $volume, $de_quem ) {
	$preco = aquametria_c3_preco_texto( $p );

	$h = '<li class="aqm-c3-vt-item">';

	if ( $p['link'] ) {
		$h .= '<a class="aqm-c3-vt-cartao" href="' . esc_url( $p['link'] ) . '" target="_blank" rel="sponsored noopener">';
	} else {
		$h .= '<div class="aqm-c3-vt-cartao aqm-c3-vt-sem-link">';
	}

	if ( ! empty( $p['imagem'] ) && ! empty( $p['imagem']['url'] ) ) {
		$img = '<img src="' . esc_url( $p['imagem']['url'] ) . '" alt="' . esc_attr( $p['imagem']['alt'] ) . '"';
		if ( ! empty( $p['imagem']['largura'] ) && ! empty( $p['imagem']['altura'] ) ) {
			$img .= ' width="' . esc_attr( $p['imagem']['largura'] ) . '" height="' . esc_attr( $p['imagem']['altura'] ) . '"';
		}
		$img .= ' loading="lazy" decoding="async">';
		$h   .= '<span class="aqm-c3-vt-foto">' . $img . '</span>';
	} else {
		/* Espaço reservado neutro. Produto sem foto NÃO some da vitrine: perder a
		   recomendação técnica certa por falta de imagem é trocar o certo pelo
		   bonito (seção 6 do ARQUIPELAGO.md). */
		$h .= '<span class="aqm-c3-vt-foto aqm-c3-vt-foto-vazia" aria-hidden="true">';
		$h .= '<span class="aqm-c3-vt-sigla">' . esc_html( $p['marca'] ) . '</span></span>';
	}

	$h .= '<span class="aqm-c3-vt-marca">' . esc_html( $p['marca'] ) . '</span>';
	$h .= '<span class="aqm-c3-vt-modelo">' . esc_html( aquametria_c3_modelo_curto( $p ) ) . '</span>';
	$h .= '<span class="aqm-c3-vt-espec">' . esc_html( aquametria_c3_espec_frase( $p, $volume, $de_quem ) ) . '</span>';

	if ( '' !== $preco ) {
		$h .= '<span class="aqm-c3-vt-preco">' . esc_html( $preco ) . '</span>';
	} else {
		$h .= '<span class="aqm-c3-vt-preco aqm-c3-vt-sem-preco">sem cotação coletada</span>';
	}

	if ( $p['link'] ) {
		$h .= '<span class="aqm-c3-vt-botao">Ver na ' . esc_html( 'shopee' === $p['loja'] ? 'Shopee' : $p['loja'] ) . '</span>';
		$h .= '<span class="aqm-c3-vt-selo">link patrocinado</span>';
		$h .= '</a>';
	} else {
		$h .= '<span class="aqm-c3-vt-espera">link de loja em breve</span>';
		$h .= '<span class="aqm-c3-vt-selo">entrou pela ficha técnica, não pelo link</span>';
		$h .= '</div>';
	}

	$h .= '</li>';

	return $h;
}
}

/* A vitrine SERVIDA no HTML, para o caso de referência de 100 litros. A pintada
   pelo script mostra o aquário de quem está lendo; esta existe porque um modelo
   de linguagem e um crawler não executam JavaScript, e vitrine que só nasce no
   clique é vitrine que só o comprador que já chegou vê. Mesmo motivo da tabela
   de exemplos, mesma regra da seção 5 do contrato. */
if ( ! function_exists( 'aquametria_c3_vitrine_servida_html' ) ) {
function aquametria_c3_vitrine_servida_html() {
	$volume = 100;
	$e      = aquametria_c3_exemplo( $volume );
	$lista  = aquametria_c3_produtos_exemplo( $e['piso'], $e['com_teto'], $volume );

	$divulgacao = function_exists( 'aquametria_casca_url_pagina' )
		? aquametria_casca_url_pagina( AQUAMETRIA_C3_PAGINA_AFILIADOS )
		: home_url( '/' . AQUAMETRIA_C3_PAGINA_AFILIADOS . '/' );

	$h  = '<div class="aqm-c3-painel aqm-c3-vitrine-servida">';
	$h .= '<h3>Os filtros que atendem um aquário de ' . esc_html( number_format_i18n( $volume, 0 ) ) . ' litros</h3>';

	if ( ! $lista ) {
		$h .= '<p class="aqm-c3-sub">Nenhum filtro do banco da Aquametria passa hoje nas duas condições deste exemplo — '
			. esc_html( aquametria_c3_lh( $e['piso'] ) ) . ' a ' . esc_html( aquametria_c3_lh( $e['com_teto'] ) )
			. ' L/h de vazão declarada E volume do fabricante cobrindo ' . esc_html( number_format_i18n( $volume, 0 ) )
			. ' litros. O banco tem ' . esc_html( count( aquametria_c3_catalogo() ) ) . ' filtros com ficha completa e cresce a cada coleta. '
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

	$h .= '<p class="aqm-c3-sub">Um aquário comunitário de ' . esc_html( number_format_i18n( $volume, 0 ) )
		. ' litros de água real pede de ' . esc_html( aquametria_c3_lh( $e['piso'] ) ) . ' a '
		. esc_html( aquametria_c3_lh( $e['com_teto'] ) ) . ' L/h, e estes são os '
		. esc_html( number_format_i18n( count( $lista ), 0 ) ) . ' filtros do banco da Aquametria que entregam essa vazão '
		. 'E têm, do fabricante, declaração de volume que cobre ' . esc_html( number_format_i18n( $volume, 0 ) ) . ' litros. '
		. 'A ordem é por proximidade do meio da faixa; entre modelos tecnicamente equivalentes, quem tem link de loja aparece antes. '
		. 'Troque o número no formulário acima para ver a lista do seu aquário.</p>';

	$h .= '<ul class="aqm-c3-vt-trilho">';
	foreach ( $lista as $p ) {
		$h .= aquametria_c3_vitrine_cartao_html( $p, $volume, 'deste exemplo' );
	}
	$h .= '</ul>';

	$h .= '<p class="aqm-c3-criterio">' . esc_html( $com_link ) . ' de ' . esc_html( count( $lista ) )
		. ' têm link de loja hoje; os outros aparecem do mesmo jeito, com o lugar do botão reservado — '
		. 'quem entra é decidido pela ficha técnica, e nunca por ter ou não link.</p>';

	$h .= '<p class="aqm-c3-aviso-afiliado"><strong>Sobre o preço e o botão.</strong> '
		. 'O valor de cada cartão <strong>não é preço de hoje</strong>: é a cotação que a Aquametria leu naquele anúncio na data escrita ao lado, '
		. 'e preço de aquarismo muda toda semana. Confira no anúncio antes de comprar. '
		. 'Os botões levam a lojas por link de afiliado, marcado como patrocinado: se você comprar por eles, a Aquametria pode receber comissão, sem custo a mais para você. '
		. 'A ficha técnica de cada filtro vem do fabricante ou do varejo especializado, com o endereço e a data — o anúncio da loja nunca é a nossa fonte. '
		. '<a href="' . esc_url( $divulgacao ) . '">Como a Aquametria ganha dinheiro</a>.</p>';

	$h .= '</div>';

	return $h;
}
}

/* A linha de promessa, antes do formulário: o que a pessoa recebe se preencher.
   Curta, sem exclamação, sem tom de anúncio (seção 6 do ARQUIPELAGO.md). */
if ( ! function_exists( 'aquametria_c3_promessa_html' ) ) {
function aquametria_c3_promessa_html() {
	return '<p class="aqm-c3-promessa">Calcule a vazão do seu aquário e veja quais filtros atendem, '
		. 'com a faixa e a fonte de cada um.</p>';
}
}

/* A barra do celular. Ela só existe enquanto o resultado está fora da tela, e
   só em tela estreita — o CSS a esconde acima de 600 px, e o script só liga a
   classe depois de um cálculo. Fora do <form> de propósito: position:fixed
   dentro de um painel com rolagem própria briga com o painel. */
if ( ! function_exists( 'aquametria_c3_barra_html' ) ) {
function aquametria_c3_barra_html() {
	$h  = '<div class="aqm-c3-barra" id="aqm-c3-barra" aria-hidden="true">';
	$h .= '<span class="aqm-c3-barra-texto" id="aqm-c3-barra-texto"></span>';
	$h .= '<button type="button" class="aqm-c3-barra-botao" id="aqm-c3-barra-ir">Ver o resultado</button>';
	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c3_css' ) ) {
function aquametria_c3_css() {
	return <<<'CSS'
.aqm-c3{--c3-tinta:var(--aqm-tinta,#0D1B22);--c3-lamina:var(--aqm-lamina,#0E7C8C);
--c3-papel:var(--aqm-papel,#F4F7F7);--c3-superficie:var(--aqm-superficie,#FFFFFF);
--c3-traco:var(--aqm-traco,#DDE5E6);--c3-legenda:var(--aqm-legenda,#5C7075);
--c3-alerta:var(--aqm-alerta,#B5762A);
--c3-display:var(--aqm-display,"Chivo","Trebuchet MS",Arial,sans-serif);
--c3-texto:var(--aqm-texto,"IBM Plex Sans",system-ui,Arial,sans-serif);
--c3-mono:var(--aqm-mono,"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace);
max-width:52rem;font-family:var(--c3-texto);color:var(--c3-tinta);}
.aqm-c3 *{box-sizing:border-box;}
.aqm-c3 form{margin:0;}
.aqm-c3-painel{background:var(--c3-superficie);border:1px solid var(--c3-traco);border-radius:3px;padding:1.2rem 1.3rem;margin:0 0 1.2rem;}
.aqm-c3-painel h3{font-family:var(--c3-display);font-size:1.05rem;margin:0 0 .2rem;}
.aqm-c3-painel .aqm-c3-sub{color:var(--c3-legenda);font-size:.9rem;margin:0 0 1rem;line-height:1.5;}
.aqm-c3-grade{display:grid;grid-template-columns:repeat(auto-fit,minmax(10.5rem,1fr));gap:.9rem;}
.aqm-c3-campo{display:flex;flex-direction:column;gap:.25rem;}
.aqm-c3-campo label{font-size:.82rem;font-weight:600;letter-spacing:.01em;}
.aqm-c3-campo .aqm-c3-dica{font-size:.74rem;color:var(--c3-legenda);line-height:1.35;}
.aqm-c3 input[type=text],.aqm-c3 select{width:100%;font-family:var(--c3-mono);font-size:1rem;padding:.5rem .6rem;border:1px solid var(--c3-traco);border-radius:2px;background:var(--c3-superficie);color:var(--c3-tinta);}
.aqm-c3 select{font-family:var(--c3-texto);}
.aqm-c3 input:focus,.aqm-c3 select:focus{outline:2px solid var(--c3-lamina);outline-offset:1px;}
.aqm-c3 input.aqm-c3-erro{border-color:var(--c3-alerta);}
.aqm-c3-caixa{display:flex;align-items:flex-start;gap:.45rem;margin:1rem 0 0;font-size:.9rem;}
.aqm-c3-caixa input{margin-top:.2rem;}
.aqm-c3-botoes{display:flex;flex-wrap:wrap;gap:.7rem;align-items:center;margin:1.1rem 0 0;}
.aqm-c3 button{font-family:var(--c3-texto);font-weight:600;font-size:.95rem;padding:.6rem 1.1rem;border:0;border-radius:2px;background:var(--c3-lamina);color:var(--c3-superficie);cursor:pointer;}
.aqm-c3 button.aqm-c3-secundario{background:transparent;color:var(--c3-lamina);border:1px solid var(--c3-traco);}
.aqm-c3 button:hover{filter:brightness(1.08);}
.aqm-c3-avisos{margin:.9rem 0 0;padding:0;list-style:none;}
.aqm-c3-avisos li{font-size:.88rem;color:var(--c3-alerta);margin:.25rem 0 0;line-height:1.45;}
.aqm-c3-resultado{margin:0 0 1.2rem;}
.aqm-c3-faixa{background:var(--c3-superficie);border:2px solid var(--c3-lamina);border-radius:3px;padding:1.1rem 1.2rem;margin:0 0 1rem;}
.aqm-c3-rotulo{font-family:var(--c3-mono);font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--c3-legenda);}
.aqm-c3-valor{font-family:var(--c3-mono);font-size:2rem;font-weight:600;line-height:1.1;font-variant-numeric:tabular-nums;display:block;margin:.15rem 0 .1rem;}
.aqm-c3-valor .aqm-c3-unidade{font-size:.95rem;font-weight:500;color:var(--c3-legenda);margin-left:.3rem;}
.aqm-c3-criterio{font-size:.83rem;color:var(--c3-legenda);line-height:1.5;margin:0;}
.aqm-c3-cartoes{display:grid;grid-template-columns:repeat(auto-fit,minmax(13rem,1fr));gap:.9rem;margin:0 0 1rem;padding:0;list-style:none;}
.aqm-c3-cartao{background:var(--c3-superficie);border:1px solid var(--c3-traco);border-radius:3px;padding:1rem 1.1rem;margin:0;display:flex;flex-direction:column;gap:.3rem;}
.aqm-c3-cartao .aqm-c3-valor{font-size:1.5rem;}
.aqm-c3-nota{border-left:3px solid var(--c3-lamina);background:var(--c3-superficie);padding:.85rem 1rem;font-size:.92rem;line-height:1.55;color:var(--c3-legenda);margin:0 0 1rem;}
.aqm-c3-nota strong{color:var(--c3-tinta);}
.aqm-c3-nota.aqm-c3-nota-alerta{border-left-color:var(--c3-alerta);}
.aqm-c3-vazio{font-family:var(--c3-texto);font-size:.95rem;color:var(--c3-legenda);font-weight:500;}
.aqm-c3-produtos{margin:0 0 1.2rem;}
.aqm-c3-fora{border-left:3px solid var(--c3-alerta);}
.aqm-c3-fora .aqm-c3-numero{color:var(--c3-alerta);}
.aqm-c3-produtos h3{font-family:var(--c3-display);font-size:1.05rem;margin:0 0 .2rem;}
.aqm-c3-lista{list-style:none;margin:1rem 0 0;padding:0;display:grid;gap:.9rem;}
.aqm-c3-produto{background:var(--c3-superficie);border:1px solid var(--c3-traco);border-radius:3px;padding:1rem 1.1rem;display:grid;grid-template-columns:6.5rem 1fr;gap:1rem;align-items:start;}
.aqm-c3-placa{background:var(--c3-papel);border:1px solid var(--c3-traco);border-radius:2px;padding:.7rem .5rem;text-align:center;display:flex;flex-direction:column;gap:.15rem;justify-content:center;min-height:6rem;}
.aqm-c3-placa .aqm-c3-marca{font-family:var(--c3-display);font-size:.9rem;font-weight:700;line-height:1.15;}
.aqm-c3-placa .aqm-c3-numero{font-family:var(--c3-mono);font-size:1.15rem;font-weight:600;color:var(--c3-lamina);line-height:1.1;}
.aqm-c3-placa .aqm-c3-un{font-family:var(--c3-mono);font-size:.62rem;letter-spacing:.08em;text-transform:uppercase;color:var(--c3-legenda);}
.aqm-c3-produto h4{font-family:var(--c3-display);font-size:1rem;margin:0 0 .35rem;}
.aqm-c3-porque{font-size:.88rem;line-height:1.5;margin:0 0 .5rem;}
.aqm-c3-porque strong{font-family:var(--c3-mono);font-size:.86rem;}
.aqm-c3-ficha{list-style:none;margin:0 0 .6rem;padding:0;font-size:.82rem;color:var(--c3-legenda);line-height:1.5;}
.aqm-c3-ficha li{margin:0;}
.aqm-c3-ficha b{font-family:var(--c3-mono);font-weight:600;color:var(--c3-tinta);}
.aqm-c3-loja{display:inline-block;font-family:var(--c3-texto);font-weight:600;font-size:.88rem;padding:.45rem .9rem;border-radius:2px;background:var(--c3-lamina);color:var(--c3-superficie);text-decoration:none;}
.aqm-c3-loja:hover{filter:brightness(1.08);color:var(--c3-superficie);}
.aqm-c3-semloja{font-size:.82rem;color:var(--c3-legenda);font-style:italic;}
.aqm-c3-aviso-afiliado{background:var(--c3-papel);border:1px solid var(--c3-traco);border-left:3px solid var(--c3-alerta);border-radius:2px;padding:.8rem 1rem;font-size:.86rem;line-height:1.5;color:var(--c3-legenda);margin:1rem 0 0;}
.aqm-c3-aviso-afiliado strong{color:var(--c3-tinta);}
.aqm-c3-citar{background:var(--c3-papel);border:1px dashed var(--c3-traco);border-radius:3px;padding:.85rem 1rem;font-size:.9rem;line-height:1.5;margin:0 0 1rem;}
.aqm-c3-citar p{margin:0 0 .6rem;}
.aqm-c3-rolagem{overflow-x:auto;-webkit-overflow-scrolling:touch;}
.aqm-c3-fontes{width:100%;min-width:32rem;font-size:.86rem;border-collapse:collapse;margin:.4rem 0 0;}
.aqm-c3-fontes th,.aqm-c3-fontes td{border:1px solid var(--c3-traco);padding:.45rem .6rem;text-align:left;vertical-align:top;}
.aqm-c3-fontes th{background:var(--c3-papel);font-family:var(--c3-display);font-size:.8rem;}
.aqm-c3-fontes td:first-child{font-family:var(--c3-mono);font-size:.8rem;white-space:nowrap;}
.aqm-c3-selo{display:inline-block;font-family:var(--c3-mono);font-size:.66rem;letter-spacing:.08em;text-transform:uppercase;color:var(--c3-alerta);border:1px solid var(--c3-alerta);border-radius:2px;padding:.1rem .35rem;}
.aqm-c3-adiante ul{margin:.5rem 0 0;padding-left:1.1rem;}
.aqm-c3-adiante li{margin:0 0 .4rem;font-size:.94rem;line-height:1.5;}
.aqm-c3-direta{background:var(--c3-papel);border-left:3px solid var(--c3-lamina);border-radius:0 3px 3px 0;padding:1.05rem 1.25rem;margin:0 0 1.2rem;}
.aqm-c3-direta p{font-size:.94rem;line-height:1.62;margin:0 0 .75rem;color:var(--c3-tinta);}
.aqm-c3-direta p:last-child{margin-bottom:0;}
.aqm-c3-direta .aqm-c3-destaque{font-size:1.06rem;line-height:1.5;}
.aqm-c3-direta .aqm-c3-destaque strong{font-family:var(--c3-display);}
.aqm-c3-exemplos .aqm-c3-fontes td{font-size:.84rem;}
.aqm-c3-exemplos .aqm-c3-fontes td:first-child{font-weight:600;color:var(--c3-tinta);}
.aqm-c3-exemplos .aqm-c3-fontes{min-width:46rem;}
.aqm-c3-prod{display:block;font-weight:600;color:var(--c3-tinta);font-size:.86rem;line-height:1.35;}
a.aqm-c3-prod{color:var(--c3-lamina);text-decoration:underline;}
.aqm-c3-sem{display:block;color:var(--c3-legenda);font-size:.78rem;line-height:1.45;}
.aqm-c3-num{font-family:var(--c3-mono);font-variant-numeric:tabular-nums;white-space:nowrap;}
.aqm-c3-xh{display:block;color:var(--c3-legenda);font-family:var(--c3-texto);font-size:.76rem;}
.aqm-c3-oculto{display:none;}
.aqm-c3-promessa{font-family:var(--c3-display);font-size:1.02rem;line-height:1.5;color:var(--c3-tinta);border-left:3px solid var(--c3-lamina);padding:.15rem 0 .15rem .8rem;margin:0 0 1.1rem;}
.aqm-c3-vitrine{margin:1rem 0 0;}
.aqm-c3-vitrine h4{font-family:var(--c3-display);font-size:.95rem;margin:0 0 .15rem;}
.aqm-c3-vt-trilho{display:flex;gap:.8rem;margin:.7rem 0 0;padding:.15rem .15rem .9rem;list-style:none;overflow-x:auto;-webkit-overflow-scrolling:touch;scroll-snap-type:x mandatory;scroll-padding-left:.15rem;}
.aqm-c3-vt-item{flex:0 0 13.5rem;margin:0;scroll-snap-align:start;}
.aqm-c3-vt-cartao{display:flex;flex-direction:column;gap:.28rem;height:100%;background:var(--c3-superficie);border:1px solid var(--c3-traco);border-radius:3px;padding:.7rem .75rem .8rem;text-decoration:none;color:var(--c3-tinta);}
a.aqm-c3-vt-cartao:hover{border-color:var(--c3-lamina);color:var(--c3-tinta);}
a.aqm-c3-vt-cartao:focus-visible{outline:2px solid var(--c3-lamina);outline-offset:1px;}
.aqm-c3-vt-foto{display:flex;align-items:center;justify-content:center;aspect-ratio:1/1;width:100%;max-width:100%;background:var(--c3-papel);border:1px solid var(--c3-traco);border-radius:2px;overflow:hidden;margin:0 0 .35rem;}
.aqm-c3-vt-foto img{display:block;width:100%;height:100%;max-width:100%;object-fit:contain;}
.aqm-c3-vt-foto-vazia .aqm-c3-vt-sigla{font-family:var(--c3-display);font-size:1rem;font-weight:700;color:var(--c3-legenda);letter-spacing:.02em;text-align:center;padding:0 .4rem;}
.aqm-c3-vt-marca{font-family:var(--c3-mono);font-size:.66rem;letter-spacing:.1em;text-transform:uppercase;color:var(--c3-legenda);}
.aqm-c3-vt-modelo{font-family:var(--c3-display);font-size:.92rem;font-weight:700;line-height:1.25;}
.aqm-c3-vt-espec{font-family:var(--c3-mono);font-size:.76rem;line-height:1.4;color:var(--c3-lamina);font-variant-numeric:tabular-nums;}
.aqm-c3-vt-preco{font-family:var(--c3-mono);font-size:.8rem;font-variant-numeric:tabular-nums;color:var(--c3-tinta);}
.aqm-c3-vt-preco.aqm-c3-vt-sem-preco{font-family:var(--c3-texto);font-size:.76rem;color:var(--c3-legenda);font-style:italic;}
.aqm-c3-vt-botao{margin-top:auto;text-align:center;font-family:var(--c3-texto);font-weight:600;font-size:.85rem;padding:.42rem .7rem;border-radius:2px;background:var(--c3-lamina);color:var(--c3-superficie);}
.aqm-c3-vt-espera{margin-top:auto;text-align:center;font-family:var(--c3-texto);font-weight:600;font-size:.82rem;padding:.42rem .7rem;border-radius:2px;background:var(--c3-papel);border:1px dashed var(--c3-traco);color:var(--c3-legenda);}
.aqm-c3-vt-selo{font-family:var(--c3-mono);font-size:.62rem;letter-spacing:.06em;text-transform:uppercase;color:var(--c3-legenda);text-align:center;margin-top:.25rem;}
.aqm-c3-vitrine-servida .aqm-c3-criterio{margin-top:.5rem;}
.aqm-c3-barra{position:fixed;left:0;right:0;bottom:0;z-index:40;display:none;align-items:center;gap:.7rem;background:var(--c3-superficie);border-top:1px solid var(--c3-traco);padding:.55rem .85rem;}
.aqm-c3-barra-texto{flex:1 1 auto;font-family:var(--c3-mono);font-size:.8rem;line-height:1.3;color:var(--c3-tinta);font-variant-numeric:tabular-nums;}
.aqm-c3-barra-botao{flex:0 0 auto;}
@media (max-width:600px){.aqm-c3-valor{font-size:1.6rem;}
.aqm-c3-produto{grid-template-columns:1fr;}
.aqm-c3-vt-item{flex-basis:11.5rem;}
.aqm-c3-barra.aqm-c3-barra-ver{display:flex;}
.aqm-c3-placa{min-height:0;flex-direction:row;gap:.5rem;align-items:baseline;justify-content:flex-start;}}
@media (prefers-reduced-motion:reduce){.aqm-c3-vt-trilho{scroll-behavior:auto;}}
CSS;
}
}

/* ---------------------------------------------------------------------------
 * 4. Comportamento (todo o cálculo mora aqui)
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c3_js' ) ) {
function aquametria_c3_js() {
	return <<<'JS'
(function () {
	'use strict';

	var CHAVE = 'aquametria.aquario';
	var FABRICANTE_XH = 1.76;   /* eheim-classic-250-2213: 440 L/h para 250 L */
	var SUMP_PCT = 20;          /* sump-proporcao-minima */

	/* Bandas de turnover, por perfil. Cada uma é uma constante do registro em
	   dados/constantes-calculadoras.json, com fonte e data. Não há banda para
	   aquário marinho: o levantamento não trouxe nenhuma, e aqui não se inventa.
	   Desde 09/09/2026 elas NÃO são escritas aqui: vêm do PHP, de
	   aquametria_c3_bandas(), pela variável AQM_C3_BANDAS impressa no rodapé.
	   O motivo é a tabela de exemplos pré-renderizada, que precisa das mesmas
	   faixas — e duas cópias das mesmas faixas divergem em silêncio. */
	var BANDAS = (typeof AQM_C3_BANDAS === 'object' && AQM_C3_BANDAS) ? AQM_C3_BANDAS : {};
	if (!BANDAS.comunitario || !BANDAS.plantado) { return; }

	var raiz = document.querySelector('.aqm-c3');
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

	/* Vazão é número grosso: arredondar para dezena abaixo de 1000 e para
	   cinquentena acima disso evita a falsa precisão de "437 L/h". */
	function lh(n) {
		if (n === null || !isFinite(n)) { return '—'; }
		var passo = n >= 1000 ? 50 : 10;
		return fmt(Math.round(n / passo) * passo, 0);
	}

	function litros(n) {
		if (n === null || !isFinite(n)) { return '—'; }
		return n >= 100 ? fmt(Math.round(n), 0) : fmt(Math.round(n * 10) / 10, 1);
	}

	function campos() {
		return {
			volume: num(el('aqm-c3-volume').value),
			perfil: el('aqm-c3-perfil').value === 'plantado' ? 'plantado' : 'comunitario',
			carga: el('aqm-c3-carga').value,
			coluna: num(el('aqm-c3-coluna').value),
			tipo: el('aqm-c3-tipo').value,
			sump: el('aqm-c3-sump').checked
		};
	}

	/* ------------------------------------------------------------- o cálculo */

	function calcular(d) {
		var r = { erros: [], avisos: [] };

		if (d.volume === null) {
			r.erros.push({ campo: 'volume', texto: 'Informe o volume real de água do aquário, em litros.' });
		} else if (d.volume <= 0) {
			r.erros.push({ campo: 'volume', texto: 'O volume precisa ser maior que zero.' });
		} else if (d.volume > 20000) {
			r.erros.push({ campo: 'volume', texto: 'Acima de 20 000 L: confira a unidade (o campo é em litros).' });
		}
		if (d.coluna !== null && (d.coluna < 0 || d.coluna > 6)) {
			r.erros.push({ campo: 'coluna', texto: 'Altura de coluna em metros, entre 0 e 6.' });
		}
		if (r.erros.length) { return r; }

		var V = d.volume;
		r.entradas = d;
		r.piso = V * FABRICANTE_XH;
		r.bandas = BANDAS[d.perfil].map(function (b) {
			return {
				id: b.id, rotulo: b.rotulo, fonte: b.fonte, xh: b.faixa,
				min: V * b.faixa[0], max: V * b.faixa[1]
			};
		});

		var tetos = r.bandas.map(function (b) { return b.max; });
		r.teto = Math.max.apply(null, tetos);
		r.teto_xh = r.teto / V;
		r.razao = r.teto / r.piso;

		/* A banda de bolso é a última da lista: é ela que a maioria das fontes
		   brasileiras repete, e é sobre ela que a carga de peixes se posiciona. */
		r.bolso = r.bandas[r.bandas.length - 1];

		if (d.sump) {
			r.sump_L = V * SUMP_PCT / 100;
		}

		if (d.coluna !== null && d.coluna > 0) {
			r.avisos.push('A vazão nominal do catálogo é medida a coluna zero e sem mídia. Com ' + fmt(d.coluna, 1)
				+ ' m de coluna e o cesto cheio, a vazão que chega ao aquário é menor — quanto menor, não sabemos: '
				+ 'não existe fator de perda com fonte no nosso levantamento, e aqui não se inventa constante. Meça com o protocolo do balde.');
		}

		r.produtos = escolher(r, d);
		return r;
	}

	/* A DUPLA CONDIÇÃO. Espelho exato de aquametria_c3_cobre_volume() no PHP:
	   quem não declara volume entra (com a ressalva escrita no cartão), quem
	   declara e não cobre o volume do visitante NÃO entra nos recomendados. */
	function cobreVolume(p, V) {
		if (p.volume_max_L !== null && V > p.volume_max_L) { return false; }
		if (p.volume_min_L !== null && V < p.volume_min_L) { return false; }
		return true;
	}

	/* Espelho de aquametria_c3_degrau_adequacao(): a adequação vira degrau de um
	   décimo da largura da faixa, para que "tecnicamente equivalente" seja um
	   número e não uma impressão. */
	function degrau(p, r) {
		var meio = (r.piso + r.teto) / 2;
		var passo = (r.teto - r.piso) / 10;
		var dist = Math.abs(p.vazao_lh - meio);
		return passo <= 0 ? dist : Math.floor(dist / passo);
	}

	/* Três degraus, nesta ordem: adequação técnica; depois, SÓ entre equivalentes,
	   quem tem link de loja; depois a distância exata e o id, para a ordem ser
	   sempre a mesma. Comissão não é comparada em lugar nenhum. */
	function ordenar(lista, r) {
		var meio = (r.piso + r.teto) / 2;
		return lista.sort(function (a, b) {
			var ga = degrau(a, r), gb = degrau(b, r);
			if (ga !== gb) { return ga - gb; }
			var la = a.link ? 0 : 1, lb = b.link ? 0 : 1;
			if (la !== lb) { return la - lb; }
			var da = Math.abs(a.vazao_lh - meio), db = Math.abs(b.vazao_lh - meio);
			if (Math.abs(da - db) >= 0.001) { return da - db; }
			return a.id < b.id ? -1 : (a.id > b.id ? 1 : 0);
		});
	}

	/* Elegibilidade: vazão dentro da faixa calculada, coluna suficiente, tipo
	   compatível E volume do visitante dentro do volume que o fabricante declara.
	   Quem passa em tudo menos no volume declarado vai para a seção separada, e
	   nunca para os recomendados: até 09/09/2026 a página recomendava em primeiro
	   lugar um filtro que ela mesma dizia não cobrir o aquário. */
	function escolher(r, d) {
		var V = d.volume;
		var fora = [];
		var dentro = [];
		var foraVolume = [];

		AQM_C3_CATALOGO.forEach(function (p) {
			if (d.tipo !== 'qualquer' && p.tipo !== d.tipo) { return; }
			if (p.vazao_lh < r.piso || p.vazao_lh > r.teto) { return; }
			if (d.coluna !== null && d.coluna > 0 && !p.coluna_na && p.coluna_m !== null && p.coluna_m < d.coluna) {
				fora.push(nomeProduto(p) + ' atende a faixa, mas a coluna máxima declarada ('
					+ fmt(p.coluna_m, 1) + ' m) é menor que os ' + fmt(d.coluna, 1) + ' m que você informou.');
				return;
			}
			if (cobreVolume(p, V)) { dentro.push(p); } else { foraVolume.push(p); }
		});

		r.barrados_por_coluna = fora;
		r.fora_do_volume = ordenar(foraVolume, r).slice(0, 5);
		return ordenar(dentro, r).slice(0, 5);
	}

	/* ------------------------------------------------------------------ tela */

	function pintar(r) {
		var alvo = el('aqm-c3-saida');
		var ul = el('aqm-c3-erros');
		ul.innerHTML = '';
		raiz.querySelectorAll('.aqm-c3-erro').forEach(function (n) { n.classList.remove('aqm-c3-erro'); });

		if (r.erros && r.erros.length) {
			var vistos = {};
			r.erros.forEach(function (er) {
				var campo = el('aqm-c3-' + er.campo);
				if (campo) { campo.classList.add('aqm-c3-erro'); }
				if (vistos[er.texto]) { return; }
				vistos[er.texto] = true;
				var li = document.createElement('li');
				li.textContent = er.texto;
				ul.appendChild(li);
			});
			alvo.classList.add('aqm-c3-oculto');
			barraLigada = false;
			mostrarBarra(false);
			return;
		}

		alvo.classList.remove('aqm-c3-oculto');

		el('aqm-c3-faixa-valor').innerHTML = lh(r.piso) + ' a ' + lh(r.teto) + '<span class="aqm-c3-unidade">L/h</span>';
		el('aqm-c3-faixa-criterio').textContent =
			'Do piso ao teto: ' + fmt(FABRICANTE_XH, 2) + ' renovações por hora, que é o que o próprio fabricante dimensiona, até '
			+ fmt(r.teto_xh, 0) + ' renovações por hora, que é o teto da regra de bolso brasileira para aquário '
			+ (r.entradas.perfil === 'plantado' ? 'plantado' : 'comunitário') + '. '
			+ 'A faixa é larga porque as fontes discordam em ' + fmt(r.razao, 1) + ' vezes — e essa discordância é o resultado, não um defeito dele.';

		var lista = el('aqm-c3-bandas');
		lista.innerHTML = '';

		lista.appendChild(cartao(
			'Piso do fabricante',
			lh(r.piso) + '<span class="aqm-c3-unidade">L/h</span>',
			'O Eheim classic 250 (2213) declara 440 L/h para aquários de até 250 L: são ' + fmt(FABRICANTE_XH, 2)
			+ ' renovações por hora. Aplicado ao seu volume, dá este número. É o único extremo da faixa que vem de quem fabrica o filtro.'
		));

		r.bandas.forEach(function (b) {
			lista.appendChild(cartao(
				b.rotulo + ' (' + fmt(b.xh[0], 0) + ' a ' + fmt(b.xh[1], 0) + ' x/h)',
				lh(b.min) + ' a ' + lh(b.max) + '<span class="aqm-c3-unidade">L/h</span>',
				'Regra repetida por ' + b.fonte + ', do nosso levantamento de setembro de 2026. '
				+ 'Nenhuma das fontes brasileiras explica de onde saiu o número nem confronta o dimensionamento do fabricante.'
			));
		});

		if (r.sump_L) {
			lista.appendChild(cartao(
				'Volume mínimo do sump',
				litros(r.sump_L) + '<span class="aqm-c3-unidade">L</span>',
				SUMP_PCT + ' % do volume do aquário, mínimo repetido pela AquaOnline. É a única constante de sump que o levantamento trouxe: '
				+ 'turnover de aquário marinho não tem fonte no nosso corpus, então esta calculadora não publica um.'
			));
		}

		var pos = { leve: ['o piso', r.bolso.min], media: ['o meio', (r.bolso.min + r.bolso.max) / 2], pesada: ['o topo', r.bolso.max] };
		var escolha = pos[r.entradas.carga] || pos.media;
		el('aqm-c3-carga-nota').innerHTML =
			'<strong>Com a carga de peixes que você informou, mire ' + escolha[0] + ' da faixa de bolso: cerca de '
			+ lh(escolha[1]) + ' L/h.</strong> Onde mirar dentro de uma faixa publicada é convenção da Aquametria, não constante com fonte — '
			+ 'os números dos extremos têm origem; a posição dentro deles é critério editorial, e está declarado.';

		var av = el('aqm-c3-avisos');
		av.innerHTML = '';
		(r.avisos || []).forEach(function (t) {
			var li = document.createElement('li');
			li.textContent = t;
			av.appendChild(li);
		});

		pintarProdutos(r);

		el('aqm-c3-citacao').textContent =
			'Aquário de ' + litros(r.entradas.volume) + ' L de água real, perfil '
			+ (r.entradas.perfil === 'plantado' ? 'plantado' : 'comunitário') + ': a vazão de filtro pedida vai de '
			+ lh(r.piso) + ' a ' + lh(r.teto) + ' L/h, conforme a fonte — ' + fmt(FABRICANTE_XH, 2)
			+ ' renovações por hora pelo dimensionamento do fabricante, até ' + fmt(r.teto_xh, 0)
			+ ' pela regra de bolso brasileira. Calculado pela Aquametria, ' + AQM_C3_DATA + '.';

		guardar(r);
		atualizarEndereco(r.entradas);
		armarBarra(r);
	}

	function cartao(rotulo, valor, criterio) {
		var li = document.createElement('li');
		li.className = 'aqm-c3-cartao';
		var r = document.createElement('span');
		r.className = 'aqm-c3-rotulo';
		r.textContent = rotulo;
		var v = document.createElement('span');
		v.className = 'aqm-c3-valor';
		v.innerHTML = valor;
		var c = document.createElement('p');
		c.className = 'aqm-c3-criterio';
		c.textContent = criterio;
		li.appendChild(r); li.appendChild(v); li.appendChild(c);
		return li;
	}

	/* ------------------------------------------------------------- produtos */

	function pintarProdutos(r) {
		var bloco = el('aqm-c3-produtos');
		var lista = el('aqm-c3-produtos-lista');
		var nada = el('aqm-c3-produtos-nada');
		lista.innerHTML = '';

		pintarForaDoVolume(r);

		if (!r.produtos.length) {
			bloco.classList.add('aqm-c3-oculto');
			nada.classList.remove('aqm-c3-oculto');
			nada.textContent = 'Nenhum filtro do nosso banco atende ao mesmo tempo às duas condições do seu caso: '
				+ 'entregar entre ' + lh(r.piso) + ' e ' + lh(r.teto) + ' L/h e ter, do fabricante, declaração de volume que cubra '
				+ litros(r.entradas.volume) + ' L'
				+ (r.entradas.tipo !== 'qualquer' ? ', no tipo que você escolheu' : '')
				+ (r.barrados_por_coluna.length ? '. ' + r.barrados_por_coluna.length + ' modelo(s) foram barrados pela altura da coluna' : '')
				+ (r.fora_do_volume.length ? '. ' + r.fora_do_volume.length + ' modelo(s) atendem a vazão mas o fabricante não cobre esse volume, e estão listados logo abaixo' : '')
				+ '. O banco tem ' + AQM_C3_CATALOGO.length + ' filtro(s) com ficha completa hoje e cresce a cada coleta. '
				+ 'Preferimos não mostrar produto nenhum a mostrar um que não atende o seu número.';
			return;
		}

		nada.classList.add('aqm-c3-oculto');
		bloco.classList.remove('aqm-c3-oculto');
		el('aqm-c3-produtos-sub').textContent =
			'São os filtros do nosso banco que passam nas DUAS condições: a vazão declarada cai dentro da faixa que o seu aquário pede — '
			+ lh(r.piso) + ' a ' + lh(r.teto) + ' L/h — e o volume que o fabricante declara cobre os '
			+ litros(r.entradas.volume) + ' L que você informou. Quem não declara volume nenhum entra também, e o cartão diz isso. '
			+ 'A ordem é por proximidade do meio da faixa; entre modelos tecnicamente equivalentes (mesmo décimo da faixa), '
			+ 'quem tem link de loja aparece antes. Comissão não é comparada em lugar nenhum, e produto sem link de loja aparece do mesmo jeito.';

		/* A vitrine vem ANTES da ficha e antes da procedência: contrato 7. */
		pintarVitrine(r);

		r.produtos.forEach(function (p) {
			lista.appendChild(produtoHtml(p, r));
		});

		if (r.barrados_por_coluna.length) {
			var li = document.createElement('li');
			li.className = 'aqm-c3-criterio';
			li.textContent = 'Fora da lista pela coluna: ' + r.barrados_por_coluna.join(' ');
			lista.appendChild(li);
		}
	}

	/* A seção separada. Ela vem SEMPRE depois dos recomendados no HTML e no
	   sentido: são filtros que a faixa aceita e que a declaração do fabricante
	   não cobre. Some quando não há nenhum. */
	function pintarForaDoVolume(r) {
		var bloco = el('aqm-c3-fora');
		var lista = el('aqm-c3-fora-lista');
		lista.innerHTML = '';

		if (!r.fora_do_volume || !r.fora_do_volume.length) {
			bloco.classList.add('aqm-c3-oculto');
			return;
		}

		bloco.classList.remove('aqm-c3-oculto');
		el('aqm-c3-fora-sub').textContent =
			'Estes entregam a vazão que o seu aquário pede, mas o fabricante declara um volume atendido que não inclui os '
			+ litros(r.entradas.volume) + ' L que você informou. Não são recomendação: estão aqui porque você pode encontrá-los '
			+ 'por aí com essa vazão e merece saber por que a Aquametria não os coloca na lista de cima.';

		r.fora_do_volume.forEach(function (p) {
			lista.appendChild(produtoHtml(p, r, true));
		});
	}

	function produtoHtml(p, r, foraDoVolume) {
		var V = r.entradas.volume;
		var turno = p.vazao_lh / V;

		var li = document.createElement('li');
		li.className = 'aqm-c3-produto';

		var placa = document.createElement('div');
		placa.className = 'aqm-c3-placa';
		placa.innerHTML = '<span class="aqm-c3-marca">' + esc(p.marca) + '</span>'
			+ '<span class="aqm-c3-numero">' + lh(p.vazao_lh) + '</span>'
			+ '<span class="aqm-c3-un">L/h nominais</span>';

		var corpo = document.createElement('div');

		var h = document.createElement('h4');
		h.textContent = nomeProduto(p);
		corpo.appendChild(h);

		var porque = document.createElement('p');
		porque.className = 'aqm-c3-porque';
		porque.innerHTML = 'No seu aquário de ' + litros(V) + ' L, este filtro entrega <strong>'
			+ fmt(Math.round(turno * 10) / 10, 1) + ' renovações por hora</strong>. ' + textoVolume(p, V, foraDoVolume);
		corpo.appendChild(porque);

		var ficha = document.createElement('ul');
		ficha.className = 'aqm-c3-ficha';
		var linhas = [
			'Tipo: <b>' + esc(p.tipo) + '</b>',
			'Potência: <b>' + fmt(p.potencia_w, 0) + ' W</b>',
			(p.coluna_na
				? 'Coluna máxima: <b>não se aplica</b> (hang-on fica na borda do aquário)'
				: (p.coluna_m !== null ? 'Coluna máxima: <b>' + fmt(p.coluna_m, 1) + ' m</b>' : 'Coluna máxima: <b>não declarada</b>')),
			'Voltagem: <b>' + (p.voltagem.length ? p.voltagem.join(' ou ') + ' V' : 'não declarada') + '</b>'
		];
		if (p.uv_w) { linhas.push('UV embutido: <b>' + fmt(p.uv_w, 0) + ' W</b>'); }
		if (p.midia.length) { linhas.push('Mídia inclusa: ' + esc(p.midia.join(', '))); }
		linhas.push('Ficha conferida em ' + esc(dataBr(p.verificado_em))
			+ (p.fonte_url ? ' — <a href="' + esc(p.fonte_url) + '" target="_blank" rel="noopener nofollow">fonte da especificação</a>' : '')
			+ (p.fonte_status ? ' (' + esc(p.fonte_status) + ')' : ''));
		ficha.innerHTML = linhas.map(function (t) { return '<li>' + t + '</li>'; }).join('');
		corpo.appendChild(ficha);

		if (p.link) {
			var a = document.createElement('a');
			a.className = 'aqm-c3-loja';
			a.href = p.link;
			a.target = '_blank';
			a.rel = 'sponsored noopener';
			a.textContent = 'Ver na ' + (p.loja === 'shopee' ? 'Shopee' : p.loja);
			corpo.appendChild(a);
			var nota = document.createElement('p');
			nota.className = 'aqm-c3-semloja';
			nota.textContent = 'Link patrocinado. Confira no anúncio a voltagem e o modelo exato antes de comprar — '
				+ 'o anúncio não é nossa fonte técnica, e a ficha acima é.';
			corpo.appendChild(nota);
		} else {
			var sem = document.createElement('p');
			sem.className = 'aqm-c3-semloja';
			sem.textContent = 'Ainda não temos link de loja para este modelo. Ele aparece aqui porque atende ao seu número — '
				+ 'quem entra na lista é decidido pela ficha técnica, e nunca por ter ou não link. O link só desempata entre modelos tecnicamente equivalentes.';
			corpo.appendChild(sem);
		}

		li.appendChild(placa);
		li.appendChild(corpo);
		return li;
	}

	/* ------------------------------------------------------------- vitrine */

	/* Espelho de aquametria_c3_preco_texto(). Cotação com data, nunca preço
	   atual: é o que a seção 7 do contrato permite publicar. */
	function precoTexto(p) {
		if (!p.preco || p.preco.min === null || p.preco.min === undefined) { return ''; }
		var valor = 'R$ ' + fmt(p.preco.min, 2);
		if (p.preco.max > p.preco.min) { valor += ' a R$ ' + fmt(p.preco.max, 2); }
		return valor + (p.preco.loja ? ' na ' + p.preco.loja : '')
			+ ', cotado em ' + dataBr(p.preco.coletado_em);
	}

	/* Espelho de aquametria_c3_modelo_curto(): o cartão já tem linha de marca, e
	   repeti-la no modelo é a cara de cartão gerado por máquina que ninguém leu. */
	function modeloCurto(p) {
		var modelo = p.modelo;
		if (p.voltagem && p.voltagem.length === 1) { modelo += ' (' + p.voltagem[0] + ' V)'; }
		return modelo;
	}

	/* Espelho de aquametria_c3_espec_frase(): a especificação que fez o produto
	   entrar, no tamanho de um cartão. */
	function especFrase(p, V) {
		return lh(p.vazao_lh) + ' L/h — atende os ' + litros(V) + ' L do seu aquário';
	}

	/* Espelho de aquametria_c3_vitrine_cartao_html(). Mesma marcação, mesmo CSS —
	   duas marcações para o mesmo cartão viram duas aparências. */
	function vitrineCartao(p, V) {
		var li = document.createElement('li');
		li.className = 'aqm-c3-vt-item';

		var cartao;
		if (p.link) {
			cartao = document.createElement('a');
			cartao.className = 'aqm-c3-vt-cartao';
			cartao.href = p.link;
			cartao.target = '_blank';
			cartao.rel = 'sponsored noopener';
		} else {
			/* Sem link não existe destino, e cartão sem destino não é âncora. O
			   que o contrato proíbe é div com onclick fingindo ser link. */
			cartao = document.createElement('div');
			cartao.className = 'aqm-c3-vt-cartao aqm-c3-vt-sem-link';
		}

		var foto = document.createElement('span');
		if (p.imagem && p.imagem.url) {
			foto.className = 'aqm-c3-vt-foto';
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
			foto.className = 'aqm-c3-vt-foto aqm-c3-vt-foto-vazia';
			foto.setAttribute('aria-hidden', 'true');
			var sigla = document.createElement('span');
			sigla.className = 'aqm-c3-vt-sigla';
			sigla.textContent = p.marca;
			foto.appendChild(sigla);
		}
		cartao.appendChild(foto);

		cartao.appendChild(linha('aqm-c3-vt-marca', p.marca));
		cartao.appendChild(linha('aqm-c3-vt-modelo', modeloCurto(p)));
		cartao.appendChild(linha('aqm-c3-vt-espec', especFrase(p, V)));

		var preco = precoTexto(p);
		cartao.appendChild(preco
			? linha('aqm-c3-vt-preco', preco)
			: linha('aqm-c3-vt-preco aqm-c3-vt-sem-preco', 'sem cotação coletada'));

		if (p.link) {
			cartao.appendChild(linha('aqm-c3-vt-botao', 'Ver na ' + (p.loja === 'shopee' ? 'Shopee' : p.loja)));
			cartao.appendChild(linha('aqm-c3-vt-selo', 'link patrocinado'));
		} else {
			cartao.appendChild(linha('aqm-c3-vt-espera', 'link de loja em breve'));
			cartao.appendChild(linha('aqm-c3-vt-selo', 'entrou pela ficha técnica, não pelo link'));
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

	function pintarVitrine(r) {
		var bloco = el('aqm-c3-vitrine');
		var trilho = el('aqm-c3-vitrine-trilho');
		trilho.innerHTML = '';

		if (!r.produtos.length) {
			bloco.classList.add('aqm-c3-oculto');
			return;
		}

		bloco.classList.remove('aqm-c3-oculto');

		var comLink = 0;
		r.produtos.forEach(function (p) {
			if (p.link) { comLink += 1; }
			trilho.appendChild(vitrineCartao(p, r.entradas.volume));
		});

		el('aqm-c3-vitrine-nota').textContent = comLink + ' de ' + r.produtos.length
			+ ' têm link de loja hoje; os outros aparecem do mesmo jeito, com o lugar do botão reservado — '
			+ 'quem entra é decidido pela ficha técnica, e nunca por ter ou não link.';
	}

	/* ------------------------------------------------- rolagem e barra fixa */

	/* Rola até o resultado, e SÓ quando ele não está à vista. Rolar uma página
	   em que a resposta já está na tela é tirar o leitor do lugar em que ele
	   está — o que a regra pede é não deixar ninguém calculando no escuro. */
	function irParaResultado() {
		var alvo = el('aqm-c3-saida');
		if (!alvo || alvo.classList.contains('aqm-c3-oculto')) { return; }

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
		var barra = el('aqm-c3-barra');
		if (!barra) { return; }

		el('aqm-c3-barra-texto').textContent = lh(r.piso) + ' a ' + lh(r.teto) + ' L/h para '
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
		observador.observe(el('aqm-c3-saida'));
	}

	function mostrarBarra(ver) {
		var barra = el('aqm-c3-barra');
		if (!barra) { return; }
		barra.classList.toggle('aqm-c3-barra-ver', !!ver);
		barra.setAttribute('aria-hidden', ver ? 'false' : 'true');
	}

	/* A frase de volume declarado, em um lugar só, porque ela é o que separa um
	   recomendado de um listado à parte — e uma página que diz duas coisas sobre
	   isso perde a única coisa que ela tem de valioso, que é ser confiável. */
	function textoVolume(p, V, foraDoVolume) {
		if (p.volume_max_L === null && p.volume_min_L === null) {
			return 'O fabricante não declara volume atendido para este modelo: ele entra pela vazão, '
				+ 'e não há declaração de volume para conferir contra os ' + litros(V) + ' L do seu aquário.';
		}

		if (!foraDoVolume) {
			return 'O fabricante declara que ele atende '
				+ (p.volume_min_L !== null ? 'de ' + litros(p.volume_min_L) + ' a ' : 'até ')
				+ litros(p.volume_max_L !== null ? p.volume_max_L : V) + ' L — o seu volume cabe nessa declaração.';
		}

		if (p.volume_max_L !== null && V > p.volume_max_L) {
			return '<strong>O fabricante declara este modelo para até ' + litros(p.volume_max_L)
				+ ' L, abaixo dos ' + litros(V) + ' L do seu aquário.</strong> A vazão cabe na faixa; a declaração de volume não cobre o seu caso, '
				+ 'e por isso ele não está na lista de recomendados.';
		}

		return '<strong>O fabricante declara este modelo a partir de ' + litros(p.volume_min_L)
			+ ' L, acima dos ' + litros(V) + ' L do seu aquário.</strong> A vazão cabe na faixa; a declaração de volume não cobre o seu caso, '
			+ 'e por isso ele não está na lista de recomendados.';
	}

	/* Espelho de aquametria_c3_nome_produto(): o banco separa por voltagem quando
	   cada anúncio vende uma versão só, e sem isso a lista mostra dois itens de
	   nome idêntico. */
	function nomeProduto(p) {
		var nome = p.marca + ' ' + p.modelo;
		if (p.voltagem && p.voltagem.length === 1) { nome += ' (' + p.voltagem[0] + ' V)'; }
		return nome;
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
	   pode apagar o que ela gravou. Só acrescenta o que é dela. */
	function guardar(r) {
		var estado = recuperar() || { versao: 1, calculadora: 'c3-vazao-filtro' };
		estado.volumes = estado.volumes || {};
		if (!estado.volumes.real_L || estado.volumes.real_L !== r.entradas.volume) {
			estado.volumes.real_L = r.entradas.volume;
			if (!estado.volumes.origem) { estado.volumes.origem = 'informado na C3'; }
		}
		estado.perfil = estado.perfil || {};
		estado.perfil.tipo_aquario = r.entradas.perfil;
		estado.perfil.carga_peixes = r.entradas.carga;
		estado.perfil.tem_sump = !!r.entradas.sump;
		estado.equipamentos = estado.equipamentos || {};
		estado.equipamentos.filtro_coluna_m = r.entradas.coluna;
		estado.equipamentos.filtro_vazao_alvo_lh = [Math.round(r.piso), Math.round(r.teto)];
		estado.calculado_em = new Date().toISOString().slice(0, 10);

		try {
			window.localStorage.setItem(CHAVE, JSON.stringify(estado));
			el('aqm-c3-guardado').classList.remove('aqm-c3-oculto');
		} catch (erro) {
			el('aqm-c3-guardado').classList.add('aqm-c3-oculto');
		}
	}

	/* ------------------------------------------- permalink e query string */

	function atualizarEndereco(d) {
		var q = ['v=' + d.volume, 'p=' + d.perfil, 'cg=' + d.carga, 't=' + d.tipo];
		if (d.coluna !== null) { q.push('col=' + d.coluna); }
		if (d.sump) { q.push('sump=1'); }
		var url = window.location.pathname + '?' + q.join('&');
		try { window.history.replaceState(null, '', url); } catch (erro) { /* sem history: segue sem permalink */ }
		el('aqm-c3-link').value = window.location.origin + url;
	}

	function lerQuery() {
		var busca = window.location.search;
		if (!busca || busca.length < 2) { return null; }
		var fora = {};
		busca.substring(1).split('&').forEach(function (par) {
			var p = par.split('=');
			if (p.length === 2) { fora[decodeURIComponent(p[0])] = decodeURIComponent(p[1]); }
		});
		return fora.v ? fora : null;
	}

	/* ------------------------------------- o filtro que a pessoa já tem */

	function veredito() {
		var q = num(el('aqm-c3-tenho').value);
		var V = num(el('aqm-c3-volume').value);
		var saida = el('aqm-c3-tenho-saida');

		if (q === null || q <= 0) {
			saida.textContent = 'Informe a vazão nominal do filtro, em litros por hora — é o número que vem na caixa.';
			return;
		}

		var texto = 'Um filtro de ' + lh(q) + ' L/h cobre ';
		var partes = [];
		partes.push('até ' + litros(q / FABRICANTE_XH) + ' L pelo dimensionamento do fabricante (' + fmt(FABRICANTE_XH, 2) + ' x/h)');
		var perfil = el('aqm-c3-perfil').value === 'plantado' ? 'plantado' : 'comunitario';
		BANDAS[perfil].forEach(function (b) {
			partes.push('de ' + litros(q / b.faixa[1]) + ' a ' + litros(q / b.faixa[0]) + ' L pela ' + b.curto
				+ ' (' + fmt(b.faixa[0], 0) + ' a ' + fmt(b.faixa[1], 0) + ' x/h)');
		});
		texto += partes.join('; ') + '. ';

		if (V !== null && V > 0) {
			var t = q / V;
			texto += 'No seu aquário de ' + litros(V) + ' L, ele entrega ' + fmt(Math.round(t * 10) / 10, 1) + ' renovações por hora — '
				+ (t < FABRICANTE_XH
					? 'abaixo até do que o fabricante do 2213 considera suficiente.'
					: (t < BANDAS[perfil][BANDAS[perfil].length - 1].faixa[0]
						? 'acima do dimensionamento do fabricante e abaixo do que as regras de bolso brasileiras pedem. É exatamente a faixa onde as fontes discordam.'
						: 'dentro do que as regras de bolso brasileiras pedem.'));
		}
		texto += ' Vazão nominal é medida sem mídia e a coluna zero: no seu aquário, com o cesto cheio, chega menos que isso.';
		saida.textContent = texto;
	}

	/* ---------------------------------------------------------- ligações */

	function preencher(fora) {
		if (fora.v) { el('aqm-c3-volume').value = fora.v; }
		if (fora.p === 'plantado' || fora.p === 'comunitario') { el('aqm-c3-perfil').value = fora.p; }
		if (fora.cg) { el('aqm-c3-carga').value = fora.cg; }
		if (fora.t) { el('aqm-c3-tipo').value = fora.t; }
		if (fora.col) { el('aqm-c3-coluna').value = fora.col; }
		if (fora.sump === '1') { el('aqm-c3-sump').checked = true; }
	}

	el('aqm-c3-form').addEventListener('submit', function (ev) {
		ev.preventDefault();
		pintar(calcular(campos()));
		/* Só no envio explícito. A pintura automática de quem chegou por link ou
		   com o aquário guardado NÃO rola a página: sequestrar a rolagem de quem
		   acabou de abrir a página é o oposto de ajudar. */
		irParaResultado();
	});

	el('aqm-c3-limpar').addEventListener('click', function () {
		el('aqm-c3-form').reset();
		el('aqm-c3-saida').classList.add('aqm-c3-oculto');
		el('aqm-c3-erros').innerHTML = '';
		barraLigada = false;
		mostrarBarra(false);
		try { window.history.replaceState(null, '', window.location.pathname); } catch (erro) { /* segue */ }
	});

	el('aqm-c3-barra-ir').addEventListener('click', function () {
		var alvo = el('aqm-c3-saida');
		if (!alvo || alvo.classList.contains('aqm-c3-oculto')) { return; }
		try {
			alvo.scrollIntoView({ block: 'start' });
		} catch (erro) {
			alvo.scrollIntoView();
		}
	});

	el('aqm-c3-copiar').addEventListener('click', function () {
		var campo = el('aqm-c3-link');
		campo.select();
		var ok = false;
		try { ok = document.execCommand('copy'); } catch (erro) { ok = false; }
		if (!ok && window.navigator && window.navigator.clipboard) {
			window.navigator.clipboard.writeText(campo.value);
			ok = true;
		}
		el('aqm-c3-copiado').textContent = ok ? 'Link copiado.' : 'Selecione e copie o endereço acima.';
	});

	el('aqm-c3-tenho-calcular').addEventListener('click', veredito);

	/* Query string manda; senão, o aquário que a C1 guardou neste navegador. */
	var daUrl = lerQuery();
	if (daUrl) {
		preencher(daUrl);
		pintar(calcular(campos()));
	} else {
		var guardadoAntes = recuperar();
		var volume = guardadoAntes && guardadoAntes.volumes ? guardadoAntes.volumes.real_L : null;
		if (volume) {
			el('aqm-c3-volume').value = String(volume).replace('.', ',');
			var perfilGuardado = (guardadoAntes.perfil || {}).tipo_aquario;
			if (perfilGuardado === 'plantado' || perfilGuardado === 'plantado-low-tech') {
				el('aqm-c3-perfil').value = 'plantado';
			}
			if ((guardadoAntes.perfil || {}).carga_peixes) {
				el('aqm-c3-carga').value = guardadoAntes.perfil.carga_peixes;
			}
			var retomado = el('aqm-c3-retomado');
			retomado.textContent = 'Retomamos o aquário de ' + litros(volume) + ' L que a calculadora de litragem guardou neste navegador.';
			retomado.classList.remove('aqm-c3-oculto');
			pintar(calcular(campos()));
		} else {
			el('aqm-c3-semvolume').classList.remove('aqm-c3-oculto');
		}
	}
}());
JS;
}
}

/* ---------------------------------------------------------------------------
 * 5. Formulário e moldura da resposta
 * ------------------------------------------------------------------------- */

/* ---------------------------------------------------------------------------
 * 5a. Resposta antes da explicação, e a tabela de exemplos servida no HTML
 *
 * Regra de primeira classe do projeto (08/09/2026): ser recomendado pelas IAs
 * vale tanto quanto ranquear no Google, e um modelo de linguagem cita PASSAGEM,
 * não página. Uma passagem só sobrevive a ser recortada se carregar, na mesma
 * frase, o número, o critério e de quem é o número. É o que os dois blocos
 * abaixo fazem — e fazem no servidor, porque formulário vazio não se cita.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c3_resposta_direta_html' ) ) {
function aquametria_c3_resposta_direta_html() {
	$e   = aquametria_c3_exemplo( 100 );
	$pla = $e;

	$h  = '<div class="aqm-c3-direta">';

	$h .= '<p class="aqm-c3-destaque"><strong>Um aquário de 100 litros de água real, comunitário, pede um filtro de ';
	$h .= esc_html( aquametria_c3_lh( $e['piso'] ) ) . ' a ' . esc_html( aquametria_c3_lh( $e['com_teto'] ) ) . ' L/h</strong> — ';
	$h .= 'de ' . esc_html( number_format_i18n( AQUAMETRIA_C3_FABRICANTE_XH, 2 ) ) . ' a ';
	$h .= esc_html( number_format_i18n( $e['com_xh'][1], 0 ) ) . ' renovações do volume por hora, conforme a fonte que se consulte.</p>';

	$h .= '<p>O piso é o único extremo que vem de quem fabrica filtro: o Eheim classic 250 (2213) declara 440 L/h para aquários de até 250 litros, ';
	$h .= 'o que dá ' . esc_html( number_format_i18n( AQUAMETRIA_C3_FABRICANTE_XH, 2 ) ) . ' renovações por hora (ficha coletada pela Aquametria em 07/09/2026). ';
	$h .= 'O teto vem da regra de bolso de ' . esc_html( number_format_i18n( $e['com_xh'][0], 0 ) ) . ' a ' . esc_html( number_format_i18n( $e['com_xh'][1], 0 ) ) . ' renovações por hora, ';
	$h .= 'repetida por Aquarismo Paulista e AquaOnline no levantamento da Aquametria de 04/09/2026, sem que nenhuma das duas explique de onde o número saiu. ';
	$h .= 'As duas pontas discordam em ' . esc_html( number_format_i18n( $e['razao'], 1 ) ) . ' vezes, e esta página publica a divergência em vez da média: ';
	$h .= 'média entre fontes que discordam não é dado, é opinião com cara de número.</p>';

	$h .= '<p>Para aquário plantado a faixa é mais lenta — de ' . esc_html( aquametria_c3_lh( $pla['piso'] ) ) . ' a ';
	$h .= esc_html( aquametria_c3_lh( $pla['pla_teto'] ) ) . ' L/h nos mesmos 100 litros, ou seja até ';
	$h .= esc_html( number_format_i18n( $pla['pla_xh'][1], 0 ) ) . ' renovações por hora, segundo o AquaPeixes (levantamento de 04/09/2026): ';
	$h .= 'planta quer corrente suave e superfície pouco agitada, para o CO2 não escapar. ';
	$h .= 'Para aquário marinho esta calculadora não publica número nenhum, porque o nosso levantamento não trouxe turnover de marinho com fonte — e constante sem origem é proibida aqui.</p>';

	$h .= '<p class="aqm-c3-criterio">Um aviso que vale para as duas faixas e que quase nenhuma página faz: ';
	$h .= '<strong>vazão nominal não é a vazão que chega ao seu aquário.</strong> O número da caixa é medido sem mídia no cesto e com a bomba na altura da água. ';
	$h .= 'Quanto se perde, não publicamos: não existe fator de perda com fonte no nosso levantamento. Existe medição sua, e ela está mais abaixo, no protocolo do balde.</p>';

	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c3_exemplos_html' ) ) {
function aquametria_c3_exemplos_html() {
	$h  = '<div class="aqm-c3-painel aqm-c3-exemplos">';
	$h .= '<h3>Seis aquários já resolvidos</h3>';
	$h .= '<p class="aqm-c3-sub">Estes números estão prontos no HTML desta página: são a mesma conta que o formulário acima faz, ';
	$h .= 'aplicada aos seis volumes mais comuns do comércio brasileiro. Servem a quem não quer preencher nada e a quem lê esta página por máquina.</p>';

	$h .= '<div class="aqm-c3-rolagem"><table class="aqm-c3-fontes">';
	$h .= '<tr><th>Volume real de água</th><th>Comunitário</th><th>Mira com carga média</th><th>Plantado</th><th>Filtro do banco que atende</th></tr>';

	foreach ( aquametria_c3_volumes_exemplo() as $v ) {
		$e = aquametria_c3_exemplo( $v );

		$h .= '<tr>';
		$h .= '<td>' . esc_html( number_format_i18n( $e['volume'], 0 ) ) . ' L</td>';

		$h .= '<td><span class="aqm-c3-num">' . esc_html( aquametria_c3_lh( $e['piso'] ) ) . ' a ' . esc_html( aquametria_c3_lh( $e['com_teto'] ) ) . ' L/h</span>';
		$h .= '<span class="aqm-c3-xh">' . esc_html( number_format_i18n( AQUAMETRIA_C3_FABRICANTE_XH, 2 ) ) . ' a ';
		$h .= esc_html( number_format_i18n( $e['com_xh'][1], 0 ) ) . ' renovações/h</span></td>';

		$h .= '<td><span class="aqm-c3-num">' . esc_html( aquametria_c3_lh( $e['com_mira'] ) ) . ' L/h</span>';
		$h .= '<span class="aqm-c3-xh">meio da faixa de bolso</span></td>';

		$h .= '<td><span class="aqm-c3-num">' . esc_html( aquametria_c3_lh( $e['piso'] ) ) . ' a ' . esc_html( aquametria_c3_lh( $e['pla_teto'] ) ) . ' L/h</span>';
		$h .= '<span class="aqm-c3-xh">' . esc_html( number_format_i18n( AQUAMETRIA_C3_FABRICANTE_XH, 2 ) ) . ' a ';
		$h .= esc_html( number_format_i18n( $e['pla_xh'][1], 0 ) ) . ' renovações/h</span></td>';

		$h .= aquametria_c3_produto_celula_html( $e );

		$h .= '</tr>';
	}

	$h .= '</table></div>';

	$h .= '<p class="aqm-c3-criterio" style="margin-top:.8rem">O piso é o mesmo critério em todas as linhas: ';
	$h .= esc_html( number_format_i18n( AQUAMETRIA_C3_FABRICANTE_XH, 2 ) ) . ' renovações por hora, que é o que o Eheim classic 250 (2213) dimensiona quando declara 440 L/h para até 250 litros ';
	$h .= '(coletado em 07/09/2026). O teto do comunitário são 10 renovações por hora, topo da regra de bolso de Aquarismo Paulista e AquaOnline (04/09/2026); ';
	$h .= 'o do plantado são 5, do AquaPeixes (04/09/2026). A coluna do meio é convenção editorial declarada, não constante com fonte: ';
	$h .= 'é o meio da faixa de bolso, onde esta página manda mirar quando a carga de peixes é média. ';
	$h .= 'Nenhum número desta tabela foi digitado à mão — todos saem das mesmas constantes que a calculadora usa, calculados no servidor a cada carregamento.</p>';

	$divulgacao = function_exists( 'aquametria_casca_url_pagina' )
		? aquametria_casca_url_pagina( AQUAMETRIA_C3_PAGINA_AFILIADOS )
		: home_url( '/' . AQUAMETRIA_C3_PAGINA_AFILIADOS . '/' );

	$h .= '<p class="aqm-c3-aviso-afiliado"><strong>Sobre a última coluna.</strong> ';
	$h .= 'Ela mostra o filtro do banco técnico da Aquametria que passa nas duas condições daquela linha — vazão declarada dentro da faixa E ';
	$h .= 'volume do fabricante cobrindo o volume da linha — e, entre esses, o que cai mais perto do meio da faixa. ';
	$h .= 'É o mesmo critério que a calculadora acima aplica, e a comissão não entra nele: modelo sem link de loja aparece do mesmo jeito. ';
	$h .= 'Entre modelos tecnicamente equivalentes (mesmo décimo da largura da faixa), quem tem link de loja aparece antes — é desempate, não ordenação por comissão: ';
	$h .= 'taxa de comissão não é comparada em lugar nenhum e modelo pior nunca sobe por pagar mais. ';
	$h .= 'Quando o escolhido ainda não tem link de loja no banco, aparece embaixo, rotulada, a opção da MESMA faixa que já tem — o primeiro da mesma ordem, não o de maior comissão. ';
	$h .= 'A tabela não sabe duas coisas que o formulário pergunta: o tipo de filtro que você quer e a altura entre a bomba e a superfície da água. ';
	$h .= 'Por isso ela indica um só modelo por faixa, e a lista completa, já filtrada pelo seu caso, sai depois do cálculo. ';
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
 * Dois nós: WebApplication (o que esta ferramenta é, para quem cataloga
 * ferramentas) e FAQPage (as perguntas que esta página realmente responde no
 * HTML servido — cada resposta abaixo existe, com o mesmo número, na tabela de
 * exemplos acima; FAQPage que promete o que a página não mostra é lixo).
 * ------------------------------------------------------------------------- */

/* A frase de "onde comprar" da resposta do FAQ, quando quem atende melhor ainda
   não tem link. Fica separada porque ela só existe nesse caso, e escrever isso
   dentro do array do FAQ deixaria o array ilegível. */
if ( ! function_exists( 'aquametria_c3_faq_com_link' ) ) {
function aquametria_c3_faq_com_link( $e, $volume ) {
	$c = aquametria_c3_produto_com_link( $e['piso'], $e['com_teto'], $volume );

	if ( null === $c ) {
		return 'Nenhum filtro dessa faixa tem link de loja no banco da Aquametria hoje. ';
	}

	$ressalva = aquametria_c3_volume_ressalva( $c, $volume );

	return 'Esse modelo ainda não tem link de loja no banco; na mesma faixa, o primeiro que tem é o '
		. aquametria_c3_produto_frase( $c, $volume ) . '. ' . ( '' === $ressalva ? '' : $ressalva . ' ' );
}
}

if ( ! function_exists( 'aquametria_c3_jsonld_dados' ) ) {
function aquametria_c3_jsonld_dados() {
	$url = function_exists( 'aquametria_casca_url_pagina' )
		? aquametria_casca_url_pagina( AQUAMETRIA_C3_SLUG )
		: home_url( '/' . AQUAMETRIA_C3_SLUG . '/' );

	$editora = array(
		'@type' => 'Organization',
		'name'  => 'Aquametria',
		'url'   => home_url( '/' ),
	);

	$app = array(
		'@type'                  => 'WebApplication',
		'@id'                    => $url . '#calculadora',
		'name'                   => 'Calculadora de vazão do filtro de aquário',
		'alternateName'          => 'Aquametria C3 — vazão e renovações por hora',
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
		'softwareVersion' => AQUAMETRIA_C3_VERSAO,
		'description'     => 'Converte o volume real de água do aquário na faixa de vazão que o filtro precisa entregar, em litros por hora. '
			. 'A faixa vai de ' . number_format_i18n( AQUAMETRIA_C3_FABRICANTE_XH, 2 ) . ' renovações por hora, que é o dimensionamento do próprio fabricante '
			. '(Eheim classic 250, 440 L/h para até 250 L), até 10 renovações por hora, topo da regra de bolso brasileira. '
			. 'Publica a divergência entre as fontes em vez da média, e sugere filtros do banco técnico da Aquametria cuja vazão declarada cai dentro da faixa calculada.',
		'featureList' => array(
			'Faixa de vazão em L/h a partir do volume real de água',
			'Piso vindo do dimensionamento declarado pelo fabricante, não de regra de bolso',
			'Cada extremo da faixa com a fonte e a data ao lado',
			'Caminho inverso: até quantos litros cobre o filtro que você já tem',
			'Volume mínimo de sump, para quem tem ou vai ter',
			'Protocolo do balde para medir a vazão real, já com mídia e coluna',
			'Lista de filtros do banco técnico elegíveis pelas duas condições (vazão na faixa e volume declarado pelo fabricante), ordenada por adequação técnica, nunca por comissão',
			'Tabela pré-calculada para 30, 60, 100, 150, 200 e 300 litros',
			'Filtro do banco indicado para cada um desses seis volumes, já no HTML servido',
		),
		'publisher' => $editora,
		'isBasedOn' => 'Levantamento de fontes brasileiras da Aquametria, 04/09/2026, e fichas de fabricante coletadas em 07/09/2026',
	);

	$perguntas = array();
	foreach ( aquametria_c3_volumes_exemplo() as $v ) {
		$e = aquametria_c3_exemplo( $v );

		$perguntas[] = array(
			'@type' => 'Question',
			'name'  => 'Qual a vazão de filtro para um aquário de ' . number_format_i18n( $v, 0 ) . ' litros?',
			'acceptedAnswer' => array(
				'@type' => 'Answer',
				'text'  => 'Um aquário de ' . number_format_i18n( $v, 0 ) . ' litros de água real, comunitário, pede um filtro de '
					. aquametria_c3_lh( $e['piso'] ) . ' a ' . aquametria_c3_lh( $e['com_teto'] ) . ' L/h — de '
					. number_format_i18n( AQUAMETRIA_C3_FABRICANTE_XH, 2 ) . ' a ' . number_format_i18n( $e['com_xh'][1], 0 ) . ' renovações do volume por hora. '
					. 'O piso vem do fabricante: o Eheim classic 250 (2213) declara 440 L/h para até 250 L, ou seja '
					. number_format_i18n( AQUAMETRIA_C3_FABRICANTE_XH, 2 ) . ' renovações por hora (coletado em 07/09/2026). '
					. 'O teto vem da regra de bolso brasileira de ' . number_format_i18n( $e['com_xh'][0], 0 ) . ' a ' . number_format_i18n( $e['com_xh'][1], 0 )
					. ' renovações por hora, repetida por Aquarismo Paulista e AquaOnline (levantamento de 04/09/2026). '
					. 'Com carga de peixes média, mire o meio da faixa de bolso, cerca de ' . aquametria_c3_lh( $e['com_mira'] ) . ' L/h. '
					. 'Se o aquário for plantado, a faixa é mais lenta: ' . aquametria_c3_lh( $e['piso'] ) . ' a ' . aquametria_c3_lh( $e['pla_teto'] )
					. ' L/h, até ' . number_format_i18n( $e['pla_xh'][1], 0 ) . ' renovações por hora, segundo o AquaPeixes. '
					. 'Vazão nominal é medida sem mídia e a coluna zero, então a que chega ao aquário é menor.',
			),
		);
	}

	/* Pergunta de COMPRA, uma por volume. Cada resposta abaixo existe, com o
	   mesmo modelo e o mesmo número, na última coluna da tabela servida — FAQPage
	   que promete o que a página não mostra é lixo, e é lixo detectável. */
	foreach ( aquametria_c3_volumes_exemplo() as $v ) {
		$e   = aquametria_c3_exemplo( $v );
		$p   = aquametria_c3_produto_exemplo( $e['piso'], $e['com_teto'], $v );

		if ( null === $p ) {
			continue;
		}

		$perguntas[] = array(
			'@type' => 'Question',
			'name'  => 'Qual filtro comprar para um aquário de ' . number_format_i18n( $v, 0 ) . ' litros?',
			'acceptedAnswer' => array(
				'@type' => 'Answer',
				'text'  => 'Para um aquário de ' . number_format_i18n( $v, 0 ) . ' litros de água real, o filtro do banco técnico da Aquametria que cai mais perto do meio da faixa é o '
					. aquametria_c3_produto_frase( $p, $v ) . '. '
					. 'A faixa que esse volume pede é de ' . aquametria_c3_lh( $e['piso'] ) . ' a ' . aquametria_c3_lh( $e['com_teto'] ) . ' L/h, '
					. 'e o critério é duplo: a vazão declarada dentro dessa faixa e o volume que o fabricante declara cobrindo os '
					. number_format_i18n( $v, 0 ) . ' litros. Nunca a comissão: modelo sem link de loja aparece na lista do mesmo jeito. '
					. aquametria_c3_volume_ressalva( $p, $v ) . ( aquametria_c3_volume_ressalva( $p, $v ) ? ' ' : '' )
					. ( $p['link'] ? '' : aquametria_c3_faq_com_link( $e, $v ) )
					. 'Antes de comprar, confira dois números que esta indicação não conhece: a voltagem da sua tomada e a altura entre a bomba e a superfície da água, '
					. 'porque vazão nominal é medida sem mídia no cesto e com a bomba na altura da água.',
			),
		);
	}

	$perguntas[] = array(
		'@type' => 'Question',
		'name'  => 'Quantas renovações por hora o filtro do aquário precisa fazer?',
		'acceptedAnswer' => array(
			'@type' => 'Answer',
			'text'  => 'Depende de quem responde, e a diferença é grande o bastante para ser o assunto. O fabricante dimensiona '
				. number_format_i18n( AQUAMETRIA_C3_FABRICANTE_XH, 2 ) . ' renovações por hora: o Eheim classic 250 (2213) declara 440 L/h para aquários de até 250 litros '
				. '(coletado em 07/09/2026). A web brasileira repete de 5 a 10 renovações por hora para aquário comunitário '
				. '(Aquarismo Paulista e AquaOnline, levantamento de 04/09/2026) e de 3 a 5 para plantado (AquaPeixes). '
				. 'São até 5,7 vezes de diferença, e nenhuma das fontes brasileiras explica a origem do número nem confronta o dimensionamento do fabricante. '
				. 'A Aquametria publica as duas pontas com o nome de quem as sustenta, em vez de publicar a média.',
		),
	);

	$perguntas[] = array(
		'@type' => 'Question',
		'name'  => 'A vazão que vem na caixa do filtro é a que chega ao aquário?',
		'acceptedAnswer' => array(
			'@type' => 'Answer',
			'text'  => 'Não. A vazão nominal do catálogo é medida com o filtro vazio, sem mídia no cesto, e com a bomba na altura da água. '
				. 'No móvel, com o cesto cheio e a mangueira subindo, chega menos. Quanto menos, a Aquametria não publica: '
				. 'não existe fator de perda de carga com fonte no nosso levantamento, e constante sem origem não entra. '
				. 'O que existe é medição própria: com o filtro ligado, aponte a saída para um balde de volume conhecido e cronometre. '
				. 'Vazão real em L/h é o volume do balde em litros dividido pelo tempo em horas — 10 litros em 45 segundos são 800 L/h.',
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

if ( ! function_exists( 'aquametria_c3_imprimir_jsonld' ) ) {
function aquametria_c3_imprimir_jsonld() {
	$json = wp_json_encode( aquametria_c3_jsonld_dados(), JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE );
	if ( ! $json ) {
		return;
	}
	echo '<script type="application/ld+json" id="aquametria-c3-jsonld">' . "\n" . $json . "\n" . '</script>' . "\n";
}
}

if ( ! function_exists( 'aquametria_c3_form_html' ) ) {
function aquametria_c3_form_html() {
	$c1 = function_exists( 'aquametria_casca_url_pagina' ) ? aquametria_casca_url_pagina( 'calculadora-de-litragem' ) : home_url( '/calculadora-de-litragem/' );

	$h  = '<form id="aqm-c3-form" class="aqm-c3-painel" novalidate>';
	$h .= '<h3>O seu aquário</h3>';
	$h .= '<p class="aqm-c3-sub">Se você já usou a calculadora de litragem neste navegador, o volume vem preenchido daqui. Nada é enviado para servidor nenhum.</p>';

	$h .= '<div class="aqm-c3-grade">';

	$h .= '<div class="aqm-c3-campo">';
	$h .= '<label for="aqm-c3-volume">Volume real de água (L)</label>';
	$h .= '<input type="text" inputmode="decimal" autocomplete="off" id="aqm-c3-volume" name="volume" placeholder="110">';
	$h .= '<span class="aqm-c3-dica">A água que está lá dentro, não o número da etiqueta.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c3-campo">';
	$h .= '<label for="aqm-c3-perfil">Perfil do aquário</label>';
	$h .= '<select id="aqm-c3-perfil" name="perfil">';
	$h .= '<option value="comunitario">comunitário (peixes, pouca planta)</option>';
	$h .= '<option value="plantado">plantado</option>';
	$h .= '</select>';
	$h .= '<span class="aqm-c3-dica">Marinho não está aqui: o nosso levantamento não trouxe turnover de marinho com fonte.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c3-campo">';
	$h .= '<label for="aqm-c3-carga">Carga de peixes</label>';
	$h .= '<select id="aqm-c3-carga" name="carga">';
	$h .= '<option value="leve">leve (poucos peixes pequenos)</option>';
	$h .= '<option value="media" selected>média</option>';
	$h .= '<option value="pesada">pesada (peixes grandes ou aquário cheio)</option>';
	$h .= '</select>';
	$h .= '<span class="aqm-c3-dica">Move a mira dentro da faixa, não a faixa.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c3-campo">';
	$h .= '<label for="aqm-c3-coluna">Altura da coluna (m)</label>';
	$h .= '<input type="text" inputmode="decimal" autocomplete="off" id="aqm-c3-coluna" name="coluna" placeholder="ex.: 0,8">';
	$h .= '<span class="aqm-c3-dica">Do filtro até a superfície da água. Só importa para canister e sump; em branco, não filtramos por coluna.</span>';
	$h .= '</div>';

	$h .= '<div class="aqm-c3-campo">';
	$h .= '<label for="aqm-c3-tipo">Tipo de filtro</label>';
	$h .= '<select id="aqm-c3-tipo" name="tipo">';
	$h .= '<option value="qualquer">tanto faz</option>';
	$h .= '<option value="canister">canister</option>';
	$h .= '<option value="hang-on">hang-on (cascata)</option>';
	$h .= '<option value="interno">interno</option>';
	$h .= '<option value="sump">sump</option>';
	$h .= '</select>';
	$h .= '<span class="aqm-c3-dica">Filtra a lista de produtos, não o cálculo.</span>';
	$h .= '</div>';

	$h .= '</div>';

	$h .= '<label class="aqm-c3-caixa"><input type="checkbox" id="aqm-c3-sump"> <span>Tenho ou vou ter sump — quero também o volume mínimo dele</span></label>';

	$h .= '<div class="aqm-c3-botoes">';
	$h .= '<button type="submit">Calcular a vazão</button>';
	$h .= '<button type="button" class="aqm-c3-secundario" id="aqm-c3-limpar">Limpar</button>';
	$h .= '<span class="aqm-c3-dica aqm-c3-oculto" id="aqm-c3-retomado"></span>';
	$h .= '</div>';
	$h .= '<ul class="aqm-c3-avisos" id="aqm-c3-erros"></ul>';
	$h .= '<p class="aqm-c3-criterio aqm-c3-oculto" id="aqm-c3-semvolume" style="margin-top:.9rem">';
	$h .= 'Não sabe o volume real? Ele não é o número da etiqueta: o vidro, a borda livre e as rochas tiram uma parte. ';
	$h .= 'A <a href="' . esc_url( $c1 ) . '">calculadora de litragem</a> devolve esse número a partir das medidas em centímetros e o guarda para esta página usar.</p>';
	$h .= '</form>';

	return $h;
}
}

if ( ! function_exists( 'aquametria_c3_resposta_html' ) ) {
function aquametria_c3_resposta_html() {
	$h  = '<div class="aqm-c3-resultado aqm-c3-oculto" id="aqm-c3-saida" aria-live="polite">';

	$h .= '<div class="aqm-c3-faixa">';
	$h .= '<span class="aqm-c3-rotulo">Vazão nominal que o seu aquário pede</span>';
	$h .= '<span class="aqm-c3-valor" id="aqm-c3-faixa-valor">—</span>';
	$h .= '<p class="aqm-c3-criterio" id="aqm-c3-faixa-criterio"></p>';
	$h .= '</div>';

	$h .= '<ul class="aqm-c3-cartoes" id="aqm-c3-bandas"></ul>';

	$h .= '<p class="aqm-c3-nota" id="aqm-c3-carga-nota"></p>';

	$h .= '<ul class="aqm-c3-avisos" id="aqm-c3-avisos"></ul>';

	$h .= '<p class="aqm-c3-nota aqm-c3-nota-alerta"><strong>Vazão nominal não é a vazão que chega ao seu aquário.</strong> ';
	$h .= 'O número da caixa é medido sem mídia dentro do filtro e com a bomba na altura da água. No seu móvel, com o cesto cheio e a mangueira subindo, chega menos. ';
	$h .= 'Quanto menos, nós não publicamos: não existe fator de perda com fonte no nosso levantamento, e constante sem origem é proibida aqui. ';
	$h .= 'O que existe é medição sua: com o filtro ligado, aponte a saída para um balde de volume conhecido e cronometre. Vazão real em L/h = volume do balde em litros ÷ tempo em horas — ';
	$h .= '10 litros em 45 segundos são 800 L/h. Vale mais que qualquer número de catálogo, inclusive o nosso.</p>';

	$h .= aquametria_c3_produtos_html();

	$h .= '<div class="aqm-c3-citar">';
	$h .= '<p id="aqm-c3-citacao"></p>';
	$h .= '<div class="aqm-c3-campo"><label for="aqm-c3-link">Link desta resposta</label>';
	$h .= '<input type="text" id="aqm-c3-link" readonly></div>';
	$h .= '<div class="aqm-c3-botoes"><button type="button" class="aqm-c3-secundario" id="aqm-c3-copiar">Copiar link</button>';
	$h .= '<span class="aqm-c3-dica" id="aqm-c3-copiado"></span></div>';
	$h .= '<p class="aqm-c3-dica" id="aqm-c3-guardado" style="margin-top:.4rem">Este aquário ficou guardado neste navegador para as próximas calculadoras.</p>';
	$h .= '</div>';

	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c3_produtos_html' ) ) {
function aquametria_c3_produtos_html() {
	$divulgacao = function_exists( 'aquametria_casca_url_pagina' )
		? aquametria_casca_url_pagina( AQUAMETRIA_C3_PAGINA_AFILIADOS )
		: home_url( '/' . AQUAMETRIA_C3_PAGINA_AFILIADOS . '/' );

	$h  = '<div class="aqm-c3-produtos aqm-c3-painel aqm-c3-oculto" id="aqm-c3-produtos">';
	$h .= '<h3>Filtros que atendem essa faixa</h3>';
	$h .= '<p class="aqm-c3-sub" id="aqm-c3-produtos-sub"></p>';

	/* A vitrine vem ANTES da ficha e da procedência (contrato 7): a prova de
	   onde veio o número fica, mas ela existe para ser conferida — não para ser
	   o único clique de compra da página. */
	$h .= '<div class="aqm-c3-vitrine aqm-c3-oculto" id="aqm-c3-vitrine">';
	$h .= '<h4>Onde comprar cada um</h4>';
	$h .= '<p class="aqm-c3-criterio">Mesma ordem da lista completa abaixo: elegibilidade técnica primeiro, '
		. 'adequação depois e o link de loja só como desempate entre equivalentes. '
		. 'O valor de cada cartão é cotação com data, não preço de hoje.</p>';
	$h .= '<ul class="aqm-c3-vt-trilho" id="aqm-c3-vitrine-trilho"></ul>';
	$h .= '<p class="aqm-c3-criterio" id="aqm-c3-vitrine-nota"></p>';
	$h .= '</div>';

	$h .= '<ul class="aqm-c3-lista" id="aqm-c3-produtos-lista"></ul>';
	$h .= '<p class="aqm-c3-aviso-afiliado"><strong>Aviso de publicidade.</strong> ';
	$h .= 'Alguns dos botões acima levam a lojas por links de afiliado: se você comprar por eles, a Aquametria pode receber uma comissão, sem custo nenhum a mais para você. ';
	$h .= 'Isso não muda quem aparece na lista: quem entra é decidido pela ficha técnica — vazão dentro da faixa que o seu aquário pede E volume declarado pelo fabricante cobrindo o seu volume —, e modelo sem link aparece do mesmo jeito. ';
	$h .= 'Na ordem, o link tem um papel só: desempatar entre modelos tecnicamente equivalentes, isto é, que caem no mesmo décimo da faixa. ';
	$h .= 'Taxa de comissão não é comparada em lugar nenhum, e modelo pior nunca sobe por pagar mais. ';
	$h .= 'A ficha técnica de cada filtro vem do fabricante ou do varejo especializado, com o endereço e a data ao lado; o anúncio da loja nunca é a nossa fonte. ';
	$h .= 'O valor que aparece nos cartões da vitrine <strong>não é preço de hoje</strong>: é a cotação que a Aquametria leu naquele anúncio na data escrita ao lado. ';
	$h .= 'Preço de aquarismo muda toda semana — confira no anúncio antes de comprar, e trate o nosso número como ordem de grandeza, não como promessa. ';
	$h .= '<a href="' . esc_url( $divulgacao ) . '">Como a Aquametria ganha dinheiro</a>.</p>';
	$h .= '</div>';
	$h .= '<p class="aqm-c3-nota aqm-c3-oculto" id="aqm-c3-produtos-nada"></p>';

	/* Seção SEPARADA, abaixo e rotulada: quem atende a vazão e o fabricante não
	   cobre o volume. Ela nunca se mistura com os recomendados — foi exatamente
	   essa mistura o defeito visto no ar em 09/09/2026. */
	$h .= '<div class="aqm-c3-produtos aqm-c3-fora aqm-c3-painel aqm-c3-oculto" id="aqm-c3-fora">';
	$h .= '<h3>Atendem a vazão, mas o fabricante não cobre esse volume</h3>';
	$h .= '<p class="aqm-c3-sub" id="aqm-c3-fora-sub"></p>';
	$h .= '<ul class="aqm-c3-lista" id="aqm-c3-fora-lista"></ul>';
	$h .= '</div>';

	return $h;
}
}

if ( ! function_exists( 'aquametria_c3_tenho_html' ) ) {
function aquametria_c3_tenho_html() {
	$h  = '<div class="aqm-c3-painel">';
	$h .= '<h3>Caminho inverso: o filtro que eu já tenho serve?</h3>';
	$h .= '<p class="aqm-c3-sub">Informe a vazão que vem na caixa e devolvemos até quantos litros ele cobre por cada critério — e, se o volume estiver preenchido acima, quantas renovações por hora ele entrega no seu aquário.</p>';
	$h .= '<div class="aqm-c3-grade">';
	$h .= '<div class="aqm-c3-campo"><label for="aqm-c3-tenho">Vazão do filtro (L/h)</label>';
	$h .= '<input type="text" inputmode="decimal" id="aqm-c3-tenho" placeholder="1000"></div>';
	$h .= '</div>';
	$h .= '<div class="aqm-c3-botoes"><button type="button" id="aqm-c3-tenho-calcular">Ver o que ele cobre</button></div>';
	$h .= '<p class="aqm-c3-criterio" id="aqm-c3-tenho-saida" style="margin-top:.6rem"></p>';
	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c3_fontes_html' ) ) {
function aquametria_c3_fontes_html() {
	$h  = '<div class="aqm-c3-painel">';
	$h .= '<h3>De onde vem cada número desta página</h3>';
	$h .= '<p class="aqm-c3-sub">Verificado em ' . esc_html( AQUAMETRIA_C3_VERIFICADO_EM ) . '. Calculadora versão ' . esc_html( AQUAMETRIA_C3_VERSAO ) . '.</p>';
	$h .= '<div class="aqm-c3-rolagem"><table class="aqm-c3-fontes">';
	$h .= '<tr><th>Constante</th><th>Valor</th><th>Origem e o que ela significa</th></tr>';

	$h .= '<tr><td>eheim-classic-250-2213</td><td>' . esc_html( number_format_i18n( AQUAMETRIA_C3_FABRICANTE_XH, 2 ) ) . ' x/h</td>';
	$h .= '<td>O Eheim classic 250 (2213) declara 440 L/h para aquários de até 250 L. A divisão dá 1,76 renovações por hora — o piso da faixa, e o único extremo que vem de quem fabrica filtro. ';
	$h .= 'Ficha coletada em 07/09/2026 <span class="aqm-c3-selo">fabricante via busca</span>: a página do fabricante não foi lida direto, reconferir no manual.</td></tr>';

	$h .= '<tr><td>turnover-comunitario-br</td><td>5 a 10 x/h</td>';
	$h .= '<td>Regra repetida por Aquarismo Paulista e AquaOnline, do levantamento de 04/09/2026 <span class="aqm-c3-selo">divergente entre fontes BR</span>. ';
	$h .= 'Nenhuma das duas explica a origem do número nem cita o dimensionamento do fabricante.</td></tr>';

	$h .= '<tr><td>turnover-comunitario-mybest</td><td>4 a 5 x/h</td>';
	$h .= '<td>Leitura conservadora da mesma pergunta, publicada pela my-best BR <span class="aqm-c3-selo">divergente entre fontes BR</span>. Está aqui porque discorda da anterior, e a discordância é o conteúdo.</td></tr>';

	$h .= '<tr><td>turnover-plantado</td><td>3 a 5 x/h</td>';
	$h .= '<td>AquaPeixes, para aquário plantado <span class="aqm-c3-selo">divergente entre fontes BR</span>. Corrente mais lenta é o argumento repetido; nenhuma fonte publica a medição que sustentaria o número.</td></tr>';

	$h .= '<tr><td>sump-proporcao-minima</td><td>' . esc_html( AQUAMETRIA_C3_SUMP_PCT ) . ' % do volume</td>';
	$h .= '<td>Mínimo repetido pela AquaOnline <span class="aqm-c3-selo">divergente entre fontes BR</span>. É a única constante de sump do levantamento.</td></tr>';

	$h .= '<tr><td>fator de perda de carga</td><td>sem valor <span class="aqm-c3-selo">pendente</span></td>';
	$h .= '<td>Quanto a vazão cai com mídia e coluna. Nenhuma fonte brasileira do levantamento publica, e o fabricante só declara a coluna máxima. Sem fonte, esta calculadora não aplica fator nenhum e entrega o protocolo do balde no lugar.</td></tr>';

	$h .= '<tr><td>turnover marinho</td><td>sem valor <span class="aqm-c3-selo">pendente</span></td>';
	$h .= '<td>O levantamento não trouxe turnover de aquário marinho com fonte brasileira. Por isso o perfil não está no formulário: quem tem sump recebe o volume mínimo dele, que tem fonte, e nada além disso.</td></tr>';

	$h .= '</table></div>';
	$h .= '</div>';
	return $h;
}
}

if ( ! function_exists( 'aquametria_c3_adiante_html' ) ) {
function aquametria_c3_adiante_html() {
	$hub   = function_exists( 'aquametria_casca_url_pagina' ) ? aquametria_casca_url_pagina( 'calculadoras' ) : home_url( '/calculadoras/' );
	$meto  = function_exists( 'aquametria_casca_url_pagina' ) ? aquametria_casca_url_pagina( 'metodologia' ) : home_url( '/metodologia/' );
	$c1    = function_exists( 'aquametria_casca_url_pagina' ) ? aquametria_casca_url_pagina( 'calculadora-de-litragem' ) : home_url( '/calculadora-de-litragem/' );
	$divul = function_exists( 'aquametria_casca_url_pagina' ) ? aquametria_casca_url_pagina( AQUAMETRIA_C3_PAGINA_AFILIADOS ) : home_url( '/' . AQUAMETRIA_C3_PAGINA_AFILIADOS . '/' );
	$c5    = function_exists( 'aquametria_casca_url_pagina' ) ? aquametria_casca_url_pagina( 'calculadora-de-potencia-do-aquecedor' ) : home_url( '/calculadora-de-potencia-do-aquecedor/' );
	$c12   = function_exists( 'aquametria_casca_url_pagina' ) ? aquametria_casca_url_pagina( 'calculadora-de-midia-filtrante' ) : home_url( '/calculadora-de-midia-filtrante/' );
	$c15   = function_exists( 'aquametria_casca_url_pagina' ) ? aquametria_casca_url_pagina( 'calculadora-de-iluminacao' ) : home_url( '/calculadora-de-iluminacao/' );

	$h  = '<div class="aqm-c3-painel aqm-c3-adiante">';
	$h .= '<h3>O que conversa com esta página</h3>';
	$h .= '<ul>';
	$h .= '<li><a href="' . esc_url( $c1 ) . '"><strong>Calculadora de litragem (C1)</strong></a> — é de onde vem o volume real que esta página usa. Se o número acima veio preenchido, veio de lá.</li>';
	$h .= '<li><a href="' . esc_url( $c5 ) . '"><strong>Potência do aquecedor (C5)</strong></a> — o outro aparelho que o seu volume dimensiona, e o único que pergunta quanto frio faz no seu cômodo. Usa o mesmo volume real desta página.</li>';
	$h .= '<li><a href="' . esc_url( $c12 ) . '"><strong>Mídia filtrante (C12)</strong></a> — quantos mililitros de mídia biológica o seu filtro precisa carregar, e se isso cabe no cesto dele. Usa o mesmo volume e o mesmo modelo de filtro que você escolheu aqui. A água precisa passar, e precisa passar por alguma coisa: vazão e mídia são as duas metades da mesma decisão.</li>';
	$h .= '<li><a href="' . esc_url( $c15 ) . '"><strong>Iluminação e fotoperíodo (C15)</strong></a> — o mesmo volume, do outro lado do aquário. Se o seu é plantado, a faixa de vazão desta página já é mais lenta por causa disso: planta quer corrente suave, e luz forte com CO2 pede que o gás não escape na superfície agitada.</li>';
	$h .= '<li><strong>Consumo elétrico (C7)</strong> — o filtro fica ligado 24 horas por dia, e é ele que pesa na conta. Vai ler a potência do modelo escolhido aqui. Ainda em construção.</li>';
	$h .= '<li><a href="' . esc_url( $meto ) . '"><strong>Como a Aquametria calcula</strong></a> — por que uma faixa com duas fontes que discordam vale mais que um número redondo sem origem.</li>';
	$h .= '<li><a href="' . esc_url( $divul ) . '"><strong>Como a Aquametria ganha dinheiro</strong></a> — o que é link de afiliado, o que muda (nada na ordem) e o que não publicamos.</li>';
	$h .= '</ul>';
	$h .= '<p class="aqm-c3-criterio">A lista completa, com o estado de cada calculadora, está em <a href="' . esc_url( $hub ) . '">todas as calculadoras</a>.</p>';
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

if ( ! function_exists( 'aquametria_c3_estilo_impresso' ) ) {
function aquametria_c3_estilo_impresso( $marcar = false ) {
	static $impresso = false;
	if ( $marcar ) {
		$impresso = true;
	}
	return $impresso;
}
}

if ( ! function_exists( 'aquametria_c3_pagina_usa' ) ) {
function aquametria_c3_pagina_usa() {
	if ( ! is_singular() ) {
		return false;
	}
	$pagina = get_post();
	if ( ! $pagina || ! isset( $pagina->post_content ) ) {
		return false;
	}
	return has_shortcode( $pagina->post_content, 'aquametria_calculadora_vazao' );
}
}

if ( ! function_exists( 'aquametria_c3_imprimir_estilo' ) ) {
function aquametria_c3_imprimir_estilo() {
	if ( aquametria_c3_estilo_impresso() ) {
		return;
	}
	aquametria_c3_estilo_impresso( true );
	echo '<style id="aquametria-c3-estilo">' . "\n" . aquametria_c3_css() . "\n" . '</style>' . "\n";
}
}

if ( ! function_exists( 'aquametria_c3_cabeca' ) ) {
function aquametria_c3_cabeca() {
	if ( ! aquametria_c3_pagina_usa() ) {
		return;
	}
	aquametria_c3_imprimir_estilo();
	aquametria_c3_imprimir_jsonld();
}
}
add_action( 'wp_head', 'aquametria_c3_cabeca', 20 );

if ( ! function_exists( 'aquametria_c3_rodape' ) ) {
function aquametria_c3_rodape() {
	/* Rede de segurança: se o shortcode entrou por um caminho que o wp_head não
	   enxergou (bloco, template, widget), o estilo ainda sai — atrasado, mas sai. */
	aquametria_c3_imprimir_estilo();

	$js  = 'var AQM_C3_DATA = ' . wp_json_encode( AQUAMETRIA_C3_VERIFICADO_EM ) . ";\n";
	$js .= 'var AQM_C3_BANDAS = ' . wp_json_encode( aquametria_c3_bandas() ) . ";\n";
	$js .= 'var AQM_C3_CATALOGO = ' . wp_json_encode( array_values( aquametria_c3_catalogo() ) ) . ";\n";
	$js .= aquametria_c3_js();
	echo '<script id="aquametria-c3-script">' . "\n" . $js . "\n" . '</script>' . "\n";
}
}

/* ---------------------------------------------------------------------------
 * 7. Shortcode — devolve SÓ o HTML. Estilo e comportamento saem acima.
 * ------------------------------------------------------------------------- */

if ( ! function_exists( 'aquametria_c3_shortcode' ) ) {
function aquametria_c3_shortcode() {
	static $ja_saiu = false;
	if ( $ja_saiu ) {
		/* Uma instância por página: os ids do formulário são únicos e o
		   comportamento liga na primeira. */
		return '';
	}
	$ja_saiu = true;

	/* O comportamento e o estilo saem no rodapé, fora dos filtros de conteúdo. */
	add_action( 'wp_footer', 'aquametria_c3_rodape', 20 );

	$h  = '<div class="aqm-c3">';
	$h .= aquametria_c3_promessa_html();
	$h .= aquametria_c3_resposta_direta_html();
	$h .= aquametria_c3_form_html();
	$h .= aquametria_c3_resposta_html();
	$h .= aquametria_c3_vitrine_servida_html();
	$h .= aquametria_c3_exemplos_html();
	$h .= aquametria_c3_tenho_html();
	$h .= aquametria_c3_fontes_html();
	$h .= aquametria_c3_adiante_html();
	$h .= aquametria_c3_barra_html();
	$h .= '</div>';

	return $h;
}
}
add_shortcode( 'aquametria_calculadora_vazao', 'aquametria_c3_shortcode' );
