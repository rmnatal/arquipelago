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
