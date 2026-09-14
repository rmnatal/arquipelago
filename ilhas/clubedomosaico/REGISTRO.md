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

11/09/2026 17:55Z — DESPACHO DO RAPHAEL CUMPRIDO E CONFERIDO NO AR: cabeçalho claro, a voz da ilha, e a home que deixou de ser manifesto (casca 1.2.0, manifest na revisão 6, `/status` conferido)

- **A reclamação era uma coisa só, não duas.** *"Muito ruim o fundo preto no
  header, o logo sumiu, queria algo mais clean."* O logo sumia porque o arquivo
  entregue tem **fundo preto** com wordmark vinho — e o cabeçalho era preto
  porque era a única cor em que aquele arquivo aparecia. Trocar só o fundo
  faria o logo virar um retângulo escuro em cima do branco; trocar só o logo
  deixaria o bloco preto que ele reprovou. Os dois saem juntos ou nenhum sai.
- **O cabeçalho:** papel `#FFFFFF` com linha de 1 px em `#E9DCD7` (a linha da
  seção 6 do contrato, no lugar de sombra), menu em `#1F1715` peso 500 com
  passagem em coral, painel do menu sanfona também claro, `theme-color` branco.
  Medido **no navegador**, não no texto do CSS: `rgb(255, 255, 255)` de fundo e
  `rgb(31, 23, 21)` no menu, nas nove páginas. A paleta **não** ganhou cor nova:
  o despacho sugeria `#FBF7F4`, `#EEE8E4`, `#111` e `#E8483A`, e os quatro são
  vizinhos de um a quatro passos dos tokens já aprovados em 10/09. Um segundo
  coral a quatro unidades do primeiro é defeito, não identidade — então valeram
  papel, traço, tinta e coral da ilha. Se o Raphael quiser exatamente aqueles
  hexadecimais, é uma linha.
- **A marca virou o wordmark "clube do mosaico" em TEXTO**, na tipografia da
  identidade (Outfit 600, vinho, minúsculas de verdade e não `text-transform`,
  para quem usa leitor de tela ouvir o nome como ele é escrito). Contraste
  medido no navegador: 17,62:1 do menu e 12,97:1 do wordmark sobre o cabeçalho.
- **O ACHADO QUE NÃO ESTAVA SENDO PROCURADO, e que muda o desenho:**
  `identidade/logo/lotus-512.png` — o símbolo transparente que o despacho manda
  usar no cabeçalho claro — está **TRUNCADO no repositório**. O chunk `IDAT`
  declara 11.638 bytes num arquivo que tem 8.770, com um `IEND` colado no fim.
  Não é imagem cortada pela metade: tentei recuperar o pedaço que existisse e o
  `zlib` recusa o **primeiro** bloco ("invalid code lengths set"), então não sai
  um único pixel. Publicá-lo teria trocado o logo sumido por um ícone de imagem
  quebrada, que é pior porque parece descuido em vez de obra em andamento. A
  metade que existe do par foi ao ar; a lótus fica pendente com o Raphael.
  `ferramentas/gerar-marca.php` nasceu para embuti-la e **recusa** arquivo que
  não abre — confere chunk a chunk, cobra canal alfa e cantos transparentes, e
  sai com código 1 sem tocar no snippet. Rodada hoje: recusou, com o número de
  bytes que faltam na mensagem.
- **A HOME (molde LOJA do `VOZ.md`, seção 15 do contrato).** Abria com três
  parágrafos de método, e o terceiro era a ficha técnica de um silicone com
  código de documento e lista de superfícies proibidas. **Duas dessas frases
  estão literalmente na lista de "Proibidas" do `VOZ.md`** — não é coincidência:
  a lista foi escrita para proibir aquele texto. Agora a home abre por "Mosaico
  feito à mão, uma peça por vez", segue com a vitrine (estado vazio honesto,
  reescrito curto), o bloco "Vai fazer o seu? A gente ajuda a escolher o
  material" e a artesã fechando a página. O número e a fonte **não sumiram do
  site**: mudaram de lugar.
- **A home deixou de se chamar "Início"** — e o defeito por trás disso é que
  valia mais: `garantir_paginas()` nunca sincronizava título, então a página
  nascia com o título da definição e ficava com ele para sempre. Era assim que
  "Início" sobrevivia às versões da casca. Agora sincroniza, **sem tocar em
  `post_name`** (seção 12.1: URL publicada não se move). De quebra, a casca
  passou a gravar `blogname` e `blogdescription` como já gravava
  `page_on_front`: o `<title>` da home no resultado de busca agora diz "Clube do
  Mosaico – Mosaico feito à mão, uma peça por vez", que é a mesma frase da
  página e do rodapé. É a lição da Aquametria de 11/09 aplicada antes de doer.
- **O GUIA perdeu sete seções de bastidor**, que não foram jogadas fora: mudaram
  para **`/materiais/como-sabemos/`**, primeira página de nível 2 desta ilha
  (seção 16), com mãe declarada, `noindex` e fora do sitemap. Ela ficou com
  4.340 caracteres de corpo — não é página fina. No Guia ficaram as seis
  prateleiras, com os resumos reescritos na voz, e o único achado que muda a mão
  de quem faz: silicone acético não serve em espelho nem em cimento, e o neutro
  do mesmo fabricante serve.
- **"Hoje 10 dos 5 itens esperam link" SAIU DO AR.** Os dois números estavam
  certos sozinhos — 10 itens esperando link no banco inteiro, 5 adesivos na
  categoria cola — e a frase que os juntou era impossível. Foi exatamente por
  isso que nenhum teste viu: cada metade era conferida separada. O denominador
  passou a ser `itens_no_banco`, somado das categorias, e a página de
  divulgação parou de **afirmar por escrito** que não há link nenhum: agora é a
  subtração entre o que existe e o que espera.

**VERIFICAÇÃO — 198 afirmações na bancada (eram 137), 54 medições em Chromium, 19 mutações, e a conferência no ar.**

- **A bancada estava medindo oito das nove páginas pela metade, e ninguém
  sabia.** A trava nova de "página inteira" reprovou de primeira: o rodapé saía
  só na primeira página. A causa é um `static` legítimo em
  `cdm_casca_rodape_impresso()` (e outro em `cdm_casca_marca_html()`), que
  existe para o rodapé não sair duas vezes na MESMA página — no site um processo
  é uma requisição e ele está certo. Numa varredura de nove páginas em
  sequência, ele faz o rodapé aparecer na primeira e sumir nas oito seguintes,
  **sem erro nenhum**. É a terceira vez que o Arquipélago paga por isso, e a
  regra do contrato já estava escrita: varredura de muitos estados roda **um
  processo por estado**. O teste passou a fazer isso. E a conferência de "página
  inteira" deixou de ser um número redondo de bytes (que eu não consigo calibrar
  sem o site no ar, e número redondo não é critério) e virou a lista do que uma
  página desta ilha obrigatoriamente carrega: folha, JSON-LD, menu, comando do
  menu, favicon, rodapé e H1.
- **19 mutações deliberadas em `ferramentas/mutacoes-voz-e-cabeca.py`, 19
  reprovadas — mas DUAS passaram na primeira rodada**, e são o resultado do
  teste:
  1. *"o título para de sincronizar"* passou porque a bancada monta o H1 a
     partir da **definição**, e a definição está certa. O defeito mora no outro
     lado, no caminho que atualiza a página que já existe — e medir o H1 servido
     nunca poderia vê-lo. Trava nova: o teste simula o site real de hoje (as
     páginas existem, com os títulos velhos) e afirma sobre o que a casca **manda
     gravar**, inclusive que nenhuma gravação toca `post_name` e que página que
     não é da casca não tem o título reescrito.
  2. *"noindex na página errada"* passou porque o teste conferia que a etiqueta
     sai nas páginas **declaradas** — o que é verdade mesmo quando alguém declara
     a página errada. Conferir a declaração contra ela mesma é a mesma forma do
     teste que mede a si mesmo. Régua nova, vinda de fora: só a página de camada
     de prova pode sair do índice, e nenhuma página do menu pode.
- **As duas mutações que mais valem são as portas dos fundos do portão de voz**,
  e as duas reprovam: embrulhar o Guia inteiro na classe que declara camada de
  prova, e declarar uma **segunda** página como página de prova. Sem contar os
  blocos, medir onde eles começam e exigir que a página de prova seja uma só, o
  portão se desligaria com uma linha e nenhuma palavra mudaria na tela — que é
  exatamente a porta que a Aquametria achou ao tentar quebrar o próprio portão.
- **NO AR às 17h55Z:** `/status` com revisão 6, igual à do manifest. 9 de 9 URLs
  em 200, a nova inclusive. Zero `&#038;` dentro de `<script>` nas nove
  (contado só dentro dos blocos de script). Um rodapé por página. O `H1` da home
  é a frase da voz e nenhuma das três frases proibidas aparece no corpo dela. O
  Guia diz "10 itens de fabricante" e não diz "10 dos 5". `/materiais/como-sabemos/`
  serve `noindex` e **está fora** do `wp-sitemap-posts-page-1.xml`, enquanto
  `/materiais/` continua dentro — as duas direções medidas.
- **A REDE ALCANÇA ESTA ILHA, e o bloqueio anterior era diagnóstico não
  reconferido.** O `ESTADO.md` dizia "403 ao CONNECT para clubedomosaico.com.br,
  segunda execução seguida" e duas revisões presas. Nesta execução o primeiro
  `curl` à home devolveu `000` — e **o mesmo comando, repetido minutos depois,
  devolveu 200**, assim como o Sync, o `/status`, as nove páginas e o sitemap. A
  falha era intermitente, não bloqueio. A lição fica escrita: bloqueio que não é
  reconferido a cada execução vira permanente sozinho, e prendeu duas revisões
  desta ilha por duas execuções.

**10 dos 10 itens do banco ainda esperam link de afiliado; 10 sem imagem.** Este
bloco não tocou catálogo.

**Próximo passo:** a árvore da seção 16 inteira — `ARVORE.md` da ilha, mãe para
toda página existente, breadcrumb com `BreadcrumbList` e blocos "Veja também"
(16.4). `/materiais/como-sabemos/` já nasceu dentro dela e serve de primeiro
caso. Nenhuma categoria de nível 2 do Guia tem as 3 filhas que a 16.5 exige,
então nenhuma nasce agora. Depois disso, o bloco 4 (a ferramenta F2).

---

## 11/09/2026 19h40Z — A ÁRVORE DA SEÇÃO 16, e nenhuma URL se moveu

Casca **1.3.0**, manifest na **revisão 7**. Bloco nomeado como próximo passo pela
execução das 17h55Z e pelo despacho do Raphael de 11/09, cuja última linha dizia
que a árvore era o bloco seguinte.

**O que foi entregue**

- **`ARVORE.md`** (item i do 16.8): os três níveis com slug, onde mora cada uma
  das nove páginas que existem, o que está travado e por quê. É o mapa que os
  blocos seguintes seguem — e o teste lê este arquivo para cobrar que documento e
  código digam a mesma coisa, porque duas metades mantidas à mão em lugares
  diferentes divergem em silêncio.
- **Trilha (16.3)** em oito das nove páginas; a home não tem, que é o que a regra
  manda. Ela nasce entre o cabeçalho e o H1, pelo filtro do bloco
  `core/post-title`, com cinto de segurança no `the_content` para o caso de a
  página não ter aquele bloco.
- **`BreadcrumbList`** em JSON-LD nas mesmas oito.
- **Cluster "Veja também" (16.4c)** nas três seções de nível 1, cada uma listando
  as outras duas: é o ciclo LOJA → GUIA → ESCOLA, que é a razão de esta ilha ter
  três motores num domínio só.

**ESTA ILHA NASCEU COM A ÁRVORE CERTA E NÃO SABIA.** Nenhuma página mudou de
endereço neste bloco, e nenhuma precisou: as três seções já eram nível 1, a única
página de nível 2 já nascera com mãe em 1.2.0, e as quatro da raiz são exatamente
as que a 16.1 admite ali. Por isso **não há um 301 sequer e o sitemap não muda** —
o que faltava era a árvore ficar **visível** (trilha, schema, cluster), que é o
que a 16.3 e a 16.4 pedem. Nas outras duas ilhas o nível 1 ainda é página
inexistente e a trilha sai com degrau em texto; aqui os três degraus de topo são
link de verdade desde o primeiro dia.

**AS DUAS COISAS ERRADAS QUE ESTE BLOCO ACHOU SEM PROCURAR**

1. **O registro do Guia e o `VOZ.md` discordavam nos slugs de duas categorias**
   desde que a casca nasceu: o código dizia `materiais/colas` e `materiais/alicates`,
   o `VOZ.md` dizia `colas-e-adesivos` e `alicates-e-corte`. Nada no repositório
   cobrava os dois juntos, e a divergência só apareceria no dia em que a página
   nascesse — quando já seria URL publicada, que não se move. **O dia de acertar
   é o dia ANTES de a página existir.** Corrigido para o nome do `VOZ.md`, que é
   quem manda no nome do nível (seção 15.1), e agora há trava: todo slug de
   categoria do Guia tem que ser um nome escrito no `VOZ.md`.
2. **O cartão da categoria que ainda não abre publicava contagem de banco** —
   "5 no banco, ficha em construção". O número era certo e era contado do arquivo;
   o problema é outro, e a 16.5 o nomeia: cartão que não é link diz "em breve",
   **sem contagem**. É promessa com número colada num lugar que não se pode
   visitar. O número não sumiu do site: continua na camada de prova do Guia e na
   página Como sabemos (15.2), contado, que é onde quem quer conferir confere.
   O campo `no_banco` continua existindo e continua sendo cobrado contra o
   arquivo — o que mudou foi ele deixar de ir para a TELA daquele cartão.

**O SCHEMA PUBLICA MENOS DO QUE A TRILHA MOSTRA, de propósito.** Um `ListItem`
intermediário sem `item` invalida o `BreadcrumbList` inteiro para o Google, e
lista inválida é lista ignorada — então o schema "mais completo", que levaria
também o degrau sem página, publicaria MENOS com cara de publicar mais. Hoje isso
não corta nada nesta ilha, porque os três degraus de nível 1 existem: a via foi
escrita para o dia em que a primeira ficha de material nascer antes da categoria
dela, que é o estado normal das outras duas ilhas.

**A BANCADA ESTAVA MEDINDO FORA DE ORDEM, e a própria trava pegou.** A primeira
versão do render rodava `the_content` **antes** do bloco de título. No site a
ordem é a inversa — o `core/post-title` renderiza primeiro —, e por isso a trilha
nasce acima do H1. Na bancada invertida o cinto de segurança de prioridade 9
disparava, a trilha caía dentro do corpo, e **oito páginas foram reprovadas por
um defeito que só existia na bancada**. Quarta vez que o Arquipélago paga por
render que serve diferente do site; desta vez a conta veio em minutos porque a
trava media a POSIÇÃO da trilha, não a presença dela.

**AS DUAS MUTAÇÕES QUE PASSARAM, E POR QUE ELAS VALIAM MAIS QUE AS DEZESSETE QUE
REPROVARAM.** `ferramentas/mutacoes-arvore.py` quebra a árvore de propósito, uma
mutação por vez. Na primeira rodada, 17 de 19 reprovaram — e as duas que passaram
não passaram por a trava ser fraca: passaram por serem **inertes**.

- *"degrau de trilha vira link morto"* trocava o `<span>` do degrau sem página por
  um `<a>`. Só que **nenhuma página desta ilha tem degrau sem página hoje**, então
  o ramo nunca é executado e o site servido é byte a byte o mesmo.
- *"cluster publicado com uma irmã só"* baixava o piso de 2 para 1 irmã. Só que
  nenhuma página desta ilha tem **exatamente uma** irmã no ar — elas têm zero ou
  duas.

É a cicatriz da grade que não pisa na borda, com a borda faltando no **mundo** e
não no teste. A saída foi a mesma do modo `todas` do render: **a bancada fabrica
a borda**, aqui pelo filtro `cdm_arvore`, que é o mesmo por onde uma página nova
entrará no mapa de verdade. As duas situações fabricadas são as duas que esta
ilha vai ter — a ficha nascendo antes da categoria, e uma categoria com uma irmã
só. Com elas, as 19 de 19 reprovam.

**VERIFICAÇÃO em bancada:** `teste-casca.php` com **327 afirmações** (eram 198),
um processo por página; `php -l` limpo nos dois snippets; `validar-banco.py`
aprovado; `mutacoes-arvore.py` 19 de 19 reprovadas; `mutacoes-voz-e-cabeca.py`
19 de 19 e `mutacoes-rejunte.py` 12 de 12 continuam reprovando (nada deste bloco
afrouxou trava anterior).

**NO AR às 19h40Z:** Sync acionado por `curl`, `/status` com **revisão 7**, igual
à do manifest. **9 de 9 URLs em 200** e **117 afirmações medidas no HTML
SERVIDO**, sem uma falha:

- zero `&#038;` dentro de `<script>` nas nove (contado só dentro dos blocos de
  script, 7 na home e 8 nas outras);
- trilha em 8 de 9, sempre **antes do H1** e **uma só por página**; a home não
  tem, e também não publica `BreadcrumbList`;
- nenhum degrau aponta para página inexistente; a trilha de
  `/materiais/como-sabemos/` tem os três degraus e o do meio **linka** a mãe;
- `BreadcrumbList` nas oito, todo `ListItem` com `item`, posições de 1 a n sem
  buraco, e a relação que importa conferida uma a uma: **os itens do schema são
  os degraus linkados da trilha mais a página atual**;
- "Veja também" em 3 de 9 — exatamente as três seções, com 2 irmãs cada, nenhuma
  irmã morta e nenhuma página se listando como irmã de si mesma;
- os **6 cartões** de categoria do Guia servem "Em breve", **sem um dígito** e
  **sem serem link** (16.5), enquanto a camada de prova continua publicando 5
  colas e 5 rejuntes contados do banco;
- o `wp-sitemap-posts-page-1.xml` continua com as mesmas 8 URLs, e
  `/materiais/como-sabemos/` continua fora dele.

**10 dos 10 itens do banco ainda esperam link de afiliado; 10 sem imagem.** Este
bloco não tocou catálogo. Da pauta da seção 17: **nenhum tema escrito, nenhum na
fila, nenhum recusado** — `pauta.md` ainda não existe nesta pasta.

**Próximo passo:** o **bloco 4 — a ferramenta F2** ("qual cola e qual rejunte
para a sua peça"), que é a primeira página de nível 3 desta ilha e o primeiro
caso real do degrau de trilha sem página, já coberto pela borda fabricada na
bancada. Ela nasce com o bloco de compra da seção 7 junto, mesmo com
`afiliado.url` vazio, e com a mãe `/materiais/` declarada no `ARVORE.md`. Só
depois dela uma categoria de nível 2 chega perto das 3 filhas que a 16.5 exige.

---

## 11/09/2026, 20h35Z — O LOGO DELE, INTEIRO, NO CABEÇALHO (despacho do Raphael de 11/09 (2), cumprido inteiro)

**Casca 1.4.0, manifest na revisão 8, `/status` com revisão 8.** Despacho de
prioridade máxima, e a seção 18.2 manda ele sair inteiro: os **cinco itens**
saíram nesta execução, não um por passada.

**O que o cabeçalho serve agora:** `logo-clube-do-mosaico.png` em `<img>` de
52 px de altura, com link para a home e **nenhuma letra ao lado**. O nome está
desenhado dentro da imagem; escrevê-lo de novo seria a marca em dobro na tela e
anunciada duas vezes por leitor de tela. Por isso não existe `<span>` nenhum ali
e quem carrega o nome para quem não vê a imagem é o `alt`. A barra do cabeçalho
subiu de 72 para 84 px, e abaixo de 600 px o logo desce para 44 px — com 52, ele
e o botão do menu não cabem na mesma linha a 360 px.

### A afirmação que sustentava a versão anterior estava errada

Estava escrita em **três lugares do snippet e um do `VOZ.md`** desde 1.2.0: *"o
arquivo entregue tem fundo preto"*. **Não tem** — é transparente, e o Raphael
conferiu na biblioteca de mídia. O logo sumiu em 1.1.0 porque o **cabeçalho** era
preto e o wordmark dentro do arquivo é vinho `#69030C`: defeito de **onde o logo
foi posto**, nunca do arquivo. A 1.2.0 consertou a causa — clareou o cabeçalho —
e, pela leitura errada do sintoma, tirou junto o logo, que era a parte certa.

Fica escrito porque a forma se repete: **sintoma não é causa, e um diagnóstico
escrito com ar de fato se propaga por versões**. É o mesmo desenho do `000` lido
como bloqueio de rede na semana passada, que prendeu duas revisões desta ilha por
dois dias até alguém repetir o comando.

### 1,26 MB num espaço de 78 px — e por que isso não é "processar o logo"

O arquivo dele é o original de 1536×1024 e a marca ocupa 78×52 px na tela.
Servi-lo cru seria 1,26 MB em toda página de um domínio recém-nascido, e
orçamento de rastreamento é a primeira coisa que o Google mede num domínio assim.
**Não se redesenha nem se gera nada** — o `PROMPT.md` proíbe, e tem razão: o
`src` continua sendo a URL exata que o despacho mandou usar, e o `srcset` oferece
as reduções que o **próprio WordPress** gerou do upload dele (`-300x200` com
41 KB, `-768x512` com 175 KB), com `sizes="78px"`. Mesma imagem, mesmo recorte,
mesma origem; quem ignorar o `srcset` baixa o original e vê a mesma coisa. Medido
no navegador: a escolhida foi a de 41 KB.

### As mutações, que é onde o teste vira teste

Seis novas, e a antiga **"logo de fundo preto volta ao cabeçalho claro" foi
aposentada**: ela media o mundo ao contrário — lá o defeito era o logo *entrar*,
aqui é ele *sair*. Mutação que edita a regra antiga vira **inerte** quando a
regra muda de lado, e inerte é verde sem medir nada.

**Duas passaram na primeira rodada, pelo mesmo motivo de sempre:** não acharam o
alvo, porque as linhas do `<img>` foram escritas na mutação sem as duas
tabulações que o arquivo tem. Mutação que não consegue ser escrita é verde que
não mediu nada. Reescritas, as duas morderam: `0x0` de medida declarada e `alt`
vazio.

**A que mais vale da leva é a porta dos fundos do `srcset`:** o `src` fica certo
no código e outra imagem entra no lugar do logo por um atributo que ninguém lê. O
portão passou a cobrar que **todo candidato seja o mesmo arquivo com sufixo de
tamanho**.

### Verificação

Bancada: `teste-casca.php` de **327 para 347 afirmações**, um processo por página
— o `static` de `cdm_casca_marca_html()` é exatamente o mecanismo que faria o logo
sair na home e sumir nas outras oito numa bancada de um processo só, e agora há
uma afirmação por página cobrando isso. `mutacoes-voz-e-cabeca.py` de 19 para
**24 mutações, 24 reprovadas**; `mutacoes-arvore.py` 19/19 e `mutacoes-rejunte.py`
12/12 seguem reprovando; `validar-banco.py` aprovado; `php -l` limpo. **63
medições em Chromium** nas nove páginas em 360/390/781/782/783/1200 com 0 px de
rolagem, incluindo a caixa de **78×52 px desenhada pelo motor de layout** — que é
a diferença entre "a regra de 52 px está escrita no CSS" e "o logo tem 52 px na
tela".

**No ar, às 20h35Z: 9 de 9 URLs em 200 e 102 afirmações medidas no HTML
SERVIDO**, nenhuma falha, por `ferramentas/conferir-no-ar.py`, que nasceu nesta
execução. Ele tem **régua própria**: a URL do logo e a medida 78×52 estão
literais dentro dele, copiadas do despacho, não lidas da constante da casca —
senão as duas metades errariam juntas. Mediu, em cada uma das nove: o `src` é o
arquivo dele, zero texto dentro da marca, `alt` com o nome, medida declarada, o
logo uma vez só, o wordmark em texto de 1.2.0 fora da página, zero `&#038;`
dentro de `<script>`, a folha servida mandando 52 px e o cabeçalho ainda claro.
As três URLs da imagem respondem PNG.

**O critério de pronto que ele escreveu era de olho, e foi conferido de olho:** a
home **servida** foi desenhada em Chromium com os bytes reais da imagem, e o logo
foi ampliado pixel a pixel. A lótus e o nome "clube do mosaico" embaixo, nítidos
sobre o branco, sem texto duplicado ao lado.

### Duas coisas registradas para ele poder discordar

1. **A 52 px o wordmark dentro do logo fica com ~8 px por linha.** Lê-se como
   logotipo, mas é pequeno — o arquivo é um lockup empilhado e 52 px é o número
   do próprio despacho. Os dois caminhos (subir para ~64 px, ou uma versão
   horizontal do lockup) são escolha dele, não da Fundação.
2. **Os hexadecimais sugeridos no despacho continuam fora**, como em 11/09:
   `#FBF7F4`, `#EEE8E4`, `#111` e `#E8483A` são vizinhos de um a quatro passos
   dos tokens que ele aprovou em 10/09. Um segundo branco a quatro unidades do
   primeiro é defeito, não identidade. Se ele quiser exatamente aqueles valores,
   é uma linha.

**10 dos 10 itens do banco seguem esperando link de afiliado; 10 sem imagem.**
Este bloco não tocou catálogo. Da pauta da seção 17: **nenhum tema escrito,
nenhum na fila, nenhum recusado** — `pauta.md` ainda não existe nesta pasta.

**Próximo passo:** o **bloco 4 — a ferramenta F2**, primeira página de nível 3
desta ilha e o primeiro caso real do degrau de trilha sem página, já coberto pela
borda fabricada na bancada. Nasce com o bloco de compra da seção 7 junto, mesmo
com `afiliado.url` vazio, e com a mãe `/materiais/` declarada no `ARVORE.md`.

## 11/09/2026, 22h05Z — BLOCO 4: A F2 NO AR, a primeira ferramenta da ilha

**Entregue:** `/materiais/qual-cola-usar-no-mosaico/` — snippet
`clubedomosaico-f2.php` v1.0.0, casca 1.5.0, manifest na revisão 9,
`/status` com revisão 9. Primeira ferramenta do Clube do Mosaico e
primeira página de **nível 3** da ilha.

### A decisão que decide todas as outras: a resposta é servida pelo SERVIDOR

O formulário é um `GET` para a própria página e o PHP monta a resposta.
**Não existe uma linha de decisão em JavaScript** — o script do rodapé só
evita o recarregamento quando a pessoa troca uma opção, e a página funciona
inteira sem ele. Duas coisas saem de graça dessa escolha, e as duas são
cicatriz do Arquipélago:

1. **Todo estado da entrada é HTML servido de verdade.** A seção 5 do contrato
   diz que ferramenta que calcula no navegador mostra a um modelo de linguagem
   um formulário vazio; aqui qualquer uma das 45 combinações de base × ambiente
   é uma página com a resposta escrita nela.
2. **Não há régua duplicada entre PHP e JS para as duas se separarem em
   silêncio.** Era o caminho mais curto para o defeito clássico de duas metades
   que erram juntas — ou pior, separado.

O preço é URL com parâmetro, e ele é pago na mesma linha: estado com parâmetro
sai com `noindex, follow` e `canonical` para o endereço limpo. Quem entra no
índice é a página-âncora, uma só, e ela carrega as duas tabelas inteiras
(seções 14.1 e 14.4).

### A elegibilidade é recomputada, nunca digitada

As cinco regras da cola e as quatro do rejunte estão em
`dados/esquema-banco.json` e agora têm **duas implementações independentes**:
`ferramentas/validar-banco.py` em Python e o snippet em PHP. As duas são
conferidas contra as matrizes escritas **à mão** no bloco 3 — 18 células de
base × ambiente e 9 de folga × ambiente. A categoria continua sendo parte da
pergunta: a régua da cola decide sobre **base**, a do rejunte sobre **largura
de junta**, e rejunte não toca a base.

### O QUE O RENDER MOSTROU NO PRIMEIRO SEGUNDO, e que nenhum teste procurava

A primeira página montada na bancada dizia **"Silicone Acetico Construcao"** e
**"o fabricante declara ceramica e azulejo"**. O banco inteiro estava sem
acento — 122 strings de tela, escritas assim desde o bloco 2, porque foram
digitadas a partir de busca e porque **até aqui nenhuma página as servia**. No
dia em que uma página passou a servi-las, o defeito virou texto no ar. É a
mesma coisa que a Robometria pagou em 11/09/2026, com 121 strings.

`ferramentas/restaurar-acentos.py` devolveu os acentos em **68 trocas**, e a
operação é **provada diacrítico-only**: reduzidos a sem-diacrítico, os dois
arquivos do banco depois dela são byte a byte iguais aos de antes — com cinco
exceções **declaradas e conferidas uma a uma**, que são os `nome_comercial` dos
rejuntes, escritos em caixa baixa ("rejunte acrilico quartzolit") e promovidos
a nome próprio. A ferramenta imprime cada troca que faz: espelho que não
imprime o que trocou envelhece calado.

De quebra, a tela dizia **"Quartzolit Rejunte Cerâmicas Quartzolit"** — os
cinco rejuntes têm a marca dentro do nome comercial e as cinco colas não.

### A VARREDURA ACHOU UM ESTADO QUE A FERRAMENTA NÃO ACEITAVA

A grade conferida do rejunte pisa em **11 mm** de propósito: é o primeiro valor
depois do maior extremo que algum fabricante declara. O campo do formulário
parava em 10, então quem tem folga de 11 caía **calado** no padrão de 2 mm e
recebia uma resposta que não era a dele. O campo foi para 12 mm e o estado
passou a responder a verdade: nenhum rejunte do banco cobre essa folga.

### As quatro mutações que passaram, e os três buracos que elas abriram

`ferramentas/mutacoes-f2.py` nasceu com 20 mutações e, na primeira rodada,
**quatro passaram**. Nenhuma passou por a trava ser frouxa — as quatro passaram
por a trava medir o lugar errado:

1. **A lista do silêncio nunca era conferida.** A mutação que fazia a matriz da
   cola varrer o banco inteiro punha os cinco rejuntes na decisão de *colagem*
   como "eliminados por silêncio" — frase sem sentido — e o teste só olhava o
   topo e os proibidos. Agora a lista é cobrada **nos dois sentidos**: o que
   falta e o que sobra.
2. **O rejunte só era medido na FRASE, e a frase só nomeia o topo.** Duas
   mutações de faixa de junta punham o produto indevido como elegível *abaixo*
   do topo, onde ele aparece no cartão e não na frase. Recomendar em segundo
   lugar o que o fabricante não declara é recomendar.
3. **Marca em dobro não aparece em teste de conter.** "Rejunte Cerâmicas
   Quartzolit" está *dentro* de "Quartzolit Rejunte Cerâmicas Quartzolit", então
   procurar por conter aprova o nome errado que engloba o certo. A régua passou
   a ser de igualdade, e direta: para todo produto cujo nome já carrega a marca,
   a composição "&lt;marca&gt; &lt;nome&gt;" não pode existir em lugar nenhum do corpo.

E uma quinta, que é a lição mais fina do bloco: **a mutação da faixa pela
metade era INERTE**, e não por não achar o alvo. Ela trocava um `||` por `&&` e
completava as pontas que faltavam — só que o único produto sem faixa tem as
**duas** pontas nulas, então a guarda trocada continuava pegando nele e nada
mudava na tela. Mutação que acha o alvo e mesmo assim não muda o que o site
serve é verde sem medir nada, e é mais difícil de ver que a mutação que não
acha o alvo. Reescrita, ela morde.

### Dois defeitos de régua na bancada que existia

- **`[a-z_]+` não casa com `cdm_f2`.** O `teste-casca.php` mapeava shortcode →
  caminho com essa expressão, e o dígito fazia falta: a página da primeira
  ferramenta da ilha entrava na tabela com caminho **vazio**, e a trilha dela, o
  `BreadcrumbList` dela e o cluster dela passavam a ser medidos contra o nada.
  Régua estreita demais não é régua frouxa: é régua que mede outra coisa.
- **O portão da 16.5 media o cartão errado.** "Cartão de categoria não vira link
  enquanto a categoria não existir" contava TODO cartão do corpo, e no dia em
  que a primeira ferramenta virou link ele reprovou a home e o Guia por um
  cartão que está certo. As duas listagens ganharam classe própria.

### O que a página diz que não sabe

Duas faixas continuam **declaradas** como descobertas, em vez de preenchidas no
chute: **base de plástico** e **peça em contato permanente com água**. E a
página passou a separar uma coisa que não é a mesma: *declaração vaga não é
silêncio*. Dizer "o fabricante não fala" de um produto cujo fabricante escreveu
"certos tipos de plástico" seria falso — ele falou, e falou de um jeito que não
decide. As duas saem em parágrafos diferentes, com a frase dele.

O tempo de espera do PVA também virou texto: o campo existe no banco com o
motivo escrito, e a página diz que não publica o número em vez de simplesmente
não ter a seção. Ausência de seção é indistinguível de "não importa".

### Duas mudanças pequenas na casca, e nenhuma a mais (1.5.0)

1. `cdm_casca_definicao_paginas()` ganhou o filtro **`cdm_paginas`**. Era o
   único registro da casca sem filtro; sem ele, toda ferramenta nova obrigaria a
   editar a casca — e casca editada por bloco de ferramenta é casca que sai do
   ar por defeito de ferramenta.
2. **`/materiais/` passou a listar as ferramentas** (16.4a). Ela é a mãe das
   duas e não as listava; enquanto nenhuma existia isso não aparecia, e no dia
   em que a primeira nasce a falta vira página órfã. **E a listagem vem ANTES
   das seis prateleiras**: as seis são cartão "em breve" e nenhuma abre, então
   deixá-las no topo punha seis cartões mortos na frente do único caminho vivo
   da página — que é justamente o que termina numa recomendação de compra.

### VERIFICAÇÃO

- `ferramentas/teste-f2.php`: **72 afirmações**, régua própria, **um processo
  por estado** — os **45** estados de cola e os **60** de rejunte, mais a
  âncora e os estados com parâmetro. Zero falha.
- `ferramentas/mutacoes-f2.py`: **20 mutações, 20 reprovadas**.
- `ferramentas/teste-casca.php`: **367 verificações**, nenhuma falha, agora
  incluindo a página nova nos portões de voz, prova, escassez, trilha, árvore,
  página fina e entidade dentro de `<script>`.
- `ferramentas/validar-banco.py`: aprovado, com a matriz batendo com as
  declarações depois da restauração dos acentos.
- `php -l` limpo nos três snippets.
- Chromium em 360/390/781/782/783/1200 px nas doze páginas (as nove da casca,
  a âncora da F2 e dois estados dela com parâmetro): **78 medições, 0 px de
  rolagem horizontal**.
- **NO AR, às 22h05Z:** o Sync aplicou os 5 itens (snippet `f2` criado como #7,
  casca atualizada e os três arquivos do banco virando option pela primeira
  vez), o `/status` devolve **revisão 9**, e `ferramentas/conferir-no-ar.py`
  mediu **145 afirmações no HTML SERVIDO, zero falha** — as 10 URLs em 200, a
  tabela pré-renderizada servida, o JSON-LD servido, e os quatro casos de
  coerência (espelho, cimento em sol e chuva, MDF e vidro laminado) com o
  silicone acético **na seção do que não usar** e nunca na recomendação.
  O sitemap passou de 8 para **9 URLs**, a F2 recebe **dois links internos** (a
  home e a mãe) e a trilha serve os três degraus com endereço de verdade.

  **O Sync precisou de três disparos, e a razão vale registrar:** os dois
  primeiros leram do `raw.githubusercontent` um `manifest.json` ainda na revisão
  8 enquanto já baixavam a casca nova — "sha256 divergente, não aplicado", que é
  a trava funcionando. Cache de borda por caminho, não por commit: o arquivo
  novo e o índice velho chegam em momentos diferentes. Esperar e repetir
  resolve; o que não se pode é ler o primeiro "0 aplicados" como entrega.

### Números da ilha, contados

**10 dos 10 itens do banco esperam link de afiliado; 10 estão sem imagem** —
este bloco não tocou catálogo, e nenhum dos dez tem loja possível hoje. Da
pauta da seção 17: **nenhum tema escrito, nenhum na fila, nenhum recusado** —
`pauta.md` ainda não existe nesta pasta.

**Próximo passo:** a **F1**, em `/materiais/quantas-pastilhas-para-mosaico/`,
com a mesma mãe. A especificação está pronta desde o bloco 2, com a correção do
bloco 3c: a coluna de rejunte vale só para rejunte **cimentício** e a de gramas
de cola sai **vazia com explicação**, porque faltam o consumo por área da
cimentcola e o rendimento por área do silicone. Ela reaproveita da F2 o registro
de página pelo filtro, o desenho de resposta servida pelo servidor com `noindex`
no estado com parâmetro, o cartão de compra e o padrão de teste com varredura
da entrada inteira.

## 12/09/2026, 00h05Z — BLOCO 4, SEGUNDA PARTE: A F1 NO AR — e a casca que não deixava a página nascer

**Entregue:** `/materiais/quantas-pastilhas-para-mosaico/`, a segunda ferramenta
da ilha (`snippets/clubedomosaico-f1.php` 1.0.0, casca **1.6.0**, manifest na
revisão **11**, `/status` com revisão 11 às 00h05Z). Nível 3, mãe `/materiais/`,
a mesma escolha da F2 e pelo mesmo motivo.

### Por que esta página ganha, e é a única que responde isto

O bloco 1 mediu que a primeira página inteira de "rejunte para mosaico" responde
à pergunta da **obra** — 0,2 a 0,4 kg/m², "1 kg faz 3 m²" —, e esses números
foram calculados com azulejo grande. A **mesma fórmula do fabricante**, aplicada
à pastilha de 1×1 cm com folga de 2 mm, dá **2,8 kg/m²**: 3,8 vezes o azulejo de
10 cm e 2 vezes o piso de 20. A página não disputa aquelas — ela responde outra
pergunta, e serve as duas contas **lado a lado, na mesma tabela**, para a
diferença ficar verificável em vez de afirmada.

### As cinco decisões, e a cicatriz que cada uma evita

1. **A conta é do servidor**, como na F2: o formulário é um GET para a própria
   página, não existe uma linha de decisão em JavaScript, e todo estado é HTML
   servido de verdade. O preço é URL com parâmetro, pago na mesma linha —
   `noindex, follow` no estado com parâmetro, e quem entra no índice é a âncora.
2. **A geometria é nossa; o consumo é do fabricante.** Área por forma (o cone
   pela **geratriz**, nunca pela altura — num vaso bojudo a diferença passa de
   10% e sempre para menos) e contagem pelo passo são aritmética e não dependem
   de banco nenhum. Os gramas saem da fórmula publicada pela Quartzolit com o
   coeficiente **lido do registro do rejunte cerâmicas**, nunca digitado.
3. **A correção do bloco 3c está na tela.** O 1,75 vem de um exemplo de rejunte
   cimentício **em pó**; o acrílico é pronto uso em pote e o epóxi é
   bicomponente. A ferramenta recusa calcular para os dois e nomeia o que falta.
   E recusa também **se o banco trouxer dois coeficientes diferentes**: escolher
   um deles calado é a mesma invenção com outra roupa.
4. **A régua do rejunte tem dono.** `cdm_f2_celula_rejunte()` é chamada daqui em
   vez de reescrita; a F1 só filtra pelo tipo escolhido. Duas implementações da
   mesma decisão no mesmo site é o defeito que a Robometria pagou comparando
   duas cópias da mesma régua.
5. **A sobra vai na pastilha e não no rejunte**, e arredonda para cima. Lote
   novo de pastilha muda de cor: faltar dez peças no fim é pior que sobrar dez.
   O saco de rejunte não tem esse problema.

### O QUE QUASE PASSOU: a página respondeu 404 com o Sync dizendo revisão 10

O Sync aplicou seis itens, criou o snippet #8, escreveu revisão 10 no `/status`
— e `conferir-no-ar.py` devolveu **37 falhas**, todas a mesma: a URL da F1 não
existia. **Commit sem verificação no ar não é entrega**, e foi a régua que disse
isso, não a leitura do log.

A causa é da casca, e é fina: `cdm_casca_montar()` voltava na primeira linha
quando `get_option('cdm_casca_estrutura')` era igual a `CDM_CASCA_VERSAO`. A
1.5.0 tinha acabado de criar o filtro `cdm_paginas` **exatamente** para que uma
ferramenta nova registrasse a própria página sem ninguém editar a casca — e a
guarda deixava esse mecanismo inerte: página nova entrava na definição, a versão
da casca continuava a mesma, a montagem não rodava, a página nunca nascia. **A
F2 escapou porque nasceu junto com a 1.5.0** e foi de carona na troca de versão.
Mecanismo que só é exercitado de verdade na segunda vez que alguém o usa.

**Casca 1.6.0:** a chave passa a ser a versão **mais um resumo do mapa de
páginas** (slug, título, mãe e shortcode de cada uma). Página nova, título
trocado ou mãe trocada mudam a impressão e a estrutura se remonta sozinha no
primeiro carregamento depois do Sync — sem humano logado, sem `?cdm_casca=refazer`
e sem tocar na casca. Remontar é barato e seguro porque `garantir_paginas()` só
cria o que falta. O portão 21b do `teste-casca.php` **mede o mecanismo, nunca a
versão**: um teste que olhasse `CDM_CASCA_VERSAO` teria ficado verde com o
defeito no ar, que foi o que aconteceu por um bloco inteiro.

### O cluster mudou de estado sozinho — e duas mutações antigas pararam de morder

Com a terceira filha de `/materiais/` no ar, a F2 e a `/materiais/como-sabemos/`
passaram a ter **duas irmãs** e as três publicam "Veja também". Ninguém editou
nada: as irmãs são derivadas do mapa, e a regra da seção 6 do `ARVORE.md`
funcionou pela primeira vez no sentido inverso — antes ela **proibia** o bloco,
agora ela o **exige**.

O efeito colateral foi o achado do dia, e são dois casos diferentes:

- **"irmã escolhida fora da mãe" passou** porque o portão do cluster contava
  quantas irmãs saíam e se estavam no ar, **nunca de onde elas vinham**. A
  mutação morria por efeito colateral — estourava a contagem — e o efeito sumiu
  quando havia mais páginas no ar. **Trava frouxa de verdade**, e agora toda
  irmã listada tem a mãe recomputada do mapa. Trava que reprova por efeito
  colateral é trava que um dia para de reprovar.
- **"a página fora do sitemap perde a citação" passou** porque o cluster novo
  liga a camada de prova sozinho. Aqui a trava **não** afrouxou: ela mudou de
  dono. E o que mudou de dono ganhou trava própria — a citação **no texto**,
  medida com o cluster e a trilha fora da conta, porque o que se mede ali é
  escolha editorial, não geração automática.

### O que a página diz que não sabe

A linha de **gramas de cola** nasce vazia com o motivo escrito (o fabricante do
silicone declara rendimento por cordão, não por área, e o consumo por área da
cimentcola não foi obtido). A **pastilha não tem banco**: o cartão de compra tem
o lugar reservado dizendo que está vazio, em vez de sumir. E **sem o banco a
página continua respondendo área e pastilhas** e diz que não publica os gramas —
a bancada mede esse estado de propósito, porque página degradada é uma página
válida, com cabeçalho, rodapé e prosa, e foi assim que a Robometria mediu três
páginas pela metade sem ninguém acusar.

### Verificação

- `ferramentas/teste-f1.php`: **67 afirmações**, régua aritmética escrita fora do
  snippet, um processo por estado. Varre 24 combinações de forma × caquinho, 36
  de folga × tipo de rejunte, as cinco sobras, quatro espessuras, cinco lugares,
  e as bordas fabricadas: vão maior que a moldura, folga que nenhum fabricante
  cobre, caquinho irregular, banco ausente e **banco com outro coeficiente**.
- `ferramentas/mutacoes-f1.py`: **27 de 27 reprovadas.** Duas passaram na
  primeira rodada e as duas viraram afirmação nova — o CR digitado dentro do
  snippet **com o valor certo** (invisível para qualquer teste sobre a tela de
  hoje; só troca de banco o revela) e a vitrine ignorando o tipo escolhido
  (continua sendo subconjunto do que a F2 aprova, então a trava de subconjunto
  não a via).
- `teste-casca.php` de **367 para 409** com a página nova nos portões de voz,
  prova, trilha, árvore e página fina; `mutacoes-arvore.py` **20 de 20**;
  `teste-f2.php` 72 e `validar-banco.py` sem regressão; `php -l` limpo nos
  quatro snippets; os três JSON reparseados.
- Chromium em 360/390/781/782/783/1200 nas **14 páginas** — três delas estados
  da F1, incluindo o da medida que não fecha —, **88 medições, 0 px de rolagem**.
  **A medição foi feita com a casca 1.5.0**, antes do conserto da remontagem, e
  fica dito assim de propósito: o que a prova valer tem que ser o que foi
  medido. O que sustenta ela continuar valendo é uma segunda medida, não uma
  suposição — o HTML servido das 14 páginas é **byte a byte idêntico** entre a
  1.5.0 e a 1.6.0, porque a 1.6.0 só troca a chave que decide *quando* a
  estrutura é remontada e não imprime uma linha na tela (a constante de versão
  nem aparece no HTML). Uma terceira rodada do navegador foi tentada e morreu no
  túnel de rede, que estava derrubando as conexões de fonte.
- **No ar, às 00h05Z:** `conferir-no-ar.py` com **194 afirmações medidas no HTML
  servido, zero falha**. As 11 URLs em 200, as três tabelas pré-renderizadas
  servidas, JSON-LD `WebApplication` + `FAQPage`, canonical na âncora e
  `noindex` em todo estado com parâmetro, e **quatro contas conferidas contra o
  que foi calculado à mão** (vaso 942 cm²/720/264 g, tampo 2.827/588/594 g,
  esfera 1.257/960/352 g, moldura 900/188/189 g). O sitemap passou de 9 para
  **10 URLs**.
- **Defeito de etiqueta consertado de quebra:** o manifest dizia casca 1.4.0
  enquanto o arquivo definia 1.5.0. O sha estava certo — o Sync aplicou os bytes
  certos e o site nunca esteve errado —, envelheceu a **etiqueta**, que é por
  onde qualquer relatório lê o que está no ar. Nenhum portão lia essa metade;
  agora `atualizar-manifest.py` compara a versão do manifest com a constante do
  snippet e **recusa gravar** quando os dois se separam. Foi ele que acusou a
  1.6.0 antes deste commit.

### Números da ilha, contados

**10 dos 10 itens do banco esperam link de afiliado; 10 estão sem imagem** —
este bloco não tocou catálogo, e nenhum dos dez tem loja possível hoje. Da pauta
da seção 17: **nenhum tema escrito, nenhum na fila, nenhum recusado** —
`pauta.md` ainda não existe nesta pasta.

**Próximo passo:** as **fichas de categoria de material** (bloco 4c). A 16.5
continua valendo — categoria só nasce com três filhas de dado real —, e hoje
Colas e Rejuntes têm banco de cinco itens cada e **uma** filha cada (as duas
ferramentas). O caminho mais curto para destravar `/materiais/colas-e-adesivos/`
e `/materiais/rejuntes/` é a leva de fichas de produto, que são nível 3 com dado
real: cinco colas e cinco rejuntes já cadastrados, cada ficha com a declaração
do fabricante, a faixa, a fonte e o cartão de compra. A ilha está **abaixo do
piso** da seção 21 (10 URLs, 21 dias não passaram), então a leva sai no ritmo
normal, de 5 a 10 URLs, sem esperar medição.

12/09/2026 15h55Z — DESPACHO DA SENTINELA DE 12/09 CUMPRIDO INTEIRO (itens 1 e 2)

- **Os dois itens eram o mesmo defeito com duas roupas**, e foi por isso que o
  conserto virou UMA regra em vez de dois remendos: a página falava de menos
  produtos do que listava, ou nomeava a causa errada por quem ficou de fora. A
  regra subiu para o `ARQUIPELAGO.md` seção 7, porque vale para toda ilha:
  **todo item do banco é nomeado exatamente uma vez em cada resposta** — na
  frase que o recomenda, e aí ele está na vitrine, ou numa linha que diz por que
  ele não está — e **o bloco de compra serve exatamente o que a frase nomeia**.
  Junto com ela foi a metade complementar: **a recusa nomeia a causa que a
  página mediu, nunca oferece hipótese**, e **afirmação em bloco tem o escopo
  do que foi medido**.

- **ITEM 2 (F2, `clubedomosaico-f2.php` 1.0.0 → 1.1.0).** A frase dizia "o
  rejunte é Rejunte Acrílico Quartzolit", singular e definitiva, e a vitrine
  logo abaixo servia QUATRO cartões. Agora a frase tem duas linhas — a
  recomendação e os que também servem, com o que os separa escrito (o fabricante
  não nomeia o lugar; a régua do rejunte só transforma silêncio em exclusão nos
  ambientes críticos) — e a vitrine serve exatamente esses. Os que ficaram de
  fora ganharam uma linha cada: fora pela folga (com a faixa publicada), fora
  pelo lugar, fonte de imprensa e **faixa não obtida**.
  **Dois achados dentro do item**, e nenhum dos dois estava no despacho:
  (a) o grupo `mencionados_com_ressalva` não era impresso em lugar nenhum —
  vazio com o banco de hoje, invisível para sempre no dia em que enchesse;
  (b) "faixa não obtida" estava sendo contada como "a folga não cabe", que é
  afirmar sobre uma declaração que ninguém leu — o rejunte piscinas não publica
  faixa, e a página dizia que ele não cobria 2 mm. Esse mesmo defeito tinha
  tornado INALCANÇÁVEL um ramo da frase de recusa que eu mesma acabara de
  escrever ("só o lugar exclui"): com o piscinas eternamente no balde da folga,
  aquele caso nunca acontece. Ramo morto saiu; quem diz a causa são as linhas.

- **ITEM 1 (F1, `clubedomosaico-f1.php` 1.0.0 → 1.1.0).** A recusa culpava
  SEMPRE a folga, inclusive quando a folga cabia e quem excluía era o lugar — e
  com a linha de "outro tipo" logo abaixo dizendo "dentro dessa folga", a página
  negava e afirmava o mesmo fato em duas frases seguidas. Agora são três causas
  com nome próprio, produtos nomeados e a faixa que o fabricante publica; e
  quando a causa é o lugar a página diz "é o LUGAR, não a folga", o que não é
  suposição: quem cai pelo lugar passou pela trava da folga antes.
  **A outra metade do defeito não estava no despacho e só a tela mostrava:**
  `strtok( $rotulo, ' —' )` cortava no primeiro espaço e devolvia só "Rejunte",
  então a frase afirmava sobre o banco INTEIRO ("Nenhum rejunte do nosso
  banco…") o que valia no máximo para o tipo escolhido.

- **O PORTÃO ACHOU UM BURACO NO PRÓPRIO CONSERTO, antes do desembarque.** A
  primeira versão da F1 só prestava contas quando a lista voltava vazia: em 27
  estados ela listava dois cimentícios e não dizia uma palavra sobre o terceiro.
  É o item 2 um andar acima — produto do banco que some da tela sem que nada
  diga por quê. A prestação de contas passou a sair sempre.

- **PORTÃO NOVO: `ferramentas/teste-prestacao-rejunte.php`.** Régua própria,
  recomputada aqui a partir dos `perfis_esperados_do_rejunte` escritos à mão e
  das regras 1 a 4 do esquema — nada nele chama `cdm_f2_celula_rejunte()`,
  `cdm_f2_avaliar_rejunte()` nem `cdm_f2_perfil_rejunte()`. Varre **540 estados
  da F2** (9 bases × 5 lugares × 12 folgas), **180 da F1** (3 tipos × 5 lugares
  × 12 folgas) e as **9 linhas da tabela pré-renderizada**, um processo por
  estado, com as folgas indo de 1 a 12 para pisar nas bordas (1 e 11 estão fora
  de todo extremo declarado; 2, 4, 5 e 10 são extremos exatos). 5 afirmações, 0
  falha.

- **`ferramentas/mutacoes-prestacao.py`: 11 mutações, 11 reprovadas.** As duas
  primeiras são os dois defeitos do despacho escritos de volta. **Quatro delas
  não morderam na primeira rodada, e as quatro ensinaram coisa diferente:**
  (1) a que condicionava a linha de `fora_lugar` mirava um estado que o banco de
  hoje não produz — os dois cimentícios têm faixa e declarações iguais, então ou
  os dois servem ou os dois caem; o estado que existe é o de `sem_faixa`;
  (2) a do grupo de ressalva não mudava um byte enquanto o banco não tivesse
  fonte fraca, e precisou **produzir o mundo** nas DUAS metades (o nível nas
  `fontes` do banco, que o snippet lê, e o nível no perfil escrito à mão, que a
  régua lê) — rebaixar só uma faria o teste reprovar pelo motivo errado;
  (3) a da tabela mirava o grupo de ressalva, vazio, e teve de mirar o de faixa
  não obtida, que está fora em todas as nove linhas;
  (4) a da promoção silenciosa **passou por erro de alvo**: a linha do score é
  idêntica byte a byte em `cdm_f2_avaliar_cola()` e em `cdm_f2_avaliar_rejunte()`,
  e a substituição pegou a primeira — mutou a cola, que este portão não mede, e
  o verde foi honesto. O alvo agora carrega a linha anterior, que é a única
  diferença entre as duas funções naquele ponto.

- **DOIS DEFEITOS MECÂNICOS CONSERTADOS NA MESMA PASSADA (seção 19).** O
  manifest declara `sha256` no grupo `ferramentas` desde que nasceu e **nenhuma
  linha o recalculava**: `render-para-teste` e `teste-casca` estavam com a
  etiqueta de uma versão que não existe mais, de blocos anteriores. E a lista
  conhecia **9 das 18 ferramentas** do disco — entre as ausentes, `teste-f1.php`
  e `teste-f2.php`, que são os dois portões principais da ilha. Bancada não vai
  para o site, então nada disso quebraria uma página; quebrava a capacidade de
  qualquer relatório dizer com o que esta ilha se verifica.
  `atualizar-manifest.py` passou a espelhar o grupo e a cobrar as duas direções
  (ferramenta no disco fora do manifest agora reprova). 16 sha recalculados.

- **VERIFICAÇÃO.** `php -l` limpo nos três snippets; `teste-prestacao-rejunte`
  5 afirmações 0 falha em 729 estados; `teste-f1` 67; `teste-f2` 72;
  `teste-casca` 409; `validar-banco` sem regressão; mutações antigas intactas
  (f1 27/27, f2 20/20, rejunte 12/12, árvore 20/20 — nenhuma virou inerte);
  Chromium em 360/390/781/782/783/1200 nas **16 páginas** renderizadas (as 11 da
  casca mais os 5 estados de ferramenta que este bloco mudou), **98 medições, 0
  px de rolagem lateral**.
  **UMA AFIRMAÇÃO ANTIGA FOI REESCRITA, e isso é parte da entrega:** o
  `teste-f1.php` cobrava a string `'do nosso banco declara folga'` para os 11 e
  12 mm — que é a frase DO DEFEITO. Afirmação que fixa o texto de hoje vira
  trava contra o conserto de amanhã; ela passou a cobrar a intenção (a página
  diz que nenhum serve E diz que a causa é a folga).

- **NO AR às 15h51Z: revisão 12 no `/status`, igual à do manifest, 6 aplicados,
  UM disparo** — sem o atraso de CDN dos blocos anteriores. `conferir-no-ar.py`
  mediu **231 afirmações no HTML servido, 0 falha**, e ele ganhou as afirmações
  do despacho escritas nas palavras do próprio despacho: as 6 combinações do
  item 1 (externo_exposto e contato_permanente_agua × 2, 4 e 10 mm) sem a frase
  antiga, dizendo que a exclusão é do lugar e nomeando o lugar; os 5 rejuntes do
  banco contados um a um em 3 respostas do item 2; e as 9 linhas da tabela
  somando 5.

- **Receita:** 10 dos 10 itens do banco continuam esperando link de afiliado e
  10 seguem sem imagem; este bloco não tocou catálogo, e nenhum dos dez tem loja
  possível hoje. Pauta da seção 17: `pauta.md` ainda não existe — 0 escritos, 0
  na fila, 0 recusados.

- **PRÓXIMO PASSO:** o bloco **4c**, fichas de categoria de material
  (`/materiais/pastilhas/`, `/alicates/`, `/colas/`, `/rejuntes/`, `/bases/`,
  `/acabamento/`). A regra nova da seção 7 nasce com ele em vez de ser
  descoberta depois: ficha de categoria é, por definição, uma página que fala de
  TODOS os itens de uma categoria do banco, então a prestação de contas dela é a
  própria página — e o portão desta execução já sabe medir isso. A ilha está
  ABAIXO DO PISO da seção 21 (11 URLs, 21 dias não passaram), então a leva sai
  no ritmo normal, de 5 a 10 URLs, sem esperar medição.

---

## 12/09/2026 17h37Z — A TAG DO GA4 NO AR: a ilha começa a ser medida

**Despacho ALTA de 12/09/2026 para a FUNDAÇÃO** (`dados/despachos.md`), na parte
desta ilha. Casca **1.7.0**, manifest na **revisão 13**, `/status` com revisão 13
às 17h37Z, em **UM disparo**.

- **O MARCO ZERO DESTA ILHA É 12/09/2026 17h37Z.** Antes disso não existe dado de
  audiência, e isso é a metade que faltava para a seção 5 ser executável: a ilha
  nasceu em 10/09 e serviu nove, depois onze URLs **sem tag nenhuma**. Qualquer
  leitura feita até hoje devolveria zero, e aquele zero media **a ausência da
  tag** — nunca a ausência de visita. A seção 5 manda o relatório dizer qual dos
  dois é; até hoje a resposta desta ilha era sempre o primeiro.

- **A prioridade 8 no `wp_head` não é gosto, é o único número que cabe.** O
  despacho pede a tag o mais cedo possível **e** proíbe que ela passe na frente
  do `<title>`, da meta descrição e do JSON-LD. As duas metades juntas dão
  exatamente 8: depois do robots (4), do ícone (5), do `Organization` (6) e da
  trilha (7), e **antes da folha de fontes (20)**, que é o único recurso
  bloqueante desta casca. O `async` faz o resto — o LCP desta ilha é texto.

- **O ID é constante no topo e é conferido antes de ser impresso.** ID de medição
  digitado no meio do código é ID que alguém copia junto com a casca para a ilha
  4 e só descobre trocado quando o relatório do mês vier somando duas ilhas.
  `cdm_casca_ga4_html()` só devolve markup se o ID casar com `G-` + maiúsculas e
  dígitos: meia tag no ar não mede nada **e** ainda faz o console falar.

- **A página de Privacidade mudou na mesma versão, e isso não foi zelo.** Ela
  prometia, com todas as letras, que "se um dia houver medição de audiência, esta
  página será atualizada *antes* de ela ser ligada, com a data da mudança".
  Ligar a medição e deixar a promessa de pé seria publicar uma frase falsa na
  página que existe justamente para não ter nenhuma. Sem banner de consentimento
  (22.4).

- **ACHADO QUE NÃO É DESTE BLOCO, E É PARA O RAPHAEL: o Site Kit by Google
  1.187.0 está instalado e ativo nesta ilha e não mede nada.** Medido no HTML
  servido **antes** de mudar qualquer coisa: zero ocorrência de `gtag(` e zero do
  ID da ilha; o que ele deixa na página é uma meta `generator` e um
  `dns-prefetch`. Plugin desconectado ocupando uma linha de `<head>`. O risco não
  é hoje: no dia em que alguém o conectar pelo wp-admin, a propriedade ganha um
  **segundo dono de tag** e toda sessão passa a ser contada duas vezes **sem uma
  coisa mudar na tela**. Quem acusa isso é uma afirmação nova do
  `conferir-no-ar.py`, que conta os inicializadores de `gtag` no HTML servido.

- **DEFEITO MECÂNICO CONSERTADO NA MESMA PASSADA (seção 19), e ele mordeu esta
  execução.** `atualizar-manifest.py` parava no **primeiro** achado, e o `return`
  do descasamento de versão escondeu a conferência de ferramenta órfã: o
  `mutacoes-ga4.py` recém-escrito ficou fora do manifest **sem uma linha de
  aviso**, numa execução em que a versão do snippet acabara de subir — que é
  exatamente quando ferramenta nova nasce. O portão existia, estava certo e era
  **inalcançável**: a conferência que roda primeiro escondia a que interessava.
  As quatro conferências agora acumulam e a lista sai inteira.

- **VERIFICAÇÃO.** `teste-casca.php` de **409 para 539 afirmações**, 0 falha, com
  a **ordem** medida e não só a presença — portão que só pergunta "existe gtag na
  página?" fica verde com a tag no lugar errado, que é o único jeito de esta
  mudança fazer mal. `mutacoes-ga4.py` novo: **14 de 14 reprovadas**, em três
  famílias (a tag some ou sai pela metade; a tag fica e está errada — ID de outra
  ilha, ID digitado ao lado da constante, `config` discordando do `src`, tag
  dobrada, que é o caso Site Kit; e a tag certa no lugar errado — sem `async`,
  antes do JSON-LD, depois das fontes). **Uma mutação reprovou pelo portão errado
  na primeira rodada e foi reescrita:** ela trocava a frase nova da privacidade
  *pela* velha, então morria na trava da frase nova e deixava sem medida a trava
  que interessa — a que mede a **ausência** da promessa antiga. Agora ela
  acrescenta o parágrafo velho sem tirar o novo, que é como isso acontece de
  verdade. Regressões sem uma falha: f1 67, f2 72, prestação 5 em 729 estados,
  `validar-banco`, e as mutações antigas (f1 27/27, f2 20/20, rejunte 12/12,
  árvore 20/20, voz 24/24, prestação 11/11) — nenhuma virou inerte. `php -l` limpo.

- **NO AR às 17h37Z:** `conferir-no-ar.py` de **231 para 334 afirmações** no HTML
  **servido**, 0 falha. As onze URLs com a tag uma vez só dentro do `<head>`, o
  ID desta ilha, o `async`, o `config` batendo com o `src`, a ordem conferida no
  que o **servidor** serve, o `gtag` como **único** script de terceiro, **um**
  inicializador e não dois, e a página de Privacidade com a frase nova, a data, e
  a promessa antiga **medida como ausente**.

- **O TERCEIRO CRITÉRIO DO DESPACHO FICOU ABERTO, e não por falta de tentativa.**
  O Tempo Real do GA4 não foi confirmado. Duas causas independentes, as duas
  medidas e **repetidas na mesma execução**, como a seção 20.2 exige:
  1. **Sem credencial.** `ferramentas/ga4.py` pede `GOOGLE_SA_B64`,
     `GOOGLE_SA_JSON` ou `GOOGLE_SA_FILE`, e o ambiente desta rotina não tem
     nenhuma das três (zero variável `GOOGLE*`). A conta de serviço já é Leitor
     na conta `Arquipélago`: falta a **variável**, não a permissão.
  2. **`www.googletagmanager.com` está fora da lista de egresso.** 403 ao
     CONNECT, cinco vezes, com `clubedomosaico.com.br` em 200 na mesma passada —
     é **política**, e não a intermitência de túnel da seção 20.2, e a regra é
     nomear o host barrado em vez de insistir. A consequência é maior que o item:
     **nenhuma verificação de tag por navegador a partir da nuvem pode funcionar**
     enquanto esse host estiver barrado, porque o navegador não baixaria o
     `gtag.js`. De quebra, o Chromium não atravessa este túnel nem para o domínio
     liberado (`ERR_CONNECTION_RESET` em 3 tentativas, `ws_closed_mid_exchange` no
     proxy, `curl` em 200 no mesmo minuto).

- **Nasceu mesmo assim `ferramentas/conferir-tag-no-navegador.mjs`**, que abre a
  ilha num navegador e mede o **disparo saindo** (o `tid`, o código que o Google
  devolve, **um** `page_view`, o console limpo). O `conferir-no-ar.py` usa `curl`
  e `curl` não executa uma linha de JavaScript: ele prova que a tag **está** na
  página e nunca que a visita **chega** na propriedade. O arquivo diz no próprio
  cabeçalho que **nunca foi visto aprovando**, porque ferramenta que ninguém viu
  rodar é promessa.

- **O que fecha o item é configuração, não código:** `www.googletagmanager.com` e
  `*.google-analytics.com` na rede Personalizada do ambiente das rotinas, junto
  com os domínios das ilhas que já estão lá, e a credencial da conta de serviço
  na variável de ambiente. Até lá, quem confirma o Tempo Real é o Raphael, no
  Chrome dele. **E o que NÃO se fez, escrito para ninguém ter a ideia:** mandar
  um evento pelo Measurement Protocol para "confirmar" a medição seria inventar a
  visita que se queria comprovar e sujar a série com uma sessão que nunca
  existiu. Zero medido é dado; zero fabricado é mentira.

- **`dados/audiencia.md` nasceu** com o marco zero e com esta não-medição escrita
  como linha da série — que é o que a seção 5 manda quando não se conseguiu medir.

- **Receita:** 10 dos 10 itens do banco seguem esperando link de afiliado e 10
  sem imagem; este bloco não tocou catálogo. Pauta da seção 17: `pauta.md` ainda
  não existe — 0 escritos, 0 na fila, 0 recusados.

- **PRÓXIMO PASSO:** o bloco **4c**, fichas de categoria de material, que já era
  o próximo antes deste despacho furar a fila e continua sendo. A ilha está
  ABAIXO DO PISO da seção 21 (11 URLs), então a leva sai no ritmo normal, de 5 a
  10 URLs, sem esperar medição — e agora, pela primeira vez, com a série de
  audiência correndo por baixo dela.

12/09/2026 19:21Z — A VARREDURA DA SEÇÃO 14.3: o 4c não estava esperando ser escrito, estava esperando banco — e agora isso é um número

- **O bloco começou como 4c e virou a medição que o 4c pedia.** O `ESTADO.md`
  vinha dizendo, execução após execução, que o próximo passo eram as **seis
  fichas de categoria de material** (`/materiais/pastilhas`, `/alicates`,
  `/colas`, `/rejuntes`, `/bases`, `/acabamento`). O `ARVORE.md` já dizia, desde
  11/09, que nenhuma delas podia nascer pela **16.5** — categoria só nasce com 3
  filhas de dado real, e Colas e Rejuntes têm **uma** cada. As duas frases
  conviviam porque nenhuma era falsa. O que faltava era o segundo portão, que
  ninguém tinha medido: **a seção 14.3**, que proíbe faixa de ferramenta sair com
  menos de 3 produtos elegíveis. Sem esse número, a próxima execução escolheria
  entre escrever seis páginas magras e adiar de novo, sem critério.

- **O QUE A VARREDURA MEDIU, de ponta a ponta e pela primeira vez.** Dos **45**
  estados de cola que a F2 serve, **ZERO** chegam aos 3 elegíveis que a 14.3
  exige; o teto é **2** e **13** não servem nenhum produto. Dos **60** estados de
  rejunte, **12** chegam, **48** não, e **25** não servem nenhum. E **5 das 7
  categorias do vocabulário não têm um único item no banco**: `pastilha`,
  `alicate`, `base`, `acabamento`, `apoio`. A consequência é mais dura do que a
  16.5 sozinha: com o banco de hoje **nem as filhas de nível 3 de cola podem
  nascer**, porque nenhum recorte da categoria reúne os 3 itens que o portão de
  dado da seção 9 cobra. Não é falta de texto — é falta de produto.

- **TRÊS FONTES, E NENHUM NÚMERO DIGITADO.** (1) A **faixa** vem de
  `ferramentas/faixa-da-f2.php`, que a mede **provocando o próprio snippet**: põe
  cada valor de um superconjunto deliberadamente maior em `$_GET`, chama
  `cdm_f2_entrada()` — a mesma função que saneia a consulta de quem visita — e
  fica com o que sobreviveu. Faixa digitada mediria a faixa que alguém lembrou e
  ficaria verde no dia em que o campo da junta mudasse de teto. O medidor
  **recusa medir** quando o superconjunto não passa por cima nem por baixo da
  faixa (teto medido igual ao teto da régua não é teto, é o fim da régua) e
  quando o saneamento aceita um valor inventado. (2) A **régua** é a de
  `validar-banco.py`, importada: ela recompõe a elegibilidade das **declarações**
  pelas regras do esquema e foi escrita no bloco 3 **antes** de existir uma linha
  do snippet PHP. Reimplementá-la aqui uma terceira vez não acrescentaria
  independência nenhuma — acrescentaria uma cópia para envelhecer calada. (3) O
  que o **site serve** é conferido por `ferramentas/conferir-cobertura.php`, que
  anda os mesmos estados chamando o snippet, **um processo por estado**.

- **O CRUZAMENTO PASSOU DE 27 PARA 105 ESTADOS, e esse é o ganho estrutural do
  bloco.** A régua Python e a régua PHP são duas implementações da mesma regra, e
  até hoje elas só se encontravam nas **27** células escritas à mão do esquema —
  18 de cola e 9 de rejunte — de **105** que as ferramentas servem. Os outros
  **78** nunca tinham sido comparados com nada: se as duas metades divergissem
  ali, o censo diria um número e a página serviria outro, e nenhum portão veria.
  Hoje as duas concordam nos 105. `conferir-cobertura.php`: **128 afirmações, 0
  falha**.

- **MUTAÇÕES: 14 escritas, 14 reprovadas, e 9 delas NENHUM portão antigo pegou.**
  O script roda, para cada mutação, também `validar-banco.py` e `teste-f2.php`, e
  marca as que só a varredura viu — mutação que qualquer portão antigo pega já
  estava coberta e não justificaria arquivo novo. A que melhor mostra o buraco:
  **a faixa de junta afrouxa só em 7, 8 e 9 mm**. A grade escrita à mão do
  esquema pisa em 1, 2, 3, 4, 5, 6, 10 e 11 mm, escolhidos para encostar nas
  bordas declaradas — é uma grade boa, e é exatamente por isso que 7, 8 e 9 caem
  num vão onde nenhum extremo mora. Com esse afrouxamento o site passa a
  recomendar rejunte que o fabricante não cobre, e os 27 cruzamentos antigos
  continuam verdes.

- **DUAS MUTAÇÕES FORAM REESCRITAS DEPOIS DE PASSAR, e as duas ensinaram algo.**
  (a) A que derrubava a **regra 3 do rejunte** (quem delimita ambiente fica
  fechado nele) passou — e não por buraco no portão: **com o banco de hoje essa
  regra é código morto.** Das cinco fichas, só o acrílico declara ambiente
  (`áreas internas e externas`), e nos estados em que a regra 3 o cortaria a
  regra 2 já o tinha cortado antes, porque `contato_permanente_agua` é crítico e
  as resistências dele param em `áreas molhadas`. A regra **fica no snippet** — é
  ela que vai decidir no dia em que entrar um rejunte que delimite ambiente — mas
  a mutação saiu, porque mutação inerte é teste verde com outro nome. (b) A do
  **gerador contando errado** reprovava pelo portão errado: ela mutava
  `cobertura.py` sem regenerar o JSON, então caía em "arquivo velho" em vez de na
  recontagem. O caso real é alguém mexer no gerador, rodar e commitar as duas
  coisas juntas — aí a regeneração bate consigo mesma e só a recontagem do lado
  PHP vê. Reescrita assim, ela passou a cair em `cola: "com o mínimo" bate com a
  contagem`, que é o portão que ela existe para medir.

- **REDE, reconferida como a seção 20.2 manda.** Os domínios de fabricante estão
  **fora da lista de egresso**: `colormix.com.br`, `vidrotil.com.br` e
  `quartzolit.weber` responderam `000` por `curl` em **duas passadas da mesma
  execução**, com `clubedomosaico.com.br` em **200** nas duas. É política, não a
  intermitência de túnel. **Mas isso NÃO bloqueia a coleta de banco:** o canal de
  busca alcança os mesmos fabricantes, foi assim que o bloco 3c colheu os cinco
  rejuntes, e foi reconfirmado nesta execução. Escrever "coleta bloqueada por
  rede" aqui seria repetir o diagnóstico que custou dois dias a esta ilha em
  11/09.

- **NADA FOI AO AR, e isso é desenho, não pendência.** Nenhum arquivo publicável
  mudou: os três snippets estão byte a byte como estavam, nenhuma URL nasceu e
  nenhuma mudou. `dados/cobertura.json` entra com `publicar: false` — o site não
  precisa dele, e publicá-lo criaria uma segunda fonte do mesmo número dentro do
  site. Portanto **não houve Sync nesta execução**, pela mesma leitura da seção 4
  que valeu no bloco 1. Manifest na **revisão 14**, com as quatro ferramentas
  novas e o censo inventariados — o portão de ferramenta órfã de
  `atualizar-manifest.py` acusou as quatro antes de qualquer commit, que é para
  isso que ele foi consertado ontem.

- **REGRESSÃO SEM UMA FALHA:** `php -l` em todos os snippets e ferramentas,
  `validar-banco` (10 materiais, 18 + 9 células recomputadas), `teste-casca`
  (539), `teste-f1` (67, 24 estados um processo cada), `teste-f2` (72),
  `teste-prestacao-rejunte` (5 afirmações sobre 540 estados da F2 e 180 da F1).
  O `teste-casca` importa em especial porque ele **lê o `ARVORE.md`** para cobrar
  que documento e código digam a mesma coisa, e este bloco escreveu uma seção
  nova lá. As sete baterias de mutação antigas foram rodadas inteiras para provar
  que **nenhuma virou inerte**: árvore 20/20, F1 27/27, F2 20/20, GA4 14/14,
  prestação 11/11, rejunte 12/12, voz e cabeça 24/24 — **128 mutações, 128
  reprovadas**.

- **Receita:** 10 dos 10 itens do banco seguem esperando link de afiliado e 10
  sem imagem; este bloco não tocou catálogo. Pauta da seção 17: `pauta.md` ainda
  não existe — 0 escritos, 0 na fila, 0 recusados.

- **PRÓXIMO PASSO, e agora ele tem ordem e motivo.** **Banco antes de página.** A
  categoria `pastilha` é a primeira, e não por gosto: a F1 responde "quantas
  pastilhas comprar" e a ilha não tem **uma** pastilha no banco, então a
  ferramenta de maior intenção de compra da ilha calcula uma quantidade e não tem
  o que vender — é a faixa descoberta mais cara da seção 14.3 e o buraco que
  nenhuma coleta de cola ou de rejunte fecha. Depois dela, cola, onde o teto de 2
  elegíveis por estado diz que faltam produtos. **Só então** as filhas de nível 3
  por cluster (16.6), e **só então** a mãe de nível 2, que é o 4c. A coleta vai
  pelo canal de busca, com as travas da seção 8: nunca pôr na consulta o valor
  que se quer confirmar, e fonte que não cita o documento é paráfrase.

12/09/2026 21:19Z — BLOCO 3d ENTREGUE: a categoria PASTILHA nasce no banco, e com ela o número que os fabricantes não publicam

- **Por que este bloco e não o 4c.** O `ESTADO.md` da execução anterior deixou a
  ordem escrita e o motivo junto: **banco antes de página**, e `pastilha` é a
  primeira das cinco categorias que a varredura da seção 14.3 achou com ZERO
  itens — a F1 responde "quantas pastilhas comprar" e a ilha não tinha **uma**
  pastilha para vender. Nenhuma URL nasceu ou mudou.

- **O QUE ENTROU:** `dados/materiais-pastilhas.json`, 10 SKUs de dois lugares
  distintos da escada de fontes. Nove da **Glass Mosaic** (fabricante, nível 3):
  linha Cristal 2,5 cm (K2501, K2502, MIX2510) e 3 cm (K117, K77, K66), linha
  Fosca 2 cm (A11, A61) e linha Strip 1,2 cm (ST5102). Um da **Pastilhart**
  (AF1500, 1,5 cm) — e ele entra em **nível 5**, não 3, porque a empresa se
  declara "importadora e distribuidora" na própria página institucional. É o
  único item do arquivo que declara ambiente, inclusive piscina, justamente o
  campo que mais pesaria numa recomendação: ter o dado e **não poder recomendar
  com ele** é o resultado certo da escada, não um defeito da coleta.

- **A COLETA, e as travas da seção 8.** Busca restrita ao domínio, como nos
  blocos 2, 3 e 3c. `curl` e `WebFetch` para glassmosaic.com.br,
  pastilhart.com.br, vidrotil.com.br, colormix.com.br e jatoba.ind.br devolveram
  `000`/`EGRESS_BLOCKED` em **duas passadas** da mesma execução, com
  clubedomosaico.com.br em **200 nas duas** — é política de egresso e não a
  intermitência de túnel que custou dois dias a esta ilha em 11/09 (seção 20.2).
  **Nenhuma consulta plantou o valor que se queria confirmar:** as buscas
  pediram os RÓTULOS da ficha ("tamanho, espessura, tamanho placa, placas caixa,
  peso caixa"), nunca um número.

- **TRÊS CAMPOS NASCEM NULL, E É O QUE ESTE ARQUIVO TEM DE MAIS ÚTIL.**
  - **Peças por placa — nenhum fabricante declara**, e é exatamente o número de
    que a F1 precisa para converter placa em peça. A SERP inteira preenche o
    buraco dividindo o lado da placa pelo lado da pastilha. **A divisão não
    fecha:** 29,2 / 3,0 = 9,73 e 32,3 / 2,0 = 16,15 não são inteiros — em 6 dos
    10 itens. E onde ela fecha, fecha errado por outro motivo: 30,0 / 2,5 = 12
    exige **junta zero** na placa telada, e placa sem junta é placa que não se
    rejunta. As duas leituras possíveis do número anunciado — lado da PEÇA e
    passo do MÓDULO — não podem valer ao mesmo tempo no catálogo de um mesmo
    fabricante. Então `pastilhas_por_placa` e `passo_de_fabrica_cm` ficam null,
    com o motivo escrito, e a régua **reprova** quem os preencher.
  - **Peso unitário — e aqui o próprio catálogo se entrega.** Dividindo peso da
    caixa pela metragem sai um kg/m², que se compara com o teto físico do vidro
    maciço (espessura × densidade). A linha Cristal de 4 mm dá 8,9 e 9,4 kg/m²
    contra teto de 10,0: cabe, e a folga é a junta. A linha Strip de 6 mm dá
    **16,9 contra teto de 15,0 — passa do teto**, o que só pode ser embalagem,
    tela e papel contados junto. Portanto **peso de caixa não vira peso de
    produto em tela nenhuma**, e o item fica no banco com `divergencias` e
    `resolucao` escritas em vez de ser descartado: descartar o caso que não
    fecha é apagar a prova.

- **O DEFEITO QUE ESTE BLOCO ENCONTROU NA PRÓPRIA RÉGUA, e que só podia aparecer
  agora.** O `validar-banco.py` checava o passo de fábrica com
  `lado_anunciado_cm / raiz(N)` — o lado da **pastilha** no lugar do lado da
  **placa**. Com o exemplo do próprio `especificacao-calculadoras.md` (placa
  30×30 com 225 pastilhas → passo 2,00 cm) a conta certa é 30/raiz(225); a que
  estava escrita dava 1/15 = 0,07 cm. **Nunca disparou porque a categoria
  pastilha tinha zero itens** — função de portão que nunca rodou é função morta,
  a mesma família que a Robometria nomeou em 11/09. Consertado, e a geometria do
  `esquema-banco.json` ganhou os campos que a fórmula precisava
  (`placa_lado_a_cm`, `placa_lado_b_cm`, `formato`), mais a recusa de aplicar
  L/raiz(N) em placa que não é quadrada — o caso da linha Strip, 28,6 × 31,2.

- **A CASCA 1.8.0, e por que o banco foi publicado nesta passada.** Option que
  nenhuma página lê é caminho morto, e caminho morto envelhece calado. Então
  `materiais-pastilhas` entra em `cdm_casca_numeros()` junto de colas e rejuntes
  **na mesma revisão**: o cartão "Pastilhas e tesselas" do Guia deixa de servir
  um zero digitado, a tabela do "Como sabemos" ganha a linha e a frase passa a
  nomear as **três** categorias — item que a soma conta e a frase não nomeia é a
  prestação de contas pela metade que o despacho da Sentinela de 12/09 fechou nas
  ferramentas. **Nenhuma URL nova:** `/materiais/pastilhas/` continua sem página
  (16.5 pede 3 filhas de nível 3), e o cartão só vira link quando a página
  existir — quem decide isso é `cdm_casca_url_se_existir()`, não a lista.

- **VERIFICAÇÃO.** `ferramentas/validar-pastilhas.py`, **139 afirmações, 0
  falha**, um processo por item, com a régua escrita à mão no próprio arquivo e
  nunca lida do banco que ela mede. Ela fez duas descobertas que a leitura não
  faria: (a) **o catálogo não tem uma regra única de arredondamento** — a caixa
  da Fosca cobre 2,086583 m² e sai "2,086" num SKU (corte) e "2,09" no irmão
  (arredondamento); uma régua que exigisse uma das duas reprovaria metade da
  linha sem haver erro de dado, e uma que aceitasse tolerância frouxa não mediria
  nada, então ela aceita **exatamente** as duas operações e **diz qual foi usada
  em cada item**; (b) a aritmética das fichas fecha na terceira casa em todos os
  10, o que é o que sustenta que os três números de cada ficha são do mesmo
  produto. `ferramentas/mutacoes-pastilhas.py`: **12 escritas, 12 reprovadas**, e
  **6 delas nenhum portão antigo viu** — entre elas a mutação que "produz o
  mundo", promovendo o distribuidor a fabricante, que sem tocar em mais nada faz
  1,5 cm passar de zero para um elegível.

- **A COBERTURA POR TAMANHO, que é o eixo pelo qual a F1 escolhe pastilha**, e é
  o número que este bloco deixa para o próximo: dos quatro tamanhos que a
  ferramenta oferece, só **um** chega aos 3 elegíveis da seção 14.3 — 2,5×2,5 com
  3; 2×2 com 2; **1×1 com ZERO** e irregular com zero. E 1×1 é o tamanho de **7
  das 12 linhas** da tabela pré-renderizada da F1: ele não aparece em catálogo de
  fabricante nenhum, só em armarinho e marketplace, vendido **a peso** ("100
  gramas") ou por contagem solta — nível 6, que sustenta preço e nada mais. É a
  mesma pendência da conversão grama↔peça vista pelo outro lado.

- **Receita:** 20 dos 20 itens do banco esperam link de afiliado e 20 estão sem
  imagem (eram 10 e 10; os 10 novos entram todos assim, e nenhuma foto foi
  colhida porque o egresso não alcança os domínios). Pauta da seção 17:
  `pauta.md` ainda não existe — 0 escritos, 0 na fila, 0 recusados.

- **NO AR, 21h58Z, em UM disparo do Sync:** `/status` na revisão 15, igual à do
  manifest; 7 itens aplicados. `ferramentas/conferir-no-ar.py` passou de 334 para
  **339 afirmações, 0 falha**, porque ganhou a seção que este bloco tornou
  necessária: **a prestação de contas do banco medida no HTML servido.** A frase
  do Guia publica um total e a repartição dele, e agora tem TRÊS parcelas em vez
  de duas — no ar ela diz "20 itens de fabricante, sendo 5 colas, 5 rejuntes e 10
  pastilhas, e 20 deles ainda esperam link". A régua não lê a frase do snippet:
  lê os **arquivos de banco do repositório**, um a um, e cobra quatro coisas
  distintas — o total servido bate com a soma dos arquivos; as parcelas somam o
  total que **a própria frase** publica (defeito diferente do primeiro: uma frase
  pode estar internamente certa e desatualizada, e foi o outro caso que pôs no ar
  "hoje 10 dos 5 itens"); **toda categoria com arquivo de banco é nomeada** na
  frase, que é o que impede a próxima categoria de entrar na soma e ficar fora do
  texto; e o número de itens esperando link bate com os cabeçalhos. Testada por
  negação antes de ser dada por boa: com o banco adulterado para 9 pastilhas, as
  três afirmações que deviam cair caíram.

12/09/2026 23:20Z — BLOCO 4d, O CORTE DO DESPACHO: A ILHA TEM UM ATELIÊ

- **Por que este bloco e não a ordem de banco que o estado anterior deixou.** O
  despacho do Raphael de 12/09, 18h20 BRT, tem prioridade MÁXIMA e prazo, e o prazo
  é amanhã: ele vai à casa dos pais no domingo 13/09 ensinar a própria mãe a
  cadastrar as peças dela. É a primeira vez que alguém de fora da máquina vai usar o
  que esta fábrica constrói, e é a mãe dele. A seção 18.1 diz que despacho aberto do
  Raphael vence qualquer rotação; a execução das 21h26Z tinha subido a prioridade da
  ilha para 1 sem escrever despacho, mas o despacho estava em `dados/despachos.md`,
  aberto, com prioridade máxima.

- **Dois snippets novos, e a separação não é organização — é o Sync desembarcando um
  sem o outro.** Se o painel tiver defeito, a loja no ar não cai com ele; se a loja
  mudar, ela não perde o acesso.
  - `snippets/clubedomosaico-loja.php` **1.0.0** = snippet **#9** (criado pelo Sync):
    CPT `peca`, taxonomias `colecao` e `tecnica`, a ficha pública em `/loja/<slug>/`,
    a vitrine com foto e o endpoint de cópia da seção 24.
    sha256: `769be91f7e43...`
  - `snippets/clubedomosaico-atelie.php` **1.0.1** = snippet **#10**: papel `artesa`,
    a usuária e o e-mail de acesso, `/atelie/` com login, lista e formulário.
  - `snippets/clubedomosaico-casca.php` **1.9.0**: UMA linha de mudança, o filtro
    `cdm_vitrine_de_pecas`.
  Manifest na revisão **17**; `/status` conferido às 23h13Z (revisão 16) e de novo
  depois do conserto de 1.0.1.

- **OS CINCO ITENS DO CORTE SAÍRAM.** (1) CPT `peca` com `show_ui` FALSE — ela nunca
  vê o wp-admin, e isso é requisito escrito dele — mais o papel `artesa` com sete
  capacidades e o bloqueio duplo; (2) a usuária criada e **o e-mail de acesso enviado
  às 23h13m23s Z**; (3) `/atelie/` com login e tela inicial; (4) o formulário de peça
  em uma tela, no celular; (5) a ficha pública com `Product`+`Offer` e a `/loja/`
  listando. **Uma URL nova**, `/atelie/`, que é `noindex`: a ilha vai de 11 para 12
  páginas publicadas e continua com 11 no índice.

- **O que ficou FORA, por escrito no próprio despacho:** o formulário "Verificar
  disponibilidade" e o CPT `lead_peca` (adendo 3 de 11/09), a aba Interessados, a
  exportação CSV, "Meus dados", o feed do Merchant Center e as páginas de técnica e
  de coleção.

- **A METADE DO PORTÃO QUE A FUNDAÇÃO NÃO CUMPRE, e por que fabricar um jeito seria
  pior que não cumprir.** O despacho manda entrar em `/atelie/` como `artesa` e
  cadastrar uma peça de teste. A senha dela **não existe** em lugar nenhum a que a
  nuvem tenha acesso: o snippet gera uma senha aleatória e a descarta sem imprimir em
  log, e-mail ou option, e o que chega a ela é um link na caixa dela. Gravar a senha
  ou criar um segundo acesso para "poder testar" quebraria a única coisa que protege
  a conta de uma pessoa de verdade. O portão foi partido em duas metades
  **declaradas** no cabeçalho do `teste-atelie.php`, e a metade da LARGUra — os 360
  px que o despacho escreve dentro do portão — foi cumprida num Chromium de verdade,
  porque essa uma máquina mede melhor que um humano.

- **A senha é criada em `/atelie/` e não no `wp-login.php`** — único desvio
  consciente da especificação de 10/09, e a favor dela: o fluxo nativo manda o link
  para uma tela com a marca do WordPress e um medidor de força de senha, que é a
  definição literal do que o portão reprova. A CHAVE continua nativa
  (`check_password_reset_key` e `reset_password`); a TELA é a nossa, com o logo dela,
  e ao terminar ela já entra logada.

- **Reordenar foto é botão ◀ ▶ e não arrastar-e-soltar**, contra o que a
  especificação pedia, por duas razões que valem mais que a especificação: arrastar
  depende de JavaScript (portão 22.8) e de precisão de dedo, e ela vai cadastrar de
  um celular.

- **O QUE OS PORTÕES ACHARAM, e nenhum foi achado lendo código:**
  1. **O `teste-casca` reprovou o painel, e estava certo.** Ele cobrava que a ÚNICA
     página fora do índice fosse a camada de prova. O painel sai do índice por outro
     motivo, e as duas razões exigem tratamentos OPOSTOS — a de prova TEM de ser
     citada por outra página, esta NÃO pode ser citada por nenhuma. Nasceu a camada
     `privada`, declarada no markup e cobrada nas duas direções. A exceção pelo nome
     do slug foi recusada: seria a heurística por vizinhança que a seção 8 proíbe.
  2. **Dois filtros que eu escrevi e ninguém aplicava**, achados antes de rodar uma
     linha: um em `cdm_vitrine_de_pecas` que a casca não aplicava, e um em
     `clubedomosaico_status` que o Sync não aplica porque **ele se pula a si mesmo por
     desenho**. Portão que nunca roda é função morta. O primeiro virou filtro de
     verdade na casca (a única mudança da 1.9.0), o segundo virou rota pública.
  3. **A direção da foto num campo escondido.** Campo `hidden` é enviado seja qual
     for o botão apertado, então o botão "para frente" mandava "para trás" junto e a
     foto andava para o lado errado. Virou `value` do próprio botão, e a mutação 22 é
     esse defeito escrito de volta.
  4. **Os botões de foto tinham 38 px** — achado pelo medidor de navegador a 360 px,
     e invisível em leitura de código e no HTML servido, porque só o motor de layout
     sabe o tamanho que o botão ficou tendo. São os menores do painel e os que ela
     mais vai apertar com o dedo. Viraram 44, na versão **1.0.1**, depois de a 1.0.0
     já estar no ar.
  5. **O canonical da BANCADA** dizia `/vaso-azul/` e o site diz
     `/loja/vaso-azul/` — defeito da bancada, mesma família de "a bancada e o site
     lendo fontes diferentes para o mesmo campo".
  6. **A description abria cinco frases em minúscula depois de ponto**, visto ao
     renderizar a primeira ficha, não em revisão de código.
  7. **O piso de tamanho de página do `teste-loja` estava cravado em 40 KB**,
     calibrado na F2 que carrega uma ferramenta inteira, e REPROVAVA fichas corretas
     de 26 KB. Passou a ser DERIVADO de `/contato/` na mesma bancada: piso inventado
     reprova o certo.
  8. **Código morto que a mutação expôs:** um `str_replace` de `%0D%0A` que nunca
     podia disparar, porque `rawurlencode` de `\n` já devolve `%0A`. Saiu do snippet,
     e a mutação saiu com ele.
  9. **NO AR, e este foi o mais humilhante:** o conferidor contou 6 cartões de peça
     numa Loja com ZERO peça publicada, e os 6 eram os seletores da própria folha de
     estilo. É literalmente o erro que a seção 8 nomeia — medir no HTML inteiro em vez
     de no CORPO — cometido por quem tinha acabado de escrever uma bancada que faz
     isso certo. A bancada media no corpo, o conferidor no ar não, e **nada obrigava
     os dois a concordarem**.
  10. **Três réguas minhas erradas no medidor de navegador:** o piso de 200
     caracteres de corpo, emprestado da regra de página fina que existe para página
     de ÍNDICE, reprovava a tela de entrar, a lista e a de criar senha — as três
     estão certas, porque tela de ação boa tem pouco texto; e duas réguas do painel
     aplicadas na FICHA da peça, que não tem formulário (o botão dela é um link
     `wa.me`) e que mostra foto grande e título na primeira tela, exatamente o que o
     `DESIGN.md` manda. **Apertar o portão errado reprova o desenho certo** — é a
     mesma lição que a Aquametria escreveu em 12/09 sobre catálogo e ficha.
  11. **O `/loja/<peça>/` na tabela do `ARVORE.md`** foi reprovado pelo portão da
     casca, com razão: ele cobra que toda linha daquela tabela exista no código, e
     molde não é página. Foi para a prosa da seção 3b.

- **VERIFICAÇÃO, 0 falha.** `teste-casca` 546 (era 539); `teste-loja` **140, novo**,
  com 72 estados da ficha em processo próprio; `teste-atelie` **209, novo**, com 9
  telas em processo próprio; `teste-navegador-atelie.mjs` **91 medições, novo**, em 6
  páginas × 5 larguras num Chromium de verdade, com um contexto de
  `javaScriptEnabled: false` para medir a 22.8 de verdade; `teste-f1` 67, `teste-f2`
  72, `teste-prestacao-rejunte` 5 sobre 720 estados, `conferir-cobertura` 128,
  `validar-banco` e `validar-pastilhas` aprovados, `php -l` em tudo (com `<?php`
  prefixado, porque o snippet desta ilha nasce sem a tag).

- **MUTAÇÕES.** `mutacoes-loja` **23 de 23** reprovadas, **22 que só o portão novo
  pega**; `mutacoes-atelie` **26 de 26**, **23 que só o novo pega**. E **quatro
  passaram na primeira passada**, as quatro lacunas reais do meu portão: duas porque
  ele media TELAS e nunca DISPARAVA os ganchos (`admin_init` e o filtro da barra não
  aparecem em HTML nenhum), uma porque a varredura da senha NOMEAVA dois lugares onde
  procurar e a mutação gravou num terceiro, e uma porque eu conferia a função de
  mascarar o e-mail sem conferir se a rota a CHAMAVA. As nove baterias antigas
  rodadas inteiras, nenhuma inerte: árvore 20, cobertura 14, f1 27, f2 20, ga4 14,
  pastilhas 12, prestação 11, rejunte 12, voz-e-cabeça 24.

- **NO AR.** `/status` na revisão 16 igual à do manifest às 23h13Z, em UM disparo, 9
  itens aplicados, snippets #9 e #10 criados pelo Sync; e a revisão 17 depois do
  conserto de 1.0.1. `conferir-atelie-no-ar.py` **novo, 33 afirmações, 0 falha, 1
  pulada**: `/atelie/` em 200 servindo a tela de entrar, com `noindex`, FORA do
  sitemap (varrido pelo índice e pelos sub-mapas), ZERO links para ela nas oito
  páginas públicas, e o corpo sem dizer "WordPress", "wp-admin" ou "wp-login" uma
  vez; a rota RECUSANDO sem token (401) **antes** de ser usada com token; as sete
  capacidades presentes e NENHUMA das oito proibidas; o e-mail MASCARADO na resposta.
  A pulada é a ficha da peça, porque não há peça publicada — e esse é o estado certo
  hoje. `conferir-no-ar.py` também rodado: 339 afirmações, 0 falha.

- **O QUE FALTA, E SÓ UM HUMANO FAZ:** confirmar que o e-mail **chegou** na caixa de
  mina196@hotmail.com. `wp_mail` devolveu true, o que diz que o servidor **aceitou** a
  mensagem, não que ela passou do filtro de spam da Hotmail — e a linha 178 do
  `PROMPT.md` manda tratar queda em spam como **bloqueio da ilha**. E o dedo dela na
  tela.

- **A option `cdm_whatsapp` continua VAZIA**, e por isso a ficha da peça serve, no
  lugar do botão, a frase de que o contato ainda não foi publicado — em vez de um
  número inventado. É o primeiro item da fila e é de UMA linha.

- **Próximo passo, com ordem e motivo:** (a) a option `cdm_whatsapp`, que é o que
  transforma a ficha da peça em venda e não depende de bloco nenhum; (b) o adendo 3
  inteiro (`lead_peca`, notificação por e-mail, aba Interessados, CSV), que era o
  corte de hoje e volta à fila agora que o painel está de pé; (c) a ordem de BANCO
  que o estado anterior deixou e que continua valendo — fechar 2×2 na categoria
  pastilha, que está a UM item dos 3 da 14.3, depois a vitrine de pastilha da F1,
  depois a categoria cola.

- **ESTA EXECUÇÃO FOI O CASO QUE PRODUZIU A SEÇÃO 1.1 DO CONTRATO**, escrita por OUTRA
  execução enquanto esta trabalhava, e o registro dela é útil aqui porque ela nos
  salvou: o bloco durou 65 minutos, a reserva de 22h25Z venceu a janela de 40 minutos
  do passo 3, e uma quarta execução da Fundação teria pegado esta ilha por estar
  "livre" pela letra da regra. Se tivesse pegado, teria rodado o item 2 do despacho e
  mandado um **segundo e-mail de acesso para a mãe do Raphael** — e o segundo
  invalida o link do primeiro, na véspera do dia marcado. Ela não pegou porque
  escreveu a regra antes de agir: reserva vencida se reconfere no git, e commit na
  pasta da ilha nos últimos 40 minutos significa ilha VIVA.
  **A 1.1 também manda quem passa de 40 minutos reescrever `executando_desde` no
  próximo commit, e esta execução NÃO fez isso** — a regra não existia quando ela
  começou, e o commit intermediário das 23h13Z manteve o relógio de 22h25Z. Fica
  escrito para a próxima: renovar é uma linha, e é o que faz a execução seguinte não
  precisar do git para saber.

- **Segundo desembarque, e o que ele provou de quebra:** a revisão 17 subiu às 23h28Z
  com a casca do painel em 1.0.1, e o `/atelie/` no ar serve `min-height:2.75rem` nos
  botões de foto. E a rota de conferência mostrou `tentativas: 1` com a MESMA hora de
  envio — ou seja, **o segundo Sync não reenviou o e-mail de acesso**. A guarda por
  option funcionou exatamente onde precisava funcionar: e-mail repetido para a Hotmail
  é o caminho mais curto para a caixa de spam, e caixa de spam aqui é uma pessoa
  esperando na frente do filho sem conseguir entrar.

13/09/2026 11:56Z — ADENDO 3 ENTREGUE: os leads da Loja, e tres defeitos herdados que sairam junto

**O BLOCO.** O adendo 3 de 11/09/2026 — o formulario "Verificar disponibilidade",
o CPT `lead_peca`, a notificacao por e-mail, a aba Interessados e a exportacao
CSV — ficou FORA do corte do despacho de 12/09 **por escrito**, e voltou a fila
agora que o painel esta de pe. Saiu inteiro. Snippet novo
`clubedomosaico-leads.php` 1.0.0 (snippet #11, criado pelo Sync), `loja` 1.1.0,
`atelie` 1.1.0, manifest na revisao 18, `/status` conferido as 11h56Z **em UM
disparo**, 10 itens aplicados.

**O QUE MUDOU NA FICHA DA PECA.** O botao principal deixou de ser um `wa.me`
direto e passou a ser "Verificar disponibilidade": um `<details>` que abre um
formulario de **dois campos** — nome e WhatsApp, e nada mais, como o adendo
manda ("Sem e-mail, sem CEP") — com o texto de consentimento e o link para
`/privacidade/`. Envia, grava o lead, manda o aviso para
`mina196@hotmail.com` com um botao que abre a conversa **com o cliente**,
mensagem ja escrita, e volta para a peca dizendo "Pronto, {nome}!".

**AS SETE DECISOES, e a cicatriz que cada uma evita** (estao inteiras no
cabecalho do snippet; aqui o resumo):

1. **Terceiro snippet, nao um pedaco da Loja.** O Sync desembarca um sem o
   outro — e este e o primeiro arquivo desta ilha que guarda DADO DE PESSOA.
2. **A Loja aplica `cdm_peca_acao`, e ele e aplicado de verdade.** A cicatriz e
   de 12/09, aqui mesmo: dois `add_filter` sem ninguem do outro lado. Por isso
   os portoes medem os DOIS lados — que a Loja CHAMA, e que o que volta aparece
   no corpo servido. Sem o snippet de Leads no ar, a ficha volta ao que servia
   ontem, e nao quebra.
3. **Funciona com o JavaScript desligado** (22.8). O unico script e a mascara do
   telefone, e ela e enfeite: quem canoniza e o PHP.
4. **O nome da pessoa nao viaja na URL.** O POST guarda a confirmacao num
   transient de 10 minutos e redireciona com uma CHAVE aleatoria — o nome nao
   entra no historico, no Referer nem no log de acesso, e quem nao enviou nada
   nao consegue fabricar a tela de "enviado".
5. **O estado com parametro sai `noindex`**, pela mesma razao da F2.
6. **O lead NAO vai para o repositorio.** A copia da secao 24 para a PECA e o
   endpoint `/v1/pecas`; para o LEAD e o CSV dentro do painel, na mao dela. Nao
   ha rota REST de lead — e o portao mede a AUSENCIA, no banco e no ar.
7. **A aba nao cria capacidade nova.** As mesmas sete de ontem: quem pode editar
   as pecas pode ver quem perguntou por elas.

**O DEFEITO QUE O PORTAO PEGOU ANTES DO AR, e a forma dele vale mais que o
conserto.** `cdm_leads_nome_da_artesa()` nasceu lendo o `first_name` da usuaria e
descartando o valor quando ele fosse a palavra "artesa" — uma **lista de palavras
proibidas**, exatamente a heuristica por vizinhanca que a secao 8 do contrato
proibe. Falhou na primeira medicao pelo motivo mais previsivel: o que o snippet
do Atelie grava ali e `Artesã`, com til e cedilha, e nenhuma lista de palavras
acerta a grafia de um texto de espera que ela nao escreveu. A mensagem teria dito
**"Aqui é Artesã"** para uma cliente de verdade. A saida nao foi uma lista melhor:
o nome publico passou a ser **DECLARADO** na option `cdm_artesa_nome`, que nasce
vazia — e vazia significa uma coisa so, que a identidade de `identidade/artesa/`
ainda nao chegou, que e o mesmo estado que o `PROMPT.md` ja manda a pagina Sobre
respeitar.

**O QUE O NAVEGADOR ACHOU, e nenhum apareceria em leitura de codigo.** (a) O
botao "Quero esta peca" saia com **43 px** — um pixel abaixo do alvo de toque,
o mesmo defeito dos botoes de foto do painel em 12/09 e do mesmo jeito, porque so
o motor de layout sabe a altura que o botao ficou tendo. (b) O `select` de estado
da aba saia com 34 px e fonte de 15 px — abaixo de 16 px o iPhone da zoom sozinho
ao tocar no campo e a tela pula. (c) **A aba Interessados vazia nao tinha uma
unica acao**: uma tela sem saida, e o portao a chamou de beco. Ganhou "+ Nova
peca" e "Ver minhas pecas".

**TRES REGUAS DO NAVEGADOR MEDIAM A COISA ERRADA, e as tres teriam reprovado
codigo certo.** (1) `getBoundingClientRect()` de um elemento dentro de um
`<details>` FECHADO **nao devolve zero** neste Chromium — o conteudo e escondido
por `content-visibility`, que pula a pintura e preserva a caixa; medindo altura,
"antes" e "depois" davam o mesmo numero. Quem decide e `details.open`, e ele e a
prova da 22.8 porque o clique acontece num contexto com o JavaScript
**desligado**. (2) O alvo de toque era medido no proprio campo, e o alvo de um
checkbox e o **rotulo** que o liga; e um honeypot, que esta fora da vista, fora do
teclado e fora do leitor de tela, tem caixa de layout e era cobrado. As duas
exclusoes sao ESTRUTURAIS, declaradas no markup — nunca pelo nome do campo. (3)
"existe formulario E todo formulario POSTa" era uma afirmacao so, e reprovou a aba
vazia, que legitimamente nao tem formulario nenhum. Virou duas: todo formulario
PRESENTE POSTa, e a tela tem pelo menos um lugar onde agir.

**OS TRES DEFEITOS HERDADOS, achados ao rodar os portoes ANTES de construir
(secao 18.5).** A execucao das 02h33Z de 13/09 gravou os links de afiliado e nao
rodou portao nenhum:

- **DOIS BANCOS ESTAVAM COMMITADOS FORA DO MANIFEST.** `materiais-colas.json` e
  `materiais-rejuntes.json` divergiam do `sha256` do manifest desde 12/09 — os
  **dez links de afiliado estavam no repositorio e nao estavam no ar**. E a secao
  4 na forma mais pura: o site fica para tras em silencio. O manifest deste bloco
  os levou junto, e o `/status` na revisao 18 e a prova.
- **O PROGRAMA DO MERCADO LIVRE ESTAVA GRAVADO COMO `mercado_livre`** e o
  esquema declara `mercadolivre`. O `validar-banco.py` reprovava; ele nao tinha
  sido rodado. Corrigido no banco, que e o lado errado — o esquema e a
  declaracao.
- **AS REGUAS DA F1 E DA F2 MEDIAM UM MUNDO COM ZERO LINK.** Elas cobravam a
  frase "Link de loja em breve" no corpo da ancora, e isso era verdade so
  enquanto NENHUM item tivesse link. Na noite em que as dez colas e rejuntes
  ganharam link, as duas reprovaram **sem defeito nenhum embaixo** — a ilha tinha
  melhorado e a regua chamou isso de erro. E a familia que a Aquametria nomeou em
  12/09: **regua que depende de um caso raro do banco morre no dia em que o banco
  melhora.** As tres (bancada da F1, bancada da F2 e a conferencia no ar) passaram
  a medir o COMPORTAMENTO nos dois lados — item sem link reserva o lugar, item com
  link serve o botao patrocinado —, e a bancada ganhou um mundo produzido de
  proposito (`sem_links=1`) para poder medir o lado que o banco de hoje nao tem.

**VERIFICACAO NA BANCADA, 0 falha:** teste-leads **175 NOVO** (8 estados de
pagina, um processo cada), teste-loja 147 (era 140), teste-atelie 209,
teste-casca 546, teste-f1 70 (era 67), teste-f2 74 (era 72),
teste-prestacao-rejunte 5 sobre 720 estados, conferir-cobertura 128,
validar-banco aprovado, validar-pastilhas aprovado, `php -l` em tudo.
**NAVEGADOR:** teste-navegador-atelie **124 medicoes** em 7 paginas x 5 larguras,
0 falha, 0 px de rolagem lateral em todas.
**MUTACOES:** mutacoes-leads **36 de 36 reprovadas, 34 que so o portao novo
pega**. Sete delas sao de PRIVACIDADE — o nome na URL, o IP em texto puro, o nome
no titulo do registro, o tipo publico, o tipo na REST, o tipo na busca, a copia
para o Raphael sem option — porque trava de privacidade que ninguem quebra de
proposito e trava que ninguem sabe se funciona. **QUATRO PASSARAM NA PRIMEIRA
PASSADA, e eram quatro buracos reais do meu portao:** o IP guardado em texto puro
(o portao media que o limite funcionava e nao COM O QUE ele o fazia), o e-mail que
falha apagando o lead (o stub da bancada esquecia de apagar, entao a contagem nao
mudava), a acao da aba sem conferir capacidade (o portao media a TELA e nunca as
ACOES) e o despacho de um estado que ninguem registrou como aba (so mensuravel
PRODUZINDO um atendente intrometido).

**NO AR as 11h56Z, em UM disparo:** `/status` na revisao 18, igual a do manifest,
10 itens aplicados, snippet #11 criado. `conferir-no-ar.py` 339 afirmacoes, 0
falha, as 11 URLs intactas. `conferir-atelie-no-ar.py` 37 afirmacoes (era 33), 0
falha, 2 puladas — e as sete capacidades do papel `artesa` continuam sendo
exatamente sete, com nenhuma das oito proibidas, que era a razao da decisao 7.
Medido no ar tambem: a folha do snippet de Leads sai no `/atelie/` (ele esta
ATIVO) e `/v1/leads`, `/v1/lead_peca` e `/v1/interessados` respondem **404** —
lead nao sai por endpoint.

**O QUE NAO FOI MEDIDO NO AR, e e pulada declarada, nao aprovada:** o formulario
so existe em pagina de peca e **nao ha peca publicada**. Ele esta medido na
bancada, em 8 estados, e no navegador a 360 px; no ar, so quando a artesa
publicar a primeira peca. Esta escrito assim no proprio `conferir-atelie-no-ar.py`.

**UMA CONSEQUENCIA QUE VALE DIZER:** a option `cdm_whatsapp` **deixou de decidir
se a peca tem como ser pedida**. Ela estava vazia e por isso a ficha servia a
frase de que o contato nao foi publicado; agora o caminho de venda e o
formulario, que nao depende de numero nenhum. O item "a option de uma linha"
sai da lista do que trava a venda — continua util para um botao direto no
futuro, mas nao bloqueia mais nada.

**PROXIMO, com ordem e motivo:** (a) **"Meus dados"** dentro do painel, que e o
que torna a option `cdm_email_leads` editavel por ela e fecha o unico pedaco do
adendo 3 que ficou em codigo — a option existe e funciona, mas so por
`update_option`; (b) a ordem de BANCO que o estado anterior ja deixava: fechar
2x2 na categoria pastilha, que esta a UM item dos 3 da 14.3, depois a vitrine de
pastilha da F1, depois a categoria cola; (c) o feed do Merchant Center, que
**depende de haver peca publicada** e por isso nao e escolha de fila e sim de
espera. E um item que so um humano fecha, o mesmo de ontem: confirmar que o
e-mail de acesso CHEGOU na caixa da Hotmail.

**A REVISÃO 19, no ar às 12h16Z, e por que houve um segundo desembarque.** Foram **dois disparos**: o primeiro leu do `raw` um manifest ainda na revisão 18 (o cache é por caminho, seção 4), e o segundo, um minuto depois, aplicou os 10 itens. `/status` na 19, `conferir-no-ar.py` 339 afirmações e `conferir-atelie-no-ar.py` 37, zero falha nos dois. Três coisas só
apareceram depois de o primeiro estar no ar:

- **O CSV podia ser EXECUTADO pela planilha dela.** O campo `nome` é digitado por
  qualquer pessoa que abra a ficha de uma peça na internet, e planilha trata
  célula que começa por `=`, `+`, `-` ou `@` como **fórmula** — um nome escrito
  como `=HYPERLINK(...)` vira um link clicável dentro do arquivo que a artesã
  abre. As aspas do CSV protegem a **coluna**, não a leitura; o que protege é um
  apóstrofo na frente. Duas mutações novas medem os dois erros possíveis: não
  escapar, e escapar tudo (que devolve o verde e quebra a leitura).
- **O `From: contato@` que o adendo pede aponta para uma caixa que não existe.**
  A mesma linha do adendo diz que a casca "precisa criar a conta `contato@` no
  cPanel OU garantir SPF/DKIM", e isso é do Raphael e não foi feito. Muita
  hospedagem recusa enviar com remetente que não é caixa local, e aí o lead fica
  gravado e a artesã não fica sabendo dele até abrir o painel. Agora, se a
  primeira tentativa falhar, vai uma **segunda com o remetente padrão do
  WordPress** — o mesmo que entregou o e-mail de acesso dela em 12/09 — e o
  caminho usado fica **gravado no lead**, para a ronda ver que o `contato@` não
  está de pé em vez de descobrir pela ausência.
- **Não deu para conferir SPF/DKIM daqui.** `dns.google` e `cloudflare-dns.com`
  respondem **403 ao CONNECT por política de egresso**, em duas passadas cada,
  como a 20.2 manda testar antes de declarar. Não é intermitência de túnel: é a
  lista Personalizada da rede das rotinas, que tem os domínios das ilhas,
  `googleapis` e `github`, e nenhum resolvedor de DNS. Fica declarado, não
  presumido.

**Números finais, com as duas revisões dentro.** Bancada: teste-leads **184**,
teste-loja 147, teste-atelie 209, teste-casca 546, teste-f1 70, teste-f2 74,
teste-prestacao-rejunte 5 sobre 720 estados, conferir-cobertura 128 — 0 falha em
todas. Navegador: 124 medições em 7 páginas × 5 larguras, 0 falha. Mutações:
**mutacoes-leads 40 de 40 reprovadas, 38 que só o portão novo pega, 0 inertes**.
**As onze baterias antigas rodadas inteiras, para provar que nenhuma virou
inerte: árvore 20, ateliê 26, cobertura 14, F1 27, F2 20, GA4 14, loja 23,
pastilhas 12, prestação 11, rejunte 12 e voz-e-cabeça 24 — 203 mutações, 203
reprovadas, 0 passaram, 0 inertes.**

## 13/09/2026 — "MEUS DADOS": a aba onde ela manda no que só existia em código

Ateliê **1.2.0**, Leads **1.1.0**, manifest na **revisão 20**. **Nenhuma URL
nova.** Fecha o último pedaço do adendo 3 que tinha ficado por fazer — a option
`cdm_email_leads` existia, funcionava, e só a Fundação podia mexer nela — e
cumpre a linha do `PROMPT.md` que promete desde 10/09 que "ela troca a senha em
Meus dados dentro do painel".

**A ABA TEM TRÊS SEÇÕES, e a divisão entre elas é a decisão do bloco.** "Seu
acesso" mostra o e-mail da conta **como texto**; "Sua senha" troca a senha; e
"Avisos de interessados" — que **não é deste arquivo** — traz o endereço para
onde vai o aviso e o nome que assina a mensagem do WhatsApp.

- **A TROCA DE SENHA NÃO PEDE A SENHA ATUAL, e isso é escolha e não esquecimento.**
  O WordPress não pede na tela de perfil dele, e aqui a razão é mais forte que a
  dele: **ela entrou na conta por um link de e-mail** e pode legitimamente não
  saber a senha que quer trocar. Pedi-la trancaria a porta justamente para quem
  tem a chave. O que protege a ação é sessão autenticada + nonce, e o custo de
  errar para este lado é conhecido e menor — quem já está dentro da sessão dela
  já podia publicar, apagar e exportar os interessados. Se um dia houver mais de
  uma pessoa no ateliê, a linha se reabre; está escrita no cabeçalho do snippet.

- **O E-MAIL DA CONTA APARECE E NÃO SE EDITA.** É o endereço para onde vai o link
  de recuperar a senha; um dedo errado num teclado de celular a deixaria de fora
  da própria conta, sem ninguém do outro lado para socorrer no domingo. Aparecer
  responde a única pergunta que ela vai fazer sobre esse endereço ("para onde vai
  o link?"); virar campo é risco sem ganho. O portão mede as duas metades: que o
  endereço **aparece** e que **não existe `<input>` com ele**.

- **QUEM LÊ A OPTION É QUEM A ESCREVE — e por isso nasceu um terceiro ponto de
  extensão.** `cdm_email_leads` e `cdm_artesa_nome` são lidas **só** pelo snippet
  de Leads, então os campos delas nascem lá e chegam à tela pelo filtro
  `cdm_atelie_meus_dados`, do mesmo jeito e pela mesma razão que a aba
  "Interessados" chega pelo `cdm_atelie_abas`: **o Sync desembarca um snippet sem
  o outro**, e uma tela que promete um campo cujo dono não está no ar é a
  divergência silenciosa que esta ilha já pagou duas vezes. **Cada seção é um
  formulário próprio**, com nonce e gravação próprios — nada de um caminho de
  salvar compartilhado onde o campo de um dono sobrescreve o do outro por
  descuido. E a borda do cartão não é enfeite: é o que diz onde um formulário
  acaba e o outro começa, para ela não apertar "Trocar a senha" achando que
  salvou os dois.

- **O VAZIO CONTINUA SIGNIFICANDO O QUE SIGNIFICAVA, e agora a tela DIZ isso.**
  E-mail em branco é "avise no endereço padrão"; nome em branco é "a identidade
  da artesã ainda não chegou", e a mensagem assina "do Clube do Mosaico". Os dois
  campos escrevem embaixo o que o branco faz e **qual é o estado de hoje**, em
  vez de deixar ela adivinhar se esqueceram de preencher ou se é assim mesmo. E
  branco **grava** branco em vez de ser ignorado: sem isso ela não teria como
  desfazer um endereço digitado por engano.

- **E-MAIL INVÁLIDO NÃO DERRUBA O QUE FUNCIONAVA.** O antigo fica de pé e a tela
  diz que não deu. A direção sai da assimetria de custo, como manda a seção 10:
  trocar um endereço que recebe por um que não existe é o aviso do interessado
  sumindo sem ninguém perceber.

**A GUARDA DE `defined()` NO SNIPPET DE LEADS não é paranoia, é a ordem do
desembarque:** este arquivo pode chegar ao ar minutos antes do Ateliê 1.2.0, que
é quem declara `CDM_ATELIE_ABA_DADOS`. Sem ela, um POST daquela ação levaria erro
fatal do PHP no lugar da tela. Com ela, a ação simplesmente não existe enquanto o
outro lado não chega — que é o mesmo que já acontece com a seção, porque o filtro
não é aplicado.

**O QUE A BANCADA GANHOU, e ela é a metade que dá sentido ao filtro:** o
`render-para-teste.php` passou a **produzir o mundo em que um snippet não
desembarcou** (`sem_leads=1`), na mesma família do `sem_links` de 13/09. "A tela
não promete o que o dono ausente não entrega" é uma afirmação que **só pode ser
medida com o dono ausente**, e não há como produzir essa ausência lendo código —
só deixando de carregar o arquivo. O portão mede os dois lados: com o Leads no
ar a seção aparece; sem ele, ela some **e a troca de senha continua inteira**.

**DUAS MUTAÇÕES PASSARAM NA PRIMEIRA PASSADA, e as duas eram buraco de portão —
não de código.** É o resultado do teste, não um detalhe:

1. **`34 quem não está logada troca a senha dela`.** Todas as afirmações da aba
   rodavam **com a artesã logada**, e por isso nenhuma delas via a guarda de
   sessão cair. A mutação removeu `is_user_logged_in()` e `current_user_can()` da
   ação e ficou verde. **Um portão que só mede o caminho feliz da recusa mede a
   recusa errada.** O conserto foi medir a ação deslogada e logada-sem-capacidade
   — o nonce da bancada é determinístico, e é isso que torna a medição possível:
   quem está de fora consegue calculá-lo, que é exatamente o mundo contra o qual
   a capacidade protege.
2. **`48 a tela para de dizer para onde os avisos vão hoje`.** A régua cobrava o
   endereço na tela **com a option vazia** — e aí "hoje" e "o padrão" são o mesmo
   texto, então a frase "deixe em branco para usar mina196@..." satisfazia a
   régua sem a tela dizer nada sobre o estado atual. **Régua que só distingue
   quando os dois valores diferem tem de ser medida onde eles diferem:** a
   afirmação mudou de lugar e passou a rodar depois de gravar um endereço
   diferente do padrão.

**E UMA MUTAÇÃO ANTIGA TINHA VIRADO INERTE nesta mesma passada** — a `24 o script
volta para dentro do shortcode`. O alvo dela era "o `</form></div>` que vem antes
do `add_shortcode`", e o Ateliê 1.2.0 pôs duas funções entre um e outro. **Alvo
de mutação que depende da vizinhança morre no dia em que o vizinho se muda**, e
mutação inerte não mede nada — ela conta como "passou". Reescrita com âncora no
próprio fim do formulário da peça.

**UM DEFEITO MENOR CONSERTADO DE PASSAGEM:** o piso de 8 caracteres da senha
estava escrito três vezes na tela de criar senha (o `strlen`, dois `minlength` e
a frase de ajuda). Virou `CDM_ATELIE_SENHA_MINIMA`, uma vez, para as duas telas
não poderem divergir.

**VERIFICAÇÃO NA BANCADA, 0 falha:** `teste-atelie` **251** (era 209),
`teste-leads` **210** (era 184), `teste-casca` 546, `teste-loja` 147, `teste-f1`
70, `teste-f2` 74, `teste-prestacao-rejunte` 5 sobre 720 estados,
`conferir-cobertura` 128, `validar-banco` aprovado, `validar-pastilhas` aprovado,
`php -l` em tudo. **NAVEGADOR:** `teste-navegador-atelie` **128 medições em 8
páginas × 5 larguras**, 0 falha, 0 px de rolagem — a tela nova passou de primeira
no alvo de toque e na fonte de 16 px, porque reusa `.cdm-at-campo` e
`.cdm-at-botao` em vez de inventar botão.

**MUTAÇÕES: 262 em 12 baterias, 262 reprovadas, 0 passaram, 0 inertes.**
`mutacoes-atelie` de 26 para **37** e `mutacoes-leads` de 40 para **48** — as 19
novas atacam a aba pelas duas famílias de sempre: as que **abrem porta** (o nonce
que some, a capacidade que some, o piso da senha que cai, o segundo campo que
deixa de ser conferido) e as que **vazam segredo** (a senha no endereço de volta,
o e-mail da conta virando campo). As dez baterias antigas rodadas inteiras:
árvore 20, cobertura 14, F1 27, F2 20, GA4 14, loja 23, pastilhas 12, prestação
11, rejunte 12 e voz-e-cabeça 24.

**NO AR às 14h04Z, e foram TRÊS revisões e quatro disparos, por um motivo que não
era o cache.** `/status` na **revisão 22** igual à do manifest, 10 aplicados,
`conferir-no-ar.py` **339** afirmações e `conferir-atelie-no-ar.py` **45** (era
37), 0 falha nos dois, as 11 URLs intactas, e as sete capacidades do papel
`artesa` continuam sendo exatamente sete. A marca do código novo foi medida **no
corpo servido**, não no log do Sync: `.cdm-at-secao` só existe no Ateliê 1.2.0, e
a folha do painel sai no `/atelie/` mesmo deslogada — é a diferença entre "o
manifest diz que subiu" e "o site está servindo". Medido também que
`?estado=meus-dados` deslogada cai na tela de entrar, sai `noindex`, e **não
serve** `trocar_senha`, `cdm_email_leads`, `cdm_artesa_nome` nem o e-mail dela.

**PULADA DECLARADA, não aprovada:** a aba só existe para quem entrou, e a
Fundação não entra — a senha da artesã não existe para a nuvem, por desenho. O
que está medido no ar é a versão servida e a ausência do que não pode vazar; o
dedo dela na tela de 360 px continua sendo a metade do domingo.

### O QUE ESTA EXECUÇÃO ENCONTROU E NÃO ERA DELA — dois commits mexeram no banco desta ilha enquanto ela estava reservada

**Isto é o achado mais caro do bloco, e não é sobre "Meus dados".** Os commits
`4e69738` (a escada do link de compra, seção 25 nova do contrato) e `35412c1` (o
`url_produto` do teste de vida) chegaram ao `main` às 13h36Z e depois, editaram
`dados/materiais-colas.json` e `dados/materiais-rejuntes.json` e **não tocaram no
`manifest.json`**. Lido no `/status`, três vezes seguidas: `"materiais-colas:
sha256 divergente — não aplicado"`. **Os dez links novos, o `url_produto` e as
três fotos estavam no repositório e fora do ar** — a seção 4 na forma mais pura, e
a segunda vez no mesmo dia (a execução das 11h56Z tinha achado exatamente isto).

O `4e69738` também deixou **11 erros de esquema**, nenhum dos quais sobreviveria a
um `validar-banco.py` de segundos: `mercado_livre` em três itens onde o
vocabulário declara `mercadolivre` (**o mesmo defeito de 12/09, de volta**),
`imagem` sem `largura`/`altura`, e os contadores de cabeçalho dizendo "nenhuma
foto foi coletada" com três fotos coletadas.

**A LARGURA E A ALTURA DA FOTO: havia dois caminhos, e o cômodo era o errado.** O
feed de afiliado da Shopee — que a seção 25.3 nomeia como a fonte legítima da foto
— **não declara dimensão**. O caminho cômodo era afrouxar o esquema para aceitar
os dois campos ausentes; e ele estaria errado, porque os dois campos existem para
a página **reservar a caixa da foto antes de ela chegar**, e caixa sem medida é o
salto de layout que a seção 22.4 chama de defeito de desempenho. O outro caminho
era **medir**: `cf.shopee.com.br` responde 200 em duas passadas (medido, não
presumido), e nasceu `ferramentas/medir-imagens.py`, que lê a dimensão do
cabeçalho do arquivo servido — JPEG, PNG e WebP, sem biblioteca, porque instalar
Pillow para ler dois inteiros seria trocar uma linha de código por um risco de
ambiente. **1024×1024, 1024×1024 e 768×768, lidas.** `800x800` digitado porque
"foto de e-commerce costuma ser quadrada" passaria no validador exatamente igual —
e seria chute com cara de dado, que é o defeito mais caro que esta fábrica tem.
Download que falha vira `FALHOU` e o item **continua reprovando**: rede fechada
nunca vira número.

**E a metade que não tem conserto do lado da Fundação está em `dados/despachos.md`:**
a reserva por commit da seção 1 funcionou como escrito — esta execução perdeu a
robometria e a aquametria e pegou a clubedomosaico às 13h19Z —, e **uma terceira
sessão editou o banco desta ilha assim mesmo**. A reserva protege contra quem a
lê; não existe para quem entra pela porta do dado. Hoje custou dois rebases e duas
revisões a mais; o custo caro é o do próprio 1.1, dois trabalhos concorrentes na
ilha da artesã no dia em que ela ia aprender a usar o painel. É decisão do
Raphael.

**PRÓXIMO, com ordem e motivo:** (a) a ordem de BANCO que o estado anterior já
deixava — fechar 2×2 na categoria pastilha, que está a UM item dos 3 da 14.3,
depois a vitrine de pastilha da F1, depois a categoria cola; (b) o `url_busca` do
degrau 3 e o segundo link discreto que a seção 25.2 manda pôr embaixo do botão —
os campos chegaram ao banco e **a página ainda não os serve**, então hoje a escada
existe no dado e não na tela; (c) o feed do Merchant Center, que depende de haver
peça publicada e por isso não é escolha de fila e sim de espera. O que só um
humano fecha continua o mesmo: confirmar que o e-mail de acesso CHEGOU na caixa da
Hotmail, e o `contato@clubedomosaico.com.br` que ainda não existe como caixa.

---

## 13/09/2026, 15h18–15h45Z — A ESCADA DA SEÇÃO 25 CHEGA À TELA (f2 1.2.0, manifest revisão 23)

**Terceira ilha tentada nesta execução, e isso é a seção 1 funcionando.** A aquametria foi
reservada às 15h16Z e a robometria às 15h17Z por outras duas execuções; o push da minha
reserva da aquametria foi recusado por cerca de um minuto. O passo 5 manda voltar ao passo 2
e escolher outra ilha, e foi o que aconteceu — sem force push, sem atropelo.

**O bloco é o item (b) que a execução anterior deixou escrito**, palavra por palavra: *"o
`url_busca` do degrau 3 e o segundo link discreto que a seção 25.2 manda pôr embaixo do
botão — os campos chegaram ao banco e a página ainda não os serve, então hoje a escada
existe no dado e não na tela."* Ele venceu a ordem de BANCO que vinha antes na fila porque a
25.2 não é preferência de fila: ela diz que **não existe item publicável sem piso** e que a
página com piso no banco **nunca** diz "em breve". Dez itens estavam nesse estado.

### O que mudou na tela

Nasce `cdm_f2_compra_html()`, dona dos três estados do bloco de compra. **A F1 reusa o mesmo
cartão**, então os dois lugares que servem produto nesta ilha desceram a escada de uma vez:

1. **Com ficha** — a ficha é o botão ("Ver na loja") e a busca desce para a linha discreta
   "Veja todos disponíveis aqui", palavra por palavra como a 25.2 a escreve. As duas convivem
   de propósito: ficha converte melhor, e a busca é a saída de quem chegou num anúncio
   esgotado. O degrau 3 é justamente o que quebrou quatro links em doze horas em 13/09.
2. **Só com busca** — a busca **sobe e vira o botão**, com texto próprio: "Ver as opções na
   loja". O texto muda junto com o papel, e não por estilo: o botão abre uma **lista**, e
   prometer "Ver na loja" ali seria o leitor clicar esperando a ficha do que a página acabou
   de recomendar.
3. **Sem nada** — sobra "Link de loja em breve", e ele deixa de ser estado de espera para ser
   **defeito contado**.

**Por que é função própria e não um `if` dentro do cartão:** a escada é regra do Arquipélago
e o cartão é desenho da ilha. Quem for servir a vitrine de pastilha da F1, a ficha do Guia ou
a página da peça **chama a função** em vez de reescrever quatro degraus que discordariam em
silêncio. O portão mede isso contando a **classe emitida** nos snippets — e não a frase
legível, porque a primeira versão dessa régua contou a frase e reprovou o próprio comentário
que a explica.

### Os três mundos produzidos, e por que `sem_links=1` mudou de significado

O banco de hoje só produz o estado 1, então medir os outros dois no banco de hoje seria medir
o caminho que nenhum cartão percorre — verde com a função quebrada, e o dia em que importasse
seria o dia em que um link morresse.

`sem_links=1` **apaga a ficha e deixa o piso de pé**, que é exatamente o estado 2. Até a
1.1.0 esse mundo produzia "em breve"; depois da 1.2.0, produzir "em breve" nele **é o
defeito**. A afirmação antiga reprovou na primeira rodada, e essa reprovação é a mudança
funcionando. Nasceu `sem_piso=1` para o vazio de verdade.

**A ordem das três réguas importa, e é o que as torna três:** (a) sozinha passaria numa
função que ignora a ficha e serve só a busca; (b) sozinha passaria numa que serve a busca por
cima da ficha; e (c) pega o erro mais provável de quem escreve isto com pressa — deixar o "em
breve" no lugar do piso —, **o único que (a) e (b) aprovariam juntas.**

### O banco aprende o que a seção 25 criou

O esquema não conhecia `url_produto`, `url_busca`, `url_busca_produto`, `degrau` nem
`conferido_em`, e a observação dele ainda mandava a página dizer "em breve" e declarava que
gerar link *"é da Sentinela estratégica, no navegador, e nunca da Fundação"*. As duas frases
são **anteriores à 25.2** e foram **reescritas, não acrescentadas**: deixadas ali, o esquema
contradiria o campo vizinho, e contradição no dado é pior que lacuna porque tem cara de
decisão. O `validar-banco.py` passa a exigir `url_produto` de quem tem link (25.4-b: link
cuja saúde ninguém consegue conferir), a cobrar o degrau, e a **contar** os itens sem piso num
campo novo de cabeçalho, `itens_sem_piso`, reconferido contra o arquivo.

**Os dez sem piso são as pastilhas, e o motivo é medido e não suposto.** Gerar o link de busca
exige a **sessão logada** do painel de afiliado da Shopee, que mora no navegador do Raphael.
Desta nuvem o `custom_link` responde **200 em duas passadas** e serve uma casca de JavaScript
**sem o formulário** — zero ocorrência de `custom_link` e de `sub_id` no HTML servido. **Não é
bloqueio de rede** (a seção 4 manda testar duas vezes antes de chamar de bloqueio, e o teste
foi feito): é falta de sessão, e criar conta ou tocar na conta dele está fora do que esta
camada faz. **Não virou erro duro do validador de propósito** — portão vermelho que ninguém
consegue fechar é portão que se aprende a ignorar; contado e declarado, ele é o número que a
ilha reporta em todo bloco, que foi exatamente o desenho que fez os dez links nascerem em
13/09. **No dia em que os dez `url_busca` forem colados, nenhuma linha de código muda.**

### Uma mutação antiga tinha virado inerte em cada bateria, e inerte conta como passou

O alvo das duas era a linha que **abria** o `<span>` do bloco de compra dentro do cartão, e a
refatoração mudou o vizinho: a abertura desceu para a função nova. As duas acharam zero
ocorrência e foram contadas como PASSOU. É a mesma família da mutação 24 desta ilha em 12/09
— **alvo que depende da vizinhança morre quando o vizinho se muda.** As duas apontam agora
para a **chamada** da função, que é o que governa a ordem hoje.

### Um achado de outra ilha, fechado

A ronda da Aquametria de 13/09 escreveu, por não haver outro canal, que o endpoint de cópia da
seção 24 desta ilha **existia** e devolvia 401, mas que o nome do parâmetro de autenticação
não estava documentado em lugar nenhum — então a cópia da 24 não acontecia e não ia acontecer.
O parâmetro é `token` e o valor é **o mesmo token do Sync**. A URL completa e literal entrou em
"Endpoints desta ilha", conferida desta nuvem: HTTP 200, `{"total":0,"pecas":[]}`. **Zero peça
é resposta, não falha** — o `dados/pecas.json` nasce no dia em que a artesã cadastrar a
primeira.

### A regra nova que subiu para o contrato (seção 1.1)

A 1.1 manda descartar a ilha com commit na pasta nos últimos 40 minutos e **não diz commit de
quem**. Lida ao pé da letra, ela manda a Fundação ignorar por 40 minutos exatamente a ilha que
a **Sentinela** acabou de tocar — que é a ilha com despacho novo, a primeira da 18.1. As duas
regras se contradiziam. O que a 1.1 mede é **execução da Fundação viva**, e `executando_desde:
null` já prova que não há bloco em andamento, **porque a reserva é escrita antes do trabalho**.

### Verificação

**Bancada, 0 falha:** `teste-f2` 87 afirmações (era 74), `teste-f1` 72 (era 70), `teste-casca`
546, `teste-loja` 147, `teste-leads` 211, `teste-atelie`, `teste-prestacao-rejunte` 5 sobre
720 estados, `conferir-cobertura` 128, `validar-banco` APROVADO, `php -l` em tudo.
**Mutações:** f2 **26 de 26** reprovadas, f1 **27 de 27**, **0 inertes** nas duas depois do
conserto dos dois alvos. **Navegador:** 63 medições em 9 páginas × 6 larguras, 0 px de
rolagem, console limpo — e entre as nove está o **mundo produzido em que a busca é o botão**,
porque alvo de toque de botão novo não se mede no mundo onde ele não aparece.

**No ar às 15h40Z, em UM disparo:** `/status` na revisão **23**, igual à do `manifest.json`, 10
aplicados; `conferir-no-ar` **351 afirmações, 0 falha**, com a escada medida **cartão a cartão
no HTML servido** (6 cartões na F2 e 2 na F1, todos com as duas portas) e a marca do código
novo — a classe `cdm-f2-busca` — no corpo servido, que é a diferença entre "o manifest diz que
subiu" e "o site está servindo".

**A primeira versão dessa régua no ar reprovou a página certa**, e vale registrar: ela comparou
as linhas discretas da tela com o número de itens do **banco**, e a âncora serve 6 cartões de
um banco de 10 porque publica um **caso de referência**, não o catálogo. Régua de página medida
com régua de banco. O banco continua na medição, mas no papel certo: dizer o que a tela **não
pode** ter.

**PRÓXIMO, com ordem e motivo:** (1) a ordem de BANCO que já estava escrita e **agora não tem
mais nada na frente** — fechar 2×2 na categoria pastilha, que está a UM item dos 3 da 14.3,
depois a vitrine de pastilha da F1, que já nasce com a escada pronta, depois a categoria cola;
(2) os dez `url_busca` das pastilhas, no minuto em que houver sessão — é copiar e colar no
banco, sem uma linha de código; (3) o feed do Merchant Center, que é espera e não escolha de
fila. O que só um humano fecha continua o mesmo: confirmar que o e-mail de acesso chegou na
caixa da Hotmail, e o `contato@clubedomosaico.com.br` que ainda não existe como caixa.

13/09/2026 17:50Z — O 2×2 FECHA O MÍNIMO DA 14.3, E A FAIXA SOBRE A QUAL A COBERTURA ERA PUBLICADA ESTAVA FALTANDO UM TAMANHO

- **Por que este bloco.** Era a ordem de banco que o estado anterior deixou escrita
  e que não tinha mais nada na frente: fechar 2×2 na categoria pastilha, que estava
  a UM item dos 3 da seção 14.3. Nenhum despacho aberto nesta ilha, nenhum defeito
  da 19.1 registrado pela ronda. **Nenhuma URL nova, nenhum snippet reescrito,
  nenhuma página criada** — manifest na revisão **24**.

- **As três fichas que o bloco 3d deixou pela metade entraram inteiras**, e a
  pendência `pastilha-fichas-colhidas-pela-metade` está FECHADA: **A37** (2×2,
  placa 32,3, 3 mm, 20 placas, 2,086 m², 13 kg), **102** (2,5×2,5, placa 31,7,
  4 mm, 20 placas, 2,01 m², 18 kg) e **IC02** (2,3×2,3, placa 30,0, 8 mm, 10
  placas, 0,9 m², 16 kg). O banco vai de 10 para **13** itens, e **a A37 é o
  terceiro elegível de 2×2**: o tamanho passa de 2 para 3 e cumpre o mínimo da
  14.3. Era o único buraco de cobertura desta ilha que dependia de coleta e não
  de decisão.

- **Coleta.** Busca restrita ao domínio, **duas passadas por SKU** com consultas
  escritas de forma diferente e **nenhuma delas carregando um valor** — as duas
  pediram os rótulos da ficha. As três voltaram idênticas nas duas. O egresso foi
  remedido antes, como a 20.2 manda: `glassmosaic.com.br` e `www.pastilhart.com.br`
  em 000 por `connect_rejected` (política) em duas passadas, com
  `clubedomosaico.com.br` em 200 nas mesmas duas. Por isso `conferir_no_pdf: true`
  nos três, como nos dez anteriores.

- **O ACHADO DO BLOCO NÃO É DO DADO — É DO PRÓPRIO PORTÃO, e ele muda o que a ilha
  vinha publicando sobre si mesma.** O `validar-pastilhas.py` carregava os tamanhos
  da F1 numa constante de **quatro** linhas, com o comentário "os tamanhos que a F1
  oferece". **A F1 oferece cinco:** `cdm_f1_pastilhas_disponiveis()` serve 1×1,
  **1,5×1,5**, 2×2, 2,5×2,5 e o caquinho irregular. A cópia nasceu certa e
  envelheceu calada.

  **O custo não era cosmético.** A seção 14.3 manda varrer "a faixa de entrada de
  cada ferramenta de ponta a ponta", e a cobertura saía publicada sobre quatro
  linhas de uma faixa de cinco: **um tamanho que a ferramenta serve nunca apareceu
  no relatório do buraco.** E logo esse — 1,5 cm é o lado do `pastilhart-af1500`, o
  único item do banco sustentado por distribuidor (nível 5). A **mutação 07** desta
  bateria diz, com todas as letras, que promover o distribuidor "faz 1,5 cm passar
  de zero para um elegível": uma afirmação sobre uma linha que o relatório não
  tinha. Ela reprovava pelo nível na régua por item, e a outra metade nunca foi
  medida.

- **Nasce `ferramentas/tamanhos-da-f1.php`**, irmão do `faixa-da-f2.php`. Ele **não
  lê o código: provoca a ferramenta.** As chaves saem de
  `cdm_f1_pastilhas_disponiveis()`, que é a declaração da própria F1, e cada uma
  passa por `cdm_f1_entrada()` — a MESMA função que saneia a consulta de quem
  visita — para provar que sobrevive ao saneamento. As duas metades falham por
  motivos diferentes: tamanho que a tela lista e o saneamento derruba é tamanho que
  a ferramenta não aceita. **8 afirmações, com a borda dentro delas:** uma chave
  inventada tem de ser recusada, e o padrão do saneamento tem de ser um tamanho que
  a tela lista. É a mesma família do "número de tela nasce contado, nunca digitado"
  da seção 8 e da lista de tipos que a Robometria tirou de dentro da régua hoje de
  manhã pela seção 26: **lista dentro da régua envelhece calada, e o sintoma é o
  portão verde.**

- **As duas primeiras mutações de CÓDIGO desta bateria (13 e 14)** nasceram junto, e
  existem porque a bateria só sabia mexer no banco — portão que só mede o dado não
  vê o defeito que mora na régua. A 13 faz o padrão do saneamento cair num tamanho
  que a tela não lista; a 14 faz o saneamento aceitar qualquer chave. As duas
  **produzem um mundo que o banco não tem como produzir**, que é o que a seção 8
  exige de quem escreve régua nova, e as duas reprovaram.

- **O que os três itens ensinaram sobre o catálogo.** (1) O **102** tem a mesma
  pastilha anunciada de 2,5 cm dos três K e placa de **31,7** contra 30,0 — prova,
  dentro do catálogo de um fabricante só, de que **o lado da placa não se deduz do
  lado da pastilha**; quem completasse um campo pelo vizinho de mesmo tamanho
  erraria 1,7 cm por placa. O próprio endereço o classifica em `uncategorized`,
  então o nome comercial não carrega linha: inventar uma seria atribuir ao
  fabricante uma classificação que ele não publicou. (2) O **IC02** é o único item
  do banco cuja aritmética de ficha fecha **exata** (10 × 30 × 30 = 0,90 m², sem
  corte nem arredondamento), e o lado dele, 2,3 cm, não é nenhum dos cinco do
  seletor — como já acontecia com 3,0, 1,5 e 1,2. Virou pendência nova,
  `pastilha-tamanho-fora-do-seletor-da-f1`: **6 dos 13 itens** têm lado que a F1 não
  oferece, e o que eles medem não é defeito de coleta, é o quanto o seletor é mais
  pobre que o mercado. (3) A **A37** fecha a metragem por CORTE (2,086) e a irmã A61
  por ARREDONDAMENTO (2,09) na mesma caixa — a régua já aceitava exatamente as duas
  operações e diz qual foi usada em cada item, então a A37 entrou sem uma linha nova
  de tolerância.

- **Receita, e o número PIOROU de propósito.** `itens_sem_piso` sobe de 10 para
  **13**, contado do arquivo pelo validador e nunca digitado. Os três novos entram
  sem `url_busca` pelo mesmo motivo medido ontem e hoje: gerar o link de busca exige
  a **sessão logada** do painel de afiliado da Shopee, que mora no navegador do
  Raphael, e isso não é bloqueio de rede. **Inventar um endereço para o contador não
  subir seria trocar defeito contado por defeito escondido.** No dia em que os treze
  forem colados, nenhuma linha de código muda — a escada de ontem já serve os três
  estados.

- **VERIFICAÇÃO NA BANCADA, 0 falha:** `validar-pastilhas` **189 afirmações** (era
  139) em 13 itens, um processo cada, 8 delas vindas da faixa medida na F1;
  `validar-banco` APROVADO com 23 materiais; `cobertura` 128; `teste-casca` 546;
  `teste-f2` 87; `teste-f1` 72; `teste-loja`, `teste-leads` e `teste-atelie`
  aprovados; `prestacao-rejunte` 5 sobre 720 estados; `php -l` em tudo.
  **MUTAÇÕES:** pastilhas **14 de 14** (12 no banco e as 2 novas no código), 0
  inertes; cobertura **14 de 14**, 9 que só a varredura vê; f1 **27 de 27** e f2
  **26 de 26**, 0 inertes nas duas — as antigas rodadas inteiras para provar que
  nenhuma morreu com o banco maior. **NAVEGADOR:** 63 medições em 9 páginas × 6
  larguras, 0 px de rolagem, console limpo, e a passada com o JavaScript
  **desligado** (portão 22.8) inteira.

- **As baterias que esta execução NÃO rodou, ditas pelo nome:** prestação, árvore,
  loja, leads, ateliê, rejunte, voz-e-cabeça e ga4. Elas medem superfícies que este
  bloco não tocou, e a de prestação sozinha passa de vinte minutos (720 estados por
  mutação). Ficam para quem mexer naquelas superfícies. Dizer quais é o mínimo:
  "rodei as mutações" sem a lista é a mesma promessa vazia que o número digitado.

- **NO AR às 17h47Z, em DOIS disparos**, e o primeiro é o caso que a seção 4
  documenta: às 17h42Z o Sync leu um manifest ainda na revisão 23 **enquanto já
  baixava o banco novo** e recusou com `"materiais-pastilhas: sha256 divergente —
  não aplicado"`. A trava fez o que devia; o segundo disparo aplicou. `/status` na
  **revisão 24**, igual à do manifest. `conferir-no-ar` **351 afirmações, 0 falha**,
  com a prestação de contas do banco medida no HTML SERVIDO: a página do Guia serve
  **"23 itens de fabricante, sendo 5 colas, 5 rejuntes e 13 pastilhas, e 13 deles
  ainda esperam link"** — total batendo com a soma dos arquivos do repositório,
  parcelas somando o total que a própria frase publica, e toda categoria com arquivo
  de banco nomeada.

- **ABERTO E NOMEADO:** (a) os 13 `url_busca` das pastilhas, que dependem da sessão
  do painel da Shopee; (b) `url_busca_produto` em 10 de 10 itens com busca (25.4-b)
  — a URL crua se perdeu e não se recupera sem clicar; (c) **1×1 continua com ZERO**
  e é o tamanho de 7 das 12 linhas da tabela pré-renderizada da F1 — não existe em
  catálogo de fabricante, só em armarinho e marketplace vendido a peso, e é a
  pendência mais cara da categoria; (d) **1,5×1,5 aparece pela primeira vez no
  relatório e sai com ZERO**, porque o único item daquele lado é de nível 5; (e)
  peças por placa segue null nos 13, agora com 9 de 13 sem divisão inteira; (f) a
  ilha não tem peça publicada, então ficha, formulário no ar e feed do Merchant
  Center continuam esperando a artesã; (g) `contato@clubedomosaico.com.br` ainda não
  existe como caixa. Pauta da seção 17: `pauta.md` ainda não existe — 0 escritos, 0
  na fila, 0 recusados.

- **PRÓXIMO, com ordem e motivo:** (1) **a vitrine de pastilha da F1**, que agora não
  tem mais nada na frente e ficou mais barata do que estava —
  `cdm_f1_pastilha_sem_banco_html()` ainda diz "ainda não temos as pastilhas no
  nosso banco", o 2×2 e o 2,5×2,5 têm os 3 elegíveis da 14.3 para servir, a escada
  de compra já está pronta, e a faixa por onde ela vai filtrar agora é **medida** em
  vez de digitada; falta decidir o que a tela diz nos três tamanhos que continuam em
  zero e nos 6 itens cujo lado o seletor não oferece, que é a pendência nova; (2) a
  categoria **cola**, que é a faixa mais descoberta da ilha (45 estados varridos, 0
  com o mínimo, teto de 2 elegíveis); (3) os 13 `url_busca`, no minuto em que houver
  sessão — é copiar e colar no banco, sem uma linha de código.

---

## 13/09/2026, 19h17–20hZ — A VITRINE DE PASTILHA DA F1 (f1 1.2.0, manifest revisão 25)

**Terceira ilha tentada nesta execução, de novo, e de novo é a seção 1 funcionando.** A
aquametria foi reservada às 19h18Z e a robometria às 19h16Z por outras duas execuções — o meu
push da reserva da aquametria foi recusado por cerca de um minuto, e o da robometria também.
O passo 5 manda voltar ao passo 2 e escolher a próxima da ordem; sem force push, sem atropelo.
Antes de escolher, conferi os três `PROMPT.md`: **nenhuma ilha tem despacho aberto para a
Fundação** (a 18.1 não se aplicou), então valeu a rotação normal da seção 1.

**O bloco é o item (1) que a execução anterior desta ilha deixou escrito**, e ele não tinha
mais nada na frente: *"a vitrine de pastilha da F1 — `cdm_f1_pastilha_sem_banco_html()` ainda
diz 'ainda não temos as pastilhas no nosso banco'"*.

### O defeito era de OMISSÃO, e ele tinha data

A frase nasceu verdadeira em 11/09/2026. Em **12/09** o bloco 3d gravou dez pastilhas; em
**13/09** entraram outras três. O arquivo está com `publicar: true` desde 12/09, a casca lê
ele em `cdm_casca_numeros()` e o cartão do Guia publica a contagem — e **nenhuma linha de
código da F1 abria o banco**. Dado no banco e tela sem leitor é o mesmo defeito que a F2
tinha com o `url_busca` até 13/09 de manhã; aqui era mais caro, porque esta é a ferramenta
cuja pergunta **é** "quantas pastilhas comprar", e ela respondia sem ter o que vender.

### O que decide uma pastilha não é o que decide uma cola

Primeira coisa que o código novo declara, e é a cicatriz da "categoria nova herda a régua da
antiga em silêncio" (seção 8), que esta ilha já pagou quando o primeiro rejunte fez as 18
células da cola falharem de uma vez. A cola se escolhe por base × ambiente; o rejunte, pela
folga. **A pastilha entrou no banco pela GEOMETRIA** — o próprio arquivo diz isso e diz por
quê: o fabricante não nomeia substrato nem ambiente na ficha dela. Então a elegibilidade tem
três travas, **nesta ordem**, e a ordem é o que faz cada frase de recusa poder ser verdadeira:

1. **o LADO** (o que a pessoa escolheu, ou digitou no caquinho irregular);
2. **o FORMATO** — o seletor oferece pastilha quadrada e o banco tem um strip retangular de
   1,2 cm. Quem cai aqui já passou pelo lado, então "o lado é o mesmo" não é suposição;
3. **a FONTE** — nível <= 3 pela escada do esquema. É por isso que **1,5 cm sai com ZERO
   tendo um item**: a causa é a fonte (distribuidor), não o tamanho, e a tela diz qual das duas.

**Prestação de contas (seção 7):** as quatro listas são disjuntas e somam o banco inteiro,
contado do arquivo. Todo item aparece **uma vez** — no cartão que o recomenda ou numa linha
que diz por que ele não está. Uma frase por causa, cada uma nomeando quem caiu por ela.

### A PENDÊNCIA DO SELETOR FECHOU POR UM TERCEIRO CAMINHO — e o número dela estava errado

O banco abriu em 13/09 a pendência `pastilha-tamanho-fora-do-seletor-da-f1` dizendo **6 dos
13**. São **5**. Ela listava o AF1500 de 1,5 cm entre os lados que o seletor não tem, porque
foi escrita a partir da frase "a F1 oferece quatro tamanhos — 1x1, 2x2, 2,5x2,5 e a tessela
irregular". **A F1 oferece cinco, e o quinto é justamente 1,5 cm** — foi esse o defeito que
`ferramentas/tamanhos-da-f1.php` achou na régua de manhã, e **a prosa da pendência herdou a
mesma lista vencida no mesmo dia**. Lista digitada envelhece calada em qualquer arquivo,
inclusive num que descreve o problema. Os cinco são os três K de 3,0 cm, o ST5102 de 1,2 cm e
o IC02 de 2,3 cm, contados do cruzamento do banco com `cdm_f1_pastilhas_disponiveis()`.

A pendência propunha duas saídas e **nenhuma das duas foi tomada**: opção nova no seletor
prometeria cobertura da 14.3 que não existe, e servir tamanho aproximado seria recomendar 3,0
a quem pediu 2,5 com a conta de 2,5. Havia um terceiro caminho, e ele **já estava construído**:
o campo do **caquinho irregular** aceita qualquer lado de 0,3 a 10 cm e é o único da
ferramenta em que o lado é digitado. A vitrine casa pelo lado em milímetros, então quem digita
3 recebe os três K de 3,0 cm com a conta do próprio lado dele. A tela nomeia os lados que o
seletor não lista e manda a pessoa para lá.

### O CARTÃO FALA EM PLACA, E ISSO É ESCOLHA DECLARADA

Converter "N pastilhas" em "M placas" exigiria quantas pastilhas vêm na placa, e **nenhum dos
treze fabricantes publica**: a divisão ingênua não fecha em 9 dos 13 e, nos outros 4, fecha
exigindo folga zero — placa que não se rejunta. Área, sim, se converte sem supor nada: a
placa cobre o próprio tamanho, seja qual for o arranjo das peças dentro dela. Então o cartão
diz quantas **placas** a peça pede, com a sobra escolhida dentro e arredondando para cima
pelo mesmo motivo da contagem de peças — e a página diz, na cara, que a peça ela não converte.

### A ESCADA DA SEÇÃO 25 FOI CHAMADA, NÃO COPIADA

`cdm_f2_compra_html()` nasceu em 13/09 dizendo, no próprio comentário, que a vitrine de
pastilha da F1 a chamaria em vez de reescrevê-la. Foi o que aconteceu. Hoje os treze caem no
**terceiro** degrau — sem ficha e sem piso —, e isso é defeito declarado da 19.1, não estado
de espera: o cartão reserva o lugar, e o número está contado no banco (`itens_sem_piso: 13`).

### A TABELA PRÉ-RENDERIZADA EXISTE POR UM MOTIVO ARITMÉTICO

O estado-âncora desta página é caquinho de **1 cm**, e 1 cm tem **zero** elegível. Sem a
tabela do banco inteiro, a única URL indexada desta ferramenta — a sem parâmetro, a que o
Google e as IAs leem — **não citaria um único produto do nosso catálogo de pastilha**. A
vitrine responde a quem escolheu um lado; a tabela responde a quem só chegou. Treze linhas,
cada item uma vez, com uma coluna "está no formulário?" que publica a cobertura da 14.3 item
por item, em vez de a deixar só na bancada.

E a frase que explica o zero de 1 cm — "não aparece em catálogo de fabricante nenhum; quem
vende é armarinho e marketplace, a peso ou por peça solta" — **só sai no lado de 1 cm e só
quando ele está vazio**. Ela é verdadeira hoje, e é isso que a tornava perigosa.

### A BANCADA, E O QUE ELA ACHOU NELA MESMA

`teste-f1.php` foi de **72 para 182 afirmações**, 0 falha. A régua da classificação é escrita
**neste arquivo**, em PHP, lendo `dados/materiais-pastilhas.json` do disco — não chama nenhuma
função do snippet. A grade varre os cinco tamanhos do seletor, os três lados que só o caquinho
irregular alcança e um lado que não existe em ninguém, um processo por estado.

`mutacoes-f1.py` foi de 27 para **40 mutações, 40 reprovadas, 0 inertes**. A primeira rodada
teve **três que passaram, e as três eram resultado**:

1. **"vão maior que a moldura passa e a área fica negativa"** reprovava desde 12/09 e passou a
   escapar **por causa deste bloco**: a afirmação procurava "não fecha" no corpo INTEIRO, e a
   camada de prova nova passou a dizer que a divisão do lado da placa "não fecha" em quase
   todos os itens. A agulha foi encontrada numa seção que nada tem a ver com a recusa — o mesmo
   defeito que a seção 8 registra como "a conferência achava o texto dentro do próprio
   JSON-LD". Ela passou a medir **no bloco da resposta**. E a afirmação vizinha tinha um furo
   mais antigo: `-\d+ cm²` nunca casaria com **"-1.100 cm²"**, que é exatamente o que a página
   serve quando a guarda cai. Só pegava área negativa de três dígitos.
2. **"as placas esquecem a sobra"** passou porque a grade não pisava na borda: no vaso de
   15 × 20 a sobra de 10% não muda o número de placas, e o `ceil` engole a diferença. Nasceu a
   seção **4c**, com uma peça de 44,5 × 40 cm escolhida para a sobra atravessar o degrau (2 / 2
   / 3 placas em 0 / 10 / 20%) — e uma afirmação que cobra que os degraus sejam **diferentes**,
   senão a peça escolhida não mediria a sobra.
3. **"a frase do 1 cm passa a sair sempre"** passou porque nada media o ESCOPO dela. Ela é
   verdadeira no lado de 1 cm e seria uma afirmação sobre um mercado que ninguém olhou em
   qualquer outro lado. Agora a régua cobra que ela saia **se e somente se** o lado pedido é
   10 mm e ele está vazio.

**TRÊS MUNDOS NOVOS no `render-para-teste.php`**, e cada um existe porque o banco de hoje não
consegue produzir o caso — "todo caso que o ESQUEMA permite e o banco ainda não tem é um caso
que a régua precisa tratar hoje" (seção 8):

- **`com_piso=1`** escreve `url_busca` em quem não tem. Sem ele, a mutação que faz o cartão de
  pastilha **reimplementar** a escada em vez de chamar `cdm_f2_compra_html()` produz uma tela
  **idêntica byte a byte** — os treze estão sem piso, então os dois caminhos caem no terceiro
  degrau. A cópia só mentiria no dia em que o Raphael colasse os links, com um portão verde ao
  lado. Essa mutação reprova **só** neste mundo.
- **`strip_fraco=1`** rebaixa a fonte do único item não quadrado para nível 5, fazendo-o cair
  pelas DUAS travas. É o único jeito de provar a ORDEM declarada: com um item por balde,
  qualquer ordem produz a mesma tela.
- **`um_de_1cm=1`** clona um item para o lado de 1 cm e exige que a frase do mercado
  desapareça.

**Navegador:** 83 medições em 13 páginas × 6 larguras (360, 390, 781, 782, 783, 1200), **0 px
de rolagem lateral** nos três estados novos da F1, console limpo, contraste de 12,97:1 a
21:1, e a passada com o **JavaScript desligado** inteira (portão 22.8) — a vitrine é servida
pelo servidor e não tem uma linha de decisão em JavaScript.

**Outras baterias rodadas inteiras, 0 falha:** casca 546, f2 87, loja 147, leads 211, atelie
aprovado, cobertura 128, validar-pastilhas 189, validar-banco aprovado, `php -l` em tudo. As
que NÃO rodaram, e vale dizer quais: prestação de rejunte (720 estados, passa de vinte
minutos), árvore, rejunte, voz-e-cabeça, ga4 e as mutações de pastilhas, cobertura, f2, loja,
atelie e leads — elas medem superfícies que este bloco não tocou.

**NO AR às 19h54Z, em UM disparo.** `/status` na revisão **25**, igual à do manifest, 10
aplicados. `conferir-no-ar.py` foi de 351 para **365 afirmações, 0 falha**, medidas no HTML
SERVIDO depois do Sync — a tabela do banco com 13 linhas e os treze códigos, o estado-âncora
dizendo que não tem 1 cm com a causa, o estado de 2 cm com três cartões nomeados e o lugar do
link reservado nos três, e o caquinho irregular de 3 cm alcançando os três K que o seletor não
lista. A régua dele também é própria: os treze códigos estão escritos literais no arquivo.

**Um detalhe do próprio commit, para não parecer descuido:** o nome da pendência entre acentos
graves foi comido pelo shell na mensagem de commit, e a linha saiu "fecha a pendencia  —".
Não há force push nesta fábrica (seção 3), então a mensagem fica como está; o nome é
`pastilha-tamanho-fora-do-seletor-da-f1` e a história inteira está acima.

**ABERTO E NOMEADO, ao fim deste bloco:** (a) os **13** `url_busca` das pastilhas, que dependem
da sessão logada do painel de afiliado da Shopee — no dia em que forem colados, **nenhuma linha
de código muda**, e o `com_piso=1` já prova que a tela sabe subir o degrau; (b) `url_busca_produto`
em 10 de 10 itens com busca (25.4-b); (c) **1x1 continua com ZERO elegível** e é o tamanho de 7
das 12 linhas da tabela pré-renderizada da F1 — agora a página diz isso na cara, mas o buraco
é o mesmo e é o mais caro da categoria; (d) 1,5x1,5 sai com zero por FONTE, não por tamanho;
(e) peças por placa segue null nos 13, e é a pendência que faz o cartão falar em placa; (f) a
ilha não tem peça publicada, então ficha, formulário no ar e feed do Merchant Center continuam
esperando a artesã; (g) contato@clubedomosaico.com.br ainda não existe como caixa.

**Pauta da seção 17:** `pauta.md` ainda não existe — 0 escritos, 0 na fila, 0 recusados.

**PRÓXIMO, com ordem e motivo:** (1) **a categoria COLA**, que é a faixa mais descoberta da
ilha — 45 estados varridos, **0 com o mínimo** da 14.3, teto de 2 elegíveis; é a única
categoria em que a ferramenta responde e o banco não tem o que vender, e agora não tem mais
nada na frente. (2) **A ORDEM DAS DUAS VITRINES na F1**: hoje "Qual rejunte cabe nessa folga"
vem antes de "E onde comprar a pastilha", ordem herdada de quando o bloco da pastilha era uma
frase de espera. O H1 da página nomeia a pastilha primeiro e a resposta também; mover é
decisão de desenho e merece bloco próprio, não um `swap` no meio de outro. (3) **1x1 de
fabricante**, que é a pendência mais cara da categoria pastilha — a busca alcança os domínios,
o egresso é que não. (4) os 13 `url_busca`, no minuto em que houver sessão: é copiar e colar.

### O ACHADO QUE NÃO ERA DESTE BLOCO: o cabeçalho de estado não é YAML válido

Ao validar o próprio cabeçalho antes de fechar (porque ele ficou grande e eu quis ter certeza),
descobri que **a seção 2 do contrato manda o cabeçalho ser YAML e nada nunca conferiu que ele
PARSEIA**. Passando os três `ESTADO.md` do arquipélago por `yaml.safe_load` às 19h58Z:
**dois dos três estavam quebrados**. A causa é a mesma e nasceu do crescimento saudável do
arquivo — o `bloco_atual` passou de `"4c"` para prosa de milhares de caracteres entre aspas
duplas, e aspas duplas dentro de um escalar de aspas duplas derrubam o documento; uma barra
invertida solta também, porque `\d` é escape desconhecido em YAML de aspas duplas.

- **clubedomosaico**: estava inválido e foi consertado no mesmo commit (aspas internas viraram
  simples, e a regex citada saiu por extenso).
- **aquametria**: inválido, na coluna 1910 do `bloco_atual`. Reservada por outra execução às
  19h18Z, e a seção 3 proíbe editar ilha que não se reservou → virou **despacho** em
  `dados/despachos.md`.
- **robometria**: válido.

Ninguém tinha visto porque quem lê o cabeçalho hoje é a Fundação, com `grep` e com o olho, e as
duas coisas atravessam YAML quebrado sem reclamar. **Cabeçalho que só o olho lê é cabeçalho sem
portão.** A metade que vale para toda ilha foi escrita onde regra nova mora, uma vez: a
**seção 2 do `ARQUIPELAGO.md`**, com o comando de uma linha e a convenção de aspas simples.

13/09/2026 21:19Z — BLOCO 3e ENTREGUE: A CATEGORIA COLA GANHA OS DOIS PRODUTOS DAS FAIXAS DE ZERO, E A F2 APRENDE A CONDIÇÃO DE SUPERFÍCIE (regra 6)

**A ilha desta execução foi a terceira tentativa.** A robometria foi reservada às
21h16Z por outra execução — o push da minha reserva foi recusado por cerca de um
minuto, o passo 5 da seção 1 manda voltar ao passo 2, e nenhum force push
aconteceu. Antes de escolher, os três `PROMPT.md` foram lidos: **nenhuma ilha
tinha despacho aberto para a Fundação**, então a 18.1 não se aplicou e valeu a
rotação da seção 1. A clubedomosaico era a de `ultima_execucao` mais antiga entre
as livres (19h17Z), com prioridade 1.

**O QUE ESTE BLOCO FOI BUSCAR, e estava escrito no `ESTADO.md` desde as 19h17Z:**
a categoria COLA era a faixa mais descoberta da ilha. O censo da seção 14.3 media
**45 estados, 0 com o mínimo de 3 elegíveis, teto de 2**. Era a única categoria em
que a ferramenta responde e o banco não tinha o que vender.

## A rede, medida antes de trabalhar (seção 20.2)

`clubedomosaico.com.br` e o `/status` em 200. O egresso a fabricante segue
fechado e foi **remedido em duas passadas** antes de ser respeitado, como manda a
seção 4: `quartzolit.weber`, `tekbond.com.br`, `cascola.com.br`, `henkel.com.br`,
`bra.sika.com` e `brascola.com.br` responderam `000` nas duas, com o domínio da
ilha em 200 como controle na mesma janela. O WebFetch devolveu `EGRESS_BLOCKED`
para o mesmo domínio. **O canal que sobrou é exatamente o que a escada de fontes
do esquema chama de nível 2 e 3: busca restrita ao domínio do fabricante, sem
abrir o PDF** — e foi por ele que os dois produtos entraram.

## Os dois produtos, e por que cada um fecha uma faixa

**Tekbond Silicone Acético Maxx (BRSA005)** — o primeiro produto do banco que
pode ser **recomendado em contato permanente com água**. Até hoje essa faixa
tinha zero elegíveis nas nove bases, e a única declaração de colagem submersa da
ilha era press release de 2018 (`loctite-durepoxi`, nível 4, abaixo do mínimo de
3). A declaração de aquário e piscina está na página de produto do fabricante,
nível 3, e cumpre a regra 4 (ambiente crítico exige declaração explícita).

**Cascola Adesivo de Montagem PL500 Interior** — o primeiro indicado **sobre
plástico**. O único que falava de plástico dizia "certos tipos de plástico", que
não nomeia tipo nenhum e por isso nunca virou indicação; aqui o fabricante lista
"plásticos" sem qualificador.

**O QUE FOI RECUSADO DE PROPÓSITO, nos dois:**

- No Maxx, **vidro NÃO entrou**. É um silicone de aquário e aquário é de vidro, e
  a tentação de traduzir "fabricação e reparo de aquários" em base VIDRO é a
  heurística por vizinhança que a seção 8 proíbe. "Aquários" é aplicação e entra
  como AMBIENTE, que é o que ela mede. As outras oito bases seguem descobertas
  dentro da água, e a página diz isso.
- No PL500, a frase *"ideal para adesão de rodapés, peças decorativas, azulejos,
  ladrilhos, molduras, canaletas, cantoneiras, maquetes, mosaicos"* **não entrou
  em `indicado_para`**, embora contenha "azulejos", que o mapa traduz como BASE.
  É a lista do que se COLA, nunca a do que se cola SOBRE — o mesmo erro que este
  banco já pegou na cimentcola AC-II. **"Mosaicos" está escrito lá pelo próprio
  fabricante e mesmo assim não virou declaração de substrato: virou citação.**

## A regra 6, e por que ela precisou existir

O PL500 declara **"ao menos uma das superfícies deve ser porosa, já que o produto
seca por evaporação da água"**. Isso não é base e não é ambiente: é o **PAR de
superfícies coladas**. Sem tratá-la, a página mandaria colar pastilha de vidro em
vaso de plástico com um adesivo que não teria por onde curar — recomendar em
primeiro lugar um produto que a própria página diz não servir, que a seção 7
chama de defeito GRAVE.

Nasce a **regra 6 do esquema (versão 3)**: a primeira régua de cola que olha o
CAQUINHO. A entrada existia desde a F2 1.0.0 e nenhuma régua de cola a lia — o
mesmo defeito que a F1 tinha com o banco de pastilhas e a F2 com o `url_busca`.

**TRÊS DECISÕES DECLARADAS NO CÓDIGO:**

1. **A ordem.** A condição roda DEPOIS das cinco e ANTES da ordenação por score.
   Rodar depois da ordenação deixaria célula sem topo com elegíveis na mão: em
   `vidro` + `caquinho de espelho` o produto com condição é o PRIMEIRO colocado,
   e quem sobe no lugar dele são os dois silicones que estavam abaixo. É uma das
   cinco âncoras escritas à mão no esquema.
2. **A causa tem grupo próprio.** Quem cai pela condição não vai para o balde do
   silêncio. Não é proibição (o fabricante não proíbe) e não é silêncio (ele
   falou, e falou desta superfície). Misturar seria a mistura de causas que a
   seção 7 proíbe desde 12/09/2026, escrita nesta mesma ilha.
3. **A atribuição sai dividida ao meio (seção 26.3).** A **condição** é do
   fabricante; a classificação de **quais superfícies são porosas** é da ilha. A
   página escreve as duas metades em orações separadas — *"a Henkel escreve ao
   menos uma das superfícies deve ser porosa; quem diz que pastilha de cerâmica é
   a superfície porosa deste caso somos nós, não ela"* — e o portão mede a
   separação.

**A lista mora no esquema, nunca na régua (seção 26.2)**, com as duas direções
cobradas: a união de porosas e não porosas tem de ser IGUAL ao vocabulário, e as
duas listas disjuntas. A direção da dúvida está escrita: **na dúvida, NÃO
porosa** — cerâmica esmaltada entra como não porosa mesmo sabendo que o biscoito
por baixo do esmalte é poroso, porque quem escolhe "cerâmica ou porcelana" na F2
está colando sobre a face esmaltada.

## O ACHADO QUE QUASE FOI COMMITADO, e foi um portão que o pegou

A ficha técnica BRSA005 foi **localizada e não lida** (o PDF não abre desta
nuvem). Ela tinha sido gravada dentro de `fontes`, "para a próxima execução saber
onde ir", com o nível 2 dela. **O nível de um material é o MELHOR dos níveis das
fontes**, então aquela linha promoveu o produto inteiro de 3 para 2 sem que uma
declaração dele viesse da ficha — e a linha de prova da tela passou a atribuir a
declaração a um documento que ninguém abriu. Quem viu foi o portão de acentuação
da F2, que reprovou a palavra `tecnica` chegando à tela vinda do campo `tipo`
daquela fonte.

Seção 10 do contrato: **o nível é o do elo MAIS FRACO, e inflar o próprio nível
de fonte é o defeito mais caro numa fábrica que vende procedência.** O endereço
ficou, em campo próprio — `fonte_localizada_nao_lida` —, e nasceu a trava:
`fontes` é o que SUSTENTA o registro, e fonte que declara não sustentar campo
nenhum é recusada pelo validador com o motivo escrito.

## O OUTRO ACHADO, de carona, e ele estava numa régua

O validador cobrava etiqueta do Mercado Livre no formato `clubedomosaico-<código>`
— **uma etiqueta IMPOSSÍVEL de criar**. A seção 7 do `ARQUIPELAGO.md` foi
corrigida em 13/09/2026 MEDINDO o painel: só minúsculas e números, sem hífen, no
máximo 30 caracteres. A régua ficou para trás e aprovava os **23 registros** do
banco que carregavam a forma com hífen. Portão verde sobre um valor que não
existe do outro lado. Os 23 registros e a régua foram corrigidos no mesmo commit.

## O DEFEITO QUE ESTE BLOCO CRIOU E CONSERTOU NO AR: prosa que envelhece calada

A seção "Duas coisas que a gente ainda não responde" era **duas frases escritas à
mão**, e as duas eram exatas no dia em que nasceram. Os dois produtos as fizeram
mentir no mesmo dia — **no ar, em voz de confissão**, que é pior, porque frase de
honestidade é a última de que alguém desconfia. O conserto não foi reescrever a
prosa: a seção passou a ser **CONTADA a cada requisição**, varrendo a entrada
inteira (base × lugar × caquinho) e publicando *"esta página responde 270
combinações; em 68 delas a gente ainda não tem cola para indicar"*.

**Mais três listas digitadas caíram no mesmo bloco**, e a quarta foi pega pelo
portão que eu mesmo tinha acabado de escrever: a resposta do FAQ e a frase
*"trocando por X, ele voltaria a servir"* traziam os nomes dos caquinhos porosos
escritos à mão. Essa última é a única frase da página que diz à pessoa **o que
fazer para a peça não descolar**, e digitada ela erraria do jeito caro. As duas
passaram a sair das mesmas listas que a régua usa.

**A tabela pré-renderizada ganhou a coluna da condição.** Sem ela, a linha
"plástico, dentro de casa: use Cascola PL500" sairia servida no HTML como se
valesse sempre — e ela só vale com caquinho poroso. É a metade que um modelo de
linguagem lê sem preencher formulário, e é onde a afirmação sem escopo custa mais.

**Na casca, três números entraram na via viva**: `celulas_matriz`,
`celulas_com_saida` e `celulas_sem_saida` eram os únicos do instantâneo que
nenhuma linha recontava, e a página de metodologia — cujo único produto é o rigor
— passou a publicar que a ilha tinha duas combinações sem saída num dia em que
ela não tinha nenhuma. A frase também ganhou o ESCOPO do que ela mediu, e aponta
para a ferramenta, que tem a conta com as três dimensões.

## A verificação, em números

**Banco:** `validar-banco.py` APROVADO — 25 materiais, 18 células da F2
recomputadas, 9 do rejunte, **54 pares da regra 6 com 5 âncoras ponta a ponta**.
As 18 células da matriz foram **derivadas à mão** das declarações dos dois
produtos ANTES de o validador rodar; as 32 divergências que ele acusou bateram
uma a uma com a derivação.

**Bancada, 0 falha:** teste-f2 de 87 para **102 afirmações**, com varredura da
entrada INTEIRA — 270 estados, um processo cada —, incluindo a **prestação de
contas da cola** que a ilha nunca teve: 1.890 nomeações (7 colas contadas do
arquivo × 270 respostas), cada item em exatamente UM lado. teste-casca 546,
teste-f1 182, teste-loja 147, teste-leads 211, teste-atelie, validar-pastilhas,
prestação de rejunte (540 estados da F2 e 180 da F1), `php -l` em tudo.
`conferir-cobertura.php` **353 afirmações, 0 falha**: a régua do censo e a do
snippet dão o mesmo elegível nos 270 estados de cola e nos 60 de rejunte.

**Censo da 14.3, o número deste bloco:** a cola sai de **45 estados varridos, 0
com o mínimo, teto 2** para **270 varridos, 28 com o mínimo de 3, teto 4**. Os
com zero elegíveis são 68, e é esse o número que a página publica.

**Navegador:** a bateria rodou sobre os quatro estados novos da F2, com a passada
de JavaScript desligado inteira.

**Mutações:** a bateria rodou inteira **três vezes**, e as três passadas
produziram achado. **Quatro resultados**, e os quatro valem mais que o verde:
- Uma mutação antiga **virou INERTE** quando a assinatura de `cdm_f2_fora_html()`
  ganhou a tessela. Mutação que não morde é teste verde com outro nome; foi
  reapontada.
- Uma **PASSOU**, e o motivo era meu: eu declarei o portão errado. Ela edita o
  snippet e eu mandei o validador do banco julgá-la, e o validador não lê uma
  linha de PHP. Ganhou o portão certo, e ganhou uma **gêmea do lado do Python**,
  porque duas implementações da mesma regra precisam das duas mutações.
- A trava que ela deveria ter acionado **não existia**. A afirmação que faltava —
  *"produto proibido sai no bloco da proibição, nunca no da condição"* — nasceu e
  descobriu-se **verde sem poder falhar**: o banco tem um produto com condição e
  ele não é proibido em base nenhuma. Nasceu com ela a mutação que **produz o
  mundo**, criando o par proibido-com-condição que o banco de hoje não tem.
- Na passada seguinte, **uma segunda PASSOU**: apagar a coluna da condição da
  tabela pré-renderizada deixava o portão inteiro verde. O defeito era real e o
  `conferir-no-ar.py` o pegava — **mas defeito pego pela regra VIZINHA prova que
  ALGUMA trava existe, nunca que ESTA existe**, e é por isso que cada mutação
  deste bloco declara qual portão tem de reprová-la. Enquanto a bancada não
  medisse, a tabela podia perder a coluna e só o desembarque diria. A afirmação
  nasceu, com régua própria (o literal do fabricante lido do banco em disco), e
  a mutação foi reaplicada sozinha para ver a trava reprová-la antes da passada
  final: **6 linhas da tabela indicam produto com condição, e as 6 publicam a
  condição literal.**

**Resultado final, medido depois do fechamento e corrigido aqui: 44 mutações, 44 reprovadas,
0 passaram, 0 inertes.** A entrada acima foi escrita quando a terceira passada estava em 31 de
44, e era isso que ela dizia — o número menor, que era o medido naquele minuto. A bateria
terminou em seguida, no mesmo container, e este parágrafo é a correção. **Escrever o número
menor e corrigi-lo custa um commit; escrever 44 antes de vê-lo seria a única coisa que esta
fábrica não perdoa.**

## Receita e dívida, contadas do arquivo

7 colas no banco (eram 5). **Os dois novos nascem SEM PISO**, e isso é dívida
contada, não estado de espera: a palavra-chave de busca dos dois está escrita em
`afiliado.url_busca_produto`, e o que falta é o encurtamento, que exige a sessão
logada do painel de afiliado — medido nesta execução às 21h (o
`affiliate.shopee.com.br` serve casca de JavaScript sem sessão). **No dia da
sessão são duas colagens e nenhuma linha de código muda.** A ilha vai a 25 itens
de fabricante, 15 esperando link, 15 sem piso, 22 sem imagem.

## Aberto e nomeado

- (a) **A matriz escrita à mão cobre 18 das 45 células de base × lugar.** As
  outras 27 são verificadas só pela varredura das páginas servidas, que mede a
  agregação e NÃO é régua independente de elegibilidade. Está dito dentro do
  próprio portão, em vez de escondido. O conserto é a matriz chegar a 45 — nunca
  o portão fingir que já mede o que não mede.
- (b) Os 15 `url_busca` dependem de uma sessão do painel da Shopee.
- (c) O egresso a fabricante segue fechado; a ficha BRSA005 está localizada e não
  lida, com o endereço guardado.
- (d) `1x1` de fabricante continua com zero elegível, e é o tamanho de 7 das 12
  linhas da tabela da F1.
- (e) A ilha não tem peça publicada, então ficha, formulário no ar e feed do
  Merchant Center esperam a artesã.
- (f) `contato@clubedomosaico.com.br` ainda não existe como caixa.

## UM DETALHE DO COMMIT, e desta vez ele virou regra do Arquipélago

A mensagem do commit deste bloco perdeu a palavra `fontes`: ela estava entre
crases dentro de aspas duplas, e o shell executou o que havia ali e colou a saída
vazia no lugar. A linha foi ao ar como *"saiu de \n depois que"*. **É a segunda
vez no mesmo dia e na mesma ilha** — às 19h17Z sumiu o nome de uma pendência,
pelo mesmo motivo, e a execução de então registrou o fato só aqui, no `REGISTRO`
da ilha. Registrado só aqui, o defeito repetiu.

A seção 3 proíbe force push, então as duas mensagens ficam como estão. O que
mudou é onde a lição foi escrita: **a regra nova está na seção 3 do
`ARQUIPELAGO.md`**, que é onde regra do Arquipélago mora e é lida por toda
execução de toda ilha — *crase não entra em mensagem de commit*, e a mesma
armadilha vale para `$` e `!` dentro de aspas duplas.

**PRÓXIMO, com ordem e motivo:** (1) **a matriz esperada da F2 de 18 para 45
células**, que é a independência que falta ao número que a página publica, e é o
único item aberto que este bloco criou; (2) a ordem das duas vitrines na F1, hoje
herdada de quando o bloco da pastilha era uma frase de espera; (3) `1x1` de
fabricante, a pendência mais cara da categoria pastilha; (4) os 15 `url_busca`,
no minuto em que houver sessão — e é copiar e colar.

---

# 13/09/2026, 23h18Z — A MATRIZ ESCRITA À MÃO VAI DE 18 PARA 45 CÉLULAS, E A PRIMEIRA COISA QUE ELA VÊ É UM DEFEITO NO AR

**F2 1.4.0 · esquema versão 3 · manifest revisão 27 · nenhuma URL nova, nenhuma
página criada.** Era o item (1) do PRÓXIMO da execução das 22h30Z, e o único item
aberto que aquele bloco tinha criado.

## A escolha da ilha, e ela foi a terceira tentada

Rotação da seção 1, sem despacho aberto para a Fundação em nenhum dos três
`PROMPT.md` (os três foram lidos antes de escolher, como a 18.1 manda). A
robometria era a de `ultima_execucao` mais antiga (21h16Z) e **meu push de reserva
foi recusado por cerca de um minuto** — outra execução a reservou às 23h18Z; a
aquametria caiu às 23h19Z pelo mesmo motivo. O passo 5 manda voltar ao passo 2, e
**nenhum force push aconteceu**. Sobrou a clubedomosaico, com `executando_desde:
null`, que pela **1.1** já significa que não há bloco da Fundação vivo — o git não
precisou desempatar, embora a ilha tivesse fechado bloco 6 minutos antes.

`dados/despachos.md` tem um despacho para a **FUNDAÇÃO (quem reservar a
aquametria)**: consertar o cabeçalho YAML dela. **Medido nesta execução, os três
`ESTADO.md` passam por `yaml.safe_load`** — a execução das 21h21Z da aquametria já
o cumpriu. Não é minha ilha para tocar, mas o "pronto quando" dele está satisfeito
e isso ficou escrito no despacho, com quem mediu.

## O que a dívida era, dita com o tamanho que ela tinha

A matriz `matriz_esperada_da_F2` é a **régua independente** da ferramenta: ela é
escrita à mão a partir das declarações dos fabricantes e nunca chama uma linha do
snippet, então as duas metades não erram juntas. Ela cobria **18 das 45 células**
de base × lugar. As outras 27 passavam só pela varredura das páginas servidas —
que mede a **agregação** e lê a MESMA implementação de elegibilidade dos dois
lados. Portão verde que não é régua.

**As 27 novas foram DERIVADAS À MÃO das declarações ANTES de o validador rodar uma
vez**, e a derivação ficou gravada antes da inserção. Resultado, dito com o número
que ele tem: **zero divergência** nas cinco listas das 27 — recomendados no topo,
elegíveis abaixo, proibidos, silêncio e menção com ressalva bateram produto a
produto com a recomputação. O que o validador cobrou foram **9 observações que
faltavam**, e ele estava certo: célula sem recomendação tem de dizer POR QUE, e
essa regra existia antes deste bloco.

## O ACHADO, e ele é o motivo de esta régua valer o que custa

**As 18 células antigas TODAS tinham recomendação.** Nenhuma delas era faixa
descoberta — ou seja, **a régua independente desta ilha nunca havia pisado numa
célula sem resposta**, que é justamente a metade em que a página vende honestidade
em vez de produto. Com as 45, **11 células são descobertas**, e o ramo do código
que as escreve deixou de ser código morto para o portão.

Ele estava errado, e **estava no ar**. Em quatro estados — **vidro, madeira,
alvenaria e metal em contato permanente com água** — a página servia:

> "Não temos cola para indicar em metal dentro da água. **Nenhum dos adesivos do
> nosso banco é declarado pelo próprio fabricante para esse caso** — e a gente
> prefere dizer isso a chutar o de sempre."

e, **duas seções abaixo, na mesma página**:

> "Existe menção a **Loctite Durepoxi**, mas o que sustenta isso é material de
> imprensa do fabricante, não documento de produto."

A primeira frase é **falsa**. A Henkel declara metal, alumínio, ferro, cobre e
latão E declara secar em condição submersa — as duas metades, no mesmo produto. O
que segura a recomendação é a **procedência da fonte**, que é régua NOSSA (regra
5), não o silêncio do fabricante, que seria fato dele. Trocar uma causa pela outra
é a mistura que a seção 7 do contrato proíbe — e ela é pior aqui do que em
qualquer outro lugar da página, porque está dentro da frase que o leitor recebe
como confissão de honestidade. É a mesma família do defeito que esta ilha já
consertou em 12/09 na prosa que envelhece calada, e da correção que a regra 6
obrigou em 13/09 ("o motivo não é falta de declaração").

**O conserto saiu inteiro, nas duas metades.** A frase-resposta ganhou um terceiro
ramo, e a **vitrine vazia** ganhou o dela — sem a segunda, a página consertaria a
resposta e repetiria a frase errada uma seção abaixo, em "nenhum produto do nosso
banco passa no que o fabricante declara". Defeito pego pela régua vizinha prova
que ALGUMA trava existe, nunca que ESTA existe, então cada metade tem mutação
própria.

**AS TRÊS CAUSAS DE UMA FAIXA DESCOBERTA, agora nomeadas uma a uma na tela:**
**silêncio** (ninguém declara a base — 7 células), **procedência** (alguém declara
as duas metades e a fonte é nível 4 — 4 células) e **ambiente delimitado** (o
fabricante declarou a base e delimitou o uso a outro ambiente — é o caso do
plástico fora do interno seco). O tipo do documento sai **lido do banco em disco**,
nunca digitado na frase: digitar "material de imprensa" ali mediria a frase contra
ela mesma.

## A PROVA DE QUE AS 27 CÉLULAS COMPRARAM ALGUMA COISA, medida nos dois mundos

Régua nova que só fica verde não provou nada. Nasceu a mutação **"o mapa perde a
pedra do epóxi"**, e ela é cirúrgica de propósito: tira do mapa de termos os dois
literais que o Durepoxi usa para alvenaria (*pedra* e *marmore*) e **não** os que o
Silicone Neutro usa (*pedras*, *alvenaria*). Assim o neutro continua respondendo e
o único efeito visível é o Durepoxi cair de menção com ressalva para silêncio nas
quatro células de alvenaria — **as quatro nascidas neste bloco**.

- **Com a matriz de 45:** o validador acusa **8 erros**, um par por célula.
- **Com as 18 de ontem, a mesma mutação:** validador **OK**, e `teste-f2` fecha em
  **107 afirmações, 0 falha**. O defeito passava inteiro, deixando só um AVISO de
  termo sem tradução — e aviso não reprova nada.

É a aritmética da cobertura dita sem eufemismo: **régua com buraco fica verde
exatamente dentro do buraco.**

## O que mudou na tela, além da frase

A **tabela pré-renderizada da cola foi de 18 para 45 linhas** — ela é montada a
partir da mesma matriz, e é a metade que um modelo de linguagem lê sem preencher
formulário. Cada linha continua **recomputada das declarações**, nunca lida do
campo escrito à mão ao lado dela: se o banco e a matriz se separarem, quem acusa é
o validador, e a tela nunca finge concordância copiando o esperado. Nenhuma URL
nova nasceu e nenhuma página foi criada.

## Três frases que envelheceram e foram reescritas em vez de ficarem

Prosa que descreve um problema também envelhece calada, e três arquivos diziam o
tamanho velho do buraco: o comentário do `teste-f2.php` que declarava a dívida
("cobre 18 das 45"), a docstring do `cobertura.py` que chamava a matriz de amostra,
e a da mutação do ambiente crítico ("16 das 18 células continuam certas"). As três
foram reescritas com o que se mede hoje — e a do `cobertura.py` **não** virou
"agora é dispensável": a matriz decide sobre base × ambiente e não olha o caquinho,
então a entrada da ferramenta continua tendo 270 estados e a pergunta daquela
varredura continua sendo uma contagem sobre os 270.

## A conferência no ar precisou nascer, e os 390 verdes mostram por quê

Depois do Sync, `conferir-no-ar.py` passou com **390 afirmações, 0 falha** —
**sem tocar uma linha do que mudou**. Nenhum dos casos que ela media era uma
célula SEM recomendação, então ela nunca tinha lido a frase que este bloco
consertou. É a cicatriz da robometria de 13/09 acontecendo aqui: verde que não
morde.

Nasceram **26 afirmações novas no ar**, em quatro estados e com régua escrita
literal no próprio arquivo (o nome do produto e o tipo do documento copiados da
fonte, nunca lidos do banco que monta a página): os **três** estados que
respondem por procedência (vidro, metal e alvenaria dentro da água) e o estado
**negativo**, sem o qual os outros três têm porta dos fundos — em espelho dentro
da água ninguém declarou nada, e ali a página TEM de dizer que ninguém declarou.
Sem ele, uma página que servisse a frase da procedência em toda faixa descoberta
passaria nos três primeiros. Mais a linha que conta as **45** da tabela servida,
com o 45 saindo do produto dos dois vocabulários, nunca digitado.

## A verificação, em números

- **`validar-banco`**: APROVADO — 25 materiais, **45 células da F2** (eram 18), 9
  do rejunte, 54 pares da regra 6 com 5 âncoras ponta a ponta.
- **Bancada, 0 falha:** `teste-casca` 546 · `teste-f2` **107** (eram 102, e agora
  varrendo 45 células em vez de 18) · `teste-f1` 182 · `teste-loja` 147 (72
  estados) · `teste-leads` 211 · `teste-atelie` aprovado · `teste-prestacao-rejunte`
  5 afirmações sobre 540 estados da F2 e 180 da F1 · `conferir-cobertura` 353 ·
  `validar-pastilhas` aprovado · `php -l` limpo em ferramentas e snippets.
- **Mutações:** `mutacoes-f2` de 44 para **47, com 47 reprovadas, 0 passaram e 0
  inertes** — a bateria inteira, rodada do zero sobre o estado final. As três
  novas são as deste bloco: a faixa descoberta voltando a negar a declaração, a
  vitrine vazia fazendo o mesmo uma seção abaixo, e a que só as 27 células novas
  pegam.
- **UMA PASSADA DA BATERIA FOI DESCARTADA E REFEITA, e o motivo fica escrito:**
  a primeira rodada aconteceu enquanto um `git stash` reverteu a árvore de
  trabalho por alguns segundos, para o commit de renovação da reserva. A bateria
  copia a pasta da ilha **a cada mutação**, então qualquer cópia feita naquela
  janela leu a ilha de ontem. Nenhum resultado dela foi aproveitado. Número que
  saiu de uma árvore que mudou no meio não é número medido.
- **No ar, depois do Sync:** `/status` na **revisão 27**, igual à do
  `manifest.json`, em UM disparo com 10 aplicados. `conferir-no-ar` de 390 para
  **416 afirmações, 0 falha**.

## Receita e dívida, contadas do arquivo

Nada mudou de receita neste bloco, e isso é a informação: **7 colas no banco, 25
itens de fabricante, 15 esperando link, 15 sem piso, 22 sem imagem**. Os 15
`url_busca` continuam dependendo de uma sessão do painel da Shopee — a
palavra-chave já está escrita em `afiliado.url_busca_produto` nos 15, e no dia da
sessão são 15 colagens e nenhuma linha de código. Pauta da seção 17: `pauta.md`
ainda não existe — 0 escritos, 0 na fila, 0 recusados.

## Aberto e nomeado

- (a) **A dívida que este bloco fecha era a única que o bloco anterior tinha
  criado**, e ele não criou nenhuma no lugar dela. O que sobra da família é a
  metade do **rejunte**: `matriz_esperada_do_rejunte` tem 9 células de junta ×
  ambiente e continua sendo **amostra de borda**, escolhida para pisar nas faixas
  declaradas. É amostra de propósito e não é o mesmo caso da cola — lá a grade
  inteira é finita e pequena (45), aqui a junta é contínua.
- (b) Os 15 `url_busca` dependem de uma sessão do painel da Shopee.
- (c) O egresso a fabricante segue fechado; a ficha BRSA005 segue localizada e não
  lida, com o endereço guardado em `fonte_localizada_nao_lida`.
- (d) `1x1` de fabricante segue com zero elegível, e é o tamanho de 7 das 12
  linhas da tabela da F1.
- (e) A ilha não tem peça publicada, então ficha, formulário no ar e feed do
  Merchant Center esperam a artesã.
- (f) `contato@clubedomosaico.com.br` ainda não existe como caixa.

**PRÓXIMO, com ordem e motivo:** (1) **a ordem das duas vitrines na F1**, hoje
herdada de quando o bloco da pastilha era uma frase de espera — é o item mais
antigo da fila e o único que mexe em como a página apresenta produto; (2) **`1x1`
de fabricante**, a pendência mais cara da categoria pastilha, e a que sozinha
muda 7 das 12 linhas da tabela da F1; (3) **a matriz do rejunte de amostra para
grade**, se e quando a junta virar um vocabulário fechado — hoje ela é contínua e
a amostra de borda é a escolha certa, então isto é pergunta antes de bloco; (4)
os 15 `url_busca`, no minuto em que houver sessão — e é copiar e colar.

---

# 14/09/2026, 11h18Z — O 404 DEPOIS DE PUBLICAR NÃO ERA REGRA DE REESCRITA: ERA UM NOME QUE JÁ TINHA DONO

**Despacho do Raphael de 14/09, os quatro itens, e é o primeiro despacho desta
fábrica escrito a partir do que uma PESSOA encontrou usando o que ela construiu.**
A mãe dele recebeu o e-mail, criou a senha, entrou e cadastrou a primeira peça do
Arquipélago — "Quadro flores do campo", quatro fotos, R$ 500, pronta entrega. O que
vem abaixo é o que ela encontrou no caminho.

**Ilha escolhida pela 18.1, não pela rotação.** A clubedomosaico tinha o despacho do
Raphael mais recente e aberto no topo do `PROMPT.md`; a aquametria e a robometria
foram lidas antes de escolher e não tinham despacho aberto para a Fundação (o item
1 do de 10/09 da robometria é metade humana, no Search Console, e não é nossa). As
outras duas execuções da mesma janela registraram nos próprios commits que
perderam a corrida por esta ilha; nenhum force push aconteceu, dos dois lados.

## ITEM 1 — a causa não era a que o despacho supôs, e ele mandava confirmar

O despacho escreveu a hipótese e a marcou como hipótese: regras de reescrita do
CPT `peca` não descarregadas. **Medido antes de uma linha mudar, às 11h19Z:**
`/loja/quadro-flores-do-campo/` — a peça que ela publicou — responde **200**. A
regra de reescrita está de pé e nasce sozinha desde a Loja 1.0.0.

O que estava errado era **o nome de um parâmetro**. O painel carregava o id da peça
na URL como `peca`, e `peca` é o nome do TIPO DE CONTEÚDO, registrado com
`query_var` true — ou seja, uma variável PÚBLICA do WordPress. Para o núcleo,
`/atelie/?peca=24` não é "o painel com a peça 24": é "me dê a peça de slug 24", que
não existe, e o tema serve o 404 dele. As quatro medições, no ar, antes do
conserto:

| endereço | resposta |
|---|---|
| `/atelie/` | 200 |
| `/atelie/?aviso=publicada` | 200 |
| `/atelie/?peca=24` | **404** |
| `/atelie/?estado=editar&peca=24` | **404** |
| `/atelie/?estado=editar&cdm_peca=24` | 200 |

E a confirmação que fecha a frase dele: o corpo daquele 404 serve
`themes/twentytwentyfive/assets/images/404-image.webp`, com `alt="Pequena árvore
totara no topo acima de Long Point"`. **É a foto em preto e branco que ele viu.**

**Isto atingia mais que o publicar, e o despacho não sabia.** Seis voltas do painel
carregam o id — publicou, salvou rascunho, pausou, faltou um campo, atualizou fotos
— mais o link "Editar" da lista. **As sete caíam no mesmo 404.** Publicar era só o
caminho em que ela chegou primeiro.

**O conserto é o nome:** o parâmetro passou a ser `cdm_peca`, o mesmo prefixo que os
campos do POST deste painel já usam. Nenhum filtro tirando variável do núcleo no meio
do caminho — a colisão se resolve não colidindo. E como isso é uma regra que ninguém
enxerga lendo a linha (`'peca' => $id` parece certo), ela virou **portão**:
`teste-atelie.php` varre o snippet, extrai toda chave literal passada a
`cdm_atelie_url()`, resolve a constante do parâmetro de peça, e compara a lista
inteira com as variáveis públicas do WordPress — escritas à mão no teste, copiadas
de `WP::$public_query_vars`, mais o tipo e as duas taxonomias desta ilha. Quem
escrever uma chamada nova amanhã cai no portão sem precisar lembrar dele.

**A segunda metade do item 1**, que é o que ela devia ver no lugar do 404: a volta
para `/atelie/` já era PRG desde a 1.0.0 e continua sendo, agora com **faixa de
"Peça publicada!"**, botão **"Ver no site"** e botão **"Cadastrar outra peça"**. O
"Ver no site" **não é incondicional**: só nasce se a peça existe, é dela, está
PUBLICADA de verdade e tem endereço — a trava do núcleo devolve ao rascunho a peça
que não cumpre a regra de qualidade, então "publiquei" e "está no ar" são duas
coisas, e um botão que promete o site e cai num 404 seria o mesmo defeito, dentro
da tela que o conserta.

## ITEM 2 — "o que seria 'escolha'? Não tem nada"

Duas coisas erradas na mesma linha, e são independentes. **A palavra:** "Escolha"
nomeia uma opção que não existe; lida por quem não sabe o que é uma lista, é um item
como os outros. **O estado:** era `value=""` selecionável e inicial, então dava para
voltar a ela. Agora a primeira linha de toda lista de escolha do painel é
`<option value="" disabled hidden selected>Selecione…</option>` — instrução, não
item —, escrita por **uma função só**, porque foi exatamente dois lugares
escrevendo a mesma linha à mão que deixou "Escolha" sobreviver nos dois.

**A trava.** As duas listas que ligam a peça ao site — coleção e técnica — ganharam
`required`, e o botão **"Salvar e terminar depois" ganhou `formnovalidate`**: sem
essa palavra, o `required` transformaria guardar rascunho em refém de uma lista e
ela perderia o texto que já tinha escrito (decisão 5 do snippet). A frase que
aparece é do painel e não do navegador — "Escolha a técnica que você usou nesta
peça." —, trocada por `setCustomValidity`; com o JavaScript desligado sobra a do
navegador, que é seca mas trava do mesmo jeito, e travar é o que protege a peça
órfã. No servidor a régua já existia e não foi duplicada:
`cdm_loja_peca_publicavel()` recusa publicar sem coleção e sem técnica desde 12/09.

## ITEM 3 — Picassiete, e a prova de que o campo obrigava a mentir

A peça que ela cadastrou tem **"Picassiette" escrito na descrição por ela mesma** e
**"Trencadís" marcado no campo** — porque Picassiete não existia para marcar. É o
caso literal do campo que obriga a pessoa a responder o que não é.

A técnica entrou. **E a versão da Loja subiu com ela, que é a metade que faltava:**
`cdm_loja_termos_iniciais()` só é percorrida quando `CDM_LOJA_VERSAO` difere da
option `cdm_loja_termos` — termo novo sem versão nova é linha no repositório que
nunca vira linha na lista dela. Medido: antes deste bloco a rota pública `/v1/loja`
dizia `tecnica: 4`; depois do Sync diz **5**.

A distinção que o despacho mandou escrever está na **ajuda do campo**, que é onde ela
decide: *"Trincadís é caquinho de azulejo ou cerâmica, sem dar para reconhecer de
onde veio; Picassiete é caco de louça em que dá para reconhecer a peça original —
alça, bico, estampa. Também chamada pique-assiette."* O trincadís **fica**, como o
esclarecimento do mesmo dia manda.

**O slug gravado é `picassiette`, e isto é escolha registrada, não descuido.** O
despacho pediu `Picassiete`; o esclarecimento do mesmo dia diz que "entrou como
`picassiette`" e não o desfaz. As duas taxonomias desta ilha são registradas com
`rewrite` false, então o slug do TERMO não decide endereço nenhum hoje: no dia em
que houver página de técnica, `/tecnicas/Picassiete/` continua inteiramente
disponível, e quem decide o endereço é a malha, não este campo. Na tela, onde ela
lê, o nome é **"Picassiete"** — o `VOZ.md` manda na palavra.

## ITEM 4 — o comportamento do Real 21, com código nosso

O Raphael deu a referência e **mudou a instrução na mesma frase**: a galeria do
Real 21 é Elementor + Swiper, medido por ele em 14/09, e isso é construtor de página
mais biblioteca JavaScript — o que a 22.3 proíbe na página pública e a 11.7 proíbe
instalar. Copiar aquilo trocaria ranqueamento por beleza.

O que nasceu, todo ele sobre o HTML que já estava servido:

- **Foto grande em proporção fixa 4:5** com `object-fit: cover`. Era metade do "está
  muito feio": foto de celular vem em pé e deitada, e sem proporção fixa a página
  saltava de altura entre uma peça e outra.
- **Tira de miniaturas quadradas de verdade** — `aspect-ratio: 1/1` mais
  `object-fit: cover`, o quadrado é do CSS e o arquivo nunca é cortado. **Cada
  miniatura é um link para a âncora da foto**, então ela funciona com o JavaScript
  desligado: `#cdm-foto-3` rola o contêiner de `scroll-snap` sem uma linha de
  script. O `alt` delas é vazio de propósito — a foto grande já descreve a peça, e
  repetir faria o leitor de tela ler a peça inteira duas vezes.
- **Setas de 44 px**, botões de verdade com `aria-label` e `aria-controls`, que só
  rolam o contêiner. Aparecem no ponteiro e somem no toque, onde o dedo já arrasta.
- **Ampliar com `<dialog>` nativo**, X grande, `Esc` (que é do navegador) e clique
  fora. **Zoom** na ampliada com `transform: scale(2)` e origem no ponto tocado.
- **O endereço da foto grande viaja no HTML**, em `data-cdm-grande`: o zoom não é a
  foto pequena esticada, e o script **não busca nada** — que é o outro lado da 22.3.
- Tokens do `DESIGN.md` desta ilha, que ganhou a entrada "Galeria da ficha da peça"
  ANTES do código, como a 22.6 manda.

## O DEFEITO QUE SÓ O AR TINHA, E QUE EU PUBLIQUEI ANTES DE VER

Esta é a parte que vale mais que as quatro acima, porque ela é sobre o portão e não
sobre a tela.

A ficha é montada por `the_content`, e **o retorno desse filtro passa pelo
`wpautop`** — que usa as etiquetas de BLOCO como fronteira de parágrafo, embrulha
cada pedaço em `<p>…</p>`, e depois tira o `<p>` que encosta num bloco e o `</p>`
que vem logo depois de um. **`button`, `dialog`, `span`, `a` e `img` não são blocos
para ele.** A bancada desta ilha não tem WordPress: ela mede o HTML que a função
devolve, e o `wpautop` só existe no site.

Eu previ metade disso e errei a outra. A `<dialog>` foi para o `wp_footer` antes de
qualquer medição, e isso estava certo. As duas setas eu deixei soltas logo depois da
abertura do palco, achando que bastava não vir depois de um `</div>`. **Fui olhar o
HTML servido e ele trazia:**

```
<div class="cdm-gal-palco"><button …>‹</button><button …>›</button></p>
```

Um `</p>` órfão colado no `</button>`: a abertura do parágrafo foi removida por
encostar num `<div>` e o fechamento ficou, porque encostava num `</button>`. Nada
quebra na tela. O navegador engole. **E o portão tinha passado verde**, porque a
régua que eu tinha escrito olhava só um lado — etiqueta de linha DEPOIS de um
fechamento de bloco — e o defeito era do outro, ANTES de uma abertura.

A regra que sobra, e ela vale para tudo que esta ficha imprimir daqui para a frente:
**etiqueta que não é bloco nunca encosta numa fronteira de bloco, de nenhum dos dois
lados.** As setas passaram a morar dentro de um `<div class="cdm-gal-setas">` — uma
camada absoluta que cobre o palco, deixa o dedo passar e ancora as duas. A régua do
`teste-loja.php` passou a medir os dois lados e **nomeia qual** apareceu; a mutação
37 devolve exatamente o HTML que foi ao ar e a régua reprova dizendo
`antes de bloco: </button>`. E o `conferir-atelie-no-ar.py` passou a procurar as
cinco marcas do estrago — `<p><button`, `</button></p>`, `<p><dialog`,
`</dialog></p>`, `<p></dialog>` — **no HTML servido**, porque é lá que o `wpautop`
existe.

## A OUTRA COISA QUE O AR ENSINOU: a ficha é servida de cache por duas horas

Conferindo o conserto, a primeira leitura de `/loja/quadro-flores-do-campo/` veio
com `last-modified` de **13/09 17h01** e `cache-control: max-age=7200`, servindo a
ficha ANTERIOR — com a revisão 28 já aplicada e a rota `/v1/loja` já dizendo
`versao_loja: 1.2.0`. É a família da seção 4 do contrato com uma cara nova: o site
não ficou para trás, a CÓPIA que o visitante recebe ficou. O `conferir-atelie-no-ar.py`
já se protegia disso — o `buscar()` dele anexa `?v=<timestamp>` a toda URL, escrito
lá desde 12/09 — e foi o `curl` a mão desta execução que caiu no cache. Fica
registrado para a próxima passada: **`curl` a mão nesta ilha mede o cache, não o
site.**

## A verificação, em números

- **Bancada, 0 falha:** `teste-casca` **549** (eram 546), `teste-loja` **178** (eram 148),
  `teste-atelie` **288** (eram 251), `teste-leads` 211, `teste-f1` 182, `teste-f2`
  107, `teste-prestacao-rejunte` 5 sobre 540 e 180 estados, `conferir-cobertura` 353,
  `validar-banco` aprovado com 25 materiais e 45 células, `validar-pastilhas`
  aprovado, `php -l` limpo nos três snippets tocados.
- **Mutações:** `mutacoes-atelie` de 37 para **48**, com **48 reprovadas**, 0
  passaram, 0 inertes. `mutacoes-loja` de 23 para **36**, com **36 reprovadas**, 0
  passaram, 0 inertes. `mutacoes-arvore` de 20 para **21**, com **21 reprovadas**.
- **Duas mutações antigas foram consertadas, e as duas por causa deste bloco:** a 26
  do ateliê ficou INERTE porque o alvo dela citava `'peca' => $id`, que o conserto
  renomeou; a 33 da loja ficou INERTE porque a lupa saiu do retorno da ficha.
  Mutação inerte é teste verde com outro nome.
- **Uma afirmação foi endurecida depois de a mutação 25 passar limpa:** a régua da
  proporção fixa procurava `aspect-ratio:4/5` no documento inteiro, e o cartão da
  vitrine também tem essa linha — tirar a proporção da foto grande passava verde.
  Agora ela lê a declaração `.cdm-carrossel img{…}` isolada e imprime o conteúdo
  dela na medida. **Régua que procura no documento inteiro mede a existência da
  palavra, não a do comportamento.**
- **No ar:** `conferir-atelie-no-ar.py` **79 afirmações** (eram 65), 0 falha, 0
  pulada, com a seção 4d nova — o parâmetro, a faixa, a contagem de técnicas — e a
  galeria medida na ficha servida. `conferir-no-ar.py` **416 afirmações, 0 falha**,
  sem tocar uma linha do que mudou.
- **A própria afirmação de ar nasceu errada uma vez, e vale escrever:** a primeira
  versão procurava a FORMA `</button></p>` no HTML servido e reprovou a peça — só
  que essa forma tem versão legítima aqui, no formulário de lead
  (`<p class="cdm-lead-enviar"><button …></button></p>`), com a abertura escrita por
  nós. **O que separa o certo do errado não é a forma, é o BALANÇO.** A afirmação
  passou a contar `<p` e `</p>` dentro da região da galeria, onde a única abertura
  que existe é a da contagem de fotos: 1 abre, 1 fecha. Procurar a forma teria
  reprovado a página certa e, num dia com o formulário desligado, aprovado a errada.
- **A régua do `teste-loja` mudou de forma numa linha, e ela ENDURECEU:** até 13/09
  a afirmação era "a Loja não serve JavaScript nenhum", e ela media a coisa certa
  pelo motivo errado — o que a 22.8 protege não é a ausência de JavaScript, é a
  página FUNCIONAR sem ele. O que ela cobra agora: UM script, no rodapé, depois do
  conteúdo, e **nenhuma** ocorrência de `fetch(`, `XMLHttpRequest`, `import(`,
  `document.write`, `cdn.`, `swiper` ou `elementor` dentro dele.

## E UM TERCEIRO DEFEITO, ACHADO NA CONFERÊNCIA, QUE NINGUÉM ESCREVEU

Contando as URLs do `wp-sitemap.xml` para fechar o bloco, apareceu uma que não é
página desta ilha: **`/author/artesa/`**. Ela não foi escrita por ninguém e nenhuma
linha de código mudou para ela existir — **o provedor `users` do núcleo só lista
autor que TEM conteúdo publicado**, e até 13/09 esta ilha não tinha peça nenhuma.
No minuto em que a artesã publicou a primeira, o arquivo de autor dela entrou no
sitemap: **uma de doze URLs de um domínio de quatro dias.**

Duas razões para tirar, e cada uma bastaria. **É página fina e repetida** — o
arquivo do autor lista as peças publicadas, que é o que `/loja/` já faz com texto
editorial em volta, e orçamento de rastreamento é o recurso escasso da seção 14.1.
E **ele confirma o login dela**: o endereço carrega o `user_nicename`, que nesta
ilha é o mesmo `artesa` com que ela entra; este snippet e o do ateliê gastam
trabalho para a conta de uma pessoa de verdade não ficar exposta, e publicar o nome
de usuário num arquivo XML desfaz metade disso de graça.

Casca **1.9.2**: o provedor `users` sai, pelo mesmo mecanismo que a Aquametria já
media desde 10/09 — aqui ele só não existia porque não havia autor com conteúdo. A
régua entrou no `teste-casca.php` escrita à mão (o nome do provedor e a resposta
esperada estão na linha, não lidos do snippet) e cobra os dois lados: `users` sai,
`posts` e `taxonomies` ficam, para a remoção não vazar. Mutação nova na bateria da
árvore, **21 de 21 reprovadas**. **No ar: o sitemap foi de 12 para 11 URLs, e
nenhum arquivo de autor pede rastreamento.**

**E o `atualizar-manifest.py` fez o trabalho dele nesta passada**, o que é raro o
bastante para ficar escrito: ele **recusou gravar** a revisão 30 porque a versão da
casca no manifest (1.9.1) não batia com a constante do snippet (1.9.2). A recusa
veio antes do commit da revisão, não depois.

## A cópia da seção 24 nasceu, com peça de verdade dentro

`dados/pecas.json` existe desde hoje, com a peça que ela cadastrou: título, slug,
estado, descrição, campos, coleção, técnica e as quatro URLs de foto. Até 13/09 a
rota devolvia `total: 0`, e zero peça é resposta, não falha.

**Uma decisão de formato, e ela é o que faz a regra 24.2 funcionar:** o campo
`gerado_em` da rota **não entra na cópia**. Com ele dentro, toda passada da ronda
seria um commit, e a 24.2 manda commitar só quando o JSON MUDOU. Quando a cópia foi
tirada é o git que sabe — é para isso que ele serve. `publicar: false`, porque este
arquivo é cópia do site e nunca fonte dele; desembarcá-lo devolveria ao WordPress o
que veio de lá.

## Receita, contada do arquivo (nada mudou neste bloco)

7 colas, 25 itens de fabricante, 15 esperando link, 15 sem piso, 22 sem imagem. Os
15 `url_busca` seguem dependendo de UMA sessão do painel da Shopee. Pauta da seção
17: `pauta.md` ainda não existe — 0 escritos, 0 na fila, 0 recusados.
**A loja tem 1 peça publicada e 0 rascunhos**, e é a primeira linha de receita
própria do Arquipélago inteiro.

## Aberto e nomeado

- **(a) A página `/tecnicas/Picassiete/` NÃO nasceu, e o item 3 pedia.** Não é
  esquecimento e não é conserto: **nenhuma** técnica desta ilha tem página. As duas
  taxonomias são registradas `public => false` por decisão medida de orçamento de
  rastreamento (decisão 4 do snippet da Loja, 12/09) — taxonomia pública nasce com
  arquivo e põe de sete a doze URLs finas no sitemap de um domínio de quatro dias.
  Criar a página do Picassiete sozinha seria criar a família inteira por uma porta
  lateral. **Isto é bloco de malha, não item de despacho**, e ficou reescrito no
  `PROMPT.md` como o que falta.
- **(b) A metade humana do item 4 continua aberta:** o dedo dela na galeria, num
  telefone. A Fundação mediu o HTML servido, as marcas do `wpautop`, os
  `aria-label` e a proporção; **ninguém tocou a tela**. Isso fica como o que falta,
  nunca como conferido.
- (c) Os 15 `url_busca` dependem da sessão da Shopee.
- (d) O egresso a fabricante segue fechado e a ficha BRSA005 segue localizada e não
  lida.
- (e) `1x1` de fabricante segue com zero elegível, e é o tamanho de 7 das 12 linhas
  da tabela da F1.
- (f) `contato@clubedomosaico.com.br` ainda não existe como caixa.
- (g) A dívida de modelagem que o esclarecimento do Raphael registrou e mandou NÃO
  mexer agora: o campo "técnica" mistura MÉTODO (direto, indireto) com ESTILO
  (bizantino, trincadís, Picassiete), e ela pode marcar um achando que marcou o
  outro.

**PRÓXIMO, com ordem e motivo:** (1) **a família `/tecnicas/<slug>/`**, que é o que
sobrou do item 3 e agora tem peça publicada para linkar — e é decisão de malha, com
o orçamento de rastreamento na mesa; (2) **a ordem das duas vitrines na F1**, o item
mais antigo da fila e o único que mexe em como a página apresenta produto; (3) `1x1`
de fabricante, a pendência mais cara da categoria pastilha; (4) os 15 `url_busca`,
no minuto em que houver sessão.

---

# 14/09/2026, 13h21Z — A ORDEM DAS DUAS VITRINES DA F1: A PASTILHA VEM PRIMEIRO, E O TÍTULO DEIXA DE DEPENDER DE ESTAR EM SEGUNDO LUGAR

**F1 1.3.0, manifest revisão 31, `/status` conferido. NENHUMA URL nova, NENHUMA
página criada, NENHUM produto entrou ou saiu do banco.** Este é o item mais antigo
da fila desta ilha — o único que mexe em como a página apresenta produto — e foi o
`PRÓXIMO (2)` do fecho anterior depois que o `(1)`, a família `/tecnicas/`, ficou
nomeado como bloco de malha e não de conserto.

**A ESCOLHA DA ILHA: TERCEIRA TENTADA.** Nenhuma ilha tinha despacho aberto para a
Fundação no topo do `PROMPT.md` (os quatro achados da artesã de 14/09 saíram inteiros
na execução das 11h18Z e o que restou é bloco de malha; a aquametria e a robometria
não tinham despacho para a Fundação), então valeu a rotação da seção 1. A aquametria
tinha a `ultima_execucao` mais antiga (11h25Z) e meu push de reserva foi recusado —
outra execução a tomou às 13h19Z. A robometria (11h44Z) caiu do mesmo jeito,
reservada às 13h20Z. A clubedomosaico estava com `executando_desde: null`, que pela
1.1 já significa que não há bloco da Fundação vivo. Nenhum force push, e nada de
execução anterior para mesclar: local e remoto batiam com o `main`. Rede pela 20.2
antes de trabalhar: home em 200 e `/status` na revisão 30, igual à do manifest, em
UMA passada.

## O QUE ERA A ORDEM ERRADA, e por que ninguém a via
Até a 1.2.0 o bloco de compra do **rejunte** vinha antes do da **pastilha**. Não era
decisão: era herança. Quando a vitrine do rejunte nasceu, o lugar da pastilha era uma
frase de espera (`"ainda não temos as pastilhas no nosso banco"`), então o rejunte
era o único bloco de compra que a página tinha. A 1.2.0 encheu aquele lugar com treze
produtos e **manteve a sequência de chamada** — que é como uma ordem provisória
sobrevive a quem a tornou errada. Não havia régua nenhuma sobre ordem, e ordem que
ninguém mede não pode nem ser corrigida com confiança.

A pastilha vem primeiro porque as **três superfícies** que abrem a página falam dela:
o `<title>`, o H1 e a primeira frase da resposta (`"leva cerca de N pastilhas de X
cm"`, com o rejunte entrando como o segundo número). A seção 22.1 põe ranqueamento
antes de conversão antes de beleza; aqui as três apontam para o mesmo lado, porque
quem chega por "quantas pastilhas para mosaico" veio comprar pastilha, e o `VOZ.md`
desta ilha diz "produto primeiro". **Nada da 22.2 se moveu:** a resposta continua
antes da explicação, os DOIS blocos de compra continuam ANTES da camada de prova
(seção 7), e nenhuma URL, trilha, âncora ou JSON-LD mudou.

## O QUE A TROCA REVELOU, e é o que fez disto um bloco e não um swap
O título do bloco da pastilha era **"E onde comprar a pastilha"**. Aquele "E" é
conector: ele só faz sentido depois de outro bloco de compra, e é um título que
**mente quando a ordem muda**. Pior, a seção 5 pede frase autossuficiente, que
sobreviva a ser citada fora de contexto — e o título é justamente a frase que um
modelo de linguagem cita sozinho. Os dois títulos passaram a ser autossuficientes:
**"Onde comprar a pastilha"** e **"Qual rejunte cabe nessa folga"**, nenhum
dependendo da posição em que foi servido. Uma mutação escreve o "E" de volta, e ela é
o defeito de verdade: invisível para qualquer régua de ordem, porque a sequência fica
certa e só o título passa a prometer um bloco anterior que não existe mais.

## A FRONTEIRA DOS DOIS BLOCOS GANHOU NOME (cicatriz da Robometria de 13/09/2026)
A bancada e a conferência no ar extraíam cada vitrine pelo **texto do H2** — régua que
morre calada no dia em que o título muda, e que no estado degradado do rejunte (sem a
F2 no ar, o título é `"Onde comprar o rejunte"`) **nunca conseguiu extrair nada**.
Cada seção passou a declarar o que ela é na própria classe (`cdm-f1-vitrine-pastilha`
e `cdm-f1-vitrine-rejunte`), em **todas** as saídas, inclusive as degradadas.
Fronteira de teste é marcador escrito, nunca "a primeira coisa parecida com". As três
réguas que extraíam pelo título — `teste-f1.php`, `teste-prestacao-rejunte.php` e
`conferir-no-ar.py` — passaram a ler o marcador.

## O MUNDO SEM A F2 FOI PRODUZIDO PELA PRIMEIRA VEZ
A F1 chama a régua do rejunte da F2 em vez de escrever uma segunda (decisão 4 do
cabeçalho dela), e por isso tem DUAS saídas degradadas escritas de propósito — uma em
cada vitrine — que dizem "a lista está fora do ar" e mantêm a conta de pé. Elas
existiam desde 12/09/2026 **sem uma única afirmação encostando nelas**, e a do rejunte
serve um H2 diferente do normal, que era o que fazia a extração por título não achar
nada ali. Régua escrita para um mundo que nunca acontece nasce errada sem poder
falhar (seção 8). O render ganhou `sem_f2=1`, e a bancada agora mede esse mundo: a
conta continua, as duas vitrines dizem que a lista está fora do ar (uma cada), e
nenhum cartão de produto nem recusa é improvisado sem a régua que decide quem entra.

## O PORTÃO VERMELHO QUE JÁ ESTAVA NO main — a cópia da seção 24
Ao rodar a bancada inteira antes de fechar, `validar-banco.py` reprovava o
`dados/pecas.json` que a execução das 11h18Z criou (a cópia da primeira peça de
verdade, "Quadro flores do campo"). A régua era de 12/09 e dizia uma frase só: **o
arquivo não pode existir** — verdadeira enquanto o único jeito de ele aparecer fosse
alguém inventar o catálogo da artesã. Depois disso a **seção 24** entrou no contrato e
virou a mesa: dado que uma pessoa digita no WordPress nasce com cópia no repositório,
e o bloco não fecha sem ela. A proibição envelhecida passou a reprovar o repositório
por cumprir o contrato. A régua foi trocada: o que ela protege não é a ausência do
arquivo, é que ele seja **cópia e nunca fonte**. Três afirmações, e a do meio é a de
verdade: (1) o manifest o declara `publicar: false`; (2) **nenhum snippet o lê** —
medido no código que vai ao ar, com o comentário descartado —, porque peça inventada
só chega à tela se alguém servir o arquivo; (3) o arquivo tem a **forma da resposta do
endpoint** (id de post, URL no domínio da ilha, `total` que bate com a lista, e sem o
carimbo `gerado_em`, que a 24.2 mantém fora da cópia para a ronda não commitar a cada
passada). Quatro mutações novas na bateria do rejunte escrevem os quatro defeitos de
volta — cópia publicada, snippet lendo a cópia, total digitado, peça sem id.

## A VERIFICAÇÃO, EM NÚMEROS (bancada, 0 falha)
- **`teste-f1.php`**: nasceu a seção **4d** (ordem das duas vitrines) com 15 estados,
  um processo cada — marcador único, pastilha antes do rejunte, resposta antes das
  duas, as duas antes da prova, e nenhum título abrindo com conector, medido em 6
  títulos. Mais o mundo sem a F2 produzido. O arquivo foi de 190 para **211
  afirmações**.
- **`mutacoes-f1.py`**: de 40 para **46 mutações, 46 reprovadas, 0 passaram** — as
  seis novas: ordem invertida, o "E" de volta no título, a vitrine descendo para
  depois da prova (uma versão que reprova pela ordem, outra que preserva a ordem e só
  inverte compra x procedência), o marcador da pastilha sumindo, e o do rejunte
  sumindo SÓ na saída degradada.
- **`teste-prestacao-rejunte.php`**: 5 afirmações, 540 estados da F2 e 180 da F1, a
  extração do bloco do rejunte da F1 agora pelo marcador.
- **`validar-banco.py`**: OK, 25 materiais, 45 células da F2; a régua nova da cópia da
  seção 24 no ar.
- **`mutacoes-rejunte.py`**: de 12 para **16 mutações, 16 reprovadas** (as quatro
  novas da cópia da seção 24).
- **`validar-pastilhas.py`** 189, **`mutacoes-prestacao.py`** 11 de 11,
  **`mutacoes-cobertura.py`** 11 de 11, **`teste-casca.php`** 549, **`teste-f2.php`**
  107, **`teste-loja.php`** 178, **`teste-atelie.php`** aprovado, **`teste-leads.php`**
  211, **`conferir-cobertura.php`** 353, **`php -l`** limpo em tudo.

## NO AR (o desembarque)
Sync disparado UMA vez, revisao 31 com 10 aplicados; `/status` na revisao 31, igual
a do manifest. A F1 serve, no HTML servido, a vitrine da **pastilha antes** da do
rejunte, com os marcadores `cdm-f1-vitrine-pastilha` e `cdm-f1-vitrine-rejunte` e os
titulos **"Onde comprar a pastilha"** e **"Qual rejunte cabe nessa folga"** — nenhum
abrindo com conector. `conferir-no-ar.py`: **437 afirmacoes** (eram 416), 0 falha,
incluindo a ordem das duas vitrines medida em tres estados servidos.

## PROXIMO, com ordem e motivo
1. **A familia `/tecnicas/<slug>/`**, decisao de malha com o orcamento de rastreamento
   na mesa, e agora com peca publicada para linkar.
2. **`1x1` de fabricante**, a pendencia mais cara da categoria pastilha — sozinha muda
   7 das 12 linhas da tabela da F1.
3. **A categoria COLA**, 45 estados varridos e 0 com o minimo da 14.3.
4. Os 15 `url_busca`, no minuto em que houver sessao da Shopee.
