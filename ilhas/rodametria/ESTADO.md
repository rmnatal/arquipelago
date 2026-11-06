---
ilha: rodametria
estado: viva              # `nascendo` -> `viva` em 29/10/2026 as 12h1xZ: a ilha SERVE PAGINA. Duas URLs no wp-sitemap.xml, as duas em 200, com a casca e a F2 desembarcadas na revisao 9 e os dois portoes de ar APROVADOS. Antes deste dia a ilha tinha banco e nenhum byte que um visitante visse.
prioridade: 1
piso: abaixo              # 10 URLs publicadas contra as 40 da 21.1, e primeira_indexacao null. O NUMERO DESTE COMENTARIO ESTAVA VENCIDO: dizia 5, de 30/10, e a ilha passou por 9 e chegou a 10 em 06/11 — numero velho lido como fato e o defeito que a secao 4 nomeia. O VALOR do campo nao mudou e nao e meu de mudar. Quem decide este campo e a leitura semanal (21.6), nunca a Fundacao de cabeca. O teto da 21.4 tem folga: esta semana saiu UMA leva, de 3 URLs, contra o teto de 3 levas por semana.
urls_publicadas: 10       # SEM MUDANCA nesta passada: nenhuma URL nasceu. O bloco foi DESPACHO, nao construcao, e pela 18.2 correcao nao consome a vez de um bloco. Contado no wp-sitemap.xml no ar com quebra de cache, sub-sitemap por sub-sitemap. Piso da 21.1 pede 40 — faltam 30. Teto da 21.4: a LEVA 1 de 3 desta semana foi gasta em 06/11 pela F3, e esta passada nao gastou leva nenhuma.
ultima_ronda: 2026-11-06T15:01Z   # RONDA DIARIA TECNICA de 2026-11-06, 14h4xZ-15h0xZ, medida na revisao 60. Cinco defeitos, ZERO consertos (nenhum e da lista 19.1): despacho no PROMPT.md. A porta de entrada que caiu em 05/11 esta REPARADA — 10 de 10 URLs em 200 em duas leituras com quebra de cache, as tres portas da 29.2 verdes e o sitemap servindo XML de verdade.
primeira_indexacao: null  # as duas primeiras URLs foram ao ar hoje; indexacao e trabalho de dias. Quem grava este campo e a leitura semanal, lendo o Search Console.
ultima_execucao: 2026-11-06T16:51Z   # OS CINCO ITENS DO DESPACHO DA RONDA DE 06/11 FECHADOS E CONFERIDOS NO AR (18.4), na revisao 62, com as 11 linhas de item do log dizendo `ok` (20.4, lidas do fecho para baixo pela 20.8). O conserto que vale mais que os cinco: o estado do cartao da home passou a ser DERIVADO da existencia da pagina, e nasceu a regua das duas afirmacoes que esta ilha nao pode fazer — UMA regra, usada no repositorio e no HTML servido das 10 URLs. Ela REPROVOU a revisao 60 antes de qualquer conserto. A HORA SAIU DO `date -u` NA MESMA LINHA DE COMANDO QUE A GRAVA, nunca digitada.
executando_desde: 2026-11-06T19:17Z   # RESERVA da execucao de 2026-11-06T19:17Z (passo 5 da secao 1 / 1.2: `foco.md` nomeia a rodametria). A hora saiu do `date -u` na MESMA linha de comando que a grava, nunca digitada. A ilha estava livre: `executando_desde: null` (que pela 1.1 ja significa que nao ha bloco da Fundacao vivo) e ultimo commit em ilhas/rodametria as 16h54Z, muito acima dos 40 minutos.
rede: aberta em 2026-11-06   # 20.2, MEDIDA e nao herdada ANTES da reserva: rodametria.com.br em 200 nas TRES passadas, com aquametria.com.br e robometria.com.br em 200 nas MESMAS tres — 12 de 12 verdes (o `www` em 301, que e o redirecionamento normal). A PAREDE DO `.gov.br` SEGUE DE PE e NAO foi remedida de proposito (medida em 05/11 as 19h1xZ). E A FICHA DA SHOPEE FOI MEDIDA E FECHADA COMO FONTE DE NIVEL 5 em 06/11: 200 nas tres passadas e casca de SPA VAZIA, 155.908 bytes com ZERO ocorrencia de `Potencia`, `500W`, `km/h`, `Velocidade`, `Marca`, `Peso` ou do nome do produto, e nem `<title>`.
bloqueada_por: null      # obrigatorio pela secao 2. `null` DE PROPOSITO: o que falta (gov.br para a F1, as prefeituras para a camada municipal, as tres etiquetas do Mercado Livre) trava a FABRICA e nao a ILHA, e isso se escreve no despacho, que e o canal da 12.2. Preenche-lo congelaria tambem os blocos que ja podem andar.
bloco_atual: |
  O DESPACHO DE CINCO ITENS DA RONDA DE 06/11 ESTA FECHADO E CONFERIDO NO AR
  (18.4), na revisao 62. E o que ele deixou nao foi cinco frases trocadas: foi
  UMA REGUA e UM MECANISMO.

  ESTE ARQUIVO CONTINUA SENDO A MEMORIA DESTA ILHA — `/areas/projeto-rodametria.md`
  nao existe nesta nuvem, e e por isso que este campo e longo.

  PRIMEIRO COMANDO DE QUEM PEGAR ESTA ILHA: `python3 ferramentas/bancada.py --no-ar`.
  A bancada tem 35 portoes sem rede e 39 com rede — um a mais de cada, com o
  `teste-afirmacao-de-tela.py` que nasceu nesta passada.

  A REGUA NOVA, E ELA E O ATIVO DESTA PASSADA: `ferramentas/teste-afirmacao-de-tela.py`
  e dona de DUAS regras e as aplica ao REPOSITORIO; `conferir-no-ar.py` as
  IMPORTA e as aplica ao HTML servido das 10 URLs do sitemap e aos blocos
  `application/ld+json`. As duas regras sao:
  (A) HABILITACAO — toda frase que fala de CNH ou habilitacao tem de estar numa
      das ORACOES PERMITIDAS da ilha (a lista esta no proprio portao), ou ser
      pergunta, ou ser citacao de titulo de anuncio entre aspas. Redacao NOVA
      reprova, e e de proposito: falso positivo custa uma linha de texto, falso
      negativo manda alguem para a rua sem habilitacao.
  (B) O PESO NA AUTONOMIA — `seu peso` (ou `seus N kg`, ou `desconto de peso`,
      ou `peso de quem pilota`) ao lado de `autonomia`, `km` ou `watt-hora` so
      passa no elemento que NEGA que o peso entre na conta.
  E HA UM PAR separado, porque nenhuma busca por palavra o pegaria: pergunta de
  `FAQPage` que fala de habilitacao exige oracao de recusa NA RESPOSTA. Foi
  assim que o "precisa de CNH?" respondido com "nao" apareceu.

  ELA REPROVOU A REVISAO 60 ANTES DE QUALQUER CONSERTO, como o item 3 do
  despacho manda: 6 afirmacoes de habilitacao, 9 promessas de peso e 2 pares de
  FAQ, em 5 das 10 URLs, com ZERO falso positivo nas outras cinco. 41 mundos de
  autoteste, tres deles exigindo que a regua VELHA e a nova DISCORDEM.

  O MECANISMO, E ELE VALE PARA A QUARTA FERRAMENTA QUE NASCER: o estado do
  cartao de ferramenta da home saiu da PROSA e passou a ser DERIVADO de
  `rodametria_casca_url_do_slug()`. Pagina existe -> o cartao e LINK; nao existe
  -> prosa de espera com a causa. A home dizia que a F3 "ainda nao esta no ar"
  com a F3 no ar, e o cartao dela nao tinha `<a>` — ZERO link de miolo para a
  pagina. Agora sao QUATRO (home, as duas familias e a F2). A caixa de fora da
  primeira tela, que dizia "1 de 3 ferramentas" com os dois numeros digitados,
  tambem conta as paginas que existem.

  AS DUAS ESCOLHAS DE 19.2 QUE O DESPACHO DEIXOU PARA A FUNDACAO, e as duas
  razoes:
  - ITEM 2: as promessas CAIRAM, a formula nao mudou. Fazer a F2 usar o peso
    exigiria a constante de consumo por quilo, que esta `pendente` e pela secao
    10 nao entra em formula. Nao ha fonte, entao nao ha conta.
  - ITEM 5: o `nota` de veiculos.json passou a ser RECONTADO pelo
    `derivar-banco.py` e conferido pelo `validar-banco.py`, em vez de apagado.
    Apagar conserta hoje; recontar impede o proximo numero digitado de entrar
    amanha. Tres quebras novas na bateria de mutacao provam que o portao morde.

  O DESPACHO ERROU UM NUMERO NO MESMO DEFEITO QUE RELATAVA: disse que CINCO
  registros tem saida de compra e nomeou QUATRO. Sao QUATRO — honeywhale-m2-max
  (degrau 1), sousa-bike-aro-24, x13-chopper-1000w e ls-sport-scooter-1000w
  (degrau 4).

  TRES DEFEITOS FORA DO DESPACHO, consertados na mesma passada:
  - `/sobre/` estava VENCIDA em tres afirmacoes: dizia que a pergunta do peso
    "nao esta no ar", que "a conta que esta no ar e a da autonomia" (sao tres) e
    justificava a ausencia da F1 com uma parede que caiu em 05/11. Na secao que
    a ilha batizou de "o que ainda nao da para responder aqui, dito aqui e nao
    escondido".
  - duas paginas condicionavam a recusa a "enquanto a gente nao ler a Resolucao
    996/2023", que JA foi lida. O que falta e o CTB.
  - `derivar-banco.py` reescrevia `pecas.json` em TODA passada, trocando 186
    linhas de indentacao com zero byte de conteudo diferente.

  O QUE FOI MEDIDO NO AR: `conferir-no-ar.py` 577 afirmacoes e 0 falha; bancada
  com rede 39 portoes e 0 falha; 32.5 em 10 de 10 paginas do molde, pior caixa
  405 px (teto 700) e pior compra 1.279 px (teto 1.400) — o cartao da home virou
  BOTAO sem custar pixel de dobra. Casca 1.17.0, F2 1.6.1, F3 1.4.1, produto
  1.8.0.

  O PROXIMO PASSO DESBLOQUEADO, e nenhum deles depende de ninguem:
  1. O BLOCO DE CONTEUDO DA MALHA. As tres ferramentas estao no ar e o piso da
     21.1 pede 40 URLs contra as 10 de hoje — faltam 30. A fila natural e a
     secao 30 (paginas pelo nome do produto) sobre as consultas de
     `dados/consultas-de-produto.json`, respeitando o teto de 3 levas por
     semana da 21.4 (a leva 1 desta semana foi gasta em 06/11 pela F3).
  2. A VITRINE DA F3 ESTA VAZIA com a causa nomeada: os TRES registros que
     declaram `carga_max_kg` declaram 120 kg e NENHUM tem oferta aberta.
     Coleta de ficha que declare carga maxima destrava a vitrine da F3 sem
     mexer em uma linha de codigo.
  3. A SUPERFICIE DE REPOSITORIO DA REGUA NOVA le o PHP por INSTRUCAO, e juntar
     por instrucao gruda vizinhos que a pagina serve separados. Lá ela e aviso
     barato; a medicao de verdade e a do ar. Quem quiser fecha essa folga.
  4. A `VOZ.md` desta ilha ainda traz, nos exemplos aprovados de 27/10, a frase
     "dispensa CNH e placa". O `dados/constantes.json` ja registra que, onde os
     dois lados dela divergirem, manda a PROIBICAO — mas o exemplo continua
     escrito, e ele nao e texto servido, entao nenhuma regua o alcanca.

  O QUE CONTINUA TRAVADO E NAO E DA FUNDACAO: o `.gov.br` inteiro (o CTB, que e
  quem decide habilitacao, e as prefeituras da camada municipal) e as tres
  etiquetas do Mercado Livre. Os dois estao em `dados/despachos.md`.
