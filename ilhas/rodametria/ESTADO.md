---
ilha: rodametria
estado: viva              # `nascendo` -> `viva` em 29/10/2026 as 12h1xZ: a ilha SERVE PAGINA. Duas URLs no wp-sitemap.xml, as duas em 200, com a casca e a F2 desembarcadas na revisao 9 e os dois portoes de ar APROVADOS. Antes deste dia a ilha tinha banco e nenhum byte que um visitante visse.
prioridade: 1
piso: abaixo              # 5 URLs publicadas contra as 40 da 21.1, e primeira_indexacao null. Quem decide este campo e a leitura semanal (21.6), nunca a Fundacao de cabeca. O teto da 21.4 tem folga: esta semana saiu UMA leva, de 3 URLs, contra o teto de 3 levas por semana.
urls_publicadas: 9        # 5 -> 9 em 30/10/2026 as 14h4xZ: as QUATRO paginas que a 16.1 nomeia (`/sobre/`, `/contato/`, `/divulgacao-de-afiliados/`, `/privacidade/`), pelo bloco 5d. CONTADO no wp-sitemap.xml no ar com quebra de cache, nao na conta de antes do desembarque. ELAS NAO MEXEM NO PISO DA 21.1 NEM GASTAM LEVA: a 21.7 tira as cinco paginas nomeadas da 16.1 do teto de 10 URLs por leva e 3 levas por semana, porque sao familia fechada e nenhuma responde a uma busca — o piso de malha segue pedindo 40 e as paginas de malha seguem 5. A DIVIDA QUE ELAS PAGAM estava medida na contagem de 30/10 as 10h3xZ: a ilha serve link de afiliado da Shopee desde 29/10 e nao tinha pagina de divulgacao de afiliados nem de privacidade.
ultima_ronda: 2026-10-30T15:10Z   # RONDA DIARIA TECNICA, a PRIMEIRA desta ilha, e ela foi FUNDA. Escrito pela Sentinela, nunca pela Fundacao (secao 2). A ilha tinha 9 URLs no ar no momento da ronda (nao 5): as quatro institucionais do bloco 5d desembarcaram no meio dela, revisao 19 as 14h40:39Z. 9 de 9 em HTTP 200, porta da 29.2 verde nas quatro, soft 404 da borda AUSENTE nesta ilha (caminho virgem em 404 nas quatro leituras), regua tecnica inteira verde, console sem uma mensagem, conta da F2 refeita na mao em cinco casos e fechando. SEIS defeitos achados e ZERO consertados, de proposito: ver dados/consertos.md e o despacho de 30/10 em PROMPT.md. Teste de vida: 9 itens testados, 9 vivos, 0 morto, 13 nao testados por orcamento do anti-robo da Shopee.
primeira_indexacao: null  # as duas primeiras URLs foram ao ar hoje; indexacao e trabalho de dias. Quem grava este campo e a leitura semanal, lendo o Search Console.
ultima_execucao: 2026-10-30T19:44Z   # A ESCADA DA 25.2 CHEGA A TELA NAS DUAS PONTAS — o bloco PRE-REGISTRADO pelo fecho das 18h13Z. Conferido NO AR (18.4): revisao 27, as 7 linhas da revisao corrente dizendo `ok` (20.4, lidas uma por uma), portao novo da vitrine em 191 afirmacoes / 0 falha, 32.5 em 8 de 8 com o primeiro botao de compra IDENTICO ao de antes, e bancada com rede em 21 portoes / 0 falha. A HORA SAIU DO `date -u` NA MESMA LINHA DE COMANDO QUE A GRAVA, nunca digitada.
executando_desde: null   # LIMPO as 2026-10-30T19:44Z pela propria execucao que reservou as 19h17Z e renovou as 19h29Z (1.1). O bloco passou de 40 minutos pela MESMA causa de 30/10 as 18h13Z e por mais nada: UM turno de cron. O Sync desta ilha roda por VISITA (20.6) e nao antecipa evento que ainda nao venceu — push as 19h29Z, `ultimo` do /status em 19:17:02 (recente e ANTERIOR ao push, que e turno de cron e nem defeito nem cache), revisao pousada as 19h41:02Z no turno seguinte, com as visitas de pe.
rede: aberta em 2026-10-30   # 20.2, MEDIDA e nao herdada nesta execucao: rodametria.com.br/, /wp-sitemap.xml e /wp-json/rodametria/v1/status os TRES em 200, com aquametria.com.br em 200 na mesma passada. O soft 404 da borda do hospedeiro, de 29/10, NAO foi remedido aqui: e despacho ALTA de dados/despachos.md e nao se conserta daqui.
bloqueada_por: null      # obrigatorio pela secao 2. `null` DE PROPOSITO: o que falta (gov.br para a F1, as prefeituras para a camada municipal, as tres etiquetas do Mercado Livre) trava a FABRICA e nao a ILHA, e isso se escreve no despacho, que e o canal da 12.2. Preenche-lo congelaria tambem os blocos que ja podem andar — e o proximo da fila, o 3d, nao depende de nenhum deles.
bloco_atual: |
  A ESCADA DA 25.2 CHEGOU A TELA NAS DUAS PONTAS. Era o bloco PRE-REGISTRADO pelo
  fecho das 18h13Z, e nao um despacho — nada estava quebrado no ar.

  ESTE ARQUIVO CONTINUA SENDO A MEMORIA DESTA ILHA — `/areas/projeto-rodametria.md`
  nao existe nesta nuvem, e e por isso que este campo e longo.

  O DEFEITO NUNCA APARECEU NUMA PAGINA, E ISSO E O ACHADO. A 25.2 manda a BUSCA
  SUBIR E VIRAR O BOTAO quando a ficha nao existe ou morre. So a primeira ponta
  estava na tela: o cartao da casca devolvia STRING VAZIA com `url` vazia, e a
  segunda ponta vivia no CHAMADOR da F2. A F2 nunca sofreu; a VITRINE de produto,
  que passa `url` crua do dado, tinha TRES lugares lendo-a crua, e os tres
  quebravam juntos no dia em que uma ficha morresse: o CARTAO sumia da pagina, a
  celula "Comprar" da tabela servia `href=""` — que nao e botao morto, e um botao
  que RECARREGA A PROPRIA PAGINA com "Ver na Shopee" do lado, pior que o cartao
  que ao menos sumia — e a `Offer` do JSON-LD saia com `"url": ""`.
  POR QUE NADA VIU: 21 de 21 anuncios da vitrine tem ficha. O ramo NAO EXISTE no
  dado publicado, e regua que le o dado publicado aprova o mundo que existe. E a
  32.5-d inteira, e a saida e a da ohmetria: so a mutacao que PRODUZ o mundo o
  enxerga.

  O CONSERTO E MECANISMO E NAO INTENCAO: a escada virou UMA funcao da casca,
  `rodametria_casca_escada_de_compra()`, e todo chamador entrega os DOIS links
  crus. A F2 parou de escolher, entao a regra deixou de morar em dois lugares onde
  podia divergir — a 32.5-c nasceu exatamente da metade que nao viajou. E O DEGRAU
  SOBE COM A BUSCA, que e a metade que mente se ficar para tras: botao que abre
  PAGINA DE BUSCA dizendo "Ver na Shopee" promete ficha que nao existe mais.
  Medido no ar: o bloco de compra da F2 serve degraus [1, 4], entao os itens do
  mundo B passam pela escada nova EM PRODUCAO.

  A TABELA GANHOU A LINHA DISCRETA DO PISO, UMA vez embaixo dela e nao por linha:
  o piso e da CONSULTA e nao do anuncio (uma `url_busca` distinta por pagina,
  medido nas duas), e repeti-la seria o mesmo link dezesseis vezes. Com duas
  buscas distintas a linha NAO sai — "a primeira" e arbitraria. No JSON-LD,
  `availability: InStock` sai de cena quando o piso sobe: estoque de resultado de
  busca e afirmacao sem medicao.

  PORTOES: 21 na bancada com rede (eram 20), 0 falha. DOIS novos.
  `teste-escada-de-compra.php` e PHP porque a escolha e decidida em PHP, entao
  CHAMA a funcao em vez de ler o arquivo: 138 afirmacoes, FABRICA os seis mundos
  que o dado nao tem, prova que morde reproduzindo a escada velha, e COBRA a
  promessa que eu escrevi no comentario da F2 comparando item a item com a regra
  velha (10 itens, 4 ja no mundo B, identicos). Tres mutacoes no codigo de verdade
  reprovadas: 13, 6 e 2 falhas.
  `conferir-produto-no-ar.py` nasceu porque as paginas de VITRINE nao tinham
  portao de ar NENHUM desde 29/10 — o portao de PIXEL da 32.5 e o
  `mutacoes-produto.py` sem rede, e entre os dois faltava quem lesse a pagina. 191
  afirmacoes, descobrindo as URLs no sitemap no ar. RODADO CONTRA A REVISAO 23
  ANTES DO DESEMBARQUE: 2 falhas, as duas a linha do piso que estava subindo.

  AS TRES COISAS QUE O PORTAO NOVO ACHOU DO LADO DA REGUA, pagas antes de aprovar:
  (1) a linha do piso se conta pela CLASSE e nunca pela frase — a MESMA frase e a
      linha discreta de cada cartao do carrossel, 5x numa pagina sa;
  (2) `&quot;`, porque um titulo tem `10"` — mesma pedra do portao institucional;
  (3) O WORDPRESS TEXTURIZA O HIFEN, e isto vale guardar: o `wptexturize` do
      `the_content` troca hifen CERCADO DE ESPACOS por EN DASH no retorno do
      shortcode. O dado diz `550W - 40km/h`, o corpo serve `550W &#8211; 40km/h`,
      e o JSON-LD — que sai no `wp_head` e nao passa pelo filtro — serve o hifen
      cru: O MESMO NOME EM DUAS FORMAS NA MESMA PAGINA. Nao e defeito a consertar,
      e tipografia do WordPress. E a cicatriz que esta ilha ja tinha escrita no
      topo da casca ("troca && por &#038;&#038; no retorno do shortcode") num
      traje novo, e quem nao a souber escreve regua que reprova a pagina certa.

  UM ACHADO FORA DO ESCOPO, corrigido como PROSA e nao como mecanismo: o
  comentario da vitrine afirmava que `atualizar-manifest.py` casa a constante de
  versao com um campo `versao` do manifest. NAO CASA — a palavra nao aparece uma
  vez naquela ferramenta e os itens de `snippets` nao tem o campo, conferido nos
  quatro. `RODAMETRIA_PRODUTO_VERSAO` e `RODAMETRIA_F2_VERSAO` sao LIDAS POR
  NINGUEM; so a da casca e viva, porque e o gatilho de reinstalacao dela. E a
  familia do `height:44px` morto da 32.5-d: comentario que declara mecanismo
  parece conferido e nao mede nada.

  O PROXIMO PASSO DESBLOQUEADO, e sao TRES em ordem de valor:
  (1) `/veiculos/` ESTA FORA DO MOLDE, e o portao de pixel o diz com essas
      palavras ("sem componente de molde nenhum") nas duas passadas de hoje. A mae
      serve `<p class="rdm-promessa">` onde o molde pede a CAIXA DE RESPOSTA,
      entao os 700 px da 32.5 NUNCA A JULGARAM. E exatamente a lacuna que o 5d
      fechou na home, uma pagina depois — a 32.5-c em estado puro. E BLOCO e nao
      conserto: a pagina nao esta quebrada, ela esta NAO MEDIDA.
  (2) O CAMPO `versao` NO `manifest.json`, para a constante de cada snippet ser
      espelhada e IMPRESSA como o `sha256` ja e. Mexe no CONTRATO DO SYNC, que e o
      unico canal desta ilha — entao e bloco com desembarque proprio, nunca
      carona. Foi por isso que nao entrou hoje.
  (3) A FILA NORMAL segue no bloco 4, com a F1 e a F3 travadas por ABERTURA e nao
      por coleta: `gov.br` para o limiar legal da F1 e o nivel 5 (`casasbahia`,
      `extra`, `magazineluiza`) para `carga_max_kg` da F3 — os dois despacho ALTA
      em dados/despachos.md.

  E A ROBOMETRIA SEGUE FORA DO AR com despacho ALTA, remedida nesta passada: home
  em 200 e os tres endpoints em 404. Nao e consertavel do repositorio — o gesto e
  de cPanel e e do Raphael.
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
