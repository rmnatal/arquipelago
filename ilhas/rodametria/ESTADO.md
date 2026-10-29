---
ilha: rodametria
estado: viva              # `nascendo` -> `viva` em 29/10/2026 as 12h1xZ: a ilha SERVE PAGINA. Duas URLs no wp-sitemap.xml, as duas em 200, com a casca e a F2 desembarcadas na revisao 9 e os dois portoes de ar APROVADOS. Antes deste dia a ilha tinha banco e nenhum byte que um visitante visse.
prioridade: 1
piso: abaixo              # 5 URLs publicadas contra as 40 da 21.1, e primeira_indexacao null. Quem decide este campo e a leitura semanal (21.6), nunca a Fundacao de cabeca. O teto da 21.4 tem folga: esta semana saiu UMA leva, de 3 URLs, contra o teto de 3 levas por semana.
urls_publicadas: 5        # CONTADO no wp-sitemap.xml no ar com quebra de cache, as 20h1xZ de 29/10/2026: `/`, `/autonomia-patinete-eletrico/`, `/veiculos/`, `/veiculos/patinete-eletrico/` e `/veiculos/bicicleta-eletrica/`. Eram 2 antes desta execucao. Corpo medido pelo portao: 2.586 · 11.246 · 3.488 · 9.408 · 6.377 caracteres, todos acima do piso de 1.500 da secao 8 — e a mae `/veiculos/` so passou porque a conta foi feita ANTES de medir no ar: ela daria 1.253.
ultima_ronda: 2026-10-28T20:00Z   # escrito pela Sentinela, nunca pela Fundacao (secao 2). SEGUE SENDO O DA LEITURA SEMANAL DE 28/10, e o contexto dele mudou: ele diz "nao houve ronda tecnica: a ilha tem zero pagina publicada e o egresso esta recusado". As duas metades cairam hoje — a ilha tem pagina e o egresso responde 200. Pela decisao do Raphael de 28/09/2026 a ronda tecnica alcanca toda ilha com URL servida, logo esta ilha ENTRA na ronda a partir de agora.
primeira_indexacao: null  # as duas primeiras URLs foram ao ar hoje; indexacao e trabalho de dias. Quem grava este campo e a leitura semanal, lendo o Search Console.
ultima_execucao: 2026-10-29T20:16Z   # BLOCO 5b ENTREGUE: a secao /veiculos/ e as duas primeiras paginas pelo nome do produto, no ar e conferidas. Das SEIS cabecas do dossie so DUAS abrem o portao da 30.2, e a causa das outras quatro esta medida e escrita. Revisao 16. A HORA SAI DO `date -u` NA MESMA LINHA DE COMANDO QUE A GRAVA, nunca digitada.
executando_desde: null   # limpo as 2026-10-29T20:16Z pela propria execucao que reservou as 19h18Z e RENOVOU as 19h37Z e 19h48Z pela 1.1. O bloco levou cerca de uma hora, e a espera NAO foi de trabalho: foi do cron do Sync, que roda a cada 30 minutos POR VISITA (20.6). A revisao 16 entrou as 20h09Z, 21 minutos depois do push, porque a passada anterior do cron havia sido as 19h48Z e o relogio dele nao se adianta por GET — os 409 do wp-cron.php sao o lock, nao prova de que a tarefa da ilha estava vencida.
rede: aberta em 2026-10-29   # 20.2, MEDIDA e nao herdada: rodametria.com.br e o /status em 200 nas TRES passadas as 19h1xZ, com aquametria.com.br em 200 nas mesmas tres. E A LEITURA SEM QUEBRA DE CACHE (como o Google le) tambem foi feita: as tres URLs novas em 200 nas duas leituras. O QUE REPROVOU FOI A BORDA DO HOSPEDEIRO, e nao e desta ilha: sonda VIRGEM em `/nao-existe-<relogio>-xyz/` devolveu 404 · 200 · 200 · 200, com o corpo do 404 servido em HTTP 200 e o title 'Pagina nao encontrada'. E o mesmo soft 404 que a clubedomosaico registra ha oito medicoes, agora medido numa SEGUNDA conta do mesmo hospedeiro — linha acrescentada ao despacho ALTA de dados/despachos.md. Nao se conserta daqui.
bloqueada_por: null      # obrigatorio pela secao 2. `null` DE PROPOSITO: o que falta (gov.br para a F1, as prefeituras para a camada municipal, as tres etiquetas do Mercado Livre) trava a FABRICA e nao a ILHA, e isso se escreve no despacho, que e o canal da 12.2. Preenche-lo congelaria tambem os blocos que ja podem andar — e o proximo da fila, o 3d, nao depende de nenhum deles.
bloco_atual: |
  BLOCO 5b ENTREGUE, E O ACHADO DELE E DE PALAVRA E NAO DE PRODUTO.

  NO AR: `/veiculos/` (a secao de nivel 1 da 16.1, com o nome que o VOZ.md ja declarava no menu),
  `/veiculos/patinete-eletrico/` e `/veiculos/bicicleta-eletrica/`, filhas diretas dela pela 30.1, no
  molde da 32.2. Revisao 16, casca 1.2.1 -> 1.4.0, snippet `rodametria-produto` 1.0.0.

  ESTE ARQUIVO CONTINUA SENDO A MEMORIA DESTA ILHA — `/areas/projeto-rodametria.md` nao existe nesta
  nuvem, e e por isso que este campo e longo.

  O ACHADO: a chave `patinete eletrico` devolve ZERO patinete de adulto nas 20 primeiras ofertas da
  loja; serve `Patinete Eletrico Infantil 150W UNITOYS` e `Moto Eletrica Infantil 6V`. Com o
  qualificador `adulto` a MESMA familia devolve 16 patinetes de adulto, de R$ 1.297,13 a R$ 3.399,00, e
  5 e-bikes, tres delas com 74, 28 e 25 vendas. A consulta e a palavra da PESSOA; a chave e a palavra
  da LOJA, e neste nicho elas divergem por um qualificador. Cada consulta passou a declarar uma ESCADA
  DE CHAVES com o degrau gravado, pela 25.6(a).

  DAS SEIS CABECAS SO DUAS NASCERAM, e a causa das outras quatro esta medida em
  `dados/consultas-de-produto.json`: `moto eletrica` e `scooter eletrica` tem tres anuncios de adulto,
  ZERO venda nos tres e precos variando R$ 6.500 para a mesma classe — o caminho delas e o Mercado
  Livre, onde a geracao de link exige clique humano (25.6), logo e DESPACHO e nao bloco. `bike
  eletrica` e `motos eletricas para adultos` nao nascem pela 30.4, por serem a mesma intencao de outras
  duas.

  NENHUM DADO TECNICO FOI PUBLICADO, e isso e o produto da pagina: potencia nominal, velocidade maxima,
  acelerador e carga maxima tem piso de nivel 5 no esquema e titulo de anuncio e nivel 6. A coluna diz
  o que o anuncio DECLARA, e a frase que conta isso e CONTADA no gerador em cinco formas: de 16
  anuncios do patinete, 15 declaram um watt e 1 diz qual watt e.

  OS NUMEROS NO AR: `conferir-no-ar.py` APROVADO com 281 afirmacoes e 0 falha;
  `conferir-32-5-no-navegador.mjs` APROVADO em 3 de 3 paginas do molde, com a caixa de resposta a 211
  px (teto 700) e o primeiro botao de compra a 1.129 e 1.084 px (teto 1.400); 21 links `sponsored`,
  ItemList com 16 itens, FAQPage com 4 perguntas e BreadcrumbList de tres niveis na pagina do patinete.
  Bancada: 13 portoes sem rede, 0 falha, contra 9 antes deste bloco. `mutacoes-produto.py`: 26
  mutacoes, 26 reprovadas, 0 sobrevivente e 0 inerte.

  O DEFEITO QUE A ENTREGA ACHOU NO AR, e ele e a secao 4 em forma de instalador: a revisao 13 subiu os
  arquivos e NAO criou as tres paginas. A instalacao da casca rodava uma vez por VERSAO, e a 13 subiu
  casca nova e o snippet da pagina nova na MESMA passada do Sync — quando o `init` chamou a instalacao,
  o snippet novo ainda nao estava carregado naquela requisicao, entao o filtro `rodametria_instalar`
  dele nao existia. O sintoma era VERDE EM TODO LUGAR: /status em 13, as cinco linhas do log dizendo
  `ok`, a rota `/casca` ja listando as tres paginas no mapa com `url` VAZIA nos tres, e o
  wp-sitemap.xml com duas URLs. A casca 1.4.0 passou a reinstalar tambem quando a ASSINATURA DO MAPA
  muda, e nao so quando a versao dela muda.

  E A CASCA JA TINHA SUBIDO PARA 1.3.0 POR DUAS RAZOES DE ARVORE, as duas da 16:
  `garantir_pagina()` passou a aceitar PAI (16.2), e `url_do_slug()` passou a achar a pagina pela meta
  `_rodametria_id` em vez de por caminho — `get_page_by_path()` casa o caminho INTEIRO e devolveria
  nulo para a filha, com `casca_link()` transformando link vazio em texto sem reclamar.

  O QUE FICOU FORA DO MOLDE, dito sem maquiar: `/veiculos/` e a home sao as duas paginas desta ilha sem
  componente da 32 (sem formulario e sem bloco de compra), e o portao de pixel as lista como FORA DO
  MOLDE em vez de aprova-las em silencio. Para a home isso e decisao registrada, ela nasceu HUB; para a
  mae e porque a 32 nao nomeia familia de pagina de LISTAGEM — ela tem FERRAMENTA (32.1) e
  FICHA/RESPOSTA (32.2) e mais nada. Duas ilhas ja tem pagina de listagem, `/materiais/` da
  clubedomosaico e esta. Fica anotado para a leitura semanal; nao inventei regra de cabeca.

  O PROXIMO PASSO DESBLOQUEADO E O 5c, E ELE SE DIVIDE EM DOIS. A maquina do 5b faz pagina nova SEM UMA
  LINHA DE CODIGO: declarar a consulta em `dados/consultas-de-produto.json` com a escada de chaves e
  escrever a voz em `dados/paginas-de-produto.json`. O que TRAVA o primeiro passo e a 30.8: `alvo` nao
  se afirma desta nuvem, nunca, e nenhuma consulta de CAUDA teve a SERP brasileira aberta com os olhos
  — as seis cabecas tem (Raphael, 27/10, Chrome dele). Entao a parte desta nuvem e montar a lista das
  caudas de `dados/corpus-buscas.md` (`patinete eletrico adulto` 49,5 mil, `scooter eletrica 1000w`
  33,1 mil, `moto eletrica 1000w` 14,8 mil) com os `tomada` FECHADOS e os `nao-medida` NOMEADOS com as
  URLs; a outra parte e uma sessao de Chrome dele, que a propria 30.8 chama de "um despacho de uma
  sessao, nao um bloco". Publicar na execucao seguinte, sem remedir nada.
---

# Estado da ilha RODAMETRIA

Espelho legível do estado do projeto. **Nunca guarde credencial aqui.**

## Infraestrutura
- Domínio: **`rodametria.com.br` — REGISTRADO E PAGO pelo Raphael em 27/10/2026** (RDAP oficial lido no Chrome dele às 16h41 de Brasília: `status: active`, registro 27/10/2026 19:31Z, expira em 27/10/2028, nameservers ainda `a.auto.dns.br` / `b.auto.dns.br`). Passo 1 da seção 11 cumprido.
- Hospedagem: domínio adicional no mesmo plano da HostGator, raiz própria. **FEITO** — o domínio serve HTML próprio.
- Nameservers `ns604` / `ns605.hostgator.com.br`: **FEITO** — o DNS delegou e o domínio resolve.
- Search Console (propriedade de Domínio): **não medido daqui** (é navegador do Raphael).
- WordPress: **NO AR desde 27/10/2026 às 22h17Z**, medido em 28/10 às 10h17Z pela execução do bloco 1 —
  `https://rodametria.com.br/` devolve 200, `<title>Rodametria - Mobilidade elétrica</title>`, tema de blocos cru,
  **nenhuma página publicada**, `/wp-sitemap.xml` sem URL nenhuma. `/nao-existe-xyz/` devolve 404 de verdade, então
  a porta de entrada da seção 29 está sã nesta primeira leitura.
- Snippet de Sync: `Rodametria Sync`, versão **1.1.5**. **NO AR** — `/wp-json/rodametria/v1/status` devolve 200,
  revisão **9** (igual ao `manifest.json`), com as linhas da revisão corrente no log dizendo `ok` uma por uma
  (20.4, lidas pelo portão). **O cron é de ~25 a 30 minutos e é o ÚNICO caminho de desembarque desta ilha:** o
  token do Sync não está no repositório e não deve estar, então a Fundação **não aciona** o Sync aqui — ela empurra
  e espera. Nesta execução isso custou **nove esperas de cron** entre 10h44Z e 12h10Z. *(Esta linha dizia "revisão
  1" até 29/10 às 12h1xZ; é a seção 4 em ação.)*
- **Casca e F2 NO AR desde 29/10/2026 às 12h10Z**, na revisão 9. `rodametria_casca` (#6) e `rodametria_f2` (#7) no
  Code Snippets, páginas `inicio` (#7, fixada como página inicial) e `autonomia-patinete-eletrico` (#8).
  A casca publica `/wp-json/rodametria/v1/casca` (GET público) com a versão, o relato da instalação e o mapa de
  páginas — é por ele que o portão de ar confere que nenhum link interno aponta para 404.
- Lista de Domínios permitidos (seção 20): **FEITO para o domínio da ilha** — o egresso desta nuvem alcança
  `rodametria.com.br`. **E FEITO TAMBÉM PARA A SHOPEE**, medido em 28/10 às 19h1xZ pela 20.3:
  `open-api.affiliate.shopee.com.br` em 200, `shopee.com.br` em 200, `s.shopee.com.br` em 307 — é o que tornou o
  piso de compra possível nesta ilha, e nenhuma execução dela tinha medido isso. **Falta `gov.br`**, que é a fonte
  da F1: despacho ALTA de 28/10 em `dados/despachos.md`, **REMEDIDO em 29/10 às 10h2xZ e ainda recusado** — os
  cinco domínios oficiais em `000`, com `rodametria.com.br` em 200 na mesma passada.

## O que já foi entregue
- Dossiê, ficha, identidade aprovada (símbolo V9, assinatura H1), `DESIGN.md`, `VOZ.md` e `logo.svg` — 27/10/2026, pela Bússola. Nenhuma URL publicada.
- **BLOCO 1 — `dados/corpus-buscas.md`**, 28/10/2026: quatro eixos, 19 consultas com procedência medida consulta a
  consulta, a **S_par medida** (era a primeira tarefa de leitura que o dossiê deixou) e a contagem do vazamento da
  busca da nuvem **por eixo** (zero fora do Brasil no eixo da regra; quase total no de autonomia e no de peças).
  Nenhuma URL publicada — bloco de dado, `publicar: false`.
- **BLOCO 2 — `dados/especificacao-calculadoras.md` e `dados/constantes.json`**, 28/10/2026: as três ferramentas
  especificadas inteiras e 9 constantes com procedência, com os quatro limiares legais da F1 isolados num objeto só.
- **BLOCO 3 — o MODELO DO BANCO**, 28/10/2026: `dados/esquema-banco.json`, 24 registros, `validar-banco.py`,
  `derivar-banco.py`, `mutacoes-banco.py` (66 casos) e `bancada.py`. Zero registro `publicavel`.
- **O PISO DE COMPRA**, 28/10/2026 às 19h3xZ: `escada_de_compra` no esquema (**versão 2**),
  `ferramentas/coletar-piso-de-compra.py` e `ferramentas/mutacoes-piso.py`. **5 de 17 registros não excluídos
  passaram a `publicavel`** — 4 veículos e a câmara Kenda —, cada um com a palavra-chave **medida na Open API**
  (`ofertas_na_medicao` gravado), a busca crua, o link encurtado com `sub_id_1` e `encurtamento_tentado_em`.
  **Nenhuma URL publicada:** esta ilha não tem página, e o piso vive no banco.

- **A CASCA (bloco 3b) — 29/10/2026 às 10h1xZ–12h1xZ, e com ela A ILHA SAIU DO CHÃO.**
  `snippets/rodametria-casca.php` (1.2.1) e `snippets/rodametria-f2.php` (1.2.0), mais `regras/f2.py` (o cérebro),
  `dados/f2-respostas.json` (tudo que a tela serve), `ferramentas/gerar-f2.py`, `ferramentas/teste-f2.py`,
  `ferramentas/atualizar-manifest.py`, `ferramentas/conferir-no-ar.py` e
  `ferramentas/conferir-32-5-no-navegador.mjs`. **DUAS URLs no ar**, os dois portões de ar APROVADOS, e a bancada
  em 8 portões / 0 falha. O manifest saiu da revisão 1 para a 9 — e **cinco dessas revisões foram conserto de
  defeito que só o ar mostrou**, cada um registrado no `REGISTRO.md`: a option lida com o nome errado (o Sync grava
  com hífen, a casca pedia com sublinhado), o sitemap servindo quatro URLs de lixo de fábrica do WordPress, dois
  `<h1>` por página, a palavra "egresso" chegando à tela **por dado** e não por código, texto ASCII sem acento no
  mesmo campo, e o primeiro botão de compra a 1.730 px contra o teto de 1.400 da 32.5.

## O que está travando
- ~~**A CASCA (bloco 3b) não é o próximo passo, e isto foi MEDIDO em 28/10 às 19h3xZ.**~~ — **SUPERADO EM
  29/10/2026: A CASCA FOI, e a medição que o item traz continua VERDADEIRA — ela só não impedia a casca.** O que
  ela impede é o bloco de compra servir *"o produto que a ferramenta escolheu"*, e a saída foi a página **dizer
  isso**, com a prestação de contas da seção 7 nomeando cada um dos 17 registros num grupo por causa: nenhum entra
  pela conta de Wh, e os quatro da vitrine estão lá com o rótulo "a ficha não declara a bateria". A seção 7 proíbe
  bloco de compra vazio e proíbe recomendar em primeiro lugar o que a página diz não servir — as duas são obedecidas
  dizendo a causa. **O 3d continua sendo o próximo passo**, e agora com a razão visível na tela. O texto original
  fica abaixo, preservado.** O piso e o dado técnico
  caíram em registros **diferentes** e a interseção é **vazia**: dos 4 veículos publicáveis, zero declara
  tensão+amperagem (entrada da F2) e zero declara carga máxima (entrada da F3); os 2 com Wh derivado e os 3 com
  carga máxima estão todos entre os 12 **sem** saída de compra. A 32.1 põe na primeira tela o bloco de compra com
  **o produto que a ferramenta escolheu**, e hoje nenhuma das três escolhe um publicável. **O que destrava é o
  CASAMENTO do registro com a oferta (degraus 1 a 3 da 25.1)** — ele traz a ficha e, com ela, o campo técnico.
  O aviso está dentro do `validar-banco.py`, para ser lido por quem abrir o banco e não só por quem abrir este arquivo.
- **A fonte oficial da F1.** O texto da Resolução Contran nº 996/2023 no `gov.br` é **negado pelo egresso desta
  nuvem** (`connect_rejected`, e `ENOTFOUND www.gov.br` na busca de página), medido em 28/10 às 10h4xZ. O bloco 2
  pode ser escrito inteiro, mas a constante central nasce `publicavel: false`. Despacho **ALTA** de 28/10 em
  `dados/despachos.md`. **Isto NÃO é `bloqueada_por`** (seção 11, passo 4): travou uma fonte, não a ilha.
- **A SERP dos eixos de autonomia, carga e peças**, que a busca da nuvem não vê (30.8) — despacho NORMAL de 28/10.
- Os passos 4b a 9 da seção 11 que faltam (Search Console, snippet de Sync, plugins, conta de serviço) são trabalho
  de navegador do Raphael. **O WordPress e o DNS já saíram dessa lista** — ver a Infraestrutura acima.
- Os blocos 2 e 3 não dependem de site, e o 2 é o próximo.
