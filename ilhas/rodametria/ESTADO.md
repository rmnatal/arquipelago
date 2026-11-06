---
ilha: rodametria
estado: viva              # `nascendo` -> `viva` em 29/10/2026 as 12h1xZ: a ilha SERVE PAGINA. Duas URLs no wp-sitemap.xml, as duas em 200, com a casca e a F2 desembarcadas na revisao 9 e os dois portoes de ar APROVADOS. Antes deste dia a ilha tinha banco e nenhum byte que um visitante visse.
prioridade: 1
piso: abaixo              # 10 URLs publicadas contra as 40 da 21.1, e primeira_indexacao null. O NUMERO DESTE COMENTARIO ESTAVA VENCIDO: dizia 5, de 30/10, e a ilha passou por 9 e chegou a 10 em 06/11 — numero velho lido como fato e o defeito que a secao 4 nomeia. O VALOR do campo nao mudou e nao e meu de mudar. Quem decide este campo e a leitura semanal (21.6), nunca a Fundacao de cabeca. O teto da 21.4 tem folga: esta semana saiu UMA leva, de 3 URLs, contra o teto de 3 levas por semana.
urls_publicadas: 10       # 9 -> 10 em 06/11/2026 as 14h4xZ: a F3, `/peso-maximo-patinete-eletrico/`, pelo bloco 4c. CONTADO no wp-sitemap.xml no ar com quebra de cache, sub-sitemap por sub-sitemap, e nao na conta de antes do desembarque. ELA MEXE NO PISO E GASTA LEVA, ao contrario das quatro da 16.1 que a 21.7 isenta: e pagina de MALHA e responde a uma busca medida (a consulta do eixo C do corpus, `patinete eletrico peso maximo suportado`). Piso da 21.1 pede 40 — faltam 30. Teto da 21.4: LEVA 1 de 3 desta semana (a semana virou em 02/11; a F1 foi ao ar hoje de manha e NAO gastou leva, porque e a home e nenhuma URL nasceu).
ultima_ronda: 2026-11-06T15:01Z   # RONDA DIARIA TECNICA de 2026-11-06, 14h4xZ-15h0xZ, medida na revisao 60. Cinco defeitos, ZERO consertos (nenhum e da lista 19.1): despacho no PROMPT.md. A porta de entrada que caiu em 05/11 esta REPARADA — 10 de 10 URLs em 200 em duas leituras com quebra de cache, as tres portas da 29.2 verdes e o sitemap servindo XML de verdade.
primeira_indexacao: null  # as duas primeiras URLs foram ao ar hoje; indexacao e trabalho de dias. Quem grava este campo e a leitura semanal, lendo o Search Console.
ultima_execucao: 2026-11-06T14:45Z   # AS TRES FERRAMENTAS DA ILHA ESTAO NO AR: a F3 desembarcou na revisao 60, com o fecho do log declarando 10 aplicados e as 10 linhas de item dizendo `ok` (20.4, lidas do fecho para baixo pela 20.8). Bancada com rede em 38 portoes e 0 falha; portao de ar em 547 afirmacoes e 0 falha; 32.5 em 10 de 10 paginas, com as disputas de especificidade LATENTES caindo de 3 para 0. SETE defeitos achados, TRES deles no ar na home desde a manha. A HORA SAIU DO `date -u` NA MESMA LINHA DE COMANDO QUE A GRAVA, nunca digitada.
executando_desde: 2026-11-06T16:17Z   # RESERVA desta execucao, escrita ANTES do trabalho (passo 5 da secao 1). A hora saiu do `date -u` na MESMA linha de comando que a grava, nunca digitada. Renovo este campo pela 1.1 se a passada passar de 40 minutos.
rede: aberta em 2026-11-06   # 20.2, MEDIDA e nao herdada ANTES da reserva: rodametria.com.br em 200 nas TRES passadas, com aquametria.com.br e robometria.com.br em 200 nas MESMAS tres — 12 de 12 verdes (o `www` em 301, que e o redirecionamento normal). A PAREDE DO `.gov.br` SEGUE DE PE e NAO foi remedida de proposito (medida em 05/11 as 19h1xZ). E A FICHA DA SHOPEE FOI MEDIDA E FECHADA COMO FONTE DE NIVEL 5 em 06/11: 200 nas tres passadas e casca de SPA VAZIA, 155.908 bytes com ZERO ocorrencia de `Potencia`, `500W`, `km/h`, `Velocidade`, `Marca`, `Peso` ou do nome do produto, e nem `<title>`.
bloqueada_por: null      # obrigatorio pela secao 2. `null` DE PROPOSITO: o que falta (gov.br para a F1, as prefeituras para a camada municipal, as tres etiquetas do Mercado Livre) trava a FABRICA e nao a ILHA, e isso se escreve no despacho, que e o canal da 12.2. Preenche-lo congelaria tambem os blocos que ja podem andar.
bloco_atual: |
  AS TRES FERRAMENTAS QUE ESTA ILHA EXISTE PARA TER ESTAO NO AR. A F3 —
  "aguenta o meu peso?" — desembarcou em 06/11/2026, na mesma tarde em que a F1
  foi ao ar pela manha. A F2 esta no ar desde 29/10.

  ESTE ARQUIVO CONTINUA SENDO A MEMORIA DESTA ILHA — `/areas/projeto-rodametria.md`
  nao existe nesta nuvem, e e por isso que este campo e longo.

  PRIMEIRO COMANDO DE QUEM PEGAR ESTA ILHA: `python3 ferramentas/bancada.py --no-ar`.
  A bancada tem 34 portoes sem rede e 38 com rede.

  O QUE FAZ A F3 DIFERENTE DAS DUAS IRMAS, e e o que a tornou publicavel com o
  banco de hoje: A RESPOSTA PRINCIPAL DELA NAO DEPENDE DO BANCO. Dado o peso de
  quem pilota e o que ele carrega, a carga maxima a procurar sai de
  `total x (1 + margem)` — aritmetica sobre a entrada da pessoa mais UMA
  constante desta ilha. A vitrine e a segunda camada, e hoje esta VAZIA com a
  causa nomeada: os TRES registros que declaram `carga_max_kg` declaram 120 kg,
  os tres lidos em ficha de varejo grande, e NENHUM tem oferta aberta.

  A TABELA PRE-RENDERIZADA PUBLICA A TESE DA ILHA: com a folga de 10%, 109 kg e
  o ultimo peso total que os 120 kg do teto de varejo acolhem, e 110 kg ja nao.
  A constante previa isso POR ESCRITO em 28/10, e agora o numero esta na tela.

  O QUE ESTA EXECUCAO ENTREGOU, em uma linha cada:
  - o BLOCO 4c: `regras/f3.py`, `dados/f3-respostas.json`,
    `ferramentas/gerar-f3.py`, `ferramentas/teste-f3.py` (640 afirmacoes) e
    `snippets/rodametria-f3.php`, em `/peso-maximo-patinete-eletrico/`.
  - a 32.1-b VIAJANDO PARA A IRMA, pela 18.5. A regra nasceu nesta manha com a
    F1 e a primeira ponta do portao nasceu DENTRO de `teste-f1-arvore.mjs`,
    medindo so a F1 — por isso a divida da F2 (cinco campos nus e zero
    `<noscript>`, no ar desde 29/10) era invisivel.
    `ferramentas/teste-formulario-da-ilha.py` e a ponta SEM LISTA.
  - SETE defeitos, e tres deles estavam NO AR na home desde a manha.

  A LICAO DE METODO, E ELA VALE MAIS QUE QUALQUER DAS REGUAS: QUATRO reguas
  desta execucao reprovaram o texto ou o codigo CERTO (1, 5, 5 e 90 falsos
  positivos), e as quatro pela mesma causa — foram escritas ANTES de medir o que
  reprovariam. A quinta, a de paragrafo duplicado, foi medida nas 10 URLs antes
  de entrar: achou 3 duplicatas reais e ZERO falso positivo. REGUA SE MEDE
  CONTRA O REPOSITORIO ANTES DE ENTRAR.

  E O OUTRO EIXO: SEIS VEZES A 32.5-c nesta passada. Regra que existia e nao
  viajou — o prefixo e o `<noscript>` da 32.1-b, o seletor `.rdm-f1-noscript`, a
  guarda de `function_exists` (que o `rodametria-produto` fazia certo desde
  29/10), a maquinaria de `FONTE_NA_TELA`, e a licao do bloco de compra que
  dizia a mesma coisa tres vezes. Nenhuma era desconhecida: as seis estavam
  escritas e nenhuma morava num lugar que OBRIGASSE a proxima ferramenta a
  obedece-las. O conserto das seis foi o mesmo — mover para a CASCA ou para um
  portao que varre SEM LISTA.

  O PROXIMO PASSO DESBLOQUEADO, E ELE E DE DOIS MINUTOS DE NAVEGADOR E NAO DE
  BLOCO: a secao 6 de `dados/fonte-oficial-f1.md` esta PRONTA e VAZIA, no mesmo
  formato da 5, para a leitura do CTB aterrissar. Preenchida, a execucao
  seguinte copia os valores para `exigencia-de-habilitacao-por-categoria-ctb`,
  troca o status, e A F1 PASSA A RESPONDER A PERGUNTA DO TITULO DELA — sem uma
  linha de logica mudar. O mecanismo foi exercitado em 06/11 com o limiar.

  O PROXIMO PASSO DE CONSTRUCAO, se nao houver despacho: a MALHA. As tres
  ferramentas estao no ar e a ilha tem 10 URLs contra as 40 do piso da 21.1,
  com `primeira_indexacao: null`. O que NAO e o caminho: pagina de produto pela
  cauda (a 30.8 trava, e as caudas medidas estao `tomada` ou `nao-medida`) e
  coleta de campo tecnico (nivel 5 fechado — ver "O que esta travando").

  O QUE NAO REMEDIR: a parede do `.gov.br` (medida em 05/11), a porta da busca
  para a F1 (medida e descartada em 05/11), e a FICHA DA SHOPEE como fonte de
  nivel 5 (medida em 06/11: 200 nas tres passadas e casca de SPA vazia, 155.908
  bytes com ZERO ocorrencia de `Potencia`, `500W`, `km/h`, `Velocidade`,
  `Marca`, `Peso` ou do nome do produto, e nem `<title>`).

  O QUE AINDA NAO TEM PORTAO, e e decisao e nao lacuna: a ponta do
  COMPORTAMENTO. Nenhuma regua desta ilha APERTA um controle da ferramenta — o
  portao de ar le o HTML servido (e aperta o BOTAO de cada formulario, exigindo
  200) e o de pixel abre a pagina e mede. A F1 foi exercitada a mao no navegador
  em 06/11 (4 casos, 0 erro de JavaScript); A F3 NAO FOI. A receita esta no
  REGISTRO.md de 06/11: `createRequire` e nao `import from 'playwright'`, e o
  caminho do Chromium DESCOBERTO em `/opt/pw-browsers` em vez de fixo.
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
  revisão **29**, medida em 02/11/2026 às 17h4xZ, com as **8 linhas da revisão corrente** no log dizendo `ok` uma
  por uma e conferidas contra o `8 aplicado(s)` que a própria linha de fecho declara (20.4, lidas pelo portão).
  **O cron é o ÚNICO caminho de desembarque desta ilha:** o token do Sync não está no repositório e não deve estar.
  **MAS ELE NÃO RODA POR RELÓGIO, RODA POR VISITA (20.6)** — a frase antiga desta linha, *"a Fundação não aciona o
  Sync aqui, ela empurra e espera"*, está **certa sobre o token e errada sobre o relógio**, e foi medida errada em
  29/10: depois de empurrar, a execução **abre a própria página** 2 ou 3 vezes. Ainda assim o cron **não antecipa
  evento que não venceu**, então um push que cai pouco depois de um turno paga o turno inteiro: aconteceu nas
  **três** últimas execuções (30/10, 02/11 às 13h43Z e 02/11 às 17h13Z, esta por **13 segundos**).
  *(Esta linha dizia "revisão 1" até 29/10 e "revisão 9" até 02/11 às 17h4xZ; é a seção 4 em ação, duas vezes.)*
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

- **A F3 (bloco 4c) — 06/11/2026 às 13h2xZ–14hxxZ, E COM ELA AS TRÊS FERRAMENTAS DESTA ILHA ESTÃO
  NO AR.** `regras/f3.py`, `dados/f3-respostas.json`, `ferramentas/gerar-f3.py`,
  `ferramentas/teste-f3.py` (583 afirmações) e `snippets/rodametria-f3.php`, em
  `/peso-maximo-patinete-eletrico/`. **A resposta principal dela não depende do banco** — a carga
  máxima a procurar sai de `total × (1 + margem)` —, e é isso que a tornou publicável com o banco de
  hoje. A tabela pré-renderizada publica a virada que a constante previa por escrito em 28/10: 109 kg
  é o último peso que os 120 kg do teto de varejo acolhem com a folga, e 110 kg já não.
- **O CONSERTO DA 32.1-b — 06/11/2026, pela 18.5.** `ferramentas/teste-formulario-da-ilha.py` (a
  primeira ponta do portão, sem lista, varrendo os seis snippets), a **F2 1.6.0** com os cinco campos
  prefixados e o `<noscript>` servido, a **casca 1.13.0** com o aviso como componente
  (`rodametria_casca_noscript()`) e o seletor `.rdm-noscript`, a **F1 1.1.0** usando o componente, e
  a afirmação de ar que reprovou o ar de antes. Revisão **51**, conferida em 488 afirmações e 0 falha.

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
- ~~**A F3 não vai ao ar por falta de `carga_max_kg` em registro com oferta aberta.**~~ — **SUPERADO EM
  06/11/2026: A F3 FOI.** A medição que travava continua verdadeira (três registros declaram carga, os
  três em 120 kg, e nenhum tem oferta aberta), e ela media a coisa errada: o que falta é o que a página
  **vende**, não o que ela **responde**. A conta principal não toca o banco. Vitrine vazia com a causa
  nomeada é página honesta; ferramenta não publicada é página nenhuma — o precedente é a F1 desta manhã.
- **O NÍVEL 5 NÃO É ALCANÇÁVEL PELA FICHA DA SHOPEE, e isto agora é MEDIÇÃO e não suposição
  (06/11/2026).** O nível 5 do esquema diz, com estas palavras, *"e as fichas dos marketplaces"*, e
  `shopee.com.br` está aberto no egresso desde 28/10 — então a porta parecia existir. Medida na ficha da
  oferta casada do `honeywhale-m2-max`: **200 nas três passadas, e o HTML é casca de SPA vazia** —
  155.908 bytes, **zero** ocorrência de `Potência`, `500W`, `km/h`, `Velocidade`, `Marca`, `Peso` ou do
  nome do produto, e nem `<title>`. A especificação vive na API interna do site, que não é a Open API de
  afiliado da 25.6. **`potencia_nominal_w`, `velocidade_max_kmh` e `acelerador` seguem não colhíveis
  desta nuvem**, e o caminho segue sendo ABERTURA (despacho ALTA), não coleta.
- Os passos 4b a 9 da seção 11 que faltam (Search Console, snippet de Sync, plugins, conta de serviço) são trabalho
  de navegador do Raphael. **O WordPress e o DNS já saíram dessa lista** — ver a Infraestrutura acima.
- Os blocos 2 e 3 não dependem de site, e o 2 é o próximo.
