---
ilha: rodametria
estado: nascendo
prioridade: 1
piso: abaixo
ultima_ronda: 2026-10-28T20:00Z   # LEITURA SEMANAL. Primeiro campo ultima_ronda desta ilha, pela secao 2. Nao houve ronda tecnica: a ilha tem zero pagina publicada e o egresso da nuvem para rodametria.com.br esta recusado (403 do proxy, medido duas vezes as 19h5xZ). Despacho de 4 itens no PROMPT.md, com a conta da 31.6: 0 de 5.
primeira_indexacao: null
ultima_execucao: 2026-10-28T19:33Z   # BLOCO DO PISO DE COMPRA ENTREGUE: o banco tem os PRIMEIROS `publicavel` da historia desta ilha, 5 de 17 — `escada_de_compra` no esquema (versao 2), `coletar-piso-de-compra.py` e `mutacoes-piso.py`. O ACHADO E UMA INTERSECAO VAZIA: dos 4 veiculos publicaveis, ZERO declara tensao+amperagem e ZERO declara carga maxima — o piso e o dado tecnico cairam em registros DIFERENTES. A HORA SAIU DO `date -u` NA MESMA LINHA DE COMANDO QUE A GRAVA, nunca digitada.
executando_desde: null   # limpo as 2026-10-28T19:33Z pela propria execucao que reservou as 19h16Z de 28/10 (commit e34d578). Reserva NAO renovada pela 1.1: entre a reserva e o primeiro commit de trabalho nao passaram 40 minutos.
bloco_atual: |
  O PISO DE COMPRA EXISTE, E COM ELE O BANCO TEM OS PRIMEIROS `publicavel` DESTA ILHA: 5 de 17
  registros nao excluidos (4 veiculos e a camara Kenda), de ZERO. `esquema-banco.json` na versao 2
  com a secao `escada_de_compra` — o termo de contexto por `tipo_comercial` e por `tipo`, a escada
  de palavra-chave de quatro degraus (tres na peca), o que NUNCA compoe chave (termo sozinho, marca
  sozinha, modelo sozinho, titulo inteiro) e o porque de `sub_id_2` nascer null no piso de registro.
  Entraram `ferramentas/coletar-piso-de-compra.py` (mede, encurta, grava; `--conferir` sem rede) e
  `ferramentas/mutacoes-piso.py`. O `validar-banco.py` NAO precisou de linha nenhuma para cobrar a
  25.2 e a 25.2-b: o portao do bloco 3 estava certo e esperando dado.
  POR QUE ESTE BLOCO E NAO A CASCA, e a divergencia e decisao e nao esquecimento: a 25.2 manda o
  piso ANTES DE QUALQUER OUTRA COISA, e a 32.1 poe o BLOCO DE COMPRA na primeira tela de toda pagina
  de ferramenta, com a 32.5 reprovando quem nao tem botao antes de 1.400 px. Com zero publicavel a
  casca nao estava em segundo lugar: estava IMPOSSIVEL.
  A CHAVE E MEDIDA, NUNCA SUPOSTA: cada degrau da escada e consultado em `productOfferV2` antes de
  virar piso, e o numero volta gravado em `ofertas_na_medicao` com `medido_em`. Chave com ZERO
  oferta nao vira piso — botao que leva a busca vazia e o beco sem saida que o piso existe para
  impedir. Dos 12 sem piso: 7 nao compoem chave nenhuma (o anuncio empacota tres nomes no titulo,
  `tipo_comercial` fica honestamente em `nao_declarado` e sem marca E modelo nao ha o que compor —
  e a 25.9 outra vez, num campo novo) e 5 percorreram a escada inteira com ZERO oferta em todos os
  degraus (MAXSHOT V1, MAXSHOT V1SPRO, PLAYBIK, Honeywhale H3, Haixia). Os degraus medidos ficaram
  gravados um por um, no formato CAUSA || ULTIMA TENTATIVA da 25.4-b.3.
  O `sub_id` SAIU CERTO POR CONSTRUCAO E A PROVA NAO GASTOU UM CLIQUE DESTA ILHA: pela 25.8 o salto
  do encurtador e onde a Shopee CONTA o clique, entao os cinco links da ilha NAO foram abertos. O
  mecanismo foi provado uma vez com `ferramentas/conferir-sub-id.py` e sub-id de BANCADA — 301, com
  o utm_content trazendo 'bancada' no campo 1, 't0' no campo 2 e os campos 3 a 5 vazios —, e os
  links da ilha saem da MESMA funcao. (A frase acima nasceu colando os cinco campos com hifen, como
  o 301 os devolve, e TRES HIFENS SEGUIDOS cortam este cabecalho ao meio: a regua da secao 2 le o
  YAML partindo o arquivo no marcador de tres hifens, e ela perdeu `ultima_ronda` e `bloqueada_por`
  na primeira rodada. E a
  mesma familia das aspas duplas de 13/09/2026 na clubedomosaico, e foi a propria regua que a pegou
  antes do commit.)
  O ACHADO DO BLOCO, E ELE VALE MAIS QUE OS CINCO LINKS: O PISO E O DADO TECNICO CAIRAM EM REGISTROS
  DIFERENTES, E A INTERSECAO E VAZIA. Dos 4 veiculos publicaveis, ZERO declara tensao+amperagem
  (entrada da F2) e ZERO declara carga maxima (entrada da F3); os 2 com Wh derivado e os 3 com carga
  maxima estao TODOS entre os 12 sem saida de compra. Sao duas populacoes de anuncio: o que nomeia
  marca e modelo e achavel na loja e nao publica ficha; o que publica '60 V 20 Ah' empacota tres
  nomes no titulo e nao e achavel por nome nenhum. CONSEQUENCIA: o bloco de compra da 32.1 pede o
  produto QUE A FERRAMENTA ESCOLHEU, e hoje NENHUMA DAS TRES escolhe um publicavel. Isto virou AVISO
  DO VALIDADOR, para quem abrir o banco ler antes de desenhar a casca.
  OS DOIS DEFEITOS QUE A PASSADA ACHOU EM SI MESMA, os dois por portao e nenhum por leitura: (1) o
  degrau com NOME MENTIROSO — `_juntar()` filtrava parte vazia, entao `marca_modelo_termo` de um
  registro sem modelo compunha `marca_termo` e era gravado com o nome errado; procedencia que mente
  e pior que procedencia ausente. (2) a coleta PULAVA o registro `excluido_do_banco` e a conferencia
  NAO — o portao reprovou banco CERTO, que a 32.5-b ja nomeou como o caminho mais curto para alguem
  passar a ignorar um portao. Os dois fechados antes do commit, com caso de bateria cada um.
  BANCADA 0 FALHA, 5 portoes e dois nasceram hoje: validar-banco APROVADO (4 avisos),
  mutacoes-banco APROVADO com os 66 casos intactos, mutacoes-piso APROVADO (18 casos — 3 mundos que
  passam, 11 quebras, 4 MORTES DO ESQUEMA — mais 10 afirmacoes de composicao e o autoteste),
  coletar-piso-de-compra --conferir APROVADO, derivar-banco --conferir APROVADO. A bancada DESCOBRIU
  os dois portoes novos pela convencao de nome, sem ninguem os listar.
  NADA FOI AO AR E NADA PODIA: zero pagina existe nesta ilha, o manifest segue na revisao 1 com os
  tres grupos vazios e `publicar` segue false nos arquivos de dados — eles alimentam ferramenta, nao
  sao pagina.
  PROXIMO PASSO: o CASAMENTO do registro com a oferta da Shopee, degraus 1 a 3 da 25.1, e ele vem
  ANTES da casca. Resolve tres coisas de uma vez — `url_produto` (e com ela o teste de vida da
  25.4-b passa a EXISTIR nesta ilha), a FOTO que o cartao da 32.1 pede, e o caminho para a ficha
  onde o campo tecnico mora. Leia a 25.7 (as cinco armadilhas de casamento) e a 25.9 antes de
  escrever uma linha. Alvo apertado, saindo da medicao de hoje: os 7 que nao compoem chave e os 5
  que a loja nao respondeu.
ultima_ronda: null
bloqueada_por: null
rede: ok em 2026-10-28   # 20.2 REMEDIDA as 19h1xZ por esta execucao, nao herdada do campo: rodametria.com.br e www.rodametria.com.br em 200, com aquametria.com.br e robometria.com.br em 200 na mesma passada. NOVO HOJE, e medido pela 20.3 porque este bloco escreveu a regra que exige a fonte: o EGRESSO DA SHOPEE ESTA ABERTO para esta ilha — open-api.affiliate.shopee.com.br em 200, shopee.com.br em 200, s.shopee.com.br em 307. Nenhuma execucao desta ilha tinha medido isso. SEGUE RECUSADO o dominio .gov.br (os cinco hosts oficiais do despacho ALTA e os quatro de prefeitura, medidos em 28/10 as 16h3xZ) e seguem em ENOTFOUND dspace.ups.edu.ec e stdjet.scienceandtechnology.com.vn | CANAL DE DESEMBARQUE SAO (20.5): /status em revisao 1 igual ao manifest, `ultimo` as 18:40:29, ZERO linha de FALHA depois das 13h40 — e nada foi ao ar nesta execucao, porque esta ilha ainda nao tem pagina.
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
  revisão **1** (igual ao `manifest.json`), `ultimo` às 18:40:29 de 28/10 e zero FALHA depois das 13h40: o cron de
  30 minutos está vivo e o canal está são (20.5). *(Esta linha dizia "Pendente — devolve 404" até 28/10 às 19h3xZ,
  e já estava errada desde as 11h48Z do mesmo dia: é a seção 4 em ação, o site anda e o cabeçalho fica para trás.)*
- Lista de Domínios permitidos (seção 20): **FEITO para o domínio da ilha** — o egresso desta nuvem alcança
  `rodametria.com.br`. **E FEITO TAMBÉM PARA A SHOPEE**, medido em 28/10 às 19h1xZ pela 20.3:
  `open-api.affiliate.shopee.com.br` em 200, `shopee.com.br` em 200, `s.shopee.com.br` em 307 — é o que tornou o
  piso de compra possível nesta ilha, e nenhuma execução dela tinha medido isso. **Falta `gov.br`**, que é a fonte
  da F1: despacho ALTA de 28/10 em `dados/despachos.md`.

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

## O que está travando
- **A CASCA (bloco 3b) não é o próximo passo, e isto foi MEDIDO em 28/10 às 19h3xZ.** O piso e o dado técnico
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
