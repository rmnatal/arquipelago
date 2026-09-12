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
