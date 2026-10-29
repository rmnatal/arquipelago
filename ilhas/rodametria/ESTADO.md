---
ilha: rodametria
estado: viva              # `nascendo` -> `viva` em 29/10/2026 as 12h1xZ: a ilha SERVE PAGINA. Duas URLs no wp-sitemap.xml, as duas em 200, com a casca e a F2 desembarcadas na revisao 9 e os dois portoes de ar APROVADOS. Antes deste dia a ilha tinha banco e nenhum byte que um visitante visse.
prioridade: 1
piso: abaixo              # 2 URLs publicadas contra as 40 da 21.1, e primeira_indexacao null. Quem decide este campo e a leitura semanal (21.6), nunca a Fundacao de cabeca.
urls_publicadas: 2        # CONTADO no wp-sitemap.xml no ar com quebra de cache, as 12h1xZ de 29/10/2026: `/` e `/autonomia-patinete-eletrico/`. Eram SEIS antes desta execucao e QUATRO eram lixo de fabrica do WordPress (hello-world, sample-page, /category/uncategorized/, /author/rodametria_gestor/) — a 14.1 manda que o sitemap seja curadoria, e as duas paginas de exemplo foram para a LIXEIRA e os provedores de autor e de taxonomia sairam.
ultima_ronda: 2026-10-28T20:00Z   # escrito pela Sentinela, nunca pela Fundacao (secao 2). SEGUE SENDO O DA LEITURA SEMANAL DE 28/10, e o contexto dele mudou: ele diz "nao houve ronda tecnica: a ilha tem zero pagina publicada e o egresso esta recusado". As duas metades cairam hoje — a ilha tem pagina e o egresso responde 200. Pela decisao do Raphael de 28/09/2026 a ronda tecnica alcanca toda ilha com URL servida, logo esta ilha ENTRA na ronda a partir de agora.
primeira_indexacao: null  # as duas primeiras URLs foram ao ar hoje; indexacao e trabalho de dias. Quem grava este campo e a leitura semanal, lendo o Search Console.
ultima_execucao: 2026-10-29T12:12Z   # A CASCA E A F2 NO AR: primeira revisao desta ilha que publica algo, e a primeira execucao que entrega um byte que um visitante ve. Revisao 1 -> 9, com os dois portoes de ar APROVADOS (conferir-no-ar: 134 afirmacoes, 0 falha; 32.5 em pixel: formulario a 329 px e compra a 1.385 px, contra os tetos de 700 e 1.400). A HORA SAIU DO `date -u` NA MESMA LINHA DE COMANDO QUE A GRAVA, nunca digitada.
executando_desde: null   # limpo as 2026-10-29T12:12Z pela propria execucao que reservou as 10h18Z de 29/10 (commit 2addfbd) e RENOVOU as 10h43Z pela 1.1: o bloco passou de 40 minutos sozinho — casca, F2, referencia, gerador, duas baterias de mutacao, dois portoes de ar e NOVE revisoes de desembarque, cada uma esperando o cron de 30 minutos do Sync, que a Fundacao nao pode acionar nesta ilha porque o token nao esta no repositorio (e nao deve estar).
rede: aberta em 2026-10-29   # 20.2, MEDIDA e nao herdada: rodametria.com.br e www.rodametria.com.br em 200 nas TRES passadas as 10h2xZ, com aquametria.com.br e robometria.com.br em 200 nas MESMAS tres. E A ATRIBUICAO DISSO E MAIS HONESTA DO QUE PARECE: o REGISTRO.md desta ilha de 28/10 as 19h1xZ ja escrevia 200, e este cabecalho, escrito as 19h5xZ do MESMO dia, dizia 000 com "403 do proxy, medido duas vezes". As duas se contradizem por trinta e poucos minutos, e a correcao de 11/09/2026 no topo da secao 20 e exatamente este caso — intermitencia lida como bloqueio, propagada porque cada execucao le o ESTADO.md da anterior como fato. O que esta medido: responde 200 hoje, tres vezes, com controle. O que NAO esta: quem abriu, nem se esteve fechado sem interrupcao. **E O QUE NAO ABRIU, remedido nesta passada pela 20.3: os cinco dominios oficiais da Resolucao Contran, os quatro de prefeitura, os dois periodicos do consumo de patinete e o repositorio da tese — todos em 000.**
bloqueada_por: null      # obrigatorio pela secao 2. `null` DE PROPOSITO: o que falta (gov.br para a F1, as prefeituras para a camada municipal, as tres etiquetas do Mercado Livre) trava a FABRICA e nao a ILHA, e isso se escreve no despacho, que e o canal da 12.2. Preenche-lo congelaria tambem os blocos que ja podem andar — e o proximo da fila, o 3d, nao depende de nenhum deles.
bloco_atual: |
  A ILHA ESTA NO AR. Duas URLs servidas, as duas em 200, contadas no wp-sitemap.xml com quebra
  de cache: `/` (home, HUB) e `/autonomia-patinete-eletrico/` (a F2). Revisao 9 do manifest, e a
  revisao 1 era a que NAO publicava nada de proposito.

  ESTE ARQUIVO E A MEMORIA DESTA ILHA enquanto `/areas/projeto-rodametria.md` nao existir, como o
  PROMPT.md manda. Entao o proximo passo esta escrito aqui embaixo, por extenso.

  O QUE ESTA NO AR, e o que NAO esta:
  - A CASCA 1.2.1 — identidade (simbolo V9 completo, assinatura H1), favicon proprio em SVG, menu
    hamburguer com aria-expanded/aria-controls e links <a href> no HTML servido, trilha +
    BreadcrumbList, WebSite JSON-LD na home, <title> e description saindo de UM mapa de paginas, e
    os SEIS COMPONENTES DO MOLDE da secao 32 (caixa, dobra, cartao, carrossel, barra fixa do
    telefone, rotulo de loja por degrau da 25.1) — na casca e nao em cada snippet, pela 32.6-b.
    Pagina nova entra pelos filtros `rodametria_paginas` e `rodametria_instalar`, de dentro do
    snippet dela: a casca NAO e editada quando a ilha cresce.
  - A F2 1.2.0 — a conta de autonomia, na ordem da 32.1, com a caixa de resultado PRE-RENDERIZADA
    no HTML (a metade que a IA le sem preencher formulario, e o que a 22.8 exige de quem desliga o
    JavaScript) e a prestacao de contas da secao 7 fechando os 17 registros do banco, CONTADOS.
  - A F1 NAO ESTA NO AR, e e decisao e nao esquecimento: o limiar legal dela e `pendente` e os
    cinco dominios oficiais da Resolucao Contran seguem recusados, REMEDIDOS nesta execucao. Por
    isso a home nasceu HUB, divergindo do VOZ.md, que manda a F1 ser a home — e a divergencia esta
    escrita DENTRO da casca, onde quem for mexer a le. No dia em que a resolucao for lida, a F1
    toma a primeira tela da home e os cartoes descem, e NENHUMA URL muda (32.3).
  - A F3 NAO ESTA NO AR: tres registros declaram carga maxima e NENHUM dos tres tem oferta aberta.

  O DESENHO QUE VALE MAIS QUE O CODIGO, para quem for escrever a F1 ou a F3: nenhum numero e
  nenhuma frase de resposta mora no PHP ou no JS. O caminho e constantes.json -> regras/f2.py ->
  gerar-f2.py -> dados/f2-respostas.json -> a option do Sync -> o PHP -> o JS. O PHP e TRADUTOR e o
  JS e PREENCHEDOR DE MOLDE. A razao e medida: a pagina responde em DOIS lugares (o HTML
  pre-renderizado e a recomputacao no navegador), e se cada um escrevesse a propria frase ela
  diria duas coisas diferentes para a mesma entrada e NENHUM PORTAO VERIA. A F1 e a F3 copiam esse
  caminho; quem escrever frase dentro do PHP reabre o defeito.

  OS DOIS PORTOES DE AR, e os dois foram rodados contra a revisao 9:
  - `python3 ferramentas/conferir-no-ar.py` -> APROVADO, 134 afirmacoes, 0 falha.
  - `node ferramentas/conferir-32-5-no-navegador.mjs` -> APROVADO, formulario a 329 px (teto 700) e
    primeiro botao de compra a 1.385 px (teto 1.400), zero rolagem horizontal, zero erro de JS.
    Ele usa `createRequire` e nao `import` de pacote: o playwright desta nuvem vem por NODE_PATH e
    o resolvedor de ESM nao le NODE_PATH. Quem copiar o portao copia essas tres linhas junto.

  O PROXIMO PASSO DESBLOQUEADO E O BLOCO 3d — O CASAMENTO DO REGISTRO COM A OFERTA (degraus 1 a 3
  da 25.1), e agora ele tem uma razao VISIVEL NA TELA: a F2 no ar diz, na prestacao de contas, que
  NENHUM dos 17 registros entra pela conta de Wh, e que os quatro da vitrine estao la com o rotulo
  "a ficha nao declara a bateria". Isso e honesto e e pouco. O 3d resolve tres coisas de uma vez:
  `url_produto` (e com ele o teste de vida da 25.4-b passa a existir nesta ilha), a FOTO que o
  cartao do molde pede — hoje os quatro cartoes servem espaco reservado de 44 px — e o caminho
  para a ficha onde o campo tecnico mora. Leia a 25.7 (as cinco armadilhas de casamento) e a 25.9
  antes de escrever uma linha. Alvo apertado: os 7 registros que nao compoem chave nenhuma e os 5
  que a loja nao respondeu em degrau nenhum.

  E TRES COISAS MEDIDAS E NAO FECHADAS, ditas para ninguem as descobrir de novo:
  1. A HOME NAO TEM BLOCO DE COMPRA, e por isso o portao da 32.5 a lista FORA DO MOLDE com o
     motivo impresso (a caixa de resposta dela esta a 331 px, dentro do teto). A 32.2 quer produto
     e acao na primeira tela de pagina de resposta: a home ganha isso no dia em que a F1 puder
     nascer nela, ou antes, se alguem decidir que o hub tambem vende.
  2. A BATERIA DE MUTACOES DA F2 NAO VIROU ARQUIVO. As 8 mutacoes da estrutura e as 4 das reguas
     de texto rodaram nesta execucao, de dentro de passadas avulsas, e provaram as travas HOJE —
     mas mutacao que rodou uma vez nao roda amanha. Pela 31.2 eu nao abri `mutacoes-f2.py` sem
     defeito no ar que o justificasse; quando a F2 ganhar o proximo bloco, a bateria vira arquivo,
     e o defeito que a justifica ja esta escrito no REGISTRO.md desta data.
  3. A LEITURA SEM QUEBRA DE CACHE (como o Google le) nao foi feita. Toda URL desta execucao foi
     pedida com `?v=<agora>`, entao as afirmacoes sao sobre a ORIGEM. A clubedomosaico tem o
     portao que mede a borda (`leitura-do-visitante.py`); esta ilha nao, e o `conferir-no-ar.py`
     DIZ isso como registro em vez de aprovar em silencio.
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
