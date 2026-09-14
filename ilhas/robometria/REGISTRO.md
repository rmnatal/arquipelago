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

## 2026-09-10 21h15Z — Bloco 5: o ARTIGO-ANCORA da R1 existe, e a malha da ilha fechou

Entregue: `snippets/robometria-a1.php` v1.0.0 — a pagina **"Por que nao existe
filtro universal de robo aspirador"**, em
`/filtro-universal-de-robo-aspirador/` —, mais `ferramentas/gerar-a1.py`,
`dados/a1-fatos.json` (o combustivel, `publicar: true`) e
`ferramentas/teste-a1.php` (53 medicoes). A casca subiu para **1.0.2** e a R1
para **1.1.1**. Manifest na **revisao 11**.

**Por que este assunto, e nao um guia de compra.** O corpus desta ilha (cluster
A1) registrou uma consulta de sinal invertido: "filtro hepa universal robo
aspirador". Quem digita isso esta prestes a comprar a peca errada, e a unica
pagina do nicho que hoje avisa contra ela avisa *sem dado* — "os encaixes sao
diferentes", sem contar nada. A Robometria tem o catalogo dos fabricantes
transcrito, entao aqui a mesma frase virou medicao. E a medicao e mais dura do
que o aviso generico:

- das **16** pecas com compatibilidade declarada, **nenhuma** e declarada para
  modelos de mais de uma marca;
- a lista mais longa do banco inteiro nomeia **5** codigos de modelo (a escova
  lateral Multi PR10124), e para dentro de uma marca so;
- **e nao se herda nem dentro da marca**: as 6 pecas da Electrolux formam **6
  conjuntos de modelos diferentes** — nenhuma repete a lista de outra. Esse e o
  achado que o artigo tem e o aviso generico nao tem, e e o que pega quem compra
  por semelhanca dentro do proprio catalogo.

**A TESE NAO ESTA DIGITADA NO HTML, e essa foi a decisao de desenho do bloco.**
Um artigo cuja tese e um numero nao pode ter esse numero dentro do texto: no dia
em que o banco crescer e uma peca atravessar marca, a pagina passaria a mentir em
silencio. Entao a frase de abertura, a `description` do JSON-LD e a resposta do
FAQPage tem **duas formas**, escolhidas pela contagem — foi medido numa copia do
banco com uma peca multimarca plantada de proposito, e as tres mudaram juntas.

**E o defeito que so apareceu por causa dessa prova:** na primeira versao a
pagina visivel ja se corrigia e o **JSON-LD continuava afirmando o que deixou de
valer**. Numa ilha cuja seccao 5 diz que ser recomendado pela IA vale tanto
quanto ranquear, contradizer-se justamente no canal que a IA le e pior do que se
contradizer na tela. Corrigido antes do desembarque, nos dois lados.

**A malha da secao 9 fechou nos dois sentidos.** A casca ganhou um **catalogo de
artigos**, alimentado por filtro como o de ferramentas, e o artigo aparece na
**home** e no **hub de ferramentas** (as duas listagens). Ele aponta para tres
irmas — a R1, a metodologia e a divulgacao de afiliados — e a **R1 aponta de
volta**, na secao "Leia tambem": sem os dois sentidos, o artigo-ancora seria um
beco. Cinco apelidos 301 novos levam as formulacoes reais da busca
("filtro-hepa-universal", "peca-universal-robo-aspirador") ao endereco canonico.

**Secao 7 desde o nascimento, sem retrofit.** O bloco de compra com 4 itens de
banco reais vem ANTES da prova de procedencia, o aviso de comissao esta dentro
dele, os 4 reservam o lugar com "link de loja em breve", e a procedencia e link
de texto "fonte" com `rel="nofollow noopener"`. O Kit Performance ERB44 e o ERB30
**ficaram de fora da vitrine de proposito**: a composicao deles nao foi
transcrita, e oferecer a compra de um produto cuja composicao a propria pagina
diz nao conhecer e exatamente o defeito da secao 7. O teste reprova se um deles
voltar.

**A folha da porta de compra passou a ter um dono so.** As regras do botao de
compra, do lugar reservado e do link discreto de procedencia sairam da R1 e
foram para a casca (`robometria_casca_css_vitrine`,
`robometria_casca_porta_de_compra`, `robometria_casca_rotulo_da_loja`,
`robometria_casca_fonte_link`), e a R1 delega. Com uma copia por pagina,
bastaria alguem ajustar uma delas para a ilha voltar — numa pagina so, e sem
ninguem notar — ao defeito de 10/09/2026.

**Verificacao (secao 8).** `php -l` nos tres snippets; `teste-a1.php` **APROVADO
em 53 medicoes**, entre elas a **recontagem da tese em PHP, direto do banco, sem
olhar para o que o gerador em Python escreveu**; `teste-casca.php` APROVADO em 64
e `teste-r1.php` APROVADO em 90 (nenhuma frase de resposta da R1 mudou);
`validar-banco.py` APROVADO. As travas novas foram testadas quebrando o banco de
proposito numa copia, para provar que reprovam: numeros adulterados nos fatos
reprovaram 3 medicoes, e a peca multimarca plantada reprovou a trava da tese.
Medicao num Chromium de verdade a 360, 390, 782 e 1200 px: **rolagem horizontal
da pagina 0 px em todas**, com as tabelas de 5 colunas rolando dentro do proprio
envoltorio e a vitrine com `scroll-snap` em CSS puro.

**NO AR, e conferido no ar (secao 4).** Sync acionado por esta execucao as
**21h36Z**: `revisao 11`, 5 itens aplicados, `robometria-a1` criado como snippet
**#8**, casca (#6) e R1 (#7) atualizados. O `/status` responde **revisao 11**.
Medido na pagina publicada: **HTTP 200**, **zero `&#038;` dentro dos blocos
`<script>`**, JSON-LD **Article + FAQPage** decodificando, canonica propria,
**4 links externos e nenhum sem `nofollow` e `noopener`**, e o bloco de compra
antes da primeira prova de procedencia. A malha conferida no ar: a **home** e o
**hub** listam o artigo, a **R1 aponta de volta**, o apelido
`/filtro-hepa-universal/` devolve **301** para o endereco canonico, e o
`wp-sitemap-posts-page-1.xml` passou a listar **7** paginas, com o artigo entre
elas.

**16 pecas do banco esperando link de afiliado** (44 itens contando modelos, que
e como o `validar-banco.py` conta) — trabalho da Sentinela estrategica, no
navegador do Raphael, nao da Fundacao.

- **Proximo passo: Bloco 3c, alvo (a)** — pecas com codigo da Xiaomi e da WAP, o
  unico lado coletavel da emenda partida entre a R1 e a R2, **se a rede alcancar
  o fabricante**. Se nao alcancar, o proximo e a **R2**, que ja tem as cinco
  decisoes de desenho definidas pela R1 e ainda nao tem implementacao de
  referencia.

## 2026-09-11 (00h07Z) — Bloco 5: o ARTIGO-ANCORA da R2, e o acento que faltava no A1

- **NO AR** em `https://robometria.com.br/quantos-m2-o-robo-aspirador-limpa-por-carga/`
  (`snippets/robometria-a2.php` v1.0.0, manifest **revisao 13** conferida no
  `/status`, snippet #10 criado). Sitemap com **9 paginas**, home e hub listando
  os DOIS artigos, e a malha da secao 9 fechada: o A2 aponta para a R2, para a R1
  e para o A1, e as tres apontam de volta.
- Segundo bloco da mesma execucao (mutirao da secao 13 do contrato): a R2 passou
  pela verificacao da secao 8 inteira e foi registrada **antes** de este comecar.
- Nenhuma coleta: a rede continua sem alcancar fabricante nenhum. Todo numero do
  artigo sai do banco ja commitado.

### A tese, e por que ela nao esta digitada

O artigo nao repete a ferramenta (decisao 3 do bloco 5): a R2 calcula a casa da
pessoa, este texto conta o CATALOGO e responde a pergunta anterior — **de onde
vem o numero de m2 que os sites publicam.** Tres afirmacoes, as tres derivadas:

1. **Uma marca so declara area por carga** — a Electrolux, em 5 dos 28 modelos.
   As outras 4 nao publicam o numero em canal nenhum.
2. **A conta de tempo precisa de tres numeros e nenhum modelo tem os tres.** 5
   declaram a area, 2 declaram a recarga, e os dois conjuntos nao se encontram.
3. **Os pares declarados discordam entre si:** 1,35 a 1,66 m2 por minuto, 23% de
   diferenca dentro da MESMA marca.

Cada uma tem mais de um molde, escolhido pela contagem. E **a prova de que sao
derivadas roda dentro do teste, toda vez**: `teste-a2.php` planta SEIS bancos
adulterados num subprocesso, um por molde, e exige que o texto troque de forma E
que os numeros de hoje sumam da tela. Ler a pagina de hoje so prova que ela esta
certa hoje; a decisao 1 do bloco 5 e sobre amanha, quando o banco crescer e
ninguem reler o artigo.

### O DEFEITO QUE ESTAVA NO AR DESDE 21h36Z DE ONTEM

O A1 publicava as tres respostas do FAQPage em **ASCII** — "Nao. Nas 16 pecas de
reposicao..." — porque elas vinham do arquivo de fatos escritas como o banco
escreve. O banco desta ilha e ASCII porque ele **cita** fontes; o que a ilha
**escreve** sai em portugues de verdade (fase 4b do playbook). E o canal em que o
defeito aparecia e justamente o que a secao 5 do `ARQUIPELAGO.md` diz valer tanto
quanto ranquear.

Achado ao escrever o A2, que nasceu com a trava que mede isso. Corrigido em
`gerar-a1.py`, **sem tocar no snippet**: o A1 ja montava o FAQPage dos fatos, e
era o texto dos fatos que estava errado. Conferido no ar: o JSON-LD do A1 agora
sai acentuado.

### O RENDER DE BANCADA ESTAVA MEDINDO OUTRA PAGINA — a segunda vez nesta execucao

Alem de nao ligar o filtro de pagina (corrigido na revisao 12), o
`render-para-teste.php` nao carregava nas options o que o Sync carrega. Resultado:
toda pagina caia no aviso de "estamos sem o banco no momento" — e o aviso e uma
pagina **valida**, com folha, cabecalho e rodape, entao o engano nao aparecia. As
paginas renderizadas pularam de 26 KB para 62 KB quando o carregamento entrou.

**A medicao de rolagem horizontal foi refeita do zero, nas paginas de verdade:
0 px em 360/390/782/1200 nas CINCO paginas.** As tres lacunas de medicao desta
execucao tem a mesma forma — um teste verde que nao media o que dizia medir — e
as tres so apareceram porque alguem quebrou o codigo de proposito para ver a
trava reprovar.

### Uma trava apertada demais

`teste-a1.php` exigia que o catalogo de artigos tivesse **exatamente um** item, e
reprovou no dia em que a ilha ganhou o segundo. "Este artigo se registrou" nao e
a mesma afirmacao que "este e o unico artigo", e a segunda nunca foi sobre o A1.

### Verificacao

- `teste-a2.php` **62 medicoes**, `teste-r2.php` 86, `teste-r1.php` 90,
  `teste-a1.php` 53, `teste-casca.php` 64, `validar-banco.py` aprovado.
- No ar: HTTP 200, zero `&#038;` dentro de `<script>`, corpo comecando por texto,
  JSON-LD valido com `Article` + `FAQPage` acentuados, e as tres respostas do
  FAQPage com todos os numeros escritos tambem no corpo da pagina.
- `cobertura_de_faixa_r2`, dentro de `modelos-robo.json`, passou a apontar para
  `dados/cobertura-r2.json` e a explicar as duas diferencas de leitura — duas
  medicoes da mesma coisa sem ponteiro entre elas divergem em silencio.
- **5 modelos esperando link de loja** na vitrine deste artigo (os mesmos que
  declaram area por carga).

### O que ficou bloqueado, e o que NAO esta

**Toda coleta esta bloqueada pela rede**: `mi.com.br`, `wap.ind.br`,
`mais.conteudo.wap.ind.br` e `xiaomi.com.br` devolvem `000`, e so os dominios das
ilhas respondem. Isso trava os quatro alvos do 3c e o bloco 6.

**O que nao depende de rede e esta esperando:** acentuar o que o banco CITA e que
hoje aparece na tela (`nome_na_fonte`, `publicador`, `o_que_muda` saem em ASCII
dentro da resposta da R1) e resolver a contradicao do nivel 2 da escada de fontes
— as duas ja estao escritas no `PROMPT.md` da ilha e as duas sao trabalho de
repositorio.

- **Proximo passo: o bloco de dados que nao depende de rede** — o acento do que a
  ilha cita, e a decisao de regra sobre o nivel 2.

## 2026-09-10 (23h18Z) — Bloco 4: a R2 no ar, e a conta que ninguem publica

- **NO AR** em `https://robometria.com.br/quantos-pa-o-robo-aspirador-precisa/`
  (`snippets/robometria-r2.php` v1.0.0, manifest **revisao 12** conferida no
  `/status`, snippet #9 criado). Sitemap com 8 paginas, apelidos em 301, home e
  hub listando a ferramenta como publicada, e a **mao dupla fechada**: a R1
  passou a servir `<a href>` de verdade para a R2, e a R2 aponta de volta para a
  R1 e para o artigo-ancora.
- A ilha reservada por commit as 23h18Z, depois de a **clubedomosaico** ter sido
  levada por outra execucao no push das 23h16Z. Perder a corrida do push e o
  desenho da secao 1 do contrato funcionando, nao um erro.
- **A rede continua sem alcancar os fabricantes** (`mi.com.br`, `wap.ind.br`,
  `mais.conteudo.wap.ind.br`, `xiaomi.com.br` deram `000`, so os dominios das
  ilhas respondem). Por isso o alvo (a) do 3c — pecas com codigo da Xiaomi e da
  WAP — nao pode ser colhido, e a fila caiu para a R2, como o PROMPT.md previa.
  **Nenhum dado tecnico novo entrou no banco nesta execucao.**

### O ACHADO, e ele muda o que a ilha vai colher

A especificacao define **TEMPO REAL ATE TERMINAR = ciclos x autonomia +
(ciclos - 1) x recarga**. A varredura mediu que a formula precisa de TRES
numeros declarados pelo fabricante e que **nenhum dos 28 modelos publicaveis tem
os tres**: quem declara cobertura por carga (Electrolux, 5 modelos) nao declara
recarga; quem declara recarga (Xiaomi S20, Positivo PRA2000) nao declara
cobertura. A pagina publica os **ciclos** e o tempo de limpeza somado, e diz com
todas as letras que o total depende de um numero que ninguem publica.

Isso vira **lista de compras**: coletar `recarga_min_declarada` dos Electrolux
que ja declaram cobertura e o item de menor custo e maior retorno que esta
varredura encontrou — um campo por modelo destrava a frase que e a razao de a
ferramenta existir.

### O que a R2 se recusa a fazer, e por que isso e o produto

- **Nao converte minuto em metro quadrado.** Das 5 marcas publicaveis, 4 nao
  declaram area coberta em canal nenhum, e entre os dois pares declarados — os
  dois da MESMA marca — a taxa varia 23%. A recusa, dita com procedencia, e a
  frase que um modelo de linguagem cita.
- **Nao publica conta de mais de um ciclo** quando o fabricante nao declara se o
  modelo retoma de onde parou. ERB44 e ERB80 caem nesse caso e a pagina diz.
- **Nao pergunta voltagem**, porque nenhum modelo publicavel declara voltagem —
  a mesma regra que tirou "reservatorio" do seletor da R1.
- **"Acima de 4.000 Pa" e exclusivo.** Xiaomi S10 e E10 declaram exatamente
  4.000 e vao para secao propria, rotulada, abaixo: estar no numero nao e estar
  acima dele, e por-los em primeiro lugar seria recomendar em primeiro lugar
  quem a fonte citada nao cobre.
- **Uma situacao (tapete fino sem animal) nao e nomeada por fonte nenhuma.** A
  pagina publica as duas vizinhas com nome e data e resolve para a de cima,
  dizendo que esta estendendo — errar para baixo ali custa a compra inteira.

### TRES DEFEITOS DE MEDICAO, achados quebrando o codigo de proposito

A trava que nunca foi vista reprovando e trava nao medida. As seis travas novas
foram testadas numa copia; tres delas passaram na primeira tentativa e o motivo
era sempre o mesmo — o teste media a si mesmo:

1. **A regua da elegibilidade era uma funcao do proprio snippet**, e o teste a
   chamava para conferir a lista que o snippet publica. Trocar `>` por `>=` fazia
   as duas metades errarem juntas e o teste passar, com um modelo que a fonte
   citada nao cobre em primeiro lugar. A funcao **saiu do snippet** (era codigo
   morto que parecia a regra) e a comparacao passou a ser escrita no teste, lida
   do operador que a fonte declara.
2. **A grade de 10 em 10 m2 nunca pisava num multiplo exato da cobertura.** 162 e
   166 m2 nao tem multiplo terminado em zero, entao trocar `ceil` por `floor + 1`
   nao mudava resposta nenhuma: a grade so cobria o lado facil. Agora ela leva os
   multiplos e os vizinhos, e a trava reprova exatamente em 166 e 332 m2.
3. **A conferencia do FAQPage procurava a resposta no HTML inteiro** — e a
   achava dentro do proprio bloco de JSON-LD, passando sempre, inclusive com
   resposta inventada. Corrigida para procurar no corpo, ela **reprovou de
   verdade**: a marcacao publicava a resposta das 9 situacoes e a pagina servia
   so a da ancora. A correcao nao foi podar o FAQPage — foi **servir as nove**,
   cada uma com a frase inteira em HTML.

E o **render de bancada saia pela metade, em silencio**: sem `is_page()`, todo
snippet de pagina respondia "nao estou na minha pagina" e o HTML vinha sem folha,
sem JSON-LD e sem rodape, enquanto o shortcode aparecia — entao a pagina PARECIA
inteira. A primeira medicao de rolagem horizontal da R2 deu zero por falta do CSS
que ela deveria medir. `render-para-teste.php` passou a ligar o filtro
`<alvo>_na_pagina` sozinho, e a medicao foi refeita.

### Verificacao

- `teste-r2.php`: **86 medicoes**, zero falhas. Percorre a grade inteira — 9
  situacoes frase a frase, **114 cartoes** com ordem e ressalvas, **200 casos**
  de metragem contra cada modelo de referencia, bordas incluidas.
- `teste-casca.php` 64, `teste-r1.php` 90, `teste-a1.php` 53, `validar-banco.py`
  aprovado. A R1 e a casca **nao mudaram** nesta revisao — a R2 entra no catalogo
  pelo filtro da casca, que e exatamente o que o filtro existe para permitir.
- Chromium em 360/390/782/1200 px: **0 px de rolagem horizontal** nas quatro
  paginas, agora com as folhas servidas.
- No ar: HTTP 200, **zero `&#038;` dentro de `<script>`** (4 na pagina inteira,
  todas da casca do tema), corpo comecando por texto, script vindo do rodape, as
  63 linhas da tabela no HTML servido, `noindex,follow` + canonica na consulta e
  a pagina limpa sem `noindex`.
- **11 modelos esperando link de loja** (todos os que aparecem na tela).

- **Proximo passo: o artigo-ancora da R2**, na mesma execucao, como o bloco 5 do
  `PROMPT.md` manda — com a tese derivada, nunca digitada.

---

## 11/09/2026, 13h17Z — BLOCO DE DADOS: as duas dívidas nomeadas, fechadas

Nenhuma coleta. A rede foi testada antes de escolher o alvo, como o `PROMPT.md`
manda: `robometria.com.br` devolve **200**, `mi.com.br` e
`mais.conteudo.wap.ind.br` devolvem **000**. O 3c segue bloqueado, e a fila caiu
para o trabalho de repositório — que era o que estava escrito.

### 1. O banco parou de servir português errado

Com a R1 e a R2 no ar, o texto do banco é CITADO dentro da resposta publicada, e
a mesma frase saía metade certa e metade errada:

> "... e a **peça** certa depende da sua: bateria — o fabricante vende a **peca**
> PR10127 identificada como '**Versao** A'"

"peça" foi escrita pela ilha; "peca" e "Versao" vieram do banco. **121 strings
restauradas** nos nove campos que a varredura mediu chegando à tela.

**A restauração é PROVADA, não prometida.** Reduzido a sem-diacrítico, o banco de
hoje é byte a byte o de ontem — conferido nos três arquivos inteiros, e depois
linha a linha por `teste-acentuacao.php`, com uma régua escrita no teste. É isso
que torna impossível, por construção, que a operação tenha trocado uma palavra,
um código de peça, um número ou um modelo.

**E ela NÃO é releitura, o que é a parte honesta:** o acento foi reposto pela
ilha, não lido no fabricante — a rede não alcança fabricante nenhum. Por isso
existe `dados/acentuacao-restaurada.json`: não é log, é a **lista de conferência**
de quem reler os manuais quando a rede abrir. Se alguma fonte de fato escrever
sem acento, a linha volta atrás e vira exceção declarada.

Duas decisões de escopo, as duas para não adivinhar:
- **Monossílabo ambíguo ficou fora do mapa.** O "e" que deveria ser "é" exigiria
  entender a frase, e corretor que interpreta frase inventa.
- **A borda das palavras inclui o hífen.** Dentro do banco há endereço de página
  citado inteiro (`bateria-para-aspirador-robo-mars-ho041-versao-b--pr8116`), e
  acentuar um pedaço de URL destruiria justamente a evidência que a citação
  existe para dar. A prosa ao redor foi acentuada; o slug ficou intacto.

**A primeira versão da trava reprovou 15 mudanças CERTAS**, e o defeito era dela:
ela reduzia a string a ASCII, e o travessão "—" já estava no banco antes — era
apagado junto com os acentos. Régua errada reprova trabalho certo com a mesma
cara com que aprova trabalho errado.

### 2. A regra do nível 2, decidida: NÃO é nível 2

*Manual do fabricante hospedado por terceiro, colhido por busca, é nível 2?*
**Não. É nível 3.**

**A regra:** uma origem tem três elos — quem escreveu, quem guarda, como lemos —
e **o nível é o do elo mais fraco**. O manual do ERB10/11/20 é da Electrolux (elo
forte), mas está guardado por `manuals.plus` e chegou por busca, sem leitura.
Dois dos três elos são fracos.

**A direção saiu da assimetria de custo, não do gosto.** Errar para baixo custa
uma frase mais fraca ("a confirmar no manual"). Errar para cima faz a página de
metodologia declarar um rigor que a ilha não tem — e metodologia é a página cujo
único produto é o rigor.

**A medição decidiu sozinha, e foi ela que mostrou o tamanho da coisa:** as
QUATRO únicas fontes de nível 2 do banco inteiro eram a mesma entrada de
`manuals.plus`. Nível 2, neste banco, era **inteiro** custódia de terceiro. Três
das quatro nem eram usadas por campo nenhum.

### 3. O que a correção da escada descobriu, e ninguém procurava

A coluna "Temos hoje" era **digitada** dentro do snippet. Ao trocá-la por uma
contagem do banco, dois números caíram:

- **nível 2** dizia "—" enquanto quatro fontes se declaravam nível 2 — a
  contradição que abriu este bloco;
- **nível 6 (anúncio de marketplace)** dizia "sim" e a ilha **não tem uma fonte
  de marketplace**: zero selo `declarada_terceiro`, zero fonte de nível 6. Esse
  ninguém tinha percebido.

É o mesmo defeito que o bloco 5 nomeou no artigo-âncora: número que é a afirmação
da página não pode estar digitado no HTML, porque passa a mentir em silêncio no
dia em que o banco muda — e "em silêncio" é o ponto.

**E a primeira versão do gerador quase trocou um erro por um pior.** Ela contava
`pecas.json` e `modelos-robo.json` e declarava, com ar de medição, que a ilha não
tinha fonte editorial — quando tem sete, em `constantes.json`, citadas pela R2 em
TODA resposta de Pa. Medição que lê metade das origens é pior que o número
digitado que ela substitui, porque esta parece conferida. A ponte
tipo-de-constante → nível foi declarada no esquema, não escondida na ferramenta.

### 4. O render de bancada saía pela metade OUTRA VEZ, e só uma varredura grande viu

`ferramentas/varrer-corpo.php` monta os **72 estados** que a ilha consegue servir
— as 9 páginas fixas, a R1 em cada modelo publicável e em cada tipo de peça, a R2
nas 9 situações e nas bordas da metragem. Ele existe porque **renderizar uma
página só não é medir a página toda**: "Aspirador Robo" e "Versao A" só aparecem
quando alguém escolhe um modelo da Multi, e ficaram invisíveis para uma medição
que renderizava as nove páginas e se dava por satisfeita.

Montando os 72 no mesmo processo, **o cabeçalho apareceu no primeiro e sumiu nos
71 seguintes**. A causa é legítima e está no lugar certo:
`robometria_casca_marca_html()` guarda um `static $ja_impressa` para a marca não
sair duas vezes na mesma página, e no site um processo é uma requisição. Num
varredor, esse static vira contaminação entre estados. **Um processo por estado**
devolveu 45 KB de corpo que sumiam em silêncio — e mata junto qualquer outro
estado acumulado.

É a terceira vez que esta ilha paga por bancada que serve menos do que o site.

### 5. As travas novas, e a prova de que reprovam

`ferramentas/teste-acentuacao.php`, 16 medições, lendo o CORPO dos 72 estados.
Três cuidados, cada um uma cicatriz do Arquipélago:

1. **A régua é escrita no teste**, à mão, sem importar a do corretor. Régua
   compartilhada faz as duas metades errarem juntas — foi assim que a régua da
   elegibilidade da R2 morou no snippet e o teste a chamou para conferir o
   snippet.
2. **A afirmação se mede no CORPO**, não no HTML completo.
3. **A exceção se declara no markup e vem CONTADA.** O wordmark da ilha é
   "ROBO"+"METRIA" colados, e ROBO ali é a assinatura, não a palavra. A página
   marca o bloco com `rbm-wordmark`, o teste o retira e exige **um por estado** e
   que cada um seja exatamente a assinatura. Perdoar por vizinhança foi o que
   deixou passar "Peça mais vendido, últimas unidades!" no Clube do Mosaico.

**SEIS MUTAÇÕES deliberadas, e as seis reprovaram:**

| mutação | o que reprovou |
|---|---|
| devolver "Robo" a um `nome_na_fonte` da tela | 4 ocorrências no corpo |
| marcar um parágrafo comum como `rbm-wordmark` | 73 blocos em 72 estados, e o bloco não é a assinatura |
| adulterar o livro-razão (trocar "Escova" por "Escovinha") | não é só acento, e não está no banco |
| repor uma fonte no nível 2 sem declarar leitura | 3 medições, entre elas a confissão da página |
| repor no nível 2 COM leitura declarada | a confissão da página passa a mentir |
| tirar a classe `rbm-wordmark` | 0 exceções, e "ROBO" pego **72 vezes** |

A última é a que importa mais: ela prova que a exceção é **carregada**, não
decorativa — sem a declaração no markup, o teste realmente vê aquela palavra.

A primeira tentativa da terceira mutação **passou**, e era mutação vazia:
`mudancas[0]` não continha o texto que eu tentei trocar. Mutação que não muda
nada não mede nada.

Em `validar-banco.py`, duas invariantes novas, as duas testadas quebrando o banco:
- **`origem` tem que bater com a `origem` que a escada dá àquele `nivel`.** Era
  por aqui que o defeito entrava: só o `nivel` era conferido, então um manual em
  custódia de terceiro podia se declarar nível 2 com origem `manual-fabricante` e
  nada reprovava.
- **Nível 1 ou 2 exige `leitura: "direta-na-fonte-primaria"` declarado.**
  Silêncio nunca promove; adivinhar pelo texto do `canal_de_coleta` seria a
  heurística por vizinhança que a seção 8 proíbe.

### Verificação

- `teste-casca` **64**, `teste-r1` **90**, `teste-a1` **53**, `teste-r2` **86**,
  `teste-a2` **62**, `teste-acentuacao` **16** — zero falhas. `validar-banco`
  aprovado.
- Chromium em 360/390/782/1200 px, nas nove páginas: **0 px de rolagem
  horizontal** nas 36 medições. Corpo de 1.886 a 18.505 caracteres — nenhuma
  página fina.
- Os três bancos: reduzidos a sem-diacrítico, **idênticos** aos de antes.
- 44 itens esperando link de afiliado (16 peças + 28 modelos) — não mudou, este
  bloco não tocou em catálogo.

### Achado que fica na fila, da MESMA família, não corrigido

`robometria_casca_numeros()` lê `get_option('robometria_dados_cobertura-r1')`,
mas **`cobertura-r1` tem `publicar: false`**. No site no ar aquele `get_option`
nunca devolve nada, e a seção 4 da metodologia serve os números DIGITADOS no
snippet, com a data digitada junto. Hoje eles por acaso batem com a medição
(28 / 15 / 12 / 168 / 116, conferido nesta execução): o defeito está **latente,
não disparado** — e foi exatamente assim que a escada ficou meses errada. O
conserto barato é derivar esses cinco números para `casca-fatos.json`, pelo cano
que este bloco abriu.

- **Próximo passo: derivar os cinco números da seção 4 da metodologia**, fechando
  a última afirmação digitada daquela página. Depois dela, o 3c — se a rede abrir.

## 2026-09-11 — A ilha ganha VOZ e CABECA DE PAGINA (casca 1.2.0, revisao 15)

Bloco do despacho do Raphael de 11/09 (secao 15 do `ARQUIPELAGO.md` e `VOZ.md`
desta pasta) somado aos **itens 1 e 2 do despacho da Sentinela de 11/09**, que
moram no mesmo arquivo e na mesma cabeca de pagina. Fazer os dois separados
custaria duas versoes da casca e dois Syncs para mexer nas mesmas linhas.

### 1. Nenhuma das nove paginas tinha description — item 1 do despacho

A Sentinela mediu no navegador, as 14h40Z:
`document.querySelector('meta[name=description]')` devolvia `null` nas nove URLs
do sitemap, e nao havia `og:title`, `og:description` nem `og:url` em nenhuma.
**A causa e de desenho, nao de esquecimento:** a casca montava o JSON-LD do
`Organization` com um campo `description`, e aquela string ia so para o JSON-LD.
Como esta ilha nao tem plugin de SEO por decisao de projeto, ninguem mais
imprimia a tag. A consequencia de negocio esta na secao 12.1 do contrato, que
chama a faixa de posicao 4 a 10 de "trabalho de CTR (titulo, meta, schema)" — sem
description nao existe o que ajustar, e o Google escreve o trecho do resultado
sozinho.

Agora `robometria_casca_cabecas()` traz um mapa slug -> `{titulo, descricao,
tipo}` para as nove paginas, passado pelo filtro `robometria_cabecas` para pagina
nova poder trazer a dela de dentro do proprio snippet. O `wp_head` imprime
`description` mais `og:type`, `og:title`, `og:description`, `og:url`,
`og:site_name` e `og:locale`.

**A DECISAO QUE MAIS VAI DURAR: nenhuma description carrega numero.** Description
e texto digitado que ninguem rele, e ela nem aparece na tela para alguem
estranhar — e a cicatriz de 11/09/2026 (secao 8 do contrato, o cartao do Clube do
Mosaico que dizia "0" depois de a categoria ganhar cinco produtos) e exatamente
sobre numero digitado numa metade que nao fala com o banco. Aqui seria pior:
mentira no resultado da busca, invisivel de dentro do site. Numero mora na camada
de prova (secao 15.2). **A bancada reprova digito dentro de cabeca.**

**E o negativo importa tanto quanto:** pagina que a casca nao conhece sai SEM
description nenhuma. A saida tentadora — uma frase generica de reserva — publicaria
o MESMO texto em endereco diferente, que e o defeito que a tag existe para nao ter.

### 2. O H1 da raiz era a palavra "Inicio" — item 2 do despacho

Medido na mesma ronda: `[...document.querySelectorAll('h1')]` devolvia
`["Início"]` na home. E o H1 da pagina que disputa a marca, e "Inicio" e o nome do
LUGAR na estrutura do WordPress, nao o nome do que a pagina responde. Passou a ser
**"Robo aspirador: qual peca serve no seu, e quanta succao precisa"** — os dois
eixos da ilha, nas palavras da pessoa, e diferente do titulo das duas ferramentas
para as tres nao competirem no indice (secao 14.4).

**O defeito por tras do defeito:** `garantir_paginas()` nunca sincronizou titulo.
A pagina nascia com o titulo da definicao e ficava com ele para sempre — foi por
isso que "Inicio" sobreviveu a tres versoes da casca. Agora o titulo e
sincronizado para as paginas marcadas como nossas, e **o `post_name` nao e
tocado**: nenhuma URL muda, que e o que a secao 12.1 protege.

### 3. A home era um manifesto; virou a ferramenta

Primeira frase em terceira pessoa ("A Robometria diz..."), tres paragrafos de
metodo antes de qualquer campo, e uma secao inteira de confissao numerica. Tudo
verdade, e tudo no lugar errado: quem chega aqui esta com o robo aberto em cima da
mesa. Pelo molde FERRAMENTA do `VOZ.md`, agora e promessa numa linha, o seletor de
marca e modelo, atalhos por tipo de peca, e so depois o apoio.

- **O formulario e o da R1, CHAMADO, nao copiado.** Copia de formulario e a mesma
  armadilha da folha de estilo que este bloco desfez. Sem banco nas options a home
  nao desenha formulario vazio: diz que o seletor esta fora do ar e manda para a
  pagina da ferramenta.
- **Os atalhos sao DERIVADOS** de `r1-respostas['tipos']`, a mesma lista que
  preenche o seletor. O `VOZ.md` pede "filtro, escova e bateria"; digitar esses
  tres seria repetir a cicatriz do cartao que dizia zero. A bancada conta: banco 5,
  tela 5. Eles saem com `rel="nofollow"` porque o destino e uma consulta, e
  consulta desta ilha ja sai com `noindex,follow` (decisao 4 da R1).
- **A confissao de cobertura nao foi apagada** — foi para a metodologia, que e a
  pagina cujo unico produto e o rigor, e a home aponta para la com uma frase que
  qualquer pessoa entende.
- **O menu virou Pecas / Succao / Como conferimos**, apontando para as duas
  ferramentas e para a metodologia. NAO virou "Pecas / Modelos / Guias", que e o
  que o `VOZ.md` descreve: esses tres sao niveis da arvore da secao 16 e ainda nao
  existem como pagina, e rotulo sem pagina sai como `<span>` — um menu de tres
  spans seria pior que o menu tecnico que ele substitui.
- `/ferramentas/` e `/sobre/` sairam do menu e ganharam link no rodape, com o hub
  tambem linkado do corpo da home: nenhuma URL do sitemap com menos de dois links
  internos (secao 16.4-f).

### 4. A folha do formulario ganhou um dono so

`.rbm-promessa` e `.rbm-form*` estavam duplicadas na R1 e na R2 **e ja divergiam**
— so a R2 estilizava `input[type=number]`. Com a home servindo o mesmo formulario
seriam TRES copias de uma regra de layout, e basta alguem ajustar uma delas para a
ilha passar a ter dois formularios diferentes sem ninguem notar. E o mesmo desenho
da porta de compra, que a R1 devolveu a casca em 10/09. A versao da casca e a
UNIAO das duas, entao nenhuma pagina muda de aparencia. A bancada conta: a folha
existe em UM arquivo so.

### 5. O QUE A TRAVA NOVA ACHOU SEM PROCURAR — duas paginas, as duas ja no ar

A trava de **pagina fina** (secao 8 do contrato, cicatriz do Clube do Mosaico)
entrou porque a home tinha acabado de perder uma secao, e foi ela que reprovou
**`/divulgacao-de-afiliados/` com 1.325 caracteres de corpo** — uma pagina magra
no sitemap de um dominio recem-nascido, gastando orcamento de rastreamento. Nao
era defeito de render: a pagina era magra mesmo. Ganhou conteudo real da propria
ilha (o que quer dizer "link de loja em breve", por que dois programas e nao um, e
o bloco de recusa), e foi de 1.325 para 2.767.

E dentro dela caiu **um segundo numero digitado**: a frase "ainda nao ha nenhum
link de afiliado no ar nesta ilha" era verdade no dia em que foi escrita e ninguem
releria no dia em que deixasse de ser. Passou a ser contada — `com_link` derivado
de `itens_publicaveis - esperando_link`, com os dois lados conferidos contra o
banco commitado pela bancada, e a frase tem duas formas escolhidas pela contagem.

**E a trava de escassez achou a terceira:** a lista "O que a Robometria nao faz",
na pagina Sobre, usa as MESMAS palavras que a secao 7 do contrato proibe. Ela e
legitima — e o lugar onde a recusa deve estar escrita —, entao pelo desenho do
Clube do Mosaico ela foi **marcada no markup** (`rbm-recusa`), e o teste retira os
blocos marcados e proibe o termo em todo o resto. Os blocos sao poucos, contados, e
**todo item tem que ABRIR negando**, senao bastaria enfiar uma promessa dentro de
um bloco com nome de recusa.

### Verificacao

- `teste-casca` **133** medicoes (eram 64), `teste-r1` **90**, `teste-a1` **53**,
  `teste-r2` **86**, `teste-a2` **62**, `teste-acentuacao` **16** — zero falhas.
  `validar-banco` aprovado, `php -l` limpo nos tres snippets tocados.
- **QUINZE MUTACOES deliberadas** em `ferramentas/mutacoes-cabeca-e-voz.py`, cada
  uma numa copia da arvore inteira, exigindo que a bancada saia com codigo 1.
  **DUAS PASSARAM na primeira rodada, e as duas viraram conserto:**
  1. A regua de escassez listava `mais vendido` e **deixou passar** a mutacao que
     escreveu *"a peça mais vendida da categoria"* no corpo. Genero e numero em
     portugues sao o buraco por onde a frase proibida entra inteira. A regua passou
     a usar RADICAL (`mais vendid`), e a mutacao reprova.
  2. A mutacao de pagina fina era fraca: cortava 409 caracteres de uma pagina com
     522 de folga. Mutacao que nao muda o resultado nao mede nada — reforcada, e
     agora derruba o corpo de 2.022 para 1.243.
  Na segunda rodada, **15 de 15 reprovadas**.
- A bancada da casca passou a **carregar as options do manifest**, como o Sync as
  grava. Sem isso a home serviria o aviso de "seletor fora do ar", que e uma pagina
  VALIDA — seria a terceira vez que esta ilha mede uma pagina pela metade sem ver
  (secao 8 do contrato).
- 44 itens esperando link de afiliado — nao mudou, este bloco nao tocou em catalogo.

### O que NAO entrou, de proposito

- **A arvore da secao 16** (niveis de URL, breadcrumb com `BreadcrumbList`, cluster
  "Veja tambem", 301 do que mudar) e um bloco proprio e e o proximo. Ela precisa da
  decisao de pai e slug de cada pagina existente, e a secao 12.1 nao deixa trocar
  URL de pagina posicionada sem olhar a medicao — que depende do Search Console.
- **O defeito latente de `robometria_casca_numeros()`** (le a option de
  `cobertura-r1`, que tem `publicar: false`) continua latente. A home deixou de
  depender dele, mas a metodologia ainda serve aqueles cinco numeros digitados.

- **Proximo passo: a ARVORE da secao 16** — escrever `ARVORE.md`, dar pai a toda
  pagina, publicar breadcrumb e "Veja tambem". Junto com ela, derivar para
  `casca-fatos.json` os cinco numeros da secao 4 da metodologia, fechando a ultima
  afirmacao digitada daquela pagina.

### NO AR — conferido em 11/09/2026, 15h47Z

Sync acionado por `curl` as 15h43Z. `/status` responde **revisao 15**, igual a do
`manifest.json`, com `snippets/robometria-casca: ok (snippet #6 atualizado)`.
"Aplicado com sucesso" no log nao e evidencia de nada (secao 8), entao as nove
URLs foram medidas no ar, com quebra de cache:

- **9 de 9 em HTTP 200**, e **9 de 9 com `<meta name="description">`** — de 116 a
  136 caracteres, todas diferentes, com `og:type`, `og:title`, `og:description`,
  `og:url` e `og:site_name` presentes em todas. Era `null` nas nove ontem.
- **Zero `&#038;` dentro de `<script>`** nas nove, contado so dentro dos blocos.
- **O H1 da raiz** e `Robô aspirador: qual peça serve no seu, e quanta sucção
  precisa`. O corpo comeca por esse texto, nao por metadado.
- **A home serve a ferramenta:** `<form class="rbm-form">` no HTML, com 5
  `<optgroup>` (as 5 marcas), 28 `<option>` de modelo e 5 atalhos
  `rel="nofollow"` — os mesmos 5 tipos que o banco declara.
- **O menu no ar:** Peças → `/qual-peca-serve-no-meu-robo-aspirador/`, Sucção →
  `/quantos-pa-o-robo-aspirador-precisa/`, Como conferimos → `/metodologia/`,
  os tres como `<a href>` reais dentro de `<nav>`.
- **`/divulgacao-de-afiliados/`** serve o bloco de recusa marcado, com 4 itens
  abrindo com negacao, e a frase contada: "nenhum dos 44 itens do banco tem link
  de loja ainda". Tamanho da pagina no ar: 85 KB (era fina no corpo, nao no HTML).
- Tamanhos no ar, de 84 a 122 KB, coerentes com paginas inteiras.

## 2026-09-11, 19h18Z — Bloco da ARVORE: a secao 16 nas nove paginas, sem criar uma URL

Fecha o item que o despacho do Raphael de 11/09 deixou de pe depois do bloco da
voz. Casca **1.3.0**, R2 **1.0.2**, manifest na **revisao 16**.

**1. A ARVORE VIRA DOCUMENTO ANTES DE VIRAR CODIGO.** Nasceu `ARVORE.md` com os
tres niveis (16.1), as quatro secoes de nivel 1 — `/pecas/`, `/succao/`,
`/modelos/`, `/guias/` —, as quatorze categorias de nivel 2 e o lugar de cada uma
das nove paginas de hoje. `ferramentas/teste-arvore.php` **le esse arquivo** e
cobra que documento e codigo digam a mesma coisa, nas duas direcoes: categoria no
codigo que o documento nao tem reprova, e vice-versa. Dois lugares mantidos a mao
divergem em silencio, e o documento e o que a proxima execucao vai ler.

**2. AS DUAS DECISOES QUE O DESPACHO MANDOU TOMAR, TOMADAS.**
- **`/metodologia/` fica na raiz.** A lista da 16.1 nomeia uma familia — a pagina
  institucional, que fala da casa e nao do assunto — e a metodologia e dela.
  Pô-la dentro de uma secao de topico a faria filha de um assunto que ela nao tem.
  A Aquametria resolveu igual no mesmo dia; duas ilhas resolvendo diferente o
  mesmo caso seria a fabrica decidindo por gosto.
- **`/ferramentas/` fica, e e a unica pagina desta ilha com prazo de validade.**
  Ela e hoje a **mae de transicao** das duas ferramentas: da a elas um degrau com
  endereco de verdade, em vez de um degrau em texto apontando para o vazio. No dia
  em que `/pecas/` e `/succao/` nascerem ela passa a servir a mesma listagem que
  elas — duas URLs com o mesmo conteudo, que a 14.4 proibe — e sai com 301 para a
  home, que nesta ilha ja e a ferramenta. Nao neste bloco: retirar a mae antes de
  a substituta existir deixaria as duas ferramentas sem trilha.
- **O menu NAO virou Peças · Modelos · Guias** (o que o `VOZ.md` descreve): esses
  sao niveis que ainda nao existem como pagina, e sairiam como `<span>`. O
  `ARVORE.md` secao 5 escreve o que o menu vira quando elas nascerem.

**3. O QUE FOI AO AR.** Trilha nas oito paginas que nao sao a home (a home nao
tem, 16.3), sempre entre o cabecalho e o H1; `BreadcrumbList` em JSON-LD; blocos
"Veja tambem" nas quatro paginas de conteudo, com as irmas **derivadas** do mesmo
registro que alimenta o hub; e a frase que linka a mae com a contagem **contada**.
**Nenhuma URL nova** — e era essa a condicao para caber agora, porque esta ilha
nao publica leva de malha enquanto o sitemap nao for reenviado no Search Console
(metade humana do despacho da Sentinela de 10/09).

**O degrau sem endereco sai em TEXTO e fica FORA do schema.** Num guia a trilha
mostra quatro degraus na tela (Início › Guias › Peças › o titulo) e o
`BreadcrumbList` publica dois. Nao e esquecimento: `ListItem` do meio sem `item`
invalida a lista inteira para o Google, e lista invalida e lista ignorada — o
schema "mais completo" publicaria MENOS com cara de publicar mais.

**Cada mae tem duas filhas, entao cada filha tem UMA irma, e a 16.4(c) pede de 2 a
4.** Estado de transicao declarado no `ARVORE.md`, nao desenho: o minimo de duas
chega no dia da terceira filha.

**4. O DEFEITO QUE A VARREDURA DE LINKS ACHOU SEM PROCURAR.** Medindo qual pagina
cita qual **no corpo**, a ferramenta de succao linkava o guia do filtro universal
e **nao linkava o guia dela**, o de metros quadrados por carga — que e justamente
o texto que explica de onde vem o numero de area que ela usa. O par da 16.4(d)
estava aberto de um lado so, e ninguem via, porque um link para guia havia e
nenhum teste perguntava se era o guia CERTO. Agora o portao deriva o par do campo
`ferramenta` do catalogo de artigos e cobra os dois sentidos.

**5. OS ONZE NUMEROS DA ILHA SAIRAM DO SNIPPET — e o defeito latente disparou na
leitura.** `robometria_casca_numeros()` tinha os onze digitados e um caminho
"derivado" que lia `get_option('robometria_dados_cobertura-r1')`. **`cobertura-r1`
tem `publicar: false` no manifest: a option nunca existiu no site.** Quer dizer
que, no ar, todo numero da secao 4 da metodologia, da `/sobre/` e da
`/divulgacao-de-afiliados/` sempre veio do valor digitado, e o trecho que parecia
corrigi-lo era decoracao. Estavam certos porque alguem os copiou a mao no dia
certo — e um ja tinha deixado de estar.

**"Pares peca × modelo, todos declarados" dizia 33 e o banco serve 32.** O par que
sobrava aponta para `multi-ho401`, que e `nao_publicavel` (nome comercial nao
confirmado): a ferramenta nunca o oferece, entao ele nao cobre nada. Numa tabela
chamada "o que medimos sobre a nossa propria cobertura", o numero certo e o que a
ilha CONSEGUE servir. **Os dois numeros continuam existindo e medem coisas
diferentes** — o cabecalho de `pecas.json` conta o que o banco guarda, a tela
conta o que o site responde —, e a pagina agora diz a regua em voz alta: "um par
so e contado quando as duas pontas estao publicadas".

Os onze passaram a viajar em `dados/casca-fatos.json`, que e publicavel, derivado
por `gerar-casca-fatos.py`, com a **regua de cada um escrita no proprio arquivo**
(`reguas_da_medicao`). O gerador **RECUSA** gravar quando `cobertura-r1.json` nao
bate com o banco de hoje, para a ilha nunca publicar medicao de ontem com data de
hoje. E **sem o arquivo a pagina nao inventa numero**: diz que a medicao nao
chegou. Valor de reserva seria o numero digitado que este bloco veio tirar, so que
invisivel.

**O TESTE QUE COMPARAVA DUAS COPIAS DA MESMA REGUA.** A secao 8 do
`teste-casca.php` conferia o numero da tela contra `contagem.publicavel` e irmaos
— campos escritos no proprio arquivo de banco. As duas metades da comparacao
vinham da mesma regua, e trocar a regra as faria errar juntas. Agora o teste conta
nos registros, e foi assim que o 33 apareceu.

**6. A BANCADA VOLTOU A SERVIR O QUE O SITE SERVE.** Tres consertos no
`render-para-teste.php`, e os tres sao a mesma cicatriz: (a) ela **nao montava o
bloco `core/post-title`**, entao media paginas sem H1 nenhum — e a trilha nasce
justamente entre o cabecalho e o H1; (b) ela **nao rodava os filtros do
`the_content`**, so escapava a string, entao o "Veja tambem" (prioridade 20) e a
rede de seguranca da trilha (prioridade 9) seriam invisiveis; (c) `add_filter`
**aceitava a prioridade e a jogava fora**, rodando na ordem de registro — com tres
filtros no mesmo gancho, so uma das ordens possiveis e a do site. Achado de
tabela: montado o bloco de titulo DEPOIS do conteudo, a rede de seguranca disparava
primeiro e a bancada media o caminho reserva achando que media o principal.

**7. VERIFICACAO.** `teste-arvore.php` 213 afirmacoes (um processo `php` por
pagina, porque a trava `static` da trilha faz a segunda pagina do mesmo processo
sair sem ela); `teste-casca` 135, `r1` 90, `a1` 53, `r2` 86, `a2` 62, acentuacao
16; `validar-banco` aprovado; `php -l` limpo nos 6 snippets e nas 9 ferramentas
PHP. **18 mutacoes deliberadas em `ferramentas/mutacoes-arvore.py`, 18 reprovadas**
— e **TRES passaram na primeira rodada, as tres por serem INERTES**: tirar a
guarda da home nao punha trilha nela (a home nao esta em catalogo nenhum), mexer
no `url_mae` nao fazia a frase sair nos guias (a segunda condicao segurava), e
cortar 345 caracteres de uma pagina com 526 de folga nao a deixa fina. As tres
foram reescritas ate morder. Chromium em 360/390/781/782/783/1200 nas nove
paginas: **258 medicoes, 0 px de rolagem horizontal**, trilha sempre dentro da
tela e acima do H1, console sem mensagem.

**8. O TETO DE QUATRO IRMAS SO E MEDIDO PORQUE A BANCADA FABRICA A BORDA.** Com
duas ferramentas no ar, nenhuma pagina chega a ter cinco irmas candidatas: trocar
o teto de 4 por 40 nao mudaria uma linha do que o site serve, e o portao ficaria
verde nas duas versoes. O teste monta um catalogo de seis filhas para o teto ter o
que cortar — e a mutacao correspondente reprova por causa disso, so.

**9. O CATALOGO NAO FOI TOCADO: 44 itens publicaveis, 44 esperando link de
afiliado**, nenhum com loja possivel hoje. Temas da pauta (secao 17): a `pauta.md`
ainda nao existe nesta pasta — 0 escritos, 0 na fila, 0 recusados.

**ACHADO REGISTRADO, fora do escopo:** `/sobre/` e a unica das nove paginas que
nenhum CORPO de outra cita — ela vive do menu e do rodape, que estao em todas,
entao nao e orfa pelo 16.4(f), mas e a unica sem citacao editorial. A Aquametria
tem exatamente o mesmo achado no mesmo dia, o que sugere que e do molde da casca e
nao da ilha. E assunto de pauta (secao 17).

### NO AR — conferido em 11/09/2026, 19h47Z

Sync acionado por `curl` as 19h45Z. `/status` responde **revisao 16**, igual a do
`manifest.json`. As nove URLs foram medidas no ar, com quebra de cache:

- **9 de 9 em HTTP 200**, de 86 a 126 KB.
- **94 afirmacoes medidas no HTML servido, todas passando.** Uma "falha" da
  primeira rodada era da regua, nao da pagina: procurar `rbm-veja` no HTML
  INTEIRO acha a regra de CSS na home. Medido de novo por `<nav class="rbm-veja"`,
  a home tem zero — e a licao e a mesma da secao 8 do contrato, que este bloco
  passou o dia aplicando em outro lugar.
- **Trilha:** uma por pagina nas oito, sempre antes do H1, nenhum degrau apontando
  para pagina inexistente, e o degrau atual igual ao H1 servido nas oito.
- **`BreadcrumbList`:** posicoes 1..N sem buraco, todo `ListItem` com endereco,
  e os itens sao exatamente os degraus linkados mais o atual — 3 nas ferramentas,
  2 nos guias e nas paginas de raiz, nenhum na home.
- **Cluster:** "Veja tambem" so nas quatro filhas, uma irma cada, todas paginas que
  existem; a frase da mae so nas duas ferramentas, dizendo **2** — contado.
- **Zero `&#038;` dentro de `<script>`** nas nove.
- **Os numeros no ar:** 5 marcas, 28 modelos, 16 pecas, **32 pares**, 15 que
  respondem, 12 vazios, 116 de 168 combinacoes, medicao de **11/09/2026**; a
  `/sobre/` diz os mesmos 5/28/32 e a `/divulgacao-de-afiliados/` diz "nenhum dos
  44 itens tem link de loja ainda". A R2 serve o link do guia dela.

- **Proximo passo: a `pauta.md` da secao 17 nao existe nesta pasta, e ela e quem
  destrava os guias.** Enquanto isso, o proximo bloco sem URL nova e a **reescrita
  na voz das paginas restantes** (a 15.5 manda reescrever cada pagina existente ao
  passar pela ronda; home e header ja foram). Tudo que cria URL — as quatro secoes,
  as quatorze categorias, a troca de pai e slug — espera o **reenvio do sitemap no
  Search Console**, que e do Raphael.

## 11/09/2026, 21h48Z — UM NOME POR PAGINA NAS NOVE, e a bancada que media tres delas pela metade (casca 1.4.0, R1 1.2.0, R2 1.1.0, A1 1.1.0, A2 1.1.0, manifest revisao 17)

Bloco da voz da secao 15.5 — a reescrita das paginas restantes, que era o proximo
passo sem URL nova. Ele cresceu porque a medicao achou duas familias de defeito
antes de chegar ao texto, e as duas sao a mesma coisa: **metades que nao se falam.**

**SEIS DAS NOVE PAGINAS TINHAM DOIS NOMES.** O `og:title` publicava "Quem publica
a Robometria" e o H1 da mesma pagina dizia "Sobre"; o artigo do filtro universal
se chamava "Por que nao existe filtro universal de robo aspirador" no H1 e
"Existe filtro universal de robo aspirador?" no cartao compartilhado; a R2 tinha
um nome no H1 e outro na cabeca. Ninguem errou: a casca 1.2.0 criou um mapa de
cabecas com `titulo` proprio, ao lado do titulo da definicao da pagina, e os dois
eram certos no seu lugar. Nenhum podia corrigir o outro — a mesma forma da coluna
"Temos hoje" digitada ao lado de um banco que ja dizia outra coisa.
**Conserto:** `robometria_casca_nome_da_pagina()` e a fonte unica (definicao da
casca para as cinco dela, catalogo da propria ferramenta ou artigo para as
quatro, que agora recebe o titulo da constante do snippet que CRIA a pagina). O
H1, o `<title>`, o `og:title`, o degrau da trilha e o rotulo do cartao derivam
dela. O mapa das cabecas perdeu o campo `titulo`.

**O `<title>` ERA A UNICA SUPERFICIE QUE O REPOSITORIO NAO ESCREVIA.** Medido na
home no ar: `Robometria – Compatibilidade de pecas e dimensionamento de robo
aspirador`, 73 caracteres, vindos do campo de descricao curta do wp-admin. Um
terceiro nome para a pagina mais importante da ilha, em vocabulario de dentro da
fabrica, num campo que nenhum arquivo daqui escreve e nenhuma bancada podia ver —
porque a bancada servia um `<title>` digitado ("Robometria — teste") em todas as
paginas. Agora a casca assume `document_title_parts`, a bancada monta o titulo
pelo mesmo caminho do nucleo, e o teto de 65 caracteres e cobrado no NOME (52),
antes de publicar.

**A BANCADA MEDIA TRES PAGINAS PELA METADE, e a causa e a quarta repeticao da
mesma cicatriz.** `ferramentas/varrer-corpo.php` — o varredor que existe
justamente para medir a entrada inteira, 72 estados, um processo por estado —
nunca chamou `robometria_teste_carregar_options()`. Entao `pagina:a1` devolvia
**1.118 caracteres** de corpo (a pagina real tem 7.2 mil), `pagina:a2` 1.107, e
`pagina:metodologia` servia o aviso de que a medicao nao chegou, ou seja, os onze
numeros que a ilha publica sobre si mesma NUNCA foram varridos. Os tres eram
paginas **validas**: cabecalho, rodape, folha, trilha e um aviso honesto de tres
linhas. Por isso passou em silencio, e por isso o `teste-acentuacao` — o unico que
varre a entrada inteira — nunca leu o corpo dos dois artigos.
**Conserto em tres partes, e a do meio e a que fecha a familia:** (1) o varredor
carrega as options como o Sync; (2) o aviso de "estamos sem o banco" ganhou **dono
unico** na casca e a marca `rbm-sem-banco` no markup, que nao muda nada na tela e
existe so para a bancada conseguir dizer "isto nao e a pagina"; (3) dois portoes
reprovam o estado degradado (`teste-voz.php` e `teste-acentuacao.php`). Depois
disso, os dois renderizadores de bancada passaram a medir a mesma pagina com 34
caracteres de diferenca — constante, e explicada.

**O TITULO DO A1 AFIRMAVA UMA TESE QUE O BANCO PODE INVERTER.** A tese do artigo e
uma contagem; por isso a frase de abertura, a `description` do JSON-LD e a
resposta do FAQPage tem DUAS formas, escolhidas pela contagem do dia. O titulo
tinha uma so, digitada — e ia junto para o `headline` do JSON-LD, que e o canal
que a secao 5 do contrato diz valer tanto quanto ranquear. Virou a pergunta, que
sobrevive as duas formas e e o que a pessoa digita. A regra ficou estrutural no
`teste-a1.php`: titulo de artigo de tese derivada termina em "?", e pergunta nao
afirma.

**O QUE SO APARECEU AO RENOMEAR: os quatro snippets de pagina nunca reespelhavam
o `post_title`.** So a casca aprendeu isso, na 1.2.0. Renomear a R2 no repositorio
teria trocado o `og:title`, o cartao e a trilha (derivados) e deixado o H1 e o
`<title>` DO AR com o nome antigo — duas fontes para o mesmo campo, e a bancada
lendo a que esta certa. E exatamente a cicatriz da Aquametria do mesmo dia.
Corrigido nos quatro, com a versao de cada um bumpada para o `garantir_pagina`
rodar. De quebra, o `manifest` dizia que a R2 estava na 1.0.2 e a constante dizia
1.0.1: duas copias do mesmo numero, uma envelhecida sozinha — agora conferidas.

**A VOZ, que era o pedido original.** As quatro paginas da casca perderam o nome
de gaveta ("Sobre", "Ferramentas", "Metodologia", "Divulgacao de afiliados") e
ficaram com o nome que a cabeca da propria pagina ja publicava na voz desde a
1.2.0 — nada inventado, uma divergencia desfeita para o lado que ja estava
escrito. As aberturas das oito paginas deixaram de comecar nomeando a si mesmas e
passaram a falar com quem entrou; a procedencia (nome de fabricante, codigo,
data) desceu um paragrafo, para a camada de prova `rbm-prova`, dentro da mesma
caixa — quem cita a abertura continua levando a prova junto. No A2 isso tirou
"Electrolux" da primeira linha sem tirar o numero, que e a resposta.

**O PORTAO NOVO:** `ferramentas/teste-voz.php`, 155 afirmacoes, um processo por
pagina, regua propria, lista de proibidas lida do `VOZ.md`, regua de procedencia
lida do banco (5 publicadores e 32 codigos). Ele cobra as cinco superficies do
nome, o teto do `<title>`, o nome de gaveta (lista fechada, casada no nome
inteiro), a abertura que nao fala de si, a segunda pessoa, a procedencia fora da
abertura, o estado degradado e o piso de 1.500 caracteres de corpo. A excecao por
classe vem com a contrapartida que a impede de ser porta dos fundos: **a
linha-mestra nunca pode ser bloco de prova**, e os blocos marcados sao contados e
impressos um a um.

**VERIFICACAO:** teste-voz 155, teste-casca 149 (era 135), teste-arvore 213,
teste-r1 90, teste-a1 55, teste-r2 86, teste-a2 63, teste-acentuacao 17,
validar-banco aprovado, `php -l` limpo nos seis snippets. **29 mutacoes
deliberadas, 29 reprovadas** — e uma delas so mordeu depois de reescrita: a
mutacao antiga do H1 da raiz ficou **inerte** no instante em que o titulo da home
mudou, porque o alvo dela deixou de existir. Mutacao que nao encontra o alvo edita
nada e o teste passa. `mutacoes-arvore.py` segue 18/18. 258 medicoes em Chromium
nas nove paginas em 360/390/781/782/783/1200, 0 px de rolagem.
**NO AR as 21h48Z:** Sync acionado por curl (revisao 17, 10 aplicados), `/status`
com revisao 17 igual a do manifest, e `ferramentas/conferir-no-ar.py` — que nasceu
nesta execucao com os nove enderecos e os nove nomes **escritos literalmente
dentro dele**, copiados da decisao e nao lidos do codigo — mediu **65 afirmacoes
no HTML servido, 0 falha**: as nove em 200, `<title>` = nome + marca em todas e
dentro do teto (o maior tem 63), `og:title` = H1 = nome nas nove, nenhuma servindo
o estado degradado, zero `&#038;` dentro de `<script>`.

- **44 itens esperando link de afiliado** (nao mudou; este bloco nao tocou
  catalogo), nenhum com loja possivel hoje.
- **Pauta da secao 17:** `pauta.md` ainda nao existe nesta pasta — 0 escritos, 0 na
  fila, 0 recusados.
- **Proximo passo:** a 15.5 esta fechada nesta ilha e o nome tem fonte unica. Sem
  criar URL, o que sobra e a **vitrine de produto dentro do resultado da R2** (a R1
  ja tem o bloco de compra desde 10/09; a R2 recomenda modelo e nao tem) e a
  **transcricao da composicao dos kits**, que abre porta de compra por dado em vez
  de afrouxar regra. Tudo que cria URL — as quatro secoes, as quatorze categorias,
  a troca de pai e slug — continua esperando o **reenvio do sitemap no Search
  Console**, que e do Raphael.

---

## 2026-09-11, 23h37Z — A PROCEDÊNCIA DO Pa CHEGA AO CARTÃO DA R2 (snippet 1.2.0, manifest revisão 18, `/status` conferido)

**O bloco começou pelo passo errado, e isso é o primeiro registro.** O `ESTADO.md`
da execução anterior mandava construir "a vitrine de produto dentro do resultado da
R2 — a R1 já tem o bloco de compra, a R2 recomenda modelo e não tem". A vitrine
**existia**: nasceu junto com a R2 em 11/09, `robometria_r2_vitrine()` é chamada na
resposta e o HTML servido trazia cinco cartões com botão reservado. O próximo passo
tinha sido escrito de memória e não medido. Foi ao abrir a página no ar, antes de
escrever uma linha, que isso apareceu — e foi lendo o cartão **como um leitor lê**
que apareceu o defeito de verdade, que ninguém tinha nomeado.

**O QUE O CARTÃO NÃO DIZIA.** O Pa é o único número que decide aquela recomendação,
e o cartão o publicava assim: "Xiaomi S20: 5.000 Pa declarados pelo fabricante".
Sem endereço, sem data, sem o degrau da escada de fontes. A R1 faz isso desde o
primeiro dia, no mesmo tipo de cartão, com "Como sabemos — página do fabricante ·
fonte". A R2, não. Numa ilha cuja seção 5.4 do contrato pede a procedência **dentro
da própria frase, com data**, e cujo produto inteiro é a afirmação técnica com
origem, o número que decide a compra era o único sem origem na tela.

**E A ATRIBUIÇÃO ERA DIGITADA.** "declarados pelo fabricante" estava no molde da
frase, nos dois lados (referência e snippet). Hoje é verdade — as onze fontes de Pa
do banco são todas `fabricante-via-busca` —, e é exatamente por isso que passava:
**a frase estava certa por coincidência do banco, não por construção.** No dia em
que um Pa entrasse por loja oficial da marca (degrau 4, que já existe na escada e já
tem fonte no banco para outros campos), a página emprestaria, calada, a autoridade
do fabricante a quem apenas transcreveu. É a mesma família do número de tela
digitado que a casca pagou em 11/09: nasce contado, nunca digitado — aqui, nasce
**lido do degrau**.

**O ROTULO E A RESSALVA DE CADA DEGRAU MUDARAM DE CASA, e essa é a metade estrutural
do bloco.** Eles eram uma tabela DIGITADA dentro de `ferramentas/gerar-r1.py`
(`ROTULOS_DE_ORIGEM`), enquanto a `escada_de_fontes` do `esquema-banco.json`
descrevia os mesmos textos em prosa ("Vai para a tela com 'a confirmar no manual'").
Duas cópias do mesmo fato, cada uma certa no seu lugar e **nenhuma capaz de corrigir
a outra** — a forma exata do defeito dos dois mapas de nome que a casca 1.2.0 pagou,
e da coluna "Temos hoje" digitada na metodologia. Agora cada degrau declara
`na_tela: {rotulo, ressalva, quem_declara}` ao lado do `nivel` que ele já declarava,
e os geradores das duas ferramentas leem de lá. O `r1-respostas.json` foi regerado e
**nenhum valor existente mudou**: a tabela só ganhou campos — que é a prova de que a
derivação reproduz o que estava digitado, e não de que alguém trocou o texto.

**O QUE MUDOU NA TELA.** Cada cartão da R2 passou a trazer, nesta ordem: a ressalva
do degrau (`a confirmar no manual`), a porta de compra, e **só depois dela** a linha
"Como sabemos — página do fabricante, verificado em 09/09/2026 · fonte", com o link
`nofollow noopener` na classe discreta da casca. A ordem é a seção 7 escrita em
código: inverter os dois devolve ao link de procedência o papel de única porta
clicável, que é a cicatriz de 10/09/2026.

**A JANELA DO SYNC ESTÁ COBERTA, e ela é real.** O Sync aplica item a item, então
existem minutos com o snippet na 1.2.0 e a option ainda no arquivo de dados
anterior, sem `procedencia`. Sem conferência, isso seria aviso de PHP no ar. Agora
`robometria_r2_dados()` recusa o banco de forma antiga e a página cai no estado
degradado que a ilha já desenhou — que diz a verdade e que o portão da voz reprova,
então não passa despercebido se durar. Medido quebrando o arquivo de dados de
propósito: `teste-voz.php` acusa `rbm-sem-banco servido`.

**VERIFICAÇÃO.** `teste-r2.php` de 86 para **90 medições**, com a seção 16 nova.
Três cuidados nela, e os três já custaram caro nesta ilha: **régua própria** (ela lê
`esquema-banco.json` e `modelos-robo.json` direto, nunca `robometria_r2_modelo()`
nem o `r2-respostas.json`, que é escrito pelo mesmo gerador que preenche a
procedência — conferir contra ele seria comparar o arquivo com ele mesmo); **medição
no corpo**, recortando cada `<li>` da vitrine, nunca na página inteira; e **a entrada
inteira**, as 9 situações, **38 cartões**, não o caso-âncora.
`mutacoes-procedencia.py`: **11 mutações deliberadas, 11 reprovadas**. A que importa
quase saiu inerte: "a atribuição volta a ser digitada" não muda um byte enquanto o
banco tiver um degrau só, então ela precisa produzir o mundo em que o defeito
aparece — um Pa entrando por loja oficial — **e** regerar o arquivo de dados; sem
esse terceiro passo ela reprovava pelo motivo errado (divergência banco × dados) e a
trava da atribuição continuava não medida. `validar-banco.py` ganhou a trava do
`na_tela` (todo degrau declara os três campos; ressalva nula exatamente nos níveis 1
e 2, porque silêncio nunca promove), medida quebrando a escada de propósito e
reprovando as duas. `teste-casca` 149, `r1` 90, `a1` 55, `a2` 63, `acentuacao` 17,
`arvore` 213, `voz` 155; `php -l` limpo nos cinco snippets.

**A ILHA GANHOU `ferramentas/atualizar-manifest.py`**, que ela não tinha: o sha e a
versão eram escritos à mão, e foi assim que o manifest ficou dizendo R2 1.0.2 com a
constante do próprio snippet em 1.0.1. A versão passou a ter fonte única — a
constante — e o manifest é espelho. **Ele espelha só o que a chave `esquema` do
próprio manifest declara:** a primeira versão gravou `sha256` nas 20 ferramentas de
bancada, campo que aquela seção do contrato não tem, e ainda faria a revisão subir
por mudança que nunca vai ao site. E **imprime cada troca que faz**, que é a metade
que faltou na Aquametria em 11/09. Sete ferramentas de bancada que estavam fora do
manifest entraram nele.

**NO AR às 23h36Z, em UM disparo do Sync:** `/status` com revisão 18 igual à do
manifest, 10 aplicados. `conferir-no-ar.py` mediu **72 afirmações no HTML servido,
0 falha** — as nove URLs em 200, nome único nas cinco superfícies, nenhuma no estado
degradado, zero `&#038;` dentro de `<script>`, e o bloco novo: nos 4 cartões da
âncora, a linha de procedência com a data, a ressalva do degrau, a atribuição do
degrau, a porta de compra antes da fonte e o link discreto com `nofollow`. Os três
textos esperados estão escritos **literalmente** dentro do arquivo, como os nomes das
páginas.

- **44 itens esperando link de afiliado** (não mudou; este bloco não tocou catálogo),
  nenhum com loja possível hoje. Na R2, 11 de 11 modelos na tela esperam link.
- **Pauta da seção 17:** `pauta.md` ainda não existe nesta pasta — 0 escritos, 0 na
  fila, 0 recusados.
- **Próximo passo, e desta vez medido no ar antes de ser escrito:** o **A2**
  (`/quantos-m2-o-robo-aspirador-limpa-por-carga/`) serve **5 cartões de vitrine com
  ZERO procedência** — "O fabricante declara 166 m² por carga" sem endereço, sem
  data, sem degrau e sem link. É o mesmo defeito que este bloco fechou na R2, na
  página irmã dela, e agora a casca já tem as peças. Depois dele, a seção "Exatamente
  no limiar" da própria R2, que nomeia modelos e Pa e também não cita origem. A
  **transcrição da composição dos kits** e o **3c** seguem parados por rede: medido
  nesta execução, `electrolux.com.br`, `mi.com.br`, `wap.ind.br`,
  `mais.conteudo.wap.ind.br` e `positivotecnologia.com.br` devolvem `000` por
  política do egresso, repetido duas vezes, com o domínio da ilha respondendo 200 na
  mesma passada — é política de rede, não a intermitência de túnel da seção 20. Tudo
  que cria URL continua esperando o **reenvio do sitemap no Search Console**, que é
  do Raphael.

## 2026-09-12, 15h40Z — A procedência da área por carga chega ao cartão do A2 (1.2.0, revisão 20)

**O bloco começou medindo no ar antes de escrever uma linha** — que foi a lição que o
bloco anterior deixou escrita, depois de começar pelo passo errado. Desta vez a página
foi aberta primeiro, e o que ela mostrou era pior do que o cabeçalho previa.

**O QUE O CABEÇALHO PREVIA:** "o A2 serve 5 cartões de vitrine com ZERO procedência". Era
verdade e era metade. **O QUE ESTAVA NO AR:** os cinco cartões diziam *"O fabricante
declara 166 m² por carga"*, e essa frase era **falsa**. Os cinco modelos que declaram área
por carga declaram todos pela fonte `f-loja` — degrau **4** da escada, `varejo-oficial-da-marca`,
cujo `quem_declara` é "pela loja oficial da marca". A página não estava só calando a
origem: estava **creditando ao fabricante o que a loja transcreveu**.

**E ISSO É EXATAMENTE O QUE A R2 PREVIU EM 11/09, NA PÁGINA IRMÃ.** O registro daquele
bloco diz, palavra por palavra: *"No dia em que um Pa entrasse por loja oficial da marca
(degrau 4), a página emprestaria calada a autoridade do fabricante a quem apenas
transcreveu."* Lá o defeito era latente — a frase digitada era verdade por coincidência do
banco. Aqui o dia já tinha chegado e ninguém tinha olhado: **o mesmo defeito, na página ao
lado, já disparado.** A diferença entre as duas páginas não era o código; era que uma
tinha sido lida como um leitor lê e a outra não.

**A REGRA MUDOU DE LUGAR, e essa é a metade estrutural.** `procedencia_do_pa()` sabia
derivar a procedência de **um campo só**. O A2 decide pela ÁREA, não pelo Pa, e por isso
não tinha de onde ler o degrau — regra derivável por um campo só é regra que a segunda
página reescreve. Agora existe `procedencia_do_campo(m, campo)` em `cobertura-r2.py`, com
`procedencia_do_pa`, `procedencia_da_cobertura` e `procedencia_da_autonomia` por cima.
**Regerar a R2 devolve `r2-respostas.json` byte a byte idêntico** — a prova de que a
refatoração não mudou valor nenhum, e não uma promessa.

**NA TELA:** o cartão traz a ressalva do degrau ("confira a embalagem"), a porta de compra,
e só depois dela a linha "Como sabemos — loja oficial da marca, verificado em 09/09/2026 ·
fonte", com `nofollow` na classe discreta da casca. A ordem é a seção 7 escrita em código.
O título da seção também era digitado ("Os modelos cujo fabricante publica o número") e
agora só nomeia um publicador **quando todos os itens concordam**; com degraus misturados
ele não atribui a lista a ninguém, porque uma frase só não pode fazer isso sem mentir
sobre parte dela.

**E UMA CORREÇÃO QUE VEIO DE LER O CARTÃO COMO UM LEITOR LÊ:** a frase nova abria repetindo
o número que já era o título do cartão uma linha acima ("166 m² por carga" / "166 m² por
carga, declarados pela…"). O número já está dito; a frase existe para dizer QUEM declarou.
Virou "Área por carga declarada pela loja oficial da marca".

**VERIFICAÇÃO.** `teste-a2.php` de 63 para **73 medições**, com os três cuidados que esta
ilha já pagou: **régua própria** (lê `esquema-banco.json` e `modelos-robo.json` direto,
nunca `a2-fatos.json`, que é escrito pelo mesmo gerador que preenche a procedência),
**medição no corpo** (recorta cada `<li>`, nunca a página inteira — a seção de procedência
do artigo também fala em "fabricante", e medir a página toda aprovaria um cartão mudo) e
**a entrada inteira** (os cinco cartões).

`mutacoes-a2-procedencia.py`: **15 deliberadas, 15 reprovadas** — e **TRÊS passaram na
primeira rodada**, que é o que este arquivo existe para descobrir:
1. **a ressalva empurrada para depois do botão de compra.** O teste media que ela
   *existisse*, nunca *onde* — e ressalva depois da decisão não é ressalva, é nota de
   rodapé. Virou medição por POSIÇÃO.
2. **a tabela `rotulos_de_origem` divergindo da escada** no lado que o site consome. Duas
   cópias do mesmo fato, nenhuma capaz de corrigir a outra — a forma exata dos dois mapas
   de nome que a casca 1.2.0 pagou.
3. **a que não era trava faltando, e sim bancada incompleta:** "o degrau 4 fica sem
   ressalva na escada" passou porque a mutação rodava só `teste-a2.php`. A trava existia
   desde 11/09, no `validar-banco.py`, e não estava sendo chamada. **Mutação no BANCO
   julgada só pelo teste da PÁGINA mede metade do mundo** — a bancada deste arquivo passou
   a ter os dois portões.

A diferença deste arquivo para o irmão da R2 vale ser lida antes do próximo bloco: lá, "a
atribuição volta a ser digitada" era **inerte** com o banco de hoje e precisava PRODUZIR o
mundo em que o defeito aparece. Aqui esse mundo já era o mundo, e a mutação reprova sem
tocar no banco. O banco mutado continua necessário para as duas travas **latentes** — a
atribuição do SEGUNDO número do cartão (a autonomia, hoje da mesma fonte nos cinco) e o
título com degraus misturados. **Trava latente sem mutação que produza o mundo dela é
trava não medida.**

**DE QUEBRA, E NÃO ERA DESTE BLOCO — um conserto estava commitado e fora do ar.** A
bancada acusou `casca: manifest 1.4.0 / snippet 1.4.1`. A ronda de hoje, 14h40Z
(`1ffbdd2`), consertou o `robometria_casca_numeros()` lendo option de `publicar=false` — o
defeito latente que o `ESTADO.md` nomeava — bumpou a casca para 1.4.1 e **não tocou no
manifest**: nem a versão, nem o sha. O Sync não tinha como ver o arquivo novo, então o
conserto passou uma hora commitado e invisível. É a seção 4 ("o site fica para trás em
silêncio") pelo caminho mais discreto de todos, porque aqui nem o desembarque parcial
aparecia no log. Entrou nesta revisão. `atualizar-manifest.py` acusou os dois
descasamentos antes do commit, que é para isso que ele nasceu no bloco anterior.

**NO AR às 15h30Z:** `/status` na **revisão 20**, igual à do manifest, 10 aplicados, **um
disparo**. `conferir-no-ar.py` de 72 para **82 afirmações** no HTML servido, **0 falha** —
as nove URLs em 200, e no A2 os cinco cartões com a linha de procedência com data, a
ressalva do degrau 4, a atribuição da loja oficial, a porta de compra antes da fonte, a
ressalva antes da porta e o link discreto com `nofollow`. **A afirmação mais importante da
lista nova mede a AUSÊNCIA:** a frase "O fabricante declara" sumiu dos cinco cartões —
trava que só confere o texto novo aprova uma página que sirva os dois.

**Receita:** 44 itens esperando link de afiliado (não mudou; este bloco não tocou
catálogo), nenhum com loja possível hoje. Na vitrine do A2, 5 de 5 esperam link.
**Pauta da seção 17:** `pauta.md` ainda não existe — 0 escritos, 0 na fila, 0 recusados.

- **Próximo passo, e desta vez ele sai MEDIDO deste bloco, não lembrado:** a seção
  "Exatamente no limiar" da própria R2 nomeia modelos e Pa e **não cita origem** — é o
  último lugar das duas ferramentas onde um número decide e a origem não aparece, e as
  peças já existem. Junto com ele, um achado pequeno e de receita que este bloco viu e
  **não consertou de propósito, para não alargar o bloco:** os cinco itens da vitrine do
  A2 viajam com `afiliado.sub_id_2 = "R2"`, porque o campo é do MODELO no banco e as duas
  páginas o compartilham. No dia em que o primeiro link entrar, todo clique vindo do
  artigo será contado como se fosse da ferramenta. O conserto não é trocar o valor no
  banco (quebraria a R2): é o gerador de cada página carimbar o próprio código, que é o
  que a seção "Específico desta ilha" do `PROMPT.md` já descreve.

- **Achado de processo, o mesmo de 11/09 com outra roupa:** a ronda de hoje commitou às
  14h40Z e o `ultima_ronda` do `ESTADO.md` continua em `2026-09-11T14:53Z`. O campo é da
  Sentinela e a Fundação não o escreve (seção 2), então ele fica como está — mas é a
  segunda vez que uma ronda trabalha nesta ilha sem gravar a própria data, e da primeira
  vez foi preciso um despacho para fechar. O que muda em relação àquela: **desta vez a
  ronda também não atualizou o manifest**, e foi por isso que o conserto dela ficou fora
  do ar. As duas metades esquecidas são a mesma metade — o registro do que foi feito.

## 2026-09-12 17:23Z — Despacho do GA4: a ilha passa a ser medida (casca 1.5.0, revisao 21)

- **MARCO ZERO DA SERIE DE AUDIENCIA: 12/09/2026, 17h23Z.** E a partir deste
  desembarque que existe medicao de audiencia nesta ilha. Toda leitura anterior
  a esta data e ausencia de tag, nunca ausencia de visita — e a serie em
  `dados/audiencia.md`, que a Sentinela escreve, comeca daqui.
- Despacho de 12/09/2026 em `dados/despachos.md` (prioridade ALTA, FUNDACAO):
  as tres ilhas ganharam propriedade GA4 e nenhuma tinha a tag no ar. Esta
  execucao cumpriu a parte da Robometria; a Aquametria e o Clube do Mosaico
  seguem abertas no despacho, para as execucoes que reservarem cada uma.
- **A tag entra pela casca, nunca por plugin** (secao 11.7 do contrato): a
  pagina publica e territorio deste repositorio, e plugin de medicao seria um
  segundo dono do `<head>` que este repositorio nao versiona.
- **O ID e constante do topo**, `ROBOMETRIA_CASCA_GA4 = G-RM7KS75QP2`, com o
  nome da ilha ao lado. Nao e preciosismo de estilo: e a unica coisa que muda de
  ilha para ilha nesta secao, e ID digitado no meio de uma funcao e exatamente
  o que faz a casca copiada nascer medindo a propriedade da ilha anterior.
- **PRIORIDADE 23, e o porque esta escrito no codigo.** O despacho pede a tag
  cedo E proibe que ela entre antes do `<title>`, da meta descricao ou do
  JSON-LD. As duas metades so cabem juntas depois do ultimo bloco protegido:
  nesta casca eles saem em 1 (o titulo, pelo nucleo), 4 (description e Open
  Graph), 6 (Organization + WebSite), 7 (o JSON-LD de cada ferramenta e de cada
  artigo, nos snippets deles) e 22 (o BreadcrumbList). 23 e o primeiro degrau
  livre acima de todos.
- Script de terceiro com `async`, endereco com **um parametro so** de proposito
  (um segundo traria um `&` dentro de `<script>`, que e o defeito que derrubou
  cinco calculadoras da Aquametria em 08/09/2026), e **nenhum banner de
  consentimento bloqueante** (secao 22.4).
- **O PORTAO MEDE ORDEM, NAO PRESENCA — e essa e a licao deste bloco.** "A tag
  esta na pagina" e a afirmacao facil, e e a que nao protege nada: um JSON-LD
  novo numa prioridade acima de 23 quebra a regra sem tirar a tag do lugar, e
  uma trava de presenca aprova isso com folga. Foi a quinta das nove mutacoes,
  e por causa dela o teste mede a posicao da tag contra o ULTIMO bloco de
  `application/ld+json` servido, nunca contra uma lista do que a casca acha que
  imprime.
- **O ID DESTA ILHA ESTA ESCRITO NA REGUA DOS DOIS TESTES**, e nao lido da
  constante. Ler a constante e compara-la com o que a casca serviu e comparar a
  constante consigo mesma — e o unico erro que essa comparacao nunca pegaria e o
  que vai acontecer de verdade: esta casca foi copiada da Aquametria em
  10/09/2026, a proxima ilha vai copiar esta, e o ID esquecido vai ao ar
  funcionando, sem uma linha de defeito visivel, gravando sessao na propriedade
  errada por meses. Foi a segunda mutacao.
- **A pagina de divulgacao conta o que o site mede**, em duas frases, com a
  origem de IA nomeada — o despacho pedia a frase na pagina de privacidade, e
  esta ilha **nao tem** uma. Enquanto nao tiver, o lugar honesto e a pagina onde
  o site conta como funciona por dentro e que esta no rodape de todas as outras.
  Quando `/privacidade/` nascer, a secao muda de casa. De quebra, o corpo que a
  ronda de 11/09 achou fino (1.325 caracteres, reprovado pela trava de pagina
  fina) cresceu e passou com folga.
- **VERIFICACAO.** Bancada: `teste-casca.php` de 152 para 191 afirmacoes, 0
  falha, com a secao 15 nova (ID servido, async, `gtag('config')` na propriedade
  certa, a tag depois do `<title>`, depois da description e depois do ultimo
  JSON-LD, um unico script de terceiro contado pelo endereco servido, o ID
  aparecendo UMA vez no arquivo da casca e dentro de um `define`, e a frase da
  divulgacao medida no CORPO — no `<head>` a palavra googletagmanager aparece
  nas nove paginas, e medir no HTML inteiro aprovaria uma pagina muda).
  `ferramentas/mutacoes-ga4.py` novo: **9 de 9 reprovadas**, cada uma numa
  afirmacao diferente — a tag sumindo, o ID da ilha vizinha, o `config` medindo
  outra propriedade com o `src` certo, o async caindo, o JSON-LD intruso acima
  da tag, a prioridade caindo para 3, o ID voltando a ser digitado no meio do
  codigo, um segundo script de terceiro na pagina publica, e a pagina parando de
  contar o que mede. As mutacoes so foram aceitas com a bancada verde por baixo:
  na primeira rodada o manifest ainda estava na 1.4.1 contra a constante 1.5.0,
  e **toda** mutacao reprovava tambem por isso — teste que ja esta vermelho nao
  prova mutacao nenhuma.
- Regressao sem uma falha: `teste-arvore` (213), `teste-voz` (155), `teste-r1`
  (90), `teste-r2` (90), `teste-a1` (55), `teste-a2` (73), `teste-acentuacao`
  (17), `validar-banco`, `php -l` em tudo, e as quatro baterias de mutacao
  antigas (18, 29, 11, 15) — **nenhuma virou inerte**.
- **NO AR as 17h23Z, em UM disparo do Sync:** `/status` na revisao 21, igual a
  do manifest. `conferir-no-ar.py` de 82 para **138 afirmacoes, 0 falha**, com a
  conferencia da tag nas nove URLs (ID, async, `config`, ordem contra o
  `<title>` e contra o ultimo JSON-LD, unico terceiro) e a frase da divulgacao
  medida no corpo servido. As nove URLs em 200.
- **A METADE QUE NAO E DAQUI, e ela nao e defeito:** o despacho declara pronto
  tambem quando o Tempo Real do GA4 registrar a visita de verificacao, e este
  ambiente **nao tem** a credencial da conta de servico (`ferramentas/ga4.py`
  responde "Sem credencial: defina GOOGLE_SA_B64..."). O que esta medido daqui e
  a metade que estava quebrada — a tag certa, no lugar certo, no HTML servido.
  A confirmacao no Tempo Real e de quem tiver a credencial: o navegador do
  Raphael, ou a variavel de ambiente das rotinas.
- Rede reconferida como manda a secao 20.2: o dominio da ilha em 200 em duas
  passadas, mais o Sync e o `/status`. Nenhum bloqueio.
- 44 itens esperando link de afiliado (nao mudou; este bloco nao tocou
  catalogo). Pauta da secao 17: `pauta.md` ainda nao existe — 0 escritos, 0 na
  fila, 0 recusados.
- **PROXIMO:** a secao "Exatamente no limiar" da R2, que nomeia modelos e Pa e
  nao cita origem — o ultimo lugar das duas ferramentas onde um numero decide e
  a origem nao aparece, e as pecas ja existem. Junto dele, o `afiliado.sub_id_2`
  dos cinco itens da vitrine do A2, que viajam carimbados como "R2" porque o
  campo e do MODELO no banco e as duas paginas o compartilham: no dia em que o
  primeiro link entrar, todo clique vindo do artigo sera contado como da
  ferramenta, e o conserto e cada gerador carimbar o proprio codigo, nunca
  trocar o valor no banco. Os kits e o 3c seguem parados por rede (politica de
  egresso). Tudo que cria URL espera o reenvio do sitemap no Search Console, que
  e do Raphael.

## 2026-09-12 — A procedencia chega a secao "Exatamente no limiar", e o carimbo de origem sai do banco (R2 1.3.0, revisao 22)

- **O ULTIMO LUGAR DAS DUAS FERRAMENTAS em que a pagina nomeava modelo e numero
  sem dizer de onde o numero veio.** A frase da secao comecava por "Xiaomi E10
  declara exatamente 4.000 Pa" — o modelo como sujeito do verbo declarar, que e
  o fabricante dito sem nome e sem degrau da escada de fontes. O cartao da
  vitrine fechou isso em 11/09 e esta secao ficou para tras **justamente porque
  ninguem a le como recomendacao**, e e por isso que ela passou despercebida: a
  pagina nomeia modelo e Pa aqui com a mesma autoridade que la.
- **SAO DOIS NUMEROS E DUAS PROCEDENCIAS** (sexta decisao do `PROMPT.md`): o Pa
  e do modelo e sai atribuido ao degrau dele, lido de `procedencia_do_pa()` na
  implementacao de referencia; o limiar e da fonte editorial e sai com o nome de
  quem o publica, dentro da mesma frase. Frase que publica dois numeros de
  origens diferentes nao pode atribuir os dois de uma vez.
- Cada item ganhou a ressalva do degrau e a linha "Como sabemos — pagina do
  fabricante, verificado em 09/09/2026 · fonte", no mesmo molde do cartao.
- **A AUSENCIA DA PORTA DE COMPRA DEIXOU DE SER SILENCIO, e isto foi a decisao
  de desenho do bloco.** A regra da secao 7 (porta de compra antes da
  procedencia) existe para o link de fonte nunca ser a unica coisa clicavel de
  um bloco. Aqui a porta nao pode existir: a pagina acabou de dizer que estes
  modelos nao estao acima do limiar, e botao embaixo de uma recusa e recomendar
  assim mesmo. O que a regra proibe e o silencio sobre a ausencia, nao a
  ausencia — entao a pagina declara a ausencia e diz por que. **Trocar um
  silencio por outro nao seria conserto**, e a mutacao que apaga essa frase
  reprova por isso.
- **A CORRECAO QUE NAO APARECE NA TELA E QUE SO VIRARIA NUMERO NO DIA DO
  PRIMEIRO LINK: `afiliado.sub_id_2` saiu do banco.** Ele nomeia a PAGINA que
  levou o clique, e o banco so sabe dizer um valor por registro: os 33 modelos
  traziam `"R2"` e as 18 pecas `"R1"`. So que o mesmo modelo aparece na R2 **e**
  no artigo A2, e a mesma peca na R1 **e** no A1 — entao os dois artigos
  publicavam a vitrine deles carimbada com o codigo da ferramenta irma. Nada
  disso quebra nada hoje; no dia do primeiro link de afiliado, a medicao diria
  que os dois artigos nao vendem nada, **com cara de numero conferido**, e a
  decisao seguinte seria despublicar o que estava vendendo.
- **O A1 TINHA O MESMO DEFEITO e ninguem tinha visto**: o despacho anterior
  nomeou os cinco itens do A2, e o `gerar-a1.py` repassava o `afiliado` INTEIRO
  do registro da peca, entao as quatro pecas dele saiam como "R1". Conserto:
  cada gerador carimba o proprio codigo (`gerar-r1` R1, `gerar-r2` R2,
  `gerar-a1` A1, `gerar-a2` A2), o campo saiu de `modelos-robo.json` e de
  `pecas.json`, saiu da forma do `esquema-banco.json` com o motivo escrito, e
  `validar-banco.py` REPROVA o campo de volta no banco. **Nao se conserta
  trocando o valor no banco, porque nenhum valor unico e certo la.**
- **Campo que parece a regra e nao e, num arquivo publicado, e a mesma familia
  da funcao morta no snippet:** um dia alguem o usa. Por isso ele saiu, em vez
  de ficar zerado.
- **VERIFICACAO.** `teste-r2.php` de 90 para **92** afirmacoes, com a secao 17
  nova medindo a entrada inteira (9 situacoes, 16 itens em 8 delas, um processo
  por situacao), regua propria lida do `esquema-banco.json` e do
  `modelos-robo.json` — nunca do `r2-respostas.json`, que o mesmo gerador
  escreve. `teste-casca.php` de 191 para **200**, com a secao 17 nova: cada um
  dos quatro arquivos de dados carimba SO o proprio codigo, e o banco nao
  carimba nenhum. **O portao mora na casca e nao dentro de cada pagina**, pelo
  mesmo motivo que a porta de compra mora la: e regra de toda pagina desta ilha
  que recomenda item, e pagina nova que copiar um gerador antigo reprova antes
  de existir URL.
- **MUTACOES.** `mutacoes-procedencia.py` de 11 para **17 de 17 reprovadas**;
  `mutacoes-carimbo-de-origem.py` novo, **5 de 5**. Duas licoes delas:
  (a) **a mutacao central do carimbo precisa das DUAS metades** — o gerador
  voltando a ler do banco E o campo voltando ao banco —, porque cada uma
  sozinha e inerte: com o banco limpo o `or "A2"` devolve "A2", e com o gerador
  carimbando o campo no banco e ignorado;
  (b) **o alvo de uma mutacao antiga deixou de ser unico** quando a frase nova
  passou a usar `$m['procedencia']['quem_declara']` — quatro tabs sao um pedaco
  de cinco tabs, e so a quebra de linha desempatou. A guarda de unicidade do
  proprio arquivo pegou isso; sem ela a mutacao teria editado nada e passado
  verde.
- **NO AR as 19h30Z, em UM disparo:** `/status` na revisao **22**, igual a do
  manifest; `conferir-no-ar.py` de 82 para **149** afirmacoes, 0 falha, com a
  secao nova medida no HTML SERVIDO — os dois modelos (escritos literalmente no
  medidor, nunca lidos do arquivo de dados), a frase com as duas procedencias,
  a linha "Como sabemos", a ressalva, o link discreto, a **ausencia de porta de
  compra junto com a frase que a explica**, e a secao servida depois da lista
  principal.
- Regressao sem uma falha: `teste-r1` (90), `teste-a1` (55), `teste-a2` (73),
  `teste-acentuacao` (17), `teste-arvore` (213), `teste-voz` (155),
  `validar-banco`, `php -l` em tudo, e as mutacoes antigas (`a2-procedencia`
  15/15, `arvore` 18/18, `cabeca-e-voz` 29/29, `ga4` 9/9) — nenhuma virou
  inerte. A pagina que este bloco editou foi medida a parte em Chromium a
  360/390/781/782/1200 px: rolagem horizontal 0 px nas cinco, e os tres blocos
  de cada item empilhados em vez de colados. `teste-navegador-arvore.mjs` nas
  nove paginas x seis larguras: 258 medicoes, 0 falha.
- **REDE reconferida (secao 20.2):** dominio da ilha em 200, mais Sync e
  `/status`. Nenhum bloqueio.
- 44 itens esperando link de afiliado (nao mudou; este bloco nao tocou
  catalogo). Nenhuma URL nova e nenhum numero novo. Pauta da secao 17:
  `pauta.md` ainda nao existe — 0 escritos, 0 na fila, 0 recusados.
- **PROXIMO:** a **transcricao da composicao dos kits** (item do `PROMPT.md`),
  que e o que destrava a porta de compra do Kit Performance na consulta ERB30 +
  filtro, e junto dela o item **(e)** da fila do 3c — a recarga dos cinco
  Electrolux que ja declaram cobertura e autonomia, o campo de menor custo e
  maior retorno do banco, porque e ele que completa a frase que e a razao de a
  R2 existir ("a sua casa fica pronta em X minutos"). **As duas dependem de
  rede que hoje esta fechada por politica de egresso** (`wap.ind.br`,
  `mi.com.br`, `xiaomi.com.br`): teste com `curl` antes de escolher o alvo, e
  se continuar fechada a fila cai para trabalho de repositorio. A leva de malha
  (5b) segue travada pela metade humana do despacho de 10/09 — o reenvio do
  sitemap no Search Console, que e do Raphael.

## 2026-09-12, 21h16Z — Bloco 3c, item dos kits: a composicao do ERB30 e do ERB44 transcrita, e o ERB30 sai do vazio

**Manifest revisao 23, `/status` conferido as 21h29Z em UM disparo.** Nenhuma URL
nova e nenhum snippet tocado: mudou o BANCO e, com ele, o que cinco arquivos de
dados publicaveis servem.

**A REDE DE FABRICANTE SEGUE FECHADA, E O CANAL DE BUSCA NAO.** Reconferido como
a secao 20.2 manda, em duas passadas da mesma execucao: `robometria.com.br` em
200 nas duas, `mais.conteudo.wap.ind.br`, `mi.com.br`, `electrolux.com.br` e
`loja.electrolux.com.br` em `000` nas duas, por politica de egresso (o CONNECT
ao proxy morre antes do TLS). O `WebFetch` devolveu `EGRESS_BLOCKED` em
`loja.electrolux.com.br` e em `cuida.electrolux.com.br`. **Mas o canal de BUSCA
alcanca a Electrolux** — foi o que o Clube do Mosaico registrou em 12/09 e vale
aqui igual. Era por esse canal que os dois kits estavam esperando desde 09/09, e
nenhuma execucao tinha testado a distincao entre os dois canais nesta ilha.

**O QUE ENTROU NO BANCO.**
- **ERB30** — composicao completa, com as quantidades que a propria pagina do kit
  declara: `01 Filtro HEPA`, `01 Pano de Microfibra (seco)`, `02 Escovas de
  Varredura de Cantos`. Pedida DUAS vezes, com perguntas diferentes e **sem o
  valor dentro da consulta** (secao 8), as duas devolvendo a mesma lista a partir
  da pagina deste kit. Era a unica peca que servia o ERB30: o modelo nao respondia
  consulta nenhuma, e o kit fechado e justamente o estado em que a R1 sabe que ha
  um kit e nao sabe dizer o que vem dentro.
- **ERB44** — composicao **pela metade, de proposito**. A pagina declara os TIPOS
  e nao as quantidades, e chama a escova de "escovas" sem dizer se e a de cantos
  ou a rotativa central — e o ERB44 tem uma rotativa central vendida a parte.
  Filtro e mop entram confirmados; a escova entra com `tipo: null`, que e como o
  esquema diz "o kit serve e nos nao sabemos dizer este item". **A busca ofereceu
  a composicao do ERB30 como preenchimento e ela foi RECUSADA:** modelo vizinho
  nao declara pelo vizinho, que e a cicatriz do coeficiente do epoxi.

**MEDIDO, pela varredura e nao por contagem de cabecalho:** celulas declaradas de
41 para 45; os **11** cruzamentos em "kit sem composicao" foram a **zero**; a R1
responde em **16** dos 28 modelos publicaveis (era 15) e a Electrolux passa a
**9/9**. Por tipo: filtro 10 -> 11, escova lateral 13 -> 14, mop 10 -> 12. Sete
celulas mudaram de "ha um kit e nao sabemos" para **vazia declarada**, que e mais
honesto e nao menos: o kit realmente nao traz bateria nem reservatorio.

**A RECARGA (item (e) do 3c) MUDOU DE NATUREZA E NAO E MAIS COLETA — igual ao que
aconteceu com os m2 no item (d).** Nenhuma pagina de modelo declara tempo de
carga (conferido nas paginas do ERB60 e do ERB80). O unico numero publicado pela
Electrolux no canal alcancavel esta num artigo de **familia** —
`cuida.electrolux.com.br/artigos/como-faco-para-utilizar-o-meu-robo-aspirador-home-e-experience-com-autonomous-technology`,
24 h na primeira carga e 5 h nas seguintes — e **esse mesmo artigo declara, na
mesma frase, autonomia de 90 minutos**. 90 min nao e a autonomia de nenhum dos
cinco modelos alvo (ERB60/61/62/80 tem 100 e o ERB44 tem 120): o artigo fala de
outro aparelho, e atribuir aquele 5 h a estes seria generalizar de uma linha de
produto para outra. **Foi a propria declaracao vizinha do documento que
desmascarou a atribuicao** — e essa e a regra que vale para toda coleta desta
ilha: quando um documento de familia traz DOIS numeros, o que voce ja conhece
diz se o outro e do seu modelo. Os cinco `motivo_do_null` passaram de "nao
coletado ainda" para a causa medida, com o nome do documento.

**O DEFEITO QUE A PROPRIA TRANSCRICAO DESCOBRIU, e ele estava verde havia
blocos.** Os quatro lacos da secao 3 do `teste-r1.php` — o bloco que justifica o
arquivo existir — varriam a lista da REFERENCIA e indexavam a do PHP pela chave
dela:
1. **Peca a MAIS no lado do PHP nunca era comparada com nada.** Se o snippet
   passasse a recomendar uma peca que a regra da ilha nao declarou, nao havia
   chave por onde encontra-la. Numa ilha cujo produto e compatibilidade, esse e o
   defeito mais caro que existe.
2. **Grupo vazio rodava zero vezes e continuava verde.** Ao transcrever os kits,
   `kits_sem_composicao` zerou em TODOS os modelos e aquela comparacao deixou de
   medir o que foi escrita para medir — a "mutacao inerte" de 11/09, agora do
   lado do teste, e causada pela minha propria entrega.
3. E ao contar por grupo apareceu **um segundo vazio que ninguem sabia**:
   `terceiro`, que nunca mediu nada desde que o arquivo existe.
Conserto: as chaves sao comparadas nos **dois sentidos**, e grupo com zero
aparece nomeado ("<- vazio") em vez de passar calado.

**VERIFICACAO.** `teste-r1.php` de 90 para 93 medicoes. Os oito portoes de
bancada em **898** afirmacoes, 0 falha: teste-casca 200, teste-r1 93, teste-a1
55, teste-r2 92, teste-a2 73, teste-acentuacao 17, teste-arvore 213, teste-voz
155. `php -l` em todos os snippets e ferramentas. `validar-banco.py` aprovado
(os mesmos 2 avisos de variante de antes). **Mutacoes:**
`ferramentas/mutacoes-chaves-da-r1.py` novo, **4 de 4 reprovadas**, e a de "peca a
mais" so a trava nova pega — as outras tres foram escolhidas para passar pelo
portao ANTIGO de proposito (a de grupo vazio deixa 141 frases comparadas, acima
do piso de 100). As **seis baterias antigas** rodadas inteiras para provar que
nenhuma virou inerte: procedencia 17/17, arvore 18/18, cabeca-e-voz 29/29, ga4
9/9, a2-procedencia 15/15, carimbo-de-origem 5/5.

**NO AR as 21h3xZ:** `ferramentas/conferir-kits-no-ar.py` novo — **41 afirmacoes,
0 falha** —, porque o `conferir-no-ar.py` mede as nove URLs no caso-ANCORA e este
bloco mudou paginas que **so existem quando alguem escolhe um modelo**. Ele varre
9 estados de entrada (ERB30 x 5 tipos, ERB44 x 4), com a regua escrita
literalmente dentro do arquivo. `conferir-no-ar.py` rodado tambem: 149
afirmacoes, 0 falha.
**A LICAO DELE, e ela custou uma reprovacao antes de o arquivo servir para algo:**
a primeira versao procurava "nao localizamos" no CORPO e reprovou os cinco
estados que RESPONDEM — porque a frase existe duas vezes na pagina por motivo
legitimo (na promessa do topo e na secao que lista os 12 modelos sem resposta).
Era a heuristica por vizinhanca que a secao 8 proibe, escrita por quem acabara de
citar a secao 8. **Quem decide e a ESTRUTURA:** o bloco vai de `id="resultado"`
ate `rbm-quadro`, e se a fronteira nao for encontrada a conferencia REPROVA em
vez de aprovar por ausencia — que foi o `<body>` da Aquametria.

**O numero de tela nasceu contado, e mudou sozinho:** a home e a R1 servem agora
"cobrindo **16** dos 28 modelos do banco" (era 15), sem ninguem digitar, porque
`casca-fatos.json` e derivado. E o ERB30 saiu da lista dos 12 modelos que a
pagina nomeia como ainda sem resposta.

**Itens esperando link de afiliado: 44** (nao mudou; este bloco nao acrescentou
item ao catalogo, so descreveu o que ja estava la).
**Pauta da secao 17:** `pauta.md` ainda nao existe — 0 escritos, 0 na fila, 0
recusados.

**PROXIMO PASSO, e ele agora tem alvo e canal nomeados.** O canal de busca esta
aberto e e por ele que o 3c anda enquanto o egresso direto nao abrir:
1. **O Kit Performance do ERB80** (`loja.electrolux.com.br/kit-performance-electrolux-para-robo-aspirador-erb80/p`
   e `content.electrolux.com.br/brasil/electrolux/cybertron/kit_performance_erb80/index.html`).
   Ele **existe e nao esta no banco** — achado nesta execucao. O ERB80 hoje so
   responde escova principal; o kit destravaria filtro e mop. **Ficou fora deste
   bloco de proposito:** e registro NOVO, nao transcricao, e as duas leituras que
   fiz dele devolveram so o trio generico ("escovas, filtros e pano de
   microfibra"), sem quantidade e sem o tipo da escova — entao ele entra no nivel
   do ERB44, nao no do ERB30, e quem o gravar precisa saber disso antes.
2. **Pecas da Xiaomi e da WAP com codigo**, que a varredura da R1 aponta como o
   primeiro alvo entre os coletaveis: sao os 8 modelos que a R2 ja recomenda e a
   R1 deixa vazios — a emenda partida entre as duas ferramentas. O canal de busca
   alcanca `mi.com`? Nao foi testado nesta execucao; teste antes de escolher.
3. A leva de malha (5b) **continua travada** pela metade humana do despacho de
   10/09 — o reenvio do sitemap no Search Console, que e do Raphael.

## 2026-09-12, 23h18Z — Bloco 3c: o kit do ERB80 e o pano de microfibra entram no banco, e um pronome sem antecedente sai do ar (R1 1.3.0, revisao 24)

**O que foi entregue.** Dois registros novos em `dados/pecas.json`, colhidos pelo
canal de busca, e uma correcao de frase que estava publicada em tres paginas. O
banco vai de 18 para 20 pecas (16 para 18 publicaveis) e de 33 para 38 pares
peca x modelo declarados. **Nenhuma URL nova.**

**A REDE, reconferida como a 20.2 manda, em duas passadas na mesma execucao:**
`robometria.com.br` em 200 nas duas; `loja.electrolux.com.br`,
`content.electrolux.com.br`, `mi.com.br` e `wap.ind.br` em `000` por politica de
egresso, com o proxy nomeando `connect_rejected`. Nao e intermitencia de tunel: e
politica, e o canal de BUSCA continua alcancando os mesmos fabricantes. Foi por
ele que os dois registros subiram.

### O kit do ERB80, e a previsao deste arquivo estava errada

O `PROMPT.md` dizia, escrito na execucao anterior, que o kit do ERB80 entraria
"no nivel do ERB44": tipos declarados, sem quantidade e **sem o tipo da escova**.
A coleta desta execucao achou o contrario. A pagina do kit no dominio do
**fabricante** (`content.electrolux.com.br/.../kit_performance_erb80/`) descreve
os tres itens **um a um** — filtro HEPA, "escovas laterais, direita e esquerda",
refil de microfibra — e portanto **nomeia a escova pelo tipo**. Ele entra ACIMA
do ERB44.

**A CONFERENCIA QUE SUSTENTA ISSO CUSTOU UMA LEITURA A MAIS, e vale como regua
para toda transcricao desta ilha.** Bloco por item numa pagina de catalogo pode
ser **molde do gerador de paginas**, e molde nao declara nada sobre o produto. O
jeito de separar as duas coisas nao e olhar mais forte a mesma pagina: e ler a
pagina IRMA com a MESMA pergunta. A do ERB44, no mesmo dominio e no mesmo
formato, devolveu so a copia generica ("escovas, filtros e pano de microfibra
originais"), sem um bloco por item. Logo o bloco por item existe na pagina do
ERB80 porque a Electrolux o escreveu la — e, de quebra, **isso confirma
retroativamente que o `tipo: null` da escova do ERB44 foi acerto, e nao
preguica**. E a prima da regra de 12/09 sobre documento de familia com dois
numeros; a diferenca e que ali a declaracao vizinha desmascarou uma atribuicao e
aqui ela CONFIRMA uma.

**A QUANTIDADE FICOU `null` NOS TRES ITENS, de proposito.** "Direita e esquerda"
esta numa frase de BENEFICIO, descrevendo o que escova lateral faz, e nao numa
lista de conteudo de embalagem. Ler dali um "2" seria transformar prosa de venda
em quantidade declarada. A assimetria de custo manda o lado: dizer "o fabricante
nao declara quantas" custa uma frase mais fraca na tela; dizer "2 escovas" e vir
uma faz alguem comprar errado.

**E A BUSCA TENTOU PREENCHER DE NOVO, agora se confessando.** A segunda leitura
devolveu "1 filtro HEPA, 1 pano de microfibra e 2 escovas de canto" dizendo
**textualmente** que era "baseado em kits similares de outros modelos
(ERB10/ERB11/ERB20)". Recusado, pela mesma regra que barrou o preenchimento do
ERB44 em 12/09: modelo vizinho nao declara pelo vizinho. Registrar que a resposta
veio rotulada como analogia e util — nem sempre ela vem.

### O pano de microfibra ERB60/61/62/80, que ninguem tinha pedido

Apareceu na lista de resultados da mesma varredura. E a **primeira peca avulsa
desta ilha a servir o ERB80** e cobre quatro modelos de uma vez. Duas leituras
com perguntas diferentes, uma restrita a `content.electrolux.com.br` e outra a
`loja.electrolux.com.br`, devolveram a mesma lista de compativeis; a quantidade
por embalagem nao esta declarada em nenhuma das duas, entao o registro nao a
carrega. O ERB44 NAO esta na lista, embora esteja na do filtro HEPA com espuma:
ficou como esta declarado, sem estender por semelhanca.

**A licao de fila:** varredura feita para colher UM alvo devolve vizinhos, e aqui
o vizinho era mais barato que o alvo. Vale ler a lista de resultados inteira
antes de fechar a coleta.

### O DEFEITO QUE OS DOIS REGISTROS DESENTERRARAM, e ele JA ESTAVA NO AR

Ao ler a resposta do ERB80 como um leitor le — o que a secao 12 do contrato
manda e a verificacao por regra objetiva nao faz — apareceu isto:

> A Electrolux nao vende a escova lateral avulsa para este modelo: ela vem dentro
> do kit "…". **Ele tambem vem dentro do kit "…"**, que a Electrolux declara
> compativel com ERB80.

**"Ele" quem?** A frase do kit-com-avulso nasceu com pronome em 11/09, e lia
certo por **sorte de ordem**: as frases da resposta saem na ordem do banco, e no
unico caso que existia entao (o filtro do ERB60/61/62) o registro da peca avulsa
vinha antes do registro do kit, entao o pronome caia logo depois da frase que
nomeava o filtro. **O pano de microfibra deu ao mop um avulso**, e a frase do kit
foi emitida na posicao do KIT — depois da escova lateral e ANTES de o mop ser
nomeado. Pronome sem antecedente, em pagina publicada, e nao so no ERB80: no
ERB60, no ERB61 e no ERB62, que estao no ar desde 09/09.

**Oito portoes verdes**, porque todos mediam a frase sozinha — e sozinha ela
estava certa. E a mesma familia do "teste que mede a si mesmo", com uma volta a
mais: aqui nao era a regua que estava errada, era a **unidade medida**. Frase e a
unidade errada quando a correcao depende da frase vizinha.

**A saida NAO foi reordenar a lista.** Reordenar devolveria o verde e deixaria a
dependencia de pe — no dia seguinte, qualquer mudanca de ordem no banco traria o
defeito de volta, calado. A frase passa a **NOMEAR O TIPO** ("O mop tambem vem
dentro do kit…"), nas duas implementacoes, e fica autossuficiente. E literalmente
o que a 5.2 do contrato pede ("frase autossuficiente que sobrevive a ser citada
fora de contexto") e o que a 8 decide ("quem decide e a estrutura, nunca a
vizinhanca").

**A TRAVA, e a prova de que ela reprova.** Secao 14 do `ferramentas/teste-r1.php`:
toda frase de resposta **ABRE** nomeando o tipo de peca de que fala, medido nas
DUAS implementacoes, so na primeira oracao — o nome do tipo aparecendo depois,
dentro do rodape "identifique o item pelo titulo", nao salva uma abertura que nao
nomeia nada. A tabela de nomes e escrita a mao dentro do teste; chamar
`robometria_r1_nome_do_tipo()` faria as duas metades errarem juntas. Ela tambem
conta quantas frases do tipo kit-com-avulso existem e reprova se forem zero:
grade que nao pisa no caso e amostra com nome de grade.

`ferramentas/mutacoes-frase-nomeia-o-tipo.py`, **4 de 4 reprovadas**:
1. a referencia volta ao pronome;
2. o snippet volta ao pronome;
3. **os dois lados voltam juntos** — e esta e a que importa: a comparacao PHP x
   referencia da secao 3 continua VERDE, o numero de frases comparadas nao muda,
   e **so a trava nova pega**. Era exatamente assim que o defeito original
   entrava;
4. o tipo existe na frase, mas so depois do ponto final — a porta dos fundos de
   uma regua que procurasse o nome na frase inteira, mesma familia do "contar
   `&#038;` na pagina inteira".

**A metade NO AR** entrou em `conferir-kits-no-ar.py`, que passou de 9 para 14
estados de entrada: os 5 do ERB80 entraram, cada um cobrando que a resposta
nomeie o tipo e que nenhuma frase abra por "ele/ela tambem vem dentro do kit",
com as duas reguas escritas literalmente dentro do arquivo. Ele confere ainda que
o estado que PRODUZIU o defeito (o mop do ERB80, que tem avulso e kit) esteja
mesmo entre os medidos — senao a trava daria verde sem medir nada.

### E uma mutacao morreu calada por culpa desta propria entrega

Ao rodar as sete baterias antigas para provar que nenhuma virou inerte, uma
passou: "o par peca x modelo volta ao numero digitado", em `mutacoes-arvore.py`.
Ela trocava `"pares_declarados": 32,` por `33,` — **com o numero digitado nos
dois lados**. O banco cresceu, o alvo sumiu do arquivo, e a mutacao passou a
editar coisa nenhuma. E a "mutacao inerte" que aquele arquivo existe para
impedir, agora dentro dele. A irma dela ("a contagem de marcas engorda em um")
tinha o mesmo desenho e so nao caiu porque o numero de marcas nao mudou hoje.

Consertadas: as duas leem o valor de HOJE e somam 1. **A cicatriz do "numero de
tela nasce contado" vale para a bancada, nao so para a pagina** — quem digita um
numero derivado assina um cheque contra o banco de amanha.

### Verificacao

**Bancada, 901 afirmacoes, 0 falha:** teste-casca 200, teste-r1 **96** (era 93),
teste-a1 55, teste-r2 92, teste-a2 73, teste-acentuacao 17, teste-arvore 213,
teste-voz 155. `php -l` limpo em todo snippet e toda ferramenta.
`validar-banco.py` aprovado, com os mesmos 2 avisos de variante — **e ele pegou
sozinho as duas contagens digitadas do cabecalho de `pecas.json`** quando os
registros entraram, que e o portao funcionando.

**Mutacoes, 101 em 8 baterias, todas reprovadas:** a2-procedencia 15, arvore
**18** (depois do conserto acima), cabeca-e-voz 29, carimbo-de-origem 5,
chaves-da-r1 4, **frase-nomeia-o-tipo 4 (nova)**, ga4 9, procedencia 17.

**NO AR as 23h30Z, em UM disparo:** `/status` na revisao **24**, igual a do
manifest, 10 itens aplicados. `conferir-no-ar.py` 149 afirmacoes, 0 falha;
`conferir-kits-no-ar.py` **71** afirmacoes (era 41), 0 falha.

**Itens esperando link de afiliado: 46** (eram 44; os dois registros novos entram
com `afiliado.url` presente e vazio, como manda a secao 7).
**Cobertura:** a R1 continua respondendo **16 dos 28** modelos — o ERB80 ja
respondia escova principal, entao nenhum modelo saiu do vazio —, mas as celulas
sem resposta caem de **123 para 120** (modelo x tipo).
**Pauta da secao 17:** `pauta.md` ainda nao existe — 0 escritos, 0 na fila, 0
recusados.

### PROXIMO PASSO

1. **Pecas da Xiaomi e da WAP com codigo** — segue sendo o primeiro alvo entre os
   coletaveis (os 8 modelos que a R2 ja recomenda e a R1 deixa vazios). O egresso
   direto para `mi.com.br` e `wap.ind.br` foi remedido hoje, duas passadas, `000`
   por politica. **O canal de BUSCA nunca foi testado nesses dois dominios** — e
   foi ele que trouxe os tres kits da Electrolux. Teste a busca antes de declarar
   a coleta bloqueada; foi essa confusao que deixou os kits tres dias parados.
2. **CATEGORIA DESCOBERTA, nao coleta pendente: o `Kit 3 Sacos Descartaveis` do
   ERB80** (`loja.electrolux.com.br/kit-3-sacos-descartaveis-electrolux-para-robo-aspirador-erb80/p`).
   Saco descartavel e consumivel de base autolimpante, e o ERB80 tem base
   autolimpante — mas `tipo_de_peca` nao tem esse tipo no `esquema-banco.json`, e
   acrescentar tipo mexe no seletor da R1, na cobertura e nos portoes. Quem pegar
   decide primeiro **se o tipo nasce**, pela regua da 14.3 (faixa descoberta, nao
   numero redondo). Nao grave o registro antes dessa decisao.
3. **O ERB40 tem Kit Performance proprio e o modelo nao esta em
   `modelos-robo.json`** — achado na mesma varredura. Modelo antes de peca: sem o
   modelo, o par nao tem onde encostar.
4. A leva de malha (5b) **continua travada** pela metade humana do despacho de
   10/09 — o reenvio do sitemap no Search Console, que e do Raphael.

---

## 2026-09-13 — bloco 3c, leva 4: oito peças da Xiaomi **com código**, e o kit que nunca foi kit sai do ar

Manifest **revisão 25**, `/status` conferido às 11h35Z em **um** disparo, 10 itens
aplicados. **Nenhuma URL nova e nenhum snippet tocado** — o dado abriu tudo
sozinho, como o kit do ERB30 em 12/09.

**O NÚMERO DO BLOCO:** a R1 responde agora em **20 dos 28** modelos publicáveis
(eram 16), e o cruzamento com a R2 — a emenda que a varredura de 10/09 nomeou
como urgência número 1 — vai de **3 para 7**. Entrada vazia de 12 para 8, células
vazias de 120 para 112, Xiaomi de 1/7 para 5/7. Saíram do vazio: **E10, H40, S40
e S40C**; o **S20**, que já respondia, passou a responder com código e como peça
avulsa.

**A COLETA SÓ ACONTECEU PORQUE O DOMÍNIO TESTADO ESTAVA ERRADO, e isto vale mais
que a leva.** O `PROMPT.md` e o `ESTADO.md` mandavam testar `mi.com.br` e
`xiaomi.com.br`. O banco desta ilha **sempre** citou `www.mi.com/br` — o endereço
está escrito em sete registros desde 09/09. O egresso direto segue fechado por
política nos três (`000`, 403 ao CONNECT nomeado pelo proxy, duas passadas), mas
a **busca alcança `mi.com`**, e nunca tinha sido testada nele. Três dias de
"coleta bloqueada" eram um domínio digitado errado numa linha de prosa. A lição
não é sobre a Xiaomi: **quando o canal falha, confira o endereço contra o BANCO**,
que é quem guarda a fonte, e não contra o texto que descreve o bloqueio.

**O DEFEITO QUE ESTAVA NO AR, e ele mentia duas vezes na mesma tela.** O registro
`xiaomi-s20-acessorios` leu a página "Xiaomi Robot Vacuum S20 Accessories" como um
**kit** — uma caixa com cinco peças dentro — e ela é um **catálogo de variantes**:
cinco produtos avulsos, cada um com código e pacote próprios ("Package contents:
Mop pad x2", "Side brush x2", "Main brush x1"). A R1 dizia a quem tem um S20 que o
filtro, as escovas e o mop só existem **dentro de um kit** (`dentro_de_kit=true`,
`existe_avulso=false`) **e** que a peça não tem código para procurar. O
`motivo_sem_codigo` de 09/09 — *"a Xiaomi identifica consumível pelo nome do
acessório e pelo modelo compatível, não por código de peça"* — é uma afirmação
sobre o fabricante que o fabricante **desmente na subpágina `/specs/` da mesma
URL**, que publica "Product model" para cada variante. A coleta de 09/09 leu a
página e não a especificação dela.

**A RÉGUA DESTA LEVA, escrita antes de gravar.** A Xiaomi declara compatibilidade
no **título publicado** da peça ("Xiaomi Robot Vacuum E10/E12/E10C/S20 Brush") e o
código mora na `/specs/`. Um par entra quando o modelo é nomeado num título que
aparece na página de acessório **daquele** modelo ou numa página de peça dedicada;
título de **listagem** que nomeia modelo que a especificação não repete vai para
`divergencias` e é resolvido pelo **mais estreito** (seção 10).

Onde isso custou caro de propósito: o mop **E101-TB**. A listagem o chama de
"S40C/H40/S40 Mop Pad" e a especificação, de "S40C Mop Pad". O H40 e o S40 **estão
no banco**, então aqui a escolha muda a tela — e é por isso que ela é a estreita:
errar para o lado largo faz alguém com um H40 comprar um mop que não encaixa.
Ficou só no S40C, com a divergência transcrita.

A **régua da página irmã** (12/09) foi aplicada e passou: a lista de acessórios do
E10 e a do S20 declaram conjuntos **diferentes** por peça — mop e tampa levam o
prefixo `D106`, que é o código do próprio S20, e escova principal e filtro levam
`B112`, da família E10. Página de catálogo que fosse molde não faria essa
distinção.

**O DEFEITO LATENTE QUE ESTA LEVA DESENTERROU, e ele só podia aparecer hoje.** O
esquema diz desde sempre que `compatibilidade[].modelo` é `null` quando o código
aparece na declaração e o modelo ainda não está no banco — e o banco **não tinha
um único par assim**, zero, medido. Duas réguas do `gerar-a1.py` foram escritas
como se o null não pudesse existir:

1. `marcas_atendidas` resolvia o modelo desconhecido para a marca `"?"` e a
   contava. A **primeira** peça com par null fazia `atravessa_marca` virar
   verdadeiro sozinha — e esse é o número que **escolhe entre as duas formas** da
   frase de abertura do A1, cuja tese é que não existe peça universal. O gerador
   anunciou "4 peças atravessam marca" e mandou reescrever o artigo. Nenhuma
   atravessa.
2. A dispersão montava o conjunto com ids de **modelo**, e num `frozenset` os
   vários nulls de uma peça viram **um** elemento só: a B112-ZS (E10/E12/E10C/S20)
   e a B112-CH (E10/E10C/S20) colapsavam no mesmo conjunto — e "conjuntos
   distintos" é publicado como prova de que compatibilidade não se herda.

É o **contrário** da cicatriz de 12/09: lá a régua morreu no dia em que o banco
melhorou; aqui ela dependia de um caso que **nunca tinha acontecido** e nasceu
errada sem poder falhar. **Quem pegou o (1) sozinho foi o `teste-a1.php`**, porque
a régua dele em PHP já ignorava modelo null — "quem confere escreve a própria
régua" pagando exatamente como foi desenhado.

**O que ficou mecânico:** os dois lados passaram a contar **código declarado**,
que o esquema exige em todo par e nunca é null; e nasceu no `teste-a1.php` uma
**terceira conta**, que lê só código declarado e compara com o que foi
**publicado**. Ela existe porque a afirmação que compara gerador e teste fica
**verde quando os dois erram juntos**, que é como esta família de defeito entra
nesta ilha. `ferramentas/mutacoes-par-sem-modelo.py`, **5 de 5** reprovadas: a
quarta **produz o mundo** (quebra gerador e teste juntos, a comparação continua
verde e só a terceira conta pega) e a quinta ataca pelo **dado**, apagando o
código declarado de um par — é o ramo `__sem_codigo__`, que nunca tinha sido visto
reprovando.

**Dois portões pegaram coisa minha, e os dois estavam certos.** O
`teste-acentuacao.php` achou `dominio` sem acento chegando ao corpo servido em
cinco estados, pelo campo `canal` das divergências — texto que a ilha **escreve**
sai acentuado, o banco é ASCII porque **cita**. E o `conferir-kits-no-ar.py`, na
primeira versão da afirmação de ausência de código, procurava o rótulo do cartão
("sem código publicado") e **reprovou uma página certa**: o rótulo existe, mas
fora do bloco de resposta, e a declaração de verdade está na prosa ("este
fabricante não publica código de peça nesta página: identifique o item pelo título
e pela lista de modelos"). Régua trocada pela que mede o **sentido**.

**VERIFICAÇÃO, 0 falha.** Bancada **902** afirmações em 8 portões (`teste-a1` de
55 para 56); `php -l` limpo nos cinco snippets; `validar-banco.py` aprovado — e foi
**ele** que pegou as duas contagens digitadas do cabeçalho de `pecas.json`, de
novo. Mutações: **106** em 9 baterias, todas reprovadas, com as 101 antigas
rodadas inteiras para provar que nenhuma virou inerte. No ar às 11h35Z, em **um**
disparo: `/status` na revisão 25 igual à do manifest; `conferir-no-ar.py` 149
afirmações e `conferir-kits-no-ar.py` **de 71 para 163** — os cinco estados novos
de modelo × tipo medidos no corpo servido, com o código do fabricante conferido
**com maiúscula preservada**, porque é o que a pessoa digita na busca da loja.

**BANCO:** 28 peças (25 publicáveis), 55 pares declarados, **53 esperando link de
afiliado** (eram 46 — as 8 novas nascem com o campo presente e vazio, seção 7).
Pauta da seção 17: `pauta.md` ainda não existe — 0 escritos, 0 na fila, 0
recusados.

### PROXIMO PASSO

1. **A WAP é o que sobrou da emenda — 0/3 modelos — e o alvo TROCOU.** Medido hoje:
   a busca alcança `wap.ind.br`, `loja.wap.ind.br` **e**
   `mais.conteudo.wap.ind.br`, inclusive os **manuais em PDF** (voltaram nomeados
   na busca o do W400 "FW009293 REV00MAI23", o do W1000 "FW010143 REV03ABR25" e o
   do W90 "FW010263 REV00JAN24"); o `WebFetch` do PDF segue `EGRESS_BLOCKED`. E a
   loja da WAP publica página de peça **por modelo** ("Escova Direita Para Robô
   Aspirador de Pó WAP Robot W300", "Escova Rotativa … W90", "Escova Central …
   WSMART") — e **nenhum** desses modelos está em `modelos-robo.json`. O gargalo lá
   é **modelo**, não peça: vale a regra desta ilha, modelo antes de peça.
2. **O S10 e o Mop 2** são os dois Xiaomi que sobraram vazios. O S10 destrava com
   **uma** leitura da `/specs/` da escova lateral de título largo da família E10
   ("S10/E10/X20/S20" e "S10/E10/S12/E12/X20" foram vistos, nenhum ao lado de um
   código — e juntar título de uma página com código de outra seria inventar a
   declaração).
3. **CATEGORIA DESCOBERTA, sem mudança:** o `Kit 3 Sacos Descartáveis` do ERB80 e
   agora também a **tampa de escova D106-BZSZ** do S20. Os dois ficam fora porque
   "saco descartável" e "tampa de escova" não existem no vocabulário
   `tipo_de_peca`, e acrescentar tipo mexe no seletor da R1, na cobertura e nos
   portões. Decida **se o tipo nasce** pela régua da 14.3 antes de gravar.
4. **O ERB40 tem Kit Performance próprio e o modelo não está em
   `modelos-robo.json`** — modelo antes de peça.
5. A leva de malha (5b) **continua travada** pela metade humana do despacho de
   10/09 — o reenvio do sitemap no Search Console, que é do Raphael.

## 2026-09-13, 13h32Z — bloco 3c, leva 5: os cinco modelos WAP que faltavam, e o degrau da loja oficial corrigido

**Bloco de BANCO, zero URL nova.** Manifest na revisão **26**, `/status` conferido
às 13h32Z em **um** disparo (10 aplicados), nenhum snippet reescrito além do que o
Sync atualiza por mudança de dado.

### O QUE ENTROU

A WAP sai de **3 para 8 modelos**: `wap-w90`, `wap-w100`, `wap-w100c`,
`wap-w300` e `wap-wsmart`. Com eles o banco vai a **38 registros, 33
publicáveis**. Era exatamente o gargalo que o `PROMPT.md` nomeava desde 12/09: a
loja da WAP publica página de peça **por modelo**, e nenhum desses modelos estava
no banco. Ordem da ilha cumprida — **modelo antes de peça**.

**Nenhum dos cinco declara Pa**, e isso é medição, não falta de procura: a WAP
publica Pa no W400 (1.400, o piso da faixa do banco) e declara "modos" ou "níveis"
de sucção no resto da linha. Logo a **R2 não muda**: nenhuma faixa de
`cobertura_de_faixa_r2` ganhou ou perdeu elegível. O que esta leva abre é o lado do
modelo.

**O preço está medido e publicado:** a R1 continua respondendo em **20** modelos e
passa a sair vazia em **13** (era 8). A página de metodologia serve os dois
números contados, e mais: 33 modelos publicáveis, 25 peças, 48 pares, 142 de 198
combinações sem declaração localizada. Um bloco que piora um número publicado e o
publica assim mesmo é o desenho da seção 4 do `ARQUIPELAGO.md` funcionando —
cobertura é razão, e o denominador cresceu de propósito, para o numerador poder
crescer na leva seguinte.

### AS DUAS RECUSAS, e elas valem mais que os campos que entraram

1. **Recarga e bateria do W90.** A primeira passada devolveu "4 horas para uma
   carga completa" e "2.600mAh" — os dois de um artigo de **família**, o que
   compara o W90 com o W100, que na mesma passada mistura o W90 com o **W90
   Pérola**: produto diferente, manual próprio (`FW010263 REV00JAN24`) e autonomia
   declarada de 1h20 contra 1h40. A segunda passada, restrita à página do produto,
   não confirmou nenhum dos dois. É a régua que fechou a recarga dos cinco
   Electrolux em 12/09, aplicada de novo: **quando um documento de família traz
   dois números, o que você já conhece diz se o outro é do seu modelo**. E havia
   um segundo sinal no 2.600 mAh: é exatamente a capacidade que o banco já declara
   para o **W1000**, de outra faixa.
2. **Bateria e voltagem do W100, e aqui nasceu regra nova.** A primeira passada
   devolveu "bateria recarregável bivolt com capacidade de 1.800mAh". A segunda,
   feita **só na página do produto**, respondeu que a capacidade em mAh **não está
   detalhada ali**. Isso não é silêncio — é **desmentido**, na própria página de
   onde o número teria vindo. **Segunda passada que nega o campo derruba a FRASE
   INTEIRA, e não só o número**: por isso a voltagem caiu junto, embora "bivolt"
   fosse a metade confortável de acreditar. Aceitar metade de uma frase negada é
   escolher a metade que agrada.

E uma terceira, de método, que a execução cometeu contra si mesma e corrigiu:
**uma das consultas de confirmação do WSMART levava o valor dentro da pergunta**
("reservatório 450 ml?"). A resposta voltou confirmando 450 ml — eco, exatamente a
armadilha que a seção 8 do contrato registra. A passada foi descartada como
verificação e o campo só entrou depois de uma pergunta limpa ("quantos ml tem o
coletor de pó deste robô") devolver o mesmo número. Fica registrado porque a
armadilha é fácil de cair justamente na hora de **confirmar**, e não na de colher.

### O DEGRAU DA LOJA OFICIAL ESTAVA EM DOIS LUGARES AO MESMO TEMPO

Achado ao escrever a fonte do primeiro registro novo: `loja.wap.ind.br` estava
declarada **nível 3 — página do fabricante** nos três registros WAP antigos, e
`loja.electrolux.com.br` estava **nível 4 — loja oficial da marca** desde 09/09. A
mesma espécie de fonte em dois degraus, e a escada tem uma linha só para cada. O
`loja.meupositivo.com.br` do PRA500 estava no mesmo erro.

**A direção saiu da assimetria de custo (seção 10), como toda decisão de fonte:**
errar para baixo custa uma ressalva mais dura na tela ("confira a embalagem" em vez
de "a confirmar no manual"); errar para cima faz a metodologia declarar um rigor
que a ilha não tem — e é o defeito mais caro que existe numa ilha cujo produto é
procedência. **Quatro fontes desceram para 4**, e o efeito está no ar: a coluna
"Temos hoje" da escada, que é contada e não digitada, foi de 64/24 para **60 no
nível 3 e 28 no nível 4**.

Não é correção cosmética: `wap-w400` sustenta com essa fonte o **Pa de 1.400**, que
é o piso da faixa inteira da R2.

### O PISO DIGITADO DA VARREDURA, e ele estava DENTRO da bancada

O `teste-acentuacao.php` é o portão que garante que a ilha não serve português sem
acento, e ele mede o corpo de **um estado de R1 por modelo** — palavra vinda do
banco só chega à tela quando alguém escolhe aquele modelo. Duas afirmações
seguravam essa cobertura com o número **digitado**:

```
rbm_ok( count( $estados ) >= 70, 'a varredura monta 70 estados ou mais', ... );
rbm_ok( $com_r1 >= 28, 'a R1 e medida em pelo menos 28 estados — um por modelo do banco', ... );
```

Os dois eram exatos no dia em que foram escritos e envelheceram calados. Com o
banco em 33, **cinco modelos inteiros podiam sumir da varredura sem uma única
falha** — e a frase "um por modelo do banco" continuava ali, afirmando a cobertura
que a régua tinha parado de cobrar. É a cicatriz do "número de tela nasce contado,
nunca digitado", agora na bancada em vez da página.

A régua passou a **ler `dados/modelos-robo.json`** e a cobrar, **por id**, um
estado para cada modelo publicável. Não há mais número para envelhecer, e quem
apagar um modelo da varredura reprova **nomeando qual**.
`ferramentas/mutacoes-varredura-por-modelo.py`, **3 de 3 reprovadas**: (1) um
modelo some da varredura; (2) a varredura para nos 28 primeiros, que é o defeito
como ele estava vivo; (3) **produz o mundo pelo dado** — um modelo entra no banco e
`r1-respostas.json` continua o de ontem, sem uma linha de código errada, e o modelo
novo não chega a medição nenhuma. A terceira é o caso que a régua antiga não podia
pegar nem em princípio, porque comparava a varredura com um número e nunca com o
banco.

### VERIFICAÇÃO

**Bancada, 0 falha:** `teste-casca` 200, `teste-r1` 96, `teste-a1` 56, `teste-r2`
92, `teste-a2` 73, `teste-acentuacao` 17, `teste-arvore` 213, `teste-voz` 155 —
**902 afirmações**. `validar-banco.py` **APROVADO**, e foi ele que pegou, de novo,
as três contagens digitadas do cabeçalho (total, publicáveis, esperando link) antes
de qualquer outra coisa. **Mutações: 109 em 10 baterias, 109 reprovadas, 0
passaram** — as 106 antigas rodadas inteiras para provar que nenhuma virou inerte
com o banco maior.

**No ar às 13h32Z, em UM disparo:** `/status` na revisão **26**, igual à do
manifest; `conferir-no-ar.py` **149** afirmações e `conferir-kits-no-ar.py`
**163**, zero falha nos dois. E a metade que só este bloco tinha para provar, no
HTML **servido**: os cinco modelos novos no seletor da R1; a resposta de
`?modelo=wap-w300` dizendo, tipo por tipo, "não localizamos declaração do
fabricante … não vamos supor" e **sem bloco de compra**; e a página de metodologia
com os seis números da cobertura e a coluna da escada em 60/28.

**UMA ARMADILHA DE MEDIÇÃO PARA QUEM VIER DEPOIS:** a primeira leitura da
metodologia logo após o desembarque veio do **cache de página** e serviu os números
de 10/09 — 28 publicáveis, 15 respondendo, 116 de 168. Nada estava errado no site:
a mesma URL com um parâmetro qualquer (`?nocache=…`) devolveu os números de hoje no
mesmo minuto. **Conferência no ar logo depois do Sync passa por um parâmetro**, ou
mede a página de antes do desembarque e se chama de defeito.

**BANCO:** 38 modelos (33 publicáveis, 33 esperando link de afiliado), 28 peças (25
publicáveis), 48 pares declarados. `marcas.json`: a WAP ganhou `canal_de_pecas`
(`loja.wap.ind.br/acessorios/para-aspiradores`) — a frase que estava lá, "a busca
não devolveu página de peça de reposição com código", estava errada pela metade.
Pauta da seção 17: `pauta.md` ainda não existe — 0 escritos, 0 na fila, 0
recusados.

**REDE (20.2), remedida hoje:** `loja.wap.ind.br` e `www.wap.ind.br` em **000** na
leitura direta, com `robometria.com.br` em **200** na mesma passada — política de
egresso, não intermitência. A **busca** alcança os dois, e é por ela que esta leva
inteira saiu.

### PROXIMO PASSO

1. **A PEÇA da WAP, e ela está a duas medições de distância — não de rede.** As
   páginas de acessório por modelo já foram varridas (W300 com 9 acessórios em 7
   categorias; WSMART com 9; W90 com escova rotativa e carregador). O que impediu a
   gravação hoje: **(a)** o código voltou em UMA passada e não na segunda
   (`FW006267` escova direita do W300, `FW008028` escova central do WSMART,
   `FW009132` escova rotativa do W90) — e código de peça é o que a pessoa digita na
   busca da loja, então meio confirmado é pior que ausente; **(b)** a página de
   acessório **não declara a função** da escova, e "Direita", "Central", "Frontal"
   e "Rotativa" são nomes — ler `tipo_de_peca` de um nome é a heurística por
   vizinhança que a seção 8 proíbe, a mesma que fez a Xiaomi publicar catálogo de
   variantes como kit. Decida **onde** a função está declarada antes de gravar.
2. **O tipo `reservatorio` pode voltar ao seletor da R1 de graça:** o W300 e o
   WSMART publicam acessório na categoria **Recipiente**, e `reservatorio` é o
   único tipo do vocabulário sem nenhuma peça no banco inteiro — foi por isso que
   ele saiu do seletor.
3. **W90 Pérola, W96, W3000, W4000, W2000 e WConnect** — localizados nesta
   varredura e não gravados, cada um por falta de duas passadas limpas próprias.
   O **W90 Pérola é o mais urgente**: é ele que a fonte de família confunde com o
   W90, e é por causa dessa confusão que dois campos do W90 estão null.
4. **O S10 e o Mop 2** seguem sendo os dois Xiaomi vazios, com o caminho já escrito
   na leva 4.
5. A leva de malha (5b) **continua travada** pela metade humana do despacho de
   10/09 — o reenvio do sitemap no Search Console, que é do Raphael.

---

## 2026-09-13, 15h32Z — bloco 3c, leva 6: as primeiras peças da WAP, e a função da escova vira campo porque o título do fabricante não a declara

**Bloco de BANCO, zero URL nova.** Esquema do banco na **versão 4**, manifest na
revisão **28**, `/status` conferido em **dois** disparos: **27** às 15h29Z com o
banco, **28** às 15h35Z com a lista de compras reescrita e a nota da marca (10
aplicados em cada).

**O número que mede o bloco:** a R1 sai de **20 para 22** modelos que respondem e
o vazio cai de **13 para 11**. W300 e WSMART saem da lacuna que a varredura de
10/09 apontou como urgência número 1 — o lado da emenda que dava para colher.
Banco: **32 peças, 29 publicáveis, 59 pares**.

### QUATRO PEÇAS ENTRAM, UMA É RECUSADA — e a recusa é o achado

| peça | tipo | modelo | função declarada por |
|---|---|---|---|
| Escova Direita Para Robô Aspirador de Pó Robot W300 | escova lateral | W300 | contraste no catálogo |
| Escova Esquerda Para Robô Aspirador WAP Robot W300 | escova lateral | W300 | contraste no catálogo |
| Escova Central Para Robô Aspirador de Pó WAP Robot WSMART | escova principal | WSMART | título |
| Escova Frontal Para Robô Aspirador de Pó WAP Robot WSmart | escova lateral | WSMART | contraste no catálogo |

### A FUNÇÃO NÃO SE LÊ DO NOME DO PRODUTO

O vocabulário desta ilha separa `escova lateral` de `escova principal` — são
**funções**, e é a função que decide se a peça encaixa. O fabricante não nomeia
função nenhuma: batiza pela **posição**. A WAP publica "Escova Direita", "Escova
Esquerda", "Escova Central", "Escova Frontal" e "Escova Rotativa", e nenhuma
dessas cinco palavras está no vocabulário.

**A prova de que ler a função do nome é chute veio da própria fonte, e é o
parágrafo mais importante desta entrada:**

- o conteúdo declarado do **W300** chama de "escovas **giratórias** direita e
  esquerda" o par **LATERAL**;
- o artigo de limpeza do **W90**, no blog da **mesma marca**, chama de "Escova
  Principal (Escova **giratória**)" a **PRINCIPAL**.

Mesma palavra, mesmo fabricante, funções opostas. Quem lesse "Escova Rotativa
para o W90" e gravasse `escova lateral` porque "rotativa parece lateral"
acertaria ou erraria por sorte — e a R1 publicaria o palpite com cara de
declaração do fabricante, que é a única coisa que esta ilha vende.

**Por isso a escova do W90 não entrou.** O catálogo daquele modelo publica **uma**
escova, sem vizinha para contrastar, enquanto o canal de manutenção da própria WAP
declara que o W90 tem **duas**. Não há de onde ler. O que destrava é o manual
`FW010263 REV00JAN24`, nomeado na busca e atrás do egresso fechado — **não é falta
de procura**.

### A SEGUNDA RECUSA: O CÓDIGO, NAS QUATRO

`FW006267`, `FW008028` e `FW009132` voltaram em **uma** passada e **sempre** em
título de marketplace ou de varejista (níveis 5 e 6), **nunca** num canal da WAP.
A segunda passada restrita à loja oficial devolve a página e o título, e **não o
campo da ficha**. Os quatro registros entraram com `codigo_fabricante: null` e
motivo, pela mesma regra que já vale para a Electrolux; o par com o modelo é
declarado pelo **título publicado**, que é a régua escrita na leva Xiaomi de hoje
mais cedo.

Isso corrige pela metade a frase que estava em `marcas.json`: **a ficha tem
código — a busca é que não o alcança.**

### O CAMPO NOVO, E ONDE A LISTA MORA

`funcao{declarada_por, fonte, declarado_como}`, obrigatório nos tipos que o título
do fabricante não separa. Três origens legítimas e só três: o **título**, o
**contraste** do catálogo do fabricante para **aquele** modelo, e o **canal de
manutenção**. As 8 escovas que já estavam no banco foram preenchidas — 5 pelo
título, 3 pelo contraste (as duas Xiaomi "Brush", que só significam "principal"
porque a vizinha se chama "Side Brush", e a Escova Frontal do WSMART).

A lista de tipos mora no **esquema** (`tipos_que_exigem_funcao_declarada`), não
dentro da régua, pelo mesmo motivo que matou o piso digitado do `teste-acentuacao`
ontem: **lista dentro da régua envelhece calada.**

**A mutação que importa é a (6), e ela não estraga registro nenhum.** Tira do
esquema a lista de tipos. Sem a trava que **exige** a chave, o validador passaria a
aprovar tudo em silêncio — banco de hoje verde, peça seguinte entrando sem o campo,
e a falha só aparecendo no dia em que alguém comprasse a peça errada.

**A regra subiu para o contrato como seção 26 do `ARQUIPELAGO.md`**, porque não é
da Robometria: toda ilha com vocabulário controlado classifica pela função e lê
título escrito pelo marketing de outra pessoa.

### DESCOBERTA DE PROCESSO

`blog.wap.ind.br` é **onde a WAP nomeia a função das peças, por modelo** — a loja
nunca faz isso. Até hoje só `wap.ind.br`, `loja.wap.ind.br` e
`mais.conteudo.wap.ind.br` tinham sido testados. Foi o blog que sustentou a recusa
do W90 e o contraste do W300.

### VERIFICAÇÃO

**Bancada, 0 falha:** `validar-banco` APROVADO; **902 afirmações** em 8 portões
(casca 200, r1 96, a1 56, r2 92, a2 73, acentuação 17, árvore 213, voz 155);
`php -l` limpo. **Mutações: 116 em 11 baterias, 116 reprovadas, 0 passaram, 0
inertes** — as 109 antigas rodadas inteiras para provar que nenhuma morreu com o
banco maior. `mutacoes-funcao-da-escova.py`: 7 de 7.

**No ar:** `/status` na revisão **28**, igual à do manifest; `conferir-no-ar` 149 e
`conferir-kits-no-ar` 163 rodados **depois de cada um dos dois disparos** — zero
falha nas quatro passadas. E a medição que só
este bloco tinha para fazer, **no HTML servido** e com parâmetro anti-cache (a
armadilha que o bloco das 13h32Z nomeou):

- `?modelo=wap-w300` serve *"declara a **escova lateral** «Escova Direita…»"* e
  *"a **escova lateral** «Escova Esquerda…»"*, e **não** serve Central nem Frontal;
- `?modelo=wap-wsmart` serve *"a **escova principal** «Escova Central…»"* e
  *"a **escova lateral** «Escova Frontal…»"*, e **não** serve Direita nem Esquerda;
- `?modelo=wap-w90` **não serve nenhuma das cinco** — a recusa vale em produção, e
  não só na bancada;
- a página passou a servir *"Em **11** dos 33 modelos"* onde servia 13.

**Rede (20.2), remedida às 15h17Z:** `robometria.com.br` em **200** na home e no
`/status`; `wap.ind.br`, `loja.wap.ind.br` e `blog.wap.ind.br` em **000** por
`connect_rejected` (política de egresso) **na mesma passada**, e o WebFetch de
`loja.wap.ind.br` devolveu `EGRESS_BLOCKED`. Por isso a coleta inteira saiu por
busca restrita e todas as fontes desta leva são **nível 4**.

### O QUE ESTE BLOCO ABRIU E NÃO FECHOU

1. **A ilha não cumpre a seção 25.2 do contrato**, escrita ontem: *"todo item ganha
   `url_busca` ANTES de qualquer outra coisa; item sem `url_busca` é defeito da
   19.1, sempre."* Medido: `url_busca` **não existe em nenhum arquivo** do banco
   desta ilha, e são **62 itens publicáveis** (33 modelos + 29 peças) sem piso de
   monetização — a ilha está no ar com "link de loja em breve" em todo cartão. Não
   foi consertado aqui porque é esquema + dois geradores + snippet, com portão
   próprio, e não cabe na cauda de um bloco de coleta. **É o maior buraco nomeado
   desta ilha hoje.**
2. **A frase da tela atribui ao fabricante a função que a ilha derivou.** *"A WAP
   declara a escova lateral «Escova Direita…»"* está certo quando a função veio do
   título e **empresta autoridade** quando veio do contraste (3 das 8 escovas). O
   defeito é **anterior** a este bloco — já estava no ar nas duas Xiaomi "Brush";
   o que mudou é que agora ele é **mensurável**, porque `declarada_por` existe.
   Está escrito na seção 26.3 do contrato.


---

## 2026-09-13, 17h22Z — a frase da R1 devolve a função a quem a leu (R1 1.3.0, manifest revisão 29)

**O único defeito de precisão que a ilha tinha no ar, e ele foi nomeado pela execução anterior.** A R1 publicava,
em cinco peças:

> A WAP (loja oficial) declara **a escova lateral** "Escova Direita Para Robô Aspirador de Pó Robot W300"
> compatível com W300 (loja oficial da marca, verificado em 13/09/2026).

A WAP nunca usou a palavra "lateral". Ela batiza a peça pela **posição** — Direita, Esquerda, Central, Frontal —
e o vocabulário desta ilha classifica pela **função**. Quem leu a função no contraste do catálogo dela foi a
Robometria, e a frase emprestava ao fabricante a única coisa que esta ilha vende, que é a declaração dele. A
Xiaomi é o caso extremo: o título dela é só "Brush", e não nomeia nem posição.

**O conserto, e por que o molde mudou em vez de ganhar um remendo.** Onde `funcao.declarada_por` não é `titulo`,
o verbo "declara" passa a recair sobre o que o fabricante **de fato** declarou — o nome da peça e a lista de
modelos — e a atribuição da função vira ressalva própria, ao lado das que a frase já tinha (sem código
publicado, canais que discordam, variante de hardware):

> Escova lateral: "Escova Direita Para Robô Aspirador de Pó Robot W300", que a WAP (loja oficial) declara
> compatível com W300 (loja oficial da marca, verificado em 13/09/2026). **Quem chama esta peça de escova lateral
> é a Robometria, pelo contraste do catálogo do próprio fabricante: o título dela não nomeia a função.**

O tipo continua **abrindo** a frase, porque a régua 14 (toda frase nomeia o tipo de que fala, seção 5.2) mede a
primeira oração e o leitor descobre ali de que peça se fala. Onde o título declara a função — Multi, Positivo,
Electrolux, a "Side Brush" da Xiaomi — **nada mudou**: a atribuição ao fabricante é verdadeira e é a frase mais
forte que a ilha tem.

**A RESSALVA FICOU HONESTA NA SEGUNDA VERSÃO, e isso é medição e não capricho.** A primeira dizia "o título dela
nomeia a posição, não a função" — verdade na WAP e **falsa na Xiaomi**, cujo título é só "Brush" e não nomeia
posição nenhuma. Afirmação em bloco tem o escopo do que foi medido (seção 8 do contrato), e o que vale nos dois
é mais curto: o título **não nomeia** a função. O detalhe de cada caso continua no banco, em
`funcao.declarado_como`.

**POR QUE NENHUM PORTÃO DA ILHA VIA O DEFEITO, que é o achado de processo deste bloco.** Todos comparavam a
frase do PHP com a da referência — e as duas diziam a mesma coisa errada. **Duas metades que erram juntas ficam
verdes.** Por isso o portão 15 novo do `teste-r1.php` não chama `robometria_r1_funcao_derivada()` nem lê o campo
`funcao_declarada_por` de `r1-respostas.json`: os dois são produto de quem escreve a frase. Ele reabre
`dados/pecas.json` e o esquema, recomputa quem é derivada e cobra as duas implementações.

**E ele cobra os DOIS LADOS.** Proibir a atribuição na peça derivada, sozinho, seria atendido por uma frase que
nunca atribui nada a ninguém — e a ilha perderia de graça a autoridade do título do fabricante. Então: derivada
nunca atribui e sempre traz a ressalva; de título sempre atribui e nunca traz ressalva.

**A PRIMEIRA VERSÃO DA RÉGUA TINHA UM BURACO, e quem o mostrou foi a mutação.** Ela procurava só a frase
"Quem chama esta peça de", e a mutação que faz a ressalva sair em **toda** peça escapava dela: com
`declarada_por = titulo` o PHP cai no aviso de origem desconhecida, que começa com outras palavras. Quem proíbe
um texto tem de proibir as formas que o **código consegue produzir**, não a que veio à cabeça de quem escreveu a
régua. Corrigido, a mutação passou a ser pega por dois portões em vez de um.

**O RAMO DEFENSIVO DO SNIPPET PASSOU A SER MEDIDO.** Ele existe porque o Sync entrega dado e código em
requisições separadas: um `r1-respostas.json` com origem de função nova pode chegar ao site **antes** do snippet
que sabe explicá-la, e aí a página não pode publicar a atribuição por omissão. Nenhum caminho do teste passava
por ele — ramo defensivo não medido é ramo que pode mentir à vontade (seção 8). O mundo é produzido no item,
porque o banco nunca gravaria uma origem fora do vocabulário: o validador o impede.

**AS TRÊS MUTAÇÕES QUE PRODUZEM O MUNDO, e a décima, que tem de PASSAR.** O esquema permite
`canal-de-manutencao` como origem de função e o banco **não tem nenhuma peça assim** — é o caso em que a função é
palavra do fabricante, só que dita no manual e não no título, e a ressalva muda de sujeito. Régua escrita para um
mundo que nunca aconteceu nasce sem poder falhar (seção 8, cicatriz de hoje mais cedo nesta ilha), então três
mutações criam a peça que não existe e só então quebram a regra nela. A décima é o mesmo mundo **intacto**: se a
régua reprovasse ali, seria um falso-positivo esperando a primeira peça de manual entrar no banco, e o próximo
coletor aprenderia a ignorá-la.

**VERIFICAÇÃO NA BANCADA, 0 falha:** `teste-r1` 106 medições (era 96), `teste-casca` 200, `teste-a1` 56,
`teste-r2` 92, `teste-a2` 73, `teste-voz` 155, `teste-acentuacao` 17, `teste-arvore` 213, `validar-banco`
APROVADO, `php -l` limpo em tudo. **NAVEGADOR:** 258 medições em 9 páginas × 6 larguras, 0 px de rolagem,
console limpo.

**MUTAÇÕES: 126 em 12 baterias, 125 reprovadas e 1 aprovada de propósito, 0 inertes.** As 116 antigas foram
rodadas inteiras para provar que nenhuma morreu com o molde novo — a de `mutacoes-frase-nomeia-o-tipo`, que é a
vizinha mais próxima, continua reprovando as 4.

**NO AR às 17h32Z, em UM disparo:** `/status` na revisão 29, igual à do manifest, 10 aplicados.
`conferir-no-ar` 149 e `conferir-kits-no-ar` 163 rodados depois do Sync, 0 falha. E a medição que só o ar podia
fazer nasceu como arquivo commitado, `ferramentas/conferir-atribuicao-no-ar.py`, 19 afirmações e 0 falha: as
cinco peças derivadas com a ressalva servida e nenhuma atribuição ao fabricante no corpo, e o
`electrolux-erb60` do outro lado, com a atribuição de título intacta e sem ressalva nenhuma. Ela mede no
**corpo** e imprime o tamanho da página (132 a 136 KB), e o modelo de cada peça sai do gabarito, nunca digitado.

**UMA AFIRMAÇÃO QUE A RÉGUA NÃO PODE FAZER, e está escrita nela:** "nada atribui X ao fabricante" só é cobrada
no modelo em que **todas** as peças daquele tipo são derivadas. Num modelo misto, a mesma frase proibida seria a
frase **certa** da peça vizinha — e cobrar ali reprovaria a página correta, que é como duas réguas desta ilha já
nasceram erradas.

**A REDE (20.2), remedida no começo desta execução:** `robometria.com.br` em 200 na home e no `/status`.

**BANCO, sem mudança:** 38 modelos (33 publicáveis), 32 peças (29 publicáveis), 59 pares. **Nenhuma URL nova,
nenhuma peça entrou ou saiu, nenhum snippet além da R1 foi tocado.** Pauta da seção 17: `pauta.md` ainda não
existe — 0 escritos, 0 na fila, 0 recusados.

**RECEITA:** 29 de 29 peças publicáveis esperando link de afiliado. E o item (a) do bloco anterior continua de
pé e continua sendo o maior buraco desta ilha: **`url_busca` não existe em nenhum arquivo do banco**, e a seção
25.2 diz que item sem piso é defeito da 19.1, sempre.

**PRÓXIMO, com ordem e motivo:** (1) **O PISO DA 25.2** — os 62 itens publicáveis (33 modelos + 29 peças) sem
`url_busca`, com a ilha no ar servindo "link de loja em breve" em todo cartão. Agora ele não tem mais nada na
frente: era o item (2) da ordem anterior porque o (1) era este conserto de frase, e o (1) saiu. É esquema + dois
geradores + snippet, com portão próprio, e é bloco inteiro. (2) o **recipiente de pó** do W300 e do WSMART, a
coleta mais barata que existe hoje — a página já está localizada e `reservatorio` é o único tipo do vocabulário
com zero peça, então a primeira devolve o tipo ao seletor da R1 de graça. (3) W90 Pérola, W96, W3000, W4000,
W2000 e WConnect, localizados e não gravados por falta de duas passadas limpas próprias. (4) o S10 e o Mop 2
seguem sendo os dois Xiaomi vazios. (5) o reenvio do sitemap no Search Console, metade humana do despacho de
10/09, segue travando a leva de malha 5b.

## 2026-09-13 (19h16Z) — O PISO DA 25.2 NASCE NO ESQUEMA E NO BANCO: 62 itens saem de "esperando link" para "com palavra-chave escrita"

Era o item (a) que a execução das 17h22Z deixou nomeado, e ela mesma disse que
era "o maior buraco desta ilha e agora não tem mais nada na frente". Continuava
sendo: `url_busca` não existia em NENHUM arquivo do banco, e os 62 itens
publicáveis (33 modelos + 29 peças) estavam no ar com "Link de loja em breve"
em todo cartão. **Nenhuma URL nova, nenhuma página servida mudou, nenhum
snippet tocado** — este bloco é banco, esquema e portões.

**MEDIDO ANTES DE ESCOLHER O BLOCO.** Rede remedida às 19h16Z como manda a
20.2: robometria.com.br em 200 na home e no `/status`; `shopee.com.br/search`
em 200 servindo casca de JavaScript com **zero** ocorrência de
`shopee.com.br/`; `affiliate.shopee.com.br/offer/custom_link` em 200 servindo
casca com **zero** ocorrência de `custom_link`; `mercadolivre.com.br` em 403.
Ou seja: o encurtamento continua fora do alcance desta nuvem, e a Aquametria
mediu a mesma coisa duas horas antes. As duas ilhas estão na mesma posição, e
viram a chave no mesmo dia.

**A CORRENTE TEM DOIS ELOS E ESTE BLOCO SEPARA OS DOIS.** Escolher a
palavra-chave não depende de sessão de ninguém; encurtá-la num link de
afiliado depende. O que estava na fila esperando o Raphael não era a escolha —
era o encurtamento. Nasce `ferramentas/gerar-busca-de-produto.py`, que escreve
`afiliado.url_busca_produto` nos 62 publicáveis. **No dia em que houver sessão
são 62 colagens e NENHUMA LINHA DE CÓDIGO MUDA.**

**A FRASE DO PRÓPRIO ESQUEMA QUE CONTRADIZIA O CONTRATO FOI REESCRITA, NÃO
ACRESCENTADA.** O campo `afiliado` dizia, com todas as letras, que "quem gera o
link é a Sentinela estratégica, no navegador do Raphael, com teto de
calendário" — e a 25.2 decide o contrário com a palavra do dono citada: "deve
ser 100% automático sem eu tocar" e "nada, nunca, fica na fila esperando o
Raphael". Duas frases em desacordo no mesmo arquivo não são história, são
armadilha: a próxima execução acredita na que ler primeiro.

**O ACHADO DO BLOCO NÃO É DO DADO, É DA MARCA — e ele é desta ilha e de mais
nenhuma.** A 25.3 proíbe escolher produto só por marca porque "marca sem
contexto é armadilha". Ao compor a primeira chave apareceu que **nem o `id` nem
o `nome` das marcas desta ilha serviam para buscar**: o `id` de duas das cinco
é palavra comum do português (`multi`, `positivo`), e o `nome` de duas carrega
texto que envenena consulta de marketplace — "Multi (ex-Multilaser)" levaria
**parêntese** para dentro da busca, e "Positivo Casa Inteligente" gasta três
tokens onde um basta. Nasce `nome_de_busca` em `marcas.json`, obrigatório, para
que marca nova não entre muda. E a armadilha da 25.3 tem aqui uma **segunda
forma, que é do CÓDIGO**: `S20` sozinho é um celular de outra marca, `E10` e
`H40` são código de qualquer coisa, `W90` não diz nada. Por isso o termo de
contexto entra nas DUAS entidades, e não só onde a marca é fraca.

**A ASSIMETRIA ENTRE MODELO E PEÇA É DECISÃO DECLARADA, COM A MEDIÇÃO QUE FALTA
NOMEADA.** Modelo leva o código (`Electrolux ERB60 robo aspirador`) porque o
código do modelo É o nome comercial: ninguém vende "Electrolux robô aspirador".
Peça NÃO leva (`WAP escova lateral robo aspirador`), porque código de peça é SKU
interno de fabricante e o vendedor de marketplace não o digita no título — e
chave com token que ninguém usa traz zero resultado, que é o beco sem saída que
o piso existe para impedir. **O lado que não dá para medir daqui está escrito
em vez de escondido:** a busca da Shopee serve casca de JavaScript, então esta
nuvem não consegue CONTAR resultado nenhum. Entre uma escolha que falha em
"resultado menos relevante" e outra que falha em "beco sem saída", com a
medição indisponível, a seção 8 manda ficar com a que falha conhecido. O
estreitamento é melhoria e já tem dono: a Open API da 25.6, cujo primeiro uso
escrito no contrato é "buscar produto por palavra-chave COM ESTOQUE".

**O QUE ENTROU.** Esquema na versão 5: seis campos novos em `afiliado`
(`url_produto`, `motivo_sem_url_produto`, `degrau`, `url_busca`,
`url_busca_produto`, `motivo_sem_url_busca`) e o bloco `escada_de_compra` com
os quatro degraus da 25.1 nomeados, a base da busca, o termo de contexto por
entidade e a regra de composição. Sete invariantes novas. `nome_de_busca` nas
cinco marcas. 62 chaves escritas, **50 distintas** — 7 chaves cobrem 19 itens,
e essa é a largura medida da escolha de não pôr o código da peça, publicada em
vez de escondida.

**VERIFICAÇÃO NA BANCADA, 0 falha.** `teste-escada-compra.py` nasce com **487
afirmações** e régua própria: ele não importa o gerador nem o validador, porque
duas metades que erram juntas ficam verdes — foi exatamente assim que a
atribuição da função da R1 passou por todos os portões até hoje de manhã. Dez
chaves-âncora escritas à mão, cada uma uma borda (a marca cujo nome de tela tem
parêntese, o modelo cujo código sozinho é um celular, a peça sem
`codigo_fabricante`, a peça que o fabricante batiza pela POSIÇÃO). E duas
afirmações que existem para a régua não envelhecer calada: **o conjunto de
marcas e o de entidades que ela conhece tem de ser igual ao do banco e ao do
esquema**, então marca nova REPROVA em vez de passar por cima. `validar-banco`
APROVADO com a versão 5. Resto da bancada rodado inteiro: teste-r1 106,
teste-r2 92, teste-a1 56, teste-a2 73, casca 200, voz 155, acentuação 17,
árvore 213; `php -l` limpo.

**MUTAÇÕES: 143 em 13 baterias, 0 INERTES.** As 126 antigas rodadas inteiras
porque este bloco reordenou o campo `afiliado` nos dois arquivos de banco — e
todas seguem reprovando. A bateria nova, `mutacoes-escada.py`, tem 17 e é mais
dura que as irmãs em duas coisas. (1) **Cada mutação declara qual portão tem de
reprová-la e com que palavra**, e o runner confere a palavra na saída: defeito
pego pela regra vizinha prova que ALGUMA trava existe, não que ESTA existe.
(2) **A maioria PRODUZ O MUNDO**, porque a ilha tem 62 publicáveis e ZERO ficha
de produto — as travas de `degrau`, de `url_produto` e de "degrau 3 sem piso"
nasceram hoje sobre um banco que nunca as exercita, que é a "régua escrita para
um mundo que nunca aconteceu" da seção 8. As quatro últimas criam o **primeiro
link de afiliado desta ilha** dentro da cópia e só depois quebram a regra nele;
a última entrega esse mundo INTACTO e **tem de passar**, senão a régua seria
falso-positivo esperando o dia da monetização.

**UMA MUTAÇÃO NASCEU INERTE E QUEM MOSTROU FOI A PRÓPRIA BATERIA.** A que faz a
marca voltar a ser buscada pelo nome de tela só editava `marcas.json`, e o
portão seguia verde — porque a chave já gravada no banco não muda sozinha.
Mutação que não regera mede a intenção de quem a escreveu, não o que a máquina
produz. O conserto rendeu **duas** mutações em vez de uma, e a segunda vale por
si: com o `marcas.json` mudado e o banco NÃO regerado, as duas cópias do mesmo
fato ficam em desacordo — e quem vê isso é o **validador**, que lê a marca do
arquivo, nunca o portão, que tem o token escrito à mão. Sem ela ninguém saberia
que o portão sozinho não enxerga essa divergência.

**A DÍVIDA DEIXOU DE SER PROSA E VIROU NÚMERO CONTADO**, recomputado do arquivo
pelo validador e nunca digitado: `itens_com_ficha` 0 de 62, `itens_sem_piso` 62
de 62, `links_sem_degrau` 0 de 0. Enquanto era prosa, o cabeçalho dizia "nenhum
link de loja em nenhum cartão" e **não dizia que 62 estavam sem PISO**, que é
outra coisa e é a que a 25.2 chama de defeito.

**O QUE ESTE BLOCO NÃO FEZ, COM NOME E MOTIVO.** A escada NÃO CHEGOU À TELA, e
é escolha declarada, igual à que a Aquametria fez às 17h20Z sobre a mesma
cláusula. Com `url_busca` vazia nos 62, o estado em que a busca vira botão
**nunca acontece**, e a linha discreta do outro estado não tem para onde
apontar: seria refatoração em quatro superfícies (R1, R2, A1, A2) provadamente
dormente, e meia refatoração em quatro superfícies que discordam em silêncio é
pior que nenhuma. O cartão continua dizendo "Link de loja em breve" — que é
verdade hoje e deixa de ser no minuto em que houver sessão.

**NO AR às 19h35Z, em UM disparo:** `/status` na **revisão 30**, igual à do
manifest. **Nenhum arquivo `publicar: true` mudou um byte** — os quatro
geradores e o de casca foram rodados e os nove derivados saíram com o MESMO
sha256, e era essa medição que decidia se este bloco tocava o ar. O log do Sync
diz "10 aplicado(s)" e isso não contradiz o parágrafo: o disparo vai com
`forcar=1`, que reaplica os publicáveis **tenha o conteúdo mudado ou não**, e
dizer que ele aplicou zero seria ler o campo errado. O que prova que a tela não
mudou são os sha256 iguais e as **331 afirmações medidas no ar DEPOIS do
Sync**: `conferir-no-ar` 149, `conferir-kits-no-ar` 163 e
`conferir-atribuicao-no-ar` 19, **0 falha nas três**. Os três portões novos
ENTRARAM no manifest, então a dívida de arquivo fora dele não cresceu com este
bloco — e ela foi **contada** em vez de repetida: são **13** arquivos fora do
manifest, não os 23 que o cabeçalho anterior vinha carregando.

**Próximo passo desbloqueado:** o RECIPIENTE DE PÓ do W300 e do WSMART — a
coleta mais barata que existe hoje, com a página já localizada, e
`reservatorio` é o único tipo do vocabulário com zero peça, então a primeira
devolve o tipo ao seletor da R1 de graça.

---

## 2026-09-13 (21h16Z) — O TIPO `reservatorio` DEIXA DE SER ZERO: os dois recipientes de pó da WAP entram, e a borda da 16.5 passa a produzir o mundo

**Ilha escolhida pela rotação da seção 1**, sem despacho aberto em nenhuma das
três (os três `PROMPT.md` foram lidos antes de escolher, e a 18.1 não se
aplicou). A robometria era a de `ultima_execucao` mais antiga (19h16Z, contra
19h17Z da clubedomosaico e 19h35Z da aquametria), com `executando_desde: null`
nas três — e pela 1.1, `null` já significa que nenhum bloco da Fundação está
vivo, então o git não precisou desempatar nada. Reserva escrita às 21h16Z e
**empurrada de primeira**; ela foi renovada às 21h29Z, no commit do bloco,
porque a execução passou dos 40 minutos. O push do bloco foi recusado uma vez
(duas outras execuções reservaram clubedomosaico e aquametria nesse intervalo),
resolvido com `fetch` + `rebase` — **nenhum force push**.

**O alvo era o mais barato da lista de compras, e por um motivo que não é
tamanho:** as páginas dos dois recipientes já estavam localizadas desde a leva
de escovas da manhã, e `reservatorio` era o **único tipo do vocabulário com zero
peça no banco inteiro** — por isso estava fora do seletor da R1 desde 10/09. A
primeira peça dele devolvia o tipo **de graça**, porque o seletor é **gerado da
varredura e nunca digitado**. Foi o que aconteceu: `tipos_sem_nenhuma_peca_no_banco`
ficou **vazio pela primeira vez na história da ilha**, e nenhuma linha de código
mudou para isso.

**O QUE ENTROU NO BANCO — dois registros, e a assimetria entre eles é a medição:**

- `wap-recipiente-de-po-w300`, "Recipiente de Pó Para Robô Aspirador de Pó WAP
  Robot W300", **sem código de fabricante**. E a ausência foi **procurada**, não
  presumida: duas passadas próprias, uma delas com o título entre aspas somado ao
  token `FW`, não devolveram código em canal nenhum — nem da WAP, nem de
  marketplace.
- `wap-fw008024`, "Recipiente de Pó Para Robô Aspirador de Pó WAP Robot WSMART",
  **com código**. É o **primeiro código de fabricante WAP do banco**, e ele entra
  pelo critério que a leva de escovas escreveu ao **recusar** três códigos hoje
  de manhã. O que reprovava FW006267, FW008028 e FW009132 não era o formato nem a
  marca: era o **canal** — apareceram em UMA passada e sempre em título de
  marketplace ou de varejista (níveis 5 e 6), nunca num canal da WAP. FW008024
  passa nesse mesmo critério, e a prova está em **quatro passadas**: três
  restritas aos domínios da WAP e uma **sem restrição nenhuma**, com o código
  entre aspas, em que a página da loja oficial volta entre os primeiros
  resultados **ao lado de dois anúncios de marketplace que nomeiam o MESMO
  produto**. Canais independentes concordando sobre **qual peça** o código nomeia
  é mais forte do que qualquer um deles sozinho.

**O que continua não sendo possível, dito em vez de escondido:** ler o campo
"Referência" na ficha. `loja.wap.ind.br` segue em `EGRESS_BLOCKED` (medido nesta
execução: os três domínios da WAP em `000`/`connect_rejected`, `robometria.com.br`
em 200 na mesma passada, e o WebFetch da loja recusado pelo proxy). Por isso o
nível das duas fontes é **4, e não 2**. Os 300 ml e os 450 ml que os modelos
declaram **já estavam** em `modelos-robo.json` antes desta coleta e bateram com o
que a busca devolveu — **corroboração, não fonte**: capacidade é atributo do
MODELO e não foi copiada para a peça.

**O DEFEITO QUE O PRÓPRIO BLOCO ACORDOU, e ele é o achado da execução.** Assim
que o reservatório deixou de ser vazio, `teste-arvore.php` **reprovou** — e
reprovou dizendo, com todas as letras, `tipos vazios: NENHUM — esta afirmacao nao
mede nada`. A afirmação "tipo sem peça nenhuma não vira categoria, **e a borda
existe no banco de hoje**" dependia de o banco **conter** a borda. É uma régua que
o **crescimento saudável do banco desliga**: no dia em que a ilha cobrisse todos
os tipos, a trava da 16.5 deixaria de ser exercitada exatamente quando a árvore
ficasse mais fartamente povoada. Ela estava certa em gritar, e é o melhor
comportamento que uma régua dessas pode ter — gritar em vez de virar verde
silencioso.

**O conserto não foi afrouxar nem apagar: foi FABRICAR o mundo.** Saiu uma
afirmação e entraram sete. Uma mede o **mundo real** (nenhum tipo vazio tem
categoria declarada hoje). Uma cobra que **exista** categoria de peça na árvore
para a borda poder ser produzida. E cinco produzem o mundo, **uma por categoria
declarada**: esvaziam o tipo daquela categoria e exigem que a trava aponte
**exatamente ela**, comparando com a **linha de base** e não com lista vazia —
comparar com vazio faria as cinco repetirem o mesmo defeito no relatório em vez
de cada uma dizer o que pegou. Enquanto existir uma categoria de peça na árvore,
essa afirmação tem o que medir: não há banco que a desligue.

**A MUTAÇÃO DO RESERVATÓRIO FICOU INERTE PELO MESMO MOTIVO, e foi re-apontada.**
"Nasce a categoria de reservatórios, que não tem uma peça sequer" continuava
sendo reprovada — mas pela regra **vizinha**, a de documento e código
divergentes. *Defeito pego pela regra vizinha prova que ALGUMA trava existe, não
que ESTA existe.* Agora ela esvazia o tipo, declara a categoria **e** acerta o
`ARVORE.md`, tudo na mesma cópia, e a 16.5 volta a ser a trava medida — as
falhas saíram de 2 genéricas para as 2 que nomeiam a 16.5. Nasceram os auxiliares
`troca_n` (alvo legitimamente repetido, com a contagem **declarada**, para que
banco maior faça a mutação **parar** em vez de editar linhas que ninguém previu)
e `varias` (mutação de mais de um arquivo). E nasceu uma **mutação nova**, a
única que faz a trava do **mundo produzido** reprovar: a casca declara uma
categoria de peça que o vocabulário do banco não conhece.

**A CONFERÊNCIA NO AR DESTE BLOCO PRECISOU EXISTIR, e os três conferidores
antigos mostram por quê:** `conferir-no-ar` (149), `conferir-kits-no-ar` (163) e
`conferir-atribuicao-no-ar` (19) passaram **verdes depois do desembarque sem
tocar uma linha do que mudou** — nenhum deles sabe o que é um reservatório. Dar o
bloco por entregue com 331 afirmações verdes que não medem a mudança é a cicatriz
"VARRER A ENTRADA INTEIRA, NÃO O CASO-ÂNCORA" da seção 8. Nasce
`conferir-reservatorio-no-ar.py`, **25 afirmações em quatro estados**, com régua
escrita literalmente no arquivo (não lida de `pecas.json`: conferência que deriva
do mesmo lugar de onde a página deriva erra junto com ela).

- **A âncora**, e nela a **promessa cumprida**: os seis tipos no seletor, e a
  frase "o seletor acima não oferece..." **sumida**. Ela terminava com *"o tipo
  volta ao seletor no dia em que a primeira peça dele entrar"* — a página fez uma
  promessa em 10/09 e hoje ela é cobrada por um portão.
- **Os dois estados que respondem**, com a assimetria cobrada: o W300 cita o
  **título** e **não pode citar código nenhum** (`fw\d{6}` no bloco da resposta
  reprova), o WSMART cita **FW008024**.
- **O estado NEGATIVO**, sem o qual os três de cima têm porta dos fundos: o ERB60
  consultado por reservatório **tem de recusar**, e a recusa não pode vazar nem o
  título do W300 nem o código do WSMART. Sem ele, uma página que respondesse
  qualquer coisa a qualquer consulta passaria.

**E A RÉGUA DE AR FOI VISTA REPROVANDO — o problema que ela tem por ser de ar, e
como ele se resolveu.** Conferência no ar não se muta: o site é um só, e fabricar
o defeito nele seria **publicar defeito para depois medi-lo**. A saída foi separar
o que a régua **afirma** do lugar de onde ela **lê**: com `RBM_BANCADA` no
ambiente ela lê cada estado de um arquivo renderizado em vez da rede. Para isso,
`render-para-teste.php` ganhou dois argumentos (modelo e tipo) que entram pelo
**filtro `robometria_r1_entrada`** — o caminho que o próprio snippet já oferece a
quem monta a página fora do WordPress, e **não** `$_GET` forjado, que o
`teste-r1.php` proíbe o snippet de usar e que mediria um caminho que o site não
tem. Até hoje o render solto só sabia produzir o caso-âncora, e é por isso que os
estados de consulta nunca tinham sido medidos fora do ar. `mutacoes-reservatorio.py`:
**5 mutações reprovadas e 1 mundo intacto aprovado**, cada uma montando a ilha
inteira num diretório temporário, quebrando UMA coisa, regerando o catálogo da R1
e renderizando os quatro estados. O site não foi tocado.

**O QUE ESTE BLOCO NÃO FEZ, com nome e motivo:**

- **`/pecas/reservatorios/` não nasceu**, e não é esquecimento: a própria tabela
  do `ARVORE.md` exige **3 filhas de dado real** e há **2** peças, de uma marca
  só. A terceira peça de reservatório é o que abre a linha — não uma decisão de
  desenho. O parágrafo do `ARVORE.md` que dizia "não tem **nenhuma** peça
  declarada" **virou mentira no mesmo dia** e foi reescrito com o motivo novo:
  prosa que descreve o problema também envelhece calada.
- **A chave de busca dos dois recipientes é a mesma** — `WAP reservatorio robo
  aspirador` — e isso é propriedade do desenho da 25.2, não deste bloco: a chave
  de PEÇA não leva código porque vendedor de marketplace não digita SKU no
  título. **Este bloco mediu a outra metade disso**, e ela está escrita aqui
  porque vale para os 31 itens de peça: os dois anúncios de Mercado Livre que
  apareceram na passada sem restrição chamam a peça de *"Recipiente Para
  Aspirador De Pó Wap Robot Wsmart"* — **o vendedor digita o MODELO**. Uma chave
  que nomeasse o modelo para a peça declarada em **um só** modelo seria mais
  estreita; para as peças de família (a B112-CH atravessa cinco modelos) não há
  modelo único a nomear. É bloco próprio, com portão próprio, e não cabia aqui.
- **A frase da R1 para peça COM código cita só o código**, e para peça sem código
  cita o título. É o formato estabelecido da ilha (Multi, Positivo e Xiaomi saem
  assim), e foi mantido. Registro do que isso significa **nesta marca**: como o
  vendedor da WAP não usa o código no título, quem procurar "FW008024" num
  marketplace acha menos do que quem procurar o nome — mas quem compra não segue a
  frase, segue a escada, e a escada usa a palavra-chave, não o código.

**VERIFICAÇÃO NA BANCADA, 0 falha:** `teste-casca` 200, `teste-r1` 106,
`teste-r2` 92, `teste-a1` 56, `teste-a2` 73, `teste-voz` 155, `teste-acentuacao`
17, `teste-arvore` **de 213 para 219**, `teste-escada-compra` 503,
`validar-banco` aprovado, `php -l` limpo em tudo.
**MUTAÇÕES: 14 baterias, 0 inertes** — `arvore` 19 (eram 18), `reservatorio` 6
(nova), `a2-procedencia` 15, `cabeca-e-voz` 29, `procedencia` 17, `ga4` 9,
`funcao-da-escova` 7, `carimbo-de-origem` 5, `par-sem-modelo` 5, `chaves-da-r1` 4,
`frase-nomeia-o-tipo` 4, `varredura-por-modelo` 3, mais `atribuicao-da-funcao` e
`escada`, que declaram trava a trava. As antigas rodaram **inteiras** porque o
banco mudou.
**NAVEGADOR:** 258 medições em 9 páginas × 6 larguras, 0 px de rolagem
horizontal, console limpo.
**NO AR**, manifest na revisão **31**, `/status` conferido às 21h30Z em UM
disparo (10 aplicados, 14 aguardando desembarque), e as quatro conferências
rodadas **depois** do Sync: `conferir-no-ar` 149, `conferir-kits-no-ar` 163,
`conferir-atribuicao-no-ar` 19 e `conferir-reservatorio-no-ar` 25 — **0 falha nas
quatro**. **Nenhuma URL nova, nenhum snippet tocado.**

**RECEITA (seção 7), contada do arquivo:** 31 peças publicáveis e 33 modelos
publicáveis, **64 itens publicáveis, 0 com ficha de loja, 64 sem piso** — os dois
recipientes entram no **terceiro degrau** da escada da 25.1, com a palavra-chave
escrita e sem o encurtamento, e os cartões deles dizem "Link de loja em breve",
medido no ar. Nenhum modelo saiu do vazio da R1 (W300 e WSMART já respondiam), e
não era para sair: o que este bloco tirou do zero foi um **tipo**, não um modelo.
Pauta da seção 17: `pauta.md` ainda não existe — 0 escritos, 0 na fila, 0
recusados.

**Próximo passo desbloqueado:** o RECIPIENTE DE PÓ dos outros modelos WAP — o
catálogo publica a categoria "Recipiente" e a ilha tem **6 modelos WAP no vazio
da R1** (W400, W1000, W310, W100, W100c e W90). A terceira peça de reservatório
abre `/pecas/reservatorios/` pelo mínimo de 3 filhas do `ARVORE.md`, e cada
recipiente de um modelo que hoje não responde **tira o modelo do vazio**, que é o
critério da lista de compras. Depois dele, a chave de busca que nomeia o modelo
para peça de modelo único, com a medição dos títulos de marketplace já feita
acima.

## 2026-09-13, 23h18Z — O recipiente do W100 e do W90 entra, e quem diverge passa a decidir a frase

**Manifest na revisão 34**, `/status` conferido com a revisão batendo com o
manifest. **Nenhuma URL nova, nenhuma URL mudou.** R1 1.4.0, casca 1.5.1.

**Escolha da ilha.** Rotação da seção 1, sem despacho aberto para a Fundação em
nenhuma das três (os três `PROMPT.md` lidos antes de escolher; o que resta nos
desta ilha é a metade **humana** do reenvio do sitemap). A robometria tinha a
`ultima_execucao` mais antiga e as três estavam com `executando_desde: null` —
pela 1.1, o `null` já significa que não há bloco da Fundação vivo, então o git não
precisou desempatar. Reserva às 23h18Z empurrada de primeira; nenhum push
recusado, nenhum force push.

### O que entrou

O **Kit Recipiente de Pó FW008543**, declarado pela loja oficial da WAP para o
**WAP Robot W100** e para o **WAP Robot W90**. É a **terceira** peça de tipo
`reservatorio` e a primeira peça WAP a tirar **dois** modelos do vazio da R1 de
uma vez: a ferramenta passa a responder em **24 dos 33** modelos publicáveis e o
vazio cai de 11 para **9**. Era o item (1) do PRÓXIMO da execução das 21h16Z, e o
critério daquela lista era exatamente este — cada recipiente de um modelo que hoje
não responde tira o modelo do vazio.

**O código passou no critério de canal** que a leva de escovas escreveu ao recusar
`FW006267`, `FW008028` e `FW009132`: `FW008543` voltou em passada restrita aos
domínios da WAP, com a página da loja oficial entre os resultados, **e** em
passada sem restrição nenhuma, em que quatro canais independentes entre si
(Americanas, Amazon, Mercado Livre e um varejista de peças) nomeiam o **mesmo**
produto com o **mesmo** código.

**Por que o tipo é `reservatorio` e não `kit`**, que é a palavra do próprio
fabricante no título: a seção 26 do contrato diz que o fabricante batiza pela
posição ou pelo marketing e a ilha classifica pela **função**, e a função está
escrita literalmente no título. O tipo `kit` deste esquema exige `composicao` com
um item por peça separada, e a WAP não declara composição nenhuma. A direção saiu
da assimetria de custo da seção 10: gravar `reservatorio` faz a R1 deixar de
oferecer esta peça a quem procura **filtro**, que é uma frase mais fraca; gravar
`kit` com a composição lida em **varejista** faria a R1 dizer a alguém que o
filtro dele vem nesta caixa, com a autoridade do fabricante emprestada a quem só
revende.

### A recusa, que vale mais que o que entrou

Os revendedores declaram o mesmo código para até **cinco** modelos, e um deles é o
**W100C**, que está no banco desta ilha e está no vazio da R1. Estender por
vizinhança tiraria um **terceiro** modelo do vazio hoje — e o próprio varejo deu o
argumento contra: **dois anúncios do mesmo código, na mesma loja, declaram
conjuntos diferentes** (um diz W90/W95/W96/W100/W100C, o outro diz W100/W100C).
Canal que discorda de si mesmo não promove modelo nenhum. As três declarações
foram para `divergencias`, com a `resolucao` escrita, e o caminho de volta também:
a vista explodida VEG02.122 do W100C existe em `mais.wap.ind.br`, e uma leitura
dela declara ou nega o par no canal do fabricante. W95 e W96 não estão no banco de
modelos desta ilha.

### O achado, e ele estava no ar

A cauda da frase da R1 era **fixa** — *"Dois canais do fabricante discordam sobre
o alcance desta peça"* — e o **título** do bloco de divergências dizia o mesmo. As
duas eram verdadeiras **por acidente do banco**: as sete divergências de peça
existentes vinham todas de canal de fabricante. Este registro fez as duas
emprestarem a autoridade do **fabricante** a três anúncios de revendedor, e **oito
portões seguiram verdes**, porque nenhum deles media **quem** diverge. E "Dois"
era a cicatriz do número de tela digitado, já paga duas vezes nesta ilha.

**O conserto não foi reescrever a frase:** o número sai **contado** e o lado é
**lido** do degrau que cada divergência declara. Nasceu `fala_pela_marca` na
escada de fontes do esquema — a fronteira mora lá para que degrau novo declare de
que lado está sem uma linha de código mudar — e `origem` passou a ser obrigatória
em toda divergência de **peça**, com o validador cobrando as duas. As origens das
sete divergências antigas não foram classificadas de fora: foram **lidas** da
fonte do próprio registro que publica aquele mesmo canal. O rodapé da casca, que
descreve o método em **toda** página, dizia só a metade que o banco tinha no dia
em que foi escrito; e a metodologia perdeu a contagem digitada de casos.

**A mutação que passou foi o segundo achado**, e é da mesma família do `>` trocado
por `>=` que a R2 pagou em 11/09: mover a fronteira no esquema deixava a bancada
**inteira** verde, porque a régua derivava o lado do mesmo arquivo que ela
conferia e as três metades erravam juntas. A fronteira passou a ser escrita **à
mão** dentro do `teste-r1.php`, e o esquema é conferido contra ela.

**O terceiro achado veio da régua de ar nova reprovando**, e o defeito era do
**localizador**: os dois conferidores delimitavam "a resposta" de `id="resultado"`
até o primeiro `rbm-quadro` — e `rbm-quadro` é a classe de **qualquer** quadro,
inclusive o de **divergências**, que fica **dentro** da resposta. O bloco medido
terminava exatamente no começo dele, então a tabela que publica os modelos que só
o varejo declara estava no ar **sem régua nenhuma lendo**, desde que a primeira
divergência existe. A tabela pré-renderizada ganhou `id="rbm-exemplos"` e os dois
conferidores param nele: fronteira de teste tem de ser marcador escrito, nunca "a
primeira coisa parecida com uma tabela".

### Verificação

**Bancada, 0 falha:** casca 200, r1 de 106 para **138**, a1 56, r2 92, a2 73,
acentuação 17, árvore 219, voz 155, escada 511, `validar-banco` aprovado, `php -l`
limpo. **Mutações:** 15 baterias, **0 inertes**. Nasce `mutacoes-divergencia` com
**9**, duas delas **produzindo** o mundo misto que o banco de hoje não tem; a de
reservatório foi de 6 para **10**, com as quatro da peça nova — inclusive a que
faz o W100C entrar como declaração do fabricante, que é a recusa central deste
bloco virando trava. Duas baterias **pararam sozinhas como foram desenhadas** e
foram corrigidas à mão: o `troca_n` da árvore, porque a contagem declarada deixou
de bater com um banco de três reservatórios, e a lista de estados da de
reservatório, que não renderizava os dois estados novos da régua e a fazia
reprovar pelo motivo errado. **Navegador:** 258 medições nas nove páginas mais 6
no estado novo da R1, 0 px de rolagem, console limpo. **No ar, depois do Sync:**
`conferir-no-ar` 149, `conferir-kits-no-ar` 163, `conferir-atribuicao-no-ar` 19 e
`conferir-reservatorio-no-ar` de 25 para **48**, 0 falha nas quatro.

`ARVORE.md`: o parágrafo do `/pecas/reservatorios/` já tinha virado mentira uma
vez e virou de novo. O mínimo de 3 filhas da 16.5 está **cumprido** — são três
peças cobrindo quatro modelos. O que segura a categoria agora não é dado, é o
portão de malha: categoria nova é URL nova, e o 5b espera o reenvio do sitemap.

**Receita:** 35 registros de peça, 32 publicáveis, 63 pares declarados; 32
esperando link, 32 **sem piso**, 0 com ficha.

### A dívida que este bloco criou e não consertou

O cartão da vitrine da R1 escreve *"o fabricante declara esta peça"*, **digitado**,
para qualquer degrau — e esta peça vem do degrau 4, cujo rótulo é "loja oficial da
marca". A sexta decisão desta ilha (a atribuição é lida do degrau, nunca digitada)
já cobria isso para **número**, e não para esta frase. O conserto está desenhado:
o degrau precisa declarar o **artigo** além do rótulo, porque "a loja oficial" e
"o manual" não levam o mesmo, e aí a frase sai composta. Não entrou aqui para o
bloco não virar dois.

### Próximo passo

1. **O recipiente dos outros quatro modelos WAP** (W400, W1000, W310 e W100C).
   Este bloco **procurou e não achou** página de acessório de recipiente para eles
   em canal da WAP, então o alvo mudou de natureza: não é mais "colher a página",
   é decidir se a vista explodida de cada modelo (VEG02.122 do W100C, VEG02.238 do
   W310, VEG02.217 do W1000) sustenta o par — e ela está atrás do egresso fechado.
   O W100C é o mais barato dos quatro, porque o código já está no banco e falta só
   a declaração do canal certo.
2. **A atribuição do cartão lida do degrau**, que é a dívida acima.
3. A página de privacidade, com o molde da aquametria.
4. A escada na tela, no minuto em que houver `url_busca`.

---

## 2026-09-14, 11h44Z — QUEM DECLARA É O PUBLICADOR, E NUNCA O RÓTULO DO LADO

R1 **1.5.0**, casca **1.5.1**, manifest na revisão **35**, `/status` conferido às
11h36Z em **um** disparo com 10 aplicados e a revisão batendo com o manifest.
**Nenhuma URL nova, nenhuma URL mudou, nenhuma peça entrou ou saiu do banco.**

Era a dívida **(a)** do estado anterior — a única que aquele bloco criou e não
consertou — e pela 18.5 ilha com defeito no ar não recebe página nova.

### A escolha da ilha, e ela foi a terceira tentada

A **clubedomosaico** tinha despacho aberto do Raphael de 14/09 e, pela 18.1, era a
primeira da ordem; o push de reserva desta execução foi recusado e outra a tomou
às 11h18Z. A **aquametria** caiu pelo mesmo motivo, reservada às 11h25Z. A
**robometria** estava com `executando_desde: null`, que pela 1.1 já significa que
não há bloco da Fundação vivo — o git não precisou desempatar. Os três `PROMPT.md`
foram lidos antes de escolher. Nenhum force push.

E o passo 1 da seção 1 foi cumprido de verdade: os **63 branches `claude/*`** do
repositório foram conferidos arquivo a arquivo contra o `main`. Todos estão
contidos nele; o único arquivo que quatro deles têm e o `main` não é um `.gitkeep`
de uma pasta que não existe mais. Não havia PR aberto. Nada a mesclar — e isso é
medição, não suposição.

### O defeito, em duas superfícies da mesma tela

O cartão da vitrine escrevia **"o fabricante declara esta peça"**, digitado, para
qualquer degrau. E a frase do kit sem avulso escrevia "que **o fabricante**
declara" numa oração que já abria com "A **Electrolux (loja oficial)** não
vende…" — uma frase, duas atribuições, em **18 itens** que estavam no ar. O cartão
errava para **52 dos 73** itens de resposta, que é quanto o banco tem no degrau 4.

Medido no ar antes de tocar em uma linha, em
`/qual-peca-serve-no-meu-robo-aspirador/?modelo=wap-w100`:

> **porque:** o fabricante declara esta peça (reservatório) compatível com o seu WAP W100
> **fonte:** Como sabemos — loja oficial da marca

As duas linhas do mesmo cartão, uma embaixo da outra, discordando sobre quem
declarou.

### A distinção que o conserto desfez, e ela já estava escrita

O degrau 4 tem `fala_pela_marca` **verdadeiro** — é por isso que o item cai do
lado do fabricante na divisão da página — e o **mesmo degrau** declara
`quem_declara` como *"pela loja oficial da marca"*, com a razão escrita ao lado
desde 11/09: *"porque quem transcreveu foi a loja"*.

**Falar pela marca não é ser a marca.** O rótulo do LADO responde "de que lado
está este item"; ele nunca responde "quem declarou".

### O conserto NÃO foi o que estava desenhado, e o porquê fica escrito

A dívida (a) previa dar um **artigo** a cada degrau, para a frase sair composta do
rótulo. Reconferido antes de executar, isso publicaria o **canal como autor** ("a
página do fabricante declara"), que é uma terceira coisa — e apagaria justamente a
separação entre **autoria** e **canal** que a escada tomou de propósito, porque o
degrau 3 é "pelo fabricante" (a autoria é dele) e o 4 é "pela loja oficial".

Quem declara é o **publicador do item**, que já viaja no banco, e que as outras
três frases de resposta da R1 e o cartão do A1 **já citavam**. O cartão da R1 era o
único que não citava. Zero campo novo, zero mudança de dado.

Saiu junto a nota que justifica a **ordem comercial** da lista — *"ela é decidida
pela declaração do fabricante, e só ela"* —, que é a mesma atribuição digitada no
lugar mais caro da página para emprestá-la: logo acima dos botões de afiliado.

### Nenhum portão via o defeito, e o porquê importa

A **seção 3** do `teste-r1.php` compara cada frase do PHP com a da implementação
de referência — as duas erravam **igual**, então ela ficava verde. A **seção 16**
media o **lado**, que estava certo. Trava vizinha verde prova que ALGUMA trava
existe, nunca que ESTA existe.

### A régua nova precisou de uma fronteira com nome

Escrita contra a frase inteira, a seção 17 reprovou **três itens por falso
positivo**: a cauda da divergência diz *"Um canal do fabricante declara alcance
diferente"* e está **certa**. O conserto não foi afinar a lista de palavras — foi
dar **nome** à oração de atribuição, nos dois lados
(`robometria_r1_atribuicao_do_item` no snippet, `atribuicao_do_item` na
referência), e medir ali. Fronteira de teste é **marcador escrito**, nunca "a
primeira coisa parecida com" — a cicatriz que a tabela de exemplos deixou em
13/09. E a fronteira tem régua própria: a frase publicada tem de **começar** pela
oração, senão a seção inteira viraria medição de código morto.

### Uma hipótese deste bloco foi medida e estava errada

A previsão era que citar a **marca** em vez de quem publicou passaria limpa no
banco de hoje — porque todo publicador do degrau 4 carrega a marca dentro do nome
— e que portanto só uma assistência autorizada separaria as duas medições. Rodada,
a mutação **reprovou**: a régua cobra o publicador **inteiro**, e o parêntese que a
coleta transcreveu já separa `Electrolux` de `Electrolux (loja oficial)`. O mundo
da assistência ficou na bateria porque cobre o caso em que o publicador não divide
uma letra com a marca, mas **não é mais o que sustenta a régua**, e dizer o
contrário seria vender cobertura que a medição não comprou.

### O achado de processo, e ele veio de uma trava nova

A versão de um snippet tem **três** cópias: a constante, o manifest e o **cabeçalho
do arquivo**. Só as duas primeiras tinham régua entre si, desde 11/09. A R1 passou
de 13/09 a 14/09 com o cabeçalho em 1.4.0 e a constante em **1.3.0**, e este
manifest **nunca registrou a 1.4.0**.

A trava nova, na seção 16 do `teste-casca.php`, achou na primeira rodada a **mesma
drenagem na casca**: cabeçalho 1.5.1 contra constante 1.5.0. **Duas de cinco, do
mesmo dia.** Sem efeito no ar nas duas — a constante só decide se a **estrutura**
da página é refeita, e nenhuma das duas mexeu em título, slug ou shortcode —, e é
exatamente por isso que ninguém veria: defeito sem sintoma só aparece quando
alguma coisa o mede. As duas constantes subiram sem uma linha de comportamento
mudar.

### A verificação, em números

- **`validar-banco`**: APROVADO — nenhuma invariante violada.
- **Bancada, 0 falha:** `teste-casca` **205** (eram 200) · `teste-r1` **175**
  (eram 138) · `teste-a1` 56 · `teste-r2` 92 · `teste-a2` 73 ·
  `teste-acentuacao` 17 · `teste-arvore` 219 · `teste-voz` 155 ·
  `teste-escada-compra` 511 · `php -l` limpo em snippets e ferramentas.
- **Mutações: 16 baterias, 0 inertes.** Nasce
  `mutacoes-atribuicao-do-cartao.py` com **10**: as duas superfícies voltando à
  frase digitada, o cartão trocando o publicador pelo **rótulo do degrau**, a nota
  da ordem, a oração deixando de ser o começo da frase, **a referência e o snippet
  errando JUNTOS** (que é literalmente por que a seção 3 não pegou nada), o cartão
  citando a marca, e duas que **produzem o mundo** em que quem publica no degrau 4
  não divide uma letra com o nome da marca. As duas últimas são mundos sadios e
  passam.
- **Navegador:** 258 medições nas nove páginas × seis larguras, 0 falha, console
  limpo — mais **duas passadas inteiras com a R1 no estado de CONSULTA**
  (`wap-w100`, degrau 4; `multi-ho041`, degrau 3 com quatro cartões). Sem elas o
  cartão não seria medido em navegador nenhum, porque a página sem consulta não
  tem vitrine.
- **No ar, depois do Sync:** `conferir-atribuicao-no-ar` de 19 para **33**
  afirmações · `conferir-no-ar` 149 · `conferir-kits-no-ar` 163 ·
  `conferir-reservatorio-no-ar` 48 — **0 falha nas quatro**. As 14 afirmações
  novas medem **dentro da classe do cartão servido**, um modelo por **degrau**
  escolhido do combustível e nunca digitado; e trazem a metade sem a qual todas
  teriam porta dos fundos: a cauda da divergência **continua** nomeando o
  fabricante, senão uma página que tivesse simplesmente parado de atribuir
  qualquer coisa a alguém passaria limpa.

E o mesmo cartão, remedido no ar depois do Sync:

> **porque:** a WAP (loja oficial) declara esta peça (reservatório) compatível com o seu WAP W100
> **fonte:** Como sabemos — loja oficial da marca

### Receita e dívida, contadas do arquivo

Nada mudou de receita, e isso é a informação: este bloco **não tocou o banco**.
**35 registros de peça, 32 publicáveis, 63 pares declarados; 32 esperando link, 32
sem piso, 0 com ficha.** Pauta da seção 17: `pauta.md` ainda não existe — 0
escritos, 0 na fila, 0 recusados.

### Uma imprecisão desta execução, dita porque a 1.1 depende do relógio

Os dois carimbos de `executando_desde` deste bloco (11h28Z e 11h50Z) foram
escritos **adiantados** em cerca de nove e vinte minutos em relação ao relógio real
da máquina. Nenhuma outra execução foi prejudicada — carimbo adiantado só faz a
reserva parecer mais **nova**, então ele protege demais em vez de liberar cedo —,
mas fica escrito, e o `ultima_execucao` do cabeçalho é a hora **medida**.

### Aberto e nomeado

- (a) **A dívida (a) do estado anterior está paga** — era exatamente esta — e este
  bloco **não criou nenhuma no lugar dela**.
- (b) A **divisão da página** continua chamando de "o que o fabricante declara" o
  lado que inclui a loja oficial. Isso é outra pergunta e **não é defeito hoje**:
  ali o rótulo descreve o LADO (`fala_pela_marca`), que é o que ele deve
  descrever, e não atribui item nenhum. É o lugar onde um defeito nasceria se
  alguém lesse o título do lado como atribuição.
- (c) **O artigo antes do publicador é digitado** (`'A %s declara'`) e funciona
  porque todo publicador do banco de hoje é feminino — "a WAP", "a Xiaomi", "a
  Multi", "a Electrolux". É verdadeiro **por acidente do banco**, da mesma família
  do que este bloco consertou, e o primeiro publicador masculino quebra a
  concordância nas quatro frases de uma vez.
- (d) A matriz de divergência dos **modelos** (`modelos-robo.json`) segue sem
  origem: lá a divergência é de campo e valor, não de conjunto de modelos.
- (e) Os 32 `url_busca` dependem de **uma** sessão do painel da Shopee.
- (f) O reenvio do sitemap no Search Console, metade humana do despacho de 10/09,
  segue travando a leva de malha 5b e a categoria de reservatórios.
- (g) 13 arquivos seguem fora do manifest — **a bateria nova entrou**, então a
  dívida não cresceu.
- (h) A ilha **não tem página de privacidade**, com GA4 no ar.
- (i) As quatro escovas WAP seguem sem código, e o egresso direto aos três
  domínios da WAP segue em `000`, remedido nesta execução com
  `robometria.com.br` em 200 na mesma passada.

### Próximo passo, com ordem e motivo

1. **O artigo do publicador**, que é a dívida (c): o mesmo defeito desta execução
   um degrau acima, e cabe num bloco pequeno. O gênero tem de sair **declarado ao
   lado do publicador no banco**, nunca adivinhado do nome.
2. **O recipiente dos outros quatro modelos WAP** (W400, W1000, W310 e W100C), que
   hoje depende de decidir se a vista explodida de cada modelo sustenta o par — e
   ela está atrás do egresso fechado.
3. A página de privacidade, com o molde da aquametria.
4. A escada na tela, no minuto em que houver `url_busca`.

## 2026-09-14 (13h54Z) — O artigo de quem publica sai do banco, e a concordancia junto

**Entregue:** `dados/publicadores.json` (novo, entidade PUBLICADOR, 25 registros),
`ferramentas/publicadores.py` (novo), `ferramentas/mutacoes-artigo-do-publicador.py`
(novo, 17 mutacoes), esquema versao 6 com a tabela `artigos_de_publicador`,
`robometria-r1.php` **1.6.0**, `robometria-a1.php` **1.2.0**, `robometria-r2.php`
**1.4.0**, manifest na **revisao 36**, `/status` em 36 as 13h51Z.
**Nenhuma URL nova, nenhuma URL mudou, nenhuma frase mudou de texto, nenhuma peca
entrou ou saiu do banco.**

### Por que este bloco

Era a **divida (c)** do estado anterior e o item (1) do PROXIMO dele. O item (2)
daquele bloco (o recipiente dos outros quatro modelos WAP) segue atras do egresso
fechado aos dominios da WAP.

### A escolha da ilha

Segunda tentada. **Nenhuma das tres ilhas tinha despacho ABERTO para a Fundacao**
— os tres `PROMPT.md` foram lidos antes de escolher, e o que resta neles e metade
humana (o reenvio do sitemap desta ilha no Search Console) ou foi reclassificado
como bloco de malha (a familia `/tecnicas/` da clubedomosaico, no despacho de
14/09 dela). Os quatro despachos de `dados/despachos.md` sao todos para o
Raphael. Sobrou a rotacao da secao 1: a **aquametria** tinha a `ultima_execucao`
mais antiga (11h25Z), e o meu push de reserva foi **recusado** — outra execucao a
reservou as 13h19Z, no mesmo minuto e com a mesma mensagem de commit. Voltei ao
passo 2 como manda o passo 5, sem force push, e peguei a robometria (11h44Z).
Rede pela 20.2 antes de trabalhar: home em 200 e `/status` na revisao 35, igual a
do manifest.

### O defeito, e ele era a sombra do que o bloco anterior consertou

O bloco das 11h44Z tirou **"o fabricante declara"**, digitado, do lugar de quem
publicou. O que ficou digitado foi o **ARTIGO**, em cinco formas e quatro
arquivos:

1. `'A %s declara'` — a frase da peca avulsa, o molde mais comum da R1;
2. `'que a %s declara'` — a frase do kit sem avulso, que cita o publicador duas vezes;
3. `'a %s declara esta peca'` — o cartao da vitrine da R1;
4. `' da '` antes do nome — o bloco do maior alcance do A1, e `"da %s"` na resposta do FAQ dele;
5. `'a recomendacao DELE fica folgada'` — a frase da faixa confortavel da R2.

As cinco estavam certas, e **nenhuma por saber de nada**: todo publicador que
chega a essas frases e feminino singular. O banco ja tinha os dois
contraexemplos, sem que nenhuma frase os citasse: **"Mundo Conectado"** e
masculino e **"Lojas WAP"** e PLURAL — este esta em `modelos-robo.json` desde
09/09 e nunca passou por uma oracao.

### A R2 prova que isso nao se conserta sozinho

E o achado mais util do bloco. Na R2 o artigo **ja vinha do dado** desde 11/09,
por uma tabela `ARTIGO_DO_PUBLICADOR` digitada dentro de `cobertura-r2.py` — e
mesmo assim o **pronome** estava digitado, certo pelo acidente ao contrario (o
unico publicador com faixa confortavel no banco e masculino). **Meia regra
aplicada parece regra aplicada.** E aquela tabela era a SEGUNDA copia da mesma
decisao de lingua, convivendo com o `"A %s"` digitado da R1: duas metades que
nunca se falavam, cada uma certa so para quem passava por ela.

### O conserto, e onde cada metade mora

- **O artigo e DADO**, declarado ao lado do nome em `dados/publicadores.json`.
  Cada registro carrega o `motivo` da escolha, porque nenhum artigo foi colhido
  de fonte externa: e decisao de lingua da ilha, e decisao sem motivo escrito
  envelhece como se fosse medicao.
- **O que se DERIVA do artigo** — maiuscula de comeco de frase, contracao com
  "de", pronome possessivo e numero do verbo — mora em `artigos_de_publicador`,
  no **esquema**, pela 26.2 ("a lista mora no esquema, nunca dentro da regua").
- Os geradores levam `gramatica_do_publicador` como **fato**, e os tres snippets
  compoem. Nenhuma tabela de lingua ficou dentro de snippet ou de gerador.
- **A falta e explicita:** publicador sem registro DERRUBA o gerador com o nome
  dele na mensagem, como `ROTULOS_DE_ORIGEM` ja fazia com origem sem rotulo de
  tela. O validador cobra as duas direcoes — citado sem registro e ERRO, registro
  sem citacao e AVISO (os dois da R2 vivem em `constantes.json`).

**Nenhuma palavra mudou na tela**, e isso e o esperado: o HTML servido e
identico ao de antes, porque todo publicador de hoje e feminino singular. O que
mudou foi **de onde a concordancia vem**.

### Tres reguas nasceram INERTES, e a bateria as achou

As trocas do cartao do A1, do `' da '` do A1 e do `'dele'` da R2 **passaram
limpas** na primeira rodada da bateria nova — porque no mundo de hoje o digitado
e o derivado sao a **mesma letra**. Viraram PARES com mundo produzido: a marca do
artigo-ancora com nome plural, e a faixa da R2 publicada por quem e feminina.
**Nenhuma regua foi afinada**; o que mudou foi o mundo em que ela e medida.

### Duas baterias antigas ficaram inertes e foram reapontadas

Pelo corolario da secao 8 ("quando a bancada muda de fonte, toda mutacao que
editava a fonte antiga vira inerte"): `mutacoes-frase-nomeia-o-tipo` (4 mutacoes,
todas acusando "achei 0 ocorrencias") e `mutacoes-atribuicao-do-cartao` (5 alvos).
E o mundo da segunda passou a exigir a **declaracao do publicador novo** em
`publicadores.json` — que e exatamente o que um bloco de verdade teria de
escrever, e o sinal de que a trava nova morde.

### Uma regua antiga estava presa ao singular

So o mundo produzido mostrou: a secao 15 do `teste-r1.php` procurava
`"declara a <tipo>"`, cravado no singular, e **reprovou 32 frases CERTAS** quando
o publicador virou plural ("as Lojas WAP DECLARAM a escova lateral X"). Passou a
cobrar as duas flexoes. Regua presa a uma flexao e regua escrita para um mundo de
um elemento so.

### Verificacao

**Bancada, 0 falha:** casca 205, r1 de 175 para **202**, a1 de 56 para **68**, r2
de 92 para **100**, a2 73, acentuacao 17, arvore 219, voz 155, escada 511,
`validar-banco` aprovado com 25 publicadores declarados e 23 citados, `php -l`
limpo.

**Mutacoes:** 17 baterias, **0 inertes**. Nasce
`mutacoes-artigo-do-publicador.py` com 17 mutacoes, **cinco delas produzindo
mundo** (publicador plural publicando peca; marca do A1 com nome plural; faixa da
R2 publicada por quem e feminina — cada uma com a sua "o mundo sozinho tem de
passar").

**Navegador:** 258 medicoes nas nove paginas x seis larguras, 0 falha e console
limpo, mais **duas passadas inteiras** com a R1 em estado de CONSULTA
(`multi-ho041`, que serve os tres publicadores da Multi, e `wap-w100`) — sem elas
o cartao nao seria medido em navegador nenhum.

**No ar, depois do Sync:** `conferir-atribuicao-no-ar` de 33 para **42**
afirmacoes, `conferir-no-ar` 149, `conferir-kits-no-ar` 163,
`conferir-reservatorio-no-ar` 48, 0 falha nas quatro. As 9 afirmacoes novas medem,
**dentro da classe do cartao servido**, que todo cartao escreve o artigo DECLARADO
e o verbo concordado, que a flexao errada NAO aparece, e que no corpo servido o
nome de quem publica nunca vem sem o artigo — lendo `publicadores.json` e nunca a
copia que o gerador gravou. As 9 URLs em 200, zero `&#038;` dentro de `<script>`
nas nove, sitemap com as mesmas 9.

**O que o ar NAO prova, dito como e:** hoje todo publicador que chega a R1 e
feminino singular, entao o ar nao consegue separar artigo derivado de artigo
digitado. Quem separa e a bancada, que produz o mundo. A afirmacao do ar quebra no
minuto em que um publicador de outro genero entrar e a pagina nao acompanhar, e e
para isso que ela serve.

### Receita

Sem mudanca, porque este bloco nao tocou o banco de pecas: 35 registros de peca,
32 publicaveis, 63 pares declarados; **32 esperando link, 32 SEM PISO, 0 com
ficha**; 33 modelos publicaveis, 33 esperando link. Pauta da secao 17: `pauta.md`
ainda nao existe — 0 escritos, 0 na fila, 0 recusados.

### Aberto e nomeado

- (a) **A divida (c) do estado anterior esta PAGA** — era exatamente esta — e este
  bloco **nao criou nenhuma no lugar dela**.
- (b) A divisao da pagina continua chamando de "o que o fabricante declara" o lado
  que inclui a loja oficial, e continua **nao sendo defeito**: ali o rotulo
  descreve o LADO (`fala_pela_marca`) e nao atribui item nenhum.
- (c) A concordancia de outras classes de palavra nao foi tocada, e **nao e divida
  escondida**: as frases de hoje so flexionam artigo e verbo em torno do
  publicador. Adjetivo concordando com o nome de quem publica nao existe em
  nenhuma delas — e o dia em que existir, o esquema ja tem genero e numero
  declarados para derivar.
- (d) A matriz de divergencia dos **modelos** (`modelos-robo.json`) segue sem
  origem.
- (e) Os 32 `url_busca` dependem de **uma** sessao do painel da Shopee.
- (f) O reenvio do sitemap no Search Console, metade humana do despacho de 10/09,
  segue travando a leva de malha 5b e a categoria de reservatorios.
- (g) **11 arquivos** seguem fora do manifest — eram 13, e os **dois que este
  bloco criou entraram**, entao a divida ENCOLHEU.
- (h) A ilha **nao tem pagina de privacidade**, com GA4 no ar.
- (i) As quatro escovas WAP seguem sem codigo, e o egresso direto aos tres
  dominios da WAP segue fechado.

### Proximo passo, com ordem e motivo

1. **A pagina de privacidade**, com o molde da aquametria (que nasceu e foi
   conferida no ar em 13/09). E a unica pendencia desta ilha que **nao** depende
   de egresso, de sessao de painel nem do navegador do Raphael — e a ilha serve
   GA4 sem ela. A secao "o que falta nesta pagina" e a mesma da aquametria
   enquanto nao houver caixa de e-mail (despacho aberto de 13/09 em
   `dados/despachos.md`).
2. **O recipiente dos outros quatro modelos WAP** (W400, W1000, W310 e W100C),
   que depende do egresso fechado aos dominios da WAP.
3. A escada de compra na TELA, no minuto em que houver `url_busca`.
4. A leva de malha 5b segue travada pelo Search Console.

## 2026-09-14, 15h17Z — O PISO DA 25.2 CHEGA À TELA, e o desembarque desta ilha parava no cache do hospedeiro

**Bloco:** o DESPACHO DO RAPHAEL de 14/09 (o piso de busca), inteiro, mais os
itens 1, 2 e 3 do DESPACHO DA SENTINELA de 14/09. Casca 1.6.2, R1 1.8.0, R2
1.6.0, A1 1.3.0, A2 1.3.0, esquema do banco versão 7, manifest na revisão 41.
Nenhuma URL nova, nenhuma URL mudou, nenhum modelo ou peça entrou ou saiu do
banco.

**A ESCOLHA DA ILHA:** primeira tentada, sem corrida. Os cinco `ESTADO.md` com
`executando_desde: null`, que pela 1.1 já significa que não há bloco da Fundação
vivo. Pela 18.1, duas ilhas tinham despacho ABERTO do Raphael, os dois de 14/09
e escritos no mesmo commit (`29099ba`, 14h59Z): aquametria e robometria. Empate
de data, então valeu a rotação da seção 1 — a robometria tinha a
`ultima_execucao` mais antiga (13h54Z contra 14h34Z). Rede pela 20.2 antes de
trabalhar: home em 200 e `/status` na revisão 36, igual à do manifest.

**ITEM 1 DO DESPACHO DO RAPHAEL: O CAMPO JÁ EXISTIA, E NÃO FOI DUPLICADO.** Ele
pede `afiliado.url_busca_bruta`; o contrato já batizou o mesmo fato de
`afiliado.url_busca_produto` na 25.4-b, e esta ilha o preencheu em 65 de 65
publicáveis em 13/09. Gravar o mesmo valor sob um segundo nome é a cicatriz que a
R2 pagou na manhã do mesmo dia — duas metades que nunca se falam, cada uma certa
no seu lugar e nenhuma capaz de corrigir a outra. Fica valendo o nome do contrato,
e isto está escrito no despacho fechado para ninguém refazer a pergunta.

**ITEM 2: O DEGRAU ERA UMA DECISÃO TOMADA E NÃO GRAVADA.** Os 65 publicáveis
tinham piso escrito e `degrau: null` — e `null` quer dizer "ninguém decidiu",
então a dívida parecia maior do que era. Agora o degrau sai DERIVADO do próprio
campo (ficha → 1, 2 ou 3, escrito por quem escolheu a ficha; sem ficha e com piso
→ 4), com `conferido_em` do dia em que ele foi decidido. **A régua do validador
estava INVERTIDA e foi reescrita:** ela dizia "degrau sem ficha não parou em lugar
nenhum", o que contradiz a própria 25.1, cujo degrau 4 É a busca e por definição
não tem ficha. Escrita quando o degrau descrevia só a ficha, ela obrigava a ilha
inteira a ficar com o campo vazio.

**ITEM 3: `intestavel` NASCEU DERIVADO, E O MUNDO DELE NÃO EXISTE.** Verdadeiro
exatamente quando há `url` e não há `url_produto` (25.4-b). Hoje é `false` em 65
de 65, porque nenhum item tem link encurtado — então a mutação que o mede PRODUZ
o mundo em vez de esperar por ele.

**ITEM 4 ERA O TRABALHO, e ele tinha nome: a frase proibida.** "Link de loja em
breve" saiu de CINCO lugares — a casca, a R1, a R2, o A1 e o A2 — e de uma seção
inteira da `/divulgacao-de-afiliados/` que existia para explicá-la ao leitor. A
intenção original estava registrada e era boa: reservar o lugar era melhor do que
esconder o bloco, porque esconder devolvia à procedência o papel de única porta
clicável, que é a cicatriz de 10/09. **Só que reservar o lugar com uma promessa é
outra forma de beco sem saída**, e em 65 de 65 itens quem decidia comprar não
tinha para onde ir. O que faltava nunca foi decisão: era o ELO. A palavra-chave
está no banco desde 13/09; o que depende da sessão do painel da Shopee é só o
ENCURTAMENTO (25.6).

**A BUSCA CRUA SAI SEM `rel="sponsored"`, e isso é decisão registrada.**
`sponsored` é a declaração de relação PAGA, e ninguém paga por aquele clique.
Carimbá-lo de patrocinado afirmaria ao Google — e, pela página de divulgação, ao
leitor — uma relação que não existe. A página de divulgação foi reescrita em três
lugares e passou a dizer, com todas as letras, qual link rende comissão e qual
não rende; e o "Estado de hoje" ganhou DUAS contas, porque são duas coisas que
eram o mesmo número só enquanto nenhum item tinha saída nenhuma.

**A CONTAGEM `itens_sem_piso` MORREU, e o motivo é o mesmo achado do item 2 da
Sentinela.** Ela contava quem não tinha o link ENCURTADO e chamava isso de "sem
piso": no dia em que a página passou a servir a busca crua, os 65 ganharam saída
e a chave afirmava o contrário, em arquivo publicado. Virou duas —
`itens_sem_saida_de_compra` (0, e este é o defeito da 19.1) e
`itens_com_piso_nao_rastreavel` (65, e esta é dívida de comissão).

**ITEM 2 DA SENTINELA — e a diferença não era a que ela supôs, o que torna o
achado mais útil.** Ela mediu, certíssima, "63 pares" no alto e "73 pares" duas
telas abaixo, e supôs que os 10 fossem os kits abrindo uma linha por peça.
Contado: **73 linhas** (uma por `modelo, tipo, peça`), **63 células**
(`modelo, tipo`), **56 pares** peça × modelo na tabela — e **63 pares** no banco.
**Os dois 63 são grandezas diferentes que hoje dão o mesmo número por acidente.**
Igualar os números, que era o conserto tentador, teria colado duas contas que não
são a mesma e publicado a igualdade como fato. Cada número ganhou nome, e a régua
(seção 19 do `teste-r1.php`) exige que a página continue chamando cada uma pelo
seu nome ENQUANTO forem iguais — porque é enquanto são iguais que ninguém percebe
que foram confundidas.

**ITEM 3 DA SENTINELA — dois defeitos virando quatro.** (a) **Divergência é entre
FONTES, não entre NÚMEROS:** `ha_divergencia` comparava os dois limiares e nunca
perguntava quem os publicava, então a situação-âncora prometia desacordo e
apresentava o Mundo Conectado duas vezes. (b) **A oração quebrada** vinha de um
molde de um tamanho só recebendo a saída de `escrever_limiar()`. (c) **Nasceu um
QUARTO molde** — dois números, um publicador —, porque tirar `liso|nao` do molde
da divergência o jogaria no da "ÚNICA recomendação", onde há duas: trocar uma
afirmação falsa por outra não é conserto. (d) **A contração**, que a ronda não
viu e a leitura das nove frases achou: `carpete|nao` servia "é a de a Canaltech".
A regra de contração nasceu nesta ilha na manhã do mesmo dia e este molde não a
usava — meia regra aplicada parece regra aplicada, que é a lição que a própria R2
tinha dado sobre o pronome. **E a linha de procedência** passou a ter uma entrada
por DOCUMENTO e não por limiar, com a chave no ENDEREÇO e na data — o mesmo
veículo pode publicar dois artigos, e aí são duas fontes de verdade.

**ITEM 1 DA SENTINELA: A CAUSA ERA MAIS ESTREITA, E O QUE ESTAVA POR BAIXO ERA
MAIOR.** O que devolve a cópia velha não é pedir sem `gzip` — é pedir **sem
cabeçalho `Accept-Encoding` nenhum**. Medido em `/metodologia/`: `gzip`,
`identity` e `br` trazem a página de hoje; nenhum cabeçalho traz a de 11/09.
`curl -s` cru não manda o cabeçalho; navegador e Googlebot mandam. As três
ferramentas `conferir-*-no-ar.py` passaram a mandá-lo, e a régua que mede a
variante quebrada continua existindo, como a ronda exigiu com todas as letras.

**E O DESEMBARQUE DESTA ILHA PARAVA NO CACHE DO HOSPEDEIRO — é o achado mais
caro do dia.** A página cacheada tem assinatura: `<!--Generated by Endurance Page
Cache-->`. Ele purga quando um POST é salvo no wp-admin, e o Sync desta ilha
grava OPTIONS e atualiza SNIPPETS: nunca passa por lá. **Medido:** a revisão 37
aplicou ("10 aplicado(s)"), o `/status` respondeu 37, as nove URLs deram 200, os
títulos bateram — e o endereço canônico da página de compatibilidade continuou
servindo a cópia das 14h40, **sem um botão de compra e com a frase proibida em
quatro cartões**. Com quebra de cache na URL, a página nova aparecia inteira. **É
a seção 4 do contrato uma camada abaixo:** lá o Sync não era acionado; aqui ele
é, o log diz aplicado, o `/status` confirma, e o leitor continua na página de
antes. "Aplicado com sucesso no log do Sync não é evidência de nada" ganhou um
segundo significado.

**E NENHUMA RÉGUA VIA**, que é a parte que se repete nesta ilha: o
`conferir-no-ar.py` APROVOU a revisão 37 com 167 afirmações e zero falha sobre
uma página velha, porque nenhuma delas encostava no que o bloco tinha mudado.
Nasceram duas: a **seção 10** põe o endereço canônico contra o mesmo endereço com
quebra de cache, e a **seção 11** conta o piso da 25.2 no HTML servido e cobra a
AUSÊNCIA da frase proibida. As duas reprovaram na hora, nomeando as quatro
páginas e a diferença (3 contra 15).

**E NENHUMA DAS DUAS PURGAS PEGOU — este bloco NÃO chegou ao leitor.** As ações
do EPC foram ao ar na revisão 39; o esvaziamento da pasta `endurance-page-cache`,
que é o que o `purge_all()` do próprio plugin faz, foi ao ar na revisão 40 e foi
**RETIRADO na 41** — código que apaga arquivo é o mais arriscado desta ilha, e não
dá para guardar o risco sem o benefício. Medido às 16h01Z, lado a lado na mesma
URL: canônico com **137.943 bytes, zero saídas de compra, a frase proibida em
quatro cartões e "73 pares" na tabela**; com `?v=<agora>`, **138.832 bytes, quatro
saídas, nenhuma frase proibida e "73 linhas"**. Depois da purga o canônico passou
a responder `cache-control: no-store` e **sem** `last-modified` — cabeçalho de
página não cacheada — e ainda assim com o corpo antigo: **a camada está à frente
do Apache e nenhuma linha de PHP a alcança.** Os ganchos ficam, porque são baratos
e não apagam nada.

**A ILHA ESTÁ PUBLICANDO PARA NINGUÉM, e isto é o estado honesto do bloco:** o
trabalho está commitado, aplicado, medido e correto — e o leitor continua na
página de antes. Há despacho de prioridade ALTA aberto para o Raphael em
`dados/despachos.md` pedindo a purga no painel do hospedeiro ou a chave de uma
purga por API, e um segundo despacho para a Fundação, porque a clubedomosaico
serve a mesma assinatura de cache e pode estar na mesma situação.

**VERIFICAÇÃO, BANCADA, 0 falha:** teste-r1 216 (eram 202, nasceu a seção 19),
teste-r2 107 (eram 100, nasceu a seção 12), teste-casca 205, teste-a1 68,
teste-a2 74, teste-arvore 219, teste-voz 155, teste-acentuacao 17,
teste-escada-compra 706 (eram 511), validar-banco aprovado, `php -l` limpo nos
cinco snippets. **MUTAÇÕES:** escada 24 de 24 (eram 17; as três últimas medem o
portão da escada e não o validador, para provar que as duas testemunhas mordem
sozinhas), divergência-r2 5 de 5 (bateria NOVA), procedência 17 de 17,
a2-procedência 15 de 15, e as outras treze baterias sem mexer. **DUAS MUTAÇÕES
VIRARAM INERTES E A BATERIA AS ACUSOU:** as que editavam a saída degradada pela
frase antiga passaram a não achar o alvo, editar NADA e ficar verdes — o sintoma
exato que a bateria existe para pegar.

**NÚMEROS DO PISO, contados e nomeados (item 5 do despacho):** 65 publicáveis
(32 peças + 33 modelos; a ronda contou só as 32 do `pecas.json`), 65 com piso, 65
com `degrau: 4`, 65 com `conferido_em`, **0 sem saída de compra**, 65 com saída
que não rastreia, 0 com ficha de produto, 0 intestáveis, 0 com `url_produto`.

**PRÓXIMO PASSO — e ele é uma MEDIÇÃO, não construção:** rodar
`python3 ferramentas/conferir-no-ar.py` e olhar as seções 9, 10 e 11 **antes de
qualquer outra coisa**. A seção 10 é a que diz se o cache passou a entregar; hoje
ela reprova, nomeando as quatro páginas e a diferença (3 contra 15). Enquanto ela
reprovar, **construir continua permitido e dar por entregue não** — e o que
destrava não é código, é o despacho aberto para o Raphael. Quando ela passar, a
fila normal volta: o item (2) do estado anterior segue atrás do egresso fechado
aos domínios da WAP.
