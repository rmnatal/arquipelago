---
ilha: clubedomosaico
estado: nascendo
prioridade: 2
piso: abaixo            # abaixo | atingido — ver seção 21 do ARQUIPELAGO.md
urls_publicadas: 11
primeira_indexacao: desconhecida
ultima_execucao: 2026-09-12T00:10Z
executando_desde: null
bloco_atual: "A F1 ESTA NO AR — /materiais/quantas-pastilhas-para-mosaico/ (snippet clubedomosaico-f1.php 1.0.0, casca 1.6.0, manifest revisao 11, /status com revisao 11 as 00h05Z). Segunda ferramenta da ilha e segunda URL de nivel 3. POR QUE ELA GANHA: a primeira pagina inteira de 'rejunte para mosaico' responde a pergunta da OBRA, e a MESMA formula do fabricante aplicada a pastilha de 1x1 cm com folga de 2 mm da 2,8 kg/m2 — 3,8 vezes o azulejo de 10 cm e 2 vezes o piso de 20. A pagina serve as duas contas LADO A LADO na mesma tabela, com os dois numeros saindo da mesma formula, para a diferenca ficar verificavel em vez de afirmada. A GEOMETRIA E NOSSA E O CONSUMO E DO FABRICANTE: area por forma (o cone pela GERATRIZ, nunca pela altura — em vaso bojudo a diferenca passa de 10% e sempre para menos) e contagem pelo passo nao dependem de banco nenhum; os gramas saem da formula da Quartzolit com o coeficiente LIDO do registro do rejunte ceramicas. A CORRECAO DO BLOCO 3c ESTA NA TELA: o 1,75 vem de exemplo de rejunte cimenticio EM PO, entao a ferramenta RECUSA calcular para acrilico (pronto uso em pote) e epoxi (bicomponente) e nomeia o que falta — e recusa tambem se o banco trouxer dois coeficientes diferentes, porque escolher um calado e a mesma invencao com outra roupa. A REGUA DO REJUNTE TEM DONO: cdm_f2_celula_rejunte() e chamada daqui em vez de reescrita, e a F1 so filtra pelo tipo escolhido. O QUE QUASE PASSOU, E E O ACHADO DO DIA: a pagina respondeu 404 com o Sync dizendo revisao 10, seis itens aplicados e o snippet #8 criado. conferir-no-ar.py devolveu 37 falhas, todas a mesma — a URL nao existia. A causa era da CASCA: cdm_casca_montar() voltava na primeira linha quando a option cdm_casca_estrutura era igual a CDM_CASCA_VERSAO, e a 1.5.0 tinha acabado de criar o filtro cdm_paginas EXATAMENTE para a ferramenta registrar a propria pagina sem editar a casca. A guarda deixava esse mecanismo inerte: pagina nova entrava na definicao, a versao nao mudava, a montagem nao rodava, a pagina nunca nascia. A F2 escapou porque nasceu JUNTO com a 1.5.0 e foi de carona na troca de versao — mecanismo so exercitado de verdade na SEGUNDA vez que alguem o usa, que e o padrao desta ilha. Casca 1.6.0: a chave passa a ser a versao MAIS um resumo do mapa de paginas (slug, titulo, mae, shortcode), entao pagina nova, titulo trocado ou mae trocada remontam a estrutura sozinhos no primeiro carregamento depois do Sync, sem humano logado. O portao 21b mede o MECANISMO e nunca a versao — teste que olhasse CDM_CASCA_VERSAO teria ficado verde com o defeito no ar, e foi o que aconteceu por um bloco inteiro. O CLUSTER MUDOU DE ESTADO SOZINHO: com a terceira filha de /materiais/ no ar, a F2 e a /materiais/como-sabemos/ passaram a ter duas irmas e as tres publicam 'Veja tambem' — a regra da secao 6 do ARVORE.md funcionando pela primeira vez no sentido inverso (antes proibia o bloco, agora exige). E ISSO DESARMOU DUAS MUTACOES ANTIGAS, por motivos DIFERENTES, e a distincao e o aprendizado: 'irma escolhida fora da mae' passou porque o portao contava as irmas e conferia se estavam no ar, NUNCA de onde vinham — ela morria por efeito colateral, e o efeito sumiu com mais paginas no ar; trava frouxa de verdade, agora toda irma tem a mae recomputada. Ja 'a pagina fora do sitemap perde a citacao' passou porque o cluster novo liga a camada de prova sozinho: a trava nao afrouxou, MUDOU DE DONO, e o que mudou de dono ganhou trava propria — a citacao no TEXTO, medida com o cluster e a trilha fora da conta. O QUE A PAGINA DIZ QUE NAO SABE: a linha de gramas de cola nasce vazia com o motivo (o fabricante do silicone declara rendimento por cordao, nao por area); a pastilha nao tem banco e o cartao de compra fica reservado dizendo que esta vazio; e sem o banco a pagina continua respondendo area e pastilhas e diz que nao publica os gramas — a bancada mede esse estado de proposito. VERIFICACAO: teste-f1.php 67 afirmacoes com regua aritmetica escrita fora do snippet e um processo por estado (24 combinacoes de forma x caquinho, 36 de folga x tipo, cinco sobras, quatro espessuras, cinco lugares e as bordas); mutacoes-f1.py 27 de 27 reprovadas — DUAS passaram na primeira rodada e viraram afirmacao nova: o CR digitado dentro do snippet COM O VALOR CERTO (invisivel para qualquer teste sobre a tela de hoje; so troca de banco revela) e a vitrine ignorando o tipo escolhido (continua sendo subconjunto do que a F2 aprova, entao a trava de subconjunto nao a via). teste-casca.php de 367 para 409; mutacoes-arvore.py 20 de 20; teste-f2.php 72 e validar-banco.py sem regressao; php -l limpo; Chromium em 360/390/781/782/783/1200 nas 14 paginas, 88 medicoes, 0 px de rolagem — MEDIDO COM A CASCA 1.5.0, e isso fica dito porque prova vale pelo que foi medido: o que sustenta a medicao continuar valendo e que o HTML servido das 14 paginas e byte a byte IDENTICO entre a 1.5.0 e a 1.6.0 (a 1.6.0 so troca a chave que decide QUANDO a estrutura e remontada e nao imprime nada na tela), conferido por diff, nao suposto; uma terceira rodada do navegador morreu no tunel de rede. NO AR as 00h05Z: 194 afirmacoes medidas no HTML servido por conferir-no-ar.py, zero falha — 11 URLs em 200, tres tabelas pre-renderizadas, JSON-LD servido, noindex em todo estado com parametro, e QUATRO contas conferidas contra o calculo a mao (vaso 942 cm2/720/264 g, tampo 2.827/588/594 g, esfera 1.257/960/352 g, moldura 900/188/189 g). Sitemap de 9 para 10 URLs. O SYNC PRECISOU DE TRES DISPAROS NO TOTAL, e os dois primeiros nao foram cache: foram o defeito da casca acima — o terceiro, ja com a 1.6.0, fez a pagina nascer. DEFEITO DE ETIQUETA CONSERTADO DE QUEBRA: o manifest dizia casca 1.4.0 e o arquivo definia 1.5.0. O sha estava certo e o site nunca esteve errado — envelheceu a ETIQUETA, que e por onde qualquer relatorio le o que esta no ar. Nenhum portao lia essa metade; atualizar-manifest.py agora compara a versao do manifest com a constante do snippet e recusa gravar quando divergem (foi ele que acusou a 1.6.0 antes do commit). 10 dos 10 itens do banco esperam link de afiliado e 10 estao sem imagem; este bloco nao tocou catalogo, e nenhum dos dez tem loja possivel hoje. Pauta da secao 17: pauta.md ainda nao existe — 0 escritos, 0 na fila, 0 recusados. PROXIMO: as fichas de categoria de material (bloco 4c). A 16.5 continua valendo e hoje Colas e Rejuntes tem banco de cinco itens cada e UMA filha cada (as duas ferramentas); o caminho mais curto para destravar /materiais/colas-e-adesivos/ e /materiais/rejuntes/ e a leva de fichas de produto, que sao nivel 3 com dado real. A ilha esta ABAIXO DO PISO da secao 21 (10 URLs, 21 dias nao passaram), entao a leva sai no ritmo normal, de 5 a 10 URLs, sem esperar medicao."
ultima_ronda: null
bloqueada_por: null
---

# Estado da ilha CLUBE DO MOSAICO

Espelho legível do estado do projeto. **Nunca guarde credencial aqui.**

## Infraestrutura
- Domínio: clubedomosaico.com.br, registrado no registro.br em 10/09/2026.
- Hospedagem: domínio adicional criado no cPanel da HostGator em 10/09/2026 (br604, raiz própria `/clubedomosaico.com.br`), mesmo plano das outras ilhas, custo extra zero.
- DNS: nameservers ns604/ns605.hostgator.com.br apontados no registro.br em 10/09/2026, ~11h20 BRT. Zona no br604 com A = 108.179.253.218. Propagação pendente no momento deste commit.
- Search Console: propriedade `sc-domain:clubedomosaico.com.br` criada; TXT `google-site-verification=KWnwrQz3FOTs0Bln_y9EpjPhjJrWKwzpT2fi68L-2uA` gravado na zona (serial 2026091004). Verificação falhou na primeira tentativa porque o Google ainda via o DNS do registro.br — repetir depois da propagação.
- WordPress: instalado em 10/09/2026 14h51 BRT via Softaculous (7.1 pt-BR, instalação limpa, admin não é "admin"); SSL emitido na madrugada de 11/09; plugins da lista curta ativos em 11/09.
- Snippet de Sync: "Clube do Mosaico Sync" v1.1.5, snippet #5, ATIVO desde 11/09/2026; primeiro sync leu a revisão 3 (0 aplicados, 5 aguardando desembarque). Endpoints no PROMPT.md.
- Logo: logo completo e favicon subidos pelo Raphael na biblioteca de mídia em 11/09/2026 (URLs no PROMPT.md). **O logo completo é o do cabeçalho, transparente, a 52 px e sem texto ao lado, desde 11/09 20h35Z.** Em `identidade/logo/` ficam os favicons e a lótus solta (esta, truncada, só faria falta em ícone pequeno).
- E-mail da artesã (usuário `artesa` e notificações de lead): mina196@hotmail.com
- Casca: snippet "Clube do Mosaico Casca" **v1.5.0**, `publicar: true` no manifest (revisão 9),
  snippet #6 no Code Snippets. **No ar e conferido nas dez URLs em 11/09/2026 22h05Z.**
- Ferramenta F2: snippet "Clube do Mosaico F2 — qual cola e qual rejunte" **v1.0.0**,
  snippet **#7**, criado pelo Sync em 11/09/2026 22h03Z. Serve
  `/materiais/qual-cola-usar-no-mosaico/`, a primeira página de nível 3 da ilha.
- **O banco virou dado PUBLICADO nesta execução**: `esquema-banco`, `materiais-colas` e
  `materiais-rejuntes` passaram a `publicar: true` e viraram option no site. Até aqui eles
  eram pesquisa, e o caminho vivo de `cdm_casca_numeros()` — o que lê a option — **nunca
  tinha existido no ar**, exatamente o defeito latente que a Robometria encontrou em
  11/09/2026. Agora os números da tela vêm do banco servido, não do instantâneo digitado.

## O que já foi entregue
- 11/09/2026 22h05Z — **BLOCO 4: A F2, a primeira ferramenta da ilha, no ar em
  `/materiais/qual-cola-usar-no-mosaico/`** (snippet `clubedomosaico-f2.php` v1.0.0,
  casca 1.5.0, manifest na revisão 9, `/status` conferido). Primeira página de **nível 3**
  da ilha. A resposta é servida pelo **servidor** — formulário GET para a própria página,
  nenhuma linha de decisão em JavaScript —, então cada uma das 45 combinações de base ×
  ambiente é HTML servido de verdade e não existe régua duplicada entre PHP e JS. O estado
  com parâmetro sai com `noindex, follow`; quem entra no índice é a âncora, uma só, e o
  canonical fica com o `rel_canonical()` do núcleo (imprimir o nosso serviria dois).
  A elegibilidade é recomputada das declarações dos fabricantes pelas regras do
  `esquema-banco.json`, conferida contra as matrizes escritas à mão no bloco 3.
  O bloco de compra vem antes da procedência em todo cartão, mesmo com os dez itens sem
  link. Vieram junto `ferramentas/teste-f2.php` (72 afirmações, varrendo os 45 estados de
  cola e os 60 de rejunte, um processo cada), `ferramentas/mutacoes-f2.py` (20 mutações),
  `ferramentas/restaurar-acentos.py` e `ferramentas/atualizar-manifest.py`.
- 11/09/2026 20h35Z — **O LOGO DELE, INTEIRO, NO CABEÇALHO** (casca 1.4.0, manifest na revisão 8,
  `/status` conferido). Fecha o despacho do Raphael de 11/09 (2) inteiro, os cinco itens na mesma
  execução: `<img>` do logo completo a 52 px com link para a home e **sem texto ao lado**, barra de
  84 px, lótus solta fora do cabeçalho, `VOZ.md` corrigido no molde de casca LOJA. O `srcset` serve
  as reduções que o próprio WordPress gerou do upload dele (41 KB no lugar de 1,26 MB num espaço de
  78 px) e o `src` continua sendo a URL exata do despacho. Veio junto
  `ferramentas/conferir-no-ar.py`, que mede o HTML **servido** com régua própria (102 afirmações,
  nenhuma falha), e seis mutações novas no `mutacoes-voz-e-cabeca.py` — 24 de 24 reprovadas.
- 11/09/2026 19h40Z — **A ÁRVORE DA SEÇÃO 16** (casca 1.3.0, manifest na revisão 7,
  `/status` conferido). `ARVORE.md` com os três níveis e o lugar das nove páginas;
  trilha visível em oito delas (a home não tem, 16.3); `BreadcrumbList` nas mesmas
  oito; cluster "Veja também" ligando LOJA, GUIA e ESCOLA. **Nenhuma URL mudou e
  nenhuma precisou:** esta ilha já nascera com a árvore certa na estrutura — as três
  seções eram nível 1, a única página de nível 2 já tinha mãe desde 1.2.0 e as quatro
  da raiz são as que a 16.1 admite ali. Sem 301, sem mudança de sitemap. Veio junto
  `ferramentas/mutacoes-arvore.py` (19 mutações, 19 reprovadas) e a bancada aprendeu a
  **fabricar duas bordas que o mundo ainda não tem**: o degrau de trilha sem página e a
  página com exatamente uma irmã. `teste-casca.php` foi de 198 para 327 afirmações.
- 11/09/2026 — **Bloco 3b: a casca da ilha**, em `snippets/clubedomosaico-casca.php` v1.0.0
  (manifest na revisão 4, `publicar: true`, `ativo: true`). Oito páginas por shortcode: início,
  loja, materiais, como-fazer, sobre, contato, divulgação de afiliados e privacidade. Cabeçalho e
  rodapé pretos com miolo branco, menu sanfona acessível, favicon próprio embutido a partir do PNG
  entregue, JSON-LD Organization + WebSite. Vieram junto quatro ferramentas de bancada:
  `gerar-favicon.php`, `render-para-teste.php`, `teste-casca.php` (127 afirmações) e
  `teste-navegador-casca.mjs` (33 medições em Chromium).
- 10/09/2026 — Pesquisa de palavras-chave e SERP (na memória `/areas/projeto-clube-do-mosaico.md`) e estratégia aprovada em conversa (artifact "Clube do Mosaico").
- 10/09/2026 — **Bloco 3: modelo do banco** em `dados/esquema-banco.json`, a categoria
  COLA em `dados/materiais-colas.json` (5 registros) e o verificador
  `ferramentas/validar-banco.py`. Manifest na revisão 3, `publicar: false`, sem Sync.
  Sem coleta nova: os 5 registros vêm inteiros do bloco 2, com a mesma fonte e a mesma data.
  O verificador recomputa as 18 células da matriz da F2 a partir das declarações e bate com a
  tabela publicada no esquema; três mutações provaram que ele falha quando deve.

- 10/09/2026 — **Bloco 2: especificação das duas ferramentas** em
  `dados/especificacao-calculadoras.md` e **constantes de fabricante** em
  `dados/constantes.json` (manifest na revisão 2, `publicar: false`, sem Sync). 11 constantes
  coletadas direto do domínio de cada fabricante e 6 pendências nomeadas com o documento
  exato que fecha cada uma. A F2 (cola e rejunte) vem antes da F1, como o bloco 1 mandou.
- 10/09/2026 — **Bloco 1: corpus de buscas** em `dados/corpus-buscas.md` (manifest na revisão 1, `publicar: false`). Três clusters com a SERP classificada consulta a consulta em aberta/tomada/armadilha, coletada por busca web da nuvem. Ordem da fila definida por intenção × chance de primeira página: colas/F2 antes de rejuntes/F1, alicates antes de pastilhas, `/tecnicas/bizantino` como única cabeça de volume alto com chance real. Confirmadas como TOMADAS e fora da fila: `curso de mosaico` (escolas reais — a ilha não vende curso), `presente artesanal` (Elo7) e `vaso centro de mesa` (Leroy).

## O que a coleta do bloco 1 já provou, e que muda o desenho das ferramentas
- **A SERP de rejunte responde a pergunta errada.** Todo resultado é de obra (0,2–0,4 kg/m², "1 kg faz 3 m²"), calculado com azulejo grande. Peça de artesanato usa pastilha de 1×1 ou 2×2 cm e não é medida em m². A F1 não vai competir com essas páginas: ela responde outra coisa.
- **A regra cola × base circula sem procedência.** Madeira → cola branca, vidro → silicone, alvenaria → argamassa aparece em blog (FazFácil, Vila do Artesão) sem fabricante, sem código, sem data e sem separar interno/externo/molhado. Abre a F2 e ao mesmo tempo **proíbe** usar a SERP como fonte dela: o bloco 2 coleta de Quartzolit, Tekbond, Loctite e Cascola.
- **As lojas vendem pastilha em três unidades diferentes** — 100 peças (Shopee), 100 gramas (Bazar Horizonte), placa 30×30 com 225 (Boutique dos Azulejos). Converter peça ↔ grama ↔ placa é número próprio da ilha e não existe na SERP.

## O que o bloco 2 provou, e que decide como as ferramentas nascem
- **A ficha do próprio fabricante do silicone acético desmonta a prática corrente do
  mosaico brasileiro.** A ficha BRSA004 do Silicone Acético Construção Tekbond (revisada em
  10/2025) lista **espelho, concreto, cimento, tijolo, calcário, superfície alcalina,
  superfície pintada ou porosa, acrílico, aquário, metal corrosível e imersão contínua**
  entre as superfícies em que o produto não deve ser usado. Vaso de cimento, caco de espelho
  e peça de área molhada são exatamente o que o blog manda colar com silicone acético. Isso
  torna a elegibilidade da F2 **mecânica**: basta uma restrição bater com a entrada para o
  produto sair dos recomendados, com a frase do fabricante e a data na tela.
- **O par acético/neutro é do mesmo fabricante**, então a F2 diz "não use A, use B" sem sair
  de uma fonte só: o Silicone Neutro Tekbond é declarado para espelho, concreto, alvenaria e
  pedra, que são justamente as restrições do acético.
- **O número que abre a F1 existe e é grande.** Aplicando a fórmula publicada pela própria
  Quartzolit ao tamanho real da pastilha de artesanato, pastilha de 1×1 cm com 4 mm de
  espessura e junta de 2 mm consome **2,80 kg/m²** de rejunte — sete a catorze vezes os
  0,2–0,4 kg/m² que a primeira página do Google publica, porque a SERP inteira calcula com
  azulejo de obra. O bloco 1 tinha suspeitado; o bloco 2 mediu.
- **A placa 30×30 com 225 pastilhas não é pastilha de 1×1 cm.** O passo é 30/√225 = 2,00 cm,
  ou seja, pastilha nominal de 2 cm. É o erro que a artesã comete ao comparar preço entre
  loja que vende por peça e loja que vende por placa.
- **A espessura da pastilha não é constante de fabricante** — nenhum fabricante de pastilha
  de artesanato padroniza — então virou campo de entrada com aviso, e cada linha da tabela
  de exemplos declara a espessura que usou.

## O que o bloco 3 provou, e que corrige a matriz escrita à mão no bloco 2
- **A cimentcola AC-II não tem declaração de SUBSTRATO.** A especificação a recomendava para
  base de cimento citando que ela é declarada para "área interna e externa" — mas isso é
  ambiente, não superfície de aplicação. As únicas superfícies que a coleta nomeou
  ("cerâmicas e placas de pedra natural de até 120 × 120 cm") são a **peça assentada**. Sem
  essa declaração ela não é recomendação primária em base nenhuma, e quem responde à base de
  cimento é o silicone neutro, que declara concreto e alvenaria com todas as letras.
  Pendência nomeada: `cimentcola-substrato-declarado`.
- **Cerâmica e vidro em ambiente comum são empate, não escolha.** O mesmo fabricante declara
  cerâmica para o acético *e* para o neutro, e nenhum dos dois declara o ambiente. A página
  lista os dois como equivalentes; fingir uma preferência que a fonte não sustenta é o começo
  de ordenar por comissão.
- **Em sol e chuva o acético não fica "em segundo lugar": fica fora.** Ambiente de exposição
  continuada exige declaração explícita de resistência — só o neutro declara chuva e raios UV.
- **MDF molhado e externo têm resposta.** A especificação dizia "a ilha não recomenda" porque
  só tinha olhado PVA e acético; o neutro declara madeira entre os substratos que veda, e
  chuva e UV entre as resistências. O PVA sai desses ambientes por delimitação do próprio
  fabricante ("ambientes internos"), não por proibição inventada.
- **O par acético/metal mostrou por que "conjunto mais estreito" precisa ser regra escrita.**
  A mesma ficha indica alumínio anodizado e proíbe metal corrosível, zinco e chapa
  galvanizada. Vence a proibição: quem monta mosaico não sabe dizer se a chapa dela é
  galvanizada.

## O que o bloco 3c provou, ao encher a categoria REJUNTE

- **Rejunte não é cola, e o esquema só tinha olhado cola.** Na cola, a lista do fabricante nomeia
  a **base** — a superfície sobre a qual se cola. No rejunte, a mesma lista nomeia a **tessela** e o
  **ambiente**: "cerâmicas, pastilhas de porcelana e de vidro" é o que vai ser rejuntado, nunca o
  vaso de cimento embaixo. Rejunte não toca a base. Por isso a categoria ganhou mapa de termos,
  regras e matriz próprios, e a variável que decide passou a ser a **largura da junta**.
- **O defeito latente que isso revelou, medido:** `computar_celula()` varria todos os materiais do
  banco sem olhar categoria. As 18 células da F2 passavam porque o banco só tinha cola; o primeiro
  rejunte gravado fez as 18 falharem de uma vez, cada uma acusando os cinco rejuntes como
  "eliminados por silêncio". O conserto tentador — colar os cinco ids nas 18 células — deixaria a
  matriz verde dizendo uma bobagem.
- **Um número falso que já estava NO AR:** o cartão "Rejuntes" do Guia trazia `no_banco => 0`
  digitado à mão, e a categoria acabara de ganhar cinco produtos. O `teste-casca` não viu porque
  conferia só a categoria cola — a única que existia quando ele foi escrito. A casca 1.1.0 passa a
  contar o banco por categoria, e o teste passa a cobrar as seis, nos dois sentidos: categoria sem
  arquivo mapeado reprova, e arquivo de banco sem cartão no Guia também.
- **Uma busca que se respondeu sozinha, apanhada no ato.** Uma consulta com o número `1,55` escrito
  dentro dela devolveu `1,55` como se fosse declaração do fabricante. Foi descartada: pergunta que
  carrega a resposta não mede nada. O CR por tipo de rejunte continua pendente — e isso virou
  limite declarado da F1, não "seria bom ter": a coluna de rejunte vale só para rejunte
  **cimentício**, porque o acrílico é pronto uso em pote de 1 kg e o epóxi é bicomponente, e o
  1,75 sai de um exemplo de pó.
- **O achado mais valioso é também o que não fecha.** O *rejunte piscinas quartzolit* é o único
  material do banco inteiro cujo fabricante nomeia **pastilha de vidro** em uso submerso — e mesmo
  assim não é recomendado em célula nenhuma: a faixa de junta dele não foi obtida, e o que ele
  declara é **água tratada quimicamente**, que é piscina, não a água parada de um vaso de jardim.
  A peça submersa segue sem cola declarada (só o Durepoxi, nível 4). A faixa continua descoberta, e
  a página diz exatamente o que já existe e o que falta.

## O que está travando
- **A rede foi RECONFERIDA em 11/09/2026 21h23Z, antes de trabalhar** (seção 20.2 do
  contrato), e de novo no desembarque: dois `curl` seguidos à home devolveram **200,
  200**, e o `/status`, o Sync, as dez páginas, o sitemap e as três URLs da imagem
  responderam. Nada de `000`, nada de 403. A ilha está no ar na **revisão 9**.
- **O SYNC PRECISOU DE TRÊS DISPAROS, e isso não é bloqueio: é cache de borda.** Os dois
  primeiros leram do `raw.githubusercontent` um `manifest.json` ainda na revisão 8
  enquanto já baixavam a casca nova, e a trava de `sha256` recusou aplicar — que é ela
  funcionando. O cache é por caminho, não por commit: o arquivo novo e o índice velho
  chegam em momentos diferentes, e o `?v=` que o Sync já acrescenta não resolveu. Esperar
  e repetir resolveu em poucos minutos. **O que não se pode é ler o primeiro
  "0 aplicado(s)" como entrega** — é exatamente a forma de "commit sem Sync" que a seção
  20 existe para impedir, com outra roupa.
- ~~**A rede foi RECONFERIDA em 11/09/2026 19h21Z, antes de trabalhar**~~ (seção 20.2 do
  contrato): três `curl` seguidos à home devolveram **200, 200, 200** — nenhum `000`, nenhum
  403. O Sync, o `/status`, as nove páginas e o sitemap também responderam. A ilha está no ar
  na **revisão 7**. Esta linha existe porque bloqueio que não é reconferido a cada execução
  vira permanente sozinho, e foi assim que esta ilha ficou dois dias fora do ar por um
  diagnóstico que ninguém retestou.
- ~~**A ILHA INTEIRA NÃO ESTÁ NO AR, e agora são DUAS revisões presas.**~~ **RESOLVIDO em
  11/09/2026 17h50Z, e o diagnóstico anterior estava errado.** A ilha ESTÁ no ar: o Sync foi
  acionado por `curl` desta execução, as revisões 4, 5 e 6 desembarcaram, e o `/status` devolve
  **revisão 6**, igual à do manifest. As nove URLs respondem 200.
  **O que aconteceu, porque isto vale mais que o conserto:** o primeiro `curl` desta execução à
  home devolveu `000`, exatamente como nas duas execuções anteriores — e **o mesmo comando,
  repetido minutos depois, devolveu 200**, assim como o Sync, o `/status`, as nove páginas e o
  sitemap. Era intermitência do túnel, não bloqueio de rede: `clubedomosaico.com.br` está, sim,
  na lista Personalizada do ambiente. Duas execuções anteriores leram um `000`, escreveram
  "403 ao CONNECT" e nunca reconferiram — e o bloqueio virou permanente sozinho, prendendo duas
  revisões desta ilha por dois dias.
  **A regra que fica:** bloqueio herdado se testa de novo a cada execução, e uma falha de rede
  só vira bloqueio depois de repetir. A seção 4 do contrato manda testar antes de presumir; falta
  a outra metade, que é testar de novo antes de continuar presumindo.
- ~~**A LÓTUS DO CABEÇALHO**~~ — **deixou de ser pendência em 11/09/2026, 20h35Z.** O cabeçalho
  serve o **logo completo** do Raphael, que já contém a lótus e o nome, e o despacho de 11/09 (2)
  proíbe texto ao lado dele. A lótus SOLTA continua truncada no repositório
  (`identidade/logo/lotus-512.png`: o `IDAT` declara 11.638 bytes num arquivo com 8.770, `IEND`
  colado no fim, e o `zlib` recusa o primeiro bloco), e isso agora não bloqueia nada — o lugar dela
  é ícone pequeno, não o cabeçalho. Quando chegar um PNG transparente de ≥ 512 px no mesmo caminho,
  `php ferramentas/gerar-marca.php .` embute e confere; a ferramenta recusa arquivo que não abre,
  sem canal alfa ou com canto opaco.
- **O DIAGNÓSTICO DE 1.2.0 ESTAVA ERRADO, e é a cicatriz que esta execução deixa escrita.** Três
  lugares do snippet e um do `VOZ.md` afirmavam que o arquivo do Raphael "tem fundo preto". Não
  tem: é transparente, e ele conferiu na biblioteca de mídia. O logo sumiu em 1.1.0 porque o
  **cabeçalho** era preto e o wordmark dentro do arquivo é vinho `#69030C` — defeito de onde o
  logo foi posto, nunca do arquivo. A 1.2.0 consertou a causa (clareou o cabeçalho) e, pela
  leitura errada do sintoma, tirou também o logo, que era a parte certa. **Sintoma não é causa, e
  um diagnóstico escrito com ar de fato se propaga por versões** — a mesma forma do `000` lido
  como bloqueio de rede na semana passada.
- **Caixa `contato@clubedomosaico.com.br` não existe ainda.** O adendo 3 do `PROMPT.md` pede que ela
  seja criada no cPanel (ou que o SPF/DKIM do domínio seja garantido) para o e-mail de lead do bloco
  4d chegar ao Hotmail da artesã. Não é trabalho da Fundação: exige o painel da hospedagem. Por isso
  a página `/contato/` publicada **não** anuncia endereço de e-mail — diz que o canal está sendo
  configurado, em vez de publicar um endereço que devolveria a mensagem.
- **Substrato da cimentcola AC-II** (achado do bloco 3): sem ele, a base de cimento fica
  respondida só pelo silicone neutro. Está no Boletim Técnico 2024-09 da Quartzolit, que a
  nuvem não abre. Não bloqueia publicação.
- Loja: depende da mãe do Raphael cadastrar peças na área da artesã (bloco 4d, snippet de CPT). O login é criado pelo snippet e entregue ao Raphael. Não bloqueia os blocos 1–3.
- CPC por consulta: o Planejador está na conta do Raphael, no navegador. Ficou declarado como ausente no corpus, nunca estimado. Coluna a preencher na primeira leitura semanal com o painel aberto.
- SERP de `colar de mosaico` e `mandala de mosaico`: não verificadas nesta execução, e estão escritas assim no corpus.
- **Coluna de gramas de cola da F1**: falta o consumo em kg/m² da cimentcola AC-II/AC-III e o
  rendimento do silicone por área (o fabricante declara por cordão). São as duas únicas
  pendências que bloqueiam publicação, e bloqueiam só essa coluna — a F1 sai sem ela dizendo
  por quê. As outras quatro pendências (CR por tipo de rejunte, secagem do Cascorez, ficha do
  Tekbond Espelho Fix, rejunte epóxi) são coleta, não bloqueio.
- **Duas faixas descobertas da F2, declaradas em vez de chutadas**: peça em contato
  permanente com água e base de plástico. A página vai dizer que não publica recomendação
  nesses dois casos.
- **A nuvem não abre PDF de fabricante.** `curl` e `WebFetch` para quartzolit.weber e
  tekbond.com.br voltaram `EGRESS_BLOCKED`/`connect_rejected`: a rede das rotinas libera os
  domínios das ilhas, `*.googleapis.com` e `github.com`, e nada mais. A coleta do bloco 2 foi
  feita por busca web restrita ao domínio de cada fabricante, e cada constante declara isso
  em `fonte_tipo`, com `conferir_no_pdf` marcando as que merecem segunda leitura. Se o
  Raphael quiser fechar essa lacuna, é acrescentar quartzolit.weber, tekbond.com.br,
  cascola.com.br e henkel.com.br à rede Personalizada do ambiente das rotinas.
- DNS/WordPress/Search Console seguem como no registro de 10/09. Nada disso trava os blocos 2 e 3, que não dependem de site.

## Pendências do Raphael (não travam)
- Nome, foto e perfis de redes sociais da artesã para o Sobre — decidido em 11/09/2026 que ela aparece.
  A casca já publica o Sobre com o bloco dela pronto: escreve "uma artesã", sem nome de fantasia e sem
  foto genérica, e o teste reprova se alguém inventar um nome. Chegando à pasta `identidade/artesa/`,
  entram também o `sameAs` do JSON-LD, que hoje está deliberadamente ausente.
- ~~**Domínio da ilha na rede Personalizada do ambiente das rotinas.**~~ **Não era isso.** A rede
  alcança a ilha; o que houve foi intermitência lida como bloqueio em duas execuções seguidas —
  ver "O que está travando". Nada a fazer, e nada a pedir ao Raphael por aqui.
- ~~**A lótus do cabeçalho**~~ — **não é mais pendência**: o cabeçalho leva o logo completo dele
  desde 20h35Z de 11/09. A lótus solta segue truncada no repositório e só faria falta em ícone
  pequeno; ver "O que está travando" e `identidade/logo/LEIA-ME.md`.
- **O tamanho do logo no cabeçalho, se ele quiser opinar.** A 52 px de altura (o número do
  despacho dele) o wordmark dentro do arquivo fica com ~8 px por linha: lê-se como logotipo, mas é
  pequeno. Caminhos, e a escolha é dele: subir para ~64 px, ou mandar uma versão horizontal do
  lockup (lótus ao lado do nome em vez de acima). Não trava nada.
- **Os hexadecimais do cabeçalho.** O despacho sugeriu `#FBF7F4`, `#EEE8E4`, `#111` e `#E8483A`;
  a casca serve os tokens aprovados por ele em 10/09 (`papel #FFFFFF`, `traço #E9DCD7`,
  `tinta #1F1715`, `coral #FC483B`), que são vizinhos de um a quatro passos. Um segundo branco a
  quatro unidades do primeiro é defeito, não identidade — mas se ele quiser exatamente aqueles
  valores, é uma linha. Registrado em 11/09 e de novo em 20h35Z.
