# Registro de execucoes — Clube do Mosaico

Log append-only da Fundacao. Cada execucao escreve aqui o bloco entregue e o
proximo passo desbloqueado.

10/09/2026 — pasta da ilha criada pelas mãos, a pedido da sessão de conversa

- Criada a pasta `ilhas/clubedomosaico/` com `snippets/`, `conteudo/`,
  `dados/`, `identidade/logo/`, `manifest.json` (revisao 0, nenhum item, nada
  marcado para publicar), `README.md`, `PROMPT.md`, `ESTADO.md` e este
  registro.
- `snippets/clubedomosaico-sync.php` gerado a partir de
  `ilhas/robometria/snippets/robometria-sync.php`, sem outra alteracao alem da
  troca de nome da ilha. Passou em `php -l`.
  sha256: `0b893702fd4614928adeddabdf51465f7214304798640041c6a277f2fcfd0649`
- Proximo passo: bloco 1 — corpus de buscas em `dados/corpus-buscas.md`. Nao
  depende de site nem de WordPress.

10/09/2026 15:21Z — BLOCO 1 ENTREGUE: corpus de buscas

- `dados/corpus-buscas.md` criado com os tres clusters da ilha
  (materiais/ferramentas, pecas prontas, aprender), a SERP classificada
  consulta a consulta em aberta/tomada/armadilha pela regra da secao 14.9, e a
  ordem da fila derivada do cruzamento intencao de compra x chance de primeira
  pagina. Manifest na revisao 1; `publicar: false`, entao **nao houve Sync
  nesta execucao** — a secao 4 do contrato so exige acionar o Sync em bloco que
  mexe em conteudo publicavel, e este nao mexeu.
  sha256: `5580e5fa9084b4c06da3bb26e8e2088936b9cffbb65ca60f1b4de243f14db695`
- Procedencia separada em duas coletas, e assim escrita no arquivo: a faixa de
  volume veio do Planejador na conta do Raphael (10/09, via `PROMPT.md`, nao
  refeita aqui); a SERP foi coletada nesta execucao por busca web da nuvem, com
  os ocupantes do top 10 nomeados. **CPC nao foi coletado e esta declarado como
  ausente, nunca estimado** — a fila do bloco 1 pedia CPC e ele nao existe sem
  o painel autenticado.
- Tres achados medidos que mudam o desenho das ferramentas:
  (1) toda a SERP de rejunte responde a pergunta de OBRA (0,2-0,4 kg/m2, azulejo
  grande) e portanto esta ERRADA para peca de artesanato com pastilha de 1x1 cm
  — a F1 nao compete com essas paginas, responde outra coisa;
  (2) a regra cola x base ja circula em blog, mas sem fabricante, codigo, data
  nem separacao interno/externo/molhado — abre a F2 e ao mesmo tempo proibe usar
  a SERP como fonte dela;
  (3) as lojas vendem pastilha em tres unidades diferentes (100 pecas, 100 g,
  placa 30x30 com 225), entao converter peca <-> grama <-> placa e numero
  proprio da ilha.
- Tomadas, e por isso FORA da fila: `curso de mosaico` (top 10 sao escolas reais
  com professora e turma; a ilha nao vende curso), `presente artesanal` (Elo7) e
  `vaso centro de mesa` (Leroy). `mosaico bizantino` entrou como alvo: faixa
  1k-100k com a primeira pagina em portugues ocupada por resultado em espanhol.
- Concorrente nomeado para a leitura semanal acompanhar: `mosaico.arq.br`, que
  vende peca artesanal e curso — o mais parecido com esta ilha inteira.
- Nao houve memoria disponivel nesta execucao (`/areas` nao existe no ambiente).
  O estado vive no `ESTADO.md` desta pasta, como manda o `PROMPT.md`.
- Proximo passo desbloqueado: **bloco 2** — `dados/especificacao-calculadoras.md`
  e `dados/constantes.json`, comecando pela F2 (seletor de cola e rejunte), que
  o corpus mostrou ser a de maior intencao e menor concorrencia. Constante so
  com fonte de fabricante e data (Quartzolit, Tekbond, Loctite, Cascola); sem
  fonte, `pendente` e fora de formula publicada. Nao depende de site.

10/09/2026 19:30Z — BLOCO 2 ENTREGUE: especificacao das duas ferramentas + constantes

- `dados/constantes.json` (11 constantes de fabricante, 6 pendencias nomeadas) e
  `dados/especificacao-calculadoras.md` (contrato de construcao da F1 e da F2). Manifest na
  revisao 2; os dois com `publicar: false`, entao **nao houve Sync nesta execucao** — a
  secao 4 do contrato so exige Sync em bloco que mexe em conteudo publicavel.
  sha256 constantes: `99c6c5cb7130fc0428bb15312226c74ced0b51fa79cc95c3ca4de7f45dca1e39`
  sha256 especificacao: `1189ad6f0fc3e21ed046acc7d2215e0c947f267b1557b07b1c87a05edb58fa7a`
- **Procedencia, e o limite dela, declarados item a item.** A coleta foi por busca web
  restrita ao dominio de cada fabricante (quartzolit.weber, tekbond.com.br, cascola.com.br,
  henkel.com.br). `curl` e `WebFetch` para esses dominios voltaram `EGRESS_BLOCKED` /
  `connect_rejected` — a rede das rotinas libera os dominios das ilhas, `*.googleapis.com` e
  `github.com` —, entao os PDFs de boletim tecnico **nao foram abertos linha a linha**. Cada
  constante diz isso em `fonte_tipo` e marca `conferir_no_pdf`. **Nada de blog, loja ou
  agregador entrou**: o bloco 1 tinha medido que a regra cola x base circula na SERP sem
  fabricante, codigo nem data, e a fila proibiu usar a SERP como fonte da F2.
- **O achado que decide a F2:** a ficha BRSA004 do Silicone Acetico Construcao Tekbond
  (revisada em 10/2025) lista espelho, concreto, cimento, tijolo, calcario, superficie
  alcalina, superficie pintada ou porosa, acrilico, aquario, metal corrosivel e imersao
  continua entre as superficies em que o produto NAO deve ser usado — que sao exatamente os
  casos em que o mosaico artesanal brasileiro usa silicone acetico por indicacao de blog.
  Isso torna a elegibilidade da secao 7 **mecanica**: basta uma restricao bater com a entrada
  para o produto sair dos recomendados e ir para a secao rotulada, com a frase do fabricante
  e a data. E o par acetico/neutro sendo do mesmo fabricante, a F2 diz "nao use A, use B" sem
  sair de uma fonte so.
- **O achado que decide a F1:** aplicando a formula publicada pela propria Quartzolit
  (`((A+B) x E x L x CR)/(A x B)`, CR 1,75 no exemplo do fabricante) ao tamanho real da
  pastilha de artesanato, pastilha de 1x1 cm com 4 mm de espessura e junta de 2 mm consome
  **2,80 kg/m2** de rejunte — 7 a 14 vezes os 0,2-0,4 kg/m2 que a primeira pagina do Google
  publica com azulejo de obra. A tabela pre-renderizada de 12 pecas tipicas ja esta calculada
  no arquivo. Segundo numero proprio: a placa 30x30 com 225 pastilhas tem passo 30/raiz(225)
  = 2,00 cm, ou seja, **nao e pastilha de 1x1 cm** — e o erro de quem compara preco entre
  loja que vende por peca e loja que vende por placa.
- **O que NAO foi publicado, de proposito.** A espessura da pastilha virou campo de entrada,
  nao constante, porque nenhum fabricante de pastilha de artesanato a padroniza. A coluna de
  gramas de cola da F1 nasce vazia com explicacao na tela: falta o consumo em kg/m2 da
  cimentcola e o rendimento do silicone por area (o fabricante declara por cordao), e as duas
  estao em `pendentes`. A F2 declara duas faixas DESCOBERTAS — peca em contato permanente com
  agua e base de plastico — em vez de preencher no chute. A conversao grama <-> peca fica
  pendente por SKU, para o banco MATERIAL do bloco 3 coletar com data.
- A especificacao ja carrega o bloco de compra obrigatorio ANTES da prova de procedencia,
  pela cicatriz da Robometria de 10/09: nenhuma das duas ferramentas vai ao ar sem ele, mesmo
  com `afiliado.url` vazio, e a ilha reporta quantos itens esperam link.
- Nao houve memoria disponivel nesta execucao (`/areas` nao existe no ambiente), como no
  bloco 1. O estado vive no `ESTADO.md` desta pasta.
- Proximo passo desbloqueado: **bloco 3** — modelo do banco (MATERIAL, PECA, TECNICA). A
  especificacao ja nomeou os campos que as duas ferramentas exigem de MATERIAL: categoria
  cola (com a lista de restricoes declaradas por produto), rejunte (com faixa de junta) e
  pastilha (com lado, espessura e unidade de venda). Nao depende de site. Depois dele, o
  bloco 4 fica dependendo so do WordPress existir.

10/09/2026 23:16Z — BLOCO 3 ENTREGUE: modelo do banco + categoria COLA + verificador

- `dados/esquema-banco.json` (modelo das entidades MATERIAL, PECA, TECNICA e da serie
  temporal COTACAO), `dados/materiais-colas.json` (5 registros da categoria cola) e
  `ferramentas/validar-banco.py`. Manifest na revisao 3; tudo com `publicar: false`, entao
  **nao houve Sync nesta execucao** — a secao 4 do contrato so exige Sync em bloco que mexe
  em conteudo publicavel, e a ilha ainda nao tem WordPress.
  sha256 esquema: `862f84b64ed9005ab00dc2c97335e470c1c44d63b63d025e51e93be77e50ed33`
  sha256 colas:   `0df9a40da7343f2a96675aaf4c9b0bc8506fed008fc6781afa6f37b9d62a090d`
  sha256 validador: `ac3f1f6001ea405f26303b3ecf6a82092329926701070ee686eb61909db27f3a`
- **NENHUM dado novo foi coletado, e isso e proposital.** Os 5 registros de cola sao a
  transposicao campo a campo do que o bloco 2 ja tinha colhido em `dados/constantes.json`,
  com a mesma fonte, o mesmo tipo de documento e a mesma data. O que o bloco acrescenta e
  ESTRUTURA: a lista literal do fabricante virou campo COM PESO — indicado, proibido, nao
  recomendado, delimita ambiente, resiste a ambiente — e por isso a matriz da F2 passou a ser
  RECOMPUTADA em vez de lida.
- **O verificador nao e enfeite.** Ele recomputou as 18 celulas base x ambiente pelas cinco
  regras de elegibilidade e bateu com a tabela publicada no esquema. Tres mutacoes provaram
  que ele falha quando deve: apagar `espelhos` da lista de restricoes da ficha BRSA004
  (2 erros, o acetico deixa de ser eliminado no espelho), promover o press release do
  Durepoxi de nivel 4 para 3 (20 erros, ele invade os recomendados de 8 celulas) e criar
  `dados/pecas.json` (1 erro: PECA nao vive no repositorio).
- **QUATRO ACHADOS que corrigem a matriz que o bloco 2 tinha escrito a mao**, e por isso a
  secao 1.3 da especificacao ganhou uma nota dizendo que quem manda agora e o esquema:
  (1) **a cimentcola AC-II nao tem declaracao de SUBSTRATO** — a especificacao a recomendava
  para base de cimento citando que ela e declarada para "area interna e externa", que e
  AMBIENTE; as unicas superficies nomeadas na coleta ("ceramicas e placas de pedra natural de
  ate 120 x 120 cm") sao a PECA ASSENTADA. Ela sai dos recomendados de todas as celulas, e
  quem responde base de cimento e o silicone neutro, que declara concreto e alvenaria com
  todas as letras;
  (2) **ceramica e vidro em ambiente comum sao EMPATE** entre acetico e neutro — o mesmo
  fabricante declara ceramica para os dois e nenhum declara o ambiente —, entao a pagina
  lista os dois em vez de fingir uma preferencia que a fonte nao sustenta;
  (3) **em sol e chuva o acetico nao fica "em segundo lugar", fica FORA**: ambiente de
  exposicao continuada exige declaracao explicita, e so o neutro declara chuva e raios UV;
  (4) **MDF molhado e externo TEM resposta** — o neutro declara madeira entre os substratos
  que veda —, ao contrario do "a ilha nao recomenda" da especificacao, que so tinha olhado
  PVA e acetico. O PVA sai desses ambientes por DELIMITACAO do proprio fabricante
  ("ambientes internos"), nunca por proibicao inventada.
- **O que o esquema tem de proprio desta ilha**, e que nao foi copiado de Aquametria nem de
  Robometria: o campo que decide a recomendacao e NEGATIVO (a lista de restricoes vale mais
  que a de indicacoes); existem TRES estados de declaracao e nao dois, porque silencio nao e
  proibicao e foi o Cascorez que obrigou isso; a escada de fontes tem um nivel 4 criado para
  material de imprensa, que e o que mantem a peca submersa como faixa DESCOBERTA mesmo com o
  Durepoxi declarando secar debaixo d'agua; e PECA e a unica entidade do Arquipelago que NAO
  e arquivo do repositorio — o validador falha de proposito se alguem criar `dados/pecas.json`.
- **Uma correcao de entrada para o bloco 4:** a secao 1.2 da especificacao tem so "vidro",
  mas a matriz distingue vidro comum de vidro LAMINADO — e a distincao decide o produto
  (o acetico e proibido no laminado). O formulario precisa da pergunta, escrita em portugues
  de gente: "o vidro tem uma pelicula entre duas camadas?".
- 5 itens esperando link de afiliado e 5 sem imagem — os cinco da categoria cola. Geracao de
  link e da Sentinela estrategica, no navegador, e nunca da Fundacao.
- Nao houve memoria disponivel nesta execucao (`/areas` nao existe no ambiente), como nos
  blocos 1 e 2. O estado vive no `ESTADO.md` desta pasta.
- Proximo passo desbloqueado: **as categorias REJUNTE e PASTILHA do banco**, que nao dependem
  de site e que o esquema ja deixou com os campos nomeados (rejunte com faixa de junta;
  pastilha com lado anunciado, passo de fabrica, espessura e unidade de venda). O bloco 3b
  (casca) e o bloco 4 (ferramentas) continuam dependendo so de o WordPress existir.

11/09/2026 — sessão de conversa: decisões do Raphael gravadas — artesã aparece com nome/foto/redes; botão Verificar disponibilidade + leads por e-mail; acesso do painel vai direto para a artesã.

11/09/2026 11:49Z — BLOCO 3b ENTREGUE: a casca da ilha (commitada e verificada; NAO esta no ar)

- `snippets/clubedomosaico-casca.php` v1.0.0, manifest na revisao 4 com `publicar: true` e
  `ativo: true`. Oito paginas criadas e mantidas por shortcode: inicio, loja, materiais,
  como-fazer, sobre, contato, divulgacao-de-afiliados e privacidade. Cabecalho e rodape pretos
  com o miolo branco, menu sanfona com aria-expanded/aria-controls, favicon proprio no lugar do
  icone do WordPress, JSON-LD Organization + WebSite em toda pagina, apelidos com 301 e a trava
  do sitemap 404.
  sha256 casca: `9b678bcffd00fc75261a6769d64777c2b6d1be1e3fb56e02398bd9d627753001`
- Ferramentas de bancada que nasceram junto, nenhuma publicada no site:
  `ferramentas/gerar-favicon.php`, `ferramentas/render-para-teste.php`,
  `ferramentas/teste-casca.php` e `ferramentas/teste-navegador-casca.mjs`.

- **O QUE ESTA CASCA TEM DE PROPRIO**, e que nao foi copiado de Aquametria nem de Robometria:
  (1) **a marca e uma imagem ENTREGUE, nao um desenho do snippet.** As duas primeiras ilhas
  desenham o simbolo em SVG dentro do codigo; aqui o logo foi feito por gente e o `PROMPT.md`
  proibe redesenhar, vetorizar ou escrever o nome ao lado do arquivo, que ja traz o wordmark. O
  teste reprova se aparecer um `<svg>` de logotipo ou se o nome for repetido em texto dentro do
  bloco da marca.
  (2) **tres motores, tres catalogos.** Loja, Guia e Escola nao cabem num catalogo de
  "ferramentas": a casca tem `cdm_casca_ferramentas()`, `cdm_casca_categorias_do_guia()` e
  `cdm_casca_tutoriais()`, e o cartao de categoria do Guia diz **quantos itens ela tem no banco**
  em vez de um "em breve" generico — e esse numero que separa promessa de trabalho feito.
  (3) **a Loja tem estado vazio honesto, e ele e testado nos DOIS estados.** O catalogo de pecas
  vive no CPT que a artesa alimenta (bloco 4d) e nunca no repositorio, entao hoje a Loja mostra
  "em breve, e sem peca de mentira ate la". O teste simula o CPT com duas pecas e exige que a
  vitrine apareca e o estado vazio suma — sem isso, uma vitrine que nunca mostra peca nenhuma
  passaria despercebida.
  (4) A casca nasce com a **trava do sitemap 404** que a Robometria so descobriu depois de
  publicar: ilha sem post publicado faz o `wp-sitemap.xml` sair com o XML certo e status 404.

- **VERIFICACAO** (secao 8): `php -l` limpo; `teste-casca.php` com **127 afirmacoes** e
  `teste-navegador-casca.mjs` com **33 medicoes** num Chromium de verdade — rolagem horizontal
  **0 px** em 360/390/781/782/783/1200 px nas oito paginas, o botao do menu aparecendo e sumindo
  na borda exata dos 782 px, contraste 21:1 no cabecalho e no rodape e 17,6:1 no corpo (formula da
  WCAG escrita dentro do proprio teste), e a **mesma pagina com o JavaScript DESLIGADO** servindo
  os quatro links do menu visiveis e o corpo inteiro, que e o que o crawler de IA recebe.

- **QUINZE MUTACOES DELIBERADAS, e o que elas custaram.** Treze reprovaram de primeira. **Duas
  passaram**, as duas na mesma trava — a de escassez inventada —, e reescreve-la duas vezes foi o
  trabalho mais util do bloco:
  1. A 1a versao procurava o termo no corpo inteiro com excecao para algumas negacoes escritas a
     mao. Reprovou a pagina Sobre, que diz com todas as letras que **nao** publica selo de mais
     vendido. Regua que reprova a frase certa.
  2. A 2a versao separava o corpo em frases e perdoava a frase com qualquer negacao. A mutacao
     "a ficha tecnica do silicone acetico mais vendido do Brasil lista ... entre as superficies em
     que o produto **nao** deve ser usado" **passou**: o "nao" da frase negava outra coisa.
     Perdoar por presenca de palavra e adivinhar.
  3. A 3a versao, que ficou: a pagina **declara no markup** qual bloco e recusa
     (`class="cdm-nao-fazemos"`), o teste retira esses blocos e proibe o termo em todo o resto. E
     para a declaracao nao virar porta dos fundos, exige que **todo bloco marcado ABRA negando** —
     porque a mutacao seguinte enfiou "Peca mais vendido, ultimas unidades!" dentro do bloco de
     recusa e passou enquanto a regra so pedia negacao em algum lugar dele.
- **A 2a versao, antes de ser reprovada, achou um defeito de verdade escrito pela propria
  Fundacao**: a home chamava o produto de "o silicone acetico **mais vendido** para construcao" —
  numero de venda que esta ilha nunca mediu e nao pode afirmar (secao 7). Corrigido para o nome do
  produto. E a trava de "a pagina medida tem tamanho de pagina" reprovou duas paginas finas demais
  para o indice de um dominio novo (como-fazer com 971 e contato com 1194 caracteres de corpo); as
  duas ganharam conteudo real, tirado do banco e nao de enchimento, e hoje tem 2.716 e 1.813.

- **O DESEMBARQUE NAO ACONTECEU, e isso nao e detalhe.** `curl` para
  `https://clubedomosaico.com.br/...` devolveu **000**, e o `$HTTPS_PROXY/__agentproxy/status`
  registrou `connect_rejected: gateway answered 403 to CONNECT` para
  `clubedomosaico.com.br:443` as 11h19Z. A secao 4 do contrato manda testar antes de presumir
  bloqueio — foi testado, duas vezes, e falhou. Entao **a casca esta no `main` e nao esta no ar**:
  o site continua servindo o tema padrao do WordPress. O item fica aberto e e de uma linha: acionar
  o Sync da ilha e conferir no `/status` que a revisao aplicada e a **4**. Quem tiver o dominio na
  rede Personalizada do ambiente faz isso em um minuto. "Aplicado com sucesso" nao foi dito aqui
  porque nao foi medido.

- 5 itens do banco esperando link de afiliado e 5 sem imagem — os mesmos cinco da categoria cola,
  inalterados: este bloco nao coletou dado nenhum, e nao devia.
- Nao houve memoria disponivel nesta execucao (`/areas` nao existe no ambiente), como nos blocos
  1, 2 e 3. O estado vive no `ESTADO.md` desta pasta.
- Proximo passo desbloqueado: **bloco 4 — a ferramenta F2** (seletor de cola e rejunte), que o
  esquema do bloco 3 ja deixou especificado com as 18 celulas recomputadas e as regras de
  elegibilidade executaveis. Ela agora tem casca para viver dentro, catalogo que a lista e pagina
  de divulgacao de afiliados ja publicada, que era o que faltava. Alternativa que nao depende de
  nada: as categorias REJUNTE e PASTILHA do banco.

11/09/2026 13:47Z — BLOCO 3c ENTREGUE: a categoria REJUNTE do banco, e os tres defeitos
que ela revelou (commitado e verificado; a ilha continua NAO estando no ar)

- `dados/materiais-rejuntes.json` com **5 rejuntes Quartzolit** — ceramicas, porcelanatos e
  ceramicas (BT 2024), acrilico, epoxi e piscinas —, mais a regua propria deles no esquema
  (`versao_esquema` 2) e `ferramentas/mutacoes-rejunte.py`. Manifest na revisao 5; a casca
  subiu para 1.1.0.
  sha256 rejuntes:  `ver manifest.json` (recalculado nesta execucao junto com esquema,
  constantes, especificacao, validador, teste-casca e casca)
- **Por que este bloco e nao a F2, que o registro anterior indicava.** A F2 se chama
  "seletor de cola E REJUNTE" e o banco tinha **zero** rejuntes: metade da resposta dela
  sairia cravada na prosa do snippet em vez de recomputada da declaracao, que e exatamente o
  que o esquema do bloco 3 existe para impedir. E o desembarque esta bloqueado por rede, entao
  um bloco publicavel nasceria sem poder ser conferido no ar (secao 8: nao se marca sucesso
  sem medir). O REGISTRO do 3b ja nomeava esta alternativa.

- **O QUE A CATEGORIA DESCOBRIU SOBRE O PROPRIO BANCO: rejunte nao e cola.** Na cola, a lista
  do fabricante nomeia a **base** — a superficie sobre a qual se cola. No rejunte, a mesma
  lista nomeia a **tessela** e o **ambiente**: "ceramicas, pastilhas de porcelana e de vidro"
  e o que vai ser rejuntado, nunca o vaso de cimento embaixo. Rejunte nao toca a base. Por
  isso a categoria ganhou `mapa_de_termos_do_rejunte` (que traduz para ambiente e tessela,
  nunca para base), `regras_de_elegibilidade_do_rejunte`, `perfis_esperados_do_rejunte` e
  `matriz_esperada_do_rejunte` — e a variavel que decide passou a ser a LARGURA DA JUNTA.
  Uma diferenca de regra que vale ser lida antes de discordar: o rejunte tem **tres** ambientes
  criticos e a cola tem dois, e o que entra e `interno_molhado`. Nao e inconsistencia, e
  geometria: a cola fica escondida atras da tessela e a agua chega nela por ultimo; o rejunte e
  a superficie exposta, a agua fica parada em cima dele e e nele que o mofo cresce.

- **DEFEITO 1 — latente, e medido antes de consertado.** `computar_celula()` varria TODOS os
  materiais do banco sem olhar categoria. As 18 celulas da F2 passavam so porque o banco so
  tinha cola: o primeiro rejunte gravado fez **as 18 falharem de uma vez**, cada uma acusando
  os cinco rejuntes como "eliminados por silencio" — frase sem sentido para um produto que
  nunca foi candidato a colar nada. O conserto tentador seria colar os cinco ids nas 18
  celulas do esquema: a matriz voltaria ao verde dizendo uma bobagem. O conserto certo foi
  declarar `categoria_considerada: cola` na matriz e conferir isso em codigo, com trava de
  regressao que reprova rejunte em qualquer lista da matriz da F2.

- **DEFEITO 2 — um numero FALSO que ja estava NO AR.** O cartao "Rejuntes" do Guia trazia
  `'no_banco' => 0` digitado a mao, no mesmo dia em que a categoria ganhou cinco produtos. O
  `teste-casca` nao viu porque conferia so a categoria **cola**, a unica que existia quando ele
  foi escrito — a mesma familia da cicatriz da secao 8 do contrato: regua que so mede a metade
  que ja existia. Casca **1.1.0**: `cdm_casca_numeros()` passa a contar o banco por categoria,
  e os totais de "esperando link" e "sem imagem" da ilha so assumem a via viva do Sync quando
  TODOS os bancos chegaram (somar metade das categorias daria um total menor e com cara de
  verdadeiro). O teste passa a cobrar as **seis** categorias e nos dois sentidos: categoria do
  Guia sem arquivo de banco mapeado reprova, e arquivo de banco sem cartao no Guia tambem —
  dado colhido que a tela nunca mostra e trabalho jogado fora.

- **DEFEITO 3 — de metodo, e apanhado no proprio ato.** Uma busca feita com o numero `1,55`
  escrito DENTRO da consulta devolveu `1,55` como se fosse declaracao do fabricante. Foi
  descartada: pergunta que carrega a resposta nao mede nada. Uma segunda, com pergunta limpa,
  generalizou o 1,75 do cimenticio sem citar documento do epoxi, e ainda inventou uma
  justificativa para o numero — tambem descartada. A pendencia `rejunte-CR-por-tipo` continua
  aberta e **virou limite declarado da ferramenta**, nao um "seria bom ter": dos cinco produtos,
  o acrilico e monocomponente pronto uso em pote de 1 kg e o epoxi e bicomponente fracionado, e
  o CR 1,75 sai de um exemplo de **po**. A coluna de rejunte da F1 passa a dizer na tela que
  vale para rejunte CIMENTICIO.

- **O ACHADO DE MAIOR VALOR E TAMBEM O QUE ELE NAO RESOLVE.** O *rejunte piscinas quartzolit*
  e o unico material do banco inteiro cujo fabricante nomeia **"pastilhas de porcelana e de
  vidro"** em uso submerso — a tessela do mosaico no ambiente mais critico do vocabulario. E
  mesmo assim ele NAO e recomendado em celula nenhuma, por dois motivos que a pagina diz com
  todas as letras: (1) a faixa de junta dele nao foi obtida — a unica mencao e de PROCEDIMENTO,
  "juntas com ate 3 mm devem ser molhadas antes", e ler 3 mm como maximo inverteria a frase do
  fabricante —, entao a regra 1 o mantem fora; e (2) o que ele declara e **agua TRATADA
  quimicamente**, que e piscina, e nao a agua parada de uma fonte ou de um vaso de jardim.
  O lado do rejunte ganhou resposta de verdade (o epoxi: junta de 1 a 5 mm, liberacao em 7
  dias, boletim 2018-01, nivel 2), mas **peca submersa precisa de cola tambem**, e a unica
  declaracao de colagem submersa da ilha continua sendo o press release do Durepoxi, nivel 4.
  A faixa fica declarada como descoberta. Meia resposta escrita como meia resposta ainda e a
  resposta mais util da pagina; meia resposta escrita como resposta inteira e o defeito.

- **VERIFICACAO** (secao 8): `php -l` limpo; `validar-banco.py` com 18 celulas de cola + 9 de
  rejunte + 5 perfis, todos conferidos contra o que esta escrito **A MAO** no esquema, escrito
  antes de rodar o validador; `teste-casca.php` com **137** afirmacoes (eram 127); 33 medicoes
  em Chromium de verdade, 0 px de rolagem em 360/390/781/782/783/1200 px nas oito paginas, com
  a trava 0 confirmando que as paginas medidas tem tamanho de pagina (corpo de 1.557 a 5.915
  caracteres).
- **QUATORZE MUTACOES DELIBERADAS, todas reprovadas.** Doze em `mutacoes-rejunte.py` (junta com
  1 mm a mais, faixa pela metade, faixa invertida, faixa inventada para o rejunte piscinas,
  epoxi perdendo a piscina, ambiente generico cobrindo sol e chuva, grade deixando de pisar na
  borda de 4 mm, rejunte voltando a entrar na matriz da cola, fonte de blog sustentando
  recomendacao, rejunte sem perfil escrito, cabecalho mentindo sobre itens esperando link) mais
  duas na casca (o zero cravado de volta no cartao, e categoria do Guia sem arquivo mapeado).
  **A que mais vale e a decima segunda:** ela tira a declaracao do banco E ajusta o perfil
  esperado no esquema junto, que e como um editor de verdade mexeria nas duas metades — as duas
  passam a errar juntas e a conferencia de perfil deixa de ver. Quem viu foi a **matriz**, que
  continuava esperando o epoxi no topo da celula de 3 mm submersa. E a prova de que a matriz
  nao e enfeite da conferencia de perfil, e a resposta local a cicatriz da secao 8.
- A grade da matriz do rejunte pisa **exatamente** em 1, 2, 4, 5 e 10 mm — os extremos
  declarados pelos cinco produtos — e em 6 e 11, logo depois do ultimo. Grade de passo fixo nao
  separaria "ate 4" de "ate 5", e o validador reprova se alguem tirar uma borda da grade.

- **10 itens esperando link de afiliado e 10 sem imagem**: os 5 de cola, inalterados, mais os 5
  de rejunte. Geracao de link e da Sentinela estrategica, no navegador, nunca da Fundacao.
- **O DESEMBARQUE CONTINUA NAO ACONTECENDO, e agora sao DUAS revisoes presas (4 e 5).** `curl`
  para o Sync e para o `/status` devolveu **000** as 13h46Z, e o `$HTTPS_PROXY/__agentproxy/status`
  registrou `connect_rejected: gateway answered 403 to CONNECT` para `clubedomosaico.com.br:443`.
  **A medicao que aponta a causa, e que nao existia no registro de 11h49Z:** na mesma execucao,
  `aquametria.com.br` e `robometria.com.br` responderam **200**. Nao e a nuvem que nao alcanca
  site nenhum — e o dominio da ilha 3 que nunca entrou na lista Personalizada do ambiente, que
  foi montada quando so existiam duas ilhas. E conserto de um minuto, do Raphael, no seletor de
  ambiente. Nao foi marcado em `bloqueada_por` de proposito: a ilha tem trabalho de sobra que
  nao depende do site, e marca-la bloqueada a tiraria da fila.
- Nao houve memoria disponivel nesta execucao (`/areas` nao existe no ambiente), como nos blocos
  1, 2, 3 e 3b. O estado vive no `ESTADO.md` desta pasta.
- Proximo passo desbloqueado: **bloco 4 — a ferramenta F2**, que agora tem as DUAS metades no
  banco e ganhou uma entrada nova, escrita no esquema e na especificacao: a **largura da junta em
  milimetros** ("quanto espaco voce deixa entre uma pastilha e outra?"), sem a qual nao ha como
  escolher rejunte. Alternativa que nao depende de rede nem de site: as categorias **PASTILHA** e
  **ALICATE** — mas atencao, a PASTILHA e de outra natureza, porque os campos que ela exige (passo
  de fabrica, espessura, peso unitario, unidade de venda) nao existem em boletim de fabricante e
  sim em anuncio de loja, nivel 5 e 6 da escada, e nenhum desses dominios foi testado ainda.
