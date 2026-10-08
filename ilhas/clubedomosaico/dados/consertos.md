# CONSERTOS DA SENTINELA — Clube do Mosaico

Trava 19.4(c) do `ARQUIPELAGO.md`: todo conserto que uma ronda faz entra aqui, e a ronda SEGUINTE abre esta lista antes de qualquer outra coisa e reconfere no ar o que está escrito. É essa releitura que substitui a validação pelo autor. Uma linha por conserto.

| data | URL | o que mudou | conferido pela ronda de |
|---|---|---|---|
| 2026-09-24 | as 17 URLs do sitemap, mais `/wp-sitemap.xml`, `/robots.txt` e `/wp-json/` | o `.htaccess` da raiz tinha só o bloco `NFD EPC` e não tinha o `# BEGIN WordPress`: a ilha servia a página de estacionamento da HostGator em 16 das 17 URLs. Reparado por `flush_rewrite_rules( true )` pela rota `/rotas` da casca 1.12.0 | **a ronda de 28/09/2026 — PASSOU** |
| 2026-09-25 | os 31 links de Shopee do banco, servidos em `/materiais/qual-cola-usar-no-mosaico/` e `/materiais/quantas-pastilhas-para-mosaico/` | os `sub_id` estavam deslocados uma casa (`-clubedomosaico-F2--`, campo 1 vazio) nos 16 links de 13/09, e 15 itens não tinham piso encurtado. Todos regerados pela Open API (25.6, 25.8). As 13 chaves das pastilhas devolviam ZERO oferta e foram trocadas | **a ronda de 28/09/2026 — PASSOU** |
| 2026-09-25 | `/author/mosaico_gestor/`, `/materiais/como-sabemos/`, `/?s=<termo>`, `/atelie/` e os estados com parâmetro da F1 e da F2 | a ilha servia **DUAS** `<meta name="robots">` em toda página que saía do índice — a do núcleo e a que a casca, a F1, a F2 e o Leads imprimiam cada um num `wp_head` paralelo. E `/author/mosaico_gestor/`, que o Google indexou e serviu na posição 1,0, não tinha etiqueta nenhuma. Agora quem imprime é a casca 1.13.0, uma vez, pelo filtro `wp_robots`; quem quer sair do índice declara pelo `cdm_fora_do_indice` | **a ronda de 28/09/2026 — PASSOU EM 4 ALVOS, FALHOU NOS ESTADOS DA F1 (ver despacho de 28/09)** |
| 2026-09-28 | — | **Nenhum conserto.** A ronda diaria tecnica de 28/09/2026 (15h10Z) foi a PRIMEIRA ronda tecnica desta ilha e achou cinco defeitos; os cinco caem na lista fechada 19.2, que vale mais que a 19.1: (1) o texto de medida das pecas sai com a unidade dobrada — `46x36cm cm`, `35cm de diâmetro cm`, `46cm de diâmetro cm`, `46x37cm cm` — em 4 das 5 pecas, na vitrine `/loja/`, na pagina da peca e dentro do campo `description` do `Product` no JSON-LD; a causa e o molde que acrescenta ` cm` a um valor de `cdm_medidas` que ja traz a unidade, e o conserto e no snippet OU no dado que so existe no site (secao 24), nunca num arquivo do repositorio; (2) os estados com parametro da F1 (`/materiais/qual-cola-usar-no-mosaico/?base=...&onde=...`) NAO servem `<meta name="robots">` com `noindex` — servem so `max-image-preview:large` —, enquanto os da F2 servem; e codigo de snippet; (3) 27 imagens das 5 paginas de `/loja/` tem `alt` vazio, incluindo a foto de destaque de cada peca, e o `alt` mora na biblioteca de midia do WordPress, nao no repositorio; (4) 8 das 17 URLs nao tem `<meta name="description">` nenhuma — a home, `/loja/`, `/materiais/`, `/como-fazer/`, `/sobre/`, `/contato/`, `/divulgacao-de-afiliados/` e `/privacidade/` —, e quem emite a etiqueta e a casca; (5) 13 dos 38 itens do banco com link de afiliado tem `afiliado.degrau` em `null` servindo degrau 4, contra a 25.1. Os cinco foram para o `DESPACHO DA SENTINELA — 2026-09-28` no `PROMPT.md`. **RECONFERENCIA DA 19.4(c):** as tres linhas acima foram reconferidas no ar nesta ronda; as duas primeiras passaram e a terceira passou em 4 dos 5 alvos. | — |
| 2026-09-30 | — | **Nenhum conserto.** A ronda diária técnica de 30/09/2026 (14h53Z) mediu as 17 URLs no ar e achou **um** defeito novo, e ele é da lista fechada 19.2: doze dos dezessete itens de degrau 4 do banco (`glassmosaic-k2501`, `k2502`, `mix2510`, `102`, `k117`, `k77`, `k66`, `a11`, `a61`, `a37`, `ic02` e `pastilhart-af1500`) não escrevem por que pararam no degrau 4 — trazem só `motivo_da_chave`, que diz como a chave foi montada e não se o produto não está anunciado ou se os candidatos foram barrados por trava (25.4-b.4). É dado do banco, então virou o item 1 do `DESPACHO DA SENTINELA — 2026-09-30` no `PROMPT.md`. **RECONFERÊNCIA DA 19.4(c):** as quatro linhas acima foram reconferidas no ar nesta ronda — a porta de entrada de 24/09 PASSOU pela segunda ronda seguida; os links regerados de 25/09 PASSARAM; a etiqueta de robô de 25/09 **agora PASSA NOS CINCO ALVOS** (a metade que falhou em 28/09 foi conferida hoje com os nomes de campo reais da F1, `base`, `caco` e `junta`, e serve `noindex, follow` uma única vez, inclusive com valor inválido), o que **fecha o item 2 do despacho de 28/09**; e o soft 404 na borda de 29/09 **continua e foi medido também na robometria**, o que o tira do escopo desta ilha e o põe na camada do hospedeiro. Teste de vida: **21 de 21 itens com `url_produto` vivos**, 0 morto, 0 esgotado; piso 38 de 38; 10 de 10 chaves de busca com resultado; zero intestável. | — |
| 2026-10-02 | — | **Nenhum conserto.** A ronda diária técnica de 02/10/2026 (14h51Z) mediu as 17 URLs no ar e **não achou defeito novo nesta ilha**. **RECONFERÊNCIA DA 19.4(c):** as cinco linhas acima foram abertas antes de qualquer outra coisa e reconferidas no ar, com quebra de cache e `Accept-Encoding: identity`. **(1) A porta de entrada de 24/09 PASSOU pela terceira ronda seguida** — 17 de 17 em 200, `/wp-sitemap.xml` com XML de sitemap de verdade, `/robots.txt` em `text/plain`, `/wp-json/` em `application/json`, e caminho inexistente em 404 da própria ilha. **(2) Os links regerados de 25/09 PASSARAM** — 41 de 41 itens com `url_busca` encurtada e `url_busca_produto` crua, `sub_id_1 = clubedomosaico`, zero encurtador desconhecido servido nas 17. **(3) A etiqueta de robô de 25/09 PASSOU** — zero `noindex` indevido nas 17 do sitemap, e nenhuma das três âncoras que rankeiam saiu do índice. **(4) O soft 404 na borda de 29/09 CONTINUA** — sonda virgem em 404 · 200 · 200 · 200, e a mesma sonda na aquametria deu 404 nas quatro: segue sendo camada do hospedeiro e pendência do Raphael. **(5) A linha de 30/09 não tem conserto a reconferir**, e o defeito que ela despachou está **CUMPRIDO**: os 17 itens de degrau 4 escrevem `motivo_sem_ficha` na forma da 25.4-b.3, 17 de 17, com a causa separada da última tentativa pelo marcador. **Teste de vida:** 24 de 24 itens com `url_produto` vivos (20 Shopee com `item_status: normal` pela API de ficha, inclusive os três nascidos hoje; 4 Mercado Livre `/p/MLB...` com opção de compra), 0 morto, 0 esgotado; piso 41 de 41; 12 de 12 chaves de busca com resultado (46 a 5.923 ofertas); zero intestável. **E um achado de método:** User-Agent `Mozilla/5.0` pelado recebe **406** nas 17 (e nas 83 do arquipélago); com `curl/8`, com Chrome completo, com Googlebot e sem User-Agent nenhum, todas respondem 200. É firewall do hospedeiro contra agente truncado, não apagão — régua nova manda User-Agent de navegador completo. | — |
| 2026-10-05 | — | **Nenhum conserto efetivado, e UM tentado e recusado.** A ronda diária técnica de 05/10/2026 (14h55Z) escolheu esta ilha pela regra da dívida (seção 12): é a única com publicação nova desde a última ronda (`ultima_execucao` de hoje 14h05Z; sitemap de 17 para **21** URLs). Mediu as 21 no ar e achou **três** defeitos. **(1) O BANCO SABE E O SITE NÃO:** a execução de hoje fechou `junta_min_mm: 2` e `junta_max_mm: 10` do `quartzolit-rejunte-piscinas` e **não acionou o Sync** (`/status` e manifest na revisão 56; último desembarque em 02/10 19h52), então 7 das 9 células de rejunte da F2 seguem erradas no ar — a de 6 mm em `contato_permanente_agua` está **vazia** e as de 3 e 5 mm dizem ao leitor que *a gente não conseguiu a faixa de junta*, afirmação que o `main` contradiz desde hoje. É defeito da lista fechada **19.1** (`Sync não disparado`) e **eu tentei consertá-lo pela 19.3: o acionamento de `?clubedomosaico_sync=<token>&forcar=1` por curl foi RECUSADO por este ambiente de rotina, classificado como deploy em produção.** Pela 19.4(a) virou despacho — *tentei consertar em 2026-10-05, falhou: acionamento do Sync bloqueado para a rotina da Sentinela*. **(2)** `quartzolit-rejunte-acrilico` tem `degrau: 2` com `url_produto` de anúncio de vendedor comum na Shopee (`shop_id` 1462074750, a mesma loja que o registro irmão classifica como degrau 3), mais `etiqueta_ml` com `programa: shopee` e sem bloco `casamento`: pela 25.1 o degrau 2 é só a `/p/MLB...` do Mercado Livre. Dado do banco, **19.2**, despachado. **(3)** O teste de vida da 25.4 **parou de cobrir uma ronda**: `api/v4/pdp/get_pc` responde 200 com `item_status` só nos primeiros 4 a 6 chamados de cada contexto de aba e depois devolve `error: 90309999` com redirecionamento para `verify/traffic?...&scene=crawler_item`; abrir `shopee.com.br/` direto cai no `verify/captcha`. Resultado honesto: **10 de 24 itens medidos, 0 morto, 0 esgotado, 14 NÃO MEDIDOS** (6 de 20 da Shopee com `item_status: normal`; 4 de 4 do Mercado Livre `/p/MLB...` vivos com preço). Piso da 25.2: **41 de 41** com `url_busca` e `url_busca_produto`; **zero** intestável; **zero** `degrau` nulo. **RECONFERÊNCIA DA 19.4(c):** as oito entradas acima foram abertas antes de qualquer outra coisa e reconferidas no ar com quebra de cache. A **porta de entrada de 24/09 PASSOU pela quarta ronda seguida**, e a mesma medição **reconfere o reparo do `.htaccess` de hoje 10h17Z: PASSOU** — 21 de 21 em 200, sitemap com XML de verdade, `robots.txt` em `text/plain`, `/wp-json/` em `application/json`, caminho inexistente em 404 da própria ilha; pela 19.4(b) uma terceira queda vira chamado na HostGator, não terceiro reparo. Os **links regerados de 25/09 PASSARAM** (35 links servidos nas 21, todos do banco, zero encurtador desconhecido, zero link cru). A **etiqueta de robô de 25/09 PASSOU em cinco alvos, um deles novo** — `/author/artesa/`, linkado das cinco páginas de peça, serve **uma** `noindex, follow`, igual a `/author/mosaico_gestor/`, `/materiais/como-sabemos/` e `/?s=`; zero `noindex` indevido nas 21. O **soft 404 na borda de 29/09 CONTINUA** e segue sendo do Raphael. Os **cinco itens de 28/09 estão fechados**: zero `cm cm` nas 21, estados da F1 com `noindex`, `description` nas 21 e nenhuma acima de 160, zero `degrau` nulo em 41 de 41, e o `alt` de `/loja/` certo — restam só as miniaturas de 150×150 com alt vazio, duplicata decorativa da foto já rotulada, que **não** são defeito. O **item 1 de 30/09 CONTINUA cumprido** (17 de 17 no degrau 4 com motivo na forma da 25.4-b.3). **Ferramentas com entrada real e conta na mão:** F1 em `disco, d=30, p25, junta=4, sobra=15` → 707 cm², passo 2,9 cm, 1.189/m², 97 pastilhas, e os cinco números batem (π×15²=706,86; 10.000÷2,9²=1.189,1; 706,86÷8,41=84,05 ×1,15=96,66 → 97); F2 em `espelho + externo_exposto + caco_espelho + 3 mm` → Tekbond Silicone Neutro, com `espelhos` em `indicado_para` e `chuva` e `raios UV` em `resistencias_declaradas`, e o recomendado **fora** da própria lista de "o que não usar". Console sem uma mensagem, com recarga, na mãe e numa filha nova. | — |
| 2026-10-07 | — | **Nenhum conserto, e nenhum tentado — porque nenhum defeito da lista fechada 19.1 apareceu.** A ronda diária técnica de 07/10/2026 (14h5xZ) escolheu esta ilha pela regra da dívida (seção 12): é a única com publicação nova desde a última ronda (`ultima_execucao` de hoje 14h16Z, manifest e `/status` na **revisão 66**; sitemap segue em 21 URLs). Mediu as 21 no ar e **não achou defeito novo**. Mediu também a **ronda técnica inteira** na aquametria (52 URLs) e na robometria (14), pela decisão do Raphael de 28/09, e as duas passaram. **OS DOIS ITENS QUE A RONDA DE 05/10 DEIXOU PARA A FUNDAÇÃO ESTÃO FECHADOS E FORAM CONFERIDOS NO AR PELA 18.4:** (1) a revisão 66 desembarcou e a célula de `junta=6` em `contato_permanente_agua`, antes **vazia**, serve agora *"o rejunte é Rejunte Piscinas Quartzolit"* com *"Cobre junta de 2 a 10 mm"*; `junta=3` e `junta=5` nomeiam os dois rejuntes; a frase *"a gente não conseguiu a faixa de junta"* tem **zero** ocorrência nos três estados; (2) `quartzolit-rejunte-acrilico` saiu do degrau 2 para o **degrau 3**, e os 4 que ficaram no degrau 2 são todos `/p/MLB...` do Mercado Livre — degraus hoje 1 / 4 / 19 / 17. **O ÚNICO ACHADO DE HOJE É DE INSTRUMENTO E PIOROU:** o teste de vida da 25.4 parou de funcionar por inteiro — a ficha crua da Shopee é redirecionada para `verify/traffic` **na primeira leitura**, em aba nova, e `api/v4/pdp/get_pc` devolve `error: 90309999` na **primeira** chamada de cada contexto, inclusive aberta direto na barra de endereço. Três passadas, dois contextos limpos, zero leitura. Resultado honesto: **4 de 24 medidos (os 4 do Mercado Livre `/p/MLB...`, vivos com preço), 0 morto, 0 esgotado, 20 NÃO MEDIDOS**. É o item 1 do `DESPACHO DA SENTINELA — 2026-10-07`, endereçado ao Raphael. **RECONFERÊNCIA DA 19.4(c):** as nove entradas acima foram abertas antes de tudo e reconferidas no ar com quebra de cache e `Accept-Encoding: identity`. A **porta de entrada de 24/09 PASSOU pela quinta ronda seguida**, e com ela o **reparo do `.htaccess` de 05/10** — 21 de 21 em 200, `/wp-sitemap.xml` com XML de verdade, `/robots.txt` em `text/plain`, `/wp-json/` em `application/json`, caminho inexistente em 404 da própria ilha. Os **links regerados de 25/09 PASSARAM e em número maior**: **39** links de loja servidos (eram 35), todos do banco, zero cru, zero encurtador desconhecido. A **etiqueta de robô de 25/09 PASSOU nos SEIS alvos** — `/author/mosaico_gestor/`, `/author/artesa/`, `/materiais/como-sabemos/`, `/?s=`, o estado com parâmetro da F2 e o da F1 servem **uma** `noindex, follow` cada, e a URL canônica da ferramenta segue indexável; zero `noindex` indevido nas 21. O **soft 404 na borda de 29/09 CONTINUA** (404 · 200 · 200 · 200) e segue do Raphael. Os **cinco itens de 28/09 continuam fechados** e o **item 1 de 30/09 continua cumprido** (17 de 17 com `motivo_sem_ficha`). **Ferramentas com entrada real e conta na mão:** F1 em `cilindro, d=15, h=20, p20, junta=3, sobra=10, rejunte=cimenticio` → 942 cm², passo 2,3 cm, 1.890/m², 196 pastilhas, 198 g, e os cinco batem (π×15×20=942,48; 10.000÷2,3²=1.890,4; 942,48÷5,29=178,16 ×1,10=195,98 → 196; 0,0942×2,10=0,1979 kg); F2 em `espelho + externo_exposto + caco_espelho + 3 mm` → Tekbond Silicone Neutro, com a declaração citada e o recomendado fora da própria lista de "o que não usar". Console sem uma mensagem, com recarga, num estado com parâmetro da F2 e numa filha de `/materiais/acabamento/`. Piso da 25.2: **41 de 41** com `url_busca` e `url_busca_produto`; **zero** intestável; **zero** degrau nulo. | — |

## 12/09/2026 — primeira ronda desta ilha, nenhum conserto

`ultima_ronda` era `null`: a ilha nunca tinha sido rondada. Foram abertas as 11 URLs no navegador do Raphael e nenhum defeito da lista fechada 19.1 apareceu — não há, portanto, nada para a próxima ronda reconferir nesta tabela.

Os dois defeitos encontrados são de **coerência da recomendação** (seção 12) e caem na lista 19.2 (lógica de ferramenta), então a Sentinela não os consertou: eles estão em `PROMPT.md`, na seção `## DESPACHO DA SENTINELA — 12/09/2026`. O que a próxima ronda tem de reconferir é aquele despacho, no ar, pelos critérios de "pronto quando" que ele declara.

## 25/09/2026 — O QUE A PRÓXIMA RONDA RECONFERE NA LINHA DA ETIQUETA DE ROBÔ

**É um comando, e ele mede as duas direções:** `python3 ferramentas/conferir-no-ar.py .` — a seção "A etiqueta
de robô (uma só, e nas páginas certas)" cobra que `/author/`, `/materiais/como-sabemos/`, `/?s=` e os estados
com parâmetro da F1 e da F2 sirvam **UMA** etiqueta com `noindex, follow`, **e** que as 17 URLs do sitemap e as
duas âncoras que rankeiam continuem **no** índice. `noindex` indevido tira do ar uma página que rankeia, e esta
ilha tem três na primeira página — por isso as duas direções.

**O que a ronda NÃO pode usar como régua:** a aspa. O `wp_robots()` do núcleo imprime `content='noindex,
follow'` com aspas **simples**. Cinco réguas desta ilha procuravam aspas duplas e tiveram de ser consertadas
em 25/09; duas delas passavam a vazio, aprovando qualquer coisa.

## 24/09/2026 — CONSERTO DA FUNDAÇÃO, não da Sentinela, e está aqui de propósito

Esta tabela é da Sentinela pela 19.4(c). A linha acima foi escrita pela **Fundação**, e entra aqui por um motivo só: **a ronda seguinte abre esta lista antes de qualquer outra coisa**, e o que ela tem de reconferir é justamente a porta de entrada do site. O conserto está em `REGISTRO.md`, na entrada de 24/09 às 19h40Z, com o antes e o depois do arquivo.

**O que a próxima ronda reconfere, e é um comando:** `python3 ferramentas/conferir-no-ar.py .` — ele ganhou hoje a seção da porta de entrada e reprova se o sitemap, o `robots.txt` ou a raiz do REST saírem do ar, ou se um caminho inexistente passar a responder a página do hospedeiro em vez da desta ilha. Se reprovar, o diagnóstico por dentro do servidor está em `?rest_route=/clubedomosaico/v1/rotas&token=<token do Sync>`, e `&reparar=1` conserta.

**A causa de origem continua sem nome** (ver a seção 29.5 do `ARQUIPELAGO.md`). Se o defeito **voltar**, a 19.4(b) vale com força dobrada: defeito que volta não é defeito, é sintoma de causa que ninguém enxergou — e aí o caminho é chamado na HostGator sobre o `.htaccess` da raiz de `/clubedomosaico.com.br`, não mais um reparo.

## 25/09/2026 — CONSERTO DA FUNDAÇÃO (bloco 0 do despacho do Raphael de 24/09)

Também não é conserto de Sentinela, e está aqui pelo mesmo motivo da linha de 24/09: **a ronda seguinte abre esta lista antes de qualquer outra coisa.**

**O que a próxima ronda reconfere, e são dois comandos:**

1. `python3 ferramentas/conferir-no-ar.py .` — ganhou hoje a seção *"O link de afiliado servido"*: ela varre as URLs do sitemap e **reprova se aparecer encurtador de Shopee que o banco não conhece**. É o portão que pega link velho continuando na tela depois de uma regeração, que é defeito mudo — o link antigo continua **vivo** na Shopee, nada dá 404, e a ilha só perde a atribuição.
2. `SHOPEE_APP_ID=… SHOPEE_SECRET=… python3 ../../ferramentas/conferir-sub-id.py` — gera um link de **bancada** e lê a casa do sub-id no `utm_content` do 301. **Não use link desta ilha nesse teste:** o salto do encurtador é onde a Shopee conta o clique, e a leitura semanal está justamente procurando o PRIMEIRO clique orgânico desta ilha (proposta 3 do despacho de 23/09). Um autoclique com a etiqueta `clubedomosaico` apaga esse sinal. É a seção **25.8** do contrato, escrita hoje.

**O que ela NÃO consegue reconferir, e é a metade que falta:** se o Relatório de cliques da Shopee passou a mostrar `clubedomosaico-f2---` com o campo 1 preenchido. Isso só aparece quando houver um clique **de gente**, e é o que o "pronto quando" do item 2 do despacho de 23/09 pede. Até lá o que está provado é a mecânica, na bancada, e que a tela serve os links de hoje.

## 29/09/2026 — ACHADO DA FUNDAÇÃO QUE **NÃO** FOI CONSERTADO, e o motivo é que não há daqui como consertar: SOFT 404 NA BORDA

Não é conserto. Está nesta lista porque **a ronda seguinte abre esta lista antes de qualquer outra coisa**, e esta
é a linha que ela precisa ler antes de concluir que a ilha está sã pelo portão verde.

**O QUE FOI MEDIDO**, em 29/09/2026 entre 10h5xZ e 11h0xZ, repetido pela 20.2 antes de virar afirmação — cinco
leituras de uma URL, três de outra e uma URL virgem nunca lida:

| leitura de uma URL que **não existe** | resposta |
|---|---|
| **1ª** (o cache ainda não tem a entrada) | **404**, `cache-control: no-cache, must-revalidate, max-age=0, no-store, private` — a **origem**, e ela está certa |
| **2ª em diante, por 2 horas** | **200**, `x-proxy-cache: HIT`, `x-server-cache: true`, `max-age=7200` — e o corpo é a página de **404 desta ilha** |

A prova de que é mecanismo e não coincidência está numa URL virgem, criada com o relógio no nome: 1ª leitura
**404**, 2ª **200**, 3ª **200**. E as três URLs inexistentes lidas uma vez minutos antes, todas com 404 na
primeira, respondiam **200** na segunda.

**POR QUE ISTO IMPORTA, e não é zelo teórico:** 200 com corpo de erro é **soft 404**. O Google conta a URL como
existente, e quem lê uma URL duas vezes é exatamente o Googlebot. O orçamento de rastreamento é o recurso escasso
da seção 14.1 e esta ilha tem **15 URLs ainda não indexadas**. É também a mesma família do achado do BLOCO C de
25/09 — *"o rastreador nunca recebe redirecionamento"* —, com a mesma causa: **a camada de cache responde antes do
WordPress**.

**POR QUE NENHUM PORTÃO DAQUI VIA:** todos leem com `?v=<agora>`, isto é, medem a **origem**. A afirmação
`[rota] caminho inexistente responde 404` do `conferir-no-ar.py` passa, e está **certa** — a origem responde 404.
O defeito mora na camada da frente, e até hoje nada daqui a lia.

**QUEM FECHA: o Raphael, e não a Fundação.** O cache é do hospedeiro, roda **antes** do PHP, e a origem já manda
`no-store`, que ele ignora. Não há linha de código desta ilha que o alcance — snippet do Code Snippets roda dentro
do WordPress, depois da camada que está servindo a resposta. O pedido está escrito no `ESTADO.md` como pendência
dele.

**O QUE A PRÓXIMA RONDA RECONFERE, e é um comando:**

`python3 ferramentas/leitura-do-visitante.py .` — ele lê as 17 URLs do sitemap **sem quebra de cache** (a leitura
que se parece com a do Google) e termina com a sonda de 404 pela borda. Hoje ele fecha **REPROVADO por 1 defeito**,
e esse 1 defeito é este. **Ficar vermelho é a verdade, e é para ficar** até a pendência fechar.

O `conferir-no-ar.py` ganhou as mesmas medições, mas ali a linha da borda **registra e não reprova** — a
jurisprudência é desta ilha, de 14/09: portão vermelho que nenhuma execução consegue fechar "se aprende a ignorar,
que é pior do que não ter portão". **No dia em que o Raphael fechar, a linha vira portão trocando `ok(True` por
`ok(_borda_404_ok`**, e está escrito assim no próprio arquivo.

## 05/10/2026 — A PORTA DE ENTRADA CAIU DE NOVO, E PELA 19.4(b) ISSO DEIXA DE SER CONSERTO E VIRA CHAMADO

**Defeito, não sintoma:** o bloco `# BEGIN WordPress` desapareceu outra vez do `.htaccess` da raiz
(`/home3/rapha921/clubedomosaico.com.br/.htaccess`), **1.057 bytes, bloco único `NFD EPC`,
`tem_wordpress: false`, 8 linhas de reescrita** — byte por byte a mesma assinatura de 24/09/2026. Sem o bloco, o
Apache não encaminha caminho bonito para o `index.php` e o WordPress deixa de receber toda URL que não seja
arquivo em disco.

**O que estava fora do ar, medido às 10h17Z:** as **21** URLs do sitemap, `/wp-sitemap.xml`, `/robots.txt`,
`/wp-json/` e as **três páginas que estão na primeira página do Google**. Só a home respondia. O
`?rest_route=/clubedomosaico/v1/status` respondia **200** o tempo inteiro, que é a 29.1 exatamente como escrita:
todo portão desta fábrica entra pela porta que continuou aberta.

**O que foi feito:** a rota de reparo da 29.3,
`?rest_route=/clubedomosaico/v1/rotas&token=<token do Sync>&reparar=1`. O `.htaccess` foi de **1.057 para 1.580
bytes**, de **1 para 2 blocos** (`NFD EPC` + `WordPress`) e de **8 para 15 linhas** de reescrita.

**Conferido pela 19.4(a), no ar, com quebra de cache:** 21 de 21 URLs em **200**; `/wp-sitemap.xml` em 200 com
`application/xml` e XML de sitemap de verdade; `/robots.txt` em 200 e `text/plain`; `/wp-json/` em 200 e
`application/json`; e `/nunca-existiu-abc123/` em **404 na página desta ilha**. `conferir-no-ar.py`: **524
afirmações, 0 falha**. `leitura-do-visitante.py` fecha **REPROVADO pelo único defeito de 29/09** (o soft 404 na
borda), que é vermelho esperado com dono escrito e **não** é regressão desta passada.

**A JANELA, e ela é o número mais caro desta entrada: até 2 dias e 14 horas.** A última prova de vida é de
**02/10 às 19h57Z** (fecho do bloco 4c, conferido no ar) e a queda foi medida em **05/10 às 10h17Z**. Nenhuma
ronda rodou nessa janela — `ultima_ronda` estava em **02/10 14h51Z**. Não há como estreitar daqui: a Search
Console é o instrumento que diria quando o Google viu 404, e **não há credencial neste ambiente**
(`GOOGLE_SA_B64` ausente), o que por si é uma pendência.

**PELA 19.4(b) ESTE DEFEITO JÁ NÃO É PARA CONSERTAR DAQUI.** A entrada de 24/09 neste mesmo arquivo
pré-registrou o desfecho com estas palavras: *"Se o defeito voltar, a 19.4(b) vale com força dobrada (...) e aí o
caminho é chamado na HostGator sobre o `.htaccess` da raiz de `/clubedomosaico.com.br`, não mais um reparo."* É
a segunda vez, na mesma raiz, com a mesma assinatura. **O chamado é do Raphael** — a Fundação não abre conta,
não contrata e não fala com fornecedor —, e está escrito em `dados/despachos.md` na lista de ABERTOS. O reparo
desta passada foi feito porque a ilha estava fora do ar **agora** e deixá-la caída esperando chamado seria pior;
ele não substitui o chamado.

**ACHADO NOVO, e ele explica por que nenhum relógio delata esta falha:** o `.htaccess` é reescrito
**a cada requisição**. O `mtime` devolvido pela rota de diagnóstico avançou 10:23:49 → 10:24:10 → 10:24:31 em
três leituras espaçadas pelos meus próprios ~20 segundos de intervalo. Duas consequências, e as duas importam:
(1) **"mtime recente" nunca vai acusar o defeito** — o arquivo parece sempre recém-salvo, inclusive nos dias em
que está errado, então qualquer portão que pensasse em vigiar a data do arquivo estaria vigiando ruído; e
(2) o reescritor **preserva o que encontra** — o bloco do WordPress sobreviveu às três reescritas medidas depois
do reparo —, o que quer dizer que a perda **não é desgaste gradual**: é **um evento único** que todas as
reescritas seguintes copiam fielmente. Isso estreita a causa que a 29.5 declara sem nome: o que se procura é o
evento que escreveu o arquivo sem o bloco, não um processo que o corrói. Está escrito na 29.5 do
`ARQUIPELAGO.md`.

**O que a próxima ronda reconfere, e é um comando:** `python3 ferramentas/conferir-no-ar.py .` (a seção da porta
de entrada da 29.2 reprova se qualquer uma das três cair). Se reprovar **antes** de o chamado da HostGator ter
resposta, repare pela 29.3 para a ilha não ficar caída, **e escreva a terceira linha aqui** — a série é o que vai
sustentar o chamado.

---

## 08/10/2026 — A TERCEIRA QUEDA DA MESMA PORTA, REPARADA PORQUE A ILHA ESTAVA CAÍDA AGORA — E A LINHA QUE A ENTRADA DE 05/10 MANDOU ESCREVER

**Medido às 19h2xZ de 08/10/2026 pela Fundação, no começo do bloco, pelo comando que a entrada de 05/10
pré-registrou com estas palavras:** *"O que a próxima ronda reconfere, e é um comando: `python3
ferramentas/conferir-no-ar.py .`"*. Ele **REPROVOU com 349 falhas em 513 afirmações**, e a causa era uma só.

**O SINTOMA:** **20 das 21 URLs do sitemap em 404**, mais `/wp-sitemap.xml`, `/robots.txt` e `/wp-json/` — as
três da 29.2 — também em 404. Só a raiz respondia 200, porque ela é o documento raiz e não depende de reescrita.
Medido em **três passadas** com `aquametria.com.br` em 200 nas mesmas três (seção 20.2: falha de rede só vira
diagnóstico depois de repetir).

**A ASSINATURA É IDÊNTICA ÀS DUAS ANTERIORES, byte por byte**, lida pela rota da 29.3 antes de qualquer reparo:
`.htaccess` da raiz com **1.057 bytes**, **um bloco só (`NFD EPC`)**, `tem_wordpress: false`, **8 linhas de
reescrita**, arquivo existente, legível e gravável, `mod_rewrite: true`, `regras_no_banco: 115`,
`permalink_structure` inalterado (`/%year%/%monthnum%/%day%/%postname%/`, o mesmo que o `REGISTRO.md` já
registrava). **Nada no retrato é novo** — e isso é o achado desta linha: a terceira queda não trouxe sintoma
novo nenhum, o que fecha a porta para a hipótese de que as duas primeiras fossem acidente de configuração em
transição.

**O REPARO, e por que ele foi feito mesmo sendo a terceira vez:** a 29.5 escreve, com todas as letras, que *"o
reparo da 29.3 continua valendo enquanto o chamado não tiver resposta — ilha caída esperando fornecedor é pior
que ilha reparada duas vezes —, e cada reparo novo escreve uma linha na série"*. A ilha estava fora do ar
**agora**, com 21 URLs em 404 para o Google, três delas em primeira página. `&reparar=1` devolveu o antes e o
depois: **1.057 → 1.580 bytes**, **8 → 15 linhas de reescrita**, blocos `NFD EPC` → `NFD EPC` + **`WordPress`**,
`tem_wordpress` **false → true**.

**CONFERIDO NO AR DEPOIS, pela 19.4(a), e não só pelas sete URLs do diagnóstico:** duas passadas com quebra de
cache deram 200 em `/`, `/loja/`, `/materiais/`, `/wp-sitemap.xml`, `/robots.txt` e `/wp-json/`, e **404 em
caminho inexistente** — que é o 404 que tem de ser 404 da 29.2. Em seguida o `conferir-no-ar.py` inteiro passou
a **APROVADO: 524 afirmações, 0 falha**, e o `leitura-do-visitante.py` fechou **REPROVADO com EXATAMENTE 1
defeito**, o soft 404 da borda — a pendência do Raphael desde 29/09, vermelho esperado e com dono escrito. **Zero
defeito novo.**

**O QUE ESTA LINHA NÃO É:** não é solução, e não substitui o chamado. Pela **19.4(b)** — defeito que volta não é
defeito, é sintoma de causa que ninguém enxergou — **a terceira queda na mesma raiz é chamado na HostGator sobre
o `.htaccess` da raiz de `/clubedomosaico.com.br`**, e o chamado é do Raphael: a Fundação não abre conta, não
contrata e não fala com fornecedor. Ele está em `dados/despachos.md` desde 05/10 e **continua sem resposta** —
esta queda é a prova de que ele não envelheceu, ficou mais caro.

**E A METADE DO ACHADO QUE É SOBRE QUEM OLHA, outra vez, com o número desta queda:** a 29.5 escreveu em 05/10 que
*"as duas quedas têm a mesma causa de demora: ninguém rodou o comando"* — nove dias na primeira, até 2 dias e 14
horas na segunda. **Desta vez quem achou foi a própria Fundação, no começo do bloco, e não a ronda.** O
`ultima_ronda` do cabeçalho era de **07/10 20h35Z** (leitura semanal; a ronda técnica daquele dia foi às 14h55Z),
e a queda está entre aquela ronda e agora. A diferença não é que a regra passou a rodar sozinha: é que o
`PROMPT.md` desta ilha manda rodar os dois comandos **antes de qualquer bloco**, e foi essa linha, e não a ronda,
que pegou a terceira queda. **Portão que mora no caminho do trabalho roda; portão que depende de alguém lembrar,
não.**

**O que a próxima passada reconfere, e continua sendo um comando:** `python3 ferramentas/conferir-no-ar.py .`.
Se reprovar de novo **antes** de o chamado ter resposta, repare pela 29.3 e escreva a **quarta** linha aqui. A
série é o que sustenta o chamado, e ela agora tem três eventos com a mesma assinatura.
