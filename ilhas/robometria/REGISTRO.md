# Registro de execucoes — Robometria

Log append-only da Fundacao. Cada execucao escreve aqui o bloco entregue e
o proximo passo desbloqueado, e espelha o mesmo resumo em
`/areas/projeto-robometria.md` na memoria.

## 2026-09-09 — Pasta da ilha criada

- Criada a pasta `ilhas/robometria/` com `snippets/`, `conteudo/`, `dados/`,
  `ferramentas/`, `manifest.json` (revisao 0, nenhum item, nada marcado para
  publicar), `README.md`, `PROMPT.md`, `ESTADO.md` e este registro.
- A pasta nasceu junto com a reorganizacao do Arquipelago em uma unica
  Fundacao com despachante: as regras comuns passaram para o `ARQUIPELAGO.md`
  da raiz e o que e desta ilha ficou no `PROMPT.md` daqui.
- Infraestrutura no dia da criacao: dominio robometria.com.br registrado em
  09/09/2026, dominio adicional ja criado no cPanel da HostGator com raiz
  propria, nameservers ns604 e ns605.hostgator.com.br apontados no
  registro.br. WordPress ainda NAO instalado, aguardando propagacao de DNS;
  snippet de Sync ainda nao existe. Identidade visual aprovada em 09/09/2026.
- **Proximo passo: bloco 1 — levantamento de buscas parametricas** em
  `dados/corpus-buscas.md`, separando o eixo de compatibilidade (peca x
  modelo) do de dimensionamento (Pa, m2, autonomia), com procedencia marcada
  consulta a consulta. Nao depende de site nem de WordPress.

## 2026-09-09 — Bloco 1: corpus de buscas parametricas

- Criado `dados/corpus-buscas.md` (revisao 1 do manifest) com o levantamento
  de buscas do nicho robo aspirador, coletado por busca web em 09/09/2026
  (paginas oficiais de fabricante, marketplaces, foruns, titulos de video).
  Sem acesso a ferramenta de volume de busca nesta coleta — o arquivo registra
  essa limitacao explicitamente em vez de inventar contagem.
- Dois eixos separados, sem mistura em nenhuma ferramenta: **compatibilidade**
  (cluster A1 filtro, A2 escova lateral, A3 mop, A4 bateria) e
  **dimensionamento** (cluster B1 Pa, B2 cobertura em m2, B3 autonomia por
  carga, B4 forum/video de guia de compra geral).
- Achados principais: (1) cada fabricante nomeia a peca pelo codigo do proprio
  modelo e nao existe comparador cross-marca — confirma o buraco que a
  Bussola identificou; (2) um blog do proprio nicho ja alerta contra "filtro
  HEPA universal" por causa de encaixe diferente por modelo — a Robometria
  resolve isso com dado verificado por modelo; (3) Pa recomendado para pet
  diverge entre fontes brasileiras (1.500 a 6.000 Pa, sem consenso) — vira
  ferramenta de faixa com criterio, no mesmo padrao da Aquametria; (4) nenhuma
  fonte publica a formula mAh -> minutos -> m2 com a conta explicita, so
  numero fechado do fabricante — e o vacuo de conteudo que o dimensionador
  (ferramenta b) deve ocupar.
- Lista inicial de modelos/codigos de peca para o Bloco 3 (nenhum dado tecnico
  copiado para banco ainda, precisa reconfirmar na fonte primaria e datar):
  Multilaser HO041/HO400/HO401/HO407/OB010, HO03/HO04, HO011/HO012; Positivo
  PRA500/PRA1000/PRA8000/PRA2000; Xiaomi Mop/Mop 2/Mop 2 Lite/S20/S40/H40;
  iRobot Roomba serie s; Velds RALW-C; WAP W90/W100/W400; Electrolux ERB44.
- `manifest.json` foi para revisao 1: item `corpus-buscas` em `dados`, com
  `publicar: false` (e pesquisa, ainda nao vira pagina) e sha256 conferido.
- **Proximo passo: bloco 2 — especificacao das ferramentas**
  (`dados/especificacao-calculadoras.md` + `dados/constantes.json`), usando os
  dois eixos deste corpus como esqueleto: (a) localizador de peca compativel
  por modelo, (b) dimensionador de succao e autonomia por area, piso e pelo.
  Continua sem depender de WordPress nem de dominio.

## 2026-09-09 — Bloco 2: especificacao das ferramentas R1 e R2

- Criados `dados/especificacao-calculadoras.md` e `dados/constantes.json`
  (manifest para revisao 2, os dois com `publicar: false` — sao pesquisa, e o
  site desta ilha ainda nao existe). As duas ferramentas ancora do `PROMPT.md`
  ficaram especificadas ponta a ponta: **R1**, localizador de peca compativel
  por modelo (eixo compatibilidade), e **R2**, dimensionador de succao e
  autonomia por area, piso e pelo (eixo dimensionamento). Sub_id 2: `R1` e `R2`.
- **A R1 nunca infere compatibilidade.** Cada par peca x modelo sai com um de
  tres selos, e o selo aparece na frase, nao numa legenda de rodape:
  `declarada_fabricante` (unico nivel que pode ser escrito como "serve"),
  `declarada_terceiro` (lojista ou marketplace, em secao separada, rotulada e
  nunca em primeiro lugar) e `nao_declarada` (a ferramenta diz que nao achou e
  para ali — silencio parece defeito). Entrada de modelo e lista fechada: campo
  livre faria a ferramenta adivinhar de qual fabricante e o "V3" dos anuncios
  sem marca que o Bloco 1 encontrou, e adivinhar compatibilidade e o defeito
  que esta ilha existe para nao cometer.
- **REGRA NOVA, e ela inverte a da Aquametria: divergencia de compatibilidade
  resolve pelo conjunto MAIS ESTREITO.** O caso que a fixou apareceu nesta
  coleta: o filtro Multilaser **PR10205** e declarado para "HO041" no canal de
  varejo e para "HO041 e OB010" no canal de empresas — mesmo codigo, mesmo
  fabricante, conjuntos diferentes — e ainda existe um **PR10343**, codigo
  proprio para o OB010. Vale HO041; a outra declaracao e publicada como
  divergencia, com as duas datas; para o OB010 a R1 aponta o PR10343. O banco
  de especies da Aquametria resolve divergencia pelo MAIOR, e a inversao aqui e
  deliberada: la o erro para o lado largo da ao peixe mais espaco do que
  precisa, aqui faz alguem comprar peca que nao encaixa. **A assimetria de
  custo decide a direcao do arredondamento, nao o gosto de quem grava.**
- Achado estrutural da mesma coleta: a escova lateral **PR10124** e declarada
  para cinco modelos (HO041, HO400, HO401, HO407, OB010) enquanto o filtro da
  MESMA familia cobre menos. **Compatibilidade nao se herda do modelo para a
  classe de peca** — e declarada por codigo de peca, um a um. E o que justifica
  o `selo_de_compatibilidade` ser campo de primeira classe no Bloco 3.
- **A R2 calcula o numero que ninguem publica, sem inventar coeficiente.** O
  Bloco 1 achou o vacuo (nenhuma fonte mostra a conta bateria -> autonomia ->
  area) e esta coleta confirmou com um caso limpo: a pagina oficial da Xiaomi
  declara 3.200 mAh, ate 120 min e recarga de 220 min para o S20 — e **nao
  declara m2 nenhum**. Entao a R2 publica CICLOS = teto(area / cobertura
  declarada) e TEMPO REAL ATE TERMINAR = ciclos x autonomia + (ciclos - 1) x
  recarga. Com o Electrolux ERB44 (162 m2 por carga, ate 2 h, loja oficial),
  uma casa de 200 m2 da 2 ciclos: o servico termina em muito mais tempo do que
  as "2 horas" do anuncio. Era esse o numero que a pessoa queria — nao a
  autonomia, mas **quando a casa fica limpa**.
- Tres honestidades ficaram escritas na propria pagina, em vez de virarem
  coeficiente: a area informada e area livre de piso e a ferramenta **nao**
  aplica fator de obstrucao inventado; o calculo de mais de um ciclo so vale se
  o modelo **retomar apos recarregar** (campo novo `retoma_apos_recarga` no
  Bloco 3); e onde o fabricante declara so minutos, a R2 escreve "o fabricante
  nao declara cobertura em m2 para este modelo" e **nao converte**.
- **A taxa de cobertura m2/min entrou como `pendente` e PROIBIDA em formula
  publicada** (secao 10 do contrato). O banco tem um unico par (minutos, m2)
  declarado por fabricante — 1,35 m2/min do ERB44 — e **um ponto nao e um
  coeficiente**. Sai de pendente com 5 pares declarados de marcas diferentes, e
  mesmo assim publica faixa com a dispersao a mostra, nunca a media.
- **Limiar de Pa e recomendacao editorial, nao especificacao de fabricante, e a
  pagina diz isso com essas palavras.** As fontes brasileiras divergem e a R2
  mostra o desacordo com o nome de quem recomenda cada numero, no padrao das C3
  e C5 da Aquametria: Canaltech recomenda acima de 4.000 Pa para pet; Mundo
  Conectado trata 3.000 Pa como consenso minimo, com faixa confortavel entre
  4.000 e 6.000, e ainda registra que acima de 6.000 Pa o ganho fica proximo do
  limite pratico percebido — constante util contra o proprio nicho, porque e o
  que impede a R2 de virar corrida de Pa.
- **Classificacao de SERP feita antes de especificar, como manda a secao 14.9.**
  A consulta de compatibilidade ("qual filtro serve no PRA500") e ALVO: a
  primeira pagina e anuncio de marketplace, pagina do robo (nao da peca) e
  review — **a resposta que esta no ar e copy de anuncio**, sem fonte e sem
  data. Ja "quantos Pa para pelo de cachorro" e alvo apenas PARCIAL: a consulta
  curta esta tomada por Canaltech, Mundo Conectado, TechTudo e Exame, e a
  Robometria **nao** disputa essa — seria gastar rastreamento de dominio novo
  para estacionar na pagina 4. Nasce mirando a paramétrica com a casa da pessoa
  dentro, que nenhum daqueles veiculos responde com numero.
- Quatro numeros ficaram **`nao_publicavel` por atribuicao incerta** (faixa
  5.000–10.000 Pa para carpete, minimo de 3.000 Pa para piso frio, vida util da
  escova lateral): vieram de resumo agregado de busca, sem dar para dizer qual
  veiculo os publica. Numero sem autor identificado nao vai para a tela.
- Duas correcoes no que o Bloco 1 tinha registrado: **`PRA8000` nao existe** em
  canal oficial nenhum (a linha da Positivo e PRA500, PRA800, PRA1000 e
  PRA2000 — vale PRA800, e nenhum dado tecnico foi herdado do nome errado), e o
  filtro **PR550 (HO03/HO04) esta fora do banco** porque e peca de aspirador de
  po 2 em 1, nao de robo. Os dois ficaram gravados justamente para a proxima
  execucao nao recolhe-los de novo.
- Coleta em aberto, declarada e nao escondida: o egresso HTTP direto esta
  fechado (`multilaser.com.br` e `manuals.plus` devolveram EGRESS_BLOCKED em
  09/09/2026), entao tudo saiu de busca restrita ao dominio. A Aquametria ja
  registrou um caso de busca restrita devolver numero errado com atribuicao
  certa — por isso cada constante traz o canal de coleta, e a releitura na
  fonte primaria e trabalho do Bloco 3, nao capricho.
- Nada foi publicado e nao havia o que publicar: os tres itens do manifest sao
  pesquisa (`publicar: false`) e o WordPress desta ilha ainda nao existe. Sem
  site nao ha Sync para acionar nem `/status` para conferir — a secao 4 do
  contrato passa a valer aqui quando houver WordPress. Itens esperando link de
  afiliado nesta ilha: **zero**, porque o banco de produtos ainda nao existe.
- **Proximo passo: bloco 3 — modelo do banco** (`dados/esquema-banco.json` e os
  primeiros registros de MODELO DE ROBO, PECA e MARCA), com os campos que a
  secao 4 da especificacao lista: `categoria` (para barrar aspirador comum),
  `pa_declarado`, `autonomia_min_declarada`, `cobertura_m2_declarada` (nulo
  quando o fabricante nao declara — e nulo e resposta, nao lacuna),
  `recarga_min_declarada`, `retoma_apos_recarga`, `bateria_mah`, `voltagem`,
  `base_autoesvaziamento`, `codigo_fabricante`, `modelos_compativeis[]`,
  `selo_de_compatibilidade`, `divergencias[]`, `vida_util_declarada`, mais
  `imagem{url,largura,altura,fonte,coletado_em,alt}` e `afiliado{url,coletado_em}`
  desde ja — a Aquametria descobriu tarde que o banco nao tinha imagem e travou
  a vitrine. Continua sem depender de WordPress nem de dominio.

## 2026-09-09 — Bloco 3: modelo do banco, e o banco ja verificavel

- Entregues `dados/esquema-banco.json` (contrato das entidades MARCA,
  MODELO_ROBO, PECA e COTACAO), `dados/marcas.json` (4 marcas),
  `dados/modelos-robo.json` (17 modelos), `dados/pecas.json` (8 pecas, **10
  pares peca x modelo**) e `ferramentas/validar-banco.py`. Manifest na
  revisao 3, com sha256 de cada arquivo commitado.
- **Todo par de compatibilidade e DECLARADO pelo fabricante. Nenhum foi
  inferido.** Onde nao ha declaracao, nao ha linha — e a R1 diz que nao achou e
  para ali, em vez de supor.
- **Todo numero e `{valor, fonte, declarado_como}`**, com a transcricao do texto
  do fabricante junto do numero. Sem a transcricao a pagina parafraseia em vez
  de citar, e a frase citavel com procedencia e exatamente o que a secao 5 do
  contrato exige. Onde o fabricante nao declara, o valor e `null` COM MOTIVO, e
  o motivo vai para a tela com essas palavras.
- **ACHADO QUE MUDOU O ESQUEMA: `variante_de_hardware`.** O proprio fabricante
  vende DUAS baterias para o MESMO codigo de modelo — PR10127 ("Versao A") e
  PR8116 ("Mars HO041 versao B"). Saber que o robo e um HO041 nao basta para
  acertar a peca. O campo entrou no esquema e a consequencia ficou escrita: com
  mais de uma variante conhecida, a R1 mostra as duas e explica como a pessoa
  descobre qual e a dela. Devolver uma so seria adivinhar.
- **Pendencia do Bloco 2 RESOLVIDA:** HO011 e HO012 sao aspirador de po vertical
  e de mao 2 em 1 (127 V/1000 W e 220 V/700 W, pelos titulos das paginas do
  proprio fabricante), NAO robos. Logo o filtro PR684 nao e peca de robo e ficou
  `excluido_do_banco`, com a fonte, para nenhuma execucao futura recolhe-lo de
  novo. Mesmo tratamento do PR550 (HO03/HO04), que ja vinha do Bloco 2.
- **Quatro modelos novos com categoria confirmada pelo fabricante:** HO407
  (Duster), OB010 (ObaDuster), HO243 (Hydra / Acqua Solution, 90 minutos
  declarados) e HO411 (Midnight, com lamina oficial em PDF que devolveu
  EGRESS_BLOCKED). **Duas pecas novas:** o pano PR10342, que fecha o cluster A3
  do corpus (mop) — ate agora sem nenhum item — e a bateria PR8116.
- **Duas divergencias resolvidas pelo conjunto MAIS ESTREITO**, com as duas
  declaracoes publicadas e datadas: o filtro PR10205, em que dois canais do
  proprio fabricante discordam sobre o OB010; e a bateria PR8116, cuja
  divergencia esta DENTRO de uma unica pagina — o titulo promete "Mars, Moon e
  Duster" e o endereco da mesma pagina diz "Mars HO041 versao B". Antes de
  resolver, ficou escrito qual e o erro caro: mandar alguem comprar peca que nao
  encaixa. A direcao saiu sozinha depois disso, como manda a secao 10.
- **Achado de elegibilidade:** o Positivo PRA800 declara 2.800 Pa e portanto fica
  ABAIXO dos dois limiares editoriais para casa com pet (3.000 Pa no Mundo
  Conectado, 4.000 Pa no Canaltech). E um caso limpo da secao 7: ele nao pode
  encabecar a lista de uma consulta com pet.
- **VERIFICACAO DESTE BLOCO** (nao ha site, entao a secao 8 se aplica pela parte
  que existe): `python3 ferramentas/validar-banco.py` roda sem rede e sai
  APROVADO — 4 marcas, 17 modelos (12 publicaveis, 1 nao publicavel, 4 excluidos
  por nao serem robo), 8 pecas, 10 pares declarados, 18 itens esperando link. Ele
  reprova id duplicado, numero sem fonte, null sem motivo, registro publicavel
  com categoria que nao e robo, divergencia sem resolucao escrita, peca apontando
  para modelo inexistente ou excluido, e contagem de cabecalho que nao bate com o
  arquivo. Os tres arquivos de dados passam por ele.
- **O que este bloco deliberadamente NAO fez:** nao converteu os 30 W do HO041
  em Pa (potencia nao e succao e nao existe conversao); nao emprestou a vida util
  de 6 meses do manual da Electrolux para as pecas da Multi; nao coletou nenhuma
  imagem (o campo `imagem{}` existe completo com `url` null, e pela secao 6 isso
  NAO elimina o registro da vitrine); e nao tirou a taxa de cobertura m2/min de
  `pendente`, porque continua havendo um unico par (minutos, m2) declarado.
- **Infraestrutura: a Fundacao nao escreve o que nao mediu.** `robometria.com.br`
  devolveu EGRESS_BLOCKED nesta execucao, entao a nuvem nao consegue dizer se ha
  WordPress no ar. Quem atualiza essa linha do `ESTADO.md` e quem tem navegador
  (Sentinela ou o proprio Raphael), como ja diz a secao 12 do contrato.
- Itens esperando link de afiliado nesta ilha: **18** (12 modelos e 6 pecas). O
  campo `afiliado.url` nasce presente e vazio em todo registro, com
  `sub_id_1 = robometria` e `sub_id_2` = R1 ou R2.
- **Proximo passo: bloco 3c — expandir o banco**, e ele vem antes do bloco 6
  (prospeccao do widget) por um motivo medido: hoje so DOIS modelos tem
  `pa_declarado`, entao a lista de recomendados da R2 sairia praticamente vazia
  em qualquer entrada, e faixa descoberta e a unica urgencia de catalogo (secao
  14.3 — numero redondo de itens nao e criterio). Ordem de coleta, da maior para
  a menor: (1) pares (minutos, m2) declarados, que sao o que tira a taxa de
  cobertura de `pendente` e destrava a R2 fora do ERB44 — a Xiaomi e a Electrolux
  sao as fontes de maior rendimento por consulta; (2) `pa_declarado` dos modelos
  que ja estao no banco sem ele; (3) pecas da Xiaomi e da Positivo, que hoje
  estao no banco so pelo lado do MODELO e nao respondem nada na R1; (4) pecas de
  reposicao da Electrolux, que e a lacuna mais barata — a ilha ja tem a vida util
  de 6 meses do manual e nao tem o codigo da peca a que ela se aplica. O bloco
  3b (casca) continua sendo o primeiro que depende do WordPress.

## 2026-09-09 21:26Z — Bloco 3c: o banco saiu do modelo e virou cobertura

- **Entregue:** 24 modelos de robo (eram 17), 18 pecas (eram 8) e **33 pares
  peca x modelo declarados** (eram 10). Esquema na **versao 2**, manifest na
  **revisao 4**. Nenhum par inferido: todos saem de declaracao do fabricante,
  com titulo transcrito, URL, canal de coleta e data campo a campo.
- **Modelos novos (7):** Electrolux ERB30, ERB60, ERB61, ERB62 e ERB80;
  Positivo PRA500 e PRA2000. **Atualizados (4):** ERB10 e ERB11 ganharam
  autonomia declarada (140 min, "2h20"), o ERB44 ganhou os dois reservatorios
  (520 ml de po e 150 ml de agua), e os quatro Electrolux ganharam o motivo
  correto no `pa_declarado` null.
- **Pecas novas (10):** Kit Performance **KPCEL01** (ERB10/ERB11/ERB20), filtro
  HEPA com espuma (ERB44/60/61/62), Kit Performance (ERB60/61/62), escova
  rotativa central (ERB60/61/62/80), kits do ERB44 e do ERB30, as tres pecas da
  Positivo para PRA800/PRA2000 (escova lateral 11206518, escova central 11206519
  e mop 11206540) e os acessorios do Xiaomi S20.
- **LACUNA (d) FECHADA.** Desde o Bloco 3 a ilha tinha a vida util de 6 meses do
  manual da Electrolux e **nao tinha o codigo da peca a que ela se aplica**.
  Agora tem: e o filtro HEPA dentro do KPCEL01. O achado que muda a R1 e que a
  Electrolux **nao vende filtro de robo avulso** nesta linha — quem procura
  "filtro do ERB10" compra o kit.
- **LACUNA (c) FECHADA nas duas pontas.** Positivo e Xiaomi estavam no banco so
  pelo lado do MODELO e nao respondiam nada na R1. Agora respondem.
- **DESCOBERTA QUE MUDA A ESTRATEGIA DE COLETA: a Electrolux nao publica succao
  em Pa em canal nenhum** — loja oficial, content, cuida e compraparceiros
  declaram NIVEIS de succao (minimo, medio, maximo), nunca pascal. Veiculos
  editoriais citam 4.000 Pa para a linha, mas pela escada_de_fontes editorial
  NUNCA sustenta especificacao de aparelho, entao o numero ficou de fora de
  proposito. Isso **corrige a suposicao do bloco anterior**, que tratava a
  Electrolux como fonte de maior rendimento: `pa_declarado` segue em **2 de 19**
  modelos publicaveis e tem que vir de Xiaomi, Multi, WAP e Positivo.
- **LACUNA (a) AVANCOU E CONTINUA ABERTA, com numero na mao.** O segundo par
  (minutos, m2) declarado entrou: 166 m2 em ate 1h40 na familia ERB60/61/62/80,
  contra 162 m2 em ate 2h do ERB44. Sao **1,66 contra 1,35 m2/min — 23% de
  diferenca DENTRO da mesma marca**. A `taxa-cobertura-m2-por-min` **continua
  PROIBIDA em formula publicada**, e agora com dois numeros do proprio fabricante
  sustentando o porque. Faltam pares de marcas DIFERENTES: sao 2 declaracoes de 1
  marca e o criterio pede 5 de marcas diferentes. Publicar a media seria a unica
  saida proibida pela secao 10 do contrato.
- **O ESQUEMA SUBIU PARA A VERSAO 2, e os dois campos novos foram forcados pelo
  dado, nao pelo gosto:** (1) tipo de peca **`kit`** com `composicao[]`, porque
  sem ele a R1 nao responde a propria consulta-alvo quando a marca so vende
  consumivel em kit; (2) **`codigo_fabricante` aceita null COM
  `motivo_sem_codigo`**, porque a Multi publica codigo proprio, a Electrolux
  identifica peca por titulo e a Positivo por SKU do canal oficial. E a mesma
  regra que ja valia para numero: null e resposta, nao lacuna.
- **"COMPATIBILIDADE NAO SE HERDA" APARECEU NO CATALOGO DO PROPRIO FABRICANTE:**
  o ERB80 esta na lista da escova rotativa central e **nao** esta na do filtro
  HEPA com espuma nem na do Kit Performance do ERB60/61/62. A R1 nao pode
  completar lista por analogia, e agora a ilha tem o exemplo para mostrar.
- **ARMADILHA DA R1, ESCRITA ANTES DE CUSTAR CARO:** o **PRA500** e literalmente
  a consulta-alvo da especificacao, e as tres pecas novas da Positivo declaram
  **PRA800 e PRA2000 sem cita-lo**. Pelo conjunto mais estreito, a resposta certa
  para o PRA500 e "nao encontramos peca declarada". Esta escrito no registro do
  modelo e no de cada peca, para nenhuma execucao futura afrouxar isso.
- **VERIFICACAO DESTE BLOCO** (nao ha site, entao a secao 8 se aplica pela parte
  que existe): `python3 ferramentas/validar-banco.py` roda sem rede e sai
  **APROVADO** — 4 marcas, 24 modelos (19 publicaveis, 4 excluidos por nao serem
  robo, 1 a confirmar), 18 pecas (16 publicaveis), 33 pares declarados, 35 itens
  esperando link. O verificador ganhou **cinco invariantes** da versao 2, e as
  cinco foram **testadas quebrando o banco de proposito numa copia**: kit sem
  composicao, kit dentro de kit, item de composicao sem tipo e sem descricao,
  composicao em peca que nao e kit, e codigo null sem motivo. As cinco reprovam
  alto. Verificador que nao falha nao vale nada.
- **O que este bloco deliberadamente NAO fez:** nao aceitou os 4.000 Pa
  editoriais para a linha Electrolux; nao leu a diferenca de texto entre "base de
  carregamento inteligente" (ERB60/61/62) e "base autolimpante" (ERB80) como
  declaracao de ausencia de autoesvaziamento nos tres primeiros; nao estendeu os
  acessorios do Xiaomi S20 ao S20+, que tem FAQ propria e nao esta no banco; nao
  gravou o KPCEL02 nem o controle remoto CRCEL01 (o primeiro tem codigo e nao tem
  compatibilidade confirmada, o segundo nao e consumivel e nao tem tipo no
  vocabulario) — os dois foram para a lista de compras; e nao coletou imagem
  nenhuma, porque o egresso segue fechado.
- **Egresso medido nesta execucao:** `loja.electrolux.com.br` e
  `content.electrolux.com.br` devolveram EGRESS_BLOCKED, somando-se aos dominios
  da Multi, ao `mi.com` e ao `manuals.plus`. Toda a coleta saiu de busca restrita
  ao dominio oficial, com o canal declarado campo a campo.
- Itens esperando link de afiliado nesta ilha: **35** (19 modelos e 16 pecas) —
  quase o dobro dos 18 anteriores. Pela secao 7 do contrato isso e trabalho
  pendente de verdade e nao compete com a fila da Fundacao: quem gera link e a
  Sentinela estrategica, no navegador do Raphael, com teto de calendario.
- **Proximo passo: continuar o 3c, com o alvo trocado.** A ordem agora e (1)
  `pa_declarado` em **Xiaomi, Multi, WAP e Positivo** — nunca mais na Electrolux,
  que nao publica o campo — porque sem ele a lista de recomendados da R2 sai
  vazia em qualquer entrada; (2) pares (minutos, m2) de marcas DIFERENTES, que
  sao o que tira a taxa de cobertura de pendente; (3) confirmar se existe peca
  declarada para o PRA500, que e a consulta-alvo da R1; (4) transcrever a
  composicao dos kits do ERB44 e do ERB30, hoje no banco com a composicao em
  aberto. O bloco 3b (casca) continua sendo o primeiro que depende do WordPress,
  que depende do certificado.

---

## 2026-09-09T23:16Z — Bloco 3c, SEGUNDA LEVA: `pa_declarado` fora da Electrolux

**Ilha reservada por commit** (secao 1 do ARQUIPELAGO.md) as 23:16Z, com a Aquametria
livre e a Robometria com `ultima_execucao` mais antiga (21:26Z contra 21:55Z). Sem
DESPACHO DA SENTINELA na fila desta ilha e sem branch ou PR pendente.

**O QUE FOI ENTREGUE.** O banco foi de 24 para **33 modelos** e de 4 para **5 marcas**.
Entraram seis Xiaomi (S10, E10, S40, S40C, H40 e Mop 2) e tres WAP (W400, W1000, W310), e
as fichas de PRA500 e PRA2000 sairam do vazio. Esquema na **versao 3**, manifest na
**revisao 5**.

**O NUMERO QUE IMPORTA: `pa_declarado` passou de 2 para 11 modelos publicaveis**, em 3
marcas, cobrindo de **1.400 Pa (WAP W400) a 10.000 Pa (Xiaomi S40 e H40)** numa escala
continua. Antes desta leva a R2 sairia com **lista vazia em qualquer entrada**. Agora nao
sai.

- **A VARREDURA QUE A SECAO 14.3 EXIGE FOI FEITA, e esta gravada em
  `cobertura_de_faixa_r2` dentro de `modelos-robo.json`.** A faixa de entrada da R2 foi
  percorrida de ponta a ponta contra as seis constantes de limiar de Pa. Resultado: **5
  das 6 faixas passam** no portao de 3 itens da secao 9.
- **A FAIXA DESCOBERTA que sobrou:** acima de **6.000 Pa** so ha 2 elegiveis (S40 e H40).
  Pela secao 14.3, faixa descoberta e a unica urgencia de catalogo — entao ela virou o
  topo da `lista_de_compras`.
- **O ACHADO QUE SO APARECEU PORQUE A VARREDURA FOI OLHADA INTEIRA, e que contar elegiveis
  esconde: TODA faixa igual ou acima de 3.000 Pa e 100% Xiaomi.** Os seis elegiveis da
  faixa de pet do Canaltech sao seis Xiaomi. O portao de 3 itens passa contando, e a
  vitrine ainda assim sairia como catalogo de uma marca so — numa ilha cuja promessa e ser
  o comparador **cross-marca** que o nicho nao tem. Isso NAO e defeito de elegibilidade e
  NAO se conserta afrouxando a regra da secao 7: conserta-se colhendo Pa de outra marca
  dentro da faixa. Ficou escrito em tres lugares para nenhuma execucao futura ler "6
  elegiveis" e dar a faixa por resolvida.
- **A CAUSA DAS DUAS COISAS ESTA MEDIDA, e vira conteudo:** Electrolux e Multi **nao
  publicam Pa em canal nenhum** (declaram *niveis* de succao), e a WAP so publica na parte
  barata da linha — 1.400 Pa no W400, e nenhum numero no topo W1000, que declara so "tres
  modos de succao". Publicar Pa e decisao de marketing por modelo, nao politica de marca.
  Quem declara succao alta no Brasil, hoje, e essencialmente a Xiaomi.
- **A LACUNA DE m² MUDOU DE NATUREZA E DEIXOU DE SER COLETA.** Xiaomi, WAP, Multi e
  Positivo foram varridas modelo a modelo e **NENHUMA declara area coberta em m2 em canal
  nenhum**. So a Electrolux declara. Nao adianta procurar mais: o numero nao esta
  publicado. A `taxa-cobertura-m2-por-min` continua `pendente` e **PROIBIDA em formula**,
  agora com quatro marcas de silencio medido sustentando o porque — e a recusa da R2 deixa
  de ser pendencia envergonhada e vira a resposta publicavel: quando um site promete
  "atende ate 120 m2" para um robo cujo fabricante so declarou minutos, esse numero foi
  inventado por alguem. Essa e a frase que um modelo de linguagem cita.
- **PRIMEIRA DIVERGENCIA DE ESPECIFICACAO DE APARELHO DO BANCO, e ela forcou o esquema.**
  O PRA500 declara **1600 Pa na ficha e 2000 Pa no texto de venda da MESMA pagina do
  fabricante**. Mesmo canal, mesmo nivel: nao ha desempate por escada de fontes, e a media
  (1800) e a unica saida proibida pela secao 10. **Valeu 1600**, porque o erro caro e o do
  lado ALTO — publicar 2000 faz alguem comprar um robo fraco demais para o pelo que tem em
  casa, por recomendacao nossa. Errar para baixo so tira o PRA500 de uma lista que ele
  talvez coubesse. As duas declaracoes vao para a tela com atribuicao. Ate a versao 2 so
  PECA tinha `divergencias[]`; agora MODELO_ROBO tambem tem.
- **REGRA NOVA DA VERSAO 3, escrita antes de custar caro: faixa e tolerancia declaradas
  resolvem para o lado em que errar doi menos, NUNCA para o meio.** O fabricante quase
  nunca da numero: da "de 5 a 6 horas" (recarga do PRA2000) ou "130 minutos +-10%"
  (autonomia do S10). Por campo: **Pa para baixo** e **autonomia para baixo** (errar para
  cima promete um aparelho que nao existe); **recarga para cima** (errar para baixo faz a
  R2 prometer mais ciclos por dia do que o robo entrega). `declarado_como` guarda a faixa
  INTEIRA, entao a pagina cita "de 5 a 6 horas" e nao o numero escolhido.
- **A WAP entrou no banco e e a melhor chance de NIVEL 2 que a ilha ja teve.** E a unica
  marca da coleta que publica um manual em PDF por modelo, em endereco proprio e estavel,
  com revisao e data no nome do arquivo (`REV00MAI23` no W400). Hoje o dominio devolve
  EGRESS_BLOCKED e o PDF ficou registrado em `fontes{}` como alvo da releitura. **A ilha
  inteira esta em nivel 3 e 4: nao existe nenhuma fonte de nivel 2 ate agora.**

**VERIFICACAO DESTE BLOCO** (nao ha site, entao a secao 8 se aplica pela parte que
existe): `python3 ferramentas/validar-banco.py` roda sem rede e sai **APROVADO** — 5
marcas, 33 modelos (28 publicaveis, 4 excluidos por nao serem robo, 1 a confirmar), 18
pecas, 33 pares declarados, 44 itens esperando link. O verificador ganhou **tres
invariantes** da versao 3 mais a **conferencia das contagens do cabecalho** de
`modelos-robo.json`, e **as seis quebras foram testadas de proposito numa copia**:
`divergencias` ausente, divergencia sem `resolucao`, divergencia apontando campo
inexistente, divergencia sem transcricao, `contagem.com_pa_declarado` mentindo e
`contagem.marcas_que_declaram_pa` mentindo. As seis reprovam alto. Verificador que nao
falha nao vale nada. Os sete sha256 do manifest foram recalculados e conferidos um a um.

**O que este bloco deliberadamente NAO fez:** nao gravou a bateria do S10, porque a busca
devolveu 3.200 mAh — exatamente o numero do S20 — e a Aquametria ja registrou busca
restrita devolvendo numero com atribuicao contaminada pelo vizinho de prateleira; nao
herdou autonomia nem bateria do S40 para o S40C, que declara METADE da succao e portanto
nao e o mesmo aparelho com outro acabamento; nao converteu W em Pa em nenhum modelo da
Multi; nao tratou os 10.000 Pa do S40 como numero de modo padrao (sao "no modo turbo e com
carga completa", e isso vai para a tela junto); e nao coletou imagem nenhuma, porque o
egresso segue fechado.

**Egresso medido nesta execucao:** `www.mi.com`, `loja.wap.ind.br`,
`mais.conteudo.wap.ind.br` (os manuais em PDF) e `static.positivocasainteligente.com.br`
(o guia rapido em PDF) devolveram EGRESS_BLOCKED, somando-se aos dominios ja medidos. Toda
a coleta saiu de busca restrita ao dominio oficial, com o canal declarado campo a campo.

**Itens esperando link de afiliado nesta ilha: 44** (28 modelos e 16 pecas), contra 35
antes. Pela secao 7 isso e trabalho pendente de verdade e nao compete com a fila da
Fundacao: quem gera link e a Sentinela estrategica, no navegador do Raphael, com teto de
calendario.

**Proximo passo desbloqueado:** continuar o 3c com o alvo novo — **Pa de marca que nao
seja Xiaomi acima de 3.000**, que resolve a faixa descoberta e a concentracao de marca de
uma vez; depois os manuais em PDF da WAP, que sao a porta de entrada do nivel 2; depois as
pecas da Xiaomi e da WAP com codigo, que a R1 precisa. A lacuna de m2 saiu da fila de
coleta de proposito: ela e fato de mercado, nao trabalho pendente. O bloco 3b (casca)
continua sendo o primeiro que depende do WordPress, que depende do certificado.

## 2026-09-10 — Bloco 3c, terceira leva: a entrada da R1 foi varrida, e a varredura reordenou a fila

**O que foi entregue** (manifest na revisao 6):

- `ferramentas/cobertura-r1.py` — implementacao de REFERENCIA da R1 e varredura da
  entrada dela de ponta a ponta. Roda sem rede e sem site: `python3
  ferramentas/cobertura-r1.py` imprime o relatorio, `--gravar` escreve os dois arquivos
  abaixo. Implementa num lugar so as regras que ate agora existiam apenas em prosa na
  especificacao: os tres selos da secao 1.3, o conjunto MAIS ESTREITO da secao 1.4, o
  aviso de variante de hardware, a recusa explicita do selo `nao_declarada` e o kit que
  responde por uma peca que o fabricante nao vende avulsa.
- `dados/cobertura-r1.json` — a medicao. 28 modelos publicaveis x 6 tipos consultaveis =
  168 celulas, em tres estados: `declarada` (41), `kit_sem_composicao` (11) e `vazia`
  (116).
- `dados/tabela-exemplos-r1.md` — a tabela de exemplos pre-renderizada da secao 5 do
  contrato, **gerada**: 45 linhas contra um minimo de 8, cada uma com o codigo, o selo e a
  data que o banco tem.
- `dados/pecas.json` — `lista_de_compras` reordenada pela medicao, com o criterio escrito
  em `ordem_da_lista_de_compras`. Nenhum registro de peca foi tocado.
- `dados/especificacao-calculadoras.md` — secao 1.2 (o seletor de tipo passa a ser gerado
  da varredura) e secao 1.7 (a tabela e gerada, nao digitada).
- `PROMPT.md` — fila do 3c reordenada, com o motivo medido de cada posicao.

**O ACHADO, e ele so aparece cruzando as duas varreduras.** A R1 responde em 15 dos 28
modelos publicaveis e sai VAZIA em 12. Cruzando com a R2 (que responde quando o modelo tem
`pa_declarado`): apenas **3 dos 28** modelos sao atendidos pelas DUAS ferramentas. A R2
atende 8 que a R1 nao atende (Xiaomi, WAP e o PRA500); a R1 atende 12 que a R2 nao atende
(Electrolux e Multi). A causa e a mesma nos dois sentidos e e de mercado: **Electrolux e
Multi publicam peca com compatibilidade declarada e nao publicam Pa; Xiaomi e WAP publicam
Pa e nao publicam peca com codigo.**

**Por que isso custa dinheiro:** a ilha ganha a visita pela R2 ("quantos Pa para pelo de
cachorro"), que na faixa alta so consegue recomendar Xiaomi. Quem compra volta meses depois
procurando o filtro daquele robo — a consulta de maior intencao de compra do nicho, e a
razao de a R1 existir — e recebe "nao localizamos declaracao do fabricante". As duas
ferramentas nao se entregam a visita uma para a outra. **O funil esta partido na emenda**, e
nenhuma das duas medicoes isoladas mostrava a emenda.

**O que a medicao mudou de posicao:** "pecas da Xiaomi e da WAP com codigo" estava em
ULTIMO lugar entre os alvos de coleta e passou a PRIMEIRO. Dois motivos medidos: e o unico
lado da emenda que da para colher (o lado simetrico — Pa da Electrolux e da Multi — ja foi
medido como inexistente no mercado brasileiro), e sao exatamente os 8 modelos que a R2 ja
recomenda, entao o retorno chega na visita que a ilha ja sabe atrair.

**O que a implementacao de referencia pegou antes de ir para a tela.** Rodar as regras da
especificacao contra o banco de verdade produziu duas frases quebradas: "ele vem dentro do
**sem codigo publicado**", quando o fabricante nao publica codigo de peca, e "nao vende
**escova lateral avulso**", sem concordancia de genero. As duas teriam nascido dentro do PHP
do Bloco 4, num snippet que so da para testar com o site no ar. Escrever a regra onde ela
pode ser conferida saiu mais barato do que escreve-la onde ela nao pode — e e por isso que a
saida do PHP da R1 tera que BATER com a saida deste arquivo.

**Duas decisoes que esta leva fixa:**

1. **O seletor de tipo de peca da R1 e gerado da varredura, nunca digitado.** O tipo
   `reservatorio` tem ZERO pecas no banco inteiro; oferece-lo e oferecer uma escolha que
   sempre devolve recusa, contra a promessa antes do formulario (secao 6 do contrato). Ele
   volta ao seletor no dia em que a primeira peca dele entrar.
2. **A pagina-ancora da R1 NAO pode ser a do PRA500** enquanto nao houver peca declarada
   para ele. O PRA500 e literalmente a consulta-alvo da secao 1.1 da especificacao, e a R1
   sai vazia nele: as tres pecas da Positivo no banco declaram PRA800 e PRA2000 e nao o
   citam. Pelo conjunto mais estreito a recusa e a resposta CERTA — mas estrear a
   ferramenta com um "nao sabemos" na propria consulta-alvo seria escolha errada de pagina.

**O que esta leva deliberadamente NAO fez, e por que.**

- **Nao coletou nada, e isso foi medido.** A busca web devolveu `unavailable` em tres
  consultas seguidas e o `WebFetch` devolveu `EGRESS_BLOCKED` em `www.wap.ind.br`,
  `www.positivocasainteligente.com.br` e `global.roborock.com`. Nenhum dado tecnico novo
  entrou no banco e nenhum numero desta leva vem de fora do repositorio. Isso NAO e
  `bloqueada_por` (que e para dependencia humana): e uma execucao em que a coleta nao
  estava disponivel, e a resposta certa foi medir o que o banco ja tem em vez de deixar a
  execucao passar em branco ou escrever numero de memoria.
- **Nao aplicou o portao de 3 itens da secao 9 a R1.** Na R2 a faixa produz uma lista de
  produtos concorrentes e tres e o minimo honesto; na R1 a resposta certa costuma ser UMA
  peca, a que o fabricante declarou, e exigir tres levaria a ilha a inventar concorrente
  onde o fabricante tem uma peca so. O criterio da R1 e binario e mais duro: a celula
  responde ou nao responde.
- **Nao escreveu snippet PHP.** O bloco 3b e o 4 dependem do WordPress, que depende do
  certificado, que continua pendente.

**Verificacao feita:** `python3 ferramentas/validar-banco.py` APROVADO depois das mudancas
(5 marcas, 33 modelos, 18 pecas, 33 pares, os mesmos 2 avisos conhecidos de variante de
hardware). Os numeros da varredura foram conferidos na mao em seis modelos — `multi-ho041`,
`electrolux-erb10`, `electrolux-erb44`, `electrolux-erb30`, `positivo-pra500` e
`xiaomi-s20` — lendo resposta por resposta. As frases publicadas foram lidas uma a uma, e
foi assim que os dois defeitos de texto apareceram. Os `sha256` do manifest foram
recalculados a partir dos arquivos no disco: so os dois arquivos alterados mudaram de
hash, o que confirma que nenhum registro do banco foi tocado.

**Itens esperando link de afiliado: 44** (28 modelos e 16 pecas) — continua em 44, porque
esta leva nao acrescentou item ao banco.

**Proximo passo desbloqueado: bloco 3c, alvo (a) — pecas com codigo da Xiaomi (S10, S40,
S40C, H40, E10, Mop 2) e da WAP (W400, W1000, W310)**, na primeira execucao em que a rede
responder. Antes de colher, rodar `python3 ferramentas/cobertura-r1.py` e
`ferramentas/validar-banco.py`: as duas varreduras sao o que separa "acrescentei um item"
de "tirei uma entrada do vazio".

---

## 2026-09-10, 13h19Z — Bloco 3b: a CASCA DO SITE existe, e o site deixou de ser WordPress padrao

**Ilha reservada** pela regra da secao 1 do `ARQUIPELAGO.md`: a Robometria tinha o
`ultima_execucao` mais antigo (11h28Z contra 11h37Z da Aquametria), a reserva foi commitada
sozinha e o push passou de primeira. Nenhuma outra execucao disputou.

**O que foi entregue: `snippets/robometria-casca.php` v1.0.0, `publicar: true`.** E o
PRIMEIRO item desta ilha marcado para ir ao ar — ate hoje o manifest inteiro era pesquisa
com `publicar: false`. Manifest na **revisao 7**.

A casca faz oito coisas, e cada uma responde a uma regra do contrato, nao a gosto:

1. **Identidade sobre o tema ativo** — paleta grafite `#16191D` / varredura `#CC3311` /
   piso `#F2F1EF`, Archivo nos titulos, IBM Plex Sans no texto e IBM Plex Mono com
   `tabular-nums` em **todo** numero, unidade e codigo de peca. Texto corrido nunca em
   Mono, e por isso a citacao em bloco desta ilha ficou no tipo de texto — ao contrario da
   casca da Aquametria, onde ela e monoespacada. Copiar aquela regra teria posto texto
   corrido em Mono nesta ilha.
2. **O logotipo e o ENCAIXE, nao o robo** — anel aberto de raio 15 com corte de 50 graus a
   direita e a peca de lingueta entrando no corte, em SVG inline. Wordmark ROBO em 700
   colado a METRIA em 400.
3. **Menu hamburgueres pela regra da secao 6** — `<button>` com `aria-expanded` e
   `aria-controls`, e os tres links SEMPRE no HTML servido dentro de `<nav>`. Quem esconde
   a lista no celular e um seletor que depende de um atributo posto pelo JavaScript do
   rodape: sem JavaScript o menu nao some, e e essa a versao que o crawler de IA le.
4. **Favicon proprio no lugar do icone do WordPress** (`remove_action` do `wp_site_icon`),
   como data URI: SVG na aba, PNG de 32 px como alternativa e PNG de 180 px para o iOS.
   Nada sobe para a biblioteca de midia. O desenho e GERADO por
   `ferramentas/gerar-favicon.php` a partir da mesma geometria do logotipo, entre os
   marcadores `FAVICON-INICIO` e `FAVICON-FIM` — desenho mantido em dois lugares diverge
   em silencio.
5. **Cinco paginas** com o conteudo em shortcode do proprio snippet: inicio, ferramentas,
   metodologia, sobre e **divulgacao-de-afiliados**. A quinta nasceu junto de proposito:
   pela secao 7 do contrato o aviso de comissao precisa estar publicado ANTES do primeiro
   link, nao depois — e hoje ela diz, com essas palavras, que ainda nao ha nenhum link de
   afiliado no ar.
6. **"Hello world" e "Sample page" para a LIXEIRA.** Nesta ilha isso nao e acabamento:
   sao esses dois itens que o sitemap submetido ao Search Console em 10/09/2026 lista, e
   sitemap e curadoria, nao inventario (secao 14.1). Pagina de amostra gasta orcamento de
   rastreamento de dominio novo ensinando ao robo que aqui se publica coisa que nao vale
   voltar para buscar.
7. **JSON-LD Organization + WebSite em toda pagina** (secao 5.3), **sem `sameAs`**. A ilha
   nao tem perfil externo nenhum, e `sameAs` apontando para perfil inventado seria
   exatamente a fabricacao que esta ilha existe para nao cometer. Ele entra no dia em que
   houver perfil de verdade — e o teste reprova se aparecer antes disso.
8. **Rodape proprio no lugar da template part do tema**, com rede de seguranca em
   `wp_footer` e no CSS, para nao ficarem dois rodapes empilhados.

**A pagina de metodologia publica a nossa propria cobertura, inclusive a parte
desconfortavel.** Ela diz que a ferramenta de pecas responde em **15 dos 28** modelos e sai
vazia em **12**; que **116 das 168** combinacoes modelo x tipo de peca nao tem declaracao
localizada; e que a ilha **nao tem nenhuma fonte de nivel 1 nem de nivel 2** — esta inteira
apoiada nos niveis 3 e 4. Nenhum desses numeros e enfeite de transparencia: sao a medicao
da terceira leva do 3c, servidos em HTML, e um comparador que nunca diz "nao sei" esta
inventando em algum lugar. **Nenhum numero da tela foi digitado**: todos saem do banco
commitado, e o teste reprova se divergirem dele.

**VERIFICACAO — o que foi medido, e o que NAO da para medir daqui.**

Feito: `php -l` nos tres arquivos PHP; **`ferramentas/teste-casca.php` APROVADO em 59
medicoes**; e a conferencia do menu num Chromium de verdade (a 390 px o botao aparece, a
lista comeca escondida, o clique abre e o `aria-expanded` vira `true`, Escape fecha; a
360 px a rolagem horizontal e de 0 px; nenhum erro de console vindo do nosso codigo).

O `teste-casca.php` existe porque a nuvem **nao alcanca** robometria.com.br — a
alternativa a ele seria marcar `publicar: true` por fe. Ele mede, entre outras coisas:
nenhum `<script>`/`<style>` dentro do retorno dos cinco shortcodes; **zero `&#038;` dentro
dos blocos `<script>`**, contando so os blocos e nunca a pagina inteira, que e o teste
ERRADO; `aria-controls` apontando para um id que existe mesmo; o icone do WordPress
removido; JSON-LD que decodifica; nenhuma cor fora da paleta e nenhum gradiente no CSS; a
varredura ausente do corpo, porque e cor de sinal de um uso por tela; e cada numero da
tela conferido contra o banco.

**Ele ja rendeu na primeira rodada, e o defeito era invisivel:** o snippet trazia o nome da
superglobal de servidor escrito DENTRO de um comentario que explicava por que nao se deve
usa-la. O ModSecurity desta hospedagem casa a string do mesmo jeito, comentario ou nao, e a
gravacao do snippet teria falhado **em silencio** no wp-admin. O comentario foi reescrito.

**NAO da para medir daqui, e por isso o bloco NAO esta no ar:** o Sync e acionado pela
Sentinela, no navegador do Raphael (secao 4 do contrato). Enquanto ele nao rodar, o
repositorio esta na revisao 7 e o site na 6 — que e exatamente o buraco que a secao 4
descreve. **"Aplicado com sucesso" no log do Sync tambem nao seria evidencia**: o que fecha
o 3b e o `/status` responder revisao 7.

**O que este bloco deliberadamente NAO fez.**

- **Nao escreveu ferramenta.** O Bloco 4 (a R1) e outra execucao. A casca entrega o hub com
  os dois cartoes em "Em construcao", e o cartao so vira link quando a pagina existir
  publicada de verdade — a trava que a Aquametria so ganhou depois de publicar um 404 em
  08/09/2026.
- **Nao inventou `sameAs`, nem perfil, nem numero.** Onde nao havia dado, a pagina diz o
  que falta.
- **Nao coletou.** Nao era o bloco.

**Itens esperando link de afiliado: 44** (28 modelos e 16 pecas) — continua em 44, porque a
casca nao acrescenta item ao banco.

**Proximo passo desbloqueado, em duas frentes que nao competem:**

1. **Para a Sentinela, no navegador:** acionar o Sync
   (`https://robometria.com.br/?robometria_sync=<token>&forcar=1`) e conferir no
   `/wp-json/robometria/v1/status` que a revisao aplicada e **7**. So entao a casca esta no
   ar, e so entao o sitemap para de listar "Hello world".
2. **Para a Fundacao, na proxima execucao:** o **Bloco 4 — a ferramenta R1**, agora que a
   casca existe para recebe-la; a implementacao de referencia `ferramentas/cobertura-r1.py`
   ja tem as regras e a saida do PHP tem que BATER com a dela. Alternativa, se a rede
   responder: o **3c alvo (a)** — pecas com codigo da Xiaomi (S10, S40, S40C, H40, E10,
   Mop 2) e da WAP (W400, W1000, W310), que e o unico lado coletavel da emenda entre as
   duas ferramentas. **Atencao ao que a varredura ja avisou:** a pagina-ancora da R1 NAO
   pode ser a do PRA500, porque a R1 sai vazia nele.

## 2026-09-10 (15h16Z) — Blocos 4 e 4e: A FERRAMENTA R1 EXISTE, e esta no ar

**A primeira ferramenta desta ilha.** `snippets/robometria-r1.php` v1.0.0 mais
`ferramentas/gerar-r1.py`, `ferramentas/teste-r1.php`, `dados/r1-respostas.json`
(o combustivel, `publicar: true`) e `dados/r1-referencia.json` (o gabarito,
`publicar: false`). Manifest na revisao 8, e depois na 9 pelo despacho da
Sentinela que chegou no meio desta execucao.

**O que ela responde.** Dado um dos 28 modelos publicaveis do banco, ela diz
qual filtro, escova lateral, escova principal, mop ou bateria o FABRICANTE
declarou compativel — com o codigo, o conjunto de modelos que ele citou, o
endereco da declaracao e a data. Onde nao ha declaracao, recusa com todas as
letras: "nao localizamos declaracao do fabricante de X para este modelo; nao
vamos supor." Sao 45 pares peca x modelo respondidos e 12 modelos em que ela sai
vazia, e os 12 estao publicados na propria pagina, com os nomes.

**A DECISAO QUE MAIS IMPORTA: a resposta e servida pelo SERVIDOR.** O formulario
e um GET para a propria pagina e quem monta a resposta e o PHP. Sem JavaScript a
ferramenta funciona por completo. Isso e a secao 5 do contrato levada a serio em
vez de contornada: calculadora que so calcula no navegador mostra a um modelo de
linguagem um formulario vazio, nunca um numero. Aqui, sem clique nenhum, ja saem
no HTML servido a resposta inteira do modelo-ancora, as 45 linhas da tabela
pre-renderizada e a lista dos modelos sem resposta.

**O modelo-ancora e escolhido por REGRA, nunca a dedo** (mais tipos cobertos,
depois mais itens, depois ordem alfabetica; hoje da `electrolux-erb60`). Duas
consequencias: a ancora acompanha o banco sozinha quando a coleta melhorar outro
modelo, e a regra impede sozinha o erro que a varredura da terceira leva do 3c
tinha registrado — o PRA500 e a consulta-alvo escrita na especificacao e a R1
sai VAZIA nele, entao estrear a ferramenta com ele seria estrear com um "nao
sabemos".

**AS REGRAS NAO FORAM REESCRITAS EM PHP, E ISSO E MEDIDO.**
`ferramentas/gerar-r1.py` importa a implementacao de referencia
(`cobertura-r1.py`) e deriva dela os FATOS que o site consome; o snippet escreve
a frase, em portugues acentuado, porque o banco desta ilha e ASCII e texto de
tela sai acentuado. `ferramentas/teste-r1.php` compara **as 188 frases** das
duas implementacoes, modelo a modelo, ignorando acento e aplicando dos dois
lados a mesma tabela de rotulos de origem. As duas nao batem por sorte: batem
por construcao, e o teste reprova se alguem mexer no molde de um lado so.

**LER A RESPOSTA COMO UM LEITOR LE PEGOU DOIS DEFEITOS QUE REGRA OBJETIVA NAO
PEGA** — e os dois foram consertados na REFERENCIA, que e a fonte, e nao no PHP:

1. **A pagina se contradizia na mesma tela.** Para o ERB60 ela dizia "a
   Electrolux declara o filtro [HEPA com espuma] compativel com o ERB60" e, na
   frase seguinte, "a Electrolux **nao vende o filtro avulso** para este
   modelo". As duas frases eram verdadeiras isoladamente e falsas juntas: "nao
   vende avulso" e uma afirmacao sobre o CATALOGO INTEIRO daquele modelo, entao
   so pode ser escrita quando nenhuma peca avulsa daquele tipo responde por ele.
   Onde existe a avulsa, o kit passou a ser um caminho A MAIS: "ele tambem vem
   dentro do kit ...". Este e exatamente o defeito de julgamento que a secao 12
   do contrato descreve — verificacao por regra objetiva pega encanamento, e
   contradicao so aparece lendo o resultado como um leitor leria.
2. **O aviso de variante de hardware colava duas frases sem pontuacao**, e a
   segunda comecava em minuscula porque era texto do banco. Virou dois pontos,
   com o ponto final que faltava antes de "Confira a etiqueta".

**A vitrine (Bloco 4e) nasceu junto**, como a secao 6 manda. Carrossel com
`scroll-snap` em CSS puro, sem biblioteca; UM cartao por peca e nao por par, que
foi decisao de leitura (o Kit Performance responde filtro, mop e escova lateral
do mesmo modelo, e tres cartoes identicos seriam tres vezes o mesmo conselho);
peca sem imagem NAO some, entra com espaco reservado neutro; e peca sem link de
loja **diz que nao tem link** em vez de mostrar botao fingido. O link do cartao
leva ao endereco da declaracao, que e o que esta pagina tem de mais valioso hoje.

**Consulta nao vira URL indexavel.** Endereco com `?modelo=` sai com
`noindex,follow` e canonica para a pagina limpa. Sao 196 combinacoes de modelo x
tipo, e cada URL fraca gasta orcamento de rastreamento que uma pagina boa
precisaria (secao 14.1). O que merece indexar — a ancora e a tabela inteira —
esta na pagina limpa, e o teste confere que a pagina limpa NAO leva noindex.

**VERIFICACAO — o que foi medido.**

De bancada, sem site: `php -l` nos dois snippets; **`teste-r1.php` APROVADO em 70
medicoes** (entre elas as 188 frases contra a referencia, zero `<script>` e
`<style>` no retorno do shortcode em cinco estados da pagina, zero `&#038;`
dentro dos blocos `<script>`, o seletor sem o tipo que o banco nao responde,
declaracao de terceiro nunca antes da do fabricante, JSON-LD que decodifica com
toda resposta do FAQPage conferida contra o que a pagina serve, e os numeros da
tela contra o banco commitado); `teste-casca.php` APROVADO em 64;
`validar-banco.py` aprovado.

Num Chromium de verdade: rolagem horizontal **0 px a 360, 390, 782 e 1200**,
botao do menu visivel ate 782 e ausente a 1200, `aria-expanded` false -> true no
clique e -> false no Escape, barra fixa do celular so enquanto o resultado esta
fora da tela, console limpo. **A primeira medicao acusou 39 px de rolagem
horizontal a 360 px** — o item de flex do formulario recebia `min-width:auto` e
a largura intrinseca do `<select>` (o maior rotulo de optgroup) mandava. Sem a
medicao no navegador, isso teria ido para o ar.

No ar, depois do Sync acionado por esta execucao: `/status` responde **revisao
8**, a pagina `qual-peca-serve-no-meu-robo-aspirador` devolve **200**, serve as
45 linhas da tabela, a resposta-ancora inteira, o formulario GET, JSON-LD
WebApplication + FAQPage, favicon proprio e **zero `&#038;` dentro dos blocos
`<script>`** (a pagina inteira tem 4, e contar ali seria o teste ERRADO). Uma
consulta real (`?modelo=multi-ho041&peca=bateria`) devolve as duas baterias com
o aviso de variante e sai com `noindex,follow` e canonica para a pagina limpa.

**Itens esperando link de afiliado: 44** (28 modelos e 16 pecas) — continua em
44, porque este bloco nao acrescentou item ao banco. Dos 45 itens de resposta que
a R1 serve hoje, os 45 esperam link.

## 2026-09-10 (15h16Z) — Despacho da Sentinela, item 1 cumprido: o sitemap deixa de responder 404

O despacho chegou ao `main` as 15h36Z, no meio desta execucao. Pela secao 12.2 do
contrato ele tem prioridade sobre a fila, e defeito no ar custa mais que bloco
atrasado — entao foi atacado na mesma execucao, depois de o bloco 4 estar no ar.

**O sintoma era esquisito e por isso instrutivo:** `wp-sitemap.xml` e
`wp-sitemap-posts-page-1.xml` serviam XML **valido**, com as seis paginas
dentro, e status HTTP **404**. Para o Google, sitemap com 404 e sitemap
inexistente — era isso que estava por tras do "Nao foi possivel buscar" no
Search Console, e era isso que travava a rampa de indexacao, que e a prioridade
maxima desta ilha.

**A causa nasce na propria casca, e nao no nucleo nem na hospedagem.** Como a
casca manda "Hello world!" para a lixeira — de proposito, porque sitemap e
curadoria e nao inventario (secao 14.1) —, esta ilha fica com **ZERO posts
publicados**. As rotas de sitemap do WordPress passam pela consulta principal
(`index.php?sitemap=...`), a consulta volta sem nenhum post, e o `handle_404()`
do nucleo carimba 404 ANTES de o renderizador de sitemap imprimir o XML. A
Aquametria devolve 200 nos mesmos caminhos pelo motivo simetrico: ela tem posts.

**O conserto fica ao lado da causa e nao desliga nada:** o filtro
`pre_handle_404`, que existe no proprio nucleo para isto, e que age SO em
requisicao que ja e de sitemap. Endereco inexistente continua podendo 404 —
um filtro que dissesse "nunca 404" faria a ilha responder 200 no vazio, e isso
seria pior do que o defeito. Casca na versao 1.0.1, manifest na revisao 9.

O `teste-casca.php` passou a medir os cinco casos do filtro (indice de sitemap,
sitemap de paginas, pagina comum, endereco inexistente e consulta ausente).

**O que fecha o item 1 e o curl no ar**, e esta registrado abaixo, na secao de
verificacao desta execucao. **O que NAO da para fazer daqui: reenviar o sitemap
no Search Console.** Isso e propriedade da conta do Raphael e exige o navegador
dele ou credencial de conta de servico que este ambiente ainda nao tem — fica
como a metade humana do item 1.

**MEDIDO NO AR depois do Sync da revisão 9 (10/09/2026, 15h49Z):**
`wp-sitemap.xml` → **200** (antes 404), `wp-sitemap-posts-page-1.xml` → **200**
(antes 404), `/pagina-que-nao-existe-mesmo/` → **404** (o conserto não vazou
para endereço comum, que era o risco), `/status` → **revisão 9**.
`wp-sitemap-posts-post-1.xml` segue 404, e está certo: esta ilha não tem post
nenhum, e ele não aparece no índice.

**Próximo passo desbloqueado: Bloco 5 — o artigo-âncora pareado com a R1.** Ele
é o que dá à ferramenta a segunda listagem e as três irmãs que a regra da malha
exige, e não depende de rede. Depois dele, o **3c alvo (a)** (peça com código da
Xiaomi e da WAP), na primeira execução em que a rede alcançar o fabricante —
nesta ela não alcançou: `www.wap.ind.br`, `mais.conteudo.wap.ind.br`,
`www.mi.com` e `www.xiaomi.com.br` não responderam. **Nenhuma leva de malha
(5b)** antes de o Search Console voltar a buscar o sitemap.

## 2026-09-10 (17h17Z) — Despacho da Sentinela, item 0 cumprido: a procedencia deixa de ser a unica porta de compra

**O defeito, medido pela Sentinela na vespera do conserto:** na URL
`/qual-peca-serve-no-meu-robo-aspirador/?modelo=electrolux-erb30&peca=filtro`, 12
links externos, todos para loja do fabricante (loja.electrolux.com.br,
meupositivo, multilaser, mi.com), e **zero link de afiliado, zero bloco de
compra**. A R1 tinha nascido impecavel de procedencia — cada afirmacao com
publicador, endereco e data — e, exatamente por isso, com uma unica porta
clicavel por peca: a loja de quem fabrica. Quem decidia comprar clicava nela,
porque nao havia outra. A ilha mandava a venda de graca para a Electrolux.

Esta e a cicatriz que virou a regra "PROCEDENCIA NUNCA E A UNICA PORTA DE
COMPRA" na secao 7 do `ARQUIPELAGO.md`, e vale para toda ilha. O que esta
execucao fez foi cumpri-la na ferramenta que a produziu.

### O que mudou (R1 v1.1.0, manifest revisao 10)

1. **O bloco de compra vem ANTES da prova de procedencia**, na mesma resposta. A
   vitrine virou o bloco "Onde comprar estas pecas", e o aviso de comissao esta
   DENTRO dele — quem ve o botao ve o aviso sem rolar, e nao so no rodape.
2. **A procedencia fica, e fica discreta.** Ela e o que da a esta ilha o direito
   de afirmar compatibilidade, entao nao sai da pagina; o que muda e o peso.
   Texto "fonte", `rel="nofollow noopener"`, nunca um botao — e o CSS nao lhe da
   fundo nem preenchimento, medido no proprio teste, porque o desenho e que
   fazia dela a porta de compra, nao so o texto.
3. **O bloco existe mesmo sem link de afiliado.** Reserva o lugar, escreve "Link
   de loja em breve" e a pagina publica quantas pecas estao esperando. Esconder
   o bloco ate o link chegar devolveria a procedencia ao papel de unica porta
   clicavel durante todas as semanas em que o cano de links esta enchendo — que
   e o defeito de novo, so que com data marcada para voltar.
4. **Link de afiliado sai com `rel="sponsored nofollow noopener"`** e nomeia a
   loja para quem vai clicar. Nenhum existe ainda no banco desta ilha; o caminho
   e medido com item sintetico, na funcao que monta o cartao.
5. **Modelo sem declaracao de fabricante nao ganha bloco de compra — e a pagina
   DIZ por que:** "nos ganhamos comissao quando alguem compra por um link nosso,
   e e exatamente por isso que ele nao pode aparecer aqui". Silencio no lugar do
   bloco parece defeito de pagina; a recusa explicada e conteudo.

O campo `afiliado` passou a viajar como FATO em `dados/r1-respostas.json`
(`ferramentas/gerar-r1.py`), e nao como decisao do PHP — mesmo desenho das
outras regras da R1: quem decide mora onde da para conferir sem site.

### O KIT QUE FICOU DE FORA, de proposito

Na consulta do despacho (ERB30 + filtro) a resposta cita um Kit Performance que
a Electrolux **declara** compativel com aquele modelo, e ainda assim a pagina nao
oferece porta de compra para ele. Nao e esquecimento: a lista do que vem dentro
do kit nao foi transcrita, entao a pagina nao sabe se ele contem filtro. Vender
o kit debaixo da pergunta "qual filtro serve no meu robo" seria recomendar em
primeiro lugar um produto que a propria pagina diz nao saber se serve — o defeito
GRAVE da secao 7, com a agravante de ser o defeito que rende comissao.
**A destravar por DADO, nao por regra:** transcrever a composicao dos kits na
proxima leva do 3c abre a porta de compra sozinha, sem afrouxar nada.

### Verificacao (secao 8 do contrato)

- `php -l` limpo; `teste-r1.php` **APROVADO em 90 medicoes** (eram 70), sendo a
  secao 13 inteira nova e so sobre este item: 48 links externos conferidos um a
  um com `nofollow` e `noopener`, o texto do link de fonte sendo sempre "fonte"
  e nada alem, a ordem compra -> fonte na pagina E dentro de cada um dos 3
  cartoes, o CSS da fonte sem fundo nem preenchimento, o caminho com
  `afiliado.url` preenchido saindo com `sponsored`, e o modelo de entrada vazia
  sem bloco e com a frase que explica. As **188 frases** continuam batendo com a
  implementacao de referencia.
- `teste-casca.php` APROVADO em 64; `validar-banco.py` APROVADO.
- **NO AR e medido pela nuvem, revisao 10 confirmada no `/status`** (Sync
  acionado as 17h25Z pela propria Fundacao): pagina limpa **HTTP 200**, **zero
  `&#038;` dentro dos blocos `<script>`**, **48 links externos e ZERO sem
  `nofollow`**, o bloco de compra servido antes da primeira fonte, "Link de loja
  em breve" nos 3 cartoes e o aviso de comissao no HTML servido. **Na URL exata
  do despacho** (`?modelo=electrolux-erb30&peca=filtro`): HTTP 200, 45 links
  externos, **zero sem `nofollow`**, `noindex,follow` mantido, nenhum bloco de
  compra e a explicacao de por que ele nao esta ali.

### O numero que e trabalho pendente

**14 pecas recomendadas na tela, 14 esperando link de afiliado** (o banco tem 16
publicaveis, 16 sem link). Gerar link e da Sentinela estrategica, no navegador do
Raphael, com teto de calendario — nao consome execucao da Fundacao e nao compete
por esta fila. Enquanto nao houver nenhum, cada cartao da ferramenta reserva o
lugar em vez de fingir um botao.

**Proximo passo desbloqueado: Bloco 5 — o artigo-ancora pareado com a R1**, que
da a ela a segunda listagem e as tres irmas da regra da malha, e nao depende de
rede. Nenhuma leva de malha (5b) antes de o Search Console voltar a buscar o
sitemap — metade humana do item 1 do despacho, ainda aberta.
