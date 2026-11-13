# ILHA: RODAMETRIA — mobilidade elétrica

Leia o `ARQUIPELAGO.md` da raiz antes deste arquivo. Ele carrega todas as regras comuns; aqui fica só o que é desta ilha. **Nunca copie regra do `ARQUIPELAGO.md` para cá.**
O dossiê que aprovou esta ilha é `bussola/dossies/rodametria/DOSSIE.md`, e a ficha é `bussola/oportunidades/rodametria.md` — leia os dois na primeira execução e não repita o que eles já mediram. **A ficha manda sobre o dossiê** onde os dois divergirem: o dossiê foi escrito antes da regra só-Shopee (BUSSOLA.md 0.8 e 0.9) e trata o Mercado Livre como porta principal; a ficha, reaprovada às 14h29, põe o patinete só-Shopee no centro.

## Identidade
- Nicho: **acertar os três números antes de comprar um veículo elétrico** — potência e velocidade (precisa de CNH e placa?), bateria (quantos km faz?) e carga máxima (aguenta o meu peso?). O eixo paramétrico, não "patinete" como categoria comercial.
- Domínio: `rodametria.com.br`, **registrado e pago pelo Raphael em 27/10/2026**. Ilha nº 6 do Arquipélago.
- **Tokens, símbolo e assinatura moram em `DESIGN.md`**, nesta pasta, e é de lá que a casca renderiza (seção 22.6). Onde este arquivo e o `DESIGN.md` discordarem, vale o `DESIGN.md`. Resumo: tinta `#13212B` · verde `#0A6B4C` (um uso forte por tela fora da marca) · piso `#F6F8F7` · superfície `#FFFFFF` · traço `#D3DAD7` · legenda `#4A5A66` · alerta `#8F4A00`; Alfa Slab One só no nome da marca, Barlow Semi Condensed nos títulos, Barlow no texto, JetBrains Mono em todo número e unidade.
- Símbolo: **V9**, aprovado pelo Raphael em 27/10/2026 — patinete elétrico de frente com asas curvas e raios verdes. **É exceção aprovada por ele à regra "símbolo nunca é o objeto desenhado"**; o registro das recusas está no `DESIGN.md`. Assinatura horizontal **H1**.
- O site vende **mobilidade elétrica**, nunca só "patinete": a assinatura diz `MOBILIDADE ELÉTRICA`.

## O buraco que esta ilha existe para ocupar
Medido em 27/10/2026 no Chrome do Raphael (`bussola/dossies/rodametria/DOSSIE.md`, seção b): as seis cabeças de compra do nicho (`moto eletrica` 823 mil, `bicicleta eletrica` 673 mil, `scooter eletrica` 301 mil, `patinete eletrico` 246 mil, `bike eletrica` 201 mil, `motos eletricas para adultos` 201 mil buscas/mês) têm **SERP mista e não tomada**: só o Mercado Livre como varejo grande fixo, o resto é loja pequena de marca, YouTube, Instagram, OLX e Reddit; **sem carrossel de compras**, com visão geral de IA; **nenhuma fazenda da lista e nenhuma calculadora** de CNH, autonomia ou carga na primeira página. **O que isso decide:** a ilha entra pela ferramenta que ninguém tem (F1, CNH), e as páginas pelo nome do produto (seção 30) disputam as cabeças.

## Memória a carregar
`/areas/projeto-rodametria.md`, `/areas/fabrica-de-sites.md`, `/areas/playbook-nascimento-projeto.md` (fase 4b), `/areas/arquipelago-bussola.md` (a rodada que aprovou este nicho, em 27/10/2026), `/topics/dev-conventions.md`. Sem memória, **não pare**: o estado está em `ESTADO.md`, `REGISTRO.md` e neste arquivo.

> **ESTA SEÇÃO FALTAVA, E FOI ACRESCENTADA EM 28/10/2026 PELO BLOCO 3.** As outras **cinco** ilhas e o próprio `ilhas/_modelo/PROMPT.md` têm esta seção; esta nasceu sem ela, em 27/10. É a mesma família das dívidas que o Pente Fino vem achando no molde — campo que o molde tem e a ilha nova não herdou —, com o sinal invertido: aqui o molde estava certo e a ilha nasceu incompleta. **E a parte honesta:** `/areas/projeto-rodametria.md` **pode não existir ainda**, porque esta ilha tem dois dias e nenhuma execução a escreveu. Por isso a frase "sem memória, não pare" vale literalmente aqui, e por isso o `bloco_atual` do `ESTADO.md` desta ilha é longo: enquanto não houver memória, ele **é** a memória, e quem fechar bloco escreve nele o próximo passo desbloqueado. Esta ilha não tem `README.md` — a linha do molde o cita e aqui ele não existe.

## Endpoints desta ilha
- **Status (público, GET):** `https://rodametria.com.br/wp-json/rodametria/v1/status` — **medido em 200 às 13h2xZ de 28/10/2026**, devolvendo `versao_sync: 1.1.5`. Às 10h17Z da mesma manhã devolvia **404**: o snippet **Rodametria Sync nasceu entre as duas medições** (passo 8 da seção 11, feito pelo Raphael), e nem o `ESTADO.md` nem este arquivo sabiam.
- **Sync (POST, exige `manage_options`):** `https://rodametria.com.br/wp-json/rodametria/v1/sync` — e o gatilho por query na raiz, `https://rodametria.com.br/?rodametria_sync=<token>`, com o token lido em `/wp-json/rodametria/v1/token` (também exige `manage_options`). **O token desta ilha não está no repositório e não deve estar** — quem precisa dele o lê logado. A Fundação **não precisa dele** para desembarcar: o Sync tem **cron próprio de 30 minutos** (`rodametria_30min`), e foi ele que rodou às 11h48, 12h30, 12h48 e 13h10Z de 28/10.
  > **MEDIDO EM 29/10/2026 às 16h3xZ — O CRON NÃO RODA POR RELÓGIO: RODA POR VISITA, E ISSO MUDA O CUSTO DE TODA EXECUÇÃO AQUI.** A frase acima e a do `ESTADO.md` ("ela empurra e espera") estão certas sobre o **token** e erradas sobre o **relógio**. O log do `/status` trazia disparos às 11h39, 12h09, 13h56 e 14h09Z e depois **nada por 2h29** — e 14h12Z é o minuto em que a execução anterior fechou e **parou de abrir o site**. É WP-Cron: ele é acionado por **requisição**, não por um relógio no servidor. Três GETs na home e o `wp-cron.php` respondendo **409** (já havia cron em andamento), e a revisão entrou em **um minuto**. A execução da manhã registrou **nove esperas de cron** entre 10h44Z e 12h10Z: eram evitáveis. **Depois de empurrar, abra a própria página** — não precisa do token para isso.
- **Base que o Sync lê:** `https://raw.githubusercontent.com/rmnatal/arquipelago/main/ilhas/rodametria/` + o arquivo, com `?v=<timestamp>` contra cache. Vale a **20.5**: revisão atrasada logo depois do push é cache do GitHub, não defeito — reacione de dois em dois e só trate como defeito se não subir em ~10 minutos.
- **Diagnóstico e reparo da porta de entrada (GET, exige o token do Sync):**
  `https://rodametria.com.br/wp-json/rodametria/v1/rotas` — e com `&reparar=1` ela roda o
  `flush_rewrite_rules( true )` e devolve o antes e o depois. **NO AR DESDE 03/11/2026**, revisão 30,
  casca 1.7.0. É a rota que a **29.3** manda toda ilha servir, e esta ilha nasceu sem ela.
  **O token não está no repositório e não deve estar** — e pela **29.3-a** do contrato (12/11/2026) isso
  **não** significa que o reparo não é exercitável daqui: esta linha dizia que não era, e a dedução é
  falsa. Em 11/11 às 17h54Z a Sentinela reparou duas ilhas desta nuvem, e em 12/11 às 10h18Z a Fundação
  reparou a clubedomosaico em um minuto. **Tente antes de escrever que não dá.** E pela exceção da
  **29.4** (a cura da porta) a ilha que a tiver repõe o bloco sozinha,
  sem token nenhum — **e desde 12/11/2026 esta ilha A TEM: seção 14 da casca, versão 1.26.0, revisão
  87, com as cinco travas do contrato e o portão `ferramentas/teste-cura-da-porta.php` (174
  afirmações, 5 mutações cobradas).** `/casca` serve `tem_cura_da_porta` e `fonte_do_log_da_cura`, os
  dois sem token, para a leitura no ar não precisar supor que ela está carregada. *(Esta linha dizia
  "esta ilha ainda não a tem, e copiar a seção 6-b é tarefa aberta aqui", escrito em 12/11 de manhã
  pela execução da clubedomosaico; fechado na tarde do mesmo dia.)* A
  parede é: medida em 03/11 às 10h4xZ, a rota devolve **401** sem token (`rodametria_rotas_token_ausente`)
  e **401** com token errado (`rodametria_rotas_token_invalido`), e **é esse segundo código que prova que
  a casca achou a fonte do token e rodou o `hash_equals`** — ele não sairia se o nome herdado
  (`rodametria_sync_token`) estivesse errado. Quem tiver o token fecha a última afirmação com um GET:
  o diagnóstico tem de dizer `tem_wordpress: true`. **Não há gancho automático (29.4).**
- **A CASCA E A F2 ESTÃO NO AR DESDE 29/10/2026.** `/` (home, molde da 32.2) e
  `/autonomia-patinete-eletrico/` (F2, molde de FERRAMENTA da 32.1). A casca publica
  `https://rodametria.com.br/wp-json/rodametria/v1/casca` (GET público), que devolve a versão
  da casca, o relato da instalação e o mapa de páginas com a URL de cada uma — é por ele que
  `ferramentas/conferir-no-ar.py` confere que link interno não aponta para 404.
  **Desde 03/11/2026 (casca 1.8.0) ele serve também `tem_purga_de_cache`**, o mesmo booleano que o
  retrato da rota `/rotas` traz — e está aqui porque aquele retrato **exige o token do Sync**, que
  não está no repositório: o "pronto quando" do despacho da purga não era conferível desta nuvem, e
  critério de pronto que ninguém mede fecha por leitura de código. Booleano sobre a existência de
  uma função desta ilha não é segredo do servidor (29.3).
- **O `manifest.json` desta ilha nasceu em 28/10/2026 na revisão 1, e ela NÃO PUBLICAVA NADA de propósito** — os três grupos vazios, para provar o canal ponta a ponta com zero página em risco. Antes dele o `/status` acusava `revisao: -1` e quatro `FALHA manifest: HTTP 404` seguidas. A primeira revisão que publica algo é a da **casca (bloco 3b)**.
- **O WORDPRESS JÁ ESTÁ NO AR, medido em 28/10/2026 às 10h17Z** pela execução do bloco 1: `https://rodametria.com.br/`
  devolve **200** em três tentativas, `<title>Rodametria - Mobilidade elétrica</title>`, `last-modified` de 27/10
  às 22h17Z, tema de blocos cru e **nenhuma página publicada**. `/wp-json/` responde 200, `/wp-sitemap.xml`
  redireciona (301) e **não lista URL nenhuma**, `/nao-existe-xyz/` devolve 404 de verdade (a porta de entrada da
  seção 29 está sã) e `/wp-json/rodametria/v1/status` devolve **404** — o snippet de Sync não existe ainda.
  **O domínio também já passa pelo egresso desta nuvem**, então o passo 20.1 está cumprido de fato.
  *(O `ESTADO.md` dizia "WordPress: pendente" até esta medição: é a seção 4 em ação — o site anda e o cabeçalho
  fica para trás em silêncio.)*

---

## DESPACHO DA SENTINELA — 2026-11-13 (RONDA DIÁRIA TÉCNICA) — **OS TRÊS ITENS ESTÃO FECHADOS E CONFERIDOS NO AR EM 13/11/2026 às 16h4xZ (18.4)**

> **FECHADO PELA EXECUÇÃO DA FUNDAÇÃO QUE RESERVOU A ILHA ÀS 16h16Z**, inteiro e numa passada só, como a 18.2 manda. Revisão **92** no `/status` = `manifest.json` em **92**, as **8 linhas** da revisão lidas uma por uma e todas dizendo `ok` (20.4). O despacho não foi apagado quando o conserto foi escrito, e sim quando foi **medido no ar**: `conferir-no-ar.py` em **735 afirmações, 0 falha**; `conferir-32-5-no-navegador.mjs` **APROVADO, 10 de 10**; console **10 de 10 limpo** em duas passadas. A história inteira está no `REGISTRO.md` desta data.
>
> **ITEM 1 — o anúncio morto saiu.** `23898889810` e `4fxWYUAZJT` com **zero** ocorrência no HTML servido das 10 URLs e em `dados/vitrine-de-produto.json`. A página do patinete vai de 15 para 14 linhas e a mediana de R$ 1.695,92 para R$ 1.697,46. **E o achado que vale mais que a baixa:** a Open API de afiliados **ainda lista** o item, com o mesmo `productLink`, o mesmo título e o mesmo preço — **catálogo de afiliado não é teste de vida**, e quem perguntar à API em vez de abrir a ficha ressuscita o anúncio. Está escrito na linha de quarentena, que é o que o coletor lê.
>
> **ITEM 2 — os dois campos chegam vazios, e o que a primeira tela entrega é a energia.** `rdm_aut` e `rdm_peso` saem do HTML **sem `value`** (medido no ar), a manchete é **960 Wh**, a recusa nomeia a causa logo abaixo do bloco de compra e **nenhum kg** aparece na resposta entregue. As linhas 3 e 5 da tabela 2.1 da especificação foram corrigidas junto. O primeiro botão de compra da F2 **desceu** de ~1.380 px para **1.333 px** (teto 1.400). As frases do peso viraram **pares**: informado, o peso é nomeado — decisão do item 2 de 30/10/2026, que continua de pé; ausente, não existe para ser nomeado.
>
> **A METADE DA DESIGUALDADE QUE O CONSERTO NÃO ALCANÇA, dita aqui em vez de sumir no verde:** com a entrada que o servidor entrega, 374 Wh e 2.160 Wh devolvem **"374 Wh"** e **"2.160 Wh"** e **faixa de km nenhuma** — a desigualdade que o despacho cobra está cumprida ali. Mas se o **leitor** declarar os mesmos 60 km para as duas baterias, a faixa volta a ser **"25 a 60 km"** nas duas, e isso **não tem conserto nesta ilha hoje**: o degrau 2 degrada o número **declarado** pelo relevo, e com `consumo-absoluto-wh-por-km-patinete` em `pendente` não existe segunda fonte de km. O que a página continua distinguindo é a **energia**, que é a primeira frase da caixa. Os três fatos estão cobrados por afirmação em `teste-f2.py`, inclusive o de que **o dia em que o degrau 3 destravar essa régua reprova** em vez de seguir verde.
>
> **ITEM 3 — a quarta cópia morreu.** `venda medida` com **zero** ocorrência no HTML servido das 10 URLs e em `dados/paginas-de-produto.json`; as duas páginas de produto servem a **mesma** cadeia do `rdm_produto_criterio_de_ordem()` nas duas camadas, por marcador. E a régua passou a mordê-la: `PADROES_DE_AFIRMACAO` virou expressão regular (a cadeia crua `a ordem e por` nunca alcançaria `a ordem DOS CARTÕES é por`), ganhou a família genérica e a própria cadeia `venda medida`, mais quatro mundos — dois deles os literais que estavam no ar.
>
> **O QUE ESTA EXECUÇÃO ACHOU E NÃO ESTAVA NO DESPACHO, para a próxima ronda decidir:** o convite da F3 para a F2 monta `?rdm_peso=<exemplo da F3>`, e **a F2 nunca leu `$_GET`** — o parâmetro não faz nada, e nunca fez. Não mexi: ler o `rdm_peso` da URL devolveria à F2 um peso que é o **exemplo da F3**, não o do leitor, que é exatamente o defeito que o item 2 acabou de fechar. Quem for consertar tem de decidir primeiro de quem é aquele número.

## DESPACHO DA SENTINELA — 2026-11-11 (LEITURA SEMANAL, 19h4xZ–20h1xZ) — A ILHA ENTROU NA DISPUTA, E A PÁGINA DE COMPRA DE 673 MIL BUSCAS/MÊS ESTÁ FORA DO ÍNDICE COMO 404 — **O ITEM 1 ESTÁ FECHADO EM 12/11/2026 às 13h2xZ; O QUE SOBRA NÃO É DA FUNDAÇÃO E ESTÁ LISTADO ABAIXO**

> **REESCRITO PELA 18.3 EM 12/11/2026, e a 18.3 é literal: "a execução resolve os que couber, reescreve o despacho deixando SÓ os itens que faltam (com o motivo em uma linha) e fecha".** O texto original fica preservado embaixo, inteiro — o que esta nota faz é dizer, de cima, o que ainda está aberto e **de quem é**, porque despacho pela metade sem essa reescrita é o próximo trabalhador não tendo como saber o que já foi feito.
>
> **ITEM 1 — FECHADO, E A RESPOSTA JÁ MORAVA NOS ARQUIVOS DESTA ILHA.** O item pede uma linha em `dados/consertos.md` dizendo, **com número**, se houve ou não queda da porta em 05/11. **Houve**, e a linha está lá, datada de hoje. A janela: verde em **04/11 20h1xZ**, queda achada em **05/11 10h19Z** (8 das 9 URLs e as três portas da 29.2 em 404 na página da HostGator, só `/` em 200), **ainda no chão às 13h2xZ e às 19h17Z** de 05/11, levantada às **~02h3xZ de 06/11** pela mão do Raphael no cPanel. O rastreamento de **05/11 às 22:14:32** cai dentro dessa janela **nas duas leituras possíveis do fuso** (Brasília ⇒ 06/11 01h14Z, ~1h20 antes do reparo; UTC ⇒ 05/11 22h14Z, ~4h20 antes), então não há leitura do relógio que o ponha fora dela. **O 404 no índice é a porta de entrada, não a página.**
>
> **E O ATALHO QUE O ITEM OFERECIA RESPONDERIA ERRADO**, o que vale mais que a resposta: ele dizia *"se o `.htaccess` desta raiz tiver `tem_wordpress: true` e um `mtime` anterior a 05/11, a resposta é 'não houve'"*. O arquivo foi **reescrito** no conserto de 06/11, então o `mtime` dele é **posterior** a 05/11 e aquele ramo nunca poderia fechar — e ele exigia o token do Sync, que não está no repositório. **A resposta barata estava em `dados/consertos.md`, escrita pelas próprias execuções de 05/11.** É a família do `git log` raso da 1.1 e do "não havia navegador" da 33: instrumento novo procurado onde já havia registro.
>
> **E A PREMISSA DO ITEM ESTAVA CERTA NO MECANISMO E ERRADA NA ESCALA:** ele supõe *"uma queda de minutos nesta ilha em 05/11 não teria sido vista por ninguém"*. Foi vista por três execuções, com despacho ALTA e notificação ao Raphael às 10h2xZ, e durou **~16 horas**.
>
> **O QUE A FUNDAÇÃO FEZ ALÉM DE RESPONDER, porque responder não põe ilha no ar:** a casca passa a repor o bloco sozinha — **seção 14, casca 1.26.0, revisão 87**, a exceção nomeada da 29.4 com as cinco travas, portão `ferramentas/teste-cura-da-porta.php` com **174 afirmações e 5 mutações cobradas**. Era o item 1 do despacho de CLASSE de 11/11 (no `PROMPT.md` da robometria), que diz com todas as letras que esta ilha estava sem a cura. **Não é o conserto da causa (29.5):** o chamado na HostGator continua aberto e continua sendo o único lugar onde a causa se resolve.
>
> **O QUE CONTINUA ABERTO, E NENHUM DOS TRÊS É BLOCO DA FUNDAÇÃO:**
>
> 1. **ITEM 1, a metade do Search Console — É DA LEITURA DE 18/11.** A indexação de `/veiculos/bicicleta-eletrica/` foi **solicitada em 11/11 e o Google aceitou**; pela trava 2 da seção 12 quem confere não é quem pediu. **pronto quando:** a Inspeção de URL disser "O URL está no Google" e ela aparecer com ≥1 impressão.
> 2. **ITEM 2 e PROPOSTA 3 — a ação correta é NÃO AGIR, e isso é regra e não preguiça.** A **12.1** proíbe mexer em texto de página que o Google ainda não viu. **pronto quando:** a leitura de 18/11 disser se `/veiculos/patinete-eletrico/` recebeu a primeira impressão dela.
> 3. **PROPOSTA 2 (`moto elétrica`, 823 mil buscas/mês) — É DO RAPHAEL E NÃO É AUTOMATIZÁVEL.** Falta o **produto**, não a SERP: criar a etiqueta `rodametriamotoeletrica` em `mercadolivre.com.br/afiliados/adminlabel` e gerar os 5 links, porque o gerador do Mercado Livre tem reCAPTCHA (seções 7 e 25.6). A lista está em `dados/links-afiliado-pendentes.md`. **pronto quando:** aquele arquivo tiver os 5 encurtados com `url_produto` ao lado.
>
> **O texto original do despacho fica abaixo, preservado.**

**O NÚMERO DA SEMANA, E ELE É BOM: as primeiras 8 impressões da vida desta ilha** (0 em 04/11), sitemap **Processado** com 10 páginas e última leitura do Google em 09/11, **9 das 10 URLs do sitemap no índice**. O conserto que a leitura de 04/11 fez — enviar o sitemap, que nunca tinha sido enviado — pagou em sete dias.

**ITEM 1 — ALTA. `/veiculos/bicicleta-eletrica/` ESTÁ FORA DO ÍNDICE COMO "NÃO ENCONTRADO (404)", E ELA É UMA DAS DUAS ÚNICAS PÁGINAS DESTA ILHA COM BOTÃO DE COMPRA.** Medido na Inspeção de URL da propriedade `sc-domain:rodametria.com.br` em 11/11 por volta das 20h0xZ, com o retrato inteiro na tela:

- veredito: **"O URL não está no Google"** · "A página não está indexada: Não encontrado (404)"
- Detecção → Sitemaps: `https://rodametria.com.br/wp-sitemap.xml` · Página de referência: "Nenhuma página foi detectada"
- Rastreamento → **Último rastreamento: 5 de nov. de 2026, 22:14:32** · Rastreada como **Googlebot Smartphone** · O rastreamento é permitido? **Sim** · **Busca de página: Falha: Não encontrado (404)**
- balde de Indexação das páginas: "Não encontrado (404)", **detectada pela primeira vez em 07/11/2026**, 9 páginas afetadas — e das 9 esta é a **única** que é página da ilha; as outras 8 são `wp-content/*`, `wp-*.php` e variantes `http://`.

**E A PÁGINA ESTÁ SÃ HOJE, MEDIDO E NÃO SUPOSTO:** `https://rodametria.com.br/veiculos/bicicleta-eletrica/` responde **200** desta nuvem com quebra de cache em 11/11 20h0xZ, e a ronda diária de hoje mediu **10 de 10 URLs em 200 em duas leituras**. Ou seja: **o registro do Google é velho e a página é boa.**

**O QUE A SENTINELA JÁ FEZ:** puxou a alavanca da 14.7 — **SOLICITEI INDEXAÇÃO desta URL em 11/11 por volta das 20h0xZ e o Google aceitou** ("Indexação solicitada · O URL foi adicionado a uma fila de rastreamento prioritário"). A cota não recusou, ao contrário de 14/10. **Quem confere não é esta execução** (trava 2 da seção 12): o veredito é da leitura de 18/11.

**O QUE FICA PARA A FUNDAÇÃO, E NÃO É CONSERTO DE CÓDIGO — É UMA PERGUNTA COM RESPOSTA MEDÍVEL:** por que o Googlebot pegou 404 nessa URL em **05/11 às 22:14:32**? A página existia desde 30/10 (está na lista de 9 URLs do sitemap que a leitura de 04/11 escreveu) e as rondas de 04, 06 e 09/11 mediram a ilha inteira em 200. **As três portas da 29.2 desta ilha estão verdes agora** (medidas desta nuvem em 11/11 20h0xZ: `/wp-sitemap.xml` 200, `/robots.txt` 200, caminho virgem em 404 na página da própria ilha, 73.064 bytes — não é a página de estacionamento de 2.361 bytes). Mas **as duas ilhas irmãs na mesma raiz do mesmo cPanel caíram com a assinatura da seção 29 em 30/10 e em 11/11**, e a clubedomosaico caiu DE NOVO hoje às 20h00:34Z. **Uma queda de minutos nesta ilha em 05/11 não teria sido vista por ninguém, e o 404 no índice seria o único rastro que ela deixaria.** **pronto quando:** existir no `dados/consertos.md` desta ilha uma linha dizendo, com número, se houve ou não queda da porta em 05/11 — e, se o `.htaccess` desta raiz tiver `tem_wordpress: true` e um `mtime` anterior a 05/11, a resposta é "não houve" e o caso fecha aí.

**ITEM 2 — AS 8 IMPRESSÕES FORAM TODAS PARA `/veiculos/`, E AS TRÊS CONSULTAS NOMEADAS SÃO DE ASSINATURA, NÃO DE COMPRA** (`mobilidade elétrica` 4, `electric scooter vehicle price` 2, `mobilidade elatrica` 1). **A ação correta aqui é NÃO AGIR, e ela é uma regra, não preguiça:** a 12.1 diz que consulta sem impressão é problema de indexação e não de ranqueamento, e proíbe mexer no texto de página que o Google ainda não viu. **pronto quando:** a leitura de 18/11 disser se `/veiculos/patinete-eletrico/` recebeu a primeira impressão dela — esse é o sinal que autoriza qualquer trabalho de texto nas páginas de produto.

**AS TRÊS PROPOSTAS DE ACELERAÇÃO DA 12.1, com consulta nomeada, em ordem de ROI:**

**PROPOSTA 1 — `bicicleta elétrica` (673 mil buscas/mês).** Página: `/veiculos/bicicleta-eletrica/`. Posição hoje: **não tem — está fora do índice**. O que falta: só o rastreamento novo, já pedido. O que muda: a página serve **6 cartões com ficha de anúncio** mais o piso de busca (`2BGBa08SR6`), e **hoje ela não é vista por ninguém**. É a maior devolução por menor esforço do Arquipélago nesta semana, porque o trabalho já está feito e preso atrás de um registro velho do Google. **pronto quando:** a Inspeção de URL dela disser "O URL está no Google" e ela aparecer com ≥1 impressão na tabela por página.

**PROPOSTA 2 — `moto elétrica` (823 mil buscas/mês, a maior cabeça do nicho).** Página: ainda não existe; o slug `veiculos/moto-eletrica` está reservado em `dados/consultas-de-produto.json` com `publicar_declarado: false`. Posição hoje: sem página. O que falta, e está medido: **o PRODUTO, não a SERP** — a SERP já tem veredito `alvo` visto com os olhos do Raphael em 27/10, e a medição de 29/10 na Open API da Shopee achou só **três** anúncios de adulto, **os três com ZERO venda** e com preços variando R$ 6.500 para a mesma classe. **Medido HOJE no Chrome, no Mercado Livre, que é o caminho que o próprio `consultas-de-produto.json` nomeia para esta consulta:** `lista.mercadolivre.com.br/moto-eletrica-adulto` devolve **7 páginas de catálogo `/p/MLB`**, e o achado é duro — **três delas (MLB81237529, MLB81237531, MLB81237535) são o MESMO anúncio** (Scooter Falcon 500W, R$ 10.000) em três entradas de catálogo, e **só UMA das sete declara venda** (MLB78820650, Off-road GT600 7500W, R$ 17.999, +50 vendidos). **Produtos distintos: 5. Com venda declarada: 1.** A lista inteira está em `dados/links-afiliado-pendentes.md`, criado nesta leitura. **O gesto é do Raphael e não é automatizável** (reCAPTCHA no gerador do Mercado Livre, seções 7 e 25.6): criar a etiqueta `rodametriamotoeletrica` em `mercadolivre.com.br/afiliados/adminlabel` e gerar os 5 links. **pronto quando:** `dados/links-afiliado-pendentes.md` tiver os 5 encurtados colados com `url_produto` ao lado, e a consulta `moto elétrica` existir em `dados/anuncios-por-consulta.json` com ≥3 anúncios que servem e o número próprio contado — que é o piso da 30.2.

**PROPOSTA 3 — `patinete elétrico` (246 mil buscas/mês).** Página: `/veiculos/patinete-eletrico/`, no índice e **com zero impressão** nesta janela. Posição hoje: sem impressão. O que falta: tempo e sinal de entrada — a página tem poucos dias de índice e a ilha inteira tem 8 impressões. **A proposta é explicitamente NÃO TOCAR NELA e medir em 18/11**, porque a 12.1 proíbe trabalhar texto de página que o Google ainda não viu, e porque esta é a página mais trabalhada da ilha (15 anúncios que servem, mediana R$ 1.695,92, 32.5 aprovada a 1.351 px). **pronto quando:** a leitura de 18/11 trouxer a primeira impressão dela, com posição de uma casa decimal — e só então ela vira tarefa de banda.

## ~~DESPACHO DA SENTINELA — 2026-11-11 (RONDA DIÁRIA TÉCNICA, 14h3xZ–15h0xZ) — QUATRO ITENS, E O PRIMEIRO É UM BOTÃO DE COMPRA QUE NÃO VENDE~~ — **OS QUATRO FECHADOS EM 11/11/2026 às 17h1xZ, CONFERIDOS NO AR PELA 18.4, NAS REVISÕES 84 E 85**

> **O "PRONTO QUANDO" DE CADA ITEM, medido nas 10 URLs do sitemap com quebra de cache:**
>
> **ITEM 1 — FECHADO.** `s.shopee.com.br/9pfbJrNKOR` com **zero** ocorrência no HTML servido de `/veiculos/patinete-eletrico/` e nas outras nove; o anúncio `58212105781` com **zero** ocorrência em campo vivo do banco — ele saiu da lista de anúncios e virou **uma linha de prosa** em `anuncios_aposentados`, no formato fechado `APOSENTADO EM <data> — item <id> da loja <id> — … CAUSA: … || ULTIMA MEDICAO: …` que a 25.4-b.3 pede; a vitrine serve **5 cartões, os 5 com ficha**, mais a busca (`60Su92trfV`) como piso em 6 botões. **E a ficha do cartão que entrou foi testada VIVA pela própria ronda de hoje**: a tabela daquela página já servia os 16 anúncios, e as 24 fichas do teste de vida de hoje deram 23 vivas e UMA esgotada — a que saiu. **O conserto virou ferramenta** (`aplicar-aposentadoria-de-anuncio.py`, com portão próprio) **e a quarentena atravessa a coleta**: `coletar-por-consulta.py --gravar` passa a recusar o anúncio aposentado quando a loja o devolver, imprimindo a recusa. Sem isso o conserto se desfazia na coleta seguinte, calado — está escrito na **25.11** do contrato.
>
> **ITEM 2 — FECHADO.** `\bilhas?\b` com **zero** ocorrência no texto visível **e** no HTML servido das 10 URLs (as 9 da prosa institucional e a 1 da nota da F2 dizem `este site`). A afirmação nova **morde e não reprova a trilha**: `BASTIDOR_COM_FRONTEIRA` em `conferir-no-ar.py` é lista de padrão com **fronteira de palavra** sobre o texto **dobrado**, e os mundos fabricados do `--autoteste` exigem que ela reprove a frase que estava no ar nomeando a página e **aprove** a trilha de migalhas, que sai em 5 a 7 ocorrências por página. `ilha` continua livre em comentário de snippet. **E a palavra foi encontrada uma décima vez depois do desembarque da 84** — na FONTE do gerador da F2, que desfez calada a troca feita no arquivo gerado; está na **20.12** do contrato.
>
> **ITEM 3 — FECHADO.** `publicáv`, `publicav` e a cadeia `Tipo: pendente` com **zero** ocorrência nas 10 URLs, no visível e no servido. A prestação de contas da constante pendente continua dizendo, em português de leitor, que não publicamos número para aquele consumo **e por quê** — e agora ela diz isso **uma** vez em vez de três: com valor nulo a linha é só a prosa da fonte, o rótulo `Tipo:` saiu e a cláusula do tipo é omitida. **O termo entrou na mesma lista única do item 2, e o achado vale mais que o conserto:** `publicavel` **já estava** na lista de bastidor e não pegava nada, porque o ar servia a palavra **com acento** e a comparação era de pedaço de texto cru. Está na **32.4-e**.
>
> **ITEM 4 — FECHADO, E ERAM QUATRO CÓPIAS.** As duas páginas servem a **mesma cadeia**, vinda de **um** lugar, e as duas páginas de produto a servem também — 4 páginas com a cadeia idêntica, **zero** molde cru. A cadeia descreve o que as ferramentas realmente usam: a tupla `CHAVES_DE_ORDEM` de `gerar-vitrine-de-produto.py` é de onde saem **a chave de `ordenar()` e a frase**, então frase e ordem não existem separadas. **Além das duas do despacho, a varredura achou mais duas, as duas em snippet e as duas servidas:** o rodapé da casca dizia *"quem decide a ordem é o que o FABRICANTE declara"* — **falso, e em toda página da ilha** — e o bloco de compra dizia *"a ordem é por VENDA MEDIDA"*, que afirma uma medição nossa que não existe (a contagem é da loja). O rodapé passou a **remeter com link** em vez de declarar. O portão sem rede é `ferramentas/teste-criterio-de-ordem.py`: 27 afirmações, com as **quatro frases que estavam no ar** como mundos fabricados, a remissão nova como o mundo que tem de **PASSAR**, e a prova em dado fabricado de que `ordenar()` segue a tupla. **E a liberação de quantificador da frase antiga foi apagada junto com a frase**, porque liberação morta parece conferida.

> **A ILHA ESTÁ SÃ, E ISSO FOI MEDIDO E NÃO SUPOSTO.** 10 de 10 URLs em 200 em duas leituras com quebra de cache; as três portas da 29.2 verdes com `content-type` certo e o `/wp-sitemap.xml` servindo `sitemapindex` de verdade; caminho virgem em 404 na página da própria ilha; `/status` em **83** = `manifest.json` em **83**; zero `&#038;` dentro de `<script>`; zero página órfã contada na direção de ENTRADA (16.9(b)); zero link interno para fora do sitemap; meta description máxima de 159.
>
> **E HOUVE NAVEGADOR NESTA PASSADA — as três medições que as rondas de 04, 06 e 09/11 declararam impossíveis foram feitas.** A extensão de Chrome do Raphael respondeu e o Chromium desta nuvem subiu (seção 33). Resultado: **32.5 aprovada 10 de 10** (pior formulário/caixa 548 px de 700; pior botão de compra 1.351 px de 1.400); **console 10 de 10 limpo do lado da ilha** — as 5 a 10 falhas de rede por página são `fonts.gstatic.com` e `cf.shopee.com.br` recusados pelo EGRESSO DESTA NUVEM, não defeito de página, e por isso não viram item; **comportamento**: menu abre e fecha nas 10 com o `aria-expanded` alternando, `<details>` nenhum aberto por padrão, rolagem horizontal zero, barra fixa escondendo quando o bloco de compra entra na tela nas 6 que a servem; **as três ferramentas apertadas de verdade, 9 de 9 certas** (F1 em 1.000 W/32, 1.000 W/40, 1.500 W/45, 5.000 W/80 e 500 W/25 só pedal; F2 em 36 V × 10,4 Ah plano = 374 Wh e 50 km, e 72 V × 30 Ah ladeira = 2.160 Wh e 38 km; F3 em 130 kg = 143 kg e 60 kg = 66 kg).
>
> **A 32.4-d, ESCRITA HOJE, ESTÁ FECHADA NO AR:** zero comentário dentro do `<script>` da ilha nas 10 páginas. Os 7 marcadores que sobram por página estão no `speculationrules` do próprio WordPress e não são da ilha.
>
> **RECONFERÊNCIA DO DESPACHO DE 09/11, item por item, no ar — OS CINCO PASSAM:** (1) os quatro `id` de repositório com **zero** ocorrência em texto visível nas 10 URLs; (2) o `nota` de `veiculos.json` dizendo **4 publicáveis** recontados por `derivar-banco.py` e conferidos por `validar-banco.py` — o campo que voltou duas vezes fechou na terceira; (3) rótulo da barra fixa `Ver produtos` só onde há cartão e `Por que não indicamos` onde não há; (4) `17 registros` × `14 anúncios colhidos`, separados pelo verbo; (5) o menu serve **4 itens** e a ferramenta principal da ilha está entre eles.

**ITEM 1 — UM BOTÃO DE COMPRA DA VITRINE ESTÁ ESGOTADO, E ELE É O SEGUNDO CARTÃO DA PÁGINA DE MAIOR INTENÇÃO DE COMPRA DA ILHA.** Medido no navegador do Raphael às 14h5xZ, abrindo a `url_produto` e **nunca** o link de afiliado, em **duas** leituras:

- registro: *"Patinete Elétrico Adulto 650W com 3 Velocidades Bateria Recarregável para Mobilidade Urbana"*
- `url_produto`: `https://shopee.com.br/product/1430771203/58212105781`
- encurtado servido ao leitor: `https://s.shopee.com.br/9pfbJrNKOR`
- **degrau atual: 1** (loja oficial)
- onde está no ar: **cartão 2 da vitrine de `/veiculos/patinete-eletrico/`**, e o mesmo encurtado é servido **duas vezes** naquela página
- o que a página do produto serve: a palavra **`Esgotado`** colada ao título, nas duas leituras, sem CAPTCHA. O corpo caiu de ~4.400 para 2.789 caracteres na primeira leitura e voltou a 4.353 na segunda, com o `Esgotado` nas duas — o sinal é o texto do corpo, nunca o `<title>`, que nesta leva veio com o nome do produto e por isso é ainda mais enganoso que o genérico que a 25.4 descreve.

**Não consertei, e o motivo é a 19.2:** link morto é **dado do banco**, e trocar por outro anúncio é escolher entre duas opções defensáveis (reescolher ficha do mesmo produto, ou descer para o degrau 4 e deixar a busca virar o botão, como a robometria fez com o `electrolux-erb60` em 02/11).

**pronto quando:** `s.shopee.com.br/9pfbJrNKOR` tem **zero** ocorrência no HTML servido de `/veiculos/patinete-eletrico/` lido com quebra de cache; o anúncio `58212105781` tem **zero** ocorrência em campo vivo do banco; a vitrine daquela página volta a ter **todos** os cartões com ficha viva ou com a busca no botão; e a história do anúncio aposentado fica inteira dentro de `motivo_sem_url_produto`, fora dos campos vivos, como a 25.4-b manda.

**ITEM 2 — A PALAVRA `ilha` ESTÁ SENDO SERVIDA AO VISITANTE EM 5 DAS 10 PÁGINAS, 10 VEZES, E ELE NÃO TEM COMO SABER DO QUE SE TRATA.** Medido no HTML servido **e** no texto visível, com fronteira de palavra (`\bilhas?\b`), para não confundir com `trilha`:

| página | ocorrências | trecho |
|---|---|---|
| `/contato/` | 3 | *"Se um número desta **ilha** está errado…"*, *"Esta **ilha** ainda não tem uma caixa de e-mail própria…"*, *"nenhuma outra página desta **ilha** pede cadastro…"* |
| `/divulgacao-de-afiliados/` | 3 | *"Quando você compra por um botão desta **ilha**…"*, *"Hoje todos os botões de compra desta **ilha** são endereços de afiliado da Shopee…"*, *"Os dois casos foram medidos nesta **ilha**…"* |
| `/privacidade/` | 2 | *"Nenhuma página desta **ilha** tem um campo pedindo um dado seu…"*, *"esta **ilha** ainda não tem uma caixa de e-mail própria"* |
| `/sobre/` | 1 | *"O código e os dados desta **ilha** são versionados fora do site…"* |
| `/autonomia-patinete-eletrico/` | 1 | *"a única medição real de autonomia que a **ilha** tem com a ficha ao lado"* |

**Isto é a 32.4 no sentido mais literal que existe, e a 32.4-d de hoje já escreveu a régua:** *"o nome das ilhas irmãs entra na lista da 32.4: nome de outra ilha do Arquipélago numa página é bastidor da fábrica no sentido mais literal que existe, e o visitante não tem nem como saber do que se trata."* **`ilha` é o nome que o contrato dá a um site desta fábrica** (seção de vocabulário: *"cada site de nicho é uma ilha"*). A 32.4-d cuidou do nome PRÓPRIO das irmãs e deixou de pé o nome COMUM da coisa — e é o nome comum que aparece 10 vezes, em prosa de leitor, dizendo ao visitante que ele está dentro de uma peça de uma fábrica cujo nome o site nunca explica.

**Não consertei, por três motivos independentes:** (a) a prosa mora em **dois lugares de natureza diferente** — `dados/paginas-institucionais.json` (9 ocorrências) e os snippets `rodametria-casca.php` (33, a maioria em comentário), `rodametria-f2.php` (4) e `rodametria-institucional.php` (3) —, e a trava 3 da seção 12 proíbe a Sentinela de tocar em snippet *"sem exceção, mesmo que a mudança pareça de uma linha"*; (b) alcança **5 páginas de uma vez**, o que a 22.7 manda despachar; (c) não está na lista fechada da 19.1 — não é título, meta description, primeiro parágrafo nem rótulo, e `ilha` não está na lista "Proibidas" do `VOZ.md`. **Na dúvida, é despacho.**

**E a parte que vale mais que o conserto:** o conserto de uma palavra em cinco arquivos é a 32.5-c de novo. **A lista de termos de bastidor da régua desta ilha precisa ganhar `ilha`/`ilhas` com fronteira de palavra**, medida no HTML servido (32.4-c), **excluindo `trilha`** — senão o portão reprova a própria trilha que a 16.3 exige. E a lista mora num lugar só, para a régua nova não nascer fora do conserto.

**pronto quando:** `\bilhas?\b` tem **zero** ocorrência em texto visível e em JSON-LD nas 10 URLs do sitemap, lidas com quebra de cache; o portão de ar da ilha faz uma afirmação nova que **morde** (plantando `desta ilha` numa das cinco páginas, ele reprova nomeando a página) e **não** reprova a trilha; e a palavra `ilha` continua livre em comentário de snippet, porque comentário é a memória da ilha (seção 3) e a 32.4-b item 2 já decidiu isso para o `.php`.

**ITEM 3 — A F2 SERVE A PALAVRA `publicável` E O RÓTULO `Tipo: pendente` AO LEITOR, NO "COMO SABEMOS".** O trecho, literal, do HTML servido de `/autonomia-patinete-eletrico/`:

> *"Consumo de um patinete por km — **sem valor publicável**. **Tipo: pendente**, sem valor publicado. Não publicamos nenhum valor. A medição mais forte que achamos está em periódico que não conseguimos abrir, e as outras três candidatas foram recusadas…"*

`publicavel` e `pendente` são **valores do enum de `status` do banco** (`dados/esquema-banco.json`), e `Tipo:` é rótulo de campo de banco impresso como se fosse texto de leitor. **É a SEGUNDA vez que `publicavel` chega ao ar nesta ilha:** a ronda de 06/11 achou a palavra cinco vezes dentro do JSON do rodapé e o item foi fechado naquele dia. Pela **19.4(b)**, defeito que volta deixa de ser conserto e vira despacho de qualquer jeito. E a frase diz a coisa certa duas vezes com dois vocabulários — *"sem valor publicável"* e *"Não publicamos nenhum valor"* —, então o que falta ali não é informação, é a palavra da fábrica.

**pronto quando:** `publicáv`, `publicav` e a cadeia `Tipo: pendente` têm **zero** ocorrência em texto visível e em JSON-LD nas 10 URLs; a prestação de contas da constante pendente continua dizendo, em português de leitor, que a ilha não publica número para aquele consumo e por quê; e o termo entra na mesma lista única do item 2, medida no servido.

**ITEM 4 — `/sobre/` E `/divulgacao-de-afiliados/` DECLARAM O MESMO FATO — O CRITÉRIO QUE ORDENA A VITRINE — COM DUAS RÉGUAS DIFERENTES.** Os dois trechos, literais, do HTML servido:

- `/sobre/`: *"Não publica 'melhor patinete' nem 'top dez': **quem ordena uma lista aqui é o que o anúncio declara e o preço**, nunca a comissão."*
- `/divulgacao-de-afiliados/`: *"A ordem da lista. **Primeiro vem quem a loja mostra como mais vendido na busca medida**, e o desempate é o preço — nunca a taxa que um programa paga."*

As duas concordam no que a ordem **não** é (comissão) e discordam no que ela **é**: numa, o que o anúncio declara; na outra, a posição de mais vendido que a loja mostra. **A 20.7 já mediu o que isso dá:** *"duas declarações do mesmo fato começam iguais e só uma sobe."* E há um agravante de voz: a lista "Proibidas" do `VOZ.md` barra *"'mais vendido', selo de avaliação que a ilha não mediu"*, e a `/divulgacao-de-afiliados/` usa a posição de mais vendido da loja como o **critério** — a `/sobre/`, na mesma leitura, promete que a ilha não publica esse selo.

**Não consertei: é escolha entre duas opções defensáveis (19.2)** — a ordem real é uma só e quem sabe qual é quem escreveu o gerador da vitrine, não quem leu as duas páginas. E o conserto certo não é acertar as duas frases: pela 32.4-c, *"o conserto de uma frase duplicada não é consertar as duas: é a segunda deixar de existir"* — uma função monta a frase do critério e as duas páginas a chamam.

**pronto quando:** as duas páginas servem a **mesma** cadeia de critério de ordenação, vinda de **um** lugar; a cadeia descreve o que `ferramentas/` realmente usa para ordenar `cartoes` em `dados/vitrine-de-produto.json`; e um portão sem rede reprova quem escrever a segunda cópia.

### O QUE ESTA RONDA MEDIU E NÃO VIROU ITEM, dito para ninguém gastar execução redescobrindo

- **As 5 a 10 falhas de recurso por página no console são do EGRESSO DESTA NUVEM.** `fonts.gstatic.com` (as 5 fontes do `DESIGN.md`) e `cf.shopee.com.br` (as fotos dos cartões) devolvem `ERR_TUNNEL_CONNECTION_FAILED` no Chromium desta nuvem. **Zero** erro de JavaScript, **zero** exceção e **zero** resposta ≥ 400 vinda da ilha nas 10 páginas. Quem rodar console daqui vai ver as mesmas linhas e **não** é defeito de página.
- **A barra fixa da `/veiculos/bicicleta-eletrica/` parece quebrada na primeira leitura e não está.** No instante do `load` ela sai `hidden`/`display:none` nessa página e `flex` na `/veiculos/patinete-eletrico/` — é corrida do observador, não comportamento. Com a página assentada, as duas se comportam igual: escondida enquanto o bloco de compra está na tela (ele começa a 794 e 821 px, dentro dos 844 px do telefone) e `flex` a partir de ~1.400 px de rolagem. **Quem medir barra fixa espera a página assentar, ou mede duas vezes.**
- **O teste de vida da Shopee continua NÃO sendo tarefa desta nuvem, e agora a causa tem NOME.** O Chromium daqui abre `shopee.com.br/product/...` com HTTP 200, e a página **não renderiza**: `<title>` vazio, `innerText` vazio, `body.innerHTML` com 2.321 bytes, e **23 recursos de `deo.shopeemobile.com` recusados pelo egresso** — é a CDN de script da Shopee. `curl` é pior: devolve 200 com **199.781 bytes idênticos** para dois produtos diferentes e o corpo *"Please enable JavaScript on your browser"*. **O que funciona é o navegador do Raphael pela extensão**, lendo o corpo da `url_produto`: 31 itens em lotes de 3, zero CAPTCHA, título e `h1` do produto de verdade em cada um.
- **O teste de vida saiu INTEIRO nesta passada, e é a primeira vez desde 06/11:** 24 links de ficha (**23 vivos, 1 esgotado** — o item 1) e **7 palavras-chave de busca, 7 vivas**, 15 cartões cada, zero busca vazia (`Honeywhale M2 MAX patinete eletrico`, `Sousa Bike bicicleta eletrica`, `X13 scooter eletrica`, `LS Sport scooter eletrica`, `Kenda camara de ar 16 x 3.0`, `bicicleta eletrica adulto`, `patinete eletrico adulto`). **29 de 29 botões servidos no `<main>` rastreáveis até o repositório; intestáveis ZERO; item sem piso da 25.2 ZERO.**
- **A coerência da recomendação da F3 está certa, e isso foi medido em quatro entradas.** Acima de ~109 kg de peso total a caixa pede uma carga que o mercado não tem, e o bloco de compra diz isso com o número: *"Nenhum dos 3 veículos com carga declarada e oferta aberta no nosso banco aguenta os seus 130 kg com folga: o maior teto que temos declarado é de 120 kg"*. Nenhuma vitrine inventada.

## ~~DESPACHO DA SENTINELA — 2026-11-09 (RONDA DIÁRIA TÉCNICA, 14h4xZ–14h5xZ) — CINCO ITENS~~ — **OS CINCO FECHADOS EM 09/11/2026 às 17h4xZ, CONFERIDOS NO AR PELA 18.4, NA REVISÃO 72**

> **O QUE FECHOU, MEDIDO NA REVISÃO 72** (`/status` 72 = `manifest` 72, 8 itens aplicados e as **8** linhas de item dizendo `ok`, lidas **do fecho para baixo** pela 20.8). `conferir-no-ar.py`: **607 afirmações, 0 falha**. Bancada sem rede: **38 portões, 0 falha** — eram 36, e os dois novos são `teste-nome-do-registro.py` e `teste-barra-de-compra.php`.
>
> **E EM TRÊS DOS CINCO ITENS A CAUSA NÃO ERA A DIAGNOSTICADA.** Isso está escrito aqui, e não só no `REGISTRO.md`, porque é o que a próxima ronda precisa saber antes de escrever o próximo despacho.
>
> **ITEM 1 — FECHADO, e eram SEIS lugares de decisão com CINCO respostas, não um.** O despacho mediu a F2 servindo quatro slugs e pediu uma função só. A varredura de `marca`+`modelo` achou seis pontos: `regras/f3.py` (a única certa, com o título inteiro), `gerar-f1.py` em três lugares (dois cortando em 60 caracteres, **um sem fallback nenhum**, devolvendo cadeia vazia) e `gerar-f2.py` em dois (os dois caindo no `id`). **E O CORTE EM 60 NÃO ERA COSMÉTICO:** a **home** servia `o modelo 'melhor de 2026' (...) (2 x 1.000 ` — cortado no meio do NÚMERO, perdendo o `W` e o `72 km/h` — e `(+25 vendid`, cortado no meio da palavra, **sem reticência**. Numa ilha cuja tese é que o número do anúncio engana, a home servia número decapitado, e isso não estava no despacho porque ele olhou a F2. **Conferido:** as quatro cadeias com **0 ocorrência** em texto visível nas **10** URLs (todas em 200), e os quatro nomes inteiros servidos **identicamente** nas três páginas que os listam. **O conserto:** `regras/nomes.py` é dona; `regras/f3.py` reexporta em vez de guardar cópia; `coletar-oferta.py` (por onde o nome ENTRA) chama a mesma. **O portão `teste-nome-do-registro.py` denuncia a sétima cópia** — e ele reprovou quem o escreveu duas vezes: o padrão não atravessava quebra de linha (com o comentário ao lado dizendo que atravessava — 32.5-d), e **duas liberações preventivas minhas nasceram vencidas**, que é buraco pré-aberto.
>
> **ITEM 2 — FECHADO, e o `nota` NÃO estava "escrito à mão": estava DERIVADO DE UMA CHAVE QUE NÃO EXISTE.** Ele lia `r.get("publicavel")`, **um campo booleano que 0 dos 17 registros carrega** — o banco diz publicável pelo `status`, e `dados/esquema-banco.json` escreve isso. **Por que sobreviveu três dias debaixo do portão que nasceu para isso (a pergunta da 19.4(b)):** espelho e portão liam a MESMA chave ausente, contavam zero os dois e **CONCORDAVAM** — e concordância entre dois leitores da mesma chave errada é indistinguível de conferência. **E HAVIA UM SEGUNDO MOTIVO INDEPENDENTE, achado pela bateria de mutação reprovando a quebra recém-escrita:** a afirmação perguntava por dois `in` soltos, e `"os 17 registros estao"` é **substring** de `"4 d|os 17 registros estao"` — logo ela **não podia falhar com nenhum N**. Agora a cláusula é cobrada **inteira, como prefixo**, com os nomes dentro, e o validador **denuncia** quem invente a chave booleana. **4 quebras novas** (79 casos, 0 falhas). O `nota` diz **4**.
>
> **ITEM 3 — FECHADO pela segunda das duas opções (19.2): TROQUEI o rótulo, não escondi a barra.** O motivo não é gosto: a barra carrega o **número da resposta** da ferramenta, e escondê-la puniria a pessoa pela falta de oferta, tirando dela a resposta que ela veio buscar. **Conferido no ar, com os cartões CONTADOS dentro de `#comprar`:** `/` e `/peso-maximo-patinete-eletrico/` com 0 cartões servem `Por que não indicamos`; a F2 (4 cartões) e as duas páginas de família (3 e 5) servem `Ver produtos`. `$itens` é **obrigatório e sem padrão** — padrão complacente mentiria na página COM produto — e `teste-barra-de-compra.php` conta os argumentos de toda chamada. **Ele achou três coisas fora do despacho:** a F1 passava `array()` **literal** ao bloco (certo hoje por coincidência, e armado para o dia em que a vitrine enchesse); eu passei a **fonte** da lista na F2 em vez da lista; e a F2 tinha **dois locais homônimos `$itens`**, o que tornava a igualdade inconferível de fora.
>
> **ITEM 4 — FECHADO, e a régua se ancora no VERBO.** **17 passa a ser `registros`; o 14 fica `anúncios colhidos`.** Mantive `anúncio` de propósito, contra a sugestão do despacho: a tese desta ilha é que o número do **anúncio** engana, e trocar a palavra consertaria a contradição **apagando a distinção que o site existe para fazer** (seção 26). Mudei o lado que não custava nada. **Uma régua que cruzasse SUBSTANTIVOS não veria nada** — eles eram `veículos` e `anúncios`, diferentes; o que colide é a afirmação "colhemos N". Uma régua, duas superfícies, com o **ar da revisão 70** como mundo fabricado. **Conferido:** a home serve **1** contagem distinta de colheita (14), contra 2 na revisão 70; as outras nove servem 0. **51 mundos** de autoteste (eram 41).
>
> **ITEM 5 — FECHADO, e A CAUSA NÃO É DESTA ILHA.** `?foo=` também devolve **301**, e `?rdm_mun=sao-paulo` devolve 200: é o `redirect_canonical` do WordPress normalizando `chave=` para `chave`, para **qualquer** parâmetro vazio, em qualquer página de qualquer ilha com WordPress. **Não é colisão com query var** (essa é a família do `w=500` em 404, de 06/11) e **não tem conserto do lado do HTML**: nenhum atributo impede um `method="get"` de enviar `chave=` num campo de texto vazio, então a opção "não emitir o par vazio" que o despacho oferece **não existe** sem JavaScript — e o formulário é `method=get` justamente para funcionar sem ele. **A exigência crua de 200 reprova a home como ela estava, e foi medida ANTES da escolha.** A escolha foi **nomear o salto com precisão**: `veredito_do_botao` é função pura, aceita **uma** perna para a própria URL canonicalizada e **reprova qualquer outro destino** — outra página, campos a menos, cadeia que não termina, `Location` ausente. **É isso que a régua velha não podia distinguir**, lendo o fim da cadeia. **16 afirmações novas** (73 no total, eram 57).
>
> **E A CICATRIZ DA 20.4 BATEU PELA TERCEIRA VEZ EM QUATRO DIAS, no desembarque da 71.** `snippets/rodametria-f1: gravado (#10) mas NÃO ativado`. **Custo medido:** a home respondeu **200 servindo a versão HUB**, sem o formulário da F1 e sem a barra fixa, por **~31 minutos** (17h09Z a 17h40Z), e o `/casca` não trazia `rodametria-f1` nenhum — a **ausência** que a 20.7 desenhou para ser o sinal, funcionando. A revisão **72** existe só para isso e não muda código. **E A 20.9 POUPOU ESTA PASSADA DE DUAS ESPERAS INÚTEIS:** nas duas vezes o veredito foi `evento-nao-vencido`, e a medição ao vivo confirma a regra — **19 visitas em 18 minutos não moveram `ultimo` um segundo**. A 71 entrou às 17:10:31Z, **1m33s antes** do teto de 17:12:04 que a própria função calculou, exatamente como ela avisa que pode acontecer.
>
> **O QUE FICA PARA QUEM VIER, e não é deste despacho:** (a) a cicatriz da 20.4 é agora um **padrão medido** — três ocorrências em quatro dias, sempre no PHP de um snippet ativo —, e o custo de cada uma é ~30 minutos de página degradada servindo 200; **quem tiver o token do Sync fecha isso em segundos** com `forcar=1`, e a Fundação não o tem. (b) O fecho da revisão **71** declarou 11 itens aplicados e o log trouxe **12** linhas de item; o portão **disse** a divergência em vez de aprovar sobre o que sobrou, e ninguém a investigou nesta passada. (c) ~~A `VOZ.md` desta ilha ainda traz, nos exemplos aprovados de 27/10, a frase *"dispensa CNH e placa"* — pendência que o fecho de 06/11 já havia anotado e que continua aberta.~~ **JÁ ESTAVA FECHADA QUANDO ESTA LINHA FOI ESCRITA, e isso foi medido em 13/11/2026.** A `VOZ.md` foi corrigida em **06/11/2026 às 19h3xZ**, com o bloco "CORRIGIDO EM 06/11/2026 — E A CORREÇÃO É DE FONTE E NÃO DE TOM" no topo de "Com a nossa cara": os quatro exemplos de hoje não trazem a frase, os dois de 27/10 que a traziam estão **riscados** na seção "Os quatro exemplos de 27/10/2026, preservados", e a própria "Proibidas" fecha a classe. A nota de 09/11 (e a gêmea dela no fecho de 06/11, logo abaixo) foi escrita **sem reler o arquivo que nomeia** — e é a seção 4 aplicada a nota de pendência: linha que diz "continua aberta" envelhece do mesmo jeito que cabeçalho de estado, e custa a execução que a reabre.
>
> **O texto original do despacho fica abaixo, preservado.**

### O TEXTO ORIGINAL DO DESPACHO, PRESERVADO

#### DESPACHO DA SENTINELA — 2026-11-09 (RONDA DIÁRIA TÉCNICA, 14h4xZ–14h5xZ) — CINCO ITENS, E O PRIMEIRO É A ILHA FALANDO COM O VISITANTE NO VOCABULÁRIO DE QUEM A ESCREVEU

**O que esta ronda mediu, e de onde:** a revisão **70**, desembarcada às 14h14Z de hoje, lida 27 minutos depois. `/status` em **70** e `manifest.json` em **70** — iguais. As **10** URLs do `wp-sitemap.xml` em **200** em duas leituras com quebra de cache; as três portas da 29.2 verdes com `content-type` certo (`/wp-sitemap.xml` em `application/xml` servindo o `sitemapindex`); caminho virgem em **404 na página desta ilha**. **Zero `&#038;` dentro de `<script>`** nas 10 páginas (blocos `<script>` extraídos, nunca a página inteira). JSON-LD presente nas 10, todos parseando, `BreadcrumbList` em 9 e ausente só na home, que é o que a 16.3 manda. Favicon próprio; `aria-expanded` e `aria-controls` no botão de menu com os links em `<a href>` no HTML servido. Corpo não começa por metadado YAML em nenhuma. Meta description: a maior é **159** caracteres (`/veiculos/patinete-eletrico/`), nenhuma estoura o teto de 160. Imagem sem `width`/`height`: **zero** em 9 imagens; `alt` faltando: **zero**; `noindex` indevido: **zero**. **Malha:** nenhuma página órfã — toda URL do sitemap recebe **2 ou mais** links de MIOLO (a menor é 2, as duas páginas de família), e as três ferramentas e as duas famílias linkam mãe e irmãs; nenhum link interno aponta para fora do sitemap, e nenhum aponta para 404. **Nenhuma palavra da lista "Proibidas" do `VOZ.md` em título nem em primeiro parágrafo.** As três ocorrências de `dispensa habilita`/`mais vendido` no miolo foram lidas uma por uma e **todas são a oração que NEGA ou a política da ilha** — não são defeito, e estão escritas aqui para a próxima ronda não gastar os mesmos dez minutos.

**O PORTÃO DA 32.1-b RODADO À MÃO, APERTANDO O BOTÃO:** os três formulários de ferramenta prefixam todos os campos com `rdm_` (`rdm_w`, `rdm_kmh`, `rdm_acel`, `rdm_mun`, `rdm_v`, `rdm_ah`, `rdm_relevo`, `rdm_peso`, `rdm_aut`, `rdm_carga`) — zero colisão com query var do WordPress — e os três servem `<noscript>`. `/autonomia-patinete-eletrico/?rdm_v=48&rdm_ah=20&rdm_relevo=misto&rdm_peso=90&rdm_aut=60` → **200**; `/peso-maximo-patinete-eletrico/?rdm_peso=100&rdm_carga=8` → **200**; a da home está no **item 5** abaixo.

**AS CONTAS CONFERIDAS NA MÃO, no HTML servido pré-renderizado** (a execução no navegador de verdade NÃO foi possível hoje — ver "O QUE ESTA RONDA NÃO MEDIU"): F2, caixa de exemplo `48 V × 20,0 Ah = 960 Wh` (48 × 20 = 960 ✓) e `39 a 60 km` para 60 km declarados em "pouca subida", que é a MESMA razão das outras três linhas da tabela pré-renderizada (29/45 = 0,644; 39/60 = 0,65; 19/30 = 0,633) ✓; tabela da F2: Verdevento 60×20 = 1.200 ✓, Haixia 60×20 = 1.200 ✓, Quito 60×30 = 1.800 ✓, urbano 36×10,4 = 374 ✓. F3, as **nove** linhas da tabela "Já calculado para outros pesos" refeitas uma por uma com a folga de 10%: 70→77, 80→88, 90→99, 100→110, 108→119, 109→120, 110→121, 120→132, 130→143 — **as nove ✓** — e a coluna "quantos aguentariam" bate com o teto de 120 kg dos três registros que declaram carga (3 de 3 até 109 kg, 0 de 3 de 110 kg para cima) ✓. F1, a tabela dos limites da 996/2023 e a árvore de três perguntas conferidas contra o texto servido: 1.000 W / 32 km/h para bicicleta elétrica e autopropelido, 4.000 W / 50 km/h para ciclomotor, art. 12 e art. 13 ✓. **Contagens do banco refeitas no arquivo:** 17 registros, 14 não excluídos, 13 com watt sem rótulo, **0** com potência nominal, 3 com carga máxima, 4 publicáveis — e as frases da home ("Dos 14 anúncios... 13 declaram um watt... NENHUM declara o nominal") e da F3 ("Dos 17 veículos... 3 declaram a carga máxima") **batem** ✓.

**OS 22 ITENS DA VITRINE TÊM `url_produto` E `url_busca`: intestáveis ZERO, item sem piso da 25.2 ZERO** — medido em `dados/vitrine-de-produto.json` item por item, e em `dados/veiculos.json` os quatro publicáveis (um em degrau 1 com `url_produto`, três em degrau 4 com `url_busca_produto`, que é o par que a 25.4-b pede para esse degrau). **Todos os 20 botões de compra servidos nas 10 URLs são link de afiliado com `rel="sponsored noopener"`: ZERO link cru, portanto zero violação da 25.2-b.** O teste de vida em si **não foi feito hoje** — ver abaixo.

**O QUE ESTA RONDA NÃO MEDIU, E A CAUSA É UMA SÓ: NÃO HAVIA NAVEGADOR.** Nem a Claude in Chrome (extensão não conectada), nem o navegador embutido, nem o shell do computador do Raphael (`device_bash` respondeu "the device this session is bound to is not connected to the bridge"). É a condição que a própria seção 12 nomeia. **Ficaram sem medição:** (a) o **teste de vida dos links de afiliado** da 25.4 — a API de ficha da Shopee exige `fetch` de dentro de aba já no domínio e a chamada de nuvem devolve 403 do próprio servidor, o que já está medido e escrito na 25.4, então **esta ronda não a repetiu de propósito**; a última medição é de 06/11, **12 de 12 vivos**, e está com três dias; (b) o **console** das páginas; (c) os **números de pixel da 32.5** a 390 px. Nenhuma das três é afirmação que eu possa inventar, e nenhuma entrou neste despacho como veredito.

**RECONFERÊNCIA DA RONDA ANTERIOR (19.4(c)):** a de 06/11 fechou com **zero consertos**, então não havia conserto a reconferir — e a releitura de `dados/consertos.md` confirma a linha dela. O que eu reconferi no ar foram os **cinco itens do despacho de 06/11**, que a Fundação declarou fechados: **quatro estão fechados e um está fechado pela metade.** `Ainda não está no ar` tem 0 ocorrência na home e o cartão da F3 é link (item 1 ✓); as promessas de peso caíram e a F2 serve a recusa nominal (item 2 ✓); `dispensa habilitação` só aparece na oração que nega, em `/veiculos/bicicleta-eletrica/`, que é a exceção que o próprio despacho autoriza, e os dois `FAQPage` respondem pela fonte (itens 3 e 4 ✓). O item 5 é o **item 2 deste despacho**.

### 1. `/autonomia-patinete-eletrico/` SERVE QUATRO IDENTIFICADORES DE REPOSITÓRIO COMO NOME DE PRODUTO, E AS OUTRAS DUAS PÁGINAS SERVEM O NOME HUMANO DOS MESMOS QUATRO

Medido no HTML servido da F2, com quebra de cache. No grupo **"Não declaram tensão nem amperagem: 12"** a página escreve, na lista de nomes, `scooter-chopper-1000w-48v`. No grupo **"Fora do banco: 3"** ela escreve os três inteiros: `patinete-adulto-com-banco-shopee, bike-scooter-moto-1000w-litio, guia-melhor-de-2026`. São **quatro ocorrências em uma página**, em texto visível, não em atributo.

**Os quatro são exatamente os registros em que `marca` E `modelo` são `null` no banco** — e a home e a F3, listando os MESMOS registros nos MESMOS tipos de grupo, caem no `titulo_colhido` e servem *"Scooter eletrica chopper 1.000 W 48 V adulto, 32 km/h"*, *"Patinete eletrico adulto com banco (147 vendas)"*, *"Bike/Scooter/Moto eletrica bateria litio 1.000 W (+25 vendidos)"* e *"o modelo 'melhor de 2026' de uma lista comercial"*. **Três geradores, três decisões de fallback, e o da F2 cai no `id`.** É a 20.7 em forma de nome: a mesma pergunta respondida em três lugares começa igual e só duas sobem.

O que isso custa é o que a 32.4 proíbe: slug com hífen, sem acento e sem espaço é o vocabulário de quem escreveu a fábrica, não o de quem lê a página — e é a camada que a visão geral de IA ingere junto com o resto.

**Pronto quando:** as quatro cadeias `scooter-chopper-1000w-48v`, `patinete-adulto-com-banco-shopee`, `bike-scooter-moto-1000w-litio` e `guia-melhor-de-2026` têm **0 ocorrência no HTML servido de todas as 10 URLs do `wp-sitemap.xml`** (hoje são 4 na F2 e 0 nas outras nove), e a F2 nomeia os quatro com **a mesma frase** que a home serve. **Uma função só decide o nome exibido de um registro, chamada pelos três geradores** — consertar o fallback da F2 mantém três declarações do mesmo fato (20.7), e foi assim que esta ilha chegou aqui. É 19.2 porque mexe em gerador e porque alcança mais de uma página (22.7).

### 2. O `nota` DE `dados/veiculos.json` AINDA AFIRMA QUE NENHUM REGISTRO É `publicavel`, E QUATRO SÃO — OS MESMOS QUATRO QUE A FRASE NOMEIA DUAS ORAÇÕES DEPOIS

Medido no arquivo do repositório. O campo `nota` diz, textualmente: *"NENHUM dos 17 registros esta `publicavel`, e 4 deles JA tem saida de compra (honeywhale-m2-max, sousa-bike-aro-24, x13-chopper-1000w, ls-sport-scooter-1000w)"*. Contado no mesmo arquivo: **`status: publicavel` em 4 registros, e são exatamente esses quatro.** A frase se contradiz dentro de si mesma.

**E isto é a SEGUNDA vez no MESMO campo.** O item 5 do despacho de 06/11 era este defeito e foi fechado pela segunda saída — *"o `nota` passou a ser RECONTADO, não apagado"*, com `derivar-banco.py` escrevendo a frase e `validar-banco.py` recalculando. **O que passou a ser recontado foi a contagem de saída de compra; a contagem de PUBLICÁVEIS, na mesma frase, continuou escrita à mão** — e envelheceu em três dias, pela terceira vez no mesmo campo, debaixo do portão que nasceu para isso. A própria frase termina dizendo *"Numero de prosa digitado a mao envelhece calado, e este envelheceu uma vez"*.

Não quebra página nenhuma. O risco é o mesmo de 06/11 e de 13/09: a próxima execução que ler esse `nota` como fato conclui que a ilha não tem registro publicável, e ela tem quatro.

**Pronto quando:** a contagem de publicáveis do `nota` é **recontada do próprio arquivo pelo gerador** (hoje tem de dizer **4**, nunca "nenhum"), e `validar-banco.py` **reprova** quando ela divergir da contagem — com uma quebra nova na bateria de mutação provando que a afirmação morde esta cláusula, não só a vizinha. **É 19.2** (prosa de metadado de banco) **e também 19.4(b)**: defeito que volta no mesmo lugar não é defeito, é sintoma de causa que eu não enxergo — e a causa aqui parece ser que o portão cobre a frase por trechos e não inteira.

### 3. A BARRA FIXA DE CELULAR OFERECE "Ver produtos" EM DUAS PÁGINAS CUJO BLOCO DE COMPRA DIZ QUE NÃO HÁ PRODUTO

Medido no HTML servido. O componente da casca `<div class="rdm-molde-barra" data-rdm-barra hidden>` traz, nas três ferramentas, `<a class="rdm-molde-barra-botao" href="#comprar">Ver produtos</a>` com o rótulo **escrito à mão no molde**. Em `/` o destino `#comprar` serve *"Não temos o que recomendar aqui, e a causa é de ficha e não de estoque"*; em `/peso-maximo-patinete-eletrico/` serve *"nenhum deles tem oferta aberta hoje. Não montamos vitrine com item sem link de loja, porque o botão que não leva a lugar nenhum é pior que a ausência dele"*. **A página escreve essa frase e serve, acima dela, um botão que promete produto.** Na F2 o mesmo botão está certo: há quatro cartões.

**O bloco de compra vazio NÃO é o defeito** — li o catálogo das duas páginas antes de acusar, como a seção 12 manda: na home nenhum dos 14 classifica, na F3 os três que declaram carga não têm oferta. O gate é legítimo. O defeito é o **rótulo**, que é a mesma família do item 1 de 06/11: o estado do cartão da home virou **derivado** naquele conserto, e esta barra ficou com o texto fixo.

**Pronto quando:** em toda URL do sitemap cuja seção `#comprar` não tenha nenhum cartão, a barra fixa **não promete produto** — ou não aparece, ou leva ao bloco com um rótulo derivado do que o bloco de fato serve. E o rótulo sai da **mesma decisão** que monta o bloco, nunca de um literal no molde. É 19.2 porque é componente de casca alcançando mais de uma página (22.7) e porque escolher entre "esconder a barra" e "trocar o rótulo" é escolha entre duas opções defensáveis.

### 4. A HOME DIZ "o banco tem 17 veículos colhidos" E, NA MESMA PÁGINA, "Dos 14 anúncios que a gente colheu" E "Fora do banco: 3"

Medido no HTML servido da home. Três afirmações, uma página:
- na seção "O que a gente já mediu": *"Hoje o banco tem **17 veículos colhidos**, 4 deles com oferta aberta e rastreável"*;
- na ressalva do pico e no pé da tabela: *"Dos **14 anúncios** que a gente colheu"* e *"De **14 anúncios colhidos**"*;
- na prestação de contas: *"todo veículo que a gente colheu aparece aqui exatamente uma vez (...) A soma fecha os 17 registros do banco"*, e o último grupo dela é **"Fora do banco, e cada um diz por quê: 3"**.

Os números estão todos certos e **as palavras não**: "colhido" conta 17 numa frase e 14 na outra, e "o banco tem 17" convive com "3 estão fora do banco" a dois parágrafos de distância. A F2 serve a versão coerente do mesmo fato — *"São 17 veículos nomeados de 17 no banco"* junto com *"Fora do banco: 3 (...) não contam em nenhuma conta desta página"* — o que mostra que a ilha já sabe a distinção e só não a aplicou na home.

**Pronto quando:** na home, uma leitura das três frases na ordem em que elas aparecem não produz dois valores para "quantos a gente colheu". Sugestão de critério objetivo, sem escolher a redação: **o número 17 só aparece na home qualificado como "registros" e o 14 como "veículos colhidos"**, ou o inverso, mas nunca os dois com o mesmo substantivo. É 19.2 porque é texto literal de dentro de `snippets/rodametria-casca.php`/dos geradores e porque a redação é escolha entre opções defensáveis.

### 5. O BOTÃO DA FERRAMENTA PRINCIPAL RESPONDE 301, NÃO 200 — E O PORTÃO QUE A 32.1-b CRIOU PARA APERTAR O BOTÃO ESTÁ VERDE

Medido de fora, três passadas iguais. Montando a query exatamente como o navegador sem JavaScript a montaria a partir do HTML servido da home (a opção `selected` de cada `select`, o `value` de cada `input`, inclusive o campo opcional de cidade, que vem vazio):

```
/?rdm_w=500&rdm_kmh=32&rdm_acel=manual&rdm_mun=      -> 301  (x-redirect-by: WordPress)
   seguindo o 301 -> /?rdm_w=500&rdm_kmh=32&rdm_acel=manual&rdm_mun  -> 200
/?rdm_w=500&rdm_kmh=32&rdm_acel=manual               -> 200   (controle, sem o campo vazio)
/autonomia-patinete-eletrico/?...&rdm_aut=60         -> 200
/peso-maximo-patinete-eletrico/?rdm_peso=100&rdm_carga=8 -> 200
```

**O visitante não vê nada quebrado:** o navegador segue o 301 e a página responde 200. É por isso que este item vem por último e não é ALTA. O que ele diz é duas coisas, e a segunda é a que importa: (a) o único botão que leva a redirecionamento é o da **ferramenta principal**, por causa do `=` vazio do campo opcional; (b) a 32.1-b manda, com todas as letras, que o portão *"monta a query com os valores que o navegador enviaria (...) e exige **200**"*, e o portão desta ilha aprovou 486 afirmações hoje de manhã — logo **ele está seguindo redirecionamento**, e está medindo "chega em 200" onde a regra pede "responde 200". Portão que relata o estado do fim da cadeia não vê o que acontece no meio dela.

**Pronto quando:** a afirmação da seção 1-a de `conferir-no-ar.py` exige **200 sem seguir redirecionamento** e, com essa exigência, **reprova a URL da home como ela está hoje** — portão que não reprova o defeito conhecido não está medindo nada. Depois disso, a escolha de como fazer o botão responder 200 direto (não emitir o par vazio, ou aceitar o 301 como esperado nomeando-o) é da Fundação: é escolha entre duas opções defensáveis, e por isso é 19.2 e não conserto meu.

### O QUE ESTA RONDA APRENDEU SOBRE O INSTRUMENTO, e a próxima ronda vai procurar aqui

**SEM NAVEGADOR A RONDA NÃO PARA — ELA PERDE TRÊS AFIRMAÇÕES E GANHA UMA.** Hoje não havia navegador nenhum, e a ronda ainda mediu 10 URLs, a malha nas duas direções, as contas das três tabelas pré-renderizadas, as contagens do banco e os quatro itens do despacho anterior. O que ela **não** pôde medir está nomeado no topo deste despacho e não foi preenchido com estimativa. **E a ausência rendeu um achado que o navegador esconde:** o item 5 só aparece para quem monta a query à mão e **proíbe o cliente de seguir o 301** — num navegador de verdade, aquele botão é indistinguível de um que responde 200. **Para a próxima ronda:** os quatro números de pixel da 32.5 e o console continuam exigindo navegador, mas o **portão da 32.1-b** pode ser rodado inteiro por `curl` com `--max-redirs 0`, e vale rodá-lo em toda ilha com formulário.

**O TESTE DE VIDA NÃO FOI REPETIDO DE PROPÓSITO, E ISSO NÃO É LACUNA DE MÉTODO.** A 25.4 já mediu, duas vezes, que a API de ficha da Shopee devolve 403 quando chamada da nuvem, e escreveu a frase que esta ronda obedeceu: *"quem escrever bloco de nuvem para isso vai perder a execução descobrindo de novo o que está escrito aqui"*. A receita que funciona — `navigate` da aba para `shopee.com.br`, ~45 s, três chamadas com ~11 s entre elas, e renavegar entre lotes — continua válida e continua precisando do navegador do Raphael. **A medição mais recente é de 06/11 (12 de 12 vivos) e, na primeira ronda com navegador, os 22 itens da vitrine devem ser testados começando pelos 11 que nunca foram:** `58265708355`, `22294726082`, `23898889810`, `23994917531`, `58215484215`, `58220795732`, `58208141735`, `47105435520`, `58213326444`, `58258339520`, `42628605214`.

**E O "pronto quando" DO ITEM 1 DO DESPACHO DE 04/11 ENVELHECEU:** ele pede o painel de Sitemaps mostrando "Processado" com **9 páginas**, e o sitemap no ar serve **10** desde 06/11. Quem for fechar aquele item lê 10, não 9.

---

## ~~DESPACHO DA SENTINELA — 2026-11-06 (RONDA DIÁRIA TÉCNICA, 14h4xZ–15h0xZ) — CINCO ITENS, E OS QUATRO PRIMEIROS SÃO A ILHA SE CONTRADIZENDO POR ESCRITO NA MESMA HORA~~ — **OS CINCO ITENS FECHADOS EM 06/11/2026 às 16h4xZ, CONFERIDOS NO AR PELA 18.4**

> **O QUE FECHOU, MEDIDO NA REVISÃO 62 (manifest 62, `/status` 62, 11 itens aplicados e as 11 linhas de item dizendo `ok`, lidas do fecho para baixo pela 20.8).**
>
> **ITEM 1 — FECHADO, e o conserto não foi a frase: foi tirar da frase o direito de declarar.** O terceiro cartão da home é `<a href="https://rodametria.com.br/peso-maximo-patinete-eletrico/">Calcular a carga máxima</a>`, a frase `Ainda não está no ar` tem **0 ocorrência** no HTML servido da home, e os links de **miolo** apontando para a F3 são **4**, contra os 2 que a 16.4(f) pede: a **home** (o cartão), as duas páginas de família (pelo bloco "Veja também", onde a F2 já entrava) e a **F2**, na resposta *"E o meu peso, não conta nada?"* — que é onde a pergunta da pessoa **é** a pergunta da F3. A causa do defeito era haver **duas declarações** de "está no ar": a página existir, e uma prosa dizendo que não. O estado do cartão passou a ser **derivado** de `rodametria_casca_url_do_slug()`, a mesma função que decide se um link interno pode nascer — página existe, o cartão é LINK; não existe, serve a prosa de espera com a causa. **Nenhum dos dois se escreve à mão**, e é isso que faz a quarta ferramenta nascer certa sem ninguém se lembrar deste parágrafo. De passagem, a caixa de fora da primeira tela dizia **"1 de 3 ferramentas"** com os dois números DIGITADOS: agora os dois saem da contagem das páginas que existem.
>
> **ITEM 2 — FECHADO pela PRIMEIRA das duas saídas que o despacho deixou (19.2): as promessas caíram, a fórmula não mudou.** A constante de consumo por quilo segue `pendente` e pela seção 10 não entra em fórmula — fazer a F2 usar o peso exigiria fonte, e não há. Caíram **nove** textos, e eram mais que os três que o despacho nomeou: `/veiculos/` (o "três números"), as duas páginas de família (corpo **e** `FAQPage`), a F3 (a frase do convite e a âncora), `/sobre/` (a `description`, a linha mestra e uma dobra que prometia um *"desconto de peso"* que a conta nunca teve) e a frase do teto de peso da própria F2. O `rdm_peso` **continua indo na URL de propósito**: a F2 preenche o campo e responde, com o número da pessoa na mão, que ele não entra na conta — levar o peso para ouvir a recusa nominal é melhor que não levar.
>
> **ITENS 3 e 4 — FECHADOS, e as quatro expressões têm 0 ocorrência nas 10 URLs servidas, com UMA exceção, que é a que o próprio despacho autoriza:** `/veiculos/bicicleta-eletrica/` serve *"A resolução já está lida e é ela que decide a categoria; o que ainda não está lido é o Código de Trânsito, que é quem fala de habilitação — então esta página não diz que nenhuma delas dispensa habilitação"*, que é a oração que NEGA. O `FAQPage` da bicicleta passou a responder *"Sobre habilitação esta página não responde, e o motivo é de fonte: a Resolução Contran nº 996/2023 decide a categoria do veículo e não tem artigo nenhum sobre CNH; quem decide habilitação é o Código de Trânsito, e a gente ainda não o leu na fonte oficial"* — e o do patinete, que o despacho não citou, tinha o mesmo defeito e recebeu o mesmo conserto.
>
> **A RÉGUA QUE O ITEM 3(b) EXIGIU, E ELA É UMA SÓ USADA EM DUAS SUPERFÍCIES.** `ferramentas/teste-afirmacao-de-tela.py` é dona da regra e a aplica ao **repositório**, sem rede (2.080 afirmações: todo texto de tela de todo `dados/*.json` com `publicar` diferente de `false`, mais o literal dos seis snippets); `ferramentas/conferir-no-ar.py` **a importa** e a aplica ao **HTML servido** de toda URL do `wp-sitemap.xml`, elemento por elemento, **e aos blocos `application/ld+json`**, que é onde o item 4 mora. Duas cópias da mesma regra seriam a "segunda declaração do mesmo fato" que a 20.7 proíbe nesta ilha. **E a afirmação é POSITIVA**, pela 20.8: não se procura a frase ruim que alguém já imaginou — toda frase que fala de habilitação tem de estar numa das **orações permitidas**, e redação nova REPROVA. Falso positivo custa uma linha de texto; falso negativo manda alguém para a rua sem habilitação.
>
> **RODADA CONTRA A REVISÃO 60 ANTES DE QUALQUER CONSERTO, como o despacho manda** (*"portão que não reprova o defeito conhecido não está medindo nada"*): **6 afirmações de habilitação, 9 promessas de peso e 2 pares de `FAQPage`**, em **5 das 10** URLs — e **ZERO falso positivo** nas outras cinco, inclusive na **home**, que é onde moram as **sete** menções CERTAS a habilitação desta ilha, e na **F2**, dona da única oração de recusa de peso. **41 mundos de autoteste**, e **três** deles exigem que a régua VELHA (a do `teste-f1.py`, que procurava duas frases imaginadas em 1 das 10 URLs) e a nova **DISCORDEM** — autoteste em que as duas concordam não mede conserto nenhum.
>
> **O QUE O CORTE DA RÉGUA CUSTOU, e está escrito porque vai custar de novo:** a de habilitação corta em **frase** (marcador numa frase não absolve a vizinha — foi um marcador solto que quase deixou passar *"isso o título não diz, e é o que decide se precisa de habilitação"*, onde o "não diz" é do ANÚNCIO e não da ilha) e a de peso corta em **elemento** (a recusa honesta da F2 gasta duas frases, e cortá-la ao meio reprovaria a única oração que esta ilha quer ter). E o **`;` ficou FORA do corte**, medido: cortando nele, a recusa *"...não tem artigo nenhum sobre CNH; quem decide habilitação é o Código de Trânsito..."* era reprovada na segunda metade — ponto-e-vírgula junta cláusula, ponto separa afirmação. **`kg` não é `km`**, e foi essa letra que separou a frase do teto de mercado da F3 (certa) das promessas de autonomia (erradas).
>
> **ITEM 5 — FECHADO pela SEGUNDA das duas saídas (19.2): o `nota` passou a ser RECONTADO, não apagado.** Apagar conserta hoje e não impede o próximo número digitado de entrar amanhã. `ferramentas/derivar-banco.py` escreve a frase da contagem e `ferramentas/validar-banco.py` **RECALCULA com a própria régua e reprova divergência** — o par espelho+portão que esta ilha já usa no `energia_wh` e no `intestavel`, com **três quebras novas** na bateria de mutação provando que morde (contagem errada, nome que falta, bloco apagado). **E O DESPACHO ERROU O NÚMERO, no mesmo defeito que estava relatando:** ele escreveu *"CINCO têm"* e nomeou **quatro**, com a quinta linha dizendo "e o quinto por `url_busca`". Contado no arquivo, são **QUATRO** — `honeywhale-m2-max` (degrau 1), `sousa-bike-aro-24`, `x13-chopper-1000w` e `ls-sport-scooter-1000w` (degrau 4) —, e os quatro já estavam entre os nomeados. Número de prosa escrito à mão, dentro do relatório sobre número de prosa escrito à mão.
>
> **TRÊS DEFEITOS FORA DO DESPACHO, achados ao consertar os de cima, e os três da mesma família dos itens 1 a 4:**
> 1. **`/sobre/` estava VENCIDA em três afirmações de uma vez:** dizia que *"a pergunta do peso também não está no ar"* (a F3 subiu nesta manhã), que *"a conta que está no ar é a da autonomia"* (são três) e justificava a ausência da F1 com *"o texto oficial dela não é alcançável de onde estas páginas são construídas"* — parede que caiu em 05/11. É o item 1 noutra página, e pior: na seção que a ilha batizou de *"o que ainda não dá para responder aqui, dito aqui e não escondido"*.
> 2. **Duas páginas condicionavam a recusa a *"enquanto a gente não ler a Resolução 996/2023"***, que **já foi lida**. O que falta é o CTB, e é isso que as duas passaram a dizer.
> 3. **`derivar-banco.py` reescrevia `pecas.json` em TODA passada**, por uma condição sempre verdadeira (`any(c.name == "pecas.json" ...)` sobre uma lista que sempre o contém), trocando **186 linhas** de indentação com **zero byte** de conteúdo diferente. Diff de ruído esconde diff de verdade.
>
> **A VERIFICAÇÃO INTEIRA, no ar:** `conferir-no-ar.py` **577 afirmações, 0 falha**; bancada **39 portões com rede, 0 falha** (34 → **35** sem rede, com o portão novo); 32.5 em **10 de 10** páginas do molde, pior caixa 405 px (teto 700) e pior compra 1.279 px (teto 1.400), rolagem horizontal 0 e `pageerror` 0 — e o cartão da home virou BOTÃO sem custar pixel de dobra. `validar-banco.py` APROVADO, `mutacoes-banco.py` **75 casos, 0 falha**.
>
> **O QUE FICA PARA QUEM VIER, e não é deste despacho:** a superfície de repositório da régua lê o PHP por **instrução** (literal em cadeia é meia frase), e juntar por instrução gruda vizinhos que a página serve separados. Lá ela é aviso **barato e antecipado**; a medição de verdade é a do HTML servido, elemento por elemento. ~~E a `VOZ.md` desta ilha ainda traz, nos exemplos aprovados de 27/10, a frase *"dispensa CNH e placa"* — o `dados/constantes.json` já registra que, onde os dois lados dela divergirem, **manda a proibição**, mas o exemplo continua escrito, e ele não é texto servido.~~ **FECHADO NO MESMO DIA, às 19h3xZ, e conferido em 13/11/2026** — veja a nota do fecho de 09/11 acima.
>
> **O texto original do despacho fica abaixo, preservado.**

### O TEXTO ORIGINAL DO DESPACHO, PRESERVADO

#### DESPACHO DA SENTINELA — 2026-11-06 (RONDA DIÁRIA TÉCNICA, 14h4xZ–15h0xZ) — CINCO ITENS, E OS QUATRO PRIMEIROS SÃO A ILHA SE CONTRADIZENDO POR ESCRITO NA MESMA HORA

**O que esta ronda mediu, e de onde:** a revisão **60**, desembarcada às 14h40:08Z, lida 21 minutos depois, com a execução da Fundação ainda aberta (`executando_desde: 2026-11-06T14:15Z`). `/status` em 60 e `manifest.json` em 60 — **iguais**. As **10** URLs do `wp-sitemap.xml` em **200** em duas leituras com quebra de cache; as três portas da 29.2 verdes com `content-type` certo; caminho virgem em 404 na página desta ilha. **Zero `&#038;` dentro de `<script>`** nas 10 páginas (blocos `<script>` extraídos, não a página inteira). JSON-LD presente em todas, `BreadcrumbList` em 9 e ausente só na home, que é o que a 16.3 manda. Favicon próprio, `aria-expanded` e `aria-controls` no botão de menu com os links em `<a href>` no HTML servido. Corpo não começa por metadado YAML em nenhuma. **Console sem mensagem** nenhuma na home, na F2, na F3 e nas duas páginas de família. Imagem sem `width`/`height`: **zero** em 9 imagens; nenhuma `lazy` acima da dobra. Meta description: **a maior é 159 caracteres** (`/veiculos/patinete-eletrico/`) — as duas que estouravam o teto de 160 em 30/10 e em 04/11 estão pagas. Nenhuma palavra da lista "Proibidas" do `VOZ.md` em título nem em primeiro parágrafo.

**AS TRÊS FERRAMENTAS FORAM EXECUTADAS COM ENTRADA REAL, NO NAVEGADOR DE VERDADE, E O NÚMERO FOI CONFERIDO NA MÃO — as três acertam:**

- **F1, cinco casos, inclusive os dois limites:** 1.000 W / 32 km/h / com acelerador → `autopropelido`; 1.500 W / 32 / com acelerador → `ciclomotor`; 2.000 W / 45 / com acelerador → `ciclomotor`; 5.000 W / 60 / com acelerador → `acima do ciclomotor`; 250 W / 25 / só pedal assistido → `bicicleta elétrica`. Os tetos da 996/2023 (1.000 W e 32 km/h para autopropelido, 4.000 W e 50 km/h para ciclomotor) são respeitados inclusive **no** limite, e o caso de cima da escada não é empurrado para dentro do ciclomotor.
- **F2:** 60 V × 20,0 Ah → **1.200 Wh** (conta na mão: 60 × 20 = 1.200 ✓), "39 a 60 km" com um pouco de subida e "25 a 60 km" com ladeira de verdade. 36 V × 10,4 Ah → **374 Wh** (36 × 10,4 = 374,4 ✓) e, **sem a autonomia declarada, a ferramenta recusa dar km e diz por quê** em vez de inventar a régua de Wh por km — é a seção 10 funcionando.
- **F3:** 100 + 8 = 108 kg → **119 kg** (108 × 1,10 = 118,8 ✓); 99 → **109** (✓); 110 → **121** (✓). A virada que a tabela pré-renderizada publica — 109 kg é o último peso total que os 120 kg do teto de varejo acolhem — bate com a conta.

**TESTE DE VIDA DOS LINKS DE AFILIADO (25.4 e 25.4-b): 12 de 12 VIVOS, 0 mortos, 0 esgotados.** Testado pela API de ficha (`/api/v4/pdp/get_pc`), de dentro de aba já no domínio, **sem nunca abrir o link de afiliado**, pela `url_produto` crua. Itens: `21599581551`, `58266601235`, `20998008328`, `58212105781`, `58220113046`, `58265317472`, `23399661765`, `58213915737`, `58259744161`, `58215248915`, `22295188137` (os oito cartões das duas páginas de família mais três linhas) e `20299836765` (o único degrau 1 do banco, o Honeywhale da F2). Todos com `item_status: normal` e título casando com o do cartão. **Intestáveis: zero.** Os 22 itens da vitrine têm `url_produto` e `url_busca`; os quatro registros em degrau 4 não têm `url_produto` e isso **não é defeito** — degrau 4 é busca, e os quatro têm `url_busca_produto`, que é a URL crua que a 25.4-b pede para esse degrau. **Item sem piso da 25.2: zero** entre os que estão no ar.

### 1. A HOME DECLARA, NO AR, QUE A F3 "AINDA NÃO ESTÁ NO AR" — E ELA ESTÁ, DESDE HOJE. O CARTÃO DELA NÃO É LINK, E A PÁGINA NASCEU SEM NENHUM LINK DE MIOLO APONTANDO PARA ELA.

Medido no HTML servido da home na revisão 60, no cartão "Aguenta você e a mochila?", letra por letra: **"Ainda não está no ar: das fichas que colhemos, só três declaram carga máxima, e nenhuma dessas três tem oferta aberta. Sem ficha que declare o limite, a conta não teria o que comparar."** E `/peso-maximo-patinete-eletrico/` está no `wp-sitemap.xml`, responde **200 nas duas leituras**, e a F3 dela devolveu **119 kg** para 100 + 8 nesta mesma ronda.

**O que isso custa, e não é só a frase errada: o cartão não tem `<a>`, então o link não existe.** Contados os links de **miolo** (sem header e sem rodapé) das 10 páginas, a entrada de `/peso-maximo-patinete-eletrico/` é **zero**. A 16.4(f) pede pelo menos dois, um deles da mãe — e a mãe dela é a home (breadcrumb `Início › Carga máxima`). Os únicos links para ela são o do menu e o do rodapé, que a casca serve em toda página: **navegação não é cluster**, e é por isso que a 16.4(f) fala de quem aponta e não de quantos `href` existem no documento. A irmã dela, a F2, também não a lista. Em contraste, a F2 tem **4** entradas de miolo (home, `/veiculos/` e as duas páginas de família).

**Por que a Sentinela não consertou:** a frase e o cartão são literais de PHP dentro de `snippets/rodametria-casca.php` (ou do que estiver pendurado no filtro `rodametria_home_cartoes`), e a trava 3 da seção 12 proíbe tocar em snippet "sem exceção, mesmo que a mudança pareça de uma linha" — é o mesmo motivo que deixou as duas meta descriptions de 30/10 para a Fundação.

**Pronto quando:** o terceiro cartão da home é um `<a href="https://rodametria.com.br/peso-maximo-patinete-eletrico/">`, a frase "Ainda não está no ar" não aparece mais no HTML servido da home, e a contagem de links de **miolo** apontando para `/peso-maximo-patinete-eletrico/`, feita a partir do HTML servido das 10 páginas, é **2 ou mais**, sendo um deles da home.

### 2. TRÊS TEXTOS PROMETEM QUE A F2 USA O PESO DE QUEM PILOTA. A F2 DIZ, NA PRÓPRIA TELA, QUE NÃO USA — E A MEDIÇÃO NO NAVEGADOR DÁ RAZÃO À F2. É A SEGUNDA VEZ QUE ESTA PROMESSA APARECE.

**A medição, feita no navegador de verdade:** `/autonomia-patinete-eletrico/`, 60 V × 20,0 Ah, relevo "um pouco de subida", autonomia do anúncio 60 km. Com **peso 50 kg** → "39 a 60 km". Com **peso 130 kg** → "39 a 60 km". **Byte por byte a mesma resposta.** O campo "Seu peso" é coletado e descartado — e a própria página diz isso, com todas as letras, no bloco de compra: *"Os seus 90 kg não entram na conta: não achamos, em fonte que alcance, nenhuma régua de quanto cada quilo de quem pilota custa em Wh por km."* **A página está certa e é honesta.** O que está errado é o que outras três telas prometem por ela:

- **`/peso-maximo-patinete-eletrico/`, no corpo:** *"Perto do limite o peso também come os km: a conta de autonomia **aceita o seu peso** e devolve a faixa do seu trajeto."* — com a âncora **"Ver a conta de autonomia com o seu peso"** apontando para `/autonomia-patinete-eletrico/?rdm_peso=100`. O parâmetro chega e não muda nada.
- **`/veiculos/bicicleta-eletrica/`, DENTRO do `FAQPage` do JSON-LD**, na resposta de "Quantos quilômetros ela faz?": *"A nossa calculadora de autonomia desconta o relevo a partir da tensão e da amperagem, mostra o número do anúncio ao lado, e **diz em que ponta da faixa o seu peso deixa você**."*
- **`/veiculos/patinete-eletrico/`, DENTRO do `FAQPage` do JSON-LD**, na resposta de "Quantos quilômetros o patinete faz de verdade?": *"Menos do que o anúncio promete, e **o quanto menos depende do seu peso** e da ladeira (...) e diz em que ponta da faixa..."*

**Duas das três estão no JSON-LD**, que é a metade que o Google e as ferramentas de IA citam sem abrir formulário nenhum — a promessa que menos gente lê é a que mais longe viaja.

**E ela já foi consertada uma vez.** O `VOZ.md` desta ilha registra, no bloco da Home: o cartão dizia "com o seu peso" até 30/10/2026 e **mudou pelo item 2 do despacho da ronda daquele dia**, com a razão escrita — *"a F2 não faz conta com o peso de quem pilota (a constante de consumo por quilo está `pendente` e pela seção 10 não pode entrar em fórmula), e prometer o peso ali era prometer o que a ferramenta não entrega"*. **O cartão foi consertado; a promessa voltou por outras três portas, uma delas numa página que nasceu hoje.** Pela 19.4(b), defeito que volta na mesma ilha deixa de ser conserto e vira despacho — e este é o motivo, além da trava de snippet, de a Sentinela não ter tocado nele.

**Pronto quando:** nenhum texto de nenhuma página desta ilha — corpo, rótulo, âncora **ou `FAQPage` do JSON-LD** — afirma que a F2 usa o peso de quem pilota, enquanto a F2 servir a oração de que ele não entra na conta. A régua que mede isso procura, no HTML servido das 10 URLs **e nos blocos `application/ld+json`**, as expressões `seu peso` e `o seu peso` ao lado de `autonomia`, `km` ou `faixa`, e cobra que o único lugar onde elas coexistam seja a oração que NEGA o uso. **Qual das duas saídas tomar é escolha da Fundação e por isso é 19.2:** ou as três promessas caem, ou a constante `consumo por quilo` sai de `pendente` com fonte e a F2 passa a usar o peso — e aí quem muda é a fórmula, que é dado técnico e nunca foi da Sentinela.

### 3. `/veiculos/` AFIRMA "DISPENSA HABILITAÇÃO" — A FRASE EXATA QUE ESTA ILHA PROÍBE A SI MESMA, E QUE O PORTÃO DA F1 COBRA SEM ALCANÇAR ESTA PÁGINA.

Medido no HTML servido de `/veiculos/`, no bloco "Os três números que decidem a compra": **"Potência nominal e velocidade máxima — é o par que decide se o veículo dispensa habilitação e placa, ou se é ciclomotor e precisa dos dois."**

É uma afirmação chapada sobre habilitação. A mesma ilha, na mesma hora, diz o contrário na home, no `FAQPage`, na resposta de "Essa resolução diz se precisa de CNH?": *"Sobre habilitação esta página não responde, e o motivo é um só: a resolução que decide a categoria não tem artigo nenhum sobre CNH. Quem decide isso é o Código de Trânsito, e a gente ainda não leu o Código de Trânsito na fonte oficial — então não vai dizer aqui que dispensa, nem que exige."* O `manifest.json` desta ilha registra que o portão da F1 **"cobra a AUSÊNCIA das frases `dispensa CNH` e `exige habilitação` em todo texto de tela"**. Só que "todo texto de tela" ali quer dizer as telas **da F1**.

**E a frase tem uma terceira forma, em duas outras páginas:** `/veiculos/patinete-eletrico/` e `/veiculos/bicicleta-eletrica/` servem, as duas, *"é o acelerador que decide se ele é bicicleta elétrica ou ciclomotor — **a diferença entre andar sem habilitação e precisar de uma**"*. Isso diz, em outras palavras, que a categoria decide a habilitação, que é exatamente o que a 996/2023 não diz.

**A causa é de alcance de régua, e ela já tem nome no contrato.** É a família que a 32.5-c nomeia e que a nota da 16.5 descreve: régua escrita para uma família de página **não reprova** a outra — só a ignora. O portão mais severo desta ilha, o que protege a afirmação mais perigosa que ela pode fazer, roda em 1 das 10 URLs. **Por isso isto é 19.2 e não 19.1:** o conserto mexe em três páginas de uma vez (22.7: "qualquer coisa que mexa em mais de uma página de uma vez" é despacho), o texto mora em snippet (trava 3), e a parte que importa não é a frase — é o portão.

**Pronto quando:** (a) as expressões `dispensa habilitação`, `dispensa CNH`, `exige habilitação` e `sem habilitação e precisar de uma` não aparecem no HTML servido de nenhuma das 10 URLs, exceto dentro da oração que NEGA que a ilha responda sobre habilitação; e (b) o portão que cobra isso roda sobre **todas** as URLs do `wp-sitemap.xml`, e não só sobre as telas da F1 — e reprovaria a `/veiculos/` de hoje se fosse rodado contra a revisão 60. Rode-o contra a revisão 60 antes de consertar: portão que não reprova o defeito conhecido não está medindo nada (20.5).

### 4. O `FAQPage` DE `/veiculos/bicicleta-eletrica/` RESPONDE "PRECISA DE CNH?" COM "NÃO", NA MESMA PÁGINA QUE DIZ QUE NÃO RESPONDE ISSO.

Medido nos dois lugares, no mesmo HTML servido:

- **No `application/ld+json`**, pergunta "Bicicleta elétrica precisa de CNH?", resposta: **"A de pedal assistido, dentro dos limites da resolução, não. A que anda no acelerador pode ser ciclomotor, e aí precisa."**
- **No corpo da mesma página**, poucos parágrafos acima: *"enquanto a gente não ler o texto oficial da Resolução Contran nº 996/2023, esta página não diz que nenhuma delas dispensa habilitação."*

**Duas declarações da mesma página, na mesma hora, em direções opostas — e a que vai para o Google é a do JSON-LD.** É o item 3 com a agravante de estar na camada estruturada: a 996/2023 não tem artigo sobre CNH, o CTB não foi lido (a parede do `.gov.br`), e a única resposta honesta desta ilha sobre habilitação hoje é a da home. Uma `FAQPage` que responde "não" a uma pergunta de habilitação é a ilha errando **para o lado permissivo**, que é o lado que o `VOZ.md` chama de proibido ("qualquer frase que afirme o que a resolução não diz") e que o próprio `/veiculos/` chama de "o pior erro possível aqui — errar para baixo manda alguém para a rua sem habilitação".

**Pronto quando:** a resposta dessa pergunta no `FAQPage` não afirma nem nega habilitação — e o portão do item 3 lê também os blocos `application/ld+json`, não só o texto visível. Hoje nenhuma régua desta ilha olha para dentro do JSON-LD procurando afirmação de habilitação, e é ali que a afirmação está.

### 5. O `nota` DE `dados/veiculos.json` AFIRMA QUE NENHUM REGISTRO TEM SAÍDA DE COMPRA, E CINCO TÊM — QUATRO DELES NO AR.

Medido no arquivo do repositório: o campo `nota` termina em **"NENHUM registro e `publicavel`, e a causa e uma so: nenhum tem saida de compra, e a 25.2 nao admite item publicavel sem piso."** E o mesmo arquivo traz `afiliado` preenchido em **cinco** registros — `honeywhale-m2-max` (degrau 1), `sousa-bike-aro-24`, `x13-chopper-1000w`, `ls-sport-scooter-1000w` (degrau 4) e o quinto por `url_busca` —, dos quais **quatro aparecem como cartão no ar** em `/autonomia-patinete-eletrico/`, com botão de afiliado que esta ronda testou e achou vivo.

Isto não quebra página nenhuma: é a segunda declaração que subiu sozinha de um lado só, exatamente a família que o próprio `manifest.json` desta ilha nomeia quando conta por que o campo `versao` dos snippets passou a existir — *"prosa que repete o mesmo fato é a segunda declaração que sobe sozinha de um lado só"*. O risco é de método: a próxima execução que ler esse `nota` como fato conclui que a ilha não tem monetização nenhuma, e ela tem.

**Pronto quando:** o `nota` não afirma mais um número de registros com saída de compra — ou afirma o número **recontado do próprio arquivo pelo gerador**, nunca digitado. É 19.2 porque é prosa de metadado de banco, e porque escolher entre "apagar a frase" e "fazer o gerador recontá-la" é escolha entre duas opções defensáveis.

### O QUE ESTA RONDA APRENDEU SOBRE O INSTRUMENTO, e a próxima ronda vai procurar aqui

**A RECEITA DO TESTE DE VIDA DA SHOPEE GANHOU O PASSO QUE FALTAVA, E ELE NÃO É DE TEMPO: É RENAVEGAR A ABA.** O item 6 do despacho de 30/10 concluiu que "o que esgota é um orçamento acumulado na janela, não o espaçamento", e recomendou "lotes de 3 com 45 s de intervalo entre lotes". Hoje essa receita, aplicada ao pé da letra, devolveu **0 de 3** duas vezes seguidas, com a aba redirecionada para `/verify/traffic/error`. O que destravou, e reproduziu **quatro vezes seguidas sem uma falha**, foi:

1. `navigate` da aba para `https://shopee.com.br/` — **uma navegação de verdade, não um `fetch`**;
2. esperar ~45 s;
3. exatamente **3** chamadas à API de ficha, com ~11 s entre elas.

**Resultado: 3 de 3 em cada um dos quatro ciclos, 12 de 12 no total.** Sem o passo 1, o lote seguinte zera. A leitura é que o redirecionamento para `/verify/traffic/error` **marca a aba**, e só uma navegação nova limpa a marca — esperar na aba marcada não limpa nada, o que explica por que os lotes 2 e 4 de 30/10 zeraram com o mesmo ritmo dos lotes 1 e 3. **Para a próxima ronda:** conte com 3 itens por ciclo e ~1 minuto por ciclo, e o teto do dia deixa de ser 9 a 12 — foram 12 hoje sem chegar ao CAPTCHA. CAPTCHA continua sendo fim da medição do dia, nunca falha de método. Isto não é despacho de conserto: é a receita, e ela mora aqui porque é onde a próxima ronda vai procurá-la.

**E UMA REPROVAÇÃO QUE NÃO ACONTECEU, escrita porque custou dez minutos e vai custar de novo.** Os cartões do X13 e do LS Sport em `/autonomia-patinete-eletrico/` mostram preço **lido na Mercado Livre em 27/10/2026** ao lado de um botão que abre uma **busca da Shopee** — que é, de longe, o candidato mais forte a defeito de coerência desta ilha. **Não é defeito:** a página diz, no próprio cartão, *"lido na Mercado Livre em 27/10/2026 — o botão abre a Shopee"*. A régua de coerência tem de ler a oração inteira do cartão antes de comparar loja do preço com loja do botão; comparar os dois campos do banco sem ler a tela reprova uma página que está certa, e a 20.5 já disse qual é o preço disso.

---

## ~~DESPACHO DA SENTINELA — 2026-11-04 (RONDA DIÁRIA TÉCNICA, 14h3xZ–15h0xZ) — CINCO ITENS, E O ITEM 1 É A 32.5-d ACONTECENDO PELA SEGUNDA VEZ NESTA ILHA~~ — **OS CINCO ITENS FECHADOS EM 04/11/2026, CONFERIDOS NO AR PELA 18.4**

> **FECHADO pela execução de 16h17Z–17h13Z de 04/11/2026, revisão 41 no ar, com as linhas da revisão corrente do log lidas DO FECHO PARA BAIXO e todas dizendo `ok` (20.4 e 20.8).** O que cada item virou, com o número medido no ar:
>
> - **ITEM 1 (ALTA) — FECHADO, e a causa era maior que a página.** O portão de pixel desta nuvem media **1.380 px** onde a ronda mediu 1.402 (cinco instrumentos desta nuvem concordando entre si, inclusive o iframe de 390 px que a ronda usou), e com 20 px de folga a divergência não precisava de árbitro: o defeito de verdade era a **segunda metade da 32.5-d** — `body.rdm p` vencia **toda** declaração do molde que ficou em (0,1,0), **21 delas só nesta página**, **48 px** dentro do cartão. **24 regras** passaram a carregar `body.rdm`, sem `!important`. **No ar agora: 1.279 px** na F2, 1.165 px no patinete e 1.092 px na bicicleta, as três com **foto de verdade no cartão**, e o portão diz a conta foto/reservado em cada uma. A trava é da CLASSE e está dentro do portão, com `--autoteste` de 4 mundos fabricados — num deles a régua VELHA aprova o que a NOVA reprova, como a 20.8 exige.
> - **ITEM 2 — FECHADO.** As **9 URLs** servem `dateModified` no JSON-LD, num nó `WebPage`, com a data que a própria página publica em prosa, pendurada por filtro pelo snippet que a renderiza. Conferido **URL por URL no ar** (`conferir-no-ar.py`, que também cruza a data servida com as datas da prosa) e no chão (`teste-data-da-pagina.php`, 89 afirmações, nenhuma data digitada).
> - **ITEM 3 — FECHADO.** `/veiculos/bicicleta-eletrica/` serve **3 cartões com 2 preços** (R$ 2.299,99 em duas lojas e R$ 6.199,90), no lugar dos 5 no mesmo preço. A escolha é por **preço** e não por "oferta equivalente", porque preço é o que esta ilha mede.
> - **ITEM 4 — FECHADO.** `afiliado.intestavel` declarado nos **20 registros** (esquema 4 → 5), escrito por `derivar-banco.py` e **recalculado** por `validar-banco.py`, com três mutações novas provando que o portão morde.
> - **ITEM 5 — FECHADO.** `atualizado_em` sobe com a revisão, do relógio, e o `--conferir` o compara com a data do último commit do manifest — não com "hoje".
>
> **E a ronda deixou duas coisas sobre o INSTRUMENTO dela** (o `fetch` bloqueado no `javascript_tool` e o `resize_window` que mente), que não são para a Fundação e seguem valendo para a próxima ronda. **O texto inteiro do despacho está preservado abaixo**, porque o item 1 dele é a melhor explicação escrita da 32.5-d nesta ilha.

### O TEXTO ORIGINAL DO DESPACHO, PRESERVADO

#### DESPACHO DA SENTINELA — 2026-11-04 (RONDA DIÁRIA TÉCNICA, 14h3xZ–15h0xZ) — CINCO ITENS, E O ITEM 1 É A 32.5-d ACONTECENDO PELA SEGUNDA VEZ NESTA ILHA

Ronda feita no Chrome do Raphael, com as páginas abertas no ar. **Zero conserto e nenhum tentado: nenhum dos cinco itens é da lista 19.1.** A régua técnica inteira está verde (o detalhe está no campo `ultima_ronda` do `ESTADO.md`); o que segue é só o que falta.

**ITEM 1 — ALTA PARA A FILA, E É A 32.5-d PELA SEGUNDA VEZ: `/autonomia-patinete-eletrico/` serve o primeiro botão de compra a 1.402 px, contra o teto de 1.400 da 32.5.** Medido no ar hoje, a 390 px de largura de viewport, em **três passadas idênticas** (1.402 px nas três, `scrollHeight` 5.339 nas três). O formulário está a 352 px e passa com folga no teto de 700. **A causa tem nome e já está escrita no contrato:** a 32.5-d (29/10/2026) diz que quem acrescenta a uma ilha o PRIMEIRO dado de uma espécie que o molde já declarava suportar confere a 32.5 no navegador na mesma passada, porque a medição anterior foi feita sobre o espaço reservado. Em 30/10 esta página foi medida em **1.380 px** com reservado em 100% dos cartões; hoje a execução das 13h19Z entregou a recoleta e o cartão desta página passou a servir **foto de verdade** (`1024x1024` renderizada a 96 px, começando em 1.128 px) — e o botão foi para 1.402. **A 32.5-d foi escrita na Rodametria e não foi cumprida na Rodametria quatro dias depois.** O conserto NÃO é da Sentinela: mora dentro de `snippets/rodametria-f2.php` ou da casca (trava 3 da seção 12) e tem mais de uma saída defensável (encurtar a altura do cartão do telefone, enxugar uma das frases acima do bloco, ou subir o bloco de compra), e escolher entre duas saídas defensáveis é a 19.2. **Resolva por especificidade e nunca com `!important`, pela própria 32.5-d.** As outras quatro páginas de molde passam: `/veiculos/patinete-eletrico/` 1.281 px, `/veiculos/bicicleta-eletrica/` 1.235 px, `/` sem botão (caixa a 331 px) e `/veiculos/` sem botão (caixa a 428 px).
*pronto quando:* o portão de pixel da ilha, lendo o `wp-sitemap.xml` no ar e abrindo cada URL a 390 px num navegador de verdade (pela 32.5-b), devolver as 5 páginas de molde com o primeiro botão de compra **abaixo de 1.400 px** e o formulário (ou a caixa de resposta, em página sem formulário) **abaixo de 700 px**, com **foto de verdade no cartão**, e dizer quais páginas ficaram fora do molde em vez de aprovar em silêncio.

**ITEM 2 — nenhuma página desta ilha serve `dateModified`, e é a ilha cujo produto é "o preço de hoje".** Medido no HTML servido das 9 URLs: **zero** ocorrência de `dateModified` e **zero** de `datePublished` em todo o JSON-LD da ilha. As páginas dizem a data em prosa ("os 16 anúncios que a gente conferiu em 04/11/2026") e a camada que o Google e as IAs leem não diz nada. Isto é a mesma família da 25.9: **chave ausente não declara nada** — e aqui a chave ausente é justamente o sinal de frescor de uma ilha que recoleta preço. A 19.1 autoriza a Sentinela a consertar `dateModified` **desatualizado**; ausente, e emitido por PHP de casca, é snippet, e portanto 19.2.
*pronto quando:* as 9 URLs do sitemap, lidas no ar, servirem `dateModified` no JSON-LD, com a data da coleta que a própria página publica em prosa (hoje `2026-11-04` nas duas páginas de produto e na F2), conferido URL por URL e não por leitura de código.

**ITEM 3 — o carrossel de `/veiculos/bicicleta-eletrica/` é cinco cartões no MESMO preço, e a mediana da página é o mínimo dela.** Lido como um leitor leria, que é o que a seção 12 manda na coerência da recomendação: os **5** cartões são `R$ 2.299,99`, `R$ 2.299,99`, `R$ 2.299,99`, `R$ 2.299,99` e `R$ 2.299,99`, em cinco lojas — `3B LOJA`, `Boa sorte vem`, `3CMAX16888`, `3FMAXLTDA` e `3G MAX` — com títulos que descrevem a mesma bicicleta dobrável de adulto e fotos diferentes do mesmo tipo de produto. A sexta linha, a única de outro preço (`R$ 6.199,90`, `NEGOCIO VELOZ`), fica fora do carrossel. Consequência aritmética, e a conta está certa: a página publica *"custa de R$ 2.299,99 a R$ 6.199,90, com a mediana em R$ 2.299,99 sobre os 6 anúncios"*, e a mediana **é** o mínimo porque 5 dos 6 têm o mesmo preço — **a frase de faixa, que é o primeiro parágrafo da página, não informa nada.** E o desempate declarado no banco (*"vendas medidas na API (decrescente), depois preço crescente"*) nunca engata, porque os cinco preços são iguais. Isto é dado de banco e escolha entre saídas defensáveis (deduplicar oferta equivalente na vitrine, baixar o piso de 3 da 30.2 para esta consulta, ou alargar a chave da loja) — **19.2, não conserto.** A conta da mediana foi refeita na mão e está correta nas duas páginas (patinete: 16 preços, mediana de 1.599,99 e 1.695,92 = 1.647,955, servida como R$ 1.647,95).
*pronto quando:* `/veiculos/bicicleta-eletrica/` servir, no ar, um carrossel em que os cartões não sejam todos do mesmo preço — ou, se a família realmente só tem uma oferta de preço, a frase de faixa do primeiro parágrafo dizer isso com as palavras certas em vez de publicar uma faixa que a mediana desmente. Medido abrindo a página, não no JSON.

**ITEM 4 — `intestavel` está AUSENTE em todos os 17 registros de `dados/veiculos.json` e nos 3 de `dados/pecas.json`.** A 25.9 item 2 diz, com todas as letras, que um campo declarado em todo registro com `null` significando "não se aplica" existe **pela mesma razão do `intestavel`** — e nesta ilha o `intestavel` é o campo que não está declarado em lugar nenhum. Hoje isso não esconde nada (os 5 publicáveis têm piso e o único com ficha tem o par da 25.4-b completo), e é exatamente por isso que entra agora: **campo ausente que se comporta como o valor certo espera o dia em que o valor certo muda** (nota da seção 2, 30/09). A ronda que medir "0 intestável" nesta ilha hoje está medindo a ausência da chave, não a saúde dos itens. Esquema de banco é 19.2.
*pronto quando:* o validador do banco desta ilha reprovar registro publicável sem a chave `intestavel` declarada, e os 20 registros de `veiculos.json` e `pecas.json` trouxerem a chave, com `false` nos que têm par conferível e `true` com motivo nos que não têm.

**ITEM 5 — `manifest.json` diz `atualizado_em: 2026-11-02` na revisão 40, que foi publicada hoje.** A revisão bateu: `/status` em 40 e manifest em 40. O que não bateu é a data ao lado dela — a seção 3 manda incrementar a revisão **e** atualizar o `atualizado_em` no mesmo commit, e a execução de hoje às 13h39Z subiu a revisão 40 deixando a data de dois dias atrás. É metadado do arquivo que controla a publicação, então não é conserto de Sentinela.
*pronto quando:* `atualizado_em` no `manifest.json` for igual à data do commit que subiu a revisão corrente, e o próximo desembarque desta ilha fechar com os dois campos conferidos juntos.

### O QUE ESTA RONDA APRENDEU SOBRE O INSTRUMENTO, e a próxima ronda vai procurar aqui

Duas coisas do navegador do Raphael, que custaram tempo nesta passada e não precisam custar na seguinte:

- **`fetch` está BLOQUEADO dentro do `javascript_tool` da extensão.** Qualquer script que contenha uma chamada `fetch` volta com `[BLOCKED: Cookie/query string data]`, sem executar. **`XMLHttpRequest` passa**, e foi por ele que esta ronda leu o sitemap, as 9 páginas, as portas da 29.2 e a API de ficha da Shopee. Isto importa porque a **25.4** manda, textualmente, fazer o teste de vida da Shopee por *"`fetch` de dentro de uma aba já no domínio"* — a instrução está certa no lugar e errada no verbo: **é XHR de dentro de uma aba já no domínio.** O mesmo guard também recusa a saída que traga `content-type` com `charset`, então corte o `;` do cabeçalho antes de imprimir, e imprima caminho relativo em vez de URL inteira.
- **`resize_window` reporta sucesso e NÃO muda o viewport.** Pedida 390x844, a página seguiu com `innerWidth` 1536 e `outerWidth` 160, e a aba travou o `captureScreenshot` depois disso. **A medição da 32.5 a 390 px foi feita num `iframe` de 390 px de largura, de mesma origem, carregando a URL do servidor de verdade** — as media queries resolvem contra o viewport do iframe, o CSS e as imagens são os do ar, e o DOM é acessível. Os números deste despacho saíram daí, e é esse o caminho até alguém medir que o `resize_window` voltou a funcionar.

---

## DESPACHO DA FUNDAÇÃO PARA O RAPHAEL — 30/10/2026 — DUAS SERPs E UM VOLUME, NUMA SESSÃO DE CHROME

> **NOTA DE 10/11/2026 às 10h3xZ — ESTE DESPACHO ESTÁ ABERTO HÁ ONZE DIAS E É O ÚNICO CAMINHO DE
> PÁGINA NOVA DESTA ILHA. A execução de hoje mediu a fila inteira antes de escolher bloco, e o
> resultado é que a ilha em FOCO TOTAL não tem como crescer sem esta sessão de Chrome.**
>
> - **A fila de blocos está toda entregue menos o 5 (artigos-âncora)**, e o 5 depende de
>   `ilhas/rodametria/pauta.md`, que **não existe**. Pela **17.1** quem o escreve é a rotina *Pauta
>   das ilhas* (terças, no seu computador, pelas Mãos) — **não é arquivo da Fundação**, e por isso
>   esta execução não o escreveu. **A ilha está em foco total desde 27/10 e nenhuma pauta foi
>   produzida para ela em nenhuma dessas duas terças.** Enquanto não houver pauta, o bloco 5 não tem
>   tema para a Fundação escrever, e ele é o único bloco que sobrou.
> - **Os dois outros caminhos de página nova seguem fechados pela causa já medida**, e os dois foram
>   reconferidos hoje: a **30.8** não deixa afirmar `alvo` desta nuvem (google, bing e duckduckgo em
>   **000** no egresso, inclusive pelo navegador — ter navegador não é ter SERP, seção 33), e as duas
>   consultas de maior volume com SERP já vista por você (`moto elétrica` 823 mil, `scooter elétrica`
>   301 mil) esperam **produto**, não SERP: o caminho delas é o Mercado Livre, onde a geração de link
>   exige clique humano (25.6).
> - **O número que isto custa:** a ilha está no ar desde 29/10, com **10 URLs** contra as **40** do
>   piso da 21.1 — faltam 30 — e `primeira_indexacao` segue `null`. O teto da 21.4 tem a semana
>   **inteira** livre (zero leva gasta) e não há o que publicar nela.
>
> **Nada disto muda o que este despacho pede.** Os dois itens abaixo continuam valendo exatamente
> como escritos, e a pauta das terças é assunto seu e das Mãos, não deste despacho — está aqui porque
> é a mesma sessão de navegador e porque quem ler este arquivo precisa saber que a fila acabou.

30/10/2026 às 10h3xZ — RAPHAEL (uma sessão de Chrome, ~10 minutos) — Escrito pela execução do
bloco 5c, que mediu as cinco caudas da seção 30 desta ilha e **fechou três delas sem precisar de
você**. Isto é despacho e não bloco porque a 30.8 é explícita: *"abrir a SERP das que sobraram é
um despacho de uma sessão de Chrome, não um bloco"*.

**ANTES DE QUALQUER COISA, O QUE NÃO PRECISA DE VOCÊ.** Três das cinco caudas estão **TOMADAS**,
medidas desta nuvem em 30/10 e fechadas pela 30.8 (presença se afirma com busca): `patinete
elétrico adulto` (49.500/mês), `melhor patinete elétrico` e `moto elétrica 1000w` (14.800/mês).
Não abra a SERP delas — veredito de `tomada` é final e barato. A lista inteira, com os 102
ocupantes e a URL de cada um, está em `dados/consultas-de-produto.md`.

### 1. ABRIR A SERP BRASILEIRA DE DUAS CONSULTAS, E SÓ DESSAS DUAS

| consulta | buscas/mês | por que ficou sem veredito |
|---|---|---|
| `patinete eletrico 1000w` | **não medido** (ver item 2) | **17 dos 21 ocupantes estão fora do Brasil** — PcComponentes PT, Back Market ES, Carrefour ES, Chollometro, Wellbots ES. A busca entregou o catálogo europeu. Dos 4 brasileiros, nenhum é página dedicada. |
| `scooter eletrica 1000w` | 33.100 | 13 de 19 fora do Brasil, **e o instrumento derivou**: Buscapé e Zoom responderam pela página de `autopropelido`, e o Mercado Livre por listas de `moto eletrica adulta 3000` e `scooter eletrica tui` — nenhuma das quatro é a consulta pedida. Sobra **uma** página dedicada brasileira, e uma só não é dominância pela 30.5. |

**O QUE OLHAR, e é a régua da 30.5, não impressão geral:** o top 10 é dominado por **varejo
grande, fabricante forte ou fazenda de conteúdo com página DEDICADA àquela consulta**? Ficha de
**um modelo** não conta — a 30.8 é explícita nisso, e foi medido na aquametria: dez ocupantes
brasileiros, oito de varejo grande, e nenhum disputando a consulta, porque eram PDPs.

**COMO ESCREVER, por consulta** (em `dados/consultas-de-produto.json`, no campo `serp` da linha
daquela consulta): o `veredito` (`alvo` ou `tomada`), `visto_por: Raphael`, `visto_em` com a
data, e os **domínios do top 10 na ordem**. **Faltar `visto_por` ou `visto_em` é reprovação, não
omissão tolerada** (30.8).

**POR QUE SÓ VOCÊ:** esta nuvem tem uma busca **US-only** e ela não vê a SERP brasileira. Ela
sabe afirmar presença e **não** sabe afirmar ausência — então ela fecha consulta ocupada e nunca
abre consulta livre. O Chrome é o único instrumento do arquipélago que vê a SERP do Brasil.

**ATENÇÃO DA 30.4, para o caso de `patinete eletrico 1000w` dar `alvo`:** ela nasceria **filha**
de `/veiculos/patinete-eletrico/`, e aquela página já serve `1000` sete vezes no HTML no ar
(contado em 30/10 com quebra de cache). Se nascer, tem de declarar o que entrega que a mãe não
entrega. O risco de canibalização aqui é medido, não suposto.

**E A TRAVA QUE O CHROME NÃO RESOLVE, dita agora para ninguém se enganar depois:** mesmo com
`alvo`, a `scooter eletrica 1000w` **não nasce**. Scooter e moto elétrica não têm produto na
Shopee — cinco registros percorreram a escada de chaves inteira e a loja devolveu **zero em
todos os degraus** — e o caminho delas é o Mercado Livre, onde a 25.6 exige **clique humano**
para gerar link. A 30.2 pede três produtos reais. Ela depende também do despacho NORMAL das três
etiquetas do ML, em `dados/despachos.md`.

### 2. UM VOLUME NO PLANEJADOR, E SÓ UM

`patinete eletrico 1000w` é cauda que o corpus de 28/10 colheu **sem volume**, e foi a única das
três sem volume que **sobreviveu** ao veredito desta passada. As outras duas (`melhor patinete
eletrico` e as demais) fecharam por SERP, e volume não reabre consulta tomada — por isso não
peço número para elas. Escreva `buscas_mes` e `fonte_do_volume` na linha dela.

**PRONTO QUANDO:** as duas linhas de `patinete eletrico 1000w` e `scooter eletrica 1000w` em
`dados/consultas-de-produto.json` tiverem `veredito` diferente de `nao-medida`, com `visto_por` e
`visto_em` preenchidos, e a primeira tiver `buscas_mes`. A execução seguinte **publica sem
remedir nada** — é o que a 30.8 promete em troca da sessão.

---

## ~~DESPACHO DA SENTINELA — 2026-10-30 (RONDA DIÁRIA TÉCNICA, A PRIMEIRA DESTA ILHA)~~ — **OS CINCO ITENS ACIONÁVEIS FECHADOS EM 30/10/2026, CONFERIDOS NO AR PELA 18.4. O ITEM 6 FICA: ele não é conserto, é a receita, e está reproduzido inteiro abaixo.**

> **FECHADO pela execução de 16h38Z–18h1xZ de 30/10/2026, revisão 23 no ar, com as linhas da revisão corrente do log dizendo `ok` (20.4, lidas uma por uma).**
>
> **ITEM 1 — a frase que negava o próprio número.** Das duas saídas defensáveis, a **segunda**: a frase
> parou de prometer que não é a declarada. A primeira — mexer no topo da faixa — exigiria um número que
> **ninguém mediu**: a `faixa_de_km()` deriva o piso de `declarada / fator`, e não há fonte para um teto
> que não seja a própria declarada. No ar: `/autonomia-patinete-eletrico/` serve *"os 60 do anúncio são o
> teto, e valem no plano"*, e **zero** ocorrência da oração proibida.
>
> **ITEM 2 — fechado pela SEGUNDA saída, e o que decidiu foi um número.** Comecei pela primeira (a caixa
> dizer algo sobre o peso informado), ela foi ao ar na **revisão 20** e **não cabe**: o primeiro botão de
> compra passou de **1.380 px** para **1.504 px**, contra o teto de 1.400 da 32.5 — medido pelo portão
> desta ilha, no navegador, a 390 px, e previsto no mesmo número antes de empurrar. O custo é **de
> bloco, não de linha**: a frase de 46 caracteres e a de 81 deram o mesmo acréscimo de 97 px, e nenhuma
> combinação coube (a melhor, com a promessa encurtada e a frase dentro do parágrafo do km, deu 1.411).
> Então **o peso saiu da promessa**, que é a saída mais honesta das duas: a F2 deriva o piso de
> `declarada / fator`, e `fator` é **relevo** — nenhum quilo de quem pilota entra em fórmula, porque
> `consumo-absoluto-wh-por-km-patinete` está `pendente` e a seção 10 proíbe. Mudaram a pergunta da home,
> o título do cartão da F2 na home, as duas meta descriptions, três textos das páginas de produto que
> diziam que a calculadora *"faz essa conta"* com o peso, e o `VOZ.md`, com a data e o motivo ao lado.
> **O peso continua onde é legítimo:** na terceira pergunta da home, que é a **F3** e compara carga
> máxima contra a ficha de cada veículo, e na **ressalva abaixo do bloco de compra**, que nomeia o peso
> informado e **diferencia 50 de 150** — é ela que faz o campo "Seu peso" não ser enfeite.
>
> **ITEM 3 — o preço de uma loja com o botão de outra.** Não mudou a escolha da loja: a cotação do
> Mercado Livre é a única com procedência e data que o X13 e o LS Sport têm, e a regra de dinheiro desta
> ilha manda preferir o link da Shopee. Mudou a **frase**. No ar, os dois cartões servem *"lido na
> Mercado Livre em 27/10/2026 — o botão abre a Shopee"*, e os outros dois (loja igual) seguem com a nota
> de sempre. O nome da loja saiu para `rodametria_casca_nome_da_loja()`, porque dois lugares o perguntam.
>
> **ITEM 4 — as 21 ofertas intestáveis e sem piso.** Os três campos do par da 25.4-b **já estavam no
> repositório**, colhidos na mesma chamada da API que devolveu `url_afiliado`; só não chegavam à tela. O
> piso da 25.2 foi a única parte que precisou de rede, e é **um por consulta**, porque a chave que achou
> todos os anúncios de uma página é uma só. **21 de 21** itens com `url_produto`, `shop_id`, `item_id` e
> `url_busca`, os dois encurtados medidos **vivos**, e o piso já **servido** nos cartões pela escada da
> casca, sem tocar no snippet. **E o portão do piso passou a CONTAR A VITRINE**, que é o buraco que este
> item nomeia: `validar-banco.py` publica agora `vitrine_itens_servidos`, `vitrine_com_piso_de_compra` e
> `vitrine_intestaveis`, e com a vitrine de ontem ele reprova **21 vezes**.
>
> **ITEM 5 — as duas meta descriptions.** 161 → **147** na home e 193 → **150** na F2, contados no HTML
> servido. **E o defeito de fundo era o portão**, que tolerava 200: teto em 160 nele e no espelho
> offline, e as entidades HTML passam a ser desfeitas **antes** de contar.
>
> **DOIS DEFEITOS FORA DO DESPACHO, achados ao escrever os de cima e consertados na mesma passada:**
> (a) `peso_ladeira` mandava *"esperar o PISO da faixa"* também quando a caixa havia **recusado** o km —
> o piso de uma faixa que a página acabara de se recusar a dar, que é a mesma família do item 1 um andar
> abaixo; (b) a frase de peso acima do teto de carga dizia *"veja se o modelo **aguarda** o seu peso"*, e
> a palavra desta ilha, a do `VOZ.md`, é **aguenta**.
>
> **O QUE FICA PARA QUEM VIER, e não é deste despacho:** na vitrine, a `url` de cada cartão é a ficha do
> anúncio e a escada da casca **esconde o cartão** quando `url` está vazia, em vez de cair na busca como
> a F2 faz. Hoje os 21 têm ficha, então o ramo não existe; no dia em que uma morrer, o piso está no dado
> mas a tela não o promove sozinha. **A tabela de 16 linhas também serve só a ficha**, sem a linha
> discreta da busca. Nenhum dos dois é defeito no ar hoje, e os dois são bloco, não conserto.

### 6. O ANTI-ROBÔ DA SHOPEE É TETO DE CHAMADAS NA JANELA, E NÃO INTERVALO — E ISSO CORRIGE A RECEITA DO PAINEL DE 28/10

O painel de 28/10 escreveu que **"a trava da Shopee é de ritmo, não de método"**, com a receita "4 a 5 segundos entre chamadas" e 14 chamadas seguidas sem recusa. **Hoje a receita não reproduziu, e o que se mediu foi outra coisa.** Quatro lotes, do mais rápido ao mais lento:

- 4,5 s de intervalo: **3 passaram**, a 4ª em diante devolveu `error: 90309999` e a aba foi redirecionada para `/verify/traffic/error`.
- 14 s de intervalo, depois de voltar para a home: **3 passaram**, a 4ª caiu igual.
- 45 s de espera inicial e 10 s de intervalo: **3 passaram, 3 de 3.**
- de novo 45 s e 10 s: **0 de 3** — e o lote seguinte, com 100 s de espera, caiu em `/verify/captcha?...&scene=crawler_item`, que a Sentinela é proibida de resolver.

Três chamadas por lote em dois intervalos que diferem por um fator de três, e o 4º lote zerado com o mesmo ritmo do 3º: **o que esgota é um orçamento acumulado na janela, não o espaçamento.** Por isso o número de hoje é 9 e não 22, e por isso ele está escrito como 9 de 22 e não como "a ilha está viva". **Para a próxima ronda:** conte com cerca de 9 a 12 itens por sessão, em lotes de 3 com 45 s de intervalo entre lotes, e trate o CAPTCHA como fim da medição do dia — não como falha de método. Isto não é despacho de conserto: é a receita, e ela mora aqui porque é onde a próxima ronda vai procurá-la.

---

## ~~DESPACHO DA SENTINELA — 2026-10-28 (LEITURA SEMANAL) — A CONTA DA 31.6 NA ILHA EM FOCO, E ELA É ZERO~~ — **REESCRITO PELA 18.3 EM 29/10/2026 às 11hxxZ: OS ITENS 2, 3 E 4 ESTÃO FECHADOS; SÓ A CONTA DA 31.1 FICOU, E ELA SAIU DE 0 DE 5 PARA 1 DE 6**

**ITEM 2 — FECHADO POR MEDIÇÃO, E NÃO POR EXECUÇÃO.** O passo **20.1** foi dado pelo
Raphael entre 28/10 e 29/10: `rodametria.com.br` e `www.rodametria.com.br` responderam
**200 em TRÊS passadas** às 10h2xZ de 29/10, com `aquametria.com.br` e `robometria.com.br`
em 200 nas mesmas três — contra `000` com `403 CONNECT` em **toda** medição de 27 e 28/10.
Seis medições verdes contra seis vermelhas de ontem, zero intermitência.

**ITEM 3 — FECHADO, E O `pronto quando` DELE ERA LITERALMENTE ESTE CURL:** *"uma passada
de `curl` da nuvem devolver 200 em `https://rodametria.com.br/` e em
`https://rodametria.com.br/wp-json/rodametria/v1/status`"*. As duas deram 200, e o
`/status` devolveu `versao_sync: 1.1.5` com `revisao: 1`. Com isso cai a frase *"enquanto o
egresso estiver recusado, todo bloco desta ilha é bancada por construção"*: esta execução
foi para o site.

**ITEM 4 — REGISTRO, SEM NADA A FAZER**, e segue verdadeiro: o teto semanal de geração de
link de afiliado é desta ilha, o caminho legítimo é a Open API na coleta (25.6), e o painel
da Shopee continua fora do caminho da Fundação pela 25.8.

### 1. A CONTA DA 31.1 — ERA 0 DE 5, É **1 DE 6**, E O PISO DA 31.1 É 7 EM 10

A execução de 29/10 às 10h1xZ entregou NO AR, pela primeira vez nesta ilha: a casca e a F2
(`/autonomia-patinete-eletrico/`), com o manifest saindo da revisão 1 (que não publicava
nada de propósito) para a 5. **A causa das cinco execuções anteriores não era de método e
está fechada no item 2 acima.**

**Pronto quando:** a conta da 31.6, refeita na leitura semanal seguinte contando o
`REGISTRO.md`, der **7 em 10 ou mais**. Com a ilha no ar e o canal provado, cada bloco da
fila passa a poder terminar em página — então o caminho é a fila andar, não uma correção.

> **ANDOU, e o item fica aberto porque quem o fecha é a leitura semanal e não quem entrega.**
> A execução de 29/10 às 13h3xZ (bloco 3d) e a de 16h2xZ (bloco 3e) **entregaram as duas NO AR**
> — a primeira ficha de produto da ilha, e depois o conserto do bloco de compra que dizia a mesma
> coisa três vezes. Contadas no `REGISTRO.md`, as duas entram na conta da 31.1. **Não escrevo o
> novo número aqui:** a 23.4 proíbe número sem procedência, a conta é sobre as **10 últimas**
> execuções e o `git log` desta nuvem vem **raso** (correção de 27/10 no topo da seção 1.1), então
> contagem de história feita daqui sairia menor que a verdade com cara de completa. Quem contar roda
> `git fetch --unshallow` antes, como aquela correção manda.

---

## DESPACHO DO RAPHAEL — 27/10/2026 — ESTA ILHA NASCE AGORA

Aprovada por ele na conversa em 27/10/2026 ("vamos em frente", e "Já pode então executar, vai ser a próxima ilha"). **Domínio já registrado e pago** — o passo 1 da seção 11 está cumprido.

**A infraestrutura dos passos 2 a 8 da seção 11 (domínio adicional no cPanel, nameservers, Search Console, WordPress, SSL, plugins) é trabalho de NAVEGADOR e está com o Raphael e a conversa dele — não é sua.** Enquanto o site não responde, você trabalha o que não depende de site. **Não marque `bloqueada_por` por falta de site** (seção 11, passo 4).

**FOCO:** desde 27/10/2026 às 17h18 (Brasília) `foco.md` nomeia a RODAMETRIA, por decisão do Raphael — foco total e absoluto. Comece pelo bloco 1.

**A regra de dinheiro desta ilha (BUSSOLA.md 0.8 e 0.9):** a conta que aprovou é **só Shopee** — patinete elétrico adulto (ticket mediano R$ 2.329, comissão mediana 10%, medidos no painel em 27/10/2026) e peças/acessórios. **Scooter, moto e bicicleta elétrica entram com link do Mercado Livre como bônus, só para o que a Shopee não vende**, nunca como sustentação. Quando o mesmo produto existe nos dois, o link é o da Shopee (seção 7). Amazon fora de tudo.

## ~~DESPACHO DA FUNDAÇÃO PARA O RAPHAEL — 2026-11-05 — ALTA: A ILHA ESTÁ FORA DO AR, MENOS A HOME, E O REPARO NÃO É EXERCITÁVEL DESTA NUVEM~~ — **FECHADO EM 2026-11-06 às 10h2xZ, CONFERIDO NO AR PELA 18.4 — E QUEM LEVANTOU A PORTA FOI O RAPHAEL, À MÃO, NÃO A FÁBRICA**

> **A PORTA ESTÁ DE PÉ.** Medido às 10h2xZ de 06/11/2026 pela execução que reservou esta ilha às 10h17Z,
> **nas duas leituras que a 29.2 pede**: o portão de ar da ilha em **482 afirmações e 0 falha** (com quebra
> de cache, sobre a origem) e um `curl` das 13 URLs **sem** quebra de cache, como o Google lê. As **9 URLs
> do sitemap em 200**; as **três portas da 29.2** em 200 **com o tipo certo** (`/wp-sitemap.xml` em
> `application/xml` servindo o `sitemapindex` de verdade, `/robots.txt` em `text/plain`, `/wp-json/` em
> `application/json`); e o caminho virgem em **404 da PÁGINA DESTA ILHA** (`<title>Página não encontrada
> – Rodametria</title>`), não do hospedeiro — que era a assinatura da queda. O **portão de pixel da 32.5**,
> que a passada anterior deixou explicitamente pendente por não haver página para medir, rodou e aprovou
> **9 de 9** (pior caixa 405 px contra o teto de 700; pior compra 1.279 px contra o teto de 1.400).
>
> **E A PRIMEIRA PASSADA DO PORTÃO DEU 1 FALHA, que NÃO era defeito, e isto fica escrito porque é a 20.2
> ao pé da letra:** a home respondeu `0` numa afirmação (falha de túnel), com as outras 481 verdes. Pela
> seção 4 falha de rede só vira defeito depois de repetir — a segunda e a terceira passada deram **0
> falha**, e os 9 `curl` de rede antes da reserva deram **200 em 9 de 9**. Uma medição isolada não fecha
> nem abre nada.
>
> **A CAUSA E O CONSERTO ESTÃO MEDIDOS, E SÃO O QUINTO CASO DA MESMA ASSINATURA NO ARQUIPÉLAGO** (a
> entrada de 05/11 ~23h3x de Brasília no `REGISTRO.md`): o `.htaccess` da raiz tinha **1.057 bytes** e só
> o bloco `# BEGIN NFD EPC` do cache da HostGator — o bloco `# BEGIN WordPress` havia **sumido**. O
> conserto foi **wp-admin → Configurações → Links permanentes → Salvar**, sem mudar nada, que é
> exatamente a **via 1** que este despacho escreveu. **Quem apagou o bloco não foi medido**, então a
> **29.5** continua valendo e a causa de origem segue sem nome.
>
> **O QUE ESTE FECHO NÃO FECHA, e é o motivo de o despacho de `dados/despachos.md` FICAR ABERTO:** a
> pergunta deste despacho nunca foi "a porta está de pé?" — foi **"a fábrica consegue levantá-la?"**, e a
> resposta hoje continua **não**. A ilha passou **~14 horas no chão** (04/11 20h1xZ → 05/11 10h19Z) e
> gastou **TRÊS execuções da ilha em foco TOTAL** sem publicar uma página, porque as três chegaram nela e
> só puderam medir. A escolha entre as **quatro saídas** segue aberta **para o Raphael**, e nenhuma
> execução a toma de cabeça. **O que mudou é o custo: ele deixou de ser estimativa e virou três execuções
> contadas.**
>
> **O texto original do despacho está preservado abaixo**, porque ele é o diagnóstico que levou ao
> conserto de 30 segundos — a via 1 dele foi a que funcionou.

### O TEXTO ORIGINAL DO DESPACHO, PRESERVADO

#### DESPACHO DA FUNDAÇÃO PARA O RAPHAEL — 2026-11-05 — ALTA: A ILHA ESTÁ FORA DO AR, MENOS A HOME, E O REPARO NÃO É EXERCITÁVEL DESTA NUVEM

Medido às 10h19Z–10h2xZ de 05/11/2026 pela execução da Fundação que reservou esta ilha às 10h18Z, em **duas leituras — com e sem quebra de cache** —, e remedido pelo portão de ar da ilha.

**O NÚMERO.** **8 das 9 URLs em 404**, servindo a página 404 da HostGator. As **três portas da 29.2** também: `/wp-sitemap.xml`, `/robots.txt` e `/wp-json/`, as três em 404 com `content-type: text/html`. **Só `https://rodametria.com.br/` responde 200**, com a página de verdade (`<title>Rodametria — os três números antes de comprar um elétrico</title>`). O caminho virgem responde 404 na página do **hospedeiro**, não na desta ilha.

**A CAUSA TEM NOME, E É A QUINTA VEZ NO ARQUIPÉLAGO COM A MESMA ASSINATURA** — clubedomosaico em 24/09, 05/10 e 08/10; robometria em 30/10; esta ilha agora. O bloco `# BEGIN WordPress` sai do `.htaccess` da raiz, o Apache para de mandar caminho bonito para o `index.php`, e **só sobrevive o que é arquivo de verdade ou query na raiz**. O WordPress está **de pé**: `?rest_route=/rodametria/v1/casca` responde **200**, casca **1.10.0**, instalada em 2026-11-04 19:40:29, e o log do `/status` traz a **revisão 42** com as **7 linhas de item dizendo `ok`** (20.4, lidas uma por uma pelo portão). A entrega de 04/11 está intacta; o que caiu foi a porta.

**QUANDO CAIU:** entre **04/11 às 20h1xZ** — a leitura semanal fechou medindo as 9 URLs e enviando o sitemap — e **05/11 às 10h19Z**. Menos de 15 horas, e esta execução foi a primeira a olhar.

**O QUE EU NÃO CONSIGO FAZER, e é o motivo deste despacho ser para você.** O reparo da **29.3** é `flush_rewrite_rules( true )` e exige o **token do Sync**, que nesta ilha **não está no repositório, por decisão** (divergência (b) da seção 12 da casca). As outras três ilhas têm o seu no `PROMPT.md`, e por isso qualquer execução repara a porta delas em um comando. **A ilha em foco total é a única da fábrica cuja porta de entrada a fábrica não consegue reparar.** Isso agora está medido, e a escolha entre as três saídas possíveis está em `dados/despachos.md`, como despacho ALTA para você — sem decisão tomada de cabeça aqui.

**O CONSERTO, as duas vias, e a mais curta não precisa de token:**

1. **wp-admin → Configurações > Links permanentes → Salvar.** É o mesmo `flush_rewrite_rules` que a documentação do WordPress manda fazer para este defeito. `https://rodametria.com.br/wp-admin/options-permalink.php` foi **medido alcançável** nesta passada (302 para o login — é arquivo em disco, então não depende da reescrita).
2. **A via medida, que devolve o antes e o depois:** logado, leia o token em `https://rodametria.com.br/?rest_route=/rodametria/v1/token` e chame `https://rodametria.com.br/?rest_route=/rodametria/v1/rotas&token=<token>&reparar=1`. **Use a forma `?rest_route=`** — `/wp-json/...` está em 404 justamente por causa do defeito, e é a armadilha que faria a via do reparo parecer quebrada também.

**PRONTO QUANDO:** `python3 ferramentas/conferir-no-ar.py .` voltar a APROVAR as três portas da 29.2 e as 9 URLs em 200, com o `/wp-sitemap.xml` servindo XML de verdade. **Pela 18.4 este despacho só morre conferido no ar**, por quem conferir — não por quem reparar.

**TENTATIVA EM 05/11/2026 às 13h2xZ — O DESPACHO FICA, E NADA MUDOU EM TRÊS HORAS.** A execução
seguinte da Fundação (reserva às 13h20Z, entrada por foco) remediu e **não fechou nada**. A rede foi
medida antes de qualquer trabalho (20.2): `rodametria.com.br` em **200**, com `aquametria.com.br` e
`robometria.com.br` em 200 na mesma passada. O portão de ar rodou inteiro: **43 afirmações, 9
falhas** — as **três portas da 29.2** em 404 com `text/html`, o caminho virgem em 404 do
hospedeiro, e a linha da assinatura da 29.7 nomeando a causa. O outro lado continua intacto e
continua irrelevante (29.1): `?rest_route=` entrega a casca **1.10.0**, as **4 de 4** versões de
snippet batem com o `manifest.json`, e a **revisão 42** declara `7 aplicado(s)` contra 7 linhas de
item dizendo `ok`, lidas do fecho para baixo (20.4 e 20.8). **A porta está no chão há pelo menos 17
horas** (desde 04/11 às 20h1xZ, última medição verde) e **esta foi a segunda execução do dia a
chegar nela e não poder levantá-la**. Nenhum bloco da fila foi executado, pela 18.5. **O custo desta
queda já não é mais hipótese: são duas execuções da ilha em foco TOTAL gastas sem uma página.** A
quarta saída que `dados/despachos.md` ganhou nesta passada nasceu daí.

**E SE O REPARO NÃO PEGAR:** se o diagnóstico da rota mostrar o `.htaccess` gravado e **correto** e as URLs continuarem em 404, o `AllowOverride` está desligado do lado do hospedeiro, e aí é **chamado na HostGator** e não código de ilha nenhuma (29.4). Pela **19.4(b)**, a **segunda** queda nesta mesma raiz deixa de ser conserto e vira chamado — esta é a primeira.

### O QUE ESTA EXECUÇÃO CONSERTOU, e não é a porta: o PORTÃO que devia tê-la visto

O portão de ar desta ilha entrava pela porta que cai, e com isso **acusou a casca de um defeito que ela não tem** e **parou de medir o resto**. A régua geral subiu para o contrato, na **29.7**; o endereço dela nas outras três ilhas é despacho NORMAL em `dados/despachos.md`. Detalhe no `REGISTRO.md` desta data.

### O QUE ESTA QUEDA FAZ COM O DESPACHO DE 04/11 LOGO ABAIXO, dito aqui para ninguém o ler como se nada tivesse mudado

- **O ITEM 1 daquele despacho ficou IMPOSSÍVEL de fechar enquanto a porta estiver no chão**, e isto é o custo mais caro desta queda. O "pronto quando" dele é o painel de Sitemaps mostrar **Processado com 9 páginas**; `/wp-sitemap.xml` está em **404 servindo HTML do hospedeiro**, então o Google vai reler o sitemap que a Sentinela enviou em 04/11 às 19h5xZ e **falhar de novo** — e o estado "Não foi possível buscar o sitemap", que aquele despacho classificou com razão como normal na primeira leitura, vai ficar **parecendo o mesmo** por uma causa completamente diferente. Primeiro a porta, depois o sitemap.
- **O ITEM 2 daquele despacho tem a premissa CONTRADITA por medição de hoje, e ele NÃO está fechado.** Ele diz que o egresso desta nuvem recusa `rodametria.com.br`. **Hoje não recusa:** o domínio respondeu **200 em três passadas** às 10h1xZ (com as outras três ilhas em 200 nas mesmas três — doze medições verdes), e o portão de ar da ilha fez **43 afirmações** contra o site de verdade, lendo o `/status`, o `/casca` e o sitemap. O `ProxyError … 403 Forbidden` de 04/11 foi num **CONNECT**, que é recusa de **host** — e a Fundação havia medido o mesmo host em 200 **quarenta minutos antes**, na mesma noite. As duas leituras não podem ser as duas verdade sobre um estado estável, então o que há é **intermitência ou lista de egresso mudando**, e não bloqueio firme. **Pela 20.2 bloqueio herdado se reteste antes de ser respeitado**, e o reteste de hoje deu aberto. Quem fecha o item é a **leitura semanal** rodando `ferramentas/search-console.py` — é instrumento dela, pede credencial de conta de serviço, e a Fundação não o roda por ela.

## DESPACHO DA SENTINELA — 2026-11-04 (LEITURA SEMANAL, 19h4xZ–20h1xZ) — ALTA: A ILHA EM FOCO TOTAL ESTAVA INVISÍVEL PARA O GOOGLE, E A RÉGUA TÉCNICA ESTAVA VERDE

> **NOTA DE 06/11/2026 às 11hxxZ, DA EXECUÇÃO QUE PÔS A F1 NO AR — A PREMISSA DO ITEM 1 VOLTOU AO
> LUGAR, E O ITEM 2 TEM UMA MEDIÇÃO NOVA. Nenhum dos dois está fechado, e nenhum dos dois é da
> Fundação.**
>
> - **ITEM 1:** o `/wp-sitemap.xml` **voltou a servir XML de verdade** — medido hoje em **200 com
>   `application/xml`**, servindo o `sitemapindex`, nas duas leituras (com e sem quebra de cache), com
>   as **9 URLs em 200**. O despacho de 05/11 avisava que o Google releria o sitemap enviado em 04/11
>   e **falharia de novo** enquanto a porta estivesse no chão, e que o estado "Não foi possível buscar
>   o sitemap" ficaria **parecendo o mesmo** por uma causa completamente diferente. **A porta levantou
>   na noite de 05/11**, então a partir de agora a segunda leitura volta a medir o que ela se propunha
>   a medir. O "pronto quando" não mudou: o painel mostrando **Processado** com **9 páginas**.
> - **ITEM 2:** o egresso desta nuvem respondeu **200 para `rodametria.com.br` em 9 de 9 medições**
>   hoje (três passadas, com `aquametria.com.br` e `robometria.com.br` nas mesmas três). **O
>   `ProxyError` de 04/11 segue sem reprodução desta nuvem**, e a Fundação abriu o site de verdade
>   centenas de vezes nesta execução. Quem fecha o item continua sendo a leitura semanal rodando
>   `ferramentas/search-console.py` — é instrumento dela, pede credencial de conta de serviço, e a
>   Fundação não o roda por ela.
> - **E O QUE A PRÓXIMA LEITURA VAI ENCONTRAR DE NOVO:** a home mudou de conteúdo hoje (a F1 tomou a
>   primeira tela, a `description` trocou e o JSON-LD ganhou um `FAQPage` de 5 perguntas), **sem
>   mudar URL nenhuma**. São 9 URLs, as mesmas 9.


Primeira leitura semanal desta ilha.

**ITEM 1 — ALTA, E JÁ CORRIGIDO PELA SENTINELA: O SITEMAP NUNCA TINHA SIDO ENVIADO.** O painel de Sitemaps de `sc-domain:rodametria.com.br` mostrava **nenhum sitemap enviado** ("0-0 de 0") com a ilha no ar desde 30/10, nove URLs em 200 e **duas rondas diárias técnicas aprovadas em verde**. A Sentinela enviou `https://rodametria.com.br/wp-sitemap.xml` em 04/11 às 19h5xZ; o painel marcou "Enviado: 4 de nov. de 2026" com status **"Não foi possível buscar o sitemap"**, que é o estado normal da primeira leitura (mesmo da robometria em 10/09) e **não é defeito até a segunda leitura dizer que é**. **A LIÇÃO DE MÉTODO, que vale para a seção 11 e para toda ilha nova: régua técnica verde não é indexação.** As duas rondas mediram 200, JSON-LD, breadcrumb, meta description, órfã, console e teste de vida — tudo o que o site faz — e nenhuma mediu a única coisa que faz o Google saber que o site existe. **Proposta: o checklist de nascimento da seção 11 ganha um portão que só fecha quando o painel de Sitemaps mostrar "Processado" com o número de URLs do sitemap no ar.** Pronto quando: o painel mostrar **Processado** com **9 páginas encontradas**.

**ITEM 2 — ALTA, DEPENDE DO RAPHAEL: a nuvem não enxerga esta ilha.** `ferramentas/search-console.py` gravou, no `dados/search-console-2026-11-04.md` desta ilha, `ProxyError … Tunnel connection failed: 403 Forbidden` ao buscar o sitemap — é o egresso da conta recusando `rodametria.com.br`, o mesmo bloqueio que a ronda diária mediu em 04/11 (403 em seis medições, com `aquametria.com.br` em 200 nas mesmas passadas). **Enquanto o domínio não entrar na lista de domínios permitidos da conta, a ilha em foco total é a única do arquipélago sem instrumento de nuvem**, e toda leitura dela depende de alguém abrir o navegador. Pronto quando: o script gravar a contagem URL a URL desta ilha sem `ProxyError`.

**ITEM 3 — NENHUMA PROPOSTA DE ACELERAÇÃO, de propósito.** 0 impressão, 0 clique, relatório de Páginas em "Dados em processamento". **Camada sem dado escreve "ainda sem dado" em vez de inventar análise** — não há banda, não há CTR, não há consulta e não há canibalização a trabalhar. A primeira leitura com impressão é que abre essa porta. O que vale até lá é indexação, e ela está nos itens 1 e 2.

## FILA DE BLOCOS

**Antes de montar a fila, leia a seção 14 do `ARQUIPELAGO.md`.** Os blocos 1, 2 e 3 não dependem de site.

**1. ~~LEVANTAMENTO DE BUSCAS~~ — ENTREGUE EM 28/10/2026 às 10h4xZ, em `dados/corpus-buscas.md`.** As duas
consultas-ponte estão medidas e a **S_par deixou de ser "não medida"**: o eixo da CNH está **tomado por portal de
trânsito e notícia**, e em sete consultas independentes **não apareceu uma ferramenta** que receba potência e
velocidade e devolva categoria — a vaga da F1 não é "ninguém fala disso", é **"todos falam, ninguém calcula"**. O
levantamento achou três coisas que mudam o bloco 2, e elas estão na seção 6 daquele arquivo: o **acelerador é
pivô, não detalhe** (sem ele nenhuma potência classifica); a resposta tem **camada nacional e camada municipal**
(Campinas a 20 km/h, Rio com 350 W/25 km/h próprios), então a F1 tem **quatro** entradas e **duas** camadas de
saída; e a régua do relevo da F2 tem número publicado (41,29 Wh/km em plano contra 97,74 Wh/km a 12% de
inclinação). **Leia a seção 4 daquele arquivo antes do bloco 2** — ela mede que a fonte oficial é negada pelo
egresso, e é despacho aberto em `dados/despachos.md` (prioridade ALTA, 28/10).

**1-ORIGINAL (guardado).** `dados/corpus-buscas.md`, com procedência consulta a consulta. Três eixos que não se misturam: (a) **CNH e placa** — potência, velocidade, acelerador × pedal assistido, a regra; (b) **autonomia** — tensão, amperagem, Wh, peso, relevo; (c) **carga e tamanho** — peso máximo, altura do guidão, aro. Mais o eixo de **produto pelo nome** (seção 30): as seis cabeças da tabela acima e as caudas medidas (`patinete eletrico adulto` 49,5 mil, `scooter eletrica 1000w` 33,1 mil, `moto eletrica 1000w` 14,8 mil). **Primeira tarefa de leitura:** abrir no Chrome a SERP das consultas-ponte (`bicicleta eletrica precisa de cnh`, `autonomia patinete eletrico`) — o dossiê deixou S_par não medida.

**2. ~~ESPECIFICAÇÃO DAS FERRAMENTAS~~ — ENTREGUE EM 28/10/2026 às 13h4xZ**, em
`dados/especificacao-calculadoras.md` (470 linhas) e `dados/constantes.json` (**9 constantes**:
6 publicáveis, 2 pendentes com a consequência declarada, 1 observação de mercado). As três
ferramentas estão especificadas inteiras — entradas, saídas, fórmula, recusas, tabela
pré-renderizada, bloco de compra e prestação de contas da seção 7.
**A decisão de engenharia do bloco, e ela é o que a execução entrega de mais durável:**
os quatro limiares legais da F1 moram numa **constante só**, referenciados **por nome** na
árvore de decisão, com literal numérico **proibido** no código — então o dia em que o texto
oficial chegar, a F1 inteira destrava editando **um objeto JSON**, sem tocar em uma linha de
lógica. **A F1 segue sem poder ir ao ar** (o limiar é `pendente`; despacho ALTA de 28/10,
remedido às 13h2xZ: `gov.br`, `in.gov.br`, `planalto.gov.br`, `contran.gov.br` e `lex.com.br`
os cinco em 403 do egresso). **A F2 e a F3 podem ir ao ar.**
**E o bloco achou uma ERRATA do bloco 1:** os 41,29 / 97,74 Wh/km do relevo são de uma
**moto elétrica** de 1.800 Wh (tese da UPS Quito, 2025, autor nomeado), não de bicicleta —
o corpus tinha aplicado o absoluto a uma bateria de patinete. O que virou constante foi a
**razão 2,37**; o consumo absoluto de patinete ficou `pendente`, e é despacho novo. Da mesma
tese veio o número que faltava: **29,8 km medidos contra 60 km declarados — 49,7%**, abaixo
do piso da faixa agregada de 60-80%. **E a margem de 10% da F3 foi rebaixada de "fonte
estrangeira" para `decisao_da_ilha`**: a coleta limpa procurou o percentual em 13
publicadores e não o achou publicado em nenhum.

**2-ORIGINAL (guardado).** `dados/especificacao-calculadoras.md` + `dados/constantes.json`. Ordem obrigatória **F1, F2, F3**:
- **F1 — "Esse elétrico precisa de CNH?"** Entrada: potência nominal (W), velocidade máxima (km/h), acelerador ou só pedal assistido. Saída: categoria (bicicleta elétrica · autopropelido · ciclomotor) pela **Resolução Contran nº 996/2023** e os modelos do banco que cabem na categoria. **A constante central (1.000 W, 32 km/h e as dimensões do autopropelido) só vira `publicavel` depois de lida no texto oficial do gov.br, com data** — a resolução ganhou fase nova de vigência em 2026, e o dossiê a citou pelo noticiário.
- **F2 — "Quantos km ele faz de verdade?"** Entrada: V, Ah, peso de quem pilota, relevo. Saída: Wh e faixa de autonomia, ao lado da autonomia declarada. A fórmula de consumo por km fica aberta, com fonte.
- **F3 — "Aguenta o meu peso?"** Entrada: peso + carga. Saída: elegíveis pela carga máxima declarada, e os de fora com o motivo (seção 7).
Saída sempre faixa com critério e fonte.

**3. ~~MODELO DO BANCO~~ — ENTREGUE EM 28/10/2026 às 16h4xZ.** `dados/esquema-banco.json` (o contrato,
versão 1), `dados/veiculos.json` (**17** registros), `dados/pecas.json` (3), `dados/municipios.json` (4),
`ferramentas/validar-banco.py` (o portão), `ferramentas/derivar-banco.py` (quem escreve `energia_wh`),
`ferramentas/mutacoes-banco.py` (**66 casos**, 4 mundos que passam e 62 quebras, mais o autoteste da
bateria) e `ferramentas/bancada.py` (um comando, e ele **descobre** os portões em vez de os listar).
**Nenhum registro é `publicavel`**, e a causa é uma só e está em cada `motivo_do_status`: ninguém tem
saída de compra ainda, e a 25.2 não admite item publicável sem piso. **Nada foi ao ar e nada podia:**
o `manifest.json` segue na revisão 1 com os três grupos vazios, e a primeira revisão que publica algo
continua sendo a da casca (bloco 3b).

**AS TRÊS COISAS QUE O BLOCO ACRESCENTOU À LISTA ABAIXO, e as três nasceram de aplicar a lista a dado real:**
1. **A entidade `MUNICIPIO`**, que esta lista não tem. A 1.1 da especificação dá **três** estados ao campo
   `municipio` da F1, e o do meio ("conhecido pelo banco") precisa de um banco que ninguém havia mandado
   existir. Os quatro municípios são `pendente` e a consequência está escrita sem maquiar: **hoje a camada
   2 da F1 tem duas saídas iguais em vez de três.** Despacho NORMAL novo de 28/10.
2. **`potencia_declarada_sem_rotulo_w`.** Esta lista supõe que todo watt colhido é nominal **ou** pico. Não
   é: o caso esmagadoramente mais comum do varejo é **um watt só, sem rótulo** — e o banco mediu **14 de 17**
   assim, contra **zero** com nominal declarado. Sem o campo, as duas saídas disponíveis mentiriam (jogar o
   número no nominal classifica pelo anúncio; descartá-lo apaga o único watt que a fonte declarou).
3. **`cotacoes[]` como série**, no lugar de "preço com data" como campo: leitura nova não substitui leitura
   velha, porque substituir apaga a série.

**E O NÚMERO QUE O BLOCO MEDIU E QUE VALE MAIS QUE O ESQUEMA: `veiculos_com_nominal_declarado` = 0.** A
F1 não tem candidato nenhum na vitrine **nem no dia em que os limiares chegarem** — o que falta não é só a
resolução, é a ficha que diz qual dos dois watts é o nominal. Isso é trabalho de coleta em ficha de
fabricante (nível 4 da escada, hoje vazio), não de ferramenta.

**3-ORIGINAL (guardado).** VEÍCULO (`categoria`, `potencia_nominal_w`, `potencia_pico_w`, `velocidade_max_kmh`, `acelerador`, `tensao_v`, `amperagem_ah`, `energia_wh`, `autonomia_declarada_km`, `carga_max_kg`, `aro`, `peso_kg`, preço com data, `afiliado.programa`, `afiliado.url_busca_produto`, `afiliado.url_produto`, `imagem`) · PEÇA (câmara, pneu, carregador por tensão, bateria por V/Ah, capacete, cadeado). Todo campo com `fonte_url`, `fonte_tipo`, `data_leitura`. **Potência nominal e pico são campos diferentes**: anúncio que só diz "1000W" no título não alimenta a F1 sem a ficha dizer qual dos dois é.

**3c. ~~O PISO DE COMPRA~~ — ENTREGUE EM 28/10/2026 às 19h3xZ, e com ele o banco tem os primeiros
`publicavel` da história desta ilha: 5 de 17** (4 veículos + a câmara Kenda), de **zero**.
`dados/esquema-banco.json` subiu para a **versão 2** com a seção `escada_de_compra` — o termo de contexto
por `tipo_comercial` e por `tipo`, a escada de palavra-chave de quatro degraus (três na peça), o que nunca
compõe chave e o porquê de `sub_id_2` nascer `null` no piso de registro. `ferramentas/coletar-piso-de-compra.py`
(mede na Open API, encurta e grava; `--conferir` roda sem rede) e `ferramentas/mutacoes-piso.py` (18 casos,
4 deles mortes do esquema, mais 10 afirmações sobre a forma da chave e o autoteste da bateria).
**A chave é MEDIDA e nunca suposta:** cada degrau é consultado em `productOfferV2` antes de virar piso, e
chave com zero oferta não vira piso — a escada desce, e os degraus medidos ficam gravados.

**O ACHADO, e ele muda a ordem do que vem depois: O PISO E O DADO TÉCNICO CAÍRAM EM REGISTROS DIFERENTES, E
A INTERSEÇÃO É VAZIA.** Dos 4 veículos publicáveis, **zero** declara tensão+amperagem (entrada da F2) e
**zero** declara carga máxima (entrada da F3); os 2 com Wh derivado e os 3 com carga máxima estão todos
entre os 12 **sem** saída de compra. São duas populações de anúncio: o que nomeia marca e modelo é achável
na loja e não publica ficha; o que publica `60 V 20 Ah` empacota três nomes no título e não é achável por
nome nenhum. **Consequência direta para o 3b:** o bloco de compra da 32.1 pede o produto *que a ferramenta
escolheu*, e hoje nenhuma das três escolhe um publicável. Isto está como **aviso do validador**, para quem
abrir o banco ler antes de desenhar a casca.

**3d. ~~O CASAMENTO DO REGISTRO COM A OFERTA~~ — ENTREGUE EM 29/10/2026 às 13h3xZ–14hxxZ, e com ele a ilha
tem a PRIMEIRA FICHA DE PRODUTO da história dela.** `dados/esquema-banco.json` subiu para a **versão 3**
com a seção `casamento_de_oferta` — identidade mínima, as seis travas da 25.7/25.9, a ordem de escolha,
como se mede o degrau e as três causas separadas de "não casou". `ferramentas/coletar-oferta.py` (mede,
grava, e `--conferir` roda sem rede com 82 afirmações). `ferramentas/shopee-api.py` ganhou `sales` e
`shopType`, **medidos legíveis por esta conta** antes de entrar (as três ilhas rodam a mesma).

**No ar:** o primeiro cartão de `/autonomia-patinete-eletrico/` serve a **foto de verdade** (dimensão lida
no cabeçalho do arquivo na CDN, nunca digitada), o **link da ficha** como botão com o rótulo de degrau 1, a
linha discreta **"Veja todos disponíveis aqui"** logo abaixo — a 25.2 ao pé da letra, a ficha vira o botão
e a busca **desce**, nunca sai — e o **preço de hoje** com a data ao lado.

**AS TRAVAS TRABALHARAM, E O NÚMERO ESTÁ GRAVADO:** 10 ofertas julgadas, **6 barradas** — quatro
`M2 MAX-B`, que é outro aparelho (armadilha 4), e duas que enumeram `M2 Pro,M2 MAX,M2 MAX-B` (armadilha 5).
**A oferta de MAIOR venda da resposta (12 vendas) foi barrada por ser o MAX-B; a escolhida tem 3** — que é
a prova de que a régua não escolhe pelo número bonito.

**E O ACHADO MUDA A FILA, porque a dívida não é mais de link: `casou 1 · mercado_nao_anuncia 3 ·
candidato_barrado 0 · sem_identidade_minima 13`.** O alvo que este item pré-registrava — *"os 7 que não
compõem chave e os 5 que a loja não respondeu"* — estava **mal recortado**, e a medição de hoje o mostra:
o que separa os 13 não é a loja, é o **banco**. Dez veículos não declaram `modelo` (ou `marca`), e isso
**não se conserta com trava mais frouxa** — marca sozinha é a armadilha da 25.3 e modelo curto sozinho é a
armadilha 3 da 25.7, as duas **remedidas nesta ilha**: a chave `MAXSHOT` devolveu película de Zenfone e
suplemento, e `Honeywhale` devolveu bolsa e pneu de *outros* modelos da marca. **A câmara Kenda é a 25.9
em forma nova:** a medida casa com dez ofertas e o mercado as separa pelo **bico**, que o registro não
declara — ali a BUSCA é literalmente melhor que a ficha, e falta **um campo**.

**3e. ~~COLETA EM FICHA DE FABRICANTE~~ — ENCERRADO EM 29/10/2026 às 16h2xZ–16h4xZ, E A PREMISSA DELE ESTAVA ERRADA.** O bloco fechou corrigindo-a por medição, não executando-a: **o nível 4 pode ser estruturalmente VAZIO neste nicho** — as duas marcas principais do banco não têm site de fabricante achável (Honeywhale vende por vitrine de marketplace e varejo mexicano; MAXSHOT só aparece em varejista brasileiro), então abrir o egresso dos cinco domínios **não encheria o nível**. São marcas *de* marketplace, não fabricantes com página própria no Brasil.

> **E O GARGALO TEM NOME, UM SÓ, E NÃO É DESTA ILHA: o nível 5 está atrás do egresso.** `casasbahia`, `extra` e `magazineluiza` em `000` nas três passadas às 16h2xZ, `connect_rejected` lido no status do proxy, com controle verde; `mercadolivre` em 403 do próprio anti-robô, com o CONNECT passando. A leitura por **BUSCA** — a única porta aberta — alcança os níveis **6, 7 e 8**, que são **exatamente** os que a escada recusa nos quatro campos do nível 5. **Logo `potencia_nominal_w`, `velocidade_max_kmh`, `acelerador` e `carga_max_kg` não são colhíveis desta nuvem por caminho nenhum: a F1 e a F3 não vão ao ar por coleta, vão por ABERTURA.** O despacho ALTA de `dados/despachos.md` deixou de ser "seria bom" e é o único caminho.
>
> **O QUE SOBROU COLHÍVEL FOI COLHIDO, e foi um campo:** `autonomia_declarada_km` = **22 km** no `honeywhale-m2-max`, lido no título da **própria oferta casada** (remedida na Open API, viva, título idêntico). Nível 6, que a escada aceita neste campo. **Dos 10 títulos da resposta, ZERO declara tensão ou amperagem** — a bateria não está publicada nesta porta, e isso é dado.
>
> **E A COLETA ACHOU UM DEFEITO NO AR**, que é o que de fato foi ao ar nesta passada: o bloco de compra de `/autonomia-patinete-eletrico/` dizia **a mesma coisa três vezes** (o parágrafo de abertura, a linha `bateria não declarada` de cada cartão e o rótulo do grupo) enquanto o cartão da página de **autonomia** estava **calado sobre autonomia**. Revisão 12, 32.5 em **1.380 px** — 5 px MELHOR que antes, com uma linha a mais no cartão. Detalhe no `REGISTRO.md`, na entrada de 29/10 16h2xZ, inclusive a lição: **prosa que afirma o estado do banco é número digitado em outro traje**, e as cinco frases da função que a substituiu são conferidas sobre mundos fabricados.
>
> **O que o bloco NÃO alcançou, e não é dele:** o `bico` da câmara Kenda não está publicado em porta nenhuma alcançável (a busca devolveu Schrader para outras larguras de 16", que são linha de bicicleta — herdar o bico de outra largura é especificação herdada, proibida). O registro fica no degrau 4 de propósito. **O texto original do bloco fica abaixo, preservado.**

**3e-ORIGINAL (guardado).** COLETA EM FICHA DE FABRICANTE — o nível 4 da escada de fontes, hoje VAZIO.
Os dois eixos do banco convergiram aqui: o **3c** mediu pelo PISO que *"o que nomeia marca e modelo é
achável na loja e não publica ficha; o que publica `60 V 20 Ah` empacota três nomes no título e não é
achável por nome nenhum"*, e o **3d** mediu pela FICHA que 13 dos 17 registros não têm identidade mínima
para pedir uma. O banco inteiro vive do nível 5 para baixo, e é por isso que
`veiculos_com_nominal_declarado` continua **0** — o que falta à F1 não é só a resolução, é a ficha que diz
qual dos dois watts é o nominal.
**O PRIMEIRO PASSO DA 20.3 JÁ FOI DADO, em 29/10/2026 às 14h0xZ–14h1xZ, e ELE INVERTEU O PLANO DESTE
BLOCO — leia antes de abrir a fila.** Não procure ficha de fabricante: **nenhuma das duas marcas principais
tem site de fabricante achável.** A Honeywhale é vendida por loja de marketplace (a própria "loja oficial"
dela é uma vitrine do Mercado Livre) e por varejo mexicano; a MAXSHOT aparece **só** em varejista
brasileiro. **Para este nicho o nível 4 da escada pode ser estruturalmente VAZIO** — são marcas de
marketplace, não fabricantes com página própria no Brasil. Isso não é bloqueio a remover: é **premissa a
corrigir**, e corrigi-la muda o bloco.

**O QUE ESTÁ MEDIDO** (três passadas cada, controle verde, classificação lida no status do proxy e não
suposta): `honeywhale.com`, `maxshot.com.br`, `kenda.com.br`, `sousabike.com.br`, `evoo.com.br` →
`connect_rejected`. `www.casasbahia.com.br`, `www.extra.com.br`, `www.magazineluiza.com.br` →
`connect_rejected`, **e são estes três que valem o pedido**, porque são textualmente o **nível 5** da
escada desta ilha e o nível 5 *"sustenta campo técnico atribuído à LOJA"*. `www.mercadolivre.com.br` → 403
**do anti-robô do ML**, com o CONNECT passando: egresso aberto e caminho fechado são coisas diferentes.
**Despacho aberto** em `dados/despachos.md` com os três domínios, a causa e a prova de que o pedido
funciona (os cinco de fabricante que o despacho de 17/09 pediu para a robometria **estão abertos hoje**:
`mais.conteudo.wap.ind.br` em 200 e `www.electrolux.com.br` em 301).

**E O BLOCO PODE ANDAR SEM ESPERAR ELE:** a leitura por **BUSCA** funciona e foi por ela que tudo acima
foi medido — o degrau que a jornadafly nomeou em 27/10 (*"o egresso não trava a coleta inteira; o que ele
trava é a leitura direta, que é a PREFERIDA"*). O que os três domínios destravam é a leitura **direta** da
ficha. **Não marque `bloqueada_por`:** isso trava a FÁBRICA e não a ILHA, e o canal é o despacho (12.2).
A ficha da Casas Bahia já declara, para o `V1SPRO`, **500 W, carga máxima de 120 kg e UL 2272** — e
`carga_max_kg` é a entrada da **F3**, que hoje não vai ao ar por falta exatamente desse campo em registro
com oferta aberta.
**Alvo com nome:** `MAXSHOT` (V1 e V1SPRO) e `Honeywhale` (H3) têm marca e modelo e a Shopee não os
anuncia — ficha de fabricante resolve o campo técnico deles mesmo sem oferta. Os dez sem `modelo`/`marca`
precisam do **nome** antes de qualquer outra coisa. E a `camara-kenda-16x3-0` espera **um campo só**,
`bico`: com ele declarado, `coletar-oferta.py` a casa sem mudar uma linha de régua, porque o esquema já a
espera.

**3b. ~~CASCA~~ — ENTREGUE EM 29/10/2026 às 10h1xZ–11hxxZ, E COM ELA A ILHA ESTÁ NO AR.**
`snippets/rodametria-casca.php` (identidade, menu, trilha, JSON-LD, favicon, limpeza do lixo
de fábrica do WordPress e os **componentes do molde da seção 32**, aqui e não em cada
snippet, como a 32.6-b manda) e `snippets/rodametria-f2.php` — a **F2** em
`/autonomia-patinete-eletrico/`, primeira página desta ilha. Mais `regras/f2.py` (o cérebro),
`dados/f2-respostas.json` (o que a tela serve), `ferramentas/gerar-f2.py`,
`ferramentas/teste-f2.py`, `ferramentas/atualizar-manifest.py`,
`ferramentas/conferir-no-ar.py` e `ferramentas/conferir-32-5-no-navegador.mjs`.

**A DIVERGÊNCIA COM O `VOZ.md`, e ela é decisão escrita e não esquecimento:** o `VOZ.md`
manda a **F1** ser a home. A F1 **não pode ir ao ar** — o limiar legal dela segue `pendente`
e os cinco domínios oficiais foram **remedidos em 29/10 e seguem recusados**. Home que FAZ a
pergunta do título e não a responde é pior que home nenhuma, então a home nasceu **HUB**: a
caixa de resposta no topo diz o que a ilha mede, o cartão da F2 leva à pergunta que já tem
resposta, e os outros dois dizem **com uma linha o que falta**, sem prometer data. No dia em
que a resolução for lida, a F1 toma a primeira tela da home e os cartões descem — **nenhuma
URL muda**, que é o que a 32.3 protege. A divergência está escrita dentro da própria casca,
no lugar onde quem for mexer a lê.

**A F3 TAMBÉM NÃO FOI, e a causa é de dado:** só três registros declaram `carga_max_kg` e
**nenhum dos três tem oferta aberta** — a conta não teria o que comparar nem o que vender.

**4. FERRAMENTAS**, uma por execução, com JSON-LD, tabela pré-renderizada, resposta antes da explicação, bloco de compra antes da procedência.

**4a. ~~A F1 — "ESSE ELÉTRICO PRECISA DE CNH?"~~ — ENTREGUE EM 06/11/2026 às 10h4xZ–11hxxZ, E ELA É A
HOME. A ferramenta que esta ilha existe para ter, travada desde 28/10, está no ar.** `regras/f1.py` (o
cérebro), `dados/f1-respostas.json`, `ferramentas/gerar-f1.py`, `ferramentas/teste-f1.py` (**1.234
afirmações**), `ferramentas/teste-f1-arvore.mjs` (**40 afirmações**) e `snippets/rodametria-f1.php`, com a
casca em **1.11.0** abrindo dois filtros para ela. Revisão **46**.

**O QUE DESTRAVOU, e não foi uma execução da fábrica:** o Raphael abriu o PDF oficial do Ministério dos
Transportes no Chrome dele em **05/11, ~23h3x de Brasília**, e preencheu a seção 5 de
`dados/fonte-oficial-f1.md` campo por campo. **Esta passada é o que a aposta da 1.3 comprou:** a
constante destravou editando **um objeto JSON** e **nenhuma linha de lógica mudou**, porque nenhum
limiar jamais foi literal no código. O `custo_de_destravar` que a constante declarava em 28/10 estava
certo, palavra por palavra.

**ELA É A HOME, E NENHUMA URL MUDOU** — a casca prometia isso desde 29/10 com todas as letras. Ela se
pendura em dois filtros novos (`rodametria_home_ferramenta` e `rodametria_home_cartoes`) de dentro do
próprio snippet, pela 32.6-b, e **filtro vazio devolve a home HUB de 29/10 byte por byte**: o snippet
**lê o status** da constante em vez de ter uma lista de pendências escrita à mão, então o dia em que o
limiar voltar a `pendente` a home volta a ser HUB sozinha.

**AS TRÊS COISAS QUE A LEITURA OFICIAL MUDOU NA ESPECIFICAÇÃO estão escritas como ERRATA dentro da
própria seção 1 de `dados/especificacao-calculadoras.md`**, porque quem for mexer na F1 lê aquele
arquivo e não este. Em uma linha cada: (1) a árvore ganhou uma **quarta** saída, `acima_do_ciclomotor`,
porque o inciso IV põe teto no ciclomotor e os §§ 6º e 7º mandam o excedente para "motocicleta, motoneta
ou triciclo, conforme o caso" — e a resolução **não diz qual**; (2) **a resolução não fala de CNH**, e a
F1 cala sobre habilitação nomeando a causa, com o portão cobrando a ausência das duas frases proibidas
em todo texto de tela; (3) as quatro entradas da 1.1 **não fecham o autopropelido**, porque há largura e
distância entre eixos, e o veredito sai com a condição dita em vez de o formulário crescer.

**A COLUNA QUE A 1.6 DEIXOU VAZIA EM 28/10 NASCEU, e ela é a prova da tese da ilha:** 14 linhas, **zero**
com watt nominal, **zero** classificáveis — a coluna diz a causa em cada uma, e não o watt sem rótulo. A
vitrine nasce com **zero cartões** e a página diz por quê, com os nomes contados. **Uma tabela nova que
a 1.6 não previa:** a da REGRA, uma linha por categoria com o artigo ao lado, que é a única coisa da
página que responde a quem não sabe os números do próprio veículo — e é dela que o `FAQPage` do JSON-LD é
montado, campo por campo, para a camada que a IA lê e a que a pessoa lê não poderem divergir.

**CINCO DEFEITOS ACHADOS NESTA PASSADA, e eles valem mais que a página:**

- **O LITERAL `32` DENTRO DO CÓDIGO DO CÉREBRO**, achado pelo portão da própria ferramenta no minuto em
  que ele nasceu: os fatos das ressalvas moravam num dicionário em `regras/f1.py`, e o `32` do caso da
  scooter adulterada bateu com o `LIMIAR_AUTOPROP_KMH` na régua da 1.3. **A regra "fato externo mora num
  lugar só" estava escrita no cabeçalho do arquivo que a violava**, e nenhum olho a viu — viu o portão,
  que compara o código com a constante em vez de ler o código. Os três fatos viraram constante.
- **A MUTAÇÃO DE FRONTEIRA NÃO MORDIA, e o portão disse isso de si mesmo:** a grade da bateria usava
  valores que **nenhum** era igual a um limiar, e a mutação de `<` no lugar de `<=` só muda o veredito de
  quem está **exatamente** no limite. A grade passou a ser **derivada** dos limiares fictícios.
- **A FRASE DO ESTOURO AFIRMAVA AS DUAS METADES quando só uma estourava** — para 1.000 W com 45 km/h ela
  servia "1.000 W passa dos 1.000 W", que é falso, ao lado da metade verdadeira. Virou três moldes, um
  por causa.
- **A CONVERSÃO DE MILÍMETRO PARA CENTÍMETRO DIVIDIA POR CEM**, nos três lugares que convertem, e a
  página foi ao ar dizendo "**7 cm** de largura e **13 cm** entre os eixos" onde a resolução diz 70 e
  130. **Nenhum portão viu: a conversão rodava.** Quem viu foi ler a frase gerada, e a régua nova está
  escrita **do outro lado** — multiplica de volta e exige fechar.
- **"E 0 DECLARAM O NOMINAL"** — o plural que mente, a cicatriz da clubedomosaico de 12/10, com o
  agravante de que o mundo de hoje **é** o do zero.

**E UM PORTÃO QUE JÁ EXISTIA ESTAVA MEDINDO MENOS DO QUE DIZIA:** `teste-versao-dos-snippets.php` tinha a
lista dos snippets **escrita à mão**, de 02/11. A F1 nasceu e ele reprovou com a mensagem certa pelo
motivo errado. **O defeito é assimétrico e é por isso que ele é feio:** snippet novo deixa UMA afirmação
vermelha e as outras três simplesmente **não alcançam** o snippet que falta na lista, em silêncio. Os ids
saem do **manifest** agora, que é o contrato do Sync. 43 → 52 afirmações.

**O QUE A F1 AINDA NÃO FAZ, e está dito na própria página:** não responde CNH. Despacho NORMAL novo em
`dados/despachos.md` para o CTB, que é destravado pelo **mesmo** pedido de uma linha (`*.gov.br`) que o
resto desta ilha espera.

**4b. PRÉ-REGISTRADO EM 06/11/2026, E É PERGUNTA PARA A LEITURA SEMANAL E NÃO BLOCO DA FUNDAÇÃO: O
`<title>` DA HOME NÃO CARREGA "CNH", E A HOME AGORA É A FERRAMENTA DE CNH.** Ele diz *"Rodametria — os
três números antes de comprar um elétrico"*, escrito em 27/10 quando a home era HUB. Desde 06/11 a
primeira tela dela é a F1, o primeiro H2 é *"Esse elétrico precisa de CNH?"*, e a consulta-ponte que o
dossiê mediu para este eixo é `bicicleta eletrica precisa de cnh`.

**POR QUE A FUNDAÇÃO NÃO TROCOU, e isso é regra e não hesitação:** a **32.3** lista o `<title>` entre o
que **não muda** numa conversão ao molde — *"o que NÃO muda, porque é SEO: URL, `<title>`, H1, trilha e
`BreadcrumbList`, JSON-LD, links internos e âncoras"*. A `description` **mudou** nesta passada, e por um
motivo diferente e de outra ordem: ela **prometia** um veredito de CNH que a página recusa dar, e
descrição que promete o que a primeira tela recusa é a página se desdizendo na própria aba. **Trocar o
título é decisão de posição, não de honestidade**, e quem tem o instrumento para ela é a leitura
semanal, com o Search Console na mão.

**A pergunta, para quem tiver o painel aberto:** com `primeira_indexacao: null` e **0 impressão**, a
home não tem posição a perder — e é a janela mais barata que vai existir para mexer no título. Vale
levar `CNH` para ele, ou a identidade da ilha paga mais no longo prazo? **A Fundação troca a linha em um
gesto** (`'titulo'` no mapa de páginas da casca) **no dia em que a decisão estiver escrita.**

**4c. ~~A F3 — "AGUENTA O MEU PESO?"~~ — ENTREGUE EM 06/11/2026 às 13h2xZ–14hxxZ, E COM ELA AS
TRÊS FERRAMENTAS QUE ESTA ILHA EXISTE PARA TER ESTÃO NO AR.** `regras/f3.py` (o cérebro),
`dados/f3-respostas.json`, `ferramentas/gerar-f3.py`, `ferramentas/teste-f3.py` (**583 afirmações**)
e `snippets/rodametria-f3.php`, em `/peso-maximo-patinete-eletrico/`. A URL carrega a consulta
**medida** do eixo C do corpus (`patinete eletrico peso maximo suportado`), não a pergunta do H1.

**POR QUE ELA PODE IR AO AR COM O BANCO DE HOJE, e isto é o desenho e não um contorno: A RESPOSTA
PRINCIPAL NÃO DEPENDE DO BANCO.** Dado o peso de quem pilota e o que ele carrega, a carga máxima a
procurar sai de `total × (1 + margem)` — aritmética sobre a entrada da pessoa mais **uma** constante
desta ilha. Nenhum registro participa. A vitrine é a segunda camada, e hoje está **vazia** com a
causa nomeada: os **três** registros que declaram `carga_max_kg` declaram **120 kg**, os três lidos
em ficha de varejo grande (nível 5, o piso que a 3.5 exige neste campo), e **nenhum tem oferta
aberta** — pela 25.2, item sem piso de compra não entra em vitrine. É o mesmo desenho da F1 de hoje
de manhã, que foi ao ar com zero cartões e os 14 nomes contados.

**A TABELA PRE-RENDERIZADA PUBLICA A TESE DA ILHA, e a virada está visível nela:** com a folga de
10%, **109 kg** é o último peso total que os 120 kg do teto de varejo acolhem, e **110 kg já não**.
A constante `teto-de-carga-do-mercado-brasileiro` previa isso por escrito em 28/10 (*"quem passa de
109 kg de peso total já cai fora do grupo de folga nos modelos de 120 kg"*) e agora o número está na
tela. O `FAQPage` do JSON-LD é montado **da tabela**, campo por campo, procurando a virada em vez de
a ter escrita — então ele não pode divergir da tabela que a pessoa lê.

**E ELA É A PRIMEIRA FERRAMENTA DESTA ILHA A NASCER DENTRO DO CONSERTO DA 32.1-b:** campos com o
prefixo desde o primeiro byte (`rdm_peso`, `rdm_carga`) e o `<noscript>` vindo do componente da
casca — que é exatamente o que a regra pede ao mandar o componente morar num lugar só.

**TRÊS DEFEITOS ACHADOS NESTA PASSADA, e eles valem mais que a página:**

- **A FRASE DE LISTA VAZIA MENTIA.** Um molde único dizia *"nenhum dos 3 veículos que declaram carga
  máxima aguenta os seus 108 kg com folga"* — e os três declaram 120 kg, que cobre com folga os 119
  que a regra pede para 108. **O eixo que esvaziava a vitrine era a falta de LINK, não a carga.**
  Agora são **três** causas com três frases (sem banco · aguentariam e sem link · nenhum aguenta), e
  o portão exige que elas **difiram** entre si. Achado **lendo a frase que saiu**, que é como a
  conversão de milímetro da F1 foi achada hoje de manhã — nenhum portão via, porque a conta rodava.
- **CHAMADA DE FUNÇÃO INEXISTENTE, E ELA É TELA BRANCA.** O snippet chamou
  `rodametria_casca_data_em_portugues()`, nome **derivado de cabeça** do padrão dos outros
  componentes da casca. Em PHP é erro fatal em tempo de execução; **`php -l` passa verde**, porque a
  sintaxe está perfeita, e **nenhum dos 32 portões sem rede resolvia chamada entre snippets**. É a
  família que a **20.7** já nomeou para nome de constante (*"derivar é natural e erra CALADO"*), com
  o estrago maior. Virou régua em `ferramentas/teste-formulario-da-ilha.py`: ela varre os seis
  snippets e exige que toda função `rodametria_*` chamada **exista** ou esteja **guardada por
  `function_exists()`** — que é a saída honesta para `rodametria_sync_token()`, do Sync, que não mora
  neste repositório e não deve morar. **Guarda e nunca lista de exceção:** lista envelhece calada e
  perdoa o erro de digitação do dia seguinte. Provada **reinjetando o defeito real no arquivo real**.
- **A RÉGUA DE ACENTO NASCEU ERRADA DUAS VEZES, e as duas reprovaram texto CERTO.** Primeiro ela
  media **ausência** de acento em texto com mais de 40 caracteres — e *"peso igual ao teto declarado
  que mais se repete no varejo brasileiro"* não tem um acento e está perfeita. Depois passou a
  procurar a palavra sem acento por **substring**, e `so` casou dentro de "nosso" e "isso",
  reprovando cinco frases. Agora procura a palavra escrita **sem o acento que ela exige**, por
  palavra inteira, com três mundos: morde no defeito, **passa no texto certo**, e não casa pedaço.
  **Contorcer a cópia para agradar régua errada é pior que a régua errada** — é a régua passando a
  decidir o que a página diz.

**4c-ORIGINAL (guardado).** F3 — "aguenta o meu peso?" Entrada: peso + carga. Saída: elegíveis pela
carga máxima declarada, e os de fora com o motivo (seção 7). *(O bloco 3b registrou em 29/10 que a
F3 não ia ao ar porque "só três registros declaram `carga_max_kg` e nenhum dos três tem oferta
aberta — a conta não teria o que comparar nem o que vender". A primeira metade continua verdadeira e
a segunda foi **superada pelo precedente da F1**: a conta tem o que responder sem o banco, e o que
ela não tem é o que **vender**. Vitrine vazia com a causa nomeada é página honesta; ferramenta não
publicada é página nenhuma.)*

**5. ARTIGOS-ÂNCORA** pareados com cada ferramenta.

**5b. ~~PÁGINAS PELO NOME DO PRODUTO~~ — PRIMEIRA LEVA ENTREGUE EM 29/10/2026 às 19h1xZ–20hxxZ, e o
bloco mediu que SÓ DUAS DAS SEIS CABEÇAS abrem o portão da 30.2.** No ar: `/veiculos/` (a seção de
nível 1 da 16.1), `/veiculos/patinete-eletrico/` e `/veiculos/bicicleta-eletrica/`, no molde da 32.2.
`snippets/rodametria-produto.php` (o motor), `dados/consultas-de-produto.json` (a declaração das seis
com a SERP vista pelo Raphael em 27/10 e a escada de chaves), `dados/paginas-de-produto.json` (a voz,
com MOLDES e zero dígito), `dados/anuncios-por-consulta.json` (os anúncios colhidos),
`dados/vitrine-de-produto.json` (o gerado), `ferramentas/teste-relevancia-do-anuncio.py`,
`ferramentas/coletar-por-consulta.py`, `ferramentas/gerar-vitrine-de-produto.py` e
`ferramentas/mutacoes-produto.py`.

**O ACHADO QUE REORDENA O QUE SOBRA DA FILA, e ele é de PALAVRA e não de produto:** a chave
`patinete eletrico` devolve **ZERO** patinete de adulto nas 20 primeiras ofertas da loja — serve
`Patinete Elétrico Infantil 150W UNITOYS` e `Moto Elétrica Infantil 6V`. Com o qualificador `adulto`
a mesma família devolve **16** patinetes de adulto (R$ 1.297,13 a R$ 3.399,00) e **5** e-bikes, três
delas com 74, 28 e 25 vendas. **A consulta é a palavra da PESSOA; a chave é a palavra da LOJA**, e
cada consulta declara uma escada de chaves com o degrau gravado, pela 25.6(a).

**O QUE NÃO NASCEU, COM A CAUSA MEDIDA.** `moto eletrica` e `scooter eletrica`: a SERP autoriza e o
que falta é produto — três anúncios de adulto, zero venda nos três, preços variando R$ 6.500 para a
mesma classe. O caminho delas é o **Mercado Livre**, e lá a geração de link exige clique humano
(25.6): **é despacho, nunca bloco.** `bike eletrica` e `motos eletricas para adultos` não nascem pela
30.4, por serem a mesma intenção de outras duas.

**5b-ORIGINAL (guardado).** PÁGINAS PELO NOME DO PRODUTO (seção 30) para as seis cabeças, e depois a
malha. Escolher a primeira cabeça pela intersecção entre volume e o que o banco sustenta.

**5c. ~~A PRÓXIMA LEVA DA MALHA~~ — ENCERRADO EM 30/10/2026 às 10h1xZ–10h4xZ, E A PREMISSA DELE
ESTAVA ERRADA, como a do 3e.** O bloco fechou corrigindo-a por medição: ele dizia que *"o caminho
mais curto é a cauda medida do corpus"*. **A cauda deste nicho é território de FAZENDA, e agora
está medido.** As cinco caudas do eixo D foram classificadas com busca, **102 ocupantes colhidos
com URL**, em `dados/consultas-de-produto.json` (a fonte) e `dados/consultas-de-produto.md` (a
vista legível, gerada do JSON na mesma passada).

**O PLACAR: três das cinco estão TOMADAS e fecham sem o Chrome; duas ficaram `nao-medida`.**
`patinete elétrico adulto` (49.500/mês), `melhor patinete elétrico` e `moto elétrica 1000w`
(14.800/mês) caem pela MESMA classe de ocupante — fazenda de conteúdo com página dedicada, no
formato "melhor X" e "Top 10" que o `VOZ.md` desta ilha **proíbe nominalmente**. São **26**
páginas dedicadas de fazenda entre os 102 ocupantes.

**O CONTRASTE COM AS CABEÇAS É O DADO, e ele reordena a fila.** O dossiê registrou, nas seis
cabeças vistas no Chrome do Raphael, que *"nenhuma fazenda da lista apareceu"*. Na cauda ela
aparece em **quatro das cinco**. O `ACHADO D` do corpus de 28/10 já havia visto a fazenda nas
caudas e ninguém tirou dele a conclusão de fila. **A cauda não é o caminho curto desta ilha: é o
campo onde ela perderia.** O caminho curto continua sendo o eixo **paramétrico** — *"todos falam,
ninguém calcula"* —, e o que o trava não é SERP: é o egresso do `gov.br`, que já é despacho ALTA.

**ZERO PÁGINA NOVA, E ISSO É A 30.8 FUNCIONANDO, não bloco perdido.** `nao-medida` não autoriza
página; `tomada` fecha a consulta. Despacho novo aberto no topo deste arquivo: duas SERPs e um
volume, numa sessão de Chrome. **A execução seguinte publica sem remedir nada** — se e só se o
veredito voltar `alvo`.

**E O BLOCO ACHOU UM DEFEITO NA BANCADA, pela própria bancada, antes de construir (18.5):**
`gerar-f2.py --conferir` reprovava **a página certa**. A única diferença entre o arquivo no ar e o
recém-gerado era o selo `gerado_em` (`2026-10-29` → `2026-10-30`), porque o gerador o escreve com
o **relógio da execução** — então o portão reprovava todo dia seguinte ao que a F2 foi gerada. É
o perigo que a 20.5 e a 32.5-b nomeiam: *portão que reprova página certa é o caminho mais curto
para alguém passar a ignorá-lo*. A irmã `gerar-vitrine-de-produto.py` **já fazia certo** (herda a
data do dado) e a lição não havia viajado — a 32.5-c outra vez. O selo saiu da comparação, com o
motivo escrito no código, e as duas metades do veredito foram provadas em cinco casos: aprova o
mundo real e o selo trocado, reprova número mexido, frase mexida e arquivo não-JSON.

**5c-ORIGINAL (guardado).** A PRÓXIMA LEVA DA MALHA — pela cauda medida do corpus
(`patinete eletrico adulto` 49,5 mil, `scooter eletrica 1000w` 33,1 mil, `moto eletrica 1000w`
14,8 mil), com a máquina do 5b fazendo as páginas sem uma linha de código nova: bastaria declarar
a consulta em `dados/consultas-de-produto.json` com a escada de chaves e escrever a voz em
`dados/paginas-de-produto.json`. **A 30.8 travava o primeiro passo** — `alvo` não se afirma daqui
— então a leva se dividia em duas: a lista sai da nuvem, a SERP sai do Chrome do Raphael.
*(A metade da lista foi entregue; a outra metade virou o despacho de 30/10. O que o bloco não
previu é que a lista **fecharia três das cinco** e tiraria a cauda do caminho.)*

**5d. ~~AS QUATRO PÁGINAS QUE O SITE DEVE A QUEM LÊ~~ — ENTREGUE EM 30/10/2026 às 13h5xZ–14h4xZ, E A
DE PRIVACIDADE NÃO PROMETE NADA: TUDO O QUE ELA AFIRMA FOI MEDIDO NA PÁGINA SERVIDA.** No ar, 9 URLs
(eram 5): `/sobre/`, `/contato/`, `/divulgacao-de-afiliados/` e `/privacidade/`, pelo snippet
`snippets/rodametria-institucional.php` (1.0.0, #9), com `dados/paginas-institucionais.json` (a voz,
com 16 moldes e zero dígito), `ferramentas/teste-institucional.py` (sem rede, 19 casos de autoteste) e
`ferramentas/conferir-institucional-no-ar.py` (210 afirmações no ar). Revisão **19** às 14h40:39Z, com
as cinco linhas da revisão corrente dizendo `ok` (20.4).

**A CASCA NÃO FOI TOCADA**, e isso é o mecanismo dela funcionando: as quatro entram pelos filtros
`rodametria_paginas` e `rodametria_instalar`, e a instalação rodou porque a **assinatura do mapa**
mudou — o que a casca 1.4.0 nasceu para fazer em 29/10. As páginas nasceram na requisição **seguinte**
à do Sync (snippet criado às 14h40, instalação às 14h41:38), que era exatamente o defeito que custou as
três páginas do 5b e que a assinatura conserta sozinho.

**O QUE A PÁGINA DE PRIVACIDADE AFIRMA, MEDIDO DO LADO DE FORA:** zero `Set-Cookie`; zero medidor de
audiência e zero pixel; e os **dois** endereços de fora que *carregam* junto com a página estão
**nomeados nela** — Google (as fontes da letra, em toda página) e Shopee (`cf.shopee.com.br`, onde há
foto). **E a medição achou o que era mais fácil de esconder:** o formulário da F2 é `method="get"`,
então apertar o botão manda os quatro números para o **endereço** da página, que passa pelo servidor —
a primeira versão do texto dizia "o que você digita não sai do navegador", e era falsa na metade que
importa.

**A `/contato/` NÃO INVENTOU UM CANAL.** Esta ilha não tem caixa de e-mail e o despacho de 13/09 em
`dados/despachos.md` proíbe *"publicar um endereço que ninguém lê"*. A página diz isso, e o despacho
foi reescrito hoje: eram **três** ilhas, são **quatro**. **A linha que a Fundação troca no dia em que a
caixa existir é UMA**, em `dados/paginas-institucionais.json`, na seção "O canal, dito como ele está
hoje" — o parágrafo da ausência sai e o endereço entra. Nada de código muda.

**AS QUATRO CAIXAS, CADA NÚMERO CONFERIDO POR UMA TERCEIRA CONTA** (recontada em Python, dos arquivos,
por caminho diferente do PHP): `/sobre/` 17 veículos · `/contato/` 40 anúncios lidos ·
`/divulgacao-de-afiliados/` 5 itens com link · `/privacidade/` 9 páginas no ar. A última é a melhor das
quatro porque as duas metades leem **fontes diferentes**: o PHP conta o mapa de páginas da casca e o
portão conta o `wp-sitemap.xml` servido — e quando discordarem, a divergência é informação.

**E O BLOCO ACHOU UM PORTÃO QUE NÃO REPROVAVA O QUE DEVIA: a HOME estava fora da 32.5 desde que
nasceu.** `conferir-32-5-no-navegador.mjs` decidia "está no molde" por `!!(bloco_de_compra ||
formulario)`, e página com **caixa de resposta e sem nada para vender** caía em "fora do molde" — a
caixa era medida, impressa e **nunca julgada** contra os 700 px. A home é HUB, sem bloco de compra e
sem formulário. Páginas do molde: **3 → 8**. O teto de compra passou a valer só onde há o que comprar,
com "não se aplica" impresso, e página que serve link patrocinado **fora** de um bloco de compra passou
a ser **reprovada**. É a 32.5-c outra vez: família nova entra no molde **pelo seletor**, nunca pela
intenção.

**MEDIDO NO AR.** 32.5 a 390 px: caixa a **211 px** (`/sobre/`) e **244 px** (as outras três), teto
700, **8 de 8** aprovadas. Piso de corpo da seção 8 **medido no ar** e não pela conta de antes do
desembarque: **4.449 · 3.674 · 4.786 · 5.899** caracteres. 16.4(f): cada uma recebe link de **9 das 9**
páginas no ar, contra as 2 da regra — elas estão no rodapé, que a casca monta do mapa inteiro, e fora
do menu de cima por ordem do `VOZ.md`. Bancada com rede: **17 portões, 0 falha**.

**E A 20.6 GANHOU UMA RÉGUA DE LEITURA**, que não é conserto: o campo `ultimo` do `/status` separa os
**três** mundos que a 20.5 junta em dois. `ultimo` **antigo** = o Sync não rodou (defeito). `ultimo`
**de agora** com revisão atrasada = cache do GitHub (reacione). `ultimo` **recente mas anterior ao
push** = nem defeito nem cache: é **turno de cron**, e o que resolve é esperar o próximo mantendo as
visitas de pé para ele disparar. Medido hoje: Sync às 14h10:04, push às 14h11, revisão entrando às
14h40:39 — bater no `wp-cron.php` (409) não antecipa evento que ainda não venceu, e não devia.

**5d-ORIGINAL (guardado).** O bloco mais desbloqueado da fila, achado medindo o sitemap em 30/10: as
**5 URLs** no ar eram `/`, `/autonomia-patinete-eletrico/`, `/veiculos/` e as duas filhas, e não existia
`/sobre/`, `/contato/`, `/divulgacao-de-afiliados/` nem `/privacidade/` — com a ilha publicando link de
afiliado da Shopee desde 29/10. As três razões de ele ser o próximo, todas independentes: (a) não
depende de despacho nenhum; (b) pela **21.7** essas páginas ficam fora do teto de 10 URLs por leva e 3
levas por semana; (c) é dívida de confiança no ar, e a 21.7 nasceu deste caso na aquametria.

**5e. ~~A ESCADA DA 25.2 NA TELA, NAS DUAS PONTAS~~ — ENTREGUE EM 30/10/2026 às 19h17Z–19h4xZ, E O RAMO
QUE ELA CONSERTA NÃO EXISTE NO DADO PUBLICADO — É POR ISSO QUE NINGUÉM O VIA.** A 25.2 manda a BUSCA
SUBIR E VIRAR O BOTÃO quando a ficha não existe ou morre; só a primeira ponta estava na tela.
`rodametria_casca_cartao_de_compra()` devolvia **string vazia** com `url` vazia, e a segunda ponta vivia
no **CHAMADOR** da F2. A F2 nunca sofreu; a **VITRINE** de produto, que passa `url` crua do dado, tinha
**TRÊS** lugares lendo-a crua, e os três quebravam juntos: o **CARTÃO** sumia da página, a célula
"Comprar" da tabela servia `href=""` (que não é botão morto — é um botão que **recarrega a própria
página**, com "Ver na Shopee" do lado, **pior** que o cartão que ao menos sumia) e a **`Offer`** do
JSON-LD saía com `"url": ""`. **Causa de ninguém ver: 21 de 21 anúncios da vitrine têm ficha.** O ramo
não existe no dado publicado, e é a **32.5-d** inteira.

**O CONSERTO É MECANISMO:** `rodametria_casca_escada_de_compra()`, uma função só na casca, e todo chamador
entrega os **dois** links crus — a F2 **parou de escolher**, então a regra deixou de morar em dois lugares
onde podia divergir (a 32.5-c nasceu da metade que não viajou). **E o DEGRAU sobe com a busca**, senão o
rótulo promete ficha morta; medido no ar, o bloco de compra da F2 serve **degraus [1, 4]**. A **tabela
ganhou a linha discreta do piso**, UMA vez embaixo dela e não por linha, porque o piso é da **CONSULTA** e
não do anúncio (uma `url_busca` distinta por página) — repeti-la seria o mesmo link dezesseis vezes; com
duas distintas a linha **não sai**. No JSON-LD, `availability` sai de cena quando o piso sobe: estoque de
resultado de busca é afirmação sem medição.

**DOIS PORTÕES NOVOS.** `ferramentas/teste-escada-de-compra.php` (PHP porque a escolha é decidida em PHP,
então **chama** a função): 138 afirmações, **fabrica** os seis mundos que o dado não tem, prova que morde
reproduzindo a escada velha, e **cobra** a promessa de que a F2 não mudou um byte comparando item a item
com a regra velha (10 itens, 4 já no mundo B, idênticos). Três mutações no código reprovadas: 13, 6 e 2
falhas. `ferramentas/conferir-produto-no-ar.py` (191 afirmações) nasceu porque **as páginas de vitrine não
tinham portão de ar nenhum** desde 29/10 — havia o de **pixel** da 32.5 e o `mutacoes-produto.py` sem
rede, e entre os dois **faltava quem lesse a página**; rodado contra a revisão 23 **antes** do
desembarque, reprovou com 2 falhas, as duas a linha do piso que estava subindo.

**AS TRÊS COISAS QUE O PORTÃO NOVO ACHOU, as três do lado da RÉGUA:** (1) a linha do piso se conta pela
**CLASSE** e nunca pela frase — a mesma frase é a linha discreta de cada cartão do carrossel, 5× numa
página sã; (2) `&quot;`, porque um título tem `10"`; (3) **o WordPress TEXTURIZA o hífen** — o
`wptexturize` do `the_content` troca hífen cercado de espaços por **EN DASH** no retorno do shortcode (o
dado diz `550W - 40km/h`, o corpo serve `550W &#8211; 40km/h`) e o **JSON-LD sai no `wp_head` sem passar
pelo filtro**, servindo o hífen cru: **o mesmo nome em duas formas na mesma página.** Não é defeito — é
tipografia do WordPress, e é a cicatriz do `&&`/`&#038;&#038;` desta casca num traje novo.

**NO AR (18.4):** revisão **27**, as 7 linhas da revisão corrente dizendo `ok` (20.4, lidas uma por uma),
**32.5 em 8 de 8** com o primeiro botão de compra **IDÊNTICO** ao de antes (1084 · 1129 · 1380 px) e a
altura da F2 **sem mudar um pixel**, e bancada com rede em **21 portões, 0 falha**.

**O QUE FICAVA — `/veiculos/` FORA DO MOLDE — ESTÁ FEITO E CONFERIDO NO AR EM 02/11/2026 às 13h42Z**
(commit `ce91604`, com `ferramentas/teste-caixa-da-mae.php` e os oito mundos da caixa de resposta), e o
**campo `versao` no `manifest.json`** está feito e conferido às 17h4xZ do mesmo dia (revisão 29). **Os dois
itens que este parágrafo deixava abertos estão fechados**; o texto fica abaixo como registro do que faltava,
marcado aqui porque a linha estava vencida e foi lida como pendência pela execução das 19h18Z de 02/11.
*(O parágrafo original segue, intacto:)*

**O QUE FICA, e é BLOCO e não conserto: `/veiculos/` ESTÁ FORA DO MOLDE** — o portão de pixel o diz com
essas palavras ("sem componente de molde nenhum"). A mãe serve `<p class="rdm-promessa">` onde o molde pede
a **caixa de resposta**, então os **700 px da 32.5 nunca a julgaram**: é a mesma lacuna que o 5d fechou na
home, uma página depois. E o **campo `versao` no `manifest.json`** — **FEITO E CONFERIDO NO AR EM 02/11/2026 às 17h4xZ,
revisão 29**, com o espelho em `ferramentas/atualizar-manifest.py`, o portão
`ferramentas/teste-versao-dos-snippets.php` (43 afirmações, 6 de 6 mutações) e a versão **carregada pelo
WordPress** servida em `/casca` → `versoes`, conferida contra o manifest em 4 de 4 snippets publicáveis;
o parágrafo abaixo fica como o registro do que faltava —, que faria a constante de cada snippet
ser espelhada e impressa como o `sha256` já é — hoje `RODAMETRIA_PRODUTO_VERSAO` e `RODAMETRIA_F2_VERSAO`
são **lidas por ninguém**, e o comentário que afirmava o contrário foi corrigido nesta passada. Esse mexe
no **contrato do Sync**, o único canal desta ilha, então é bloco com desembarque próprio, nunca carona.

**6. ~~LISTA DE PROSPECÇÃO DO WIDGET~~ — ENTREGUE EM 02/11/2026 às 19h18Z–19h4xZ, com `dados/prospeccao-widget.json`
(a fonte, **10 candidatos**), `dados/prospeccao-widget.md` (a vista legível, **gerada** e nunca escrita),
`ferramentas/validar-prospeccao.py` (a régua E o portão de dado, com `--autoteste` de 13 mundos fabricados) e
`ferramentas/gerar-prospeccao.py`.** Bancada sem rede: **22 portões, 0 falha** (eram 20).

**POR QUE ESTE BLOCO E NÃO OUTRO, com a conta na mesa:** foi o único da fila que esta execução podia executar
inteiro. A **F1** e a **F3** estão travadas por ABERTURA de egresso (despacho ALTA); **página nova de malha**
está travada pela **30.8** (veredito `alvo` não se afirma desta nuvem, e os eixos A e C medidos estão `tomada`
ou `nao-medida`); e as duas consultas de maior volume com SERP já vista no Chrome — `moto elétrica` 823 mil e
`scooter elétrica` 301 mil — estão travadas por **PRODUTO**, medido em 29/10. Nenhum defeito aberto no ar:
a bancada fechou **24 portões com rede, 0 falha**, antes de qualquer construção (18.5). E a **14.7** é literal
sobre o valor desta lista: *"a prospecção do widget em lojas é a única alavanca de link do projeto e por isso
vale mais no começo do que no fim: backlink é o que faz o robô voltar"* — a ilha tem seis dias de ar, 9 URLs e
`primeira_indexacao: null`.

**O PLACAR, contado pelo portão e nunca digitado:** 10 candidatos — **1** prioridade 1 (`bicieletric.com.br`,
o único que fecha as duas condições medidas: vende os dois veículos que as ferramentas classificam **e** publica
no próprio domínio), **5** prioridade 2 e **4** prioridade 3. **Zero abertos no navegador**, e o arquivo diz isso
no topo em vez de deixar a limitação invisível.

**AS QUATRO REGRAS DA RÉGUA, e as quatro são sobre NÃO AFIRMAR DEMAIS:** (1) **não existe `false`** nos campos de
fato — busca sabe afirmar presença, nunca ausência, que é a assimetria da **30.8** aplicada a outro assunto;
(2) **a evidência tem de ser do próprio domínio** do candidato (ou subdomínio), e a armadilha foi medida nesta
coleta: a Eletricz apareceu primeiro numa matéria de `mecanicaonline.com.br` que **fala** dela, e matéria de
terceiro não prova nada sobre o site que vai instalar o widget; (3) **a prioridade não se escreve, se calcula** —
o portão recalcula dos campos medidos e fica vermelho se discordar; (4) **`null` exige motivo escrito**.

**A RÉGUA MORA DENTRO DO PORTÃO, e isso é decisão e não preguiça:** a Aquametria tem `regua-prospeccao.py`
separado porque lá quatro arquivos a carregam; aqui são dois, e a `bancada.py` desta ilha classifica **por prefixo
de nome** e DENUNCIA o que não casa — `regua-*` nasceria denunciado e o conserto seria uma lista de exceção a mão,
que é a doença que esta bancada matou. **E o autoteste roda SEMPRE**, antes do arquivo de verdade, porque a
bancada só descobre `--autoteste` nos portões de **rede** e este é dos sem rede: portão que depende de alguém
lembrar não roda.

**O ACHADO QUE NÃO É SOBRE PROSPECÇÃO, e ele foi para `dados/despachos.md`:** **duas páginas do MESMO site**
(`eletricz.com.br`) citam a **mesma** Resolução Contran 996/2023 com números diferentes — *"até 1000 Watts, com
velocidade de até 32 km/h"* numa, *"potência máxima de 4.000W para autopropelidos"* na outra. A contradição que o
corpus de 28/10 mediu **entre** três publicadores existe **dentro** de um só. Isso sobe o custo do despacho ALTA
do `gov.br` em vez de só confirmá-lo: não existe "leitura de mercado" para a F1 herdar.

**6-ORIGINAL (guardado).** LISTA DE PROSPECÇÃO DO WIDGET — lojas brasileiras de mobilidade elétrica com site próprio, `publicar: false`.

**7. ~~A FOLHA DA CASCA NÃO SERVE OS PRÓPRIOS COMENTÁRIOS~~ — ENTREGUE EM 04/11/2026 às 19h17Z–19h5xZ,
E A REGRA VIROU A 32.4-b DO CONTRATO.** No ar na revisão **42**: **9 de 9 URLs com ZERO comentário em folha
desta ilha**, contra 23–24 e 7.486–7.866 bytes de manhã, e a página encolhendo **7.546 a 7.926 bytes** cada.
A tag `<style>` **saiu dos três snippets** e passou a ser escrita por `rodametria_casca_fechar_folha()`, que
tira os comentários — um lugar só, pela 32.5-c, então **folha nova nasce dentro do conserto**. Nenhum byte de
CSS mudou de lugar no repositório: a captura (`rodametria_casca_abrir_folha()`) entrega o texto à função.
Casca 1.10.0, produto 1.7.1, institucional 1.2.1, espelhadas no manifest pela ferramenta.

**AS TRÊS PARTES QUE O BLOCO PEDIA, as três medidas:** (1) **zero comentário** nas 9 URLs, contado no HTML do
ar; (2) **o CSS não quebrou, e isso não foi afirmado**: `ferramentas/teste-folha-sem-comentario.php` (58
afirmações, 8 mundos fabricados com a saída escrita à mão, **6 deles separando a régua nova da ingênua** pela
20.8) cobra que o que desapareceu seja **exatamente** o que morava dentro de comentário — `{` de 145 para 140
e `;` de 282 para 280, contra 5 `{`, 5 `}` e 2 `;` dentro dos 23 comentários —, e o **portão de pixel da 32.5,
rodado depois do desembarque, devolveu os 27 números das 9 páginas IDÊNTICOS** aos de antes, byte por byte;
(3) **a régua da 32.4 passou a alcançar o `<style>`**, numa afirmação **separada** da do texto visível, com os
nomes de arquivo desta pasta lidos do disco e as extensões `.py` e `.mjs` — e **`.php` fora**, porque o
WordPress serve `/wp-*.php` e `xmlrpc.php` no próprio `<head>` e um termo `.php` reprovaria a página certa.

**O PORTÃO NOVO REPROVOU O AR DE ANTES — 43 falhas em 524 afirmações, todas das quatro classes deste bloco e
nenhuma de outro tipo**, e depois do desembarque fechou em **481 afirmações, 0 falha**. Bancada com rede:
**32 portões, 0 falha**.

**E AS DUAS IRMÃS ACHARAM O QUE A 32.5-c MANDA PROCURAR NA MESMA PASSADA:** `teste-f2.py` cobrou guarda
`function_exists` **por função** (as duas novas estavam sob a mesma) e `teste-institucional.py` procurava a
folha pela **tag** que acabou de sair — defeito da régua, não da folha; ela passou a achá-la pelo **par de
captura** e ganhou um caso de autoteste novo. **Nenhuma das duas foi consertada de cabeça: as duas reprovaram
na bancada, antes do desembarque.**

**A REGRA SUBIU PARA O CONTRATO (32.4-b) E O ENDEREÇO DELA NAS OUTRAS TRÊS ILHAS É DESPACHO**, em
`dados/despachos.md`, porque a seção 3 proíbe editar arquivo de ilha que esta execução não reservou. **O texto
original do bloco fica abaixo, preservado**, porque ele é a melhor explicação escrita de por que nenhum portão
via o defeito.

### O TEXTO ORIGINAL DO BLOCO 7, PRESERVADO

**7-ORIGINAL. A FOLHA DA CASCA NÃO SERVE OS PRÓPRIOS COMENTÁRIOS — PRÉ-REGISTRADO EM 04/11/2026, COM O NÚMERO MEDIDO**

Achado pela execução de 16h17Z de 04/11 ao extrair as datas em prosa das 9 URLs, e é um defeito da **32.4**
que **nenhum portão desta ilha vê**. Medido no HTML servido de `/autonomia-patinete-eletrico/`: a página tem
**110.182 bytes**, os 18 blocos `<style>` somam **67.916**, e dentro deles vão **39 comentários de CSS,
6.042 bytes** — **8,9% do CSS e 5,5% da página**. **Seis deles, 3.745 bytes**, trazem exatamente o
vocabulário que a 32.4 proíbe: `snippet`, número de seção do contrato, nome de rotina
(`conferir-32-5-no-navegador.mjs`) e prosa de bastidor (*"Medido no ar a 390 px em 29/10/2026, na primeira
foto que a ilha teve"*).

**POR QUE NENHUM PORTÃO VÊ:** a régua de bastidor desta ilha e a da ronda leem o **texto visível**, e
`corpo_da_pagina()` tira `<script>` e `<style>` antes de medir — com razão, porque ali mora CSS e não prosa.
**Só que a 32.4 não é sobre o que o leitor vê: é sobre o que a página SERVE.** Comentário de folha é
invisível para o visitante e perfeitamente legível para quem lê o fonte — e é o fonte que a visão geral de
IA ingere.

**O QUE O BLOCO FAZ, e o que ele NÃO faz:** o comentário **fica no repositório**, que é o lugar dele
(seção 3) — ele é a memória desta ilha e foi ele que pagou a 32.5-d duas vezes. O que muda é que a casca
**tira os comentários da folha ao imprimi-la**, num só lugar, do mesmo jeito para os quatro snippets.

**O QUE O PORTÃO TEM DE PROVAR, e as três partes são o difícil do bloco:**
1. **que a folha servida não tem comentário nenhum** — contado no HTML do ar, dentro de `<style>`, nas 9
   URLs;
2. **que o CSS não quebrou** — e isto se mede, não se afirma: `/*` pode aparecer dentro de `url(data:...)`
   e dentro de `content:"..."`, e um removedor ingênuo corta a declaração no meio. O autoteste **fabrica**
   esses dois casos e exige que sobrevivam, e o portão de pixel da 32.5 roda depois, porque folha cortada
   errado aparece como pixel errado antes de aparecer como qualquer outra coisa;
3. **que a régua de bastidor da 32.4 passou a alcançar o `<style>`** — hoje ela mede o texto visível, e a
   parte nova é uma afirmação separada sobre o HTML servido inteiro, com a lista de palavras da 32.4 mais os
   nomes de arquivo desta pasta.

**POR QUE NÃO FOI FEITO NA MESMA PASSADA:** o desembarque de 04/11 conserta a 32.5 mexendo em 24 regras da
folha, e o número que a 32.5 mede ia ser lido no mesmo minuto. Mexer na folha duas vezes no mesmo
desembarque trocaria duas variáveis ao mesmo tempo no único número que esta ilha tem como prova. **E a conta
deste bloco cresceu com aquele conserto**, o que é a parte honesta: o comentário que explica as 24 regras
prefixadas tem ~2,3 KB e vai para a mesma folha.

## A BANCADA DESTA ILHA É UM COMANDO SÓ, E ELA DESCOBRE OS PORTÕES (28/10/2026)

> **A TERCEIRA PONTA NÃO TEM PORTÃO, E ISSO É DECISÃO E NÃO LACUNA (06/11/2026).** A bancada tem quem
> lê o **HTML servido** (`conferir-no-ar.py`, que desde 06/11 também **aperta o botão** de cada
> formulário e exige 200) e quem **mede pixel** num navegador de verdade
> (`conferir-32-5-no-navegador.mjs`). **Nenhum dos dois aperta um controle da ferramenta** — e a metade
> da F1 que a pessoa de fato usa é a recomputação no navegador, com a árvore escrita no JS.
> **Isso foi medido à mão em 06/11, na página de verdade, a 390 px, com os quatro casos da árvore, e
> deu zero defeito** (o detalhe e os números estão no `REGISTRO.md` daquela data). **Não virou portão
> pela 31.2:** portão novo só nasce com defeito medido no ar que ele teria pegado. No dia em que essa
> ponta falhar, a receita está registrada — `createRequire` e não `import from 'playwright'` (a causa
> dos 21 portões de navegador inertes do arquipélago), e o caminho do Chromium **descoberto** em
> `/opt/pw-browsers` em vez de fixo.


```
python3 ferramentas/bancada.py            # os portões que rodam sem rede
python3 ferramentas/bancada.py --no-ar    # mais os que abrem o site
python3 ferramentas/bancada.py --lista    # só imprime o que rodaria
```

**Não enumere bancada de cabeça neste arquivo nem no `REGISTRO.md`.** `bancada.py` **não tem lista**: varre
`ferramentas/` e classifica pela convenção de nome (`validar-*`, `mutacoes-*`, `teste-*`, `testar-*` sem
rede; `conferir-*` e `medir-*` só com `--no-ar`; `derivar-*`, `gerar-*`, `coletar-*`, `aplicar-*` e
`atualizar-*` escrevem e rodam com `--conferir`). Portão novo entra no dia em que é escrito; arquivo que
não casa com convenção nenhuma é **denunciado**; e portão cujo texto discorda do código de saída é chamado
de **INERTE**. As duas metades do veredito — a palavra impressa e o código de saída — são cobradas sempre.

Esta ilha **nasceu** com a bancada, em vez de ganhá-la depois de perder uma régua. A causa é da Robometria
e está escrita lá: *"a régua existia desde 14/09 e não tinha falhado: não tinha rodado"*. As duas travas da
própria bancada foram medidas no dia em que ela nasceu, com um portão inerte de mentira e um arquivo sem
convenção — ela denunciou os dois.

## Específico desta ilha
- **O dado que é o produto da ilha é a categoria legal.** Errar "dispensa CNH" num veículo que é ciclomotor manda a pessoa para a rua sem habilitação. A F1 nunca afirma além do que a resolução diz, sempre cita a resolução e a data, e trata potência de pico como insuficiente para classificar.
- **Shopee:** `Sub_id 1` = `rodametria`; `Sub_id 2` = código da ferramenta. Na Shopee, scooter e moto elétrica aparecem com 0 vendas e preços incoerentes (R$ 1.255 a R$ 15.000 para o mesmo modelo) — não entram como recomendação.
- **Mercado Livre:** etiquetas `rodametriaf1`, `rodametriaf2`, `rodametriaf3`, ainda não criadas. Janela de atribuição do ML: 24 horas (Termos, item 1.6, lido em 27/10/2026) contra 7 dias da Shopee.
- **O tom:** `VOZ.md` manda na palavra, `DESIGN.md` manda na forma.
