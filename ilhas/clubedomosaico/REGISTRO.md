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
