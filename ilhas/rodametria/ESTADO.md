---
ilha: rodametria
estado: viva              # `nascendo` -> `viva` em 29/10/2026 as 12h1xZ: a ilha SERVE PAGINA. Duas URLs no wp-sitemap.xml, as duas em 200, com a casca e a F2 desembarcadas na revisao 9 e os dois portoes de ar APROVADOS. Antes deste dia a ilha tinha banco e nenhum byte que um visitante visse.
prioridade: 1
piso: abaixo              # 5 URLs publicadas contra as 40 da 21.1, e primeira_indexacao null. Quem decide este campo e a leitura semanal (21.6), nunca a Fundacao de cabeca. O teto da 21.4 tem folga: esta semana saiu UMA leva, de 3 URLs, contra o teto de 3 levas por semana.
urls_publicadas: 9        # 5 -> 9 em 30/10/2026 as 14h4xZ: as QUATRO paginas que a 16.1 nomeia (`/sobre/`, `/contato/`, `/divulgacao-de-afiliados/`, `/privacidade/`), pelo bloco 5d. CONTADO no wp-sitemap.xml no ar com quebra de cache, nao na conta de antes do desembarque. ELAS NAO MEXEM NO PISO DA 21.1 NEM GASTAM LEVA: a 21.7 tira as cinco paginas nomeadas da 16.1 do teto de 10 URLs por leva e 3 levas por semana, porque sao familia fechada e nenhuma responde a uma busca — o piso de malha segue pedindo 40 e as paginas de malha seguem 5. A DIVIDA QUE ELAS PAGAM estava medida na contagem de 30/10 as 10h3xZ: a ilha serve link de afiliado da Shopee desde 29/10 e nao tinha pagina de divulgacao de afiliados nem de privacidade.
ultima_ronda: 2026-10-30T15:10Z   # RONDA DIARIA TECNICA, a PRIMEIRA desta ilha, e ela foi FUNDA. Escrito pela Sentinela, nunca pela Fundacao (secao 2). A ilha tinha 9 URLs no ar no momento da ronda (nao 5): as quatro institucionais do bloco 5d desembarcaram no meio dela, revisao 19 as 14h40:39Z. 9 de 9 em HTTP 200, porta da 29.2 verde nas quatro, soft 404 da borda AUSENTE nesta ilha (caminho virgem em 404 nas quatro leituras), regua tecnica inteira verde, console sem uma mensagem, conta da F2 refeita na mao em cinco casos e fechando. SEIS defeitos achados e ZERO consertados, de proposito: ver dados/consertos.md e o despacho de 30/10 em PROMPT.md. Teste de vida: 9 itens testados, 9 vivos, 0 morto, 13 nao testados por orcamento do anti-robo da Shopee.
primeira_indexacao: null  # as duas primeiras URLs foram ao ar hoje; indexacao e trabalho de dias. Quem grava este campo e a leitura semanal, lendo o Search Console.
ultima_execucao: 2026-10-30T14:47Z   # BLOCO 5d ENTREGUE E CONFERIDO NO AR: as quatro paginas da 16.1, pelo snippet `rodametria-institucional` 1.0.0 (#9), SEM UMA LINHA DE CASCA — elas entram pelos filtros, e a instalacao rodou porque a ASSINATURA DO MAPA mudou (casca 1.4.0). Revisao 19 no ar as 14h40:39Z com as CINCO linhas da revisao corrente dizendo `ok` (20.4, lidas uma por uma). A pagina de privacidade nao promete: zero Set-Cookie medido, zero medidor de audiencia, e os DOIS enderecos de fora que carregam estao NOMEADOS nela. Bancada com rede: 17 portoes, 0 falha. A HORA SAIU DO `date -u` NA MESMA LINHA DE COMANDO QUE A GRAVA, nunca digitada.
executando_desde: null   # limpo as 2026-10-30T14:47Z pela propria execucao que reservou as 13h54Z e reescreveu o campo as 14h11Z (1.1). O bloco passou de 40 minutos por uma causa que NAO e de trabalho e vale registrar: metade do tempo foi espera do TURNO DO CRON. O Sync havia rodado as 14h10:04, um minuto antes do push das 14h11, e o `rodametria_30min` so vencia as ~14h40 — visitar a home e bater no wp-cron.php (409, cron em andamento) nao antecipa evento que ainda nao venceu, e nao devia.
rede: aberta em 2026-10-30   # 20.2, MEDIDA e nao herdada: rodametria.com.br em 200 nas TRES passadas as 13h5xZ, com aquametria.com.br em 200 nas MESMAS tres, e o /wp-json/rodametria/v1/status em 200 — na revisao 17 no inicio e na 19 no fecho, as duas com TODAS as linhas da revisao corrente dizendo `ok` (20.4). O soft 404 da borda do hospedeiro, registrado em 29/10, NAO foi remedido nesta passada: ele e despacho ALTA de dados/despachos.md e nao se conserta daqui.
bloqueada_por: null      # obrigatorio pela secao 2. `null` DE PROPOSITO: o que falta (gov.br para a F1, as prefeituras para a camada municipal, as tres etiquetas do Mercado Livre) trava a FABRICA e nao a ILHA, e isso se escreve no despacho, que e o canal da 12.2. Preenche-lo congelaria tambem os blocos que ja podem andar — e o proximo da fila, o 3d, nao depende de nenhum deles.
bloco_atual: |
  BLOCO 5d ENTREGUE — AS QUATRO PAGINAS QUE O SITE DEVIA A QUEM LE, E A DE PRIVACIDADE
  NAO PROMETE NADA: TUDO O QUE ELA AFIRMA FOI MEDIDO NA PAGINA SERVIDA.

  ESTE ARQUIVO CONTINUA SENDO A MEMORIA DESTA ILHA — `/areas/projeto-rodametria.md` nao existe nesta
  nuvem, e e por isso que este campo e longo.

  NO AR, 9 URLs (eram 5): `/sobre/`, `/contato/`, `/divulgacao-de-afiliados/` e `/privacidade/`,
  pelo snippet `rodametria-institucional` 1.0.0 (#9 no Code Snippets), revisao 19 as 14h40:39Z com
  as CINCO linhas da revisao corrente dizendo `ok` (20.4, lidas uma por uma).

  A CASCA NAO FOI TOCADA, e isso e o mecanismo dela funcionando: as quatro entram pelos filtros
  `rodametria_paginas` e `rodametria_instalar`, de dentro do proprio snippet delas, e a instalacao
  rodou porque a ASSINATURA DO MAPA mudou — exatamente o que a casca 1.4.0 nasceu para fazer em
  29/10. O log diz `snippet #9 criado` as 14h40 e o relato de instalacao e de 14h41:38: as paginas
  nasceram na requisicao SEGUINTE, porque na do Sync o snippet ainda nao estava carregado. Era o
  defeito que custou as tres paginas do 5b, e com a assinatura ele se conserta sozinho.

  O QUE A PAGINA DE PRIVACIDADE AFIRMA, E CADA COISA MEDIDA DO LADO DE FORA:
  zero `Set-Cookie` nas URLs no ar; zero medidor de audiencia e zero pixel (doze familias
  procuradas, esta ilha nao tem GA4); e os UNICOS dois enderecos de fora que CARREGAM junto com a
  pagina estao NOMEADOS nela — Google (`fonts.googleapis.com` e `fonts.gstatic.com`, em toda pagina)
  e Shopee (`cf.shopee.com.br`, onde ha foto). `s.shopee.com.br` e `dspace.ups.edu.ec` sao so LINK,
  e link nao faz nada ate o clique — a diferenca entre carregar e linkar e a afirmacao inteira.

  E A MEDICAO ACHOU O QUE ERA MAIS FACIL DE ESCONDER. A primeira versao da pagina dizia, como toda
  politica de privacidade de calculadora diz, que "o que voce digita nao sai do navegador". O
  formulario da F2 e `method="get"`: apertar o botao manda os quatro numeros para o ENDERECO da
  pagina, que passa pelo servidor e fica no registro de acesso do hospedeiro. A frase bonita era
  falsa na metade que importa. O que foi ao ar separa as duas coisas e nomeia os quatro campos.

  A /contato/ NAO INVENTOU UM CANAL: esta ilha nao tem caixa de e-mail, o despacho de 13/09 em
  dados/despachos.md proibe "publicar um endereco que ninguem le", e a pagina diz isso com todas as
  letras. O despacho foi reescrito hoje — eram TRES ilhas, agora sao QUATRO — e a linha que a
  Fundacao troca no dia em que a caixa existir e UMA, no JSON declarado, sem tocar em codigo.

  NENHUM NUMERO E DIGITADO: 16 moldes CONTADOS na hora de servir, das options do Sync e do mapa de
  paginas da casca. As quatro caixas, cada uma conferida por uma TERCEIRA CONTA recontada em Python
  por caminho diferente do PHP: /sobre/ 17 veiculos, /contato/ 40 anuncios lidos, /divulgacao/ 5
  itens com link, /privacidade/ 9 paginas no ar. A ultima e a melhor das quatro, porque as duas
  metades leem fontes DIFERENTES — o PHP conta o mapa da casca, o portao conta o wp-sitemap servido.

  TRES PORTOES REPROVARAM A PAGINA CERTA EM DOIS DIAS, e a terceira foi hoje:
  (1) 5c, `gerar-f2.py --conferir`, pelo selo de data; (2) `teste-institucional.py`, que procurava a
  palavra `h1` no texto da folha e achou o COMENTARIO que explica por que ela nao mexe em h1 —
  consertado para medir SELETOR, com as duas metades provadas no autoteste; (3)
  `conferir-institucional-no-ar.py`, que disse que dois itens do bloco de recusa de /sobre/ "nao
  estao no ar" quando estavam: `esc_html()` vira `&quot;` e a comparacao era contra a aspa reta.
  Nas tres a tentacao era mexer na pagina; nas tres o defeito era da regua.

  E UM PORTAO NAO REPROVAVA O QUE DEVIA: A HOME ESTAVA FORA DA 32.5 DESDE QUE NASCEU.
  32.5-c outra vez. `conferir-32-5-no-navegador.mjs` decidia "esta no molde" por
  `!!(bloco_de_compra || formulario)`, e pagina com CAIXA DE RESPOSTA e sem nada para vender caia em
  "fora do molde": a caixa era medida, impressa e NUNCA julgada contra os 700 px. A home desta ilha
  e HUB, sem bloco de compra e sem formulario — estava fora do veredito desde 29/10, e as quatro de
  hoje entrariam pela mesma porta. Paginas do molde: 3 -> 8. O teto de COMPRA passou a valer so onde
  ha o que comprar, com "nao se aplica" IMPRESSO, e pagina que serve link patrocinado FORA de um
  bloco de compra passou a ser REPROVADA — senao a isencao seria a porta dos fundos dos 1.400 px.

  MEDIDO NO AR, 390 px, Chromium de verdade, com quebra de cache: caixa de resposta a 211 px
  (/sobre/) e 244 px (as outras tres), contra o teto de 700. 8 de 8 paginas do molde aprovadas.
  PISO DE CORPO DA SECAO 8, MEDIDO NO AR e nao pela conta de antes do desembarque (o erro que a mae
  /veiculos/ quase pagou, quando a conta de antes dava 1.253): /sobre/ 4.449, /contato/ 3.674,
  /divulgacao-de-afiliados/ 4.786, /privacidade/ 5.899 caracteres.
  16.4(f) com folga: cada uma das quatro recebe link de 9 das 9 paginas no ar, contra as 2 da regra —
  elas estao no RODAPE, que a casca monta do mapa inteiro, e fora do menu de cima por ordem do VOZ.md.

  BANCADA: 17 portoes com rede, 0 falha (conferir-no-ar 445 afirmacoes nas 9 URLs;
  conferir-institucional-no-ar 210; 32-5-no-navegador 8 de 8). Sem rede: 14 portoes, 0 falha, com os
  19 casos de autoteste do portao novo, que FABRICAM o mundo de cada regra — digito plantado na
  prosa, molde orfao, promessa escondida dentro do bloco de recusa, negacao no meio da frase, numero
  literal na caixa, pagina fina.

  A 20.6 GANHOU UMA REGUA DE LEITURA, e ela nao e conserto: o campo `ultimo` do /status separa os
  TRES mundos que a 20.5 junta em dois. `ultimo` ANTIGO = o Sync nao rodou (defeito). `ultimo` DE
  AGORA com revisao atrasada = cache do GitHub (reacione). `ultimo` RECENTE MAS ANTERIOR AO PUSH =
  nem defeito nem cache: e TURNO DE CRON, e o que resolve e esperar o proximo mantendo as visitas de
  pe. Medido hoje: Sync as 14h10:04, push as 14h11, revisao entrando as 14h40:39. Gastei uma rodada
  de reacao achando que era cache, ate ler o `ultimo` e ver que ele era mais velho que meu push.

  PROXIMO PASSO DESBLOQUEADO: o BLOCO 4 — a F3 como REGRA, sem pagina. Nao depende de ninguem,
  diferente de tudo o mais que sobrou na fila: a F1 depende do gov.br (despacho ALTA), as duas
  consultas da cauda dependem de uma sessao de Chrome (despacho de 30/10 no topo do PROMPT.md), e
  scooter/moto eletrica dependem das etiquetas do Mercado Livre. O desenho e o que a ohmetria usou
  para a F1 dela com banco vazio e que esta ilha ja usou na F2: a regra nasce medindo quantos
  registros declaram `carga_max_kg` e dizendo na propria tela o que falta, em vez de esperar o dado.
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
