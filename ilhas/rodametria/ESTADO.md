---
ilha: rodametria
estado: viva              # `nascendo` -> `viva` em 29/10/2026 as 12h1xZ: a ilha SERVE PAGINA. Duas URLs no wp-sitemap.xml, as duas em 200, com a casca e a F2 desembarcadas na revisao 9 e os dois portoes de ar APROVADOS. Antes deste dia a ilha tinha banco e nenhum byte que um visitante visse.
prioridade: 1
piso: abaixo              # 2 URLs publicadas contra as 40 da 21.1, e primeira_indexacao null. Quem decide este campo e a leitura semanal (21.6), nunca a Fundacao de cabeca.
urls_publicadas: 2        # CONTADO no wp-sitemap.xml no ar com quebra de cache, as 12h1xZ de 29/10/2026: `/` e `/autonomia-patinete-eletrico/`. Eram SEIS antes desta execucao e QUATRO eram lixo de fabrica do WordPress (hello-world, sample-page, /category/uncategorized/, /author/rodametria_gestor/) — a 14.1 manda que o sitemap seja curadoria, e as duas paginas de exemplo foram para a LIXEIRA e os provedores de autor e de taxonomia sairam.
ultima_ronda: 2026-10-28T20:00Z   # escrito pela Sentinela, nunca pela Fundacao (secao 2). SEGUE SENDO O DA LEITURA SEMANAL DE 28/10, e o contexto dele mudou: ele diz "nao houve ronda tecnica: a ilha tem zero pagina publicada e o egresso esta recusado". As duas metades cairam hoje — a ilha tem pagina e o egresso responde 200. Pela decisao do Raphael de 28/09/2026 a ronda tecnica alcanca toda ilha com URL servida, logo esta ilha ENTRA na ronda a partir de agora.
primeira_indexacao: null  # as duas primeiras URLs foram ao ar hoje; indexacao e trabalho de dias. Quem grava este campo e a leitura semanal, lendo o Search Console.
ultima_execucao: 2026-10-29T16:42Z   # BLOCO 3e ENTREGUE: a premissa dele (coleta em ficha de fabricante) estava ERRADA e esta corrigida por medicao, e a coleta achou um defeito NO AR — o bloco de compra dizia a mesma coisa TRES vezes e a pagina de autonomia estava calada sobre autonomia. Revisao 12, os dois portoes de ar APROVADOS. A HORA SAIU DO `date -u` NA MESMA LINHA DE COMANDO QUE A GRAVA, nunca digitada.
executando_desde: null   # limpo as 2026-10-29T16:42Z pela propria execucao que reservou as 16h25Z e RENOVOU as 16h37Z pela 1.1. E o custo da espera caiu nesta passada: o cron do Sync roda por VISITA e nao por relogio (ver o bloco_atual), entao a revisao 12 entrou em um minuto depois de tres GETs na home, em vez das nove esperas de cron da execucao de manha.
rede: aberta em 2026-10-29   # 20.2, MEDIDA e nao herdada: rodametria.com.br e www.rodametria.com.br em 200 nas TRES passadas as 10h2xZ, com aquametria.com.br e robometria.com.br em 200 nas MESMAS tres. E A ATRIBUICAO DISSO E MAIS HONESTA DO QUE PARECE: o REGISTRO.md desta ilha de 28/10 as 19h1xZ ja escrevia 200, e este cabecalho, escrito as 19h5xZ do MESMO dia, dizia 000 com "403 do proxy, medido duas vezes". As duas se contradizem por trinta e poucos minutos, e a correcao de 11/09/2026 no topo da secao 20 e exatamente este caso — intermitencia lida como bloqueio, propagada porque cada execucao le o ESTADO.md da anterior como fato. O que esta medido: responde 200 hoje, tres vezes, com controle. O que NAO esta: quem abriu, nem se esteve fechado sem interrupcao. **E O QUE NAO ABRIU, remedido nesta passada pela 20.3: os cinco dominios oficiais da Resolucao Contran, os quatro de prefeitura, os dois periodicos do consumo de patinete e o repositorio da tese — todos em 000.**
bloqueada_por: null      # obrigatorio pela secao 2. `null` DE PROPOSITO: o que falta (gov.br para a F1, as prefeituras para a camada municipal, as tres etiquetas do Mercado Livre) trava a FABRICA e nao a ILHA, e isso se escreve no despacho, que e o canal da 12.2. Preenche-lo congelaria tambem os blocos que ja podem andar — e o proximo da fila, o 3d, nao depende de nenhum deles.
bloco_atual: |
  A PREMISSA DO BLOCO 3e ESTAVA ERRADA, E O QUE A COLETA ACHOU FOI UM DEFEITO NO AR.
  O bloco fechou pelos dois lados: a premissa esta corrigida POR MEDICAO, e a pagina
  de autonomia deixou de dizer a mesma coisa tres vezes e passou a dizer a autonomia.

  ESTE ARQUIVO E A MEMORIA DESTA ILHA — `/areas/projeto-rodametria.md` NAO EXISTE nesta
  nuvem (procurado nesta passada, nao encontrado), como o PROMPT.md previa. O proximo
  passo esta escrito aqui embaixo, por extenso.

  O QUE ESTA NO AR (revisao 12, CONFERIDA: `/status` em 12 igual ao manifest, as DUAS
  linhas da revisao 12 do log dizendo `ok` lidas uma por uma pela 20.4,
  `conferir-no-ar.py` em 138 afirmacoes e 0 falha, e o portao de pixel da 32.5 no
  navegador a 390 px APROVADO):
  - O primeiro cartao de `/autonomia-patinete-eletrico/` serve
    `22 km declarados pelo vendedor · 500 W no anúncio · a ficha não declara a bateria`.
    A pagina que RESPONDE autonomia estava calada sobre o unico numero de autonomia
    que a oferta do botao dela declara.
  - `bateria não declarada` tem ZERO ocorrencia na pagina (eram 4, uma por cartao) e a
    frase digitada `Nenhum destes entrou pela conta de Wh` tem ZERO (era 1).
  - A frase de abertura do bloco de compra e DERIVADA: `Nenhum dos 4 com oferta aberta
    hoje entrou pela conta de Wh, e cada cartão diz por quê.` O `4` e contado da vitrine.
  - 32.5: formulario 329 px (teto 700) e primeiro botao de compra 1.380 px (teto 1.400).
    O botao SUBIU 5 px com uma linha A MAIS no cartao, porque a frase de abertura
    derivada e mais curta que a digitada e devolveu uma linha acima dos cartoes.
  - A F1 e a F3 seguem fora do ar, e agora com a causa MEDIDA em vez de suposta — leia
    o paragrafo do gargalo mais abaixo.

  O QUE A MEDICAO DO 3e DECIDE, e e a parte que vale mais que o campo colhido:
  O NIVEL 4 DA ESCADA (ficha de fabricante) PODE SER ESTRUTURALMENTE VAZIO NESTE NICHO.
  Nao e bloqueio a remover: as duas marcas principais do banco nao tem site de
  fabricante achavel — a Honeywhale vende por vitrine de marketplace e varejo mexicano,
  a MAXSHOT so aparece em varejista brasileiro. Abrir o egresso dos cinco dominios de
  fabricante nao encheria este nivel.
  E O GARGALO TEM NOME, UM SO: O NIVEL 5 (varejo grande) ESTA ATRAS DO EGRESSO.
  casasbahia, extra e magazineluiza em 000 nas TRES passadas as 16h2xZ, com controle
  verde e `connect_rejected` lido no status do proxy. A leitura por BUSCA — a unica
  porta aberta — alcanca os niveis 6, 7 e 8, que sao EXATAMENTE os que a escada recusa
  nos quatro campos do nivel 5. Logo `potencia_nominal_w`, `velocidade_max_kmh`,
  `acelerador` e `carga_max_kg` NAO SAO COLHIVEIS desta nuvem por caminho nenhum.
  A F1 e a F3 nao vao ao ar por coleta: vao por ABERTURA. Despacho ALTA em
  `dados/despachos.md`, e ele deixou de ser "seria bom" e passou a ser o unico caminho.

  O QUE A BUSCA ACHOU E FOI RECUSADO, escrito no esquema registro a registro para a
  proxima execucao nao gastar a mesma busca: a variante de 350 W do M2 MAX (loja
  estrangeira, nivel 8, nao sustenta campo nenhum), os 36 V que sao do MAX-B (nivel 7,
  e outro aparelho — justamente o que as travas do casamento barraram), os 25 km/h de
  guia de compra contra os 32 km/h da oferta (os dois campos exigem nivel 5, e a
  divergencia entre as leituras e ela mesma a prova de que aceitar uma seria sorteio),
  e o `bico` da camara Kenda, que nao esta publicado em lugar nenhum alcancavel.

  O ACHADO DE METODO DESTA PASSADA, E ELE MUDA O CUSTO DE TODA EXECUCAO NESTA ILHA:
  O CRON DO SYNC NAO RODA POR RELOGIO — ELE RODA POR VISITA. O log do `/status` tinha
  disparos as 11h39, 12h09, 13h56 e 14h09 e depois NADA por 2h29, e as 14h12Z e
  exatamente quando a execucao anterior parou de abrir o site. E WP-Cron: ele e
  acionado por requisicao, nao por um relogio no servidor. Tres GETs na home as 16h38Z
  e o `wp-cron.php` respondeu 409 (ja havia cron em andamento); a revisao 12 entrou em
  UM minuto. O `ESTADO.md` anterior registrou "nove esperas de cron" entre 10h44Z e
  12h10Z numa unica execucao: aquele custo era evitavel. A FUNDACAO NAO ESPERA O CRON
  NESTA ILHA — ELA O ACIONA, abrindo a propria pagina. Nao precisa do token para isso.

  E DUAS COISAS MEDIDAS E NAO FECHADAS, ditas para ninguem as descobrir de novo:
  1. A BATERIA DO HONEYWHALE M2 MAX NAO ESTA PUBLICADA EM PORTA NENHUMA ALCANCAVEL.
     Dos 10 titulos que a Open API devolveu para a chave do casamento, ZERO declara
     tensao ou amperagem. Enquanto nenhum registro com oferta aberta declarar V e Ah,
     o grupo `cabem_no_wh` fica vazio e o bloco de compra desta pagina continua
     dizendo o que os cartoes SAO em vez do que a conta escolheu. Isso e honesto e
     esta na tela; nao e defeito.
  2. A LEITURA SEM QUEBRA DE CACHE (como o Google le) segue nao feita, terceira
     execucao seguida. Toda URL desta passada foi pedida com `?v=<agora>`, entao as
     afirmacoes sao sobre a ORIGEM. A clubedomosaico tem o portao que mede a borda
     (`leitura-do-visitante.py`); esta ilha nao, e a 31.3 proibe abri-lo enquanto
     houver item de conteudo e de pagina pelo nome do produto aberto na fila.

  POR QUE NENHUM PORTAO NOVO NASCEU NESTA PASSADA, e e decisao e nao esquecimento: a
  31.3 proibe ampliar portao enquanto a ilha tiver item de conteudo ou de pagina pelo
  nome do produto aberto na fila, e os blocos 4, 5, 5b e 6 estao abertos. As cinco
  frases da funcao nova de abertura sao conferidas sobre mundos FABRICADOS dentro do
  proprio gerador (vitrine de 1 e de 4, com 0, com todos e com parte cabendo no Wh),
  que e o que a 32.5-d manda e nao custa arquivo novo.

  O PROXIMO PASSO DESBLOQUEADO E O BLOCO 5b — PAGINA PELO NOME DO PRODUTO (secao 30).
  E ele e o proximo por eliminacao MEDIDA, nao por ordem de lista: o 3e fechou e
  provou que coleta nao destrava mais nenhuma ferramenta desta ilha (o que destrava e
  o despacho do egresso, que nao e trabalho da Fundacao); o bloco 4 pede ferramenta
  nova e as duas que faltam, F1 e F3, estao travadas por dado que nao se colhe daqui;
  o 5 pede artigo-ancora PAREADO com ferramenta, e so ha uma ferramenta no ar. O 5b
  nao depende de nenhum dos tres: as seis cabecas de compra estao medidas no dossie
  (`moto eletrica` 823 mil, `bicicleta eletrica` 673 mil, `scooter eletrica` 301 mil,
  `patinete eletrico` 246 mil, `bike eletrica` 201 mil, `motos eletricas para adultos`
  201 mil), a SERP delas esta medida e NAO TOMADA, e a ilha tem 4 registros publicaveis
  com piso de compra e 1 com ficha para sustentar pagina de produto. A ilha tem 2 URLs
  contra as 40 do piso da 21.1, e e a unica fila que anda sem esperar ninguem.
  PRIMEIRO PASSO DELE: ler a secao 30 do ARQUIPELAGO.md inteira e a 21.4 (teto de leva
  por semana) ANTES de escolher quantas paginas, e escolher a PRIMEIRA cabeca pela
  interseccao entre volume e o que o banco sustenta — hoje `patinete eletrico`, que e
  a unica das seis com registro de ficha aberta nesta ilha.
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
